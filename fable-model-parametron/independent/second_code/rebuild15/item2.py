import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from model import *
from sim import Sim

ndiv = int(sys.argv[1]) if len(sys.argv) > 1 else 222
TEND = float(sys.argv[2]) if len(sys.argv) > 2 else 4000.0
cell = sys.argv[3] if len(sys.argv) > 3 else 'D'
dt = TC / ndiv
here = os.path.dirname(os.path.abspath(__file__))
VsL = np.round(np.arange(0.80, 1.1501, 0.025), 4)
pL = np.array([0.10, 0.15, 0.20, 0.30])
th = np.arange(12) * 2 * np.pi / 12
VV, PP, TH = np.meshgrid(VsL, pL, th, indexing='ij')
Vs, p, theta = VV.ravel(), PP.ravel(), TH.ravel()
B = len(Vs)
t0c = time.time()
sim = Sim(cell, np.array([[CELLS[cell][1]]]), dt, B)
x0, vj0, ix0 = dc_point(cell, Vs)
a = 2e-3
w = 2 * np.pi * FD
Ct = CELLS[cell][0] + CD
for h, s in ((0, 1), (1, -1)):
    x0[:, idx(0, h, 'vp')] += s * a * np.cos(theta); x0[:, idx(0, h, 'vst')] += s * a * np.cos(theta)
    x0[:, idx(0, h, 'iL')] += s * a * w * Ct * np.sin(theta)
x0 = x0[None]
nsteps = int(round(TEND / dt))
nb = ndiv  # one carrier period per block
nblk = nsteps // nb
Z = np.zeros((nblk, B), complex)
cur = np.zeros(B, complex)
ip, iq = sim.ip[0], sim.iq[0]


def obs(k, t, x):
    global cur
    v = 0.5 * (x[0, :, ip] - x[0, :, iq])
    cur = cur + v * np.exp(-1j * w * t)
    if k % nb == 0 and k // nb <= nblk:
        Z[k // nb - 1] = cur * 2 / nb
        cur = np.zeros(B, complex)


Fs = np.zeros((1, B, NS))
c0 = (1000 / RB) * Vs / CB


def forcing(t):
    Fs[0, :, 0] = c0 * (1 + p * np.cos(2 * w * t + np.pi))
    return Fs


sim.run(x0, 0.0, nsteps, forcing, obs)
np.savez(os.path.join(here, 'item2_%s_%d.npz' % (cell, ndiv)), Vs=Vs, p=p, theta=theta, Z=Z, tblk=(np.arange(nblk) + 0.5) * TC)
print('done', B, 'runs', nsteps, 'steps dt', dt, 'time %.1f s' % (time.time() - t0c))
