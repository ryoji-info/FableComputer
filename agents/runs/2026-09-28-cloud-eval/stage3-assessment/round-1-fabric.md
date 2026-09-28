### 🧵 Fabric — **STORE** (required edits) — round 1, 2026-09-28

VOTE: store

REASONS: STORE WITH REQUIRED EDITS. This is not a clean pass and goes to rework. The reply delivers the record's first two-cell time-domain cascade, and every decisive row reproduced in my own instrument, written from the reply's stated coupling definition before I opened cascade_driver.py. The rows: the gate (8.287855791924049 / −11.828336851446547 / −11.775002445228234, ≤ 1.3×10⁻¹³ relative); the J = −1 chain at N = 240 and N = 480 (G4_A 1.581 → 1.503); the matched-amplitude Δ (+0.001 / +0.101); the J = −25 sweep row (G4_A 1.959, floor −3.72); the passive density transfer (15.83 / 16.23 dB); the relaunch attenuation (−24.60 / −25.04 dB); and the un-windowed residue (−5.698 dB over the stated denominator). Substance and durability therefore hold: 08-01 §4's stated premise is confirmed at matched amplitude to within 0.6 dB (signed negative); under the session's density coupling G4 falls short of Table 7's bar at 0 / −1 / −3 dB; and the stage-2 floor fails both spec readings everywhere. Labels, citations and honesty hold only after edits. The coupling the session built is called "the released coupling" / "the released model's own physics" in six places, including the title and the bench discriminant. The priced "alternative plane" is not independent: the drain velocity is −M × the drain density at the current-clamped drain, so the plane gap is 18.4 dB, not 44, and its passive "−28 dB transfer" is an O(Δx) residue. Table 1's m = 30 "seed spread" is the ⅛-rt window-rounding knife-edge, whose measured −6 dB sensitivity (0.033 in G4) is larger than the −6 dB class's 1.7× margins at N = 480/720. Also: 08-01 §4's operating point is mis-cited; 07-22 / 08-12 are not credited for the ring-down mechanism; 07-20 L4, 07-21 L3 and 08-13 go unaddressed; and the two-sided bench discriminant leaves its lower side unassigned and does not pin the launch amplitude that Table 4 shows decides G4. None of these moves a measured number, and every one can be fixed without a new campaign.

REQUIRED EDITS:
- R1 (labels: the scope of the coupling). Replace 'the released coupling', 'the released model's own density coupling', 'the released cascade' and 'the released model's own physics' with 'the session's in-model density-plane coupling (unidirectional, ideal isolation)'. The occurrences are: title; executive items 5 and 6; the grading rows for G4 and for cascade_per_cell_dB; §5's bench discriminant ('discriminates against the released coupling's plane or scale'; 'the released model predicts'). The released chain has no inter-cell coupling, as item 6 itself says ('the released solver has no such link'). Scope the 'contradicted' grades for G4 '≈ 2×' and for Part I's cascadability row to that construction.
- R2 (item 8, limitation 2: the alternative plane). (i) Label the passive 'port-to-port velocity transfer −28 dB (N = 240) / −34 dB (N = 480)' as an O(Δx) numerical residue that vanishes in the continuum. My passive mean-'1' drain velocity is 8.085e-05 at N = 240 and 4.238e-05 at N = 480, a ratio of 1.91 per doubling; the continuum passive drain is an exact velocity node. (ii) Correct 'worth 44 dB of drive' and '44 dB apart'. What cell 2 actually receives at J = −1 is 0.03027 (density plane) against 0.00362 (velocity plane), a gap of 18.44 dB, which is about 20·log10(1/M) = 18.54 dB. At the current-clamped drain u − u0 ≈ −M(h − 1): my least-squares slope is −0.11797 against −M = −0.11826, with 7 % residual. The drain-velocity plane is therefore the density plane scaled by −M, and the priced 'plane' sensitivity is a scale sensitivity that Table 4 already spans. (iii) Strike or correct 'exactly the plane fork 08-02 named'. 08-02 §3.1's fork is source-plane velocity (cav_u) against drain-plane density, not drain velocity. (iv) Report G4_A in that plane (I measured 4.976 at N = 240, shift 2.625 rt) or state that definition A is ill-conditioned there, because its passive twin is the vanishing residue. The rework may either price a genuinely independent alternative, or state the resulting defence of the density plane: a current-clamped drain offers one independent AC observable.
- R3 (numbers and honesty: seed spread versus window rounding). Item 1's 'seed spread ≤ 0.04; 0.033 at −6 dB', Table 1's m = 30 [min, max] envelopes, and the key cascade2_G4_worst1_ratio_J1's 'Seed envelope at N = 240: 1.569–1.581' are the ⅛-rt window-rounding knife-edge, not pattern dependence. At a fixed shift, seeds 7 and 13 give identical chains: J = −1, 13.000 / 13.000 dB at 2.5 rt and 13.103 / 13.103 at 2.625 rt; J = −6, 14.555 / 14.554 and 14.826 / 14.826. Seed 13's passive lag (2.508 rt) rounds to 2.5 and seed 7's (2.568 rt) to 2.625. Relabel the spread as window-rule spread; the seed spread at a fixed window is ≤ 0.001 in G4. Restate limitation 6's rule sensitivity (≈ 0.1 dB / 0.012 in G4) to include the −6 dB class's measured 0.271 dB / 0.033 in G4. State that the −6 dB margins over 1.7× at N = 480/720 (0.032 / 0.011) lie inside that sensitivity, or show that they survive it. Until then, item 1's 'met at −6 dB' at those grids is window-rule-dependent.
- R4 (the 08-01 §4 grade, a mis-citation). Strike 'Against the ledger's own operating point (2×10⁻³, G_worst1 = 8.13–8.53 dB)' in item 3 and in the grading row. 08-01 §4's construction evaluates the measured G(A) at its fixed point A_fix (its §4 table, 0.0117–0.0140 on the analytic-bias leg), never at the 2×10⁻³ measurement drive. Its stated premise, G_c2c(A) = G_boundary(A), is confirmed at matched amplitude (Δ −0.60 … +0.00 dB worst-'1', Table 2a). Name what the density coupling actually contradicts: the ledger's link term. 08-01 §4 books −per_gate_loss = −2.555 dB, while the session's coupling measures a passive density transfer of +15.8 dB. Add, from Table 3, that no loaded attractor exists short of h − 1 ≈ 1.
- R5 (bench discriminant). (i) Pin the launch amplitude in bench-measurable terms, e.g. the model's 2×10⁻³ = 0.166 × the promoted gated streaming knee 0.01203 (knee_gated_duty0p8_streaming_m30_N240), and state the G4 prediction as a function of it. Table 4 shows G4 running from 1.53 to 1.96 with cell 2's input amplitude, so without the pin a G4 > 1.7 'pass' is also produced by a weaker launch, and the discriminant cannot discriminate. (ii) 'Two-sided' is asserted, but only G4 > 1.7 and floor < −8 dB are assigned. Assign the lower sides (G4 < 1.40; floor shallower than −3 dB) and the gaps (1.65–1.70; −6 to −8 dB), or relabel it as two one-sided discriminants.
- R6 (prior art and citations, standing rule 10). (i) Credit notes/2026-07-22-cavity-ringdown-isi.md (ring-down is the binding ISI memory) and notes/2026-08-12-gated-zero-residual-phasor.md (run-length 1 binds; −24.4 dB/slot decay) where item 4 uses '≈ 24 dB/slot ring-down' and the one-slot-memory mechanism. The un-windowed −5.70 dB value is new; the mechanism is the record's. (ii) Cite every promoted note by filename. The reply cites none by filename, and 'the 08-01' refers to three different notes. (iii) State whether 07-20 Limitation 4 and 07-21 Limitation 3, which the prompt named, are discharged. They are not: F = 1, no splitter, ideal isolation, no disorder. (iv) Cite notes/2026-08-13-walk-excess-clamp-placement.md in limitation 4 as the known first-order ghost-centre clamp-placement term acting on both coupled clamps. The prompt required it to be kept in view, and the reply never mentions it.
- R7 (item 7, Table 6, cascade_stage_latency_rt). Strike 'plus the LF half-step'. At N = 240 the LF half-step is 3.47×10⁻⁴ rt, while the measured passive peak-time lag 0.5243 rt exceeds the L/s = 0.5 rt transit by 0.0243 rt, about 70 half-steps. Label the excess unexplained, or measure its origin.
- R8 (grading row for Part I's cascadability). Grade the row's 'in-model yes' and its per-cell figure separately, under R1's scope. The two-cell chain still delivers +12.5–14.8 dB over the passive chain, but the stage-2 floor fails both spec readings. The '+8.4–9.3 dB/cell' is contradicted for cell 2 (4.0–6.4 dB). The current single 'contradicted' rests only on the gain numbers.

TOP ISSUES:
- Mislabelled scope. The session built the coupling itself (drain density → next source clamp, κ = 10^(J/20), ideal isolation), yet the reply calls it 'the released coupling' / 'the released model's own physics' in the title, items 5–6, two grading rows and the bench discriminant. Grades that depend on this construction ('G4 ≈ 2× contradicted'; 'the printed gate cannot be met by the released model's own physics') are stated without its scope.
- The 'alternative plane' is not independent. Measured at m = 30 / N = 240 / seed 7, the active drain velocity is u − u0 ≈ −M(h − 1) (LS slope −0.11797 vs −M = −0.11826, residual 7 %). Cell 2 receives 0.03027 (density) vs 0.00362 (velocity), 18.44 dB apart, not '44 dB of drive'. The −28 dB passive velocity transfer is an O(Δx) residue: 8.085e-05 → 4.238e-05 from N = 240 to 480. Definition-A G4 in that plane measures 4.976 and the reply does not print it. The claim that this is 'exactly the plane fork 08-02 named' is a mis-citation, since 08-02's fork is source-plane velocity vs drain-plane density.
- Table 1's m = 30 'seed spread' is window rounding. At a fixed shift seeds 7 and 13 give identical chains (J = −1: 13.000 / 13.000 at 2.5 rt, 13.103 / 13.103 at 2.625 rt; J = −6: 14.555 / 14.554, 14.826 / 14.826). The spread arises because seed 13's lag (2.508 rt) rounds to 2.5 and seed 7's (2.568) to 2.625. The rule's measured sensitivity at −6 dB (0.271 dB, 0.033 in G4) is about 3× limitation 6's stated 0.012, and it exceeds the −6 dB class's 1.7× margins at N = 480/720 (0.032 / 0.011).
- 08-01 §4 is mis-cited. The reply's 'ledger's own operating point (2×10⁻³, G_worst1 = 8.13–8.53 dB)' is the promoted keys' measurement drive, not the ledger's operating point; 08-01 §4 evaluates G(A) at A_fix, analytic-bias leg. Its stated premise is confirmed at matched amplitude (my Δ at the rule shift: +0.001 worst / +0.101 mean). What the coupling contradicts is the link term: −2.555 dB booked vs +15.83 dB measured passive density transfer.
- The bench discriminant is incompletely specified. No launch-amplitude pin, although G4 runs from 1.53 to 1.96 with cell 2's input (Table 4; my J = −25 row gives 1.959). The label is two-sided, but no reading below the G4 band or above the floor band is assigned.
- Prior art and citations. The ring-down one-slot-memory mechanism of item 4 is not credited to 07-22-cavity-ringdown-isi or 08-12 (−24.4 dB/slot). No promoted note is cited by filename. 07-20 L4 and 07-21 L3, both named in the prompt, and 08-13's clamp-placement error, which the prompt said to keep in view, go unaddressed.
- Item 7's latency explanation is wrong by about 70×. The excess 0.0243 rt over the L/s = 0.5 rt transit is attributed to 'the LF half-step', which is 3.47×10⁻⁴ rt at N = 240.
- Optional, not required. The Table 2a Δ sign at J = 0…−3 dB depends on window placement: my J = −1 row gives Δ worst +0.001 at 2.625 rt, −0.093 at the exact 2.568 rt and −0.148 unshifted. The ≤ 0.6 dB verdict is robust. The solver-side falsifier ('same-convention rerun outside the band') is generic on a deterministic chain; a non-vacuous one would help.

SEAT MODEL NOTE: This seat (assess-fabric) was requested on claude-opus-5-5 by the maintainer for this run, as the 2026-08-13 policy's Opus assessor seat. It is not Fable 5 and does not claim to be. The reply it assessed was executed on claude-fable-5-1. Every number in this record was produced on Linux x86_64 / Python 3.11.15 / numpy 2.4.6, and reproductions of promoted values are stated as relative deviations, not exact equality.

<details><summary>Re-execution log (verbatim)</summary>

```text
Seat directory: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/assess-fabric/. Files: fab.py (own instrument), phase1-4.py, score1-3.py, and 25 .npz series. Released fable-model-chain/ was imported unedited with PYTHONDONTWRITEBYTECODE=1; run_all.py was never run. `git status --short` was empty at the end.

fab.py was written from the reply's §1–§2 definitions before cascade_driver.py was opened:
- 07-31 make_sig_duty, verbatim logic.
- run_cell replicates solver.run stepping (t += dt, the released dt rule, the blow-up guard).
- Cell 2's clamp is h_left = 1 + κ·x1(t_k), with x1 = h1[−1] − 1 or u1[−1] − u0, np.interp on cell 1's released-labelled series (exact when dt is equal).
- cav = max|u − u0|; drn_h = |h[−1] − 1|; slot-mode = carrier lock-in amplitude over the (shifted) window.
- Envelope lag = argmax of the cross-correlation of one-carrier-period moving-mean |drn_h| envelopes, about 20k samples, search ≤ 6 rt; a Hilbert variant was also run.

$ python3 -c "import sys,numpy,platform;print(...)"
3.11.15 2.4.6 Linux x86_64   (nproc 4)

$ python3 phase1.py
M_th_num(240) = 0.16894319463373797 shipped 0.16894319463373791 rel dev 3.285787944971905e-16 [35s]
bias = 0.11826023624361658
done ('c1_0_m30N240s7', 1728000, 1728000, 0.001388888888888889, 78.4)
done ('c1_M_m30N240s7', 1898294, 1898294, 0.0012642926038760258, 82.3)
done ('c1_0_m30N480s7', 3456000, 3456000, 0.0006944444444444445, 143.7)

$ python3 score1.py
GATE cav: Gw 8.287855791924049, Gm 8.410165254217045, mean1 0.03267155023359718, pp 0.30577762777571854, eye 11.705114659586407, floor -11.828336851446547
GATE drn_h: Gw 8.663537342727865, Gm 8.769558457037114, mean1 0.03396500068703142, pp 0.2653510968361314, eye 11.668429556367615, floor -11.775002445228234
rel dev: G 3.86e-15 floor cav 5.68e-14 floor drn_h 1.32e-13   [targets 8.287855791924017 / -11.828336851447219 / -11.775002445226676 -> gate passed on a relative tolerance; exact equality not claimed]
cell-1 slot-mode drn_h floor: -15.664876659072402  peak-mode gap: 3.889874213844168   [08-12: 3.89]
passive cell-1 mean-'1' windowed |drn_h| = 0.012374008905000889 -> passive port density transfer 15.8296085712346 dB
active cell-1 mean-'1' |drn_h| = 0.03396500068703142 -> 24.600032640950246 dB over launch; relaunch junction -24.600032640950246
drain velocity mean-'1': active 0.004065219510236737 (6.16 dB over launch)  passive 8.08452818019026e-05 (-27.87 dB over launch)
active drain velocity / density (mean-1) = 0.11968848602994218  vs M = 0.11826023624361658 ; ratio of what cell 2 receives, density vs velocity plane: 18.44 dB
LS fit du = c*dh: c = -0.1179728973101061  (-M = -0.11826023624361658 ) residual rms / du rms = 0.07379744924064732
n after-1 zeros 8 ; mean-1 windowed 0.03396500068703142  mean-1 first-quarter 0.02112298068773024
after-1 '0': window -11.775 dB; first-quarter over (a) -5.698 dB, over (b) -1.573 dB; whole-slot over (a) -5.698 dB
position of whole-slot max (slot fraction): [0.009, 0.009, 0.0084, 0.0084, 0.0084, 0.0084, 0.0084, 0.009]
after-0 '0': window -36.31, first-quarter over (a) -30.07 dB
'0'-slot energy over mean '1'-slot energy: max -10.56 / median -13.83 dB

$ python3 -c (passive planes, N = 240 vs 480)
c1_0_m30N240s7 passive mean-1 drain density 0.012374 (15.83 dB over launch); drain velocity 8.085e-05 (-27.87 dB over launch)
c1_0_m30N480s7 passive mean-1 drain density 0.012962 (16.23 dB over launch); drain velocity 4.238e-05 (-33.48 dB over launch)

$ python3 phase2.py   (11 cell-2 / matched runs, Pool(4), 297 s)
cell-1 active mean-'1' windowed |drn_h| peak: 0.03396500068703142
A*(J=-1) = 0.030271338726030064

$ python3 score2.py J1
[J1] passive stage-1->2 envelope lag (rt): movmean 2.5681  hilbert@20k 2.5681  hilbert@200k 2.5389
[J1] active  stage-1->2 envelope lag (rt): movmean 5.7045  hilbert@20k 5.6451  hilbert@200k 5.6609
[J1] passive per-slot peak-time lag, '1' slots: median 0.5243 rt, min 0.5243, max 0.5243; dt = 1.389e-03 (half-step 3.47e-04 rt)
[J1] single cell (cav) G_worst 8.2879 mean 8.4102; drn_h G_worst 8.6635
[J1] shift 0.000 rt: chain/passive worst 12.734 mean 13.139 | G4_A 1.537 / 1.562 | G4_A(drn_h) 1.486 | G4_B 1.788 | c2c 4.649 / 5.003 | upstream-thru-passive 8.062 / 8.136 | floor cav -3.56 drn_h -3.09 mode -4.10 | pp 0.997 eye 3.15 | mean-1 drn_h 0.3166
[J1] shift 2.568 rt: chain/passive worst 13.000 mean 13.337 | G4_A 1.569 / 1.586 | G4_A(drn_h) 1.550 | G4_B 1.804 | c2c 4.704 / 4.968 | upstream-thru-passive 8.270 / 8.369 | floor cav -4.64 drn_h -4.31 mode -6.21 | pp 0.853 eye 4.29 | mean-1 drn_h 0.3310
[J1] shift 2.500 rt: chain/passive worst 13.000 mean 13.337 | G4_A 1.569 / 1.586 | ... floor cav -4.64 drn_h -4.31 mode -6.16 | pp 0.853 eye 4.29
[J1] shift 2.625 rt: chain/passive worst 13.103 mean 13.399 | G4_A 1.581 / 1.593 | G4_A(drn_h) 1.550 | G4_B 1.804 | c2c 4.799 / 5.030 | upstream-thru-passive 8.270 / 8.369 | floor cav -4.70 drn_h -4.31 mode -6.26 | pp 0.750 eye 4.40 | mean-1 drn_h 0.3310 | passive stage-2 transfer 14.82 dB (+1 dB kappa = 15.82)
[J1] shift 5.704 rt: chain/passive worst 13.110 mean 13.402 | floor cav -6.33 drn_h -6.10 mode -8.52 | eye 6.03
[vs reply: Table 1 13.103/1.581/1.593/1.550/1.804; Table 2a/4 c2c 4.798/5.030; Table 5 -4.70/-4.31/-6.26/0.750/+4.39; Table 3 stage 2 13.000/13.337, 4.704/4.969, -4.64/-4.31, -6.21, 0.853, +4.29, 0.3310; Table 3b 5.71: 13.110/-6.33/+6.03; Table 6 lags 2.568/0.525/5.704 -- all reproduce to the printed digits (±0.001 from the same-step vs previous-step coupling label)]

$ python3 -c (matched amplitude)
matched A*=0.030271 boundary-driven cav: G_worst 4.7973 mean 4.9294 floor -13.083 pp 0.3375
Delta vs c2c at 2.625 rt shift (4.799/5.030): worst +0.001 mean +0.101; at exact 2.568 (4.704/4.968): -0.093 / +0.039; unshifted (4.649/5.003): -0.148 / +0.073

$ python3 score2.py J25
[J25] passive env lag movmean 2.5681; active 5.9422
[J25] shift 0.000 rt: chain/passive worst 15.699 mean 15.841 | G4_A 1.894 / 1.884 | c2c 7.314 / 7.471 | floor cav -1.94 drn_h -1.91 mode -3.00 | eye 1.80
[J25] shift 2.568 rt: chain/passive worst 16.073 mean 16.412 | G4_A 1.939 / 1.951 | c2c 7.599 / 7.845 | floor cav -3.63 drn_h -4.01 mode -5.23 | eye 3.29
[J25] shift 2.625 rt: chain/passive worst 16.232 mean 16.503 | G4_A 1.959 / 1.962 | G4_A(drn_h) 1.917 | G4_B 0.952 | c2c 7.759 / 7.937 | upstream-thru-passive 8.473 / 8.567 | floor cav -3.72 drn_h -4.01 mode -5.27 | pp 0.674 eye 3.45 | mean-1 drn_h 0.0297
[vs reply Table 4/5 m30 J-25: 1.958/1.962; c2c 7.757/7.935; -3.72/-4.01/-5.27; pp 0.676; +3.44]

$ python3 score2.py U1   (velocity plane, J = -1)
[U1] passive per-slot peak-time lag median 2.0271 rt
[U1] shift 0.000 rt: chain/passive worst 40.846 mean 41.010 | G4_A 4.928 / 4.876 | c2c 7.327 / 7.447 | floor cav -1.93
[U1] shift 2.625 rt: chain/passive worst 41.242 mean 41.523 | G4_A 4.976 / 4.937 | G4_A(drn_h) 4.797 | G4_B 1.166 | c2c 7.554 / 7.742 | upstream-thru-passive 33.687 / 33.781 | floor cav -3.69 drn_h -3.78 mode -5.24 | pp 0.688 eye 3.41 | passive stage-2 transfer -28.96 dB
what cell 2 receives at J=-1: density plane 0.03027, velocity plane 0.00362 -> plane gap 18.44 dB (= 20log10(1/M) 18.54 dB)

$ python3 phase3.py   (seed 13 cell 1; J = -6 and J = -1 chains for seeds 7 and 13; 207 s)
$ python3 score3.py
seed 7 J=-1: G_single 8.2879; passive env lag 2.5681 rt -> rounds to 2.625 | shift 2.568: chain 13.000 G4_A 1.569 floor -4.64 | shift 2.500: chain 13.000 G4_A 1.569 floor -4.64 | shift 2.625: chain 13.103 G4_A 1.581 floor -4.70
seed 7 J=-6: G_single 8.2879; passive env lag 2.5681 rt -> rounds to 2.625 | shift 2.568: chain 14.639 G4_A 1.766 floor -4.00 | shift 2.500: chain 14.555 G4_A 1.756 floor -3.85 | shift 2.625: chain 14.826 G4_A 1.789 floor -4.10
seed 13 J=-1: G_single 8.2876; passive env lag 2.5083 rt -> rounds to 2.500 | shift 2.508: chain 13.000 G4_A 1.569 floor -4.65 | shift 2.500: chain 13.000 G4_A 1.569 floor -4.65 | shift 2.625: chain 13.103 G4_A 1.581 floor -4.71
seed 13 J=-6: G_single 8.2876; passive env lag 2.5083 rt -> rounds to 2.500 | shift 2.508: chain 14.554 G4_A 1.756 floor -3.88 | shift 2.500: chain 14.554 G4_A 1.756 floor -3.87 | shift 2.625: chain 14.826 G4_A 1.789 floor -4.11
[-> Table 1's m=30 N=240 '[min,max] over seeds' (J=-1 [1.569,1.581], J=-6 [1.756,1.789]) is the 1/8-rt rounding of each seed's own lag, not pattern dependence]

$ python3 phase4.py   (N = 480, m = 30, J = -1; 328 s)
M_th_num(480) = 0.1587475408418196 promoted 0.1587475408418196 exact: True [74s]
$ python3 -c (score N480)
N480 cell 1: G_worst 8.4681 floor -11.4628 (promoted 8.4681 / -11.4628)
N480 active mean-1 drn_h 0.03573 -> A*(J=-1) 0.03184; relaunch -25.04 dB
N480 passive env lag 2.6278 rt
shift 2.628 rt: chain worst 12.726 mean 12.952 G4_A 1.503 / 1.521 floor cav -4.70 drn_h -4.29 mode -6.04 eye 4.48
shift 2.625 rt: chain worst 12.726 mean 12.952 G4_A 1.503 / 1.521 floor cav -4.70 drn_h -4.29 mode -6.03 eye 4.48
shift 2.500 rt: chain worst 12.644 mean 12.903 G4_A 1.493 / 1.515 floor cav -4.66 drn_h -4.29 mode -5.94 eye 4.40
[vs reply Table 1 N480 m30 J-1: 12.726/1.503/1.521; Table 5: -4.70/-4.29/-6.03/+4.48; Table 6: 16.23 dB, 2.628 rt; item 5: -25.0]

$ grep -rl <each of the 9 registered key names> notes fable-model-chain fable-model-quantum papers -> 0 hits each (no collisions).

Text audits:
- Part I was extracted with pymupdf; §7.4, Table 6, Table 7 G4, the passive-twins sentence and §9.4 are quoted correctly.
- cell.py: cascade_per_cell_gain_dB uses swing = A_op·10^(J/20), with A_op a 'drive-plane amplitude'.
- 08-01 gated §4: the fixed point is at A_fix on the 0.7·M_th_analytic leg.
- 08-02 §3.1: the plane fork is cav_u (source velocity) vs drn_h (drain density).
- 07-22-cavity-ringdown header: Windows/CPython.
- 07-20 L4: the loaded multi-cell transient with a real splitter is the WP1 check.
- stage1 quanta.md: |r|² ≤ 11.6 %.

Not re-executed (budget): m = 28 rows, N = 720 rows, seed 11, J = 0/−3/−10/−15/−20, Table 2b, Table 3 stages 3–5, and M_th_num(720). I accept no number from these; my findings do not rest on them. The 08-13 mirrored N = 240 cfl = 0.8 falsifier was not run, because the reply does not bear on it.
```

</details>
