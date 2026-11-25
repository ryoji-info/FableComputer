"""analysis helpers for adder runs"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from model import TP, TC
from net import *

deg = 180 / np.pi


def wrap(a):
    return np.angle(np.exp(1j * a))


def load(tag):
    return dict(np.load(os.path.join(here, 'run_%s.npz' % tag)))


def windows(R, delta=2.0, ncar=2.0):
    """Z (G,Bg,N,NSL): mean demodulated odd voltage (complex amplitude, V) in the window
    [s T + d T/4 + T/4 + delta, + ncar*TC] of pair (depth d), slot s.  Quantised to blocks of TC/8."""
    Zb, tb = R['Zb'], R['tb']
    bdt = tb[1] - tb[0]
    nb = int(round(ncar * 8))
    NSL = int(R['NSL'])
    G, Bg, N, nblk = Zb.shape
    Z = np.zeros((G, Bg, N, NSL), complex)
    for m in range(N):
        for s in range(NSL):
            st = s * TP + DEPTH[m] * TP / 4 + TP / 4 + delta
            j0 = int(round((st - tb[0]) / bdt))
            Z[:, :, m, s] = Zb[:, :, m, j0:j0 + nb].mean(-1)
    return Z


def judge(Z, E):
    """Z (...,N,NSL); E (N,NSL) expected bits (-1 unknown).  Own axis = expected-weighted mean of unit phasors over
    slots 1..NSL-1 with known bits (as rebuild15 dec.own_axis).  Returns dict of arrays over (...,N)."""
    z = Z[..., 1:]
    e = E[:, 1:]
    known = e >= 0
    b = np.where(e == 1, 1.0, np.where(e == 0, -1.0, 0.0))
    u = z / np.maximum(np.abs(z), 1e-30)
    ax = np.angle(np.sum(u * b, axis=-1))
    d = wrap(np.angle(z) - ax[..., None] - np.where(b > 0, 0, np.pi))
    d = np.where(known, d, 0.0)
    maxdev = np.abs(d).max(-1) * deg
    proj = np.abs(z) * np.cos(d)
    proj = np.where(known, proj, np.inf)
    right = (np.abs(d) < np.pi / 2) | ~known
    return dict(ax=ax, dev=d * deg, maxdev=maxdev, level=np.abs(z), proj=proj, right_all=right.all(-1), right=right)


def blind_decode(Zs):
    """Zs (..., NSL) of one pair: two-cluster axis from the doubled phase over slots 1..; orientation chosen so that
    most slots... (returned both orientations; caller fixes the global sign)."""
    z = Zs[..., 1:]
    u = z / np.maximum(np.abs(z), 1e-30)
    ax = 0.5 * np.angle(np.sum(u ** 2, -1))
    pr = np.real(z * np.exp(-1j * ax[..., None]))
    return (pr > 0).astype(int), ax
