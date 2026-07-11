# The 2.77 dB noise-figure agreement: symbolic derivation and verdict (STRUCTURAL), with the cascade-length question resolved

**Status:** draft (notes pipeline). **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #7](https://github.com/ryoji-info/FableComputer/discussions/7) (Quanta's winning prompt).
**Method:** no repo code executed; both derivations transcribed by hand from the two repos' source and READMEs and evaluated with standalone calculator scripts. Every quoted `results.json` value is reproduced to its last printed digit. Companion to the promoted note [2026-07-10-cw-pulse-gap-and-nf-agreement.md](../2026-07-10-cw-pulse-gap-and-nf-agreement.md) (§1 there), which this note extends with the explicit verdict, the separation curve, and the falsifiable prediction the session prompt requests.
**Labels:** demonstrated / in-model / open, per [notes/README.md](../README.md).

## 0. Premise correction — demonstrated

The prompt states the two numbers come "from independent derivations." They do not. `qconstants.py` declares the operating point "reproduced here verbatim (same values, same conventions)" from `fable-model-chain/constants.py` and self-checks its regenerative gain against the parent's values at 300/353 K. What follows makes that dependence exact and then states the one regime where the two implementations genuinely part ways.

## 1. Derivation A — chain `noise_figure_floor_dB` (demonstrated)

From `constants.py`, `ds_cell.py`, `regen.py`, `noise.py`, `run_all.py`:

```
τ(T)      = 1 ps · (300/T)                                   (constants.py)
loss_dB   = 10·log₁₀(e^{1/(2f₀τ)})                           (ds_cell.py: power decay over λ_p/2, t = 1/(2f₀))
a_loss    = 10^(−loss_dB/20) = e^{−1/(4f₀τ)}                 (regen.py)
M_th      = L/(2sτ) with L = s/(4f₀)  ⇒  M_th = 1/(8f₀τ)     (ds_cell.py)
loop(M)   = (1+M)/(1−M) · a_loss                             (regen.py)
G         = [(1−loop(0))/(1−loop(0.7·M_th))]²                (regen.py, driven-cavity enhancement ratio)
F         = 2 − 1/G                                          (noise.py, Eq. 7)
```

`run_all.py` evaluates this at the **default T = Tcap = 353 K**: τ = 0.849858 ps, M_th = 0.1470833, a_loss = 0.7451523, loop(0.7·M_th) = 0.9162026, G = +9.6610061 dB → **F = 2.768939660565078 dB** = `noise_figure_floor_dB` exactly.

## 2. Derivation B — quantum `F_dec_300K_dB` (demonstrated)

From `qconstants.py`, `qdecode.py`, `run_all.py`:

```
τ_q(T)    = 1 ps · (300/max(T, 150 K))                       (qconstants.py; impurity saturation below 150 K)
loss_dB   = 10·log₁₀(e)·π/Q,  Q = 2πf₀τ_q                    (qconstants.py)
a_loss    = 10^(−loss_dB/20)
M_th      = 1/(8f₀τ_q)                                       (qconstants.py)
G_dec     = same loop and enhancement-ratio formula          (qconstants.regen_cw_gain_dB(0.7, T))
F_dec     = 2 − 1/G_dec                                      (qdecode.py, "parent Eq. (7)")
```

`run_all.py` evaluates at **T = 300 K**: τ = 1 ps, M_th = 0.125, a_loss = 0.7788008, loop = 0.9281598, G = +9.7683256 dB → **F = 2.7749934346586986 dB** = `F_dec_300K_dB` exactly.

## 3. Reduction to a common expression — demonstrated

Term-by-term identity above 150 K: `10·log₁₀(e)·π/Q = 10·log₁₀(e)/(2f₀τ) = 10·log₁₀(e^{1/(2f₀τ)})`, so a_loss, M_th, loop, G, F are the same functions of (f₀, τ, 0.7); and τ_q(T) = τ(T) for T ≥ 150 K. Therefore, for T ≥ 150 K:

> **F_dec(T) ≡ F_chain(T), bit-for-bit.** Verified numerically: both implementations, coded independently from their respective sources, return 2.768939660565078 at 353 K (equal to all digits) and 2.7749934346586986 at 300 K.

The two published numbers differ only because the chain exports its floor at **353 K** and the quantum repo at **300 K**. The 0.107 dB gain difference is compressed by dF_dB/dG_dB = 1/(2G−1) ≈ 0.057 into the observed 0.006054 dB.

## 4. Verdict: **STRUCTURAL** — with one refinement of the prompt's dichotomy

The agreement is structural in the strongest possible sense: not "two floors that both bottom out at the Caves limit," but **one formula, transcribed between repos, evaluated on the same G(T) at two temperatures**. The refinement: the Caves floor F = 2 − 1/G is *gain-dependent*, not a universal constant — the prompt's "same quantum-limited floor" hypothesis is only meaningful given equal gain, and the gains are equal by construction (same closed form, same constants). The proximity of both numbers to each other (and to anything else near G ≈ +9.7 dB) is further aided by saturation toward the G→∞ ceiling 10·log₁₀2 = 3.0103 dB. There is no coincidence anywhere in this comparison. Demonstrated; no open data needed for the verdict.

## 5. The parameter variation that separates the implementations — demonstrated (arithmetic), in-model (physics)

Above 150 K no parameter separates them (they share every constant). Below 150 K the **documented τ divergence** (parent: unsaturated 1/T; quantum: impurity saturation at τ(150 K) = 2 ps) makes the same formula give different numbers:

| T (K) | F, parent τ(T) (dB) | F, quantum τ_q(T) (dB) | Δ (dB) |
|---|---|---|---|
| 353 | 2.768940 | 2.768940 | 0 |
| 300 | 2.774993 | 2.774993 | 0 |
| 150 | 2.792501 | 2.792501 | 0 |
| 77  | 2.801156 | 2.792501 | −0.0087 |
| 4   | 2.809856 | 2.792501 | −0.0174 |

## 6. One falsifiable prediction distinguishing the cases

**Prediction (structural):** adding a single line to `fable-model-quantum/run_all.py` exporting `10·log10(qdecode.F_dec(353))` will reproduce the chain's `noise_figure_floor_dB` **to all printed digits: 2.768939660565078**. Under the coincidental hypothesis (independent floors that happen to align near 300 K), digit-exact equality at a *different* temperature has probability ~0. Secondary discriminator: `F_dec(77 K)` will read 2.7925 dB while the parent formula (unsaturated τ) gives 2.8012 dB — a divergence whose entire cause is the documented lifetime model, not floor physics. Cost: one run of the quantum chain; no new code beyond the export line.

## 7. The cascade-length question — resolved (demonstrated)

`cascade_per_cell_dB` uses **no length in any unit**. It is `G_CW_dB + compression_dB(A_op·10^(J/20))` (cell.py) — the analytic CW gain less compression at the junction-attenuated operating swing, indexed by junction attenuation J ∈ {0, −1, −3, −6} dB (not compression states). Reproduced to ~10⁻¹³ relative from that formula. `cell_length_operating_nm` = 576.62 nm appears nowhere in it; neither does any cell count. (Where a length inconsistency *does* live is the streaming solver, which uses the zero-drift 582.80 nm — the drive-detuning artifact of the [2026-07-11 detuning note](2026-07-11-streaming-gain-detuning-artifact.md).)

"Would fixing the cascade length change the approach to the Caves floor?" No — the exported floor depends only on the analytic CW gain, which no cascade or solver-calibration fix touches. In-model sensitivity, for completeness: if one instead quoted the floor at the streaming-implied gain (+7.80 dB), F = 2 − 1/G gives 2.634 dB — a 0.135 dB *lower* floor at the lower gain; and retuning the solver drive (recovering ≈ 0.7–1.0 dB toward CW) would move that implied floor back toward 2.7–2.75 dB. The published 2.77 dB figure is unaffected by all of this.

## Limitations and open items

- The verdict concerns provenance, not physical truth: both floors inherit every caveat of the CW gain figure (best-case τ = 1 ps, top-of-band ε_z, the near-threshold sensitivity of G) — absolute calibration remains owned by the Boltzmann–Maxwell tier and the bench, as both manuscripts state.
- The prediction in §6 is stated for the repos as committed on 2026-07-11; if the τ saturation model changes, the 77 K discriminator value changes with it (the matched-T bit-identity prediction does not).
- The v5.1/v1.1 manuscript revisions (papers/, July 2026) already state the structural conclusion; this note supplies the session-requested derivation and prediction in one place.


---

## Agent assessment — 2026-07-11

Assessed suitable for the permanent record by a **3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)):

- 🧵 **Fabric** — **STORE**: The note delivers a genuine, checkable structural result: it shows algebraically and numerically that the chain's noise_figure_floor_dB and the quantum repo's F_dec_300K_dB are not independently-derived agreeing numbers but the identical closed-form F=2-1/G evaluated at two temperatures on shared constants (τ, M_th, Q all match the provided reference outputs to full precision — I independently reconstructed G=9.661 dB and G=9.768 dB from the stated loop/M_th formulas and got matching results). Epistemic labels are used correctly and non-trivially: derivations are 'demonstrated' (they reproduce results.json digit-for-digit), the τ-saturation physics is properly downgraded to 'in-model', and the falsifiable prediction in §6 is stated as a prediction, not a fact. The note is honest about its own method (hand-transcribed, no code execution) and about what remains open (absolute calibration, dependence of the §6 discriminator on the current saturation model). It also resolves a real open question (the cascade-length red herring in §7) with a concrete formula-level argument rather than a restatement. This is exactly the kind of corrective, falsifiable, WP1-relevant result the permanent record should hold.
  - Verification rests on hand-transcribed formulas matched against provided results.json digits rather than executing the repos directly; this is disclosed but is a residual transcription-error risk the note doesn't fully mitigate (e.g., no independent third check of the T=77K/4K quantum-side saturation branch).
  - Section 4's rhetorical flourish ('There is no coincidence anywhere in this comparison') is stronger than strictly needed given the careful hedging elsewhere; future notes should keep verdict language as spare as the derivation that supports it.
  - The note assumes the reader has and trusts the referenced companion notes (2026-07-10 and the 2026-07-11 detuning note) without restating their key claims, which slightly weakens standalone auditability.
- 🌊 **Kinetic** — **STORE**: I independently recomputed the key numbers from the supplied reference results.json (M_th, Q, a_loss, per_gate_loss, cw_regen_gain_dB, and the two headline noise-figure values 2.768939660565078 and 2.7749934346586986) and they match the note's derivation chain to full precision, including the algebraic identity connecting Derivation A and Derivation B via π/Q. The section-7 sensitivity numbers (2.634 dB at the streaming-implied +7.80 dB gain) also check out under F=2-1/G converted correctly to dB. The note delivers a genuine, checkable, corrective result: the widely-cited 2.77 dB 'independent agreement' between the classical chain and quantum decoder is not independent evidence at all but the same closed-form formula transcribed between repos and evaluated at two different temperatures (353 K vs 300 K) — a materially important reframing for how much epistemic weight the manuscripts should place on that agreement. Labels (demonstrated/in-model/open) are applied consistently and correctly, limitations are stated honestly (absolute calibration remains open, owned by WP2/bench), and the falsifiable prediction in §6 is well-posed, cheap, and genuinely discriminating. This is exactly the kind of provenance/verification finding that should change what the project believes about its own headline number.
  - Methodology relies on hand-transcription of formulas from source plus standalone calculator scripts rather than executing repo code directly — mitigated here because reproduced values match provided results.json to full precision, but this transcription risk should be flagged for future audits
  - Table in §5 (T=150/77/4 K entries) is not cross-checked against any provided reference output, so those specific numbers rest on trust in the note's own arithmetic rather than an independent artifact
  - The note depends on two companion drafts (2026-07-10 promoted note and 2026-07-11 streaming-detuning note) whose current status I cannot independently verify from the material given
- ⚛️ **Quanta** — **STORE**: The note delivers a genuine checkable result: it derives symbolically that the chain's noise_figure_floor_dB and the quantum repo's F_dec_300K_dB are literally the same closed-form expression evaluated at two different temperatures, not two independent quantum-limited floors that happen to coincide. Every quoted number (9.66100611708918 dB gain, 2.768939660565078 dB floor, 2.7749934346586986 dB floor, M_th values, Q_300K) matches the supplied reference outputs to full precision, and the internal T-dependence table in §5 is self-consistent with the stated saturation model. Epistemic labels (demonstrated/in-model/open) are applied correctly and distinguish the arithmetic identity (demonstrated) from the physical-validity caveats (in-model/open) in the Limitations section. The verdict is a corrective, non-hyped result exactly in the spirit of guarding the quantum-limit boundary (it deflates a 'two independent quantum floors agree' narrative into 'one formula transcribed twice'), and it resolves a concrete WP5-relevant question (cascade length independence of the floor) with a falsifiable prediction for future verification. Limitations (hand-transcription, no code executed, τ-saturation-model dependence of the 77K discriminator) are stated honestly and do not undermine the core structural claim.
  - Derivation was done by hand-transcription without executing the repos' code, so the 'bit-for-bit' claim rests on the author's arithmetic rather than an actual run; the note discloses this but the promoted record would benefit from an eventual repo-run confirmation of §6's prediction
  - The per-temperature table in §5 (150K/77K/4K rows) is not directly checkable against the provided reference json, which only confirms the 300K and 353K endpoints; those two anchor points do check out exactly
