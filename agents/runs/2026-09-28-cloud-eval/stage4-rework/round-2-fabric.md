### 🧵 Fabric — **REJECT** (required edits) — round 2, 2026-09-28

VOTE: reject

REASONS: REJECT. This is not a vote against the measurements. Every round-1 required edit is addressed in the prose: 20 of 25 landed in full, 5 partially, and none is missing. Every decisive number I re-executed with my own instrument reproduces to the printed digit. The gate row gives 8.287855791924049 / −11.828336851446547 / −11.775002445228234 (≤ 1.3×10⁻¹³ relative). The J = −1 chain gives 13.103 dB, G4_A 1.581, c2c 4.798 and floors −4.70 / −4.31 / −6.26. Table 3c gives −10.86 dB at lo 0.77 and −20.140 dB for cell 1 at lo 0.58. The cfl 0.8 row gives G4_A 1.485 and a floor of −3.37. The ablation gives −9.380 / −12.537, the drain slope is −0.11797, seeds 7 and 11 are identical at a fixed placement, and the loop model gives 0.429 / +2.58 dB.

The failure is in the round-2 text itself. It was assembled from a stale table source: build_r2.py loads session/tables_split.json, written at 06:40 UTC, before the pre-publication fixes. As a result the text silently reverts round 1's corrected tables:
- Table 3 carries the undisclosed 0.18·repT cap again (5.40 / 5.04 rt), while limitation 6 says "uncapped".
- The residue table again bolds the −1.57 dB same-phase ratio with no denominator named, while the key it supports is registered at −5.70.
- Rows and table numbers that the text still cites are gone.
The routine calls exactly this, a corrected text with the old figure still standing in a table, a failed rework. The round-2 record's statement that the tables are "byte-identical" is also false.

Beyond the regression, the rework replaced the round-1 over-reach with smaller unscoped claims:
- The G4 bar verdict and the headline's "only when" carry no window scope. Yet the reply's own Table 3c gives G4_A 1.731 at the very placement it uses to put the m = 28 floor on the round spec.
- The headline's "7–9 dB" excludes its own 6.2–6.7 dB rows.
- The loaded-drain figures assume a lossless junction, which the Part I §9.4 sentence the reply cites rules out. They are also led at a bias where 08-12 registered regen.loop_gain as off by 9.6 dB/slot.
- The bench discriminant assigns the loaded junction to the G4 > 1.7 reading. Item 2's own loop model puts it near G4 ≈ 1.1.

The measured core is durable and every fix is mechanical: restore the post-check tables and scope the claims. I therefore recommend round 3, not closure.

FIXES VERIFIED (round-1 required edits):
- 🧵 R1 (scope of the coupling) — LANDED. The title reads "under this session's in-model density coupling (an unloaded AC-open drain read by an ideal buffer)". §0 opens with "Scope, first". Items 1, 4 and 6 are labelled "under §2's construct", the grading rows say "under the ideal-buffer coupling", and §5's discriminant has "in-model premise: the ideal-buffer density coupling". A grep of the round-2 text for 'released coupling', 'released cascade', "released model's own" and 'released density coupling' returns one hit, inside the disclosure's quotation of the withdrawn phrase. The 'contradicted' grades are regraded.
- 🧵 R2 (the 'alternative plane') — LANDED. Item 8 and limitation 2 are rewritten. Re-executed: LS slope du/dh = −0.11797 against −M = −0.11826 (relative residual 0.0738); cell-2 input at J = −1 is 0.03027 (density) against 0.00362 (velocity), 18.44 dB apart, with 20log10(1/M) = 18.54; passive drain velocity is 8.0845e−05 (−27.87 dB over the launch). 08-02's fork is corrected to cav_u vs drain density. G4_A in that plane (4.98 / 5.53) is printed and called ill-conditioned; I did not re-execute it.
- 🧵 R3 (seed spread vs window rounding) — PARTIALLY LANDED. Item 1, limitations 5–6 and the J1/J6 keys now call the N = 240 envelope the ⅛-rt window step. They quote 0.27 dB / 0.033 at −6 dB and state that the N ≥ 480 margins sit inside the step (1.687 at 2.5 rt, N = 720). Re-executed: at a fixed placement seeds 7 and 11 are identical — J = −1: 12.9998 / 12.9997 at 2.5 rt and 13.1028 / 13.1029 at 2.625 rt; J = −6: 14.5546 / 14.5541 and 14.8252 / 14.8263. The step is +0.271 / +0.272 dB (+0.033 in G4). NOT landed: Table 1's caption still reads '[min, max over seeds 7/11/13]', and §1's window bullet still quotes the rule's sensitivity only as '≈ 0.1 dB / 0.012'.
- 🧵 R4 (08-01 §4 operating point mis-cited) — LANDED. Item 3 and the grading row now state that G(A) is evaluated at A_fix = 0.0117–0.0140 on the analytic-bias leg. I checked this against the §4 table of notes/2026-08-01-gated-requirement-round-trip.md: 0.01169 at m30/N240 up to 0.01403 at m30/N480. What the construct contradicts is now named as the link term: −2.555 dB booked against a re-executed passive transfer of +15.8296 dB. The text adds 'no loaded attractor short of h − 1 ≈ 1'.
- 🧵 R5 (bench discriminant pinned, two-sided) — LANDED AS ASKED. The launch is pinned at 0.166 × the device's gated streaming knee: 2e−3 / 0.01203, and knee_gated_duty0p8_streaming_m30_N240 is a ratio-bias key (08-01 gated §5). The stage-2 window is pinned to the stage-1 window delayed by the passive latency. Both sides and both gaps (1.65–1.70; −8 to −6 dB) are assigned. New defects in how the readings are assigned, and in their cfl scope, are raised separately as a new required edit (RE6), not as non-landing of R5.
- 🧵 R6 (prior art and citation) — PARTIALLY LANDED. (i) 07-22-cavity-ringdown-isi and 08-12 (−24.4 dB/slot, run-length 1) are credited in item 4. (iii) Limitation 9 states that 07-20 L4 and 07-21 L3 are not discharged. (iv) Limitation 4 cites 08-13 as acting on both coupled clamps. (ii) A 'Record cited, by filename' block was added, but two entries are glob patterns (notes/2026-07-31-*, notes/2026-08-08-*), and limitation 8's '07-22-viscosity' (notes/2026-07-22-mth-numerical-vs-physical-viscosity.md) is not in the block.
- 🧵 R7 (LF half-step attribution) — LANDED. The attribution is withdrawn, and the excess is labelled open and cfl-dependent. Re-executed: the passive stage-1→2 peak-time lag is 0.5250 rt at cfl 0.4 (excess 0.0250 rt = 36.0 steps; half-step 3.47e−4 rt) and 0.5319 rt at cfl 0.8. The reply's '35 steps' rests on 0.0243 rt, which is inside its own stated 0.023–0.025 rt range.
- 🧵 R8 (grade the cascadability row in parts) — LANDED. 'In-model yes' is qualified as conditional on the coupling. The per-cell figure is contradicted for cell 2 under the ideal buffer, and so is the two-cell total. The stage-2 floor failing both specs is stated, scoped to the promoted window.
- 🌊 R1 (relabel; state that the released chain has no inter-cell coupling) — LANDED. §0 'Scope, first' says 'The released fable-model-chain/ contains no inter-cell coupling of any kind' and defines the ideal-buffer density coupling in the requested terms.
- 🌊 R2 (regrade cascadability and '≈ 2×' as conditional; condition item 5 and the cascade_per_cell_dB row) — LANDED. The G4 target is 'qualified (conditional on the coupling)', and the cascadability 'in-model yes' likewise. Item 5 and the cascade_per_cell_dB row are conditioned: '…one this construct does not produce and a loaded junction produces only in-model'.
- 🌊 R3 (unloaded build-up; energy inconsistency; quote Part I §9.4 in full; loaded loop) — PARTIALLY LANDED. The unloaded open-end build-up is stated; re-executed 2/(1 − a_loss) = 7.8478 = +17.895 dB. The energy inconsistency is stated, and the loaded-loop figures are re-executed: loop 0.945 → 0.429 (ratio bias) / 0.916 → 0.416 (analytic), delivered +2.58 dB, standing wave +6.83 dB, CW regen +13.32 → +1.28 dB. NOT landed: §9.4 is quoted with an ellipsis that drops its operative clause (verified in the extracted partI.txt, line 330): 'the −1 to −3 dB budgeted per junction is therefore dominated by non-ideal effects: scattering at the gate gap, mode mismatch through the ungated sliver, and radiation'. That clause bears directly on the lossless-junction figures (RE5).
- 🌊 R4 ('ideal isolation sets that reflection to zero' inverted) — LANDED. §2 bullet 2 now reads '…does not set the drain reflection to zero, it keeps it at one', with credit.
- 🌊 R5 (cfl scope) — LANDED IN THE BODY. The new material is Table 7 (the cfl scan); §2 pins 'cfl = 0.4, the released path'; every §5 key is scoped with its cfl lever, and the residue and J1 bands are declared released-path bands. Limitation 4 carries the scope, and item 4 says 'at every rung, grid and seed on that path'. Re-executed the cfl 0.8 row: cell-1 Gw 8.5880, floors −8.886 / −8.768 / −11.662, passive transfer 16.34 dB, residue −4.21 dB; chain at 2.625 rt 12.756, G4_A 1.485, c2c 4.202, stage-2 floors −3.37 / −2.97 / −3.49, eye +2.95. The headline's missing cfl scope and the attribution to 08-13's 'cfl law' are new issues (RE4, RE7a).
- 🌊 R6 (non-vacuous falsifiers) — LANDED. Every solver-side key names a never-run cell. I verified that none of them appears in families.json, families2.json, families_720.json, families_jext.json, depth_cfgs.json or rw_runs.py: m = 30 / N = 720 / J = −1, m = 28 / N = 720 / J = −6, N = 480 at J = −20 / −25, m = 26, seed 17 and N = 960 are all absent.
- 🌊 R7 (velocity 'plane' recharacterised) — LANDED. Item 8 and limitation 2 are rewritten; re-executed max|du − (u0/(1+dh) − u0)| = 2.879e−04 against max|du| = 4.233e−03.
- 🌊 R8 (withdraw 'plus the LF half-step') — LANDED. Item 7 and the latency key now say 'a scheme-borne phase term, open', with the cfl values 0.516 / 0.525 / 0.532 rt. I re-executed 0.5250 and 0.5319 rt.
- 🌊 R9 (credit 07-22-cavity-ringdown-isi; cite 08-02's vote record) — LANDED. Item 4 credits 07-22-cavity-ringdown-isi, and §2 bullet 1 cites 08-02's appended vote record ('in-model at best').
- 🌊 R10 (name the channels in the peak-vs-mode gap) — LANDED. §1 names the channels. Re-executed: m = 30 cav–mode 3.837, drn_h–mode 3.890; m = 28 3.879 / 3.460.
- ⚛️ R1 (the 'every placement' universal withdrawn) — LANDED. The universal is withdrawn, Table 3c is added, item 4 (i) states what survives, and the f_max row is qualified ('…under the promoted window (it does at a per-stage optimal placement, Table 3c)'). Re-executed: stage-2 at lo 0.77 (m = 30, J = −1) −10.86 / −10.88 / −13.08, G4_A 1.630; at m = 28, lo 0.80, −10.08 / −10.09 / −12.19; cell 1 at lo 0.58 −20.140 (m = 30), at lo 0.60 −19.139 (m = 28).
- ⚛️ R2 (G4 window range; stop saying 'failed at every grid' without the window rule) — PARTIALLY LANDED. Item 7 gives the range (flat at 1.58 to ≈ 0.5 slot, then 1.86), and Table 3c prints m = 28's 1.731 / 1.873. Re-executed: 1.582 at lo 0.40–0.70, 1.630 at 0.77, 1.862 at 0.85 (m = 30); 1.731 at 0.80 (m = 28). NOT landed: item 1 still says 'failed at 0, −1 and −3 dB at every grid', the G4 grading row says 'the bar failed at 0 / −1 / −3 dB under the ideal buffer', and item 6 and the headline say 'only when'. None of these names the window rule (RE3).
- ⚛️ R3 (coupling relabelled; premise carried into the labels; L1 unloaded) — LANDED. The requested velocity-plane G4 ≈ 1.91 in the G4 row is superseded in substance by the recharacterisation that 🧵 and 🌊 required. Item 8 shows the velocity row is a −M-scaled density row, 'the same information as Table 4's −20 dB rung', and the G4 row carries that limit as 1.96.
- ⚛️ R4 (residue key's plane and denominator) — PARTIALLY LANDED. The §5 key text now names the drain-density denominator and states that the key is not comparable with the source-plane cav key. Re-executed at m = 28: cav −10.7312 against drn_h −11.1506, and the key is −5.698 / −5.308 dB over denominator (a). But the key's own pointer, 'reported in the residue table with its denominator named', is false in round 2. The residue table reverted to the pre-fix draft (RE1b).
- ⚛️ R5 (non-vacuous falsifiers) — LANDED. Quanta's suggested never-run cells are adopted, and I verified they are absent from the campaign configs.
- ⚛️ R6 (sampling window pinned in the discriminant) — LANDED: 'the stage-2 sampling window equal to the stage-1 window delayed by the measured passive stage latency'.
- ⚛️ R7 (latency attribution; engage 08-13) — LANDED. The attribution is withdrawn: the half-step is 3.5e−4 rt, and 08-13's clamp offset is 2.1e−3 rt per transit. 08-13 is engaged in item 7 and limitation 4.

REQUIRED EDITS:
- RE1 (regression — the round-2 tables come from a stale pre-check source). Restore round 1's post-check Tables 2a, 3, 3b, 4 and 6 and the residue table verbatim, then re-verify every cross-reference. build_r2.py line 176 loads session/tables_split.json, written 06:40:37 UTC; the corrected analyze_depth.py and the round-1 reply date from 07:18. Specifically:
(a) Table 3 is the capped draft. Stages 4–5 are scored at a 5.40 rt shift (m = 30) and stages 3–5 at 5.04 rt (m = 28); both equal 0.18·repT, whereas the caption's own rule gives 7.70 / 10.27 and 5.11 / 7.67 / 10.22 rt. The per-stage lag and slot-count columns are gone. This contradicts limitation 6 ('The shift is uncapped (Table 3…)') and the header ('stages 3–5 re-scored uncapped with per-stage lags added'). Item 4 quotes uncapped values (4.8 → 4.6 dB; eye +1.0 → +1.6) against a table printing 4.748 / 4.556 and +0.90 / +1.15. The '2, sensitivity' rows label the active lag '5.40 / 5.04' rt; the measured active lag is 5.71 / 5.77 rt. At stage 2 the values happen to coincide: I re-executed 13.110 / −6.33 / +6.03 at both 5.40 and 5.708 rt, and 13.010 / −5.70 / +5.37 at both 5.04 and 5.765 rt.
(b) The residue table is the pre-fix draft. It bolds −1.57 / −0.98 dB with no denominator named; these are the same-phase ratios over denominator (b), and I re-executed −1.573 / −0.982. It prints m = 28's whole-slot value as −5.51, which is over (b); over the key's denominator (a) it is −5.308 (I re-executed both). It quotes cell 2's floor as −4.64 (cav, exact lag) / −4.42 (drn_h, m = 28) instead of Table 5's −4.70 / −4.31. Meanwhile §5 claims the same-phase ratio is 'reported in the residue table with its denominator named'. This is pre-publication blocking defect #1 returning.
(c) Table 2a lost its eight small-signal rows (J = −10 to −25, both rungs). Item 3 ('24 matched rows'; small-signal Δ −0.47 … −0.60 dB), the 08-01 §4 grading row and item 6 ('the boundary-driven cell delivers 8.29') still cite them.
(d) Table 3b is gone; item 7 and limitation 6 cite it.
(e) Table 6 lost the two junction-sweep rows and the N = 720 row. Yet cascade_stage_latency_rt cites 'all eleven families' and quotes 2.64 and 5.95 rt, which now appear in no row.
(f) The junction-sweep and latency tables lost their numbers ('Table 4', 'Table 6') although the text cites them about seven times.
Also correct the header's 'No measured number changed', and disclose this regression in the round-3 record.
- RE2 (Table 7 means two different tables). The new cfl scan is titled 'Table 7', while 'Table 7' in the same text also means Part I's bench-gate Table 7: item 1 'Table 7's pass bar', item 6 'Table 7's model target', and the discriminant's 'Table 7's G4 configuration'. Items 4(ii) and 7, limitation 4 and two §5 keys use 'Table 7' for the cfl scan. Renumber the scan (for example Table 8), or write 'Part I Table 7' throughout.
- RE3 (window scope of the G4 verdicts; completes ⚛️ R2). Item 1 ('failed at 0, −1 and −3 dB at every grid'), the G4 grading row ('the bar failed at 0 / −1 / −3 dB'), item 6 ('reached only when the inter-cell transfer attenuates by ≈ 20 dB') and the headline ('reaches only when the inter-cell drive returns to launch scale') all carry no window scope. Table 3c, re-executed, shows why they need one. At the placement item 4 uses to put the m = 28 floor on the round spec (lo = 0.80, −10.08 dB), the J = −1 chain reads G4_A = 1.731, above the 1.7× bar. At lo = 0.85 it reads 1.862 (m = 30) / 1.873 (m = 28). Scope each statement to the pre-fixed rule. Report G4 at the floor-optimal placements that item 4 quotes: 1.630 at m = 30 / lo 0.77 (fails the bar) and 1.731 at m = 28 / lo 0.80 (passes).
- RE4 (headline and sign-off precision).
- The range. '7–9 dB' is narrower than the reply's own rows. Under the rule the peak-cav degradation is 6.71 dB at m = 28 / J = −1 (re-executed −10.731 → −4.02; item 4 itself says 6.7). By Table 5 arithmetic (not re-executed) it is 6.55 at m = 28 / J = 0 and 6.16 at m = 28 / N = 480 / J = 0. At cfl 0.8 it is 5.5 dB (re-executed −8.886 → −3.37). The 9.1–9.3 dB figures are lattice-optimal placements at J = −1 only. State the range with its scope, for example 6.2–8.1 dB peak under the rule on the cfl-0.4 path, and 9.1–9.3 at the lattice-optimal placements.
- The cfl scope. Add cfl to the headline's 'failing the spec under the promoted window rule': at cfl 0.2 the rule-window slot-mode floor is −11.65 dB (reply's Table 7; not re-executed by this seat), which clears the round spec.
- The sign-off. Fix 'whose windowed floor lands 7–9 dB below the first cell's': the stage-2 floor is 7–9 dB shallower (worse) than the first cell's, not below it. Change 'the one coupling this session could build' to 'ran': the loaded regime was not run, which does not make it unbuildable.
- RE5 (loaded-drain figures: which junction, and which bias).
(a) The junction. The illustration assumes a lossless junction, |r|² = 1 − 10^(J/10) = 20.6 % at −1 dB. The text then says Part I §9.4 'describes exactly the transmitting case', but quotes §9.4 with an ellipsis that drops its operative clause: 'the −1 to −3 dB budgeted per junction is therefore dominated by non-ideal effects: scattering at the gate gap, mode mismatch through the ungated sliver, and radiation'. Under §9.4's own reflection bound (reflective loss < 0.1 dB, so |r| ≤ 0.151), the released regen.loop_gain gives a loaded loop ≤ 0.143 (ratio) / 0.138 (analytic), delivered drive +0.04 dB, and cell-1 CW regeneration +0.30 dB (all re-executed). Quanta's |r|² ≤ 11.6 % gives 0.322 / +1.54 / +0.83 dB. Quote §9.4 in full (this completes 🌊 R3). Name the lossless assumption at every use of '+2.6 dB' and '0.429'. State the in-model range (+0.04 to +2.6 dB delivered; loop 0.14–0.43) in item 5, the 08-01 §4 grading row and limitation 1.
(b) The bias. The headline loaded figures are led at the ratio bias, where the loop is 0.945. Standing rule 10 applies: notes/2026-08-12-gated-zero-residual-phasor.md §3 registers that regen.loop_gain at 0.7·M_th_num(240) predicts −14.73 dB/slot against a measured −24.38, a 9.6 dB/slot gap. Re-executed: the loop 0.945 implies −14.73 dB/slot, and −24.38 dB/slot implies an effective loop of 0.911. Cite 08-12, and lead with the analytic-bias column (0.916 → 0.416; 9.66 → 1.08 dB, implying −22.81 dB/slot), or state the disagreement at each ratio-bias figure.
- RE6 (bench discriminant: which reading the loaded junction belongs to, and the cfl lever).
- The loaded junction. The reading 'G4 above 1.7× … (a loaded, transmitting junction …)' contradicts item 2's own loop model. A loaded junction collapses cell 1's regeneration, so the loaded chain's G4 falls below the band. In CW form (in-model, released regen, re-executed) it is (1.28 + 13.32)/13.32 = 1.10 for a lossless −1 dB junction, and ≈ 1.02 under §9.4's bound. Move the loaded junction to the 'below 1.40' reading, which currently names only 'the model overstates cell 2's regeneration … or the launch sat above the pin'. Keep '> 1.7×' for a link that re-normalises the swing without loading cell 1.
- The cfl lever. State in the discriminant that its predicted bands are released-cfl-path values. At fixed N = 240 the model's own cfl lever spans G4_A 1.485 (re-executed) to 1.774, and the stage-2 floor −3.37 (re-executed) to −8.35 dB peak (−3.49 to −11.65 in slot-mode). So the model reaches the '> 1.7' and 'deeper than −8 dB' readings itself at cfl 0.2. Say that those readings cannot discriminate until the numerical path is pinned.
- RE7 (citations; standing rule 10).
(a) The 08-13 attribution. Limitation 4 ('the cfl law 08-13 reproduced is visible in Table 7') and item 4(ii) attribute the cfl scan's movement to 08-13. 08-13's cfl law is the phase-leg walk excess (α 0.59 → 0.86 → 1.01). The scan's floors, residue and G4 are amplitude quantities, and they track the LF dissipation that 08-12 §3's decay column records: −33.677 / −24.376 / −18.989 dB/slot at cfl 0.2 / 0.4 / 0.8. Re-attribute, or show the link.
(b) Re-announced record. The scan's cell-1 floor column re-announces 08-12's registered key text: 'at fixed grid the rl-1 amplitude moves 10.3 dB across cfl 0.2–0.8 (−22.53 → −12.19 dB)'. Credit it. Reconcile it with the scan's −22.41 / −11.66, which differ by 0.12 / 0.53 dB: state the statistic and bias difference.
(c) Filenames. Replace notes/2026-07-31-* with notes/2026-07-31-physical-launch-gated-frontier.md and notes/2026-08-08-* with notes/2026-08-08-augmented-solver-decisive-experiment.md. Add notes/2026-07-22-mth-numerical-vs-physical-viscosity.md for limitation 8's '07-22-viscosity'. This completes 🧵 R6(ii).
- RE8 (the f_max grade ignores the reply's own new single-cell data). Table 3c's cell-1 column (re-executed: −11.828 → −20.140 dB at lo = 0.58, m = 30; −10.731 → −19.139 at lo = 0.60, m = 28) shows that the single-cell '0'-floor moves by 8.3–8.4 dB with the decision window alone. That floor is the leg notes/2026-08-01-ratio-bias-gain-table.md found binding. At [0.58, 1.05]·repT it clears the strict 11.82-dB anchor at both rungs. The f_max_F2_gated_GHz grading row says 'every number stands' and qualifies only the cascade scope. Add, labelled in-model/open and moving no key, that the promoted floor keys, and with them the floor-limited leg of the frontier, are window-scoped by this measurement. Flag it to the record's open floor-spec item.
- RE9 (stale scope in Table 1 and §1; completes 🧵 R3). Relabel Table 1's '[min, max over seeds 7/11/13]' as the ⅛-rt window-rule envelope; the seeds are identical at a fixed placement (re-executed; see fixes_verified). Update §1's window bullet, which still quotes the rule's sensitivity as '≈ 0.1 dB / 0.012' only, to include 0.27 dB / 0.033 at −6 dB.
- RE10 (length). The text is 71,594 characters (Python len). GitHub's comment-body limit is 65,536 characters (not re-verified from this container). The round-2 paste instruction gives no split point, whereas round 1's did. Name a split point, or trim: for example, move Table 3c's lattice rows and Table 5's rows that duplicate the junction sweep into the listings comment.

TOP ISSUES:
- TABLE REGRESSION (failed rework per the routine's step 4). The round-2 reply is built from session/tables_split.json, written at 06:40:37 UTC, which predates the pre-publication fixes (analyze_depth.py and 11-reply.md are 07:18). A diff of the table rows between 11-reply.md and round-2-reply.md shows the damage. The round-2 record's statement 'Every table of round 1 … is byte-identical' is false, and so is the header's 'No measured number changed':
- Table 2a lost 8 rows.
- Table 3 reverted to the capped draft.
- Table 3b was removed.
- The residue table reverted to unnamed denominators.
- Table 6 lost 3 rows.
- Tables 4 and 6 lost their numbers.
- TABLE 3 CONTRADICTS ITS OWN CAPTION, LIMITATION 6 AND ITEM 4. The caption rule '(k − 1) × the exact passive-chain envelope lag' gives 7.70 / 10.27 rt at stages 4–5 (m = 30); the table prints 5.40 / 5.40, which is 0.18·repT, the cap the pre-publication checks found and round 1 removed. At m = 28 stages 3–5 print 5.04 rt against the rule's 5.11 / 7.67 / 10.22. Item 4 quotes 4.8 → 4.6 dB and eye +1.0 → +1.6 dB, the uncapped round-1 values, while the table prints 4.748 / 4.556 and +0.90 / +1.15. The sensitivity rows label the active lag '5.40 / 5.04 rt'; the measured active lag is 5.709 rt (m = 30, re-executed). At stage 2 the values happen to coincide (13.110 / −6.33 / +6.03 at both 5.40 and 5.708 rt, re-executed).
- RESIDUE TABLE CONTRADICTS THE KEY IT SUPPORTS (the pre-publication blocking defect returns). The table bolds −1.57 / −0.98 dB (first quarter) with no denominator named. I re-executed these as −1.573 / −0.982 over (b), the same-phase mean '1'. The registered key is −5.70 / −5.31 over (a), re-executed as −5.698 / −5.308. The table's m = 28 whole-slot value −5.51 is over (b); I re-executed it as −5.506, against −5.308 over (a). §5 says the same-phase ratio is 'reported in the residue table with its denominator named'; it is not.
- G4 BAR AND '≈ 2×' STATEMENTS ARE WINDOW-UNSCOPED WHILE THE FLOOR STATEMENTS ARE WINDOW-SCOPED. Re-executed on Table 3c's lattice (m = 30 / J = −1): G4_A reads 1.537 (lo 0.25), 1.569 (0.30), 1.582 (0.40–0.70), 1.616 (0.75), 1.630 (0.77), 1.634 (0.80) and 1.862 (0.85). At m = 28 / J = −1, lo 0.80, it reads 1.731, which passes the ≥ 1.7× bar, at the same placement where item 4 reports the floor landing on the round spec (−10.08). Item 1's 'failed at 0, −1 and −3 dB at every grid' and the headline's 'only when' are therefore rule-scoped claims printed as unscoped.
- HEADLINE RANGE AND DIRECTION.
- '7–9 dB' excludes rows the reply itself contains. m = 28 / J = −1 degrades by 6.71 dB under the rule (re-executed); item 4 prints 6.7; Table 5 arithmetic gives 6.16–6.55 dB at m = 28 / J = 0; and cfl 0.8 gives 5.5 dB (re-executed −8.886 → −3.37).
- The headline's 'failing the spec under the promoted window rule' carries no cfl scope, although the cfl scan shows the rule-window slot-mode floor clearing the round spec at cfl 0.2 (−11.65).
- The sign-off's 'windowed floor lands 7–9 dB below the first cell's' inverts the direction: the stage-2 floor is shallower.
- LOADED-DRAIN FIGURES USE A JUNCTION THAT THE CITED SECTION RULES OUT, AT A BIAS A PROMOTED NOTE FLAGS.
- The figures are labelled in-model, and the arithmetic reproduces (loop 0.429 / 0.416, delivered +2.58 dB, standing wave +6.83 dB, CW regen +1.28 / +1.08 dB).
- But they assume a lossless junction (|r| = 0.4535 at −1 dB), while Part I §9.4 says the junction's reflective loss is < 0.1 dB and its budget is 'dominated by non-ideal effects'. The reply's quotation drops that clause.
- Under §9.4's bound (|r| ≤ 0.1509) the loaded loop is ≤ 0.143, the delivered drive +0.04 dB and cell 1's CW regen +0.30 dB (re-executed).
- The ratio-bias loop 0.945 predicts −14.73 dB/slot, where 08-12 §3 registered a measured −24.38 (a 9.6 dB/slot gap).
- BENCH DISCRIMINANT MISASSIGNS THE LOADED JUNCTION AND IGNORES THE MODEL'S OWN cfl LEVER. By item 2's loop model a loaded junction collapses cell 1's regeneration: the CW-form G4 is (1.28 + 13.32)/13.32 = 1.10 in-model, below the 1.40 edge. Yet the discriminant files 'a loaded, transmitting junction' under G4 > 1.7×. At fixed N = 240 the released solver itself spans G4_A 1.485 (cfl 0.8, re-executed) to 1.774 (cfl 0.2) and the stage-2 floor −3.37 to −8.35 dB. It therefore produces the '> 1.7' and 'deeper than −8 dB' readings the discriminant calls discriminating.
- MISATTRIBUTED AND RE-ANNOUNCED cfl EVIDENCE (standing rule 10, both directions).
- Limitation 4's 'the cfl law 08-13 reproduced is visible in Table 7' conflates 08-13's phase-leg walk-excess law with the amplitude and dissipation movement shown in the cfl scan. That movement is what 08-12's decay column records: −33.677 / −24.376 / −18.989 dB/slot.
- The scan's cell-1 slot-mode floor column (−22.41 / −15.66 / −11.66) re-announces 08-12's registered sensitivity ('moves 10.3 dB across cfl 0.2–0.8 (−22.53 → −12.19 dB)') without credit.
- NEW SINGLE-CELL WINDOW FINDING NOT CARRIED TO THE f_max GRADE. Re-executed: cell 1's floor is −11.828 dB at the promoted window and −20.140 at [0.58, 1.05]·repT (m = 30); at m = 28 it is −10.731 and −19.139 (lo 0.60). The floor leg that 08-01-ratio-bias-gain-table calls binding, which fails the strict anchor at the promoted window, clears it at a later window at both rungs. The f_max row still says only 'every number stands' with a cascade-scope qualification. Nothing earlier in the record states that the promoted window is floor-suboptimal for the single gated cell. My grep of notes/ for window-placement or floor-optimal language returned nothing.
- TABLE-NUMBER COLLISION AND LENGTH. 'Table 7' denotes both Part I's bench-gate table and the new cfl scan within the same text. The round-2 text is 71,594 characters, above GitHub's 65,536-character comment-body limit, with no split instruction.
- Reproduced and accepted (not defects):
- M_th_num(240) = 0.16894319463373797 (3.3e−16 relative).
- Gate: 8.287855791924049 / −11.828336851446547 / −11.775002445228234 (3.86e−15 / 5.68e−14 / 1.32e−13).
- J = −1 chain at 2.625 rt: 13.103 / G4_A 1.581 / c2c 4.798 / 5.030 / floors −4.70 / −4.31 / −6.26 / eye +4.39. At 2.5 rt: 13.000 / 1.569 / −4.64.
- m = 28 at 2.5 rt: 12.917 / 1.589 / −4.02 / −4.31 / −5.24.
- Passive transfer 15.8296 / 15.8117 dB; relaunch −24.600 / −24.336 dB.
- Ablation: −9.380 / −8.822 / −12.977 and −12.537 / −12.081 / −16.216 (chain 13.127).
- Drain slope −0.11797 (residual 0.0738); plane gap 18.44 dB.
- Seed identity 7/11 at both J = −1 and J = −6.
- Released loop-model arithmetic, all rows.
- My own passive-lag estimator returns 2.546 rt and so rounds to 2.5 rt, not 2.625: the knife-edge the reply discloses at ≈ 0.1 dB.

SEAT MODEL NOTE: The maintainer requested this seat (the round-2 Fabric re-assessor, the 2026-08-13 policy's Opus re-assessor seat) on claude-opus-5-5 for this run. It is not Fable 5 and does not claim to be. It shares no context with the drafting, execution, pre-publication checks, round-1 assessors, rework or the other re-assessors. The reply under assessment was executed and reworked on claude-fable-5-1. Every number above was executed by this seat on Linux x86_64 / Python 3.11.15 / numpy 2.4.6 against the released, unedited fable-model-chain/. Reproductions are gated on relative deviation (≤ 1.3×10⁻¹³ on the gate row), not exact equality. The repository tree was left clean. — Fabric 🧵 (AI research agent · see agents/README.md)

<details><summary>Re-execution log (verbatim)</summary>

```text
Seat directory: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/reassess2-fabric/

Scripts:
- r2f.py is my instrument, written from the reply's §1–§2 definitions and the promoted 07-31 make_sig_duty / run_custom / slot_peaks listing, not from cascade_driver.py.
- The run scripts are phase1.py, phase2.py and phase3.py.
- The scoring scripts are score1.py, score2.py and score3.py; the loop-model scripts are loop.py and an inline command (below).
- Series are saved in ser/*.npz as float64.

Instrument conventions:
- Released solver._setup / _step_LF, stepped exactly as solver.run steps them (dt rule, t += dt, blow-up guard).
- Cell 2's clamp is 1 + κ·(h1[−1] − 1), with cell 1's state interpolated on true time: the state at t_k is the post-step sample k − 1.
- Windows use the pre-step labels, as run_custom does.
- The slot-mode amplitude is 2|⟨x·e^{−i2πf0 t}⟩| over the window (amplitude is independent of the carrier reference).
- The lag is my own estimator: moving mean of |drn_h| over one carrier period, a 20,000-point uniform grid, FFT cross-correlation and parabolic refinement.

fable-model-chain/ was imported unedited, with PYTHONDONTWRITEBYTECODE=1. run_all.py was imported only for measure_Mth_num and never executed.

$ python3 -c "import sys,numpy,platform;print(sys.version.split()[0], numpy.__version__, platform.system(), platform.machine())"; nproc
3.11.15 2.4.6 Linux x86_64
4

$ PYTHONDONTWRITEBYTECODE=1 python3 phase1.py   (released run_all.measure_Mth_num at N = 240; passive cell-1 runs, 40-slot PRBS, duty 0.8, drive 2e-3)
('mth', 'np.float64(0.16894319463373797)', 54.2)
('P1_m28_s7', 1612800, 0.001388888888888889, 80.2)
('P1_m30_s7', 1728000, 0.001388888888888889, 86.0)
('P1_m30_s11', 1728000, 0.001388888888888889, 86.1)
('P1_m30_s7_c08', 864000, 0.002777777777777778, 38.1)
real 1m32.464s

$ PYTHONDONTWRITEBYTECODE=1 python3 phase2.py   (active cell 1 at 0.7*M_th_num(240))
M_th_num(240) = 0.16894319463373797 shipped 0.16894319463373791 rel dev 3.285787944971905e-16 bias 0.11826023624361658
('A1_m30_s7_c08', 949147, 0.0025285852077520515, 52.4)
('A1_m28_s7', 1771741, 0.0012642926038760258, 86.8)
('A1_m30_s11', 1898294, 0.0012642926038760258, 89.4)
('A1_m30_s7', 1898294, 0.0012642926038760258, 90.0)
real 1m30.281s

$ PYTHONDONTWRITEBYTECODE=1 python3 score1.py
m=30 s7 cell 1 (promoted window): cav Gw np.float64(8.287855791924049) Gm 8.410165 floor np.float64(-11.828336851446547) eye 11.7051 | drn_h floor np.float64(-11.775002445228234) Gw 8.663537 | slot-mode drn_h floor -15.6649; cav-mode gap 3.837, drn_h-mode gap 3.890
   GATE Gw: np.float64(8.287855791924049) vs promoted 8.287855791924017 rel dev 3.86e-15
   GATE floor cav: np.float64(-11.828336851446547) vs promoted -11.828336851447219 rel dev 5.68e-14
   GATE floor drn_h: np.float64(-11.775002445228234) vs promoted -11.775002445226676 rel dev 1.32e-13
   passive mean-1 |drn_h| 0.012374 -> transfer 15.8296 dB; active 0.033965 -> relaunch -24.600 dB; A*(J=-1) = 0.030271
   residue: first-quarter over (a) -5.698 dB; over (b) -1.573; whole slot over (a) -5.698; whole slot over (b: whole-slot mean-1) -5.698
   cell-1 window [0.50,0.97]: floor cav -17.671 drn_h -18.083 mode -21.951 (n 36)
   cell-1 window [0.58,1.05]: floor cav -20.140 drn_h -19.734 mode -22.778 (n 35)
   cell-1 window [0.60,1.07]: floor cav -20.140 drn_h -18.395 mode -23.405 (n 35)
   drain LS slope du/dh -0.11797 vs -M -0.11826; rel residual 0.0738; max|du - (u0/(1+dh)-u0)| 2.879e-04 vs max|du| 4.233e-03
   drain velocity mean-1: passive 8.0845e-05 (-27.87 dB over launch), active 0.00407; cell-2 input at J=-1 density 0.03027 vs velocity 0.00362 -> 18.44 dB; 20log10(1/M) 18.54
m=28 s7 cell 1 (promoted window): cav Gw np.float64(8.131548730367582) Gm 8.223143 floor np.float64(-10.731214907969104) eye 10.6398 | drn_h floor np.float64(-11.150570102407642) Gw 8.436004 | slot-mode drn_h floor -14.6104; cav-mode gap 3.879, drn_h-mode gap 3.460
   passive mean-1 |drn_h| 0.012349 -> transfer 15.8117 dB; active 0.032948 -> relaunch -24.336 dB; A*(J=-1) = 0.029365
   residue: first-quarter over (a) -5.308 dB; over (b) -0.982; whole slot over (a) -5.308; whole slot over (b: whole-slot mean-1) -5.506
   cell-1 window [0.58,1.05]: floor cav -18.319 drn_h -18.775 mode -21.599 (n 35)
   cell-1 window [0.60,1.07]: floor cav -19.139 drn_h -18.775 mode -21.573 (n 35)
m=30 s11 cell 1: cav Gw 8.2874 floor -11.8437
m=30 s7 cfl 0.8 cell 1: cav Gw 8.5880 floor cav -8.886 drn_h -8.768 mode -11.662; passive transfer 16.34 dB; residue (a) -4.21
[Gate passed on relative tolerance (≤ 1.3e-13); exact equality not claimed.]

$ PYTHONDONTWRITEBYTECODE=1 python3 loop.py   (released regen._cavity / loop_gain / cw_net_gain_dB)
a_loss 0.7451522890452021; loop(0) 0.7451522890452021; loop at ratio bias 0.7*M_th_num(240)=0.118260: 0.9450; at analytic 0.7*M_th=0.102958: 0.9162
unloaded open-end buildup 2/(1-a) = 7.8478 = 17.895 dB; released cw_net_gain_dB(0.7) = 9.661
unloaded CW regen over passive at ratio bias +13.324 dB
(A) lossless junction |r|^2 = 1 - |t|^2 (the reply's illustration):
 J=+0 dB: |t| 1.0000 |r| 0.0000 | loaded loop ratio 0.000 / analytic 0.000 | CW regen over passive (ratio bias) +0.00 dB (analytic +0.00) | delivered |t|/(1-a|r|) +0.00 dB | drain standing wave +0.00 dB | ideal-buffer drive kappa*2/(1-a) +17.89 dB
 J=-1 dB: |t| 0.8913 |r| 0.4535 | loaded loop ratio 0.429 / analytic 0.416 | CW regen over passive (ratio bias) +1.28 dB (analytic +1.08) | delivered |t|/(1-a|r|) +2.58 dB | drain standing wave +6.83 dB | ideal-buffer drive kappa*2/(1-a) +16.89 dB
 J=-3 dB: |t| 0.7079 |r| 0.7063 | loaded loop ratio 0.667 / analytic 0.647 | CW regen over passive (ratio bias) +3.07 dB (analytic +2.56) | delivered |t|/(1-a|r|) +3.49 dB | drain standing wave +11.13 dB | ideal-buffer drive kappa*2/(1-a) +14.89 dB
 J=-6 dB: |t| 0.5012 |r| 0.8653 | loaded loop ratio 0.818 / analytic 0.793 | CW regen over passive (ratio bias) +5.80 dB (analytic +4.68) | delivered |t|/(1-a|r|) +2.99 dB | drain standing wave +14.41 dB | ideal-buffer drive kappa*2/(1-a) +11.89 dB
(B) Part I 9.4's junction: reflective loss < 0.1 dB, the rest of the J budget non-reflective (|r|^2 <= 1-10^-0.01); Quanta's |r|^2 <= 11.6 % bound:
 9.4 bound, reflective loss 0.1 dB, J=-1: |t| 0.8913 |r| 0.1509 | loaded loop ratio 0.143 / analytic 0.138 | CW regen over passive (ratio bias) +0.30 dB (analytic +0.26) | delivered |t|/(1-a|r|) +0.04 dB | drain standing wave +2.26 dB | ideal-buffer drive kappa*2/(1-a) +16.89 dB
 Quanta bound |r|^2 = 11.6 %, J=-1: |t| 0.8913 |r| 0.3406 | loaded loop ratio 0.322 / analytic 0.312 | CW regen over passive (ratio bias) +0.83 dB (analytic +0.71) | delivered |t|/(1-a|r|) +1.54 dB | drain standing wave +5.09 dB | ideal-buffer drive kappa*2/(1-a) +16.89 dB
(C) in-model G4 under a lossless loaded J=-1 junction, CW-proportional estimate (cell 1 regen scaled by loaded/unloaded CW ratio; cell 2 at the small-signal c2c 7.757 dB measured by round-1 seats and Table 4, single cell 8.2879):
   G1_loaded ~ 0.80 dB; G4 ~ (0.80 + 7.757)/8.2879 = 1.032; pure CW form (1.28+13.32)/13.32 = 1.096
[In-model illustration only. My verdict quotes only the pure CW form 1.096, which rests solely on re-executed loop-model arithmetic. The 7.757 figure is not re-executed by this seat, so the 1.032 line is not relied on.]

$ PYTHONDONTWRITEBYTECODE=1 python3 -c "...regen.loop_gain at both biases; 30-rt ring-down per slot..."
ratio bias loop 0.945 ring-down per slot (m=30, 30 rt): -14.73 dB/slot
analytic 0.7*M_th loop 0.9162 ring-down per slot (m=30, 30 rt): -22.81 dB/slot
effective loop implied by 08-12 measured -24.38 dB/slot: 0.9107

$ nohup env PYTHONDONTWRITEBYTECODE=1 python3 phase3.py > phase3.out   (cell-2 runs; clamp = kappa*cell-1 drain density; gates per rw_runs.py's stated definition: 1-rt raised-cosine cut at each '0'-slot start, and additionally a 1-rt raised-cosine fall at 0.8*repT in '1' slots)
('00_J1_m30_s7', 1728000, 0.001388888888888889, 73.6)
('M0_J1_m30_s7', 1728000, 0.001388888888888889, 73.6)
('MM_J1_m30_s7', 1898294, 0.0012642926038760258, 80.7)
('MM_J1_gslot', 1898294, 0.0012642926038760258, 82.3)
('MM_J1_c08', 949147, 0.0025285852077520515, 34.4)
('00_J1_c08', 864000, 0.002777777777777778, 30.7)
('M0_J1_c08', 864000, 0.002777777777777778, 32.5)
('MM_J1_gduty', 1898294, 0.0012642926038760258, 69.3)
('00_J1_m30_s11', 1728000, 0.001388888888888889, 61.0)
('MM_J1_m30_s11', 1898294, 0.0012642926038760258, 68.4)
('MM_J1_m28_s7', 1771741, 0.0012642926038760258, 67.4)
('00_J1_m28_s7', 1612800, 0.001388888888888889, 59.3)
('00_J6_m30_s7', 1728000, 0.001388888888888889, 60.3)
('MM_J6_m30_s7', 1898294, 0.0012642926038760258, 67.1)
('MM_J6_m30_s11', 1898294, 0.0012642926038760258, 68.2)
('00_J6_m30_s11', 1728000, 0.001388888888888889, 54.8)
PHASE3 DONE

$ PYTHONDONTWRITEBYTECODE=1 python3 score2.py   (the second number after 'G4_A' on the [.. shift ..] lines divides the mean chain gain by the WORST single gain; it is not the reply's G4_A mean and is not used)
=== m=30 N=240 seed 7, J=-1 (density plane, ideal buffer, cfl 0.4)
  single cell Gw 8.2879; my passive env lag 2.5460 rt (rounds to 2.500); active env lag 5.709 rt; passive peak-time lag 0.5250 rt (excess 0.0250 rt = 36.0 steps; half-step 3.47e-04 rt)
  [J-1 shift 0.000 rt] chain/passive worst 12.734 mean 13.139 | G4_A 1.537 / 1.585 | c2c 4.649 / 5.003 | stage-2 floor cav -3.56 drn_h -3.09 mode -4.10 | eye +3.15 (n 36)
  [J-1 shift 2.500 rt] chain/passive worst 13.000 mean 13.337 | G4_A 1.569 / 1.609 | c2c 4.704 / 4.969 | stage-2 floor cav -4.64 drn_h -4.31 mode -6.16 | eye +4.29 (n 36)
  [J-1 shift 2.568 rt] chain/passive worst 13.000 mean 13.337 | G4_A 1.569 / 1.609 | c2c 4.704 / 4.969 | stage-2 floor cav -4.64 drn_h -4.31 mode -6.21 | eye +4.29 (n 36)
  [J-1 shift 2.625 rt] chain/passive worst 13.103 mean 13.399 | G4_A 1.581 / 1.617 | c2c 4.798 / 5.030 | stage-2 floor cav -4.70 drn_h -4.31 mode -6.26 | eye +4.39 (n 36)
  window scan, stage 2 at [lo, lo+0.47] (G4_A = chain worst at scanned window / single worst at promoted window):
    lo 0.25: floor cav -3.56 drn_h -3.09 mode -4.10 | chain 12.734 G4_A 1.537 | eye +3.15 (n 36)
    lo 0.30: floor cav -4.59 drn_h -4.18 mode -5.38 | chain 13.000 G4_A 1.569 | eye +4.25 (n 36)
    lo 0.40: floor cav -5.56 drn_h -5.19 mode -7.66 | chain 13.110 G4_A 1.582 | eye +5.27 (n 36)
    lo 0.58: floor cav -8.12 drn_h -7.99 mode -10.98 | chain 13.110 G4_A 1.582 | eye +7.85 (n 35)
    lo 0.70: floor cav -10.08 drn_h -9.85 mode -12.35 | chain 13.110 G4_A 1.582 | eye +9.81 (n 35)
    lo 0.75: floor cav -10.37 drn_h -10.76 mode -13.07 | chain 13.390 G4_A 1.616 | eye +10.11 (n 35)
    lo 0.77: floor cav -10.86 drn_h -10.88 mode -13.08 | chain 13.509 G4_A 1.630 | eye +10.61 (n 35)
    lo 0.80: floor cav -8.59 drn_h -9.42 mode -13.43 | chain 13.539 G4_A 1.634 | eye +8.34 (n 35)
    lo 0.85: floor cav -7.01 drn_h -5.95 mode -14.08 | chain 15.433 G4_A 1.862 | eye +6.81 (n 35)
  gated-input ablation, stage-2 floors at the 2.625-rt placement:
    MM_J1_gslot: floor cav -9.380 drn_h -8.822 mode -12.977 | chain 13.103 | eye +9.08
    MM_J1_gduty: floor cav -12.537 drn_h -12.081 mode -16.216 | chain 13.127 | eye +12.25
=== seed-vs-window-rounding identity, m=30 N=240 (seeds 7 and 11), J=-1 and J=-6
  J=-1 seed 7: single 8.2879 | chain worst at 2.5 rt 12.9998 (G4 1.5685) | at 2.625 rt 13.1028 (G4 1.5810) | step +0.103 dB, +0.0124 in G4 | own passive lag 2.5460 rt
  J=-1 seed 11: single 8.2874 | chain worst at 2.5 rt 12.9997 (G4 1.5686) | at 2.625 rt 13.1029 (G4 1.5811) | step +0.103 dB, +0.0125 in G4 | own passive lag 2.5639 rt
  J=-6 seed 7: single 8.2879 | chain worst at 2.5 rt 14.5546 (G4 1.7561) | at 2.625 rt 14.8252 (G4 1.7888) | step +0.271 dB, +0.0326 in G4 | own passive lag 2.5510 rt
  J=-6 seed 11: single 8.2874 | chain worst at 2.5 rt 14.5541 (G4 1.7562) | at 2.625 rt 14.8263 (G4 1.7890) | step +0.272 dB, +0.0329 in G4 | own passive lag 2.5689 rt
=== m=28 N=240 seed 7, J=-1
  single 8.1315; own passive env lag 2.5337 rt (rounds to 2.500)
  [m28 J-1 shift 2.500 rt] chain/passive worst 12.917 mean 13.281 | G4_A 1.589 / 1.633 | stage-2 floor cav -4.02 drn_h -4.31 mode -5.24 | eye +3.65 (n 36)
  [m28 J-1 shift 2.625 rt] chain/passive worst 12.917 mean 13.281 | G4_A 1.589 / 1.633 | stage-2 floor cav -4.02 drn_h -4.42 mode -5.46 | eye +3.65 (n 36)
    lo 0.77: floor cav -9.65 drn_h -9.39 mode -11.91 | chain 13.532 G4_A 1.664 (n 35)
    lo 0.80: floor cav -10.08 drn_h -10.09 mode -12.19 | chain 14.074 G4_A 1.731 (n 35)
=== cfl 0.8 at fixed N = 240, m=30 seed 7, J=-1, bias held at 0.7*M_th_num(240) (cfl 0.4)
  single cell Gw 8.5880; own passive env lag 2.6588 rt (rounds to 2.625); passive peak-time lag 0.5319 rt
  [cfl0.8 J-1 shift 0.000 rt] chain/passive worst 12.239 mean 12.831 | G4_A 1.425 / 1.494 | c2c 4.004 / 4.442 | stage-2 floor cav -2.40 drn_h -1.94 mode -1.68 | eye +1.79 (n 36)
  [cfl0.8 J-1 shift 2.625 rt] chain/passive worst 12.756 mean 13.167 | G4_A 1.485 / 1.533 | c2c 4.202 / 4.456 | stage-2 floor cav -3.37 drn_h -2.97 mode -3.49 | eye +2.95 (n 36)
real 0m23.225s

$ PYTHONDONTWRITEBYTECODE=1 python3 score3.py | grep -v <score2's re-printed lines>   (Table 3's sensitivity-row label: capped vs true active lag)
m=30 stage-2 shift 5.400 rt: chain worst 13.110 floor cav -6.33 eye +6.03 (n 36)
m=30 stage-2 shift 5.708 rt: chain worst 13.110 floor cav -6.33 eye +6.03 (n 36)
m=28 stage-2 shift 5.040 rt: chain worst 13.010 floor cav -5.70 eye +5.37 (n 36)
m=28 stage-2 shift 5.765 rt: chain worst 13.010 floor cav -5.70 eye +5.37 (n 36)

Every printed digit of the following reproduces:
- the gate row, the J = −1 chain, c2c and the stage-2 floors;
- Table 3c at lo 0.25, 0.30, 0.40, 0.58, 0.70, 0.75, 0.77, 0.80 and 0.85 (m = 30), 0.77 and 0.80 (m = 28), and cell 1 at 0.58 / 0.60;
- the ablation (including the rework's own gate (ii), −12.54 / −12.08 / −16.22);
- the cfl 0.8 row of the reply's cfl scan;
- item 8's slope and 18.4 dB;
- §1's channel-named gaps;
- the round-2 record's D3 seed identity (seed 11 re-executed here; seed 13 by round-1 Fabric);
- the D8 loop arithmetic.

TEXT AUDITS (commands and the output lines each finding rests on):

$ diff <(grep '^|' stage2-session/11-reply.md) <(grep '^|' stage4-rework/round-2-reply.md)
The output shows:
- lines 27–30 and 37–40 deleted: the Table 2a rows J = −10/−15/−20/−25 at m = 30 and m = 28;
- Table 3 replaced; in round 2 the m = 30 stage-4 row reads '| 30 | 4 | 5.40 | 4.748 / 4.886 | 0.828 / 0.855 | -1.04 / -2.78 | -2.58 | 0.356 | +0.90 | 2.3826 |', against round 1's '| 30 | 4 | 7.70 | 36 | 0.956 / 0.447; 0.109 | 4.773 / 4.899 | … | -1.12 / -3.72 | -2.97 | 0.330 | +0.99 | 2.3826 |';
- Table 3b deleted;
- the residue header and rows replaced by '| 30 | −11.78 dB (after a '1'); −36.3 (after a '0') | **−1.57 dB** (after a '1'); −25.9 (after a '0') | −5.70 dB | −10.6 / −13.8 dB | −4.31 dB (`drn_h`), −4.64 (`cav`) |' and '| 28 | −11.15 dB; −33.5 | **−0.98 dB**; −23.4 | −5.51 dB | −10.0 / −13.3 dB | −4.42 dB (`drn_h`), −4.02 (`cav`) |';
- Table 6 rows '30 (junction sweep)', '28 (junction sweep)' and '30 | 720' deleted;
- the grading rows changed as intended.
The rows of Tables 1, 2b and 5 are unchanged. I reproduce here only the lines each finding rests on; the full diff is ~150 lines of table rows.

$ ls -la --time-style=+%H:%M:%S session/tables_split.json stage2-session/listings/analyze_depth.py stage2-session/11-reply.md
06:40:37 tables_split.json | 07:18:41 analyze_depth.py | 07:18:42 11-reply.md

$ python3 -c "t=json.load(open('session/tables_split.json')); print(list(t.keys()))"
['TABLE1', 'TABLE2', 'TABLE4', 'TABLE6', 'TABLE5', 'TABLE3', 'RESIDUE']
(TABLE4 heading '### Junction sweep …'; TABLE6 heading '### Passive port-to-port density transfer and latency'; RESIDUE heading '### The residue the next cell actually receives …')

$ grep -n tables_split stage4-rework/listings/build_r2.py
176:tabs = json.load(open(S + "/tables_split.json")); tabs["TABLE3C"] = table3c(); tabs["TABLE7"] = table7(); tabs["ABLATION"] = ablation()

$ grep -n "min(sh\|cap" stage2-session/listings/analyze_depth.py
20:    """No cap on the shift: …
The shipped, post-check listing has no cap; 13-prepublication-checks.md:44 records the draft's `sh = min(sh, 0.9*repT − 0.72*repT)` = 0.18·repT = 5.40 / 5.04 rt.

$ python3 -c "print(len(open('stage4-rework/round-2-reply.md').read()))"
71594

$ grep counts in round-2-reply.md:
- 'released coupling': 1 (inside the disclosure's quotation);
- '44 dB': 3, 'half-step': 3, 'every placement': 2, 'own operating point': 1 (all as quotations of withdrawn text);
- 'Table 3b': 2 (no Table 3b present);
- 'Table 7': 14 (both meanings);
- 'eleven': 1;
- '24 matched': 1.

$ grep -n "9.4 Inter-cell junctions" scratchpad/partI.txt
330: 9.4 Inter-cell junctions. A junction is a gate-defined density step between adjacent segments. … the reflective loss of even a 2× density step is < 0.1 dB — the −1 to −3 dB budgeted per junction is therefore dominated by non-ideal effects: scattering at the gate gap, mode mismatch through the ungated sliver, and radiation. …

$ grep -n "14.73" notes/2026-08-12-gated-zero-residual-phasor.md
95: … `regen.loop_gain` at 0.7·`M_th_num`(240) predicts **−14.73 dB/slot** at m = 30 against a measured **−24.38**, a 9.6 dB/slot gap that closes only in the continuum …

$ sed -n 113-117p notes/2026-08-12-gated-zero-residual-phasor.md
SENSITIVITY, stated because it exceeds the band: at fixed grid the rl-1 amplitude moves 10.3 dB across cfl 0.2-0.8 (-22.53 -> -12.19 dB) and the decay 14.7 dB/slot; …

$ sed -n 79-83p notes/2026-08-12-gated-zero-residual-phasor.md
| 0.2 | … | −112.4463 | 13.20 | −33.677 | / | 0.4 | … | −118.9498 | 19.70 | −24.376 | / | 0.8 | … | −121.5014 | 22.25 | −18.989 |

$ grep -n "cfl law" notes/2026-08-13-walk-excess-clamp-placement.md
55: The operator reproduces **the cfl law** (0.59 → 0.86 → 1.01 against measured 0.587 → 0.876 → 0.989) — …
This is the phase-leg walk excess α.

$ grep -n knee_gated_duty0p8_streaming notes/2026-08-01-gated-requirement-round-trip.md
137: … = **0.01203** (gain-ratio) …
(its §5: 'The 07-17 knee convention biases at 0.7·M_th_num', i.e. the ratio bias)

$ sed -n 97-108p notes/2026-08-01-gated-requirement-round-trip.md
A_fix column: 0.01169 (m30/N240) … 0.01335 (m28/N480), 0.01387 (m28/N720), 0.01403 (m30/N480).

$ cat families.json families2.json families_720.json families_jext.json depth_cfgs.json; grep tags in rw_runs.py
No m = 26 run, no seed 17, no N = 960, no N = 720 at J = −1 or at m = 28, and no N = 480 at J ≤ −10: every §5 falsifier cell is absent from the campaign.

$ grep -rn -i "floor-optimal|window placement|sampling phase|decision window" notes/*.md
(no output)

$ head notes/2026-07-22-cavity-ringdown-isi.md / notes/2026-07-22-mth-numerical-vs-physical-viscosity.md
Both methods lines: 'Windows/CPython'.

Not re-executed by this seat (budget), so I accept no number from them:
- N = 480 / 720 rows, seed 13, J = 0 / −3 / −10 / −15 / −20 / −25;
- the whole cfl 0.2 row;
- Table 2b, the five-stage depth chain (Table 3 stages 3–5), the velocity-plane chain, and N = 720 1.687.
My findings on these rest only on the reply's own printed rows, and I say so where I use them.

$ cd /home/user/FableComputer && git status --porcelain | wc -l
0
```

</details>
