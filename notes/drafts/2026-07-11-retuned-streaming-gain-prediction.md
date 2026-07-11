# Retuned-cavity streaming gain: analytic partition of the 1.86 dB gap and one falsifiable number

**Status:** draft (notes pipeline). **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #10](https://github.com/ryoji-info/FableComputer/discussions/10) (Kinetic's winning prompt), building on the promoted note [2026-07-11-streaming-gain-detuning-artifact.md](../2026-07-11-streaming-gain-detuning-artifact.md).
**Method:** hand/symbolic derivation only, per the promoted notes' standard — no code execution. All inputs are the documented solver equations, ghost-cell boundary conditions, and the linear driven-cavity response verified in the promoted note (whose eigencondition reproduces the chain's Eq. (2) term-for-term). Numerical evaluation by standalone calculator scripts.
**Labels:** demonstrated / in-model / open, per [notes/README.md](../README.md).

## 1. Setup — demonstrated

Shipped streaming run: cavity at the zero-drift length L₀ = 582.80 nm, drive carrier f0_n = f₀L₀/s = 0.25 exactly, bias M_run = 0.7·M_th,num = 0.118260, single cell (no cascade count exists — the "cascade" table is a disjoint closed form), drive_amp = 3×10⁻³, per-slot-peak metric; reported 7.7967069614868425 dB against the CW analytic 9.66100611708918 dB: **gap = 1.8643 dB**.

Linearized about (h = 1, u = M), the cavity's driven response at round-trip phase mismatch θ obeys (promoted note, exact BVP-verified):

```
penalty(θ; l) = 10·log₁₀[ ((1−l)² + 2l(1−cos θ)) / (1−l)² ]      (dB, vs on-resonance)
θ = 2π·(f_drive − f_line)·T_rt,   T_rt = 2/(1−M²)  (units L/s)
f_line = (1−M²)/4 − δ_relax,      δ_relax = 0.0011  (damping line-shift, exact linear BVP)
```

with l the *effective* round-trip amplitude of the diffused solver. Two independent estimates (threshold calibration; Lax-Friedrichs damping at the carrier): **l_a ∈ [0.902, 0.914]** (active), l_p ∈ [0.711, 0.721] (passive). The l_a range is the dominant uncertainty below; the eigencondition itself is exact for the linearized system (BC approximations contribute no error — it was derived with the solver's own ghost-cell clamps), and linearization at the ~0.7 % operating swing contributes ≲ ±0.1 dB.

## 2. Mismatch angles — demonstrated (arithmetic on the above)

| configuration | θ_active (rad) | θ_passive (rad) |
|---|---|---|
| shipped (L₀, drive 0.25) | 0.05858 (drift-only part: 0.04456) | 0.01382 (relax only) |
| retuned to exported L_op = L₀(1−M_ex²), M_ex = 0.10296 | 0.02451 | 0.01977 |

The L_op retune shrinks the geometric mismatch by the factor (M_run² − M_ex²)/M_run² = 0.242 but does **not** remove the damping line-shift (δ_relax survives in both), and it slightly detunes the passive reference (which was perfectly tuned at L₀). A fully consistent retune would use L(M_run) or, equivalently, drive at the measured line center.

## 3. Gap partition — in-model (l_eff-banded), Caves term demonstrated

| component of the 1.8643 dB gap | size (dB) | share | label |
|---|---|---|---|
| drift-geometry detuning (artifact proper; removed by the L_op fix) | 0.74–0.95 | 40–51 % | in-model |
| damping line-shift + its cross-term with the drift detuning (in-model physics the on-resonance CW formula ignores; removed only by driving the actual line center) | 0.46–0.57 | 25–31 % | in-model |
| **total detuning deficit** | **1.20–1.53** | **64–82 %** | in-model |
| residual (metric convention + finite-drive compression + diffusion residual, jointly; genuine streaming transient ≲ 0.05 inside it) | 0.34–0.67 | 18–36 % | in-model sum; split open |
| Caves/Haus–Mullen amplification floor | 0.000 | 0 % | demonstrated |

Uncertainty on the detuning fraction: ±0.16 dB from the l_a band, ±0.1 dB linearization, negligible from the BC-exact eigencondition ⇒ **detuning = 1.36 ± 0.20 dB (73 ± 11 % of the gap)**.

## 4. The falsifiable prediction

**Code fix defined as:** `solver._setup` uses `L = cell_length(s, M=0.7*M_th)` (the exported 576.62 nm) for both the active and passive runs — f0_n then becomes 0.2473 automatically — holding the absolute bias M = 0.118260, drive_amp = 3×10⁻³, N = 240, and the estimator fixed.

Linear recovery: penalty(θ_a: 0.0586→0.0245) + passive change = **+0.98 to +1.23 dB**; less compression feedback from the ~12 % higher intracavity swing (knee model): **−0.10 to −0.17 dB**. Prediction:

> **pulse_gain_dB_at_0p7_streaming (retuned) = 8.77 ± 0.35 dB** (band 8.61–8.93 from the l_eff and compression ranges, widened for linearization/estimator).
> Variant: if the fix also re-measures M_th,num on the retuned geometry (bias drops to ≈ 0.1170), subtract 0.20 dB: **8.57 ± 0.35 dB**.
> **Falsification:** a retuned run reporting ≤ 8.2 dB or ≥ 9.3 dB refutes this partition. Digit-level precision (results.json style) is not analytically attainable; the error bar is the honest statement, and its width is dominated by the effective-loop estimate that the same run's line shape would pin (fit θ_HW = (1−l)/√l).

Consistency check (in-model): the prediction lands on the independently computed on-resonance linear steady-state waypoint (≈ 8.9 dB, peak metric, promoted 2026-07-10 note) minus the residual detuning and compression — two routes, one answer.

## 5. Residual assessment: discretization vs Caves vs neither — from the equations alone

**Caves/Haus–Mullen: excluded, demonstrated.** Both gain figures are deterministic classical mean-field quantities; the amplifier bound enters variance, never mean gain (the quantum repo's own rule x → √G·x is noise-free in the mean, Fock-verified there). Even under deliberate misattribution its scale at rail signals is ≤ 0.006 dB against a ~0.5 dB residual. No parameter regime changes this.

**Δt/N discretization: plausible only as a subdominant term — open.** The residual's sign (solver below CW even after retune) and size (0.34–0.67 dB) are already accounted for, within their bars, by two *named, non-discretization* conventions: the per-slot-peak vs energy metric (~0.7 dB at the tuned linear waypoint, partially overlapping the detuning buckets) and finite-drive compression (0.2–0.8 dB), offset by the bias renormalization to M_th,num, which if anything overcompensates. A pure Δt/N artifact would have to (i) survive the threshold renormalization constructed to absorb leading-order diffusion and (ii) conspire to the same sign; nothing in the equations requires a ≳ 0.3 dB term of that kind, and nothing rules out a ≲ 0.2 dB one. Cannot be bounded further without runs.

**Neither/undiagnosed:** not needed — the budget closes within stated uncertainties.

## 6. Which follow-up has higher expected information value?

Of the two live candidates: **the Δt/N refinement rerun, by a wide margin** — the Caves-bound comparison has *zero* expected information for this gap (demonstrated above: it constrains variance, not mean gain; its "comparison" can only restate 0.000). The refinement rerun bounds the one genuinely open sub-component (the diffusion residual inside 0.34–0.67 dB).

But stated fully: the retune run of §4 dominates both — it tests this note's prediction, measures l_eff from the line shape (retiring the dominant uncertainty), and converts the largest single component of the gap (64–82 %) from in-model to demonstrated, all in one N = 240 run. The Δt/N refinement is then the natural second run; the Caves comparison should be retired as a gap hypothesis (it remains correct and load-bearing where it lives: the noise budget, Eq. 7).

## Limitations and open items

- All penalties assume the single-comb-line linear response (spillover to the n = ±1 lines ≲ 0.05 dB, promoted-note comb analysis) and the two l_eff estimators; a measured line shape supersedes both.
- The compression feedback uses the phenomenological knee (A_SAT = 0.02) the chain itself flags as unanchored.
- The prediction is for the code fix exactly as defined in §4; re-measuring M_th,num changes it by −0.20 dB (variant given), and an exact line-center retune (drive at the measured f_line) would add a further ≈ +0.2–0.3 dB beyond the L_op fix.
- The residual's internal split (metric / compression / diffusion) remains open pending the §4 run plus a drive-amplitude sweep and an energy-metric estimator variant.
