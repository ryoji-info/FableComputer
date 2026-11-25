"""SBDF2 integrator as in rebuild15 sim.py, but built from given (A, Li) per group and with a noise
amplitude scale per batch point (scale = sqrt(noise power factor); 0 = no noise)."""
import numpy as np
from model import *


class Sim16:
    def __init__(self, cell, ALs, N, dt, nscale, seed=0):
        self.cell = cell
        self.G = len(ALs); self.N = N
        self.nscale = np.asarray(nscale, float)          # (Bg,)
        self.Bg = len(self.nscale)
        self.n = NS * N
        self.dt = dt
        As = [A for A, _ in ALs]; Lis = [Li for _, Li in ALs]
        I = np.eye(self.n)
        self.MbeT = np.array([np.linalg.inv(I - dt * A).T for A in As])
        self.Mbd2T = np.array([np.linalg.inv(3 * I - 2 * dt * A).T for A in As])
        self.ivj = vj_idx(N); self.iix = ix_idx(N)
        self.ip, self.iq = vst_idx(N)
        self.iS = np.array([idx(m, name='vS') for m in range(N)])
        self.noise = bool((self.nscale > 0).any())
        if self.noise:
            self.rng = np.random.default_rng(seed)
            self.BnT = np.array([noise_matrix(cell, Li, N, dt) for Li in Lis])     # (G, nsrc, n)
            self.sh_sig = 1000 * np.sqrt(QE / 1000 / (dt * 1e-12))
            self.sc = self.nscale[None, :, None]

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
        return xi * self.sc

    def run(self, x0, t0, nsteps, forcing, observe=None):
        dt = self.dt
        x = x0.copy()
        Nn = self.nonlin(x)
        t = t0
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
