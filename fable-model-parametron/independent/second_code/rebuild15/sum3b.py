import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from dec import *
here = os.path.dirname(os.path.abspath(__file__))
cleantag = sys.argv[1]; ntags = sys.argv[2].split(',')
c = np.load(os.path.join(here, 'row_%s.npz' % cleantag))
Vs, p, Zc, sgn = c['Vs'], c['p'], c['Z'][0], c['sgn']
rc, mdc, ac, _ = own_axis(Zc, sgn)
Zn, dr = [], []
for t in ntags:
    d = np.load(os.path.join(here, 'row_%s.npz' % t))
    Zn.append(d['Z']); dr += list(d['draws'])
Zn = np.concatenate(Zn, 0)          # (G, Bg, N, NSL)
dr = np.array(dr)
nw, rms, dev = vs_clean(Zn, Zc[None])
rn, mdn, an, _ = own_axis(Zn, sgn)
clean_ok = rc.all(-1)
print('draw order', dr, '(0 = no spread)')
print('Vs     p   clean16  | nospread: wrong14 rms14 own16 | spread draws: wrong14 / rms14 (deg) / own-axis right pairs | HOLD  HOLD_nospread')
res = []
for pv in np.unique(p):
    for v in np.unique(Vs):
        j = np.where((Vs == v) & (p == pv))[0][0]
        s0 = np.where(dr == 0)[0]; sp = np.where(dr != 0)[0]
        h0 = clean_ok[j] and all(nw[g, j] == 0 and rms[g, j] <= 8 for g in s0)
        hs = clean_ok[j] and all(nw[g, j] == 0 and rms[g, j] <= 8 for g in sp)
        res.append((v, pv, hs, h0))
        print('%.3f %.2f  %2d  | %s | %s | %s  %s' % (
            v, pv, rc[j].sum(),
            ' '.join('%2d %6.1f %2d' % (nw[g, j], rms[g, j], rn[g, j].sum()) for g in s0),
            '  '.join('%2d/%6.1f/%2d' % (nw[g, j], rms[g, j], rn[g, j].sum()) for g in sp),
            'HOLD' if hs else '----', 'HOLD' if h0 else '----'))
print()
for pv in np.unique(p):
    hs = [r[0] for r in res if r[1] == pv and r[2]]
    h0 = [r[0] for r in res if r[1] == pv and r[3]]
    print('p %.2f: holds with spread at Vs = %s ; without spread at Vs = %s' % (pv, hs, h0))
