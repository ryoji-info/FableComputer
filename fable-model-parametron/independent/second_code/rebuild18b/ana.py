"""analysis helpers"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from model import TP, TC
from netx import *

deg = 180 / np.pi


def wrap(a):
    return np.angle(np.exp(1j * a))


def load(tag):
    R = dict(np.load(os.path.join(here, 'res', 'run_%s.npz' % tag)))
    R['layout'] = str(R['layout'])
    return R


def judge(Z, E):
    """Z (...,N,NSL) complex window amplitudes; E (N,NSL) expected bits.  Own axis of a pair = angle of
    sum over slots 1.. of (unit phasor * (+1 for expected 1, -1 for expected 0)).  Signed deviation d of each slot
    from the expected half of that axis; right = |d| < 90 deg; projection = |z| cos d."""
    z = Z[..., 1:]
    e = E[:, 1:]
    known = e >= 0
    b = np.where(e == 1, 1.0, np.where(e == 0, -1.0, 0.0))
    u = z / np.maximum(np.abs(z), 1e-30)
    ax = np.angle(np.sum(u * b, axis=-1))
    d = wrap(np.angle(z) - ax[..., None] - np.where(b > 0, 0, np.pi))
    d = np.where(known, d, 0.0)
    proj = np.abs(z) * np.cos(d)
    ratio = proj / np.abs(z).mean(-1, keepdims=True)
    right = (np.abs(d) < np.pi / 2) | ~known
    return dict(ax=ax, dev=d * deg, maxdev=np.abs(d).max(-1) * deg, level=np.abs(z), proj=proj, ratio=ratio,
                right=right, right_all=right.all(-1))


def two_cluster(zs):
    """zs (...,NSL) one pair; axis from doubled phase over slots 1..; returns bits in both orientations"""
    z = zs[..., 1:]
    u = z / np.maximum(np.abs(z), 1e-30)
    ax = 0.5 * np.angle(np.sum(u ** 2, -1))
    pr = np.real(z * np.exp(-1j * ax[..., None]))
    return (pr > 0).astype(int), ax


def val(bits_from_slot1):
    return sum(int(v) << (i + 1) for i, v in enumerate(bits_from_slot1))
