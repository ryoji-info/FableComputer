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


---

## Agent assessment — 2026-07-11

Assessed suitable for the permanent record by a **3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)):

- 🧵 **Fabric** — **STORE**: The note delivers a concrete, falsifiable numeric prediction (retuned streaming gain = 8.77 ± 0.35 dB, with explicit falsification bounds ≤8.2/≥9.3 dB) derived from an analytic partition of the already-observed 1.8643 dB gap, building explicitly on the promoted note it cites. I independently re-derived several of the key arithmetic steps (θ_active/θ_passive from the stated f_line, T_rt, δ_relax formulas; M_ex from the cell_length_operating/zero_drift ratio; M_run from 0.7·M_th_num) and they reproduce the note's reported values to the stated precision, and the two headline gain numbers (7.7967069614868425, 9.66100611708918) match the reference model-chain output exactly. Epistemic labels (demonstrated/in-model/open) are applied consistently and with justification at each step, including a correctly scoped 'demonstrated' exclusion of the Caves/Haus-Mullen bound as irrelevant to mean gain. Limitations (unanchored knee parameter, open residual split, dependence on re-measuring M_th,num, cascade table being a disjoint closed form) are stated candidly rather than papered over, and §6 gives an honest, reasoned ranking of follow-up experiments rather than padding. This is durable, actionable WP1 material: it tells a future model-chain run exactly what number to check and how the prediction would be falsified.
  - The l_a ∈[0.902,0.914] and l_p∈[0.711,0.721] bands, which dominate the uncertainty, are asserted from 'threshold calibration' and 'Lax-Friedrichs damping at the carrier' without showing the derivation in this note, so a reader cannot independently verify the dominant error source.
  - The A_SAT=0.02 knee model used for the compression correction is explicitly flagged by the note itself as unanchored, so the ±0.1-0.17 dB compression term rests on a parameter the project has not calibrated.
  - The consistency check against an '≈8.9 dB' waypoint from the 2026-07-10 promoted note could not be verified against material provided here and is taken on trust.
- 🌊 **Kinetic** — **STORE**: The note passes a stringent numeric audit: every figure it borrows from the model chain (582.7994913552518 nm, 576.62157290196 nm, M_th_num=0.16894319463373791, cw gain 9.66100611708918 dB, streaming gain 7.7967069614868425 dB) matches the provided reference outputs exactly, and the internal algebra (θ_active, θ_passive, drift-only vs relax-only decomposition, the retuned f0_n≈0.2473) recomputes consistently by hand. It delivers a genuine checkable result: a partitioned account of the 1.8643 dB gap plus a falsifiable numeric prediction (8.77±0.35 dB, with explicit falsification bounds) for a specific, well-defined code fix -- exactly the kind of pre-registered check future WP2 runs should be held to. Epistemic labels (demonstrated/in-model/open) are applied per-line-item rather than blanket, the Caves/Haus-Mullen exclusion is argued rather than asserted, and limitations (unanchored knee model, open residual split, dependence on l_eff bands) are stated without softening the headline number. It builds explicitly on the promoted 2026-07-11 detuning-artifact note and a 2026-07-10 promoted waypoint rather than restating them, and its cross-check (two independent routes converging near 8.9 dB) adds real evidential weight. Remaining weaknesses are honestly flagged rather than hidden, which is the behavior the storability standard is meant to reward.
  - The l_eff bands (l_a, l_p) that dominate the uncertainty are quoted from prior work but not re-derived in this note, so a reader cannot independently audit the single largest source of error here.
  - δ_relax = 0.0011 is asserted as an 'exact linear BVP' value without showing the computation in this note; traceability to the cited promoted note should be double-checked before this becomes load-bearing for the falsification test.
  - The residual bucket (metric convention / compression / diffusion, 0.34-0.67 dB) is left explicitly unresolved -- appropriately labeled open, but it means the note's central number still carries a real unresolved ambiguity pending the proposed follow-up run.
- ⚛️ **Quanta** — **STORE**: Spot-checking the arithmetic against the supplied model-chain reference (L0=582.7995 nm, L_op=576.6216 nm, M_th,num=0.168943, cw gain=9.6610, pulse gain=7.7967) confirms the note's setup numbers and several derived mismatch angles (θ_active=0.05858, drift-only 0.04456, L_op/L0 ratio 0.98940) reproduce exactly, which is unusually rare and a strong sign of genuine derivation rather than assertion. The Caves/Haus-Mullen exclusion argument (amplifier quantum limits bound noise/variance, not mean gain) is physically correct, cleanly demonstrated, and does real work guarding against exactly the kind of quantum-mislabeling this project must avoid. Labels are applied consistently and non-trivially: the Caves row is marked demonstrated while the gap partition is honestly kept in-model with explicit, propagated uncertainty bands, and the note ends with a genuinely falsifiable numerical prediction (8.77±0.35 dB, falsified by ≤8.2 or ≥9.3 dB) plus a variant and named limitations — this is a checkable, durable result a WP5 rerun could directly test or refute. The main weakness is that the l_a/l_p effective-loop estimates (0.902–0.914 active, 0.711–0.721 passive), which dominate the uncertainty budget, are asserted from unshown 'threshold calibration' and 'Lax–Friedrichs damping' methods without enough detail to independently reproduce them, so the partition's precision rests partly on unverifiable inputs even though the note is transparent about this being the dominant error source. On balance the substance, honesty, and falsifiability clear the bar despite that gap.
  - l_a/l_p effective round-trip amplitude bands are stated as 'two independent estimates' without showing the calibration/damping calculation, so a reader cannot independently verify the dominant source of uncertainty
  - Several ranges (compression feedback, residual split) are combined additively across sections without a stated error-propagation rule (worst-case vs quadrature), which could overstate or understate the final band
  - Passive θ_relax arithmetic (0.01382 vs a naive recompute of ~0.0140) has a small unexplained discrepancy that isn't flagged, suggesting an unstated passive-config detail
