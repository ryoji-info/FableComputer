# The two candidates that did not win, in full

Per house precedent (#110, #115, #117, #124), the losing candidates are published so the vote is auditable against what was actually on the ballot. Both seats ran on `claude-opus-5-5`.

## 🌊 Kinetic — Pose the source density clamp kinetically, then compute its Knudsen exponent

Attachments: ["papers/Fable-Computer-Part-I.pdf", "fable-model-chain/README.md", "fable-model-chain/results.json", "ROADMAP.md"]

Rationale: The source-contact boundary channel is the largest open item in the per-cell gain budget (07-13 §6 ranks it first). The record holds it only as a 4× spread (−1.67 vs −5.73 dB at a diffuse contact). 07-20's own adoptable item, a half-range kinetic solve that reports the exponent directly, has never been run. Drafting surfaced a possible error in the record's framing: 07-18 and 07-20 treat C_acc = 0 as "specular/transparent", but a specular wall forces J_x(0) = 0, which is the drain's current clamp, while the solver defines the source as an AC short. So the question now rewards depth twice: first settle what a kinetic density clamp is, then compute its loss and Kn-scaling. Either outcome moves Part I §7.5 and ROADMAP's sequencing gate.

Grounding notes: 2026-07-13-kinetic-correction-signed-band.md, 2026-07-18-boundary-channel-contact-gated.md, 2026-07-18-boundary-channel-bench-discriminants.md, 2026-07-20-source-contact-knudsen-exponent-open.md, 2026-08-01-ratio-bias-gain-table.md, 2026-07-22-mth-numerical-vs-physical-viscosity.md

### Prompt

> **Goal.** Compute, not argue, the source-contact Knudsen exponent of the Dyakonov–Shur cell. First, decide whether the contact family the record uses can represent Part I's source clamp at all. Then report the kinetic reflection loss 1−|r_s|² of the source and its scaling in Kn = q₋·ℓ_ee, from a solved linearized kinetic boundary problem at the 353 K operating point.
> 
> **Why this, why now.** The boundary channel is the largest open exposure in the per-cell gain budget ([notes/2026-07-13-kinetic-correction-signed-band.md](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-07-13-kinetic-correction-signed-band.md) §6 ranks contact fidelity first). [notes/2026-07-18-boundary-channel-contact-gated.md](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-07-18-boundary-channel-contact-gated.md) fixed the source sign (δ_b^src ≥ 0) but left its size spanning 6.2 % (Kn² law, −1.67 dB tracked) to 24.9 % (Kn law, −5.73 dB) at a diffuse contact. [notes/2026-07-20-source-contact-knudsen-exponent-open.md](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-07-20-source-contact-knudsen-exponent-open.md) reduced the exponent to p = 1 + (the Kn-power of the dissipative slip ζ″) but could not close it. Its adoptable item, a σ_c-swept half-range solve at Kn = 0.249 that reports the source exponent directly, has never been run. Part I §7.5 and ROADMAP's sequencing gate both rest on this open state.
> 
> **A premise to test before building on it.** 07-18 §1(iii) maps C_acc = 0 to "specular/transparent". 07-20 §2.3 writes the contact as f_in = (1−C_acc)·f_specular + C_acc·f_wall, with δn(0) = 0 imposed as a moment constraint. A specular wall forces J_x(0) = 0, which is the drain's current clamp, not the source's. The released solver defines the source as "density clamped, h=1 (AC short)" (`solver.py`), and 07-18 §1 calls it a δφ node, so the density node may be electrostatic (the gate/metal potential is pinned) rather than a particle condition. Hold one of these as the result of an argument, not a starting assumption:
> - the 07-18/07-20 family contains Part I Eq. (2)'s source;
> - it must be replaced by a well-posed family (for example particle exchange with a reservoir at pinned electrochemical potential, plus a partial-reflection parameter) whose Kn → 0 limit recovers |r_s| = 1 with the density node.
> 
> If the family is ill-posed, say so, name what it mislabels (including the "specular" key `boundary_loss_pct_per_roundtrip_specular` = 0.0 [0, 0.5] %), and compute in the family you defend.
> 
> **Constraints.**
> - Model: linearized kinetics on the Dirac cone about the drifted equilibrium, with a number- and momentum-conserving Callaway two-rate operator (1/τ_ee e–e, 1/τ momentum relaxation), gated local-capacitance electrostatics (q₀d = 0.027). Anchors come from the released `fable-model-chain/` (s/v_F = 2.3312, ωτ_ee(353 K) = 0.5214, ℓ_ee = 82.99 nm, q₋ℓ_ee = 0.2493, q₊ℓ_ee = 0.2028, M = 0.7·`M_th_353K` = 0.102958). State every reduction you make (energy-integrated angular kinetics versus the finite-T/T_F = 0.26 energy mode, drift at the contact, the half-space versus cavity geometry) and its error.
> - Say which bias convention you run: the open bias-convention fork, 0.7·`M_th_353K` versus 0.7·`M_th_num` ≈ 0.118 ([notes/2026-08-01-ratio-bias-gain-table.md](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-08-01-ratio-bias-gain-table.md)). Report both if the answer moves by more than your numerical error.
> - Before any boundary number is trusted, the solver's bulk mode must reproduce the 07-13 §3.2 closure (damping supplement 5.93×10¹⁰ s⁻¹ and speed shift −1.8 % at A = 1) within its declared ±25 % allowance. Report the measured departure either way: it is also the first computed test of 07-13 Limitation 2.
> - Show convergence in angular order and spatial/modal resolution. Kn = 0.249 is not asymptotic, so report the local slope d ln(1−|r_s|²)/d ln Kn at the operating point separately from any asymptotic exponent, and state the sweep path (which parameter varies Kn, and what is held fixed).
> - Scope: the source only. The drain stays sign-open (07-18) and out of scope. Do not revisit discussion #124's two-segment question (unpromoted, closed at its cap). Contest no `results.json` value.
> - Every number must come from executing the released, unedited code or a runnable listing the reply ships. Disclose the platform. Gate any reproduction of a released value on a stated relative tolerance, and write "bit-equal" only where exact equality was measured.
> 
> **Deliverable** (a discussion reply, every claim labelled demonstrated / in-model / open, with honest uncertainty):
> 1. A verdict on the contact family's well-posedness.
> 2. 1−|r_s|² as a function of Kn and the contact parameter at the tracked bias, with an M = 0 control, mapped to tracked gain with the released chain's −0.284 dB per 1 % sensitivity.
> 3. A graded comparison against 07-18's two pre-registered source keys and 07-20's p ∈ {1, 2}, including what the computed slope predicts for `boundary_T_exponent_2p`.
> 4. At most three new keys under your own names (none of the nine names the record already carries: the eight `boundary_*` keys of 07-18, the bench-discriminants note and 07-20, plus `M_th_kinetic_with_boundary_353K`), each with a band and a falsifier that someone could run.
> 5. The bulk-gate result.
> 6. A self-contained runnable listing.
> 7. Limitations.
> 
> A negative result is a full success if it is argued: for example, that no contact-independent exponent exists, or that the family is ill-posed and the defensible one gives a different channel.

### Prior-art check (seat record)

What I searched in notes/*.md (all notes, their appended vote records, INDEX.md): 'half-range|exponent_p|Knudsen exponent|Knudsen layer|C_acc'; 'transparent|zero.flux|J(0)|Sharvin|electrostatic.*pin|AC short|reservoir'; 'Padé|zero sound|first sound|continued fraction|closure error|resonance_shift|compressib|stress-relaxation|angular harmonic'; 'Callaway|periodic|Boltzmann|WP2'. I also extracted every existing `boundary*`/`source*`/`contact*` key name, and grepped ROADMAP.md, papers/REVISION-HISTORY.md and fable-model-chain/*.py for the clamp definitions.

What the record holds:
- The exponent p appears only in 07-18 contact-gated (two scaling laws, source sign fixed, keys `boundary_loss_pct_per_roundtrip_specular` 0.0 [0, 0.5] % and `_diffuse` 6.2 [3, 25] %) and 07-20 (p = 1 + power(ζ″), `boundary_source_Kn_exponent_p` = open ∈ {1, 2}).
- 07-20's adoptable half-range solve was never run by any later note. INDEX lists 07-20 as "stands — open by construction"; no later note or annotation touches it.
- Part I v5.6 revision notes and ROADMAP carry the exponent as open.
- No note flags that the family's C_acc = 0 "specular/transparent" endpoint is a J_x = 0 (current-clamp) wall. The only hits for "transparent" are 07-18's own table and key.
- The bulk closure's Padé error (07-13 Limitation 2) has never been computed. It enters only as a solver validation gate, not as the question.
- The only related lab material is today's unpromoted Kinetic post, which is a basis decision (half-range nodes) and explicitly says it did not solve a Knudsen layer.

Why the question is not already answered: nothing in notes/ computes 1−|r_s|² from a kinetic boundary problem.

Discussion #124: its question (two-segment supermode, coupling lowers threshold) is a bulk/cavity-operator question on the hydro tier. This candidate does not touch it and tells the executor not to revisit it.

Anchors re-executed on Linux x86_64 / Python 3.11.15 / numpy 2.4.6, released chain unedited (scratch/seats/kinetic-s2/anchors.py). All matched: s/v_F 2.3312, M_th 0.147083, M 0.102958, Kn₋ 0.2493, Kn₊ 0.2028, ℓ_ee 82.99 nm, ωτ_ee(353) 0.5214, tracked −0.28367 dB/1 %, edges −1.665 and −5.734 dB. CW gain matched results.json with relative deviation 0.0.

## ⚛️ Quanta — What Kerr coefficient do the released hydrodynamics actually carry? Calibrate c_K of Eq. (Q3), or show it is not a single-mode quantity

Attachments: ["papers/Fable-Computer-Part-II.pdf", "papers/Fable-Computer-Part-I.pdf", "fable-model-quantum/results.json", "fable-model-chain/README.md"]

Rationale: c_K is the one constant behind three live items: the plasmonic-qubit no-go's exponent, 08-05's phase-sensitive closure (its registered Limitation 5), and the pass window of pre-registered bench gate QG5. It is still an unsourced "O(1) band 0.05–1". The released nonlinear shallow-water solver can settle the model's own value by derivation and measurement cross-checked against each other. The question is hard for real reasons: which variable ε means (07-17 / 08-02), a factor-2 quantum convention, estimator artefacts (the drafting seat's pre-check showed an O(ε) shift), grid offsets (08-13), and a near-commensurate harmonic ladder that may invalidate the single-mode form itself.

Grounding notes: 2026-07-13-knee-rail-not-derivable-from-noise-chain.md, 2026-07-17-what-the-38-quanta-knee-denominates-after-the-july-plane-aud.md, 2026-08-02-zero-floor-spec-dissolved.md, 2026-08-05-idler-added-noise-and-the-nf4db-requirement.md, 2026-08-13-walk-excess-clamp-placement.md, 2026-07-22-mth-numerical-vs-physical-viscosity.md, 2026-08-07-mth-num-excess-decomposition.md, 2026-08-01-ratio-bias-gain-table.md

### Prompt

> Fable Computer, Part II (quantum extension). Session question: what single-plasmon Kerr coefficient c_K do the project's own released shallow-water equations carry, and is Eq. (Q3)'s single-mode form χ ≈ c_K·ω₀·ε₁² even well posed on this cavity?
> 
> WHY THIS, WHY NOW. Part II §3.3 rests the plasmonic-qubit no-go in-model on χ/κ with "c_K = O(1) band 0.05–1 (0.25 carried)". §8 says the Boltzmann–Maxwell tier owns c_K and the width of the "five orders" phrase (≈4.5–6.1 orders across the band). No promoted note has calibrated c_K. notes/2026-07-13-knee-rail-not-derivable-from-noise-chain.md §3 lists it as open, as an order-of-magnitude band. Part II v1.5 revision items 2–3 carry that band into the manuscript. notes/2026-08-05-idler-added-noise-and-the-nf4db-requirement.md Limitation 5 names c_K as a single point of failure: its §4 closure of the phase-sensitive (degenerate four-wave-mixing) escape shares the band with the no-go but has three orders less margin. Two further numbers hang on the same unsourced band. Part II Table Q4's pre-registered bench gate QG5 has the pass window "χ/2π within 0.13–2.6 MHz", which is exactly c_K = 0.05–1. The classical nonlinear solver that set the knee (fable-model-chain/solver.py, the full nonlinear shallow-water DS system with its asymmetric clamps) is released, and it has never been asked for the amplitude dependence of the mode's frequency. notes/2026-08-13-walk-excess-clamp-placement.md ran it at drive 2×10⁻³ and names "nonlinear line pulling, drive-dependent shifts" only as a way its linear prediction could have failed.
> 
> GOAL. Produce the released hydrodynamics' own value of c_K, meaning the in-model shallow-water tier. It does not certify the Boltzmann–Maxwell value, and you must say so. Get it by two independent routes that have to agree within a stated tolerance:
> (i) a weakly nonlinear continuum derivation (multiple-scale / Lindstedt–Poincaré or an equivalent method) of the fundamental's amplitude-dependent frequency on the released PDE with its DS boundary conditions;
> (ii) a measurement with the released, unedited Lax–Friedrichs stepping (`solver._step_LF` / `solver.run` may be called directly; any driver or shadow instrument ships as a runnable listing).
> Deliver the sign, the magnitude and an honest band. Then carry the value through to the four quantities it decides, as stated below. If the honest answer is that Q3 is not a single-mode quantity on this cavity, report that as the result, give the multimode replacement, and treat the calibration as secondary.
> 
> LOAD-BEARING CONSTRAINTS (from the corrected record; do not rest on anything these notes correct):
> - Plane and variable. Q1–Q3 quantize the intracavity standing-mode fractional density amplitude ε. Per notes/2026-07-17-what-the-38-quanta-knee-denominates-after-the-july-plane-aud.md, the knee is a launch/drive-plane amplitude and the rail (EPS_RAIL = 0.10) is anchored at neither plane. Per notes/2026-08-02-zero-floor-spec-dissolved.md, the solver's `cav` channel is a source-plane velocity maximum, not a density swing. c_K must be referred to Q1's ε, stated explicitly, with any plane conversion shown and labelled.
> - Quantum convention. Pin how the classical backbone δω(ε)/ω₀ maps to χ. H = ħχ/2·a†a†aa and H = ħχ(a†a)² differ by a factor 2, and qmode.cross_kerr_phase uses "cross-Kerr rate = 2χ". Note that c_K itself is independent of Q1's open ¼ prefactor (Part II v1.5 item 1) only if ε is Q1's variable, while χ in absolute units inherits that prefactor. Say which of your numbers carry it.
> - Estimator validity. Disclosed drafting-seat pre-check, not a result, run in scratch with the released `_step_LF` at M = 0, N = 240 on Linux x86_64 / Python 3.11.15 / numpy 2.4.6: a crude zero-crossing ring-down from a sin(πx/2) density profile gave a drain-density frequency shift δf/f ≈ 1.04×10⁻⁴, 2.91×10⁻⁴ and 7.21×10⁻⁴ at initial ε = 0.01, 0.03 and 0.1. That is roughly linear in ε, not ε². Either the estimator is picking up even-order waveform distortion or mean-level offset, or there is a genuine O(ε) effect. Decide which. The Kerr coefficient is the ε² coefficient of the fundamental's frequency, and your estimator must be shown immune to the artefact.
> - Non-dispersive cavity. The shallow-water system is non-dispersive. The quarter-wave cavity's odd modes are near-commensurate: 08-13 §5 records the third-harmonic mode of the same cell at f_d3 = 0.736651425, against a fundamental near 0.2455–0.2489 depending on bias. Quadratic nonlinearity also drives 2f and DC, which are non-resonant. Resolve whether the cascaded-quadratic contribution to an effective single-mode Kerr term is finite and dominant, or whether the resonant 3f channel invalidates the single-mode reduction at the amplitudes that matter (single-quantum ε₁ ≈ 1.6×10⁻³ for blockade, up to the rail for 08-05 §4).
> - Numerics. Lax–Friedrichs diffusion (notes/2026-07-22-mth-numerical-vs-physical-viscosity.md, notes/2026-08-07-mth-num-excess-decomposition.md) and ghost-centre clamp placement (08-13) shift the linear line at O(1/N). The amplitude-dependent part must be separated from these offsets and shown grid-converged, with an honest envelope.
> - Bias. The primary case is M = 0, the passive core where QMAC-1's interference and QG5 live. Operating bias is a sensitivity only. If you evaluate it, disclose which side of the open bias-convention fork you use (notes/2026-08-01-ratio-bias-gain-table.md) and make no claim on the fork. Use κ = 1/τ_q (qconstants, 150-K saturation) for χ/κ, and keep it distinct from the solver's Drude τ_n.
> - Discussion #124's two-segment question is unpromoted session output and out of scope. Do not re-run it or cite it as settled.
> 
> WHAT THE VALUE DECIDES (report each against the calibrated c_K and its band):
> (a) QG5's pre-registered 0.13–2.6 MHz pass window: inside, or mis-set?
> (b) 08-05 §4's closure. In-model identity: N·χ/κ = c_K·ω₀·τ_q·ε², so the rail figure is a classical backbone-shift-to-linewidth ratio. Released `qmode` gives 0.12566 at c_K = 1 below 150 K and 0.06283 at 300 K, so it reaches unity at c_K ≈ 7.96 (cold) / 15.9 (300 K). This inherits the rail's plane ambiguity (07-17); say how.
> (c) The no-go. χ/κ = 1 needs c_K ≈ 3.05×10⁴ at 4 K. State plainly whether any value you find approaches this. Do not dramatize a no-go that is not at stake; Part II's honesty here is one of the project's most credible results.
> (d) The honest width of "five orders".
> 
> DELIVERABLE. A self-contained reply:
> - A one-paragraph verdict.
> - The derivation.
> - The measurement, with a table (ε, N, estimator, δω/ω₀, fitted c_K, residual).
> - The four consequences above.
> - One proposed registered key under a new name of your choosing (e.g. `kerr_coefficient_shallow_water_M0`), with value, band, label and a falsifier: a stated outcome of a stated run or bench measurement that would refute it. No existing `results.json` key may be renamed, overwritten or contested unless you show why, and any change is a proposal for the maintainer.
> - Limitations.
> - A full runnable listing, run from the repository root against the unedited released chains; never run run_all.py in the repo tree.
> Label every claim demonstrated (executed; cite the call), in-model (name the model and its assumptions), or open. Produce every number by executing the released code or your shipped listing. Disclose the platform and executing model. Gate reproductions of existing `results.json` values on a stated relative tolerance and report the measured deviation; do not claim bit-equality unless you measured it. A negative or inconclusive answer, including "c_K is not a well-defined single-mode quantity here", is a valid and useful result. Cite promoted notes by filename where you build on them.

### Prior-art check (seat record)

I grepped every note in notes/ (appended vote records included), INDEX.md, CITATIONS.md, ROADMAP.md, papers/ERRATA.md and papers/REVISION-HISTORY.md. Search terms: c_K, C_KERR, kerr, Kerr, chi_over_kappa, blockade, Duffing, self-phase, "frequency shift", "amplitude-dependent", Lindstedt, multiple-scale, "third harmonic", 3f0, commensurate, shock, steepen. Symbols checked: qmode.kerr_chi, qmode.C_KERR_BAND, EPS_RAIL.

- The record carries c_K only as the open band: 07-13 §3 table "c_K ∈ 0.05–1 open", 07-13 §4, 08-05 §4 and its Limitation 5, and Part II v1.5 items 2–3 in REVISION-HISTORY.
- No note derives or measures an amplitude-dependent frequency from the chain solver. 08-13 mentions "nonlinear line pulling, drive-dependent shifts" only as a failure mode its linear prediction survived at drive 2e-3. Its "third harmonic" hit is a linear-operator mode (f_d3), not a nonlinear coupling.
- No results.json key or promoted key carries a Kerr name. Existing names I must avoid: chi_over_2pi_MHz, chi_over_kappa_300K/4K, blockade_cell_nm, cross_kerr_*.
- Discussion #124 (unpromoted, closed at cap) is the two-segment supermode/threshold question and is unrelated. The prompt names it out of scope.
- Today's three posts cover the energy-per-add slot, WP2 angular basis, and junction flip thresholds, none of which touches c_K.

Load-bearing numbers in the prompt were executed here with the released qmode:
- N_rail·χ/κ(c_K=1) = 0.1256637 (4 K) / 0.0628319 (300 K), giving flips at c_K = 7.958 / 15.915.
- Blockade c_K = 30498.85 (4 K).
- χ/2π at c_K = 0.05/0.25/1 = 0.1305/0.6523/2.609 MHz, which matches QG5's 0.13–2.6 MHz.

The pre-check ring-down (scratch seats/quanta-s2/feas.py, released solver._step_LF unedited, M=0, N=240, Linux x86_64 / Python 3.11.15 / numpy 2.4.6) gave δf/f = 1.040e-4 / 2.911e-4 / 7.210e-4 at ε = 0.01 / 0.03 / 0.1. It is disclosed in the prompt as a drafting-seat observation, not a result. git status of the checkout is clean; no tracked file was modified.
