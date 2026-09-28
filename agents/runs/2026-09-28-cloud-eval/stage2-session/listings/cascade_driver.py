# -*- coding: utf-8 -*-
"""Fable Session 2026-09-28 (cloud evaluation) — two-cell cascade instrument.

Imports the released integrator verbatim (solver._setup / _step_LF) and schedules
only each cell's source clamp. Cell 1 is driven by the 07-31 §2 duty-gated launch
(exp_duty.make_sig_duty logic verbatim, active-envelope carrier reference). Cell 2's
source clamp is driven by cell 1's DRAIN-PLANE series (density, the 08-02 plane; or
velocity, the sensitivity plane), attenuated by the junction class kappa = 10^(J/20):

    h_left2(t_k) = 1 + kappa * x1(t_k),   x1 = h1[-1]-1  (plane 'h')  or  u1[-1]-u0 (plane 'u')

Coupling is causal and unidirectional (ideal isolation): at step k cell 2's clamp
reads cell 1's state at t_k (the state before step k). When both cells share the
released dt (same bias) the coupling is exact lockstep; when they do not (mixed
active/passive chains, whose released dt differ through cmax = 1+|u0|+0.2), cell 1's
recorded series is linearly interpolated onto cell 2's time grid ("recorded-series
coupling"), which for unidirectional coupling is equivalent up to interpolation error.
Every cell keeps its own released dt, so single-cell references reproduce the
promoted rows exactly.

Observables per cell, per step: cav = max|u-u0| (the promoted 'cav'), drn_h = h[-1]-1
(drain-plane density, signed), drn_u = u[-1]-u0 (drain velocity, signed).
"""
import sys, math, time
import numpy as np

CHAIN = "/home/user/FableComputer/fable-model-chain"
sys.path.insert(0, CHAIN)
import constants as C
import ds_cell as DS
import solver as SOL
from solver import _setup, _step_LF

S_PL = DS.plasmon_speed(); TAU = C.tau(C.Tcap); L_CELL = DS.cell_length(S_PL)
MTH_ANALYTIC = DS.M_threshold(L_CELL, S_PL, TAU)      # 0.14708333333333332
F0N = C.f0 * L_CELL / S_PL                            # 0.25
RT_PS = 1.0 / (2 * C.f0) * 1e12                       # 0.5 ps per round trip


def mth_num(N, n_roundtrips=90):
    """run_all.measure_Mth_num generalized to grid N (verbatim scan and interpolation)."""
    xs = np.linspace(1.05, 1.30, 8)
    g = [SOL.growth_rate(x * MTH_ANALYTIC, n_roundtrips=n_roundtrips, N=N) for x in xs]
    for i in range(len(xs) - 1):
        if g[i] < 0 <= g[i + 1]:
            xz = xs[i] + (xs[i + 1] - xs[i]) * (-g[i]) / (g[i + 1] - g[i])
            return xz * MTH_ANALYTIC
    return float("nan")


def make_sig_duty(bits, repT, f0_n, amp, duty=0.8, edge_rt=2.0):
    """07-31 exp_duty.make_sig_duty, verbatim logic (active-envelope carrier reference)."""
    edge = edge_rt * 2.0
    span = duty * repT

    def sig(t):
        slot = int(t / repT)
        b = bits[slot] if slot < len(bits) else 0
        if not b:
            return 0.0
        x = t - slot * repT
        if x >= span:
            return 0.0
        if x < edge:
            env = 0.5 * (1 - math.cos(math.pi * x / edge))
        elif x > span - edge:
            env = 0.5 * (1 - math.cos(math.pi * (span - x) / edge))
        else:
            env = 1.0
        tc = slot * repT + 0.5 * span
        return amp * env * math.sin(2 * math.pi * f0_n * (t - tc))
    return sig


def released_dt(M, N, cfl=0.4):
    dx = 1.0 / N
    cmax = 1.0 + abs(M) + 0.2
    return cfl * dx / cmax


def run_cell(M, N, n_roundtrips, clamp, cfl=0.4, T=C.Tcap):
    """One released cell, released stepping verbatim; `clamp` is a callable of the
    step index k and time t returning the source-clamp perturbation (h_left - 1).
    Returns the three drain/intracavity series and the time grid."""
    s, tau, L, tau_n, f0n = _setup(N, T)
    u0 = M
    dx = 1.0 / N
    dt = released_dt(M, N, cfl)
    nsteps = int(n_roundtrips * 2.0 / dt)
    h = np.ones(N); hu = np.ones(N) * u0
    cav = np.empty(nsteps); drn_h = np.empty(nsteps); drn_u = np.empty(nsteps); tarr = np.empty(nsteps)
    t = 0.0
    for k in range(nsteps):
        h_left = 1.0 + clamp(k, t)
        h, hu = _step_LF(h, hu, dx, dt, u0, tau_n, h_left, u0)
        if not np.all(np.isfinite(h)) or np.any(h < 1e-6):
            cav = cav[:k]; drn_h = drn_h[:k]; drn_u = drn_u[:k]; tarr = tarr[:k]; break
        u = hu / h
        cav[k] = np.max(np.abs(u - u0))
        drn_h[k] = h[-1] - 1.0
        drn_u[k] = u[-1] - u0
        tarr[k] = t
        t += dt
    return dict(t=tarr, cav=cav, drn_h=drn_h, drn_u=drn_u, dt=dt, f0_n=f0n, M=M, N=N)


def source_clamp(sigfun):
    return lambda k, t: sigfun(t)


def upstream_clamp(up, plane, kappa):
    """Clamp for cell 2 from cell 1's recorded series `up` (a run_cell dict).
    Uses the sample at the same step when the time grids coincide, else np.interp."""
    x = up["drn_h"] if plane == "h" else up["drn_u"]
    tu = up["t"]
    # state at t_k is the state produced by step k-1; at k = 0 the cell is unperturbed
    x_state = np.concatenate(([0.0], x[:-1]))

    def clamp_same(k, t):
        return kappa * (x_state[k] if k < len(x_state) else x[-1])

    def clamp_interp(k, t):
        return kappa * float(np.interp(t, tu, x_state))
    return clamp_same, clamp_interp


def run_chain(M1, M2, N, n_roundtrips, sigfun, kappa=1.0, plane="h", cfl=0.4, up=None):
    """Two-cell chain. Returns (cell1, cell2). `up` may pass a pre-run cell 1."""
    c1 = up if up is not None else run_cell(M1, N, n_roundtrips, source_clamp(sigfun), cfl)
    same, interp = upstream_clamp(c1, plane, kappa)
    dt2 = released_dt(M2, N, cfl)
    clamp = same if abs(dt2 - c1["dt"]) < 1e-15 else interp
    c2 = run_cell(M2, N, n_roundtrips, clamp, cfl)
    return c1, c2


# ---------------- scoring (07-25/07-31/08-02 conventions) ----------------
def slot_windows(t, repT, nslots, w_lo=0.25, w_hi=0.72, shift=0.0):
    """Boolean masks of the scoring window per slot; `shift` (time units) delays the
    window by a stage latency, the same for every slot (fixed before scoring)."""
    return [(t >= (k + w_lo) * repT + shift) & (t < (k + w_hi) * repT + shift) for k in range(nslots)]


def slot_peaks(x, masks):
    return np.array([np.max(np.abs(x[m])) if m.sum() > 3 else np.nan for m in masks])


def slot_modes(x, t, masks, f0_n, repT, duty=0.8, shift=0.0):
    """08-12 slot-mode lock-in amplitude: |<x(t) e^{-i 2π f0_n (t - t_c)}>| over the
    window, t_c = active-envelope centre (0.5*duty*repT into the slot), plus the
    stage shift. Returned as (amplitude, phase deg) per slot."""
    amps = []; phs = []
    for k, m in enumerate(masks):
        if m.sum() <= 3:
            amps.append(np.nan); phs.append(np.nan); continue
        tc = k * repT + 0.5 * duty * repT + shift
        z = np.mean(x[m] * np.exp(-2j * np.pi * f0_n * (t[m] - tc))) * 2.0
        amps.append(abs(z)); phs.append(math.degrees(np.angle(z)))
    return np.array(amps), np.array(phs)


def metrics(bits, pk_M, pk_0, drop=4):
    """07-31 metrics on per-slot peaks: worst/mean '1' gain vs identical-pattern passive
    run, raw '1' pp, eye, and the '0'-floor max0_below_mean1 (peak denomination)."""
    n = min(len(pk_M), len(pk_0))
    b = np.asarray(bits[drop:n]); pM = pk_M[drop:n]; p0 = pk_0[drop:n]
    ones = b == 1; zeros = b == 0
    res = {}
    if ones.any():
        g = 20 * np.log10(pM[ones] / p0[ones])
        res["G_worst1_dB"] = float(np.min(g)); res["G_mean1_dB"] = float(np.mean(g))
        res["pp_raw_dB"] = float(20 * np.log10(np.max(pM[ones]) / np.min(pM[ones])))
        res["mean1_level"] = float(np.mean(pM[ones])); res["min1_level"] = float(np.min(pM[ones]))
    if ones.any() and zeros.any():
        res["eye_dB"] = float(20 * np.log10(np.min(pM[ones]) / np.max(pM[zeros])))
        res["max0_below_mean1_dB"] = float(20 * np.log10(np.max(pM[zeros]) / np.mean(pM[ones])))
        res["max0_level"] = float(np.max(pM[zeros]))
    return res


def floor_mode(bits, mode_amp, drop=4):
    """'0'-floor in the slot-mode denomination: max '0' mode amplitude over mean '1'."""
    n = len(mode_amp); b = np.asarray(bits[drop:n]); a = mode_amp[drop:n]
    ones = b == 1; zeros = b == 0
    if not (ones.any() and zeros.any()):
        return float("nan")
    return float(20 * np.log10(np.max(a[zeros]) / np.mean(a[ones])))


def default_bits(nslots=40, seed=7):
    return np.random.default_rng(seed).integers(0, 2, nslots)


def platform_line():
    import platform as P
    return f"{P.system()} {P.machine()}, Python {P.python_version()}, numpy {np.__version__}"
