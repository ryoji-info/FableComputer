# -*- coding: utf-8 -*-
"""Augmented-solver instrument for the 2026-08-08 Fable session.

Released fable-model-chain imported UNEDITED. The run() path below is a
line-faithful transcription of solver.run for drive_kind='none' (same RNG
draws, same op order) so that nu=0 is bit-identical to the released solver;
at nu>0 a momentum-only viscous sub-step (Strang-free, first-order split,
sub-cycled explicit) is applied AFTER the released _step_LF + relaxation.

Boundary treatments for the viscous stencil (the sensitivity axis):
  T1 'released-ghosts': source ghost u = u[0] (zero-gradient, the released
     HU[0] semantics); drain ghost u = u0/h[-1] (the released HU[-1]=u0,
     H[-1]=h[-1] semantics).
  T2 'neumann': zero viscous flux both ends (u ghost = nearest interior).
"""
import math
import statistics
import sys

import numpy as np

CHAIN = "/Users/rxiii/Documents/GitHub/FableComputer/fable-model-chain"
sys.path.insert(0, CHAIN)
import constants as C                      # noqa: E402
from ds_cell import M_threshold            # noqa: E402
import solver as S                         # noqa: E402

MTH353 = 0.14708333333333332


def run_aug(M, N=240, n_roundtrips=120, cfl=0.4, T=C.Tcap, seed=1,
            nu=0.0, bc="released-ghosts", subcycle_factor=1.0):
    """solver.run(drive_kind='none') transcribed, plus optional viscous sub-step."""
    s, tau, L, tau_n, f0n = S._setup(N, T)
    f0_n = f0n
    u0 = M
    dx = 1.0 / N
    cmax = 1.0 + abs(u0) + 0.2
    dt = cfl * dx / cmax
    nsteps = int(n_roundtrips * 2.0 / dt)
    h = np.ones(N); hu = np.ones(N) * u0
    rng = np.random.default_rng(seed)
    h += 1e-4 * rng.standard_normal(N)     # drive_kind == 'none' seed noise
    out = np.empty(nsteps); tarr = np.empty(nsteps); cav = np.empty(nsteps)
    if nu > 0.0:
        m = max(1, math.ceil(subcycle_factor * nu * dt / (0.45 * dx * dx)))
        alpha = nu * (dt / m) / (dx * dx)
    t = 0.0
    for k in range(nsteps):
        h, hu = S._step_LF(h, hu, dx, dt, u0, tau_n, 1.0, u0)
        if nu > 0.0:
            u = hu / h
            for _ in range(m):
                if bc == "released-ghosts":
                    ug0 = u[0]
                    ugN = u0 / h[-1]
                else:                       # 'neumann'
                    ug0 = u[0]
                    ugN = u[-1]
                lap = np.empty_like(u)
                lap[1:-1] = u[2:] - 2.0 * u[1:-1] + u[:-2]
                lap[0] = u[1] - 2.0 * u[0] + ug0
                lap[-1] = ugN - 2.0 * u[-1] + u[-2]
                u = u + alpha * lap
            hu = h * u
        if not np.all(np.isfinite(h)) or np.any(h < 1e-6):
            out = out[:k]; tarr = tarr[:k]; cav = cav[:k]; break
        out[k] = hu[-1] / h[-1] - u0
        cav[k] = np.max(np.abs(hu / h - u0))
        tarr[k] = t
        t += dt
    return dict(t=tarr, drain=out, cav=cav, dt=dt, f0_n=f0_n, tau_n=tau_n,
                L=L, s=s, M=M)


def growth_aug(M, **kw):
    """solver.growth_rate transcribed onto run_aug (identical fit convention)."""
    r = run_aug(M, **kw)
    sig = np.abs(r["drain"])
    t = r["t"]
    if len(t) < 100:
        return np.nan
    i0 = int(0.4 * len(t))
    tt = t[i0:]
    amp = sig[i0:]
    nb = 40
    edges = np.linspace(tt[0], tt[-1], nb + 1)
    cen = 0.5 * (edges[1:] + edges[:-1])
    rms = np.array([np.sqrt(np.mean(amp[(tt >= edges[i]) & (tt < edges[i + 1])] ** 2) + 1e-30)
                    for i in range(nb)])
    good = rms > 0
    A = np.polyfit(cen[good], np.log(rms[good]), 1)
    return A[0] * 2.0


def threshold(N=240, cfl=0.4, seed=1, n_roundtrips=240, nu=0.0,
              bc="released-ghosts", subcycle_factor=1.0, start=2,
              cache=None, verbose=False):
    """Widened-bracket root at released node spacing (08-07 sec 3.1 convention):
    nodes x_i = 1.05 + i*(0.25/7), integer i (any sign); walk down from `start`
    to a negative-growth node, then up to the first non-negative; linear interp."""
    step = 0.25 / 7.0

    def g_at(i):
        key = (N, cfl, seed, n_roundtrips, nu, bc, subcycle_factor, i)
        if cache is not None and key in cache:
            return cache[key]
        x = 1.05 + i * step
        val = growth_aug(x * MTH353, N=N, cfl=cfl, seed=seed,
                         n_roundtrips=n_roundtrips, nu=nu, bc=bc,
                         subcycle_factor=subcycle_factor)
        if cache is not None:
            cache[key] = val
        if verbose:
            print(f"    node {i} (x={x:.6f}, M={x*MTH353:.8f}): g={val:+.6e}")
        return val

    i = start
    gi = g_at(i)
    while not (gi < 0):                    # walk down to a negative node
        i -= 1
        gi = g_at(i)
        if i < -40:
            return float("nan")
    while True:                            # walk up to first non-negative
        gj = g_at(i + 1)
        if gj >= 0:
            break
        i += 1
        gi = gj
        if i > 80:
            return float("nan")
    xi = 1.05 + i * step
    xz = xi + step * (-gi) / (gj - gi)
    return xz * MTH353


def census(N=240, cfl=0.4, n_roundtrips=240, nu=0.0, bc="released-ghosts",
           subcycle_factor=1.0, start=2, seeds=range(1, 9), cache=None,
           label=""):
    roots = []
    for sd in seeds:
        r = threshold(N=N, cfl=cfl, seed=sd, n_roundtrips=n_roundtrips, nu=nu,
                      bc=bc, subcycle_factor=subcycle_factor, start=start,
                      cache=cache)
        roots.append(r)
    med = statistics.median(roots)
    sd_ = statistics.pstdev(roots)
    rng_ = max(roots) - min(roots)
    print(f"[{label}] N={N} cfl={cfl} nu={nu:.10g} bc={bc} rt={n_roundtrips} "
          f"median={med:.10f} sd={sd_:.3e} range={rng_:.3e}")
    print(f"    roots: {[f'{r:.8f}' for r in roots]}")
    return dict(median=med, sd=sd_, range=rng_, roots=roots)


def nu_num(N, cfl, M):
    """1/2 tr D of the LF modified-equation matrix (08-07 sec 1.1)."""
    dx = 1.0 / N
    cmax = 1.0 + abs(M) + 0.2
    dt = cfl * dx / cmax
    nubar = dt / dx
    return (dx * dx / (2.0 * dt)) * (1.0 - nubar * nubar * (1.0 + M * M))


def partner_cfl(N, cfl0, M, dnu):
    """Solve nu_num(N, cfl2, M) = nu_num(N, cfl0, M) + dnu for cfl2 (bisection).
    nu_num decreases with cfl, so dnu>0 means cfl2 < cfl0."""
    target = nu_num(N, cfl0, M) + dnu
    lo, hi = 0.02, 0.999
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if nu_num(N, mid, M) > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


NU0 = 0.015270489933688769                 # (vF^2 tau_ee/4)/(L s), 07-22/08-07
