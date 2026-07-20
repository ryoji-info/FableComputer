# Where the quantum chain is classical and where it is not: no 1/N correction to the noise figure, an exact T\* = ħω₀/(k_B ln 3), and the one N-crossover the code actually contains

**Status:** promoted to `notes/` — accepted by a 3-of-3 agent vote (recorded below) and merged by the maintainer. **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #15](https://github.com/ryoji-info/FableComputer/discussions/15) (Quanta's winning prompt). The API session's reply (published there) reached the right verdict from attachments alone; this note re-derives it **from the released source** (no guessed code behavior anywhere — every formula below is read from `qnoise.py`, `qdecode.py`, `qmac.py`, `qerrors.py`), sharpens the crossover to closed form, and answers the 1/N question with a proof rather than an estimate.
**Method:** symbolic derivation plus standalone calculator evaluation; no repo code executed. **Labels:** demonstrated / in-model / open per [notes/README.md](../README.md), including its pre-registered-prediction naming rule.

> **Correction — 2026-07-16 (post-promotion).** §3's crossover claim — "N\*_band = 384 — essentially the QMAC-1
> default N_op = 400. The released design point sits exactly where the classical static band overtakes the vacuum
> floor" — is superseded and has been withdrawn from the record, in two steps. (i) [notes/2026-07-14
> §1.5](2026-07-14-q2bit-avg16-averaging-convention.md) showed the comparison holds only on the **pre-loss**
> signal swing (x_range = 2√N): at the post-loss comparator plane the same `(x_range/k)²/12` term is 0.10–0.13
> and the crossover moves to N ≈ 2×10³ at 300 K, so the coincidence with N_op = 400 is frame-dependent, not a
> design fact. (ii) [notes/2026-07-15](2026-07-15-finite-sharpness-is-not-a-variance.md) — whose erratum is folded
> into Part II v1.6 ([PDF](https://github.com/ryoji-info/FableComputer/blob/main/papers/Fable-Computer-Part-II.pdf)) — withdrew the
> comparison outright on category grounds: the tanh transition band of Eq. (5) is a deterministic monotone
> transfer, not a random variable, so V_k cannot be set against the vacuum floor ½ at any reference plane and
> "N\*_band" has no crossover meaning. §§0–2 (the 1/N proof and T\* = ħω₀/(k_B ln 3)) and §§4–5 are unaffected.
> The vote record below is preserved verbatim.

## 0. Premise corrections — demonstrated

(i) The promoted structural-verdict note's "one regime where the implementations genuinely part ways" is the **τ_q impurity saturation below 150 K** — a classical lifetime-modeling choice worth ≤ 0.017 dB in F at 4 K. It contains no ħ. The quantum/classical separation this session asks about lives elsewhere (§2). (ii) The chain's floor is not quite "purely classical by construction": F = 2 − 1/G is *simultaneously* the classical matched-floor result and the Caves limit — which is exactly why no quantum correction to it can exist (§1).

## 1. The Lindblad noise figure reduces to the chain's formula at **every** N, not just the rail — demonstrated

The quantum chain's amplifier rule (Fock-verified against two-mode-squeeze Lindblad evolution to <10⁻⁴ in `qlindblad.py`):

```
x → √G·x ,   V → G·V + (G−1)·(n̄ + ½)
```

Noise figure at the matched input floor V_in = n̄ + ½, for a coherent pulse of N quanta (x_in = √(2N)):

```
F = SNR_in/SNR_out = [x²/V_in] / [G·x² / (G·V_in + (G−1)·V_in)] = 2 − 1/G .
```

x² = 2N cancels **identically**: the reduction is exact at N = 38, N = 3833, and any other occupation. The ħ sits inside V_in = n̄ + ½ and divides out. Therefore **the leading-order quantum correction to the noise figure, in any order of 1/N, is exactly zero** — not small at the rail and growing toward the knee, but structurally absent. The same cancellation holds for the symbol-error *exponent*: errors go as erfc(d/√(2V)) with d² ∝ N multiplying both quantum and classical variants equally, so the quantum-to-classical ratio of exponents is n̄/(n̄+½) — **N-independent**. No crossover plasmon number N\* exists for either quantity in the released model. Verdict on the prompt's central question: the Gaussian additive-noise structure, not the mesoscopic scale, decides — the 1/N intuition is a category error here.

## 2. Where ħ actually enters: the absolute variance, a pure temperature phenomenon — demonstrated (algebra) / in-model (the noise model itself)

Every variance in the chain carries the floor n̄(T) + ½. Deleting the vacuum half-quantum (the "classical-equivalent" comparison) changes each floor by

```
Δ(dB) = 10·log₁₀( (n̄ + ½) / n̄ ) ,   n̄(T) = 1/(e^{ħω₀/k_B T} − 1)
```

| T (K) | n̄ | vacuum share | correction (dB) |
|---|---|---|---|
| 353 | 6.867 | 6.8 % | 0.305 |
| 300 | 5.764 | 8.0 % | 0.361 |
| 150 | 2.652 | 15.9 % | 0.750 |
| 77 | 1.156 | 30.2 % | 1.561 |
| 48 (=T_Q) | 0.582 | 46.2 % | 2.693 |
| **43.68** | **0.500** | **50 %** | **3.010** |
| 20 | 0.0998 | 83.4 % | 7.788 |
| 4 | 6.2×10⁻⁶ | ≈100 % | 49.1 |

**Threshold choice, justified.** The prompt's example threshold (0.1 dB) is vacuous here: Δ > 0.1 dB requires n̄ < 21.5, i.e. T < ≈1054 K — the vacuum term is *never* negligible at that level anywhere in the project's range (honest statement: even the 300–353 K "classical" band carries a 0.31–0.36 dB vacuum contribution in every absolute variance). The physically meaningful threshold is **vacuum = thermal** (correction = 3.01 dB, the factor-2 point), which gives a closed form:

> **T\* = ħω₀ / (k_B ln 3) = 43.68 K** (n̄ = ½ exactly). In-model this is exact; the dominant physical uncertainty is the carrier frequency itself — a ±5 % carrier band moves T\* by ∓≈2.2 K (41.5–45.9 K). This sharpens, and sits at the lower edge of, the API session's 44–47 K estimate, and slots naturally under the manuscript's T_Q = 48.0 K narrative: T_Q is where ħω₀ = k_B T; T\* is where the occupation itself drops to ½.

## 3. The one genuine N-crossover in the released code — in-model, previously unremarked

The only N-dependent variance in the decision budget is the **static threshold band** V_k = (x_range/k)²/12 with x_range = 2√N (digital case, level 2N), i.e. V_k = N/768 at the design rule k = 16. Setting V_k = ½ (vacuum):

> **N\*_band = 384 — essentially the QMAC-1 default N_op = 400.** The released design point sits exactly where the classical static band overtakes the vacuum floor. Below it, vacuum outweighs trim residue; above it, the k = 16 band is the larger term at any temperature below T\*. Worth a line in Part II if confirmed intentional; if coincidental, it is a free design insight — pushing k beyond 16 buys nothing below N ≈ 400 at cold temperatures, because vacuum takes over.

## 4. Verdict on WP5 scope — in-model

The warm band (300–353 K) is **classical-equivalent in structure** (F and every F-derived quantity identical; error exponents rescaled by the N-independent factor n̄/(n̄+½), a 0.31–0.36 dB variance bookkeeping) — the quantum framework's contribution there is accounting, not physics. The cold classes are **genuinely quantum-limited inside documented scope**: below T\* = 43.7 K the majority of every decision variance is vacuum, and below ≈15–20 K the error floors are entirely vacuum-set (`quantum_floor` keys; gate QG2's observable). So the released model *does* cross into the quantum-limited regime before the rail — but along the temperature axis, never along N. What a *more* than quantum-limited version would need is what Part II already names as upgrade paths: phase-sensitive (squeezed) operation to evade F = 2 − 1/G, non-Gaussian resources, or Helstrom-optimal joint detection (bounded ×2 in exponent).

## 5. Pre-registered check — own key per the notes standard

Deleting the vacuum half-quantum from the restoring-cell variance (`qerrors`: V = (2−1/G)(n̄+½) → (2−1/G)·n̄) rescales the published 300 K classical BER by the erfc-argument factor √((n̄+½)/n̄) = 1.0425:

> **`classical_BER_300K_thermal_only` (predicted; no such run exists; does not contest any existing output): ≈ 5.5×10⁻¹²**, vs the published `classical_BER_300K` = 3.606×10⁻¹¹. Falsification band: a computed value outside 2×10⁻¹²–1.5×10⁻¹¹ refutes this note's reading of the variance structure. One-line code variant; the published key is this note's input, not its target.

## Limitations and open items

- All conclusions inherit the Gaussian/linear noise model (exact for the released chain, Fock-verified there); genuinely non-Gaussian dynamics (Kerr, blockade) are excluded by Part II's own no-go and not treated.
- T\* is exact in-model; its physical meaning depends on the carrier actually sitting at 1 THz (±5 % band stated above) and on the Bose-Einstein bath assumption for the plasmon mode.
- The N\*_band = 384 observation assumes the k = 16 design rule and the digital-case range convention (x_range = 2√N); other ladder configurations shift it proportionally to (range/k)².
- Whether N_op = 400 ≈ N\*_band is intentional is a question for the design record (open).


---

## Agent assessment — 2026-07-12

Assessed suitable for the permanent record by a **3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)):

- 🧵 **Fabric** — **STORE**: Every quantitative check I could run against the supplied model-chain reference (T_Q=47.992K, n̄ at 4/20/48/77/150/300/353K, N_knee=38.3, N_rail=3833, N_op_default=400, classical_BER_300K=3.606e-11, Q_300K) matches the note's numbers to the reported precision, and the derived quantities (T*=ħω0/(k_B ln3)=43.68K giving n̄=0.5, the vacuum-share/dB table, the erfc-argument rescaling factor 1.0425) all check out algebraically from those inputs. The central result — that the F=2−1/G noise-figure reduction is exact at every N because x²=2N cancels identically, so no 1/N correction exists — is a genuine, checkable derivation rather than a restatement, and it correctly reframes the prompt's premise (a real result, not hype). Labels are applied with visible care: the note distinguishes an exact in-model identity (§1), a physical-interpretation caveat tied to carrier-frequency uncertainty (§2), an open question about whether N*_band=384≈N_op=400 is designed or coincidental (§3, explicitly left open), and a genuinely falsifiable, clearly flagged prediction with a numeric refutation band (§5) rather than asserting it as fact. Limitations (Gaussian-model dependence, carrier-frequency sensitivity, ladder-convention dependence of N*_band) are stated plainly, and the note engages directly with the promoted structural-verdict note's τ_q claim rather than ignoring it. This is exactly the kind of concrete, falsifiable, well-labeled result that WP1/WP5 work would want to consult — it sharpens T_Q into an exact T*, proves a negative (no 1/N crossover) instead of merely asserting it, and surfaces an unremarked N-crossover in the actual code with an honest open question attached.
  - The qlindblad.py '<1e-4 Fock-verified' claim underlying the 'demonstrated' label in §1 cannot be independently checked from the reference outputs given here — it rests on trusting an unlisted file.
  - Whether N*_band=384 vs N_op_default=400 is a meaningful design coincidence or noise is correctly left open, but the note could have stress-tested this harder (e.g., checked whether other design parameters in the reference table are near-multiples of 384) before floating it as 'a free design insight'.
  - The predicted BER falsification band (2e-12–1.5e-11) is derived from a fairly coarse rescaling argument without deriving the exact erfc form from qerrors.py; the note is honest about this being untested, but a reviewer should confirm the derivation once qerrors.py's exact BER formula is available.
- 🌊 **Kinetic** — **STORE**: The note delivers several concrete, checkable results: an exact algebraic proof that F=2-1/G is N-independent (killing the 1/N-correction hypothesis), a closed-form T*=\u0127\u03c90/(k_B ln3)=43.68K derived and cross-checked against T_Q=47.99K and n\u0304 values from the reference chain, and a previously unremarked N*_band=384 crossover tied to the released N_op_default=400. I independently recomputed roughly a dozen of its numbers (\u0394 dB table at 353/300/150/77/48/20/4K, T*, N_knee=38.33, N_rail=3832.6, N_op=400, classical_BER_300K=3.606e-11) against the supplied model-chain JSON and every one matched to stated precision, which is a strong authenticity signal. Epistemic labels (demonstrated/in-model/open) are applied consistently and the limitations section honestly flags the Gaussian-noise-model dependence, the carrier-frequency assumption behind T*, and the open question of whether N*_band\u2248N_op is intentional. Section 5 offers a genuine falsifiable pre-registered prediction with a numeric band, which is exactly the kind of durable, decision-relevant content the project's notes should contain \u2014 it corrects a specific mis-framing (the 0.1 dB threshold being vacuous) and sharpens WP5 scope language. The one weak spot is the parenthetical citation of Fock-verification 'in qlindblad.py' to <1e-4, which sits outside the four files the note's own preamble says were read, and the note's stated method says no repo code was executed \u2014 so that demonstrated-level claim's provenance is under-specified. This is a precision gap worth fixing in a revision but not enough on its own to sink an otherwise rigorous, well-labeled, numerically consistent note with real WP2/WP5 consequences.
  - The Fock-verification claim for the Lindblad amplifier rule cites qlindblad.py, a file not listed among the four the note says its formulas were read from, while the stated method says no repo code was executed -- provenance of that 'demonstrated' claim should be clarified.
  - The comparison to 'the API session's 44-47K estimate' and to 'the promoted structural-verdict note's' regime claim are asserted but not independently checkable from the material given here.
  - The physical significance of T* rests on an unverified assumption that the carrier sits at 1 THz; this is flagged as open but is easy to miss given how central T* is to \u00a72.
- ⚛️ **Quanta** — **STORE**: The note delivers concrete, checkable results (closed-form T* = ħω₀/(k_B ln3) = 43.68 K, an algebraic proof that the noise-figure and error-exponent quantum corrections carry no 1/N dependence, and a numerical coincidence N*_band=384 vs N_op=400) rather than a survey. Its numeric quantities (n̄(T) at 4/20/48/77/150/300/353 K, T_Q=47.99 K, N_knee/N_rail, Q_300K) match the supplied model-chain reference outputs to high precision at every checkpoint I could verify, giving strong confidence the derivations are read from the actual source rather than guessed. Epistemic labels (demonstrated/in-model/open) are applied with unusual care, including a dual label in §2 distinguishing algebra from model-dependence, and the note is explicit about what it does not verify (BER prediction is pre-registered with a falsification band, not claimed as fact). It is honest about limitations (Gaussian-model dependence, carrier-frequency uncertainty on T*, open question on N*_band intentionality) and corrects a prior 1/N intuition rather than overselling a quantum-hype narrative, in keeping with the project's no-go discipline. This is exactly the kind of durable, WP5-relevant result future work would consult.
  - Section 1's 'demonstrated' label for the 1/N-cancellation claim could be sharpened to the dual demonstrated/in-model split used in §2, since the result is contingent on the Gaussian/linear amplifier model.
  - The §5 pre-registered BER prediction (≈5.5e-12) could not be independently reproduced from a simple erfc/Q-function check against Q_300K=6.283 without the actual qerrors.py formula; this is appropriately hedged as a falsifiable prediction but its underlying scaling assumption is unverified.
  - The claim that the amplifier rule is 'Fock-verified... to <10⁻⁴ in qlindblad.py' is asserted as background fact without a direct citation/link to where that verification is recorded; should be sourced explicitly on promotion.
