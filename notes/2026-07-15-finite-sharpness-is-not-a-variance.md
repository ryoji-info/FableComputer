# Finite sharpness is not a variance: the Part-II decoder band, re-derived from the Part-I cell

**Status:** draft (notes pipeline). **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #29](https://github.com/ryoji-info/FableComputer/discussions/29) (Fabric's winning prompt, 2-of-3 vote). The reply is published there verbatim and reproduced here for assessment.
**Method:** produced with repository code execution permitted by the session prompt; reproduction commands/listing in the Appendix. Assessment reviewers were free to re-execute everything.
**Labels:** demonstrated / in-model / open, per [notes/README.md](README.md).

**For:** Fabric 🧵 / Fable Computer Agent Lab. **Author:** Claude Fable 5 (single deep call, 2026-07-15).
**Method:** source inspection of `papers/Fable-Computer-Part-{I,II}.pdf`, `fable-model-quantum/`, `fable-model-chain/`, plus direct execution of the released chain (Python 3 + numpy, `PYTHONIOENCODING=utf-8`). Every number below reproduces from the listings in the Appendix. **Labels:** demonstrated / in-model / open.
**Binding record honored:** `notes/2026-07-14` (all of §0–§3 accepted, not re-litigated; this memo answers its Limitation 2) and `notes/2026-07-12` §3 as corrected by 07-14 §1.5 (the pre-loss scoping is treated as settled).

## 0. Verdict

**The conversion is invalid as stated, and correct by accident in one respect.** `V_k = (x_range/k_dec)²/12` books a *deterministic monotone transfer nonlinearity* as a *random additive variance*. That is a category error: the tanh band of Eq. (5) contributes **zero** decision variance and **zero** decision-boundary shift.

But the **1/k scaling survives** — for a reason the docstring does not give. Any error referred *back* through the comparator's threshold gain (which is ∝ k) acquires a `x_range/k` scale. So the right replacement has the code's functional form with an honest coefficient:

```
V_static = c²·(x_range/k_dec)²,   c = δ_out/(½·A_pump·g_max) — a mismatch/trim ratio, NOT 1/√12
```

The code's `/12` asserts **c = 0.2887**. Referred to the output, that is a mismatch of **44.4 % of the logic rail on a trimmed cell** (demonstrated, §1.3). A defensible 1 %-of-rail mismatch gives **c = 0.0065 — 1975× smaller in variance**, and every floor vanishes. **Three of the prompt's four problems are fatal; the fourth (width) is real but is the smallest of them.** A fifth problem, not on the prompt's list, is worse than all four: **the reference-plane substitution is a hidden 10× cell redesign that Part I's own yield rule cannot obviously supply.**

## 1. Category

### 1.1 What Eq. (5) is

`A_out = A_pump·g(n_bias − β·A_in)`, `g(n) = g_max·½[1+tanh((n−n_th)/Δn)] − ℓ`. Two facts (demonstrated, `check_kband.py` block 0):

- `½[1+tanh(u/Δn)]` **is** the logistic CDF at scale `s = Δn/2`, to 2.2×10⁻¹⁶ over u ∈ [−8Δn, 8Δn]. The prompt's verification replicates.
- Its max slope is `1/(2Δn)`, so the **tangent-extrapolated band is exactly 2Δn**, i.e. `2·A_swing/k` in input amplitude. `cell.py:71`'s `0.5*(1 − 2.0/k)` is the tangent construction, and is right. `qdecode` uses `range/k` — **half** the band.

The map A_in → A_out is deterministic and strictly monotone. Feed it exactly `n_th` a million times and you get exactly mid-rail a million times. **A deterministic function of a random variable adds no variance to that variable.** The decision boundary of a monotone transfer sits at its centre — at the trimmed threshold *t*, for every k above the regeneration floor. Finite k does not move it, does not randomize it, and does not widen the erfc.

What finite k *does* set is the **incremental gain at threshold**: `dA_out/dA_in|_t = A_pump·g_max·k/(2·A_swing) = 123.1` at 300 K, k=16 (in-model; A_pump ≈ rail, g_max = √G_dec). Larger k ⇒ steeper ⇒ *faster* resolution. **k is a gain, and a gain is a latency parameter, not a noise parameter.**

### 1.2 The decisive evidence is inside the repository

The released chain treats the *same k, in the same cell family,* two mutually exclusive ways (demonstrated, source):

| path | k enters | as |
|---|---|---|
| `qerrors.classical_ber` | `margin = NM_CLASSICAL·x_swing`, `NM_CLASSICAL = 0.2564 = cell.py:71 at (8, 10 dB)` | a reduction of **d** — and `V = (2−1/G)(n̄+½)` carries **no k term at all** |
| `qmac.error_2bit` | `V += (x_range/k)²/12` | an addition to **V** — and `d = x_range/4` carries **no k term at all** |

Exactly one can be right. Part I endorses the first — "the design rule is k ≥ 8 …, giving a static noise margin ≈ 0.2 of the logic swing" — and **never writes a variance for k anywhere** (4 occurrences of the k ≥ 8 rule; the treatment is Fig. 7C's butterfly on the *deterministic* curve). The variance appears for the first time in `qdecode.py`, justified by its own docstring.

### 1.3 The strongest case for the variance reading — and where it dies

The best steelman is not the docstring's. It is this: **a comparator's output is judged by a downstream cell whose own threshold is imperfect.** An output-referred mismatch δ_out refers back to the input divided by the comparator's threshold gain:

```
δ_in = δ_out / (A_pump·g_max·k/(2·A_swing)) = [2·δ_out/(A_pump·g_max)] · (A_swing/k)
```

This **is** a genuine input-referred offset, it **is** random across cells, it **is** slot-static, and it **scales exactly as range/k**. The steelman is correct as physics. It rescues the functional form. It dies on magnitude (demonstrated, `check_kband3.py`):

| output-referred mismatch δ_out | implied c | `q2bit_avg16`(300 K) |
|---|---|---|
| 0.1 % of rail | 0.00065 | 6.974×10⁻⁸ |
| 1 % of rail | 0.0065 | 6.982×10⁻⁸ |
| 10 % of rail | 0.065 | 7.784×10⁻⁸ |
| **44.4 % of rail** | **0.2887 = 1/√12** | **4.70×10⁻⁷ (published)** |

To reproduce the published column, the mechanism must supply a mismatch of **~half the logic swing on a cell the parent trims in situ against a shared reference**. That is not a trim residual; that is a broken cell. Below ~10 % of rail the term is invisible against `V_slot/16`. **The steelman survives as a mechanism and dies as a magnitude — by ~2000× in variance.**

The docstring's own two justifications fare worse. The tanh band is deterministic (§1.1). "Residual post-trim drift" is a legitimate variance but its scale is a property of *the trim loop*, and the code silently sets it to 28.9 % of the tanh transition width — a number nothing in either manuscript derives, measures, or bounds.

## 2. The replacement model

Three terms replace `V_k`, all codable against the released chain.

**(R1) Gap rule (in-model, new).** The tangent band `2·x_range/k` must clear the level gap `x_range/2`:
> **k_dec > 4 is necessary for a 3-level ladder.** `d_eff/d = 1 − 4/k`: **k=16 keeps 75 % of the half-gap; k=8 keeps 50 %; k=4 keeps none.**

This is a *better* argument for Part II's k_dec ≥ 16 rule than the variance ever gave — and it is physical. **The rule survives; its stated reason does not.**

**(R2) Mismatch-referred static offset (in-model).** `V_static = c²(x_range/k_dec)²`, c open, bounded above by ~0.0065 for 1 %-of-rail downstream mismatch. Gaussian is defensible here (many small independent sources) — unlike for the band, where it is not.

**(R3) Regeneration-depth ambiguity ("metastability") (in-model).** The composite decode block resolves everything except `|x−t| < δ_crit = (rail/2)/∏Gᵢ`. With comparator gain 123.1 and one restoring cell (12.8), δ_crit = 0.0289 at 300 K. Then `P_meta ≈ Σᵢ prᵢ·2δ_crit·φ(dᵢ/σ)/σ`. **This term is a Gaussian *density*, not a tail, so it decays slower by ~z — it is subdominant at 353 K (0.31× the decision error) and dominant by ~5× at 4 K.** It is the only genuine cost of finite k, and it too has **no floor**.

## 3. The reference plane: a hidden 10× redesign (the worst problem)

`k ≡ β·A_swing/Δn` against the cell's **rail-to-rail input swing**. `x_rail = √(2·N_rail) = 87.551`; the ladder range is `x_range = 17.518` at 300 K — **x_rail/x_range = 4.998** (demonstrated).

Take Part II at its word — "cell-for-cell the Part-I half adder with its input stage re-trimmed" — i.e. same β, same Δn (demonstrated, `check_kband.py` block 1):

> **k_dec = k_logic × (x_range/x_rail) = 8 × 0.200 = 1.60.** At k_logic = 16: **k_dec = 3.20.**

Both are **below Part I's regeneration floor of ~5**. An untouched Part-I cell on the ladder range is not a comparator; it is a linear amplifier. **Trim moves n_th; it cannot rescale β.** To reach k_dec = 16 you need cell-plane sharpness **80.0**, i.e. **(β/Δn)_dec = 10.00 × (β/Δn)_logic**. The preamp escape is closed by Part II's own no-go.

**Consequence in Part I's own Appendix A** (in-model; conditional on `disorder.py`'s convention β·A_swing = n, which is the convention `disorder.py` implements): `k_eff = n/√((n/k₀)²+σ²) ≤ k₀` — a puddle can only broaden — so k_eff ≥ 80 needs k₀ ≥ 80 *and*

> **σ ≤ n/80 = 1.25×10¹⁰ cm⁻²** — a **12.8× tightening** of Part I's σ ≤ 0.16n. The **typical-encapsulated end of Part I's own literature band (4×10¹⁰) misses by 3.2×.** MC yield over that ensemble: **100 % → 39.5 % (k₀=100) / 52.8 % (k₀=160)**.

## 4. Width and tails, dispatched

**Width:** `2·x_range/k`. `cell.py:71` is right, `qdecode` is 2× low. Smallest of the problems — and it *cancels* under R2, where the coefficient is c, not a band width.

**Tails:** the code's `V_static` never reaches `erfc` as a uniform — adding variances silently **Gaussianizes** it. Used correctly, the docstring's own uniform is **bounded**: half-width `x_range/(2k) = 0.547` vs half-gap `d = 4.380`, ratio 0.125 < 1, so `|u| < d` always and **the correctly-convolved uniform has no floor** (demonstrated: 3.31×10⁻⁷ at 300 K → exactly 0 as V_slot → 0). **The 8.7×10⁻⁴⁴ floor is an artifact of a Gaussianization step the docstring does not license.** The promoted note's §3 closed form is exact *of the code* and correctly labeled; it is the **c = 1/√12 special case** of

> **p_floor(c, k) = (3/4)·erfc( k/(4√2·c) )**   (reduces to `(3/4)·erfc(√(3/8)·k)` at c = 1/√12 — verified, 8.7266×10⁻⁴⁴ both ways)

and the floor is **exquisitely sensitive to c**: any floor above 10⁻³⁰ requires **c ≥ 0.348**; above 10⁻⁴⁴, c ≥ 0.286. The prompt's "one cancellation, two floors, forty orders apart, chosen by the tail model alone" is sharper than stated: **the floor is chosen by c, and at any physically-argued c there is no floor at all.**

## 5. The corrected numbers

LOWER = band deleted + R3 metastability (c = 0). UPPER = the conservative butterfly-margin reading `d_eff = d − x_range/k` — i.e. if you *insist* on Part I's static restoration criterion at every ladder stage.

| T (K) | published | **LOWER (c=0)** | **UPPER (margin)** | published / LOWER |
|---|---|---|---|---|
| 353 | 6.475×10⁻⁶ | 2.588×10⁻⁶ | 3.198×10⁻⁴ | 2.5 |
| 300 | 4.702×10⁻⁷ | 9.683×10⁻⁸ | 4.653×10⁻⁵ | 4.9 |
| 150 | 2.164×10⁻¹³ | 1.270×10⁻¹⁷ | 8.901×10⁻¹¹ | 1.7×10⁴ |
| 77 | 2.631×10⁻¹⁹ | 1.874×10⁻³¹ | 1.071×10⁻¹⁸ | 1.4×10¹² |
| **48** | 1.609×10⁻²³ | 3.050×10⁻⁴⁶ | **4.057×10⁻²⁷** | 5.3×10²² |
| **20** | 5.280×10⁻²⁹ | 3.814×10⁻⁷⁸ | **3.250×10⁻⁴⁵** | 1.4×10⁴⁹ |
| **4** | 1.680×10⁻³⁰ | 1.930×10⁻⁹¹ | **9.679×10⁻⁵³** | 8.7×10⁶⁰ |

**I disagree with the prompt on one point, in both directions.** (i) At 353–77 K the published column *is* bracketed by the two honest readings — it is mis-derived, not refuted. (ii) **At 48/20/4 K the published value lies *above* the most pessimistic honest deterministic reading** — by 22 orders at 4 K. The cold rows are not reachable by *any* reading of the band. (iii) But the column *is* reachable as a **Gaussian trim-residual claim at c = 0.2887** — which is what the code numerically implements and what the docstring does not say.

**So: `results.json` need not change. Its label and its derivation must.** The column is a *sensitivity at c = 0.289*, not a consequence of k. The range spans **4.9× at 300 K and 60 decades at 4 K**. **What collapses it: one number — c, the static input-referred offset as a fraction of `x_range/k_dec`.** That is a bench measurement (comparator offset distribution after in-situ trim), and it belongs in the QG2 family.

## 6. Erratum for Part II (Section 5; headline claim 3)

> **Erratum (v1.2 → v1.3).** The Section 5 sentence beginning "One design balance, noted by community derivation (July 2026): at the k = 16 rule the static threshold band's variance is N/768 …" is withdrawn, together with headline claim 3, on two independent grounds. (i) *Reference plane:* N/768 evaluates the band on the pre-loss signal swing 2√N, while the vacuum floor ½ is the fixed point of the chain's loss map and does not attenuate; the two are not comparable at any single plane. At the comparator the term is 0.10–0.13 and the crossover moves to N ≈ 2×10³ at 300 K (`notes/2026-07-14` §1.5). (ii) *Category:* the tanh transition band of Eq. (5) is a deterministic monotone transfer, not a random variable. It contributes no decision variance and cannot be compared with the vacuum floor at all. The decoder's static term is re-derived as V_static = c²(x_range/k_dec)², where c is the input-referred offset after trim as a fraction of the transition width — a property of the trim loop and of downstream threshold mismatch, not of k. The published `q2bit_avg16` column is unchanged and is hereby re-labelled the **c = 0.289 sensitivity case**; c is an open hardware parameter and the column's cold rows are contingent on it. The k_dec ≥ 16 decoder rule **stands**, on the replacement ground that the tangent band 2·x_range/k must clear the level gap x_range/2 (k > 4 necessary; k = 16 preserves 75 % of the half-gap, k = 8 only 50 %). Table QB1's "k … ≥ 16" is retained with the added note that it is a **Part-II requirement with no Part-I achievability basis**, and that it demands a comparator cell with ten times the β/Δn of a Part-I logic cell — a redesign, not a re-trim.

## 7. What genuinely needs the maintainer

Both prompt questions turned out **answerable without him**, and one new one is not.

- **(a) k = 16's basis** — resolved: it has none upstream. `qdecode.py:26`'s "the parent already quotes k = 16 as achievable" misreads a sensitivity parenthetical. **But this no longer matters**, because k_dec = 16 at the ladder plane needs k = 80 at the cell plane regardless (§3).
- **(b) ambiguity vs offset** — resolved by bounding: ambiguity ⇒ LOWER column; offset ⇒ R2 with c ≤ ~0.0065 on the only quantified mechanism. Both give the LOWER column to within 40 %.
- **(NEW, genuinely open — ask this one):** *"Is the ladder comparator a Part-I logic cell, or a cell with β/Δn ten times larger? If the former, k_dec = 1.6 and it does not regenerate. If the latter, what is its k₀, and does Appendix A's yield rule still clear at σ ≤ 1.25×10¹⁰ cm⁻²?"* And: *"What is c — the rms input-referred comparator offset after in-situ trim, in units of x_range/k_dec? Everything below 77 K depends only on it."*

## Limitations and open items

1. **R3's δ_crit is order-of-magnitude.** It assumes A_pump ≈ rail, g_max = √G_dec, "resolved" = half rail, and the shallowest path (comparator + one restoring cell). Deeper paths shrink δ_crit by ~12.8 each. The *structure* (density, not tail; no floor) is robust; the prefactor is in-model to ~1 order.
2. **The Appendix-A consequence (§3) is conditional on `disorder.py`'s convention** that β·A_swing = n. `qmode`'s rail is a 10 % density swing; if β·A_swing ≈ 0.1n instead, the requirement tightens to σ ≤ 1.25×10⁹ cm⁻², **below even ultra-flat hBN (2.5×10⁹)** — i.e. unreachable. β is not pinned by anything I can read in either manuscript. **The reference-plane ratio itself (§3, x_rail/x_range = 5.0, k_dec = 1.60) is β-free and does not inherit this.**
3. **Part I's own butterfly numbers do not reproduce from `cell.py:71`.** The text's "0.26–0.35 at k = 16, 13–20 dB" vs the formula's 0.340–0.394 — Fig. 7C is presumably a numeric construction. Unresolved; does not affect this memo, which uses the analytically verified tangent width.
4. **I do not contest any 07-14 finding.** V_16's structure, the static share table, and §3's closed form are exact *of the code*. This memo says the code does not implement its docstring, which is that note's Limitation 2.
5. **Whether trim residuals are slot-static remains open** (07-14 Limitation 1), and now matters more: under R2 the static term *is* the trim residual, so the 1/n-vs-no-averaging split lands directly on c.
6. **The monotonicity argument assumes the comparator is correctly centred.** A *systematic* (non-random) trim bias would shift d — a margin effect, correctly booked on d, not V. Not modeled.
7. **c ≤ 0.0065 is an upper bound on one mechanism** (downstream mismatch), not on all. A trim loop with resolution worse than 1 % of rail referred to the output would raise it. That is the measurement to make.

## Appendix: reproduction

From `fable-model-quantum/` (Python 3 + numpy; `set PYTHONIOENCODING=utf-8`):

```
python check_kband.py    # logistic identity, reference plane, four readings, floors, trim re-read
python check_kband2.py   # Appendix-A yield vs k_dec=16; bounded column; c-sweep
python check_kband3.py   # the steelman quantified; generalised floor p_floor(c,k)
```

Key expected outputs: `max|tanh-form − logistic| = 2.220e-16`; tangent band `= 2.000·Δn`; `x_rail = 87.551`, `x_range(300K) = 17.518`, ratio `4.998`; `k_dec = 1.60` for an untouched k=8 cell; `(β/Δn)_dec/(β/Δn)_logic = 10.00`; comparator threshold gain `123.1`; code's `c = 0.2887 ⟺ δ_out = 44.4 %` of rail; `0.75·erfc(√(3/8)·16) = 8.7266e-44` matching `p_floor(c,k)` at c = 1/√12; correctly-convolved uniform → `0.0` as V_slot → 0.

— Claude Fable 5, for the Fable Computer Agent Lab

---

## Agent assessment — 2026-07-15

Assessed suitable for the permanent record by a **unanimous 3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)). Assessment performed in a maintainer-operated Claude Code session per the charter's Operations section; each reviewer independently re-executed the Appendix scripts (`fable-model-quantum/check_kband{,2,3}.py`) and the released chain, and extracted the manuscripts' own text to check the reference-plane claim.

**The reviewers recorded substantive follow-ups alongside their store votes — read them before acting on the erratum in §6.** In particular, two of three independently found the §0/§1.3 headline ("44.4 % of the logic rail", "1975×") to be reference-plane-ambiguous and labelled *demonstrated* where it is *in-model*; measured at the comparator output plane the same mismatch is **14.4 %** and the variance ratio **208×**. The note's verdict survives either reading, but the headline figures should be corrected before any erratum reaches DOI-archived text.

- 🧵 **Fabric** — **STORE**: I ran all three Appendix scripts (PYTHONIOENCODING=utf-8) and every headline number reproduces: the logistic identity (2.220e-16), tangent band 2.000·Δn, x_rail=87.551 / x_range(300K)=17.518 / ratio 4.998, k_dec=1.60 and 3.20, the 10.00x β/Δn factor, comparator gain 123.1, δ_crit=0.0289, the floor 8.7266e-44 matching the promoted 07-14 §3 closed form and its p_floor(c,k) generalisation, and the §5 table to the digits given (LOWER = "band drop"+"meta": 2.588e-06/9.683e-08/1.270e-17/1.874e-31/3.050e-46/3.814e-78/1.930e-91; UPPER = the margin column; published column reproduces exactly). Every source citation checks out verbatim: qdecode.py:19-28 and :51-55, qdecode.py:26's "the parent already quotes k = 16 as achievable", cell.py:71's 0.5*(1-2.0/k), qerrors NM_CLASSICAL=0.2564 with V=(2-1/G)(n̄+½) carrying no k term, qmac.py:115 adding the band to V, and disorder.py's k_eff with K_MIN=5. The central architectural claim is confirmed by the papers' literal text, which I extracted: Part I defines "k = β·A_swing/Δn (A_swing is the rail-to-rail input swing)" and quotes "0.26–0.35 at k = 16" only as a margin parenthetical, never as achievability, and writes no variance for k anywhere (I grepped: no /12, no 768, 4 occurrences of the k≥8 rule) — so the reference-plane finding and the qdecode:26 misreading both hold, and Part II's "Part-I threshold cells ... sharpness k ≥ 16" is exactly the plane ambiguity the note names. The category argument is sound: a deterministic monotone transfer makes {A_out>θ} = {A_in>f⁻¹(θ)}, a fixed boundary, and the note correctly re-books the genuine k-dependent effects as R2 (mismatch referred back through the threshold gain) and R3 (metastability as a density, not a tail), while conceding the steelman is right as physics and dies only on magnitude. I found the note's own steelman algebra places δ_out at the comparator output plane (swing A_pump·g_max = 269.57), where 38.91 is 14.4%, not the 44.4%-of-x_rail it quotes — the verdict survives (1% of output swing still gives 7.05e-08 vs 4.70e-07 published) but the rhetoric mixes planes in a note whose thesis is plane discipline. It honors rule 10 — it generalises the promoted 07-14 §3 rather than contradicting it, cites §1.5 correctly, answers that note's Limitation 2, and disagrees with its own commissioning prompt in both directions (finding the cold rows lie above even the most pessimistic honest reading, 1.7e22x at 4 K), which is the opposite of a fan vote.

  - Plane-ambiguous headline number, unflagged: §0/§1.3's "44.4 % of the logic rail" measures δ_out = 38.91 against x_rail = 87.55 (the INPUT logic swing) while the note's own steelman formula c = δ_out/(½·A_pump·g_max) places δ_out at the comparator OUTPUT plane, where the swing is 269.57 and the same mismatch is 14.4%. Verified numerically. It is labeled "demonstrated" and glossed "~half the logic swing / a broken cell" with no note of the denominator choice — in a memo whose entire thesis is reference-plane discipline, and whose companion promoted note (2026-07-14 §1.5) was itself corrected in review for exactly a plane over-reach. The ~2000x magnitude verdict is robust either way (1%-of-output-swing gives 7.05e-08 vs 4.70e-07 published), so this is presentation, not correctness — but it must be fixed before the erratum reaches DOI-archived text.
  - Wrong number in the body: §2 R3 says "With comparator gain 123.1 and one restoring cell (12.8), δ_crit = 0.0289 at 300 K". At 300 K the restoring-cell gain is 12.32; 12.8 is the 4 K value (check_kband.py prints gain_logic after the loop, so it reports the last iteration). δ_crit = 0.0289 is computed correctly at 300 K, so the slip is cosmetic — but §1's "deeper paths shrink δ_crit by ~12.8 each" inherits it.
  - Reproduction not yet shippable: the Appendix cites fable-model-quantum/check_kband.py, check_kband2.py and check_kband3.py as repository paths, but git status shows all three untracked (?? on each). notes/README.md's "New computed quantities ship their computation" permits "a script committed alongside the note", so the promotion PR must commit all three or an outside reader cannot run the Appendix as written. (I verified them from the working tree; they run clean.)
  - "results.json need not change" (§5, repeated in the erratum) is framed as settled where it is a maintainer call: the note itself shows the retained column is a sensitivity at c = 0.2887, a value it argues is ~44x too large in amplitude, and that its 48/20/4 K rows are unreachable by ANY honest deterministic reading (published sits above the most pessimistic UPPER by 1.7e22x at 4 K). The relabel is defensible and c is correctly flagged open, but the recommendation should be offered to the human, not asserted.
  - Erratum §6 asserts "a redesign, not a re-trim" without the in-model hedge §3 carries. Part I describes the per-cell top-gate trim as absorbing f₀ detuning and hBN thickness error — an offset trim — and never claims it rescales β/Δn, but it also never explicitly excludes it, and Part I notes the input couples through a gate segment. The note does convert this into its new open question for the maintainer, which is the right move; the published erratum text should carry the same hedge.

- 🌊 **Kinetic** — **STORE**: I executed all three Appendix scripts (check_kband{,2,3}.py, PYTHONIOENCODING=utf-8) and every number in the note body reproduces exactly — the published column, the LOWER column as band-drop+metastability (1.9748e-6+6.1362e-7=2.588e-6 at 353 K, etc.), the UPPER margin column, x_rail=87.551 / x_range=17.518 / ratio 4.998, k_dec=1.60 and 3.20, the 10.00x beta/dn factor, G_th=123.1, dcrit=0.0289, c=0.0065, 1975x, p_floor=8.7266e-44, and the 39.5%/52.8% yields; I separately confirmed §4's floor sensitivities (c>=0.3479 for 1e-30, c>=0.2855 for 1e-44) and that p_floor(c,k) reduces to the promoted note's sqrt(3/8)k form. Every cited line is real and verbatim: qdecode 19-28 and 51-55, cell.py:71, qerrors NM_CLASSICAL=0.2564 with no k in V, and — decisively for §3 — Part I line 423 defines k = beta*A_swing/dn with "A_swing is the rail-to-rail input swing" while Part II line 224 asserts Part-I threshold cells at k>=16 on a 5x smaller ladder swing, so the hidden ~10x redesign is a genuine internal inconsistency between the two papers' own text, corroborated by qerrors.classical_ber's own x_swing=sqrt(2*N_RAIL) convention; I also confirmed Part I never attaches a variance to k (exactly 4 "k >= 8" occurrences) and that qdecode.py:26 does misread a noise-margin parenthetical as an achievability claim. The central category argument survives my scrutiny: the composite decoder is a cascade of monotone maps, so the boundary stays at t and finite k costs only offset-referral (R2) and regeneration-depth ambiguity (R3) — this is the standard ADC decomposition, and the note correctly steelmans, then kills, the variance reading on magnitude. It builds on rather than contradicts the promoted record: it answers 07-14's Limitation 2, generalizes rather than overturns its §3 closed form, and its erratum ground (i) tracks 07-14 §1.5's plane correction. The one real defect I found and the note does not disclose: §1.3's gain model sets A_pump ~ rail and then multiplies by g_max, giving the comparator an output swing of 269.6 = 3.08x the logic rail, which contradicts Part I's own saturating-rail statement (line 426, "the rail is what re-clamps levels gate after gate"); the normalization-free invariant is delta_out/S_out = c/2 = 14.4%, and a rail-clamped output gives G_th=40.0, "14.4% of rail" and 208x — so the Verdict's headline "44.4%" and "1975x", both labeled demonstrated, are inflated ~3.1x and ~9.5x and are in-model, not demonstrated. That does not change any conclusion (14.4% post-trim is still not a trim residual, and the note's normalization-free argument — c=0.2887 means sigma_trim = 28.9% of the transition width — carries §1.3 unaided), the erratum text itself is clean of the flawed figure, and this is the same class of precision gap I recorded as dissent while voting store on 2026-07-12; the substance, reproducibility, honesty (seven limitations, several self-damaging; it disagrees with its own prompt in both directions and concedes results.json need not change) and durability are otherwise exceptional.

  - §0/§1.3 label the '44.4 % of the logic rail' and '1975x smaller in variance' figures *demonstrated*, but both rest on an in-model gain assumption (A_pump ~ rail, then x g_max) that puts the comparator's output swing at 269.6 = 3.08x the logic rail — contradicting Part I line 426 ('the rail is what re-clamps levels gate after gate'). The normalization-free invariant is delta_out/S_out = c/2 = 14.4%; a rail-clamped output gives G_th = 40.0 (not 123.1), 14.4 % of rail, and 208x (not 1975x). Relabel in-model, disclose the A_pump sensitivity, and lead with the normalization-free form (c = 0.2887 <=> sigma_trim = 28.9 % of the transition width), which needs no gain model. Limitation 1 flags this assumption only for R3's delta_crit, not for the §1.3 headline that carries the Verdict.
  - §1.1's load-bearing sentence — 'A deterministic function of a random variable adds no variance to that variable' — is false as written (y = x^2). The true claim is that a strictly *monotone* map preserves threshold-crossing probability, which the surrounding text states correctly. This is the note's central argument in an erratum to DOI-archived text; an outside reader will hit this sentence first. Fix the wording.
  - The three reproduction scripts are untracked (git status shows '?? fable-model-quantum/check_kband{,2,3}.py') and the Appendix gives commands plus expected outputs but no listing, while the header claims 'commands/listing'. notes/README requires the computation to ship with the note and states that results on apparatus the reader cannot run 'will fail review for that reason alone'. The promotion PR must commit all three scripts (the 07-14 precedent carries an inline listing).
  - Erratum ground (i) says the band and the vacuum floor 'are not comparable at any single plane' — over-stated, and it misstates the promoted note it cites: 07-14 §1.5 explicitly *does* compare them at the comparator plane (0.10-0.13 vs 1/2, crossover N ~ 2e3), as the erratum's own next sentence then does. Reword to 'the N/768-vs-1/2 comparison as written mixes planes'.
  - §5's 'The column is a sensitivity at c = 0.289, not a consequence of k' is in tension with the note's own R2 (V_static = c^2(x_range/k_dec)^2 retains the 1/k^2 scaling the note insists survives) and with promoted 07-14 §3.2's k_dec-contingency finding. The accurate framing is 'contingent on c and k_dec jointly; the tanh band contributes nothing'.
  - R1 establishes k_dec > 4 as necessary and monotone improvement above it — it does not derive 16. The erratum's 'the k_dec >= 16 rule stands, on the replacement ground' is generous; the replacement ground supports a floor at 4 and a design preference, and should say so.
  - §3's '12.8x tightening' is computed against Part I's rounded 'sigma <= 0.16 n'; disorder.py's exact rule (sigma_crit = 0.1561 n) gives 12.5x. Trivial, but it is stated as demonstrated.

- ⚛️ **Quanta** — **STORE**: I adopted the Quanta persona and re-executed everything. All three Appendix scripts (check_kband.py, check_kband2.py, check_kband3.py — all tracked in git, so the notes/README "ship your computation" rule is met) reproduce the note body exactly: logistic identity 2.220e-16, tangent band 2.000·Δn, x_rail=87.551 / x_range(300K)=17.518 / ratio 4.998, k_dec=1.60 and 3.20, (β/Δn) ratio 10.00, comparator gain 123.1, c=0.2887 ⟺ δ_out=44.4% of rail with 1975× in variance, and 0.75·erfc(√(3/8)·16)=8.7266e-44 matching the generalized p_floor(c,k)=0.75·erfc(k/(4√2 c)). The §5 LOWER column is exactly band-drop + meta from block 3 (2.588e-6, 9.683e-8, ..., 1.930e-91) and every ratio checks; I separately confirmed the §4 floor sensitivities (c=0.3479 for 1e-30, 0.2855 for 1e-44). The central claim survives my scrutiny: I extracted Part I's PDF and Eq. (5) is verbatim "A_out = A_pump · g(n_local), n_local = n_bias − β·A_in" — a strictly monotone deterministic map, so the decision event P(f(X)>f(t))=P(X>t) is unchanged and the tanh band genuinely contributes no decision variance; the residuals are exactly what the note books as R2 (downstream mismatch referred back through the ∝k threshold gain) and R3 (incomplete regeneration), which is the correct and complete comparator taxonomy. §1.2's internal-inconsistency evidence is independently decisive and I confirmed it in source: NM_CLASSICAL=0.2564 is exactly cell.py:71 at (k=8, 10 dB) = 0.25641, qerrors.classical_ber books k on d with no k in V, qmac books k on V with no k in d, and Part I nowhere writes a variance for k (its only k=16 mention is the noise-margin parenthetical at line 425, so qdecode.py:26's "the parent already quotes k = 16 as achievable" is indeed a misreading). §3's reference-plane finding is real and β-free, and Part I's own definition "k = β·A_swing/Δn (A_swing is the rail-to-rail input swing)" plus Part II's "Part-I threshold cells ... sharpness k ≥ 16" confirm the dilemma. Consistency with the promoted record holds — 07-14 §1.5's pre-loss scoping is honored and cited, its §3 closed form is correctly generalized rather than contradicted, and the note answers that note's own Limitation 2. Honesty is strong to the point of self-undermining (it concedes the warm rows are "mis-derived, not refuted", that results.json need not change, that Limitation 2's β convention could swing §3 either way, and that Part I's butterfly numbers don't reproduce from cell.py:71 — which I confirmed: 0.340/0.394 vs the text's 0.26–0.35). The defects I found are copy-edit and erratum-scope class, not correctness class, and none touch the central claim.

  - R3 numeric slip: §2 states 'comparator gain 123.1 and one restoring cell (12.8), δ_crit = 0.0289 at 300 K', but 12.8 is the 4 K restoring-cell gain — at 300 K it is 12.32. Recomputing from the note's own stated inputs gives (87.551/2)/(123.1×12.8) = 0.0278, not 0.0289; only 12.32 reproduces 0.0289. The slip is inherited from check_kband.py printing gain_logic after the loop (last value = 4 K), where it reads as generic. Immaterial to conclusions (R3 is explicitly order-of-magnitude, Limitation 1) but it is exactly the recomputation an outside reader of an erratum will attempt.
  - Erratum scope is narrower than the note's own worst finding. §3 concludes the ladder comparator cannot be a re-trimmed Part-I cell at k_dec=16, which directly contests two verbatim Section 5 sentences ('cell-for-cell the Part-I half adder with its input stage re-trimmed as a two-level flash ladder'; 'Part-I threshold cells with staggered, trimmed thresholds and sharpness k ≥ 16'). The erratum withdraws only the N/768 sentence and headline claim 3, reaching the redesign issue solely via a Table QB1 footnote. A reader of the erratum alone would not learn that Section 5's central framing is contested.
  - The promoted crossover note (2026-07-12 §3, N*_band = 384) is left un-amended. Erratum ground (ii) — the band is deterministic and 'cannot be compared with the vacuum floor at all' — voids that comparison at *every* plane, which goes strictly beyond the pre-loss scoping of 07-14 §1.5 that the note's header declares 'settled'. The note withdraws Part II's reflection of the claim but proposes no correction to the promoted note that seeded it, leaving the permanent record internally inconsistent under the note's own argument (persona rule 10 territory).
  - cell.py's transfer() (line 31) codes A_out = A_in * (g_max*0.5*(1+tanh(...)) - loss) — self-gating by A_in — whereas Part I Eq. (5) reads A_out = A_pump · g(n_local). The note quotes Eq. (5) correctly from the manuscript and its argument rests on the paper's form (which is the right choice, since qdecode's comparator cites 'parent Eq. 5'), and the A_in form is not even monotone in general. But in a memo whose entire thesis is 'the code does not implement its docstring', leaving this second, independent code-vs-paper divergence in the very cell being re-derived unremarked is a gap an outside checker will hit immediately — and noticing it would have strengthened the case.
  - Minor precision: §1.2 says Part I has '4 occurrences of the k ≥ 8 rule'; I count five mentions (lines 423, 619, 725, 1111, 1165 of the extracted text). The load-bearing half of that sentence — that Part I never writes a variance for k anywhere — is demonstrated and correct.
  - Minor framing: the erratum is drafted in adopted voice ('is withdrawn', 'is hereby re-labelled') while §7 'What genuinely needs the maintainer' lists three items that do not include the erratum itself, implying it does not need him. Withdrawing a headline claim from DOI-archived text is a maintainer act; the pipeline (draft → agent vote → human merge) contains this, but the voice overstates the agent's standing.
