# -*- coding: utf-8 -*-
"""Round-2 re-execution of Quanta R1/R2/T1-T3: window-placement dependence of the stage-2 floor and G4_A,
from the depth run's stored series (J = -1, N = 240, seed 7, cfl 0.4; m = 30 and 28). Window [lo, lo + 0.47]*repT,
same width as the promoted window; fully windowed slots only (a slot whose window runs past the record is dropped).
G4_A = chain worst-'1' dB over passive twin chain (at the scanned window) / single-cell worst-'1' dB (promoted window)."""
import sys, os, json, math
import numpy as np
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, S)
from cascade_driver import metrics, floor_mode, slot_windows, slot_peaks, slot_modes, F0N
D = S + "/depth"
def load(tag, st):
    return {"t": np.load(f"{D}/{tag}_{st}_t.npy").astype(float), **{o: np.load(f"{D}/{tag}_{st}_{o}.npy").astype(float) for o in ("cav", "drn_h")}}
def score(cell, ref, bits, repT, ns, lo, width=0.47):
    tend = min(cell["t"][-1], ref["t"][-1]); n_ok = sum(1 for k in range(ns) if (k + lo + width) * repT <= tend)
    mk = slot_windows(cell["t"], repT, n_ok, lo, lo + width); mr = slot_windows(ref["t"], repT, n_ok, lo, lo + width)
    out = {o: metrics(bits[:n_ok], slot_peaks(cell[o], mk), slot_peaks(ref[o], mr)) for o in ("cav", "drn_h")}
    a, _ = slot_modes(cell["drn_h"], cell["t"], mk, F0N, repT, 0.8, shift=(lo - 0.25) * repT)
    out["mode"] = floor_mode(bits[:n_ok], a); out["n"] = n_ok - 4; return out
LOS = [0.25, 0.30, 0.40, 0.50, 0.58, 0.60, 0.70, 0.75, 0.77, 0.80, 0.85]
res = {}
for tag in ("D_N240_m30_s7", "D_N240_m28_s7"):
    meta = json.load(open(f"{D}/{tag}.json")); bits = meta["bits"]; repT = meta["repT"]; ns = meta["nslots"]; m = int(tag.split("_m")[1].split("_")[0])
    c1M, c10, MM, OO = load(tag, "st1_M"), load(tag, "st1_0"), load(tag, "st2_MM"), load(tag, "st2_00")
    s1 = score(c1M, c10, bits, repT, ns, 0.25)["cav"]["G_worst1_dB"]
    # '1'-peak position within the slot (median over '1' slots after drop 4), cell 1 and stage 2
    def peakpos(c):
        pos = []
        for k in range(4, ns):
            if bits[k] != 1: continue
            sel = (c["t"] >= k * repT) & (c["t"] < (k + 1) * repT); pos.append((c["t"][sel][np.argmax(np.abs(c["cav"][sel]))] - k * repT) / repT)
        return float(np.median(pos))
    print(f"=== {tag}: single-cell worst-'1' cav gain (promoted window) {s1:.4f}; '1'-peak position in slot: cell 1 {peakpos(c1M):.3f}, stage 2 {peakpos(MM):.3f}")
    print("  lo   | cell 1 alone: floor cav / drn_h / mode (n) | stage 2 chain: worst gain, G4_A | floor cav / drn_h / mode (n) | eye")
    rows = []
    for lo in LOS:
        a = score(c1M, c10, bits, repT, ns, lo); b = score(MM, OO, bits, repT, ns, lo)
        g = b["cav"]["G_worst1_dB"]; g4 = g / s1
        rows.append({"lo": lo, "cell1": {"cav": a["cav"]["max0_below_mean1_dB"], "drn_h": a["drn_h"]["max0_below_mean1_dB"], "mode": a["mode"], "n": a["n"]},
                     "stage2": {"gain": g, "G4_A": g4, "cav": b["cav"]["max0_below_mean1_dB"], "drn_h": b["drn_h"]["max0_below_mean1_dB"], "mode": b["mode"], "eye": b["cav"]["eye_dB"], "n": b["n"]}})
        print(f"  {lo:.2f} | {a['cav']['max0_below_mean1_dB']:7.2f} / {a['drn_h']['max0_below_mean1_dB']:7.2f} / {a['mode']:7.2f} ({a['n']}) | {g:.3f}, {g4:.3f} | {b['cav']['max0_below_mean1_dB']:7.2f} / {b['drn_h']['max0_below_mean1_dB']:7.2f} / {b['mode']:7.2f} ({b['n']}) | {b['cav']['eye_dB']:+.2f}")
    res[tag] = {"single_gain": s1, "rows": rows, "peakpos_cell1": peakpos(c1M), "peakpos_stage2": peakpos(MM)}
json.dump(res, open(S + "/rework/window_scan.json", "w"), indent=1)
