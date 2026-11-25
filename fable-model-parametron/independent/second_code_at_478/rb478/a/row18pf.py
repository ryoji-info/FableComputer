"""Row of sixteen pairs, cell F, third specification (pump phase pi (q + KSTEP d)).
usage: row18pf.py TAG NDIV KSTEP NOISE DRAWS VSLIST PLIST QLIST [NSL] [SEED] [PF]
  PF : factor on the noise power (added on 23 November 2026 for runs at the noise of the 1-THz-class cell; default 1)
  DRAWS : comma list; 0 = no spread, k>0 = spread draw g ~ rng(5000+k) standard normal per pair, L_odd*(1+0.03 g)
  points = mesh VSLIST x PLIST x QLIST (all combinations, Vs fastest-varying last)
Saves block means (blocks of TC/8) of the demodulated odd-mode voltage: Zb (G,Bg,16,nblk), complex amplitude in V,
block j covers times (tb[j], tb[j]+TC/8].
"""
import sys, os, time
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from model import *
from sim_pf import Sim

tag = sys.argv[1]; ndiv = int(sys.argv[2]); kstep = float(sys.argv[3]); noise = int(sys.argv[4])
draws = [int(s) for s in sys.argv[5].split(',')]
VsL = [float(s) for s in sys.argv[6].split(',')]
pL = [float(s) for s in sys.argv[7].split(',')]
qL = [float(s) for s in sys.argv[8].split(',')]
NSL = int(sys.argv[9]) if len(sys.argv) > 9 else 11
seed = int(sys.argv[10]) if len(sys.argv) > 10 else 1
PF = float(sys.argv[11]) if len(sys.argv) > 11 else 1.0
assert ndiv % 8 == 0
cell = 'F'
N = 16
dt = TC / ndiv
PP, QQ, VV = np.meshgrid(pL, qL, VsL, indexing='ij')
Vs, p, q = VV.ravel(), PP.ravel(), QQ.ravel()
Bg = len(Vs); G = len(draws)
L0 = CELLS[cell][1]
Lg, gs = [], []
for d in draws:
    g = np.zeros(N) if d == 0 else np.random.default_rng(5000 + d).standard_normal(N)
    gs.append(g); Lg.append(L0 * (1 + 0.03 * g))
Lg = np.array(Lg)
t0c = time.time()
sim = Sim(cell, Lg, dt, Bg, noise=bool(noise), seed=seed, pf=PF)
n = sim.n
w = 2 * np.pi * FD
bits = np.array([1, 0, 1, 1, 0, 0, 1, 0])
sgn = np.where(bits[np.arange(NSL) % 8] == 1, 1.0, -1.0)
m = np.arange(N)
iS = sim.iS
ip, iq = sim.ip, sim.iq
cS = (1000 / RB) / CB
F = np.zeros((G, Bg, n))
Is = 0.4
ph = np.pi * (q[:, None] + kstep * m[None, :])            # (Bg,N) pump phase


def forcing(t):
    wv = win(t - m * TP / 4)                               # (N,)
    pump = 1 + p[:, None] * np.cos(2 * w * t + ph)         # (Bg,N)
    F[:, :, iS] = cS * Vs[:, None] * wv[None, :] * pump
    s = int(np.floor((t + 0.25 * TP) / TP))                # drive of slot s: [sT - T/4, sT + 3T/4)
    il = sgn[s] * Is * np.cos(w * t) / CS if 0 <= s < NSL else 0.0
    F[:, :, ip[0]] = il; F[:, :, iq[0]] = -il
    return F


bl = ndiv // 8
t0 = -1.25 * TP
tend = (NSL - 1) * TP + 15 * TP / 4 + 0.75 * TP + 2.0
nsteps = int(np.ceil((tend - t0) / dt))
nblk = nsteps // bl
Zb = np.zeros((G, Bg, N, nblk), np.complex64)
tb = t0 + dt * (np.arange(nblk) * bl)
cur = np.zeros((G, Bg, N), complex)


def obs(k, t, x):
    global cur
    v = 0.5 * (x[..., ip] - x[..., iq])
    cur += v * np.exp(-1j * w * t)
    if k % bl == 0:
        j = k // bl - 1
        if j < nblk:
            Zb[..., j] = cur * (2.0 / bl)
        cur[:] = 0


x0 = np.zeros((G, Bg, n))
xe, te = sim.run(x0, t0, nsteps, forcing, obs)
assert np.isfinite(xe).all()
np.savez(os.path.join(here, 'row_%s.npz' % tag), Zb=Zb, tb=tb, dt=dt, ndiv=ndiv, kstep=kstep, Vs=Vs, p=p, q=q,
         draws=np.array(draws), g=np.array(gs), NSL=NSL, sgn=sgn, noise=noise, seed=seed, pf=PF)
el = time.time() - t0c
print('row18', tag, 'G', G, 'Bg', Bg, 'steps', nsteps, 'dt %.5f ps' % dt, 'time %.1f s' % el)
with open(os.path.join(here, 'timing.txt'), 'a') as fh:
    fh.write('%s G %d Bg %d steps %d dt %.5f noise %d time %.1f s\n' % (tag, G, Bg, nsteps, dt, noise, el))
