# The boundary factor resolved by exact construction: no closed form exists, no calibration is needed, and the +15 % threshold offset is now derived to 0.1 %

**Status:** draft (notes pipeline). **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #17](https://github.com/ryoji-info/FableComputer/discussions/17) (Kinetic's winning prompt: derive the ghost-cell boundary reflection factor exactly, or show rigorously that no single scheme-derived value exists; recombine; confront the 1.8643 dB gap).
**Method:** the linearized one-step operator of the released scheme — Lax–Friedrichs interior + explicit-Euler relaxation + the documented ghost cells, at the shipped N = 240, cfl = 0.4, cmax = 1+|u₀|+0.2 — is constructed **exactly** as a 480×480 matrix from the update algebra alone (my own construction, evaluated with standalone linear algebra; no repo code executed; no scheme detail assumed beyond the released source). Spectral radius → free modes and thresholds; resolvent at the drive frequency → exact driven response. **Labels:** demonstrated / in-model / open per [notes/README.md](../README.md), including the pre-registered-prediction naming rule.

## 1. Answer to the either/or: both — demonstrated

**(b) No single closed-form boundary factor exists.** The ghost-cell conditions couple the two characteristic families to the Lax–Friedrichs checkerboard (odd–even) modes, so the discrete reflection coefficients are roots of a quartic with no simple closed form, and the boundary defect is **bias- and frequency-dependent**, not a constant of the scheme: the exact analysis gives a per-round-trip boundary factor ≈ **1.000000 for the passive cavity** (the passive exact loop factors as l_p = 0.724999 = a_loss × interior von Neumann factor to 4×10⁻⁶ — the boundaries are lossless at M = 0) but **0.99549 at the operating bias** — the loss is *drift-induced*, living in the drain's amplified reflection at finite Δx. Any scalar "a_b" is therefore a fiction; the promoted/drafted calibrations (0.98947 ± 0.0039) were absorbing frequency-model error, not boundary physics.

**(a) The scheme-derived value nevertheless exists uniquely, with no free calibration**: it is the spectral radius of the exactly constructed operator. All quantities below follow from that construction alone.

## 2. Validation — the strongest available: the threshold offset is now derived

| quantity | exact operator | released chain | label |
|---|---|---|---|
| M_th,lin (N = 240) | **0.168764** | measured M_th,num = 0.168943 | demonstrated |
| relative agreement | **0.11 %** | (analytic M_th = 0.147083) | demonstrated |

The entire "+15 % numerically-diffused threshold" of Part I §7.3 is reproduced from first principles by the linear discrete operator; the unexplained residue of the released measurement is 1.8×10⁻⁴ in M (nonlinearity of the growth-rate fit, seed, windowing). Continuum check: M_th,lin = 0.16876 / 0.15883 / 0.15402 at N = 240/480/960 — first-order convergence toward the analytic 0.14708 (Richardson at 960: ≈ 0.149), which converts Appendix A's convergence claim into a demonstrated statement **with an exponent ≈ 1**.

## 3. Exact operating-point quantities — demonstrated (within the linear model)

| quantity | value | supersedes |
|---|---|---|
| l_a (effective loop, shipped config, M = 0.118260) | **0.910958** | interval [0.902, 0.914]; the composite 0.9041 of the von Neumann draft |
| exact discrete line center (active) | **0.244513** | 0.245405 (BVP estimate) |
| l_p / passive line center | 0.724999 / 0.247862 | 0.7174 / 0.24893 |
| active boundary factor (derived, not calibrated) | 0.99549 | calibrated 0.98947 ± 0.0039 |

## 4. Confronting the 1.8643 dB gap — the requested recombination

Exact driven steady state (resolvent at the shipped drive f0_n = 0.25, source-ghost drive, **the same max|δu| metric as the released `cav` estimator**):

```
exact linear CW response, shipped config:  8.7052 dB
CW analytic reference:                     9.6610 dB   →  linear-numerics share of the gap: 0.9558 dB
released streaming measurement:            7.7967 dB   →  residual (train + nonlinearity + estimator): 0.9085 dB
```

So the exact linear discretization + detuning explains **0.956 dB** of the 1.8643 dB gap — neither closing it nor overshooting — and leaves a 0.909 dB residual that is *not* linear numerics: in-model, ≈ 0.5 dB drive-amplitude compression (0.73 % swing against the 1 %-knee) plus ≈ 0.4 dB pulse-train/per-slot-estimator structure; the split is open pending a drive sweep. One observable caution the exact numbers force: the CW-analytic 9.661 is a *different observable* (enhancement ratio) from the max|δu| ratio — in the retuned configuration the exact linear ratio reaches 10.16 dB, *above* 9.661, because the passive reference detunes and mode-shape/coupling factors do not cancel; gap bookkeeping must always name its observable.

## 5. Supersessions — stated per the record-consistency standard

This note **corrects part of the now-promoted von Neumann note** ([2026-07-11 pipeline, promoted 3/3 as notes/2026-07-12-effective-loop-von-neumann.md](../2026-07-12-effective-loop-von-neumann.md)) — in the same way the detuning note corrected the promoted 2026-07-10 note. What stands there: the interior von Neumann derivation (its §2, confirmed here to 4×10⁻⁶ by the passive factorization) and the diagnosis of the interval's structure. What this note supersedes there: the calibrated scalar a_b = 0.98947 (no scalar boundary factor exists; passive ≈ 1.000000, active 0.99549); the composite l_a = 0.9041 ± 0.0036 (exact: **0.910958**); the two-branch `M_th,num(480)` prediction 0.1573/0.1560 (both branches would have been falsified by a run — replaced by prediction 1 below); and the tightened band `pulse_gain_dB_at_0p7_streaming_retuned` = 8.69 ± 0.20 (replaced by prediction 2 below — the exact recovery is larger than the single-mode penalty formula captured). The **promoted 2026-07-11 band** (8.77 ± 0.35) survives: the new central value sits in its upper half. Lesson worth recording: two layers of approximation (single-Lorentzian response; scalar frequency-flat boundary calibration) each looked individually tight and jointly drifted — the exact operator is cheap enough that it should simply be the standard tool for this class of question from now on.

## 6. Pre-registered predictions — own keys; no such runs exist; nothing here contests any existing output

1. **`M_th_num_N480` = 0.1590 ± 0.0010** (exact-linear 0.158834 plus the +1.8×10⁻⁴ nonlinear/estimator offset observed at N = 240). Falsification: outside 0.157–0.161.
2. **`pulse_gain_dB_at_0p7_streaming_retuned` = 9.05 ± 0.30** (exact retuned-config linear response 10.1605 dB, minus the measured shipped-config offset −0.9085 dB compression-adjusted by −0.199 dB). Falsification: outside 8.45–9.65. Supersedes the draft band 8.69 ± 0.20; consistent with the promoted 8.77 ± 0.35.
3. **`pulse_gain_dB_at_0p5_streaming` = 5.08 ± 0.30** (second-bias check requested by the session prompt: exact linear response 5.7307 dB at M = 0.5·M_th,num, offset −0.648 dB after compression adjustment). Falsification: outside 4.6–5.6.

The uncertainty in (2) and (3) is dominated by one assumption, stated openly: the nonlinear/train/estimator offset measured at the shipped 0.7-bias point transfers across configurations with only its compression term adjusted (±0.2 dB assigned), plus the unanchored A_SAT knee (±0.1).

## Limitations and open items

- The operator is exact for the *linearized* scheme; the released measurement includes 0.7 %-swing nonlinearity — bounded here only through the knee model.
- The offset-transfer assumption above is the open hinge of predictions (2)–(3); the drive-amplitude sweep remains the decisive experiment for it.
- The quartic/checkerboard structure of the boundary coupling is stated, not exhibited symbolically; the operator construction subsumes it, but a reader wanting the four roots explicitly must extract them from the stated 2×2 recurrence.
- All conclusions are at T = 353 K, the shipped configuration's temperature.
