"""Time-domain model of pumped RTD pairs, written from BLIND_SPEC_T1.md only.

Internal units: V, mA, kohm, fF, nH, ps  (consistent: C dv/dt in mA, L di/dt in V, R i in V).
State per pair (11): 0 vS, 1 vj+, 2 vj-, 3 ix+, 4 ix-, 5 vP+, 6 vP-, 7 vT+, 8 vT-, 9 iL+, 10 iL-
(vT = stub node).  Integrator: linearised BDF2 (one Newton step from the BDF2 predictor),
implicit per pair, inter-pair inductive coupling explicit at the predictor.
"""
import numpy as np

kB = 1.380649e-23
qe = 1.602176634e-19
TK = 353.0

frac = 0.25
Cd = 0.5233
rho = 12.0e-3
tau = 0.02093
Cp = 2.8256
Lodd0 = 5.5047e-3
kk = 0.3
RL = 9.29e-3
Rb = 2.5e-3
Cb = 1.000
Rk = 1.0e-3
Cs = 0.1465

fd = 1.076
Tc = 1.0 / fd
om = 2 * np.pi * fd
T = 14.50
qph = 0.25
Is = 0.4
RISE = 3.0

A_ = 3.541; B_ = 0.1002; C_ = 0.1480; D_ = 0.02606; n1 = 0.2882; n2 = 0.1843; H_ = 0.007984
VT = 0.025852


def Ifull(V):
    v = V / 1.667
    a = (B_ - C_ + n1 * v) / VT
    b = (B_ - C_ - n1 * v) / VT
    u = (C_ - n1 * v) / D_
    t1 = A_ * (np.logaddexp(0, a) - np.logaddexp(0, b)) * (np.pi / 2 + np.arctan(u))
    t2 = H_ * (np.exp(n2 * v / VT) - 1)
    t3 = 2.218 * np.tanh(v / 0.05)
    return 0.9333 * (t1 + t2 + t3)


def dIfull(V):
    v = V / 1.667
    a = (B_ - C_ + n1 * v) / VT
    b = (B_ - C_ - n1 * v) / VT
    u = (C_ - n1 * v) / D_
    sa = 0.5 * (1 + np.tanh(a / 2)); sb = 0.5 * (1 + np.tanh(b / 2))
    spd = np.logaddexp(0, a) - np.logaddexp(0, b)
    d1 = A_ * ((sa + sb) * n1 / VT * (np.pi / 2 + np.arctan(u)) + spd * (-n1 / D_) / (1 + u * u))
    d2 = H_ * n2 / VT * np.exp(n2 * v / VT)
    d3 = 2.218 / 0.05 / np.cosh(v / 0.05) ** 2
    return 0.9333 * (d1 + d2 + d3) / 1.667


def win(tau_):
    """Clock window, periodic T, argument already shifted by d T/4."""
    x = np.mod(tau_, T)
    w = np.zeros_like(x)
    h = RISE / 2
    on = (x >= h) & (x <= 0.75 * T - h)
    w[on] = 1.0
    r1 = x < h
    w[r1] = 0.5 * (1 - np.cos(np.pi * (x[r1] + h) / RISE))
    r2 = x > T - h
    w[r2] = 0.5 * (1 - np.cos(np.pi * (x[r2] - T + h) / RISE))
    f = (x > 0.75 * T - h) & (x < 0.75 * T + h)
    w[f] = 0.5 * (1 + np.cos(np.pi * (x[f] - 0.75 * T + h) / RISE))
    return w


class Layout:
    def __init__(self, names, depth, links, drives):
        self.names = list(names)
        self.N = len(names)
        self.idx = {n: i for i, n in enumerate(names)}
        self.depth = np.array(depth, dtype=float)
        self.links = links      # list of (src, dst, sign) ; sign +1 normal (M=-0.06 L), -1 reversed
        self.drives = drives    # dict pair index -> bit array (0/1) per slot


def build_L(lay, g):
    """g: (B,N) normal draws. Returns Gamma = L^-1, (B,2N,2N), in 1/nH."""
    Bn = g.shape[0]; N = lay.N
    Lodd = Lodd0 * (1 + 0.03 * g)
    Lh = Lodd / (1 + kk)
    L = np.zeros((Bn, 2 * N, 2 * N))
    for n in range(N):
        L[:, 2 * n, 2 * n] = Lh[:, n]
        L[:, 2 * n + 1, 2 * n + 1] = Lh[:, n]
        L[:, 2 * n, 2 * n + 1] = -kk * Lh[:, n]
        L[:, 2 * n + 1, 2 * n] = -kk * Lh[:, n]
    for (a, b, s) in lay.links:
        M = -0.06 * s * np.sqrt(Lodd[:, a] * Lodd[:, b])
        for (i, j, sg) in ((0, 0, 1), (0, 1, -1), (1, 0, -1), (1, 1, 1)):
            L[:, 2 * b + i, 2 * a + j] += 0.5 * M * sg
            L[:, 2 * a + j, 2 * b + i] += 0.5 * M * sg
    return np.linalg.inv(L)


def local_A(G2):
    """G2: (...,2,2) local block of Gamma.  Returns A (...,11,11)."""
    sh = G2.shape[:-2]
    A = np.zeros(sh + (11, 11))
    gr = 1 / rho
    A[..., 0, 0] = (-1 / Rb - 2 * gr) / Cb
    for hh in (0, 1):
        vj = 1 + hh; ix = 3 + hh; vP = 5 + hh; vT = 7 + hh; iL = 9 + hh
        A[..., 0, vP] = gr / Cb; A[..., 0, vj] = gr / Cb
        A[..., vj, 0] = gr / Cd; A[..., vj, vP] = -gr / Cd; A[..., vj, vj] = -gr / Cd; A[..., vj, ix] = -1 / Cd
        A[..., ix, ix] = -1 / tau
        A[..., vP, 0] = gr / Cp; A[..., vP, vP] = (-gr - 1 / Rk) / Cp; A[..., vP, vj] = -gr / Cp
        A[..., vP, iL] = -1 / Cp; A[..., vP, vT] = 1 / (Rk * Cp)
        A[..., vT, vP] = 1 / (Rk * Cs); A[..., vT, vT] = -1 / (Rk * Cs)
        for h2 in (0, 1):
            A[..., iL, 5 + h2] = G2[..., hh, h2]
            A[..., iL, 9 + h2] = -RL * G2[..., hh, h2]
    return A


def dc_state(Vs):
    """DC operating point of a lone pair on constant supply Vs (array). Returns (...,11)."""
    Vs = np.asarray(Vs, float)
    Rt = 2 * Rb + rho + RL
    lo = np.zeros_like(Vs); hi = Vs.copy()
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        f = mid + Rt * frac * Ifull(mid) - Vs
        hi = np.where(f > 0, mid, hi); lo = np.where(f > 0, lo, mid)
    vj = 0.5 * (lo + hi)
    I = frac * Ifull(vj)
    x = np.zeros(Vs.shape + (11,))
    x[..., 0] = Vs - 2 * Rb * I
    x[..., 1] = vj; x[..., 2] = vj
    x[..., 3] = I; x[..., 4] = I
    x[..., 5] = RL * I; x[..., 6] = RL * I
    x[..., 7] = RL * I; x[..., 8] = RL * I
    x[..., 9] = I; x[..., 10] = I
    return x


def simulate(lay, Vs, p, g, nf, seed, h, t0, t1, dec, nowin=False, x0=None, start_zero_before_first=True):
    """Vs, p, nf: (B,) arrays; g: (B,N).  Returns rec times (nr,), vodd (nr,B,N) float32."""
    Vs = np.asarray(Vs, float); p = np.asarray(p, float); nf = np.asarray(nf, float)
    Bn = Vs.shape[0]; N = lay.N
    Gam = build_L(lay, g)
    G2 = np.zeros((Bn, N, 2, 2))
    Goff = Gam.copy()
    for n in range(N):
        G2[:, n] = Gam[:, 2 * n:2 * n + 2, 2 * n:2 * n + 2]
        Goff[:, 2 * n:2 * n + 2, 2 * n:2 * n + 2] = 0
    has_cross = np.abs(Goff).max() > 0
    gam = 2.0 / 3.0
    A = local_A(G2)
    M0 = np.eye(11) - gam * h * A
    Pm = np.linalg.inv(M0)                      # (B,N,11,11)
    PU = Pm[..., :, 3:5]                        # columns ix+, ix-
    Q = Pm[..., 1:3, 3:5]                       # rows vj, cols ix  (B,N,2,2)
    depth = lay.depth[None, :]
    php = np.pi * (qph + 1.5 * depth)
    # drives
    drv_sign = np.zeros((N,)); drv_bits = {}
    for n, bits in lay.drives.items():
        drv_bits[n] = np.asarray(bits)
    rng = np.random.default_rng(seed)
    noisy = np.any(nf > 0)
    hs = h * 1e-12
    sRb = np.sqrt(2 * kB * TK / (Rb * 1e3 * hs)) * 1e3
    srho = np.sqrt(2 * kB * TK / (rho * 1e3 * hs)) * 1e3
    sRk = np.sqrt(2 * kB * TK / (Rk * 1e3 * hs)) * 1e3
    sRL = np.sqrt(2 * kB * TK * RL * 1e3 / hs)
    ssh = np.sqrt(qe * 1e-3 / hs) * 1e3          # times sqrt(|ix| in mA)
    sqf = np.sqrt(nf)[:, None]
    if x0 is None:
        x = np.zeros((Bn, N, 11))
    else:
        x = np.array(x0, float).copy()
    xprev = x.copy()
    nsteps = int(round((t1 - t0) / h))
    nrec = nsteps // dec + 1
    rec = np.zeros((nrec, Bn, N), np.float32)
    trec = t0 + h * dec * np.arange(nrec)
    rec[0] = 0.5 * (x[..., 7] - x[..., 8])
    ir = 1
    gh = gam * h
    for it in range(1, nsteps + 1):
        t = t0 + it * h
        xp = 2 * x - xprev
        hist = (4.0 / 3.0) * x - (1.0 / 3.0) * xprev
        vjp = xp[..., 1:3]
        gd = frac * dIfull(vjp) / tau            # (B,N,2)
        s = np.zeros((Bn, N, 11))
        s[..., 3:5] = frac * Ifull(vjp) / tau - gd * vjp
        # clock / pump
        if nowin:
            w = np.ones((1, N))
        else:
            tt = t - depth * T / 4
            w = win(tt)
            if start_zero_before_first:
                w = np.where(tt < -RISE / 2, 0.0, w)
        vclk = Vs[:, None] * w * (1 + p[:, None] * np.cos(2 * om * t + php))
        s[..., 0] += vclk / (Rb * Cb)
        # drives into stub nodes
        if drv_bits:
            c = Is * np.cos(om * t)
            for n, bits in drv_bits.items():
                sl = int(np.floor((t - lay.depth[n] * T / 4 + T / 4) / T))
                if 0 <= sl < len(bits):
                    val = c * (1.0 if bits[sl] else -1.0)
                    s[:, n, 7] += val / Cs
                    s[:, n, 8] -= val / Cs
        # noise
        e = None
        if noisy:
            z = rng.standard_normal((Bn, N, 9))
            nRb = sRb * sqf * z[..., 0]
            nrho = srho * sqf[..., None] * z[..., 1:3]
            nsh = ssh * sqf[..., None] * np.sqrt(np.abs(xp[..., 3:5])) * z[..., 3:5]
            nRk = sRk * sqf[..., None] * z[..., 5:7]
            e = sRL * sqf[..., None] * z[..., 7:9]
            s[..., 0] += (nRb - nrho.sum(-1)) / Cb
            s[..., 1:3] += (nrho - nsh) / Cd
            s[..., 5:7] += (nrho - nRk) / Cp
            s[..., 7:9] += nRk / Cs
            s[..., 9:11] += -np.einsum('bnij,bnj->bni', G2, e)
        if has_cross:
            u = xp[..., 5:7] - RL * xp[..., 9:11]
            if e is not None:
                u = u - e
            cr = np.einsum('bij,bj->bi', Goff, u.reshape(Bn, 2 * N)).reshape(Bn, N, 2)
            s[..., 9:11] += cr
        rhs = hist + gh * s
        y = np.einsum('bnij,bnj->bni', Pm, rhs)
        # Woodbury for entries (ix_h, vj_h) of matrix: M = M0 + delta_h e_ix e_vj^T, delta=-gh*gd
        dlt = -gh * gd                            # (B,N,2)
        # K = I + D Q  (2x2), solve K w = D (V^T y)
        DQ = dlt[..., :, None] * Q
        K00 = 1 + DQ[..., 0, 0]; K01 = DQ[..., 0, 1]; K10 = DQ[..., 1, 0]; K11 = 1 + DQ[..., 1, 1]
        r0 = dlt[..., 0] * y[..., 1]; r1 = dlt[..., 1] * y[..., 2]
        det = K00 * K11 - K01 * K10
        w0 = (K11 * r0 - K01 * r1) / det
        w1 = (-K10 * r0 + K00 * r1) / det
        xn = y - PU[..., 0] * w0[..., None] - PU[..., 1] * w1[..., None]
        xprev = x; x = xn
        if it % dec == 0:
            rec[ir] = 0.5 * (x[..., 7] - x[..., 8]); ir += 1
    return trec[:ir], rec[:ir], x


def lockin(trec, rec, tstart, length):
    """Complex phasor Z of v = Re(Z e^{i om t}) over [tstart, tstart+length). rec (nr,B,N) -> Z (B,N)."""
    dt = trec[1] - trec[0]
    i0 = int(round((tstart - trec[0]) / dt))
    n = int(round(length / dt))
    tt = trec[i0:i0 + n]
    ph = np.exp(-1j * om * tt)
    return (2.0 / n) * np.einsum('t,tbn->bn', ph, rec[i0:i0 + n].astype(float))


RD_OFF = T / 4 + 0.5     # read window start after slot start
RD_LEN = 2 * Tc          # read window length


def read_slots(lay, trec, rec, nslots):
    Bn = rec.shape[1]
    Z = np.zeros((Bn, lay.N, nslots), complex)
    for n in range(lay.N):
        d = lay.depth[n]
        for s in range(nslots):
            ws = s * T + d * T / 4 + RD_OFF
            Z[:, n, s] = lockin(trec, rec[:, :, n:n + 1], ws, RD_LEN)[:, 0]
    return Z


def maj(*a):
    return (sum(int(x) for x in a) >= 2)


def layout_c():
    a = [int(c) for c in "0 1 1 1 0 1 1 0 0 1 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0".split()]
    b = [int(c) for c in "0 1 1 0 1 0 0 1 1 0 1 0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0 1 0 1 0 0".split()]
    names = ['At', 'Bt', 'Ac', 'Bc', 'Ct', 'Cc', 'Mt', 'Mc', 'Gt', 'Gc', 'Kt', 'Kc', 'St', 'Sc',
             'X2t', 'X2c', 'X3t', 'X3c', 'Ft', 'Fc']
    dep = dict(At=0, Bt=0, Ac=0, Bc=0, Ct=0, Cc=0, Mt=1, Mc=1, Gt=1, Gc=1, Kt=1, Kc=1, St=2, Sc=2,
               X2t=2, X2c=2, X3t=3, X3c=3, Ft=3, Fc=3)
    src = dict(Mt=['At', 'Bt', 'Ct'], Mc=['Ac', 'Bc', 'Cc'], Gt=['At', 'Bt', 'Cc'], Gc=['Ac', 'Bc', 'Ct'],
               Kt=['Ct'], Kc=['Cc'], St=['Mc', 'Gt', 'Kt'], Sc=['Mt', 'Gc', 'Kc'], X2t=['Mt'], X2c=['Mc'],
               X3t=['X2t'], X3c=['X2c'], Ft=['St'], Fc=['Sc'], Ct=['X3c'], Cc=['X3t'])
    idx = {n: i for i, n in enumerate(names)}
    links = []
    for dst, ss in src.items():
        for sname in ss:
            links.append((idx[sname], idx[dst], 1))
    na = [1 - x for x in a]; nb = [1 - x for x in b]
    drives = {idx['At']: a, idx['Bt']: b, idx['Ac']: na, idx['Bc']: nb}
    lay = Layout(names, [dep[n] for n in names], links, drives)
    lay.src = src; lay.ops = (a, b)
    return lay


def expected_c(lay, nslots=32):
    """Meant labels per pair/slot, evaluated from the netlist; crossing from depth 3 into depth 0
    of the next slot flips the label (4 x 135 deg = 540 deg)."""
    a, b = lay.ops
    E = {}
    order = ['Mt', 'Mc', 'Gt', 'Gc', 'Kt', 'Kc', 'St', 'Sc', 'X2t', 'X2c', 'X3t', 'X3c', 'Ft', 'Fc']
    for nme in lay.names:
        E[nme] = [0] * nslots
    for s in range(nslots):
        E['At'][s] = a[s]; E['Bt'][s] = b[s]; E['Ac'][s] = 1 - a[s]; E['Bc'][s] = 1 - b[s]
        if s == 0:
            E['Ct'][s] = 0; E['Cc'][s] = 1
        else:
            E['Ct'][s] = 1 - E['X3c'][s - 1]; E['Cc'][s] = 1 - E['X3t'][s - 1]
        for nme in order:
            E[nme][s] = int(maj(*[E[x][s] for x in lay.src[nme]])) if len(lay.src[nme]) == 3 else E[lay.src[nme][0]][s]
    return np.array([E[n] for n in lay.names])


def true_sum_bits(lay, nslots=32):
    a, b = lay.ops
    A = sum(a[i] << i for i in range(nslots)); Bv = sum(b[i] << i for i in range(nslots))
    S = (A + Bv) % (1 << nslots)
    return np.array([(S >> i) & 1 for i in range(nslots)])


def layout_a():
    pat = [1, 0, 1, 1, 0, 0, 1, 0] * 4
    names = ['P%d' % i for i in range(16)]
    links = [(i, i + 1, 1) for i in range(15)]
    lay = Layout(names, list(range(16)), links, {0: pat})
    lay.pat = pat
    return lay


def expected_a(lay, nslots=32):
    # pair n copies pair n-1; depth 4 equals depth 0 one slot later: label flips each time depth passes a
    # multiple of 4 (4 x 135 deg = 180 deg).  Axis orientation for depth d: theta0 + d*135 deg (no wrap mod 4).
    return np.array([lay.pat[:nslots] for _ in range(16)])


def layout_single():
    return Layout(['P'], [0], [], {})


def axis_and_signs(lay, Z, ref_one_mask, step_deg=135.0):
    """Z (B,N,S).  Axis of depth 0 per run from doubled-angle mean over all pairs (de-rotated by depth),
    oriented so that depth-0 pairs meant to be 1 (ref_one_mask (N,S) True where meant 1, depth-0 driven only)
    sit on the + end in majority.  Returns theta0 (B,), signs (B,N,S) in {+1,-1}."""
    d = lay.depth[None, :, None]
    rot = np.exp(-1j * np.deg2rad(step_deg) * d)
    Zr = Z * rot
    m = (Zr[..., 1:] ** 2 / (np.abs(Zr[..., 1:]) + 1e-30)).sum(axis=(1, 2))
    th = 0.5 * np.angle(m)
    proj = np.real(Zr * np.exp(-1j * th)[:, None, None])
    sel = ref_one_mask
    score = (np.sign(proj) * sel[None] * 1.0).sum(axis=(1, 2))
    th = np.where(score < 0, th + np.pi, th)
    proj = np.real(Zr * np.exp(-1j * th)[:, None, None])
    return th, np.sign(proj)


def signs_with_theta(lay, Z, th, step_deg=135.0):
    d = lay.depth[None, :, None]
    Zr = Z * np.exp(-1j * np.deg2rad(step_deg) * d)
    return np.sign(np.real(Zr * np.exp(-1j * th)[:, None, None]))
