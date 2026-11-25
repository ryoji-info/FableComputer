"""Ten-pair bit-serial adder (addendum to spec D225), cell F.
usage: adder.py TAG NDIV OPS GROUPS POINTS [SEED] [P]
  OPS    : main | loop
  GROUPS : comma list of draw:kfac   (draw 0 = no spread; spread 3 % on L_odd, g from rng(2000+draw))
  POINTS : comma list of Vs:q:pfac   (pfac = noise POWER factor; 0 = no noise)
Saves block averages of the demodulated odd-mode voltage, blocks of TC/8.
"""
import sys, os, time
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from model import *
from net import *
from sim16 import Sim16

tag, ndiv, ops = sys.argv[1], int(sys.argv[2]), sys.argv[3]
groups = [(int(s.split(':')[0]), float(s.split(':')[1])) for s in sys.argv[4].split(',')]
pts = [tuple(float(u) for u in s.split(':')) for s in sys.argv[5].split(',')]
seed = int(sys.argv[6]) if len(sys.argv) > 6 else 1
PUMP = float(sys.argv[7]) if len(sys.argv) > 7 else 0.25
DRVEND = float(sys.argv[8]) if len(sys.argv) > 8 else 0.0   # <0: drive ends this many ps before the fall centre
assert ndiv % 8 == 0
cell = 'F'
N = 10
NSL = 32
dt = TC / ndiv
a_op, b_op = (A_OP, B_OP) if ops == 'main' else loop_operands(NSL)
Vs = np.array([p[0] for p in pts]); q = np.array([p[1] for p in pts]); pf = np.array([p[2] for p in pts])
Bg = len(pts); G = len(groups)
L0 = CELLS[cell][1]
ALs, gs = [], []
for d, kf in groups:
    g = np.zeros(N) if d == 0 else np.random.default_rng(2000 + d).standard_normal(N)
    gs.append(g)
    ALs.append(build_net(cell, L0 * (1 + 0.03 * g), kfac=kf))
t0c = time.time()
sim = Sim16(cell, ALs, N, dt, np.sqrt(pf), seed=seed)
n = sim.n
w = 2 * np.pi * FD
dep = DEPTH
iS = sim.iS
ip, iq = sim.ip, sim.iq
cS = (1000 / RB) / CB
F = np.zeros((G, Bg, n))
Is = 0.4
sa = np.where(a_op == 1, 1.0, -1.0); sb = np.where(b_op == 1, 1.0, -1.0)


def forcing(t):
    wv = win(t - dep * TP / 4)                                                        # (N,)
    pump = 1 + PUMP * np.cos(2 * w * t + np.pi * (q[:, None] + dep[None, :]))          # (Bg,N)
    F[:, :, iS] = cS * Vs[:, None] * wv[None, :] * pump
    s = int(np.floor((t + 0.25 * TP) / TP))          # input pairs have depth 0
    if DRVEND < 0 and (t - s * TP) > 0.75 * TP + DRVEND:
        s = -1                                        # drive of slot s cut DRVEND ps before the fall centre
    if 0 <= s < NSL:
        c = Is * np.cos(w * t) / CS
        ia, ib = sa[s] * c, sb[s] * c
    else:
        ia = ib = 0.0
    F[:, :, ip[0]] = ia; F[:, :, iq[0]] = -ia
    F[:, :, ip[1]] = ib; F[:, :, iq[1]] = -ib
    return F


bl = ndiv // 8
t0 = -1.25 * TP
tend = NSL * TP + 0.75 * TP + 2.0
nsteps = int(np.ceil((tend - t0) / dt))
nblk = nsteps // bl
Zb = np.zeros((G, Bg, N, nblk), np.complex64)
tb = t0 + dt * (np.arange(nblk) * bl)          # block covers steps k = j*bl+1 .. (j+1)*bl, i.e. times (tb, tb+bl*dt]
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
sim.run(x0, t0, nsteps, forcing, obs)
np.savez(os.path.join(here, 'run_%s.npz' % tag), Zb=Zb, tb=tb, bl=bl, dt=dt, ndiv=ndiv, Vs=Vs, q=q, pf=pf,
         groups=np.array(groups), g=np.array(gs), a=a_op, b=b_op, NSL=NSL, seed=seed, pump=PUMP)
el = time.time() - t0c
print('run', tag, 'G', G, 'Bg', Bg, 'steps', nsteps, 'dt %.5f ps' % dt, 'time %.1f s' % el)
with open(os.path.join(here, 'timing.txt'), 'a') as fh:
    fh.write('%s G %d Bg %d steps %d dt %.5f time %.1f s\n' % (tag, G, Bg, nsteps, dt, el))
