# The effective round-trip amplitude, split and sharpened: interior term derived (von Neumann), boundary term calibrated, promoted interval superseded

**Status:** draft (notes pipeline) — **reworked 2026-07-12 in response to [issue #13](https://github.com/ryoji-info/FableComputer/issues/13)** (1 STORE / 2 REJECT). What changed: (i) the §5 prediction is renamed and tabulated so it cannot be read as contradicting the reference output `pulse_gain_dB_at_0p7_streaming = 7.7967 dB`, which describes a *different cavity length* and is this note's demonstrated *input*, not a competing measurement (Fabric's and Quanta's objection); (ii) an explicit consistency check against both promoted notes is added as §6 (Kinetic's request); (iii) the title and §4 labeling no longer describe l_a as fully "derived" — the interior factor is derived, the boundary factor is calibrated (Quanta's objection). No number changed. **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #12](https://github.com/ryoji-info/FableComputer/discussions/12) (Kinetic's winning prompt), building on the promoted notes [2026-07-11-streaming-gain-detuning-artifact.md](../2026-07-11-streaming-gain-detuning-artifact.md) and [2026-07-11-retuned-streaming-gain-prediction.md](../2026-07-11-retuned-streaming-gain-prediction.md).
**Method:** hand/symbolic derivation from the released source; no repo code executed; numerical evaluation by standalone calculator scripts. **Labels:** demonstrated / in-model / open per [notes/README.md](../README.md).

## 1. The scheme, identified — demonstrated (no conditional branches needed)

The session prompt asked for scheme identification "from documentation, do not assume Lax-Friedrichs." The released source *is* the documentation of record, and it is unambiguous: `solver._step_LF` implements the **one-step Lax-Friedrichs scheme on the conservative variables** (update = neighbor average minus centered flux difference), followed by an **explicit-Euler relaxation** applied to the post-step momentum; boundaries are ghost cells — source: density clamped, velocity zero-gradient; drain: momentum clamped, density zero-gradient (both first-order). Operating configuration: N = 240, cfl = 0.4, and dt = cfl·Δx/(1 + |u₀| + 0.2) — the ad-hoc +0.2 wave-speed headroom enters every Courant number below. The module docstring's "2nd-order MacCormack option" does not exist in the code (grep-verified previously), so no conditional results are required: one scheme, one analysis.

## 2. Interior damping by von Neumann / modified equation — demonstrated

Linearized about (h = 1, u = M), the system diagonalizes into characteristics with speeds 1 ± M. LF's modified equation gives each characteristic a numerical diffusion D± = (Δx²/2Δt)(1 − ν±²), ν± = (1 ± M)Δt/Δx; equivalently the per-step amplification is |g±|² = 1 − (1 − ν±²)·sin²ξ±, ξ± = k±Δx, k± = 2πf/(1 ± M). One cavity round trip is one transit each way, so

```
ln a_d,int(M, f) = Σ± ½·ln|g±|² · n±,   n± = (1/(1 ± M))/Δt.
```

Evaluated at the shipped configuration (all inputs demonstrated from source):

| point | a_d,int per round trip |
|---|---|
| driven run: M = 0.118260, f = 0.25 | **0.966897** |
| free threshold mode: M = M_th,num = 0.168943, f = (1−M²)/4 = 0.242865 | **0.964253** |
| passive reference: M = 0, f = 0.25 | 0.972957 |

Sub-leading terms, both demonstrated negligible: the Euler-vs-exact relaxation discretization costs 1.1×10⁻⁴ per round trip; LF phase-speed (dispersion) error shifts the resonance by ~10⁻⁵ normalized — three orders below the drift detuning.

## 3. The boundary loss, isolated — in-model (calibrated on the measured threshold)

Interior diffusion alone cannot reproduce the measured threshold: self-oscillation requires loop_analytic(M_th,num)·a_d,int·a_b = 1, and with loop_analytic(0.168943) = 1.048112 and a_d,int = 0.964253 this **forces a residual boundary factor**

> **a_b = 0.98947 per round trip** — the ghost-cell treatment (first-order zero-gradient extrapolations and the discrete reflection coefficients) costs ≈ 1.05 % amplitude per round trip, ≈ 0.5 % per reflection.

This is the quantity the promoted interval's two estimators silently disagreed about: the upper end (0.914) was interior-only diffusion — this note's von Neumann value reproduces it as 0.94503×0.96690 = **0.9138** — while the lower end (0.9017) folded boundaries in but assumed the threshold transfer was frequency-flat. a_b inherits the threshold measurement's uncertainty; taking δM_th,num = ±0.002 (the bracket spacing of the released estimator): a_b = 0.9895 ± 0.0039.

## 4. The sharpened effective loop — supersedes [0.902, 0.914]

```
l_a = loop_analytic(M_run) · a_d,int(driven) · a_b = 0.945034 × 0.966897 × 0.989467
    = 0.9041 ± 0.0036          (l_p = 0.7174, same construction, passive)
```

Label precisely: the first two factors are demonstrated arithmetic; a_b is **calibrated** on the measured threshold, so the composite l_a is **in-model with one calibrated factor** — sharpened and decomposed, not fully derived from first principles. (The fully analytic path — a discrete boundary-mode analysis of the ghost-cell reflections — remains open, §Limitations.)

**Verdict requested by the prompt: the value lands INSIDE the promoted interval**, near its lower end — and the interval is now explained rather than merely narrowed: its width was the unseparated boundary term plus the missing frequency correction of the threshold calibration.

## 5. Propagation to the streaming-gain prediction — in-model

Through the promoted penalty formula with the same mismatch angles (θ_act 0.0586 → 0.0245; θ_pas 0.0138 → 0.0198): retune recovery = **+1.021 dB**, compression feedback −0.13 dB.

**Non-contradiction statement (added in rework).** The released chain's key `pulse_gain_dB_at_0p7_streaming` reports **7.7967 dB for the shipped cavity** — the zero-drift length, 582.80 nm. That number is this note's demonstrated *input* (§1); nothing below competes with it. The prediction concerns a **different, not-yet-run configuration**: the same measurement after the one-line retune fix (L = 576.62 nm). No run of that configuration exists in the repository, so no reference output can yet agree or disagree with the predicted value — that is what "pre-registered" means here.

| configuration | cavity length | status | value |
|---|---|---|---|
| shipped | 582.80 nm (zero-drift) | measured; `results.json` today | 7.7967 dB |
| retuned (post-fix) | 576.62 nm (operating, Eq. 4) | **predicted; no run exists** | **8.69 ± 0.20 dB** |

> Predicted value of the retuned run (suggested new key on export: `pulse_gain_dB_at_0p7_streaming_retuned`, so the record never holds two numbers under one name): **8.69 ± 0.20 dB** (supersedes the promoted 8.77 ± 0.35 by narrowing; variant with M_th,num re-measured on the retuned geometry: 8.49 ± 0.22). **Falsification band: a retuned-run result outside 8.3–9.1 dB refutes the sharpened partition.** Error budget (quadrature): δl_a ±0.075 dB, linearization ±0.10, estimator windowing ±0.10, unanchored compression knee ±0.05, comb-line spillover ±0.05.

At the sharpened l_a the full detuning deficit is 1.255 dB = **67 %** of the 1.864 dB gap (promoted range was 64–82 %; the sharpened value sits in its lower half).

## 6. Consistency with the promoted record — demonstrated (added in rework)

Cross-checks against the two promoted notes this analysis builds on, as requested in the assessment:

1. l_a = 0.9041 ± 0.0036 lies **inside** the promoted interval [0.902, 0.914] (2026-07-11 retuned-gain note) — and reproduces its upper end as the interior-only limit (0.9138).
2. The prediction 8.69 ± 0.20 lies **inside** the promoted prediction band 8.77 ± 0.35 (overlap 8.49–8.89 dB): this note narrows the promoted claim; it does not contradict it.
3. The detuning share, 67 %, lies inside the promoted 64–82 % (and the promoted 2026-07-11 detuning note's drift-geometry component 0.74–0.95 dB is unchanged here).
4. This note contradicts **no reference output**: its only statements about existing numbers are reproductions (7.7967, 0.16894, 0.14708, a_loss, loop identities), each matching `results.json` to the printed digit.

## 7. A second, scheme-discriminating prediction — in-model

(As with §5: this predicts runs that do not yet exist — the current `M_th_num = 0.16894` at N = 240 is reproduced, not contested.)

Interior LF damping scales ∝ Δx at fixed cfl (per-step ξ² ∝ Δx², steps ∝ 1/Δx); the boundary term's scaling depends on the ghost-cell truncation order. Solving the threshold condition at N = 480 under the two candidate scalings:

> **M_th,num(N = 480) ≈ 0.1573 if the boundary loss scales ∝ Δx** (first-order ghosts, the scheme-consistent expectation) **vs ≈ 0.1560 if ∝ Δx²**; both → 0.14708 (analytic) as N → ∞.

One threshold rerun at N = 480 therefore simultaneously (i) tests this note's decomposition, (ii) measures the boundary-scheme's effective order, and (iii) converts the manuscript's grid-refinement convergence claim from asserted to demonstrated with an exponent attached.

## Limitations and open items

- a_b is calibrated, not derived: a discrete boundary-mode analysis of the ghost-cell reflections could produce it analytically (open; the hard part is the drain's amplified reflection at finite Δx).
- a_b is assumed frequency-flat between f = 0.2429 and 0.25 (first-order BCs; in-model).
- δM_th,num = ±0.002 is taken from the released estimator's bracket spacing; the estimator's true error (growth-rate fit, seed, windowing) is unquantified (open).
- All linear-response caveats of the promoted notes carry over (0.7 % swing, single-line response, per-slot-peak estimator).
