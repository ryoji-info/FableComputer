# -*- coding: utf-8 -*-
"""Score the hard-cut ablation (rw3_runs.py) at the rule window and add it to cfl_scan.json."""
import sys, os, json
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, S); sys.path.insert(0, S + "/rework")
from rw_cfl import load, score
X = load("J1_MM_abl_hard_cfl0.4"); ref = load("J1_00_cfl0.4"); g = score(X, ref, shift=5.25)
row = {"floor_cav": g["cav"]["max0_below_mean1_dB"], "floor_drnh": g["drn_h"]["max0_below_mean1_dB"], "floor_mode": g["mode"], "chain": g["cav"]["G_worst1_dB"], "eye": g["cav"]["eye_dB"]}
print("hard cut at 0.8*repT (and every '0' slot zeroed):", {k: round(v, 3) for k, v in row.items()})
CF = json.load(open(S + "/rework/cfl_scan.json")); CF["ablation_hard"] = row; json.dump(CF, open(S + "/rework/cfl_scan.json", "w"), indent=1)
