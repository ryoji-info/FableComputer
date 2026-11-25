"""Usage: run_lay.py <layout a|c> <out.npz> <Vs comma list> <p comma list> <noise factor> <spread 0|1> <ndraws> <noise seed> [hdiv]
Every combination of Vs and p is one batch member group; with ndraws>1 each group has ndraws members
(draw j uses spread row j of the fixed spread matrix and its own noise stream)."""
import sys, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
import warnings; warnings.simplefilter("ignore")
from sim import *

which, out = sys.argv[1], sys.argv[2]
Vl = [float(v) for v in sys.argv[3].split(',')]
pl = [float(v) for v in sys.argv[4].split(',')]
nf = float(sys.argv[5]); spread = int(sys.argv[6]); nd = int(sys.argv[7]); seed = int(sys.argv[8])
hdiv = int(sys.argv[9]) if len(sys.argv) > 9 else 128
lay = layout_c() if which == 'c' else layout_a()
t1 = 467.0 if which == 'c' else 511.0
# fixed spread draws: 64 rows, same for every point of every scan of this layout
G = np.random.default_rng(20261123 if which == 'c' else 20261124).standard_normal((64, lay.N))
Vs, ps, gg, rows = [], [], [], []
for v in Vl:
    for p in pl:
        for j in range(nd):
            Vs.append(v); ps.append(p); rows.append(j)
            gg.append(G[j] if spread else np.zeros(lay.N))
Vs = np.array(Vs); ps = np.array(ps); gg = np.array(gg)
h = Tc / hdiv
dec = hdiv // 32
t = time.time()
tr, rec, xf = simulate(lay, Vs, ps, gg, np.full(len(Vs), nf), seed, h, -2.0, t1, dec)
Z = read_slots(lay, tr, rec, 32)
np.savez(out, Z=Z, Vs=Vs, p=ps, g=gg, rows=np.array(rows), nf=nf, hdiv=hdiv, seed=seed)
print("done", out, "members", len(Vs), "time", round(time.time() - t, 1), "finite", np.all(np.isfinite(Z)))
