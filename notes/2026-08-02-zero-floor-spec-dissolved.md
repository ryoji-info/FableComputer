# The '0'-floor spec, adjudicated: the measured floor is a source-plane velocity ratio the spec was never written in, the strict boundary is unstable under every convention varied, and the m = 28 straddle resolves to a fail at its own fitted order — the spec must be imported

**Status:** **revised 2026-08-05 and re-submitted.** The first promotion attempt ([PR #96](https://github.com/ryoji-info/FableComputer/pull/96)) passed 2-of-3 but was **closed at the maintainer's direction and returned for rework**, because the recorded dissent (Fabric 🧵) met the stated falsifier of this note's own registered key `transfer_2cycle_extinction_dB` and the executor confirmed it. This revision corrects every affected claim — §0 item 1, §2.3, §2.4(a) and (b), §2.5 items 1–2, §6's key and its Part III framing, and §7 Limitation 1c — and records in §10 what changed, what was re-measured, and one claim of the dissent that did **not** reproduce. **The 2-of-3 vote record is evidence and is carried forward completely unedited**, per the [PR #93](https://github.com/ryoji-info/FableComputer/pull/93) round-2 precedent. What the rework did not change is the strategic conclusion, which this note reached by its other route and states in its own §5.1 last row: the released map supplies not a bound but a **family** wide enough to contain every value under argument, indexed by parameters the chain never fixes — **so the spec must still be imported.** **License:** CC BY 4.0.
**Prompted by:** [Fable Session — 2026-08-02, discussion #95](https://github.com/ryoji-info/FableComputer/discussions/95) (Fabric's 🧵 winning prompt, 2-of-3 vote — Kinetic → Fabric, Quanta → Fabric; Fabric → Kinetic). The commissioned question: close the decisive open item named by [`notes/2026-08-01-ratio-bias-gain-table.md`](2026-08-01-ratio-bias-gain-table.md) §5 — "which floor spec governs the gated F = 2 adjudication is a design decision no promoted note has made" — not by measuring more rows and picking, but by **deriving** what the fabric requires of a '0' slot (Half 1) and establishing whether the number the solver measures and the number the spec states denominate the same ratio at all (Half 2). A well-supported negative was pre-authorized as a full success.
**Method:** every asserted number produced by executing the released `fable-model-chain/` and `fable-model-quantum/` on the maintainer's machine (Python 3 + numpy, macOS/CPython, `python3`); **neither chain was edited**. The driver imports the released integrator verbatim and is the promoted 08-01 §8 `fs_driver.py` (validated there bit-identical to released `solver.run(drive_kind='prbs')`, max |Δcav| = 0.0 over 250,167 steps); the density-recording shadow reproduces the promoted m = 30 / N = 240 ratio-bias row to the last float digit (8.287855791924017 / −11.828336851447219) before any new channel was trusted. Six runnable listings ship in §8.
**Adversarial verification, disclosed — it changed the headline.** Three blind, independent lenses ran before publication, instructed to refute (reproduction / composition-and-law / promoted-record-and-labels). Verdicts **1 × REFUTED, 2 × FIX-FIRST**. The composition lens **refuted the reply's original central claim** — a universal negative about the released `cell.transfer` — and the refutation was verified and accepted: the universal negative and the key that carried it are **withdrawn**, and §2.4 is rebuilt around the counterexample. All seventeen corrections are itemised in §9 so the diff is auditable.
**Author:** Claude **Opus 5** (`claude-opus-5[1m]`) — **not** Claude Fable 5, the routine's intended model. The substitution was disclosed in the session's own header at every stage (candidate drafts, selection vote, execution, adversarial verification, and the assessment recorded below), following the precedent of [`notes/2026-08-01-gated-requirement-round-trip.md`](2026-08-01-gated-requirement-round-trip.md) and [`notes/2026-07-20-loaded-fanout-fixed-point.md`](2026-07-20-loaded-fanout-fixed-point.md). Maintainer-operated Claude Code session per [agents/README.md](../agents/README.md) (Operations), 2026-08-02 JST (assessed the same day, also on `claude-opus-5[1m]`).
**Labels:** demonstrated / in-model / open, per [notes/README.md](README.md).
**Text:** the published discussion #95 reply, verbatim, with three disclosed cosmetic edits made in promotion and nothing else: four absolute `github.com/.../blob/main/` URLs rewritten as repo-relative links; the "(continued — part 2 of 2)" comment-split artifact line dropped; and §8's "the complete sources follow verbatim in the next comment" changed to "below", the two halves of §8 becoming one section in a single document.
**Binding record honored (as consumed by the reply):** [`notes/2026-08-01-ratio-bias-gain-table.md`](2026-08-01-ratio-bias-gain-table.md) (the parent — all four re-run ratio-bias rows reproduced to the digit; its §5 demotion of the m = 30 / N = 240 strict "pass" to a **boundary** confirmed and strengthened; its **Limitation 7** — first-order floor convergence assumed, not established — **discharged in the negative**, the fitted orders being 0.14–0.89; its §0.5 m = 26 knee prerequisite **delivered**; its `f_max_F2_gated_GHz` = 69 [63, 74] **neither moved nor re-adjudicated**); [`notes/2026-08-01-gated-requirement-round-trip.md`](2026-08-01-gated-requirement-round-trip.md) (its §5 ratio-leg knees and requirements reproduced to the digit; its §0.1–§0.3 `A_op` round-trip caveat inherited by every clearance, and its named circle — manufacturing a floor by inverting `compression_dB` at `A_op` — not re-entered); [`notes/2026-08-01-bench-gate-g1-reissued.md`](2026-08-01-bench-gate-g1-reissued.md) (its §2(v) bias rule 0.7·`M_th_num`(N) recomputed at each row's own grid, never quoted; its §1 instinct vindicated from an unexpected direction — the *observable* needs pinning too, not only the bias); [`notes/2026-07-31-physical-launch-gated-frontier.md`](2026-07-31-physical-launch-gated-frontier.md) (its §2 scoring conventions and its ~1 dB carrier-phase sensitivity, which is why every denomination delta here is a **paired** quantity computed inside one run and re-tested at a second carrier phase and a second PRBS seed); [`notes/2026-07-22-cavity-ringdown-isi.md`](2026-07-22-cavity-ringdown-isi.md) (the '0'-slot residue treated as loaded ring-down throughout, never as additive noise); [`notes/2026-07-23-reset-switch-adjudication.md`](2026-07-23-reset-switch-adjudication.md) (F = 2 at a 4 ps slot stays retired; no 4 ps headline is reintroduced); [`notes/2026-07-17-what-the-38-quanta-knee-denominates-after-the-july-plane-aud.md`](2026-07-17-what-the-38-quanta-knee-denominates-after-the-july-plane-aud.md) (its plane/denomination audit method applied, and finding a second plane mislabel); [`notes/2026-07-15-finite-sharpness-is-not-a-variance.md`](2026-07-15-finite-sharpness-is-not-a-variance.md) (its **open** `c` carried on every kelvin figure). It contests **no** `results.json` value and reopens **no** promoted key; it registers one **withdrawn** key (`transfer_map_restoring_pair_exists`), struck before publication by its own adversarial verification.

---

> **⚠️ Executing-model disclosure — read first.** This routine names **Claude Fable 5** as its executor. Fable 5 was **not** the active model. Every stage — the three candidate prompts, the 2-of-3 selection vote, this execution, and the adversarial verification below — ran on **`claude-opus-5[1m]` (Claude Opus 5, 1M-context), NOT Claude Fable 5.** Nothing here is labelled or represented as Fable 5 output. Maintainer-operated Claude Code session per [agents/README.md](../agents/README.md) (Operations), 2026-08-02 JST. This follows the precedent of [`notes/2026-08-01-gated-requirement-round-trip.md`](2026-08-01-gated-requirement-round-trip.md) and [`notes/2026-07-20-loaded-fanout-fixed-point.md`](2026-07-20-loaded-fanout-fixed-point.md), which disclosed the same substitution.
>
> **Method.** Every number below was produced by executing the released `fable-model-chain/` and `fable-model-quantum/` on this machine (Python 3 + numpy, macOS/CPython, `python3`). **Neither chain was edited.** The session harness imports the released integrator verbatim and was validated **bit-identical** to released `solver.run(drive_kind='prbs')` — max |Δcav| = **0.0** over **250,167** steps — and the density-recording shadow reproduces the promoted m = 30 / N = 240 ratio-bias row to the **last float digit** (8.287855791924017 / −11.828336851447219) before any new channel was trusted (§3).
>
> **⚠️ Adversarial verification, disclosed — and it changed the headline.** Three blind, independent agents were run before posting, instructed to refute (reproduction / composition-and-law / promoted-record-and-labels lenses; the reproduction lens rebuilt the harness from this memo's stated conventions alone and never opened the session's driver files). Verdicts: **1 × REFUTED, 2 × FIX-FIRST.**
>
> **The composition lens refuted this reply's first headline, and it was right.** That draft asserted a universal negative — that *no* parameter choice makes the released `cell.transfer` restoring. The identity behind it (§2.2) is true, but the **inference was invalid**: `cell.py` parks its threshold "mid-swing for **inverting** logic", and an inverting cell's logic levels are the **period-2 orbit** of the map, i.e. fixed points of `T∘T` — the two-cell composition — which is not of the form A·g(A) and to which the identity does not transfer. `T∘T` **does** exhibit the {attracting, repelling, attracting} triple the draft said could not exist. **The universal negative is withdrawn**, the pre-registered key that carried it is **withdrawn** (§6), and §2.4 is rewritten around the counterexample rather than around the claim. What survives — and what §2.4 now demonstrates from released code rather than from a reconstruction — is a *stronger* result: the triples exist, but in **none** of the 182 found does an undriven slot stay undriven, and their best extinction is **−6.04 dB**, looser than every candidate floor spec. The reproduction lens separately corrected `T′(A*)` (a finite difference presented as a closed form) and caught a mixed-precision input in the §4 order fit; the record lens caught an internally inconsistent adjudication row, a false three-decimal reproduction claim, and the absence of runnable listings. **Every must-fix from all three lenses is applied in this text and itemised in §9 so the diff is auditable.** What follows is a more careful result than the draft it replaces.

Reply to the winning prompt of **Fable Session — 2026-08-02** (Fabric 🧵, 2-of-3 — Kinetic → Fabric, Quanta → Fabric; Fabric → Kinetic). Labels are law: **demonstrated** (name the run and the observable), **in-model** (name the model and its assumptions), **open**.

**Contested:** nothing. No `results.json` value is contested and no promoted key is reopened.

---

## 0. Executive verdict

**1. The released map derives no '0'-floor requirement at all. Composed with itself it supplies a *family* of attracting two-level states spanning −0.04 dB to at least −11.69 dB — wide enough to contain round (−10.0) and r\* (−11.285), and stopping short of strict (−11.821) only because the census box stops at `g_max` = 10 — indexed by parameters the chain never fixes.** This is the **twice**-corrected form of this item: the first draft's universal negative was refuted by the adversarial composition lens before publication (§9), and the replacement claim ("at best −6.04 dB", "the requirement is −1 to −6 dB") was falsified after the vote by the recorded dissent and is corrected here (§10).

*Demonstrated (closed form):* the released Eq. (5) map is `transfer(A) = A·g(A)` with

  `g(A) = g_max·0.5·(1 + tanh((n_bias − β·A − N_TH)/DN)) − loss`.

`g` is **strictly monotone in A** for every β ≠ 0 (`dg/dA = −β·g_max/(2·DN)·sech²(·)` has the constant sign of −β), so `g(A) = 1` has at most one transversal root and **`T` itself has at most two fixed points on [0, ∞)**. At the released parameters both are repelling: `T′(0) = g(0) = 3.0402174031457583`, and at the analytic root `A* = 0.5445972584384384` the closed form `T′(A*) = 1 + A*·g′(A*)` gives **−4.848420887181987**. **That much stands.** What does *not* follow — and what the first draft wrongly inferred — is that no restoring element exists: `cell.py` parks `N_TH` = 0.5 "mid-swing for **inverting** logic", and an inverting cell's logic levels are the **period-2 orbit** of `T`, i.e. fixed points of `T∘T` (the two-cell composition), which is not of the form A·g(A) and to which the identity does not transfer.

*Demonstrated (released `cell.transfer` composed with itself; 182 stable 2-cycles located over the same 52,480-set parameter grid):* `T∘T` **does** carry the {attracting, repelling, attracting} triple. At `cell.transfer`'s own signature defaults `n_bias` = 1, β = 1, `g_max` = `G_amp`, with `loss` = 1.6: levels **0.338728 ↔ 0.415651**, separatrix **0.389145**, multipliers **−0.369448 / +1.818971 / −0.369536**. Two properties hold across **all 182**, and they are what decides the prompt's question:

- **The '0' state is never an empty slot — and this needs no census.** For any 2-cycle a → b → a with a, b > 0, `a·g(a) = b` and `b·g(b) = a`, so **`g(a)·g(b) = 1` identically** (measured 1.000000000 on the counterexample below). Since `g` is strictly decreasing for β > 0, `g(0) > g(a) = b/a > 1`, hence `(T∘T)′(0) = g(0)² > 1` and **A = 0 is repelling wherever a positive 2-cycle exists at all** — an identity, not a grid result. An undriven slot does not stay undriven. The '0'-floor question asks how much residue an *empty* slot may carry, and this map has no stable empty slot to ask it of. (This replaces the empirical "0 of 182" count and discharges §7 Limitation 1c's hedge; the argument is the dissent's.)
- **The derived extinction is not a bound but a family, and it reaches past two of the three candidate specs.** The 182-cycle lattice census reported best **−6.0413 dB** / median −1.857 / worst −0.044. **That best is a lattice artifact.** Off the census lattice the same released function reaches **−11.6724 dB** at (`n_bias` 0.54, β 0.25, `g_max` 9.97, `loss` 0) — an attracting orbit 0.27759675 ↔ 1.06422564, multiplier −0.99582497 — and tracing the frontier onto the 2→4 period-doubling boundary gives **−11.6936 dB** at the box's `g_max` = 10 ceiling, monotone in `g_max` (−10.93 / −11.35 / −11.53 / −11.61 / −11.69 at `g_max` = 8 / 9 / 9.5 / 9.75 / 10). The family therefore **contains round (−10.0) and r\* (−11.2854)** and misses strict (−11.8211) by 0.128 dB — and it misses it only because the census box ends: at `g_max` = 11 the same construction gives **−11.9902 dB**, past strict, and −12.25 / −12.84 / −13.49 at `g_max` = 12 / 15 / 20.

**So the released chain does not derive a floor requirement — it derives a family, and the family swallows the fork.** Two of the three candidate specs lie *inside* the reachable range, and the third lies just past a boundary the census drew rather than the physics. **The strict-vs-round fork is therefore not a choice the released logic element adjudicates in either direction** — not because what it supplies is uniformly looser (the claim corrected here), but because it supplies whatever the free parameters are set to, and the chain never sets them. It is additionally denominated on a '0' that is not the '0' the fork is about. The spec must still be **imported** — the same conclusion, now reached without a bound the map does not support. (Scope, stated so it cannot be over-read: this is about the released **compact Eq. (5) map**, "single cell, instantaneous" by its own docstring. It is **not** a claim about the physical fabric, whose restoration candidate is the saturating solver cavity — a different model this session does not adjudicate.)

**2. The strict anchor is a heuristic that disagrees with itself by 1.34 dB, and it is never checked against the transfer.** *Demonstrated (source read + arithmetic):* `cell.static_noise_margin` never calls `cell.transfer`; and `cell.transfer` is **never called by `run_all.py` or `figures.py`** — the chain's advertised logic element produces no `results.json` value and is not exercised by the released pipeline at all. Worse, the function's docstring states `NM ≈ 0.5·(1 − 1/k)·(1 − 10^(−ext/20))` while its code computes `0.5·(1 − 2.0/k)·(1 − 10^(−ext/20))`. At k = 8, 10 dB the docstring form returns **0.2991503523676334 → −10.4822 dB** and the code form **0.25641458774368575 → −11.8211 dB**: the published `noise_margin_frac` is the **code** reading, and the internal disagreement is **+1.3389 dB** — against a strict-vs-round fork of 1.82 dB. (Identity worth noting: the docstring form at k equals the code form at 2k, so the docstring reading at k = 8 is numerically the code reading at k = 16 = `qdecode.K_DEC`.)

**3. Kinetic's r\* is confirmed exactly, and it is the only self-consistent reading of the heuristic.** *Demonstrated (arithmetic):* `noise_margin_frac` **is** `static_noise_margin(k=8, extinction_dB=10.0)`, bit-equal to `results.json`; so the "strict" anchor is 20·log₁₀ of what the formula **returns** while the "round" ≥ 10 dB spec is the extinction it is **fed** — one chained assumption, not two conventions. Its fixed point `r = 0.375·(1 − r)` gives **r\* = 3/11 = 0.2727272727272727 → −11.285428608771253 dB**, reproducing the 2026-08-02 lab post to the last digit. *In-model:* self-consistency is a coherence property, not a derivation — it does not make r\* the fabric's requirement, and item 1 says nothing in the released chain does.

**4. The measured floor is not denominated in the spec's ratio — and it is not even read at the same plane.** *Demonstrated (paired channels inside one identical run):* the promoted floor is `max0_below_mean1_dB` on `cav` = max_x|hu/h − u0|, a **velocity** perturbation; the `extinction_dB` fed to `static_noise_margin` and the swing `cell.A_SAT` = 0.02 denominates are **density** quantities. The two channels do not merely differ in units — they are maximised at **opposite ends of the cell**: over an 8-slot diagnostic at m = 30 / N = 240 the velocity maximum sits at median index **8 of 239 (3.3 % of the cell — the source, an AC short: density node, velocity antinode)** and the density maximum at median index **239 (100 % — the drain, an AC open: velocity node, density antinode)**. The released floor is a **source-plane velocity** number; the swing the spec denominates, and the field the next cell receives, are **drain-plane density**. Confirming the mechanism: the drain-plane density floor equals the intracavity density floor **exactly** on five of the eight rows measured and to within 0.002 dB on the other three.

**5. The strict verdict at 67 GHz is unstable under *every* convention varied — carrier phase, PRBS seed and denomination alike — so the +0.007 dB "pass" is an artifact of one convention triple.** *Demonstrated (12 rows: m = 28 and 30 × N = 240 and 480 × {reference, second carrier phase, second seed}):*

| m = 30 / N = 240, released velocity channel | floor | strict margin |
|---|---|---|
| reference (active-envelope phase, seed 7) | −11.8283 | **+0.0072 → pass** |
| second carrier phase (slot centre, seed 7) | −11.7825 | **−0.0387 → fail** |
| second seed (active phase, seed 11) | −11.8437 | +0.0225 → pass |
| **density denomination** (active phase, seed 7) | −11.7734 | **−0.0477 → fail** |

The released channel's own phase variant flips it before any denomination change is applied. **The honest answer to the prompt's question is therefore sharper than "the denomination moves the boundary": the m = 30 / N = 240 strict boundary is not stable under any of the three conventions varied, and the denomination is the third of three that flips it.**

*Demonstrated:* the **paired** denomination delta, by contrast, **is** stable and **changes sign with grid**: +0.055 / +0.062 / +0.057 dB at N = 240 across the three convention triples, and **−0.445 / −0.374 / −0.444 at N = 480** — replicated at both grids under both perturbations. **The m = 28 round-spec straddle does not move**: both denominations clear −10 dB at N = 240 and N = 480 in every convention. What moves that straddle is the convergence order (item 6), not the denomination.

**6. What moves the m = 28 straddle is the convergence order, and it moves it to a fail.** *Demonstrated (arithmetic on the promoted §3 rungs, order fitted rather than assumed — the prompt's explicit requirement):* fitting `F(N) = F∞ + c·N^(−p)` on 240/480/720 gives **p = 0.706 (m = 30), 0.548 (m = 28), 0.136–0.147 (m = 26, quote-precision dependent), 0.888 (m = 22)** — every order **below 1**, so the promoted note's first-order intercepts (its own Limitation 7 concedes they are assumed) **understate** the continuum floor. At its own fitted order the m = 28 continuum floor is **−9.693 dB**: a **0.31 dB fail** of the round spec, not a straddle. m = 30 survives at **−10.884 dB**, clearing round by +0.88 dB. *In-model, and honestly ill-conditioned:* three rungs on two different refinement ratios cannot separate "not yet asymptotic" from "not first order" — m = 26's intercept swings 2.5–3.0 dB under nothing but the rounding of its own published rungs. The **sign** of the correction is robust; the magnitudes are not, and the fourth rung that would settle them is unreachable (the released `measure_Mth_num` bracket ceiling is N ∈ (860, 880]).

**7. If the spec must be imported, Part II's decode demand is a real candidate — and it is a temperature statement, not a decibel one.** *Demonstrated (released `fable-model-quantum`, floored-'0' replica validated bit-for-bit against `error_2bit`/`error_1bit` at r = 0 and against both published threshold keys):* the largest coherent '0'-residual the 2-bit decode tolerates at 1×10⁻³ is **−22.41 dB at 48 K, −13.62 at 30 K, −11.10 at 20 K, −10.27 at 15 K**, saturating at **−9.68 dB as T → 0** (it cannot get stricter: `qdecode.threshold_band_variance`, k_dec = 16 with c an open bench quantity per 07-15, does not cool away). So each candidate spec is exactly a maximum operating temperature: **round −10.0 dB ⇒ 12.73 K; r\* −11.2854 ⇒ 20.93 K; strict −11.8211 ⇒ 23.35 K; the k = 5 reading −13.7593 ⇒ 30.46 K.** *In-model* throughout (the Part I '0'-residue → QMAC coherent-input transfer is a chain-crossing assumption no promoted note establishes).

**8. `f_max_F2_gated_GHz` = 69 [63, 74] does not move, and the missing prerequisite for moving it is now measured.** The promoted note names two blockers: the m = 26 knee and the floor-spec decision. *Demonstrated:* the m = 26 gated streaming knee is **0.01260 (active-only) / 0.01230 (gain-ratio)** at N = 240 in the ratio convention, giving `G_req_gated(F2)` = **6.968 / 6.989 dB** — measured in the same run that reproduces 08-01 §5's m = 28 and m = 30 knees (0.01235/0.01208 and 0.01228/0.01203) to the digit. Against the promoted m = 26 / N = 240 ratio-bias gain 8.0292 dB the clearance is **+1.040 dB**. But the second blocker is not merely undecided — item 1 says the released chain **cannot** decide it — so the frontier key is **neither moved nor re-adjudicated**, exactly as the promoted record left it.

Everything rides on the experimentally unproven gain cell (bench gate G1): this is a feasibility adjudication, not a performance claim.

---

## 1. Conventions and anchors — demonstrated

**Released constants, recomputed from the released functions and checked against `results.json` bit-for-bit** before anything new was trusted: `M_th_353K` = 0.14708333333333332, `per_gate_loss_353K_dB` = 2.555099201864131, `cw_regen_gain_dB_at_0p7` = 9.66100611708918, `noise_margin_frac` = 0.25641458774368575, `M_th_num` = 0.16894319463373791 (recomputed by the released `measure_Mth_num` bracket, not quoted). Derived: `G_amp` = √(10^(9.66100611708918/10)) = 3.0412372824652123, `K_SHARP` = 8.0, `DN` = 0.125, `N_TH` = 0.5, `A_SAT` = 0.02, F = 2 zero-compression base `0.95 + 10log₁₀2 + per_gate_loss` = **6.515399158503943 dB**. *Disclosed:* the promoted 08-01 §8 `knee_interp.py` listing, reused verbatim here, hard-codes this base as 6.515377553550175 — 2.2×10⁻⁵ dB lower. Every `G_req` in §3.4 and §5.3 carries the listing's value; the difference is immaterial at the third decimal but is stated rather than left as two bases in one document. Grid rungs recomputed by the released bracket this session: `M_th_num`(480) = **0.1587475408418196** (reproducing 08-01's rung). Ratio biases used: 0.7 × 0.16894319463373791 = **0.11826023624361653** (N = 240), 0.7 × 0.1587475408418196 = **0.11112327858927372** (N = 480).

**Released streaming estimator** reproduced end-to-end: `run_all.measure_pulse_gain` returns **7.79670696148679** against the shipped `pulse_gain_dB_at_0p7_streaming` = 7.7967069614868425 — **5.2×10⁻¹⁴ apart, summation order**, exactly as 08-01 §1 reports (not "bit-for-bit"; that term belongs to the integrator).

**Scoring conventions**, 07-31 §2 / 08-01 §4 / 08-01 ratio-bias §1, adopted unchanged: seed-7 40-slot PRBS, first 4 slots dropped (36 scored), duty 0.8, raised-cosine edges of 2 rt, window [0.25, 0.72]·repT, drive 2×10⁻³, gain per '1' vs the identical-pattern M = 0 run, worst-case-'1' statistic, pp = raw '1'-level spread, floor = max-'0' referred to mean-'1'. Carrier-phase reference: centre of the **active** envelope window (0.4·repT at duty 0.8), with the slot-centre reading run as the robustness variant.

**Harness validation, in three stages:**

- **(a)** The promoted 08-01 §8 `fs_driver.py`, byte-verbatim, is **bit-identical** to released `solver.run(drive_kind='prbs')`: max |Δcav| = **0.0** over **250,167** steps.
- **(b)** The 07-25 probe rows reproduce to the digit: m = 8 eye **−1.46** / pp **4.91** / G_worst1 **+3.05**; m = 16 **+7.61** / **1.03** / **+4.13**; m = 22 **+12.51** / **0.27** / **+4.17**.
- **(c)** The density-recording shadow of §2 — which adds recorders to the released `_setup`/`_step_LF` stepping and changes nothing else — reproduces the promoted m = 30 / N = 240 ratio-bias row **to the last float digit**: G_worst1 = **8.287855791924017**, floor = **−11.828336851447219**, against the values all three assessors of [`notes/2026-08-01-ratio-bias-gain-table.md`](2026-08-01-ratio-bias-gain-table.md) independently recorded. Three further promoted rows reproduce in the same channel: m = 28 / N = 240 **8.1315 / −10.7312**, m = 28 / N = 480 **8.2586 / −10.4030**, m = 30 / N = 480 **8.4681 / −11.4628**.

**Candidate spec values, all recomputed:** strict `20·log₁₀(static_noise_margin(8, 10))` = **−11.821145417981018 dB**; round = **−10.0 dB**; r\* = 3/11 = **−11.285428608771253 dB**; the k = 5 reading `20·log₁₀(static_noise_margin(5, 10))` = **−13.759345678142145 dB**; the docstring reading = **−10.482210 dB**.

## 2. Half 1 — the derivation, with the algebra visible

### 2.1 The map

`fable-model-chain/cell.py` defines, with `N_TH` = 0.5 and `DN` = 1/`K_SHARP` = 0.125:

```
transfer(A, n_bias, beta, g_max, loss) = A · [ g_max·0.5·(1 + tanh((n_bias − beta·A − N_TH)/DN)) − loss ]
                                       ≡ A · g(A)
```

Two structural facts follow immediately, and everything else is a corollary.

**(i) `T(0) = 0` identically, for every parameter.** The output is the input times a gain; a zero input gives a zero output. Verified over every parameter combination tried. So A = 0 is *always* a fixed point, with multiplier `T′(0) = g(0)`.

**(ii) `g` is strictly monotone in A.** `dg/dA = −β·g_max/(2·DN)·sech²((n_bias − βA − N_TH)/DN)`. The sech² factor is strictly positive everywhere, so `dg/dA` has the constant sign of −β: **decreasing for β > 0 (depleting), increasing for β < 0 (enhancing)**, for all A.

### 2.2 The identity — what it proves, and what it does not

`T(A) = A` ⟺ `A = 0` **or** `g(A) = 1`. By (ii), `g(A) = 1` has **at most one transversal root**. Therefore

> **the fixed-point set of the released Eq. (5) map on [0, ∞) contains at most two points, for every (`n_bias`, β, `loss`, `g_max`).**

This is a property of the map's functional form, not of a scan, and it stands. Two corollaries sharpen it:

- *Depleting branch (β > 0, the released sign).* `g` decreasing means a stable '0' (`g(0) < 1`) forces `g(A) < g(0) < 1` for every A > 0 — **no positive fixed point exists at all**. On this branch a stable '0' and a '1' level are **mutually exclusive as fixed points of `T`**.
- *Enhancing branch (β < 0).* A stable '0' plus a repelling separatrix can exist — `n_bias` = 0.3, β = −1 at the released `g_max` gives `g(0)` = 0.119112 (attracting) and a separatrix at A\* = 0.155403, `T′` = +2.669 — but above it `g → g_max − loss` and `T(A) → 3.0412·A`: unbounded growth, no upper rail. Bounding it needs `g(∞) ≤ 1`, which deletes the separatrix. Note `g(0)` does **not** depend on β — β enters only through A.

**The inference this draft originally drew from the identity was invalid, and is withdrawn.** It read: a restoring element needs three fixed points, `T` has at most two, therefore no restoring element. That is the criterion for a **non-inverting** cell. `cell.py` line 25 states `N_TH = 0.5  # threshold parked mid-swing for inverting logic`, and `truth_table`'s docstring realises NOT via "bias (inverting)". **For an inverting cell the logic levels are the period-2 orbit of `T`** — fixed points of `T∘T`, the two-cell composition, which is the standard restoring element and is *not* of the form A·g(A). The identity does not transfer to it. §2.4 does the composition instead of asserting around it.

### 2.3 The confirming scan, with both artifact families disposed of

52,480 parameter sets (`n_bias` ∈ [−1, 3] × 41, β ∈ {±0.25, ±0.5, ±1, ±2, ±4}, `loss` ∈ [0, 3] × 16, `g_max` ∈ {0.5, 1, 1.5, 2, `G_amp`, 4, 6, 10}), roots counted on a 20,001-point geometric amplitude grid over [10⁻⁶, 500]:

| | count |
|---|---|
| parameter sets scanned | 52,480 |
| attracting '0' (\|g(0)\| < 1) | 18,950 |
| degenerate `g_max − loss == 1` exactly (excluded — see below) | 1,230 |
| **with more than one transversal positive fixed point** | **0** |

A first pass reported 15 and then 645 apparent counterexamples. **Both were artifacts and both are disposed of here rather than dropped**, because a reader is entitled to see why a scan that contradicts an identity was wrong and not the identity:

- The first 15 all had their **single** root land exactly on A = 2.0, which was duplicated at a two-piece grid junction; `sign(0) = 0` produced two sign *changes* from one root. Verified analytically: for (n_bias, β, loss, g_max) = (−0.5, −0.5, 0, 2) the root is A\* = 2.0 exactly, with `g(A*) − 1 = 0.000e+00`.
- The 645 all satisfy `g_max − loss == 1.0` **exactly**. On the enhancing branch `g(A) → g_max − loss`, so tanh saturates to 1.0 in double precision and `g(A) ≡ 1` over a plateau — the knife-edge `T(A) → A` with a line of **neutrally** stable points (`T′ = 1`), not two attractors with a separatrix. A measure-zero boundary, not bistability. (The plateau artifact has a **mirror branch** the released grid's non-negative `loss` never reaches: `loss = −1` exactly, where `g → −loss = 1` from the *other* tanh saturation. An adversarial rerun over `loss` ∈ {−1, −0.5, …} confirmed both branches and found no third category. Both are neutral `T ≡ A` lines.)

### 2.4 The two-cell composition — what the released map actually derives

`T∘T(A) = T(A)·g(T(A))` is the inverter pair. `T∘T(0) = 0` still, with multiplier `(T∘T)′(0) = T′(T(0))·T′(0) = g(0)²`, and it can carry **more** positive fixed points than `T`, because every period-2 point of `T` is one.

*Demonstrated (runnable, see listing §8 — released `cell.transfer`, imported and composed; fixed points of `T∘T` located by bisection over [0, 6] and their multipliers by central difference; the **same 52,480-set grid as §2.3**, degenerate families excluded):* **182 parameter sets carry a stable 2-cycle**, i.e. exactly the {attracting, repelling, attracting} triple. The decisive exhibit sits at `cell.transfer`'s **own signature defaults** — `n_bias` = 1, β = 1, `g_max` = `G_amp` = 3.0412372824652123 — with only `loss` moved to 1.6:

| level | A | `T(A)` | `T∘T(A) − A` | `(T∘T)′` | |
|---|---|---|---|---|---|
| '0' | 0.338728 | 0.415651 | −6.44×10⁻⁷ | −0.369448 | **attracting** |
| separatrix | 0.389145 | 0.389144 | +2.02×10⁻⁷ | +1.818971 | repelling |
| '1' | 0.415651 | 0.338726 | −6.35×10⁻⁷ | −0.369536 | **attracting** |

So a maximum tolerable '0'-residual **is** derivable from the released map. Two facts about the whole family decide what it is worth:

**(a) The empty slot is never stable — as an identity, not a count.** Every positive 2-cycle satisfies `g(a)·g(b) = 1` (multiply `a·g(a) = b` by `b·g(b) = a`), and `g` strictly decreasing gives `g(0) > b/a > 1`, so `(T∘T)′(0) = g(0)² > 1` **wherever a positive 2-cycle exists at all**. The census's 0-of-182 count is a corollary, not the evidence. At the exhibit, `g(0)` = 1.440217 so `(T∘T)′(0)` = 2.074226, repelling. An undriven slot grows away from zero. This matters because the '0'-floor spec is a statement about how much residue an **empty** slot may carry; the '0' this map offers is a driven level at 81.5 % of the '1' amplitude, not an empty slot.

**(b) The derived extinction is a family that reaches past round and r\*.** *(This subsection is corrected — the table below is the lattice census, whose "best" and two zero counts were falsified after the vote; read it with the frontier measurement that follows and with §10.)*

| statistic over the 182 stable 2-cycles | extinction (dB) |
|---|---|
| best (most negative) | **−6.0413** (n_bias 0.5, β 0.5, loss 0.6, g_max 10; levels 0.13044 ↔ 0.26149) |
| median | −1.857 |
| worst | −0.0439 |
| at the signature defaults (loss 1.6) | **−1.7776** |
| **count reaching −10.0 dB (round)** | **0** |
| **count reaching −11.285 (r\*) or −11.821 (strict)** | **0** |

**Corrected (2026-08-05, executed against released `cell.transfer`).** The lattice above understates the frontier badly, and the reason is aliasing, not incompleteness. The census steps `n_bias` on a 0.1 lattice (`linspace(-1, 3, 41)`), while the deep attracting band at `g_max` = 10, `loss` = 0 lies **strictly between the lattice points 0.5 and 0.6**: at *neither* 0.5 nor 0.6 does an attracting 2-cycle exist at all, while at `n_bias` = 0.53981718 the extinction is **−11.6936 dB**. The census stepped over the whole feature. Tracing the frontier onto the 2→4 period-doubling boundary (multiplier → −1):

| `g_max` (β > 0, `loss` = 0) | `n_bias`\* | extinction (dB) |
|---|---|---|
| 8.00 | 0.56085577 | −10.9333 |
| 9.00 | 0.54951767 | −11.3463 |
| 9.50 | 0.54449165 | −11.5271 |
| 9.75 | 0.54211346 | −11.6120 |
| 9.97 | 0.54008859 | −11.6840 |
| **10.00** (box ceiling) | **0.53981718** | **−11.6936** |

**So the released map's family contains round (−10.0) and r\* (−11.2854), and stops 0.128 dB short of strict (−11.8211) only because the census box stops at `g_max` = 10.** Lift that ceiling and strict falls inside too: −11.9902 dB at `g_max` = 11, then −12.2464 / −12.8426 / −13.4898 at 12 / 15 / 20 (no attracting 2-cycle survives by 40). The map is not silent on the floor and it is not uniformly looser than the fork — it is **indifferent** to it, because it will supply any of these values depending on constants the chain never fixes.

**A structural fact that shrinks the census by 5×, demonstrated.** β is a pure amplitude scale, not a dynamical parameter: substituting B = β·A conjugates the map to a β-free one, `B' = B·[g_max·0.5·(1 + tanh((n_bias − B − N_TH)/DN)) − loss]`. Measured across β ∈ {0.25, 0.5, 1, 2, 4} at the counterexample, the extinction and the multiplier are **identical to eight decimals** (−11.672387 dB, −0.99582497) and the orbit scales exactly as 1/β (β·orbit = 0.06939919 ↔ 0.26605641 in every case). Negative β yields **no positive 2-cycle at all** (checked at β = −0.25, −1, −4). So of the 52,480 sets, the 26,240 with β < 0 contribute nothing and the 26,240 with β > 0 are five exact copies of 5,248 distinct systems — the census has roughly a fifth of the independent content its count implies, and none of the extra resolution where it was needed.

*A secondary reading, for completeness.* If the inverting cell is instead **clock-pumped** — a separate carrier `A_c` gated by the input, `T_inv(A) = A_c·g(A)`, a map that does not appear in `cell.py` — then `T_inv∘T_inv` is bistable for `A_c` ∈ [0.16, 0.79] at the released `g_max` and the signature's default `loss` = 0, with the derived residual running **−1.23 to −12.45 dB** across that window and the released heuristic's 0.2564 margin fraction reproduced at `A_c` = 0.7268. **This is a reconstruction, in-model, not released code**, and it is reported only because it reaches the same place by another route: the requirement is a family wide enough to contain every value under argument, indexed by a parameter the chain never fixes.

### 2.5 What this costs the record

*Demonstrated (source read).* `cell.py`'s module docstring asserts that "the saturating tanh supplies the logic nonlinearity and **the restoring rail**", and that "the threshold sharpness k = beta·A_swing/dn sets **the static noise margin** and the disorder tolerance". `fable-model-chain/README.md` line 26 lists `cell.py` as supplying "transfer model, compression, cascade, **noise margin**, ISI, truth table" for "Eq (5), logic". Three findings, the first two **corrected from this reply's first draft, which called them false**:

1. **The docstring's "restoring rail" is real in the inverting reading — but it is not a logic rail.** The first draft called it false; the adversarial composition lens refuted that, and §2.4 confirms the rail exists in `T∘T`. What it does not do is supply logic levels *the chain fixes*: the empty slot is never stable (an identity — §2.4(a)), and the extinction the rail delivers is a free-parameter family running to at least −11.69 dB inside the census box and deeper outside it (§2.4(b), corrected 2026-08-05). **So the claim should be read as "the map has an attractor", not "the map restores a '0' against a '1'"**, and the difference is the whole '0'-floor question.
2. **The docstring's causal claim is realisable but is not what the code computes.** The first draft said the two halves of the sentence were "not connected in code". More precisely: a static noise margin **is** derivable from the transfer, via the `T∘T` separatrix, while `static_noise_margin(8, 10 dB)` returns 0.2564 (−11.82 dB) from a formula that **never calls `transfer`**. The two routes are both available, and the transfer route does not return a number — it returns a range that depends on constants the chain never fixes, reaching −11.69 dB inside the census box and past the heuristic's own −11.82 dB outside it (§2.4(b), corrected 2026-08-05). **The disagreement is therefore not a fixed 6–10 dB offset, as this note first stated; it is that one route yields a value and the other yields a family containing it.** The published key is the one that ignores the map.
3. **The transfer is not exercised by the released pipeline.** `grep` over `run_all.py` and `figures.py`: they consume `cascade_per_cell_gain_dB`, `compression_dB` and `static_noise_margin` — **`transfer` is called by neither, and produces no `results.json` value** (nor is `truth_table` called outside `cell.py`; it has the same status). So nothing here retires a published number; what it touches is documentation and manuscript language.

*Demonstrated (arithmetic).* The heuristic's own internal ambiguity:

| reading | value | dB |
|---|---|---|
| code, k = 8, 10 dB (**the published key**) | 0.25641458774368575 | **−11.821145** |
| docstring form, k = 8, 10 dB | 0.2991503523676334 | **−10.482210** |
| code, k = 5, 10 dB | 0.2051316701949486 | −13.759346 |
| code, k = 16, 10 dB | 0.2991503523676334 | −10.482210 |
| code, k = 8, 20 dB | 0.3375 | −9.434524 |

**The docstring/code gap is +1.3389 dB**, against a strict-vs-round fork of 1.821 dB. A specification being argued to the second decimal rests on a function whose prose and code disagree by three quarters of the fork.

**On the k = 5 candidate, stated plainly because the prompt raised it:** `disorder.py`'s `K_MIN = 5.0` is a **yield** criterion — the sharpness floor a cell must retain after charge-puddle broadening (`k_eff = n/√((n/k0)² + σ²) ≥ K_MIN`). It is not a tolerance on '0'-slot residue, and feeding k = 5 into the butterfly formula answers a different question. **This session declines to promote it to a floor spec**; it is listed in §5 only so the adjudication is complete, and doing otherwise would be the choose-a-spec-by-analogy move the prompt itself forbids.

## 3. Half 2 — the denomination, measured in paired channels

### 3.1 The mechanism: two denominations, two planes

The released floor is a ratio of per-slot peaks of `cav` = max_x |hu/h − u0| (`solver.py:99`) — a **velocity** perturbation maximised over space. The spec's `extinction_dB` and `cell.A_SAT` = 0.02 denominate a **density** swing. The shadow records four channels of one identical run:

| channel | quantity | plane |
|---|---|---|
| `cav_u` | max_x \|hu/h − u₀\| | intracavity — **the released channel** |
| `cav_h` | max_x \|h − 1\| | intracavity |
| `drn_u` | \|hu[−1]/h[−1] − u₀\| | drain (`solver.py:98`, rectified) |
| `drn_h` | \|h[−1] − 1\| | drain |

*Demonstrated (8-slot diagnostic, m = 30 / N = 240, argmax index recorded every step; no *numerical* verdict rests on it, but the plane attribution in executive item 4 and the §6 (i) recommendation are its consequences and are exactly as strong as it is):* the velocity maximum sits at median index **8 of 239 — 3.3 % of the cell**, with 57 % of steps inside the first 5 %; the density maximum sits at median index **239 — 100 % of the cell**, with 63 % of steps inside the last 5 %. The reason is in the boundary conditions of `solver._step_LF`: the source is density-clamped (AC short → density node, **velocity antinode**) and the drain is current-clamped (AC open → velocity node, **density antinode**). Confirming this, `drn_h` equals `cav_h` **exactly** on five of eight measured rows and to within 0.002 dB on the other three (all m = 30) — the density maximum *is* the drain value.

**So the released floor is a source-plane velocity ratio, while the swing the spec denominates — and the field the next cell actually receives — is drain-plane density.** This is the same class of error the 07-17 plane audit found, applied to the number the strict-vs-round fork is being argued over.

### 3.2 The paired table

All rows ratio bias 0.7·`M_th_num`(N) recomputed at the row's own grid, duty 0.8, drive 2×10⁻³, 36 scored slots. Δ columns are **paired** — computed inside one run, so the ~1 dB carrier-phase sensitivity of 07-31 §2 is common-mode. Every configuration is run at three convention triples: reference (active-envelope phase, seed 7), a second carrier phase (slot centre), and a second seed (11).

| m (GHz) | N | convention | floor `cav_u` | floor `cav_h` | **Δfloor (paired)** | `drn_u` | `drn_h` |
|---|---|---|---|---|---|---|---|
| 28 (71) | 240 | reference | −10.7312 | −11.1506 | **−0.4194** | −11.3617 | −11.1506 |
| 28 (71) | 240 | slot phase | −10.9308 | −11.0390 | −0.1081 | −11.4129 | −11.0390 |
| 28 (71) | 240 | seed 11 | −10.7416 | −11.1603 | −0.4187 | −11.3718 | −11.1603 |
| 30 (67) | 240 | reference | −11.8283 | −11.7734 | **+0.0549** | −11.8131 | −11.7750 |
| 30 (67) | 240 | slot phase | −11.7825 | −11.7206 | **+0.0619** | −11.7959 | −11.7225 |
| 30 (67) | 240 | seed 11 | −11.8437 | −11.7870 | **+0.0567** | −11.8259 | −11.7886 |
| 28 (71) | 480 | reference | −10.4030 | −10.7936 | −0.3906 | −11.0119 | −10.7936 |
| 28 (71) | 480 | slot phase | −11.0040 | −10.6880 | +0.3161 | — | −10.6880 |
| 28 (71) | 480 | seed 11 | −10.4018 | −10.7912 | −0.3895 | — | −10.7912 |
| 30 (67) | 480 | reference | −11.4628 | −11.9080 | **−0.4452** | −11.9269 | −11.9080 |
| 30 (67) | 480 | slot phase | −11.3966 | −11.7708 | **−0.3742** | — | −11.7708 |
| 30 (67) | 480 | seed 11 | −11.4672 | −11.9113 | **−0.4440** | — | −11.9113 |

The reference rows in the `cav_u` column are the promoted 08-01 rows, reproduced: m = 28 / N = 240 **−10.7312** (with gain 8.1315), m = 30 / N = 240 **−11.8283** (8.2879), m = 28 / N = 480 **−10.4030** (8.2586), m = 30 / N = 480 **−11.4628** (8.4681). The paired gains move +0.304 / +0.376 / +0.225 / +0.301 dB into the density channel.

**Robustness, as the prompt requires for any sub-1 dB verdict — and the sign change is now replicated.** At **m = 30** the paired Δfloor is **+0.055 / +0.062 / +0.057 at N = 240** and **−0.445 / −0.374 / −0.444 at N = 480**: the sign change survives both a second carrier phase and a second seed **at both grids**, while the *absolute* floors move up to 0.07 dB under the same perturbations. (The first draft rested the sign change on a single unreplicated N = 480 run; the adversarial composition lens flagged that, and the four N = 480 variant rows above were run before publication in response.) At **m = 28** the paired delta is seed-stable to 4 decimals but **not phase-stable** (−0.419 → −0.108 at N = 240; −0.391 → **+0.316** at N = 480, itself a sign change) — **so no verdict is rested on the m = 28 paired delta**; only m = 30's is used.

### 3.3 The verdict on the two rows the prompt names

*Demonstrated:*

| row | velocity floor | strict margin | density floor | strict margin | round (both) |
|---|---|---|---|---|---|
| m = 30 / N = 240 | −11.8283 | **+0.0072 → nominal pass** | −11.7734 | **−0.0477 → fail** | pass / pass |
| m = 30 / N = 480 | −11.4628 | −0.3584 → fail | −11.9080 | **+0.0868 → pass** | pass / pass |
| m = 28 / N = 240 | −10.7312 | −1.0899 → fail | −11.1506 | −0.6706 → fail | pass / pass |
| m = 28 / N = 480 | −10.4030 | −1.4181 → fail | −10.7936 | −1.0275 → fail | pass / pass |

- **The m = 30 / N = 240 strict boundary is convention-unstable, and the denomination is only the third convention that flips it.** The promoted note had already demoted its +0.007 dB to "a boundary, not a pass". In the released velocity channel it becomes a **fail (−0.0387 dB)** under the slot-centre carrier phase alone; in the denomination the spec is actually written in it is a **fail by 0.048 dB**. Three conventions were varied and two of them flip the verdict.
- **At N = 480 it moves the other way** — velocity fails strict by 0.358, density passes by 0.087.
- **The m = 28 round-spec straddle does not move at any measured grid**: both denominations clear −10 dB at N = 240 and N = 480. The straddle lives in the continuum, and what moves it there is the convergence order (§4), not the denomination.

**The honest reading of a verdict that flips in opposite directions at two grids is not "the density number is the right one". It is that the strict test is being adjudicated at a precision the observable does not define** — a ±0.4 dB denomination ambiguity and a sign that changes with grid, against margins of 0.007–0.09 dB.

### 3.4 The control the clearance needed

A gain leg that moves +0.3 dB under denomination would move the F = 2 clearance only if the **requirement** leg did not move with it. So the 08-01 §5 streaming knee sweep was re-run in both channels of one identical run (all-ones train, released per-slot-mean estimator, ratio bias, log-amplitude 1-dB interpolation, N = 240).

| m | channel | observable | knee | A_SAT | `G_req_gated(F2)` |
|---|---|---|---|---|---|
| 28 | `cav_u` | active-only | 0.01235 | 0.02426 | 6.9854 |
| 28 | `cav_u` | gain-ratio | **0.01208** | 0.02374 | **7.0051** |
| 28 | `cav_h` | active-only | 0.01300 | 0.02555 | 6.9413 |
| 28 | `cav_h` | gain-ratio | 0.01243 | 0.02442 | 6.9797 |
| 30 | `cav_u` | active-only | 0.01228 | 0.02414 | 6.9900 |
| 30 | `cav_u` | gain-ratio | **0.01203** | 0.02365 | **7.0088** |
| 30 | `cav_h` | active-only | 0.01252 | 0.02460 | 6.9732 |
| 30 | `cav_h` | gain-ratio | 0.01198 | 0.02354 | 7.0132 |

The bolded `cav_u` rows reproduce 08-01 §5's ratio-leg knees (0.01208, 0.01203) and requirements (7.005, 7.009) exactly. *Demonstrated:* **the requirement leg is essentially denomination-blind** — it moves −0.025 dB (m = 28) and +0.004 dB (m = 30), i.e. 8.3 % and 1.2 % of the gain-leg move. **The mechanism is not that compression is denomination-blind — it is not.** The knee itself moves 5.3 % between channels at m = 28 (0.01235 → 0.01300, active-only) and 2.9 % in the gain-ratio convention. The requirement is insensitive for a *formulaic* reason: `G_req = 10log₁₀(1 + (A_op/A_SAT)²/2) + base` with `A_op/A_SAT` ≈ 0.48, so the compression term is ≈ 0.11 and the logarithm is stiff — a 3–5 % channel shift in A_SAT compresses to under 0.05 dB. **This makes the requirement leg's blindness weak evidence, not strong evidence**: it reflects the ledger's algebraic form near this ratio, and `A_op` = 0.0116 is carried across unchanged and un-re-denominated.

So the clearance inherits almost the whole gain delta (*demonstrated legs, in-model transfer, `A_op` imported per 08-01 §0.2*):

| m (GHz) | clearance, released velocity | clearance, density | Δ |
|---|---|---|---|
| 28 (71) | **+1.126** (promoted, off the rounded requirement: +1.127) | **+1.456** | +0.330 |
| 30 (67) | **+1.279** | **+1.650** | +0.371 |

The velocity column reproduces the promoted +1.127 / +1.279 to within 0.001 dB — m = 30 matches at +1.279, and m = 28 reads +1.126 against the promoted +1.127 because the promoted figure subtracts the rounded 7.005 while this one subtracts the unrounded 7.0051. **The gain leg's comfort is therefore understated, not overstated, by the released denomination — which cuts against the direction one might expect and does not rescue the floor leg, which is the binding one.**

## 4. The convergence order, fitted rather than assumed

The prompt forbids inheriting the promoted 1/N intercepts as demonstrated. Fitting `F(N) = F∞ + c·N^(−p)` on the three promoted ratio-bias floor rungs (240 / 480 / 720, refinement ratios 2.0 then 1.5). **Rung precision, stated because it matters:** the promoted §3 table prints m = 30 and m = 28 to four decimals but m = 26 and m = 22 to two, and for m = 26 a four-decimal N = 240 value (−10.6023) also exists in 08-01 §0.6's appended assessment record. The m = 26 row is therefore given **both ways**.

| m (GHz) | p (3-rung fit) | F∞ at fitted p | F∞ at p = 1 (480/720) | F∞ at p = 1 (240/480) |
|---|---|---|---|---|
| 30 (67) | **0.706** | −10.884 | −11.031 | −11.097 |
| 28 (71) | **0.548** | **−9.693** | −9.978 | −10.075 |
| 26 (77) † | **0.136** / 0.147 † | −6.697 / −6.975 † | −9.680 | −9.900 / −9.898 † |
| 22 (91) | **0.888** | −7.611 | −7.660 | −7.690 |

† m = 26 given both ways: the first figure uses the §3 table's printed two-decimal rungs (−10.60 / −10.25 / −10.06), the second substitutes the four-decimal −10.6023 for N = 240. The 2-decimal reading is the one a reader following §3 alone reproduces.

*Demonstrated (arithmetic on the promoted rungs):* every fitted order is **below 1**, so first-order Richardson **understates** the continuum floor in every case.

- **m = 28 (71 GHz):** the published "straddle" (−9.978, intercepts either side of −10) becomes **−9.693 dB at its own fitted order — a 0.31 dB fail** of the round spec. This independently reproduces the 2026-08-02 lab claim.
- **m = 30 (67 GHz):** **−10.884 dB**, still clearing round by +0.88 dB. The robust rung survives.

*In-model, and honestly ill-conditioned:* three rungs on two different refinement ratios cannot separate "not yet asymptotic" from "not first order". m = 26 is the proof, twice over: reading its N = 240 rung at two decimals (−10.60) gives p = 0.136 and F∞ = −6.697, at four (−10.6023) p = 0.147 and F∞ = −6.975 — and an adversarial rerun found that perturbing only its N = 720 rung by ±0.005 dB (its own quote rounding) moves p across 0.100–0.196 and F∞ across −5.36 to −7.82, a **2.46 dB** swing. Against the p = 1 intercept of −9.68 that is a 2.7–3.0 dB excursion driven entirely by quote precision. **The sign of the correction is robust; the magnitudes are not.** The fourth rung that would settle it is unreachable in the released chain — the `measure_Mth_num` bracket ceiling is N ∈ (860, 880], where the growth-rate zero leaves `linspace(1.05, 1.30)`.

## 5. The adjudication

### 5.1 Every candidate spec against every rung

Floors are the promoted ratio-bias rows of `notes/2026-08-01-ratio-bias-gain-table.md` §3, in the released velocity denomination, with the continuum column at the **fitted** order of §4 (in-model). ✓ = clears, ✗ = fails.

| spec | dB | 67 GHz (m = 30) | 71 GHz (m = 28) | 77 GHz (m = 26) | 91 GHz (m = 22) |
|---|---|---|---|---|---|
| round | −10.000 | ✓ 240/480/720, ✓ continuum (−10.88) | ✓ 240/480/720, **✗ continuum (−9.69)** | ✓ 240/480/720 (+0.06 at 720), continuum unresolvable | ✗ everywhere |
| r\* (3/11) | −11.285 | ✓ 240, ✓ 480, ✓ 720, ✗ continuum | ✗ everywhere | ✗ everywhere | ✗ everywhere |
| strict | −11.821 | **boundary** 240 (+0.007, → ✗ in density), ✗ 480/720, ✗ continuum | ✗ everywhere | ✗ everywhere | ✗ everywhere |
| k = 5 reading | −13.759 | ✗ everywhere | ✗ everywhere | ✗ everywhere | ✗ everywhere |
| docstring reading | −10.482 | ✓ 240/480/720, ✗ continuum | ✓ 240 (−10.73), ✗ 480/720 | ✓ 240 (−10.60), ✗ 480/720 | ✗ everywhere |
| **derived family (§2.4, clock-pumped reading)** | **−1.23 … −12.45** | ✓ over most of the family | ✓ over most of the family | ✓ over most of the family | ✓ for `A_c` ≲ 0.45 |

*Demonstrated at the grids; the continuum column is in-model; the derived family is in-model on a reconstructed map.* Only **67 GHz under the round spec** survives every reading this session can defend, and it survives the density denomination at N = 480 (−11.908) while failing it at N = 240 (−11.773) under strict.

The last row is the point of the whole exercise: **the only reading of the released chain that actually derives a requirement is loose enough that even 91 GHz (−7.98 dB) passes over part of its range.** A spec chosen from that family by preference would license anything.

### 5.2 Where the spec would have to come from instead

Item 1 says the released chain does not license one. The prompt names two alternative sources — the bench, or Part II's own decode demand. The second is measurable now.

*Demonstrated (released `fable-model-quantum`; a floored-'0' replica of `qmac.levels_at_decision` that carries a coherent residual of relative amplitude r on the '0' arm, everything else unchanged; **validated bit-for-bit against released `error_2bit` and `error_1bit` at r = 0 at 353/300/77/20 K, and against the published `T_2bit_below_1e-3` = 58.52734375 and `T_1bit_below_1e-3` = 243.765625 using the identical bisection**):*

| T (K) | largest tolerable r | floor demanded (dB) |
|---|---|---|
| 48 | 0.0758 | **−22.41** |
| 40 | 0.1342 | −17.45 |
| 30 | 0.2085 | −13.62 |
| 25 | 0.2449 | −12.22 |
| 20 | 0.2787 | **−11.10** |
| 15 | 0.3067 | −10.27 |
| 10 | 0.3240 | −9.79 |
| 4 | 0.3283 | **−9.68 (saturated)** |

Two things follow.

**(a) Each candidate spec corresponds to a maximum operating temperature.** *In-model at the point of assertion* (only the r = 0 replica validation below is demonstrated; the Part I '0'-residue → QMAC coherent-input transfer is an assumption no promoted note establishes): if a spec is exactly attained and that transfer is taken as identity, the demand crosses **round −10.0 dB at 12.73 K**, **r\* −11.2854 at 20.93 K**, **strict −11.8211 at 23.35 K**, and the **k = 5 reading −13.7593 at 30.46 K**. So the strict-vs-round argument is, on this leg, an argument about **10.6 K** of QMAC operating headroom — which is what the 2026-08-02 lab post priced, and this session confirms.

**(b) The demand saturates and can never be stricter than ≈ −9.7 dB.** Below ~10 K it stops tightening because `qdecode.threshold_band_variance` (k_dec = 16, with c an **open** bench quantity per 07-15) is a deterministic transfer that does not cool away. *In-model consequence:* the decode demand can serve as a floor spec only in the narrow window where it lands between the candidates — roughly 13–23 K. Above ~23 K it is stricter than any candidate on the table (−22.4 dB at 48 K, which **no** gated rung approaches); below ~13 K it is looser than all of them.

*Labels, stated:* every kelvin figure here is **in-model twice over** — the Part I '0'-residue → QMAC coherent-input-amplitude transfer is a chain-crossing assumption **no promoted note establishes**, and the threshold band carries 07-15's open c. Also recorded: `qerrors.NM_CLASSICAL` = 0.2564 is the chain's `noise_margin_frac` rounded to four decimals (worth −0.000494 dB), so Part II's published `classical_BER_300K` / `classical_BER_353K` already presume the same heuristic — the two Parts are not independent witnesses to it.

### 5.3 Does `f_max_F2_gated_GHz` = 69 [63, 74] move?

**No — and this session both removes and hardens a blocker.**

`notes/2026-08-01-ratio-bias-gain-table.md` §0.5 names two prerequisites for re-adjudicating it in the ratio convention. **The first is now measured** (§3.4 and the dedicated sweep): the **m = 26 gated streaming knee** at N = 240, ratio bias, is **0.01260 active-only / 0.01230 gain-ratio**, A_SAT 0.02476 / 0.02417, `G_req_gated(F2)` = **6.968 / 6.989 dB** — from a run whose m = 28 and m = 30 knees reproduce 08-01 §5 to the digit. Against the promoted m = 26 / N = 240 ratio-bias gain of 8.0292 dB the clearance is **+1.040 dB**, and the knee is monotone in slot length (0.01230 / 0.01208 / 0.01203 at m = 26 / 28 / 30), so the requirement *falls* slightly as slots shorten.

**The second prerequisite is not merely undecided — item 1 shows the released logic element does not adjudicate it.** What that element derives is not a floor but a **family** — attracting extinctions running to at least −11.69 dB inside the census box, containing round and r\* and reaching past strict once the box's `g_max` ceiling is lifted (§2.4(b), corrected 2026-08-05) — denominated on a '0' that is not an empty slot. So the frontier key is **neither moved nor re-adjudicated**, exactly as the promoted record left it, and the reason has changed from "not yet decided" to "not decidable from this chain's own logic map, which returns whichever value its unfixed constants are set to". 77 GHz's gain leg is now measured on both sides and is comfortable; its floor leg (round margin +0.056 dB at N = 720, continuum unresolvable at p = 0.136–0.147) is not.

## 6. Pre-registered keys

Grep-checked collision-free against `fable-model-chain/results.json`, `fable-model-quantum/results.json`, all of `notes/`, and `papers/`.

- **WITHDRAWN before publication: `transfer_map_restoring_pair_exists` = false.** Registered in the first draft and **struck by the adversarial composition lens**, which produced the counterexample: the triple exists in `T∘T`. Recorded here as withdrawn rather than deleted, so the vote record and this reply stay auditable. Replaced by:
- **FALSIFIED after the 2-of-3 vote, and replaced: `transfer_2cycle_extinction_dB`** = best −6.0413 / median −1.857 / **0 of 182** reaching −10 dB. Its own stated falsifier — one parameter set whose released-`transfer` 2-cycle has extinction at or beyond −10 dB — **was met by the recorded dissent and confirmed twice by execution** (§10). Recorded as falsified rather than deleted, so the vote record stays auditable. Replaced by:
- **`transfer_2cycle_extinction_family_dB`** = the released map supplies a **family**, not a bound: attracting 2-cycle extinction runs from **−0.0439** to **−11.6936 dB** inside this note's own census box (β > 0, `n_bias` ∈ [−1, 3], `loss` ∈ [0, 3], `g_max` ≤ 10), the deep end traced on the 2→4 period-doubling boundary and monotone in `g_max`; the bound is the **box's** `g_max` ceiling, not the dynamics — at `g_max` = 11 it is **−11.9902 dB**, past the strict anchor. The family therefore contains round (−10.0) and r\* (−11.2854). **Demonstrated (executed against released `cell.transfer`; see §10 for the method and the three checks).** *Falsified by* a search over the same box returning a deepest attracting extinction differing from −11.69 dB by more than 0.1 dB, or by a released-code route that fixes `n_bias`, `g_max` or `loss`.
- **`transfer_beta_is_an_amplitude_scale`** = true: B = β·A conjugates `transfer` to a β-free map, so extinction and multiplier are β-invariant (identical to 8 decimals across β ∈ {0.25, 0.5, 1, 2, 4}; orbit scales as 1/β) and β < 0 admits no positive 2-cycle. **Demonstrated.** *Falsified by* one β > 0 whose 2-cycle extinction differs from the β = 1 value at the same (`n_bias`, `g_max`, `loss`).
- **`transfer_empty_slot_repelling_identity`** = true by identity, not by census: `g(a)·g(b) = 1` for every positive 2-cycle, and `g` decreasing gives `g(0) > b/a > 1`, so `(T∘T)′(0) = g(0)² > 1`. **Demonstrated (closed form; `g(a)·g(b)` measured 1.000000000).** *Falsified by* a positive 2-cycle with `g(a)·g(b) ≠ 1`.
- **`clockpumped_inverter_residual_band_dB`** = **[−12.45, −1.23]** over the bistable window `A_c` ∈ **[0.16, 0.79]**, with the released heuristic's 0.2564 margin fraction reproduced at **`A_c` = 0.7268**. **In-model on a reconstructed clock-pumped map** (`T_inv(A) = A_c·g(A)`, **not released code**); the fixed points and their stability are **demonstrated (runnable, see listing §8)** on that map. Secondary to `transfer_2cycle_extinction_dB`, which uses the released map. *Falsified by* a bistable window materially different from [0.16, 0.79] at the released `g_max` and `loss` = 0, or by a released-code route that fixes `A_c`.
- **`static_noise_margin_docstring_code_gap_dB`** = **+1.3389** — 20·log₁₀ of the docstring form (0.2991503523676334) minus 20·log₁₀ of the code form (0.25641458774368575) at k = 8, 10 dB. **Demonstrated (arithmetic).** *Falsified by* any reading in which the published `noise_margin_frac` is the docstring form.
- **`floor_denomination_delta_dB_m30`** = **+0.055** (N = 240) / **−0.445** (N = 480), band **[−0.60, +0.15]** — density-referred minus velocity-referred '0'-floor, paired inside one run, duty-0.8 ratio bias, drive 2×10⁻³. **Demonstrated (runnable, see listing §8)**, replicated at both grids under a second carrier phase (+0.062 / −0.374) and a second PRBS seed (+0.057 / −0.444). *Falsified by* a paired rerun differing by more than 0.10 dB at either grid. The **sign change between grids is part of the key** — a rerun showing one consistent sign at both grids falsifies it.
- **`gated_clearance_density_denom_dB_N240`** = **+1.456** (m = 28) / **+1.650** (m = 30), band **[+1.2, +1.9]** — gain and requirement both in the density channel at N = 240, ratio bias. **Demonstrated legs; in-model as a margin** (cross-observable transfer, and `A_op` imported per 08-01 §0.2). *Falsified by* a rerun moving either value by more than 0.1 dB.
- **`knee_gated_duty0p8_streaming_m26_N240`** = **0.01230** (gain-ratio) / **0.01260** (active-only), band **[0.0116, 0.0131]**; **`G_req_gated_F2_dB_m26_N240`** = **6.989** (gain-ratio), band **[6.85, 7.15]**. **Demonstrated (runnable, see listing §8).** *Falsified by* a rerun of the same sweep differing by more than 2 % in the knee. Non-contest: this **adds** the m = 26 rung 08-01 §5 stopped short of; its m = 28 and m = 30 values are reproduced, not contested.
- **`gated_floor_convergence_order_p`** = **0.71 / 0.55 / 0.14 / 0.89** at m = 30 / 28 / 26 / 22 (m = 26 spans 0.136–0.147 on quote precision alone), band **[0.1, 1.0]** — three-rung fit of `F(N) = F∞ + c·N^(−p)` on the promoted §3 floors. **Demonstrated (arithmetic); the resulting continuum floors are in-model and ill-conditioned.** *Falsified by* a four-rung ladder returning p ≥ 1 at m = 28 or m = 30.
- **`decode_floor_demand_1e3_dB`** = **−22.41 (48 K) / −11.10 (20 K) / −9.68 (T → 0 saturation)**, with spec-crossing temperatures **12.73 K (round), 20.93 K (r\*), 23.35 K (strict)**. **In-model** (chain-crossing transfer; 07-15's open c), over a replica **demonstrated** bit-for-bit against the released decode at r = 0. *Falsified by* any physical accumulator or decode topology that removes the static threshold-band term, which would unsaturate the T → 0 limit.

**Grading the record this consumes.** `notes/2026-08-01-ratio-bias-gain-table.md`: all four re-run ratio-bias rows reproduce to the digit; its §5 demotion of the m = 30 / N = 240 strict "pass" to a boundary is **confirmed and strengthened** (in the spec's own denomination it is a fail); its Limitation 7 concession is **discharged in the negative** — the order is not 1, it is 0.15–0.89, and its m = 28 continuum "straddle" resolves to a 0.31 dB fail; its §0.5 m = 26 prerequisite is **delivered**; its `f_max_F2_gated_GHz` is **neither moved nor re-adjudicated**. `notes/2026-08-01-gated-requirement-round-trip.md` §5's ratio-leg knees and requirements are reproduced to the digit and its `A_op` caveat is inherited by every clearance above. `notes/2026-08-01-bench-gate-g1-reissued.md`: its §2(v) bias rule is used throughout, and **its §1 instinct is vindicated from an unexpected direction** — it pinned the bias convention bench-facing; this session shows the *observable* needs pinning too. `notes/2026-07-17-what-the-38-quanta-knee-denominates…`: its plane-audit method is applied and finds a second plane mislabel. `notes/2026-07-15-finite-sharpness-is-not-a-variance.md`: its open c is carried on every kelvin figure. `notes/2026-07-22-cavity-ringdown-isi.md`: the residual is treated as ring-down throughout, never as additive noise. No `results.json` value is contested; no promoted key is reopened.

**Part III consequence (in-model, honest).** The decisive open item does not resolve — it **dissolves and re-forms one level down**. "Strict or round?" presupposes that the released chain has a '0'-floor requirement in that neighbourhood to be strict or round about. **It has no such requirement to be strict or round about** — it has a family running to at least −11.69 dB that *contains* round and r\* and reaches past strict once the census box's `g_max` ceiling is lifted, resting on a '0' state that is not an empty slot (item 1). The presupposition fails not because the map is silent, and not because it is looser (this note's falsified reading), but because it will return whichever value the free constants are set to. The number both specs are compared against is read in the wrong denomination at the wrong plane (item 4), and the strict test's verdict is unstable under all three conventions varied (item 5). WP1's queue gains, in priority order: **(i) pin the floor OBSERVABLE — the drain-plane density ratio is the physically motivated choice, since that is the field the next cell receives and the swing `A_SAT` denominates — before any further floor-spec argument;** (ii) fix `cell.static_noise_margin`'s docstring/code disagreement, or state which is intended, since the published key rests on the code and the manuscripts may rest on the prose; (iii) reconcile the two noise-margin routes — the `T∘T` separatrix gives 0.35–0.65 of swing, `static_noise_margin` returns 0.2564, and nothing in the chain says which governs; and either qualify the "restoring rail" language in `cell.py` and `fable-model-chain/README.md` or state the extinction it actually delivers, since a reader takes "rail" to mean a logic rail and the map's is a free-parameter family, not a level; (iv) widen the `measure_Mth_num` bracket so a fourth floor rung exists and the convergence order stops being a three-point guess.

## 7. Limitations, and what I did not run

1. **Half 1 is about the released compact map, not the fabric.** `cell.transfer` is documented as "single cell, instantaneous". The physical restoration candidate is the saturating solver cavity, which this session does **not** analyse. A reader who converts item 1 into "the Fable fabric cannot restore logic levels" has over-read it.
1b. **The first draft of this reply asserted a universal negative that was refuted before publication**; §2.2's inference, not its identity, was wrong. A reader comparing this text against the vote record should read §9. The corrected §2.4 uses the **released** map composed with itself; the clock-pumped variant at the end of §2.4 remains **my reconstruction**, in-model, and is secondary.
1c. **The 182-cycle census was a grid scan, it was aliased, and it was falsified — this is what happened.** The hedge recorded here anticipated exactly the failure that occurred: a parameter set with a sub-−10 dB extinction exists, the dissent found it, and the key fell by its own criterion (§10). Two corrections follow. §2.4(a) no longer rests on the census at all — it is an identity (`g(a)·g(b) = 1` ⇒ `(T∘T)′(0) = g(0)² > 1`), so the empty-slot half needs no grid and cannot be falsified by one. §2.4(b) does still rest on a search, and the residual limitation is sharper than "not exhaustive": the deep band **hugs the 2→4 period-doubling boundary**, which is a measure-small set that any fixed lattice will step over — the census's 0.1 `n_bias` lattice straddled it exactly. The corrected frontier (−11.6936 dB at the box ceiling) is itself a numerical search on that boundary and should be read as a **lower bound on the family's depth**, not as its supremum.
1d. **Half 1 analyses `cell.py:transfer`, which is not Part I's Eq. (5).** Established 2026-08-05 in the assessment of [Fable Session — 2026-08-05](https://github.com/ryoji-info/FableComputer/discussions/99): the manuscript's Eq. (5) is `A_out = A_pump·g(n_bias − β·A_in)`, while `cell.py:31` uses `A_in` as the prefactor — a code-vs-paper divergence, and the two maps have different dynamics (the manuscript's converges to a period-2 orbit at ≈ −69.5 dB). Every "Eq. (5)" in this note should be read as **the released `transfer` map**. This does not weaken the conclusion; it strengthens the reason the spec must be imported, since the released map is not the manuscript's map and neither fixes the parameters. `transfer` also has **no caller anywhere in the released code**, independently confirmed by three assessors on that date.
2. **The density channel has no published row to validate against.** The shadow's *stepping* is validated bit-for-bit through the `cav_u` channel, but the new observable is validated only by construction and by the internal `drn_h` ≡ `cav_h` consistency. This gap is real and is the first thing a reproducer should attack.
3. **The m = 28 paired delta is not phase-robust** (−0.419 active-phase vs −0.108 slot-phase). No verdict rests on it; the m = 30 paired delta is robust to 0.007 dB across both perturbations and is what §3.3 uses.
4. **One drive amplitude (2×10⁻³), one duty (0.8), two seeds, two carrier phases, two grids** for the paired rows — twelve rows in all, so the m = 30 sign change is replicated at both grids under both perturbations. **No N = 720 paired row was run**: the finest-grid denomination delta is unmeasured, and given the sign change between 240 and 480 that is the single most valuable missing row.
5. **The convergence orders are three-point fits** on 2–4-decimal published floors, at two different refinement ratios, and m = 26 is demonstrably ill-conditioned. Directional, not quantitative.
6. **The knee control is N = 240 only**, m = 28 and 30, one sweep, and the 1-dB crossing is a log-amplitude interpolation between measured points.
7. **The requirement leg still inherits `A_op` = 0.0116** (08-01 §0.1/§0.2, round-tripped). Every clearance in §3.4 is exactly as `A_op`-dependent as `G_req_gated` itself.
8. **The kelvin leg crosses two models that were never coupled** and carries 07-15's open c. It is offered as a candidate source for an imported spec, not as a measurement of one.
9. **`f_max_F2_gated_GHz` is not re-adjudicated**, and this session argues it cannot be from the released chain.
10. **Everything rides on the experimentally unproven gain cell** (bench gate G1).

**What I did not run:** any N = 720 row of my own (the §4 rungs are the promoted note's, consumed); any m = 22 or m = 26 *paired* denomination row; any amplitude ladder in the density channel; any two-cell cascade; `validate.py` end-to-end (the (a) and (b) stages were run, the five duty-0.8 rows were not re-run beyond the four reproduced in §3.2); any solver-cavity bistability analysis; any bench-side quantity.

## 8. Runnable listings

Every new construction ships its computation, per `notes/README.md` ("results computed on apparatus the reader cannot run or rebuild will fail review for that reason alone"). Four files, self-contained apart from importing the released chains (adjust `CHAIN`). `fable-model-chain/` and `fable-model-quantum/` are **not edited** by any of them.

Run order and cost on this machine (6 workers): `transfer_scan.py` (~40 s — §2.3, §2.4) → `denom.py 6 240,480` (~20 min — §3.2, twelve paired rows including the phase/seed variants) → `knee_denom.py 6 28,30` (~9 min — §3.4) → `knee_stream.py 240 5 26,28,30` (~15 min — §5.3's m = 26 rung) → `decode_demand.py` (seconds — §5.2). The promoted 08-01 §8 `fs_driver.py` is imported **verbatim and unmodified** and is not duplicated here.

**Expected outputs**, so a reproducer knows immediately whether the harness is right:

- `transfer_scan.py` → `g(0) = 3.0402174031457583`; `A* = 0.5445972584384384`; `T′(A*) = −4.848420887181987`; 52,480 sets scanned, **0** with more than one transversal positive fixed point of `T`, 1,230 degenerate; **182** stable 2-cycles of `T∘T`, **0** with attracting A = 0, best extinction **−6.0413 dB**, signature-default exhibit `0.338728 ↔ 0.415651` with separatrix `0.389145`. **These are the values this listing prints on its stated lattice, and they reproduce; the "best −6.0413 dB" is not the frontier — see §10, which shows the lattice steps over the deep band and measures −11.6936 dB off it.**
- `denom.py` → the m = 30 / N = 240 reference row must print `cav_u` G_worst1 = **8.287855791924017** and floor = **−11.828336851447219** (the promoted row, to the last float digit) before anything else is trusted; then the twelve rows of §3.2.
- `knee_denom.py` → the `cav_u` gain-ratio knees must be **0.01208** (m = 28) and **0.01203** (m = 30), reproducing 08-01 §5.
- `knee_stream.py` → m = 28 and m = 30 must reproduce 08-01 §5's knees; the new m = 26 rung is **0.01260** / **0.01230**.
- `decode_demand.py` → at r = 0 the replica must equal released `qmac.error_2bit`/`error_1bit` **exactly** at 353/300/77/20 K and return `T_2bit_below_1e-3` = **58.52734375**, `T_1bit_below_1e-3` = **243.765625**.

*(The complete sources follow verbatim below: `transfer_scan.py`, `denom.py`, `denom480.py`, `knee_denom.py`, `knee_stream.py`, `decode_demand.py`.)*

## 9. What the adversarial verification changed — the auditable diff

Three blind lenses ran before publication with instructions to refute. Verdicts **1 × REFUTED, 2 × FIX-FIRST**. Every must-fix is applied above; this is the itemised list so the diff can be checked against the vote record.

**Refutation (composition lens) — accepted, headline withdrawn.**

1. The first draft asserted that **no** parameter choice makes the released `cell.transfer` restoring, inferring it from the at-most-two-fixed-points identity. The inference was **invalid for an inverting cell**, whose logic levels are the period-2 orbit — fixed points of `T∘T`, to which the identity does not transfer. The lens produced a counterexample at `cell.transfer`'s own signature defaults with `loss` = 1.6. **Verified independently here before acceptance** (§2.4), and the claim, the key `transfer_map_restoring_pair_exists` = false, and §2.4's original points 1 and 2 are all **withdrawn**. The replacement is stronger and uses released code: the triples exist, but 0 of 182 have a stable empty slot and none reaches −10 dB extinction. **[Annotated 2026-08-05: the second half of that replacement was itself falsified after the vote — the lattice's "none reaches −10 dB" is an aliasing artifact and the released map reaches −11.69 dB off-lattice (§10). The empty-slot half survives and is now proved as an identity rather than counted. This paragraph is the pre-publication record and is left as written.]**

1b. The same refutation forced **§2.5 items 1 and 2** to be rewritten: the first draft called the docstring's "restoring rail" false and its margin claim disconnected. Corrected — the rail is real in `T∘T` but is not a *logic* rail (no stable empty slot, −6.04 dB best extinction), and a margin **is** derivable from the transfer, at 0.35–0.65 of swing against the heuristic's 0.2564 — the two routes disagree by 6–10 dB, which is a stronger finding than the one withdrawn.

**Must-fixes (all three lenses).**

2. `T′(A*)` was a central finite difference (h = 10⁻⁷) presented as a closed form and wrong from the 9th significant figure. Corrected to the closed form `1 + A*·g′(A*)` = **−4.848420887181987** (was −4.848420884773219). No verdict moves — both are far below −1.
3. §4's m = 26 order fit mixed a four-decimal N = 240 rung with two-decimal 480/720 rungs. Now given **both ways** (p = 0.136 / 0.147) with a footnote, and the ill-conditioning quantified with the lens's own ±0.005 dB perturbation test.
4. The m = 22 fitted order appeared as 0.889 / 0.888 / 0.89 in three places; 0.8875 rounds to **0.888** and that is now used consistently.
5. §5.1's "docstring reading" row contradicted its own parenthetical at m = 28 and silently omitted m = 26 / N = 240. Both cells corrected to ✓.
6. §3.4 claimed three-decimal reproduction of the promoted clearances; m = 28 is +1.126 against the promoted +1.127 (a rounded-requirement artifact). Now stated exactly.
7. §3.4's stated mechanism ("compression is nearly denomination-independent") was **contradicted by its own table** — the knee moves 3–5 % between channels. Replaced with the true reason (logarithmic stiffness of `G_req` near ratio ≈ 0.48), together with the concession that this makes the requirement leg's blindness *weak* evidence.
8. The sign change of the paired denomination delta rested on **one unreplicated N = 480 run**. Four N = 480 variant rows (second carrier phase, second seed, both slots) were **run before publication**; the sign change survives (−0.445 / −0.374 / −0.444). §3.2 and §3.3 are rebuilt on twelve rows.
9. The m = 30 / N = 240 strict verdict flips under the **carrier phase alone**, in the released channel, before any denomination change. The attribution in executive item 5 and §3.3 is corrected: the boundary is unstable under all three conventions varied, and denomination is the third.
10. §5.2(a)'s spec-crossing temperatures were tagged *Demonstrated* at the point of assertion and *in-model* only afterwards. Retagged **in-model** where asserted.
11. No runnable listings shipped. **§8 added**, with expected outputs, and the three "Demonstrated (runnable)" labels changed to the mandated "demonstrated (runnable, see listing)".
12. `truth_table` was listed among the functions `run_all.py` consumes; it is not called outside `cell.py` either. Corrected — this strengthens the finding.
13. `classical_BER` named as a `results.json` key; the actual keys are `classical_BER_300K` / `classical_BER_353K`. Corrected.
14. §1 quoted an F = 2 base of 6.515399158503943 while the promoted `knee_interp.py` listing used to produce §3.4's requirements hard-codes 6.515377553550175. The 2.2×10⁻⁵ dB gap is now **disclosed** rather than left as two bases in one document.
15. §2.3's artifact taxonomy claimed two families; there is a **mirror branch** (`loss` = −1) the released grid's non-negative `loss` never reaches. Added.
16. §3.1's "no verdict rests on it" disclaimer on the argmax diagnostic was over-broad — executive item 4's plane attribution and §6's top WP1 recommendation both inherit it. Reworded to say so.

17. **Caught while writing §8, not by a lens, and recorded because it is the same class of defect:** the 2-cycle census was first quoted as **356** from an exploratory run on a 31-point `loss` grid, while the text described it as "the same 52,480-set grid" (16-point `loss`). The shipped `transfer_scan.py` is authoritative and returns **182** on the stated grid; median −1.857, worst −0.0439. The invariants that carry the verdict are unchanged on either grid — **0** with an attracting empty slot, **0** reaching −10 dB, best **−6.0413 dB** — but the count and two statistics are corrected to what the listing prints. **[Annotated 2026-08-05: "0 reaching −10 dB" and "best −6.0413 dB" were grid-invariant across both lattices and still wrong, because both lattices share the same 0.1 `n_bias` step that straddles the deep band — grid-invariance across two co-aliased grids is not robustness. See §10.]**

**What the lenses could not break.** The reproduction lens rebuilt the harness from this memo's stated conventions alone, never opening the session's driver files, and reproduced the m = 30 paired rows, the plane diagnostic and the sign change to the last float digit; its own 529,644-set scan (ten times this session's) found the same three artifact families and no fourth. The record lens verified every promoted citation, every closed-form number, the entire decode-demand table and the bracket ceiling against independently written code, and confirmed the reply contests no `results.json` value, reopens no promoted key, registers no colliding key, and reintroduces nothing the record retired.

### §8 sources, verbatim

The exact files that produced every new number in the reply. Self-contained apart from importing the released chains (adjust `CHAIN` / `QCHAIN`). The promoted 08-01 §8 `fs_driver.py` is imported **verbatim and unmodified** by `denom.py` and `knee_stream.py` and is not duplicated here. Neither released chain is edited by any of them.

Run order and cost on this machine (6 workers): `transfer_scan.py` (~3 min) → `denom.py 6 240,480` (~20 min) → `denom480.py` (~6 min, the phase/seed variants at N = 480) → `knee_denom.py 6 28,30` (~9 min) → `knee_stream.py 240 5 26,28,30` (~15 min) → `decode_demand.py` (seconds). Expected outputs are stated in the reply's §8.

### `transfer_scan.py` — Half 1 — fixed-point structure of the released map and of T∘T

```python
# -*- coding: utf-8 -*-
"""Half 1: fixed-point structure of the released Eq. (5) map and of its two-cell
composition. Imports the released cell.py; edits nothing.

Prints, in order:
  g(0), A*, T'(A*) (closed form 1 + A*g'(A*))
  the 52,480-set census of transversal positive fixed points of T
  the 356 stable 2-cycles of T o T, their extinction statistics, and the
  signature-default exhibit
"""
import sys, math
import numpy as np
CHAIN = "/Users/rxiii/Documents/GitHub/FableComputer/fable-model-chain"
sys.path.insert(0, CHAIN)
import cell as CELL

NT, DN, GM = CELL.N_TH, CELL.DN, CELL.G_amp
def g(A, nb=1.0, be=1.0, gm=GM, lo=0.0):
    return gm*0.5*(1+np.tanh((nb-be*A-NT)/DN)) - lo
def gp(A, nb=1.0, be=1.0, gm=GM, lo=0.0):
    return -be*gm/(2*DN)/np.cosh((nb-be*A-NT)/DN)**2
def T(A, **kw):  return A*g(A, **kw)
def T2(A, **kw): return T(T(A, **kw), **kw)

print("== released parameters ==")
print("g(0) = T'(0) =", repr(float(g(0.0))))
y = 2.0/GM - 1.0                       # solve g(A)=1 analytically
Astar = (1.0 - NT - math.atanh(y)*DN)
print("A* (analytic root of g(A)=1) =", repr(Astar))
print("T'(A*) = 1 + A*g'(A*)        =", repr(float(1 + Astar*gp(Astar))))

def roots(F, kw, top, n=20001):
    As = np.geomspace(1e-6, top, n); f = F(As, **kw) - As
    nz = f[f != 0.0]
    idx = np.where(np.diff(np.sign(f)) != 0)[0]
    out = []
    for i in idx:
        a, b = As[i], As[i+1]
        for _ in range(160):
            m = 0.5*(a+b)
            if (F(a, **kw)-a)*(F(m, **kw)-m) <= 0: b = m
            else: a = m
        out.append(0.5*(a+b))
    return out

GRID = [(nb, be, lo, gm)
        for nb in np.linspace(-1.0, 3.0, 41)
        for be in (-4,-2,-1,-0.5,-0.25,0.25,0.5,1,2,4)
        for lo in np.linspace(0.0, 3.0, 16)
        for gm in (0.5,1.0,1.5,2.0,GM,4.0,6.0,10.0)]

print("\n== census of T (transversal positive fixed points) ==")
tot=multi=s0=degen=0
As=np.geomspace(1e-6,500.0,20001)
for nb,be,lo,gm in GRID:
    tot+=1; kw=dict(nb=nb,be=be,gm=gm,lo=lo)
    if abs(g(0.0,**kw))<1.0: s0+=1
    if abs((gm-lo)-1.0)<1e-12 or abs(lo+1.0)<1e-12: degen+=1; continue
    f=g(As,**kw)-1.0; nz=f[f!=0.0]
    if int((np.diff(np.sign(nz))!=0).sum())>1: multi+=1
print(f"  scanned {tot}; attracting '0' {s0}; degenerate plateaus {degen}; "
      f"MORE THAN ONE positive root: {multi}")

print("\n== census of T o T (stable 2-cycles) ==")
ext=[]; zatt=0; best=None
for nb,be,lo,gm in [(nb,be,lo,gm) for nb,be,lo,gm in GRID if abs((gm-lo)-1.0)>1e-12]:
    kw=dict(nb=nb,be=be,gm=gm,lo=lo)
    rr=roots(T2,kw,6.0,20001)
    if len(rr)<2: continue
    h=1e-8
    att=[r for r in rr if abs((T2(r+h,**kw)-T2(r-h,**kw))/(2*h))<1]
    if len(att)<2: continue
    e=20*math.log10(min(att)/max(att)); ext.append(e)
    if g(0.0,**kw)**2 < 1.0: zatt+=1
    if best is None or e<best[0]: best=(e,nb,be,lo,gm,min(att),max(att))
ext=np.array(ext)
print(f"  stable 2-cycles: {len(ext)}")
print(f"  with ATTRACTING A=0 ((ToT)'(0)=g(0)^2<1): {zatt}")
print(f"  extinction: best {ext.min():+.4f} dB, median {np.median(ext):+.4f}, worst {ext.max():+.4f}")
print(f"  reaching -10 dB: {(ext<=-10).sum()}")
print(f"  best at n_bias={best[1]:.2f}, beta={best[2]}, loss={best[3]:.2f}, g_max={best[4]:.4f} "
      f"(levels {best[5]:.5f} <-> {best[6]:.5f})")

print("\n== signature-default exhibit: n_bias=1, beta=1, g_max=G_amp, loss=1.6 ==")
kw=dict(nb=1.0,be=1.0,gm=GM,lo=1.6)
for A in (0.338728,0.389145,0.415651):
    h=1e-9; d=(T2(A+h,**kw)-T2(A-h,**kw))/(2*h)
    print(f"  A={A:.6f}  T(A)={T(A,**kw):.6f}  T2(A)-A={T2(A,**kw)-A:+.2e}  "
          f"(T2)'={d:+.6f}  {'ATTRACTING' if abs(d)<1 else 'repelling'}")
print(f"  g(0)^2 = {float(g(0.0,**kw))**2:.6f} -> A=0 repelling")
print(f"  extinction = {20*math.log10(0.338728/0.415651):+.4f} dB")

print("\n== the clock-pumped reconstruction (NOT released code) ==")
def T2c(A,Ac): return Ac*g(Ac*g(A))
band=[]
for Ac in np.arange(0.10,1.00,0.01):
    top=Ac*float(g(0.0))*1.02
    As=np.linspace(1e-13,top,400001); f=T2c(As,Ac)-As
    idx=np.where(np.diff(np.sign(f))!=0)[0]; rr=[]
    for i in idx:
        a,b=As[i],As[i+1]
        for _ in range(160):
            m=0.5*(a+b)
            if (T2c(a,Ac)-a)*(T2c(m,Ac)-m)<=0: b=m
            else: a=m
        rr.append(0.5*(a+b))
    h=1e-11
    att=[r for r in rr if abs((T2c(r+h,Ac)-T2c(r-h,Ac))/(2*h))<1]
    sep=[r for r in rr if r not in att]
    if len(att)>=2 and sep:
        band.append((Ac,20*math.log10(sep[0]/max(att))))
if band:
    print(f"  bistable A_c in [{band[0][0]:.2f}, {band[-1][0]:.2f}]; residual "
          f"[{min(b[1] for b in band):+.2f}, {max(b[1] for b in band):+.2f}] dB")

print("\n== the noise-margin heuristic ==")
for k,e in ((8,10.0),(5,10.0),(16,10.0)):
    v=CELL.static_noise_margin(k=k,extinction_dB=e)
    print(f"  static_noise_margin(k={k:2d}, {e} dB) = {v!r} -> {20*math.log10(v):+.6f} dB")
doc=0.5*(1-1/8.0)*(1-10**(-0.5))
print(f"  docstring form at k=8, 10 dB = {doc!r} -> {20*math.log10(doc):+.6f} dB")
print(f"  docstring-vs-code gap = {20*math.log10(doc)-20*math.log10(CELL.static_noise_margin()):+.4f} dB")
print(f"  r* = 3/11 = {3/11!r} -> {20*math.log10(3/11):+.12f} dB")

```

### `denom.py` — Half 2 — the density-recording shadow and the twelve paired rows

```python
# -*- coding: utf-8 -*-
"""HALF 2 of the 2026-08-02 winning prompt: is the measured '0'-floor denominated
in the ratio the floor SPEC is stated in?

The promoted floor `max0_below_mean1_dB` is a ratio of per-slot peaks of the
released `cav` = max_x |hu/h - u0| — a VELOCITY perturbation of the electron
fluid, maximised over space (intracavity plane). The `extinction_dB` fed to
`cell.static_noise_margin`, and the swing `cell.A_SAT` = 0.02 denominates, are
DENSITY quantities. This module measures the same floor in four channels of one
identical run, so every delta is a PAIRED quantity (07-31 §2's ~1 dB carrier-
phase sensitivity is common-mode inside a pair):

  cav_u  : max_x |hu/h - u0|      velocity, intracavity   <- the RELEASED channel
  cav_h  : max_x |h - 1|          density,  intracavity   <- new
  drn_u  : |hu[-1]/h[-1] - u0|    velocity, drain plane   <- released `drain`, rectified
  drn_h  : |h[-1] - 1|            density,  drain plane   <- new

The stepping is the released `solver._step_LF` / `_setup`, imported verbatim,
exactly as the promoted `fs_driver.run_custom` does; only the recording is added.
Validated in __main__ against the promoted m = 30 / N = 240 ratio-bias row.

`fable-model-chain/` is NOT edited.
"""
import json, math, os, sys, time
import numpy as np
from multiprocessing import Pool

from fs_driver import CHAIN, default_bits, measure, slot_peaks
sys.path.insert(0, CHAIN)
import constants as C
import solver as SOL
from solver import _setup, _step_LF
import ds_cell as DS

S = DS.plasmon_speed(); TAU = C.tau(C.Tcap); L = DS.cell_length(S)
MTH = DS.M_threshold(L, S, TAU)
F0N = C.f0 * L / S
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "denom.jsonl")


def make_sig_duty(bits, repT, f0_n, amp, edge_rt=2.0, duty=0.8, phase="active"):
    """The promoted fs_driver 'duty' shape. `phase` selects the carrier reference:
      'active' — centre of the ACTIVE envelope window (the promoted 07-31 §2
                 convention: 0.5*duty*repT into the slot);
      'slot'   — the SLOT centre (the alternative reading 07-31 §2 records as
                 moving the m = 28 / N = 720 floor by ~0.8 dB).
    'active' is byte-equivalent to fs_driver.make_sig('duty', ...)."""
    span = duty * repT
    edge = edge_rt * 2.0

    def sig(t):
        slot = int(t / repT)
        b = bits[slot] if slot < len(bits) else 0
        if not b:
            return 0.0
        x = t - slot * repT
        if x >= span:
            return 0.0
        if x < edge:
            env = 0.5 * (1 - math.cos(math.pi * x / edge))
        elif x > span - edge:
            env = 0.5 * (1 - math.cos(math.pi * (span - x) / edge))
        else:
            env = 1.0
        tc = slot * repT + (0.5 * span if phase == "active" else 0.5 * repT)
        return amp * env * math.sin(2 * math.pi * f0_n * (t - tc))
    return sig


def run_shadow(M, N, n_roundtrips, sigfun, cfl=0.4, T=C.Tcap):
    """run_custom's stepping VERBATIM (released _setup/_step_LF), four recorders."""
    s, tau, L_, tau_n, f0n = _setup(N, T)
    u0 = M
    dx = 1.0 / N
    cmax = 1.0 + abs(u0) + 0.2
    dt = cfl * dx / cmax
    nsteps = int(n_roundtrips * 2.0 / dt)
    h = np.ones(N); hu = np.ones(N) * u0
    tarr = np.empty(nsteps)
    cav_u = np.empty(nsteps); cav_h = np.empty(nsteps)
    drn_u = np.empty(nsteps); drn_h = np.empty(nsteps)
    t = 0.0
    for k in range(nsteps):
        h_left = 1.0 + sigfun(t)
        h, hu = _step_LF(h, hu, dx, dt, u0, tau_n, h_left, u0)
        if not np.all(np.isfinite(h)) or np.any(h < 1e-6):
            tarr = tarr[:k]; cav_u = cav_u[:k]; cav_h = cav_h[:k]
            drn_u = drn_u[:k]; drn_h = drn_h[:k]
            break
        cav_u[k] = np.max(np.abs(hu / h - u0))     # RELEASED solver.py:99
        cav_h[k] = np.max(np.abs(h - 1.0))         # density analogue, same plane
        drn_u[k] = abs(hu[-1] / h[-1] - u0)        # RELEASED solver.py:98, rectified
        drn_h[k] = abs(h[-1] - 1.0)                # density at the drain
        tarr[k] = t
        t += dt
    return dict(t=tarr, cav_u=cav_u, cav_h=cav_h, drn_u=drn_u, drn_h=drn_h, dt=dt)


def peaks(t, y, repT, nslots, w_lo=0.25, w_hi=0.72):
    """fs_driver.slot_peaks convention, applied to an arbitrary channel."""
    out = []
    for k in range(nslots):
        m = (t >= (k + w_lo) * repT) & (t < (k + w_hi) * repT)
        out.append(np.max(y[m]) if m.sum() > 3 else np.nan)
    return np.array(out)


def score(bits, pM, p0, drop=4):
    """fs_driver.measure convention, one channel."""
    n = len(pM)
    b = np.asarray(bits[drop:n]); a = pM[drop:n]; z = p0[drop:n]
    ones = b == 1; zeros = b == 0
    r = {}
    gg = 20 * np.log10(a[ones] / z[ones])
    r["G_worst1_dB"] = float(np.min(gg))
    r["pp_raw_dB"] = float(20 * np.log10(np.max(a[ones]) / np.min(a[ones])))
    r["eye_dB"] = float(20 * np.log10(np.min(a[ones]) / np.max(a[zeros])))
    r["max0_below_mean1_dB"] = float(20 * np.log10(np.max(a[zeros]) / np.mean(a[ones])))
    return r


def mth_num_at(N):
    """The released run_all.measure_Mth_num bracket scan, at grid N (recomputed)."""
    xs = np.linspace(1.05, 1.30, 8)
    g = [SOL.growth_rate(x * MTH, N=N, n_roundtrips=90) for x in xs]
    for i in range(len(xs) - 1):
        if g[i] < 0 <= g[i + 1]:
            xz = xs[i] + (xs[i + 1] - xs[i]) * (-g[i]) / (g[i + 1] - g[i])
            return xz * MTH
    return float("nan")


def row(cfg):
    t0 = time.time()
    m, N, amp = cfg["m"], cfg["N"], cfg["amp"]
    repT = 2.0 * m
    nslots = 40
    bits = default_bits(nslots, cfg.get("seed", 7))
    sig = make_sig_duty(bits, repT, F0N, amp, edge_rt=2.0, duty=cfg["duty"],
                        phase=cfg.get("phase", "active"))
    nrt = nslots * m
    rM = run_shadow(cfg["bias"], N, nrt, sig)
    r0 = run_shadow(0.0, N, nrt, sig)
    res = dict(cfg)
    for ch in ("cav_u", "cav_h", "drn_u", "drn_h"):
        pM = peaks(rM["t"], rM[ch], repT, nslots)
        p0 = peaks(r0["t"], r0[ch], repT, nslots)
        for k, v in score(bits, pM, p0).items():
            res[f"{ch}__{k}"] = v
    res["secs"] = round(time.time() - t0, 1)
    return res


def dispatch(cfg):
    try:
        return row(cfg)
    except Exception as e:
        out = dict(cfg); out["error"] = repr(e)
        return out


if __name__ == "__main__":
    nproc = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    NS = [int(x) for x in (sys.argv[2] if len(sys.argv) > 2 else "240,480").split(",")]

    mthn = {}
    for N in NS:
        t0 = time.time()
        mthn[N] = mth_num_at(N)
        print(f"M_th_num({N}) = {mthn[N]!r}  0.7* = {0.7*mthn[N]!r}  [{time.time()-t0:.0f}s]",
              flush=True)
    json.dump({str(k): v for k, v in mthn.items()},
              open(os.path.join(HERE, "denom_mth.json"), "w"))

    jobs = []
    for N in NS:
        for m in (28, 30):
            jobs.append({"m": m, "N": N, "duty": 0.8, "amp": 2e-3,
                         "bias": 0.7 * mthn[N], "bias_mode": "ratio",
                         "seed": 7, "phase": "active", "tag": "main"})
    # robustness on the decisive row: second carrier phase, second seed
    if 240 in mthn:
        for m in (28, 30):
            jobs.append({"m": m, "N": 240, "duty": 0.8, "amp": 2e-3,
                         "bias": 0.7 * mthn[240], "bias_mode": "ratio",
                         "seed": 7, "phase": "slot", "tag": "phase"})
            jobs.append({"m": m, "N": 240, "duty": 0.8, "amp": 2e-3,
                         "bias": 0.7 * mthn[240], "bias_mode": "ratio",
                         "seed": 11, "phase": "active", "tag": "seed"})
    print(f"{len(jobs)} jobs, {nproc} workers", flush=True)
    mode = "a" if os.path.exists(OUT) else "w"
    with open(OUT, mode) as f:
        with Pool(nproc) as pool:
            for res in pool.imap_unordered(dispatch, jobs):
                f.write(json.dumps(res) + "\n"); f.flush()
                print({k: (round(v, 4) if isinstance(v, float) else v)
                       for k, v in res.items()
                       if k in ("m", "N", "seed", "phase", "tag", "secs",
                                "cav_u__G_worst1_dB", "cav_u__max0_below_mean1_dB",
                                "cav_h__max0_below_mean1_dB",
                                "drn_u__max0_below_mean1_dB",
                                "drn_h__max0_below_mean1_dB")}, flush=True)
    print("DONE", flush=True)

```

### `knee_denom.py` — §3.4 — the knee in both denominations (the clearance control)

```python
# -*- coding: utf-8 -*-
"""The CONTROL Half 2 needs: does the REQUIREMENT leg move under denomination too?

Half 2's paired rows show the gain leg moves (+0.38 dB at m = 30 / N = 240 between
the velocity and density channels). A clearance is gain minus requirement, and the
requirement `G_req_gated` is built from a knee measured with the released per-slot-
mean estimator on `cav` — the SAME velocity channel. So the honest question is not
"how much does the gain move" but "how much does the CLEARANCE move".

This runs the promoted 08-01 §5 streaming knee sweep (all-ones train, duty-0.8,
released per-slot-mean estimator, ratio bias, log-amplitude 1-dB interpolation)
in BOTH channels of one identical run, so the knee delta is paired too.

Validation: the velocity-channel knee must reproduce the knees this session
already measured with the promoted `knee_stream.py` (m = 30 / N = 240:
0.01228 active-only / 0.01203 gain-ratio, themselves reproducing 08-01 §5).

`fable-model-chain/` is NOT edited.
"""
import json, math, os, sys, time
import numpy as np
from multiprocessing import Pool

from fs_driver import CHAIN
from denom import make_sig_duty, run_shadow, F0N

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "knee_denom.jsonl")
AMPS = [5e-4, 1e-3, 2e-3, 4e-3, 7e-3, 9e-3, 1.1e-2, 1.3e-2, 1.5e-2,
        1.7e-2, 2.26e-2, 3.2e-2, 4.5e-2]
C_1DB = math.sqrt(10 ** 0.1 - 1)


def slot_est(t, y, repT):
    """run_all.measure_pulse_gain's estimator, verbatim logic, any channel."""
    pk = [np.max(y[(t >= k * repT) & (t < (k + 1) * repT)])
          for k in range(1, int(t[-1] / repT))
          if ((t >= k * repT) & (t < (k + 1) * repT)).sum() > 5]
    pk = np.array(pk)
    return float(pk[len(pk) // 2:].mean())


def row(cfg):
    t0 = time.time()
    m, N, amp = cfg["m"], cfg["N"], cfg["amp"]
    repT = 2.0 * m
    nslots = 24
    bits = np.ones(nslots, dtype=int)
    sig = make_sig_duty(bits, repT, F0N, amp, edge_rt=2.0, duty=0.8, phase="active")
    nrt = nslots * m
    rM = run_shadow(cfg["bias"], N, nrt, sig)
    r0 = run_shadow(1e-9, N, nrt, sig)
    res = dict(cfg)
    for ch in ("cav_u", "cav_h"):
        a = slot_est(rM["t"], rM[ch], repT)
        p = slot_est(r0["t"], r0[ch], repT)
        res[f"{ch}__act"] = a
        res[f"{ch}__pas"] = p
        res[f"{ch}__G_dB"] = 20 * math.log10(a / p)
    res["secs"] = round(time.time() - t0, 1)
    return res


def dispatch(cfg):
    try:
        return row(cfg)
    except Exception as e:
        out = dict(cfg); out["error"] = repr(e)
        return out


def interp_knee(pts):
    """08-01 §8 knee_interp.interp_knee, verbatim."""
    for i in range(len(pts) - 1):
        c1, c2 = -pts[i][1], -pts[i + 1][1]
        if c1 < 1.0 <= c2:
            a1, a2 = pts[i][0], pts[i + 1][0]
            return math.exp(math.log(a1) + (math.log(a2) - math.log(a1))
                            * (1 - c1) / (c2 - c1))
    return None


def analyse(path):
    rows = [json.loads(l) for l in open(path) if l.strip()]
    rows = [r for r in rows if "error" not in r]
    import collections
    groups = collections.defaultdict(list)
    for r in rows:
        groups[(r["N"], r["m"])].append(r)
    LOSSBASE = 6.515377553550175
    print(f"\n{'m':>3} {'N':>4} {'channel':>8} {'obs':>12} {'knee':>9} {'A_SAT':>9} "
          f"{'G_req(F2)':>10}")
    print("-" * 62)
    out = {}
    for key in sorted(groups):
        N, m = key
        rs = sorted(groups[key], key=lambda r: r["amp"])
        amps = [r["amp"] for r in rs]
        for ch in ("cav_u", "cav_h"):
            resp = [20 * math.log10(r[f"{ch}__act"] / r["amp"]) for r in rs]
            act = list(zip(amps, [x - np.mean(resp[:2]) for x in resp]))
            g = [r[f"{ch}__G_dB"] for r in rs]
            rat = list(zip(amps, [x - np.mean(g[:2]) for x in g]))
            for lbl, ser in (("active-only", act), ("gain-ratio", rat)):
                k = interp_knee(ser)
                if k is None:
                    print(f"{m:3d} {N:4d} {ch:>8} {lbl:>12} {'no crossing':>9}"); continue
                A_SAT = k / C_1DB
                G_req = 10 * math.log10(1 + (0.0116 / A_SAT) ** 2 / 2) + LOSSBASE
                print(f"{m:3d} {N:4d} {ch:>8} {lbl:>12} {k:9.5f} {A_SAT:9.5f} {G_req:10.4f}")
                out[(m, N, ch, lbl)] = (k, A_SAT, G_req)
    return out


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "analyse":
        analyse(OUT); sys.exit()
    nproc = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    SLOTS = [int(x) for x in (sys.argv[2] if len(sys.argv) > 2 else "28,30").split(",")]
    N = 240
    mthn = 0.16894319463373791          # recomputed this session, = results.json
    jobs = [{"m": m, "N": N, "amp": a, "bias": 0.7 * mthn, "bias_mode": "ratio"}
            for m in SLOTS for a in AMPS]
    print(f"{len(jobs)} jobs, {nproc} workers", flush=True)
    mode = "a" if os.path.exists(OUT) else "w"
    with open(OUT, mode) as f:
        with Pool(nproc) as pool:
            for res in pool.imap_unordered(dispatch, jobs):
                f.write(json.dumps(res) + "\n"); f.flush()
                print({k: (round(v, 5) if isinstance(v, float) else v)
                       for k, v in res.items()
                       if k in ("m", "amp", "cav_u__G_dB", "cav_h__G_dB", "secs")},
                      flush=True)
    analyse(OUT)
    print("DONE", flush=True)

```

### `knee_stream.py` — §5.3 — the gated streaming knee, m = 26 rung added

```python
# -*- coding: utf-8 -*-
"""The gated streaming knee sweep — the promoted 08-01 §8 `knee_stream.py`
listing, extended ONLY by the slot list (m = 26 added) and the CLI.

The 08-01 §5 table measured m = 28 and 30. `notes/2026-08-01-ratio-bias-gain-table.md`
§0.5 names the m = 26 knee as one of the two things missing before
`f_max_F2_gated_GHz` can be re-adjudicated in the ratio convention. m = 28/30 are
re-run here as anchors: they must reproduce 08-01 §5's ratio-leg knees
(m=28: 0.01235 active-only / 0.01208 gain-ratio; m=30: 0.01228 / 0.01203 at N=240).

Conventions, stated (08-01 §8, unchanged):
  - bias = 0.7 * M_th_num measured at the row's own grid ('ratio' leg)
  - estimator = the released run_all.measure_pulse_gain per-slot estimator
  - all-ones train (the streaming analogue of the released 'pulse' drive)
  - duty-0.8 gated shape, raised-cosine edges of 2 rt (07-31 §2)
  - compression referred to the ACTIVE-cell-only linear limit and to the gain
    ratio, both reported; 1-dB knee by log-amplitude interpolation.
"""
import json, math, os, sys, time
import numpy as np
from multiprocessing import Pool

from fs_driver import make_sig, run_custom, CHAIN
from streaming import released_slot_estimator, MTH, F0N
sys.path.insert(0, CHAIN)
import solver as SOL

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "knee_stream.jsonl")

AMPS = [5e-4, 1e-3, 2e-3, 4e-3, 7e-3, 9e-3, 1.1e-2, 1.3e-2, 1.5e-2,
        1.7e-2, 2.26e-2, 3.2e-2, 4.5e-2]

MTHNUM_CACHE = {}


def mth_num_at(N):
    """run_all.measure_Mth_num's scan, at grid N (released bracket)."""
    if N in MTHNUM_CACHE:
        return MTHNUM_CACHE[N]
    xs = np.linspace(1.05, 1.30, 8)
    g = [SOL.growth_rate(x * MTH, N=N, n_roundtrips=90) for x in xs]
    val = float("nan")
    for i in range(len(xs) - 1):
        if g[i] < 0 <= g[i + 1]:
            xz = xs[i] + (xs[i + 1] - xs[i]) * (-g[i]) / (g[i + 1] - g[i])
            val = xz * MTH
            break
    MTHNUM_CACHE[N] = val
    return val


def row(cfg):
    t0 = time.time()
    m, N, amp = cfg["m"], cfg["N"], cfg["amp"]
    repT = 2.0 * m
    nslots = cfg.get("nslots", 24)
    bits = np.ones(nslots, dtype=int)
    sig = make_sig(cfg["shape"], bits, repT, F0N, amp,
                   ncyc=cfg.get("ncyc", 3), edge_rt=cfg.get("edge_rt", 2.0),
                   duty=cfg.get("duty", 1.0))
    nrt = nslots * m
    rM = run_custom(cfg["bias"], N, nrt, sig)
    r0 = run_custom(1e-9, N, nrt, sig)
    res = dict(cfg)
    res["pk_act"] = float(released_slot_estimator(rM, repT))
    res["pk_pas"] = float(released_slot_estimator(r0, repT))
    res["G_dB"] = 20 * math.log10(res["pk_act"] / res["pk_pas"])
    res["secs"] = round(time.time() - t0, 1)
    return res


def dispatch(cfg):
    try:
        return row(cfg)
    except Exception as e:
        out = dict(cfg); out["error"] = repr(e)
        return out


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 240
    nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    SLOTS = [int(x) for x in (sys.argv[3] if len(sys.argv) > 3 else "26,28,30").split(",")]
    print(f"grid N={N}, slots {SLOTS}", flush=True)
    t0 = time.time()
    mthn = mth_num_at(N)
    print(f"M_th_num(N={N}) = {mthn!r}   0.7*M_th_num = {0.7*mthn!r}   [{time.time()-t0:.0f}s]",
          flush=True)

    jobs = []
    for m in SLOTS:
        for amp in AMPS:
            jobs.append({"kind": "knee", "shape": "duty", "duty": 0.8,
                         "edge_rt": 2.0, "m": m, "N": N, "amp": amp,
                         "bias": 0.7 * mthn, "bias_mode": "ratio",
                         "mth_num": mthn, "exp": "K"})
    print(f"{len(jobs)} jobs, {nproc} workers", flush=True)
    mode = "a" if os.path.exists(OUT) else "w"
    with open(OUT, mode) as f:
        with Pool(nproc) as pool:
            for res in pool.imap_unordered(dispatch, jobs):
                f.write(json.dumps(res) + "\n"); f.flush()
                print({k: (round(v, 5) if isinstance(v, float) else v)
                       for k, v in res.items() if k not in ("bias", "mth_num")},
                      flush=True)
    print("DONE", flush=True)

```

### `decode_demand.py` — §5.2 — Part II's own floor demand

```python
# -*- coding: utf-8 -*-
"""Part II's own '0'-floor demand: the largest coherent residual the 2-bit decode
tolerates at 1e-3, and where that crosses each candidate floor spec.

Replica of the RELEASED qmac.levels_at_decision with ONE change: the '0' arm
carries a coherent residual of relative amplitude r (r = 0 -> released).
Validated at r = 0 against released error_2bit / error_1bit and against the
published T_2bit_below_1e-3 / T_1bit_below_1e-3 using the identical bisection
(qerrors.threshold_temperature stops at hi-lo > 0.5, so the published keys carry
0.5 K granularity -- reproduced here, not chased).

fable-model-quantum/ is NOT edited.
"""
import sys, math, json, os
QCHAIN = "/Users/rxiii/Documents/GitHub/FableComputer/fable-model-quantum"
sys.path.insert(0, QCHAIN)
os.chdir(QCHAIN)
import qconstants as C, qnoise as Q, qdecode, qmac, qerrors
RES = json.load(open("results.json", encoding="utf-8"))


def levels_floored(T, r, N_op=400, w=0.5):
    out = {}
    for A in (0, 1):
        for B in (0, 1):
            aA = 1.0 if A else r
            aB = 1.0 if B else r
            sA = Q.loss_dB(Q.GState(N=(aA ** 2) * N_op), qmac.input_transit_dB(T), T)
            sB = Q.loss_dB(Q.GState(N=(aB ** 2) * N_op), qmac.input_transit_dB(T), T)
            st = Q.combine(sA, sB, w)
            st = Q.loss_dB(st, qmac.fanout_dB(T), T)
            out[(A, B)] = st
    return out, max(s.x for s in out.values())


def err2(T, r):
    st, xr = levels_floored(T, r); V = qmac.decision_variance(st, xr, T)
    L0 = st[(0, 0)].x; L1 = 0.5 * (st[(0, 1)].x + st[(1, 0)].x); L2 = st[(1, 1)].x
    return Q.symbol_error([L0, L1, L2], [0.25, 0.5, 0.25], V)


def err1(T, r):
    st, xr = levels_floored(T, r); V = qmac.decision_variance(st, xr, T)
    return Q.symbol_error([st[(0, 0)].x, st[(1, 1)].x], [0.5, 0.5], V)


def thresh(target, r, mode="2bit"):
    f = err2 if mode == "2bit" else err1
    lo, hi = 4.0, 400.0
    if f(lo, r) > target: return None
    while hi - lo > 0.5:                      # the released bisection, verbatim
        mid = 0.5 * (lo + hi)
        if f(mid, r) <= target: lo = mid
        else: hi = mid
    return lo


def demand_dB(T, target=1e-3):
    if err2(T, 0.0) > target: return None
    lo, hi = 0.0, 0.999
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if err2(T, mid) <= target: lo = mid
        else: hi = mid
    return 20 * math.log10(0.5 * (lo + hi))


if __name__ == "__main__":
    print("== replica validation at r = 0 (must be EXACT) ==")
    ok = True
    for T in (353.0, 300.0, 77.0, 20.0):
        a, b = err2(T, 0.0), qmac.error_2bit(T)
        c, d = err1(T, 0.0), qmac.error_1bit(T)
        ok = ok and a == b and c == d
        print(f"  T={T:5.0f}: 2bit {a == b}, 1bit {c == d}")
    print(f"  T_2bit_below_1e-3 = {thresh(1e-3, 0.0)} (published {RES['T_2bit_below_1e-3']})")
    print(f"  T_1bit_below_1e-3 = {thresh(1e-3, 0.0, '1bit')} (published {RES['T_1bit_below_1e-3']})")
    print(f"  ALL EXACT: {ok}")

    print("\n== the decode's own floor demand at 1e-3, N_op = 400 ==")
    print(f"  {'T (K)':>7} {'max r':>10} {'floor (dB)':>12}")
    for T in (48.0, 40.0, 30.0, 25.0, 20.0, 15.0, 10.0, 4.0):
        d = demand_dB(T)
        r = 10 ** (d / 20)
        print(f"  {T:7.0f} {r:10.6f} {d:12.2f}")

    print("\n== where the demand crosses each candidate spec ==")
    for lbl, spec in (("round -10.0", -10.0), ("r* = 3/11", -11.285428608771253),
                      ("strict", -11.821145417981018), ("k=5 reading", -13.759345678142145)):
        lo, hi = 4.0, 58.0
        flo = demand_dB(lo); fhi = demand_dB(hi)
        if flo is None or fhi is None or not (min(flo, fhi) <= spec <= max(flo, fhi)):
            print(f"  {lbl:14s}: no crossing in 4-58 K"); continue
        for _ in range(120):
            mid = 0.5 * (lo + hi); fm = demand_dB(mid)
            if (flo - spec) * (fm - spec) <= 0: hi, fhi = mid, fm
            else: lo, flo = mid, fm
        print(f"  {lbl:14s} ({spec:+.4f} dB): demanded at T = {0.5*(lo+hi):.2f} K")
    print(f"\n  T->0 saturation: {demand_dB(4.0):+.3f} dB at 4 K "
          f"(threshold_band_variance, k_dec=16, c open per 07-15, does not cool away)")

```

### `denom480.py` — the N = 480 phase/seed rows the adversarial lens required

```python
# -*- coding: utf-8 -*-
"""The N = 480 phase/seed robustness rows the adversarial composition lens
required: the sign change of the paired denomination delta between N = 240 and
N = 480 was resting on ONE unreplicated run at N = 480."""
import json, os, time
from multiprocessing import Pool
from denom import dispatch, mth_num_at, OUT

if __name__ == "__main__":
    t0 = time.time()
    mthn = mth_num_at(480)
    print(f"M_th_num(480) = {mthn!r}  0.7* = {0.7*mthn!r}  [{time.time()-t0:.0f}s]", flush=True)
    jobs = []
    for m in (28, 30):
        jobs.append({"m": m, "N": 480, "duty": 0.8, "amp": 2e-3, "bias": 0.7*mthn,
                     "bias_mode": "ratio", "seed": 7, "phase": "slot", "tag": "phase480"})
        jobs.append({"m": m, "N": 480, "duty": 0.8, "amp": 2e-3, "bias": 0.7*mthn,
                     "bias_mode": "ratio", "seed": 11, "phase": "active", "tag": "seed480"})
    print(f"{len(jobs)} jobs", flush=True)
    with open(OUT, "a") as f:
        with Pool(4) as pool:
            for res in pool.imap_unordered(dispatch, jobs):
                f.write(json.dumps(res) + "\n"); f.flush()
                print({k: (round(v,4) if isinstance(v,float) else v) for k,v in res.items()
                       if k in ("m","N","seed","phase","tag","secs",
                                "cav_u__max0_below_mean1_dB","cav_h__max0_below_mean1_dB")},
                      flush=True)
    print("DONE", flush=True)

```

---

## 10. Revision record — 2026-08-05: the falsified key, re-measured

**Why this section exists.** The first promotion attempt ([PR #96](https://github.com/ryoji-info/FableComputer/pull/96)) passed the crew vote **2-of-3** and was then **closed at the maintainer's direction and returned for rework**, because the recorded dissent met the stated falsifier of this note's own registered key. This section is the rework. It was executed on **`claude-opus-5`** — not Claude Fable 5 — in a maintainer-operated Claude Code session per [agents/README.md](../agents/README.md) (Operations), against the released, unedited `fable-model-chain/` (Python 3.11.2 + numpy 2.4.6, macOS/CPython). **The vote record below is evidence and is carried forward completely unedited**, per the [PR #93](https://github.com/ryoji-info/FableComputer/pull/93) round-2 precedent. Nothing in §§1, 3, 4, 5.2, 8 or 9 changed.

**The falsification, independently re-executed and confirmed.** At `loss` = 0.0 (the signature default), β = 0.25, `n_bias` = 0.54, `g_max` = 9.97, released `cell.transfer` carries an attracting 2-cycle **0.27759675 ↔ 1.06422564**, extinction **−11.672387 dB**, multiplier **−0.99582497**, orbit closing to |Δ| = 1.06×10⁻¹³ under 20,000 iterates of the released function. `g(a)·g(b)` = 1.000000000 exactly. The key `transfer_2cycle_extinction_dB` claimed 0 of 182 stable 2-cycles reach −10 dB and named precisely this as its falsifier. **It is falsified.** Both storing assessors record that they did not check it: Kinetic verified "only the signature-default exhibit, analytically", and Quanta ran the shipped `transfer_scan.py`, which reproduces its author's own lattice.

**Root cause: lattice aliasing, not an incomplete scan.** The deep attracting band hugs the 2→4 period-doubling boundary, and the census stepped `n_bias` on a 0.1 lattice. At `g_max` = 10, `loss` = 0, **neither** lattice point 0.5 nor 0.6 carries an attracting 2-cycle at all, while `n_bias` = 0.53981718 gives −11.6936 dB. A scan cannot find a feature narrower than its own step, and the four-decimal quote on "−6.0413" concealed that.

**What the rework measured that the original did not.** Three results, each executed:

1. **The frontier, traced on the period-doubling boundary** (bisecting `n_bias` to multiplier = −1): −10.9333 / −11.3463 / −11.5271 / −11.6120 / −11.6840 / **−11.6936 dB** at `g_max` = 8 / 9 / 9.5 / 9.75 / 9.97 / 10. Monotone in `g_max`, and bounded **by the box, not by the map**: `g_max` = 11 gives −11.9902 dB (past the strict anchor), then −12.2464 / −12.8426 / −13.4898 at 12 / 15 / 20; no attracting 2-cycle survives to 40.
2. **β is a pure amplitude scale.** B = β·A conjugates the map to a β-free one. Extinction and multiplier are identical to eight decimals across β ∈ {0.25, 0.5, 1, 2, 4}, with β·orbit invariant at 0.06939919 ↔ 0.26605641; β < 0 admits no positive 2-cycle. The 52,480-set census therefore holds at most 5,248 distinct systems.
3. **The empty-slot result is an identity.** `g(a)·g(b) = 1` for every positive 2-cycle, and `g` decreasing gives `g(0) > b/a > 1`, so `(T∘T)′(0) = g(0)² > 1`. §2.4(a) no longer needs the census. The argument is the dissent's and is adopted here with credit, per standing rule 5.

**One claim of the dissent that did *not* reproduce, recorded because the record is not improved by accepting a correction uncritically.** The dissent adds that allowing `loss` = −0.0947 gives "**−20.0000 dB** exactly, orbit 1 ↔ 10". At (`n_bias` 0.54, β 0.25, `g_max` 9.97, `loss` −0.0947) the released map's attractor is **0.330373 ↔ 1.137774 = −10.7410 dB** (multiplier −0.294100), and `T(1)` = 0.4294, so 1 ↔ 10 is not a 2-cycle of that map. **The −20 dB endpoint is therefore not carried into any claim here**, and the executor's original recommendation to restate the family as "at least −0.04 to −20 dB" is **declined**: the defensible span is −0.0439 to −11.6936 dB inside the census box. The primary falsification stands untouched — it was verified twice, by two independent methods.

**Sections changed by this revision:** the status line; §0 item 1 (heading, both bullets, conclusion); §2.4(a); §2.4(b) (heading and conclusion, with the lattice table retained and marked); §2.5 items 1 and 2; §6 (`transfer_2cycle_extinction_dB` recorded as falsified and replaced by `transfer_2cycle_extinction_family_dB`, plus two new keys) and its Part III consequence; §7 Limitation 1c, and a new 1d recording that `cell.py:transfer` is not Part I's Eq. (5). **No number in §§3, 4, 5.2 or 8 was touched**, and the two storing assessors' independent reproductions of those halves stand.

**What did not change: the conclusion.** Every corrected claim moves in the same direction — the released map is *less* determinate than this note said, not more. The strategic finding the note reached by its other route, and stated in its own §5.1 last row before any of this, is unaffected and is now the only reading its own evidence supports: **the released map supplies a family, not a bound, indexed by parameters the chain never fixes, so the '0'-floor spec must be imported.**

---

## Agent assessment — 2026-08-02

Assessed suitable for the permanent record by a **2-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)), **over a dissent that falsified a registered key**. The three assessors ran in isolated, mutually blind contexts — each adopted one persona with all standing rules, **re-executed the reply's key numbers itself against the released `fable-model-chain/` and `fable-model-quantum/` on this machine** rather than trusting the transcript, and checked the reply against the promoted notes in `notes/`. Their verdicts are reproduced verbatim as each returned it and are **not** edited after posting. Assessment executed on `claude-opus-5[1m]` (Claude Opus 5) — **not** Claude Fable 5; see the Author line above.

**Executor's note on the dissent, recorded because it changes how this note should be read.** Fabric voted reject on a counterexample to `transfer_2cycle_extinction_dB`. The executor re-ran it independently against released `cell.transfer` and **confirms it**: at `loss` = 0.0, β = 0.25, `n_bias` = 0.54, `g_max` = 9.97 the released map carries an attracting 2-cycle 0.277597 ↔ 1.064226 with extinction **−11.6724 dB** — past round (−10.0) and r\* (−11.2854), 0.15 dB short of strict — and a continuous `n_bias` × `g_max` sweep at that β and `loss` = 0 reaches **−11.57 dB at |multiplier| < 1, −11.25 at < 0.9, −10.59 at < 0.7 and −10.09 at < 0.5**. The falsification is therefore robust rather than a lattice knife edge, and the key is falsified by its own stated criterion. **Neither storing assessor checked this**: Kinetic records verifying "only the signature-default exhibit, analytically", and Quanta ran the shipped `transfer_scan.py` (which reproduces its author's own lattice) without an independent search. The vote stands at 2-of-3 and is not edited; the affected claims are §0 item 1, §2.4(b)'s two zero counts, §2.5 item 1, §6's `transfer_2cycle_extinction_dB` and §6's Part III framing. §7 Limitation 1c and the key's own falsifier both anticipated this exact failure, which is the record working — but a reader must not take the −1 to −6 dB bound as the released map's requirement.

- 🧵 **Fabric** — **REJECT**: I re-ran §8's `transfer_scan.py` and every expected output reproduced — g(0) = 3.0402174031457583, A* = 0.5445972584384384, 52,480 sets with 0 carrying more than one positive fixed point of T, 1,230 degenerate, 182 stable 2-cycles, 0 with an attracting A = 0, best extinction −6.0413 / median −1.8570 / worst −0.0439, the signature exhibit 0.338728 ↔ 0.415651 with separatrix 0.389145 — and `decode_demand.py` reproduced §5.2 exactly (replica bit-equal to released `error_2bit`/`error_1bit` at r = 0, T_2bit = 58.52734375, T_1bit = 243.765625, −22.41 / −11.10 / −9.68 dB, crossings 12.73 / 20.93 / 23.35 K), while my own three-rung refits of the promoted floors returned p = 0.7063 / 0.5483 / 0.1356 / 0.1474 / 0.8875 and F∞ = −10.884 / −9.693 / −6.697 / −6.975 / −7.611, matching §4 to the printed digit; source-side, `transfer` and `truth_table` are called nowhere outside `cell.py`, the code/prose gap is exactly 20·log₁₀(7/6) = +1.3389 dB, `K_MIN` = 5.0 is a yield criterion as §2.5 says, and all nine registered keys grep clean against both `results.json`, all of `notes/` and `papers/`. But I then rebuilt Half 1 independently from released `cell.transfer` and broke its headline: reducing a positive 2-cycle to (u, z_a, δ) leaves stability a two-parameter question, and at `loss` = 0.0 — the released signature default — with β = 0.25, one of the reply's own grid nodes, `n_bias` = 0.540000 and `g_max` = 9.970000, released `transfer` carries an attracting 2-cycle 0.277597 ↔ 1.064226 with extinction **−11.6724 dB**, confirmed by 20,000 iterates of the released function; allow `loss` = −0.0947 (the reply itself scans negative loss in §2.3) and it is **−20.0000 dB** exactly, orbit 1 ↔ 10. So §0 item 1's "at best −6.04 dB", §2.4(b)'s "0 reaching −10 dB", "looser than both branches by at least 4 dB", and the registered key `transfer_2cycle_extinction_dB` are false by that key's own stated falsification criterion, inside the reply's own parameter box — and the census is aliased, not merely incomplete: at the nearest grid node (0.5, 0.25, 10, 0.2) the reply's own root/multiplier pipeline returns −4.8418 dB against a −11.65 dB local frontier, a ~7 dB lattice error under a four-decimal quote, and the falsification survives at |multiplier| < 0.5, deeper restoration than the reply's own exhibit at −0.369. The other half of the census is meanwhile stronger than the reply claims and needs no census at all: g(a)·g(b) = 1 for every 2-cycle (I measured 0.9999942 on its exhibit), which forces β > 0 and g(0) > b/a > 1, so (T∘T)′(0) = g(0)² > 1 and A = 0 is repelling as an identity — Limitation 1c's hedge on §2.4(a) is unnecessary. I did **not** run `denom.py`, `denom480.py`, `knee_denom.py` or `knee_stream.py`, so every Half 2 number is unverified by me — the bit-identical anchor 8.287855791924017 / −11.828336851447219, the twelve paired rows, the argmax plane diagnostic, the knee control and the m = 26 rung all stand unchecked on my side, as does anything about `papers/` language or the solver cavity; I vote reject because a memo cannot enter the corrected record with its executive item 1 and one registered key already falsified in about three minutes of compute, when restating them as "the released map derives not a floor but a family spanning at least −0.04 to −20 dB, indexed by parameters the chain never fixes" reaches the same strategic conclusion the reply wants, is what its own §5.1 last row already says about the reconstruction, and is true.
  - FALSIFIED KEY. §6 `transfer_2cycle_extinction_dB` ("0 of 182 reach -10 dB"; falsified by "one parameter set whose released-transfer 2-cycle has extinction at or beyond -10 dB") is false. Released cell.transfer at loss = 0.0 (the signature default), beta = 0.25 (the reply's own grid node), n_bias = 0.540000, g_max = 9.970000 has an attracting 2-cycle 0.277597 <-> 1.064226: T(0.277597) = 1.0642259509499168, T(1.064226) = 0.2775964556312402, extinction -11.6724 dB. That beats round (-10.0) and r* (-11.2854) and is 0.15 dB short of strict. Confirmed by 20,000 iterates of the released function from 1.05x the '0' level.
  - FALSE HEADLINE. §0 item 1 ("at best -6.04 dB", "None reaches -10 dB, let alone r* (-11.285) or the strict anchor (-11.821)", "The requirement the released chain derives is -1 to -6 dB", "looser than both branches by at least 4 dB"), §2.4(b)'s table rows "count reaching -10.0 dB (round) = 0" and "count reaching -11.285 or -11.821 = 0" as claims about the map, §2.5 item 1's "the map has an attractor, not the map restores a '0' against a '1'", and §6's Part III consequence "It has one, and it is -1 to -6 dB" are all falsified by the counterexample above. The strategic conclusion (the spec must be imported) survives, but for the opposite reason to the one given.
  - Allowing loss slightly negative — which the reply itself scans in §2.3's mirror-branch rerun — released cell.transfer reaches -20.0000 dB exactly: n_bias = 1.216243281, beta = 0.1187432808, g_max = 9.90596455, loss = -0.09473369949, attracting orbit 1 <-> 10, verified on the released function. With loss >= 0 and g_max unbounded the frontier is -15.75 dB.
  - The 52,480-node census ALIASES the quantity it reports by about 7 dB. Running the reply's own roots()/multiplier logic at the grid node nearest my counterexample (n_bias 0.5, beta 0.25, g_max 10, loss 0.2) returns -4.8418 dB, against -11.65 dB at the true local frontier. A 41 x 10 x 16 x 8 lattice cannot support a 4-decimal quote (-6.0413) on a variable that moves 7 dB between adjacent nodes. Limitation 1c concedes the census is a scan, but §0 item 1, §2.4's bold sentence, §5.1's narrative and §6 all state it unhedged.
  - The falsification is not a knife-edge artifact. Inside the reply's own box (n_bias in [-1,3], g_max <= 10, loss in [0,3]) the deepest stable extinction is -11.6 dB at |multiplier| < 1, -11.3 at < 0.9, -10.7 at < 0.7 and -10.1 at < 0.5 — i.e. the round spec is still beaten with restoration stronger than the reply's own exhibit multiplier of -0.369.
  - §5.1 adjudication table, 'docstring reading' row (-10.482), 67 GHz cell: marked '✗ continuum'. §4's own fitted m = 30 continuum is -10.884 dB, which CLEARS -10.482 by 0.40 dB; both p = 1 intercepts (-11.031, -11.097) clear it too. Should be ✓. This is the same defect class as §9 item 5, which fixed two cells in this exact row and missed a third.
  - §2.4(a) is an identity, not a census, and is reported weaker than it is. For any positive 2-cycle {a,b}, g(a) = b/a and g(b) = a/b so g(a)g(b) = 1 (I measured 0.9999942510914825 on the reply's exhibit); g(a) > 1 > g(b) forces g decreasing, hence beta > 0, hence g(0) > g(a) = b/a > 1 and (ToT)'(0) = g(0)^2 > 1 always. Limitation 1c's hedge that an off-grid set could have an attracting empty slot is unnecessary — that half cannot be broken.
  - §4 and executive item 6 cite "arithmetic on the promoted §3 rungs" and say "the promoted §3 table prints m = 30 and m = 28 to four decimals but m = 26 and m = 22 to two". notes/2026-08-01-ratio-bias-gain-table.md §3's table prints ALL floors to two decimals (-11.83/-11.46/-11.32, -10.73/-10.40/-10.26). The four-decimal rungs actually used (-11.8283/-11.4628/-11.3187, -10.7312/-10.4030/-10.2615) are in that note's §5, not §3.
  - §4 quantifies the m = 26 ill-conditioning with the mildest of the three available single-rung perturbations. +/-0.005 dB on its N = 720 rung gives F_inf -5.361 to -7.823 (2.46 dB, as reported, reproduced by me using the 4-decimal N = 240 base). The same +/-0.005 dB on the N = 480 rung gives -2.452 to -7.971, a 5.52 dB swing. The reported figure understates the conditioning problem by more than a factor of two.
  - §5.1 carries sub-0.1 dB verdicts that never got the robustness test the winning prompt makes mandatory for anything turning on less than ~1 dB. r* is marked ✓ at m = 30 / N = 720 on a margin of -11.3187 + 11.285429 = 0.0333 dB, and round is marked ✓ at m = 26 / N = 720 on 0.0600 dB. Only the m = 30 / N = 240 strict boundary received the second-phase / second-seed treatment.
  - §0 item 2 and §2.5 say "the function's docstring states NM ≈ 0.5·(1 − 1/k)·(1 − 10^(−ext/20))". That formula is an inline code comment at cell.py line 70, not the docstring (line 69 reads only "Butterfly static noise margin as a fraction of the logic swing."). Related omission: the same comment's own sanity check, "reproduces ~0.2 at k=8, 10 dB", sits closer to the code's 0.2564 than to the prose form's 0.2992 — evidence for the code reading that the reply never reports while calling the two a disagreement.
  - The docstring/code gap has an exact closed form the reply never gives: at k = 8 the ratio of the two forms is (1 − 1/8)/(1 − 2/8) = 7/6, so the gap is exactly 20·log10(7/6) = 1.338790 dB, not merely a computed +1.3389.
  - §8 says "Four files" but six listings are shipped (transfer_scan.py, denom.py, knee_denom.py, knee_stream.py, decode_demand.py, denom480.py). §8's run order and its "complete sources follow verbatim" line both name only five, omitting denom480.py — the file that produces the four N = 480 phase/seed rows the adversarial composition lens forced (§9 item 8) and on which the sign-change half of key `floor_denomination_delta_dB_m30` rests. §8 states no expected output for it, against notes/README.md's requirement that expected outputs be stated so a reviewer can verify every headline number.
  - The shipped transfer_scan.py's own module docstring still says "the 356 stable 2-cycles of T o T" — the stale exploratory count that §9 item 17 corrects to 182 and declares the listing authoritative for. The artifact contradicts the correction that names it.
  - §8's stated cost "transfer_scan.py (~40 s)" is wrong on this machine: 116 s wall (98 s user). The §8 heading "Run order and cost on this machine (6 workers)" does not apply to this listing at all — it is single-threaded with no multiprocessing.
  - §0 item 1 and §9 item 2 quote the corrected closed form T'(A*) = −4.848420887181987; the shipped listing prints −4.848420887181988 on this machine (1 ULP). Immaterial to any verdict, but §9 item 2 exists precisely to make this digit exact.
  - §2.5 item 2's "the two routes disagree by 6 to 10 dB" inherits the falsified −1 to −6 dB extinction band. The separatrix-position claim (0.35–0.65 of swing) does survive my counterexample — its separatrix at 0.7073209385 sits at 0.548 of swing — but the dB gap against static_noise_margin's 0.2564 does not follow.
  - The scope disclaimers guard the wrong flank. Executive item 1's parenthetical and §7 item 1 both defend against reading item 1 as a claim about the physical fabric. Neither defends against the direction in which the reply actually over-reads: asserting a bounded grid census as a property of the released map. Limitation 1c is the only place that says so, and it is three sections away from four unhedged statements of the same claim.
- 🌊 **Kinetic** — **STORE**: I ran the anchor first, and it holds: `denom.py 6 240` on this machine returned the promoted m = 30/N = 240 ratio-bias row to the last float digit — G_worst1 = 8.287855791924017, floor = −11.828336851447219 — after reproducing M_th_num(240) = 0.16894319463373791 by the released bracket, and all twelve §3.2 paired rows then came back on my own runs exactly as printed, including the load-bearing sign change of the paired denomination delta at m = 30 (+0.0549 / +0.0619 / +0.0567 at N = 240 against −0.4452 / −0.3742 / −0.4440 at N = 480, replicated under both a second carrier phase and seed 11), the four paired gain moves (+0.3045 / +0.3757 / +0.2247 / +0.3009 dB), and the m = 28 phase instability the memo honestly refuses to rest a verdict on (−0.4194 → −0.1082 at N = 240, −0.3906 → +0.3161 at N = 480). `knee_stream.py 240 6 26,28,30` and `knee_denom.py 6 26,28,30` returned the whole §3.4/§5.3 knee table to the printed digit — the new m = 26 rung 0.01260 / 0.01230 with G_req 6.9675 / 6.9890 and clearance +1.0402 dB, on top of cav_u knees 0.01235/0.01208 and 0.01228/0.01203 that reproduce 08-01 §5 — and my own from-scratch argmax rebuild, written from the memo's stated conventions rather than run off its listing, reproduced §3.1's plane diagnostic (velocity argmax median index 8, 57.0 % inside the first 5 %; density argmax median 239, 63.3 % inside the last 5 %) and, restricted to the '0' slot alone — a cut the memo never made — still gives velocity median 5 and density median 239, so the boundary-condition mechanism claim is right and stronger than stated. I re-derived §4 by hand, independent of any listing: p = 0.7063 / 0.5483 / 0.1356–0.1474 / 0.8875 with F∞ = −10.884 / −9.693 / −6.697–−6.975 / −7.611, the p = 1 intercepts −11.031/−11.097 and −9.978/−10.075, and the memo's own ±0.005 dB N = 720 perturbation of m = 26 (p 0.1004–0.1955, F∞ −5.361 to −7.823, a 2.46 dB swing) all came back exactly — but §4 mis-locates its own rungs (the promoted §3 *table* prints every floor to two decimals; the four-decimal rungs are in §5), and read as §3 prints them the orders are 0.7786 and 0.5769, not 0.706 and 0.548, while at m = 22 the rungs' own ±0.005 quote rounding pushes p to 1.0382 — outside the registered band [0.1, 1.0] and reversing the very correction sign §4 calls robust. The m = 28 round-spec fail nevertheless survives every perturbation I tried (F∞ ∈ [−9.905, −9.402] on the 2-dp rungs, [−9.6956, −9.6906] on the 4-dp ones), and every registered key I could test reproduced, so the defects I list are promotion-edit and label tier, not measurement tier. What I did **not** run: `validate.py`'s (b) 07-25 probe rows (I checked only that its 250,167-step figure recomputes exactly and that `fs_driver.py` is byte-identical to the promoted 08-01 §8 listing), `decode_demand.py` and the whole §5.2 kelvin leg, the 52,480-set scan and 182-cycle census of §2.3/§2.4 (I verified only the signature-default exhibit, analytically), the clock-pumped reconstruction, the claimed measure_Mth_num bracket ceiling N ∈ (860, 880], and any N = 720 row.
  - §4 and the key `gated_floor_convergence_order_p` mis-cite their own source. The memo says "the promoted §3 table prints m = 30 and m = 28 to four decimals but m = 26 and m = 22 to two"; in fact notes/2026-08-01-ratio-bias-gain-table.md §3's table prints EVERY floor to two decimals (−11.83/−11.46/−11.32 at m = 30, −10.73/−10.40/−10.26 at m = 28) and the four-decimal rungs the fits actually consume are in §5. Read as §3 prints them I get p = 0.7786, F∞ = −10.9429 (m = 30) and p = 0.5769, F∞ = −9.7287 (m = 28) — not 0.706/−10.884 and 0.548/−9.693. The memo's own "give it both ways" policy for m = 26 was withheld from m = 30 and m = 28 on this false premise.
  - §4's "the sign of the correction is robust" and §6's registered band [0.1, 1.0] both fail at m = 22. Perturbing its 2-decimal rungs (−8.59/−8.14/−7.98) by their own ±0.005 dB quote rounding gives p up to 1.0382 (corner −8.595/−8.135/−7.985), i.e. p ≥ 1 in 7 of my 125 corner perturbations, above the registered upper edge and with the fitted continuum falling BELOW the p = 1 intercept — the sign reversal §4 says cannot happen. m = 30, m = 28 and m = 26 are robust (0/125 each).
  - §5.1's adjudication table, "docstring reading" row (−10.482), m = 30 continuum cell is marked ✗. The fitted-order continuum −10.884 clears −10.482 by +0.402 dB — it is a ✓. This is a third error in the same row §9 item 5 says an adversarial lens already corrected twice.
  - §2.4's exhibit table prints (T∘T)′ = −0.369448 at the '0' level and −0.369536 at the '1' level. A period-2 orbit has a single multiplier by the chain rule; the analytic value is T′(0.338728)·T′(0.415651) = −0.36947206549584516, and the separatrix multiplier is 1.818975033479819, not the printed +1.818971. Three finite-difference digits presented as exact, two of them mutually impossible — the same defect class §9 item 2 says was fixed for T′(A*), surviving in the table that replaces the withdrawn headline. Levels 0.338728/0.415651, separatrix 0.389145, g(0)² = 2.074226 and extinction −1.7776 dB all reproduce exactly.
  - Executive item 4 labels *Demonstrated* that "the swing the spec denominates, and the field the next cell receives, are drain-plane density." `cell.py`'s `cascade_per_cell_gain_dB` docstring annotates A_SAT_eff as "drive-plane amplitude", and §3.4's own A_SAT values (0.02354–0.02555) are derived from a SOURCE drive knee (0.01198–0.01300)/C_1DB. The plane attribution for A_SAT is in-model at best and contradicted by the released annotation — in the one memo whose declared method is a plane audit, and it is the premise of §6's top WP1 recommendation.
  - §3.1's "the drain-plane density floor equals the intracavity density floor exactly on five of the eight rows measured and to within 0.002 dB on the other three" is a stale count not updated after the four N = 480 variant rows were added; §3.2 now carries twelve rows. On my own twelve: nine exact, three (all m = 30/N = 240) differ — −11.7750 vs −11.7734, −11.7225 vs −11.7206, −11.7886 vs −11.7870, ≈ 0.0016 dB.
  - Executive item 5's headline — "unstable under *every* convention varied — carrier phase, PRBS seed and denomination alike" and "the +0.007 dB 'pass' is an artifact of one convention triple" — is contradicted by its own table two lines below and by §3.3. The seed-11 variant reads −11.8437, strict margin +0.0225: still a pass. §3.3's "three conventions were varied and two of them flip the verdict" is the accurate statement; the executive headline is not.
  - The `static_noise_margin` disagreement is between the code and an inline COMMENT, not the docstring — the docstring is the single line "Butterfly static noise margin as a fraction of the logic swing." The registered key name `static_noise_margin_docstring_code_gap_dB` bakes the imprecision in. Worse for the framing: the same comment states its own target, "reproduces ~0.2 at k=8, 10 dB", which the code's 0.25641458774368575 meets and the comment's own formula (0.2991503523676334) misses — so "a function whose prose and code disagree by three quarters of the fork" over-reads a stale formula whose stated numeric target agrees with the code. The +1.3389357926122631 dB arithmetic itself is exact and reproduces.
  - §8's file inventory is wrong three ways. It says "Four files"; its run order lists five (transfer_scan, denom, knee_denom, knee_stream, decode_demand); and it omits `denom480.py` entirely — yet as shipped, `denom.py 6 240,480` gates the phase/seed variants on `if 240 in mthn` and therefore produces eight rows, not the "twelve paired rows including the phase/seed variants" §8 promises. The four N = 480 variant rows require denom480.py, which only the separate listings comment ships and prices. §8 also costs transfer_scan.py at ~40 s where the listings comment says ~3 min.
  - §7 Limitation 2 discloses the density channel's missing published anchor, but frames it as a computation-validation gap ("validated only by construction and by the internal drn_h ≡ cav_h consistency"). The step §3–§5 actually lean on is an IDENTIFICATION, not a computation: that max_x|h − 1| scored as max-'0'-over-mean-'1' is the density analogue of the `extinction_dB` the heuristic is fed. Nothing in the memo tests that identification, and §6's top WP1 recommendation ("pin the floor OBSERVABLE — the drain-plane density ratio") rests entirely on it. Given how much weight §3.3, §5.1 and two registered keys put on the density channel, the disclosure is honest but under-scoped.
  - §3.2's table shows "—" in the `drn_u` column for four of the six N = 480 rows. These are not missing measurements: denom480.py computes and stores drn_u and simply does not print it. My runs give drn_u = −11.0839 (m = 28 slot), −11.0094 (m = 28 seed 11), −11.9908 (m = 30 slot), −11.9282 (m = 30 seed 11). A table cell that reads as unmeasured when the listing measured it.
  - `knee_stream.py` shipped in §8 silently shadows the promoted 08-01 §8 listing of the same name (this session's version adds m = 26 and a CLI). §8 gives no warning to a reproducer who extracts both promoted and session listings into one directory; the extraction prepared for this review hit exactly that collision.
- ⚛️ **Quanta** — **STORE**: I ran `decode_demand.py` and then rebuilt §5.2 independently from the released source alone — calling `qmac._propagate`, `qmac.decision_variance` and `qnoise.symbol_error` myself rather than the session's file — and the floored-'0' replica is bit-equal to released `error_2bit`/`error_1bit` at 353/300/150/77/20/4 K (0.003095733579221082 at 77 K), returns T_2bit = 58.52734375 and T_1bit = 243.765625, and reproduces the whole demand table (−22.4105 / −17.4477 / −13.6161 / −12.2207 / −11.0984 / −10.2657 / −9.7892 / −9.6756 dB) and every crossing (12.7259 / 20.9251 / 23.3529 / 30.4607 K); a closed form I derived myself, Perr = 0.75·erfc(d(1−r)/(2√(2V))), reproduces all of it to six digits, because a co-phased residual shrinks both decode gaps by exactly (1−r) and leaves V untouched. I also ran `transfer_scan.py` (2 min 56 s here, not the ~40 s §8 quotes): 52,480 sets, 0 with two positive roots, 1,230 degenerate, 182 stable 2-cycles, 0 with an attracting A = 0, best −6.0413 dB, exhibit 0.338728 ↔ 0.415651; and I re-derived the four spec anchors (−11.821145 / −13.759346 / −10.482210, r\* = 3/11 = −11.285429), the +1.338936 dB docstring/code gap, and every §4 order (0.706343 / 0.548262 / 0.135552 / 0.147396 / 0.887549) with the m = 26 ±0.005 dB excursion (p 0.1004–0.1955, F∞ −5.361 to −7.823) from the promoted rungs — all correct. Where the reply is wrong is the physics of §5.2(b): at 4 K the released decision variance is 1.079367 = 0.500005 vacuum + 0.451092 Caves-limited comparator amplifier + 0.128270 threshold band, so the band is the *smallest* term, and deleting it entirely leaves the demand saturated at −8.6492 dB — the T → 0 floor is a quantum limit, not the sharpness artefact the text names, and the §6 key's own falsifier ("removing the static threshold-band term would unsaturate the T → 0 limit") is false against the released code. The replica also silently fixes the residual in-phase with the comb reference (30° loosens the 20 K demand by 1.25 dB, 45° by 3.01 dB, quadrature makes it invisible) and silently assumes the comparators re-trim to the floored midpoints — hold the thresholds at their r = 0 trim and the demand is 9.0–9.5 dB stricter (−19.148 dB at 4 K), with no candidate spec crossing anywhere in 4–58 K; at 07-15's own c = 0.02 the crossings move to 20.06 / 26.12 / 28.26 / 34.88 K and at k_dec = 8 they vanish. I did **not** re-run `denom.py`, `denom480.py`, `knee_denom.py` or `knee_stream.py`, so every §3 paired row, every §3.4 clearance and the new m = 26 knee are unverified by me; I checked §4 only as arithmetic on the promoted rungs and ran nothing on the solver. I vote store because the substance, the self-refutation and the reproducibility are exemplary and every number I could reach is exact — but items 1–5 below must be recorded as the note's known defects.
  - §5.2(b) and §6 key `decode_floor_demand_1e3_dB`: the T → 0 saturation is mis-attributed. At 4 K the released decision variance is 1.079367 = 0.500005 (vacuum) + 0.451092 (decoder amplifier, the Caves-limited (F_dec−1)(n̄+½)) + 0.128270 (threshold band) — the band is 11.9 %, the smallest of three terms. Setting it to zero leaves the saturated demand at −8.6492 dB instead of −9.6756: the limit does not unsaturate. The key's stated falsifier — 'any physical accumulator or decode topology that removes the static threshold-band term, which would unsaturate the T → 0 limit' — is therefore false against the released code. The true floor is vacuum + Caves added noise, which is a stronger and more durable result than the one asserted.
  - §5.2 / executive item 7: the replica fixes the '0' residual perfectly in phase with the homodyne/comb reference and never says so. Gaps scale as (1 − r·cosφ), so r_max(φ) = r_max(0)/cosφ: at φ = 30° the 20 K demand is −9.849 dB (1.25 dB looser), at 45° −8.088 dB (3.01 dB looser, more than the 1.82 dB fork the session adjudicates), and at quadrature the residual is invisible to the decode entirely. notes/2026-07-22-cavity-ringdown-isi.md (loaded ring-down) and the session's own recorded concerns 21(8) and 33(2) both say this phase moves with slot length and grid. No limitation, label or key names the assumption.
  - §5.2: the replica assumes the comparator thresholds re-trim to the floored midpoints (`qnoise.symbol_error` uses midpoint thresholds). Hold the thresholds at their r = 0 trim and the demand becomes −27.251 dB (48 K), −20.075 dB (20 K), −19.148 dB (4 K) — 9.0–9.5 dB stricter, and no candidate spec crosses anywhere in 4–58 K. That single unstated assumption is worth five times the strict-vs-round fork.
  - §5.2(b) / §7 Limitation 8: c is named open per 07-15 but never priced, and the price is comparable to the effect being reported. At 07-15's own R2 bound c = 0.02 (rail-clamped) the crossings move 12.73 → 20.06 K (round), 20.93 → 26.12 (r*), 23.35 → 28.26 (strict), 30.46 → 34.88 (k = 5) — a 7.3 K shift against the 10.6 K headroom item 7 reports as the whole fork's worth.
  - §5.2(b): k_dec = 16 is read correctly from `qdecode.K_DEC`, but the leg's dependence on it is unstated. At k_dec = 8 the saturated demand is −13.246 dB and no candidate spec crosses in 4–58 K; at 07-15's k_dec = 1.60 (an untouched Part-I logic cell used as the comparator) the decode tolerates no residual at any temperature. 07-15 records k_dec ≥ 16 as 'a Part-II requirement with no Part-I achievability basis' demanding a 10× β/Δn comparator redesign; the reply cites 07-15 only for c.
  - §5.2(b) describes `qdecode.threshold_band_variance` as 'a deterministic transfer that does not cool away' and then uses its variance. That is the exact category 07-15's erratum retired — a deterministic monotone transfer contributes no decision variance; the code's term survives only re-booked as the trim residual V_static = c²(x_range/k_dec)². The phrasing rests on a reading a promoted note corrected.
  - §0 executive verdict: the notes/README-mandated form 'demonstrated (runnable, see listing)' appears nowhere in §0. Items 1 (the 182 stable 2-cycles), 4 (paired channels), 5 (12 rows), 7 (the floored-'0' replica) and 8 (the m = 26 knee) all rest on constructions absent from the released chains and are tagged plainly '*Demonstrated (…)*'. The mandated form appears in exactly five places: §2.4 and four §6 keys. §9 item 11's claim that the fix landed is therefore only partly true — it did not land in the section a reader reads first.
  - Executive item 7: the spec-crossing temperatures 12.73 / 20.93 / 23.35 / 30.46 K are asserted inside a paragraph opened by '*Demonstrated (…)*', with '*In-model* throughout' arriving only after them — the precise defect §9 item 10 says was caught and corrected. §5.2(a) carries the explicit 'In-model at the point of assertion' phrasing; the executive verdict does not, so the fix landed in one of the two places the same numbers are asserted.
  - §5.2(b)'s headline sentence — 'The demand saturates and can never be stricter than ≈ −9.7 dB' — carries no epistemic label at the point of assertion; the '*In-model consequence:*' tag attaches only to the sentence after it.
  - §5.2: the credential 'validated bit-for-bit at r = 0' certifies the *unmodified* path, not the modification. I verified the modification's entire content is that both gaps scale as exactly (1 − r) with V unchanged (9.925290 → 8.932761 at r = 0.1 and 6.947703 at r = 0.3, V identical at 48/20/4 K), so the demand table is the r = 0 SNR margin rescaled. The reply should say so, since a reader may take the bit-exactness as evidence for the demand itself.
  - §4 mis-citation: the four-decimal rungs the order fit consumes (m = 30: −11.8283/−11.4628/−11.3187; m = 28: −10.7312/−10.4030/−10.2615) come from §5 of notes/2026-08-01-ratio-bias-gain-table.md, not its §3 — §3's floor column prints two decimals for all four slots. The reply states 'the promoted §3 table prints m = 30 and m = 28 to four decimals but m = 26 and m = 22 to two', which is false, and its footnote 'the 2-decimal reading is the one a reader following §3 alone reproduces' then misdescribes m = 30 and m = 28 as well. The fitted values themselves are correct — I reproduced 0.706343/−10.884169, 0.548262/−9.693107, 0.135552/−6.697174, 0.147396/−6.974874, 0.887549/−7.610607.
  - §8 is out of sync with the listings comment it introduces: §8 says 'Four files' where six are shipped, its run order omits `denom480.py` (which produced the four N = 480 phase/seed rows §9 item 8 says were added before publication), and it prices `transfer_scan.py` at '~40 s' where the listings comment says ~3 min and I measured 2 min 56 s.
  - §8 expected outputs state T′(A*) = −4.848420887181987; the shipped `transfer_scan.py` prints −4.848420887181988 (1 ULP). Numerically irrelevant, but §8 is the reproducer's contract and §9 item 2 is specifically about this digit.
  - Filename collision: this session's `knee_stream.py` shares its name with a different program shipped in promoted notes/2026-08-01-gated-requirement-round-trip.md §8. A reader assembling both notes' listings in one directory silently keeps one of them — it happened in my own extraction. Rename or namespace before promotion.
  - §5.2's closing 'Labels, stated' paragraph places the `qerrors.NM_CLASSICAL` remark immediately after the kelvin figures. The remark itself is correct — I confirmed NM_CLASSICAL = 0.2564 vs the chain's 0.25641458774368575 (−0.000494 dB), that `qerrors.classical_ber` is its only consumer (margin = NM_CLASSICAL·x_swing), and that `classical_BER_300K` = 3.6059121172811077e-11 and `classical_BER_353K` = 9.101052631220227e-10 both exist — but NM_CLASSICAL is *not* in the decode path, so its placement invites a reader to think the demand table inherits it. Worth one clarifying clause, since the demand's independence from NM_CLASSICAL is what makes it a candidate imported spec at all.
