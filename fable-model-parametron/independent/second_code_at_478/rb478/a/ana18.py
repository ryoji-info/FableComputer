"""analysis helpers for row18 runs"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from model import TP, TC

deg = 180 / np.pi
N = 16
DELTA_E = 2.0      # early window starts T/4 + 2 ps after the pair's period start (rise centre)
NCAR = 2.0         # window length in carrier periods
LATE_END = 0.75 * TP - 7.15   # late window ends where the supply starts to fall


def wrap(a):
    return np.angle(np.exp(1j * a))


def load(tag):
    return dict(np.load(os.path.join(here, 'row_%s.npz' % tag)))


def windows(R, which='early', delta=DELTA_E, ncar=NCAR):
    """Z (G,Bg,N,NSL): mean of 2 v_odd exp(-i w t) over the window of pair m (depth m), slot s."""
    Zb, tb = R['Zb'], R['tb']
    bdt = tb[1] - tb[0]
    nb = int(round(ncar * 8))
    NSL = int(R['NSL'])
    G, Bg, _, nblk = Zb.shape
    Z = np.zeros((G, Bg, N, NSL), complex)
    for m in range(N):
        for s in range(NSL):
            if which == 'early':
                st = s * TP + m * TP / 4 + TP / 4 + delta
            else:
                st = s * TP + m * TP / 4 + LATE_END - ncar * TC
            j0 = int(round((st - tb[0]) / bdt))
            assert j0 >= 0 and j0 + nb <= nblk
            Z[:, :, m, s] = Zb[:, :, m, j0:j0 + nb].mean(-1)
    return Z


def judge(Z, sgn):
    """own axis per pair: angle of sum over slots 1.. of unit phasor * expected sign; sign right if |dev| < 90."""
    z = Z[..., 1:]
    b = sgn[1:]
    u = z / np.maximum(np.abs(z), 1e-30)
    ax = np.angle(np.sum(u * b, axis=-1))
    d = wrap(np.angle(z) - ax[..., None] - np.where(b > 0, 0, np.pi))
    right = np.abs(d) < np.pi / 2
    return dict(ax=ax, dev=d * deg, maxdev=np.abs(d).max(-1) * deg, right_all=right.all(-1),
                level=np.abs(z), minlev=np.abs(z).min(-1), meanlev=np.abs(z).mean(-1))
