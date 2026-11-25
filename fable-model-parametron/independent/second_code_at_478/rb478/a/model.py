"""Independent rebuild of the pumped RTD pair (spec D225).
Units: V, mA, ohm, fF, pH, ps.  C dv/dt [fF V/ps] = mA ; i = 1000 v / R ; di/dt = 1000 v / L.
Integrator: SBDF2 (BDF2 on the linear network, 2nd-order extrapolation of the diode term),
first step backward Euler.  Known forcing (supply, launcher) and noise taken at t_{n+1}.
"""
import numpy as np

VT = 0.025852
A_, B_, C_, D_, n1, n2, H_ = 3.541, 0.1002, 0.1480, 0.02606, 0.2882, 0.1843, 0.007984


def I_full(V):
    v = V / 1.667
    a = (B_ - C_ + n1 * v) / VT
    b = (B_ - C_ - n1 * v) / VT
    return 0.9333 * (A_ * (np.logaddexp(0, a) - np.logaddexp(0, b)) * (np.pi / 2 + np.arctan((C_ - n1 * v) / D_))
                     + H_ * np.expm1(n2 * v / VT) + 2.218 * np.tanh(v / 0.05))


FRAC, CD, RHO, TAU, KC, RB, CB, RK, CS = 0.25, 2.5, 12.0, 0.100, 0.3, 2.5, 4.78, 1.0, 0.7
CELLS = {'B': (21.5, 17.84, 6.31), 'D': (13.5, 24.60, 11.59), 'F': (13.5, 26.30, 9.29)}
FD = 0.2252          # carrier, 1/ps
TC = 1.0 / FD        # 4.4405 ps
TP = 69.28           # clock period ps
WRISE = 14.3
KB = 1.380649e-23
QE = 1.602176634e-19
TEMP = 353.0
NS = 11              # states per pair


def idx(m, h=None, name=None):
    if name == 'vS':
        return NS * m
    off = {'vj': 0, 'ix': 1, 'vp': 2, 'vst': 3, 'iL': 4}[name]
    return NS * m + 1 + 5 * h + off


def build(cell, Lodd, Mfac=-0.06, Mmode='geo'):
    """Return A (n x n), Lmat inverse, and index arrays for a row of len(Lodd) pairs."""
    Cp, _, RL = CELLS[cell]
    N = len(Lodd)
    n = NS * N
    A = np.zeros((n, n))
    Gr, Gb, Gk = 1000 / RHO, 1000 / RB, 1000 / RK
    W = 2 * N
    Lm = np.zeros((W, W))
    for m in range(N):
        Lh = Lodd[m] / (1 + KC)
        Lm[2 * m, 2 * m] = Lm[2 * m + 1, 2 * m + 1] = Lh
        Lm[2 * m, 2 * m + 1] = Lm[2 * m + 1, 2 * m] = -KC * Lh
    for m in range(N - 1):
        if Mmode == 'geo':
            M = Mfac * np.sqrt(Lodd[m] * Lodd[m + 1])
        else:
            M = Mfac * Mmode
        for (a, b) in ((m, m + 1), (m + 1, m)):
            ap, am, bp, bm = 2 * a, 2 * a + 1, 2 * b, 2 * b + 1
            Lm[bp, ap] += 0.5 * M; Lm[bp, am] -= 0.5 * M
            Lm[bm, ap] -= 0.5 * M; Lm[bm, am] += 0.5 * M
    Li = np.linalg.inv(Lm)
    for m in range(N):
        iS = idx(m, name='vS')
        A[iS, iS] += -Gb / CB
        for h in (0, 1):
            vj, ix, vp, vst, iL = [idx(m, h, s) for s in ('vj', 'ix', 'vp', 'vst', 'iL')]
            A[iS, iS] -= Gr / CB; A[iS, vj] += Gr / CB; A[iS, vp] += Gr / CB
            A[vj, iS] += Gr / CD; A[vj, vj] -= Gr / CD; A[vj, vp] -= Gr / CD; A[vj, ix] -= 1 / CD
            A[ix, ix] = -1 / TAU
            A[vp, iS] += Gr / Cp; A[vp, vj] -= Gr / Cp; A[vp, vp] -= (Gr + Gk) / Cp
            A[vp, iL] -= 1 / Cp; A[vp, vst] += Gk / Cp
            A[vst, vp] += Gk / CS; A[vst, vst] -= Gk / CS
    for w in range(W):
        iw = idx(w // 2, w % 2, 'iL')
        for w2 in range(W):
            A[iw, idx(w2 // 2, w2 % 2, 'vp')] += 1000 * Li[w, w2]
            A[iw, idx(w2 // 2, w2 % 2, 'iL')] -= RL * Li[w, w2]
    return A, Li


def noise_matrix(cell, Li, N, dt):
    """Thermal sources: map unit normals -> derivative contributions (per step sample)."""
    Cp, _, RL = CELLS[cell]
    dts = dt * 1e-12
    kT = KB * TEMP
    sI = lambda R: 1000 * np.sqrt(2 * kT / (R * dts))      # mA
    sV = lambda R: np.sqrt(2 * kT * R / dts)               # V
    n = NS * N
    cols = []
    for m in range(N):
        c = np.zeros(n); c[idx(m, name='vS')] = sI(RB) / CB; cols.append(c)
        for h in (0, 1):
            c = np.zeros(n)
            c[idx(m, name='vS')] -= sI(RHO) / CB; c[idx(m, h, 'vj')] += sI(RHO) / CD; c[idx(m, h, 'vp')] += sI(RHO) / Cp
            cols.append(c)
            c = np.zeros(n)
            c[idx(m, h, 'vp')] -= sI(RK) / Cp; c[idx(m, h, 'vst')] += sI(RK) / CS
            cols.append(c)
            c = np.zeros(n)
            w = 2 * m + h
            for w2 in range(2 * N):
                c[idx(w2 // 2, w2 % 2, 'iL')] += 1000 * Li[w2, w] * sV(RL)
            cols.append(c)
    return np.array(cols)          # (nsrc, n)


def shot_sigma(ix, dt):
    return 1000 * np.sqrt(QE * np.abs(ix) / 1000 / (dt * 1e-12))   # mA


def win(t):
    """periodic window, period TP, raised-cosine rise centred at 0, fall centred at 0.75 TP"""
    tau = np.mod(t + 0.5 * TP, TP) - 0.5 * TP     # in [-T/2, T/2)
    h = WRISE / 2
    tf = 0.75 * TP
    tau2 = np.mod(t, TP)
    w = np.zeros_like(tau2)
    w = np.where((tau2 >= h) & (tau2 <= tf - h), 1.0, w)
    rise = (tau >= -h) & (tau < h)
    w = np.where(rise, 0.5 * (1 - np.cos(np.pi * (tau + h) / WRISE)), w)
    fall = (tau2 > tf - h) & (tau2 < tf + h)
    w = np.where(fall, 0.5 * (1 + np.cos(np.pi * (tau2 - tf + h) / WRISE)), w)
    return w


def dc_point(cell, Vs):
    Cp, _, RL = CELLS[cell]
    Rt = RHO + RL + 2 * RB
    Vs = np.atleast_1d(np.asarray(Vs, float))
    lo = np.zeros_like(Vs); hi = Vs.copy()
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        f = mid + FRAC * I_full(mid) * Rt / 1000 - Vs
        lo = np.where(f < 0, mid, lo); hi = np.where(f >= 0, mid, hi)
    vj = 0.5 * (lo + hi)
    ix = FRAC * I_full(vj)
    x = np.zeros((len(Vs), NS))
    x[:, 0] = Vs - RB * 2 * ix / 1000
    for h in (0, 1):
        b = 1 + 5 * h
        x[:, b] = vj; x[:, b + 1] = ix; x[:, b + 2] = RL * ix / 1000; x[:, b + 3] = RL * ix / 1000; x[:, b + 4] = ix
    return x, vj, ix


def vj_idx(N):
    return np.array([idx(m, h, 'vj') for m in range(N) for h in (0, 1)])


def ix_idx(N):
    return np.array([idx(m, h, 'ix') for m in range(N) for h in (0, 1)])


def vst_idx(N):
    p = np.array([idx(m, 0, 'vst') for m in range(N)]); q = np.array([idx(m, 1, 'vst') for m in range(N)])
    return p, q
