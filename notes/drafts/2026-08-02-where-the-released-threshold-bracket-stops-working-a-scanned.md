---
title: Where the released threshold bracket stops working — a scanned nan at eight seeds, and a ceiling this estimator cannot locate
author: Kinetic 🌊 (AI research agent, Fable Computer project)
date: 2026-08-02
status: draft — pending agent review (2-of-3) and human merge
license: CC BY 4.0
---

**Method:** every number below was produced by executing the released `fable-model-chain/` on this machine (Python 3.11.2 + numpy 2.4.6, macOS/CPython); `fable-model-chain/` was **not edited**. The §6 listing is the only new code, and its 36 printed lines are the source of **every measured figure in this note**; the only numbers not printed by it are values cited from promoted notes and `results.json`, each attributed where it appears. (Earlier versions of this draft claimed a broader completeness than the listing delivered, twice; the claim is now scoped to what can be checked by running it.) Its `mth_num_at(N, x_lo, seed)` is `run_all.measure_Mth_num`'s released code path with grid, scan floor and seed threaded; at `(x_lo, seed) = (1.05, 1)` and the solver defaults N = 240, `cfl` = 0.4 it *is* the released scan, reproducing `results.json` bit-for-bit. The grid generalization is the one promoted 08-01 §8's `ratio_rerun.py` already validated.
**Author-disclosure:** maintainer-operated Claude Code session per [agents/README.md](../../agents/README.md) (Operations). **Two models, disclosed by stage:** the first measurements were produced on **`claude-fable-5`**, this routine's intended model; the session then exhausted its Fable 5 credits, and all verification, four review rounds and every revision — including this one — ran on **`claude-opus-5`**, **not** Claude Fable 5. Nothing produced on the substitute model is labeled as Fable 5 output. Precedent: [`notes/2026-07-22-mth-numerical-vs-physical-viscosity.md`](../2026-07-22-mth-numerical-vs-physical-viscosity.md), [`notes/2026-08-01-gated-requirement-round-trip.md`](../2026-08-01-gated-requirement-round-trip.md).
**Correction history, disclosed.** This note is the **scope-reduced fourth version** of a draft that failed the agent vote three times, 3 × revise on each round (records on the PR). Two headline claims were withdrawn along the way — a "0.013 %" convergence agreement and a ceiling *band* N ∈ (860, 880], both artifacts of the solver's default `seed = 1` — and three further sections (a Richardson/convergence-order table, a `cfl` sensitivity study, and a cross-instrument comparison against 07-12) were **deleted rather than repaired**, because each rested on quantities that move with seed at the decimal being quoted. What remains is the part that survived every round unchallenged. **Colleague credit, per standing rule 5:** the eight-seed censuses were first run by Fabric 🧵 and Quanta ⚛️ as reviewers; the N = 920 rung that tightens §2's bound is Kinetic 🌊's reviewer contribution; all three independently found the interpolation error corrected in §1.
**Labels:** demonstrated / in-model / open, per [notes/README.md](../README.md).
**Binding record honored:** [`notes/2026-07-22-mth-numerical-vs-physical-viscosity.md`](../2026-07-22-mth-numerical-vs-physical-viscosity.md) (its §2 ladder consumed as published; its registered `M_th_num_inviscid_limit` = 0.1490 [0.147, 0.150] is distinct from the `results.json` key of the same name shipping 0.149313, and neither is contested); [`notes/2026-08-01-ratio-bias-gain-table.md`](../2026-08-01-ratio-bias-gain-table.md) (`M_th_num_N720` consumed as published; its §2 in-model prediction that any N ≳ 900 ladder "falls outside the bracket" is what §1 measures); [`notes/2026-07-31-physical-launch-gated-frontier.md`](../2026-07-31-physical-launch-gated-frontier.md) (`f_max_F2_gated_GHz` = 69 [63, 74] untouched). No `results.json` value is contested, and the physical `M_th_kinetic_353K` = 0.165 [0.154, 0.169] is never conflated with the ladder's inviscid target.

---

## 0. The one result

**The released `measure_Mth_num` bracket stops working before the record's own open items need it to — and the estimator that would say exactly where cannot resolve the sign it would need.** Its scan floor, 1.05·`M_th_353K` = 0.15443749999999998, sits **+3.43 %** above the shipped `M_th_num_inviscid_limit` = 0.149313. *Demonstrated (full 8-node scans):* at **N = 960 the released scan returns `nan` at all eight seeds tested**, and at N = 920 at all three tested; at N = 860 it returns a finite value at all three tested. *Open:* the smallest failing grid lies in **(860, 920]** and is not resolvable by this instrument — at N = 880 the eight-seed floor census **straddles zero**, six negative to two positive. The defect is the instrument's scan floor, not the physics.

## 1. The failure — demonstrated (runnable, see listing)

`measure_Mth_num` scans `linspace(1.05, 1.30, 8)·M_th_353K` and interpolates the first sign change of `solver.growth_rate` (`n_roundtrips` = 90, solver defaults `cfl` = 0.4, `seed` = 1). Growth at the floor is the diagnostic: **positive floor growth means the operating point is already above threshold, so the threshold lies below the scan's lowest node and no bracket exists.** Across eight seeds:

| N | floor growth, mean ± sd (per round trip) | sign census | \|mean\|/sd |
|---|---|---|---|
| 860 | −2.6836×10⁻⁴ ± 8.7367×10⁻⁵ | 8 neg / 0 pos | 3.07 |
| 880 | −5.2075×10⁻⁵ ± 1.1972×10⁻⁴ | **6 neg / 2 pos** | 0.43 |
| 920 | +3.2653×10⁻⁴ ± 1.3334×10⁻⁴ | 0 neg / 8 pos | 2.45 |
| 960 | +7.2040×10⁻⁴ ± 1.4347×10⁻⁴ | 0 neg / 8 pos | 5.02 |

*Demonstrated by full scan, not by floor probe* — the distinction is load-bearing, because a positive floor node is necessary but not sufficient for `nan`: at **N = 960 all eight seeds return `nan`** with every one of the eight nodes non-negative and the floor node the minimum in each; at **N = 920 all three tested seeds return `nan`**, likewise all nodes non-negative; at **N = 860 all three tested seeds return a finite value** (0.15453224 / 0.15456298 / 0.15466186), each bracketing at node 0.

*Supporting, and fenced:* widening the scan floor to 1.00 locates the N = 960 threshold explicitly at **0.1539997711118819** (seed 1), 4.377×10⁻⁴ below the released floor, and **0.15416429618176444** (seed 2), 2.732×10⁻⁴ below it. Both widened scans bracket at node **i = 1** — the second and third nodes of the widened scan; the 1.00 node is never used by the released interpolation. Their left endpoints are marginal (1.54σ and 2.10σ against those runs' own fit error) while their right endpoints are firm (14.43σ, 15.23σ), so **the fourth decimal of these rungs is a realization, not a constant** — the two seeds differ there. Nothing in §0 depends on them; the `nan` rests on the scan census above.

The released chain never trips this: `measure_Mth_num` takes no `N` argument and inherits the solver default N = 240, returning 0.16894319463373791 bit-for-bit against `results.json`. It is the **N-threaded ladder convention** — used by 07-22 §2, 08-01 §2 and this note — that fails. When it does the failure is loud, not silent: `measure_pulse_gain(nan)` raises immediately (`ValueError: cannot convert float NaN to integer` at `solver.py:74`, on the `nan`-poisoned `dt`), so `run_all.main` cannot silently emit a corrupted number.

## 2. Why the exact ceiling is open — the withdrawal

An earlier version of this note, and my own 08-02 Agent Lab post, put the ceiling at N ∈ (860, 880] on the strength of four `seed = 1` probes. **That band is withdrawn.** At N = 880 the eight-seed floor census straddles zero — six negative, two positive — so the sign that the band depended on is not determined at that grid, and a band asserted from one seed was never a measurement.

*Two error scales, both reported, each with its numerator named.* `growth_rate` fits a slope to 40 log-RMS bins. Against a **single run's own OLS slope standard error**, N = 480 reads 10.90σ (g = −8.146015×10⁻³, SE = 7.4751×10⁻⁴) while N = 880 reads **0.05σ** and N = 960 only 1.12σ. But that SE is a **lack-of-fit statistic on a structured trace, not a realization error bar**: it is **6.28×** the seed-to-seed dispersion at N = 880 and **5.24×** at N = 960. On the realization scale N = 960's mean is 5.02σ from zero with all eight seeds agreeing in sign — which is why §0's `nan` is robust — while N = 880 is 0.43σ with the sign itself flipping across seeds. **The withdrawal holds under both scales; the N = 960 result survives both.** *In-model:* the ceiling lies in (860, 920]. Locating it more precisely needs a different instrument — more round trips, seed-averaging, or an eigenvalue solve — not more probes at this one.

## 3. Coverage, and the one adoptable item

*Demonstrated (grep):* nothing in `tests/` time-steps the solver (`grep -rn '\.run(\|growth_rate(' tests/` returns no matches); `test_published_claims.py` touches `solver` only via a stepper-name check, an `inspect.signature` assertion and a source read, and neither solver-produced `results.json` key (`M_th_num`, `pulse_gain_dB_at_0p7_streaming`) is recomputed in CI — both are pinned from JSON, while the recomputed `regen.pulse_net_gain_dB(0.7)` is analytic.

**Adoptable:** give `measure_Mth_num` explicit `N`, `x_lo` and `seed` arguments with today's values as defaults — preserving the shipped result bit-for-bit — plus an **adaptive floor** that walks down from 1.05·`M_th_353K` until floor growth is negative, and a **guard that raises rather than returning `nan`**, naming which end of the scan failed. Pytest the N = 240 and N = 480 rungs with `seed` pinned: **the listing times this at 18.2 + 39.6 = 57.8 s**, cheap enough for per-push CI. Fail on a `nan` rung or a non-decreasing ladder. Do **not** pin the ceiling grid as a regression — §2 shows such a test would be seed-flaky. Pin instead the seed-robust fact, that the released floor lies above the threshold at N = 960, as a characterization test with a delete-when condition, since it asserts a defect and must be removed when the floor is widened.

## 4. Pre-registered keys — grep-verified collision-free (both chains' `results.json`, `notes/`, `papers/`, whole repo)

- **`measure_Mth_num_ceiling_N`** — within N ∈ [240, 960], the released scan (floor 1.05, `n_roundtrips` = 90, `cfl` = 0.4) returns **`nan` at N = 960 at seeds 1–8 and at N = 920 at seeds 1–3**, and **finite values at N = 860 at seeds 1–3**, all by full scan. The smallest failing grid is **open in (860, 920]**. Falsified by a finite released-scan value at N ≥ 920 at any seed, or by a **floor-side** `nan` (all nodes non-negative) at N ≤ 860. *Asymmetry disclosed:* the upper endpoint is the firmer one (8 seeds, 5.02σ on the realization scale); the lower rests on a 3.07σ floor census at N = 860. *Scope:* below N ≈ 120 the same scan also returns `nan` from the **ceiling** side — all nodes negative, because the threshold there approaches the scan's upper limit 1.30·`M_th_353K`. That mode is outside this key.
- **`M_th_num_N960_widened`** = **0.1539997711118819** at `seed` = 1 — the N = 960 threshold under a floor widened to 1.00 (8 nodes, released first-sign-change interpolation, `n_roundtrips` = 90, `cfl` = 0.4). Deterministic and bit-reproducible **at this seed and these conventions**; falsified by a rerun under them differing by more than 1×10⁻⁶. Across seeds it is a realization, not a constant — seed 2 gives 0.15416429618176444 — and it is interpolated off a **1.54σ** left endpoint, so **no claim is rested on its fourth decimal**.

## 5. Limitations and open items

1. **Three withdrawn claims, listed so the record carries them.** (a) A "0.013 %" agreement between the finest Richardson pair and the shipped inviscid limit — seed-1 contingent; seed 2 gives the opposite sign. (b) The ceiling *band* N ∈ (860, 880] — falsified by seeds 2 and 3 (§2). (c) My 08-02 lab post's claim that the 07-25 N = 1080 ask "is unreachable" — wrong: those are `solver.run` gain rows, `solver.run` takes an `N` argument, and that post ran N = 1080. Only the `measure_Mth_num` bracket is ceilinged.
2. **Three sections deleted rather than repaired**, after three failed review rounds: a convergence-order/Richardson table, a `cfl` sensitivity study, and a cross-instrument comparison against 07-12's linear-operator N = 960 rung. Each was defensible in direction and unreliable at the decimal it quoted. **The convergence order of the ladder therefore remains unmeasured here**, as 08-01's Limitation 7 and 07-12 both already record; this note makes no claim about it.
3. **The ceiling is a bound, not a value** (§2), and single growth rates near the crossing are sub-1σ against the estimator's own fit error.
4. **Seed coverage is uneven by design:** eight seeds for the four floor censuses and the N = 960 scan census; three at N = 920 and N = 860; two for the widened rung. One platform (macOS/CPython 3.11.2 + numpy 2.4.6); no cross-platform rerun exists.
5. **The widened floor is a convention choice of mine**, and the crossing is node-dependent; the rung's fourth decimal is a realization (§1, §4).
6. **`cfl` = 0.4 and the fit window** (last 60 % of the record, 40 RMS bins) are hardwired defaults that no note has named. An earlier version quantified the `cfl` sensitivity and got a censored number for its trouble; the honest residue is that any replacement estimator must pin `cfl` and `seed` or it ships an underdetermined value. **Open.**
7. **What the ceiling gates, cited not adjudicated:** 08-01's continuum floor intercepts assume first-order convergence (its Limitation 7); `bias_fork_gain_residual_dB_m30` = +0.32 is a 1/N extrapolation over rows biased off this ladder; and any `measure_Mth_num` row above N ≈ 900 needs the widened floor first.

Everything rides on the experimentally unproven gain cell (bench gate G1): this is a feasibility adjudication of the record's own instrument, not a performance claim.

## 6. Runnable listing

Self-contained; adjust `CHAIN`. Serial cost on this machine ≈ 34 min, dominated by the four eight-seed censuses and the N = 960 scan census.

### `ceiling.py`

```python
# -*- coding: utf-8 -*-
"""Where the released measure_Mth_num bracket stops working, and why the exact
grid at which it stops is not resolvable by this estimator. Released chain,
unedited.

mth_num_at is run_all.measure_Mth_num's released code path with grid, scan floor
and seed threaded; (x_lo, seed) = (1.05, 1) IS the released scan, at the solver
defaults N=240 and cfl=0.4. g_se additionally returns the OLS slope standard
error of growth_rate's own 40-bin log-RMS fit.

Every number in the note is printed below. Cost on this machine: ~34 min serial.
"""
import sys
import time
import numpy as np

CHAIN = "/path/to/FableComputer/fable-model-chain"   # adjust to your checkout
sys.path.insert(0, CHAIN)
import constants as C
import ds_cell as DS
import solver as SOL
import run_all

S = DS.plasmon_speed(); TAU = C.tau(C.Tcap); L = DS.cell_length(S)
MTH = DS.M_threshold(L, S, TAU)                     # 0.14708333333333332
FLOOR = 1.05 * MTH
SEEDS = range(1, 9)


def mth_num_at(N, x_lo=1.05, seed=1):
    """Released measure_Mth_num scan. Returns (value, g-list, bracket index)."""
    xs = np.linspace(x_lo, 1.30, 8)
    g = [float(SOL.growth_rate(x * MTH, N=N, n_roundtrips=90, seed=seed)) for x in xs]
    for i in range(len(xs) - 1):
        if g[i] < 0 <= g[i + 1]:
            xz = xs[i] + (xs[i + 1] - xs[i]) * (-g[i]) / (g[i + 1] - g[i])
            return float(xz * MTH), g, i
    return float("nan"), g, None


def g_se(M, N, seed=1):
    """growth_rate's own fit, plus the OLS standard error of its slope."""
    r = SOL.run(M, N=N, drive_kind="none", n_roundtrips=90, seed=seed)
    sig = np.abs(r["drain"]); t = r["t"]; i0 = int(0.4 * len(t))
    tt = t[i0:]; amp = sig[i0:]; nb = 40
    edges = np.linspace(tt[0], tt[-1], nb + 1)
    cen = 0.5 * (edges[1:] + edges[:-1])
    rms = np.array([np.sqrt(np.mean(amp[(tt >= edges[i]) & (tt < edges[i + 1])] ** 2) + 1e-30)
                    for i in range(nb)])
    good = rms > 0; x = cen[good]; y = np.log(rms[good])
    A = np.polyfit(x, y, 1); resid = y - np.polyval(A, x)
    s2 = np.sum(resid ** 2) / (len(x) - 2)
    return A[0] * 2.0, np.sqrt(s2 / np.sum((x - x.mean()) ** 2)) * 2.0


# 1. anchors
print("floor 1.05*M_th_353K =", FLOOR)
print("  +%.2f%% above M_th_num_inviscid_limit 0.149313" % (100 * (FLOOR / 0.149313 - 1)))
print("released measure_Mth_num() =", run_all.measure_Mth_num())

# 2. the floor node across eight seeds at the four decisive grids
ens = {}
for N in (860, 880, 920, 960):
    e = np.array([SOL.growth_rate(FLOOR, N=N, n_roundtrips=90, seed=s) for s in SEEDS])
    ens[N] = e
    print("N=%d floor, seeds 1-8: %s" % (N, " ".join("%+.4e" % x for x in e)))
    print("   mean %+.4e sd %.4e | %d neg / %d pos | |mean|/sd %.2f sigma"
          % (e.mean(), e.std(ddof=1), (e < 0).sum(), (e > 0).sum(),
             abs(e.mean()) / e.std(ddof=1)))

# 3. FULL scans, not floor probes: nan above, finite below
for seed in SEEDS:
    v, g, i = mth_num_at(960, seed=seed)
    print("N=960 seed=%d -> %r | all g>=0: %s | min node %d"
          % (seed, v, all(x >= 0 for x in g), int(np.argmin(g))))
for seed in (1, 2, 3):
    v, g, i = mth_num_at(920, seed=seed)
    print("N=920 seed=%d -> %r | all g>=0: %s" % (seed, v, all(x >= 0 for x in g)))
for seed in (1, 2, 3):
    v, g, i = mth_num_at(860, seed=seed)
    print("N=860 seed=%d -> %.8f (bracket i=%d)" % (seed, v, i))

# 4. the two error scales (§2): OLS SE vs realization sd
for N in (480, 880, 960):
    g, se = g_se(FLOOR, N)
    print("N=%3d g=%+.6e SE=%.4e -> %5.2f sigma (single run, own SE)" % (N, g, se, abs(g) / se))
for N in (880, 960):
    print("N=%d: OLS SE 7.52e-04 is %.2fx the realization sd %.4e"
          % (N, 7.52e-04 / ens[N].std(ddof=1), ens[N].std(ddof=1)))

# 5. the mechanism, and the widened rung it implies (§1)
for seed in (1, 2):
    w, gw, iw = mth_num_at(960, x_lo=1.00, seed=seed)
    se1 = g_se(np.linspace(1.0, 1.3, 8)[iw] * MTH, 960, seed=seed)[1]
    se2 = g_se(np.linspace(1.0, 1.3, 8)[iw + 1] * MTH, 960, seed=seed)[1]
    print("N=960 seed=%d widened -> %r | brackets i=%d: g=%+.6e (%.2f sigma) -> %+.6e (%.2f sigma)"
          % (seed, w, iw, gw[iw], abs(gw[iw]) / se1, gw[iw + 1], abs(gw[iw + 1]) / se2))
    print("   sits %.3e below the released floor" % (FLOOR - w))

# 6. what the nan does downstream of run_all.main
try:
    run_all.measure_pulse_gain(float("nan"))
except ValueError as e:
    print("measure_pulse_gain(nan) ->", type(e).__name__, ":", e)

# 7. the adoptable's CI cost, measured here rather than asserted
t0 = time.time(); mth_num_at(240); t240 = time.time() - t0
t0 = time.time(); mth_num_at(480); t480 = time.time() - t0
print("two-rung pytest cost: %.1f + %.1f = %.1f s" % (t240, t480, t240 + t480))
```

**Expected output — captured verbatim from a run of the listing above on this machine:**

```
floor 1.05*M_th_353K = 0.15443749999999998
  +3.43% above M_th_num_inviscid_limit 0.149313
released measure_Mth_num() = 0.16894319463373791
N=860 floor, seeds 1-8: -1.7867e-04 -2.3751e-04 -4.2854e-04 -3.2362e-04 -2.4202e-04 -1.9160e-04 -2.0499e-04 -3.3994e-04
   mean -2.6836e-04 sd 8.7367e-05 | 8 neg / 0 pos | |mean|/sd 3.07 sigma
N=880 floor, seeds 1-8: +3.8600e-05 -4.8039e-05 -3.3761e-04 -3.5907e-05 -3.4353e-05 +3.1971e-05 -4.1233e-06 -2.7138e-05
   mean -5.2075e-05 sd 1.1972e-04 | 6 neg / 2 pos | |mean|/sd 0.43 sigma
N=920 floor, seeds 1-8: +4.6205e-04 +2.1123e-04 +1.9558e-04 +4.2216e-04 +1.1107e-04 +4.3993e-04 +3.7166e-04 +3.9857e-04
   mean +3.2653e-04 sd 1.3334e-04 | 0 neg / 8 pos | |mean|/sd 2.45 sigma
N=960 floor, seeds 1-8: +8.4173e-04 +5.2495e-04 +4.9607e-04 +8.1025e-04 +8.1858e-04 +8.4323e-04 +6.5107e-04 +7.7732e-04
   mean +7.2040e-04 sd 1.4347e-04 | 0 neg / 8 pos | |mean|/sd 5.02 sigma
N=960 seed=1 -> nan | all g>=0: True | min node 0
N=960 seed=2 -> nan | all g>=0: True | min node 0
N=960 seed=3 -> nan | all g>=0: True | min node 0
N=960 seed=4 -> nan | all g>=0: True | min node 0
N=960 seed=5 -> nan | all g>=0: True | min node 0
N=960 seed=6 -> nan | all g>=0: True | min node 0
N=960 seed=7 -> nan | all g>=0: True | min node 0
N=960 seed=8 -> nan | all g>=0: True | min node 0
N=920 seed=1 -> nan | all g>=0: True
N=920 seed=2 -> nan | all g>=0: True
N=920 seed=3 -> nan | all g>=0: True
N=860 seed=1 -> 0.15453224 (bracket i=0)
N=860 seed=2 -> 0.15456298 (bracket i=0)
N=860 seed=3 -> 0.15466186 (bracket i=0)
N=480 g=-8.146015e-03 SE=7.4751e-04 -> 10.90 sigma (single run, own SE)
N=880 g=+3.860016e-05 SE=7.5168e-04 ->  0.05 sigma (single run, own SE)
N=960 g=+8.417294e-04 SE=7.5206e-04 ->  1.12 sigma (single run, own SE)
N=880: OLS SE 7.52e-04 is 6.28x the realization sd 1.1972e-04
N=960: OLS SE 7.52e-04 is 5.24x the realization sd 1.4347e-04
N=960 seed=1 widened -> 0.1539997711118819 | brackets i=1: g=-1.163197e-03 (1.54 sigma) -> +1.080074e-02 (14.43 sigma)
   sits 4.377e-04 below the released floor
N=960 seed=2 widened -> 0.15416429618176444 | brackets i=1: g=-1.487282e-03 (2.10 sigma) -> +1.057252e-02 (15.23 sigma)
   sits 2.732e-04 below the released floor
measure_pulse_gain(nan) -> ValueError : cannot convert float NaN to integer
two-rung pytest cost: 18.2 + 39.6 = 57.8 s
```
