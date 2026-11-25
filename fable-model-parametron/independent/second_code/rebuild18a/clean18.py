"""usage: clean18.py TAG   table for clean runs (group 0, all points)"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from ana18 import *

R = load(sys.argv[1])
sgn = R['sgn']
ZE = windows(R, 'early')[0]; ZL = windows(R, 'late')[0]
JE = judge(ZE, sgn); JL = judge(ZL, sgn)
print('clean %s kstep %.2f dt %.5f ps, slots 1..%d counted; early window T/4+%.1f ps, late window ends 0.75T-7.15 ps, %.0f TC each'
      % (sys.argv[1], R['kstep'], R['dt'], int(R['NSL']) - 1, DELTA_E, NCAR))
print('   p     q     Vs  | E:all16 nright firstbad maxdev14 | L:all16 nright | lev14E mean/min mV | lev14L mean/min mV | minlevE any pair mV (pair)')
for b in range(len(R['Vs'])):
    rE = JE['right_all'][b]; rL = JL['right_all'][b]
    fb = np.where(~rE)[0]
    fb = str(fb[0]) if len(fb) else '-'
    ml = JE['minlev'][b]; k = np.argmin(ml)
    print('%5.2f %5.2f %6.3f | %-5s %3d %4s %8.1f | %-5s %3d | %7.1f %7.1f | %7.1f %7.1f | %7.2f (%d)' % (
        R['p'][b], R['q'][b], R['Vs'][b], bool(rE.all()), rE.sum(), fb, JE['maxdev'][b, 14], bool(rL.all()), rL.sum(),
        1000 * JE['meanlev'][b, 14], 1000 * JE['minlev'][b, 14], 1000 * JL['meanlev'][b, 14], 1000 * JL['minlev'][b, 14],
        1000 * ml[k], k))
