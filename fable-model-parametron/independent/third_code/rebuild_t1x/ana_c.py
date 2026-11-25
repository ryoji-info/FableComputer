"""Analyse layout (c) noiseless runs: ana_c.py <npz>"""
import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
from sim import *

lay = layout_c()
E = expected_c(lay)                       # (N,32) labels 0/1
Ssum = true_sum_bits(lay)
# orientation weights: driven depth-0 pairs, +1 where meant 1, -1 where meant 0, slots 1..31
W = np.zeros((lay.N, 32))
for n in lay.drives:
    W[n, 1:] = 2 * E[n, 1:] - 1


def analyse(Z, verbose=True, label=''):
    th, sg = axis_and_signs(lay, Z, W, 135.0)
    out = []
    for b in range(Z.shape[0]):
        lab = (sg[b] > 0).astype(int)
        ok = (lab[:, 1:] == E[:, 1:])
        right = ok.all()
        wrong_pairs = [lay.names[n] for n in range(lay.N) if not ok[n].all()]
        nwrong = (~ok).sum()
        # convention (ii): odd depths flipped
        th2, sg2 = axis_and_signs(lay, Z[b:b + 1], W, -45.0)
        ok2 = ((sg2[0] > 0).astype(int)[:, 1:] == E[:, 1:])
        st = lab[lay.idx['St'], 1:]
        stream_ok = (st == Ssum[1:]).all()
        lev = np.abs(Z[b, :, 1:]) * 1e3
        imin = np.unravel_index(np.argmin(lev), lev.shape)
        out.append(dict(right=right, nwrong=int(nwrong), wrong_pairs=wrong_pairs, right_ii=bool(ok2.all()),
                        stream_ok=bool(stream_ok), minlev=lev[imin], minpair=lay.names[imin[0]], minslot=imin[1] + 1,
                        meanlev=lev.mean(axis=1), theta0=np.rad2deg(th[b])))
    return out


if __name__ == '__main__':
    d = np.load(sys.argv[1])
    Z = d['Z']
    res = analyse(Z)
    print("pairs:", ' '.join(lay.names))
    for b, r in enumerate(res):
        print("Vs %.3f p %.2f right %s (conv ii %s) nwrong %d %s stream_ok %s min %.1f mV at %s slot %d theta0 %.1f" % (
            d['Vs'][b], d['p'][b], r['right'], r['right_ii'], r['nwrong'], r['wrong_pairs'], r['stream_ok'], r['minlev'],
            r['minpair'], r['minslot'], r['theta0']))
        print("   mean levels mV:", ' '.join('%s=%.0f' % (lay.names[n], r['meanlev'][n]) for n in range(lay.N)))
