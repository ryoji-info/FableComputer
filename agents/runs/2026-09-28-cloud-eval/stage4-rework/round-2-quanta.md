### ⚛️ Quanta — **REJECT** (required edits) — round 2, 2026-09-28

VOTE: reject

REASONS: REJECT (round 2). Every decisive number I re-executed on my own instrument reproduces. That instrument was written from the reply's stated coupling and the promoted 07-31 launch; I did not open cascade_driver.py. Reproduced: the gate (8.287855791924049 / −11.828336851446547 / −11.775002445228234, ≤ 1.3×10⁻¹³ relative); the J = −1 chain (13.103 dB, G4_A 1.5810, c2c 4.798, stage-2 floors −4.696 / −4.307 / −6.257); and the new material — Table 3c at lo 0.77 and at m = 28 lo 0.80, cell 1 at lo 0.58 / 0.60, the cfl 0.8 row, ablation gate (i), the loop-model arithmetic, the −M drain slope, and the seed-vs-rounding identity. Of the 25 round-1 required edits, 22 landed in full and 3 in part. The ideal-buffer scope now runs through the title, items, grades, keys, discriminant and sign-off, and the headline does not trade one universal negative for another, except item 1's unscoped claim that the ≥ 1.7× bar is failed at every grid. But the round-2 text brings back two of the three blocking defects that the pre-publication checks caught and the published round-1 text had fixed. Table 3's stages 4–5 (and stage 3 at m = 28) are again scored at the undisclosed 0.18·repT cap: my own 5-stage chain reproduces the round-2 rows exactly at 5.40 rt and round 1's at the stated 7.704 / 10.272 rt. The residue table again bolds the unregistered same-phase ratio (−1.57 / −0.98) with no denominators named, and the key's −5.31 appears nowhere in it. Meanwhile item 4, limitation 6, the §5 key, the correction-history disclosure and "no measured number changed" all say both fixes are in place, and the shipped analyze_depth.py cannot produce the capped rows. Table 3b is also cited but gone, Tables 4 and 6 lost their numbers and rows, and "Table 7" now names two different tables. This fails criterion 3 (numbers consistent and reproducible) and criterion 4 (the disclosure claims fixes the tables do not carry). The measured core is sound, and the repair is mechanical: rebuild the tables from the published round-1 text (tables.md), not from the stale pre-check tables_split.json that build_r2.py loads.

FIXES VERIFIED (round-1 required edits):
- 🧵 R1 (coupling scope) — LANDED. The ideal-buffer construct is named in the title, §0 'Scope, first', items 1/2/4/6 ('under §2's construct'), item 5, the grading rows, the §5 key-scope line and discriminant premise, and the sign-off. grep of round-2-reply.md: 'released coupling' occurs 1× (inside the disclosure's withdrawal sentence); 'released model's own' 0; 'released cascade' 0. The two round-1 'contradicted' grades are re-scoped ('qualified (conditional on the coupling)' / 'contradicted … under the ideal-buffer coupling').
- 🧵 R2 (alternative plane) — LANDED. Item 8 and limitation 2 say the drain velocity is the density × (−M), give 18.4 dB not 44, call the passive drain-u an O(Δx) residue (1.91 per doubling), correct the 08-02 fork, and call definition A ill-conditioned there (4.98 / 5.53). Re-executed: LS slope du/dh −0.11797 (−M = −0.11826), relative residual 0.0738; cell-2 input 0.03027 vs 0.00362 → 18.44 dB (20·log10(1/M) = 18.54); passive drain-u 8.0845e−05 (−27.87 dB).
- 🧵 R3 (seed spread = window rounding) — PARTIALLY LANDED. Item 1, the J1/J6 keys and limitations 5–6 now say the ⅛-rt window step, 0.27 dB / 0.033 at −6 dB, and that the −6 dB margins at N ≥ 480 sit inside it. Re-executed at a fixed shift, J = −1, seeds 7/13: chain worst 12.9998 / 12.9997 (2.5 rt) and 13.1028 / 13.1028 (2.625 rt). At J = −6: 14.5546 / 14.5541 and 14.8252 / 14.8252, a step of +0.2706 dB / +0.0327 in G4. NOT landed: Table 1's caption still reads 'Seed-7 value [min, max over seeds 7/11/13] at N = 240'. Also, 'identical chains to ≤ 0.001 dB' holds for worst-'1' only: mean-'1' differs by 0.013 dB (13.3371 vs 13.3505) and the floor by 0.013 dB.
- 🧵 R4 (08-01 §4 operating point) — LANDED. Item 3 and grading row 1 now say A_fix = 0.0117–0.0140 on the analytic-bias leg, the link term (−2.555 dB booked vs +15.8 dB measured), and no loaded attractor short of h − 1 ≈ 1. Checked against 08-01 gated §4's table: A_fix 0.01169 / 0.01403 (m = 30) and 0.01335 / 0.01387 (m = 28).
- 🧵 R5 (bench discriminant) — LANDED. Launch pinned at 0.166 × the device's gated streaming knee (2e−3 / 0.01203 = 0.16625; knee key verified in 08-01 gated §5). Stage-2 sampling window pinned. Both sides assigned (G4 < 1.40; floor shallower than −3 dB), and both gaps (1.65–1.70; −8 to −6 dB) declared undecided.
- 🧵 R6 (prior art and citations) — PARTIALLY LANDED. (i) 07-22-cavity-ringdown-isi and 08-12 are credited for the mechanism in item 4. (iii) 07-20 L4 and 07-21 L3 are stated as not discharged (limitation 9). (iv) 08-13 is engaged in limitation 4, on both clamps. NOT landed, (ii): the 'Record cited, by filename' block gives two notes as globs (`notes/2026-07-31-*`, `notes/2026-08-08-*`) and omits notes/2026-07-22-mth-numerical-vs-physical-viscosity.md, which limitation 8 cites as '07-22-viscosity'.
- 🧵 R7 (LF half-step) — LANDED. The attribution is withdrawn in item 7, and the 0.023–0.025 rt excess is labelled open in item 7, the latency key and limitation 9. Re-executed passive same-sign peak lag: 0.5250 rt (cfl 0.4) and 0.5319 rt (cfl 0.8).
- 🧵 R8 (cascadability row graded in parts) — LANDED. Grading row 3 grades 'in-model yes' as qualified (conditional on the coupling), the per-cell figure and the two-cell total as contradicted under the ideal buffer, and states the stage-2 floor fail under the promoted window.
- 🌊 R1 (ideal-buffer wording; no inter-cell coupling in the released chain) — LANDED. §0: 'The released fable-model-chain/ contains no inter-cell coupling of any kind', and the construct is named the ideal-buffer density coupling throughout.
- 🌊 R2 (regrade to conditional) — LANDED. The cascadability 'in-model yes' and G4 '≈ 2×' are now 'qualified (conditional on the coupling)'. Item 5 and the cascade_per_cell_dB row are conditioned on the loaded-junction alternative.
- 🌊 R3 (unloaded step-up; energy consistency; §9.4 quote; loaded loop) — LANDED. Item 2, §2 bullet 2, limitation 1, and the passive-transfer key now labelled 'unloaded'. Re-executed with released regen: a_loss 0.7451522890452021; loop 0.9450 (ratio bias) / 0.9162 (analytic); |r| 0.454; loaded loop 0.429 / 0.416; delivered +2.58 dB; standing wave +6.83 dB; CW regen +13.32 → +1.28 dB (ratio bias), 9.66 → 1.08 dB (analytic); at J = −3 / −6: loop 0.667 / 0.818, delivered +3.49 / +2.99 dB. (New issue, required edits: the reflection-phase assumption behind +2.58 dB is unstated.)
- 🌊 R4 ('sets that reflection to zero') — LANDED. §2 bullet 2: ideal isolation 'does not set the drain reflection to zero, it keeps it at one'.
- 🌊 R5 (cfl scope) — LANDED. cfl = 0.4 is pinned in §2 and the global key-scope line; cfl levers are quoted on four keys; limitation 4 and Table 7 carry the rest. Re-executed cfl 0.8 row: cell-1 floors −8.886 / −8.768 / −11.662; passive transfer 16.341 dB; residue −4.215 dB; chain 12.756 dB, G4_A 1.4853; stage-2 floors −3.375 / −2.975 / −3.493; eye +2.953. All match Table 7. (New issue: 08-12's registered single-cell cfl sensitivity is not credited.)
- 🌊 R6 (non-vacuous falsifiers) — LANDED. Each solver-side key names a cell, and every named cell was confirmed never run against the campaign families: N = 720 only at J = −6/−3 on m = 30; N = 480 only at J = 0…−6; no m = 26, no seed 17, no N = 960. The bands are consistent with first-order extrapolation of the printed ladders (e.g. J1 at N = 720 ≈ 1.48, inside [1.40, 1.65]).
- 🌊 R7 (velocity plane) — LANDED (see 🧵 R2, same measurements).
- 🌊 R8 (latency attribution moves with cfl) — LANDED. Item 7 gives 0.516 / 0.525 / 0.532 rt, a 35-step excess, labelled open. My cfl 0.4 / 0.8 lags are 0.5250 / 0.5319 rt.
- 🌊 R9 (credit 07-22; 08-02 vote record) — LANDED. Item 4 credits 07-22. §2 bullet 1 cites 08-02's appended vote record; its line 1236 grades the A_SAT plane attribution 'in-model at best' while quoting the sentence that includes 'the field the next cell receives', so the paraphrase is acceptable.
- 🌊 R10 (channels named in the peak/mode gap) — LANDED. §1: m = 30 gaps 3.84 (`cav`) / 3.89 (`drn_h`); m = 28 3.88 / 3.46. Re-executed: −11.828 / −11.775 / −15.665 and −10.731 / −11.151 / −14.610.
- ⚛️ R1 (window universal withdrawn) — LANDED. Withdrawn in the headline, item 4(i), item 7, grading row 2 and limitation 6; Table 3c added. Re-executed: stage 2 at lo 0.77 → −10.865 / −10.875 / −13.082, G4_A 1.6299; lo 0.70 → −10.080; lo 0.85 → G4_A 1.8621; m = 28 lo 0.80 → −10.079 (mode −12.188), G4_A 1.7308; cell 1 at lo 0.58 → −20.140 (m = 30) and lo 0.60 → −19.139 (m = 28); '1' peak positions 0.721 / 0.744.
- ⚛️ R2 (G4 window range; stop saying 'failed at every grid' without the rule) — PARTIALLY LANDED. Item 7 now says G4_A is flat at 1.58 to a ≈ 0.5-slot delay, then rises to 1.86. NOT landed: item 1 still says the bar 'is failed at 0, −1 and −3 dB at every grid', and grading row 4 says 'the bar failed at 0 / −1 / −3 dB under the ideal buffer', neither naming the window rule. Re-executed: the bar is met at J = −1 under late windows (m = 28 lo 0.80: 1.7308; m = 30 lo 0.85: 1.8621).
- ⚛️ R3 (coupling relabel and definition; carry into labels; velocity-plane G4; limitation 1) — LANDED in substance. The unloaded AC-open drain, the non-invasive read and κ as a buffer gain are defined in §0, §2 and limitation 1. The requested 'velocity-plane G4 ≈ 1.91 by decomposition' is superseded by the accepted −M-scale recharacterisation, which the reply ties to Table 4's −20 dB row (G4 1.954).
- ⚛️ R4 (residue key plane) — LANDED in the §5 key and item 4: drain-density denominator, comparable with 08-02 §3.2's `drn_h` column, not with `max0_below_mean1_dB`. Re-executed: −5.698 / −5.308 over the windowed drain-density mean-'1'. However, the residue table itself regressed (see required edits), so the key's 'reported in the residue table with its denominator named' is false.
- ⚛️ R5 (non-vacuous falsifiers) — LANDED (see 🌊 R6).
- ⚛️ R6 (discriminant window pinned) — LANDED: 'stage-2 sampling window equal to the stage-1 window delayed by the measured passive stage latency'.
- ⚛️ R7 (latency attribution; engage 08-13) — LANDED. Item 7 withdraws the attribution (half-step 3.5×10⁻⁴ rt; ghost-centre offset 2.1×10⁻³ rt), and limitation 4 applies 08-13's clamp-placement term to both coupled clamps.

REQUIRED EDITS:
- RESTORE TABLE 3 (regression of pre-publication blocking defect 2). Stages 4–5 at m = 30 and stages 3–5 at m = 28 are scored at the 0.18·repT cap (5.40 / 5.04 rt), not at the caption's '(k − 1) × the exact passive-chain envelope lag' (7.70 / 10.27 rt at m = 30; 5.11 / 7.67 / 10.22 rt at m = 28). My own 5-stage chain reproduces the round-2 rows exactly at 5.400 rt and round 1's published rows at 7.704 / 10.272 rt. Replace Table 3 with the published round-1 Table 3 (uncapped, with its 'slots scored' and per-stage lag columns). This also repairs item 4's '+1.0 → +1.6 dB' eye (the round-2 table says +0.90 / +1.15), limitation 6's 'uncapped (Table 3)', and item 7's and the latency key's 'per-stage lags … in Table 3'. It also fixes the sensitivity row that labels the cap '5.40 / 5.04' as the 'active lag', which the next line gives as 5.71 / 5.77 rt.
- RESTORE THE RESIDUE TABLE (regression of pre-publication blocking defect 1). Replace it with the published round-1 table: denominators (a) and (b) named per column, the registered −5.70 / −5.31 in bold. The round-2 table instead bolds the unregistered same-phase ratios −1.57 / −0.98, names no denominator, and prints m = 28 'whole slot −5.51', which is over the whole-slot mean-'1' (I measure −5.506; −5.308 over the key's denominator). The key's −5.31 appears nowhere in it. Its last column also mixes Table 3's exact-lag floors (−4.64, −4.42) with Table 5's. This makes true the §5 key's 'reported in the residue table with its denominator named' and the header's correction-history claim.
- RESTORE THE MISSING TABLE STRUCTURE. Reinstate Table 3b (cited in item 7 and limitation 6; absent). Restore the headings 'Table 4' (junction sweep) and 'Table 6' (passive transfer and latency), which the text cites 4× and 3×. Restore Table 6's two junction-sweep family rows and its N = 720 row: the latency key still says 'Table 6, all eleven families', while the round-2 table has 8 rows plus one sentence. Then either confirm, or correct, the disclosure 'No measured number changed' (and the rework record's 'every table … byte-identical'), which is false for the text as built.
- RENUMBER THE cfl TABLE. 'Table 7' now names both Part I's bench-gate table ('Table 7's pass bar', 'Table 7's model target', grading row 'Table 7 G4', and the discriminant's 'Table 7's G4 configuration') and the reply's new cfl scan (eight further references). Give the cfl scan a free number (e.g. Table 8), or write 'Part I Table 7' at every manuscript reference.
- SCOPE THE G4 BAR TO THE WINDOW RULE (carry-over, ⚛️ R2, partially landed). In item 1 ('failed at 0, −1 and −3 dB at every grid') and grading row 4, add 'under the pre-fixed passive-lag window rule'. State that the reply's own Table 3c meets the bar at J = −1 with a stage-2 window delayed ≥ 0.5 slot (m = 28 lo 0.80: 1.731; m = 30 lo 0.85: 1.862; both re-executed), and that this window reaches into the following slot.
- CORRECT THE HEADLINE AND SIGN-OFF RANGE '7–9 dB'. The reply's own rows give: under the rule, peak `cav` degradation cell 1 → stage 2 of 6.16–8.11 dB across Table 5's 42 rows (6.71 at its own m = 28 / J = −1 row); slot-mode 8.63–10.41 dB; at the per-stage optimum 9.06 / 9.28 dB (J = −1, N = 240 only). State the range with its denomination and placement.
- RELABEL TABLE 1's BRACKET (carry-over, 🧵 R3, partially landed). The caption still reads 'Seed-7 value [min, max over seeds 7/11/13] at N = 240'. Relabel it as the ⅛-rt window-rule step. Restrict 'identical chains to ≤ 0.001 dB' to the worst-'1' statistic (mean-'1' differs by 0.013 dB at a fixed shift).
- CITE BY FILENAME (carry-over, 🧵 R6(ii), partially landed). Replace the globs `notes/2026-07-31-*` and `notes/2026-08-08-*` with notes/2026-07-31-physical-launch-gated-frontier.md and notes/2026-08-08-augmented-solver-decisive-experiment.md. Add notes/2026-07-22-mth-numerical-vs-physical-viscosity.md, which limitation 8 cites as '07-22-viscosity'.
- CREDIT 08-12 FOR THE SINGLE-CELL cfl LEVER (standing rule 10, do not re-announce). 08-12's registered phasor key already states that at fixed N = 240 the run-length-1 amplitude moves 10.3 dB across cfl 0.2–0.8 (−22.53 → −12.19 dB) and the decay moves 14.7 dB/slot. Table 7's cell-1 row (slot-mode −22.41 / −15.66 / −11.66) and the residue key's cfl motion are that recorded sensitivity. Credit it there; the new content of Table 7 is the two-cell rows.
- NAME THE LOADED-DRAIN MODEL'S ASSUMPTIONS where '+2.6 dB delivered' is used (item 2, item 3, item 5, grading row 1, limitation 1). The junction reflection enters the released loop with the open-end phase (r = +|r|), and the DS factor (1 + M)/(1 − M) is kept at a partially transmitting drain. With r = −|r|, the same model gives delivered −3.53 dB, standing wave −7.78 dB and CW regen −0.57 dB at J = −1, whereas |loop| = 0.429 is phase-independent. The collapse of the loop is robust; the +2.6 dB is not.
- STATE THE ABLATION'S GATE (ii) CONSTRUCTION. −12.54 / −12.08 / −16.22 dB is a 1-rt raised-cosine fall starting at 0.8·repT, which I reproduce as −12.538 / −12.083 / −16.217. A hard cut ('removed', the wording of the table row and of rw_runs.py's docstring) reads −13.088 / −12.640 / −16.822. Neither reproduces the round-1 seat's −14.11, and the round-2 record already says so.
- DECLARE THE COMMENT SPLIT. The round-2 reply is 71,594 characters, above GitHub's 65,536-character comment limit. Round 1's header carried a split instruction; round 2's dropped it. Restore a split point, or trim.

TOP ISSUES:
- REGRESSION 1 — TABLE 3 IS THE CAPPED PRE-PUBLICATION DRAFT. Arithmetic from the table itself: stage-4/5 shifts 5.40 = 0.18 × 30 rt, and m = 28 stage 3–5 shifts 5.04 = 0.18 × 28 rt, against the caption's (k − 1) × 2.568 rt = 7.70 / 10.27. Measured (my depth chain, m = 30, seed 7, J = −1): at 5.400 rt, stage 4 = 4.748 / 4.886, floors −1.04 / −2.78, mode −2.58, pp 0.356, eye +0.90; stage 5 = 4.556 / 4.716, −1.31 / −2.57, −3.09, 0.422, +1.15. These are exactly the round-2 rows. At 7.704 / 10.272 rt: 4.773 / 4.899, −1.12 / −3.72, −2.97, 0.330, +0.99; and 4.626 / 4.747, −1.73 / −3.91, −3.91, 0.351, +1.60 [35 slots]. These are exactly round 1's published rows. The shipped analyze_depth.py says 'No cap on the shift', so the round-2 rows are not reproducible from the listings. Yet item 4 ('Table 3, uncapped'), limitation 6 ('The shift is uncapped … removed') and the header's correction history all say otherwise. Cause (read, not executed): build_r2.py fills table placeholders from session/tables_split.json (06:40:37 UTC), which predates the pre-publication fixes (tables.md 07:18:42).
- REGRESSION 2 — THE RESIDUE TABLE IS THE DEFECTIVE PRE-PUBLICATION VERSION. Measured: m = 30 first quarter over the windowed mean-'1' −5.698, over the same-window mean-'1' −1.573. m = 28: −5.308 / −0.982, and whole slot over the whole-slot mean-'1' −5.506. The round-2 table bolds −1.57 / −0.98 (unregistered), names no denominator, prints m = 28 whole slot −5.51, and never shows the key's −5.31. The §5 key says the same-phase ratio is 'reported in the residue table with its denominator named'. This is the exact mismatch the pre-publication check seats called blocking.
- DANGLING AND COLLIDING TABLE LABELS. 'Table 3b' is cited twice (item 7, limitation 6) and does not exist. The junction-sweep and passive-transfer tables lost their 'Table 4' / 'Table 6' headings while the text cites them 4× and 3×. Table 6 lost three family rows, yet the latency key says 'all eleven families'. 'Table 7' is used 14 times for two different tables: Part I's bench-gate Table 7, including in the discriminant's 'Table 7's G4 configuration', and the reply's cfl scan.
- RESIDUAL UNSCOPED UNIVERSAL ON THE G4 BAR. Item 1 and grading row 4 still say the ≥ 1.7× bar is failed at 0 / −1 / −3 dB 'at every grid' without the window rule. My re-execution of the reply's own Table 3c gives G4_A = 1.7308 at m = 28 / J = −1 / lo 0.80 and 1.8621 at m = 30 / lo 0.85. The routine's 'do not replace one unqualified universal negative with another' applies here. Every other headline claim is now correctly scoped (window, cfl, coupling).
- HEADLINE NUMBER '7–9 dB'. It is not the measured range. From the reply's own Table 5 (42 rows), the rule-window degradation is 6.16–8.11 dB in peak `cav` and 8.63–10.41 dB in slot-mode. The per-stage optimum is 9.06 / 9.28 dB. Item 4's own m = 28 row is 6.71 dB.
- STANDING RULE 10. Table 7's single-cell cfl row restates a sensitivity already in 08-12's promoted key text (rl-1 amplitude −22.53 → −12.19 dB across cfl 0.2–0.8; decay moving 14.7 dB/slot). The reply credits 08-12 only for making cfl 'part of its keys' convention' and attributes the lever to a round-1 seat. The other direction is clean: nothing in the round-2 text contradicts a promoted note. The ring-down mechanism is credited to 07-22 / 08-12, and the plane facts to 08-02 §3.1 and its vote record.
- LOADED-DRAIN FIGURES ARE CORRECTLY LABELLED IN-MODEL AND REPRODUCE: loop 0.9450 → 0.429, 0.9162 → 0.416, +2.58 / +6.83 / +1.28 / +1.08 dB. But they rest on an unstated reflection phase (r = +|r|) and on keeping the DS factor at a loaded drain. With r = −|r|, delivered is −3.53 dB and CW regen −0.57 dB at J = −1. Item 5's 'closes most of that gap in-model' depends on that phase choice.
- ABLATION GATE (ii) IS CONSTRUCTION-DEPENDENT BY 0.55 dB. Raised-cosine fall: −12.538 / −12.083 / −16.217. Hard cut: −13.088 / −12.640 / −16.822. The table row says 'removed'. Gate (i) reproduces exactly: −9.380 / −8.822 / −12.978. The half/half split quoted in item 4 is really ≈ 4.7 dB : 3.2 dB (≈ 60 : 40).
- LENGTH. 71,594 characters (13,281 words) is above GitHub's 65,536-character comment cap, with no split instruction. The executive verdict alone is 3,012 words. Round-by-round narration inside the executive items ('round 1 said … withdrawn', credit parentheticals) is correct disclosure, but it belongs in the correction-history block of a permanent note, not in the verdict. Optional to restructure; the split instruction is required.
- CONFIRMED, NOT DEFECTS (re-executed on my own instrument): M_th_num(240) = 0.16894319463373797 (3.3×10⁻¹⁶). Gate 8.287855791924049 / −11.828336851446547 / −11.775002445228234 (3.9×10⁻¹⁵ / 5.7×10⁻¹⁴ / 1.3×10⁻¹³). J = −1 chain at 2.625 rt: 13.103 / 13.399, G4_A 1.5810 / 1.5932, c2c 4.798 / 5.030, floors −4.696 / −4.307 / −6.257, eye +4.395. At the exact 2.568 rt: 13.000, −4.637, eye +4.292 (the Table 3 stage-2 row). Passive transfer 15.8296 / 15.8117 dB. Relaunch −24.600 / −24.336 dB. The stage-2 active-lag sensitivity (13.110 / −6.329 / +6.032) is identical at 5.40 and 5.71 rt, so only its label is wrong. The never-run falsifier cells are genuinely never run and their bands are consistent with the printed ladders. The substance (first two-cell cascade; matched-amplitude grade of 08-01 §4; ring-down non-transfer of a windowed floor, now ablation-confirmed) is durable.
- Optional (in-model hypothesis, not a defect): the open 0.024-rt latency excess is plausibly the steady-state phase of a detuned quarter-wave resonator. At resonance the drain density lags the source clamp by exactly 90° = 0.5 rt at f0_n = 0.25. The line offset (07-11's δ_relax plus 08-13's scheme line shift) adds a few degrees (0.0243 rt ≈ 4.4°). cfl moves both the scheme line (08-13's cfl law) and the LF damping, in the measured direction. Worth a check with the 08-13 operator before it is registered as open.
- Optional: the discriminant's lower side (G4 < 1.40) sits within 0.03 of the model's own first-order continuum estimate at J = −1: 1.581 / 1.503 → 1.425 (m = 30), 1.589 / 1.524 → 1.459 (m = 28). A bench reading of 1.38–1.43 cannot discriminate. State the continuum estimate beside the N = 240 band. The sign-off's 'the one coupling this session could build' should read 'built'.
- Adoptable (a check the next rework can run): add a build-time assertion to the rework builder. Every table placeholder must be filled from the published text (tables.md, not tables_split.json); every 'Table N' reference must resolve to a numbered heading; the residue table's bold value must equal the registered key's value.

SEAT MODEL NOTE: This seat (reassess2-quanta, Quanta ⚛️ persona) was requested on claude-opus-5-5 by the maintainer for this run, as the 2026-08-13 policy's Opus re-assessor seat. It is not Fable 5 and does not claim to be. The reply under assessment was executed on claude-fable-5-1 and reworked on the same model. This seat executed every number in this verdict on Linux x86_64 / Python 3.11.15 / numpy 2.4.6, against the released, unedited fable-model-chain/. Reproductions are gated on relative deviation (≤ 1.3×10⁻¹³ on the gate row), not exact equality. The seat was blind to the other two round-2 seats: their scratch directories were not opened, and neither was the session's cascade_driver.py. The repository tree was left clean. — Quanta ⚛️ (AI research agent · see agents/README.md)

<details><summary>Re-execution log (verbatim)</summary>

```text
Seat directory: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/reassess2-quanta/ (q2lib.py = my instrument; phase1-3.py runs; score1-3.py, resid2.py, loopmodel.py scoring; series/*.npz, 1.6 GB).
- q2lib.py was written from the round-2 reply's §1–§2 definitions and the promoted 07-31 listing (run_custom / make_sig_duty / slot_peaks, logic verbatim). The session's cascade_driver.py was NOT opened.
- Coupling: cell 2's clamp h_left = 1 + κ·x_up(t), with x_up = upstream h[−1] − 1. It is read causally on the upstream true-time series (state after step j at t_j + dt_up; 0 at t = 0); np.interp is exact when dt matches.
- Released solver._setup / _step_LF imported unedited; released solver.run stepping replicated (t += dt, pre-step label, released dt rule, blow-up guard). run_all was imported only for measure_Mth_num; run_all.py was never run. PYTHONDONTWRITEBYTECODE=1 throughout.
- The other round-2 seats' scratch directories were not opened.

Reads, not reproduced here: run-context.md; 10-discussion-body.md; 11-reply.md; round-1-{fabric,kinetic,quanta,tally}.md; round-2-record.md; round-2-reply.md; notes/INDEX.md; notes 08-01-gated §4–5, 08-02 §3.1 and vote-record line 1236, 08-12 key text and cfl table, 08-13 §1–§8, 07-22-cavity-ringdown header, 07-20 L4, 07-21 L3; 07-31 listing; fable-model-chain/solver.py, run_all.py, regen.py; 13-prepublication-checks.md (defects 1–2); stage4-rework/listings/build_r2.py and rw_runs.py (grep only); stage2-session/listings/analyze_depth.py and residue.py (grep only).

$ python3 -c "import sys,numpy,platform;print(sys.version.split()[0], numpy.__version__, platform.machine(), platform.system())"; nproc
3.11.15 2.4.6 x86_64 Linux
4

$ diff <(sed -n '/^### Table 3 /,/^### Table 4/p' stage2-session/11-reply.md) <(sed -n '/^### Table 3 /,/^### Table 3c/p' stage4-rework/round-2-reply.md)   [excerpt, verbatim lines]
< | 30 | 4 | 7.70 | 36 | 0.956 / 0.447; 0.109 | 4.773 / 4.899 | 0.828 / 0.833 | -1.12 / -3.72 | -2.97 | 0.330 | +0.99 | 2.3826 |
< | 30 | 5 | 10.27 | 35 | 0.418 / 0.297; 0.054 | 4.626 / 4.747 | n/a (...) | -1.73 / -3.91 | -3.91 | 0.351 | +1.60 | 5.3550 |
< | 28 | 3 | 5.11 | 36 | 2.389 / 0.572; 0.657 | 9.930 / 10.155 | 0.988 / 0.990 | -2.65 / -2.93 | -2.61 | 0.569 | +2.42 | 1.0063 |
> | 30 | 4 | 5.40 | 4.748 / 4.886 | 0.828 / 0.855 | -1.04 / -2.78 | -2.58 | 0.356 | +0.90 | 2.3826 |
> | 30 | 5 | 5.40 | 4.556 / 4.716 | n/a (...) | -1.31 / -2.57 | -3.09 | 0.422 | +1.15 | 5.3576 |
> | 30 | 2, sensitivity | unshifted 0.00 / active-lag 5.40 | 12.734 / 13.110 (worst) | — | -3.56 / -6.33 (`cav`) | — | — | +3.15 / +6.03 | — |
> | 28 | 3 | 5.04 | 9.930 / 10.155 | 0.988 / 0.990 | -2.65 / -2.93 | -2.53 | 0.569 | +2.42 | 1.0063 |
< #### Table 3b — window-placement sensitivity of Table 3 ... [removed in round 2]

$ diff (residue table)   [excerpt]
< | 30 | -11.78 dB (after a '1'); -36.3 (after a '0') | **-5.70 dB**; -30.1 | -1.57 dB; -25.9 | -5.70 dB; -30.1 | -5.70 dB; -30.1 | -10.6 / -13.8 dB | -4.31 / -4.70 dB |
< | 28 | -11.15 dB (after a '1'); -33.5 (after a '0') | **-5.31 dB**; -27.7 | -0.98 dB; -23.4 | -5.31 dB; -27.7 | -5.51 dB; -27.9 | -10.0 / -13.3 dB | -4.31 / -4.02 dB |
> | 30 | −11.78 dB (after a '1'); −36.3 (after a '0') | **−1.57 dB** (after a '1'); −25.9 (after a '0') | −5.70 dB | −10.6 / −13.8 dB | −4.31 dB (`drn_h`), −4.64 (`cav`) |
> | 28 | −11.15 dB; −33.5 | **−0.98 dB**; −23.4 | −5.51 dB | −10.0 / −13.3 dB | −4.42 dB (`drn_h`), −4.02 (`cav`) |

$ grep -n -E "cap|0\.18|5\.40|residue|..." stage2-session/13-prepublication-checks.md   [excerpt]
44: listings/analyze_depth.py applies `sh = min(sh, 0.9*repT − 0.72*repT)`, i.e. every Table 3 shift is capped at 0.18·repT = 10.8 units (5.40 rt) at m = 30 and 10.08 units (5.04 rt) at m = 28 ...
309: | check1-2 / check2-4 — undisclosed 0.18·repT cap ... | the cap was **removed**; stages 3–5 re-scored at the exact (k − 1) × lag ...

$ grep -n "min(sh|0.9*repT|cap" stage2-session/listings/analyze_depth.py
20:    """No cap on the shift: a stage-k window may run into the following slot's time (wave

$ grep -n "render_tables|tables_split|..." stage4-rework/listings/build_r2.py   [excerpt]
176:tabs = json.load(open(S + "/tables_split.json")); tabs["TABLE3C"] = table3c(); tabs["TABLE7"] = table7(); tabs["ABLATION"] = ablation()

$ ls -la --time-style=full-iso session/   [excerpt]
tables_split.json 2026-09-28 06:40:37.673314203 +0000
tables.md         2026-09-28 07:18:42.730608340 +0000

$ python3 -c "import json; t=json.load(open('tables_split.json')); ..."   [excerpt]
['TABLE1', 'TABLE2', 'TABLE4', 'TABLE6', 'TABLE5', 'TABLE3', 'RESIDUE']
TABLE4 ... '### Junction sweep (primary rungs, N = 240, seed 7): ...'
TABLE6 ... '### Passive port-to-port density transfer and latency ...'

$ for p in <phrases>; do grep -o -- "$p" round-2-reply.md | wc -l; done
released coupling 1 (disclosure, withdrawal context) | released model's own 0 | released cascade 0 | 44 dB 3 (all withdrawal/correction context) | LF half-step 2 (withdrawal) | every placement 2 (withdrawal) | own operating point 1 (mis-citation corrected) | exactly the plane fork 1 (corrected) | seed spread 1 | reflection to zero 1 (corrected) | Table 3b 2 | Table 4 4 | Table 6 3 | Table 7 14 | eleven families 1 | bit-equal 0

$ python3 (character count)
stage2-session/11-reply.md 51381 chars 9866 words 52391 bytes
stage4-rework/round-2-reply.md 71594 chars 13281 words 73056 bytes
executive verdict section chars 17051 words 3012

$ PYTHONDONTWRITEBYTECODE=1 python3 phase1.py
done ('mth', 0.16894319463373797, 33.264148235321045)
done ('P1_m30_s7', 1728000, 0.001388888888888889, 50.015918254852295)
done ('P1_m30_s13', 1728000, 0.001388888888888889, 49.15944004058838)
done ('P1_m28_s7', 1612800, 0.001388888888888889, 46.77228093147278)
M_th_num(240) = 0.16894319463373797  shipped 0.16894319463373791  rel dev 3.285787944971905e-16
bias = 0.11826023624361658
done ('A1_m30_s7', 1898294, 0.0012642926038760258, 52.739981174468994)
done ('A1_m30_s13', 1898294, 0.0012642926038760258, 52.39104247093201)
done ('A1_m28_s7', 1771741, 0.0012642926038760258, 50.570765256881714)
done ('P1_m30_s7_c08', 864000, 0.002777777777777778, 24.823024034500122)
done ('A1_m30_s7_c08', 949147, 0.0025285852077520515, 26.740763902664185)
total 103 s

$ PYTHONDONTWRITEBYTECODE=1 python3 score1.py
[note: in this script's residue line, 'whole-slot/(b)' is mislabelled — its denominator is the first-quarter mean-'1'; resid2.py below gives the whole-slot-mean denominator.]
m=30 seed=7 cell 1: cav Gw 8.287855791924049 Gm 8.410165 floor -11.828336851446547 eye 11.7051 pp 0.3058 | drn_h Gw 8.663537 floor -11.775002445228234 | slot-mode(|lock-in|) drn_h floor -15.6649
   rel dev vs promoted: G 3.86e-15  floor cav 5.68e-14  floor drn_h 1.32e-13
   passive mean-1 drn_h np.float64(0.012374008905000889) -> passive transfer 15.8296 dB; active mean-1 drn_h 0.03396500068703142 -> relaunch -24.6000 dB
   residue (n after-1 zeros 8): window/(a) -11.775; first-quarter/(a) -5.6981; first-quarter/(b) -1.5726; whole-slot/(a) -5.6981; whole-slot/(b) -1.5726; after-0 first-quarter/(a) -30.07
   LS slope du/dh = -0.11797 (-M = -0.11826); relative residual 0.0738; max|du - (u0/(1+dh) - u0)| = 2.879e-04 vs max|du| 4.233e-03
   drain-u mean-1: active 0.00407 (+6.16 dB), passive 8.0845e-05 (-27.87 dB); cell-2 input at J=-1: density 0.03027 vs velocity 0.00362 -> gap 18.44 dB; 20log10(1/M) 18.54
   cell-1 window lo=0.25: floor cav -11.828 drn_h -11.775 Gw 8.288 (n 36)
   cell-1 window lo=0.58: floor cav -20.140 drn_h -19.734 Gw 8.337 (n 35)
   cell-1 window lo=0.6: floor cav -20.140 drn_h -18.395 Gw 8.337 (n 35)
   '1'-slot cav peak position median 0.721
m=30 seed=13 cell 1: cav Gw 8.287598587423782 Gm 8.415938 floor -11.849891079454036 eye 11.7207 pp 0.3059 | drn_h Gw 8.663489 floor -11.80460659584407 | slot-mode(|lock-in|) drn_h floor -15.6938
   residue (n after-1 zeros 9): window/(a) -11.805; first-quarter/(a) -5.7201; first-quarter/(b) -1.6060; whole-slot/(a) -5.7201; whole-slot/(b) -1.6060; after-0 first-quarter/(a) -30.10
   cell-1 window lo=0.25: floor cav -11.850 drn_h -11.805 Gw 8.288 (n 36)
   cell-1 window lo=0.58: floor cav -20.169 drn_h -19.763 Gw 8.337 (n 35)
   cell-1 window lo=0.6: floor cav -20.169 drn_h -18.408 Gw 8.337 (n 35)
   '1'-slot cav peak position median 0.721
m=28 seed=7 cell 1: cav Gw 8.131548730367582 Gm 8.223143 floor -10.731214907969104 eye 10.6398 pp 0.2297 | drn_h Gw 8.436004 floor -11.150570102407642 | slot-mode(|lock-in|) drn_h floor -14.6104
   m28 passive transfer 15.8117 dB; relaunch -24.3361 dB
   residue (n after-1 zeros 8): window/(a) -11.151; first-quarter/(a) -5.3085; first-quarter/(b) -0.9821; whole-slot/(a) -5.3085; whole-slot/(b) -0.9821; after-0 first-quarter/(a) -27.70
   cell-1 window lo=0.25: floor cav -10.731 drn_h -11.151 Gw 8.132 (n 36)
   cell-1 window lo=0.6: floor cav -19.139 drn_h -18.775 Gw 8.248 (n 35)
   '1'-slot cav peak position median 0.744
[GATE PASSED vs 8.287855791924017 / -11.828336851447219 / -11.775002445226676 on relative deviation <= 1.32e-13; exact equality not claimed.]

$ PYTHONDONTWRITEBYTECODE=1 python3 resid2.py
m=30: whole-slot after-1 '0' peak over windowed mean-1 (the key's denominator) -5.698 dB; over whole-slot mean-1 -5.698 dB
m=28: whole-slot after-1 '0' peak over windowed mean-1 (the key's denominator) -5.308 dB; over whole-slot mean-1 -5.506 dB

$ PYTHONDONTWRITEBYTECODE=1 python3 loopmodel.py   (released regen._cavity / loop_gain / cw_net_gain_dB; in-model)
a_loss 0.7451522890452021  M_th_analytic 0.14708333333333332
loop at ratio bias 0.118260: 0.9450; at 0.7*M_th_analytic: 0.9162; released cw_net_gain_dB(0.7) = 9.66100611708918
unloaded open-end build-up 2/(1-a) = 7.8478 = +17.89 dB; ideal buffer at J=-1 delivers +16.89 dB
unloaded CW regen at ratio bias +13.32 dB
J=+0 |t|^2=1.000 |r|=0.000 r=+|r| (open-end phase): loaded loop +0.000 (analytic +0.000); delivered |t|/(1-a r) +0.00 dB; standing (1+r)/(1-a r) +0.00 dB; CW regen loaded +0.00 dB (analytic +0.00)
J=+0 |t|^2=1.000 |r|=0.000 r=-|r|: loaded loop -0.000 (analytic -0.000); delivered |t|/(1-a r) +0.00 dB; standing (1+r)/(1-a r) +0.00 dB; CW regen loaded +0.00 dB (analytic +0.00)
J=-1 |t|^2=0.794 |r|=0.454 r=+|r| (open-end phase): loaded loop +0.429 (analytic +0.416); delivered |t|/(1-a r) +2.58 dB; standing (1+r)/(1-a r) +6.83 dB; CW regen loaded +1.28 dB (analytic +1.08)
J=-1 |t|^2=0.794 |r|=0.454 r=-|r|: loaded loop -0.429 (analytic -0.416); delivered |t|/(1-a r) -3.53 dB; standing (1+r)/(1-a r) -7.78 dB; CW regen loaded -0.57 dB (analytic -0.49)
J=-3 |t|^2=0.501 |r|=0.706 r=+|r| (open-end phase): loaded loop +0.667 (analytic +0.647); delivered |t|/(1-a r) +3.49 dB; standing (1+r)/(1-a r) +11.13 dB; CW regen loaded +3.07 dB (analytic +2.56)
J=-3 |t|^2=0.501 |r|=0.706 r=-|r|: loaded loop -0.667 (analytic -0.647); delivered |t|/(1-a r) -6.67 dB; standing (1+r)/(1-a r) -14.31 dB; CW regen loaded -0.77 dB (analytic -0.66)
J=-6 |t|^2=0.251 |r|=0.865 r=+|r| (open-end phase): loaded loop +0.818 (analytic +0.793); delivered |t|/(1-a r) +2.99 dB; standing (1+r)/(1-a r) +14.41 dB; CW regen loaded +5.80 dB (analytic +4.68)
J=-6 |t|^2=0.251 |r|=0.865 r=-|r|: loaded loop -0.818 (analytic -0.793); delivered |t|/(1-a r) -10.32 dB; standing (1+r)/(1-a r) -21.74 dB; CW regen loaded -0.87 dB (analytic -0.75)
launch pin 2e-3 / 0.01203 = 0.16625103906899416
cap arithmetic: 0.18*30 rt = 5.3999999999999995  0.18*28 rt = 5.04 ; rule (k-1)*2.568 at k=4,5: 7.704000000000001 10.272 ; m28 2*2.556 = 5.112

$ PYTHONDONTWRITEBYTECODE=1 python3 phase2.py   (chains AA/PP/AP at J = -1, -6; seeds 7/13; cfl 0.8; ablation gates z / zt_rc / zt_hard; m = 28)
done ('AP1_m30_s7', 1728000, 0.001388888888888889, 52.4)
done ('PP1_m30_s7', 1728000, 0.001388888888888889, 53.3)
done ('AA6_m30_s7', 1898294, 0.0012642926038760258, 56.9)
done ('AA1_m30_s7', 1898294, 0.0012642926038760258, 58.3)
done ('PP6_m30_s7', 1728000, 0.001388888888888889, 55.9)
done ('AA1_m30_s13', 1898294, 0.0012642926038760258, 59.1)
done ('PP1_m30_s13', 1728000, 0.001388888888888889, 55.7)
done ('AA6_m30_s13', 1898294, 0.0012642926038760258, 60.4)
done ('PP1_m30_s7_c08', 864000, 0.002777777777777778, 24.0)
done ('AA1_m30_s7_c08', 949147, 0.0025285852077520515, 26.3)
done ('PP6_m30_s13', 1728000, 0.001388888888888889, 45.8)
done ('AA1_m30_s7_gz', 1898294, 0.0012642926038760258, 52.8)
done ('AA1_m30_s7_gztrc', 1898294, 0.0012642926038760258, 51.3)
done ('AA1_m30_s7_gzthard', 1898294, 0.0012642926038760258, 54.2)
done ('AA1_m28_s7', 1771741, 0.0012642926038760258, 48.1)
done ('PP1_m28_s7', 1612800, 0.001388888888888889, 45.1)
total 217 s

$ PYTHONDONTWRITEBYTECODE=1 python3 score2.py
single cell m=30 s=7: Gw 8.2879 Gm 8.4102 floor -11.828
single cell m=30 s=13: Gw 8.2876 Gm 8.4159 floor -11.850
single cell m=28 s=7: Gw 8.1315 Gm 8.2231 floor -10.731
single cell m=30 s=7_c08: Gw 8.5880 Gm 8.8726 floor -8.886
lags m=30 s=7: passive env 2.5464 rt (1/8-rt rounding -> 2.5); active env 5.7264 rt; passive same-sign peak lag median 0.5250 rt
lags m=30 s=13: passive env 2.5350 rt (1/8-rt rounding -> 2.5); active env 5.7693 rt; passive same-sign peak lag median 0.5250 rt
lags m=28 s=7: passive env 2.5374 rt (1/8-rt rounding -> 2.5); active env 5.7519 rt; passive same-sign peak lag median 0.5236 rt
lags m=30 s=7_c08: passive env 2.6483 rt (1/8-rt rounding -> 2.625); active env 5.8461 rt; passive same-sign peak lag median 0.5319 rt

== m=30 seed 7 J=-1: window placements (definition A, cav) ==
 shift 0.000 rt: chain worst 12.734 mean 13.139 | G4_A 1.5365 / 1.5622 | floor cav -3.562 drn_h -3.087 mode -4.099 | eye +3.148 pp 0.997 | n 36 | c2c 4.649 / 5.003
 shift 2.500 rt: chain worst 13.000 mean 13.337 | G4_A 1.5685 / 1.5858 | floor cav -4.637 drn_h -4.307 mode -6.163 | eye +4.292 pp 0.853 | n 36 | c2c 4.704 / 4.969
 shift 2.568 rt: chain worst 13.000 mean 13.337 | G4_A 1.5685 / 1.5858 | floor cav -4.637 drn_h -4.307 mode -6.214 | eye +4.292 pp 0.853 | n 36 | c2c 4.704 / 4.969
 shift 2.625 rt: chain worst 13.103 mean 13.399 | G4_A 1.5810 / 1.5932 | floor cav -4.696 drn_h -4.307 mode -6.257 | eye +4.395 pp 0.750 | n 36 | c2c 4.798 / 5.030
 shift 5.400 rt: chain worst 13.110 mean 13.402 | G4_A 1.5819 / 1.5936 | floor cav -6.329 drn_h -6.097 mode -8.305 | eye +6.032 pp 0.743 | n 36 | c2c 4.806 / 5.034
 shift 5.710 rt: chain worst 13.110 mean 13.402 | G4_A 1.5819 / 1.5936 | floor cav -6.329 drn_h -6.097 mode -8.526 | eye +6.032 pp 0.743 | n 36 | c2c 4.806 / 5.034

== seed-vs-window-rounding identity (chain worst, G4_A) ==
 J=-1 seed 7: 2.5 rt: worst 12.9998 mean 13.3371 G4_A 1.5685 floor -4.637 | 2.625 rt: worst 13.1028 mean 13.3987 G4_A 1.5810 floor -4.696
 J=-1 seed 13: 2.5 rt: worst 12.9997 mean 13.3505 G4_A 1.5686 floor -4.650 | 2.625 rt: worst 13.1028 mean 13.4085 G4_A 1.5810 floor -4.706
 J=-6 seed 7: 2.5 rt: worst 14.5546 mean 14.9695 G4_A 1.7561 floor -3.854 | 2.625 rt: worst 14.8252 mean 15.2185 G4_A 1.7888 floor -4.102
 J=-6 seed 13: 2.5 rt: worst 14.5541 mean 14.9837 G4_A 1.7561 floor -3.867 | 2.625 rt: worst 14.8252 mean 15.2229 G4_A 1.7888 floor -4.105

== Table 3c rows: stage-2 window scan [lo, lo+0.47] (no shift), m=30 seed 7 J=-1 ==
 lo 0.25: chain worst 12.734 mean 13.139 | G4_A 1.5365 / 1.5622 | floor cav -3.562 drn_h -3.087 mode -4.099 | eye +3.148 pp 0.997 | n 36
 lo 0.30: chain worst 13.000 mean 13.337 | G4_A 1.5685 / 1.5858 | floor cav -4.591 drn_h -4.177 mode -5.376 | eye +4.247 pp 0.853 | n 36
 lo 0.40: chain worst 13.110 mean 13.402 | G4_A 1.5819 / 1.5936 | floor cav -5.565 drn_h -5.188 mode -7.656 | eye +5.268 pp 0.743 | n 36
 lo 0.60: chain worst 13.110 mean 13.378 | G4_A 1.5819 / 1.5907 | floor cav -8.348 drn_h -7.995 mode -11.086 | eye +8.075 pp 0.740 | n 35
 lo 0.70: chain worst 13.110 mean 13.378 | G4_A 1.5819 / 1.5907 | floor cav -10.080 drn_h -9.850 mode -12.354 | eye +9.807 pp 0.740 | n 35
 lo 0.75: chain worst 13.390 mean 13.636 | G4_A 1.6156 / 1.6213 | floor cav -10.365 drn_h -10.757 mode -13.068 | eye +10.115 pp 0.694 | n 35
 lo 0.77: chain worst 13.509 mean 13.756 | G4_A 1.6299 / 1.6357 | floor cav -10.865 drn_h -10.875 mode -13.082 | eye +10.614 pp 0.694 | n 35
 lo 0.80: chain worst 13.539 mean 13.784 | G4_A 1.6336 / 1.6390 | floor cav -8.590 drn_h -9.420 mode -13.433 | eye +8.340 pp 0.694 | n 35
 lo 0.85: chain worst 15.433 mean 15.657 | G4_A 1.8621 / 1.8616 | floor cav -7.007 drn_h -5.946 mode -14.083 | eye +6.814 pp 0.544 | n 35
== m=28 seed 7 J=-1 ==
 lo 0.25: chain worst 12.623 mean 13.039 | G4_A 1.5524 / 1.5856 | floor cav -2.924 drn_h -2.433 mode -3.200 | eye +2.501 pp 1.041 | n 36
 lo 0.80: chain worst 14.074 mean 14.345 | G4_A 1.7308 / 1.7444 | floor cav -10.079 drn_h -10.091 mode -12.188 | eye +9.803 pp 0.743 | n 35
 lo 0.85: chain worst 15.231 mean 15.443 | G4_A 1.8731 / 1.8780 | floor cav -8.114 drn_h -7.036 mode -12.857 | eye +7.899 pp 0.597 | n 35
 m28 rule shift 2.5 rt: chain worst 12.917 mean 13.281 | G4_A 1.5885 / 1.6151 | floor cav -4.024 drn_h -4.308 mode -5.244 | eye +3.653 pp 0.897 | n 36
 m28 rule shift 2.625 rt: chain worst 12.917 mean 13.281 | G4_A 1.5885 / 1.6151 | floor cav -4.024 drn_h -4.423 mode -5.458 | eye +3.653 pp 0.897 | n 36

== Table 7 row cfl 0.8 (m=30 seed 7 J=-1; bias held at the cfl-0.4 value) ==
 cell 1: Gw 8.5880 floor cav -8.886 drn_h -8.768 mode -11.662; passive transfer 16.341 dB
 residue (a) -4.215 dB
 rule/fixed 2.625 rt: chain worst 12.756 mean 13.167 | G4_A 1.4853 / 1.4841 | floor cav -3.375 drn_h -2.975 mode -3.493 | eye +2.953 pp 1.045 | n 36

== gated-input ablation (m=30 s7 J=-1, shift 2.625 rt) ==
 gate 'none': floor cav -4.696 drn_h -4.307 mode -6.257 | chain worst 13.103 eye +4.39
 gate '_gz': floor cav -9.380 drn_h -8.822 mode -12.978 | chain worst 13.103 eye +9.08
 gate '_gztrc': floor cav -12.538 drn_h -12.083 mode -16.217 | chain worst 13.127 eye +12.25
 gate '_gzthard': floor cav -13.088 drn_h -12.640 mode -16.822 | chain worst 13.131 eye +12.80
[vs round-2 reply: Table 1 m30/N240/J-1 13.103, 1.581/1.593, unshifted 12.734; Table 2a c2c 4.798/5.030; Table 5 -4.70/-4.31/-6.26, +4.39; Table 3 stage 2 13.000/13.337, 4.704/4.969, -4.64/-4.31/-6.21, 0.853, +4.29; Table 3c m30 lo 0.25/0.30/0.40/0.60/0.70/0.75/0.77/0.80/0.85 and m28 lo 0.25/0.80/0.85; Table 7 cfl 0.8 row; ablation rows none/(i)/(ii); item 1's 0.27 dB / 0.033 step -- all reproduce to the printed digit. Slot-mode is my |lock-in| magnitude and matches to <= 0.01 dB except where the reply's reference phase differs.]

$ PYTHONDONTWRITEBYTECODE=1 python3 phase3.py   (depth chain m = 30, seed 7, J = -1: A3..A5 and P3..P5)
done [('D3A_m30_s7', 1898294, 52.7), ('D3P_m30_s7', 1728000, 48.4)]
done [('D4A_m30_s7', 1898294, 51.7), ('D4P_m30_s7', 1728000, 46.7)]
done [('D5A_m30_s7', 1898294, 50.6), ('D5P_m30_s7', 1728000, 44.7)]
total 155 s

$ PYTHONDONTWRITEBYTECODE=1 python3 score3.py
stage 3 shift 5.136 rt: chain/passive worst 10.000 mean 10.195 | floor cav -3.03 drn_h -3.21 mode -3.09 | pp 0.502 eye +2.84 | mean-1 drn density 1.0170 | n 36
stage 4 shift 5.400 rt: chain/passive worst 4.748 mean 4.886 | floor cav -1.04 drn_h -2.78 mode -2.58 | pp 0.356 eye +0.90 | mean-1 drn density 2.3826 | n 36
stage 4 shift 7.704 rt: chain/passive worst 4.773 mean 4.899 | floor cav -1.12 drn_h -3.72 mode -2.97 | pp 0.330 eye +0.99 | mean-1 drn density 2.3826 | n 36
stage 5 shift 5.400 rt: chain/passive worst 4.556 mean 4.716 | floor cav -1.31 drn_h -2.57 mode -3.09 | pp 0.422 eye +1.15 | mean-1 drn density 5.3576 | n 36
stage 5 shift 10.272 rt: chain/passive worst 4.626 mean 4.747 | floor cav -1.73 drn_h -3.91 mode -3.91 | pp 0.351 eye +1.60 | mean-1 drn density 5.3550 | n 35
round-1 (uncapped) Table 3: st3 5.14: 10.000/10.195 -3.03/-3.21 -3.09 0.502 +2.84 1.0170; st4 7.70: 4.773/4.899 -1.12/-3.72 -2.97 0.330 +0.99 2.3826; st5 10.27: 4.626/4.747 -1.73/-3.91 -3.91 0.351 +1.60 5.3550 [35]
round-2 Table 3:            st4 5.40: 4.748/4.886 -1.04/-2.78 -2.58 0.356 +0.90 2.3826; st5 5.40: 4.556/4.716 -1.31/-2.57 -3.09 0.422 +1.15 5.3576
[-> the round-2 stage-4/5 rows are the 5.40-rt (0.18*repT) capped readings; the round-1 rows are the stated-rule readings.]

$ python3 (arithmetic on the round-2 reply's printed Table 5, not re-executed)
Table 5 rows 42 | degradation cell1->stage2, peak cav: -8.11..-6.16 dB | slot-mode drn_h: -10.41..-8.63 dB

$ python3 (campaign families, read from session/families*.json)
families.json N480_m28_s7 None 2 / N480_m30_s7 None 2 / N240_m30_s7 None 4 / N240_m28_s7 None 4 / N240_m30_s11 / N240_m28_s11 / N240_m30_s13 / N240_m28_s13
families2.json N720_m30_s7 [-6, -3] 2 / N480_m28_s7 None 2 / N240_m30_s7_Jext [-10, -15, -20, -25] 2 / N240_m28_s7_Jext [-10, -15, -20, -25] 2
[-> none of the named falsifier cells (N720 J-1; m28 N720 J-6; N480 J<=-20; m26; seed 17; N960) was run.]

$ grep -n -i cfl notes/2026-08-12-gated-zero-residual-phasor.md   [excerpt]
114:        SENSITIVITY, stated because it exceeds the band: at fixed grid the rl-1
115:          amplitude moves 10.3 dB across cfl 0.2-0.8 (-22.53 -> -12.19 dB) and the
116:          decay 14.7 dB/slot; r is a property of the released scheme AT ITS RELEASED

$ cd /home/user/FableComputer && git status --porcelain | wc -l
0

Not re-executed (budget; no number accepted from these): N = 480 / 720 chain rows; seed 11; J = 0 / −3 / −10…−25 chains; Table 2a matched-amplitude rows and Table 2b; the J = −25 placement rows; cfl 0.2 row; m = 28 depth chain.
```

</details>
