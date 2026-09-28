# -*- coding: utf-8 -*-
"""Round-2 analysis of rw_runs.py's series: (A) cfl sensitivity at fixed grid (Kinetic R5/R8), (B) the J = -25 chain's
window-placement row (Quanta R1), (C) the gated-input ablation (Quanta T8). m = 30, N = 240, seed 7, ratio bias."""
import sys, os, json, math
import numpy as np
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, S)
from cascade_driver import metrics, floor_mode, slot_windows, slot_peaks, slot_modes, F0N, default_bits
from analyze import envelope_lag
from residue import WINDOWS
OUT = S + "/rework/series"; m, N, seed = 30, 240, 7; repT = 60.0; ns = 40; bits = default_bits(ns, seed).tolist()
def load(tag):
    return {"t": np.load(f"{OUT}/{tag}_t.npy").astype(float), **{o: np.load(f"{OUT}/{tag}_{o}.npy").astype(float) for o in ("cav", "drn_h", "drn_u")}}
def score(cell, ref, lo=0.25, width=0.47, shift=0.0):
    tend = min(cell["t"][-1], ref["t"][-1]); n_ok = sum(1 for k in range(ns) if (k + lo + width) * repT + shift <= tend)
    mk = slot_windows(cell["t"], repT, n_ok, lo, lo + width, shift); mr = slot_windows(ref["t"], repT, n_ok, lo, lo + width, shift)
    out = {o: metrics(bits[:n_ok], slot_peaks(cell[o], mk), slot_peaks(ref[o], mr)) for o in ("cav", "drn_h")}
    a, _ = slot_modes(cell["drn_h"], cell["t"], mk, F0N, repT, 0.8, shift=(lo - 0.25) * repT + shift)
    out["mode"] = floor_mode(bits[:n_ok], a); out["n"] = n_ok - 4; return out
def residue(c):
    t = c["t"]; x = c["drn_h"]; b = np.array(bits)[4:]; ones = b == 1; zeros = b == 0; prev1 = np.array([bits[k - 1] == 1 for k in range(4, ns)])
    pk = lambda lo, hi: np.array([np.max(np.abs(x[(t >= (k + lo) * repT) & (t < (k + hi) * repT)])) for k in range(ns)])[4:]
    ref = np.mean(pk(0.25, 0.72)[ones]); q = pk(0.0, 0.25)
    return 20 * math.log10(np.max(q[zeros & prev1]) / ref), 20 * math.log10(np.max(q[zeros & prev1]) / np.mean(q[ones]))
def peaklag(a, b):
    d = []
    for k in range(4, ns):
        if bits[k] != 1: continue
        sa = (a["t"] >= k * repT) & (a["t"] < (k + 1) * repT); sb = (b["t"] >= k * repT) & (b["t"] < (k + 1) * repT)
        d.append(b["t"][sb][np.argmax(np.abs(b["drn_h"][sb]))] - a["t"][sa][np.argmax(np.abs(a["drn_h"][sa]))])
    return float(np.median(d))
res = {}
print("=== (A) cfl sensitivity at fixed N = 240 (bias held at the released-convention 0.7*M_th_num(240) measured at cfl 0.4)")
for cfl in (0.2, 0.4, 0.8):
    c1M, c10 = load(f"c1M_cfl{cfl}"), load(f"c10_cfl{cfl}"); MM, M0, OO = load(f"J1_MM_cfl{cfl}"), load(f"J1_M0_cfl{cfl}"), load(f"J1_00_cfl{cfl}")
    s1 = score(c1M, c10); ds = max(1, len(c10["t"]) // 20000)
    Lp = envelope_lag(c10["drn_h"][::ds], OO["drn_h"][::ds], c10["t"][::ds]); La = envelope_lag(c1M["drn_h"][::ds], MM["drn_h"][::ds], c1M["t"][::ds])
    pl = peaklag(c10, OO); rule = round(Lp / 0.25) * 0.25          # 1/8-rt grid (0.25 time units)
    b = np.array(bits)[4:]; ones = b == 1
    pas = np.mean(slot_peaks(c10["drn_h"], slot_windows(c10["t"], repT, ns))[4:][ones]); act = np.mean(slot_peaks(c1M["drn_h"], slot_windows(c1M["t"], repT, ns))[4:][ones])
    ra, rb = residue(c1M)
    row = {"cfl": cfl, "dtM": None, "single": s1, "L_passive_units": Lp, "L_active_units": La, "peak_lag_units": pl, "rule_units": rule,
           "passive_transfer_dB": 20 * math.log10(pas / 2e-3), "active_drn_h": act, "residue_a": ra, "residue_b": rb}
    for name, sh in (("rule", rule), ("fixed2625", 5.25), ("unshifted", 0.0)):
        g = score(MM, OO, shift=sh); c = score(MM, M0, shift=sh)
        row[name] = {"shift": sh, "chain": g["cav"]["G_worst1_dB"], "G4_A": g["cav"]["G_worst1_dB"] / s1["cav"]["G_worst1_dB"], "c2c": c["cav"]["G_worst1_dB"],
                     "floor_cav": g["cav"]["max0_below_mean1_dB"], "floor_drnh": g["drn_h"]["max0_below_mean1_dB"], "floor_mode": g["mode"], "eye": g["cav"]["eye_dB"], "n": g["n"]}
    res[f"cfl{cfl}"] = row
    print(f" cfl {cfl}: cell 1 gain {s1['cav']['G_worst1_dB']:.4f}, floors cav {s1['cav']['max0_below_mean1_dB']:.3f} drn_h {s1['drn_h']['max0_below_mean1_dB']:.3f} mode {s1['mode']:.3f}; passive transfer {row['passive_transfer_dB']:.2f} dB; active drn_h {act:.5f}; residue (a) {ra:.2f} / (b) {rb:.2f} dB")
    print(f"        lags: passive env {Lp/2:.3f} rt (rule {rule/2:.3f}), peak {pl/2:.4f} rt; active env {La/2:.3f} rt")
    for name in ("rule", "fixed2625", "unshifted"):
        r = row[name]; print(f"        window {name:9s} shift {r['shift']/2:.3f} rt: chain {r['chain']:.3f} G4_A {r['G4_A']:.3f} c2c {r['c2c']:.3f} | floor cav {r['floor_cav']:.2f} drn_h {r['floor_drnh']:.2f} mode {r['floor_mode']:.2f} | eye {r['eye']:+.2f} (n {r['n']})")
print("=== (B) J = -25 chain (cfl 0.4): window-placement rows")
c1M, c10 = load("c1M_cfl0.4"), load("c10_cfl0.4"); MM, OO = load("J25_MM_cfl0.4"), load("J25_00_cfl0.4"); s1 = score(c1M, c10)
res["J25"] = {}
for lo in (0.25, 0.60, 0.70, 0.77, 0.80, 0.85):
    g = score(MM, OO, lo=lo); res["J25"][str(lo)] = {"chain": g["cav"]["G_worst1_dB"], "G4_A": g["cav"]["G_worst1_dB"] / s1["cav"]["G_worst1_dB"], "floor_cav": g["cav"]["max0_below_mean1_dB"], "floor_drnh": g["drn_h"]["max0_below_mean1_dB"], "floor_mode": g["mode"], "n": g["n"]}
    print(f" lo {lo:.2f}: chain {g['cav']['G_worst1_dB']:.3f} G4_A {g['cav']['G_worst1_dB']/s1['cav']['G_worst1_dB']:.3f} | floor cav {g['cav']['max0_below_mean1_dB']:.2f} drn_h {g['drn_h']['max0_below_mean1_dB']:.2f} mode {g['mode']:.2f} (n {g['n']})")
g = score(MM, OO, shift=5.25); print(f" rule window (2.625 rt): chain {g['cav']['G_worst1_dB']:.3f} G4_A {g['cav']['G_worst1_dB']/s1['cav']['G_worst1_dB']:.3f} floor cav {g['cav']['max0_below_mean1_dB']:.2f} mode {g['mode']:.2f}")
print("=== (C) gated-input ablation (J = -1, cfl 0.4, rule window 2.625 rt): stage-2 floors")
res["ablation"] = {}
for tag, lbl in (("J1_MM_cfl0.4", "no gate"), ("J1_MM_abl_zero_cfl0.4", "'0'-slot residue zeroed (1-rt raised-cosine cut at each '0'-slot start)"), ("J1_MM_abl_duty_cfl0.4", "additionally the '1' slots' post-drive tail [0.8, 1.0]*repT removed")):
    X = load(tag); g = score(X, load("J1_00_cfl0.4"), shift=5.25)
    res["ablation"][lbl] = {"floor_cav": g["cav"]["max0_below_mean1_dB"], "floor_drnh": g["drn_h"]["max0_below_mean1_dB"], "floor_mode": g["mode"], "chain": g["cav"]["G_worst1_dB"], "eye": g["cav"]["eye_dB"]}
    print(f" {lbl}: floor cav {g['cav']['max0_below_mean1_dB']:.3f} drn_h {g['drn_h']['max0_below_mean1_dB']:.3f} mode {g['mode']:.3f}; chain gain {g['cav']['G_worst1_dB']:.3f}; eye {g['cav']['eye_dB']:+.2f}")
json.dump(res, open(S + "/rework/cfl_scan.json", "w"), indent=1)
