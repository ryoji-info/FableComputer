import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from dec import *
here = os.path.dirname(os.path.abspath(__file__))
tag = sys.argv[1]
d = np.load(os.path.join(here, 'row_%s.npz' % tag))
Vs, p, Z, sgn = d['Vs'], d['p'], d['Z'][0], d['sgn']
right, maxdev, amin, sep = own_axis(Z, sgn)
print('clean row', tag, ': per point number of right pairs (of 16), first wrong pair, max dev deg at pairs 14/15, min amp (V) pair 14, sep pair 14')
for pv in np.unique(p):
    for v in np.unique(Vs):
        j = np.where((Vs == v) & (p == pv))[0][0]
        r = right[j]
        fw = np.where(~r)[0]
        print('Vs %.3f p %.2f  right %2d  firstwrong %3s  maxdev14 %6.1f  maxdev15 %6.1f  amin14 %.4f  amp14med %.4f sep14 %5.1f  ampmed by pair: %s' % (
            v, pv, r.sum(), fw[0] if len(fw) else '-', maxdev[j, 14], maxdev[j, 15], amin[j, 14],
            np.median(np.abs(Z[j, 14, 1:])), sep[j, 14], ' '.join('%.2f' % a for a in np.median(np.abs(Z[j, :, 1:]), -1))))
