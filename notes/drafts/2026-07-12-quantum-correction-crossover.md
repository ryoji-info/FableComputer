# Where the quantum chain is classical and where it is not: no 1/N correction to the noise figure, an exact T\* = ħω₀/(k_B ln 3), and the one N-crossover the code actually contains

**Status:** draft (notes pipeline). **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #15](https://github.com/ryoji-info/FableComputer/discussions/15) (Quanta's winning prompt). The API session's reply (published there) reached the right verdict from attachments alone; this note re-derives it **from the released source** (no guessed code behavior anywhere — every formula below is read from `qnoise.py`, `qdecode.py`, `qmac.py`, `qerrors.py`), sharpens the crossover to closed form, and answers the 1/N question with a proof rather than an estimate.
**Method:** symbolic derivation plus standalone calculator evaluation; no repo code executed. **Labels:** demonstrated / in-model / open per [notes/README.md](../README.md), including its pre-registered-prediction naming rule.

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
