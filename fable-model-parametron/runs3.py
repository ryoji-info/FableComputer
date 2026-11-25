# -*- coding: utf-8 -*-
"""Common part of the runner: job arguments, the cell values, building a batch of pairs, the integration loop
and the reader of levels and phases (used by chain4.py).

Job arguments (key=value on the command line after the experiment name):
  backend=numpy|torch   numpy (the default) runs in double precision; torch is imported only when asked for,
                        and runs in single precision on a graphics processor if one is present
  out=<folder>          where settings are read and results written (default: the folder "out" beside this file)
  dt=<ps>               time step in model ps (default 0.0025)
  nseg=<n>              sections of each stub (default 4, as in every batch of the paper)
  f=<THz>               frequency of the reader (default 1.076, as in every batch of the paper)
  edge=<ps>             duration of the clock edges (default 3.0)
  iv=<a,b,c>            diode law (default 0.9333,1.667,2.218, as in every batch; "central" gives the plain law)
  seed=<n>, pseed=<n>   noise generator (default 5) and spread generators (default 11)

Level and phase: the level of a pair is half the difference of the voltages at the far ends (node B) of the
stubs of its two halves, read as the part at the reader frequency of a least-squares fit of
[1, t, cos, sin] over windows of 1 model ps.  Model units: V, mA, fF, nH, kohm, ps, um; see MODEL.md.
Estimates only.
"""
import math
import os
import sys
import time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
import cellbase
import fdtd3

args = dict(a.split("=", 1) for a in sys.argv[2:] if "=" in a)
EXP = sys.argv[1] if len(sys.argv) > 1 else "none"
backend = args.get("backend", "numpy")
OUT = args.get("out", os.path.join(HERE, "out"))
os.makedirs(OUT, exist_ok=True)
if backend == "torch":
    import torch as xp
else:
    xp = np


def LOG(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


DT = float(args.get("dt", "0.0025"))            # time step (model ps)
NSEG = int(args.get("nseg", "4"))               # sections per stub
F_REF = float(args.get("f", "1.076"))           # reader frequency (model THz)
EDGE = float(args.get("edge", "3.0"))           # clock edge (model ps)
IV_ARG = args.get("iv", ",".join("%g" % x for x in cellbase.IV))
KEYS_H = ("Z0", "s", "tau", "l", "area", "cd", "tau_d", "rho", "RL", "Cp", "Rk", "Ck", "jscale")   # of a half
KEYS_P = ("Rb", "Cb", "Lodd", "kL")                                                                # of a pair


def tonp(x):
    return x if xp is np else x.detach().cpu().numpy()


def cell_info(name, c_end=0.0):
    """Base values of one design (cellbase.py)."""
    return cellbase.cell_info(name, c_end)


def info_json(names):
    return cellbase.info_json(names)


def build(rows, n=1, links=None, linkC=None, CpadB=0.0, jsig=0.0, jpair=0.0, jdiff=0.0, lsig=0.0, seed=11, rsig=0.0, **common):
    """rows: list of dicts with 'design', optional 'c_end', overrides (key) and multipliers (key_x).
    jsig: relative spread (one standard deviation) of the diode current from pair to pair (both diodes of a
    pair alike); jpair: spread of the difference between the two diodes of a pair; jdiff: a fixed relative
    difference between them (+ half above, - half below); lsig: spread of the tank inductance from pair to
    pair; rsig: spread of the damping resistor from pair to pair.  Each may be a number or one value per run."""
    B = len(rows)
    cols = {k: np.zeros(B) for k in KEYS_H + KEYS_P}
    for i, r in enumerate(rows):
        base = cell_info(r["design"], r.get("c_end", 0.0))
        for k in cols:
            cols[k][i] = r.get(k, base[k]) * r.get(k + "_x", 1.0)
    rng = np.random.default_rng(seed)
    b3 = lambda v: np.broadcast_to(np.asarray(v, float).reshape(-1, 1, 1), (B, 1, 1))
    half = np.array([0.5, -0.5]).reshape(1, 1, 2)
    g1, g2, g3 = rng.standard_normal((B, n, 1)), rng.standard_normal((B, n, 1)), rng.standard_normal((B, n))
    kw = dict(cols)
    kw["jscale"] = cols["jscale"][:, None, None] * (1.0 + b3(jsig) * g1) * (1.0 + (b3(jpair) * g2 + b3(jdiff)) * half)
    kw["Lodd"] = cols["Lodd"][:, None] * (1.0 + b3(lsig)[:, :, 0] * g3)
    if np.any(np.asarray(rsig, float) != 0.0):          # spread of the damping resistor from pair to pair, both halves alike; its own generator
        g4 = np.random.default_rng(seed + 477).standard_normal((B, n, 1))
        kw["RL"] = cols["RL"][:, None, None] * (1.0 + b3(rsig) * g4)
    fab = fdtd3.PairFabric(B, n, xp=xp, N=NSEG, dt=DT, links=links, linkC=linkC, CpadB=CpadB, **kw, **common)
    return fab


class Reader:
    """Least-squares fit of [1, tau, cos, sin] over windows of `win` ps to the signals given to add()."""

    def __init__(self, fab, f_ref, win=1.0, names=("D",)):
        self.fab, self.win, self.names = fab, win, names
        self.nw = int(round(win / fab.dt))
        self.w = fdtd3.W0 * f_ref
        z = fab._zeros((fab.B, fab.n))
        self.r = {nm: [z + 0, z + 0, z + 0, z + 0] for nm in names}
        self.g = dict(c=0.0, s=0.0, tc=0.0, ts=0.0, cc=0.0, ss=0.0, cs=0.0)
        self.k = 0
        self.t1 = self.t2 = 0.0

    def add(self, t, **sig):
        tau = (self.k + 0.5) / self.nw - 0.5
        c, s = math.cos(self.w * t), math.sin(self.w * t)
        g = self.g
        g["c"] += c; g["s"] += s; g["tc"] += tau * c; g["ts"] += tau * s
        g["cc"] += c * c; g["ss"] += s * s; g["cs"] += c * s
        self.t1 += tau
        self.t2 += tau * tau
        for nm in self.names:
            v = sig[nm]
            r = self.r[nm]
            r[0] += v; r[1] += tau * v; r[2] += c * v; r[3] += s * v
        self.k += 1
        return self.k == self.nw

    def solve(self):
        """Returns {name: (amplitude, phase)} as numpy arrays [B, n] and resets."""
        g = self.g
        G = np.array([[self.nw, self.t1, g["c"], g["s"]], [self.t1, self.t2, g["tc"], g["ts"]],
                      [g["c"], g["tc"], g["cc"], g["cs"]], [g["s"], g["ts"], g["cs"], g["ss"]]])
        Gi = np.linalg.inv(G)
        out = {}
        for nm in self.names:
            rhs = np.stack([tonp(x).astype(np.float64) for x in self.r[nm]], -1)
            x = rhs @ Gi.T
            out[nm] = (np.hypot(x[..., 2], x[..., 3]), np.arctan2(-x[..., 3], x[..., 2]))
            for v in self.r[nm]:
                v *= 0
        self.g = dict(c=0.0, s=0.0, tc=0.0, ts=0.0, cc=0.0, ss=0.0, cs=0.0)
        self.k = 0
        self.t1 = self.t2 = 0.0
        return out


def run(fab, t_end, vclk_fn, iB_fn, win=1.0, progress=None):
    """Advance to t_end.  Per window and pair: odd level and phase at the far ends, even level, mean
    junction voltage, mean supply power of the pair (mW)."""
    nt = int(round(t_end / fab.dt))
    rd = Reader(fab, F_REF, win, names=("D", "E"))
    nwin = nt // rd.nw
    B, n = fab.B, fab.n
    z = fab._zeros((B, n))
    acc = dict(vj=z + 0, e=z + 0)
    res = {k: np.zeros((nwin, B, n), np.float32) for k in ("amp", "ph", "ampE", "vj", "p")}
    for k in range(nt):
        t = (k + 1) * fab.dt
        vclk = vclk_fn(t)
        fab.step(vclk, iB_fn(t) if iB_fn else 0.0)
        acc["vj"] += 0.5 * (fab.vj[..., 0] + fab.vj[..., 1])
        acc["e"] += vclk * (vclk - fab.vb) / fab.Rb
        if rd.add(t, D=fab.odd_B(), E=fab.even_B()):
            j = (k + 1) // rd.nw - 1
            o = rd.solve()
            res["amp"][j], res["ph"][j] = o["D"][0], o["D"][1]
            res["ampE"][j] = o["E"][0]
            res["vj"][j] = tonp(acc["vj"]) / rd.nw
            res["p"][j] = tonp(acc["e"]) / rd.nw
            for a_ in acc.values():
                a_ *= 0
            if progress and (j + 1) % progress == 0:
                LOG("   window %d of %d" % (j + 1, nwin))
    return res


def rc_t(x, edge):
    """Raised-cosine edge: 0 before -edge/2, 1 after +edge/2."""
    y = xp.clip(x / edge + 0.5, 0.0, 1.0) if xp is not np else np.clip(x / edge + 0.5, 0.0, 1.0)
    return 0.5 - 0.5 * xp.cos(math.pi * y)
