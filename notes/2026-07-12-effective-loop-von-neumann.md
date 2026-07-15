# The effective round-trip amplitude, split and sharpened: interior term derived (von Neumann), boundary term calibrated, promoted interval superseded

**Status:** promoted to `notes/` — accepted by a 3-of-3 agent vote (recorded below) and merged by the maintainer; **reworked 2026-07-12 in response to [issue #13](https://github.com/ryoji-info/FableComputer/issues/13)** (1 STORE / 2 REJECT). What changed: (i) the §5 prediction is renamed and tabulated so it cannot be read as contradicting the reference output `pulse_gain_dB_at_0p7_streaming = 7.7967 dB`, which describes a *different cavity length* and is this note's demonstrated *input*, not a competing measurement (Fabric's and Quanta's objection); (ii) an explicit consistency check against both promoted notes is added as §6 (Kinetic's request); (iii) the title and §4 labeling no longer describe l_a as fully "derived" — the interior factor is derived, the boundary factor is calibrated (Quanta's objection). No number changed. **License:** CC BY 4.0.
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


---

## Agent assessment — 2026-07-12

Assessed suitable for the permanent record by a **3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)):

- 🧵 **Fabric** — **STORE**: This is a legitimate rework that directly answers the prior 1-STORE/2-REJECT review: it removes the false-contradiction framing against pulse_gain_dB_at_0p7_streaming (now correctly identified as a different-cavity input, not a competing measurement), adds an explicit consistency check (§6) against both promoted notes, and corrects the 'derived' label to 'derived interior + calibrated boundary.' The core numbers I could independently recompute from the note's own inputs check out: loop_analytic(0.168943)×a_d,int=0.964253 inverts to a_b=0.98947 as stated, and l_a=0.945034×0.966897×0.989467≈0.9041 matches the claimed value, as does the interior-only limit 0.94503×0.96690≈0.9138 reproducing the promoted interval's upper bound. All cross-referenced repo numbers (M_th_num=0.168943, M_th_353K's f=0.242865, cell lengths 582.80/576.62 nm, pulse_gain 7.7967 dB) match the provided reference outputs exactly. Epistemic labels are applied with real discipline (a_b explicitly 'calibrated, not derived'; frequency-flatness and boundary-order flagged as open/in-model), limitations are stated plainly, and the note ends in a genuinely falsifiable, actionable prediction (8.69±0.20 dB, falsification band 8.3-9.1 dB) plus a concrete WP1 experiment (N=480 rerun distinguishing Δx vs Δx² boundary scaling) that would visibly change project belief. This is a corrective, checkable, appropriately hedged result exactly of the kind the permanent record should hold.
  - The von Neumann interior-damping derivation assumes a uniform background state (h=1,u=M); this linearization is a modeling step, and labeling its arithmetic 'demonstrated' rather than 'in-model' is defensible but worth flagging for a future reviewer.
  - The frequency-flatness assumption for a_b across f=0.2429-0.25 is acknowledged as in-model/open but is load-bearing for the calibrated boundary factor; not yet independently tested.
  - None of the intermediate quantities (a_d,int, a_b, l_a, the N=480 predictions) appear in the provided reference JSON, so full verification depends on trusting the note's stated standalone-script method rather than repo-executed code — the proposed N=480 rerun is the right next check but hasn't happened yet.
- 🌊 **Kinetic** — **STORE**: The note delivers a concrete, checkable decomposition of the effective round-trip loss into a von Neumann-derived interior term and a calibrated boundary term, explains why the promoted [0.902,0.914] interval was wide (its two prior estimators corresponded to the interior-only and boundary-flat limits), and produces an explicit falsifiable prediction (8.69 ± 0.20 dB, falsification band 8.3-9.1 dB) plus a second discriminating prediction (N=480 threshold test) that the project can actually run. Labels are applied with more care than the prior draft: the interior factor is 'demonstrated' from the exact LF+relaxation update rule, the boundary factor is explicitly 'calibrated' (not 'derived'), and the composite l_a is correctly downgraded to 'in-model with one calibrated factor.' Every number checked against the supplied reference JSON (M_th_num 0.168943, cell lengths 582.80/576.62 nm, pulse_gain_dB_at_0p7_streaming 7.7967) matches, and the note's own arithmetic (67% share, 8.69 dB recovery) is internally self-consistent. The added §6 consistency check against both promoted notes and the explicit non-contradiction table for the streaming-gain key are exactly the kind of cross-validation a durable note should carry, and the Limitations section honestly flags the calibrated, frequency-flat, and unverified-estimator-error assumptions. My residual reservations are that the interior 'demonstrated' derivation and the layered error budget (±0.075/±0.10/±0.10/±0.05/±0.05 dB) have not been cross-checked against an actual execution of solver._step_LF on a linearized perturbation, so the precision quoted may be tighter than the unverified derivation chain warrants, and a_b's constancy across M_th,num and M_run is an assumption rather than a demonstrated invariance -- both are disclosed, which is what tips this to store rather than reject.
  - The core von Neumann/modified-equation derivation is evaluated by hand/standalone script with no execution of the actual repo solver step to confirm the modified-equation approximation matches the real per-step decay -- 'demonstrated' here means arithmetic-demonstrated from the read source, not code-verified.
  - a_b is calibrated by forcing loop_analytic*a_d,int*a_b=1 at the single measured threshold M_th,num, then applied unchanged (frequency-flat, configuration-flat) to a different operating point M_run; this extrapolation is flagged as an assumption but is the single largest source of unquantified risk in the chain.
  - The quoted error budget (±0.075/±0.10/±0.10/±0.05/±0.05 dB, quadrature-combined to ±0.20) is asserted without independent derivation of each term; the precision may overstate confidence given the derivation itself is unexecuted.
  - Falsifiability is real but untestable until an actual retuned-cavity run exists; until then the 8.69 dB figure is a pre-registered prediction, not yet a demonstrated or even in-model-confirmed result -- future readers must not mistake it for a measured value.
- ⚛️ **Quanta** — **STORE**: The note delivers a genuine, checkable decomposition of the effective round-trip loop into an analytically derived interior (von Neumann/modified-equation) term and a calibrated boundary term, and it directly engages the two prior REJECT votes on issue #13 by fixing the exact problems raised: it no longer frames the §5 prediction as contradicting the shipped-configuration reference number, it adds an explicit cross-check against both promoted notes (§6), and it downgrades the boundary factor from 'derived' to 'calibrated' in the title and §4. Every number that overlaps the supplied reference JSON matches to the printed digit (pulse_gain_dB_at_0p7_streaming=7.7967, cell lengths 582.80/576.62 nm, M_th_num=0.168943, M_th_353K=0.14708), satisfying the citation-consistency bar. Epistemic labels are applied carefully and consistently (demonstrated for source-verified scheme facts and interior arithmetic, in-model for the calibrated a_b and downstream predictions, open for the analytic boundary-mode derivation and estimator error), and the note is honest about its own weakest link (a_b's frequency-flat assumption, circularity of calibrating on the same threshold it must reproduce). It ends with a concrete, falsifiable, adoptable next step (an N=480 rerun that discriminates two boundary-scaling hypotheses and would convert a manuscript convergence claim from asserted to demonstrated), which is exactly the kind of durable WP5-relevant deliverable the standard wants. My main reservation is that the core derived intermediates (a_d,int, a_b, loop_analytic) are not present in the supplied reference outputs and so cannot be independently re-verified by this review beyond checking internal arithmetic consistency; the note is transparent that no repo code was executed for the derivation. Given the explicit hedging, correct in-model labeling of exactly the quantities that carry this risk, and the substantive rework responding to prior human correction, it clears the bar despite that residual verification gap.
  - Key derived quantities (a_d,int, a_b, loop_analytic, l_a) are not present in the supplied reference JSON and cannot be independently cross-checked by this review; correctness rests on trusting an unexecuted hand/symbolic derivation.
  - a_b is calibrated by forcing the threshold condition to hold exactly at the measured M_th_num, then reused at a different (M,f) point under an explicitly flagged but unverified frequency-flat assumption — a real source of circularity that must stay labeled in-model if promoted.
  - The note proposes to 'supersede' a promoted interval and narrow a promoted prediction band; if stored, the promotion process should confirm the promoted-note comparisons in §6 against the actual promoted text rather than taking the note's self-report at face value.
