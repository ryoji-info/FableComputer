# Pre-publication verification record — Fable Session 2026-09-28 (paste as the comment before the reply, after the losing candidates)

Two mutually blind check seats, each requested on the Fable model alias (`claude-fable-5-1` in this session; each seat's own model note is reproduced below), re-executed the draft reply with instruments they wrote from the reply's stated definitions before opening the executor's listings, audited every citation against the record, audited prior art against `notes/INDEX.md`, and audited the format against the winning prompt. Their records follow **verbatim** (the structured output each seat returned; nothing edited, nothing omitted), then the executor's adjudication of every defect: what was re-executed, what was changed, and where. Both seats returned **revise**. Every defect reproduced; none was declined.

<details><summary>The check-seat task text (identical for both seats)</summary>

```markdown
You are an independent PRE-PUBLICATION CHECK seat for the Fable Computer Agent Lab (repository checkout: /home/user/FableComputer), requested on the Fable model alias for this run. You share no context with the executor. Your job is adversarial: try to refute the session reply below before it is published. Read these in full first:
1. /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/run-context.md (run context, platform disclosure, thread state).
2. /home/user/FableComputer/notes/INDEX.md, then the promoted notes the reply cites (notes/2026-07-31-…, 2026-08-01-gated-requirement-round-trip, 2026-08-01-ratio-bias-gain-table, 2026-08-02-zero-floor-spec-dissolved §3, 2026-08-12-gated-zero-residual-phasor §1–2, 2026-07-20-loaded-fanout-fixed-point §2, 2026-07-21 §2) as far as the claims you check require.
3. The reply: /home/user/FableComputer/agents/runs/2026-09-28-cloud-eval/stage2-session/11-reply.md. The listings that produced it: /home/user/FableComputer/agents/runs/2026-09-28-cloud-eval/stage2-session/listings/ (cascade_driver.py is the instrument; campaign.py/analyze.py/depth.py/analyze_depth.py/table2.py/render_tables.py the campaign and scoring). The raw campaign outputs are under /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/session/ (runs/*.json, depth/*.npy, table2.jsonl, analysis.json, analysis_depth.json) — you MAY read them to locate what to re-execute, but every number you accept must be one you re-executed yourself with your own script against the released, unedited fable-model-chain/.

Platform: this container is Linux x86_64 / Python 3.11.15 / numpy 2.4.6; the record's values reproduce to ~1e-13–1e-16 relative, never bit-equal; gate on a stated tolerance. Never modify a tracked file; never run run_all.py inside the repo tree; work under /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/CHECK_ID/ (create it). Runs at N = 240 cost ~50 s each, so budget: re-execute the DECISIVE rows (not the whole campaign) — at least: (a) the gate row (cell 1 alone, m = 30, N = 240, ratio bias, must reproduce 8.287855791924017 / −11.828336851447219 to ≤1e-9); (b) one two-cell chain row at J = −1 (m = 30, N = 240, seed 7): rebuild the coupling from the reply's stated definition (cell 2's source clamp = 1 + κ·(h1[−1] − 1) at the same step, released _setup/_step_LF stepping) WITHOUT reading cascade_driver.py's implementation first, and reproduce the chain-over-passive gain, the cell-to-cell gain, the passive port transfer (+15.8 dB) and the stage-2 floors under the reply's stated window rule; (c) one matched-amplitude single-cell row (Table 2a); (d) one junction-sweep row (Table 4) if time permits.

Then audit, and record evidence for each item:
A. Every number and every "demonstrated" claim in the executive verdict and Tables 1–5: re-executed or, where you could not (say so), cross-checked for internal consistency (e.g. G4 = 1 + c2c/G1 within the worst-vs-mean caveat; chain gain = c2c + upstream-through-passive). A number that does not reproduce is a blocking defect; state the deviation.
B. Every promoted note and manuscript passage the reply cites says what the reply says it says (mis-citation is blocking). Check the reply against notes/INDEX.md for any premise the record has corrected and for re-announcing what the record already carries (the prior-art rule).
C. Epistemic labels: demonstrated only for executed numbers; in-model with model and assumptions named; open where open. A code-semantics reading labelled demonstrated is a defect. "Bit-equal" must not appear unless exact equality was measured.
D. The coupling design (§2): is it defended, not assumed? Are the ledger terms booked once? Is the definition of G4 the one Part I uses ("over the passive chain"; passive twins)? Is the alternative plane priced? Is anything from discussion #124 cited as settled?
E. The window rule: fixed before scoring, applied identically to active and passive chains, with its sensitivity stated? Any per-stage tuning?
F. The grading table: does each grade follow from the measurements? Are the registered keys new names (grep both results.json files and notes/ for collisions), each with a band and a falsifier, bench discriminants labelled one- or two-sided, and no existing key's name reused?
G. Format: executive verdict ≤ 8 items each labelled; Tables 1–3 as the prompt specified; limitations; platform/model line; word count.

Return the structured output: verdict (clear / revise), the defect list (claim quoted; what you measured, verbatim; severity blocking/minor; the fix), your re-execution log (every command and printed output), citation audit, prior-art audit, and your seat model note (the model this seat was requested on, as told to you; do not guess beyond that).
```

</details>

## Check seat 1 — verdict: **revise**

*Seat model note (the seat's own words):* This seat (check1) was requested on the Fable model alias for this run, as stated in the task; the session names it claude-fable-5-1. No further inference about the served model is made. Platform for every number above: Linux x86_64, Python 3.11.15, numpy 2.4.6.

### Defects

**check1-1 — blocking.**

- *Claim:* Registered key `zero_slot_residue_unwindowed_dB` = −1.57 (m = 30): "the peak of cell 1's active drain density in the first quarter of a '0' slot that follows a '1', over the mean-'1' windowed peak; whole-slot −5.70"; band [−2.5, −0.5]. Same numbers in executive item 4 ("−1.6 dB (m = 30) … in the slot's first quarter and −5.7 … over the whole slot") and the residue table.
- *Measured:* My run (seat_driver, cell 1 active, m = 30, N = 240, seed 7, ratio bias 0.11826023624361658): mean-'1' windowed drn_h peak 0.03396500068703142; after-'1' '0'-slot first-quarter peak max 0.01762482648518382 → −5.698 dB over the windowed mean-'1'; whole-slot −5.70 dB (the whole-slot maximum sits in the first quarter, as ring-down requires). The −1.57 is reproduced only as the first-quarter '0' peak over the mean-'1' FIRST-QUARTER peak (0.02112298068773024): −1.5726 dB. As printed the key is internally impossible: a sub-interval maximum cannot exceed the whole-slot maximum by 4.1 dB with the same denominator.
- *Fix proposed:* Either (a) keep −1.57 and its band and redefine the key's denominator as the mean-'1' first-quarter peak (a same-phase-of-slot ratio), or (b) keep the stated denominator and register −5.70 (= the whole-slot value) with a new band. Restate executive item 4 and the residue table with the denominator named in each cell.

**check1-2 — blocking.**

- *Claim:* §2 / Table 3 caption / limitation 6: "window rule shift = (k − 1) × the exact passive-chain envelope lag"; Table 3 sensitivity row "active-lag 5.40 / 5.04"; executive item 7 "with the active lag instead, the stage-2 floor reads −5.7 / −6.3 dB".
- *Measured:* listings/analyze_depth.py applies `sh = min(sh, 0.9*repT − 0.72*repT)`, i.e. every Table 3 shift is capped at 0.18·repT = 10.8 units (5.40 rt) at m = 30 and 10.08 units (5.04 rt) at m = 28. Consequences: Table 3 stages 4–5 at both rungs (rule would be 7.70 / 10.27 rt at m = 30, 7.67 / 10.22 rt at m = 28) and stage 3 at m = 28 (rule 5.11 rt, printed 5.04) are scored at the cap, not at (k − 1)×lag; the "active-lag" row is the cap, not the active lag (the reply's own measured active envelope lag is 5.71 / 5.77 rt; my estimate 5.66 rt); item 7's active-lag floor is therefore at a capped shift. The cap is disclosed nowhere in the reply. (Stage-2 rule rows are unaffected and reproduce: 13.000 / 4.704 / −4.64 / −4.31 / −6.21 / 0.853 / +4.29 at the exact 2.568-rt shift.)
- *Fix proposed:* State the cap (window end ≤ 0.90·repT ⇒ shift ≤ 0.18·repT) in §2 and the Table 3 caption, mark the capped cells, relabel the sensitivity row "capped 5.40 / 5.04 rt (active lag 5.71 / 5.77 exceeds the cap)", and correct item 7 — or re-score stages ≥ 3 with a window that can carry the full (k − 1)×lag and disclose the slot overrun.

**check1-3 — blocking.**

- *Claim:* Executive item 4: "at stage 2 the floor is −4.0 to −4.8 dB (per-slot peak, cav/drn_h) and −5.2 to −6.4 dB (08-12's slot-mode drn_h) at J = 0…−6 dB".
- *Measured:* The reply's own Table 5 at J = 0…−6: peak cav −3.21 (m = 28, J = −6, seed 7) … −4.82; peak drn_h −3.66 … −4.51; slot-mode −4.43 (m = 28, seed 11, J = −6) … −6.40. My re-execution of the m = 30 / J = −1 cell: −4.696 / −4.307 / −6.257, inside Table 5, so the table is right and the summary range is wrong by up to 0.8 dB at the shallow end. The fail verdict is unchanged.
- *Fix proposed:* Restate as "−3.2 to −4.8 dB (peak cav), −3.7 to −4.5 (peak drn_h), −4.4 to −6.4 (slot-mode)" and recompute the "5–9 dB fail" span from those bounds.

**check1-4 — minor.**

- *Claim:* Executive item 7: the window rule "moves the two-cell gain by +0.2 to +0.5 dB and the stage-2 floor by −0.9 to −1.7 dB relative to the unshifted window (Table 1, last column; Table 3's sensitivity rows)".
- *Measured:* From Table 1 itself (shifted − unshifted chain worst): +0.19 (m = 28, N = 480, J = 0) to +0.67 (m = 30, N = 240, J = −6). My J = −1 row: 13.1033 − 12.7344 = +0.369; my J = −25 row: +0.533. Floors: Table 3 sensitivity gives −1.08 / −1.10 only; my rows give −1.13 (J = −1) and −1.78 (J = −25); the executor's own analysis.json spans −1.00 to −1.98 over all classes. Neither printed range is supported.
- *Fix proposed:* Restate as +0.2 to +0.7 dB (Table 1 classes) and −1.0 to −2.0 dB (or −1.1 at J = −1), citing the rows that set each bound.

**check1-5 — minor.**

- *Claim:* Executive item 3: "the cell-to-cell gain is 3.5–4.1 dB lower (Table 1's c2c column vs its G_single column)".
- *Measured:* Table 1 has no c2c column; the cell-to-cell values are in Tables 2a and 4. The range itself checks (8.2879 − 4.798 = 3.49; 8.4681 − 4.414 = 4.05; my c2c worst 4.7986 at J = −1).
- *Fix proposed:* Cite Tables 2a/4 for the c2c column.

**check1-6 — minor.**

- *Claim:* Executive item 6 (headed *Demonstrated*): "`cell.cascade_per_cell_gain_dB` evaluates the compression at `A_op`·κ, a source-plane swing 0.0116κ, which presupposes a link that returns the swing to source-plane scale; the released solver has no such link, and this session found none."
- *Measured:* cell.py line `swing = A_op * 10 ** (J / 20)` confirms the code read; the "presupposes a link" clause is an interpretation of the ledger, not an executed observable, and sits under a demonstrated label.
- *Fix proposed:* Label the sentence in-model (code read + interpretation) inside item 6.

**check1-7 — minor.**

- *Claim:* Executive item 1: G4 at N = 240 with "seed spread ≤ 0.03".
- *Measured:* Table 1, m = 30 / N = 240 / J = −6: G4_A worst [1.756, 1.789] → spread 0.033.
- *Fix proposed:* Write "≤ 0.04" or "≤ 0.033".

**check1-8 — minor.**

- *Claim:* §1/§2: the window rule is "the passive-chain latency … envelope cross-correlation", stated without the estimator; Table 6 gives 2.568 rt (m = 30, N = 240).
- *Measured:* The estimator (moving mean over one carrier period on the ~20,000-sample downsampled |drn_h| series, lag search ≤ 6 rt) exists only in listings/analyze.py. My independent estimator (FFT analytic-signal envelope, 0.01-rt resolution) returns 2.540 rt for the same passive stage, which rounds to 2.5 rt on the ⅛-rt grid, not 2.625; at 2.5 rt the J = −1 chain worst reads ≈ 13.00 (G4 1.569) instead of 13.103 (1.581). Per-slot peak-time lag reproduces exactly (0.5243 rt vs 0.525).
- *Fix proposed:* State the envelope estimator and its grid-rounding sensitivity (≈ 0.1 dB, 0.012 in G4) in §2 or limitation 6, so the 2.625-rt shift is reproducible from the text.

**check1-9 — minor.**

- *Claim:* §2 "The coupling": junction classes taken from "Part I's junction transmissions" / "(Part I §9.4)" only.
- *Measured:* The winning prompt attributes "the junction classes are a budget, not a derivation" to Part I §9.4 AND Quanta ⚛️'s 2026-09-28 lab post (stage1-posts/quanta.md: "Open: the −1 to −3 dB band itself, which is Part I's budget rather than a derivation"; reflection budget |r|² ≤ 11.6 %). The reply never names Quanta or that post.
- *Fix proposed:* Credit ⚛️ Quanta's 2026-09-28 post (standing rule 5) where the junction budget and the ideal-isolation assumption are introduced.

**check1-10 — minor.**

- *Claim:* Prompt deliverable Table 3: "'0'-floor (both denominations), '1' pp and latency per stage".
- *Measured:* Latency is measured for stages 1–2 only (Table 6, text after Table 3); Table 3 carries the window shift, not a per-stage latency, for stages 3–5.
- *Fix proposed:* Add the measured (or capped) per-stage latency column for stages 3–5, or state that it was not measured beyond stage 2.

**check1-11 — minor.**

- *Claim:* Executive item 2: cell 2's clamp swing 0.017–0.036 is "1.5–3.1× the ledger's `A_op` = 0.0116"; grading table G4 row: "the bar is failed at −1/−3 dB".
- *Measured:* 0.01651 / 0.0116 = 1.42 (Table 2a m = 28 J = −6), so 1.4–3.1×; item 1 and Table 1 fail the ≥ 1.7× bar at 0 dB too (1.525 / 1.539).
- *Fix proposed:* "1.4–3.1×"; "failed at 0 / −1 / −3 dB".

### Re-execution log (verbatim)

```text
Seat directory: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/check1/ (seat_driver.py, batch1.py, batch2.py, score.py, residue_diag.py, batch3.py; outputs batch1.out, batch2.out, score.out, batch3.out; series *.npz). Released fable-model-chain/ imported unedited (PYTHONDONTWRITEBYTECODE=1); git status clean throughout. The instrument was written from the reply's stated definition before cascade_driver.py was opened; cascade_driver.py/depth.py/analyze*.py were read afterwards only for the window-rule audit.

$ python3 -c "import sys,numpy,platform;print(sys.version, numpy.__version__, platform.machine())"; nproc
3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0] 2.4.6 x86_64
4

$ PYTHONDONTWRITEBYTECODE=1 python3 batch1.py
M_th_num(240) = 0.16894319463373797  shipped 0.16894319463373791  rel dev 3.285787944971905e-16 [30s]
bias 0.7*M_th_num(240) = 0.11826023624361658
done ('c1_0', 1728000, 0.001388888888888889, 71.0s); ('match_0', 1728000, ..., 72.5s); ('match_M', 1898294, 0.0012642926038760258, 76.0s); ('c1_M', 1898294, 0.0012642926038760258, 76.3s)
GATE cav: G_worst1 8.287855791924049, G_mean1 8.410165254217045, pp 0.30577762777571854, mean1 0.03267155023359718, max0 0.008370528882036612, eye 11.705114659586407, max0_below_mean1 -11.828336851446547
GATE drn_h: G_worst1 8.663537342727865, G_mean1 8.769558457037114, pp 0.2653510968361314, mean1 0.03396500068703142, eye 11.668429556367615, max0_below_mean1 -11.775002445228234
rel dev gain 3.857984973672145e-15 floor cav 5.676731172997833e-14 floor drn_h 1.3230272820754644e-13   [targets 8.287855791924017 / -11.828336851447219 / -11.775002445226676: all ≤ 1e-9, gate PASSED]
passive port density transfer = 15.8296 dB (mean-'1' drn_h passive 0.012374); active cell-1 mean-'1' drn_h = 0.033965 (24.600 dB over launch)  [reply: 15.83; 0.01237; 0.03397; relaunch −24.6 dB]
MATCHED A*=0.03027 boundary-driven cav: G_worst1 4.797421624399798, G_mean1 4.929497472481481, pp 0.3375, floor -13.083  [reply Table 2a m30/N240/s7/J=-1: 4.797 / 4.929]
platform: Linux x86_64 / Python 3.11.15 / numpy 2.4.6 [108s total]

$ PYTHONDONTWRITEBYTECODE=1 python3 batch2.py   (cell 2 clamp = 1 + κ·(h1[-1]-1), κ=10^(J/20), np.interp on cell 1's released-labelled series; 'prev' variant couples from cell 1's state before its step)
done J-1_M0 (1728000 steps, 56.0s); J-1_00 (59.0s); J-1_MM (1898294 steps, 67.7s); J-25_MM (70.2s); J-25_M0 (73.8s); J-25_00 (73.8s); J-1_MM_prev (72.0s) [140s total]

$ PYTHONDONTWRITEBYTECODE=1 python3 score.py
cell 1: G_worst1 8.287856 G_mean1 8.410165; mean-'1' drn_h 0.033965; abs single gain over launch 24.600 dB
J=-1 shift 0.000 rt: chain_worst 12.7344 mean 13.1388; c2c 4.6488/5.0025; thru 8.0616/8.1363; G4A 1.5365/1.5622; G4A_drnh 1.4862; G4B 1.7882; floor cav -3.5615 drnh -3.0874 mode -4.0993; pp 0.9968; eye 3.1481   [reply Table 1 unshifted 12.734; Table 3 sens. -3.56 / +3.15]
J=-1 shift 2.568 rt: chain 12.9998/13.3371; c2c 4.7038/4.9685; thru 8.2696/8.3686; G4A 1.5685/1.5858; G4A_drnh 1.5498; G4B 1.8039; mean1_drn_MM 0.331; floor cav -4.6365 drnh -4.3074 mode -6.2141; pp 0.8535; eye 4.2919   [reply Table 3 stage 2: 13.000/13.337; 4.704/4.969; -4.64/-4.31; -6.21; 0.853; +4.29; 0.3310]
J=-1 shift 2.625 rt: chain 13.1033/13.399; c2c 4.7986/5.0303; thru 8.2696/8.3686; G4A 1.581/1.5932; G4A_drnh 1.5498; G4B 1.8039; floor cav -4.6961 drnh -4.3074 mode -6.257; pp 0.7499; eye 4.3954   [reply Table 1: 13.103/1.581/1.593/1.550/1.804; Table 2a/4: 4.798/5.030; Table 5: -4.70/-4.31/-6.26/0.750/+4.39; §3 consistency 8.369+5.030=13.399, 8.270+4.798]
J=-25 shift 0.000 rt: chain 15.6994/15.8407; c2c 7.3141/7.4705; G4A 1.8943; floor cav -1.9427; eye 1.8036
J=-25 shift 2.625 rt: chain 16.232/16.5033; c2c 7.7586/7.9365; G4A 1.9585/1.9623; G4A_drnh 1.9169; floor cav -3.7185 drnh -4.0105 mode -5.273; pp 0.6741; eye 3.4452   [reply Table 4/5 m30 J=-25: 7.757/7.935; 1.958/1.962; -3.72/-4.01/-5.27; 0.676; +3.44]
coupling-step sensitivity (J=-1 MM from cell 1's previous step, shift 2.625): chain 13.1028/13.3987; c2c 4.7981/5.0301; floor cav -4.6958; eye 4.3949   [≤ 0.0005 dB from the same-step variant; cascade_driver.py uses this 'previous state' convention]
envelope lag (FFT analytic-signal envelope, 0.01-rt grid): launch->passive cell-1 drain 2.150 rt; passive stage 2 (c1_0 drain -> 00 drain) 2.540 rt; launch->active cell-1 5.530 rt; active stage 2 (c1_M -> MM) 5.660 rt   [reply: 2.568 / 5.704 with its moving-mean estimator]
per-slot peak-time lag, passive stage 2, '1' slots: median 0.5243 rt (min = max = 0.5243)   [reply 0.525]
residue m=30 after-'1' '0' slots (n=8): windowed peak -11.78 dB; first-quarter peak -5.70 dB; whole-slot -5.70 dB; energy max/median(after-'1') -10.6 / -10.6 dB   [reply: -11.78; -1.57 (!); -5.70; -10.6 / -13.8]

$ PYTHONDONTWRITEBYTECODE=1 python3 residue_diag.py
mean-'1' windowed 0.03396500068703142 first-quarter 0.02112298068773024 whole 0.03396500068703142
after-'1' zero first-quarter peak max 0.01762482648518382 over mean1_win -5.698135552334909 over mean1_q1 -1.5726070375520012   [→ the reply's -1.57 is the first-quarter '0' peak over the first-quarter mean-'1' peak, not over the windowed mean-'1' peak as its key states]

$ PYTHONDONTWRITEBYTECODE=1 python3 batch3.py   (item 8, velocity plane: cell 2 clamp = 1 + κ·(u1[-1]-u0), J=-1)
['c1u_0', 'c1u_M'] [53s]
velocity plane: passive cell-1 mean-'1' drain velocity 0.000081 -> transfer -27.87 dB over launch; active 0.004065; cell 2 receives (J=-1) 0.00362   [reply: -28 dB; 0.0036]
['Ju-1_M0', 'Ju-1_00', 'Ju-1_MM'] [107s]
velocity-plane J=-1 shift 2.625 rt: chain worst 41.242 mean 41.523 (over the velocity passive twin chain; G4 in that definition 4.976, not printed by the reply); c2c worst 7.554 mean 7.742; stage-2 floor cav -3.69 eye +3.41   [reply: c2c 7.55–7.63 worst; floor -3.6 to -3.7]
[109s total]

Cross-checks by arithmetic on the reply's own tables (not re-executed): G4 ≈ 1 + c2c/G1 at J=-1: 1 + 4.798/8.2879 = 1.579 vs 1.581 (inside the worst-vs-mean caveat); first-order (480,720) extrapolant 3·1.711 − 2·1.732 = 1.669 → 1.67; −6 dB margins 0.089/0.032/0.011; relaunch attenuations 20log10(0.03397/0.002)=24.60, (0.03295)=24.34, (0.03573)=25.04, (0.03456)=24.75; loop model 1/(1−0.7451522890452021)=3.924 → 11.87 dB, +6.02 → 17.9 dB; 08-12 peak/mode gap 3.83/3.89; slot fractions 2.625/30=0.0875, 2.625/28=0.094, 2.5/28=0.089; 1 rt = 0.5 ps. Executor listings in 12-listings.md verified byte-identical to listings/*.py (10 blocks). Reply: 8,248 words, 44,273 characters (< 60,000). Not re-executed: Tables 1/2a/4/5/6 rows other than m=30/N=240/seed 7 at J=-1, J=-25 and the matched A*=0.03027 row; Table 2b; Table 3 stages 3–5; N=480/720 and seeds 11/13; the ranges in items 1–2 were checked against the printed tables only.
```

### Citation audit

Checked against the cited text, all as the reply says unless noted. Part I §7.4 (papers/Fable-Computer-Part-I.docx): "two-cell total ~+17–19 dB over the passive chain, computed as twice the per-cell figure", "+8.4 to +9.3 dB net per cell", "the per-cell figure is defined at the junction-attenuated swing", "the direct two-cell time-domain test is open work" — quoted correctly. Table 6 cascadability row "in-model yes: 2 cells, +8.4–9.3 dB/cell through −6 dB junctions" — correct (the reply calls it the §7.4 row; it is Table 6, minor). Table 7 G4: "two cascaded cells, one junction; ≥ 1.7× the single-cell decibel gain; ≈ 2×" — correct; "passive twins for differential measurement" — correct (die-plan paragraph after Table 7). §9.4 "the −1 to −3 dB budgeted per junction" — correct. cell.py: cascade_per_cell_gain_dB(A_op=0.0116), swing = A_op·10^(J/20), G_CW + compression_dB(swing); results.json cascade_per_cell_dB 8.40/8.63/8.98/9.31 — correct. 08-01 gated-requirement §4: the load-bearing assumption is quoted verbatim ("that the source-boundary-driven single-cell G_worst1(A) this harness measures equals the cell-to-cell gain of a real cascade — i.e. that an upstream cell presents the same duty-0.8 waveform the drive boundary does"); "no re-launch inside that depth" is §4's stated assumption — correct. 08-01 §5 knee 0.01203/0.01208 → reply's "0.0120" — correct. 08-01 ratio-bias §1/§3: rows 8.2879/−11.83 (m30 N240), 8.1315/−10.73, 8.4681/−11.46, 8.2586/−10.40, 8.5316/−11.32 (N=720) and M_th_num(480)=0.1587475408418196, M_th_num_N720=0.15556838465677247 — all match the reply's §1 gate list; "08-01 ratio-bias measured +0.6 to +1.2 dB between conventions" (limitation 3) — the note's ΔG column spans +0.43 to +1.19, so the lower edge is understated (+0.4), trivial. 08-02 §3.1/§3.2: drain = density antinode, source = velocity antinode (argmax indices 239 / 8); drn_h = |h[−1]−1|; rows 8.287855791924017 / −11.828336851447219 / −11.775002445226676 (gate 2 as 08-12 §1 lists them, full precision) — correct; 08-02 §8 shadow-driver pattern — correct. 08-12 §1 gates and §2 denomination: peak-vs-slot-mode gap 3.83 (cav_u) / 3.89 (drn_h), slot-mode lock-in over the [0.25, 0.72] window with the active-envelope carrier reference, decay −24.4 dB/slot (reply's "≈ 24 dB/slot ring-down") — correct. 07-31 §2/§8: duty 0.8, raised-cosine 2-rt edges, active-envelope carrier reference, seed-7 40-slot PRBS drop 4, window [0.25, 0.72]·repT, drive 2×10⁻³, worst-'1' statistic, exp_duty.make_sig_duty logic — the reply's launch is that listing verbatim (my copy of it reproduces the promoted row to 4×10⁻¹⁵). 07-20 §2 / 07-21 §2: F = 2 split −3.01 dB, per_gate_loss 2.555 dB, −0.95 dB bulk term of 07-13 (band [−1.5, −0.3]) — the reply's ledger-term list matches. 08-01-bench-gate-g1 §2(v): bench bias 0.7 × the device's own measured threshold; model side 0.7·M_th_num(N) — the reply's bench discriminant uses exactly this — correct. 08-06 limitation 1 "monoculture" — as the INDEX row summarises it. Discussion #124 cited only as "unpromoted, not re-run and not cited as settled" — compliant with the run context. One mis-citation of the reply's own tables: item 3 refers to "Table 1's c2c column", which does not exist (Tables 2a/4).

### Prior-art audit

INDEX-corrected premises: none violated. The reply builds on the ratio-bias convention (08-01 ratio-bias / bench-gate-g1), not 07-31's analytic bias; it does not move f_max_F2_gated_GHz (08-01/08-02 left it unmoved) and says so; it treats the '0'-floor spec as an open import (08-02) and reports both readings; it uses 08-12's slot-mode denomination beside the peak, never mixed; it does not re-announce 08-02's plane finding (drain = density antinode) but cites §3.1 for it; the 3.83/3.89 dB peak/mode gap is presented as a reproduction of 08-12, not new. It does not re-run or cite #124 as settled. The 08-06 record-length/fit caveat on M_th_num is not contradicted (the reply uses the released bracket as the ratio-bias notes do). Nothing in the reply contradicts a ⛔/⚠️ entry in notes/INDEX.md. Prior art not credited: the winning prompt names Quanta ⚛️'s 2026-09-28 lab post beside Part I §9.4 for "the junction classes are a budget, not a derivation" (that post: "Open: the −1 to −3 dB band itself, which is Part I's budget rather than a derivation", and a reflection budget |r|² ≤ 11.6 % per junction, its 09-02 isolation scout); the reply names neither Quanta nor the post (minor, standing rule 5). The 2026-09-02 posts' scouts (passive propagation length, elasticity register, inter-cell isolation) are not repeated as this reply's own; the reply's "unidirectional, ideal isolation" assumption is the point Quanta's isolation scout raised and could be cited there. The registered key names (cascade2_G4_worst1_ratio_J1, cascade2_G4_worst1_ratio_J6, cascade2_G4_smallsignal_limit, passive_port_density_transfer_dB, cascade2_cell2_gain_worst1_J1_dB, cascade2_zero_floor_J1_dB, zero_slot_residue_unwindowed_dB, cascade_stage_latency_rt, cascade_relaunch_junction_dB) were grepped against fable-model-chain/results.json, fable-model-quantum/results.json, notes/*.md and papers/*.md: no collisions. Each carries a band; the solver-side falsifier is a single generic clause (same-convention rerun outside the band, window-scoped), which is acceptable but weak on a deterministic chain (08-12's assessors required a non-vacuous bench falsifier for the same reason); the bench discriminant is labelled two-sided, per 08-01-bench-gate-g1's convention, not a firing falsifier — compliant.

### Format audit

Executive verdict: 8 items, each labelled (Demonstrated ×6 with in-model sub-clauses, In-model over demonstrated rows ×1, Demonstrated ×1) — compliant with the ≤ 8 limit; item 6 carries an unlabelled code-semantics/interpretation clause under a demonstrated head (minor defect). Table 1: G4 in the defended definition A and the other (B), against junction class × rung × grid, with seed envelopes — as the prompt specified. Table 2 (2a + 2b): cell-to-cell vs boundary-driven at matched amplitude with signed Δ — as specified. Table 3: '0'-floor in both denominations, '1' pp, eye, per stage to depth 5 with the regime breach stated — as specified except that the prompt's "latency per stage" is delivered only for stages 1–2 (Table 6/text), and the window-rule caption misstates the rule actually applied at stages ≥ 3 (blocking defect 2). Grading table: all five targets graded (qualified / qualified (scope) / contradicted / contradicted / qualified (scope)) with reasons. Registered keys: new names, bands, falsifier clause, bench discriminant labelled two-sided. Limitations and open items (9), runnable-listing pointer (sources verified byte-identical to listings/), platform line (Linux x86_64 / Python 3.11.15 / numpy 2.4.6) and model disclosure (claude-fable-5-1 executor; claude-opus-5-5 seats) present. "Bit-equal" appears only in negation ("not claimed anywhere", "not bit-equal"); every reproduction states a relative deviation; the N = 480 threshold is called "exact", which matches the digit-identical value in mth_num.json. Length: 8,248 words / 44,273 characters, under the 60,000-character comment split. Both floor readings (round ≥ 10 dB, strict 11.82 dB) reported; both denominations reported and never mixed; three seeds at N = 240; ladder 240/480 with 720 where the −6 dB verdict turned — compliant with constraints 2 and 6.

## Check seat 2 — verdict: **revise**

*Seat model note (the seat's own words):* This seat (check2) was requested on the Fable model alias for this run, as stated in the task text; the runtime in which it executed identifies itself as claude-fable-5-1 (Fable 5.1). No further inference about the served model is made.

### Defects

**check2-1 — blocking.**

- *Claim:* §5 registered key `zero_slot_residue_unwindowed_dB` = −1.57 (m = 30) / −0.98 (m = 28): "the peak of cell 1's active drain density in the first quarter of a '0' slot that follows a '1', over the mean-'1' windowed peak; whole-slot −5.70 / −5.51 … Band [−2.5, −0.5]"; verdict item 4: "carries the previous '1's ring-down at −1.6 dB (m = 30) … in the slot's first quarter and −5.7 … over the whole slot"; residue table column "first quarter of the slot [0, 0.25]·repT: −1.57 dB (after a '1'); −25.9 (after a '0')".
- *Measured:* Own instrument, m = 30 / N = 240 / seed 7, cell 1 active drn_h (h[-1]−1): mean-'1' windowed peak 0.033965; max over first quarter [0, 0.25]·repT of '0' slots after a '1' = 0.017625 → 20·log10 = −5.698 dB over the windowed mean-'1' peak (identical to the whole-slot value −5.698, because the '0'-slot maximum sits at 0.008–0.009 slot). −1.5726 dB is obtained only when the denominator is the mean-'1' peak taken in the SAME first-quarter window (0.021123 — the '1' still ringing up), a denominator the reply never states; likewise −25.94 (after a '0') vs −30.07 over the windowed mean-'1'. The stated definition therefore reproduces at −5.70, outside the registered band [−2.5, −0.5]; the table's first-quarter (−1.57) and whole-slot (−5.70) columns use different denominators (a first-quarter maximum cannot exceed the whole-slot maximum under one denominator). No shipped listing computes the residue table (grep 'quarter|resid' over listings/*.py: none), against prompt constraint 7. Energy column −10.56 / −13.83 dB reproduces.
- *Fix proposed:* Either register the key under its stated definition (−5.70 / −5.51 over the windowed mean-'1' peak, band re-set, e.g. [−7, −4.5]) or state the first-quarter-mean-'1' denominator explicitly in the key, the table header and item 4, and drop the "−1.6 dB … and −5.7 dB over the whole slot" contrast, which is a change of denominator, not of window. Ship the listing that produced the residue table.

**check2-2 — blocking.**

- *Claim:* Verdict item 4: "at stage 2 the floor is −4.0 to −4.8 dB (per-slot peak, `cav`/`drn_h`) and −5.2 to −6.4 dB (08-12's slot-mode `drn_h`) at J = 0…−6 dB, and still −2.9 to −3.8 dB (peak) at J = −25 dB".
- *Measured:* Reply's own Table 5 at J = 0…−6: peak `cav` spans −4.82 … −3.21 (m = 28 rows: −3.67/−3.21 seed 7, −3.72/−3.24 seed 11, −3.68/−3.22 seed 13, −3.74/−3.23 at N = 480), peak `drn_h` −4.51 … −3.66; slot-mode −6.40 … −4.43 (m = 28 J = −6: −4.51, −4.43, −4.55, −4.52). At J = −25: peak −2.98 (m = 28 `cav`) … −4.01 (m = 30 `drn_h`). My re-execution confirms the m = 30 J = −1 / −6 rows (−4.70/−4.31/−6.26; −4.10/−3.85/−5.51) — the tables are right, the executive-verdict ranges are not. Verdict (fail vs ≥ 10 / 11.82 dB everywhere) unchanged.
- *Fix proposed:* Restate: peak −3.2 to −4.8 dB, slot-mode −4.4 to −6.4 dB at J = 0…−6 dB; −3.0 to −4.0 dB (peak) at J = −25 dB.

**check2-3 — minor.**

- *Claim:* Header, Platform: "three of them (`M_th_num`, `pulse_gain_dB_at_0p7_streaming`, `noise_figure_floor_dB`) only to the last one or two significant digits (relative 1–3×10⁻¹⁶)"; §1: "(720) = 0.15556838465677253 (promoted … 0.15556838465677247; 3.9×10⁻¹⁶)".
- *Measured:* `python3 run_all.py --json` in a scratch copy of fable-model-chain/ vs shipped results.json: M_th_num 3.29e-16, noise_figure_floor_dB 1.60e-16, but pulse_gain_dB_at_0p7_streaming 7.7967069614868425 → 7.796706961486704, relative 1.78e-14 (all 43 other numeric keys equal). M_th_num(720) recomputed = 0.15556838465677253, relative deviation 3.57e-16 (not 3.9e-16). M_th_num(480) exact (= 0.1587475408418196) as the reply states.
- *Fix proposed:* State the measured band as 1.6×10⁻¹⁶ to 1.8×10⁻¹⁴ (pulse gain 1.8×10⁻¹⁴); correct the N = 720 deviation to 3.6×10⁻¹⁶.

**check2-4 — minor.**

- *Claim:* §2 / Table 3 caption: window rule "the promoted [0.25, 0.72]·repT window delayed by (k − 1) × the passive envelope lag"; Table 3 sensitivity rows labelled "active-lag 5.40" (m = 30) / "active-lag 5.04" (m = 28); verdict item 7 "with the *active* lag instead, the stage-2 floor reads −5.7 / −6.3 dB and the eye +5.4 / +6.0 dB"; Limitation 6 "declined as per-stage tuning".
- *Measured:* Table 3 as printed: m = 28 stage 3 shift 5.04 rt (rule gives 2×2.556 = 5.11), stages 4–5 shift 5.40 / 5.04 rt (rule gives 7.7 / 10.3 rt at m = 30, 7.7 / 10.2 at m = 28). listings/analyze_depth.py:44 applies an undisclosed cap `sh = min(sh, 0.9*repT − 0.72*repT)` = 0.18·repT (10.80 units at m = 30, 10.08 at m = 28), and the "active-lag" sensitivity uses the same capped value (analyze_depth.out: "active-lag (shift 10.80)" while "L_active 11.417"), i.e. 5.40 rt, not the measured active lag 5.71 rt. My run at a 5.40-rt shift reproduces the sensitivity row (13.110 / −6.33 / +6.03), so the numbers are right for the shift actually used. Not load-bearing (stages ≥ 3 declared out of regime; sensitivity direction unchanged), but the rule as applied differs from the rule as stated.
- *Fix proposed:* Disclose the 0.18·repT cap in §2 and the Table 3 caption; relabel the sensitivity rows "capped shift 5.40 / 5.04 rt (the maximum window placement inside the slot)" or re-run them at the measured active lag.

**check2-5 — minor.**

- *Claim:* Verdict item 7: the window rule "moves the two-cell gain by +0.2 to +0.5 dB"; key `cascade_stage_latency_rt` "active stage envelope 5.70–5.93" (item 7: "5.70–5.93 rt in all; 2.85–2.97 ps").
- *Measured:* Table 1 shifted − unshifted chain gain: +0.19 (m = 28 N = 480 J = 0) to +0.67 dB (m = 30 N = 240 J = −6: 14.825 − 14.157; also 0.526 at N = 480 and 0.473 at N = 720 for J = −6, 0.527 at N = 240 J = −3). My re-execution: J = −1 +0.369, J = −6 +0.669. Table 6's active envelope lag maximum is 5.841 rt; the 5.93–5.95 rt values exist only in the raw Jext families (analyze_final.out: 11.905 / 11.884 / 11.850 units) that Table 6 omits. Floor sensitivity "−0.9 to −1.7 dB" is supported by the raw unshifted floors (−0.98 … −1.71; my J = −6 row −2.39 → −4.10 = −1.71).
- *Fix proposed:* State +0.2 to +0.7 dB; either add the Jext rows to Table 6 or quote 5.70–5.84 rt for the tabulated rows.

**check2-6 — minor.**

- *Claim:* Verdict item 2: cell 2's gain "4.0–6.4 dB … against the 8.1–8.5 dB the ledger books for it"; item 3: "the cell-to-cell gain is 3.5–4.1 dB lower (Table 1's c2c column vs its G_single column)".
- *Measured:* The ledger (`cascade_per_cell_dB`) books 8.40 / 8.63 / 8.98 / 9.31 dB; 8.1–8.5 dB is the measured single-cell G_worst1 (8.13–8.53). Table 1 has no c2c column (c2c is in Tables 2a and 4). G_single − c2c from the reply's own rows: 3.46–4.45 dB at J = 0/−1 (N = 480 m = 30 J = 0: 8.4681 − 4.016 = 4.45; m = 28 N = 480 J = 0: 4.29), 1.9–3.3 dB at J = −3/−6. My re-execution: J = −1 8.288 − 4.799 = 3.49, J = −6 8.288 − 6.365 = 1.92.
- *Fix proposed:* "against the 8.1–8.5 dB the single cell delivers at the launch amplitude (the ledger books 8.4–9.3)"; "3.5–4.5 dB lower at the 0/−1 dB classes (Tables 2a/4 c2c vs G_single)".

**check2-7 — minor.**

- *Claim:* Verdict item 8: "J = −1, cell 1's drain velocity fed to the next source clamp: the drain is a velocity node, so the transfer is −28 dB (N = 240) … cell 2 receives 0.0036".
- *Measured:* Own run, velocity-plane coupling h_left = 1 + κ(u1[−1] − u0): active cell 1's mean-'1' drain velocity perturbation 0.004065 → cell 2 receives 0.003623 (reproduces 0.0036), c2c worst 7.554 dB (reproduces 7.55–7.63), stage-2 floor −3.69 (`cav`) / −3.78 (`drn_h`) (reply −3.6 to −3.7). The active cell's velocity transfer over the launch is +6.2 dB; −28 dB is the PASSIVE cell's velocity port transfer (session gate.out: active drn_u gain 34.0 dB over passive → passive 8.1×10⁻⁵ = −27.9 dB), consistent with Table 6's passive definition but not said so.
- *Fix proposed:* Write "the passive port-to-port velocity transfer is −28 dB" and name the active cell's 0.0041 (+6.2 dB) beside it.

**check2-8 — minor.**

- *Claim:* Limitation 8: "the record's macOS monoculture (08-06 limitation 1) is broken for the first time here".
- *Measured:* notes/2026-07-22-mth-numerical-vs-physical-viscosity.md header: executed on "Windows/CPython"; notes/2026-08-08 §"07-22's own convention first" reproduces its augmented root "across platforms (Windows/CPython there, macOS arm64 here)" and its Limitation 2 names that cross-platform datum. First Linux x86_64 execution: yes; first non-macOS: no.
- *Fix proposed:* "the first Linux x86_64 execution of the chain (07-22 ran on Windows; 08-08 reproduced its root cross-platform)".

**check2-9 — minor.**

- *Claim:* Table 3 (prompt deliverable: "'0'-floor (both denominations), '1' pp and latency per stage"); verdict item 4 bold "A windowed floor is a single-cell quantity; it does not transfer through a resonant stage" under a *Demonstrated* label; header/Limitation 8 use of the string "bit-equal" (in negation only).
- *Measured:* Table 3 carries a window-shift column and a one-line latency note (stage 1→2 passive/active only), not a per-stage latency column; the bold sentence is a generalisation beyond the measured rows (in-model/interpretive); "bit-equal" appears twice, both as "not bit-equal" / "not claimed" — no exact equality is asserted.
- *Fix proposed:* Add a per-stage latency column (or state that stage k→k+1 latencies were measured only for k = 1); label the bold generalisation in-model; optionally replace "bit-equal" with "exact equality" to satisfy the letter of the rule.

### Re-execution log (verbatim)

```text
Seat dir: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/check2/ (seat.py = own instrument written from the reply's stated coupling definition before reading cascade_driver.py; released fable-model-chain/ imported unedited; platform Linux x86_64, Python 3.11.15, numpy 2.4.6; nproc 4).

[1] python3 phase1.py  (own measure_Mth_num_N(240) = released bracket generalised to N; cell 1 active/passive, m=30, N=240, seed 7, duty 0.8, 2e-3, window [0.25,0.72]):
M_th_num(240) = 0.16894319463373797  shipped 0.16894319463373791  rel dev 3.285787944971905e-16 (29.5s)
bias = 0.11826023624361658
('pas1', 1728000 steps, 46.6s) ('act1', 1898294 steps, 50.5s)
GATE cav: G_worst1_dB 8.287855791924049, G_mean1_dB 8.410165254217045, pp_raw_dB 0.30577762777571854, eye_dB 11.705114659586407, max0_below_mean1_dB -11.828336851446547, mean1_level 0.03267155023359718
GATE drn_h: G_worst1_dB 8.663537342727865, G_mean1_dB 8.769558457037114, max0_below_mean1_dB -11.775002445228234, mean1_level 0.03396500068703142
promoted: G 8.287855791924017 (rel 3.9e-15) floor cav -11.828336851447219 (rel 5.7e-14) floor drn_h -11.775002445226676 (rel 1.3e-13)
cell1 slot-mode drn_h floor: -15.6648766590724 (peak−mode gap 3.89 dB, = 08-12)
passive transfer stage1 = 20log10(mean1 drn_h passive / 2e-3): 15.8296085712346
act1 mean1 drn_h: 0.03396500068703142

[2] python3 phase2.py  (A* = act1 mean-'1' drn_h × κ(−1 dB) = 0.030271338726030064; 10 runs in Pool(4): act2/pas2 on act1 at J=−1 and J=−6, pas2 on pas1 at both, boundary-driven act/pas at A*, velocity-plane act2/pas2 on act1's drn_u at J=−1; lockstep when dt equal (act→act, pas→pas), np.interp across the two released dt otherwise)
('pas2_act1_J1', 1728000, lock False, 93.5s) ('pas2_pas1_J1', 1728000, True, 94.6s) ('act2_act1_J1', 1898294, True, 97.5s) ('act2_act1_J6', 1898294, True, 97.8s) … DONE

[3] python3 phase3.py (verbatim output):
LATENCY passive stage (pas1->pas2, J=-1): envelope xcorr lag = 5.0986 units = 2.5493 rt = 1.2747 ps = 0.0850 slot
   peak-time lag (median/min/max, units): (1.0486, 1.0486, 1.0486) -> rt 0.5243
LATENCY active stage (act1->act2, J=-1): envelope xcorr lag = 11.4520 units = 5.7260 rt; peak-time lag median 9.583 units (4.79 rt)
reply: passive 0.525 rt peak / 2.568 rt envelope; active 4.792 / 5.704 rt
SINGLE cell 1 (cav): 8.287855791924049 8.410165254217045
===== J=-1 kappa=0.8913 input amp to cell2 = 0.03027
[unshifted] chain/passive-chain cav worst 12.734 mean 13.139 | G4_A worst 1.537 mean 1.562 | G4_A(drn_h) 1.486 | G4_B 1.788 | c2c worst 4.649 mean 5.003 | upstream-through-passive worst 8.062 mean 8.136 | stage-2 floor peak cav -3.56 / drn_h -3.09 / mode -4.10 | pp 0.997 | eye 3.15 | mean-'1' drn density 0.3166
[exact passive lag 2.568 rt] chain worst 13.000 mean 13.337 | G4_A 1.569 / 1.586 | drn_h 1.550 | G4_B 1.804 | c2c 4.704 / 4.968 | upstream 8.270 / 8.369 | sum means 13.337 | floors -4.64 / -4.31 / -6.21 | pp 0.853 | eye 4.29 | density 0.3310
[rounded 1/8 rt 2.625 rt] chain worst 13.103 mean 13.399 | G4_A 1.581 / 1.593 | drn_h 1.550 | G4_B 1.804 | c2c 4.799 / 5.030 | upstream 8.270 / 8.369 | sum means 13.399 | floors -4.70 / -4.31 / -6.26 | pp 0.750 | eye 4.40 | density 0.3310
[active lag 5.40 rt] chain worst 13.110 mean 13.402 | floors -6.33 / -6.10 / -8.30 | eye 6.03
passive transfer stage1 15.83 dB; stage2 15.82 dB (unshifted and shifted)
===== J=-6 kappa=0.5012 input amp 0.01702
[unshifted] chain worst 14.157 mean 14.545 | G4_A 1.708 / 1.729 | c2c 5.961 / 6.285 | floors -2.39 / -2.09 / -3.24 | eye 1.99
[exact 2.568 rt] chain worst 14.639 mean 15.109 | G4_A 1.766 / 1.797 | drn_h 1.758 | G4_B 1.678 | c2c 6.178 / 6.582 | floors -4.00 / -3.82 / -5.46 | pp 1.158 | eye 3.51
[rounded 2.625 rt] chain worst 14.826 mean 15.219 | G4_A 1.789 / 1.810 | drn_h 1.758 | G4_B 1.678 | c2c 6.365 / 6.692 | upstream 8.422 / 8.527 | floors -4.10 / -3.85 / -5.51 | pp 0.989 | eye 3.70 | density 0.2318
[active lag 5.40 rt] chain worst 14.861 | floors -5.79 / -5.72 / -7.74 | eye 5.40
passive transfer stage2 15.79 dB
===== Table 2a matched row: G(A*) worst / mean: 4.7972804165535985 4.929355438500025 floor -13.083 (reply 4.797 / 4.929)
  Delta (rounded 2.625rt) worst +0.001 mean +0.101 (reply +0.001 / +0.101); (exact 2.568rt) -0.093 / +0.039; (unshifted) -0.149 / +0.073
===== velocity plane (J=-1): act1 mean-'1' drain velocity pert 0.004065219510236737 -> input to cell 2 0.003623130702218097; active transfer vs launch +6.16 dB
  [rounded 2.625rt] c2c worst 7.554 mean 7.742 | floor peak cav -3.69 drn_h -3.78 ; [unshifted] c2c 7.327 / 7.447 | floor -1.93 / -1.99
===== residue (cell 1 active drn_h, '0' slots after a '1' / after a '0'): promoted window (-11.775, -36.310); first quarter [0,0.25] (-5.698, -30.068); whole slot (-5.698, -30.068)   (reply: -11.78/-36.3 ; -1.57/-25.9 ; -5.70)

[4] residue denominators (inline python over act1_m30N240s7.npz):
dh mean1 windowed 0.03396500068703142 mean1 first-quarter 0.02112298068773024 mean1 whole 0.03396500068703142
  first-quarter after-1 max: 0.01762482648518382 -> over windowed mean1: -5.698135552334909  over first-quarter mean1: -1.5726070375520012
  first-quarter after-0 max over windowed mean1: -30.067518505351373  over first-quarter mean1: -25.941989990568466
  whole-slot after-1 max over windowed mean1: -5.698135552334909
  '0'-slot energy over mean '1'-slot energy max/median dB: -10.562902465497718 -13.827133119305548
  slot 7/13/16: first-quarter peak at 0.009/0.009/0.008 slot, value 0.01706/0.01709/0.01762

[5] run_all.py in scratch copy (never in the repo tree): cp -r fable-model-chain chain_copy; python3 run_all.py (51.9s, no --json → results.json unchanged, 0 diffs); python3 run_all.py --json (51.8s) then diff vs shipped:
M_th_num 0.16894319463373791 0.16894319463373797 3.285787944971905e-16
pulse_gain_dB_at_0p7_streaming 7.7967069614868425 7.796706961486704 1.777107106341685e-14
noise_figure_floor_dB 2.768939660565078 2.7689396605650773 1.603824078129005e-16
differing numeric keys: 3 (of 46) | results.json mtime changed: True

[6] python3 mth_ladder.py 480 / 720:
M_th_num(480) = 0.1587475408418196  promoted 0.1587475408418196  exact_equal=True  rel_dev=0.000e+00 (69s)
M_th_num(720) = 0.15556838465677253  promoted 0.15556838465677247  exact_equal=False  rel_dev=3.568e-16 (121s)

[7] Key-collision grep (grep -rl over notes/, fable-model-chain/results.json, fable-model-quantum/results.json, papers/*.md) for the nine registered names: no hits for any.

[8] Internal-consistency arithmetic on the reply's tables (by hand from the printed rows): G4_A = chain/G_single holds to 3 decimals on all 18 Table 1 rows (e.g. 13.103/8.2879 = 1.581, 14.667/8.4681 = 1.732, 14.599/8.5316 = 1.711); margins 0.089/0.032/0.011 and extrapolant 3·1.711 − 2·1.732 = 1.669 check; item 5's −24.6/−24.3/−25.0/−24.8 = −20log10(A*/2e-3) check; item 2's 0.01237 = 2e-3·10^(15.83/20), 1/(1−0.7451522890452021) = 3.924 (+11.88 dB, doubled +17.9) check; item 1's range 12.5–14.8 / 12.1–14.7 / 13.5–14.6 checks; item 4's floor ranges do NOT match Table 5 (defect 2); item 7's +0.2 to +0.5 dB does not match Table 1 (defect 5).

Not re-executed (budget): m = 28 rows, N = 480/720 chains, seeds 11/13, depth stages 3–5, Table 2b ladder, J = −3/−10/−15/−20/−25 rows (cross-checked against the raw analysis_final.out / analyze_depth.out and for internal consistency only).
```

### Citation audit

Checked against the record (all verbatim reads): (1) 08-12 §1 gate 2 digits 8.287855791924017 / −11.828336851447219 / −11.775002445226676 and gate 3's 8.531556 / −11.318743 — as cited. (2) 08-02 §3.2 paired table: m=28/N=240 8.1315/−10.7312, m=30/N=480 8.4681/−11.4628, m=28/N=480 8.2586/−10.4030, seed-11 −11.8437, drn_h −11.7750 — as cited; §3.1 plane attribution (drain = density antinode, source = node; "the field the next cell actually receives … is drain-plane density") — as cited. (3) 08-12 §2: peak-vs-mode gap 3.83 (cav_u) / 3.89 (drn_h) — as cited and reproduced (3.89). (4) 08-01 ratio-bias §1–§3: bias 0.7·M_th_num(N) values, N=720 rung 0.15556838465677247, rows 8.2879/−11.83 etc. — as cited. (5) 08-01 gated §4: the load-bearing assumption quoted verbatim ("an upstream cell presents the same duty-0.8 waveform the drive boundary does. No multi-cell cascade was run") and "no re-launch inside that depth" — as cited; §5 ratio-leg streaming knee 0.01203/0.01208 → reply's "0.0120" — as cited. (6) 07-31 §2 launch conventions (duty 0.8, raised-cosine 2 rt, active-envelope carrier centre 0.5·φ·repT, window [0.25, 0.72]) and exp_duty.make_sig_duty — reproduced verbatim in my instrument. (7) Part I §7.4 "+8.4 to +9.3 dB net per cell (two-cell total ~+17–19 dB over the passive chain, computed as twice the per-cell figure)", "the direct two-cell time-domain test is open work", cascadability row "in-model yes: 2 cells, +8.4–9.3 dB/cell through −6 dB junctions", Table 7 G4 "≥ 1.7× the single-cell decibel gain / ≈ 2×", "passive twins for differential measurement", §9.4 "−1 to −3 dB budgeted per junction", §6.3/§7.4 "per-cell gain … defined at the junction-attenuated swing" — all present verbatim. (8) cell.py:43–52 cascade_per_cell_gain_dB: swing = A_op·10^(J/20), A_op = 0.0116; results.json cascade_per_cell_dB {8.40, 8.63, 8.98, 9.31}, per_gate_loss_353K_dB 2.555 — as cited. (9) 07-20 §2 / 07-21 §2 (F = 2 split −3.01 dB, per-gate loss, −0.95 dB bulk term outside the solver) — as cited; booked once in §2. (10) 08-06 limitation 1 "One machine, one platform" — as cited, but see prior-art audit. (11) 08-02 §4 and 08-06 "sub-first-order" floors (fitted p 0.55–0.89; 08-06 p ≈ 1.03–1.06 with 0.79–0.89 variants) — Limitation 4's "both measured sub-first-order floors" is fair for 08-02, loose for 08-06 (whose fitted order straddles 1). (12) agents/README 2026-08-13 policy names Fable 5 for execution — as cited. (13) Discussion #124 cited only as unpromoted, not re-run, not settled — compliant. Mis-citations found: none blocking; one prior-art misstatement (Limitation 8, below) and one mis-attribution of "the ledger books 8.1–8.5 dB" (defect 6).

### Prior-art audit

INDEX.md read in full; no premise the record has corrected is used as a premise: the reply builds on the ratio bias (08-01), both denominations (08-02), the slot-mode floor (08-12), A_op's retirement (08-01 G1), the retired 4-ps slot, and treats f_max_F2_gated_GHz = 69 [63, 74] as unmoved. It does not re-announce record content as new: the density-antinode plane (08-02 §3.1), the peak/mode gap (08-12), the 07-22 ring-down memory, the fixed-point ledger (07-20/07-21/08-01) are all credited, and the static T∘T composition of 08-02 §2.4 is explicitly not composed. The two-cell time-domain cascade itself is genuinely new (Part I §7.4 and 08-01 §4 say it was never run; notes/ carry no such run; #124 is a coupled-segment stability operator, not a cascade, and is cited as unpromoted). One prior-art misstatement: Limitation 8's "the record's macOS monoculture … is broken for the first time here" — 07-22 (promoted) was executed on Windows/CPython (its header), and 08-08 reproduced its augmented root cross-platform (08-08 §"07-22's own convention first", Limitation 2). Registered key names: all nine are new (no hits in notes/, either results.json, or papers/*.md).

### Format audit

Executive verdict: 8 items, each carries a label (demonstrated / in-model / open where used; item 5 "in-model over demonstrated rows"). Tables: Table 1 = G4 in the defended definition (A, over passive twins) and the other (B), × junction class × rung × grid, with seed envelopes at N = 240 — as specified; Table 2a = signed Δ (c2c − boundary-driven at matched amplitude) with Table 2b ladder — as specified; Table 3 = per-stage floors in both denominations, pp, eye, chain gain, but latency only as a window-shift column plus a one-line note (per-stage latency measured only for stage 1→2; prompt asked "latency per stage") — minor. Grading table: five items, each confirmed/qualified/contradicted with reasons; grades follow from the measurements (G4 1.45–1.79 < 2; bar failed at 0/−1/−3 dB; Δ ≤ 0.6 dB at matched amplitude; key numbers not moved). Registered keys: nine, new names, each with band; falsifier stated once globally (same-convention rerun outside the band, window-scoped) — acceptable but the residue key's value/definition mismatch (defect 1). Bench discriminant labelled two-sided, premise stated, per 08-01 G1. Limitations (9) and open items present; platform/model line present (Linux x86_64 / Python 3.11.15 / numpy 2.4.6; claude-fable-5-1 executor, claude-opus-5-5 candidate/vote seats, Fable check seats). Epistemic labels: executed numbers labelled demonstrated; extrapolants, loop-model cross-check, coupling construction, scope qualifications labelled in-model; back-action/plane mixing/bias fork labelled open; one bold generalisation under a demonstrated label (defect 9). "Bit-equal": appears twice, only negated ("not bit-equal"/"not claimed"); no exact equality is asserted except N = 480's "exact", which I measured as exactly equal. Word count 8248 (no limit set by the prompt; the ~450-word rule applies to lab posts, not the session reply). Reply header, executing-model disclosure and cloud-session note present; listings referenced to the next comment (12-listings.md exists), but the residue-table computation is absent from the shipped listings (defect 1).

## Executor's adjudication — every defect, re-executed and applied

The executor re-ran each claimed defect against its own artifacts before changing anything (`residue.py`, `analyze_depth.py`, `analysis.json`, the rendered tables). Where the two seats found the same defect, one entry covers both. Nothing was declined; the verdicts did not move.

| defect | reproduced? | what was done | where in the reply |
|---|---|---|---|
| check1-1 / check2-1 — residue key: −1.57 dB was the same-phase ratio, −5.70 dB the ratio under the stated denominator; two denominators mixed in one table; no shipped listing | **yes** (`residue.py`, both denominators: first quarter −5.70 / −1.57 dB at m = 30, −5.31 / −0.98 at m = 28; whole slot −5.70 / −5.31 under the stated denominator) | option (b): the key is registered under its stated denominator at **−5.70 / −5.31 dB**, band re-set to **[−7.0, −4.5]**; the same-phase ratio is reported beside it with its denominator named and is not registered; the residue table names the denominator in every column; `residue.py` ships in the listings | executive item 4; §5 key; residue table after Table 5; §7 |
| check1-2 / check2-4 — undisclosed 0.18·repT cap on Table 3's window shift; "active-lag" row was the cap, not the active lag | **yes** (`sh = min(sh, 0.9·repT − 0.72·repT)` in the first `analyze_depth.py`; bound at stages ≥ 3) | the cap was **removed**; stages 3–5 re-scored at the exact (k − 1) × lag with the slot overrun disclosed and the scored slot count shown (36 → 35 at stage 5); the sensitivity table (Table 3b) now uses the true (k − 1) × active lag; stage 2 (the only load-bearing row) was never capped and is unchanged; the cap is disclosed in limitation 6 | Table 3 caption and rows, Table 3b, §1 (window rule), limitation 6, header (correction history) |
| check1-3 / check2-2 — executive item 4's stage-2 floor ranges narrower than Table 5 | **yes** (Table 5 spans: peak `cav` −4.82 … −3.21, peak `drn_h` −4.51 … −3.66, slot-mode −6.40 … −4.43 at J = 0…−6; J = −25 peak −4.01 … −2.98) | restated as −3.2 to −4.8 (peak `cav`; −3.7 to −4.5 `drn_h`), −4.4 to −6.4 (slot-mode), −3.0 to −4.0 at J = −25; the fail spans recomputed from those bounds (5.2–6.8 / 3.6–5.6 dB round; 7.0–8.6 / 5.4–7.4 dB strict) | executive item 4 |
| check1-4 / check2-5 — window-rule sensitivity ranges (+0.2 to +0.5 gain; −0.9 to −1.7 floor) unsupported | **yes** (`analysis.json`: gain +0.19 … +0.67 dB across Table 1's classes, +1.06 at the sweep's J = −25; floor −1.00 … −1.98 dB) | restated as +0.2 to +0.7 dB (Table 1 classes; up to +1.1 in the sweep) and −1.0 to −2.0 dB, with the bounding rows named | executive item 7 |
| check2-5 — active envelope lag 5.93–5.95 rt not in Table 6 | **yes** (the junction-sweep families were filtered out of Table 6) | Table 6 now carries the junction-sweep families (5.942 / 5.952 rt); the range is quoted as 5.70–5.95 rt | Table 6; item 7; §5 key |
| check1-5 / check2-6 — "Table 1's c2c column" does not exist; "the ledger books 8.1–8.5" conflates the measured single cell with `cascade_per_cell_dB` | **yes** | cites Tables 2a and 4 for the cell-to-cell column; "8.1–8.5 dB the single cell delivers at the launch amplitude (the ledger's `cascade_per_cell_dB` books 8.4–9.3)"; "3.5–4.5 dB lower at the 0 / −1 dB classes and 1.9–3.3 dB at −3 / −6" | executive items 2 and 3; grading table |
| check1-6 / check2-9 — an interpretive clause (item 6) and a bold generalisation (item 4) under *demonstrated* labels | **yes** | both labelled *in-model* in place | executive items 4 and 6 |
| check1-7 — "seed spread ≤ 0.03" (0.033 at −6 dB) | **yes** | "≤ 0.04; 0.033 at −6 dB" | executive item 1 |
| check1-8 — envelope estimator unstated; grid-rounding sensitivity | **yes** (2.568 rt rounds to 2.625; a Hilbert-envelope estimate of 2.54 rounds to 2.5; ≈ 0.1 dB / 0.012 in G4) | estimator and its sensitivity stated | §1 window-rule bullet; limitation 6 |
| check1-9 — ⚛️ Quanta's 2026-09-28 post not credited for the junction budget / isolation point | **yes** | credited where the junction classes and the ideal-isolation assumption are introduced | §2 |
| check1-10 / check2-9 — no per-stage latency for stages ≥ 3 | **yes** | stage-(k − 1)→k lags measured on the passive twin chain (envelope and peak-time) and the active chain, added as a Table 3 column; reported, not registered | Table 3; item 7; limitation 7 |
| check1-11 / check2-6 — "1.5–3.1×" (1.42 at m = 28 / J = −6); "failed at −1/−3 dB" (also failed at 0 dB) | **yes** | "1.4–3.1×"; "failed at 0 / −1 / −3 dB" | executive item 2; grading table |
| check2-3 — platform deviation band and the N = 720 threshold deviation | **yes** (`pulse_gain_dB_at_0p7_streaming` 1.78×10⁻¹⁴; `M_th_num`(720) 3.57×10⁻¹⁶) | header restated as 1.6×10⁻¹⁶ … 1.8×10⁻¹⁴ with each key's deviation; §1 "3.6×10⁻¹⁶" | header; §1 |
| check2-7 — item 8's −28 / −34 dB is the passive velocity transfer, unlabelled | **yes** (`analyze_final.out`: T2pas −27.96 at N = 240, −33.57 at N = 480; active mean-'1' drain velocity 0.0041 = +6.2 dB) | labelled passive; the active figure named beside it | executive item 8 |
| check2-8 — "macOS monoculture broken for the first time" | **yes** (07-22 ran on Windows/CPython; 08-08 reproduced its root cross-platform) | "first Linux x86_64 execution — not its first non-macOS one" | limitation 8 |
| check2-9 — "bit-equal" (in negation only) | **yes** | "exact equality" | header; limitation 8 |
| citation-audit remarks not filed as defects — limitation 3's "+0.6" (08-01's ΔG column starts at +0.43); limitation 4's "08-06 sub-first-order" (its fitted order straddles 1); "§7.4 cascadability row" is Part I's Table 6 | **yes** | all three applied | limitations 3 and 4; grading table |

**Not changed, and why.** The seats' re-executions reproduced every gate, Table 1, Table 2a, Table 3 stage-2, Table 5 and Table 6 number they ran (deviations ≤ 6×10⁻¹⁴ relative on the gate rows; identical to the printed digits elsewhere), so no table value was altered by hand: Tables 3 and 6 and the residue table were re-rendered by the revised listings, and every other table is byte-identical to the draft the seats checked.
