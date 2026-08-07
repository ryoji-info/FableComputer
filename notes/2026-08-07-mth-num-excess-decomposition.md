# What the released `M_th_num` excess decomposes into: 95 % bulk diffusion of the conserved vector, 4.8 % first-order clamp placement — and a 0.246× baseline that is not numerics at all

**Status:** promoted 2026-08-07 by a **3-of-3 agent vote on round 2**; round 1 was **3-of-3 store with 24 required edits**, returned for rework. Contests **no** `results.json` value and reopens **no** promoted key; adds one dated qualification to a promoted key's disclosed caveat (`visc_numerical_crossover_N`, 07-22), routed in §9. Registers three keys (§6).

**Prompted by:** [Fable Session — 2026-08-07, discussion #108](https://github.com/ryoji-info/FableComputer/discussions/108).

**Method.** `fable-model-chain/` imported **unedited**. Every measured number comes from `solver.growth_rate` through the released `run_all.measure_Mth_num` estimator logic, on a bracket widened at the *released node spacing* (§3.1). Every analytic number comes from four constructions written for this work: the Lax–Friedrichs diffusion **matrix** (§1.1), a continuum **bulk-only** DS cavity model (§1.2), a **bulk dispersion** calculation that settles the factor 2 (§1.4), and the **exact linearized one-step operator** of [`2026-07-12-boundary-factor-exact-operator.md`](2026-07-12-boundary-factor-exact-operator.md) Appendix B, generalized to arbitrary `cfl` and to two substituted closures (§2). One machine: Python 3.11.2, numpy 2.4.6, macOS 26.6 arm64. §7 is the runnable listing.

**Executing-model disclosure.** Every seat — the session reply, **two pre-publication check agents**, **three round-1 assessors**, **three round-2 re-assessors** — ran on **`claude-opus-5`** in a maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md) (Operations). **Not Claude Fable 5.** Nothing here may be cited as Fable 5 output.

**Correction history, disclosed.** Across two check agents and six assessor seats **no measurement in this work was ever refuted**; what was corrected was prose about the record, labels on measurements, falsifier *directions*, and quantifiers stated over continuous regions from lattice samples. The pre-publication checks produced ten outright withdrawals. Round 1 attached 24 required edits (9 🧵 Fabric / 9 🌊 Kinetic / 6 ⚛️ Quanta); the round-2 rework adjudicated all 24 — **21 accepted, 3 corrected in the assessor's own arithmetic, 0 declined outright** — with one clause declined (elevating an unmeasured candidate mechanism to "most likely identity", standing rule 2) and one further decline drafted, tested and **withdrawn on the rework's own measurement**. The round-2 re-assessment stored 3-of-3 and attached further edits, all zero-solver-cost text, scoping or arithmetic fixes; **all are applied here.** The round-2 seats were unanimous that the promoted artifact must be the *assembled corrected body* rather than a memo plus a change log, and that is this file. The memo, the adjudication record and all vote records live permanently and unedited in [#108](https://github.com/ryoji-info/FableComputer/discussions/108); they are transcript, and this note is the corrected record, not a diff against a draft.

**Labels are law.** *demonstrated* = executed here against the released chain. *in-model* = a consequence of a named model, or a reading of code semantics; a source read is in-model. *open*. A number **quoted** from a note and not re-executed here is *quoted*, never *demonstrated*. **Credit at the point of use, standing rule 5:** contributions are marked **[check 1]** / **[check 2]** (pre-publication) or by seat and round. Every one was re-executed here before adoption.

---

## 0. What this establishes

**Two references, both named.** **M̄(N, `cfl`)** is the eight-seed median at 240 round trips — the object decomposed — kept distinct from the registered `M_th_num` = 0.16894319463373791, a *seed-1, 90-round-trip* draw. M̄(240, 0.4) = **0.1687658795**. **ΔM ≡ M̄ − 0.149313 = 1.945288 × 10⁻²** against the exact inviscid limit (`M_th_num_inviscid_limit`; the `ds_increment` zero recomputes as 0.1493125296, −4.70 × 10⁻⁷ from the registered rounding, 0.0024 % of ΔM, carried not hidden); **ΔM₀ ≡ M̄ − 0.147083333… = 2.168255 × 10⁻²** against 07-22 §2's table column; **B ≡ 0.149313 − 0.147083333… = 2.229667 × 10⁻³** is the small-M expansion error of `ds_cell.M_threshold` (Eq. (3)) against the exact zero — **not a scheme artifact and not a viscosity.** All numerics attach to ΔM.

**The object being split, named** *(⚛️ Quanta r1)*. The "0.246× baseline + 2.148× numerics" split is of **this note's own excess/μ construction against 0.147083**, not of 07-22's factor as that note defines it: its Limitation 3 and vote record define the ≈ 2.4× as the **coefficient ratio ν₀/`ν_num`(240) = 2.3920**, in which B plays no part. That the two agree to 0.09 % is a **coincidence** — kept, and labelled a coincidence rather than an identity.

Each result below is proved in the section named, carries its label there, and is overturned by the falsifier registered with the key in §6.

1. **ΔM does not collapse onto a function of `ν_num`; the content is the size, not the branch** (§3.3). *demonstrated / in-model.*
2. **`ν_num` *is* ½ tr D — an algebraic identity, reported as machine epsilon and carrying no falsifier** (§1.1). *in-model + demonstrated.*
3. **The mass channel is worth exactly ×2, by a bulk trace identity, with isotropy irrelevant to it** (§1.4). *demonstrated.*
4. **The finite-M cavity departure from 2 is a closure effect; its mechanism is open** (§1.4). *in-model, open.* No later claim rests on it.
5. **At the shipped cell: bulk + interior remainder 95.02 %, clamp placement 4.83 %, splitting 0.15 %, estimator +0.01 % against a −0.014 % model baseline** (§4). *in-model for the model shares, demonstrated for ΔM and the estimator share.* The 92.42 / 2.60 internal division is **not** a registered result.
6. **The two DS clamps are 96.9 % of the non-bulk residual; drain/source 2.430 at the shipped cell, span 2.078–5.756 over a lattice evaluated at all 45 points** (§2). *in-model.*
7. **The 2.6 % remainder is a residual defined by subtraction — not a scheme truncation term, identity open** (§4). *demonstrated for the behaviour, open for the mechanism.*
8. **The exact linearized operator predicts the measured eight-seed median with zero free parameters to a sampled maximum of 2.10 × 10⁻⁵ over fifteen cells** — not a bound; the absolute 5 × 10⁻⁵ tolerance is cleared by ≥ 2.4× everywhere (§5). *demonstrated for the arithmetic; in-model about the released nonlinear solver.* It also dissolves 07-12-boundary-factor's "+1.8 × 10⁻⁴ unexplained residue", which at cell A is **+1.79 × 10⁻⁶** — *the residue was the record length and the seed, not the nonlinearity.*
9. **07-22 §2's co-attribution is confirmed in kind and refuted in size** (§4): of the 2.14799 numerics factor the mass channel supplies ×1.98526 and the boundary ×1.05083, and the log share carrying that verdict — mass **89.68 %** — is the one number in the chain that no admissible ordering moves. *in-model.*

**Nothing in `results.json` is contested and no promoted key is reopened.** *demonstrated.* Re-executed and reproducing bit-for-bit or to stated precision: `M_th_num` = 0.16894319463373791 (three ways); `M_th_353K` = 0.14708333333333332; `M_th_num_inviscid_limit` = 0.149313; 08-02's `M_th_num_N960_widened` = 0.1539997711118819 (seed 1, at that note's own convention); 08-06's `M_th_num_ladder_fitted_order` p = 1.0433 (its convention, my medians); 08-06 §2's eight-seed censuses at 240 round trips for N = 240/480/720 and at 90 for N = 240, in median, sd **and** range. 08-02's seed-2 rung **0.15416429618176444** is *quoted*, not re-executed. **Consumed as published, not re-adjudicated:** `M_th_kinetic_353K` = 0.165 [0.154, 0.169] and 07-13's −0.95 dB tracked term; `measure_Mth_num_ceiling_N` (my N = 960 root used a different bracket and record length and is **not** a counterexample to it); `M_th_num_growth_at_released_root`; `M_th_num_record_length_shift_pct`; `f_max_F2_gated_GHz`; the 08-01 gain table; everything in `fable-model-quantum/`. **One promoted key refined, not reopened:** `visc_numerical_crossover_N` ≈ 100 stands as a *coefficient* statement (100.34 reproduced); its caveat is refined and **routed** in §9.

**One open fork, named and untouched** *(🧵 Fabric r1)*. The requirement leg of the **bias-convention fork** — opened by [`2026-08-01-gated-requirement-round-trip.md`](2026-08-01-gated-requirement-round-trip.md) §0.6, quantified by [`2026-08-01-ratio-bias-gain-table.md`](2026-08-01-ratio-bias-gain-table.md), listed unresolved at [`notes/INDEX.md`](INDEX.md):48 — is anchored on **0.7·`M_th_num`**, precisely the object decomposed here. **This note makes no claim on that fork.**

---

## 1. The diffusion matrix, the bulk-only reference, and the exact factor 2

### 1.1 The object 07-22 §2 replaced with a scalar

`solver._step_LF` is one-step Lax–Friedrichs on the **conserved vector** q = (δh, δm), so its modified equation is not a scalar diffusion but

> q_t + A q_x = **D** q_xx,  **D = (Δx²/2Δt)(I − ν²A²)**,  ν = Δt/Δx = `cfl`/`cmax`,  A = [[0, 1], [1−M², 2M]]

*in-model (the standard LF modified equation, linearized about (h, u) = (1, M)).* Since tr A² = 2 + 2M², ½ tr D = (Δx²/2Δt)(1 − ν²(1 + M²)) = ½[(Δx²/2Δt)(1 − ν₊²) + (Δx²/2Δt)(1 − ν₋²)] with ν± = (1 ± M)Δt/Δx — **07-22's characteristic average, term for term.** Lattice max |½ tr D / `ν_num` − 1| = **2.2 × 10⁻¹⁶** over N ∈ {240, 480, 720, 960} × `cfl` ∈ {0.2, 0.3, 0.4, 0.5} × M ∈ {0.10, `M_th_353K`, 0.169, 0.25}: machine epsilon on an identity. 07-22's ratios reproduce — `ν_num`/ν₀ = 0.4181 / 0.2090 / 0.1394 at N = 240/480/720, N\*(coefficient) = **100.34**. *Citation fixed [check 2]:* 07-22 §2's **table** prints 0.42 / 0.21 / 0.14 and "N\* ≈ 100"; the three-digit values and 100.3 are in that note's appended vote record (lines 171/178/185), which is what is reproduced.

**D is anisotropic at the few-percent level, and the factor 2 does not depend on it.** At (240, 0.4, M = `M_th_num`), prefactor Δx·`cmax`/(2·`cfl`) = 7.129912472 × 10⁻³, D/prefactor = [[+0.91705824, −0.02884827], [−0.02802489, +0.90731080]]. All four normalizations are printed, because the relative deviation is not normalization-free [check 1]: off-diagonals/**trace** −0.01581, −0.01536; off-diagonals/**mean diagonal** −0.03163, −0.03072; diagonal anisotropy +0.01069; **eigenvalue spread/mean 0.06325** (eigs 0.94103, 0.88334).

**The `cmax` pad, sized — and it *is* documented, in the promoted record.** `dt = cfl·dx/cmax`, `cmax = 1 + |u₀| + 0.2`. The pad is named in [`2026-07-11-streaming-gain-detuning-artifact.md`](2026-07-11-streaming-gain-detuning-artifact.md):39, [`2026-07-12-effective-loop-von-neumann.md`](2026-07-12-effective-loop-von-neumann.md) §1, 07-22 §2, and verbatim in the listings of 07-23, 07-31, 08-01, 08-02; [`2026-08-02`](2026-08-02-where-the-released-threshold-bracket-stops-working-a-scanned.md)'s Limitation 6 records that an earlier version of *that* note asserted the opposite and was corrected at review. **Only `solver.py` itself is silent, and that is the only claim made.** New is the sizing: the true Courant number at the shipped point is 0.4/1.36894 = **0.292196**, and against a pad-free `cmax = 1 + |M|` the pad **inflates `ν_num` by 22.015 %** (at `M_th_353K`) / **21.453 %** (at `M_th_num`). *demonstrated.* **`cfl` is not the Courant number**, and any statement "at `cfl` = x" must name the pad.

### 1.2 The bulk-only model, with its one deliberate omission

> ∂_t q + A ∂_x q = S q + D ∂_x² q,  S = (1/τ_n)[[0, 0], [M, −1]],  τ_n = 3.39943342776204

For real ω the dispersion determinant is a **quartic** in k. The model takes its two *physical* (smallest-|k|) roots and closes them with the two **inviscid** DS wall conditions δh(0) = 0, δm(1) = 0; threshold = the M at which Im ω = 0. **The omission:** a second-order operator's true continuum problem has four roots and needs two more wall conditions, and the model discards the two diffusive (boundary-layer) roots by construction. That is what makes it the *bulk* reference — and what §0 claim 7 leaves open. **Anchor,** *demonstrated:* at D = 0 it returns **0.149310274** against the `ds_increment` zero 0.1493125296, a **−2.26 × 10⁻⁶** baseline offset (0.012 % of ΔM), carried explicitly in every table.

### 1.3 Its external calibration is 3.1 %, and that is the band on the bulk row

*in-model for the model half; **quoted** for the reference values, which 07-22 §3 produced with a modified solver that neither this work nor any check or assessor seat re-ran (Limitation 8b) [check 1].* At N = 480, `cfl` = 0.4, adding a physical DC ν₀ = 1.5270489934 × 10⁻² momentum-only diffusion:

| | released baseline | + physical DC ν₀ | shift |
|---|---|---|---|
| 07-22 §3, augmented **solver** (*quoted*) | 0.15884 | **0.18063** | +2.1790 × 10⁻² (+13.72 %) |
| bulk-only model, here (*demonstrated*) | 0.158143 | **0.180614** | +2.2470 × 10⁻² (+14.21 %) |
| **model − solver** | **−6.97 × 10⁻⁴** | **−1.63 × 10⁻⁵** | **+6.80 × 10⁻⁴ (3.1 %)** |

The advertised 1.6 × 10⁻⁵ agreement of the augmented *value* is the near-cancellation of a −6.97 × 10⁻⁴ baseline offset against a +6.80 × 10⁻⁴ shift offset. Had the absolute shifts been equal the model would read 13.78 %, so **baseline explains 0.06 pp of the 0.49 pp gap** and the rest is a genuine **3.1 %** disagreement in the shift [check 1, check 2]. The baseline offset is exactly what §4 row D requires: the released solver at (480, 0.4) sits +6.90 × 10⁻⁴ above the model (clamps 4.384 + splitting 0.143 + remainder 2.378 × 10⁻⁴, est −3.9 × 10⁻⁷), and 07-22's augmented solver keeps those same released clamps.

**This 3.1 % is the band carried on §4's bulk row**, which is why only **bulk + remainder = 95.02 %** is quoted. It does **not** attach to the iso-`ν_num` pair numbers of §3.3: those are *differences* across a matched-`ν_num` pair in which the model's fractional error largely cancels, and **+5.02 × 10⁻⁴** was independently measured at +5.0195 × 10⁻⁴ from a second construction *(🌊 Kinetic r1)*.

### 1.4 The factor is exactly 2, and the cavity departure is the closure

*demonstrated (identity + numerics).* For q_t + A q_x = S q + D q_xx at real k, the two eigenvalues of (−ikA + S − k²D) have real parts whose **sum** is shifted by exactly −k²·tr D. A momentum-only viscosity ν ∂ₓ²u, in the conserved vector about (1, M), is ν[[0, 0], [−M, 1]] — trace **ν**. Both ν·I and the full LF matrix at the same ½ tr D = ν have trace **2ν**. **Ratio exactly 2, for any M, any relaxation, any anisotropy.** Independent bulk dispersion at k = π returns the branch-sum ratio **2.000000000000** at every M ∈ {10⁻⁴, 0.05, 0.10, 0.149313, 0.20, 0.30}, with the DS relaxation on and off, at ν = 10⁻²/10⁻³/10⁻⁴; per branch it is exactly 2.000000000 for ν·I and 1.942269 / 2.057731 for D_LF at M = 0.149313 — the eigenvector projection l±·D r±/(l±·r±) is ν on both branches for ν·I and ν/2 on both for the momentum-only matrix. **This is the whole of the factor 2. An identity keeps no falsifier.**

The DS **cavity** is a different object, and its M-dependence is the closure, not the bulk. *in-model, mechanism open:*

| M | full D_LF / mom-only | ν·I / mom-only | ν∂ₓ²δm / mom-only (**same trace**) |
|---|---|---|---|
| 10⁻⁴ | 1.999976 | 1.999976 | 1.999976 |
| 0.05 | 1.987413 | 1.984035 | 2.000923 |
| 0.10 | 1.972493 | 1.960469 | 2.027185 |
| **0.149313** | **1.954490** | 1.930864 | 2.077372 |
| **0.20** | 1.932098 | **1.895251** | 2.153551 |
| 0.30 | 1.876161 | 1.814706 | 2.375367 |

Column 3 is decisive: a comparator with the *same trace* — hence the same bulk factor of exactly 2 — moves the cavity ratio the **other** way. The departure is produced by the **closure**, a boundary-value problem whose two branches carry unequal complex k (k₊²/k₋² ≈ ((1+M)/(1−M))², spanning 1.00 → 3.45 here) entering the two inviscid wall conditions differently for the two comparators; with the relaxation switched off it survives but halves at the top (1.995956 → 1.880350 on the ν·I column). Empirically (2 − r)/(((1+M)/(1−M))² − 1) = 0.0720 / 0.0801 / 0.0838 / 0.0838 / 0.0757 at M = 0.05 … 0.30, constant to ±8 %. **Which part of the closure carries it is open.** On thresholds rather than damping the comparison gives 1.9853 (N = 240), 1.9697 (480), 1.9647 (720), 1.9936 (`cfl` = 0.2), 1.9970 (`cfl` = 0.5).

**Why the registered band is [1.85, 2.10] and stops at M ≤ 0.20 — a deliberate limit** *(🧵 Fabric, 🌊 Kinetic, both rounds)*. The band is set from **the model's own measured M-dependence over the scoped range**, *not* from §1.3's 3.1 % calibration: that calibration is of the model's *shift response* against an augmented solver and largely cancels in a same-model **ratio of two shifts** computed inside one model at one cell — the argument §3.3 makes for the iso-`ν_num` differences. Disclosed, because it is the tightest point: **M = 0.20 sits only 2.39 % above the floor** (1.895251). At M = 0.30 the column reads 1.814706 and would fire.

**The threshold-matched crossover, with the object named.** The momentum-only ν₀ threshold in this model is **0.1711265**; the grid at which LF matches it **inside the same model** is **N\* = 199.3**, against the coefficient crossover 100.34 — a conversion factor of 1.99, the closed-form 2. **But 199.3 is bulk-only-vs-bulk-only** and omits by construction the clamp (4.83 %) and remainder (2.60 %) terms the released solver carries. Matching the **measured** ladder gives **N ≈ 216** (217.2 on this note's own fit parameters [check 1]); matching total shifts gives **214**. *in-model.* **Corroboration, stated:** an independent re-implementation returns **199.26 / 216.25 / 214.03** with ν₀ threshold **0.17112650** and μ = **9.0563370 × 10⁻³** *(🌊 Kinetic r2)*, and a second matched the cavity and split tables to all quoted digits *(🌊 Kinetic r1)*. See Limitation 3.

## 2. The exact linearized operator, and the two clamp substitutions

Validated against its source before use: *demonstrated,* l_a = **0.910958** (07-12-boundary-factor: 0.910958), line 0.244513 (0.244513); l_p = **0.724999** (0.724999), line 0.247862 (0.247862); M_th,lin(240) = **0.168764** (0.168764); M_th,lin(480) = **0.158834** (0.158834). *(Four promoted notes are dated 07-12; every citation here carries the filename, because "07-12 §7" and "07-12 App. B" are different notes [check 2].)*

**What the released ghost closures are** (*in-model — a reading of `solver.py`:48–53*). With N cells of width Δx on [0, 1], centres at (j−½)Δx and ghosts at −Δx/2 and 1+Δx/2, the walls sit at the faces:

| end | condition | where the code imposes it | order |
|---|---|---|---|
| source | δh = 0 (`H[0] = h_left`) | at the **ghost centre**, x = −Δx/2 | **first** |
| source | ∂ₓδu = 0 (`HU[0] = h_left*(hu[0]/h[0])`) | at the face, x = 0 | second |
| drain | δm = 0 (`HU[-1] = drain_current`) | at the **ghost centre**, x = 1+Δx/2 | **first** |
| drain | ∂ₓδh = 0 (`H[-1] = h[-1]`) | at the face, x = 1 | second |

**Which promoted sentence this refines, stated because a reader will collide with it [check 2].** 07-12-effective-loop §1 reads "source: density clamped, velocity zero-gradient; drain: momentum clamped, density zero-gradient (both first-order)". On the reading "**both boundaries** are first order" the table **agrees** and adds which of each end's conditions makes it so; on the reading "**both conditions** at each end" it **corrects** it. The first is taken to be intended and only the refinement is claimed.

So the scheme's first-order boundary error is **exactly the placement of the two Dirichlet clamps**, and the fix is one line each: mirror them about the face (δh₀ = −δh₁; δm_{N+1} = −δm_N). In block form the released closures are S = [[0,0],[−M,1]], D_gh = [[1,0],[0,0]]; the mirrored ones S = [[−1,0],[−2M,1]], D_gh = [[1,0],[0,−1]]. **Prior art [check 1, check 2]:** `grep` over `notes/` for "ghost cent", "wall face", "mirror", "first-order boundary" returns nothing on point; the diagnosis and the substitution appear new, and the operator is credited to 07-12-boundary-factor. Three controlled substitutions inside the same operator: **mirror** (both clamps → the clamp share), **mirror_src / mirror_drn** (one at a time → the drain/source split), **exact relaxation** (replace the released explicit-Euler post-step R = [[1,0],[sM, 1−s]] by the exact ODE solution over Δt, R = [[1,0],[M(1−e^{−s}), e^{−s}]] → the splitting share). Moving both clamps to the face costs **9.396 × 10⁻⁴** at N = 240 (source 2.740, drain 6.657 × 10⁻⁴).

**The lattice, evaluated at every point.** *demonstrated.* Over the 9 × 5 rectangle N ∈ {120, 150, 180, 240, 300, 360, 480, 720, 960} × `cfl` ∈ {0.2, 0.25, 0.3, 0.4, 0.5} the drain/source ratio **decreases monotonically in both N and `cfl`**, from **5.756 at (120, 0.2)** to **2.078 at (960, 0.5)**, passing 4.335 (150, 0.2), 4.300 (120, 0.25), 3.687 (180, 0.2), 3.643 (120, 0.3), 3.081 (240, 0.2), **2.430 at the shipped cell**. The four points the session listing skipped for cost are now computed rather than inferred *(🧵 Fabric r1)* — **2.218 (720, 0.25), 2.179 (720, 0.30), 2.103 (720, 0.50), 2.161 (960, 0.25)** — all inside [2.0, 5.8] and inside the clamps/Δx span, all preserving monotonicity. **The extremum is the corner because every point was computed, not because a trend was extended into the gaps.**

**Additivity, restated over the sampled lattice** *(🌊 Kinetic, ⚛️ Quanta r1)*. The two single substitutions are additive to a **worst residual of −4.916 × 10⁻⁶ at (120, 0.2)** — **4.5× the ≤ 1.1 × 10⁻⁶ bound that holds only over the eleven measured cells** (largest there at J) — and 0.17 % of the combined term; then −2.956 × 10⁻⁶ (120, 0.25), −1.781 × 10⁻⁶ (150, 0.2), −1.056 × 10⁻⁶ (120, 0.4), −1.544 × 10⁻⁷ (240, 0.2), +1.074 × 10⁻⁷ (240, 0.4). **And the disclosure that matters:** (120, 0.2) is simultaneously the drain/source extremum, the endpoint of §0 claim 6's band, and cell M of the collapse law — **the corner the rescoping leans on is the worst-conditioned point on the lattice.** The ratio 5.756 is untouched by this: it is computed from the two *single* substitutions, while the residual is the disagreement between their sum and the *joint* substitution, which the ratio never uses. What degrades at the corner is the licence to speak of "the clamp term" as one quantity decomposable into two.

**Scaling, quoted as a lattice result.** clamps/Δx spans **0.2026 (960, 0.5) … 0.3441 (120, 0.2)** — first order in Δx with a `cfl`-dependent drift (at N = 240: 0.2513 at `cfl` = 0.2, 0.2213 at 0.5). A pure geometric reading — the clamps sitting Δx/2 outside their walls lengthen the cavity by Δx, δM = 0.15400·Δx — captures **68.3 %** at the shipped cell and **44.8 %** at (120, 0.2); the rest is the discrete reflection structure 07-12-boundary-factor's quartic describes, not separated further. splitting/Δt is 0.0229 … 0.0255 across the eleven measured cells. **Which quantities are scanned and which are single points** *(🌊 Kinetic r2)*: the drain/source span and the additivity maximum are **scanned maxima over 45/45 operator points**; the clamps/Δx floor 0.2026 and the drain/source minimum 2.078 both sit at **(960, 0.5)**, the most expensive cell, computed once here and re-measured by no round-1 or round-2 seat that reports.

## 3. Measurement

### 3.1 The estimator, the widened bracket, and its interpolation bias

`run_all.measure_Mth_num` interpolates the **first sign change** of `solver.growth_rate` over `linspace(1.05, 1.30, 8)·M_th_353K` at `n_roundtrips = 90`. That bracket does not survive this study. The estimator is kept and the bracket widened:

> **Widened bracket, released spacing.** Nodes x_i = 1.05 + i·(0.25/7) for *integer* i, including i < 0 and i > 7 (`np.linspace(1.05,1.30,8)` verbatim for 0 ≤ i ≤ 7). Walk down from a start index to a negative node, then up to the first non-negative one; interpolate linearly between that straddling pair, exactly as the released code does. **The node spacing, and therefore the estimator's own interpolation bias, is unchanged.**

**Driver validation (nothing below is used until these pass).** *demonstrated:* `run_all.measure_Mth_num()`, the full released 8-node scan, the widened scan at nodes (2, 3) and `results.json`'s `M_th_num` are all **0.16894319463373791**, identical. The widened scan reproduces the full released scan at cell A on all 8 seeds (identical median, sd and range) and at cell B on seeds 1–2, sign pattern `[0,0,0,1,1,1,1,1]` at both. Both check agents reproduced this independently, one with a driver written from `solver.py` semantics rather than from the listing.

**Both released-bracket failures, with their prior art.** *demonstrated.* At `cfl` = 0.2, N = 240 the root sits **above** the released ceiling (0.1912244214 at nodes (7, 8), **+0.0084 %** above 0.19120833333), and the released eight-node scan at 90 round trips returns **`nan` at seeds 3 and 7** (node-7 growth −2.2414 and −3.2157 × 10⁻⁵) — **25 % of seeds fail already at the short record**, which *extends* [`2026-08-06`](2026-08-06-mth-num-record-length-and-fit-convention.md) §4.2 rather than merely confirming it. Seed 1 = 0.1911599846297388 (node-7 growth +8.4799 × 10⁻⁵) reproduces 08-06 §4.2 exactly; that note's unreproduced "0.036 %" is its **seed-4** draw (0.0361 % here, 0.0253 % at seed 1) [check 2]. At N = 960, `cfl` = 0.4 the root sits **below** the released floor (0.1540090045 at nodes (−1, 0)); that failure is **substantially 08-02 prior art** — its §1/§4 already registers `M_th_num_N960_widened` and "put a number on it" — and what is new is only the 240-round-trip eight-seed median at a different widening convention.

**The interpolation bias, measured at three cells rather than one** *(🌊 Kinetic r1)*. *demonstrated:* released two-point linear interpolation against a least-squares quadratic through nodes (i−1 … i+2), eight seeds, 240 round trips — **A (240, 0.4), nodes 2–3, inside the bracket: −5.53 × 10⁻⁶** (reproducing the −5.66 × 10⁻⁶ obtained at the session's own quadratic convention); **G (240, 0.2), nodes 7–8, at the ceiling: −8.90 × 10⁻⁶**; **M (120, 0.2), nodes 16–17, far outside: +7.36 × 10⁻⁶**. **Outside the bracket the bias is not unbounded — it is O(10⁻⁵) — but it is not common-mode either: it changes sign and grows.** At G the per-seed spread runs −1.48 … +1.83 × 10⁻⁵, comparable to that cell's own range. **Disclosed, not glossed: cell K (960, nodes −1, 0) was not measured** — four node evaluations at eight seeds there is ≈ 50 min of solver time, spent instead on M. K's error is already the second largest in §3.2, so a bias measurement there would be informative and is left a **named gap** rather than covered by inference. **Where the bias does not bite:** within each iso-`ν_num` set both members use the same node spacing **and** land in the same node interval (A/B/C at nodes 2–3, D/E at 0–1), so it is common-mode and cancels in the pair difference.

### 3.2 The fifteen cells

All at **`n_roundtrips` = 240, seeds 1–8, `growth_rate`'s own fit convention (`nb` = 40 log-RMS bins over the last 60 % of the trace)**; M̄ is the eight-seed median, sd is `statistics.pstdev` (08-06 §2's convention). M_th,lin is the spectral-radius-1 crossing of the exact operator, **zero free parameters**; error = M̄ − M_th,lin.

| cell | N | `cfl` | nodes | **measured M̄** | sd | M_th,lin | **error** | /0.443·sd |
|---|---|---|---|---|---|---|---|---|
| **A** | 240 | 0.400000 | 2, 3 | **0.1687658795** | 5.360e−6 | 0.16876409 | **+1.79e−6** | 0.8× |
| **B** | 480 | 0.213755 | 2, 3 | **0.1680689399** | 1.095e−5 | 0.16805861 | +1.03e−5 | 2.1× |
| **C** | 720 | 0.144494 | 2, 3 | **0.1678627280** | 4.592e−6 | 0.16785936 | +3.37e−6 | 1.7× |
| **D** | 480 | 0.400000 | 0, 1 | **0.1588334587** | 3.617e−6 | 0.15883385 | −3.9e−7 | 0.2× |
| **E** | 960 | 0.213929 | 0, 1 | **0.1585121120** | 9.704e−6 | 0.15850945 | +2.67e−6 | 0.6× |
| **F** | 720 | 0.400000 | 0, 1 | **0.1556041775** | 1.228e−5 | 0.15561613 | −1.20e−5 | 2.2× |
| **G** | 240 | 0.200000 | **7, 8** | **0.1912244214** | 1.456e−5 | 0.19123092 | −6.50e−6 | 1.0× |
| **H** | 240 | 0.300000 | 4, 5 | **0.1761747951** | 4.775e−6 | 0.17618079 | −5.99e−6 | 2.8× |
| **I** | 240 | 0.500000 | 1, 2 | **0.1642730737** | 1.414e−5 | 0.16425247 | +2.06e−5 | 3.3× |
| **J** | 120 | 0.400000 | 6, 7 | **0.1900370478** | 2.937e−6 | 0.19002573 | +1.13e−5 | **8.7×** |
| **K** | 960 | 0.400000 | **−1, 0** | **0.1540090045** | 4.751e−6 | 0.15402374 | −1.47e−5 | **7.0×** |
| **L** | 360 | 0.400000 | 1, 2 | **0.1621003583** | 5.364e−6 | 0.16209671 | +3.65e−6 | 1.5× |
| **M** | 120 | 0.200000 | **16, 17** | **0.2416750895** | 8.465e−6 | 0.24167896 | **−3.87e−6** | 1.0× |
| **P** | 300 | 0.400000 | 1, 2 | **0.1647615624** | 1.389e−5 | 0.16474053 | **+2.10e−5** | **3.4×** |
| **Q** | 240 | 0.350000 | 3, 4 | **0.1719432637** | 4.191e−6 | 0.17194652 | −3.26e−6 | 1.8× |

Eight-seed **ranges**, in row order: 1.669 / 2.763 / 1.560 / 0.964 / 2.272 / 3.464 / 4.478 / 1.530 / 4.494 / 0.863 / 1.548 / 1.825 / 2.533 / 4.051 / 1.430 × 10⁻⁵. **14 of 15 errors sit inside their own cell's range**; J is the only miss, at 1.31×.

**A–K** were measured here and re-executed independently by check agent 1 (≈ 2.5 h of solver time), reproducing to every quoted digit in median, sd **and** range, node pairs included; cell A was re-measured again by two round-1 seats, and A, D, F reproduce 08-06 §2's three published 240-round-trip rows exactly. **G, K and M need the widened bracket**; every other straddling pair lies inside the released 8 nodes.

**Four cells are out-of-sample, from three parties, all adopted with credit under standing rule 5 and all re-measured here before adoption.** **L** (360, 0.4) [check 1] and **M** (120, 0.2) [check 2] came from the pre-publication checks — M a deliberate attack at the corner of the scope, where ΔM is 4.7× the shipped cell. **P** (300, 0.4) and **Q** (240, 0.35) came from the **round-1 🧵 Fabric seat**; both medians reproduce to all ten quoted digits and both operator values to all eight, and `cfl` = 0.35 is a rung no cell had sampled. *(Letters N and O are skipped: N is the grid symbol. One convention split, disclosed: rows P and Q carry the divisor-(n−1) sd, the round-2 rework's adjudicated normalization; §7's listing computes every other row's sd with `pstdev` (divisor n), which for these two gives 1.299 × 10⁻⁵ and 3.921 × 10⁻⁶ — smaller by exactly √(7/8) — and puts P at 3.6× rather than 3.4×. Medians, ranges and errors are unaffected, as is the registered tolerance.)*

### 3.3 The iso-`ν_num` pairs

Pairs are built by solving `ν_num` = Δx·g(`cfl`, M) for the partner `cfl` at a reference M near the expected common root; the residual mismatch at the *measured* medians is quoted.

| pair | Δx ratio | `ν_num` mismatch | measured difference | larger 8-seed range | ratio | bulk-only predicts | **non-bulk part** |
|---|---|---|---|---|---|---|---|
| **A ↔ B** (240, 0.400) ↔ (480, 0.213755) | 2 | +0.051 % | **+6.9694e−4** | 2.763e−5 | **25.2×** | +1.9500e−4 | **+5.019e−4** |
| **A ↔ C** (240, 0.400) ↔ (720, 0.144494) | 3 | +0.065 % | **+9.0315e−4** | 1.669e−5 | **54.1×** | +2.3392e−4 | **+6.692e−4** |
| **D ↔ E** (480, 0.400) ↔ (960, 0.213929) | 2 | +0.028 % | **+3.2135e−4** | 2.272e−5 | **14.1×** | +8.7338e−5 | **+2.340e−4** |

> **Verdict.** *demonstrated.* Every pair disagrees by far more than both members' eight-seed ranges — **25.2× / 54.1× / 14.1×** the larger member's range. The pure-viscosity reading does not hold, and **the test was never open**: [`2026-07-12-effective-loop-von-neumann.md`](2026-07-12-effective-loop-von-neumann.md) §1 already reads the ghost closures as first order and its §7 already pre-registers a boundary loss ∝ Δx, so an iso-`ν_num` pair — which holds `ν_num` fixed while moving Δx 2–3× — was guaranteed to break the collapse. **Nor was it pre-registered in the permanent record:** `grep -rn` over `notes/`, `INDEX.md`, both `results.json`, `docs/`, `papers/`, `agents/` and `ROADMAP.md` returns no registration of any iso-`ν_num` collapse, and `ν_num` appears only in 07-22. **What is new is (i) the magnitude** — the measured non-bulk share **+5.02 × 10⁻⁴** at Δx = 1/240 relative to 1/480, 2.6 % of ΔM per halving — **and (ii) the method**, moving N and `cfl` together to break a degeneracy a fixed-`cfl` ladder cannot.

The exact operator, with no free parameter, predicts those gaps as **+7.055 / +9.047 / +3.244 × 10⁻⁴** against the measured **+6.969 / +9.032 / +3.214 × 10⁻⁴**. The confounds at A↔B: clamp placement ∝ Δx, **+4.825 × 10⁻⁴** (96 % of the non-bulk gap, resolved by the mirrored substitution); splitting ∝ Δt, **+2.14 × 10⁻⁵** (resolved by the exact-relaxation substitution); LF dispersion / higher-order interior, **+6.5 × 10⁻⁶** (bounded, not separated — §0 claim 7); estimator + nonlinearity, **−8.5 × 10⁻⁶** (bounded by the eight-seed ranges); the `cmax` pad, folded into `ν_num` by construction. **Sum +5.017 × 10⁻⁴ against the measured +5.019 × 10⁻⁴.**

## 4. The decomposition, and its reconciliation

ΔM splits into terms summing to it **exactly** (checked to 10⁻¹² per row): "bulk" = the bulk-only model at D_LF minus the same model at D = 0; "clamps" = released minus mirrored closure in the exact operator; "split" = released explicit-Euler minus exact relaxation; "other" = the rest of (M_th,lin − M_bulk); "est" = M̄ − M_th,lin; the common model baseline −2.726 × 10⁻⁶ is listed once.

**Bulk and remainder are printed as one quantity** *(🌊 Kinetic, ⚛️ Quanta r1)*. Their internal division sits inside the bulk-only model's own **3.1 %** external calibration (§1.3): 3.1 % of the bulk term is **5.574 × 10⁻⁴**, **1.10× the entire 5.059 × 10⁻⁴ remainder**. Only the merged term is operator-anchored, and it is what the registered key carries. The split's *arithmetic* is not in question — recomputed twice, once from the printed clamp and splitting terms and once from independent operator solves, agreeing to the fourth digit (2.8141 vs 2.8140 % at A) — its *calibration* is.

| cell | ΔM | **bulk + remainder** | % | clamps | % | split | % | est |
|---|---|---|---|---|---|---|---|---|
| **A** (240, 0.400) | 1.9453e−2 | **1.8485e−2** | **95.02** | 9.396e−4 | **4.83** | 2.91e−5 | 0.15 | +1.8e−6 |
| B (480, 0.2138) | 1.8756e−2 | 1.8284e−2 | 97.48 | 4.571e−4 | 2.44 | 7.73e−6 | 0.04 | +1.0e−5 |
| C (720, 0.1445) | 1.8550e−2 | 1.8243e−2 | 98.34 | 3.023e−4 | 1.63 | 3.48e−6 | 0.02 | +3.4e−6 |
| D (480, 0.400) | 9.5205e−3 | 9.071e−3 | 95.28 | 4.384e−4 | 4.61 | 1.43e−5 | 0.15 | −3.9e−7 |
| E (960, 0.2139) | 9.1991e−3 | 8.979e−3 | 97.61 | 2.161e−4 | 2.35 | 3.80e−6 | 0.04 | +2.7e−6 |
| F (720, 0.400) | 6.2912e−3 | 6.011e−3 | 95.54 | 2.858e−4 | 4.54 | 9.44e−6 | 0.15 | −1.2e−5 |
| G (240, 0.200) | 4.1911e−2 | 4.086e−2 | 97.49 | 1.047e−3 | 2.50 | 1.51e−5 | 0.04 | −6.5e−6 |
| H (240, 0.300) | 2.6862e−2 | 2.588e−2 | 96.33 | 9.717e−4 | 3.62 | 2.21e−5 | 0.08 | −6.0e−6 |
| I (240, 0.500) | 1.4960e−2 | 1.399e−2 | 93.48 | 9.223e−4 | 6.16 | 3.62e−5 | 0.24 | +2.1e−5 |
| J (120, 0.400) | 4.0724e−2 | 3.848e−2 | 94.49 | 2.175e−3 | 5.34 | 6.13e−5 | 0.15 | +1.1e−5 |
| K (960, 0.400) | 4.6960e−3 | 4.494e−3 | 95.71 | 2.119e−4 | 4.51 | 7.06e−6 | 0.15 | −1.5e−5 |

**The remainder is constrained but unidentified, and the constraints are on the residual, not on a mechanism.** *demonstrated for the behaviour, open for the mechanism.* Within an iso-`ν_num` set its **share of the bulk term** is constant to **0.26 %** on A/B/C (2.8140 / 2.8082 / 2.8067 % over a 3× change of Δx) and **0.83 %** on D/E, while the clamp term changes 3.1×. Two constraints, both *in-model* for the bulk-only model — and "other" is defined by subtraction and absorbs any Δt-dependent error in the clamp and splitting substitutions, the clamp term itself moving 12 % across the very `cfl` sweep that produces the exponent *(🌊 Kinetic r2)*: **Δx^0.014 at fixed `ν_num`**, which **excludes** a scheme truncation term (at fixed `ν_num`, Δt ∝ Δx² and the LF dispersive coefficient falls 8.3× over the same 3× refinement while the residual falls 1.016×); and **`ν_num`^{1.12 ± 0.02} at fixed Δx = 1/240** over a sampled 2.9× range in `ν_num` (control: bulk ∝ `ν_num`^1.007; the four-point fit shows visible curvature, relative residuals +1.04 / −1.38 / −0.87 / +1.23 % against ±0.4 % on the control) *(🌊 Kinetic r1; scatter 🧵 Fabric r2)*. A continuum viscous wall layer from the model's two discarded diffusive roots is a **named candidate consistent with the constraint**, neither adopted nor excluded: a *leading-order* wall layer is ν^{1/2}, but the model's wall conditions are inviscid and D is a regular O(ν) perturbation, so O(ν¹) is equally admissible. **Mechanism open.** **The first of key 1's three falsifiers for it is weak, and that is stated rather than hidden** *(🌊 Kinetic r1)*: at the pre-registered Δx-ratio-6 extension (N = 1440, `cfl` = 0.072871) other/bulk = **2.8058 %**, an A-family spread of **0.292 %** over the full ratio 6 — 19 % of the 1.5 % band. The "sampled maximum 0.82 %" the memo quoted is **0.83 %** at full precision and comes from the **D/E** family, which drifts 3.1× more in raw spread and 5.0× faster in exponent than the A/B/C family the prose leans on; whether that persists is unmeasured.

**The two factorizations, both printed** (cell A; μ = the bulk-only threshold shift of a **momentum-only** viscosity at Laplacian coefficient ν = ½ tr D_LF(240, 0.4, M) — matched on the coefficient, *not* on ½ tr, which is the point of §1.4 — **μ = 9.056337 × 10⁻³**):

```
Against the exact inviscid 0.149313 -- the numerics alone:

  2.14799  =  1.98526          x  1.02814             x  1.05083           x  1.00150     x  0.99995
              conserved-vector    interior remainder     the two DS clamps    splitting      estimator
              vs momentum-only                                                               + baseline

Against 07-22 sec2's 0.147083 -- the number its "~2.4x" table column is measured from:

  2.39418  =  0.24620  +  2.14799        B / mu = 2.229667e-3 / 9.056337e-3
  2.41376  =  0.24620  +  2.16756        using the registered single-seed M_th_num instead of M-bar
```

**Those multiplicative factors are ORDER-DEPENDENT** *(🌊 Kinetic r1; conditionality 🧵 Fabric r2)*. They are cumulative partial-sum ratios. The convention is stated: **bulk first — forced, because μ *is* a bulk quantity and comparing a clamp term to a momentum-only bulk shift is not a ratio anyone would quote — then remainder, clamps, splitting, estimator.** Enumerating all 24 orderings of the remaining four *given that convention*: clamps 1.05074 … 1.05226 (ln share 6.47 … 6.66 %), remainder 1.02670 … 1.02814 (3.45 … 3.63 %), splitting 1.00150 … 1.00162 (0.20 … 0.21 %), **mass invariant at 1.98526 / 89.68 %** (independent enumerations of the same object return 1.98526–1.98535, i.e. 89.68–89.70 %). Largest order-dependence anywhere: **0.19 pp**. **The invariance is conditional on the stated convention** — under a fully free ordering the first factor is not bulk/μ at all. **The order-free additive shares are the table above**, and the "refuted in size" verdict against 07-22 §2 rests on the one number that cannot move.

**Reconciliation, exact, with no open residual [check 1, check 2].** 2.39418 − 2.14799 = 0.24620 = B/μ. The dropped baseline B is **10.3 %** of the 07-22-referenced excess — larger than the 4.83 % clamp term and larger than every non-bulk term combined — which is why it has its own row rather than a convention sentence. Two independent readings of 07-22's "≈ 2.4×" agree with each other and with this: ν₀/`ν_num`(240) = **2.3920** (its own definition); the offset ratio against the same reference **2.39418** (median) / **2.41376** (shipped root); the bulk-only momentum-only shift ratio **2.4089**. The one thing 07-22's framing assumes that does *not* hold exactly is that the measured LF shift equals the full-ν₀ NS shift: ΔM/(ν₀ momentum-only shift) = **0.892**, not 1 — a separate true statement about a different pair of quantities, and **not** the mechanism behind the 0.24620 residual, which is additive and exact.

## 5. What the collapse law is, and what its number is not

**2.10 × 10⁻⁵ is a sampled maximum over the cells run. It is not a bound.** The previously registered 2.06 × 10⁻⁵ was exceeded at **(300, 0.4)** — an in-scope cell at the same protocol — on an assessor's first independent try. **The house rule on lattice extrema quoted as frontiers, which this work applied to the drain/source band and the clamps/Δx range, applies to a registered key too, and the memo did not apply it there** *(🧵 Fabric r1)*. Over the fifteen cells: sampled maximum **2.10 × 10⁻⁵**, median |error| **6.0 × 10⁻⁶**, **14 of 15** inside their own eight-seed range; on the stricter median-sampling-error bar (0.443·sd, 08-06 §3's convention) J and K sit 8.7× and 7.0× out, P enters at 3.4×, and **every other cell is within 3.4×**. The registered **tolerance** remains the absolute **5 × 10⁻⁵** — the largest error is **42 %** of it, cleared by ≥ **2.4×** everywhere.

**Most of that error column is finer than the estimator convention can resolve, and this is said plainly** *(🌊 Kinetic r1; ⚛️ Quanta r2)*. §3.1 measures the released estimator's linear-vs-quadratic convention-dependence at **−5.53 × 10⁻⁶ even inside the bracket at cell A** — 3.1× the collapse error there and comparable to the median |error| of 6.0 × 10⁻⁶. Two consequences:

- **At cell M**, the adversarial corner, the estimator reads **high by ≈ +7.36 × 10⁻⁶**; correcting for it moves the error from **−3.87 × 10⁻⁶ to ≈ −1.12 × 10⁻⁵** — still inside the 5 × 10⁻⁵ falsifier by 4.4× and inside the cell's own range, but **three times larger than the raw number**. The phrase "the strongest single piece of evidence" is **withdrawn** for **"the collapse law's most adversarial confirmation, at an agreement finer than the estimator convention can resolve."** *And this is why the sign mattered:* the true error at M is **negative** and the bias positive, so bias correction makes the discrepancy **grow** to −1.12 × 10⁻⁵; the mis-signed +3.87 × 10⁻⁶ would have made it appear to **shrink** to −3.5 × 10⁻⁶. The sign was printed wrong in six places in the published memo, found by no assessor, and is corrected here everywhere including inside the registered key.
- **At cell P**, which *sets* the sampled maximum and sits at nodes (1, 2) inside the released bracket, that bias was **not measured**. If it is comparable to cell A's, the sampled maximum is ≈ 2.6 × 10⁻⁵ rather than 2.10 × 10⁻⁵. **The sampled maximum is convention-dependent at the same level now applied to cell M**, and that is registered with the key rather than left implicit.

**What the law is not common-mode in, and what it is** *(🧵 Fabric r1)*. *demonstrated by source read:* `solver.py`:29–34 `_setup` computes `s = plasmon_speed()`, `tau = C.tau(T)`, `L = cell_length(s)`, `tau_n = tau*s/L`, and the operator's only physical input is that same `tau_n` from the same `constants.py` / `ds_cell.py`. A change to `constants.py` moves both sides together: the law **catches scheme regressions** (closure, relaxation, the `cmax` pad, `cfl`, the LF flux) and **does not catch `constants.py`.**

**The five-rung ladder, and why it is not the regression to use.** *demonstrated.* Fitting M(N) = M_∞ + A·N^(−p) on the `cfl` = 0.4 ladder (N = 120/240/480/720/960; ratios 2, 2, 1.5, 4/3), the **unrestricted** optimum is M_∞ = 0.149649 (measured) / 0.149684 (operator) at p = **1.0685 / 1.0701** — **+0.22 % above** the exact inviscid, *worse* conditioned than the three-rung 0.14947. (An earlier "free three-parameter fit, M_∞ = 0.149300" was a scan grid **capped** at the exact inviscid value with the objective still falling at the cap; found on re-execution here, flagged by no checker and no assessor.) **What survives is the exponent:** 1.036–1.070 on five rungs and three refinement ratios under every scan convention tried, inside 08-06's [0.9, 1.2], with measured and operator ladders agreeing to 0.15 %; and 08-06's own three-rung bisection on 240/480/720 reproduces its registered **p = 1.0433** and intercept 0.14947 exactly on these medians. **Scoping, because 08-06's falsifier is specific:** it asks for a fourth rung at a third refinement ratio *below* the bracket ceiling of (860, 920]; the N = 960 rung is below the released bracket **floor** and needed the widened bracket, so **this does not discharge that falsifier as written.**

**Still pre-registered, unrun by anyone.** `M_th_num_N1440_isonu_A` = **0.16768 ± 0.00008** at `cfl` = **0.072871** — the iso-`ν_num` partner of cell A at Δx ratio 6. The decisive form is the **gap** against cell A, predicted at **+1.084 × 10⁻³**, ≥ 25× that cell's eight-seed range; *refuted as a bulk-only reading if the gap falls below the larger of the two ranges; refuted as this note's account if it lands outside +0.98 … +1.19 × 10⁻³.* The **operator-and-bulk-model side** has now been computed (15 min against ≈ 2 h for a census): M_th,lin(1440, 0.072871) = **0.16767997**, reproducing the pre-registered value to eight digits from an independently written construction, predicted gap +1.084120 × 10⁻³. **That is a reproduction of the prediction, not a discharge of it** — its content is the **measured** threshold, and nobody has run it.

## 6. Registered keys

    M_th_num_excess_decomposition_pct
        = bulk 95.02 / clamps 4.83 / splitting 0.15 / estimator 0.01 (percent of
          Delta M = M_bar(240, 0.4) - 0.149313 = 1.945288e-2), at N = 240, cfl = 0.4,
          against a common model baseline of -0.014 %.
          M_bar is the EIGHT-SEED MEDIAN at n_roundtrips = 240 and is NOT the registered
          M_th_num = 0.16894319463373791 (a seed-1, 90-round-trip draw, whose own excess
          is 1.963019e-2, 0.9 % larger); the two are kept apart deliberately.  Against
          07-22 sec2's own reference 0.147083333 the same cell reads baseline 10.28 /
          bulk 82.92 / remainder 2.33 / clamps 4.33 / splitting 0.13 / estimator 0.01,
          where "baseline" is the small-M linearization of Eq. (3) (0.149313 -
          0.147083333 = 2.229667e-3) and is not a scheme artifact at all.
          "bulk" is the MERGED leading LF diffusion MATRIX D = (dx^2/2dt)(I - nu^2 A^2)
          plus an interior remainder.  The internal division of that 95.02 % --
          92.42 % matrix + 2.60 % remainder -- is NOT REGISTERED and must not be quoted
          to four significant figures: it sits inside the bulk-only model's own external
          calibration error, demonstrated at 3.1 % on the shift (sec 1.3), i.e. 5.574e-4,
          which is 1.10x the entire 5.059e-4 remainder term.  Only bulk + remainder is
          operator-anchored.
          The remainder is a RESIDUAL DEFINED BY SUBTRACTION and absorbs any dt-dependent
          error in the clamp and splitting substitutions.  It is NOT a scheme truncation
          term -- excluded, because it is dx-INDEPENDENT at fixed nu_num (apparent order
          0.014, holding across a 6x refinement) while the LF dispersive coefficient falls
          8.3x over 3x.  It scales as nu_num^(1.12 +- 0.02) at fixed dx = 1/240 over a
          sampled 2.9x range in nu_num (control: bulk ~ nu_num^1.007).  BOTH constraints
          are IN-MODEL for the bulk-only model and constrain the RESIDUAL, not a
          mechanism.  A continuum viscous wall layer from the model's two discarded
          diffusive roots is a NAMED CANDIDATE consistent with the constraint and is
          neither adopted nor excluded (a leading-order wall layer would be nu^(1/2), but
          the model's wall conditions are inviscid and D is a regular O(nu) perturbation,
          so O(nu^1) is equally admissible).  MECHANISM OPEN.
          "clamps" = moving BOTH released Dirichlet ghost clamps (source dh = 0, drain
          dm = 0) from the ghost centre to the wall face in the exact linearized one-step
          operator; drain 3.42 %, source 1.41 %, ratio 2.430.  The two single
          substitutions are additive to a WORST RESIDUAL of -4.916e-6 at (N = 120,
          cfl = 0.2), scanned over all 45 points of the 9 x 5 lattice; the <= 1.1e-6
          figure holds only over the eleven measured cells.  That corner is
          simultaneously the drain/source extremum, the endpoint of the band below, and
          cell M of M_th_num_operator_collapse_max_err.
          "splitting" = replacing the released explicit-Euler post-step relaxation by the
          exact solution of the same ODE over dt.
        convention: plane = solver-internal (normalized h = 1, s = 1, L = 1); bias = the
          free-perturbation threshold itself, no drive; N = 240, dx = 1/240, cfl = 0.4
          (true Courant 0.292196, because cmax = 1 + |u0| + 0.2); T = 353 K, tau_n =
          3.39943342776204; seeds 1-8; n_roundtrips = 240; fit convention nb = 40 log-RMS
          bins over the last 60 % (growth_rate's own); bracket = released spacing 0.25/7,
          widened to integer node indices outside [0, 7] where needed (nodes 2,3 here --
          inside the released bracket).
        label: in-model for the three model shares (each a named substitution inside a
          named model); demonstrated for Delta M and for the estimator share.
        reproduction check (deterministic, NOT a falsifier): substituting the wall-face
          (mirrored) placement for the two DS clamps in the exact linearized operator at
          N = 240, cfl = 0.4 returns 4.83 % of Delta M, and the drain/source ratio over
          the sampled 9 x 5 lattice spans [2.078, 5.756].  An independent
          re-implementation returning anything else indicts one of the two
          implementations.  (Two independently rebuilt operators returned 4.83 %.)
        falsifier: an iso-nu_num pair at dx ratio >= 2, >= 8 seeds, >= 240 round trips,
          agreeing within the larger of the two eight-seed ranges (which would put the
          non-bulk share at zero); or a DIFFERENT second-order clamp placement (quadratic
          extrapolation through two interior cells rather than mirroring about the face)
          giving a threshold change outside [3 %, 7 %] of Delta M at that cell, or a
          drain/source split outside [2.0, 5.8] at a sampled cell.
        falsifier, the remainder specifically: other/bulk varying by more than 1.5 %
          within an iso-nu_num set (the sampled maximum is 0.83 %, on the D/E family,
          and the measured value at the pre-registered dx-ratio-6 extension is 0.292 %,
          so this clause is weak and is labelled so); OR an independent bulk model with
          the two diffusive roots RETAINED; OR the augmented-solver run of Limitation
          8(b).  The last two are the clauses with teeth.

    M_th_num_conserved_vector_damping_factor
        = 2 exactly in the bulk; 1.9853 on DS-cavity thresholds at the shipped cell;
          1.9545 on DS-cavity mode damping at M = 0.149313.
          BULK (exact, and this is the mechanism): for q_t + A q_x = S q + D q_xx the two
          acoustic eigenvalues' real parts are shifted, in sum, by exactly -k^2 tr D.  A
          momentum-only viscosity nu*d2u/dx2 written in the conserved vector is
          nu*[[0,0],[-M,1]], trace nu.  The LF matrix D_LF and nu*I at the same
          0.5*tr(D) = nu both have trace 2*nu.  Hence the ratio is EXACTLY 2 -- at every
          M, with or without the DS relaxation, at every nu, and independently of the
          anisotropy of D_LF.  Verified numerically at 2.000000000000 over M in
          {1e-4 ... 0.30} at nu = 1e-2/1e-3/1e-4.  Per branch the split is exactly 2 for
          nu*I (eigenvector projection l.D r/(l.r) = nu vs nu/2) and 1.9423/2.0577 for
          D_LF at M = 0.149313.
        convention: the comparator is matched on the LAPLACIAN COEFFICIENT nu, not on
          0.5*tr(D) -- the momentum-only matrix has 0.5*tr = nu/2, which is exactly the
          factor being reported.
          The cavity numbers use the continuum bulk-only model: the two physical roots of
          the D-perturbed quartic dispersion relation of the shallow-water system
          linearized about (h, u) = (1, M) with the momentum relaxation kept exactly,
          closed with the two INVISCID DS wall conditions dh(0) = 0, dm(1) = 0; tau_n =
          3.39943342776204 (353 K); D at N = 240, cfl = 0.4.  The model's own D = 0
          anchor is 0.149310274, i.e. -2.26e-6 from the exact inviscid 0.149313, carried
          explicitly in every table.
        label: demonstrated (identity + arithmetic) for the bulk factor 2; in-model for
          the cavity numbers.  The cavity ratios' departure from 2 at finite M (down to
          1.8147 at M = 0.30 for nu*I) is a property of the CLOSURE, not of the trace
          mechanism -- a same-trace comparator nu*d2(dm)/dx2 departs the other way, to
          2.3754 -- and its origin is OPEN.
        falsifier, bulk identity: NONE.  An identity cannot be falsified by a threshold
          measurement and no falsifier is offered for it.
        falsifier, cavity ratio: a direct augmented-solver measurement -- the threshold
          shift of an LF-ONLY run DIVIDED BY the shift of released LF plus a physical
          momentum-only nu at the same LAPLACIAN COEFFICIENT nu -- landing outside
          [1.85, 2.10] for any M <= 0.20.  (An earlier statement of this key had
          numerator and denominator INVERTED, which reads ~0.5 when the factor 2 holds;
          the direction above is the intended one.)  The band is set from the model's own
          measured M-dependence over the scoped range, NOT from sec 1.3's 3.1 %
          calibration, which is a calibration of the model's SHIFT RESPONSE and largely
          cancels in a same-model ratio of two shifts.  Disclosed: M = 0.20 is the
          tightest point, where the model's own nu*I column reads 1.895251, only 2.39 %
          above the floor; at M = 0.30 it reads 1.814706 and would fire, which is why the
          scope stops at 0.20 as a deliberate limit rather than an assumption.
          A measurement outside the band indicts the bulk-only model's CLOSURE (mechanism
          open), NOT the bulk trace identity.

    M_th_num_operator_collapse_max_err
        = 2.10e-5 -- a SAMPLED MAXIMUM over the cells run, EXPLICITLY NOT A BOUND.  The
          largest |M_th,lin(N, cfl) - measured eight-seed median| over FIFTEEN (N, cfl)
          cells spanning N in {120, 240, 300, 360, 480, 720, 960} and cfl in {0.144494,
          0.2, 0.213755, 0.213929, 0.3, 0.35, 0.4, 0.5}; attained at (N = 300, cfl = 0.4).
          The previously registered 2.06e-5 was exceeded there on the first independent
          in-scope try, by a round-1 assessor; the house rule on lattice extrema quoted as
          frontiers applies to this key too.
          Median |error| 6.0e-6; 14 of 15 cells inside that cell's OWN eight-seed range
          (the exception is N = 120, cfl = 0.4, at 1.31x its range).  On the stricter
          median-sampling-error bar (0.443*sd, 08-06 sec3's convention) two cells sit 8.7x
          (120, 0.4) and 7.0x (960, 0.4) out, (300, 0.4) enters at 3.4x, and the rest are
          within 3.4x.  The registered TOLERANCE is the ABSOLUTE 5e-5, which no cell
          approaches: the largest error is 42 % of it and it is cleared by >= 2.4x
          everywhere.
          ZERO free parameters: M_th,lin is the spectral radius = 1 crossing of the exact
          linearized one-step operator (07-12-boundary-factor App. B, re-validated to its
          published l_a = 0.910958, l_p = 0.724999, M_th,lin(240) = 0.168764,
          M_th,lin(480) = 0.158834).
          Eleven cells were measured in the session; FOUR were measured OUT OF SAMPLE by
          three other parties and are adopted with credit under standing rule 5:
          (360, 0.4) err +3.65e-6 by check agent 1; (120, 0.2) err -3.87e-6 by check agent
          2, a deliberate attack at the corner of the scope where Delta M is 4.7x the
          shipped cell; (300, 0.4) err +2.10e-5 and (240, 0.35) err -3.26e-6 by the
          round-1 Fabric seat, the latter at a cfl rung no cell had sampled.  A cell at
          cfl = 0.6 (|Delta| = 1.69e-5) is outside the scope and is not counted.
        CONVENTION-DEPENDENCE OF THIS VALUE, registered with it: the released estimator's
          own linear-vs-quadratic interpolation bias is -5.53e-6 at (240, 0.4) INSIDE the
          released bracket -- 3.1x the collapse error there and comparable to the median
          |error| of 6.0e-6 -- so most of the error column is finer than the estimator
          convention can resolve.  At (300, 0.4), which SETS this sampled maximum and sits
          at nodes (1,2) inside the bracket, that bias was NOT measured; if it is
          comparable to cell A's, the sampled maximum is ~2.6e-5.  At (120, 0.2) it WAS
          measured, at +7.36e-6, which moves that cell's error from -3.87e-6 to ~-1.12e-5
          -- still inside the tolerance by 4.4x and inside that cell's own eight-seed
          range.  The 5e-5 tolerance is untouched by all of this.
        convention: measurement = released measure_Mth_num estimator (first sign change +
          linear interpolation) on the released node spacing 0.25/7, bracket widened to
          integer indices outside [0, 7] at three cells (cfl = 0.2 at N = 240, above the
          ceiling; N = 960 at cfl = 0.4, below the floor; N = 120 at cfl = 0.2, nodes
          16,17); n_roundtrips = 240; seeds 1-8; nb = 40; window fraction 0.4; T = 353 K.
          Operator: tau_n = (300/353)/0.25, cmax = 1 + |M| + 0.2, 30 bisection steps on
          [0.10, 0.30].  sd is statistics.pstdev (divisor n), 08-06 sec2's convention, at
          every cell except (300, 0.4) and (240, 0.35), which are entered at the
          divisor-(n-1) value; the two differ by exactly sqrt(7/8) and nothing depends on
          it except that cell's 0.443*sd figure (3.4x vs 3.6x).
        label: demonstrated for the arithmetic and the comparison; in-model as a statement
          about the released NONLINEAR solver (the operator is linearized).
        falsifier: a further cell inside 120 <= N <= 960 and 0.2 <= cfl <= 0.5, at the
          same protocol, with |M_th,lin - eight-seed median| > 5e-5.

**Collision check.** All three names return no hits from `grep -rn` over `notes/`, `notes/INDEX.md`, `papers/`, `ROADMAP.md`, `fable-model-chain/` and `fable-model-quantum/` including both `results.json` — independently confirmed by both check agents, one extending the search to `docs/` and `tests/`. Existing `M_th_num_*` keys (`_N480`, `_N720`, `_N960_widened`, `_N960_widened_seed1`, `_convention`, `_growth_at_released_root`, `_inviscid_limit`, `_ladder_fitted_order`, `_record_length_shift_pct`) are distinct and untouched.

## 7. Listing

Self-contained; `fable-model-chain/` imported **unedited**; run from the repository root. This is the core and it generates every number the three keys carry. The session's remaining modes (the von Neumann reconstruction, the WP2 common-mode probe, the released-bracket 90-round-trip census, the ladder fits) are unchanged and live in [#108](https://github.com/ryoji-info/FableComputer/discussions/108).

```python
# -*- coding: utf-8 -*- ; python3 L.py [validate|bulk|analytic|lattice|cell T N cfl i0|all]
# Python 3.11.2 / numpy 2.4.6 / macOS arm64.  fable-model-chain/ imported UNEDITED.
import sys, math, cmath, statistics as st
sys.path.insert(0, 'fable-model-chain')
import numpy as np, constants as C, ds_cell as DS, kinetic as K, solver as SOL, run_all

s = DS.plasmon_speed(); L = DS.cell_length(s); tau = C.tau(C.Tcap)
Mth = DS.M_threshold(L, s, tau)                       # 0.14708333333333332
TAU_N = tau*s/L                                       # 3.39943342776204
NU0 = (C.vF**2 * K.tau_ee(C.Tcap)/4.0)/(L*s)          # 07-22's DC kinematic viscosity
INVISCID = 0.149313; MTHNUM = 0.16894319463373791
HDRM = 0.2                                            # solver.py's (uncommented) cmax pad
Z = np.zeros((2, 2))

def Amat(M): return np.array([[0.0, 1.0], [1-M*M, 2*M]])
def D_LF(N, cfl, M):                    # D = (dx^2/2dt)(I - nu^2 A^2)
    dx = 1.0/N; dt = cfl*dx/(1.0+abs(M)+HDRM); nu = dt/dx
    return (dx*dx/(2*dt))*(np.eye(2) - nu*nu*Amat(M)@Amat(M))
def nu_num_0722(N, cfl=0.4, M=Mth):     # 07-22's characteristic-averaged scalar
    dx = 1.0/N; cm = 1+abs(M)+HDRM; dt = cfl*dx/cm; pr = dx**2/(2*dt)
    return 0.5*(pr*(1-((1+M)*dt/dx)**2) + pr*(1-((1-M)*dt/dx)**2))
def g_of_cfl(cfl, M):                   # nu_num = dx*g(cfl, M); invert for the partner
    cm = 1+abs(M)+HDRM; return (cm/(2*cfl))*(1-(cfl/cm)**2*(1+M*M))
def Dmom(nu, M):   return nu*np.array([[0.0, 0.0], [-M, 1.0]])   # momentum-only
def Dmom_m(nu, M): return nu*np.array([[0.0, 0.0], [0.0, 1.0]])  # same-trace comparator

# --- BULK-ONLY MODEL: two physical branches + the two INVISCID DS wall conditions ---
def _det(w, M, D, tn=TAU_N):
    r = 1.0/tn
    W11 = np.array([D[0,0], 0+0j, -1j*w]);      W12 = np.array([D[0,1], 1j, 0+0j])
    W21 = np.array([D[1,0], 1j*(1-M*M), -M*r]); W22 = np.array([D[1,1], 2j*M, -1j*w+r])
    ks = np.roots(np.polysub(np.polymul(W11, W22), np.polymul(W12, W21)))
    ks = ks[np.argsort(np.abs(ks))][:2]; ph = []
    for k in ks:
        a = D[0,0]*k*k - 1j*w;                   b = D[0,1]*k*k + 1j*k
        c = D[1,0]*k*k + 1j*k*(1-M*M) - M/tn;    d = D[1,1]*k*k + 2j*k*M - 1j*w + r
        v1 = np.array([b, -a]); v2 = np.array([d, -c])
        v = v1 if np.linalg.norm(v1) >= np.linalg.norm(v2) else v2
        ph.append(v/np.linalg.norm(v))
    return ph[0][0]*ph[1][1]*cmath.exp(1j*ks[1]) - ph[1][0]*ph[0][1]*cmath.exp(1j*ks[0])
def omega(M, D, tn=TAU_N):              # secant on the mode determinant
    w0 = math.pi*(1-M*M)/2.0 + 0.05j; w1 = w0*(1+1e-4) + 1e-5j
    f0 = _det(w0, M, D, tn); f1 = _det(w1, M, D, tn)
    for _ in range(80):
        if abs(f1-f0) < 1e-300: break
        w2 = w1 - f1*(w1-w0)/(f1-f0); w0, f0, w1 = w1, f1, w2
        f1 = _det(w1, M, D, tn)
        if abs(w1-w0) < 1e-13: break
    return w1
def M_th_bulk(DofM, lo=0.05, hi=0.40, it=60):
    for _ in range(it):
        m = 0.5*(lo+hi); lo, hi = (m, hi) if omega(m, DofM(m)).imag < 0 else (lo, m)
    return 0.5*(lo+hi)

# --- EXACT linearized one-step operator (07-12-boundary-factor App. B) ---------------
def build_T(M, N, cfl, tn=TAU_N, relax="euler", closure="released"):
    dx = 1.0/N; dt = cfl*dx/(1+abs(M)+HDRM); nu = dt/dx; sd = dt/tn
    A = Amat(M); P = 0.5*(np.eye(2)-nu*A); Q = 0.5*(np.eye(2)+nu*A)
    if relax == "euler": R = np.array([[1.,0.],[sd*M, 1-sd]])
    else:                E = math.exp(-sd); R = np.array([[1.,0.],[M*(1-E), E]])
    if   closure=="released":   S=np.array([[0.,0.],[-M,1.]]);    Dg=np.array([[1.,0.],[0.,0.]])
    elif closure=="mirror":     S=np.array([[-1.,0.],[-2*M,1.]]); Dg=np.array([[1.,0.],[0.,-1.]])
    elif closure=="mirror_src": S=np.array([[-1.,0.],[-2*M,1.]]); Dg=np.array([[1.,0.],[0.,0.]])
    elif closure=="mirror_drn": S=np.array([[0.,0.],[-M,1.]]);    Dg=np.array([[1.,0.],[0.,-1.]])
    T = np.zeros((2*N, 2*N))
    def put(j, jc, m):
        for a in range(2):
            for b in range(2): T[j+a*N, jc+b*N] += m[a, b]
    for j in range(N):
        put(j, j+1, R@P) if j+1 <= N-1 else put(j, N-1, R@P@Dg)
        put(j, j-1, R@Q) if j-1 >= 0    else put(j, 0,   R@Q@S)
    return T, dt
def dominant(M, N, cfl, **kw):
    T, dt = build_T(M, N, cfl, **kw); ev = np.linalg.eigvals(T)
    lam = ev[np.argmax(np.abs(ev))]
    return abs(lam)**(2.0/dt), abs(np.angle(lam))/dt/(2*math.pi)
def M_th_lin(N, cfl=0.4, lo=0.10, hi=0.30, it=30, **kw):
    for _ in range(it):
        m = 0.5*(lo+hi); T, _ = build_T(m, N, cfl, **kw)
        lo, hi = (m, hi) if max(abs(np.linalg.eigvals(T))) < 1 else (lo, m)
    return 0.5*(lo+hi)

# --- the estimator: RELEASED logic, WIDENED bracket at the RELEASED node spacing -----
XS8 = np.linspace(1.05, 1.30, 8); STEP = XS8[1]-XS8[0]
def xnode(i): return XS8[i] if 0 <= i <= 7 else 1.05 + i*STEP
def widened_scan(N, nrt, seed, cfl, i0, span=8):
    cache = {}
    def G(i):
        if i not in cache:
            cache[i] = float(SOL.growth_rate(xnode(i)*Mth, N=N, n_roundtrips=nrt,
                                             seed=seed, cfl=cfl))
        return cache[i]
    i = i0
    while G(i) >= 0 and i > i0-span: i -= 1
    if G(i) >= 0: return float('nan'), cache
    j = i+1
    while G(j) < 0 and j < i+span: j += 1
    if G(j) < 0: return float('nan'), cache
    return (xnode(j-1) + (xnode(j)-xnode(j-1))*(-G(j-1))/(G(j)-G(j-1)))*Mth, cache

CELLS = [("A",240,.4,2), ("B",480,.213755,2), ("C",720,.144494,2), ("D",480,.4,0),
         ("E",960,.213929,0), ("F",720,.4,0), ("G",240,.2,7), ("H",240,.3,4),
         ("I",240,.5,1), ("J",120,.4,6), ("K",960,.4,-1),
         ("L",360,.4,1), ("M",120,.2,16),       # L, M: pre-publication check agents
         ("P",300,.4,1), ("Q",240,.35,3)]       # P, Q: round-1 Fabric seat
MED = {"A":.1687658795,"B":.1680689399,"C":.1678627280,"D":.1588334587,"E":.1585121120,
       "F":.1556041775,"G":.1912244214,"H":.1761747951,"I":.1642730737,"J":.1900370478,
       "K":.1540090045,"L":.1621003583,"M":.2416750895,"P":.1647615624,"Q":.1719432637}

def validate():
    r0 = run_all.measure_Mth_num(); r2, ca = widened_scan(240, 90, 1, .4, 2)
    la, _ = dominant(.7*MTHNUM, 240, .4); lp, _ = dominant(1e-9, 240, .4)
    print("[V] %r ; widened %s -> %r ; equal %s %s ; l_a %.6f (0.910958) l_p %.6f "
          "(0.724999) ; M_th,lin(240,.4) %.6f (0.168764)"
          % (r0, sorted(ca), r2, r2 == r0, r0 == MTHNUM, la, lp, M_th_lin(240, .4, it=44)))

def bulk():                                   # sec 1.1 identity, sec 1.4 factor 2 + cavity
    print("[1.1] max|0.5trD/nu_num-1| %.2e (machine eps on an IDENTITY)" % max(
        abs(nu_num_0722(N,c,M)/(.5*np.trace(D_LF(N,c,M)))-1)
        for N in (240,480,720,960) for c in (.2,.3,.4,.5) for M in (.10,Mth,.169,.25)))
    k = math.pi
    for withS in (True, False):
        for nu in (1e-2, 1e-3, 1e-4):
            for M in (1e-4, .05, .10, .149313, .20, .30):
                S = (1./TAU_N)*np.array([[0.,0.],[M,-1.]]) if withS else Z
                base = -1j*k*Amat(M) + S
                def dmp(D):
                    e0 = np.sort(np.linalg.eigvals(base).real)[::-1]
                    return e0 - np.sort(np.linalg.eigvals(base-k*k*D).real)[::-1]
                nn = .5*np.trace(D_LF(240,.4,M)); bb = dmp(Dmom(nn,M)); a = dmp(D_LF(240,.4,M))
                assert abs(dmp(nu*np.eye(2)).sum()/dmp(Dmom(nu,M)).sum() - 2.) < 1e-10
                if withS and nu == 1e-2:
                    print("  [1.4] M=%.6f branch-sum %.12f per-branch %.6f,%.6f"
                          % (M, a.sum()/bb.sum(), (a/bb)[0], (a/bb)[1]))
    for M in (1e-4, .05, .10, .149313, .20, .30):
        nn = .5*np.trace(D_LF(240,.4,M)); I = nn*np.eye(2)
        w0 = omega(M, Z).imag;         d  = lambda D: w0 - omega(M, D).imag
        w0b = omega(M, Z, tn=1e9).imag; dn = lambda D: w0b - omega(M, D, tn=1e9).imag
        asym = ((1+M)/(1-M))**2 - 1; ri = d(I)/d(Dmom(nn,M))
        print("  [cav] M=%.6f full %.6f iso %.6f same-trace %.6f no-relax %.6f (2-r)/asym %.5f"
              % (M, d(D_LF(240,.4,M))/d(Dmom(nn,M)), ri, d(I)/d(Dmom_m(nn,M)),
                 dn(I)/dn(Dmom(nn,M)), (2-ri)/asym if asym > 1e-6 else float("nan")))

def analytic():                               # sec 1.1 matrix, sec 1.3 calibration, sec 4
    D = D_LF(240,.4,MTHNUM); pr = (1/240)*(1+MTHNUM+HDRM)/(2*.4); Dn = D/pr
    md = .5*(Dn[0,0]+Dn[1,1]); ev = np.linalg.eigvals(Dn)
    print("[1.1] D/pref(%.9e)" % pr, Dn.tolist(),
          "| offdiag/tr %.5f %.5f /mean-diag %.5f %.5f | aniso %.5f | eig %.5f | Courant %.6f"
          % (Dn[0,1]/np.trace(Dn), Dn[1,0]/np.trace(Dn), Dn[0,1]/md, Dn[1,0]/md,
             (Dn[0,0]-Dn[1,1])/md, (max(ev)-min(ev))/np.mean(ev), .4/(1+MTHNUM+HDRM)))
    for M in (Mth, MTHNUM):
        cm0 = 1+M; r = .4/cm0
        print("    cmax pad inflates nu_num %.3f %% at M=%.8f"
              % (100*(g_of_cfl(.4,M)/((cm0/.8)*(1-r*r*(1+M*M)))-1), M))
    print("    nu_num/nu0 %s ; N*(coefficient) %.2f"
          % ([round(nu_num_0722(N)/NU0, 4) for N in (240,480,720)], 240*nu_num_0722(240)/NU0))
    M0 = M_th_bulk(lambda M: Z)
    a = M_th_bulk(lambda M: D_LF(480,.4,M)); b = M_th_bulk(lambda M: D_LF(480,.4,M)+Dmom(NU0,M))
    S0, S1 = 0.15884, 0.18063                 # 07-22 sec3, QUOTED not re-run
    tgt = M_th_bulk(lambda M: Dmom(NU0,M)); lo, hi = 40., 400.
    for _ in range(50):
        m = .5*(lo+hi); lo, hi = (m,hi) if M_th_bulk(lambda M: D_LF(m,.4,M)) > tgt else (lo,m)
    print("[1.2/1.3] D=0 anchor %.9f | Validation 2 model %+.6e vs solver %+.6e -> %.1f %%"
          " | nu0 threshold %.7f ; bulk-only N* %.1f"
          % (M0, b-a, S1-S0, 100*((b-a)-(S1-S0))/(S1-S0), tgt, .5*(lo+hi)))
    print("[4] DECOMPOSITION -- bulk+remainder is the registered share")
    for tag, N, cfl, _ in CELLS:
        mb = M_th_bulk(lambda M: D_LF(N,cfl,M)); mr = M_th_lin(N,cfl)
        mm = M_th_lin(N,cfl,closure="mirror"); me = M_th_lin(N,cfl,relax="exact")
        dM = MED[tag]-INVISCID; bk = mb-M0; cl = mr-mm; sp = mr-me
        oth = (mr-mb)-cl-sp; est = MED[tag]-mr; q = lambda x: 100*x/dM
        assert abs(bk+(M0-INVISCID)+cl+sp+oth+est - dM) < 1e-12
        print("  %s N=%4d cfl=%.6f dM %.4e | bulk+rem %.4e %5.2f%% | clamps %.3e %5.2f%%"
              " | split %.2e %5.2f%% | est %+.1e | M_th,lin %.8f"
              % (tag,N,cfl,dM, bk+oth,q(bk+oth), cl,q(cl), sp,q(sp), est, mr))
    mb = M_th_bulk(lambda M: D_LF(240,.4,M)); mr = M_th_lin(240,.4)
    mm = M_th_lin(240,.4,closure="mirror"); me = M_th_lin(240,.4,relax="exact")
    mu = M_th_bulk(lambda M: Dmom(.5*np.trace(D_LF(240,.4,M)), M)) - M0
    dM = MED["A"]-INVISCID; bk = mb-M0; cl = mr-mm; sp = mr-me; oth = (mr-mb)-cl-sp
    c1 = bk; c2 = c1+oth; c3 = c2+cl; c4 = c3+sp      # cumulative -> ORDER-DEPENDENT
    print("    mu %.7e ; dM/mu %.5f = %.5f x %.5f x %.5f x %.5f x %.5f  [bulk-first]"
          % (mu, dM/mu, c1/mu, c2/c1, c3/c2, c4/c3, dM/c4))
    print("    07-22-referenced %.5f = B/mu %.5f + %.5f ; 07-22's OWN nu0/nu_num(240) %.4f"
          % ((MED["A"]-Mth)/mu, (INVISCID-Mth)/mu, dM/mu, NU0/nu_num_0722(240)))

def lattice():                                # sec 2: all 45 points, no skips
    worst = (0., None)
    for N in (120,150,180,240,300,360,480,720,960):
        for c in (.2,.25,.3,.4,.5):
            mr = M_th_lin(N,c); mm = M_th_lin(N,c,closure="mirror")
            ms = M_th_lin(N,c,closure="mirror_src"); md = M_th_lin(N,c,closure="mirror_drn")
            add = (mr-ms)+(mr-md)-(mr-mm)
            if abs(add) > abs(worst[0]): worst = (add, (N, c))
            print("%4d %.2f both %.4e d/s %8.3f clamps/dx %.4f additivity %+.3e"
                  % (N, c, mr-mm, (mr-md)/(mr-ms), (mr-mm)*N, add), flush=True)
    print("    WORST additivity residual %.3e at %s" % worst)

def cell(tag, N, cfl, i0, nrt=240, ns=8):
    v = []
    for sd in range(1, ns+1):
        M, ca = widened_scan(N, nrt, sd, cfl, i0); v.append(M)
        print("   %s seed %d -> %.10f nodes %s" % (tag, sd, M, sorted(ca)), flush=True)
    v = sorted(v)
    print("   %s N=%d cfl=%.6f median %.10f sd %.3e range %.3e"
          % (tag, N, cfl, st.median(v), st.pstdev(v), v[-1]-v[0]))

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if mode in ("validate","all"): validate()
    if mode in ("bulk","all"):     bulk()
    if mode in ("analytic","all"): analytic()
    if mode in ("lattice","all"):  lattice()
    if mode == "cell": cell(sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]))
    if mode == "all":
        for tg, N, c, i0 in CELLS: cell(tg, N, c, i0)
```

**Costs on this machine.** `validate` ≈ 40 s; `bulk` seconds; `analytic` ≈ 12 min; `lattice` ≈ 45 min; the fifteen cells ≈ 3 h of solver time, dominated by C, E, M and P. The operator alone: **4.2–4.3 s** for 30 bisections at N = 240 (480 × 480), **2.5–3.0 s** for one 1920 × 1920 `eigvals` at N = 960, **≈ 76–90 s** for 30 bisections there — across the two seats that timed it.

## 8. Limitations, including what was not run

1. **One machine, one platform, one numpy** (3.11.2 / 2.4.6 / macOS 26.6 arm64) — shared by the author, both check agents and all six assessors, so **a platform-borne agreement is invisible to every seat that has looked at this.** Their reproductions test the *construction*, not the platform.
2. **The exact operator is linear.** Every share in §4 except "est" is a property of the linearized scheme. §5 measures the linearization error at ≤ 2.10 × 10⁻⁵ over fifteen cells, 0.1 % of ΔM at the shipped grid — a *measurement of the residual*, not a proof that the decomposition is nonlinearly stable.
3. **The bulk-only model discards two roots by construction**, its D = 0 anchor sits −2.26 × 10⁻⁶ from the exact inviscid value, and its external calibration is **3.1 %** on the shift — larger than the entire remainder term. Everything defined against it inherits that: the unregistered 92.42/2.60 division, the cavity ratios and key 2's band, μ, N\* = 199.3, the ratio-6 other/bulk. **Corroboration status, stated:** it has been independently re-implemented **twice, both times by the 🌊 Kinetic seat** (round 1, matching the cavity and split tables to all quoted digits; round 2, returning 199.26 / 216.25 / 214.03, ν₀ threshold 0.17112650, μ = 9.0563370 × 10⁻³). **Neither check agent, neither Fabric seat and neither Quanta seat rebuilt it.** It remains the largest surface here resting on one author's construction plus one re-implementer.
4. **The mirrored closure is one particular second-order substitute**, and no alternative was run — which is why an alternative is now the *falsifier* rather than the reproduction check. The additivity residual and the near-constancy of clamps/Δx are evidence, not proof, and clamps/Δx drifts 70 % across the sampled lattice, so "near-constancy" is a statement about the `cfl` = 0.4 edge.
5. **Eight seeds is the whole census at every cell**, and the pair comparisons use the eight-seed *range* — the looser of the two statistics 08-06 flagged as ambiguous. All three pairs clear both by ≥ 14×; §3.2 prints the stricter 0.443·sd bar alongside, where it does bite at two cells.
6. **`n_roundtrips` = 240 only** (plus three cells at 90 and the released-bracket census). No cell at 360 or 480; 08-06's plateau result is inherited, not extended.
7. **The iso-`ν_num` lattice is three pairs**, at Δx ratios 2, 2 and 3. A scan cannot find a feature narrower than its own step.
8. **Did not run, and why.** (a) The Δx-ratio-6 **measured** census (N = 1440, `cfl` = 0.072871), ≈ 2 h — pre-registered and attempted by nobody; only its operator-and-model side was computed. (b) An **augmented solver** with a physical momentum-only ν added to the released step — 07-22 §3's own check, validated *against* rather than re-run, so 0.15884 / 0.18063 / +13.72 % are **quoted**. This is the decisive open experiment: the only falsifier for key 2's cavity clause that can fire, the only way to settle §1.3 above the 3.1 % level, one of the two falsifiers with teeth for §0 claim 7, and the object 07-22's "≈ 240" and this note's 216 actually disagree about. (c) `measure_Mth_num_ceiling_N` at 08-02's own convention — not tested, not contested. (d) N = 880, the one rung where 08-02's interval could move. (e) The estimator bias at cell **K** (960, nodes −1, 0), ≈ 50 min — a named gap on the floor side, at the cell with the second-largest error. (f) The same bias at cell **P**, which sets the registered sampled maximum. (g) Any drive/gain-plane consequence — no CW, pulse or PRBS run, so §9's WP2 remarks are about the threshold estimator, not about `pulse_gain_dB_at_0p7_streaming` or any gated row. (h) 08-02's seed-2 widened rung, which is quoted.
9. **A "failed reproduction" that was this session's own convention error — the third of its kind in this project's record.** An earlier draft reported that 07-12-effective-loop §3/§4's `loop_analytic` = 1.048112 / 0.945034 did not reproduce, built a 0.87 % gap on it, and declined to reconstruct that note's §7 branches. **All of it was wrong.** The cause was an extra 1/(1−M²) drift factor inserted into the exponent of a formula the draft printed correctly; evaluated as printed it gives **1.048112105** and **0.945034135** — six digits at two independent operating points — and the whole chain then reconstructs (a_b = 0.9894669 against the note's 0.98947; §7's branches 0.157281 / 0.155965 against 0.1573 / 0.1560). [`agents/README.md`](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md) already records two instances of this failure and the rule written from them — *"a failed search is not a refutation … 'I could not reproduce it' is a statement about the searcher, not about the number"*. It was broken a third time, caught by a check agent in two lines, and verified withdrawn by all three round-1 seats. **The operational lesson: before publishing a non-reproduction, evaluate the printed formula symbol-for-symbol against the source rather than re-deriving it.**
10. **Three quantities were stated over continuous regions from lattice samples and two of them broke** — a drain/source band that fired inside its own quantifier at the corner, a clamps/Δx range that understated its top by 32 %, and a registered key value an assessor exceeded on the first independent try. **Every such statement here is scoped to the sampled lattice and says so.**
11. **Everything here is numerics, not physics.** No claim is made about the physical threshold; `M_th_kinetic_353K` = 0.165 [0.154, 0.169] is consumed as published. Everything downstream still rides on the unproven gain cell (bench gate G1).

## 9. What this changes

### `M_th_num_convention` in `results.json`

It reads *"coarse-grid Lax-Friedrichs at the single released grid N=240; Dx->0 limit is the exact inviscid 0.149313"* (verified verbatim). True, and incomplete in four ways:

1. **A tenth of the excess over 0.147083 is not numerics at all.** *The fact is already released* — [`fable-model-chain/README.md`](https://github.com/ryoji-info/FableComputer/blob/main/fable-model-chain/README.md):46 and [`ROADMAP.md`](https://github.com/ryoji-info/FableComputer/blob/main/ROADMAP.md):18 both carry "**+1.52 % above the small-M analytic 0.147083**" adjacent to the convention string, both corrections made in response to [`2026-07-26-record-audit-ten-findings.md`](2026-07-26-record-audit-ten-findings.md) Finding 5 *(🧵 Fabric r1)*. **What is new is the share, not the fact:** B is **10.3 %** of the +14.86 % offset 07-22 §2's table quotes — larger than the 4.83 % clamp term and larger than every non-bulk term combined.
2. **The rest is not "numerical viscosity" in the momentum sense.** It is **95 % bulk diffusion of the conserved vector** — LF diffuses mass and momentum, and by a trace identity that is **exactly twice** a momentum-only viscosity at the same Laplacian coefficient — plus **4.8 % first-order placement of the two DS Dirichlet clamps** (drain 3.4 %, source 1.4 %) and **0.15 % explicit-Euler splitting**.
3. **`cfl` is an independent viscosity lever at fixed Δx, and it is stronger than the grid.** The load-bearing fact is **already registered** *(⚛️ Quanta r1)*: [`2026-08-06`](2026-08-06-mth-num-record-length-and-fit-convention.md) §4.2 puts the `cfl` = 0.2 root 0.036 % below the released ceiling at N = 240 with `nan` at 4/4 seeds, which with that note's own ladder already implies the ≈ +13 % lever. Added here is the eight-seed 240-round-trip census: at N = 240, `cfl` = 0.2 → **+13.31 %**, 0.3 → +4.39 %, 0.5 → −2.66 %, against a whole 240 → 720 grid ladder of **−7.80 %**. (At 90 round trips the same quantities are +13.15 % and −7.91 %, reproducing the 2026-08-07 lab datum exactly and identifying its convention.) A convention line naming N but not `cfl` names half the configuration — and **`cfl` is not the Courant number.**
4. **The estimator convention** 08-06 already asks for, plus the fact that **the released bracket is not safe over the (N, `cfl`) family**: it fails above the ceiling at `cfl` = 0.2 — at **25 % of seeds already at 90 round trips**, extending 08-06 §4.2 — and below the floor at N ≥ 920.

### 07-22's two readings, and one annotation to route

**The band-edge coincidence survives; only its numerical leg is retired.** 07-22 §2 reads N = 240's landing at the upper edge of 0.165 [0.154, 0.169] as *"a coincidental alignment of differently-sized numerical effects."* The numerical alignment now has a single dominant mechanism: the shipped grid sits at 1.12–1.20× the threshold-matched crossover, the LF scheme delivers **0.89×** the shift a physical DC ν₀ would, and the boundary contributes 4.8 %. **But the coincidence has a second leg this note cannot touch [check 2]:** the *position* of the physical kinetic band edge 0.1693 depends on the viscoelastic crossover 1/(1+x²) and the A ∈ [0.5, 3] prefactor band, which is physics, and Limitation 11 says everything here is numerics. **Retired: the numerical leg's mystery. Not retired: the coincidence.**

**`visc_numerical_crossover_N` ≈ 100 stands** as a coefficient statement (100.34 reproduced) and now has its conversion factor **× ≈ 2** to reach a threshold statement. Which grid that lands on depends on what you match: **199.3** bulk-only-vs-bulk-only, **≈ 216** against the measured ladder, **214** on total shifts. 07-22's disclosed caveat — *"the threshold-matched effective crossover is ≈ N = 240"* ([`2026-07-22-mth-numerical-vs-physical-viscosity.md`](2026-07-22-mth-numerical-vs-physical-viscosity.md):60) — is an **empirical measured-shift estimate, the same kind of object as the 216, and is refined by ~10 %, not superseded.**

> **Two record-maintenance actions, to be written into the promoting PR — not merely prescribed here** *(⚛️ Quanta and 🧵 Fabric, both rounds)*. The precedent is [`2026-07-26-record-audit-ten-findings.md`](2026-07-26-record-audit-ten-findings.md):75, **Finding 5** — *"Retired readings persist in released source, and the record's machine-readable promises are unkept"* — a charge about unrouted refinements surviving in released artifacts.
> 1. A **dated post-promotion annotation on 07-22** recording that its ≈ N = 240 caveat is refined to **≈ 216** (measured-ladder match) and **199.3** (bulk-only-vs-bulk-only), with the conversion factor ≈ 2 from the coefficient crossover 100.34, and `visc_numerical_crossover_N` ≈ 100 **unmoved** as a coefficient statement. The 199.3 leg's corroboration status (Limitation 3) travels with it.
> 2. The corresponding **[`notes/INDEX.md`](INDEX.md):43 row edit** on 07-22's line, alongside the existing "stands" verdict.

### WP1 — a CI item stronger than a three-rung ladder, priced honestly

Replace "assert `M_th_num(N)` falls first-order toward 0.14931" with a **collapse law**:

> **CI assertion.** On the sampled set N ∈ {120, 240, 300, 360, 480, 720, 960} × `cfl` ∈ {0.144494, 0.2, 0.213755, 0.213929, 0.3, 0.35, 0.4, 0.5}, the spectral-radius-1 crossing of the exact linearized one-step operator predicts the released estimator's eight-seed median to **|Δ| ≤ 5 × 10⁻⁵**. Demonstrated at fifteen cells, sampled-maximum error 2.10 × 10⁻⁵, zero free parameters. **Offered as a prediction, not a demonstrated universal, for interpolated (N, `cfl`)** inside 120 ≤ N ≤ 960, 0.2 ≤ `cfl` ≤ 0.5 — fifteen points do not establish "any", and the house rule on lattice censuses applies. The best evidence that interpolation is safe is the adversarial corner cell (120, 0.2), run precisely to break it, which held at −3.87 × 10⁻⁶ (−1.12 × 10⁻⁵ after the estimator-bias correction) at 4.7× the shipped ΔM.

Four things must be said with it, and were not *(all 🧵 Fabric r1)*:

- **It costs more than "seconds" at the top of the sheet.** Operator: **4.2–4.3 s** for 30 bisections at N = 240; **≈ 76–90 s** at N = 960 (one 1920 × 1920 `eigvals` is 2.5–3.0 s alone). Solver spot-check: **≈ 105 s** for an eight-seed N = 240 census.
- **The analytic sheet on its own is a reproduction check, not a regression test** — it re-executes a deterministic eigenvalue computation. **All regression protection lives in the measured spot-check cell**, and the memo's framing inverted that emphasis.
- **CI must run the 240-round-trip, eight-seed census and must not be wired to the released estimator's own output.** Against `run_all.measure_Mth_num()` = 0.16894319463373791 (seed-1, 90 round trips) the operator's 0.16876409 is **+1.79 × 10⁻⁴ = 3.58× the 5 × 10⁻⁵ tolerance** — the assertion fails outright at the convention CI would most naturally reach for. Against the 240-round-trip median at the same cell it is +1.79 × 10⁻⁶.
- **The law is common-mode in the shared physical constants** (§5): it catches scheme regressions and **not** `constants.py` changes.

It remains a better regression than the ladder: it is **two-dimensional** — constraining the `cfl` axis, which no promoted ladder touches and which moves the threshold more than the grid does — and its analytic half is cheap enough to assert the whole sheet while the solver budget buys one measured cell instead of a three-rung ladder 08-06 has called ill-conditioned, a verdict §5 reinforces from the other side. Emit the eight-seed spread beside the value, as 08-06 §9 item 2 already asks.

### WP2 — where the Boltzmann–Maxwell tier's error budget should go

clamps/ΔM is **bounded but not constant**: 5.34 % (N = 120), 4.83 % (240), 4.61 % (480), 4.54 % (720), 4.51 % (960) at `cfl` = 0.4 — a **15.5 % relative drift** over an 8× refinement.

- **At the released scheme's order, refining the grid does not change the contact closure's share by more than ~15 % over an 8× refinement, and cannot change it by an order.** Both channels are first order, so the ratio is bounded, and refinement *helps* the contact slightly. Spending the budget on the interior is correct *for this scheme*: **a high-order interior buys ≈ 19.7× before the contact binds** — and the method is stated, because four candidate constructions all round to "~20": bulk/clamps = 19.13, (bulk + remainder)/clamps = 19.67, ΔM/clamps = 20.70, and **(ΔM − clamps)/clamps = 19.70**, the one that means what the sentence says. It is **not constant**: over the sampled `cfl` = 0.4 ladder it runs **17.7 (120) / 19.7 (240) / 20.7 (480) / 21.0 (720) / 21.2 (960)** *(🌊 Kinetic r1)*.
- **Raising the interior order makes the contact closure the leading error term across the sampled family for any plausible second-order scheme — but that is a claim with a constant, and here it is.** A second-order interior of dimensionless coefficient C exceeds the O(Δx) contact term only for **N > C/c_clamp**, so the **binding cell is the coarsest grid**, not the smallest c_clamp: measured c_clamp·N is **31.3 at (120, 0.4)** and **41.3 at (120, 0.2)** against 194.5 at (960, 0.5), so the family bound is **≈ 29–31**. **C ≲ 24 is therefore a *sufficient* condition, conservatively so, and not a necessity** — the word "only" is struck *(🌊 Kinetic r1; derivation corrected by ⚛️ Quanta and 🧵 Fabric r2)*. For scale the released *first-order* interior coefficient is bulk/Δx = **4.315** at the shipped cell. C is not measured here, and the statement is not made off the family N ∈ [120, 960].
- **The drain is the leveraged end** — 2.430× the source at the shipped cell, 2.078–5.756× over the fully-evaluated lattice, rising steeply toward low N and low `cfl`. **Two things must be said with that number.** First, it is a numerical statement about clamp placement and must **not** be conflated with [`2026-07-18-boundary-channel-contact-gated.md`](2026-07-18-boundary-channel-contact-gated.md)'s physical, σ_c-gated contact channel, whose δ_b is one-signed at the source and **sign-open at the drain**. Second — the collision a reader will actually hit [check 2] — [`2026-07-18-boundary-channel-bench-discriminants.md`](2026-07-18-boundary-channel-bench-discriminants.md) §5 carries the near-identical phrase "~3× more leveraged", and its own post-promotion note and vote record **record that it does not hold on the linewidth observable**. The recorded lesson is that such a claim must name its observable. **This one's observable is the threshold M under a clamp-placement substitution in the exact linearized operator, and it is claimed for no other.**
- **The clamp term is a deterministic common-mode offset, not a resolution floor.** It is a deterministic function of (N, `cfl`, M) with no seed dependence, so a contact-parameter sweep at fixed (N, `cfl`) differences it out. How completely: moving the operator's threshold with τ_n and re-measuring gives **d(drain term)/d(M_th) = +0.0067** at (240, 0.4) — drain term 7.366 → 6.071 × 10⁻⁴ as M_th falls 0.17920 → 0.15959 — so a differential contact measurement retains **0.67 %** of the bias, and a δM = 10⁻⁴ contact effect leaves 6.7 × 10⁻⁷. **What 6.657 × 10⁻⁴ does bound is the absolute calibration:** no *absolute* statement that the released N = 240 threshold equals a physical threshold is meaningful below it. Converting to a grid, with the method stated: solving drain(N) = 10⁻⁴ on the operator's measured Δx-linearity gives **N = 1378** anchored at N = 960 and **N = 1598** anchored at N = 240 — the spread is exactly the clamps/Δx drift of §2 — or the two-line mirrored closure at any N.

### The mirrored closure is PRICED, not proposed for adoption

Adoption is a maintainer's versioned edit, and it must move a published literal at the same time. The full ledger *(🧵 Fabric r1; arithmetic corrected in r2)*:

- `M_th_num` moves **−9.395991 × 10⁻⁴ = −0.5562 %**.
- **0.7·`M_th_num` moves 0.1182602 → 0.1176025, which still rounds to the 0.118 the chain hard-codes.** The margin is thin and is printed rather than hidden: it would take a shift of 1.086 × 10⁻³ = **1.16× the measured clamp cost** to push it below 0.1175, so the rounding survives by **16 %**. Two caveats belong with that *(🌊 Kinetic r2)*: 0.1176025 clears the round-down edge by 1.4645 × 10⁻⁴ in M, which is **1.61× the 90-round-trip eight-seed sd (9.110 × 10⁻⁵)** and **0.52× that census's range (2.832 × 10⁻⁴)**, so "still rounds to 0.118" is a **seed-1 statement**; and the 9.396 × 10⁻⁴ clamp cost is a 240-round-trip *linearized-operator* number applied to a 90-round-trip seed-1 draw. (Applied instead to the eight-seed median M̄ the shifted value is 0.1174784, which rounds to 0.117 — the cross-convention mixing this note's own M̄ / `M_th_num` distinction exists to prevent, and the reason the round-1 figure "0.11748, which no longer rounds to 0.118" does not hold on the object the code names.)
- `energy_per_add_fJ`'s upper end is `P·slot` with `P ∝ v₀²`, so it moves by (0.1176025/0.1182602)² − 1 = **−1.109 %** *if the literal is updated*, and **0 %** if it is not. Named through the chain: the released `energy_per_add_fJ` upper end is **0.4659989139805216**, computed from the hard-coded 0.118; **0.46806 fJ** is what the chain emits when the literal is replaced by 0.7·`M_th_num`, and **0.46286 fJ** is that with the clamp shift applied — a before/after on the *recomputed* constant, not a discrepancy against `results.json` *(⚛️ Quanta and 🧵 Fabric r2)*.

**And the durable defect, present today and independent of the closure fix:** `0.118` is a **hard-coded literal** at [`fable-model-chain/run_all.py`](https://github.com/ryoji-info/FableComputer/blob/main/fable-model-chain/run_all.py):54 (`P_hi = TH.joule_kW_cm2(C.n_op, 0.118 * s, tau353)`) and [`fable-model-chain/thermal.py`](https://github.com/ryoji-info/FableComputer/blob/main/fable-model-chain/thermal.py):50–51 (`# upper (solver-class) bias bound: M/M_th,num=0.7 -> M=0.118` / `v0b = 0.118 * s`). **It does not track `M_th_num` at all — even though `Mthn = measure_Mth_num()` is in scope three lines earlier, at `run_all.py`:51.** *(Read at source. The round-2 rework cited `run_all.py`:45 and "five lines earlier"; the 🧵 Fabric round-2 seat caught it, and :51 is verified here.)* Any future change to the threshold leaves that literal silently stale against its own provenance comment, and the failure would be invisible because nothing recomputes it. **That is a worse defect than a broken rounding, and it is the one worth fixing first.**agentId: a21d75cf02e961e36 (use SendMessage with to: 'a21d75cf02e961e36', summary: '<5-10 word recap>' to continue this agent)
<usage>subagent_tokens: 412851
tool_uses: 35
duration_ms: 2636684</usage>

---

## Agent assessment — 2026-08-07 — two rounds, six assessor seats

Assessed by the project's disclosed AI research crew ([agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md)). Each round used **three fresh, mutually blind persona assessors** sharing no context with the drafting, the pre-publication check, or any prior round, and each was required to re-execute the decisive numbers against the released, unedited chain rather than trust the transcript. All seats ran on `claude-opus-5` — **not** Claude Fable 5.

| stage | tally | outcome | record |
|---|---|---|---|
| pre-publication check | 2 blind agents | refuted **nothing measured**; refuted **six claims**, all withdrawn or repaired before publication | in the reply's closing section |
| round 1 | **3 of 3 store** | storable, but all three attached required edits (9 + 9 + 6 = **24**) → rework | [vote record](https://github.com/ryoji-info/FableComputer/discussions/108#discussioncomment-17929052) |
| round 2 — rework | — | **21 accepted, 3 corrected, 0 declined outright**; one clause declined with its measurement | [rework](https://github.com/ryoji-info/FableComputer/discussions/108#discussioncomment-17930099) |
| round 2 — re-assessment | **3 of 3 store** | promoted | [vote record](https://github.com/ryoji-info/FableComputer/discussions/108#discussioncomment-17930101) |

The vote records are **evidence and are never edited after posting**. They are linked rather than duplicated here because they are permanent and unedited in the discussion; this note is the corrected record of the physics.

**No assessor, in either round, refuted a measurement.** Every defect found across eight adversarial seats was a claim *about* a number, a label, a scope, or a falsifier that could not fire.

**Three findings from the assessment are in this note because assessors put them there**, credited under standing rule 5:

- 🧵 **Fabric (round 1)** ran two cells that did not exist in the memo — (N = 300, `cfl` = 0.4) and (N = 240, `cfl` = 0.35), a `cfl` absent from every published cell. The collapse law held out-of-sample at +2.10 × 10⁻⁵ and −3.26 × 10⁻⁶. Both are now in §3.2's table, and the first is why `M_th_num_operator_collapse_max_err` is registered as a **sampled maximum, not a bound**.
- 🌊 **Kinetic (round 1)** established that the bulk-versus-"other" split inherits the bulk-only model's own ~3.1 % external calibration error — ≈5.6 × 10⁻⁴, **larger than the entire 5.06 × 10⁻⁴ "other" term** — so the merged 95.02 % is the defensible figure and the finer split is not printed as though it were resolved.
- ⚛️ **Quanta (round 1)** required the record-maintenance consequence be routed rather than implied: 07-22's disclosed "≈ N = 240" crossover caveat is refined here, and that needs a dated post-promotion annotation on 07-22 and a row edit in `INDEX.md` (§9).

**One correction ran the other way, and it is recorded because the rule requires it.** Round-1 Fabric's edit 4 asserted that adopting the mirrored closure would move 0.7·`M_th_num` off the hard-coded 0.118. The hard-coding is real, but the arithmetic was not: the shift gives **0.1176025, which still rounds to 0.118**. The substance was accepted, the number corrected, and the durable defect underneath found in the process — **0.118 is a literal at `run_all.py`:54 and `thermal.py`:50–51, not a computed `0.7 * Mthn`, though `Mthn = measure_Mth_num()` is in scope five lines earlier.** Separately, the rework drafted a decline of one objection, tested it against the pre-registered point the decline rested on, found the assessor right, and withdrew the decline before publication rather than after.

That last item is the reason `agents/README.md` now carries the rule that a failed search is not a refutation, and that the duty to re-execute binds before *rejecting* an objection exactly as it does before accepting one.
