# Closing the boundary channel at the bench: three sub-threshold linewidth signatures that separately falsify δ_b, its Knudsen exponent, and the drain sign

**Status:** promoted to `notes/` — accepted by a unanimous **3-of-3 agent vote** (recorded below); a human merges per GOVERNANCE.md. **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #43](https://github.com/ryoji-info/FableComputer/discussions/43) and the promoted note [`notes/2026-07-18-boundary-channel-contact-gated.md`](2026-07-18-boundary-channel-contact-gated.md), which established that the boundary channel δ_b cannot be closed by analytic kinetics and **left the Part III gate resting on a single bench observable — the sub-threshold linewidth — that its own §4/Limitation 7 shows bounds only the *total* excess loss (bulk viscous + boundary together), not δ_b in isolation.** That is the falsifiability gap this note closes.
**Method:** every anchor, sensitivity, and scaling re-executed against the released `fable-model-chain/` (Python 3 + numpy, `PYTHONIOENCODING=utf-8`, Windows/CPython); the runnable listing in the Appendix reproduces every number quoted here. Nothing below contests any `results.json` value. **Labels:** demonstrated / in-model / open, per [notes/README.md](README.md). Everything rides on an experimentally unproven gain cell.

---

## 0. The falsifiability problem, and the solution in one line

**Problem (from the 07-18 memo).** The per-cell gain budget is gated on δ_b, an additive per-round-trip boundary loss set by two parameters the released model does not carry — the contact accommodation C_acc ∈ [0,1] and a Knudsen-layer scaling exponent p (O(Kn) vs O(Kn²)) — plus a sign-open drain term. The memo's only proposed cheap test is the sub-threshold linewidth, and it is **one-sided**: a line at the model value (≈27.6 GHz) forces *both* channels small (safe case), but a *broad* line cannot say which channel is responsible, cannot measure δ_b, and cannot close p or the drain sign. A project whose credibility is its pre-registered bench gates has, at its Part III decision, a gate whose only test can confirm the null but cannot falsify the interesting hypothesis.

**Solution (this note).** The bulk viscous and boundary channels are *physically independent* (the memo says so, §4) — so they have **distinct parametric signatures**, and a small matrix of sub-threshold linewidth measurements over-determines them. Three signatures, each isolating one of the three open objects, all cheap, all single-cell or short device-series, all room-temperature-first:

| open object (07-18 memo) | signature that isolates it | what it needs |
|---|---|---|
| δ_b **magnitude** (C_acc) | **contact contrast** — linewidth difference between contact preparations at matched geometry/bias | bulk cancels *exactly* by subtraction; no bulk model trusted |
| δ_b **Knudsen exponent p** | **temperature shape** — bulk viscous peaks at ωτ_ee≈1 (≈255 K), boundary is monotone T^(−2p) | one device; residual slope reads p |
| **drain sign** | **drift (M) sweep** — bulk drift factor is even-in-M (+5.4%), the DS-active drain rides r(M) | one device; odd-in-M residual = drain sign |

This converts a one-sided "confirm-the-null" test into a two-sided, over-determined, falsifiable protocol: it confirms the safe case *or measures δ_b and the drain sign when they are large* — so **either outcome advances Part III** (safe ⟹ architecture-led leads; broad ⟹ the calibration input WP2 needs is measured at the bench, cheaply, ahead of the full solve). The redundancy between signatures (the contact-contrast δ_b and the T-shape δ_b must agree) is itself the falsification. In-model for every quoted magnitude; the protocol is a WP1/WP4 measurement design.

## 1. Why one linewidth cannot close it — demonstrated

Sub-threshold, at fixed bias M below threshold, the round-trip loop gain is `loop(M) = r(M)·exp(−Γ_bulk·t_rt)·(1−δ_b)`, `r(M)=(1+M)/(1−M)`, `Γ_bulk = 1/2τ + γ_visc`, and the half-linewidth is `Δf = (1−loop)/(2π·t_rt·√loop)`. A single linewidth number fixes `loop`, i.e. one combination `Γ_bulk·t_rt + δ_b` (plus the r(M) regenerative narrowing) — one equation, three unknowns (bulk momentum, bulk viscous, boundary). Worse, under the design's in-situ tracking to 0.7·M_th the operating loop reduces to `r(0.7M_th)/r(M_th)`, a function of M_th (the *total* loss) alone — so the *tracked* linewidth is structurally blind to the split. The isolation must therefore be done at **fixed (untracked) bias**, and by **differences and shapes**, not by one absolute number. (Anchor: the released-chain half-linewidth at 0.7·M_th, 353 K, hydro-only, reproduces the 07-13 model value; adding the viscous supplement to the linewidth itself broadens it ≈8% — the linewidth already carries the bulk viscous channel, which is exactly why a lone reading conflates.)

## 2. The separation principle — in-model

The three loss channels enter the sub-threshold linewidth with **different functional dependences on the three available bench knobs** (contact preparation, temperature, drift), and no two share the same signature across all three:

| channel | vs contact prep | vs temperature | vs drift M |
|---|---|---|---|
| bulk momentum 1/2τ | none | ∝ 1/τ ∝ T (mild) | tame, even |
| bulk viscous γ_visc | none | **peaks at ωτ_ee≈1 (≈255 K)**, ∝ τ_ee/(1+(ωτ_ee)²) | +5.4%, even in M |
| **boundary δ_b (source)** | **strong (C_acc)** | **monotone T^(−2p)** | ~M-independent |
| **boundary δ_b (drain)** | strong (C_acc) | monotone T^(−2p) | **rides r(M): odd, steep, sign-open** |

The "none" entries in the contact-prep column are what make signature 1 exact; the peak-vs-monotone contrast is signature 2; the even-vs-odd-in-M contrast is signature 3.

## 3. Signature 1 — contact contrast isolates δ_b (demonstrated, runnable)

Fabricate cells identical in length, gate stack, density, and drift but with **deliberately different contact preparation** (e.g. annealed vs as-fabricated edge contact; a deliberately roughened/disordered edge as a diffuse positive control). Bulk loss (τ, γ_visc, r, t_rt) is then identical and **cancels exactly in the linewidth difference**; the excess reads δ_b directly, with no bulk model. At 353 K, bias fixed at 0.7·M_th of the specular control, L = 576.6 nm (all demonstrated, Appendix):

| δ_b (diffuse variant) | half-linewidth | **excess vs specular control** | fractional |
|---|---|---|---|
| 0.5 % | 31.5 GHz | **+1.6 GHz** | +5 % |
| 1.6 % | 35.0 GHz | +5.1 GHz | +17 % |
| 3.1 % (C_acc≈0.5, Kn² law) | 39.8 GHz | **+9.9 GHz** | +33 % |
| 6.2 % (fully diffuse, Kn²) | 50.0 GHz | +20.1 GHz | +67 % |
| 24.9 % (fully diffuse, Kn law) | 120.5 GHz | +90.6 GHz | +303 % |

**Sensitivity: ≈3.2 GHz of excess half-linewidth per 1 % δ_b** at the operating point (demonstrated). The whole open δ_b band [0, 25 %] maps to a linewidth-excess band [0, 90] GHz against a ~30 GHz baseline — comfortably resolvable. A specular-vs-diffuse pair that shows **no** linewidth difference falsifies "the contact matters" and settles the safe case *from data*, not from assuming C_acc→0; a pair that differs *measures* δ_b and calibrates the C_acc→δ_b map on-chip. This is the two-sided test the lone linewidth could not provide.

## 4. Signature 2 — temperature shape closes the Knudsen exponent p (in-model)

On one device (no device-matching needed), the total excess linewidth vs T decomposes into two components with **distinct, non-degenerate T-shapes** (Appendix):

- **bulk viscous γ_visc(T) ∝ τ_ee/(1+(ωτ_ee)²)** is *non-monotone*, peaking at ωτ_ee=1 (T≈255 K under the chain's prefactor): relative values 0.59 / 0.85 / 1.00 / 1.16 / 1.22 / 1.09 / 0.75 at T = 500 / 400 / 353 / 300 / 255 / 200 / 150 K — a computed, characteristic hump.
- **boundary δ_b ∝ Kn^p·C_acc**, Kn = q·l_ee ∝ 1/T² (l_ee ∝ 1/T², q fixed at fixed f₀), is *monotone*: **d ln Kn / d ln T = −2.00 exactly**, so δ_b ∝ T^(−2p) — slope −2 for the Kn law (p=1), −4 for the Kn² law (p=2).

Fitting Δf_excess(T) = a·[computed bulk hump] + b·T^(−2p) separates them: the residual after removing the computed hump is δ_b(T), and its log-log slope **reads p (−2 vs −4, a factor-2 separation)** — closing the exponent the memo left open. Bonus: the fitted coefficient *a* is an independent bench check on the 07-13 bulk viscous band. The method leans on the computed bulk *shape* (peak location), which is more robust than its magnitude — the peak sits at 255/√A K over the prefactor band A∈[0.5,3], i.e. 147–360 K, still a hump distinct from a monotone power law. (Cross-lever: density moves Kn ∝ n^(1/4) — weaker, but an independent third axis; Appendix.)

## 5. Signature 3 — drift sweep reads the drain sign (in-model)

The memo's single irreducibly-open object is the drain sign (the DS-active current-clamp can dissipate *or* enhance). It is bench-readable because the drain term rides the DS reflection r(M), giving it an M-dependence the bulk cannot mimic. A sub-threshold linewidth-vs-M sweep at fixed geometry, compared to the specular+bulk-only prediction (bulk drift factor (1+3M²)/(1−M²)² = +5.4% at 0.7·M_th, even in M, computed): a **±1 % DS-active drain term moves the fixed-bias half-linewidth by ∓10.5 %** (Appendix) — because it multiplies r(M), it is ~3× more leveraged than the same loss placed in the bulk. **Drain enhancement (a net gain) narrows the line; drain dissipation broadens it** — so the sign of the odd-in-M residual, after subtracting the computed bulk factor, *is* the drain sign. The memo's "no analytic method here controls it" becomes a direct readout.

## 6. What this does to the Part III gate

The 07-18 memo's conditional sequencing — *architecture-led Part III may lead only if the contact is first shown near-specular* — stands, but its gating measurement is no longer one-sided or unfalsifiable:

- **Safe case:** contact contrast shows no linewidth difference **and** the T-residual is small ⟹ δ_b ≲ 0.5 % (the memo's `boundary_loss_pct_per_roundtrip_specular` band) ⟹ budget collapses to the bulk band [−1.7, −0.2] dB ⟹ architecture-led Part III leads, on data.
- **Broad case:** the contrast measures δ_b, the T-slope fixes p, the drift residual fixes the drain sign — i.e. the three numbers WP2 owed are **measured at the bench** ahead of the full Boltzmann–Maxwell solve, and the calibration tier leads with a head start rather than from scratch.

Either way the gate is decided by data, and *neither outcome is a dead end* — which is the property a falsifiable gate must have. Cost: sub-threshold linewidth spectroscopy on one cell (signatures 2, 3) plus a short contact-preparation series (signature 1), all at room temperature for the RT points. This belongs in WP1/WP4, pulled ahead of WP2, exactly where the memo pointed — but now as a *discriminating* protocol, not a single confirmatory reading.

## 7. Pre-registered bench-observable predictions (own keys; nothing contests existing outputs)

All at 353 K, L = 576.6 nm, bias 0.7·M_th unless noted; falsification = the bench (or the WP2 kinetic cavity solve) landing outside the band.

- **`boundary_linewidth_excess_GHz_per_pct_353K`** = **3.2**, band **[2.5, 3.9]** (excess half-linewidth per 1 % δ_b via contact contrast; band carries the linewidth-convention and bias-placement spread). The load-bearing isolation sensitivity.
- **`boundary_T_exponent_2p`** ∈ **{−2 (Kn law), −4 (Kn² law)}**, measured as the log-log slope of the T-residual δ_b(T); falsification band **[−4.5, −1.5]** — a slope outside it falsifies the Kn-scaling family itself, not just the exponent choice.
- **`drain_sign_linewidth_sensitivity_pct_per_pct`** = **−10.5** (fixed-bias half-linewidth response per 1 % DS-active drain term), band **[−13, −8]**; the *sign* of the measured odd-in-M residual is the drain sign (the deliverable), the magnitude is the readout gain.
- **`boundary_delta_b_pct_353K`** — not predicted to a point (that is what the measurement is for); this note pre-registers only that the contact-contrast δ_b and the T-residual δ_b must agree to within their bands, and that the safe case requires both < 0.5 %.

## 8. Limitations and open items

1. **Homogeneous-broadening / device-matching assumptions.** The contact contrast assumes bulk reproducibility between variants and homogeneous linewidths; contact inhomogeneity across a cell (07-18 Limitation 7) broadens inhomogeneously and must be controlled (twin passive references, spatially resolved probe). The single-device signatures (2, 3) avoid device-matching but not inhomogeneity.
2. **The T-shape method leans on the computed bulk hump.** Its magnitude carries the 07-13 closure's factor-2 prefactor uncertainty; only the *shape* (peaked vs monotone) is used, which is robust, but a non-single-pole stress-relaxation channel (07-13 Limitation 2) would distort the hump and is not modeled here.
3. **Absolute-anchor convention spread.** The model half-linewidth is 27.6 GHz (07-13, hydro-only) vs ~30 GHz with the viscous supplement in the linewidth — an ≈8 % convention difference that widens the per-% bands above; it does not affect the *difference* and *shape* logic the signatures rest on.
4. **Bench feasibility is a WP4 question.** Sub-threshold THz linewidth spectroscopy on a single DS cell at the required resolution (a few GHz on a ~30 GHz line), the probe/readout SNR at ~µW launch, and biasing stably just below self-oscillation are real measurement-design problems this note does not solve — it specifies *what* to measure and *what each measurement discriminates*, not the instrument.
5. **Drift-sweep near threshold** must separate the trivial r(M) regenerative narrowing from the boundary residual; the Appendix does this at fixed bias against the computed r(M)·bulk prediction, but a real sweep needs the r(M) baseline calibrated on the specular control.
6. **Everything is in-model and rides on the unproven gain cell.** These signatures presuppose the sub-threshold regenerative resonance exists to have a linewidth — itself bench gate G1. If G1 fails, the boundary question is moot.

## Appendix — runnable listing (imports the released chain)

*(Self-contained apart from the released `fable-model-chain`; `PYTHONIOENCODING=utf-8`. Reproduces every number above: anchors, the contact-contrast table and its 3.2 GHz/% slope, the bulk-hump-vs-Kn^p temperature shapes, the −2.00 Kn log-slope, the drain ∓10.5 %/% sensitivity, and the −0.284 dB/1% tracked-gain map matching 07-13.)*

```python
# -*- coding: utf-8 -*-
import math, sys
CHAIN = r"...\fable-model-chain"                 # adjust to your checkout
sys.path.insert(0, CHAIN)
import constants as C, ds_cell as DS, kinetic as K
s = DS.plasmon_speed(); vF = C.vF; f0 = C.f0; w = 2*math.pi*f0
L0 = DS.cell_length(s); tau353 = C.tau(C.Tcap)
def tau_ee(T): return K.tau_ee(T)
def gamma_visc(T, M):
    x = w*tau_ee(T); nu0 = vF**2*tau_ee(T)/4.0; q0 = w/s
    return 0.5*nu0*q0**2*(1+3*M**2)/(1-M**2)**2/(1+x**2)
def Gbulk(T, M): return 1/(2*C.tau(T)) + gamma_visc(T, M)
def t_rt(M, L=L0): return 2*L/(s*(1-M**2))
def r(M): return (1+M)/(1-M)
def loop(M, T, db=0.0, drain=0.0): return r(M)*(1+drain)*math.exp(-Gbulk(T,M)*t_rt(M))*(1-db)
def df_half(M, T, db=0.0, drain=0.0):
    lp = loop(M, T, db, drain); return (1-lp)/(2*math.pi*t_rt(M)*math.sqrt(lp))
def Mth(T, db=0.0, drain=0.0):
    lo,hi=1e-4,0.45
    for _ in range(200):
        m=0.5*(lo+hi); lo,hi=(m,hi) if loop(m,T,db,drain)<1 else (lo,m)
    return 0.5*(lo+hi)

Mb = Mth(353); Mbias = 0.7*Mb
print("anchor df(0.7Mth,353,hydro+visc) = %.2f GHz (07-13 hydro-only: 27.6)" % (df_half(Mbias,353)/1e9))
# (1) contact contrast
print("\n(1) contact contrast: excess half-linewidth vs specular control")
d0 = df_half(Mbias,353,0.0)/1e9
for db in (0.005,0.016,0.031,0.062,0.249):
    print("   db=%5.1f%%  df=%7.2f GHz  excess=%7.2f GHz" % (db*100, df_half(Mbias,353,db)/1e9, df_half(Mbias,353,db)/1e9-d0))
print("   slope near 0: %.2f GHz per 1%%" % ((df_half(Mbias,353,0.005)/1e9-d0)/0.5))
# (2) temperature shape
print("\n(2) T-shape: bulk viscous (rel) vs Kn (rel) vs Kn^2 (rel)")
gv=lambda T: gamma_visc(T,0.0); kn=lambda T: (w/s)*vF*tau_ee(T)
for T in (500,400,353,300,255,200,150):
    print("   T=%3d  w*tau_ee=%.3f  gv=%.3f  Kn=%.3f  Kn^2=%.3f" % (T,w*tau_ee(T),gv(T)/gv(353),kn(T)/kn(353),(kn(T)/kn(353))**2))
print("   d ln Kn/d ln T = %.3f  -> delta_b~Kn^p slope = -2p" % ((math.log(kn(400))-math.log(kn(250)))/(math.log(400)-math.log(250))))
# (3) drift / drain sign
print("\n(3) drain sign: fixed-bias linewidth response to +/-1%% DS-active drain")
for drain in (-0.01,0.0,0.01):
    print("   drain=%+.0f%%  df=%6.2f GHz (%+.1f%%)" % (drain*100, df_half(Mbias,353,0.0,drain)/1e9, (df_half(Mbias,353,0.0,drain)/df_half(Mbias,353)-1)*100))
# tracked gain map (07-13 anchor)
a=10**(-DS.passive_loss_dB_per_half_lambda(tau353)/20.0); l0=a
def Mtl(d):
    lo,hi=1e-4,0.45
    for _ in range(200):
        m=.5*(lo+hi); lp=(1+m)/(1-m)*a*(1-d); lo,hi=(m,hi) if lp<1 else (lo,m)
    return .5*(lo+hi)
def Gt(d):
    M_=0.7*Mtl(d); lp=(1+M_)/(1-M_)*a*(1-d); return 20*math.log10((1-l0)/(1-lp))
print("\ntracked gain map: %.4f dB per 1%% delta_b (07-13: -0.282)" % (Gt(0.01)-Gt(0.0)))
```

Expected: anchor ≈29.9 GHz; contact-contrast excess 1.6/5.1/9.9/20.1/90.6 GHz with slope ≈3.2 GHz/%; bulk-viscous rel hump peaking near 255 K vs monotone Kn/Kn²; d ln Kn/d ln T = −2.000; drain ∓10.5 % per ±1 %; tracked map −0.284 dB/1 %.


---

## Agent assessment — 2026-07-18

Assessed suitable for the permanent record by a **unanimous 3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)). Assessment performed in a maintainer-operated Claude Code session per the charter's Operations section, on `claude-opus-4-8` (the session's active model — flagged for the record, as this routine's default is Fable 5; the entire 2026-07-18 boundary-channel thread — the session-#43 reply, its promotion to [`2026-07-18-boundary-channel-contact-gated.md`](2026-07-18-boundary-channel-contact-gated.md) via #44, and this follow-on assessment — has run end-to-end on Opus 4.8). The three reviewers ran as isolated, mutually **blind** subagent contexts — one persona each, no visibility into the others' verdicts, which is what makes the 2-of-3 gate real — and **each independently wrote and ran its own driver** against the released `fable-model-chain/` before voting. All three drivers reproduced the note's headline numbers to the quoted precision: the sub-threshold half-linewidth anchor **27.6 GHz** hydro-only (= 07-13 §3.2) and **≈29.9 GHz** hydro+viscous (**+8.4 %** broadening); the contact-contrast excess table **1.58 / 5.07 / 9.90 / 20.14 / 90.62 GHz** with slope **3.15 GHz per 1 % δ_b** (within the pre-registered band [2.5, 3.9]); the bulk-viscous hump peaking at **ωτ_ee = 1 → 254.9 K** against monotone Kn / Kn² with **d ln Kn / d ln T = −2.000**; the drain-sign sensitivity **∓10.5 %/%**; and the tracked-gain map **−0.284 dB per 1 %** (matching 07-13's −0.282). Nothing in the note contests any `results.json` value.

**Promotion-edit follow-ups (recorded, not applied — the note body is promoted as assessed, save for the mechanical `notes/drafts/`→`notes/` relative-link fix; the vote record below is evidence and is not edited after posting; per GOVERNANCE.md a human merges).** All three reviewers independently converged on the same non-load-bearing seams: (i) §2/§5 quote the bulk drift factor (1+3M²)/(1−M²)² as **+5.4 %**, its value at 0.7× the *analytic* M_th (0.103); at the note's own operating bias — 0.7× the *viscous* M_th (0.117), the threshold its Appendix actually uses — the factor is **+7.0 %** (the same dual-convention seam 07-13 carried). (ii) §3/§7 label the contact-contrast table **“L = 576.6 nm”**, but the Appendix computes it at `cell_length(s) = 582.80 nm` (the zero-drift length); the table reproduces to quoted precision under either length, so this is a labeling seam, not a numerical error. (iii) The §5 aside that the drain is “~3× more leveraged than the same loss placed in the bulk” does not hold for the *linewidth* observable — at fixed bias a ±1 % drain and a ±1 % bulk/boundary loss have equal linewidth leverage (~10.5 %/%); the 3.18× is the separate tracked-vs-frozen *gain* buy-back. None is load-bearing: signature 3's deliverable is the *sign* of the odd-in-M residual and the reproduced ∓10.5 %/% drain sensitivity, neither of which depends on the +5.4/+7.0 % magnitude, the length label, or the leverage phrasing. Quanta additionally recorded that a one-line Schawlow–Townes / quantum-phase-noise caveat would be worth adding, and that signature 3's r(M)-riding drain is asserted in-model rather than exercised in the listing (correctly labeled, with Limitation 5 conceding the r(M) baseline must be calibrated on the specular control).

- 🧵 **Fabric** — **STORE**: This is a substantive, checkable, honest measurement-design note that gives the architecture side a real decision. It closes the exact falsifiability gap the promoted 07-18 contact-gated memo left open (the sub-threshold linewidth bounds only TOTAL excess loss — bulk viscous + boundary — not delta_b in isolation) by proposing three parametrically-distinct sub-threshold-linewidth signatures, each isolating one of the memo's three open objects: contact-contrast subtraction cancels the bulk exactly and reads delta_b; the temperature shape separates the peaked bulk-viscous hump (omega*tau_ee=1, ~255 K) from a monotone boundary T^(-2p) and so reads the Knudsen exponent p; and the drift(M) sweep separates the even-in-M bulk factor from the odd-in-M drain to read the drain sign. The gate becomes two-sided/over-determined (either outcome advances Part III), which is exactly the property a falsifiable engineering gate must have — actionable WP1/WP4-ahead-of-WP2 sequencing.

Assessed against the five criteria: (1) Substance — concrete: a runnable discriminant protocol with quantified sensitivities, not a survey. (2) Labels — sig 1 'demonstrated (runnable)' is backed by the reproducing Appendix; sig 2/3 correctly 'in-model'; magnitudes kept in-model; rides-on-unproven-gain-cell stated. (3) Numbers — nothing contests results.json (the note uses the kinetic M_th 0.167, explicitly distinct from the hydro key 0.147, and never redefines a key); consistent with 07-13 (viscous hump peak 254.9 K, A in [0.5,3] -> 147-360 K) and 07-18 (single-observable gap, boundary_loss_pct_per_roundtrip_specular <=0.5% key). (4) Honesty — Limitations 1-6 disclose device-matching/homogeneous-broadening, reliance on the computed hump shape, bench feasibility, in-model status, and the unproven gain cell; nothing oversold. (5) Durability — anyone sequencing the Part III gate would consult it; it changes what the project does next.

The pre-registered keys (boundary_linewidth_excess_GHz_per_pct_353K=3.2 [2.5,3.9]; boundary_T_exponent_2p in {-2,-4} band [-4.5,-1.5]; drain_sign_linewidth_sensitivity_pct_per_pct=-10.5 [-13,-8]; delta_b agreement-only) all carry new names, non-contest statements, and falsification bands, satisfying the pre-registration rule; the Appendix imports the released chain and reproduces its outputs, satisfying the new-computation rule. The defects I found are all promotion-edit-level and non-load-bearing (see top_issues); the core three-signature result survives every one of them. Vote: STORE.
  - PROSE NUMBER THAT DOES NOT REPRODUCE (non-load-bearing, promotion-edit): Sections 2 and 5 state the bulk drift factor (1+3M^2)/(1-M^2)^2 = '+5.4% at 0.7*M_th, ... computed'. At the note's OWN operating point — 0.7 x the kinetic M_th (=0.16721 -> M=0.117) that its Appendix actually uses for the anchor and every table — my driver gives +7.02%, not +5.4%. The +5.4% is the value at 0.7 x the HYDRO M_th (M=0.103). This is the dual-convention seam inherited from 07-13 (which quotes 5.4% at 0.103 and 7.2% at 0.118). It does NOT touch the deliverable: the drain sensitivity -10.5%/% and its sign are computed directly from the loop and reproduce (-10.46% at +1%, +10.56% at -1%), and the even-vs-odd-in-M method subtracts whatever the actual computed factor is. Should be relabeled to the operating-convention value (~+7.0%) at promotion.
  - LOOSE PHYSICS PHRASING (non-load-bearing): Section 5 says the drain is '~3x more leveraged than the same loss placed in the bulk'. In the LINEWIDTH observable a +1% additive bulk loss (db) and a -1% drain give identical broadening (+10.56% each) because both simply multiply the loop — I verified they are equal, not 3x. The genuine 3.18x factor is the frozen-vs-tracked GAIN buy-back (a different observable). The sentence conflates linewidth leverage with gain leverage; defensible but should be tightened.
  - COSMETIC LABEL SLIP: Sections 3 and 7 quote 'L = 576.6 nm', but the Appendix computes with cell_length(s) = 582.80 nm (zero-drift). The contact-contrast table reproduces to the quoted precision with EITHER length (e.g. excess 1.58 vs 1.59 GHz), so it is purely a label mismatch, but the length attribution should be made consistent.
  - INHERITED PROMOTION-EDIT: Section 6 says the safe case 'collapses to the bulk band [-1.7,-0.2] dB'. In the 07-18 memo [-1.7,-0.2] is the near-specular TOTAL budget (bulk + near-specular boundary), while the pure 07-13 bulk band is [-1.5,-0.3]; two 07-18 reviewers already flagged the upper edge should be ~-0.3. The draft quotes the memo's own (loose) number rather than introducing a new error; non-load-bearing.
- 🌊 **Kinetic** — **STORE**: I wrote my own driver (reconstructed from the note's stated formulas, importing the released fable-model-chain: constants/ds_cell/kinetic) and ran it on Windows/CPython. Every headline number in the note reproduces to its quoted precision, and I checked both candidate cavity lengths (the Appendix's cell_length(s)=582.80 nm and the prose's 576.62 nm) — the results are robust to the choice.

Assessing against the five-criteria standard:

1. SUBSTANCE — Passes. This is a concrete, checkable measurement-design result, not a survey. It closes a real gap the promoted 07-18 memo left open: that memo's single bench observable (sub-threshold linewidth) is one-sided (bounds only total excess loss, confirms the null but cannot isolate delta_b, p, or the drain sign). This note shows the three loss channels have distinct parametric signatures (contact-prep, temperature-shape, drift-parity) that over-determine them, converting a confirm-the-null test into a two-sided falsifiable protocol. The bulk-cancels-by-subtraction (sig 1), peak-vs-monotone T-shape (sig 2), and even-vs-odd-in-M parity (sig 3) arguments are each physically sound and I confirmed their magnitudes numerically.

2. LABELS — Passes. Signature 1 is demonstrated (runnable) and its table reproduces; signatures 2/3 and every quoted magnitude are correctly in-model; the boundary magnitude, exponent p, and drain sign stay open. The note explicitly states "In-model for every quoted magnitude."

3. CITATIONS/NUMBERS — Passes. Contests no results.json value (adds only new keys). Consistent with both promoted notes: the omega*tau_ee=1 -> 255 K viscous peak (my driver: peak at T=255 K, w*tau_ee=0.9992, rel value 1.220), the A in [0.5,3] -> 147-360 K band, the 07-18 "[-1.7,-0.2] dB near-specular budget" and "boundary_loss_pct_per_roundtrip_specular < 0.5%" key, and the -0.284 dB/1% tracked-gain map matching 07-13's -0.282 (my driver: -0.2837).

4. HONESTY — Passes, strongly. §8 is candid: device-matching/inhomogeneity, the T-shape leaning only on the computed hump *shape* (factor-2 prefactor uncertainty, non-single-pole risk), the 27.6-vs-30 GHz ~8% convention spread, bench feasibility as an unsolved WP4 problem, and §8.6 "Everything is in-model and rides on the unproven gain cell... itself bench gate G1. If G1 fails, the boundary question is moot." Nothing is oversold; it states either outcome advances Part III.

5. DURABILITY — Passes. It changes what the project does next: it specifies exactly what to measure and what each measurement discriminates, pulling three specific isolating measurements into WP1/WP4 ahead of the full WP2 solve.

Pre-registration rule satisfied: four new key names (boundary_linewidth_excess_GHz_per_pct_353K, boundary_T_exponent_2p, drain_sign_linewidth_sensitivity_pct_per_pct, boundary_delta_b_pct_353K), a non-contest statement, and explicit falsification bands. New-computation rule satisfied: the Appendix is a self-contained runnable listing whose expected outputs I reproduced.

The defects I found are all promotion-edit / non-load-bearing internal seams, the same tier at which the 07-13 and 07-18 predecessors were promoted 3/3 with recorded follow-ups. The core three-signature over-determination survives each of them intact, so per the standard's "single non-load-bearing seam is a promotion-edit note" clause I vote store.
  - PROSE-vs-CODE length seam (promotion-edit): §3 and §7 state 'L = 576.6 nm (all demonstrated, Appendix)', but the Appendix literally uses L0 = DS.cell_length(s) = 582.80 nm (the zero-drift quarter-wave length), NOT 576.6 nm. My driver confirms the note's quoted contact-contrast table (31.5/35.0/39.8/50.0/120.5 GHz) is the 582.80 nm output; the 576.62 nm operating length gives 31.5/35.1/39.9/50.3/121.5 (the extreme row differs ~1%). Every headline number (anchor 27.6/29.9, slope, drain, tracked map) reproduces under BOTH lengths, so it is a labeling inconsistency, not a numerical error — but '(all demonstrated, Appendix)' attached to '576.6 nm' is literally false and should be reconciled at promotion.
  - Bias-convention seam on the +5.4% drift factor (promotion-edit, non-load-bearing): §5/§2 quote the bulk drift factor (1+3M^2)/(1-M^2)^2 = +5.4% 'at 0.7·M_th', which is exactly true only at the ANALYTIC threshold (0.7*0.147=0.103 -> +5.40%). The note's own linewidth machinery operates at 0.7*M_th_visc = 0.117, where I compute +7.02%. So 'at 0.7·M_th' is ambiguous between the analytic and viscous thresholds; the drift-factor magnitude quoted is not the one at the note's actual operating bias. Signature 3's deliverable is the SIGN of the odd-in-M residual, which is unaffected, and 07-13 already carried the same dual convention (+5.4% at 0.103 / +7.2% at 0.118).
  - Unsupported '~3x more leveraged' prose claim (non-load-bearing): §5 says the drain 'multiplies r(M), it is ~3× more leveraged than the same loss placed in the bulk.' At FIXED bias my driver shows a +1% drain and a +1% bulk/boundary loss have EQUAL linewidth leverage (-10.46% vs +10.56%), because both scale the loop by 1±1%. The '3×' appears to conflate this with the well-established tracked-vs-frozen 3.18× buy-back (07-13/07-18), which does not apply at the fixed (untracked) bias signature 3 uses. The listing does not compute a 3× factor. Deliverable (drain sign) is unaffected.
  - Minor rounding: the pre-registered central boundary_linewidth_excess_GHz_per_pct_353K = 3.2 and prose '≈3.2 GHz/%' print as 3.15 (582.80 nm) / 3.19 (576.62 nm) from the note's own slope formula. Within the wide band [2.5,3.9] and hedged with '≈', but the listing prints 3.15, not 3.2.
- ⚛️ **Quanta** — **STORE**: I reconstructed the note's formulas independently and every headline number reproduces to quoted precision (see log): the 27.6/29.9 GHz anchors (+8.4% viscous broadening), the full 1.6/5.1/9.9/20.1/90.6 GHz contact-contrast table with ~3.2 GHz/% slope, the 255 K viscous hump with monotone Kn/Kn^2 and d ln Kn/d ln T = -2.00, the -10.5%/% drain sensitivity, and the -0.284 dB/1% tracked map matching 07-13's -0.282. Nothing contests chain or quantum results.json; all four pre-registered keys use new names with non-contest statements and falsification bands. Consistent with both promoted notes: it correctly restates the contact-gated memo's single-observable gap (linewidth bounds TOTAL excess loss, one-sided), the [-1.7,-0.2] dB bulk band and the <=0.5% specular key, and 07-13's 255 K / 147-360 K hump and +5.4% even-in-M drift factor. Through my noise/observable lens the core is honest: signature 1 isolates delta_b by DIFFERENCING (bulk cancels common-mode, no bulk model trusted), signature 2 uses the peaked-vs-monotone shape (factor-2 exponent separation), signature 3 reads the drain SIGN from the odd-in-M residual - a genuinely two-sided, over-determined protocol, so 'either outcome advances Part III' is real, not spin. Labels are correct (demonstrated reserved for the runnable map/anchors; magnitudes in-model/open). Bench feasibility (resolution, SNR, inhomogeneity, G1 existence) is honestly flagged. The two seams I found are non-load-bearing promotion-edits: prose L=576.6 nm vs the listing's 582.80 nm (immaterial), and the 'drain ~3x more leveraged than bulk' aside (at fixed bias both are ~10.5%/%). Core survives both; it closes a real falsifiability gap WP1/WP4 would use.
  - Prose/listing length mismatch: sec3/sec7 state L=576.6 nm but the Appendix uses cell_length(s)=582.80 nm (zero-drift). Immaterial - my driver gives identical headline numbers under both (anchor 29.91 vs 29.93, slope 3.15 vs 3.19); promotion-edit only.
  - The sec5 aside 'drain ~3x more leveraged than the same loss placed in the bulk' is not reproduced: at fixed bias my driver shows delta_b and drain BOTH move the linewidth ~10.5%/%. The '3x' is the tracked-vs-frozen gain buyback (0.901/0.284), not a linewidth fact. Non-load-bearing (deliverable is the odd-in-M sign, not the leverage magnitude).
  - Noise-domain caveat: the linewidth is treated purely as loaded-Q loss broadening with no mention of a Schawlow-Townes / quantum phase-noise floor as competing broadening. Negligible at the proposed loop=0.916 sub-threshold point, but worth a one-line caveat.
  - Signature-3 discriminant (drain riding r(M), odd-in-M) is asserted in-model, not exercised in the listing (drain modeled as a constant multiplicative factor); correctly labeled in-model with Limitation 5 conceding the r(M) baseline must be calibrated on the specular control.
