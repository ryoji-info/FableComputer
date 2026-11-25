"""usage: stats.py NOISYTAG CLEANTAG [CLEANTAG2 ...] [-w IW]
Per point (Vs, p, kfac, noise factor) of the noisy run: wrong decisions (phase > 90 deg from the clean run at the same
Vs, p, kfac, same pair and slot; slots 1..31, all pairs), runs with any wrong decision, runs whose decoded sum is wrong.
Decoded sum of a run: the clean run's two-cluster decode of S/St, with every slot whose S/St phase is > 90 deg off the
clean phase flipped; wrong when it differs from the arithmetic sum in any slot 1..31.
Clean status: all pairs right on own axis (adder semantics) and clean decode == sum."""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from ana import *

args = sys.argv[1:]
iw = 0
if '-w' in args:
    k = args.index('-w'); iw = int(args[k + 1]); del args[k:k + 2]
ntag, ctags = args[0], args[1:]
R = load(ntag)
lname = R['layout']
names, depth, links, drives, spair = layout(lname)
N = len(names); iSp = names.index(spair)
E = rules(lname[0] + '1', A_OP, B_OP)
ssum = sum_bits(A_OP, B_OP)[0][1:]
clean = {}
for ct in ctags:
    C = load(ct)
    assert C['layout'] == lname and abs(C['pstep'] - R['pstep']) < 1e-9 and abs(C['q'] - R['q']) < 1e-9
    for gi, (d, kf) in enumerate(C['groups']):
        if d != 0:
            continue
        for bi in range(len(C['Vs'])):
            if C['pf'][bi] != 0:
                continue
            key = (round(C['Vs'][bi], 4), round(C['p'][bi], 4), round(kf, 4))
            Z = C['Zw'][iw, gi, bi]
            J = judge(Z, E)
            bits, _ = two_cluster(Z[iSp])
            if (bits != ssum).sum() > ((1 - bits) != ssum).sum():
                bits = 1 - bits
            clean[key] = (Z, bool(J['right_all'].all()), bool((bits == ssum).all()), bits, 1000 * J['level'].min(),
                          J['ratio'].min())
G, Bg = len(R['groups']), len(R['Vs'])
rows = {}
for gi, (d, kf) in enumerate(R['groups']):
    for bi in range(Bg):
        key = (round(R['Vs'][bi], 4), round(R['p'][bi], 4), round(kf, 4))
        pk = key + (round(R['pf'][bi], 3), d != 0)
        Zc, cr, cs, cbits, clev, crat = clean[key]
        Z = R['Zw'][iw, gi, bi]
        dph = wrap(np.angle(Z[:, 1:]) - np.angle(Zc[:, 1:]))
        wrong = np.abs(dph) > np.pi / 2
        dec = np.where(wrong[iSp], 1 - cbits, cbits)
        r = rows.setdefault(pk, dict(runs=0, wd=0, tot=0, anyw=0, sumw=0, cr=cr, cs=cs, clev=clev, crat=crat,
                                     minlev=1e9, pairs={}, maxd=0.0, ss=0.0))
        r['runs'] += 1; r['wd'] += int(wrong.sum()); r['tot'] += wrong.size
        r['anyw'] += int(wrong.any()); r['sumw'] += int((dec != ssum).any())
        r['maxd'] = max(r['maxd'], float(np.abs(dph).max() * deg)); r['ss'] += float((dph ** 2).sum() * deg ** 2)
        r['minlev'] = min(r['minlev'], 1000 * np.abs(Z[:, 1:]).min())
        for m in np.where(wrong.any(1))[0]:
            r['pairs'][names[m]] = r['pairs'].get(names[m], 0) + int(wrong[m].sum())
print('noisy %s (layout %s, pstep %.2f, dt %.5f ps, %s), window %s' % (ntag, lname, R['pstep'], R['dt'], R.get('dtype', ''),
      R['windows'][iw].tolist()))
print('  Vs     p     kfac  noise spread runs | wrongdec/total  runs-any-wrong  runs-wrong-sum | clean: right sum-ok minlev(mV) minratio | noisy minlev(mV) max|dph| rms dph (deg) | wrong decisions by pair')
for pk in sorted(rows):
    r = rows[pk]
    print('%6.3f %5.2f %6.3f %5.0f %5s %4d | %6d/%-7d %6d %14d | %5s %5s %8.1f %7.3f | %8.1f %7.1f %6.1f | %s' % (pk[0], pk[1], pk[2], pk[3],
          'yes' if pk[4] else 'no', r['runs'], r['wd'], r['tot'], r['anyw'], r['sumw'], r['cr'], r['cs'], r['clev'], r['crat'],
          r['minlev'], r['maxd'], np.sqrt(r['ss'] / r['tot']), ' '.join('%s:%d' % kv for kv in sorted(r['pairs'].items()))))
