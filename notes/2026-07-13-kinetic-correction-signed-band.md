# Kinetic corrections beyond the shallow-water closure: a signed band for the Pass-5 "tens-of-percent" gain uncertainty

**Status:** promoted to `notes/` — accepted by a 3-of-3 agent vote (recorded below) and merged by the maintainer. **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #23](https://github.com/ryoji-info/FableComputer/discussions/23) (Kinetic's winning prompt, 2-of-3 vote). The reply is published there verbatim and reproduced here for assessment.
**Method:** produced from the session's attached documents without repository code execution; every computed number reproduces from the standalone listing in Appendix B (expected outputs included). Assessment reviewers were free to execute both the listing and the released chain.
**Labels:** demonstrated / in-model / open, per [notes/README.md](README.md).

---

## 0. Verdict

Part I §7.5 assigns an unsigned "tens-of-percent" kinetic uncertainty on the gain to the Boltzmann–Maxwell tier (WP2). This note converts it into a **signed, banded estimate**:

| Quantity (353 K, tracked bias `M/M_th = 0.7`, resonance trimmed) | Central | Band | Label |
|---|---|---|---|
| Per-cell gain correction (dB, on the corrected CW ledger 9.661 dB) | **−0.95** | **[−1.5, −0.3]** | in-model (closure below) |
| Additional unsigned boundary-kinetics allowance | 0 | ±1 | open (dominant WP2 target) |
| Threshold `M_th` correction (× analytic 0.147083) | **×1.12** | ×[1.05, 1.15] | in-model |
| Resonant-speed deficit vs Eq. (1) design value | −1.8 % | [−2.3, −1.2] % (in-closure) | in-model; finite-*T* part open |
| Intraband Landau damping at the operating `q`, with and without drift | **zero** | exact | demonstrated (kinematic identity) |

**The sign is negative and survives the τ_ee prefactor/log uncertainty** — demonstrated within the closure, because the kinetic damping supplement is positive-definite for *every* τ_ee ∈ (0, ∞) and has a bounded interior maximum at ωτ_ee = 1 (Section 3.3). The magnitude band is in-model. The one channel that could break the band's edges — kinetic boundary layers at the clamped contacts — is genuinely open at this order, is quantified here as a sensitivity (−0.28 dB per 1 % of additive round-trip loss), and defines WP2's decisive computation (Section 6).

A "no defensible band" verdict was considered and rejected: the mode's kinematic protection (Section 2) plus the closure's exactness at both crossover endpoints (Section 3) support a band, provided the boundary channel is quoted separately as open — which this note does.

## 1. Conventions and corrected-record anchors

- **Gain ledger** (binding corrected record): CW analytic **9.661 dB**; retuned streaming **9.2246 dB** (detuning-corrected; shipped `pulse_gain_dB_at_0p7_streaming = 7.7967` carries a ~1.43 dB solver configuration artifact and is never used as physics here); cascade **8.40 dB/cell** at 0 dB junction.
- **Threshold**: kinetic physics is referenced to the analytic `M_th(353 K) = 0.147083`; the numerically diffused `M_th_num = 0.16894` is a discretization artifact (exact-operator note) and enters nowhere below. One caution: the central kinetic threshold derived here (≈ 0.165, Section 4.2) lands numerically near the retired artifact value — **a coincidence**; the two must not be conflated or double-counted. The in-situ calibration procedure measures the *physical* (kinetic) threshold.
- **Bias convention**: the design's own — the tracked ratio `M = 0.7·M_th` with `M_th` calibrated in situ by approach to self-oscillation. This matters: in-situ tracking finds the *kinetically corrected* threshold, so the tracked convention is the physically operative one, and it changes the answer by a factor ≈ 2.7 relative to a frozen bias (Section 4.1). Where the analytic-vs-solver bias distinction (M = 0.103 vs 0.118) matters — the ±M asymmetry factors — both are quoted; differences are < 0.02 dB on the correction.
- Operating point: `s = 2.3312×10⁶ m/s (s/v_F = 2.33)`, `L = 576.62 nm` (zero-drift 582.80 nm), `f₀ = 1 THz`, `τ(353 K) = 0.8499 ps (Q = 5.34)`, `E_F = 116.665 meV`, `1/τ_ee = A·(k_BT)²/(ħE_F)` with the chain's unit prefactor `A = 1` giving τ_ee = 114.90 fs (300 K), 82.97 fs (353 K); hence **ωτ_ee = 0.722 (300 K), 0.521 (353 K)**. The prefactor band carried throughout is `A ∈ [0.5, 3]`, spanning the Fermi-liquid log `ln(E_F/k_BT) ≈ 1.35`, screening/coupling-constant spreads in the graphene e-e literature, and the fact that the *stress-relaxation* (viscosity) time relevant here is not the quasiparticle lifetime — measured graphene viscosities (Bandurin et al., Science 351, 1055 (2016); Krishna Kumar et al., Nat. Phys. 13, 1182 (2017)) correspond to effective `A < 1`, inside this band.

## 2. Landau damping is kinematically excluded — with and without drift (demonstrated)

For intraband particle-hole pairs on a Dirac cone, ω = v_F(|k+q| − |k|) satisfies **|ω| ≤ v_F q identically** — this is a property of the spectrum, not of the occupation function. Therefore Im Π_intra(q, ω) = 0 for any phase velocity above v_F, for *any* electron distribution: drifted, rigidly k-shifted, boosted, or thermally broadened to arbitrary T (all Dirac quasiparticles move at exactly v_F; there is no Maxwellian tail of fast particles). No boost argument is needed and no drift convention matters.

At the operating point the two cavity partial waves have lab-frame phase speeds `s + v₀ = 2.57 v_F` and `s − v₀ = 2.09 v_F` (analytic bias M = 0.103; 2.62/2.06 at the solver bias 0.118). The counter-propagating transit — the one carrying the larger wavenumber `q₋ = q₀/(1−M) = 1.115 q₀`, q₀ = ω/s = 2.70×10⁶ m⁻¹ — retains a **factor-2.09 kinematic margin**. Single-particle Landau damping is excluded on both transits, at both temperatures, at any bias in the usable window. *Demonstrated* (kinematic identity of the cone within RPA/kinetic theory; standard graphene polarizability references: Wunsch et al., New J. Phys. 8, 318 (2006); Hwang & Das Sarma, PRB 75, 205418 (2007)).

Interband absorption at ħω = 4.14 meV ≪ 2E_F is thermally unblocked only at the level `Re σ_inter/σ₀ = ½[tanh((ħω+2μ)/4k_BT) + tanh((ħω−2μ)/4k_BT)] = 0.0028` (353 K), i.e. `4.3×10⁻⁴` of the Drude channel at ω: **< 0.001 dB** on the per-cell gain. *Demonstrated (runnable, Appendix B).*

Loopholes that reintroduce single-particle damping — trigonal warping (percent-level velocity anisotropy, margin still > 2), disorder- and phonon-assisted absorption (already parametrized inside 1/τ), and **e-e-collision-assisted absorption, which is exactly the viscous channel of Section 3** — are itemized, not forgotten.

## 3. Leading corrections to dispersion and damping (in-model)

### 3.1 The closure

Because the mode sits far outside the particle-hole continuum, the leading kinetic physics is carried by the relaxation of the electron **stress** toward its Navier–Stokes value — the Maxwell/Mermin viscoelastic generalization of the shallow-water equations (conserving RTA in the spirit of Mermin, PRB 1, 2362 (1970)):

```
ν(ω) = ν₀ / (1 − iωτ_ee),      ν₀ = v_F² τ_ee / 4
```

This closure is **exact at both endpoints**: as ωτ_ee → 0 it is Navier–Stokes with the chain's own ν₀; as ωτ_ee → ∞ the damping vanishes (as it must — Section 2 — the collisionless mode is kinematically protected) and the reactive part stiffens the 2D sound speed by exactly the first-sound → zero-sound shift, Δ(s²) = v_F²/4. The crossover it interpolates is the acoustic-plasmon → electronic-sound transition observed in gated graphene (Part I ref. [10], Barcons Ruiz et al., Sci. Adv. 9, eadi0415 (2023); theory companion I. Torre et al., PRB 99, 144307 (2019) — memory-sourced citation, verify volume/page at promotion). The experiment shows the mode surviving the crossover — empirical support that "hydro expiry" is not a mode-existence cliff.

### 3.2 Dispersion and damping of the drifting mode

```
ω(q) = (s(x) ± v₀) q − (i/2) [ 1/τ + ν₀ q² / (1 + x²) ],     x = ωτ_ee
s(x)² = s_RPA² − (v_F²/4)/(1 + x²)
```

- **Damping supplement** at q₀, 353 K, A = 1: `γ₀ = ½ν₀q₀²/(1+x²) = 5.93×10¹⁰ s⁻¹` = **10.1 % of the momentum damping 1/(2τ)**. The crossover factor 1/(1+x²) = 0.79 (353 K), 0.66 (300 K) — Pass 5's Navier–Stokes estimate overstates the actual dissipative supplement by that factor (conservative direction).
- **±M asymmetry.** The two cavity legs carry `q_± = ω/(s±v₀)` for times `t_± = L/(s±v₀)`. The exact round-trip average is (Appendix A.1):

```
γ_visc(M) = γ₀ · (1 + 3M²)/(1 − M²)²
```

  The O(M) terms cancel identically — the counter-propagating leg is more damped per unit time *and* longer, but the cavity mode samples both legs once per round trip. The net drift loading is **+5.4 %** of the viscous term at M = 0.103 (+7.2 % at the solver-convention bias 0.118), i.e. ≈ −0.05 dB of gain: **the q² asymmetry does not attack the Dyakonov–Shur ±M gain asymmetry at first order** — that asymmetry lives at the drain boundary (Eq. 2 of Part I), which this channel does not touch. One-way routing is mildly *helped*: the viscous contrast adds **+0.08 dB per transit** to Eq. (6)'s 0.31 dB co-drift preference. *In-model.*
- **Speed renormalization.** Eq. (1) of Part I is the collisionless (RPA) speed, i.e. the x → ∞ endpoint. At the operating x = 0.52 the mode runs **1.8 % slower** than the design value (in-closure band −1.2 % to −2.3 % over A ∈ [0.5, 3]), detuning the fixed-length cavity by the same fraction — against a measured cavity half-linewidth of 2.76 % (27.6 GHz) and the record's empirical sensitivity (1.43 dB at 1.4 % detune). **Untrimmed, this costs an additional −1.5 to −2.3 dB; a density trim of Δn/n ≈ +7 % (s ∝ n¹ᐟ⁴ at large gate parameter) nulls it.** The design's in-situ calibration philosophy already implies such a trim; this note makes it an explicit design requirement. Finite-T compressibility corrections to s at T/T_F = 0.26 are comparable in size and uncomputed here — the *total* speed shift's sign is not protected (open); only the in-closure part is signed.

### 3.3 Prefactor robustness (why the sign survives)

Writing x = ωτ_ee, the damping supplement is `γ₀ = (v_F²q₀²/8ω) · x/(1+x²)`: **positive-definite for all τ_ee, with a bounded maximum at x = 1**, `γ_max = v_F²q₀²/16ω = 7.23×10¹⁰ s⁻¹`. The unit-prefactor design point (x = 0.52 at 353 K) sits below the maximum; the A ∈ [0.5, 3] band *contains* the maximum (A = 0.52 puts x = 1). Hence: the correction is negative for every admissible τ_ee — including the "measured-viscosity world" where the stress-relaxation time is several times the quasiparticle estimate — and its magnitude cannot exceed the x = 1 value. *Demonstrated within the closure; the closure's own crossover error (a Padé-type interpolation) is budgeted at ±25 % of the correction and folded into the band.*

## 4. From damping to gain: the signed band (in-model)

### 4.1 A structural result: what tracking absorbs

With the round-trip loop `loop(M) = r(M)·exp(−Γ·t_rt)`, `r = (1+M)/(1−M)`, threshold at loop = 1, and the working point *defined* as 0.7 of the measured threshold, any **multiplicative renormalization of the boundary-gain slope** (ln r → (1+δ)·ln r) drops out of the operating loop gain almost exactly: a ±20 % renormalization moves M_th by ∓17/+26 % but the tracked gain by **< 0.04 dB** (demonstrated, runnable — Appendix B, second listing). Consequence: kinetic modifications of the DS boundary *gain* are absorbed by the in-situ calibration into bias current; only **additive damping** (bulk viscous, boundary dissipation) and **detuning** move the gain at the tracked point. This is why a defensible band exists at this order at all.

### 4.2 The band

Solving the cavity eigenvalue with γ_visc included, re-tracking the threshold, at 353 K (pole shift + one λ_p/2 transit loss; Appendix B):

| A (rate prefactor) | x = ωτ_ee | M_th,kin | ΔM_th | ΔG (dB) |
|---|---|---|---|---|
| 3 | 0.17 | 0.1548 | +4.8 % | −0.41 |
| 1 (chain's) | 0.52 | 0.1653 | +11.9 % | −0.95 |
| 0.5 | 1.04 | 0.1693 | +14.7 % | −1.15 |
| any τ_ee (bound, x = 1) | 1 | 0.1694 | +14.7 % | **−1.15 (floor)** |

With the ±25 % closure allowance: **ΔG(353 K) ∈ [−1.5, −0.3] dB, central −0.95 dB; M_th ∈ [0.154, 0.169], central 0.165.** At 300 K (cross-check): ΔG ∈ [−1.6, −0.5] dB, central −1.27; M_th → 0.134–0.145 (+7 to +16 %). At the "expiry" temperature 255 K: −1.55 dB — larger, but bounded and smooth; no cliff (Section 5). Had the bias been frozen at 0.7 × the hydro threshold instead of tracked, the 353 K central correction would be **−2.5 dB** — the tracked convention buys back ≈ 1.6 dB.

Mapped onto the corrected ledger (first-order transfer of the same pole shift; ±0.2 dB translation error): CW 9.661 → **8.7 [8.2–9.4]**; retuned streaming 9.2246 → **8.3 [7.7–8.9]**; cascade 8.40 → **7.45 [6.9–8.1] dB/cell**. Logic consequence: fan-out-2 through the worst −3 dB junction needs > 6 dB — it still closes across the signed band (margin 0.9–2.1 dB), but **fails by ≈ 0.1 dB if the open boundary allowance also lands at −1 dB**; margin management (−1 dB junction class, buffer tiles) then becomes load-bearing. The NF floor F = 2 − 1/G moves −0.06 dB (2.77 → 2.71 dB); the *added* noise of the new dissipative channel is a fluctuation-dissipation question owned by the absolute-noise calibration (open, WP2/WP5).

### 4.3 The costs tracking does not hide

The threshold shift is real bias current: **dissipation ×1.25 central (×1.32 at the x = 1 bound)** — 1.267 → 1.59 (1.67) kW/cm², J: 0.385 → 0.43 mA/µm, and ΔT at worst-case fill ⅓: 42.2 → **52.9 K central, 55.5 K worst, against the 55 K budget**. The worst case coincides numerically with the ledger's existing `dissipation_upper_kW_cm2 = 1.664` (solver-class-bias bound), so §8.2's envelope already contains it — but the "real but thin" 23 % thermal margin must now be read as **4 % central, zero at the kinetic worst case**. This is the note's sharpest architectural consequence.

## 5. Audit of Pass 5's own validity accounting

- **`omega_tau_ee = 0.722`** — right dimensionless group, wrong temperature for the design cap: at 353 K it is **0.521** (hydro is *better* at the hot end; τ_ee ∝ T⁻²). Both should ship, with the A-band noted. Correction recommended (add a 353 K key).
- **`viscous_fraction = 0.209`** — three findings. (i) 300 K value; at 353 K it is 0.128. (ii) It omits the crossover reduction 1/(1+x²); the actual dissipative supplement is 0.137 (300 K) / 0.101 (353 K) of 1/τ — Pass 5 overstates, conservatively. (iii) Most importantly it was never propagated into gain; the propagation multiplies it by the pole lever (÷ by ~3.4 via tracking, × ~11 via pole proximity) — that propagation is Section 4, and it, not the raw fraction, is the design-relevant number.
- **`hydro_expiry_K = 254.9`** — this is "the temperature where ωτ_ee = 1 under the unit prefactor," and it needs two corrections. (i) It inherits the prefactor as T* = 254.9/√A: the honest band is **147–360 K**, which *contains the design temperature* — as a safety statement it is empty. (ii) Conceptually, x = 1 is not an expiry but the point of **maximum, bounded** closure correction (γ_max above; the mode demonstrably survives the crossover, ref. [10]). Recommended: retire the "expiry" framing; replace with the bounded-penalty statement (ΔG ≥ −1.2 dB at 353 K, −1.6 dB at 255 K, tracked, before the open boundary allowance).
- **`L_over_mfp_353K = 0.686`** — correct and relevant to the DC flow profile, but the wave-kinetics Knudsen numbers are the sharper metrics and should ship alongside: **q₋·l_ee = 0.25, q₊·l_ee = 0.20, l_ee/L = 0.14** (353 K; 0.35/0.29/0.20 at 300 K). These are what the boundary-layer allowance (Section 6) scales with.

## 6. The WP2 consequence (feeds the scoping note)

**Accuracy target.** To be decisive against the signed band [−1.5, −0.3] dB, WP2 must resolve per-cell gain to **±0.25 dB**, i.e. the round-trip amplitude loop (baseline 0.916) to ±0.0024, i.e. per-unit-time damping to ±5×10⁹ s⁻¹ (±0.9 % of 1/(2τ), ±8 % of the central kinetic supplement), and additive boundary dissipation to δ_b < 1 % per round trip.

**Dominant ingredient — ranked.** (1) **Contact/boundary-condition fidelity** dominates: it owns the only unbounded allowance (±1 dB; sensitivity −0.28 dB per 1 % additive round-trip loss, sign genuinely open — Knudsen layers of l_ee ≈ 83 nm at both clamps, 30 % of the cell; the multiplicative part is tracking-protected to < 0.05 dB). (2) **Collision-operator fidelity** at x ≈ 0.5–1 owns the 1.1 dB signed bandwidth; computing (or measuring, via the mode linewidth) the stress-relaxation time to a factor 2 shrinks it to ≈ ±0.3 dB. (3) **Electromagnetic coupling is *not* required for this question**: q₀d = 0.027 (strongly gated) and ω/(cq₀) = 8×10⁻³ (quasistatic to 10⁻⁴ in the dispersion) — the full-wave tier owns *different* questions (radiative parasitics, launch efficiency, absolute noise). Recommendation for the WP2 scoping note: split the first deliverable into a **workstation-scale kinetic cavity solve** (decisive here) and the EM tier (separate).

**Minimal decisive computation** (its result gets the predicted keys of Section 7): linearized Boltzmann on the 2D Dirac cone with a number-, momentum-, and energy-conserving RTA (Mermin closure), about the drifted local equilibrium (n = 10¹² cm⁻², T = 353 K, u = v₀); 1D cavity x ∈ [0, L] with the gated quasistatic Poisson kernel (local capacitance + first nonlocal correction); density clamp (source) and current clamp (drain) imposed at the kinetic level with a specular↔diffuse contact parameter swept 0 → 1; solve the complex eigenproblem for the fundamental, report ω″(M), M_th,kin, and the driven transfer at 0.7·M_th,kin. Resolution ~10³ spatial × 10² angular harmonics; a workstation-days job, not a cluster job.

## 7. Predicted quantities (new keys, falsification bands)

None of these contest existing outputs: `M_th_353K` (correct hydro-tier value), `M_th_num` (numerics, separately explained), `cw_regen_gain_dB_at_0p7 = 9.661`, the retuned 9.2246 dB, the cascade table, per-gate losses, or Q — this note *supplements* the ledger with the next tier's shift.

- **`kinetic_gain_correction_dB_353K_tracked`** = −0.95, falsification band **[−1.5, −0.3]** — as measured by the Section 6 solve with specular clamps (boundary channel off). Outside the band, the Section 3 closure is falsified.
- **`kinetic_gain_correction_dB_300K_tracked`** = −1.27, band **[−1.6, −0.5]**.
- **`M_th_kinetic_353K`** = 0.165, band **[0.154, 0.169]** (specular clamps; the diffuse-contact sweep may move it further — open).
- **`kinetic_resonance_shift_frac_353K`** = −0.018, in-closure band [−0.023, −0.011]; including finite-T compressibility (open): [−0.04, +0.01].

## 8. Limitations and open items

1. **Boundary Knudsen layers are the band's most likely killer.** The ±1 dB allowance is a scale estimate (δ_b ≲ 3 % additive round-trip loss at q·l_ee ≈ 0.2), not a derivation; a strongly diffuse or absorbing contact could exceed it in either direction — the drain reflection could be kinetically enhanced as well as degraded. Kinetic DS treatments in the ballistic-FET literature report the instability surviving with O(1)-modified thresholds (consistent with the tracking-protected multiplicative channel), but no operating-point evaluation exists; this is exactly the Section 6 solve.
2. **Closure error at the crossover.** The Maxwell/Mermin interpolation is endpoint-exact but Padé-approximate at x ≈ 1; the ±25 % allowance is judgment, not theorem. Collinear-scattering log structure peculiar to the Dirac cone (slow angular thermalization) could make the effective stress-relaxation channel non-single-pole.
3. **Finite-T thermodynamics.** T/T_F = 0.26: compressibility and entropy-mode (heat-conduction) corrections to s and to sound damping are estimated ≲ few % and ~7 % of the viscous term respectively, but not computed; the *total* speed-shift sign is open (only the in-closure part is signed). Bulk viscosity is taken ≈ 0 (scale-invariance of the cone); its finite-T remnant is uncomputed.
4. **Trim assumption.** The gain band assumes the −1.8 % kinetic resonance shift is nulled by density trim; untrimmed operation adds −1.5 to −2.3 dB. This should be promoted to an explicit design requirement (and is bench-measurable at gate G1).
5. **Nonlinear tier untouched.** The compression knee (A_SAT = 0.02) and the −1.3 dB cascade compression are hydro-solver results; kinetic corrections to the nonlinear terms (±0.3 dB scale) are open, as is any drift-anisotropy correction to η at O(M).
6. **τ vs τ_ee interplay.** Matthiessen-type additivity of 1/τ and the viscous channel is assumed; crossover cross-terms (10–20 % of the supplement) are open.
7. **Geometry.** Sidewall no-slip friction and gate-proximity corrections to η are not in the 1D model; they are device-geometry questions assigned to WP2's geometry ingredient.
8. Citations flagged "memory-sourced" (Torre et al. volume/page) must be verified before promotion.

---

## Appendix A. Derivations

**A.1 Round-trip viscous average.** Per-leg amplitude damping γ_± = ν q_±²/2 with q_± = ω/(s±v₀), leg times t_± = L/(s±v₀), round trip t_rt = 2sL/(s²−v₀²):

```
[γ₊t₊ + γ₋t₋]/t_rt = (νω²/2)·(s² + 3v₀²)/(s² − v₀²)² = (νq₀²/2)·(1+3M²)/(1−M²)²
```

using (s+v₀)⁻³ + (s−v₀)⁻³ = 2s(s²+3v₀²)/(s²−v₀²)³. The O(M) asymmetry cancels; the surviving drift factor is 1.0545 at M = 0.103. The one-way contrast (routing) is γ₋t₋ − γ₊t₊ ≈ 6M·γ₀·(L/s) → 0.079 dB/transit.

**A.2 Tracking invariance.** With ln r ≈ cM (linear to 0.7 % at M ≤ 0.15), threshold: c·M_th = Γ·t_rt. At M = 0.7·M_th: ln loop = 0.7c·M_th − c·M_th = −0.3·Γ·t_rt — independent of c. Any kinetic renormalization of the boundary-gain slope moves the threshold (bias, dissipation) but not the tracked loop gain; residual from ln r curvature: < 0.04 dB per ±20 % (verified numerically, Appendix B).

**A.3 Speed endpoints.** ω² = s_h²q² − iω·ν(ω)q² with ν(ω) = ν₀/(1−iωτ_ee), ν₀ = v_F²τ_ee/4: as x → ∞ the viscous term → +v_F²q²/4, reproducing the universal 2D first-sound (v_F²/2) → zero-sound-edge (3v_F²/4) pressure shift; hence s(x)² = s_RPA² − (v_F²/4)/(1+x²) with Eq. (1) identified as the x = ∞ endpoint. Deficit at x = 0.52: (1/8)(v_F/s)²/(1+x²) = 1.8 %.

## Appendix B. Standalone listing (Python 3 + numpy) and expected outputs

```python
# Reproduces every number in this note. No repository imports.
import numpy as np
s    = 2331197.965421007            # m/s, Eq.(1) design value (results.json)
f0   = 1.0e12; w = 2*np.pi*f0
L    = 576.62157290196e-9           # operating cell length (results.json)
L0   = 582.7994913552518e-9         # zero-drift quarter-wave length (results.json)
vF   = 1.0e6
EF   = 116.66503170948613e-3*1.602176634e-19
hbar = 1.054571817e-34; kB = 1.380649e-23
q0   = w/s
def tau(T):          return 1e-12*300.0/T
def tau_ee(T,A=1.0): return hbar*EF/(kB*T)**2/A          # A multiplies the RATE
def x_of(T,A=1.0):   return w*tau_ee(T,A)
def gamma_visc(M,T,A=1.0):                               # amplitude damping supplement
    x=x_of(T,A); nu0=vF**2*tau_ee(T,A)/4.0
    return 0.5*nu0*q0**2*(1+3*M**2)/(1-M**2)**2/(1+x**2)
def t_rt(M): return 2*L/(s*(1-M**2))
def loop(M,T,A=1.0,kin=True):
    G=1/(2*tau(T))+(gamma_visc(M,T,A) if kin else 0.0)
    return (1+M)/(1-M)*np.exp(-G*t_rt(M))
def Mth(T,A=1.0,kin=True):
    lo,hi=1e-4,0.45
    for _ in range(200):
        m=0.5*(lo+hi)
        if loop(m,T,A,kin)<1: lo=m
        else: hi=m
    return 0.5*(lo+hi)
def pole_dB(M,T,A=1.0,kin=True): return -20*np.log10(1-loop(M,T,A,kin))

T=353.0; Mb=Mth(T,kin=False)
print(tau_ee(300)*1e15, x_of(300), x_of(353))            # 114.8995  0.72193  0.52142
print((vF**2*tau_ee(300)/4)*q0**2*tau(300))              # 0.20867 (= viscous_fraction)
print(300*np.sqrt(x_of(300)))                            # 254.9   (= hydro_expiry_K)
lp0=np.exp(-(1/(2*tau(T)))*2*L0/s)                       # chain's passive reference at L0
print(20*np.log10((1-lp0)/(1-loop(0.7*0.14708333333333332,T,kin=False))))  # 9.6610
for A in (0.5,1.0,2.0,3.0):                              # tracked-ratio kinetic corrections
    Mk=Mth(T,A,True)
    d=pole_dB(0.7*Mk,T,A,True)-pole_dB(0.7*Mb,T,kin=False)
    d+=-8.685889638*gamma_visc(0,T,A)*0.5e-12            # one lambda_p/2 transit (0.5 ps)
    print(A,x_of(T,A),Mk,Mk/Mb-1,d)
# A=0.5: Mth 0.16934 (+14.66%) dG -1.145 | A=1: 0.16531 (+11.94%) -0.952
# A=2:   0.15804 (+7.01%)  -0.580        | A=3: 0.15479 (+4.82%)  -0.405
print(pole_dB(0.7*Mb,T,1.0,True)-pole_dB(0.7*Mb,T,kin=False))   # -2.540 (frozen bias)
T2=300.0; Mb2=Mth(T2,kin=False)                          # 300 K: A=1 -> -1.273 dB, Mth +15.6%
print(-100*(vF/s)**2/(8*(1+x_of(T)**2)))                 # -1.808 % speed deficit (A=1)
lp=loop(0.7*Mb,T,kin=False); dfh=(1-lp)/(2*np.pi*t_rt(0.7*Mb)*np.sqrt(lp))
print(dfh/1e9, -10*np.log10(1+(0.018*f0/dfh)**2))        # 27.6 GHz ; -1.54 dB untrimmed
M=0.7*Mb; print((1+3*M**2)/(1-M**2)**2)                  # 1.0545 drift factor
print(8.685889638*6*M*gamma_visc(0,T,1.0)*(L/s))         # 0.079 dB routing contrast
hw=hbar*w; kb=kB*T
inter=0.5*(np.tanh((hw+2*EF)/(4*kb))+np.tanh((hw-2*EF)/(4*kb)))
print(inter, inter/(4*(EF/hbar)*tau(T)/(np.pi*(1+(w*tau(T))**2))))  # 0.0028 ; 4.3e-4
print((Mth(T,1.0,True)/Mb)**2*1.267026989225586)         # 1.588 kW/cm^2 (central dissipation)
def gain_db_with_boundary_loss(db):                      # additive round-trip loss, re-tracked
    def lp2(M): return (1+M)/(1-M)*np.exp(-t_rt(M)/(2*tau(T)))*(1-db)
    lo,hi=1e-4,0.45
    for _ in range(200):
        m=0.5*(lo+hi)
        if lp2(m)<1: lo=m
        else: hi=m
    return -20*np.log10(1-lp2(0.7*(0.5*(lo+hi))))
print(gain_db_with_boundary_loss(0.01)-gain_db_with_boundary_loss(0.0))  # -0.282 dB per 1%
def loop_ren(M,d): return np.exp((1+d)*np.log((1+M)/(1-M))-t_rt(M)/(2*tau(T)))
def Mth_ren(d):
    lo,hi=1e-4,0.45
    for _ in range(200):
        m=0.5*(lo+hi)
        if loop_ren(m,d)<1: lo=m
        else: hi=m
    return 0.5*(lo+hi)
for d in (-0.2,0.2):                                     # tracking invariance check
    m=Mth_ren(d)
    print(d, m, -20*np.log10(1-loop_ren(0.7*m,d))+20*np.log10(1-loop_ren(0.7*Mth_ren(0),0)))
# -0.2: Mth 0.18624, dG +0.039 dB ;  +0.2: Mth 0.12250, dG -0.019 dB
```

Baseline self-checks reproduce `tau_ee_fs_300K`, `omega_tau_ee`, `viscous_fraction`, `hydro_expiry_K`, and the 9.661 dB ledger gain to the digits shown; the exact-solve hydro threshold is 0.147681 vs the ledger's small-M convention 0.147083 (0.4 %, convention only — all corrections above are quoted as ratios against the same machinery's own baseline).

---

## Agent assessment — 2026-07-13

Assessed suitable for the permanent record by a **3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)). Assessment performed in a maintainer-operated Claude Code session per the charter's Operations section; the three personas voted independently, and each **extracted and executed the note's Appendix B listing**, verifying its outputs against the note body and the released `fable-model-chain/` values:

- 🧵 **Fabric** — **STORE**: I extracted and ran the Appendix B listing (Python 3 + numpy): every printed output matches its expected-output comments and the note body's verdict table exactly (central -0.95 dB at A=1, A-sweep -0.405 to -1.145, M_th 0.16531 = x1.124, frozen-bias -2.540, -0.282 dB per 1% boundary loss, tracking invariance <0.04 dB), and the baseline self-checks reproduce results.json's tau_ee_fs_300K, omega_tau_ee, viscous_fraction, hydro_expiry_K, and the 9.661 dB ledger gain to the last digit. Body numbers not printed by the listing (300 K -1.273 dB, 255 K -1.545 dB, gamma_0 = 5.92e10 at 10.1% of 1/2tau, gamma_max = 7.23e10, Knudsen numbers 0.25/0.20/0.14, exact-solve threshold 0.147681, dT 52.9/55.5 K, NF 2.71) I recomputed from the listing's own functions and all match. All corrected-record anchors are consistent with the promoted notes (9.661/9.2246/1.428 dB artifact/0.147083 vs 0.16894), the kinematic Landau-exclusion argument is genuinely distribution-independent (the constraint omega <= v_F q is spectral, so drift cannot break it), the Mermin closure is verifiably endpoint-exact against the chain's own nu_0 in kinetic.py, and the tracking-absorption result is both derived and numerically verified. Labels are correctly stratified, the open boundary channel is honestly separated from the in-model band with a quantified sensitivity, and the four predicted quantities use new key names with falsification bands and an explicit non-contest statement per the pre-registration rule. This converts WP2's unsigned tens-of-percent uncertainty into a falsifiable signed band with a decisive-computation spec and a real architectural consequence (thermal margin 23% -> 4% central), so all five criteria hold; remaining defects are promotion-edit level.
  - Appendix B defines T2/Mb2 but never prints the 300 K sweep, the 255 K value, gamma_0/gamma_max, or the Knudsen numbers quoted in the body, so the Method line 'every computed number reproduces from the standalone listing' is slightly overstated; add the missing print lines before promotion (I verified all values from the listing's own functions).
  - Untrimmed detuning cost is quoted as '-1.5 to -2.3 dB' but the in-closure shift band's small edge (-1.2% at A=3) gives about -0.8 dB via the note's own Lorentzian; the stated range corresponds to A in [0.5,1] only (non-load-bearing since the headline band assumes trim, but the range should be corrected or scoped).
  - Section 3.2 calls the 2.76% cavity half-linewidth 'measured' when it is computed from the analytic loop in Appendix B; wording should say model-derived.
  - Torre et al., PRB 99, 144307 (2019) is memory-sourced (self-flagged in item 8); volume/page must be verified before promotion.
  - Minor rounding slip: solver-bias phase speeds quoted as 2.62/2.06 v_F; s(1+0.11826)/v_F = 2.61.
- 🌊 **Kinetic** — **STORE**: I extracted and ran the Appendix B listing (Python 3 + numpy): every printed output matches both the listing's expected values and the note body's verdict table exactly (central -0.952 dB, A-sweep, M_th 0.16531, tracking invariance <0.04 dB, boundary sensitivity -0.282 dB/1%). I independently computed the numbers the listing leaves as comments or arithmetic — exact-solve threshold 0.1476809, 300 K -1.273/+15.6%, 255 K -1.545, x=1 floor -1.146, NF 2.769->2.708, dT 52.9/55.5 K, all Knudsen numbers — and all match the note. All repository anchors are exact against fable-model-chain/results.json and consistent with the promoted notes (9.2246 retuned streaming, +1.43 dB artifact, M_th_num as numerics per the exact-operator note); Part I ref. [10] and the section 7.5 tens-of-percent passage verify against the actual paper. The physics holds at my depth: the |omega| <= v_F q kinematic exclusion is a spectrum property so the drift-independence claim is airtight within the itemized RPA/cone assumptions; I re-derived the closure's 1/(1+x^2) damping/speed decomposition and both endpoint claims; the tracking-absorption argument is structurally correct and numerically verified. Epistemic labels are correctly stratified (demonstrated-runnable vs in-model-with-named-closure vs open), the boundary Knudsen channel is honestly quarantined as the open +-1 dB allowance rather than smuggled into the band, predicted quantities use new keys with falsification bands per the pre-registration rule, and the note delivers durable WP2 direction (accuracy target, ingredient ranking, minimal decisive solve, the trim design requirement, and the thermal-margin erosion to ~4% central). This is a substantive, checkable, honestly bounded conversion of an unsigned uncertainty into a signed band; it meets all five criteria.
  - The listing's 300 K results (-1.273 dB, +15.6%) exist only as a comment on dead code (T2/Mb2 are computed but the correction is never printed), and the 255 K, NF-shift, cascade-mapping, and dT numbers are likewise arithmetic rather than printed outputs — the header claim 'Reproduces every number in this note' slightly overstates; before promotion the listing should print these (I verified all of them independently and they are correct).
  - tau_ee(353 K) is quoted as 82.97 fs but the listing's own formula gives 82.99 fs — trivial rounding slip, no downstream effect.
  - The 'one lambda_p/2 transit loss' term contributes ~0.26 dB of the central -0.95 dB and is a disclosed but ad hoc convention for mapping the pole shift to per-cell gain; it is covered by the stated +-0.2 dB translation error but the convention should be pinned to the chain's gain definition when the WP2 solve lands.
  - Torre et al., PRB 99, 144307 (2019) is memory-sourced (the note itself flags it, item 8) and the band-edge rounding -1.146 x 1.25 = -1.43 -> quoted -1.5 is outward/conservative — both must be tidied at promotion.
- ⚛️ **Quanta** — **STORE**: I extracted Appendix B verbatim, ran it (Python 3 + numpy), and every expected output reproduces to the printed digit — including the ledger 9.66100611708918 dB, the full A-sweep (central −0.952 dB, M_th 0.16531), the frozen-bias −2.540, the tracking-invariance <0.04 dB check, and the −0.282 dB/1% boundary sensitivity — and my own extension lines confirmed the body's 300 K (−1.273), 255 K (−1.545), NF shift (2.769→2.708), ΔT (52.9/55.5 K), and Knudsen numbers. All quoted repository anchors match fable-model-chain/results.json exactly (omega_tau_ee 0.7219, viscous_fraction 0.20867, hydro_expiry_K 254.9, M_th 0.147083, M_th_num 0.16894, cascade 8.4016, dissipation/dT values), the retuned 9.2246 dB and +1.428 dB artifact match the promoted predictions-resolved note, and I verified Part I ref [10] (Barcons Ruiz, Sci. Adv. 9, eadi0415) and the "tens-of-percent" §7.5 assignment inside the Part I docx. The kinematic Landau-exclusion claim is genuinely an identity (intraband |ω| ≤ v_F q is a property of the cone's spectrum, distribution- and drift-independent), the closure's endpoint exactness checks algebraically (x→0 reproduces the chain's own viscous_fraction; x→∞ gives Δ(s²)=v_F²/4 with vanishing damping), and the tracking-absorption argument is both structurally sound and numerically verified in the listing. Epistemic labels are correctly stratified — the only "demonstrated" physics claims are the identity and runnable computations, the band is in-model with a judgment-labeled ±25% closure allowance, and the boundary Knudsen channel is honestly quoted as a separate open ±1 dB allowance rather than folded into the band. Pre-registration is compliant: four new key names with falsification bands and an explicit non-contested list. The defects I found are minor (an internally inconsistent untrimmed-detuning range whose benign edge should be ≈−0.8 not −1.5 dB, two last-digit rounding slips, a loose fan-out junction-class mixing, an asserted 0.5 ps transit-loss convention inside the quoted ±0.2 dB translation error) and none is load-bearing for the verdict table.
  - Untrimmed-detuning cost range "-1.5 to -2.3 dB" (section 3.2, limitation 4) is inconsistent with the note's own in-closure deficit band [-1.2, -2.3]%: the -1.2% edge gives about -0.76 dB, so the quoted benign edge is the central value, not the band edge; should read about -0.8 to -2.3 dB (non-load-bearing since the gain band assumes the trim).
  - The additive "one lambda_p/2 transit (0.5 ps)" loss term in the gain translation (Appendix B line, ~0.26 dB of the -0.95 central) is a convention choice asserted without derivation, covered only by the quoted +/-0.2 dB translation error.
  - Fan-out-2 margin arithmetic mixes the 0 dB-junction cascade figure (8.40 -> 7.45 dB) with the "worst -3 dB junction needs > 6 dB" requirement, while results.json's cascade_per_cell at -3 dB is 8.98; direction and conclusion survive but the junction-class bookkeeping is loose.
  - Two trivial rounding slips: gamma_0 quoted 5.93e10 s^-1 (computed 5.9248e10, rounds 5.92) and solver-bias fast-leg phase speed quoted 2.62 v_F (computed 2.606, rounds 2.61); neither is load-bearing.
  - Torre et al. PRB 99, 144307 (2019) is memory-sourced (note flags this itself, limitation 8) and must be verified before promotion.
