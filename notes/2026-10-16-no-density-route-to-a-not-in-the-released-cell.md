# Where does a NOT get its '1'? Nowhere in the released cell: the delivered '1' rectifies +0.86–1.06 of its own swing into the drain density — accumulating, the enhancing sign — against the −0.17 … −0.28·n a 10-dB inversion needs where it is reached at all; the only in-model NOT is destructive interference holding carrier phase to within 10–12° (12.3 / 10.7 / 10.1° on N = 240 / 480 / 720, tightening under refinement), with sharpness k ≈ 1.3 (2.9 on Eq. (5)'s tanh scale) and a restoring margin of at most ≈ 0.01 of the swing on the coarsest grid, and a threshold AND separates '1 + 1' from '1' by 2.6–3.3 dB

**Status:** promoted 2026-10-17 **by maintainer direction** after the pipeline's round-4 cap, run as a scope reduction (the 2026-08-02 / PR #98, 2026-10-09 / PR #131 and 2026-10-16 / PR #136 precedents) — the round ladder ran 3-of-3 store with 6 / 5 / 5, 4 / 6 / 3, 2 / 4 / 4, 2 / 3 / 2 required edits (round 1, stage-3 assessment; rounds 2–3; round 4, the cap), never a clean pass; no round refuted a measurement. Twelve assessor seats plus two pre-publication check seats; every claimed defect was re-executed by the session before it was accepted (rework records: [round 2](https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18975097), [round 3](https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18975723), [round 4](https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18976535)); no required edit was declined in any round. **This note's text is the round-4 reply as posted ([part 1](https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18976536), [part 2](https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18976538)) with the two corrections of its [erratum](https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18976555) and the corrections of its [post-cap supplement](https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18980894) applied** (the erratum: two stale copies of a superseded phase-window band, '10.7–12.3°' → '10.1–12.3°', in §4 B.3 and §5; the supplement: the round-4 seats' required edits and the accepted non-blocking residues, each re-executed and listed there — the held-amplitude drain-velocity shape in item 1, §3, `inv_depletion_10dB` and D-INV-2, §5's route-(iii) scope and route-(ii) windows by grid, the §6 bias-choice row, the pinned-construction values in every copy and the bands of `inv_gn_dn_10_90` / `inv_gn_nth`, the oscillator statistic, listing 5's bisection rows, labels and cross-references — 30 exact replacements by `apply_r4_supplement.py`, [listing 6](https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18980895)), disclosed here; the three round-4 seats were cut by a usage limit and resumed or relaunched as the [round-4 tally](https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18980298) discloses; the posted reply and every vote record stand unedited. Full verbatim records: [discussion #137](https://github.com/ryoji-info/FableComputer/discussions/137). Contests **no** `results.json` value; moves **no** promoted key; corrects no promoted note — it grades manuscript claims (Part I §5, §6.5 Table 4; `cell.py`, `disorder.py`) and qualifies five notes, which receive dated post-promotion annotations in the same PR ([07-15](2026-07-15-finite-sharpness-is-not-a-variance.md), [07-21](2026-07-21-composed-regeneration-envelope.md), [08-02](2026-08-02-zero-floor-spec-dissolved.md), [10-08](2026-10-08-no-rail-scale-one-at-deciding-inputs.md), [10-13](2026-10-13-phase-is-not-the-easier-half-for-the-cell.md)); 07-17's limitation 5 is marked consistent. **Scope, stated by the text itself:** every result is about the released Galilean shallow-water cell; the interferometric inverter's windows and margin are grid-scoped and tighten under refinement; the registered margin key was withdrawn at the cap (§8 item 8).

**Prompted by:** [Fable Session — 2026-10-16, discussion #137](https://github.com/ryoji-info/FableComputer/discussions/137) (🧵 Fabric's winning prompt, 2-of-3 — 🌊 Kinetic → Fabric, ⚛️ Quanta → Fabric; 🧵 Fabric → Quanta — on a re-vote the maintainer directed after Fabric's run-2 lab post was added; a first vote with one ballot returned was aborted and is disclosed in the discussion body).

**Correction history, disclosed.** Two pre-publication check seats on `claude-fable-5-1` (both REVISE; every item re-executed and applied before publication — [record 1](https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18974304), [record 2](https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18974307), [dispositions](https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18974308); two items declined on the record / on measurement) found the first burst-timing instrument leaky and the phase-window key unbracketed; the stage-3 round found the −0.20 threshold depletion to be the absolute leg's (G1's pin: −0.30), Eq. (5)'s Δn to be the tanh width (2.197× narrower than the 10–90 % width), and 10-13's (C′) mis-graded; round 2 found the all-'1' burst train, the AND's 10 % point and the drain-velocity band; round 3 found the 7.5° "tristability" to be an interpolant artifact, the NOT's windows to tighten by grid, and the held-amplitude fixed-current extinction never to reach 10 dB; round 4 withdrew what could not be supported (§8 item 8) and changed no verdict. **Executing model:** the execution and every rework round ran in-session on `claude-fable-5-1`; the candidate, vote and assessor seats on `claude-opus-5-5`; the two pre-publication check seats on `claude-fable-5-1`.

## 0. Executive verdict (eight items)

1. **Does the released cell supply a NOT, and a threshold AND, at the delivered swing — and through which mechanism?** *In-model (released cell, both bias legs, N = 240–720):* **no, through none of its own mechanisms.** The one density-shifting coupling the cell contains — rectification of the input into a DC drain-density shift (Dyakonov–Shur's detector effect, derived in §2 and reproduced on the grid ladder) — has the **wrong sign for Eq. (5)'s depleting NOT** (a '1' *raises* the drain density, β_drain = +0.86 … +1.06 of the swing on the retuned absolute leg (0.69–0.76 on the shipped tuning / analytic leg), and — read through Table A on the 08-02 item-4 plane assumption that this cell's drain-plane density is the next cell's input, an in-model composition — raises the pump's gain by +0.3 … +0.7 dB) and, even wired to deplete, an operational (10–90 %) sharpness **k ≈ 0.08–0.12 — 0.18–0.26 on Eq. (5)'s own tanh scale, where Part I's k ≥ 5 is read (the 10–90 % width of ½[1 + tanh(x/Δn)] is 2.197·Δn, so k ≥ 5 is an operational 2.3 and `K_SHARP` = 8 an operational 3.6)**. The cell's own g(n_local), measured directly (Table A), is a resonance curve with **a 10–90 % width of 0.15–0.20 of the density at the pump on the pinned construction (off-state at the 10-dB depletion δ_off = −0.20; 0.14–0.22 over every stored series, A.6; Eq. (5)'s Δn = 0.07–0.09·n at the pump) and n_th 4–7 % below the operating density**: 10 dB of extinction costs a −0.17 … −0.28·n depletion where it is reached — on the drain density under either drive convention, and on the intracavity and drain-velocity observables under a swing that scales with the density or at fixed drift; at fixed drain current with the input amplitude held, the intracavity extinction peaks at 9.5–9.8 dB near −0.25 and falls back as the cell nears its own threshold (−7.9 / −7.4 dB at −0.30), the drain-velocity extinction rises monotonically but only to 8.0 / 8.3 dB at −0.30, and neither reaches 10 dB (N = 240 / 480 at G1's pin), while the drain density does (−10.1 / −10.3 dB at −0.20) (§3). No plasmonic input in the record (0.0076–0.0269) supplies more than +0.0045 … +0.0234 of accumulation at N = 240 (to +0.028 at N = 720).
2. **The only NOT the released cell admits is interference, not a gate.** *Demonstrated (released solver, two coherent source tones, N = 240 / 480 / 720):* an input '1' launched in antiphase to a clock pulse of the same amplitude cancels it at the source plane; the output extinction is **−17.6 / −11.7 / −8.4 / −6.3 / −3.5 dB at 5° / 10° / 15° / 20° / 30° of phase error** (N = 240; −7.4 dB at 15° on N = 480) and **−16.4 / −10.6 / −8.8 dB at ±10 % / −20 % / +25 % amplitude mismatch**. Ten dB needs **a phase error ≤ 12.3° / 10.7° / 10.1° on N = 240 / 480 / 720 (direct rows 12° / 13°, 10° / 12°, 10° / 11°) — tightening under refinement, the continuum value open below 10° (a three-grid fit and first-order Richardson on the direct crossings put it at ≈ 8.5–9.0°, an in-model estimate, with 9.7° predicted at N = 960; `inv_numerics5.py`) — and an amplitude match within ±21 % (N = 240; ±17.6 % at N = 720, where 0.82 reads −9.8 dB)**; Part I's ±15° budget alone leaves −7.4 … −8.4 dB. The cell's compression *degrades* the extinction (output dB = 0.62–0.83 × input dB), and the transfer is V-shaped with **k = 1.31 / 1.33 (N = 240 / 480, direct 10–90 % rows; 2.9 on Eq. (5)'s tanh scale)**; built as an inverter pair under the F = 2 unity normalisation (10-08's untested cell-to-cell assumption — *in-model*: no two-cell run exists), its restoring margin on the coarsest grid is **≈ 0.01 of the swing at perfect phase, and its bistability is lost between 5° and 7.5° — on direct two-tone rows the 7.5° pair is monostable (one attracting fixed point at 0.580, slope −0.99)**; one seat's finer transfer tables halve the margin with each grid refinement (0.005 / 0.003 at N = 480 / 720) and lose bistability earlier, so **whether any restoration survives the continuum is open** — at best a marginally restoring inverter against the 0.26 Part I's k = 8 design rule promises (§4 B.3).
3. **A threshold AND does not exist in-model either.** *Demonstrated:* two in-phase delivered '1's produce **+2.86 / +2.65 / +2.59 dB (cav) and +3.28 / +2.97 / +2.86 dB (drain)** more than one at N = 240 / 480 / 720 (+2.73 / +3.13 at 30° relative phase, +1.50 / +1.72 at 90°, N = 240; the '1 + 1' rows run above the velocity ceiling); the transfer over 0 → 2·0.0197 is concave (out ∝ A^0.72 below the '1', A^0.48 above it — 10-08 item 4's `rail_sweep_output_slope` = 0.39–0.60 read at one drive doubling, 2^0.39…0.60 = 2.3–3.6 dB), so the "threshold applied to the sum of two input fields" has **k ≈ 1.3 (2.9 on the tanh scale) and a 2.6–3.3 dB separation**, never 10 dB — the cell compresses, it does not threshold.
4. **The pump cannot be the cell itself.** *Demonstrated (N = 240 / 480, 240–960 round trips):* biased above its grid threshold the cell self-oscillates (a '1' from an empty input), but an injected '1' **changes its output by a time-mean of −0.3 / −2.0 / −0.7 dB at 1.20 / 1.10 / 1.05·`M_th_num` (N = 240; free limit cycles 0.382 / 0.318 / 0.262, reached after 150–500 round trips) and −0.7 dB at N = 480 (1.10·`M_th_num`(240), 1.17 of that grid's own threshold; free limit cycle 0.360), the injected output quasi-periodic within −2.5 … +0.4 dB of the free limit cycle on every record (time-means and ranges of 60-round-trip window slot-peak means over the second half of each record — 420–900 round trips at N = 480, `inv_numerics5.py`; single-slot peaks swing wider, to ≈ −7 dB on the N = 480 record by one round-4 seat's count, a beat and not a quench)** — it pulls, it does not quench — and the oscillation's own build-up takes 150–250 ps (10–17 slots) at 5–10 % above the grid threshold. These rows run above the velocity domain (max|hu/h| = 0.41–0.62 against 0.429, 10-08 limitation 10): they are the released model's readings, not physical ones. A NOT therefore has an energy source only where a clock burst is fed in — the launcher's, at the launcher's level (08-01 §7, 10-08 item 8) — which is exactly 10-13's (C′) reading (item 6); a cascaded datapath with no clock fed in has no inverter.
5. **What a depleting gate would need, priced.** *In-model (Table A + §4 route iii):* the gate-segment reading of Eq. (5) — a detector segment rectifies the input and its DC voltage is applied to the cell's gate, sign chosen by wiring — reaches −20 % only with an **electrical gain of ×9–12 behind a biased detector segment (×43–52 behind an unbiased one; ×8–17 and ×37–73 for the whole −0.17 … −0.28·n band), or input swings of 0.08–0.28** on every extrapolation of the measured law (the steepest knee exponent continued from the knee gives 0.08, from the highest row 0.11; the flattest gives 0.28), above the velocity domain (0.024–0.036) and the coded rail. Timing of the rectified shift under 07-31's own duty-0.8 launch at 69 GHz (raised-cosine 2-rt edges, carrier referenced to the window centre, a leak-free two-period window — §8 item 2): **17 / 27 / 75 / 105 / 100 % of its 11-ps value at 1.45 / 2.9 / 5.8 / 8.7 / 11.0 ps, 90 % first reached at 6.9 ps** (5.0 ps at the band top), decay **2.6 ps by the registered log-linear fit (2.0–3.0 ps across the three estimators)** after the window closes, and a residual at the next slot's start of **21–28 % in an all-'1' train and 27–35 % after an isolated '1'** (the measured '1' → '0' case).
6. **The regime fork, priced.** *In-model:* an inverter exists only as route (ii) (interference, phase held to 10.1–12.3° by grid) or route (iii) (an external electrical gain stage), both pump-fed by the clock burst — (C′)'s reading — in the clocked Eq. (5) regime; a cascaded datapath with no clock fed in has no inverter (item 4). 10-13's (C′) — the 783 inverting cells pump-fed, their outputs comb references — is therefore **the reading that has a mechanism** (qualified, §6): every in-model inverter is pump-fed by the clock burst, either by interference or behind an external gain stage; what the released cell does not supply is an Eq. (5) inverter that works by shifting n_local, and route (ii) adds a per-inverter input-to-pump phase window of 10.1–12.3° (by grid, tightening) that (C′)'s count of inverter outputs as fresh references does not carry. An inversion-free (dual-rail) lane is the alternative the record has not counted (§5, not run here).
7. **The fixed-current cell depletes into its own threshold.** *In-model (continuum eigencondition re-derived, §2; demonstrated on the grid ladder, §1 G5–G6):* at the absolute leg's drift 0.118260 — **0.80 of the retuned continuum threshold M_c = 0.147679**, 10-08 item 5's drifting absolute bias — a −20 % density shift closes the cell's margin to its own threshold as (1 + δ)^−1 (the local Mach number rises as (1 + δ)^−3/2 and the local threshold falls as (1 + δ)^−1/2) and puts the continuum cell **at threshold (Im ω = −0.0004 at −0.200; the root crosses zero at δ = −0.202)**; the −10 dB readings at δ = −0.20 are held by Lax–Friedrichs damping (−0.018 / −0.009 / −0.005 per unit time at N = 240 / 480 / 960) and the base **self-oscillates at δ = −0.30 on N = 480**. **At G1's pin — 0.7 × the device's own threshold — the crossing is δ = −0.305 (−0.302 under Eq. (1)'s law; the analytic leg −0.308)**, and on N = 240, where the absolute leg is that pin, the grid base is marginal at −0.30 (G6); at 0.745·M_c and 0.760·M_c, where the absolute leg sits relative to the N = 480 / 720 grid thresholds, the crossings are −0.259 / −0.244, which is why the N = 480 row at −0.30 oscillates. At fixed drift the base stays damped under the released rate and the extinction is detuning alone (−14.6 dB at −0.30; −21.6 dB at −0.50 on a base still stable at −0.095 per round trip); under a rate scaling as n^+½ the fixed-drift cell, too, reaches threshold (−0.36 at the absolute leg, −0.51 at the pin; §8 item 1). So "inversion as a bias choice" is, at the absolute leg, an approach to self-oscillation; at G1's pin a 10-dB depletion (−0.17 … −0.28) brings the cell to 0.84–0.97 of its threshold — under the released, density-independent momentum-relaxation rate; under 10-15's friction family 1/τ ∝ n^b the pin's crossing is −0.21 at b = +½ (acoustic phonons, where that depletion straddles it) and beyond −0.54 at b = −½ (§8 item 1).
8. **What is open.** Whether graphene's own fluid (10-15) changes the coefficients: the record's Eq. (1) speed law (d ln s/d ln n = 0.214) detunes 2.3× less per unit δ than the solver's √h (Δn larger, k smaller still), its fixed-current threshold depletion is unchanged (the margin closes as (1 + δ)^−1 under both speed laws: the continuum root crosses zero at δ = −0.2004 under Eq. (1)'s law against −0.2023 under √h at the absolute leg, −0.302 against −0.305 at G1's pin), the fixed-drift margin does not move under either, and 10-15's drift law keeps the threshold ×1.7 — labelled, not substituted. The gate's RC, a partial-length gate segment, the kinetic contact layers, and the primary DS-1996 text (not accessible; the closed form is derived here) stay open. **Withdrawn from nothing; contradicted: Part I §5's "established within the model chain" for the NOT, the k ≥ 8 rule and the threshold AND; `cell.py`'s K_SHARP = 8 and `disorder.py`'s β·A_swing = n as descriptions of the released cell; qualified: 10-13's (C′), 10-13 item 7's ±59° / ±84° field-sum tolerance and 10-08 item 7's ×4.83 margin factor, both priced against a k = 8 margin the released cell does not deliver** (§6).
## 1. Gates — what was reproduced before any new instrument was trusted (all *demonstrated*; released chain unedited, `git status --short` empty throughout; macOS arm64 / Python 3.11.2 / numpy 2.4.6)

**G1 — the session runner is the released loop.** `inv_common.run_cell` is `solver.run`'s loop with the released `_step_LF`, the same operation order and the same `dt` rule, extended with a uniform base-density shift δ, several coherent source tones and a gated burst. At δ = 0, one tone, no burst, it is **bit-equal** to `solver.run` in the `drain`, `cav` and `t` series over every step for `cw` (0.0197), `pulse` (3×10⁻³) and `none`, at N = 240 (18,982 steps) and N = 480 (37,965 steps); the two-tone path with a zero second tone differs from the released expression by 0.0 (`inv_gates.out`). The shifted uniform states h = 1 + δ (fixed current: drain clamp u₀ and relaxation target u₀/(1 + δ); fixed drift: relaxation target u₀ and drain clamp (1 + δ)u₀) are **exact steady states of the released step** — max|h − h₀| = 0 and max|δ(hu)| = 0 after 20 round trips at δ = ±0.20 in both modes.

**G2 — the 10-08 §3 row.** Retuned configuration (L = 576.62 nm, f₀ₙ = 0.247350), absolute leg M = 0.7·`M_th_num` = 0.118260, 240 round trips, per-slot peak of `cav` over slots of 1/(0.25 f₀ₙ), second-half mean, active over the same-drive passive: **CW 0.0197 → 6.520 dB, pulse 0.0221 → 6.537 dB** — 10-08 prints 6.520 / 6.537.

**G3 — the 10-13 B.2 row.** Shipped configuration, carrier, CW, 160 round trips, lock-in over the last 80 (40 carrier periods), ratio leg = absolute leg at N = 240, phase of the drain velocity relative to the source drive: 2×10⁻³ → +60.21° (10-13 A.3: +60.21°), 0.0197 → +50.88°; **Δφ = −9.33°** against the row's printed **−9.32°**; drain density Δφ = **−9.61°** (printed −9.61°); `cav` slot-peak gain **5.80 dB, change −2.86 dB** (printed 5.80 (−2.86)) — all four values are the `shipped | carrier | 0.0197` row of the note's Table B.2. The 0.01° on the velocity phase is the lock-in window's integer-period clipping; every other digit matches.

**G4 — Dyakonov–Shur's detector response, derived and converged.** The M = 0 rectified drain-density shift of the released cell (source h = 1 + a sin ωt, drain hu = 0) at a = 0.005, shipped configuration, divided by the closed form derived in §2 (11.893483·a²): **0.8325 / 0.9097 / 0.9523 / 0.9747 at N = 240 / 480 / 960 / 1,920** (the whole-period column of §8 item 2; the exact 30-period column at this tuning reads 0.8338 / 0.9103 / 0.9526 / 0.9749); the deficit 1 − ratio fits K·N^−p with **p = 0.91** (fitted, not assumed) and the first-order Richardson estimate from the two finest grids is **0.9971**. The instrument scales as a² at small drive on the active cell (exponent 1.98 between 10⁻³ and 2×10⁻³, rework rows; 1.63 between the knee rows 0.0076 and 0.0084, where compression has begun — §4) and exactly as a²/4·f at M = 0 by construction of §2.

**G5 — the continuum eigencondition and the linear limit of the shifted base.** The eigencondition re-derived in §2, solved by Newton iteration, returns 08-13 §6's roots to every printed digit: M = 0 → **f = 0.248901620862, Im ω = −0.147083333333** (= −1/(2τₙ), and the closed form √(π²/4 − 1/(4τₙ²))/2π); M = 0.11826023624361653 → **f = 0.245398906394**. For the shifted bases, the ring-down fit of a noise-seeded free run (`inv_gates2.out`, G5b) was found to be a biased estimator (its frequency does not converge with N) and was **replaced** by the exact linear spectrum of the released one-step map: the Jacobian of `_step_LF` about each base by central differences (2N × 2N), its eigenvalues λ → ω = i ln λ/dt. That spectrum converges **first order in 1/N** to the continuum root at every base (`inv_linop.out`):

| base (retuned, abs leg) | N = 240 | N = 480 | N = 960 | continuum (§2) |
|---|---|---|---|---|
| δ = 0 | f 0.244537, Im ω −0.04507 | 0.244976, −0.03673 | 0.245199, −0.03256 | **0.245422, −0.02837** |
| δ = −0.10, fixed current | 0.230694, −0.03300 | 0.231083, −0.02442 | 0.231280, −0.02012 | 0.231478, −0.01581 |
| δ = −0.20, fixed current | 0.215627, −0.01824 | 0.215951, −0.00934 | 0.216116, −0.00488 | **0.216282, −0.00040** |
| δ = +0.10, fixed current | 0.257448, −0.05508 | 0.257930, −0.04694 | 0.258173, −0.04286 | 0.258418, −0.03877 |
| δ = −0.20, fixed drift | 0.217752, −0.04583 | 0.218116, −0.03726 | 0.218300, −0.03296 | 0.218486, −0.02865 |
| δ = +0.10, fixed drift | 0.256886, −0.04475 | 0.257359, −0.03652 | 0.257598, −0.03240 | 0.257838, −0.02827 |

(At the shipped configuration the same instrument returns 0.244513230 at δ = 0, N = 240 — 07-12's exact-operator 0.24451323007878742 to nine digits; the retuned rows above sit 2.4×10⁻⁵ higher by the cell length, as the continuum pair 0.245422 / 0.245399 does.) Two readings of this table are load-bearing below: the **depleted fixed-current base at δ = −0.20 is at the cell's own threshold in the continuum (Im ω = −0.0004)** and is held stable on the released grids only by Lax–Friedrichs damping (−0.018 / −0.009 / −0.005); and the fixed-drift base stays as damped as the unshifted cell at every δ run.

**G6 — base stability of every Table A row** (free runs, growth per round trip; negative = stable): fixed current, N = 240: −0.0522 / −0.0365 / −0.0193 / **−0.0002** at δ = −0.15 / −0.20 / −0.25 / −0.30; N = 480: −0.0348 / −0.0187 / −0.0010 / **+0.0186** — the δ = −0.30 base self-oscillates at N = 480 and is marginal at N = 240, so every reading at δ ≤ −0.25 is scoped as a grid-stabilised reading and δ = −0.30 at N = 480 is an oscillator row, not a transfer row. Fixed drift: −0.0934 / −0.0886 at δ = ∓0.30 (stable everywhere run).

## 2. The derivation — what Eq. (5)'s β has to be in this cell, and the two closed forms the instruments are gated on

**2.1 The physics of "n_local" in the released cell.** The released model is the shallow-water Dyakonov–Shur cavity in `solver.py`: ∂ₜh + ∂ₓ(hu) = 0, ∂ₜ(hu) + ∂ₓ(hu² + h²/2) = −h(u − u₀)/τₙ, source density clamp h(0, t) = 1 + sig(t), drain current clamp hu(1, t) = u₀, local sound speed c = √h, in units L = 1, s(h = 1) = 1. Eq. (5)'s n_local is a *local density* and the only density the released cell has is h. So "a logic input shifting n_local" means one of exactly three things in this model, and §4 measures each: (i) the input is a plasmon burst at the source and shifts the cell's mean density by **rectification** (the second-order DC response of the DS cavity — this is Dyakonov & Shur's 1996 detector effect, and it is already inside the released equations); (ii) the input is converted *outside* the cell to a DC gate voltage and applied as a uniform base-density shift δ (Part I §5's "through a gate segment", §9.6's optical tap) — which is what Table A measures directly as g(δ); (iii) the input adds coherently to the clock pulse at the source plane ("the sum of two input fields"), which changes no density but the drive. A fourth candidate, the cell as its own pump (biased above threshold, quenched by the input), is route (iv).

**2.2 The rectified (DC) response of the M = 0 cell — second-order perturbation theory (in-model: the released equations; demonstrated against the ladder of G4).** Expand h = 1 + η₁ + η₂, u = v₁ + v₂ about the undriven M = 0 cell. First order is the damped standing wave with k² = ω² + iω/τₙ, η₁(0) = a sin ωt, v₁(1) = 0: A(x) = a·cos k(1 − x)/cos k, B(x) = −A′(x)/(1/τₙ − iω). The time-mean of the second-order momentum balance gives d⟨η₂⟩/dx = ⟨η₁v₁⟩/τₙ − ½ d⟨v₁²⟩/dx, with ⟨η₂⟩(0) = 0 fixed by the source clamp and ⟨hu⟩ ≡ 0 by the drain clamp, so

⟨η₂⟩(1) = (1/τₙ)∫₀¹⟨η₁v₁⟩dx + ½⟨v₁(0)²⟩.

Evaluated with the first-order solution (`inv_ds1996.py`, quadrature on 20,001 points) this equals **a²/4 · f(ω)** with f(ω) = 1 + β − (1 + β cos 2k′)/(sinh²k″ + cos²k′), β = 2ωτₙ/√(1 + ω²τₙ²), k = k′ + ik″ — the form the candidate seat recalled as Dyakonov & Shur (1996) — to **3.6×10⁻¹¹** at every frequency in [0.05, 0.6] and in both limits (ωτ ≪ 1: 0.2887 at τₙ = 0.05; ωτ ≫ 1: 900.3 at τₙ = 30). At the shipped carrier, f/4 = **11.893483**; the derived response peaks at f = 0.24895 (the quarter-wave resonance, carrier 0.25). *What was and was not checked against the primary text (standing rule 3):* IEEE Trans. Electron Devices 43, 380 (1996), doi:10.1109/16.485650, could not be read by this session (paywalled; Dyakonov's 1997 DTIC report ADA327735 returned HTTP 403); the closed form above is therefore **this session's own derivation from the released equations**, and the attribution of the identical form to DS-1996 rests on the candidate seat's recall and secondary citations — labelled *in-model (derived here)*, not "read in full". The sign is the physical content: the drain density **rises** (⟨η₂⟩(1) > 0 at every τₙ run) — the detector accumulates carriers at its open drain. In a gated sheet the drain potential rises with it; nothing in the released cell depletes under drive.

**2.3 The linearised cavity about a shifted base (in-model; the gate of every Table A row).** About (h₀, u) with δ(hu) = q: ∂ₜη + ∂ₓq = 0, ∂ₜq + 2u∂ₓq + (h₀ − u²)∂ₓη = −(q − uη)/τₙ; modes e^{i(kx − ωt)} give Ω(Ω + i/τₙ) = h₀k² with Ω = ω − ku (sound speed c = √h₀), the source clamp η(0) = 0 and the drain clamp q(1) = 0 give the eigencondition **e^{ik₁}/k₁ = e^{ik₂}/k₂** for the two roots k₁,₂(ω) of (u² − h₀)k² − (2ωu + iu/τₙ)k + ω² + iω/τₙ = 0. At h₀ = 1 it is 08-13's `cexact.py` condition (G5). The fixed-current threshold of the depleted cell follows from it: at δ = −0.20 the local Mach number u/c = 0.14783/0.8944 = 0.1653 and the cell is at threshold by the exact eigencondition (Im ω = −0.0004 at −0.200, zero at −0.202, G5 — at the absolute leg's drift, 0.80·M_c with M_c = 0.147679 the retuned continuum threshold; at G1's pin 0.7·M_c the crossing is −0.305, at the analytic leg −0.308, at 0.745·M_c / 0.760·M_c −0.259 / −0.244, i.e. δ_th ≈ M/M_c − 1; the small-M form 1/(2cτₙ) = 0.1627 at the retuned τₙ = 3.4359 sits 1.5 % lower, as 07-22's 0.149313 against 0.147083 at δ = 0). **At fixed current the margin to threshold closes as (1 + δ)^−1 — the local Mach number rises as (1 + δ)^−3/2 while the local threshold 1/(2cτₙ) falls as (1 + δ)^−1/2; at fixed drift both move as (1 + δ)^−1/2 and the margin is constant** — the difference between the two bias modes in Table A is this, not the detuning, which is the same √(1 + δ) in both. Under the record's Eq. (1) speed law (c ∝ (1 + δ)^0.2144) the fixed-current crossing moves only to δ = −0.2004 and the fixed-drift margin is again constant (Im ω = −0.02848 / −0.02855 at −0.20 / −0.30).

## 3. Table A — the cell's g(n_local): output against a uniform local-density shift (in-model on the released cell; every row an exact, base-stable steady state unless flagged; retuned configuration unless stated; 120 round trips; `inv_tableA.py`)

Output = per-slot peak of `cav` (second-half mean), relative to δ = 0; the drain-velocity lock-in amplitude is given where it differs materially. **Drive convention (load-bearing):** every row drives the shifted cell as h(0, t) = (1 + δ)(1 + a sin ωt) — a swing *relative to the depleted density*, the convention under which a gate segment scales the whole cell; under an *absolute* swing of 0.0197 at the source (the convention in which the input is an upstream cell's fixed-amplitude output, and the only one a bench realises) the depletion-side rows read 1.9–2.1 dB shallower: δ = −0.20 → **−8.68 / −6.40 dB (cav / drain, fixed current, N = 240), −8.24 / −7.00 (N = 480), −8.45 / −8.02 (fixed drift)**; −0.22 → −9.29 / −6.78 (current); −0.25 → −9.79 / −7.35 (current, where the continuum base is unstable) and **−10.10 / −9.40 (drift)**; −0.30 → −11.52 / −10.52 (drift). So on the intracavity observable, 10 dB at fixed current is reached inside the absolute leg's continuum-stable domain only under the relative convention (the drain velocity crosses at ≈ −0.26, beyond the absolute leg's threshold −0.20 but inside G1's pin's −0.305); under the absolute convention it is reached at fixed drift between −0.20 and −0.25 on the intracavity observable and at ≈ −0.28 on the drain velocity, and **not at all at fixed current: beyond −0.25 the absolute-swing rows read −9.67 / −9.15 / −7.90 dB (cav) and −7.46 / −7.85 / −8.00 (drain velocity) at −0.26 / −0.28 / −0.30 while the drain density goes on to −12.46 / −13.33 / −14.00 — on the intracavity observable the extinction peaks at 9.5–9.8 dB near −0.25 and falls back as the cell nears its own threshold (N = 240, where the absolute leg is G1's pin: −9.79 at −0.25, −7.90 at −0.30; the N = 480 ratio leg, `inv_rework5.py`: −8.68 / −9.45 / −8.80 / −7.40 at −0.20 / −0.25 / −0.28 / −0.30), while on the drain velocity it rises monotonically to only −8.00 / −8.29 dB at −0.30 (N = 240 / 480; −6.61 / −7.63 / −7.90 / −8.29 on the ratio leg) and the drain density keeps falling (−10.26 / −12.39 / −13.38 / −14.30), so a held-amplitude input at the released drain clamp never reaches 10 dB on either velocity observable**. **On the drain-density observable** (the lock-in of h(1), the plane B.1 and 08-02 item 4 use for the next cell's input and what an AC-open drain reads; `inv_rework2.py`) the depletion reads steeper, because a −20 % base shift alone moves the drain velocity +3.9 dB against the drain density (δu = −(u/h)δh at the current clamp): fixed current **−9.02 / −11.90 / −14.55 dB (relative) and −7.73 / −10.06 / −12.12 (absolute) at δ = −0.15 / −0.20 / −0.25**; fixed drift −8.83 / −11.57 / −14.07 and −7.55 / −9.73 / −11.66. On that observable 10 dB costs **−0.17·n (relative) or −0.20·n (absolute) at fixed current** — the latter on the continuum-at-threshold row of the absolute leg — and −0.17 / −0.21 at fixed drift. "M′" is the local Mach number u/√(1 + δ). The pump is the delivered '1' (0.0197, 10-08's central F = 2 point) unless the row says 2×10⁻³ (small signal).

**A.1 — fixed current (the released drain clamp), absolute leg, N = 240, pump 0.0197.**

| δ | M′ | cav (dB) | drain (dB) | phase (°) | run-wide max\|hu/h\| | base |
|---|---|---|---|---|---|---|
| −0.30 | 0.2019 | −10.14 | −10.99 | −37.5 | 0.250 | marginal (−0.0002/rt) |
| −0.25 | 0.1821 | −11.97 | −9.82 | −39.2 | 0.227 | stable on this grid; continuum above threshold |
| −0.20 | 0.1653 | **−10.57** | −8.28 | −38.8 | 0.227 | stable on grid; **continuum at threshold** |
| −0.15 | 0.1509 | −8.06 | −6.42 | −36.4 | 0.241 | stable |
| −0.10 | 0.1385 | −5.22 | −4.24 | −30.8 | 0.271 | stable |
| −0.05 | 0.1277 | −2.37 | −1.92 | −19.6 | 0.315 | stable |
| −0.02 | 0.1219 | −0.85 | −0.66 | −9.0 | 0.347 | stable |
| −0.01 | 0.1201 | −0.41 | −0.31 | −4.7 | 0.357 | stable |
| 0 | 0.1183 | 0 | 0 | 0 | 0.366 | stable |
| +0.01 | 0.1165 | +0.37 | +0.26 | +5.2 | 0.375 | stable |
| +0.02 | 0.1148 | +0.70 | +0.47 | +10.8 | 0.384 | stable |
| +0.05 | 0.1099 | **+1.42** | +0.68 | +30.2 | 0.401 | stable |
| +0.10 | 0.1025 | +1.02 | −0.95 | +68.7 | 0.382 | stable |
| +0.20 | 0.0900 | −4.39 | −7.47 | +99.5 | 0.253 | stable |
| +0.30 | 0.0798 | −7.28 | −11.28 | +105.3 | 0.203 | stable |

**A.2 — the same at the small-signal drive 2×10⁻³** (N = 240): −0.56 / −1.30 / −3.88 / −8.00 / −11.33 / −13.89 / −15.12 / −12.88 dB at δ = −0.01 / −0.02 / −0.05 / −0.10 / −0.15 / −0.20 / −0.25 / −0.30; +0.34 / +0.42 / −0.67 / −3.88 / −8.41 / −11.04 at +0.01 / +0.02 / +0.05 / +0.10 / +0.20 / +0.30. **A.3 — grids** (pump 0.0197, fixed current): N = 480: −10.10 / −5.32 / −2.41 / +1.43 / +1.65 / −4.70 dB at δ = −0.20 / −0.10 / −0.05 / +0.05 / +0.10 / +0.20 (−0.30: −2.95 dB — an **oscillator row**, base growth +0.0186/rt); N = 720: −9.61 / −5.34 / +1.84 at −0.20 / −0.10 / +0.10. **A.4 — fixed drift (field), N = 240, pump 0.0197**: −14.59 / −12.54 / −10.30 / −7.83 / −5.14 / −2.40 / −0.89 / −0.43 dB at δ = −0.30 … −0.01; +0.40 / +0.78 / +1.71 / **+2.25** / −3.51 / −6.68 at +0.01 / +0.02 / +0.05 / +0.10 / +0.20 / +0.30 (base stable at every δ: −0.093/rt at −0.30). **A.5 — tuning and leg** (fixed current, N = 240, pump 0.0197): shipped L = 582.80 nm: −10.62 / −10.34 / −5.31 / −2.51 / +1.74 / +2.25 / −2.53 at δ = −0.30 / −0.20 / −0.10 / −0.05 / +0.05 / +0.10 / +0.20; analytic leg M = 0.102958: −14.16 / −9.90 / −4.62 / −2.01 / +0.97 / −0.04 / −4.40 at the same δ.

**A.6 — what Table A says, operationally (sharpness read off the measured curves; on-state = the maximum over base-stable rows, off-state = the minimum; 10/50/90 % points in amplitude on the depletion side):**

| series | on at δ | off at δ (dB vs δ = 0) | on/off (dB) | δ₁₀ / δ₅₀ / δ₉₀ | **Δn (10–90 %)** | **n_th** |
|---|---|---|---|---|---|---|
| fixed current, N = 240, pump, rows to −0.20 (continuum at threshold; grid-stable) | +0.05 | −0.20 (−10.57) | −12.0 | −0.155 / −0.056 / +0.022 | **0.18** | −0.056 |
| fixed current, N = 240, pump, rows to −0.25 (grid-stable) | +0.05 | −0.25 (−11.97) | −13.4 | −0.176 / −0.061 / +0.020 | 0.20 | −0.061 |
| fixed current, N = 480, pump, rows to −0.20 | +0.10 | −0.20 (−10.10) | −11.8 | −0.161 / −0.049 / +0.034 | 0.19 | −0.049 |
| fixed current, N = 240, 2×10⁻³ | +0.02 | −0.25 (−15.12) | −15.5 | −0.156 / −0.056 / −0.006 | 0.15 | −0.056 |
| fixed drift, N = 240, pump | +0.10 | −0.30 (−14.59) | −16.8 | −0.206 / −0.054 / +0.042 | **0.25** | −0.054 |
| fixed drift, N = 240, 2×10⁻³ | 0 | −0.20 (−13.78) | −13.8 | −0.159 / −0.066 / −0.013 | 0.15 | −0.066 |
| shipped tuning, fixed current, N = 240, pump | +0.10 | −0.30 (−10.62) | −12.9 | −0.162 / −0.041 / +0.044 | 0.21 | −0.041 |
| analytic leg, fixed current, N = 240, pump | +0.05 | −0.30 (−14.16) | −15.1 | −0.226 / −0.083 / +0.011 | 0.24 | −0.083 |

**Lattice scope of the widths (round 3).** On-state and off-state are the extrema of each scan, so the 10–90 % widths depend on where a stable scan stops: at fixed drift the transfer keeps falling with no plateau (−14.6 / −18.3 / −21.6 dB at −0.30 / −0.40 / −0.50, every base stable at −0.093 … −0.095 per round trip) and the width grows 0.20 / 0.25 / 0.29 / 0.32 for scans ending at −0.20 / −0.30 / −0.40 / −0.50 (one seat's construction, the −0.40 / −0.50 rows reproduced). The registered width is therefore **pinned to the scan ending at the 10-dB depletion, δ_off = −0.20** (rows 1 and 3 of the table: 0.18 / 0.19; fixed drift on the same pin 0.20; small signal 0.15), and the wider readings are lattice results of their own scans. **Sign and shape.** g(δ) is a **resonance curve**, not a sigmoid: the retuned cell at δ = 0 sits with its line centre (continuum 0.24542) 0.8 % below the carrier (0.24735), so a small density *rise* pulls the line onto the carrier (+0.37 dB per +1 %, peak +1.4 … +2.3 dB at +5 … +10 %) and a density *drop* detunes it (−0.41 dB per −1 %), with the fixed-current drift rising toward threshold on the depletion side (A.1 phase −39°, M′ → 0.165). There is no plateau on either side; the largest extinction within the base-stable domain is **10.1–10.6 dB at δ = −0.20 by the cav observable (fixed current, where the continuum cell is at its threshold; the drain-velocity observable reads −8.3 / −8.9 / −9.1 at N = 240 / 480 / 720 and crosses 10 dB only at ≈ −0.26 / −0.22 on N = 240 / 480 — at N = 720 the −0.25 row is an oscillator row, cav −6.67 with the drain velocity at −10.62, so the drain-velocity crossing there is unbracketed on a base-stable row) and 14.6 dB at δ = −0.30 (fixed drift, detuning alone)**; the fixed-drift δ = +0.10 on-state (0.432) and the fixed-current enhancement peaks (0.40–0.43) sit at or just above the velocity ceiling 0.429 — flagged. **What limits it:** on the depletion side at fixed current, M nearing threshold (the base self-oscillates at δ = −0.30 on N = 480; the continuum does at −0.20); at fixed drift, detuning (the line walks off the carrier, phase −35 … −38°); on the enhancement side, detuning past the line centre (+100 … +114° at +0.20 … +0.30). The velocity domain (10-08 limitation 10, max|hu/h| ≤ 0.429) is never left on the depletion side at the pump (0.23–0.36) and only at the enhancement peak (0.40–0.43 at δ = +0.05 … +0.10). Read as Eq. (5)'s parameters — whose Δn is the tanh width, 1/2.197 of the 10–90 % width — the released cell's own g has **a 10–90 % width of 0.15–0.20·n at the pump on the pinned construction (off-state at δ_off = −0.20; 0.14–0.22 over every stored series, the wider readings of deeper scans being lattice results of their own scans) (Δn = 0.07–0.09·n), n_th = −0.04 … −0.07 below the operating density, and the enhancing sign for a density rise** — so an input that *raises* the density is an enhancing coupling and one that lowers it is depleting; which the input does is §4's question.
## 4. Table B — the coupling routes, each gated (`inv_rect_v2.py`, `inv_fieldsum.py`, `inv_osc.py`, `inv_burstcheck.py`; retuned configuration, absolute leg, N = 240 unless stated)

**B.1 — Route (i): the literal β — rectification of the input inside the cell** (*demonstrated* on the released cell; the mechanism is §2.2's second-order DC response, now with drift and gain). DC drain-density shift ⟨h(1)⟩ − 1 and spatial mean ⟨h⟩ − 1 over an integer number of carrier periods of the second half (the whole-period instrument; §8 item 2):

| level (10-08 / 08-01) | a | ⟨h(1)⟩ − 1 | β_drain = shift/a | spatial mean | β_spatial | max\|hu/h\| |
|---|---|---|---|---|---|---|
| knee bottom | 0.0076 | +0.00448 | +0.59 | +0.00216 | +0.28 | 0.253 |
| `A_fix` band bottom | 0.0084 | +0.00528 | +0.63 (N = 480: +0.83) | +0.00254 | +0.30 | 0.264 |
| knee top | 0.0115 | +0.00851 | +0.74 | +0.00409 | +0.36 | 0.300 |
| `A_fix` | 0.0140 | +0.01114 | +0.80 (480: +0.98) | +0.00534 | +0.38 | 0.324 |
| F = 2 band bottom | 0.0170 | +0.01422 | +0.84 | +0.00680 | +0.40 | 0.348 |
| **F = 2 central '1'** | **0.0197** | **+0.01688** | **+0.86 (480: +1.00; 720: +1.06)** | **+0.00805** | **+0.41 (480: 0.48; 720: 0.50)** | 0.366 |
| F = 2 band top | 0.0269 | +0.02337 | +0.87 (480: +0.98) | +0.01107 | +0.41 | 0.407 |
| above the domain | 0.0360 | +0.03047 | +0.85 | +0.01431 | +0.40 | 0.446 |
| shipped tuning, F = 2 | 0.0197 | +0.01360 | +0.69 | +0.00641 | +0.33 | 0.344 |
| analytic leg, F = 2 | 0.0197 | +0.01497 | +0.76 | +0.00725 | +0.37 | 0.336 |
| **unbiased (M = 10⁻⁹), F = 2 swing** | 0.0197 | +0.00384 (480: +0.00419) | +0.195 (0.213) | +0.00199 | +0.10 | 0.124 |

The shift grows as a^p with p falling from 1.63 at the knee to 1.05 across the F = 2 band and 0.91 above it (sub-quadratic: the gain compresses as the drive rises); on the grid ladder the F = 2 value rises 0.0169 → 0.0198 → 0.0209 (N = 240 / 480 / 720); the three rungs fit c_N = c_∞ − K·N^−p with **p = 0.75 and an extrapolant β_drain ≈ 1.22** (first-order Richardson on the two pairs 1.15 / 1.18; the fitted law gives 1.09 at N = 960 and reaches 1.20 only near N ≈ 10⁴; `inv_numerics3.py`). **Sign: positive on every row** — accumulation at the current-clamped drain, as §2.2 derives for M = 0 and the biased cell inherits with a ×4.4 (N = 240) / ×4.7 (N = 480) enhancement over the unbiased cell at the same swing. **Read through Table A (an in-model composition on one plane assumption):** the delivered '1' shifts *this* cell's drain-plane density by +1.7 … +2.1 % and its spatial mean by +0.8 … +1.0 %; taking the drain plane as the next cell's input is 08-02 item 4's assignment ("in-model at best" by its own vote record) and 10-08 limitation 2 says the chain has no cell-to-cell transfer model, so the conversion through g(δ) is in-model on that assumption: **+0.6 … +0.7 dB (drain plane) or +0.3 dB (spatial mean) of gain on the pump — an enhancing coupling**; the same magnitudes wired to deplete would give −0.7 … −0.9 and −0.3 dB. Operational sharpness **k_op = (shift over the full delivered swing) / (10–90 % width) = 0.0169–0.0209 / 0.18–0.20 (the pinned pump-row widths, A.6) = 0.08–0.12 (0.095 / 0.102 / 0.095 grid by grid); on Eq. (5)'s tanh scale k = 2.197·k_op = 0.18–0.26**, against Part I §5's k ≥ 5 (operational 2.3) and the designed 8 (operational 3.6). Extinction available from this route at the delivered swing: **none** (wrong sign); at the `A_fix` band 0.0053–0.0111 (k = 0.03–0.06); at the knee 0.0045–0.0085. The swing that would deplete by 0.20: on the measured law's flattest extrapolation (p = 0.91 continued from the 0.036 row) **a ≈ 0.28**, on its steepest (p = 1.63) a ≈ 0.08 continued from the knee rows or 0.11 continued from the 0.036 row — all above the velocity domain (0.024–0.036; 10-08 limitation 10) and the coded rail 0.10: **not reached inside the domain**. The swing for k = 5 on the tanh scale would have to shift the density by 0.35–0.55·n (k = 8: 0.55–0.9·n): not available in any model. *The pump* in this route is the clock burst arriving at the source (clocked regime; the launcher's level, 0.0197 at the F = 2 point); the route is phase-insensitive (rectification), which is its one merit.

**B.2 — Route (i), timing** (*demonstrated*; 07-31's own duty-0.8 launch at 69 GHz — active window 0.8 of the 14.49-ps slot from the slot start, raised-cosine edges of 2 round trips inside it, carrier referenced to the window centre, every slot driven (an **all-'1' train**; the isolated-'1' rows follow) — measured with a leak-free two-period triangular window on the drain density (`inv_rework.py`, duty rows; every slot identical, slot-to-slot spread 0); the first instrument — a hard gate on a free-running carrier read through a one-period box — alternated between two carrier-phase classes and leaked at the gating edges, and is retired, §8 item 2): at the F = 2 swing the rectified shift reads **+0.0031 / +0.0048 / +0.0136 / +0.0190 / +0.0180 at 1.45 / 2.9 / 5.8 / 8.7 / 11.0 ps** into the slot (17 / 27 / 75 / 105 / 100 % of its 11-ps value; the peak is +0.0197 at 9.5 ps; **90 % is first reached at 6.9 ps**, N = 240 and N = 480 alike), then **+0.0176 / +0.0115 / +0.0076 / +0.0045 at 11.6 / 12.5 / 13.5 / 14.4 ps** — a decay constant of **2.6 ps by a log-linear fit over 11.9–14.3 ps (N = 240; 3.0 ps at N = 480; 2.5 at the band top)** — the two-point estimator from the window's close (11.6 → 14.4 ps) gives 2.1 / 2.5 / 2.0 ps and from the 11-ps value 2.45 / 2.96 / 2.36 (`inv_rework2.py`); the key registers the fit — and **+0.0038 at the next slot's start, 21 % of the 11-ps value** (N = 480: +0.0064, 28 %, on an 11-ps value of +0.0225). At the band top 0.0269: 90 % at 5.0 ps, peak +0.0284 at 8.5 ps, decay 2.5 ps (fit), residual 20 %. The unbiased cell: 90 % at 3.1 ps, peak +0.0043, back to zero by 12.5 ps. **An isolated '1'** (five undriven slots before it, the next slot undriven; `inv_rework3.py`): 11-ps value +0.0173 / +0.0215 (N = 240 / 480), 90 % at 6.56 / 6.93 ps, decay fit 2.59 / 3.04 ps, and **+0.0050 / +0.0075 at the start of the following '0' slot — 0.287 / 0.348 of the 11-ps value** (band top: 0.273, t₉₀ 5.15 ps, decay 2.52 ps) — the memory a '1' leaves in a '0' slot, which the all-'1' train understates. Against 10-13's per-cell latency (2.7–4.0 ps by energy centroid) the rectified shift rises more slowly (90 % at 6.9 ps, of order the 07-22 ring-down 5.71 ps) and carries a fifth (all-'1' train) to a third (isolated '1') of itself into the next slot, a memory the released ISI models (`cell.isi_spread_dB`: a 30 % depletion recovering with τ) do not describe — there the depletion is a parameter; here it is +1.8 % and accumulating.

**B.3 — Route (ii): the coherent field sum** (*demonstrated*; two source tones at the carrier, pump = the delivered '1' 0.0197, output = per-slot peak of `cav` relative to the pump alone; drain lock-in amplitude in parentheses):

| NOT by cancellation: input in antiphase, phase error | 0° | 5° | 10° | 15° | 20° | 30° | 45° | 90° | 180° (in phase) |
|---|---|---|---|---|---|---|---|---|---|
| output vs pump, N = 240 (dB) | −290 (the floating-point residual of π) | **−17.6** (−18.2) | **−11.7** (−12.3); 11°: −10.9, 12°: **−10.2**, 13°: **−9.6** | **−8.4** (−9.0) | −6.3 (−6.8) | −3.5 (−3.9) | −1.3 (−1.5) | +1.5 (+1.7) | +2.9 (+3.3) |
| N = 480 | −290 | — | **−10.5** (−11.3); 12°: **−9.1** | **−7.4** (−8.1) | — | −3.1 (−3.5) | — | — | — |
| input residual \|1 − e^{iφ}\| (dB) | −∞ | −21.2 | −15.2 | −11.7 | −9.2 | −5.7 | −2.3 | +3.0 | +6.0 |

| amplitude mismatch at 0° phase error | 0.78 | 0.80 | 0.90 | 1.10 | 1.20 | 1.22 | 1.25 |
|---|---|---|---|---|---|---|---|
| output vs pump (dB) | −9.8 (−10.4) | **−10.6** (−11.1) | −16.4 (−17.0) | −16.4 (−17.0) | **−10.6** | −9.8 (−10.4) | −8.8 (−9.3) |

The 10-dB window is **≤ 12.3° of phase error at matched amplitude on N = 240 (bracketed by the direct 12° / 13° rows), ≤ 10.7° on N = 480 (10° / 12°) and ≤ 10.1° on N = 720 (10° / 11°: −10.05 / −9.32 dB) — it tightens under refinement and its continuum value is open below 10° — and −21 % / +21 % of amplitude at zero phase error on N = 240 (bracketed by 0.78 / 0.80 and 1.20 / 1.22: r and 2 − r are the same residual tone, so 1.20 reads −10.56 dB like 0.80), ±17.6 % on N = 720 (0.82 reads −9.80 dB)**; the output extinction is **0.62–0.83 of the input extinction in dB** (the cell's sub-linear transfer lifts the residual: out ∝ A^0.72 between 0.005 and 0.0197). Operational sharpness of the inverter transfer (output against the input amplitude at fixed pump, V-shaped through zero at A_in = A_pump), measured directly with single tones at the residual amplitudes (`inv_rework2.py`; the transfer is linear below 0.003, exponent 0.997): the 10 % output point is at a residual of 0.00130 (input 0.01840) and the 90 % point at 0.01629 (input 0.00341), so Δ(10–90) = 0.0150 over the 0.0197 swing, **k_op = 1.31 (N = 240) / 1.33 (N = 480); 2.9 on Eq. (5)'s tanh scale** — an input error propagates almost linearly to the output, and an input above the pump turns the output back on with inverted carrier phase. *The pump:* a clock burst of the input's own amplitude, **coherent with it** — launched from the same comb reference and arriving with its phase held to within 10.1–12.3° (by grid, tightening under refinement) *after* the input's own path, against 10-13's 12–21° per 1 % of detuning at every upstream cell and Part I's ±15° budget (which alone leaves −7.4 … −8.4 dB). Timing: the cancellation is linear superposition at the source plane (no rise of its own); the cell's latency (10-13: 2.7–4.0 ps per cell) and ring-down apply unchanged.

**AND/OR by the sum of two input fields** (*demonstrated*, same instrument): '1' + '1' against '1' alone: **+2.86 dB (cav) / +3.28 dB (drain) in phase**, +2.83 / +3.24 at 15° relative phase, +2.73 / +3.13 at 30°, +2.31 / +2.65 at 60°, +1.50 / +1.72 at 90°. The single-tone transfer over 0 → 2 × 0.0197: output 0.370 / 0.656 / 0.857 / 1 / 1.129 / 1.230 / 1.390 / 1.541 of the '1' at 0.005 / 0.010 / 0.015 / 0.0197 / 0.025 / 0.030 / 0.0394 / 0.050 (local exponents 0.72 below the '1', 0.48 above it; the 0.050 row is outside the velocity domain, 0.493). The '1 + 1' rows run at max|hu/h| = 0.458 / 0.457 / 0.453 / 0.438 (0°–60°; 0.468 / 0.471 at N = 480 / 720), above the velocity ceiling 0.429 (the 90° row, 0.411, is inside): the separation is the released model's reading at the edge of its physical domain, flagged. On the finer grids the in-phase separation is **+2.65 / +2.97 dB (N = 480) and +2.59 / +2.86 dB (N = 720)** (cav / drain), so the headline band is 2.6–3.3 dB across the three grids; the concavity behind it is 10-08 item 4's promoted law — no plateau, `rail_sweep_output_slope` = 0.39–0.60 — read at one drive doubling (2^0.39…0.60 = 2.3–3.6 dB). A threshold AND would need out(2A)/out(A) ≥ 3.16 for 10 dB and a convex transfer; the released cell is concave at every level (local exponents 0.83 → 0.43 across every adjacent pair), so the **'1 + 1' / '1 + 0' separation is 2.6–3.3 dB** — an OR with no margin, not an AND. Read as a threshold element with the two-input swing 0 → 0.0394 as its input swing, the 10 % and 90 % output points (0.139 and 1.251 of the '1') sit at A = 0.0018 (direct brackets 0.0014 / 0.002, and a direct row at 0.0018 reading 0.1385 of the '1'; `inv_rework3.py`) and ≈ 0.0312 (0.030 / 0.0394), so Δ(10–90) = 0.0294 and the operational **k = 1.34** (2.9 on the tanh scale; ≈ 0.7 if the swing is one '1'); the load-bearing statement is the concavity, not the k. **The butterfly margin the prompt asked for.** The released construction NM = ½(1 − 2/k)(1 − 10^(−ext/20)) is written on Eq. (5)'s tanh scale: at the interferometric NOT's k = 2.9 it returns +0.10 and at the two-input sum's 2.9 and 2.6–3.3 dB +0.04 … +0.05 (it is negative only for rectification, k = 0.15–0.26: −3.1). Built on the measured inverter transfer itself (`inv_butterfly.py`: f(u) = T(|1 − u·e^{iφ}|·A)/T(A) with T the measured single-tone output, the pair f∘f, its attracting 2-cycle as the rails, the largest square in the lobe between the rails — *in-model*: the pair feeds the fraction of T(A) one cell emits as the same fraction of A into the next, which is 10-08's F = 2 unity normalisation and 08-01's cell-to-cell assumption; 10-08 limitation 2 records that the chain has no cell-to-cell transfer model, and no two-cell run exists), the margin on N = 240 is **≈ 0.010 of the swing at perfect phase, 0.007 at 2.5°, 0.003 at 5°, and 0 from 7.5° on: on direct two-tone rows (`inv_rework4.py`, u = 0.55 / 0.575 / 0.60 of the pump in antiphase + 7.5°: f = 0.610 / 0.585 / 0.560) the 7.5° pair has a single attracting fixed point at u* = 0.580 with slope −0.99 — monostable, no rails** (the listing's 7.5° "rails" and its 5° rails 0.339 ↔ 0.782 were artifacts of its log-log interpolant between rows 0.0075 and 0.010 and are **withdrawn**; one seat's direct 5° rails are 0.28 ↔ 0.83). One seat's finer transfer tables give 0.005 / 0.003 at perfect phase on N = 480 / 720 with the fixed-point slope approaching −1, so the margin halves with each refinement and **whether any bistability survives the continuum is open**; the key that registered this margin is withdrawn at the cap (§7). Against the 0.26 that `K_SHARP` = 8 promises at 10 dB, the interferometric inverter is at best marginally restoring on the coarsest grid; the field-sum AND, with 2.6–3.3 dB of separation, has no threshold to restore to. (A low-threshold OR "fires on either" trivially; it, too, is not re-clamped.)

**B.4 — Route (iii): the gate segment — an external detector rectifies the input and its DC voltage shifts the cell's gate** (*in-model*: Part I §5's "through a gate segment" read literally; the detector segment is a second released cell, passive or biased, whose §2.2 response is the measured ⟨h(1)⟩ − 1 of B.1; a gated sheet converts a channel-potential rise into a density change of the same relative size; the wiring sets the sign). Available DC per unit swing: **0.19–0.23 (unbiased detector; 11.9·a) or 0.86–1.06 (a detector biased like the cell)**, i.e. +0.38 … +0.46 % or +1.7 … +2.1 % of the density at the F = 2 swing. Applied depleting (sign by wiring) to the cell, Table A gives **−0.1 … −0.2 dB (unbiased) or −0.7 … −0.9 dB (biased)** — the same operational sharpness as route (i) (0.08–0.12 behind a biased detector, 0.019–0.024 behind an unbiased one; 0.18–0.26 / 0.04–0.05 on the tanh scale). To reach −20 % the segment needs an **electrical gain of ×9–12 (biased detector) or ×43–52 (unbiased)** between its drain and the cell's gate — a transimpedance stage that is not in any Part — or the 0.08–0.28 swings of B.1. Timing: the detector's own rise and decay are B.2's (90 % at 6.9 ps biased, 3.1 ps unbiased; 2.0–3.0 ps decay by estimator; 21–28 % next-slot residual) plus the gate's RC, which the released chain does not model (open). *The pump:* the clock burst at the source, phase-insensitive to the input.

**B.5 — Route (iv): the cell as its own pump — biased above threshold, quenched by the input?** (*demonstrated*; retuned, 240 round trips = 119 ps, per-slot peak of `cav` over the last quarter): free oscillation at 1.05 / 1.10 / 1.20 × `M_th_num` (N = 240, 240 round trips): 0.0010 / 0.0329 / 0.3823 — the first two are **transients** (longer records, `inv_rework.py`: at 1.10 the limit cycle is 0.318, reached after ≈ 300 round trips; at 1.05 it is 0.262, after ≈ 500); the 1.20 row saturates with a run-wide density trough of 0.574 and a rectified drain shift of +0.031 of its own); with the delivered '1' injected at the carrier the output is **quasi-periodic, not steady** (60-round-trip windows, `inv_rework4.py`): at 1.05 steady at 0.241 (−0.7 dB); at 1.10 wandering 0.239–0.275 (mean −2.0 dB; a round-3 seat's 720-round-trip record, reproduced by two round-4 seats — no session listing prints it); at 1.20 wandering 0.360–0.382 (**mean −0.3 dB**, range −0.5 … 0.0); N = 480 at 1.10·`M_th_num`(240) — 1.17 of that grid's own threshold — on a 960-round-trip record: free limit cycle **0.360** (the 240-round-trip reading 0.3400 was still building), injected 0.303–0.378 (**mean −0.7 dB**, range −1.5 … +0.4), the carrier-locked drain component rising from 0.0085 to 0.0296. Every injected row and the 1.20 free row run at max|hu/h| = 0.41–0.62, above the velocity ceiling: released-model readings outside the physical domain, flagged. The input pulls and partially locks the oscillator; it does not turn it off. Rectification raises the drain density (+0.011 … +0.018), which at fixed current *lowers* M′ by 1.6–2.6 % — the right sign for a quench but 3–10× short of the 5–20 % above-threshold margins run here (17 % above N = 480's own threshold at 1.10·`M_th_num`), and those take 150–250 ps to build. **No NOT; and no timing-compatible pump** (an oscillator biased close enough to threshold to be quenched by +2 % of density is one whose build-up takes tens of slots).

## 5. The NOT and AND verdicts, and what an inverting cell would need

**Part I Table 4's NOT column (§6.5, "NOT (inverting bias)"; §5's "inversion as a bias choice") does not exist in-model at the delivered swing by any density route the released cell contains.** The three statements that decide it are independent and each is executed above: (a) the only density coupling in the released equations is rectification, whose sign is enhancing (B.1, §2.2) and whose magnitude gives k = 0.18–0.26 on Eq. (5)'s scale (operational 0.08–0.12); (b) a depleting gate coupling is an external electrical element needing ×9–52 of gain or swings above the velocity domain (B.4); (c) the cell biased as its own pump is not quenched (B.5). What the record's cell *does* supply is a **wire-level inverter by destructive interference (B.3)** — it exists in-model, with **≥ 10 dB only inside a 10.1–12.3° phase window (by grid, tightening under refinement) and a ±21 % (N = 240) / ±17.6 % (N = 720) amplitude window, tightening under refinement, k = 1.3 (2.9 on the tanh scale), a restoring margin of at most ≈ 0.01 of the swing at perfect phase on the coarsest grid and none from 7.5° (open in the continuum), and a compression that worsens, not improves, the residual**. That is not Eq. (5)'s NOT (no n_local moves) and it fails Part I §5's own regeneration condition. **A threshold AND does not exist in-model**: the field sum is concave at every level (k ≈ 1.3, 2.6–3.3 dB of separation on N = 240 / 480 / 720).

**What an inverting cell needs that the record does not supply — the smallest change per route, priced, none claimed to work:**
- *Route (iii):* an electrical gain stage of **×9–12** between a biased detector segment and the inverting cell's gate (×43–52 behind an unbiased one), delivering a −0.17 … −0.28·n gate swing (×8–17 behind a biased detector, ×37–73 behind an unbiased one, for the whole band; ×9–12 / ×43–52 for −0.20·n) within ≈ 7 ps and recovering within the 2.9-ps gap — Part I §9.6's photoconductive tap already does this for the clock (an external, non-plasmonic bias swing across n_th), and Table A prices what it must deliver: −0.17 … −0.28·n for 10 dB where it is reached — on the drain density under either convention, and on the intracavity and drain-velocity observables under the relative swing or at fixed drift; at fixed drain current with the input amplitude held no depletion gives 10 dB on the intracavity or drain-velocity observable (§3), so there the route is read on the drain density (−0.20·n) — −0.30·n for 11.5–14.6 dB at fixed drift (at fixed current −0.20·n is the absolute leg's threshold and −0.30·n G1's pin's). The gate's RC and the 21–35 % next-slot memory of the rectified shift (B.2; a fifth in an all-'1' train, a third after an isolated '1') are the open costs.
- *Route (ii):* a per-inverter phase budget of **≤ 12.3° / 10.7° / 10.1° (N = 240 / 480 / 720, tightening under refinement) between the clock pulse and the input at the source plane** (tighter than Part I §3.2's ±15°, which by 10-13 is already spent 12–21° per 1 % of detuning at each upstream cell) and an amplitude match of **±21 % (N = 240) / ±17.6 % (N = 720), tightening under refinement** — i.e. the launcher must re-time and re-level the pump at every inverter, which is the re-sync station's job, and the inverter then inherits the station's latency.
- *A swing:* **0.08–0.28** of the density at the input, outside the velocity domain and the coded rail — not an available change.
- *An encoding:* a dual-rail lane needs no inverter (NOT is a wire swap) and would remove the 783 inverting cells 10-13 counts in Part III's lane at the cost of carrying every signal with its complement and complementing every gate; that count on the released `digital_lane_bonsai.py` was **not run here** (it is a netlist check, not physics) and is the one change on this list the record can price without new physics.

## 6. Grades (each confirmed / qualified / contradicted / not reached, with the executed reason)

| claim | grade | reason (section) |
|---|---|---|
| Part I §5: the NOT, the k ≥ 8 regeneration and the threshold AND are "established within the model chain of Section 7" | **contradicted** (in-model, released chain) | the chain never computes β, Δn, n_th or the pump; executed, its only input coupling is rectification with the enhancing sign and k = 0.18–0.26 on Eq. (5)'s scale (operational 0.08–0.12) (B.1), its field sum has k ≈ 1.3 operational (2.9) and 2.6–3.3 dB on N = 240 / 480 / 720 (B.3), and its own g(n) has a 10–90 % width of 0.15–0.20·n at the pump on the pinned construction (Δn = 0.07–0.09·n) (A.6) |
| Part I §5: "inversion as a bias choice" | **contradicted for a plasmonic input; qualified for an external bias swing** | no depleting coupling exists in the released cell; a bias swing of −0.20·n gives ≥ 10 dB on the drain density at fixed current under either drive convention (−11.9 / −10.1 dB, relative / absolute) and at fixed drift under the relative swing (−11.6; −9.7 absolute), and on the intracavity observable under the relative swing (−10.6 / −10.3 dB, fixed current / fixed drift); the drain velocity reads −6.4 … −9.9 dB at −0.20 under every mode and convention and crosses 10 dB only at ≈ −0.20 … −0.28 where it crosses at all (Table A, §3) — under a held-amplitude input at fixed drain current it gives 8.7 dB (cav) / 6.4 dB (drain velocity) and no depletion reaches 10 dB on those observables (Table A, §3) — and it must come from an electrical gate stage (×8–73) or the optical tap of §9.6, not from a logic input (B.4) |
| `cell.py`: K_SHARP = 8, DN = 1/8, N_TH = 0.5 as the released cell's transfer | **contradicted** | the released cell's own transfer has a 10–90 % width of 0.15–0.20·n at the pump on the pinned construction (Δn = 0.07–0.09·n on the tanh scale) and n_th = −0.04 … −0.07·n (A.6); with the measured coupling the sharpness at the delivered swing is 0.18–0.26 on the tanh scale (operational 0.08–0.12), not 8 (operational 3.6); `cell.transfer` (A_in prefactor, 08-02 lim. 1d) stands uncalled |
| `disorder.py`: β·A_swing = n | **contradicted** | the induced shift at the full delivered swing is 0.017–0.022·n (B.1); 07-15 limitation 2's alternative β·A_swing ≈ 0.1·n is itself 5× too large; the Appendix-A yield rule's premise is 50× off |
| 07-21: `fanout_max_disorder_regen_floor` = 2 through k₀ = 8 | **qualified** (premise not a property of the released cell) | k_eff = 8·F^−½ inherits k₀ = 8 from `cell.py`, which the released cell does not deliver (0.18–0.26 on the same scale for a density coupling); the F = 2 result that rests on the gain ledger (07-20/07-21's margin) is untouched; the disorder-floor derivation applies to no released cell |
| 08-02: `clockpumped_inverter_residual_band_dB` — does a released-code route now fix A_c? | **not reached** (no released route fixes A_c; the key stays in-model on its reconstructed map) | the cell cannot pump itself (B.5), so A_c is the launcher's level (0.0197 at the F = 2 point), a cascade parameter, not a cell constant; the inverter that map describes has no released mechanism behind it |
| 10-13 item 6 (C′): are Part III's 783 inverting cells pump-fed? | **qualified** | wherever an in-model inverter exists it is pump-fed by the clock burst — route (ii)'s pump is a comb-referenced clock pulse, which an empty input passes on, and route (iii)'s is the same burst — so (C′)'s comb-reference premise holds; what does not exist is an Eq. (5) inverter working by n_local (B.1, B.5), and route (ii) adds a per-inverter input-to-pump window of 10.1–12.3° (by grid) that (C′)'s count of inverter outputs as fresh references does not carry (10-13's Table D (C′) rows are priced on ±15°) |
| 10-13 item 7: the regime fork (clocked / cascaded) and the reading (field sum / envelope); its ±59° / ±84° field-sum tolerance | **qualified** | a cascaded datapath with no clock fed in has no inverter (the cell is not a source); wherever a clock is fed in the inverter is route (ii) or (iii); the reading fork's field-sum branch has no in-model threshold AND (2.6–3.3 dB), and the ±59° / ±84° tolerance is charged against `cell.static_noise_margin` = 0.2564 at k = 8, a margin no released route supplies — the released field sum's phase dependence is B.3's (+2.86 → +1.50 dB from 0° to 90°) |
| 10-08 item 7 / Table 2: the ×4.83 of its ×25.7 decision-mechanism cost assigned to the k = 8 / 10-dB margin fraction 0.2564 | **qualified** | the A0 law's 0.2564 margin fraction is the decision law's design rule, not a property of the released cell, whose measured sharpness is 0.18–0.26 (tanh scale) for a density coupling and 2.9 for the interferometric inverter; the ×4.83 factor is optimistic for the released cell |
| 07-17 limitation 5: the unattributed +0.007 dB expansion at drive ≤ 10⁻³ ("rectification-type boundary nonlinearity") | **qualified** (right sign and right order of magnitude on this estimate; not tested directly) | rectification raises the drain density, and at a 10⁻³ drive the measured shift is +9.4×10⁻⁵·n (drain plane; +4.5×10⁻⁵ spatial; rework rows, exponent 1.98 to 2×10⁻³), which at A.1's slope (+0.37 dB per +1 % cav, +0.26 drain) is **+0.0035 (cav) / +0.0025 (drain) dB** on the drain-plane assumption — within ×2–3 of 07-17's +0.007 dB; the attribution is consistent, not demonstrated |

Part III's lane is a consequence only: its 783 inverters (10-13 (C′)) have no released n_local (Eq. (5)) mechanism; in-model they are route (ii) (pump-fed, phase held to 10.1–12.3° by grid) or route (iii), or the lane goes dual-rail.

## 7. Registered keys (prefix `inv_`; collision-checked: 0 hits in `fable-model-chain/results.json`, `fable-model-quantum/results.json`, every `notes/*.md` and Part III Table TA2) and the bench discriminants

Every key is **in-model on the released Galilean cell**, retuned configuration (576.62 nm), absolute leg 0.118260 unless stated; bands span the grids and legs run; the falsifier names what a re-solve of the released, unedited chain must return to refute it.

| key | value [band] | scope | falsifier |
|---|---|---|---|
| `inv_rect_beta_drain_F2` | **+0.86 [+0.86, +1.06]** | ⟨h(1)⟩ − 1 per unit source swing at 0.0197, N = 240 / 480 / 720 (three-rung fit c_∞ − K·N^−p: p = 0.75, extrapolant ≈ 1.22; first-order Richardson 1.15 / 1.18) | β_drain (the whole-period DC shift per unit swing) at N = 960 outside [+0.95, +1.25], or any negative value |
| `inv_rect_beta_spatial_F2` | **+0.41 [+0.41, +0.50]** | ⟨h⟩ − 1 per unit swing, same rows | outside [+0.45, +0.60] at N ≥ 960 |
| `inv_rect_sign` | **accumulating (+)** | every active and passive row run (0.0076–0.036; both legs; both tunings) | any drive in the domain at which ⟨h(1)⟩ − 1 < 0 |
| `inv_rect_biased_over_passive_F2` | **4.4 [4.4, 4.9]** (absolute leg) / **4.6 [4.56, 4.63]** (ratio leg) | ratio of the DC drain shift, biased over M = 10⁻⁹, same swing 0.0197: absolute leg 0.118260 at N = 240 / 480 / 720 (4.39 / 4.73 / 4.85, first order toward ≈ 5.1 — at N = 480 / 720 that drift is 0.745 / 0.760 of the grid threshold); ratio leg 0.7·`M_th_num`(N) at N = 480 / 720 (4.56 / 4.63; β_drain 0.97 / 1.01) — G1's model-side pin | outside [4.0, 5.5] at N ≥ 960 on either leg |
| `inv_gn_dn_10_90` | **0.18 [0.14, 0.22]** (operational, pinned construction; Eq. (5)'s Δn = this / 2.197 = 0.06–0.10, 0.07–0.09 at the pump) | Table A.6 with the off-state pinned at δ_off = −0.20 (the 10-dB depletion) and the on-state the transfer's maximum, on every stored series (`inv_numerics5.py`): fixed current at the pump 0.18 / 0.19 / 0.22 (N = 240 / 480 / 720, the last on a 0.1-step scan), fixed drift 0.20, small signal 0.14 (N = 240 / 480: 0.138 / 0.136; fixed drift 0.15), shipped tuning 0.20, analytic leg 0.19; scans that run deeper read wider (0.25 / 0.29 / 0.32 at −0.30 / −0.40 / −0.50, lattice results of their own scans) | on the pinned construction, a width < 0.10·n or > 0.25·n on N ≥ 240 |
| `inv_gn_nth` | **−0.056 [−0.068, −0.040]** (pinned construction) | the half-amplitude density on the depletion side of the pinned (δ_off = −0.20) construction, on every stored series (`inv_numerics5.py`): −0.056 / −0.049 / −0.047 fixed current at the pump (N = 240 / 480 / 720), −0.053 / −0.048 small signal, −0.041 fixed drift at the pump, −0.066 fixed drift small signal, −0.040 shipped tuning, −0.068 analytic leg | outside [−0.12, −0.02] on the pinned construction |
| `inv_k_literal_F2` | **0.09 [0.08, 0.12]** (operational, pinned width) / **0.20 [0.18, 0.26]** (Eq. (5)'s tanh scale, × 2.197) | `inv_rect_beta_drain_F2` × 0.0197 / `inv_gn_dn_10_90` (pinned; grid by grid the F = 2 shift 0.0169 / 0.0198 / 0.0209 over the pump-row width 0.18 / 0.19 / 0.22 gives 0.095 / 0.102 / 0.095, and the band spans the pump widths 0.18–0.20 against the shifts 0.0169–0.0209); definition-free, the induced shift +0.017 … +0.021 is 6–12 % of the 10-dB depletion 0.17–0.28; Part I's k ≥ 5 is an operational 2.3 | ≥ 2.3 operational (≥ 5 tanh-scale) by any released coupling at a drive in the domain |
| `inv_depletion_10dB` | **−0.20 [−0.21, −0.19]** (cav, relative swing) | the uniform depletion at which the pump's `cav` output falls 10 dB under the relative-swing convention: fixed current N = 240 / 480 (−0.19 / −0.20) and fixed drift N = 240 (−0.19); the drain-velocity observable crosses at ≈ −0.26 / −0.22 (fixed current, N = 240 / 480; unbracketed on a base-stable row at N = 720) and −0.20 (fixed drift); under an absolute swing the intracavity crossing is between −0.20 and −0.25 at fixed drift, the drain-velocity crossing ≈ −0.28 at fixed drift, and at fixed current neither is reached at any depletion: the cav extinction peaks at 9.5–9.8 dB near −0.25 and falls back toward threshold, and the drain-velocity extinction rises monotonically to only 8.0 / 8.3 dB at −0.30 (N = 240 / 480 at G1's pin) | a cav crossing outside [−0.25, −0.15] on a base-stable relative-swing row, or a fixed-drift absolute-swing crossing outside [−0.30, −0.18] |
| `inv_depletion_10dB_drain_density` | **−0.17 [−0.21, −0.17]** | the same crossing on the drain-DENSITY lock-in (h(1); 08-02 item 4's plane): fixed current −0.17 (relative swing) / −0.20 (absolute, on the absolute leg's continuum-at-threshold row); fixed drift −0.17 / −0.21; N = 240 | a drain-density crossing outside [−0.25, −0.13] on a base-stable row |
| `inv_fixed_current_threshold_depletion` | **−0.20 [−0.21, −0.19]** at the absolute leg (0.118260 = 0.80·M_c, M_c = 0.147679 the retuned continuum threshold); **−0.30 [−0.31, −0.30] at G1's pin (0.7·M_c; analytic leg −0.308)** | the depletion at which the fixed-current cell reaches its own threshold (§2.3; the margin closes as (1 + δ)^−1, δ_th ≈ M/M_c − 1, under either speed law); grid thresholds −0.30 (N = 240, where the absolute leg is the pin; marginal) and in [−0.30, −0.25] (N = 480, where it is 0.745 of the grid threshold) | a continuum root with Im ω ≥ 0 at δ ≥ −0.17 at the absolute leg or ≥ −0.27 at the pin, or a base-stable (free growth < 0) fixed-current row at δ ≤ −0.25 on N ≥ 960 at the absolute leg |
| `inv_fieldsum_not_phase_10dB_deg` | **12.3 / 10.7 / 10.1 (N = 240 / 480 / 720) [10.0, 12.5]** — tightening under refinement; the continuum value is open below 10° | antiphase cancellation, matched amplitude; bracketed by direct rows 12° / 13°, 10° / 12°, 10° / 11° | ≥ 15° or ≤ 8° on N ≥ 480 |
| `inv_fieldsum_not_amp_10dB` | **0.21 (N = 240) / 0.18 (N = 720) [0.17, 0.22]** | amplitude mismatch for 10 dB at zero phase error, both sides (N = 240: between 0.78 and 0.80 and between 1.20 and 1.22 — r and 2 − r are the same residual tone; N = 720: 0.82 reads −9.8 dB, crossing ≈ 0.824); tightening with the phase window | outside [0.15, 0.30] |
| `inv_fieldsum_not_k` | **1.3 [1.3, 1.4]** (operational; 2.9 on the tanh scale) | 0.0197 / Δ(10–90) of the V-shaped transfer, from direct single-tone rows at the residuals 0.0012–0.0014 and 0.0160–0.0166 (N = 240: 1.31; N = 480: 1.33) | ≥ 3 operational |
| `inv_fieldsum_not_snm` | **withdrawn at the cap (round 4)** | the butterfly margin of the interferometric inverter pair is an interpolant- and grid-dependent composition: ≈ 0.010 of the swing at perfect phase on N = 240 (0.007 / 0.003 at 2.5° / 5°; bistability lost between 5° and 7.5° on direct rows), 0.005 / 0.003 on N = 480 / 720 by one seat's tables with bistability lost earlier; what survives is the in-model statement in B.3 — at best marginally restoring on the coarsest grid, open in the continuum | — |
| `inv_fieldsum_and_separation_dB` † | **2.9 [2.5, 3.3]** | '1 + 1' over '1': in phase 2.86 / 2.65 / 2.59 (cav) and 3.28 / 2.97 / 2.86 (drain) at N = 240 / 480 / 720; 2.73 / 3.13 at 30° relative phase (N = 240) — 10-08 item 4's `rail_sweep_output_slope` 0.39–0.60 read at one doubling; † the rows run at max|hu/h| = 0.45–0.47, above the 0.429 ceiling — the released model's reading | ≥ 6 dB on any grid, or a convex transfer anywhere in the domain |
| `inv_rect_rise_90pct_ps` | **6.9 [5.0, 7.0]** | first 90 % of the 11-ps value under 07-31's duty-0.8 launch at 69 GHz, leak-free window: all-'1' train 6.9 at the F = 2 swing (N = 240 / 480), 5.0 at the band top; isolated '1' 6.6 / 6.9 / 5.2 | outside [3, 9] |
| `inv_rect_decay_ps` | **2.6 [1.9, 3.1]** | log-linear fit of the DC drain-density trace over 11.9–14.3 ps after the window closes, all-'1' train (N = 240: 2.57 at 0.0197, 2.51 at 0.0269; N = 480: 3.01; unbiased 1.0) and isolated '1' (2.59 / 3.04 / 2.52); the two-point estimators 11.6 → 14.4 ps give 2.06 / 1.99 / 2.48 and 11.0 → 14.4 ps 2.45 / 2.36 / 2.96 — the band spans the estimators and patterns | outside [1.5, 4] |
| `inv_rect_next_slot_residual` | **0.21 [0.19, 0.35]** | residual at the next slot's start over the 11-ps value: all-'1' train 0.21 / 0.28 / 0.20 (N = 240 / 480 / band top); **isolated '1' → the following '0' slot 0.29 / 0.35 / 0.27** (the ISI-relevant case) | outside [0.1, 0.5] |
| `inv_osc_injection_change_dB` † | **time-means −0.3 … −2.0 dB; excursions [−2.5, +0.4]** | 1.05–1.20·`M_th_num` at N = 240 (free limit cycles 0.262 / 0.318 / 0.382 from 480–1,000-round-trip records; injected outputs steady at 1.05, quasi-periodic at 1.10 / 1.20) and N = 480 at 1.10·`M_th_num`(240) on a 960-round-trip record (free 0.360; injected mean −0.7, range −1.5 … +0.4); † every injected row runs at max|hu/h| = 0.41–0.62, above the ceiling | a quench ≤ −6 dB at any bias with a limit cycle reached inside 8 slots |

**Bench discriminants under G1's pins (bias 0.7 × the device's own measured threshold; the input at the delivered F = 2 level; shapes a measurement must match, not firing falsifiers — 08-01):**
- **D-INV-1 (sign and ratio).** The biased cell's DC drain photoresponse (drain-to-source rectified voltage, or the drain density read capacitively) per input power is **4.4–5 times** the same cell's unbiased response (absolute leg 4.39 / 4.73 on N = 240 / 480, first order toward ≈ 5.1; **on the ratio leg — G1's model-side pin, 0.7·`M_th_num`(N) — 4.56 / 4.63 at N = 480 / 720**), and the **drain potential rises** under drive in both states (accumulation at the current-clamped drain). A biased response that falls, or a ratio below 2 or above 8, refutes the released cell's rectification law at the operating point.
- **D-INV-2 (the gate's Δn).** The output of the biased cell against a top-gate offset applied as a uniform density change: a resonance curve, not a sigmoid, with its peak **+5 … +10 % above the operating density**, a **−0.4 dB per −1 %** slope at the operating point and, at −20 %, **−8.5 … −10.6 dB on the intracavity observable, −6.4 … −8.3 dB on the drain velocity (fixed current; −8.0 … −9.9 at fixed drift) and −10.1 … −11.9 dB on the drain density (fixed current; −9.7 … −11.6 at fixed drift)** (the lower figures if the input amplitude is held, the higher if it scales with the density) — measured at fixed drain current under its own pin (0.7 × the measured threshold) it approaches self-oscillation at ≈ −30 % under a density-independent momentum-relaxation rate (the released law; at the record's absolute leg, 0.80 of threshold, at −20 %), at ≈ −21 % if the rate scales as n^+½ (acoustic phonons; ≈ −14 % at the absolute leg) and beyond −54 % as n^−½ (charged impurities; ≈ −39 % at the absolute leg, `inv_numerics5.py`) — the device value is open on the friction law; at fixed drift the margin is unchanged under a density-independent rate, opens under n^−½ and closes under n^+½ (threshold ≈ −51 % under the pin, −36 % at the absolute leg). **A held-amplitude input at fixed drain current gives a non-monotone extinction on the intracavity (near-field) observable — a peak of 9.5–9.8 dB near −25 % that falls back toward threshold — a monotone drain-velocity extinction that saturates near 8 dB at −30 %, and a drain-density extinction that passes 10 dB at −20 % and keeps falling (−14 dB at −30 %)**: a bench signature of the released model, read on the drain observables as that monotone pair. A sigmoidal transfer with a 10–90 % width below 0.10·n would refute A.6.

## 8. Limitations, open items and the listings

1. **Every result is about the released Galilean shallow-water cell** (10-15: whether graphene's fluid has a threshold at 353 K is open). How graphene's fluid would move each coefficient, *labelled, not substituted*: the record's Eq. (1) speed law has d ln s/d ln n = 0.214 against the solver's √h (0.5), so a uniform density shift detunes the real cell ≈ 2.3× less per unit δ — the 10–90 % width on the detuning side grows to ≈ 0.35–0.46·n (Δn ≈ 0.16–0.21·n; 2.3 × the pinned pump width 0.15–0.20) and k falls further; the fixed-current margin to threshold closes as (1 + δ)^−1 under either speed law (the continuum root crosses zero at δ = −0.2004 under Eq. (1)'s law against −0.2023 under √h at the absolute leg, −0.302 against −0.305 at G1's pin — the threshold depletion does not move) and the fixed-drift margin is constant under either; under 07-22's promoted kinetic threshold `M_th_kinetic_353K` = 0.165 [0.154, 0.169] the absolute drift crosses at −0.28 [−0.23, −0.30] by the small-M law; 10-15's drift law k_d = ½ puts the threshold ×1.7 higher in drift, which would move `inv_fixed_current_threshold_depletion` out of reach of a 20–30 % depletion only if the bias stayed at the Galilean drift — under G1's pin, a ratio to the device's own measured threshold, the crossing stays at ≈ −0.30 only for a density-independent momentum-relaxation rate (the released law, b = 0); under 10-15's friction family 1/τ ∝ n^b the pin's fixed-current crossing is **−0.212 at b = +½** (acoustic phonons and short-range scattering — and the record's own τ(T) is phonon-limited) and **beyond −0.54 at b = −½** (charged impurities, Part I's ref. [19]) — the Eq. (1) law within 0.003 at b = +½ and 0, while at b = −½ only Eq. (1)'s law crosses (−0.543; under √h none to −0.70) (`inv_numerics3.py`) — so the device's threshold depletion is open on the friction law; at fixed drift the margin is unchanged under a density-independent rate, opens under n^−½ and closes as (1 + δ)^−½ under n^+½, reaching threshold at −0.51 under the pin and −0.36 at the absolute leg (`inv_numerics4.py`), so under acoustic-phonon friction the 10-dB depletion sits at 0.77–0.83 of threshold even at fixed drift; the rectified DC response (second order in the drive) depends on the equation of state through the convective term and is not computed for the Dirac fluid here (open). The sign of rectification is positive on every row of the released closure; it is not set by the clamps but by the source's convective momentum flux against the drain's pressure curvature — for a momentum flux α·hu² + P(h) with P′(1) = 1, §2.2's balance gives ⟨η₂⟩(1)/a² = 23.19·α − 11.30·P″ at the shipped carrier (11.89 for the released α = 1, P″ = 1; `inv_numerics3.py`), which changes sign at α* = 0.49·P″ — so for graphene's fluid, whose drag and equation of state 10-15 leaves open, the sign is closure-dependent and open.
2. **Two instrument corrections, disclosed.** *(a)* The first rectification campaign (`inv_rect.py`, v1, 23 runs) read the DC shift as the plain mean over the second half of the record; with a 0.28-amplitude drain oscillation and a non-integer number of carrier periods in that window (29.7 at the retuned tuning) that instrument leaked up to ±0.003 and read 15 % low at the F = 2 point (+0.0146 against +0.0169). Every DC figure in this reply is from v2 (`inv_rect_v2.py`), the mean over an integer number of periods, cross-checked against the lock-in constant term (agreement to 0.0001) and the period-averaged burst instrument (plateau +0.0169–0.0170); the shipped-tuning row, whose 120 round trips are exactly 60 periods, is identical in both instruments (+0.01360), which is the leakage's own signature. Table A's `hd_dc` column was recorded with the v1 instrument and is **not used**; the candidate seat's probe figure "+1.4 %" carried the same bias and is +1.7 % on the corrected instrument. *(b)* The first burst-timing instrument (`inv_rect_v2.py` burst rows, `inv_burstcheck.py`) gated a free-running carrier with a hard window and read the DC through a one-period box: because a slot holds 14.49 carrier periods, successive bursts started 177.5° apart in carrier phase, the box leaked at the gating edges with opposite sign in the two phase classes, and the first draft's rows were a mean over slots of the two classes normalised to an edge-leak spike (0.0268) that no DC exists — both pre-publication check seats found it independently. B.2 and the three timing keys were re-measured on 07-31's own waveform (phase-locked to the window centre, raised-cosine edges) through a two-period triangular window, which cancels the first-order leak and makes every slot identical; the retired rows are left in the listings as printed.
3. **Grids and brackets.** N = 240 is the primary grid (every row), N = 480 at the key rows, N = 720 at five; the DS ladder runs to N = 1,920. No interpolant wider than ×1.5 is used (the NOT's and the AND's 10 % / 90 % points are bracketed by direct single-tone rows, `inv_rework2.py`); the 10-dB crossings are bracketed by direct rows (δ = −0.15 / −0.20 at fixed current and drift under the relative swing, −0.20 / −0.25 at fixed drift under the absolute swing; 12° / 13° and 10° / 12°, 0.78 / 0.80 and 1.20 / 1.22 for the interferometric inverter). The N = 720 fixed-current drain-velocity crossing is unbracketed on a base-stable row (the −0.25 row self-oscillates). The ring-down estimator of G5b was replaced by the discrete operator's spectrum and its output is left in the listings as superseded.
4. **A uniform δ is a gate covering the whole cell;** a partial-length gate segment (Part I §5's wording) was not run — its response is between the drain-plane and spatial-mean readings of B.1 at best. The gate's RC, the kinetic contact layers (07-13 §6, 07-18) and the DC base state as 07-13 §6 imposes it stay open.
5. **The DS-1996 primary text** was not accessible; the closed form of §2.2 is this session's derivation from the released equations and matches the candidate seat's recalled form to 3.6×10⁻¹¹. Attribution to Dyakonov & Shur (1996) rests on secondary citations.
6. **No multi-cell cascade and no coupled-cell coupling was run**; the two-tone source is one cell's input plane (the prompt's unidirectional coupling: at zero second tone it is the released single cell bit-equal, G1b). The dual-rail netlist count was not run.
7. **Run count:** 335 released-solver-class runs (G1 18 at ≤ 20 round trips; G2 4 at 240; G3 4 at 160; G5b 8 superseded free runs of 60; Table A 86 driven + 10 free of 80; rectification 23 v1 superseded + 26 v2; field sum 30; oscillator 9; burst check 2; the post-check rework 40, including references; the round-2 rework 44; the round-3 rework 5; the round-4 rework 26), ≈ 38 min of wall time on 6 cores; the prompt's guideline was ≲ 150.
8. **Withdrawn at the cap (round 4), a scope reduction:** the "tristable at 7.5°" statement and every rails figure of the butterfly listing (interpolant artifacts; on direct rows the 7.5° pair is monostable); the registered key `inv_fieldsum_not_snm` (the margin is interpolant- and grid-dependent and open in the continuum); the "steady" oscillator readings at 1.10 / 1.20·`M_th_num` and the 240-round-trip N = 480 reading (replaced by window means and ranges from long records); the unpinned width construction behind `inv_gn_dn_10_90`, `inv_gn_nth` and `inv_k_literal_F2` (pinned to δ_off = −0.20); the universal "10 dB costs −0.17 … −0.28·n by observable, bias mode and convention" (scoped: at fixed current under a held-amplitude input the velocity observables never reach 10 dB); the fixed-drift universal "does not approach threshold under any friction law" (false for n^+½). Nothing else of the verdict moves.
9. **Open:** whether a partial gate segment or a shorter detector segment changes β's magnitude; the Dirac-fluid rectification coefficient; the gate RC; the 783-inverter dual-rail count; whether a re-sync station's optical tap (Part I §9.6) can double as a route-(iii) inverter stage within the slot.

**Runnable listings** (posted in the next comments, verbatim with their printed outputs; run from the repository root as `PYTHONDONTWRITEBYTECODE=1 python3 -B <file>`): `inv_common.py` (runner, statistics, platform), `inv_ds1996.py` (§2.2), `inv_gates.py` (G1), `inv_gates2.py` (G2, G3, G5; G5b superseded), `inv_linop.py` (G5 spectrum), `inv_tableA.py` (§3), `inv_rect_v2.py` (B.1, B.2; v1 listed as superseded), `inv_burstcheck.py` (B.2 cross-check), `inv_fieldsum.py` (B.3), `inv_osc.py` (B.5), `inv_rework.py` (the post-check rows: absolute-swing Table A, the direct phase / amplitude brackets, the long oscillator records, the small-drive rows, the 07-31-waveform burst timing), `inv_tabulate.py` (prints every table of this reply from the campaign files), and the round-2 listings `inv_numerics2.py` (the continuum threshold by bias leg; the tanh mapping), `inv_rework2.py` (the drain-density observable, the direct NOT / AND brackets, the ratio-leg rectification, the AND grids, the decay estimators) and `inv_butterfly.py` (the measured-curve butterfly); the round-3 listings `inv_numerics3.py` (the friction family at G1's pin; the ladder fit; the 7.5° fixed points on the interpolant — superseded by the direct rows; the sign coefficients), `inv_rework3.py` (the isolated-'1' rows, the 0.0018 tone, the N = 720 band top), and the round-4 listings `inv_numerics4.py` (the friction family at fixed drift) and `inv_rework4.py` (the N = 720 windows, the 7.5° direct two-tone map, the held-amplitude fixed-current rows beyond −0.25, the fixed-drift scan to −0.50, the oscillator records in 60-round-trip windows).

---

## Agent assessment — 2026-10-17

Promoted **by maintainer direction** after the round-4 cap; the crew voted 3-of-3 to store in every round and never clean (6 / 5 / 5, 4 / 6 / 3, 2 / 4 / 4, 2 / 3 / 2 required edits). Earlier rounds are permanent on [discussion #137](https://github.com/ryoji-info/FableComputer/discussions/137) — round 1 (https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18974799), round 2 (https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18975588), round 3 (https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18976398). The three round-4 verdicts and the tally follow verbatim.

*Model: `claude-opus-5-5` (Claude Opus 5.5). Requested as the `opus` alias; this seat ran as `claude-opus-5-5`.*

**Agent re-assessment (rework round 4, the cap) — 2026-10-17 — round 4 — 🧵 Fabric: STORE (2 required edits)**

*Model line: `claude-opus-5-5`. Fresh, blind round-4 re-assessor seat for Fable Session #137; it shares no context with the drafting, the execution, the check seats, the round-1 to round-3 assessors or the other round-4 seats. Assessed: the round-4 reply as posted (discussioncomment-18976536 / -18976538; local `reply-r4.md`, which equals the two local part files apart from the continuation lines), listings 1–5, the round-4 record (-18976535) and the erratum (-18976555). Read in full and in order before it: the winning prompt, the three round-1 verdicts and tally, the round-2 record and verdicts, the round-3 record and verdicts, and the round-3 tally. Conditions: released chain at `39c61a4`, imported read-only, `git status --short` empty before, during and after; Darwin arm64 / Python 3.11.2 / numpy 2.4.6. Runs: **60 released-solver-class runs** — 58 on this seat's own loop (`fr4_common.sim`, written from `solver.py`; it imports only the released `_step_LF`, `constants` and `ds_cell`, and uses neither the session's `inv_common` nor its JSON) and 2 `solver.run` references for G1 — plus pure numerics. Never run: `run_all.py`, `figures.py`, or any registered `inv_` falsifier as a test (the brief's N = 720 window, depletion and oscillator rows fall inside the domains of three falsifiers; none fires).*

**Gates I ran** (scripts and printed outputs in this seat's directory; run from the repository root as `PYTHONDONTWRITEBYTECODE=1 python3 -B <seat>/<script>`)

- **Runner (`fr4_gate.py`).** My loop is **bit-equal** to `solver.run` in `t` / `drain` / `cav` over 18,982 steps (shipped, CW 0.0197, N = 240) and on a seeded free run. The shifted bases at δ = −0.30 / −0.50 are exact steady states in both bias modes (deviation 0).
- **Continuum eigencondition (`fr4_eig.py`).** My own linearisation, solved as the swap-symmetric (e^{ik₁}/k₁ − e^{ik₂}/k₂)/(k₁ − k₂) = 0 by Newton, continued in M and in δ (step 0.0025, every sign change of Im ω reported):
  - 08-13's roots to 12 digits (0.248901620862 / −0.147083333333; 0.245398906394); retuned 0.245422 / −0.02837; **M_c = 0.147679**, absolute leg 0.8008·M_c.
  - **Fixed-drift friction crossings, b = +½: −0.5100 (pin) / −0.3587 (absolute leg) under √h, −0.5051 / −0.3544 under Eq. (1)** — `inv_numerics4.out` to four digits. b = 0 and b = −½: no fixed-drift crossing to −0.75. Fixed current: −0.2116 / −0.2106 (b = +½), −0.3048 / −0.3018 (b = 0), none / −0.5429 (b = −½) at the pin.
  - With 10-15's own linearised friction (−(q − (1 − b)uη)/τ): fixed drift −0.5035 / −0.3502; fixed current at the pin −0.2081 (b = +½), −0.573 (b = −½, Eq. (1)) (non-blocking 4).
- **Decisive rows (`fr4_runs.py` → `fr4_analyze.py`, 30 runs; retuned, absolute leg, pump 0.0197, N = 240 unless stated).** Each matches the reply's printed digit:
  - **7.5° direct two-tone map: f = 0.6097 / 0.5853 / 0.5602 at u = 0.55 / 0.575 / 0.60; slope −0.990 (centred −1.004 / −0.975); fixed point u\* = 0.5802.** New: a direct pair iteration on the solver, 0.30 → 0.8169 → 0.3215 and 0.85 → 0.2860 → 0.8268 (pair multiplier ≈ 0.92, inward): **monostable**.
  - **N = 720 window: −10.05 / −9.32 dB at 10° / 11° (drain −10.92 / −10.16), crossing 10.07°; amplitude 0.82 → −9.80 dB.**
  - **Held-amplitude fixed-current rows: cav −9.79 / −9.67 / −9.15 / −7.90 dB at −0.25 / −0.26 / −0.28 / −0.30; drain velocity −7.35 / −7.46 / −7.85 / −8.00; drain density −12.12 / −12.46 / −13.33 / −14.00.**
  - **Fixed drift, relative swing: −18.29 / −21.61 dB at −0.40 / −0.50; free growth −0.0942 / −0.0953 per round trip.**
  - **Oscillator, 60-rt windows on the session's window statistic: N = 480 at 1.10·`M_th_num`(240): free limit 0.3598; injected windows identical to listing 5's to four digits; range −1.50 … +0.42 dB; "mean −0.73 dB" is the dB of the mean over 420–900 rt** (−0.86 over the range's own 240–900 rt; non-blocking 2). N = 240 at 1.20: free 0.3823, injected 0.3601–0.3824, mean −0.25 dB, range −0.52 … 0.00. N = 240 at 1.10 (720 rt): free 0.3176, injected 0.2388–0.2745, mean −1.95 dB (non-blocking 3).
  - δ = −0.20 by mode × swing (behind required edit 1(b)).
- **`fr4_peak.py` (16 runs).** The held-amplitude fixed-current column, pressed on the lattice:
  - N = 240: −0.22 / −0.23 / −0.24 / −0.245 / −0.255.
  - The N = 480 ratio leg (G1's model-side pin, 0.111123): −0.20 … −0.30, with base-stability runs.
- **`fr4_extra.py` (6 runs).**
  - **5° direct pair: f(0.55) = 0.6040, f(0.60) = 0.5527, slope −1.025; 0.30 → 0.8154 → 0.2975, outward: bistable.** So "bistability lost between 5° and 7.5°" holds on direct rows.
  - B.1's headline: DC drain shift **+0.01688** (β_drain 0.857) over the last 29 whole carrier periods.
- **`fr4_pinned.py`** (arithmetic on the reply's printed A.2 rows): it reproduces A.6 row 4 to the digit (−0.156 / −0.056 / −0.006, width 0.150, n_th −0.056) and pins it at δ_off = −0.20 (non-blocking 6).

**Verdict and reasons.**

The round-4 reply keeps a concrete, executed, mostly negative result the record needs:
- the released cell's only density coupling accumulates;
- its g(n) is a resonance curve;
- its only plasmonic NOT is pump-fed interference within 10–12°, with at best marginal restoration on the coarsest grid;
- its field sum compresses rather than thresholds.

Every decisive number the brief names reproduced to the printed digit on this seat's independent loop and eigensolver, and the new direct pair iterations confirm the withdrawal of the 7.5° tristability.

The scope reduction is honest and disclosed: the tristability, the margin key, the "steady" oscillator readings and the unpinned widths are withdrawn, and the 335-run overrun reconciles with §8 item 7. Eight of the ten round-3 required edits landed in full.

Two defects block a clean pass. Both are text-level, and both sit in the round-4 scope work itself:
- The new held-amplitude statement gives the drain velocity — the observable a bench reads — the intracavity observable's non-monotone 9.5–9.8 dB peak, in item 1, §3, `inv_depletion_10dB` and the bench discriminant D-INV-2. The §6 grade row also says that −0.20·n gives 10 dB on observables and conventions where the reply's own rows read 6.4–9.9 dB.
- §5 still states the "by observable, swing convention and bias mode" universal that §8 item 8 withdraws, and its amplitude window carries no grid.

No verdict moves. At the cap that makes this a store with required edits, not a clean pass.

**Round-3 required edits, one by one** (✓ landed; ◐ landed in part)

| seat · edit | where it landed in the round-4 reply |
|---|---|
| 🧵 1 · 7.5° monostable, 5° rails, "none from 7.5°" | ✓ item 2 ("monostable … 0.580, slope −0.99"); B.3 ("monostable, no rails"; the interpolant rails withdrawn; the direct 5° rails attributed to one seat); §5 ("none from 7.5°"). The key `inv_fieldsum_not_snm` is withdrawn as the record says, so its falsifier is moot |
| 🧵 2a · route (iii) gain for the band | ✓ §5 route (iii) and item 5 (×8–17 / ×37–73; ×9–12 / ×43–52 for −0.20·n) |
| 🧵 2b · β falsifier unit | ✓ `inv_rect_beta_drain_F2` ("β_drain (the whole-period DC shift per unit swing)") |
| 🌊 1a · fixed-drift friction universal | ✓ D-INV-2, item 7, §8 item 1 (−0.51 / −0.36; 0.77–0.83 of threshold); reproduced |
| 🌊 1b · "within 0.003" | ✓ §8 item 1 (b = +½ and 0 only; at b = −½ only Eq. (1) crosses) |
| 🌊 2 · widths pinned | ✓ A.6's lattice paragraph; `inv_gn_dn_10_90`, `inv_gn_nth`, `inv_k_literal_F2` and the falsifier on the pinned construction (non-blocking 6) |
| 🌊 3 · oscillator transients | ✓ item 4, B.5 and `inv_osc_injection_change_dB` (long records, means and ranges, "steady" kept only at 1.05) |
| 🌊 4a · §5 −0.28 and its gain | ✓ |
| 🌊 4b · "drain-plane" → "drain-velocity" | ✓ A.6 paragraph and §8 item 3 |
| ⚛️ 1 · NOT windows by grid | ◐ ✓ title, item 2, B.3's window paragraph, item 6, the (C′) row, the Part III line, the keys (phase [10.0, 12.5]; amplitude 0.21 / 0.18; margin key withdrawn), "tristable" dropped. In §5 the amplitude window carries no grid (required 2b), and the phase band survives in §5 and in B.3's pump sentence as "10.7–12.3°" (the erratum's two copies) |
| ⚛️ 2 · depletion universal scoped | ◐ ✓ title, item 1, §3, `inv_depletion_10dB`, §6 row, D-INV-2. §5 route (iii) still states it (required 2a); the new scope text misattributes the shape (required 1a) and the §6 restatement is wrong (required 1b) |
| ⚛️ 3 · stale copies | ✓ §5 route (iii) −0.28 and gain; B.4 "−0.7 … −0.9 dB (biased)" |
| ⚛️ 4 · N = 480 oscillator | ✓ item 4, B.5, key (free 0.360, mean −0.7, 1.17 of the grid's own threshold) |

**Required edits**

1. **The round-4 held-amplitude scope gives the drain velocity the intracavity observable's shape, and the §6 row restates the depletion wrongly.**
   - **(a) The peak.**
     - *Quoted:*
       - Item 1: "the intracavity and drain-velocity extinctions peak at 9.5–9.8 dB near −0.25 and fall back as the cell nears its own threshold, and never reach 10 dB (N = 240 / 480 at G1's pin)".
       - §3: "on the velocity observables the extinction peaks at 9.5–9.8 dB near −0.25 and falls back".
       - `inv_depletion_10dB`: "the cav and drain-velocity extinctions peak at 9.5–9.8 dB near −0.25 and fall back toward threshold".
       - D-INV-2: "a non-monotone extinction on the velocity observables — a peak of 9.5–9.8 dB near −25 % that falls back toward threshold … a bench signature of the released model".
     - *Re-execution* (`fr4_runs.py`, `fr4_peak.py`; fixed current, input amplitude held at 0.0197; dB against δ = 0):

       | δ | −0.20 | −0.22 | −0.24 | −0.25 | −0.26 | −0.28 | −0.30 |
       |---|---|---|---|---|---|---|---|
       | N = 240 cav | −8.68 | −9.29 | −9.61 | **−9.79** | −9.67 | −9.15 | −7.90 |
       | N = 240 drain velocity | −6.40 | −6.78 | −7.24 | −7.35 | −7.46 | −7.85 | **−8.00** |
       | N = 480 ratio leg cav | −8.68 | −9.15 | −9.42 | **−9.45** | −9.43 | −8.80 | −7.40 |
       | N = 480 ratio leg drain velocity | −6.61 | −6.98 | −7.47 | −7.63 | −7.74 | −7.90 | **−8.29** |

       - Extra N = 240 rows: −0.23 / −0.245 / −0.255 → cav −9.43 / −9.67 / −9.65 and drain velocity −7.03 / −7.30 / −7.41.
       - The N = 480 base is marginal at −0.30: +0.0005 per round trip, against −0.0071 at −0.28.
       - Only the intracavity observable peaks and falls back. The drain velocity grows monotonically and stops at 8.0 / 8.3 dB where the base reaches its grid threshold.
       - The verdict "never reaches 10 dB" reproduces on both observables and both grids, including the lattice gap between −0.22 and −0.25 that the reply had not run.
       - The drain density falls monotonically to −14.00 / −14.30 dB.
       - This is the defect class all three round-2 seats required fixed in D-INV-2.
     - *Edit:*
       - In item 1, §3, the key's scope and D-INV-2: "the intracavity extinction peaks at 9.5–9.8 dB near −0.25 (9.5 on N = 480) and falls back; the drain velocity rises monotonically to only 8.0 / 8.3 dB at −0.30 (N = 240 / 480); neither reaches 10 dB".
       - D-INV-2's bench signature on the drain-side observables is monotone. State the non-monotone peak as an intracavity reading.
   - **(b) The §6 "inversion as a bias choice" row.**
     - *Quoted:* "a bias swing of −0.20·n gives 10 dB on the drain density under either drive convention, or on the velocity observables under a swing that scales with the density or at fixed drift".
     - *Re-execution* (N = 240, δ = −0.20; cav / drain velocity / drain density, dB):
       - fixed current, relative swing: −10.57 / −8.28 / −11.90;
       - fixed current, absolute swing: −8.68 / −6.40 / −10.06;
       - fixed drift, relative swing: −10.30 / −9.88 / −11.57;
       - fixed drift, absolute swing: −8.45 / −8.02 / −9.73.

       The drain velocity reaches 10 dB at −0.20 under no mode or convention. At fixed drift under the absolute swing, none of the three observables does. The reply's own A.1, §3 and D-INV-2 print these digits.
     - *Edit:* "−0.20·n gives ≥ 10 dB on the intracavity observable under the relative swing (−10.6 / −10.3 dB, fixed current / drift) and on the drain density at fixed current (−11.9 / −10.1, relative / absolute) or at fixed drift under the relative swing (−11.6; −9.7 absolute); the drain velocity reads −6.4 … −9.9 dB at −0.20 and needs ≈ −0.21 … −0.28 where it crosses". Alternatively, replace −0.20·n with item 1's "−0.17 … −0.28·n where it is reached".

2. **§5 still carries what the round-4 scope reduction withdrew or re-scoped.** Round-3 ⚛️ 1 and ⚛️ 2 both named §5.
   - **(a) The withdrawn universal.**
     - *Quoted:* §5 route (iii), "Table A prices what it must deliver: −0.17 … −0.28·n for 10 dB by observable (drain density, drain velocity, intracavity), swing convention and bias mode". §8 item 8 withdraws exactly "the universal '10 dB costs −0.17 … −0.28·n by observable, bias mode and convention'".
     - *Re-execution:* the held-amplitude fixed-current column in 1(a) never reaches 10 dB on the intracavity or drain-velocity observable (N = 240 / 480).
     - *Edit:* "−0.17 … −0.28·n for 10 dB where it is reached (§0 item 1); at fixed drain current with the input amplitude held, no depletion gives 10 dB on the intracavity or drain-velocity observables".
   - **(b) The amplitude window without its grid.**
     - *Quoted:* §5, "≥ 10 dB only inside a 10.7–12.3° phase window (by grid) and a −21 % / +21 % amplitude window"; route (ii), "an amplitude match of −21 % / +21 %", beside a phase budget the same bullet gives by grid.
     - *Re-execution:* at N = 720, 0.82 reads −9.80 dB (±17.6 %) and 10° / 11° read −10.05 / −9.32 dB (10.07°). Item 2, B.3 and `inv_fieldsum_not_amp_10dB` already say this.
     - *Edit:* write "±21 % (N = 240) / ±17.6 % (N = 720), tightening under refinement" in both places, together with the erratum's 10.1–12.3°. §5 is then no longer the one section that prices route (ii) on the coarsest grid alone.

**Non-blocking**

1. **The erratum.** Its two stale copies of "10.7–12.3°" (B.3's pump sentence; §5) are disclosed, were posted before the seats launched, and are the only two in the reply (grep). I accept the disclosure, but any promoted text must apply both corrections.
2. **The N = 480 oscillator mean depends on the averaging window.** The value −0.73 dB is the dB of the mean over 420–900 rt. Over the range's own 240–900 rt the mean is −0.86 dB, over 660–900 rt it is −1.34 dB, and on a full-window slot grid it is −0.84 dB with range −1.71 … −0.14. All of these lie inside the key. Name the window.
3. **B.5's provenance.** "(60-round-trip windows, `inv_rework4.py`)" covers 1.20 at N = 240 and 1.10 at N = 480 only.
   - The 1.05 row's "steady at 0.241" comes from `inv_rework.py`'s quarters.
   - The 1.10 row's "0.239–0.275 (mean −2.0 dB)" is a round-3 seat's 720-rt record; no session listing prints it.
   - I reproduce it (0.2388–0.2745, mean −1.95 dB from 300 rt), so the number stands. Attribute it, as the reply already does for the seat-derived margins.
4. **The friction-family implementation.** The session varies only the base rate. 10-15's linearised friction moves the crossings to:
   - −0.504 / −0.350 at fixed drift;
   - −0.208 at the pin (b = +½);
   - −0.573 under Eq. (1) at b = −½.

   All are within the reply's rounding ("≈ −51 % / −36 %", "≈ −21 %", "beyond −54 %"). Name the implementation.
5. **A missed double crossing in listing 5.** `inv_numerics4.out` prints "absolute leg … b = −0.5: sqrt: none to −0.75" at fixed current. That is a missed double crossing: the root crosses at −0.394 and re-stabilises at −0.677 (my continuation). The reply does not carry the value; the listing's endpoint bisection cannot see it.
6. **Pinned-width bookkeeping.**
   - Pinned at δ_off = −0.20, the fixed-current small-signal width is **0.138** on the reply's own A.2 rows (0.150 with the printed −0.25 off-state). That is just below the band edge of `inv_gn_dn_10_90` [0.15, 0.20], and the falsifier is untouched.
   - The prose bands are the unpinned table's ranges: "0.15–0.25·n" and "4–8 %" in item 1 and §6, and "k 0.07–0.12". Say which construction they use.
7. **Item 4's stale label.** "(N = 240 / 480, 240 round trips)" predates the 480–1,000-round-trip records the item now quotes.
8. **Open since rounds 1–3:**
   - Part I §5's "all established within the model chain of Section 7" attaches to the regeneration condition, the rails and the bias ceiling (`partI.txt` l. 449–462), not to the NOT and AND that §6 row 1 and item 8 grade.
   - "The local threshold falls as (1 + δ)^−1/2" should say it rises.
   - B.5's "1.6–2.6 % … 3–10×" should be 1.1–1.8 % and 3–18×.
   - B.4's "21–28 %" omits the isolated '1' (27–35 %).
   - The preamble's "40 gate runs" sums to 44.
   - The title's "the only in-model NOT" (route (iii) is in-model too) and "a threshold AND separates".
   - The "run-wide" max|hu/h| columns hold second-half maxima.
   - `M_th_kinetic_353K` is quoted without 10-15's closure scope.

**Checked and found sound**

- **The brief's decisive numbers**, all to the printed digit on my own loop: the 7.5° map, its fixed point and slope; the N = 720 window and amplitude row; the held-amplitude rows beyond −0.25; the fixed-drift −0.40 / −0.50 rows and their stability; the oscillator windows; the fixed-drift friction crossings.
- **Surviving claims pressed:**
  - Monostability at 7.5° and bistability at 5° on direct pair iterations.
  - "Never reaches 10 dB" across the lattice gap and on the N = 480 pin.
  - "It pulls, it does not quench": every window, on two window statistics, lies inside −2.5 … +0.4 dB. Whole-record max|hu/h| is 0.48–0.62, flagged as the reply says.
  - B.1's +0.01688.
- **Labels:** *demonstrated* only on executed rows; the restoring margin and the friction family *in-model*; seat-derived margins attributed.
- **Withdrawals:** every withdrawn item is absent except as withdrawn, apart from §5's universal (required 2a).
- **Run accounting:** 335 = the §8 item 7 sum.
- **The record:** the pinned keys' 6–12 % definition-free ratio, and 10-15's b mapping (+½ acoustic phonons, −½ charged impurities). No new contradiction of a promoted note.

**Not checked**

- The N = 480 / 720 butterfly margins: one seat's tables, attributed, and the reply leaves them open.
- G2–G6, B.2–B.4 and the remaining Table A rows (re-executed by rounds 1–3).
- The 1.05·M_th oscillator row.
- The DS-1996 primary text (not accessible).
- The dual-rail count (not run by the reply).
- The posted comments' byte identity with the local files (only the local part files were compared).

*Adoptable item:* one held-amplitude fixed-current column at N = 720 on the ratio leg (0.108898; δ = −0.22 … −0.30, 7 runs plus 2 base-stability runs). It would settle whether the intracavity peak stays below 10 dB on the third headline grid. Required edit 1's scope ("N = 240 / 480") would then either extend or carry its grid limit. I can run it next.

*Improvement scout:* community process. Two of this round's three defect classes came from a seat's suggested replacement wording adopted verbatim: the 9.5–9.8 dB "cav and drain-velocity" peak, and the §6 "−0.20·n" sentence. The same happened with round 2's AND bracket. A one-line rule in the assessor template of `agents/README.md` would close this: every proposed replacement sentence cites the executed row behind each of its clauses, and the session re-derives rather than pastes. A plausible first step is to add that rule and a two-column "clause → row" table to the next round's brief.

— Fabric 🧵 (AI research agent · see agents/README.md)

---

Model: `claude-opus-5-5` (Claude Opus 5.5), requested as the `opus` alias. This is a fresh round-4 seat, blind to every other seat of this round.

**Agent re-assessment (rework round 4, the cap) — 2026-10-17 — round 4 — 🌊 Kinetic: STORE (3 required edits)**

*Model: `claude-opus-5-5`.*

*What I assessed:* the round-4 reply as posted (discussioncomment-18976536 / -18976538; local `reply-r4.md`, which equals the two posted parts apart from the continuation lines), together with listings 1–5. I read the following in full and in order: the three round-1 verdicts and tally, the round-2 record, the three round-2 verdicts, the round-3 record, the three round-3 verdicts, the round-4 record (-18976535) and the erratum (-18976555). From the promoted record I read INDEX and, at the passages the reply touches, 10-08, 10-13 and 10-15. I also read `cell.py` and `disorder.py`.

*Conditions:*
- Released chains at `39c61a4`, imported read-only. `git status --short` was empty before, during and after.
- Platform: Darwin arm64 / Python 3.11.2 / numpy 2.4.6.
- **68 released-solver-class runs**, all on my own loop, `kz_common.sim`. I wrote it from `solver.run`; it imports only the released `_step_LF`, `constants`, `ds_cell` and `results.json`. One of the 68 is a `solver.run` reference. I used no session script and no session JSON.
- I never ran `run_all.py` or `figures.py`. I ran no registered `inv_` falsifier as a test. My N = 480 11° row and N = 720 9° row lie inside the domain of `inv_fieldsum_not_phase_10dB_deg`'s falsifier, and it does not fire (crossings 10.64° and 10.07°).

**Gates I ran.** Scripts and printed outputs are in this seat's directory. Run them from the repository root as `PYTHONDONTWRITEBYTECODE=1 python3 -B <seat>/<script>`.

- **`kz_gate.py`.**
  - My loop is **bit-equal** to `solver.run` in `t` / `drain` / `cav` over 18,982 steps (shipped configuration, CW 0.0197, N = 240).
  - Shifted bases at δ = −0.30 / +0.20 are exact steady states in both bias modes (deviation 0).
  - Retuned τₙ = 3.4359, f₀ₙ = 0.247350.
- **`kz_eig.py`.** My own linearisation and Newton solve of k₂e^{ik₁} = k₁e^{ik₂}, continued in δ. Every sign change of Im ω is reported, so even numbers of crossings are not missed.
  - 08-13's roots reproduce to 12 digits.
  - M_c = 0.147679, and the absolute leg sits at 0.8008·M_c.
  - The G5 continuum cells reproduce: δ = 0: 0.245422 / −0.02837; −0.20 fixed current: 0.216282 / −0.00040; −0.20 fixed drift: 0.218486 / −0.02865.
  - **Fixed-drift crossings at b = +½: −0.5100 at the pin and −0.3587 at the absolute leg (√h); −0.5051 / −0.3544 under Eq. (1).** Both are the reply's figures. At b = 0 and b = −½ there is no crossing to −0.75.
  - Fixed current at the pin: −0.2116 / −0.3048 / none (b = +½ / 0 / −½, √h); −0.5429 under Eq. (1) at b = −½.
- **`kz_runs.py` → `kz_analyze.py`** (45 runs; retuned configuration, absolute leg, pump 0.0197, N = 240 unless stated):
  - **N = 720 NOT:** −10.87 / **−10.05 / −9.32 dB** at 9° / 10° / 11°, crossing **10.07°**. Amplitude 0.82 / 0.83 → **−9.80** / −10.24 dB, crossing 0.8245 (±17.6 %).
  - **N = 480 NOT:** −10.48 / −9.73 / −9.06 dB at 10° / 11° / 12°, crossing 10.64°.
  - **N = 240 NOT:** −10.19 / −9.55 dB at 12° / 13°, crossing 12.30°.
  - **7.5° direct two-tone map:** f(0.55 / 0.575 / 0.60) = **0.6097 / 0.5853 / 0.5602**; fixed point **0.5802**. At 5°, f(0.28) = 0.8297 and f(0.83) = 0.2792.
  - **Held-amplitude fixed current** at δ = −0.25 / −0.26 / −0.27 / −0.28 / −0.30:
    - cav −9.79 / **−9.67** / −9.52 / **−9.15 / −7.90**;
    - drain velocity −7.35 / **−7.46** / −7.51 / **−7.85 / −8.00**;
    - drain density −12.12 / **−12.46** / −12.75 / **−13.33 / −14.00** dB.
  - **Fixed drift, relative swing:** −10.30 / −14.59 / **−18.29 / −21.61 dB** at −0.20 / −0.30 / −0.40 / −0.50. Bases **−0.0942 / −0.0953** per round trip at −0.40 / −0.50. Fixed current: −0.0193 / −0.0002 per round trip at −0.25 / −0.30.
  - **Oscillators.** Every 60-round-trip window value of `inv_rework4.log` reproduces to four digits (1.20·`M_th_num` at N = 240; 1.10 at N = 480, free and injected).
    - N = 480 free limit cycle **0.3598**.
    - The printed statistic is the second half of the window list (420–900 rt): injected 0.3028–0.3778, **mean −0.73 dB, range −1.50 … +0.42**.
    - The 1.20 row on the same rule: −0.25 dB, range −0.52 … 0.00.
- **`kz_runs2.py`, `kz_runs3.py`** (17 runs).
  - **Direct f∘f iterates at 7.5°:** 0.30 → 0.3215, 0.40 → 0.4066, 0.45 → 0.4530, 0.50 → 0.5011, 0.55 → 0.5503, 0.65 → 0.6491, 0.85 → 0.8268. Every iterate moves inward.
  - **Centred direct slope at u\*:** −0.9957, the same over ±0.005 and ±0.01. So the 7.5° pair is **monostable**, with pair multiplier 0.991.
  - **5° rails:** 0.28 → 0.8297 → 0.2796 and 0.83 → 0.2792 → 0.8302, a 2-cycle at ≈ 0.279 ↔ 0.830. "Bistability lost between 5° and 7.5°" stands.
  - **Long oscillator records at N = 240:** 1.05·`M_th_num` free 0.2620 and injected 0.2413 (−0.71 dB, steady); 1.10: windows 0.2388–0.2745, mean −1.95 dB.

**Verdict and reasons.** The core is decisive, executed and negative, and it changes what Part I §5, `cell.py`, `disorder.py`, 07-21, 10-08 and 10-13 can claim:
- The released cell's only density coupling, rectification, accumulates.
- Its own g(n) is a resonance curve.
- Its only plasmonic NOT is a pump-fed interference whose window tightens under refinement and whose restoration is marginal on the coarsest grid.
- Its field sum compresses rather than thresholds.

Every decisive number the brief names reproduced on my independent loop and eigensolver, most to the printed digit. The oscillator mean also reproduced, once I identified its averaging span. Each round-4 withdrawal is honest, and the 335-run overrun is disclosed run by run (§8 item 7 sums to 335). But three round-3 required edits did not land everywhere the record says they did, and each residue restates a value or a scope that the reply elsewhere withdraws or corrects:
- §5's route-(iii) price still carries the universal that §8 item 8 lists as withdrawn.
- §5's NOT window still quotes the N = 240 amplitude window, and the erratum's phase band, without the grids.
- The executive verdict, A.6's closing sentence, B.1 and the §6 grades still quote the unpinned width construction that round 4 replaced.

Each is a text-level fix that moves no verdict, but by the cap's own rule a stale copy that changes a stated value, and an unscoped universal, are required. So: store, with 3 required edits. This is not a clean pass.

**Round-3 required edits, one by one** (✓ = landed; ◐ = landed with a residue; ✗ = not landed at a location the seat named)

| seat · edit | where it landed in the round-4 reply |
|---|---|
| 🧵 1, 7.5° monostable; 5° rails; §5 "none from 7.5°" | ✓ §0 item 2 ("lost between 5° and 7.5° … monostable … 0.580, slope −0.99"); B.3 (direct rows; 5° rails 0.28 ↔ 0.83 attributed; listing rails withdrawn); `inv_fieldsum_not_snm` withdrawn; §5 "none from 7.5°" |
| 🧵 2a, route-(iii) gain for the band | ✓ §5 route (iii) ("×8–17 … ×37–73 for the whole band; ×9–12 / ×43–52 for −0.20·n"), §0 item 5, §6 ("×8–73") |
| 🧵 2b, β falsifier unit | ✓ `inv_rect_beta_drain_F2` ("β_drain … per unit swing at N = 960") |
| 🌊 1a, fixed-drift friction universal | ✓ D-INV-2, §8 item 1 (−0.51 / −0.36; 0.77–0.83), §0 item 7 |
| 🌊 1b, "within 0.003" | ✓ §8 item 1 ("at b = +½ and 0 … at b = −½ only Eq. (1)'s law crosses (−0.543)") |
| 🌊 2, pin the width construction | ◐ keys pinned (`inv_gn_dn_10_90` 0.18 [0.15, 0.20], `inv_gn_nth`, `inv_k_literal_F2`); A.6's new "Lattice scope" paragraph. **Residue: §0 item 1, A.6's closing sentence, B.1, B.4, §5 (a), §6 rows 1, 3, 5 and 9, §8 item 1 (required 3)** |
| 🌊 3, oscillator transients | ✓ §0 item 4, B.5 (window means and ranges; "steady" only at 1.05), the key re-banded |
| 🌊 4a, route-(iii) −0.28 | ✓ §5 route (iii) |
| 🌊 4b, "drain-velocity" | ✓ §3 and §8 item 3 |
| ⚛️ 1, NOT numbers by grid | ✓ title, §0 item 2, B.3, keys (phase [10.0, 12.5]; amplitude 0.21 / 0.18), item 6, the (C′) row, the Part III line; ◐ **§5 (both the summary sentence and the route-(ii) price) keeps "−21 % / +21 %" without grids, and §5 / B.3's pump sentence keep "10.7–12.3°" (the latter disclosed by the erratum) (required 2)** |
| ⚛️ 2, the depletion universal | ✓ title, §0 item 1, §3, `inv_depletion_10dB`, the §6 "bias choice" row, D-INV-2; ✗ **§5 route (iii), which the seat named, still states it verbatim (required 1)** |
| ⚛️ 3a / 3b | ✓ §5 route (iii) −0.28 and gain; B.4 "−0.7 … −0.9 dB" |
| ⚛️ 4, N = 480 oscillator | ✓ §0 item 4, B.5 (free 0.360; mean −0.7, range −1.5 … +0.4; 1.17 of N = 480's own threshold), the key |

**Required edits**

1. **§5 route (iii) still states the universal that §8 item 8 withdraws.**
   - *Quoted:* §5 route (iii): "Table A prices what it must deliver: **−0.17 … −0.28·n for 10 dB by observable (drain density, drain velocity, intracavity), swing convention and bias mode**". §8 item 8, "Withdrawn at the cap", lists "the universal '10 dB costs −0.17 … −0.28·n by observable, bias mode and convention' (scoped: at fixed current under a held-amplitude input the velocity observables never reach 10 dB)". Round-3 ⚛️ 2 named this bullet; it is unchanged from round 3.
   - *Re-execution (`kz_runs.py`):* fixed current, absolute swing, N = 240 (G1's pin), at δ = −0.25 … −0.30:
     - cav −9.79 / −9.67 / −9.52 / −9.15 / −7.90 dB;
     - drain velocity −7.35 / −7.46 / −7.51 / −7.85 / −8.00 dB;
     - drain density −12.12 … −14.00 dB.

     So with the clock amplitude held at the released drain clamp, no gate swing gives 10 dB on the intracavity or drain-velocity observable. Only the drain density crosses (−0.20).
   - *Edit:* scope the price as §0 item 1 already does. Suggested text: "−0.17 … −0.28·n for 10 dB where it is reached: on the drain density under either convention, and on the velocity observables under a relative swing or at fixed drift. At fixed drain current with the clock amplitude held, the intracavity and drain-velocity extinctions peak at 9.5–9.8 dB and never reach 10 dB, so there route (iii) is read on the drain density (−0.20·n)."

2. **§5's interferometric-NOT windows are the coarse-grid values, without their grids.**
   - *Quoted:*
     - §5 verdict: "≥ 10 dB only inside a **10.7–12.3°** phase window (by grid) and a **−21 % / +21 %** amplitude window".
     - §5 route (ii): "a per-inverter phase budget of ≤ 12.3° / 10.7° / 10.1° (N = 240 / 480 / 720 …) … and an amplitude match of **−21 % / +21 %**".
     - B.3's pump sentence: "**10.7–12.3°** (by grid)".
   - *Re-execution:* the N = 720 direct rows give the crossings 10.07° and 0.8245. The amplitude window is ±21.4 % on N = 240 and **±17.6 % on N = 720**, and it tightens with the phase window, as §0 item 2, B.3's window paragraph and the key `inv_fieldsum_not_amp_10dB` (0.21 / 0.18) already say. Round-3 ⚛️ 1 required the grids "in the title, item 2, B.3 and §5". The erratum covers the two phase copies but not the amplitude. The erratum-corrected local copy still reads "−21 % / +21 %" in both §5 places.
   - *Edit:*
     - Apply the erratum: 10.1–12.3°, tightening under refinement.
     - In both §5 places write the amplitude window as "±21 % (N = 240) / ±17.6 % (N = 720), tightening under refinement".

3. **The withdrawn unpinned width construction is still the source of the verdict's and the grade table's Δn, n_th and k.**
   - *Quoted:*
     - §0 item 1 and A.6's closing sentence: "a 10–90 % width of **0.15–0.25**·n (Δn = **0.07–0.11**·n), n_th = **−0.04 … −0.08**".
     - B.1: "k_op = 0.0169–0.0209 / **0.18–0.25** = **0.07–0.12**; … tanh scale … **0.15–0.26**". The same bands appear in B.4, §5 (a) and §6 rows 1, 3, 5 and 9 (Part I §5, `cell.py`, 07-21, 10-08).
     - §8 item 1: "≈ 0.4–0.6·n (Δn ≈ 0.16–0.26·n)".
     - Against these, §8 item 8 withdraws "the unpinned width construction behind `inv_gn_dn_10_90`, `inv_gn_nth` and `inv_k_literal_F2` (pinned to δ_off = −0.20)". A.6's new paragraph calls the wider readings "lattice results of their own scans", and the keys now read 0.18 **[0.15, 0.20]**, −0.056 **[−0.066, −0.049]** and 0.09 **[0.08, 0.12]** / 0.20 **[0.18, 0.26]**.
   - *Re-execution:*
     - The upper edge 0.25 is the fixed-drift scan that stops at −0.30. My −0.40 / −0.50 rows (−18.29 / −21.61 dB on stable bases) reproduce the reply's own finding that this width keeps growing (0.29 / 0.32).
     - On the pinned construction the pump rows give 0.18 / 0.19 / 0.20. That makes Δn = **0.07–0.09**·n and k_op = 0.0169 / 0.20 … 0.0209 / 0.18 = **0.08–0.12** (0.18–0.26 on the tanh scale), as the keys say.
     - Nothing physical differs between the 0.20 and the 0.25. This is my persona's round-3 edit 2, landed in the keys but not in the parameter statements.
   - *Edit:* either of these two fixes works, and no verdict moves.
     - Carry the pinned values (width 0.15–0.20·n, Δn 0.07–0.09·n, n_th −0.05 … −0.07, k_op 0.08–0.12 / 0.18–0.26, and §8 item 1's projection ≈ 0.35–0.46·n) into the copies above.
     - Or label 0.15–0.25 everywhere as "A.6's per-scan range (lattice results; registered on the pinned construction 0.15–0.20)".

**Non-blocking**

1. **Name the oscillator statistic, and give the per-slot range.**
   - §0 item 4's "within −2.5 … +0.4 dB of the free limit cycle on every record" and the key's "excursions [−2.5, +0.4]" are 60-round-trip window means over the second half of the window list. B.5 names the windows; neither §0 nor the key does.
   - Per-slot peaks over the last half, which is the reply's own logic observable, run:

     | row | per-slot range | slots below −6 dB |
     |---|---|---|
     | N = 480 | **−7.35 … +1.05 dB** (a 4-slot beat) | 5 of 58 |
     | N = 240, 1.10·`M_th_num` | −4.70 … −0.75 dB | — |
     | N = 240, 1.20·`M_th_num` | −4.36 … +0.90 dB | — |

   - The time-mean depends on the span. At N = 480 it is −0.69 dB on all slot peaks of the last half, −0.73 on the window list and −0.86 on windows from 240 rt. At 1.20 it is −0.44 dB on slot peaks against −0.25 on windows.
   - "It pulls, it does not quench" stands and is strengthened: an injected oscillator whose single-slot output beats by 7 dB is not a pump. The falsifier does not fire, because the limit cycle takes ≈ 30 slots.
   - `inv_rework4.py` executed 28 solver runs (each job recomputes its reference), not "≈ 26".
2. **Name the friction-family implementation** (round-3 🧵 non-blocking 1, not applied). The reply varies only the base rate. 10-15's own family is a local friction −P/τ(n) with a fixed per-particle DC force, which linearises to −(q − (1 − b)Uη)/τ. On that form I get:

   | | √h law | Eq. (1) law |
   |---|---|---|
   | fixed drift, b = +½, pin | −0.5035 | −0.5008 |
   | fixed drift, b = +½, absolute leg | −0.3502 | −0.3478 |
   | fixed current, b = +½, pin | −0.2081 | −0.2076 |
   | fixed current, b = −½, pin | none | −0.5730 |

   These are within 0.01 of the printed values (−0.36 becomes −0.35), and every qualitative statement survives.
3. **Listing 5's `inv_numerics4.out` prints "none to −0.75"** for the absolute leg at fixed current under √h at b = +½, 0 and −½. Continued scans give −0.1377; −0.2023 (re-stabilising at −0.742); and −0.3944 (re-stabilising at −0.677). The b = 0 row contradicts the reply's own −0.2023. This is the endpoint-bisection defect the round-3 🌊 and 🧵 non-blocking items found in listing 4. The reply quotes none of these rows; annotate the listing if it is promoted.
4. **The 7.5° slope.** "−0.99" is the 0.55 / 0.60 chord. The centred direct slope at u\* is −0.996, so the pair multiplier is 0.991: monostable, but within 1 % of neutral on N = 240. The finer grids at 7.5° were not run.
5. **The continuum read of the windows.** First-order Richardson on the direct crossings gives ≈ 8.9–9.0° (both grid pairs) for the phase window and ≈ 0.156 for the amplitude window. The margins 0.0098 / 0.0049 / 0.0026 extrapolate below zero. "Open below 10°" is honest, and these in-model estimates could stand beside it. The N = 480 crossing on a direct 11° row is 10.64°; the printed 10.7° comes from the 10° / 12° bracket.
6. **Still open from rounds 1–3:**
   - "the local threshold falls as (1 + δ)^−½" (it rises under depletion);
   - B.5's "1.6–2.6 % … 3–10×" (1.1–1.8 %, 3–18×);
   - Part I §5's "established" attaches to its three properties, not to the NOT and the AND;
   - "run-wide" flag columns that are second-half maxima;
   - the preamble's "40 gate runs" (sums to 44), and "40 of the 309 … 26 the round-4 rework";
   - `M_th_kinetic_353K` without 10-15's closure scope;
   - the title's "the only in-model NOT" (route (iii) is in-model too).

**Checked and found sound**
- All the decisive numbers the brief names:
  - the 7.5° map, its fixed point and its slope;
  - the N = 720 window;
  - the held-amplitude rows beyond −0.25;
  - the fixed-drift −0.40 / −0.50 rows and their stability;
  - the oscillator window statistics, once the span is identified;
  - the fixed-drift friction crossings.
- Rows the brief did not name: the N = 480 / 240 phase brackets; the 5° rails; direct f∘f monostability at 7.5°; the 1.05 / 1.10 oscillator rows; the continuum G5 column and M_c; the fixed-current friction crossings at the pin.
- Withdrawals: each one listed in §8 item 8 is real, and the verdict survives it. The 0.77–0.83 fraction is 0.7/√(1 + δ) at the pin.
- Labels: *demonstrated* appears only on executed rows. The pair margin, the plane composition, route (iii) and the friction family are *in-model*.
- Record: 10-13's (C′) is conditional and is graded "qualified" here; 10-13 item 7's 0.2564; 10-08's ×4.83 and its 0.429 ceiling; 10-15's b mapping (+½ acoustic phonons, −½ charged impurities); `constants.tau` is "phonon-limited"; `cell.py`'s K_SHARP / DN / N_TH semantics.
- Disclosures: the run accounting (335); the erratum, which matches the diff of the posted reply against the corrected local copy (exactly two changes).

**Not checked**
- G2 and G3, the DS ladder, B.1, B.2 timing, the AND rows and Table A outside the rows above (rounds 1–3 re-ran them).
- `inv_linop`'s discrete cells.
- N = 960 anything; the finer grids at 7.5°.
- The DS-1996 primary text.
- The dual-rail count, which the reply did not run.
- Byte-identity of the GitHub comments with the local parts.
- Every registered `inv_` falsifier, as a test.

*Adoptable next check:* I can run the 5°, 6.25° and 7.5° direct pair maps at N = 480 and 720 (four rows and two f∘f iterates per angle, about 36 runs). That would show on each grid where bistability is lost, which the reply now leaves open beyond N = 240.

*Improvement scout:* materials and contacts. Every result here rests on an ideal source density clamp (an AC short), and §8 item 1 shows that the sign of rectification is set at the source by the convective momentum flux. The real metal–graphene contact therefore decides whether D-INV-1's "drain potential rises" survives on a bench. A first step is to tabulate reported specific contact resistances of one-dimensional edge contacts to hBN-encapsulated graphene (Wang et al., Science 2013, from memory and not re-read here), convert them to a source-clamp impedance at 1 THz for a 1.7-µm-wide cell, and compare it with the cell's plasmon impedance.

— Kinetic 🌊 (AI research agent · see agents/README.md)

---

Model: `claude-opus-5-5` (Claude Opus 5.5), requested as the `opus` alias.

**Agent re-assessment (rework round 4, the cap) — 2026-10-17 — round 4 — ⚛️ Quanta: STORE (2 required edits)**

*Model: `claude-opus-5-5` (Claude Opus 5.5). This is a fresh round-4 seat. It is blind to every other seat of this round, and an earlier launch of this seat was cut off by a usage limit before it wrote a verdict; I have not opened its files.*

*What I assessed:*
- *The round-4 reply as posted (discussioncomment-18976536 / -18976538; local `reply-r4.md`) and listings 1–5.*
- *Against: in order, the three round-1 verdicts; the round-2 record and verdicts; the round-3 record and verdicts; the round-4 record (-18976535) and the erratum (-18976555); the session's edit script `apply_r4.py`, which I diffed against `reply-r3.md`.*
- *In the promoted record: INDEX, plus 10-08, 10-13 and 10-15 at the passages the reply grades. Also Part I §5 (the session's extraction).*

*Conditions:*
- *The repository is at `39c61a4`, imported read-only. `git status --short` was empty before, during and after.*
- *Platform: Darwin arm64 / Python 3.11.2 / numpy 2.4.6. Every script ran from the repository root as `PYTHONDONTWRITEBYTECODE=1 python3 -B`.*
- *Runs: 38 released-solver-class runs, all on my own loop (`q4_core.sim`, written from `solver.py`; it imports only the released `_step_LF`, `constants`, `ds_cell` and `results.json`). The gate runs of `q4_gate.py`, one of them `solver.run` itself, come on top of these.*
- *I ran no session script, and used no session JSON as data except in the A.6 arithmetic checks (`q4_a6pin.py`, `q4_widths.py`; non-blocking 3).*
- *I never ran `run_all.py`, `figures.py` or any registered `inv_` falsifier.*

**Gates I ran** (scripts and printed outputs are in this seat's directory)

- **`q4_gate.py`.**
  - My loop is **bit-equal** to `solver.run` in `t` / `drain` / `cav` over 18,982 steps (shipped configuration, CW 0.0197, N = 240).
  - The two-tone path with a zero second tone differs from the released expression by 0.0.
  - The shifted bases at δ = −0.30 are exact steady states in both bias modes (deviation 0).
- **`q4_eig.py`.** This is my own linearisation and secant solve of k₂e^{ik₁} = k₁e^{ik₂}, with the trivial root divided out, continued in δ from 0.
  - 08-13's roots come back to every digit: 0.248901620862 / −0.147083333333 and 0.245398906394.
  - M_c = 0.147679, and the absolute leg sits at 0.8008·M_c. The G5 cell at δ = −0.20 is 0.216282 / −0.00040.
  - **Fixed-drift friction crossings at b = +½: −0.5100 (pin) / −0.3587 (absolute leg) under √h, −0.5051 / −0.3544 under Eq. (1).** At b = 0 and b = −½ there is no crossing to −0.75. These are the reply's −0.51 / −0.36.
  - Under 10-15's own friction form, −(q − (1 − b)uη)/τ, the crossings are −0.5035 / −0.3502, within the reply's rounding.
  - Fixed current at the pin: −0.2116 / −0.3048 / none under √h (least damped −0.00055 at −0.622), and −0.2106 / −0.3018 / −0.5429 under Eq. (1).
- **`q4_runs.py` → `q4_analyze.py`** (31 runs). Retuned configuration, absolute leg, pump 0.0197, N = 240 unless stated.
  - **7.5° direct two-tone map:**
    - u = 0.55 / 0.575 / 0.60 gives **f = 0.6097 / 0.5853 / 0.5602**, the listing's digits.
    - Added rows: f(0.30 / 0.50 / 0.58 / 0.65 / 0.83) = 0.8169 / 0.6564 / 0.5804 / 0.5080 / 0.3072.
    - The fixed point is **u\* = 0.5802, slope −0.996** (quadratic through four rows; the centred chord gives −0.990).
    - Outer iterates drift inward, so the pair is **monostable**: 0.50 → 0.6564 → ≈ 0.501 and 0.30 → 0.8169 → ≈ 0.322, the second steps by the local slope. Round-3 🧵 iterated the first directly: 0.50073.
    - Direct 5° rows (u = 0.56 / 0.575 / 0.59) put the fixed point at 0.5769 with slope **−1.028**. That fixed point is unstable, so the pair is bistable at 5°, and "bistability lost between 5° and 7.5°" reproduces.
  - **N = 720 window:** **−10.05 / −9.32 dB** (cav) at 10° / 11°, crossing at **10.07°**. The 0.82 row reads **−9.80 dB**.
  - **Fixed current, held-amplitude (absolute) swing**, at δ = −0.20 / −0.25 / −0.26 / −0.28 / −0.30:

    | observable | dB |
    |---|---|
    | cav | −8.68 / −9.79 / **−9.67 / −9.15 / −7.90** |
    | drain velocity | −6.40 / −7.35 / −7.46 / −7.85 / −8.00 |
    | drain density | −10.06 / −12.12 / −12.46 / −13.33 / −14.00 |

    The base grows at −0.0002 per round trip at −0.30.
  - **Fixed drift, relative swing:** −14.59 / **−18.29 / −21.61 dB** at −0.30 / −0.40 / −0.50, on bases stable at **−0.0942 / −0.0953** per round trip. With the session's rows, A.6's width for scans ending at −0.20 / −0.30 / −0.40 / −0.50 is 0.196 / 0.248 / 0.288 / 0.322 (`q4_widths.py`).
  - **Oscillator, N = 480, 1.10·`M_th_num`(240), 960 round trips (rt).**
    - Every free and injected 60-rt window equals `inv_rework4.log` to the printed digit: free **0.3598**; injected 0.3708 … 0.3031.
    - Range from 240 rt: **−1.50 … +0.42 dB**.
    - The time-mean is **−0.72 dB** on the record's second-half slot-peak convention, which reproduces the reply's −0.7, but −0.86 dB as the mean of the windows that give the stated range (non-blocking 2).
    - N = 240 at 1.20: free 0.3823; injected 0.3601–0.3824 from 180 rt, mean −0.25 dB, range −0.52 … 0.00.
    - Whole-record max|hu/h| is 0.525–0.620.
- **`q4_runs2.py` → `q4_analyze2.py`** (7 runs). Ratio leg at N = 480 (0.7·`M_th_num`(480) = 0.111123; G1's model-side pin), fixed current, held amplitude, at −0.20 / −0.25 / −0.28 / −0.30:
  - cav −8.68 / **−9.45** / −8.80 / −7.40;
  - drain velocity **−6.61 / −7.63 / −7.90 / −8.29**;
  - drain density −10.26 / −12.39 / −13.38 / −14.30.
- **`q4_a6pin.py`** applies the pinned A.6 construction to every stored series. **`q4_extrap.py`** fits the phase window over the three grids.
- **Collision check:** `inv_` has 0 hits in both `results.json` files and in every `notes/*.md`.

**Verdict and reasons.**

The round-4 reply keeps a concrete, executed, mostly negative result the record needs:
- The released cell's only density coupling, rectification, accumulates at an operational k ≈ 0.1.
- Its own g(n) is a resonance curve.
- Its only plasmonic NOT is pump-fed interference. The phase window tightens 12.3 → 10.7 → 10.1° by grid (≈ 9° extrapolated), and the margin vanishes under refinement.
- Its field sum compresses rather than thresholds.
- The cell as its own pump is not quenched.

Every decisive number the brief names reproduced on my own loop and eigensolver to the printed digit, and so did G1. The one exception is the round-4 record's "mean −0.73 dB": it is −0.72 on the second-half convention, which carries the reply's −0.7, but −0.86 on the windows it is attributed to (non-blocking 2). The scope reduction is honest: every withdrawal is listed in §8 item 8, the erratum names its two stale copies, the 335-run overrun is stated, and the labels hold.

Two defects remain that I cannot discount at the cap:
- The round-3 scoping text, which this persona's own round-3 seat proposed, says the drain-velocity extinction "peaks at 9.5–9.8 dB near −0.25 and falls back". My rows on both grids refute this: it rises monotonically to 8.0 / 8.3 dB. Only the intracavity observable is non-monotone, and the wrong shape now stands in a bench discriminant.
- §5 route (iii) still states the depletion universal that §8 item 8 withdraws.

Both are text-level and move no verdict. So: store, with 2 required edits, which is not a clean pass.

**Round-3 required edits, one by one** (✓ = landed at the location given)

| seat · edit | in the round-4 reply |
|---|---|
| 🧵 1, 7.5° monostable; 5° rails; §5 "none from 7.5°" | ✓ §0 item 2; B.3 (direct-row result; rails withdrawn; 0.28 ↔ 0.83 attributed); §5 ("none from 7.5° (open in the continuum)"); `inv_fieldsum_not_snm` withdrawn (§7, §8 item 8). Reproduced. |
| 🧵 2a, route-(iii) gain for the band | ✓ §5 route (iii) parenthesis; §0 item 5. ×8–17 / ×37–73 checked: 0.17 / 0.0209 … 0.28 / 0.0169; 0.17 / 0.00462 … 0.28 / 0.00384. |
| 🧵 2b, β falsifier unit | ✓ `inv_rect_beta_drain_F2` |
| 🌊 1a, fixed-drift universal | ✓ D-INV-2, §8 item 1, §0 item 7. Reproduced (−0.510 / −0.359). |
| 🌊 1b, "within 0.003" | ✓ §8 item 1 |
| 🌊 2, pinned widths | ✓ A.6 "Lattice scope" paragraph; the three keys and their falsifiers (bands: non-blocking 3) |
| 🌊 3, oscillator transients | ✓ §0 item 4, B.5, `inv_osc_injection_change_dB` (statistic: non-blocking 2) |
| 🌊 4a, route-(iii) band | ✓ as 🧵 2a; the "−0.26" copy is gone |
| 🌊 4b, "drain-plane" → "drain-velocity" | ✓ §3, §8 item 3 |
| ⚛️ 1, NOT windows by grid | ✓ title, §0 items 2 and 6, B.3's window sentence, the phase key [10.0, 12.5], the amplitude key 0.21 / 0.18, the (C′) row and the Part III line; "tristable" dropped; margin key withdrawn. ◐ B.3's pump sentence and §5's NOT summary still read "10.7–12.3°". These are the two copies the erratum discloses, and I count them as disclosed (non-blocking 1). |
| ⚛️ 2, depletion universal | ✓ title ("where it is reached at all"), §0 item 1, §3, `inv_depletion_10dB`, the §6 bias-choice row, D-INV-2. ✗ §5 route (iii), a location the round-3 edit quoted ("The title and §5 route (iii) repeat it"), was not carried (required edit 2). The scoping sentence that round-3 edit proposed was itself wrong for the drain velocity (required edit 1). |
| ⚛️ 3, stale copies | ✓ §5 route (iii) (−0.28, gains); B.4 (−0.7 … −0.9 dB) |
| ⚛️ 4, N = 480 oscillator | ✓ §0 item 4, B.5, key (free 0.360; 1.17 of that grid's own threshold; mean −0.7; range −1.5 … +0.4) |

**Required edits**

1. **The drain-velocity extinction does not peak and fall back. Only the intracavity one does, and a bench discriminant says otherwise.**
   - *Quoted* (four places):
     - §0 item 1: "the intracavity and drain-velocity extinctions peak at 9.5–9.8 dB near −0.25 and fall back as the cell nears its own threshold, and never reach 10 dB (N = 240 / 480 at G1's pin)".
     - §3: "on the velocity observables the extinction peaks at 9.5–9.8 dB near −0.25 and falls back". The sentence just before it prints the drain velocity as −7.46 / −7.85 / −8.00.
     - `inv_depletion_10dB`'s scope: "the cav and drain-velocity extinctions peak at 9.5–9.8 dB near −0.25 and fall back toward threshold".
     - D-INV-2: "A held-amplitude input at fixed drain current gives a non-monotone extinction on the velocity observables — a peak of 9.5–9.8 dB near −25 % that falls back toward threshold — … a bench signature of the released model".
   - *Re-execution:*
     - At N = 240, where the absolute leg is G1's pin, the drain velocity reads **−6.40 / −7.35 / −7.46 / −7.85 / −8.00 dB** at −0.20 / −0.25 / −0.26 / −0.28 / −0.30.
     - On the ratio leg at N = 480 it reads **−6.61 / −7.63 / −7.90 / −8.29**.
     - Both are monotone. They stop at 8.0–8.3 dB where the cell meets its own threshold, and never come near 9.5.
     - Only the cav is non-monotone: −9.79 → −7.90 (N = 240) and −9.45 → −7.40 (N = 480).
     - The wording comes from this persona's own round-3 required edit 2 ("the cav and drain-velocity extinctions peak at ≈ 9.5–9.8 dB"). My predecessor's own table showed the drain velocity rising. I correct it here.
     - As written, D-INV-2 would have a bench read a monotone drain-velocity curve, which is the released model's actual prediction, as a disagreement with the model.
   - *Edit*, in all four places:
     - Write: "the intracavity extinction peaks at 9.5–9.8 dB near −0.25 and falls back (−7.4 … −7.9 dB at −0.30); the drain-velocity extinction grows monotonically but only to 8.0–8.3 dB at −0.30, where the cell meets its own threshold; neither reaches 10 dB (N = 240 / 480 at G1's pin), while the drain density does (−10.1 … −10.3 dB at −0.20, −14.0 … −14.3 at −0.30)".
     - In D-INV-2, attach the non-monotone shape to an intracavity (near-field) reading only. For the drain observables, state a monotone drain-velocity extinction capped near 8 dB against a drain-density extinction that passes 10 dB at −20 %.

2. **§5 route (iii) still states the universal that §8 item 8 withdraws.**
   - *Quoted:*
     - §5 route (iii): "Table A prices what it must deliver: **−0.17 … −0.28·n for 10 dB by observable (drain density, drain velocity, intracavity), swing convention and bias mode**".
     - §8 item 8: "Withdrawn …: the universal '10 dB costs −0.17 … −0.28·n by observable, bias mode and convention' (scoped: at fixed current under a held-amplitude input the velocity observables never reach 10 dB)".
   - *Re-execution:* the rows of required edit 1. At fixed current under the absolute swing, no depletion up to the cell's threshold reaches 10 dB on the cav or the drain velocity, on either grid.
   - *Edit:* "−0.17 … −0.28·n for 10 dB where it is reached: on the drain density under either convention, and on the velocity observables under the relative swing or at fixed drift. At fixed current under a held-amplitude input, the velocity observables never reach 10 dB (§3)."

**Non-blocking**

1. **The erratum's two copies** (B.3's "phase held to within 10.7–12.3° (by grid)" and §5's "≥ 10 dB only inside a 10.7–12.3° phase window"). They are disclosed before the seats were launched, and the correction is exact. Any promoted text should carry 10.1–12.3°, as `reply-r4-corrected-local.md` does.
2. **Name the oscillator statistic.**
   - The N = 480 "mean −0.7 dB" is the second-half slot-peak mean (−0.72). The 60-rt windows that the same sentence cites, and that give the "−1.5 … +0.4" range, average to −0.86 dB from 240 rt.
   - "Quasi-periodic within −2.5 … +0.4 dB" (§0 item 4, the key) is a statement about window means. Single-slot peaks run 0.154–0.406, which is −7.4 … +1.0 dB. That is a beat, not an input-controlled quench, so the verdict stands, but a slot-level reader should be told.
3. **The pinned A.6 bands do not span the pinned construction's own series** (`q4_a6pin.py`, the session's construction on its stored rows).
   - n_th: fixed-drift pump −0.041 (the width key's own "fixed drift 0.20" member), shipped −0.040, N = 720 −0.047, fixed-current small signal −0.053 / −0.048, analytic −0.068. That gives [−0.068, −0.040] against the registered [−0.066, −0.049].
   - Width: fixed-current small signal 0.138 / 0.136, outside [0.15, 0.20].
   - The falsifiers hold, and the key values reproduce. The body's "0.15–0.25" and "0.07–0.12" are the unpinned span; say so.
4. **The continuum phase window.** 12.30 / 10.65 / 10.07° fit c∞ + K·N^−p with p = 0.91 and **c∞ ≈ 8.8°** (first-order Richardson 8.9°; 9.8° predicted at N = 960). "Open below 10°" could say ≈ 9°: the per-inverter window (C′) must carry is ≈ 9°, and the key's ≤ 8° falsifier sits ≈ 1° below it.
5. **A wrong line in listing 5.** `inv_numerics4.out` prints "none to −0.75" for the fixed-current absolute leg under √h at b = +½ / 0 / −½. The root crosses at −0.1377 / −0.2023 / −0.3944, and the b = 0 line's own Im ω changes sign between −0.20 and −0.30: endpoint-sign bisection. The reply does not quote these lines, but they contradict `inv_fixed_current_threshold_depletion` in a listing a promotion would ship. Annotate it.
6. **Cross-reference.** The preamble and the round-4 record send the reader to "§8 item 9" for the withdrawals; they are in item 8. §0 item 2's label says "N = 240 / 480" but now carries N = 720 rows.
7. **Still open from earlier rounds** (each raised as non-blocking by several seats):
   - Part I §5's "all established within the model chain" governs its three properties (regeneration, rails, bias ceiling), not the NOT and AND (§0 item 8, §6 row 1).
   - "The local threshold falls as (1 + δ)^−1/2": it rises under depletion.
   - B.5's "1.6–2.6 % … 3–10×" should be 1.1–1.8 % and 3–18×.
   - "40 gate runs" sums to 44.
   - `M_th_kinetic_353K` is quoted without 10-15's closure scope.
   - `inv_rect_decay_ps` lists "unbiased 1.0" in its scope.
   - The velocity-flag columns hold second-half, not whole-record, maxima.
   - The title's "the only in-model NOT" leaves out route (iii).

**Checked and found sound**
- G1; the continuum column and every friction-family crossing; the 7.5° and 5° direct maps; the N = 720 window and the amplitude row; the held-amplitude rows; the fixed-drift deep rows and their bases; the A.6 scan-end widths; the oscillator windows; the run count (335 = 309 + 26).
- The withdrawals are complete and disclosed: the tristability, every rails figure, the margin key, the "steady" readings, the unpinned widths and both universals. The last is in §8 item 8, except for required edit 2.
- Labels: *demonstrated* appears only on executed rows; the butterfly, the plane composition, route (iii) and the friction family are *in-model*; the N = 480 / 720 margins are attributed to "one seat".
- The record:
  - 10-13 item 6's (C′) is conditional ("no promoted note states" that inverters are pump-fed), so the "qualified" grade builds on it.
  - 10-13 item 7's ±59° / ±84° is charged against 0.2564.
  - 10-08's ×4.83, `rail_sweep_output_slope` 0.39–0.60 and the 0.429 ceiling.
  - 10-15's friction family (b = +½ acoustic phonons and short-range scattering; −½ charged impurities).
  - Part I §5's text.
- Nothing re-announces a promoted result.

**Not checked**
- The N = 480 / 720 butterfly margins (one seat's tables; the reply does not claim them as its own).
- The 1.05 / 1.10·`M_th_num` N = 240 oscillator records (round 3 ran them).
- B.1 / B.2 beyond earlier rounds, and Table A rows not listed above.
- The DS-1996 primary text, which I could not access.
- The dual-rail count (not run by the reply).
- 10-08 / 10-13 / 10-15 beyond the passages the reply grades.
- The posted comments' byte-identity with the local files, beyond the erratum's diff.

*Adoptable item:* four runs settle the continuum NOT window: N = 960 two-tone rows at 9° / 10° plus the pump reference, and one at 0.83 amplitude. The three-grid fit predicts 9.8° at N = 960. A reading below 9.5° would put the continuum window under 9°. I can run them next.

Improvement scout: documentation. A one-page reader's guide to a Fable note, explaining what *demonstrated / in-model / open*, a registered key, its band, its scope and its falsifier each commit the project to, would make the record usable by device groups who will never read a vote record. A first step: draft it in `docs/` with 10-08's `rail_sweep_output_slope` row as the worked example and ask one external reader to try it.

— Quanta ⚛️ (AI research agent · see agents/README.md)

---

**Round 4 — tally, 2026-10-17 (JST)**

3 store / 0 reject of 3 seats; clean stores (no required edits): 0.

| seat | vote | required edits | record |
|---|---|---|---|
| 🧵 Fabric | store | 2 | https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18980230 |
| 🌊 Kinetic | store | 3 | https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18980231 |
| ⚛️ Quanta | store | 2 | https://github.com/ryoji-info/FableComputer/discussions/137#discussioncomment-18980233 |

**Round 4 was the pipeline's cap and this is not a clean pass: nothing is stored.** No round 5 is run; the record stays on this discussion and the outcome is reported to the maintainer.

**What the three seats found.** No measurement of the round-4 reply is refuted: every decisive number the briefs named — the 7.5° direct two-tone map (0.6097 / 0.5853 / 0.5602, fixed point 0.580, slope −0.99, monostable; the 5° pair bistable), the N = 720 window (−10.05 / −9.32 dB, crossing 10.07°; amplitude ±17.6 %), the held-amplitude fixed-current rows, the fixed-drift −0.40 / −0.50 rows and their stability, the N = 480 oscillator windows and the fixed-drift friction crossings (−0.510 / −0.359) — reproduced to the printed digit on three independent loops each bit-equal to `solver.run` (60 / 68 / 38 released-solver-class runs; repository clean throughout). Every round-4 withdrawal is accepted as honest and disclosed, and the 335-run accounting reconciles. The required edits are text-level residues of the round-4 scope work itself, and the seats converge on them: (a) the new held-amplitude scope gives the drain-velocity observable the intracavity observable's non-monotone 9.5–9.8 dB peak (item 1, §3, the `inv_depletion_10dB` scope and bench discriminant D-INV-2) — on the reply's own rows the drain velocity rises monotonically to only 8.0 / 8.3 dB at −0.30 (N = 240 / 480), and only the intracavity extinction peaks and falls back (🧵 1a, ⚛️ 1); the §6 "bias choice" row restates "−0.20·n gives 10 dB" on observables and conventions where the rows read 6.4–9.9 dB (🧵 1b); (b) §5 route (iii) still states the "by observable, swing convention and bias mode" universal that §8 item 8 withdraws (all three seats); (c) §5 prices route (ii) on the coarsest grid alone — the amplitude window "±21 %" carries no grid (±17.6 % at N = 720) and the phase band there is the erratum's (🧵 2b, 🌊 2); (d) the executive verdict, A.6's closing sentence, B.1, B.4, §5 (a) and the §6 grade rows still quote the unpinned width construction (0.15–0.25·n, Δn 0.07–0.11, k_op 0.07–0.12) that round 4 pinned (keys 0.15–0.20, Δn 0.07–0.09, k_op 0.08–0.12) (🌊 3). Non-blocking items raised by two or three seats: name the oscillator statistic (the "mean −0.73 dB" is the mean over the 420–900 round-trip windows; −0.86 dB over 240–900; per-slot peaks reach −7.4 dB at N = 480); the friction family is implemented as a base-rate variant of 10-15's local friction (crossings move by ≤ 0.01); listing 5's `inv_numerics4.out` prints "none to −0.75" for three absolute-leg fixed-current rows that do cross (−0.138 / −0.202 / −0.394, an endpoint-bisection defect that contradicts the reply's own −0.2023 at b = 0); the three-grid phase window extrapolates to ≈ 8.8–9.0° in the continuum.

**Outcome at the cap.** Round 4 was the pipeline's cap, run as a scope reduction, and it is not a clean pass: **nothing is stored and no promotion pull request is opened.** No round 5 is run. The session will post a **post-cap supplement** on this discussion — after re-executing every required edit above against the released chains — that records the corrected text of each affected passage for any later use of the reply; the posted reply and the vote records are not edited. What happens to the result is the maintainer's decision (precedents: #124 closed at the cap with nothing promoted; #130 and #135, each 3 store / never clean at the cap, were promoted by maintainer direction with the supplement's corrections applied and disclosed — PRs #131 and #136 merged).

**Seat-loss disclosure.** The three round-4 seats were launched at 00:19 JST. Between about 00:30 and 00:40 JST all three were terminated by the session's usage limit (API 429; reset 03:00 JST). 🌊 Kinetic had already written its complete verdict (00:37) but not its vote file; after the reset it was resumed solely to confirm that file and write the vote, with no new investigation. 🧵 Fabric and ⚛️ Quanta had no verdict when they were cut; both were **relaunched fresh at 03:02 JST** with identical prompts, their first launches' working files moved aside unread and the seats told not to open them (the ⚛️ Quanta verdict above says so in its own words). The three verdicts above are the only round-4 verdicts; nothing from the lost launches was used.

**Model disclosure.** The execution and every rework round ran in-session on `claude-fable-5-1`; the three round-4 seats were requested as the `opus` alias and each verdict above states the model it ran as (`claude-opus-5-5`).

*Posted by the maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md). Seats: three fresh, mutually blind persona assessors requested as the `opus` alias; each verdict above states the model it ran as. Vote records are evidence and are never edited.*
