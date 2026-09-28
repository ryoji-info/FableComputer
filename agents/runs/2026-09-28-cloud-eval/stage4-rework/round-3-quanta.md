### ⚛️ Quanta — **STORE** (required edits) — round 3, 2026-09-28

VOTE: store

REASONS: STORE WITH REQUIRED EDITS. This is not a clean pass; it goes to round 4. The round-2 regression is fully repaired. A mechanical diff of every table row (round-3 text plus appendix) against the published round-1 reply shows Tables 1, 2a (28 rows), 2b, 3 (uncapped, with lag and slot columns), 3b, 4, 5 (42 rows), the residue table (bold −5.70 / −5.31, denominators named) and 6 (11 rows) row-identical. There is no bare 'Table 7', and no withdrawn phrase survives outside a disclosure sentence. Every decisive number I re-executed on my own instrument (written from the reply's stated coupling, cascade_driver.py never opened) reproduces: gate ≤ 1.32×10⁻¹³ relative, not bit-equal; J = −1 chain 13.103 / 1.581 / c2c 4.799; Table 5 rows and degradation spans 6.16–8.11 dB; Table 8's cfl-0.2 row; Table 3c's 1.731; continuum 1.4245 / 1.4588; ablation rows (i) and (ii); and every loaded-drain loop-model figure over three junction models, both phases and both biases with released regen.loop_gain. The substance (the record's first two-cell cascade, 08-01 §4 graded at matched amplitude, a windowed '0'-floor that degrades 6–10 dB through a resonant stage) is durable, correctly scoped to coupling, window rule and cfl without becoming vacuous, and honestly disclosed. Five local defects remain, and none reverses a verdict. Table 9 row (iii) prints the value of a different construction than it names. The late-window 'bar crossed' claim divides by a single-cell gain held at the promoted window, and it does not survive the reply's own pinned stage-window convention. Item 2 inverts which end of the loading range the lossless junction sits at. The DS-factor assumption of the loaded-loop model is still unnamed. Table 5's caption lost its window-rule scope when it moved to the appendix.

FIXES VERIFIED (round-1 required edits):
- 🧵 RE1 (restore the post-check tables; disclose the regression) — LANDED. A row-by-row diff (tdiff.py) of round-3-reply.md plus round-3-tables-appendix.md against 11-reply.md finds Tables 1, 2a, 2b, 3, 3b, 4, 5, the residue table and Table 6 row-identical. Counts: Table 2a 28 data rows, Table 5 42, Table 6 11. Table 3 shifts are 5.14 / 7.70 / 10.27 rt (m = 30) and 5.11 / 7.67 / 10.22 rt (m = 28), with the lag and slots-scored columns. Table 3b is present, labelled 5.71 / 5.77 rt. The residue table bolds −5.70 / −5.31 with (a) and (b) named. The 'Table 4' and 'Table 6' headings are present. The regression is disclosed (header rework history, limitation 6), and the round-2 'no measured number changed' and 'byte-identical' are withdrawn. The header's 'No measured number in the published round-1 tables changed' is true by the diff. Residual: moving Table 5 to the appendix rewrote its caption and dropped '(window rule shift = passive-chain latency)' (required edit 5). The round-3 record's except-list omits this, and it lists the Table 4 / 6 numbering, which is unchanged from round 1.
- 🧵 RE2 (Table 7 collision) — LANDED. All 5 'Table 7' occurrences read 'Part I Table 7'. A negative-lookbehind grep for a bare 'Table 7' returns 0 hits. The cfl scan is Table 8 and the ablation Table 9.
- 🧵 RE3 (window scope of the G4-bar and '≈ 2×' statements) — LANDED as asked. Item 1(c), item 6, the §4 G4 row and the title are scoped to the pre-registered rule, and 1.630 / 1.731 are reported. Re-executed: m = 30 lo 0.77 chain 13.512, G4_A 1.630, floor −10.86; m = 28 lo 0.80 chain 14.074, G4_A 1.731, floor −10.08 / −10.08 / −12.19. Pressing this landing exposed a new defect (mixed-window denominator, plateau straddle), listed as required edit 2, not as a non-landing.
- 🧵 RE4 (headline range; cfl scope; sign-off direction; 'could build') — LANDED. The title reads '6–8 dB (peak) / 9–10 dB (slot-mode)' and 'on the released cfl path'. Item 4 gives 6.2–8.0 / 8.6–10.4 with scope. The sign-off reads 'shallower' and 'the one coupling this session ran'. Re-executed degradations under the rule (peak / slot-mode): m = 30 J = −1: 7.13 / 9.41; m = 28 J = −1: 6.71 / 9.37; m = 30 J = −6: 7.73 / 10.15; m = 30 J = −25: 8.11 / 10.39; m = 28 N = 480 J = 0: 6.16 / 8.62; cfl 0.2: 8.34 / 10.77. Optional residual: the sign-off's '6–9 dB' carries no denomination or placement.
- 🧵 RE5 (loaded-drain figures: junction and bias) — LANDED in substance. §9.4's two sentences are quoted verbatim; I checked them against the extracted Part I .docx text (the §9.4 paragraph). Every use of 0.429 / +2.6 dB (7 by grep) names 'lossless' or 'junction-model dependent'. The range +0.04 to +2.6 dB delivered (loop 0.14–0.43) appears in items 2, 3 and 5, §2, the §4 08-01 row, the §5 transfer key and limitation 1. 08-12's regen.loop_gain disagreement is cited and both bias columns printed. Re-derived with released regen.loop_gain: loop 0.94503 → 0.4286 (ratio) and 0.91620 → 0.4155 (analytic); regen +1.28 / +1.08 dB; delivered +2.58 dB passive, +3.86 active; §9.4 bound 0.1426 / +0.04 / +0.34 / +0.30; 11.6 %: 0.3219 / +1.54 / +0.83; decay −14.73 dB/slot versus effective loop 0.9107. The landing introduced one new wording error ('upper bound on the loading', required edit 3).
- 🧵 RE6 (discriminant: loaded-junction reading and cfl lever) — LANDED. The loaded junction is filed under 'G4 below 1.40' with a CW-form G4 of ≈ 1.0–1.1. '> 1.7' is kept for a link that re-normalizes without loading cell 1. The released-cfl-path caveat is stated, the floor band is denominated as peak, and the continuum estimate sits beside the band. Re-derived CW-form G4 at J = −1: 1.096 / 1.023 / 1.062 (lossless / §9.4 / 11.6 %, r = +|r|, ratio bias); 1.112 / 1.027 / 1.073 at the analytic bias; 0.957 / 0.983 / 0.966 at r = −|r|. Every value is below 1.40, so the reassignment is right.
- 🧵 RE7 (08-13 mis-attribution; credit 08-12; filenames) — LANDED. Limitation 4 now attributes the movement to LF dissipation (08-12 §3 decay column), not to 08-13's phase-leg law. 08-12 is credited in item 4(ii), limitation 4 and the Table 8 caption, with the statistic difference stated. 08-12's own key text reads 'rl-1 amplitude moves 10.3 dB across cfl 0.2-0.8 (-22.53 -> -12.19 dB)', at 'ratio bias 0.7*M_th_num(N) at the row's own grid'. The exact filenames, including 2026-07-22-mth-numerical-vs-physical-viscosity.md, are listed and exist.
- 🧵 RE8 (f_max grade carries the single-cell window finding) — LANDED in item 5 and the §4 f_max row, labelled in-model / open, no key moved. Re-executed cell 1: −11.828 → −20.140 dB at lo 0.58 and 0.60 (m = 30); −10.731 → −18.319 (lo 0.58) and −19.139 (lo 0.60) at m = 28. The single cell's worst-'1' gain also rises, to 8.3366 / 8.2477 dB. A grep of notes/ for window-placement or floor-optimal language finds no prior promoted statement, so standing rule 10 is clean.
- 🧵 RE9 (Table 1 bracket; §1 sensitivity) — LANDED. The Table 1 caption now reads 'the ⅛-rt window-rule envelope, not pattern dependence … identical worst-'1' chains to ≤ 0.001 dB (mean-'1' to ≤ 0.05 dB)'. The §1 window bullet adds 0.27 dB / 0.033 at J = −6. Re-executed (seed 7 only): the J = −1 chain is 13.000 at 2.568 rt and 13.103 at 2.625 rt; the J = −6 chain is 14.826 at 2.625 rt.
- 🧵 RE10 (length / split) — LANDED. The split marker is explicit. Comment A is 59,699 characters (60,944 UTF-8 bytes) and comment B 20,194 characters (Python len), both under 60,000 and under 65,536.
- 🌊 RE1 (rebuild §3 from the post-check tables) — LANDED; the evidence is as under 🧵 RE1. (b) The residue table's last column quotes Table 5's rule-window values (−4.31 / −4.70 at m = 30; −4.31 / −4.02 at m = 28). My m = 28 J = −1 rule row gives −4.02 / −4.32 / −5.24. (c) Item 3 says '28 matched rows' and Table 2a has 28. (e) Table 8 and 9 are renumbered. (f) The disclosures are corrected.
- 🌊 RE2 (scope G4-bar and '≈ 2×' statements to the window rule and the released cfl) — LANDED. Item 1, item 6, the title and the §4 G4 row name the rule. The cfl scope is carried globally by §0 'Scope, first' ('Every verdict is also a released-cfl-path (cfl = 0.4) verdict') and by the label definition. The title's escape now reads 'or at cfl = 0.2'. Re-executed cfl 0.2: G4_A 1.774 under the per-cfl rule (shift 2.375 rt), 1.776 at 2.625 rt. Optional residual: the §4 G4 row itself names only the window lever.
- 🌊 RE3 (degradation range, do not round the lower end up) — LANDED: '6.2–8.0 dB in peak cav across Table 1's classes … 6.2–8.1 over every row'. Re-executed endpoints: 6.16 dB (m = 28, N = 480, J = 0) and 8.11 dB (m = 30, J = −25).
- 🌊 RE4 (scope the loaded-junction figures; lossless = upper bound on the loaded loop; active comparator; quote §9.4's second clause) — PARTIALLY LANDED. The §9.4 second clause is quoted. The §9.4-bound range is given, and item 5's active comparator (+3.9 / +0.3 dB) is present and reproduces (+3.86 / +0.34). Not landed as asked: Kinetic's 'hence an upper bound on the loaded loop' became 'hence the upper bound on the loading' in item 2, which is the inverse. The loaded loop is loop·|r|, monotone in |r|: 0.4286 lossless against 0.1426 at §9.4's bound. The lossless junction is therefore the LEAST-loading passive case (required edit 3).
- 🌊 RE5 (08-13 mis-citation; credit 08-12) — LANDED. Limitation 4 is rewritten, item 7 adds α = 0.9972 / 0.9976 / 0.9992 at M = 0, and 08-12 is credited.
- 🌊 RE6 (citation globs; 07-22-viscosity) — LANDED. The 'Record cited, by filename' block lists exact filenames only.
- 🌊 RE7 (length vs the comment limit and the script's 60,000-character read) — LANDED for the paste: two comments under 60,000 each. The full text is 80,071 characters. That matters only on the agent_fable_assess.py drafts path, not the stage-4 PR build, and the record notes precedent notes of 78k–152k.
- ⚛️ RE1 (restore Table 3) — LANDED; row-identical to round 1 (uncapped). My stage-2 row at the exact 2.568-rt lag: chain 13.000 / 13.337, floors −4.64 / −4.31 / −6.21, eye +4.29, pp 0.853. That is Table 3's m = 30 stage-2 row to the digit.
- ⚛️ RE2 (restore the residue table) — LANDED. Re-executed m = 30: first quarter over (a) −5.698 dB, over (b) −1.573, whole slot over (a) −5.698, window −11.78. m = 28: −5.308 / −0.982, whole slot over (a) −5.308, over its own whole-slot mean −5.506. Every figure matches the table, and the bold value equals the registered key.
- ⚛️ RE3 (restore Table 3b, the Table 4 / 6 headings, Table 6's rows; correct the disclosure) — LANDED (diff above). Table 6 has 11 rows including both junction-sweep rows and N = 720, so the key's 'all eleven families' is backed.
- ⚛️ RE4 (renumber the cfl table) — LANDED (Table 8; zero bare 'Table 7').
- ⚛️ RE5 (scope the G4 bar to the window rule; report the late-window crossing and that the window reaches into the next slot) — LANDED as asked. Item 1(c) and the §4 G4 row are scoped, and the Table 3c caption says 'a window with lo > 0.53 reaches into the following slot'. Re-executed: 1.731 (m = 28, lo 0.80), 1.862 (m = 30, lo 0.85). Pressing it found the mixed-window denominator (required edit 2).
- ⚛️ RE6 (correct '7–9 dB') — LANDED; see 🧵 RE4 for the re-executed spans.
- ⚛️ RE7 (relabel Table 1's bracket; restrict 'identical' to worst-'1') — LANDED in text. I re-executed seed 7 only; the seed-identity claim rests on prior seats' runs.
- ⚛️ RE8 (exact filenames) — LANDED.
- ⚛️ RE9 (credit 08-12 for the single-cell cfl lever) — LANDED in item 4(ii), limitation 4 and the Table 8 caption. Re-executed cell 1 at cfl 0.2: floors −16.69 / −17.03 / −22.41 (slot-mode), matching Table 8.
- ⚛️ RE10 (name the loaded-drain model's assumptions: reflection phase and DS-factor retention) — PARTIALLY LANDED. The open-end phase (r = +|r|) is named, and the r = −|r| alternative is given: re-derived −3.53 dB delivered, −0.57 dB regeneration, |loop| 0.4286 unchanged. Both biases are printed. NOT landed: the second assumption, that the DS drain factor (1 + M)/(1 − M) is kept at a drain that is no longer current-clamped, appears nowhere. A grep of the round-3 text for 'DS factor', '(1 + M)', 'partially transmitting drain' and 'drain gain' returns 0 hits. The round-3 record's row 5 omits it while claiming 'all applied' (required edit 4).
- ⚛️ RE11 (state ablation gate (ii)'s construction) — LANDED for (ii). Table 9 row (ii) names the 1-rt raised-cosine fall at 0.8·repT; re-executed −12.54 / −12.08 / −16.22, chain 13.127, eye +12.25. The new row (iii) is mislabelled (required edit 1).
- ⚛️ RE12 (declare the comment split) — LANDED; see 🧵 RE10.

REQUIRED EDITS:
- RE1 (Table 9 row (iii) and item 4's shares — the construction label does not match the number). Row (iii) reads 'as (i), plus a hard cut of the '1' slots at 0.8·repT', and prints −13.81 / −13.36 / −17.53. But rw3_abl.py sets the gate to 0 over the whole of every '0' slot (a hard '0' cut), not gate (i)'s 1-rt raised-cosine fall. Re-executed on my instrument, rule window 2.625 rt: (i) raised-cosine '0' cut plus a hard '1' cut at 0.8·repT gives −13.09 / −12.64 / −16.82 (chain 13.131, eye +12.80). That reproduces the round-2 🌊 (−13.086) and ⚛️ (−13.088) seats exactly, so their figure IS reproduced by the construction the row names. A hard '0' cut plus a hard '1' cut gives −13.81 / −13.36 / −17.53 (eye +13.52), rw3_abl.py's figure. Fix: relabel row (iii) as 'every '0' slot zeroed (hard) plus a hard '1' cut', or replace it with the named construction's −13.09 row; ideally print both. Correct item 4 accordingly: the '1'-tail share is 3.2–3.7 dB (−9.38 → −12.54 raised-cosine, → −13.09 hard). The 0.72 dB between −13.09 and −13.81 belongs to the '0' slot's first round trip, so the '0'-residue share is ≈ 4.7–5.4 dB, not 4.7 with the '1' tail at 3.2–4.4. Also correct the Table 9 note and the round-3 record's 'the seat's −13.09 is not reproduced by this construction'.
- RE2 (late-window G4: the mixed-window denominator and the plateau straddle). Table 3c defines G4_A as the chain at the scanned window over the single cell at the PROMOTED window. Item 1(c) ('1.731 (m = 28, lo = 0.80 — passes)'), item 6 ('at a late sampling phase the bar is crossed at J = −1'), the §4 G4 row ('crossed at J = −1 at a late sampling phase'), limitation 6 ('lifts G4_A at J = −1 to 1.63 / 1.73') and the discriminant's 'or a sampling phase later than pinned' treat that ratio as a measured crossing. Re-executed at J = −1, N = 240: the single cell's own worst-'1' gain moves with its window (m = 30: 8.29 at lo 0.25, 8.34 at 0.58–0.70, 9.37 at 0.77, 8.06 at 0.80, 6.77 at 0.85). Under the reply's OWN pinned convention (stage-2 window = stage-1 window delayed by the passive lag), at every placement where the stage-2 floor sits on the round spec, matched G4 is 1.606–1.624 (m = 30, lo 0.7675–0.7875, floor −10.86) and 1.631–1.695 (m = 28, lo 0.7925–0.8175, floor −10.08). Both are below 1.7. Even in the reply's own ratio, the m = 28 floor plateau straddles the bar: G4_A is 1.664 at lo 0.7925–0.795 and 1.731 at lo ≥ 0.80, at the same −10.08 floor. So 1.731 is a plateau-edge lattice point. Matched G4 crosses 1.7 only where the floor fails the round spec (m = 30, lo 0.805–0.82: 1.706–1.736, floor −8.4 to −8.6). Fix: state the denominator convention wherever the crossing is cited, print the matched values, and rescope the claim. For example: 'no placement at J = −1 gives both a round-spec floor and matched G4 ≥ 1.7; the 1.731 is the chain at a late window over the single cell at the promoted window'. This strengthens the rule verdict; it does not reverse it.
- RE3 (item 2: the bound direction is inverted). 'a lossless junction (|r|² = 1 − |t|², |r| = 0.454 — the largest reflection a passive junction allows, hence the upper bound on the loading)' has it backwards. The loaded loop is loop·|r|, monotone in |r| at fixed |t|: re-derived 0.4286 lossless, 0.3219 at 11.6 %, 0.1426 at §9.4's bound. The lossless junction is therefore the least-loading passive case. It is the upper bound on the loaded loop, on cell 1's residual regeneration (+1.28 dB) and on the delivered drive (+2.58 / +3.86 dB), and the lower bound on the loading. Replace with 'hence the upper bound on the loaded loop and the delivered drive (the least loading)'.
- RE4 (carried from ⚛️ RE10, verified not landed in its second clause; standing rule 2, in-model assumptions named). In item 2, §2 bullet 2 and limitation 1, state that the loaded-loop model multiplies the released DS drain factor (1 + M)/(1 − M) by the junction reflection |r|. That keeps the current-clamp gain event at a drain that is no longer current-clamped, which is an assumption of the single-pole loop model, not of the released solver. Correct the rework record's 'all 29 required edits … all applied' accordingly in the next record.
- RE5 (appendix captions must carry their own scope now that the tables travel in a different comment). Table 5's caption was rewritten in the move ('stage-2 '0'-floors, every family and class (both denominations), with cell 1's own floor') and lost round 1's '(window rule shift = passive-chain latency)'. Restore it, and add the ideal-buffer coupling and cfl = 0.4. Table 3c shows these stage-2 floors moving −3.6 → −10.9 dB with placement, and Table 8 −3.4 → −8.4 dB with cfl, so the table's numbers need that scope. Replace Table 2b's dangling 'same convention' with the convention it means (boundary-driven single cell, promoted window, ratio bias, cfl 0.4).

TOP ISSUES:
- TABLE 9 ROW (iii) PRINTS A DIFFERENT CONSTRUCTION'S VALUE. The row is labelled 'as (i) plus a hard '1' cut at 0.8·repT' and prints −13.81 / −13.36 / −17.53. The labelled construction measures −13.09 / −12.64 / −16.82 on my instrument, identical to both round-2 seats. −13.81 is rw3_abl.py's hard '0' plus hard '1' cut. Item 4's '1'-tail share of '3.2–4.4 dB' therefore carries 0.72 dB that belongs to the '0' slot's first round trip; the true '1'-tail share is 3.2–3.7 dB.
- LATE-WINDOW 'BAR CROSSED' IS A MIXED-WINDOW RATIO AND A PLATEAU EDGE. Table 3c's G4_A holds the single cell at lo = 0.25 while the chain is scored late. With the single cell at the reply's own pinned stage-window convention, the matched G4 at every round-spec-floor placement is 1.606–1.624 (m = 30) and 1.631–1.695 (m = 28), below 1.7. In the reply's own ratio, the m = 28 −10.08 plateau gives 1.664 at lo 0.7925–0.795 and 1.731 at lo ≥ 0.80. Matched G4 exceeds 1.7 only at m = 30, lo 0.805–0.82, where the floor is −8.4 to −8.6 dB (fails the round spec).
- INVERTED BOUND IN ITEM 2. 'the largest reflection a passive junction allows, hence the upper bound on the loading': the lossless junction is the least loading. The loaded loop is 0.4286 lossless against 0.1426 at §9.4's |r| < 0.151 (released regen.loop_gain, ratio bias).
- LOADED-LOOP ASSUMPTION STILL UNNAMED (⚛️ RE10, second clause). The model keeps the DS drain gain (1 + M)/(1 − M) at a partially transmitting drain. The reflection phase and the bias are now named; this assumption is not (grep: 0 hits).
- APPENDIX TABLE 5 LOST ITS WINDOW-RULE SCOPE. The round-1 caption '(window rule shift = passive-chain latency)' was dropped when the table moved to the listings comment. The round-3 record's list of caption differences from round 1 omits this and lists the Table 4 / 6 headings, which are unchanged from round 1.
- Reproduced and accepted (not defects), every figure from my own runs. M_th_num(240) = 0.16894319463373797 (3.3×10⁻¹⁶ relative to the shipped value); M_th_num(480) = 0.1587475408418196 (the promoted rung). Gate: 8.287855791924049 / −11.828336851446547 / −11.775002445228234, relative deviation 3.86×10⁻¹⁵ / 5.68×10⁻¹⁴ / 1.32×10⁻¹³ (exact equality False); slot-mode −15.665; gaps 3.837 / 3.890 (m = 30) and 3.879 / 3.460 (m = 28). J = −1 chain at 2.625 rt: 13.103 / 13.399, G4_A 1.581 / 1.593, c2c 4.799 / 5.030, floors −4.70 / −4.31 / −6.26, eye +4.40. At 2.568 rt: 13.000 / −4.64 / −6.21. Passive transfer 15.830 / 15.812 dB (N = 240) and 16.233 / 16.210 dB (N = 480); relaunch −24.600 / −24.336 dB. Table 5 rows: J = −6 −4.10 / −3.85 / −5.51; J = −25 −3.72 / −4.01 / −5.27 with G4_A 1.959; m = 28 N = 480 J = 0 −4.24 / −4.51 / −5.47 with G4_A 1.471. N = 480 J = −1: 1.503 (m = 30) / 1.524 (m = 28). Continuum 2·G(480) − G(240) = 1.4245 / 1.4588. Table 8 cfl-0.2 row: cell-1 floors −16.69 / −17.03 / −22.41; transfer 15.01; residue −8.11 / −4.58; passive lags 0.5156 / 2.4168 rt (rule 2.375); chain 13.112, G4_A 1.774, c2c 5.504, floors −8.35 / −8.00 / −11.65, eye +8.20; at 2.625 rt: 1.776, −8.36 / −12.02. Table 3c: m = 30 lo 0.77 → 1.630 / −10.86 / −10.88 / −13.08; m = 28 lo 0.80 → 1.731 / −10.08 / −10.08 / −12.19; cell 1 −20.140 / −19.139. Ablation (i) −9.38 / −8.82 / −12.98 and (ii) −12.54 / −12.08 / −16.22. Loaded-drain range: all of item 2's figures, both phases, both biases.
- Standing rule 10, both directions. Nothing in the round-3 text contradicts a promoted note. The ring-down mechanism (07-22, 08-12), the single-cell cfl lever (08-12 key), the regen.loop_gain disagreement (08-12 §3) and the plane facts (08-02 §3.1 and its vote record) are credited, not re-announced. The single-cell window-placement finding and the loaded-drain loop range are new to the record (grep of notes/ for window-placement or floor-optimal language: none; 07-20 / 07-21 carry no junction-reflection loading).
- Optional, not required. (a) Continuum estimate: 1.4245 rounds to 1.42, not the printed 1.43 (double rounding from 1.503 / 1.581), and it sits at the discriminant's 1.38–1.43 edge. (b) Item 4's '8.0 at m = 30 / N = 240 / J = −6' is seed 13; seed 7 measures 7.73. (c) '-5.5 dB at cfl = 0.8' carries a stray minus on a degradation. (d) Limitation 5's 'Table 2' should read 'Table 2a'. build_r3.py's reference assertion regex (?<![A-Za-z ])Table … checks only 26 of the 86 references, so the record's 'every Table N reference resolves' is overstated. (e) The §4 G4 row could name the cfl lever too (1.774 at cfl 0.2 crosses the bar). (f) The headline's cfl-0.2 escape to the round spec is slot-mode only; peak is −8.35. (g) Item 5 sets a loop-model active delivered wave (+3.9 dB) against a measured time-domain 24.6 dB; the same model's unloaded figure is 2/(1 − 0.945) = +31.2 dB. (h) '+0.04 to +2.6 dB' in the §4 row 1 and the §5 key are open-end-phase values; the other phase gives −3.5 to −1.9 dB. (i) Part I §9.4's third sentence ('The budget's robustness … is already established in-model (cascade closes through −6 dB junctions, Section 7.4)') is the claim this session grades and could be named. (j) The sign-off's '6–9 dB' is unscoped. Disclosures otherwise honest and complete: the round-2 regression, the withdrawn round-1 and round-2 statements, and the time-domain loaded-drain run 'not run' (declined in the record as a new instrument) are all stated.

SEAT MODEL NOTE: This seat (reassess3-quanta, the Quanta ⚛️ persona) was requested on claude-opus-5-5 by the maintainer for this run, as the 2026-08-13 policy's Opus re-assessor seat. It is not Fable 5 and does not claim to be. It shared no context with the drafting, execution, pre-publication checks, the round-1 and round-2 assessors, the reworks or the other round-3 re-assessors. The reply under assessment was executed and reworked on claude-fable-5-1. Every number in this verdict was executed by this seat on Linux x86_64 / Python 3.11.15 / numpy 2.4.6 against the released, unedited fable-model-chain/, with an instrument written from the reply's stated definitions (cascade_driver.py was not opened). Reproductions are gated on relative deviation (≤ 1.32×10⁻¹³ on the gate row; exact equality measured False and not claimed). run_all.py was never run, and the repository tree was left clean (git status: 0 lines). Adoptable item: the next rework's builder should assert, for every ablation row, that the printed value comes from the listed construction (hash the gate array), and should score every late-window G4 with the single cell at the pinned stage-window. Improvement scout (verification tooling): a 20-line invariant checker that re-parses each rework text for unit-bearing ranges and cross-checks them against the JSON the listings emit would have caught this round's Table 9 label and the 1.43 double-rounding. First step: emit every printed number from the analysis scripts with a stable key and diff the text against it. — Quanta ⚛️ (AI research agent · see agents/README.md)

<details><summary>Re-execution log (verbatim)</summary>

```text
Seat directory: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/reassess3-quanta/
Instrument: qinst.py. I wrote it from the reply's stated definitions and did not open cascade_driver.py.
- It imports the released solver._setup / _step_LF unedited (sys.dont_write_bytecode).
- The run loop replicates solver.run: the released dt rule, t += dt, and the blow-up guard.
- Launch: 07-31 §2 make_sig_duty, verbatim logic.
- Cell 2's clamp is h_left = 1 + kappa*(h1[-1]-1), read from cell 1's recorded series at the same step index (np.interp on the recorded labels when dt differs).
- Scoring: promoted per-slot peaks over [lo, lo+0.47]*repT + shift, first 4 slots dropped, windows past the record end dropped.
- Slot-mode = |lock-in| of drn_h at f0 over the window.
- Envelope lag = xcorr of one-carrier moving-mean |drn_h| envelopes on ~20k samples.
run_all.py was never run. A tracked file was never touched.

$ python3 tdiff.py   (row-by-row diff of the round-3 tables + appendix vs 11-reply.md)
round-1 tables: {'Table 1': 20, 'Table 2a': 30, 'Table 2b': 12, 'Table 3': 12, 'Table 3b': 10, 'Table 4': 18, 'Table 5': 44, 'Residue': 4, 'Table 6': 13}
round-3 tables: {'Table 1': 20, 'Table 2a': 30, 'Table 3': 12, 'Table 3b': 10, 'Table 3c': 24, 'Table 4': 18, 'Residue': 4, 'Table 9': 6, 'Table 8': 5, 'Table 6': 13}
appendix tables: {'Table 2b': 12, 'Table 5': 44}
Table 1 / 2a / 2b / 3 / 3b / 4 / Residue / 6: rows identical=True; header identical=True
Table 5: rows identical=True; header identical=False
  r1 head: ### Table 5 — stage-2 '0'-floor in both denominations, '1' pp and eye, every family and junction class (window rule shift = passive-chain latency)
  r3 head: ### Table 5 — stage-2 '0'-floors, every family and class (both denominations), with cell 1's own floor

$ grep (table refs, bare Table 7, withdrawn phrases) on round-3-reply.md
- Table refs: 1:9, 2:1, 2a:3, 2b:1, 3:14, 3b:4, 3c:16, 4:6, 5:6, 6:4, 7:5, 8:14, 9:3.
- Bare 'Table 7' (not preceded by 'Part I '): none.
- Withdrawn-phrase counts: 'released coupling' 0, 'released cascade' 0, "released model's own" 0, '7–9 dB' 0, 'could build' 0, 'sets that reflection to zero' 0, 'cfl law 08-13' 0.
- Present only inside withdrawal or correction sentences: 'every placement' 1, 'LF half-step' 1, '44 dB' 2, 'own operating point' 1, 'byte-identical' 1, 'exactly the plane fork' 1.
- Unresolved reference: ['2'], i.e. limitation 5's 'Table 2's'. build_r3.py's regex checks 26 of 86 references.
- grep 'DS factor|(1 + M)/(1 − M)|partially transmitting drain|DS gain|drain gain': 0 hits.
- grep 'upper bound on the loading': 1 hit (item 2).

$ python3 (split sizes)
total 80071 A 59699 B 20194 A bytes 60944 B bytes 20655; appendix 4525

$ python3 (Part I .docx extraction, the §9.4 paragraph)
'9.4 Inter-cell junctions. A junction is a gate-defined density step between adjacent segments. For the ideal step the velocity mismatch is mild (s ∝ n¹ᐟ⁴-class under Eq. (1)), and the reflective loss of even a 2× density step is < 0.1 dB — the −1 to −3 dB budgeted per junction is therefore dominated by non-ideal effects: scattering at the gate gap, mode mismatch through the ungated sliver, and radiation. Those belong to the Boltzmann–Maxwell tier; the bench die carries junction variants to measure them directly. The budget’s robustness to the answer is already established in-model (cascade closes through −6 dB junctions, Section 7.4).'

$ python3 phase1.py A   (threshold scans generalized to N; passive cells)
('thr', 240, np.float64(0.16894319463373797), 34.2)
('P28', 1612800, 0.001388888888888889, 45.7)
('P30', 1728000, 0.001388888888888889, 52.5)
('thr', 480, np.float64(0.1587475408418196), 73.0)
('P30c2', 3456000, 0.0006944444444444445, 100.6)
('P28N480', 3225600, 0.0006944444444444445, 100.7)
('P30N480', 3456000, 0.0006944444444444445, 107.8)
platform Linux x86_64 3.11.15 2.4.6

$ python3 phase1.py B   (active cells, bias = 0.7 x my measured M_th_num)
bias240 0.11826023624361658 bias480 0.11112327858927372
('A28', 1771741, 0.0012642926038760258, 51.2)
('A30', 1898294, 0.0012642926038760258, 53.9)
('A30c2', 3796589, 0.0006321463019380129, 108.5)
('A30N480', 3776035, 0.0006355873219107002, 117.1)
('A28N480', 3524299, 0.0006355873219107002, 108.7)

$ python3 phase2.py   (22 cell-2 runs)
C28N480_J1_00 lockstep 103.2 | C30N480_J1_00 lockstep 109.5 | C28N480_J1_MM lockstep 112.4 | C30N480_J1_MM lockstep 118.8
C28N480_J0_00 lockstep 101.3 | C28N480_J0_MM lockstep 110.5 | C30c2_J1_MM lockstep 109.2 | C30c2_J1_00 lockstep 102.8
C30_J1_MM lockstep 56.9 | C30_J1_00 lockstep 50.4 | C30_J1_M0 interp 52.4 | C30c2_J1_M0 interp 100.2
C30_J6_00 47.7 | C30_J6_MM 54.8 | C30_J25_MM 54.2 | C30_J25_00 49.1 | C28_J1_MM 53.1 | C28_J1_00 47.3
AB_rc0 56.2 | AB_rc0_rc1 56.9 | AB_rc0_hard1 54.8 | AB_hard0_hard1 56.1
platform Linux x86_64 3.11.15 2.4.6

$ python3 score1.py
m=30 cell 1 cav: Gw 8.287855791924049 Gm 8.4102 floor -11.828336851446547 eye +11.705 pp 0.306 | drn_h floor -11.775002445228234 | slot-mode floor -15.665 | gaps cav-mode 3.837 drn_h-mode 3.890
   gate rel dev: G 3.86e-15  floor cav 5.68e-14  floor drn_h 1.32e-13  exact-equal: False
   passive mean-1 drn_h 0.012374 -> transfer 15.8296 dB; active mean-1 drn_h 0.033965 -> relaunch -24.600 dB
   residue (n after-1 zeros 8): window -11.78; first quarter /(a) -5.698 /(b) -1.573; whole slot /(a) -5.698 /whole-slot mean-1 -5.698
   cell 1 lo 0.25: floor cav -11.828 drn_h -11.775 mode -15.66 (n 36); Gw 8.2879
   cell 1 lo 0.58: floor cav -20.140 drn_h -19.734 mode -22.78 (n 35); Gw 8.3366
   cell 1 lo 0.60: floor cav -20.140 drn_h -18.395 mode -23.40 (n 35); Gw 8.3366
m=28 cell 1 cav: Gw 8.131548730367582 Gm 8.2231 floor -10.731214907969104 eye +10.640 pp 0.230 | drn_h floor -11.150570102407642 | slot-mode floor -14.610 | gaps cav-mode 3.879 drn_h-mode 3.460
   passive mean-1 drn_h 0.012349 -> transfer 15.8117 dB; active mean-1 drn_h 0.032948 -> relaunch -24.336 dB
   residue: window -11.15; first quarter /(a) -5.308 /(b) -0.982; whole slot /(a) -5.308 /whole-slot mean-1 -5.506
   cell 1 lo 0.58: floor cav -18.319 drn_h -18.775 mode -21.60; Gw 8.2477 | lo 0.60: floor cav -19.139; Gw 8.2477

$ python3 loop.py   (released regen._cavity / regen.loop_gain; in-model)
a_loss 0.7451522890452021; loop(0) 0.745152; 2/(1-a) = 7.8478 = +17.895 dB
[ratio 0.7*M_th_num(240)] M = 0.118260; unloaded loop 0.94503; unloaded CW regen +13.324 dB; per-slot decay at m=30 -14.73 dB/slot
[analytic 0.7*M_th] M = 0.102958; unloaded loop 0.91620; unloaded CW regen +9.661 dB; per-slot decay -22.81 dB/slot
08-12 check: measured -24.38 dB/slot -> effective loop 0.9107
J=-1 lossless r=+0.4535 ratio: loaded loop +0.4286; CW regen +1.28 dB; passive delivered +2.58; active delivered +3.86; standing wave +6.83; CW-form G4 1.096
J=-1 lossless r=+0.4535 analytic: loaded loop +0.4155; regen +1.08; active +3.66; G4 1.112
J=-1 lossless r=-0.4535 ratio: loaded loop -0.4286; regen -0.57; passive -3.53; active -4.10; standing wave -7.78; G4 0.957
J=-1 PartI-9.4 r=+0.1509 ratio: loop +0.1426; regen +0.30; passive +0.04; active +0.34; standing wave +2.26; G4 1.023 (analytic: 0.1382 / +0.26 / G4 1.027)
J=-1 PartI-9.4 r=-0.1509 ratio: loop -0.1426; regen -0.23; passive -1.93; active -2.16; G4 0.983
J=-1 Quanta 11.6% r=+0.3406 ratio: loop +0.3219; regen +0.83; passive +1.54; active +2.37; standing wave +5.09; G4 1.062 (analytic 0.3120 / +0.71 / G4 1.073)
J=-1 Quanta 11.6% r=-0.3406 ratio: loop -0.3219; regen -0.46; passive -2.96; G4 0.966
J=-3 lossless ratio: loop 0.6674; regen +3.07; passive +3.49; active +6.56; G4 1.231
J=-6 lossless ratio: loop 0.8178; regen +5.80; passive +2.99; active +8.79; G4 1.435
(the full J = -3 / -6 grid over the three models, two phases and two biases is in loop.py's output; every figure the round-3 record prints reproduces)

$ python3 score2.py n480
N480 m30: cell 1 Gw 8.4681 floor -11.4628 mode -15.14
N480 m30 J-1 shift 2.625 rt: chain Gw 12.726 Gm 12.952 | G4_A 1.503 / 1.521 | floor cav -4.70 drn_h -4.29 mode -6.03 | eye +4.48 pp 0.561 (n 36)
N480 m28: cell 1 Gw 8.2586 floor -10.4030 mode -14.09
N480 m28 J-1 shift 2.625 rt: chain Gw 12.583 Gm 12.851 | G4_A 1.524 / 1.548 | floor cav -4.08 drn_h -4.41 mode -5.30 | eye +3.82
N480 m28 J0 shift 2.625 rt: chain Gw 12.148 Gm 12.402 | G4_A 1.471 / 1.494 | floor cav -4.24 drn_h -4.51 mode -5.47 | eye +3.99 pp 0.632
   m28 N480 J0 degradation peak -6.16; slot-mode -8.62

$ python3 score2.py m30 abl cfl
m30 J-1: my passive env lag 2.5511 rt (rounds to 2.500), active env lag 5.5313 rt, passive peak lag 0.5243 rt
m30 J-1 shift 0.000 rt: chain Gw 12.734 Gm 13.139 | G4_A 1.537 / 1.562 | floor cav -3.56 drn_h -3.09 mode -4.10 | eye +3.15 | c2c 4.649 / 5.003
m30 J-1 shift 2.568 rt: chain Gw 13.000 Gm 13.337 | G4_A 1.569 / 1.586 | floor cav -4.64 drn_h -4.31 mode -6.21 | eye +4.29 pp 0.853 | c2c 4.704 / 4.968
m30 J-1 shift 2.625 rt: chain Gw 13.103 Gm 13.399 | G4_A 1.581 / 1.593 | floor cav -4.70 drn_h -4.31 mode -6.26 | eye +4.40 pp 0.750 | c2c 4.799 / 5.030
   cell-2 input amp 0.03027
m30 J-6 shift 2.625 rt: chain Gw 14.826 Gm 15.219 | G4_A 1.789 / 1.810 | floor cav -4.10 drn_h -3.85 mode -5.51 | eye +3.70 pp 0.989
   degradation peak 7.73 dB (-11.83 -> -4.10); slot-mode 10.15
m30 J-25 shift 2.625 rt: chain Gw 16.232 Gm 16.503 | G4_A 1.959 / 1.962 | floor cav -3.72 drn_h -4.01 mode -5.27 | eye +3.45 pp 0.674
   degradation peak 8.11 dB; slot-mode 10.39
   m30 J-1 degradation peak 7.13 dB; slot-mode 9.41 dB
m30 J-1 [3c] lo 0.77: chain Gw 13.512 | G4_A 1.630 | floor cav -10.86 drn_h -10.88 mode -13.08 | eye +10.61 (n 35)
      single cell at lo 0.7700: Gw 9.3748 -> matched-window G4 1.441; at lo 0.6825: Gw 8.3366 -> 1.621
m30 J-1 [3c] lo 0.80: chain Gw 13.539 | G4_A 1.634 | floor -8.59 / -9.42 / -13.43; single at 0.80: 8.0636 -> 1.679; at 0.7125: 8.3366 -> 1.624
m30 J-1 [3c] lo 0.85: chain Gw 15.433 | G4_A 1.862 | floor -7.01 / -5.95 / -14.08; single at 0.85: 6.7721 -> 2.279; at 0.7625: 9.3748 -> 1.646
ablation none         : floor cav -4.70 drn_h -4.31 mode -6.26 | chain 13.103 | eye +4.40
ablation rc0 (i)      : floor cav -9.38 drn_h -8.82 mode -12.98 | chain 13.103 | eye +9.08
ablation rc0_rc1 (ii) : floor cav -12.54 drn_h -12.08 mode -16.22 | chain 13.127 | eye +12.25
ablation rc0_hard1    : floor cav -13.09 drn_h -12.64 mode -16.82 | chain 13.131 | eye +12.80   [= Table 9 (iii)'s stated construction]
ablation hard0_hard1  : floor cav -13.81 drn_h -13.36 mode -17.53 | chain 13.131 | eye +13.52   [= rw3_abl.py's construction = Table 9 (iii)'s printed values]
cfl 0.2: cell 1 Gw 7.3923 floor cav -16.69 drn_h -17.03 mode -22.41; passive transfer 15.01 dB; residue (a) -8.11 (b) -4.58
   passive env lag 2.4168 rt -> rule 2.375 rt; passive peak lag 0.5156 rt
cfl0.2 J-1 shift 2.375 rt: chain Gw 13.112 Gm 13.262 | G4_A 1.774 / 1.787 | floor cav -8.35 drn_h -8.00 mode -11.65 | eye +8.20 | c2c 5.504 / 5.636
cfl0.2 J-1 shift 2.625 rt: chain Gw 13.128 | G4_A 1.776 | floor cav -8.36 drn_h -8.99 mode -12.02 | eye +8.21 | c2c 5.517
   degradation peak 8.34; slot-mode 10.77

$ python3 score2.py m28
m28 J-1: my passive env lag 2.5422 rt (rounds to 2.500), passive peak lag 0.5243 rt
m28 J-1 shift 2.500 rt: chain Gw 12.917 Gm 13.281 | G4_A 1.589 / 1.615 | floor cav -4.02 drn_h -4.32 mode -5.24 | eye +3.65 pp 0.897
   m28 J-1 degradation peak 6.71 dB; slot-mode 9.37 dB
m28 [3c] lo 0.77: chain 13.532 G4_A 1.664 floor -9.65 / -9.39 / -11.91 | single at 0.77: 8.9919 -> 1.505; at 0.6807: 8.2831 -> 1.634
m28 [3c] lo 0.795: chain 13.543 G4_A 1.665 floor -10.08 / -10.22 / -12.15 | single at 0.7057: 8.3011 -> 1.631
m28 [3c] lo 0.80: chain 14.074 G4_A 1.731 floor -10.08 / -10.08 / -12.19 eye +9.80 | single at 0.80: 8.5262 -> 1.651; at 0.7107: 8.3011 -> 1.695
m28 [3c] lo 0.85: chain 15.231 G4_A 1.873 floor -8.11 / -7.04 / -12.86 | single at 0.85: 6.9528 -> 2.191; at 0.7607: 8.9919 -> 1.694
m28 single-cell Gw by lo: 0.25 8.1315 | 0.30-0.60 8.2477 | 0.70 8.2831 | 0.75-0.77 8.9919 | 0.80 8.5262 | 0.85 6.9528

$ python3 fine.py   (0.0025-step scan; G4 matched = chain at lo over single cell at lo - rule lag)
m28 lo 0.7625-0.7875: chain 13.532 floor -9.65..-9.68 | G4_A 1.664 | matched 1.634
m28 lo 0.7925: chain 13.532 floor -10.08 | G4_A 1.664 | matched 1.634
m28 lo 0.7950: chain 13.543 floor -10.08 | G4_A 1.665 | matched 1.631
m28 lo 0.7975: chain 13.852 floor -10.08 | G4_A 1.703 | matched 1.669
m28 lo 0.8000-0.8175: chain 14.074 floor -10.08 | G4_A 1.731 | matched 1.695
m28 lo 0.8200: chain 14.074 floor -9.19 | G4_A 1.731 | matched 1.695
m30 lo 0.7675: chain 13.390 floor -10.86 | G4_A 1.616 | matched 1.606
m30 lo 0.7700: chain 13.512 floor -10.86 | G4_A 1.630 | matched 1.621
m30 lo 0.7725-0.7875: chain 13.537 floor -10.86 | G4_A 1.633 | matched 1.624
m30 lo 0.7900-0.8000: floor -10.19..-8.59 | G4_A 1.633-1.634 | matched 1.624
m30 lo 0.8025: chain 13.813 floor -8.59 | G4_A 1.667 | matched 1.657
m30 lo 0.8050: chain 14.562 floor -8.59 | G4_A 1.757 | matched 1.736
m30 lo 0.8075-0.8200: chain 14.486-14.612 floor -8.41..-8.59 | G4_A 1.748-1.763 | matched 1.706-1.712

$ python3 (continuum from own runs)
m30 N240: single 8.2879 chain 13.1033 G4_A 1.58103; passive transfer 15.830 dB
m30 N480: single 8.4681 chain 12.7255 G4_A 1.50277; passive transfer 16.233 dB
m28 N240: single 8.1315 chain 12.9173 G4_A 1.58854; passive transfer 15.812 dB
m28 N480: single 8.2586 chain 12.5832 G4_A 1.52365; passive transfer 16.210 dB
m30: continuum 2*G(480)-G(240) = 1.4245
m28: continuum 2*G(480)-G(240) = 1.4588

$ grep notes/ (standing rule 10)
- No promoted statement of scoring-window placement dependence of the gated single-cell floor; 08-02's 're-trim' is the comparator threshold trim.
- 07-20 / 07-21 carry no junction-reflection loading of the drain.
- 08-12 key text: 'at fixed grid the rl-1 amplitude moves 10.3 dB across cfl 0.2-0.8 (-22.53 -> -12.19 dB)'; conventions 'ratio bias 0.7*M_th_num(N) at the row's own grid'.

$ cd /home/user/FableComputer && git status --short | wc -l
0

Not re-executed (I accept no number from these): seeds 11/13, N = 720, m = 28 J ≠ −1 at N = 240, Table 2a matched boundary-driven rows, Table 2b, Table 3 stages 3–5, Table 6 latency families other than m = 30/28 N = 240, cfl 0.8, the velocity plane.
```

</details>
