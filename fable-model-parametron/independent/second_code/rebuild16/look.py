import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from ana import *

tag = sys.argv[1]
delta = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
ncar = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
R = load(tag)
E = logic(R['a'], R['b'])
Z = windows(R, delta, ncar)[0, 0]
J = judge(Z, E)
print('expected bits / phase dev from own axis (deg) / level (mV)')
for m in range(10):
    print('%-3s right %s maxdev %5.1f  minlev %6.1f mV  minproj %6.1f mV' % (NAMES[m], J['right_all'][m], J['maxdev'][m],
          1000 * J['level'][m].min(), 1000 * J['proj'][m].min()))
    print('    E ', ''.join('x' if v < 0 else str(v) for v in E[m]))
    print('    dv', ' '.join('%4.0f' % v for v in J['dev'][m]))
    print('    lv', ' '.join('%4.0f' % v for v in 1000 * J['level'][m]))
# time trace of amplitude and phase across one slot for each pair (slot 5), every TC
s = int(sys.argv[4]) if len(sys.argv) > 4 else 5
Zb, tb = R['Zb'][0, 0], R['tb']
print('slot', s, 'trace: t from pair start (ps), amp mV / phase deg (8-block means)')
for m in range(10):
    st = s * TP + DEPTH[m] * TP / 4
    j0 = int(round((st - tb[0]) / (tb[1] - tb[0])))
    row = []
    for k in range(0, 15):
        zz = Zb[m, j0 + 8 * k: j0 + 8 * k + 8].mean()
        row.append('%3.0f/%4.0f' % (1000 * abs(zz), np.angle(zz) * deg))
    print('%-3s' % NAMES[m], ' '.join(row))
