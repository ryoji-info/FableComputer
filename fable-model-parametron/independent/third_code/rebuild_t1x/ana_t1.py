import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
from sim import *


def env(t, v):
    """amplitude per carrier period (2*rms), times at period centres"""
    dt = t[1] - t[0]; n = int(round(Tc / dt))
    m = len(t) // n
    vv = v[:m * n].reshape(m, n, -1)
    return t[:m * n].reshape(m, n)[:, n // 2], np.sqrt(2 * (vv ** 2).mean(axis=1))


def freq(t, v):
    """frequency from upward zero crossings of v (1-D)"""
    s = np.sign(v)
    idx = np.where((s[:-1] < 0) & (s[1:] >= 0))[0]
    if len(idx) < 3:
        return np.nan
    tc = t[idx] - v[idx] * (t[idx + 1] - t[idx]) / (v[idx + 1] - v[idx])
    return (len(tc) - 1) / (tc[-1] - tc[0])


def lin_eig(Vs):
    lay = layout_single()
    Gam = build_L(lay, np.zeros((1, 1)))
    A = local_A(Gam.reshape(1, 1, 2, 2))[0, 0]
    x = dc_state(np.array([Vs]))[0]
    J = A.copy()
    for hh in (0, 1):
        J[3 + hh, 1 + hh] = frac * dIfull(x[1 + hh]) / tau
    w, V = np.linalg.eig(J)
    # odd modes: eigenvector antisymmetric in vP
    res = []
    for k in range(11):
        if w[k].imag > 0:
            odd = abs(V[5, k] + V[6, k]) < 1e-6 * abs(V[5, k] - V[6, k]) + 1e-12
            res.append((w[k].real, w[k].imag / 2 / np.pi, 'odd' if odd else 'even'))
    return res


if __name__ == '__main__':
    d = np.load('res/t1a.npz'); t = d['t']; v = d['v']
    te, e = env(t, v)
    print("Task 1a  (p=0). seed 1 mV.  columns: Vs, amp at 20 ps, 100 ps, 400 ps (mV), freq last 100 ps (THz), lin odd-mode growth (1/ps) & freq, even-mode growth")
    for b in range(len(d['Vs'])):
        m = t > 300
        f = freq(t[m], v[m, b])
        le = lin_eig(d['Vs'][b])
        od = [x for x in le if x[2] == 'odd']; ev = [x for x in le if x[2] == 'even']
        i20 = np.argmin(abs(te - 20)); i100 = np.argmin(abs(te - 100))
        print("%.2f  %.3g %.3g %.4g  f %.4f  odd %s even %s" % (d['Vs'][b], e[i20, b] * 1e3, e[i100, b] * 1e3, e[-1, b] * 1e3, f,
              ' '.join('%.3f/%.3f' % (x[0], x[1]) for x in od), ' '.join('%.3f/%.3f' % (x[0], x[1]) for x in ev)))
