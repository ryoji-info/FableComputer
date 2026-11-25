"""Time-domain run of a layout of BLIND_SPEC_D225_STEP.
usage: run.py TAG LAYOUT NDIV GROUPS POINTS [SEED] [PSTEP] [Q] [TRACE]
  GROUPS : comma list draw:kfac   (draw 0 = no spread; else g ~ N(0,1) per pair from rng(5000+draw), L_odd*(1+0.03 g))
  POINTS : comma list Vs:p:pf     (p pump level, pf noise POWER factor, 0 = no noise)
  PSTEP  : pump phase per clock depth in units of pi (1.5 = this spec, 1.0 = second spec); phase = pi (Q + PSTEP d)
  TRACE  : 1 = also store TC/2 block averages of the demodulated odd voltage (for clean diagnostics)
Integrator: SBDF2 (rebuild15/16 scheme): BDF2 on the linear network, 2nd-order extrapolation of the diode term.
Read windows accumulated on the fly: Z = (2/Tw) * sum v_odd exp(-i w t) dt over [sT + dT/4 + T/4 + delta, + ncar TC].
"""
import sys, os, time
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from model import *
from netx import *

WINDOWS = [(2.0, 2.0), (0.0, 1.0), (2.0, 4.0), (5.0, 2.0)]   # (delta ps after T/4, length in carrier periods)

tag, lname, ndiv = sys.argv[1], sys.argv[2], int(sys.argv[3])
groups = [(int(s.split(':')[0]), float(s.split(':')[1])) for s in sys.argv[4].split(',')]
pts = [tuple(float(u) for u in s.split(':')) for s in sys.argv[5].split(',')]
seed = int(sys.argv[6]) if len(sys.argv) > 6 else 1
PSTEP = float(sys.argv[7]) if len(sys.argv) > 7 else 1.5
Q = float(sys.argv[8]) if len(sys.argv) > 8 else 0.25
TRACE = int(sys.argv[9]) if len(sys.argv) > 9 else 0
cell = 'F'
names, depth, links, drives, spair = layout(lname)
P = {nm: i for i, nm in enumerate(names)}
N = len(names)
NSL = 32
dt = TC / ndiv
Vs = np.array([p[0] for p in pts]); pp = np.array([p[1] for p in pts]); pf = np.array([p[2] for p in pts])
Bg, G = len(pts), len(groups)
L0 = CELLS[cell][1]
ALs, gs = [], []
for d, kf in groups:
    g = np.zeros(N) if d == 0 else np.random.default_rng(5000 + d).standard_normal(N)
    gs.append(g)
    ALs.append(build_net(cell, L0 * (1 + 0.03 * g), names, links, kfac=kf))
t0c = time.time()
n = NS * N
I = np.eye(n)
MbeT = np.array([np.linalg.inv(I - dt * A).T for A, _ in ALs])
Mbd2T = np.array([np.linalg.inv(3 * I - 2 * dt * A).T for A, _ in ALs])
ivj, iix = vj_idx(N), ix_idx(N)
ip, iq = vst_idx(N)
iS = np.array([idx(m, name='vS') for m in range(N)])
noise = bool((pf > 0).any())
rng = np.random.default_rng(seed)
if noise:
    BnT = np.array([noise_matrix(cell, Li, N, dt) for _, Li in ALs])
    sh_sig = 1000 * np.sqrt(QE / 1000 / (dt * 1e-12))
    sc = np.sqrt(pf)[None, :, None]


def nonlin(x):
    out = np.zeros_like(x)
    out[..., iix] = FRAC * I_full(x[..., ivj]) / TAU
    return out


def noise_term(x):
    z = rng.standard_normal((G, Bg, BnT.shape[1]))
    xi = np.matmul(z, BnT)
    sh = sh_sig * np.sqrt(np.abs(x[..., iix])) * rng.standard_normal((G, Bg, len(iix)))
    xi[..., ivj] -= sh / CD
    return xi * sc


w = 2 * np.pi * FD
cS = (1000 / RB) / CB
F = np.zeros((G, Bg, n))
Is = 0.4
ops = {'a': A_OP, 'b': B_OP}
drv = [(P[nm], np.where(ops[op] == 1, 1.0, -1.0) * pol) for nm, (op, pol) in drives.items()]
assert all(depth[m] == 0 for m, _ in drv)


def forcing(t):
    wv = win(t - depth * TP / 4)                                                     # (N,)
    pump = 1 + pp[:, None] * np.cos(2 * w * t + np.pi * (Q + PSTEP * depth[None, :]))  # (Bg,N)
    F[:, :, iS] = cS * Vs[:, None] * wv[None, :] * pump
    s = int(np.floor((t + 0.25 * TP) / TP))     # drive of slot s: from sT - T/4 to sT + 0.75 T (fall centre)
    c = Is * np.cos(w * t) / CS if 0 <= s < NSL else 0.0
    for m, sg in drv:
        v = sg[s] * c if 0 <= s < NSL else 0.0
        F[:, :, ip[m]] = v; F[:, :, iq[m]] = -v
    return F


t0 = -1.25 * TP
tend = NSL * TP + 0.75 * TP + 1.0
nsteps = int(np.ceil((tend - t0) / dt))
nW = len(WINDOWS)
Zw = np.zeros((nW, G, Bg, N, NSL), complex)
woff = np.array([[depth[m] * TP / 4 + TP / 4 + dl for m in range(N)] for dl, _ in WINDOWS])   # (nW,N)
wlen = np.array([nc * TC for _, nc in WINDOWS])
if TRACE:
    bl = ndiv // 2
    nblk = nsteps // bl
    Zb = np.zeros((G, Bg, N, nblk), np.complex64)
    cur = np.zeros((G, Bg, N), complex)
    tb = t0 + dt * (np.arange(nblk) * bl)
arN = np.arange(N)


def observe(k, t, x):
    global cur
    v = 0.5 * (x[..., ip] - x[..., iq])
    e = v * np.exp(-1j * w * t)
    for iw in range(nW):
        u = t - woff[iw]
        s = np.floor(u / TP).astype(int)
        act = ((u - s * TP) < wlen[iw]) & (s >= 0) & (s < NSL)
        if act.any():
            Zw[iw][:, :, arN[act], s[act]] += e[:, :, act] * (2 * dt / wlen[iw])
    if TRACE:
        cur += e
        if k % bl == 0:
            j = k // bl - 1
            if j < nblk:
                Zb[..., j] = cur * (2.0 / bl)
            cur[:] = 0


x = np.zeros((G, Bg, n))
Nn = nonlin(x)
t = t0
rhs = x + dt * (Nn + forcing(t + dt) + (noise_term(x) if noise else 0))
xn = np.matmul(rhs, MbeT)
xprev, x = x, xn
Nprev, Nn = Nn, nonlin(x)
t = t + dt
observe(1, t, x)
vmax = 0.0
for k in range(2, nsteps + 1):
    rhs = 4 * x - xprev + 2 * dt * (2 * Nn - Nprev + forcing(t + dt))
    if noise:
        rhs += 2 * dt * noise_term(x)
    xn = np.matmul(rhs, Mbd2T)
    xprev, x = x, xn
    Nprev, Nn = Nn, nonlin(x)
    t = t + dt
    observe(k, t, x)
    if k % 2000 == 0:
        vmax = max(vmax, np.abs(x[..., ivj]).max())
        if not np.isfinite(x).all():
            print('NON-FINITE at t', t); break
out = dict(Zw=Zw, windows=np.array(WINDOWS), dt=dt, ndiv=ndiv, Vs=Vs, p=pp, pf=pf, groups=np.array(groups),
           g=np.array(gs), layout=lname, pstep=PSTEP, q=Q, NSL=NSL, seed=seed, vjmax=vmax)
if TRACE:
    out.update(Zb=Zb, tb=tb)
np.savez_compressed(os.path.join(here, 'res', 'run_%s.npz' % tag), **out)
el = time.time() - t0c
msg = 'run %s %s G %d Bg %d steps %d dt %.5f ps vjmax %.3f V time %.1f s' % (tag, lname, G, Bg, nsteps, dt, vmax, el)
print(msg)
with open(os.path.join(here, 'res', 'timing.log'), 'a') as fh:
    fh.write(msg + '\n')
