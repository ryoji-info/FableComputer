"""Faster version of run.py (same model, same SBDF2 scheme, same read windows).
usage: run2.py TAG LAYOUT NDIV GROUPS POINTS [SEED] [PSTEP] [Q] [DTYPE]
  GROUPS : comma list draw:kfac   (draw 0 = no spread; else g ~ N(0,1) per pair from rng(5000+draw))
  POINTS : comma list Vs:p:pf
  DTYPE  : f8 (default) or f4 for the state and propagation matrices
Changes against run.py, algebraically identical: forcing tables precomputed; the step
  x_{n+1} = [4x_n - x_{n-1} + 2dt(2N_n - N_{n-1} + F_{n+1} + xi_n)] (3I - 2dtA)^{-1}
is done as one product of [4x-xprev, 2dt(2y-yprev), 2dt u_S, 2dt u_drv, 2dt z] with a stacked matrix, where y are the
diode terms (only the ix rows are non-zero), u_S the supply forcing (only the S rows), u_drv the launcher currents
(stub rows of driven pairs), z the unit normals of the thermal sources (through the noise matrix), and the shot noise
(vj rows).  Random numbers drawn in chunks.
"""
import sys, os, time
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from model import *
from netx import *

WINDOWS = [(2.0, 2.0), (0.0, 1.0), (2.0, 4.0), (5.0, 2.0)]

tag, lname, ndiv = sys.argv[1], sys.argv[2], int(sys.argv[3])
groups = [(int(s.split(':')[0]), float(s.split(':')[1])) for s in sys.argv[4].split(',')]
pts = [tuple(float(u) for u in s.split(':')) for s in sys.argv[5].split(',')]
seed = int(sys.argv[6]) if len(sys.argv) > 6 else 1
PSTEP = float(sys.argv[7]) if len(sys.argv) > 7 else 1.5
Q = float(sys.argv[8]) if len(sys.argv) > 8 else 0.25
DT_ = np.float32 if (len(sys.argv) > 9 and sys.argv[9] == 'f4') else np.float64
cell = 'F'
names, depth, links, drives, spair = layout(lname)
P = {nm: i for i, nm in enumerate(names)}
N = len(names)
NSL = 32
dt = TC / ndiv
Vs = np.array([p[0] for p in pts]); pp = np.array([p[1] for p in pts]); pf = np.array([p[2] for p in pts])
Bg, G = len(pts), len(groups)
L0 = CELLS[cell][1]
t0c = time.time()
n = NS * N
I = np.eye(n)
ivj, iix = vj_idx(N), ix_idx(N)
ip, iq = vst_idx(N)
iS = np.array([idx(m, name='vS') for m in range(N)])
ops = {'a': A_OP, 'b': B_OP}
drv = [(P[nm], np.where(ops[op] == 1, 1.0, -1.0) * pol) for nm, (op, pol) in drives.items()]
nd = len(drv)
noise = bool((pf > 0).any())
cS = (1000 / RB) / CB
gs, Ms, Bes = [], [], []
for d, kf in groups:
    g = np.zeros(N) if d == 0 else np.random.default_rng(5000 + d).standard_normal(N)
    gs.append(g)
    A, Li = build_net(cell, L0 * (1 + 0.03 * g), names, links, kfac=kf)
    rows = []
    # rows: x-part (n), diode (2N), supply (N), drive (nd), [thermal (nsrc), shot (2N)]
    E_ix = np.zeros((2 * N, n)); E_ix[np.arange(2 * N), iix] = 1.0
    E_S = np.zeros((N, n)); E_S[np.arange(N), iS] = cS
    E_d = np.zeros((nd, n))
    for j, (m, _) in enumerate(drv):
        E_d[j, ip[m]] = 1.0 / CS; E_d[j, iq[m]] = -1.0 / CS
    blocks = [np.eye(n), E_ix, E_S, E_d]
    if noise:
        Bn = noise_matrix(cell, Li, N, dt)
        E_sh = np.zeros((2 * N, n)); E_sh[np.arange(2 * N), ivj] = -1.0 / CD
        blocks += [Bn, E_sh]
    Bstack = np.vstack(blocks)
    for (Mx, lst) in ((np.linalg.inv(3 * I - 2 * dt * A).T, Ms), (np.linalg.inv(I - dt * A).T, Bes)):
        lst.append(Bstack @ Mx)
MS = np.array(Ms).astype(DT_)       # (G, K, n)
MBE = np.array(Bes).astype(DT_)
K = MS.shape[1]
nsrc = (K - n - 2 * N - N - nd - 2 * N) if noise else 0
off_ix, off_S, off_d = n, n + 2 * N, n + 3 * N
off_z = n + 3 * N + nd
off_sh = off_z + nsrc
w = 2 * np.pi * FD
Is = 0.4
t0 = -1.25 * TP
tend = NSL * TP + 0.75 * TP + 1.0
nsteps = int(np.ceil((tend - t0) / dt))
# forcing tables at t_{k} = t0 + k dt, k = 1..nsteps (forcing is taken at t_{n+1})
tk = t0 + dt * np.arange(nsteps + 1)
WIN = np.stack([win(tk - dd * TP / 4) for dd in range(4)], 1)                      # (nsteps+1, 4)
PC = np.stack([np.cos(2 * w * tk + np.pi * (Q + PSTEP * dd)) for dd in range(4)], 1)
sl = np.floor((tk + 0.25 * TP) / TP).astype(int)
DRV = np.zeros((nsteps + 1, nd))
okk = (sl >= 0) & (sl < NSL)
for j, (m, sg) in enumerate(drv):
    DRV[okk, j] = Is * sg[sl[okk]] * np.cos(w * tk[okk])
sh_sig = 1000 * np.sqrt(QE / 1000 / (dt * 1e-12))
sc = np.sqrt(pf)[None, :, None]
rng = np.random.default_rng(seed)
CH = 400
VsB = Vs[:, None]; ppB = pp[:, None]


def ufor(k):
    u = VsB * WIN[k, depth][None, :] * (1 + ppB * PC[k, depth][None, :])        # (Bg,N)
    return u


vec = np.zeros((G, Bg, K), DT_)
nW = len(WINDOWS)
Zw = np.zeros((nW, G, Bg, N, NSL), complex)
woff = np.array([[depth[m] * TP / 4 + TP / 4 + dl for m in range(N)] for dl, _ in WINDOWS])
wlen = np.array([nc * TC for _, nc in WINDOWS])
# per step and window: active pairs and slot (precomputed)
arN = np.arange(N)
ACT = []
for iw in range(nW):
    u = tk[:, None] - woff[iw][None, :]
    s = np.floor(u / TP).astype(int)
    act = ((u - s * TP) < wlen[iw]) & (s >= 0) & (s < NSL)
    ACT.append((act, s))
EXP = np.exp(-1j * w * tk)


def diode(x):
    return (FRAC / TAU) * I_full(x[..., ivj])


def fill(k, x, xprev, y, yprev, first, zt):
    if first:
        vec[..., :n] = x
        vec[..., off_ix:off_S] = dt * y
        fac = dt
    else:
        vec[..., :n] = 4 * x - xprev
        vec[..., off_ix:off_S] = 2 * dt * (2 * y - yprev)
        fac = 2 * dt
    vec[..., off_S:off_d] = fac * ufor(k)[None]
    vec[..., off_d:off_z] = fac * DRV[k][None, None, :]
    if noise:
        vec[..., off_z:off_sh] = fac * zt[..., :nsrc] * sc
        vec[..., off_sh:] = fac * sh_sig * np.sqrt(np.abs(x[..., iix])) * zt[..., nsrc:] * sc


def observe(k, x):
    v = 0.5 * (x[..., ip] - x[..., iq])
    e = v * EXP[k]
    for iw in range(nW):
        act, s = ACT[iw]
        a = act[k]
        if a.any():
            Zw[iw][:, :, arN[a], s[k][a]] += e[:, :, a] * (2 * dt / wlen[iw])


x = np.zeros((G, Bg, n), DT_)
xprev = x.copy()
y = diode(x)
yprev = y
zbuf = None
vmax = 0.0
for k in range(1, nsteps + 1):
    if noise:
        j = (k - 1) % CH
        if j == 0:
            zbuf = rng.standard_normal((CH, G, Bg, nsrc + 2 * N)).astype(DT_)
        zt = zbuf[j]
    else:
        zt = None
    fill(k, x, xprev, y, yprev, k == 1, zt)
    xn = np.matmul(vec, MBE if k == 1 else MS)
    xprev, x = x, xn
    yprev, y = y, diode(x)
    observe(k, x)
    if k % 2000 == 0:
        vmax = max(vmax, float(np.abs(x[..., ivj]).max()))
        if not np.isfinite(x).all():
            print('NON-FINITE at step', k); break
out = dict(Zw=Zw, windows=np.array(WINDOWS), dt=dt, ndiv=ndiv, Vs=Vs, p=pp, pf=pf, groups=np.array(groups),
           g=np.array(gs), layout=lname, pstep=PSTEP, q=Q, NSL=NSL, seed=seed, vjmax=vmax, dtype=str(np.dtype(DT_)))
np.savez_compressed(os.path.join(here, 'res', 'run_%s.npz' % tag), **out)
el = time.time() - t0c
msg = 'run2 %s %s G %d Bg %d steps %d dt %.5f ps %s vjmax %.3f V time %.1f s' % (tag, lname, G, Bg, nsteps, dt,
                                                                              np.dtype(DT_), vmax, el)
print(msg)
with open(os.path.join(here, 'res', 'timing.log'), 'a') as fh:
    fh.write(msg + '\n')
