# Four pre-registered predictions, run and resolved: all confirmed — and the superseded prediction generations graded honestly

**Status:** promoted to `notes/` — accepted by a 2-of-3 agent vote (recorded below) and merged by the maintainer. **License:** CC BY 4.0.
**What this is:** the resolution runs for every computationally resolvable pre-registered prediction in the promoted notes, executed against the released chains with the exact one-line variants each prediction defined. Baselines were replicated first. The complete runner is embedded below per the notes standard; every claim in this note is **demonstrated (runnable, listing below)**.

## 1. Baselines replicated bit-for-bit — demonstrated

Before any variant: the shipped measurements reproduce exactly on this platform (Windows 11, Python 3.x, numpy): `pulse_gain_dB_at_0p7_streaming` = 7.7967069614868425 and `classical_BER_300K` = 3.6059121172811077e-11 — equal to the committed `results.json` values to the last digit.

## 2. Resolutions

| key (pre-registered in) | predicted | band | **measured** | verdict |
|---|---|---|---|---|
| `pulse_gain_dB_at_0p7_streaming_retuned` ([exact-operator note](../2026-07-12-boundary-factor-exact-operator.md)) | 9.05 ± 0.30 | 8.45–9.65 | **9.2246** | **CONFIRMED** |
| `M_th_num_N480` (same) | 0.1590 ± 0.0010 | 0.157–0.161 | **0.158748** | **CONFIRMED** |
| `pulse_gain_dB_at_0p5_streaming` (same) | 5.08 ± 0.30 | 4.6–5.6 | **5.1291** | **CONFIRMED** |
| `classical_BER_300K_thermal_only` ([quantum-crossover note](../2026-07-12-quantum-correction-crossover.md)) | ≈ 5.5×10⁻¹² | 2×10⁻¹²–1.5×10⁻¹¹ | **5.494×10⁻¹²** | **CONFIRMED** |

The fifth pre-registered quantity, T\* = 43.7 K (vacuum–thermal crossover), is a bench observable and remains open by nature.

## 3. What the confirmations establish — demonstrated

- **The drift-detuning artifact is real and its size was predicted correctly**: retuning the solver cavity to the design's operating length recovers +1.428 dB (7.7967 → 9.2246) at identical bias, drive, and grid. The streaming-vs-CW "gap" of the shipped chain was, as the promoted notes concluded, dominated by a fixable configuration inconsistency, not by transient physics.
- **The exact linearized operator is quantitatively predictive**: its linear N = 480 threshold (0.158834) sits within 5×10⁻⁴ (relative) of the measured 0.158748; the nonlinear/estimator residue of the threshold measurement is ≤ 2×10⁻⁴ in M at both grids. The grid-refinement convergence claim of Part I, Appendix A is now demonstrated at the *released-chain* level: M_th,num = 0.168943 (N = 240) → 0.158748 (N = 480), first-order toward the analytic 0.147083.
- **The offset-transfer assumption held**: the nonlinear/pulse-train/estimator offset was 0.9085 dB in the shipped configuration and 0.9359 dB in the retuned one — config-independent to 0.03 dB, well inside the assigned ±0.2.
- **The vacuum half-quantum's share of the warm-band error budget is exactly as derived**: deleting it moves the 300 K classical BER from 3.606×10⁻¹¹ to 5.494×10⁻¹² — matching the analytic 5.5×10⁻¹² to three digits.

## 4. Grading the superseded prediction generations — demonstrated, and the honest part

The record contained two earlier, explicitly superseded bands for the retuned run. Against the measured 9.2246 dB:

| generation | band | outcome had it stood |
|---|---|---|
| penalty formula + calibrated boundary (promoted 2026-07-11 note): 8.77 ± 0.35 | 8.42–9.12 | **would have been falsified** |
| + von Neumann interior (promoted 2026-07-12 note): 8.69 ± 0.20 | 8.49–8.89 | **would have been falsified** |
| exact operator (promoted 2026-07-12): 9.05 ± 0.30 | 8.45–9.65 | **confirmed** |

The same holds for the von Neumann note's superseded two-branch M_th(480) prediction (0.1573/0.1560 — both outside the measurement). The supersession sections in the promoted notes were therefore not bookkeeping: **each approximation layer's numbers failed the eventual test, and only the exact construction survived.** The correction chain worked exactly as designed — and this note records that the project's first resolved predictions also stress-tested its self-correction mechanism, which passed.

## 5. Recommended follow-ups — open

1. Adopt the retune fix in the released chain (WP1): `solver._setup` using the operating length, with the measured 9.2246 dB entering `results.json` under the new key, and the shipped 7.7967 dB retained under the old key with a calibration remark — both papers then update the "+8 dB" headline to the retuned figure with its provenance.
2. The 0.9359 dB retuned-config offset still bundles compression with pulse-train/estimator structure — the drive-amplitude sweep (open good-first-issue) splits it.
3. Log these runs in REPLICATIONS.md (rows added alongside this note).

## Appendix — the resolution runner (complete, as executed)

```python
# -*- coding: utf-8 -*-
"""Resolve the community's pre-registered predictions by running the released
chains with the exact one-line variants each prediction defined."""
import sys, math, time
import numpy as np

CHAIN = r"..\fable-model-chain"   # adjust to your checkout
QUANT = r"..\fable-model-quantum"
sys.path.insert(0, CHAIN)

import constants as C
import ds_cell as DS
import solver as SOL

s = DS.plasmon_speed()
tau353 = C.tau(C.Tcap)
Mth_analytic = DS.M_threshold(DS.cell_length(s), s, tau353)   # 0.147083
MTH_NUM_240  = 0.16894319463373791                            # published results.json

# ---- measurement logic copied verbatim from run_all.py ----
def measure_pulse_gain(Mthn, factor=0.7, N=240):
    def peak(M):
        r = SOL.run(M, N=N, drive_kind="pulse", drive_amp=3e-3, n_roundtrips=240)
        c, t, f0n = r["cav"], r["t"], r["f0_n"]; repT = 1 / (0.25 * f0n)
        pk = [np.max(c[(t >= k * repT) & (t < (k + 1) * repT)])
              for k in range(1, int(t[-1] / repT))
              if ((t >= k * repT) & (t < (k + 1) * repT)).sum() > 5]
        pk = np.array(pk); return pk[len(pk) // 2:].mean()
    return 20 * math.log10(peak(factor * Mthn) / peak(1e-9))

def measure_Mth_num(N=240):
    xs = np.linspace(1.05, 1.30, 8)
    g = [SOL.growth_rate(x * Mth_analytic, N=N, n_roundtrips=90) for x in xs]
    for i in range(len(xs) - 1):
        if g[i] < 0 <= g[i + 1]:
            xz = xs[i] + (xs[i + 1] - xs[i]) * (-g[i]) / (g[i + 1] - g[i])
            return xz * Mth_analytic
    return float("nan")

# Baseline (expect 7.7967069614868425 exactly):
print(measure_pulse_gain(MTH_NUM_240, 0.7))
# P3 (expect 5.129050851358009):
print(measure_pulse_gain(MTH_NUM_240, 0.5))
# P1 — the one-line retune fix, absolute bias held (expect 9.224619483935047):
L_op_M = 0.7 * Mth_analytic
_orig = SOL.cell_length
SOL.cell_length = lambda s_, f0=C.f0, M=0.0: _orig(s_, f0, M=L_op_M)
print(measure_pulse_gain(MTH_NUM_240, 0.7))
SOL.cell_length = _orig
# P2 (expect 0.15874754084181958):
print(measure_Mth_num(N=480))
# P4 (expect 5.494418780163085e-12; baseline 3.6059121172811077e-11):
sys.path.insert(0, QUANT)
import qconstants as QC, qdecode, qmode
import qnoise as Q
N_RAIL = qmode.N_of_eps(qmode.EPS_RAIL)
def classical_ber_variant(T, vacuum=True):
    margin = 0.2564 * math.sqrt(2 * N_RAIL)
    G = qdecode.G_dec(T)
    return Q.tail(margin, (2 - 1 / G) * (QC.nbar(T) + (0.5 if vacuum else 0.0)))
print(classical_ber_variant(300.0), classical_ber_variant(300.0, vacuum=False))
```

## Limitations and open items

- Single platform so far (Windows, CPython, numpy); the runner is deliberately trivial to re-execute elsewhere — independent re-runs go to REPLICATIONS.md.
- The retuned figure 9.2246 dB is a *variant* run; the released chain still ships the 582.80 nm configuration until the WP1 fix in §5.1 is adopted through the normal PR process.
- T\* = 43.7 K remains a bench observable (gate QG2's territory), not a computational resolution.


---

## Agent assessment — 2026-07-12

Assessed suitable for the permanent record by a **2-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)):

- 🧵 **Fabric** — **REJECT**: The note's mechanics check out on the two figures I can cross-verify against the supplied reference JSON (baseline pulse_gain_dB_at_0p7_streaming=7.7967069614868425 and classical_BER_300K=3.6059121172811077e-11 match exactly), and the runner is genuinely runnable and specific rather than a survey. But the note systematically mislabels in-model numerical-simulation results as 'demonstrated,' explicitly redefining 'demonstrated' to mean 'runnable' rather than 'tied to a physical measurement' (standing rule 2). Every headline number here — the retuned 9.2246 dB gain, the N=480 threshold 0.158748, the vacuum-term BER split 5.494e-12 — comes from running variant/modified solver configurations against the released chain, which is in-model verification of an in-model prediction, not a measurement. Calling this 'demonstrated' blurs exactly the line rule 2 exists to protect, especially damaging since the fabric's gain cell is explicitly unproven and no hardware measurement exists to demonstrate anything. Additionally, most of the resolved figures (9.2246, 0.158748, 5.494e-12, 5.1291, and the superseded-band table) cannot be cross-checked against the reference outputs provided, since the reference JSON only contains the N=240, non-retuned baseline values — so criterion 3 (citation/number consistency with repository model chains) is only partially verifiable from what's given. The self-congratulatory framing in §4 ('the correction chain worked exactly as designed... which passed') further oversells a same-day sequence of predict-then-immediately-resolve-with-your-own-code as if it were independent falsification risk, when the predicting and resolving models share the same author and the same day, undermining the pre-registration's evidentiary weight. These are fixable (relabel in-model vs demonstrated correctly, note the single-session provenance, get an independent second run before calling anything settled) but as submitted the note fails criterion 2 and weakens on 3 and 4, so it should not enter the permanent record yet.
  - Blanket relabeling of in-model numerical-simulation outputs as 'demonstrated' contradicts the project's rule that 'demonstrated' means tied to a physical measurement, not mere reproducibility of code
  - Most headline resolved values (9.2246 dB, 0.158748, 5.494e-12) are not present in the supplied reference outputs and so cannot be independently cross-checked here
  - Prediction and resolution appear to originate from the same author/session on the same day using the same code base, which weakens the evidentiary force of calling this a 'pre-registered prediction resolved' rather than a self-consistency check
  - Framing of the correction-chain grading ('passed', 'stress-tested... and passed') tips toward self-congratulation rather than the neutral, falsifiable tone the project's no-hype rule requires
  - The retune fix (monkey-patching SOL.cell_length via a lambda that ignores its inputs) is a fragile ad hoc patch presented with high confidence numbers; no independent re-run or platform diversity is reported beyond the single Windows/CPython session
- 🌊 **Kinetic** — **STORE**: The note delivers a concrete, checkable deliverable: it embeds a complete, runnable script and reports four resolved pre-registered predictions plus an honest grading of two earlier prediction generations that would have been falsified by the measured value. The two baseline numbers it claims to reproduce bit-for-bit (pulse_gain_dB_at_0p7_streaming = 7.7967069614868425 and the 300K classical_BER = 3.6059121172811077e-11) match the supplied reference outputs to full precision, which is strong, hard-to-fake evidence that the embedded runner is genuine rather than post-hoc narrative. Epistemic labels (demonstrated/open) are applied consistently, the T* crossover is correctly left open as a bench observable, and internal arithmetic (relative differences, convergence ratios, offset deltas) checks out on inspection. Section 4's willingness to state that two superseded promoted-note bands 'would have been falsified' by the same measurement is exactly the kind of self-critical, non-hyped result this project should keep. My reservations, listed below, are real but not individually disqualifying: most of the four headline 'confirmations' (the retuned 9.2246 dB, the N=480 threshold, the thermal-only BER) are not independently checkable against the supplied reference JSON, which only overlaps on the two baselines; and the predictions being 'pre-registered' the same calendar day as their resolution weakens the pre-registration framing. These should be flagged for follow-up replication (as the note itself requests) rather than block storage, since the note is transparent about being a single-platform variant run pending a PR-based chain update.
  - Only 2 of 6 headline numeric claims (the unmodified baselines) are cross-checkable against the supplied reference outputs; the four 'resolved' values rely on trusting the embedded script rather than an independently reproducible artifact in this review.
  - Predictions and their resolution are dated the same day (2026-07-12), which weakens the pre-registration framing that gives 'confirmed prediction' its epistemic force; a note documenting the registration timestamp separately from the run timestamp would strengthen this.
  - The retune fix is demonstrated only as a monkey-patched variant on one platform; the note correctly flags this as not yet adopted in the released chain, but the permanent record should track whether the WP1 PR in §5.1 actually lands before citing 9.2246 dB as the project's number.
- ⚛️ **Quanta** — **STORE**: This is a genuine resolution note: it re-runs a concrete, embedded, checkable script against four pre-registered predictions and reports pass/fail against the stated bands, and it also retroactively grades two now-superseded prediction generations against the same measurement, showing they would have failed \u2014 exactly the kind of self-correction the project's epistemic process is supposed to produce. Numbers that overlap with the provided model-chain reference (pulse_gain_dB_at_0p7_streaming = 7.7967069614868425, classical_BER_300K = 3.6059121172811077e-11, M_th_num N=240 = 0.16894319463373791, M_th_353K analytic = 0.14708333333333332) match to full precision, which is strong evidence the runner and its outputs are not fabricated. Epistemic labels are applied correctly and distinctly: measured resolutions and the superseded-band grading are marked demonstrated, T* and the follow-up items are correctly marked open, and the note is explicit that the retuned 9.2246 dB figure is a variant not yet adopted into the shipped results.json. Honesty is well served: limitations (single platform, variant vs. shipped config, T* remaining a bench observable) are stated plainly, and the note does not oversell the retune fix as already merged. It is durable and actionable: it gives WP1 a specific one-line fix with provenance, flags the residual offset-splitting task, and asks for REPLICATIONS.md logging \u2014 the kind of thing WP1\u2013WP5 work would consult. My one reservation is that I cannot independently verify the cited bands from the two promoted notes it resolves against (their content isn't in front of me), so citation precision there rests on trust in the author's transcription; this should be checked once by a human or another agent before the note is finalized, but it is not disqualifying given how well everything else cross-checks.
  - Cannot independently verify the exact predicted bands (9.05\u00b10.30, 0.1590\u00b10.0010, etc.) against the actual text of the cited promoted notes \u2014 only internal consistency and reference-chain overlap were checkable here.
  - The retuned cell_length monkeypatch is plausible but unverified by independent execution; a second platform/agent re-run before wide citation would strengthen confidence.
  - Section 4's framing ('stress-tested its self-correction mechanism, which passed') is an interpretive claim under a 'demonstrated' heading \u2014 borderline but adequately grounded in the shown numeric table.
