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
print("Definition A (defended): both chain and single cell over their identical passive twins (the promoted gain convention), `cav` observable, worst-'1' statistic; mean-'1' in the second column. Definition B: absolute drain-density gain over the 2×10⁻³ launch amplitude, mean-'1'. Seed-7 value [min, max over seeds 7/11/13] at N = 240.\n")
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
print("\n### Table 2b — boundary-driven single-cell gain ladder G(A), same convention (seed 7)\n")
print("| m | N | A | G worst / mean (dB) | floor (dB) | pp (dB) |")
print("|---|---|---|---|---|---|")
lad = [r for r in T2 if r["kind"] == "ladder"]
for r in sorted(lad, key=lambda r: (r["N"], -r["m"], r["amp"])):
    print(f"| {r['m']} | {r['N']} | {r['amp']:.4f} | {r['cav']['G_worst1_dB']:.3f} / {r['cav']['G_mean1_dB']:.3f} | {r['cav']['max0_below_mean1_dB']:.3f} | {r['cav']['pp_raw_dB']:.3f} |")

print("\n### Table 3 — stage by stage (J = −1 dB, density plane, seed 7, N = 240): gain over the passive twin chain, the stage cell's gain on its real input, '0'-floor in both denominations, '1' pp, eye, latency\n")
if os.path.exists(S + "/analysis_depth.json"):
    Dp = json.load(open(S + "/analysis_depth.json"))
    print("| m | stage | window shift (rt) | chain/passive worst / mean (dB) | stage cell worst / mean (dB) | floor peak `cav` / `drn_h` (dB) | floor slot-mode `drn_h` (dB) | '1' pp (dB) | eye (dB) | mean-'1' drain density |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for tag, D in sorted(Dp.items(), key=lambda kv: -int(kv[0].split("_m")[1].split("_")[0])):
        m = int(tag.split("_m")[1].split("_")[0])
        for k, ent in sorted(D["stages"].items(), key=lambda kv: int(kv[0])):
            g = ent["rule"]["chain_over_passive"] if "chain_over_passive" in ent["rule"] else ent["rule"]
            c = ent["rule"].get("cell_on_real_input", g)
            sh = ent["rule"].get("shift", 0.0)
            print(f"| {m} | {k} | {sh/2:.2f} | {g['cav']['G_worst1_dB']:.3f} / {g['cav']['G_mean1_dB']:.3f} | {c['cav']['G_worst1_dB']:.3f} / {c['cav']['G_mean1_dB']:.3f} | {g['cav']['max0_below_mean1_dB']:.2f} / {g['drn_h']['max0_below_mean1_dB']:.2f} | {g['floor_mode_drn_h']:.2f} | {g['cav']['pp_raw_dB']:.3f} | {g['cav']['eye_dB']:+.2f} | {g['drn_h']['mean1_level']:.4f} |")

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
for tag, R in sorted(A.items(), key=lambda kv: (kv[1]["N"], -kv[1]["m"], kv[1]["seed"])):
    if tag.endswith("_Jext"): continue
    e = R["J"].get("-1_h"); L = R["latency"]
    if e is None: continue
    print(f"| {R['m']} | {R['N']} | {R['seed']} | {e['rule']['passive_transfer_stage1_dB']:.2f} | {e['rule']['passive_transfer_stage2_dB']:.2f} | {L['peak_passive']/2:.3f} / {L['env_passive']/2:.3f} | {L['peak_active']/2:.3f} / {L['env_active']/2:.3f} | {L['rule_rt']:.3f} rt, {L['rule_ps']:.3f} ps, {L['rule_frac_slot']:.3f} |")
