"""usage: stats.py TAG CLEANTAG [delta ncar] [verbose]
Clean reference: CLEANTAG group 0 point 0 (no spread, no noise) at the same settings.
A decision is wrong when the phase in the read window lies > 90 deg from the clean run's phase (slots 1..31)."""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from ana import *

tag, ctag = sys.argv[1], sys.argv[2]
delta = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
ncar = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
verbose = len(sys.argv) > 5 and sys.argv[5] == 'v'
sl = None
if ':' in tag:
    tag, rg = tag.split(':'); lo, hi = map(int, rg.split('-')); sl = slice(lo, hi + 1)
R = load(tag); Rc = load(ctag)
if sl is not None:
    R['Zb'] = R['Zb'][:, sl]
    for k in ('Vs', 'q', 'pf'):
        R[k] = R[k][sl]
    if Rc['Zb'].shape[1] > 1:
        Rc['Zb'] = Rc['Zb'][:, sl]
E = logic(R['a'], R['b'])
Z = windows(R, delta, ncar)                    # (G,Bg,N,NSL)
G, Bg = Z.shape[:2]
Zc_all = windows(Rc, delta, ncar)[0]          # (Bgc,N,NSL)
pidx = np.arange(Bg) if Zc_all.shape[0] == Bg else np.zeros(Bg, int)   # per-point clean reference if available
Zc = Zc_all[0]
d = wrap(np.angle(Z) - np.angle(Zc_all[pidx])[None]) * deg
d = d[..., 1:]
wrong = np.abs(d) > 90                         # (G,Bg,N,31)
J = judge(Z, E)
Jc = judge(Zc, E)
runs = G * Bg
any_wrong = wrong.any(axis=(2, 3))
sum_wrong_bits = wrong[:, :, P['S'], :].sum(-1)
print('tag %s  runs %d (G %d draws x Bg %d)  window start T/4+%.1f ps, %.1f carrier periods' % (tag, runs, G, Bg, delta, ncar))
print('groups (draw:kfac):', R['groups'].tolist(), ' points (Vs,q,noise power factor):',
      list(zip(R['Vs'].tolist(), R['q'].tolist(), R['pf'].tolist())))
print('runs with any wrong decision: %d / %d' % (any_wrong.sum(), runs))
print('runs with any wrong sum bit (S): %d / %d ; wrong S bits total %d of %d' % ((sum_wrong_bits > 0).sum(), runs,
      sum_wrong_bits.sum(), runs * 31))
print('runs with any own-axis sign error (any pair): %d / %d' % ((~J['right_all']).any(-1).sum(), runs))
# per pair counts
print('pair   wrong-dec-runs  wrong-decisions  max|dphi| deg (all runs)  rms dphi deg  own-axis-fail-runs  min level mV (all runs)  clean min level mV')
for m in range(10):
    print('%-4s %8d %14d %16.1f %16.1f %12d %20.1f %16.1f' % (NAMES[m], wrong[:, :, m].any(-1).sum(), wrong[:, :, m].sum(),
          np.abs(d[:, :, m]).max(), np.sqrt((d[:, :, m] ** 2).mean()), (~J['right_all'][..., m]).sum(),
          1000 * np.abs(Z[..., m, 1:]).min(), 1000 * np.abs(Zc[m, 1:]).min()))
# first wrong decision per run (in time order: slot, then depth)
tt = np.array([[s * TP + DEPTH[m] * TP / 4 for s in range(1, 32)] for m in range(10)])
firsts = []
for g in range(G):
    for b in range(Bg):
        w = wrong[g, b]
        if w.any():
            mm, ss = np.where(w)
            k = np.argmin(tt[mm, ss])
            firsts.append((NAMES[mm[k]], ss[k] + 1, g, b, int(w.sum()),
                           ' '.join('%s%d' % (NAMES[x], y + 1) for x, y in sorted(zip(mm, ss), key=lambda u: tt[u[0], u[1]]))))
if firsts:
    print('first wrong decision per failing run: pair slot (draw-index, point) nwrong | all wrong in time order')
    for f in firsts:
        print('  %-3s slot %2d  (g%d,b%d) n=%d | %s' % f)
lev = np.abs(Z[..., 1:])
gg, bb, mm, ss = np.unravel_index(np.argmin(lev), lev.shape)
print('weakest level over all runs: %.1f mV at pair %s slot %d (g%d,b%d)' % (1000 * lev.min(), NAMES[mm], ss + 1, gg, bb))
if verbose:
    for g in range(G):
        for b in range(Bg):
            print('g%d b%d maxdev per pair' % (g, b), ' '.join('%s:%.0f' % (NAMES[m], np.abs(d[g, b, m]).max()) for m in range(10)))
