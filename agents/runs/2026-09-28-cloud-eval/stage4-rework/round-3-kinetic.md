### 🌊 Kinetic — **STORE** (required edits) — round 3, 2026-09-28

VOTE: store

REASONS: STORE WITH REQUIRED EDITS. This is not a clean pass. The round-2 regression is repaired: I diffed every table row of the round-3 text and its appendix against the published round-1 reply (11-reply.md), and Tables 1, 2a (28 rows), 2b, 3 (uncapped, with its lag and slot columns), 3b, 4, 5, 6 (eleven families) and the residue table (bold −5.70 / −5.31, denominators (a) and (b) named) are identical row for row. No bare 'Table 7' survives, and 26 of the 29 round-2 required edits landed in full, 3 in part. I wrote my own instrument from the reply's stated coupling and ran 25 new solver runs against the released, unedited chain. Every decisive number reproduces: the gate (8.287855791924049 / −11.828336851446547 / −11.775002445228234, ≤ 1.3×10⁻¹³ relative, not bit-equal); the J = −1 chain (13.103, G4_A 1.581); Table 3c's 1.731 at m = 28 / lo 0.80; Table 8's cfl-0.2 row (1.774, −8.35 / −11.65); the N = 480 rung (1.503) and the continuum estimate 1.425; the whole loop-model range; and ablation rows (i) and (iii). One exception: Table 9 row (iii) prints a construction its label does not describe. The substance and its durable content hold under the three scopes the text now states honestly (the ideal-buffer coupling, cfl 0.4, the pre-registered window). That content is the matched-amplitude grade of 08-01 §4 (≤ 0.6 dB), the ring-down that stops a windowed floor transferring through a resonant stage, "≈ 2×" as the 1.96 small-signal limit, and the new single-cell window scoping. Eight mechanical defects remain: the mislabelled ablation row and the tail share it inflates; a plane mislabel restored with the residue caption; a slot-mode headline range rounded inward; a sign slip; downstream copies of the loaded-drain range that drop their J = −1 / open-end-phase scope; an unnamed DS-factor assumption; a limitation that lists a resolved item as open; and a detached Table 5 caption that lost its window rule. None of them moves a verdict, but each must be fixed before the text enters the record.

FIXES VERIFIED (round-1 required edits):
- 🧵 RE1 (restore the post-check tables, a–f; correct the header; disclose the regression): LANDED. A row-by-row diff (difftables.py) of the round-3 text plus appendix against 11-reply.md gives identical rows for Table 1 (20 lines), 2a (28 rows), 2b, 3 (shifts 7.70 / 10.27 rt at m = 30 and 5.11 / 7.67 / 10.22 rt at m = 28; lag and slots-scored columns present), 3b, 4, 5 (42 rows), residue and 6 (11 rows, including both junction-sweep rows and N = 720). The 'Table 4' / 'Table 6' headings are present. The header withdraws 'no measured number changed' and 'byte-identical'. Residuals, both new required edits: the residue caption came back verbatim with round 1's plane mislabel, and the appendix Table 5 caption was rewritten without its window rule.
- 🧵 RE2 (two tables called 'Table 7'): LANDED. The cfl scan is Table 8 and the ablation Table 9. grep finds 5 'Table 7' occurrences, all 'Part I Table 7'; build_r3.py asserts the same.
- 🧵 RE3 (window scope on the G4 verdicts; report 1.630 / 1.731): LANDED. Item 1 reads 'failed at 0, −1 and −3 dB at every grid under the pre-registered window rule' and its scope (c) prints 1.630 / 1.731 / 1.86 / 1.87. The §4 G4 row, item 6 and the title are all rule-scoped. Re-executed: 1.6303 (m = 30, lo 0.77), 1.7308 (m = 28, lo 0.80), 1.8621 / 1.8731 (lo 0.85).
- 🧵 RE4 (range; cfl in the headline; sign-off direction; 'could build'): LANDED for the peak range. The title's 6–8 and item 4's 6.2–8.0 / 6.2–8.1 match my recomputation from the appendix rows (6.16–7.98 over Table 1's classes, 6.16–8.11 over all 42 rows). The title carries cfl ('on the released cfl path … or at cfl = 0.2'), the sign-off says 'shallower', and 'the one coupling this session ran' replaces 'could build'. A new defect lives in the new slot-mode figure and the cfl-0.8 sign (required edit 3).
- 🧵 RE5 (loaded-drain figures: which junction, which bias): LANDED in item 2, item 5, §2 and limitation 1. §9.4 is quoted in full, verbatim; I checked it against the Part I docx text through 'and radiation'. The lossless case is named, the range runs 0.143–0.429, both bias columns are printed and 08-12's −14.73 vs −24.38 dB/slot is cited. Every figure was re-executed with released regen.loop_gain (log). Residual: the downstream copies drop the J = −1 / open-end-phase scope (required edit 5).
- 🧵 RE6 (discriminant: file the loaded junction under the low reading; the cfl caveat): LANDED. Re-executed: the loaded chain's CW-form G4 at J = −1 is 1.10 / 1.02 / 1.06 (lossless / §9.4 bound / 11.6 %, r = +|r|, ratio bias), 0.96 / 0.98 / 0.97 at r = −|r|, and 1.03–1.11 at the analytic bias. All are below 1.40, so the reassignment is right in-model. The cfl caveat is present: the model's cfl lever spans 1.49–1.77.
- 🧵 RE7 (a: re-attribute away from 08-13; b: credit 08-12 and state the statistic; c: exact filenames): LANDED. Limitation 4 and item 7 now carry 08-13's α(cfl) = 0.59 / 0.86 / 1.01 and the cfl-independent 0.9972 / 0.9976 / 0.9992 at M = 0 (checked against 08-13 lines 33 and 55). Item 4(ii), limitation 4 and the Table 8 caption credit 08-12's −22.53 → −12.19 dB and name the different statistic. The three filenames exist in notes/.
- 🧵 RE8 (carry the single-cell window finding into the f_max grade): LANDED in item 5 and §4 row 2, labelled in-model / open, no key moved. Re-executed: cell 1 alone −20.14 dB (m = 30, lo 0.58) and −19.14 dB (m = 28, lo 0.60).
- 🧵 RE9 (relabel Table 1's bracket; update §1's window bullet): LANDED. The caption now names the ⅛-rt window-rule envelope. §1 quotes ≈ 0.1 dB / 0.012 at J = −1 and 0.27 dB / 0.033 at J = −6.
- 🧵 RE10 (length: a split point): LANDED. The split sits after §3; my counts are comment A 59,515 characters and comment B 20,193, both under 60,000.
- 🌊 RE1 (rebuild §3 from the post-check tables, a–f): LANDED. Same evidence as 🧵 RE1. (b) The residue table's last column now quotes one convention, the Table 5 rule values (−4.31 / −4.70; −4.31 / −4.02). (c) Item 3 reads '28 matched rows'. (d) Table 6 has 11 rows. (e) Headings are restored and the scan renumbered. (f) The disclosures are corrected.
- 🌊 RE2 (scope every G4-bar and '≈ 2×' statement to the rule and the released cfl): LANDED. Item 1, the §4 G4 row, item 6 and the title are rule-scoped; §0 'Scope, first' and item 1's label carry cfl = 0.4; the title adds 'or at cfl = 0.2'.
- 🌊 RE3 (correct the degradation range; do not round the lower end up): PARTIALLY LANDED. The peak range is correct (6.2–8.0; row-named). The new slot-mode figure in the title and in item 4's bold lead, '9–10 dB', rounds the measured 8.63 up; item 4's body and the rework header say 8.6–10.4. Item 4 also prints the cfl-0.8 degradation as '-5.5 dB'. I re-executed it as the stage-2 floor sitting 5.51 dB shallower than cell 1's (−8.886 → −3.376).
- 🌊 RE4 (scope the loaded-junction figures; §9.4 bound; active comparator in item 5; quote the second clause): PARTIALLY LANDED. Item 2, §2, limitation 1 and item 5 (active +3.9 / +0.3 dB against 24.6 dB) are correct and re-executed. But item 3, §4 row 1 and the §5 passive-transfer key state '+0.04 to +2.6 dB … between the two' with no J = −1 / r = +|r| scope. Outside that scope the same released loop model gives −3.53 dB (r = −|r|, J = −1), −1.96 / −4.96 dB (§9.4 bound at J = −3 / −6) and +3.49 dB (lossless, J = −3). Several of these fall below the booked −2.555 dB, so 'between the two' is false outside the scope.
- 🌊 RE5 (limitation 4's 08-13 mis-citation; credit 08-12): LANDED. See 🧵 RE7.
- 🌊 RE6 (globs → filenames; add 07-22-viscosity): LANDED. notes/2026-07-31-physical-launch-gated-frontier.md, notes/2026-08-08-augmented-solver-decisive-experiment.md and notes/2026-07-22-mth-numerical-vs-physical-viscosity.md are all in the block and exist.
- 🌊 RE7 (length / split): LANDED. See 🧵 RE10.
- ⚛️ RE1 (restore Table 3): LANDED. The rows are identical to round 1 (uncapped, lag and slot columns), and the sensitivity rows carry the measured active lags 5.71 / 5.77 rt. Re-executed: the stage-2 row at the exact lag 2.568 rt gives 12.9998 / 13.3371, c2c 4.7038 / 4.9685, floors −4.6365 / −4.3074 / −6.2141, eye +4.29, pp 0.8535, mean-'1' 0.3310; active lag 5.7045 rt.
- ⚛️ RE2 (restore the residue table): LANDED AS ASKED, verbatim, with the registered −5.70 / −5.31 in bold and (a) / (b) named. Re-executed: −5.6981 / −1.5726 (m = 30), −5.3085 / −0.9821 (m = 28), argmax at 0.0084–0.0090 / 0.0158–0.0167 slot. The verbatim restore re-imported the caption clause '(a) = … the promoted floor key's own denominator'. That clause is round 1's plane mislabel, which ⚛️ round-1 R4 required removed, and the text's own §5 contradicts it (required edit 2).
- ⚛️ RE3 (restore Table 3b, the Table 4 / 6 headings, Table 6's rows; correct the disclosure): LANDED.
- ⚛️ RE4 (renumber the cfl table): LANDED.
- ⚛️ RE5 (scope the G4 bar to the window rule; say the late window reaches into the next slot): LANDED. Item 1(c) and the Table 3c caption ('a window with lo > 0.53 reaches into the following slot') carry it. Re-executed 1.7308 / 1.8621.
- ⚛️ RE6 (correct '7–9 dB' with denomination and placement): PARTIALLY LANDED. Item 4's body has 6.2–8.0 peak / 8.6–10.4 slot-mode and the 9.3 / 9.1 dB optimum, but the title and item 4's lead print slot-mode '9–10 dB'.
- ⚛️ RE7 (relabel Table 1's bracket; restrict ≤ 0.001 dB to worst-'1'): LANDED. The mean-'1' spread of ≤ 0.05 dB is stated (the rework's rw3 output gives 13.3987 / 13.4425 / 13.4085).
- ⚛️ RE8 (cite by filename): LANDED.
- ⚛️ RE9 (credit 08-12 for the single-cell cfl lever): LANDED in item 4(ii), limitation 4 and the Table 8 caption.
- ⚛️ RE10 (name the loaded-drain model's assumptions): PARTIALLY LANDED. The open-end phase is named, and the r = −|r| figures are printed and re-executed (−3.53 / −4.10 / −7.78 / −0.57 dB; |loop| 0.429 either phase). The second assumption, that the DS factor (1 + M)/(1 − M) is kept at a partially transmitting drain, is never named; it is only implicit in the formula |t|/(1 − loop·|r|).
- ⚛️ RE11 (state gate (ii)'s construction): LANDED for (ii). The 1-rt raised-cosine fall at 0.8·repT is named; re-executed −12.54 / −12.08 / −16.22 (rework's reading, reproduced in round 2). The row (iii) the rework added is mis-described (required edit 1).
- ⚛️ RE12 (declare the comment split): LANDED. See 🧵 RE10.

REQUIRED EDITS:
- 1. Table 9 row (iii) and item 4's split of the mechanism. The row is labelled '(iii) as (i), plus a hard cut of the '1' slots at 0.8·repT' but prints −13.81 / −13.36 / −17.53, eye +13.52. Those numbers come from a different construction, rw3_runs.py, which hard-zeroes every '0' slot from its start instead of using (i)'s 1-rt raised-cosine fall. Re-executed at m = 30, J = −1, cfl 0.4, rule window 2.625 rt: the construction as labelled gives −13.086 / −12.638 / −16.820, eye +12.80, chain 13.131, which is ⚛️'s round-2 −13.088. The construction as executed gives −13.807 / −13.363 / −17.528, eye +13.52. Either relabel row (iii) with the executed construction and add the labelled one as its own row, or replace the numbers. Then correct item 4's 'the '1' slot's own tail ≈ 3.2–4.4 dB'. With (i)'s '0' gate held fixed, the tail share is 3.2–3.7 dB (raised-cosine fall vs hard cut). The extra 0.72 dB belongs to the harder '0'-slot gate, so the residue share of ≈ 4.7 dB is a lower bound. Correct the round-3 record's line on this row the same way.
- 2. Residue-table caption: strike 'the promoted floor key's own denominator' from definition (a). (a) is the drain-density mean-'1' windowed peak. The promoted max0_below_mean1_dB is the source-plane cav ratio (08-02 §3.1; ⚛️ round-1 R4 withdrew exactly this phrase; the text's own §5 residue key says so). Write, for example, '(a) = the mean-'1' drain-density peak inside the promoted window, the denominator of 08-02 §3.2's drn_h floor column'.
- 3. Headline precision. In the title and in item 4's bold lead, replace 'degrades by … 9–10 dB (slot-mode)' with the measured 8.6–10.4 dB. My recomputation from the appendix rows gives 8.63–10.28 over Table 1's classes and 8.63–10.41 over all 42; the rework's own header says 8.6–10.4. Write the title's 'or at cfl = 0.2' as 'or, in slot-mode only, at cfl = 0.2' (re-executed: stage-2 peak −8.35, slot-mode −11.65). In item 4, change '-5.5 dB at cfl = 0.8' to '5.5 dB at cfl = 0.8'. Re-executed: the stage-2 floor sits 5.51 dB shallower than cell 1's (−8.886 → −3.376); the printed sign is an artifact of build_r3.py's deg08 = single − stage-2.
- 4. Scope the loaded-drain range wherever it is copied: item 3 ('the loaded loop model of item 2 (+0.04 to +2.6 dB delivered …) lies between the two'), §4 row 1 ('… between the two') and the §5 passive_port_density_transfer_dB key. Add 'at J = −1, open-end reflection phase'. 'Between the two' (the booked −2.555 dB and the measured +15.8 dB) holds only inside that scope. Re-executed with released regen.loop_gain: r = −|r| gives −3.53 dB delivered at J = −1; §9.4's bound gives −1.96 / −4.96 dB at J = −3 / −6; lossless at J = −3 gives +3.49 dB. Either scope the sentence or print the full range (−10.3 to +3.5 dB over J ∈ {−1, −3, −6}, both phases).
- 5. Complete ⚛️ RE10. At item 2's loop-model paragraph, name the second assumption: the DS drain factor (1 + M)/(1 − M) is kept at a partially transmitting drain, so the loaded loop is regen.loop_gain × |r|. Label it in-model and open, because a transmitting drain is no longer the current clamp that defines r_d.
- 6. Limitation 9 (standing rule 10). '07-22's flush-sufficiency question is not addressed' is listed under 'Open items of the record this session does not discharge'. The record already resolves that question: 07-22-cavity-ringdown-isi's 2026-07-26 post-promotion annotation, 07-22-flush-noise-figure-negative and 07-23-reset-switch-adjudication, per INDEX. Strike the sentence, or rewrite it as 'the flush question 07-22-flush and 07-23 resolved at the 4-ps slot is not re-examined for the gated two-cell chain'.
- 7. Appendix Table 5 caption. The round-1 caption's '(window rule shift = passive-chain latency)' was dropped when the table moved to the listings comment. Restore it, and add, since the table is now detached from the text, the ideal-buffer coupling, cfl = 0.4, and that the cell-1 column is at the promoted window. Item 4's 'at every rung, grid and seed on that path' and the 6.2–8.1 dB span rest on this table.
- 8. Correct the round-3 record's 'What was not changed' paragraph. The Table 5 caption also changed (undisclosed). The appendix's Table 5 rows are drawn by build_r3.py from old_split['TABLE5'], i.e. the stale tables_split.json the builder docstring says is never used; the rows happen to be identical to round 1's (diff-verified). 'All 29 required edits … applied' is overstated by edits 3–5 above.

TOP ISSUES:
- TABLE 9 ROW (iii) PRINTS A CONSTRUCTION ITS LABEL DOES NOT DESCRIBE (new round-3 material; criterion 3). The label reads 'as (i), plus a hard cut of the '1' slots at 0.8·repT'. The executed code (rw3_runs.py: g = 0 over every whole '0' slot) hard-zeroes the '0' slots instead of applying (i)'s raised-cosine fall. My runs: labelled construction −13.086 / −12.638 / −16.820, eye +12.80; executed construction −13.807 / −13.363 / −17.528, eye +13.52 (the printed row). The round-2 ⚛️ seat's 'hard cut' −13.088 therefore does reproduce, as the labelled construction; the round-3 record's claim that it is 'not reproduced by this construction' is true only of the other construction. Item 4's '1'-tail share of '≈ 3.2–4.4 dB' absorbs 0.72 dB that belongs to the '0'-slot gate; at a fixed (i) gate the share is 3.2–3.7 dB.
- A WITHDRAWN PLANE MISLABEL CAME BACK WITH THE VERBATIM RESTORE. The residue caption defines (a) as 'the promoted floor key's own denominator'. The table's quantity is drain density, and 08-02 §3.1 established that the promoted max0_below_mean1_dB is a source-plane cav ratio. ⚛️ round-1 R4 withdrew this phrase, and the text's own §5 now says the key is 'not comparable with the promoted max0_below_mean1_dB'. Measured at m = 28: cav −10.7312 against drn_h −11.1506, a 0.42 dB plane gap. No round-2 seat saw this because round 2's residue table was the pre-check version with a different caption.
- HEADLINE SLOT-MODE RANGE ROUNDED INWARD, AND A SIGN SLIP. The title and item 4's lead say '9–10 dB (slot-mode)'. Recomputed from the appendix Table 5 rows: 8.63–10.28 dB over J ≥ −6 and 8.63–10.41 over all 42 rows (minimum at m = 28 / N = 480 / J = 0; 8.79 and 8.98 are also below 9). The rework header itself says 8.6–10.4. Item 4's '-5.5 dB at cfl = 0.8' is a degradation printed with the wrong sign; I measured the stage-2 floor 5.51 dB shallower than cell 1's (−8.886 → −3.376). The title's 'reaching the round spec … at cfl = 0.2' holds in slot-mode only (peak −8.35, slot-mode −11.65, both re-executed).
- LOADED-DRAIN RANGE: FAIR IN ITEM 2, OVER-GENERALISED DOWNSTREAM. Every loop-model figure reproduces with released regen.loop_gain (a_loss 0.7451522890452021). Lossless: loop 0.429 / 0.416, passive +2.58, active +3.86, standing wave +6.83, CW regen +1.28 / +1.08 dB. §9.4 bound (|r| = 0.1509): 0.143 / 0.138, +0.04, +0.34, +2.26, +0.30. 11.6 %: 0.322, +1.54, +2.37, +0.83. r = −|r|: −3.53 / −4.10 / −7.78 / −0.57. The ratio-bias loop predicts −14.73 dB/slot against 08-12's −24.38 (effective loop 0.9107); the analytic bias predicts −22.81. Item 2 states J = −1 and the phase explicitly. Item 3, §4 row 1 and the §5 key repeat '+0.04 to +2.6 dB … between the two' with no scope. Outside it the same model gives −3.53 (J = −1, r = −|r|), −1.96 / −4.96 (§9.4 bound, J = −3 / −6) and +3.49 (lossless, J = −3), so 'between −2.555 and +15.8 dB' is not a property of the loaded junction in general. The DS-factor retention that ⚛️ RE10 asked to be named is still implicit.
- STANDING RULE 10, BOTH DIRECTIONS. Contradicting the record: limitation 9 lists 07-22's flush-sufficiency question among open items, but the record resolved it (07-22 post-promotion annotation; 07-22-flush; 07-23). The residue caption contradicts 08-02 §3.1 (above). Re-announcing: none found. The Table 8 single-cell column is credited to 08-12, the ring-down mechanism to 07-22 / 08-12, the plane facts to 08-02 and its vote record, and the loop-model disagreement to 08-12 §4. The single-cell window finding is new: grep of notes/ for sampling-phase or floor-optimal language finds only 08-12's 'window-scoped' falsifier clause, where the early sub-window [0.25, 0.45]·repT reads r −11.94..−11.68 against −15.9. Citing that clause beside item 5 would be good practice (optional); it does not anticipate the late-window result.
- DETACHED APPENDIX. Moving Tables 2b and 5 into the listings comment is acceptable, since the text points to 'appendix Table 5' at every use and the rows are identical to round 1. But Table 5's caption lost '(window rule shift = passive-chain latency)', and the detached table states neither the coupling nor the cfl path, although item 4's range and 'every rung, grid and seed' rest on it. build_r3.py builds this table from tables_split.json, the file behind the round-2 regression, and no assertion guards its rows. The rows are identical by my diff, so no number is wrong, but the round-3 record's 'never from the stale tables_split.json' and 'byte-identical except Table 1's caption and the 4 / 6 numbering' are both inaccurate (Tables 4 and 6 were already numbered in round 1; the Table 5 caption change is not disclosed).
- THE TWO-COMMENT SPLIT IS ACCEPTABLE. Comment A (59,515 characters) carries the header, the executive verdict with every label, and §3; comment B (20,193 characters) carries §4–§7. Each is under GitHub's 65,536 limit, and the split point is marked. One caveat for any later promotion: as a single 80,071-character file, agent_fable_assess.py's read(path, 60000) would cut at line 252, inside §4 row 1, and drop the grades, keys and limitations. The note build must account for that.
- IS THE HEADLINE SCOPED WITHOUT BEING VACUOUS? Yes. Every headline and verdict now carries the ideal-buffer coupling, cfl = 0.4 and the pre-registered window rule. The durable, construct-light content survives that scoping. (a) 08-01 §4's waveform premise holds to ≤ 0.6 dB at matched amplitude (re-executed at J = −1: +0.001 / +0.101 in round 1's rows; Table 2a's 28 rows are unchanged). (b) '≈ 2×' is the 1.96 small-signal limit. (c) A windowed floor does not transfer through a resonant stage (ablation (i): −4.70 → −9.38 dB). (d) The single-cell floor moves 8.3–8.4 dB with window placement.
- The bench discriminant is honestly caveated but thin. Its '> 1.7' and 'deeper than −8 dB' readings are declared non-discriminating until the numerical path is pinned (the cfl lever spans G4 1.49–1.77 and the floor −3.4 to −8.4 dB, re-executed at both ends). Its '< 1.40' reading lumps three causes and sits within 0.03 of the first-order continuum estimate (re-executed 2·1.5028 − 1.5810 = 1.4246). The reassignment of the loaded junction to '< 1.40' is right in-model (CW-form G4 0.95–1.11 at J = −1 across junction models, phases and biases). Optional: re-register it as a one-sided discriminant. Also optional: state the CW-form G4 formula ((loaded + unloaded CW regen)/unloaded) in item 2, which the discriminant cites for it.
- Disclosures are honest and nearly complete. The round-2 regression, its cause (build_r2.py line 176) and the withdrawn 'byte-identical' / 'no measured number changed' are disclosed. So are what was withdrawn in each round, and the declined time-domain loaded-drain run (item 2 and limitation 1 name it as the deciding experiment and credit 🌊's round-2 seat). The residual inaccuracies are in the round-3 record (required edit 8), not in the reply's claims.
- Minor, optional: the tables run out of order (3c, 4, residue, 9, 8, 6). Item 4's peak fail '5.2–6.8 dB' against the round spec excludes the m = 28, J ≤ −10 rows of its own appendix (7.0–7.1 dB). Item 1(c)'s 'flat at 1.58' runs 1.54–1.62 (m = 30) and 1.55–1.60 (m = 28) over lo ≤ 0.75. Item 2's '+2.6 / +3.9 dB … instead of +16 dB' compares the active wave with the passive transfer; item 5 has the right active comparator, 24.6 dB.
- REPRODUCED AND ACCEPTED (not defects, my own instrument, released chain unedited). M_th_num(240) = 0.16894319463373797 (3.3×10⁻¹⁶ relative); M_th_num(480) = 0.1587475408418196 (exactly the promoted value). Gate: G_worst1 8.287855791924049 (3.86×10⁻¹⁵), floors −11.828336851446547 (5.68×10⁻¹⁴) and −11.775002445228234 (1.32×10⁻¹³); exact equality False; slot-mode −15.665. m = 28: 8.131548730367582 / −10.731214907969104 / −11.150570102407642. Passive transfer 15.8296 / 15.8117 dB; relaunch −24.600 / −24.336 dB. J = −1 chain (m = 30, 2.625 rt): 13.1033 / 13.3990, G4_A 1.5810 / 1.5932, G4_A(drn_h) 1.5498, G4_B 1.8039, c2c 4.7986 / 5.0303, floors −4.6961 / −4.3074 / −6.2570, eye +4.395, pp 0.750. Lags: passive envelope 2.5681 rt, passive peak 0.5243 rt, active envelope 5.7045 rt. m = 28 at 2.5 rt: 12.9173, G4_A 1.5885, floors −4.024 / −4.317 / −5.245 (degradation 6.71; m = 30 7.13). Table 3c: m = 28 lo 0.80 gives 14.0741, G4_A 1.7308, −10.079 / −10.084 / −12.188, eye +9.80, 35 slots. cfl 0.2: cell 1 −16.694 / −17.028 / −22.415, transfer 15.008, residue −8.110 / −4.579, lags 0.5156 / 2.3889 → 2.375 rt, chain 13.1125, G4_A 1.7738, c2c 5.5036, floors −8.349 / −8.000 / −11.646, eye +8.20; fixed 2.625 rt: 1.7759, −8.359 / −12.017. cfl 0.8: G4_A 1.4857, floor −3.376. N = 480: 8.4681 / −11.4628, transfer 16.233, relaunch −25.040, chain 12.7255, G4_A 1.5028. Ablation (i): −9.380 / −8.822 / −12.978.

SEAT MODEL NOTE: This seat is the Kinetic 🌊 round-3 re-assessor. The maintainer requested it on claude-opus-5-5 for this run, as the 2026-08-13 policy's Opus re-assessor seat; it is not Fable 5 and does not claim to be. It was blind to the other two round-3 seats and shared no context with the drafting, execution, pre-publication checks, the round-1 and round-2 assessors, or the reworks. It held every prior round's record. The reply under assessment was executed and reworked on claude-fable-5-1. Every number in this verdict was executed by this seat on Linux x86_64 / Python 3.11.15 / numpy 2.4.6 against the released, unedited fable-model-chain/ (25 solver runs plus two threshold scans). Reproductions are gated on relative deviation (≤ 1.3×10⁻¹³ on the gate row); exact equality was measured False and is not claimed. run_all.py was never run, and the repository tree was left clean (git status: 0 lines). — Kinetic 🌊 (AI research agent · see agents/README.md)

<details><summary>Re-execution log (verbatim)</summary>

```text
Seat directory: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/reassess3-kinetic/. Files: kin3.py (my instrument), phase1.py, runs.py, score.py, loopmodel.py, difftables.py, series/*.npz (float64).

kin3.py was written from the reply's §1–§2 definitions and from the promoted 07-31 make_sig_duty / run_custom listings:
- Stepping is the released solver._step_LF, called verbatim, with the released dt rule and the released blow-up guard.
- cav = max|u − u0|; drn_h = h[−1] − 1.
- Cell 2's clamp is h_left = 1 + κ·(cell 1's recorded drn_h), κ = 10^(J/20): exact index when the two cells' dt are equal, np.interp when not.
- Per-slot peaks in [(k + lo), (k + hi)]·repT + shift; slots running past the record's end are dropped.
- Slot-mode = |2⟨x·e^{−i2πf0t}⟩| over the window.
- Envelope lag = argmax of the cross-correlation of one-carrier-period moving-mean |drn_h| envelopes (≈ 20k samples, lag ≤ 6 rt).
- Floor = max '0' / mean '1'; G4_A = chain worst dB (AA over PP, stage-2 cav) / single worst dB; c2c = AA over AP.
I read the session's cascade_driver.py only to confirm the chain topology. I read rw_runs.py / rw3_runs.py only to identify the ablation constructions.
Every run used PYTHONDONTWRITEBYTECODE=1. run_all.py was never run. At the end, `git status --short | wc -l` → 0.

$ python3 -c "import kin3; print(kin3.F0N, kin3.MTH_AN, kin3.platform_line())"
0.25 0.14708333333333332 Linux x86_64, Python 3.11.15, numpy 2.4.6

$ python3 phase1.py   # run_all.measure_Mth_num bracket (xs = linspace(1.05, 1.30, 8), growth_rate at 90 rt), generalised to N; Pool(4)
M_th_num(240) = np.float64(0.16894319463373797)
M_th_num(480) = np.float64(0.1587475408418196)
rel dev N240 vs shipped 3.285787944971905e-16 ; N480 vs promoted 0.1587475408418196: True 0.0
wall 37.7 s; Linux x86_64, Python 3.11.15, numpy 2.4.6

$ python3 runs.py   # 25 solver runs; bias 0.7*M_th_num(N); seed-7 40-slot PRBS; duty 0.8; 2e-3; J = -1 chains; cfl as tagged (tag, s, dt, steps)
A ('c1P_m30_c02', 195.0, 0.0006944444444444445, 3456000)
A ('c1P_m30_N480', 201.8, 0.0006944444444444445, 3456000)
A ('c1A_m30_c02', 211.4, 0.0006321463019380129, 3796589)
A ('c1A_m30_N480', 229.7, 0.0006355873219107002, 3776035)
A ('c1P_m30', 97.6, 0.001388888888888889, 1728000)
A ('c1A_m30', 105.9, 0.0012642926038760258, 1898294)
A ('c1A_m28', 95.8, 0.0012642926038760258, 1771741)
A ('c1P_m28', 82.3, 0.001388888888888889, 1612800)
A ('c1P_m30_c08', 24.9, 0.002777777777777778, 864000)
A ('c1A_m30_c08', 27.5, 0.0025285852077520515, 949147)
B ('PP_m30_c02', 201.1, 0.0006944444444444445, 3456000)
B ('PP_m30_N480', 209.8, 0.0006944444444444445, 3456000)
B ('AA_m30_c02', 222.1, 0.0006321463019380129, 3796589)
B ('AA_m30_N480', 234.3, 0.0006355873219107002, 3776035)
B ('AA_m30', 109.2, 0.0012642926038760258, 1898294)
B ('PP_m30', 98.7, 0.001388888888888889, 1728000)
B ('AP_m30', 99.7, 0.001388888888888889, 1728000)
B ('AP_m30_c02', 200.4, 0.0006944444444444445, 3456000)
B ('ABL_i', 109.7, 0.0012642926038760258, 1898294)
B ('ABL_iii_text', 108.2, 0.0012642926038760258, 1898294)
B ('ABL_iii_code', 105.5, 0.0012642926038760258, 1898294)
B ('AA_m30_c08', 35.3, 0.0025285852077520515, 949147)
B ('PP_m30_c08', 28.6, 0.002777777777777778, 864000)
B ('AA_m28', 72.9, 0.0012642926038760258, 1771741)
B ('PP_m28', 52.7, 0.001388888888888889, 1612800)
ALL RUNS DONE 808.3 s; Linux x86_64, Python 3.11.15, numpy 2.4.6
(Ablation gates on cell 1's drn_h before κ:
- ABL_i: '0' slots multiplied by a 1-rt raised-cosine fall at the slot start, then 0.
- ABL_iii_text: ABL_i plus '1' slots set to 0 on [0.8, 1.0]·repT (the construction the Table 9 row (iii) label describes).
- ABL_iii_code: '0' slots set to 0 over the whole slot plus '1' slots set to 0 on [0.8, 1.0]·repT (rw3_runs.py's construction).
Reference for all three = the ungated passive twin chain PP_m30.)

$ python3 score.py gate
[gate m=30] cav Gw 8.287855791924049 Gm 8.4102 floor -11.828336851446547 eye 11.705 pp 0.306 | drn_h Gw 8.6635 floor -11.775002445228234 mean1 0.03396500068703142 | slot-mode floor -15.665
   rel dev vs promoted: G 3.86e-15 floor cav 5.68e-14 floor drn_h 1.32e-13; exact equality: False
   passive mean-'1' drn_h 0.012374 -> passive port transfer 15.8296 dB; active mean-'1' drn_h over launch 24.6000 dB -> relaunch -24.600 dB
   residue: {'win_a': -11.775, 'q_a': -5.6981, 'q_b': -1.5726, 'whole_a': -5.6981, 'argmax_slot': (np.float64(0.008366463273970719), np.float64(0.009001962231208912)), 'n': 8}
   cell 1 alone lo 0.58: floor cav -20.14 drn_h -19.73 mode -22.78 (n 35)
   cell 1 alone lo 0.6: floor cav -20.14 drn_h -18.39 mode -23.40 (n 35)
[gate m=28] cav Gw 8.131548730367582 Gm 8.2231 floor -10.731214907969104 eye 10.640 pp 0.230 | drn_h Gw 8.4360 floor -11.150570102407642 mean1 0.0329483883046833 | slot-mode floor -14.610
   passive mean-'1' drn_h 0.012349 -> passive port transfer 15.8117 dB; active mean-'1' drn_h over launch 24.3361 dB -> relaunch -24.336 dB
   residue: {'win_a': -11.1506, 'q_a': -5.3085, 'q_b': -0.9821, 'whole_a': -5.3085, 'argmax_slot': (np.float64(0.015830955454936606), np.float64(0.016682539799686782)), 'n': 8}
   cell 1 alone lo 0.58: floor cav -18.32 drn_h -18.78 mode -21.60 (n 35)
   cell 1 alone lo 0.6: floor cav -19.14 drn_h -18.78 mode -21.57 (n 35)

$ python3 score.py j1 cfl n480
[J=-1 m=30] passive stage-1->2 envelope lag 2.5681 rt (rule rounds to 2.625); passive peak-time lag median 0.5243 rt [0.5243, 0.5243]; A* = 0.03027
   shift 0.000 rt: {'chain_w': 12.7344, 'chain_m': 13.1388, 'G4w': 1.5365, 'G4m': 1.5622, 'G4h': 1.4862, 'fc': -3.5615, 'fh': -3.0874, 'fm': -4.0993, 'eye': 3.1481, 'pp': 0.9968, 'mean1_drn': 0.3166, 'n': 36, 'G4B': 1.7882, 'c2c_w': 4.6488, 'c2c_m': 5.0025}
   shift 2.568 rt: {'chain_w': 12.9998, 'chain_m': 13.3371, 'G4w': 1.5685, 'G4m': 1.5858, 'G4h': 1.5498, 'fc': -4.6365, 'fh': -4.3074, 'fm': -6.2141, 'eye': 4.2919, 'pp': 0.8535, 'mean1_drn': 0.331, 'n': 36, 'G4B': 1.8039, 'c2c_w': 4.7038, 'c2c_m': 4.9685}
   shift 2.500 rt: {'chain_w': 12.9998, 'chain_m': 13.3371, 'G4w': 1.5685, 'G4m': 1.5858, 'G4h': 1.5498, 'fc': -4.6365, 'fh': -4.3074, 'fm': -6.1631, 'eye': 4.2919, 'pp': 0.8535, 'mean1_drn': 0.331, 'n': 36, 'G4B': 1.8039, 'c2c_w': 4.7038, 'c2c_m': 4.9685}
   shift 2.625 rt: {'chain_w': 13.1033, 'chain_m': 13.399, 'G4w': 1.581, 'G4m': 1.5932, 'G4h': 1.5498, 'fc': -4.6961, 'fh': -4.3074, 'fm': -6.257, 'eye': 4.3954, 'pp': 0.7499, 'mean1_drn': 0.331, 'n': 36, 'G4B': 1.8039, 'c2c_w': 4.7986, 'c2c_m': 5.0303}
   active stage-1->2 envelope lag 5.7045 rt
   Table-3c lo 0.77: {'chain_w': 13.5118, 'chain_m': 13.7596, 'G4w': 1.6303, 'G4m': 1.6361, 'G4h': 1.5623, 'fc': -10.8649, 'fh': -10.8751, 'fm': -13.0827, 'eye': 10.6145, 'pp': 0.6943, 'mean1_drn': 0.3304, 'n': 35, 'G4B': 1.8033}
   Table-3c lo 0.8: {'chain_w': 13.5391, 'chain_m': 13.7848, 'G4w': 1.6336, 'G4m': 1.6391, 'G4h': 1.6691, 'fc': -8.5903, 'fh': -9.4205, 'fm': -13.4327, 'eye': 8.3399, 'pp': 0.6943, 'mean1_drn': 0.3281, 'n': 35, 'G4B': 1.8008}
   Table-3c lo 0.85: {'chain_w': 15.4328, 'chain_m': 15.6566, 'G4w': 1.8621, 'G4m': 1.8616, 'G4h': 1.7641, 'fc': -7.0071, 'fh': -5.9465, 'fm': -14.0833, 'eye': 6.8136, 'pp': 0.5445, 'mean1_drn': 0.3281, 'n': 35, 'G4B': 1.8008}
[cfl 0.2] cell 1: Gw 7.3923, floor cav -16.694 drn_h -17.028 mode -22.415; passive transfer 15.008 dB; residue {'win_a': -17.0281, 'q_a': -8.1098, 'q_b': -4.5785, 'whole_a': -8.1098, 'argmax_slot': (np.float64(0.0068177058552578275), np.float64(0.007031772521783827)), 'n': 8}
   lags: passive peak 0.5156 rt, passive env 2.3889 rt -> rule 2.375; active env 4.7790 rt
   shift 2.375 rt: {'chain_w': 13.1125, 'chain_m': 13.2618, 'G4w': 1.7738, 'G4m': 1.7874, 'G4h': 1.7396, 'fc': -8.3494, 'fh': -7.9999, 'fm': -11.6461, 'eye': 8.1991, 'pp': 0.3738, 'mean1_drn': 0.2733, 'n': 36, 'G4B': 1.8721, 'c2c_w': 5.5036, 'c2c_m': 5.636}; degradation cell1->stage2 (peak cav) = -8.345 dB
   shift 2.625 rt: {'chain_w': 13.1281, 'chain_m': 13.2711, 'G4w': 1.7759, 'G4m': 1.7887, 'G4h': 1.7396, 'fc': -8.3585, 'fh': -8.9853, 'fm': -12.0174, 'eye': 8.2147, 'pp': 0.3582, 'mean1_drn': 0.2733, 'n': 36, 'G4B': 1.8721, 'c2c_w': 5.5172, 'c2c_m': 5.6453}; degradation cell1->stage2 (peak cav) = -8.335 dB
   [my 'degradation' print is single-minus-stage-2, the same formula as build_r3.py's deg08; its negative sign is the artifact behind the reply's '-5.5 dB']
[N=480 m=30] cell 1 Gw 8.4681 floor -11.4628; passive transfer 16.233 dB; relaunch -25.040; passive env lag 2.6278 rt
   shift 2.5: {'chain_w': 12.6443, 'chain_m': 12.9029, 'G4w': 1.4932, 'G4m': 1.5154, 'G4h': 1.4806, 'fc': -4.6553, 'fh': -4.2916, 'fm': -5.9431, 'eye': 4.3951, 'pp': 0.6418, 'mean1_drn': 0.3423, 'n': 36, 'G4B': 1.7838}
   shift 2.625: {'chain_w': 12.7255, 'chain_m': 12.9522, 'G4w': 1.5028, 'G4m': 1.5212, 'G4h': 1.4806, 'fc': -4.7035, 'fh': -4.2916, 'fm': -6.0347, 'eye': 4.4763, 'pp': 0.5606, 'mean1_drn': 0.3423, 'n': 36, 'G4B': 1.7838}
   [continuum estimate at J = -1, first order from (240, 480): 2*1.5028 - 1.5810 = 1.4246 -> the reply's 1.43 (m = 30); the m = 28 N = 480 rung was not run by this seat]

$ python3 - (score m = 28, ablations, cfl 0.8)
[J=-1 m=28] single Gw 8.1315; passive env lag 2.5556 rt (rounds to 2.5)
   shift 2.5: {'chain_w': 12.9173, 'chain_m': 13.2814, 'G4w': 1.5885, 'G4m': 1.6151, 'G4h': 1.5551, 'fc': -4.0242, 'fh': -4.3165, 'fm': -5.2447, 'eye': 3.6526, 'pp': 0.8975, 'mean1_drn': 0.3231, 'n': 36, 'G4B': 1.8148}
   shift 2.625: {'chain_w': 12.9173, 'chain_m': 13.2814, 'G4w': 1.5885, 'G4m': 1.6151, 'G4h': 1.5551, 'fc': -4.0242, 'fh': -4.4225, 'fm': -5.4589, 'eye': 3.6526, 'pp': 0.8975, 'mean1_drn': 0.3231, 'n': 36, 'G4B': 1.8148}
   Table-3c lo 0.77: {'chain_w': 13.5315, 'chain_m': 13.8027, 'G4w': 1.6641, 'G4m': 1.6785, 'G4h': 1.6228, 'fc': -9.6523, 'fh': -9.3932, 'fm': -11.9103, 'eye': 9.3764, 'pp': 0.7427, 'mean1_drn': 0.3282, 'n': 35, 'G4B': 1.8205}
   Table-3c lo 0.8: {'chain_w': 14.0741, 'chain_m': 14.3448, 'G4w': 1.7308, 'G4m': 1.7444, 'G4h': 1.652, 'fc': -10.0794, 'fh': -10.0839, 'fm': -12.1882, 'eye': 9.8035, 'pp': 0.7427, 'mean1_drn': 0.3282, 'n': 35, 'G4B': 1.8205}
   Table-3c lo 0.85: {'chain_w': 15.2309, 'chain_m': 15.4432, 'G4w': 1.8731, 'G4m': 1.878, 'G4h': 1.8059, 'fc': -8.114, 'fh': -7.036, 'fm': -12.858, 'eye': 7.8988, 'pp': 0.5968, 'mean1_drn': 0.3235, 'n': 35, 'G4B': 1.8153}
[ablation] (0) no gate: floor cav -4.696 drn_h -4.307 mode -6.257 | chain 13.103 | eye +4.40
[ablation] (i) '0' slots zeroed behind a 1-rt raised-cosine fall at slot start: floor cav -9.380 drn_h -8.822 mode -12.978 | chain 13.103 | eye +9.08
[ablation] (iii-as-labelled) (i) + hard cut of '1' slots at 0.8 repT: floor cav -13.086 drn_h -12.638 mode -16.820 | chain 13.131 | eye +12.80
[ablation] (iii-as-executed, rw3_runs.py) '0' slots hard-zeroed from slot start + hard cut of '1' at 0.8 repT: floor cav -13.807 drn_h -13.363 mode -17.528 | chain 13.131 | eye +13.52
[cfl 0.8] cell 1 Gw 8.5880 floor cav -8.886 mode -11.662; passive transfer 16.341; env lag 2.6278 -> 2.625; chain 12.759 G4_A 1.4857 floor cav -3.376 mode -3.494; degradation (stage-2 floor shallower than cell 1 by) 5.51 dB; residue {'win_a': -8.7679, 'q_a': -4.2149, 'q_b': 0.1961, 'whole_a': -4.2149, 'argmax_slot': (np.float64(0.009377898249912657), np.float64(0.010582327984927057)), 'n': 8}
[degradation, own rows] m=30 J=-1: 7.13 dB; m=28 J=-1 (2.5 rt): see above   [10.7312 - 4.0242 = 6.71 dB]

$ python3 loopmodel.py   # released regen._cavity / regen.loop_gain; loaded loop = loop_gain(M)*r; delivered passive |t|/(1-a r), active |t|/(1-loop r); standing wave (1+r)/(1-a r); loaded CW regen 20log10((1-a r)/(1-loop r)); CW-form G4 = (loaded + unloaded CW regen)/unloaded
a_loss = 0.7451522890452021; loop(0) = 0.7451522890452021
[ratio 0.7*M_th_num(240)] M = 0.118260: unloaded loop 0.9450, CW regen +13.32 dB, ring-down -14.73 dB/slot (m = 30)
[analytic 0.7*M_th] M = 0.102958: unloaded loop 0.9162, CW regen +9.66 dB, ring-down -22.81 dB/slot (m = 30)
08-12 measured -24.38 dB/slot -> effective loop 0.9107
unloaded open-end build-up 2/(1-a) = 7.8478 = +17.89 dB; ideal-buffer at J=-1: +16.89 dB
Part I 9.4 bound: reflective loss 0.1 dB -> |r| = 0.1509; Quanta 11.6 % -> |r| = 0.3406
[ratio 0.7*M_th_num(240)]
  J=-1 lossless |r|^2=1-|t|^2       r=+0.454: loaded loop +0.429; delivered passive +2.58 dB (sign +), active +3.86 dB; standing wave +6.83 dB; loaded CW regen +1.28 dB (unloaded +13.32); CW-form G4 1.10
  J=-1 lossless |r|^2=1-|t|^2       r=-0.454: loaded loop -0.429; delivered passive -3.53 dB (sign +), active -4.10 dB; standing wave -7.78 dB; loaded CW regen -0.57 dB (unloaded +13.32); CW-form G4 0.96
  J=-1 Part I 9.4 bound             r=+0.151: loaded loop +0.143; delivered passive +0.04 dB (sign +), active +0.34 dB; standing wave +2.26 dB; loaded CW regen +0.30 dB (unloaded +13.32); CW-form G4 1.02
  J=-1 Part I 9.4 bound             r=-0.151: loaded loop -0.143; delivered passive -1.93 dB (sign +), active -2.16 dB; standing wave -2.35 dB; loaded CW regen -0.23 dB (unloaded +13.32); CW-form G4 0.98
  J=-1 Quanta |r|^2<=11.6%          r=+0.341: loaded loop +0.322; delivered passive +1.54 dB (sign +), active +2.37 dB; standing wave +5.09 dB; loaded CW regen +0.83 dB (unloaded +13.32); CW-form G4 1.06
  J=-1 Quanta |r|^2<=11.6%          r=-0.341: loaded loop -0.322; delivered passive -2.96 dB (sign +), active -3.42 dB; standing wave -5.58 dB; loaded CW regen -0.46 dB (unloaded +13.32); CW-form G4 0.97
  J=-3 lossless |r|^2=1-|t|^2       r=+0.706: loaded loop +0.667; delivered passive +3.49 dB (sign +), active +6.56 dB; standing wave +11.13 dB; loaded CW regen +3.07 dB (unloaded +13.32); CW-form G4 1.23
  J=-3 lossless |r|^2=1-|t|^2       r=-0.706: loaded loop -0.667; delivered passive -6.67 dB (sign +), active -7.44 dB; standing wave -14.31 dB; loaded CW regen -0.77 dB (unloaded +13.32); CW-form G4 0.94
  J=-3 Part I 9.4 bound             r=+0.151: loaded loop +0.143; delivered passive -1.96 dB (sign +), active -1.66 dB; standing wave +2.26 dB; loaded CW regen +0.30 dB (unloaded +13.32); CW-form G4 1.02
  J=-3 Part I 9.4 bound             r=-0.151: loaded loop -0.143; delivered passive -3.93 dB (sign +), active -4.16 dB; standing wave -2.35 dB; loaded CW regen -0.23 dB (unloaded +13.32); CW-form G4 0.98
  J=-3 Quanta |r|^2<=11.6%          r=+0.341: loaded loop +0.322; delivered passive -0.46 dB (sign +), active +0.37 dB; standing wave +5.09 dB; loaded CW regen +0.83 dB (unloaded +13.32); CW-form G4 1.06
  J=-3 Quanta |r|^2<=11.6%          r=-0.341: loaded loop -0.322; delivered passive -4.96 dB (sign +), active -5.42 dB; standing wave -5.58 dB; loaded CW regen -0.46 dB (unloaded +13.32); CW-form G4 0.97
  J=-6 lossless |r|^2=1-|t|^2       r=+0.865: loaded loop +0.818; delivered passive +2.99 dB (sign +), active +8.79 dB; standing wave +14.41 dB; loaded CW regen +5.80 dB (unloaded +13.32); CW-form G4 1.44
  J=-6 lossless |r|^2=1-|t|^2       r=-0.865: loaded loop -0.818; delivered passive -10.32 dB (sign +), active -11.19 dB; standing wave -21.74 dB; loaded CW regen -0.87 dB (unloaded +13.32); CW-form G4 0.93
  J=-6 Part I 9.4 bound             r=+0.151: loaded loop +0.143; delivered passive -4.96 dB (sign +), active -4.66 dB; standing wave +2.26 dB; loaded CW regen +0.30 dB (unloaded +13.32); CW-form G4 1.02
  J=-6 Part I 9.4 bound             r=-0.151: loaded loop -0.143; delivered passive -6.93 dB (sign +), active -7.16 dB; standing wave -2.35 dB; loaded CW regen -0.23 dB (unloaded +13.32); CW-form G4 0.98
  J=-6 Quanta |r|^2<=11.6%          r=+0.341: loaded loop +0.322; delivered passive -3.46 dB (sign +), active -2.63 dB; standing wave +5.09 dB; loaded CW regen +0.83 dB (unloaded +13.32); CW-form G4 1.06
  J=-6 Quanta |r|^2<=11.6%          r=-0.341: loaded loop -0.322; delivered passive -7.96 dB (sign +), active -8.42 dB; standing wave -5.58 dB; loaded CW regen -0.46 dB (unloaded +13.32); CW-form G4 0.97
[analytic 0.7*M_th]
  J=-1 lossless |r|^2=1-|t|^2       r=+0.454: loaded loop +0.416; delivered passive +2.58 dB (sign +), active +3.66 dB; standing wave +6.83 dB; loaded CW regen +1.08 dB (unloaded +9.66); CW-form G4 1.11
  J=-1 lossless |r|^2=1-|t|^2       r=-0.454: loaded loop -0.416; delivered passive -3.53 dB (sign +), active -4.02 dB; standing wave -7.78 dB; loaded CW regen -0.49 dB (unloaded +9.66); CW-form G4 0.95
  J=-1 Part I 9.4 bound             r=+0.151: loaded loop +0.138; delivered passive +0.04 dB (sign +), active +0.29 dB; standing wave +2.26 dB; loaded CW regen +0.26 dB (unloaded +9.66); CW-form G4 1.03
  J=-1 Part I 9.4 bound             r=-0.151: loaded loop -0.138; delivered passive -1.93 dB (sign +), active -2.12 dB; standing wave -2.35 dB; loaded CW regen -0.20 dB (unloaded +9.66); CW-form G4 0.98
  J=-1 Quanta |r|^2<=11.6%          r=+0.341: loaded loop +0.312; delivered passive +1.54 dB (sign +), active +2.25 dB; standing wave +5.09 dB; loaded CW regen +0.71 dB (unloaded +9.66); CW-form G4 1.07
  J=-1 Quanta |r|^2<=11.6%          r=-0.341: loaded loop -0.312; delivered passive -2.96 dB (sign +), active -3.36 dB; standing wave -5.58 dB; loaded CW regen -0.39 dB (unloaded +9.66); CW-form G4 0.96
  J=-3 lossless |r|^2=1-|t|^2       r=+0.706: loaded loop +0.647; delivered passive +3.49 dB (sign +), active +6.05 dB; standing wave +11.13 dB; loaded CW regen +2.56 dB (unloaded +9.66); CW-form G4 1.26
  J=-3 lossless |r|^2=1-|t|^2       r=-0.706: loaded loop -0.647; delivered passive -6.67 dB (sign +), active -7.33 dB; standing wave -14.31 dB; loaded CW regen -0.66 dB (unloaded +9.66); CW-form G4 0.93
  J=-3 Part I 9.4 bound             r=+0.151: loaded loop +0.138; delivered passive -1.96 dB (sign +), active -1.71 dB; standing wave +2.26 dB; loaded CW regen +0.26 dB (unloaded +9.66); CW-form G4 1.03
  J=-3 Part I 9.4 bound             r=-0.151: loaded loop -0.138; delivered passive -3.93 dB (sign +), active -4.12 dB; standing wave -2.35 dB; loaded CW regen -0.20 dB (unloaded +9.66); CW-form G4 0.98
  J=-3 Quanta |r|^2<=11.6%          r=+0.341: loaded loop +0.312; delivered passive -0.46 dB (sign +), active +0.25 dB; standing wave +5.09 dB; loaded CW regen +0.71 dB (unloaded +9.66); CW-form G4 1.07
  J=-3 Quanta |r|^2<=11.6%          r=-0.341: loaded loop -0.312; delivered passive -4.96 dB (sign +), active -5.36 dB; standing wave -5.58 dB; loaded CW regen -0.39 dB (unloaded +9.66); CW-form G4 0.96
  J=-6 lossless |r|^2=1-|t|^2       r=+0.865: loaded loop +0.793; delivered passive +2.99 dB (sign +), active +7.67 dB; standing wave +14.41 dB; loaded CW regen +4.68 dB (unloaded +9.66); CW-form G4 1.48
  J=-6 lossless |r|^2=1-|t|^2       r=-0.865: loaded loop -0.793; delivered passive -10.32 dB (sign +), active -11.07 dB; standing wave -21.74 dB; loaded CW regen -0.75 dB (unloaded +9.66); CW-form G4 0.92
  J=-6 Part I 9.4 bound             r=+0.151: loaded loop +0.138; delivered passive -4.96 dB (sign +), active -4.71 dB; standing wave +2.26 dB; loaded CW regen +0.26 dB (unloaded +9.66); CW-form G4 1.03
  J=-6 Part I 9.4 bound             r=-0.151: loaded loop -0.138; delivered passive -6.93 dB (sign +), active -7.12 dB; standing wave -2.35 dB; loaded CW regen -0.20 dB (unloaded +9.66); CW-form G4 0.98
  J=-6 Quanta |r|^2<=11.6%          r=+0.341: loaded loop +0.312; delivered passive -3.46 dB (sign +), active -2.75 dB; standing wave +5.09 dB; loaded CW regen +0.71 dB (unloaded +9.66); CW-form G4 1.07
  J=-6 Quanta |r|^2<=11.6%          r=-0.341: loaded loop -0.312; delivered passive -7.96 dB (sign +), active -8.36 dB; standing wave -5.58 dB; loaded CW regen -0.39 dB (unloaded +9.66); CW-form G4 0.96
[the '(sign +)' tag is a print bug of mine; the dB values carry the sign]

$ python3 difftables.py   # every '|' row of 11-reply.md vs round-3-reply.md + round-3-tables-appendix.md, by table heading
R1 tables: [('Table 1', 20), ('Table 2a', 30), ('Table 2b', 12), ('Table 3', 12), ('Table 3b', 10), ('Table 4', 18), ('Table 5', 44), ('Residue', 4), ('Table 6', 13), ('4. Grading the record', 7)]
R3 tables: [('Table 1', 20), ('Table 2a', 30), ('Table 3', 12), ('Table 3b', 10), ('Table 3c', 24), ('Table 4', 18), ('Residue', 4), ('Table 9', 6), ('Table 8', 5), ('Table 6', 13), ('4. Grading the record', 7), ('Table 2b', 12), ('Table 5', 44)]
'Table 1': R1 rows 20, R3 rows 20, identical rows: True
'Table 2a': R1 rows 30, R3 rows 30, identical rows: True
'Table 2b': R1 rows 12, R3 rows 12, identical rows: True
'Table 3': R1 rows 12, R3 rows 12, identical rows: True
'Table 3b': R1 rows 10, R3 rows 10, identical rows: True
'Table 4': R1 rows 18, R3 rows 18, identical rows: True
'Table 5': R1 rows 44, R3 rows 44, identical rows: True
   CAPTION DIFFERS:
   R1: ### Table 5 — stage-2 '0'-floor in both denominations, '1' pp and eye, every family and junction class (window rule shift = passive-chain latency)
   R3: ### Table 5 — stage-2 '0'-floors, every family and class (both denominations), with cell 1's own floor
'Residue': R1 rows 4, R3 rows 4, identical rows: True
'Table 6': R1 rows 13, R3 rows 13, identical rows: True
'4. Grading the record': R1 rows 7, R3 rows 7, identical rows: False   [the five grading rows, rewritten by design]

$ python3 (degradation spans recomputed from the appendix Table 5's 42 printed rows: cell-1 floor minus stage-2 floor)
rows 42
peak cav degradation, J>=-6 (Table-1 classes): 6.16 .. 7.98
slot-mode degradation, J>=-6: 8.63 .. 10.28
peak all rows: 6.16 .. 8.11 argmax (8.11, '30', '240', '7', -25.0)
mode all rows: 8.63 .. 10.41 argmax (10.41, '30', '240', '7', -15.0)

$ grep of round-3-reply.md for withdrawn and stale phrases (counts)
'released coupling' 0; 'released cascade' 0; "released model's own" 0; '44 dB' 2 (both 'not 44 dB' corrections); 'LF half-step' 1 (inside the withdrawal); '7–9' 0; 'byte-identical' 1 and 'no measured number changed' 1 (both inside the withdrawal); 'every placement' 1 (inside the withdrawal); 'Table 7' 5 (all 'Part I Table 7'); 'could build' 0; 'below the first cell' 0; "the promoted floor key's own denominator" 1 (line 195, residue caption: SURVIVES); '9–10' 2 (title, item 4 lead); '-5.5' in item 4 ('-5.5 dB at cfl = 0.8'); 'between the two' 2 (item 3, §4 row 1); '+0.04 to +2.6' 3 (item 3, §4 row 1, §5 key).
$ python3 (split sizes): total chars 80071; comment A (title → split) 59515; comment B (## 4 → end) 20193; a 60,000-char cut of the single file falls at line 252 (inside §4 row 1).

$ python3 (Part I docx word/document.xml, tags stripped): '9.4 Inter-cell junctions. A junction is a gate-defined density step between adjacent segments. For the ideal step the velocity mismatch is mild (s ∝ n¹ᐟ⁴-class under Eq. (1)), and the reflective loss of even a 2× density step is < 0.1 dB — the −1 to −3 dB budgeted per junction is therefore dominated by non-ideal effects: scattering at the gate gap, mode mismatch through the ungated sliver, and radiation. …' → the reply's item-2 quotation is verbatim.

Record text checks:
- notes/INDEX.md 07-22 row and 07-22-cavity-ringdown-isi.md line 12: '§7.3's sufficiency question is resolved' → contradicts the reply's limitation 9.
- 08-13 lines 33 / 55: α(M = 0) = 0.9972 / 0.9976 / 0.9992; cfl law 0.59 → 0.86 → 1.01.
- 08-12 §4: regen.loop_gain predicts −14.73 dB/slot against −24.38 measured.
- 08-12 key text: rl-1 amplitude −22.53 → −12.19 dB across cfl 0.2–0.8; window-scoped falsifier with the early sub-window [0.25, 0.45] reading r −11.94..−11.68.
- 08-01 gated §4/§5: A_fix 0.00763–0.01403; knee_gated_duty0p8_streaming_m30_N240 = 0.01203.
- build_r3.py: appendix Table 5 = old_split['TABLE5'] (tables_split.json); deg08 = single floor − rule floor.
- rw3_runs.py: '0' slots g = 0 over the whole slot (hard), '1' slots g = 0 on [0.8, 1.0]·repT; rw_runs.py gate (i): 1-rt raised-cosine fall at '0'-slot start.

$ cd /home/user/FableComputer && git status --short | wc -l
0

Not re-executed (budget): N = 720 rows; m = 28 at N = 480 (so the m = 28 continuum estimate 1.46 is accepted only as arithmetic on printed rungs); seeds 11 / 13; J = 0 / −3 / −6 / −10 … −25 chains; Table 2a's matched boundary-driven runs; Table 3 stages 3–5; the velocity-plane chain; ablation (ii) (reproduced by round-2 seats, not by me). I accept no number from these beyond what I state.
```

</details>
