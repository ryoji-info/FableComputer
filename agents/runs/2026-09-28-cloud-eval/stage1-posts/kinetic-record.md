# Kinetic 🌊 — stage-1 evidence record, 2026-09-28 (run 1)

Status: **posted**. Drafter seat requested on `claude-opus-5-5`; check seat(s) on the Fable alias (Fable 5.1 in this session). Final word count 515.

## Drafter: prior-art check

Slot: Monday = WP2 development (one design decision with alternatives). Greps run over all of notes/ (including appended vote records and INDEX.md):
(1) `grep -rniE "quasi-static|quasistatic|full-wave|fullwave|FDTD|retard|gradual.channel|tanh\(qd|qd\)|nonlocal|speed of light|Poisson" notes/` hit 07-13 §6 (lines 115/117). It already records q0·d = 0.027 and ω/(c·q0) = 8e-3, i.e. quasistatic to 1e-4, and the WP2 split of EM from kinetics. My first candidate (a quasistatic-vs-full-wave Maxwell decision) duplicated this, so I dropped it.
(2) `grep -rniE "second-order|MacCormack|WENO|spectral method|Chebyshev|Galerkin|high-order|higher-order|Runge|RK4|implicit|eigen(value)? ?solve|core-hour|workstation" notes/` shows 08-07 already carries the WP2 spatial-order error budget (a high-order interior buys ≈19.7× before the contact binds; C ≲ 24) and the eigvals timing at N = 960 (1920×1920 in 2.5–3.0 s). A spatial-scheme decision would duplicate that, so I dropped it too.
(3) `grep -rniE "angular|harmonics|discrete.ordinate|S_N|half-range|Fourier coeff|ellip|conic|boosted|drifted (local )?equilibrium|1 ?- ?b ?cos|eigvals|continued fraction" notes/` returns three things. 07-13 §6 states the "~10³ spatial × 10² angular harmonics" budget as an assertion, with no convergence basis. 07-20 §2.3 poses the half-range Maxwell accommodation condition, recommends a "σ_c-swept half-range moment solve at Kn = 0.249", and names the Callaway two-rate operator. 07-18 notes it did not carry a half-range Gross–Ziering solve.
Nothing in notes/ derives the angular spectrum of the drifted Dirac-cone equilibrium (the T-independent (1−b cosθ)^−p form and the ρ = (1−√(1−b²))/b decay). Nothing gives the perturbation's harmonic ratio, the harmonic count at either side of the bias fork, a half-range-Gauss vs Fourier comparison at a diffuse contact, or the dense-vs-sparse eigen-solve budget that follows. The post builds on 07-13 §6 and 07-20 §2.3 rather than re-announcing them.
(4) The scout subject `grep -rnoiE "(eps_z|speed_band|permittivity)" notes/` returned nothing. It differs from the three recent scouts (passive interconnect, elasticity register over d/R_th/…, isolation) and from Fabric's same-day scout (mutation testing). ε_z was not in 09-02's list of unbanded parameters.
Limits: I did not search earlier Agent Lab threads beyond the run-context extracts. #124 is cited only as an unpromoted session output.

## Drafter: citations checked

- notes/2026-07-13-kinetic-correction-signed-band.md §6 ("The WP2 consequence", line 117): "Resolution ~10³ spatial × 10² angular harmonics; a workstation-days job, not a cluster job." It supports the post's quoted 07-13 budget. Line 73 carries the "cavity half-linewidth of 2.76 % (27.6 GHz)". The vote record (Fabric seat, line 245) asks that it be called model-derived, and the post calls it "model-derived".
- notes/2026-07-20-source-contact-knudsen-exponent-open.md §2.3: "At x=0 the incoming half (v_x > 0) is set by Maxwell accommodation on the outgoing half: f_in(0, v) = (1−C_acc)·f_specular(0, v) + C_acc·f_wall". This is the half-range accommodation condition and the C_acc = 1 (fully diffuse, drift-free f_wall) case the contact test models. §2.2 gives the "Two-relaxation-time Callaway operator", the operator named in the post. §2.1 gives "Boundary Knudsen number Kn ≡ q₋·l_ee = 0.2493", which I reproduced as 0.24934.
- notes/2026-08-01-ratio-bias-gain-table.md, via its INDEX row: "the bias fork survives the continuum at ≈ +0.3 dB". 07-31's INDEX row adds: "the comparison ... straddles two bias conventions (0.7·M_th_analytic on the gain leg, 0.7·M_th_num on the requirement leg) ... open". This supports calling 0.7·M_th_353K and the 0.118 literal (≈ 0.7·M_th_num, per 08-07) the two sides of the open bias fork.
- Discussion #124 is cited only as an "unpromoted" session. The run context says: "A round found an instrument artefact: the root finder discards purely damped roots by construction (abs(w.real) < 1e-6), moving the claimed band's upper edge 0.7175 → 0.6856."
- Fabric's 2026-09-28 post is referenced by name. Its energy band ends are "0.7·M_th_353K = 0.102958 ... and the 0.118 literal", the same two biases I evaluate.
- The ε_z band [3.3, 3.8] and the design value 3.32 come from fable-model-chain/constants.py lines 18–21 ("adopt eps_z = 3.32 as the design point, which places the plasmon speed at the top of the band"). The post phrases this as "near the low edge of its [3.3, 3.8] band (the top of the speed band)".

## Drafter: verification log

```
All scripts are under /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/kinetic/. They import the released modules from /home/user/FableComputer/fable-model-chain unedited. Platform: Linux x86_64, Python 3.11.15, numpy 2.4.6. `git status --short` is empty, so no tracked file was modified.

1) `python3 params.py`
s 2331197.965421007 rel dev vs results 0.0
L0 nm 582.7994913552518 tau353 ps 0.8498583569405099 Mth 0.14708333333333332 json M_th_353K 0.14708333333333332
tau_ee353 fs 82.9872325140912 omega tau_ee 0.5214241600160339
M_th_num json 0.16894319463373791
0.7*M_th_353K M 0.10295833333333332 b=u/vF 0.2400162571898045 rho 0.12178813102405768 eta 2.105472374890862
0.118 literal M 0.118 b=u/vF 0.2750813599196788 rho 0.1402459577838402 eta 1.964357556500275
0.7*M_th_num M 0.11826023624361653 b=u/vF 0.2756880221213265 rho 0.14056770960720189 eta 1.962065987381491
Gamma_m>=2 13226713037717.783 vF/Gamma nm 75.60457364942923 L/(vF/Gam) 7.708521630683801
0.7*M_th_353K q0 q l_ee 0.22367219247373796 |z| 0.0915379371462775
0.7*M_th_353K q- q l_ee 0.24934426212874317 |z| 0.10191075170002027
0.118 q0 q l_ee 0.22367219247373796 |z| 0.0915379371462775
0.118 q- q l_ee 0.2535965901062789 |z| 0.10362482947677018
(q-·l_ee = 0.24934 reproduces 07-20's Kn = 0.2493.)

2) `python3 angular.py` (Part 1: FFT, Nf = 16384)
0.7*M_th_353K b=0.2400 p=2 ... first m with |c_m/c0|<eps: {1e-4: 6, 1e-6: 8, 1e-10: 13}
0.7*M_th_353K b=0.2400 p=3 ... {1e-4: 6, 1e-6: 9, 1e-10: 14}
0.118 b=0.2751 p=2 ... {1e-4: 6, 1e-6: 9, 1e-10: 14}
0.118 b=0.2751 p=3 ... {1e-4: 7, 1e-6: 10, 1e-10: 15}
The observed c9/c8 ratios are 0.135–0.171; they approach ρ asymptotically, with a polynomial prefactor.

3) `python3 bulkquad.py`. Half-range Gauss–Legendre in θ, K nodes per half; errors relative to K = 400:
0.7*M_th_353K density K=4:4.0e-04 K=6:6.7e-06 K=8:1.0e-07 K=10:1.5e-09
0.7*M_th_353K current K=4:5.4e-03 K=6:9.8e-05 K=8:1.6e-06 K=10:2.3e-08
0.7*M_th_353K mom.flux K=4:1.4e-02 K=6:3.7e-04 K=8:8.0e-06 K=10:1.5e-07
0.118 density K=4:6.7e-04 K=6:1.4e-05 K=8:2.7e-07 K=10:4.9e-09
0.118 current K=4:7.0e-03 K=6:1.6e-04 K=8:3.1e-06 K=10:5.8e-08
0.118 mom.flux K=4:1.9e-02 K=6:6.2e-04 K=8:1.6e-05 K=10:3.8e-07
The maximum at K = 10 is 3.8e-7.

4) `python3 contact2.py`. Fully diffuse wall: the incoming half is set to 1 (drift-free), the outgoing half to (1−b cosθ)^−p; moments are taken over the outgoing half.
0.7*M_th_353K out flux | half-range Gauss K=6:3.7e-07 K=8:4.7e-10 K=10:5.2e-13 | Fourier M=10:5.3e-05 M=32:2.0e-06 M=64:2.6e-07 M=100:6.9e-08
0.7*M_th_353K out mom.flux | K=6:1.6e-07 K=8:9.4e-09 K=10:4.7e-11 | Fourier M=10:1.9e-06 M=32:5.8e-09 M=64:1.8e-10 M=100:1.9e-11
0.7*M_th_353K out density | K=6:6.9e-08 K=8:9.9e-11 K=10:3.5e-14 | Fourier M=10:3.1e-05 M=32:9.3e-07 M=64:1.2e-07 M=100:3.1e-08
0.118 out flux | K=6:3.3e-07 K=8:1.8e-10 K=10:3.3e-12 | Fourier M=10:6.4e-05 M=32:2.4e-06 M=64:3.1e-07 M=100:8.3e-08
0.118 out mom.flux | K=6:2.7e-06 K=8:2.1e-08 K=10:7.1e-11 | Fourier M=10:2.7e-06 M=32:8.1e-09 M=64:2.5e-10 M=100:2.7e-11
0.118 out density | K=6:7.7e-08 K=8:7.6e-12 K=10:5.3e-13 | Fourier M=10:4.1e-05 M=32:1.3e-06 M=64:1.6e-07 M=100:4.2e-08
T/T_F 0.26073953754301404
The K = 8 maximum is 2.1e-8. The Fourier M = 100 outgoing flux is 6.9e-8 to 8.3e-8. (The earlier angular.py run gives the same flux numbers: M=32 1.99e-06, M=100 6.93e-08.)
Caveat: Fourier momentum-flux moments converge fast, because the cos² weight vanishes at the jump. The post therefore quotes the Fourier comparison on the outgoing flux only.

5) `python3 timing.py` (dense complex random matrices, numpy.linalg.eigvals, 4 cpus):
1000 1.17 s
2000 4.45 s
4000 24.54 s
Extrapolation (in-model, n³ from the n = 4000 point): 24.54×(10⁴/4000)³ = 383 s ≈ 6.4 min, memory 10⁸×16 B = 1.6 GB; 24.54×(10⁵/4000)³ = 3.83e5 s ≈ 4.4 days, memory 1.6e11 B = 160 GB.

6) Reproduction of committed results.json values:
- `plasmon_speed_design_m_s` 2331197.965421007: relative deviation 0.0 (exact equality measured).
- `M_th_353K` 0.14708333333333332: exact equality (`==` True).
- `speed_band_m_s` [2201384.4943482894, 2337247.3489001123], recomputed with `DS.plasmon_speed(eps_z=C.eps_z_band[1]/[0])`: relative deviations [0.0, 0.0]. Its lower edge relative to design s is −0.055685305580332245 (−5.57 %).
No other results.json value is gated on. The 2.76 % half-linewidth is quoted from 07-13, not recomputed.
```

## Drafter: seat model note

The maintainer requested this drafting seat on claude-opus-5-5 (the 2026-08-13 policy's Opus seat), and it ran on claude-opus-5-5. It is not Fable 5, and the post header names no model.

## Check seat round 1 — verdict: **clear**

### Defects

- [minor] claim: `plasmon_speed`, `M_th_353K` and `speed_band_m_s` reproduce `results.json` exactly (relative deviation 0.0)
  - measured: plasmon_speed 2331197.965421007 2331197.965421007 rel dev 0.0 exact: True / M_th_353K 0.14708333333333332 ... exact: True / speed_band [2201384.4943482894, 2337247.3489001123] ... exact: True — the values reproduce exactly, but `plasmon_speed` is the ds_cell function name; the results.json key is `plasmon_speed_design_m_s`.
  - fix: Write `plasmon_speed_design_m_s` (the key) instead of `plasmon_speed` so the three names in the sentence are all results.json keys.
- [minor] claim: The perturbation falls faster (|z| = 0.092–0.104).
  - measured: z is not defined anywhere in the post. Under the natural reading — harmonic ratio of the streaming resolvent 1/(Γ − iω + i q v_F cos θ), z = (1 − √(1−β²))/β with β = −i q v_F/(Γ − iω) — I get |z| = 0.0915 at q = q0 = ω/s (either bias) and 0.1036 at q₋ = q0/(1−0.118); q₋ at 0.7·M_th gives 0.1019. So 0.092–0.104 reproduces as the span q0 → q₋(0.118), but only after guessing the definition.
  - fix: Name z in five words, e.g. "(|z| = 0.092–0.104, the streaming-resolvent ratio at Γ − iω over q0…q₋)", so the range is checkable without guessing.
- [minor] claim: 0.1402 at the `0.118` literal. These are the two sides of the open bias fork (08-01)
  - measured: 08-01 ratio-bias's fork is 0.7·M_th_analytic = 0.102958 vs 0.7·M_th_num(N) = 0.11826 at N = 240 (continuum 0.104519); the `0.118` literal is run_all.py:54 / thermal.py:50–51's rounding of the N = 240 side (08-07 names it). ρ = 0.140246 at 0.118 (post: 0.1402 ✓); at 0.11826 it would be ≈0.1405. The identification is a fair reading at N = 240 but not 08-01's own numbers.
  - fix: Say "the `0.118` literal (run_all.py's rounding of 0.7·M_th_num at N = 240)" or use 0.7·M_th_num = 0.11826 directly; 08-01 also shows the ratio side moving to 0.1045 in the continuum, which the sentence could acknowledge in three words.
- [minor] claim: the same ends Fabric 🧵 prices today
  - measured: Not verifiable from this seat: the run context records no post by any persona today (K = 0), and Fabric's 2026-09-28 draft is not in my context. If Fabric's post does not price the fork ends, this is a false colleague reference.
  - fix: Orchestrator/drafter to confirm against Fabric's actual 2026-09-28 post; otherwise drop the clause.
- [minor] claim: (whole post length)
  - measured: wc -w post.md → 497 words (including the two URLs and the signature). Over the ~450 target, under the ~500 defect line.
  - fix: Trim ~40 words (e.g. the "Dense also returns every root" sentence and the alternatives' sub-clauses) to land under 450.
- [minor] claim: The bulk needs about ten, so the rest of the 10² can only be a contact budget
  - measured: 07-13 §6 says only "Resolution ~10³ spatial × 10² angular harmonics; a workstation-days job"; it does not decompose the 10² into bulk plus contact. The decomposition is the drafter's inference, stated in the topic line as if it were 07-13's.
  - fix: Soften to "the rest of the 10² is, on my reading, a contact budget" or move the inference out of the topic line.
- [minor] claim: *Open:* my contact test integrates a prescribed jump, not a Knudsen-layer solution.
  - measured: Reproduction shows the outgoing-flux Fourier error (6.94e-8 / 8.31e-8 at M = 100, p = 2) is identical for wall = 1.0 (no value jump, kink only), wall = 1.05 and wall = (1−b²)⁻¹ (true jumps): on this observable the window cos θ·H(−cos θ) is zero on the incoming half, so the jump's harmonics pair to zero beyond m = 1 and the error is set by the window's kink at grazing, not by the jump. The numbers are right; the sentence overstates what the test probes.
  - fix: Say "integrates a prescribed profile against a half-range window (the jump itself is invisible to the flux moment); the Fourier error is the grazing kink's" — one clause.

### Format audit

No top-level heading (grep '^# ' = 0); the first line is a bold one-line topic. Word count measured with wc -w on the saved draft: 497 (URLs and signature included) — over the ~450 target, under the ~500 defect line; flagged minor. Labels: *Demonstrated* on the released-constant compositions (executed here, exact equality measured for the three keys — the "relative deviation 0.0" wording is therefore admissible) and on the eigvals timings (executed); *In-model* on the Callaway/drifted-cone harmonic and quadrature results and on the n³ budget scaling (model and assumptions named: conduction band, Callaway operator, linearized about drifted equilibrium, per energy moment); *Open* on the contact test and holes. One unlabeled code/algorithm-semantics sentence ("Dense also returns every root.") — trivially true, not presented as demonstrated. #124 cited explicitly as unpromoted. One concrete adoptable item present (K = 10 baseline; pre-register K ∈ {10, 14, 20} sweep of ω″; own next check named). `Improvement scout:` line present, on materials metrology (THz ellipsometry of hBN ε_z) — outside today's WP2-development focus and not among the recent scouts (passive interconnect/floorplan, parameter elasticity register, inter-cell isolation). Exact signature "— Kinetic 🌊 (AI research agent · see agents/README.md)" present. Monday slot honoured: one WP2 discretization decision with three alternatives (a)/(b)/(c) and a compute budget. No claim of a fixed posting schedule; no back-fill; no top-level model claim in the post body. "bit-equal"/"bit-for-bit"/"bit-identical" absent (grep). Platform disclosure present (Linux x86_64 / Python 3.11.15 / numpy 2.4.6).

### Prior-art audit

Grepped notes/*.md for 'gauss.legendre|half-range|discrete.ordinate|angular harmonic|angular basis|Legendre', 'eigvals|shift-invert|0.7175|0.6856|4.4 days|160 GB', '0.118' (INDEX, run_all.py, thermal.py), '2.76', 'T/T_F', 'ellipsometr|eps_z'. Findings: no promoted note chooses an angular discretization; 07-13 §6 gives only "Resolution ~10³ spatial × 10² angular harmonics; a workstation-days job" (quoted correctly by the post); 07-18 and 07-20 mention half-range/Gross–Ziering moment solves as what they did NOT do, and 07-20's adoptable calls for "a σ_c-swept half-range moment solve at Kn = 0.249" — the post builds on that, it does not re-announce it. 07-20 §2.3 is indeed "The half-range accommodation condition" with C_acc ∈ [0,1] and the fully-diffuse limit C_acc → 1, as the post cites. 08-01 ratio-bias §0.3/§6 carries the open bias fork (0.7·M_th_analytic vs 0.7·M_th_num(N), persistent ≈ +0.3 dB) — the post treats it as open, consistent with INDEX; its identification of the ratio side with the `0.118` literal (run_all.py:54, thermal.py:50–51; INDEX 08-07 row) is a rounding of 0.11826 at N = 240 (minor). 07-13's "measured cavity half-linewidth of 2.76 %" was flagged by its own assessors as model-derived; the post says "model-derived" — it uses the corrected reading, and I reproduced 27.603 GHz = 2.7603 % from App. B. T/T_F = 0.26 (07-13 §8.3) matches the post's 0.2607. Discussion #124's 0.7175 → 0.6856 root-finder artefact appears in no promoted note; the post cites it as unpromoted, per the run context. The `eigvals` hits in 07-12/08-07 are dense eigensolves of the LF step operator, not a WP2 angular-basis decision. No premise the record has corrected is relied on (the analytic M_th_353K and the numerics-only status of M_th_num are used correctly; nothing rests on the 7.7967 pulse-gain artefact or on the withdrawn items in INDEX). The central finding (half-range GL, K = 10, vs 10² Fourier; budget) is not carried by the record — not a re-announcement.

### Re-execution log

```
Platform: Linux x86_64, Python 3.11.15, numpy 2.4.6, nproc 4. Scratch: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/kinetic/ (post.md, repro_constants.py, timing_eig.py, angular.py, contact.py, lw0713.py, jumpcheck.py). Released fable-model-chain/ imported unedited; git status clean of tracked changes. Reproduction gate: relative tolerance 1e-12 for closed-form values (measured deviation reported); timings accepted within ±10 %.

[1] python3 repro_constants.py
plasmon_speed 2331197.965421007 2331197.965421007 rel dev 0.0 exact: True
M_th_353K 0.14708333333333332 0.14708333333333332 rel dev 0.0 exact: True
speed_band [2201384.4943482894, 2337247.3489001123] [2201384.4943482894, 2337247.3489001123] exact: True
tau_ee(353K) fs = 82.9872325140912
T_F K = 1353.8414746239466  T/T_F = 0.26073953754301404
Gamma = 1/tau_ee + 1/tau = 13226713037717.783  (1/tau_ee=1.20500e+13, 1/tau=1.17667e+12)
0.7*M_th_353K M=0.102958 b=0.240016 rho=0.121788
0.118 literal M=0.118000 b=0.275081 rho=0.140246
eps_z design 3.32 band (3.3, 3.8)
eps_z=3.8 speed rel to design: -5.5685 %  ratio to 2.76 %: 2.018
→ post's 82.987 fs, 0.2607, 1.3227e13, ρ 0.1218 / 0.1402, −5.57 %, "twice" all reproduce (exact equality measured for the three keys; the others to the printed digit).

[2] python3 lw0713.py (07-13 App. B verbatim constants)
07-13 App B: Mb = 0.14768088835596477  half-linewidth GHz = 27.603009591027714  % of f0 = 2.7603009591027714
→ the "2.76 % half-linewidth" the scout cites reproduces; it is model-derived (07-13's own assessors recorded that "measured" should read model-derived), as the post says.

[3] python3 timing_eig.py
cpu_count 4
n=1000 eigvals complex dense: 1.21 s  mem(A)=0.016 GB
n=2000 eigvals complex dense: 4.50 s  mem(A)=0.064 GB
n=4000 eigvals complex dense: 24.46 s  mem(A)=0.256 GB
1e3 x 10: n=1e+04 time~382.2 s = 6.37 min = 0.00 days; mem 1.6 GB
1e3 x 1e2: n=1e+05 time~382164.2 s = 6369.40 min = 4.42 days; mem 160.0 GB
post-scaled from 24.5 s: 1e3 x 10: 382.8 s = 6.38 min = 0.00 days
post-scaled from 24.5 s: 1e3 x 1e2: 382812.5 s = 6380.21 min = 4.43 days
→ post's 1.17 / 4.45 / 24.5 s reproduce within 3.4 % / 1.1 % / 0.2 %; the n³ scaling to 6.4 min / 1.6 GB and 4.4 days / 160 GB is arithmetic and reproduces.

[4] python3 angular.py
=== (1) Fourier harmonics of (1-b cos th)^-p: first m with |c_m/c_0| < 1e-6 ===
0.7*M_th_353K  p=1 b=0.24002 rho=0.12179  ... -> first m<1e-6: 7
0.7*M_th_353K  p=2 b=0.24002 rho=0.12179  |c_m/c_0|: m=6 4.45e-05 m=7 6.20e-06 m=8 8.49e-07 m=9 1.15e-07 m=10 1.54e-08 -> first m<1e-6: 8
0.7*M_th_353K  p=3 b=0.24002 rho=0.12179  |c_m/c_0|: m=6 1.70e-04 m=7 2.65e-05 m=8 4.03e-06 m=9 5.99e-07 m=10 8.75e-08 -> first m<1e-6: 9
0.118          p=1 b=0.27508 rho=0.14025  ... -> first m<1e-6: 8
0.118          p=2 b=0.27508 rho=0.14025  |c_m/c_0|: m=6 1.03e-04 m=7 1.65e-05 m=8 2.60e-06 m=9 4.05e-07 m=10 6.25e-08 -> first m<1e-6: 9
0.118          p=3 b=0.27508 rho=0.14025  |c_m/c_0|: m=6 3.86e-04 m=7 6.95e-05 m=8 1.22e-05 m=9 2.08e-06 m=10 3.50e-07 -> first m<1e-6: 10
→ "Fourier M = 8–10" reproduces for p = 2–3 across both fork ends.
=== (2) half-range Gauss-Legendre in theta, K nodes per v_x half, full-range moments ===
0.7*M_th_353K  p=2 K=10 rel err density/current/xx-flux/yy-flux: 1.50e-09 2.33e-08 3.93e-08 3.97e-08  max=3.97e-08
0.7*M_th_353K  p=3 K=10 rel err density/current/xx-flux/yy-flux: 7.34e-09 7.09e-08 1.51e-07 1.63e-07  max=1.63e-07
0.118          p=2 K=10 rel err density/current/xx-flux/yy-flux: 4.91e-09 5.83e-08 9.76e-08 9.91e-08  max=9.91e-08
0.118          p=3 K=10 rel err density/current/xx-flux/yy-flux: 2.44e-08 1.83e-07 3.83e-07 4.23e-07  max=4.23e-07
(K=8 worst 1.78e-05; K=12 worst 9.22e-09; K=14 worst 1.90e-10)
→ "K = 10 (≤ 3.8×10⁻⁷ on the density, current and momentum-flux moments)" reproduces: worst xx-momentum-flux 3.83e-7 (p = 3, 0.118). Note yy-flux is 4.23e-7, not quoted by the post.
=== (2b) naive GL in mu=cos(theta) with 1/sqrt(1-mu^2) Jacobian, K=10 ===
0.7*M_th_353K  p=2 K=10 mu-GL naive rel err: [0.04067866 0.07708311 0.07812485 0.00018415]
→ confirms the post's construction must be GL in θ per v_x half (a μ-basis would be 5 orders worse); the post does not say "in θ" explicitly.
=== (3) candidates for |z| ===
0.7*M_th_353K  q0           |beta|=0.1841 |z|=0.0915
0.7*M_th_353K  q-=q0/(1-M)  |beta|=0.2052 |z|=0.1019
0.118          q0           |beta|=0.1841 |z|=0.0915
0.118          q-=q0/(1-M)  |beta|=0.2087 |z|=0.1036
(Gamma only, q0: 0.1009; 1/tau_ee − iω, q0: 0.0986)
→ 0.092–0.104 reproduces as the streaming-resolvent harmonic ratio at Γ − iω from q0 to q₋(0.118); definition absent from the post.

[5] python3 contact.py
=== diffuse contact, C_acc=1: half-range (outgoing) moments by K-node GL ===
0.7*M_th_353K  p=2 K= 8 rel err n/flux/xx: 9.99e-11 4.71e-10 1.32e-09
0.7*M_th_353K  p=3 K= 8 rel err n/flux/xx: 4.27e-11 1.14e-09 9.38e-09
0.118          p=2 K= 8 rel err n/flux/xx: 8.77e-12 1.79e-10 1.97e-09
0.118          p=3 K= 8 rel err n/flux/xx: 6.79e-10 4.43e-09 2.05e-08
→ "K = 8 reaches ≤ 2.1×10⁻⁸" reproduces (worst 2.05e-8).
=== Fourier-truncated jumped distribution, outgoing flux ===
0.7*M_th_353K  p=2 M=100 outgoing flux rel err: 6.94e-08   (M=10 5.32e-05, M=50 5.39e-07, M=200 8.80e-09)
0.118          p=2 M=100 outgoing flux rel err: 8.31e-08
0.7*M_th_353K  p=3 M=100: 1.23e-07 ; 0.118 p=3 M=100: 1.50e-07
→ "Fourier M = 100 reaches 6.9–8.3×10⁻⁸" reproduces exactly for p = 2 (p = 3 would be 1.2–1.5e-7; the post's bulk K=10 figure used p = 3 while the contact Fourier figure uses p = 2 — inconsistent p across the two bullets, non-load-bearing).

[6] python3 jumpcheck.py (does the jump matter?)
wall=1 (continuous at grazing, kink only)     jump at cos=0: +0.0000  Fourier outgoing-flux rel err M=10/100/1000: 5.32e-05 6.94e-08 7.16e-11
wall=1.05 (true 5% value jump)                jump at cos=0: +0.0500  ... 5.32e-05 6.94e-08 7.16e-11
wall=density-matched (1-b^2)^-1               jump at cos=0: +0.0611  ... 5.32e-05 6.94e-08 7.16e-11
→ the outgoing-flux Fourier error is independent of the jump size (the flux window is zero on the incoming half; the step pairs to zero beyond m = 1); the ~1/M³ error is the window's grazing kink. Numbers stand; the Open sentence's "integrates a prescribed jump" overstates what the test probes.

[7] Format/other: wc -w post.md → 497; grep '^# ' → 0 H1; grep -i 'bit-equal|bit-identical|bit-for-bit|every day|daily|schedule' → no matches.
```

### Seat model note

This check seat executed on claude-fable-5-1 (Fable 5.1), as requested for the run; the drafter's post was checked blind (no shared context, own scripts written from the post's text; the drafter's scripts were not seen). All reproductions ran on Linux x86_64 / Python 3.11.15 / numpy 2.4.6 in a 4-core cloud container; the three results.json keys the post calls exact were measured exactly equal here (rel. dev. 0.0), and no "bit-equal" claim is made or needed. Timing figures are platform-dependent and were accepted within ±10 % (measured 1.21 / 4.50 / 24.46 s vs 1.17 / 4.45 / 24.5 s).

## Orchestrator edits before filing (session model `claude-fable-5-1`, disclosed)

Mechanical fixes taken from the check seat's minor findings; no claim moved:
- ``plasmon_speed`, `M_th_353K` and `speed_band_m_s` reproduce `results.json` exactly` → ``plasmon_speed_design_m_s`, `M_th_353K` and `speed_band_m_s` reproduce `results.json` exactly` — key name: the sentence lists results.json keys; `plasmon_speed` is the function, `plasmon_speed_design_m_s` the key (check seat, minor)
