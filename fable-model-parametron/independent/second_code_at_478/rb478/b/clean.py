"""usage: clean.py TAG[:g:b] [v]   task-1 table for a clean run."""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from ana import *

arg = sys.argv[1]
verbose = len(sys.argv) > 2
gi = bi = 0
if ':' in arg:
    arg, gi, bi = arg.split(':'); gi, bi = int(gi), int(bi)
R = load(arg)
lname = R['layout']
names, depth, links, drives, spair = layout(lname)
N = len(names); P = {nm: i for i, nm in enumerate(names)}
E = rules(lname[0] + '1', A_OP, B_OP)   # adder semantics (section 3 of the first addendum)
Er = rules(lname, A_OP, B_OP)            # literal link-rule propagation of this layout
ssum, va, vb, s = sum_bits(A_OP, B_OP)
print('clean %s layout %s pstep %.2f q %.2f  Vs %.3f p %.2f pf %g kfac %.3f dt %.5f ps' % (arg, lname, R['pstep'], R['q'],
      R['Vs'][bi], R['p'][bi], R['pf'][bi], R['groups'][gi][1], R['dt']))
print('a=%d b=%d a+b=%d ; sum bits slots1..31 %s' % (va, vb, s, ''.join(map(str, ssum[1:]))))
for iw, (dl, nc) in enumerate(R['windows']):
    Z = R['Zw'][iw, gi, bi]
    J = judge(Z, E)
    lev = J['level']; rat = J['ratio']
    m, sl = np.unravel_index(np.argmin(lev), lev.shape)
    m2, sl2 = np.unravel_index(np.argmin(rat), rat.shape)
    print('\nwindow start T/4 + %.1f ps, %.0f carrier periods' % (dl, nc))
    print(' pair  depth right  maxdev   minlev(mV) meanlev(mV) minratio')
    for k in range(N):
        print(' %-4s %3d   %-5s %6.1f %10.1f %10.1f %9.3f' % (names[k], depth[k], J['right_all'][k], J['maxdev'][k],
              1000 * lev[k].min(), 1000 * lev[k].mean(), rat[k].min()))
    print(' all pairs right:', bool(J['right_all'].all()), ' wrong (pair,slot):',
          [(names[a], b + 1) for a, b in zip(*np.where(~J['right']))][:40])
    print(' lowest level %.1f mV (%s slot %d); smallest proj/meanlevel %.3f (%s slot %d)' % (1000 * lev.min(), names[m], sl + 1,
          rat.min(), names[m2], sl2 + 1))
    zS = Z[P[spair]]
    bits, ax = two_cluster(zS)
    nm1 = int((bits != ssum[1:]).sum()); nm2 = int(((1 - bits) != ssum[1:]).sum())
    if nm2 < nm1:
        bits = 1 - bits
    print(' %s two-cluster decode (orientation with fewer mismatches): %s  value %d  mismatches vs sum %d (other orientation %d)'
          % (spair, ''.join(map(str, bits)), val(bits), min(nm1, nm2), max(nm1, nm2)))
    ruleS = Er[P[spair], 1:]
    print(' %s link-rule stream                                       : %s  value %d' % (spair, ''.join(map(str, ruleS)), val(ruleS)))
    if lname[0] == 'c':
        dts = wrap(np.angle(Z[P['St'], 1:]) - np.angle(Z[P['Sc'], 1:])) * deg
        print(' St-Sc phase difference (deg), min |.| %.1f  max |.| %.1f' % (np.abs(dts).min(), np.abs(dts).max()))
    if verbose and iw == 0:
        for k in range(N):
            print('  %-4s E  %s' % (names[k], ''.join('x' if v < 0 else str(v) for v in E[k, 1:])))
            ph = np.angle(Z[k, 1:]) * deg
            print('       ph %s' % ' '.join('%4.0f' % v for v in ph))
            print('       dv %s' % ' '.join('%4.0f' % v for v in J['dev'][k]))
            print('       lv %s' % ' '.join('%4.0f' % v for v in 1000 * lev[k]))
