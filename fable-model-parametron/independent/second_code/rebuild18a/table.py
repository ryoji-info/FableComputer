"""compact combined table: clean (early+late) and noisy (early, judged) per point"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from ana18 import *

sets = [('c1', ['n1p15', 'n1p25', 'n1p35']), ('c2', ['n2p25']), ('c3', ['n3a', 'n3b', 'n3c', 'n3d'])]
for ctag, ntags in sets:
    Rc = load(ctag); sgn = Rc['sgn']
    ZcE = windows(Rc, 'early')[0]; ZcL = windows(Rc, 'late')[0]
    JE = judge(ZcE, sgn); JL = judge(ZcL, sgn)
    print('%s (kstep %.1f): p q Vs | clean right16 E/L (n right E) | lev14 E/L mV clean | w14/80 rms14 max14 (E) | w14 rms14 (L) | PASS E/L'
          % (ctag, Rc['kstep']))
    for nt in ntags:
        R = load(nt)
        ZE = windows(R, 'early'); ZL = windows(R, 'late')
        for b in range(len(R['Vs'])):
            ci = [i for i in range(len(Rc['Vs'])) if abs(Rc['Vs'][i] - R['Vs'][b]) < 1e-6 and abs(Rc['p'][i] - R['p'][b]) < 1e-6
                  and abs(Rc['q'][i] - R['q'][b]) < 1e-6][0]
            out = []
            for Z, Zc, J in ((ZE, ZcE, JE), (ZL, ZcL, JL)):
                d = wrap(np.angle(Z[:, b, 14, 1:]) - np.angle(Zc[ci, 14, 1:])[None]) * deg
                w = (np.abs(d) > 90).sum(); r = np.sqrt((d ** 2).mean())
                ok = J['right_all'][ci].all() and w == 0 and r <= 8
                out.append((w, r, np.abs(d).max(), ok))
            print('%.2f %.2f %.3f | %s/%s (%2d) | %6.1f/%6.1f | %2d %6.1f %6.1f | %2d %6.1f | %s/%s' % (
                R['p'][b], R['q'][b], R['Vs'][b], 'Y' if JE['right_all'][ci].all() else 'N', 'Y' if JL['right_all'][ci].all() else 'N',
                JE['right_all'][ci].sum(), 1000 * JE['meanlev'][ci, 14], 1000 * JL['meanlev'][ci, 14], out[0][0], out[0][1], out[0][2],
                out[1][0], out[1][1], 'Y' if out[0][3] else 'N', 'Y' if out[1][3] else 'N'))
