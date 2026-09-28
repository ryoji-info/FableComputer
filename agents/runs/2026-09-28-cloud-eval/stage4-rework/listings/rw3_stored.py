# -*- coding: utf-8 -*-
"""Round-3 re-executions from stored data and the released loop model (no new solver runs):
  (1) the stage-1 -> stage-2 floor degradation spans under the rule window (all families and classes, Table 5's rows), peak cav and slot-mode;
  (2) the loaded-drain loop model: lossless junction vs Part I 9.4's reflection bound vs Quanta's |r|^2 <= 11.6 %, both biases, both
      reflection phases, passive and active delivered waves, CW-form G4 of the loaded chain; 08-12's registered decay disagreement;
  (3) first-order continuum estimates of G4 at J = -1 from the (240, 480) rungs;
  (4) Table 1's mean-'1' seed spread at a fixed placement."""
import sys, os, json, math
import numpy as np
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, S); sys.path.insert(0, "/home/user/FableComputer/fable-model-chain")
from cascade_driver import metrics
import regen
A = json.load(open(S + "/analysis.json"))
print("=== (1) floor degradation cell 1 -> stage 2 under the rule window (peak cav; slot-mode drn_h), by family and class")
dp, dm = [], []
for tag, R in sorted(A.items()):
    c1 = R["cell1"]
    for Jk, e in sorted(R["J"].items(), key=lambda kv: -int(kv[0].split("_")[0])):
        if not Jk.endswith("_h"): continue
        g = e["rule"]["chain_over_passive"]; J = int(Jk.split("_")[0])
        d1 = c1["cav"]["max0_below_mean1_dB"] - g["cav"]["max0_below_mean1_dB"]; d2 = c1["floor_mode_drn_h"] - g["floor_mode_drn_h"]
        dp.append((d1, tag, J)); dm.append((d2, tag, J))
        if J >= -6 and not tag.endswith("_Jext"): print(f" {tag:16s} J={J:+d}: peak cav {c1['cav']['max0_below_mean1_dB']:.2f} -> {g['cav']['max0_below_mean1_dB']:.2f} = {d1:.2f} dB; slot-mode {c1['floor_mode_drn_h']:.2f} -> {g['floor_mode_drn_h']:.2f} = {d2:.2f} dB")
t1 = [x for x in dp if x[2] >= -6 and not x[1].endswith("_Jext")]; m1 = [x for x in dm if x[2] >= -6 and not x[1].endswith("_Jext")]
print(f" Table-1 classes (J >= -6): peak cav {min(t1)[0]:.2f} .. {max(t1)[0]:.2f} dB (min {min(t1)[1]} J={min(t1)[2]}, max {max(t1)[1]} J={max(t1)[2]}); slot-mode {min(m1)[0]:.2f} .. {max(m1)[0]:.2f}")
print(f" all Table-5 rows incl. the sweep: peak cav {min(dp)[0]:.2f} .. {max(dp)[0]:.2f}; slot-mode {min(dm)[0]:.2f} .. {max(dm)[0]:.2f}")
print("=== (2) loaded-drain loop model (released regen.loop_gain), in-model")
s, tau, L, Mth, a = regen._cavity(); Mb = 0.11826023624361658
loops = {"ratio bias 0.7*M_th_num(240)": regen.loop_gain(Mb), "analytic bias 0.7*M_th": regen.loop_gain(0.7 * Mth)}; loop0 = regen.loop_gain(0.0)
print(f" a_loss {a:.6f}; loop0 (M=0) {loop0:.4f}; unloaded loops: " + "; ".join(f"{k} {v:.4f}" for k, v in loops.items()) + f"; unloaded CW regen (ratio) {20*math.log10((1-loop0)/(1-loops['ratio bias 0.7*M_th_num(240)'])):+.2f} dB, (analytic) {20*math.log10((1-loop0)/(1-loops['analytic bias 0.7*M_th'])):+.2f} dB")
print(f" 08-12 §3 check: loop {loops['ratio bias 0.7*M_th_num(240)']:.4f} per round trip -> per slot (m=30, 30 rt): {30*20*math.log10(loops['ratio bias 0.7*M_th_num(240)']):.2f} dB/slot; measured -24.38 dB/slot -> effective loop {10**(-24.38/30/20):.4f}; analytic loop -> {30*20*math.log10(loops['analytic bias 0.7*M_th']):.2f} dB/slot")
cases = [("lossless junction, |r|^2 = 1 - 10^(J/10)", lambda J: math.sqrt(1 - 10 ** (J / 10))),
         ("Part I 9.4 bound: reflective loss < 0.1 dB, |r|^2 < 1 - 10^(-0.01)", lambda J: math.sqrt(1 - 10 ** (-0.01))),
         ("Quanta 09-28 budget |r|^2 <= 11.6 %", lambda J: math.sqrt(0.116))]
for J in (-1, -3, -6):
    t = math.sqrt(10 ** (J / 10))
    for name, rf in cases:
        r = rf(J)
        for bk, lp in loops.items():
            for ph, rr in (("r=+|r|", r), ("r=-|r|", -r)):
                loaded = lp * rr; loaded0 = loop0 * rr
                dp_ = 20 * math.log10(abs(t / (1 - a * rr))); da_ = 20 * math.log10(abs(t / (1 - loaded))); sw = 20 * math.log10(abs((1 + rr) / (1 - a * rr)))
                cw = 20 * math.log10(abs((1 - loaded0) / (1 - loaded))); cw_un = 20 * math.log10((1 - loop0) / (1 - lp)); g4cw = (cw + cw_un) / cw_un
                if ph == "r=+|r|" or (J == -1 and "lossless" in name):
                    print(f" J={J:+d} {name[:34]:34s} {bk[:22]:22s} {ph}: |r|={r:.3f} loaded loop {loaded:+.3f}; passive delivered {dp_:+.2f} dB, active delivered {da_:+.2f} dB, drain standing wave {sw:+.2f} dB; loaded CW regen {cw:+.2f} dB (unloaded {cw_un:+.2f}); CW-form G4 of the loaded chain {g4cw:.2f}")
print("=== (3) first-order continuum estimate of G4_A at J=-1 from (240, 480): 2*G(480) - G(240)")
for m in (30, 28):
    g240 = A[f"N240_m{m}_s7"]["J"]["-1_h"]["rule"]["G4_A_worst"]; g480 = A[f"N480_m{m}_s7"]["J"]["-1_h"]["rule"]["G4_A_worst"]
    print(f" m={m}: {g240:.3f} / {g480:.3f} -> {2*g480-g240:.3f}")
print("=== (4) seed spread of the mean-'1' chain gain at a fixed placement (2.625 rt), m=30 N=240 J=-1")
def chain_mean(tag, idx):
    F = json.load(open(f"{S}/runs/{tag}.json")); return metrics(F["bits"], np.array(F["chains"]["J-1_h_MM"]["pk_cav"][idx]), np.array(F["chains"]["J-1_h_00"]["pk_cav"][idx]))
for tag in ("N240_m30_s7", "N240_m30_s11", "N240_m30_s13"):
    r = chain_mean(tag, 21); print(f" {tag}: worst {r['G_worst1_dB']:.4f} mean {r['G_mean1_dB']:.4f}")
