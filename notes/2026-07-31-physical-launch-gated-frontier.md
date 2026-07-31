# The physical launch burst, adjudicated: the ‚âà0.1 THz F = 2 headline does not survive a slot-confined, data-gated drive ‚Äî the knee migrates to the CW corner, the slot-filling eye floor rises 5‚Äì6 dB at matched grid, and the honest gated operating point is ‚âà 0.07 THz (67‚Äì71 GHz at the measured rungs), with 91 GHz surviving only as an F = 1 wire

**Status:** promoted to `notes/` ‚Äî accepted by a **3-of-3 agent vote** (recorded below). **License:** CC BY 4.0.
**Prompted by:** [Fable Session ‚Äî 2026-07-31, discussion #83](https://github.com/ryoji-info/FableComputer/discussions/83) (Fabric's üßµ winning prompt, 2-of-3 vote ‚Äî Kinetic ‚Üí Fabric, Quanta ‚Üí Fabric; Fabric ‚Üí Quanta). The commissioned question: does E1's ‚âà0.1 THz headline ‚Äî the `f_max_F2_burst12_GHz` = 80 [71, 91] operating point of [`notes/2026-07-25-e1-burst-scaling-proviso.md`](2026-07-25-e1-burst-scaling-proviso.md) ‚Äî survive a slot-confined, data-gated, knee-migrated, energy-priced launch drive?
**Method:** every anchor and premise re-executed against the released `fable-model-chain/` (Python 3 + numpy, macOS/CPython, `python3`); the listings reproduced below produce every number. The custom driver imports the released integrator verbatim and was validated **bit-identical** to released `solver.run(drive_kind='prbs')` (max |cav diff| = 0.0 over 250,167 steps) and against three 07-25 probe rows to the digit. Adversarially checked before posting by three blind, independent verification agents instructed to refute (verdicts **3√ó FIX-FIRST, 0 REFUTED**; the required fixes are applied in the reply text and itemized in its own disclosure header). Each promotion assessor below additionally re-executed key numbers independently (their runs are quoted in the vote record).
**Author:** Claude **Fable 5** (`claude-fable-5`) ‚Äî the routine's intended model, active for every pipeline stage (candidate drafts, selection vote, execution, adversarial verification, and the assessment recorded below). Maintainer-operated Claude Code session per [agents/README.md](../agents/README.md), 2026-07-31 (assessed the same day, also on `claude-fable-5`).
**Labels:** demonstrated / in-model / open, per [notes/README.md](README.md).
**Binding record honored (as consumed by the reply):** [`notes/2026-07-23-reset-switch-adjudication.md`](2026-07-23-reset-switch-adjudication.md) (the G_req ledger ‚Äî re-derived to the digit ‚Äî the 4-ps F = 2 negative, the E-table, and the ¬ß1 quiet-switching spec, whose signal-plane descendant this reply derives); [`notes/2026-07-25-e1-burst-scaling-proviso.md`](2026-07-25-e1-burst-scaling-proviso.md) (the parent qualification: its probe rows reproduced to the digit, its `f_max_F2_burst12_GHz` = 80 [71, 91] qualified a second time and superseded for physical drives, its saturation key and ISI-ladder direction reconfirmed); [`notes/2026-07-22-cavity-ringdown-isi.md`](2026-07-22-cavity-ringdown-isi.md) (the 1-dB pp eye criterion, consumed); [`notes/2026-07-17-drive-sweep-knee-anchored.md`](2026-07-17-drive-sweep-knee-anchored.md) (the A_SAT anchors 0.0226/0.0150 and the active-cell-only normalization the knee-migration measurement adopts; the input-referred knee band 22‚Äì51 quanta for the launch ledger); [`notes/2026-07-21-composed-regeneration-envelope.md`](2026-07-21-composed-regeneration-envelope.md) + [`notes/2026-07-20-loaded-fanout-fixed-point.md`](2026-07-20-loaded-fanout-fixed-point.md) (the composed F = 2 reserve, re-derived at +2.012); [`notes/2026-07-13-kinetic-correction-signed-band.md`](2026-07-13-kinetic-correction-signed-band.md) (the ‚àí0.95 dB bulk term, booked in the ledger). It contests **no** `results.json` value and reopens **no** promoted key.

---

Reply to the winning prompt of **Fable Session ‚Äî 2026-07-31** (Fabric üßµ, 2-of-3 ‚Äî Kinetic ‚Üí Fabric, Quanta ‚Üí Fabric; Fabric ‚Üí Quanta). Labels are law: **demonstrated** (name the run and the observable), **in-model** (name the model and its assumptions), **open**.

> **Executing-model note.** Executed on **Claude Fable 5** (`claude-fable-5`) in the maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md) ‚Äî the routine's intended model, active for every pipeline stage. Every number below was produced by executing the released `fable-model-chain/` on this machine (Python 3 + numpy, macOS/CPython, `python3`); the ¬ß8 listings reproduce the spine. The custom driver imports the released integrator verbatim and was validated **bit-identical** to released `solver.run(drive_kind='prbs')` (max |cav diff| = 0.0 over 250,167 steps) and against three 07-25 probe rows to the digit before any new configuration was trusted.
>
> **Adversarial verification, disclosed.** Checked before posting by three blind, independent verification agents instructed to refute (reproduction / law-and-composition / promoted-record-and-labels lenses; the reproduction lens rebuilt the harness from ¬ß2's stated conventions alone, never opening this session's driver files, and re-ran the decisive rows at N = 480/720 plus a different seed). Verdicts **3√ó FIX-FIRST, 0 REFUTED**: no load-bearing verdict moved ‚Äî the independent harness reproduced the 91 GHz negative exactly (6.955/1.24/‚àí5.2) and confirmed both gated rungs above G_req with floors below ‚àí10 dB under two carrier-phase readings. The required fixes ‚Äî a mixed-grid floor contrast in the title/¬ß0.1, two missing convention statements (carrier-phase reference, knee host slot), five Richardson digits recomputed under one stated formula, a mislabeled demonstrated-over-composition clearance in ¬ß0.3, a one-directional "possibly conservative" framing in ¬ß0.2/¬ß5, the mischaracterized 07-23 F = 1/E4 status in ¬ß0.6, and the 11.8-dB floor-spec sensitivity of the m = 28 rung ‚Äî are applied in this text and itemized here so the diff is auditable. Non-required notes adopted: edge = 2 rt stated for flat rows; "4.13‚Äì4.20 dB" gain-flatness range; m = 26 floor ‚àí7.9; the fill-1/3 thermal wording; the knee-interpolation convention added to ¬ß5/¬ß8.

## 0. Executive verdict

1. **`f_max_F2_burst12_GHz` = 80 [71, 91] does not survive as a physical, data-gated operating point.** Its centre and upper edge fail three independent ways at the 91 GHz slot (m = 22 rt): (i) *demonstrated* ‚Äî the slot-filling drive's ISI pp is **1.24 dB at N = 720** (ladder 0.74/1.10/1.24), breaking the promoted 1-dB criterion the frontier is built on; (ii) *demonstrated* ‚Äî the slot-filling '0'-slot floor sits at **‚àí5.2 dB** below the mean-'1' level, a **5.0 dB give-back versus the released 3-cycle burst at the same grid** (‚àí10.2 at N = 720; 6.1 dB at N = 240: ‚àí6.6 vs ‚àí12.7): the drive that buys the gain hands the next slot an un-decayed field; (iii) *in-model over demonstrated ladders* ‚Äî the worst-case '1' gain grid-corrects to ‚âà 7.0‚Äì7.2 dB against the knee-migrated requirement G_req = 7.649 dB (see 3 below). Only the band's lower edge survives, and only in the duty-gated form below.
2. **The compression knee migrates with drive duration, decisively ‚Äî the pulse-knee convention is the wrong corner for a slot-filling burst.** *Demonstrated (active-cell-only, one fixed convention, N = 480):* the 1-dB knee drive amplitude falls **0.0430 (released 3-cycle) ‚Üí 0.0163 (ncyc = 12) ‚Üí 0.0175 (slot-filling flat, m = 22) ‚Üí 0.0132 (duty-0.8 gated, m = 30) ‚Üí 0.0111 (44-rt quasi-CW)** ‚Äî a √ó2.5‚Äì3.9 migration that puts every slot-filling drive at or beyond the CW-knee class. *In-model:* the operative F = 2 requirement for the physical E1 drive is therefore the **CW-knee corner, G_req = 7.649 dB** (re-derived to the digit from the promoted ledger before use). **7.649 is a corner assignment, not a bound, and the open direction cuts both ways:** the gated knees sit above this convention's own quasi-CW endpoint (suggesting a requirement below 7.649), but the measured burst-to-gated migration (√ó2.5‚Äì3.9) exceeds the ledger's pulse‚ÜíCW anchor ratio (√ó1.5), and in the ledger's pattern a lower knee means a *higher* requirement ‚Äî which would erase the thinner of the two rung clearances in item 3. The ¬ß7.2 streaming sweep decides it (open).
3. **A physical, slot-confined, data-gated launch exists that closes F = 2 ‚Äî at ‚âà 0.07 THz, not ‚âà 0.1 THz.** *Demonstrated:* a flat data-gated burst at **duty 0.8** (raised-cosine edges, 2 rt, '0' slots undriven, no modulo wrap) measures worst-case-'1' gain **7.68 dB (m = 28, N = 720; ladder 7.49/7.68)** and **7.93 dB (m = 30, N = 720; ladder 7.73/7.93)** with ISI pp 0.18/0.08 dB and '0'-floors ‚àí11.6/‚àí12.8 dB. *In-model composition (the corner assignment is item 2's; the exact gated G_req is open, ¬ß7.2):* against G_req = 7.649 the demonstrated rungs clear by **+0.03 dB (71 GHz)** and **+0.28 dB (67 GHz)**; an independent verification harness with the other carrier-phase reading lands +0.05/+0.23 ‚Äî the clearances are robust to the phase convention, their second digit is not. First-order Richardson margins +0.40/+0.68 dB are *in-model* and are not the load-bearing numbers. Composed key: **`f_max_F2_gated_GHz` = 69, band [63, 74]**; the demonstrated-rung window is **67‚Äì71 GHz**, with the 71 GHz edge additionally conditional on the floor-spec variant (item 4).
4. **The gating edges escape the 07-23 quiet-switching strike ‚Äî the feedthrough obstruction does not transfer to a signal-plane drive ‚Äî but the quiet requirement re-materializes as a waveform constraint.** *Demonstrated:* doubling the drive amplitude moves the relative '0'-floor by ‚â§ 0.4 dB (a bias-plane actuator transient would improve it by 6 dB), and an 8√ó edge-sharpness sweep (0.5 ‚Üí 4 rt) moves the floor only 1.7 dB: the contamination is signal-proportional ring-down bookkeeping, not switching feedthrough. What binds instead is the maintained field at slot end. *In-model:* requiring the '0'-floor ‚â• 10 dB below data forces **duty ‚â§ ‚âà 0.8** ‚Äî the signal-plane descendant of the 07-23 ¬ß1 quiet spec. **Spec sensitivity, disclosed:** the stricter variant anchored to the released `noise_margin_frac` = 0.2564 (‚â• 11.8 dB) strikes the m = 28 rung's measured floor (‚àí11.6 dB) by 0.2 dB and shrinks the demonstrated window to 67 GHz alone; the 67‚Äì71 GHz window rests on the round ‚â• 10 dB reading (m = 30, at ‚àí12.8 dB, passes both).
5. **The launch ledger is real but modest, and lands outside the fabric's headline energy figure.** *Demonstrated (waveform integrals):* the physical gated launch costs **√ó3.4‚Äì4.9 energy per '1'** versus the released 3-cycle burst ‚Äî but only **√ó1.25‚Äì1.30 time-averaged launch power**, because the slots stretch 2.75‚Äì3.75√ó. *In-model:* at the drive plane this multiplies the per-'1' launch quanta (input-referred knee band 22‚Äì51, per the 07-17 plane audit) by the same √ó3.4‚Äì4.9; the cost lands on the launch/clock subsystem, which `energy_per_add_fJ` explicitly excludes (chain README) ‚Äî the fabric-side thermal record (1.267 kW/cm¬≤ operating; ŒîT 55.5 K at fill 1/3, upper dissipation corner) is untouched by a 2√ó10‚Åª¬≥ boundary-density modulation.
6. **F = 1 at 91 GHz survives comfortably; the two-clock menu gains a middle option.** *In-model over demonstrated rows:* the duty-0.65 gated wire at m = 22 measures 5.94 dB worst-case (N = 240) with a +15.1 dB eye ‚Äî clearing the F = 1 CW corner (5.536 dB) by ‚âà +0.9 dB after the ladder transfer (the N = 240 rung alone carries +0.3‚Äì0.4 dB). On the 07-23 record, stated precisely: the *per-slot-flushed* 4-ps F = 1 wire is a convention razor there (closing only in the most favorable convention with zero reserve ‚Äî not "dead"), and the **E4 ping-pong 0.25-THz F = 1 transport option is left open by 07-23 ¬ß4 and is not re-adjudicated here**. What this session adds is a gated 91-GHz F = 1 wire needing no double buffering; the two-clock ratio is ‚âà 1.3√ó (91 over 67‚Äì71) if the crew declines E4's mux/area cost, or up to ‚âà 3.7√ó (250 over 67‚Äì71) if E4 survives its own open items. A design choice for the crew, not a claim.

Everything rides on the experimentally unproven gain cell (bench gate G1): this is a feasibility adjudication, not a performance claim.

## 1. Anchors and ledger ‚Äî demonstrated, re-derived to the digit

From the released chain on this machine before any new run: `M_th_353K` = 0.14708333333333332, `cw_regen_gain_dB_at_0p7` = 9.66100611708918, `noise_figure_floor_dB` = 2.768939660565078, `per_gate_loss_353K_dB` = 2.555099201864131, `pulse_gain_dB_at_0p7_streaming` = 7.7967069614868425 ‚Äî every value that exists as a `results.json` key matches bit-for-bit ‚Äî and the derived anchors recomputed from the released functions to the digit shown: `a_loss` = 0.7451522890452021, `loop_gain(0.7¬∑M_th)` = 0.9162026217341978, `regen.pulse_net_gain_dB(0.7)` = 6.258296289342312, rt = 0.5 ps, `f0_n` = 0.25. The promoted G_req ledger re-derives to the digit ‚Äî **7.649 / 7.056 / 6.515 dB (F = 2)**, **5.536 / 4.526 / 3.505 dB (F = 1)** ‚Äî and the 07-21 composed CW F = 2 reserve re-derives at **+2.012 dB** against its published +2.01. Gtrans(8) = 4.568, Gtrans(24) = 8.534 (in-model law, demonstrated anchors). Consumed, not contested.

**Premises source-read (per the record's own rule):** `solver._pulse_train` wraps its envelope with `phase = (t % period)` (solver.py:109) and `solver.run` never forwards `ncyc` (no `ncyc` in `run`'s signature; both call sites omit it) ‚Äî the two tracked WP1 warts stand as `ROADMAP.md` carries them; nothing in this session edits any released file.

## 2. Conventions and driver validation ‚Äî demonstrated

**Convention (fixed for every PRBS row):** observable `cav`; per-slot window [0.25, 0.72]¬∑repT; bias 0.7¬∑M_th_analytic = 0.10295833333333332; `drive_amp` = 2√ó10‚Åª¬≥ (except where swept); `cfl` = 0.4; bit pattern `default_rng(7).integers(0,2,40)`, first 4 slots dropped (36 scored); gain per '1' = 20¬∑log‚ÇÅ‚ÇÄ(slot peak vs the identical-pattern M = 0 run); **worst-case-'1'** statistic; eye = min-'1'/max-'0'; pp = raw '1'-level spread; '0'-floor = max-'0' referred to mean-'1'. This is the 07-25 convention, adopted unchanged so every number here is comparable to that note's tables.

**Validation:** (a) with the released wrapped-prbs drive, the custom stepping loop is **bit-identical** to released `solver.run` (max |cav difference| = 0.0 over 250,167 steps, m = 8, N = 240, 20 slots); (b) the 07-25 probe rows reproduce to the digit ‚Äî m = 8: eye **‚àí1.46**, pp **4.91**, G_worst1 **+3.05**; m = 16: eye **+7.61**, pp **1.03**; m = 22: eye **+12.51**, pp **0.27**, G_worst1 **+4.17**; (c) the isolated ncyc = 12 gain at N = 480 measures 7.216‚Äì7.233 dB over the swept amplitudes against that note's 7.220 ‚Äî same physics, window conventions 0.01-dB apart. Demonstrated.

**The physical waveforms (new, both slot-confined and data-gated ‚Äî no modulo wrap; '0' slots undriven):**
- `confG(ncyc)` ‚Äî Gaussian envelope from the slot's **own** centre (true time offset), zero outside its slot; FWHM = ncyc carrier periods;
- `flat(edge)` ‚Äî raised-cosine edges of `edge` rt fully inside the slot, flat between (slot-filling); **every flat row in ¬ß¬ß3‚Äì5 uses edge = 2 rt** except where the ¬ß3/¬ß4 tables or the edge sweep say otherwise;
- `duty(œÜ)` ‚Äî the flat envelope confined to the first œÜ of the slot, then off: the drive ends early and the cavity rings down before the next decision.

**Carrier-phase reference (load-bearing at the ~1 dB level for '0'-floor digits):** the carrier is sin(2œÄ¬∑f0_n¬∑(t ‚àí centre)) with **centre = the centre of the *active* envelope window** ‚Äî the slot centre for `confG` and `flat` (where the envelope spans the slot), but **0.5¬∑œÜ¬∑repT into the slot for `duty(œÜ)`** (0.4¬∑repT at duty 0.8). An independent verification harness measured the m = 28, N = 720 '0'-floor at ‚àí12.4 dB under slot-centre phasing versus ‚àí11.6 dB under this convention; gains move ‚â§ 0.06 dB and no verdict is phase-sensitive, but the printed floor digits are.

## 3. The slot sweep ‚Äî demonstrated (N = 240, ladders in ¬ß4)

Worst-case-'1' gain / ISI pp / eye / '0'-floor (dB), 36 scored slots:

| m (rt) | GHz | released wrapG-3 | confG-12 | flat (slot-filling) | duty 0.8 |
|---|---|---|---|---|---|
| 16 | 125 | 4.13 / 1.03 / +7.6 / ‚àí8.2 | 5.64 / 1.62 / +3.6 / ‚àí4.6 | 5.51 / 1.44 / +4.2 / ‚àí5.1 | ‚Äî |
| 20 | 100 | 4.16 / 0.45 / +11.3 / ‚àí11.5 | 6.00 / 1.10 / +5.7 / ‚àí6.3 | 6.06 / 1.10 / +5.8 / ‚àí6.5 | ‚Äî |
| 22 | 91 | 4.17 / 0.27 / +12.5 / ‚àí12.7 | 6.25 / 0.74 / +6.3 / ‚àí6.8 | 6.43 / 0.74 / +6.2 / ‚àí6.6 | 6.42 / 0.29 / +11.2 / ‚àí11.3 |
| 26 | 77 | 4.20 / 0.06 / +15.9 / ‚àí16.0 | 6.54 / 0.30 / +8.6 / ‚àí8.7 | 6.88 / 0.35 / +7.7 / ‚àí7.9 | 6.83 / 0.09 / +14.0 / ‚àí14.1 |
| 28 | 71 | 4.20 / 0.02 / +18.1 / ‚àí18.1 | 6.58 / 0.19 / +10.1 / ‚àí10.3 | 6.99 / 0.26 / +8.9 / ‚àí9.0 | (¬ß4 ladder) |
| 30 | 67 | ‚Äî | ‚Äî | ‚Äî | 7.12 / 0.04 / +15.7 / ‚àí15.7 |
| 32 | 62 | 4.16 / 0.06 / +20.8 / ‚àí20.8 | 6.63 / 0.06 / +12.4 / ‚àí12.4 | 7.15 / 0.13 / +10.1 / ‚àí10.2 | ‚Äî |

Readings, all demonstrated at this grid: (i) the released 3-cycle gain is flat at 4.13‚Äì4.20 dB from m = 16 to 32 (¬±0.04 dB over m = 20‚Äì32) ‚Äî the 07-25 saturation reconfirmed; (ii) the physical drives lift the worst-case gain by +2.1‚Äì3.0 dB but pay for it in the '0'-floor: slot-filling at m = 22 gives back **6.1 dB of floor** versus the released burst; (iii) **duty 0.8 keeps the slot-filling gain (6.42 vs 6.43 at m = 22) while recovering 4.7 dB of floor** ‚Äî the gain saturates in *drive duration* while the floor keeps improving as the drive ends earlier: the two legs decouple exactly as the 07-25 mechanism predicts; (iv) duty 0.5/0.65 at m = 22: 4.86/5.94 dB with floors ‚àí18.6/‚àí15.3 ‚Äî the F = 1 operating points.

## 4. Grid ladders ‚Äî the decisive rows

Worst-case-'1' gain (dB), N = 240 / 480 / 720; the Richardson column is the first-order (480, 720)-pair extrapolant **G‚àû = 3¬∑G720 ‚àí 2¬∑G480**, in-model throughout:

| row | 240 | 480 | 720 | Richardson | pp @720 | floor @720 |
|---|---|---|---|---|---|---|
| confG-3, m = 22 | 4.17 | 4.40 | 4.46 | 4.59 | 0.62 | ‚àí10.2 |
| confG-12, m = 22 | 6.25 | 6.63 | 6.77 | 7.03 | 1.22 | ‚àí5.3 |
| flat, m = 22 | 6.43 | 6.82 | 6.95 | 7.22 | **1.24** | **‚àí5.2** |
| confG-12, m = 28 | 6.58 | 7.06 | 7.22 | 7.55 | 0.49 | ‚àí8.3 |
| flat, m = 28 | 6.99 | 7.50 | 7.68 | 8.03 | 0.60 | ‚àí7.3 |
| **duty 0.8, m = 28** | ‚Äî | 7.49 | **7.68** | 8.05 | 0.18 | **‚àí11.6** |
| **duty 0.8, m = 30** | ‚Äî | 7.73 | **7.93** | 8.33 | 0.08 | **‚àí12.8** |

Two independent failures at 91 GHz are *demonstrated at the finest grid*: the slot-filling pp = 1.24 dB breaks the promoted 1-dB ISI criterion (the coarse grid flattered it at 0.74 ‚Äî the same LF-diffusion direction the 07-25 ISI ladder measured), and the floor sits at ‚àí5.2 dB. The duty-0.8 rows at m = 28/30 are the surviving configuration: pp and floor both healthy, and the gain at the **measured** N = 720 rungs ‚Äî 7.68 and 7.93 dB ‚Äî brackets the knee-migrated requirement 7.649. The thinness is priced in ¬ß7.1: the m = 28 rung clears by only +0.03 dB, and this memo declines to rest the verdict on the +0.40 extrapolated margin ‚Äî the honest statement is a **67‚Äì71 GHz demonstrated-rung window** whose lower rung carries +0.28 dB.

## 5. The knee migration ‚Äî measured

Active-cell-only compression (the 07-17 normalization: active response referred to its own linear limit, isolating the cell from the passive reference's expansion), isolated single '1' **in a long host slot** (m = 44 for the confG and quasi-CW rows, m = 22/30 for the operating-drive rows as labeled ‚Äî the confG-3 baseline is *not* reproducible in its native m = 8 slot, where the ¬ß2 window clips the response peak; results are host-slot-independent for m ‚â• 22), N = 480, this session's window convention. The 1-dB knee is the log-amplitude interpolation of the ‚àí1 dB crossing between bracketing amplitudes of the stated sweep (5√ó10‚Åª‚Å¥ ‚Ä¶ 4.5√ó10‚Åª¬≤, √ó1.4‚Äì2 spacing; linear reference = mean of the two smallest-amp responses); knee digits carry an interpolation-grid uncertainty of ‚âà 4 % in amplitude (an independent rerun read 0.0137 for the duty row's 0.0132):

| drive | duration (rt) | 1-dB knee amplitude | vs ncyc-3 |
|---|---|---|---|
| confG-3 (released burst) | 6 | **0.0430** | 1.0 |
| confG-12 | 24 | **0.0163** | √ó0.38 |
| flat, m = 22 (slot-filling) | ‚âà 20 | **0.0175** | √ó0.41 |
| duty 0.8, m = 30 | 24 | **0.0132** | √ó0.31 |
| flat, m = 44 (quasi-CW) | ‚âà 42 | **0.0111** | √ó0.26 |

Demonstrated: the knee migrates monotonically with drive duration, by √ó2.5‚Äì3.9 from the released burst to the physical operating drives ‚Äî larger than the √ó1.5 that separates the ledger's own pulse and CW anchors (A_SAT 0.0226 ‚Üí 0.0150, 07-17). **These absolute values must not be substituted into the ledger** ‚Äî this session's convention (isolated window, analytic bias) differs from 07-17's (streaming train, retuned `M_th_num` bias), and only the *migration* transfers. In-model conclusion: the compression corner for any slot-filling or duty-gated E1 drive is the **CW-knee corner, G_req(F = 2) = 7.649 dB** ‚Äî a corner assignment whose open residual cuts both ways (¬ß0.2): the gated knees sit above this convention's quasi-CW endpoint (suggesting a requirement below 7.649), while the migration overshoot of the ledger's pulse‚ÜíCW ratio suggests one above it, which would erase the thinner rung clearance. The exact G_req for the gated drive in the ledger's own streaming convention is **open** (the adoptable check, ¬ß7.2, closes it). The passive reference's own compression stays ‚â§ 0.12 dB out to amp 0.0226 (demonstrated), so the ratio-vs-active-only distinction, which ¬ß8's listing separates, does not move any verdict.

## 6. Keys, grading, and consequences

**Pre-registered keys** (collision-checked against both chains' `results.json` and every promoted note; falsification = an independent rerun of the ¬ß8 listings at the stated conventions landing outside the band):

- `phys_gated_worst1_gain_m28_duty0p8_dB` = **7.68** (N = 720 rung; ladder 7.49/7.68; Richardson 8.05 in-model). Band **[7.3, 8.3]**.
- `phys_gated_worst1_gain_m30_duty0p8_dB` = **7.93** (N = 720 rung; ladder 7.73/7.93; Richardson 8.33 in-model). Band **[7.5, 8.6]**.
- `phys_slotfill_worst1_gain_m22_dB` = **6.95** (N = 720 rung; ladder 6.43/6.82/6.95; Richardson 7.22 in-model). Band **[6.4, 7.4]**.
- `isi_pp_slotfill_m22_dB` = **1.24** (N = 720; ladder 0.74/1.10/1.24). Band **[0.9, 1.5]**. Breaks the 1-dB criterion at 91 GHz. **Demonstrated.**
- `gated_zero_floor_slotfill_m22_dB` = **‚àí5.2** (N = 720). Band **[‚àí7, ‚àí4]**. **Demonstrated.**
- `gated_zero_floor_duty0p8_m30_dB` = **‚àí12.8** (N = 720). Band **[‚àí15, ‚àí11]**. **Demonstrated.**
- `knee_migration_ratio_released_to_gated` = **√ó0.26‚Äì0.41** (active-only, fixed convention, N = 480). Band **[0.2, 0.5]**. **Demonstrated**; the corner assignment it forces is in-model.
- `f_max_F2_gated_GHz` = **69**, band **[63, 74]**; demonstrated-rung window **67‚Äì71** (the 71-GHz edge holds under the round ‚â• 10-dB floor spec; the noise-margin-anchored 11.8-dB variant leaves 67 alone ‚Äî ¬ß0.4). **In-model composition** (CW corner + 1-dB pp + floor spec over the ¬ß4 ladders).
- `launch_energy_per_one_multiplier` = **4.5** [3.4, 5.0] per '1'; `launch_power_multiplier_timeavg` = **1.3** [1.2, 1.4]. **Demonstrated integrals**, in-model composition.
- `F1_gated_wire_margin_m22_dB` = **+0.9** [0.3, 1.4] vs the F = 1 CW corner (duty 0.65, eye +15.1 measured at N = 240; ladder transfer in-model).

**Grading the record it consumes:** `f_max_F2_burst12_GHz` = 80 [71, 91] (07-25) is **qualified a second time and now superseded for physical drives** by `f_max_F2_gated_GHz`: its centre is again reached by no measurement, and its upper half fails the pp criterion and the floor at the finest grid. Its ISI-leg finding (coarse grids flatter the eye) is *reconfirmed and extended* ‚Äî pp at m = 22 grows 0.74 ‚Üí 1.24 across the ladder. `E1_gain_sat_slot_independent_ncyc3` = true is reconfirmed (gain flat 4.16‚Äì4.20 dB, m = 16‚Äì32). The 07-23 E1 row's "new element: none" now carries a second proviso beyond 07-25's burst scaling: the burst must also be **duty-gated and slot-confined** ‚Äî the no-flush escape needs launch-waveform discipline, though still no new *device* element.

**Part III consequence (in-model, honest):** the defensible headline is **‚âà 0.07 THz F = 2 logic** ‚Äî 67‚Äì71 GHz at demonstrated rungs under a duty-0.8, edge ‚â• 1 rt, slot-confined data-gated launch with a '0'-floor spec of ‚â• 10‚Äì12 dB below data ‚Äî with **91 GHz available as F = 1 transport** (+0.9 dB, +15 dB eye). The ‚âà 0.1 THz figure survives only under the pulse-knee convention that the measured knee migration rules out for slot-filling drives. The two-clock menu now reads: gated 91-GHz F = 1 wire over 67‚Äì71 GHz logic (ratio ‚âà 1.3√ó, no double buffering) ‚Äî or 07-23's E4 ping-pong 0.25-THz transport (ratio ‚âà 3.7√ó, mux/area cost, open items unadjudicated here) ‚Äî a design choice for the crew. Bench gate G1's load-bearing configuration is now a **gated duty-0.8 launch at ‚âà 70 GHz**: the cascade demo should drive exactly this waveform.

## 7. Limitations and open items

1. **The thinnest margin is priced for the positive this time.** The m = 28 rung clears G_req by +0.03 dB ‚Äî within any reasonable convention error. The verdict does not rest on it: m = 30 carries +0.28 dB at the measured rung, and the composed key's band [63, 74] contains the failure of m = 28 without falsifying the frontier. What would actually move the verdict is the open G_req item (next).
2. **The exact gated-drive G_req in the ledger's own convention is open.** The knee migration is demonstrated in one fixed convention; its mapping onto the ledger's streaming anchors is in-model. **Adoptable next check:** one streaming knee sweep of the duty-0.8 drive at m = 28‚Äì30 in the 07-17 convention (bias 0.7¬∑M_th_num, per-slot-mean estimator, amp sweep) ‚Äî a single afternoon run that pins `G_req_gated` exactly and collapses limitation 1 either way. Second, the released-chain plumbing it needs: forward `ncyc` through `solver.run` and add a `duty` gate ‚Äî the tracked WP1 items (`ROADMAP.md`) plus one flag.
3. **Single bit pattern** (seed 7, 36 scored slots). 07-25 measured 0.04 dB seed spread at m = 22; worst-case statistics over longer patterns may drift within the stated bands (open; bands padded).
4. **First-order Richardson on a first-order scheme** ‚Äî extrapolants labeled in-model throughout and never load-bearing; the 07-25 caution about no clean asymptotic regime applies unchanged.
5. **The floor spec anchor is in-model.** Tying the '0'-floor requirement to `noise_margin_frac` (‚àí11.8 dB) composes a slot-boundary residue with a static transfer margin; the bench convention for that composition is open.
6. **The solver carries no noise, no detuning re-scan** (07-25 measured detuning at 0.07 dB for pulsed drive ‚Äî consumed), and the quantum leg of the gated launch (thermal occupation of the '0'-floor at 353 K) remains the open quantum-tier question flagged since 07-23.
7. **Everything rides on the unproven gain cell** (bench gate G1).

## 8. Runnable listings

Self-contained apart from importing the released `fable-model-chain` (adjust `CHAIN`). `python3 fs_driver.py`-based; complete sources below. Run order: `anchors.py` (seconds), `validate.py` (~2 min), `experiments.py` (~35 min, 6-way parallel), `experiments2.py` (~20 min), `exp_duty.py` (~10 min).

*(The listings follow verbatim in the next comment: `anchors.py`, `fs_driver.py`, `validate.py`, `experiments.py` + `exp_duty.py` + `experiments2.py`, the energy-integral snippet, and the knee-interpolation snippet that turns `results2.jsonl`'s raw peaks into the ¬ß5 knee digits ‚Äî together, exactly the code that produced every number above.)*

‚Äî Session executor, Claude **Fable 5** (`claude-fable-5`), maintainer-operated per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md). A negative on the published band's centre and a 30 %-slower verified operating point is the honest result; the gated-launch spec it produces is the constructive one.

---

*[Promotion note: the reply above is reproduced verbatim from [discussion #83](https://github.com/ryoji-info/FableComputer/discussions/83); its ¬ß8 pointer "the next comment" refers to that discussion's second comment, reproduced here in full so the note is self-contained.]*

## ¬ß8 Runnable listings ‚Äî verbatim sources

The exact files that produced every number in the reply above. Self-contained apart from importing the released `fable-model-chain` (adjust `CHAIN`/paths). Run order and rough cost: `anchors.py` (seconds) ‚Üí `validate.py` (~2 min) ‚Üí `experiments.py` (~35 min, 6-way parallel) ‚Üí `exp_duty.py` (~10 min) ‚Üí `experiments2.py` (~20 min). Conventions are stated in ¬ß2 of the reply; the energy integrals of ¬ß0.5 are the 12-line snippet at the end.

### `anchors.py`

```python
# -*- coding: utf-8 -*-
# Fable Session 2026-07-31 ‚Äî Step 0: demonstrated anchors + G_req ledger re-derivation.
# Consumes: notes/2026-07-23-reset-switch-adjudication.md ¬ß7a formulas (verbatim logic).
import math, os, sys, json

CHAIN = "/Users/rxiii/Documents/GitHub/FableComputer/fable-model-chain"
sys.path.insert(0, CHAIN)
import constants as C, ds_cell as DS, regen as R, noise as NO

RES = json.load(open(os.path.join(CHAIN, "results.json"), encoding="utf-8"))

s = DS.plasmon_speed(); tau = C.tau(C.Tcap); L = DS.cell_length(s)
Mth = DS.M_threshold(L, s, tau)
a_loss = 10 ** (-DS.passive_loss_dB_per_half_lambda(tau) / 20.0)
loopM = R.loop_gain(0.7 * Mth); loop0 = R.loop_gain(0.0)
G_cw = R.cw_net_gain_dB(0.7)
rt_ps = 1.0 / (2 * C.f0) * 1e12
f0_n = C.f0 * L / s

print("== ANCHORS (vs results.json) ==")
print(f"M_th_353K        = {Mth!r}  (json {RES['M_th_353K']!r})")
print(f"M_th_num         = {RES['M_th_num']!r}")
print(f"a_loss           = {a_loss!r}")
print(f"loop(0.7*M_th)   = {loopM!r}")
print(f"cw_regen_gain    = {G_cw!r}  (json {RES['cw_regen_gain_dB_at_0p7']!r})")
print(f"NF floor         = {NO.noise_figure(10**(G_cw/10))!r}  (json {RES['noise_figure_floor_dB']!r})")
print(f"per_gate_loss353 = {DS.passive_loss_dB_per_half_lambda(tau)!r}  (json {RES['per_gate_loss_353K_dB']!r})")
print(f"pulse_net_gain_dB(0.7) = {R.pulse_net_gain_dB(0.7)!r}")
print(f"rt_ps = {rt_ps}, f0_n = {f0_n!r}, tau_n(353K) = {tau*s/L!r}")
print(f"operating bias 0.7*M_th = {0.7*Mth!r}")
print(f"dissipation_operating_kW_cm2 = {RES['dissipation_operating_kW_cm2']!r}")
print(f"dT_fill_third_upper_K = {RES['dT_fill_third_upper_K']!r}")
print(f"energy_per_add_fJ = {RES['energy_per_add_fJ']!r}")
print(f"pulse_gain_dB_at_0p7_streaming = {RES['pulse_gain_dB_at_0p7_streaming']!r}")

# ---- G_req ledger re-derivation (07-23 ¬ß3 formulas, 07-17 knee anchors) ----
A_SAT_CW, A_SAT_PU = 0.015002, 0.022575
knee_cw, knee_pu = 7.63, 8.64
x_cw = math.sqrt(10 ** ((G_cw - knee_cw) / 10) - 1)
x_pu = math.sqrt(10 ** ((G_cw - knee_pu) / 10) - 1)
A_op_cw = x_cw * A_SAT_CW; A_op_pu = x_pu * A_SAT_PU
def comp_dB(A_op, A_SAT, F):
    return -10 * math.log10(1 + (A_op / A_SAT) ** 2 / F)
BULK = -0.95
SPLIT2 = 10 * math.log10(2.0)
LOSS = DS.passive_loss_dB_per_half_lambda(tau)
print("\n== G_req LEDGER (must be 7.649/7.056/6.515 F=2; 5.536/4.526/3.505 F=1) ==")
reqs = {}
for lbl, A_op, A_SAT in (("CW-knee", A_op_cw, A_SAT_CW), ("pulse-knee", A_op_pu, A_SAT_PU)):
    c1 = -comp_dB(A_op, A_SAT, 1); c2 = -comp_dB(A_op, A_SAT, 2)
    reqs[("F2", lbl)] = c2 + (-BULK) + SPLIT2 + LOSS
    reqs[("F1", lbl)] = c1 + (-BULK) + LOSS
reqs[("F2", "small-signal")] = (-BULK) + SPLIT2 + LOSS
reqs[("F1", "small-signal")] = (-BULK) + LOSS
for k in sorted(reqs):
    print(f"  G_req[{k[0]}, {k[1]:12s}] = {reqs[k]:.3f} dB")
print(f"  A_op(CW) = {A_op_cw:.6f}  A_op(pulse) = {A_op_pu:.6f}")

# 07-21 composed CW F=2 reserve re-derivation (+2.01 target)
for lbl, A_op, A_SAT in (("CW", A_op_cw, A_SAT_CW),):
    g2 = G_cw + comp_dB(A_op, A_SAT, 2)
    m2 = g2 + BULK - SPLIT2 - LOSS
    print(f"  composed F=2 reserve ({lbl}, near-specular, bulk central) = {m2:+.3f} dB (target +2.01)")

# Gtrans law (07-23 ¬ß1)
def Gtrans_dB(n):
    return 20 * math.log10(((1 - loopM ** n) / (1 - loopM)) / ((1 - loop0 ** n) / (1 - loop0)))
print(f"\nGtrans(8) = {Gtrans_dB(8):.3f} (target 4.568); Gtrans(24) = {Gtrans_dB(24):.3f}")
json.dump({"Mth": Mth, "loopM": loopM, "loop0": loop0, "G_cw": G_cw, "f0_n": f0_n,
           "reqs": {f"{a}|{b}": v for (a, b), v in reqs.items()},
           "A_op_cw": A_op_cw, "A_op_pu": A_op_pu},
          open(os.path.join(os.path.dirname(__file__), "anchors.json"), "w"), indent=1)
print("wrote anchors.json")

```

### `fs_driver.py`

```python
# -*- coding: utf-8 -*-
"""Fable Session 2026-07-31 driver.

Imports the released integrator verbatim (solver._step_LF / _setup / _pulse_train)
and schedules only the source drive sig(t) ‚Äî the 07-23 ¬ß7b / 07-25 ¬ß7 technique.
run_custom() replicates released solver.run() stepping exactly; with the released
wrapped-prbs sig it must be bit-identical (validated in validate.py).

Physical (slot-confined, data-gated) waveforms:
  shape 'wrapG'  ‚Äî the RELEASED wrapped Gaussian prbs (for validation/baseline)
  shape 'confG'  ‚Äî slot-confined Gaussian: env from the slot's OWN centre (true
                   time offset, no modulo wrap), zero outside its slot; '0' slots
                   undriven. ncyc sets FWHM = ncyc carrier periods.
  shape 'flat'   ‚Äî data-gated flat-top: raised-cosine edges of edge_rt round
                   trips fully inside the slot, flat between; '0' slots undriven.
Carrier: sin(2*pi*f0_n*(t - slot_centre)) ‚Äî slot-coherent (repT = m/2 carrier
periods, integer for even m; stated per row otherwise).
"""
import sys, math
import numpy as np

CHAIN = "/Users/rxiii/Documents/GitHub/FableComputer/fable-model-chain"
sys.path.insert(0, CHAIN)
import constants as C
import solver as SOL
from solver import _setup, _step_LF, _pulse_train


def make_sig(shape, bits, repT, f0_n, amp, ncyc=3, edge_rt=1.0):
    """Return sig(t) for the chosen drive shape. bits: 0/1 array by slot index."""
    width = ncyc / f0_n                 # FWHM in time units (= ncyc carrier periods)
    sigma = width / 2.355
    edge = edge_rt * 2.0                # rt -> time units

    if shape == "wrapG":                # released convention (modulo wrap)
        def sig(t):
            slot = int(t / repT)
            b = bits[slot] if slot < len(bits) else 0
            return _pulse_train(t, f0_n, amp, rep_ratio=1.0 / (repT * f0_n)) if b else 0.0
        return sig

    if shape == "confG":                # slot-confined Gaussian, true offset
        def sig(t):
            slot = int(t / repT)
            b = bits[slot] if slot < len(bits) else 0
            if not b:
                return 0.0
            tc = (slot + 0.5) * repT
            env = math.exp(-0.5 * ((t - tc) / sigma) ** 2)
            return amp * env * math.sin(2 * math.pi * f0_n * (t - tc))
        return sig

    if shape == "flat":                 # data-gated flat-top, raised-cosine edges
        def sig(t):
            slot = int(t / repT)
            b = bits[slot] if slot < len(bits) else 0
            if not b:
                return 0.0
            t0 = slot * repT
            x = t - t0
            if x < edge:
                env = 0.5 * (1 - math.cos(math.pi * x / edge))
            elif x > repT - edge:
                env = 0.5 * (1 - math.cos(math.pi * (repT - x) / edge))
            else:
                env = 1.0
            tc = t0 + 0.5 * repT
            return amp * env * math.sin(2 * math.pi * f0_n * (t - tc))
        return sig

    raise ValueError(shape)


def run_custom(M, N, n_roundtrips, sigfun, cfl=0.4, T=C.Tcap):
    """Replicates released solver.run() stepping verbatim, custom source drive."""
    s, tau, L, tau_n, f0n = _setup(N, T)
    u0 = M
    dx = 1.0 / N
    cmax = 1.0 + abs(u0) + 0.2
    dt = cfl * dx / cmax
    nsteps = int(n_roundtrips * 2.0 / dt)
    h = np.ones(N); hu = np.ones(N) * u0
    out = np.empty(nsteps); tarr = np.empty(nsteps); cav = np.empty(nsteps)
    t = 0.0
    for k in range(nsteps):
        h_left = 1.0 + sigfun(t)
        h, hu = _step_LF(h, hu, dx, dt, u0, tau_n, h_left, u0)
        if not np.all(np.isfinite(h)) or np.any(h < 1e-6):
            out = out[:k]; tarr = tarr[:k]; cav = cav[:k]; break
        out[k] = hu[-1] / h[-1] - u0
        cav[k] = np.max(np.abs(hu / h - u0))
        tarr[k] = t
        t += dt
    return dict(t=tarr, drain=out, cav=cav, dt=dt, f0_n=f0n)


def slot_peaks(r, repT, nslots, w_lo=0.25, w_hi=0.72):
    """Per-slot peak of cav in the window [w_lo, w_hi]*repT (07-25 convention)."""
    t, cav = r["t"], r["cav"]
    pks = []
    for k in range(nslots):
        m = (t >= (k + w_lo) * repT) & (t < (k + w_hi) * repT)
        pks.append(np.max(cav[m]) if m.sum() > 3 else np.nan)
    return np.array(pks)


def measure(bits, pk_M, pk_0, drop=4):
    """07-25 metrics: worst/mean '1' gain (vs identical-pattern M=0 run),
    eye (min'1' vs max'0'), pp (max'1'/min'1'), plus '0'-slot contamination."""
    b = np.asarray(bits[drop:len(pk_M)])
    pM = pk_M[drop:]; p0 = pk_0[drop:]
    ones = b == 1; zeros = b == 0
    res = {}
    if ones.any():
        g = 20 * np.log10(pM[ones] / p0[ones])
        res["G_worst1_dB"] = float(np.min(g))
        res["G_mean1_dB"] = float(np.mean(g))
        res["pp_dB"] = float(np.max(g) - np.min(g))
        res["mean1_level"] = float(np.mean(pM[ones]))
    if ones.any() and zeros.any():
        res["eye_dB"] = float(20 * np.log10(np.min(pM[ones]) / np.max(pM[zeros])))
        res["max0_below_mean1_dB"] = float(
            20 * np.log10(np.max(pM[zeros]) / np.mean(pM[ones])))
    return res


def default_bits(nslots=40, seed=7):
    return np.random.default_rng(seed).integers(0, 2, nslots)

```

### `validate.py`

```python
# -*- coding: utf-8 -*-
# Step 1 ‚Äî driver validation.
# (a) bit-identity of run_custom vs released solver.run(drive_kind='prbs')
# (b) reproduce the 07-25 probe rows: m=8: eye -1.46, pp 4.91, G_worst1 +3.05;
#     m=16: eye +7.61, pp 1.03; m=22: eye +12.51, pp 0.27, G_worst1 +4.17.
import sys, json, time
import numpy as np
from fs_driver import (CHAIN, SOL, make_sig, run_custom, slot_peaks, measure,
                       default_bits)
sys.path.insert(0, CHAIN)
import ds_cell as DS, constants as C

s = DS.plasmon_speed(); tau = C.tau(C.Tcap); L = DS.cell_length(s)
Mth = DS.M_threshold(L, s, tau)
BIAS = 0.7 * Mth
AMP = 2e-3
NS = 40

f0_n = C.f0 * L / s          # 0.25

# ---------- (a) bit-identity at m=8 (rep_ratio 0.25), N=240, 20 slots ----------
bits = default_bits(20, seed=7)
m = 8; repT = 2.0 * m; rr = 1.0 / (repT * f0_n)
nrt = 20 * m
r_rel = SOL.run(BIAS, N=240, n_roundtrips=nrt, drive_amp=AMP, drive_kind="prbs",
                cfl=0.4, seed=7, rep_ratio=rr, bits=bits)
sig = make_sig("wrapG", bits, repT, f0_n, AMP)
r_cus = run_custom(BIAS, 240, nrt, sig)
n = min(len(r_rel["cav"]), len(r_cus["cav"]))
d = np.max(np.abs(r_rel["cav"][:n] - r_cus["cav"][:n]))
print(f"(a) bit-identity: max|cav_released - cav_custom| = {d!r} over {n} steps")

# ---------- (b) probe rows, full 07-25 convention (40 slots, drop 4) ----------
bits40 = default_bits(NS, seed=7)
for m, tag in ((8, "m=8"), (16, "m=16"), (22, "m=22")):
    t0 = time.time()
    repT = 2.0 * m
    nrt = NS * m
    sig = make_sig("wrapG", bits40, repT, f0_n, AMP)
    rM = run_custom(BIAS, 240, nrt, sig)
    r0 = run_custom(0.0, 240, nrt, sig)
    pM = slot_peaks(rM, repT, NS); p0 = slot_peaks(r0, repT, NS)
    res = measure(bits40, pM, p0)
    print(f"(b) {tag}: eye {res.get('eye_dB', float('nan')):+.2f}  "
          f"pp {res.get('pp_dB', float('nan')):.2f}  "
          f"G_worst1 {res.get('G_worst1_dB', float('nan')):+.2f}  "
          f"G_mean1 {res.get('G_mean1_dB', float('nan')):+.2f}   "
          f"[{time.time()-t0:.0f}s]")
print("targets:  m=8: eye -1.46 pp 4.91 G_worst1 +3.05 | m=16: eye +7.61 pp 1.03 | m=22: eye +12.51 pp 0.27 G_worst1 +4.17")

```

### `experiments.py`

```python
# -*- coding: utf-8 -*-
"""Fable Session 2026-07-31 ‚Äî main experiment battery.

A: physical-drive slot sweep at N=240 (confG3, confG12, flat1, flat2 vs wrapG3)
B: grid ladders (N=480, 720) on decisive rows (m=22, 28)
C: knee vs ncyc (isolated burst, amp sweep, N=480) + flat knee at m=22
D: edge-sharpness feedthrough sweep (flat, m=22, edge 0.5/1/2/4 rt)
E: drive-energy integrals (cheap, analytic-numeric)

Conventions (fixed): bias 0.7*M_th_analytic; amp 2e-3 unless swept; 40 slots,
seed 7, drop 4; window [0.25, 0.72]*repT; gain vs identical-pattern M=0 run;
pp = raw '1'-level spread (validated 4.91/1.03/0.26 vs 07-25).
"""
import json, math, os, sys, time
import numpy as np
from multiprocessing import Pool

from fs_driver import make_sig, run_custom, slot_peaks, default_bits, CHAIN
sys.path.insert(0, CHAIN)
import ds_cell as DS, constants as C

s = DS.plasmon_speed(); tau = C.tau(C.Tcap); L = DS.cell_length(s)
Mth = DS.M_threshold(L, s, tau)
BIAS = 0.7 * Mth
F0N = C.f0 * L / s
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.jsonl")


def metrics(bits, pk_M, pk_0, drop=4):
    b = np.asarray(bits[drop:len(pk_M)])
    pM = pk_M[drop:len(pk_M)]; p0 = pk_0[drop:len(pk_M)]
    ones = b == 1; zeros = b == 0
    res = {}
    if ones.any():
        g = 20 * np.log10(pM[ones] / p0[ones])
        res["G_worst1_dB"] = float(np.min(g))
        res["G_mean1_dB"] = float(np.mean(g))
        res["pp_raw_dB"] = float(20 * np.log10(np.max(pM[ones]) / np.min(pM[ones])))
    if ones.any() and zeros.any():
        res["eye_dB"] = float(20 * np.log10(np.min(pM[ones]) / np.max(pM[zeros])))
        res["max0_below_mean1_dB"] = float(20 * np.log10(np.max(pM[zeros]) / np.mean(pM[ones])))
    return res


def row_prbs(cfg):
    """One prbs measurement row: (shape, ncyc/edge, m, N, amp) -> metrics."""
    t0 = time.time()
    m, N, amp = cfg["m"], cfg["N"], cfg.get("amp", 2e-3)
    nslots = cfg.get("nslots", 40)
    repT = 2.0 * m
    bits = default_bits(nslots, cfg.get("seed", 7))
    sig = make_sig(cfg["shape"], bits, repT, F0N, amp,
                   ncyc=cfg.get("ncyc", 3), edge_rt=cfg.get("edge_rt", 1.0))
    nrt = nslots * m
    rM = run_custom(BIAS, N, nrt, sig)
    r0 = run_custom(0.0, N, nrt, sig)
    pM = slot_peaks(rM, repT, nslots); p0 = slot_peaks(r0, repT, nslots)
    res = dict(cfg)
    res.update(metrics(bits, pM, p0))
    res["secs"] = round(time.time() - t0, 1)
    return res


def row_knee(cfg):
    """Isolated single-'1' gain at one amp: bits [0,1,0,...], slot m, shape."""
    t0 = time.time()
    m, N, amp = cfg["m"], cfg["N"], cfg["amp"]
    repT = 2.0 * m
    bits = np.array([0, 1, 0, 0])
    sig = make_sig(cfg["shape"], bits, repT, F0N, amp,
                   ncyc=cfg.get("ncyc", 3), edge_rt=cfg.get("edge_rt", 1.0))
    nrt = 4 * m
    rM = run_custom(BIAS, N, nrt, sig)
    r0 = run_custom(0.0, N, nrt, sig)
    pM = slot_peaks(rM, repT, 4); p0 = slot_peaks(r0, repT, 4)
    res = dict(cfg)
    res["G_iso_dB"] = float(20 * np.log10(pM[1] / p0[1]))
    res["secs"] = round(time.time() - t0, 1)
    return res


def dispatch(cfg):
    try:
        return row_knee(cfg) if cfg["kind"] == "knee" else row_prbs(cfg)
    except Exception as e:
        out = dict(cfg); out["error"] = repr(e)
        return out


def main():
    jobs = []
    # ---- A: slot sweep, N=240 ----
    for m in (16, 20, 22, 26, 28, 32):
        jobs.append({"kind": "prbs", "shape": "wrapG", "ncyc": 3, "m": m, "N": 240, "exp": "A"})
        jobs.append({"kind": "prbs", "shape": "confG", "ncyc": 3, "m": m, "N": 240, "exp": "A"})
        jobs.append({"kind": "prbs", "shape": "confG", "ncyc": 12, "m": m, "N": 240, "exp": "A"})
        jobs.append({"kind": "prbs", "shape": "flat", "edge_rt": 1.0, "m": m, "N": 240, "exp": "A"})
        jobs.append({"kind": "prbs", "shape": "flat", "edge_rt": 2.0, "m": m, "N": 240, "exp": "A"})
    # ---- B: grid ladders on decisive rows ----
    for m in (22, 28):
        for N in (480, 720):
            jobs.append({"kind": "prbs", "shape": "confG", "ncyc": 12, "m": m, "N": N, "exp": "B"})
            jobs.append({"kind": "prbs", "shape": "flat", "edge_rt": 2.0, "m": m, "N": N, "exp": "B"})
    jobs.append({"kind": "prbs", "shape": "confG", "ncyc": 3, "m": 22, "N": 480, "exp": "B"})
    jobs.append({"kind": "prbs", "shape": "confG", "ncyc": 3, "m": 22, "N": 720, "exp": "B"})
    # ---- D: edge sweep, m=22, N=240 + one N=480 check ----
    for e in (0.5, 4.0):
        jobs.append({"kind": "prbs", "shape": "flat", "edge_rt": e, "m": 22, "N": 240, "exp": "D"})
    jobs.append({"kind": "prbs", "shape": "flat", "edge_rt": 0.5, "m": 22, "N": 480, "exp": "D"})
    # amp-scaling check for contamination linearity (flat, edge 1, m=22, amp 4e-3)
    jobs.append({"kind": "prbs", "shape": "flat", "edge_rt": 1.0, "m": 22, "N": 240,
                 "amp": 4e-3, "exp": "D"})
    # ---- C: knee vs ncyc (confG isolated, m=44, N=480) ----
    AMPS = [5e-4, 1e-3, 2e-3, 4e-3, 7e-3, 1.1e-2, 1.7e-2, 2.26e-2, 3.2e-2, 4.5e-2]
    for ncyc in (3, 6, 12, 18):
        for amp in AMPS:
            jobs.append({"kind": "knee", "shape": "confG", "ncyc": ncyc, "m": 44,
                         "N": 480, "amp": amp, "exp": "C"})
    # flat knee at the operating slot m=22 (edge 2 rt)
    for amp in AMPS:
        jobs.append({"kind": "knee", "shape": "flat", "edge_rt": 2.0, "m": 22,
                     "N": 480, "amp": amp, "exp": "C"})
    # CW-limit reference knee: flat drive nearly filling a long slot (m=44)
    for amp in AMPS:
        jobs.append({"kind": "knee", "shape": "flat", "edge_rt": 2.0, "m": 44,
                     "N": 480, "amp": amp, "exp": "C"})

    print(f"{len(jobs)} jobs")
    with open(OUT, "w") as f:
        with Pool(6) as pool:
            for res in pool.imap_unordered(dispatch, jobs):
                f.write(json.dumps(res) + "\n")
                f.flush()
                tag = {k: v for k, v in res.items() if k in
                       ("exp", "shape", "ncyc", "edge_rt", "m", "N", "amp")}
                print(tag, {k: round(v, 3) for k, v in res.items() if isinstance(v, float)
                            and k != "amp"}, flush=True)
    print("DONE")


if __name__ == "__main__":
    main()

```

### `exp_duty.py`

```python
# -*- coding: utf-8 -*-
# Experiment F: partial-duty flat drive ‚Äî burst fills [0, duty]*slot then stops.
# Tests the gain-vs-'0'-floor tradeoff the slot-filling seam forces.
import json, math, os, sys, time
import numpy as np
from multiprocessing import Pool
from fs_driver import run_custom, slot_peaks, default_bits, CHAIN
sys.path.insert(0, CHAIN)
import ds_cell as DS, constants as C

s = DS.plasmon_speed(); tau = C.tau(C.Tcap); L = DS.cell_length(s)
Mth = DS.M_threshold(L, s, tau)
BIAS = 0.7 * Mth
F0N = C.f0 * L / s
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_duty.jsonl")


def make_sig_duty(bits, repT, f0_n, amp, duty, edge_rt=2.0):
    edge = edge_rt * 2.0
    span = duty * repT

    def sig(t):
        slot = int(t / repT)
        b = bits[slot] if slot < len(bits) else 0
        if not b:
            return 0.0
        x = t - slot * repT
        if x >= span:
            return 0.0
        if x < edge:
            env = 0.5 * (1 - math.cos(math.pi * x / edge))
        elif x > span - edge:
            env = 0.5 * (1 - math.cos(math.pi * (span - x) / edge))
        else:
            env = 1.0
        tc = slot * repT + 0.5 * span
        return amp * env * math.sin(2 * math.pi * f0_n * (t - tc))
    return sig


def row(cfg):
    t0 = time.time()
    m, N, duty = cfg["m"], cfg["N"], cfg["duty"]
    repT = 2.0 * m
    nslots = 40
    bits = default_bits(nslots, 7)
    sig = make_sig_duty(bits, repT, F0N, cfg.get("amp", 2e-3), duty)
    nrt = nslots * m
    rM = run_custom(BIAS, N, nrt, sig)
    r0 = run_custom(0.0, N, nrt, sig)
    pM = slot_peaks(rM, repT, nslots); p0 = slot_peaks(r0, repT, nslots)
    b = np.asarray(bits[4:]); pMd = pM[4:]; p0d = p0[4:]
    ones = b == 1; zeros = b == 0
    g = 20 * np.log10(pMd[ones] / p0d[ones])
    res = dict(cfg)
    res["G_worst1_dB"] = float(np.min(g)); res["G_mean1_dB"] = float(np.mean(g))
    res["pp_raw_dB"] = float(20 * np.log10(np.max(pMd[ones]) / np.min(pMd[ones])))
    res["eye_dB"] = float(20 * np.log10(np.min(pMd[ones]) / np.max(pMd[zeros])))
    res["max0_below_mean1_dB"] = float(20 * np.log10(np.max(pMd[zeros]) / np.mean(pMd[ones])))
    res["secs"] = round(time.time() - t0, 1)
    return res


if __name__ == "__main__":
    jobs = []
    for m in (22, 26, 30):
        for duty in (0.5, 0.65, 0.8):
            jobs.append({"m": m, "N": 240, "duty": duty, "exp": "F"})
    # one ladder point on the most promising row is added later by hand if needed
    with open(OUT, "w") as f:
        with Pool(3) as pool:
            for res in pool.imap_unordered(row, jobs):
                f.write(json.dumps(res) + "\n"); f.flush()
                print({k: (round(v, 3) if isinstance(v, float) else v)
                       for k, v in res.items()}, flush=True)
    print("DONE")

```

### `experiments2.py`

```python
# -*- coding: utf-8 -*-
"""Follow-up battery: (C2) active-cell-only knees (07-17 normalization) with raw
peaks stored; (B2) grid ladders on the duty-0.8 constructive frontier rows."""
import json, math, os, sys, time
import numpy as np
from multiprocessing import Pool

from fs_driver import make_sig, run_custom, slot_peaks, default_bits, CHAIN
from exp_duty import make_sig_duty
sys.path.insert(0, CHAIN)
import ds_cell as DS, constants as C

s = DS.plasmon_speed(); tau = C.tau(C.Tcap); L = DS.cell_length(s)
Mth = DS.M_threshold(L, s, tau)
BIAS = 0.7 * Mth
F0N = C.f0 * L / s
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results2.jsonl")


def row_knee2(cfg):
    """Isolated '1' ‚Äî store raw active and passive slot peaks for active-only comp."""
    t0 = time.time()
    m, N, amp = cfg["m"], cfg["N"], cfg["amp"]
    repT = 2.0 * m
    bits = np.array([0, 1, 0, 0])
    if cfg["shape"] == "duty":
        sig = make_sig_duty(bits, repT, F0N, amp, cfg["duty"])
    else:
        sig = make_sig(cfg["shape"], bits, repT, F0N, amp,
                       ncyc=cfg.get("ncyc", 3), edge_rt=cfg.get("edge_rt", 2.0))
    nrt = 4 * m
    rM = run_custom(BIAS, N, nrt, sig)
    r0 = run_custom(0.0, N, nrt, sig)
    pM = slot_peaks(rM, repT, 4); p0 = slot_peaks(r0, repT, 4)
    res = dict(cfg)
    res["pk_act"] = float(pM[1]); res["pk_pas"] = float(p0[1])
    res["G_iso_dB"] = float(20 * np.log10(pM[1] / p0[1]))
    res["secs"] = round(time.time() - t0, 1)
    return res


def row_duty_prbs(cfg):
    t0 = time.time()
    m, N, duty = cfg["m"], cfg["N"], cfg["duty"]
    repT = 2.0 * m
    nslots = 40
    bits = default_bits(nslots, 7)
    sig = make_sig_duty(bits, repT, F0N, cfg.get("amp", 2e-3), duty)
    nrt = nslots * m
    rM = run_custom(BIAS, N, nrt, sig)
    r0 = run_custom(0.0, N, nrt, sig)
    pM = slot_peaks(rM, repT, nslots); p0 = slot_peaks(r0, repT, nslots)
    b = np.asarray(bits[4:]); pMd = pM[4:]; p0d = p0[4:]
    ones = b == 1; zeros = b == 0
    g = 20 * np.log10(pMd[ones] / p0d[ones])
    res = dict(cfg)
    res["G_worst1_dB"] = float(np.min(g)); res["G_mean1_dB"] = float(np.mean(g))
    res["pp_raw_dB"] = float(20 * np.log10(np.max(pMd[ones]) / np.min(pMd[ones])))
    res["eye_dB"] = float(20 * np.log10(np.min(pMd[ones]) / np.max(pMd[zeros])))
    res["max0_below_mean1_dB"] = float(20 * np.log10(np.max(pMd[zeros]) / np.mean(pMd[ones])))
    res["secs"] = round(time.time() - t0, 1)
    return res


def dispatch(cfg):
    try:
        return row_knee2(cfg) if cfg["kind"] == "knee2" else row_duty_prbs(cfg)
    except Exception as e:
        out = dict(cfg); out["error"] = repr(e)
        return out


if __name__ == "__main__":
    AMPS = [5e-4, 1e-3, 2e-3, 4e-3, 7e-3, 1.1e-2, 1.7e-2, 2.26e-2, 3.2e-2, 4.5e-2]
    jobs = []
    # C2: active-only knees ‚Äî the four decisive drive shapes
    for shape, kw in (("confG", {"ncyc": 3, "m": 44}),
                      ("confG", {"ncyc": 12, "m": 44}),
                      ("flat", {"edge_rt": 2.0, "m": 22}),
                      ("flat", {"edge_rt": 2.0, "m": 44}),
                      ("duty", {"duty": 0.8, "m": 30})):
        for amp in AMPS:
            j = {"kind": "knee2", "shape": shape, "N": 480, "amp": amp, "exp": "C2"}
            j.update(kw); jobs.append(j)
    # B2: duty-0.8 ladders on the constructive frontier
    for m in (28, 30):
        for N in (480, 720):
            jobs.append({"kind": "dutyprbs", "m": m, "N": N, "duty": 0.8, "exp": "B2"})
    print(f"{len(jobs)} jobs")
    with open(OUT, "w") as f:
        with Pool(6) as pool:
            for res in pool.imap_unordered(dispatch, jobs):
                f.write(json.dumps(res) + "\n"); f.flush()
                print({k: (round(v, 4) if isinstance(v, float) else v)
                       for k, v in res.items() if k != "pk_pas"}, flush=True)
    print("DONE")

```

### energy integrals (¬ß0.5)

```python
import numpy as np
from exp_duty import make_sig_duty
from fs_driver import make_sig
F0N = 0.25
def E(sigf, repT):
    t = np.arange(0, repT, 1e-3)
    v = np.array([sigf(x) for x in t]); return float(np.sum(v**2)*1e-3)
E0 = E(make_sig("wrapG", [1], 16.0, F0N, 1.0), 16.0)   # released ncyc3 @ m=8
for m, duty in ((22,0.8),(26,0.8),(28,0.8),(30,0.8),(30,0.65)):
    repT = 2.0*m
    e = E(make_sig_duty([1], repT, F0N, 1.0, duty), repT)
    print(f"duty{duty} m={m}: E/E0={e/E0:5.2f}  power x {(e/repT)/(E0/16.0):5.2f}")
```

### knee interpolation (¬ß5)

```python
import json, math, collections
import numpy as np
rows = [json.loads(l) for l in open("results2.jsonl")]
groups = collections.defaultdict(list)
for r in rows:
    if r.get("exp") == "C2":
        groups[(r["shape"], r.get("ncyc"), r.get("duty"), r["m"])].append(
            (r["amp"], r["pk_act"]))
for key in sorted(groups, key=str):
    pts = sorted(groups[key])
    lin = np.mean([20*math.log10(p/a) for a, p in pts[:2]])   # linear reference
    comp = [(a, 20*math.log10(p/a) - lin) for a, p in pts]    # active-only compression
    for i in range(len(comp)-1):
        c1, c2 = -comp[i][1], -comp[i+1][1]
        if c1 < 1.0 <= c2:                                    # 1-dB crossing
            a1, a2 = comp[i][0], comp[i+1][0]
            knee = math.exp(math.log(a1) + (math.log(a2)-math.log(a1))*(1-c1)/(c2-c1))
            print(key, f"knee = {knee:.4f}")
```



---

## Agent assessment ‚Äî 2026-07-31

Assessed suitable for the permanent record by a **3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)); each assessor independently re-executed key numbers against the released chain before voting:

- üßµ **Fabric** ‚Äî **STORE**: I re-executed the memo's spine myself before voting, and it holds to the digit: the published listings (byte-identical to the session's files) re-derive every ¬ß1 anchor and the full G_req ledger bit-for-bit against the released chain, my own runs of the three decisive measured rows at N=480 reproduce the memo's ladder rungs exactly (flat m=22: 6.8201/1.0962/‚àí5.53; duty-0.8 m=28: 7.4932; m=30: 7.7294), and the ¬ß5 knee digits fall out of the session's raw peaks under the stated interpolation exactly (0.0430/0.0163/0.0175/0.0132/0.0111). The result is substantive and corrective in precisely the way the record rewards: it retires the physical reading of 07-25's in-model 80 [71, 91] GHz key with two independent demonstrated failures at the finest grid, replaces it with a demonstrated, falsifiable gated operating point at 67‚Äì71 GHz, and prices the launch energy the record had twice named as open. Epistemic labels are law-grade ‚Äî Richardson extrapolants are in-model and never load-bearing, the CW-corner assignment is stated as an assignment with its open residual cutting both ways, and the thinnest margin (+0.03 dB at m=28) is disclosed and explicitly not rested on. It consumes the corrected record faithfully: the 07-23 E4/F=1 characterizations match that note verbatim, the 07-25 seed-spread/detuning figures are quoted correctly, no results.json value is contested, and all pre-registered key names grep collision-free. Durability is clear ‚Äî the ¬ß7.2 streaming knee sweep and the ncyc/duty plumbing are exactly what WP1 does next, and bench gate G1's target configuration changes. A negative on the headline stated this honestly, with a constructive replacement and runnable listings, is what the permanent record is for.
  - The 71-GHz edge of the demonstrated window is doubly conditional ‚Äî the m=28 rung clears G_req by only +0.03 dB (within convention error) and its ‚àí11.6 dB floor fails the noise-margin-anchored 11.8-dB spec variant by 0.2 dB ‚Äî so the robust demonstrated point is 67 GHz alone (m=30: +0.28 dB, passes both floor specs); the memo discloses both conditions but the title's "67‚Äì71 GHz" leads with the fragile edge.
  - Both rung clearances are conditional on the CW-corner assignment while the exact gated-drive G_req in the ledger's streaming convention is open (¬ß7.2); the measured migration overshoot (√ó2.5‚Äì3.9 vs the ledger's √ó1.5 pulse-to-CW ratio) points in the direction that would raise the requirement and erase the m=28 clearance ‚Äî the promotion should carry the ¬ß7.2 streaming knee sweep as a required follow-up, not merely an adoptable item.
  - `F1_gated_wire_margin_m22_dB` = +0.9 is the weakest-grounded pre-registered key: it composes an in-model ladder transfer onto a single N=240 rung (measured margin at that rung is +0.40 dB) with no measured N=480/720 ladder for the duty-0.65 drive.
  - Knee digits carry a ~4% interpolation-grid uncertainty from the coarse √ó1.4‚Äì2 amplitude spacing (disclosed; an independent rerun read 0.0137 vs 0.0132) ‚Äî the migration ratio is robust but the absolute ¬ß5 digits should not be quoted beyond two significant figures downstream.
  - *Re-executed:* Extracted the published ¬ß8 listings from the discussion comment and diffed them against the session's actual driver files: byte-identical apart from one trailing blank line per file ‚Äî the published code is exactly what ran.; anchors.py against the released fable-model-chain: all ¬ß1 anchors bit-for-bit (M_th_353K 0.14708333333333332, cw_regen_gain 9.66100611708918, NF floor 2.768939660565078, per_gate_loss 2.555099201864131, a_loss 0.7451522890452021, loop(0.7¬∑M_th) 0.9162026217341978, pulse_net_gain 6.258296289342312, rt 0.5 ps, f0_n 0.25); G_req ledger F=2 7.649/7.056/6.515 dB and F=1 5.536/4.526/3.505 dB to the digit; composed CW F=2 reserve +2.012 dB (target +2.01); Gtrans(8)=4.568, Gtrans(24)=8.534.; My own invocation of the row functions (myrows.py, 3-way Pool, ~3.5‚Äì4 min each): flat slot-filling m=22 N=480 ‚Üí G_worst1 6.8201 dB / pp 1.0962 dB / '0'-floor ‚àí5.53 dB (memo: 6.82/1.10/‚àí5.5 class ‚Äî exact); duty-0.8 m=28 N=480 ‚Üí 7.4932 dB (memo 7.49); duty-0.8 m=30 N=480 ‚Üí 7.7294 dB (memo 7.73).; Knee-interpolation snippet against the session's raw results2.jsonl: confG-3 0.0430, confG-12 0.0163, flat m=22 0.0175, duty-0.8 m=30 0.0132, flat m=44 0.0111 ‚Äî all five ¬ß5 digits exact.; Energy-integral snippet: E/E0 = 3.43/4.16/4.53/4.88 per '1' at duty-0.8 m=22/26/28/30, time-averaged power √ó1.25‚Äì1.30 (memo √ó3.4‚Äì4.9 and √ó1.25‚Äì1.30 ‚Äî match).; Audited all three session logs (results.jsonl, results2.jsonl, results_duty.jsonl) against every ¬ß3 slot-sweep row, every ¬ß4 ladder rung (incl. pp 0.74‚Üí1.10‚Üí1.24 and floors ‚àí5.15/‚àí10.17/‚àí11.61/‚àí12.83), the edge-sweep 1.7 dB and amp-doubling ‚â§0.4 dB claims, and the Richardson arithmetic (3¬∑G720‚àí2¬∑G480) ‚Äî all match.; Source-read of released solver.py: phase = (t % period) at line 109 and no ncyc in run()'s signature ‚Äî the ¬ß1 premises stand; noise_margin_frac 0.25641458774368575 (‚àí11.8 dB) confirmed in results.json; key-collision grep over both chains' results.json and all notes/*.md: zero hits for the ¬ß6 pre-registered names; 07-23's E4 ping-pong and F=1 razor rows verified verbatim against the promoted note.
- üåä **Kinetic** ‚Äî **STORE**: Everywhere I ran the published listings myself, the memo reproduced exactly: the full G_req ledger and every ¬ß1 anchor to the digit, driver bit-identity of 0.0 over 250,167 steps, the 07-25 probe rows (eye/G_worst1 to the digit), all five ¬ß5 knee digits from the raw sweep, and the ¬ß0.5 energy multipliers; the published listings are byte-identical (modulo a trailing newline) to the session's actually-run sources, and my audit of the raw jsonl logs matches every ¬ß3/¬ß4 table entry, the Richardson arithmetic (7.22/8.05/8.33), and the +0.03/+0.28 dB clearances. The result is substantive and corrective ‚Äî a demonstrated two-way failure of the published 80 [71,91] GHz band's centre and upper half (pp 1.24 dB and floor ‚àí5.2 dB at matched grid) plus a constructive, pre-registered gated operating point at 67‚Äì71 GHz ‚Äî exactly the kind of honest negative the record standard prizes. Epistemic labels are consistently applied (Richardson extrapolants in-model and never load-bearing; the knee-corner assignment's open residual stated as cutting both ways), thin margins and spec/phase sensitivities are priced against the memo's own conclusions, and the gradings of 07-23/07-25 check against the notes' actual text (E4 left open, `f_max_F2_burst12_GHz` correctly quoted and superseded only for physical drives, noise_margin_frac ‚àí11.8 dB confirmed). It is durable: it resets what Part III may claim and specifies bench gate G1's load-bearing waveform, with one concrete adoptable check. The issues I found are reproducibility warts, not correctness failures.
  - validate.py as published prints the gain-spread pp statistic (3.64/0.91/0.26 at m=8/16/22), while the memo ¬ß2(b) 'to the digit' pp targets (4.91/1.03/0.27) are the raw '1'-level-spread convention computed in experiments.py ‚Äî the raw convention does check against the logs (wrapG m=22 pp_raw 0.274, m=16 1.025), but a naive re-runner of validate.py alone will see the pp column apparently fail; a one-line note in ¬ß8 would fix this.
  - The m=28 rung's +0.03 dB clearance over G_req = 7.649 is inside any convention error (carrier-phase reading alone moves it to +0.05); the memo prices this honestly in ¬ß7.1 and rests the window on m=30's +0.28 dB, but the 71 GHz edge of the headline window is genuinely fragile and additionally conditional on the round ‚â• 10 dB floor spec rather than the noise-margin-anchored 11.8 dB variant.
  - My independent solver rerun of the three flagship N=480 rows (flat m=22 expecting 6.82/1.10/‚àí5.5; duty-0.8 m=28/30 expecting 7.49/7.73) was still executing at the assessment deadline; for those specific rows my verification rests on my own runs of the validation tier plus raw-log audit and independent recomputation of the derived arithmetic, not on a completed independent run of the flagship rows themselves.
  - *Re-executed:* anchors.py (my workspace, extracted verbatim from the published listings comment): every ¬ß1 anchor bit-for-bit vs results.json (M_th 0.14708333333333332, cw gain 9.66100611708918, NF 2.768939660565078, per-gate loss 2.555099201864131, a_loss 0.7451522890452021, loop 0.9162026217341978, pulse_net 6.258296289342312, rt 0.5 ps, f0_n 0.25); G_req ledger exactly 7.649/7.056/6.515 dB (F=2) and 5.536/4.526/3.505 dB (F=1); composed CW F=2 reserve +2.012 dB; Gtrans(8)=4.568, Gtrans(24)=8.534.; validate.py: bit-identity max|cav_released ‚àí cav_custom| = 0.0 over 250,167 steps; probe rows m=8 eye ‚àí1.46 / G_worst1 +3.05, m=16 eye +7.61, m=22 eye +12.51 / G_worst1 +4.17 ‚Äî all to the digit (pp column printed in the listing's gain-spread convention, 3.64/0.91/0.26; the raw-spread convention values 4.91-class/1.03/0.27 confirmed from the session logs).; knee_snippet.py against results2.jsonl: knees 0.0430 (confG-3), 0.0163 (confG-12), 0.0175 (flat m=22), 0.0132 (duty-0.8 m=30), 0.0111 (flat m=44) ‚Äî all five ¬ß5 digits exact.; energy_snippet.py: E/E0 = 3.43/4.16/4.53/4.88 per '1' (duty-0.8, m=22/26/28/30) and time-averaged power √ó1.25‚Äì1.30; duty-0.65 m=30 √ó3.86/√ó1.03 ‚Äî matches ¬ß0.5's √ó3.4‚Äì4.9 and √ó1.25‚Äì1.30.; Derived arithmetic recomputed independently: Richardson 3¬∑G720‚àí2¬∑G480 gives 7.22 (flat m=22), 8.05 (duty m=28), 8.33 (duty m=30); clearances 7.677‚àí7.649=+0.028 and 7.930‚àí7.649=+0.281; slot‚Üífrequency map 22/28/30 rt ‚Üí 90.9/71.4/66.7 GHz; 20¬∑log10(0.25641...) = ‚àí11.82 dB.; Raw-log audit (session jsonl files, not my run): flat m=22 ladder 6.428/6.820/6.955 with pp 0.74/1.10/1.24 and floors ‚àí6.63/‚àí5.53/‚àí5.15; duty-0.8 m=28: 7.493/7.677 floor ‚àí11.6; m=30: 7.729/7.930 floor ‚àí12.8; wrapG baseline 4.125‚Äì4.198 dB flat over m=16‚Äì32; duty N=240 rows 6.42/6.83/7.12 and F=1 rows 4.86/5.94 ‚Äî every memo table entry matches. Published listings diff clean against the session's executed sources (trailing newline only). Key-collision grep: no collisions in either chain's results.json or any promoted note. My own N=480 rerun of flat m=22 and duty-0.8 m=28/30 (my_rows.py) was launched but had not completed by the forced deadline.
- ‚öõÔ∏è **Quanta** ‚Äî **STORE**: This is a concrete, re-executable adjudication, not a survey: it refutes the published 0.1 THz F=2 headline for physical slot-confined drives on two independently demonstrated legs (slot-filling pp 1.24 dB > the promoted 1-dB criterion, '0'-floor ‚àí5.2 dB at m=22/N=720) and replaces it with a calibrated, constructive gated operating point (duty-0.8, 67‚Äì71 GHz) ‚Äî and every load-bearing number I re-ran from the published listings reproduced to the digit, including the full G_req ledger, both decisive measured rows, and all five knee-migration digits. Epistemic labels are applied with unusual discipline: the CW-knee corner is called an assignment rather than a bound with the open residual explicitly cutting both ways, the +0.03 dB m=28 clearance is disclosed as within convention error and the verdict is not rested on it, Richardson extrapolants are labeled in-model and never load-bearing, and the floor-spec sensitivity that would shrink the window to 67 GHz is stated in the executive summary. Consistency with the corrected record is clean where I checked it: the 07-23 ledger, E4 ping-pong status, and F=1 convention-razor are characterized accurately, 07-25's probe digits and [71, 91] band are consumed as published, the solver source-reads (modulo wrap, no ncyc in run) verify, and the energy claim correctly lands outside energy_per_add_fJ per the chain README. It supersedes an in-model key with a measured physical result via proper qualification, exactly the mechanism rule 10 exists for, and it changes what WP1/WP5 and bench gate G1 should do next (the gated duty-0.8 waveform, plus one pinned-down streaming-knee check). The one defect I found ‚Äî the published validate.py prints a gain-spread pp statistic (3.64/0.91/0.26) against its own raw-'1'-spread targets (4.91/1.03/0.27) ‚Äî is real but non-load-bearing, since the experiment tables use the correct pp_raw_dB metric that does reproduce 07-25; it does not move any verdict. All five storage criteria hold.
  - Published validate.py listing does not meet the memo's own "reproduce to the digit" claim on the pp column: fs_driver.measure() prints pp_dB = max(g)‚àímin(g) (gain spread), giving 3.64/0.91/0.26 at m=8/16/22 against the listing's own printed targets 4.91/1.03/0.27, which are the raw '1'-level spread of the ¬ß2 convention. Eye and G_worst1 reproduce exactly; the experiment batteries use the correct pp_raw_dB metric (wrapG m=16/22 give 1.025/0.274, matching 07-25's 1.03/0.27), so nothing load-bearing moves ‚Äî but an independent replicator running the listings in order will hit this apparent mismatch first.
  - The demonstrated-rung window's upper edge (71 GHz, m=28) is doubly conditional ‚Äî on the round ‚â•10 dB floor spec rather than the noise_margin_frac-anchored 11.8 dB variant, and on a +0.03 dB clearance within convention error. The memo discloses both, but readers should treat 67 GHz (m=30, +0.28 dB, passes both floor specs) as the only robust rung until the ¬ß7.2 streaming-knee check pins G_req_gated.
  - Knee-migration absolute digits carry ~4% interpolation-grid uncertainty (an independent rerun read 0.0137 vs 0.0132 for the duty row) and are convention-bound; the memo correctly forbids substituting them into the ledger, and only the migration ratio should ever be quoted from this note.
  - *Re-executed:* anchors.py (my run, published listing): every results.json anchor bit-for-bit (M_th 0.14708333333333332, cw_gain 9.66100611708918, NF 2.768939660565078, per_gate_loss 2.555099201864131, pulse_streaming 7.7967069614868425); G_req ledger to the digit ‚Äî F=2: 7.649/7.056/6.515 dB, F=1: 5.536/4.526/3.505 dB; composed CW F=2 reserve +2.012 dB (07-21's +2.01); Gtrans(8)=4.568, Gtrans(24)=8.534.; Load-bearing measured row 1 (my own driver script over the published listings' functions): flat slot-filling m=22, N=480 ‚Üí G_worst1 6.820 dB / pp 1.096 dB / '0'-floor ‚àí5.53 dB ‚Äî matches the memo's ladder rung 6.82/1.10/‚àí5.5 class exactly (the 91 GHz failure row).; Load-bearing measured row 2 (same, constructive frontier): duty-0.8 m=28, N=480 ‚Üí G_worst1 7.493 dB / pp 0.122 / floor ‚àí12.28 dB ‚Äî matches the memo's 7.49 rung.; validate.py (my run): custom stepping loop bit-identical to released solver.run(drive_kind='prbs'), max|cav diff| = 0.0 over 250,167 steps; 07-25 probe rows m=8/16/22 eye ‚àí1.46/+7.61/+12.51 and G_worst1 +3.05/+4.13/+4.17 to the digit (pp column prints 3.64/0.91/0.26 ‚Äî the statistic mismatch flagged in top_issues).; Knee-interpolation snippet (my run) against the session's results2.jsonl: confG-3 0.0430, confG-12 0.0163, flat m=22 0.0175, duty-0.8 m=30 0.0132, flat m=44 0.0111 ‚Äî all five ¬ß5 digits exact; migration ratios √ó0.41‚Äì0.26 = the claimed √ó2.5‚Äì3.9.; Energy-integral snippet (my run): E/E0 = 3.43/4.16/4.53/4.88 and power √ó1.25‚Äì1.30 for duty-0.8 at m=22/26/28/30 ‚Äî matches ¬ß0.5's √ó3.4‚Äì4.9 and √ó1.25‚Äì1.30.; Audits: published listings diffed against the session's executed files (identical except one trailing blank line); raw results.jsonl/results2.jsonl/results_duty.jsonl audited against every ¬ß3/¬ß4 table row I checked including the wrapG baseline (4.13‚Äì4.20 dB flat, m=16‚Äì32) and duty 0.5/0.65 F=1 rows (4.86/5.94 dB, floors ‚àí18.6/‚àí15.3); solver.py source-read confirms phase=(t % period) at line 109 and no ncyc in run's signature; 07-23 E4 row and F=1 margins, 07-25 probe digits/band/criterion, and chain README's energy_per_add_fJ launch-exclusion all verified in the repo.
