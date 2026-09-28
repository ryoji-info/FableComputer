# Round-3 rework record — Fable Session 2026-09-28 (paste after the round-2 vote records and before the round-3 reply)

**Round 2 tally: 0 store / 3 reject** (🧵 Fabric, 🌊 Kinetic, ⚛️ Quanta; `stage4-rework/round-2-{fabric,kinetic,quanta}.md`). Every seat reproduced every measured row (gate ≤ 1.3×10⁻¹³ relative; the J = −1 chain, Table 3c's optima, the cfl-0.8 row, ablation gate (i), the drain slope, the loop-model arithmetic and the seed-vs-rounding identity to the printed digit) and verified 20–22 of the 25 round-1 required edits as landed and the rest as partial. The rejection was earned by the text: **the round-2 builder (`build_r2.py`) filled the §3 table placeholders from `tables_split.json`, a file written before the pre-publication fixes**, so the round-2 text silently reverted Table 3 to the capped draft (5.40 / 5.04 rt at stages ≥ 3), the residue table to its pre-check form (the same-phase ratio in bold, no denominators), dropped Table 3b, eight small-signal rows of Table 2a and three family rows of Table 6, and lost the "Table 4" / "Table 6" headings — while the round-2 header said "no measured number changed" and the round-2 record said the tables were "byte-identical". Both statements were false as written and are withdrawn. The executor did not diff the built text against the published round-1 tables before posting it; the round-3 builder (`build_r3.py`) renders the tables fresh from `render_tables.py` and **asserts at build time** that Table 3 is uncapped and carries its lag and slot-count columns, that Table 3b exists, that Table 2a has ≥ 28 rows and Table 6 ≥ 11, that the residue table's bold value equals the registered key, that every "Table N" reference resolves to a heading, that no bare "Table 7" survives, and that no withdrawn phrase survives outside a disclosure sentence.

Per the routine's stage-4 rules every round-2 objection was collected verbatim and **re-executed against the released, unedited `fable-model-chain/` before acceptance**: `rw3_stored.py` (the degradation spans over every family and class; the loaded-drain loop model over three junction models, two reflection phases and both biases; the continuum estimates; the mean-'1' seed spread) and `rw3_runs.py` + `rw3_abl.py` (the hard-cut ablation, one new solver run); outputs appended verbatim. No Fable consult was spawned (no issue was hard by the routine's definition: every one was settled by rebuilding, by executing the released code or by relabelling). Session model `claude-fable-5-1`; platform Linux x86_64 / Python 3.11.15 / numpy 2.4.6.

**Outcome: all 29 required edits and every top issue reproduced; all applied; none declined.** One re-execution differs in magnitude from a seat's figure and is recorded as such (the hard-cut ablation, below).

## Issue by issue

| # | raised by | claim | re-executed — result | accepted / declined | where it landed (round-3 reply) |
|---|---|---|---|---|---|
| 1 | 🧵 RE1, 🌊 RE1, ⚛️ RE1–RE3 (T1–T3 all seats) | the §3 tables regressed to the pre-check set; Table 3 capped; residue table pre-fix; Tables 2a/6 lost rows; Table 3b missing; Tables 4/6 unnumbered; "no measured number changed" / "byte-identical" false | reproduced by reading `build_r2.py` line 176 and diffing the round-2 text against `11-reply.md`; the seats' own re-scoring (capped rows reproduce only at 5.40 / 5.04 rt, round 1's only at 7.70 / 10.27 rt) is consistent with `analyze_depth.py` as shipped | **accepted — the regression is disclosed, the tables rebuilt from the post-check source with assertions** | header (rework history); §3 in full; limitation 6; this record |
| 2 | 🧵 RE2, 🌊 RE1(e), ⚛️ RE4 | "Table 7" names both the cfl scan and Part I's bench-gate table | textual | **accepted** | the cfl scan is Table 8, the ablation Table 9; every manuscript reference reads "Part I Table 7" (asserted) |
| 3 | 🧵 RE3, 🌊 RE2, ⚛️ RE5 (T4 / T3 / T4) | the G4-bar and "≈ 2×" statements (item 1, §4 G4 row, item 6, title) carry no window scope; G4_A = 1.731 at the m = 28 placement that puts the floor on the round spec, 1.86 / 1.87 at lo 0.85 | `rw_window.py` (round 2): 1.630 (m = 30, lo 0.77), 1.731 (m = 28, lo 0.80), 1.862 / 1.873 (lo 0.85) — reproduced | **accepted** | item 1 (scope (c)); item 6; §4 G4 row; title; §0 "Scope, first" |
| 4 | 🧵 RE4, 🌊 RE3, ⚛️ RE6 (T5 / T4 / T5) | "7–9 dB" is not the measured range; the sign-off inverts the direction ("below" → shallower); "could build" → ran; cfl scope in the headline | `rw3_stored.py` (1): under the rule, peak `cav` 6.16–7.98 dB across Table 1's classes (6.16–8.11 over every Table 5 row; 7.13 / 6.71 at m = 30 / 28, J = −1), slot-mode 8.63–10.41; per-stage optima 9.28 / 9.06; cfl 0.8: -5.5 dB | **accepted** | title; item 4; §7 sign-off ("6–9 dB shallower"; "the one coupling this session ran") |
| 5 | 🧵 RE5, 🌊 RE4, ⚛️ RE10 (T6 / T5 / T7) | the loaded-drain figures assume a lossless junction that Part I §9.4 rules out (quote the full sentence); §9.4's bound |r| < 0.151 → loop ≤ 0.143, +0.04 dB, regen +0.30 dB; Quanta's 11.6 % → 0.322 / +1.54 / +0.83; the reflection phase is unstated (r = −|r| gives −3.53 dB delivered, regen −0.57; |loop| phase-independent); the ratio bias is one 08-12 registered as off by 9.6 dB/slot; the active delivered wave is +3.86 dB | `rw3_stored.py` (2): all figures reproduce — lossless 0.429 / +2.58 / +3.86 / +6.83 / +1.28 dB; §9.4 bound 0.143 / +0.04 / +0.34 / +0.30; 11.6 % 0.322 / +1.54 / +2.37 / +0.83; r = −|r|: −3.53 / −4.10 / −0.57; loop 0.945 → −14.73 dB/slot vs measured −24.38 (effective 0.911), analytic 0.916 → −22.81; §9.4 full sentence verified in the extracted Part I text | **accepted** | item 2 (the range, the full §9.4 quote, the phase and bias caveats); item 3; item 5 (active +3.9 dB / +0.3 dB); §2 bullet 2; §4 row 1; §5 passive-transfer key; limitation 1 |
| 6 | 🧵 RE6 (T7), 🌊 T11 (optional), ⚛️ T12 (optional) | the discriminant files the loaded junction under "> 1.7" although the loaded chain reads G4 ≈ 1.10 in CW form; the cfl lever reaches the "> 1.7" and "deeper than −8" readings at cfl 0.2; denominate the floor band; state the continuum estimate beside the band | `rw3_stored.py` (2), (3): CW-form G4 of the loaded chain 1.10 (lossless) / 1.02 (§9.4) / 1.06 (11.6 %); continuum estimates 1.425 / 1.459; Table 8 spans 1.485–1.774 and −3.37…−8.35 dB | **accepted** | §5 discriminant: loaded junction moved to the "< 1.40" reading; "> 1.7" for a link that re-normalizes without loading; released-cfl-path caveat; peak-`cav` denomination; continuum estimate beside the band |
| 7 | 🧵 RE7(a), 🌊 RE5 (T6), ⚛️ RE9 (T6) | limitation 4 mis-attributes the cfl movement to 08-13's law (a phase-leg law, cfl-independent at M = 0); the single-cell cfl column re-announces 08-12's registered sensitivity (−22.53 → −12.19 dB; decay −33.677 / −24.376 / −18.989) without credit | 08-13 §3 and 08-12 §3 / the registered key text re-read; the scan's cell-1 slot-mode column −22.41 / −15.66 / −11.66 compared with 08-12's phasor amplitude (a different statistic, same bias) | **accepted** | limitation 4 rewritten; item 4 (ii) credits 08-12; Table 8 caption |
| 8 | 🧵 RE7(c), 🌊 RE6, ⚛️ RE8 (T8) | citation globs; 07-22-viscosity missing from the filename block | `ls notes/`: `2026-07-31-physical-launch-gated-frontier.md`, `2026-08-08-augmented-solver-decisive-experiment.md`, `2026-07-22-mth-numerical-vs-physical-viscosity.md` exist | **accepted** | "Record cited, by filename" block |
| 9 | 🧵 RE8 (T9) | the f_max grade ignores the single-cell window finding (cell 1's floor −11.83 → −20.14 at lo 0.58; clears the strict anchor at a later window at both rungs) | `rw_window.py` (round 2) cell-1 column: −20.14 (m = 30, lo 0.58) / −19.14 (m = 28, lo 0.60) — reproduced | **accepted, labelled in-model / open, no key moved** | item 5; §4 f_max row |
| 10 | 🧵 RE9, ⚛️ RE7 | Table 1's caption still says "[min, max over seeds 7/11/13]"; §1's window bullet quotes only ≈ 0.1 dB / 0.012; restrict "identical" to worst-'1' | `rw3_stored.py` (4): worst-'1' 13.1028 / 13.1029 / 13.1028 (identical to ≤ 0.001 dB); mean-'1' 13.399 / 13.443 / 13.409 (≤ 0.05 dB) | **accepted** | Table 1 caption (relabelled in `render_tables.py`); §1 window bullet; item 1 (a) |
| 11 | 🧵 RE10, 🌊 RE7, ⚛️ RE12 (T10 / T7 / T9) | 71,594 characters exceeds GitHub's comment limit and the script's 60,000-character read; name a split point or trim | `wc -c`: precedent notes run 32k–152k characters (08-13: 78k; 08-02: 152k), so the note length is not the constraint; the paste is | **accepted** | an explicit two-comment split after §3 (comment A 59,510 characters, comment B 20,193; asserted < 60,000 each); Tables 2b and 5 moved to `round-3-tables-appendix.md` for the listings comment |
| 12 | 🌊 T10, ⚛️ RE11 (T8) | the ablation's gate (ii) construction is unstated; a hard cut reads −13.09 / −12.64 / −16.82 (⚛️'s run); the split is ≈ 60 : 40, not "half and half" | `rw3_runs.py` + `rw3_abl.py`: a hard cut of the '1' slots at 0.8·repT with every '0' slot zeroed reads **-13.81 / -13.36 / -17.53 dB** here (chain 13.131, eye +13.52); the raised-cosine variant −12.54 / −12.08 / −16.22 reproduces the round-2 figure; the '0'-residue share is ≈ 4.7 dB and the '1'-tail share 3.2–4.4 dB, construction-dependent — **the seat's −13.09 is not reproduced by this construction (it presumably kept the raised-cosine '0' cut), and the value is quoted as measured here** | **accepted, constructions named** | item 4; Table 9 |
| 13 | 🧵 T12 (optional) | A_fix's full span is 0.00763–0.01403 | 08-01 gated §4's table re-read: 0.00763 (m = 22 / N = 480) … 0.01403 | **accepted** | item 3 |
| 14 | ⚛️ T11 (optional) | the latency excess may be the detuned-resonator steady-state phase | not checked (an in-model hypothesis, not a measurement) | **noted with credit, not adopted as a claim** | item 7 |
| 15 | 🌊 T13 (adoptable) | run the loaded junction in the time domain (a partially reflecting drain at |r| = 0.454 and 0.151) | not run: it is a new instrument (a modified drain closure in the released stepper), not a re-execution, and the round cap is one round away | **declined for this session, named as the deciding experiment** | item 2; limitation 1 |
| 16 | ⚛️ T13 (adoptable) | build-time assertions on the rework builder | implemented in `build_r3.py` | **adopted** | this record |

**What was withdrawn in round 3.** (a) The round-2 header's "No measured number changed" and the round-2 record's "every table … byte-identical" — false for the round-2 text as built. (b) "7–9 dB" as the degradation range. (c) The loaded junction as a "> 1.7×" reading of the discriminant. (d) The attribution of Table 8's movement to 08-13's cfl law. Nothing measured was withdrawn; no verdict reversed.

**What was not changed, and why.** Every table of the *published round-1* text is byte-identical in round 3 except Table 1's caption (relabelled, values unchanged) and the "Table 4" / "Table 6" numbering; the round-2 text's tables are superseded in full. The seats' own instruments reproduced every measured row in both rounds.

**Fable 5 consult:** none spawned (0 of the routine's ≤ 2 per run).

## Re-execution outputs, verbatim

### `rw3_stored.py` (degradation spans, the loaded-drain model over junction / phase / bias, continuum estimates, mean-'1' seed spread)

```text
=== (1) floor degradation cell 1 -> stage 2 under the rule window (peak cav; slot-mode drn_h), by family and class
 N240_m28_s11     J=+0: peak cav -10.74 -> -4.22 = -6.52 dB; slot-mode -14.59 -> -5.38 = -9.21 dB
 N240_m28_s11     J=-1: peak cav -10.74 -> -4.07 = -6.67 dB; slot-mode -14.59 -> -5.20 = -9.39 dB
 N240_m28_s11     J=-3: peak cav -10.74 -> -3.72 = -7.02 dB; slot-mode -14.59 -> -4.84 = -9.75 dB
 N240_m28_s11     J=-6: peak cav -10.74 -> -3.24 = -7.50 dB; slot-mode -14.59 -> -4.43 = -10.16 dB
 N240_m28_s13     J=+0: peak cav -10.77 -> -4.19 = -6.58 dB; slot-mode -14.66 -> -5.40 = -9.26 dB
 N240_m28_s13     J=-1: peak cav -10.77 -> -4.04 = -6.74 dB; slot-mode -14.66 -> -5.23 = -9.43 dB
 N240_m28_s13     J=-3: peak cav -10.77 -> -3.68 = -7.09 dB; slot-mode -14.66 -> -4.89 = -9.77 dB
 N240_m28_s13     J=-6: peak cav -10.77 -> -3.22 = -7.55 dB; slot-mode -14.66 -> -4.55 = -10.11 dB
 N240_m28_s7      J=+0: peak cav -10.73 -> -4.18 = -6.56 dB; slot-mode -14.61 -> -5.41 = -9.20 dB
 N240_m28_s7      J=-1: peak cav -10.73 -> -4.02 = -6.71 dB; slot-mode -14.61 -> -5.24 = -9.37 dB
 N240_m28_s7      J=-3: peak cav -10.73 -> -3.67 = -7.06 dB; slot-mode -14.61 -> -4.90 = -9.71 dB
 N240_m28_s7      J=-6: peak cav -10.73 -> -3.21 = -7.52 dB; slot-mode -14.61 -> -4.51 = -10.10 dB
 N240_m30_s11     J=+0: peak cav -11.84 -> -4.82 = -7.02 dB; slot-mode -15.66 -> -6.39 = -9.27 dB
 N240_m30_s11     J=-1: peak cav -11.84 -> -4.74 = -7.10 dB; slot-mode -15.66 -> -6.25 = -9.41 dB
 N240_m30_s11     J=-3: peak cav -11.84 -> -4.51 = -7.34 dB; slot-mode -15.66 -> -5.90 = -9.75 dB
 N240_m30_s11     J=-6: peak cav -11.84 -> -4.15 = -7.70 dB; slot-mode -15.66 -> -5.47 = -10.19 dB
 N240_m30_s13     J=+0: peak cav -11.85 -> -4.76 = -7.09 dB; slot-mode -15.69 -> -6.30 = -9.39 dB
 N240_m30_s13     J=-1: peak cav -11.85 -> -4.65 = -7.20 dB; slot-mode -15.69 -> -6.15 = -9.54 dB
 N240_m30_s13     J=-3: peak cav -11.85 -> -4.34 = -7.51 dB; slot-mode -15.69 -> -5.82 = -9.88 dB
 N240_m30_s13     J=-6: peak cav -11.85 -> -3.87 = -7.98 dB; slot-mode -15.69 -> -5.41 = -10.28 dB
 N240_m30_s7      J=+0: peak cav -11.83 -> -4.78 = -7.05 dB; slot-mode -15.66 -> -6.40 = -9.27 dB
 N240_m30_s7      J=-1: peak cav -11.83 -> -4.70 = -7.13 dB; slot-mode -15.66 -> -6.26 = -9.41 dB
 N240_m30_s7      J=-3: peak cav -11.83 -> -4.46 = -7.37 dB; slot-mode -15.66 -> -5.93 = -9.74 dB
 N240_m30_s7      J=-6: peak cav -11.83 -> -4.10 = -7.73 dB; slot-mode -15.66 -> -5.51 = -10.15 dB
 N480_m28_s7      J=+0: peak cav -10.40 -> -4.24 = -6.16 dB; slot-mode -14.09 -> -5.46 = -8.63 dB
 N480_m28_s7      J=-1: peak cav -10.40 -> -4.08 = -6.32 dB; slot-mode -14.09 -> -5.30 = -8.79 dB
 N480_m28_s7      J=-3: peak cav -10.40 -> -3.74 = -6.67 dB; slot-mode -14.09 -> -4.95 = -9.14 dB
 N480_m28_s7      J=-6: peak cav -10.40 -> -3.23 = -7.18 dB; slot-mode -14.09 -> -4.52 = -9.57 dB
 N480_m30_s7      J=+0: peak cav -11.46 -> -4.80 = -6.66 dB; slot-mode -15.14 -> -6.17 = -8.98 dB
 N480_m30_s7      J=-1: peak cav -11.46 -> -4.70 = -6.76 dB; slot-mode -15.14 -> -6.03 = -9.11 dB
 N480_m30_s7      J=-3: peak cav -11.46 -> -4.45 = -7.01 dB; slot-mode -15.14 -> -5.71 = -9.43 dB
 N480_m30_s7      J=-6: peak cav -11.46 -> -4.06 = -7.41 dB; slot-mode -15.14 -> -5.29 = -9.85 dB
 N720_m30_s7      J=-3: peak cav -11.32 -> -4.48 = -6.84 dB; slot-mode -14.94 -> -5.61 = -9.33 dB
 N720_m30_s7      J=-6: peak cav -11.32 -> -4.10 = -7.22 dB; slot-mode -14.94 -> -5.20 = -9.74 dB
 Table-1 classes (J >= -6): peak cav -7.98 .. -6.16 dB (min N240_m30_s13 J=-6, max N480_m28_s7 J=0); slot-mode -10.28 .. -8.63
 all Table-5 rows incl. the sweep: peak cav -8.11 .. -6.16; slot-mode -10.41 .. -8.63
=== (2) loaded-drain loop model (released regen.loop_gain), in-model
 a_loss 0.745152; loop0 (M=0) 0.7452; unloaded loops: ratio bias 0.7*M_th_num(240) 0.9450; analytic bias 0.7*M_th 0.9162; unloaded CW regen (ratio) +13.32 dB, (analytic) +9.66 dB
 08-12 §3 check: loop 0.9450 per round trip -> per slot (m=30, 30 rt): -14.73 dB/slot; measured -24.38 dB/slot -> effective loop 0.9107; analytic loop -> -22.81 dB/slot
 J=-1 lossless junction, |r|^2 = 1 - 10^ ratio bias 0.7*M_th_nu r=+|r|: |r|=0.454 loaded loop +0.429; passive delivered +2.58 dB, active delivered +3.86 dB, drain standing wave +6.83 dB; loaded CW regen +1.28 dB (unloaded +13.32); CW-form G4 of the loaded chain 1.10
 J=-1 lossless junction, |r|^2 = 1 - 10^ ratio bias 0.7*M_th_nu r=-|r|: |r|=0.454 loaded loop -0.429; passive delivered -3.53 dB, active delivered -4.10 dB, drain standing wave -7.78 dB; loaded CW regen -0.57 dB (unloaded +13.32); CW-form G4 of the loaded chain 0.96
 J=-1 lossless junction, |r|^2 = 1 - 10^ analytic bias 0.7*M_th r=+|r|: |r|=0.454 loaded loop +0.416; passive delivered +2.58 dB, active delivered +3.66 dB, drain standing wave +6.83 dB; loaded CW regen +1.08 dB (unloaded +9.66); CW-form G4 of the loaded chain 1.11
 J=-1 lossless junction, |r|^2 = 1 - 10^ analytic bias 0.7*M_th r=-|r|: |r|=0.454 loaded loop -0.416; passive delivered -3.53 dB, active delivered -4.02 dB, drain standing wave -7.78 dB; loaded CW regen -0.49 dB (unloaded +9.66); CW-form G4 of the loaded chain 0.95
 J=-1 Part I 9.4 bound: reflective loss  ratio bias 0.7*M_th_nu r=+|r|: |r|=0.151 loaded loop +0.143; passive delivered +0.04 dB, active delivered +0.34 dB, drain standing wave +2.26 dB; loaded CW regen +0.30 dB (unloaded +13.32); CW-form G4 of the loaded chain 1.02
 J=-1 Part I 9.4 bound: reflective loss  analytic bias 0.7*M_th r=+|r|: |r|=0.151 loaded loop +0.138; passive delivered +0.04 dB, active delivered +0.29 dB, drain standing wave +2.26 dB; loaded CW regen +0.26 dB (unloaded +9.66); CW-form G4 of the loaded chain 1.03
 J=-1 Quanta 09-28 budget |r|^2 <= 11.6  ratio bias 0.7*M_th_nu r=+|r|: |r|=0.341 loaded loop +0.322; passive delivered +1.54 dB, active delivered +2.37 dB, drain standing wave +5.09 dB; loaded CW regen +0.83 dB (unloaded +13.32); CW-form G4 of the loaded chain 1.06
 J=-1 Quanta 09-28 budget |r|^2 <= 11.6  analytic bias 0.7*M_th r=+|r|: |r|=0.341 loaded loop +0.312; passive delivered +1.54 dB, active delivered +2.25 dB, drain standing wave +5.09 dB; loaded CW regen +0.71 dB (unloaded +9.66); CW-form G4 of the loaded chain 1.07
 J=-3 lossless junction, |r|^2 = 1 - 10^ ratio bias 0.7*M_th_nu r=+|r|: |r|=0.706 loaded loop +0.667; passive delivered +3.49 dB, active delivered +6.56 dB, drain standing wave +11.13 dB; loaded CW regen +3.07 dB (unloaded +13.32); CW-form G4 of the loaded chain 1.23
 J=-3 lossless junction, |r|^2 = 1 - 10^ analytic bias 0.7*M_th r=+|r|: |r|=0.706 loaded loop +0.647; passive delivered +3.49 dB, active delivered +6.05 dB, drain standing wave +11.13 dB; loaded CW regen +2.56 dB (unloaded +9.66); CW-form G4 of the loaded chain 1.26
 J=-3 Part I 9.4 bound: reflective loss  ratio bias 0.7*M_th_nu r=+|r|: |r|=0.151 loaded loop +0.143; passive delivered -1.96 dB, active delivered -1.66 dB, drain standing wave +2.26 dB; loaded CW regen +0.30 dB (unloaded +13.32); CW-form G4 of the loaded chain 1.02
 J=-3 Part I 9.4 bound: reflective loss  analytic bias 0.7*M_th r=+|r|: |r|=0.151 loaded loop +0.138; passive delivered -1.96 dB, active delivered -1.71 dB, drain standing wave +2.26 dB; loaded CW regen +0.26 dB (unloaded +9.66); CW-form G4 of the loaded chain 1.03
 J=-3 Quanta 09-28 budget |r|^2 <= 11.6  ratio bias 0.7*M_th_nu r=+|r|: |r|=0.341 loaded loop +0.322; passive delivered -0.46 dB, active delivered +0.37 dB, drain standing wave +5.09 dB; loaded CW regen +0.83 dB (unloaded +13.32); CW-form G4 of the loaded chain 1.06
 J=-3 Quanta 09-28 budget |r|^2 <= 11.6  analytic bias 0.7*M_th r=+|r|: |r|=0.341 loaded loop +0.312; passive delivered -0.46 dB, active delivered +0.25 dB, drain standing wave +5.09 dB; loaded CW regen +0.71 dB (unloaded +9.66); CW-form G4 of the loaded chain 1.07
 J=-6 lossless junction, |r|^2 = 1 - 10^ ratio bias 0.7*M_th_nu r=+|r|: |r|=0.865 loaded loop +0.818; passive delivered +2.99 dB, active delivered +8.79 dB, drain standing wave +14.41 dB; loaded CW regen +5.80 dB (unloaded +13.32); CW-form G4 of the loaded chain 1.44
 J=-6 lossless junction, |r|^2 = 1 - 10^ analytic bias 0.7*M_th r=+|r|: |r|=0.865 loaded loop +0.793; passive delivered +2.99 dB, active delivered +7.67 dB, drain standing wave +14.41 dB; loaded CW regen +4.68 dB (unloaded +9.66); CW-form G4 of the loaded chain 1.48
 J=-6 Part I 9.4 bound: reflective loss  ratio bias 0.7*M_th_nu r=+|r|: |r|=0.151 loaded loop +0.143; passive delivered -4.96 dB, active delivered -4.66 dB, drain standing wave +2.26 dB; loaded CW regen +0.30 dB (unloaded +13.32); CW-form G4 of the loaded chain 1.02
 J=-6 Part I 9.4 bound: reflective loss  analytic bias 0.7*M_th r=+|r|: |r|=0.151 loaded loop +0.138; passive delivered -4.96 dB, active delivered -4.71 dB, drain standing wave +2.26 dB; loaded CW regen +0.26 dB (unloaded +9.66); CW-form G4 of the loaded chain 1.03
 J=-6 Quanta 09-28 budget |r|^2 <= 11.6  ratio bias 0.7*M_th_nu r=+|r|: |r|=0.341 loaded loop +0.322; passive delivered -3.46 dB, active delivered -2.63 dB, drain standing wave +5.09 dB; loaded CW regen +0.83 dB (unloaded +13.32); CW-form G4 of the loaded chain 1.06
 J=-6 Quanta 09-28 budget |r|^2 <= 11.6  analytic bias 0.7*M_th r=+|r|: |r|=0.341 loaded loop +0.312; passive delivered -3.46 dB, active delivered -2.75 dB, drain standing wave +5.09 dB; loaded CW regen +0.71 dB (unloaded +9.66); CW-form G4 of the loaded chain 1.07
=== (3) first-order continuum estimate of G4_A at J=-1 from (240, 480): 2*G(480) - G(240)
 m=30: 1.581 / 1.503 -> 1.425
 m=28: 1.589 / 1.524 -> 1.459
=== (4) seed spread of the mean-'1' chain gain at a fixed placement (2.625 rt), m=30 N=240 J=-1
 N240_m30_s7: worst 13.1028 mean 13.3987
 N240_m30_s11: worst 13.1029 mean 13.4425
 N240_m30_s13: worst 13.1028 mean 13.4085
```

### `rw3_runs.py` + `rw3_abl.py` (the hard-cut ablation)

```text
hard-cut ablation run done 51.2 s Linux x86_64, Python 3.11.15, numpy 2.4.6
hard cut at 0.8*repT (and every '0' slot zeroed): floor_cav -13.807 floor_drnh -13.363 floor_mode -17.527 chain 13.131 eye +13.523
```
