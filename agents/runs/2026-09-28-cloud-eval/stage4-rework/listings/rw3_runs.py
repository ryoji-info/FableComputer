# -*- coding: utf-8 -*-
"""Round-3 re-execution: the ablation gate (ii) as a HARD cut at 0.8*repT (Kinetic T10 / Quanta RE11), m = 30, N = 240,
seed 7, J = -1, cfl 0.4, from the stored round-2 cell-1 series (rework/series/c1M_cfl0.4)."""
import sys, os, json, time
import numpy as np
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, S)
from cascade_driver import *
sys.path.insert(0, S + "/rework")
from rw_runs import load, save, sig, bits, nslots, repT, N, nrt, BIAS
up = load("c1M_cfl0.4"); t = up["t"]; g = np.ones_like(t)
for k in range(nslots):
    x0 = k * repT
    if bits[k] == 0: g[(t >= x0) & (t < x0 + repT)] = 0.0
    else: g[(t >= x0 + 0.8 * repT) & (t < x0 + repT)] = 0.0
up2 = dict(up); up2["drn_h"] = up["drn_h"] * g
t0 = time.time(); _, c2 = run_chain(None, BIAS, N, nrt, sig, kappa=10 ** (-1 / 20.0), plane="h", cfl=0.4, up=up2); save("J1_MM_abl_hard_cfl0.4", c2)
print("hard-cut ablation run done", round(time.time() - t0, 1), "s", platform_line())
