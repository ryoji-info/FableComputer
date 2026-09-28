# -*- coding: utf-8 -*-
"""Round-4 re-execution: the ablation construction Table 9 row (iii) was LABELLED with in round 3 — gate (i)'s 1-rt
raised-cosine '0'-slot cut plus a HARD cut of the '1' slots at 0.8*repT (the round-2 seats' -13.09) — m = 30, N = 240,
seed 7, J = -1, cfl 0.4, from the stored cell-1 series."""
import sys, os, json, time
import numpy as np
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, S); sys.path.insert(0, S + "/rework")
from cascade_driver import *
from rw_runs import load, save, sig, bits, nslots, repT, N, nrt, BIAS
up = load("c1M_cfl0.4"); t = up["t"]; g = np.ones_like(t); cut = 2.0
for k in range(nslots):
    x0 = k * repT
    if bits[k] == 0:
        sel = (t >= x0) & (t < x0 + cut); g[sel] = 0.5 * (1 + np.cos(np.pi * (t[sel] - x0) / cut)); g[(t >= x0 + cut) & (t < x0 + repT)] = 0.0
    else:
        g[(t >= x0 + 0.8 * repT) & (t < x0 + repT)] = 0.0
up2 = dict(up); up2["drn_h"] = up["drn_h"] * g
t0 = time.time(); _, c2 = run_chain(None, BIAS, N, nrt, sig, kappa=10 ** (-1 / 20.0), plane="h", cfl=0.4, up=up2); save("J1_MM_abl_rc0_hard1_cfl0.4", c2)
from rw_cfl import score
gg = score(c2, load("J1_00_cfl0.4"), shift=5.25)
row = {"floor_cav": gg["cav"]["max0_below_mean1_dB"], "floor_drnh": gg["drn_h"]["max0_below_mean1_dB"], "floor_mode": gg["mode"], "chain": gg["cav"]["G_worst1_dB"], "eye": gg["cav"]["eye_dB"]}
CF = json.load(open(S + "/rework/cfl_scan.json")); CF["ablation_rc0_hard1"] = row; json.dump(CF, open(S + "/rework/cfl_scan.json", "w"), indent=1)
print("gate (i) raised-cosine '0' cut + hard '1' cut at 0.8*repT:", {k: round(v, 3) for k, v in row.items()}, round(time.time() - t0, 1), "s", platform_line())
