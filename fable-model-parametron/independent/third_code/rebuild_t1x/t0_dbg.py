import sys, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
import warnings; warnings.simplefilter("ignore")
from sim import *

for lay, nm in [(layout_single(), 'single'), (layout_c(), 'c')]:
    res = {}
    for h in [Tc / 64, Tc / 128, Tc / 256]:
        t = time.time()
        tr, rec, xf = simulate(lay, np.array([0.94]), np.array([0.25]), np.zeros((1, lay.N)), np.zeros(1), 1, h, -2.0, 60.0, int(round(Tc / 32 / h)))
        Z = read_slots(lay, tr, rec, 3)
        res[h] = Z
        print(nm, h, "time", round(time.time() - t, 1), "finite", np.all(np.isfinite(rec)))
        print(np.array2string(np.abs(Z[0, :, 1]) * 1e3, precision=1))
        print(np.array2string(np.angle(Z[0, :, 1], deg=True), precision=1))
