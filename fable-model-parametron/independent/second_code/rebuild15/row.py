"""Clocked row of 16 pairs.  usage: row.py CELL NDIV TAG NOISE(0/1) DRAWS(comma list; 0 = no spread) [NSL] [VSLIST] [PLIST]"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from model import *
from sim import Sim

cell = sys.argv[1]; ndiv = int(sys.argv[2]); tag = sys.argv[3]; noise = int(sys.argv[4])
draws = [int(s) for s in sys.argv[5].split(',')]
NSL = int(sys.argv[6]) if len(sys.argv) > 6 else 12
VsL = np.array([float(s) for s in sys.argv[7].split(',')]) if len(sys.argv) > 7 else np.round(0.85 + 0.015 * np.arange(15), 4)
pL = np.array([float(s) for s in sys.argv[8].split(',')]) if len(sys.argv) > 8 else np.array([0.10, 0.15, 0.20, 0.30])
opts = sys.argv[9].split(',') if len(sys.argv) > 9 else []
here = os.path.dirname(os.path.abspath(__file__))
N = 16
dt = TC / ndiv
VV, PP = np.meshgrid(VsL, pL, indexing='ij')
Vs, p = VV.ravel(), PP.ravel()
Bg = len(Vs); G = len(draws)
L0 = CELLS[cell][1]
Lg = []
gs = []
for d in draws:
    g = np.zeros(N) if d == 0 else np.random.default_rng(1000 + d).standard_normal(N)
    gs.append(g); Lg.append(L0 * (1 + 0.03 * g))
Lg = np.array(Lg)
t0c = time.time()
sim = Sim(cell, Lg, dt, Bg, noise=bool(noise), seed=12345 + 7 * sum(draws) + 100 * ndiv)
n = sim.n
w = 2 * np.pi * FD
bits = np.array([1, 0, 1, 1, 0, 0, 1, 0])
sgn = np.where(bits[np.arange(NSL) % 8] == 1, 1.0, -1.0)
m = np.arange(N)
iS = sim.iS
ip0, iq0 = sim.ip[0], sim.iq[0]
cS = (1000 / RB) / CB
F = np.zeros((G, Bg, n))
Is = 0.4


def forcing(t):
    wv = win(t - m * TP / 4)                                # (N,)
    pump = 1 + p[:, None] * np.cos(2 * w * t + np.pi * (1 + m[None, :]))   # (Bg,N)
    F[:, :, iS] = cS * Vs[:, None] * wv[None, :] * pump
    s = int(np.floor((t + 0.25 * TP) / TP))
    late = 'drvend' in opts and (t - s * TP) > 0.75 * TP - 7.15
    if 0 <= s < NSL and not late:
        il = sgn[s] * Is * np.cos(w * t) / CS
    else:
        il = 0.0
    F[:, :, ip0] = il; F[:, :, iq0] = -il
    return F


W = (2 if 'W2' in opts else 4) * TC
acc = np.zeros((G, Bg, N, NSL), complex)
nacc = np.zeros((N, NSL))
blk = []
cur = np.zeros((G, Bg, N), complex)
ip, iq = sim.ip, sim.iq
off = 0.75 * TP - 7.15 - W


def obs(k, t, x):
    global cur
    v = 0.5 * (x[..., ip] - x[..., iq])               # (G,Bg,N)
    zz = v * np.exp(-1j * w * t)
    cur = cur + zz
    if k % ndiv == 0:
        blk.append(np.abs(cur) * 2 / ndiv)
        cur = np.zeros_like(cur)
    u = t - m * TP / 4 - off
    s = np.floor(u / TP).astype(int)
    r = u - s * TP
    ok = (r >= 0) & (r < W) & (s >= 0) & (s < NSL)
    if ok.any():
        mm = m[ok]; ss = s[ok]
        acc[:, :, mm, ss] += zz[:, :, mm]
        nacc[mm, ss] += 1


t0 = -1.25 * TP
tend = (NSL - 1) * TP + 15 * TP / 4 + 0.75 * TP - 7.15 + 1.0
nsteps = int(np.ceil((tend - t0) / dt))
x0 = np.zeros((G, Bg, n))
sim.run(x0, t0, nsteps, forcing, obs)
Zr = acc * 2 / np.maximum(nacc, 1)
np.savez(os.path.join(here, 'row_%s.npz' % tag), Vs=Vs, p=p, Z=Zr, draws=np.array(draws), g=np.array(gs),
         env=np.array(blk, dtype=np.float32), t0=t0, ndiv=ndiv, cell=cell, noise=noise, NSL=NSL, sgn=sgn)
print('row', cell, tag, 'G', G, 'Bg', Bg, 'steps', nsteps, 'dt %.5f' % dt, 'time %.1f s' % (time.time() - t0c))
