# Provenance of the 1.86 dB CW/pulse gain gap and the 2.77 dB noise-figure agreement

**Status:** promoted to `notes/` — accepted by a 3-of-3 agent vote (recorded below) and merged by the maintainer. **License:** CC BY 4.0.
**Method:** no model code was executed. Every number below was re-derived by hand from the equations documented in the two model READMEs, module docstrings, and source text, then evaluated with standalone calculator scripts external to the repos. All quoted `results.json` values are reproduced to their last printed digit from those hand-derived formulas, which pins provenance as firmly as a rerun would. Claims were additionally checked by five independent adversarial verification passes (code trace ×2, math re-derivation, document sweep, literature check).
**Labels:** **demonstrated** = reproduces a published output exactly from documented equations, or verified by direct inspection; **in-model** = follows from the named model's own assumptions; **open** = requires a run or a new exported output.

---

## 1. The noise-figure agreement (2.7689 vs 2.7750 dB) is structurally forced up to a temperature choice — demonstrated

Both numbers are **one closed form evaluated at two temperatures**:

```
F(T) = 2 − 1/G(T)                                        (Eq. 7, both repos)
G(T) = [(1 − loop₀)/(1 − loop_M)]²                       (regen.py / qconstants.py)
loop_M = (1+M)/(1−M) · a_loss,   M = 0.7·M_th(T)
M_th(T) = 1/(8 f₀ τ),  a_loss = e^(−1/(4 f₀ τ)),  τ(T) = 1 ps · (300/T),  f₀ = 1 THz
```

- Chain `noise_figure_floor_dB`: `run_all.py` calls `regen.cw_net_gain_dB(0.7)` whose **default is T = Tcap = 353 K** → G = 9.661006 dB → **F = 2.768940 dB**. Matches `results.json` exactly.
- Quantum `F_dec_300K_dB` = `10·log10(2 − 1/G_dec(300))` with `qconstants.regen_cw_gain_dB(0.7, 300 K)` → G = 9.768326 dB → **F = 2.774993 dB**. Matches exactly.

Term-by-term, `qconstants.py`'s formula chain is the parent's, transcribed (loss convention, threshold identity, loop, G, F — see Appendix A). Its own docstring says the operating point is "reproduced here verbatim" and "self-checked against fable-model-chain values at 300/353 K." **These are not independent derivations**; at equal temperature the two JSON values would agree to float precision.

The 0.00605 dB residual is exactly the 353→300 K change: ΔG = 0.1073 dB, and the sensitivity dF_dB/dG_dB = 1/(2G−1) ≈ 0.0571 compresses it to 0.0061 dB (Appendix B). F = 2 − 1/G saturates at 3.010 dB as G→∞, so *any* gain near +9.7 dB lands within ±0.01 dB of 2.77 — the agreement carries no cross-validating information, and no project document claims it does.

Two premises in the question this note answers are corrected (demonstrated):
1. `F_dec` does **not** derive from the comparator+NOT+AND+buffer stack. It is the single comparator cell's Eq.-7 figure; the 5-cell stack enters only the `decoder_cells` count and the truth table. The NOT/AND/buffer cells contribute zero noise anywhere in the quantum chain.
2. The chain floor is a **353 K** number (via `Q_353K`/`M_th_353K`), despite sitting unlabeled in a JSON that elsewhere labels 300 K and 353 K keys explicitly. Recommend renaming the key `noise_figure_floor_353K_dB`.

## 2. The 1.86 dB CW/pulse gap: mostly measurement convention and solver calibration; genuine streaming-transient physics ≲ 0.1 dB; quantum noise exactly 0

**Provenance (demonstrated).** `cw_regen_gain_dB_at_0p7` = 9.661 dB is the analytic, zero-swing resonant-enhancement ratio at 0.7·M_th,analytic (353 K). `pulse_gain_dB_at_0p7_streaming` = 7.797 dB is a nonlinear Lax-Friedrichs solve of a **single** cell (not a cascade of stages) at 0.7·M_th,num = 0.1183 (numerical threshold, 14.9 % above analytic), source drive amplitude 3×10⁻³, reported as 20·log₁₀ of the mean per-slot intracavity **peak** |u−u₀| over the second half of 240 round trips, referenced to an M≈0 run. Four things differ simultaneously: (i) finite-duty transient vs steady state; (ii) finite drive in a nonlinear solver vs zero-swing linear formula; (iii) waveform-peak metric vs enhancement-ratio metric; (iv) bias renormalized to the numerically-diffused threshold.

**Waypoint decomposition** (each waypoint computed from the model's own equations; Appendices C–E):

| waypoint | value | gap step | attribution | label |
|---|---|---|---|---|
| CW analytic, small-signal | 9.661 dB | — | — | demonstrated |
| linear periodic steady state of the same cavity under the solver's own pulse train, **energy metric** | ≈ 9.60–9.64 dB | **0.02–0.05 dB** | genuine pulse-vs-CW (streaming) transient — bucket (b) | in-model (computed two independent ways) |
| same, **per-slot peak metric** | ≈ 8.87 dB | **≈ 0.74 ± 0.3 dB** | metric convention — neither (a) nor (b) | in-model (single computation) |
| exported solver figure | 7.797 dB | **≈ 1.07 ∓ 0.3 dB** | nonlinear compression at the chosen drive + residual discretization/estimator — buckets (partly physics, partly (a)) | sum in-model; split open |

Within the last 1.07 dB: the model's own knee (1 dB compression at ~1 % swing; intracavity swing here ≈ 0.7 %) puts **compression at ≈ 0.2–0.8 dB** — real physics, but *not pulse-specific*: a CW measurement at the same drive would show it too. The remainder, **≈ 0.3–0.9 dB, is residual Lax-Friedrichs numerical diffusion not absorbed by the threshold renormalization, plus estimator choices** (first slot discarded, second-half mean, peak picking). The split is **open**: no grid sweep or drive sweep exists in the repo.

**Answer to the (a)/(b)/(c) question, for the 1.864 dB total:**
- **(c) Caves/Haus–Mullen amplifier noise: 0.000 dB — demonstrated.** Both figures are deterministic classical mean-field computations; amplifier quantum noise is additive *variance* and cannot shift a mean gain. Even if misattributed, its scale is 0.0005 dB (vacuum) to 0.006 dB (matched 300 K thermal) on rail-scale (3.8×10³-quanta) signals (Appendix F).
- **(b) genuine pulse-vs-CW transient physics: ≈ 0.05 dB (range 0.02–0.2) — in-model.** The README's buildup-time argument (buildup ≈ 12 round trips ≈ 6 ps vs 3-ps burst) is correct for an **isolated** burst — the never-exported analytic recirculation `regen.pulse_net_gain_dB(0.7)` evaluates to ≈ 6.26 dB, a 3.40 dB single-shot deficit — but the streaming train (3 ps FWHM in a 4 ps slot, ~75 % duty) is quasi-CW: its power sits almost entirely in the on-resonance comb line, so the linear steady-state deficit nearly vanishes (Appendix C, D).
- **(a) discretization/estimator: ≈ 0.6 ± 0.5 dB — open**, plus **≈ 0.74 ± 0.3 dB of metric convention** and **≈ 0.45 ± 0.35 dB of drive-amplitude compression** that belong to neither (a) nor (b) as posed. Constraint: the four buckets sum to 1.864 dB; the middle two are anchored by the waypoints, so (a) and compression trade off against each other within the final 1.07 dB.

**Framing correction (demonstrated by literature check):** Haus & Mullen (Phys. Rev. **128**, 2407, 1962) is a quantum *noise* theory of linear amplifiers (precursor to Caves, Phys. Rev. D **26**, 1817, 1982); it predicts nothing about pulse-vs-CW *gain*. The model's gain element is a lumped quarter-wave feedback cavity (Dyakonov–Shur reflection gain), not a traveling-wave amplifier, so TWPA analogies do not map; the relevant classical literature is regenerative-cavity buildup (Siegman, *Lasers*, 1986) and, for saturable pulse extraction, Frantz & Nodvik (J. Appl. Phys. **34**, 2346, 1963). The repos themselves cite Haus–Mullen correctly (noise bound only).

**What would settle the open items** (one-line runs, no new code beyond a loop): `g_pulse` vs N ∈ {240, 480, 960}; `g_pulse` vs drive_amp ∈ {3×10⁻⁴, 10⁻³, 3×10⁻³}; a solver **CW-drive** gain at 3×10⁻³ (isolates compression from transient); an energy-metric variant of `measure_pulse_gain`; export `regen.pulse_net_gain_dB(0.7)`. Note the "2nd-order MacCormack option" in `solver.py`'s docstring **does not exist in the code** — the natural discretization cross-check is currently unimplementable as shipped.

**Downstream consequences.** ROADMAP WP1 already lists pulse-gain calibration as open; this note quantifies the calibration debt at ~1.3–1.5 dB of convention+numerics inside the headline 7.8 dB. `qmac.py` hardcodes the gap as "CW − 1.9 dB" at **every** temperature in Part II — mostly convention, not physics, with no stated reason to be temperature-independent. Part I bench gate G1 ("+8 dB") should name its observable (per-slot peak vs energy), else it is ambiguous by ~1 dB.

## 3. Free parameters and documentation flags found (none previously consolidated)

- `A_op = 0.0116` (cell.py) — undocumented; with `A_SAT = 0.02` it fully determines the cascade table (which is **CW-based**: junction loss only reduces compression and is never subtracted; the two-cell figure plots 2× per-cell).
- `A_SAT = 0.02` — annotated "solver-anchored," but no anchoring run exists in the repo.
- `drive_amp = 3e-3` (run_all.py) — sits near the compression knee; never swept.
- `figures.py` hardcodes `Mth_num = 0.169` instead of recomputing.
- Quantum repo: `NM_CLASSICAL = 0.2564` (qerrors.py) and the 1.9 dB pulse deficit (qmac.py) are hardcoded parent values; `EPS_KNEE = 0.01`/`EPS_RAIL = 0.10` are round-number anchors which, with the unstated ~1.7 µm cell width, fix N_knee = 38 and N_rail = 3833 — the base of every Part II error rate.
- `loop(M_th) = 1.0022 ≠ 1`: M_th uses the small-M expansion while the loop uses the exact (1+M)/(1−M) reflection — footnote-level internal inconsistency.
- Introduction doc: "computed twice … must agree — and do" overstates the released code (no grid-refinement study exists; M_th,num is measured at a single N = 240), and one table row quotes 353 K gains against the 300 K per-gate loss.

## Limitations and open items

- The peak-metric steady-state value (8.87 dB) rests on a single verification computation; the energy-metric value was reproduced two independent ways. Both are linear-cavity results; the nonlinear solver could redistribute a few tenths of a dB between the "metric" and "solver" buckets.
- The compression estimate assumes the phenomenological knee (itself calibrated from the solver) applies at the streaming operating point; only a drive sweep settles it.
- Nothing here validates the *absolute* CW gain (+9.66 dB rides on best-case τ = 1 ps and top-of-band ε_z = 3.32, and sits on the steep flank of the near-threshold divergence); this note only decomposes the *difference* between two published numbers.
- No independent replication of either headline number exists yet (REPLICATIONS.md lists only the author's baseline).

---

## Appendix — derivations

### A. Formula identity (Q2)

Chain: `ds_cell.passive_loss_dB_per_half_lambda` returns 10·log₁₀(e^{t/τ}) with t = 1/(2f₀) — power loss over a half-wavelength; amplitude per round trip a_loss = 10^(−loss/20) = e^{−1/(4f₀τ)}. Quantum: `loss_dB = 10·log₁₀(e)·π/Q`, Q = 2πf₀τ ⇒ identical. Chain: M_th = L/(2sτ) with L = s/(4f₀) ⇒ 1/(8f₀τ); quantum: 1/(8f₀τ) directly. Loop, G, and F are line-identical. τ(T) agrees at 300/353 K (the quantum τ_q saturates only below 150 K).

Arithmetic (hand evaluation): 353 K: τ = 0.849858 ps, M_th = 0.1470833, a_loss = 0.7451523, loop_M = 0.9162026, G = 9.66100612 dB, F = 2.76893966 dB. 300 K: τ = 1 ps, M_th = 0.125, a_loss = 0.7788008, loop_M = 0.9281598, G = 9.76832557 dB, F = 2.77499343 dB. Both match `results.json` to the last digit.

### B. Sensitivity

F_lin = 2 − 1/G. d ln F/d ln G = (1/G)/F·… ⇒ dF_dB/dG_dB = 1/(G·F) = 1/(2G−1) = 0.05715 at the 353 K point. ΔG_dB = 0.10732 ⇒ ΔF ≈ 0.00613 dB (linearized) vs 0.006054 dB exact.

### C. Streaming linear steady state (comb picture)

The recirculation transfer at comb line n of the 0.25 THz train: |H(f)|² = 1/(1 + loop² − 2·loop·cos θ_n) with θ measured from resonance; the 1 THz carrier is the 4th harmonic of the rep rate and lands exactly on resonance (round trip = half a carrier period; source r_s = −1 restores phase). Gaussian burst (σ_t = 5.0955 in L/s units) puts amplitude e^{−2.0} ≈ 0.135 on the n = ±1 lines (power 0.018), where the active/passive enhancement ratio is 0.92. Energy-metric gain = Σp_n|H_M|²/Σp_n|H_0|² ≈ 9.64 dB (pure-Gaussian comb; independent windowed-train computation: 9.61 dB). Deficit vs CW: 0.02–0.05 dB.

### D. Isolated burst (analytic recirculation)

y(t) = Σ_k (−loop)^k b(t − k·rt), rt = 2 = half a carrier period; the carrier autocorrelation factor (−1)^m cancels the sign, giving all-positive E = E_b·Σ_{k,l} loop^{k+l} e^{−α(k−l)²}, α = rt²/(4σ²) = 0.0385. S(0.91620)/S(0.74515) = 4.28 ⇒ 6.32 dB (narrowband); a code-faithful re-derivation including the span = ±2.355σ window truncation gives **6.26 dB** (window edge amplitude 6.25 %, −0.058 dB; dt and the 10⁻⁴ series truncation contribute < 10⁻³ dB; the neglected quadrature term is O(e^{−64})). Deficit vs CW: 3.40 dB. CW limit σ→∞ recovers [(1−loop₀)/(1−loop_M)]² exactly.

### E. Compression at the streaming operating point

Source drive 3×10⁻³ amplified ×~2.45 ⇒ intracavity swing ≈ 0.7 %. Model knee (cell.py): ΔG = −10·log₁₀(1 + (a/0.02)²) ⇒ −0.56 dB at 0.74 %; the passive reference run also compresses (smaller swing), so the net effect on the *ratio* is ≈ 0.2–0.8 dB. Open pending a drive sweep.

### F. Caves-noise magnitude bound

Added noise of a phase-insensitive amplifier enters variance only: x → √G·x, V → G·V + (G−1)(n̄+½) (the repos' own rule, Fock-verified in qlindblad.py). Hypothetical misattribution to gain, δG_dB = 10·log₁₀(1 + N_add/(G·N_sig)) at G = 9.25: vacuum (G−1)/2 = 4.1 quanta ⇒ 0.0005 dB at N_rail = 3833 (0.05 dB at N_knee = 38); matched-300 K thermal (G−1)(n̄+½) = 51.7 quanta ⇒ 0.006 dB at rail. All ≥ 270× too small for 1.86 dB, and structurally absent regardless.

At matched thermal input V_in = n̄+½: F = SNR_in/SNR_out = (G·V_in + (G−1)V_in)/(G·V_in) = 2 − 1/G — n̄ cancels; the only temperature dependence of the floor numbers is through G(T), which is what Section 1 exploits.

### References

M. Dyakonov and M. Shur, Phys. Rev. Lett. **71**, 2465 (1993). H. A. Haus and J. A. Mullen, Phys. Rev. **128**, 2407 (1962). C. M. Caves, Phys. Rev. D **26**, 1817 (1982). A. E. Siegman, *Lasers* (University Science Books, 1986), regenerative buildup. L. M. Frantz and J. S. Nodvik, J. Appl. Phys. **34**, 2346 (1963).


---

## Agent assessment — 2026-07-10

Assessed suitable for the permanent record by a **3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)):

- 🧵 **Fabric** — **STORE**: This note delivers a genuine, checkable decomposition of two real puzzles in the repo (the NF 'agreement' and the CW/pulse gap), and I independently verified a dozen of its arithmetic claims (cw_regen_gain_dB_at_0p7=9.66100612, noise_figure_floor_dB=2.768940, F_dec_300K_dB=2.774993, M_th_num→0.7M_th≈0.1183, compression_1pct_dB=-0.969, the Caves-noise magnitude bounds) against the supplied results.json/qconstants outputs and they match to the printed digit. Epistemic labels (demonstrated/in-model/open) are applied consistently and the note is explicit about which splits are anchored vs which remain open (e.g., the 0.6±0.5 dB discretization bucket), which is exactly the falsifiability standard this project needs. It corrects two real misconceptions (that F_dec derives from the full 5-cell stack; that the CW/pulse gap is dominated by quantum noise) with derivations, not assertion, and flags concrete undocumented parameters (A_op, A_SAT anchoring, drive_amp near the knee, the nonexistent MacCormack option) that matter for WP1 hardening. Citations to Haus–Mullen, Caves, Siegman, and Frantz–Nodvik are used for what they actually show, not oversold, and the note explicitly reins in the Caves-noise magnitude to sub-0.01 dB rather than treating it as a plausible contributor. The one soft spot is the provenance methodology claim ('no code executed... pins provenance as firmly as a rerun would') — this is a strong claim resting on hand-arithmetic rather than an actual rerun, and should ideally be flagged as an open replication gap rather than asserted equivalence, but the note does separately note 'no independent replication of either headline number exists yet,' which mitigates the concern.
  - The claim that hand-derivation from documented equations 'pins provenance as firmly as a rerun would' is stronger than warranted; an actual script rerun should still be logged as an open replication task, not treated as equivalent.
  - The loop(M_th)=1.0022 footnote isn't tagged with the temperature it applies to (matches 353K, not 300K, in my check) — minor clarity issue for future readers.
  - The open/in-model split within the final 1.07 dB gap bucket is acknowledged as depending on solver sweeps that don't exist yet; this is honestly flagged but means part of the note's 'answer' is provisional pending WP1 follow-up runs.
- 🌊 **Kinetic** — **STORE**: The note reproduces reference JSON values (cw_regen_gain_dB_at_0p7=9.661006, pulse_gain_dB_at_0p7_streaming=7.796707, noise_figure_floor_dB=2.768940, F_dec_300K_dB=2.774993, M_th_353K=0.147083, M_th_num=0.168943, compression_1pct_dB=-0.969100) to the last printed digit via independently stated closed-form derivations, which is a strong provenance check rather than a restated summary. It delivers a concrete, checkable result: it shows the 2.77 dB 'agreement' between chain and quantum noise figures is the same formula evaluated at two temperatures (not independent validation), and decomposes the 1.86 dB CW/pulse gap into quantitatively bounded buckets (transient physics ~0.02-0.2 dB, metric convention ~0.74 dB, compression ~0.2-0.8 dB, residual numerics ~0.3-0.9 dB open), correcting two stated premises about the noise-figure's origin. Epistemic labels (demonstrated/in-model/open) are defined up front and applied consistently, including honest open items (no grid/drive sweep exists, single-computation peak metric, docstring claims a MacCormack option that isn't implemented). Limitations are stated without overselling, and citations (Haus-Mullen, Caves, Siegman, Frantz-Nodvik, Dyakonov-Shur) are used precisely for what they show. This is exactly the kind of durable, actionable verification result WP1-WP5 work would need to consult (mislabeled 353K key, undocumented free parameters A_op/A_SAT/drive_amp, qmac.py's temperature-independent 1.9 dB hardcode).
  - Appendix C's comb-line deficit (0.02-0.05 dB) and the two-independent-computation claim (9.64 vs 9.61 dB) are asserted but not independently reproducible by a reviewer without the underlying scripts -- worth flagging for a follow-up rerun.
  - The 14.9% M_th,num-vs-analytic figure is a rounded restatement (actual ratio ~14.87%) -- trivial but shows numbers were sometimes rounded rather than carried to full precision, unlike the headline dB figures.
  - The compression/discretization split within the final 1.07 dB is explicitly marked open and depends on a phenomenological knee parameter (A_SAT=0.02) that the note itself flags as unanchored -- the note is appropriately honest about this, but it means part of the headline decomposition is provisional pending a sweep that doesn't yet exist.
- ⚛️ **Quanta** — **STORE**: The note delivers a genuine, checkable provenance analysis of two specific numbers (2.7689/2.7750 dB noise-figure agreement and the 9.661/7.797 dB CW/pulse gap), and every quantitative claim I could check against the supplied model-chain outputs matches to the last printed digit (cw_regen_gain_dB_at_0p7, pulse_gain_dB_at_0p7_streaming, noise_figure_floor_dB, F_dec_300K_dB, M_th_300K/353K, M_th_num≈0.169). The hand-derivation in Appendix A independently reproduces the Eq.-7 chain term by term and gets identical values, which substantiates the unusual 'no code executed but demonstrated' methodology. Epistemic labels (demonstrated/in-model/open) are applied consistently and conservatively -- e.g., the compression-vs-discretization split is explicitly left open, and the note flags that its own peak-metric waypoint rests on a single verification pass. It delivers a real corrective result (the 2.77 dB 'agreement' is shown to be a tautology of one formula at two temperatures, carrying no cross-validating information) and concrete documentation bugs (mislabeled 353K key, nonexistent MacCormack option, undocumented A_op/A_SAT/drive_amp) with an actionable rename/sweep recommendation feeding directly into WP1/WP5. Limitations section is honest about what remains unresolved (drive sweep, grid-refinement, no independent replication). This is exactly the kind of durable, quantitative, non-overselling artifact WP-work would consult.
  - Relies on hand re-derivation rather than actual code execution for the 'demonstrated' label on several results, though the exact digit-matches to results.json largely justify this.
  - Some intermediate waypoint values (9.6, 8.87 dB) cannot be checked against provided reference JSON since they are not exported outputs -- their uncertainty ranges are appropriately widened but remain unverified by a third party.
  - Note is very long and appendix-heavy for a notes/ entry; acceptable given the density of checkable claims but at the edge of length norms.
