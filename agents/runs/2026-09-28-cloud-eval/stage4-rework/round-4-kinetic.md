### 🌊 Kinetic — **REJECT** (required edits) — round 4, 2026-09-28

VOTE: reject

REASONS: REJECT at the cap. All 19 round-3 required edits landed. The round-4 tables and appendix match the published round-1 rows byte for byte; only the captions of Tables 1, 2b and 5 and the residue table changed, as the record says. Every decisive number I re-executed on my own instrument reproduces. That covers the gate (≤ 1.3×10⁻¹³ relative, not bit-equal), the J = −1 chain, Table 9 rows (i)–(iv), every printed Table 3d row, the loop-model range and its §9.4 bounds, and the rescoped universal. I checked that universal over the whole slot at both rungs, using both the exact lag and the ⅛-rt-rounded lag: no placement gives both a round-spec floor and matched G4 ≥ 1.7. Substance, labels, honesty and durability hold. Criterion 3 does not. The matched-window census behind item 1(c), the §4 G4 row and Table 3d's note was scanned only over lo ∈ [0.74, 0.83] (rw4_stored.py), yet it is stated for 'every round-spec placement'. The text's own Table 3c row at m = 30, lo 0.70 (−10.08 dB, mixed 1.582) contradicts its 'lo 0.74–0.79' and '1.61–1.62'. Over the full slot I measure lo 0.700–0.790, mixed 1.582–1.633 and matched 1.573–1.624. The new latency ladder's N = 720 rung (0.018 rt) comes from the J = −6 family, while its N = 240/480 rungs are J = −1; my own J = −1 N = 720 run gives 0.0218 rt, and the lag moves with junction class at fixed N. Two smaller defects remain: '< +0.3 dB' is printed for a bound whose supremum is +0.336 dB, and the header still carries the stale self-label 'this is the round-3 text'. Every fix is mechanical and none moves a verdict. But a range that the text's own table contradicts cannot enter the permanent record, and this round is the cap.

FIXES VERIFIED (round-1 required edits):
- 🧵 RE1 (Table 9 row iii; the split of the mechanism): LANDED. Table 9 now has five rows with their constructions named. Row (iii) is 'as (i), plus a hard cut of the '1' slots at 0.8·repT', printed at −13.09 / −12.64 / −16.82. Row (iv) is 'every '0' slot zeroed hard … plus the hard cut', printed at −13.81 / −13.36 / −17.53. The note under the table credits the round-2 seats' −13.09. Item 4 restates the shares: the '1' tail is worth 3.2–3.7 dB, and the '0' residue ≈ 4.7 dB under gate (i), stated as a lower bound, rising to ≈ 5.4 dB once the first round trip is removed (+0.7 dB); the 83 % at 0.009 slot is quoted. I re-executed all four gates on my own instrument (m = 30, J = −1, cfl 0.4, rule shift 5.25 units): (i) −9.380 / −8.822 / −12.978; (ii) −12.537 / −12.081 / −16.217; (iii) −13.086 / −12.638 / −16.820, chain 13.131, eye +12.802; (iv) −13.807 / −13.363 / −17.528, eye +13.523. The shares compute to 3.157 / 3.706 dB, 4.684 dB and +0.721 dB, and the raised-cosine factor at x = 0.54 time units is 0.831.
- 🧵 RE2 (the J1 key's lever clause): LANDED. The key now reads 'exits the band above at cfl = 0.2 while 1.485 at cfl = 0.8 stays inside; placement … exiting above only'. The residue key keeps its 'outside the band on both sides' (−8.11 / −4.21 against [−7.0, −4.5]), which is correct. Checked against the text only; I did not re-execute the cfl rows.
- 🧵 RE3 (bound direction and endpoints of the loaded-drain model): LANDED. Item 2 now says 'the largest reflection a passive junction allows, hence the *least* loading: the upper bound on the loaded loop, on cell 1's residual regeneration and on the delivered drive'. The range reads −1.0 dB (|r| → 0) to +2.6 dB (lossless) at J = −1 in the open-end phase. The §9.4 figures are marked 'upper bounds, not a point', and the other phase is given as −3.5 dB (lossless) / −1.9 dB (§9.4). A grep for '+0.04 to +2.6' finds 0 hits. Re-executed with released regen: a_loss 0.7451522890452021; delivered drive −1.000 … +2.582 dB, monotone in |r|. At §9.4's |r| = 0.1509 the loop is 0.1426, passive delivered +0.036 dB and regen +0.300 dB; in the other phase passive delivered is −1.925 dB.
- 🧵 RE4 (name the DS drain-factor assumption): LANDED. Item 2 states 'the loaded loop is regen.loop_gain(M) × |r|, which keeps the released DS drain factor (1 + M)/(1 − M) at a drain that a transmitting junction no longer current-clamps', labelled in-model and open. §2 bullet 2 and limitation 1 repeat it.
- 🧵 RE5 (headline ranges; the sign-off's denomination): LANDED. The title reads '6.2–8.1 dB (peak) / 8.6–10.4 dB (slot-mode)'. The sign-off reads '6.2–8.1 dB shallower … in peak `cav` under the promoted rule (9.1–9.3 dB at the lattice-optimal placements)'. Recomputed from the 42 rows of appendix Table 5: peak 6.16–8.11 and slot-mode 8.63–10.41 over all rows; 6.16–7.98 and 8.63–10.28 at J ≥ −6.
- 🧵 RE6 (the latency range includes the N = 720 row; the excess given across the grid): LANDED AS REQUESTED. Item 7 and the latency key now read 0.518–0.525 rt with the excess at '0.024 → 0.022 → 0.018 rt at N = 240 / 480 / 720'. The N = 720 rung it adds is a different junction class, however (new required edit 2). The N = 720 family (runs/N720_m30_s7.json, primary_J −6) ran only J = −6 / −3. My J = −6 N = 720 passive chain gives 0.5181 rt, which reproduces the printed 0.518, while my J = −1 N = 720 chain gives 0.5218 rt.
- 🌊 RE1 (Table 9 row iii; item 4's split; correct the round-3 record): LANDED. The Table 9 and item 4 changes are the same as 🧵 RE1, with the same re-execution. The round-4 record's section 'Corrections to the round-3 record' corrects row 12: the labelled construction does reproduce −13.09.
- 🌊 RE2 (residue caption, plane mislabel): LANDED. Denominator (a) is now 'the mean-'1' drain-density peak inside the promoted window … the denominator of 08-02 §3.2's `drn_h` floor column (not of the promoted `max0_below_mean1_dB`, which is a source-plane `cav` ratio)'. A grep for 'promoted floor key's own' finds one hit, inside the round-4 disclosure paragraph. Measured at m = 28: `cav` −10.731214907969104 against `drn_h` −11.150570102407642.
- 🌊 RE3 (headline precision): LANDED. The title and item 4's lead now read 8.6–10.4 dB slot-mode. The title says 'or, in slot-mode, at cfl = 0.2', and item 4 says 'in slot-mode only at cfl = 0.2'. Item 4 now prints '5.5 dB at cfl = 0.8' as a positive degradation; a grep for '-5.5' hits only the model name `claude-opus-5-5`.
- 🌊 RE4 (scope every copy of the loaded-drain range): LANDED. Item 3, §4 row 1 and the §5 passive-transfer key all read '−1.0 to +2.6 dB at J = −1 in the open-end phase (−3.5 dB in the other; < +0.04 dB for any junction §9.4 allows)'. The false 'between the two' has been replaced by 'near the booked link, far from the ideal buffer'. My J = −1 values support that wording: lossless −3.529 dB in the other phase; §9.4 bound +0.036 dB.
- 🌊 RE5 (complete ⚛️ RE10, the DS factor): LANDED (see 🧵 RE4).
- 🌊 RE6 (limitation 9's flush item, standing rule 10): LANDED. Limitation 9 now reads 'The flush question 07-22-cavity-ringdown-isi §7.3 raised was resolved in the record at the 4-ps slot (its post-promotion annotation; 07-22-flush-noise-figure-negative; 07-23-reset-switch-adjudication, per INDEX) and is not re-examined here'. Checked against notes/INDEX.md row 41: '✅ §7.3's sufficiency question resolved — passive flush insufficient (07-22 flush) and no de-Q rate closes flushed F = 2'.
- 🌊 RE7 (appendix Table 5 caption): LANDED. The caption reads '(window rule shift = passive-chain latency, rounded to the ⅛-rt grid; the ideal-buffer density coupling of §2; released cfl = 0.4; the cell-1 columns at the promoted window)'. My diff finds the 42 data rows and the header byte-identical to the published round-1 Table 5.
- 🌊 RE8 (correct the round-3 record): LANDED, in the round-4 record's 'Corrections to the round-3 record'. It covers row 5 (⚛️ RE10 had been only half applied), row 12 (−13.09 reproduced), the 'What was not changed' paragraph (Tables 4 / 6 were already numbered; the Table 5 caption was lost; the stale-split source for Table 5) and the overstated 'all 29 … applied'.
- ⚛️ RE1 (Table 9 row iii and the shares): LANDED (see 🧵 RE1). The Table 9 note and the round-3 record's claim are both corrected.
- ⚛️ RE2 (the late-window 'bar crossed' claim is a mixed-window ratio): LANDED AS REQUESTED. Table 3c's caption now says 'a *mixed* ratio'. The new Table 3d prints the matched ratio, and the rescoped universal is carried in item 1(c), item 6, the §4 G4 row, limitation 6 and the discriminant. I re-executed every printed Table 3d row to the printed digit; for example m = 28, lo 0.80 gives mixed 1.7308, matched 1.6955, single 8.301 dB, floor −10.079. I checked the universal over the whole slot, lo 0–1 on a 0.0025 lattice, at both rungs, with the exact lag and with the ⅛-rt-rounded lag, and it holds. However, the range statements built on it claim a census over 'every round-spec placement' from a scan restricted to lo ∈ [0.74, 0.83]. The text's own Table 3c contradicts them (new required edit 1).
- ⚛️ RE3 (bound direction inverted in item 2): LANDED (see 🧵 RE3). The loaded loop re-derived monotone in |r|: 0.4286 lossless / 0.3219 at 11.6 % / 0.1426 at §9.4's bound.
- ⚛️ RE4 (name the DS-factor assumption; correct the 'all 29' claim): LANDED. The assumption is named in item 2, §2 bullet 2 and limitation 1. The round-4 record corrects 'all 29 … applied'.
- ⚛️ RE5 (appendix captions carry their own scope): LANDED. Table 5's caption now carries its scope (see 🌊 RE7). Table 2b's caption now spells out its convention: 'the single released cell driven at its source clamp by the duty-0.8 gated launch at amplitude A, over its identical passive twin, promoted window, ratio bias, cfl = 0.4, seed 7'. Table 2b's rows are byte-identical to round 1's.

REQUIRED EDITS:
- 1. (New in round 4. Affects item 1(c), item 6, the §4 G4 row and its reason, limitation 6, the note under Table 3d and the discriminant's parenthetical.) The matched-window census was scanned only over lo ∈ [0.74, 0.83]: rw4_stored.py loops `np.arange(0.74, 0.8301, 0.0025)`. Its range statements are nevertheless made for 'every round-spec placement', and the text's own Table 3c contradicts them: at m = 30, lo 0.70 it prints a stage-2 floor of −10.08 dB (round spec) with G4_A 1.582. I re-executed the whole slot (lo 0–1 on a 0.0025 lattice, m = 30 and 28, N = 240, seed 7, cfl 0.4). At m = 30 the round-spec placements are lo 0.700–0.790, 37 contiguous lattice points, 16 of them outside the scanned domain. Over them the mixed G4_A is 1.582–1.633 and the matched G4 1.573–1.624; at lo 0.700–0.7375 the matched value is 13.110 / 8.337 = 1.5726. Correct the following: (a) 'lo 0.74–0.79 at m = 30' should read lo 0.70–0.79; (b) 'it reads 1.62–1.63 (m = 30, lo 0.74–0.79)' should read 1.58–1.63; (c) 'matched G4 at every round-spec placement is 1.61–1.62 (m = 30)', and '1.61–1.62 / 1.63–1.70' in the §4 row, should read 1.57–1.62. (d) Print the m = 28 top as 1.695, not '1.70', wherever it is called 'below the bar'. Its margin under the bar is 0.0045 in G4, or 0.037 dB of chain gain, at a floor of −10.079 dB; that margin is smaller than the rule's own ⅛-rt step (0.012 in G4 at J = −1), so print it. (e) 'Crosses the bar … only where the stage-2 floor fails the round spec or at a plateau edge' is inaccurate. At m = 28 the mixed ratio is ≥ 1.7 at 9 of the 11 round-spec lattice points (lo 0.7975–0.8175), not at an edge. (f) State the lattice and the domain of the census. The enumerations '(m = 30, lo ≥ 0.81, floor −7.3 to −8.6 dB; m = 28, lo = 0.83, floor −8.4 dB)' are bounded by the scan's own domain: outside it the matched ratio is ≥ 1.7 at m = 28, lo 0.8325–0.95 (floors −8.36 to −3.17 dB) and at m = 30, lo 0.8325–0.95 (floors −7.02 to −2.07 dB). The universal conclusion itself survives unchanged: over the whole slot, no placement gives both a round-spec floor and matched G4 ≥ 1.7, at either rung and with either the exact or the ⅛-rt-rounded lag.
- 2. (New in round 4. Affects item 7 and the §5 `cascade_stage_latency_rt` key.) The grid ladder '0.525 at N = 240, 0.523 at N = 480, 0.518 at N = 720' and the excess '0.024 → 0.022 → 0.018 rt at N = 240 / 480 / 720 … moves with the grid' mix junction classes. The N = 720 family ran only J = −6 / −3 (runs/N720_m30_s7.json: primary_J −6), so its 0.518 is a J = −6 passive chain, while the N = 240 / 480 rungs are J = −1. I re-executed passive chains (m = 30, seed 7, cfl 0.4, same estimator: whole-slot argmax of |drn_h|, '1' slots). At J = −1 the lag is 0.5243 / 0.5222 / 0.5218 rt, an excess of 0.024 / 0.022 / 0.022. At J = −6 it is 0.5229 / 0.5194 / 0.5181 rt, an excess of 0.023 / 0.019 / 0.018; the 0.5181 reproduces the printed 0.518. At fixed N = 240 the lag also moves with junction class: 0.5250 / 0.5243 / 0.5229 rt at J = 0 / −1 / −6. Label the N = 720 figure's junction class, or replace it with the J = −1 value (≈ 0.022 rt excess). Also state that the open excess moves with drive amplitude (junction class) at fixed N and cfl, so 'a scheme-borne phase term' is incomplete. The key's range across families (0.518–0.525 rt) and its band are unaffected.
- 3. (Item 5.) Change 'the active delivered wave is … < +0.3 dB under §9.4's bound' to < +0.34 dB. In the released loop model at §9.4's |r| = 0.1509, open-end phase, the active delivered wave is |t|/(1 − loop·|r|) = +0.336 dB. The re-execution log of round-4-record.md prints the same +0.34. As written, the bound excludes junctions with |r| ≈ 0.135–0.151, which §9.4 allows.
- 4. (Header of comment A, line 15.) The paragraph '**Rework history, disclosed (stage 4 of the routine; this is the round-3 text).**' still calls itself the round-3 text inside the round-4 text, directly above '**Round 4 (the cap; this text).**'. Relabel it as the round-3 rework history.

TOP ISSUES:
- REQUIRED (evidence for required edit 1). The matched-window census covers a truncated domain. rw4_stored.py scans lo ∈ [0.74, 0.83] only, yet the text claims 'at every round-spec placement'. The full-slot re-execution (0.0025 lattice) at m = 30 puts the round-spec stage-2 placements (floor ≤ −10 dB) at lo 0.7000–0.7900, 37 contiguous points. The 16 points outside the scanned domain (lo 0.7000–0.7375) read floor −10.08 to −10.39, mixed 1.5819–1.6156 and matched 1.5726–1.6061. Table 3c's own lo 0.70 row (−10.08 dB, 13.110, 1.582) shows this. At m = 28 the round-spec placements are lo 0.7925–0.8175, all 11 inside the domain, with matched 1.6336–1.6955, reproduced. At m = 28 the mixed ratio is ≥ 1.7 at 9 of the 11 round-spec points. The headline universal holds over the whole slot, at both rungs, with the exact lag (0.0856 / 0.0913 slot) and with the ⅛-rt-rounded lag (0.0875 / 0.0893 slot). The stated ranges and the 'plateau edge' description do not hold.
- REQUIRED (evidence for required edit 2). The latency ladder confounds grid with junction class. Passive peak-to-peak lag (rt) from my runs: J = −1 gives 0.5243 (N = 240) / 0.5222 (480) / 0.5218 (720); J = −6 gives 0.5229 / 0.5194 / 0.5181; at N = 240, J = 0 gives 0.5250. The printed 0.518 at N = 720 is the J = −6 family's figure. At fixed J = −1 the lag moves only 0.0004 rt between N = 480 and N = 720. The amplitude dependence at fixed scheme (0.0021 rt between J = 0 and J = −6) is itself informative for the open excess: part of it is nonlinear (shallow-water c = √h at a drain perturbation of 4–8 %), not only scheme-borne. That is in-model, from my runs.
- REQUIRED (evidence for required edits 3 and 4). At |r| = 0.1509 the active delivered wave is +0.336 dB (p2_loop.py), and item 5 prints '< +0.3 dB'. Line 15 of the round-4 text still reads 'this is the round-3 text'.
- Verified, not a defect: the table regression is fully absent. A row-by-row diff of round-4-reply.md plus round-4-tables-appendix.md against 11-reply.md finds identical rows for Table 1 (18 data rows), 2a (28), 2b (10), 3 (10), 3b (8), 4 (16), 5 (42), the residue table (2) and 6 (11). Only the captions changed: Table 1's caption paragraph and the headings of Tables 2b and 5 and the residue table, as the round-4 record states. The only tables new since round 1 are 3c, 3d, 8 and 9. Table 9's rows (iii) and (iv) now carry the constructions they name; I re-executed both, and both round-2 seats' −13.09 reproduce.
- Verified, not a defect: no withdrawn or stale statement survives outside a disclosure sentence. The following occur only inside explicit withdrawal or disclosure sentences: 'released coupling', 'released cascade', 'released model's own', '7–9', '9–10', 'could build', '+0.04 to +2.6', '3.2–4.4', '0.523–0.525', '1.43', '44 dB', 'LF half-step', 'every placement', 'byte-identical', 'no measured number changed', 'promoted floor key's own'. Every 'Table 7' reads 'Part I Table 7'. The one stale item is required edit 4.
- Standing rule 10, both directions. Clean. The ring-down mechanism is credited to 07-22-cavity-ringdown-isi and 08-12. The single-cell cfl column is credited to 08-12's registered key. The M = 0 α values 0.9972 / 0.9976 / 0.9992 are in 08-13 line 33 as quoted, and the phase-leg cfl law (0.59 → 0.86 → 1.01) is in 08-13 line 55. The plane facts come from 08-02 §3.1 and its vote record, and the early window clause from 08-12 line 128. Nothing is re-announced: a grep of notes/ finds no time-domain two-cell cascade, no junction-reflection loading of the DS loop, and no late-window scoping of the single-cell floor. 08-02 §2.4 is the static map composition, a different object. Nothing contradicts a promoted note.
- Scoping is non-vacuous. Every two-cell claim is conditioned on the ideal-buffer coupling, cfl = 0.4 and the pre-registered rule, and the durable content survives that scoping. That content is: the matched-amplitude grade of 08-01 §4 (Δ ≤ 0.6 dB); ring-down non-transfer of a windowed floor, with ablation (i) taking the floor from −4.696 to −9.380 dB, re-executed; '≈ 2×' as the 1.96 small-signal limit; and the late-window scoping of the single cell's own floor. On my fine lattice the cell-1 optimum is −20.140 dB at lo 0.5769 (m = 30) and −19.139 dB at 0.5887 (m = 28), identical to the lattice values. The 'not fine-scanned' caveat on the 9.3 / 9.1 dB degradation can therefore be lifted (optional).
- The loaded-drain figures are a fairly stated range with both assumptions named: open-end phase, and the DS drain factor retained. I re-derived all of them with released regen.loop_gain: loop 0.9450 → 0.4286 (ratio bias) and 0.9162 → 0.4155 (analytic); passive delivered −1.000 … +2.582 dB, monotone; active +3.861 dB; standing wave +6.83 dB; §9.4 bound 0.1426 / +0.036 / +0.300 dB; the other phase −3.529 / −1.925 dB; 11.6 % gives 0.3219 / +1.543 / +0.831 dB. The ring-down rate implied by the loop at 30 rt per slot is −14.73 dB/slot at the ratio bias and −22.81 at the analytic bias; the effective loop for 08-12's −24.38 dB/slot is 0.9107. The CW-form G4 at J = −1 spans 0.957–1.096, consistent with '≈ 1.0–1.1'. The one numerical slip is required edit 3.
- Optional, on the discriminant's framing. It is honest that its central band belongs to a construct no passive junction realizes, and that a passive-junction die is expected in the '< 1.40' arm. The '> 1.7' reading could also list a common late placement of both stages: the matched ratio reaches 1.71–1.81 at m = 30, lo 0.8075–0.90, with the stage-2 floor failing (−8.59 to −4.15 dB), a reading the pinned stage-1 window excludes only implicitly. Consider re-registering the discriminant as one-sided.
- Optional. The note under Table 9 says the round-1 ⚛️ seat's −14.11 dB 'came with a construction it did not specify'. That seat did describe it in words ('duty-0.8 gate removing everything after 0.8·repT', on top of the '0'-residue gate), and the words match rows (iii) and (iv), neither of which reproduces the number. Say that instead.
- Optional. 'No measured number changed' in the round-4 disclosure paragraph should say that Table 9 row (iii)'s printed values changed to the labelled construction's (the −13.81 dB value moved to row iv). Also optional: 'A further caveat: and 08-12 §3 …' in item 2 has a stray 'and'. Item 1(c)'s 'for any stage-2 window with lo ≤ 0.75' holds only for lo ≥ 0.25: earlier windows give a mixed ratio of 1.42 (m = 30) and 1.36 (m = 28) on my lattice, with floors near 0 dB.
- Optional, on the record's logistics. The three-comment split is acceptable: comments A / B / C are 42,921 / 23,604 / 21,844 characters. The listings comment is 12-listings.md (55,553) plus the appendix (4,923), 60,476 characters, which is under GitHub's 65,536. PASTE-ORDER.md's 'further listings comment' for the rework listings cannot hold build_r4.py (75,665 characters) alone; it needs its own split. The promoted note must carry the appendix, and a script-path promotion must not read only 60,000 characters (the text is 88,407); PASTE-ORDER.md already says both.
- Disclosures are honest and complete apart from the round-4 items above. They cover the round-2 regression and its cause; the withdrawal of round 2's 'byte-identical' and 'no measured number changed'; the round-3 record's inaccuracies, corrected in the round-4 record; round 4's single withdrawal (the late-window 'bar crossed' claim, rescoped); the rw4_runs.py import side effect; the declined time-domain loaded-drain run (limitation 1, credited); and the executing model and platform.
- Reproduced and accepted, all on my own instrument against the released, unedited chain. M_th_num(240) = 0.16894319463373797 (3.3×10⁻¹⁶ relative; exact equality False). Gate: 8.287855791924049 / −11.828336851446547 / −11.775002445228234 (3.86×10⁻¹⁵ / 5.68×10⁻¹⁴ / 1.32×10⁻¹³). m = 28: 8.131548730367582 / −10.731214907969104 / −11.150570102407642. Passive transfer 15.8296 / 15.8117 dB; relaunch −24.600 / −24.336 dB. J = −1 chain at 2.625 rt: 13.1033 / 13.3990, G4_A 1.5810 / 1.5932 (drn_h 1.5498), floors −4.696 / −4.307 / −6.257, eye +4.395, pp 0.750. At 2.568 rt: 12.9998, −4.637 / −6.214. m = 28 at 2.5 rt: 12.9173, G4_A 1.5885, floors −4.024 / −4.317 / −5.245. Envelope lags: passive 2.5681 / 2.5556 rt, active 5.7045 / 5.7298 rt. Every printed Table 3d row. Table 9 rows (i)–(iv). The loop-model range. Passive transfer 16.23 dB (N = 480) and 16.37 dB (N = 720).

SEAT MODEL NOTE: This seat is the Kinetic 🌊 round-4 re-assessor (reassess4-kinetic). The maintainer requested it on claude-opus-5-5 for this run, as the 2026-08-13 policy's Opus re-assessor seat. It is not Fable 5 and does not claim to be. It shared no context with the drafting, the execution, the pre-publication checks, the round-1 to round-3 assessors, the reworks or the other round-4 re-assessors, and it held every prior round's record. The reply under assessment was executed and reworked on claude-fable-5-1. This seat executed every number in this verdict on Linux x86_64 / Python 3.11.15 / numpy 2.4.6, against the released, unedited fable-model-chain/, using its own instrument written from the reply's stated definitions: 11 solver runs and one threshold scan. Reproductions are gated on relative deviation, ≤ 1.32×10⁻¹³ on the gate row. Exact equality was measured False and is not claimed. run_all.py was never run, and the repository tree was left clean (git status: 0 lines). — Kinetic 🌊 (AI research agent · see agents/README.md)

<details><summary>Re-execution log (verbatim)</summary>

```text
Seat directory: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/reassess4-kinetic/

Own instrument k4.py, written from the reply's §1–§2 definitions and the promoted 07-31 exp_duty/fs_driver logic:
- It imports the released fable-model-chain/ unedited (solver._setup/_step_LF) and uses the released dt rule.
- Cell 2's clamp is h_left = 1 + κ·g(t)·(h1[−1] − 1), read from cell 1's drain after cell 1's update in the same step (exact lockstep).
- Scoring: my own per-slot peaks, worst/mean-'1' gain over the identical passive run, floor = max-'0' over mean-'1', and a complex lock-in slot mode.
- The session's cascade_driver.py was not used.
- PYTHONDONTWRITEBYTECODE=1 throughout. run_all.py was never run. `git status --short | wc -l` → 0.

$ python3 p0_mth.py   (run_all.measure_Mth_num logic, released SOL.growth_rate)
M_th_num(240) = np.float64(0.16894319463373797)  shipped 0.16894319463373791  rel dev 3.286e-16  exact equal: False  [32s]
bias 0.7*M_th_num(240) = np.float64(0.11826023624361658)
3.11.15 2.4.6 Linux x86_64

$ python3 p1_runs.py act 30 | pas 30 | act 28 | pas 28   (N = 240, 40 slots, seed 7, duty 0.8, amp 2e-3, cfl 0.4, J = −1; the m = 30 active run carries cell 2 plus ablation cells (i)–(iv))
A_m30_N240 steps 1898294 dt 0.0012642926038760258 398s x86_64
P_m30_N240 steps 1728000 dt 0.001388888888888889 190s x86_64
A_m28_N240 steps 1771741 dt 0.0012642926038760258 193s x86_64
P_m28_N240 steps 1612800 dt 0.001388888888888889 182s x86_64

$ python3 p3_score.py 30
=== m = 30, N = 240, seed 7, cfl 0.4: active dt 1.264293e-03 steps 1898294; passive dt 1.388889e-03 steps 1728000
 cell 1 (promoted window): cav Gw 8.287855791924049 Gm 8.4102 floor -11.828336851446547; drn_h floor -11.775002445228234; slot-mode floor -15.665
   GATE G_worst1: 8.287855791924049 vs promoted 8.287855791924017: rel dev 3.86e-15; exact equal False
   GATE floor cav: -11.828336851446547 vs promoted -11.828336851447219: rel dev 5.68e-14; exact equal False
   GATE floor drn_h: -11.775002445228234 vs promoted -11.775002445226676: rel dev 1.32e-13; exact equal False
 passive cell-1 mean-'1' |drn_h| 0.012374 -> passive port density transfer 15.8296 dB
 active cell-1 mean-'1' |drn_h| 0.033965 -> relaunch junction -24.600 dB; cell-2 input at J=-1 0.03027
 passive stage-1->2 envelope lag 5.1361 units = 2.5681 rt (demeaned 2.5681 rt); active 5.5262 rt; passive peak-time lag median 0.5243 rt [min 0.5243, max 0.5243]
  J=-1 chain, shift 2.6250 rt: chain/passive worst 13.1033 mean 13.3990 | G4_A worst 1.5810 mean 1.5932 (drn_h 1.5498) | floor cav -4.696 drn_h -4.307 mode -6.257 | eye +4.395 pp 0.750 | n 40
  J=-1 chain, shift 2.5681 rt: chain/passive worst 12.9998 mean 13.3371 | G4_A worst 1.5685 mean 1.5858 (drn_h 1.5498) | floor cav -4.637 drn_h -4.307 mode -6.214 | eye +4.292 pp 0.853 | n 40
  J=-1 chain, shift 2.5000 rt: chain/passive worst 12.9998 mean 13.3371 | G4_A worst 1.5685 mean 1.5858 (drn_h 1.5498) | floor cav -4.637 drn_h -4.307 mode -6.163 | eye +4.292 pp 0.853 | n 40
  ABLATION (i): floor cav -9.380 drn_h -8.822 mode -12.978 | chain 13.103 eye +9.083
  ABLATION (ii): floor cav -12.537 drn_h -12.081 mode -16.217 | chain 13.127 eye +12.251
  ABLATION (iii) gate(i)+hard '1' cut: floor cav -13.086 drn_h -12.638 mode -16.820 | chain 13.131 eye +12.802
  ABLATION (iv) hard '0' + hard '1' cut: floor cav -13.807 drn_h -13.363 mode -17.528 | chain 13.131 eye +13.523
 SCAN lo 0..1 step 0.0025: lag exact 0.0856 slot, rule-rounded 0.0875 slot
  round-spec stage-2 placements (floor <= -10 dB): lo 0.7..0.79 (count 37, contiguous: True)
   mixed G4_A 1.5819..1.6334; MATCHED (exact lag) 1.5726..1.6239; matched (rule-rounded lag) 1.5726..1.6239
   placements with BOTH round-spec floor and matched G4 >= 1.7: exact lag []; rule-rounded lag []
  matched (exact) >= 1.7 at lo: [0.0, 0.0025, 0.005]..[0.995, 0.9975, 1.0] floors 0.53..-8.59
   lo 0.6000: stage-2 floor cav   -8.35 (mode  -11.09, n 39) | chain 13.110 mixed 1.5819 | matched(exact) 1.5726 [single 8.337] | matched(rule) 1.5726 [single 8.337]
   lo 0.6900: stage-2 floor cav   -9.35 (mode  -12.43, n 39) | chain 13.110 mixed 1.5819 | matched(exact) 1.5726 [single 8.337] | matched(rule) 1.5726 [single 8.337]
   lo 0.7000: stage-2 floor cav  -10.08 (mode  -12.35, n 39) | chain 13.110 mixed 1.5819 | matched(exact) 1.5726 [single 8.337] | matched(rule) 1.5726 [single 8.337]
   lo 0.7200: stage-2 floor cav  -10.08 (mode  -12.83, n 39) | chain 13.110 mixed 1.5819 | matched(exact) 1.5726 [single 8.337] | matched(rule) 1.5726 [single 8.337]
   lo 0.7400: stage-2 floor cav  -10.38 (mode  -12.76, n 39) | chain 13.390 mixed 1.6156 | matched(exact) 1.6061 [single 8.337] | matched(rule) 1.6061 [single 8.337]
   lo 0.7700: stage-2 floor cav  -10.86 (mode  -13.08, n 39) | chain 13.512 mixed 1.6303 | matched(exact) 1.6208 [single 8.337] | matched(rule) 1.6208 [single 8.337]
   lo 0.7900: stage-2 floor cav  -10.19 (mode  -13.57, n 39) | chain 13.537 mixed 1.6334 | matched(exact) 1.6239 [single 8.337] | matched(rule) 1.6239 [single 8.337]
   lo 0.8000: stage-2 floor cav   -8.59 (mode  -13.43, n 39) | chain 13.539 mixed 1.6336 | matched(exact) 1.6241 [single 8.337] | matched(rule) 1.6241 [single 8.337]
   lo 0.8075: stage-2 floor cav   -8.59 (mode  -13.43, n 39) | chain 14.612 mixed 1.7631 | matched(exact) 1.7108 [single 8.541] | matched(rule) 1.7059 [single 8.565]
   lo 0.8250: stage-2 floor cav   -8.41 (mode  -13.87, n 39) | chain 14.486 mixed 1.7479 | matched(exact) 1.7110 [single 8.467] | matched(rule) 1.7110 [single 8.467]
   lo 0.8300: stage-2 floor cav   -7.33 (mode  -13.82, n 39) | chain 14.486 mixed 1.7479 | matched(exact) 1.7110 [single 8.467] | matched(rule) 1.7110 [single 8.467]
   lo 0.8500: stage-2 floor cav   -7.01 (mode  -14.08, n 39) | chain 15.433 mixed 1.8621 | matched(exact) 1.6462 [single 9.375] | matched(rule) 1.6462 [single 9.375]
   lo 0.9000: stage-2 floor cav   -4.15 (mode  -12.83, n 39) | chain 14.137 mixed 1.7057 | matched(exact) 1.8137 [single 7.794] | matched(rule) 1.8089 [single 7.815]
   (intermediate lo rows omitted here; full output in out/p3_score_30.log)
[n counts slots before the 4 dropped: n 40 → 36 scored, n 39 → 35, as in the reply]

$ python3 p3_score.py 28
=== m = 28, N = 240, seed 7, cfl 0.4: active dt 1.264293e-03 steps 1771741; passive dt 1.388889e-03 steps 1612800
 cell 1 (promoted window): cav Gw 8.131548730367582 Gm 8.2231 floor -10.731214907969104; drn_h floor -11.150570102407642; slot-mode floor -14.610
 passive cell-1 mean-'1' |drn_h| 0.012349 -> passive port density transfer 15.8117 dB
 active cell-1 mean-'1' |drn_h| 0.032948 -> relaunch junction -24.336 dB; cell-2 input at J=-1 0.02937
 passive stage-1->2 envelope lag 5.1111 units = 2.5556 rt (demeaned 2.5556 rt); active 5.5629 rt; passive peak-time lag median 0.5243 rt [min 0.5236, max 0.5243]
  J=-1 chain, shift 2.5000 rt: chain/passive worst 12.9173 mean 13.2814 | G4_A worst 1.5885 mean 1.6151 (drn_h 1.5551) | floor cav -4.024 drn_h -4.317 mode -5.245 | eye +3.653 pp 0.897 | n 40
 SCAN lo 0..1 step 0.0025: lag exact 0.0913 slot, rule-rounded 0.0893 slot
  round-spec stage-2 placements (floor <= -10 dB): lo 0.7925..0.8175 (count 11, contiguous: True)
   mixed G4_A 1.6641..1.7308; MATCHED (exact lag) 1.6336..1.6955; matched (rule-rounded lag) 1.6315..1.6955
   placements with BOTH round-spec floor and matched G4 >= 1.7: exact lag []; rule-rounded lag []
   lo 0.7900: stage-2 floor cav   -9.99 | chain 13.532 mixed 1.6641 | matched(exact) 1.6336
   lo 0.7975: stage-2 floor cav  -10.08 (mode -12.16) | chain 13.852 mixed 1.7035 | matched(exact) 1.6687 [single 8.301]
   lo 0.8000: stage-2 floor cav  -10.08 (mode -12.19) | chain 14.074 mixed 1.7308 | matched(exact) 1.6955 [single 8.301] | matched(rule) 1.6955
   lo 0.8200: stage-2 floor cav   -9.19 | chain 14.074 mixed 1.7308 | matched(exact) 1.6955
   lo 0.8300: stage-2 floor cav   -8.36 | chain 14.156 mixed 1.7409 | matched(exact) 1.7053 [single 8.301] | matched(rule) 1.6791 [single 8.431]
   lo 0.8400: stage-2 floor cav   -8.23 | chain 15.321 mixed 1.8841 | matched(exact) 1.7038 [single 8.992]
   lo 0.8500: stage-2 floor cav   -8.11 | chain 15.231 mixed 1.8731 | matched(exact) 1.6939
   lo 0.9000: stage-2 floor cav   -5.17 | chain 14.577 mixed 1.7926 | matched(exact) 1.7865 [single 8.159]
   (full output in out/p3_score_28.log)

$ python3 p7 (Table 3d, printed vs mine; round-spec census)
 m=30 lo 0.7400: printed 1.616 / 1.606 / 8.337 / -10.38 | mine 1.6156 / 1.6061 / 8.337 / -10.384
 m=30 lo 0.7675: printed 1.616 / 1.606 / 8.337 / -10.86 | mine 1.6156 / 1.6061 / 8.337 / -10.865
 m=30 lo 0.7700: printed 1.630 / 1.620 / 8.337 / -10.86 | mine 1.6303 / 1.6208 / 8.337 / -10.865
 m=30 lo 0.7900: printed 1.633 / 1.624 / 8.337 / -10.20 | mine 1.6334 / 1.6239 / 8.337 / -10.187
 m=30 lo 0.8000: printed 1.634 / 1.624 / 8.337 / -8.59 | mine 1.6336 / 1.6241 / 8.337 / -8.590
 m=30 lo 0.8075: printed 1.763 / 1.711 / 8.541 / -8.59 | mine 1.7631 / 1.7108 / 8.541 / -8.588
 m=30 lo 0.8250: printed 1.748 / 1.711 / 8.467 / -8.41 | mine 1.7479 / 1.7110 / 8.467 / -8.408
 m=30 round-spec lattice points: 37, lo 0.7000..0.7900; of these inside the reply's scan domain [0.74, 0.83]: 21
  round-spec placements OUTSIDE the scan domain: lo 0.7000..0.7375; mixed 1.5819..1.6156; matched 1.5726..1.6061; floors -10.08..-10.39
  mixed ratio >= 1.7 at round-spec placements: 0 of 37 lattice points
  matched >= 1.7 beyond the scan domain (0.83 < lo < 0.96): lo 0.8325: 1.711 (floor -7.02), lo 0.8800: 1.792 (floor -4.96), lo 0.9000: 1.814 (floor -4.15), lo 0.9500: 2.019 (floor -2.07)
 m=28 lo 0.7925: printed 1.664 / 1.634 / 8.283 / -10.08 | mine 1.6641 / 1.6336 / 8.283 / -10.079
 m=28 lo 0.7950: printed 1.665 / 1.635 / 8.284 / -10.08 | mine 1.6655 / 1.6347 / 8.284 / -10.079
 m=28 lo 0.7975: printed 1.703 / 1.668 / 8.301 / -10.08 | mine 1.7035 / 1.6687 / 8.301 / -10.079
 m=28 lo 0.8000: printed 1.731 / 1.695 / 8.301 / -10.08 | mine 1.7308 / 1.6955 / 8.301 / -10.079
 m=28 lo 0.8175: printed 1.731 / 1.695 / 8.301 / -10.08 | mine 1.7308 / 1.6955 / 8.301 / -10.079
 m=28 lo 0.8200: printed 1.731 / 1.695 / 8.301 / -9.20 | mine 1.7308 / 1.6955 / 8.301 / -9.193
 m=28 lo 0.8300: printed 1.741 / 1.705 / 8.301 / -8.36 | mine 1.7409 / 1.7053 / 8.301 / -8.361
 m=28 round-spec lattice points: 11, lo 0.7925..0.8175; inside the scan domain: 11
  mixed ratio >= 1.7 at round-spec placements: 9 of 11 lattice points (lo 0.7975..0.8175)
  matched >= 1.7 beyond the scan domain: lo 0.8325: 1.719 (floor -8.36), lo 0.9025: 1.787 (floor -5.17), lo 0.9525: 2.103 (floor -3.17)

$ python3 p8 (early placements; cell-1 fine optimum)
m=30: mixed G4_A over lo in [0, 0.75]: 1.4184 (lo 0.1300, floor -1.09) .. 1.6156 (lo 0.7375); over lo in [0.25, 0.75]: 1.5307 .. 1.6156
   deepest single-cell floor on the fine lattice (window lo - lag): -20.140 dB at single-cell lo 0.5769
m=28: mixed G4_A over lo in [0, 0.75]: 1.3563 (lo 0.0000, floor 0.81) .. 1.5999 (lo 0.3700); over lo in [0.25, 0.75]: 1.5473 .. 1.5999
   deepest single-cell floor on the fine lattice (window lo - lag): -19.139 dB at single-cell lo 0.5887

$ python3 p5 (active envelope lag, demeaned estimator)
m=30: active stage-1->2 envelope lag, demeaned: 5.7045 rt; raw: 5.5262 rt; passive demeaned 2.5681 rt
m=28: active stage-1->2 envelope lag, demeaned: 5.7298 rt; raw: 5.5629 rt; passive demeaned 2.5556 rt

$ python3 p2_loop.py   (released regen._cavity / loop_gain; the reply's item-2 formulas)
a_loss 0.7451522890452021; loop(ratio bias) 0.9450; loop(analytic 0.7 Mth) 0.9162; loop(0) 0.7452; unloaded 2/(1-a) = +17.89 dB
 J=-1 lossless   r=+0.4535: loaded loop +0.4286 (analytic +0.4155); delivered passive +2.582 active +3.861 dB; loaded CW regen +1.279 (analytic +1.082); CW-form G4 1.096
 J=-1 lossless   r=-0.4535: loaded loop -0.4286 (analytic -0.4155); delivered passive -3.529 active -4.098 dB; loaded CW regen -0.569 (analytic -0.490); CW-form G4 0.957
 J=-1 s9.4 bound r=+0.1509: loaded loop +0.1426 (analytic +0.1382); delivered passive +0.036 active +0.336 dB; loaded CW regen +0.300 (analytic +0.256); CW-form G4 1.023
 J=-1 s9.4 bound r=-0.1509: loaded loop -0.1426 (analytic -0.1382); delivered passive -1.925 active -2.158 dB; loaded CW regen -0.232 (analytic -0.199); CW-form G4 0.983
 J=-1 11.6%      r=+0.3406: loaded loop +0.3219 (analytic +0.3120); delivered passive +1.543 active +2.374 dB; loaded CW regen +0.831 (analytic +0.706); CW-form G4 1.062
 J=-1 11.6%      r=-0.3406: loaded loop -0.3219; delivered passive -2.964 active -3.424 dB; loaded CW regen -0.459; CW-form G4 0.966
 J=-1 |r|->0     r=+0.0000: loaded loop +0.0000; delivered passive -1.000 active -1.000 dB; loaded CW regen +0.000; CW-form G4 1.000
 (J = -3 / -6 rows in out/p2_loop.log; e.g. J=-3 lossless open-end passive +3.489, J=-6 lossless other phase passive -10.322)
J=-1 open-end phase, |r| in [0, 0.4535]: passive delivered -1.000 .. +2.582 dB (monotone: True); active -1.000 .. +3.861
J=-1 under s9.4 bound |r| < 0.1509: loop < 0.1426; passive delivered < +0.036; ACTIVE delivered < +0.336 dB; regen < +0.300 dB; other phase at bound: passive -1.925
regen.cw_net_gain_dB-consistent unloaded CW regen at ratio bias: 13.324 analytic: 9.661
dB/slot implied by loop at m=30 (30 rt/slot): -14.73 ratio; -22.81 analytic; effective loop for -24.38 dB/slot: 0.9107

$ python3 p1b_lat.py 480 ; p1b_lat.py 720   (passive J = -1 chain, m = 30, first 16 slots; causal, so identical to a 40-slot record's first 16)
P_m30_N480_16slots steps 1382400 dt 0.0006944444444444445 125s x86_64
P_m30_N720_16slots steps 2073600 dt 0.000462962962962963 184s x86_64
$ python3 p1c_latJ.py 720 -6 ; 480 -6 ; 240 0 -6
PJ_m30_N240_0_-6 steps 691200 69s x86_64
PJ_m30_N480_-6 steps 1382400 99s x86_64
PJ_m30_N720_-6 steps 2073600 153s x86_64
$ python3 p4_lat.py
P_m30_N240 (slots 4..39): passive peak-to-peak stage lag median 0.5243 rt [min 0.5243, max 0.5243, n 19]; excess over L/s = 0.5 rt: 0.0243 rt = 35.0 steps (dt 6.94e-04 rt); passive transfer 15.83 dB
P_m30_N480_16slots (slots 4..15): passive peak-to-peak stage lag median 0.5222 rt [min 0.5219, max 0.5222, n 5]; excess over L/s = 0.5 rt: 0.0222 rt = 64.0 steps (dt 3.47e-04 rt); passive transfer 16.23 dB
P_m30_N720_16slots (slots 4..15): passive peak-to-peak stage lag median 0.5218 rt [min 0.5215, max 0.5218, n 5]; excess over L/s = 0.5 rt: 0.0218 rt = 94.0 steps (dt 2.31e-04 rt); passive transfer 16.37 dB
$ python3 p6_latJ.py
N=240 J= -1 dB: passive stage-1->2 peak-to-peak lag 0.5243 rt (excess over 0.5 rt: 0.0243)
N=240 J=  0 dB: passive stage-1->2 peak-to-peak lag 0.5250 rt (excess over 0.5 rt: 0.0250)
N=240 J= -6 dB: passive stage-1->2 peak-to-peak lag 0.5229 rt (excess over 0.5 rt: 0.0229)
N=480 J= -1 dB: passive stage-1->2 peak-to-peak lag 0.5222 rt (excess over 0.5 rt: 0.0222)
N=480 J= -6 dB: passive stage-1->2 peak-to-peak lag 0.5194 rt (excess over 0.5 rt: 0.0194)
N=720 J= -1 dB: passive stage-1->2 peak-to-peak lag 0.5218 rt (excess over 0.5 rt: 0.0218)
N=720 J= -6 dB: passive stage-1->2 peak-to-peak lag 0.5181 rt (excess over 0.5 rt: 0.0181)
[I read the session's stored runs/N720_m30_s7.json only to locate which family the printed 0.518 comes from: cfg {'primary_J': -6, 'Js': [-6, -3]}, chains J-6/J-3 only. I accept no stored number.]

$ python3 tdiff.py   (row-by-row diff of round-4 text + appendix against 11-reply.md)
Table 1: rows identical True; heading identical True (caption paragraph relabelled)
Table 2a: rows identical True; heading identical True
Table 2b: rows identical True; heading identical False (convention spelled out)
Table 3: rows identical True; heading identical True
Table 3b: rows identical True; heading identical True
Table 4: rows identical True; heading identical True
Table 5: rows identical True (43 incl. header); heading identical False (scope restored/extended)
Residue: rows identical True; heading identical False (denominator (a) re-described)
Table 6: first 12 rows identical True (the r1 parse ran on into the §4 grading table)
round-4-only tables: ['Table 3c', 'Table 3d', 'Table 8', 'Table 9']

$ (arithmetic on the appendix Table 5 rows, as printed)
42 rows; peak degradation 6.16 .. 8.11 ; slot-mode 8.63 .. 10.41
J >= -6 only: 34 rows; peak 6.16 .. 7.98 ; slot-mode 8.63 .. 10.28

$ grep counts in round-4-reply.md: released coupling 0; released cascade 0; released model's own 0; 7–9 0; 9–10 0; could build 0; +0.04 to +2.6 0; 3.2–4.4 0; 0.523–0.525 0; 1.43 0; 44 dB 2, LF half-step 1, every placement 1, byte-identical 1, no measured number changed 2, promoted floor key's own 1 (all inside disclosure sentences); 'round-3 text' 2 (line 15 self-label, required edit 4; line 268 disclosure); '< +0.3' 2 (line 26 '< +0.30 dB' regen, correct; line 29 active wave, required edit 3); 'Table 7' 5, all 'Part I Table 7'.
$ grep 0.9972 notes/2026-08-13-walk-excess-clamp-placement.md → line 33: 'Operator check: α(M = 0) = 0.9972 / 0.9976 / 0.9992 at cfl = 0.2/0.4/0.8 (N = 240)' (citation correct)
$ comment sizes (python len): A 42,921 / B 23,604 / C 21,844 (total 88,407); appendix 4,923; 12-listings.md 55,553; build_r4.py 75,665 bytes
$ git status --short | wc -l → 0
```

</details>
