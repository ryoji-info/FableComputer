"""usage: clean.py TAG [TAG_HALF]   task-1 table for a clean run (group 0, point 0); window variants; dt check."""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from ana import *

tag = sys.argv[1]
bpt = 0
if ':' in tag:
    tag, bpt = tag.split(':'); bpt = int(bpt)
R = load(tag)
R['Zb'] = R['Zb'][:, bpt:bpt + 1]
print('clean run', tag, 'point', bpt, 'Vs %.3f q %.2f' % (R['Vs'][bpt], R['q'][bpt]), 'kfac', R['groups'][0][1])
E = logic(R['a'], R['b'])
ssum, va, vb, s = sum_stream(R['a'], R['b'])
print('operands a=%d b=%d sum=%d ; sum bits LSB first %s' % (va, vb, s, ''.join(map(str, ssum))))
for (delta, ncar) in [(2.0, 2.0), (0.0, 1.0), (0.0, 2.0), (2.0, 1.0), (2.0, 4.0), (5.0, 2.0), (8.0, 2.0), (-3.0, 2.0)]:
    Z = windows(R, delta, ncar)[0, 0]
    J = judge(Z, E)
    bits, ax = blind_decode(Z[P['S']])
    # orient blind decode: global sign fixed by majority agreement with the expected stream
    exp = ssum[1:]
    if (bits == exp).sum() < 15.5:
        bits = 1 - bits
    lev = J['level'][:, :]
    m, sl = np.unravel_index(np.argmin(lev), lev.shape)
    pj = J['proj']
    m2, sl2 = np.unravel_index(np.argmin(pj), pj.shape)
    print('\nwindow T/4 + %.1f ps, %.0f carrier periods' % (delta, ncar))
    print(' pair  right(1..31)  maxdev(deg)  minlevel(mV)  slot  minproj(mV)  meanlevel(mV)')
    for k in range(10):
        print(' %-4s  %-5s %12.1f %12.1f %5d %12.1f %12.1f' % (NAMES[k], J['right_all'][k], J['maxdev'][k], 1000 * lev[k].min(),
              np.argmin(lev[k]) + 1, 1000 * pj[k].min(), 1000 * lev[k].mean()))
    print(' S decoded (slots 1..31, own-axis sign):', ''.join(str(int(e)) if r else '?' for e, r in zip(E[P['S'], 1:], J['right'][P['S']])).replace('?', '!'))
    print(' S blind two-cluster decode           :', ''.join(map(str, bits)))
    print(' sum bits (slots 1..31)               :', ''.join(map(str, exp)), ' equal:', bool((bits == exp).all()))
    print(' lowest level any pair any slot: %.1f mV (%s slot %d); lowest projection on own axis %.1f mV (%s slot %d)'
          % (1000 * lev.min(), NAMES[m], sl + 1, 1000 * pj.min(), NAMES[m2], sl2 + 1))
if len(sys.argv) > 2:
    R2 = load(sys.argv[2])
    Z1 = windows(R, 2.0, 2.0)[0, 0, :, 1:]; Z2 = windows(R2, 2.0, 2.0)[0, 0, :, 1:]
    dphi = wrap(np.angle(Z2) - np.angle(Z1)) * deg
    dl = 1000 * (np.abs(Z2) - np.abs(Z1))
    print('\ntime step check: %s (dt %.5f ps) vs %s (dt %.5f ps)' % (tag, R['dt'], sys.argv[2], R2['dt']))
    print(' pair  max|dphase| deg  max|dlevel| mV   min level (half dt) mV')
    for k in range(10):
        print(' %-4s %10.2f %14.2f %14.1f' % (NAMES[k], np.abs(dphi[k]).max(), np.abs(dl[k]).max(), 1000 * np.abs(Z2[k]).min()))
    J2 = judge(windows(R2, 2.0, 2.0)[0, 0], E)
    print(' half-dt: all pairs right:', bool(J2['right_all'].all()), ' max dev %.1f deg' % J2['maxdev'].max())
