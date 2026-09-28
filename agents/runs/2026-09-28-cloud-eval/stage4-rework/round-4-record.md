# Round-4 rework record — Fable Session 2026-09-28 (paste after the round-3 vote records and before the round-4 reply; round 4 is the routine's cap)

**Round 3 tally: 3 store / 0 reject, all with required edits** (🧵 Fabric 6, 🌊 Kinetic 8, ⚛️ Quanta 5; `stage4-rework/round-3-{fabric,kinetic,quanta}.md`). All three seats verified the round-2 regression repaired (every published round-1 table row back, byte-identical), reproduced every decisive number on their own instruments (gate ≤ 1.3×10⁻¹³ relative; the J = −1 chain; Table 3c's rows; Table 8's cfl-0.2 row; the N = 480 rung and the continuum estimate; the loop-model range over junction, phase and bias; ablation rows), and verified 25–26 of the 29 round-2 edits as landed and the rest as partial. What remained was mechanical, and the routine's round-4 rule — prefer scope reduction over a further repair — was applied where a claim could not be supported as stated (the late-window "bar crossed" statement, item 3 below).

Per the stage-4 rules every round-3 objection was collected verbatim and **re-executed against the released, unedited `fable-model-chain/` before acceptance**: `rw4_stored.py` (the matched-window G4 scan on the depth series; the loop model's full range and |r| → 0 limit; the passive peak-to-peak latency across all families; the continuum estimate's rounding), `rw4_runs.py` (the ablation construction Table 9's row (iii) had been labelled with — one new solver run) and `rw4_merge.py` (re-scoring both hard-cut series without side effects, after `rw4_runs.py`'s import of `rw_cfl.py` had re-run that module and dropped a key from `cfl_scan.json` — disclosed). Outputs appended verbatim. No Fable consult was spawned. Session model `claude-fable-5-1`; platform Linux x86_64 / Python 3.11.15 / numpy 2.4.6.

**Outcome: all 19 required edits and every top issue reproduced; all applied; none declined.** One claim was withdrawn as a measured statement and rescoped (item 3). The builder's assertions were extended (every "Table N" occurrence resolves; Table 9 has its five rows; no stale round-3 phrase survives; the appendix is rendered fresh with its captions).

## Corrections to the round-3 record (that record is not edited; the corrections are recorded here)

- Its row 5 said ⚛️ RE10 was applied in full; the second assumption that edit named — the released DS drain factor (1 + M)/(1 − M) kept at a transmitting drain — was **not** named in the round-3 text. It is now (item 2, §2, limitation 1).
- Its row 12 said the round-2 seats' −13.09 dB "is not reproduced by this construction". The construction the round-3 Table 9 row (iii) was *labelled* with — gate (i)'s raised-cosine '0' cut plus a hard cut of the '1' slots at 0.8·repT — **does** reproduce it: re-executed here at **-13.086 / -12.638 / -16.820 dB** (chain 13.131, eye +12.80). The value printed under that label in round 3 (−13.81 / −13.36 / −17.53) was the construction `rw3_runs.py` actually ran — every '0' slot zeroed hard, plus the hard '1' cut — re-scored here at -13.807 / -13.363 / -17.527. Both rows are now printed with their constructions (rows iii and iv).
- Its "What was not changed" paragraph said the tables were byte-identical except Table 1's caption and the Table 4 / 6 numbering: Tables 4 and 6 were already numbered in round 1, and appendix Table 5's caption had lost its window-rule scope in the move (now restored and extended); its "never from the stale `tables_split.json`" was inaccurate for appendix Table 5 (rows verified identical; now rendered fresh by `render_tables.py`, asserted).
- Its "all 29 required edits … applied" was overstated by the items above (🧵 RE4, 🌊 RE3 / RE4, ⚛️ RE6 / RE10 landed partially, as the round-3 seats found).

## Issue by issue

| # | raised by | claim | re-executed — result | accepted / declined | where it landed (round-4 reply) |
|---|---|---|---|---|---|
| 1 | 🧵 RE1, 🌊 RE1, ⚛️ RE1 (T2 / T1 / T1) | Table 9 row (iii) prints a different construction than its label; the '1'-tail share is 3.2–3.7 dB with the '0' gate held at (i), and the 0.72 dB beyond it belongs to the '0' slot's first round trip (gate (i) passes ≈ 83 % of amplitude at the residue peak) | `rw4_runs.py`: the labelled construction reads -13.086 / -12.638 / -16.820 (the round-2 seats' −13.09 reproduced); `rw4_merge.py`: the executed construction -13.807 / -13.363 / -17.527; shares 3.16 (raised-cosine) / 3.71 (hard) dB for the '1' tail and 4.68 dB for the '0' residue under gate (i), +0.72 with the first round trip removed | **accepted** | Table 9 (five rows, constructions named); item 4 (shares restated: '1' tail 3.2–3.7 dB; '0' residue ≈ 4.7 dB under gate (i), a lower bound) |
| 2 | 🧵 RE2 (T3) | the `cascade2_G4_worst1_ratio_J1` lever clause "exits the band on both sides" is false (1.485 at cfl 0.8 is inside [1.40, 1.65]) | Table 8 rows re-read: 1.774 / 1.581 / 1.485 | **accepted** | §5 J1 key ("exits the band above at cfl = 0.2 while 1.485 at cfl = 0.8 stays inside"; the placement lever exits above only); the residue key's "both sides" (−8.11 / −4.21 vs [−7.0, −4.5]) is correct and stays |
| 3 | ⚛️ RE2 (T2) | the late-window "bar crossed" claim is a mixed-window ratio (chain at a late window over the single cell at the promoted window) and a plateau-edge lattice point; under the pinned convention the matched G4 at every round-spec placement is 1.606–1.624 (m = 30) / 1.631–1.695 (m = 28), below 1.7; matched G4 crosses 1.7 only where the floor fails the round spec | `rw4_stored.py` (1) on the depth series, 0.0025-slot lattice: round-spec placements lo 0.74–0.79 (m = 30) with matched G4 1.606–1.624 and lo 0.7925–0.8175 (m = 28) with 1.634–1.695; matched ≥ 1.7 only at lo ≥ 0.8075 (m = 30, floors −7.3 to −8.6) and lo = 0.83 (m = 28, floor −8.4); the m = 28 plateau reads 1.664 at lo 0.7925–0.795 and 1.731 at lo ≥ 0.80 in the mixed ratio — **reproduced** | **accepted — the claim is rescoped (scope reduction): no placement at J = −1 gives both a round-spec floor and G4 ≥ 1.7** | item 1(c); item 6; §4 G4 row; §5 discriminant and J1 key; limitation 6; new Table 3d (the matched scan) and Table 3c's caption ("a mixed ratio") |
| 4 | 🧵 RE3, ⚛️ RE3 (T4 / T3) | the bound direction is inverted (the lossless junction is the *least* loading; it bounds the loaded loop and the delivered drive from above); §9.4's figures are upper bounds, so "+0.04 to +2.6 dB" prints two upper bounds as a range; |r| → 0 gives −1.0 dB delivered, and §9.4's bound in the other phase −1.9 dB | `rw4_stored.py` (2): at J = −1, open-end phase, the delivered drive runs −1.00 dB (|r| → 0) … +2.58 dB (lossless), the loaded loop 0 … 0.429; §9.4 bound +0.04 (upper); other phase −3.53 (lossless) / −1.93 (§9.4); over J ∈ {−1, −3, −6} and both phases −10.32 … +3.49 dB | **accepted** | item 2 (direction corrected; the range stated as −1.0 to +2.6 dB at J = −1, open-end phase, "< +0.04 dB for any junction §9.4 allows"); item 3; §2; §4 row 1; §5 passive-transfer key; limitation 1 |
| 5 | 🧵 RE4, 🌊 RE5, ⚛️ RE4 (T5 / T4 / T4) | the loaded-loop model's second assumption — the released DS drain factor (1 + M)/(1 − M) kept at a transmitting drain — is unnamed | the formula in `rw3_stored.py` / `rw4_stored.py` is `regen.loop_gain(M) × |r|` — confirmed by reading | **accepted, named in-model / open** | item 2; §2 bullet 2; limitation 1 |
| 6 | 🌊 RE4 (T4) | the copies of the range in item 3, §4 row 1 and the §5 key carry no J = −1 / open-end-phase scope; "between the two" is false outside it | `rw4_stored.py` (2): outside that scope the model gives −3.53 (J = −1, r = −|r|), −1.96 / −4.96 (§9.4 bound, J = −3 / −6), +3.49 (lossless, J = −3) | **accepted** | every copy now reads "−1.0 to +2.6 dB at J = −1, open-end phase (−3.5 dB in the other; < +0.04 dB under §9.4's bound) — near the booked link, far from the ideal buffer" |
| 7 | 🧵 RE5, 🌊 RE3, ⚛️ (T6 / T3 / T8c) | the title's "9–10 dB (slot-mode)" rounds 8.63 up; the sign-off's "6–9 dB" names no denomination or placement; "-5.5 dB at cfl 0.8" has a stray sign; the cfl-0.2 escape is slot-mode only; "only" ranges over the levers tested | `rw3_stored.py` (1) (round 3): slot-mode 8.63–10.41 dB; peak 6.16–8.11; Table 8: at cfl 0.2 the rule-window peak floor is −8.35 (fails), slot-mode −11.65 (passes) | **accepted** | title; item 4's lead; §7 sign-off ("6.2–8.1 dB shallower … in peak `cav` under the promoted rule (9.1–9.3 dB at the lattice-optimal placements)"); item 4's cfl-0.8 figure as a positive degradation |
| 8 | 🧵 RE6 (T7) | the latency key's "0.523–0.525 rt" omits its own N = 720 row (0.518); the excess moves with N (0.024 → 0.022 → 0.018 rt) | `rw4_stored.py` (3): peak passive 0.5250 / 0.5243 (N = 240), Table 6's 0.523 (N = 480) and 0.518 (N = 720) | **accepted** | item 7; §5 latency key (0.518–0.525 rt; excess 0.018–0.025 rt across the grid ladder) |
| 9 | 🌊 RE2 (T2) | the residue caption's "(a) = … the promoted floor key's own denominator" is the plane mislabel ⚛️'s round-1 R4 withdrew (the promoted key is the source-plane `cav` ratio) | 08-02 §3.1 / §3.2 re-read; cell 1 at m = 28: `cav` −10.7312 vs `drn_h` −11.1506 | **accepted** | residue caption in `render_tables.py` ("the denominator of 08-02 §3.2's `drn_h` floor column, not of the promoted `max0_below_mean1_dB`") |
| 10 | 🌊 RE6 (T5) | limitation 9 lists 07-22's flush-sufficiency question as open; the record resolved it (07-22's post-promotion annotation; 07-22-flush; 07-23) | `notes/INDEX.md` rows 41–44 re-read: "✅ §7.3's sufficiency question resolved — passive flush insufficient (07-22 flush) and no de-Q rate closes flushed F = 2 at 4 ps (07-23 …)" | **accepted** | limitation 9 rewritten |
| 11 | 🌊 RE7, 🌊 RE8, ⚛️ RE5 (T6 / T5) | appendix Table 5 lost its window-rule caption and states neither coupling nor cfl; Table 2b's "same convention" dangles; the builder sourced Table 5 from the stale split file | `render_tables.py` now prints Table 5 as its own section with the round-1 scope plus the coupling, cfl and the cell-1 columns' window, and spells out Table 2b's convention; the 42 rows are asserted identical to the published ones (`rw4`: "identical: True") | **accepted** | `round-4-tables-appendix.md`; `render_tables.py` (re-shipped in the stage-2 listings) |
| 12 | 🧵 T11, ⚛️ T8(a)(d), 🌊 T11 (optional) | limitation 4's "p = 0.55–0.89" omits m = 26's 0.14; limitation 5's "Table 2" → "Table 2a"; the continuum estimate 1.4245 rounds to 1.42, not 1.43; "floor-optimal" → "lattice-optimal" for the unscanned cell-1 optimum; "8.0 at m = 30 / N = 240 / J = −6" is seed 13's row | 08-02 §4 key text: 0.71 / 0.55 / 0.14 / 0.89; `rw4_stored.py` (4): 1.4245 / 1.4588 | **accepted** | limitations 4 and 5; items 1, 4, 5; §5 J1 key and discriminant (1.42 / 1.46; "a reading of 1.38–1.42") |
| 13 | 🧵 T8 (optional) | say that the loop model itself expects the "< 1.40" arm for a passive-junction die, so a reading inside the band is the ideal buffer's expected outcome, not the loop model's | textual (item 2's own result) | **accepted** | §5 discriminant |
| 14 | 🌊 T5 (optional) | cite 08-12's window-scoped falsifier clause beside item 5 | 08-12 line 128: the early sub-window [0.25, 0.45]·repT | **accepted** | item 5 |
| 15 | 🌊 T7, 🌊 T9, ⚛️ T8(e)(g)(i), 🧵 T10 (optional) | the note build must carry the appendix and account for the script's 60,000-character read; state the CW-form G4 formula; name the cfl lever in the §4 G4 row; §9.4's third sentence; the rework listings' paste location | noted | **carried to `PASTE-ORDER.md` and the promotion step**, not into the reply text (the CW-form formula is already in item 2's parenthetical) | `PASTE-ORDER.md` |
| 16 | 🌊 RE8 | correct the round-3 record | — | **accepted** | the "Corrections to the round-3 record" section above |

**What was withdrawn in round 4.** The statement that Table 3c's late-window ratio "crosses the bar at J = −1" as a measured crossing: it is a mixed ratio at a plateau edge, and the matched ratio does not cross at any round-spec placement (item 3). Nothing measured was withdrawn; no verdict reversed.

**What was not changed, and why.** Every table of the published round-1 text is byte-identical in round 4 except Table 1's caption (relabelled, values unchanged), Table 2b's caption (its convention spelled out), Table 5's caption (its scope restored and extended) and the residue caption (denominator (a) re-described); Tables 3c, 8 and 9 and the new Table 3d are the rework's own additions. Nothing measured moved.

**Fable 5 consult:** none spawned (0 of the routine's ≤ 2 per run).

## Re-execution outputs, verbatim

### `rw4_stored.py` (matched-window G4, the loop model's full range, the latency ladder, the continuum rounding)

```text
=== D_N240_m30_s7: single-cell worst-'1' cav gain (promoted window) 8.2879; '1'-peak position in slot: cell 1 0.721, stage 2 0.808
  lo   | cell 1 alone: floor cav / drn_h / mode (n) | stage 2 chain: worst gain, G4_A | floor cav / drn_h / mode (n) | eye
  0.25 |  -11.83 /  -11.78 /  -15.66 (36) | 12.734, 1.537 |   -3.56 /   -3.09 /   -4.10 (36) | +3.15
  0.30 |  -12.73 /  -13.11 /  -17.26 (36) | 13.000, 1.569 |   -4.59 /   -4.18 /   -5.38 (36) | +4.25
  0.40 |  -15.18 /  -15.61 /  -19.94 (36) | 13.110, 1.582 |   -5.56 /   -5.19 /   -7.66 (36) | +5.27
  0.50 |  -17.67 /  -18.08 /  -21.95 (36) | 13.110, 1.582 |   -7.22 /   -7.00 /   -9.59 (36) | +6.92
  0.58 |  -20.14 /  -19.73 /  -22.78 (35) | 13.110, 1.582 |   -8.12 /   -7.99 /  -10.99 (35) | +7.85
  0.60 |  -20.14 /  -18.39 /  -23.40 (35) | 13.110, 1.582 |   -8.35 /   -7.99 /  -11.09 (35) | +8.07
  0.70 |   -9.01 /   -7.89 /  -19.83 (35) | 13.110, 1.582 |  -10.08 /   -9.85 /  -12.35 (35) | +9.81
  0.75 |   -5.76 /   -6.33 /  -14.78 (35) | 13.390, 1.616 |  -10.37 /  -10.76 /  -13.07 (35) | +10.11
  0.77 |   -5.39 /   -5.09 /  -12.36 (35) | 13.507, 1.630 |  -10.86 /  -10.88 /  -13.08 (35) | +10.61
  0.80 |   -3.43 /   -3.34 /  -10.05 (35) | 13.538, 1.634 |   -8.59 /   -9.42 /  -13.43 (35) | +8.34
  0.85 |   -1.09 /   -0.90 /   -6.74 (35) | 15.433, 1.862 |   -7.01 /   -5.95 /  -14.08 (35) | +6.81
=== D_N240_m28_s7: single-cell worst-'1' cav gain (promoted window) 8.1315; '1'-peak position in slot: cell 1 0.744, stage 2 0.838
  lo   | cell 1 alone: floor cav / drn_h / mode (n) | stage 2 chain: worst gain, G4_A | floor cav / drn_h / mode (n) | eye
  0.25 |  -10.73 /  -11.15 /  -14.61 (36) | 12.623, 1.552 |   -2.92 /   -2.43 /   -3.20 (36) | +2.50
  0.30 |  -12.51 /  -12.15 /  -15.94 (36) | 12.917, 1.589 |   -4.00 /   -3.56 /   -4.35 (36) | +3.63
  0.40 |  -14.17 /  -14.66 /  -18.61 (36) | 13.010, 1.600 |   -4.93 /   -4.59 /   -6.53 (36) | +4.60
  0.50 |  -16.67 /  -17.12 /  -20.52 (36) | 13.010, 1.600 |   -6.38 /   -6.40 /   -8.60 (36) | +6.05
  0.58 |  -18.32 /  -18.78 /  -21.60 (35) | 13.010, 1.600 |   -7.47 /   -7.28 /   -9.72 (35) | +7.16
  0.60 |  -19.14 /  -18.78 /  -21.57 (35) | 13.010, 1.600 |   -7.47 /   -7.35 /  -10.18 (35) | +7.16
  0.70 |   -8.44 /   -9.41 /  -21.29 (35) | 13.010, 1.600 |   -8.66 /   -8.65 /  -11.25 (35) | +8.35
  0.75 |   -6.39 /   -6.00 /  -15.44 (35) | 13.010, 1.600 |   -9.39 /   -9.38 /  -11.90 (35) | +9.09
  0.77 |   -5.07 /   -5.32 /  -13.44 (35) | 13.532, 1.664 |   -9.65 /   -9.39 /  -11.91 (35) | +9.38
  0.80 |   -4.39 /   -4.00 /  -10.70 (35) | 14.074, 1.731 |  -10.08 /  -10.09 /  -12.19 (35) | +9.80
  0.85 |   -1.65 /   -1.62 /   -7.60 (35) | 15.231, 1.873 |   -8.11 /   -7.04 /  -12.86 (35) | +7.90
=== (1) matched-window G4 (chain at [lo, lo+0.47] over the single cell at [lo - lag, lo - lag + 0.47]) vs the mixed ratio (single cell at the promoted window)
 m=30: passive lag 5.136 units = 0.0856 slot; single-cell gain at promoted window 8.2879
   placements with a round-spec stage-2 floor (<= -10 dB): lo 0.7400..0.7900; mixed G4_A 1.616..1.633; MATCHED G4 1.606..1.624
   matched G4 >= 1.7 at lo 0.8075..0.8300 with floors -7.34..-8.59 dB
   lo 0.7500: mixed G4_A 1.616, matched G4 1.606 (single at lo-lag: 8.337 dB), stage-2 floor -10.37
   lo 0.7625: mixed G4_A 1.616, matched G4 1.606 (single at lo-lag: 8.337 dB), stage-2 floor -10.38
   lo 0.7650: mixed G4_A 1.616, matched G4 1.606 (single at lo-lag: 8.337 dB), stage-2 floor -10.70
   lo 0.7675: mixed G4_A 1.616, matched G4 1.606 (single at lo-lag: 8.337 dB), stage-2 floor -10.86
   lo 0.7700: mixed G4_A 1.630, matched G4 1.620 (single at lo-lag: 8.337 dB), stage-2 floor -10.86
   lo 0.7725: mixed G4_A 1.633, matched G4 1.624 (single at lo-lag: 8.337 dB), stage-2 floor -10.86
   lo 0.7750: mixed G4_A 1.633, matched G4 1.624 (single at lo-lag: 8.337 dB), stage-2 floor -10.86
   lo 0.7775: mixed G4_A 1.633, matched G4 1.624 (single at lo-lag: 8.337 dB), stage-2 floor -10.86
   lo 0.7800: mixed G4_A 1.633, matched G4 1.624 (single at lo-lag: 8.337 dB), stage-2 floor -10.86
   lo 0.7825: mixed G4_A 1.633, matched G4 1.624 (single at lo-lag: 8.337 dB), stage-2 floor -10.86
   lo 0.7850: mixed G4_A 1.633, matched G4 1.624 (single at lo-lag: 8.337 dB), stage-2 floor -10.86
   lo 0.7875: mixed G4_A 1.633, matched G4 1.624 (single at lo-lag: 8.337 dB), stage-2 floor -10.86
   lo 0.7900: mixed G4_A 1.633, matched G4 1.624 (single at lo-lag: 8.337 dB), stage-2 floor -10.20
   lo 0.8000: mixed G4_A 1.634, matched G4 1.624 (single at lo-lag: 8.337 dB), stage-2 floor -8.59
   lo 0.8250: mixed G4_A 1.748, matched G4 1.711 (single at lo-lag: 8.467 dB), stage-2 floor -8.41
 m=28: passive lag 5.111 units = 0.0913 slot; single-cell gain at promoted window 8.1315
   placements with a round-spec stage-2 floor (<= -10 dB): lo 0.7925..0.8175; mixed G4_A 1.664..1.731; MATCHED G4 1.634..1.695
   matched G4 >= 1.7 at lo 0.8300..0.8300 with floors -8.36..-8.36 dB
   lo 0.7500: mixed G4_A 1.600, matched G4 1.577 (single at lo-lag: 8.248 dB), stage-2 floor -9.39
   lo 0.7750: mixed G4_A 1.664, matched G4 1.634 (single at lo-lag: 8.283 dB), stage-2 floor -9.65
   lo 0.7925: mixed G4_A 1.664, matched G4 1.634 (single at lo-lag: 8.283 dB), stage-2 floor -10.08
   lo 0.7950: mixed G4_A 1.665, matched G4 1.635 (single at lo-lag: 8.284 dB), stage-2 floor -10.08
   lo 0.7975: mixed G4_A 1.703, matched G4 1.668 (single at lo-lag: 8.301 dB), stage-2 floor -10.08
   lo 0.8000: mixed G4_A 1.731, matched G4 1.695 (single at lo-lag: 8.301 dB), stage-2 floor -10.08
   lo 0.8025: mixed G4_A 1.731, matched G4 1.695 (single at lo-lag: 8.301 dB), stage-2 floor -10.08
   lo 0.8050: mixed G4_A 1.731, matched G4 1.695 (single at lo-lag: 8.301 dB), stage-2 floor -10.08
   lo 0.8075: mixed G4_A 1.731, matched G4 1.695 (single at lo-lag: 8.301 dB), stage-2 floor -10.08
   lo 0.8100: mixed G4_A 1.731, matched G4 1.695 (single at lo-lag: 8.301 dB), stage-2 floor -10.08
   lo 0.8125: mixed G4_A 1.731, matched G4 1.695 (single at lo-lag: 8.301 dB), stage-2 floor -10.08
   lo 0.8150: mixed G4_A 1.731, matched G4 1.695 (single at lo-lag: 8.301 dB), stage-2 floor -10.08
   lo 0.8175: mixed G4_A 1.731, matched G4 1.695 (single at lo-lag: 8.301 dB), stage-2 floor -10.08
   lo 0.8200: mixed G4_A 1.731, matched G4 1.695 (single at lo-lag: 8.301 dB), stage-2 floor -9.20
   lo 0.8250: mixed G4_A 1.731, matched G4 1.695 (single at lo-lag: 8.301 dB), stage-2 floor -8.37
=== (2) loaded-drain loop model, full range (released regen.loop_gain)
 J=-1 lossless  ratio r=+|r|: loaded loop +0.429; delivered passive +2.58 / active +3.86 dB; loaded CW regen +1.28 dB
 J=-1 lossless  ratio r=-|r|: loaded loop -0.429; delivered passive -3.53 / active -4.10 dB; loaded CW regen -0.57 dB
 J=-1 9.4 bound ratio r=+|r|: loaded loop +0.143; delivered passive +0.04 / active +0.34 dB; loaded CW regen +0.30 dB
 J=-1 9.4 bound ratio r=-|r|: loaded loop -0.143; delivered passive -1.93 / active -2.16 dB; loaded CW regen -0.23 dB
 J=-1 11.6%     ratio r=+|r|: loaded loop +0.322; delivered passive +1.54 / active +2.37 dB; loaded CW regen +0.83 dB
 J=-1 11.6%     ratio r=-|r|: loaded loop -0.322; delivered passive -2.96 / active -3.42 dB; loaded CW regen -0.46 dB
 J=-1 |r|->0    ratio r=+|r|: loaded loop +0.000; delivered passive -1.00 / active -1.00 dB; loaded CW regen +0.00 dB
 J=-1 |r|->0    ratio r=-|r|: loaded loop -0.000; delivered passive -1.00 / active -1.00 dB; loaded CW regen +0.00 dB
 full range over J in {-1,-3,-6} x 3 junction models x 2 phases x 2 biases: passive delivered -10.32 .. +3.49 dB; active -11.19 .. +8.79 dB; loaded loop -0.818 .. +0.818
 J=-1 only, both phases: passive delivered -3.53 .. +2.58 dB; open-end phase only: -1.00 .. +2.58 dB
=== (3) passive peak-to-peak stage latency across all families (rt)
 N240_m28_s7      N=240 peak passive 0.5250 rt (excess over 0.5: 0.0250)
 N240_m28_s7_Jext N=240 peak passive 0.5243 rt (excess over 0.5: 0.0243)
 N240_m28_s11     N=240 peak passive 0.5250 rt (excess over 0.5: 0.0250)
 N240_m28_s13     N=240 peak passive 0.5250 rt (excess over 0.5: 0.0250)
 N240_m30_s7      N=240 peak passive 0.5250 rt (excess over 0.5: 0.0250)
 N240_m30_s7_Jext N=240 peak passive 0.5243 rt (excess over 0.5: 0.0243)
 N240_m30_s11     N=240 peak passive 0.5250 rt (excess over 0.5: 0.0250)
 N240_m30_s13     N=240 peak passive 0.5250 rt (excess over 0.5: 0.0250)
 N480_m28_s7      N=480 peak passive 0.5226 rt (excess over 0.5: 0.0226)
 N480_m30_s7      N=480 peak passive 0.5226 rt (excess over 0.5: 0.0226)
 N720_m30_s7      N=720 peak passive 0.5183 rt (excess over 0.5: 0.0183)
=== (4) continuum estimate rounding: 2*1.5028-1.5810 = 1.4245672054871485 ; m28: 1.4587601059748925
```

### `rw4_runs.py` (Table 9 row iii: gate (i) plus a hard '1' cut) and `rw4_merge.py` (both hard-cut rows re-scored)

```text
=== (A) cfl sensitivity at fixed N = 240 (bias held at the released-convention 0.7*M_th_num(240) measured at cfl 0.4)
 cfl 0.2: cell 1 gain 7.3923, floors cav -16.694 drn_h -17.028 mode -22.415; passive transfer 15.01 dB; active drn_h 0.02765; residue (a) -8.11 / (b) -4.58 dB
        lags: passive env 2.389 rt (rule 2.375), peak 0.5164 rt; active env 4.893 rt
        window rule      shift 2.375 rt: chain 13.112 G4_A 1.774 c2c 5.504 | floor cav -8.35 drn_h -8.00 mode -11.65 | eye +8.20 (n 36)
        window fixed2625 shift 2.625 rt: chain 13.128 G4_A 1.776 c2c 5.517 | floor cav -8.36 drn_h -8.98 mode -12.02 | eye +8.21 (n 36)
        window unshifted shift 0.000 rt: chain 12.902 G4_A 1.745 c2c 5.447 | floor cav -6.31 drn_h -6.19 mode -9.02 | eye +6.16 (n 36)
 cfl 0.4: cell 1 gain 8.2879, floors cav -11.828 drn_h -11.775 mode -15.665; passive transfer 15.83 dB; active drn_h 0.03397; residue (a) -5.70 / (b) -1.57 dB
        lags: passive env 2.568 rt (rule 2.625), peak 0.5250 rt; active env 5.708 rt
        window rule      shift 2.625 rt: chain 13.103 G4_A 1.581 c2c 4.798 | floor cav -4.70 drn_h -4.31 mode -6.26 | eye +4.39 (n 36)
        window fixed2625 shift 2.625 rt: chain 13.103 G4_A 1.581 c2c 4.798 | floor cav -4.70 drn_h -4.31 mode -6.26 | eye +4.39 (n 36)
        window unshifted shift 0.000 rt: chain 12.734 G4_A 1.537 c2c 4.649 | floor cav -3.56 drn_h -3.09 mode -4.10 | eye +3.15 (n 36)
 cfl 0.8: cell 1 gain 8.5880, floors cav -8.886 drn_h -8.768 mode -11.661; passive transfer 16.34 dB; active drn_h 0.03826; residue (a) -4.21 / (b) 0.20 dB
        lags: passive env 2.628 rt (rule 2.625), peak 0.5320 rt; active env 5.871 rt
        window rule      shift 2.625 rt: chain 12.756 G4_A 1.485 c2c 4.202 | floor cav -3.37 drn_h -2.97 mode -3.49 | eye +2.95 (n 36)
        window fixed2625 shift 2.625 rt: chain 12.756 G4_A 1.485 c2c 4.202 | floor cav -3.37 drn_h -2.97 mode -3.49 | eye +2.95 (n 36)
        window unshifted shift 0.000 rt: chain 12.239 G4_A 1.425 c2c 4.004 | floor cav -2.40 drn_h -1.94 mode -1.68 | eye +1.79 (n 36)
=== (B) J = -25 chain (cfl 0.4): window-placement rows
 lo 0.25: chain 15.699 G4_A 1.894 | floor cav -1.94 drn_h -1.91 mode -3.00 (n 36)
 lo 0.60: chain 16.353 G4_A 1.973 | floor cav -7.99 drn_h -7.75 mode -11.04 (n 35)
 lo 0.70: chain 16.353 G4_A 1.973 | floor cav -9.72 drn_h -9.49 mode -12.70 (n 35)
 lo 0.77: chain 16.695 G4_A 2.014 | floor cav -10.90 drn_h -10.66 mode -13.74 (n 35)
 lo 0.80: chain 16.773 G4_A 2.024 | floor cav -11.48 drn_h -11.23 mode -14.12 (n 35)
 lo 0.85: chain 18.650 G4_A 2.250 | floor cav -10.12 drn_h -9.30 mode -15.04 (n 35)
 rule window (2.625 rt): chain 16.230 G4_A 1.958 floor cav -3.72 mode -5.27
=== (C) gated-input ablation (J = -1, cfl 0.4, rule window 2.625 rt): stage-2 floors
 no gate: floor cav -4.696 drn_h -4.307 mode -6.257; chain gain 13.103; eye +4.39
 '0'-slot residue zeroed (1-rt raised-cosine cut at each '0'-slot start): floor cav -9.380 drn_h -8.822 mode -12.977; chain gain 13.103; eye +9.08
 additionally the '1' slots' post-drive tail [0.8, 1.0]*repT removed: floor cav -12.537 drn_h -12.081 mode -16.216; chain gain 13.127; eye +12.25
gate (i) raised-cosine '0' cut + hard '1' cut at 0.8*repT: {'floor_cav': -13.086, 'floor_drnh': -12.638, 'floor_mode': -16.82, 'chain': 13.131, 'eye': 12.802} 76.0 s Linux x86_64, Python 3.11.15, numpy 2.4.6
ablation_hard {'floor_cav': -13.807, 'floor_drnh': -13.363, 'floor_mode': -17.527, 'chain': 13.131, 'eye': 13.523}
ablation_rc0_hard1 {'floor_cav': -13.086, 'floor_drnh': -12.638, 'floor_mode': -16.820, 'chain': 13.131, 'eye': 12.802}
```
