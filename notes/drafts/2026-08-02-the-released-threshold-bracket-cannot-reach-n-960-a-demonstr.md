---
title: The released threshold bracket cannot reach N = 960 — a demonstrated nan at eight seeds, a widened fourth rung off a marginal endpoint, and why the exact ceiling is not resolvable by this instrument
author: Kinetic 🌊 (AI research agent, Fable Computer project)
date: 2026-08-02
status: draft — pending agent review (2-of-3) and human merge
license: CC BY 4.0
---

**Method:** every demonstrated number was produced by executing the released `fable-model-chain/` on this machine (Python 3.11.2 + numpy 2.4.6, macOS/CPython); `fable-model-chain/` was **not edited**. The §9 listing is the only new code; its `mth_num_at(N, x_lo, seed, cfl)` is the released `measure_Mth_num` code path with grid, scan floor, seed and CFL as arguments — the grid generalization is the one the promoted 08-01 §8 `ratio_rerun.py` already validated; the other three are this note's, and are named because §2 and §5 show they are load-bearing.
**Author-disclosure:** maintainer-operated Claude Code session per [agents/README.md](../../agents/README.md) (Operations). **Two models, disclosed by stage:** the measurement passes and the first draft were produced on **`claude-fable-5`**, this routine's intended model; the session then exhausted its Fable 5 credits, and the adversarial verification, the round-1 review vote, every re-measurement they forced, and this round-2 revision ran on **`claude-opus-5`** — **not** Claude Fable 5. Nothing produced on the substitute model is labeled or represented as Fable 5 output. This follows the substitution-disclosure precedent of [`notes/2026-07-22-mth-numerical-vs-physical-viscosity.md`](../2026-07-22-mth-numerical-vs-physical-viscosity.md) and [`notes/2026-08-01-gated-requirement-round-trip.md`](../2026-08-01-gated-requirement-round-trip.md).
**Two rounds of correction, disclosed — the first killed a headline, the second killed a supporting sentence.**
*Before the PR opened:* three blind adversarial lenses ran. The **first draft's headline was refuted and withdrawn** — it claimed the ladder confirms the inviscid limit "to 0.013 %" and pinned the scan's failure to N ∈ (860, 880]. Both rest on the solver's default `seed = 1`; at seeds 2 and 3 the band is falsified by its own stated falsifier and the 0.013 % becomes +0.419 %.
*Round 1 of the agent vote (3 × revise, 0 accept — records appended to this PR):* all three reviewers independently found that §1's replacement sentence **misdescribed the code's own interpolation** — it named bracket endpoints at multiplier 1.00 that the released first-sign-change logic never touches. Corrected in §1 below: the widened bracket closes on a **1.5–2.1σ** left endpoint, so the fourth rung is interpolated off a marginal node by this note's own criterion. Two registered keys were also falsified directly and are re-registered in §7. Every round-1 finding was re-executed against the released chain before being accepted; §8 items 1–3 itemise the corrections, and the headline **strengthened** under review (from two seeds to eight).
**Labels:** demonstrated / in-model / open, per [notes/README.md](../README.md).
**Binding record honored:** [`notes/2026-07-22-mth-numerical-vs-physical-viscosity.md`](../2026-07-22-mth-numerical-vs-physical-viscosity.md) (its §2 ladder consumed as published; its §7 key `M_th_num_inviscid_limit` = 0.1490 band [0.147, 0.150] — distinct from the `results.json` key of the same name shipping 0.149313 — and the 0.15239 arithmetic in its appended vote record, diagnosed in §4, not contested); [`notes/2026-08-01-ratio-bias-gain-table.md`](../2026-08-01-ratio-bias-gain-table.md) (`M_th_num_N720` = 0.15556838465677247 consumed as published; its §2 in-model prediction that any N ≳ 900 ladder falls outside the bracket is what §1 measures); [`notes/2026-07-12-boundary-factor-exact-operator.md`](../2026-07-12-boundary-factor-exact-operator.md) (its **linear-operator** N = 960 rung `M_th,lin`(960) = 0.154024 and its recorded local exponents 0.76–0.88); [`notes/2026-07-31-physical-launch-gated-frontier.md`](../2026-07-31-physical-launch-gated-frontier.md) (`f_max_F2_gated_GHz` = 69 [63, 74] untouched). No `results.json` value is contested; the physical `M_th_kinetic_353K` = 0.165 [0.154, 0.169] is never conflated with the ladder's inviscid target.

---

## 0. The one result

**The released `measure_Mth_num` bracket runs out before the record's open items do — and the instrument that would say exactly where cannot sign its own output there.** Its scan floor, 1.05·`M_th_353K` = 0.15443749999999998, sits **+3.43 %** above the shipped `M_th_num_inviscid_limit` = 0.149313. *Demonstrated:* at **N = 960 the released scan returns `nan` at all eight seeds tested** — every one of its eight nodes non-negative in every run — with floor growth positive at each (mean +7.20×10⁻⁴, sd 1.43×10⁻⁴ over seeds 1–8). *Demonstrated:* at N = 860 it returns a finite value at all three seeds tested. *Open, and newly so:* the smallest failing grid is **not** resolvable by this instrument — it lies in (860, 960], and no tighter statement survives a seed change. *In-model:* the mechanism, that the threshold has fallen below the floor, rests on the same sign-of-growth reading §2 shows the estimator cannot resolve near the crossing; the **`nan` itself is deterministic and is the demonstrated half.** The defect is the instrument, not the physics — the ladder still moves away from the physical 0.165 at every seed.

## 1. The failure at N = 960 — demonstrated (runnable, see listing)

`measure_Mth_num` scans `linspace(1.05, 1.30, 8)·M_th_353K` and interpolates the first sign change of `solver.growth_rate` (`n_roundtrips` = 90, and — §5 — `cfl` = 0.4, `seed` = 1). At N = 960 the released scan finds no bracket at any seed tested: growth at the floor is positive in all eight runs (+8.42, +5.25, +4.96, +8.10, +8.19, +8.43, +6.51, +7.77, all ×10⁻⁴, seeds 1–8), with all eight nodes non-negative. Under a widened floor the threshold is located below it:

| seed | released scan (floor 1.05) | widened rung (floor 1.00) | below the floor by |
|---|---|---|---|
| 1 | `nan` | 0.1539997711118819 | 4.38×10⁻⁴ |
| 2 | `nan` | 0.15416429618176444 | 2.73×10⁻⁴ |

**What closes the widened bracket, stated exactly** (this is the sentence round 1 corrected). The widened nodes are 1.000000, 1.042857, 1.085714, …, and the released first-sign-change rule brackets at **i = 1** — between x = 1.0428571 and x = 1.0857143. The x = 1.00 node, where growth is a large −1.32×10⁻² / −1.35×10⁻², is **never used by the interpolation**. The endpoints that are used are `g` = **−1.163×10⁻³ (1.54σ)** and −1.487×10⁻³ (2.10σ) on the left, against +1.080×10⁻² / +1.057×10⁻² (≈14σ) on the right. *Open:* **the fourth rung is therefore interpolated off a marginally-signed left endpoint by this note's own §2 criterion**, and its fourth decimal inherits that. The `nan` conclusion does **not** depend on it: it rests on `g`(floor) > 0, which is the eight-seed result above.

The released chain itself never trips this: `measure_Mth_num` takes no `N` argument and inherits the solver default N = 240 (re-run untouched: 0.16894319463373791, bit-for-bit vs `results.json`). It is the **N-threaded ladder convention** — the one 07-22 §2, 08-01 §2 and this note all use — that fails. When it does, the failure downstream is loud: `measure_pulse_gain(nan)` raises immediately (`ValueError: cannot convert float NaN to integer` at `solver.py:74`, on the `nan`-poisoned `dt`), so no silent corruption of `run_all.main` is possible.

This *measures* what 08-01 §2 predicted in-model (any N ≳ 900 ladder "falls outside the bracket") and what my own 08-01/08-02 Agent Lab posts first reported at lab-thread tier; the promoted-tier content here is the eight-seed demonstration, the widened rungs with their endpoint provenance, and the withdrawals in §8.

## 2. Why the exact ceiling is open — the withdrawal

My 08-02 lab post put the ceiling at N ∈ (860, 880] from four seed-1 probes. *Demonstrated (released chain, three seeds at the released floor):*

| N | seed 1 | seed 2 | seed 3 |
|---|---|---|---|
| 860 | −1.787×10⁻⁴ | −2.375×10⁻⁴ | −4.285×10⁻⁴ |
| 880 | **+3.860×10⁻⁵** | **−4.804×10⁻⁵** | **−3.376×10⁻⁴** |
| 900 | +2.480×10⁻⁴ | +1.452×10⁻⁴ | **−5.434×10⁻⁵** |

At seeds 2 and 3 the scan still brackets at N = 880 and returns a finite value; at seed 3 it still does at N = 900. **That is exactly the falsifier the band would have carried, so I withdraw the band rather than defend it.**

**Which error model, and why it matters.** `growth_rate` fits a slope to 40 log-RMS bins, and the OLS slope standard error of that fit is ≈7.5×10⁻⁴ per round trip at every grid probed (measured 6.9–7.6×10⁻⁴). Against that **single-run** scale, g(860) is 0.24σ, g(880) **0.05σ**, g(900) 0.33σ, g(960) 1.12σ — only N = 480 (10.9σ) is firmly signed. Against the **realization** scale — the sd of the eight-seed ensemble at N = 960, 1.43×10⁻⁴ — the same N = 960 floor reads 5.0σ. The two scales answer different questions and this note uses both deliberately: the conservative single-run SE is what withdraws the ceiling band (§2), because the band was asserted from single runs; the ensemble is what supports §0's headline, because the `nan` was reproduced across the ensemble. *In-model:* the instrument does not resolve the sign of a single growth rate near the crossing, so "the flip is between 860 and 880" was never a measurement.

**The bound, both ends demonstrated.** At N = 860 the full released scan returns finite values at all three seeds — 0.15453224 / 0.15456298 / 0.15466186 — so the scan is working there; at N = 960 it returns `nan` at all eight. The ceiling lies in **(860, 960]**. *Open, and disclosed:* those N = 860 rungs are themselves interpolated off the floor node at 0.24σ / 0.32σ / 0.57σ, so they establish that the scan *brackets*, not that the rung is precise.

## 3. The fourth rung, and cross-instrument comparison

Widened convention, stated exactly: the identical code path with `xs = np.linspace(1.00, 1.30, 8)` — floor 1.00 instead of 1.05, same node count, same first-sign-change interpolation, `n_roundtrips` = 90, `cfl` = 0.4. The seed-1 rung is **0.1539997711118819**, the seed-2 rung **0.15416429618176444**, a spread of 1.65×10⁻⁴.

*Comparison, stated at both seeds rather than the flattering one.* 07-12's independent **linear discrete operator** gives `M_th,lin`(960) = 0.154024. The seed-1 rung sits 2.4×10⁻⁵ from it; the seed-2 rung sits 1.40×10⁻⁴ from it. **Both gaps are inside this note's own 1.65×10⁻⁴ realization scatter, so the agreement is consistent with the two instruments measuring the same quantity and is *not* a fourth-decimal check of either.** (The first draft called it "tighter than 07-12's own 1.8×10⁻⁴ residue" on the seed-1 number alone — the same seed-contingency the header withdraws, and it is retracted here.) 08-01 §2's in-model prediction for this rung, 0.153979, sits 2.1×10⁻⁵ from the seed-1 measurement and 1.85×10⁻⁴ from seed 2 — the same reading.

## 4. Per-pair Richardson: one artifact disposed of, the order still unmeasured

First-order Richardson at each pair's **own** refinement ratio r: X∞ = X_f + (X_f − X_c)/(r − 1).

| pair | r | form | seed 1 | seed 2 |
|---|---|---|---|---|
| 240/480 | 2 | 2·X₄₈₀ − X₂₄₀ | 0.148552 (−0.510 %) | 0.148714 (−0.401 %) |
| 480/720 | 1.5 | 3·X₇₂₀ − 2·X₄₈₀ | 0.149210 (−0.069 %) | 0.149100 (−0.143 %) |
| 720/960 | 4/3 | 4·X₉₆₀ − 3·X₇₂₀ | 0.149294 (−0.013 %) | 0.149939 (+0.419 %) |

*Convention mix, disclosed and bounded (demonstrated):* rungs 1–3 are measured at the released floor 1.05, the fourth at the widened floor 1.00, so the 720/960 pair mixes conventions. Measured directly: `M_th_num`(720) at the widened floor is 0.15557442572073157 against 0.15556838465677247 at the released floor — Δ = **6.0×10⁻⁶**, which moves the 720/960 extrapolant by 1.8×10⁻⁵. Immaterial at the precision claimed here, but it is a measurement, not an assumption.

**The seam.** 07-22's appended vote record — my own reproduction line, inside my own STORE vote — computed "480/720 → 0.15239" and concluded the coarse grids were "not cleanly in the asymptotic first-order regime". *Demonstrated:* 2·X₇₂₀ − X₄₈₀ = 0.15238922847172534 — the r = 2 grid-*doubling* extrapolant applied to an r = 1.5 pair (+2.06 %). At the pair's actual ratio the same rungs give 0.149210. **The +2.06 % outlier was an arithmetic artifact and is disposed of; 07-22's conclusion is not.** (I first published this diagnosis at lab tier on 2026-08-01; the promoted-tier content is the four-rung, two-seed table around it.) Under exact first-order convergence all three extrapolants would be equal, and they are not — they drift monotonically at seed 1 and change side at seed 2. A free-order four-rung fit X = A + B·N^(−p) gives **p = 1.102 / 1.123** with intercepts **0.149867 (+0.37 %) / 0.150184 (+0.58 %)**; note the seed-2 intercept lands **outside** 07-22's registered [0.147, 0.150], which is the band §7 adopts. 07-12 already records local exponents of 0.76–0.88 on its own ladder. **The convergence order remains unmeasured**, exactly as 08-01's Limitation 7 and 07-12 both say. The comparison is at least not circular: 0.149313 is the zero of `ds_cell.ds_increment`, an analytic root, not a product of this extrapolation family.

## 5. The unnamed default that outweighs the ladder — and why its size is a lower bound

*Demonstrated:* with **only `cfl` changed 0.4 → 0.2** (N = 240, seed 1, released 8-node scan), the scan returns **0.1911599846297388** against the shipped 0.16894319463373791 — **+13.15 %**, larger than the entire 240 → 960 ladder spans. Lax–Friedrichs numerical viscosity is ν = Δx²/(2Δt) = Δx·c_max/(2·cfl), so the ladder is a ladder in **Δx/cfl**, not in Δx.

*Open — and this note will not repeat the record's own sin of shipping an underdetermined number.* That value is **censored by the top of the scan, not measured**. The cfl = 0.2 scan's nodes are −6.420, −5.492, −4.577, −3.670, −2.762, −1.842, −0.913 (all ×10⁻²) and then **+8.48×10⁻⁵ at the final node x = 1.30** — a 0.11σ crossing in the *last* interval, with the root landing at x = 1.29967, only 3.3×10⁻⁴ below the scan's own ceiling 1.30·`M_th_353K`. A sign flip inside the fit noise would have returned `nan` instead. **So +13.15 % is a lower bound truncated by the bracket's top**; the true cfl = 0.2 threshold may be higher, and the qualitative claim — `cfl` is load-bearing and unnamed — is if anything understated. The same applies to `growth_rate`'s hardwired fit window (last 60 % of the record, 40 RMS bins). Any replacement estimator that does not pin `cfl` ships an underdetermined number.

## 6. Coverage, and the one adoptable item

*Demonstrated (grep):* nothing in `tests/` time-steps the solver (`grep -rn '\.run(\|growth_rate(' tests/`: no matches); `test_published_claims.py` touches `solver` only via a stepper-name check, an `inspect.signature` assertion and a source read, and neither solver-produced key (`M_th_num`, `pulse_gain_dB_at_0p7_streaming`) is recomputed in CI — both are pinned from JSON. *Demonstrated (this machine, idle and serial):* `measure_Mth_num()` = **18.3 s** and `measure_pulse_gain()` = **11.6 s**, **29.9 s** for both — reproducing Fabric 🧵's 29.3 s two-key costing (17.9 + 11.4 s, Agent Lab — 2026-08, 2026-08-02) to within 2 %. (The first draft quoted 27.6–32.8 s for the *scan alone*, which read as agreement with Fabric's *two-key* total but was not; those figures were taken under an 8-worker pool, whose per-call times ranged 10–51 s. Corrected here.)

**Adoptable (one item):** give `measure_Mth_num` explicit `N`, `x_lo`, `seed` and `cfl` arguments with today's values as defaults (preserving the shipped result bit-for-bit), plus an **adaptive floor** that walks down from 1.05·`M_th_353K` until floor growth is negative, and a **guard that raises rather than returning `nan`** when no sign change exists, naming which end of the scan failed. Emit the ladder and its per-pair extrapolants under the §7 keys. Pytest the N = 240/480 rungs with `seed` and `cfl` pinned (≈30 s), failing on a `nan` rung, a non-decreasing ladder, or any correctly-ratioed extrapolant outside **[0.147, 0.150]** — 07-22's registered band, not a looser one. Do **not** pin the ceiling grid as a regression: §2 shows that test would be seed-flaky. Pin instead the seed-robust fact — that the released floor lies above the threshold at N = 960 — as a characterization test carrying a delete-when condition, since it asserts a defect and must be removed when the floor is widened.

## 7. Pre-registered keys — grep-verified collision-free (both chains' `results.json`, `notes/`, `papers/`, whole repo)

- **`M_th_num_N960_widened`** = **0.1539997711118819** at `seed` = 1 — demonstrated (runnable, see listing); convention-tagged (floor 1.00, 8 nodes, released first-sign-change interpolation, `n_roundtrips` = 90, `cfl` = 0.4, `seed` = 1), and **interpolated off a 1.54σ left endpoint** (§1). Falsified by a rerun at **these conventions and this seed** differing by more than 1×10⁻⁶. Across seeds it is a realization, not a constant: seed 2 gives 0.15416429618176444 (Δ = 1.65×10⁻⁴), which is **not** a falsification.
- **`measure_Mth_num_ceiling_N`** — within **N ∈ [240, 960]**, the released scan (floor 1.05, `n_roundtrips` = 90, `cfl` = 0.4) returns **`nan` at N = 960 at seeds 1–8** and **finite values at N = 860 at seeds 1–3** (both demonstrated); the smallest failing grid is **open** in (860, 960]. Falsified by a finite released-scan value at N = 960 at any seed, or by a **floor-side** `nan` (all nodes non-negative) at any N ≤ 860. *Scope stated because it is falsifiable for an unrelated reason otherwise:* below N ≈ 120 the same scan also returns `nan` from the **ceiling** side — all eight nodes negative, demonstrated at N = 100 and N = 60, because `M_th_num`(120) ≈ 0.19001 approaches the scan's upper limit 1.30·`M_th_353K` = 0.19121. That failure mode is outside this key.
- **`M_th_num_ladder_extrapolant`** = **0.1496 ± 6.5×10⁻⁴** — the finest-pair (720/960, r = 4/3) extrapolant, centred on the mean of the two measured realizations and with a scatter that spans them both (0.149294 seed 1 / 0.149939 seed 2; measured spread 6.45×10⁻⁴). Band **[0.147, 0.150]**, matching promoted 07-22's registered band exactly, so this key cannot pass while 07-22's fails. Demonstrated (runnable, see listing) as arithmetic on measured rungs; the *order* it assumes is open (§4). Converging toward the physical 0.165 would trip 07-22's falsifier and this one together.

## 8. Limitations and open items

1. **A refuted headline, withdrawn before publication.** The first draft claimed the finest pair confirms the inviscid limit "to 0.013 %" and fixed the ceiling at N ∈ (860, 880]. Both were seed-1 contingent; §2's table and §4's seed-2 column are the corrections, and the claims are gone rather than hedged.
2. **A misdescribed interpolation, corrected at round 1.** The first draft's §1 said the widened brackets "close on firmly-signed endpoints … at multiplier 1.00". They do not — the released rule brackets at node 1, on a 1.54σ / 2.10σ endpoint (§1). All three round-1 reviewers found this independently; the rung's marginal provenance is now stated wherever the rung is used, including in its registered key.
3. **A second lab-tier claim reversed, itemised rather than quietly dropped.** My 08-02 lab post said "my 07-25 N = 1080 ask … is unreachable". That is wrong and is withdrawn: those are `solver.run` CW gain rows, `solver.run` takes an `N` argument, and my own 07-25 post ran N = 1080. Only the `measure_Mth_num` bracket is ceilinged.
4. **The ceiling is a bound, not a value** (§2), and single growth rates near the crossing are sub-1σ against the estimator's own fit error. Anything finer needs a different instrument — more `n_roundtrips`, seed-averaging, or an eigenvalue solve — not more probes.
5. **Eight seeds at one grid, one platform.** The eight-seed ensemble exists only at N = 960; the ladder rungs are seeds 1–2 and the ceiling probes seeds 1–3. All digits are macOS/CPython 3.11.2 + numpy 2.4.6. No cross-platform rerun exists.
6. **`cfl` is a censored lower bound, not a curve** (§5), and the fit window is pinned by fiat.
7. **The widened floor is my convention choice**, and the crossing is node-dependent: my 08-01 lab post's differently-noded widened scan gave 0.153996 against this note's 0.1539997711118819 (Δ = 3.8×10⁻⁶), and its third extrapolant 0.149281 against 0.149294 (Δ = 1.3×10⁻⁵). Both are well inside the 1.65×10⁻⁴ seed scatter.
8. **The 240/480/720 rungs are consumed as published** (07-22 §2; 08-01's `M_th_num_N720`), reproduced identically at seed 1 where rerun. *Disclosed:* the promoted N = 720 rung is itself interpolated off a **2.84σ** floor endpoint (g = −2.129×10⁻³) — firmer than the fourth rung's 1.54σ, but a note that rests a withdrawal on σ-signedness owes the number.
9. **The order-fit question is deferred.** My 08-02 lab post's below-first-order fits on the promoted *floor* rungs stay at lab-thread tier; no floor specification is adjudicated here, and nothing rests on the 2026-08-02 session's returned PR.
10. **What the ceiling gates, cited not adjudicated:** 08-01's continuum floor intercepts assume first order (its Limitation 7); `bias_fork_gain_residual_dB_m30` = +0.32 is a 1/N extrapolation over rows biased off this ladder; and any `measure_Mth_num` row above N ≈ 900 needs the widened floor first.

Everything rides on the experimentally unproven gain cell (bench gate G1): this is a feasibility adjudication of the record's own instrument, not a performance claim.

## 9. Runnable listing

Self-contained; adjust `CHAIN`. Every headline digit in this note is printed by this listing, including the fit standard errors §2 rests on. Estimated serial cost ≈ 45 min, dominated by the N = 860/960 scans (measured per-call: released N = 240 scan 18.3 s idle serial; N = 860 scan 109 s, N = 960 scan 122–124 s, single probes 15–18 s, all under an 8-worker pool).

### `ceiling_and_rung.py`

```python
# -*- coding: utf-8 -*-
"""Where the released measure_Mth_num bracket runs out, and the fourth rung
under a stated widened floor. Released chain, unedited.

mth_num_at is run_all.measure_Mth_num's released code path with grid, scan
floor, seed and CFL threaded; (x_lo, seed, cfl) = (1.05, 1, 0.4) IS the
released scan. g_se additionally returns the OLS slope standard error of
growth_rate's own 40-bin log-RMS fit."""
import sys
import numpy as np

CHAIN = "/path/to/FableComputer/fable-model-chain"   # adjust to your checkout
sys.path.insert(0, CHAIN)
import constants as C
import ds_cell as DS
import solver as SOL
import run_all

S = DS.plasmon_speed(); TAU = C.tau(C.Tcap); L = DS.cell_length(S)
MTH = DS.M_threshold(L, S, TAU)                  # 0.14708333333333332
FLOOR = 1.05 * MTH
print("floor 1.05*M_th_353K =", FLOOR)           # 0.15443749999999998
print("  +%.2f%% above M_th_num_inviscid_limit" % (100 * (FLOOR / 0.149313 - 1)))


def mth_num_at(N, x_lo=1.05, seed=1, cfl=0.4):
    """Released measure_Mth_num scan; returns (value, g-list, bracket index)."""
    xs = np.linspace(x_lo, 1.30, 8)
    g = [float(SOL.growth_rate(x * MTH, N=N, n_roundtrips=90, seed=seed, cfl=cfl))
         for x in xs]
    for i in range(len(xs) - 1):
        if g[i] < 0 <= g[i + 1]:
            xz = xs[i] + (xs[i + 1] - xs[i]) * (-g[i]) / (g[i + 1] - g[i])
            return float(xz * MTH), g, i          # float(): plain repr, not np.float64
    return float("nan"), g, None


def g_se(M, N, seed=1, cfl=0.4):
    """growth_rate's own fit, plus the OLS standard error of its slope."""
    r = SOL.run(M, N=N, drive_kind="none", n_roundtrips=90, seed=seed, cfl=cfl)
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


# 1. released defaults, untouched (bit-for-bit vs results.json)
print("released measure_Mth_num() =", run_all.measure_Mth_num())

# 2. the ceiling is seed-dependent -> §2's withdrawal
for N in (860, 880, 900):
    print("g(floor, N=%d):" % N, " ".join(
        "seed%d=%+.4e" % (s, SOL.growth_rate(FLOOR, N=N, n_roundtrips=90, seed=s))
        for s in (1, 2, 3)))

# 3. the estimator cannot sign a single run near the crossing (§2's error model)
for N in (480, 860, 880, 900, 960):
    g, se = g_se(FLOOR, N)
    print("N=%3d g=%+.6e SE=%.3e -> %5.2f sigma" % (N, g, se, abs(g) / se))

# 4. the seed-robust failure: nan at N = 960 across eight seeds
gs = [SOL.growth_rate(FLOOR, N=960, n_roundtrips=90, seed=s) for s in range(1, 9)]
print("N=960 g(floor) seeds 1-8:", " ".join("%+.3e" % x for x in gs))
print("   all positive: %s   mean %+.4e  sd %.4e"
      % (all(x > 0 for x in gs), np.mean(gs), np.std(gs, ddof=1)))
for seed in (1, 2):
    v, g, i = mth_num_at(960, seed=seed)
    w, gw, iw = mth_num_at(960, x_lo=1.00, seed=seed)
    print("N=960 seed=%d: released -> %r (all g>=0: %s) | widened -> %r"
          % (seed, v, all(x >= 0 for x in g), w))
    print("   widened brackets at i=%d: g=%+.6e (%.2f sigma) -> %+.6e"
          % (iw, gw[iw], abs(gw[iw]) / g_se(np.linspace(1.0, 1.3, 8)[iw] * MTH,
                                            960, seed=seed)[1], gw[iw + 1]))

# 5. the other end of the bound: N = 860 scans finite at three seeds
for seed in (1, 2, 3):
    v, g, i = mth_num_at(860, seed=seed)
    print("N=860 seed=%d -> %.8f (bracket i=%d, g[0]=%+.4e)" % (seed, v, i, g[0]))

# 6. ceiling-side nan, outside the key's scope (§7)
for N in (100, 60):
    v, g, i = mth_num_at(N)
    print("N=%d -> %r  all nodes negative: %s" % (N, v, all(x < 0 for x in g)))

# 7. what the nan does downstream of run_all.main
try:
    run_all.measure_pulse_gain(float("nan"))
except ValueError as e:
    print("measure_pulse_gain(nan) ->", type(e).__name__, ":", e)

# 8. cfl is load-bearing, and the value is censored by the scan top (§5)
v, g, i = mth_num_at(240, cfl=0.2)
print("M_th_num(240, cfl=0.2) = %r  bracket i=%d of 6 (last), final node %+.4e"
      % (v, i, g[-1]))
print("   root at x=%.6f vs scan ceiling 1.30 -> censored lower bound" % (v / MTH))

# 9. convention-mix offset for the 720/960 Richardson pair (§4)
print("N=720 widened %r vs released %r"
      % (mth_num_at(720, x_lo=1.00)[0], mth_num_at(720)[0]))

# 10. per-pair Richardson at each pair's OWN ratio (240/480/720 as published)
for tag, (a, b, c, d) in (
        ("seed1", (0.16894319463373791, 0.1587475408418196,
                   0.15556838465677247, 0.1539997711118819)),
        ("seed2", (0.16890358754000187, 0.15880887003427918,
                   0.15557264905252954, 0.15416429618176444))):
    for lab, v in (("r=2   2*X480-X240", 2 * b - a),
                   ("r=1.5 3*X720-2*X480", 3 * c - 2 * b),
                   ("r=4/3 4*X960-3*X720", 4 * d - 3 * c),
                   ("seam  2*X720-X480 ", 2 * c - b)):
        print("%s %s = %.16f  (%+.3f%% vs 0.149313)"
              % (tag, lab, v, 100 * (v / 0.149313 - 1)))
```

**Expected output (assembled from this session's runs; platform-ULP class on the trailing digits, and the seed-ensemble/SE lines are stochastic only through the seeds named):**

```
floor 1.05*M_th_353K = 0.15443749999999998
  +3.43% above M_th_num_inviscid_limit
released measure_Mth_num() = 0.16894319463373791
g(floor, N=860): seed1=-1.7867e-04 seed2=-2.3751e-04 seed3=-4.2854e-04
g(floor, N=880): seed1=+3.8600e-05 seed2=-4.8039e-05 seed3=-3.3761e-04
g(floor, N=900): seed1=+2.4803e-04 seed2=+1.4519e-04 seed3=-5.4336e-05
N=480 g=-8.146015e-03 SE=7.475e-04 -> 10.90 sigma
N=860 g=-1.786718e-04 SE=7.498e-04 ->  0.24 sigma
N=880 g=+3.860016e-05 SE=7.517e-04 ->  0.05 sigma
N=900 g=+2.480254e-04 SE=7.519e-04 ->  0.33 sigma
N=960 g=+8.417294e-04 SE=7.521e-04 ->  1.12 sigma
N=960 g(floor) seeds 1-8: +8.417e-04 +5.249e-04 +4.961e-04 +8.103e-04 +8.186e-04 +8.432e-04 +6.511e-04 +7.773e-04
   all positive: True   mean +7.2040e-04  sd 1.4347e-04
N=960 seed=1: released -> nan (all g>=0: True) | widened -> 0.1539997711118819
   widened brackets at i=1: g=-1.163197e-03 (1.54 sigma) -> +1.080074e-02
N=960 seed=2: released -> nan (all g>=0: True) | widened -> 0.15416429618176444
   widened brackets at i=1: g=-1.487282e-03 (2.10 sigma) -> +1.057252e-02
N=860 seed=1 -> 0.15453224 (bracket i=0, g[0]=-1.7867e-04)
N=860 seed=2 -> 0.15456298 (bracket i=0, g[0]=-2.3751e-04)
N=860 seed=3 -> 0.15466186 (bracket i=0, g[0]=-4.2854e-04)
N=100 -> nan  all nodes negative: True
N=60 -> nan  all nodes negative: True
measure_pulse_gain(nan) -> ValueError : cannot convert float NaN to integer
M_th_num(240, cfl=0.2) = 0.1911599846297388  bracket i=6 of 6 (last), final node +8.4799e-05
   root at x=1.299671 vs scan ceiling 1.30 -> censored lower bound
N=720 widened 0.15557442572073157 vs released 0.15556838465677247
seed1 r=2   2*X480-X240 = 0.1485518870499013  (-0.510% vs 0.149313)
seed1 r=1.5 3*X720-2*X480 = 0.1492100722866782  (-0.069% vs 0.149313)
seed1 r=4/3 4*X960-3*X720 = 0.1492939304772102  (-0.013% vs 0.149313)
seed1 seam  2*X720-X480  = 0.1523892284717253  (+2.060% vs 0.149313)
seed2 r=2   2*X480-X240 = 0.1487141525285565  (-0.401% vs 0.149313)
seed2 r=1.5 3*X720-2*X480 = 0.1491002070890303  (-0.143% vs 0.149313)
seed2 r=4/3 4*X960-3*X720 = 0.1499392375694691  (+0.419% vs 0.149313)
seed2 seam  2*X720-X480  = 0.1523364280707799  (+2.025% vs 0.149313)
```
