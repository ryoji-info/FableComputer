# -*- coding: utf-8 -*-
"""Time-domain model of the pair of resonant-tunnelling diodes (the integrator of the package).

One pair has two identical halves (index 0: the + half, index 1: the - half).  Each half:
    supply node b (common to the pair) -- contact rho -- diode (junction C_d with the delayed conduction
    current) -- pad;  pad -- C_p -- ground;  pad -- coupler R_k (C_k infinite in the design) -- node A
    of its own short stub;  the far end of the stub, node B, is where the signal is read and the drive enters.
The stub is a transmission line of a few sections; in the design it is lossless (Drude time 1e6 ps) and
short (0.13 fF and 1.3 pH in model units), so it acts as a small capacitance behind R_k.  Optional
capacitors between the node B ends of different pairs (argument links/linkC) are not part of the design.
The two pads are joined by a centre-tapped inductor with a grounded tap: each pad sees a half winding
(self inductance L_h, series resistance R_L) to ground, and the halves are coupled so that the odd mode
sees L_h (1 + k) per half and the even mode L_h (1 - k).  Pairs are linked by mutual inductances between
their inductors (argument mlinks/mk).  The supply node has the resistor R_b to the clock and a capacitance
C_b to ground.

Numerics: a staggered grid for the stubs (leapfrog, Crank-Nicolson Drude loss) and the trapezoidal rule
for the eleven lumped variables of a pair
    y = [V0+, Vp+, vj+, iL+, vk+, V0-, Vp-, vj-, iL-, vk-, vb]   (V0 = node A of the stub).
Units: V, mA, fF, nH, kohm, ps, um.  Noise: thermal noise of every stub section and resistor, shot
noise of the two diodes; the power of all of them can be scaled per run by a common factor.

Works with numpy (double precision) and with torch (single precision; pass xp=torch).  Estimates only.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rtdiv

W0 = 2 * math.pi * 1.0
KB = 1.380649e-23
QE = 1.602176634e-19
NS = 11                                   # lumped variables per pair
IV0, IVP, IVJ, IIL, IVK = 0, 1, 2, 3, 4   # offsets inside a half
IVB = 10


class PairFabric:
    def __init__(self, B, n, xp=np, device=None, dtype=None, N=44, dt=0.0025,
                 Z0=92.8, s=2.3312, tau=0.85, l=1.1, area=0.14, cd=12.0, tau_d=0.035, rho=0.0143,
                 Rb=0.02, Cb=1.0, Lodd=0.0063, kL=0.3, RL=0.0033, Cp=0.8, Rk=0.0328, Ck=float("inf"),
                 CpadB=0.0, links=None, linkC=None, iv=rtdiv.CENTRAL, jscale=1.0, lin=None, dL=0.0,
                 mlinks=None, mk=None):
        """Quantities of a half (Z0 ohm, s um/ps, tau ps, l um, area um^2, cd fF/um^2, tau_d ps, rho, RL, Rk
        kohm, Cp, Ck, CpadB fF, jscale) accept scalars or arrays [B], [B, n] or [B, n, 2].  Quantities of a
        pair (Rb kohm, Cb fF, Lodd nH: odd-mode inductance per half, kL: coupling of the halves, dL: relative
        difference of the two half inductances) accept scalars, [B] or [B, n].
        links: list of (qa, qb) between B-end nodes, node index q = 2 * cell + half; linkC [B, number of
        links] gives the capacitance between the two nodes (fF; zero in the design).
        The default values of the arguments belong to an earlier study; the runner always passes the cell's own.
        mlinks: list of (cell a, cell b) whose inductors couple magnetically; mk [B, number of mlinks, 4]
        (or [number of mlinks, 4], or [4]) gives per link four coefficients:
            0  odd mode to odd mode:   mutual = mk0 sqrt(Lodd_a Lodd_b)
            1  even current of a to the odd mode of b:   mk1 sqrt(Leven_a Lodd_b)
            2  even current of b to the odd mode of a:   mk2 sqrt(Leven_b Lodd_a)
            3  even mode to even mode: mk3 sqrt(Leven_a Leven_b)
        (per half; Lodd = L_h (1 + k), Leven = L_h (1 - k)).  The inductance matrix of all windings of a
        run is inverted once; its blocks inside a pair go into the implicit lumped step, the blocks between
        pairs are applied as a source taken at mid-step by extrapolation from the two last steps."""
        self.xp, self.B, self.n = xp, B, n
        if xp is np:
            self.dtype = dtype or np.float64
            self.dev = None
        else:
            self.dtype = dtype or xp.float32
            self.dev = device or ("cuda" if xp.cuda.is_available() else "cpu")
        H, Pp = self._half, self._pair
        self.N, self.dt = N, dt
        Z0k = H(Z0) * 1e-3
        s_, self.tau_ = H(s), H(tau)
        Lp, Cp_ = Z0k / s_, 1.0 / (Z0k * s_)
        dx = H(l) / N
        self.cfl = float((s_ * dt / dx).max())
        self.Lseg = (Lp * dx)[..., None] + self._zeros((B, n, 2, N))
        self.alpha = (0.5 * dt / self.tau_)[..., None]
        cn = self._zeros((B, n, 2, N + 1)) + (Cp_ * dx)[..., None]
        cn[..., 0] = 0.5 * Cp_ * dx
        cn[..., N] = 0.5 * Cp_ * dx + H(CpadB)
        self.Cn = cn
        self.area, self.jscale, self.iv, self.lin = H(area), H(jscale), iv, lin
        self.Cd = H(cd) * self.area
        self.tau_d = H(tau_d)
        self.rho, self.RL, self.Rk = H(rho), H(RL), H(Rk)
        self.Cp = H(Cp)
        self.Rb, self.Cb = Pp(Rb), Pp(Cb)
        ck = np.asarray(Ck, np.float64)
        self.invCk = H(np.where(np.isfinite(ck), 1.0 / np.where(np.isfinite(ck), ck, 1.0), 0.0))
        # ---- inductance matrix of the tapped inductor (currents from each pad to the grounded tap)
        k_, Lo, dL_ = Pp(kL), Pp(Lodd), Pp(dL)
        Lh = Lo / (1.0 + k_)
        L1, L2 = Lh * (1.0 + 0.5 * dL_), Lh * (1.0 - 0.5 * dL_)
        Mm = -k_ * Lh                              # odd mode (iL- = -iL+) then sees L_h (1 + k)
        det = L1 * L2 - Mm * Mm
        self.a11, self.a12, self.a21, self.a22 = L2 / det, -Mm / det, -Mm / det, L1 / det
        # ---- magnetic coupling between the inductors of different pairs
        self.mlinks = list(mlinks or [])
        self.Goff = None
        if self.mlinks:
            f64 = (lambda a: np.asarray(a, np.float64)) if xp is np else (lambda a: a.detach().cpu().numpy().astype(np.float64))
            L1n, L2n, Mmn, Lon, Levn = f64(L1), f64(L2), f64(Mm), f64(Lo), f64(Lh * (1.0 - k_))
            nl = len(self.mlinks)
            mkn = np.broadcast_to(np.asarray(mk if xp is np or not xp.is_tensor(mk) else mk.detach().cpu().numpy(), np.float64), (B, nl, 4))
            Lg = np.zeros((B, 2 * n, 2 * n))
            for c in range(n):
                Lg[:, 2 * c, 2 * c] = L1n[:, c]
                Lg[:, 2 * c + 1, 2 * c + 1] = L2n[:, c]
                Lg[:, 2 * c, 2 * c + 1] = Mmn[:, c]
                Lg[:, 2 * c + 1, 2 * c] = Mmn[:, c]
            for j, (ca, cb) in enumerate(self.mlinks):
                Moo = mkn[:, j, 0] * np.sqrt(Lon[:, ca] * Lon[:, cb])
                M1 = mkn[:, j, 1] * np.sqrt(Levn[:, ca] * Lon[:, cb])          # odd of b from even of a
                M2 = mkn[:, j, 2] * np.sqrt(Levn[:, cb] * Lon[:, ca])          # odd of a from even of b
                Mee = mkn[:, j, 3] * np.sqrt(Levn[:, ca] * Levn[:, cb])
                blk = ((0.5 * (Mee + M2 + M1 + Moo), 0.5 * (Mee - M2 + M1 - Moo)),          # [half of b][half of a]
                       (0.5 * (Mee + M2 - M1 - Moo), 0.5 * (Mee - M2 - M1 + Moo)))
                for hb in (0, 1):
                    for ha in (0, 1):
                        Lg[:, 2 * cb + hb, 2 * ca + ha] += blk[hb][ha]
                        Lg[:, 2 * ca + ha, 2 * cb + hb] += blk[hb][ha]
            self.Lglob = Lg
            G = np.linalg.inv(Lg)
            ar_ = np.arange(n)
            self.a11, self.a12 = self._arr(G[:, 2 * ar_, 2 * ar_]), self._arr(G[:, 2 * ar_, 2 * ar_ + 1])
            self.a21, self.a22 = self._arr(G[:, 2 * ar_ + 1, 2 * ar_]), self._arr(G[:, 2 * ar_ + 1, 2 * ar_ + 1])
            Go = G.copy()
            for c in range(n):
                Go[:, 2 * c:2 * c + 2, 2 * c:2 * c + 2] = 0.0
            self.Goff = self._arr(Go)
        C0 = cn[..., 0]
        self.C0 = C0
        # ---- lumped system matrix [B, n, 11, 11]
        M = self._zeros((B, n, NS, NS))
        gk, gd = 1.0 / self.Rk, 1.0 / self.rho
        aa = ((self.a11, self.a12), (self.a21, self.a22))
        for h in (0, 1):
            o, oo = 5 * h, 5 * (1 - h)
            M[..., o + IV0, o + IV0] = -gk[..., h] / C0[..., h]
            M[..., o + IV0, o + IVP] = gk[..., h] / C0[..., h]
            M[..., o + IV0, o + IVK] = -gk[..., h] / C0[..., h]
            M[..., o + IVP, o + IV0] = gk[..., h] / self.Cp[..., h]
            M[..., o + IVP, o + IVP] = -(gd[..., h] + gk[..., h]) / self.Cp[..., h]
            M[..., o + IVP, o + IVJ] = -gd[..., h] / self.Cp[..., h]
            M[..., o + IVP, IVB] = gd[..., h] / self.Cp[..., h]
            M[..., o + IVP, o + IIL] = -1.0 / self.Cp[..., h]
            M[..., o + IVP, o + IVK] = gk[..., h] / self.Cp[..., h]
            M[..., o + IVJ, o + IVP] = -gd[..., h] / self.Cd[..., h]
            M[..., o + IVJ, o + IVJ] = -gd[..., h] / self.Cd[..., h]
            M[..., o + IVJ, IVB] = gd[..., h] / self.Cd[..., h]
            M[..., o + IIL, o + IVP] = aa[h][h]
            M[..., o + IIL, o + IIL] = -self.RL[..., h] * aa[h][h]
            M[..., o + IIL, oo + IVP] = aa[h][1 - h]
            M[..., o + IIL, oo + IIL] = -self.RL[..., 1 - h] * aa[h][1 - h]
            M[..., o + IVK, o + IV0] = -gk[..., h] * self.invCk[..., h]
            M[..., o + IVK, o + IVP] = gk[..., h] * self.invCk[..., h]
            M[..., o + IVK, o + IVK] = -gk[..., h] * self.invCk[..., h]
            M[..., IVB, o + IVP] = gd[..., h] / self.Cb
            M[..., IVB, o + IVJ] = gd[..., h] / self.Cb
        M[..., IVB, IVB] = -(1.0 / self.Rb + gd[..., 0] + gd[..., 1]) / self.Cb
        hh = 0.5 * dt
        eye = (np.eye(NS, dtype=self.dtype) if xp is np else xp.eye(NS, dtype=self.dtype, device=self.dev))
        inv = (np.linalg.inv(eye - hh * M) if xp is np else xp.linalg.inv(eye - hh * M))
        self.P = inv @ (eye + hh * M)
        self.Q = inv * hh
        # ---- capacitance matrix of the B ends, nodes q = 2 * cell + half
        self.links = links or []
        nq = 2 * n
        CB = cn[..., N].reshape(B, nq)
        MB = self._zeros((B, nq, nq))
        for q in range(nq):
            MB[:, q, q] = CB[:, q]
        if self.links:
            lc = self._arr(linkC)
            if lc.ndim == 1:
                lc = lc.reshape(-1, 1)
            lc = lc.expand(B, len(self.links)) if xp is not np else np.broadcast_to(lc, (B, len(self.links)))
            for j, (qa, qb) in enumerate(self.links):
                c = lc[:, j]
                MB[:, qa, qa] += c
                MB[:, qb, qb] += c
                MB[:, qa, qb] -= c
                MB[:, qb, qa] -= c
        self.MBinv = np.linalg.inv(MB) if xp is np else xp.linalg.inv(MB)
        self.noise = None
        self.reset()

    # ----------------------------------------------------------------- helpers
    def _zeros(self, shape):
        if self.xp is np:
            return np.zeros(shape, self.dtype)
        return self.xp.zeros(shape, dtype=self.dtype, device=self.dev)

    def _arr(self, val):
        xp = self.xp
        if xp is np:
            return np.asarray(val, self.dtype)
        return val.to(self.dev, self.dtype) if xp.is_tensor(val) else xp.as_tensor(np.asarray(val, np.float64), dtype=self.dtype, device=self.dev)

    def _expand(self, a, shape):
        if self.xp is np:
            return np.broadcast_to(a, shape).copy()
        return a.expand(*shape).clone()

    def _pair(self, val):
        """Scalar, [B] or [B, n] -> [B, n]."""
        a = self._arr(val)
        if a.ndim == 0:
            a = a.reshape(1, 1)
        elif a.ndim == 1:
            a = a.reshape(-1, 1)
        return self._expand(a, (self.B, self.n))

    def _half(self, val):
        """Scalar, [B], [B, n] or [B, n, 2] -> [B, n, 2]."""
        a = self._arr(val)
        if a.ndim == 0:
            a = a.reshape(1, 1, 1)
        elif a.ndim == 1:
            a = a.reshape(-1, 1, 1)
        elif a.ndim == 2:
            a = a.reshape(a.shape[0], a.shape[1], 1)
        return self._expand(a, (self.B, self.n, 2))

    def reset(self):
        self.V = self._zeros((self.B, self.n, 2, self.N + 1))
        self.I = self._zeros((self.B, self.n, 2, self.N))
        z = self._zeros((self.B, self.n, 2))
        self.vp, self.vj, self.iL, self.vk, self.ix = z + 0, z + 0, z + 0, z + 0, z + 0
        self.vb = self._zeros((self.B, self.n))
        self.vclk_prev = 0.0
        self.w_prev = None
        self.t = 0.0

    def enable_noise(self, T=353.0, fano=1.0, scale=1.0, seed=1, thermal=True, shot=True):
        """fano: shot-noise factor; scale: common factor on the power of every noise source.  Both may be
        scalars or arrays [B] (one value per run; scale 0 gives a run without noise)."""
        xp, dt = self.xp, self.dt
        kT = KB * T
        sq = xp.sqrt(self._pair(scale))[..., None]                      # [B, n, 1]
        vn = lambda R: xp.sqrt(2.0 * kT * 1e3 * R / (1e-12 * dt))       # V, white per step (R in kohm)
        self.noise = dict(
            sI=(xp.sqrt(2.0 * kT * 1e9 * dt / (self.Lseg * self.tau_[..., None])) * 1e3 * sq[..., None]) if thermal else None,
            vk=vn(self.Rk) * sq if thermal else None, vd=vn(self.rho) * sq if thermal else None,
            vL=vn(self.RL) * sq if thermal else None, vb=vn(self.Rb) * sq[..., 0] if thermal else None,
            shot=(self._pair(fano)[..., None] * (QE * 1e-3 * 1e-12 * dt) * sq * sq) if shot else None)
        if xp is np:
            self.rng = np.random.default_rng(seed)
        else:
            self.gen = xp.Generator(device=self.dev)
            self.gen.manual_seed(seed)

    def _randn(self, shape):
        if self.xp is np:
            return self.rng.standard_normal(shape).astype(self.dtype)
        return self.xp.randn(shape, device=self.dev, dtype=self.dtype, generator=self.gen)

    # -------------------------------------------------------------------- step
    def step(self, vclk, iB=0.0):
        """Advance by dt.  vclk: clock voltage at the new time ([B, n] or scalar); iB: current into the B
        ends ([B, n, 2] or scalar, mA)."""
        xp, dt, N = self.xp, self.dt, self.N
        V, I = self.V, self.I
        I = ((1.0 - self.alpha) * I - (dt / self.Lseg) * (V[..., 1:] - V[..., :-1])) / (1.0 + self.alpha)
        nz = self.noise
        if nz is not None and nz["sI"] is not None:
            I = I + nz["sI"] * self._randn(tuple(I.shape))
        Vn = V.clone() if xp is not np else V.copy()
        Vn[..., 1:N] = V[..., 1:N] - (dt / self.Cn[..., 1:N]) * (I[..., 1:] - I[..., :-1])
        rB = (I[..., N - 1] + iB).reshape(self.B, 2 * self.n)
        Vn[..., N] = V[..., N] + dt * (self.MBinv @ rB[..., None])[..., 0].reshape(self.B, self.n, 2)
        # diode conduction currents (first-order delay); mid-step value for the lumped solve
        if self.lin is None:
            jd = self.jscale * rtdiv.J(self.vj, self.iv, xp)
        else:
            jd = self.lin[1] + self.lin[2] * (self.vj - self.lin[0])
        ix_new = self.ix + (self.area * jd - self.ix) * (1.0 - xp.exp(-dt / self.tau_d))
        ix_mid = 0.5 * (self.ix + ix_new)
        self.ix = ix_new
        vclk_mid = 0.5 * (vclk + self.vclk_prev)
        self.vclk_prev = vclk
        z = self.vj * 0.0
        s0 = -I[..., 0] / self.C0                       # [B, n, 2]
        s1 = z + 0.0
        s2 = -ix_mid / self.Cd
        s3 = z + 0.0
        s4 = z + 0.0
        sb = vclk_mid / (self.Rb * self.Cb) + self.vb * 0.0
        eL = None
        if nz is not None:
            shp = tuple(self.vj.shape)
            if nz["shot"] is not None:
                dq = xp.sqrt(nz["shot"] * xp.abs(self.ix))
                s2 = s2 - dq / (1e-15 * self.Cd) * self._randn(shp) / dt
            if nz["vk"] is not None:
                e = nz["vk"] * self._randn(shp) / self.Rk
                s0 = s0 + e / self.C0
                s1 = s1 - e / self.Cp
                s4 = s4 + e * self.invCk
                e = nz["vd"] * self._randn(shp) / self.rho
                s1 = s1 + e / self.Cp
                s2 = s2 + e / self.Cd
                sb = sb - (e[..., 0] + e[..., 1]) / self.Cb
                eL = nz["vL"] * self._randn(shp)
                s3 = xp.stack([self.a11 * eL[..., 0] + self.a12 * eL[..., 1], self.a21 * eL[..., 0] + self.a22 * eL[..., 1]], -1) \
                    if xp is not np else np.stack([self.a11 * eL[..., 0] + self.a12 * eL[..., 1], self.a21 * eL[..., 0] + self.a22 * eL[..., 1]], -1)
                sb = sb + nz["vb"] * self._randn(tuple(self.vb.shape)) / (self.Rb * self.Cb)
        if self.Goff is not None:
            # voltage across each winding (pad voltage less the resistive drop) of the other pairs, at mid-step
            w = self.vp - self.RL * self.iL
            wm = (1.5 * w - 0.5 * self.w_prev) if self.w_prev is not None else w
            self.w_prev = w
            if eL is not None:
                wm = wm + eL
            s3 = s3 + (self.Goff @ wm.reshape(self.B, 2 * self.n, 1)).reshape(self.B, self.n, 2)
        st = xp.stack if xp is not np else np.stack
        y = st([V[..., 0, 0], self.vp[..., 0], self.vj[..., 0], self.iL[..., 0], self.vk[..., 0],
                V[..., 1, 0], self.vp[..., 1], self.vj[..., 1], self.iL[..., 1], self.vk[..., 1], self.vb], -1)
        src = st([s0[..., 0], s1[..., 0], s2[..., 0], s3[..., 0], s4[..., 0],
                  s0[..., 1], s1[..., 1], s2[..., 1], s3[..., 1], s4[..., 1], sb], -1)
        y2 = (self.P @ y[..., None])[..., 0] + (self.Q @ (2.0 * src)[..., None])[..., 0]
        Vn[..., 0, 0] = y2[..., 0]
        Vn[..., 1, 0] = y2[..., 5]
        self.vp = st([y2[..., 1], y2[..., 6]], -1)
        self.vj = st([y2[..., 2], y2[..., 7]], -1)
        self.iL = st([y2[..., 3], y2[..., 8]], -1)
        self.vk = st([y2[..., 4], y2[..., 9]], -1)
        self.vb = y2[..., 10]
        self.V, self.I = Vn, I
        self.t += dt

    def supply_current(self, vclk):
        return (vclk - self.vb) / self.Rb

    def odd_B(self):
        """Half the difference of the two B-end voltages: the level of a half in the odd mode."""
        return 0.5 * (self.V[..., 0, -1] - self.V[..., 1, -1])

    def even_B(self):
        return 0.5 * (self.V[..., 0, -1] + self.V[..., 1, -1])


def matrix_pencil(x, dt, order=6):
    """Damped sinusoids in a real trace: list of (f THz, growth 1/ps, amplitude), largest first."""
    x = np.asarray(x, float)
    n = len(x)
    Lp = n // 3
    Y = np.array([x[i:i + Lp + 1] for i in range(n - Lp)])
    U, S, Vh = np.linalg.svd(Y, full_matrices=False)
    m = min(order, int((S > 1e-9 * S[0]).sum()))
    V1, V2 = Vh[:m, :-1], Vh[:m, 1:]
    Z = np.linalg.eigvals(np.linalg.pinv(V1.T) @ V2.T)
    lam = np.log(Z) / dt
    A = np.exp(np.outer(np.arange(n) * dt, lam))
    amp = np.linalg.lstsq(A, x.astype(complex), rcond=None)[0]
    out = [(abs(l.imag) / W0, l.real, 2 * abs(a)) for l, a in zip(lam, amp) if l.imag > 1e-6]
    return sorted(out, key=lambda t: -t[2])
