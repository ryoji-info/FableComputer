"""decode helpers"""
import numpy as np
deg = 180 / np.pi
AMIN = 0.010   # V, a slot with less odd amplitude than this counts as wrong


def wrap(a):
    return np.angle(np.exp(1j * a))


def own_axis(Z, sgn):
    """Z (..., N, NSL) complex; slot 0 dropped.  returns right(...,N), maxdev(...,N) deg, minamp(...,N)"""
    z = Z[..., 1:]
    b = sgn[1:]
    u = z / np.maximum(np.abs(z), 1e-30)
    ax = np.angle(np.sum(u * b, axis=-1))
    d = wrap(np.angle(z) - ax[..., None] - np.where(b > 0, 0, np.pi))
    maxdev = np.abs(d).max(-1) * deg
    amin = np.abs(z).min(-1)
    right = (maxdev < 45) & (amin > AMIN)
    # separation of class means
    m1 = np.angle(np.sum(u[..., b > 0], -1)); m0 = np.angle(np.sum(u[..., b < 0], -1))
    sep = np.abs(wrap(m1 - m0)) * deg
    return right, maxdev, amin, sep


def vs_clean(Zn, Zc, pair=14):
    """Zn (..., N, NSL), Zc (N, NSL) per point broadcast; returns nwrong, rms deg"""
    d = wrap(np.angle(Zn[..., pair, 1:]) - np.angle(Zc[..., pair, 1:])) * deg
    return (np.abs(d) > 90).sum(-1), np.sqrt((d ** 2).mean(-1)), d
