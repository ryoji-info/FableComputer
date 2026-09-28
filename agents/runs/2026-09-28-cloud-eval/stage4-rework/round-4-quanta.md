### ⚛️ Quanta — **REJECT** (required edits) — round 4, 2026-09-28

VOTE: reject

REASONS: REJECT at the cap. The reason is one refuted round-4 universal plus four mechanical defects; no measurement is at fault. All 19 round-3 required edits landed (Quanta RE2 in substance), and all 170 published round-1 table rows are byte-identical in the round-4 text and appendix, with only the stated captions changed. Every decisive number I re-executed on my own instrument reproduces:
- the gate, to ≤ 1.32×10⁻¹³ relative (not bit-equal);
- the J = −1 chain: 13.1028 dB, G4_A 1.5810, c2c 4.7981;
- Table 3d at m = 28, lo 0.80: matched 1.6955 against mixed 1.7308;
- Table 9 rows (iii) −13.088 dB and (iv) −13.808 dB;
- the loop model's −1.000 to +2.582 dB range and its Part I §9.4 upper bounds;
- the latency ladder, to within a ±0.004-rt estimator spread.

The round-4 scope reduction swapped one over-reach for another, which is the failure mode the routine names:
- Item 1(c) says the 0 / −1 / −3 dB bar verdict "survives the placement lever", and the §4 G4 grade says the bar fails "at every late placement that keeps a round-spec floor". Tables 3c–3d measured only J = −1. At J = −3 (re-executed) the matched G4 is 1.790 with a −10.34 dB peak floor (m = 28, lo 0.80–0.8175), and 1.716–1.720 with −11.11 dB (m = 30).
- At J = −1 the bold conclusion holds over my full lo 0.25–0.95 scan. But the ranges printed to support it come from a scan that started at lo 0.74, so they leave out the text's own Table 3c row at lo 0.70.
- Item 6 says the matched ratio "does not" cross the bar, but Table 3d prints 1.711 and 1.705.
- The value 1.695 is printed as "1.70, below the bar".
- The header still calls the text "the round-3 text".

Substance and durability hold, and the measured core has come through four rounds untouched. Criteria 2–4 (labels, numbers, nothing oversold) do not hold for the text as written. At the cap I record these edits as required and do not soften them.

FIXES VERIFIED (round-1 required edits):
- Fabric RE1 (Table 9 row iii; the mechanism's shares) — LANDED. Table 9 now has five rows, each naming its construction. Row (iii), gate (i) plus a hard '1' cut at 0.8·repT, prints −13.09 / −12.64 / −16.82, chain 13.131, eye +12.80. I re-executed it: −13.088 / −12.640 / −16.822, chain 13.131, eye +12.804. Row (iv), a hard '0' zero plus the hard '1' cut, prints −13.81 / −13.36 / −17.53. I re-executed it: −13.808 / −13.365 / −17.528, chain 13.131, eye +13.524. The note credits the round-2 seats' −13.09. Item 4 now gives the '1'-tail share as 3.2–3.7 dB and the '0' residue as ≈ 4.7 dB under gate (i), stated as a lower bound: the 0.7 dB first round trip passes at ≈ 83 % at the 0.009-slot residue peak, and my residue argmax sits at 0.0084–0.0090 slot.
- Fabric RE2 (the J1 key's lever clause) — LANDED. The key now reads 'exits the band above at cfl = 0.2 while 1.485 at cfl = 0.8 stays inside; placement — 1.54–1.86 across Table 3c (the mixed ratio), exiting above only'. On my fine lattice the mixed-ratio minimum is 1.531 (lo 0.265), still inside [1.40, 1.65], so 'above only' holds. The residue key's 'both sides' (−8.11 / −4.21 against [−7.0, −4.5]) is correct and stays.
- Fabric RE3 (loaded-drain bound direction and endpoints) — LANDED.
- Item 2 now reads 'the largest reflection a passive junction allows, hence the *least* loading: the upper bound on the loaded loop, on cell 1's residual regeneration and on the delivered drive'.
- The range is stated as −1.0 to +2.6 dB at J = −1 in the open-end phase, with §9.4's figures as upper bounds (loop < 0.143, delivered < +0.04 dB, regeneration < +0.30 dB) and the other phase at −3.5 / −1.9 dB.
- Re-derived with the released regen.loop_gain: delivered −1.000 dB (|r| → 0) to +2.582 dB (lossless), monotone in |r| over the admissible set. §9.4's |r| < 0.1509 gives loop < 0.1426, delivered < +0.036 dB and regeneration < +0.300 dB. The other phase gives −3.529 / −1.925 dB.
- grep '+0.04 to +2.6' returns 0 hits.
- Fabric RE4 (the DS-factor assumption) — LANDED. It appears in item 2 ('the loaded loop is regen.loop_gain(M) × |r|, which keeps the released DS drain factor (1 + M)/(1 − M) at a drain that a transmitting junction no longer current-clamps'), in §2 bullet 2 and in limitation 1, and it is labelled in-model / open.
- Fabric RE5 (headline and sign-off ranges) — LANDED. The title and item 4's lead read '6.2–8.1 dB (peak) / 8.6–10.4 dB (slot-mode)'. The sign-off reads '6.2–8.1 dB shallower … in peak cav under the promoted rule (9.1–9.3 dB at the lattice-optimal placements)'. grep '9–10 dB' returns 0 hits. My fine-lattice scan reproduces the optima, −20.140 → −10.865 and −19.139 → −10.079 (9.28 / 9.06 dB); no fine-lattice point is deeper than the lattice values.
- Fabric RE6 (latency key range; excess across the grid ladder) — LANDED. Item 7 and the key read 0.518–0.525 rt with an excess of 0.018–0.025 rt (0.024 → 0.022 → 0.018 at N = 240 / 480 / 720). Re-executed with the signed-crest estimator: 0.5250 / 0.5226 / 0.5220 rt. The same rungs read 0.5238 / 0.5202 / 0.5189 by signed cross-correlation and 0.5215 / 0.5179 / 0.5167 by lock-in phase. The printed 0.518 at N = 720 therefore sits inside a ±0.003-rt estimator spread, and the grid dependence holds under every estimator (optional note in top issues).
- Kinetic RE1 (Table 9 row iii and the split; correct the round-3 record) — LANDED; same evidence as Fabric RE1. The round-4 record's 'Corrections to the round-3 record' corrects row 12: the labelled construction reproduces −13.086, and I measured −13.088.
- Kinetic RE2 (residue caption) — LANDED. Denominator (a) is now 'the mean-'1' drain-density peak inside the promoted window — the denominator of 08-02 §3.2's drn_h floor column (not of the promoted max0_below_mean1_dB, which is a source-plane cav ratio)'. The rows are byte-identical, and I re-executed the key at −5.698 / −5.308 dB.
- Kinetic RE3 (headline precision; slot-mode-only cfl escape; sign) — LANDED. The title reads '8.6–10.4 dB (slot-mode)' and '…or, in slot-mode, at cfl = 0.2'. Item 4 reads '5.5 dB at cfl = 0.8' as a positive degradation; its denomination is left implicit (optional).
- Kinetic RE4 (scope every copy of the loaded range) — LANDED. Item 3, §4 row 1 and the §5 passive-transfer key all read '−1.0 to +2.6 dB at J = −1 in the open-end phase (−3.5 dB in the other; < +0.04 dB under §9.4's bound)'.
- Kinetic RE5 (DS factor) — LANDED; same as Fabric RE4.
- Kinetic RE6 (limitation 9's flush item) — LANDED. It now says the flush question was resolved at the 4-ps slot (07-22's post-promotion annotation, 07-22-flush-noise-figure-negative, 07-23-reset-switch-adjudication; INDEX row 07-22 cavity-ringdown confirms) and is not re-examined here.
- Kinetic RE7 (appendix Table 5 caption) — LANDED. The caption carries the window rule (rounded to the ⅛-rt grid), the ideal-buffer coupling, cfl = 0.4, and the note that the cell-1 columns use the promoted window. My diff confirms all 44 rows byte-identical to the published round-1 Table 5.
- Kinetic RE8 (correct the round-3 record) — LANDED in the round-4 record's corrections section. It covers:
- row 5 (the DS factor);
- row 12 (−13.09 reproduced by the labelled construction);
- the 'what was not changed' paragraph (Tables 4 and 6 already numbered; Table 5 caption changed; Table 5 built from tables_split.json);
- the overstated 'all 29 … applied'.
A new inaccuracy in round-4 record row 15 is noted in top issues.
- Quanta RE1 (Table 9 row iii and the shares) — LANDED; same evidence as Fabric RE1. The '0'-residue share is stated as ≈ 4.7 dB, a lower bound, ≈ 5.4 dB with the first round trip removed.
- Quanta RE2 (late-window G4: mixed denominator, plateau edge, rescope) — LANDED IN SUBSTANCE, with new defects in how it was printed.
- Landed: Table 3c's caption now calls G4_A 'a mixed ratio'. A new Table 3d prints matched against mixed. Item 1(c), item 6, the §4 G4 grade, the §5 discriminant, the J1 key and limitation 6 are rescoped.
- My re-execution reproduces Table 3d's rows: m = 28, lo 0.80 matched 1.6955 / mixed 1.7308; m = 30, lo 0.8075 1.7108 / 1.7631.
- At J = −1 the conclusion holds over my full lo 0.25–0.95 scan: no peak-cav round-spec placement has matched G4 ≥ 1.7.
- New defects (required edits 1–4): the rescoping is extended beyond J = −1, where it is refuted at J = −3; its printed ranges are truncated by the scan (lo 0.74–0.83 only); item 6's wording is false; and 1.695 is rounded to '1.70, below the bar'.
- The m = 30 range 1.606–1.624 originated with my persona's round-3 seat, whose scan also started late. Disclosed.
- Quanta RE3 (bound direction) — LANDED; same as Fabric RE3.
- Quanta RE4 (DS-factor assumption; correct the record) — LANDED. It appears in item 2, §2 bullet 2 and limitation 1, and the round-4 record corrects round-3 row 5.
- Quanta RE5 (appendix captions carry their own scope) — LANDED.
- Table 5: see Kinetic RE7.
- Table 2b: the caption now reads 'the single released cell driven at its source clamp by the duty-0.8 gated launch at amplitude A, over its identical passive twin, promoted window, ratio bias, cfl = 0.4, seed 7'. Its 12 rows are byte-identical.

REQUIRED EDITS:
- 1. Item 1(c) and the §4 G4 grade extend a J = −1 measurement to the −3 dB class, where it is false. This is new in round 4 and falls under the routine's rule against a replacement universal.
- What the text says: item 1(c) opens 'The bar verdict is a rule verdict, and it survives the placement lever'; the bar verdict is item 1's 'failed at 0, −1 and −3 dB'. The §4 Part I Table 7 G4 grade says the bar fails 'at 0 / −1 / −3 dB under the ideal buffer and the pre-registered window rule — and at every late placement that keeps a round-spec floor'.
- What was measured: Tables 3c and 3d measured J = −1 only.
- Re-executed at J = −3 (m = 28 and 30, N = 240, seed 7, cfl 0.4, the reply's matched convention, 0.0025-slot lattice over lo 0.25–0.95):
  - m = 28: all 12 round-spec placements (lo 0.79–0.8175) have matched G4 ≥ 1.7. At lo 0.80–0.8175 it is 1.790 (mixed 1.827), with the stage-2 floor at −10.34 dB peak cav, −10.16 to −10.21 dB drn_h and −12.4 to −12.8 dB slot-mode.
  - m = 30: 10 such placements. For example, lo 0.77–0.79 gives matched 1.716–1.720 at −11.11 dB peak (slot-mode −13.3 to −13.8).
- The J = 0 class holds: at m = 30 matched G4 is ≤ 1.568 at all 36 round-spec placements, and m = 28 has none.
- My rule-window rows reproduce Table 1: J = −3 G4_A 1.6776 / 1.6759; J = 0 1.5247 / 1.5386.
- Fix: scope both statements to J = −1, the only class measured, and report the J = −3 result, or withdraw 'survives the placement lever' for the −3 dB class.
- 2. The ranges behind the J = −1 rescoping are truncated by the scan (item 1(c), the note under Table 3d, the §4 G4 grade). rw4_stored.py scans lo only over np.arange(0.74, 0.8301, 0.0025), so the edges of its scan window are printed as measured edges.
- Full 0.0025-slot lattice, lo 0.25–0.95, m = 30, N = 240, seed 7, J = −1, peak cav: the round-spec placements run lo 0.70–0.79 (37 points). There matched G4 is 1.573–1.624 and mixed 1.582–1.633.
- The text instead gives 'lo 0.74–0.79', 'matched 1.606–1.624' / '1.61–1.62' and 'mixed 1.62–1.63'. Its own Table 3c row at lo = 0.70 reads −10.08 dB with G4_A 1.582.
- Matched G4 ≥ 1.7 occurs over lo 0.8075–0.95 at m = 30 (peak floors −8.59 to −2.07 dB) and lo 0.83–0.95 at m = 28 (−8.36 to −3.17 dB). The text instead says 'lo ≥ 0.8075 … floor −7.3 to −8.6 dB' and 'lo = 0.83 … −8.4 dB'.
- The J = −1 conclusion survives the full scan: at either rung, no peak-cav round-spec placement has matched G4 ≥ 1.7.
- Fix: correct the ranges and state that the scan covered lo 0.25–0.95.
- 3. Item 6 makes a false statement. It reads 'at a late sampling phase Table 3c's mixed ratio crosses the bar at J = −1 only where the stage-2 floor fails the round spec or at a plateau edge, and the matched ratio does not (item 1c, Table 3d)'. Table 3d itself prints matched 1.711 (m = 30, lo 0.8075–0.825) and 1.705 (m = 28, lo 0.83); I re-executed 1.7108 and 1.7050. Fix: reword to what was measured — at J = −1 the matched ratio crosses 1.7 only where the peak stage-2 floor fails the round spec.
- 4. A value is rounded onto the bar. The m = 28 matched maximum is 1.6955 (Table 3d: 1.695; I re-executed 1.6955). It is printed as '1.70' beside text saying it is below the ≥ 1.7 bar, in four places:
- item 1(c): '1.63–1.70 (m = 28), below the bar';
- the §4 G4 grade cell: '1.61–1.70';
- the same row's reason column: '1.63–1.70';
- limitation 6: 'matched: 1.62 / 1.70'.
Fix: print 1.695 wherever it is compared with 1.7. A 0.005 margin cannot be carried at two decimals.
- 5. A stale self-label remains. The second blockquote paragraph is headed 'Rework history, disclosed (stage 4 of the routine; this is the round-3 text)' in the round-4 text, directly above 'Round 4 (the cap; this text)'. Fix: relabel it as the account of rounds 2–3.

TOP ISSUES:
- REQUIRED 1 — a refuted round-4 universal at J = −3. The late-placement result was measured only at J = −1, but item 1(c) ('survives the placement lever') and the §4 G4 grade ('at every late placement that keeps a round-spec floor') apply it to the 0 / −1 / −3 dB bar verdict.
- At J = −3, m = 28, lo 0.80: chain 14.857 dB over a single cell of 8.301 dB at lo − lag, giving matched G4 1.7897 (mixed 1.8271). The floor is −10.34 dB cav, −10.21 dB drn_h and −12.36 dB slot-mode (eye +10.01, 35 slots).
- At J = −3, m = 30, lo 0.77: matched 1.7156 at −11.11 dB.
- In the model, a −3 dB ideal-buffer junction sampled late meets both Part I Table 7's bar and a round-spec floor, in all three denominations at m = 28. The bench-facing −1 dB configuration is unaffected.
- REQUIRED 2 — the J = −1 ranges come from a scan truncated at lo 0.74 and 0.83.
- m = 30: the round-spec set is lo 0.70–0.79, with matched 1.573–1.624 and mixed 1.582–1.633. The text prints lo 0.74–0.79 with matched 1.606–1.624, and its own Table 3c lo 0.70 row (−10.08 dB, G4_A 1.582) contradicts that.
- Matched G4 ≥ 1.7 extends to lo 0.95 at both rungs, with peak floors down to −2.1 dB.
- The J = −1 conclusion survives on the full lattice.
- REQUIRED 3 — item 6's 'and the matched ratio does not' is contradicted by Table 3d's own 1.711 / 1.705.
- REQUIRED 4 — '1.70 … below the bar' for 1.695, in four places.
- REQUIRED 5 — the header still says 'this is the round-3 text'.
- Optional — name the denomination of the J = −1 universal.
- It holds for peak cav and peak drn_h. It also holds with G4 and floor both in slot-mode (the matched lock-in G4 is at most 1.627 / 1.616 at every slot-mode round-spec placement).
- A cav G4 paired with a slot-mode floor does reach it: matched 1.711 at −13.43 dB (m = 30, lo 0.8075). There are 39 such lattice placements at m = 30 and 33 at m = 28; 27 and 26 of them also clear the strict 11.82-dB anchor.
- Suggested wording: '(peak cav, as Table 3d)'.
- Optional — the latency estimator.
- The printed values are 0.525 / 0.523 / 0.518 rt.
- Signed crest gives 0.5250 / 0.5226 / 0.5220; signed cross-correlation 0.5238 / 0.5202 / 0.5189; lock-in phase 0.5215 / 0.5179 / 0.5167. At m = 28, N = 240 the range is 0.5236–0.5293.
- Suggestion: state the estimator (the median per-slot |drn_h| peak time, in analyze.py's peaktime_lag) and a spread of about ±0.004 rt.
- Item 7's '0.024' at N = 240 is the junction-sweep family's value (0.5243); it sits beside the key's 0.525.
- Optional, a disclosure accuracy point — the discriminant's 'G4 ≈ 1.0–1.1 in the loop model's CW form (item 2)' points to something item 2 does not contain. Item 2 has the loaded and unloaded CW regeneration (+1.3 / +13.3 dB) but neither the G4 value nor its formula: (1.28 + 13.32)/13.32 = 1.10 lossless, 1.02 at §9.4's bound, 0.95–0.96 in the other phase, computed in rw3_stored.py. Round-4 record row 15 says 'the CW-form formula is already in item 2's parenthetical', which is inaccurate. Disclose it in the PR or closing note.
- Optional — item 2 compares a steady-state loop-model figure with a time-domain measurement. The loop-model loaded delivery (+2.6 / +3.9 dB, CW steady state) is set against the measured unloaded +16 / +24.6 dB. The same model's unloaded values are +17.9 and +31.2 dB (2/(1 − 0.945)). Item 5's '+3.9 dB of the 24.6' has the same mismatch.
- Optional — 'A further caveat: and 08-12 §3 registered …' has a stray 'and'. The regen.loop_gain disagreement is in 08-12 §4; §3 holds the decay column.
- Optional — item 1(c)'s 'runs 1.54–1.62 (m = 30) … for any stage-2 window with lo ≤ 0.75' is a claim about Table 3c's coarse lattice. On the fine lattice the minimum is 1.531 at lo 0.265 (m = 28: 1.547 at lo 0.2875).
- Optional — item 4's '5.5 dB at cfl = 0.8' follows '8.6–10.4 dB in slot-mode' but is the peak-cav figure (−8.886 → −3.376). The slot-mode degradation at cfl 0.8 is 8.2 dB. Name the denomination.
- Optional, for pasting — 12-listings.md, the comment to paste, carries the round-1 render_tables.py (13,814 characters). The current listings/render_tables.py (14,567 characters) differs only in four caption strings and the Table 5 section. Paste the current one, or the appendix's round-4 captions cannot be reproduced from the posted listings.
- Optional, on the discriminant's framing (honest but thin) — its central band [1.40, 1.65] is the ideal-buffer construct's value, and the text itself says no passive junction realises that construct. For Part I's −1 dB passive-junction die the loop model expects the '< 1.40' arm. Consider re-registering the discriminant as one-sided, or leading with that expectation.
- Verified, not defects:
- Tables: 170 of 170 published round-1 table rows are byte-identical (Tables 1, 2a, 2b, 3, 3b, 4, 5, 6 and the residue table, including headers). The captions changed only for Table 1's bracket paragraph, Table 2b, Table 5 and the residue table, as the record states. The new tables are 3c, 3d, 8 and 9.
- Comment sizes: 42,915 / 23,449 / 21,695 characters; listings plus appendix is 60,476, under 65,536. The three-comment split and the appendix are acceptable.
- Withdrawn phrases ('released coupling', '7–9', '9–10 dB', '+0.04 to +2.6', 'upper bound on the loading', '3.2–4.4', '0.523–0.525', 'the promoted floor key's own', '44 dB', 'half-step', 'every placement', 'byte-identical', 'no measured number') survive only inside disclosure sentences.
- Standing rule 10 is clean in both directions. The nine key names have 0 collisions in notes/, papers/ and both results.json files. The prior art (07-22 ring-down, the 08-12 cfl lever and early-window clause, 08-02 planes, 08-13 α at M = 0) is credited and not re-announced. The J = −1 matched-window scan and the loaded-drain range are new to the record. 08-02 §4's orders 0.706 / 0.548 / 0.136 / 0.888 and 08-01 A_fix 0.0117–0.0140 / 0.0076–0.0140 check against the notes.
- Disclosures: the round-2 regression, the round-3 record's corrections, what was withdrawn in each round, and the declined time-domain loaded-junction run are stated honestly.
- Scope is not vacuous: the durable content stands under the stated scopes. That content is: 08-01 §4's waveform premise to ≤ 0.6 dB at matched amplitude; '≈ 2×' as the 1.96 small-signal limit; a windowed floor not transferring through a resonant stage; and the single-cell floor's 8.3-dB window dependence.
- The loaded-drain range is a fair range with both assumptions named.

SEAT MODEL NOTE: The maintainer requested this seat (reassess4-quanta, the Quanta persona, round-4 re-assessor) on claude-opus-5-5 for this run, as the 2026-08-13 policy's Opus re-assessor seat.
- It is not Fable 5 and does not claim to be.
- It shared no context with the drafting, execution, pre-publication checks, the round-1 to round-3 assessors, the reworks or the other round-4 re-assessors. It held every prior round's record.
- The reply under assessment was executed and reworked on claude-fable-5-1.
- Every number in this verdict was executed by this seat on Linux x86_64 / Python 3.11.15 / numpy 2.4.6 against the released, unedited fable-model-chain/, using q4.py, an instrument I wrote from the reply's stated definitions. The session's cascade_driver.py was never opened.
- Reproductions are gated on relative deviation (≤ 1.32×10⁻¹³ on the gate row). Exact equality was measured False and is not claimed.
- run_all.py was never run, and the repository tree was left clean (git status: 0 lines).
- Disclosure: the scan-truncated m = 30 range (1.606–1.624) that required edit 2 corrects originated with my persona's round-3 seat, whose scan also started late.

Adoptable item: before any further use of this construct, run the late-placement matched scan at every junction class the bar verdict names (0 / −1 / −3 / −6 dB) over the full lo 0.25–0.95 lattice. With q4.py and score4.py this takes about 4 minutes per class pair on 4 workers. Then have the builder assert that no quoted range touches a scan edge.

Improvement scout (community process): a GitHub issue template for outside bench reports against Part I Table 7's gates G1–G5. It would carry fields for the bias rule, the launch-amplitude pin, the sampling-phase pin and the floor denomination, so that the first external measurement enters the record in its own conventions instead of being re-derived by the crew. First step: draft .github/ISSUE_TEMPLATE/bench-report.md from notes/2026-08-01-bench-gate-g1-reissued.md's pinned protocol.

— Quanta ⚛️ (AI research agent · see agents/README.md)

<details><summary>Re-execution log (verbatim)</summary>

```text
Seat directory: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/reassess4-quanta/.
- Instrument: q4.py, my own, written from the reply's §1–§2 definitions and the promoted 07-31 listings (make_sig_duty, run_custom stepping, slot_peaks, metrics).
- Coupling: cell 2's clamp h_left = 1 + κ·g(t)·(h1[−1] − 1), κ = 10^(J/20). It is read causally: cell 2 stepping from t_k sees cell 1's drain state at time t_k. Chains with equal dt run in exact lockstep; the c2c run (active cell 1 feeding passive cell 2) interpolates in physical time.
- Slot-mode: the carrier lock-in amplitude of drn_h over the window.
- Released fable-model-chain/ was imported unedited, with PYTHONDONTWRITEBYTECODE=1. run_all.py was imported only for measure_Mth_num and never run.
- cascade_driver.py was never opened. analyze.py's peaktime_lag and the rw4_*.py listings were read for audit only.

$ python3 -c "import sys,numpy,platform;print(sys.version, numpy.__version__, platform.machine(), platform.system())"; nproc
3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0] 2.4.6 x86_64 Linux
4

$ PYTHONDONTWRITEBYTECODE=1 python3 phase1.py   (released measure_Mth_num; then Pool(4) runs: passive/active two-cell chains at J = −1, m = 30/28, N = 240; passive chains at N = 480/720; the ablation row-iii chain)
M_th_num(240) = np.float64(0.16894319463373797) shipped 0.16894319463373791 rel dev 3.285787944971905e-16 [32s]
bias = np.float64(0.11826023624361658)
done ('P_m30_N240', 1728000, 0.001388888888888889, 91.7) [123s]
done ('A_m30_N240', 1898294, np.float64(0.0012642926038760258), 102.4) [134s]
done ('P_m28_N240', 1612800, 0.001388888888888889, 92.4) [226s]
done ('A_m28_N240', 1771741, np.float64(0.0012642926038760258), 103.6) [227s]
done ('P_m30_N480', 3456000, 0.0006944444444444445, 203.2) [235s]
done ('Aiii_m30_N240', 1898294, np.float64(0.0012642926038760258), 114.2) [341s]
done ('P_m30_N720', 5184000, 0.000462962962962963, 352.4) [384s]
PHASE1 DONE [384s]

$ PYTHONDONTWRITEBYTECODE=1 python3 loopmodel.py   (released regen._cavity / loop_gain; loaded-drain model as the reply defines it)
a_loss 0.7451522890452021 loop(ratio 0.7*M_th_num(240)) 0.945 loop(analytic 0.7*M_th) 0.9162 loop(0) 0.7452
unloaded open-end build-up 2/(1-a) = 7.8478 = 17.895 dB
J=-1: |t|=0.8913; lossless |r|=0.4535; Part I 9.4 bound (reflective loss<0.1 dB) |r|<0.1509; 11.6% budget |r|=0.3406
  |r|->0    r=+|r| ratio   : loaded loop +0.0000; delivered passive -1.000 dB, active -1.000 dB; drain standing wave +0.000 dB; loaded CW regen +0.000 dB (unloaded +13.324)
  |r|->0    r=+|r| analytic: loaded loop +0.0000; delivered passive -1.000 dB, active -1.000 dB; drain standing wave +0.000 dB; loaded CW regen +0.000 dB (unloaded +9.661)
  |r|->0    r=-|r| ratio   : loaded loop -0.0000; delivered passive -1.000 dB, active -1.000 dB; drain standing wave -0.000 dB; loaded CW regen -0.000 dB (unloaded +13.324)
  |r|->0    r=-|r| analytic: loaded loop -0.0000; delivered passive -1.000 dB, active -1.000 dB; drain standing wave -0.000 dB; loaded CW regen -0.000 dB (unloaded +9.661)
  9.4 bound r=+|r| ratio   : loaded loop +0.1426; delivered passive +0.036 dB, active +0.336 dB; drain standing wave +2.256 dB; loaded CW regen +0.300 dB (unloaded +13.324)
  9.4 bound r=+|r| analytic: loaded loop +0.1382; delivered passive +0.036 dB, active +0.292 dB; drain standing wave +2.256 dB; loaded CW regen +0.256 dB (unloaded +9.661)
  9.4 bound r=-|r| ratio   : loaded loop -0.1426; delivered passive -1.925 dB, active -2.158 dB; drain standing wave -2.346 dB; loaded CW regen -0.232 dB (unloaded +13.324)
  9.4 bound r=-|r| analytic: loaded loop -0.1382; delivered passive -1.925 dB, active -2.125 dB; drain standing wave -2.346 dB; loaded CW regen -0.199 dB (unloaded +9.661)
  11.6%     r=+|r| ratio   : loaded loop +0.3219; delivered passive +1.543 dB, active +2.374 dB; drain standing wave +5.089 dB; loaded CW regen +0.831 dB (unloaded +13.324)
  11.6%     r=+|r| analytic: loaded loop +0.3120; delivered passive +1.543 dB, active +2.249 dB; drain standing wave +5.089 dB; loaded CW regen +0.706 dB (unloaded +9.661)
  11.6%     r=-|r| ratio   : loaded loop -0.3219; delivered passive -2.964 dB, active -3.424 dB; drain standing wave -5.581 dB; loaded CW regen -0.459 dB (unloaded +13.324)
  11.6%     r=-|r| analytic: loaded loop -0.3120; delivered passive -2.964 dB, active -3.359 dB; drain standing wave -5.581 dB; loaded CW regen -0.394 dB (unloaded +9.661)
  lossless  r=+|r| ratio   : loaded loop +0.4286; delivered passive +2.582 dB, active +3.861 dB; drain standing wave +6.830 dB; loaded CW regen +1.279 dB (unloaded +13.324)
  lossless  r=+|r| analytic: loaded loop +0.4155; delivered passive +2.582 dB, active +3.664 dB; drain standing wave +6.830 dB; loaded CW regen +1.082 dB (unloaded +9.661)
  lossless  r=-|r| ratio   : loaded loop -0.4286; delivered passive -3.529 dB, active -4.098 dB; drain standing wave -7.777 dB; loaded CW regen -0.569 dB (unloaded +13.324)
  lossless  r=-|r| analytic: loaded loop -0.4155; delivered passive -3.529 dB, active -4.018 dB; drain standing wave -7.777 dB; loaded CW regen -0.490 dB (unloaded +9.661)
open-end phase, J=-1, |r| in [0, lossless]: delivered passive min -1.000 max 2.582 dB, monotone increasing: True
loaded loop (ratio) over the same set: 0.0000 .. 0.4286
08-12 check: loop 0.9450/rt over 30 rt -> -14.73 dB/slot; analytic -22.81 dB/slot

$ PYTHONDONTWRITEBYTECODE=1 python3 score.py   (gate; J = −1 chains; Table 3d matched vs mixed; full placement scan lo 0.25–0.95, 0.0025-slot lattice, three denominations)
=== m=30 N=240 cell 1 (gate): Gw 8.287855791924049 Gm 8.4102 floor cav -11.828336851446547 drn_h -11.775002445228234 slot-mode -15.665 eye 11.705 pp 0.3058
    rel dev Gw: 3.858e-15 (exact equality: False)
    rel dev floor cav: 5.677e-14 (exact equality: False)
    rel dev floor drn_h: 1.323e-13 (exact equality: False)
  passive stage-1->2 envelope lag 5.0929 units = 2.5464 rt; per-slot crest lag median 0.5250 rt [0.5250, 0.5250]
  [unshifted] lo=0.25000: chain worst 12.7344 mean 13.1388 | G4_A worst 1.5365 mean 1.5622 | stage-2 floor cav -3.562 drn_h -3.087 slot-mode -4.099 | eye 3.148 pp 0.997 (n 36)
  [exact lag (reply 5.136/5.111 units)] lo=0.33560: chain worst 12.9998 mean 13.3371 | G4_A worst 1.5685 mean 1.5858 | stage-2 floor cav -4.637 drn_h -4.307 slot-mode -6.214 | eye 4.292 pp 0.853 (n 36)
  [rule 2.625 rt] lo=0.33750: chain worst 13.1028 mean 13.3987 | G4_A worst 1.5810 mean 1.5932 | stage-2 floor cav -4.696 drn_h -4.307 slot-mode -6.257 | eye 4.395 pp 0.750 (n 36)
  cell-1 active mean-'1' drn_h 0.03397 -> A*(J=-1) 0.03027; relaunch -24.600 dB; passive transfer 15.830 dB
  lo 0.7000: chain 13.110 mixed 1.5819 matched 1.5726 (single@lo-lag 8.337) | floor cav -10.08 drn_h -9.85 slot-mode -12.35 (n 35)
  lo 0.7400: chain 13.390 mixed 1.6156 matched 1.6061 (single@lo-lag 8.337) | floor cav -10.38 drn_h -10.05 slot-mode -12.76 (n 35)
  lo 0.7675: chain 13.390 mixed 1.6156 matched 1.6061 (single@lo-lag 8.337) | floor cav -10.86 drn_h -10.88 slot-mode -13.08 (n 35)
  lo 0.7700: chain 13.509 mixed 1.6299 matched 1.6204 (single@lo-lag 8.337) | floor cav -10.86 drn_h -10.88 slot-mode -13.08 (n 35)
  lo 0.7900: chain 13.537 mixed 1.6334 matched 1.6239 (single@lo-lag 8.337) | floor cav -10.20 drn_h -9.48 slot-mode -13.57 (n 35)
  lo 0.8000: chain 13.539 mixed 1.6336 matched 1.6240 (single@lo-lag 8.337) | floor cav -8.59 drn_h -9.42 slot-mode -13.43 (n 35)
  lo 0.8075: chain 14.612 mixed 1.7631 matched 1.7108 (single@lo-lag 8.541) | floor cav -8.59 drn_h -9.42 slot-mode -13.43 (n 35)
  lo 0.8175: chain 14.486 mixed 1.7479 matched 1.7110 (single@lo-lag 8.467) | floor cav -8.41 drn_h -7.92 slot-mode -13.75 (n 35)
  lo 0.8200: chain 14.486 mixed 1.7479 matched 1.7110 (single@lo-lag 8.467) | floor cav -8.41 drn_h -7.92 slot-mode -13.82 (n 35)
  lo 0.8250: chain 14.486 mixed 1.7479 matched 1.7110 (single@lo-lag 8.467) | floor cav -8.41 drn_h -7.92 slot-mode -13.87 (n 35)
  lo 0.8300: chain 14.486 mixed 1.7479 matched 1.7110 (single@lo-lag 8.467) | floor cav -7.34 drn_h -7.92 slot-mode -13.82 (n 35)
  lo 0.8500: chain 15.433 mixed 1.8621 matched 1.6462 (single@lo-lag 9.375) | floor cav -7.01 drn_h -5.95 slot-mode -14.08 (n 35)
  [f_cav] round-spec (<= -10 dB) placements on the 0.0025 lattice, lo in [0.25, 0.95]: lo 0.7000..0.7900 (37 pts); matched G4 1.5726..1.6239; mixed 1.5819..1.6334
      placements with round-spec floor AND matched G4 >= 1.7: 0; with mixed >= 1.7: 0
  [f_drn] round-spec (<= -10 dB) placements on the 0.0025 lattice, lo in [0.25, 0.95]: lo 0.7150..0.7750 (25 pts); matched G4 1.5726..1.6239; mixed 1.5819..1.6334
      placements with round-spec floor AND matched G4 >= 1.7: 0; with mixed >= 1.7: 0
  [f_mode] round-spec (<= -10 dB) placements on the 0.0025 lattice, lo in [0.25, 0.95]: lo 0.5175..0.9400 (170 pts); matched G4 1.5726..2.0118; mixed 1.5819..1.8621
      placements with round-spec floor AND matched G4 >= 1.7: 39 -> lo 0.8075..0.9400, matched 1.7100..2.0118, floor -10.19..-14.10; with mixed >= 1.7: 49
  matched G4 >= 1.7 anywhere in [0.25, 0.95]: lo 0.8075, 0.8100, 0.8125 ... 0.9450, 0.9475, 0.9500 (43 pts)
=== m=28 N=240 cell 1 (gate): Gw 8.131548730367582 Gm 8.2231 floor cav -10.731214907969104 drn_h -11.150570102407642 slot-mode -14.610 eye 10.640 pp 0.2297
  passive stage-1->2 envelope lag 5.0749 units = 2.5374 rt; per-slot crest lag median 0.5236 rt [0.5236, 0.5236]
  [unshifted] lo=0.25000: chain worst 12.6232 mean 13.0390 | G4_A worst 1.5524 mean 1.5856 | stage-2 floor cav -2.924 drn_h -2.433 slot-mode -3.200 | eye 2.501 pp 1.041 (n 36)
  [exact lag (reply 5.136/5.111 units)] lo=0.34127: chain worst 12.9173 mean 13.2814 | G4_A worst 1.5885 mean 1.6151 | stage-2 floor cav -4.024 drn_h -4.423 slot-mode -5.340 | eye 3.653 pp 0.897 (n 36)
  [rule 2.5 rt] lo=0.33929: chain worst 12.9173 mean 13.2814 | G4_A worst 1.5885 mean 1.6151 | stage-2 floor cav -4.024 drn_h -4.308 slot-mode -5.244 | eye 3.653 pp 0.897 (n 36)
  cell-1 active mean-'1' drn_h 0.03295 -> A*(J=-1) 0.02937; relaunch -24.336 dB; passive transfer 15.812 dB
  lo 0.7000: chain 13.010 mixed 1.5999 matched 1.5774 (single@lo-lag 8.248) | floor cav -8.66 drn_h -8.65 slot-mode -11.25 (n 35)
  lo 0.7400: chain 13.010 mixed 1.5999 matched 1.5774 (single@lo-lag 8.248) | floor cav -9.39 drn_h -9.38 slot-mode -11.84 (n 35)
  lo 0.7675: chain 13.532 mixed 1.6641 matched 1.6336 (single@lo-lag 8.283) | floor cav -9.65 drn_h -9.38 slot-mode -11.83 (n 35)
  lo 0.7700: chain 13.532 mixed 1.6641 matched 1.6336 (single@lo-lag 8.283) | floor cav -9.65 drn_h -9.39 slot-mode -11.91 (n 35)
  lo 0.7900: chain 13.532 mixed 1.6641 matched 1.6336 (single@lo-lag 8.283) | floor cav -9.99 drn_h -10.22 slot-mode -12.21 (n 35)
  lo 0.8000: chain 14.074 mixed 1.7308 matched 1.6955 (single@lo-lag 8.301) | floor cav -10.08 drn_h -10.09 slot-mode -12.19 (n 35)
  lo 0.8075: chain 14.074 mixed 1.7308 matched 1.6955 (single@lo-lag 8.301) | floor cav -10.08 drn_h -9.33 slot-mode -12.40 (n 35)
  lo 0.8175: chain 14.074 mixed 1.7308 matched 1.6955 (single@lo-lag 8.301) | floor cav -10.08 drn_h -9.33 slot-mode -12.64 (n 35)
  lo 0.8200: chain 14.074 mixed 1.7308 matched 1.6955 (single@lo-lag 8.301) | floor cav -9.20 drn_h -9.33 slot-mode -12.64 (n 35)
  lo 0.8250: chain 14.074 mixed 1.7308 matched 1.6955 (single@lo-lag 8.301) | floor cav -8.37 drn_h -9.31 slot-mode -12.57 (n 35)
  lo 0.8300: chain 14.154 mixed 1.7406 matched 1.7050 (single@lo-lag 8.301) | floor cav -8.36 drn_h -9.20 slot-mode -12.46 (n 35)
  lo 0.8500: chain 15.231 mixed 1.8731 matched 1.6939 (single@lo-lag 8.992) | floor cav -8.11 drn_h -7.04 slot-mode -12.86 (n 35)
  [f_cav] round-spec (<= -10 dB) placements on the 0.0025 lattice, lo in [0.25, 0.95]: lo 0.7925..0.8175 (11 pts); matched G4 1.6336..1.6955; mixed 1.6641..1.7308
      placements with round-spec floor AND matched G4 >= 1.7: 0; with mixed >= 1.7: 9
  [f_drn] round-spec (<= -10 dB) placements on the 0.0025 lattice, lo in [0.25, 0.95]: lo 0.7750..0.8000 (11 pts); matched G4 1.6336..1.6955; mixed 1.6641..1.7308
      placements with round-spec floor AND matched G4 >= 1.7: 0; with mixed >= 1.7: 2
  [f_mode] round-spec (<= -10 dB) placements on the 0.0025 lattice, lo in [0.25, 0.95]: lo 0.5925..0.9500 (144 pts); matched G4 1.5774..2.1032; mixed 1.5999..1.8960
      placements with round-spec floor AND matched G4 >= 1.7: 33 -> lo 0.8300..0.9500, matched 1.7040..2.1032, floor -10.54..-13.30; with mixed >= 1.7: 52
  matched G4 >= 1.7 anywhere in [0.25, 0.95]: lo 0.8300, 0.8325, 0.8400 ... 0.9450, 0.9475, 0.9500 (33 pts)

$ python3 - (scan.json summary)
30 lo<=0.75 mixed 1.5307..1.6156 matched 1.5717..1.6061
  peak-cav round-spec lo list: 0.7 .. 0.79 count 37 gaps: []
  peak-cav strict-anchor placements: 0
   slot-mode&matched>=1.7: lo 0.8075 matched 1.7108 mixed 1.7631 slot-mode -13.43 peak cav -8.59 drn_h -9.42 n 35
   ... of which slot-mode also clears the strict 11.82 anchor: 27
  matched>=1.7: lo 0.8075..0.9500, peak cav floor range -8.59..-2.07
28 lo<=0.75 mixed 1.5473..1.5999 matched 1.5665..1.6082
  peak-cav round-spec lo list: 0.7925 .. 0.8175 count 11 gaps: []
  peak-cav strict-anchor placements: 0
   slot-mode&matched>=1.7: lo 0.8300 matched 1.7050 mixed 1.7406 slot-mode -12.46 peak cav -8.36 drn_h -9.20 n 35
   ... of which slot-mode also clears the strict 11.82 anchor: 26
  matched>=1.7: lo 0.8300..0.9500, peak cav floor range -8.36..-3.17
30 min mixed lo<=0.75 at lo 0.265 1.5307 chain 12.686 floor -3.56
28 min mixed lo<=0.75 at lo 0.2875 1.5473 chain 12.582 floor -3.72

$ PYTHONDONTWRITEBYTECODE=1 python3 scan_mode.py   (G4 and floor in the SAME denomination, matched convention)
m=30 [peak_drn: G4 and floor both in this denomination, matched]: round-spec placements 25 (lo 0.715..0.775), G4 there 1.5514..1.5623; with G4 >= 1.7: 0
m=30 [mode: G4 and floor both in this denomination, matched]: round-spec placements 170 (lo 0.5175..0.94), G4 there 1.5140..1.6268; with G4 >= 1.7: 0
m=28 [peak_drn: G4 and floor both in this denomination, matched]: round-spec placements 11 (lo 0.775..0.8), G4 there 1.5901..1.6187; with G4 >= 1.7: 0
m=28 [mode: G4 and floor both in this denomination, matched]: round-spec placements 144 (lo 0.5925..0.95), G4 there 1.5123..1.6156; with G4 >= 1.7: 0

$ python3 - (optima.log: fine-lattice floor optima)
m=30 stage-2 fine-lattice deepest peak cav floor: lo 0.7675 -10.865 (slot-mode there -13.08)
   cell-1 fine-lattice deepest peak cav floor: lo 0.5775 -20.140 -> stage degradation -9.28 dB
m=28 stage-2 fine-lattice deepest peak cav floor: lo 0.7925 -10.079 (slot-mode there -12.17)
   cell-1 fine-lattice deepest peak cav floor: lo 0.59 -19.139 -> stage degradation -9.06 dB

$ PYTHONDONTWRITEBYTECODE=1 python3 phase2.py   (c2c: passive cell 2 driven by the stored active cell-1 series)
M0 done 1728000 54.4 s
$ python3 - (score3.log)
[rule 2.625 rt] c2c (cell 2 active over cell 2 passive, same upstream input): worst 4.7981 mean 5.0301; upstream cell 1 seen through passive cell 2: worst 8.2696 mean 8.3686; sum of means 13.3987
[unshifted] c2c (cell 2 active over cell 2 passive, same upstream input): worst 4.6488 mean 5.0025; upstream cell 1 seen through passive cell 2: worst 8.0616 mean 8.1363; sum of means 13.1388

$ PYTHONDONTWRITEBYTECODE=1 python3 score2.py   (latency ladder; ablation row iii)
P_m30_N240: passive crest lag median 0.5250 rt [0.5250, 0.5250] (excess over L/s = 0.5 rt: 0.0250); envelope lag 2.5464 rt; passive transfer 15.830 dB; dt 1.389e-03
P_m28_N240: passive crest lag median 0.5236 rt [0.5236, 0.5236] (excess over L/s = 0.5 rt: 0.0236); envelope lag 2.5374 rt; passive transfer 15.812 dB; dt 1.389e-03
P_m30_N480: passive crest lag median 0.5226 rt [0.5222, 0.5226] (excess over L/s = 0.5 rt: 0.0226); envelope lag 2.6150 rt; passive transfer 16.233 dB; dt 6.944e-04
P_m30_N720: passive crest lag median 0.5220 rt [0.5218, 0.5220] (excess over L/s = 0.5 rt: 0.0220); envelope lag 2.6414 rt; passive transfer 16.371 dB; dt 4.630e-04
ablation (iii) [gate (i) raised-cosine '0' cut + hard '1' cut at 0.8 repT], rule window 2.625 rt: floor cav -13.088 drn_h -12.640 slot-mode -16.822; chain worst 13.131; eye 12.804 (n 36)
   (cell 1 in that run, unchanged by the gate: Gw 8.287855791924049)

$ PYTHONDONTWRITEBYTECODE=1 python3 latency.py   (four estimators)
P_m30_N240: passive stage-1->2 delay (rt): E1 signed crest 0.5250 | E2 lock-in phase 0.5215 | E3 signed xcorr 0.5238 | E4 |x| per-slot peak (mod 1 rt) 0.5250 | one step = 0.00069 rt
P_m28_N240: passive stage-1->2 delay (rt): E1 signed crest 0.5236 | E2 lock-in phase 0.5293 | E3 signed xcorr 0.5284 | E4 |x| per-slot peak (mod 1 rt) 0.5236 | one step = 0.00069 rt
P_m30_N480: passive stage-1->2 delay (rt): E1 signed crest 0.5226 | E2 lock-in phase 0.5179 | E3 signed xcorr 0.5202 | E4 |x| per-slot peak (mod 1 rt) 0.5226 | one step = 0.00035 rt
P_m30_N720: passive stage-1->2 delay (rt): E1 signed crest 0.5220 | E2 lock-in phase 0.5167 | E3 signed xcorr 0.5189 | E4 |x| per-slot peak (mod 1 rt) 0.5220 | one step = 0.00023 rt

$ python3 - (residue.log: registered residue key)
m=30: after-'1' '0' slots n=8; first-quarter max over (a) -5.698 dB; whole-slot max over (a) -5.698 dB; argmax positions [np.float64(0.0084), np.float64(0.009)]
m=28: after-'1' '0' slots n=8; first-quarter max over (a) -5.308 dB; whole-slot max over (a) -5.308 dB; argmax positions [np.float64(0.0158), np.float64(0.0159), np.float64(0.0166), np.float64(0.0167)]

$ PYTHONDONTWRITEBYTECODE=1 python3 phase3.py   (J = −3 and J = 0 two-cell chains, m = 30/28, N = 240)
done ('P_m28_N240_J-3', 1612800, 0.001388888888888889, 91.6) [92s]
done ('P_m30_N240_J-3', 1728000, 0.001388888888888889, 98.0) [98s]
done ('A_m28_N240_J-3', 1771741, 0.0012642926038760258, 102.7) [103s]
done ('A_m30_N240_J-3', 1898294, 0.0012642926038760258, 106.7) [107s]
done ('P_m30_N240_J0', 1728000, 0.001388888888888889, 97.6) [196s]
done ('P_m28_N240_J0', 1612800, 0.001388888888888889, 91.7) [198s]
done ('A_m30_N240_J0', 1898294, 0.0012642926038760258, 107.5) [199s]
done ('A_m28_N240_J0', 1771741, 0.0012642926038760258, 99.0) [202s]
PHASE3 DONE
$ PYTHONDONTWRITEBYTECODE=1 python3 score4.py
J=-3 m=30: G_single 8.2879; rule window: chain 13.904 G4_A 1.6776; floor cav -4.46 slot-mode -5.93
   peak-cav round-spec placements: 38 (lo 0.7..0.7925), matched G4 1.6694..1.7203, mixed 1.6792..1.7304; with matched G4 >= 1.7: 10 e.g. lo 0.77 matched 1.7156 floor -11.11; with mixed >= 1.7: 23
J=-3 m=28: G_single 8.1315; rule window: chain 13.628 G4_A 1.6759; floor cav -3.67 slot-mode -4.90
   peak-cav round-spec placements: 12 (lo 0.79..0.8175), matched G4 1.7229..1.7897, mixed 1.7550..1.8271; with matched G4 >= 1.7: 12 e.g. lo 0.79 matched 1.7229 floor -10.12; with mixed >= 1.7: 12
J=0 m=30: G_single 8.2879; rule window: chain 12.637 G4_A 1.5247; floor cav -4.78 slot-mode -6.40
   peak-cav round-spec placements: 36 (lo 0.7..0.7875), matched G4 1.5163..1.5678, mixed 1.5252..1.5770; with matched G4 >= 1.7: 0; with mixed >= 1.7: 0
J=0 m=28: G_single 8.1315; rule window: chain 12.511 G4_A 1.5386; floor cav -4.18 slot-mode -5.41
   peak-cav round-spec placements: 0; with matched G4 >= 1.7: 0; with mixed >= 1.7: 0
$ python3 - (score4b.log: J = −3 detail rows)
J=-3 m=30 (G_single at promoted window 8.2879; passive envelope lag of this chain: see below)
   lo 0.7000: chain 13.917 | single@lo-lag 8.337 | matched G4 1.6694 mixed 1.6792 | floor cav -10.04 drn_h -9.91 slot-mode -12.51 | eye 9.72 (n 35)
   lo 0.7400: chain 14.147 | single@lo-lag 8.337 | matched G4 1.6970 mixed 1.7070 | floor cav -10.39 drn_h -10.17 slot-mode -12.97 | eye 10.07 (n 35)
   lo 0.7600: chain 14.147 | single@lo-lag 8.337 | matched G4 1.6970 mixed 1.7070 | floor cav -10.39 drn_h -10.98 slot-mode -13.37 | eye 10.07 (n 35)
   lo 0.7700: chain 14.302 | single@lo-lag 8.337 | matched G4 1.7156 mixed 1.7257 | floor cav -11.11 drn_h -10.98 slot-mode -13.31 | eye 10.79 (n 35)
   lo 0.7800: chain 14.342 | single@lo-lag 8.337 | matched G4 1.7203 mixed 1.7304 | floor cav -11.11 drn_h -10.45 slot-mode -13.60 | eye 10.79 (n 35)
   lo 0.7900: chain 14.342 | single@lo-lag 8.337 | matched G4 1.7203 mixed 1.7304 | floor cav -11.11 drn_h -10.45 slot-mode -13.80 | eye 10.79 (n 35)
   lo 0.7925: chain 14.342 | single@lo-lag 8.337 | matched G4 1.7203 mixed 1.7304 | floor cav -10.07 drn_h -10.45 slot-mode -13.78 | eye 9.75 (n 35)
J=-3 m=28 (G_single at promoted window 8.1315; passive envelope lag of this chain: see below)
   lo 0.7900: chain 14.271 | single@lo-lag 8.283 | matched G4 1.7229 mixed 1.7550 | floor cav -10.12 drn_h -10.21 slot-mode -12.35 | eye 9.79 (n 35)
   lo 0.7950: chain 14.293 | single@lo-lag 8.284 | matched G4 1.7253 mixed 1.7577 | floor cav -10.34 drn_h -10.21 slot-mode -12.31 | eye 10.01 (n 35)
   lo 0.8000: chain 14.857 | single@lo-lag 8.301 | matched G4 1.7897 mixed 1.8271 | floor cav -10.34 drn_h -10.21 slot-mode -12.36 | eye 10.01 (n 35)
   lo 0.8100: chain 14.857 | single@lo-lag 8.301 | matched G4 1.7897 mixed 1.8271 | floor cav -10.34 drn_h -10.16 slot-mode -12.67 | eye 10.01 (n 35)
   lo 0.8175: chain 14.857 | single@lo-lag 8.301 | matched G4 1.7897 mixed 1.8271 | floor cav -10.34 drn_h -10.16 slot-mode -12.81 | eye 10.01 (n 35)
   lo 0.8200: chain 14.857 | single@lo-lag 8.301 | matched G4 1.7897 mixed 1.8271 | floor cav -9.88 drn_h -10.16 slot-mode -12.81 | eye 9.55 (n 35)
   passive envelope lag J=-3 m=30: 5.0972 units (J=-1 chain: see score.log)
   passive envelope lag J=-3 m=28: 5.0798 units (J=-1 chain: see score.log)

$ PYTHONDONTWRITEBYTECODE=1 python3 phase4.py   (Table 9 row iv)
ablation (iv) [hard '0' zero + hard '1' cut at 0.8 repT], rule window 2.625 rt: floor cav -13.808 drn_h -13.365 slot-mode -17.528; chain worst 13.131; eye 13.524 (n 36) [107s]

$ python3 tdiff.py   (table rows of 11-reply.md against round-4-reply.md plus round-4-tables-appendix.md, grouped by heading; the prose of the §4 grading rows is elided here)
round-1 tables: ['## 4. Grading the record', 'Res', 'T1', 'T2a', 'T2b', 'T3', 'T3b', 'T4', 'T5', 'T6']
round-4 tables: ['## 4. Grading the record', 'Res', 'T1', 'T2a', 'T2b', 'T3', 'T3b', 'T3c', 'T3d', 'T4', 'T5', 'T6', 'T8', 'T9']
T1: rows r1=20 r4=20 rows identical=True; caption identical=True
T2a: rows r1=30 r4=30 rows identical=True; caption identical=True
T2b: rows r1=12 r4=12 rows identical=True; caption identical=False
T3: rows r1=12 r4=12 rows identical=True; caption identical=True
T3b: rows r1=10 r4=10 rows identical=True; caption identical=True
T4: rows r1=18 r4=18 rows identical=True; caption identical=True
T5: rows r1=44 r4=44 rows identical=True; caption identical=False
Res: rows r1=4 r4=4 rows identical=True; caption identical=False
T6: rows r1=13 r4=13 rows identical=True; caption identical=True
## 4. Grading the record: rows r1=7 r4=7 rows identical=False; caption identical=True   [the five grade rows are regraded prose, as the record states]
total round-1 rows compared 170
new in r4: T3c 24 rows / T3d 16 rows / T8 5 rows / T9 7 rows
(Table 1's bracket paragraph below the heading also changed: '[min, max over seeds 7/11/13, each at its own rule placement — the ⅛-rt window-rule envelope, not pattern dependence …]'.)

$ grep -c/-o on round-4-reply.md for stale or withdrawn phrases: '9–10 dB' 0; '7–9' 0; 'upper bound on the loading' 0; '+0.04 to +2.6' 0; '3.2–4.4' 0; '0.523–0.525' 0; '1.43' 0; '0.55–0.89' 0; 'released coupling' 0; 'could build' 0. 'both sides' 3 hits: the disclosure sentence, the residue key (correct) and the discriminant. 'promoted floor key's own' 1 hit, the disclosure. '44 dB', 'half-step', 'every placement', 'byte-identical', 'No measured number': disclosure or correction contexts only. 'this is the round-3 text' 1 hit, line 15 (required edit 5). 'crosses the bar' 1 hit, line 30 (item 6). '1.70' in text: line 25 (item 1c '1.63–1.70'), plus the §4 row and limitation 6. 'CW form' 1 hit, line 303 (the discriminant); item 2 has no CW-form G4.
$ grep -rn 'cascade2_|passive_port_density|zero_slot_residue|cascade_stage_latency|cascade_relaunch' notes/ both results.json papers/ | wc -l
0
$ python3 - (sizes) comments (chars): [42915, 23449, 21695] bytes: [44164, 23649, 22193]; listings+appendix chars 60476 bytes 60585; rework rw*.py listings chars 35472
$ python3 - (diff of the render_tables.py block in 12-listings.md against listings/render_tables.py): 13814 vs 14567 characters. The only differences are four caption/print strings (Table 1 paragraph, Table 2b, residue, Table 5) and the table5() section.
Record reads: notes/INDEX.md; 08-01 gated §4 table (A_fix 0.00763–0.01403; 0.01169 / 0.01335 / 0.01387 / 0.01403 at m = 28/30) and §5 knee 0.01203; 08-02 §4 orders 0.706 / 0.548 / 0.136 / 0.888; 08-12 §3 decay column and §4 line 95 (the regen.loop_gain disagreement); 07-31 §8 listings (make_sig_duty, run_custom, slot_peaks, metrics).
$ cd /home/user/FableComputer && git status --short | wc -l
0
Not re-executed (accepted from three prior rounds, not load-bearing for my findings): Table 2a matched rows other than via c2c, Table 3 stages 3–5, Table 8, the N = 480/720 chains, item 8's drain-velocity slope, seeds 11/13.
```

</details>
