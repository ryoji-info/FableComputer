# -*- coding: utf-8 -*-
"""Render the reply's tables (GitHub markdown) from analysis.json, analysis_depth.json,
table2.jsonl. Seeds at N = 240 are shown as seed-7 value with the min–max spread over
seeds 7/11/13 in brackets."""
import json, os, glob, math
import numpy as np
S = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(S + "/analysis.json"))
GHZ = {28: 71.4, 30: 66.7}


def fams(m, N):
    return {tag: R for tag, R in A.items() if R["m"] == m and R["N"] == N and not tag.endswith("_Jext")}


def val(R, J, path, sname="rule"):
    e = R["J"].get(f"{J}_h");
    if e is None: return None
    x = e[sname]
    for p in path: x = x[p]
    return x


def cell(m, N, J, path, fmt="{:.3f}", sname="rule"):
    F = fams(m, N)
    if not F: return "—"
    vals = {R["seed"]: val(R, J, path, sname) for R in F.values()}
    if any(v is None for v in vals.values()): return "—"
    v7 = vals.get(7, list(vals.values())[0])
    if len(vals) > 1:
        return fmt.format(v7) + " [" + fmt.format(min(vals.values())) + ", " + fmt.format(max(vals.values())) + "]"
    return fmt.format(v7)


print("### Table 1 — two-cell G4 ratio (chain dB over single-cell dB), density-plane coupling, ratio bias, duty-0.8 gated launch, window rule shift = passive-chain latency\n")
print("Definition A (defended): both chain and single cell over their identical passive twins (the promoted gain convention), `cav` observable, worst-'1' statistic; mean-'1' in the second column. Definition B: absolute drain-density gain over the 2×10⁻³ launch amplitude, mean-'1'. Seed-7 value [min, max over seeds 7/11/13, each at its own rule placement — the ⅛-rt window-rule envelope, not pattern dependence: at a fixed placement the three seeds give identical worst-'1' chains to ≤ 0.001 dB (mean-'1' to ≤ 0.05 dB)] at N = 240.\n")
print("| m (GHz) | N | J (dB) | G_single worst (dB) | G_chain^A worst (dB) | **G4_A worst** | G4_A mean | G4_A (`drn_h`) | G4_B | chain worst, unshifted window |")
print("|---|---|---|---|---|---|---|---|---|---|")
for N in (240, 480, 720):
    for m in (30, 28):
        F = fams(m, N)
        if not F: continue
        R7 = next((R for R in F.values() if R["seed"] == 7), list(F.values())[0])
        for J in (0, -1, -3, -6):
            if f"{J}_h" not in R7["J"]: continue
            print(f"| {m} ({GHZ[m]}) | {N} | {J:+d} | {cell(m,N,J,['chain_over_passive','cav','G_worst1_dB'],'{:.3f}') if False else R7['cell1']['cav']['G_worst1_dB']:.4f} | {cell(m,N,J,['chain_over_passive','cav','G_worst1_dB'])} | **{cell(m,N,J,['G4_A_worst'])}** | {cell(m,N,J,['G4_A_mean'])} | {cell(m,N,J,['G4_A_drnh_worst'])} | {cell(m,N,J,['G4_B_mean'])} | {cell(m,N,J,['chain_over_passive','cav','G_worst1_dB'],'{:.3f}','unshifted')} |")

print("\n### Table 2a — cell 2 on its real input vs the boundary-driven single cell at the MATCHED amplitude (signed Δ = cell-to-cell − boundary-driven), `cav`, worst-'1' / mean-'1'\n")
T2 = [json.loads(l) for l in open(S + "/table2.jsonl")] if os.path.exists(S + "/table2.jsonl") else []
T2 += [json.loads(l) for l in open(S + "/table2_480m28.jsonl")] if os.path.exists(S + "/table2_480m28.jsonl") else []
print("| m | N | seed | J (dB) | input amp A* (drain density × κ) | c2c worst / mean (dB) | boundary-driven G(A*) worst / mean (dB) | **Δ worst / mean (dB)** | G at 2×10⁻³ (promoted row) |")
print("|---|---|---|---|---|---|---|---|---|")
for r in sorted([r for r in T2 if r["kind"] == "matched"], key=lambda r: (r["N"], -r["m"], r["seed"], -r["J"])):
    R = A.get(r["tag"]);
    if R is None: continue
    e = R["J"].get(f"{r['J']}_h")
    if e is None: continue
    c = e["rule"]["cell2_on_real_input"]["cav"]
    print(f"| {r['m']} | {r['N']} | {r['seed']} | {r['J']:+d} | {r['amp']:.5f} | {c['G_worst1_dB']:.3f} / {c['G_mean1_dB']:.3f} | {r['cav']['G_worst1_dB']:.3f} / {r['cav']['G_mean1_dB']:.3f} | **{c['G_worst1_dB']-r['cav']['G_worst1_dB']:+.3f} / {c['G_mean1_dB']-r['cav']['G_mean1_dB']:+.3f}** | {R['cell1']['cav']['G_worst1_dB']:.4f} |")
print("\n### Table 2b — boundary-driven single-cell gain ladder G(A): the single released cell driven at its source clamp by the duty-0.8 gated launch at amplitude A, over its identical passive twin, promoted window, ratio bias, cfl = 0.4, seed 7\n")
print("| m | N | A | G worst / mean (dB) | floor (dB) | pp (dB) |")
print("|---|---|---|---|---|---|")
lad = [r for r in T2 if r["kind"] == "ladder"]
for r in sorted(lad, key=lambda r: (r["N"], -r["m"], r["amp"])):
    print(f"| {r['m']} | {r['N']} | {r['amp']:.4f} | {r['cav']['G_worst1_dB']:.3f} / {r['cav']['G_mean1_dB']:.3f} | {r['cav']['max0_below_mean1_dB']:.3f} | {r['cav']['pp_raw_dB']:.3f} |")

print("\n### Table 3 — stage by stage (J = −1 dB, density plane, seed 7, N = 240). Window rule: the promoted window delayed by (k − 1) × the passive twin chain's stage-1→2 envelope lag (5.136 units = 2.568 rt at m = 30; 5.111 = 2.556 rt at m = 28), applied exactly and **without a cap**: at stage 5 the delay is 0.34 slot, so the window runs into the following slot's time (the wave-pipelining reading of a cascade); slots whose delayed window would run past the record's end are dropped and the scored count is shown. Columns: gain over the passive twin chain; the stage cell's gain on its real input; '0'-floor in both denominations; '1' pp; eye; the stage's mean-'1' drain density (h − 1; the shallow-water equilibrium is h = 1); and the measured stage-(k − 1)→k latency — on the passive twin chain by envelope cross-correlation and by per-slot peak time, on the active chain by envelope\n")
if os.path.exists(S + "/analysis_depth.json"):
    Dp = json.load(open(S + "/analysis_depth.json"))
    print("| m | stage k | window shift (rt) | slots scored | lag (k − 1)→k: passive env / peak; active env (rt) | chain/passive worst / mean (dB) | stage cell on real input, worst / mean (dB) | floor peak `cav` / `drn_h` (dB) | floor slot-mode `drn_h` (dB) | '1' pp (dB) | eye (dB) | mean-'1' drain density |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    order = sorted(Dp.items(), key=lambda kv: -int(kv[0].split("_m")[1].split("_")[0]))
    for tag, D in order:
        m = int(tag.split("_m")[1].split("_")[0])
        for k, ent in sorted(D["stages"].items(), key=lambda kv: int(kv[0])):
            k = int(k); r = ent["rule"]
            if k == 1:
                g = r; ccell = "—"; sh = 0.0; lag = "—"; n = r.get("n_scored", 36)
            else:
                g = r["chain_over_passive"]; c = r["cell_on_real_input"]; sh = r["shift"]; L = D["stage_lags"][str(k)]
                lag = f"{L['passive_env']/2:.3f} / {L['passive_peak']/2:.3f}; {L['active_env']/2:.3f}"; n = g.get("n_scored")
                ccell = "n/a (record truncated at the solver's blow-up guard: the passive stage-5 twin driven by the active chain)" if c.get("note") else f"{c['cav']['G_worst1_dB']:.3f} / {c['cav']['G_mean1_dB']:.3f}"
            print(f"| {m} | {k} | {sh/2:.2f} | {n} | {lag} | {g['cav']['G_worst1_dB']:.3f} / {g['cav']['G_mean1_dB']:.3f} | {ccell} | {g['cav']['max0_below_mean1_dB']:.2f} / {g['drn_h']['max0_below_mean1_dB']:.2f} | {g['floor_mode_drn_h']:.2f} | {g['cav']['pp_raw_dB']:.3f} | {g['cav']['eye_dB']:+.2f} | {g['drn_h']['mean1_level']:.4f} |")
    print("\n#### Table 3b — window-placement sensitivity of Table 3 (same runs; `cav`, chain over the passive twin chain): the rule above, the unshifted promoted window, and the window delayed by (k − 1) × the *active* chain's stage-1→2 envelope lag (11.42 units = 5.71 rt at m = 30; 11.53 = 5.77 rt at m = 28), also uncapped\n")
    print("| m | stage k | rule shift (rt): worst (dB) / floor `cav` (dB) / eye (dB) | unshifted window: worst / floor / eye | active-lag shift (rt) [slots scored]: worst / floor / eye |")
    print("|---|---|---|---|---|")
    for tag, D in order:
        m = int(tag.split("_m")[1].split("_")[0])
        for k, ent in sorted(D["stages"].items(), key=lambda kv: int(kv[0])):
            if int(k) == 1: continue
            r, u, a = (ent[n]["chain_over_passive"] for n in ("rule", "unshifted", "active_lag"))
            f = lambda g: f"{g['cav']['G_worst1_dB']:.3f} / {g['cav']['max0_below_mean1_dB']:.2f} / {g['cav']['eye_dB']:+.2f}"
            print(f"| {m} | {k} | {ent['rule']['shift']/2:.2f}: {f(r)} | {f(u)} | {ent['active_lag']['shift']/2:.2f} [{a.get('n_scored')}]: {f(a)} |")
    lp = {int(t.split("_m")[1].split("_")[0]): D for t, D in Dp.items()}
    print(f"\nStage-1→2 lags (Table 3 runs): passive envelope {lp[30]['L_passive']:.3f} units ({lp[30]['L_passive']/2:.3f} rt, {lp[30]['L_passive']/2*RT_PS if False else lp[30]['L_passive']/2*0.5:.3f} ps, {lp[30]['L_passive']/60:.3f} slot) at m = 30 and {lp[28]['L_passive']:.3f} ({lp[28]['L_passive']/2:.3f} rt, {lp[28]['L_passive']/2*0.5:.3f} ps, {lp[28]['L_passive']/56:.3f} slot) at m = 28; active {lp[30]['L_active']:.2f} / {lp[28]['L_active']:.2f} units ({lp[30]['L_active']/2:.2f} / {lp[28]['L_active']/2:.2f} rt). The later stages' lags are in the table; they belong to the out-of-regime stages and are not registered.")

print("\n### Junction sweep (primary rungs, N = 240, seed 7): where the chain returns to the small-signal limit\n")
print("| m | J (dB) | κ | input amp to cell 2 | c2c worst / mean (dB) | G4_A worst / mean | stage-2 floor peak `cav` / slot-mode (dB) | eye (dB) |")
print("|---|---|---|---|---|---|---|---|")
for m in (30, 28):
    for tag, R in A.items():
        if R["m"] != m or R["N"] != 240 or R["seed"] != 7: continue
        for J in (0, -1, -3, -6, -10, -15, -20, -25):
            e = R["J"].get(f"{J}_h")
            if e is None: continue
            r = e["rule"]; c = r["cell2_on_real_input"]["cav"]; g = r["chain_over_passive"]
            print(f"| {m} | {J:+d} | {10**(J/20):.4f} | {r['mean1_in_cell2']:.5f} | {c['G_worst1_dB']:.3f} / {c['G_mean1_dB']:.3f} | {r['G4_A_worst']:.3f} / {r['G4_A_mean']:.3f} | {g['cav']['max0_below_mean1_dB']:.2f} / {g['floor_mode_drn_h']:.2f} | {g['cav']['eye_dB']:+.2f} |")

print("\n### Passive port-to-port density transfer and latency\n")
print("| m | N | seed | T_passive stage 1 (dB, drain density over launch) | T_passive stage 2 (dB) | latency passive: peak-time / envelope (rt) | latency active: peak-time / envelope (rt) | rule shift (rt, ps, slot fraction) |")
print("|---|---|---|---|---|---|---|---|")
for tag, R in sorted(A.items(), key=lambda kv: (kv[1]["N"], -kv[1]["m"], kv[1]["seed"], kv[0].endswith("_Jext"))):
    e = next((R["J"][k] for k in ("-1_h", "-3_h", "-10_h") if k in R["J"]), None); L = R["latency"]
    if e is None: continue
    print(f"| {R['m']}{' (junction sweep)' if tag.endswith('_Jext') else ''} | {R['N']} | {R['seed']} | {e['rule']['passive_transfer_stage1_dB']:.2f} | {e['rule']['passive_transfer_stage2_dB']:.2f} | {L['peak_passive']/2:.3f} / {L['env_passive']/2:.3f} | {L['peak_active']/2:.3f} / {L['env_active']/2:.3f} | {L['rule_rt']:.3f} rt, {L['rule_ps']:.3f} ps, {L['rule_frac_slot']:.3f} |")


print("\n### Residue — what the next cell actually receives (cell 1's active drain density h[−1] − 1, seed 7, N = 240; a '0' slot that follows a '1' carries that '1's ring-down, one that follows a '0' does not). Denominators, named per column: **(a)** = the mean-'1' drain-density peak inside the promoted window [0.25, 0.72]·repT — the denominator of 08-02 §3.2's `drn_h` floor column (not of the promoted `max0_below_mean1_dB`, which is a source-plane `cav` ratio); **(b)** = the mean-'1' peak inside the same sub-window (same phase of the slot, where the '1' is still ringing up). Computed by `residue.py`\n")
import residue as RS
print("| m | promoted window [0.25, 0.72]·repT, over (a) | first quarter [0, 0.25]·repT, over (a) | first quarter, over (b) | whole slot, over (a) | whole slot, over (b) | '0'-slot energy over mean '1'-slot energy (max / median) | cell 2's windowed stage-2 floor at J = −1, `drn_h` / `cav` (Table 5) |")
print("|---|---|---|---|---|---|---|---|")
for tag in ("D_N240_m30_s7", "D_N240_m28_s7"):
    r = RS.compute(tag); m = int(tag.split("_m")[1].split("_")[0]); W = r["windows"]
    fl = next(R for t, R in A.items() if R["m"] == m and R["N"] == 240 and R["seed"] == 7 and not t.endswith("_Jext"))["J"]["-1_h"]["rule"]["chain_over_passive"]
    q = W["first quarter"]; w = W["whole slot"]; pw = W["promoted window"]
    print(f"| {m} | {pw['after1_over_a_dB']:.2f} dB (after a '1'); {pw['after0_over_a_dB']:.1f} (after a '0') | **{q['after1_over_a_dB']:.2f} dB**; {q['after0_over_a_dB']:.1f} | {q['after1_over_b_dB']:.2f} dB; {q['after0_over_b_dB']:.1f} | {w['after1_over_a_dB']:.2f} dB; {w['after0_over_a_dB']:.1f} | {w['after1_over_b_dB']:.2f} dB; {w['after0_over_b_dB']:.1f} | {r['energy_max_dB']:.1f} / {r['energy_median_dB']:.1f} dB | {fl['drn_h']['max0_below_mean1_dB']:.2f} / {fl['cav']['max0_below_mean1_dB']:.2f} dB |")
print("\nThe first-quarter and whole-slot columns agree under denominator (a) because the '0' slot's un-windowed maximum sits at ≈ 0.01 slot, inside the first quarter; the registered key `zero_slot_residue_unwindowed_dB` is the bold column.")

# ---------------- per-table files for the finalizer ----------------
import io, contextlib
def capture(fn):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn()
    return buf.getvalue()

def table5():
    print("| m | N | seed | J (dB) | stage-2 floor, peak `cav` (dB) | peak `drn_h` (dB) | slot-mode `drn_h` (dB) | '1' pp (dB) | eye (dB) | cell-1 floor peak `cav` / slot-mode (dB) |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for tag, R in sorted(A.items(), key=lambda kv: (kv[1]["N"], -kv[1]["m"], kv[1]["seed"], kv[0].endswith("_Jext"))):
        for Jk, ent in sorted(R["J"].items(), key=lambda kv: -int(kv[0].split("_")[0])):
            J, plane = Jk.split("_")
            if plane != "h": continue
            g = ent["rule"]["chain_over_passive"]
            print(f"| {R['m']} | {R['N']} | {R['seed']} | {int(J):+d} | {g['cav']['max0_below_mean1_dB']:.2f} | {g['drn_h']['max0_below_mean1_dB']:.2f} | {g['floor_mode_drn_h']:.2f} | {g['cav']['pp_raw_dB']:.3f} | {g['cav']['eye_dB']:+.2f} | {R['cell1']['cav']['max0_below_mean1_dB']:.2f} / {R['cell1']['floor_mode_drn_h']:.2f} |")

print("\n### Table 5 — stage-2 '0'-floors, every family and class, both denominations, with cell 1's own floor (window rule shift = passive-chain latency, rounded to the ⅛-rt grid; the ideal-buffer density coupling of §2; released cfl = 0.4; the cell-1 columns at the promoted window)\n")
table5()
full = open(S + "/tables.md").read() if os.path.exists(S + "/tables.md") else ""
