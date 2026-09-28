# §7 Runnable listings — verbatim sources

The exact files that produced every number in the reply (`listings/` in this run directory; adjust `CHAIN` and the scratch paths). Run order and cost on this container (4 workers): `gate.py` (~2.5 min) → `launch.py` + `campaign.py families.json 4` (~45 min for the N = 240 families, ~35 min per N = 480 family) → `campaign.py families2.json 4` (N = 720 rung, the N = 480 m = 28 family and the junction sweep, ~70 min) → `depth.py depth_cfgs.json 2` (~11 min) → `gen_table2.py` + `table2.py` (~50 min single worker) → `analyze.py`, `analyze_depth.py`, `residue.py`, `render_tables.py` (seconds). `analyze_depth.py`, `residue.py` and `render_tables.py` are published as revised after the pre-publication checks (the window-shift cap removed, per-stage lags and scored counts added, the residue table's denominators named and its computation shipped). `campaign.py` is published in its final form: its scorer was rewritten mid-campaign to hold one window-shift mask at a time after the first version was OOM-killed at N = 720; the scoring arithmetic is unchanged and the N = 240/480 families it produced were re-scored identically.

### `cascade_driver.py`

```python
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
    Returns the three recorded series (cav = max over the cell of |u - u0|, the drain density and the drain velocity) and the time grid."""
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

```

### `gate.py`

```python
# Gate: reproduce 08-12 §1 gate 1 (M_th_num ladder) and gate 2 (the 08-02 §3.2 m=30, N=240
# duty-0.8 ratio-bias row: 8.287855791924017 / -11.828336851447219 / -11.775002445226676),
# then time one run.
import sys, time, json
sys.path.insert(0, "/tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/session")
from cascade_driver import *
t0 = time.time()
R = json.load(open(CHAIN + "/results.json"))
m240 = mth_num(240)
print("M_th_num(240) =", repr(m240), " results.json", repr(R["M_th_num"]), " rel", abs(m240 - R["M_th_num"]) / R["M_th_num"], f"[{time.time()-t0:.0f}s]", flush=True)
m, N = 30, 240
repT = 2.0 * m; nslots = 40; nrt = nslots * m
bits = default_bits(nslots, 7)
bias = 0.7 * m240
sig = make_sig_duty(bits, repT, F0N, 2e-3, duty=0.8, edge_rt=2.0)
t1 = time.time()
cM = run_cell(bias, N, nrt, source_clamp(sig))
t2 = time.time()
c0 = run_cell(0.0, N, nrt, source_clamp(sig))
t3 = time.time()
masksM = slot_windows(cM["t"], repT, nslots); masks0 = slot_windows(c0["t"], repT, nslots)
for obs in ("cav", "drn_h", "drn_u"):
    r = metrics(bits, slot_peaks(cM[obs], masksM), slot_peaks(c0[obs], masks0))
    print(obs, {k: (round(v, 12) if isinstance(v, float) else v) for k, v in r.items()}, flush=True)
print("targets (08-02 §3.2 / 08-12 gate 2): cav_u gain 8.287855791924017, floors cav_u -11.828336851447219 drn_h -11.775002445226676")
print(f"timing: active run {t2-t1:.1f}s, passive run {t3-t2:.1f}s, steps {len(cM['t'])} / {len(c0['t'])}; dt {cM['dt']:.6e} / {c0['dt']:.6e}")
print("platform:", platform_line())

```

### `launch.py`

```python
import sys, os, json, time
SESSION = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SESSION)
from cascade_driver import mth_num, platform_line
t0 = time.time()
mth = {}
for N in (240, 480):
    mth[N] = float(mth_num(N)); print(f"M_th_num({N}) = {mth[N]!r}  [{time.time()-t0:.0f}s]", flush=True)
json.dump(mth, open(os.path.join(SESSION, "mth_num.json"), "w"))
cfgs = []
for m in (28, 30):
    cfgs.append({"tag": f"N480_m{m}_s7", "m": m, "N": 480, "seed": 7, "mth_num": mth[480], "depth": 2, "primary_J": -1})
for seed in (7, 11, 13):
    for m in (30, 28):
        cfgs.append({"tag": f"N240_m{m}_s{seed}", "m": m, "N": 240, "seed": seed, "mth_num": mth[240],
                     "depth": 4 if seed == 7 else 2, "primary_J": -1})
json.dump(cfgs, open(os.path.join(SESSION, "families.json"), "w"), indent=1)
print(f"{len(cfgs)} families written; platform {platform_line()}", flush=True)

```

### `campaign.py`

```python
# -*- coding: utf-8 -*-
"""Fable Session 2026-09-28 — cascade campaign (families run in parallel).

One FAMILY = (m, N, seed): cell 1 active + passive (the promoted single-cell rows), then
cell 2 for every junction class J in dB (kappa = 10^(J/20)) in the three chains:
  MM : active cell 1 -> active cell 2      (the real cascade)
  M0 : active cell 1 -> passive cell 2     (cell 2's own reference on its real input)
  00 : passive cell 1 -> passive cell 2    (the passive twin chain, G4's reference)
plus the velocity-plane sensitivity at one J, and (primary family) a depth-4 extension.
Every run's per-slot peaks (cav, drn_h, drn_u) and drn_h slot-mode amplitudes are stored
for a grid of window shifts (0..2 rt in 0.125-rt steps), so the per-stage window rule is
fixed BEFORE scoring and applied identically to active and passive chains.
"""
import sys, os, json, time, math
import numpy as np
from multiprocessing import Pool
SESSION = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SESSION)
from cascade_driver import *

SHIFTS = np.arange(0.0, 8.01, 0.25)        # time units (0..4 rt); 0.25 = 1/8 rt
OUTDIR = os.path.join(SESSION, "runs")
os.makedirs(OUTDIR, exist_ok=True)


def score_all(cell, repT, nslots, f0n, duty=0.8):
    """Per-slot peaks / slot-mode amplitudes for every window shift, computed one shift at a
    time so the boolean masks are never all resident (the earlier version held
    33 shifts x 40 slots x nsteps booleans and was OOM-killed at N = 720)."""
    t = cell["t"]
    out = {"shifts": SHIFTS.tolist(), "nsteps": int(len(t)), "dt": float(cell["dt"]), "M": float(cell["M"])}
    for obs in ("cav", "drn_h", "drn_u"):
        out["pk_" + obs] = []
    out["mode_drn_h"] = []; out["phase_drn_h"] = []
    for sh in SHIFTS:
        mk = slot_windows(t, repT, nslots, shift=float(sh))
        for obs in ("cav", "drn_h", "drn_u"):
            out["pk_" + obs].append(slot_peaks(cell[obs], mk).tolist())
        a, p = slot_modes(cell["drn_h"], t, mk, f0n, repT, duty, shift=float(sh))
        out["mode_drn_h"].append(a.tolist()); out["phase_drn_h"].append(p.tolist())
        del mk
    tp = []
    for k in range(nslots):
        mk = (t >= k * repT) & (t < (k + 1) * repT)
        if mk.sum() > 3:
            i = int(np.argmax(np.abs(cell["drn_h"][mk]))); tp.append(float(t[mk][i] - k * repT))
        else:
            tp.append(float("nan"))
    out["tpeak_drn_h"] = tp
    step = max(1, len(t) // 20000)
    out["ds_step"] = step
    out["ds_t"] = t[::step].tolist(); out["ds_drn_h"] = cell["drn_h"][::step].tolist()
    return out


def family(cfg):
    t0 = time.time()
    m, N, seed = cfg["m"], cfg["N"], cfg["seed"]
    bias = 0.7 * cfg["mth_num"]
    amp = cfg.get("amp", 2e-3)
    Js = cfg.get("Js", [0, -1, -3, -6])
    repT = 2.0 * m; nslots = cfg.get("nslots", 40); nrt = nslots * m
    bits = default_bits(nslots, seed)
    sig = make_sig_duty(bits, repT, F0N, amp, duty=0.8, edge_rt=2.0)
    log = []
    def note(s):
        log.append(f"[{time.time()-t0:7.0f}s] {s}"); print(f"{cfg['tag']} {log[-1]}", flush=True)
    c1M = run_cell(bias, N, nrt, source_clamp(sig)); note("cell1 active done")
    c10 = run_cell(0.0, N, nrt, source_clamp(sig)); note("cell1 passive done")
    res = {"cfg": cfg, "bias": bias, "bits": bits.tolist(), "repT": repT, "nslots": nslots,
           "cell1": {"M": score_all(c1M, repT, nslots, F0N), "0": score_all(c10, repT, nslots, F0N)},
           "chains": {}}
    keep = {}
    for J in Js:
        kappa = 10 ** (J / 20.0)
        for label, M2, up in (("MM", bias, c1M), ("M0", 0.0, c1M), ("00", 0.0, c10)):
            _, c2 = run_chain(None, M2, N, nrt, sig, kappa=kappa, plane="h", up=up)
            key = f"J{J}_h_{label}"
            res["chains"][key] = score_all(c2, repT, nslots, F0N)
            if J == cfg.get("primary_J", -1):
                keep[label] = c2
            else:
                del c2
            note(f"{key} done")
    # velocity-plane sensitivity at the primary J (optional)
    Jp = cfg.get("primary_J", -1); kappa = 10 ** (Jp / 20.0)
    for label, M2, up in ((("MM", bias, c1M), ("M0", 0.0, c1M), ("00", 0.0, c10)) if cfg.get("plane_u", True) else ()):
        _, c2 = run_chain(None, M2, N, nrt, sig, kappa=kappa, plane="u", up=up)
        res["chains"][f"J{Jp}_u_{label}"] = score_all(c2, repT, nslots, F0N); note(f"J{Jp}_u_{label} done")
    # depth extension on the primary J, density plane: stages 3..depth
    depth = cfg.get("depth", 2)
    if depth > 2 and keep:
        actM = keep["MM"]; pas0 = keep["00"]
        for stage in range(3, depth + 1):
            _, nM = run_chain(None, bias, N, nrt, sig, kappa=kappa, plane="h", up=actM)      # active chain
            _, nMx = run_chain(None, 0.0, N, nrt, sig, kappa=kappa, plane="h", up=actM)      # passive stage on the active chain
            _, n0 = run_chain(None, 0.0, N, nrt, sig, kappa=kappa, plane="h", up=pas0)       # passive chain
            res["chains"][f"J{Jp}_h_stage{stage}_MM"] = score_all(nM, repT, nslots, F0N)
            res["chains"][f"J{Jp}_h_stage{stage}_M0"] = score_all(nMx, repT, nslots, F0N)
            res["chains"][f"J{Jp}_h_stage{stage}_00"] = score_all(n0, repT, nslots, F0N)
            actM, pas0 = nM, n0
            note(f"stage {stage} done")
    res["log"] = log; res["secs"] = round(time.time() - t0, 1); res["platform"] = platform_line()
    with open(os.path.join(OUTDIR, cfg["tag"] + ".json"), "w") as f:
        json.dump(res, f)
    return cfg["tag"], res["secs"]


if __name__ == "__main__":
    cfgs = json.load(open(sys.argv[1]))
    nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    print(f"{len(cfgs)} families, {nproc} workers, platform {platform_line()}", flush=True)
    with Pool(nproc) as pool:
        for tag, secs in pool.imap_unordered(family, cfgs):
            print(f"DONE {tag} in {secs:.0f}s", flush=True)
    print("ALL DONE", flush=True)

```

### `depth.py`

```python
# -*- coding: utf-8 -*-
"""Depth re-run for the primary families with FULL-resolution series kept (float32 .npy),
so any per-stage window rule can be applied after the fact. J = -1 (kappa = 10^(-1/20)),
density plane, stages 2..DEPTH: MM (active chain), M0 (passive stage on the active chain),
00 (passive twin chain)."""
import sys, os, json, time
import numpy as np
from multiprocessing import Pool
SESSION = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SESSION)
from cascade_driver import *
OUT = os.path.join(SESSION, "depth"); os.makedirs(OUT, exist_ok=True)


def save(tag, cell):
    np.save(os.path.join(OUT, tag + "_t.npy"), cell["t"].astype(np.float32))
    for obs in ("cav", "drn_h", "drn_u"):
        np.save(os.path.join(OUT, f"{tag}_{obs}.npy"), cell[obs].astype(np.float32))


def job(cfg):
    t0 = time.time()
    m, N, seed, depth = cfg["m"], cfg["N"], cfg["seed"], cfg["depth"]
    bias = 0.7 * cfg["mth_num"]; kappa = 10 ** (-1 / 20.0)
    repT = 2.0 * m; nslots = 40; nrt = nslots * m
    bits = default_bits(nslots, seed)
    sig = make_sig_duty(bits, repT, F0N, 2e-3, duty=0.8, edge_rt=2.0)
    tag = cfg["tag"]
    c1M = run_cell(bias, N, nrt, source_clamp(sig)); save(f"{tag}_st1_M", c1M)
    c10 = run_cell(0.0, N, nrt, source_clamp(sig)); save(f"{tag}_st1_0", c10)
    actM, pas0 = c1M, c10
    for stage in range(2, depth + 1):
        _, nM = run_chain(None, bias, N, nrt, sig, kappa=kappa, plane="h", up=actM)
        _, nMx = run_chain(None, 0.0, N, nrt, sig, kappa=kappa, plane="h", up=actM)
        _, n0 = run_chain(None, 0.0, N, nrt, sig, kappa=kappa, plane="h", up=pas0)
        save(f"{tag}_st{stage}_MM", nM); save(f"{tag}_st{stage}_M0", nMx); save(f"{tag}_st{stage}_00", n0)
        actM, pas0 = nM, n0
        print(f"{tag} stage {stage} done [{time.time()-t0:.0f}s]", flush=True)
    json.dump({"cfg": cfg, "bias": bias, "bits": bits.tolist(), "repT": repT, "nslots": nslots, "dtM": c1M["dt"], "dt0": c10["dt"],
               "secs": time.time() - t0, "platform": platform_line()}, open(os.path.join(OUT, tag + ".json"), "w"))
    return tag


if __name__ == "__main__":
    cfgs = json.load(open(sys.argv[1]))
    with Pool(int(sys.argv[2]) if len(sys.argv) > 2 else 2) as pool:
        for tag in pool.imap_unordered(job, cfgs):
            print("DONE", tag, flush=True)
    print("DEPTH DONE", flush=True)

```

### `table2.py`

```python
# -*- coding: utf-8 -*-
"""Table 2 — boundary-driven single cell at the MATCHED input amplitude.
For each (family, J): A* = kappa * mean-'1' drain-density peak of active cell 1 (the amplitude
cell 2 actually receives); run the single cell with the 07-31 duty-0.8 launch at amp = A*
(same PRBS, same bias, same grid), active and passive; report G_worst1 / G_mean1 (cav and drn_h).
"""
import sys, os, json, time
import numpy as np
from multiprocessing import Pool
SESSION = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SESSION)
from cascade_driver import *
OUT = os.path.join(SESSION, "table2.jsonl")


def job(cfg):
    t0 = time.time()
    m, N, seed, amp, bias = cfg["m"], cfg["N"], cfg["seed"], cfg["amp"], cfg["bias"]
    repT = 2.0 * m; nslots = 40; nrt = nslots * m
    bits = default_bits(nslots, seed)
    sig = make_sig_duty(bits, repT, F0N, amp, duty=0.8, edge_rt=2.0)
    cM = run_cell(bias, N, nrt, source_clamp(sig)); c0 = run_cell(0.0, N, nrt, source_clamp(sig))
    mM = slot_windows(cM["t"], repT, nslots); m0 = slot_windows(c0["t"], repT, nslots)
    res = dict(cfg)
    for obs in ("cav", "drn_h"):
        res[obs] = metrics(bits, slot_peaks(cM[obs], mM), slot_peaks(c0[obs], m0))
    res["secs"] = round(time.time() - t0, 1)
    return res


if __name__ == "__main__":
    cfgs = json.load(open(sys.argv[1])); nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    with open(OUT, "a") as f, Pool(nproc) as pool:
        for r in pool.imap_unordered(job, cfgs):
            f.write(json.dumps(r) + "\n"); f.flush()
            print({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items() if k in ("tag", "J", "amp", "secs")}, r["cav"]["G_worst1_dB"], r["cav"]["G_mean1_dB"], flush=True)
    print("TABLE2 DONE", flush=True)

```

### `gen_table2.py`

```python
import json, os
S=os.path.dirname(os.path.abspath(__file__))
A=json.load(open(S+"/analysis.json"))
cfgs=[]
for tag,R in A.items():
    if tag.endswith("_Jext"): continue
    for Jk,ent in R["J"].items():
        J,plane=Jk.split("_")
        if plane!="h": continue
        if R["seed"]!=7 and J!="-1": continue
        cfgs.append({"tag":tag,"m":R["m"],"N":R["N"],"seed":R["seed"],"J":int(J),"amp":ent["rule"]["mean1_in_cell2"],"bias":R["bias"],"kind":"matched"})
    if R["seed"]==7 and R["N"]==240:
        for a in (4e-3,7e-3,1.1e-2,1.7e-2,2.4e-2):
            cfgs.append({"tag":tag,"m":R["m"],"N":R["N"],"seed":7,"J":None,"amp":a,"bias":R["bias"],"kind":"ladder"})
json.dump(cfgs,open(S+"/table2_cfgs.json","w"),indent=1)
print(len(cfgs),"table2 jobs")

```

### `analyze.py`

```python
# -*- coding: utf-8 -*-
"""Score the cascade campaign under ONE window rule fixed before scoring.

Window rule (stated, applied identically to active and passive chains): stage k's
scoring window is the promoted [0.25, 0.72]*repT window delayed by (k-1)*L, where L is
the passive-chain stage latency measured ONCE per family from the passive twin chain
(J = -1, density plane, stage 2 vs cell 1) as the lag maximising the cross-correlation
of the |drn_h| envelopes, rounded to the stored 1/8-rt shift grid. The unshifted
(L = 0) reading is reported beside it as the sensitivity.
"""
import json, os, sys, math, glob
import numpy as np
SESSION = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SESSION)
from cascade_driver import metrics, floor_mode, RT_PS
RUNS = os.path.join(SESSION, "runs")
STRICT = 20 * math.log10(0.25641458774368575)   # -11.8211 dB
ROUND = -10.0


def idx(shifts, s):
    return int(np.argmin(np.abs(np.asarray(shifts) - s)))


def envelope_lag(a, b, t):
    """Lag (time units) maximising the cross-correlation of |a| and |b| envelopes (moving
    mean over ~one carrier period), b delayed relative to a. Positive = b lags a."""
    dt = t[1] - t[0]
    w = max(1, int(round(4.0 / dt)))          # one carrier period = 4 time units
    k = np.ones(w) / w
    ea = np.convolve(np.abs(a), k, mode="same"); eb = np.convolve(np.abs(b), k, mode="same")
    ea = ea - ea.mean(); eb = eb - eb.mean()
    nmax = int(round(12.0 / dt))              # search up to 6 rt
    best, bl = -np.inf, 0
    for lag in range(0, nmax):
        c = np.dot(ea[:len(ea) - lag], eb[lag:]) if lag else np.dot(ea, eb)
        if c > best: best, bl = c, lag
    return bl * dt


def peaktime_lag(bits, tp1, tp2, drop=4):
    b = np.asarray(bits[drop:]); d = np.asarray(tp2[drop:]) - np.asarray(tp1[drop:])
    return float(np.median(d[b == 1]))


def stage_scores(bits, upstream_pk, chain, ref, shift_idx, key_obs="cav"):
    """gain of `chain` over `ref` at the given shift index, for obs cav and drn_h, plus
    floors in both denominations, pp, eye (all on `chain`)."""
    out = {}
    for obs in ("cav", "drn_h"):
        r = metrics(bits, np.array(chain["pk_" + obs][shift_idx]), np.array(ref["pk_" + obs][shift_idx]))
        out[obs] = r
    out["floor_mode_drn_h"] = floor_mode(bits, np.array(chain["mode_drn_h"][shift_idx]))
    return out


def analyze_family(path):
    F = json.load(open(path)); cfg = F["cfg"]; bits = F["bits"]; shifts = F["cell1"]["M"]["shifts"]
    repT = F["repT"]; m = cfg["m"]; N = cfg["N"]; seed = cfg["seed"]; Jp = cfg.get("primary_J", -1)
    c1M, c10 = F["cell1"]["M"], F["cell1"]["0"]
    R = {"tag": cfg["tag"], "m": m, "N": N, "seed": seed, "bias": F["bias"], "repT": repT, "secs": F.get("secs")}
    # --- cell 1 (the promoted single-cell rows) ---
    R["cell1"] = {obs: metrics(bits, np.array(c1M["pk_" + obs][0]), np.array(c10["pk_" + obs][0])) for obs in ("cav", "drn_h")}
    R["cell1"]["floor_mode_drn_h"] = floor_mode(bits, np.array(c1M["mode_drn_h"][0]))
    # --- latency from the passive twin chain (rule) and the active chain (reported) ---
    p00 = F["chains"][f"J{Jp}_h_00"]; pMM = F["chains"][f"J{Jp}_h_MM"]
    t = np.array(c10["ds_t"])
    L_env_pas = envelope_lag(np.array(c10["ds_drn_h"]), np.array(p00["ds_drn_h"]), t)
    L_env_act = envelope_lag(np.array(c1M["ds_drn_h"]), np.array(pMM["ds_drn_h"]), np.array(c1M["ds_t"]))
    L_pk_pas = peaktime_lag(bits, c10["tpeak_drn_h"], p00["tpeak_drn_h"])
    L_pk_act = peaktime_lag(bits, c1M["tpeak_drn_h"], pMM["tpeak_drn_h"])
    L_rule = shifts[idx(shifts, L_env_pas)]
    R["latency"] = {"env_passive": L_env_pas, "env_active": L_env_act, "peak_passive": L_pk_pas, "peak_active": L_pk_act,
                    "rule_shift": L_rule, "rule_rt": L_rule / 2.0, "rule_ps": L_rule / 2.0 * RT_PS, "rule_frac_slot": L_rule / repT}
    s2 = idx(shifts, L_rule); s0 = 0
    # --- per junction class ---
    R["J"] = {}
    for key in F["chains"]:
        if not key.endswith("_MM") or "stage" in key: continue
        base = key[:-3]                         # e.g. J-1_h
        J = int(base.split("_")[0][1:]); plane = base.split("_")[1]
        MM = F["chains"][base + "_MM"]; M0 = F["chains"][base + "_M0"]; O0 = F["chains"][base + "_00"]
        kappa = 10 ** (J / 20.0)
        ent = {}
        for sname, si in (("rule", s2), ("unshifted", s0)):
            g_chain = stage_scores(bits, None, MM, O0, si)      # definition A: over the passive twin chain
            g_c2c = stage_scores(bits, None, MM, M0, si)        # cell-to-cell: cell 2 active vs passive on its real input
            g_up = stage_scores(bits, None, M0, O0, si)         # cell-1 gain as seen through a passive cell 2
            # absolute (port-to-port) definition B, drain density vs the 2e-3 launch amplitude
            amp = cfg.get("amp", 2e-3)
            def mean1(ch, obs, s):
                pk = np.array(ch["pk_" + obs][s]); b = np.asarray(bits[4:len(pk)]); return float(np.mean(pk[4:][b == 1]))
            T2_pas = 20 * math.log10(mean1(O0, "drn_h", si) / (kappa * mean1(c10, "drn_h", 0)))
            G1_abs = 20 * math.log10(mean1(c1M, "drn_h", 0) / amp)
            Gc_abs = 20 * math.log10(mean1(MM, "drn_h", si) / amp)
            T1_pas = 20 * math.log10(mean1(c10, "drn_h", 0) / amp)
            ent[sname] = {"chain_over_passive": g_chain, "cell2_on_real_input": g_c2c, "cell1_through_passive2": g_up,
                          "passive_transfer_stage2_dB": T2_pas, "passive_transfer_stage1_dB": T1_pas,
                          "G1_abs_dB": G1_abs, "Gchain_abs_dB": Gc_abs,
                          "G4_A_worst": g_chain["cav"]["G_worst1_dB"] / R["cell1"]["cav"]["G_worst1_dB"],
                          "G4_A_mean": g_chain["cav"]["G_mean1_dB"] / R["cell1"]["cav"]["G_mean1_dB"],
                          "G4_A_drnh_worst": g_chain["drn_h"]["G_worst1_dB"] / R["cell1"]["drn_h"]["G_worst1_dB"],
                          "G4_B_mean": Gc_abs / G1_abs,
                          "mean1_in_cell2": kappa * mean1(c1M, "drn_h", 0)}
        R["J"][f"{J}_{plane}"] = ent
    # --- depth extension ---
    R["depth"] = []
    for stage in range(2, 10):
        kMM = f"J{Jp}_h_MM" if stage == 2 else f"J{Jp}_h_stage{stage}_MM"
        if kMM not in F["chains"]: break
        kM0 = kMM.replace("_MM", "_M0"); k00 = kMM.replace("_MM", "_00")
        si = idx(shifts, min(shifts[-1], (stage - 1) * L_rule))
        MM, M0, O0 = F["chains"][kMM], F["chains"][kM0], F["chains"][k00]
        R["depth"].append({"stage": stage, "shift": shifts[si], "chain_over_passive": stage_scores(bits, None, MM, O0, si),
                           "cell_on_real_input": stage_scores(bits, None, MM, M0, si)})
    return R


def fmt(x, n=3):
    return "nan" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x:.{n}f}"


if __name__ == "__main__":
    files = sorted(glob.glob(os.path.join(RUNS, "*.json")))
    out = {}
    for p in files:
        R = analyze_family(p); out[R["tag"]] = R
        c = R["cell1"]["cav"]; L = R["latency"]
        print(f"\n=== {R['tag']}  m={R['m']} N={R['N']} seed={R['seed']} bias={R['bias']:.6f}  [{R['secs']}s]")
        print(f" cell1 cav: G_worst {c['G_worst1_dB']:.4f} G_mean {c['G_mean1_dB']:.4f} pp {c['pp_raw_dB']:.3f} eye {c['eye_dB']:+.2f} floor {c['max0_below_mean1_dB']:.4f} | drn_h floor {R['cell1']['drn_h']['max0_below_mean1_dB']:.4f} mode-floor {R['cell1']['floor_mode_drn_h']:.3f}")
        print(f" latency: env passive {L['env_passive']:.3f} / active {L['env_active']:.3f}; peak passive {L['peak_passive']:.3f} / active {L['peak_active']:.3f} -> rule shift {L['rule_shift']} units = {L['rule_rt']:.3f} rt = {L['rule_ps']:.3f} ps = {L['rule_frac_slot']:.3f} slot")
        for Jk, ent in sorted(R["J"].items(), key=lambda kv: (kv[0].split('_')[1], -int(kv[0].split('_')[0]))):
            e = ent["rule"]; ch = e["chain_over_passive"]; cc = e["cell2_on_real_input"]
            print(f"  J{Jk:>5}: chain/passive cav worst {ch['cav']['G_worst1_dB']:.3f} mean {ch['cav']['G_mean1_dB']:.3f} | G4_A worst {e['G4_A_worst']:.3f} mean {e['G4_A_mean']:.3f} (drn_h {e['G4_A_drnh_worst']:.3f}) G4_B {e['G4_B_mean']:.3f} | c2c cav worst {cc['cav']['G_worst1_dB']:.3f} mean {cc['cav']['G_mean1_dB']:.3f} | in-amp {e['mean1_in_cell2']:.5f} T2pas {e['passive_transfer_stage2_dB']:.2f} T1pas {e['passive_transfer_stage1_dB']:.2f} | st2 floor cav {ch['cav']['max0_below_mean1_dB']:.3f} drn_h {ch['drn_h']['max0_below_mean1_dB']:.3f} mode {ch['floor_mode_drn_h']:.3f} pp {ch['cav']['pp_raw_dB']:.3f} eye {ch['cav']['eye_dB']:+.2f}")
            u = ent["unshifted"]["chain_over_passive"]
            print(f"          unshifted: chain/passive cav worst {u['cav']['G_worst1_dB']:.3f} mean {u['cav']['G_mean1_dB']:.3f} floor cav {u['cav']['max0_below_mean1_dB']:.3f}")
        for d in R["depth"]:
            ch = d["chain_over_passive"]; cc = d["cell_on_real_input"]
            print(f"  stage {d['stage']} (shift {d['shift']}): chain/passive cav worst {ch['cav']['G_worst1_dB']:.3f} mean {ch['cav']['G_mean1_dB']:.3f} | stage-cell c2c worst {cc['cav']['G_worst1_dB']:.3f} mean {cc['cav']['G_mean1_dB']:.3f} | floor cav {ch['cav']['max0_below_mean1_dB']:.3f} drn_h {ch['drn_h']['max0_below_mean1_dB']:.3f} mode {ch['floor_mode_drn_h']:.3f} pp {ch['cav']['pp_raw_dB']:.3f} eye {ch['cav']['eye_dB']:+.2f}")
    json.dump(out, open(os.path.join(SESSION, "analysis.json"), "w"), indent=1)

```

### `analyze_depth.py`

```python
# -*- coding: utf-8 -*-
"""Table 3 from the depth re-run: per-stage gain over the passive twin chain, stage-cell
gain on its real input, '0'-floors (peak cav / peak drn_h / slot-mode drn_h), '1' pp, eye and
latency, under the window rule shift_k = (k-1)*L with L from the passive twin chain
(envelope cross-correlation), plus the unshifted and active-lag variants as sensitivities."""
import sys, os, json, math, glob
import numpy as np
SESSION = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SESSION)
from cascade_driver import metrics, floor_mode, slot_windows, slot_peaks, slot_modes, F0N, RT_PS
from analyze import envelope_lag
D = os.path.join(SESSION, "depth")


def load(tag, st):
    t = np.load(f"{D}/{tag}_{st}_t.npy").astype(float)
    return {"t": t, **{o: np.load(f"{D}/{tag}_{st}_{o}.npy").astype(float) for o in ("cav", "drn_h", "drn_u")}}


def score(cell, ref, bits, repT, nslots, shift):
    """No cap on the shift: a stage-k window may run into the following slot's time (wave
    pipelining). Slots whose shifted window would run past the end of the record are dropped
    (n_scored is reported), so no slot is scored on a truncated window."""
    tend = min(cell["t"][-1], ref["t"][-1])
    n_ok = sum(1 for k in range(nslots) if (k + 0.72) * repT + shift <= tend)
    mk = slot_windows(cell["t"], repT, n_ok, shift=shift); mr = slot_windows(ref["t"], repT, n_ok, shift=shift)
    NANS = {k: float("nan") for k in ("G_worst1_dB", "G_mean1_dB", "pp_raw_dB", "mean1_level", "min1_level", "eye_dB", "max0_below_mean1_dB", "max0_level")}
    if n_ok <= 4 or not np.all(np.isfinite(cell["drn_h"])) or not np.all(np.isfinite(ref["drn_h"])):
        # a record that ended in the solver's blow-up guard (non-finite series) or is too short to score
        return {"cav": dict(NANS), "drn_h": dict(NANS), "floor_mode_drn_h": float("nan"), "n_scored": 0, "note": "not scorable (non-finite or truncated record)"}
    out = {o: metrics(bits[:n_ok], slot_peaks(cell[o], mk), slot_peaks(ref[o], mr)) for o in ("cav", "drn_h")}
    for o in ("cav", "drn_h"):
        for k2, v in NANS.items(): out[o].setdefault(k2, v)
    a, _ = slot_modes(cell["drn_h"], cell["t"], mk, F0N, repT, 0.8, shift=shift)
    out["floor_mode_drn_h"] = floor_mode(bits[:n_ok], a); out["n_scored"] = n_ok - 4
    return out


def run(tag):
    meta = json.load(open(f"{D}/{tag}.json")); bits = meta["bits"]; repT = meta["repT"]; ns = meta["nslots"]
    c1M, c10 = load(tag, "st1_M"), load(tag, "st1_0")
    stages = sorted({int(f.split("_st")[1].split("_")[0]) for f in glob.glob(f"{D}/{tag}_st*_MM_t.npy")})
    st2_00 = load(tag, "st2_00"); st2_MM = load(tag, "st2_MM")
    ds = max(1, len(c10["t"]) // 20000)
    L_pas = envelope_lag(c10["drn_h"][::ds], st2_00["drn_h"][::ds], c10["t"][::ds])
    L_act = envelope_lag(c1M["drn_h"][::ds], st2_MM["drn_h"][::ds], c1M["t"][::ds])
    res = {"tag": tag, "L_passive": L_pas, "L_active": L_act, "stages": {}, "stage_lags": {}}
    # per-stage latencies: stage k-1 -> k on the passive twin chain and on the active chain
    prev0, prevM = c10, c1M
    for k in stages:
        n0 = load(tag, f"st{k}_00"); nM = load(tag, f"st{k}_MM")
        lp = envelope_lag(prev0["drn_h"][::ds], n0["drn_h"][::ds], prev0["t"][::ds]); la = envelope_lag(prevM["drn_h"][::ds], nM["drn_h"][::ds], prevM["t"][::ds])
        pp0 = float(np.median((np.array([np.argmax(np.abs(n0["drn_h"][(n0["t"] >= j * repT) & (n0["t"] < (j + 1) * repT)])) * n0["t"][1] for j in range(ns)]) - np.array([np.argmax(np.abs(prev0["drn_h"][(prev0["t"] >= j * repT) & (prev0["t"] < (j + 1) * repT)])) * prev0["t"][1] for j in range(ns)]))[4:][np.array(bits[4:]) == 1]))
        res["stage_lags"][k] = {"passive_env": lp, "active_env": la, "passive_peak": pp0}
        print(f" stage {k-1}->{k} lag: passive env {lp/2:.3f} rt, peak {pp0/2:.3f} rt; active env {la/2:.3f} rt")
        prev0, prevM = n0, nM
    print(f"=== {tag}: L_passive {L_pas:.3f} units ({L_pas/2:.3f} rt, {L_pas/2*RT_PS:.3f} ps, {L_pas/repT:.3f} slot); L_active {L_act:.3f}")
    s1 = score(c1M, c10, bits, repT, ns, 0.0)
    print(f" stage 1: G_worst {s1['cav']['G_worst1_dB']:.3f} G_mean {s1['cav']['G_mean1_dB']:.3f} floor cav {s1['cav']['max0_below_mean1_dB']:.3f} drn_h {s1['drn_h']['max0_below_mean1_dB']:.3f} mode {s1['floor_mode_drn_h']:.3f} pp {s1['cav']['pp_raw_dB']:.3f} eye {s1['cav']['eye_dB']:+.2f}")
    res["stages"][1] = {"rule": s1}
    for k in stages:
        MM, M0, O0 = load(tag, f"st{k}_MM"), load(tag, f"st{k}_M0"), load(tag, f"st{k}_00")
        ent = {}
        for name, sh in (("rule", (k - 1) * L_pas), ("unshifted", 0.0), ("active_lag", (k - 1) * L_act)):
            g = score(MM, O0, bits, repT, ns, sh); c = score(MM, M0, bits, repT, ns, sh)
            ent[name] = {"shift": sh, "chain_over_passive": g, "cell_on_real_input": c}
        res["stages"][k] = ent
        g = ent["rule"]["chain_over_passive"]; c = ent["rule"]["cell_on_real_input"]
        print(f" stage {k} (shift {ent['rule']['shift']:.2f}): chain/passive worst {g['cav']['G_worst1_dB']:.3f} mean {g['cav']['G_mean1_dB']:.3f} | stage-cell worst {c['cav']['G_worst1_dB']:.3f} mean {c['cav']['G_mean1_dB']:.3f} | floor cav {g['cav']['max0_below_mean1_dB']:.3f} drn_h {g['drn_h']['max0_below_mean1_dB']:.3f} mode {g['floor_mode_drn_h']:.3f} pp {g['cav']['pp_raw_dB']:.3f} eye {g['cav']['eye_dB']:+.2f} | mean1 drn_h {g['drn_h']['mean1_level']:.4f}")
        u = ent["unshifted"]["chain_over_passive"]; a = ent["active_lag"]["chain_over_passive"]
        print(f"          unshifted: worst {u['cav']['G_worst1_dB']:.3f} floor cav {u['cav']['max0_below_mean1_dB']:.3f} eye {u['cav']['eye_dB']:+.2f} | active-lag (shift {ent['active_lag']['shift']:.2f}): worst {a['cav']['G_worst1_dB']:.3f} floor cav {a['cav']['max0_below_mean1_dB']:.3f} eye {a['cav']['eye_dB']:+.2f}")
    return res


if __name__ == "__main__":
    tags = sorted({os.path.basename(p)[:-5] for p in glob.glob(f"{D}/*.json")})
    out = {t: run(t) for t in tags}
    json.dump(out, open(os.path.join(SESSION, "analysis_depth.json"), "w"), indent=1)

```

### `residue.py`

```python
# -*- coding: utf-8 -*-
"""The '0'-slot residue the next cell receives, from the depth re-run's stored cell-1 series
(active drain density h[-1]-1; m = 30 and 28, N = 240, seed 7). Two denominators, both named
wherever a number is quoted:
  (a) the mean-'1' peak inside the PROMOTED window [0.25, 0.72]·repT (the promoted floor
      key's own denominator, so the ratio is comparable with max0_below_mean1_dB);
  (b) the mean-'1' peak inside the SAME sub-window (same phase of the slot).
'0' slots are split into those that follow a '1' (carrying its ring-down) and those that
follow a '0'. Also the '0'-slot energy over the mean '1'-slot energy (whole slot)."""
import numpy as np, json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "depth")
WINDOWS = ((0.25, 0.72, "promoted window"), (0.0, 0.25, "first quarter"), (0.0, 1.0, "whole slot"))


def compute(tag):
    meta = json.load(open(f"{D}/{tag}.json")); bits = np.array(meta["bits"]); repT = meta["repT"]; ns = meta["nslots"]
    t = np.load(f"{D}/{tag}_st1_M_t.npy").astype(float); x = np.load(f"{D}/{tag}_st1_M_drn_h.npy").astype(float)

    def pk(lo, hi):
        return np.array([np.max(np.abs(x[(t >= (k + lo) * repT) & (t < (k + hi) * repT)])) for k in range(ns)])[4:]
    b = bits[4:]; ones = b == 1; zeros = b == 0; prev1 = np.array([bits[k - 1] == 1 for k in range(4, ns)])
    ref_a = float(np.mean(pk(0.25, 0.72)[ones]))
    out = {"tag": tag, "mean1_windowed_peak_a": ref_a, "windows": {}}
    for lo, hi, lbl in WINDOWS:
        p = pk(lo, hi); ref_b = float(np.mean(p[ones]))
        a1 = float(np.max(p[zeros & prev1])); a0 = float(np.max(p[zeros & ~prev1]))
        out["windows"][lbl] = {"lo": lo, "hi": hi, "mean1_same_window_b": ref_b, "after1_peak": a1, "after0_peak": a0,
                               "after1_over_a_dB": 20 * np.log10(a1 / ref_a), "after1_over_b_dB": 20 * np.log10(a1 / ref_b),
                               "after0_over_a_dB": 20 * np.log10(a0 / ref_a), "after0_over_b_dB": 20 * np.log10(a0 / ref_b)}
    e = np.array([np.sum(x[(t >= k * repT) & (t < (k + 1) * repT)] ** 2) for k in range(ns)])[4:]
    out["energy_max_dB"] = float(10 * np.log10(np.max(e[zeros]) / np.mean(e[ones]))); out["energy_median_dB"] = float(10 * np.log10(np.median(e[zeros]) / np.mean(e[ones])))
    return out


if __name__ == "__main__":
    for tag in ("D_N240_m30_s7", "D_N240_m28_s7"):
        r = compute(tag); print(f"{tag}: (a) mean-'1' windowed peak {r['mean1_windowed_peak_a']:.6f}")
        for lbl, w in r["windows"].items():
            print(f"  {lbl:16s} [{w['lo']:.2f}, {w['hi']:.2f}]·repT: '0' after '1' peak {w['after1_peak']:.6f} -> over (a) {w['after1_over_a_dB']:7.2f} dB, over (b) same-window mean-'1' {w['mean1_same_window_b']:.6f}: {w['after1_over_b_dB']:7.2f} dB | '0' after '0': over (a) {w['after0_over_a_dB']:7.2f}, over (b) {w['after0_over_b_dB']:7.2f}")
        print(f"  '0'-slot energy over mean '1'-slot energy: max {r['energy_max_dB']:.2f} dB, median {r['energy_median_dB']:.2f} dB")

```

### `render_tables.py`

```python
# -*- coding: utf-8 -*-
"""Render the reply's tables (GitHub markdown) from analysis.json, analysis_depth.json,
table2.jsonl. Seeds at N = 240 are shown as seed-7 value with the min–max spread over
seeds 7/11/13 in brackets."""
import json, os, glob, math
import numpy as np
S = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(S + "/analysis.json"))
GHZ = {28: 71.4, 30: 66.7}


def fams(m, N):
    return {tag: R for tag, R in A.items() if R["m"] == m and R["N"] == N and not tag.endswith("_Jext")}


def val(R, J, path, sname="rule"):
    e = R["J"].get(f"{J}_h");
    if e is None: return None
    x = e[sname]
    for p in path: x = x[p]
    return x


def cell(m, N, J, path, fmt="{:.3f}", sname="rule"):
    F = fams(m, N)
    if not F: return "—"
    vals = {R["seed"]: val(R, J, path, sname) for R in F.values()}
    if any(v is None for v in vals.values()): return "—"
    v7 = vals.get(7, list(vals.values())[0])
    if len(vals) > 1:
        return fmt.format(v7) + " [" + fmt.format(min(vals.values())) + ", " + fmt.format(max(vals.values())) + "]"
    return fmt.format(v7)


print("### Table 1 — two-cell G4 ratio (chain dB over single-cell dB), density-plane coupling, ratio bias, duty-0.8 gated launch, window rule shift = passive-chain latency\n")
print("Definition A (defended): both chain and single cell over their identical passive twins (the promoted gain convention), `cav` observable, worst-'1' statistic; mean-'1' in the second column. Definition B: absolute drain-density gain over the 2×10⁻³ launch amplitude, mean-'1'. Seed-7 value [min, max over seeds 7/11/13] at N = 240.\n")
print("| m (GHz) | N | J (dB) | G_single worst (dB) | G_chain^A worst (dB) | **G4_A worst** | G4_A mean | G4_A (`drn_h`) | G4_B | chain worst, unshifted window |")
print("|---|---|---|---|---|---|---|---|---|---|")
for N in (240, 480, 720):
    for m in (30, 28):
        F = fams(m, N)
        if not F: continue
        R7 = next((R for R in F.values() if R["seed"] == 7), list(F.values())[0])
        for J in (0, -1, -3, -6):
            if f"{J}_h" not in R7["J"]: continue
            print(f"| {m} ({GHZ[m]}) | {N} | {J:+d} | {cell(m,N,J,['chain_over_passive','cav','G_worst1_dB'],'{:.3f}') if False else R7['cell1']['cav']['G_worst1_dB']:.4f} | {cell(m,N,J,['chain_over_passive','cav','G_worst1_dB'])} | **{cell(m,N,J,['G4_A_worst'])}** | {cell(m,N,J,['G4_A_mean'])} | {cell(m,N,J,['G4_A_drnh_worst'])} | {cell(m,N,J,['G4_B_mean'])} | {cell(m,N,J,['chain_over_passive','cav','G_worst1_dB'],'{:.3f}','unshifted')} |")

print("\n### Table 2a — cell 2 on its real input vs the boundary-driven single cell at the MATCHED amplitude (signed Δ = cell-to-cell − boundary-driven), `cav`, worst-'1' / mean-'1'\n")
T2 = [json.loads(l) for l in open(S + "/table2.jsonl")] if os.path.exists(S + "/table2.jsonl") else []
T2 += [json.loads(l) for l in open(S + "/table2_480m28.jsonl")] if os.path.exists(S + "/table2_480m28.jsonl") else []
print("| m | N | seed | J (dB) | input amp A* (drain density × κ) | c2c worst / mean (dB) | boundary-driven G(A*) worst / mean (dB) | **Δ worst / mean (dB)** | G at 2×10⁻³ (promoted row) |")
print("|---|---|---|---|---|---|---|---|---|")
for r in sorted([r for r in T2 if r["kind"] == "matched"], key=lambda r: (r["N"], -r["m"], r["seed"], -r["J"])):
    R = A.get(r["tag"]);
    if R is None: continue
    e = R["J"].get(f"{r['J']}_h")
    if e is None: continue
    c = e["rule"]["cell2_on_real_input"]["cav"]
    print(f"| {r['m']} | {r['N']} | {r['seed']} | {r['J']:+d} | {r['amp']:.5f} | {c['G_worst1_dB']:.3f} / {c['G_mean1_dB']:.3f} | {r['cav']['G_worst1_dB']:.3f} / {r['cav']['G_mean1_dB']:.3f} | **{c['G_worst1_dB']-r['cav']['G_worst1_dB']:+.3f} / {c['G_mean1_dB']-r['cav']['G_mean1_dB']:+.3f}** | {R['cell1']['cav']['G_worst1_dB']:.4f} |")
print("\n### Table 2b — boundary-driven single-cell gain ladder G(A), same convention (seed 7)\n")
print("| m | N | A | G worst / mean (dB) | floor (dB) | pp (dB) |")
print("|---|---|---|---|---|---|")
lad = [r for r in T2 if r["kind"] == "ladder"]
for r in sorted(lad, key=lambda r: (r["N"], -r["m"], r["amp"])):
    print(f"| {r['m']} | {r['N']} | {r['amp']:.4f} | {r['cav']['G_worst1_dB']:.3f} / {r['cav']['G_mean1_dB']:.3f} | {r['cav']['max0_below_mean1_dB']:.3f} | {r['cav']['pp_raw_dB']:.3f} |")

print("\n### Table 3 — stage by stage (J = −1 dB, density plane, seed 7, N = 240). Window rule: the promoted window delayed by (k − 1) × the passive twin chain's stage-1→2 envelope lag (5.136 units = 2.568 rt at m = 30; 5.111 = 2.556 rt at m = 28), applied exactly and **without a cap**: at stage 5 the delay is 0.34 slot, so the window runs into the following slot's time (the wave-pipelining reading of a cascade); slots whose delayed window would run past the record's end are dropped and the scored count is shown. Columns: gain over the passive twin chain; the stage cell's gain on its real input; '0'-floor in both denominations; '1' pp; eye; the stage's mean-'1' drain density (h − 1; the shallow-water equilibrium is h = 1); and the measured stage-(k − 1)→k latency — on the passive twin chain by envelope cross-correlation and by per-slot peak time, on the active chain by envelope\n")
if os.path.exists(S + "/analysis_depth.json"):
    Dp = json.load(open(S + "/analysis_depth.json"))
    print("| m | stage k | window shift (rt) | slots scored | lag (k − 1)→k: passive env / peak; active env (rt) | chain/passive worst / mean (dB) | stage cell on real input, worst / mean (dB) | floor peak `cav` / `drn_h` (dB) | floor slot-mode `drn_h` (dB) | '1' pp (dB) | eye (dB) | mean-'1' drain density |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    order = sorted(Dp.items(), key=lambda kv: -int(kv[0].split("_m")[1].split("_")[0]))
    for tag, D in order:
        m = int(tag.split("_m")[1].split("_")[0])
        for k, ent in sorted(D["stages"].items(), key=lambda kv: int(kv[0])):
            k = int(k); r = ent["rule"]
            if k == 1:
                g = r; ccell = "—"; sh = 0.0; lag = "—"; n = r.get("n_scored", 36)
            else:
                g = r["chain_over_passive"]; c = r["cell_on_real_input"]; sh = r["shift"]; L = D["stage_lags"][str(k)]
                lag = f"{L['passive_env']/2:.3f} / {L['passive_peak']/2:.3f}; {L['active_env']/2:.3f}"; n = g.get("n_scored")
                ccell = "n/a (record truncated at the solver's blow-up guard: the passive stage-5 twin driven by the active chain)" if c.get("note") else f"{c['cav']['G_worst1_dB']:.3f} / {c['cav']['G_mean1_dB']:.3f}"
            print(f"| {m} | {k} | {sh/2:.2f} | {n} | {lag} | {g['cav']['G_worst1_dB']:.3f} / {g['cav']['G_mean1_dB']:.3f} | {ccell} | {g['cav']['max0_below_mean1_dB']:.2f} / {g['drn_h']['max0_below_mean1_dB']:.2f} | {g['floor_mode_drn_h']:.2f} | {g['cav']['pp_raw_dB']:.3f} | {g['cav']['eye_dB']:+.2f} | {g['drn_h']['mean1_level']:.4f} |")
    print("\n#### Table 3b — window-placement sensitivity of Table 3 (same runs; `cav`, chain over the passive twin chain): the rule above, the unshifted promoted window, and the window delayed by (k − 1) × the *active* chain's stage-1→2 envelope lag (11.42 units = 5.71 rt at m = 30; 11.53 = 5.77 rt at m = 28), also uncapped\n")
    print("| m | stage k | rule shift (rt): worst (dB) / floor `cav` (dB) / eye (dB) | unshifted window: worst / floor / eye | active-lag shift (rt) [slots scored]: worst / floor / eye |")
    print("|---|---|---|---|---|")
    for tag, D in order:
        m = int(tag.split("_m")[1].split("_")[0])
        for k, ent in sorted(D["stages"].items(), key=lambda kv: int(kv[0])):
            if int(k) == 1: continue
            r, u, a = (ent[n]["chain_over_passive"] for n in ("rule", "unshifted", "active_lag"))
            f = lambda g: f"{g['cav']['G_worst1_dB']:.3f} / {g['cav']['max0_below_mean1_dB']:.2f} / {g['cav']['eye_dB']:+.2f}"
            print(f"| {m} | {k} | {ent['rule']['shift']/2:.2f}: {f(r)} | {f(u)} | {ent['active_lag']['shift']/2:.2f} [{a.get('n_scored')}]: {f(a)} |")
    lp = {int(t.split("_m")[1].split("_")[0]): D for t, D in Dp.items()}
    print(f"\nStage-1→2 lags (Table 3 runs): passive envelope {lp[30]['L_passive']:.3f} units ({lp[30]['L_passive']/2:.3f} rt, {lp[30]['L_passive']/2*RT_PS if False else lp[30]['L_passive']/2*0.5:.3f} ps, {lp[30]['L_passive']/60:.3f} slot) at m = 30 and {lp[28]['L_passive']:.3f} ({lp[28]['L_passive']/2:.3f} rt, {lp[28]['L_passive']/2*0.5:.3f} ps, {lp[28]['L_passive']/56:.3f} slot) at m = 28; active {lp[30]['L_active']:.2f} / {lp[28]['L_active']:.2f} units ({lp[30]['L_active']/2:.2f} / {lp[28]['L_active']/2:.2f} rt). The later stages' lags are in the table; they belong to the out-of-regime stages and are not registered.")

print("\n### Junction sweep (primary rungs, N = 240, seed 7): where the chain returns to the small-signal limit\n")
print("| m | J (dB) | κ | input amp to cell 2 | c2c worst / mean (dB) | G4_A worst / mean | stage-2 floor peak `cav` / slot-mode (dB) | eye (dB) |")
print("|---|---|---|---|---|---|---|---|")
for m in (30, 28):
    for tag, R in A.items():
        if R["m"] != m or R["N"] != 240 or R["seed"] != 7: continue
        for J in (0, -1, -3, -6, -10, -15, -20, -25):
            e = R["J"].get(f"{J}_h")
            if e is None: continue
            r = e["rule"]; c = r["cell2_on_real_input"]["cav"]; g = r["chain_over_passive"]
            print(f"| {m} | {J:+d} | {10**(J/20):.4f} | {r['mean1_in_cell2']:.5f} | {c['G_worst1_dB']:.3f} / {c['G_mean1_dB']:.3f} | {r['G4_A_worst']:.3f} / {r['G4_A_mean']:.3f} | {g['cav']['max0_below_mean1_dB']:.2f} / {g['floor_mode_drn_h']:.2f} | {g['cav']['eye_dB']:+.2f} |")

print("\n### Passive port-to-port density transfer and latency\n")
print("| m | N | seed | T_passive stage 1 (dB, drain density over launch) | T_passive stage 2 (dB) | latency passive: peak-time / envelope (rt) | latency active: peak-time / envelope (rt) | rule shift (rt, ps, slot fraction) |")
print("|---|---|---|---|---|---|---|---|")
for tag, R in sorted(A.items(), key=lambda kv: (kv[1]["N"], -kv[1]["m"], kv[1]["seed"], kv[0].endswith("_Jext"))):
    e = next((R["J"][k] for k in ("-1_h", "-3_h", "-10_h") if k in R["J"]), None); L = R["latency"]
    if e is None: continue
    print(f"| {R['m']}{' (junction sweep)' if tag.endswith('_Jext') else ''} | {R['N']} | {R['seed']} | {e['rule']['passive_transfer_stage1_dB']:.2f} | {e['rule']['passive_transfer_stage2_dB']:.2f} | {L['peak_passive']/2:.3f} / {L['env_passive']/2:.3f} | {L['peak_active']/2:.3f} / {L['env_active']/2:.3f} | {L['rule_rt']:.3f} rt, {L['rule_ps']:.3f} ps, {L['rule_frac_slot']:.3f} |")


print("\n### Residue — what the next cell actually receives (cell 1's active drain density h[−1] − 1, seed 7, N = 240; a '0' slot that follows a '1' carries that '1's ring-down, one that follows a '0' does not). Denominators, named per column: **(a)** = the mean-'1' peak inside the promoted window [0.25, 0.72]·repT, the promoted floor key's own denominator; **(b)** = the mean-'1' peak inside the same sub-window (same phase of the slot, where the '1' is still ringing up). Computed by `residue.py`\n")
import residue as RS
print("| m | promoted window [0.25, 0.72]·repT, over (a) | first quarter [0, 0.25]·repT, over (a) | first quarter, over (b) | whole slot, over (a) | whole slot, over (b) | '0'-slot energy over mean '1'-slot energy (max / median) | cell 2's windowed stage-2 floor at J = −1, `drn_h` / `cav` (Table 5) |")
print("|---|---|---|---|---|---|---|---|")
for tag in ("D_N240_m30_s7", "D_N240_m28_s7"):
    r = RS.compute(tag); m = int(tag.split("_m")[1].split("_")[0]); W = r["windows"]
    fl = next(R for t, R in A.items() if R["m"] == m and R["N"] == 240 and R["seed"] == 7 and not t.endswith("_Jext"))["J"]["-1_h"]["rule"]["chain_over_passive"]
    q = W["first quarter"]; w = W["whole slot"]; pw = W["promoted window"]
    print(f"| {m} | {pw['after1_over_a_dB']:.2f} dB (after a '1'); {pw['after0_over_a_dB']:.1f} (after a '0') | **{q['after1_over_a_dB']:.2f} dB**; {q['after0_over_a_dB']:.1f} | {q['after1_over_b_dB']:.2f} dB; {q['after0_over_b_dB']:.1f} | {w['after1_over_a_dB']:.2f} dB; {w['after0_over_a_dB']:.1f} | {w['after1_over_b_dB']:.2f} dB; {w['after0_over_b_dB']:.1f} | {r['energy_max_dB']:.1f} / {r['energy_median_dB']:.1f} dB | {fl['drn_h']['max0_below_mean1_dB']:.2f} / {fl['cav']['max0_below_mean1_dB']:.2f} dB |")
print("\nThe first-quarter and whole-slot columns agree under denominator (a) because the '0' slot's un-windowed maximum sits at ≈ 0.01 slot, inside the first quarter; the registered key `zero_slot_residue_unwindowed_dB` is the bold column.")

# ---------------- per-table files for the finalizer ----------------
import io, contextlib
def capture(fn):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn()
    return buf.getvalue()

def table5():
    print("| m | N | seed | J (dB) | stage-2 floor, peak `cav` (dB) | peak `drn_h` (dB) | slot-mode `drn_h` (dB) | '1' pp (dB) | eye (dB) | cell-1 floor peak `cav` / slot-mode (dB) |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for tag, R in sorted(A.items(), key=lambda kv: (kv[1]["N"], -kv[1]["m"], kv[1]["seed"], kv[0].endswith("_Jext"))):
        for Jk, ent in sorted(R["J"].items(), key=lambda kv: -int(kv[0].split("_")[0])):
            J, plane = Jk.split("_")
            if plane != "h": continue
            g = ent["rule"]["chain_over_passive"]
            print(f"| {R['m']} | {R['N']} | {R['seed']} | {int(J):+d} | {g['cav']['max0_below_mean1_dB']:.2f} | {g['drn_h']['max0_below_mean1_dB']:.2f} | {g['floor_mode_drn_h']:.2f} | {g['cav']['pp_raw_dB']:.3f} | {g['cav']['eye_dB']:+.2f} | {R['cell1']['cav']['max0_below_mean1_dB']:.2f} / {R['cell1']['floor_mode_drn_h']:.2f} |")

full = open(S + "/tables.md").read() if os.path.exists(S + "/tables.md") else ""

```
