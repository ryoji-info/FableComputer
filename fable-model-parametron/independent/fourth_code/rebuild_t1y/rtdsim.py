# Core simulator for the pumped RTD pair fabric (own rebuild from BLIND_SPEC_T1).
# Internal units: V, mA, ps, fF, kohm, nH  (V = nH * mA/ps ; mA = V/kohm ; V/ps = mA/fF)
import numpy as np

# ---------------- diode law ----------------
_A, _B, _C, _D = 3.541, 0.1002, 0.1480, 0.02606
_n1, _n2, _H, _VT = 0.2882, 0.1843, 0.007984, 0.025852

def Ifull(V):
    v = V / 1.667
    a = (_B - _C + _n1 * v) / _VT
    b = (_B - _C - _n1 * v) / _VT
    t1 = _A * (np.logaddexp(0.0, a) - np.logaddexp(0.0, b)) * (np.pi / 2 + np.arctan((_C - _n1 * v) / _D))
    t2 = _H * (np.exp(np.minimum(_n2 * v / _VT, 60.0)) - 1.0)
    t3 = 2.218 * np.tanh(v / 0.05)
    return 0.9333 * (t1 + t2 + t3)

# ---------------- cell values ----------------
FRAC = 0.25
CD = 0.5233      # fF
RHO = 0.012      # kohm
TAU = 0.02093    # ps
CP = 2.8256      # fF
LODD = 0.0055047 # nH
KC = 0.3
RL = 0.00929     # kohm
RB = 0.0025      # kohm
CB = 1.000       # fF
RK = 0.001       # kohm
CS = 0.1465      # fF

FD = 1.076       # THz
TC = 1.0 / FD    # carrier period ps
TP = 14.50       # clock period ps
QPH = 0.25
IS = 0.4         # mA drive
MLINK = 0.06

# noise constants
KB = 1.380649e-23
QE = 1.602176634e-19
TEMP = 353.0

NV = 11  # unknowns per pair

def ix_S(p): return NV * p
def ix_vj(p, h): return NV * p + 1 + 5 * h
def ix_ix(p, h): return NV * p + 2 + 5 * h
def ix_vP(p, h): return NV * p + 3 + 5 * h
def ix_iL(p, h): return NV * p + 4 + 5 * h
def ix_vst(p, h): return NV * p + 5 + 5 * h


def win(tau):
    """periodic clock window, period TP; rise centred at 0, fall centred at 0.75 TP, 3.0 ps raised cosine"""
    u = np.mod(tau + 1.5, TP) - 1.5   # in [-1.5, TP-1.5)
    w = np.zeros_like(u)
    rise = (u >= -1.5) & (u < 1.5)
    w[rise] = 0.5 * (1 - np.cos(np.pi * (u[rise] + 1.5) / 3.0))
    on = (u >= 1.5) & (u < 0.75 * TP - 1.5)
    w[on] = 1.0
    fall = (u >= 0.75 * TP - 1.5) & (u < 0.75 * TP + 1.5)
    w[fall] = 0.5 * (1 + np.cos(np.pi * (u[fall] - (0.75 * TP - 1.5)) / 3.0))
    return w


class Layout:
    def __init__(self, names, depth, drive, links):
        # names: list of str; depth: list int; drive: dict idx -> bit array (len 32) ; links: list (src, dst, sign) sign +1 normal, -1 reversed
        self.names = list(names)
        self.depth = np.array(depth, int)
        self.drive = dict(drive)
        self.links = list(links)
        self.N = len(names)


def build_matrices(lay, lodd):
    """lodd: array (N,) of L_odd per pair (nH). returns A (n x n) dense."""
    N = lay.N
    n = NV * N
    A = np.zeros((n, n))
    nw = 2 * N
    Lm = np.zeros((nw, nw))
    for p in range(N):
        Lh = lodd[p] / (1 + KC)
        Lm[2 * p, 2 * p] = Lh
        Lm[2 * p + 1, 2 * p + 1] = Lh
        Lm[2 * p, 2 * p + 1] = -KC * Lh
        Lm[2 * p + 1, 2 * p] = -KC * Lh
    for (a, b, sg) in lay.links:
        M = sg * (-MLINK) * np.sqrt(lodd[a] * lodd[b])
        for (x, y) in ((a, b), (b, a)):
            Lm[2 * y, 2 * x] += 0.5 * M
            Lm[2 * y, 2 * x + 1] -= 0.5 * M
            Lm[2 * y + 1, 2 * x] -= 0.5 * M
            Lm[2 * y + 1, 2 * x + 1] += 0.5 * M
    Li = np.linalg.inv(Lm)
    for p in range(N):
        s = ix_S(p)
        A[s, s] += -1.0 / (RB * CB)
        for h in (0, 1):
            vj, ixx, vP, iL, vst = ix_vj(p, h), ix_ix(p, h), ix_vP(p, h), ix_iL(p, h), ix_vst(p, h)
            # irho = (vS - vj - vP)/rho
            for (col, sgn) in ((s, 1.0), (vj, -1.0), (vP, -1.0)):
                A[s, col] += -sgn / (RHO * CB)
                A[vj, col] += sgn / (RHO * CD)
                A[vP, col] += sgn / (RHO * CP)
            A[vj, ixx] += -1.0 / CD
            A[ixx, ixx] += -1.0 / TAU
            A[vP, iL] += -1.0 / CP
            A[vP, vP] += -1.0 / (RK * CP)
            A[vP, vst] += 1.0 / (RK * CP)
            A[vst, vP] += 1.0 / (RK * CS)
            A[vst, vst] += -1.0 / (RK * CS)
    # inductor rows
    iLidx = np.array([ix_iL(p, h) for p in range(N) for h in (0, 1)])
    vPidx = np.array([ix_vP(p, h) for p in range(N) for h in (0, 1)])
    for r in range(nw):
        A[iLidx[r], vPidx] += Li[r]
        A[iLidx[r], iLidx] += -RL * Li[r]
    return A, Li, iLidx


class Sim:
    """BDF2 integrator with fixed-point iteration on the diode nonlinearity, batched over B members."""

    def __init__(self, lay, dt, lodd_batch, constant_supply=False, start_gate=True):
        self.lay = lay
        self.dt = dt
        self.B = lodd_batch.shape[0]
        N = lay.N
        self.N = N
        self.n = NV * N
        c = 2.0 / 3.0 * dt
        self.c = c
        Ps, Lis = [], []
        for b in range(self.B):
            A, Li, iLidx = build_matrices(lay, lodd_batch[b])
            P = np.linalg.inv(np.eye(self.n) - c * A)
            Ps.append(P)
            Lis.append(Li)
        self.P = np.array(Ps)             # (B,n,n)
        self.Li = np.array(Lis)           # (B,2N,2N)
        self.iLidx = iLidx
        self.vjidx = np.array([ix_vj(p, h) for p in range(N) for h in (0, 1)])
        self.ixidx = np.array([ix_ix(p, h) for p in range(N) for h in (0, 1)])
        self.Sidx = np.array([ix_S(p) for p in range(N)])
        self.vstidx = np.array([[ix_vst(p, 0), ix_vst(p, 1)] for p in range(N)])
        self.vPidx = np.array([ix_vP(p, h) for p in range(N) for h in (0, 1)])
        self.Pix = self.P[:, :, self.ixidx]                       # (B,n,2N)
        self.Pvj_ix = self.P[:, self.vjidx][:, :, self.ixidx]     # (B,2N,2N)
        self.constant_supply = constant_supply
        self.start_gate = start_gate
        depth = lay.depth
        self.depth = depth
        self.pumpph = np.pi * (QPH + 1.5 * depth)
        self.drv_idx = np.array(sorted(lay.drive.keys()), int)
        if len(self.drv_idx):
            self.drv_bits = np.array([lay.drive[k] for k in self.drv_idx])  # (nd,32)
        else:
            self.drv_bits = np.zeros((0, 32))

    def supply(self, t, Vs, p):
        if self.constant_supply:
            w = np.ones(self.N)
        else:
            w = win(t - self.depth * TP / 4)
            if self.start_gate:
                w = np.where(t < self.depth * TP / 4 - 1.5, 0.0, w)
        return Vs * w * (1 + p * np.cos(4 * np.pi * FD * t + self.pumpph))

    def drive(self, t):
        # returns current into + stub per driven pair (minus gets negative)
        s = int(np.floor((t + TP / 4) / TP))
        if s < 0 or s >= 32 or len(self.drv_idx) == 0:
            return None
        sg = np.where(self.drv_bits[:, s] > 0, 1.0, -1.0)
        return IS * sg * np.cos(2 * np.pi * FD * t)

    def run(self, t0, t1, Vs, p, x0=None, noise_f=0.0, seeds=None, niter=3, rec_every=1, rec_even=False):
        B, n, N, dt, c = self.B, self.n, self.N, self.dt, self.c
        nsteps = int(round((t1 - t0) / dt))
        x = np.zeros((B, n)) if x0 is None else np.array(x0, float).copy()
        xm = x.copy()
        nrec = nsteps // rec_every + 1
        rec = np.zeros((B, nrec, N), np.float32)
        rece = np.zeros((B, nrec, N), np.float32) if rec_even else None
        trec = np.zeros(nrec)
        def odd(xx):
            return 0.5 * (xx[:, self.vstidx[:, 0]] - xx[:, self.vstidx[:, 1]])
        rec[:, 0] = odd(x); trec[0] = t0
        if rec_even:
            rece[:, 0] = 0.5 * (x[:, self.vstidx[:, 0]] + x[:, self.vstidx[:, 1]])
        rngs = None
        if noise_f > 0:
            rngs = [np.random.default_rng(s) for s in seeds]
            kT = KB * TEMP
            dts = dt * 1e-12
            # voltage-noise std (V) of series sources, per step, piecewise constant
            sig_rho = np.sqrt(noise_f * 2 * kT * (RHO * 1e3) / dts)
            sig_RL = np.sqrt(noise_f * 2 * kT * (RL * 1e3) / dts)
            sig_Rk = np.sqrt(noise_f * 2 * kT * (RK * 1e3) / dts)
            sig_Rb = np.sqrt(noise_f * 2 * kT * (RB * 1e3) / dts)
            # shot: current std (mA) = sqrt(f q |ix| / dt) ; |ix| in A
            shot_k = noise_f * QE * 1e-3 / dts * 1e6   # times |ix|[mA] gives mA^2
            vjI = self.vjidx; ixI = self.ixidx; vPI = self.vPidx; SI = self.Sidx
            vstI = self.vstidx.reshape(-1)  # order p0h0 p0h1 ...
        k = 0
        drv_rows_p = np.array([ix_vst(p, 0) for p in self.drv_idx], int)
        drv_rows_m = np.array([ix_vst(p, 1) for p in self.drv_idx], int)
        for step in range(1, nsteps + 1):
            t = t0 + step * dt
            u = np.zeros(n)
            u[self.Sidx] = self.supply(t, Vs, p) / (RB * CB)
            dv = self.drive(t)
            if dv is not None:
                u[drv_rows_p] += dv / CS
                u[drv_rows_m] += -dv / CS
            r = (4.0 / 3.0) * x - (1.0 / 3.0) * xm + c * u[None, :]
            if rngs is not None:
                w = np.zeros((B, n))
                for b in range(B):
                    g = rngs[b].standard_normal(9 * N)
                    eb = sig_Rb * g[:N]
                    er = sig_rho * g[N:3 * N]      # per half, order p0h0,p0h1,...
                    eL = sig_RL * g[3 * N:5 * N]
                    ek = sig_Rk * g[5 * N:7 * N]
                    ish = np.sqrt(shot_k * np.abs(x[b, ixI])) * g[7 * N:9 * N]
                    wb = w[b]
                    wb[SI] += eb / (RB * CB)
                    # rho source: irho = (vS - vj - vP - er)/rho
                    np.add.at(wb, np.repeat(SI, 2), er / (RHO * CB))
                    wb[vjI] += -er / (RHO * CD) - ish / CD
                    wb[vPI] += -er / (RHO * CP) - ek / (RK * CP)
                    wb[vstI] += ek / (RK * CS)
                    wb[self.iLidx] += -(self.Li[b] @ eL)
                r = r + c * w
            base = np.einsum('bij,bj->bi', self.P, r)
            # predictor for vj
            vj = 2 * x[:, self.vjidx] - xm[:, self.vjidx]
            basevj = base[:, self.vjidx]
            for it in range(niter):
                nl = c * FRAC * Ifull(vj) / TAU
                vj = basevj + np.einsum('bij,bj->bi', self.Pvj_ix, nl)
            nl = c * FRAC * Ifull(vj) / TAU
            xn = base + np.einsum('bij,bj->bi', self.Pix, nl)
            xm = x
            x = xn
            if step % rec_every == 0:
                k += 1
                rec[:, k] = odd(x); trec[k] = t
                if rec_even:
                    rece[:, k] = 0.5 * (x[:, self.vstidx[:, 0]] + x[:, self.vstidx[:, 1]])
        out = dict(t=trec[:k + 1], odd=rec[:, :k + 1], x=x, xm=xm)
        if rec_even:
            out['even'] = rece[:, :k + 1]
        return out


# ---------------- reading ----------------
RD_START = TP / 4 + 0.25   # ps into the slot
RD_LEN = 2 * TC            # two carrier periods

def read_slots(t, odd, depth, nslots=32):
    """odd: (nt, N). returns complex amplitude X (N, nslots) in V, so that v ~ Re(X e^{i w t})"""
    N = odd.shape[1]
    dt = t[1] - t[0]
    X = np.full((N, nslots), np.nan + 0j)
    ph = np.exp(-1j * 2 * np.pi * FD * t)
    for p in range(N):
        for s in range(nslots):
            ts = s * TP + depth[p] * TP / 4 + RD_START
            i0 = int(np.ceil((ts - t[0]) / dt - 1e-9))
            m = int(round(RD_LEN / dt))
            if i0 + m > len(t):
                continue
            seg = odd[i0:i0 + m, p] * ph[i0:i0 + m]
            X[p, s] = 2.0 * seg.mean()
    return X
