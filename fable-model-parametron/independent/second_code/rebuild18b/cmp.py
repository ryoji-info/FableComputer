"""usage: cmp.py TAG1 TAG2   compare window phasors (group 0 point 0) of two clean runs, slots 1..31"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from ana import *

R1, R2 = load(sys.argv[1]), load(sys.argv[2])
names = layout(R1['layout'])[0]
print('%s (dt %.5f, %s) vs %s (dt %.5f, %s)' % (sys.argv[1], R1['dt'], R1.get('dtype', 'float64'), sys.argv[2], R2['dt'],
      R2.get('dtype', 'float64')))
for iw, (dl, nc) in enumerate(R1['windows']):
    Z1 = R1['Zw'][iw, 0, 0, :, 1:]; Z2 = R2['Zw'][iw, 0, 0, :, 1:]
    dp = wrap(np.angle(Z2) - np.angle(Z1)) * deg
    dl_ = 1000 * (np.abs(Z2) - np.abs(Z1))
    rel = (np.abs(Z2) - np.abs(Z1)) / np.abs(Z1)
    print('window T/4+%.1f ps, %.0f TC: max|dphase| %.2f deg (pair %s), mean|dphase| %.2f deg; max|dlevel| %.2f mV '
          '(max rel %.2f %%), mean dlevel %.2f mV' % (dl, nc, np.abs(dp).max(), names[np.unravel_index(np.argmax(np.abs(dp)), dp.shape)[0]],
          np.abs(dp).mean(), np.abs(dl_).max(), 100 * np.abs(rel).max(), dl_.mean()))
