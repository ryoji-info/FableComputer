"""task1.py a|b <out.npz> [hdiv]"""
import sys, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
import warnings; warnings.simplefilter("ignore")
from sim import *

part, out = sys.argv[1], sys.argv[2]
hdiv = int(sys.argv[3]) if len(sys.argv) > 3 else 128
lay = layout_single()
if part == 'a':
    Vs = np.round(np.arange(0.90, 1.2001, 0.01), 3); ps = np.zeros_like(Vs); phis = np.zeros_like(Vs)
    t1 = 400.0
elif part == 'b':
    V0 = np.round(np.arange(0.86, 1.0001, 0.02), 3)
    Vs, ps, phis = [], [], []
    for p in (0.10, 0.25):
        for v in V0:
            for j in range(12):
                Vs.append(v); ps.append(p); phis.append(2 * np.pi * j / 12)
    Vs = np.array(Vs); ps = np.array(ps); phis = np.array(phis)
    t1 = 300.0
else:   # step check: one pumped run
    Vs = np.array([0.94]); ps = np.array([0.25]); phis = np.array([0.0]); t1 = 300.0
x0 = dc_state(Vs)[:, None, :]
a = 1e-3
c = a * np.cos(phis); sI = a * np.sin(phis) / (om * Lodd0)
x0[:, 0, 5] += c; x0[:, 0, 6] -= c; x0[:, 0, 7] += c; x0[:, 0, 8] -= c
x0[:, 0, 9] += sI; x0[:, 0, 10] -= sI
h = Tc / hdiv; dec = hdiv // 32
t = time.time()
tr, rec, xf = simulate(lay, Vs, ps, np.zeros((len(Vs), 1)), np.zeros(len(Vs)), 1, h, 0.0, t1, dec, nowin=True, x0=x0)
np.savez(out, t=tr, v=rec[:, :, 0], Vs=Vs, p=ps, phi=phis)
print("done", out, len(Vs), round(time.time() - t, 1), np.all(np.isfinite(rec)))
