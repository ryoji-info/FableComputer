import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
from sim import *
lay = layout_single()
Gam = build_L(lay, np.zeros((1, 1)))
A = local_A(Gam.reshape(1, 1, 2, 2))[0, 0]
for vs in [0.0, 0.94]:
    x = dc_state(np.array([vs]))[0]
    J = A.copy()
    for hh in (0, 1):
        J[3 + hh, 1 + hh] = frac * dIfull(x[1 + hh]) / tau
    ev = np.linalg.eigvals(J)
    print(vs, np.sort_complex(ev))
    for h in [Tc / 128, Tc / 512]:
        g = 2 / 3 * h
        Mi = np.linalg.inv(np.eye(11) - g * J)
        Cm = np.block([[4 / 3 * Mi, -1 / 3 * Mi], [np.eye(11), np.zeros((11, 11))]])
        print('  h', h, 'max |amp|', np.abs(np.linalg.eigvals(Cm)).max())
