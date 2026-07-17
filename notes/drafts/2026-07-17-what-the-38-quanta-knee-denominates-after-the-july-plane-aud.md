---
title: What the 38-quanta knee denominates after the July plane audit: a launch-plane band N ∈ [22.3, 50.6], an untenable intracavity reading, and a survival map for Part II's quantum-side imports
author: Quanta ⚛️ (AI research agent, Fable Computer project)
date: 2026-07-17
status: draft — pending agent review (2-of-3) and human merge
license: CC BY 4.0
---

## 0. One question

After `notes/2026-07-17-drive-sweep-knee-anchored.md`, what does Part II's "38-quanta knee" actually denominate — and which of the quantum-side numbers that import it survive? This weekly note compiles the answer from the four promoted notes of 2026-07-14 through 07-17 and the two released `results.json` files (both re-executed this week and reproducing). No new solver runs were made; every new number here is arithmetic on cited keys, shipped in the Appendix.

**Verdict.** The knee is a **launch/drive-plane** quantity. Input-referred, its measured band is **N_knee ∈ [22.3, 50.6] quanta** (CW/pulse observables), bracketing the published 38.3 (drive brackets demonstrated; the quanta conversion in-model). The intracavity reading — the one Part II's quantization language and three source-code labels use — is **untenable**: the measured intracavity knee converts to 7,248–8,975 quanta, *above* the rail's own N_rail = 3,833. Everything downstream that imports the knee survives input-referred; what does not survive is wording, in three specific places.

## 1. The record before this week — in-model, calibration open

`notes/2026-07-13-knee-rail-not-derivable-from-noise-chain.md` established that the ladder is quantization bookkeeping, not noise-chain physics: N(ε) = (ε/ε₁)² with ε₁ = 1.6153×10⁻³ (`fable-model-quantum/results.json:eps_one`), applied to two classical Part-I solver amplitudes hardcoded at `qmode.py:44–45` (`EPS_KNEE = 0.01`, `EPS_RAIL = 0.10`), giving `N_knee` = 38.326 and `N_rail` = 3,832.6 (results.json keys). Eq. (Q1)'s absolute calibration was and remains **open** (that note, §2). What nobody had checked until 07-17 was *which plane* the 1 % lived on.

## 2. What 07-17 measured, and what the conversion adds

Demonstrated (runnable, `notes/2026-07-17` §5 and Appendix; N = 240, single grid): the released solver's 1-dB compression knee sits at **source-drive amplitude 1.15×10⁻² (pulse observable) / 7.6×10⁻³ (CW)** — A_SAT_eff ∈ [0.0150, 0.0226], the shipped `A_SAT = 0.02` (`fable-model-chain/cell.py:34`) inside the band. The knee drives are log-log interpolations between bracketing runs; the brackets are the demonstrated fact (07-17 assessment record, Kinetic's finding). The measured intracavity |δu| swing at the knee is **0.153 (pulse) / 0.138 (CW)** — the linear intracavity-to-drive enhancement (×14.9 pulse / ×20.2 CW, 07-17 §5) *is* the plane conversion, and it is why the two readings of "the 1 % knee" differ by an order of magnitude.

In-model (two named steps, both from the corrected record): converting swings to quanta uses Eq. (Q1–Q2) plus the O(M) ≈ 12 % δu↔δn equivalence (07-17 Limitation 3), on top of the open Q1 calibration. With that labeling:

- **Input-referred:** N = (1.1487×10⁻²/ε₁)² = **50.6** (pulse), (7.6336×10⁻³/ε₁)² = **22.3** (CW). The published 38.3 sits inside the band; its *scale* is now anchored by a run, which it never was before.
- **Intracavity:** N = **8,975 (pulse) / 7,248 (CW)** — 189–234× the published value and above N_rail. A "knee" above its own "rail" is not a coherent mesoscopic ladder; the intracavity reading is dead (07-17 §5).
- **Energy:** `pulse_energy_knee_aJ` = 0.0254 becomes a band **0.0148–0.0335 aJ** (N × 6.626×10⁻⁴ aJ/quantum, from the published key pair).

## 3. The survival map — every quantum-side import of the ladder

| quantity (source) | plane it assumes | after 07-17 | label |
|---|---|---|---|
| `EPS_KNEE`/`EPS_RAIL` (`qmode.py:44–45`) | quantizes Q1's intracavity mode amplitude; values come from the drive plane | values survive as launch-plane amplitudes; relabel offered, maintainer's call | demonstrated (source) |
| `N_knee` = 38.326 (results.json) | — | survives; measured input band [22.3, 50.6] | in-model conversion of demonstrated brackets |
| `pulse_energy_knee_aJ` = 0.0254 | — | band 0.0148–0.0335 aJ | in-model |
| preamp no-go (`preamp_variant_2bit_300K` = 0.495) | window "ends at the knee" | **survives** input-referred: window N ∈ [22, 51]; the no-pay conclusion is unchanged | demonstrated (key untouched) + in-model band |
| 07-16 census, B′ attenuation arm (η = N_knee/(G·N_top), G·N_top = 1454.4 at 300 K) | knee as sampler linear limit | 233.5 → **173.9 (pulse) / 401.7 (CW)** quadrature units of loss noise, vs V_amp = 5.60 — ruinous under any anchoring; the exclusion is robust | demonstrated arithmetic in an in-model census |
| 07-16 census, B compression arm | model form at A_SAT = 0.02 (gap ratio 0.581) | measured **0.661** on the pulse observable (07-17 assessment record, my re-execution); the CW observable would *harden* it to ~0.55. B still dies on the B′/quiet-threshold arms either way | demonstrated (recorded re-execution); observable split open |
| qubit no-go anchor (`chi_over_kappa_4K` = 8.2×10⁻⁶) | none — χ/κ + geometry, per 07-13 §4 | untouched; the no-go never rested on the ladder | demonstrated (key) |
| `error_table`, `q2bit_avg16`, `F_dec_300K_dB` | quadrature units; the *knee* enters none of them | untouched by the knee relabel (the avg16 column's own problems are 07-16's, orthogonal) — but `classical_BER` imports the *rail* via x_swing = √(2·N_RAIL) (`qerrors.py:53,58`); see §4 | demonstrated (source) |

**The three mislabels (demonstrated, source grep this week):** `qmac.py:24` ("~38 **intracavity** quanta"), `qmac.py:65` (`compression_gain` docstring: "1 dB at ~1% **intracavity** swing"), and — not previously recorded — `make_manuscript.py:298–299`, which prints the knee as "N ≈ 38 quanta (0.025 aJ **intracavity**)" into the Part II text itself. All three label a launch-plane quantity intracavity. Relabels are offered, not asserted, per the 07-16/07-17 precedent; no `results.json` value changes.

## 4. The rail is now the weaker anchor

An asymmetry the week's arc exposes but did not headline: ε_knee is now anchored at the drive plane; **ε_rail = 0.10 is anchored at neither plane.** Its intracavity reading is contradicted by measurement — at 10.05 % measured intracavity swing the compression is −0.35 dB, not the model's −14.15 dB (`compression_10pct_dB`; 07-17 §5 and assessment record) — and its drive-plane reading sits beyond the sweep's 5×10⁻² maximum, in the regime where the saturation form already rolls off at ≈−10 dB/decade instead of −20 (07-17 §0, verdict 5). This matters beyond bookkeeping: `qerrors.py:53,58` builds the classical margin from `N_RAIL` (x_swing = √(2·N_rail) = 87.55, the swing 07-15 §3 uses), so the rail is load-bearing for classical-margin bookkeeping in the quantum package. Open; the natural next run is extending the drive sweep to 10⁻¹ at N = 240 and 480.

## 5. The week in one sentence

Four notes, one lesson, four planes: the static band is one term metered at two loss planes (07-14 §1.5); a mismatch fraction means nothing until input or output plane is named (07-15, both post-promotion corrections); the avg16 bookkeeping is exact only at a combiner plane the fabric cannot build (07-16); and the knee is a drive-plane number wearing an intracavity label (07-17). Every gain, variance, mismatch, or quanta figure in this project now needs its reference plane stated at first use — the cheapest discipline the record has, and the one this week shows failing most expensively.

## Limitations and open items

1. **Single grid, single platform.** All knee/swing numbers are N = 240 statements (07-17 Limitation 1); the N = 480 sweep is deferred and could move the anchors.
2. **The quanta conversions are in-model twice over**: O(M) ≈ 12 % δu↔δn equivalence (h-field estimator variant unrun) and Eq. (Q1)'s absolute calibration, open since 07-13. Only the drive brackets and |δu| swings are measured. "38 quanta" remains bookkeeping until WP2 certifies the calibration — this note moves its plane, not its ontological status.
3. **The 0.661 gap ratio is a pulse-observable number**; the CW observable hardens it (~0.55). The census's topology-B row still fails the name-your-observable rule until someone runs both; its conclusion does not depend on the split.
4. **§4's rail claim is one-sided**: the drive-plane rail is *unmeasured*, not falsified; only the intracavity reading is contradicted.
5. **No new runs.** Every number here is a cited key, a promoted note's text, or Appendix arithmetic. Where the 07-17 reviewers corrected wording (the 0.661 ratio; conversion in-model, not measured), the corrected version is carried.
6. Whether Part II's *prose* needs an erratum beyond the three source relabels is the maintainer's judgment; the manuscript-generator instance (§3) suggests at least one sentence does.

## Appendix — the arithmetic (runnable, repo root)

```python
import json, math
Q = json.load(open("fable-model-quantum/results.json", encoding="utf-8"))
e1 = Q["eps_one"]                                  # 1.6153004210548913e-3
for tag, eps in (("input pulse", 1.1487e-2), ("input CW", 7.6336e-3),
                 ("intracav pulse", 0.15303), ("intracav CW", 0.13752)):
    print(tag, round((eps / e1) ** 2, 1))          # 50.6 / 22.3 / 8975.2 / 7248.1
Eq = Q["pulse_energy_knee_aJ"] / Q["N_knee"]       # 6.626e-4 aJ per quantum
print(round(22.3 * Eq, 4), round(50.6 * Eq, 4))    # 0.0148 / 0.0335
nb = Q["nbar_300K"] + 0.5
print(round((10 ** (Q["F_dec_300K_dB"] / 10) - 1) * nb, 2))   # V_amp = 5.6
for Nk in (38.0, (1.1487e-2 / e1) ** 2, (7.6336e-3 / e1) ** 2):
    eta = Nk / 1454.4                              # census B' arm, 07-16 listing convention
    print(round(Nk, 1), round((1 - eta) * nb / eta, 1))   # 38.0 233.5 / 50.6 173.9 / 22.3 401.7
```

Drive amplitudes and |δu| swings are the 07-17 note's Appendix outputs; `A_SAT_eff` = knee/√(10^0.1−1); the rail-point compression (−0.35 dB at 10.05 % swing) is from that note's §5 and its recorded assessment re-execution.

— Quanta ⚛️ (AI research agent · see [agents/README.md](../agents/README.md))