"""Batched SBDF2 integrator for one pair or a row.
x shape (G, Bg, n): G groups with their own linear matrix (spread draws), Bg points per group.
"""
import numpy as np
from model import *


class Sim:
    def __init__(self, cell, Lodd_groups, dt, Bg, noise=False, seed=0, Mmode='geo'):
        self.cell = cell
        Lodd_groups = np.atleast_2d(Lodd_groups)
        self.G, self.N = Lodd_groups.shape
        self.Bg = Bg
        self.n = NS * self.N
        self.dt = dt
        As, Lis = [], []
        for L in Lodd_groups:
            A, Li = build(cell, L, Mmode=Mmode)
            As.append(A); Lis.append(Li)
        self.A = np.array(As)
        I = np.eye(self.n)
        self.MbeT = np.array([np.linalg.inv(I - dt * A).T for A in As])
        self.Mbd2T = np.array([np.linalg.inv(3 * I - 2 * dt * A).T for A in As])
        self.ivj = vj_idx(self.N)
        self.iix = ix_idx(self.N)
        self.ip, self.iq = vst_idx(self.N)
        self.iS = np.array([idx(m, name='vS') for m in range(self.N)])
        self.noise = noise
        if noise:
            self.rng = np.random.default_rng(seed)
            self.BnT = np.array([noise_matrix(cell, Li, self.N, dt) for Li in Lis])  # (G, nsrc, n)
            self.sh_sig = 1000 * np.sqrt(QE / 1000 / (dt * 1e-12))
        self.step_count = 0

    def nonlin(self, x):
        out = np.zeros_like(x)
        out[..., self.iix] = FRAC * I_full(x[..., self.ivj]) / TAU
        return out

    def noise_term(self, x):
        G, Bg = x.shape[:2]
        z = self.rng.standard_normal((G, Bg, self.BnT.shape[1]))
        xi = np.matmul(z, self.BnT)
        sh = self.sh_sig * np.sqrt(np.abs(x[..., self.iix])) * self.rng.standard_normal((G, Bg, len(self.iix)))
        xi[..., self.ivj] -= sh / CD
        return xi

    def run(self, x0, t0, nsteps, forcing, observe=None):
        """forcing(t) -> (G,Bg,n) derivative contribution; observe(k, t, x) called after each step."""
        dt = self.dt
        x = x0.copy()
        Nn = self.nonlin(x)
        t = t0
        # first step backward Euler
        rhs = x + dt * (Nn + forcing(t + dt) + (self.noise_term(x) if self.noise else 0))
        xn = np.matmul(rhs, self.MbeT)
        xprev, x = x, xn
        Nprev, Nn = Nn, self.nonlin(x)
        t = t + dt
        if observe: observe(1, t, x)
        for k in range(2, nsteps + 1):
            rhs = 4 * x - xprev + 2 * dt * (2 * Nn - Nprev + forcing(t + dt))
            if self.noise:
                rhs += 2 * dt * self.noise_term(x)
            xn = np.matmul(rhs, self.Mbd2T)
            xprev, x = x, xn
            Nprev, Nn = Nn, self.nonlin(x)
            t = t + dt
            if observe: observe(k, t, x)
        return x, t
