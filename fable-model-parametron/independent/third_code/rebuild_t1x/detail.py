"""detail.py <a|c> <ref.npz> <refidx> <noisy.npz>: per run, wrong (pair, slot) list and the spread draw"""
import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
from sim import *
lay = layout_c() if sys.argv[1] == 'c' else layout_a()
ref = np.load(sys.argv[2]); Zr = ref['Z'][int(sys.argv[3])]
d = np.load(sys.argv[4]); Z = d['Z']
for b in range(Z.shape[0]):
    w = np.abs(np.angle(Z[b, :, 1:] * np.conj(Zr[:, 1:]))) > np.pi / 2
    if w.sum() == 0:
        continue
    lst = [(lay.names[n], s + 1) for n, s in zip(*np.where(w))]
    lst.sort(key=lambda x: (x[1], x[0]))
    g = d['g'][b]
    print("run", b, "nwrong", w.sum(), "first slots", sorted(set(s for _, s in lst))[:12])
    print("   ", lst[:40])
    print("    spread g:", np.array2string(g, precision=2), "level of wrong pairs mV:",
          np.array2string(np.abs(Z[b, :, 1:])[w][:10] * 1e3, precision=1))
