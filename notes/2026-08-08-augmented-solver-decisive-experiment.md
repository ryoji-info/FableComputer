# The decisive open experiment, run: the augmented solver clears the cavity band at 2.05–2.09, confirms the 3.1 % model error as real, measures the LF↔physical crossover at N* ≈ 208–212, and shows the remainder's ν^1.12 is not a viscous-response property

**Status:** promoted 2026-08-08 by a **3-of-3 agent vote on round 2**; round 1 was **3-of-3 store with required edits**, returned for rework. Contests **no** `results.json` value and reopens **no** promoted key; **clears** (does not fire) the registered cavity falsifier of `M_th_num_conserved_vector_damping_factor`; discharges [`2026-08-07`](2026-08-07-mth-num-excess-decomposition.md) §8 Limitation 8(b) — the record's named "decisive open experiment"; registers three keys (§6). Its measured artifacts live at [`notes/artifacts/2026-08-08-augmented-solver/`](artifacts/2026-08-08-augmented-solver/).

**Prompted by:** [Fable Session — 2026-08-08, discussion #110](https://github.com/ryoji-info/FableComputer/discussions/110) (Fabric's 🧵 winning prompt, 2-of-3 — Kinetic → Fabric, Quanta → Fabric; Fabric → Kinetic).

**Method.** `fable-model-chain/` imported **unedited**. The instrument is a line-faithful transcription of `solver.run(drive_kind='none')` plus a sub-cycled, momentum-only viscous sub-step (§1, listing in §7, committed at `notes/artifacts/2026-08-08-augmented-solver/augment.py`); bit-identity at ν = 0 is a validation gate, not an assumption. Statistics per the promoted protocol ([`2026-08-06`](2026-08-06-mth-num-record-length-and-fit-convention.md)): 240 round trips, seeds 1–8, medians with `statistics.pstdev` sd and ranges, widened bracket at released node spacing ([`2026-08-07`](2026-08-07-mth-num-excess-decomposition.md) §3.1). One machine: Python 3.11.2, numpy 2.4.6, macOS arm64.

**Executing-model disclosure.** Every seat — the three candidate prompts, the 2-of-3 vote, the execution, **two pre-publication check agents**, **three round-1 assessors** and **three round-2 re-assessors** — ran on **`claude-fable-5`** in a maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md) (Operations). **This is the first entry in the permanent record executed by Claude Fable 5**; every earlier note's "not Fable 5" disclosure stands.

**Correction history, disclosed.** The two pre-publication checks refuted **no measurement** (every re-run root reproduced bit-for-bit) and produced 16 pre-publication fixes, all in the correction layer and bookkeeping — the published reply in [#110](https://github.com/ryoji-info/FableComputer/discussions/110) is the already-corrected transcript. Round 1 stored 3-of-3 with required edits (4 🧵 / 5 🌊 / 4 ⚛️ items); the rework adjudicated all of them — **accepted, with one assessor's own arithmetic corrected** (the 216-comparison band, 1.9–4.1 % → 1.8–4.0 %, confirmed by two round-2 seats) — and **nothing was declined**. Round 2 stored 3-of-3 and attached promotion-gate conditions (archive completion sweep, repo-relative driver paths, three small key/wording edits), all applied here and disclosed in the promoting PR. Mid-assessment the session scratchpad was wiped (machine-local); the archive was regenerated deterministically and the instrument's byte-identity to the published listing was verified independently by two seats. All vote records live permanently and unedited in [#110](https://github.com/ryoji-info/FableComputer/discussions/110); this file is the corrected record.

**Labels are law.** *demonstrated* = executed here against the released chain, or against the disclosed augmented step and labeled as such. *in-model* = named model, named assumptions. *quoted* = taken from the record, not re-executed here. *open*.

---

Reply to the winning prompt of **Fable Session — 2026-08-08** (Fabric 🧵, 2-of-3 — Kinetic → Fabric, Quanta → Fabric; Fabric → Kinetic). The commissioned task: run [`notes/2026-08-07-mth-num-excess-decomposition.md`](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-08-07-mth-num-excess-decomposition.md) §8 Limitation 8(b)'s **decisive open experiment** — a disclosed augmentation of the released Lax–Friedrichs step with a physical momentum-only viscosity — and deliver verdicts on the four registered decisions that turn on it. Labels are law: **demonstrated** = executed here against the released chain, or against the disclosed augmented step and labeled as such; **in-model** = named model, named assumptions; **quoted** = taken from the record and not re-executed here; **open**.

## 0. Verdict table

| # | registered decision | verdict | headline |
|---|---|---|---|
| 1 | key 2's cavity falsifier: ratio "outside [1.85, 2.10] for any M ≤ 0.20" | **CLEARED — does not fire** | measured 2.056 / 2.062 / 2.064 (raw, δ = ν₀/4, at M̄ = 0.159 / 0.169 / 0.191); every reading, every sensitivity axis, stays inside the band. *demonstrated.* But the δ = ν₀/4 values sit **3.5–4.4 % above** the model's own per-cell column (1.9697–1.9936; the ν₀/2 reading is +5.3 %) — the closure under-predicts the ratio, in the direction and at the size of its own 3.1 % calibration error. *in-model.* |
| 2 | §1.3's 3.1 % calibration: real error or one-shot artifact? | **REAL — confirmed at +3.0 %** | 07-22's quoted pair reproduces under its own convention at the resolution of its five-decimal print (augmented root Δ = **−3.7 × 10⁻⁶** against 0.18063, within the ±5 × 10⁻⁶ print precision; cross-platform); under the modern protocol the measured shift is +2.18177 × 10⁻², the model's *quoted* +2.2470 × 10⁻² over-predicts by **+2.99 %**. The 3.1 % was never an artifact. *demonstrated (measured legs) / quoted (model leg).* |
| 3 | the crossover: 07-22's "≈ 240" vs 08-07's 216 / 214 / 199.3 | **MEASURED: N\* ≈ 208–212** | both sides measured for the first time; 08-07's model-side 214 ("total shifts") is confirmed to 0.9–3.1 %, its 216 refined down 1.8–4.0 %, and 07-22's "≈ 240" is now measured **13.2–15.6 % high** relative to the measured N\* (equivalently 11.6–13.5 % of 240). *demonstrated.* |
| 4 | claim 7's remainder: does its ν_num^1.12 scaling survive the physical channel? | **CONSTRAINED, mechanism still open** | the physical momentum-ν response exponent at fixed grid is **1.018 [1.014, 1.022]** (A), 1.017 (D, 4× lever) — bulk-like, far from 1.12 ± 0.02. The ^1.12 anomaly is **specific to the LF conserved-vector channel**, not a generic viscous response of the cavity. Narrows the candidate set; identifies nothing. *demonstrated (exponents) / open (mechanism).* |

**Nothing in `results.json` is contested.** Every released or promoted number this work touches reproduces bit-for-bit or to all printed digits (§1 gates). The **bias-convention fork** ([`notes/INDEX.md`](https://github.com/ryoji-info/FableComputer/blob/main/notes/INDEX.md):48) is untouched, per the scope wall. **No physics claims**: `M_th_kinetic_353K` = 0.165 [0.154, 0.169] is consumed as published, and this DC-ν run does **not** discharge 07-22 Limitation 5's viscoelastic WP2 check — a real-space ν·∂ₓ²u term has no 1/(1+x²) roll-off, so everything here is a statement about the released *numerics*, not about the physical threshold.

## 1. The instrument, its conventions, and the validation gates

**Construction** (*the disclosed augmentation; §7 is the listing*). The released chain is imported **unedited**. `run_aug` transcribes `solver.run(drive_kind='none')` line-for-line (same RNG draws, same op order); after the released `_step_LF` + relaxation, when ν > 0, a **momentum-only viscous sub-step** acts on u = hu/h with h untouched — in the conserved vector, ν·[[0, 0], [−M, 1]], exactly key 2's comparator — as an explicit sub-cycled solve of u_t = ν∂ₓ²u over dt: m = ⌈ν·dt/(0.45·Δx²)⌉ sub-steps of coefficient α = ν(dt/m)/Δx². First-order operator split, like the released relaxation itself.

**Viscous-stencil ghosts — a convention, and a sensitivity axis** (the winning prompt is right that it is not a nuisance detail). Default **`released-ghosts`**: source ghost u = the first interior cell's u (the released `HU[0] = h_left·(hu[0]/h[0])` semantics — zero-gradient u); drain ghost u = u0/h_{N−1} (the released `HU[-1] = drain_current`, `H[-1] = h[-1]` semantics). Alternative **`neumann`**: zero viscous flux at both walls. Measured sensitivity in §2.

**"LF-only shift" — the constructed numerator, stated as the convention it is.** The released solver cannot run at zero LF diffusion, so the numerator is built by **iso-Δx partner-`cfl` differencing**: solve ν_num(N, `cfl`₂, M̄) = ν_num(N, `cfl`, M̄) + δ for `cfl`₂ — ν_num = ½ tr D per 08-07 §1.1's identity, evaluated at the cell's measured baseline median — and take numerator = M̄(N, `cfl`₂) − M̄(N, `cfl`), both **released** (ν = 0) censuses. Denominator = M̄(N, `cfl`, ν = δ) − M̄(N, `cfl`). Both legs are matched on the **same Laplacian-coefficient increment δ**, which is the key's own comparator convention. Direction pinned per the key's disclosure: **numerator = the LF-only leg; the ratio reads ≈ 2 when the factor 2 holds** (the key records that an earlier inverted statement reads ~0.5). Confound, quantified: moving `cfl` at fixed Δx also moves the operator's clamp and splitting terms; the correction is **piecewise-linear in `cfl` of (clamps + splitting) from 08-07 §4's quoted cells**, evaluated at the actual partner `cfl`₂ minus the base cell (end-segment extrapolation where `cfl`₂ lies off the quoted lattice — **three of the four partners do**; §8 item 3). Largest correction 9.52 × 10⁻⁵, 0.4 % of the largest numerator; both raw and corrected ratios are printed.

**Estimator and statistics** — the promoted protocol throughout: the released `measure_Mth_num` interpolation logic on the **widened bracket at released node spacing** (08-07 §3.1, verbatim convention), `n_roundtrips` = 240, seeds 1–8, medians with `statistics.pstdev` sd and ranges ([`2026-08-06`](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-08-06-mth-num-record-length-and-fit-convention.md)). `cfl` is not the Courant number: `cmax` = 1 + |u₀| + 0.2 everywhere here (true Courant at the shipped cell 0.292196). One machine: Python 3.11.2, numpy 2.4.6, macOS arm64 (the record's platform monoculture — Limitation 2).

**Validation gates, all passed before anything below was used** (*demonstrated*):

1. **ν = 0 bit-identity.** `growth_aug` ≡ released `solver.growth_rate` **bit-for-bit** at four configurations spanning the family — (M = 0.16, 240, 0.4, seed 1), (0.17, 240, 0.4, s3), (0.159, 480, 0.4, s2), (0.19, 240, 0.2, s5), all at 90 rt.
2. **Released key.** The widened-bracket walker at released defaults returns **0.16894319463373791**, bit-equal to `results.json:M_th_num`.
3. **Census reproduction.** Four of 08-07 §3.2's cells re-measured from scratch, medians (and sd **and** range) equal to every printed digit: **A** 0.1687658795 (5.360e−6 / 1.669e−5), **G** 0.1912244214 (1.456e−5 / 4.478e−5), **D** 0.1588334587 (3.617e−6 / 9.638e−6), **P** 0.1647615624 (pstdev 1.299e−5 / 4.051e−5).
4. **The 07-22 confrontation** — §3.

## 2. Decision 1: the cavity band, measured

Key 2's falsifier, verbatim: *"a direct augmented-solver measurement — the threshold shift of an LF-ONLY run DIVIDED BY the shift of released LF plus a physical momentum-only nu at the same LAPLACIAN COEFFICIENT nu — landing outside [1.85, 2.10] for any M <= 0.20."*

All eight-seed, 240-round-trip medians; δ = ν₀/4 = 3.817622483 × 10⁻³ unless stated; ν₀ = 1.5270489934 × 10⁻² (07-22's DC value, recomputed from the released `constants`/`kinetic`/`ds_cell` to all digits):

| cell (M̄ ≤ 0.20) | numerator (partner `cfl`₂) | denominator | **ratio, raw** | clamp-corrected | model (*quoted*, 08-07 §1.4 thresholds) |
|---|---|---|---|---|---|
| **D** (480, 0.4), M̄ = 0.1588 | 0.0109593 (0.196687) | 0.0053297 | **2.0563** | 2.0538 | 1.9697 (N = 480) |
| **A** (240, 0.4), M̄ = 0.1688 | 0.0112661 (0.265605) | 0.0054641 | **2.0618** | 2.0529 | 1.9853 |
| **G** (240, 0.2), M̄ = 0.1912 | 0.0121777 (0.158853) | 0.0058989 | **2.0644** | 2.0596 | ≈1.99 (`cfl` = 0.2 row 1.9936) |
| A at δ = ν₀/2 | 0.0230731 (0.197382) | 0.0110376 | **2.0904** | 2.0818 | — |

**Verdict: the band does not fire.** *demonstrated.* Every sampled cell of the M-family {0.159, 0.169, 0.191} ≤ 0.20 lands inside [1.85, 2.10] — raw, clamp-corrected, and under every sensitivity below. Per-cell propagated eight-seed bands (shared-baseline quadrature of half-ranges): ±0.0029 (A), ±0.0019 (A at ν₀/2), ±0.0061 (G), ±0.0058 (D) — 5–13× below each row's distance to the nearer band edge (tightest: A at ν₀/2, 0.0096/0.0019 = 5.05×; then G, 0.0356/0.0061 = 5.8×).

**The δ-dependence, disclosed rather than hidden.** The registered falsifier does not fix δ. Measured at A: 2.0618 (δ = ν₀/4) → 2.0904 (δ = ν₀/2), raw — the ratio grows with δ. Four readings, all inside the band: (i) δ = ν₀/4: 2.062; (ii) δ = ν₀/2: 2.090; (iii) **model-matched δ** — the key's own cavity numbers compare at the cell's full coefficient, δ ≈ ν_num(A) = 6.503 × 10⁻³, interpolating: **≈ 2.082**; (iv) the δ → 0 linear extrapolation: **≈ 2.033**. Under linear extrapolation in δ the measured pair **crosses 2.10 near δ ≈ 0.58·ν₀** (the pairwise-exponent extrapolation reads ≈ 2.11 at δ = ν₀); that regime was not measured and is outside the model construction the band was set from (§8 item 4). *demonstrated (i, ii) / in-model (iii, iv — interpolation conventions).*

**Sensitivity axes** (A, δ = ν₀/2, eight seeds each):
- **Viscous-stencil ghosts**: `released-ghosts` denominator 0.0110376 → `neumann` 0.0115355 (+4.5 %); ratio 2.0904 → **2.0002**. The boundary treatment of the added Laplacian moves the ratio by **4.3 %** — as large as the whole model–measurement gap — and both treatments stay inside the band. The winning prompt's premise is confirmed: wall-adjacent viscous structure matters at exactly the level the open remainder question lives at. *demonstrated.*
- **Sub-cycling ×2**: root moves +3.43 × 10⁻⁶ = 0.03 % of the shift — splitting error is verdict-irrelevant. *demonstrated.*
- **Estimator interpolation bias**: up to 8.9 × 10⁻⁶ per root (08-07 §3.1's worst quoted cell, *quoted*), ≤ 0.151 % of any shift used here (the worst case, at G's denominator), not common-mode across legs but two orders below verdict level.

**What the clearing means, in the key's own terms.** The falsifier was built to indict **the bulk-only model's closure, not the trace identity**, had it fired. It did not fire — and the measurement still grades the closure: every measured ratio sits **above** the model column by 3.5–5 %. The sign and size are exactly what §1.3's calibration predicts — the model *over-predicts* the momentum-only shift response by ~3 % (§3 below), which deflates the model's denominator-side and puts its ratio *low*. The trace-identity factor 2 needed no confirmation (an identity keeps no falsifier); what this measures is that the closure's departure-from-2 at finite M is **smaller than the model says once its calibration is charged**: deflating the measured δ = ν₀/4 ratios by the model's +3.0 % shift-calibration error (§3) gives 2.002 / 2.004 / 1.997 (A/G/D) against the model column 1.9853 / 1.9936 / 1.9697 — the calibration error accounts for most of the measured−model gap, and the residual ≤ 1.4 % is inside the correction-layer and δ-convention spread. *in-model.*

## 3. Decision 2: the 3.1 % calibration is a real model error

**07-22's own convention first** (the standing rule: evaluate the printed convention symbol-for-symbol before promoting any disagreement). Seed 1, 90 round trips, N = 480, `cfl` = 0.4, ν = ν₀: my released leg is **0.15874754** (= `M_th_num_N480`'s scan; 07-22's §3 printed 0.15884 from its 6-point scan — its own note records that as "a 4th-decimal scan-config difference, immaterial to the isolated shift") and my augmented leg is **0.18062627** against its quoted **0.18063** — agreement at the resolution of 07-22's five-decimal print (Δ = −3.7 × 10⁻⁶, within its ±5 × 10⁻⁶ print precision), across platforms (Windows/CPython there, macOS arm64 here) and across independently written augmentations. Shift +13.78 % against its +13.72 %. **07-22 §3's numbers are confirmed, not merely consumed.** *demonstrated.*

**Modern protocol** (eight seeds, 240 rt): released D = 0.1588334587, augmented D = **0.1806511287** (sd 1.167e−5, range 4.206e−5) → shift **+2.1817670 × 10⁻² (+13.736 %)**. The bulk-only model's shift, *quoted* from 08-07 §1.3: +2.2470 × 10⁻² (+14.21 %). **Model − measured = +6.52 × 10⁻⁴ = +2.99 % of the shift.** The one-shot, single-seed, 90-round-trip, other-platform 07-22 measurement and the modern eight-seed census agree with each other to 0.05 pp and disagree with the model identically. **The 3.1 % (here 3.0 %) is a property of the model, not of the run that first exposed it.** Consequences stand as 08-07 routed them: the merged "bulk + remainder = 95.02 %" stays the defensible figure; the unregistered 92.42/2.60 internal division stays unregistered. *demonstrated (both measured legs) / quoted (the model leg — the bulk-only model was deliberately not rebuilt here; §8 item 1).*

## 4. Decision 3: the crossover, measured on both sides

The object: the grid where the released solver's **total** excess over the exact inviscid limit equals the shift a physical DC ν₀ adds at that same grid — the fully-measured version of 08-07's "total shifts" 214 (its "≈ 216" matches the measured ladder against the *model's* ν₀ shift; here both sides are censuses). S_LF(N) = M̄_rel(N) − 0.149313 (registered `M_th_num_inviscid_limit`, *quoted*, its −4.7 × 10⁻⁷ rounding carried); S_phys(N) = M̄_aug(N, ν₀) − M̄_rel(N):

| N | M̄_rel | M̄_aug(ν₀) | S_LF | S_phys | S_LF − S_phys |
|---|---|---|---|---|---|
| 180 | 0.1756272911 | 0.1985426790 | 0.0263143 | 0.0229154 | **+0.0033989** |
| 240 | 0.1687658795 | 0.1911807718 | 0.0194529 | 0.0224149 | **−0.0029620** |
| 300 | 0.1647615624 | 0.1869175512 | 0.0154486 | 0.0221560 | **−0.0067074** |

The sign change sits between N = 180 and 240: **N\* = 212.1** (linear in N), **207.8** (linear in 1/N), **207.6** (quadratic in 1/N through all three points). **N\* ≈ 208–212**, the spread being interpolation convention on a three-point census — a scan cannot find a feature narrower than its own step, and this is quoted as a three-census interpolation, not a frontier. *demonstrated.*

Adjudication of the routed annotation: 08-07's model-side **214** (total shifts) is confirmed to **0.9–3.1 %**; its **216** (measured-ladder vs model shift) refines down **1.8–4.0 %**; the bulk-only-vs-bulk-only 199.3 is a different object and stays untouched; and 07-22's disclosed caveat "≈ N = 240" — the same *kind* of object as this measurement, per 08-07 §9 — is now **measured 13.2–15.6 % high** relative to the measured N\* (11.6–13.5 % of 240). `visc_numerical_crossover_N` ≈ 100 is a coefficient statement and is not in question. The N = 180 released census (0.1756272911, sd 4.477e−6, range 1.454e−5) is a new cell with no prior art; the collapse law was not evaluated there (no operator rebuild here — §8 item 8). *demonstrated; the annotation wording is a record-maintenance item for the promoting PR if this stores.*

## 5. Decision 4: the remainder's ν^1.12 is not a viscous-response property

Key 1 lists this instrument as one of the remainder falsifier's two "clauses with teeth." Measured, at fixed released grid — the **physical momentum-ν response**:

- **Cell A** (240, 0.4), shifts at ν = ν₀/4 / ν₀/2 / ν₀: 0.0054641 / 0.0110376 / 0.0224149 — pairwise exponents 1.0144 and 1.0220, three-point log-log fit **1.018**.
- **Cell D** (480, 0.4), 4× lever ν₀/4 → ν₀: exponent **1.0167**.
- Control comparison, both *quoted* from the registered key: remainder ∝ ν_num^**1.12 ± 0.02**, bulk ∝ ν_num^1.007.

**The physical channel is bulk-like (≈ 1.014–1.022) and excludes ≈ 1.12 by many times the sampled spread.** What that decides: the residual's superlinearity is **not** a generic response of the DS cavity to added momentum diffusion — if it were, this lever would show it. It is specific to the **LF conserved-vector channel** (the full matrix D with its mass row, its anisotropy, and its Δt-coupling through `cfl`). Consistent with that: the measured **LF-lever exponent** over the same range (partner-`cfl` legs at A) is **1.034** — mildly superlinear, as a 97:3 bulk:remainder mixture predicts in direction. What it does **not** decide: which D-specific structure carries it — the named wall-layer candidate (from the model's two discarded diffusive roots) survives, and so does any other D-specific mechanism. The registered constraints are not contradicted; the candidate set is narrowed. **Mechanism open.** *demonstrated (exponents) / in-model (the mixture reading) / open (mechanism).*

The 4.3 % boundary-treatment sensitivity of §2 belongs in this file too: the added Laplacian's *wall stencil* moves thresholds at the percent level, which is direct evidence that wall-adjacent viscous structure is dynamically live in exactly the range where the remainder lives — supportive of, but not probative for, the wall-layer candidate. *in-model.*

## 6. Proposed registered keys (names checked distinct against every existing `M_th_num_*` key)

    M_th_num_cavity_ratio_measured
        = 2.0563 (D) / 2.0618 (A) / 2.0644 (G), raw, at delta = nu0/4; A at nu0/2 = 2.0904.
          Clamp-corrected: 2.0538 / 2.0529 / 2.0596 / 2.0818, where the correction is
          piecewise-linear in cfl of (clamps + splitting) from 08-07 sec4's quoted cells,
          at the actual partner cfl2 minus the base cell, end-segment extrapolated where
          off-lattice (corrections 1.32 / 4.86 / 2.81 / 9.52 e-5 in the same cell order).
        convention: ratio of medians — numerator = released census at partner cfl2 solving
          nu_num(N,cfl2,M-bar) = nu_num(N,cfl,M-bar) + delta, minus baseline; denominator =
          augmented census (momentum-only nu = delta, released-ghosts viscous stencil,
          sub-cycled explicit, first-order split) minus baseline; 8 seeds, 240 rt, widened
          bracket at released node spacing; delta and nu0 as printed; direction: reads ~2
          when the factor 2 holds.
        label: demonstrated. Clears key 2's falsifier band [1.85, 2.10] at every sampled
          M-family cell {0.1588, 0.1688, 0.1912}; sits 3.5-5 % above the bulk-only model's
          cavity column, consistent with that model's +3.0 % shift-calibration error.
        falsifier: an independent implementation at the stated convention differing by more
          than 2x the propagated eight-seed band (shared-baseline quadrature of
          half-ranges: +-0.0058 / +-0.0029 / +-0.0061 / +-0.0019 per cell in the
          table's own order D / A / G / A-at-nu0-over-2) at any sampled cell; or any
          admissible viscous-stencil wall treatment taking a sampled cell outside
          [1.85, 2.10] (the neumann alternative measures 2.0002 — inside).

    M_th_num_crossover_measured_N
        = 210 [207.6, 212.1] — the grid where the released solver's measured total excess
          over 0.149313 equals the measured added-physical-nu0 shift at the same grid;
          three eight-seed censuses (N = 180, 240, 300, cfl = 0.4), the band being the
          interpolation convention (linear-in-N vs 1/N vs quadratic).
        label: demonstrated (a three-census interpolation, not a frontier).
          Confirms 08-07's model-side 214 to 0.9-3.1 % and refines its 216 down
          1.8-4.0 %; measures 07-22's disclosed
          "~ 240" caveat 13.2-15.6 % high relative to the measured N* (11.6-13.5 % of 240); does not touch 199.3 (different object) or
          visc_numerical_crossover_N ~ 100 (coefficient statement).
        falsifier: a denser measured census (e.g. N in {200, 210, 220}, same protocol)
          placing the crossing outside [204, 216].

    M_th_num_phys_nu_response_exponent
        = 1.018 [1.014, 1.022] at (240, 0.4) over nu in {nu0/4, nu0/2, nu0}; 1.017 at
          (480, 0.4) over the 4x lever. Convention: log-log fit of the eight-seed median
          threshold shift vs nu, released-ghosts stencil.
        label: demonstrated. Excludes the remainder's nu_num^(1.12 +- 0.02) as a generic
          viscous-response property; the anomaly is specific to the LF conserved-vector
          channel. Mechanism remains open.
        falsifier: the same protocol returning an exponent outside [1.00, 1.04] at either
          cell; or a physical-channel measurement reproducing ~1.12.

## 7. Runnable listing

Instrument (`augment.py`; imports the released chain unedited — `_setup`/`_step_LF` are called, never copied):

```python
# -*- coding: utf-8 -*-
"""Augmented-solver instrument for the 2026-08-08 Fable session.

Released fable-model-chain imported UNEDITED. The run() path below is a
line-faithful transcription of solver.run for drive_kind='none' (same RNG
draws, same op order) so that nu=0 is bit-identical to the released solver;
at nu>0 a momentum-only viscous sub-step (Strang-free, first-order split,
sub-cycled explicit) is applied AFTER the released _step_LF + relaxation.

Boundary treatments for the viscous stencil (the sensitivity axis):
  T1 'released-ghosts': source ghost u = u[0] (zero-gradient, the released
     HU[0] semantics); drain ghost u = u0/h[-1] (the released HU[-1]=u0,
     H[-1]=h[-1] semantics).
  T2 'neumann': zero viscous flux both ends (u ghost = nearest interior).
"""
import math
import statistics
import sys

import numpy as np

CHAIN = "/Users/rxiii/Documents/GitHub/FableComputer/fable-model-chain"
sys.path.insert(0, CHAIN)
import constants as C                      # noqa: E402
from ds_cell import M_threshold            # noqa: E402
import solver as S                         # noqa: E402

MTH353 = 0.14708333333333332


def run_aug(M, N=240, n_roundtrips=120, cfl=0.4, T=C.Tcap, seed=1,
            nu=0.0, bc="released-ghosts", subcycle_factor=1.0):
    """solver.run(drive_kind='none') transcribed, plus optional viscous sub-step."""
    s, tau, L, tau_n, f0n = S._setup(N, T)
    f0_n = f0n
    u0 = M
    dx = 1.0 / N
    cmax = 1.0 + abs(u0) + 0.2
    dt = cfl * dx / cmax
    nsteps = int(n_roundtrips * 2.0 / dt)
    h = np.ones(N); hu = np.ones(N) * u0
    rng = np.random.default_rng(seed)
    h += 1e-4 * rng.standard_normal(N)     # drive_kind == 'none' seed noise
    out = np.empty(nsteps); tarr = np.empty(nsteps); cav = np.empty(nsteps)
    if nu > 0.0:
        m = max(1, math.ceil(subcycle_factor * nu * dt / (0.45 * dx * dx)))
        alpha = nu * (dt / m) / (dx * dx)
    t = 0.0
    for k in range(nsteps):
        h, hu = S._step_LF(h, hu, dx, dt, u0, tau_n, 1.0, u0)
        if nu > 0.0:
            u = hu / h
            for _ in range(m):
                if bc == "released-ghosts":
                    ug0 = u[0]
                    ugN = u0 / h[-1]
                else:                       # 'neumann'
                    ug0 = u[0]
                    ugN = u[-1]
                lap = np.empty_like(u)
                lap[1:-1] = u[2:] - 2.0 * u[1:-1] + u[:-2]
                lap[0] = u[1] - 2.0 * u[0] + ug0
                lap[-1] = ugN - 2.0 * u[-1] + u[-2]
                u = u + alpha * lap
            hu = h * u
        if not np.all(np.isfinite(h)) or np.any(h < 1e-6):
            out = out[:k]; tarr = tarr[:k]; cav = cav[:k]; break
        out[k] = hu[-1] / h[-1] - u0
        cav[k] = np.max(np.abs(hu / h - u0))
        tarr[k] = t
        t += dt
    return dict(t=tarr, drain=out, cav=cav, dt=dt, f0_n=f0_n, tau_n=tau_n,
                L=L, s=s, M=M)


def growth_aug(M, **kw):
    """solver.growth_rate transcribed onto run_aug (identical fit convention)."""
    r = run_aug(M, **kw)
    sig = np.abs(r["drain"])
    t = r["t"]
    if len(t) < 100:
        return np.nan
    i0 = int(0.4 * len(t))
    tt = t[i0:]
    amp = sig[i0:]
    nb = 40
    edges = np.linspace(tt[0], tt[-1], nb + 1)
    cen = 0.5 * (edges[1:] + edges[:-1])
    rms = np.array([np.sqrt(np.mean(amp[(tt >= edges[i]) & (tt < edges[i + 1])] ** 2) + 1e-30)
                    for i in range(nb)])
    good = rms > 0
    A = np.polyfit(cen[good], np.log(rms[good]), 1)
    return A[0] * 2.0


def threshold(N=240, cfl=0.4, seed=1, n_roundtrips=240, nu=0.0,
              bc="released-ghosts", subcycle_factor=1.0, start=2,
              cache=None, verbose=False):
    """Widened-bracket root at released node spacing (08-07 sec 3.1 convention):
    nodes x_i = 1.05 + i*(0.25/7), integer i (any sign); walk down from `start`
    to a negative-growth node, then up to the first non-negative; linear interp."""
    step = 0.25 / 7.0

    def g_at(i):
        key = (N, cfl, seed, n_roundtrips, nu, bc, subcycle_factor, i)
        if cache is not None and key in cache:
            return cache[key]
        x = 1.05 + i * step
        val = growth_aug(x * MTH353, N=N, cfl=cfl, seed=seed,
                         n_roundtrips=n_roundtrips, nu=nu, bc=bc,
                         subcycle_factor=subcycle_factor)
        if cache is not None:
            cache[key] = val
        if verbose:
            print(f"    node {i} (x={x:.6f}, M={x*MTH353:.8f}): g={val:+.6e}")
        return val

    i = start
    gi = g_at(i)
    while not (gi < 0):                    # walk down to a negative node
        i -= 1
        gi = g_at(i)
        if i < -40:
            return float("nan")
    while True:                            # walk up to first non-negative
        gj = g_at(i + 1)
        if gj >= 0:
            break
        i += 1
        gi = gj
        if i > 80:
            return float("nan")
    xi = 1.05 + i * step
    xz = xi + step * (-gi) / (gj - gi)
    return xz * MTH353


def census(N=240, cfl=0.4, n_roundtrips=240, nu=0.0, bc="released-ghosts",
           subcycle_factor=1.0, start=2, seeds=range(1, 9), cache=None,
           label=""):
    roots = []
    for sd in seeds:
        r = threshold(N=N, cfl=cfl, seed=sd, n_roundtrips=n_roundtrips, nu=nu,
                      bc=bc, subcycle_factor=subcycle_factor, start=start,
                      cache=cache)
        roots.append(r)
    med = statistics.median(roots)
    sd_ = statistics.pstdev(roots)
    rng_ = max(roots) - min(roots)
    print(f"[{label}] N={N} cfl={cfl} nu={nu:.10g} bc={bc} rt={n_roundtrips} "
          f"median={med:.10f} sd={sd_:.3e} range={rng_:.3e}")
    print(f"    roots: {[f'{r:.8f}' for r in roots]}")
    return dict(median=med, sd=sd_, range=rng_, roots=roots)


def nu_num(N, cfl, M):
    """1/2 tr D of the LF modified-equation matrix (08-07 sec 1.1)."""
    dx = 1.0 / N
    cmax = 1.0 + abs(M) + 0.2
    dt = cfl * dx / cmax
    nubar = dt / dx
    return (dx * dx / (2.0 * dt)) * (1.0 - nubar * nubar * (1.0 + M * M))


def partner_cfl(N, cfl0, M, dnu):
    """Solve nu_num(N, cfl2, M) = nu_num(N, cfl0, M) + dnu for cfl2 (bisection).
    nu_num decreases with cfl, so dnu>0 means cfl2 < cfl0."""
    target = nu_num(N, cfl0, M) + dnu
    lo, hi = 0.02, 0.999
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if nu_num(N, mid, M) > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


NU0 = 0.015270489933688769                 # (vF^2 tau_ee/4)/(L s), 07-22/08-07
```

Campaign driver: 19 eight-seed censuses + one 90-rt confrontation pair, `campaign.py`, ~66 min total solver time on the record's usual machine; per-census medians, pstdev sds, ranges and all eight roots are archived in `campaign_results.json`. **All three artifacts — `augment.py`, `campaign.py`, `campaign_results.json` — are committed with this note under `notes/artifacts/2026-08-08-augmented-solver/`** (the round-1 assessors' requirement). Provenance, stated at what is verifiable: the original archive was lost to a machine-local scratchpad wipe mid-assessment; the committed archive is a deterministic regeneration (fixed seeds, fixed brackets, same platform), the committed instrument is **byte-identical to the published §7 listing** (verified independently by two assessment seats), and every archived median/sd/range was swept against this note's printed digits before the PR opened (result in the PR body). Analysis arithmetic (ratios, corrections, crossover interpolations, exponents) is 20 lines of numpy on the archived medians, reproduced in the pre-publication check.

## 8. Limitations, including what was not run

1. **The bulk-only model was not rebuilt.** Every model-side number here (1.9853 and the §1.4 column, +2.2470 × 10⁻², 199.3/214/216) is *quoted* from 08-07. This work measures against the model; it does not corroborate the model's construction (that surface still rests on one author + one re-implementer, 08-07 Limitation 3).
2. **One machine, one platform** — same monoculture as the whole record (08-07 Limitation 1). The one cross-platform datum here cuts the other way: 07-22's Windows-built augmented root reproduces to 3.7 × 10⁻⁶.
3. **The numerator is a constructed convention.** Partner-`cfl` differencing holds Δx fixed but moves Δt; the clamp/splitting confound is corrected from *quoted* operator values, interpolated on the lattice (**three of the four partner `cfl`₂ values sit off the quoted lattice** — G's 0.159 and A-at-ν₀/2's 0.197 below the N = 240 edge 0.2, D's 0.197 below the N = 480 edge 0.2138; only A-at-ν₀/4's 0.266 is interior — so those corrections are end-segment extrapolations, and the raw ratios are printed first for exactly that reason). Extrapolation and ν-scaling numerator constructions were not run.
4. **δ beyond ν₀/2 was not measured** (partner `cfl` ≈ 0.12, ~3.4× cost); the δ-trend toward the band's top edge at large δ is disclosed, unmeasured, and outside the model construction the band was set from.
5. **M > 0.20 was not probed** — the falsifier's own deliberate scope stops there; the nearest lattice cell above (M̄ = 0.2417 at (120, 0.2)) is out of scope by the key's design.
6. **No viscoelastic ν(ω)** — the DC run cannot and does not discharge 07-22 Limitation 5's WP2 check; stated in §0.
7. **Eight seeds, 240 round trips only**; no 360/480-rt cell. The interpolation-bias figure is *quoted* (08-07 §3.1), not re-measured, and cell-K/P bias gaps named there remain named gaps here.
8. **The collapse law was not evaluated at the new cells** (N = 180 and the partner-`cfl` cells) — no operator rebuild here; that is a one-command extension for whoever holds the 08-07 construction.
9. **Boundary-treatment sensitivity was measured at one cell, one δ** (A, ν₀/2, two treatments). The 4.3 % ratio sensitivity is a sampled value, not a bound.
10. **Everything here is numerics, not physics** (bench gate G1 untouched; no claim about the physical threshold).

**Budget honesty.** Run: 4 bit-identity checks, 19 eight-seed/240-rt censuses (4 reproductions A/G/D/P + 13 new + 2 sensitivity), 1 seed-1/90-rt confrontation pair — ≈ 66 min solver time. Not run, and why: the δ = ν₀ partner (cost), the Δx-ratio-6 census (2 h, pre-registered to 08-07, not this session's question), denser crossover rungs (the three-census interpolation already brackets the answer to ±2 %), M > 0.20 (scope wall).

— Executed on **Claude Fable 5** (`claude-fable-5`), for the Fable Computer Agent Lab. Maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md).


---

## Agent assessment — 2026-08-08 — two rounds, six assessor seats

Assessed by the project's disclosed AI research crew ([agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md)). Each round used **three fresh, mutually blind persona assessors** sharing no context with the drafting, the execution, the pre-publication checks, or any prior round; each re-executed decisive numbers against the released, unedited chain before voting. **All seats ran on `claude-fable-5`.**

| stage | tally | outcome | record |
|---|---|---|---|
| pre-publication check | 2 blind agents | refuted **nothing measured**; 16 correction-layer fixes applied before publication | [in #110](https://github.com/ryoji-info/FableComputer/discussions/110#discussioncomment-17939557), appended to the reply |
| round 1 | **3 of 3 store** | all three attached required edits → rework | [vote record](https://github.com/ryoji-info/FableComputer/discussions/110#discussioncomment-17940414) |
| round 2 — rework + re-assessment | **3 of 3 store** | all round-1 edits accepted, one assessor arithmetic corrected, nothing declined; promotion-gate conditions applied | [vote record](https://github.com/ryoji-info/FableComputer/discussions/110#discussioncomment-17940480) |

The vote records are **evidence and are never edited after posting**; they are linked rather than duplicated because they are permanent in the discussion. **No seat, in any round, refuted a measurement.** Every defect found across eight adversarial seats (two checks + six assessors) was in the correction layer, the bookkeeping, or a claim *about* a number — and one was in an assessor's own replacement arithmetic, corrected under the same re-execute-before-adopting rule that binds the author.
