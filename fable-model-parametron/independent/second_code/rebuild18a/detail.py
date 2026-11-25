"""phase deviation from clean of pairs 0..3 per slot in failing runs (task 3), both windows"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from ana18 import *

Rc = load('c3')
for tag in sys.argv[1].split(','):
    R = load(tag)
    for b in range(len(R['q'])):
        ci = int(np.argmin(np.abs(Rc['q'] - R['q'][b])))
        for which in ('early', 'late'):
            Z = windows(R, which)[:, b]; Zc = windows(Rc, which)[0, ci]
            d = wrap(np.angle(Z[..., 1:]) - np.angle(Zc[None, :, 1:])) * deg
            for g in range(Z.shape[0]):
                if (np.abs(d[g]) > 90).any():
                    print('%s q %.2f draw %d %s window: wrong count %d' % (tag, R['q'][b], R['draws'][g], which, (np.abs(d[g]) > 90).sum()))
                    for m in range(4):
                        print('   pair %d dev(slots1..10):' % m, ' '.join('%6.0f' % x for x in d[g, m]),
                              ' lev mV:', ' '.join('%4.0f' % (1000 * x) for x in np.abs(Z[g, m, 1:])))
