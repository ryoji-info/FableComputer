"""ana_noisy.py <layout a|c> <ref.npz> <noisy.npz> [more noisy...]
Reference member chosen by matching (Vs, p)."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
from collections import Counter
from sim import *

which = sys.argv[1]
lay = layout_c() if which == 'c' else layout_a()
if which == 'c':
    E = expected_c(lay); Ssum = true_sum_bits(lay)
else:
    E = expected_a(lay)
W = np.zeros((lay.N, 32))
for n in lay.drives:
    W[n, 1:] = 2 * E[n, 1:] - 1
ref = np.load(sys.argv[2])
for fn in sys.argv[3:]:
    d = np.load(fn)
    groups = sorted(set(zip(d['Vs'].round(4), d['p'].round(4))))
    for (v, p) in groups:
        k = np.where((ref['Vs'].round(4) == v) & (ref['p'].round(4) == p))[0][0]
        Zr = ref['Z'][k]
        th, _ = axis_and_signs(lay, Zr[None], W, 135.0)
        m = np.where((d['Vs'].round(4) == v) & (d['p'].round(4) == p))[0]
        Z = d['Z'][m]
        dphi = np.angle(Z[:, :, 1:] * np.conj(Zr[None, :, 1:]))
        wrong = np.abs(dphi) > np.pi / 2
        nw = wrong.sum()
        runs_bad = int((wrong.sum(axis=(1, 2)) > 0).sum())
        pc = Counter()
        for n in range(lay.N):
            c = int(wrong[:, n].sum())
            if c:
                pc[lay.names[n]] = c
        extra = ''
        if which == 'c':
            sg = signs_with_theta(lay, Z, np.full(len(m), th[0]), 135.0)
            st = (sg[:, lay.idx['St'], 1:] > 0).astype(int)
            nbad_stream = int((~(st == Ssum[1:][None]).all(axis=1)).sum())
            extra = ' stream_not_sum %d' % nbad_stream
        else:
            extra = ''
        lev = np.abs(Z[:, :, 1:]) * 1e3
        print("%s Vs %.3f p %.2f runs %d wrong %d / %d  runs_with_wrong %d%s  pairs %s  minlev %.1f mV" % (
            fn, v, p, len(m), nw, wrong.size, runs_bad, extra, dict(pc), lev.min()))
