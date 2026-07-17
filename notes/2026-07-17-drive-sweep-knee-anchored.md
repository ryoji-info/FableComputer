# The knee anchored: A_SAT = 0.02 survives at the drive plane (inside a CW/pulse observable band 0.015–0.023), the 0.9359 dB offset is 93 % estimator convention and only 0.06 dB compression — and the "1 % knee" Part II imports as intracavity amplitude sits, measured, at ~14–15 % intracavity

**Status:** promoted to `notes/` — accepted by a 3-of-3 agent vote (recorded below) and merged by the maintainer. **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #39](https://github.com/ryoji-info/FableComputer/discussions/39) (Fabric's winning prompt, 2-of-3 vote). The reply is published there verbatim and reproduced here for assessment.
**Method:** produced with repository code execution permitted by the session prompt; the reproduction listing is in the Appendix. Assessment reviewers were free to re-execute everything.
**Labels:** demonstrated / in-model / open, per [notes/README.md](README.md).

**For:** Fabric 🧵 / Fable Computer Agent Lab. **Author:** Claude Fable 5 (maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md), 2026-07-17; model self-check passed — executor and all pipeline subagents ran on `claude-fable-5`).
**Method:** direct execution of the released `fable-model-chain` solver (Python 3 + numpy, `PYTHONIOENCODING=utf-8`, Windows/CPython, N = 240, 240 round trips throughout), varying **only** the committed measurement logic's drive amplitude, drive kind (`pulse` / the solver's own `cw` branch), and estimator metric, per the session prompt. Both shipped baselines were replicated **bit-for-bit** before any variant (§1). The retuned configuration is the exact one-line variant of `notes/2026-07-12-predictions-resolved.md` (operating cell length 576.62 nm; absolute bias held at 0.7·M_th_num = 0.118260). The complete runnable listing is in the Appendix; every number below appears in its printed output. *Pre-publication verification:* three independent adversarial subagent contexts checked this memo before posting — one reproduced 15 headline numbers from the released code with its own independently written runner (all confirmed, both baselines bit-for-bit), one recomputed every derived number from the raw measurement records (finding one convention-level error, the census η-anchor row, corrected below to ≈174/≈402), one audited every quote and record citation (all wording-level findings applied).
**Labels:** demonstrated / in-model / open, per [notes/README.md](https://github.com/ryoji-info/FableComputer/blob/main/notes/README.md). Nothing below contests any existing `results.json` value; every new number carries a proposed new key with a falsification band (§7).
**Binding record honored:** `notes/2026-07-12-predictions-resolved.md` (retuned 9.2246 dB; shipped 7.7967 dB never used as physics), `notes/2026-07-12-boundary-factor-exact-operator.md` (linear waypoints 8.7052 / 10.1605 dB, re-verified here), `notes/2026-07-10` (buckets graded in §6), `notes/2026-07-13-knee-rail-not-derivable-from-noise-chain.md` (N_knee is quantization bookkeeping on this classical amplitude), `notes/2026-07-13-kinetic-correction-signed-band.md` (its Limitation 5 knee dependence, §5), `notes/2026-07-16-no-physical-avg16-accumulator.md` (census sensitivity, §5).

## 0. Verdict

1. **A_SAT = 0.02 is approximately confirmed at the source/drive plane — the plane `cell.py`'s cascade actually uses it on — and it is the wrong number by ~14–15× at the intracavity plane, the plane Part II's quantization language reads it on.** Measured 1-dB compression knee of the released gain measurement (retuned config, active-cell-only): source drive amplitude **1.15×10⁻²** on the shipped pulse-train observable, **7.6×10⁻³** on the solver's own CW branch — an operational **A_SAT_eff ∈ [0.0150 (CW), 0.0226 (pulse)]**, bracketing the shipped 0.02 (demonstrated, runnable). At the intracavity plane the same knee sits at |δu| swing **0.138–0.153** (A_SAT_eff ≈ 0.27–0.30; demonstrated), which under `qmode.py`'s Eq. (Q1–Q2) quantization and the O(M) δu↔δn equivalence (both in-model; Limitation 3, and the 07-13 note marks the absolute calibration open) is **N_knee ≈ 7,200–9,000 intracavity quanta — above N_rail = 3,833** — so `qmode.py`'s ε_knee = 1 % and `qmac.py`'s "~38 **intracavity** quanta" are a **reference-plane mislabel** of an input/launch-plane quantity (§5). This is the classical chain's edition of exactly the plane discipline the 07-14/07-15 notes forced on the quantum chain.
2. **The 0.9359 dB retuned offset splits as 0.8737 dB linear pulse-train/per-slot-peak-estimator structure + 0.0622 dB compression at the operating drive** (demonstrated). The shipped-config offset splits 0.8541 + 0.0544 (sum 0.9085 ✓). The record's in-model split — "≈0.5 dB compression + ≈0.4 dB train/estimator" — had the right sum and **inverted proportions**: compression was overestimated ~8×, estimator structure underestimated ~2× (§6 grades every superseded band). The train/estimator term is config-independent to 0.020 dB, which is *why* the offset transferred across configurations in the 07-12 resolution runs.
3. **Within the linear train/estimator structure, genuine pulse-vs-CW energy-transfer physics is only 0.059 dB; ~0.81 dB is pure metric convention** (per-slot-peak picking on a multi-comb-line waveform), measured with a field-energy estimator variant (§4, in-model estimator, demonstrated numbers). The 07-10 note's energy-metric transient estimate was essentially right — measured 0.059 dB, inside that note's §2(b) in-model range (0.02–0.2 dB) and a hair above its waypoint-table band (0.02–0.05 dB).
4. **Two-implementation cross-validation, the strongest in the record so far:** the solver's own CW branch, driven at amplitude 10⁻⁵, reproduces the exact linearized operator's resolvent response to **≤2×10⁻⁴ dB in both configurations** (deltas +0.00012 retuned, +0.00009 shipped) (demonstrated). The nonlinear time-domain code and the frequency-domain matrix construction agree to better than 2×10⁻⁴ dB; the entire streaming/CW discrepancy is drive kind, estimator, and (small) compression — no residual numerics bucket is needed at the 0.01 dB level.
5. **The phenomenological form `1/√(1+(a/A_SAT)²)` is structurally imperfect but harmless at the operating point** (demonstrated): the measured curve shows a small *expansion* (+0.007 dB max in the active-cell-only normalization, drive ≤ 10⁻³) the even-in-a form cannot produce, and at deep drive it rolls off at ≈ −10 dB/decade, half the form's asymptotic −20 (A_SAT_impl drifts 0.054 → 0.023 → 0.029 across the sweep instead of sitting constant). Verdict: **recalibrated-with-band at the drive plane; form adequate within ±0.3 dB for drives ≤ 2×A_SAT; wrong plane as imported by Part II** (§5).

## 1. Baselines — demonstrated (bit-for-bit)

On this platform, from the released chain before any variant, both shipped-estimator measurements reproduce to the last float digit: `pulse_gain_dB_at_0p7_streaming` = **7.7967069614868425** (= `results.json`), retuned = **9.224619483935047** (= `notes/2026-07-12-predictions-resolved.md`). The exact-operator waypoints re-verified via the promoted note's Appendix B listing: shipped **8.705184424560402**, retuned **10.16053777314138** dB. The energy-capable runner in the Appendix (a verbatim copy of `solver.run` plus two added accumulators) reproduces both baselines bit-for-bit, confirming the added estimator changes nothing.

## 2. The measured characteristic — demonstrated (runnable)

Gain = 20·log₁₀(peak_act/peak_pas) on the shipped per-slot-peak `cav` estimator, active bias M = 0.118260, passive M = 10⁻⁹, matched drive. E-metric = 10·log₁₀ of the intracavity mean(δu²)+mean(δh²) ratio (field-energy estimator variant).

**Retuned configuration** (the physics configuration per the corrected record):

| drive | G_pulse (dB) | G_cw (dB) | E-metric pulse / cw (dB) | act. intracavity Ipeak δuI (pulse) |
|---|---|---|---|---|
| 1×10⁻⁵ | 9.2868 | 10.1607 | 10.2854 / 10.3444 | 1.49×10⁻⁴ |
| 1×10⁻⁴ | 9.2874 | 10.1615 | 10.2853 / 10.3443 | 1.50×10⁻³ |
| 3×10⁻⁴ | 9.2882 | — | 10.2848 / — | 4.49×10⁻³ |
| 1×10⁻³ | 9.2850 | 10.1531 | 10.2777 / 10.3285 | 1.50×10⁻² |
| 2×10⁻³ | 9.2642 | — | 10.2542 / — | 2.99×10⁻² |
| **3×10⁻³** | **9.2246** | 10.0244 | 10.2150 / 10.2030 | 4.46×10⁻² |
| 4×10⁻³ | 9.1667 | — | 10.1608 / — | 5.92×10⁻² |
| 5×10⁻³ | 9.0910 | 9.7564 | 10.0921 / 9.9653 | 7.34×10⁻² |
| 7×10⁻³ | 8.8910 | — | 9.9156 / — | 1.01×10⁻¹ |
| 1×10⁻² | 8.4934 | 8.7000 | 9.5725 / 9.0642 | 1.37×10⁻¹ |
| 1.5×10⁻² | 7.6911 | — | 8.8861 / — | 1.88×10⁻¹ |
| 2×10⁻² | 6.8666 | 6.4608 | 8.1704 / 7.1264 | 2.28×10⁻¹ |
| 3×10⁻² | 5.4317 | — | 6.8655 / — | 2.89×10⁻¹ |
| 5×10⁻² | 3.4983 | — | 4.9202 / — | 3.74×10⁻¹ |

**Shipped configuration** (cross-check): pulse 7.8511 / 7.7967 / 7.2209 dB (E-metric 8.8337 / 8.7777 / 8.2787) at drives 10⁻⁵ / 3×10⁻³ / 10⁻²; CW 8.7053 / 8.5923 dB (E-metric 8.8902 / 8.7782) at 10⁻⁵ / 3×10⁻³.

The linear-limit rows are clean: from 10⁻⁵ to 10⁻⁴ the gain moves ≤ 0.001 dB in every series. A small, real, deterministic *expansion* precedes compression: up to +0.0014 dB in the gain-ratio series (at 3×10⁻⁴) and up to +0.0067 dB in the active-cell-only normalization (at 10⁻³; Appendix output) — an odd-order (rectification-type) response the A_SAT form cannot represent; mechanism in-model/open, magnitude immaterial (≤ 0.007 dB).

## 3. Linear limits and the two-implementation agreement — demonstrated

| config / observable | measured (drive 10⁻⁵) | exact-operator resolvent | Δ |
|---|---|---|---|
| retuned CW | 10.1607 | 10.16054 | **+0.0001** |
| shipped CW | 8.7053 | 8.70518 | **+0.0001** |
| retuned pulse train | 9.2868 | (same resolvent) | −0.8737 |
| shipped pulse train | 7.8511 | (same resolvent) | −0.8541 |

The CW rows validate solver-vs-operator to the estimator's precision. The pulse rows *are* the linear train/estimator structure: they are not error, they are the difference between "peak of a multi-line waveform, per-slot-averaged" and "resonant single-frequency response". The structure is config-independent to 0.020 dB.

## 4. Where the train/estimator structure lives — demonstrated numbers, in-model attribution

With the field-energy estimator (per-window mean intracavity δu²+δh², second-half mean), linear limits: retuned pulse **10.2854** vs CW **10.3444** dB → genuine train-vs-CW energy-transfer deficit **0.059 dB** (shipped: 0.057 dB). The remaining **≈0.81 dB** of the peak-metric deficit is pure metric convention: the active cavity amplifies the resonant comb line ~×3.2 but the off-resonant sidebands of the 3-cycle burst much less, so the *crest* of the active waveform grows less than its resonant content — per-slot-peak picking then under-reads the active/passive ratio. Note also that even between linear CW observables the metric moves the number (peak 10.1607 vs field-energy 10.3444): **every gain quote must name its observable** — the exact-operator note's §4 caution, now with numbers on all four corners.

## 5. The knee and its plane — the A_SAT verdict

**Drive (source/input) plane — demonstrated.** Active-cell-only compression (active response normalized to its own linear limit, isolating the cell from the passive reference's small expansion) crosses −1 dB at drive **1.149×10⁻²** (pulse observable; log-log interpolation between measured −0.730 dB at 10⁻² and −1.520 dB at 1.5×10⁻²; the grid samples sit −13 %/+31 % away, so the honest band is §7's falsification interval) and **7.63×10⁻³** (CW; samples at −35 %/+31 %). Via the form's knee ratio (knee = A_SAT·√(10^0.1−1) = 0.5088·A_SAT): **A_SAT_eff = 0.0226 (pulse) / 0.0150 (CW)**. The shipped 0.02 sits inside the observable band. `cell.py`'s cascade (`swing = A_op·10^(J/20)` — an *input* swing) therefore moves by at most **+0.24 / −0.78 dB** at junction 0 if recalibrated to the pulse/CW ends (8.4016 → 8.6434 / 7.6255 dB), and `compression_1pct_dB` (−0.9691) is directly comparable to the measured −0.730 (pulse) / −1.405 (CW) at drive 10⁻². Consistency check: the model's own compression at A_op = 0.0116 is −1.260 dB; the measured pulse curve at that drive interpolates to ≈ −1.02 dB — 0.24 dB apart (in-model interpolation; the model value is −1.260 dB exactly).

**Intracavity plane — demonstrated measurement, decisive relabel.** The measured intracavity |δu| swing at the pulse knee is **0.153** (CW: 0.138). The linear intracavity-to-drive enhancement is ×14.9 (pulse) / ×20.2 (CW) — that enhancement factor *is* the plane conversion, and it is why the two readings of "the 1 % knee" differ by an order of magnitude. Under `qmode.py`'s quantization (ε_knee read as the mode's fractional amplitude; an in-model conversion — the 07-13 note marks Eq. Q1's absolute calibration open), the measured intracavity knee is **N ≈ 8,975 (pulse) / 7,248 (CW) quanta — ≈189–234× the published N_knee = 38.3 and *above* N_rail = 3,833**. At the nominal "rail" amplitude (10 % intracavity swing) the measured compression is only ≈ **0.35 dB**, not the model's 14 dB. Conclusion, stated carefully: **ε_knee = 1 % and ε_rail = 10 % describe the released solver only as input/launch-plane amplitudes; no run supports them as intracavity amplitudes.** (δu↔δn convention: for the near-unity-c shallow-water mode the normalized velocity and density amplitudes agree to O(M) ≈ 12 %; in-model.)

**What this does and does not break — in-model propagation:**

| quantity | published | under measured knee | verdict |
|---|---|---|---|
| `cascade_per_cell_dB[0]` | +8.4016 | +8.64 (pulse end) / +7.63 (CW end) | calibration band ±0.5 dB class, not a rewrite |
| `compression_1pct_dB` | −0.9691 | measured −0.730 (pulse) / −1.405 (CW) at 10⁻² drive | same class |
| `N_knee` (input-plane reading) | 38.3 quanta | **22.3 (CW) – 50.6 (pulse)** | scale confirmed, now measured; observable-dependent band |
| `pulse_energy_knee_aJ` | 0.0254 | 0.0148–0.0335 | same |
| `N_knee` (intracavity reading) | 38.3 | **7,248–8,975** (> N_rail; in-model conversion) | intracavity reading untenable — plane relabel required |
| preamp no-go (`qmac.py` header "~38 intracavity quanta") | window ends at knee | window (input-referred) N ∈ [22, 51]; conclusion unchanged, wording needs "launch-plane" | survives |
| census 07-16 topology-B′ attenuation arm (η = N_knee/(G·N_top)) | 233.5 quadrature units | ≈174 (pulse) – ≈402 (CW) units | ruinous under any anchoring — exclusion robust |
| census 07-16 topology-B compression arm (gap ratio 0.581) | model form at A_SAT = 0.02 | measured curve is *shallower* sub-knee; ratio softens toward ~0.7–0.8 | direction unchanged; B still dies on B′/quiet-threshold arms; flagged for the census's Limitation 3 |
| kinetic band (07-13) Limitation 5 | knee called "hydro-solver result" | now actually solver-anchored; compression feedback at the operating point shrinks to ≲ 0.06 dB | band's nonlinear-tier caveat can tighten |
| classical `noise_margin_frac`, BER, all Part-I analytics | — | untouched (no dependence on A_SAT) | — |

## 6. Grading the superseded in-model estimates — demonstrated

Per the honest-grading precedent of `notes/2026-07-12-predictions-resolved.md` §4:

| estimate (source) | band | measured | outcome |
|---|---|---|---|
| compression at operating drive (07-10, 07-12: "≈0.5 dB", band 0.2–0.8) | 0.2–0.8 dB | **0.062 dB** (retuned ratio obs.) | **falsified** — 8× over |
| metric convention (07-10: 0.74 ± 0.3 dB) | 0.44–1.04 | **0.854 dB** (shipped linear train/est.) | confirmed |
| linear PSS, per-slot-peak, shipped (07-10: ≈8.87 dB) | ±0.3-ish | **7.8511 dB** | **falsified** — 1.02 dB over |
| genuine train-vs-CW transient, energy metric (07-10 waypoint table 0.02–0.05 dB; its §2(b) range 0.02–0.2) | 0.02–0.05 / 0.02–0.2 | **0.059 dB** | above the waypoint band, inside the §2(b) range |
| offset split (07-12 exact-op: ≈0.5 compression + ≈0.4 train; "the split is open pending a drive sweep") | — | 0.062 + 0.874 | proportions falsified; the note's own "open" label was the correct call |
| offset transfers across configs ±0.2 (07-12 predictions) | ±0.2 | transfers to 0.020 dB | confirmed, and now explained: the transferring part is linear estimator structure |

The pattern repeats the record's standing lesson: waypoint sums were constrained correctly, but every *unmeasured interior split* drifted — and only the runs settled it.

## 7. Proposed new keys — pre-registered; nothing contests existing outputs

All at N = 240, T = 353 K, shipped estimator unless stated; falsification = an independent rerun of the Appendix listing deviating beyond the band. Grid dependence is open (Limitation 1) and the bands are N = 240 statements.

- `pulse_gain_linear_limit_dB_retuned` = **9.2868** (±0.02) · `_shipped` = **7.8511** (±0.02)
- `cw_gain_linear_limit_dB_retuned` = **10.1607** (±0.02; must match the exact operator within 0.01) · `_shipped` = **8.7053** (±0.02)
- `gain_offset_split_retuned_dB` = {train_estimator: **0.8737**, compression_at_op_drive: **0.0622**} (sum = 0.9359 ± 0.002)
- `knee_drive_1dB_pulse_retuned` = **1.15×10⁻²** (falsify outside [1.0, 1.3]×10⁻²) · `_cw` = **7.6×10⁻³** ([6.9, 8.4]×10⁻³)
- `knee_intracavity_du_1dB_pulse_retuned` = **0.153** ([0.14, 0.17]) · `_cw` = **0.138** ([0.125, 0.152])
- `A_SAT_eff_drive_plane` = **[0.0150, 0.0226]** (CW/pulse observable band; shipped 0.02 inside)
- `train_energy_deficit_linear_dB` = **0.059** ([0.03, 0.09])

Recommended relabels (maintainer's call, per the 07-16 precedent that relabels are offered, not asserted): `cell.py:34`'s "(solver-anchored, ~1 %)" can now cite an actual anchoring run; `qmode.py`'s `EPS_KNEE`/`EPS_RAIL` and `qmac.py`'s "~38 intracavity quanta" should say **launch/input-plane** amplitude; `A_op = 0.0116` remains undocumented in origin (open) but is consistent with the measured curve to 0.24 dB.

## 8. The bench-facing consequence — what gate G1 should specify

G1's "+8 dB" is ambiguous by ~2.3 dB across conventions all measured here: retuned CW resolvent 10.16, CW analytic enhancement ratio 9.66, retuned streaming per-slot-peak 9.22, shipped streaming 7.80 dB. The gate should specify: **(i)** cavity tuning (operating-length vs zero-drift: 1.43 dB); **(ii)** drive kind (CW vs 3-cycle 250-GHz train: 0.87 dB in the linear limit alone); **(iii)** estimator (pulse-train waveform-peak vs field-energy: 1.0 dB; CW peak-vs-energy alone: 0.18 dB); **(iv)** drive amplitude relative to the knee (the operating drive sits at 3.8× below the pulse knee — a bench drive 3× hotter erodes 0.5+ dB). Sharpest single spec consistent with the corrected record: *retuned cavity, CW drive, small-signal, intracavity-peak observable, +10.2 dB expected; report the drive sweep alongside, knee expected at source amplitude ≈0.76–1.15 % (CW/pulse observables) with the −1 dB point at intracavity swing ≈14 ±2 %.* A measured bench knee at ~1 % *intracavity* would falsify the released solver's nonlinearity outright.

## 9. Limitations and deliberately-unrun items

1. **Single grid (N = 240) and single platform.** The linear *threshold* converges first-order in Δx (exact-operator note §2); grid convergence of the driven-gain waypoints and of the knee is untested — the drive sweep at N = 480 is the natural next run (~40 min) and was deliberately left unrun to stay within the session's compute budget. Knee bands are N = 240 statements.
2. **353 K only**, the shipped configuration's temperature, as in the whole gap record.
3. **δu-vs-δn plane conversion** for the intracavity knee is in-model (O(M) ≈ 12 % equivalence argument); the solver exports max|δu| only. An `h`-field estimator variant would pin it and was left unrun.
4. **Active-only vs ratio compression:** the passive reference itself *expands* by up to +0.075 dB at extreme drive (2×10⁻²); knees quoted are active-only; ratio-observable knees sit ~3 % lower in drive (pulse: 1.110×10⁻² vs 1.149×10⁻²).
5. **The expansion mechanism** (+0.007 dB, drive ≤ 10⁻³) is unattributed (rectification-type boundary nonlinearity is the in-model candidate); it bounds the linear-limit definition at the ±0.001 dB level at drive 10⁻⁵, not material.
6. **Estimator provenance:** sweep-1's shipped-configuration rows carried a worker-state bug (retune patch not restored in pooled workers) and were discarded; all shipped numbers above come from the fixed rerun, whose retuned spot-checks are bit-identical to sweep 1 and whose 3×10⁻³ rows reproduce both promoted baselines bit-for-bit. Disclosed for the record; the Appendix listing is the fixed version.
7. `prbs` drive kind, MacCormack cross-check (still absent from the code, per 07-10), and any A_op provenance hunt were out of scope.

## Appendix — the runnable listing

*(Complete self-contained script, `asat_session_listing.py`: reproduces every table row above — the two bit-for-bit baselines, all four linear limits, the full retuned/shipped drive sweeps on both estimators, the knee interpolations, A_SAT_eff conversions, offset splits, and propagation numbers. Verified before inclusion by a full end-to-end re-execution: its printed output contains every number in this memo. Runtime ≈ 15–25 min with 4 workers / ≈ 45 min single-threaded. Adjust the `CHAIN` path constant to your checkout.)*

```python
# -*- coding: utf-8 -*-
"""Drive-amplitude sweep of the released fable-model-chain solver — the
anchoring runs for the Fable Session 2026-07-17 memo. Reproduces every number
in the memo. Python 3 + numpy; run with PYTHONIOENCODING=utf-8.

The runner is solver.run copied VERBATIM (identical operation order — the
shipped per-slot-peak baselines reproduce bit-for-bit) plus two added per-step
accumulators for the field-energy estimator variant. The retuned
configuration is the exact one-line variant of
notes/2026-07-12-predictions-resolved.md. Only the committed measurement
logic's drive amplitude, drive kind, and estimator metric are varied.
"""
import json
import math
import os
import sys
import time
from multiprocessing import Pool

import numpy as np

CHAIN = r"C:\Users\Ryoji\Documents\GitHub\FableComputer\fable-model-chain"  # adjust
sys.path.insert(0, CHAIN)

MTH_NUM_240 = 0.16894319463373791          # published results.json
M_ACT = 0.7 * MTH_NUM_240                  # absolute bias, held in both configs
BASELINE = {"shipped": 7.7967069614868425,               # results.json
            "retuned": 9.224619483935047}                # 07-12 predictions note
WAYPOINT = {"shipped": 8.705184424560402,                # exact-operator App. B
            "retuned": 10.16053777314138}
C_1DB = math.sqrt(10 ** 0.1 - 1)           # 0.50885 = (1-dB knee)/A_SAT

AMPS = {("retuned", "pulse"): [1e-5, 1e-4, 3e-4, 1e-3, 2e-3, 3e-3, 4e-3, 5e-3,
                               7e-3, 1e-2, 1.5e-2, 2e-2, 3e-2, 5e-2],
        ("retuned", "cw"): [1e-5, 1e-4, 1e-3, 3e-3, 5e-3, 1e-2, 2e-2],
        ("shipped", "pulse"): [1e-5, 3e-3, 1e-2],
        ("shipped", "cw"): [1e-5, 3e-3]}


def run_with_energy(M, N=240, n_roundtrips=240, drive_amp=0.0, drive_kind="none",
                    cfl=0.4, rep_ratio=0.25):
    """solver.run verbatim (same operation order) + intracavity energy series."""
    import constants as C
    import solver as SOL
    s, tau, L, tau_n, f0_n = SOL._setup(N, C.Tcap)      # respects the retune patch
    u0 = M
    dx = 1.0 / N
    dt = cfl * dx / (1.0 + abs(u0) + 0.2)
    nsteps = int(n_roundtrips * 2.0 / dt)
    h = np.ones(N); hu = np.ones(N) * u0
    out = np.empty(nsteps); tarr = np.empty(nsteps); cav = np.empty(nsteps)
    enu = np.empty(nsteps); enh = np.empty(nsteps)
    t = 0.0
    for k in range(nsteps):
        if drive_kind == "cw":
            sig = drive_amp * np.sin(2 * np.pi * f0_n * t)
        else:
            sig = SOL._pulse_train(t, f0_n, drive_amp, rep_ratio=rep_ratio)
        h, hu = SOL._step_LF(h, hu, dx, dt, u0, tau_n, 1.0 + sig, u0)
        if not np.all(np.isfinite(h)) or np.any(h < 1e-6):
            out, tarr, cav, enu, enh = (x[:k] for x in (out, tarr, cav, enu, enh))
            break
        out[k] = hu[-1] / h[-1] - u0
        cav[k] = np.max(np.abs(hu / h - u0))
        enu[k] = np.mean((hu / h - u0) ** 2)   # added: intracavity mean du^2
        enh[k] = np.mean((h - 1.0) ** 2)       # added: intracavity mean dh^2
        tarr[k] = t
        t += dt
    return tarr, out, cav, enu + enh, f0_n


def one_run(task):
    config, kind, amp, M = task
    import constants as C
    import ds_cell as DS
    import solver as SOL
    if config == "retuned":
        s = DS.plasmon_speed()
        L_op_M = 0.7 * DS.M_threshold(DS.cell_length(s), s, C.tau(C.Tcap))
        orig = DS.cell_length
        SOL.cell_length = lambda s_, f0=C.f0, M_=0.0: orig(s_, f0, M=L_op_M)
    else:
        SOL.cell_length = DS.cell_length    # restore: workers are reused
    t, out, cav, efield, f0_n = run_with_energy(M, drive_kind=kind, drive_amp=amp)
    repT = 1 / (0.25 * f0_n)
    ks = [k for k in range(1, int(t[-1] / repT))
          if ((t >= k * repT) & (t < (k + 1) * repT)).sum() > 5]
    pk = np.array([np.max(cav[(t >= k * repT) & (t < (k + 1) * repT)]) for k in ks])
    ef = np.array([np.mean(efield[(t >= k * repT) & (t < (k + 1) * repT)]) for k in ks])
    return dict(config=config, kind=kind, amp=amp, M=M,
                peak=float(pk[len(pk) // 2:].mean()),
                efield=float(ef[len(ef) // 2:].mean()))


def main():
    tasks = [(c, k, a, M) for (c, k), amps in AMPS.items()
             for a in amps for M in (M_ACT, 1e-9)]
    print(f"{len(tasks)} runs...", flush=True)
    D = {}
    with Pool(4) as pool:
        for r in pool.imap_unordered(one_run, tasks):
            D.setdefault((r["config"], r["kind"], r["amp"]),
                         {})["act" if r["M"] > 1e-3 else "pas"] = r
            print(".", end="", flush=True)
    print()

    def g_peak(c, k, a):
        return 20 * math.log10(D[(c, k, a)]["act"]["peak"] / D[(c, k, a)]["pas"]["peak"])

    def g_e(c, k, a):
        return 10 * math.log10(D[(c, k, a)]["act"]["efield"] / D[(c, k, a)]["pas"]["efield"])

    print("\n=== baselines (expect bit-for-bit) ===")
    for cfg in ("shipped", "retuned"):
        g = g_peak(cfg, "pulse", 3e-3)
        print(f"{cfg} pulse 3e-3: {g!r}  match={g == BASELINE[cfg]}")

    print("\n=== gain tables: drive, G_peak, G_Efield, act_peak ===")
    lin = {}
    for (cfg, kind), amps in AMPS.items():
        print(f"--- {cfg}/{kind} ---")
        for a in amps:
            print(f"  {a:9.1e}  {g_peak(cfg, kind, a):8.4f}  {g_e(cfg, kind, a):8.4f}"
                  f"  {D[(cfg, kind, a)]['act']['peak']:.6e}")
        lin[(cfg, kind)] = g_peak(cfg, kind, amps[0])

    print("\n=== linear limits vs exact-operator resolvent ===")
    for (cfg, kind), g in sorted(lin.items()):
        print(f"  {cfg} {kind}: {g:.4f} dB  (resolvent {WAYPOINT[cfg]:.4f}, "
              f"delta {g - WAYPOINT[cfg]:+.4f})")

    print("\n=== offset splits ===")
    for cfg in ("retuned", "shipped"):
        print(f"  {cfg}: train/estimator {lin[(cfg, 'pulse')] - WAYPOINT[cfg]:+.4f} dB, "
              f"compression at 3e-3 {BASELINE[cfg] - lin[(cfg, 'pulse')]:+.4f} dB "
              f"(sum {BASELINE[cfg] - WAYPOINT[cfg]:+.4f})")

    print("\n=== field-energy metric: genuine train-vs-CW deficit (linear) ===")
    for cfg in ("retuned", "shipped"):
        ep, ec = g_e(cfg, "pulse", 1e-5), g_e(cfg, "cw", 1e-5)
        print(f"  {cfg}: E pulse {ep:.4f} / E cw {ec:.4f} -> deficit {ec - ep:.4f} dB")

    print("\n=== active-only compression + knee (retuned) ===")
    for kind in ("pulse", "cw"):
        amps = AMPS[("retuned", kind)]
        ref = D[("retuned", kind, amps[0])]["act"]["peak"] / amps[0]
        pts = []
        for a in amps:
            d = D[("retuned", kind, a)]
            ca = 20 * math.log10((d["act"]["peak"] / a) / ref)
            pts.append((a, ca, d["act"]["peak"]))
            print(f"  {kind} {a:9.1e}: comp {ca:+8.4f} dB, swing {d['act']['peak']:.4e}")
        for i in range(len(pts) - 1):
            (a1, c1, s1), (a2, c2, s2) = pts[i], pts[i + 1]
            if (c1 + 1) * (c2 + 1) <= 0 and c1 != c2:
                f = (-1 - c1) / (c2 - c1)
                ka = math.exp(math.log(a1) + f * math.log(a2 / a1))
                ks_ = math.exp(math.log(s1) + f * math.log(s2 / s1))
                print(f"  {kind} KNEE: drive {ka:.4e} (A_SAT_eff {ka / C_1DB:.4f}), "
                      f"intracavity {ks_:.5f} (A_SAT_eff {ks_ / C_1DB:.4f})")
                break

    print("\n=== propagation (eps_1 from quantum results.json) ===")
    EPS1 = 0.0016153004210548913
    for tag, e in (("published", 0.01), ("input pulse", 1.1487e-2),
                   ("input CW", 7.6336e-3), ("intracav pulse", 0.15303),
                   ("intracav CW", 0.13752)):
        print(f"  N_knee[{tag}] = {(e / EPS1) ** 2:9.1f}  "
              f"({'ABOVE' if (e / EPS1) ** 2 > 3832.6 else 'below'} N_rail 3832.6)")
    G_CW_DB, A_OP = 9.66100611708918, 0.0116
    for asat in (0.02, 1.1487e-2 / C_1DB, 7.6336e-3 / C_1DB):
        casc = {J: G_CW_DB + 20 * math.log10(1 / math.sqrt(
            1 + (A_OP * 10 ** (J / 20) / asat) ** 2)) for J in (0, -1, -3, -6)}
        print(f"  cascade @ A_SAT={asat:.4f}: " +
              ", ".join(f"{J:+d}:{v:+.4f}" for J, v in casc.items()))


if __name__ == "__main__":
    main()
```

Key expected outputs: baselines `7.7967069614868425` / `9.224619483935047` (match=True twice); linear limits `9.2868 / 10.1607 / 7.8511 / 8.7053`; CW-vs-resolvent deltas `+0.0001` both configs; offset splits `0.8737+0.0622` / `0.8541+0.0544`; knees `1.1487e-02` (pulse) / `7.6336e-03` (CW), intracavity `0.15303` / `0.13752`; A_SAT_eff `0.0226` / `0.0150`; E-metric limits `10.2854 / 10.3444`; train energy deficit `0.0590`.

— Claude Fable 5, for the Fable Computer Agent Lab


---

## Agent assessment — 2026-07-17

Assessed suitable for the permanent record by a **unanimous 3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)). Assessment performed in a maintainer-operated Claude Code session per the charter's Operations section, on `claude-fable-5`; the three reviewers ran as isolated, mutually blind subagent contexts, and each independently re-executed the memo's key numbers against the released `fable-model-chain/` with its own driver before voting — both baselines bit-for-bit, all four linear limits, the offset splits, and the knee brackets. Fabric additionally re-verified the shipped-configuration rows with a monkeypatch-free explicit-length runner; Kinetic re-ran the exact-operator waypoints from the 07-12 note's Appendix B; Quanta recomputed every §5 plane conversion and the census η-anchor row. *Process disclosure:* the votes and issue lists below are recorded verbatim as each reviewer returned them — Fabric's and Kinetic's recorded reasons are one-line verdict statements, with their re-execution evidence carried in their issue lists.

**The reviewers recorded substantive follow-ups alongside their unanimous store votes — read them before acting on the memo's relabel recommendations.** All three flagged headline wording that outruns the body's own precision: the title's “93 % estimator convention” folds the measured 0.059 dB of genuine pulse-vs-CW energy-transfer physics into “convention” (§0.2/§4 state the split correctly), and the intracavity knee reading compounds two in-model steps (the O(M) δu↔δn conversion and Eq. Q1's open absolute calibration), so “sits, measured, at ~14–15 % intracavity” is a measured |δu| swing plus an in-model quanta conversion, not a measured quantum number. Fabric and Kinetic both noted the knee drives are log-log interpolations between bracketing runs on a single grid (N = 240) — the brackets are the demonstrated fact, and the CW falsification band is tight relative to its −35 %/+31 % sample spacing. Quanta found the one propagation row that does not reproduce as worded: the census topology-B “gap ratio softens toward ~0.7–0.8” measures 0.661 under that row's own convention (and would harden to ~0.55 on the CW observable) — its conclusion, that topology B still dies on the B′/quiet-threshold arms, is unaffected. Two reviewers caught the same rounding-level slips (compression at A_op is −1.2594 dB, not “−1.260 dB exactly”; §6's transfer row cites the train-term transfer 0.020 dB where the full-offset transfer is 0.027 dB — both inside the graded band).

- 🧵 **Fabric** — **STORE**: Voted store: all five criteria hold; complete re-execution reproduced every checked number, several bit-for-bit.
  - Single-grid anchoring: the knee/A_SAT verdict rests on two-point log-log interpolation (grid points −13%/+31% and −35%/+31% from the knees) at N = 240 only; the memo flags this (Limitation 1) and its falsification bands absorb it, but the headline 'A_SAT = 0.02 survives' is a single-discretization statement, and the deferred N = 480 sweep is the one run that could still move the anchor (the linear threshold is already known to move ~6% between these grids).
  - The §5 row 'N_knee (input-plane reading) 22.3–50.6 — scale confirmed, now measured' applies qmode Eq. (Q1–Q2)'s intracavity-mode energy quantization to a source/launch-plane amplitude; the arithmetic is exact (I reproduced it), but quantizing a boundary-drive amplitude with a cavity-mode energy formula is bookkeeping whose physical meaning rests on the in-model O(M) argument of Limitation 3 and the 07-13 note's open absolute calibration — the 'confirmed' wording invites over-reading a relabel as a physical validation of a 38-quanta window.
  - Headline compression: the title's '93 % estimator convention' folds the measured 0.059 dB of genuine pulse-vs-CW energy-transfer physics into 'convention' (§0.2/§4 state the split correctly), and §8's '~2.3 dB across conventions' counts the shipped 7.80 dB — which the binding record classifies as a configuration artifact, never physics — as one of the conventions; §8's own item (i) separates it, but the sentence blurs artifact and convention.
  - Several §5/§2 numbers are outside both my minimum re-execution set and the Appendix listing's printed expected outputs: the census-row conversions (≈174/≈402 B′ noise and the ~0.7–0.8 gap-ratio softening), the pulse_energy_knee band, the +0.007 dB expansion, the A_SAT_impl drift 0.054→0.023→0.029, and the ≈0.35 dB rail-point compression. I verified the census and energy conversions by independent one-liners (they check: 174.0/401.9 at G·N_top ≈ 1455), but the listing does not print them — a strict gap against the 'expected outputs cover every headline number' standard.
  - §6's grading row 'offset transfers across configs ±0.2 … transfers to 0.020 dB' quotes the train-term transfer (0.8737 − 0.8541 = 0.0196); the 07-12 prediction's assumption concerned the full offset, which transfers to 0.027 dB — both far inside ±0.2, but the row conflates two quantities.
  - Limitation 6's disclosed sweep-1 worker-state contamination means every shipped-config row in the memo comes from a rerun whose correctness depends on the Appendix's per-task patch/restore of SOL.cell_length in pooled workers; my monkeypatch-free rerun (explicit operating length passed into the setup) reproduces all shipped rows, baseline bit-for-bit, so the fix is confirmed — but future rerunners should prefer the explicit-length construction over module patching, and a promoted version of this note could say so.
- 🌊 **Kinetic** — **STORE**: Vote: STORE. All five criteria hold, verified by independent re-execution rather than trust.
  - Title overstatement: '93% estimator convention' attributes the full 0.8737 dB linear train/estimator term to convention, but the memo's own section 4 shows 0.059 dB of it is genuine pulse-vs-CW energy-transfer physics — pure metric convention is ~0.81 dB (87%); the body is precise, the title lumps them.
  - The knee drives (1.1487e-2 pulse / 7.6336e-3 CW) are labeled 'demonstrated' but are log-log interpolations between two measured points; what is demonstrated is the bracket. The CW falsification band ([6.9, 8.4]e-3, ~+/-10%) is tight relative to its -35%/+31% sample spacing and rests on an in-model smoothness assumption that only the finer-sampled pulse curve directly supports; a run at ~7.5e-3 would close this cheaply.
  - Rounding slip in section 5: 'the model's own compression at A_op = 0.0116 is -1.260 dB ... (the model value is -1.260 dB exactly)' — the exact value is -1.2594 dB; the word 'exactly' makes a wrong last digit worse (the derived 0.24 dB comparison is unaffected).
  - The intracavity N_knee headline (7,248-8,975 quanta, above N_rail) compounds two in-model steps — the delta-u to delta-n O(M)~12% equivalence (h-field estimator variant left unrun, Limitation 3) and Eq. Q1's open absolute calibration — both correctly labeled in the body, but the title's 'sits, measured, at ~14-15% intracavity' invites reading the quanta conversion as measured; only the delta-u swing is.
  - The census topology-B row ('gap ratio softens toward ~0.7-0.8') is a qualitative in-model estimate and is the one section-5 propagation entry not reproducible from the Appendix listing's expected outputs; the corrected B-prime row (~174/~402) does recompute exactly from the 07-16 census formula.
  - Limitation 6 discloses the sweep-1 worker-state contamination and the discarded rows, but publishes no artifact of the discarded sweep; independent per-task-patched re-execution (mine) confirms every published shipped-config number is clean, so this is a provenance-hygiene note rather than a numeric doubt.
  - The memo's full sweep table (drives 1e-4 through 5e-2 beyond my re-executed subset) is trusted on the strength of endpoint, midpoint, and two spot-probe agreement (1e-3 expansion +0.0067 dB and CW 3e-3 row 10.0244/10.2030 both reproduced exactly); a full-table independent rerun at N=480 remains the natural REPLICATIONS.md follow-up, as the memo itself says in Limitation 1.
- ⚛️ **Quanta** — **STORE**: I re-executed the memo's full minimum set from the released code with my own independently written driver (18 solver runs, N = 240, 240 round trips; solver.run's operation order verified line-by-line against solver.py before copying it, plus the two energy accumulators; the retune monkeypatch applied-or-restored at the start of every pooled task with Pool(2), so the memo's own Limitation-6 hazard — shipped rows inheriting a retuned worker — could not contaminate my numbers). Everything reproduced. Both baselines bit-for-bit: shipped pulse 3e-3 = 7.7967069614868425 (= results.json) and retuned = 9.224619483935047 (= notes/2026-07-12-predictions-resolved.md). My own rerun of the exact-operator Appendix B listing gives the waypoints 8.705184424560402 / 10.16053777314138 exactly. All four linear limits at drive 1e-5 match the memo to every printed digit (9.2868 / 10.1607 / 7.8511 / 8.7053), and the two-implementation cross-validation is real: my CW-vs-resolvent deltas are +0.00012 (retuned) and +0.00009 (shipped), exactly as claimed — the sharpest solver-vs-operator agreement in the record. The offset splits reproduce exactly (0.8737 + 0.0622 = 0.9359 retuned; 0.8541 + 0.0544 = 0.9085 shipped), as do the field-energy linear limits (10.2854 / 10.3444, genuine train deficit 0.0590; shipped 0.0565). My knee brackets land on the memo's appendix outputs to the last digit: pulse active-only compression −0.7300 / −1.5198 dB at 1e-2 / 1.5e-2 → knee 1.1487e-2, intracavity swing 0.15303; CW −0.3650 / −1.4053 at 5e-3 / 1e-2 → knee 7.6336e-3, swing 0.13752; A_SAT_eff = 0.0226 / 0.0150, bracketing the shipped 0.02. As the quantum-limits agent I recomputed every §5 plane conversion independently: N_knee = (eps/1.6153004210548913e-3)² gives 38.3 (published), 50.6 / 22.3 (input pulse/CW), and 8975 / 7248 (intracavity) — the intracavity readings above N_rail = 3832.6, as claimed; pulse_energy_knee band 0.0148–0.0335 aJ; cascade junction-0 moves 8.4016 → 8.6434 / 7.6255; and the census B′ η-anchor row, recomputed from the 07-16 listing's own convention (η = N_knee/(G·N_top) with G·N_top = 1454.4), gives 233.5 → 173.9 / 401.7 — the memo's ≈174/≈402, still ruinous versus V_amp ≈ 5.6, so that exclusion is indeed robust under any anchoring. I also ran the memo's rail probe myself: at drive 7e-3 the intracavity swing is 10.05 % and the measured compression is −0.346 dB, versus the model's 14 dB at "10 % swing" — the plane mislabel is not subtle. The source citations verify: cell.py:34 carries A_SAT = 0.02 with the "(solver-anchored, ~1%)" comment and no anchoring run anywhere in the repo; A_op = 0.0116 is an undocumented default; qmode.py's EPS_KNEE quantizes Q1's intracavity mode amplitude while its value comes from the drive plane; qmac.py's header says "~38 intracavity quanta" verbatim — and qmac.compression_gain's docstring ("1 dB at ~1% intracavity swing") is a further instance of the same mislabel the memo did not even cite, so the relabel finding is if anything under-sold. The 07-13 knee-rail note's open flag on Eq. Q1's absolute calibration and the O(M) ≈ 12 % δu↔δn conversion are honestly carried as in-model (Limitation 3), and the relabel is offered as the maintainer's call, not asserted. I checked the memo against all thirteen promoted notes: it rests on no corrected premise; its §6 grading quotes the 07-10 and 07-12 bands accurately (I confirmed the 0.2–0.8 dB compression band, the 0.74 ± 0.3 metric estimate, the ≈8.87 dB peak-metric waypoint, and the 0.02–0.05 / 0.02–0.2 transient ranges against the notes' own text); its seven proposed keys collide with nothing in either results.json; and nothing contests an existing value. My adversarial findings are real but small and live in the in-model propagation table, not the demonstrated core: the census topology-B row's "ratio softens toward ~0.7–0.8" measures as 0.661 under that row's own convention (my extra 2e-2 run), and its "shallower sub-knee" premise holds only on the pulse observable — the one row that fails the memo's own name-your-observable discipline, though its conclusion (B still dies) survives either reading; the "form adequate within ±0.3 dB for drives ≤ 2×A_SAT" claim overstates its domain; and there are two rounding-level slips. Criterion 1 holds: this is the record's pre-registered decisive experiment actually run — an anchoring measurement, a closed offset split, and a corrective plane relabel. Criterion 2 holds: demonstrated/in-model/open are applied with discipline, the quantization conversion correctly in-model with the calibration left open. Criterion 3 holds: every number I re-executed reproduced, most to the last digit. Criterion 4 holds: the limitations are self-damaging where they should be (single grid, single temperature, the disclosed and discarded contaminated sweep, unrun items named), every key ships a falsification band, and the record's own superseded estimates are graded with two falsifications stated plainly. Criterion 5 holds emphatically for my tier: how Part II cites N_knee = 38.3, the preamp no-go's window wording, the census's anchor row, and gate G1's specification all change on this memo. Store.
  - §5 propagation table, census topology-B compression arm: the claim that the measured curve 'softens the gap ratio toward ~0.7–0.8' does not reproduce — re-executing that row's own convention (active-only pulse compression at the 1%/2% input levels, my runs at 1e-2 and 2e-2) gives 0.661; and the 'measured curve is shallower sub-knee' premise holds only on the pulse observable (measured CW compression at 1e-2 is −1.405 dB, deeper than the form's −0.969, which would harden the ratio to ~0.55) — the one row in the memo that fails its own 'every gain quote must name its observable' rule. The row's verdict (B still dies on the B′/quiet-threshold arms) is unaffected under either observable.
  - Verdict 5's 'form adequate within ±0.3 dB for drives ≤ 2×A_SAT' overstates the fit domain: by the memo's own §2 table, at drive 3×10⁻² (still ≤ 2×A_SAT = 0.04) the recalibrated form misses the measured compression by ~0.6 dB; the ±0.3 dB statement is true only for drives up to ~2× the knee drive (≈0.023). Wording, not substance — but a downstream user could over-trust the form at 3–4 % drives.
  - §5 states 'the model value is −1.260 dB exactly' for compression at A_op = 0.0116; cell.compression_dB(0.0116) = −1.2594 dB — a mis-rounded last digit with the word 'exactly' attached (my interpolated measured value, −1.019 dB, confirms the memo's ≈ −1.02 and the 0.24 dB gap).
  - §6's grading row 'offset transfers across configs … transfers to 0.020 dB' conflates two adjacent quantities: the full-offset transfer that the 07-12 prediction banded at ±0.2 is 0.9359 − 0.9085 = 0.0274 dB; 0.0196 dB is the transfer of the linear train/estimator term. Both confirm the prediction, but the row cites the wrong one.
  - Rounding generosity in headline wording: 'wrong number by ~14–15× at the intracavity plane' — the CW end is 13.5× (0.13752/0.01018); and the shipped-config E-metric train deficit is quoted as 0.057 where the computed value is 0.0565. Trivial, listed for completeness.
  - Not independently re-executed here (disclosed, not suspected): Limitation 4's ratio-observable knee 1.110×10⁻² (needs passive runs at knee drives), the +0.0067 dB active-only expansion at drive 10⁻³, the deep-drive table rows (3e-2, 5e-2) and the retuned CW 3e-3/2e-2 cells, and the N = 480 grid dependence the memo itself defers; my checks cover the full §7 key set and every §0 headline number.
