"""usage: noise18.py CLEANTAG NOISETAG[,NOISETAG...] [early|late]
Wrong decision: phase in the read window > 90 deg from the clean run's phase (same pair, slot, point); slots 1..NSL-1.
"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from ana18 import *

which = sys.argv[3] if len(sys.argv) > 3 else 'early'
Rc = load(sys.argv[1])
sgn = Rc['sgn']
Zc = windows(Rc, which)[0]
Jc = judge(Zc, sgn)
key = lambda V, p, q: (round(float(V), 4), round(float(p), 4), round(float(q), 4))
cidx = {key(V, p, q): i for i, (V, p, q) in enumerate(zip(Rc['Vs'], Rc['p'], Rc['q']))}
print('window %s; clean %s; wrong = |phase - clean phase| > 90 deg; pair 14 statistics over all draws and slots 1..%d'
      % (which, sys.argv[1], int(Rc['NSL']) - 1))
print('   p     q     Vs  draws | clean16 | w14 /dec  draws_w14  rms14  max14 | wrong any pair (runs) | lev14 mean mV | PASS | first wrong pair per failing run')
for tag in sys.argv[2].split(','):
    R = load(tag)
    Z = windows(R, which)                     # (G,Bg,N,NSL)
    G = Z.shape[0]
    for b in range(len(R['Vs'])):
        ci = cidx[key(R['Vs'][b], R['p'][b], R['q'][b])]
        d = wrap(np.angle(Z[:, b, :, 1:]) - np.angle(Zc[ci, :, 1:])[None]) * deg     # (G,N,ns)
        wr = np.abs(d) > 90
        w14 = wr[:, 14].sum(); dw14 = wr[:, 14].any(-1).sum()
        rms14 = np.sqrt((d[:, 14] ** 2).mean()); mx14 = np.abs(d[:, 14]).max()
        clean_ok = bool(Jc['right_all'][ci].all())
        ok = clean_ok and w14 == 0 and rms14 <= 8.0
        firsts = []
        for g in range(G):
            if wr[g].any():
                mm, ss = np.where(wr[g])
                tt = ss * 4 + mm                       # time order: slot s, depth m -> s T + m T/4
                k = np.argmin(tt)
                firsts.append('%d(s%d)' % (mm[k], ss[k] + 1))
        print('%5.2f %5.2f %6.3f %3d   | %-5s | %3d /%3d %5d %8.1f %6.1f | %5d (%d) | %7.1f | %-4s | %s' % (
            R['p'][b], R['q'][b], R['Vs'][b], G, clean_ok, w14, G * d.shape[-1], dw14, rms14, mx14, wr.sum(),
            wr.any(axis=(1, 2)).sum(), 1000 * np.abs(Z[:, b, 14, 1:]).mean(), 'yes' if ok else 'no', ' '.join(firsts)))
