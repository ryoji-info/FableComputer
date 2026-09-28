### 🧵 Fabric — **REJECT** (required edits) — round 4, 2026-09-28

VOTE: reject

REASONS: REJECT at the hard cap. The vote is on the round-4 text as written; the measured core is not in question. My own instrument (written from the reply's §1–§2 coupling definition and the promoted 07-31 launch) reproduces every decisive number: the gate (8.287855791924049 / −11.828336851446547 / −11.775002445228234 dB, ≤ 1.3×10⁻¹³ relative, not bit-equal; M_th_num(240) at 3.3×10⁻¹⁶); the J = −1 chains (13.103 dB, G4_A 1.5810 at m = 30; 1.5885 at m = 28); Table 3d's m = 28 / lo 0.80 row (matched 1.6955 against mixed 1.7308); Table 9 rows (iii) and (iv); and the loop model's −1.00 to +2.58 dB range with its §9.4 upper bounds. A full-slot placement scan also confirms that the rescoped universal is true: no placement at J = −1 gives both a round-spec floor and G4 ≥ 1.7. All 19 round-3 required edits landed as worded, the round-1 table rows are byte-identical, and every withdrawn phrase appears only inside disclosure sentences. Six mechanical defects remain, and each makes a printed number or statement false:
(1) The m = 30 round-spec placement set is a scan-boundary artifact. Table 3d's scan starts at lo 0.74, but the set runs lo 0.70–0.79, and the text's own Table 3c row at lo 0.70 reads −10.08 dB at G4_A 1.582. As a result, item 1(c), the §4 G4 row and Table 3d's note print matched G4 of 1.61–1.62 where the measured range is 1.573–1.624, and 1.695 is printed as '1.70' beside 'below the bar'.
(2) The latency 'grid ladder' 0.525 → 0.523 → 0.518 rt mixes junction classes. The N = 720 row is the J = −6 family; at J = −1, N = 720 reads 0.522 rt.
(3) Item 5's '< +0.3 dB' upper bound is actually +0.34 dB.
(4) §5 states that the prior seats reproduced 'every row to ≤ 1.3×10⁻¹³ relative'; they reproduced the gate rows at that precision and other rows only to printed digits.
(5) The listings package ships the round-1 render_tables.py, which still prints the withdrawn 'promoted floor key's own denominator' caption.
(6) The header still calls a paragraph of the round-4 text 'the round-3 text'.
None of these moves a verdict, and each is a one-line fix. Substance (1), labels (2) and durability (5) hold; numbers (3) and honesty (4) do not hold as written. The vote is therefore reject, with the required edits listed exactly.

FIXES VERIFIED (round-1 required edits):
- 🧵 RE1 (Table 9 row iii; the split of the mechanism) — LANDED. Row (iii) is labelled 'as (i), plus a hard cut of the '1' slots at 0.8·repT' and prints −13.09 / −12.64 / −16.82, eye +12.80. Re-executed with that construction (raised-cosine '0' cut + hard '1' cut): −13.086 / −12.638 / −16.820, chain 13.131, eye +12.802. Row (iv), 'every '0' slot zeroed hard … plus the hard cut', prints −13.81 / −13.36 / −17.53; re-executed −13.807 / −13.363 / −17.528, eye +13.523. The note under Table 9 credits the round-2 seats' −13.09. Item 4 now gives the '1'-tail share as 3.2–3.7 dB and the '0' residue as ≈ 4.7 dB under gate (i), a lower bound. The ≈ 83 % pass-through at 0.009 slot checks (0.5·(1+cos(π·0.27)) = 0.830), and the +0.72 dB is −13.81 − (−13.09). Gates (i) and (ii) themselves (−9.38 / −12.54) were not re-run by this seat; the shares are arithmetic on them.
- 🧵 RE2 (the J1 key's lever clause) — LANDED. It now reads 'exits the band above at cfl = 0.2 while 1.485 at cfl = 0.8 stays inside; placement … exiting above only'. A grep finds 'exits the band on both sides' only inside the header's quoted disclosure. The residue key's correct 'outside the band on both sides' stays. On my fine lattice the placement lever's mixed ratio falls to 1.418 at the lowest, still inside [1.40, 1.65], so 'exiting above only' holds.
- 🧵 RE3 (bound direction and endpoints of the loaded-drain model) — LANDED in item 2, item 3, §2 bullet 2, §4 row 1, the §5 passive-transfer key and limitation 1. The text now says the lossless junction is 'the least loading: the upper bound on the loaded loop, on cell 1's residual regeneration and on the delivered drive'. The range is −1.0 to +2.6 dB at J = −1 in the open-end phase, and the §9.4 figures are labelled upper bounds. Re-executed with the released regen: loop 0.4286, delivered +2.582 / +3.861 dB, regen +1.279; §9.4 bound 0.1426 / +0.036 / +0.300; |r| → 0 gives −1.000 dB; monotone in |r|; other phase −3.529 / −1.925. A new wrong bound was introduced in item 5 (required edit 3).
- 🧵 RE4 (name the DS drain factor) — LANDED. Item 2 says the loaded loop is regen.loop_gain(M) × |r|, 'which keeps the released DS drain factor (1 + M)/(1 − M) at a drain that a transmitting junction no longer current-clamps'. §2 bullet 2 and limitation 1 name it, labelled in-model / open.
- 🧵 RE5 (the title's slot-mode range; the sign-off's denomination) — LANDED. The title reads '6.2–8.1 dB (peak) / 8.6–10.4 dB (slot-mode)'. The sign-off reads '6.2–8.1 dB shallower … in peak `cav` under the promoted rule (9.1–9.3 dB at the lattice-optimal placements)'. Arithmetic on appendix Table 5: 6.16–8.11 / 8.63–10.41 over all 42 rows, and 6.16–7.98 / 8.63–10.28 at J ≥ −6.
- 🧵 RE6 (latency range 0.518–0.525 rt; excess given across the grid ladder) — LANDED AS WORDED. But the edit itself rested on an unverified premise. Table 6's N = 720 row is the J = −6 family (families2.json primary_J −6), whereas the N = 240 / 480 rows are J = −1. Re-executed: the J = −1 value at N = 720 is 0.5218 rt (0.5220 under the session's previous-state coupling), and J = −6 reads 0.5181 (0.5183, Table 6's 0.518). The ladder as printed therefore mislabels junction class as grid (new required edit 2).
- 🌊 RE1 (Table 9 row iii; item 4's shares; correct the round-3 record) — LANDED, as 🧵 RE1. The round-4 record's 'Corrections to the round-3 record' states that the −13.09 figure is reproduced by the labelled construction.
- 🌊 RE2 (residue caption) — LANDED IN THE REPLY. The caption now defines (a) as 'the mean-'1' drain-density peak … — the denominator of 08-02 §3.2's `drn_h` floor column (not of the promoted `max0_below_mean1_dB`, which is a source-plane `cav` ratio)'. Re-executed the table: −11.775 / −11.151 dB in the window; −5.698 / −5.308 over (a); −1.573 / −0.982 over (b). NOT carried into the shipped listing: 12-listings.md's render_tables.py still prints the withdrawn phrase (required edit 5).
- 🌊 RE3 (headline precision) — LANDED. The title has 8.6–10.4 dB and '… or, in slot-mode, at cfl = 0.2'. Item 4 reads '5.5 dB at cfl = 0.8' with no stray sign. The lead of item 4 matches the title.
- 🌊 RE4 (scope every copy of the loaded-drain range) — LANDED. Item 3, §4 row 1 and the §5 key now carry 'at J = −1 … open-end phase (−3.5 dB in the other; < +0.04 dB under §9.4's bound)'. 'Between the two' is replaced by 'near the booked link, far from the ideal buffer', which holds in both phases at J = −1: re-executed −3.53 … +2.58 dB against the booked −2.555 and the buffer's +15.8.
- 🌊 RE5 (complete ⚛️ RE10: the DS factor at item 2) — LANDED, as 🧵 RE4.
- 🌊 RE6 (limitation 9: the flush question) — LANDED. It is rewritten as 'resolved in the record at the 4-ps slot (its post-promotion annotation; 07-22-flush-noise-figure-negative; 07-23-reset-switch-adjudication, per INDEX) and is not re-examined here'. This matches INDEX row 07-22: '✅ §7.3's sufficiency question resolved'.
- 🌊 RE7 (appendix Table 5 caption) — LANDED. The caption reads '(window rule shift = passive-chain latency, rounded to the ⅛-rt grid; the ideal-buffer density coupling of §2; released cfl = 0.4; the cell-1 columns at the promoted window)'. The 42 rows are byte-identical to round 1 (programmatic diff). build_r4.py renders the appendix fresh through render_tables.py, with an assertion on the caption.
- 🌊 RE8 (correct the round-3 record) — LANDED in the round-4 record's 'Corrections to the round-3 record'. Its row 5 now says the DS factor was not named; its row 12 now says the −13.09 figure is reproducible; the 'What was not changed' paragraph now covers the Table 4/6 numbering claim, Table 5's lost caption and the stale split-file source; and 'all 29 … applied' is marked overstated.
- ⚛️ RE1 (Table 9 row iii) — LANDED, as 🧵 RE1. The Table 9 note and the round-3 record's line are corrected.
- ⚛️ RE2 (late-window G4: mixed vs matched denominator; rescope) — LANDED as requested, with a new defect in its supporting ranges. The mixed ratio is named in the Table 3c caption, item 1(c), item 6, the §4 G4 row, limitation 6 and the discriminant. The matched values are printed in the new Table 3d. The claim is rescoped to 'No placement at J = −1 gives both a round-spec floor and G4 ≥ 1.7'. My full-slot scan (lo 0–0.99, 0.0025 lattice, both rungs) confirms that universal: no lattice point has floor ≤ −10 dB and matched ≥ 1.7. The Table 3d rows reproduce (m = 30 lo 0.7400 1.616 / 1.606 / −10.38; lo 0.8075 1.763 / 1.711 / 8.541; m = 28 lo 0.80 1.731 / 1.695 / 8.301 / −10.08; lo 0.83 1.741 / 1.705 / −8.36). But the m = 30 round-spec range the text prints was inherited from a scan that starts at lo 0.74; see required edit 1.
- ⚛️ RE3 (bound direction inverted) — LANDED, as 🧵 RE3.
- ⚛️ RE4 (DS drain factor; correct the round-3 record's 'all 29 applied') — LANDED. The factor is named in item 2, §2 and limitation 1, and the round-4 record carries the correction.
- ⚛️ RE5 (appendix captions carry their own scope) — LANDED. Table 5 is as in 🌊 RE7. Table 2b now reads 'the single released cell driven at its source clamp by the duty-0.8 gated launch at amplitude A, over its identical passive twin, promoted window, ratio bias, cfl = 0.4, seed 7'.
- Table and comment audit (routine duty i) — the programmatic diff of 11-reply.md against round-4-reply.md plus the appendix: the rows of Tables 1 (20 lines), 2a (30), 2b (12), 3 (12), 3b (10), 4 (18), 5 (44), residue (4) and 6 (13) are byte-identical. The captions of Tables 1, 2b, 5 and the residue table changed exactly as the record states; Tables 3c, 3d, 8 and 9 are new. The comment parts are 42,921 / 23,604 / 21,844 characters (each < 60,000). The listings comment plus the appendix is 60,476 characters (< 65,536). Every withdrawn phrase ('every placement', 'LF half-step', '44 dB', 'own operating point', 'no measured number changed', 'byte-identical', 'exits the band on both sides', 'floor key's own') occurs only inside a disclosure sentence. 'released coupling', '7–9 dB', '9–10 dB', '0.523–0.525', '3.2–4.4', '0.55–0.89' and 'upper bound on the loading' return 0 hits.

REQUIRED EDITS:
- 1. The m = 30 round-spec placement set and the G4 values quoted at it (item 1(c) twice, Table 3d's summary line, §4 G4 row grade and reason, limitation 6).
- The error. Table 3d's matched scan starts at lo 0.74, and 0.74 is a scan boundary, not an edge of the set. The text's own Table 3c row at lo 0.70 reads −10.08 dB with G4_A 1.582. Re-executed (own instrument; J = −1, N = 240, seed 7, cfl 0.4; windows [lo, lo+0.47]·repT on a 0.0025-slot lattice over lo 0–0.99; matched = chain over the single cell at lo − 0.0856 / 0.0913 slot): at m = 30 the stage-2 peak-cav floor is ≤ −10 dB at every point of lo 0.7000–0.7900 (37 contiguous points). Over that set mixed G4_A = 1.582–1.633 and matched G4 = 1.573–1.624; at lo 0.70–0.7375 the chain is 13.110, mixed 1.5819, matched 1.5726. At m = 28 the set is lo 0.7925–0.8175, with matched 1.634–1.695 and mixed 1.664–1.731 (reproduced).
- Corrections:
  - '1.62–1.63 (m = 30, lo 0.74–0.79)' → '1.58–1.63 (lo 0.70–0.79)'.
  - 'matched … 1.61–1.62 (m = 30)' → '1.57–1.62'.
  - Table 3d's note 'lo 0.74–0.79 at m = 30 (matched G4 1.606–1.624)' → 'lo 0.70–0.79 (1.573–1.624)'. Add a lo 0.70 row or state the lattice.
  - §4 G4 row: '1.61–1.70' → '1.57–1.695'; 'matched 1.61–1.62 / 1.63–1.70' → '1.57–1.62 / 1.634–1.695'.
  - Limitation 6's '(matched: 1.62 / 1.70)' → '1.62 / 1.695'.
  - Never print 1.695 as '1.70' in a sentence that says 'below the bar'.
- Lattice scope. Scope two lattice statements the same way:
  - '1.54–1.62 … for any stage-2 window with lo ≤ 0.75' is Table 3c's lattice. On the fine lattice the ratio is 1.53–1.62 over lo 0.25–0.75, and 1.42 at lo 0.13.
  - 'matched G4 ≥ 1.7 only at lo ≥ 0.8075 (m = 30 …) and lo = 0.83 (m = 28 …)' holds only on the 0.74–0.83 scan. Over the whole slot, matched G4 also exceeds 1.7 at lo ≤ 0.065 / 0.11 and lo ≥ 0.8775, with floors from +0.8 to −6.2 dB.
- What stays. The universal 'No placement at J = −1 gives both a round-spec floor and G4 ≥ 1.7' is true over the whole slot and stays.
- 2. The latency ladder (item 7; the §5 `cascade_stage_latency_rt` key; the sentence under Table 9).
- The error. '0.525 at N = 240, 0.523 at N = 480, 0.518 at N = 720' and the excess '0.024 → 0.022 → 0.018 rt at N = 240 / 480 / 720' are presented as grid dependence. But the N = 720 row is the J = −6 family (families2.json primary_J −6), while the N = 240 / 480 rows are J = −1. The peak-time lag moves with junction class.
- Re-executed (own instrument; passive twin chain; per-'1'-slot argmax of |h − 1| over the whole slot; median; +1 dt converts to the session's previous-state coupling):
  - J = −1: 0.5243 / 0.5222 / 0.5218 rt → 0.5250 / 0.5226 / 0.5220 at N = 240 / 480 / 720.
  - J = −6: 0.5229 → 0.5236 (N = 240); 0.5181 → 0.5183 (N = 720, Table 6's 0.518).
  - J = −15: 0.5236 → 0.5243 (the junction-sweep rows' 0.524).
- Fix:
  - State the grid ladder at one junction class: J = −1, 0.525 → 0.523 → 0.522 rt; excess 0.025 → 0.023 → 0.022.
  - Say the peak-time lag also moves with junction class: 0.0014 rt at N = 240 and 0.0037 rt at N = 720 between J = −1 and −6.
  - Label Table 6's N = 720 row J = −6 and the junction-sweep rows J = −15 in a caption note; the rows are unchanged.
- What stays. The family range 0.518–0.525 rt, and 'the excess moves with the grid', both stay true.
- 3. Item 5: 'the active delivered wave is … < +0.3 dB under §9.4's bound' is a wrong upper bound. Re-executed with the released regen.loop_gain at J = −1, |r| = 0.1509, r = +|r|: the active delivered wave is +0.336 dB at the ratio bias (+0.292 at the analytic bias). Write '< +0.34 dB', or '≤ +0.3 dB at the analytic bias, < +0.34 at the ratio bias'.
- 4. The §5 key-scope line: 'the round-1 and round-2 seats' reruns reproduced every row to ≤ 1.3×10⁻¹³ relative' is false, and it overstates the verification record. The seats reproduced the gate rows at that precision. The other rows they re-executed agreed only to the printed digits (±0.001 from the one-step coupling label; round-1 🧵 log). By their own logs, several rows were never re-executed: N = 720, seed 11, m = 28 at N = 480, Table 2b, and others. Write, e.g., '… reproduced the gate rows to ≤ 1.3×10⁻¹³ relative and every row they re-executed to its printed digits'.
- 5. The shipped listing. The listings comment that PASTE-ORDER posts (stage2-session/12-listings.md) carries the round-1 render_tables.py. The revised one (stage2-session/listings/render_tables.py) is in no paste file; the rework-listings comment carries only stage4-rework/listings/*.py.
- The shipped version prints the residue caption '(a) = the mean-'1' peak inside the promoted window [0.25, 0.72]·repT, the promoted floor key's own denominator'. That is the plane mislabel withdrawn by ⚛️ round-1 R4 and 🌊 round-3 RE2.
- It also prints Table 1's pre-round-3 seed-bracket caption and Table 2b's 'same convention', and it has no Table 5 section with the restored scope.
- §7's 'The exact sources follow in the listings comment (… render_tables.py)' is therefore false. Ship the revised render_tables.py in a posted listings comment.
- 6. Header: '**Rework history, disclosed (stage 4 of the routine; this is the round-3 text).**' is stale inside the round-4 text, and the next paragraph is headed 'Round 4 (the cap; this text)'. Change it to '(stage 4 of the routine; round 3)'.

TOP ISSUES:
- REQUIRED (edit 1), evidence. At m = 30 the round-spec set runs lo 0.7000–0.7900, 37 contiguous lattice points with floors −10.08 to −10.86 dB. Table 3d, the item 1(c) text and the §4 row start it at 0.74. At lo 0.70–0.7375 the chain is 13.110 dB, mixed 1.5819 and matched 1.5726, which lowers the printed matched floor-range from 1.606 to 1.573. The deepest stage-2 floor anywhere is −10.865 dB (m = 30, lo 0.7675) and −10.079 dB (m = 28, lo 0.7925). The conclusion is unaffected: no lattice point in lo 0–0.99 has both floor ≤ −10 dB and matched G4 ≥ 1.7 at either rung. This is the routine's 2026-08-05 checklist item ('a scan cannot find a feature narrower than its own step; quote a scan's extremum as a lattice result'), turned the other way: a scan boundary quoted as a feature edge.
- REQUIRED (edit 2), evidence. families2.json gives N720_m30_s7 primary_J −6 and N240_*_Jext primary_J −15, and analyze.py takes the latency from chains f'J{Jp}_h_00'. My passive-chain peak-time lags (session convention): J = −1 0.5250 / 0.5226 / 0.5220 rt at N = 240 / 480 / 720; J = −6 0.5236 (N = 240), 0.5183 (N = 720); J = −15 0.5243 (N = 240). The envelope lag is J-independent: 2.5681 / 2.6278 / 2.6380 rt, matching Table 6. The passive transfer reproduces: 15.830 / 16.233 / 16.371 dB.
- REQUIRED (edits 3–6), evidence. Active delivered +0.336 dB at the §9.4 bound (ratio bias). The seat logs' own 'Not re-executed' lists (round-1 🧵 line 134; round-2 🌊 and ⚛️) contradict 'reproduced every row'. The diff of 12-listings.md against listings/render_tables.py shows three changed captions and the missing Table 5 section. The stale phrase 'this is the round-3 text' sits in line 15 of round-4-reply.md.
- OPTIONAL — item 6 says Table 3c's mixed ratio crosses 'only where the stage-2 floor fails the round spec or at a plateau edge'. The §4 row calls the 1.73 'a plateau edge'. On the fine lattice the m = 28 mixed ratio is ≥ 1.70 over lo 0.7975–0.8175, which is 9 of the 11 round-spec points, all with floor −10.08 dB. The numbers 1.66–1.73 are printed, but 'plateau edge' understates the extent.
- OPTIONAL — item 6's 'and the matched ratio does not' reads as 'does not cross the bar'. Matched G4 does cross (1.711 at m = 30, lo 0.8075–0.83; 1.705 at m = 28, lo 0.83) where the floor fails. Write 'does not at any round-spec placement'.
- OPTIONAL — limitation 8's '08-06 limitation 1's monoculture describes the rest of the record' is inexact. At least ten July notes declare Windows/CPython (07-12 predictions-resolved, 07-17 drive sweep, 07-18 ×2, 07-20 ×2, 07-21, 07-22 ×3, 07-23, 07-25). No promoted note mentions Linux, so 'first Linux x86_64 execution' stands.
- OPTIONAL — limitation 9 cites 07-22-flush-noise-figure-negative and 07-23-reset-switch-adjudication by slug, but neither is in the 'Record cited, by filename' block, whose lead says every reference resolves there. Both files exist.
- OPTIONAL — the J6 key's 'window-rule step 0.033 (N = 240: 1.756 ↔ 1.789; N = 720: 1.687 ↔ 1.711)' has a step of 0.024 at N = 720.
- OPTIONAL — item 4's 'a fail of 5.2–6.8 dB (peak) … against the round spec' covers J = 0…−6 only. The same sentence's J = −25 floor (−2.98 dB) fails by 7.0 dB. Scope it to 'at J = 0…−6'.
- OPTIONAL — §1 says cell 2's clamp is read 'at the same step'. cascade_driver.py reads the state before step k, i.e. cell 1's previous output. My same-step (after-update) coupling differs by exactly one dt, which shows as −0.0007 rt in the peak-time lag at N = 240, eye +4.40 vs +4.39, and a Table 3d floor of −10.19 vs −10.20. Say which convention the rows use.
- OPTIONAL — item 2 contains 'A further caveat: and 08-12 §3 registered …' (stray 'and').
- OPTIONAL — the §4 G4 row carries no cfl lever. Table 8 has G4_A(J = −1) = 1.774 at cfl 0.2, so the bar is met there under the rule. The global 'Scope, first' paragraph and the J1 key cover it, but the grading table is what readers quote.
- OPTIONAL (record, not reply) — the round-4 record's outcome line 'all 19 required edits and every top issue reproduced; all applied; none declined' conflicts with its own row 15: 'carried to PASTE-ORDER.md and the promotion step, not into the reply text'. PASTE-ORDER.md carries the appendix / 60k-read and listings-location items, but not 'name the cfl lever in the §4 G4 row' or '§9.4's third sentence'.
- VERIFIED, not defects:
- Gate: M_th_num(240) = 0.16894319463373797, 3.286×10⁻¹⁶ relative to the shipped value. Cell 1: G 3.86×10⁻¹⁵, floor cav 5.68×10⁻¹⁴, floor drn_h 1.32×10⁻¹³ relative.
- J = −1 chains: m = 30 at 2.625 rt, chain 13.103 / 13.399, G4_A 1.5810 / 1.5932, floors −4.70 / −4.31 / −6.26; at 2.5 rt 13.000 / 1.5685. m = 28 at 2.5 rt, 12.917 / 1.5885, floors −4.02 / −4.32 / −5.24.
- Relaunch −24.600 / −24.336 dB. Residue key −5.698 / −5.308 dB. Drain slope −0.11797 / −0.11799 (residual 0.074).
- Cell-1 late-window floor −20.140 (m = 30, lo 0.58) / −19.139 (m = 28, lo 0.60).
- Every loop-model figure in item 2; A_fix and 08-02 §4's fitted orders.
- Repository tree clean (git status: 0 lines).

SEAT MODEL NOTE: This is the Fabric 🧵 re-assessor seat for round 4 (the hard cap). The maintainer requested it on claude-opus-5-5 for this run, as the 2026-08-13 policy's Opus re-assessor seat. It is not Fable 5 and makes no claim to be. The reply it assessed was executed by the maintainer-operated session on claude-fable-5-1. Every number in this record was executed on Linux x86_64 / Python 3.11.15 / numpy 2.4.6 against the released, unedited fable-model-chain/. Reproductions are stated as relative deviations or printed digits, never as bit-equal. This seat's instrument reads cell 1 one step later than the session's previous-state coupling; the one-dt offset is disclosed wherever it shows. The repository tree was left clean.

<details><summary>Re-execution log (verbatim)</summary>

```text
Seat directory: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/reassess4-fabric/
Files: r4f.py (my instrument), jobs.py, jobs2.py, score.py, loop.py, residue_chk.py, cell1_window.py, tabdiff.py; series/*.npy.
- r4f.py was written from the reply's §1–§2 definitions and the promoted 07-31 make_sig_duty / run_custom listings before cascade_driver.py was opened. Both cells use the released solver._setup / _step_LF in one loop.
- Cell 2's clamp is h_left = 1 + κ·(h1[−1] − 1), with κ = 10^(J/20), read after cell 1's step k. This is one dt earlier than cascade_driver.py, which reads the state before step k; the offset is disclosed wherever it shows.
- Scoring follows 07-31 metrics: worst/mean '1' gain against the identical-pattern passive chain, floor = max '0' over mean '1', 4 slots dropped, fully windowed slots only. Slot-mode = |2⟨x·e^{−i2πf0t}⟩| over the window.
- fable-model-chain/ was imported unedited with PYTHONDONTWRITEBYTECODE=1; run_all.py was never run (only measure_Mth_num was imported and called).

$ nproc; python3 -c "import sys,numpy,platform;print(sys.version.split()[0], numpy.__version__, platform.system(), platform.machine())"
4
3.11.15 2.4.6 Linux x86_64

$ python3 jobs.py   (Pool(4): passive chains P30/P28 (N240), P30_480, P30_720; after the scan: A30, A28, ABL3, ABL4; all m=30 unless named, J=-1, seed 7, drive 2e-3, duty 0.8, cfl 0.4)
Linux x86_64 3.11.15 2.4.6
M_th_num(240) = np.float64(0.16894319463373797)  shipped 0.16894319463373791  rel dev 3.286e-16  [48 s]
bias = np.float64(0.11826023624361658)
done ('P30_720', 567.8, 5184000, 0.000462962962962963)
done ('P30_480', 390.2, 3456000, 0.0006944444444444445)
done ('P30', 160.2, 1728000, 0.001388888888888889)
done ('P28', 144.1, 1612800, 0.001388888888888889)
done ('A30', 221.9, 1898294, np.float64(0.0012642926038760258))
done ('A28', 204.7, 1771741, np.float64(0.0012642926038760258))
done ('ABL3', 162.8, 1898294, np.float64(0.0012642926038760258))
done ('ABL4', 162.0, 1898294, np.float64(0.0012642926038760258))
ALL DONE
[ABL3 = gate (i) 1-rt raised-cosine '0'-slot cut + hard '1' cut at 0.8·repT (Table 9 row iii); ABL4 = every '0' slot zeroed hard + hard '1' cut (row iv); gate applied to cell 1's drain reading at label t_k]

$ python3 score.py gate chain
[gate m=30] cell 1 cav: Gw 8.287855791924049 Gm 8.4102 floor -11.828336851446547 eye 11.705 pp 0.306 (n 36); drn_h floor -11.775002445228234; slot-mode floor -15.665
   rel dev vs promoted: G 3.86e-15, floor cav 5.68e-14, floor drn_h 1.32e-13
   passive transfer (mean-'1' |h-1| peak, promoted window, over 2e-3): 15.830 dB; active mean-'1' |h-1| 0.03397 -> relaunch -24.600 dB
[gate m=28] cell 1 cav: Gw 8.131548730367582 Gm 8.2231 floor -10.731214907969104 eye 10.640 pp 0.230 (n 36); drn_h floor -11.150570102407642; slot-mode floor -14.610
   passive transfer (mean-'1' |h-1| peak, promoted window, over 2e-3): 15.812 dB; active mean-'1' |h-1| 0.03295 -> relaunch -24.336 dB
[chain m=30 J=-1] passive stage-1->2 envelope lag 5.1361 units = 2.5681 rt = 0.0856 slot; active 5.7045 rt
   shift 0.000 rt: chain worst 12.734 mean 13.139 | G4_A 1.5365 / 1.5622 | floor cav -3.56 drn_h -3.09 mode -4.10 | pp 0.997 eye +3.15 | n 36
   shift 2.500 rt: chain worst 13.000 mean 13.337 | G4_A 1.5685 / 1.5858 | floor cav -4.64 drn_h -4.31 mode -6.16 | pp 0.853 eye +4.29 | n 36
   shift 2.625 rt: chain worst 13.103 mean 13.399 | G4_A 1.5810 / 1.5932 | floor cav -4.70 drn_h -4.31 mode -6.26 | pp 0.750 eye +4.40 | n 36
   shift 2.568 rt: chain worst 13.000 mean 13.337 | G4_A 1.5685 / 1.5858 | floor cav -4.64 drn_h -4.31 mode -6.21 | pp 0.853 eye +4.29 | n 36
[chain m=28 J=-1] passive stage-1->2 envelope lag 5.1111 units = 2.5556 rt = 0.0913 slot; active 5.7298 rt
   shift 0.000 rt: chain worst 12.623 mean 13.039 | G4_A 1.5524 / 1.5856 | floor cav -2.92 drn_h -2.43 mode -3.20 | pp 1.041 eye +2.50 | n 36
   shift 2.500 rt: chain worst 12.917 mean 13.281 | G4_A 1.5885 / 1.6151 | floor cav -4.02 drn_h -4.32 mode -5.24 | pp 0.897 eye +3.65 | n 36
   shift 2.625 rt: chain worst 12.917 mean 13.281 | G4_A 1.5885 / 1.6151 | floor cav -4.02 drn_h -4.42 mode -5.46 | pp 0.897 eye +3.65 | n 36
   shift 2.556 rt: chain worst 12.917 mean 13.281 | G4_A 1.5885 / 1.6151 | floor cav -4.02 drn_h -4.42 mode -5.34 | pp 0.897 eye +3.65 | n 36
[vs reply: Table 1 13.103 / 1.581 / 1.593; Table 5 -4.70 / -4.31 / -6.26 / +4.39 (mine +4.40, one-step coupling label); m=28 12.917 / 1.589, -4.02 / -4.31 / -5.24 (mine drn_h -4.32)]

$ python3 score.py scan   (0.0025-slot lattice, lo 0.0..0.99; chain at [lo, lo+0.47]·repT; mixed = over single cell at promoted window; matched = over single cell at [lo-lag, lo-lag+0.47]; floor = stage-2 peak cav)
[scan m=30] lag (reply) 0.0856 slot, own 0.0856 slot; single at promoted window 8.2879
   round-spec (peak cav <= -10 dB) placements: 0.7000, 0.7025, 0.7050, 0.7075, 0.7100, 0.7125, 0.7150, 0.7175, 0.7200, 0.7225, 0.7250, 0.7275, 0.7300, 0.7325, 0.7350, 0.7375, 0.7400, 0.7425, 0.7450, 0.7475, 0.7500, 0.7525, 0.7550, 0.7575, 0.7600, 0.7625, 0.7650, 0.7675, 0.7700, 0.7725, 0.7750, 0.7775, 0.7800, 0.7825, 0.7850, 0.7875, 0.7900
   at those: mixed 1.5819..1.6334; matched(reply lag) 1.5726..1.6239; matched(own lag) 1.5726..1.6239
   placements with round-spec floor AND matched G4 >= 1.7: []
   placements with round-spec floor AND mixed G4 >= 1.7: []
   matched >= 1.7 anywhere: lo [0.0, 0.0025, 0.005, 0.0075, 0.01, 0.0125]...[0.985, 0.9875, 0.99] (87 pts); best floor among them -8.590333623208485
   lo 0.2500: chain 12.734 mixed 1.5365 matched 1.5942 (single@lo-lag 7.988) | floor cav -3.56 drn_h -3.09 mode -4.10 | n 36
   lo 0.3000: chain 13.000 mixed 1.5685 matched 1.5940 (single@lo-lag 8.155) | floor cav -4.59 drn_h -4.18 mode -5.38 | n 36
   lo 0.4000: chain 13.110 mixed 1.5819 matched 1.5726 (single@lo-lag 8.337) | floor cav -5.56 drn_h -5.19 mode -7.66 | n 36
   lo 0.5000: chain 13.110 mixed 1.5819 matched 1.5726 (single@lo-lag 8.337) | floor cav -7.22 drn_h -7.00 mode -9.59 | n 36
   lo 0.5800: chain 13.110 mixed 1.5819 matched 1.5726 (single@lo-lag 8.337) | floor cav -8.12 drn_h -7.99 mode -10.99 | n 35
   lo 0.6000: chain 13.110 mixed 1.5819 matched 1.5726 (single@lo-lag 8.337) | floor cav -8.35 drn_h -7.99 mode -11.09 | n 35
   lo 0.6500: chain 13.110 mixed 1.5819 matched 1.5726 (single@lo-lag 8.337) | floor cav -9.08 drn_h -9.01 mode -11.98 | n 35
   lo 0.6800: chain 13.110 mixed 1.5819 matched 1.5726 (single@lo-lag 8.337) | floor cav -9.35 drn_h -9.15 mode -12.24 | n 35
   lo 0.6900: chain 13.110 mixed 1.5819 matched 1.5726 (single@lo-lag 8.337) | floor cav -9.35 drn_h -9.85 mode -12.43 | n 35
   lo 0.7000: chain 13.110 mixed 1.5819 matched 1.5726 (single@lo-lag 8.337) | floor cav -10.08 drn_h -9.85 mode -12.35 | n 35
   lo 0.7100: chain 13.110 mixed 1.5819 matched 1.5726 (single@lo-lag 8.337) | floor cav -10.08 drn_h -9.85 mode -12.55 | n 35
   lo 0.7200: chain 13.110 mixed 1.5819 matched 1.5726 (single@lo-lag 8.337) | floor cav -10.08 drn_h -10.05 mode -12.83 | n 35
   lo 0.7300: chain 13.110 mixed 1.5819 matched 1.5726 (single@lo-lag 8.337) | floor cav -10.08 drn_h -10.05 mode -12.76 | n 35
   lo 0.7400: chain 13.390 mixed 1.6156 matched 1.6061 (single@lo-lag 8.337) | floor cav -10.38 drn_h -10.05 mode -12.76 | n 35
   lo 0.7500: chain 13.390 mixed 1.6156 matched 1.6061 (single@lo-lag 8.337) | floor cav -10.37 drn_h -10.76 mode -13.07 | n 35
   lo 0.7675: chain 13.390 mixed 1.6156 matched 1.6061 (single@lo-lag 8.337) | floor cav -10.86 drn_h -10.88 mode -13.08 | n 35
   lo 0.7700: chain 13.512 mixed 1.6303 matched 1.6208 (single@lo-lag 8.337) | floor cav -10.86 drn_h -10.88 mode -13.08 | n 35
   lo 0.7900: chain 13.537 mixed 1.6334 matched 1.6239 (single@lo-lag 8.337) | floor cav -10.19 drn_h -9.48 mode -13.57 | n 35
   lo 0.7925: chain 13.537 mixed 1.6334 matched 1.6239 (single@lo-lag 8.337) | floor cav -9.13 drn_h -9.48 mode -13.55 | n 35
   lo 0.7950: chain 13.537 mixed 1.6334 matched 1.6239 (single@lo-lag 8.337) | floor cav -8.65 drn_h -9.48 mode -13.52 | n 35
   lo 0.7975: chain 13.537 mixed 1.6334 matched 1.6239 (single@lo-lag 8.337) | floor cav -8.59 drn_h -9.45 mode -13.48 | n 35
   lo 0.8000: chain 13.539 mixed 1.6336 matched 1.6241 (single@lo-lag 8.337) | floor cav -8.59 drn_h -9.42 mode -13.43 | n 35
   lo 0.8075: chain 14.612 mixed 1.7631 matched 1.7108 (single@lo-lag 8.541) | floor cav -8.59 drn_h -9.41 mode -13.43 | n 35
   lo 0.8175: chain 14.486 mixed 1.7479 matched 1.7110 (single@lo-lag 8.467) | floor cav -8.41 drn_h -7.92 mode -13.75 | n 35
   lo 0.8200: chain 14.486 mixed 1.7479 matched 1.7110 (single@lo-lag 8.467) | floor cav -8.41 drn_h -7.92 mode -13.82 | n 35
   lo 0.8250: chain 14.486 mixed 1.7479 matched 1.7110 (single@lo-lag 8.467) | floor cav -8.41 drn_h -7.92 mode -13.87 | n 35
   lo 0.8300: chain 14.486 mixed 1.7479 matched 1.7110 (single@lo-lag 8.467) | floor cav -7.33 drn_h -7.92 mode -13.82 | n 35
   lo 0.8500: chain 15.433 mixed 1.8621 matched 1.6462 (single@lo-lag 9.375) | floor cav -7.01 drn_h -5.95 mode -14.08 | n 35
   lo 0.9000: chain 14.137 mixed 1.7057 matched 1.8137 (single@lo-lag 7.794) | floor cav -4.15 drn_h -4.82 mode -12.83 | n 35
   lo 0.9500: chain 13.115 mixed 1.5825 matched 2.0187 (single@lo-lag 6.497) | floor cav -2.07 drn_h -2.37 mode -9.28 | n 35
[scan m=28] lag (reply) 0.0913 slot, own 0.0913 slot; single at promoted window 8.1315
   round-spec (peak cav <= -10 dB) placements: 0.7925, 0.7950, 0.7975, 0.8000, 0.8025, 0.8050, 0.8075, 0.8100, 0.8125, 0.8150, 0.8175
   at those: mixed 1.6641..1.7308; matched(reply lag) 1.6336..1.6955; matched(own lag) 1.6336..1.6955
   placements with round-spec floor AND matched G4 >= 1.7: []
   placements with round-spec floor AND mixed G4 >= 1.7: [(0.7975, 1.7035, -10.08), (0.8, 1.7308, -10.08), (0.8025, 1.7308, -10.08), (0.805, 1.7308, -10.08), (0.8075, 1.7308, -10.08), (0.81, 1.7308, -10.08), (0.8125, 1.7308, -10.08), (0.815, 1.7308, -10.08), (0.8175, 1.7308, -10.08)]
   matched >= 1.7 anywhere: lo [0.0, 0.0025, 0.005, 0.0075, 0.01, 0.0125]...[0.985, 0.9875, 0.99] (93 pts); best floor among them -8.361322504400162
   lo 0.2500: chain 12.623 mixed 1.5524 matched 1.6082 (single@lo-lag 7.849) | floor cav -2.92 drn_h -2.43 mode -3.20 | n 36
   lo 0.7500: chain 13.010 mixed 1.5999 matched 1.5774 (single@lo-lag 8.248) | floor cav -9.39 drn_h -9.38 mode -11.90 | n 35
   lo 0.7900: chain 13.532 mixed 1.6641 matched 1.6336 (single@lo-lag 8.283) | floor cav -9.99 drn_h -10.22 mode -12.21 | n 35
   lo 0.7925: chain 13.532 mixed 1.6641 matched 1.6336 (single@lo-lag 8.283) | floor cav -10.08 drn_h -10.22 mode -12.17 | n 35
   lo 0.7950: chain 13.543 mixed 1.6655 matched 1.6347 (single@lo-lag 8.284) | floor cav -10.08 drn_h -10.22 mode -12.15 | n 35
   lo 0.7975: chain 13.852 mixed 1.7035 matched 1.6687 (single@lo-lag 8.301) | floor cav -10.08 drn_h -10.22 mode -12.16 | n 35
   lo 0.8000: chain 14.074 mixed 1.7308 matched 1.6955 (single@lo-lag 8.301) | floor cav -10.08 drn_h -10.08 mode -12.19 | n 35
   lo 0.8175: chain 14.074 mixed 1.7308 matched 1.6955 (single@lo-lag 8.301) | floor cav -10.08 drn_h -9.33 mode -12.64 | n 35
   lo 0.8200: chain 14.074 mixed 1.7308 matched 1.6955 (single@lo-lag 8.301) | floor cav -9.19 drn_h -9.33 mode -12.64 | n 35
   lo 0.8300: chain 14.156 mixed 1.7409 matched 1.7053 (single@lo-lag 8.301) | floor cav -8.36 drn_h -9.20 mode -12.46 | n 35
   lo 0.8500: chain 15.231 mixed 1.8731 matched 1.6939 (single@lo-lag 8.992) | floor cav -8.11 drn_h -7.04 mode -12.86 | n 35
   lo 0.9000: chain 14.577 mixed 1.7926 matched 1.7865 (single@lo-lag 8.159) | floor cav -5.17 drn_h -5.85 mode -13.15 | n 35
   lo 0.9500: chain 13.603 mixed 1.6729 matched 2.1032 (single@lo-lag 6.468) | floor cav -3.17 drn_h -3.35 mode -10.53 | n 35
(m=28 lines at lo 0.30–0.74 omitted here for length; all have floors shallower than -10 dB; full output in score_scan.log)

$ python3 (scan summary over scan_m30.json / scan_m28.json)
m=30: mixed over lo in [0, 0.75]: 1.4184..1.6156; over [0.25, 0.75]: 1.5307..1.6156
   matched >= 1.7 at lo 0.0000..0.0650: matched 1.719..1.827; floors cav 0.53..-0.17 dB
   matched >= 1.7 at lo 0.8050..0.8375: matched 1.700..1.717; floors cav -7.01..-8.59 dB
   matched >= 1.7 at lo 0.8775..0.9900: matched 1.756..2.095; floors cav -1.76..-5.20 dB
   round-spec lo 0.7000..0.7900 (37 pts, contiguous: True); floors -10.08..-10.86; mixed 1.5819..1.6334; matched 1.5726..1.6239
   of which lo < 0.74: 0.7000..0.7375, floors -10.08..-10.39, mixed 1.5819..1.6156, matched 1.5726..1.6061
   deepest stage-2 floor anywhere: -10.865 at lo 0.7675
m=28: mixed over lo in [0, 0.75]: 1.3563..1.5999; over [0.25, 0.75]: 1.5473..1.5999
   matched >= 1.7 at lo 0.0000..0.0750: matched 1.701..1.932; floors cav 0.81..-0.03 dB
   matched >= 1.7 at lo 0.0800..0.1100: matched 1.707..1.713; floors cav -0.21..-0.23 dB
   matched >= 1.7 at lo 0.8300..0.8325: matched 1.705..1.719; floors cav -8.36..-8.36 dB
   matched >= 1.7 at lo 0.8400..0.8400: matched 1.704..1.704; floors cav -8.23..-8.23 dB
   matched >= 1.7 at lo 0.8775..0.9900: matched 1.746..2.141; floors cav -2.12..-6.18 dB
   round-spec lo 0.7925..0.8175 (11 pts, contiguous: True); floors -10.08..-10.08; mixed 1.6641..1.7308; matched 1.6336..1.6955
   deepest stage-2 floor anywhere: -10.079 at lo 0.7925
30 min mixed in [0.25,0.75]: 0.265 1.5307 floor -3.56 | lo<0.25 min mixed [0.13] 1.4184
28 min mixed in [0.25,0.75]: 0.2875 1.5473 floor -3.72 | lo<0.25 min mixed [0.0] 1.3563

$ python3 score.py abl lat
[abl] (0) no gate: floor cav -4.696 drn_h -4.307 mode -6.257 | chain worst 13.103 eye +4.395 (n 36)
[abl] (iii) rc '0' cut + hard '1' cut: floor cav -13.086 drn_h -12.638 mode -16.820 | chain worst 13.131 eye +12.802 (n 36)
[abl] (iv) hard '0' zero + hard '1' cut: floor cav -13.807 drn_h -13.363 mode -17.528 | chain worst 13.131 eye +13.523 (n 36)
[lat N=240] passive peak-time lag median 0.5243 rt (min 0.5243, max 0.5243); excess over 0.5 rt 0.0243; envelope lag 2.5681 rt; passive transfer 15.830 dB; dt 1.3889e-03
[lat N=480] passive peak-time lag median 0.5222 rt (min 0.5219, max 0.5222); excess over 0.5 rt 0.0222; envelope lag 2.6278 rt; passive transfer 16.233 dB; dt 6.9444e-04
$ python3 score.py lat   (after P30_720 finished)
[lat N=720] passive peak-time lag median 0.5218 rt (min 0.5215, max 0.5218); excess over 0.5 rt 0.0218; envelope lag 2.6380 rt; passive transfer 16.371 dB; dt 4.6296e-04

$ cat stage2-session/listings/families2.json   (excerpt)
"tag": "N720_m30_s7", ... "primary_J": -6, "Js": [-6, -3]
"tag": "N240_m30_s7_Jext", ... "primary_J": -15, "Js": [-10, -15, -20, -25]
[analyze.py: L_pk_pas = peaktime_lag(bits, c10["tpeak_drn_h"], p00["tpeak_drn_h"]) with p00 = chains[f"J{Jp}_h_00"], Jp = primary_J]
[cascade_driver.upstream_clamp: x_state = concatenate(([0.0], x[:-1])) -> previous-state coupling; mine reads x[k]]

$ python3 jobs2.py   (passive twin chains, m = 30, seed 7: N720 J=-6, N240 J=-6, N240 J=-15)
done ('P30_J15', 114.0)
done ('P30_J6', 114.0)
done ('P30_720_J6', 349.2)
ALL DONE

$ python3 cell1_window.py
m=30 cell 1 at lo 0.25: floor cav -11.828 drn_h -11.775 mode -15.66 Gw 8.288 (n 36)
m=30 cell 1 at lo 0.58: floor cav -20.140 drn_h -19.734 mode -22.78 Gw 8.337 (n 35)
m=30 cell 1 at lo 0.6: floor cav -20.140 drn_h -18.395 mode -23.40 Gw 8.337 (n 35)
m=28 cell 1 at lo 0.25: floor cav -10.731 drn_h -11.151 mode -14.61 Gw 8.132 (n 36)
m=28 cell 1 at lo 0.58: floor cav -18.319 drn_h -18.775 mode -21.60 Gw 8.248 (n 35)
m=28 cell 1 at lo 0.6: floor cav -19.139 drn_h -18.775 mode -21.57 Gw 8.248 (n 35)
[lat P30 N=240 J=-1] passive peak-time lag median 0.5243 rt (min 0.5243 max 0.5243); +1 dt (the session's previous-state coupling) -> 0.5250 rt; excess 0.0243
[lat P30_J6 N=240 J=-6] passive peak-time lag median 0.5229 rt (min 0.5229 max 0.5229); +1 dt (the session's previous-state coupling) -> 0.5236 rt; excess 0.0229
[lat P30_J15 N=240 J=-15] passive peak-time lag median 0.5236 rt (min 0.5236 max 0.5236); +1 dt (the session's previous-state coupling) -> 0.5243 rt; excess 0.0236
[lat P30_480 N=480 J=-1] passive peak-time lag median 0.5222 rt (min 0.5219 max 0.5222); +1 dt (the session's previous-state coupling) -> 0.5226 rt; excess 0.0222
[lat P30_720 N=720 J=-1] passive peak-time lag median 0.5218 rt (min 0.5215 max 0.5218); +1 dt (the session's previous-state coupling) -> 0.5220 rt; excess 0.0218
[lat P30_720_J6 N=720 J=-6] passive peak-time lag median 0.5181 rt (min 0.5178 max 0.5181); +1 dt (the session's previous-state coupling) -> 0.5183 rt; excess 0.0181

$ python3 residue_chk.py
m=30: '0'-after-'1' slots 8; window/(a) -11.775; first quarter/(a) -5.698; /(b) -1.573; whole slot/(a) -5.698
m=28: '0'-after-'1' slots 8; window/(a) -11.151; first quarter/(a) -5.308; /(b) -0.982; whole slot/(a) -5.308

$ python3 -c (LS slope of drain velocity on drain density, A30/A28)
30 LS slope du/dh -0.11797 (-M = -0.11826) rel residual 0.0738
28 LS slope du/dh -0.11799 (-M = -0.11826) rel residual 0.0737

$ python3 loop.py   (released regen._cavity / regen.loop_gain; the reply's item-2 formulas)
a_loss 0.7451522890452021; loop(0) 0.745152; unloaded open-end 2/(1-a) = 7.8478 = +17.895 dB
[ratio] M = 0.118260: loop 0.9450; unloaded CW regen +13.32 dB; per-slot decay (m=30, 30 rt) -14.73 dB/slot
[analytic] M = 0.102958: loop 0.9162; unloaded CW regen +9.66 dB; per-slot decay (m=30, 30 rt) -22.81 dB/slot
|r| lossless J=-1 0.4535; |r| at 9.4's <0.1 dB reflective loss 0.1509; |r| at 11.6% 0.3406
[ratio] J=-1 lossless  r=+|r|: loaded loop +0.4286; delivered passive +2.582 dB, active +3.861 dB; loaded CW regen +1.279 dB
[ratio] J=-1 lossless  r=-|r|: loaded loop -0.4286; delivered passive -3.529 dB, active -4.098 dB; loaded CW regen -0.569 dB
[ratio] J=-1 9.4 bound r=+|r|: loaded loop +0.1426; delivered passive +0.036 dB, active +0.336 dB; loaded CW regen +0.300 dB
[ratio] J=-1 9.4 bound r=-|r|: loaded loop -0.1426; delivered passive -1.925 dB, active -2.158 dB; loaded CW regen -0.232 dB
[ratio] J=-1 11.6%     r=+|r|: loaded loop +0.3219; delivered passive +1.543 dB, active +2.374 dB; loaded CW regen +0.831 dB
[ratio] J=-1 11.6%     r=-|r|: loaded loop -0.3219; delivered passive -2.964 dB, active -3.424 dB; loaded CW regen -0.459 dB
[ratio] J=-1 |r|->0    r=+|r|: loaded loop +0.0000; delivered passive -1.000 dB, active -1.000 dB; loaded CW regen +0.000 dB
[ratio] J=-1 |r|->0    r=-|r|: loaded loop -0.0000; delivered passive -1.000 dB, active -1.000 dB; loaded CW regen -0.000 dB
[analytic] J=-1 lossless  r=+|r|: loaded loop +0.4155; delivered passive +2.582 dB, active +3.664 dB; loaded CW regen +1.082 dB
[analytic] J=-1 lossless  r=-|r|: loaded loop -0.4155; delivered passive -3.529 dB, active -4.018 dB; loaded CW regen -0.490 dB
[analytic] J=-1 9.4 bound r=+|r|: loaded loop +0.1382; delivered passive +0.036 dB, active +0.292 dB; loaded CW regen +0.256 dB
[analytic] J=-1 9.4 bound r=-|r|: loaded loop -0.1382; delivered passive -1.925 dB, active -2.125 dB; loaded CW regen -0.199 dB
[analytic] J=-1 11.6%     r=+|r|: loaded loop +0.3120; delivered passive +1.543 dB, active +2.249 dB; loaded CW regen +0.706 dB
[analytic] J=-1 11.6%     r=-|r|: loaded loop -0.3120; delivered passive -2.964 dB, active -3.359 dB; loaded CW regen -0.394 dB
[analytic] J=-1 |r|->0    r=+|r|: loaded loop +0.0000; delivered passive -1.000 dB, active -1.000 dB; loaded CW regen +0.000 dB
[analytic] J=-1 |r|->0    r=-|r|: loaded loop -0.0000; delivered passive -1.000 dB, active -1.000 dB; loaded CW regen -0.000 dB
open-end phase, ratio bias, |r| in [0, 0.4535]: delivered passive -1.000 .. +2.582 dB (monotone: True); active -1.000 .. +3.861
open-end phase, ratio bias, |r| in [0, 0.1509] (Part I 9.4): delivered passive <= +0.036 dB; active <= +0.336 dB

$ python3 tabdiff.py   (rows = lines starting '|', grouped by '### Table N' / Residue headings; round-4 = reply + appendix)
round-1 tables: {'Table 1': 20, 'Table 2a': 30, 'Table 2b': 12, 'Table 3': 12, 'Table 3b': 10, 'Table 4': 18, 'Table 5': 44, 'Residue': 4, 'Table 6': 13}
round-4 tables: {'Table 1': 20, 'Table 2a': 30, 'Table 3': 12, 'Table 3b': 10, 'Table 3c': 24, 'Table 3d': 16, 'Table 4': 18, 'Table 6': 13, 'Residue': 4, 'Table 8': 5, 'Table 9': 7, 'Table 2b': 12, 'Table 5': 44}
Table 1    rows identical: True  (20 vs 20)  caption identical: True
Table 2a   rows identical: True  (30 vs 30)  caption identical: True
Table 2b   rows identical: True  (12 vs 12)  caption identical: False
Table 3    rows identical: True  (12 vs 12)  caption identical: True
Table 3b   rows identical: True  (10 vs 10)  caption identical: True
Table 4    rows identical: True  (18 vs 18)  caption identical: True
Table 5    rows identical: True  (44 vs 44)  caption identical: False
Residue    rows identical: True  (4 vs 4)  caption identical: False
Table 6    rows identical: True  (13 vs 13)  caption identical: True
NEW in r4: Table 3c 24 rows
NEW in r4: Table 3d 16 rows
NEW in r4: Table 8 5 rows
NEW in r4: Table 9 7 rows
$ diff (Table 1 caption paragraph, 11-reply.md vs round-4-reply.md)
< ... Seed-7 value [min, max over seeds 7/11/13] at N = 240.
> ... Seed-7 value [min, max over seeds 7/11/13, each at its own rule placement — the ⅛-rt window-rule envelope, not pattern dependence: at a fixed placement the three seeds give identical worst-'1' chains to ≤ 0.001 dB (mean-'1' to ≤ 0.05 dB)] at N = 240.

$ python3 (appendix Table 5 arithmetic: stage-2 floor minus cell-1 floor)
42 rows; peak degradation all rows 6.16..8.11; slot-mode 8.63..10.41
34 rows J>=-6; peak 6.16..7.98; slot-mode 8.63..10.28

$ grep -c (round-4-reply.md) for withdrawn/stale phrases
[1] every placement  [1] LF half-step  [2] 44 dB  [1] own operating point  [0] released coupling  [0] released cascade  [0] released model's own  [1] No measured number changed  [1] no measured number changed  [1] byte-identical  [0] 7–9 dB  [1] crosses the bar  [3] both sides  [0] upper bound on the loading  [0] +0.04 to +2.6  [0] 9–10 dB  [0] 0.523–0.525  [1] floor key's own  [0] flush-sufficiency  [0] 3.2–4.4  [0] 0.55–0.89  [2] cfl law  [5] Table 7 (all 'Part I Table 7' or the header's disclosure)
(each non-zero hit inspected: inside a disclosure sentence, or correct usage; plus line 15: '**Rework history, disclosed (stage 4 of the routine; this is the round-3 text).**')
$ grep 'reproduced every row' round-{2,3,4}-reply.md
round-2-reply.md:289: ... the round-1 seats' reruns reproduced every row to ≤ 1.3×10⁻¹³ relative ...
round-3-reply.md:260: ... the round-1 and round-2 seats' reruns reproduced every row to ≤ 1.3×10⁻¹³ relative ...
round-4-reply.md:291: ... the round-1 and round-2 seats' reruns reproduced every row to ≤ 1.3×10⁻¹³ relative ...
$ grep 'active delivered wave' round-{3,4}-reply.md
round-3: '... +3.9 dB of the 24.6 for a lossless junction and +0.3 dB under §9.4's bound (item 2) ...'
round-4: '... +3.9 dB of the 24.6 for a lossless junction and < +0.3 dB under §9.4's bound, open-end phase (item 2) ...'

$ python3 (comment lengths)
total chars 88407 parts [42921, 23604, 21844]
listings chars 55553 appendix 4923 sum 60476

$ grep / diff: stage2-session/12-listings.md (the listings paste file, 07:18) vs stage2-session/listings/render_tables.py (10:27)
12-listings.md:815: Seed-7 value [min, max over seeds 7/11/13]
12-listings.md:897: promoted floor key's own denominator
diff: line 36 (Table 1 caption), line 60 (Table 2b '... same convention (seed 7)'), line 118 (residue caption '(a) = the mean-'1' peak inside the promoted window [0.25, 0.72]·repT, the promoted floor key's own denominator'), and lines 147–148 (Table 5 section) differ; count of 'each at its own rule placement': 12-listings.md 0, listings/render_tables.py 1.
PASTE-ORDER.md round 4: appendix into the listings comment; rework listings = stage4-rework/listings/*.py (rw_*, rw3_*, rw4_*, build_r*) — render_tables.py is in neither.

$ ls notes/<each 'Record cited' file and 07-22-flush-noise-figure-negative.md, 07-23-reset-switch-adjudication.md> -> ok (16/16)
$ grep 08-02 §4 fitted orders -> '**`gated_floor_convergence_order_p`** = **0.71 / 0.55 / 0.14 / 0.89** at m = 30 / 28 / 26 / 22'
$ grep 08-12 line 128-129 -> 'Under the early sub-window [0.25, 0.45]*repT the same slots read r -11.94..-11.68 dB'
$ grep notes for 'window placement|late window|sampling phase' -> no prior art on the late-window single-cell floor
$ grep notes 'Windows' -> 07-12, 07-17, 07-18 x2, 07-20 x2, 07-21, 07-22 x3, 07-23, 07-25 declare Windows/CPython; grep 'Linux|x86' -> no files

$ git -C /home/user/FableComputer status --short | wc -l
0

Not re-executed by this seat (no number accepted from these):
- Tables 2a and 2b, and the c2c columns (these need mixed active/passive runs);
- the N = 480 / 720 active chains; seeds 11 and 13; the J = 0 / −3 / −6 / −10 … −25 active chains;
- Table 3 stages 3–5; Table 8's cfl 0.2 / 0.8 rows;
- ablation gates (i) and (ii) themselves; the J = −25 placement rows; M_th_num(480 / 720).
```

</details>
