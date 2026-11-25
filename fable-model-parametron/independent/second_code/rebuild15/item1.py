import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from model import *
from sim import Sim

ndiv = int(sys.argv[1]) if len(sys.argv) > 1 else 222
cells = sys.argv[2] if len(sys.argv) > 2 else 'BDF'
TEND = float(sys.argv[3]) if len(sys.argv) > 3 else 3000.0
dt = TC / ndiv
Vs = np.round(np.arange(0.80, 1.2501, 0.01), 3)
B = len(Vs)
here = os.path.dirname(os.path.abspath(__file__))
for cell in cells:
    t0c = time.time()
    sim = Sim(cell, np.array([[CELLS[cell][1]]]), dt, B)
    x0, vj0, ix0 = dc_point(cell, Vs)
    kick = 1e-3
    for h, s in ((0, 1), (1, -1)):
        x0[:, idx(0, h, 'vp')] += s * kick; x0[:, idx(0, h, 'vst')] += s * kick
    x0 = x0[None]
    nsteps = int(round(TEND / dt))
    dec = 4
    nrec = nsteps // dec + 1
    odd = np.zeros((nrec, B)); even = np.zeros((nrec, B)); tt = np.zeros(nrec)
    ntail = int(round(200 / dt))
    acc = {'vj': np.zeros(B), 'ix': np.zeros(B), 'n': 0}
    ip, iq = sim.ip[0], sim.iq[0]
    jv, jx = idx(0, 0, 'vj'), idx(0, 0, 'ix')

    def obs(k, t, x):
        if k % dec == 0:
            r = k // dec
            odd[r] = 0.5 * (x[0, :, ip] - x[0, :, iq]); even[r] = 0.5 * (x[0, :, ip] + x[0, :, iq]); tt[r] = t
        if k > nsteps - ntail:
            acc['vj'] += x[0, :, jv]; acc['ix'] += x[0, :, jx]; acc['n'] += 1

    Fs = np.zeros((1, B, NS)); Fs[0, :, 0] = (1000 / RB) * Vs / CB
    forcing = lambda t: Fs
    sim.run(x0, 0.0, nsteps, forcing, obs)
    tt = tt[:nsteps // dec]; odd = odd[:nsteps // dec]; even = even[:nsteps // dec]
    w1 = (tt > TEND - 400) & (tt <= TEND - 200); w2 = tt > TEND - 200
    A1 = 0.5 * (odd[w1].max(0) - odd[w1].min(0)); A2 = 0.5 * (odd[w2].max(0) - odd[w2].min(0))
    E2 = 0.5 * (even[w2].max(0) - even[w2].min(0))
    # frequency from upward zero crossings of odd signal (minus its mean) over last 400 ps
    w = tt > TEND - 400
    freq = np.full(B, np.nan)
    for b in range(B):
        s = odd[w, b] - odd[w, b].mean(); ts = tt[w]
        c = np.where((s[:-1] < 0) & (s[1:] >= 0))[0]
        if len(c) > 3:
            tc = ts[c] - s[c] * (ts[c + 1] - ts[c]) / (s[c + 1] - s[c])
            freq[b] = (len(tc) - 1) / (tc[-1] - tc[0]) * 1000
    np.savez(os.path.join(here, 'item1_%s_%d.npz' % (cell, ndiv)), Vs=Vs, A1=A1, A2=A2, E2=E2, freq=freq,
             vj_dc=vj0, ix_dc=ix0, vj_avg=acc['vj'] / acc['n'], ix_avg=acc['ix'] / acc['n'],
             tt=tt[::5], odd=odd[::5], even=even[::5])
    print('cell', cell, 'dt', dt, 'steps', nsteps, 'time %.1f s' % (time.time() - t0c))
    for b in range(B):
        print('  Vs %.2f  A1 %.4f A2 %.4f V  even %.4f V  f %.2f GHz  vjdc %.3f ixdc %.3f  vjavg %.3f ixavg %.3f'
              % (Vs[b], A1[b], A2[b], E2[b], freq[b], vj0[b], ix0[b], acc['vj'][b] / acc['n'], acc['ix'][b] / acc['n']))
