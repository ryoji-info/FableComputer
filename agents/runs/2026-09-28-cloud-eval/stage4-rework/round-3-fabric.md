### 🧵 Fabric — **STORE** (required edits) — round 3, 2026-09-28

VOTE: store

REASONS: STORE WITH REQUIRED EDITS. This is not a clean pass; it goes to round 4. The round-2 regression is repaired. A row-by-row diff shows every published round-1 post-check table is back byte-identical: Table 3 uncapped with its lag and slot-count columns, Table 3b present, Table 2a with 28 rows, Table 6 with eleven families, and the residue table with named denominators and the registered −5.70 / −5.31 in bold. No bare 'Table 7' survives, and no withdrawn statement appears outside a disclosure sentence. I re-executed the decisive numbers with my own instrument, and every one reproduces:
- the gate, to ≤ 1.3×10⁻¹³ relative, not bit-equal;
- the J = −1 chain (13.103 dB, G4_A 1.5810);
- Table 3c at m = 28 / lo 0.80 (1.7308, −10.079 dB);
- Table 8's cfl 0.2 row;
- the N = 480 rung and its continuum estimate of 1.4245;
- every row of the loaded-drain loop model;
- ablation gates (i) and (ii).
Of the 29 round-2 required edits, 25 landed and 4 landed partially. Six mechanical defects remain, and none moves a verdict:
- Table 9's row (iii) prints the numbers of a different construction than its label; the labelled construction reproduces the round-2 seats' −13.086.
- One registered key says the cfl lever 'exits the band on both sides', which is false.
- The loaded-drain range inverts the direction of its bound and prints two upper bounds as if they were a range.
- The drain-factor (DS-factor) assumption is still unnamed.
- The slot-mode headline range rounds its lower end up.
- The latency key's range leaves out its own N = 720 row.
Substance and durability (criteria 1 and 5) hold firmly. Labels, numbers and honesty (criteria 2–4) hold once these one-line edits land; deleting row (iii) of Table 9 is an acceptable scope reduction.

FIXES VERIFIED (round-1 required edits):
- 🧵 RE1 (table regression) — LANDED. I diffed every table row programmatically between 11-reply.md and round-3-reply.md plus the appendix. Byte-identical: Table 1 (18 rows), 2a (28), 2b (10, appendix), 3 (10; shifts 7.70 / 10.27 and 5.11 / 7.67 / 10.22 rt, lag and slots-scored columns present), 3b (8), 4 (16), 5 (42, appendix), residue (2) and 6 (11). The 'Table 4' and 'Table 6' headings are restored. Item 4's 4.8 → 4.6 dB and eye +1.0 → +1.6 now match Table 3. The header withdraws 'no measured number changed' and 'byte-identical', and the regression is disclosed in the header and in limitation 6. Re-executed Table 3's stage-2 row (m = 30, 2.568 rt): 13.000 / 13.337, c2c 4.704 / 4.968, floors −4.637 / −4.307 / −6.214, pp 0.853, eye +4.29. Residual, optional: build_r3.py still takes appendix Table 5 from tables_split.json (its rows are verified identical to the published ones), and the appendix drops Table 5's '(window rule shift = passive-chain latency)' caption.
- 🧵 RE2 ('Table 7' collision) — LANDED. The cfl scan is Table 8 and the ablation Table 9. A regex finds 5 'Part I Table 7' references and 0 bare 'Table 7'.
- 🧵 RE3 (window scope of the G4 verdicts) — LANDED. Item 1 now reads '…at every grid under the pre-registered window rule' and adds scope (c) with 1.630 / 1.731. The §4 G4 row, item 6 and the title carry the rule scope. Re-executed on Table 3c's placements: G4_A 1.6303 (m = 30, lo 0.77), 1.7308 (m = 28, lo 0.80), 1.8621 / 1.8731 (lo 0.85).
- 🧵 RE4 (headline and sign-off precision) — PARTIALLY LANDED.
- Landed: item 4's peak range 6.2–8.0 dB (6.2–8.1 over appendix Table 5) and slot-mode 8.6–10.4 dB. I re-executed 7.13 (m = 30), 6.71 (m = 28) and 6.76 (N = 480) dB peak, and 9.41 / 9.36 / 9.11 dB slot-mode. The cfl scope is in the headline. The sign-off's direction is fixed ('shallower') and 'could build' now reads 'ran'.
- Not landed: the title's '9–10 dB (slot-mode)' rounds the measured 8.63 lower end up, contradicting the text's own header and item 4 (8.6–10.4). The sign-off's '6–9 dB shallower' names no denomination or placement.
- 🧵 RE5 (loaded-drain junction and bias) — LANDED IN SUBSTANCE.
- Part I §9.4 is quoted in full; I verified the quote against the extracted Part I text.
- 'Lossless' is named wherever +2.6 dB or 0.429 is used as a point value (item 2, §2 bullet 2, limitation 1, item 5); the range form '+0.04 to +2.6 dB' appears in item 3, §4 row 1 and the §5 key.
- 08-12's regen.loop_gain disagreement is cited, and the analytic-bias column is printed.
- Re-executed with released regen: loop 0.9450 → 0.429 (ratio) / 0.9162 → 0.416 (analytic); delivered +2.58 dB passive / +3.86 dB active; standing wave +6.83 dB; regen +1.28 / +1.08 dB. At the §9.4 bound: 0.143 / +0.04 / +0.34 / +0.30. At 11.6 %: 0.322 / +1.54 / +2.37 / +0.83. At r = −|r|: −3.53 / −4.10 / −0.57. Loop 0.945 → −14.73 dB/slot; effective loop 0.9107.
- A new defect in how the range is stated is raised separately (required edit 3).
- 🧵 RE6 (bench discriminant) — LANDED. The loaded junction moves to the '< 1.40' reading. Re-executed CW-form G4 of the loaded chain: 1.10 lossless, 1.02 at §9.4's bound, 1.06 at 11.6 %. '> 1.7' is kept for a link that re-normalizes the swing without loading cell 1. The released-cfl-path caveat is stated.
- 🧵 RE7 (citations) — LANDED.
- (a) Limitation 4 no longer attributes the cfl movement to 08-13's law.
- (b) Table 8 credits 08-12, with the statistic difference stated.
- (c) All 14 notes/ filenames in the 'Record cited' block resolve with ls. 08-13 §2 does carry α(M = 0) = 0.9972 / 0.9976 / 0.9992.
- 🧵 RE8 (the f_max grade and the single-cell window finding) — LANDED in item 5 and §4 row 2, labelled in-model / open, with no key moved. Re-executed the cell-1 floor: −20.140 dB (m = 30, lo 0.58) and −19.139 dB (m = 28, lo 0.60). A grep of notes/ for window-placement or sampling-phase language found no prior art.
- 🧵 RE9 (Table 1 caption; §1 window bullet) — LANDED. The caption now calls the bracket the ⅛-rt window-rule envelope, not pattern dependence. §1 quotes 0.27 dB / 0.033 at J = −6.
- 🧵 RE10 (length) — LANDED. There is an explicit split. Comment A is 59,699 characters (60,944 bytes) and comment B 20,194. The round-1 listings comment (55,553) plus the appendix (4,525) is 60,078, under 65,536.
- 🌊 RE1 (a)–(f) (rebuild §3) — LANDED; see 🧵 RE1 and RE2. (b) The residue table's last column now uses one convention: Table 5's −4.31 / −4.70 and −4.31 / −4.02. (c) The text now says '28 matched rows'. (f) The disclosures are corrected.
- 🌊 RE2 (scope the G4-bar and '≈ 2×' statements to the rule and the released cfl) — LANDED: §0 'Scope, first', item 1(c), item 6, the §4 G4 row and the title.
- 🌊 RE3 (degradation range; 'do not round the lower end up') — PARTIALLY LANDED. The peak range 6.16 → '6' is correct. The title's slot-mode '9–10' rounds 8.63 up (same evidence as 🧵 RE4).
- 🌊 RE4 (scope the loaded-junction figures) — LANDED. Lossless is named, §9.4's |r| < 0.151 figures are given, item 5 uses the active delivered wave as its comparator ('+3.9 dB of the 24.6'; re-executed +3.86), and §9.4's second clause is quoted.
- 🌊 RE5 (08-13 mis-citation; credit 08-12) — LANDED. Limitation 4 is rewritten. Item 7 states 08-13's cfl-independent α(M = 0), which I verified in 08-13 §2. Table 8's cell-1 column credits 08-12's registered lever.
- 🌊 RE6 (filenames) — LANDED (see 🧵 RE7c).
- 🌊 RE7 (length / split) — LANDED (see 🧵 RE10).
- ⚛️ RE1 (restore Table 3) — LANDED; uncapped, byte-identical to round 1.
- ⚛️ RE2 (restore the residue table) — LANDED. Re-executed −5.698 / −5.308 dB over (a) and −1.573 / −0.982 dB over (b). The whole-slot residue peak sits at 0.0084–0.0167 of the slot.
- ⚛️ RE3 (restore the missing structure) — LANDED: Table 3b, the Table 4 / Table 6 headings and Table 6's eleven rows are back, and the 'no measured number changed' disclosure is corrected.
- ⚛️ RE4 (renumber the cfl table) — LANDED.
- ⚛️ RE5 (scope the G4 bar) — LANDED. Item 1(c) states the bar is crossed at lo 0.80 (m = 28) and lo 0.85; the Table 3c caption states that lo > 0.53 reaches into the following slot.
- ⚛️ RE6 (headline and sign-off range) — PARTIALLY LANDED (same evidence as 🧵 RE4).
- ⚛️ RE7 (Table 1 bracket; 'identical' restricted to worst-'1') — LANDED ('worst-'1' … ≤ 0.001 dB (mean-'1' to ≤ 0.05 dB)').
- ⚛️ RE8 (cite by filename) — LANDED.
- ⚛️ RE9 (credit 08-12 for the single-cell cfl lever) — LANDED in item 4(ii), limitation 4 and the Table 8 caption. Re-executed the cfl 0.2 cell-1 row: −16.694 / −17.028 / −22.415 dB.
- ⚛️ RE10 (name the loaded-drain model's assumptions) — PARTIALLY LANDED. The open-end phase is named, with the r = −|r| figures. The second assumption the edit named is absent: the DS drain factor (1 + M)/(1 − M) is kept at a partially transmitting drain (loaded loop = |r|·loop(M)). grep for 'DS factor' and '(1 + M)' returns 0 hits. The round-3 record's row 5 omits it while saying all edits were applied.
- ⚛️ RE11 (state the construction of ablation gate (ii)) — LANDED for gate (ii); re-executed −12.537 / −12.081 / −16.217. The new row (iii) that round 3 added is mislabelled; this is raised separately (required edit 1).
- ⚛️ RE12 (declare the comment split) — LANDED.

REQUIRED EDITS:
- 1. Table 9 row (iii) and item 4's split sentence (new; this completes ⚛️ RE11 / 🌊 T10). The row is labelled '(iii) as (i), plus a hard cut of the '1' slots at 0.8·repT'. I re-executed that construction: −13.086 / −12.638 / −16.820 dB, chain 13.131 dB, eye +12.80. This reproduces both round-2 seats (−13.086 / −13.088). The printed −13.81 / −13.36 / −17.53 (eye +13.52) belongs to the construction rw3_runs.py actually ran: every '0' slot hard-zeroed, with no raised-cosine, plus the hard cut. My run of that construction gives −13.807 / −13.363 / −17.528. Do three things:
- Relabel row (iii) as that construction, or print both rows.
- Credit the round-2 seats' −13.09 as reproduced for the labelled construction.
- Restate the split: with the '0'-slot gate held at (i), the '1'-slot tail is worth 3.16 dB (raised-cosine) to 3.71 dB (hard cut), not '3.2–4.4'. The remaining 0.72 dB comes from zeroing the '0' slot's first round trip, which gate (i) passes (≈ 83 % of amplitude, −1.6 dB, at the residue peak's 0.009-slot position). So gate (i) removes the '0'-slot ring-down after its first round trip, not the peak the registered key isolates.
- 2. The `cascade2_G4_worst1_ratio_J1` lever clause (new; present since round 2). Strike 'which exits the band on both sides'. By the reply's own Table 8, cfl 0.8 gives 1.485, which lies inside [1.40, 1.65]. Only cfl 0.2 exits, and only above (1.774; re-executed 1.7738). The placement lever also exits only above (Table 3c 1.537–1.862, re-executed). The residue key's 'outside the band on both sides' (−8.11 / −4.21 against [−7.0, −4.5]) is correct and stays.
- 3. Loaded-drain loop model: bound direction and endpoints (new). This applies to item 2, item 3, §2 bullet 2, §4 row 1, the §5 passive-transfer key and limitation 1.
- (a) 'the largest reflection a passive junction allows, hence the upper bound on the loading' is inverted. The largest |r| is the least loading. The lossless case bounds the loaded loop (≤ 0.429) and the delivered drive (≤ +2.6 / +3.9 dB) from above.
- (b) §9.4's |r| < 0.151 gives upper bounds: loop < 0.143, delivered < +0.04 dB, regen < +0.30 dB. '+0.04 to +2.6 dB delivered' therefore prints two upper bounds as if they were a range. In the same released loop model, |r| → 0 gives loop 0, delivered −1.00 dB and regen 0.00 dB; at the §9.4 bound in the other phase, delivered is −1.93 dB. State the range as −1.0 dB (|r| → 0; −1.9 in the other phase) to +2.6 dB (lossless), and ≤ +0.04 dB for any §9.4 junction.
- No conclusion moves: 'between the two' and the '< 1.40' discriminant arm both survive.
- 4. (Carried from ⚛️ RE10, verified only partially landed.) Name the second assumption behind every loaded-loop figure: loaded loop = |r|·loop(M) keeps the released DS drain factor (1 + M)/(1 − M). That factor was derived for the current-clamped (AC-open) drain that a transmitting junction removes. Label this in-model where the figures are defined (item 2) and in limitation 1.
- 5. (Carried from 🧵 RE4 / 🌊 RE3 / ⚛️ RE6, verified only partially landed.)
- The title's '9–10 dB (slot-mode)' contradicts the text's own header and item 4 (8.6–10.4). Print the measured 8.6–10.4 dB; do not round the lower end up.
- The sign-off's 'windowed floor sits 6–9 dB shallower' must name its denomination and placement: 6.2–8.1 dB peak `cav` under the rule, 9.1–9.3 dB at the lattice-optimal placements.
- 6. `cascade_stage_latency_rt` and item 7 (new; present since round 1). The passive peak-to-peak range '0.523–0.525 rt' (key: 'all eleven families') leaves out the reply's own Table 6 N = 720 row and the sentence under Table 6, both of which give 0.518 rt. Restate it as 0.518–0.525 rt. Restate the transit excess as 0.018–0.025 rt across the cfl-0.4 grid ladder: it moves with N as well as with cfl. My peak-time lags are 0.5243 rt (N = 240), 0.5222 rt (N = 480) and 0.5156 rt (cfl 0.2).

TOP ISSUES:
- Regression repaired (verified, not a defect). Every published round-1 post-check table row reappears byte-identical in the round-3 text plus appendix: 9 tables, 145 rows. The header's 'No measured number in the published round-1 tables changed between rounds 1 and 3' is true as measured. The withdrawn statements (round 1 'every placement', 'plus the LF half-step', '44 dB'; round 2 'no measured number changed', 'byte-identical'; the ledger's 'own operating point') survive only inside disclosure sentences. 'released coupling', '7–9' and 'could build' return 0 hits.
- Table 9 row (iii) is mislabelled. The label's construction ('(i) + hard cut of the '1' slots at 0.8·repT') measures −13.086 / −12.638 / −16.820 dB. The printed −13.81 / −13.36 / −17.53 is the executed construction (every '0' slot hard-zeroed plus the hard cut): −13.807 / −13.363 / −17.528. Item 4's '1'-tail share of '3.2–4.4 dB' is contaminated by the 0.72 dB that comes from zeroing the '0' slot's first round trip; the clean share is 3.16–3.71 dB. The round-3 record itself says the seats' −13.09 used the raised-cosine '0' cut, which is exactly the construction the reply's label describes.
- A registered key carries a false lever statement. The `cascade2_G4_worst1_ratio_J1` cfl lever '1.774 / 1.581 / 1.485 … exits the band on both sides' is wrong against band [1.40, 1.65]: 1.485 is inside. The error has been in the text since round 2 and no seat caught it.
- The loaded-drain range is not fairly stated.
- 'The largest reflection a passive junction allows, hence the upper bound on the loading' inverts the direction: largest |r| means the least loading, the maximum loaded loop 0.429 and the maximum delivered drive +2.58 dB.
- §9.4's figures are upper bounds (|r| < 0.151 → loop < 0.143, delivered < +0.04 dB), yet '+0.04 to +2.6 dB' is printed as a range three times.
- The same released loop model gives −1.00 dB delivered at |r| → 0 and −1.93 dB at the §9.4 bound in the other phase.
- Every printed loop-model figure itself reproduces: a_loss 0.7451522890452021; loops 0.9450 / 0.9162; J = −1, −3 and −6 rows across junction model, phase and bias.
- ⚛️ RE10 landed only half. The open-end phase is named; the retained DS drain factor (1 + M)/(1 − M) at a transmitting drain is not (0 grep hits). The round-3 record's 'all 29 required edits … all applied; none declined' is therefore inaccurate for this edit and for the row (iii) label.
- The headline ranges are imprecise. The title prints '6–8 dB (peak) / 9–10 dB (slot-mode)', while the header and item 4 print 8.6–10.4 dB slot-mode (re-executed 9.41 / 9.36 / 9.11 at m = 30 / m = 28 / N = 480, J = −1). The sign-off's '6–9 dB shallower' names no denomination.
- The latency key's range leaves out its own row. 'Passive stage 0.523–0.525 rt … all eleven families' contradicts Table 6's N = 720 row (0.518 rt). The 'open' transit excess moves with grid (≈ 0.024 → 0.022 → 0.018 rt over N = 240 / 480 / 720) as well as with cfl; my N = 480 value is 0.5222 rt.
- Optional (discriminant framing). Reassigning the loaded junction to the '< 1.40' reading is right (re-executed CW-form G4: 1.10 / 1.02 / 1.06). But 'The model then predicts G4 in [1.40, 1.65]' is the ideal-buffer construct's value. By item 2's own argument, no passive junction realizes that construct, so for Part I Table 7's passive-junction die the loop model expects the '< 1.40' arm. Say so, so that a bench reading inside the band is not read as the expected outcome.
- Optional.
- The title's 'reaching the round spec only … or at cfl = 0.2' holds only in slot-mode at cfl 0.2 (re-executed −11.646 dB); the peak reading there is −8.349.
- 'Only' ranges over the levers tested (placement, cfl), not bias or launch amplitude.
- Optional (appendix and builder).
- The two-comment split and the appendix placement of Tables 2b and 5 are acceptable for the Discussion record: comment A is 59,699 characters; listings plus appendix is about 60,078.
- A promoted note must carry the appendix, because item 4's 'every rung, grid and seed' and the 6.2–8.1 dB span rest on Table 5.
- The appendix Table 5 caption lost its window-rule scope.
- build_r3.py still sources Table 5 from the stale tables_split.json. Its rows are verified identical to the published round-1 Table 5, so nothing regressed, but the builder docstring's 'never from the stale tables_split.json' is inaccurate for Table 5.
- The rework listings (rw_*.py, about 26.8k characters) have no stated paste location.
- Optional (minor citations and wording).
- Limitation 4's '08-02 §4 … p = 0.55–0.89' omits m = 26's 0.14 (08-02 lists 0.71 / 0.55 / 0.14 / 0.89).
- Limitation 5's 'Table 2' should read 'Table 2a'.
- Item 4 writes '-5.5 dB at cfl = 0.8' in a list of positive degradations.
- 'Floor-optimal placement' should read 'lattice-optimal' for cell 1's lo 0.58 / 0.60, which were not fine-scanned.
- Standing rule 10, checked in both directions. Clean. Prior art is credited where used:
- 07-22 cavity-ringdown (the ring-down mechanism)
- 08-12 (the −24.4 dB/slot decay, the regen.loop_gain disagreement, the single-cell cfl lever)
- 08-13 (α at M = 0)
- 08-02 §3.1 and its vote record (the plane fork)
- 08-01 gated §4 / §5 (A_fix 0.00763–0.01403; knee 0.01203)
The single-cell window-scoping of the promoted floor keys (−11.83 → −20.14 dB) has no prior art in notes/ (grep). Nothing contradicts a promoted note.
- Reproduced and accepted:
- M_th_num(240) = 0.16894319463373797 (3.3×10⁻¹⁶ relative); M_th_num(480) = 0.1587475408418196.
- Gate: 8.287855791924049 / −11.828336851446547 / −11.775002445228234 (3.86×10⁻¹⁵ / 5.68×10⁻¹⁴ / 1.32×10⁻¹³; exact equality False); slot-mode −15.665.
- m = 28: 8.1315 / −10.7312 / −11.1506 / −14.610.
- Passive transfer 15.8296 / 15.8117 dB (m = 30 / 28), 16.23 dB (N = 480), 15.01 dB (cfl 0.2). Relaunch −24.600 / −24.336 / −25.04 dB.
- Residue (a) −5.698 / −5.308 dB, (b) −1.573 / −0.982 dB; cfl 0.2 −8.11 dB.
- J = −1 chain at 2.625 rt: 13.103 / 13.399 dB, G4_A 1.5810, c2c 4.799 / 5.030, floors −4.696 / −4.307 / −6.257, eye +4.40. At 2.5 rt: 13.000.
- m = 28 at 2.5 rt: 12.917 dB, G4_A 1.5885, floors −4.024 / −4.317 / −5.245.
- Envelope lags: 2.5681 rt (passive) / 5.7045 rt (active) at m = 30; 2.5556 rt at m = 28.
- Table 3c rows at lo 0.70 / 0.77 / 0.80 / 0.85 (both rungs).
- Table 8 cfl 0.2 row: rule 2.375 rt; 13.112 dB, G4_A 1.7738; floors −8.349 / −8.000 / −11.646; eye +8.20. Fixed 2.625 rt: 1.7759, −8.358 / −12.017.
- N = 480: 12.726 dB, G4_A 1.5028, floors −4.703 / −4.292 / −6.035. Continuum estimate 1.4245.
- Ablation (i): −9.380 / −8.822 / −12.978. Ablation (ii): −12.537 / −12.081 / −16.217.
- Degradations under the rule: 7.13 / 6.71 / 6.76 dB peak and 9.41 / 9.36 / 9.11 dB slot-mode. Optimal placement: 9.28 / 9.06 dB.

SEAT MODEL NOTE: The maintainer requested this seat (reassess3-fabric, the round-3 Fabric 🧵 re-assessor) on claude-opus-5-5 for this run, as the 2026-08-13 policy's Opus re-assessor seat. It is not Fable 5 and does not claim to be. It shared no context with the drafting, execution, pre-publication checks, the round-1 or round-2 assessors, the reworks, or the other round-3 re-assessors. The reply under assessment was executed and reworked on claude-fable-5-1. Every number in this verdict was executed by this seat on Linux x86_64 / Python 3.11.15 / numpy 2.4.6 against the released, unedited fable-model-chain/, using an instrument written from the reply's stated conventions and the promoted 07-31 listings; the session's cascade_driver.py was not opened. Reproductions are gated on relative deviation (≤ 1.3×10⁻¹³ on the gate row); exact equality was measured False and is not claimed. The repository tree was left clean (git status: 0 lines). — Fabric 🧵 (AI research agent · see agents/README.md)

<details><summary>Re-execution log (verbatim)</summary>

```text
Seat directory: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/reassess3-fabric/
Scripts:
- f3.py: the instrument, written from the round-3 reply's §1–§2 conventions and from 07-31's listed make_sig_duty / run_custom / slot_peaks / metrics. The session's cascade_driver.py was not opened. I read rw_runs.py and rw3_runs.py only to learn the ablation constructions.
- runs.py: Pool(4) job driver.
- mth.py, score_gate.py, score_c1b.py, score_chain.py, loop.py, tdiff.py: scoring and checks.

Conventions and platform:
- Released fable-model-chain/ imported unedited with PYTHONDONTWRITEBYTECODE=1. run_all.py was never run; run_all was only imported for measure_Mth_num's constants.
- Platform: python3 -c '…' → 3.11.15 2.4.6 Linux x86_64 (nproc 4).
- Coupling: cell 2's clamp h_left = 1 + κ·(h1[−1] − 1), κ = 10^(−1/20). Cell 2 reads cell 1's labelled series at the same step: exact lockstep when dt is equal, np.interp otherwise.
- Observables: cav = max|u − u0| over cell 2; drn_h = |h[−1] − 1|; slot-mode = 2|mean(dh·e^{−iφ})| over the shifted window, with the carrier referenced to the active-envelope centre (0.4·repT into the slot).
- Scoring: slots whose shifted window runs past the record are dropped; the first 4 slots are dropped.

$ python3 tdiff.py   (row-by-row table diff, 11-reply.md vs round-3-reply.md + appendix)
round1 tables: [('Table 1', 18), ('Table 2a', 28), ('Table 2b', 10), ('Table 3', 10), ('Table 3b', 8), ('Table 4', 16), ('Table 5', 42), ('Residue', 2), ('Table 6', 11), ('## 4. Grading the record', 5)]
round3 tables: [('Table 1', 18), ('Table 2a', 28), ('Table 3', 10), ('Table 3b', 8), ('Table 3c', 22), ('Table 4', 16), ('Residue', 2), ('Table 9', 4), ('Table 8', 3), ('Table 6', 11), ('## 4. Grading the record', 5)]
appendix tables: [('Table 2b', 10), ('Table 5', 42)]
IDENTICAL rows+header: Table 1 18 rows / Table 2a 28 / Table 2b 10 / Table 3 10 / Table 3b 8 / Table 4 16 / Table 5 42 / Residue 2 / Table 6 11
DIFF ## 4. Grading the record (regraded rows, expected)
HEADING CHANGED Table 5 — r1: '… every family and junction class (window rule shift = passive-chain latency)'  r3: '… every family and class (both denominations), with cell 1's own floor'

$ python3 (regex over round-3-reply.md): headings ['Table 1','Table 2a','Table 2b','Table 3','Table 3b','Table 3c','Table 4','Table 5','Table 6','Table 8','Table 9']
'Part I Table 7' ×5; bare 'Table 7' ×0. The only unresolved reference is limitation 5's 'Table 2'.

$ grep -c for withdrawn phrases in round-3-reply.md:
- 'every placement' 1 (in a withdrawal sentence); 'LF half-step' 1 (withdrawn); '44 dB' 2 (both 'not 44'); 'own operating point' 1 (mis-citation disclosure)
- 'released coupling' 0; 'released cascade' 0; "released model's own" 0; '7–9' 0; 'could build' 0; 'below the first cell' 0
- 'byte-identical' 1 and 'no measured number changed' 1 (both in the withdrawal sentence); 'exactly the plane fork' 1 (corrected)

$ python3 (split sizes): total 80071, A 59699, B 20194; A bytes 60944, B bytes 20655; appendix 4525; round-1 listings comment 55553, with appendix 60078

$ ls on the 14 notes/ paths cited in the reply: all OK.
$ grep -rl for the 9 registered key names in notes/, fable-model-chain/, fable-model-quantum/, papers/: 0 collisions each.
$ grep of 08-13: α(M = 0) = 0.9972 / 0.9976 / 0.9992 at cfl 0.2 / 0.4 / 0.8 (N = 240), §2. Present.
$ grep of 08-12: line 95 carries the regen.loop_gain −14.73 vs −24.38 dB/slot disagreement; line 115 carries the cfl amplitude move of 10.3 dB (−22.53 → −12.19). Present.
$ grep of notes/ for 'window placement|later window|sampling phase|window-scoped': no prior art for the single-cell window finding (08-02's 're-trim' refers to comparator thresholds).
$ PyMuPDF extraction of Part I §9.4: 'A junction is a gate-defined density step … the reflective loss of even a 2× density step is < 0.1 dB — the −1 to −3 dB budgeted per junction is therefore dominated by non-ideal effects: scattering at the gate gap, mode mismatch through the ungated sliver, and radiation.' The reply's quote matches.

$ python3 mth.py 240 & python3 mth.py 480
{"N": 240, "M_th_num": "np.float64(0.16894319463373797)", "bias": "np.float64(0.11826023624361658)", "secs": 31.0}
{"N": 480, "M_th_num": "np.float64(0.1587475408418196)", "bias": "np.float64(0.11112327858927372)", "secs": 66.4}
(shipped 0.16894319463373791 → 3.3×10⁻¹⁶ relative; N = 480 equals the promoted rung)

$ python3 runs.py jA.json 4
('c1P28', 83.2, 0.001388888888888889, 1612800)
('c1P30', 87.2, 0.001388888888888889, 1728000)
('c1M28', 87.8, 0.0012642926038760258, 1771741)
('c1M30', 91.7, 0.0012642926038760258, 1898294)

$ python3 score_gate.py
m=30 cell1 cav: Gw 8.287855791924049 Gm 8.4102 floor -11.828336851446547 eye 11.71 pp 0.306 | drn_h floor -11.775002445228234 | slot-mode floor -15.665
   rel dev vs promoted 8.287855791924017: 3.86e-15  exact-equal: False
   rel dev vs promoted -11.828336851447219: 5.68e-14  exact-equal: False
   rel dev vs promoted -11.775002445226676: 1.32e-13  exact-equal: False
   passive mean-1 |drn_h| 0.012374 -> T_passive 15.8296 dB; active mean-1 |drn_h| 0.033965 -> relaunch -24.600 dB
   residue: whole-slot over (a) -5.698 dB; first-quarter over (a) -5.698; over (b) -1.573; peak position (slot frac) [0.009, 0.009, 0.0084, 0.0084, 0.0084, 0.0084, 0.0084, 0.009]
m=28 cell1 cav: Gw 8.131548730367582 Gm 8.2231 floor -10.731214907969104 eye 10.64 pp 0.230 | drn_h floor -11.150570102407642 | slot-mode floor -14.610
   passive mean-1 |drn_h| 0.012349 -> T_passive 15.8117 dB; active mean-1 |drn_h| 0.032948 -> relaunch -24.336 dB
   residue: whole-slot over (a) -5.308 dB; first-quarter over (a) -5.308; over (b) -0.982; peak position (slot frac) [0.0166, 0.0167, 0.0159, 0.0158, 0.0159, 0.0159, 0.0158, 0.0166]

$ python3 runs.py jB.json 4
('c1P30c2', 196.3, 0.0006944444444444445, 3456000)
('c1P480', 209.4, 0.0006944444444444445, 3456000)
('c1M30c2', 211.0, 0.0006321463019380129, 3796589)
('c1M480', 219.7, 0.0006355873219107002, 3776035)

$ python3 score_c1b.py
cfl0.2 N240: cell1 Gw 7.3923 | floors cav -16.694 drn_h -17.028 mode -22.415 | passive transfer 15.01 dB | active mean-1 drn_h 0.02765 (relaunch -22.81) | residue (a) -8.11 dB
cfl0.4 N480: cell1 Gw 8.4681 | floors cav -11.463 drn_h -11.908 mode -15.143 | passive transfer 16.23 dB | active mean-1 drn_h 0.03573 (relaunch -25.04) | residue (a) -5.54 dB

$ python3 loop.py   (released regen._cavity / regen.loop_gain; in-model)
a_loss 0.7451522890452021; loop(0) 0.7452
[ratio 0.7*M_th_num(240)] M=0.118260 unloaded loop 0.9450; unloaded CW regen +13.32 dB; per-slot (30 rt) -14.73 dB/slot
[analytic 0.7*M_th] M=0.102958 unloaded loop 0.9162; unloaded CW regen +9.66 dB; per-slot (30 rt) -22.81 dB/slot
J=-1 lossless  r=+0.4535 [ratio] loaded loop +0.429 | passive delivered +2.58 | active delivered +3.86 | standing wave +6.83 | loaded CW regen +1.28 | CW-form G4 1.10
J=-1 lossless  r=+0.4535 [analytic] loaded loop +0.416 | passive delivered +2.58 | active delivered +3.66 | standing wave +6.83 | loaded CW regen +1.08 | CW-form G4 1.11
J=-1 lossless  r=-0.4535 [ratio] loaded loop -0.429 | passive delivered -3.53 | active delivered -4.10 | standing wave -7.78 | loaded CW regen -0.57 | CW-form G4 0.96
J=-1 lossless  r=-0.4535 [analytic] loaded loop -0.416 | passive delivered -3.53 | active delivered -4.02 | standing wave -7.78 | loaded CW regen -0.49 | CW-form G4 0.95
J=-1 9.4 bound r=+0.1509 [ratio] loaded loop +0.143 | passive delivered +0.04 | active delivered +0.34 | standing wave +2.26 | loaded CW regen +0.30 | CW-form G4 1.02
J=-1 9.4 bound r=+0.1509 [analytic] loaded loop +0.138 | passive delivered +0.04 | active delivered +0.29 | standing wave +2.26 | loaded CW regen +0.26 | CW-form G4 1.03
J=-1 11.6%     r=+0.3406 [ratio] loaded loop +0.322 | passive delivered +1.54 | active delivered +2.37 | standing wave +5.09 | loaded CW regen +0.83 | CW-form G4 1.06
J=-1 11.6%     r=+0.3406 [analytic] loaded loop +0.312 | passive delivered +1.54 | active delivered +2.25 | standing wave +5.09 | loaded CW regen +0.71 | CW-form G4 1.07
J=-3 lossless r=+0.7063 [ratio] loop +0.667 | passive +3.49 | active +6.56 | sw +11.13 | regen +3.07 | G4 1.23
J=-6 lossless r=+0.8653 [ratio] loop +0.818 | passive +2.99 | active +8.79 | sw +14.41 | regen +5.80 | G4 1.44
(J=-3 / -6 at the §9.4 bound and at 11.6 %, both biases, and the r=-|r| rows also printed; all match rw3_stored.py (2))
unloaded open-end buildup 2/(1-a) = 7.8478 = +17.895 dB
-24.38 dB/slot -> effective loop 0.9107

$ python3 -c (the r → 0 and other-phase endpoints)
0.0 passive delivered -1.00 dB active -1.00 loop 0.000 regen +0.00
0.1509 passive delivered +0.04 dB active +0.34 loop 0.143 regen +0.30
-0.1509 passive delivered -1.93 dB active -2.16 loop -0.143 regen -0.23

$ python3 runs.py jCD.json 4   (cell-2 chains and ablations)
('c2PP30c2', 197.9, 0.0006944444444444445, 3456000)
('c2PP480', 210.3, 0.0006944444444444445, 3456000)
('c2MM30c2', 217.5, 0.0006321463019380129, 3796589)
('c2MM480', 233.0, 0.0006355873219107002, 3776035)
('c2MM30', 110.6, 0.0012642926038760258, 1898294)
('c2M030', 104.4, 0.001388888888888889, 1728000)
('c2PP30', 100.9, 0.001388888888888889, 1728000)
('c2MM28', 102.0, 0.0012642926038760258, 1771741)
('c2PP28', 89.3, 0.001388888888888889, 1612800)
('abl_i', 105.8, 0.0012642926038760258, 1898294)
('abl_ii', 108.3, 0.0012642926038760258, 1898294)
('abl_iiiL', 102.3, 0.0012642926038760258, 1898294)
('abl_iiiE', 70.9, 0.0012642926038760258, 1898294)

$ python3 score_chain.py
[m30 N240 cfl0.4 J-1] single Gw 8.2879; passive stage-1->2 envelope lag 2.5681 rt; active 5.7045 rt
  shift 0.000 rt: chain worst 12.734 mean 13.139 | G4_A 1.5365 | floor cav -3.562 drn_h -3.087 mode -4.099 | eye +3.15 pp 0.997 (n 36) | c2c 4.649 / 5.003
  shift 2.500 rt: chain worst 13.000 mean 13.337 | G4_A 1.5685 | floor cav -4.637 drn_h -4.307 mode -6.163 | eye +4.29 pp 0.853 (n 36) | c2c 4.704 / 4.968
  shift 2.568 rt: chain worst 13.000 mean 13.337 | G4_A 1.5685 | floor cav -4.637 drn_h -4.307 mode -6.214 | eye +4.29 pp 0.853 (n 36) | c2c 4.704 / 4.968
  shift 2.625 rt: chain worst 13.103 mean 13.399 | G4_A 1.5810 | floor cav -4.696 drn_h -4.307 mode -6.257 | eye +4.40 pp 0.750 (n 36) | c2c 4.799 / 5.030
  Table3c lo 0.70: chain worst 13.110 mean 13.378 | G4_A 1.5819 | floor cav -10.080 drn_h -9.850 mode -12.354 | eye +9.81 pp 0.740 (n 35)
  Table3c lo 0.77: chain worst 13.512 mean 13.760 | G4_A 1.6303 | floor cav -10.865 drn_h -10.875 mode -13.083 | eye +10.61 pp 0.694 (n 35)
  Table3c lo 0.80: chain worst 13.539 mean 13.785 | G4_A 1.6336 | floor cav -8.590 drn_h -9.420 mode -13.433 | eye +8.34 pp 0.694 (n 35)
  Table3c lo 0.85: chain worst 15.433 mean 15.657 | G4_A 1.8621 | floor cav -7.007 drn_h -5.946 mode -14.083 | eye +6.81 pp 0.544 (n 35)
  cell 1 alone at lo 0.58: floor cav -20.140
[m28 N240 cfl0.4 J-1] single Gw 8.1315; passive env lag 2.5556 rt
  shift 2.500 rt: chain worst 12.917 mean 13.281 | G4_A 1.5885 | floor cav -4.024 drn_h -4.317 mode -5.245 | eye +3.65 pp 0.897 (n 36)
  shift 2.625 rt: chain worst 12.917 mean 13.281 | G4_A 1.5885 | floor cav -4.024 drn_h -4.423 mode -5.459 | eye +3.65 pp 0.897 (n 36)
  Table3c lo 0.77: chain worst 13.532 mean 13.803 | G4_A 1.6641 | floor cav -9.652 drn_h -9.393 mode -11.910 | eye +9.38 pp 0.743 (n 35)
  Table3c lo 0.80: chain worst 14.074 mean 14.345 | G4_A 1.7308 | floor cav -10.079 drn_h -10.084 mode -12.188 | eye +9.80 pp 0.743 (n 35)
  Table3c lo 0.85: chain worst 15.231 mean 15.443 | G4_A 1.8731 | floor cav -8.114 drn_h -7.036 mode -12.858 | eye +7.90 pp 0.597 (n 35)
  cell 1 alone at lo 0.60: floor cav -19.139
[m30 N240 cfl0.2 J-1] single Gw 7.3923; passive env lag 2.3889 rt -> rule 2.375 rt
  shift 2.375 rt: chain worst 13.112 mean 13.262 | G4_A 1.7738 | floor cav -8.349 drn_h -8.000 mode -11.646 | eye +8.20 pp 0.374 (n 36)
  shift 2.625 rt: chain worst 13.128 mean 13.271 | G4_A 1.7759 | floor cav -8.358 drn_h -8.985 mode -12.017 | eye +8.21 pp 0.358 (n 36)
[m30 N480 cfl0.4 J-1] single Gw 8.4681; passive env lag 2.6278 rt; shift 2.625 rt: chain worst 12.726 mean 12.952 | G4_A 1.5028 | floor cav -4.703 drn_h -4.292 mode -6.035 | eye +4.48 pp 0.561 (n 36)
  continuum first-order (240,480): G4_A 2*1.5028 - 1.5810 = 1.4245
  ablation (0) no gate: chain worst 13.103 mean 13.399 | G4_A 1.5810 | floor cav -4.696 drn_h -4.307 mode -6.257 | eye +4.40 pp 0.750 (n 36)
  ablation (i) '0' slots: 1-rt raised-cosine fall from slot start, then zero: chain worst 13.103 mean 13.395 | G4_A 1.5810 | floor cav -9.380 drn_h -8.822 mode -12.978 | eye +9.08 pp 0.724 (n 36)
  ablation (ii) (i) + '1' slots: 1-rt raised-cosine fall from 0.8 repT, then zero: chain worst 13.127 mean 13.407 | G4_A 1.5838 | floor cav -12.537 drn_h -12.081 mode -16.217 | eye +12.25 pp 0.696 (n 36)
  ablation (iii-as-labelled) (i) + '1' slots hard-cut at 0.8 repT: chain worst 13.131 mean 13.411 | G4_A 1.5844 | floor cav -13.086 drn_h -12.638 mode -16.820 | eye +12.80 pp 0.691 (n 36)
  ablation (iii-as-executed) '0' slots hard-zeroed + '1' slots hard-cut at 0.8 repT: chain worst 13.131 mean 13.411 | G4_A 1.5844 | floor cav -13.807 drn_h -13.363 mode -17.528 | eye +13.52 pp 0.690 (n 36)

$ python3 (passive per-slot peak-time lag, argmax |drn_h| per '1' slot)
N240 m30 passive per-slot peak-time lag (rt): median 0.5243 min 0.5243 max 0.5243
N480 m30 passive per-slot peak-time lag (rt): median 0.5222 min 0.5219 max 0.5222
N240 m28 passive per-slot peak-time lag (rt): median 0.5243 min 0.5236 max 0.5243
N240 m30 cfl0.2 passive per-slot peak-time lag (rt): median 0.5156 min 0.5156 max 0.5160

$ python3 -c (arithmetic on the rows above)
degradation m30 J-1 peak 7.13 mode 9.41
degradation m28 J-1 peak 6.71 mode 9.36
degradation N480 m30 J-1 peak 6.76 mode 9.11
degradation cfl0.2 m30 J-1 peak 8.34 mode 10.77
optimal-placement degradation m30 9.28 m28 9.06
ablation shares: (i) 0-slot gate 4.68 | 1-tail rc 3.16 | 1-tail hard (labelled) 3.71 | hard-zero of 0-slot first rt (exec-labelled) 0.72 | exec - (i) 4.43
gate (i) at the residue peak (0.009 slot = 0.54 units): 0.831 = -1.61 dB
J1 band [1.40,1.65] vs cfl lever 1.774/1.581/1.485: [(1.7738, False), (1.581, True), (1.4853, True)]   [1.485 is the reply's own Table 8 value; not re-executed here]

$ git -C /home/user/FableComputer status --short | wc -l
0

Not re-executed by this seat, and no number accepted from these:
- the cfl 0.8 row
- m = 28 at N = 480 (continuum 1.459)
- seeds 11 / 13
- the J = −25 rows
- N = 720
- Table 2a's boundary-driven rows and Table 2b
- Table 3 stages 3–5 and Table 3b
- Table 5 rows beyond the four degradation rows above
- the velocity plane
- the 08-13 standing falsifier
```

</details>
