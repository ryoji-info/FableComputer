import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
from sim import *
lay = layout_a(); E = expected_a(lay)
W = np.zeros((16, 32)); W[0, 1:] = 2 * E[0, 1:] - 1
d = np.load(sys.argv[1]); Z = d['Z']
th, sg = axis_and_signs(lay, Z, W, 135.0)
for b in range(Z.shape[0]):
    lab = (sg[b] > 0).astype(int)
    ok = lab[:, 1:] == E[:, 1:]
    badp = [n for n in range(16) if not ok[n].all()]
    # per-pair: always inverted?
    inv = [n for n in range(16) if (~ok[n]).all()]
    lev = np.abs(Z[b, :, 1:]) * 1e3
    _, sg2 = axis_and_signs(lay, Z[b:b + 1], W, -45.0)
    ok2 = ((sg2[0] > 0).astype(int)[:, 1:] == E[:, 1:]).all()
    # phase offset of each pair from its axis (deg)
    dd = np.angle(Z[b, :, 1:] * np.exp(-1j * (th[b] + np.deg2rad(135) * lay.depth[:, None])), deg=True)
    off = np.abs(((dd + 90) % 180) - 90).max()
    print("Vs %.3f right %s (ii %s) wrong pairs %s inverted %s nwrong %d | P14 mean %.1f min %.1f mV | P15 mean %.1f | P1 mean %.1f | min any %.1f | max off-axis %.1f deg th0 %.1f" % (
        d['Vs'][b], ok.all(), ok2, badp, inv, (~ok).sum(), lev[14].mean(), lev[14].min(), lev[15].mean(), lev[1].mean(), lev.min(), off, np.rad2deg(th[b])))
    print("   mean levels:", ' '.join('%.0f' % x for x in lev.mean(axis=1)))
