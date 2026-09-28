### 🌊 Kinetic — **REJECT** (required edits) — round 1, 2026-09-28

VOTE: reject

REASONS: I wrote my own instrument from the reply's stated definitions and the promoted 07-31 launch before opening cascade_driver.py, and every decisive row reproduces on it. The gate row gives 8.287855791924049 / −11.828336851446547 / −11.775002445228234, within 1.3×10⁻¹³ relative. At J = −1 the m = 30 and m = 28 chains give G4_A 1.581 / 1.589, cell-to-cell gain 4.798 / 4.667 dB and stage-2 floors −4.70 / −4.31 / −6.26 and −4.02 / −4.31 / −5.24 dB. The matched-amplitude row gives Δ = +0.001 / +0.101 dB, the residue −5.70 / −5.31 dB and the J = −20 row G4_A 1.954. No measurement is refuted, and two results are durable and decision-changing: the '0'-floor does not transfer through a second cell, and 08-01 §4's waveform premise holds to within 0.6 dB once the input amplitude is matched. The headline and two of the five grades (Part I's cascadability row and G4's '≈ 2×', both marked 'contradicted') rest on something else. They rest on the unloaded open-drain +16 dB step-up handed to cell 2 through κ by an ideal buffer. No released code contains that construct, so it is not 'the released coupling'. It is also energy-inconsistent with the junction transmissions it applies: in the released loop model, an energy-consistent −1 dB junction delivers about +2.6 dB rather than +16.9 dB and collapses the DS loop from 0.945 to 0.429. It also contradicts Part I §9.4, the section cited to defend the plane, which describes the junction as a nearly reflectionless density step. The reply's own sweep shows G4 reaching 1.96 once the drive returns to launch scale, so the released model does not decide G4. No key or verdict states its cfl scope, although the prompt named 08-13 and 08-12 makes cfl part of the convention: at fixed N = 240 and cfl 0.2 / 0.4 / 0.8, the residue key reads −8.11 / −5.70 / −4.21 dB (outside its band on both sides), G4_A(J = −1) reads 1.774 / 1.581 / 1.485, and the stage-2 slot-mode floor reads −11.65 / −6.26 / −3.49 dB. As published, the reply fails criterion 2 (labels) and criterion 4 (nothing oversold) at its headline, so I vote reject. The rework needed is framing, scope and citation, not new physics, and I recommend it. Optional, not required: an in-model two-resonator closed form, floor2 ≈ floor1 + 20·log10(1 + ln 10^(−floor1/20)), reproduces the measured stage-2 floor to within 0.02–0.4 dB across that 5 dB cfl spread and would make item 4's generalisation quantitative.

REQUIRED EDITS:
- Headline, executive items 1, 2, 5 and 6, the grading table and the §5 bench discriminant: replace 'the released coupling', 'the released cascade', 'the released model's own physics' and 'no released coupling' with 'the session's in-model ideal-buffer density coupling (cell 1's drain kept AC-open, κ applied to its antinode density)', and state once that the released chain contains no inter-cell coupling of any kind.
- Regrade Part I's cascadability row and Table 7 G4's '≈ 2×' from 'contradicted' to 'qualified (conditional on the coupling construct)'. Under the ideal-buffer density coupling G4 is 1.45–1.79× (Table 1). With a link that returns cell 2's drive to launch scale it is 1.96× (Table 4). Which of these a physical junction realizes is open: drain loading, coupled-segment physics (#124 territory, not re-run) and the Boltzmann–Maxwell tier. Condition item 5 and the cascade_per_cell_dB row ('a swing no released coupling produces') the same way.
- §2 and limitation 1: state that the +15.8–16.4 dB passive port transfer is the unloaded (|r| = 1) open-end resonant step-up (the loop model's 2/(1 − a_loss), +17.9 dB). Applying a passive junction's |t|² = 10^(J/10) to that antinode while keeping |r| = 1 does not conserve energy. Quote Part I §9.4 in full beside the plane defence: 'the reflective loss of even a 2× density step is < 0.1 dB'. Label the scale of cell 2's drive in-model and open. The released loop model prices an energy-consistent −1 dB junction at about +2.6 dB of passive drive (not +16.9) and a DS loop of 0.429 (not 0.945).
- §2: correct 'the ideal-isolation assumption below sets that reflection to zero'. In the construct, cell 1's drain is held at total reflection (AC-open); ideal isolation removes only back-action from cell 2. Quanta's |r|² ≤ 11.6 % budget describes a nearly transmitting junction, which is the opposite of the construct.
- Add cfl scope. State in §2, in every registered key and in a new limitation that the released cfl = 0.4 is part of the convention, as 08-12's registered keys state it; cite notes/2026-08-13-walk-excess-clamp-placement.md, which the prompt's constraint 2 named and the reply never engages. Report the fixed-grid sensitivity (m = 30, N = 240, J = −1, cfl 0.2 / 0.4 / 0.8): residue −8.11 / −5.70 / −4.21 dB; G4_A 1.774 / 1.581 / 1.485; stage-2 floor peak −8.35 / −4.70 / −3.37 dB and slot-mode −11.65 / −6.26 / −3.49 dB; cell-1 floor −16.69 / −11.83 / −8.89 dB. Scope item 4's 'under either reading, at every rung, grid and seed' to the released-cfl path, since at cfl 0.2 the stage-2 slot-mode floor clears the round spec. Re-set or scope the bands of zero_slot_residue_unwindowed_dB [−7.0, −4.5] and cascade2_G4_worst1_ratio_J1 [1.40, 1.65], which cfl variation at the same grid exits.
- §5 falsifiers: the only falsifier on the solver-side keys is 'a same-convention rerun … outside the band'. On a deterministic chain such a rerun cannot fire, which 08-12's promoted key text records verbatim. Give each key a non-vacuous falsifier (a stated grid or cfl lever, an independent estimator, or a bench observable), or declare the keys reproduction bands and name the levers that move them.
- Item 8 and limitation 2: recharacterize the velocity 'plane'. At the current-clamped drain, the active cell's drain velocity is slaved to density (measured |δu|/|δh| = 0.1197 against M = 0.1183). The passive cell's drain velocity (−27.87 dB at N = 240, −34 dB at N = 480 in the reply's own figures) is an O(Δx) ghost-offset residue that falls to −∞ dB in the continuum. The '44 dB' plane spread is therefore a grid artifact, not a physical plane sensitivity. Keep the correct conclusion that the floor verdict does not depend on the plane.
- Item 7 and Table 6: withdraw 'plus the LF half-step'. At cfl 0.4 the measured excess of the passive peak lag over one transit is 0.050 time units, or 36 steps, not dt/2. It moves with cfl (0.516 / 0.525 / 0.532 rt at cfl 0.2 / 0.4 / 0.8), which makes it a scheme-borne phase error of the class 08-12 and 08-13 describe. Label it in-model or remove the attribution.
- Prior art and citations: credit notes/2026-07-22-cavity-ringdown-isi.md (ring-down is the binding inter-slot memory; a per-slot flush is necessary) where item 4 and the residue table introduce the mechanism. Where §2 rests the density plane on 08-02 §3.1, also cite 08-02's appended vote record, which grades 'the field the next cell receives is drain-plane density' as in-model at best and notes that cell.py annotates A_SAT_eff as drive-plane.
- §1: 'The slot-mode floors sit 3.84–3.89 dB below the peak floors, reproducing 08-12's measured gap' is true only of the cav peak against the drn_h slot mode, which compares two planes. The same-channel drn_h peak-to-mode gap at m = 28 is 3.46 dB (−11.15 against −14.61). Name the channels.

TOP ISSUES:
- The headline verdict rests on the coupling's scale, not on the released model. Cell 2 is driven at 0.0303 (m = 30, J = −1; measured 0.030271338726030064) only because cell 1's unloaded AC-open drain antinode (+15.8296 dB passive transfer, measured) is passed on through κ by an ideal buffer. The reply's own junction sweep gives G4_A = 1.954 at J = −20 (measured 1.954 / 1.959), so the '≈ 2×' target is reached once the drive returns to launch scale. 'The released coupling never reaches' credits the released code with a construct the session built.
- The construct is energy-inconsistent with the junction classes it applies, and it contradicts Part I §9.4. §9.4 describes the junction as a gate-defined density step whose 'reflective loss of even a 2× density step is < 0.1 dB', so the junction is nearly transmitting, while the construct keeps cell 1's drain at |r| = 1. In the released loop model (a_loss = 0.7451522890452021, loop = 0.9450 at the ratio bias), an energy-consistent −1 dB junction gives about +2.58 dB of passive drive instead of +16.89 dB, and the DS loop falls to 0.429. The reply cites §9.4 to defend the plane but omits this sentence.
- The reply inverts the reflection statement. It says the ideal-isolation assumption 'sets that reflection to zero' (Quanta's |r|² ≤ 11.6 %), but its construct holds cell 1's drain at total reflection.
- The prompt's constraint 2 (08-13 clamp placement) is not engaged, and nothing states its cfl scope. At fixed N = 240 and cfl 0.2 / 0.4 / 0.8: the residue key reads −8.11 / −5.70 / −4.21 dB against a band of [−7.0, −4.5]; G4_A(J = −1) reads 1.774 / 1.581 / 1.485 against a band of [1.40, 1.65], and at cfl 0.2 it passes Table 7's ≥ 1.7× bar; the stage-2 slot-mode floor reads −11.65 / −6.26 / −3.49 dB, clearing the round spec at cfl 0.2; the cell-1 floor reads −16.69 / −11.83 / −8.89 dB. The released-path grid ladder and the two-resonator estimate both support the fail verdict, but 'at every rung, grid and seed' is scoped to cfl = 0.4 without saying so.
- The solver-side keys' only falsifier is a same-convention rerun of a deterministic chain. 08-12's promoted key text records that such a rerun cannot fire and pairs its own keys with a non-vacuous falsifier.
- The '44 dB' plane spread is a numerical artifact. The active drain velocity is slaved to density by the current clamp (measured |δu|/|δh| = 0.1197 against M = 0.1183; |δu − (u0/(1+δh) − u0)| ≤ 2.9×10⁻⁴ against |δu| ≤ 4.2×10⁻³). The passive drain velocity, 8.085×10⁻⁵ (−27.87 dB over the launch), is an O(Δx) ghost-offset residue; the reply's own N = 480 value of −34 dB shows its first-order decay.
- The passive latency attribution 'L/s = 0.5 rt plus the LF half-step' is wrong. The measured excess is 0.050 time units (36 steps at dt = 0.00139), and the peak lag moves 0.516 / 0.525 / 0.532 rt across cfl 0.2 / 0.4 / 0.8, which marks it as scheme-borne phase error.
- Prior-art and citation gaps. 07-22-cavity-ringdown-isi, the promoted note that establishes ring-down as the binding inter-slot memory, is not cited for the floor mechanism. 08-02's appended vote record, which grades the 'next cell receives drain-plane density' identification as in-model at best, is not acknowledged where §2 rests the density plane on 08-02 §3.1.
- Minor: the '3.84–3.89 dB' peak-to-mode gap compares the cav peak with the drn_h slot mode. The same-channel drn_h gap at m = 28 measures 3.46 dB (−11.1506 against −14.6104).
- Not defects; reproduced and accepted. Gate: rel ≤ 1.3×10⁻¹³. M_th_num(240) = 0.16894319463373797 (rel 3.3×10⁻¹⁶). Passive transfer 15.8296 / 15.8117 dB (m = 30 / 28). Relaunch −24.600 / −24.336 dB. Table 1: J = −1 at m = 30 is 13.103 / 1.581 / 1.593 / 1.550 / 1.804 with unshifted 12.734; J = −1 at m = 28 is 12.917 / 1.589 / 1.615 / 1.555 / 1.815. Table 2a: m = 30 is 4.798 / 5.030 against 4.797 / 4.929 (Δ +0.001 / +0.101); m = 28 c2c is 4.667 / 4.982. Tables 4/5 at J = −20: 7.749 / 7.926, 1.954 / 1.959, −3.73 / −4.06 / −5.27, pp 0.693, eye 3.45. Residue −5.70 / −1.57 / −5.31 / −0.98 dB, argmax at 0.008–0.017 slot. Passive peak lag 0.525 rt. Window-rule rounding is within the disclosed ≈ 0.1 dB: at m = 28, 2.5 and 2.625 rt give an identical gain. The key names are collision-free across notes/, papers/ and both results.json files. Ledger terms are booked once. G4 is defined as Part I's 'over the passive chain'.

SEAT MODEL NOTE: This seat is the Kinetic assessor. The maintainer requested it on claude-opus-5-5 for this run, as the 2026-08-13 policy's Opus assessor seat. It is not Fable 5 and makes no claim about the served model beyond that request. The reply under assessment was executed on claude-fable-5-1. Every number above was executed on Linux x86_64, Python 3.11.15, numpy 2.4.6, against the released, unedited fable-model-chain/, with all seat scripts under scratchpad/seats/assess-kinetic/. The repository tree was left clean.

<details><summary>Re-execution log (verbatim)</summary>

```text
Seat directory: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/assess-kinetic/ (kin.py = my instrument, written from the reply's stated coupling definition and the promoted 07-31 run_custom/make_sig_duty listings before cascade_driver.py was opened; cascade_driver.py was read only afterwards, for audit). Released /home/user/FableComputer/fable-model-chain imported unedited with PYTHONDONTWRITEBYTECODE=1; run_all.py never run; `git status --short | wc -l` = 0 at the end.

$ python3 -c "import sys,numpy,platform;print(sys.version, numpy.__version__, platform.machine(), platform.system())"; nproc
3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0] 2.4.6 x86_64 Linux
4

$ PYTHONDONTWRITEBYTECODE=1 python3 phase1.py   # released bracket generalised to N (= run_all.measure_Mth_num at N=240); cell 1 alone, seed-7 40-slot PRBS, duty 0.8, 2e-3, cfl 0.4
('mth', np.float64(0.16894319463373797), 57.454991579055786)
('c1_m30_s7_P', 1728000, 75.36018800735474)
('c1_m28_s7_P', 1612800, 72.06415295600891)
M_th_num(240) = np.float64(0.16894319463373797)  shipped 0.16894319463373791  rel dev 3.285787944971905e-16
bias = np.float64(0.11826023624361658)
('c1_m30_s7_A', 1898294, 68.90229678153992)
('c1_m28_s7_A', 1771741, 64.79647779464722)

$ PYTHONDONTWRITEBYTECODE=1 python3 gate.py
m=30 cav: G_worst1 8.287855791924049 G_mean1 8.410165 floor -11.828336851446547 eye 11.7051 pp 0.3058
      drn_h: G_worst1 8.663537 floor -11.775002445228234 mean1 0.03396500068703142; slot-mode drn_h floor -15.6649 (peak-mode gap 3.890)
      rel dev vs promoted: G 3.86e-15 floor cav 5.68e-14 floor drn_h 1.32e-13
      passive mean-'1' drn_h 0.012375; passive port transfer (mean-'1' drn_h passive / 2e-3) = 15.8296 dB; active drn_h mean-'1' over launch 24.6000 dB
m=28 cav: G_worst1 8.131548730367582 G_mean1 8.223143 floor -10.731214907969104 eye 10.6398 pp 0.2297
      drn_h: G_worst1 8.436004 floor -11.150570102407642 mean1 0.0329483883046833; slot-mode drn_h floor -14.6104 (peak-mode gap 3.460)
      rel dev vs promoted: G 3.32e-08 floor cav 8.58e-09 floor drn_h 9.18e-09   [m=28 targets are 08-12's six-decimal quotes; deviation = quote precision]
      passive mean-'1' drn_h 0.012349; passive port transfer (mean-'1' drn_h passive / 2e-3) = 15.8117 dB; active drn_h mean-'1' over launch 24.3361 dB
GATE PASSED (m = 30 targets 8.287855791924017 / -11.828336851447219 / -11.775002445226676).

$ PYTHONDONTWRITEBYTECODE=1 python3 phase2.py   # cell 2 clamp = 1 + kappa*(h1[-1]-1) at the same physical time (cell 1's state at t_k; exact lockstep for AA/PP, np.interp for AP), kappa = 10^(J/20); matched boundary-driven single cell at A*
A* (m30, J=-1) = 0.030271338726030064
('c2_m30_J-1_AP', 1728000, 121.6)
('c2_m30_J-1_PP', 1728000, 121.7)
('c2_m30_J-1_AA', 1898294, 131.8)
('match_m30_A', 1898294, 136.4)
('match_m30_P', 1728000, 119.2)
('c2_m30_J-20_AA', 1898294, 132.1)
('c2_m30_J-20_PP', 1728000, 122.1)
('c2_m30_J-20_AP', 1728000, 123.1)
('c2_m28_J-1_AA', 1771741, 108.6)
('c2_m28_J-1_PP', 1612800, 98.6)
('c2_m28_J-1_AP', 1612800, 98.6)
('c2_m30_J-25_AA', 1898294, 103.6)   [not scored: its PP/AP twins were not run]

$ PYTHONDONTWRITEBYTECODE=1 python3 score2.py   # definition A (cav, over the passive twin chain), window rule = promoted window delayed by the passive-chain envelope lag rounded to 1/8 rt
=== m=30 J=-1: my passive stage-1->2 envelope lag (moving-mean xcorr) 2.580 rt; Hilbert 2.544 rt; rule shift used 2.625 rt
  [unshifted 0.000 rt] chain/passive-chain cav worst 12.734 mean 13.139 | G4_A worst 1.537 mean 1.562 | G4_A drn_h 1.486 | G4_B 1.788
      c2c worst 4.649 mean 5.003 | upstream-through-passive worst 8.062 mean 8.136 (sum of means 13.139)
      stage-2 floor peak cav -3.56 / drn_h -3.09 / slot-mode drn_h -4.10 | pp 0.997 | eye 3.15 | mean-1 drn density 0.3166 | input amp to cell 2 0.03027
  [exact-lag 2.580 rt] chain/passive-chain cav worst 13.017 mean 13.350 | G4_A worst 1.571 mean 1.587 | G4_A drn_h 1.550 | G4_B 1.804
      c2c worst 4.712 mean 4.981 | upstream-through-passive worst 8.270 mean 8.369 (sum of means 13.350)
      stage-2 floor peak cav -4.65 / drn_h -4.31 / slot-mode drn_h -6.22 | pp 0.836 | eye 4.31 | mean-1 drn density 0.3310 | input amp to cell 2 0.03027
  [rule 2.625 rt] chain/passive-chain cav worst 13.103 mean 13.399 | G4_A worst 1.581 mean 1.593 | G4_A drn_h 1.550 | G4_B 1.804
      c2c worst 4.798 mean 5.030 | upstream-through-passive worst 8.270 mean 8.369 (sum of means 13.399)
      stage-2 floor peak cav -4.70 / drn_h -4.31 / slot-mode drn_h -6.26 | pp 0.750 | eye 4.39 | mean-1 drn density 0.3310 | input amp to cell 2 0.03027
  passive stage-2 transfer (PP mean-1 drn_h over passive stage-1 mean-1 drn_h, rule window): 15.815 dB (J removed)
=== m=28 J=-1: my passive stage-1->2 envelope lag (moving-mean xcorr) 2.576 rt; Hilbert 2.514 rt; rule shift used 2.5 rt
  [unshifted 0.000 rt] chain/passive-chain cav worst 12.623 mean 13.039 | G4_A worst 1.552 mean 1.586 | G4_A drn_h 1.519 | G4_B 1.802
      c2c worst 4.596 mean 4.990 | upstream-through-passive worst 8.001 mean 8.049 (sum of means 13.039)
      stage-2 floor peak cav -2.92 / drn_h -2.43 / slot-mode drn_h -3.20 | pp 1.041 | eye 2.50 | mean-1 drn density 0.3116 | input amp to cell 2 0.02937
  [exact-lag 2.576 rt] chain/passive-chain cav worst 12.917 mean 13.281 | G4_A worst 1.589 mean 1.615 | G4_A drn_h 1.555 | G4_B 1.815
      c2c worst 4.667 mean 4.982 | upstream-through-passive worst 8.218 mean 8.299 (sum of means 13.281)
      stage-2 floor peak cav -4.02 / drn_h -4.42 / slot-mode drn_h -5.38 | pp 0.897 | eye 3.65 | mean-1 drn density 0.3231 | input amp to cell 2 0.02937
  [rule 2.500 rt] chain/passive-chain cav worst 12.917 mean 13.281 | G4_A worst 1.589 mean 1.615 | G4_A drn_h 1.555 | G4_B 1.815
      c2c worst 4.667 mean 4.982 | upstream-through-passive worst 8.218 mean 8.299 (sum of means 13.281)
      stage-2 floor peak cav -4.02 / drn_h -4.31 / slot-mode drn_h -5.24 | pp 0.897 | eye 3.65 | mean-1 drn density 0.3231 | input amp to cell 2 0.02937
  passive stage-2 transfer (PP mean-1 drn_h over passive stage-1 mean-1 drn_h, rule window): 15.815 dB (J removed)
=== m=30 J=-20: my passive stage-1->2 envelope lag (moving-mean xcorr) 2.580 rt; Hilbert 2.544 rt; rule shift used 2.625 rt
  [unshifted 0.000 rt] chain/passive-chain cav worst 15.620 mean 15.777 | G4_A worst 1.885 mean 1.876 | G4_A drn_h 1.826 | G4_B 1.127
      c2c worst 7.291 mean 7.418 | upstream-through-passive worst 8.286 mean 8.359 (sum of means 15.777)
      stage-2 floor peak cav -1.87 / drn_h -1.88 / slot-mode drn_h -2.98 | pp 0.394 | eye 1.71 | mean-1 drn density 0.0486 | input amp to cell 2 0.00340
  [exact-lag 2.580 rt] chain/passive-chain cav worst 16.007 mean 16.365 | G4_A worst 1.931 mean 1.946 | G4_A drn_h 1.912 | G4_B 1.155
      c2c worst 7.557 mean 7.813 | upstream-through-passive worst 8.450 mean 8.551 (sum of means 16.365)
      stage-2 floor peak cav -3.62 / drn_h -4.06 / slot-mode drn_h -5.23 | pp 0.884 | eye 3.26 | mean-1 drn density 0.0527 | input amp to cell 2 0.00340
  [rule 2.625 rt] chain/passive-chain cav worst 16.199 mean 16.477 | G4_A worst 1.954 mean 1.959 | G4_A drn_h 1.912 | G4_B 1.155
      c2c worst 7.749 mean 7.926 | upstream-through-passive worst 8.450 mean 8.551 (sum of means 16.477)
      stage-2 floor peak cav -3.73 / drn_h -4.06 / slot-mode drn_h -5.27 | pp 0.693 | eye 3.45 | mean-1 drn density 0.0527 | input amp to cell 2 0.00340
  passive stage-2 transfer (PP mean-1 drn_h over passive stage-1 mean-1 drn_h, rule window): 15.744 dB (J removed)
[All reply rows at the rule shift reproduce to the printed digit: Table 1 m30/J-1 13.103, 1.581/1.593/1.550/1.804, unshifted 12.734; m28/J-1 12.917, 1.589/1.615/1.555/1.815; Table 2a 4.798/5.030, 4.667/4.982; Table 4/5 J-20 7.749/7.926, 1.954/1.959, -3.73/-4.06/-5.27, pp 0.693, eye 3.45; Table 3 stage 2 at the exact lag 13.00/4.70 vs mine 13.017/4.712 at my 2.580 rt estimate.]

$ PYTHONDONTWRITEBYTECODE=1 python3 score3.py   # (c) matched row, (d) residue
(c) matched A*=0.030271: boundary-driven G worst 4.797 mean 4.929 floor -13.083 | c2c(rule) 4.798/5.030 -> Delta worst +0.001 mean +0.101 | c2c(unshifted) Delta worst -0.149 mean +0.073
(d) m=30: n(after-1 '0')=8, n(after-0 '0')=8; mean-1 windowed peak 0.033965, first-quarter 0.021123
      after-1 '0': window -11.78 | first quarter over (a) -5.70 over (b) -1.57 | whole slot over (a) -5.70 | argmax at 0.008..0.009 slot
      after-0 '0': window -36.31 | first quarter over (a) -30.07 over (b) -25.94
      '0'-slot energy over mean '1'-slot energy: max -10.56 median -22.94 dB   [my median is over all scored '0' slots; the reply's -13.8 uses a different set, unstated]
(d) m=28: n(after-1 '0')=8, n(after-0 '0')=8; mean-1 windowed peak 0.032948, first-quarter 0.020022
      after-1 '0': window -11.15 | first quarter over (a) -5.31 over (b) -0.98 | whole slot over (a) -5.31 | argmax at 0.016..0.017 slot
      after-0 '0': window -33.50 | first quarter over (a) -27.70 over (b) -23.38
      '0'-slot energy over mean '1'-slot energy: max -10.01 median -21.48 dB

$ PYTHONDONTWRITEBYTECODE=1 python3 score4.py   # window-rule rounding sensitivity
m=28 J=-1 shift 2.5 rt: chain worst 12.917 G4_A 1.589 | c2c 4.667/4.982 | floor cav -4.02 mode -5.24
m=28 J=-1 shift 2.625 rt: chain worst 12.917 G4_A 1.589 | c2c 4.667/4.982 | floor cav -4.02 mode -5.46
m=30 J=-1 shift 2.5 rt: chain worst 13.000 G4_A 1.569 | c2c 4.704/4.969 | floor cav -4.64 mode -6.16
m=30 J=-1 shift 2.625 rt: chain worst 13.103 G4_A 1.581 | c2c 4.798/5.030 | floor cav -4.70 mode -6.26
[At m = 28 my estimator's 2.576 rt rounds to 2.625 rather than the reply's 2.5, but gain does not move; within the disclosed ~0.1 dB.]

$ PYTHONDONTWRITEBYTECODE=1 python3 phase3.py   # cfl lever at fixed N = 240, m = 30, seed 7, bias held at the released 0.7*M_th_num(240)
('c1_m30_s7_P_cfl0.8', 864000, 55.3)
('c1_m30_s7_A_cfl0.8', 949147, 58.9)
('c1_m30_s7_P_cfl0.2', 3456000, 137.1)
('c1_m30_s7_A_cfl0.2', 3796589, 146.9)
('c2_m30_J-1_AA_cfl0.8', 949147, 30.1)
('c2_m30_J-1_PP_cfl0.8', 864000, 25.9)
('c2_m30_J-1_AP_cfl0.8', 864000, 28.8)
('c2_m30_J-1_AP_cfl0.2', 3456000, 109.0)
('c2_m30_J-1_PP_cfl0.2', 3456000, 109.1)
('c2_m30_J-1_AA_cfl0.2', 3796589, 123.2)

$ PYTHONDONTWRITEBYTECODE=1 python3 score5.py | grep -v ...   (score5 imports score2, which re-printed score2's output above verbatim; only score5's own lines are reproduced here)
cfl=0.2: cell1 G_worst1 7.392 floor cav -16.69 drn_h -17.03 mode -22.41 | passive transfer 15.01 dB | residue(a) -8.11 dB
        chain J=-1 (lag 2.400 rt -> shift 2.375 rt): chain worst 13.112 G4_A 1.774 | c2c 5.504 | stage-2 floor cav -8.35 drn_h -8.00 mode -11.65 | eye 8.20
cfl=0.4: cell1 G_worst1 8.288 floor cav -11.83 drn_h -11.78 mode -15.66 | passive transfer 15.83 dB | residue(a) -5.70 dB
        chain J=-1 (lag 2.580 rt -> shift 2.625 rt): chain worst 13.103 G4_A 1.581 | c2c 4.798 | stage-2 floor cav -4.70 drn_h -4.31 mode -6.26 | eye 4.39
cfl=0.8: cell1 G_worst1 8.588 floor cav -8.89 drn_h -8.77 mode -11.66 | passive transfer 16.34 dB | residue(a) -4.21 dB
        chain J=-1 (lag 2.640 rt -> shift 2.625 rt): chain worst 12.756 G4_A 1.485 | c2c 4.202 | stage-2 floor cav -3.37 drn_h -2.97 mode -3.49 | eye 2.95

$ python3 inmodel.py   # in-model checks: two cascaded single-pole ring-downs; released regen loop model under an energy-consistent junction
two-resonator floor estimate: floor2 = floor1 + 20log10(1 + ln(10^(-floor1/20)))
  cfl0.2 m30 drn_h: floor1 -17.03 -> predicted stage-2 -7.60 dB; measured -8.00
  cfl0.4 m30 drn_h: floor1 -11.78 -> predicted stage-2 -4.33 dB; measured -4.31
  cfl0.8 m30 drn_h: floor1 -8.77 -> predicted stage-2 -2.71 dB; measured -2.97
  cfl0.4 m30 J=-20 drn_h: floor1 -11.78 -> predicted stage-2 -4.33 dB; measured -4.06
  cfl0.4 m28 drn_h: floor1 -11.15 -> predicted stage-2 -3.98 dB; measured -4.31
a_loss 0.7451522890452021; passive steady-state enhancement 1/(1-a) = 3.9239 (11.87 dB), x2 at the open end = 17.89 dB
loop at bias 0.7*M_th_num(240): 0.9450
  J=+0 dB: |t|^2 1.000 |r| 0.000 | cell-2 drive over launch, passive: ideal-buffer construct +17.89 dB vs energy-consistent drain +0.00 dB | DS loop with loaded drain 0.000, CW regen over passive +0.00 dB (unloaded +13.32)
  J=-1 dB: |t|^2 0.794 |r| 0.454 | cell-2 drive over launch, passive: ideal-buffer construct +16.89 dB vs energy-consistent drain +2.58 dB | DS loop with loaded drain 0.429, CW regen over passive +1.28 dB (unloaded +13.32)
  J=-3 dB: |t|^2 0.501 |r| 0.706 | cell-2 drive over launch, passive: ideal-buffer construct +14.89 dB vs energy-consistent drain +3.49 dB | DS loop with loaded drain 0.667, CW regen over passive +3.07 dB (unloaded +13.32)
  J=-6 dB: |t|^2 0.251 |r| 0.865 | cell-2 drive over launch, passive: ideal-buffer construct +11.89 dB vs energy-consistent drain +2.99 dB | DS loop with loaded drain 0.818, CW regen over passive +5.80 dB (unloaded +13.32)
[Labelled in-model: single-pole loop model, lossless junction apart from transmission, steady state.]

$ PYTHONDONTWRITEBYTECODE=1 python3 lat.py   # passive stage-1->2 same-sign peak lag vs cfl
cfl=0.2: passive stage-1->2 same-sign peak lag median 1.0319 units = 0.5160 rt (min 0.5160, max 0.5163); excess over L/s 0.0319 units = 46.0 steps (dt 0.00069)
cfl=0.4: passive stage-1->2 same-sign peak lag median 1.0500 units = 0.5250 rt (min 0.5250, max 0.5250); excess over L/s 0.0500 units = 36.0 steps (dt 0.00139)
cfl=0.8: passive stage-1->2 same-sign peak lag median 1.0639 units = 0.5319 rt (min 0.5319, max 0.5319); excess over L/s 0.0639 units = 23.0 steps (dt 0.00278)

$ PYTHONDONTWRITEBYTECODE=1 python3 plane.py   # is the drain velocity an independent plane?
active cell 1 mean-'1' drain |dh| 0.033965, |du| 0.004065, ratio du/dh 0.1197 vs M = 0.1183
active: max|du - (u0/(1+dh) - u0)| = 2.879e-04 vs max|du| = 4.233e-03
passive cell 1: mean-'1' drain |du| 8.085e-05 -> -27.87 dB over launch; |dh| 0.01237 -> 15.83 dB

$ for k in <nine registered key names>; do grep -rl "$k" notes fable-model-chain/results.json fable-model-quantum/results.json papers | wc -l; done
cascade2_G4_worst1_ratio_J1 0 / cascade2_G4_worst1_ratio_J6 0 / cascade2_G4_smallsignal_limit 0 / passive_port_density_transfer_dB 0 / cascade2_cell2_gain_worst1_J1_dB 0 / cascade2_zero_floor_J1_dB 0 / zero_slot_residue_unwindowed_dB 0 / cascade_stage_latency_rt 0 / cascade_relaunch_junction_dB 0

$ python3 (inline) — text extraction of papers/Fable-Computer-Part-I.docx (word/document.xml, tags stripped) and search. Verbatim hits:
[§7.4] '... sustains +8.4 to +9.3 dB net per cell (two-cell total ~+17–19 dB over the passive chain, computed as twice the per-cell figure) ...' ; 'The direct two-cell time-domain test is open work, tracked in the project roadmap.'
[§9.4] 'A junction is a gate-defined density step between adjacent segments. For the ideal step the velocity mismatch is mild (s ∝ n¹ᐟ⁴-class under Eq. (1)), and the reflective loss of even a 2× density step is < 0.1 dB — the −1 to −3 dB budgeted per junction is therefore dominated by non-ideal effects: scattering at the gate gap, mode mismatch through the ungated sliver, and radiation.'
[Table 6] 'Cascadability | in-model yes: 2 cells, +8.4–9.3 dB/cell through −6 dB junctions'; [§10] 'The die plan includes passive twins for differential measurement'.

Read, not re-executed: the session's cascade_driver.py (after my runs; its causal previous-state coupling, window masks and lock-in match my instrument), stage1-posts/quanta.md ('0.535 dB spent entirely on reflection allows |r|² ≤ 11.6 % per junction'), and the promoted notes INDEX, 07-31 §2/§8, 08-01 gated §4–§7, 08-02 §0 item 4 / §3.1 and its appended vote record, 08-12 §1–§7, 07-22-cavity-ringdown §1–2. Not re-executed (budget): N = 480/720 rows, seeds 11/13, Table 2b, Table 3 stages 3–5, J = −3/−6/−10/−15/−25 full rows, the reply's velocity-plane chain (the plane question was settled by plane.py).

$ cd /home/user/FableComputer && git status --short | wc -l
0
```

</details>
