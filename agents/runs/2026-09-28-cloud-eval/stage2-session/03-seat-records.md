# Stage 2 — seat records (prior-art checks and premise audits), 2026-09-28

## Candidate seat 🧵 Fabric (`claude-opus-5-5`)

Seat model note: Drafted by the Fabric 🧵 candidate seat on claude-opus-5-5 (the maintainer's requested Opus seat for this run under the 2026-08-13 policy), not Fable 5. The seat's scratch feasibility probe imported the released fable-model-chain unedited (solver._setup/_step_LF in lockstep) on Linux x86_64, Python 3.11.15, numpy 2.4.6. The probe ran from /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/fabric-s2/proto.py and proto2.py. No tracked file was modified; run_all.py was not run.

Prior-art check:

Grepped all of notes/ (bodies, appended vote records, INDEX.md) for: "G4", "two-cell time-domain", "time-domain test", "1.7×", "multi-cell", "two-cell", "cell-to-cell", "upstream cell", "downstream cell", "second cell", "drain output", "cascade", "restor", "port-to-port", "passive transfer", "passive reference", "impedance", "resync"/"re-sync", and the key `cascade_per_cell` / `cascade_per_cell_dB`.
- "G4": zero hits in any note. The G1 note (08-01-bench-gate-g1-reissued §4 item 4) states G2–G5 are out of scope and leaves checking G3–G5 as a follow-up.
- "cell-to-cell": the only hit is 08-01-gated-requirement-round-trip §4's listing of the untested assumption: "No multi-cell cascade was run in this session." 08-02-zero-floor-spec-dissolved lists "any two-cell cascade" among the things it did not run.
- 07-20 Limitation 4 and 07-21 Limitation 3 name the loaded-cascade transient as an unrun WP1 check.
- `cascade_per_cell_dB` appears only as a reproduced analytic anchor (07-20, 07-21, 08-01); no note audits it in the time domain.
- The "two-cell" hit in 08-02 is the static map composition T∘T (the logic-map period-2 orbit), not a time-domain run.
- No note measures the passive port-to-port transfer in a cascade context. The 07-10/07-11/07-12 hits concern the passive reference's resonance and boundary factor.
- Code check: results.json (both chains) holds no g4/two_cell/cascade2 key. `solver.run` offers no cascade drive; the released chain has no multi-cell time-domain routine.
- Manuscript: Part I (docx text) §7.4 says "The direct two-cell time-domain test is open work, tracked in the project roadmap"; Table 7's G4 row gives the model target "≈ 2×".
Not a re-run of discussion #124: that session asked whether two DS segments sharing one channel through a partial clamp go unstable below the single-cell threshold (a bidirectional supermode/threshold question). This prompt is about feed-forward signal transfer, gain and floor at the sub-threshold gated operating point, with unidirectional coupling. It explicitly excludes back-action/stability and forbids citing #124 as settled.
Scratch feasibility probe (seat-only, not record, not cited as evidence in the prompt): a 3-cell lockstep cascade at N = 240, m = 30 ran in about 45 s per chain on Linux x86_64 / Python 3.11.15 / numpy 2.4.6. It showed three things: the passive cell's drain-density/source-density transfer is about 15.8 dB (not unity), per-stage latency shifts the best decision window by about 0.2 slot per cell, and the chain-ratio G4 at N = 240 lies between 1.7× and 1.94× depending on coupling loss and window. So the question is open and sensitive exactly to the conventions the prompt forces the executor to defend.

## Candidate seat 🌊 Kinetic (`claude-opus-5-5`)

Seat model note: This Kinetic candidate seat ran on claude-opus-5-5 (Opus 5.5), which the maintainer requested for this run under the 2026-08-13 policy's Opus seat. It is not Fable 5. Platform: Linux x86_64, Python 3.11.15, numpy 2.4.6 (cloud container). The anchor check imported the released fable-model-chain unedited. Its script is at /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/kinetic-s2/anchors.py, and the draft prompt is prompt.txt in the same folder. No tracked file was modified and run_all.py was not run.

Prior-art check:

What I searched in notes/*.md (all notes, their appended vote records, INDEX.md): 'half-range|exponent_p|Knudsen exponent|Knudsen layer|C_acc'; 'transparent|zero.flux|J(0)|Sharvin|electrostatic.*pin|AC short|reservoir'; 'Padé|zero sound|first sound|continued fraction|closure error|resonance_shift|compressib|stress-relaxation|angular harmonic'; 'Callaway|periodic|Boltzmann|WP2'. I also extracted every existing `boundary*`/`source*`/`contact*` key name, and grepped ROADMAP.md, papers/REVISION-HISTORY.md and fable-model-chain/*.py for the clamp definitions.

What the record holds:
- The exponent p appears only in 07-18 contact-gated (two scaling laws, source sign fixed, keys `boundary_loss_pct_per_roundtrip_specular` 0.0 [0, 0.5] % and `_diffuse` 6.2 [3, 25] %) and 07-20 (p = 1 + power(ζ″), `boundary_source_Kn_exponent_p` = open ∈ {1, 2}).
- 07-20's adoptable half-range solve was never run by any later note. INDEX lists 07-20 as "stands — open by construction"; no later note or annotation touches it.
- Part I v5.6 revision notes and ROADMAP carry the exponent as open.
- No note flags that the family's C_acc = 0 "specular/transparent" endpoint is a J_x = 0 (current-clamp) wall. The only hits for "transparent" are 07-18's own table and key.
- The bulk closure's Padé error (07-13 Limitation 2) has never been computed. It enters only as a solver validation gate, not as the question.
- The only related lab material is today's unpromoted Kinetic post, which is a basis decision (half-range nodes) and explicitly says it did not solve a Knudsen layer.

Why the question is not already answered: nothing in notes/ computes 1−|r_s|² from a kinetic boundary problem.

Discussion #124: its question (two-segment supermode, coupling lowers threshold) is a bulk/cavity-operator question on the hydro tier. This candidate does not touch it and tells the executor not to revisit it.

Anchors re-executed on Linux x86_64 / Python 3.11.15 / numpy 2.4.6, released chain unedited (scratch/seats/kinetic-s2/anchors.py). All matched: s/v_F 2.3312, M_th 0.147083, M 0.102958, Kn₋ 0.2493, Kn₊ 0.2028, ℓ_ee 82.99 nm, ωτ_ee(353) 0.5214, tracked −0.28367 dB/1 %, edges −1.665 and −5.734 dB. CW gain matched results.json with relative deviation 0.0.

## Candidate seat ⚛️ Quanta (`claude-opus-5-5`)

Seat model note: This candidate seat ran on claude-opus-5-5 (Opus 5.5), not Fable 5, as the maintainer requested for this run under the 2026-08-13 policy's Opus seat. Platform: Linux x86_64, Python 3.11.15, numpy 2.4.6, cloud container. I imported the released chains unedited and did not run run_all.py. Scratch lives only under the scratchpad at seats/quanta-s2/: feas.py, plus p2.txt, a pypdf text extract of Part II.

Prior-art check:

I grepped every note in notes/ (appended vote records included), INDEX.md, CITATIONS.md, ROADMAP.md, papers/ERRATA.md and papers/REVISION-HISTORY.md. Search terms: c_K, C_KERR, kerr, Kerr, chi_over_kappa, blockade, Duffing, self-phase, "frequency shift", "amplitude-dependent", Lindstedt, multiple-scale, "third harmonic", 3f0, commensurate, shock, steepen. Symbols checked: qmode.kerr_chi, qmode.C_KERR_BAND, EPS_RAIL.

- The record carries c_K only as the open band: 07-13 §3 table "c_K ∈ 0.05–1 open", 07-13 §4, 08-05 §4 and its Limitation 5, and Part II v1.5 items 2–3 in REVISION-HISTORY.
- No note derives or measures an amplitude-dependent frequency from the chain solver. 08-13 mentions "nonlinear line pulling, drive-dependent shifts" only as a failure mode its linear prediction survived at drive 2e-3. Its "third harmonic" hit is a linear-operator mode (f_d3), not a nonlinear coupling.
- No results.json key or promoted key carries a Kerr name. Existing names I must avoid: chi_over_2pi_MHz, chi_over_kappa_300K/4K, blockade_cell_nm, cross_kerr_*.
- Discussion #124 (unpromoted, closed at cap) is the two-segment supermode/threshold question and is unrelated. The prompt names it out of scope.
- Today's three posts cover the energy-per-add slot, WP2 angular basis, and junction flip thresholds, none of which touches c_K.

Load-bearing numbers in the prompt were executed here with the released qmode:
- N_rail·χ/κ(c_K=1) = 0.1256637 (4 K) / 0.0628319 (300 K), giving flips at c_K = 7.958 / 15.915.
- Blockade c_K = 30498.85 (4 K).
- χ/2π at c_K = 0.05/0.25/1 = 0.1305/0.6523/2.609 MHz, which matches QG5's 0.13–2.6 MHz.

The pre-check ring-down (scratch seats/quanta-s2/feas.py, released solver._step_LF unedited, M=0, N=240, Linux x86_64 / Python 3.11.15 / numpy 2.4.6) gave δf/f = 1.040e-4 / 2.911e-4 / 7.210e-4 at ε = 0.01 / 0.03 / 0.1. It is disclosed in the prompt as a drafting-seat observation, not a result. git status of the checkout is clean; no tracked file was modified.

## Vote seat 🧵 Fabric (`claude-opus-5-5`) — voted kinetic

Seat model note: This vote seat ran on claude-opus-5-5 (the 2026-08-13 policy's Opus seat, requested by the maintainer for this run). It is not Fable 5. It persona-played Fabric 🧵 and did not vote for its own candidate. Platform: Linux x86_64 (6.18.44), Python 3.11.15, numpy 2.4.6. Anchor spot-checks were executed by importing the released, unedited fable-model-chain (kinetic.omega_tau_ee, results.json keys). No tracked file was modified, and run_all.py was not run.

Premise audit:

FABRIC (own candidate, ineligible; audited for completeness). No premise rests on a correction; it cites and builds on the corrections.
- It quotes 08-01 gated-requirement-round-trip §4's untested cell-to-cell assumption. The INDEX row for 08-01 confirms the note exists and is current.
- It takes 07-20 Limitation 4 and 07-21 Limitation 3 as the WP1 loaded-cascade check.
- It treats A_op as retired per 08-01-bench-gate-g1-reissued (INDEX: "G1b … retire A_op"; 07-17's row flags A_op as load-bearing).
- It keeps f_max_F2_gated_GHz = 69 [63, 74] as 07-31 set it, left unmoved by 08-01 ratio-bias and 08-02.
- It uses the retired 4-ps slot only as retired (07-23).
- results.json cascade_per_cell_dB = {0: 8.4016, −1: 8.6325, −3: 8.9843, −6: 9.3087}, verified by execution. This matches its "+8.4–9.3 dB/cell" reading.
- It excludes #124 (unidirectional coupling; back-action and stability out of scope).

KINETIC. Clean; no corrected premise, no re-run.
- Its core premise is posed as a question to test, not assumed. 07-18 (line 71: "Source, specular/transparent (C_acc → 0)"; line 116: the specular key) and 07-20 §2.3 (f_in = (1−C_acc)f_specular + C_acc·f_wall with δn(0) = 0 as a moment constraint) conflate specular and transparent. Meanwhile solver.py:14 defines the source as density-clamped, h = 1 (AC short), and the drain as current-clamped (solver.py:51). No later note addresses this; the INDEX lists 07-20 as "stands — open by construction".
- 07-20's adoptable item (a σ_c-swept half-range solve at Kn = 0.249) has never been run, so this is not a re-run.
- It uses the 07-18 seam correctly: it cites the key's band [0, 0.5] %, not the stale "C_acc ≲ 0.1" mapping.
- Anchors verified by execution on Linux x86_64 / Python 3.11.15 / numpy 2.4.6: kinetic.omega_tau_ee(353) = 0.52142; 0.7·M_th_353K = 0.1029583.
- The 07-13 §3.2 bulk gate figures are in the note (5.93e10 s⁻¹, line 65, whose record flags 5.9248e10 as a rounding slip, within the ±25 % allowance; −1.8 %, line 73). The 07-13 §6 ranking puts contact fidelity first (line 115).
- It reports the bias fork both ways per 08-01 ratio-bias, and excludes #124 explicitly.

QUANTA. Clean.
- It cites the corrections it rests on: 07-17 (the knee is at the launch plane; the rail is at neither plane) and 08-02 (cav is a source-plane velocity, not a density swing).
- c_K is open in 07-13 knee-rail (line 66: "c_K ∈ 0.05–1 open"). 08-05 Limitation 5 (line 152) names it as a single point of failure with three orders less margin.
- Part II's docx carries Q3 "c_K = O(1) band 0.05–1 (0.25 carried)" and the QG5 window "0.13–2.6 MHz"; both confirmed.
- 08-13 line 78 gives f_d3 = 0.736651425, and line 80 names nonlinear line pulling only as a failure route. No note has calibrated c_K.
- Minor omission, not a corrected premise: 08-12 Limitation 1 already prices a drive sensitivity on the walk (1.03 °/slot over drive 1–4×10⁻³, gated, at operating bias). The session should cite it as a related amplitude-dependent phase measurement.
- It excludes #124.

## Vote seat 🌊 Kinetic (`claude-opus-5-5`) — voted fabric

Seat model note: This vote seat ran on claude-opus-5-5 (Opus 5.5), as the maintainer requested for this run's Opus seat under the 2026-08-13 policy. It is not Claude Fable 5. The platform, per the run context, is Linux x86_64 / Python 3.11.15 / numpy 2.4.6. The audit is by reading only: the checkout's notes, notes/INDEX.md, the three 2026-09-28 posts, fable-model-chain/cell.py, run_all.py and the Part I .docx text. No solver was executed, so no reproduction or bit-equality is claimed. No tracked file was modified, and nothing was written to scratch.

Premise audit:

FABRIC (eligible, premises clean). Each premise below was checked against the file named.
(1) Untested assumption: notes/2026-08-01-gated-requirement-round-trip.md line 91 lists as load-bearing "that the source-boundary-driven single-cell G_worst1(A) … equals the cell-to-cell gain of a real cascade … No multi-cell cascade was run". Limitation 1 (line 150) repeats "No two-cell cascade was run". Base 6.515399158503943 dB confirmed at line 29 and in the Fabric/Quanta store records.
(2) Same gap named as the WP1 check in notes/2026-07-20-loaded-fanout-fixed-point.md §6 Limitation 4 (line 119: "No loaded-cascade time-domain simulation was run") and in notes/2026-07-21-composed-regeneration-envelope.md Limitation 3 (line 162).
(3) Part I (read from the .docx): "The direct two-cell time-domain test is open work". Its cascadability row reads "in-model yes: 2 cells, +8.4–9.3 dB/cell through −6 dB junctions". Table 7's G4 row is "two cascaded cells, one junction | ≥ 1.7× … | ≈ 2×". G4 is called "the single most informative outcome". All verbatim as the candidate states.
(4) `cascade_per_cell_gain_dB(junctions_dB=(0,-1,-3,-6), A_op=0.0116)` is at fable-model-chain/cell.py:43. It feeds results.json `cascade_per_cell_dB` via run_all.py:57/87. `A_op` is marked as the ledger's single free parameter and recommended for retirement in 08-01 and notes/2026-08-01-bench-gate-g1-reissued.md. That note's §4 item 4 (line 60) leaves G2–G5 unchecked, as claimed.
(5) Gate row: 8.287855791924017 dB (m = 30, N = 240, ratio bias) appears in notes/2026-08-12-gated-zero-residual-phasor.md line 30 (gate 2) and the 08-01 ratio-bias store record.
(6) Corrections it respects:
- 4-ps slot retired (07-23);
- `f_max_F2_gated_GHz` = 69 [63, 74], unmoved by 08-01 ratio-bias and 08-02;
- floor-plane mislabel and the imported spec (08-02);
- ghost-centre clamp placement (08-13);
- junction classes treated as a budget, not a derivation;
- 07-20 §3's superseded "ISI negligible" is not relied on.
(7) #124: coupling is unidirectional, and back-action and supermode stability are declared out of scope, so #124 is not re-run or cited as settled. The seat scratch probe is disclosed as "not evidence".
No premise rests on a corrected claim, and nothing already in the record is re-run.

QUANTA (eligible, premises clean, lower leverage).
(1) c_K is uncalibrated in the record: notes/2026-07-13-knee-rail-not-derivable-from-noise-chain.md line 66 has "c_K ∈ 0.05–1 open (order-of-magnitude band)", and a store record notes 4.5–5.8 orders. notes/2026-08-05-idler-added-noise-and-the-nf4db-requirement.md Limitation 5 (line 152) names c_K as a shared single point of failure with three orders less margin. Only 07-12-crossover, 07-13-knee-rail and 08-05 mention Kerr/c_K, and none calibrates it.
(2) Plane discipline is inherited correctly: 07-17 (knee at the launch/drive plane, rail at neither plane) and 08-02 (`cav` is a source-plane velocity).
(3) f_d3 = 0.736651425 is verbatim in notes/2026-08-13-walk-excess-clamp-placement.md line 78. 08-13 flags the mode-3 driven discriminant as leakage-confounded, which is relevant to Quanta's 3f-channel estimator risk.
(4) The O(ε) pre-check is disclosed as not a result. The bias fork is fenced off, and #124 is excluded.
Nothing corrected is relied on. The weakness is leverage, not premise. The no-go needs c_K ≈ 3.05×10⁴, so it is not at stake. Only QG5's window and 08-05 §4 can move, and the shallow-water value is explicitly not the Boltzmann–Maxwell c_K that Part II §8 assigns ownership of.

KINETIC (own candidate; ineligible by rule, audited for completeness). Its premises are real:
- 07-18 line 71 has "Source, specular/transparent (C_acc → 0)";
- 07-20 §2.3 (line 35) poses half-range accommodation;
- 07-20's adoptable item (line 154) is the never-run σ_c-swept half-range solve at Kn = 0.249;
- 07-13 §3.2 gives γ₀ = 5.93×10¹⁰ s⁻¹ (a store record notes it computes 5.92) and −1.8 %.
Its "specular ⇒ J_x(0) = 0" objection is posed as a hypothesis to test, not assumed. It does not depend on 07-18's unapplied seam (C_acc ≲ 0.02/0.08 rather than ≲ 0.1). It does not re-run #124.

## Vote seat ⚛️ Quanta (`claude-opus-5-5`) — voted fabric

Seat model note: This vote seat ran on claude-opus-5-5 (the Opus 5.5 seat under the 2026-08-13 mixed-model policy), not Fable 5. Platform: Linux x86_64, Python 3.11.15, numpy 2.4.6. I read only the checkout and extracted Part I's text into scratch. I executed no solver runs and modified no tracked file. The premise checks are grep and read checks against notes/, papers/Fable-Computer-Part-I.pdf and fable-model-chain/cell.py and solver.py.

Premise audit:

FABRIC: clean, and it builds explicitly on the corrections.
(1) It says 08-01 §4 lists "source-boundary-driven G_worst1 = cell-to-cell gain" as load-bearing with "No multi-cell cascade was run". Verified verbatim at notes/2026-08-01-gated-requirement-round-trip.md line 91, and again in §7 Limitation 1 (line 150: "No two-cell cascade was run ... open").
(2) Its 07-20 citation checks: notes/2026-07-20-loaded-fanout-fixed-point.md Limitation 4 (line 119) names a multi-cell loaded transient as the WP1 check. Its 07-21 citation holds only loosely: Limitation 3 of notes/2026-07-21-composed-regeneration-envelope.md is about the disorder-floor composition and calls "a loaded-cascade transient with real disorder" the check. That is the same transient but a different framing, and it is not load-bearing.
(3) Part I §7.4. The extracted Part I text reads "The direct two-cell time-domain test is open work". The cascadability row reads "in-model yes: 2 cells, +8.4–9.3 dB/cell through −6 dB junctions", and the two-cell figure is "computed as twice the per-cell figure". Table 7 G4 reads "≥ 1.7× the single-cell decibel". All verified in the PDF text.
(4) `cell.cascade_per_cell_gain_dB(junctions_dB=..., A_op=0.0116)` is verified at fable-model-chain/cell.py:43. `A_op` is the ledger's one free parameter per 08-01 (INDEX rows 07-17 and 07-23). notes/2026-08-01-bench-gate-g1-reissued.md §5 item 4 leaves G2–G5 unchecked (verified).
(5) Every binding premise is current per INDEX: the 07-31 frontier is confirmed and left unmoved by 08-01, ratio-bias and 08-02; 07-23 retired the 4-ps slot; 08-02 identifies drain-plane density as the cell-to-cell field; 08-02's restoring map is a family whose spec must be imported (the candidate forbids silent restoration); 08-12 and 08-13 cover the clamp placement.
(6) No promoted note has run a time-domain cascade. 08-02 §2.4's "two-cell composition" applies only to the static Eq. (5) map. So the candidate re-runs nothing.
(7) It excludes #124's question and does not cite it as settled. It carries the 07-31 §0.4 floor-spec fork both ways without settling it.

KINETIC: clean. It extends an open item and re-runs no settled question.
(1) The 07-20 §2.3 family f_in = (1−C_acc)f_specular + C_acc f_wall, with δn(0)=0 imposed as a moment constraint, is verified at notes/2026-07-20-source-contact-knudsen-exponent-open.md line 36. 07-20 "stands — open by construction" (INDEX), and its adoptable item, a σ_c-swept half-range solve at Kn=0.249, is unexecuted (line 154).
(2) 07-18 maps "Source, specular/transparent (C_acc → 0)" to zero loss (line 71; key at line 116). The INDEX 07-26 seam, which maps the specular band to C_acc ≲ 0.02/0.08, is not contradicted by the candidate. It quotes the key only as "0.0 [0, 0.5] %".
(3) The bulk gate uses the 07-13 §3.2 values γ₀ = 5.93e10 s⁻¹ and −1.8 %, verified at notes/2026-07-13-kinetic-correction-signed-band.md lines 65/73. That note's own assessor recorded γ₀ as computing to 5.9248e10, a trivial difference within the stated ±25 %.
(4) It discloses the open bias fork (08-01 ratio-bias) and scopes out #124.
Its central premise challenge, that specular means J_x(0)=0 (the drain clamp) while the source is a density/δφ node, is posed as a hypothesis to test, not assumed. No promoted note corrects it. Caveat on decision value, not a premise defect: 07-20 Limitation 4 says the exponent turns on "Ingredient X", a device-level contact property, so a kinetic solve may return a contact-dependent curve rather than close the gate.

QUANTA (own candidate, not eligible): premise-clean on audit. No promoted note calibrates c_K: 07-13 knee-rail line 66 still has "c_K ∈ 0.05–1 open", and 08-05 Limitation 5 (line 152) names it a single point of failure. It builds on 07-17's plane discipline, 08-02's velocity/density mislabel and 08-13's clamp offsets, and scopes out #124.
