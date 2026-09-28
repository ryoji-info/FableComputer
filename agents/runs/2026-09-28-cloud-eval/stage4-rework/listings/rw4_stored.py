# -*- coding: utf-8 -*-
"""Round-4 re-executions from stored data: (1) matched-window G4 near the round-spec placements (single cell scored in
the stage-1 window that the pinned convention implies, stage-2 window = stage-1 window + passive lag) on the depth
series; (2) the loaded-drain loop model's full range over J, junction model, phase and bias, and the |r| -> 0 limit;
(3) the passive peak-to-peak latency across all families; (4) the continuum estimate's rounding."""
import sys, os, json, math
import numpy as np
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, S); sys.path.insert(0, S + "/rework"); sys.path.insert(0, "/home/user/FableComputer/fable-model-chain")
from rw_window import load, score
import regen
D = S + "/depth"; A = json.load(open(S + "/analysis.json"))
print("=== (1) matched-window G4 (chain at [lo, lo+0.47] over the single cell at [lo - lag, lo - lag + 0.47]) vs the mixed ratio (single cell at the promoted window)")
out = {}
for tag in ("D_N240_m30_s7", "D_N240_m28_s7"):
    meta = json.load(open(f"{D}/{tag}.json")); bits = meta["bits"]; repT = meta["repT"]; ns = meta["nslots"]; m = int(tag.split("_m")[1].split("_")[0])
    c1M, c10, MM, OO = load(tag, "st1_M"), load(tag, "st1_0"), load(tag, "st2_MM"), load(tag, "st2_00")
    Lp = A[f"N240_m{m}_s7"]["latency"]["env_passive"]; lag_slot = Lp / repT
    s_prom = score(c1M, c10, bits, repT, ns, 0.25)["cav"]["G_worst1_dB"]
    rows = []
    for lo in np.arange(0.74, 0.8301, 0.0025):
        b = score(MM, OO, bits, repT, ns, float(lo)); s = score(c1M, c10, bits, repT, ns, float(lo - lag_slot))
        g = b["cav"]["G_worst1_dB"]; rows.append((float(lo), g / s_prom, g / s["cav"]["G_worst1_dB"], b["cav"]["max0_below_mean1_dB"], s["cav"]["G_worst1_dB"]))
    out[tag] = rows
    ok = [r for r in rows if r[3] <= -10.0]
    print(f" m={m}: passive lag {Lp:.3f} units = {lag_slot:.4f} slot; single-cell gain at promoted window {s_prom:.4f}")
    print(f"   placements with a round-spec stage-2 floor (<= -10 dB): lo {min(r[0] for r in ok):.4f}..{max(r[0] for r in ok):.4f}; mixed G4_A {min(r[1] for r in ok):.3f}..{max(r[1] for r in ok):.3f}; MATCHED G4 {min(r[2] for r in ok):.3f}..{max(r[2] for r in ok):.3f}" if ok else "   no round-spec placement on this grid")
    over = [r for r in rows if r[2] >= 1.7]
    print(f"   matched G4 >= 1.7 at lo {min(r[0] for r in over):.4f}..{max(r[0] for r in over):.4f} with floors {max(r[3] for r in over):.2f}..{min(r[3] for r in over):.2f} dB" if over else "   matched G4 never reaches 1.7 on this grid")
    for r in rows:
        if abs(r[0] - round(r[0] * 40) / 40) < 1e-9 or (0.79 <= r[0] <= 0.82 and m == 28) or (0.76 <= r[0] <= 0.79 and m == 30):
            print(f"   lo {r[0]:.4f}: mixed G4_A {r[1]:.3f}, matched G4 {r[2]:.3f} (single at lo-lag: {r[4]:.3f} dB), stage-2 floor {r[3]:.2f}")
json.dump({k: [list(r) for r in v] for k, v in out.items()}, open(S + "/rework/matched_scan.json", "w"))
print("=== (2) loaded-drain loop model, full range (released regen.loop_gain)")
s_, tau, L, Mth, a = regen._cavity(); loops = {"ratio": regen.loop_gain(0.11826023624361658), "analytic": regen.loop_gain(0.7 * Mth)}; loop0 = regen.loop_gain(0.0)
allv = []
for J in (-1, -3, -6):
    t = math.sqrt(10 ** (J / 10))
    for name, r in (("lossless", math.sqrt(1 - 10 ** (J / 10))), ("9.4 bound", math.sqrt(1 - 10 ** (-0.01))), ("11.6%", math.sqrt(0.116)), ("|r|->0", 0.0)):
        for bk, lp in loops.items():
            for ph in (+1, -1):
                rr = ph * r; dp_ = 20 * math.log10(abs(t / (1 - a * rr))); da_ = 20 * math.log10(abs(t / (1 - lp * rr))); cw = 20 * math.log10(abs((1 - loop0 * rr) / (1 - lp * rr)))
                allv.append((dp_, da_, cw, lp * rr, J, name, bk, ph))
                if J == -1 and bk == "ratio": print(f" J={J:+d} {name:9s} {bk} r={'+' if ph > 0 else '-'}|r|: loaded loop {lp*rr:+.3f}; delivered passive {dp_:+.2f} / active {da_:+.2f} dB; loaded CW regen {cw:+.2f} dB")
print(f" full range over J in {{-1,-3,-6}} x 3 junction models x 2 phases x 2 biases: passive delivered {min(v[0] for v in allv):+.2f} .. {max(v[0] for v in allv):+.2f} dB; active {min(v[1] for v in allv):+.2f} .. {max(v[1] for v in allv):+.2f} dB; loaded loop {min(v[3] for v in allv):+.3f} .. {max(v[3] for v in allv):+.3f}")
j1 = [v for v in allv if v[4] == -1]; print(f" J=-1 only, both phases: passive delivered {min(v[0] for v in j1):+.2f} .. {max(v[0] for v in j1):+.2f} dB; open-end phase only: {min(v[0] for v in j1 if v[7] > 0):+.2f} .. {max(v[0] for v in j1 if v[7] > 0):+.2f} dB")
print("=== (3) passive peak-to-peak stage latency across all families (rt)")
for tag, R in sorted(A.items(), key=lambda kv: (kv[1]["N"], kv[1]["m"], kv[1]["seed"])):
    print(f" {tag:16s} N={R['N']} peak passive {R['latency']['peak_passive']/2:.4f} rt (excess over 0.5: {R['latency']['peak_passive']/2-0.5:.4f})")
print("=== (4) continuum estimate rounding: 2*1.5028-1.5810 =", 2 * A["N480_m30_s7"]["J"]["-1_h"]["rule"]["G4_A_worst"] - A["N240_m30_s7"]["J"]["-1_h"]["rule"]["G4_A_worst"], "; m28:", 2 * A["N480_m28_s7"]["J"]["-1_h"]["rule"]["G4_A_worst"] - A["N240_m28_s7"]["J"]["-1_h"]["rule"]["G4_A_worst"])
