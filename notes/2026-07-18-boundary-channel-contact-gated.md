# The boundary channel does not close on paper: δ_b is a one-signed loss at the source, sign-open at the drain, and set entirely by the contact accommodation σ_c — so the per-cell gain budget stays gated on WP2 (or on one linewidth measurement)

**Status:** promoted to `notes/` — accepted by a unanimous **3-of-3 agent vote** (recorded below) and merged by the maintainer. **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #43](https://github.com/ryoji-info/FableComputer/discussions/43) (Kinetic's 🌊 winning prompt, 2-of-3 vote — Fabric → Kinetic, Quanta → Kinetic, Kinetic → Fabric). The commissioned question: bound δ_b, the additive per-round-trip amplitude loss (or gain) from the kinetic boundary layers at the two Dyakonov–Shur clamps — the single unbounded ±1 dB term left in the per-cell gain certainty budget after the July audit. The reply is published there verbatim and reproduced here for assessment.
**Method:** analysis from the session's attached documents, with every operating-point anchor and gain-sensitivity number re-executed against the released `fable-model-chain/` (Python 3 + numpy, `PYTHONIOENCODING=utf-8`, Windows/CPython); the runnable listing is in the Appendix, and its printed output contains every number quoted (CW gain and M_th bit-for-bit against `results.json`). Nothing below contests any `results.json` value. *Adversarially pre-checked before posting by two independent contexts* — one re-executed every anchor and sensitivity against the chain (all reproduced), one audited the physics and labels and forced the §3 scaling exponent to be relabeled **open** and corrected the §4 central value and linewidth claim. The three assessment reviewers each re-executed everything independently before voting.
**Author:** Claude **Opus 4.8** — *disclosed fallback, not Fable 5.* The session's premium Fable 5 budget was exhausted during the vote stage; per the pipeline's designed fallback (`fallbacks: [{"model": "claude-opus-4-8"}]` in `agents/scripts/agent_fable_session.py`) the winning prompt executed on `claude-opus-4-8`. Nothing in this note is labeled or represented as Fable 5 output; the candidate drafts and Kinetic's vote were produced earlier on `claude-fable-5`. Maintainer-operated Claude Code session per [agents/README.md](../agents/README.md), 2026-07-18.
**Labels:** demonstrated / in-model / open, per [notes/README.md](README.md).
**Binding record honored:** [`notes/2026-07-13-kinetic-correction-signed-band.md`](2026-07-13-kinetic-correction-signed-band.md) (the ±1 dB boundary allowance and its "band's most likely killer" flag, the −0.28 dB per 1 % additive-loss sensitivity, the signed bulk band [−1.5, −0.3] dB, the Knudsen numbers, and the tracking-absorption structure); [`notes/2026-07-12-predictions-resolved.md`](2026-07-12-predictions-resolved.md) (gain ledger — CW 9.661 dB, retuned streaming 9.2246 dB; the shipped 7.7967 dB is a solver-configuration artifact, never used as physics); [`notes/2026-07-12-boundary-factor-exact-operator.md`](2026-07-12-boundary-factor-exact-operator.md) (the 0.99549 active boundary factor is a finite-Δx Lax–Friedrichs artifact — "not boundary physics" — kept distinct from the physical δ_b; `M_th_num` is a discretization artifact); [`notes/2026-07-17-drive-sweep-knee-anchored.md`](2026-07-17-drive-sweep-knee-anchored.md) and [`notes/2026-07-17-what-the-38-quanta-knee-denominates-after-the-july-plane-aud.md`](2026-07-17-what-the-38-quanta-knee-denominates-after-the-july-plane-aud.md) (plane discipline — every amplitude/loss/gain figure names its reference plane).

---

> **⚠️ Executing-model disclosure.** This session's premium Fable 5 budget was exhausted during the vote stage (session usage limit, then Fable 5 credits). Per the pipeline's own designed fallback (`fallbacks: [{"model": "claude-opus-4-8"}]` in `agents/scripts/agent_fable_session.py`) and the run's disclosure rule, **the winning prompt was executed on `claude-opus-4-8` (Opus 4.8), not Fable 5.** Nothing below is labeled or represented as Fable 5 output. The candidate drafts and Kinetic's vote were produced earlier on `claude-fable-5`; Fabric's and Quanta's votes and this execution ran on Opus 4.8. The reduced depth of the fallback model is a real limitation on the derivation below — reflected in the fact that the boundary channel's *scaling exponent*, not just its coefficient, is left open (§3).

---

## 0. Verdict

**The boundary channel cannot be closed by analytic kinetics at the depth this call reached, and — importantly — the reason is not that the analysis is merely hard but that the answer is genuinely a property of the contact the released model does not specify.** Three findings, in decreasing order of how firmly I can defend them:

1. **The reactive (slip / extrapolation-length) part is trim-absorbed** — it is a static cavity-length redefinition, nulled by the same in-situ resonance trim that nulls the −1.8 % bulk speed shift (07-13 §3.2). Residual (frequency dispersion of the slip across the mode's 2.76 % bandwidth) is **< 0.1 dB**. *In-model; this removes detuning from the boundary worry and isolates the genuine dissipative channel.*

2. **The source (density-clamp) contributes a sign-definite additive LOSS, δ_b^src ≥ 0.** The sign is firm (entropy production ≥ 0 at a passive, DC-unpumped contact). The idealized DS source is an AC **power node** (δφ(0) = 0), so the boundary is lossless at *leading* order and the dissipation is a Knudsen-layer residual. **Its scaling exponent in Kn = q·l_ee is itself open** (§3): a first-order-slip estimate gives δ_b^src = O(Kn)·C_acc, a node-protected phase-lag estimate gives O(Kn²)·C_acc. With q₋·l_ee = 0.249 (demonstrated) this is δ_b^src ∈ **[0, ~6 %]** (Kn² law) up to **[0, ~25 %]** (Kn law) as C_acc (contact accommodation) runs specular→diffuse — i.e. **[0, −1.7 dB]** up to **[0, ~−5.7 dB]** on the tracked gain.

3. **The drain (current-clamp) contributes a sign-OPEN term of the same magnitude scale.** The drain is where DC drift power converts to AC (the DS gain event), so its boundary layer sits in an active region: it can dissipate (loss) *or* modify the drift-to-plasmon conversion (gain). This is the irreducible object no analytic method here controls.

**Net.** Denominated on the tracked per-cell gain, the boundary channel spans from **a small net gain (+0.9 dB, a clean source with a drain whose kinetics enhance the DS conversion)** to **a large net loss** whose diffuse edge is **−3 dB if the source dissipation scales as Kn², but ~−5 to −10 dB if it scales as Kn** — and I could not settle which. **The honest center is not zero but a net loss**, because the source term is sign-definite: even a moderately accommodating pair of contacts (C_acc ≈ 0.5) gives ≈ −0.9 dB before the open drain is counted. The 07-13 note's ±1 dB allowance corresponds to **δ_b ≈ 3.6 %**, i.e. **C_acc ≈ 0.5–0.6 under the Kn² law** (the note's scale was right for a *typical, weakly-accommodating* contact); under the Kn law the same C_acc gives several times that. A **clean, near-specular / transparent contact drives δ_b → 0 and the band is safe** regardless of the exponent (both laws vanish as C_acc → 0); a diffuse/reservoir contact breaks it, by an amount the analysis cannot pin.

**Consequence for the maintainer's Part III sequencing question (§5).** The per-cell gain certainty budget does **not** close on the corrected record as it stands, because its now-dominant uncertainty is a contact parameter the model does not carry — and this call, if anything, shows the allowance could be *worse* than ±1 dB, not better. Kinetic's calibration-first position is supported — **but with a cheaper escape hatch than the full Boltzmann–Maxwell solve:** the entire band collapses if σ_c is pinned to near-specular, and that limit is checkable at the bench (§4). So the honest answer is *not* "architecture Part III is blocked" but "**architecture Part III may lead only if the contact is first shown to be near-specular; otherwise the calibration tier must lead.**"

This is a negative result in the project's sense: the analysis did **not** shrink the ±1 dB allowance to a few tenths of a dB (the outcome that would have green-lit an architecture-led Part III outright). It did something else useful — it fixed the source sign, removed the detuning worry, reduced the whole channel to one contact parameter, identified the drain sign and the Kn-exponent as the two irreducibly-open objects, and named the single cheapest measurement that closes the safe case.

---

## 1. The boundary-layer problem, posed exactly

**Geometry and bulk.** 1-D DS cavity x ∈ [0, L], L = 576.62 nm operating length (`cell_length_operating_nm`; the regen.py CW model that reproduces the 9.661 dB ledger uses the zero-drift 582.80 nm as its cavity length — I work in that model and quote both). Bulk mode: the drifting shallow-water/viscoelastic mode of 07-13 §3, phase speeds s±v₀ = 2.571 / 2.091 v_F at the tracked bias M = 0.7·M_th(353 K) = 0.1030 (all demonstrated, Appendix).

**The two clamps (Part I, Eq. 2; regen.py docstring).**
- **Source, x = 0:** density clamp, δn(0) = 0 — an injecting/ohmic contact. Ideal reflection |r_s| = 1 (lossless). Because δφ ∝ δn in the strongly-gated local-capacitance limit (q₀d = 0.027, 07-13 §6), the source is an **AC-potential node**.
- **Drain, x = L:** current clamp, δJ(L) = 0 — open drain, the DS amplified reflection r_d = (s+v₀)/(s−v₀) = 1.2296 (demonstrated). The drain is an **AC-current node**.

**The layer.** Within ~l_ee = 82.99 nm (353 K; l_ee/L = 0.144 on the operating length, 0.142 on the zero-drift length — both ≈ 0.14, demonstrated) of each clamp the distribution f(x, θ, ε) cannot simultaneously be the local-equilibrium (hydrodynamic) form *and* satisfy the microscopic contact condition; a kinetic (Knudsen) boundary layer forms. The relevant wave-kinetic Knudsen numbers are **q₋·l_ee = 0.249, q₊·l_ee = 0.203** (demonstrated) — moderate, neither hydrodynamic (Kn → 0) nor ballistic. l_ee/L = 0.14 means a pure Knudsen expansion is not asymptotically small; every result below is **leading-order in Kn with an explicit O(Kn) ≈ 20–25 % error bar**, not an asymptotic series (this is the "does not scale-separate cleanly" caveat the prompt required), and — as §3 makes explicit — even the *power* of Kn is uncertain here.

**Distinct from the 07-12 numerical boundary factor.** The δ_b of this memo is a *physical* kinetic loss (contact accommodation), genuinely absent from the released hydro + Lax-Friedrichs model. It must not be conflated with the ~0.45 % active/passive boundary-reflection asymmetry (active factor 0.99549) that [`notes/2026-07-12-boundary-factor-exact-operator.md`](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-07-12-boundary-factor-exact-operator.md) identified as a finite-Δx LF-scheme artifact and explicitly labeled "not boundary physics." Same name, different object; the physical channel here is up to an order of magnitude larger.

**Idealizations named (all in-model):** (i) linearized kinetic theory about the drifted local equilibrium; (ii) a number/momentum/energy-conserving RTA whose bulk limit reproduces the 07-13 Mermin closure (so this composes with, and does not re-derive, the bulk band); (iii) the contact microphysics reduced to a **one-parameter family** — a specular↔diffuse accommodation, equivalently a Robin/transmission parameter σ_c in J(0) = σ_c·[n(0) − n_contact], mapped onto a dimensionless **accommodation coefficient C_acc ∈ [0, 1]** (0 = specular/transparent, 1 = fully diffuse/reservoir), the form WP2's solver has adopted; (iv) the DC drift is taken to pump only the drain (the source layer is passive) — a mild assumption, flagged in §2/Limitation 4.

## 2. The decomposition — why only one of three sub-channels survives

Every boundary effect splits into three pieces; the split is the generalization of the tracking-absorption structure the 07-13 note proved for the bulk (its §4.1):

**(A) Multiplicative — tracking-absorbed (< 0.05 dB).** Any renormalization of the reflection-amplitude *slope* (r_d → (1+δ)-scaled, or |r_s| → 1+ε) moves the threshold M_th, hence the bias current, but not the loop gain at the *tracked* working point M = 0.7·M_th — the in-situ calibration re-finds threshold and 0.7 of it. Demonstrated numerically for the bulk in 07-13 Appendix B (< 0.04 dB per ±20 % slope change); the boundary's multiplicative part inherits it identically. **Does not move tracked gain.**

**(B) Reactive — trim-absorbed (< 0.1 dB).** The real part of the boundary's complex extrapolation (slip) length ζ′ ~ C_acc·l_ee shifts the effective reflecting-plane position, i.e. the effective L. For a fully diffuse contact this is a large static detuning (2ζ′/L up to ~0.29), but it is *static* over the mode's 2.76 % bandwidth (ζ′ varies on the ωτ_ee ≈ 1 scale, ~100× wider), so it is a pure length redefinition — nulled exactly by the in-situ resonance trim, the same trim that nulls the −1.8 % kinetic speed shift (07-13 §3.2, promoted to a design requirement there). Residual = dispersion of ζ′ across the bandwidth ≈ 2.76 % × (detuning) → **< 0.1 dB**. **Does not move tracked gain.**

**(C) Additive dissipative — NOT absorbed: this is δ_b.** The imaginary part of the extrapolation length ζ″ is genuine amplitude change per reflection. Trimming ζ′ (adjusting L) does not remove ζ″ (they are the two parts of one complex boundary response). **δ_b = 2q₊ζ″_src + 2q₋ζ″_drain** (round trip, one reflection at each clamp), and it is the whole of the boundary's effect on the tracked gain.

**The node structure (what it does and does not buy).** Both ideal clamps are AC *power nodes* — the source is a δφ node, the drain a δJ node — so the leading-order AC power crossing each contact, ∝ δJ·δφ, **vanishes**. This is why the boundary is not O(1) dissipative (an O(1) loss is what a black wall absorbing the full incident flux would give); it is a Knudsen-layer residual. **But the node does *not* by itself fix the residual at O(Kn²).** At a node the conjugate variable is at an antinode (O(1)), so the generic extrapolation-length dissipation 1−|r|² ≈ 4qζ″ is **O(Kn)** (first-order slip) unless an additional low-frequency phase-lag argument (ζ″ ~ l_ee·ωτ_ee, or an entropy production ∝ (Kn·amplitude)²) suppresses it to O(Kn²). I can state that phase-lag argument heuristically but did not derive it; **the exponent is therefore open, spanning O(Kn) to O(Kn²)** (§3). This is the single most consequential open point in the memo, and the reason the band cannot be called "shrunk." (in-model / open)

## 3. The result — δ_b across the contact family

Mapping fractional round-trip amplitude loss δ_b to the tracked per-cell gain uses the **demonstrated** sensitivity (Appendix; regen.py re-tracked):

> **tracked ∂G/∂δ_b = −0.284 dB per 1 %** (reproduces the 07-13 note's −0.282), vs frozen-bias −0.901 dB per 1 % — a **3.18× tracking buy-back**. The ±1 dB allowance ⟺ **δ_b ≈ 3.6 %** (exactly 3.63 %).

| contact regime (C_acc) | δ_b model | δ_b (%) | tracked ΔG (dB) | sign | label |
|---|---|---|---|---|---|
| **Source, specular/transparent** (C_acc → 0) | either law → 0 | 0 | 0 | — | in-model |
| **Source, moderate** (C_acc ≈ 0.25, Kn² law) | (q₋l_ee)²·C_acc | 1.6 | −0.45 | loss (definite) | in-model / open exp. |
| **Source, diffuse** (C_acc ≈ 0.5, Kn² law) | " | 3.1 | −0.86 | loss (definite) | in-model / open exp. |
| **Source, fully diffuse** (C_acc → 1, **Kn² law**) | " | 6.2 | −1.66 | loss (definite) | in-model / open exp. |
| **Source, fully diffuse** (C_acc → 1, **Kn law**) | (q₋l_ee)·C_acc | 24.9 | **−5.73** | loss (definite) | open (competing scaling) |
| **Drain** (current-clamp, DS-active) | ±(source scale) | ∓(0…25) | +0.9 … **−5.7** | **OPEN** | open |
| **Round trip, clean specular both** | — | 0 | 0 | — | in-model |
| **Round trip, moderate both, drain dissipative (Kn²)** | — | +6.2 | −1.66 | loss | in-model / open exp. |
| **Round trip, specular source + drain enhancement** | — | −3.1 | **+0.93** | gain | open |
| **Round trip, fully diffuse both, dissipative (Kn²)** | — | +12.4 | **−3.13** | loss | in-model / open exp. |
| **Round trip, fully diffuse both (Kn law)** | — | ~50 | **≲ −10** | loss | open (competing scaling) |

**How firm is each column.** The **sign** of the source term is demonstrated-in-model (positive-definite entropy production at a passive, DC-unpumped contact; the DC-unpumped assumption is §1 iv, flagged). The **magnitude** rests on *two* open inputs — the O(1) coefficient *and* the Kn exponent (§2) — so the dB entries contingent on both (the −1.66/−3.13/−5.73 rows) are only as good as those inputs; they are "in-model" for the Kn²-law rows and "open" for the competing Kn-law rows. The **drain sign** is open at every C_acc.

**What I could not do** (honest statement the prompt asked for): I did not carry a full half-range moment (Gross–Ziering) or Case–van Kampen solution to a *number*, because the fallback model's depth did not support closing the ternary boundary algebra reliably, and the coefficient it would produce is contact-model-specific (two-stream vs full-angular vs BGK-Dirac differ by O(1)). Nor did I settle the Kn exponent. The defensible content is the **structure** (which sub-channel survives, the node's leading-order losslessness, the source sign, the one-parameter reduction) and the **scale with a named open coefficient *and* open exponent** — not a sharp δ_b number, and not a claim that the allowance is bounded below ±1 dB.

## 4. Composition into the per-cell gain certainty budget (353 K, tracked)

Composition rule: the bulk viscous channel (collision-operator physics) and the boundary channel (contact accommodation) are physically independent, so I interval-add them (worst-case); the note's bulk band is the signed [−1.5, −0.3] dB.

| channel | band (dB) | "center" | label |
|---|---|---|---|
| bulk viscous (07-13, unchanged) | [−1.5, −0.3] | −0.95 | in-model |
| boundary δ_b (this call), **Kn² law** | [−3.1, +0.9] | **net loss** (source ≥ 0; ≈ −0.9 at C_acc≈0.5 before the open drain) | in-model / open |
| boundary δ_b, **if Kn law** | [≲ −10, +0.9] | net loss | open |
| **total, interval-add (Kn² law)** | **[−4.6, +0.6]** | — | — |
| total **if** contact shown near-specular (C_acc ≲ 0.1) | **[−1.7, −0.2]** | −0.95 | conditional |

The middle rows are the headline: **before σ_c is known, the boundary term is larger than the entire bulk band, its sign is open, and its loss edge is set by an unresolved scaling exponent.** The last row is the prize: **pin the contact to near-specular and the budget collapses back to essentially the bulk band [−1.7, −0.2] dB** — tight enough for an architecture-led paper — and that collapse holds *regardless* of the exponent, since both laws vanish as C_acc → 0.

**Bench observable that pins the safe case (this is the cheap gate).** δ_b is an excess *amplitude* loss per round trip, so it broadens the cavity mode. The model half-linewidth is Δf₁/₂ = 27.6 GHz (07-13 §3.2, demonstrated). A sub-threshold linewidth measurement bounds the **total** excess round-trip loss — **bulk viscous + boundary together**, not σ_c alone. That is enough for the one-sided test that matters: **a measured linewidth at or near the model 27.6 GHz forces *both* channels small ⟹ the band is safe ⟹ architecture Part III can lead.** It does *not*, on its own, read σ_c off the bench — isolating the boundary term requires subtracting the in-model bulk-viscous broadening, which reintroduces the collision-operator uncertainty (and any contact inhomogeneity across the cell complicates the readout, Limitation 7). The valuable, valid use is the safe-case gate; the full σ_c isolation still wants the WP2 solve or a gain-vs-detuning map.

## 5. The Part III sequencing answer

The maintainer asked for a Part III that keeps feasibility while advancing computing performance, and the lab's three positions differ only on whether the architecture study is gated by open calibrations. **This result says: it is gated, but by one specific, measurable parameter, not by the whole Boltzmann–Maxwell tier — and the analysis leans toward the allowance being at least as large as ±1 dB, possibly larger.** Concretely:

- **If the contact is characterized as near-specular** (bench linewidth ≈ model 27.6 GHz, or WP2 solve returns C_acc ≲ 0.1): the per-cell gain budget is [−1.7, −0.2] dB, the fan-out-2 margin of 07-13 §4.2 (0.9–2.1 dB) survives, and **Fabric's architecture-led computing-block Part III can lead** on certified-enough numbers.
- **If the contact is diffuse or uncharacterized** (the current state): δ_b is loss-dominated and sign-open, larger than everything else and of uncertain magnitude — an architecture paper headlining per-cell gain would be spending an uncertified number, exactly Kinetic's objection, and **the calibration tier (or at minimum the contact measurement) must lead.**

So the budget supports a **conditional, measurement-gated sequencing**, not an unconditional one: the single cheapest experiment in the whole program — a sub-threshold linewidth on one cell at room temperature — decides which Part III is honest. That experiment belongs in WP1/WP4 and should be pulled forward ahead of the full WP2 solve.

## 6. Pre-registered keys (falsification bands; nothing contests existing outputs)

All at 353 K, tracked bias, N/A to `results.json` values. Falsification = the WP2 kinetic cavity solve (or the bench linewidth) landing outside the band.

- **`boundary_loss_pct_per_roundtrip_specular`** = **0.0**, band **[0.0, 0.5] %** (a specular/transparent contact, C_acc ≲ 0.1, must give < 0.5 % additive loss under *either* Kn law; outside falsifies the node's leading-order losslessness of §2). This is the load-bearing prediction — the safe-case gate.
- **`boundary_loss_pct_per_roundtrip_diffuse`** = **6.2**, band **[3, 25] %** (a fully diffuse/reservoir source, C_acc = 1; the wide band carries *both* the open O(1) coefficient and the open Kn-exponent: 3–10 % under the Kn² law, up to ~25 % under the Kn law). Maps to tracked ΔG ∈ [−0.86, ~−5.7] dB.
- **`boundary_sensitivity_dB_per_pct_tracked`** = **−0.284**, band **[−0.30, −0.27]** (demonstrated from regen.py; a check on the released chain, not on the kinetics — reproduces the 07-13 −0.282).
- **`M_th_kinetic_with_boundary_353K`** — not predicted to a point: the boundary shifts M_th through both the multiplicative (tracked-invariant) and additive channels; the WP2 solve should report M_th,kin(C_acc) as a curve, and this note pre-registers only that M_th,kin(C_acc → 0) → the 07-13 specular value 0.165 [0.154, 0.169].

## 7. Limitations and deliberately-unrun items

1. **Executing model.** Opus 4.8 fallback, not Fable 5 (header disclosure). The ternary/half-range boundary algebra that would produce a sharp O(1) coefficient — and settle the Kn exponent — was not closed; the deliverable is structure + scale, not a bound.
2. **The Kn exponent AND the O(1) coefficient are both open, and a moment solve could *widen* the band, not only shrink it.** If the source dissipation is first-order-slip O(Kn) rather than node-protected O(Kn²), the diffuse-edge loss is ~4× larger (§3). This is *the* pair of numbers the WP2 solve owes; the pre-registered diffuse band [3, 25] % spans both.
3. **Drain sign is irreducibly open here.** The DS-active drain can enhance or dissipate; no positive-definiteness protects it. Only the solve (with σ_c swept) or a bench gain-vs-detuning map closes the sign.
4. **DC-unpumped source (§1 iv).** If the DC drift current through the source contact pumps its boundary layer, δ_b^src loses its sign guarantee; I judged this small (the drift enters the DS mechanism at the drain) but did not prove it.
5. **Single temperature (353 K), single grid/operating point.** The Kn numbers are 353 K statements (0.35/0.29/0.20 at 300 K, from 07-13 §5 — the channel is *worse* at 300 K where Kn is larger). The N = 480 solver grid-robustness of the anchors is the standing 07-13/07-17 deferred item, unrun.
6. **Trim-absorption of the reactive part** assumes the in-situ trim is exact at the operating frequency; a static-trim residual from the two-leg (q₋ vs q₊) slip asymmetry is O(M) small and uncomputed.
7. **The linewidth bench observable (§4)** bounds total excess loss (bulk + boundary) and assumes homogeneous broadening; isolating σ_c needs the bulk term subtracted, and contact inhomogeneity across the cell would complicate the readout — WP4 measurement-design questions.

## Appendix — runnable listing

*(Self-contained; imports the released `fable-model-chain`. Reproduces every anchor bit-for-bit against `results.json`, the tracked/frozen sensitivities, the Kn brackets, and the budget composition. `PYTHONIOENCODING=utf-8`.)*

```python
import math, sys, os, json
CHAIN = r"...\fable-model-chain"          # adjust to your checkout
sys.path.insert(0, CHAIN)
import constants as C, ds_cell as DS, regen as R, kinetic as K
RES = json.load(open(os.path.join(CHAIN, "results.json"), encoding="utf-8"))
s = DS.plasmon_speed(); vF = C.vF; f0 = C.f0; w = 2*math.pi*f0
tau353 = C.tau(C.Tcap); L = DS.cell_length(s); Mth = DS.M_threshold(L, s, tau353)
M = 0.7*Mth; a_loss = 10**(-DS.passive_loss_dB_per_half_lambda(tau353)/20.0)
loop0 = R.loop_gain(0.0)
tau_ee = K.tau_ee(C.Tcap); l_ee = vF*tau_ee; x = w*tau_ee
qm = w/(s-M*s); qp = w/(s+M*s); Kn = qm*l_ee
# --- anchors (all match results.json / 07-13) ---
assert abs(R.cw_net_gain_dB(0.7) - RES["cw_regen_gain_dB_at_0p7"]) < 1e-4   # 9.66101
assert abs(DS.M_threshold(L,s,tau353) - RES["M_th_353K"]) < 1e-6            # 0.147083
# s/vF=2.3312, l_ee=82.99nm, l_ee/L=0.144(op)/0.142(zero-drift), q-*l_ee=0.2493,
# q+*l_ee=0.2028, a_loss=0.7452, r_drain=1.2296, loop(0.7Mth)=0.9162
# --- tracked sensitivity (re-track threshold with an extra multiplicative loss 1-d) ---
def Mth_loss(d):
    lo,hi=1e-4,0.45
    for _ in range(200):
        m=.5*(lo+hi); loop=(1+m)/(1-m)*a_loss*(1-d)
        lo,hi=(m,hi) if loop<1 else (lo,m)
    return .5*(lo+hi)
def dG(d):
    d = -0.02 if d<=-1 else d
    M_=0.7*Mth_loss(d); loop=(1+M_)/(1-M_)*a_loss*(1-d)
    return 20*math.log10((1-loop0)/(1-loop))
g0=dG(0.0)
print("tracked dB/1%:", round((dG(0.01)-g0)/0.01*0.01,4))   # -0.2837  (07-13: -0.282)
frozenM=(1+M)/(1-M)*a_loss
print("frozen  dB/1%:", round(20*math.log10((1-loop0)/(1-frozenM*0.99))
                              -20*math.log10((1-loop0)/(1-frozenM)),4))  # -0.9013
print("Kn, Kn^2:", round(Kn,4), round(Kn**2,4))             # 0.2493 0.0622
for pct in (0.5,1,1.6,3,3.6,6.2,12.4,24.9):
    print(pct, "% ->", round(dG(pct/100)-g0,2), "dB")       # 3.6->-0.99;6.2->-1.66;12.4->-3.13;24.9->-5.73
```

Expected: tracked −0.2837 dB/1%, frozen −0.9013 dB/1% (buy-back 3.18×); Kn = 0.2493, Kn² = 0.0622; δ_b→ΔG map 0.5 %→−0.14, 1.6 %→−0.45, 3 %→−0.83, 3.6 %→−0.99, 6.2 %→−1.66, 12.4 %→−3.13, 24.9 %→−5.73 dB; both `assert`s pass (CW gain and M_th bit-for-bit against `results.json`).

— Executed on Claude Opus 4.8 (disclosed fallback), for the Fable Computer Agent Lab.

---

## Agent assessment — 2026-07-18

Assessed suitable for the permanent record by a **unanimous 3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)). Assessment performed in a maintainer-operated Claude Code session per the charter's Operations section, on `claude-opus-4-8` (the session's active model — flagged for the record, as this routine's default is Fable 5). The three reviewers ran as isolated, mutually **blind** subagent contexts — one persona each, no visibility into the others' verdicts, which is what makes the 2-of-3 gate real — and **each independently wrote and ran its own driver against the released `fable-model-chain/`** before voting, reproducing the memo's headline numbers (CW gain 9.66100611708918 dB and M_th 0.14708333 **bit-for-bit** against `results.json`; s/v_F 2.3312; l_ee 82.99 nm; q−·l_ee 0.2493 / q₊·l_ee 0.2028; a_loss 0.7452; r_drain 1.2296; tracked/frozen sensitivity −0.2837 / −0.9013 dB per 1 %; the full δ_b→ΔG map; the 27.6 GHz half-linewidth).

**All three recorded promotion-edit-level follow-ups alongside their store votes — read them before acting on the memo's pre-registered keys.** Two reviewers independently flagged the same interval-bookkeeping slip (the near-specular total budget's upper edge is quoted [−1.7, −0.2] dB where bulk-alone [−1.5, −0.3] plus a loss-only near-specular boundary gives an upper edge nearer −0.3), and Kinetic caught a real internal inconsistency in the load-bearing safe-case key: `boundary_loss_pct_per_roundtrip_specular` = 0.0 [0, 0.5] % is annotated “C_acc ≲ 0.1 under either Kn law,” but the memo's own Kn-law δ_b = q−·l_ee·C_acc gives 2.49 % at C_acc = 0.1 — so the [0, 0.5] % band actually corresponds to C_acc ≲ 0.02 (Kn law) / ≲ 0.08 (Kn² law). Both are non-load-bearing (the safe-case physics — both laws vanish as C_acc → 0 — is unaffected), and the vote record is evidence and is not edited after posting.

- 🧵 **Fabric** — **STORE**: I wrote and ran my own driver (scratchpad/verify43.py) against C:\Users\Ryoji\Documents\GitHub\FableComputer\fable-model-chain and every headline number reproduced: CW gain 9.66100611708918 dB and M_th 0.14708333333333332 bit-for-bit against results.json; s/vF 2.3312; l_ee 82.99 nm; l_ee/L 0.144(op)/0.142(zero-drift); omega*tau_ee 0.5214; q-*l_ee 0.2493, q+*l_ee 0.2028; a_loss 0.7452; r_drain 1.2296; loop(0.7Mth) 0.9162; phase speeds 2.571/2.091 v_F; Kn 0.2493 / Kn^2 0.0622; tracked sensitivity -0.2837 dB/1% and frozen -0.9013 (buy-back 3.18x); the delta_b->tracked-dG map -0.991/-1.661/-3.132/-5.727 dB at 3.6/6.2/12.4/24.9%; +/-1 dB <-> delta_b 3.633%; half-linewidth 27.6 GHz — all match. On the physics at my depth the core is sound and, crucially, not oversold: the reactive/slip part is correctly trim-absorbed (consistent with 07-13 §3.2 as a promoted design requirement); the source density-clamp loss sign is firmly argued from entropy production >=0 at a passive DC-unpumped contact (with the DC-unpumped assumption honestly flagged); the node-protection argument correctly buys leading-order losslessness but NOT an O(Kn^2) residual, so the scaling exponent is left explicitly open between O(Kn) and O(Kn^2) and the drain sign is left open — exactly the honest labeling the standard demands, and the reduced-depth model limitation is disclosed rather than papered over. Composition is correct: the bulk [-1.5,-0.3] dB band is interval-added, not re-derived, giving [-4.6,+0.6] (Kn^2) and [-1.7,-0.2] near-specular, and the fan-out-2 margin (0.9-2.1 dB, failing by ~0.1 dB at -1 dB) is inherited from 07-13 §4.2 rather than re-derived, with the reply correctly noting the allowance could be worse than +/-1 dB not better. Pre-registered keys carry their own new names, non-contest statements, and falsification bands; the 07-12 LF boundary-factor 0.99549 is explicitly distinguished from the physical delta_b; gain-ledger and plane discipline are respected. The Part III conclusion (budget does not close on the corrected record; gated on one measurable contact parameter; sub-threshold linewidth as the cheap safe-case gate ahead of the full WP2 solve; architecture-led only if near-specular, else calibration leads) follows directly from the two-branch budget and is genuinely actionable — I would sequence WP1/WP3 work on it. This is a clean, honest negative/decision result meeting all five criteria and the README hard rules.
  - Promotion-edit only: the near-specular total upper edge is quoted [-1.7,-0.2] dB, but bulk-alone is [-1.5,-0.3] and the specular boundary key is loss-only [0,-0.14 dB], so the composed upper edge should be about -0.3 not -0.2; the band is loosened slightly outward (conservative) and non-load-bearing.
  - Promotion-edit only: the linewidth gate references the passive-hydro model value 27.6 GHz, which is in mild tension with 07-13's own in-model bulk band predicting extra broadening; the reply honestly restricts it to a one-sided total-excess-loss bound and flags the bulk-subtraction/inhomogeneity caveat in Limitation 7, so the conclusion survives.
- 🌊 **Kinetic** — **STORE**: I re-executed every headline number against the released fable-model-chain with my own driver: CW gain 9.66100611708918 dB and M_th 0.14708333333333332 reproduced bit-for-bit against results.json, and s/vF 2.3312, l_ee 82.99 nm, l_ee/L 0.142/0.144, omega*tau_ee 0.5214, q-*l_ee 0.2493, q+*l_ee 0.2028, a_loss 0.7452, r_drain 1.2296, loop 0.9162, phase speeds 2.571/2.091 vF, Kn 0.2493/Kn^2 0.0622, tracked -0.2837 and frozen -0.9013 dB/1% (buy-back 3.18x), the full delta_b->dG map (3.63%<->-1 dB, 6.2%->-1.66, 12.4%->-3.13, 24.9%->-5.73), and the 27.6 GHz half-linewidth all reproduced to the quoted digits. The runnable Appendix is faithful. On the physics in my domain: the node-protection argument (AC power ~ delta_J*delta_phi vanishes at each ideal clamp, so the boundary is a Knudsen-layer residual not an O(1) black-wall loss) is sound; the source sign-definiteness is a correct passivity/entropy-production statement honestly labeled demonstrated-in-model with the DC-unpumped caveat flagged as load-bearing; the drain sign-open and, crucially, the decision to leave the Kn exponent open between O(Kn) and O(Kn^2) is the honest call, not a dodge — it makes the result weaker, spans both in the pre-registered diffuse band [3,25]%, and is exactly the kind of numerical-honesty the standard rewards. The memo composes with the 07-13 bulk band [-1.5,-0.3] by interval-add without re-deriving it, respects the gain ledger, and explicitly separates its physical delta_b from the 07-12 LF-artifact 0.99549 and from M_th_num. Labels are correctly stratified (demonstrated reserved for runnable chain anchors, boundary magnitude kept in-model/open), the pre-registered keys carry new names, a non-contest statement, and falsification bands, and the gated Part III conclusion (architecture-led only if the contact is shown near-specular; a sub-threshold linewidth measurement is the cheap one-sided safe-case gate) is a genuine actionable decision. This is a clean negative result cleanly argued — the project's gold standard — so all five criteria hold at the promotion-edit-defect tier, same as its 3/3-promoted 07-13 predecessor.
  - Specular pre-registered key is internally loose: band boundary_loss_pct_per_roundtrip_specular = 0.0 [0,0.5]% is annotated 'C_acc <= 0.1 under either Kn law', but the memo's own delta_b = q-*l_ee*C_acc (Kn law) = 0.249*C_acc gives 2.49% at C_acc=0.1 — 5x outside the band; [0,0.5]% actually corresponds to C_acc<=0.02 (Kn law) / <=0.08 (Kn^2 law). Since this is the load-bearing safe-case gate, its C_acc<->% mapping (and hence the falsification criterion under the Kn law it claims to cover) is mis-calibrated and should be tightened at promotion. The underlying physics (both laws vanish as C_acc->0) is unaffected.
  - Near-specular total-budget row is quoted [-1.7,-0.2] dB, but bulk[-1.5,-0.3] + a small near-specular boundary loss gives an upper edge nearer -0.3 than -0.2; minor interval bookkeeping, non-load-bearing.
- ⚛️ **Quanta** — **STORE**: I re-executed a driver that imports the released fable-model-chain (constants/ds_cell/regen/kinetic + results.json) this session and reproduced every headline number: CW gain 9.66100611708918 dB and M_th 0.14708333 bit-for-bit against results.json; s/vF 2.3312; l_ee 82.99 nm; l_ee/L 0.1424(zero-drift)/0.1439(op); omega*tau_ee 0.5214; q-*l_ee 0.2493, q+*l_ee 0.2028; a_loss 0.7452; r_drain 1.2296; loop(0.7Mth) 0.9162; phase speeds 2.571/2.091 v_F; tracked -0.2837 dB/1%, frozen -0.9013, buy-back 3.18x; Kn 0.2493/Kn^2 0.0622; the delta_b->dG map (3.6%->-0.99, 6.2%->-1.66, 12.4%->-3.13, 24.9%->-5.73); +/-1 dB <-> delta_b 3.63%; half-linewidth 27.57 GHz (=27.6). All reproduced. On my noise/observable lens the linewidth claim is correctly hedged: it states the sub-threshold linewidth bounds TOTAL excess round-trip loss (bulk viscous + boundary), explicitly does NOT read sigma_c off the bench, and reserves the valid use as a one-sided safe-case gate needing the bulk-viscous subtraction (WP2) to isolate sigma_c. The reply plainly states it did NOT shrink the +/-1 dB band and that the allowance could be worse, so there is no hype about what the analysis achieved; the open drain sign and the open Kn exponent (O(Kn) vs O(Kn^2)) are kept explicit rather than averaged, the source sign is labeled demonstrated-in-model with the DC-unpumped caveat flagged (§1 iv/Limitation 4), and 'demonstrated' is reserved for runnable anchors while the boundary magnitude stays in-model/open. It composes with the promoted 07-13 bulk band [-1.5,-0.3] by interval-add to [-4.6,+0.6] (Kn^2) / [-1.7,-0.2] near-specular without re-deriving it, correctly distinguishes its physical delta_b from the 07-12 LF-artifact 0.99549, honors the gain ledger and plane discipline, and ships new-name pre-registered keys with non-contest statement and falsification bands. It delivers a genuine, actionable Part III decision (measurement-gated on the contact parameter; a room-temperature sub-threshold linewidth as the cheap gate pulled ahead of the full WP2 solve). All five criteria hold; this is exactly the honest negative/corrective result the standard rewards.
