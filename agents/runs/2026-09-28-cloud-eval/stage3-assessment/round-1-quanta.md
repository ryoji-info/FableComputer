### ⚛️ Quanta — **STORE** (required edits) — round 1, 2026-09-28

VOTE: store

REASONS: Every decisive row I re-executed reproduces the printed digits. I wrote my own instrument from the reply's stated definitions (Linux x86_64 / Python 3.11.15 / numpy 2.4.6, released fable-model-chain/ unedited) and did not open cascade_driver.py. The gate reproduces to ≤1.3×10⁻¹³ relative. The m = 30 / J = −1 chain reproduces (13.103 dB, G4_A 1.581, c2c 4.798, stage-2 floors −4.70 / −4.31 / −6.26), and so do the matched-amplitude Δ (+0.001 / +0.101), the passive transfer (15.83 dB), the J = −25 row (G4 1.958) and the residue (−5.70 / −1.57). A gated-input ablation that nobody had run confirms the reply's floor mechanism: removing cell 1's ring-down after the end of its drive from cell 2's input restores the stage-2 floor from −4.70 to −14.11 dB. The substance is new, checkable and durable. It is the record's first two-cell time-domain cascade, and it grades 08-01 §4 at matched amplitude.

Four claims above the measurements are oversold or conflict with the corrected record:
- **Window placement.** "The floor fails every spec under every placement" is false. A stage-2 window at lo = 0.77 slot reads −10.87 dB (peak) and −13.16 dB (slot-mode) at m = 30 / J = −1, and −11.48 dB at J = −25. At m = 28, lo = 0.80 gives −10.08 dB, together with G4_A = 1.731, which is at or above the 1.7× bar.
- **Coupling mislabelled as released.** The G4 and cascadability contradictions belong to this session's in-model coupling: an unloaded AC-open drain read non-invasively, with the junction classes applied as isolating-buffer gains. They are not properties of a "released coupling". The reply's own item 8 shows that the plane choice alone flips the gain verdict.
- **Plane conflation (08-02).** The residue key's claimed comparability with `max0_below_mean1_dB` repeats the plane conflation that 08-02 corrected.
- **Falsifiers and discriminant.** The solver-side falsifier is vacuous on a deterministic chain, and the bench discriminant does not pin the decision window, although the model's own stage-2 floor spans −3.6 to −10.9 dB across placements.

I vote store WITH required edits, so this is not a clean pass. The measured core survives. The required edits are scoping and labelling, plus a statement of the window dependence I measured, which the rework may adopt with credit.

REQUIRED EDITS:
- WINDOW UNIVERSAL WITHDRAWN (item 7, item 4, headline, grading rows for f_max_F2_gated_GHz, G4 and Part I's cascadability row). Delete "No verdict above depends on the rule: the floor fails every spec under every placement". Scope the stage-2 floor verdict to the pre-fixed passive-lag rule and the two alternatives actually tested (unshifted and active-lag). Report the measured placement dependence (all N = 240, seed 7, window [lo, lo+0.47]·repT, fully windowed slots only):
- Stage 2, m = 30, J = −1: floor −3.56 (lo 0.25), −4.70 (the rule), −8.35 (0.60), −10.08 (0.70) and −10.87 (0.77) dB peak `cav`. At lo = 0.77, drn_h is −10.90 and slot-mode −13.16.
- Stage 2, m = 30, J = −25: −11.48 dB at lo = 0.80.
- Stage 2, m = 28, J = −1: −10.08 dB peak (slot-mode −12.19) at lo = 0.80.
- Cell 1 alone: its floor moves from the promoted −11.83 to −20.14 dB at lo = 0.58 (m = 30), and from −10.73 to −19.14 at lo = 0.60 (m = 28).
State what survives: under the pre-fixed rule the floor fails both specs. Under a per-stage eye-optimal sampling phase, the floor degrades by ≈ 9 dB from stage 1 to stage 2 and lands at the round spec: it passes at m = 30, sits on a knife-edge at m = 28 in peak, and passes both readings in slot-mode. In the grading row for f_max_F2_gated_GHz, qualify "even a −25 dB link … does not return the floor" the same way.
- G4 WINDOW RANGE. State that G4_A at J = −1 is window-robust only up to a stage-2 delay of about 0.5 slot. It is 1.58–1.63 for lo ≤ 0.77 at m = 30, then rises to 1.86 at lo = 0.85 (m = 30) and 1.731 / 1.873 at lo = 0.80 / 0.85 (m = 28). Stop saying the ≥ 1.7× bar is "failed at every grid" without naming the window rule.
- COUPLING RELABELLED AS IN-MODEL, not released. The released chain contains no inter-cell coupling. Replace "the released coupling", "the released density coupling", "the released model's own physics" and "the released cell is a compressed repeater with no floor" (in the headline, items 5 and 6, the grading table, the bench discriminant and the sign-off) with "this session's in-model coupling". Define that coupling as: drain-plane density, unidirectional, ideal isolation; that is, an unloaded AC-open drain read non-invasively, with Part I's passive-junction transmissions applied as isolating-buffer amplitude gains. Carry this premise into the labels of executive items 1, 2, 5 and 6, and into the G4 and cascadability grades ("contradicted under the in-model density coupling"). In the G4 grading row, report the velocity-plane alternative by the reply's own decomposition: c2c 7.55 dB ⇒ G4 ≈ 1 + 7.55/8.29 ≈ 1.91. State in Limitation 1 that the +16 dB passive transfer is the unloaded resonant buildup. A passive junction that transmits 10^(J/10) of the incident power cannot leave the drain reflection at unity, so that premise carries every G4 and c2c number.
- PLANE MISLABEL IN THE RESIDUE KEY (standing rule 10; 08-02 §3.1–3.2). `zero_slot_residue_unwindowed_dB` is a drain-plane density ratio, and its denominator is the drain-density mean-'1' windowed peak. It is not "the promoted floor key's own denominator". The comparison figures "(−11.8 / −11.2)" are 08-02's `drn_h` column (−11.78 / −11.15). The promoted `max0_below_mean1_dB` is the source-plane velocity ratio (−11.83 / −10.73), which I measured and reproduced as −11.8283 / −10.7312. Restate the comparability against the drain-density floor, and fix item 4's matching sentence ("the promoted floor keys … reads −11.8 dB").
- NON-VACUOUS FALSIFIERS. Per the 08-12 §5 precedent, a same-convention rerun of a deterministic chain cannot fire. Replace "a same-convention rerun of the listings landing outside the band at any measured cell" with a named unmeasured cell per solver-side key that the band must contain. Examples: N = 720 at J = −1 for `cascade2_G4_worst1_ratio_J1` and `cascade2_zero_floor_J1_dB`, the m = 26 rung or a fourth PRBS seed for `passive_port_density_transfer_dB` and `cascade_relaunch_junction_dB`, and N = 480 at J ≤ −20 for `cascade2_G4_smallsignal_limit`. Otherwise relabel the clause as a reproduction check and not a falsifier.
- BENCH DISCRIMINANT WINDOW PINNED. Pin the stage-2 decision-window placement relative to the stage-1 window in the two-sided discriminant. The model's own stage-2 floor spans −3.6 to −10.9 dB (m = 30, J = −1) across placements, and its G4_A spans 1.54–1.86. Without a pinned placement, "a stage-2 floor deeper than −8 dB discriminates against the residue mechanism" and "G4 above 1.7×" are not discriminants.
- LATENCY ATTRIBUTION (item 7) AND 08-13. "One source-to-drain transit … plus the LF half-step" does not account for the measured 0.523–0.525 rt. At N = 240 the passive half-step is dt/2 = 6.9×10⁻⁴ time units = 3.5×10⁻⁴ rt. The ghost-centre clamp offset that 08-13 priced adds dx per transit, 2.1×10⁻³ rt. Both are an order of magnitude or more below the 0.023–0.025 rt excess. Drop the attribution or mark the excess open. Engage notes/2026-08-13-walk-excess-clamp-placement.md, which the winning prompt's constraint 2 required to be kept in view and which the reply never cites.

TOP ISSUES:
- REFUTED UNIVERSAL: item 7 says "No verdict above depends on the rule: the floor fails every spec under every placement." My measurements (m = 30, N = 240, seed 7; stage-2 window [lo, lo+0.47]·repT; peak `cav` floor; 35 fully windowed slots):
- J = −1: lo 0.70 → −10.080, 0.75 → −10.365, 0.77 → −10.865 dB (drn_h −10.90, slot-mode −13.16).
- J = −25: lo 0.80 → −11.475 dB.
- m = 28, J = −1: lo 0.80 → −10.079 dB (slot-mode −12.19).
All pass the round ≥ 10 dB spec, and every slot-mode reading passes the strict 11.82 dB spec. The reply tested three placements (Table 3b), not every placement. The headline "the gated '0'-floor does not survive a second cell" holds under its pre-fixed rule, not as a property of the cascade.
- The promoted window is not floor-optimal even for the single cell. Cell 1's own floor is −11.828 dB at the promoted [0.25, 0.72] and −20.140 dB at [0.58, 1.05] (m = 30), and −10.731 → −19.139 dB (m = 28). The '1'-slot `cav` peak sits at slot fraction 0.721 for cell 1 (exactly the window's edge) and at 0.808 for stage 2 at J = −1. So the stage-1→2 floor comparison is set by where each stage's window sits relative to its own ring-up. At matched eye-optimal placements the degradation is ≈ 9 dB (−20.1 → −10.9), still a large effect. The qualitative finding survives; the pass/fail verdict does not.
- G4 bar verdict also window-conditional at large delays. For m = 30, J = −1, G4_A worst is 1.537 (lo 0.25), 1.581 (the rule), 1.582 (0.40–0.70), 1.630 (0.77), 1.862 (0.85). For m = 28, J = −1, it is 1.589 (the rule), 1.731 (0.80) and 1.873 (0.85). Up to a ≈ 0.5-slot delay the verdict is robust, which strengthens the reply's G4 result within that range.
- MISLABEL: the coupling is presented as "the released coupling" and "the released model's own physics" (headline, item 5, grading table, bench discriminant, sign-off). The released chain has no inter-cell coupling. The construct reads an unloaded AC-open drain non-invasively and applies Part I's passive-junction transmissions as buffer gains. The +15.83 dB passive transfer (reproduced: passive mean-'1' drn_h 0.012374008905000889) is the unloaded resonant buildup; the released loop model gives 2/(1 − a_loss) = +17.89 dB. In-model illustration (my arithmetic with released regen.loop_gain; a lossless junction at J = −1 leaves drain reflection |r| = 0.454): loaded loop 0.416, CW gain 9.66 → 1.08 dB, passive drain buildup 17.89 → 6.83 dB. That premise carries the whole G4 verdict, and the reply's item 8 already shows the plane choice flips the gain verdict (velocity plane: c2c 7.55 dB ⇒ G4 ≈ 1.91 by its own decomposition). Limitation 1 names the loaded drain as open but not its stake, and the executive labels omit it.
- STANDING RULE 10 / 08-02 PLANE CONFLATION: the residue key claims "the promoted floor key's own denominator, so the key is directly comparable with `max0_below_mean1_dB` (−11.8 / −11.2)". Measured: m = 28 cell 1 gives `cav` (the promoted key) −10.7312 against `drn_h` −11.1506. The −11.2 is the drain-density floor, and the key itself is drain density. 08-02 §3.1 established that the promoted key is a source-plane velocity ratio. The two coincide at m = 30 only because 08-02's paired Δ there is +0.055 dB.
- VACUOUS FALSIFIERS: "a same-convention rerun of the listings landing outside the band at any measured cell" cannot fire on a deterministic chain. My reruns reproduce to ≤ 1.3×10⁻¹³ relative, and cross-seat reruns match the printed digits. 08-12 §5 registers a non-vacuous bench falsifier for exactly this reason. Keys such as `passive_port_density_transfer_dB`, `cascade_relaunch_junction_dB`, `zero_slot_residue_unwindowed_dB` and `cascade2_G4_smallsignal_limit` carry no other falsifier.
- BENCH DISCRIMINANT UNPINNED: the reply's discriminant predicts stage-2 floor [−6, −3] dB and G4 [1.40, 1.65], and says a floor deeper than −8 dB discriminates against the residue mechanism. The model itself gives −8.35 to −10.87 dB (lo 0.60–0.77, m = 30, J = −1) and G4 up to 1.86 (m = 30, lo 0.85) or 1.73 (m = 28, lo 0.80), depending only on where the bench samples stage 2.
- CONFIRMED BY ABLATION (mechanism no one had tested): cell 2 was driven by cell 1's output under three gates (m = 30, J = −1, rule window 2.625 rt; peak `cav` / drn_h / slot-mode floors):
- no gate: −4.696 / −4.307 / −6.257;
- gate zeroing the '0'-slot residue (1-rt raised-cosine cut at the '0'-slot start): −9.380 / −8.822 / −12.978;
- duty-0.8 gate removing everything after 0.8·repT: −14.107 / −13.582 / −17.785.
The ring-down that the promoted window excludes is the mechanism under the rule, as item 4 says. Refinement: about half the degradation (−4.70 → −9.38) comes from the '0'-slot residue that the registered key isolates, and the other half (−9.38 → −14.11) from the '1' slot's own post-drive tail in [0.8, 1.0]·repT. The key therefore captures only part of the mechanism (optional to state).
- LATENCY ATTRIBUTION: item 7 explains 0.523–0.525 rt as "L/s = 0.5 rt plus the LF half-step". Arithmetic: dt(passive, N = 240) = 0.4/240/1.2 = 1.389×10⁻³, so the half-step is 3.5×10⁻⁴ rt. The ghost-centre clamp placement (08-13) adds dx/2 per clamp, i.e. 2.1×10⁻³ rt per transit. Neither explains the 0.023–0.025 rt excess. The reply never cites 08-13, which the prompt's constraint 2 named.
- Minor, disclosed, not blocking: the ⅛-rt rounding of the window rule is estimator-sensitive. My moving-mean cross-correlation gives 2.550 rt for the passive stage-1→2 lag (reply 2.568; check seat 2.540), which rounds to 2.5 rt, not 2.625. At the exact 2.568-rt shift the matched Δ at m = 30 / J = −1 is −0.094 / +0.039 rather than +0.001 / +0.101. Limitation 6 already states ≈ 0.1 dB, so this is noted for completeness only. My active lag is 5.726 rt (reply 5.704).

SEAT MODEL NOTE: This seat (assess-quanta, Quanta persona) was requested on claude-opus-5-5 by the maintainer for this run, in the 2026-08-13 policy's Opus assessor seat. It is not Fable 5 and does not claim to be. The reply under assessment was executed on claude-fable-5-1, and its two pre-publication check seats ran on the Fable alias. Every number in this verdict was executed by this seat on Linux x86_64 / Python 3.11.15 / numpy 2.4.6 against the released, unedited fable-model-chain/. Reproductions are gated on relative deviation (≤ 1.3×10⁻¹³ on the gate row), not exact equality. Blind to the other two assessor seats. — Quanta ⚛️ (AI research agent · see agents/README.md)

<details><summary>Re-execution log (verbatim)</summary>

```text
Seat directory /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/assess-quanta/.
- Instrument: q_inst.py, written from the reply's stated coupling definition and the promoted 07-31 §8 exp_duty.make_sig_duty launch. The session's cascade_driver.py was not opened.
- Coupling: cell 2's clamp h_left = 1 + κ·(h1[−1] − 1), κ = 10^(J/20). It is read causally on the upstream cell's true-time series, which gives exact previous-state lockstep when the two dt agree and linear interpolation otherwise.
- Stepping: released solver._setup/_step_LF, with released solver.run stepping replicated (t += dt, pre-step label).
- Everything ran with PYTHONDONTWRITEBYTECODE=1. `git status --porcelain` was empty (0 lines) before and after.
- Platform: `python3 -c "import sys,numpy,platform;..."` printed "3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0] 2.4.6 x86_64 Linux"; nproc 4.

$ PYTHONDONTWRITEBYTECODE=1 python3 phase1.py   (released run_all.measure_Mth_num; then cell 1 active/passive, m=30, N=240, seed 7, duty 0.8, drive 2e-3, 40*m round trips)
M_th_num(240) = np.float64(0.16894319463373797)  shipped 0.16894319463373791  rel dev 3.285787944971905e-16 [42s]
bias = np.float64(0.11826023624361658)
done ('P1_m30', 1728000, 0.001388888888888889, 56.3)
done ('A1_m30', 1898294, np.float64(0.0012642926038760258), 63.3)
total 105s

$ python3 score1.py
GATE cav: {'G_worst': '8.287855791924049', 'G_mean': '8.410165254217045', 'mean1': '0.03267155023359718', 'floor': '-11.828336851446547', 'eye': '11.705114659586407', 'pp': '0.30577762777571854'}
GATE drn_h: {'G_worst': '8.663537342727865', 'G_mean': '8.769558457037114', 'mean1': '0.03396500068703142', 'floor': '-11.775002445228234', 'eye': '11.668429556367615', 'pp': '0.2653510968361314'}
rel dev G 3.857984973672145e-15  floor cav 5.676731172997833e-14  floor drn_h 1.3230272820754644e-13
cell-1 slot-mode drn_h floor -15.6648766590724  peak-mode gap 3.889874213844166
passive mean-1 drn_h 0.012374008905000889  transfer dB 15.8296085712346
active mean-1 drn_h 0.03396500068703142  over launch dB 24.600032640950246  relaunch junction dB -24.600032640950246
n after-1 zeros 8  after-0 zeros 8
mean1 windowed 0.03396500068703142  mean1 first-quarter 0.02112298068773024
residue after-1: window -11.775  first-quarter/(a) -5.6981  first-quarter/(b) -1.5726  whole/(a) -5.6981 ; after-0 first-quarter/(a) -30.07
 after-1 zero slot 7 max at slot fraction 0.0090
 after-1 zero slot 13 max at slot fraction 0.0090
 after-1 zero slot 16 max at slot fraction 0.0084
'1' slot drain-density peak position (slot fraction): median 0.704 min 0.703 max 0.704
[Gate PASSED against 8.287855791924017 / -11.828336851447219 / -11.775002445226676, rel dev <= 1.3e-13; not bit-equal.]

$ PYTHONDONTWRITEBYTECODE=1 python3 phase2.py   (J=-1 chains MM/M0/00; ablations MM_J1_gslot, MM_J1_gduty; boundary-driven matched active/passive at A*; J=-25 chains)
A* (J=-1) = 0.030271338726030064
done ('M0_J1', 1728000, 62.6) [63s]
done ('00_J1', 1728000, 64.1) [64s]
done ('MM_J1_gslot', 1898294, 70.2) [70s]
done ('MM_J1', 1898294, 71.1) [71s]
done ('MM_J1_gduty', 1898294, 62.1) [125s]
done ('BP_J1', 1728000, 56.6) [127s]
done ('BA_J1', 1898294, 64.1) [128s]
done ('MM_J25', 1898294, 61.2) [132s]
done ('M0_J25', 1728000, 51.3) [176s]
done ('00_J25', 1728000, 50.4) [177s]

$ python3 score2.py
J=-1 [unshifted] chain worst 12.7344 mean 13.1388 | G4_A worst 1.5365 mean 1.5622 | G4_A(drn_h) 1.4862 | G4_B 1.7882 | c2c 4.6488/5.0025 | upstream-thru-passive 8.0616/8.1363 | floor peak cav -3.562 drn_h -3.087 slot-mode -4.099 | pp 0.997 eye 3.148 | mean1 drn density 0.3166
J=-1 [exact 2.568rt] chain worst 12.9998 mean 13.3371 | G4_A worst 1.5685 mean 1.5858 | G4_A(drn_h) 1.5498 | G4_B 1.8039 | c2c 4.7038/4.9685 | upstream-thru-passive 8.2696/8.3686 | floor peak cav -4.637 drn_h -4.307 slot-mode -6.214 | pp 0.853 eye 4.292 | mean1 drn density 0.3310
J=-1 [rounded 2.625rt] chain worst 13.1028 mean 13.3987 | G4_A worst 1.5810 mean 1.5932 | G4_A(drn_h) 1.5498 | G4_B 1.8039 | c2c 4.7981/5.0301 | upstream-thru-passive 8.2696/8.3686 | floor peak cav -4.696 drn_h -4.307 slot-mode -6.257 | pp 0.750 eye 4.395 | mean1 drn density 0.3310
J=-1 passive stage-2 transfer (shift 0.000 rt) = 15.815 dB (00 mean-1 drn_h 0.06812)
J=-1 passive stage-2 transfer (shift 2.625 rt) = 15.815 dB (00 mean-1 drn_h 0.06812)
J=-1 input amplitude to cell 2 = 0.03027
J=-25 [unshifted] chain worst 15.6994 mean 15.8407 | G4_A worst 1.8943 mean 1.8835 | G4_A(drn_h) 1.8370 | G4_B 0.9254 | c2c 7.3141/7.4705 | upstream-thru-passive 8.2972/8.3702 | floor peak cav -1.939 drn_h -1.913 slot-mode -2.996 | pp 0.354 eye 1.800 | mean1 drn density 0.0275
J=-25 [exact 2.568rt] chain worst 16.0726 mean 16.4117 | G4_A worst 1.9393 mean 1.9514 | G4_A(drn_h) 1.9169 | G4_B 0.9523 | c2c 7.5993/7.8449 | upstream-thru-passive 8.4733/8.5668 | floor peak cav -3.630 drn_h -4.010 slot-mode -5.227 | pp 0.832 eye 3.286 | mean1 drn density 0.0297
J=-25 [rounded 2.625rt] chain worst 16.2302 mean 16.5022 | G4_A worst 1.9583 mean 1.9622 | G4_A(drn_h) 1.9169 | G4_B 0.9523 | c2c 7.7569/7.9354 | upstream-thru-passive 8.4733/8.5668 | floor peak cav -3.717 drn_h -4.010 slot-mode -5.273 | pp 0.676 eye 3.443 | mean1 drn density 0.0297
J=-25 passive stage-2 transfer (shift 0.000 rt) = 15.737 dB (00 mean-1 drn_h 0.00426)
J=-25 passive stage-2 transfer (shift 2.625 rt) = 15.737 dB (00 mean-1 drn_h 0.00426)
J=-25 input amplitude to cell 2 = 0.00191
MATCHED A*=0.030271 boundary-driven cav: G worst 4.7973 mean 4.9294 floor -13.083 pp 0.337
Delta (c2c - matched) worst/mean: 2.625rt +0.0008/+0.1007; 2.568rt -0.0935/+0.0391; unshifted -0.1485/+0.0731
[All of the following match the reply's printed digits:
- Table 1: m30/N240/J-1 13.103 / 1.581 / 1.593 / 1.550 / 1.804, and unshifted 12.734.
- Table 2a: 4.798/5.030 vs 4.797/4.929, Δ +0.001/+0.101.
- Table 5: -4.70/-4.31/-6.26, 0.750, +4.39.
- Table 3 stage 2: 13.000/13.337, 4.704/4.969, -4.64/-4.31/-6.21, 0.853, +4.29, 0.3310.
- Table 4/5 at J = -25: 7.757/7.935, 1.958/1.962, -3.72/-4.01/-5.27, 0.676, +3.44.
- Table 6: 15.83/15.82.
- Relaunch: -24.60.
- Residue: -5.70 / -1.57 / -30.1.]

$ python3 score3.py   (ablation + window-placement scan; scan on a 50x-decimated series, best point re-scored at full resolution)
=== ABLATION (J = -1, stage-2 active chain output, floor = max'0'/mean'1') ===
MM_J1        shift 0.000 rt: floor peak cav -3.562 | peak drn_h -3.087 | slot-mode -4.099 | eye cav +3.148 | mean1 cav 0.30762
MM_J1        shift 2.625 rt: floor peak cav -4.696 | peak drn_h -4.307 | slot-mode -6.257 | eye cav +4.395 | mean1 cav 0.31860
MM_J1_gslot  shift 0.000 rt: floor peak cav -6.864 | peak drn_h -6.717 | slot-mode -10.130 | eye cav +6.452 | mean1 cav 0.30755
MM_J1_gslot  shift 2.625 rt: floor peak cav -9.380 | peak drn_h -8.822 | slot-mode -12.978 | eye cav +9.083 | mean1 cav 0.31844
MM_J1_gduty  shift 0.000 rt: floor peak cav -11.608 | peak drn_h -11.703 | slot-mode -14.899 | eye cav +11.313 | mean1 cav 0.31295
MM_J1_gduty  shift 2.625 rt: floor peak cav -14.107 | peak drn_h -13.582 | slot-mode -17.785 | eye cav +13.839 | mean1 cav 0.31980
=== WINDOW-PLACEMENT SCAN (promoted width 0.47 repT; window [lo, lo+0.47] slot, lo scanned 0..1 slot) ===
MM_J1       : best (deepest) cav floor at lo = 0.77 slot -> -10.888 dB (eye +10.614); drn_h peak -10.900; slot-mode -13.160 | floor at lo=0.25 -3.56, lo=0.3375 -4.69
              narrow 0.2-slot window: best lo 0.97 -> floor -13.24 dB (downsampled scan)
MM_J25      : best (deepest) cav floor at lo = 0.80 slot -> -11.489 dB (eye +11.212); drn_h peak -11.240; slot-mode -14.185 | floor at lo=0.25 -1.95, lo=0.3375 -3.69
              narrow 0.2-slot window: best lo 1.00 -> floor -14.56 dB (downsampled scan)
MM_J1_gslot : best (deepest) cav floor at lo = 0.68 slot -> -17.702 dB (eye +17.409); drn_h peak -17.277; slot-mode -21.907 | floor at lo=0.25 -6.86, lo=0.3375 -9.37
              narrow 0.2-slot window: best lo 0.91 -> floor -22.95 dB (downsampled scan)
MM_J1_gduty : best (deepest) cav floor at lo = 0.64 slot -> -21.643 dB (eye +21.375); drn_h peak -21.214; slot-mode -23.577 | floor at lo=0.25 -11.61, lo=0.3375 -14.11
              narrow 0.2-slot window: best lo 0.88 -> floor -24.70 dB (downsampled scan)
A1_m30      : best (deepest) cav floor at lo = 0.58 slot -> -20.148 dB (eye +20.041); drn_h peak -19.741; slot-mode -22.801 | floor at lo=0.25 -11.78, lo=0.3375 -14.30
              narrow 0.2-slot window: best lo 0.82 -> floor -24.63 dB (downsampled scan)

$ python3 score4.py   (full-resolution scan; slots whose window runs past the record end are dropped)
bits: 1111111000011001010010001010011111111101
stage-2 (J=-1) window [lo, lo+0.47] slot: lo | floor peak cav | eye | G_chain worst (MM/00) | G4_A worst (stage-1 at promoted window, 8.2879) | slots scored
  0.2500 |  -3.562 |  +3.148 |  12.734 | 1.5365 | 36
  0.3375 |  -4.696 |  +4.395 |  13.103 | 1.5810 | 36
  0.4000 |  -5.565 |  +5.268 |  13.110 | 1.5819 | 36
  0.4500 |  -6.329 |  +6.032 |  13.110 | 1.5819 | 36
  0.5000 |  -7.220 |  +6.923 |  13.110 | 1.5819 | 36
  0.5500 |  -7.377 |  +7.105 |  13.110 | 1.5819 | 35
  0.6000 |  -8.348 |  +8.075 |  13.110 | 1.5819 | 35
  0.6500 |  -9.084 |  +8.811 |  13.110 | 1.5819 | 35
  0.7000 | -10.080 |  +9.807 |  13.110 | 1.5819 | 35
  0.7500 | -10.365 | +10.115 |  13.390 | 1.6156 | 35
  0.7700 | -10.865 | +10.614 |  13.509 | 1.6299 | 35
  0.8000 |  -8.590 |  +8.340 |  13.539 | 1.6336 | 35
  0.8500 |  -7.007 |  +6.814 |  15.433 | 1.8621 | 35
  0.9000 |  -4.147 |  +4.000 |  14.137 | 1.7057 | 35
stage-1 alone (A1 vs P1) window scan: lo | floor | eye | G worst
  0.25 | -11.828 | +11.705 |   8.288
  0.40 | -15.176 | +15.069 |   8.337
  0.50 | -17.671 | +17.565 |   8.337
  0.58 | -20.140 | +20.041 |   8.337
  0.65 | -11.535 | +11.436 |   8.337
  0.70 |  -9.012 |  +8.913 |   8.337
stage-2 (J=-25) scan: lo | floor | eye | G4_A
  0.3375 |  -3.717 |  +3.443 | 1.9583
  0.6000 |  -7.987 |  +7.723 | 1.9731
  0.7000 |  -9.721 |  +9.457 | 1.9731
  0.8000 | -11.475 | +11.212 | 2.0239
  0.8500 | -10.122 |  +9.859 | 2.2503
'1'-slot cav peak position (slot fraction) cell 1: 0.721 [0.720, 0.721]
'1'-slot cav peak position (slot fraction) stage 2 J=-1: 0.808 [0.739, 0.808]

$ PYTHONDONTWRITEBYTECODE=1 python3 phase3.py   (m = 28: cell 1 active/passive, then J=-1 MM and 00)
done ('P1_m28', 1612800, 58.4)
done ('A1_m28', 1771741, 64.6)
done ('00_J1_m28', 1612800, 57.8)
done ('MM_J1_m28', 1771741, 62.0)
total 127s

$ python3 score5.py
m=28 cell 1 gate: G worst 8.1315 (promoted 8.131549) floor cav -10.7312 (promoted -10.731215) floor drn_h -11.1506 (promoted -11.150570)
m=28 J=-1 rule window (2.500 rt): chain worst 12.917 G4_A 1.5885 floor cav -4.024 eye +3.653   [reply Table 1: 12.917 / 1.589; Table 5: -4.02 / +3.65]
m=28 J=-1 stage-2 window scan [lo, lo+0.47]: lo | floor cav | floor drn_h | slot-mode | eye | G4_A
  0.30 |  -4.004 |  -3.564 |  -4.346 |  +3.633 | 1.5885
  0.35 |  -4.026 |  -4.425 |  -5.676 |  +3.654 | 1.5885
  0.40 |  -4.928 |  -4.588 |  -6.531 |  +4.597 | 1.5999
  0.45 |  -5.703 |  -5.483 |  -7.694 |  +5.372 | 1.5999
  0.50 |  -6.381 |  -6.398 |  -8.596 |  +6.051 | 1.5999
  0.55 |  -6.712 |  -6.387 |  -9.193 |  +6.407 | 1.5999
  0.60 |  -7.466 |  -7.352 | -10.175 |  +7.161 | 1.5999
  0.65 |  -8.413 |  -8.229 | -10.641 |  +8.108 | 1.5999
  0.70 |  -8.659 |  -8.652 | -11.249 |  +8.354 | 1.5999
  0.75 |  -9.395 |  -9.382 | -11.898 |  +9.090 | 1.5999
  0.80 | -10.079 | -10.091 | -12.188 |  +9.803 | 1.7308
  0.85 |  -8.114 |  -7.036 | -12.857 |  +7.899 | 1.8731
  0.90 |  -5.174 |  -5.855 | -13.153 |  +4.959 | 1.7926
  0.95 |  -3.165 |  -3.353 | -10.536 |  +2.997 | 1.6729
m=28 cell-1 window scan: lo | floor cav
  0.25 | -10.731
  0.40 | -14.172
  0.50 | -16.669
  0.55 | -17.955
  0.60 | -19.139
  0.65 | -14.401

$ python3 lag.py   (own estimator: |drn_h| on a 0.005-unit grid, moving mean over one carrier period, cross-correlation with parabolic refinement)
passive stage 1->2 envelope lag (moving-mean |drn_h| over one carrier period, xcorr): 2.550 rt  [reply 2.568]
active  stage 1->2 envelope lag: 5.726 rt  [reply 5.704]

$ PYTHONDONTWRITEBYTECODE=1 python3 -c "...released regen._cavity / loop_gain; in-model loaded-drain illustration, |r| = sqrt(1 - 10^(J/10))..."
a_loss 0.7451522890452021 loop(0) 0.7451522890452021 loop(0.7Mth) 0.9162026217341978 cw_net_gain_dB(0.7) 9.66100611708918
unloaded passive antinode buildup 2/(1-a) dB 17.894985171199814
J=+0 dB: power transmission 1.000, lossless-junction drain reflection |r|=0.000; loaded loop(0.7Mth)=0.000; loaded CW gain 0.00 dB (unloaded 9.66); loaded passive drain buildup (1+r)/(1-a r) 0.00 dB (unloaded 17.89)
J=-1 dB: power transmission 0.794, lossless-junction drain reflection |r|=0.454; loaded loop(0.7Mth)=0.416; loaded CW gain 1.08 dB (unloaded 9.66); loaded passive drain buildup (1+r)/(1-a r) 6.83 dB (unloaded 17.89)
J=-3 dB: power transmission 0.501, lossless-junction drain reflection |r|=0.706; loaded loop(0.7Mth)=0.647; loaded CW gain 2.56 dB (unloaded 9.66); loaded passive drain buildup (1+r)/(1-a r) 11.13 dB (unloaded 17.89)
J=-6 dB: power transmission 0.251, lossless-junction drain reflection |r|=0.865; loaded loop(0.7Mth)=0.793; loaded CW gain 4.68 dB (unloaded 9.66); loaded passive drain buildup (1+r)/(1-a r) 14.41 dB (unloaded 17.89)
[In-model illustration only: released loop model with the drain reflection scaled by a lossless-junction |r|. Labelled in-model and not registered.]

Record reads:
- Part I PDF text extracted with PyMuPDF (partI.txt). §7.4 "two-cell total ~+17–19 dB over the passive chain, computed as twice the per-cell figure", Table 6 cascadability row, Table 7 G4 "≥ 1.7× … ≈ 2×", "passive twins for differential measurement", §9.4 "junction is a gate-defined density step … reflective loss of even a 2× density step is < 0.1 dB — the −1 to −3 dB budgeted per junction is therefore dominated by non-ideal effects". All confirmed verbatim.
- $ grep 08-01-gated-requirement-round-trip.md: §4 line 91 quotes the load-bearing assumption verbatim ("an upstream cell presents the same duty-0.8 waveform the drive boundary does. No multi-cell cascade was run in this session."). Confirmed.
- $ grep -rn -E "cascade2_|passive_port_density|zero_slot_residue|cascade_stage_latency|cascade_relaunch" notes/ fable-model-chain/results.json fable-model-quantum/results.json: no hits (names collision-free).
- $ grep -n -i -E "08-13|clamp placement|ghost|placement error|walk" 11-reply.md: one hit, the disclosure line only. The reply never cites notes/2026-08-13.
- 08-02 §3.1–3.2 read: `cav` = max_x|hu/h − u0| is the promoted channel (source-plane velocity); drn_h is drain density. m = 28 / N = 240 reference row: cav −10.7312, drn_h −11.1506.
- 08-12 §5 read: "falsifier (bench, non-vacuous -- a same-convention rerun of a deterministic chain cannot fire)".
- 08-13's mirrored N = 240 cfl = 0.8 falsifier: not run. The reply does not bear on it.
- Nothing inside the repository tree was modified or executed-in-place (run_all.py was only imported for measure_Mth_num). Final `git status --porcelain` printed 0 lines.
```

</details>
