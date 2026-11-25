import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from model import *
here = os.path.dirname(os.path.abspath(__file__))


def lin_odd(cell, Vs):
    A, Li = build(cell, np.array([CELLS[cell][1]]))
    x, vj, ix = dc_point(cell, Vs)
    g = FRAC * (I_full(vj + 1e-6) - I_full(vj - 1e-6)) / 2e-6
    J = A.copy()
    for h in (0, 1):
        J[idx(0, h, 'ix'), idx(0, h, 'vj')] += g[0] / TAU
    ev, evec = np.linalg.eig(J)
    best = None
    for e, v in zip(ev, evec.T):
        a, b = v[idx(0, 0, 'vst')], v[idx(0, 1, 'vst')]
        if abs(a + b) < abs(a - b) and e.imag > 0.3:
            best = e
    return best


for cell in 'BDF':
    # linear threshold scan
    vs = np.arange(0.80, 1.25, 0.0005)
    re = np.array([lin_odd(cell, v).real for v in vs])
    un = vs[re > 0]
    print('cell %s linear odd-mode instability of DC point: %.4f .. %.4f V' % (cell, un.min(), un.max()))
    for nd in (222, 444):
        d = np.load(os.path.join(here, 'item1_%s_%d.npz' % (cell, nd)))
        Vs = d['Vs']; A2 = d['A2']; A1 = d['A1']
        osc = (A2 > 0.005) & (np.abs(A2 / np.maximum(A1, 1e-12) - 1) < 0.02)
        r = Vs[osc]
        mid = 0.5 * (r.min() + r.max())
        im = np.argmin(np.abs(Vs - mid))
        lo = np.argmin(np.abs(Vs - r.min()))
        print('  ndiv %d: range %.2f..%.2f V, mid %.3f -> f %.2f GHz, odd amp %.4f V (even %.4f V); lower edge %.2f V: vj_dc %.4f V ix_dc %.3f mA, '
              'osc-avg vj %.4f V ix %.3f mA, amp %.4f V'
              % (nd, r.min(), r.max(), Vs[im], d['freq'][im], A2[im], d['E2'][im], Vs[lo], d['vj_dc'][lo], d['ix_dc'][lo],
                 d['vj_avg'][lo], d['ix_avg'][lo], A2[lo]))
        print('     upper edge amp %.4f V f %.2f GHz; amp at edge+0.01: %.5f V' % (A2[osc][-1], d['freq'][osc][-1], A2[np.argmin(np.abs(Vs - r.max() - 0.01))]))
    for v in (r.min() - 0.01, r.min(), r.max(), r.max() + 0.01):
        e = lin_odd(cell, v)
        print('     linear odd eigen at %.2f V: %.4f /ps, f %.1f GHz' % (v, e.real, e.imag / 2 / np.pi * 1000))
