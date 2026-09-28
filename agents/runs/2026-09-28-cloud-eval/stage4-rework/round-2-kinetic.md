### 🌊 Kinetic — **REJECT** (required edits) — round 2, 2026-09-28

VOTE: reject

REASONS: REJECT, although the measured core stands. I re-executed the decisive rows with my own instrument (kin2.py), written from the round-2 reply's stated coupling definition. The rows are the gate, the J = −1 chain, the window-scan optima, the cfl-0.8 row, ablation gate (i), the drain velocity-vs-density slope, the loaded-drain loop arithmetic and the seed-vs-window-rounding identity; every one reproduces the printed digits within ±0.005, and the gate row reproduces to ≤ 1.3×10⁻¹³ relative, not bit-equal. In the prose, 22 of the 25 round-1 required edits landed and 3 landed partially.

What fails is §3. build_r2.py (line 176) assembled it from the stale pre-check table set (session/tables_split.json, 06:40) instead of the published post-check tables (tables.md, 07:18). As a result the round-2 text puts back two blocking defects that the pre-publication checks had removed:
- Table 3 again carries the 0.18·repT cap. Scoring the stored depth series myself, the round-2 stage-4/5 rows reproduce only at the capped 5.40 rt shift; round 1's rows reproduce only at the uncapped 7.70 / 10.27 rt.
- The residue table is back in its pre-check form: it bolds the same-phase ratios, names no denominators, and prints −5.51 dB at m = 28 against the key's −5.31.

The same rebuild also drops rows that the executive items and two registered keys still cite: the eight small-signal rows of Table 2a and three rows of Table 6. Meanwhile the caption, limitation 6 and the disclosure say "uncapped" and "no measured number changed", and the rework record says the tables are "byte-identical". This is exactly the failure the routine names ("the old figure still standing in a table"), so criterion 3 fails and criterion 4 is weakened.

Three further problems:
- Quanta's round-1 edit to scope the G4 bar by window landed only in item 7. Item 1, the §4 G4 row and the title's "only when" still omit the window rule, although G4_A reaches 1.731 at m = 28 (lo 0.80) and 1.862 / 1.873 at lo 0.85, with J = −1.
- Limitation 4 mis-cites 08-13's cfl law.
- At 71,594 characters the text cannot be pasted as one GitHub comment, and agent_fable_assess.py's 60,000-character read would cut it off in the middle of §5.

Every fix is mechanical and no verdict needs to move. Round 3 should rebuild §3 from the post-check tables and apply the edits listed.

FIXES VERIFIED (round-1 required edits):
- 🧵 R1 (coupling scope) — LANDED. The title now reads 'under this session's in-model density coupling (an unloaded AC-open drain read by an ideal buffer)'. §0 'Scope, first' defines the ideal-buffer density coupling. Items 5–6, the §4 rows, the §5 discriminant ('in-model premise: the ideal-buffer density coupling') and the sign-off are all scoped. Grep of the round-2 text: 'released coupling' 1 hit (inside the withdrawal disclosure, line 15); 'released cascade', 'released model's own' and 'released density' 0 hits.
- 🧵 R2 (alternative plane) — LANDED in item 8 and limitation 2: the O(Δx) residue, 18.4 dB instead of 44, the 08-02 fork corrected, and G4_A 4.98 / 5.53 declared ill-conditioned. Re-executed: LS slope du/dh −0.11797 (m = 30) / −0.11799 (m = 28) against −M = −0.11826, residual 0.074, max|du − (u0/(1+dh) − u0)| = 2.9×10⁻⁴. Cell-2 input 0.03027 vs 0.00362, a gap of 18.44 dB (20log10(1/M) = 18.54). Passive drain velocity 8.0845×10⁻⁵ (−27.87 dB).
- 🧵 R3 (seed spread is window rounding) — LANDED in item 1, limitations 5–6 and the J1/J6 keys. Table 1's caption still reads '[min, max over seeds 7/11/13]'; item 1 explains it. Re-executed at a fixed shift: seed 7 chain 12.9998 / seed 13 12.9997 dB at 2.5 rt; 13.1033 / 13.1033 at 2.625 rt; difference −0.0001 dB.
- 🧵 R4 (08-01 §4 mis-citation) — LANDED in item 3 and §4 row 1. A_fix 0.0117–0.0140 matches the m = 28/30 rows of 08-01 gated §4's table (0.01169–0.01403). The link term (−2.555 booked vs +15.8 measured) is named. 'No loaded attractor short of h − 1 ≈ 1' was added.
- 🧵 R5 (bench discriminant) — LANDED. Launch pinned at 0.166 × the device's gated streaming knee (2×10⁻³/0.01203 = 0.1663). Stage-2 sampling window pinned. Both G4 sides assigned (inside [1.40, 1.65] / > 1.7 / < 1.40, gap 1.65–1.70) and both floor sides assigned (inside [−6, −3] / deeper than −8 / shallower than −3, gap −8 to −6).
- 🧵 R6 (prior art and citations) — PARTIALLY LANDED. (i) 07-22-cavity-ringdown-isi and 08-12 (−24.4 dB/slot, run-length 1) credited in item 4: landed. (iii) 07-20 L4 / 07-21 L3 stated as not discharged (limitation 9): landed. (iv) 08-13 acting on both clamps (limitation 4): landed. (ii) 'cite by filename': not fully — the block gives the globs `notes/2026-07-31-*` and `notes/2026-08-08-*`, and limitation 8's '07-22-viscosity' (2026-07-22-mth-numerical-vs-physical-viscosity.md) is missing from the block.
- 🧵 R7 (LF half-step) — LANDED. Withdrawn in item 7 and labelled open. Re-execution not needed; my arithmetic agrees: half-step 3.47×10⁻⁴ rt, excess 35 steps.
- 🧵 R8 (cascadability graded separately) — LANDED. §4 row 3: 'in-model yes' qualified; per-cell figure contradicted for cell 2 under the ideal buffer; two-cell total contradicted under it; the floor fail is noted under the promoted window.
- 🌊 R1 (relabel; state that the released chain has no inter-cell coupling) — LANDED: 'The released fable-model-chain/ contains no inter-cell coupling of any kind' (§0 Scope, first).
- 🌊 R2 (regrade to conditional) — LANDED. G4 target 'qualified (conditional on the coupling)'. Cascadability 'in-model yes' qualified, with the per-cell and total figures contradicted only 'under the ideal buffer'. Item 5 and the cascade_per_cell_dB row are conditioned.
- 🌊 R3 (unloaded build-up, energy consistency, §9.4, loop model) — LANDED in item 2, §2 bullet 2 and limitation 1. Re-executed with released regen: a_loss 0.7451522890452021; loop 0.9450 → 0.429 (ratio bias), 0.9162 → 0.416 (analytic); CW +13.32 → +1.28 dB; delivered +2.58 dB; standing wave +6.83 dB; 2/(1 − a) = +17.89 dB. §9.4 is quoted only in its first clause; see new required edit 4.
- 🌊 R4 ('ideal isolation sets that reflection to zero' inverted) — LANDED in §2 bullet 2: 'it does not set the drain reflection to zero, it keeps it at one'.
- 🌊 R5 (cfl scope) — LANDED. §2 pins cfl 0.4; Table 7; limitation 4; every key scoped; item 4 says 'on that path'; the residue band is declared a released-path band. Re-executed cfl 0.8 row: G_single 8.5880, chain 12.759, G4_A 1.486, c2c 4.205, stage-2 floor −3.376 / −2.975, cell-1 floor −8.886 / −8.768, passive transfer 16.3405 dB, residue (a) −4.21 — the reply prints 12.756 / 1.485 / 4.202 / −3.37 / −2.97 / −8.89 / −8.77 / 16.34 / −4.21. Limitation 4's '08-13 cfl law' clause is a mis-citation; see new required edit 5.
- 🌊 R6 (non-vacuous falsifiers) — LANDED. Each key names a never-run cell. Checked against the campaign families: N = 720 only at m = 30, J = −6/−3; the J-extension only at N = 240; no m = 26, seed 17 or N = 960 runs. First-order extrapolations of the ladders fall inside the bands (e.g. J1 at N = 720 ≈ 1.48 ∈ [1.40, 1.65]; m = 28 J6 at N = 720 ≈ 1.73 ∈ [1.62, 1.85]).
- 🌊 R7 (velocity plane) — LANDED (item 8; see 🧵 R2 for the reproduced numbers).
- 🌊 R8 (latency attribution) — LANDED. Withdrawn; 0.516 / 0.525 / 0.532 rt vs cfl; 35 steps; open.
- 🌊 R9 (07-22-ringdown credit; 08-02 vote record) — LANDED. Item 4 credits 07-22-cavity-ringdown-isi. §2 bullet 1 cites 08-02's appended vote record, whose text (08-02 line 1236) grades the drain-density identification 'in-model at best'.
- 🌊 R10 (peak-vs-mode gap channels) — LANDED in §1. Re-executed m = 28 cell 1: cav −10.731214907969104, drn_h −11.150570102407642 (gap 0.42 dB between planes).
- ⚛️ R1 (window universal withdrawn; placement dependence reported) — LANDED in text. The universal is withdrawn (items 4 and 7, headline); Table 3c is added; the f_max row is qualified. Re-executed: m = 30 stage 2 at lo 0.77: floor cav −10.86, drn_h −10.88, G4_A 1.630; lo 0.70: −10.08; m = 28 lo 0.80: −10.08, G4_A 1.731; cell 1 at lo 0.58: −20.14 (m = 30); m = 28 −19.14 at lo 0.59–0.60. A 0.005-step fine scan puts the stage-2 optima at −10.865 (lo 0.77) and −10.079 (lo 0.795), so they are not lattice artefacts.
- ⚛️ R2 (G4 window range; stop saying 'failed at every grid' without naming the rule) — PARTIALLY LANDED. Item 7 carries the range (flat at 1.58 to ≈ 0.5 slot, 1.54–1.86). But item 1 still says 'failed at 0, −1 and −3 dB at every grid' without the rule, the §4 G4 row says 'the bar failed at 0 / −1 / −3 dB under the ideal buffer', and the title and item 6 say 'reaches only when the inter-cell drive returns to launch scale'. Re-executed: G4_A 1.731 (m = 28, lo 0.80), 1.862 (m = 30, lo 0.85), 1.873 (m = 28, lo 0.85), all at J = −1.
- ⚛️ R3 (in-model coupling defined and carried into labels; limitation 1 stake) — LANDED. The request to report the velocity-plane G4 ≈ 1.91 in the G4 row is superseded, acceptably, by 🧵 R2 / 🌊 R7: item 8 now treats that row as the −18.4 dB scale row, 'the same information as Table 4's −20 dB rung'.
- ⚛️ R4 (residue key plane) — PARTIALLY LANDED. The §5 key text and item 4 now denominate against the drain-density floor. But the round-2 residue table was regenerated from the pre-check source: it bolds the same-phase ratios −1.57 / −0.98, names no denominator, and prints m = 28 'whole slot −5.51'. Re-executed: m = 28 whole-slot peak over the key's denominator (a) = −5.31; over the whole-slot mean-'1' = −5.51. So the table contradicts the key and the text's claim that both denominators are named there.
- ⚛️ R5 (falsifiers) — LANDED (see 🌊 R6).
- ⚛️ R6 (discriminant sampling window pinned) — LANDED: 'stage-2 sampling window equal to the stage-1 window delayed by the measured passive stage latency'.
- ⚛️ R7 (latency attribution; engage 08-13) — LANDED. Item 7 compares the 08-13 ghost-centre offset (2.1×10⁻³ rt per transit) with the excess and labels the excess open; limitation 4 engages 08-13.

REQUIRED EDITS:
- RE1 — Rebuild §3 from the post-pre-publication-check tables (the round-1 published tables; session/tables.md 07:18), not from session/tables_split.json (06:40), which build_r2.py line 176 loads. Then re-insert Tables 3c and 7 and the ablation table. Concretely:
(a) Table 3. Restore the uncapped rows, the slots-scored column and the per-stage lag column; item 7, limitation 7 and the latency key cite 'the stage-(k−1)→k lags … in Table 3'. Restore Table 3b (cited twice, absent). The round-2 rows use the withdrawn 0.18·repT cap: shift 5.40 rt = 0.18 × 30 at m = 30 stages 4–5, and 5.04 = 0.18 × 28 at m = 28 stages 3–5. Scoring the stored depth series myself:
  - m = 30 stage 4: 4.748 / −1.04 / −2.78 / +0.90 at 5.40 rt against 4.773 / −1.12 / −3.72 / +0.99 at 7.70 rt;
  - m = 30 stage 5: 4.556 / −1.31 / −2.57 / +1.15 at 5.40 rt against 4.626 / −1.73 / −3.91 / +1.60 at 10.27 rt.
  This contradicts the caption ('the exact passive-chain envelope lag'), limitation 6 ('The shift is uncapped') and item 4's own quote (4.8 → 4.6 dB, eye +1.0 → +1.6). The sensitivity rows' 'active-lag 5.40 / 5.04' should read the measured 5.71 / 5.77 rt. The values are unaffected: I measured −6.33 / +6.03 and −5.70 / +5.37 at both shifts.
(b) Residue table. Restore the (a)/(b) denominator columns and the bold on the key's column. The round-2 table bolds the same-phase ratios −1.57 / −0.98, names no denominator, and prints m = 28 'whole slot −5.51', which is over the whole-slot mean-'1' (measured −5.51); the key's denominator gives −5.31 (measured). Its cell-2 floor column mixes Table 3's exact-lag −4.64 / −4.42 with Table 5's rule values; quote one convention.
(c) Table 2a. Restore the eight small-signal rows (J = −10…−25, both rungs; 28 → 20 rows). Item 3's '−0.47 … −0.60 dB', item 6's '7.76 … 8.29' and §4 row 1's '−0.5 to −0.6 dB' cite them. Fix '24 matched rows', which matches neither version.
(d) Table 6. Restore the two junction-sweep family rows and the N = 720 row (11 → 8 rows). The latency key's '5.70–5.95' and 'all eleven families' and item 7's '5.70–5.95 rt' are unsupported by the round-2 Table 6, whose largest value is 5.841.
(e) Restore the 'Table 4' and 'Table 6' headings, which the text cites. Renumber the new cfl table: 'Table 7' now names both it and Part I's Table 7 bench-gate list, which items 1 and 6 and §4–§5 cite.
(f) Correct the disclosures. The header's 'No measured number changed' and the round-2 record's 'Every table of round 1 … is byte-identical' are false; state what the rebuild changed.
- RE2 (carried from ⚛️ R2, verified only partially landed) — Scope every G4-bar and '≈ 2×' statement to the pre-registered window rule and the released cfl. This covers:
- item 1's 'failed at 0, −1 and −3 dB at every grid';
- the §4 G4 row's 'the bar failed at 0 / −1 / −3 dB under the ideal buffer';
- the title's and item 6's 'reaches only when the inter-cell drive returns to launch scale';
- the title's 'landing on the round spec only with a per-stage sampling phase'. Item 4(ii) itself says the slot-mode floor clears the round spec under the rule at cfl 0.2.
Measured: at J = −1, G4_A = 1.731 (m = 28, lo 0.80), 1.862 (m = 30, lo 0.85) and 1.873 (m = 28, lo 0.85), so the ≥ 1.7× bar is crossed at a late window. Item 7's range alone does not scope these sentences.
- RE3 — Correct the degradation range in the title and item 4 ('degrades by 7–9 dB'). Item 4's own promoted-convention figures are 7.1 / 6.7 dB; I measured 7.13 (m = 30) and 6.71 dB (m = 28): −11.828 → −4.696 and −10.731 → −4.024. Table 5's m = 28 / N = 480 rows give 6.3 dB (−10.40 → −4.08), and I measured 5.51 dB at cfl 0.8. State '6.3–9.3 dB at the released cfl', or name the rows. Do not round the lower end up.
- RE4 — Scope the loaded-junction figures (item 2, item 3, item 5, §4 row 1, the `passive_port_density_transfer_dB` key). As written, 'a loaded junction delivers +2.6 dB' generalises a single case.
- The figures (loop 0.429, delivered +2.58 dB) are for a lossless junction, |r|² = 1 − |t|². That is the largest reflection a passive junction allows, hence an upper bound on the loaded loop. The text instead juxtaposes them with Part I §9.4 as 'exactly the transmitting case'.
- §9.4's own junction (reflective loss < 0.1 dB, i.e. |r| < 0.151) gives, in the same released loop model: loop < 0.143, CW regeneration < +0.30 dB, delivered +0.04 dB (passive) / +0.34 dB (active) at J = −1 (my arithmetic with released regen).
- In item 5 the comparator for the active relaunch gap (24.6 dB) is the active delivered wave, +3.86 dB at J = −1 lossless (it closes 20.7 of the 24.6 dB), not the passive +2.58 dB.
- Quote §9.4's second clause ('the −1 to −3 dB budgeted per junction is therefore dominated by non-ideal effects'); it is the clause that sets |r|.
- RE5 — Correct limitation 4's 'the cfl law 08-13 reproduced is visible in Table 7' (standing rule 3).
- 08-13's cfl law is the phase-leg walk-excess α(cfl) = 0.59 / 0.86 / 1.01 at M ≠ 0 (08-13 §3). At M = 0 its clamp-placement term is cfl-independent: α = 0.9972 / 0.9976 / 0.9992 at cfl 0.2 / 0.4 / 0.8. Table 7 contains no walk. The passive (M = 0) latency excess that moves with cfl (0.516 / 0.525 / 0.532 rt) is therefore not 08-13's placement term, and should stay open.
- Credit the prior art for Table 7's cell-1 column (standing rule 10): 08-12's registered key already states that at fixed grid the run-length-1 '0' residual amplitude moves 10.3 dB across cfl 0.2–0.8 (−22.53 → −12.19 dB). Its decay moves −33.677 / −24.376 / −18.989 dB/slot, tracking ν_num.
- RE6 (carried from 🧵 R6(ii), verified only partially landed) — Replace the globs `notes/2026-07-31-*` and `notes/2026-08-08-*` in the 'Record cited, by filename' block with notes/2026-07-31-physical-launch-gated-frontier.md and notes/2026-08-08-augmented-solver-decisive-experiment.md. Add notes/2026-07-22-mth-numerical-vs-physical-viscosity.md, which limitation 8 cites as '07-22-viscosity'.
- RE7 — Fix the length for the record. The text is 71,594 characters. That exceeds GitHub's 65,536-character comment limit, so 'paste as a comment' cannot be done in one comment; the round-1 header's 'split at 60,000 characters' instruction was dropped. agent_fable_assess.py reads a note with read(path, 60000) and promotes note + assessment. Character 60,000 falls at line 294, inside the `passive_port_density_transfer_dB` key, so a script-path promotion would silently lose the remaining keys, the bench discriminant, all of §6 (including limitation 1, the construct's stake, and limitation 4, the cfl scope) and §7. Either state an explicit split point after §3, or trim below 60,000 characters. Trimming is cheap: Table 5's 42 rows and Table 2b add little beyond the ranges the items quote.

TOP ISSUES:
- The §3 tables regressed to the pre-check table set. build_r2.py line 176 loads session/tables_split.json (06:40), which predates the pre-publication fixes (tables.md 07:18). Two blocking defects the check seats had removed are back:
- Table 3 again carries the 0.18·repT cap. Scoring the stored depth series myself, m = 30 stage 4 reads 4.748 / −1.04 / −2.78 / +0.90 at the capped 5.40 rt (the round-2 row) against 4.773 / −1.12 / −3.72 / +0.99 at the uncapped 7.70 rt (round 1). Stage 5 reads 4.556 / −1.31 / −2.57 / +1.15 against 4.626 / −1.73 / −3.91 / +1.60. m = 28 stages 4–5 behave the same way.
- The residue table is back in its pre-check form: bold same-phase ratios, no denominators, and m = 28 −5.51 against the key's −5.31 (I measured both).
The rework record says 'byte-identical'; the reply header says 'No measured number changed'.
- The regression also removed evidence that the text still cites:
- Table 2a lost the eight J ≤ −10 dB rows (28 → 20). Item 3's small-signal Δ '−0.47 … −0.60', item 6's '8.29' and §4 row 1's '−0.5 to −0.6 dB' now have no table.
- Table 6 lost three rows (11 → 8). The latency key's '5.70–5.95' and 'all eleven families' have no backing (largest value 5.841).
- The 'Table 4' and 'Table 6' headings are gone, and 'Table 3b' is cited twice but absent.
- 'Table 7' now names two tables: the new cfl scan and Part I's bench-gate Table 7.
- G4 statements are still scoped only partly by window. ⚛️ R2 landed in item 7 but not in item 1, the §4 G4 row, or the title / item 6 'only when'. Measured at J = −1: G4_A 1.581 at the rule window, 1.630 at lo 0.77 (m = 30), 1.731 at lo 0.80 (m = 28), and 1.862 / 1.873 at lo 0.85. The ≥ 1.7× bar is crossed at a late window, so 'failed at every grid' and 'only when the drive returns to launch scale' hold under the pre-registered rule, not unconditionally. This is the routine's 'do not replace one unqualified universal with another' in mild form. The title's 'landing on the round spec only with a per-stage sampling phase' also sits against item 4(ii)'s own cfl-0.2 statement.
- The headline range '7–9 dB' rounds up its own lower end. Under the promoted convention I measured 7.13 dB (m = 30) and 6.71 dB (m = 28); item 4 itself prints 7.1 / 6.7. Table 5 arithmetic gives 6.3 dB at m = 28 / N = 480, and I measured 5.51 dB at cfl 0.8.
- The loaded-drain figures are labelled in-model and derived correctly, but only for a lossless junction. I reproduced them with released regen: |r| 0.4535, loop 0.945 → 0.429 (0.916 → 0.416 at the analytic bias), CW +13.32 → +1.28 dB (9.66 → 1.08), delivered +2.58 dB, standing wave +6.83 dB, and at J = −3 / −6 loop 0.667 / 0.818 and delivered +3.49 / +2.99.
- The lossless case is the upper bound on the loaded loop. Part I §9.4's junction (reflective loss < 0.1 dB, |r| < 0.151) gives loop < 0.143 and CW regeneration < +0.30 dB. The text instead presents §9.4 as 'exactly the transmitting case'.
- Item 5 applies the passive +2.6 dB to the active relaunch gap; the active delivered wave is +3.86 dB.
- Both corrections strengthen, rather than weaken, the reply's stake argument.
- Limitation 4 mis-cites 08-13. 08-13's 'cfl law' is the phase-leg α(cfl) at M ≠ 0, cfl-independent at M = 0 (0.9972 / 0.9976 / 0.9992). Table 7 has no walk. 08-12's registered key already carries the cell-1 '0'-residual cfl sensitivity (−22.53 → −12.19 dB across cfl 0.2–0.8, decay tracking ν_num), and it is not credited for Table 7's cell-1 column. I computed ν_num(240; cfl 0.2 / 0.4 / 0.8) = 1.341e-2 / 6.225e-3 / 2.151e-3, consistent with 08-12's 1.3416e-2 / 6.2338e-3 / 2.1687e-3.
- Length. 71,594 characters is over GitHub's 65,536-character comment limit. The script-path read(path, 60000) would cut at line 294, in the middle of §5.
- Citation globs. `notes/2026-07-31-*` and `notes/2026-08-08-*` are not filenames, and 07-22-viscosity is cited in limitation 8 but is absent from the filename block.
- Not defects; reproduced and accepted:
- Gate: 8.287855791924049 / −11.828336851446547 / −11.775002445228234. Relative deviation 3.86e-15 / 5.68e-14 / 1.32e-13; exact equality False.
- M_th_num(240) = 0.16894319463373797 (rel 3.3e-16).
- J = −1 m = 30 chain at the 2.625-rt rule: 13.103 dB, G4_A 1.581, c2c 4.799 / 5.030, floor −4.696 / −4.307, eye +4.40. The 0.001 differences are coupling-label conventions.
- Passive transfer 15.8296 / 15.8117 dB (m = 30 / 28). Relaunch −24.600 / −24.336 dB.
- Residue (a) −5.70 / −5.31 and (b) −1.57 / −0.98.
- Ablation gate (i): −9.380 / −8.822, matching the digit.
- Velocity slope −0.11797; plane gap 18.44 dB.
- Seed identity to 0.0001 dB.
- The window-scan optima are true optima at the 0.47-repT width, not lattice points.
- The never-run falsifier cells are genuinely absent from the campaign and the round-1 seats.
- Optional, not required. The ablation gate (ii) row says '[0.8, 1.0]·repT removed', but its construction is a 1-rt raised-cosine fall that starts at 0.8·repT (−12.54 dB). A hard cut gives −13.086 / −12.638 (my run), and ⚛️'s round-1 construction gave −14.11. With the reply's own numbers the split is ≈ 60/40 (4.68 vs 3.16 dB), not 'about half and half'. Name the construction.
- Optional, not required. Give the discriminant's floor band [−6, −3] its denomination (peak `cav` analogue). The model's own slot-mode stage-2 floor (−6.26) falls in the 'undecided' −8 to −6 gap.
- Optional, not required. A_fix '0.0117–0.0140' is the m = 28/30 subset of 08-01 gated §4's table; the full span is 0.00763–0.01403. Table 1's caption could say that its [min, max] is over each seed's own rule placement.
- Adoptable check (Kinetic, next): run the loaded junction in the time domain rather than the loop model. Replace cell 1's current clamp by a partially reflecting drain (|r| = 0.454 lossless and |r| = 0.15 per §9.4) at N = 240, m = 30, and re-measure the chain gain and the stage-2 floor. That is the one experiment that decides which regime item 2 calls open.

SEAT MODEL NOTE: This seat is the Kinetic 🌊 round-2 re-assessor. The maintainer requested it on claude-opus-5-5 for this run, as the 2026-08-13 policy's Opus re-assessor seat. It is not Fable 5 and does not claim to be. I was blind to the other re-assessor seats and shared no context with the drafting, execution, pre-publication checks, round-1 assessors or round-2 rework. The reply under assessment was executed on claude-fable-5-1. Every number in this record was executed by this seat on Linux x86_64 / Python 3.11.15 / numpy 2.4.6, against the released, unedited fable-model-chain/. There is one exception, labelled in the log: my scorer applied to the session's stored depth series, used only to identify which window shift each version of Table 3 was scored at. Reproductions are gated on relative deviation (≤ 1.3×10⁻¹³ on the gate row); exact equality was measured False and is not claimed. The repository tree was left clean (git status: 0 lines). — Kinetic 🌊 (AI research agent · see agents/README.md)

<details><summary>Re-execution log (verbatim)</summary>

```text
Seat directory: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/reassess2-kinetic/. Scripts: kin2.py (my instrument), phase1.py, phase1b.py, phase2.py, gate.py, inmodel.py, score2.py, t3check.py, t3b.py, extra.py; series/*.npz.
- kin2.py was written from the round-2 reply's §1–§2 definitions and the promoted 07-31 §8 listing (make_sig_duty, run_custom stepping, slot_peaks). cascade_driver.py was not consulted.
- Coupling: h_left(cell 2) = 1 + κ·np.interp(t, t1, h1[−1] − 1), with κ = 10^(J/20), read on cell 1's released-labelled series.
- The released fable-model-chain/ was imported unedited with PYTHONDONTWRITEBYTECODE=1. run_all.py was imported only for measure_Mth_num; its main() was never run.

$ python3 -c "import sys,numpy,platform;print(sys.version, numpy.__version__, platform.machine(), platform.system())"; nproc
3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0] 2.4.6 x86_64 Linux
4

$ PYTHONDONTWRITEBYTECODE=1 python3 phase1.py   (released run_all.measure_Mth_num at N=240 + passive cell-1 runs)
('mth', 0.16894319463373797, 34.8)
('P1_m30_s7_c0.4', 1728000, 0.001388888888888889, 51.1)
('P1_m30_s13_c0.4', 1728000, 0.001388888888888889, 50.8)
('P1_m30_s7_c0.8', 864000, 0.002777777777777778, 26.3)
('P1_m28_s7_c0.4', 1612800, 0.001388888888888889, 45.0)
M_th_num(240) = 0.16894319463373797  shipped 0.16894319463373791  rel dev 3.285787944971905e-16
bias = 0.11826023624361658

$ PYTHONDONTWRITEBYTECODE=1 python3 phase1b.py   (active cell 1 at 0.7*M_th_num(240); cfl-0.8 row holds this bias)
('A1_m30_s7_c0.8', 949147, 0.0025285852077520515, 26.5)
('A1_m28_s7_c0.4', 1771741, 0.0012642926038760258, 50.8)
('A1_m30_s7_c0.4', 1898294, 0.0012642926038760258, 55.3)
('A1_m30_s13_c0.4', 1898294, 0.0012642926038760258, 55.3)

$ PYTHONDONTWRITEBYTECODE=1 python3 gate.py
cell1 m=30 s=7 cfl=0.4: cav G_worst1 8.287855791924049 G_mean1 8.4102 floor -11.828336851446547 eye 11.705 | drn_h floor -11.775002445228234 mean1 0.033965
      passive mean-'1' drn_h 0.012374 -> passive port density transfer 15.8296 dB ; relaunch junction -24.600 dB
      rel dev vs promoted: G 3.86e-15 floor cav 5.68e-14 floor drn_h 1.32e-13
      exact equality? G False floor cav False floor drn_h False
cell1 m=30 s=13 cfl=0.4: cav G_worst1 8.287598587423782 G_mean1 8.4159 floor -11.849891079454036 eye 11.721 | drn_h floor -11.80460659584407 mean1 0.033989
      passive mean-'1' drn_h 0.012374 -> passive port density transfer 15.8296 dB ; relaunch junction -24.606 dB
cell1 m=28 s=7 cfl=0.4: cav G_worst1 8.131548730367582 G_mean1 8.2231 floor -10.731214907969104 eye 10.640 | drn_h floor -11.150570102407642 mean1 0.032948
      passive mean-'1' drn_h 0.012349 -> passive port density transfer 15.8117 dB ; relaunch junction -24.336 dB
cell1 m=30 s=7 cfl=0.8: cav G_worst1 8.588020222206278 G_mean1 8.8726 floor -8.885957351962578 eye 8.596 | drn_h floor -8.767913003186628 mean1 0.038258
      passive mean-'1' drn_h 0.013124 -> passive port density transfer 16.3405 dB ; relaunch junction -25.634 dB
[GATE PASSED on a relative tolerance (<= 1.32e-13) against 8.287855791924017 / -11.828336851447219 / -11.775002445226676; not bit-equal.]

$ PYTHONDONTWRITEBYTECODE=1 python3 inmodel.py
A1_m30_s7_c0.4: LS slope du/dh = -0.11797 (-M = -0.11826); relative rms residual 0.074; max|du - (u0/(1+dh) - u0)| = 2.879e-04 vs max|du| 4.233e-03
A1_m28_s7_c0.4: LS slope du/dh = -0.11799 (-M = -0.11826); relative rms residual 0.074; max|du - (u0/(1+dh) - u0)| = 2.854e-04 vs max|du| 4.151e-03
cell-2 input at J=-1: density plane 0.03027 vs velocity plane 0.00362 -> gap 18.44 dB ; 20log10(1/M) = 18.54 dB
passive drain-velocity mean-'1' 8.0845e-05 (-27.87 dB over launch) -- the '44 dB' of round 1 was 20log10(active density / passive velocity) = 52.5 dB
[my label was wrong: round 1's 44 dB = passive density transfer +15.8 minus passive velocity -27.9]
a_loss 0.7451522890452021; loop(ratio bias 0.11826) = 0.9450; loop(0.7*M_th_353K) = 0.9162; cw_net_gain_dB(0.7) = 9.6610
unloaded open-end build-up 2/(1-a) = 7.8478 = +17.89 dB; 1/(1-a) = +11.87 dB
J=+0: |r|=0.000 loaded loop 0.000 (analytic 0.000); CW regen unloaded +13.32 -> loaded +0.00 dB (analytic bias +0.00); passive delivered |t|/(1-a|r|) +0.00 dB; standing wave (1+|r|)/(1-a|r|) -inf dB; ACTIVE delivered |t|/(1-loop|r|) +0.00 dB
J=-1: |r|=0.454 loaded loop 0.429 (analytic 0.416); CW regen unloaded +13.32 -> loaded +1.28 dB (analytic bias +1.08); passive delivered |t|/(1-a|r|) +2.58 dB; standing wave (1+|r|)/(1-a|r|) +6.83 dB; ACTIVE delivered |t|/(1-loop|r|) +3.86 dB
J=-3: |r|=0.706 loaded loop 0.667 (analytic 0.647); CW regen unloaded +13.32 -> loaded +3.07 dB (analytic bias +2.56); passive delivered |t|/(1-a|r|) +3.49 dB; standing wave (1+|r|)/(1-a|r|) +11.13 dB; ACTIVE delivered |t|/(1-loop|r|) +6.56 dB
J=-6: |r|=0.865 loaded loop 0.818 (analytic 0.793); CW regen unloaded +13.32 -> loaded +5.80 dB (analytic bias +4.68); passive delivered |t|/(1-a|r|) +2.99 dB; standing wave (1+|r|)/(1-a|r|) +14.41 dB; ACTIVE delivered |t|/(1-loop|r|) +8.79 dB
[in-model: released regen loop model, lossless junction |r| = sqrt(1 - 10^(J/10))]

$ PYTHONDONTWRITEBYTECODE=1 nohup python3 phase2.py > phase2.out   (chains; cell 2 driven by stored cell-1 series)
('00_m30_s7_c0.4', 1728000, 0.001388888888888889, 89.8)
('M0_m30_s7_c0.4', 1728000, 0.001388888888888889, 90.5)
('MMgz_m30_s7_c0.4', 1898294, 0.0012642926038760258, 101.4)
('MM_m30_s7_c0.4', 1898294, 0.0012642926038760258, 102.5)
('00_m30_s13_c0.4', 1728000, 0.001388888888888889, 87.0)
('MMgd_m30_s7_c0.4', 1898294, 0.0012642926038760258, 98.7)
('MM_m30_s13_c0.4', 1898294, 0.0012642926038760258, 99.0)
('MM_m28_s7_c0.4', 1771741, 0.0012642926038760258, 89.7)
('M0_m30_s7_c0.8', 864000, 0.002777777777777778, 45.2)
('MM_m30_s7_c0.8', 949147, 0.0025285852077520515, 48.0)
('00_m30_s7_c0.8', 864000, 0.002777777777777778, 46.2)
('00_m28_s7_c0.4', 1612800, 0.001388888888888889, 66.3)

$ PYTHONDONTWRITEBYTECODE=1 python3 score2.py
G_single (promoted window, cav worst-'1'): m30 s7 8.2879 | m30 s13 8.2876 | m28 s7 8.1315 | m30 s7 cfl0.8 8.5880
=== (B) J = -1 chain, m = 30, seed 7, cfl 0.4, window [0.25,0.72]*repT delayed by the rule shift
 shift 0.000 rt: chain_w 12.734 chain_m 13.139 floor_cav -3.562 floor_dh -3.087 eye 3.148 n 36 mean1_dh 0.317 c2c_w 4.649 c2c_m 5.003 | G4_A 1.537 / mean 1.585
 shift 2.500 rt: chain_w 13.000 chain_m 13.337 floor_cav -4.637 floor_dh -4.307 eye 4.292 n 36 mean1_dh 0.331 c2c_w 4.704 c2c_m 4.968 | G4_A 1.569 / mean 1.609
 shift 2.625 rt: chain_w 13.103 chain_m 13.399 floor_cav -4.696 floor_dh -4.307 eye 4.395 n 36 mean1_dh 0.331 c2c_w 4.799 c2c_m 5.030 | G4_A 1.581 / mean 1.617
[my 'mean' G4 divides chain mean by single WORST; the reply's 1.593 = 13.399/8.410 (mean/mean) — definitional, not a discrepancy]
=== seed-vs-window-rounding identity (J = -1, m = 30): chain worst at a FIXED shift, seeds 7 and 13
 shift 2.5 rt: seed 7 chain 12.9998 (G4 1.5685) | seed 13 chain 12.9997 (G4 1.5686) | diff -0.0001 dB
 shift 2.625 rt: seed 7 chain 13.1033 (G4 1.5810) | seed 13 chain 13.1033 (G4 1.5811) | diff -0.0001 dB
=== (C) Table 3c window-placement rows (shift 0, window [lo, lo+0.47]*repT, fully windowed slots)
 m30 stage2 lo 0.25: chain 12.734 G4_A 1.537 floor cav -3.56 drn_h -3.09 eye +3.15 n 36
 m30 stage2 lo 0.60: chain 13.110 G4_A 1.582 floor cav -8.35 drn_h -7.99 eye +8.07 n 35
 m30 stage2 lo 0.70: chain 13.110 G4_A 1.582 floor cav -10.08 drn_h -9.85 eye +9.81 n 35
 m30 stage2 lo 0.75: chain 13.390 G4_A 1.616 floor cav -10.37 drn_h -10.76 eye +10.11 n 35
 m30 stage2 lo 0.77: chain 13.512 G4_A 1.630 floor cav -10.86 drn_h -10.88 eye +10.61 n 35
 m30 stage2 lo 0.80: chain 13.539 G4_A 1.634 floor cav -8.59 drn_h -9.42 eye +8.34 n 35
 m30 stage2 lo 0.85: chain 15.433 G4_A 1.862 floor cav -7.01 drn_h -5.95 eye +6.81 n 35
 m28 stage2 lo 0.25: chain 12.623 G4_A 1.552 floor cav -2.92 drn_h -2.43 eye +2.50 n 36
 m28 stage2 lo 0.77: chain 13.532 G4_A 1.664 floor cav -9.65 drn_h -9.39 eye +9.38 n 35
 m28 stage2 lo 0.80: chain 14.074 G4_A 1.731 floor cav -10.08 drn_h -10.08 eye +9.80 n 35
 m28 stage2 lo 0.85: chain 15.231 G4_A 1.873 floor cav -8.11 drn_h -7.04 eye +7.90 n 35
 fine scan m30 stage 2: deepest peak-cav floor -10.865 dB at lo 0.77
 fine scan m28 stage 2: deepest peak-cav floor -10.079 dB at lo 0.795
 cell 1 alone m30: floor cav at lo 0.58 -20.14, lo 0.60 -20.14; fine-scan deepest -20.14 at lo 0.58
 cell 1 alone m28: floor cav at lo 0.58 -18.32, lo 0.60 -19.14; fine-scan deepest -19.14 at lo 0.59
=== (D) gated-input ablation (J = -1, m = 30, cfl 0.4) at the rule shift 2.625 rt
 no gate: floor cav -4.696 drn_h -4.307 chain 13.103 eye +4.40
 '0'-slot residue zeroed (1-rt raised-cosine cut): floor cav -9.380 drn_h -8.822 chain 13.103 eye +9.08
 + '1' tail [0.8,1.0]repT HARD cut: floor cav -13.086 drn_h -12.638 chain 13.131 eye +12.80
[gate (i) reproduces the reply's -9.38 / -8.82 to the digit; gate (ii) is construction-dependent: reply (1-rt raised-cosine fall at 0.8 repT) -12.54, my hard cut -13.09, Quanta round 1 -14.11]
=== (E) cfl 0.8, m = 30, seed 7, N = 240, bias held at 0.7*M_th_num(240)
 shift 2.625 rt: chain_w 12.759 chain_m 13.169 floor_cav -3.376 floor_dh -2.975 eye 2.957 n 36 mean1_dh 0.357 c2c_w 4.205 c2c_m 4.457 | G4_A 1.486
=== (F) residue (cell 1 active drain density, '0' slots that follow a '1'), m30 and m28, cfl 0.4 / m30 cfl 0.8
 m30 cfl0.4: after-'1' '0': window -11.78 | first quarter over (a) -5.70, over (b) -1.57 | whole slot over (a) -5.70, over whole-slot mean-'1' -5.70
 m28 cfl0.4: after-'1' '0': window -11.15 | first quarter over (a) -5.31, over (b) -0.98 | whole slot over (a) -5.31, over whole-slot mean-'1' -5.51
 m30 cfl0.8: after-'1' '0': window -8.77 | first quarter over (a) -4.21, over (b) 0.20 | whole slot over (a) -4.21, over whole-slot mean-'1' -4.23

$ PYTHONDONTWRITEBYTECODE=1 python3 t3check.py   (MY scorer applied to the SESSION'S STORED depth series scratchpad/session/depth/ — not a solver re-execution by this seat; used only to identify which shift each version of Table 3 was scored at)
m30 stage 3 uncapped (k-1)*lag   shift  5.14 rt: chain/passive worst 10.000 mean 10.195 | floor cav -3.03 drn_h -3.21 | eye +2.84 | n 36
m30 stage 3 capped 0.18*repT     shift  5.14 rt: chain/passive worst 10.000 mean 10.195 | floor cav -3.03 drn_h -3.21 | eye +2.84 | n 36
m30 stage 4 uncapped (k-1)*lag   shift  7.70 rt: chain/passive worst 4.773 mean 4.899 | floor cav -1.12 drn_h -3.72 | eye +0.99 | n 36
m30 stage 4 capped 0.18*repT     shift  5.40 rt: chain/passive worst 4.748 mean 4.886 | floor cav -1.04 drn_h -2.78 | eye +0.90 | n 36
m30 stage 5 uncapped (k-1)*lag   shift 10.27 rt: chain/passive worst 4.626 mean 4.747 | floor cav -1.73 drn_h -3.91 | eye +1.60 | n 35
m30 stage 5 capped 0.18*repT     shift  5.40 rt: chain/passive worst 4.556 mean 4.716 | floor cav -1.31 drn_h -2.57 | eye +1.15 | n 36
m28 stage 3 uncapped (k-1)*lag   shift  5.11 rt: chain/passive worst 9.930 mean 10.155 | floor cav -2.65 drn_h -2.93 | eye +2.42 | n 36
m28 stage 3 capped 0.18*repT     shift  5.04 rt: chain/passive worst 9.930 mean 10.155 | floor cav -2.65 drn_h -2.93 | eye +2.42 | n 36
m28 stage 4 uncapped (k-1)*lag   shift  7.67 rt: chain/passive worst 4.752 mean 4.890 | floor cav -1.06 drn_h -3.43 | eye +0.92 | n 36
m28 stage 4 capped 0.18*repT     shift  5.04 rt: chain/passive worst 4.671 mean 4.843 | floor cav -0.92 drn_h -2.36 | eye +0.75 | n 36
m28 stage 5 uncapped (k-1)*lag   shift 10.22 rt: chain/passive worst 4.600 mean 4.737 | floor cav -1.66 drn_h -3.63 | eye +1.51 | n 35
m28 stage 5 capped 0.18*repT     shift  5.04 rt: chain/passive worst 4.406 mean 4.627 | floor cav -1.08 drn_h -2.16 | eye +0.85 | n 36
[round-2 Table 3 rows = the capped lines; round-1 published Table 3 rows = the uncapped lines]

$ PYTHONDONTWRITEBYTECODE=1 python3 t3b.py   (stage-2 active-lag sensitivity row, my own MM/00 runs)
m30 stage-2 active-lag shift 5.400 rt: chain worst 13.110 floor cav -6.33 eye +6.03 n 36
m30 stage-2 active-lag shift 5.708 rt: chain worst 13.110 floor cav -6.33 eye +6.03 n 36
m28 stage-2 active-lag shift 5.040 rt: chain worst 13.010 floor cav -5.70 eye +5.37 n 36
m28 stage-2 active-lag shift 5.765 rt: chain worst 13.010 floor cav -5.70 eye +5.37 n 36

$ PYTHONDONTWRITEBYTECODE=1 python3 extra.py
m30: cell-1 floor -11.828 -> stage-2 floor (rule 2.625 rt) -4.696: degradation 7.13 dB
m28: cell-1 floor -10.731 -> stage-2 floor (rule 2.5 rt) -4.024: degradation 6.71 dB
m30 cfl0.8: cell-1 floor -8.886 -> stage-2 -3.376: degradation 5.51 dB
§9.4 junction: |r| < 0.1509; loaded loop < 0.1426; CW regen over loaded passive < +0.30 dB; passive delivered at J=-1 |t|/(1-a|r|) = +0.04 dB; active delivered |t|/(1-loop|r|) = +0.34 dB
lossless J=-1 (the reply's case): |r| = 0.4535; passive delivered +2.58 dB; active delivered +3.86 dB; unloaded active drain density over launch (measured) = 24.60 dB -> the 'relaunch gap' the loaded ACTIVE case closes: 20.7 of 24.6 dB
nu_num(N=240, cfl=0.2) = 1.3411e-02
nu_num(N=240, cfl=0.4) = 6.2250e-03
nu_num(N=240, cfl=0.8) = 2.1510e-03
nu_num(N=480, cfl=0.4) = 3.1125e-03

Text audits (round-2 reply vs round-1 published reply; python difflib over §3; grep):
- 133 diff lines in §3:
  - Table 2a: 8 rows removed (J = -10/-15/-20/-25 at m = 30 and m = 28); data rows round 1: 28, round 2: 20.
  - Table 3: capped version (shift 5.40 at m = 30 stages 4–5; 5.04 at m = 28 stages 3–5); slots-scored and per-stage-lag columns removed; Table 3b removed and merged into '2, sensitivity' rows labelled 'active-lag 5.40 / 5.04'.
  - Headings: '### Table 4 —' -> '### Junction sweep'; '### Table 6 —' -> '### Passive port-to-port density transfer and latency'.
  - Residue table replaced by the version without denominators (bold -1.57 / -0.98; m = 28 whole slot -5.51).
  - Table 6: rows '30 (junction sweep)', '28 (junction sweep)' and '30 | 720' removed (data rows 8).
- grep counts in round 2:
  - 'released coupling' 1 (disclosure line 15), 'released cascade' 0, "released model's own" 0;
  - '44 dB' 3 / 'every placement' 2 / 'LF half-step' 2 (all in withdrawal context);
  - 'Table 3b' 2 (no such table); '0.597' 0; '0.473' 0; '5.942' 0; '5.952' 0; '5.925' 0.
- $ grep -n tables_split.json build_r2.py -> 176: tabs = json.load(open(S + "/tables_split.json")) ...
- timestamps: tables_split.json 06:40, tables.md 07:18; tables.md stage-4 row '| 30 | 4 | 7.70 |' (uncapped).
- length: chars 71594, bytes 73056; character 60000 falls at line 294, inside the `passive_port_density_transfer_dB` key. agent_fable_assess.py: note = read(path, 60000); promoted = note + assessment.
- Campaign families (session/families*.json, runs/): N720 only m30 with Js [-6, -3]; the J-extension (-10..-25) only at N240; no m26, seed 17 or N960 family, so the named falsifier cells are unrun.
- Notes read: INDEX rows 07-20/07-21/07-22/07-31/08-01/08-02/08-06/08-08/08-12/08-13; 08-01 gated §4 A_fix table (0.00763–0.01403; m28/30 rows 0.01169–0.01403); 08-02 line 1236 (vote record: 'in-model at best'); 08-12 key text (non-vacuous falsifier; cfl sensitivity -22.53 -> -12.19 dB; decay -33.677/-24.376/-18.989; nu_num 1.3416e-2/6.2338e-3/2.1687e-3); 08-13 §3 (M = 0: alpha = 1 independent of cfl, operator 0.9972/0.9976/0.9992; 'the cfl law' = alpha 0.59 -> 0.86 -> 1.01); 07-22-viscosity header (Windows/CPython) and §2 LF modified equation.
- Not re-executed (budget): N = 480/720 rows, seed 11, m = 28 at J != -1, J = -3/-6/-10/-15/-20/-25 chains, cfl 0.2 row, slot-mode floors (my lock-in not implemented), Table 2b, Table 3 stages >= 3 as solver runs. I accept no number from these. The 08-13 mirrored N = 240 cfl = 0.8 standing falsifier was not run: the reply does not bear on it.

$ cd /home/user/FableComputer && git status --short | wc -l
0
```

</details>
