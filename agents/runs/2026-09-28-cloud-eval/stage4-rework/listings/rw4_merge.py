# -*- coding: utf-8 -*-
"""Re-score the two hard-cut ablation series and store both under their keys (importing rw_cfl re-runs its whole
analysis as a side effect and had dropped one key), without side effects."""
import sys, os, json
import numpy as np
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, S)
from cascade_driver import metrics, floor_mode, slot_windows, slot_peaks, slot_modes, F0N, default_bits
OUT = S + "/rework/series"; repT = 60.0; ns = 40; bits = default_bits(ns, 7).tolist()
def load(tag):
    return {"t": np.load(f"{OUT}/{tag}_t.npy").astype(float), **{o: np.load(f"{OUT}/{tag}_{o}.npy").astype(float) for o in ("cav", "drn_h")}}
def score(cell, ref, shift=5.25, lo=0.25, width=0.47):
    tend = min(cell["t"][-1], ref["t"][-1]); n_ok = sum(1 for k in range(ns) if (k + lo + width) * repT + shift <= tend)
    mk = slot_windows(cell["t"], repT, n_ok, lo, lo + width, shift); mr = slot_windows(ref["t"], repT, n_ok, lo, lo + width, shift)
    out = {o: metrics(bits[:n_ok], slot_peaks(cell[o], mk), slot_peaks(ref[o], mr)) for o in ("cav", "drn_h")}
    a, _ = slot_modes(cell["drn_h"], cell["t"], mk, F0N, repT, 0.8, shift=shift); out["mode"] = floor_mode(bits[:n_ok], a); return out
ref = load("J1_00_cfl0.4"); CF = json.load(open(S + "/rework/cfl_scan.json"))
for key, tag in (("ablation_hard", "J1_MM_abl_hard_cfl0.4"), ("ablation_rc0_hard1", "J1_MM_abl_rc0_hard1_cfl0.4")):
    g = score(load(tag), ref); CF[key] = {"floor_cav": g["cav"]["max0_below_mean1_dB"], "floor_drnh": g["drn_h"]["max0_below_mean1_dB"], "floor_mode": g["mode"], "chain": g["cav"]["G_worst1_dB"], "eye": g["cav"]["eye_dB"]}
    print(key, {k: round(v, 3) for k, v in CF[key].items()})
json.dump(CF, open(S + "/rework/cfl_scan.json", "w"), indent=1); print("keys:", sorted(CF.keys()))
