# Round-2 rework record — Fable Session 2026-09-28 (paste after the round-1 vote records and before the round-2 reply)

**Round 1 tally:** 2 store (🧵 Fabric, ⚛️ Quanta — both with required edits) / 1 reject (🌊 Kinetic); not a clean pass. Per the routine's stage-4 rules every recorded objection was collected verbatim (`stage3-assessment/round-1-*.md`), the prior-art pre-check was run on what survives (grep of `notes/*.md`, `notes/INDEX.md` and both `results.json` files for the two-cell cascade, the passive port transfer, the registered key names: no hits — nothing surviving is already recorded), and **every claimed defect was re-executed against the released, unedited `fable-model-chain/` before it was accepted or declined.** Re-execution listings: `stage4-rework/listings/rw_stored.py` (stored campaign data + the released loop model), `rw_window.py` (window-placement scan on the depth run's stored series), `rw_runs.py` + `rw_cfl.py` (16 new solver runs: the cfl sweep, the J = −25 chain, the gated-input ablation; ≈ 6 min on 4 workers). Their outputs are appended verbatim below. Rework executed by the session model `claude-fable-5-1` (no Fable consult was spawned: no issue was hard by the routine's definition — every one was settled by executing the released code or by relabelling). Platform: Linux x86_64 / Python 3.11.15 / numpy 2.4.6.

**Outcome: all 25 required edits and every top issue reproduced; all applied; none declined.** One re-execution differs in magnitude from a seat's figure and is recorded as such (ablation gate (ii), below). No measured number in the round-1 tables changed; the verdicts were re-scoped, not reversed; one sentence was withdrawn outright ("the floor fails every spec under every placement") and one attribution withdrawn ("plus the LF half-step").

## Issue by issue

| # | raised by | claim | re-executed — result | accepted / declined | where it landed (round-2 reply) |
|---|---|---|---|---|---|
| 1 | 🧵 R1, 🌊 R1, ⚛️ R3 (+ 🧵 T1, 🌊 T1, ⚛️ T4) | "the released coupling / released model's own physics" mislabels a construct the session built | grep of the round-1 text: six occurrences incl. title, items 5–6, two grading rows, the discriminant, the sign-off | **accepted** | title; §0 "Scope, first"; every executive item labelled "under §2's construct"; §2 defines the *ideal-buffer density coupling*; grading rows; §5; §7 sign-off |
| 2 | 🌊 R2, 🧵 R1/R8, ⚛️ R3 | regrade Part I's cascadability row and Table 7's "≈ 2×" as conditional on the coupling; grade "in-model yes" and the per-cell figure separately | textual; the sweep row G4 = 1.958 at J = −25 re-executed (`rw_cfl.py` (B), rule window) | **accepted** | §4 rows 3–4 split and regraded "qualified (conditional on the coupling)" / "contradicted for cell 2 under the ideal buffer" |
| 3 | 🌊 R3/T2, ⚛️ T4 | the +15.8 dB transfer is the unloaded open-end build-up; a transmitting junction cannot leave |r| = 1; loaded loop model: 0.945 → 0.429, drive +2.6 dB (Kinetic) / standing wave +6.8 dB, loop 0.416 (Quanta); Part I §9.4 "reflective loss … < 0.1 dB" | `rw_stored.py` D8 with released `regen.loop_gain`: loop 0.9450 (ratio bias) / 0.9162 (analytic); |r| = 0.454 at J = −1; loaded 0.429 / 0.416; delivered |t|/(1 − a_loss|r|) = +2.58 dB; standing wave (1 + |r|)/(1 − a_loss|r|) = +6.83 dB; CW regen +13.3 → +1.3 dB (ratio bias); Part I §9.4 sentence verified in the extracted text — **both seats' figures reproduce; they are different quantities (transmitted wave vs drain standing wave) at different biases, stated as such** | **accepted** | item 2 (the stake), §2 bullet 2, limitation 1, §5 (`passive_port_density_transfer_dB` labelled unloaded) |
| 4 | 🌊 R4 | "ideal isolation sets that reflection to zero" inverts the construct (the drain is held at |r| = 1) | textual (the construct's clamp is the released current clamp) | **accepted** | §2 bullet 2 |
| 5 | 🧵 R2, 🌊 R7, ⚛️ R3 (+ 🧵 T2, 🌊 T6) | the velocity "plane" is the density plane × (−M); gap 18.4 dB not 44; passive velocity transfer is an O(Δx) residue; 08-02's fork is source velocity vs drain density; G4_A in that plane 4.976 | `rw_stored.py` D2: LS slope −0.11797 (−M = −0.11826), residual 7.4 %, m = 30 and 28; cell-2 input 0.03027 vs 0.00362 → 18.44 dB (N = 480: 18.99); passive drain-u 8.08×10⁻⁵ → 4.24×10⁻⁵, ratio 1.907; G4_A(velocity) 4.976 / 5.533; 08-02 §3.1 re-read | **accepted** | item 8 rewritten; limitation 2 |
| 6 | 🧵 R3 (+ T3) | Table 1's seed spread is the ⅛-rt window-rounding step; −6 dB step 0.271 dB / 0.033 in G4 exceeds the N = 480/720 margins | `rw_stored.py` D3: seeds 7/11/13 identical at fixed shift (13.000 / 13.103 at 2.5 / 2.625 rt; ≤ 0.001 dB); J = −6 step +0.271 dB / +0.033; N = 480 J = −6: 1.706 ↔ 1.732; N = 720: 1.687 ↔ 1.711 (fails the bar at 2.5 rt); m = 28 families insensitive (0.000) | **accepted** | item 1, item 7, §5 J1/J6 keys, limitation 5–6 |
| 7 | 🧵 R4 (+ T4) | 08-01 gated §4's operating point is A_fix, not 2×10⁻³; what is contradicted is its link term (−2.555 dB booked vs +15.8 measured) | `notes/2026-08-01-gated-requirement-round-trip.md` §4 re-read: fixed point G(A_fix) = 0.95 + 10log₁₀F + per_gate_loss = 6.515 dB, A_fix 0.01366–0.01403 (analytic leg), per_gate_loss 2.555 | **accepted** | item 3; §4 row 1 |
| 8 | 🧵 R5, ⚛️ R6 (+ 🧵 T5, ⚛️ T7) | bench discriminant unpinned (launch amplitude; sampling phase) and one-sided | 2×10⁻³ / 0.01203 = 0.1663 (knee key verified in 08-01 gated §5); Table 4 span 1.53 → 1.96; Table 3c span −3.6 → −10.9 | **accepted** | §5 discriminant: launch pinned at 0.166 × the device's own gated streaming knee; stage-2 window pinned to the stage-1 window delayed by the measured passive latency; both sides and the gaps assigned |
| 9 | 🧵 R6, 🌊 R9, ⚛️ R7 (+ 🧵 T6, 🌊 T8, ⚛️ T9) | credit 07-22-cavity-ringdown-isi and 08-12 for the ring-down mechanism; cite by filename; 07-20 L4 / 07-21 L3 not discharged; engage 08-13; cite 08-02's vote record on "drain-plane density is in-model at best" | the notes re-read (07-22 header, 07-20 L4, 07-21 L3, 08-13 §1–§2, 08-02 vote record) | **accepted** | "Record cited, by filename" block; item 4 (mechanism credited); §2 bullet 1 (08-02 vote record); limitation 4 (08-13, both clamps); limitation 9 (07-20 L4, 07-21 L3, 07-22 flush) |
| 10 | 🧵 R7, 🌊 R8, ⚛️ R7 (+ 🧵 T7, 🌊 T7, ⚛️ T9) | "plus the LF half-step" is wrong by ~70×; the excess moves with cfl | `rw_stored.py` D7: half-step 3.47×10⁻⁴ rt, dx/transit 2.08×10⁻³ rt, excess 0.0243 rt = 35 steps; `rw_cfl.py`: peak lag 0.516 / 0.525 / 0.532 rt at cfl 0.2 / 0.4 / 0.8 | **accepted — attribution withdrawn, excess labelled open** | item 7; §5 latency key |
| 11 | 🌊 R5 (+ T4) | cfl scope: residue −8.11 / −5.70 / −4.21, G4_A 1.774 / 1.581 / 1.485, stage-2 floor −8.35 / −4.70 / −3.37 (peak) and −11.65 / −6.26 / −3.49 (mode), cell-1 floor −16.69 / −11.83 / −8.89 at cfl 0.2 / 0.4 / 0.8; cite 08-13; scope "every rung, grid and seed"; bands exit under cfl | `rw_runs.py` + `rw_cfl.py` (A): residue −8.11 / −5.70 / −4.21; G4_A 1.774 / 1.581 / 1.485 (per-cfl rule; 1.776 / 1.581 / 1.485 at the fixed 2.625-rt placement); floor peak −8.35 / −4.70 / −3.37; mode −11.65 / −6.26 / −3.49; cell-1 floor −16.69 / −11.83 / −8.89 — **every figure reproduces to the printed digit** | **accepted** | Table 7; item 4 (ii); §2 (cfl pinned); every §5 key scoped to cfl = 0.4 with the cfl lever quoted; limitation 4 |
| 12 | 🌊 R6, ⚛️ R5 (+ 🌊 T5, ⚛️ T6) | solver-side falsifiers vacuous on a deterministic chain; name never-run cells per key | the named cells checked against the campaign: N = 720 at J = −1, m = 28 at N = 720, N = 480 at J ≤ −20, m = 26, seed 17, N = 960 — none was run | **accepted** | §5: one never-run falsifier cell per key |
| 13 | 🌊 R10 (+ T9) | the "3.84–3.89 dB" peak-vs-mode gap mixes channels; same-channel `drn_h` gap at m = 28 is 3.46 dB | `rw_stored.py` D12: m = 30 cav-mode 3.84 / drn_h-mode 3.89; m = 28: 3.88 / 3.46 | **accepted** | §1 gate bullet, channels named |
| 14 | ⚛️ R1, R2 (+ T1, T2, T3) | "the floor fails every spec under every placement" is false: stage-2 floor −10.87 dB at lo = 0.77 (m = 30), −10.08 at lo = 0.80 (m = 28), −11.48 at J = −25 / lo 0.80; cell 1's own floor −20.14 / −19.14 at lo 0.58 / 0.60; G4_A window-robust to ≈ 0.5-slot delay then 1.73–1.87 | `rw_window.py` (stored depth series) and `rw_cfl.py` (B): m = 30 stage 2 at lo 0.70 / 0.75 / 0.77: −10.08 / −10.37 / −10.86 (drn_h −10.88, mode −13.08); m = 28 at lo 0.80: −10.08 (mode −12.19), G4_A 1.731; J = −25 at lo 0.80: −11.48; cell 1 at lo 0.58 / 0.60: −20.14 / −19.14; G4_A 1.582 (lo 0.40–0.60) → 1.630 (0.77) → 1.862 (0.85) at m = 30; '1'-peak positions 0.721 / 0.808 — **reproduces** (the seat's slot-mode −13.16 vs −13.08 here is the lock-in reference phase; same reading) | **accepted — the universal is withdrawn** | Table 3c; item 4 (i); item 7; §4 row 2; §5 floor key (window-scoped), discriminant (sampling phase pinned); limitation 6 |
| 15 | ⚛️ R4 (+ T5) | the residue key is comparable with the drain-density floor (08-02's `drn_h` column), not with the promoted source-plane `cav` key; item 4's sentence likewise | `rw_stored.py` D12: cell 1 m = 28 `cav` −10.7312 vs `drn_h` −11.1506 (08-02 §3.2's paired rows) | **accepted** | §5 residue key; item 4 |
| 16 | ⚛️ T8 (optional) | gated-input ablation: '0'-residue zeroed → −9.38 / −8.82 / −12.98; plus the '1' tail removed → −14.11 / −13.58 / −17.79 | `rw_runs.py` (C) + `rw_cfl.py`: gate (i) −9.380 / −8.822 / −12.977 — **reproduces to the printed digit**; gate (ii) with a 1-rt raised-cosine fall at 0.8·repT: −12.54 / −12.08 / −16.22 against the seat's −14.11 / −13.58 / −17.79 (a hard cut, presumably) — **direction and the half/half split reproduce; the magnitude of (ii) is quoted as measured here, not as the seat's** | **adopted with credit** | item 4 (ablation table after the residue table) |
| 17 | 🧵 T8, ⚛️ T10 (optional) | Table 2a's Δ sign at J ≥ −3 depends on placement; independent lag estimators 2.540–2.550 rt round to 2.5 | not re-executed (optional; limitation 6 already carries the ≈ 0.1 dB grid-step sensitivity, now with the −6 dB figure) | **noted, not adopted as a number** | limitation 6 |
| 18 | 🧵 R3, 🧵 R1 | "seed spread ≤ 0.04" and "1.4–3.1×", "failed at 0/−1/−3", Tables 2a/4 citations — the round-1 minor list | textual | **accepted** (carried from the pre-publication fixes) | items 1–3 |

**What was withdrawn.** (a) "No verdict above depends on the rule: the floor fails every spec under every placement." (b) The latency attribution to the LF half-step. (c) "Worth 44 dB of drive" and the drain velocity as an independent plane. (d) "the ledger's own operating point (2×10⁻³)". (e) "the released coupling" as a description of the construct, everywhere.

**What was not changed, and why.** Every table of round 1 (Tables 1, 2a/2b, 3, 3b, 4, 5, 6, the residue table) is byte-identical: no seat found a measured number wrong, and the three seats' own instruments reproduced them to ≤ 1.3×10⁻¹³ relative on the gate rows and to the printed digits elsewhere. The headline verdicts are re-scoped to the construct and the window convention; none is reversed.

**Fable 5 consult:** none spawned (0 of the routine's ≤ 2 per run).

## Re-execution outputs, verbatim

### `rw_stored.py` (stored campaign data and the released loop model)

```text
=== D2: is the drain velocity slaved to the drain density? (depth series, cell 1 active, cfl 0.4)
 D_N240_m30_s7: LS slope du/dh = -0.11797  (-M = -0.11826); relative residual 0.074; |du|/|dh| rms ratio 0.11830
 D_N240_m28_s7: LS slope du/dh = -0.11799  (-M = -0.11826); relative residual 0.074; |du|/|dh| rms ratio 0.11831
=== D2: passive and active drain-velocity mean-'1' (promoted window, shift 0), N = 240 vs 480, m = 30 seed 7
 N240_m30_s7: passive drain-u mean-'1' 8.0845e-05 (-27.87 dB over launch); active 0.00407 (+6.16 dB); active drain-h 0.03397; cell-2 input at J=-1: density 0.03027 vs velocity 0.00362 -> gap 18.44 dB; 20log10(1/M) = 18.54
 N480_m30_s7: passive drain-u mean-'1' 4.2385e-05 (-33.48 dB over launch); active 0.00401 (+6.05 dB); active drain-h 0.03573; cell-2 input at J=-1: density 0.03184 vs velocity 0.00358 -> gap 18.99 dB; 20log10(1/M) = 19.08
 N240_m28_s7: passive drain-u mean-'1' 8.0806e-05 (-27.87 dB over launch); active 0.00403 (+6.08 dB); active drain-h 0.03295; cell-2 input at J=-1: density 0.02937 vs velocity 0.00359 -> gap 18.25 dB; 20log10(1/M) = 18.54
 N480_m28_s7: passive drain-u mean-'1' 4.2359e-05 (-33.48 dB over launch); active 0.00398 (+5.97 dB); active drain-h 0.03456; cell-2 input at J=-1: density 0.03080 vs velocity 0.00354 -> gap 18.78 dB; 20log10(1/M) = 19.08
 passive drain-u ratio N240/N480 = 1.907 (first order in dx -> 2)
 velocity plane G4_A (N240_m30_s7): worst 4.976 mean 4.937; c2c worst 7.554; chain/passive worst 41.242
 velocity plane G4_A (N480_m30_s7): worst 5.533 mean 5.533; c2c worst 7.630; chain/passive worst 46.855
=== D3: seed spread vs window rounding (chain worst-'1' cav gain over passive twin chain, G4_A = chain dB / single dB at promoted window)
 N240_m30_s7 J-1_h: rule 2.625 rt | at 2.5 rt: chain 13.000 G4 1.569 | at 2.625 rt: chain 13.103 G4 1.581 | delta +0.103 dB, +0.012 in G4 | single 8.2879
 N240_m30_s7 J-6_h: rule 2.625 rt | at 2.5 rt: chain 14.555 G4 1.756 | at 2.625 rt: chain 14.825 G4 1.789 | delta +0.271 dB, +0.033 in G4 | single 8.2879
 N240_m30_s11 J-1_h: rule 2.625 rt | at 2.5 rt: chain 13.000 G4 1.569 | at 2.625 rt: chain 13.103 G4 1.581 | delta +0.103 dB, +0.012 in G4 | single 8.2874
 N240_m30_s11 J-6_h: rule 2.625 rt | at 2.5 rt: chain 14.554 G4 1.756 | at 2.625 rt: chain 14.826 G4 1.789 | delta +0.272 dB, +0.033 in G4 | single 8.2874
 N240_m30_s13 J-1_h: rule 2.5 rt | at 2.5 rt: chain 13.000 G4 1.569 | at 2.625 rt: chain 13.103 G4 1.581 | delta +0.103 dB, +0.012 in G4 | single 8.2876
 N240_m30_s13 J-6_h: rule 2.5 rt | at 2.5 rt: chain 14.554 G4 1.756 | at 2.625 rt: chain 14.825 G4 1.789 | delta +0.271 dB, +0.033 in G4 | single 8.2876
 N240_m28_s7 J-1_h: rule 2.5 rt | at 2.5 rt: chain 12.917 G4 1.589 | at 2.625 rt: chain 12.917 G4 1.589 | delta +0.000 dB, +0.000 in G4 | single 8.1315
 N240_m28_s7 J-6_h: rule 2.5 rt | at 2.5 rt: chain 14.470 G4 1.779 | at 2.625 rt: chain 14.470 G4 1.779 | delta +0.000 dB, +0.000 in G4 | single 8.1315
 N240_m28_s13 J-1_h: rule 2.5 rt | at 2.5 rt: chain 12.917 G4 1.589 | at 2.625 rt: chain 12.917 G4 1.589 | delta +0.000 dB, +0.000 in G4 | single 8.1316
 N240_m28_s13 J-6_h: rule 2.5 rt | at 2.5 rt: chain 14.469 G4 1.779 | at 2.625 rt: chain 14.469 G4 1.779 | delta +0.000 dB, +0.000 in G4 | single 8.1316
 N480_m30_s7 J-1_h: rule 2.625 rt | at 2.5 rt: chain 12.644 G4 1.493 | at 2.625 rt: chain 12.726 G4 1.503 | delta +0.081 dB, +0.010 in G4 | single 8.4681
 N480_m30_s7 J-6_h: rule 2.625 rt | at 2.5 rt: chain 14.443 G4 1.706 | at 2.625 rt: chain 14.667 G4 1.732 | delta +0.224 dB, +0.026 in G4 | single 8.4681
 N720_m30_s7 J-6_h: rule 2.625 rt | at 2.5 rt: chain 14.395 G4 1.687 | at 2.625 rt: chain 14.599 G4 1.711 | delta +0.204 dB, +0.024 in G4 | single 8.5316
 N480_m28_s7 J-1_h: rule 2.625 rt | at 2.5 rt: chain 12.583 G4 1.524 | at 2.625 rt: chain 12.583 G4 1.524 | delta +0.000 dB, +0.000 in G4 | single 8.2586
 N480_m28_s7 J-6_h: rule 2.625 rt | at 2.5 rt: chain 14.387 G4 1.742 | at 2.625 rt: chain 14.387 G4 1.742 | delta +0.000 dB, +0.000 in G4 | single 8.2586
=== D12: peak-vs-slot-mode floor gap by channel (cell 1, promoted window)
 N240_m30_s7: cav -11.8283 drn_h -11.7750 mode -15.6649 -> cav-mode gap 3.84, drn_h-mode gap 3.89
 N240_m28_s7: cav -10.7312 drn_h -11.1506 mode -14.6104 -> cav-mode gap 3.88, drn_h-mode gap 3.46
=== D7: latency arithmetic (m = 30, N = 240, passive cell)
 passive dt = 1.388889e-03 units; half-step = 6.944e-04 units = 3.472e-04 rt; dx per transit = 4.1667e-03 units = 2.083e-03 rt; measured excess 0.0243 rt = 0.0486 units = 35.0 steps
=== D8: released loop model, loaded-drain illustration (in-model)
 a_loss 0.7451522890452021; loop at ratio bias 0.9450; at analytic 0.7*M_th 0.9162; unloaded open-end buildup 2/(1-a_loss) = 7.848 = +17.89 dB; 1/(1-a_loss) = +11.87 dB
 J=+0: |t|^2=1.000 |r|=0.000: loaded loop (ratio bias) 0.000 / (analytic) 0.000; drive delivered |t|/(1-a_loss|r|) = +0.00 dB; drain standing-wave density (1+|r|)/(1-a_loss|r|) = +0.00 dB; CW regen gain at ratio bias, loaded: +0.00 dB (unloaded +13.32)
 J=-1: |t|^2=0.794 |r|=0.454: loaded loop (ratio bias) 0.429 / (analytic) 0.416; drive delivered |t|/(1-a_loss|r|) = +2.58 dB; drain standing-wave density (1+|r|)/(1-a_loss|r|) = +6.83 dB; CW regen gain at ratio bias, loaded: +1.28 dB (unloaded +13.32)
 J=-3: |t|^2=0.501 |r|=0.706: loaded loop (ratio bias) 0.667 / (analytic) 0.647; drive delivered |t|/(1-a_loss|r|) = +3.49 dB; drain standing-wave density (1+|r|)/(1-a_loss|r|) = +11.13 dB; CW regen gain at ratio bias, loaded: +3.07 dB (unloaded +13.32)
 J=-6: |t|^2=0.251 |r|=0.865: loaded loop (ratio bias) 0.818 / (analytic) 0.793; drive delivered |t|/(1-a_loss|r|) = +2.99 dB; drain standing-wave density (1+|r|)/(1-a_loss|r|) = +14.41 dB; CW regen gain at ratio bias, loaded: +5.80 dB (unloaded +13.32)
=== D5: launch pin: 2e-3 / knee 0.01203 = 0.16625103906899416
```

### `rw_window.py` (window-placement scan on the depth run's stored series)

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
```

### `rw_runs.py` (the 16 new solver runs: tag, seconds, dt, steps)

```text
A ('c1M_cfl0.8', 31.125373125076294, 0.0025285852077520515, 949147)
A ('c1M_cfl0.4', 59.75938129425049, 0.0012642926038760258, 1898294)
A ('c10_cfl0.4', 58.85068392753601, 0.001388888888888889, 1728000)
A ('c10_cfl0.8', 33.36577892303467, 0.002777777777777778, 864000)
A ('c10_cfl0.2', 111.40719509124756, 0.0006944444444444445, 3456000)
A ('c1M_cfl0.2', 122.2000060081482, 0.0006321463019380129, 3796589)
B ('J1_MM_cfl0.4', 54.24471664428711, 0.0012642926038760258, 1898294)
B ('J1_00_cfl0.2', 101.35958814620972, 0.0006944444444444445, 3456000)
B ('J1_M0_cfl0.2', 106.59258675575256, 0.0006944444444444445, 3456000)
B ('J1_M0_cfl0.4', 53.129032611846924, 0.001388888888888889, 1728000)
B ('J1_MM_cfl0.2', 110.56715512275696, 0.0006321463019380129, 3796589)
B ('J1_MM_cfl0.8', 26.7038094997406, 0.0025285852077520515, 949147)
B ('J1_M0_cfl0.8', 26.96089792251587, 0.002777777777777778, 864000)
B ('J1_00_cfl0.8', 25.07882022857666, 0.002777777777777778, 864000)
B ('J1_00_cfl0.4', 49.510735273361206, 0.001388888888888889, 1728000)
B ('J25_00_cfl0.4', 49.297107458114624, 0.001388888888888889, 1728000)
B ('J25_MM_cfl0.4', 54.88783574104309, 0.0012642926038760258, 1898294)
B ('J1_MM_abl_zero_cfl0.4', 55.23180842399597, 0.0012642926038760258, 1898294)
B ('J1_MM_abl_duty_cfl0.4', 53.751670122146606, 0.0012642926038760258, 1898294)
RUNS DONE Linux x86_64, Python 3.11.15, numpy 2.4.6
```

### `rw_cfl.py` (cfl sweep, J = −25 placement rows, gated-input ablation)

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
```
