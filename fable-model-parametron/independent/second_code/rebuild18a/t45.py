"""task 4 (time step) and task 5 (axis step along the row); plus pair-0 axis/level per q (task 3 context)"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from ana18 import *

R1 = load('c1'); R2 = load('c4')
b1 = int(np.where((np.abs(R1['Vs'] - 0.94) < 1e-6) & (np.abs(R1['p'] - 0.25) < 1e-6))[0][0])
sgn = R1['sgn']
for which in ('early', 'late'):
    Z1 = windows(R1, which)[0, b1]; Z2 = windows(R2, which)[0, 0]
    dph = wrap(np.angle(Z2[:, 1:]) - np.angle(Z1[:, 1:])) * deg
    dl = np.abs(Z2[:, 1:]) - np.abs(Z1[:, 1:])
    rel = dl / np.abs(Z1[:, 1:])
    print('task 4, %s window: dt %.5f -> %.5f ps, all 16 pairs x slots 1..10' % (which, R1['dt'], R2['dt']))
    print('  max|dphase| %.2f deg, rms dphase %.2f deg, mean dphase %.2f deg; max|dlevel| %.2f mV (%.2f %%), mean dlevel %.2f mV'
          % (np.abs(dph).max(), np.sqrt((dph ** 2).mean()), dph.mean(), 1000 * np.abs(dl).max(), 100 * np.abs(rel).max(),
             1000 * dl.mean()))
    print('  pair 14: mean dphase %.2f deg, max|dphase| %.2f; level %.1f -> %.1f mV (mean over slots)'
          % (dph[14].mean(), np.abs(dph[14]).max(), 1000 * np.abs(Z1[14, 1:]).mean(), 1000 * np.abs(Z2[14, 1:]).mean()))
    print('  per pair mean dphase:', ' '.join('%.2f' % x for x in dph.mean(-1)))
    J1 = judge(Z1, sgn); J2 = judge(Z2, sgn)
    print('  all right: dt %s, dt/2 %s' % (J1['right_all'].all(), J2['right_all'].all()))
    for J, lab in ((J1, 'dt'), (J2, 'dt/2')):
        ax = J['ax'] * deg
        dax = np.mod(np.diff(ax) + 90, 180) - 90         # modulo half a turn, in [-90, 90)
        dax2 = np.mod(np.diff(ax), 180)                  # modulo half a turn, in [0, 180)
        print('  task 5 (%s): axis of pair n (deg):' % lab, ' '.join('%.1f' % a for a in ax))
        print('     ax(n+1)-ax(n) mod 180 in [0,180):', ' '.join('%.1f' % a for a in dax2))
        print('     mean %.2f deg, std %.2f deg, min %.1f, max %.1f (n = 0..14, 15 steps); without step 0->1: mean %.2f std %.2f'
              % (dax2.mean(), dax2.std(ddof=1), dax2.min(), dax2.max(), dax2[1:].mean(), dax2[1:].std(ddof=1)))
        # same-bit phase step: phase(n+1) - phase(n) per slot, modulo 180, then stats over slots
        ps = np.mod(np.angle(Z1[1:, 1:] if lab == 'dt' else Z2[1:, 1:]) - np.angle(Z1[:-1, 1:] if lab == 'dt' else Z2[:-1, 1:]), np.pi) * deg
        print('     per-slot phase step mod 180: mean over slots per n:', ' '.join('%.1f' % a for a in ps.mean(-1)),
              '| max spread over slots %.2f deg' % (ps.max(-1) - ps.min(-1)).max())
    print('  dev from own axis, max over pairs/slots: dt %.2f deg' % J1['maxdev'].max())

R3 = load('c3')
Z3 = windows(R3, 'early')[0]
J3 = judge(Z3, sgn)
print('\npair 0 / 1 per q (clean, early window): axis of pair 0 vs the drive phase (drive cos(w t) has phase 0), min level')
for b in range(len(R3['q'])):
    print('  q %.2f  pair0 axis %7.1f deg  minlev0 %6.1f mV  meanlev0 %6.1f  minlev1 %6.1f  maxdev0 %5.1f maxdev1 %5.1f' % (
        R3['q'][b], J3['ax'][b, 0] * deg, 1000 * J3['minlev'][b, 0], 1000 * J3['meanlev'][b, 0], 1000 * J3['minlev'][b, 1],
        J3['maxdev'][b, 0], J3['maxdev'][b, 1]))
