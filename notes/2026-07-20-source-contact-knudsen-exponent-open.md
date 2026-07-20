# Does the AC density-clamp node protect the source boundary dissipation to O(Kn²)? The exponent *p*, honestly

**Status:** promoted to `notes/` — accepted by a **3-of-3 agent vote** (recorded below); a human merges per [GOVERNANCE.md](../GOVERNANCE.md). **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #47](https://github.com/ryoji-info/FableComputer/discussions/47) (Kinetic's 🌊 winning prompt, 2-of-3 vote — Fabric → Kinetic, Quanta → Kinetic, Kinetic → Fabric). The commissioned question: derive the leading Knudsen exponent *p* of the source-contact boundary dissipation — does the AC-density-node structure protect it to O(Kn²) [p=2] or leave it O(Kn) [p=1]? — the "single most consequential open point" the fallback derivation of [`notes/2026-07-18-boundary-channel-contact-gated.md`](2026-07-18-boundary-channel-contact-gated.md) §7 Limitation 2 left open. The reply is published at the discussion verbatim and reproduced here for assessment.
**Method:** analysis from the session materials, with every operating-point anchor and sensitivity re-executed against the released `fable-model-chain/` (Python 3 + numpy, `PYTHONIOENCODING=utf-8`, Windows/CPython); the runnable listing in §5 reproduces every number quoted (CW gain and M_th bit-for-bit against `results.json`). Nothing below contests any `results.json` value. *Adversarially pre-checked before posting by three independent in-session contexts* — one re-executed every anchor, one the reflection-scaling, one a physics refutation that **caught and reversed an earlier over-resolved "leaning p=2" draft to the open verdict below**. The three assessment reviewers each independently re-executed everything before voting.
**Author:** Claude **Opus 4.8** — *disclosed; not Fable 5.* This routine's default is Fable 5; that model was not active, and per the pipeline's disclosure rule the winning prompt executed on `claude-opus-4-8`. Nothing here is labeled or represented as Fable 5 output; the candidate drafts and the 2-of-3 vote were produced earlier in the same session, also on Opus 4.8. Maintainer-operated Claude Code session per [agents/README.md](../agents/README.md), 2026-07-20.
**Labels:** demonstrated / in-model / open, per [notes/README.md](README.md).
**Binding record honored:** [`notes/2026-07-18-boundary-channel-contact-gated.md`](2026-07-18-boundary-channel-contact-gated.md) (the δ_b non-closure, source-sign δ_b^src ≥ 0, drain-sign-open, and the **open** Kn exponent this note *structures*, not reopens); [`notes/2026-07-18-boundary-channel-bench-discriminants.md`](2026-07-18-boundary-channel-bench-discriminants.md) (T-shape signature #2, `boundary_T_exponent_2p` ∈ {−2, −4}, that this note's *p* maps onto); [`notes/2026-07-13-kinetic-correction-signed-band.md`](2026-07-13-kinetic-correction-signed-band.md) (bulk band, −0.284 dB/1% tracked sensitivity); [`notes/2026-07-12-boundary-factor-exact-operator.md`](2026-07-12-boundary-factor-exact-operator.md) (the 0.99549 Lax–Friedrichs artifact kept distinct from the physical δ_b); plane discipline ([2026-07-17 notes](2026-07-17-drive-sweep-knee-anchored.md)).

---

> **⚠️ Executing-model disclosure.** This reply was produced in a maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md) (Operations), and executed on **`claude-opus-4-8` (Opus 4.8), NOT Claude Fable 5.** The candidate prompts and the 2-of-3 vote that selected this question were produced earlier in the same session, also on Opus 4.8 (three isolated, mutually blind subagent contexts, one persona each — no self-votes; recorded in the discussion body). Nothing below is labeled or represented as Fable 5 output. The reduced depth of the executing model is a real limitation on a derivation the winning prompt frames as "the ternary/half-range boundary algebra the fallback could not close" — so this reply does **not** claim to close it. It delivers what the corrected record and the prompt both say is a full success: **a well-supported "still open, and here is exactly the one physical ingredient that decides it."** Every number is re-executed against the released `fable-model-chain/`; the runnable listing in §5 reproduces all of them (`PYTHONIOENCODING=utf-8`, Windows/CPython). This reply was additionally adversarially checked before posting by three independent in-session contexts (numeric re-derivation; the reflection-scaling; a physics refutation) — the refutation caught and reversed an earlier over-resolved "leaning p=2" draft, which is why the verdict below is *open*, not a lean.

---

Reply to the winning prompt of **Fable Session — 2026-07-20** (Kinetic 🌊, 2-of-3). Labels are law: **demonstrated** (cite the run), **in-model** (name the model + assumptions), **open**. The prompt asked me to settle *p* if I could and warned against manufacturing a clean answer; I find I **cannot** settle it by analytic kinetics at this depth, and I explain precisely why and what would.

## 1. Verdict

**The exponent is OPEN between p = 1 (O(Kn)) and p = 2 (O(Kn²)) — the memo's two-valued state stands — but it is no longer open in an unstructured way: analytic kinetics reduces it to a *single, physical, bench-measurable* dichotomy, and the natural reading of a diffuse ohmic contact points to the pessimistic p = 1.** In one paragraph:

The source dissipation per reflection has the exact form **1−|r|² = 4q·|ζ″|** (demonstrated algebra, §2.4 / §5C), where ζ″ is the imaginary (dissipative) part of the complex boundary slip length. Since q·l_ee = Kn, this makes **p = 1 + (the Kn-power of ζ″/l_ee)** — so the entire open exponent collapses to one question: *what is the Kn-power of the dissipative slip ζ″?* That power is fixed by **what the density-clamp accommodation actually dissipates**:

- If the contact dissipates only the **O(Kn) Knudsen-layer distortion** of the distribution (a *reversible-reservoir* / near-specular contact that absorbs and re-supplies the O(1) AC antinode current reversibly, as an ideal voltage source would), then ζ″ ~ l_ee·Kn and **p = 2** (node-protected) — but this is the near-specular limit where δ_b^src → 0 anyway.
- If the contact dissipates the **O(1) AC antinode current** itself — which a **fully-diffuse ohmic contact does**: my own §2.3 Maxwell closure re-emits the incoming half of the distribution at the drift-free reservoir equilibrium f_wall, *irreversibly stripping the O(1) AC momentum at the current antinode* — then ζ″ ~ l_ee and **p = 1**.

The density node protects the **density** (which sits at a node); it does **not** protect the **current** (which sits at an antinode, O(1)). So a contact with any real diffuse fraction C_acc > 0 carries the unprotected p = 1 channel. This is exactly the "phase-lag argument stated heuristically but not derived" that [`notes/2026-07-18-boundary-channel-contact-gated.md`](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-07-18-boundary-channel-contact-gated.md) §2 named "the single most consequential open point," and I confirm it does **not** close analytically — asserting p = 2 for "the design-intent ohmic contact" (as an earlier draft of this reply did) over-resolves it, because an ohmic contact holding density by charge exchange with a lead is the fully-*accommodating* boundary, not a lossless mirror. **Consequence for the budget and Part III:** because the honest state is open and the diffuse reading leans p = 1 (δ_b^src ~ Kn ≈ 25% ⟹ tracked ΔG ≈ −5.7 dB), the per-cell gain budget does **not** close on analytic grounds — it stays gated on the contact, which **supports Kinetic's 🌊 calibration-first sequencing**, not an architecture-led lead. **What this call adds beyond the memo:** (i) the exact reflection-dissipation structure p = 1 + power(ζ″); (ii) the reduction of the open exponent to one nameable ingredient — *does the density-clamp accommodation dissipate the O(1) antinode current (irreversible/diffuse → p=1) or only the O(Kn) distortion (reversible/specular → p=2)?*; and (iii) the explicit mapping of that ingredient onto the already-pre-registered bench T-shape signature (`boundary_T_exponent_2p` = −2p ∈ {−2, −4}), so the measurement now reads a specific contact property rather than an abstract number.

## 2. The boundary-layer derivation

**2.1 Geometry and field structure at the node (demonstrated).** 1-D DS cavity x ∈ [0, L], tracked bias M = 0.7·M_th(353 K) = **0.103** (demonstrated). Source at x=0: density clamp δn(0)=0; in the strongly-gated local-capacitance limit q₀d = 0.027 (07-18) this is also δφ(0)=0 — an **AC-potential/pressure node**. The acoustic-plasmon mode near the node is δn(x) ∝ sin(q x) (node at 0); continuity (−iω δn + n₀ ∂ₓδv = 0) puts the **current at an antinode**: δv(x) ∝ cos(q x), δv(0) = δv_max (O(1)), ∂ₓδv(0) → 0. Boundary Knudsen number **Kn ≡ q₋·l_ee = 0.2493**, l_ee = 82.99 nm, l_ee/L = 0.142 (all demonstrated, §5A). Because l_ee/L ≈ 0.14 the Kn-expansion is asymptotic with an **explicit O(Kn) ≈ 20–25% error bar**.

**2.2 Collision model (in-model).** Two-relaxation-time Callaway operator (the prompt's, and Kinetic's 🌊 07-20, choice): a momentum-conserving e–e rate 1/τ_ee producing the bulk viscosity (ν = v_F²τ_ee/4; viscous_fraction = **0.2087**, demonstrated §5D) and a separate boundary/disorder rate carrying accommodation. Bulk limit reduces to the 07-13 Mermin/shallow-water viscoelastic closure as ωτ_ee → 0 (§5D). A single-τ BGK is inadmissible — it cannot represent specular↔diffuse accommodation (Kinetic 🌊, 07-20) — so it cannot even pose this question.

**2.3 The half-range accommodation condition (in-model).** At x=0 the incoming half (v_x > 0) is set by Maxwell accommodation on the outgoing half:
f_in(0, v) = (1−C_acc)·f_specular(0, v) + C_acc·f_wall, with f_wall the reservoir's drift-free local equilibrium at the clamped density; C_acc ∈ [0,1] specular→diffuse. The node constraint δn(0)=0 fixes the density moment of the full distribution to zero. **Note the tension this exposes:** the fully-diffuse limit C_acc→1 is the *ohmic-reservoir* contact (re-emit at f_wall) — and re-emitting the drift-carrying incoming current at drift-free f_wall is precisely an **irreversible O(1) momentum strip**, not a lossless reflection.

**2.4 Order-by-order, and the fate of the O(Kn) coefficient (the crux).** Reflection off a boundary with complex slip length ζ = ζ′ + iζ″ gives, for the density-node field (Robin condition φ(0)=ζ φ′(0)), the exact coefficient r = (ikζ−1)/(1+ikζ) (passive branch, |r| ≤ 1 for ζ″ < 0), hence **1−|r|² = −4kζ″/|1+ikζ|² ≈ 4q|ζ″|** (demonstrated algebra, §5C). Two facts, and one genuinely undetermined choice:

- **(i) The real slip ζ′ is non-dissipative.** ζ′ ~ l_ee is a reversible plane displacement — *trim-absorbed* (07-18 §2B). All dissipation is in ζ″. (in-model)
- **(ii) The exponent equals 1 + the Kn-power of ζ″.** Illustrated as a scaling in §5C: **assuming** ζ″ ~ l_ee·Kn gives log-log slope → 2; **assuming** ζ″ ~ l_ee gives slope → 1. This is an algebraic tautology (the slope is a restatement of the assumed power) — it is **in-model**, not a proof of the power. (in-model)
- **(iii) The Kn-power of ζ″ is the open question, and it is set by which quantity the accommodation dissipates.** *Reversible-reservoir / near-specular:* only the O(Kn) Knudsen-layer distortion is dissipated; entropy is quadratic in that O(Kn) distortion ⟹ ζ″ ~ l_ee·Kn ⟹ **p = 2**. *Diffuse ohmic (C_acc > 0):* the O(1) AC antinode current is irreversibly thermalized (drift stripped at f_wall) ⟹ ζ″ ~ l_ee·C_acc ⟹ **p = 1**. **No symmetry forces the O(Kn) coefficient to vanish for a diffuse contact** — the node protects the density (node), while the dissipated quantity is the current (antinode). The idealized density clamp of Part I Eq. (2), read as a *perfect reversible voltage source*, is p = 2; read as a *fully-accommodating ohmic reservoir* (its C_acc→1 limit), it is p = 1. A real contact is somewhere between, and **which limit dominates is the open ingredient X** — reversible-reservoir vs irreversible-diffuse dissipation of the antinode current. (open)

## 3. Consistency checks (all demonstrated, §5)

- **Bulk limit → 07-13 closure**: viscous_fraction(300 K) = **0.2087** and the ωτ_ee=1 hydro-expiry = **254.9 K** reproduce results.json exactly (§5D).
- **Tracked sensitivity**: ∂G/∂δ_b = **−0.2837 dB per 1%** (§5B), reproducing 07-18/07-13's −0.284/−0.282.
- **Both exponent branches vs the note's [3, 25]% diffuse band**: p = 2 lands the diffuse-edge source term at δ_b^src ≈ Kn² ≈ **6.2% (ΔG −1.67 dB)** — lower edge of the note's `boundary_loss_pct_per_roundtrip_diffuse` = 6.2 [3, 25]%; p = 1 lands it at Kn ≈ **24.9% (ΔG −5.73 dB)** — upper edge. My verdict does **not** pick between these; it reproduces both edges (§5B) and states the diffuse-contact reading favours the upper (pessimistic) one.
- **Kn ↔ ωτ_ee tie** (why "O(Kn²)" ≡ "O(Kn·ωτ_ee)"): Kn/ωτ_ee(353 K) = **0.4782 = (v_F/s)/(1−M)**, with ωτ_ee(353 K) = **0.5214** (demonstrated §5A — note this is the 353 K operating value, not the 300 K results.json ωτ_ee = 0.7219).

## 4. Pre-registered key, non-contest statement, falsification

- **New keys** (own names; collide with nothing — results.json carries no `boundary_*`/exponent/drain/source key, and these differ from all six note keys):
  - `boundary_source_Kn_exponent_p` = **open ∈ {1, 2}** — *not* resolved analytically; p = 1 for a diffuse ohmic contact that dissipates the O(1) antinode current, p = 2 only for a reversible-reservoir / near-specular contact.
  - `boundary_source_exponent_controlling_ingredient` = *"reversible-reservoir (p=2) vs irreversible-diffuse dissipation of the O(1) AC antinode current (p=1)."*
  - Relation to the already-claimed bench key (a *labeled prediction*, not a redefinition): **boundary_T_exponent_2p = −2p**, so p=1 ⟹ −2 and p=2 ⟹ −4.
- **Does NOT contest**: any `fable-model-chain/` or `fable-model-quantum/` results.json value; the gain ledger, M_th, `boundary_sensitivity_dB_per_pct_tracked` = −0.284, the source-sign (δ_b^src ≥ 0) and drain-sign-open findings of 07-18, and the 07-12 LF 0.99549 artifact (a distinct object). I settle none of those; I structure *p*.
- **Falsification / resolution (two-sided)** via bench T-shape signature #2, splitting the note's [−4.5, −1.5] band at −3.0: **reservoir-verified contact + slope in [−4.5, −3.0] ⟹ p=2 (node protection real); reservoir-verified contact + slope in [−3.0, −1.5] ⟹ p=2 refuted; diffuse/rough contact + slope in [−3.0, −1.5] ⟹ p=1 as the diffuse reading predicts.** A WP2 σ_c-swept half-range moment solve returning a leading source exponent is the analytic resolution.

## 5. Runnable listing

Self-contained apart from importing the released `fable-model-chain`. §5C is an in-model *illustration* of the structure p = 1 + power(ζ″); it does not prove the power.

```python
# -*- coding: utf-8 -*-
# Source-contact Knudsen exponent p — Fable Session 2026-07-20 (Opus 4.8, disclosed).
# (A) Kn anchor from the released chain; (B) tracked sensitivity + delta_b->gain map
# incl. the p=1/p=2 diffuse edges; (C) soft-boundary reflection dissipation
# 1-|r|^2=4q|zeta''| ILLUSTRATING p = 1 + (Kn-power of zeta'') -- the power is NOT
# proven here; (D) bulk-limit self-consistency. PYTHONIOENCODING=utf-8, numpy only.
import math, os, sys, json
import numpy as np
CHAIN = r"...\fable-model-chain"                       # adjust to your checkout
sys.path.insert(0, CHAIN)
import constants as C, ds_cell as DS, kinetic as K, regen as R
RES = json.load(open(os.path.join(CHAIN, "results.json"), encoding="utf-8"))

# (A) anchors (demonstrated)
s = DS.plasmon_speed(); vF = C.vF; f0 = C.f0; w = 2*math.pi*f0
tau353 = C.tau(C.Tcap); L0 = DS.cell_length(s)
Mth = DS.M_threshold(L0, s, tau353); M = 0.7*Mth
tau_ee = K.tau_ee(C.Tcap); l_ee = vF*tau_ee
qm = w/(s-M*s); qp = w/(s+M*s); Kn = qm*l_ee
print("s/vF=%.4f  M_th=%.6f  Kn=q-*l_ee=%.4f  q+*l_ee=%.4f  l_ee/L=%.4f"
      % (s/vF, Mth, Kn, qp*l_ee, l_ee/L0))
print("CW gain 0.7 = %.6f (json %.6f)" % (R.cw_net_gain_dB(0.7), RES["cw_regen_gain_dB_at_0p7"]))
print("omega*tau_ee(353K)=%.4f ; Kn/wtau=%.4f=(vF/s)/(1-M)=%.4f"
      % (w*tau_ee, Kn/(w*tau_ee), (vF/s)/(1-M)))

# (B) tracked sensitivity + delta_b -> tracked gain (demonstrated)
a = 10**(-DS.passive_loss_dB_per_half_lambda(tau353)/20.0); loop0 = R.loop_gain(0.0)
def Mth_loss(d):
    lo,hi=1e-4,0.45
    for _ in range(200):
        m=.5*(lo+hi); lp=(1+m)/(1-m)*a*(1-d); lo,hi=(m,hi) if lp<1 else (lo,m)
    return .5*(lo+hi)
def dG(d):
    M_=0.7*Mth_loss(d); lp=(1+M_)/(1-M_)*a*(1-d); return 20*math.log10((1-loop0)/(1-lp))
g0=dG(0.0)
print("tracked dB/1%% = %.4f" % ((dG(0.01)-g0)))
print("p=2 edge Kn^2=%.1f%% -> %+.2f dB ; p=1 edge Kn=%.1f%% -> %+.2f dB"
      % (Kn**2*100, dG(Kn**2)-g0, Kn*100, dG(Kn)-g0))

# (C) soft-boundary reflection dissipation ILLUSTRATION (in-model; power NOT proven)
def one_minus_r2(k, zeta):
    r=(1j*k*zeta-1)/(1+1j*k*zeta); return 1-abs(r)**2
Kns=np.array([0.05,0.10,0.15,0.20,0.2493,0.30])
aP2=np.array([one_minus_r2(kn/l_ee, 1j*(-l_ee*kn)) for kn in Kns])  # ASSUME zeta''~l_ee*Kn
aP1=np.array([one_minus_r2(kn/l_ee, 1j*(-l_ee))    for kn in Kns])  # ASSUME zeta''~l_ee
s2=np.gradient(np.log(aP2),np.log(Kns)); s1=np.gradient(np.log(aP1),np.log(Kns))
for i,kn in enumerate(Kns):
    print("Kn=%.4f  assume zeta''~l_ee*Kn:1-|r|^2=%.5f slope=%.2f | assume zeta''~l_ee:%.5f slope=%.2f"
          % (kn,aP2[i],s2[i],aP1[i],s1[i]))
print("=> slope = 1 + assumed Kn-power of zeta''. Which power the real diffuse-vs-")
print("   reversible contact realises is OPEN (the memo's {O(Kn),O(Kn^2)}).")

# (D) bulk limit (demonstrated)
print("viscous_fraction(300K)=%.4f (json %.4f) ; hydro expiry=%.1f K (json %.1f)"
      % (K.viscous_fraction(C.T300), RES["viscous_fraction"],
         K.validity_temperature(), RES["hydro_expiry_K"]))
```

**Printed output (reproduced this session):**

```
s/vF=2.3312  M_th=0.147083  Kn=q-*l_ee=0.2493  q+*l_ee=0.2028  l_ee/L=0.1424
CW gain 0.7 = 9.661006 (json 9.661006)
omega*tau_ee(353K)=0.5214 ; Kn/wtau=0.4782=(vF/s)/(1-M)=0.4782
tracked dB/1% = -0.2837
p=2 edge Kn^2=6.2% -> -1.67 dB ; p=1 edge Kn=24.9% -> -5.73 dB
Kn=0.0500  assume zeta''~l_ee*Kn:1-|r|^2=0.00995 slope=1.98 | assume zeta''~l_ee:0.18141 slope=0.87
Kn=0.1000  assume zeta''~l_ee*Kn:1-|r|^2=0.03921 slope=1.95 | assume zeta''~l_ee:0.33058 slope=0.81
Kn=0.1500  assume zeta''~l_ee*Kn:1-|r|^2=0.08608 slope=1.91 | assume zeta''~l_ee:0.45369 slope=0.74
Kn=0.2000  assume zeta''~l_ee*Kn:1-|r|^2=0.14793 slope=1.84 | assume zeta''~l_ee:0.55556 slope=0.66
Kn=0.2493  assume zeta''~l_ee*Kn:1-|r|^2=0.22036 slope=1.76 | assume zeta''~l_ee:0.63892 slope=0.60
Kn=0.3000  assume zeta''~l_ee*Kn:1-|r|^2=0.30300 slope=1.72 | assume zeta''~l_ee:0.71006 slope=0.57
=> slope = 1 + assumed Kn-power of zeta''. ... OPEN.
viscous_fraction(300K)=0.2087 (json 0.2087) ; hydro expiry=254.9 K (json 254.9)
```

## 6. Limitations — what I did not close, and what would

1. **Executing model.** Opus 4.8, not Fable 5 (header). I did **not** carry a Case–van Kampen / half-range Gross–Ziering solve to a closed O(1) dissipation coefficient, and — the honest headline — I could **not** settle the exponent *p*: the reversible-vs-diffuse character of the density-clamp's antinode-current dissipation is exactly the coefficient that decides it, and it is contact microphysics, not pure kinetics. The value delivered is the *structure* (p = 1 + power(ζ″)), the *reduction* to one nameable ingredient, and the *mapping* to the bench signature.
2. **The node idealization is only approximate at finite q₀d = 0.027.** δφ(0)=0 follows from δn(0)=0 only in the exact local-capacitance limit; a finite q₀d admits a small δφ residual seeding an O(Kn) term with coefficient ∝ q₀d — a second, weaker route to p = 1 contamination even for an otherwise reversible contact.
3. **ωτ_ee(353 K) = 0.5214 is not asymptotically small.** The out-of-phase (dissipative) parameter is O(ωτ_ee) ~ O(Kn) at the operating point; neither is small, so even the *reversible-reservoir* p=2 prefactor is not tiny (hence a ~6% diffuse edge, not <1%), and every exponent statement carries the 20–25% Kn-expansion bar. (Operating value 0.5214 at 353 K; the 300 K value 0.7219 in results.json is a different plane — plane discipline, 07-17.)
4. **Ingredient X is a genuine device-level open.** Whether a fabricated ohmic contact dissipates its antinode current reversibly (reservoir) or irreversibly (diffuse) is a materials/fabrication fact I cannot derive; the bench T-shape signature #2 (slope −4 vs −2) is what reads it. The gain is that the exponent measurement now reads a specific, nameable contact property.
5. **Drain untouched, source-sign untouched.** Per scope: drain remains sign-open (07-18); δ_b^src ≥ 0 stands; I structured only *p* for the source, and did not close it.
6. **Everything rides on the unproven gain cell** (bench gate G1). If the sub-threshold regenerative resonance does not exist, the boundary question is moot.

*(Inherited seam, non-load-bearing: the near-specular total budget is quoted [−1.7, −0.2] dB after the 07-18 memo; two of that note's reviewers already flagged the upper edge should be ≈ −0.3 dB — bulk-alone [−1.5, −0.3] plus a loss-only near-specular boundary. It does not affect this reply's open verdict.)*

---

**Concrete next step (adoptable):** run Kinetic's 🌊 07-20 WP2 first-equation — the Callaway two-rate operator — as a **σ_c-swept half-range moment solve at Kn = 0.249**, and report the *leading source exponent* directly; that is the analytic resolution this call could not reach. In parallel, the bench T-shape signature #2 resolves it empirically: `boundary_T_exponent_2p` in [−4.5, −3.0] confirms p = 2, in [−3.0, −1.5] confirms p = 1. Until one of those lands, the honest state is: **the boundary term is not closed, the diffuse-contact reading leans pessimistic (p = 1, ΔG ≈ −5.7 dB at the diffuse edge), and the per-cell gain budget stays gated on the contact — Kinetic's 🌊 calibration-first sequencing is the supported path, and Fabric's 🧵 architecture-led Part III may lead only if a bench check first shows the contact near-specular.**

— Executed on Claude **Opus 4.8** (disclosed; not Fable 5), for the Fable Computer Agent Lab. Maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md).

---

## Agent assessment — 2026-07-20

Assessed suitable for the permanent record by a **3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)). Assessment performed in a maintainer-operated Claude Code session per the charter's Operations section, on **`claude-opus-4-8`** (the session's active model — flagged for the record, as this routine's default is Fable 5; the entire 2026-07-20 source-exponent thread — the candidate drafts, the 2-of-3 vote, the execution, and this assessment — ran end-to-end on Opus 4.8). The three reviewers ran as isolated, mutually **blind** subagent contexts — one persona each, no visibility into the others' verdicts, which is what makes the 2-of-3 gate real — and **each independently wrote and ran its own driver** against the released `fable-model-chain/` before voting; all three confirmed the anchors reproduce bit-for-bit against `results.json` (CW gain 9.66100611708918 dB; M_th 0.14708333); s/vF 2.3312; Kn = q₋·l_ee 0.2493; q₊·l_ee 0.2028; l_ee 82.99 nm; tracked sensitivity −0.2837 dB/1%; the δ_b→ΔG map with the p=2 edge 6.2 % → −1.67 dB and the p=1 edge 24.9 % → −5.73 dB; viscous_fraction 0.2087; hydro-expiry 254.9 K; and the §5C reflection-dissipation slopes → 2 (ζ″~l_ee·Kn) / → 1 (ζ″~l_ee). Nothing in the note contests any `results.json` value.

- 🧵 **Fabric** — **STORE**: I re-executed every anchor with my own driver against the released fable-model-chain: s/vF=2.3312, M_th(353K)=0.147083, Kn=0.2493, q+·l_ee=0.2028, l_ee=82.99 nm, l_ee/L=0.142, CW gain(0.7)=9.66100611708918 bit-for-bit against results.json, tracked −0.2837 dB/1%, the p=2/p=1 edges −1.67/−5.73 dB, ωτ_ee(353K)=0.5214 (correctly distinguished from the 300K json 0.7219), Kn/ωτ_ee=0.4782=(vF/s)/(1−M), viscous_fraction(300)=0.2087, hydro expiry 254.9 K, and the §5C reflection tautology (slope→2 for ζ″~l_ee·Kn, →1 for ζ″~l_ee) all reproduced — numbers_reproduced is true. Against the corrected record the reply is clean: it contests no results.json value, explicitly keeps the 07-12 LF 0.99549 artifact a distinct object, observes 07-17 plane discipline on the 353K vs 300K ωτ_ee, and does not reopen the 07-18 source-sign (δ_b^src≥0) or drain-sign-open findings; the two new keys collide with none of the six existing note keys, and boundary_T_exponent_2p=−2p is honestly cited as a relation to the bench-discriminants note's already-claimed key, not a redefinition. The open verdict is the HONEST state, not a cop-out: the 07-18 memo itself held the exponent two-valued and named it "the single most consequential open point," and the reply's header documents that an in-session physics refutation caught and reversed an over-resolved "leaning p=2" draft — the reduction to a single nameable dichotomy (reversible-reservoir p=2 vs irreversible-diffuse dissipation of the O(1) antinode current p=1, with the density node protecting the density-node but not the current-antinode) is a genuine in-model advance, labeled open throughout with the §5C illustration explicitly flagged as tautological rather than a proof of the power. All five criteria hold; the one seam is disclosed and non-load-bearing, exactly the promotion-edit tier at which the two predecessors were stored 3/3.
  - Promotion-edit (non-load-bearing, inherited + self-disclosed): the §6 footnote carries the 07-18 near-specular total budget as [-1.7,-0.2] dB, whose upper edge two prior reviewers flagged should be ~-0.3 (bulk-alone [-1.5,-0.3] plus a loss-only boundary). The reply flags it as an inherited seam that does not affect its open verdict; should be reconciled at promotion.
  - Substance-thinness (non-load-bearing, promotion-note): a large part of the 'structure' — 1-|r|^2 ≈ 4q|zeta''| and the node/antinode observation — already appears in the 07-18 contact-gated memo §2, and boundary_T_exponent_2p = -2p is the bench-discriminants note's pre-existing key. The genuinely new content is the physical lean that a fully-diffuse ohmic contact strips the O(1) antinode current (p=1) and the ingredient-X reduction; the reply is honest that (iii) restates an existing key, so this is a scope observation, not an error.
  - Cosmetic (non-load-bearing): the §5C p=1 illustration prints a finite-Kn local slope of ~0.87 (falling to 0.60 at Kn=0.2493) while the text asserts the limit '-> 1'; I confirmed the slope does approach 1 as Kn->0 (0.98/0.998/0.9998), so the limit statement is correct and the block is explicitly labeled an in-model illustration whose slope merely restates the assumed power.
- 🌊 **Kinetic** — **STORE**: I wrote and ran my own driver against the released fable-model-chain and every quoted number reproduced: s/vF=2.3312, M_th(353)=0.147083, Kn=0.2493, q+·l_ee=0.2028, l_ee=82.99nm, l_ee/L=0.1424, CW gain(0.7)=9.661006 bit-for-bit vs results.json, tracked sensitivity -0.2837 dB/1%, the p=2 edge -1.67 dB and p=1 edge -5.73 dB, ωτ_ee(353)=0.5214 (correctly distinguished from the 300K results.json 0.7219 by plane discipline), Kn/ωτ_ee=0.4782=(vF/s)/(1-M), viscous_fraction(300)=0.2087, hydro expiry 254.9K, and the §5C reflection-dissipation illustration (1-|r|²=4q|ζ''|, asymptotic slope→2 for ζ''~l_ee·Kn, →1 for ζ''~l_ee) all matched my independent run including the imperfect np.gradient endpoint slopes. On the physics this is the honest state, not a cop-out: the memo held p two-valued between O(Kn) and O(Kn²), and this reply keeps it OPEN while adding real content — the exact structure p=1+power(ζ''), the reduction of the whole open exponent to one nameable device dichotomy (reversible-reservoir → p=2 vs irreversible-diffuse dissipation of the O(1) antinode current → p=1), and the mapping onto the already-registered bench key boundary_T_exponent_2p=−2p made two-sided by splitting [−4.5,−1.5] at −3.0. The "leans p=1" is a physically-argued lean (a diffuse ohmic density-clamp is the fully-accommodating boundary; the node protects density not the antinode current) kept explicitly under the OPEN label, and the reply documents an adversarial context reversing an earlier over-resolved "leaning p=2" draft — exactly the numerical honesty the standard rewards. It contests no results.json value, does not reopen the δ_b^src≥0 / drain-sign-open / 07-12 LF-0.99549-distinct-object findings, and its new keys collide with nothing; a well-supported open result of this kind is highly storable.
  - Non-load-bearing (promotion-edit): the §5C printed p=1 slopes (0.57-0.87) visibly undershoot the claimed asymptotic limit '→1' at the sampled finite Kn (the |1+ikζ|² denominator plus np.gradient endpoints bend them below 1); the text honestly labels the whole illustration an 'algebraic tautology ... does not prove the power' and only claims the Kn→0 limit, which I confirm analytically (4Kn/(1+Kn²)→slope 1), so no reader is actually misled and the open verdict does not rest on it.
  - Non-load-bearing, self-flagged and inherited: the reply repeats the 07-18 near-specular total budget as [−1.7,−0.2] dB, which two predecessor reviewers already recorded should be ≈−0.3 dB at the upper edge; the reply explicitly parenthesizes this as a known inherited seam that does not affect its open verdict.
- ⚛️ **Quanta** — **STORE**: I wrote and ran my own driver against the released fable-model-chain and every quoted figure reproduces bit-for-bit — the anchors, the tracked −0.2837 dB/1%, both p-edge maps (−1.67 / −5.73 dB), the 353K ωτ_ee=0.5214 (correctly NOT the 300K results.json 0.7219), and the §5C reflection slopes. The OPEN verdict is the honest state, not a cop-out: the promoted 07-18 memo already held the exponent two-valued (its own generic estimate is O(Kn), with O(Kn²) needing an unproven phase-lag argument), so leaning pessimistic toward p=1 for a diffuse ohmic contact is consistent with the corrected record, and the reply explicitly refuses to settle p while flagging it reversed an earlier over-resolved p=2 draft. The genuine advance is real, not a dodge: it reduces the open exponent to the single algebraic structure p = 1 + power(ζ″), names the one physical ingredient X that decides it (reversible-reservoir vs irreversible-diffuse dissipation of the O(1) antinode current — the density node protects density, not the current antinode), and maps that ingredient onto the already-pre-registered bench signature via boundary_T_exponent_2p = −2p. Labels are law-abiding (demonstrated reserved for runnable anchors; the §5C slope honestly called an in-model tautology; source-sign and drain-sign left untouched per scope), §6 is candid about the executing-model depth limit and the finite-q₀d/finite-ωτ_ee caveats, and it lands squarely as the honest open/negative result criterion 4 rewards. All five criteria hold and someone sequencing the WP2 half-range solve or the Part III gate would consult it.
  - Non-load-bearing, self-flagged (promotion-edit): the reply's own footnote quotes the inherited [-1.7,-0.2] dB near-specular total budget and concedes two 07-18 reviewers flagged the upper edge should be ~-0.3 dB; it does not affect the open p-verdict. Same seam the 07-18 predecessors were stored 3/3 with.
  - Non-load-bearing (labeling/asymptotic framing): §2.4(ii) and §5C say the ζ''~l_ee illustration gives slope '→1', which is the Kn→0 asymptotic limit; at the operating Kn the printed slope is ~0.6-0.87. The reply prints the true finite-Kn values and labels the whole illustration in-model/tautological, so it is honest, not an error.
  - Not a defect, noted for completeness: the p=1 lean rests on the physical argument that a diffuse contact strips the O(1) antinode current — this is precisely the open ingredient X, correctly labeled open rather than resolved; no symmetry-forced-vanishing claim is oversold.
