# usage: run_lay.py <layout r|c|row3> <Vs> <p> <dt> <tag> [noise_f spread draw0 ndraw]
import sys, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
import rtdsim as R
import layouts as LY

D = __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "res")
import os
os.makedirs(D, exist_ok=True)

name = sys.argv[1]; Vs = float(sys.argv[2]); p = float(sys.argv[3]); dt = float(sys.argv[4]); tag = sys.argv[5]
nf = float(sys.argv[6]) if len(sys.argv) > 6 else 0.0
spread = float(sys.argv[7]) if len(sys.argv) > 7 else 0.0
d0 = int(sys.argv[8]) if len(sys.argv) > 8 else 0
nd = int(sys.argv[9]) if len(sys.argv) > 9 else 1

if name == 'r': lay = LY.layout_r()
elif name == 'c': lay = LY.layout_c()
elif name.startswith('row'): lay = LY.layout_row(int(name[3:]))
N = lay.N
SPREAD_SEED = 20261123
NOISE_SEED = 777000
G = np.random.default_rng(SPREAD_SEED + (0 if name == 'r' else 1)).standard_normal((64, N))  # fixed draws, same at every point
draws = list(range(d0, d0 + nd))
lodd = np.array([R.LODD * (1 + spread * G[k]) for k in draws]) if spread > 0 else np.full((nd, N), R.LODD)
seeds = [NOISE_SEED + 1000 * (0 if name == 'r' else 1) + k for k in draws]
t0 = -4.0
dmax = lay.depth.max()
t1 = 31 * R.TP + dmax * R.TP / 4 + R.RD_START + R.RD_LEN + 0.3
tic = time.time()
sim = R.Sim(lay, dt, lodd)
out = sim.run(t0, t1, Vs, p, noise_f=nf, seeds=seeds)
Xs = np.array([R.read_slots(out['t'], out['odd'][b], lay.depth) for b in range(nd)])
fn = os.path.join(D, '%s_%s.npz' % (name, tag))
np.savez_compressed(fn, X=Xs, draws=np.array(draws), Vs=Vs, p=p, dt=dt, nf=nf, spread=spread,
                    odd=out['odd'][:, ::4] if nd == 1 else np.zeros(1), t=out['t'][::4])
print('saved', fn, 'secs %.1f' % (time.time() - tic))
