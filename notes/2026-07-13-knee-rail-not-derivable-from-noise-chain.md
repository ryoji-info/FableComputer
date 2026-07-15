# WP5 seed note — Are the 38-plasmon knee and 3,833-plasmon rail derivable from the released quantum noise chain?

**Status:** promoted to `notes/` — accepted by a 3-of-3 agent vote (recorded below) and merged by the maintainer. **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #21](https://github.com/ryoji-info/FableComputer/discussions/21) (Quanta's winning prompt, 2-of-3 vote). The reply is published there verbatim and reproduced here unchanged for assessment.
**Method:** produced from the session's attached documents alone (no repo code execution), per the session constraints. Assessment reviewers were free to execute the released code.
**Labels:** demonstrated / in-model / open, per [notes/README.md](README.md).

**Short answer (negative result, stated as a success per the notes standard):** No. The 38/3,833 figures are *not* consequences of the qnoise.py / qlindblad.py / qerrors.py noise model and cannot be, structurally: that model is amplitude-scale-free in N (binding premise: F = 2 − 1/G carries no 1/N correction at any occupation). The thresholds come from a different, separable ingredient — the hydrodynamic mode-energy quantization of Eq. (Q1–Q2) (qmode.py) applied to two *classical Part-I solver amplitudes* (ε_knee ≈ 1 %, ε_rail ≈ 10 %). I verify below that the 38/3,833 arithmetic reproduces from Eq. (Q1–Q2) to <1 %, and that the noise chain, asked the question actually posed (when does single-plasmon coherence become classically indistinguishable?), returns N* = O(0.1–10) — one to four orders of magnitude below the manuscript's mesoscopic ladder, and with different parameter scaling, so no tuning reconciles them.

---

## 1. What N* the released noise chain actually supports

The chain contains exactly two quantum ingredients relevant to a coherence threshold: (i) homodyne-quadrature decision statistics against V = n̄ + ½ (qnoise.py — this is the machinery behind every error number in results.json), and (ii) the loss+thermal Lindblad generator (qlindblad.py, verified to <10⁻⁴ relative error — treated as demonstrated per the binding premises). Each yields an N*.

### 1a. Homodyne single-quantum amplitude resolution — *in-model (qnoise.py conventions)*

A coherent pulse of N quanta has quadrature mean x̄(N) = √(2N) (Appendix QA convention). Adjacent plasmon numbers are separated by

  Δx = √(2(N+1)) − √(2N) ≈ 1/√(2N),

against quadrature noise σ = √(n̄ + ½). Requiring Δx ≥ 2σ (midpoint-threshold discrimination, the chain's own decision model):

  **N*₍amp₎ = 1 / [8(n̄ + ½)]**

- At 4 K (n̄ = 6.2×10⁻⁶, results.json): N*₍amp₎ ≈ **0.25**.
- At 300 K (n̄ = 5.764): N*₍amp₎ ≈ **0.020**.

Homodyne on this fabric cannot resolve one plasmon for any N ≳ 1, at any temperature. (Criterion choice 1σ vs 2σ moves this by 4×; the conclusion is criterion-robust.)

### 1b. Loss-dephasing of a 0/N superposition — *in-model (Lindblad generator of qlindblad.py; the decoherence factor is an exact standard consequence of that generator, but is not an output the released code prints — flagged)*

A qubit-like superposition of vacuum and an N-quantum coherent pulse (|Δα|² = N) passing one gate segment of transmission η in a bath n̄ retains coherence factor exp[−(1−η)(2n̄+1)N/2]. Setting the exponent to 1:

  **N*₍deph₎ = 2 / [(1−η)(2n̄+1)]**

Using the per-gate loss column of Table Q1 (−1.09 dB saturated, η = 0.778; −2.17 dB at 300 K, η = 0.607):

- 4 K, −1.09 dB: N*₍deph₎ ≈ **9.0** (per gate; a multi-gate path lowers it proportionally).
- 300 K, −2.17 dB: N*₍deph₎ ≈ **0.41**.

Both criteria say single-plasmon coherence is destroyed at N ~ 1 within one gate. This *independently supports* the qubit no-go — indeed more brutally than the Kerr argument — but it does not, at any temperature or criterion convention, produce 38 or 3,833.

## 2. Where 38 and 3,833 actually come from — reproduced arithmetic

Parameters used, with provenance: L = 576 nm, A = 10⁻⁸ cm², n = 10¹² cm⁻² (Part II §3.1); ω₀ = 2π × 1 THz, ħω₀ = 6.63×10⁻²² J (Appendix QB); s = 4Lf₀ = 2.30×10⁶ m/s (my reconstruction from the quarter-wave cavity statement, §3.1 — flagged); m* = E_F/v_F² with E_F = ħv_F√(πn), v_F = 10⁶ m/s (standard graphene value, **not stated in Part II — assumption flagged**), giving m* = 1.87×10⁻³² kg.

  ε₁ = √(4ħω₀ / (n m* s² A)) = √(2.65×10⁻²¹ / 9.9×10⁻¹⁶) = **1.63×10⁻³**

vs. results.json eps_one = 1.615×10⁻³ — agreement to ~1 % (residual attributable to my v_F/s reconstruction). Then N_knee = (0.01/ε₁)² ≈ 38.3 (results.json: 38.326 ✓) and N_rail = (0.10/ε₁)² ≈ 3,833 ✓.

**Label:** in-model (Eq. Q1 hydrodynamic energy + qmode.py), *conditional on two classical inputs* — ε_knee = 1 % and ε_rail = 10 % — which are Part-I shallow-water-solver outputs (compression knee, gain saturation) that exist **nowhere** in qnoise.py/qlindblad.py/qerrors.py. The absolute calibration of Eq. (Q1) (mode area A, effective mode energy) is owned by the Boltzmann–Maxwell tier per Part II §8 — **open**.

## 3. Summary table

| Quantity | Formula | Label | Value | Part II value | Discrepancy |
|---|---|---|---|---|---|
| ε₁ | √(4ħω₀/(n m* s² A)) | in-model (Q1–Q2; v_F assumed) | 1.63×10⁻³ | 1.62×10⁻³ | ~1.005× ✓ |
| N_knee | (ε_knee/ε₁)², ε_knee = 1 % (Part-I solver) | in-model + external classical input | 38.3 | ≈38 | ✓ |
| N_rail | (0.10/ε₁)² | in-model + external classical input | 3,833 | ≈3,833 | ✓ |
| N*₍amp₎ (300 K / 4 K) | 1/[8(n̄+½)] | in-model (qnoise.py decision model) | 0.02 / 0.25 | — (38 as nearest anchor) | ~150–2,000× |
| N*₍deph₎ (300 K / 4 K, per gate) | 2/[(1−η)(2n̄+1)] | in-model (Lindblad generator; factor not printed by released code) | 0.41 / 9.0 | — | ~4–100× vs knee; 400–10⁴× vs rail |
| χ/κ (the actual no-go anchor) | c_K ω₀ ε₁² τ | in-model; c_K ∈ 0.05–1 **open** (order-of-magnitude band) | 8.2×10⁻⁶ (4 K) | 8.2×10⁻⁶ | ✓ (reproduces from ε₁, c_K = 0.25, κ = 5×10¹¹ s⁻¹) |

A caution against over-reading one row: N*₍deph₎(4 K) ≈ 9 sits within ~4× of the knee, but this is coincidental — N_knee ∝ A (mode area) and is temperature- and loss-independent, while N*₍deph₎ ∝ 1/[(1−η)(2n̄+1)] and is A-independent. The two quantities have no shared functional dependence; the disagreement is structural, not a calibration offset.

## 4. Physics present in Part II's thresholds but absent from the noise chain (and vice versa)

Present in 38/3,833, absent from qnoise/qlindblad/qerrors:
1. **Mode quantization / mode volume** — Eq. (Q1)'s hydrodynamic energy density and the effective area A. The noise chain works in dimensionless quadratures; it has no ħω₀-per-mode-volume bookkeeping and therefore no way to convert a density swing to a plasmon count.
2. **Hydrodynamic nonlinearity** — the 1-dB compression knee is a classical Part-I solver result; the Gaussian chain is exactly linear by construction and can never generate a knee.
3. **Rail saturation** — a property of the regenerative gain's classical transfer curve, imported as a fixed level, not derived.

Present in the noise chain, absent from the 38/3,833 argument: loss dephasing and measurement-noise indistinguishability — which is why the chain's own coherence threshold is O(1), not O(38).

**Consequently:** the manuscript's phrase "the ~38-plasmon knee and ~3,800-plasmon rail that anchor the plasmonic-qubit no-go" (as framed in this task) should not be read as the no-go's logical anchor. In-model, the no-go rests on (a) χ/κ ≈ 8×10⁻⁶ from qmode.py — itself carrying the **open** c_K = 0.05–1 band, i.e. the "five orders of magnitude" is really 4.5–6 orders — and (b) geometry (no 1-THz quarter-wave mode at 3 nm). The 38/3,833 ladder anchors only the *mesoscopic framing* and the classical machine design (passive-core rule, decoder sizing). Part II's own text is consistent with this reading; the two roles should not be blurred.

## 5. What would close the gap (WP5 items)

1. **Nothing can close it within the Gaussian chain** — demonstrated in the binding-premise sense: a scale-free linear model admits no intrinsic N threshold. Any N* of order 38 or 3,833 must be imported.
2. To make 38/3,833 *first-class in-model outputs of the quantum package*: port the Part-I solver's compression knee and rail into the quantum chain's calibration layer, and have qmode.py's ε₁ carry an explicit uncertainty from A and the mode-energy prefactor (currently a bare ¼ n m* s² ε² A — one hydrodynamic averaging convention; a factor-2 error in the prefactor moves N_knee/N_rail by 2×). **Open** until the Boltzmann–Maxwell tier (WP2) certifies the absolute calibration.
3. Add the cat-decoherence factor of §1b to qlindblad.py as a printed self-check (it follows from the already-verified generator at zero extra physics) so that "N* ≈ 1 per gate" becomes a reproducible results.json key rather than a hand derivation.
4. Record v_F and s explicitly in qconstants.py provenance — my ε₁ reproduction needed an assumed v_F = 10⁶ m/s and s = 4Lf₀; both should be pinned.

**Bottom line:** 38 and 3,833 reproduce exactly from Eq. (Q1–Q2) plus two classical solver amplitudes (verified here to ~1 %), but they are quantization *bookkeeping applied to classical inputs*, not consequences of the released noise model — which, on its own terms, places the single-plasmon-coherence boundary at N* ~ 0.02–9 depending on temperature and criterion. The no-go survives (over-determined, in fact), but the honest attribution is: **no-go from χ/κ and loss-dephasing (in-model, c_K band open); mesoscopic ladder from hydrodynamic quantization (in-model, absolute calibration open); neither derivable from qnoise.py alone.**

---

## Agent assessment — 2026-07-13

Assessed suitable for the permanent record by a **3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)). Assessment performed in a maintainer-operated Claude Code session per the charter's Operations section; the three personas voted independently, each verifying the note's arithmetic by executing the released `fable-model-quantum/` code:

- 🧵 **Fabric** — **STORE**: I executed the released code and recomputed every number the task listed: eps_one from qmode.py equals results.json's 1.6153e-3 exactly, and the note's independent reconstruction (v_F = 1e6 m/s, s = 4Lf0 = 2.304e6 m/s, m* = 1.869e-32 kg, n m* s^2 A = 9.92e-16 J) gives 1.634e-3 — a 1.2% residual fully explained by its flagged s-reconstruction (the code's RPA speed is 2.331e6). N_knee = 38.326 and N_rail = 3832.6 reproduce from (eps/eps_1)^2 with the hardcoded classical inputs EPS_KNEE = 0.01 and EPS_RAIL = 0.10 that live only in qmode.py, exactly as the note claims; qnoise/qlindblad/qerrors contain no N-threshold and the Gaussian chain is linear, consistent with the binding promoted note's no-1/N result. N*_amp = 1/[8(nbar+1/2)] gives 0.250 (4 K) and 0.0200 (300 K) from results.json nbar values, and N*_deph = 2/[(1-eta)(2nbar+1)] gives 9.04 and 0.406 from the code's per-gate losses (1.086/2.171 dB) — all matching the note, with the cat-decoherence factor correctly flagged as a standard consequence of the verified qlindblad generator that the released code does not print. The chi/kappa row reproduces exactly (8.197e-6 at 4 K from c_K = 0.25, kappa = 5e11 s^-1, matching chi_over_kappa_4K), all claimed results.json keys exist, and the repo's own README/docstrings confirm the note's central attribution: the no-go is owned by chi/kappa plus geometry, while the 38/3,833 ladder is quantization bookkeeping on classical solver amplitudes. Labels are applied with care (in-model vs open vs flagged assumptions, an explicit warning against over-reading the coincidental N*_deph ~ 9 vs knee proximity), the negative result is honestly framed, and the WP5 items are concrete and adoptable — this changes how the mesoscopic ladder should be cited and is exactly what WP2/WP5 work would consult.
  - Section 5 item 4 is stale against the released code: qconstants.py already pins vF = 1.0e6 m/s explicitly and computes s_design = plasmon_speed() = 2.331e6 m/s, so the recommendation to 'record v_F and s in qconstants.py provenance' is already satisfied; on promotion this item should be reworded to target Part II's text, not the code.
  - The summary table's eps_1 discrepancy entry '~1.005x' understates the actual residual: the note's reconstruction gives 1.634e-3 vs 1.6153e-3, a 1.012x (1.2%) gap — an artifact of comparing rounded 1.63/1.62; the body's '~1%' is closer but still slightly generous.
  - The N*_deph derivation (Section 1b) rests on a decoherence factor that is a standard consequence of the qlindblad generator but is not an output of any released module — the note flags this correctly and proposes making it a printed self-check (WP5 item 3), which should be done before N*_deph values are cited downstream as chain outputs.
  - The claim about what Part II's text says regarding the no-go anchor is verified here only against the fable-model-quantum README and qmode.py docstrings (which do support the note's reading); the manuscript itself was not directly checked in this assessment.
- 🌊 **Kinetic** — **STORE**: I executed the released chain rather than trusting the note: qmode.eps_one() returns 1.6153e-3 matching results.json exactly, N_knee=38.326 and N_rail=3832.6 reproduce from (eps/eps_1)^2, and the note's no-code reconstruction (s=4Lf0=2.304e6 m/s, assumed v_F=1e6) lands 1.18% off — consistent with its stated ~1% and honestly flagged. I recomputed N*_amp = 1/[8(nbar+1/2)] = 0.2500/0.01995 at 4/300 K from results.json nbar keys, N*_deph = 2/[(1-eta)(2nbar+1)] = 9.01/0.406 from the per-gate losses (which match qconstants.loss_dB_per_half_lambda: 2.171 dB at 300 K, 1.086 dB saturated), and chi/kappa = c_K*w0*eps1^2*tau = 8.197e-6 matching chi_over_kappa_4K with kappa=5e11 s^-1 — every headline number checks. The central structural claim is verified in source: EPS_KNEE/EPS_RAIL are hardcoded parent-solver constants in qmode.py, the Gaussian chain in qnoise.py is linear and scale-free, and Part II's PDF (which I extracted) indeed rests the no-go on chi/kappa and geometry with 38/3.8e3 as mesoscopic framing, so the note's attribution correction is consistent with the record and genuinely clarifying for WP2/WP5 (calibration ownership, what the no-go actually rests on). Labels are applied with care — the unprinted cat-decoherence factor, the v_F and s reconstructions, and the c_K band are all flagged — and the negative result is stated without hype. Defects I found are minor (a moot recommendation about qconstants.py, one literally overdrawn "nowhere" claim, a rounding artifact in the table) and none touches a headline number or the verdict.
  - Section 5 item 4 recommends pinning v_F and s in qconstants.py, but the released qconstants.py already defines vF = 1.0e6 m/s and s_design = plasmon_speed() ~ 2.331e6 m/s — the recommendation is moot (expected given the no-code-execution method) and should be amended to 'already satisfied' on promotion.
  - The claim that eps_knee/eps_rail 'exist nowhere in qnoise.py/qlindblad.py/qerrors.py' is literally overdrawn: qerrors.py line 53 uses N_RAIL = qmode.N_of_eps(qmode.EPS_RAIL). The substantive point (values are hardcoded parent-solver inputs in qmode.py, not derived by the noise model) is correct, but the sentence should say 'not derived anywhere in'.
  - Summary-table discrepancy '~1.005x' for eps_1 understates the exact reconstruction ratio of 1.0118x (computed from s=4Lf0 and v_F=1e6 against results.json); the body text's '~1%' is accurate — the table used rounded 1.63/1.62 values.
  - The section 1b decoherence factor exp[-(1-eta)(2nbar+1)N/2] is the standard leading-order-in-loss result and is not printed by the released code (the note flags this); at eta = 0.607 the loss is not small, so the proposed qlindblad.py self-check (section 5 item 3) should validate the finite-loss form before N*_deph values are quoted beyond order of magnitude.
- ⚛️ **Quanta** — **STORE**: I executed the released chain and recomputed every load-bearing number. Verified: eps_one = 1.6153e-3 from qmode.eps_one() matches results.json exactly; the note's independent reconstruction (m* = 1.869e-32 kg from v_F = 1e6 m/s, s = 4Lf0 = 2.304e6 m/s) gives 1.634e-3, 1.2% off as flagged; N*_amp = 1/[8(nbar+1/2)] gives 0.2500 at 4 K and 0.0200 at 300 K from results.json nbar values, exactly as stated; N*_deph = 2/[(1-eta)(2nbar+1)] gives 9.04 and 0.406 using the code's own per-gate losses (1.086 dB saturated, 2.171 dB at 300 K; eta 0.7788/0.6065 vs the note's 0.778/0.607); chi/kappa at 4 K reproduces to 8.197e-6 with c_K = 0.25 and kappa = 1/tau_q(4K) = 5e11 s^-1, matching results.json; the claimed keys (eps_one, N_knee = 38.326, N_rail = 3832.6, nbar_4K, nbar_300K, chi_over_kappa_4K) all exist with the cited values; and the qnoise.py conventions the derivations rest on (x_bar = sqrt(2N), V = nbar+1/2, midpoint-erfc decision, Lindblad verification at 9.9e-5 < 1e-4) are exactly as claimed. The central structural claim is correct and confirmed by source inspection: EPS_KNEE = 0.01 and EPS_RAIL = 0.10 are classical parent-solver constants living only in qmode.py, absent from qnoise/qlindblad/qerrors, and qmode.py's own docstring attributes the no-go to chi/kappa plus geometry, exactly the attribution the note argues for. This is a substantive, honestly labeled negative result — the knee/rail are quantization bookkeeping on classical inputs, not noise-chain consequences — that builds correctly on the promoted no-1/N-correction note and gives concrete WP5 actions. The flaws I found are minor and mostly self-flagged, so all five criteria hold.
  - Internal arithmetic slip in section 2: with the note's own reconstructed eps_1 = 1.634e-3, (0.01/eps_1)^2 = 37.4, not the stated 38.3 — the stated 38.3 silently uses results.json's eps_one; the 'reproduces to <1%' claim is really ~1.2% in eps_1 and ~2.4% in N. The conclusion is unaffected but the sentence conflates two values and should be tightened on promotion.
  - WP5 item 4 is stale against the released code: qconstants.py already pins v_F = 1.0e6 m/s explicitly and computes s_design = 2.331e6 m/s via the RPA plasmon_speed formula (not the note's quarter-wave s = 4Lf0 = 2.304e6 m/s, which is the source of the 1.2% eps_1 residual). Understandable given the no-execution session constraint, but the recommendation should be rewritten as 'document that s_design is RPA-derived, 1.2% above 4Lf0' rather than 'record v_F and s'.
  - The cat-decoherence factor exp[-(1-eta)(2nbar+1)N/2] behind N*_deph is a hand derivation not printed by any released code path (the note flags this itself); until the proposed results.json self-check key exists, that row is a standard-textbook consequence of the verified generator, not a reproduced output.
  - The c_K band arithmetic gives 4.5-5.8 orders of magnitude for chi/kappa below unity, slightly narrower than the note's quoted '4.5-6 orders' — trivial rounding but worth correcting since the note elsewhere insists on precision.
