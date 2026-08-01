# The gated gain table in the requirement's own convention: the bias-consistent F = 2 clearance is +1.1 to +1.3 dB — not +0.03 — the '0'-floor becomes the binding leg, and the bias fork survives the continuum

**Status:** **draft** (`notes/drafts/`) — under review, not promoted; 2-of-3 assessment per [notes/README.md](../README.md) pending. **License:** CC BY 4.0.
**What this is:** the WP1 rerun that [`notes/2026-08-01-bench-gate-g1-reissued.md`](../2026-08-01-bench-gate-g1-reissued.md) §4 item 2 named as required: the 07-31/08-01 §4 duty-0.8 gated gain rows re-measured at the **ratio bias** 0.7·`M_th_num`(N) — the same convention as the [`notes/2026-08-01-gated-requirement-round-trip.md`](../2026-08-01-gated-requirement-round-trip.md) §5 requirement leg — so the gated F = 2 comparison exists, for the first time, with both legs in one bias convention. Twelve rows (m = 22/26/28/30 × N = 240/480/720, drive 2×10⁻³), plus a new rung on the numerical-threshold ladder, `M_th_num`(720).
**Method:** every number produced by executing the released `fable-model-chain/` on this machine (Python 3 + numpy, macOS/CPython, `python3`); `fable-model-chain/` was **not edited**. The driver is the 08-01 §8 `fs_driver.py` **verbatim** (validated there bit-identical to released `solver.run`, max |Δcav| = 0.0 over 250,167 steps); the two new listings in §8 are the only new code. Anchor: the m = 26/N = 240 row reproduces 08-01 §0.6's published ratio-bias pair **8.0292 / −10.6023** to the digit before any new row was trusted.
**Adversarial verification, disclosed.** Two blind, independent lenses ran before drafting. The **reproduction lens** rebuilt the harness from the stated conventions alone — it never opened this session's driver files — and reproduced the decisive rows **bit-identically** (m = 30/N = 240: diff exactly 0.0 in both gain and floor; m = 28/N = 480 to all printed digits; `M_th_num`(720) exact to the last float digit); it also caught a floor digit mis-transcribed into its own tasking (−11.8317 for the artifact's −11.8283) and correctly attributed the slip to the tasking, not the run — recorded here for the audit trail. The **analysis lens** re-derived every table entry, baseline, and fit independently; it confirmed all of them and **refuted one presentation** — the first analysis pass had called m = 30/N = 240 "PASS both" on a +0.007 dB strict-floor margin — and that refutation is accepted and carried in §5 rather than buried.
**Author:** drafted in a maintainer-operated Claude Code session per [agents/README.md](../../agents/README.md) (Operations); active model **`claude-fable-5`**.
**Labels:** demonstrated / in-model / open, per [notes/README.md](../README.md).
**Binding record honored:** [`notes/2026-08-01-gated-requirement-round-trip.md`](../2026-08-01-gated-requirement-round-trip.md) (the §5 ratio-leg requirement values consumed as published; its §0.6 bias-fork finding is what this note quantifies at every slot and grid; its §0.2 caveat that `G_req_gated` carries the imported `A_op` is inherited by every clearance below); [`notes/2026-07-31-physical-launch-gated-frontier.md`](../2026-07-31-physical-launch-gated-frontier.md) (the duty-0.8 waveform and scoring conventions §2, adopted unchanged; its analytic-bias rows are the comparison baseline); [`notes/2026-07-22-mth-numerical-vs-physical-viscosity.md`](../2026-07-22-mth-numerical-vs-physical-viscosity.md) (the inviscid limit 0.149313 the new ladder rung is checked against); [`notes/2026-08-01-bench-gate-g1-reissued.md`](../2026-08-01-bench-gate-g1-reissued.md) (whose §2 (v) bias rule this rerun serves and whose §4 item 2 it discharges). It contests **no** `results.json` value and reopens **no** promoted key.

---

## 0. Executive verdict

1. **07-31's +0.03 dB clearance was a cross-convention artifact, and the bias-consistent clearance is thirty times larger.** *Demonstrated (both legs measured, same bias, same grid):* at the ratio bias, the measured gated gain clears the measured-knee requirement `G_req_gated` (08-01 §5, ratio leg, gain-ratio observable) by **+1.127 dB (m = 28) / +1.279 dB (m = 30) at N = 240** and **+1.130 / +1.335 dB at N = 480**. Against the in-model Richardson requirement (7.28–7.31 dB) the m = 28/N = 720 gain gives ≈ +0.94 — shrinking with refinement but staying ~+0.9 dB positive. Two inherited caveats, stated up front: the requirement leg still carries the imported `A_op` = 0.0116 (08-01 §0.2), and the two legs are different observables (all-ones streaming per-slot-mean knee vs worst-'1' PRBS gain) — that transfer is **in-model**.
2. **The '0'-floor becomes the binding leg.** *Demonstrated:* ratio-bias floors sit 1.3–3.8 dB worse than the analytic-bias record on every matched row. Under the strict noise-margin anchor (−11.8211 dB) **no ratio-bias rung passes robustly**: the lone nominal pass, m = 30/N = 240 at −11.8283, is a **+0.007 dB margin** — indistinguishable from the boundary within the ~1 dB carrier-phase sensitivity 07-31 §2 documents — and the strict test fails outright at N = 480 (−11.4628, by 0.36 dB) and N = 720 (−11.3187, by 0.50 dB), with an in-model 1/N continuum floor ≈ −11.0 to −11.1. Under the round ≥ 10 dB spec, **67 GHz (m = 30) is the robust rung** (~1.0 dB continuum margin); **71 GHz (m = 28) straddles the spec in the continuum** (intercepts −9.98/−10.07); 77 GHz clears by only +0.055 dB at N = 720; **91 GHz (m = 22) fails at every grid** (−8.59/−8.14/−7.98).
3. **The bias fork does not close with grid refinement — it is a permanent 1.5 % design fork, now quantified.** *Demonstrated at the grids; in-model in the limit:* the ratio-minus-analytic gain delta falls from +1.09…+1.20 dB (N = 240) to +0.43…+0.60 dB (N = 720), but 1/N extrapolants leave **+0.31 to +0.33 dB at m = 30** (+0.14–0.22 at m = 26; +0.09–0.11 at m = 22), because the two conventions converge to *different* biases: 0.7 × inviscid = **0.104519** vs 0.7 × analytic = **0.102958**. The convention choice 08-01 §0.6 opened is not a numerical transient; it must be made as a named design decision, and the G1 note's §2 (v) bench-facing rule is the one candidate currently on the table.
4. **A new rung on the numerical-threshold ladder:** `M_th_num`(720) = **0.15556838465677247**, measured by the released bracket scan at N = 720. *Demonstrated (runnable, see listing).* The 480/720 Richardson extrapolant lands at 0.149210 — **0.07 % from the shipped inviscid limit 0.149313** — re-confirming 07-22's first-order-convergence claim from a rung it never had. (The 240-anchored pair gives 0.148553: mild curvature, so the agreement is pair-dependent — stated, not hidden.)
5. **Nothing moves in the promoted record.** The analytic-bias keys of 07-31 are registered in their own convention and are not re-measured here; incidentally, the ratio-bias values even sit inside 07-31's falsification bands (m = 30/N = 720 floor −11.319 is 0.32 dB from its band edge — a parenthetical, not a contest). `f_max_F2_gated_GHz` = 69 [63, 74] is neither confirmed nor moved: re-adjudicating it in the ratio convention needs the m = 26 knee (unmeasured) and the strict-vs-round floor-spec decision — both **open**.

Everything rides on the experimentally unproven gain cell (bench gate G1): this is a feasibility adjudication, not a performance claim.

## 1. Conventions and anchors — demonstrated

All scoring conventions are 07-31 §2 / 08-01 §4, adopted unchanged: seed-7 40-slot PRBS, first 4 slots dropped (36 scored), duty 0.8, raised-cosine edges of 2 rt, window [0.25, 0.72]·repT, observable `cav`, gain per '1' vs the identical-pattern M = 0 run, worst-case-'1' statistic, pp = raw '1'-level spread, floor = max-'0' referred to mean-'1', drive 2×10⁻³. The **bias** is the one deliberate change: 0.7·`M_th_num`(N) with `M_th_num` measured at the row's own grid by the released `measure_Mth_num` bracket (recomputed, never quoted): 0.7 × 0.16894319463373791 = **0.11826023624361653** (N = 240), 0.7 × 0.1587475408418196 = **0.11112327858927372** (N = 480), 0.7 × 0.15556838465677247 = **0.10889786925974073** (N = 720). Anchors: `M_th_num`(240) reproduces `results.json` bit-for-bit; the m = 26/N = 240 row reproduces 08-01 §0.6's **8.0292 / −10.6023** to the digit.

## 2. The threshold ladder — demonstrated, with a new rung

| N | `M_th_num`(N) | source |
|---|---|---|
| 240 | 0.16894319463373791 | = `results.json` bit-for-bit (recomputed) |
| 480 | 0.1587475408418196 | reproduces 08-01/Kinetic's rung (recomputed) |
| 720 | **0.15556838465677247** | **new** (this note; crossing between x = 1.05 and 1.0857 of the released bracket) |

480/720 Richardson: **0.149210**, vs the shipped `M_th_num_inviscid_limit` = 0.149313 (Δ = 1.0×10⁻⁴, 0.07 %) — consistent with first-order Lax–Friedrichs convergence (07-22). The bracket floor 0.154437 sits only 7×10⁻⁴ below the N = 720 value: **the released bracket has ≈ one rung of headroom left**, which is 08-01 consequence (iii) made concrete — widen the floor below 0.149313 before any N ≳ 900 ladder.

## 3. The gain table at ratio bias — demonstrated

G_worst1 / pp_raw / eye / floor (dB), drive 2×10⁻³; Δ = ratio − analytic on matched rows (analytic values: 07-31 published rows and 08-01 §4/§0.4/§6 and its appended assessment record):

| m (GHz) | N | G_worst1 | ΔG vs analytic | pp | eye | floor | Δfloor |
|---|---|---|---|---|---|---|---|
| 22 (91) | 240 | 7.5082 | +1.09 | 0.398 | +8.38 | −8.59 | +2.76 |
| 22 (91) | 480 | 7.3972 | +0.59 | 0.694 | +7.75 | −8.14 | — |
| 22 (91) | 720 | 7.3693 | +0.43 | 0.785 | +7.53 | −7.98 | +1.25 † |
| 26 (77) | 240 | 8.0292 | +1.19 | 0.160 | +10.54 | −10.60 | +3.47 |
| 26 (77) | 480 | 8.0150 | +0.71 | 0.276 | +10.11 | −10.25 | — |
| 26 (77) | 720 | 7.9875 | +0.52 | 0.367 | +9.86 | −10.06 | +1.50 † |
| 28 (71) | 240 | 8.1315 | — | 0.230 | +10.64 | −10.73 | — |
| 28 (71) | 480 | 8.2586 | +0.77 | 0.100 | +10.36 | −10.40 | +1.88 |
| 28 (71) | 720 | 8.2435 | +0.56 ‡ | 0.181 | +10.17 | −10.26 | — |
| 30 (67) | 240 | 8.2879 | +1.17 | 0.306 | +11.71 | −11.83 | +3.84 |
| 30 (67) | 480 | 8.4681 | +0.74 | 0.119 | +11.42 | −11.46 | +2.08 |
| 30 (67) | 720 | 8.5316 | +0.60 | 0.050 | +11.30 | −11.32 | +1.51 |

† the m = 22/26 N = 720 analytic floor baselines (−9.23 / −11.56) are 08-01 §0.4's A_fix-interpolated column, not 2×10⁻³ rows; the comparison is legitimate only via 07-31 §4's demonstrated ~0.05 dB drive-independence of floors, so these two Δfloor digits carry a ~0.05–0.1 dB drive-plane caveat. ‡ against 07-31's 2-decimal quote 7.68, so ±0.005 dB quote rounding.

*Demonstrated:* the gain grid-trend is slot-dependent on the ratio leg (m = 30 rises, m = 22/26 fall, m = 28 non-monotonic) — unlike the analytic leg, where all rise. pp stays under the 1-dB criterion everywhere (max 0.785), but m = 22's pp grows monotonically with N (0.398 → 0.694 → 0.785): the 91 GHz margin to that criterion is shrinking under refinement.

## 4. The bias-consistent clearances — demonstrated legs, in-model transfer

`G_req_gated` (08-01 §5, ratio leg, gain-ratio observable; **`A_op` imported** — 08-01 §0.2's caveat inherited):

| m | N | G_worst1 (this note) | G_req_gated (08-01 §5) | **clearance** |
|---|---|---|---|---|
| 28 | 240 | 8.1315 | 7.005 | **+1.127** |
| 30 | 240 | 8.2879 | 7.009 | **+1.279** |
| 28 | 480 | 8.2586 | 7.129 | **+1.130** |
| 30 | 480 | 8.4681 | 7.133 | **+1.335** |

Both legs at the identical bias and grid — the first bias-consistent gated F = 2 comparison in the record. No knee exists at N = 720 (08-01 §5 stops at 480), so no measured clearance exists at the finest grid; against the in-model Richardson requirement 7.28–7.31 the m = 28/720 gain gives ≈ +0.94–0.96. The clearance narrows with refinement (the requirement rises faster than the m = 28 gain) but remains ~+0.9 dB — **not** +0.03. The cross-observable transfer (per-slot-mean all-ones knee → worst-'1' PRBS gain) remains **in-model**; the 0.02 dB active-only/gain-ratio spread does not bound it.

## 5. Floors against the specs — demonstrated rows, honest verdicts

Strict anchor = 20·log₁₀(`noise_margin_frac`) = **−11.8211 dB**; round spec = −10 dB.

- **m = 30 (67 GHz):** −11.8283 / −11.4628 / −11.3187. At N = 240 the strict margin is **+0.007 dB — at the boundary, indistinguishable from it** within the ~1 dB carrier-phase sensitivity of floor digits (07-31 §2); the strict test **fails at both finer grids** (0.36 / 0.50 dB) and in the 1/N continuum (≈ −11.03 to −11.10). Round spec: passes everywhere, continuum margin ≈ 1.0 dB — **the robust rung**.
- **m = 28 (71 GHz):** −10.7312 / −10.4030 / −10.2615. Strict: fails everywhere. Round: passes at every measured grid; the 1/N continuum **straddles the spec** (intercepts −9.98 from the 480/720 pair, −10.07 from 240/480).
- **m = 26 (77 GHz):** −10.60 / −10.25 / −10.06 — round margin at N = 720 is **+0.055 dB**.
- **m = 22 (91 GHz):** fails the round spec at every grid.

**Bottom line, in one convention:** the gain leg is comfortable (+1.1–1.3 dB) and the floor leg binds. Under the strict spec no rung survives robustly; under the round spec the demonstrated-robust point is 67 GHz, with 71 GHz on the continuum knife-edge. Which floor spec governs the gated F = 2 adjudication is a design decision no promoted note has made — **open**, and now the decisive one.

## 6. Keys, grading, consequences

**Pre-registered keys** (grep-checked collision-free against both chains' `results.json` and every promoted note):

- **`M_th_num_N720`** = **0.15556838465677247** — the released `measure_Mth_num` bracket at N = 720. **Demonstrated (runnable, see listing)**; falsified by a rerun of the same scan differing by more than 1×10⁻⁶ (platform-ULP class). Non-contest: extends the ladder; the shipped `M_th_num` (N = 240) and `M_th_num_inviscid_limit` are consumed, not contested.
- **`gated_F2_clearance_ratio_bias_dB`** — m = 28: **+1.127** (N = 240) / **+1.130** (N = 480); m = 30: **+1.279** / **+1.335**; band **[+0.9, +1.5]**. **Demonstrated (runnable, see listing)** as arithmetic on two measured legs at one bias; **in-model** as an operating-margin claim (cross-observable transfer; imported `A_op` in the requirement leg).
- **`gated_floor_ratio_bias_dB`** — m = 30: **−11.83 / −11.46 / −11.32** (N = 240/480/720), band **[−12.1, −11.0]**; m = 28: **−10.73 / −10.40 / −10.26**, band **[−11.0, −10.0]**. **Demonstrated (runnable, see listing)**; the continuum intercepts (m = 30 ≈ −11.0, m = 28 ≈ −10.0) are **in-model** and never load-bearing.
- **`bias_fork_gain_residual_dB_m30`** = **+0.32**, band **[+0.1, +0.6]** — the in-model 1/N limit of the ratio-minus-analytic gain delta at m = 30 (extrapolants +0.31–0.33; m = 26 gives +0.14–0.22, m = 22 +0.09–0.11). **In-model**; falsified if a finer-grid ladder drives the matched-row delta below +0.1 or above +0.6 dB at m = 30.

**Grading the record it consumes.** 08-01's §0.6 fork is **confirmed and quantified**: worth +1.1–1.2 dB of gain and 2.8–3.8 dB of floor at N = 240, decaying toward a persistent ≈ +0.3 dB (m = 30) in the continuum. Its `G_req_gated_F2_dB` = 7.3 [6.9, 7.4] is consumed at its own grid values; its registered knee and A_SAT keys are untouched. 07-31's analytic-bias rows are the baseline throughout and reproduce wherever re-derived; its `f_max_F2_gated_GHz` = 69 [63, 74] is **neither moved nor re-adjudicated** (that needs the m = 26 knee and the floor-spec decision). 07-22's inviscid limit gains a third-rung consistency check at 0.07 %. The G1 note's §4 item 2 is **discharged**: the bench comparison sheet can now be assembled with both model-side legs in the ratio convention — the two remaining transfers (observable, `A_op`) are named in §4.

**Part III consequence (in-model, honest).** In the one convention the bench will actually use, the gated F = 2 story inverts: the gain margin is not the thin leg — the '0'-floor is. The decisive open item is no longer "measure the requirement" (done, 08-01) nor "match the conventions" (done, here) but **"choose the floor spec"**: strict (−11.8211) leaves no robust gated rung; round (−10) leaves 67 GHz robust and 71 GHz marginal. That choice, plus the m = 26 knee, is what now stands between the record and a ratio-convention frontier statement.

## 7. Limitations and open items

1. **One drive amplitude.** All rows at 2×10⁻³; no ratio-bias amplitude ladder, so A_fix and the loaded fixed point are not re-measured in this convention (08-01 §4's table remains the only ladder, analytic-bias).
2. **No knee at N = 720** — the finest-grid clearance is against an in-model extrapolant only.
3. **Cross-observable transfer is in-model** (§4): the requirement leg is an all-ones streaming per-slot-mean knee, the gain leg a worst-'1' PRBS statistic. No measurement here bounds that transfer.
4. **The requirement leg inherits `A_op`** = 0.0116 (imported, round-tripped — 08-01 §0.1/§0.2). The clearances are exactly as `A_op`-dependent as `G_req_gated` itself.
5. **Single seed and pattern** (seed 7, 36 scored slots), one carrier-phase convention; floor digits carry the documented ~1 dB phase-convention sensitivity, which is why §5's strict-boundary reading at m = 30/N = 240 is reported as a boundary, not a pass.
6. **Two Δfloor baselines are drive-plane-caveated** (§3 †) and one ΔG is against a 2-decimal quote (§3 ‡).
7. **The 1/N fits use two or three rungs**; the M_th ladder shows mild curvature (intercept 0.148553 from the 240-anchored pair vs 0.149210 from 480/720), so first-order convergence of the *floors* is assumed, not established.
8. **Everything rides on the experimentally unproven gain cell** (bench gate G1).

## 8. Runnable listings

`fs_driver.py` is the 08-01 §8 promoted listing, **verbatim and unmodified** — it is not duplicated here; the two files below are the only new code. Run order and cost on this machine: `ratio_rerun.py 240,480,720 6` (~19 min wall, 6 workers: three bracket scans ≈ 19 s / 100 s / 320 s, then 12 scored rows) → `analyze_ratio.py` (instant).

### `ratio_rerun.py`

```python
# -*- coding: utf-8 -*-
"""The G1 note §4 item 2 WP1 follow-up: re-run the 07-31/08-01 §4 duty-0.8
gated PRBS gain rows at the RATIO bias 0.7 * M_th_num(N), with M_th_num
measured at the row's own grid by the released `measure_Mth_num` scan
(recomputed here, not quoted) — so the gain leg and the 08-01 §5 requirement
leg share one convention.

Conventions otherwise identical to 08-01 §4 / 07-31 §2 (adopted unchanged):
seed-7 40-slot PRBS, first 4 slots dropped (36 scored), duty 0.8, raised-cosine
edges of 2 rt, window [0.25, 0.72]*repT, observable cav, gain per '1' vs the
identical-pattern M = 0 run, worst-case-'1' statistic, pp = raw '1'-level
spread, floor = max-'0' referred to mean-'1'.

Anchor: the m = 26, N = 240 row must reproduce 08-01 §0.6's published
8.0292 dB / floor -10.6023 (bias 0.7 * 0.16894319463373791 = 0.11826024).
"""
import json, os, sys, time
import numpy as np
from multiprocessing import Pool

from fs_driver import make_sig, run_custom, slot_peaks, measure, default_bits, CHAIN
sys.path.insert(0, CHAIN)
import solver as SOL
import ds_cell as DS
import constants as C

S = DS.plasmon_speed(); TAU = C.tau(C.Tcap); L = DS.cell_length(S)
MTH = DS.M_threshold(L, S, TAU)          # 0.14708333333333332
F0N = C.f0 * L / S                       # 0.25
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "ratio_rerun.jsonl")
OUT_MTH = os.path.join(HERE, "ratio_rerun_mth.jsonl")


def mth_num_at(N):
    """run_all.measure_Mth_num's released bracket scan, at grid N (the same
    code path knee_stream.py used in 08-01; returns the scan for the record)."""
    xs = np.linspace(1.05, 1.30, 8)
    g = [SOL.growth_rate(x * MTH, N=N, n_roundtrips=90) for x in xs]
    for i in range(len(xs) - 1):
        if g[i] < 0 <= g[i + 1]:
            xz = xs[i] + (xs[i + 1] - xs[i]) * (-g[i]) / (g[i + 1] - g[i])
            return xz * MTH, list(zip([float(x) for x in xs], [float(v) for v in g]))
    return float("nan"), list(zip([float(x) for x in xs], [float(v) for v in g]))


def row(cfg):
    t0 = time.time()
    m, N, amp = cfg["m"], cfg["N"], cfg["amp"]
    repT = 2.0 * m
    nslots = 40
    bits = default_bits(nslots, cfg.get("seed", 7))
    sig = make_sig("duty", bits, repT, F0N, amp, edge_rt=2.0, duty=cfg["duty"])
    nrt = nslots * m
    rM = run_custom(cfg["bias"], N, nrt, sig)
    r0 = run_custom(0.0, N, nrt, sig)
    res = dict(cfg)
    res.update(measure(bits, slot_peaks(rM, repT, nslots), slot_peaks(r0, repT, nslots)))
    res["secs"] = round(time.time() - t0, 1)
    return res


def dispatch(cfg):
    try:
        return row(cfg)
    except Exception as e:
        out = dict(cfg); out["error"] = repr(e)
        return out


if __name__ == "__main__":
    Ns = [int(x) for x in (sys.argv[1] if len(sys.argv) > 1 else "240,480,720").split(",")]
    nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    jobs = []
    for N in Ns:
        t0 = time.time()
        mthn, scan = mth_num_at(N)
        print(f"M_th_num({N}) = {mthn!r}   0.7* = {0.7*mthn!r}   [{time.time()-t0:.0f}s]",
              flush=True)
        with open(OUT_MTH, "a") as f:
            f.write(json.dumps({"N": N, "M_th_num": mthn, "scan": scan}) + "\n")
        for m in (22, 26, 28, 30):
            jobs.append({"m": m, "N": N, "duty": 0.8, "amp": 2e-3,
                         "bias": 0.7 * mthn, "bias_mode": "ratio",
                         "mth_num": mthn, "seed": 7, "exp": "R"})
    print(f"{len(jobs)} jobs, {nproc} workers", flush=True)
    mode = "a" if os.path.exists(OUT) else "w"
    with open(OUT, mode) as f:
        with Pool(nproc) as pool:
            for res in pool.imap_unordered(dispatch, jobs):
                f.write(json.dumps(res) + "\n"); f.flush()
                print({k: (round(v, 4) if isinstance(v, float) else v)
                       for k, v in res.items()
                       if k in ("m", "N", "bias_mode", "G_worst1_dB", "pp_raw_dB",
                                "eye_dB", "max0_below_mean1_dB", "secs")}, flush=True)
    print("DONE", flush=True)
```

### `analyze_ratio.py`

```python
# -*- coding: utf-8 -*-
"""Render the one-convention bench comparison sheet from ratio_rerun.jsonl.

- ratio-bias small-signal rows (G_worst1 / pp_raw / eye / floor) per slot+grid
- delta vs the analytic-bias record (07-31 published + 08-01 §4, quoted below)
- same-convention clearance: G_small(ratio) - G_req_gated(ratio leg, 08-01 §5)
- spec status per row: round floor spec >= 10 dB; strict noise-margin anchor
  20*log10(0.25641458774368575) = -11.8211 dB
- anchor check: m=26/N=240 vs 08-01 §0.6's published 8.0292 / -10.60
NOTE (post-verification): the per-row "PASS both" column is mechanical
arithmetic; §5 of the note is the governing presentation — the m=30/N=240
strict reading is a boundary within convention error, not a pass.
"""
import json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(HERE, "ratio_rerun.jsonl"))
        if l.strip()]
rows = [r for r in rows if "error" not in r]
mth = {json.loads(l)["N"]: json.loads(l)["M_th_num"]
       for l in open(os.path.join(HERE, "ratio_rerun_mth.jsonl")) if l.strip()}

# The analytic-bias record for the same rows (07-31 published tables; 08-01 §4;
# 08-01 §6 grading row m=22/N=720; Quanta's assessment run m=30/N=720).
ANALYTIC = {  # (m, N): (G_worst1, floor)
    (22, 240): (6.4166, -11.35), (26, 240): (6.8342, -14.07), (30, 240): (7.1223, -15.67),
    (22, 480): (6.8070, None),   (26, 480): (7.3052, None),
    (28, 480): (7.4932, -12.28), (30, 480): (7.7294, -13.54),
    (22, 720): (6.9391, -9.23),  (26, 720): (7.4664, -11.56),
    (28, 720): (7.68, None),     (30, 720): (7.9304, -12.831),
}
# 08-01 §5 ratio-leg G_req_gated(F2), gain-ratio observable (a-o in parens)
GREQ_RATIO = {(28, 240): 7.005, (30, 240): 7.009, (28, 480): 7.129, (30, 480): 7.133}
STRICT = 20 * math.log10(0.25641458774368575)   # -11.8211 dB
GHZ = {22: 90.9, 26: 76.9, 28: 71.4, 30: 66.7}
BASE = 6.515399158503943

print(f"M_th_num by grid: {mth}")
print(f"strict floor anchor = {STRICT:.4f} dB; round spec = -10 dB; BASE(F2) = {BASE:.4f}\n")
hdr = (f"{'m':>3} {'GHz':>5} {'N':>4} | {'G_ratio':>8} {'G_analytic':>10} {'dG':>6} | "
       f"{'floor_r':>8} {'floor_a':>8} {'dfloor':>7} | {'pp':>6} {'eye':>7} | "
       f"{'headroom':>8} {'G_req(r)':>8} {'clear':>7} | floor spec")
print(hdr); print("-" * len(hdr))
for r in sorted(rows, key=lambda r: (r["N"], r["m"])):
    m, N = r["m"], r["N"]
    g, fl = r["G_worst1_dB"], r["max0_below_mean1_dB"]
    ga, fa = ANALYTIC.get((m, N), (None, None))
    dg = f"{g-ga:+.2f}" if ga is not None else "   —"
    df = f"{fl-fa:+.2f}" if fa is not None else "    —"
    req = GREQ_RATIO.get((m, N))
    clear = f"{g-req:+.3f}" if req else "     —"
    spec = ("PASS both" if fl <= STRICT else
            "pass round only" if fl <= -10.0 else "FAIL round")
    print(f"{m:3d} {GHZ[m]:5.1f} {N:4d} | {g:8.4f} {ga if ga is not None else float('nan'):10.4f} {dg:>6} | "
          f"{fl:8.2f} {fa if fa is not None else float('nan'):8.2f} {df:>7} | "
          f"{r['pp_raw_dB']:6.3f} {r['eye_dB']:+7.2f} | "
          f"{g-BASE:+8.4f} {req if req else float('nan'):8.3f} {clear:>7} | {spec}")

a = [r for r in rows if r["m"] == 26 and r["N"] == 240]
if a:
    r = a[0]
    ok = abs(r["G_worst1_dB"] - 8.0292) < 5e-4 and abs(r["max0_below_mean1_dB"] + 10.6023) < 5e-3
    print(f"\nANCHOR m=26/N=240 vs 08-01 §0.6 (8.0292 / -10.6023): "
          f"{r['G_worst1_dB']:.4f} / {r['max0_below_mean1_dB']:.4f}  -> {'OK' if ok else 'MISMATCH'}")
```
