import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from model import *

V = np.linspace(0, 1.6, 16001)
I = I_full(V)
ip = np.argmax(I[V < 1.0]); print('peak', I[ip], 'mA at', V[ip])
m = (V > 0.8) & (V < 1.6)
iv = np.argmin(I[m]); print('valley', I[m][iv], 'at', V[m][iv])
dI = np.gradient(I, V)
print('min slope full mA/V', dI.min(), 'at', V[np.argmin(dI)])
t = np.linspace(-10, 70, 9)
print('win', np.round(win(np.array([-7.15, 0, 7.15, 20, 0.75 * TP - 7.15, 0.75 * TP, 0.75 * TP + 7.15, 60, TP])), 4))
# linear stability of the DC point, single pair, odd/even modes
for cell in 'BDF':
    A, Li = build(cell, np.array([CELLS[cell][1]]))
    print('cell', cell)
    for Vs in np.arange(0.80, 1.26, 0.05):
        x, vj, ix = dc_point(cell, Vs)
        g = FRAC * (I_full(vj + 1e-6) - I_full(vj - 1e-6)) / 2e-6
        J = A.copy()
        for h in (0, 1):
            J[idx(0, h, 'ix'), idx(0, h, 'vj')] += g[0] / TAU
        ev, evec = np.linalg.eig(J)
        # classify odd: vst components opposite
        out = []
        for e, v in zip(ev, evec.T):
            if e.imag <= 0: continue
            a, b = v[idx(0, 0, 'vst')], v[idx(0, 1, 'vst')]
            mode = 'odd' if abs(a + b) < abs(a - b) else 'even'
            if abs(e.imag) > 0.3:
                out.append('%s %.4f%+.3fj f=%.1fGHz' % (mode, e.real, e.imag, e.imag / 2 / np.pi * 1000))
        print(' Vs %.2f vj %.3f ix %.3f g %.2f mA/V ' % (Vs, vj[0], ix[0], g[0]), '; '.join(out))
