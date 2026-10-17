# Can the released cell be a parametron? Yes in-model, in narrow windows: pumped at 2f₀ it is a phase-sensitive amplifier (8.7–9.3 dB of contrast at a 5 % source-clamp pump on the ratio leg, N = 720–240; restoring slope 0.46–0.49 at knee-level swings inside the velocity domain, only 0.76–0.87 at the delivered '1' under 1–2 % pumps) and, above an onset of 0.21–0.23 (source clamp, N = 240) or 0.70–0.72 (drain current, N = 240, rising with refinement to (0.72, 0.80] on N = 720), a latching parametric oscillator that holds and re-levels a bit under a CW pump; gated in 07-31's slot at drain 0.85 it amplifies a bit stream's flips ×1.75–3.15 over an unpumped cell on every grid but re-levels none — the level keeps the previous bit at every input run

**Status:** promoted 2026-10-17 **by maintainer direction** after the pipeline's round-4 cap (the 2026-08-02 / PR #98, 2026-10-09 / PR #131, 2026-10-16 / PR #136 and 2026-10-17 / PR #138 precedents) — the round ladder ran 3-of-3 store with 4 / 3 / 3, 2 / 2 / 1, 1 / 1 / 1, 2 / 1 / 2 required edits (🧵 / 🌊 / ⚛️ order), never a clean pass; no round refuted a measurement. 12 assessor seats plus two pre-publication check seats; every claimed defect was re-executed by the session before it was accepted (rework records: [round 2](https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18991859), [round 3](https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18992597), [round 4](https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18993160)); no required edit was declined in any round. **This note's text is the round-4 reply (posted in two parts for length: [part 1](https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18993161), [part 2](https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18993163)) with the corrections of its [post-cap supplement](https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18994632) applied (the round-4 seats' five required edits and the accepted non-blocking items, each re-executed and listed there; 39 exact replacements by `apply_r4_supplement.py`, [listing 8](https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18994636)), disclosed here as posted**; the earlier replies and every vote record stand unedited. Full verbatim records: [discussion #142](https://github.com/ryoji-info/FableComputer/discussions/142). Contests **no** `results.json` value; moves **no** promoted key; corrects no promoted note — it grades three and qualifies them, and they receive dated post-promotion annotations in the same PR ([08-05](2026-08-05-idler-added-noise-and-the-nf4db-requirement.md), [10-13](2026-10-13-phase-is-not-the-easier-half-for-the-cell.md), [10-16](2026-10-16-no-density-route-to-a-not-in-the-released-cell.md)); Part II §7(ii) and Part III limitation 24 are manuscript claims, graded in §7. **Scope, stated by the text itself:** every result is about the released Galilean shallow-water cell; the amplifier's admissible window is grid-scoped and narrows under refinement; the drain onset rises and the latched level falls with refinement, their continuum values open; the gated latch amplifies a bit stream's flips but re-levels none.

**Prompted by:** [Fable Session — 2026-10-17, discussion #142](https://github.com/ryoji-info/FableComputer/discussions/142) (🧵 Fabric's winning prompt, 2-of-3 — 🌊 Kinetic → Fabric, ⚛️ Quanta → Fabric; 🧵 Fabric → Kinetic; [candidates](https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18990509)).

**Correction history, disclosed.** Two pre-publication check seats (both REVISE; [record 1](https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18990510), [record 2](https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18990513), [dispositions](https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18990514); every item re-executed, one declined on measurement) refuted the first draft's gated-parametron 11/15 as an edge-leak artifact and corrected the pump-phase error model, the N = 720 window and the timing normalisation. Round 1 found the gated plateau's sign to be the input's own and three flips below the pump's edge-seeded state, the pump's depleting drain DC against 10-16's `inv_rect_sign`, the window's continuum scope and weak in-domain restoration at the delivered '1'. Round 2 found that no gated flip re-levels, also on an exact 15-period slot, that the from-rest control carried the pump's own self-seed on the bit's side, that the density sign count depends on its reference phase, and that the 2 % pump at the delivered '1' leaves the domain on N = 720. Round 3 found that the gated negative rested on one input (2×10⁻³) — at 4–6×10⁻³ every flip clears 0.9 of the latched level inside the domain — and that the delivered '1' rows on the ratio-leg grids had run at the absolute leg's swing. Round 4 found that the gated window's grid trend was its per-grid reference's — an unpumped cell meets the same criterion at larger inputs — that the window was a ratio-leg statement, and that the drain onset rises with refinement while the latched level falls; the post-cap supplement applies these. **Executing model:** at the maintainer's direction every seat of this run — the candidate, vote, check and assessor seats — and the execution and every rework round ran on `claude-opus-5-5` (Opus 5.5), including the seats the routine assigns to Fable 5.1.

---

## 0. Executive verdict

1. **The answer.** *In-model (released Galilean cell, retuned configuration, 353 K, a 2f₀ drive at one of its two clamps — the two time-dependent inputs the released code passes its step).* A 2f₀-pumped released cell **restores phase-encoded bits as a sub-threshold phase-sensitive amplifier through the source density clamp, inside the velocity domain only in a narrow window**. Above an onset on either clamp it is **a latching parametric oscillator that holds and re-levels a bit under a CW pump**; the drain-route latch lies inside the domain run-wide, the source-route one only at steady state. The drain onset rises and the drain latch's level falls with refinement, without converging on the grids run, so their continuum values are open. Under a 5 % source pump the amplifier restores at knee-level swings (to 0.0095 on N = 240 / 480, below a swing between 0.0085 and 0.0095 on N = 720, and at or below the knee band's bottom in the continuum by extrapolation). At the delivered '1' restoration is weak (slope 0.76–0.87 under 1–2 % pumps), and where it stays inside the domain depends on the swing within 10-08's F = 2 band: a 2 % pump keeps the ratio leg's own point (0.0189 / 0.0186 on N = 480 / 720) inside (run-wide 0.424 / 0.423), while the absolute leg's 0.0197, run on every grid, crosses the ceiling on N = 720 by 3.4×10⁻⁴ in its switch-on transient and stays inside there only under 1–1.5 %. Gated with 07-31's slot window at drain 0.85 (ratio leg), the drain-route latch **amplifies a bit stream's flips but re-levels none**. At 4–6×10⁻³ its flips are ×1.75–3.15 those of an unpumped cell with the same input, on every grid, with 15/15 signs above the pump's own edge-seeded state; against one fixed level (N = 240's CW latched 0.0183 on the drain velocity) every flip clears 0.9 from between 4 and 5×10⁻³ on every grid, where an unpumped cell needs 9×10⁻³. But the level keeps the previous bit at every input run (a flip ends at 0.55–0.75 of a repeated bit, against 0.80–0.92 unpumped). The per-grid criterion of round 4 — every flip ≥ 0.9 of that grid's own CW latched level — is withdrawn: it is an amplitude threshold on a level that falls with refinement, and an unpumped cell meets it at 9 / 7 / 6×10⁻³ on N = 240 / 480 / 720. On the N = 480 absolute leg no ladder input clears it inside the domain. The inputs carry 6–14 quanta, whose ideal antipodal error at 353 K is 0.10–0.03 (*in-model*; the runs are noiseless). At 2×10⁻³ (N = 240) the latch re-levels none of nine flips, and there the plateau's sign is the input's own, as through an unpumped cell.

2. **Phase-sensitive gain exists, and the bias makes it** (*demonstrated*, Table P, signal 2×10⁻³, 320 round trips).
   - **Source-clamp pump** of 0.02 / 0.05 / 0.10 of the density: contrast **4.11 / 9.33 / 14.40 dB** on the drain velocity and 4.29 / 9.70 / 14.88 dB on the drain density; run-wide max|hu/h| 0.18 / 0.22 / 0.31.
   - **By grid** at 0.05 on the ratio leg: **9.33 / 8.93 / 8.72 dB** (velocity) and 9.70 / 9.18 / 8.94 dB (density) at N = 240 / 480 / 720 (on a non-aliasing five-phase set ≈ 0.08 dB higher — one round-1 seat: 9.41 / 8.80 dB on the velocity).
   - **Passive twin** (M = 10⁻⁹): **3.13 dB on the density**, against the biased cell's 9.70. The bias triples the parametric contrast in dB (|B|/|A| ×2.86).
   - **Drain-current pump** of 0.1 / 0.2 / 0.5 of u₀: **3.08 / 6.24 / 16.53 dB on the drain density**. The drain velocity reads 3.73 / 7.54 / 19.68, but the pumped current clamp multiplies that observable. The 0.5 row is already a large-signal reading at 2×10⁻³, 10.4 % off the bilinear form.
   - **The pump's own rectified shift** is −3.4×10⁻⁴ of the mean density at 0.05, i.e. −1.7×10⁻⁴ of f₀ under √h. At the drain it **depletes**: ⟨h(1)⟩ − 1 = −7.35 / −5.99 / −5.53×10⁻⁵ (N = 240 / 480 / 720) under the 0.05 source pump alone, −2.72×10⁻⁴ at 0.10 and −2.46×10⁻⁴ at the 0.5 drain pump, while the passive twin accumulates (+7.53 / +5.74×10⁻⁵ on N = 240 / 480). At first order in 1/N the depletion survives refinement (≈ −4.6×10⁻⁵) and the twin tends to ≈ +3.95×10⁻⁵. That meets 10-16's `inv_rect_sign` falsifier as worded (§7). Per unit a² it is ≈ 1,500× weaker than the carrier's accumulation, and it opens no density route to a NOT.

3. **One cell restores phase; a chain of them does not accumulate the error** (*demonstrated* rows, *in-model* composition).
   - **Slope at the amplified axis.** The pump phase is set so the small-signal amplified axis sits at input phase 0. Under the 0.05 source pump the output-phase slope there is 0.458 (knee 0.0095, N = 240), 0.486 (knee, N = 480 ratio leg), 0.491 (0.0085, N = 720 ratio leg), 0.509 (`A_fix`) and 0.558 / 0.555 (delivered '1', N = 240 / 480).
   - **Symmetry.** The 0 and π states are mirror images to ≤ 8×10⁻⁷ — the half-period identity, a steady-state check rather than a result.
   - **Composition** through 10-08's plane assumption: a per-cell phase error δ settles to a fixed offset ≈ 0.84 δ leaving a cell and ≈ 1.84 δ arriving at the next (knee slope, linearised), instead of accumulating (on the drain density, the plane 08-02 item 4 composes on, the knee slopes are 0.426 / 0.460 on N = 240 / 480). The chain slips only when δ exceeds the largest φ − ψ(φ), **19.2° at φ = 55°** (5° rows, on the binding side). That is of the order of 10-13's single-cell ±15°, not its composed ±0.32 … ±0.010 % per cell.
   - **Admissible window, by grid** (source pump 0.05).
     - Inside the domain to the knee midpoint 0.0095 on N = 240 / 480 (run-wide 0.406 / 0.424); on N = 720 only below a swing between 0.0085 (0.422) and 0.0095 (0.432).
     - The edge falls with refinement. At the knee band's bottom (0.0076) the run-wide maximum is 0.380 / 0.402 / 0.411 on N = 240 / 480 / 720. A first-order extrapolation from the two finest grids puts the knee midpoint outside the domain in the continuum (≈ 0.446; one seat's fitted order gives 0.454) and the band's bottom at its edge (≈ 0.428; 0.442 fitted). *In-model:* in the continuum the 0.05-pump window lies at or below the knee band's bottom.
     - `A_fix` and the delivered '1' are outside (0.447 / 0.483 on N = 240; 0.489 on N = 480).
     - **At the delivered '1', weaker pumps restore weakly; whether they stay inside the domain depends on the swing.** The rows at 0.0197 — the absolute leg's CW F = 2 point (10-08 §3), run also on the ratio-leg grids — give, under 0.02, slope 0.771 on N = 240 (run-wide 0.425), 0.767 on N = 480 (0.4285, inside by 4.2×10⁻⁴ — a knife-edge) and 0.766 on N = 720 (**0.4293 †**, outside by 3.4×10⁻⁴ in its start-up transient; late window 0.418; first order from the two finest grids ≈ 0.431). On N = 720 only weaker pumps keep 0.0197 inside: slope 0.817 at 0.015 (0.4165) and 0.873 at 0.01 (0.403). At the ratio leg's own points (10-08's key: 0.0189 on N = 480, 0.0186 on N = 720) the 0.02 pump stays inside: slope 0.763 / 0.760, run-wide 0.4237 / 0.4227, inside by 5.2 / 6.2×10⁻³ (`psa_r4f.py`, `psa_r4.py`; 0.0186 on N = 480: 0.762, 0.4219; 0.0189 on N = 720: 0.762, 0.4246). Within the F = 2 band the domain edge moves more with the swing (≈ +0.006 per 10⁻³) than with the grid (+0.0008 from N = 480 to 720 at fixed swing). Each axis comes from its own small-signal pair.
     - **The '1' window's margins.** On its 45° lattice point the 0.02 row's slip margin is ≈ 6°, below 10-13's single-cell ±15°; one round-2 seat's scan gives 6.02° at 45° against 5.41° at 30° and 4.40° at 60°, with the basin edge near 76°; on N = 720 the 1.5 % row's lattice margin is ≈ 4.2° (4.18 / 4.24 / 2.35° at 30 / 45 / 60°, one round-3 seat). Composed (*in-model*), slope 0.87 / 0.77 leaves 6.9 δ / 3.4 δ and delivers 7.9 δ / 4.4 δ to the next cell, so a 10.1° arriving budget needs δ ≤ 1.3° / 2.3° per cell, against the knee's 5.5° (`psa_r3_arith.py`).

4. **A parametron proper exists in the released equations** (*demonstrated*, §3).
   - **The state.** Above onset the pump-only cell oscillates from noise at exactly f₀: the f₀ phasor's phase is stationary to ≤ 0.01° over 80 carrier periods. It sits in one of two states 180.00° apart. At drain 0.85 the sign of a 2×10⁻³ seed selects the state; at source 0.25 such a seed, switched off after 20 rt, loses to the pump's own turn-on state at the four phases run, and only a ×10 or a longer-held seed selects the other one (180.0000° apart, same level; one round-3 seat). The amplitude does not remember the seed (**1.000** for a ×10 seed on steady rows; that row's start-up runs at 0.529 †, late window 0.318).
   - **Onsets, bracketed from both sides on N = 240.**
     - Source clamp **(0.21, 0.23]** of the density: Floquet multiplier 0.98198 at 0.20 and 0.9906–0.9910 at 0.21 (§3, per-row agreement), decaying at 0.21 and latched at 0.23 in the time domain. The 0.23 row also latches on the N = 480 ratio leg.
     - Drain current **(0.70, 0.72]** of u₀: 0.70 decays on 600-rt records, and on 1,800- and 2,400-rt records by both check seats; 0.72 latches at 1,800 rt. On the N = 480 ratio leg 0.75 and 0.80 latch on 1,200-rt records (6.588 / 10.488×10⁻³, stationary in amplitude and phase) and 0.70 decays (6.14 → 4.69×10⁻⁴ over the last 70 periods, `psa_r4c.py`), so that grid's bracket is (0.70, 0.75], with the |Z|² intercept at 0.717. On the N = 720 ratio leg 0.72 decays, 0.75 is still relaxing after 1,200 rt and 0.80 latches (6.856×10⁻³): (0.72, 0.80], intercept 0.755 (`psa_r4e.py`, `psa_r4f.py`); one round-4 seat finds ≈ 0.78 on N = 960 at an extrapolated bias. **The drain onset rises with refinement, and the drain-0.85 latched level falls (0.0183 / 0.0133 / 0.0100 on N = 240 / 480 / 720; 0.0077 on N = 960, one seat) without converging on these grids: their continuum values are open.**
   - **Amplitude law.** Drain: |Z|² linear in the pump with p_c ≈ 0.70 on N = 240, ≈ 0.717 on N = 480 and 0.755 on N = 720 (ratio leg). Source: √(p − p_c) only on the two rows nearest onset.
   - **Velocity domain.** **The drain-route oscillator lies inside it run-wide (0.272–0.317 at 0.72–0.85).** The source-route one is outside run-wide on every row run (0.590 / 0.626 / 0.697 † at 0.23 / 0.25 / 0.30 on N = 240; 0.630 † at 0.23 on N = 480) and inside only at steady state at 0.23–0.25 (0.38 / 0.42).

5. **Timing: restoration costs memory, and the gated latch amplifies flips but re-levels none** (*demonstrated*).
   - **Memory.** The Floquet multiplier of the amplified quadrature gives an amplitude memory of **7.8 / 6.9 ps at the 0.05 source pump on N = 240 / 480, against 5.5 / 5.7 ps unpumped**. It diverges toward onset.
   - **CW-pumped amplifier in 07-31's gated slot, at the knee (N = 240).** A bit that follows its opposite starts the slot at −0.59 of the steady mid-slot level. At the decision point it reaches +0.839 of the all-(+1) response at that instant, with a phase error of 8.4°; the sign is right in 9/9 such slots. The all-(+1) stream itself rises from 0.65 to 1.14 of its mid-slot level within the slot.
   - **The gated parametron** (drain pump 0.85, gated with the slot window), read on the last whole carrier period of the absolute-time grid inside the pump plateau (leak-free). **At an in-domain input of 2×10⁻³ on N = 240:**
     - The plateau sign follows the input in 15/15 slots on the drain velocity. On the drain density the count depends on the reference phase: 14/15 against the CW latched density phase (the velocity count's own reference) and 15/15 against the slot-1 plateau phase. Slots 2 and 12 lie at −0.004 … +0.011 of the latched density level there, undecided; they are P3's seed-and-residue-opposed flips (−P3 reads 15/15 on the density, smallest margin +0.035, one round-3 seat). One period earlier, also leak-free, the pumped cell reads 12/15 on both channels (slots 2 / 7 / 12 at −0.030 / −0.002 / −0.024 on the velocity) while the unpumped cell reads 15/15 (`psa_r4_arith.py`): in three flips the previous bit's sign persists until the plateau's last period.
     - **That sign is the input's own**: the same gated input through the unpumped cell gives 15/15 at 0.21–0.25 of the latched level (velocity).
     - After a repeated bit the state re-levels (1.13–1.26 of the latched level). After a flip it reaches 0.45–0.72 in five slots, 0.28 in one, and **0.06–0.09 in slots 2, 7 and 12** — below the unpumped cell's own response and below the pump's own edge-seeded f₀ state in the same window (0.12–0.16, opposite to the bit). **No flip re-levels: 0/9 reach 0.9.** In those three slots the sign is not robustly decided (on the density, slot 2 reads wrong against the CW latched phase).
     - **At 2×10⁻³, from rest the window re-levels only when the pump's own edge-seeded state agrees with the bit.** P3's slot 0 starts with the self-seed on its side (+0.23) and reaches 1.06 (1.15 on a 15-period slot). The sign-reversed pattern −P3 starts against it and reaches 0.65 (0.76). Any opposing initial state limits the build-up: the self-seed alone suffices, and an opposing residue deepens it (flips 0.06–0.72 on P3, 0.10–0.78 on −P3).
     - **The self-seed's sign** alternates per slot on 07-31's 14.49-period slot. On an exact 15-period slot it keeps one sign (0.23) and so opposes every bit of the other value (flips 0.20–0.88 on P3, 0.20–0.87 on −P3).
     - **At 2×10⁻³ on N = 240 it re-levels after no flip within the 11.6-ps window (0/9 on either slot length and either pattern), and on 07-31's slot it does not robustly decide three of nine flips.** Against N = 240's latched level the same count holds on N = 480 / 720 (0/9); against each grid's own, smaller level it reads 1/9 and 4/9 (P3) / 2/9 (−P3) — the reference's trend, not the cell's.
   - **At larger inputs the pump amplifies the flips; it does not re-level them** (`psa_r4b.py`, `psa_r4e.py`, `psa_r4f.py`; R.4's swing table). At 4–6×10⁻³ on the ratio leg the pumped flips are ×1.75–3.15 the unpumped cell's at the same input and grid, with 15/15 signs above the pump-alone state, inside the domain (run-wide ≤ 0.425 on N = 480 / 720; 6×10⁻³ leaves it on N = 240). Against one fixed level, N = 240's 0.0183, every flip clears 0.9 from between 4 and 5×10⁻³ on every grid (0, 1, 5, 9, 9 of 9 at 2–6×10⁻³ on each; from rest against the self-seed 1.74 at 5×10⁻³); in absolute units the pumped response is grid-stable to ≈ 10–13 %. An unpumped cell needs 9×10⁻³ for the same on N = 240. The level is history-dependent in both cells, more so pumped (a flip ends at 0.55–0.75 of a repeated bit, against 0.80–0.92 unpumped), so neither re-levels a bit stream. Against each grid's own CW latched level — the criterion round 4 used — the count rises with refinement only because that level falls (0.0183 / 0.0133 / 0.0100), and an unpumped cell meets it at 9 / 7 / 6×10⁻³ on N = 240 / 480 / 720; that criterion is withdrawn. On the N = 480 absolute leg 4×10⁻³ lifts 5/9 flips of that leg's own level and 5×10⁻³ runs at 0.435 † (`psa_r4d.py`). One pump, one slot length per row, a single seed; 6–14 quanta per input (`psa_r4_arith.py`).

6. **The gate set under phase encoding** (*in-model* on executed rows, §5).
   - **Majority** reads the sign of the summed field. Its classes are separated by π in phase, not by an amplitude threshold, so the threshold 10-16 found absent is not needed.
   - **Re-levelling of the classes.** Compression brings the strong and weak classes to 4.6 dB apart. But (+++) at 3 × the knee leaves the domain (0.521), so an in-domain majority needs inputs ≤ ⅓ of the knee on N = 240 / 480, and ≤ ⅓ of the knee band's bottom (≈ 0.0025) in the continuum by item 3's estimate. One such unit is ≈ 3.8 quanta (2.5 at the continuum bound), and the weak class (++−) carries one unit: its ideal antipodal homodyne error at 353 K is 0.15 (0.21), far from decision grade (*in-model*, `psa_r3_arith.py`).
   - **Input phase spread.** Worst-case spreads of ±30° and ±40° put the weakest class's sum at 60.0° and 70.0° from the axis; both restore (to 41.2° and 54.6°).
   - **AND and OR** need a constant input: a coherent f₀ reference.
   - **NOT** is a half-period (0.5-ps) delay, in-model ≈ 2.6 dB of passive λ_p/2 line at 353 K. A single delay error restores up to the basin edge (80–85°, ≈ 222–236 fs, ≈ 518–550 nm of passive line). A systematic error repeated along a chain is bounded by the slip margin (19.2°, ≈ 53 fs, ≈ 124 nm of line at the released plasmon speed, λ_p = 2.33 µm).

7. **The pump's bill** (*in-model*, §6).
   - **Energy.** By a source-plane mean-square proxy, the 5 % source pump costs ≈ 9× a delivered-'1' burst per slot (≈ 39× a knee-level burst).
   - **Heat.** It adds AC relaxation loss of 4.6 % of the DC drift loss; the parametron adds 24 % (drain 0.75) or 114 % (source 0.23).
   - **Phase tolerance.** A uniform pump-phase error leaves an offset of δ_p/2 and never slips: δ_p ≤ 20.2° (28 fs at 2 THz) keeps it within 10.1°. A cell-to-cell increment Δ_p must stay ≤ 11.0° (15 fs) for the phase arriving at the next cell, and the chain slips at ≈ 38° (53 fs).
   - **What #139 must supply.** A 2f₀ line phase-locked to the f₀ reference that AND/OR also need — two coherent lines instead of one — and a carrier referenced to absolute time. 07-31's window-centred carrier steps 177.4° per slot against a CW pump.

8. **What 10-16's verdicts are about.** *Graded, §7.*
   - **"No density route to a NOT"** is about the cell, and stands.
   - **"The only in-model NOT is destructive interference"** is about the amplitude encoding. Under phase encoding NOT is a delay and restoration comes from the 2f₀ pump. That family is restoring in-model but admissible only in a narrow window: knee-level swings under a 5 % pump (at or below the knee band's bottom in the continuum, in-model), and weak restoration at the delivered '1' (slope 0.76–0.87 under 1–2 % pumps, the domain edge set mostly by the swing within 10-08's F = 2 band). A drain-route latch holds a bit (CW); gated in 07-31's slot at drain 0.85 it amplifies a bit stream's flips ×1.75–3.15 over an unpumped cell but re-levels none: the level keeps the previous bit at every input run.
   - **10-16's `inv_rect_sign`** (accumulating, falsifier "any drive in the domain at which ⟨h(1)⟩ − 1 < 0") is qualified: it stands for the carrier-frequency inputs it measured, but a 2f₀ drive at either clamp depletes the biased cell's drain DC, which meets the falsifier as worded. No NOT route follows.
   - **08-05's "no phase-sensitive escape"** is confirmed within its DC-drive scope and qualified outside it.
   - **10-13's Table C row** ("named, not derived") is now derived.
   - **Part II §7(ii)'s amplifier clause** is confirmed for both readings, gate and drift.
   - **Part III limitation 24** is explored, for amplification only.
   - **Quanta's single-mode estimate** is qualified.

---

## 1. Gates (`psa_gates.py`, `psa_lin.py`, `psa_floquet.py`, `psa_floquet2.py`)

| gate | result | standard |
|---|---|---|
| G1: `run_psa` against released `solver.run` (shipped; three runs: CW 0.0197 N = 240, `none` N = 240, CW N = 480; 20 rt) | t / drain / cav **bit-equal** over 31,638 / 31,638 / 63,276 steps; the general signal expression vs the released one: max diff 0.0; re-checked bit-equal after the later patches of §10 (`psa_g1post.py`, printed) | bit-equal |
| G2a: `M_th_num` by run_all's `measure_Mth_num` path (copied; 8 runs of 90 rt) | 0.16894319463373791 — **bit-equal** to results.json | printed digits |
| G2b: `cw_regen_gain_dB_at_0p7` = `regen.cw_net_gain_dB(0.7)` | 9.66100611708918 — **equal** | printed digits |
| G2c: 10-16's G2 row (retuned, absolute leg, CW 0.0197, 240 rt, slot-peak `cav` over the same-drive passive cell) | **6.520 dB** (printed 6.520) | printed digits |
| G3a: zero pump | \|B₀\|/\|A₀\| = 1.2×10⁻⁷ at 160 rt (6.8×10⁻¹¹ at 320 rt, check seat 1); A₀ = 2.46593 per unit at +74.911° | roundoff / nonlinear residual |
| G3b: time translation — signal +θ with pump +2θ rotates Z by e^{iθ} (θ = 40°) | relative residual 1.98×10⁻⁴ at 160 rt, inside that record's own steady-state change (3.1×10⁻³); 1.2×10⁻⁵ at 320 rt (check seat 2) | steady-state level |
| G3c: amplitude dependence under the 0.05 source pump (320 rt, steady 3.6×10⁻⁶) | per unit \|A\| 2.7231 at 1×10⁻³ against 2.6733 at 2×10⁻³ (**+1.9 %**); \|B\|/\|A\| 0.5008 against 0.4910. **The pumped cell is ≈ 2 % into compression at the record's 2×10⁻³ "small signal"**; an a² extrapolation from the two amplitudes puts the a → 0 contrast ≈ 0.3 dB higher (≈ 9.6 dB; an extrapolation, labelled). On 0 / 120 / 240° the bilinear residual is 0.09–0.13 % (check seat 2), but there two third-order terms nearly cancel: a five-phase fit gives |C|/|A| = 6.9×10⁻³, |D|/|A| = 5.9×10⁻³ and a 0.8 % bilinear residual (one round-1 seat), consistent with the ≈ 2 % compression. The drain 0.5 row is 10.4 % off the bilinear form (`psa_rework.py`) | departure measured |
| pump-only f₀ residue (Table P) | 2.6×10⁻¹¹ … 2.2×10⁻⁶ on the in-domain rows below onset (3.3×10⁻⁵ on the out-of-domain 0.20 source row); subtracted | — |
| steady-state criterion: relative change of the complex f₀ phasor between the last two 20-period windows | ≤ 1.5×10⁻⁵ on every in-domain Table P row; ≤ 3×10⁻⁶ on Table R; 3.6×10⁻² on the 0.20 source row (not steady, and outside the domain) | stated per row |
| F1: the batched Floquet step against released `_step_LF`, row by row | **bit-equal** on every build | bit-equal |
| F2: periodicity of the pumped base, \|x(t + T_p) − x(t)\| / \|x − x_uniform\| | per row in §3 (1.0×10⁻⁵ … 2.2×10⁻³ for the multipliers quoted). Agreement with the check seats' independent builds on bases periodic to 10⁻⁸ … 10⁻¹¹, per row: ≤ 5×10⁻⁵ at source 0.05, source 0.10 (N = 480), drain 0.5 and drain 0.60; 2.1×10⁻⁴ at source 0.10 (N = 240); 3.8×10⁻⁴ at source 0.21 (check seat 2 and a round-1 seat's time-domain reading both give 0.99058); drain 0.2 unverified | stated |
| F3: zero-pump period map = eig(J)^m of the one-step Jacobian | max \|μ − λ^m\| over the top six 4.3×10⁻⁷; one-step fundamental f = 0.244537, Im ω = −0.045069 at cfl 0.4 exactly — **10-16 G5's printed retuned N = 240 row, to the digit** (first-order convergent to 10-16 G5's retuned continuum root 0.245422) | printed digits |

**Conventions.**
- **Configuration.** Retuned (L = 576.62 nm, f₀ₙ = 0.247350, τₙ at 353 K), cfl 0.4, seed 1. One time unit (L/s) is 0.2473 ps, so the carrier period is 1.000 ps, the pump period T_p is 0.500 ps and the slot is 14.49 ps.
- **Bias legs.** Absolute 0.118260 (equal to the ratio leg at N = 240); ratio 0.7·`M_th_num`(N), i.e. 0.111123 / 0.108898 at N = 480 / 720 (08-06's roots); analytic 0.102958.
- **Drives.** The signal is a_s sin(ωt + φ) at the source clamp. The pump is a_p sin(2ωt + φ_p), added at the source clamp, or multiplying the drain current clamp as u₀(1 + a_p sin(2ωt + φ_p)).
- **Observables.** The drain-velocity and drain-density phasors Z at f₀, each a least-squares fit over the last 20 whole carrier periods with DC and harmonics 2–4 in the basis (sin convention, y₁ = Im(Z e^{iωt})). Then Z(φ) − Z_pump-only = A e^{iφ} + B e^{−iφ}, the contrast is 20 log₁₀((|A| + |B|)/(|A| − |B|)), and the amplified axis is φ* = (arg B − arg A)/2 (mod 180°).
- **Velocity domain.** 10-08 limitation 10: max|hu/h| ≤ v_F/s = 0.429, quoted run-wide with the late window beside it. † marks a row outside it.

**The mapping the prompt asked to verify.** The released code passes its step two time-dependent inputs: `h_left`, the source density clamp, and `drain_current`, the drain current clamp. The step also takes the body force u₀ as an argument, which the released code holds constant. Modulating it at 2f₀ is a third route: in one round-1 seat's rows a body-force pump of 0.2 gives 0.51 dB on the drain density, and 6.08 dB with the drain clamp also modulated against 6.24 dB for the clamp alone, so the drift reading's coupling lives in the clamp. No other bulk term carries an external time dependence. In the gradual-channel reading n = C(V_g − φ)/e, a uniform V_g drops out of the bulk force and sets n(0) = C·V_gs/e at the grounded source. So a uniform top-gate modulation enters these equations only through `h_left`, the source-gate drive the released solver's docstring takes from Dyakonov & Shur (PRL 1993; the record has not read DS-1996, 10-16 limitation 5). That is *in-model*: a statement about the released equations' structure, not about a device. A pump acting on the bulk speed itself would need a term these equations do not contain (§6, smallest change).

---

## 2. Table P — the phase-sensitive transfer (`psa_tableP.py`, `psa_extra.py`, `psa_rework.py`, `psa_rework2.py`; signal 2×10⁻³, 320 rt, φ_p = 0)

| route, pump | leg, grid | \|A\| per unit (velocity), arg A | \|B\|/\|A\| (velocity) | **contrast, velocity / density** | axis φ* (velocity) | A/A₀ | max\|hu/h\| run / window (pump only) | 4-phase residual | pump-only DC (drain / mean) |
|---|---|---|---|---|---|---|---|---|---|
| none | abs 240 | 2.46593, +74.91° | 0 | 0 / 0 | — | 1 | 0.158 / 0.158 | — | — |
| source 0.02 | abs 240 | 2.51828, +76.68° | 0.2323 | **4.11 / 4.29 dB** | 94.86° | 1.021, +1.8° | 0.180 / 0.180 (0.141) | 3×10⁻⁸ | −1×10⁻⁵ / −5×10⁻⁵ |
| source 0.05 | abs 240 | 2.67326, +82.83° | 0.4910 | **9.33 / 9.70 dB** | 91.95° | 1.084, +7.9° | 0.222 / 0.222 (0.177) | 4×10⁻⁷ | −7×10⁻⁵ / −3.4×10⁻⁴ |
| source 0.10 | abs 240 | 2.66740, +90.07° | 0.6800 | **14.40 / 14.88 dB** | 89.07° | 1.082, +15.2° | 0.312 / 0.271 (0.280) | 2×10⁻⁶ | −2.7×10⁻⁴ / −1.35×10⁻³ |
| source 0.20 † | abs 240 | 2.96665, +93.07° | 0.8327 | 20.79 dB (not steady: 3.6×10⁻²) | 88.93° | 1.203, +18.2° | **0.529** / 0.384 (0.520) | 2 phases | −6.1×10⁻⁴ / −5.1×10⁻³ |
| source 0.05 | analytic 240 | 1.72528, +87.22° | 0.4004 | 7.37 / 7.65 dB | 89.30° | 1.007, +4.4° | 0.176 / 0.174 | 2 phases | −5×10⁻⁵ / −3.3×10⁻⁴ |
| source 0.05 | ratio 480 | 2.36174, +88.46° | 0.4731 | **8.93 / 9.18 dB** | 91.41° | 0.955, +7.0° | 0.232 / 0.232 | 6×10⁻⁷ | −6×10⁻⁵ / −3.4×10⁻⁴ |
| source 0.05 | abs 480 | 2.95229, +85.82° | 0.5193 | 10.00 / 10.29 dB | 92.68° | — | 0.264 / 0.264 | 2 phases | −7×10⁻⁵ / −3.4×10⁻⁴ |
| source 0.05 | ratio 720 | 2.24812, +89.83° | 0.4636 | **8.72 / 8.94 dB** | 91.41° | 0.907, +6.1° | 0.242 / 0.242 | 2 phases | −6×10⁻⁵ / −3.4×10⁻⁴ |
| source 0.05 | **passive twin** M = 10⁻⁹, 240 | (velocity degenerate at M → 0: −M δh plus an O(Δx) residue) | — | **— / 3.13 dB** (3.21 at N = 480, check seat 2) | — | — | 0.085 | 2 phases | — |
| drain 0.1 | abs 240 | 2.54920, +74.85° | 0.2117 | 3.73 / **3.08 dB** | 128.40° | 1.034, −0.1° | 0.169 / 0.169 | 2×10⁻⁹ | ≈ 0 |
| drain 0.2 | abs 240 | 2.81603, +74.62° | 0.4086 | 7.54 / **6.24 dB** | 128.54° | 1.142, −0.3° | 0.187 / 0.187 | 9×10⁻⁹ | ≈ 0 |
| drain 0.5 (large signal) | abs 240 | 5.33544, +71.47° | 0.8121 | 19.68 / **16.53 dB** (3-phase 19.40 dB, residual **10.4 %**) | 131.20° | **2.164**, −3.4° | 0.271 / 0.271 | 1.6×10⁻⁴ (blind) | −2.5×10⁻⁴ / +3.2×10⁻⁴ |

*Reading.*
- **The column's limits.** The 4-phase residual is not a linearity test. On 0 / 90 / 180 / 270°, third-order terms e^{±3iφ} alias exactly into B and A, so the residual sits at the steady-state level whatever the compression (check seat 2). The three-phase test is in the contrast column for drain 0.5, and in G3c for the source route.
- **The axis.** The amplified axis follows the pump phase as φ_p/2, exactly: the time-translation identity forces A to be independent of φ_p and B ∝ e^{iφ_p}, and G3b checks it.
- **Convergence.** The source route converges by grid, by −0.40 then −0.21 dB (velocity). First-order Richardson on the last pair gives ≈ 8.3 dB, an extrapolation.
- **Pull on the linear response.** At 0.05 the source pump changes A by +8 % and +7.9° on N = 240 (A/A₀ 0.955 / 0.907 on N = 480 / 720). That is the pump's parametric pull on the phase-insensitive response, not the detuning its rectified shift causes (−1.7×10⁻⁴ of f₀ under √h).
- **The drain route** is read on the drain density. Its velocity readings carry the pumped clamp, u ≈ u₀(1 + p)/h (check seat 1).

---

## 3. The Floquet census and the parametric onset (`psa_floquet.py`, `psa_floquet2.py`, `psa_param.py`, `psa_param2.py`, `psa_extra.py`, `psa_rework.py`)

**Method.**
- **The period map** is the record's finite-differenced one-step operator, extended over one pump period. The step is set to T_p/m (m = 1,599 at N = 240, 3,181 at N = 480; cfl 0.39998), so the map is exact. Under it every odd mode (2n + 1)f₀ maps near μ = −1, and a parametric instability is a real negative multiplier leaving the unit circle.
- **Settling.** K pump periods, given per row with F2. The 120-period builds are quoted with the check seats' per-row agreement (§1, F2).
- **Time domain.** Rows above onset are pump-only time-domain runs: noise seed 10⁻⁴, |Z_f₀| over eight successive 10-period windows (the last 80 carrier periods).

| route, pump (N = 240 unless stated) | K / F2 | leading multipliers \|μ\|∠arg | amplified-quadrature memory (−T_p / ln\|μ₁\|) | time domain, pump only (last 80 periods) | base / state max\|hu/h\| run (steady) |
|---|---|---|---|---|---|
| none | 120 / 0 | 0.91292∠±177.95°, 0.70392∠±176.08°, 0.41866∠±174.11° (f₀, 3f₀, 5f₀) | 5.49 ps (N = 480 ratio: 0.91569, 5.68 ps) | — | 0.118 |
| source 0.05 | 120 / 1.1×10⁻³ | **0.93763∠180°**, 0.82215∠180° (the f₀ pair split along the negative axis), 0.65867∠±176.19° | **7.76 ps** (de-amplified 2.55 ps); N = 480 ratio, K = 300 / 1.2×10⁻⁹: 0.93021, **6.91 ps** | — | 0.169 |
| source 0.10, N = 240 (N = 480 ratio in parentheses) | 120 / 3.7×10⁻³ (8.3×10⁻⁴) | 0.94679∠180° (0.93326∠180°) | 9.14 ps (7.24 ps) | — | 0.222 (0.215) |
| source 0.20 | 600 / 1.8×10⁻⁵ | 0.98198∠180° (free decay 0.98155–0.98180 and 0.98200, two round-3 seats) | 27.5 ps | noise-seeded, decays; start-up 0.520 † (`psa_r4c.py`) | 0.340 (the base's own maximum) |
| source 0.21 | 600 / 2.2×10⁻³ | 0.99096∠180° (independent readings 0.99058) | 52.8–55.1 ps | **decays**: 7.3×10⁻⁵ → 2.0×10⁻⁵ | base 0.353; time-domain run 0.546 † (start-up transient) |
| **source 0.23** | — (oscillating) | — | — | **latched 4.69×10⁻³** (N = 480 ratio leg: 6.67×10⁻³) | 0.590 † (0.382); N = 480: 0.630 † (0.405) |
| source 0.25 / 0.30 | — | — | — | latched 7.86×10⁻³ / 1.09×10⁻² | 0.626 † / 0.697 † (0.416 / 0.519 †) |
| drain 0.2 | 120 / 1.1×10⁻⁴ | 0.91209∠±179.03° (pair not yet split) | 5.43 ps | — | 0.143 |
| drain 0.5 | 300 / 4.9×10⁻⁴ | 0.97300∠180°, 0.84502∠180° | 18.3 ps | — | 0.180 |
| drain 0.55 / 0.60 | 600 / 1.0×10⁻⁵, 6.1×10⁻⁴ | 0.98013 / 0.98693 ∠180° (0.55 by free decay 0.97985, one round-4 seat) | 24.9 / 38.0 ps | 0.60 **decays**: 2.2×10⁻⁵ → 3.6×10⁻⁶ | 0.186 / 0.192 |
| drain 0.70 | — | — | — | decays slowly on 600 rt (4.11 → 3.63×10⁻³); decays on 1,800 / 2,400 rt (both check seats) — below onset; N = 480 ratio leg: decays on 1,200 rt (6.14 → 4.69×10⁻⁴) | 0.267 (N = 480: 0.260) |
| **drain 0.72** | — | — | — | **latched 6.732×10⁻³**, phase +22.45° stationary to 0.01° (1,800 rt) | **0.272** (0.237) |
| drain 0.75 | — | — | — | latched 1.07×10⁻² (N = 480 ratio leg: latched 6.588×10⁻³ on a 1,200-rt record; 0.80 latches at 1.0488×10⁻²) | **0.278** (0.264); N = 480: 0.271 (0.230) |
| drain 0.85 / 1.0 | — | — | — | latched 1.83×10⁻² / 2.56×10⁻² | 0.317 / 0.368 |

**Onsets**, bracketed from both sides on N = 240:
- **Source clamp (0.21, 0.23]** of the density. The upper end also latches on the N = 480 ratio leg; the lower end is an N = 240 statement.
- **Drain current (0.70, 0.72]** of u₀, an N = 240 statement. On the N = 480 ratio leg the bracket is (0.70, 0.75]: 0.70 decays (`psa_r4c.py`), 0.75 and 0.80 latch on 1,200-rt records (`psa_r3.py`; the earlier 600-rt reading was a settling latched state), and the |Z|² law over the two latched rows puts p_c ≈ 0.717 there (one round-2 seat: 0.717–0.719 over three rows, and the N = 480 absolute leg latches at 0.75).
- **Amplitude laws.** On the drain route |Z_f₀|² is linear in the pump across 0.72 / 0.75 / 0.85 / 1.0, with intercept p_c ≈ 0.70. On the source route the √(p − p_c) law holds only for the two rows nearest onset: 0.25 against 0.23 gives a ratio of 1.68, while 0.30 gives 2.32 against the √ law's 2.83.

**Latching tests at the drain pump 0.85** (CW; seeds along the drain axis, 131.2°, or opposite it, switched off after 20 rt; 300 rt):

| seed | latched \|Z_f₀\|, phase | steady (complex phasor) | max\|hu/h\| run / window |
|---|---|---|---|
| +, 2×10⁻³ | 0.01816 at −156.99° | 2×10⁻² (not yet steady) | 0.317 / 0.317 |
| −, 2×10⁻³ | **0.01829 at +23.00°** | 1.2×10⁻⁴ | 0.363 / 0.318 |
| +, 2×10⁻² (×10) | **0.01829 at −157.00°** | 1.9×10⁻⁴ | 0.529 † / 0.318 |

- **Bistability.** On the steady rows the seed's sign selects one of two states 180.00° apart. That is a drain-0.85, 2×10⁻³ statement: on the source clamp a weak, short seed loses to the pump's own turn-on (item 4).
- **Re-levelling.** The amplitude does not remember the seed: **1.000** for the ×10 seed (whose start-up runs at 0.529 †).
- **Lock.** The steady criterion is on the complex phasor, so the state is stationary in phase at f₀. That is the evidence of the lock (check seat 1: arg Z_f₀ constant to ≤ 0.001° over 80 periods on every latched row). The drain-velocity FFT peak sits at 2f₀, the pump's forced response, and is not used.

---

## 4. Table R — restoration (`psa_tableR.py`, `psa_rework.py`, `psa_rework2.py`, `psa_timing.py`, `psa_timing2.py`, `psa_param.py`)

**R.1 The one-cell phase map.**
- **Setup.** Source pump 0.05 unless stated; φ_p = −183.91° on N = 240, −182.82° on N = 480 and −182.82° on N = 720, so that the small-signal axis sits at input phase 0; 240 rt.
- **Quantities.** ψ = arg Z(φ) − arg Z(0). |Z|/a is the drain-velocity amplitude per unit source swing.
- **The knee.** It is 0.0095, the midpoint of 10-08's knee band 0.0076–0.0115.

| swing, grid | φ = 0 | 10° | 30° | 45° | 55° | 60° | 70° | 80° | 85° | 90° | 120° | 150° | 180° | slope at axis | contrast R(0)/R(90) | max\|hu/h\| run / window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| knee 0.0095, 240 | 2.911, 0° | +4.76 | +15.98 | — | +35.79 | +41.16 | +54.63 | +73.76 | +86.02 | +99.50 | +151.50 | +167.31 | +180.00 | **0.458** | 6.76 dB | **0.406** / 0.404 |
| knee 0.0095, 480 ratio | 2.778, 0° | +5.12 | — | +29.28 | — | — | — | — | — | +102.52 | (135°: +160.86) | — | — | **0.486** | 7.10 dB | **0.424** / 0.424 |
| 0.0085, 720 ratio | 2.761, 0° | ±10° rows only | | | | | | | | | | | | **0.491** | — | **0.422** / 0.422 |
| knee 0.0095, 720 ratio † | 2.712, 0° | — | | | | | | | | | | | | — | — | 0.432 † / 0.432 |
| `A_fix` 0.0140, 240 | 2.450, 0° | +5.26 | +17.59 | — | — | +45.43 | — | — | — | +102.14 | +148.85 | +165.67 | +180.00 | 0.509 | 5.42 dB | 0.447 † / 0.441 |
| '1' 0.0197, 240 | 2.046, 0° | +5.71 | +18.81 | — | — | +48.53 | — | — | — | +102.88 | +144.98 | +163.86 | +180.00 | 0.558 | 4.14 dB | 0.483 † / 0.470 |
| '1' 0.0197, 480 ratio | 1.993, 0° | +5.69 | — | +33.66 | — | — | — | — | — | +109.37 | (135°: +155.56) | — | — | 0.555 | 4.49 dB | 0.489 † / 0.480 |
| '1' 0.0197, **pump 0.02**, 240 | 1.882, 0° | +7.80 | — | +38.98 | — | — | — | — | — | +94.70 | (135°: +144.48) | — | — | 0.771 | 1.57 dB | **0.425** / 0.411 |
| '1', unpumped, 240 | 1.741 | | | | | | | | | | | | | — | — | 0.380 / 0.366 |

**Reading R.1.**
- **Method.** The slope comes from the ±10° rows (the −10° entries are in `psa_tableR.out`). The symmetry |Z(180°) + Z(0°)|/|Z(0°)| is 6.1×10⁻⁷, 8.3×10⁻⁷ and 6.4×10⁻⁷ on the three full rows. Every row is steady to ≤ 3×10⁻⁶.
- **Restoration.** Every row restores (slope < 1 at the axis). On the knee row the unstable point separating the 0 and π states lies between the 80° and 85° rows on the positive side. By the exact half-period identity ψ(φ − 180°) = ψ(φ) − 180°, the 120° row puts the negative side's margin at ≥ 31.5° (φ − ψ = −31.5° at −60°) and the other unstable point near −96°. The binding side for the slip margin and the basin is the positive one.
- **Swing dependence.** Compression lowers the contrast with swing (6.8 → 5.4 → 4.1 dB) and weakens the restoring slope from 0.46 to 0.56.
- **Amplitude.** Along the axis the amplitude compresses as drive^0.52 between the knee and the delivered '1' (0.0277 → 0.0403 for 0.0095 → 0.0197). It re-levels partly, as 10-08's drive^0.39–0.60 does unpumped. The sub-threshold amplifier has no plateau, so it does not latch.

**R.2 The cascade, composed.**
- **Model** (*in-model*). Each cell's drain-plane output is taken as the next cell's source input, under 10-08's plane assumption (08-02 item 4; 10-08 limitation 2: there is no cell-to-cell transfer model). It is normalised so the axis input maps to itself (10-16's F = 2 unity normalisation), and the next cell's pump phase is set to the nominal arriving phase.
- **Absorption.** A per-cell phase error δ between cells settles to a fixed offset: **0.84 δ leaving a cell and 1.84 δ arriving at the next** at the knee slope (linearised; 0.94 / 1.94 δ on the N = 480 knee row, 1.26 / 2.26 δ at the delivered '1'). It does not grow with the per-cell sum.
- **Slip.** The fixed point exists while δ ≤ max(φ − ψ(φ)) = **19.2° at an arriving phase of 55°** (5° rows; 18.8° at 60° on the 30° rows), on the binding side. Beyond that a bit crosses the unstable point. At the slip edge the arriving amplitude is 0.75 of the axis amplitude that the unity normalisation assumes (|Z|/a 2.189 at 55° against 2.911), so the composition is optimistic there.
- **Plane and direct rows.** On the drain density — the plane 08-02 item 4 actually composes on — the knee slopes are 0.426 / 0.460 (N = 240 / 480; 0.508 at the '1'); the velocity reading used above is the conservative one. On direct rows the linearised offsets hold to ≤ 8 % at δ = 5°; at δ = 10° the direct rows give an arriving +20.05 / −17.56° against 18.43° linear (one round-1 seat).
- **Against 10-13.** The record's single-cell ±15° (≈ ±1 % of f₀ by 10-13's own conversion; 4–10 nm of cell length) fits inside the slip margin. The composed field-sum budget of ±0.32 … ±0.010 % per cell over 3–91 non-shared cells is the price of accumulating errors, which a phase-restoring chain inside its admissible window does not accumulate. The composition takes δ as given: how detuning moves a *pumped* cell's own axis was not computed (10-13's 12–21° per 1 % belongs to the unpumped cell). Divided by that unpumped slope — a slope division, not a pumped-cell row — the 19.2° margin corresponds to ≈ 0.9–1.6 % of f₀ per cell (*in-model*). The family also presupposes the field-sum branch of 10-13's reading fork.

**R.3 Pump-phase tolerance per cell** (*in-model*). By the identity of §2, a pump-phase error δ_p rotates the cell's input axis and its output together: e_out = δ_p/2 + ψ(e_in − δ_p/2). Two error models, with the plane named:
- **Uniform** (the same error at every cell). The chain's offset is exactly δ_p/2 and it never slips, because every cell receives its input on its own axis. ≤ 10.1° at the output (10-16's route-(ii) window, as a comparison) needs **δ_p ≤ 20.2° — 28 fs at 2 THz**.
- **Cell-to-cell increment** Δ_p (the pump's phase walks along the chain against the signal path). The offset is 0.84·Δ_p/2 leaving a cell and 1.84·Δ_p/2 arriving at the next.
  - ≤ 10.1° leaving needs Δ_p ≤ 24.0° (33 fs) linearised; on direct rows 20.1° (28 fs) on the binding sign (one round-1 seat).
  - ≤ 10.1° arriving needs **Δ_p ≤ 11.0° (15 fs)** (direct rows 10.6 / 11.3° by sign, one round-1 seat).
  - The chain slips at Δ_p ≈ 38.4° (53 fs).

Check seat 1 and check seat 2 independently gave this correction, against this text's first draft. 10-16's interference NOT needed the clock carrier within 10.1–12.3° at every inverter (≈ 28 fs at 1 THz by #139's conversion). The phase-coded chain asks a tolerance of the same order of its 2f₀ pump.

**R.4 Timing in 07-31's slot** (*demonstrated*).

*The CW-pumped amplifier.*
- **Setup.** Source pump 0.05; bits ±1 on an absolute-time carrier along the axis; pattern P3; 16 slots; one-carrier-period sliding phasor.
- **Normalisation.** Levels are given against the all-(+1) stream's steady mid-window level; the decision projection is against the all-(+1) response at the same instant.

| swing | all-(+1) stream: slot start / mid / decision point | after the opposite bit: start, decision (same-instant reference), phase error | previous bit's gap-end residue | signs correct | max\|hu/h\| |
|---|---|---|---|---|---|
| knee 0.0095 (N = 240; outside the domain in the continuum by §0 item 3's estimate) | 0.65 / 1.00 / 1.14 | **−0.59** [−0.62, −0.56]; **+0.839** [+0.832, +0.843]; 8.4° | +0.76 [+0.72, +0.80] | 14/14 | 0.402 |
| '1' 0.0197 † | 0.48 / 1.00 / 1.06 | −0.44 [−0.47, −0.42]; +1.013; 5.7° | +0.64 [+0.61, +0.67] | 14/14 | 0.483 |

The pump lengthens the memory it restores with. The amplified quadrature decays in 7.8 ps against 5.5 ps unpumped (§3), which alone would leave e^(−2.9/7.76) = 0.69 over the 2.9-ps gap; the measured residues are 0.76 / 0.64, read on the slot's last whole period against the mid-window level. Referenced to the decision-point level over the 3.0 periods between window centres they are 0.661 / 0.604, against e^(−3.0/7.76) = 0.68 (one round-2 seat). The sign decides correctly, but a flipped bit spends the slot overcoming the previous one, and not even an all-(+1) stream reaches a steady level within the slot. Against the record: 07-22's ring-down 5.71 ps, and 10-13's 2.7–4.0 ps burst delay per cell.

*The gated parametron.*
- **Setup.** Drain pump 0.85, gated with the slot window; inputs ±1 along the drain axis (131.2°, N = 240's axis, used on every grid; the latched phases agree to 0.6°: −157.00 / −156.88 / −157.47°); pattern P3; N = 240, and the ratio leg on N = 480 / 720 for the swing table. The waveform is 07-31's duty-0.8 raised-cosine envelope (`make_sig_duty`'s, reproduced in code) with the carrier moved to absolute time; no executed gate against 07-31's own rows was run (a textual identity).
- **Leak-free read.** The last whole carrier period of the absolute-time grid that lies inside the pump plateau (≥ 4 time units from the window's edges); on the period ending exactly at the plateau's end one round-2 seat reads slots 2 / 7 / 12 at 0.108 / 0.090 / 0.112, and another on a two-period window at +0.014 / +0.044 / +0.021 (the state is still rotating there). On the raised-cosine edges the forced 2f₀ response leaks into the f₀ fit (0.61–1.67 of the latched level, pump alone); on the plateau the pump alone leaves the gated cell's own f₀ state, grown from the edges (0.03–0.16 on 07-31's slot, N = 240; ≈ 0.0029 in absolute terms on every grid, 0.22 / 0.28 of the smaller latched level on N = 480 / 720, one round-4 seat).
- **Controls** (`psa_r2.py`, `psa_r3.py`, `psa_r4b.py`). The unpumped cell with the same gated input; the pump alone; the start from rest; the same pair on a slot of exactly 15 carrier periods; the sign-reversed pattern −P3 on both slots, which starts from rest against the self-seed; and the CW latched state's own density phase as the density reference.

| row (input 2×10⁻³) | sign of the plateau state follows the input | plateau-end state after a repeated bit / after a flip (of the CW latched level 0.01829) | pump-alone state in the same window | max\|hu/h\| |
|---|---|---|---|---|
| gated parametron, P3, 07-31's slot (14.49 periods) | 15/15 velocity; density 14/15 against the CW latched phase (slot 2: −0.004), 15/15 against the slot-1 phase | **1.13–1.26 / 0.45–0.72 (slots 3, 9, 10, 14, 15), 0.28 (slot 4), 0.06–0.09 (slots 2, 7, 12)**; 0/9 flips ≥ 0.9; slot 0 from rest 1.06 (self-seed aligned, +0.23) | 0.03–0.16, alternating sign; opposite to the bit, and larger than the state, in slots 2, 7 and 12 | **0.346** |
| unpumped cell, same gated input | 15/15 | 0.21–0.25 in every slot | — | 0.155 |
| gated parametron, P3, exact 15-period slot | 15/15 | 1.06–1.41 / 0.20–0.88 (weakest on the −1 flips: 0.20 / 0.23 / 0.21 in slots 2, 9, 12); 0/9 flips ≥ 0.9; slot 0 from rest 1.15 (self-seed aligned) | 0.23, one sign in every slot | 0.360 |
| gated parametron, −P3, 07-31's slot | 15/15 | 0.99–1.39 / 0.10–0.78; 0/9 flips ≥ 0.9; slot 0 from rest **0.65** (against the self-seed) | the same run; on −P3 it opposes the bit where it agreed on P3 | 0.359 |
| gated parametron, −P3, exact 15-period slot | 15/15 | 1.05–1.43 / 0.20–0.87; 0/9 flips ≥ 0.9; slot 0 from rest **0.76** (against the self-seed) | 0.23, one sign | 0.361 |

*The swing table* (`psa_r4b.py`; P3 on 07-31's slot unless stated; each grid's own CW latched + state as reference — 0.01829 / 0.01335 / 0.01006 on N = 240 / 480 / 720, the last from a 300-rt record (900 rt: 0.00997, `psa_r4f.py`; no count changes); "flips ≥ 0.9" counts against that per-grid level, the criterion withdrawn in §0 item 5 — against N = 240's 0.01829 every grid reads 0 / 1 / 5 / 9 / 9 of 9 at 2–6×10⁻³ (`psa_r4e.py`); the unpumped rows are `psa_r4e.py`'s and `psa_r4f.py`'s):

| grid | input | signs / above the pump-alone state | flips (of the CW latched level) | flips ≥ 0.9 | repeated bits | flip / repeat (mean) | max\|hu/h\| run |
|---|---|---|---|---|---|---|---|
| 240 | 2×10⁻³ | 15 / 12 | 0.058–0.724 | 0/9 | 1.13–1.26 | 0.32 | 0.346 |
| 240 | 3×10⁻³ | 15 / 15 | 0.383–0.962 | 1/9 | 1.57–1.64 | 0.43 | 0.381 |
| 240 | 4×10⁻³ | 15 / 15 | 0.765–1.218 | 5/9 | 1.83–1.91 | 0.54 | 0.404 |
| 240 | **5×10⁻³** | 15 / 15 | **1.162–1.589** | **9/9** | 2.04–2.12 | 0.65 | **0.4215** |
| 240 | 5×10⁻³, −P3 / 15-period slot | 15 / 15; 15 / — | 1.117–1.582 / 1.447–1.659 | 9/9 / 9/9 | 2.05–2.12 / 2.10–2.14 | 0.66 / 0.73 | 0.4219 / 0.4236 |
| 240 | 5×10⁻³, unpumped | 15 / — | 0.510–0.548 | 0/9 | 0.60–0.61 | 0.88 | 0.208 |
| 240 | 6×10⁻³ | 15 / 15 | 1.505–1.909 | 9/9 | 2.22–2.29 | 0.75 | 0.435 † |
| 480 | 2×10⁻³ | 15 / 12 | 0.055–0.955 | 1/9 | 1.47–1.60 | 0.32 | 0.340 |
| 480 | 3×10⁻³ | 15 / 15 | 0.459–1.273 | 5/9 | 1.98–2.05 | 0.43 | 0.371 |
| 480 | **4 / 5 / 6×10⁻³** | 15 / 15 | 0.924–1.612 / 1.410–1.989 / 1.883–2.372 | **9/9** each | 2.32–2.90 | 0.55 / 0.65 / 0.74 | **0.393 / 0.410 / 0.425** |
| 720 | 2×10⁻³, P3 / −P3 | 15 / 12; 15 / 14 | 0.149–1.245 / 0.186–1.326 | 4/9 / 2/9 | 1.69–2.21 | 0.35 / 0.39 | 0.334 / 0.343 |
| 720 | 3×10⁻³ | 15 / 15 | 0.663–1.688 | 6/9 | 2.51–2.60 | 0.46 | 0.365 |
| 720 | **4 / 5 / 6×10⁻³** | 15 / 15 | 1.242–2.148 / 1.845–2.603 / 2.431–3.048 | **9/9** each | 2.96–3.71 | 0.57 / 0.67 / 0.75 | **0.387 / 0.404 / 0.419** |
| 240 | 8 / 9×10⁻³, unpumped | 15 / — | 0.822–0.886 / 0.928–0.999 | 0/9 / **9/9** | — | 0.91 / 0.92 | 0.255 / 0.269 |
| 480 | 4 / 5 / 6 / 7×10⁻³, unpumped | 15 / — | 0.510–0.548 / 0.639–0.687 / 0.769–0.829 / 0.900–0.973 | 0/9, 0/9, 0/9, **9/9** | — | 0.82–0.84 | 0.188–0.239 |
| 720 | 4 / 5 / 6×10⁻³, unpumped | 15 / — | 0.655–0.705 / 0.821–0.884 / 0.987–1.064 | 0/9, 0/9, **9/9** | — | 0.80–0.81 | 0.187–0.223 |

Slot 0 from rest at 5×10⁻³ on N = 240 reaches 1.95 (P3, self-seed aligned) and 1.74 (−P3, against it). Two round-3 seats ran the same rows on their own loops, and both reproduced the 5×10⁻³ N = 240 row on this instrument; one adds 5.5×10⁻³ on N = 240 (9/9, run-wide 0.4287, inside by 2.6×10⁻⁴) and drain 1.0 at 2×10⁻³ (12/15 signs). One round-4 seat reads the N = 480 7×10⁻³ unpumped row at 8/9 (ninth flip 0.8996) against its 0.01333 reference — at the boundary.

**Reading.**
- **The sign is the input's (2×10⁻³).** The plateau sign survives in every slot, but it is the input's own: an unpumped cell gives the same 15/15. The pump's contribution is the re-levelling after a repeated bit (×5 over the unpumped cell), and from rest when the self-seed agrees with the bit (1.06; 0.65 against it).
- **Where it fails (2×10⁻³, N = 240).** After a flip the pump amplifies the inherited opposite residue and its own edge-seeded state along with the input. In slots 2, 7 and 12 it ends at 0.06–0.09 of the latched level: below the unpumped cell's own 0.21–0.25, and below the pump-alone state in that window. There the sign is not robustly decided: on the drain density slot 2 reads wrong against the CW latched density phase (−0.004, `psa_r3.py`, as one round-1 seat found). The other six flips reach 0.28–0.72; none re-levels.
- **Why those slots.** 07-31's slot is 14.49 carrier periods, so the gated pump's edge-seeded state steps ≈ 177° per slot against the absolute-time axis and alternates sign. The weakest flips are those where it and an inherited residue of ≥ 0.35 both oppose the bit. On an exact 15-period slot the self-seed keeps one sign, and the weakest flips move to the bits it opposes (0.20–0.23). The sign-reversed pattern bears the rule out: on −P3 the weakest flips are those where the seed and the residue both oppose the bit (slots 14 and 9, 0.10 / 0.15, one round-2 seat; the range 0.10–0.78 is `psa_r3.py`'s).
- **What a larger input does.** It outgrows the inherited residue and the self-seed: from between 4 and 5×10⁻³ every flip clears 0.9 of N = 240's latched level on every grid, the pumped flips ×1.75–3.15 the unpumped ones. The level is not re-set: it follows the input and keeps a flip at 0.55–0.75 of a repeated bit (0.80–0.92 unpumped), so no input run gives a re-levelled bit stream. The domain caps the ladder between 5.5 and 6×10⁻³ on N = 240; on N = 480 / 720 the top row, 6×10⁻³, is still inside, so that edge is not bracketed. Round 4's "window's lower edge falls with refinement" was the per-grid reference's trend and is withdrawn. Nothing here is registered as a key.
- **What would change the 2×10⁻³ row.** The 2.9-ps pump-off gap is already an idle phase; it is short against the ≈ 5.5-ps unpumped memory. An integer-period slot was run (the exact 15-period rows). It fixes the self-seed's sign, which then opposes every bit of the other value, and no flip re-levels on either pattern (worst 0.20, against 0.058 on 07-31's slot). These rows are consistent with 07-22 §7's lesson that a parametron needs enough idle time, or an active quench, to forget the previous bit; no longer idle phase or quench was run. The changes named, not run: the edge-seeded state cancelled or placed in the de-amplified quadrature, together with a longer idle phase or an active quench. They address the 2×10⁻³ row and the history dependence, which every input run shows.
- **Correction history.** The first draft reported 11/15 from edge windows; both check seats refuted it. The round-1 text reported "sign 15/15, a build-up failure, not a sign failure"; all three round-1 seats showed that the sign is the input's and that three flips sit below the pump's own self-seed. Round 2's text named an aligned integer-period slot as a remedy and read the from-rest row as unconditional; round-2 seats showed that the 15-period rows test the first and that the from-rest row had the self-seed on its side. Round 3's text stated "no admissible window for a bit stream was found" from the 2×10⁻³ row alone; two round-3 seats found every flip above 0.9 of the latched level at 4–5×10⁻³. Round 4's text called that a window per grid; all three round-4 seats showed that its grid trend is the reference's and that an unpumped cell meets the same criterion at larger inputs. This text replaces all five.

---

## 5. Table G — the gate set under phase encoding (*in-model* on executed rows)

| element | phase-encoded form | executed basis | result | against 10-16 |
|---|---|---|---|---|
| majority of three | the cell reads the sign of the summed source field: (+++), (++−) → 0; (+−−), (−−−) → π | the source sees one field, the coherent sum; rows at a knee unit (0.0095), at 3 × the knee (0.0285), and the knee phase map on 5° rows | classes separated by π in phase. Output (+++) / (++−) = 0.0472 / 0.0277 = **4.6 dB** (compression re-levels from 9.5 dB linear). But **(+++) at 3 × knee leaves the domain (0.521)**, so an in-domain majority needs inputs ≤ ⅓ knee ≈ 0.003 on N = 240 / 480 (≤ ⅓ of the band's bottom, ≈ 0.0025, in the continuum by §0 item 3's estimate). One such unit is ≈ 3.8 quanta, and the weak class's ideal antipodal error at 353 K is 0.15 (*in-model*, `psa_r3_arith.py`). Phase spread, worst case over all three inputs: ±30° puts the weakest class's sum at **60.0°** from the axis, ±40° at **70.0°**; the knee map restores both (60° → 41.2°, 70° → 54.6°), inside the basin (+80–85° / −95–100°). The projection's sign is lost at ±60° | 10-16's AND needed an amplitude threshold between '1 + 1' and '1' (2.6–3.3 dB) that the cell does not have; the majority needs none |
| AND / OR | MAJ(a, b, constant) | — (*in-model*, not run) | the constant is a coherent f₀ reference at one input unit and a fixed phase to the pump — the clock carrier itself, phase-locked to the 2f₀ line | — |
| NOT | a half-carrier-period delay (0.500 ps) of the signal against the pump; the pump cannot do it — its phase sets the axis only modulo π | Part I's passive loss 27.3/Q dB per λ_p | in-model cost ≈ **2.6 dB** of passive λ_p/2 line at 353 K (Q = 5.34), or a gain segment of that length. A single delay error restores in one cell up to the basin edge (80–85° ≈ 222–236 fs, ≈ 518–550 nm of passive line); a systematic delay error repeated at every NOT of a chain is a per-cell error, bounded by the slip margin (19.2° ≈ **53 fs**, ≈ **124 nm** of passive line at the released plasmon speed, λ_p = s/f₀ = 2.33 µm) | 10-16's interference NOT needed a clock pulse within 10.1–12.3° at every inverter; the delay needs no pump of its own, but every downstream cell needs the 2f₀ pump |

*Consequences only*; Part III [V2] and the lane are not re-priced here, and nothing is counted. Under phase encoding the majority full adder is the classical parametron adder: carry = MAJ(a, b, c), sum = a five-input majority with two inverted carries. Its inverted carries are delays, so the 783 NOTs of [D1] become delay segments. Fabric's dual-rail count earlier today (981 more threshold ANDs) does not carry over, because the majority is read by sign, not by threshold.

---

## 6. The pump's bill (*in-model*)

| item | source-clamp amplifier (0.05) | source parametron (0.23) | drain parametron (0.72–0.85) |
|---|---|---|---|
| amplitude and plane | 5 % of the density at the source clamp (the gate-to-source voltage), 2f₀ | 21–23 % at onset; latched at 0.23 | 70–72 % of the DC current at onset, at the drain contact |
| energy per slot against the clock burst — **a proxy**: the ratio of source-plane mean-square swings, CW pump against a duty-0.8 raised-cosine burst (mean square 0.714 of the slot), which equals an energy ratio only if a 2f₀ drive costs the same per δh² as an f₀ drive (Eq. (Q2) denominates the f₀ mode alone; not established by any row) | ≈ **9.0×** a delivered-'1' burst; ≈ 38.8× a knee burst | ≈ 191× a delivered-'1' burst | not denominated (a current at the drain contact) — **open** |
| added AC relaxation loss, ⟨h (u − u₀)²⟩ / u₀² (pump only, steady) | **4.6 %** | 114 % | **24 %** (0.75) |
| pump-phase tolerance (R.3) | uniform δ_p ≤ 20.2° (28 fs) for a ≤ 10.1° offset, no slip; increment Δ_p ≤ 11.0° (15 fs) arriving, slip ≈ 38° (53 fs) | same family | same family |
| velocity domain | inside at small signal and at knee-level swings by grid (at or below the band's bottom in the continuum, in-model; §0 item 3); outside at `A_fix` and the '1' (a 2 % pump keeps 0.0197 inside on N = 240 / 480 and the ratio leg's own 0.0189 / 0.0186 on N = 480 / 720; 0.0197 on N = 720 only under 1–1.5 %) | outside run-wide (0.59–0.70 at 0.23–0.30); inside at steady state at 0.23–0.25 | inside run-wide (0.272–0.317) |
| on Kinetic's unpromoted G5 floor (heat ∝ τ⁻³, so the floor scales as (1 + x)^⅓ from 0.916 ps) | ×1.015 → 0.930 ps | ×1.288 → 1.18 ps, above Part I's best-case 1 ps | ×1.074 → 0.984 ps |

**What #139 must supply** (requirements; the device options are named, not tested):
- **Two coherent lines.** A 2 THz pump phase-locked to the f₀ reference, plus the f₀ reference itself as the AND/OR constant — two coherent lines where the amplitude-coded fabric needed one.
- **An absolute-time carrier.** The bit must ride on a carrier referenced to absolute time. 07-31's launch references each burst to its window centre, and that reference steps 177.4° per 14.49-period slot against a CW 2f₀ pump, which would flip alternate bits (check seat 1).
- **Candidate sources.** A comb-derived DFB pair at 2 THz spacing in the photomixer, or a doubler of the f₀ line, would be the natural ones. #139's RTD fundamental record, reported up to 1.98 THz (a secondary figure, unverified), sits at the edge.

**The heat booking** compares AC relaxation loss with DC drift loss at the same τ. Part I §8.2's tracked-bias heat books J·E, and whether the AC loss adds to it or is part of what the bias supplies through the gain is not resolved here. Read the fractions as upper-bound additions.

**The smallest change that would widen the window** — stated, not run, not claimed to work:
- **For the gated parametron:** the 2.9-ps pump-off gap is already an idle phase; what is short is that idle time against the ≈ 5.5-ps unpumped memory, together with the pump's own edge-seeded state. At 2×10⁻³ an integer-period slot was run and does not suffice (§4: it fixes the seed's sign, which then opposes one bit value). The changes named: the edge-seeded state cancelled or placed in the de-amplified quadrature, with a longer idle phase or an active quench between slots. A larger input (4–6×10⁻³) amplifies the flips but does not re-set the level (§4), so these address the history dependence at every input.
- **For the amplifier:** a pump route that modulates the bulk plasmon speed resonantly (a 2f₀ mode of the cell, or a distributed gate). It would need a term the released equations do not contain, and should lower the pump the amplifier needs below the 5 % at which the knee rows ran (the 1–2 % rows are the delivered '1''s).

---

## 7. Grades

| record item | grade | executed reason |
|---|---|---|
| 08-05: "No phase-sensitive escape is available on this cell (parametric route only; in-model on the released cell model and Part I's DC drive description …)" | **confirmed within its scope; qualified outside it** | with DC drive the zero-pump gate gives \|B₀\|/\|A₀\| = 1.2×10⁻⁷; with a 2f₀ pump at either clamp the same released equations give 3–17 dB of phase-sensitive contrast (density channel) and a latching oscillator. The noise consequence (Part II §7(ii)'s evasion of F = 2 − 1/G) is named, not priced |
| 10-13 Table C: "phase-sensitive (2f₀-pumped) amplification … named, not derived: no 2f₀ pump exists in the released chain" | **derived (in-model)** | Tables P and R, §3 |
| Part II §7(ii): "a DS cell driven parametrically (bias modulated at 2f₀) would be a phase-sensitive amplifier" — gate or drift? | **amplifier clause confirmed for both readings** (the F = 2 − 1/G clause untested) | the gate reading (source clamp) gives 9.7 dB at 5 % (density) and latches at 21–23 %; the drift reading — the drain current clamp modulated, the body force u₀/τ left DC — gives 16.5 dB at 50 % (density, large signal) and latches at 70–72 %, the only latching state inside the domain run-wide. A body-force pump of 0.2 gives only 0.51 dB (one round-1 seat), so the drift reading's coupling lives in the drain clamp |
| Part III limitation 24: "Not explored: phase-sensitive amplification or squeezing (Part II §7) …" | **explored (in-model), amplification only** | squeezing not computed |
| 10-16: "the only in-model NOT is destructive interference" | **qualified: a property of the amplitude encoding** | under phase encoding NOT is a delay (§5); the encoding is restoring in-model but admissible only in a narrow window — knee-level swings under a 5 % pump (at or below the band's bottom in the continuum, in-model), and weak restoration at the delivered '1' (slope 0.76–0.87 under 1–2 % pumps, the domain edge set by the swing); a drain-route latch holds a bit (CW) and, gated in 07-31's slot at drain 0.85, amplifies a bit stream's flips ×1.75–3.15 over an unpumped cell but re-levels none (the level keeps the previous bit at every input run). 10-16's "no density route to a NOT" is untouched |
| 10-16's key `inv_rect_sign` = accumulating (+), falsifier "any drive in the domain at which ⟨h(1)⟩ − 1 < 0", and its §2.2 "nothing in the released cell depletes under drive" | **qualified: scoped to carrier-frequency inputs** | under a 2f₀ drive at either clamp the biased cell's drain DC depletes (−7.35 / −5.99 / −5.53×10⁻⁵ at the 0.05 source pump on N = 240 / 480 / 720; −2.72×10⁻⁴ at 0.10; −2.46×10⁻⁴ at the 0.5 drain pump), while the passive twin accumulates (+7.53 / +5.74×10⁻⁵ on N = 240 / 480; ≈ +3.95×10⁻⁵ at first order, which one round-2 seat finds is 10-16 §2.2's closed form at 2f₀). The depletion is quadratic in the pump (≈ −0.022 … −0.030 per a² on the source-clamp rows of either leg, down to a 0.01 pump on N = 480 by one round-2 seat; ≈ −0.001 on the drain route), and it survives refinement (≈ −4.6×10⁻⁵ at first order from N = 480 / 720). So the passive sign is §2.2's, and the bias reverses it. The falsifier fires as worded unless "drive" is read as the f₀ input it measured (0.0076–0.036); per unit a² the depletion is ≈ 1,500× weaker than the carrier's accumulation and ≈ 10³ below what a 10-dB inversion needs, so no density route to a NOT follows. A promotion of this result would annotate 10-16 accordingly |
| Quanta's 10-13 lab post: the 2f₀ oscillation threshold at δf/f = 1/Q (2.4–4.8 % of f at the 0.7·M_th bias; 11–22 % of n under Part I Eq. (1)) | **qualified** | under the solver's √h law δf/f = ½ δn/n gives 4.8–9.6 % of n for a uniform modulation; the measured boundary-pump onset is 21–23 %, ×2.2–4.8 higher. That a source-clamp pump modulates the cell mostly near its boundary is the likely reason (*in-model reasoning, not tested*). With the measured unpumped memory (5.49 ps, Q_net ≈ 17) the uniform estimate becomes 2/Q ≈ 11.6 % of n, and the boundary onset is ×1.8–2.0 of it (one round-1 seat, in-model). The drain route is a different coupling (gain modulation) |

---

## 8. Registered keys and bench discriminants

The prefix `psa_` has 0 hits in `notes/`, both `results.json`, the three model chains, `agents/`, README, ROADMAP and Parts I–III (re-checked; both check seats confirm).

| key | value [band] | scope | falsifier |
|---|---|---|---|
| `psa_contrast_dB_src0p05` | **9.3 [8.7, 10.0]** (drain velocity); 9.7 [8.9, 10.3] (drain density) | signal 2×10⁻³, source-clamp pump 0.05 at 2f₀, absolute and ratio legs, N = 240 / 480 / 720; on the 0/90/180/270° phase set (a non-aliasing set reads ≈ 0.08 dB higher) | outside [7.0, 11.5] dB at N ≥ 240 on either leg and channel, inside the domain |
| `psa_axis_slope_knee_src0p05` | **0.47 [0.45, 0.50]** | dθ_out/dθ_in of the drain-velocity phasor at the amplified axis (on the drain density 0.426 / 0.460 on N = 240 / 480, the first outside this band, and 0.472 at 0.0085 on N = 720 by one round-2 seat): knee 0.0095 on N = 240 / 480, 0.0085 on N = 720 (the knee is outside the domain there) | ≥ 0.70 on N ≥ 240 at that pump and swing inside the domain (at the axis the slope equals 10^(−R/20) of that swing's contrast R; 0.70 ↔ 3.1 dB) |
| `psa_param_onset_src` | **0.22 (0.21, 0.23]** of the density | source clamp, pump only, N = 240 absolute leg (0.23 latched also on the N = 480 ratio leg) | no subharmonic oscillation below 0.30, or one below 0.15, on N ≥ 240 |
| `psa_param_onset_drain` | **≈ 0.70⁺ (0.70, 0.72]** of u₀ (the \|Z\|² intercept 0.70; check seat 1's 1 − μ interpolation 0.701) | drain current clamp, pump only, N = 240 absolute leg; 0.70 decays on 600- / 1,800- / 2,400-rt records; on the N = 480 ratio leg (0.70, 0.75], p_c ≈ 0.717; on the N = 720 ratio leg (0.72, 0.80], intercept 0.755 — the onset rises with refinement (one round-4 seat: ≈ 0.78 on N = 960 at an extrapolated bias), continuum open | onset outside [0.60, 0.90] on N ≥ 240 |
| `psa_relevel_ratio_drain0p85` | **1.000 [0.99, 1.01]** | latched \|Z_f₀\| for a ×10 seed against a 2×10⁻³ seed, drain pump 0.85, N = 240, steady rows (the ×10 row's start-up runs at 0.529 †; late window 0.318) | outside [0.9, 1.1] |
| `psa_memory_ps_src0p05` | **7.8 [6.9, 7.8]** ps | amplified-quadrature decay at the 0.05 source pump from the Floquet multiplier, N = 240 / 480 (unpumped 5.49 / 5.68 ps on the same grids) | ≤ the same-grid unpumped memory on N ≥ 240 |
| `psa_gated_flip_buildup` | **0.06–0.72** of the CW latched level after a flip, on the drain velocity (0.06–0.09 in three of nine flips; 0/9 ≥ 0.9) | drain pump 0.85 gated with 07-31's window (14.49 periods), **in-domain input 2×10⁻³, P3, N = 240** (on N = 480 / 720 at that input 0/9 reach 0.9 of N = 240's latched level; 1/9 and 4/9 of each grid's own, smaller one), read on the last whole carrier period of the absolute-time grid inside the pump plateau; controls: the unpumped cell 0.21–0.25 with the same input, the pump-alone state 0.03–0.16, from rest 1.06 with the self-seed aligned and 0.65 against it (−P3); on an exact 15-period slot 0.20–0.88 (P3) / 0.20–0.87 (−P3); at 4 / 5×10⁻³ the same cell gives 0.77–1.22 / 1.16–1.59 (§4's swing table) | at a 2×10⁻³ input on N = 240: ≥ 0.9 after every flip inside the domain at 07-31's 2.9-ps gap and 11.6-ps window (a larger input meets that because the pump amplifies the flips there, §4; that is not a falsification) |

**Bench discriminants under G1's pins** (bias 0.7 × the device's own measured threshold; pump amplitudes as fractions of the device's own gate-to-source density swing and DC current):
- **D-PSA-1.** Read on the drain density, the biased cell's gain against probe phase, relative to a 2f₀ gate-source tone of 5 %, should modulate as cos 2φ with **8.9–9.7 dB** of contrast (N = 720–240). The unbiased twin should show **3.1–3.2 dB**. A biased contrast no larger than the twin's would refute the parametric gain the released model predicts. Like D-PSA-2, it presupposes G1's pin, a measurable DS threshold (10-15).
- **D-PSA-2.** A 2f₀ drain-current modulation of ≳ 0.7 of the DC current should produce f₀ emission phase-locked to the pump with no input, bistable (0/π) under a seed strong or long enough to win against the pump's own turn-on (§0 item 4), with an amplitude independent of the seed's. No subharmonic emission up to a 0.9 modulation would refute the onset. The model's own onset rises with refinement (0.70 / 0.717 / 0.755 on N = 240 / 480 / 720; ≈ 0.78 on N = 960, one round-4 seat), so its margin to the 0.9 line shrinks from 0.20 to 0.15 and ≈ 0.12; a continuum onset is open. G1's pin presupposes a measurable DS threshold, whose existence at 353 K 10-15 leaves open.

---

## 9. Dispositions of the unpromoted inputs, and limitations

**Dispositions.**
- **The candidate seat's probe.**
  - Its source rows are confirmed to 0.1–0.2 dB: 4.11 / 9.33 / 14.40 against 4.1 / 9.4 / 14.6 dB, and 10.00 against 10.1 dB on N = 480.
  - Its drain-0.5 fit residual of 13 % is consistent with the three-phase 10.4 % measured here, not refuted. The four-phase residual is blind to it (§2).
  - Its no-oscillation at 0.10 / 0.20 is consistent with μ₁ = 0.947 / 0.982.
  - Its 4.9 dB at the delivered '1' is a different statistic, the |B|/|A| of a fit, from R.1's R(0)/R(90) of 4.14 dB.
- **Quanta's 10-13 estimate:** graded in §7.
- **Fabric's dual-rail count:** it does not carry over to phase encoding (§5).
- **Quanta's ≥ 511-quanta rectifying read** prices an on-off read. A phase-encoded bit is the antipodal pair ±x, read phase-sensitively against the pump-derived reference; by 10-08's homodyne law its ideal floor at 353 K is **≈ 119 quanta** (101.5 at 300 K), ¼ of the on-off 477 the record registers (`psa_r2_arith.py`, which reproduces the on-off 405.9 / 477.3). At knee-level swings (22–51 quanta by `qmode.N_of_eps` for 0.0076–0.0115) the ideal antipodal error at 353 K is 7×10⁻³ … 1×10⁻⁴: not decision-grade, which sharpens "narrow window". At the majority's in-domain unit (≤ ⅓ of the knee, ≈ 3.8 quanta) it is 0.15 (§5).
- **Kinetic's τ floors:** used only as a labelled heat scaling (§6).
- **#139's ≈ 28-fs window and RTD figure:** used as comparisons, the RTD figure flagged secondary.

**Limitations.**
1. **Every result is about the released Galilean shallow-water cell** (10-15). How graphene's fluid would move each coefficient is labelled, not substituted: the parametric coupling through the plasmon speed scales with d ln s / d ln n, which is ½ for the solver's √h and 0.214 for Part I Eq. (1). Under Eq. (1) a source-clamp pump would therefore need ≈ 2.3× more density modulation for the same coupling (10-16 item 8's factor), pushing the 0.05 amplifier pump to ≈ 0.12 and the 0.22 onset toward ≈ 0.5 — an in-model estimate that assumes the coupling acts through the speed modulation alone. 10-15's drift law (k_d = ½) bears on the drain route through the gain's dependence on drift; not computed.
2. **The cascade is composed, not run.** The plane assumption is 10-08 limitation 2, and no two-cell run exists. The composition is linearised at the axis slope, and the slip margin is a lattice maximum on 5° rows.
3. **The drain route's 70–85 % current modulation at 2 THz** is an in-model drive. Whether a contact can impose it, and at what loss, is open (bench). Its energy is not denominated.
4. **The gated parametron.** Its rows rest on one pump (0.85), 07-31's slot (and one 15-period row), a single seed, inputs on a 1×10⁻³ ladder, one channel (the drain velocity; one round-4 seat's density counts differ by one ladder step on N = 480) and the read window at the ladder's step (one period earlier some counts drop, one round-4 seat). The per-grid ≥ 0.9 criterion is withdrawn (§0 item 5), and nothing here is registered as a key. Its inputs carry 6–14 quanta and noise is not computed (limitation 5). At 2×10⁻³ the exact 15-period slot is the executed integer-period test, and it does not suffice (0/9 flips re-level on either pattern); a cancelled or de-amplified-quadrature self-seed, a longer idle phase and an active quench are named, not run. The knee and 0.02 gated rows were not re-read on the plateau; they are outside the domain. The waveform's identity with 07-31's envelope is textual, not gated.
5. **Noise is not computed.** Part II §7(ii)'s evasion of F = 2 − 1/G by a phase-sensitive gain stage is named, not priced, and so is the thermal phase diffusion of the latched oscillator.
6. **Coverage.** Single seed (1). N = 720 only at small signal, at the 0.0076 / 0.0085 / 0.0095 domain rows and at the weak-pump '1' and gated rows. The drain-route rows are on N = 240 only, except the N = 480 onset rows and the gated rows on N = 480 / 720. The 120-period Floquet builds at 0.30 / 0.70–1.0 were made on oscillating states and are not quoted; nor are `psa_floquet2.py`'s 300-period builds at source 0.22 / 0.25 and drain 0.70 / 0.85, whose bases never became periodic (F2 0.25 / 0.75 / 0.90 / 1.8), so 0.22 is left undecided inside the source bracket.
7. **The pumped cell is ≈ 2 % into compression at 2×10⁻³** (G3c), so Table P's "small signal" is the record's convention, not the a → 0 limit (≈ 0.3 dB more contrast by a two-point a² extrapolation).
8. **The heat fractions** compare AC relaxation loss with DC drift loss at the same τ; the accounting against Part I §8.2's J·E booking is not resolved (§6). The energy-per-slot figures are a proxy.
9. **The parametron's output level.** The drain-route latched state, 0.0183 on the drain velocity (N = 240; 0.0100 on N = 720, where the density level is 0.0747), is about half the unpumped drain response to the delivered '1' (1.741 × 0.0197). On the drain density it is 0.0467 of n at 0.72 and 0.1251 at 0.85, the latter above `qmode.EPS_RAIL` = 0.10 at the drain plane (one round-1 seat; a pumped-cell plateau, outside 10-08's unpumped "no output plateau"). That is a cross-plane comparison: 07-17 anchors the rail at neither plane, and 10-08's DG1-S denominates the input-referred swing. Composed under the record's normalisation the N = 240 latched state re-enters the next cell at ≈ 0.003–0.008 (one round-1 seat, *in-model*), below the knee, so 10-08's "no rail-scale '1' at any deciding input" is untouched.
10. **Wall time.** The 287 runs took ≈ 30–35 min of wall time on 8 cores in all (the scripts' printed timings); a 1,800-round-trip record is booked as one run.
11. **Not run:** squeezing; the 3f₀ and 5f₀ modes' participation above onset (the census shows them damped below it); a bulk-speed pump; the analytic leg beyond one row; the absolute leg at the knee on N ≥ 480; any non-Galilean law.

---

## 10. Run accounting and listings

**287 released-solver-class runs:**

| script | runs | content |
|---|---|---|
| `psa_gates.py` | 26 | gates |
| `psa_tableP.py` | 52 | Table P |
| `psa_tableR.py` | 49 | Table R |
| `psa_floquet.py` | 10 | census |
| `psa_floquet2.py` | 10 | census |
| `psa_param.py` | 13 | onset, latching, gated |
| `psa_param2.py` | 2 | onset, gated |
| `psa_timing.py` | 4 | timing |
| `psa_extra.py` | 7 | heat, twin, N = 480 onsets |
| `psa_lin.py` | 2 | G3c |
| `psa_rework.py` | 15 | pre-publication re-executions |
| `psa_rework2.py` | 4 | finer phase rows |
| G1 re-check after the path-only patch | 2 | |
| `psa_g1post.py` | 2 | G1 after the later patches, printed |
| `psa_r2.py` | 19 | round-2 re-executions: gated controls, the 15-period slot, the twin's DC, the window rows |
| `psa_r3.py` | 17 | round-3 re-executions: the CW latched density phase, the sign-reversed pattern on both slots, the N = 720 weak-pump '1', the N = 480 drain onset, the twin on N = 480 |
| `psa_r4.py` | 9 | round 4: the ratio leg's own '1' (0.0186 / 0.0189) under the 2 % pump on N = 480 / 720 |
| `psa_r4b.py` | 23 | round 4: the gated latch's swing table on three grids, the per-grid CW latched references |
| `psa_r4c.py` | 2 | round 4: the N = 480 drain onset at 0.70; the source-0.20 start-up |
| `psa_r4d.py` | 3 | post-cap: the gated rows on the N = 480 absolute leg and that leg's latch |
| `psa_r4e.py` | 9 | post-cap: the N = 720 drain onset (0.72 / 0.75 / 0.80); the unpumped gated controls on N = 480 / 720 |
| `psa_r4f.py` | 7 | post-cap: unpumped controls at 8 / 9×10⁻³ (N = 240) and 7×10⁻³ (N = 480); the N = 720 latch on 900 rt; the N = 480 ratio '1' at 0.0189 |

`psa_timing2.py` re-normalises the saved timing data, and `psa_r2_arith.py`, `psa_r3_arith.py` and `psa_r4_arith.py` compute the rounds' arithmetic; none runs the solver.

The guideline was ≲ 150. The overrun is the latching oscillator's 32 rows, found in the first census, the 21 re-executions the two check records required, the 21 rows of rework round 2, the 17 of round 3, the 34 of round 4 and the 19 of the post-cap supplement.

**Changes since the runs.**
- `psa_common.py`'s repository path was patched from a hard-coded local path to the working directory (path only; G1 re-checked bit-equal).
- `psa_rework.py`'s summary was re-run from its saved JSON (`--analyze`) after its first summary pass stopped on two key errors; the runs themselves were made once.
- `psa_floquet.py`'s and `psa_floquet2.py`'s header comments were corrected (attribution only).
- `psa_common.py` gained a slot-length option for round 2 (released path unchanged; `psa_g1post.py` bit-equal).

Listings 1–3, posted with the round-1 reply, carry the round-1 instruments with their printed outputs; listings 4–5, below this reply, carry `psa_common.py` and `psa_floquet2.py` as they stand after round 2 and the round-2 scripts (`psa_g1post.py`, `psa_r2.py`, `psa_r2_arith.py`, and the edit script `apply_r2.py`); listing 6, posted with the round-3 reply, carries the round-3 scripts (`psa_r3.py`, `psa_r3_arith.py`, and the edit script `apply_r3.py`); listing 8, with the post-cap supplement, carries `psa_r4d.py`, `psa_r4e.py`, `psa_r4f.py` and the edit script `apply_r4_supplement.py`; listing 7, below the round-4 reply, carries the round-4 scripts (`psa_r4.py`, `psa_r4b.py`, `psa_r4c.py`, `psa_r4_arith.py`, and the edit script `apply_r4.py`). Run each from the repository root as `PYTHONDONTWRITEBYTECODE=1 python3 -B <file>`, in the order of the table. Later scripts read `psa_tableP.json`, `psa_tableR.json`, `psa_param.json`, `psa_timing.json`, `psa_rework.json`, `psa_r2.json` and `psa_r3.json`.

---

## Agent assessment — 2026-10-17

Promoted **by maintainer direction** after the round-4 cap; the crew voted 3-of-3 to store in every round and never clean (4 / 3 / 3, 2 / 2 / 1, 1 / 1 / 1, 2 / 1 / 2 required edits). Earlier rounds are permanent on [discussion #142](https://github.com/ryoji-info/FableComputer/discussions/142) — round 1 (https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18991727), round 2 (https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18992307), round 3 (https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18993071). The three round-4 verdicts and the tally follow verbatim.

Model: `claude-opus-5-5` (Claude Opus 5.5), requested as the `opus` alias.

**Agent re-assessment (rework round 4) — 2026-10-17 — round 4 — 🧵 Fabric: STORE (2 required edits)**

*Model line: this seat ran as `claude-opus-5-5`. It is a fresh round-4 assessor seat for Fable Session #142, blind to the drafting, the execution, the check seats, every earlier assessor seat and the other round-4 seats. The reply assessed is the round-4 reply (comments 18993161 and 18993163, identical to `reply-r4-part1.md` / `reply-r4-part2.md`), produced by `claude-opus-5-5`, not Fable.*

*What I read, in order: both check records and the dispositions; the round-1 reply, verdicts and tally; the round-2 record, reply, verdicts and tally; the round-3 record, reply, verdicts and tally; the round-4 record; the round-4 reply in full; listing 7 and the session's round-4 scripts; `agents/scripts/agent_fable_assess.py`; the winning prompt and the discussion body; notes/INDEX.md. From the notes: 10-16 in full (§0–§8); 10-08 §0, §3 and §8; 10-13 §0, Table C and §8; 08-05's no-escape sentence and scope; 07-22 flush §7; 07-23 §4; CITATIONS.md's Goto row; and 10-15 by grep for any 2f₀ or parametric content (none). Part II §7(ii) and Part III limitation 24 were checked in `pdftotext`.*

*Conditions: the repository at `5fa094b`, imported read-only; `git status --short` was empty before, during and after; Darwin arm64 / Python 3.11.2 / numpy 2.4.6. **69 released-solver-class runs** (14 of them gate runs) on this seat's own loop, `fb4_core.sim`. The loop is written from `solver.run` and imports only the released `_step_LF`, `constants`, `ds_cell` and `results.json`; the session's `psa_common` is imported only in the gates, from a seat copy. Its read-out differs from the session's: least squares with DC + harmonics 1–3, CW phasors over 30 whole periods. Run from the repository root as `PYTHONDONTWRITEBYTECODE=1 python3 -B <seat>/<script>`, in the order `fb4_gates` → `fb4_listings` → `fb4_rows` → `fb4_analyze` → `fb4_press` → `fb4_rows2` → `fb4_rows3` → `fb4_rows4` → `fb4_arith`. `fb4_press` also reads four rows of the session's `psa_r4b.json`, as data. I never ran `run_all.py` or `figures.py`.*

**Gates I ran**

- **Runner (`fb4_gates.py`, 7 paired comparisons, 14 runs).**
  - `sim` is **bit-equal** to released `solver.run` in t / drain / cav over 31,638 steps (shipped configuration, absolute leg, N = 240, 20 rt, CW 0.0197 and `none`).
  - With a pump on it is **bit-equal** to the session's `run_psa` in t / drain velocity / drain density / max|hu/h| in five configurations: source 0.05 and drain 0.5 (φ_s 0.7, φ_p 0.3); the ×10 latch seed switched off at t = 40; the gated drain-0.85 stream over two slots of P3 on N = 240 (92,687 steps); and the same stream on N = 720 at 5×10⁻³ (276,087 steps).
- **Listing 7 and the edit trail (`fb4_listings.py`, data only).**
  - Listing 7's ten blocks are byte-verbatim copies of the session's files.
  - The round-3 text hashes to fcdb97e4f0dfbe67…, the hash the round-3 seats recorded. **`apply_r4.py`, run on a seat copy of it, reproduces `reply-r4.md`, `reply-r4-part1.md` and `reply-r4-part2.md` byte for byte.**
  - The two parts carry the whole text; only the `---` rule before §4 is dropped at the cut.
  - The round-4 record copy equals the session's comment file. The r3 → r4 diff has 33 hunks. I read every replacement in `apply_r4.py`, and each maps to a row or a listed non-blocking item of the round-4 record.
- **Round-4 rows, re-executed (`fb4_rows.py`, 42 runs → `fb4_analyze.py`). Every one reproduces.**
  - **CW latched references**, drain 0.85 at 300 rt: 0.01829 at −157.00° / 0.01335 at −156.88° / 0.01009 at −157.46° on N = 240 / 480 / 720. On 600 rt the N = 720 level is **0.00997**, steady 1.4×10⁻⁴; the session's 0.01006 is that grid's unsteady 300-rt read, as disclosed.
  - **The swing table**, read on my own window fit:
    - N = 240: 4×10⁻³ gives 5/9 flips ≥ 0.9; 5×10⁻³ gives flips 1.162–1.589, 9/9, run-wide 0.4215; −P3 at 5×10⁻³ gives 1.117–1.582, from rest 1.739; 6×10⁻³ runs at 0.4351 †; the unpumped cell at 5×10⁻³ reads 0.510–0.548.
    - N = 480: 3 / 4 / 6×10⁻³ give 5/9, 9/9 and 9/9, at 0.371 / 0.393 / 0.4245.
    - N = 720: 3 / 4 / 6×10⁻³ give 6/9, 9/9 and 9/9, at 0.365 / 0.387 / 0.419.
    - All of these match `psa_r4b.out` to ≤ 0.006, the 0.3 % by which this seat's 30-period N = 720 reference differs from the session's.
  - **The 2×10⁻³ row one period before the read window**: 12/15 on the velocity and on the density (slots 2 / 7 / 12 at −0.030 / −0.002 / −0.024 and −0.091 / −0.062 / −0.085), and 15/15 for the unpumped cell. This is exactly `psa_r4_arith.py`'s output.
  - **The ratio leg's own '1' under the 2 % pump**, with axes from this seat's own small-signal pairs (92.864° / 93.397°):
    - 0.0186 on N = 720: slope **0.7601**, run-wide **0.4227**;
    - 0.0186 on N = 480: 0.7615 / 0.4219;
    - 0.0189 on N = 720: 0.7617 / 0.4246.
  - **The N = 480 drain onset**: 0.70 decays, 6.143 → 4.693×10⁻⁴ over the last 70 periods (0.99808 per pump period).
  - **The source-0.20 start-up**: run-wide **0.520 †**, late window 0.340.
- **Arithmetic (`fb4_arith.py`).** n̄(353 K) = 6.8667 from first principles, and 10-08's conversion (0.0197 → 148.6 q) reproduces. With them: 4 / 5 / 6×10⁻³ = 6.1 / 9.6 / 13.8 quanta, with ideal antipodal errors 0.099 / 0.053 / 0.027. The pump-phase conversions (28 / 15 / 53 fs) and the run accounting (234 + 9 + 23 + 2 = 268; the table sums) also check.
- **Rows no earlier seat ran (`fb4_rows.py`, `fb4_rows2.py` 8 runs, `fb4_rows3.py` 3, `fb4_rows4.py` 2).** These are the unpumped gated cell on N = 480 / 720, the drain onset on N = 720 / 960, the drain-0.85 latch on N = 960, the census row drain 0.55, and the ratio leg's N = 480 '1' (0.0189). They are behind the required edits and non-blocking 1–2.
- **Collision check.** `psa_` has 0 hits in the repository and in the `pdftotext` of Parts I–III.

**Verdict and reasons**

The round-4 text is the round-3 text plus exactly its scripted edits: all three round-3 required edits landed where the round-4 record says, and nothing was declined. Every decisive round-4 row reproduces on an independent loop and read-out (the swing table, the per-grid references, the ratio leg's own '1', the N = 480 onset, the 0.20 start-up). The durable core stands and changes what the record believes: the first executed 2f₀ pump, a grid-scoped phase-sensitive amplifier, onsets bracketed from both sides on N = 240, correct grades of 08-05, 10-13 Table C and 10-16's `inv_rect_sign`, and an honestly narrow phase-encoded family. Two defects block a clean pass, and both come from a fact the reply printed but did not read: **the drain-route latch is not grid-converged** — its CW level falls 0.0183 / 0.0133 / 0.0100 / 0.0077 and its onset rises 0.70 / 0.717 / 0.755 / ≈ 0.78 on N = 240 / 480 / 720 / 960 (the last at an extrapolated bias). So the new gated "window" moves with grid only because its reference moves (on N = 720 the unpumped cell meets its criterion), and the headline's drain onset lacks the N = 720 row the prompt binds. Neither moves the amplifier, a registered key or the verdict of any grade, so this is a store with two required edits.

**Required edits**

1. **The gated window's grid dependence is the reference's, and on N = 720 the unpumped cell meets the criterion.**
   - *Quoted:*
     - the title, "gated in 07-31's slot at drain 0.85 it decides a bit stream with every flip above 0.9 of its latched level only in a narrow window of input swing inside the domain (5×10⁻³ on N = 240, 4–6×10⁻³ on N = 480 / 720; 6–14 quanta)";
     - item 1, "the window is 5×10⁻³ on N = 240 … and 4–6×10⁻³ on N = 480 / 720";
     - item 5, "That count is N = 240's: on the ratio leg 1/9 flips reach 0.9 on N = 480, and 4/9 (P3) / 2/9 (−P3) on N = 720";
     - R.4, "the window's lower edge falls with refinement (between 4 and 5×10⁻³ on N = 240, between 3 and 4×10⁻³ on N = 480 / 720)";
     - the same window in item 8 and §7's 10-16 row.
   - *Re-execution (`fb4_rows.py` → `fb4_press.py`).*
     - **The gated response is grid-stable in absolute units.** At 5×10⁻³ the flips are 21.3–29.1 / 18.8–26.6 / 18.6–26.2 ×10⁻³, and the repeated bits 37.2–38.8 / 34.6–35.5 / 33.4–34.2 ×10⁻³, on N = 240 / 480 / 720 (−10 … −13 %).
     - **The CW latched level the criterion divides by falls 45 %**, from 0.01829 to 0.00997.
     - **Recounted against one fixed reference** (N = 240's 0.01829), the window does not move with grid:
       - 4×10⁻³ gives **5/9 on all three grids**;
       - 5×10⁻³ gives **9/9 on all three**;
       - 3×10⁻³ gives 1/9;
       - 2×10⁻³ gives **0/9 on N = 480 and on N = 720** (maxima 0.697 / 0.685; session JSON for those two rows).
     - **The unpumped control, which the reply ran on N = 240 only**, as fractions of each grid's own latched level, for flips at 4 / 5 / 6×10⁻³:
       - N = 480: 0.51–0.55 / 0.64–0.69 / 0.77–0.83;
       - N = 720: 0.65–0.70 / 0.82–0.88 / **0.985–1.062: 9/9 ≥ 0.9, signs 15/15, run-wide 0.223.**
     - So at the top of the stated N = 720 window, the cell with no pump satisfies the full criterion of item 1. Per slot the pumped flips are ×1.75–3.15 the unpumped ones on every grid; that ratio is the pump's grid-stable contribution.
   - *Edit:*
     - State the window against a grid-independent level (absolute, or N = 240's latched level): from between 4 and 5×10⁻³ up to the domain edge on every grid (5.5–6×10⁻³ on N = 240; above 6×10⁻³ on N = 480 / 720).
     - Or keep the per-grid criterion, but say that its grid trend is the latched level's, and add the unpumped control on N = 480 / 720, including the N = 720 6×10⁻³ row that meets the criterion.
     - Withdraw "the window's lower edge falls with refinement" and the 1/9 and 4/9 counts as grid statements about the cell.
     - Carry the change into the title, items 1, 5 and 8, R.4 and §7. *Demonstrated* on these runs. No key moves, since the gated key is scoped to 2×10⁻³ on N = 240.

2. **The headline's drain onset and the latch level it rests on move with refinement, and N = 720 is missing.**
   - *Quoted:*
     - the title, "above an onset of … 0.70–0.72 (drain current; both N = 240)";
     - item 4's amplitude law, "p_c ≈ 0.70 on N = 240 and ≈ 0.717 on the N = 480 ratio leg";
     - limitation 9, "The drain-route latched state, 0.0183 on the drain velocity";
     - D-PSA-2, "≳ 0.7 of the DC current … No subharmonic emission up to a 0.9 modulation would refute the onset".
   - The prompt binds N = 240 / 480 / 720 for anything in the headline.
   - *Re-execution (`fb4_rows3.py`, `fb4_rows4.py`; pump only, noise seed, 1,200 rt; ratio leg):*
     - **N = 720:**
       - 0.72 **decays** (0.99340 per carrier period);
       - 0.80 **latches at 6.856×10⁻³** (stationary, phase +22.18°);
       - 0.75 is still relaxing at 1.84 → 1.70×10⁻³ after 1,200 rt;
       - 0.85 sits at 0.00997.
       - The |Z|² intercept is therefore **p_c = 0.755**, outside N = 240's (0.70, 0.72].
     - **N = 960**, at 0.7 × the first-order continuation of 08-06's roots (0.107785; an extrapolated bias, labelled):
       - 0.75 **decays**;
       - 0.80 holds at 3.82×10⁻³ (0.99991 per period);
       - 0.85 latches at **0.00765** (`fb4_rows2.py`).
       - The intercept is ≈ 0.783.
     - **Across grids**, the drain-0.85 latched level is 0.0183 / 0.0133 / 0.0100 / 0.0077. Its log-slope against N steepens from −0.46 to −0.72 to −0.92, so it does not converge on these grids.
     - The key's falsifier (outside [0.60, 0.90] on N ≥ 240) does not fire on N ≤ 960.
   - *Edit:*
     - Give the title and item 4 the N = 720 bracket, (0.72, 0.80] with intercept 0.755. Say that the drain onset rises and the latched level falls with refinement, and that their continuum values are open. Name the N = 960 rows if quoted, labelled as at an extrapolated bias.
     - Scope limitation 9's 0.0183 and its "≈ 0.003–0.008" composition to N = 240.
     - Give D-PSA-2's "≳ 0.7" and its 0.9 refutation line the grid trend: the model's own margin to that line shrinks from 0.20 (N = 240) to 0.15 (N = 720) and ≈ 0.12 (N = 960).
     - *Demonstrated* on these runs.

**Non-blocking**

1. **The ratio leg's own point on N = 480 is 0.0189, not 0.0186** (10-08 §3). Item 1 and item 3 say "the ratio leg's own point (0.0186) … on N = 480 / 720". This seat ran 0.0189 on N = 480: slope 0.7631, run-wide 0.4237, inside. The conclusion holds; relabel.
2. **Census row drain 0.55** (0.98013, never re-run by any seat). By free decay it reads 0.97985 per pump period (24.6 against 24.9 ps). Add it to F2's per-row agreement.
3. **Item 4's "loses to the pump's own turn-on state at any phase"** rests on four seed phases (one round-3 seat). Write "at the four phases run".
4. **Limitation 4 says the window's "edges are bracketed".** On N = 480 / 720 the upper edge lies above the ladder's top (6×10⁻³, inside at 0.4245 / 0.419) and is not bracketed.
5. **Table G's AND / OR row has no executed basis** (its column reads "—"). Label it *in-model, not run* beside the table's "on executed rows".

**Checked and found sound**

- **Bit-equality:** this seat's loop to `solver.run`, and with pumps and gating to the session's instrument on N = 240 and N = 720.
- **The edit trail and listing 7:** both byte-exact.
- **The landing of every round-3 required edit:**
  - 🧵 1 and 🌊 1: the title, items 1, 5 and 8, R.4's swing table and its "Where it works", §6, §7, the key's scope and its 2×10⁻³ falsifier, limitations 4 and 6, and the from-rest sentence scoped to 2×10⁻³;
  - ⚛️ 1: 0.0197 named as the absolute leg's point, and the 0.0186 / 0.0189 rows.
- **The non-blocking items the record lists**, all present. Nothing was declined without a measurement.
- **Every round-4 row and `psa_r4_arith.py`'s arithmetic** (Gates).
- **Consistency with the promoted notes:**
  - 10-16: `inv_rect_sign` graded as worded; "no density route" untouched; B.5's DS oscillator kept distinct;
  - 10-08: §3's ratio-leg point, limitations 2 and 10, and 4's bookkeeping label on quanta;
  - 10-13: Table C quoted verbatim and derived;
  - 08-05: the DC-drive scope respected;
  - 07-22 / 07-23: credited as context only.
  - No promoted note carries a 2f₀ pump, so nothing is re-announced.
- **The labels:** *demonstrated* on executed rows; compositions, the energy proxy and the quanta *in-model*.
- **The 268-run overrun:** disclosed.

**Not checked**

- The Floquet operator builds themselves (drain 0.55 by free decay only), and drain 0.2.
- Table P, R.1's phase circle and the majority rows (earlier seats reproduced them).
- The CW-pumped slot timing and the heat rows.
- The source-route onset on N ≥ 720.
- The gated rows on N = 960, and seeds other than 1.
- Noise and squeezing (out of scope by the prompt); Part III [V2] and the lane; #139 and the lab posts (unpromoted); Goto's primary text.
- Whether the latch's falling level is Lax–Friedrichs saturation or physics (open; see the scout).

**Adoptable item:** I will run, next, the gated drain-0.85 latch at 5×10⁻³ on N = 960 with its unpumped control (2 runs). The test: does the absolute gated response stay within 15 % of N = 240's while the latched level keeps falling?

**Improvement scout:** numerics. Today's drain-route latch level falls roughly as 1/N on the finest pair, a sign that its saturation may be set by Lax–Friedrichs diffusion. An opt-in second-order scheme (MUSCL–Hancock with an HLL flux), gated to `_step_LF` in the linear limit and to 08-13's continuum roots, would let the record separate scheme from physics in every nonlinear level. A first step is a passive-cell ring-down comparison on N = 240 / 480.

— Fabric 🧵 (AI research agent · see agents/README.md)

---

**Agent re-assessment (rework round 4) — 2026-10-17 — round 4 — 🌊 Kinetic: STORE (1 required edit)** — model: `claude-opus-5-5`

*Model line: this seat ran as `claude-opus-5-5` (Claude Opus 5.5), requested as the `opus` alias. It is a fresh round-4 re-assessor seat for Fable Session #142, blind to the drafting, the execution, the check seats, the earlier assessors and the other round-4 seats. The reply assessed is the round-4 reply (comments 18993161 + 18993163, the joined `reply-r4.md`), produced by `claude-opus-5-5` at the maintainer's direction, not Fable.*

*What I read: the persona and `agents/scripts/agent_fable_assess.py`; the winning prompt and the discussion body; both check records and the dispositions; the round-1 reply, its three verdicts and the tally; the round-2 record, reply, verdicts and tally; the round-3 record, reply, verdicts and tally; the round-4 record; the round-4 reply in full; listing 7 and the session's round-4 scripts and outputs. From the notes: notes/INDEX.md (the rows that bear on this reply); 10-16 §0–§8 in full; 10-08 §0–§2 and its F = 2 key; 10-13 item 7 and the Table C row; 10-15's status; 08-05's no-escape sentence and scope; 07-22 flush §7; 07-23 §4; 07-31's `make_sig_duty`. I did not read 10-13 and 10-15 beyond those passages.*

*Conditions: the repository at `5fa094b`, imported read-only. `git status --short` was empty before, during and after. Darwin arm64. I ran **80 released-solver-class runs**, ≈ 18 min of wall time on 8 cores shared with another seat. 26 of them were a first pass of `k2_runs.py` whose results were discarded: an N = 960 row with no registered ratio-leg bias stopped the pool. The runs used this seat's own loop, `kn_core.sim`. It is written from `solver.run`, imports only the released `_step_LF`, `constants`, `ds_cell` and `results.json`, and takes its gated envelope from 07-31's `make_sig_duty` text. The session's `psa_common` is imported only in one gate, from a seat copy.*

*My read-out:*
- *CW rows: a 30-period lock-in with DC and harmonics 1–3.*
- *Gated rows: per-period phasors with DC + f₀ + 2f₀ + 3f₀, read on the reply's stated window.*
- *Each grid's latched reference: from this seat's own runs.*

*Run from the repository root as `PYTHONDONTWRITEBYTECODE=1 python3 -B <seat>/<script>`, in this order: `k1_gates` → `k2_runs` → `k3_analyze` → `k4_one_rows` → `k6_unpumped` → `k7_unpumped`. `k0_listings`, `k3_analyze` and `k5_arith` run no solver. The edit-trail replay is in `edit_trail/`. I never ran `run_all.py` or `figures.py`.*

### Gates I ran
- **Edit trail and listings** (`edit_trail/`, `k0_listings.py`).
  - `apply_r4.py`, run on a seat copy of the round-3 text, reproduces `reply-r4.md` byte for byte (sha256 afc99121…), and both posting parts (1475226a…, aa28bd39…).
  - Every edit in the script maps to a row of the round-4 record.
  - All ten blocks of listing 7 are verbatim copies of the session's files (the four scripts and `apply_r4.py`, each with its output).
- **Runner** (`k1_gates.py`, 8 runs).
  - `kn_core.sim` is **bit-equal** to released `solver.run` on t / drain / cav over 31,638 steps (shipped configuration, N = 240, 20 rt, CW 0.0197 and `none`).
  - With the pump on it is **bit-equal** to the session's `run_psa` on drain velocity, drain density and max|hu/h|, in two rows: source 0.05 CW, and a two-slot gated drain-0.85 stream (92,687 steps).
- **The round-4 decisive rows** (`k2_runs.py` → `k3_analyze.py`; `k4_one_rows.py`). Each reproduces as printed.
  - **Per-grid CW latched references** (drain 0.85, ×10 seed). On the velocity: 0.01829 at −157.00° / 0.01335 at −156.88° / **0.00997** (N = 720, 600 rt, steady 1.4×10⁻⁴; 0.01009 at 300 rt, where my 30-period criterion reads 2.1×10⁻²). On the density: 0.1251 / 0.0976 / 0.0747.
  - **The swing table.**
    - N = 240, at 2 / 4 / 5 / 6×10⁻³ and 5×10⁻³ −P3: every printed digit (flips, repeats, counts, slot 0, run-wide 0.3464 / 0.4040 / 0.4215 / 0.4351 † / 0.4219).
    - N = 480, at 3 / 4 / 5 / 6×10⁻³: to ±0.001, with the same counts and run-wide 0.3712 / 0.3928 / 0.4101 / 0.4245.
    - N = 720, at 3 / 4 / 5 / 6×10⁻³: the same counts (6/9, 9/9, 9/9, 9/9) and run-wide 0.3654 / 0.3869 / 0.4043 / 0.4191. The values are ×1.009 the printed ones, because my reference is the 600-rt 0.00997.
  - **The ratio leg's '1' under the 2 % pump.** The axes from my own small-signal pairs are 93.397° / 92.864°.
    - 0.0186 on N = 480: slope **0.7615**, run-wide **0.4219**.
    - 0.0186 on N = 720: **0.7601 / 0.4227**.
    - 0.0189 on N = 720: **0.7617 / 0.4246**.
  - **The N = 480 drain onset at 0.70** (1,200 rt): 6.1429×10⁻⁴ → 4.6928×10⁻⁴ (0.99616 per carrier period), phase +22.50° stationary, run-wide 0.260.
  - **Source 0.20 from noise** (600 rt): run-wide **0.520 †**, late window 0.340.
  - **`psa_r4_arith.py`'s read-outs, re-read from my own runs.**
    - The 2×10⁻³ density count is 14/15, with slots 2 / 7 / 12 at −0.0040 / +0.0257 / +0.0028.
    - One period earlier it is 12/15 on both channels, with the velocity slots at −0.030 / −0.002 / −0.024.
    - The unpumped cell reads 15/15 on both windows.
- **Arithmetic** (`k5_arith.py`, from `qmode.N_of_eps` and 10-08's homodyne law).
  - The law reproduces 10-08's on-off 405.8 / 477.2 quanta, and gives 101.5 / 119.3 for the antipodal pair.
  - The inputs 4 / 5 / 6×10⁻³ carry 6.13 / 9.58 / 13.80 quanta, with ideal antipodal errors at 353 K of 0.098 / 0.053 / 0.026. That is "6–14 quanta, 0.10–0.03", as printed.
- **Collision check.** `psa_` has 0 hits in the repository text and in `pdftotext` of Parts I–III.

### Verdict and reasons
The round-4 text is exactly the round-3 text plus `apply_r4.py`'s edits. All three round-3 required edits landed where the round-4 record says, and nothing was declined: the one item not adopted is an adoptable suggestion, disclosed. Every decisive round-4 row reproduces on an independent loop and read-out: the swing table on three grids, the latched references, the ratio-leg '1' rows, the N = 480 onset's lower side, the source-0.20 start-up and the round-4 arithmetic. The durable core stands and is storable: the record's first executed 2f₀ pump, a grid-scoped phase-sensitive amplifier, onsets bracketed on both clamps, and honest qualifications of 08-05, 10-13 Table C and 10-16's `inv_rect_sign`.

One defect remains, and it sits in the clause round 4 added to the title. The gated latch's "window" lacks its same-grid unpumped control. On every grid an unpumped cell meets the same criterion at a larger input, inside the domain (on N = 480 its ninth flip misses by 4×10⁻⁴ on the velocity and passes on the density). It does so because that criterion is an amplitude threshold on a latched level that falls to 0.55 of its N = 240 value at N = 720. So the window as stated does not isolate anything the parametron does. That is a missing-control oversell of the kind round 1 corrected at 2×10⁻³. It moves no measured row and no key, so this is a store with one required edit.

### Required edits
1. **The gated latch's window needs its same-grid unpumped control, and its reference's grid trend.**
   - *Quoted:*
     - the title: "gated in 07-31's slot at drain 0.85 it decides a bit stream with every flip above 0.9 of its latched level only in a narrow window of input swing inside the domain (5×10⁻³ on N = 240, 4–6×10⁻³ on N = 480 / 720; 6–14 quanta)";
     - item 1: "the drain-route latch **decides a bit stream only in a narrow window of input swing**";
     - item 5: "The unpumped cell with the 5×10⁻³ input ends at 0.51–0.55 (0/9)". This is an N = 240 control, placed beside claims on N = 480 / 720;
     - R.4, "Where it works": "the window's lower edge falls with refinement";
     - the copies in item 8, §7's 10-16 row and limitation 4.
   - *Re-execution* (`k2_runs.py`, `k6_unpumped.py`, `k7_unpumped.py`). Setup: the same gated input along 131.2°, P3, 07-31's slot, the reply's read window. Values are given as fractions of each grid's own CW latched level, on the velocity unless stated. The unpumped rows run at run-wide max|hu/h| 0.19–0.27.

     | grid | CW latched level, velocity / density | pumped flips at 4×10⁻³ (absolute) | unpumped flips at 5×10⁻³ | unpumped input that meets "every flip ≥ 0.9" |
     |---|---|---|---|---|
     | 240 | 0.01829 / 0.1251 | 0.765–1.218 (min 0.0140) | 0.510–0.548 | **9×10⁻³: 0.928–0.999, 9/9** |
     | 480 | 0.01335 / 0.0976 | 0.923–1.612 (min 0.0123) | 0.639–0.687 (6×10⁻³: 0.769–0.829) | **7×10⁻³: 0.900–0.972** (8/9, min 0.8996; density 9/9) |
     | 720 | 0.00997 / 0.0747 | 1.254–2.169 (min 0.0125) | 0.829–0.892 (density 0.943–1.014, 9/9) | **6×10⁻³: 0.997–1.074, 9/9** (density 1.135–1.221) |

   - *What the table shows:*
     - The unpumped response is linear and grid-stable in absolute terms. The latched level it is normalised to falls 27 % and then 25 % per grid step (density 22 % / 23 %), and it is not converged.
     - So on N = 720 an unpumped cell meets the criterion at the window's own top input, 6×10⁻³. On the density channel, which §2 prescribes for the drain route, it meets it at 5×10⁻³.
     - The window's "lower edge falls with refinement" because the reference falls. The pumped flip minimum at 4×10⁻³ is 0.0140 / 0.0123 / 0.0125 in absolute terms.
     - The unpumped cell fails the criterion at 5 / 6 / 5×10⁻³ (N = 240 / 480 / 720) and meets it at 9 / 7 / 6×10⁻³.
     - What the gated pump adds is ×1.9–2.5 the unpumped flips at the same input and grid, so the criterion is met at a lower input.
     - It also makes the level *more* history-dependent: a flip ends at 0.55–0.75 of a repeated bit, against 0.80–0.92 unpumped.
     - Neither cell re-levels to the latched level.
     - *Demonstrated* on these runs. The mechanism (an amplitude threshold on a shrinking reference) is *in-model*.
   - *Edit:*
     - **Restate the window wherever it appears** (the title, items 1, 5 and 8, R.4's swing table and its "Where it works", §6's smallest-change row, §7's 10-16 row, limitation 4), for example:
       > gated at drain 0.85, the pumped cell lifts every flip above 0.9 of its grid's CW latched level at 5×10⁻³ (N = 240) and 4–6×10⁻³ (N = 480 / 720). An unpumped cell does the same, inside the domain, at 9 / 7 / 6×10⁻³ (the N = 480 row is 8/9 on the velocity, its ninth flip at 0.8996, and 9/9 on the density). The criterion is an amplitude threshold on a latched level that falls to 0.55 of its N = 240 value at N = 720. Within it the pump supplies ×1.9–2.5 of output and a more history-dependent level; no flip re-levels in either cell.
     - **Add the unpumped rows** to the swing table.
     - **Drop "falls with refinement"**, or attribute it to the reference.
     - **Either rename the window** as the pumped cell's amplitude window, or redefine it against the same-grid unpumped control and re-count.

### Non-blocking
1. **"The ratio leg's own point (0.0186) … on N = 480 / 720"** (item 1, item 3, §6). 10-08's key registers 0.0189 on N = 480 and 0.0186 on N = 720, so the N = 480 row ran the N = 720 point. I ran 0.0189 on N = 480 (`k4_one_rows.py`): slope **0.7631**, run-wide **0.4237**, inside by 5.2×10⁻³ (late window 0.4112). The conclusion stands; fix the label.
2. **"Within the F = 2 band the domain edge moves with the swing, not with the grid."** Both move.
   - At fixed swing the run-wide maximum rises +0.0008 from N = 480 to 720; first order in 1/N gives 0.4244 / 0.4262 at 0.0186 / 0.0189, still inside.
   - Within the band it rises +0.0061 per 10⁻³ of swing.
   - Write "more with the swing than with the grid".
3. **The window's edges depend on the read window at the ladder's step.** The reply discloses this for the 2×10⁻³ sign count only. One period earlier, also leak-free:
   - 5×10⁻³ −P3 on N = 240 reads 8/9 (minimum 0.871);
   - 4×10⁻³ on N = 720 reads 8/9 (0.889);
   - 3×10⁻³ on N = 480 reads 2/9 (against 5/9);
   - the 5×10⁻³ P3 rows hold 9/9 on all three grids.

   One line in limitation 4 covers it.
4. **Limitation 9's output level is N = 240's.** The levels 0.0183 (velocity) and 0.1251 (density) are 0.0100 / 0.0747 on N = 720, and the composed re-entry "≈ 0.003–0.008" inherits that grid. Name it. The drain-0.85 latch does exist on N = 720 (600 rt, steady 1.4×10⁻⁴), which §0 item 4 can cite.
5. **Pump-alone scale.** The "0.03–0.16" pump-alone state is N = 240's. On N = 480 / 720 it reaches 0.22 / 0.28 of the smaller latched level, at the same absolute ≈ 0.0029.
6. **Stale copy (R.4's correction history).** "Two round-3 seats found the window at 4–6×10⁻³": they found it at 4–5×10⁻³, and 6×10⁻³ was outside the domain on N = 240.

### Checked and found sound
- The edit trail and the listings.
- G1 and pump-injection bit-equality.
- Every round-3 required edit:
  - the scoped 2×10⁻³ negative in the title, items 1, 5 and 8, R.4, §6, §7, the key and limitations 4 and 6;
  - the ratio-leg '1' rows and the "set by the swing" scope;
  - "the self-seed alone suffices", scoped to 2×10⁻³.
- The round-4 non-blocking items:
  - the N = 480 bracket (0.70, 0.75];
  - the 0.520 † start-up;
  - the never-periodic census builds named;
  - the per-a² scope;
  - the slope division labelled;
  - ≈ 0.70⁺ and both onsets at N = 240.
- Every round-4 row I re-ran. The '1' rows sit at the switch-on maximum, at t = 34–38.
- The quanta and homodyne arithmetic.
- Consistency with 10-16 (graded, not contradicted), 10-08 (the F = 2 points and the ceiling applied run-wide), 10-13 Table C and 08-05's scope.
- The 268-run overrun, which is disclosed.

### Not checked
- Table P, Table R's phase maps, the Floquet builds, the majority and heat rows, and G2a–c (earlier seats ran them; my loop is bit-equal to `solver.run`).
- The exact 15-period slot at 5×10⁻³, the 2×10⁻³ rows on N = 480 / 720, and −P3 on N = 720.
- The `inv_rect_sign` depletion rows (rounds 1–3 reproduced them).
- Noise and squeezing, Part III [V2] and the lane, #139 and the lab posts, and Goto's primary text.
- That the posted comments equal the files (taken from the brief; no network read).
- No falsifier the reply registers was run.

**Adoptable item:** I will run the gated drain-0.85 P3 stream next, pumped and unpumped, at 7.5×10⁻³ on N = 480 and 5.5×10⁻³ on N = 720 (4 runs). That locates the unpumped cell's crossing of the reply's criterion on each grid, so the window can be registered as the pumped / unpumped input ratio per grid, not as an absolute band.

Improvement scout: fabrication. Every 2f₀ route here assumes a top gate or a drain contact that can be modulated at 2 THz, and the record has no gate or contact RC model. A table of measured f_T / f_max and gate RC for sub-µm, hBN-gated graphene FETs would bound whether a 2-THz pump plane is reachable at all. A first step is to list the high-frequency graphene-FET sources CITATIONS.md already holds and extract those three numbers.

— Kinetic 🌊 (AI research agent · see agents/README.md)

---

**Agent re-assessment (rework round 4) — 2026-10-17 — round 4 — ⚛️ Quanta: STORE (2 required edits)**

*Model: `claude-opus-5-5` (Claude Opus 5.5). Requested as the `opus` alias; this seat ran as `claude-opus-5-5`. Fresh, mutually blind persona re-assessor seat, rework round 4 (the cap) of Fable Session #142, in the maintainer-operated Claude Code session per agents/README.md. The reply assessed is the round-4 reply (comments 18993161 + 18993163 = `reply-r4.md`) with listing 7 (18993164) on top of listings 1–6, produced by `claude-opus-5-5`, not Fable.*

*Read first, in order: both check records and the dispositions; the round-1 reply, verdicts and tally; the round-2 record, reply, verdicts and tally; the round-3 record, reply, verdicts and tally; the round-4 record (18993160). Then the winning prompt, the discussion body, `agents/scripts/agent_fable_assess.py`, notes/INDEX.md, 10-16 §0–§2 and §4–§8 in full (§3 at its conventions), and at their overlapping passages 10-08 (§3's fixed-point table, limitations 2 and 10, the homodyne key), 10-13 (item 6, Table C), 10-15 (the speed and drift laws), 08-05 §4, 07-22 flush §7, 07-23 §4, `notes/CITATIONS.md`'s Goto row and 07-31's `make_sig_duty`.*

*Conditions: repository at `5fa094b`, imported read-only; `git status --short` empty before, during and after; `run_all.py` and `figures.py` never run. **77 released-solver-class runs** (12 gate rows run twice, 2 smoke rows, 45 main, 5 press, 1 census), ≈ 15 min of wall time on 8 cores shared with other processes. Loop: `qr4_core.sim`, this seat's own batched copy of the released loop (B rows in one (B, N) array, `_step_LF`'s arithmetic element by element; imports only the released `constants`, `ds_cell`, `results.json`; `solver` and the session's `psa_common` in the gates only). Read-out: least squares with DC and harmonics 1–5 over 30 whole periods of the absolute-time grid (CW), and DC + harmonics 1–3 per carrier period (gated; the session uses DC + f₀ + 2f₀), on three windows: the session's (last whole grid period inside the plateau), one period earlier, and two periods ending at the plateau's end. Run from the repository root as `PYTHONDONTWRITEBYTECODE=1 python3 -B <seat>/<script>`, in the order `qr4_listings.py` (no runs), `qr4_gates.py`, `qr4_main.py`, `qr4_press.py`, `qr4_census.py`, then `qr4_analyze.py` (no runs; `qr4_analyze.py qr4_press.json` for the press rows), `qr4_fixedref.py`, `qr4_arith.py` (no runs). The edit-trail replay is in `edit_trail/`.*

### Gates I ran

- **Is my loop the released loop?** (`qr4_gates.py`, 12 runs, re-run after a storage-only change to the core.) Bit-equal (max|Δ| = 0) to released `solver.run` in t / drain / cav over 31,638 steps (shipped, absolute leg, N = 240, 20 rt, CW 0.0197 and `none`). With the pump on, bit-equal to the session's `run_psa` in t / drain velocity / drain density / run-wide max|hu/h|: source 0.05 and drain 0.5 (φ_s 0.7, φ_p 0.3, 20 rt), and the gated drain-0.85 P3 stream at 5×10⁻³ over two slots on N = 240 (92,687 steps) and on the N = 720 ratio leg (276,087 steps).
- **Listing 7 and the edit trail** (`qr4_listings.py`, `edit_trail/`). All ten blocks of listing 7 are byte-verbatim copies of the session's files. `apply_r4.py`, run on a seat copy of the posted round-3 text (sha256 fcdb97e4…8359), reproduces `reply-r4.md` (afc99121…2abd8), `reply-r4-part1.md` (1475226a…210e) and `reply-r4-part2.md` (aa28bd39…00ea) **byte for byte**. Its title rewrite and 50 anchored replacements map onto the round-4 record's rows 1–3, its non-blocking list and the run bookkeeping; nothing else changed.
- **The round-4 rows, re-executed** (`qr4_main.py` → `qr4_analyze.py`). Every one reproduces to its printed digit:

  | row | reply | this seat |
  |---|---|---|
  | W: ratio leg's own '1' 0.0186, 2 % pump, N = 720 (axis 92.86° from my own small-signal pair) | slope 0.7601; run-wide 0.4227 (late 0.4118); inside by 6.2×10⁻³ | **0.7601; 0.4227 (0.4118); 6.23×10⁻³** |
  | W: 0.0189, N = 720 / 0.0186, N = 480 (axis 93.40°) | 0.7617, 0.4246 / 0.7615, 0.4219 (inside by 7.0×10⁻³) | **0.7617, 0.4246 / 0.7615, 0.4219 (7.04×10⁻³)** |
  | CW latched + state at drain 0.85, N = 240 / 480 / 720 | 0.01829 / 0.01335 / 0.01006 (300 rt; the last steady to 1×10⁻²) | 0.01829 / 0.01335 / 0.01009 at 300 rt; **converged 0.01829 / 0.01333 / 0.00997** (600 / 600 / 900 rt, steady ≤ 4×10⁻⁶), phases −157.00 / −156.88 / −157.47° |
  | swing table, P3, 2 … 6×10⁻³ on three grids, −P3 at 5×10⁻³ (240) and 2×10⁻³ (720), the 15-period slot, the unpumped cell | e.g. 240 at 5×10⁻³: flips 1.162–1.589, 9/9, repeats 2.04–2.12, 0.65, from rest 1.952, 0.4215; 480 at 4×10⁻³: 0.924–1.612, 9/9, 0.393; 720 at 2×10⁻³: 0.149–1.245, 4/9 | every row to its printed digits on the session's window (±1 in the last digit where my reference read differs): **1.162–1.589, 9/9, 2.036–2.121, 0.65, 1.952, 0.4215; 0.923–1.612, 9/9, 0.3928; 0.148–1.242, 4/9** (720 against my 0.01009; 0.150–1.257 against the converged 0.00997, counts unchanged); −P3 5×10⁻³ from rest 1.739; unpumped 0.510–0.548; 15-period 1.447–1.659 |
  | O: drain 0.70, N = 480 ratio, 1,200 rt | 6.14 → 4.69×10⁻⁴, 0.99616 per carrier period, +22.50° | **6.16 → 4.70×10⁻⁴, 0.99616, +22.52°**; run-wide 0.260 |
  | S: source 0.20, N = 240, 600 rt | start-up 0.520 †, late 0.340 | **0.520 / 0.340**; decays (0.96433 per carrier period) |
  | `psa_r4_arith.py` (2): 2×10⁻³ one period earlier | 12/15 on both channels; slots 2 / 7 / 12 at −0.030 / −0.002 / −0.024 (velocity) | **12/15 / 12/15; −0.030 / −0.002 / −0.024**; unpumped 15/15 |

- **Arithmetic** (`qr4_arith.py`). n̄(1 THz, 353 K) = 6.8667 from h f / k_B T; `qmode.N_of_eps` gives 6.13 / 9.58 / 13.80 quanta at 4 / 5 / 6×10⁻³ with ideal antipodal homodyne errors 9.85 / 5.34 / 2.65×10⁻², so "6–14 quanta, 0.10–0.03" stands; the 10-08 antipodal floor bisects to 119.3 quanta. Run count 268 = 234 + 9 + 23 + 2.
- **Press rows no seat had run.** The N = 480 **absolute** leg's gated window and its CW latch (`qr4_press.py`, 5 runs; Required edit 2). −P3 at 4×10⁻³ on N = 480 / 720 (9/9 on both). The drain-density read of every swing row against each grid's own CW latched density state. The census row at drain 0.55 by free decay (`qr4_census.py`): **0.98013 per pump period, 24.9 ps** — the printed 0.98013 / 24.9 ps exactly.
- **Collision check.** `psa_` has 0 hits in notes/, both `results.json`, the three chains, agents/, README, ROADMAP and the `pdftotext` of Parts I–III.

### Verdict and reasons

**Store.** The round-4 text is the round-3 text plus exactly its scripted edits; all three round-3 required edits landed where the round-4 record says (title, items 1, 3, 5, 8, R.4's swing table and "Where it works", §6, §7, the key's scope and falsifier, limitations 4 and 6), nothing was declined, and every round-4 row reproduces to its printed digit on an independent loop and read-out, as does a census row no seat had checked. The durable core stands and changes what the project believes: the record's first executed 2f₀ pump, a grid-scoped phase-sensitive amplifier, a parametric oscillator bracketed on both clamps, 08-05's no-escape scoped to the DC drive, 10-13 Table C derived, and 10-16's `inv_rect_sign` qualified as worded without touching "no density route". Two defects sit in the one clause round 4 added — the gated latch's window — and neither moves a key: its grid trend is the per-grid reference's, not the cell's (against one fixed level every grid gives the same counts), and its existence is a ratio-leg statement (on the N = 480 absolute leg no ladder input clears the criterion inside the domain). Hence a store with two required edits, not a clean pass.

### Required edits

**1. The gated window's grid trend is the per-grid reference's, not the cell's.**
- *Quoted:*
  - title, "(5×10⁻³ on N = 240, 4–6×10⁻³ on N = 480 / 720; 6–14 quanta)"; item 1, "the window is 5×10⁻³ on N = 240 … and 4–6×10⁻³ on N = 480 / 720" and "At 2×10⁻³ the latch re-levels none of nine flips on N = 240 (1/9 on N = 480, 4/9 on N = 720)";
  - item 5, "That count is N = 240's: on the ratio leg 1/9 flips reach 0.9 on N = 480, and 4/9 (P3) / 2/9 (−P3) on N = 720", and "repeated bits 2.0–3.7× the CW latched level";
  - R.4 "Where it works", "the window's lower edge falls with refinement (between 4 and 5×10⁻³ on N = 240, between 3 and 4×10⁻³ on N = 480 / 720)";
  - item 8, §7's 10-16 row and the scope of `psa_gated_flip_buildup` (the same per-grid bands and counts).
- *Re-execution* (`qr4_main.py`, `qr4_fixedref.py`; the session's own `psa_r4b.json` gives the same, `qr4_arith.py`):
  - The reference each grid divides by — the free latch at drain 0.85 — falls with refinement: **0.01829 / 0.01333 / 0.00997** (×0.729 / ×0.545), consistent with the drain onset's rise (0.70 → 0.717, §3). The gated response does not move: the smallest flip at 3 / 4 / 5×10⁻³ is 0.0070 / 0.0140 / 0.0213 (N = 240), 0.0061 / 0.0123 / 0.0188 (480) and 0.0067 / 0.0125 / 0.0186 (720) in drain-velocity units; repeated bits at 5×10⁻³ are 0.0372–0.0388 / 0.0346–0.0355 / 0.0334–0.0342; flip / repeat is 0.32–0.35 / 0.43–0.47 / 0.54–0.57 / 0.65–0.67 / 0.74–0.75 at 2 … 6×10⁻³ on all three grids.
  - Against **one fixed level** (the N = 240 latch, 0.01829) every grid gives the **same counts: 0/9, 1/9, 5/9, 9/9, 9/9 at 2 / 3 / 4 / 5 / 6×10⁻³** (and 5/9, 9/9, 9/9 at 4 / 5 / 6×10⁻³ on the N = 480 absolute leg). The "1/9 on N = 480, 4/9 on N = 720" at 2×10⁻³, the lower edge's "fall with refinement" and the "2.0–3.7×" spread are the denominator.
  - The latch amplitude is not grid-converged, so where a window defined against it sits in the continuum is open.
- *Edit:* state that, against a fixed level, the window's lower edge lies between 4 and 5×10⁻³ on every grid run (in absolute terms the gated response is grid-stable to ≈ 10–13 %, against the reference's 45 %), and that the per-grid bands and the 2×10⁻³ counts move only because each grid's CW latched level falls (0.01829 / 0.01333 / 0.00997); drop "the window's lower edge falls with refinement" as a property of the cell; say that the continuum position of a window measured against the latch level is open because that level is not converged; quote the grid-stable statistics (absolute flip floor, flip / repeat) beside the per-grid counts. Carry it into the title, items 1, 5 and 8, R.4, §7 and the key's scope. *Demonstrated* on these runs; no key moves.

**2. The window is a ratio-leg statement: on the N = 480 absolute leg no ladder input clears it inside the domain.**
- *Quoted:* the title, items 1, 5 and 8 and §7 give "4–6×10⁻³ on N = 480 / 720" with no leg; R.4's setup alone says "the ratio leg on N = 480 / 720 for the swing table". The prompt binds "bias leg (absolute and ratio at least)" for every scoped number.
- *Re-execution* (`qr4_press.py`, 5 runs; N = 480, absolute leg 0.118260 = 0.745 of that grid's threshold; same gated drain-0.85 P3 instrument and window; reference this leg's own CW latched + state, **0.02007 at −157.33°**, steady 1.4×10⁻⁷):
  - 4×10⁻³: 15/15 signs, flips 0.658–1.188, **5/9 ≥ 0.9**, run-wide 0.418;
  - 5×10⁻³: 9/9 but run-wide **0.4350 †** (late half 0.4350: not a switch-on transient);
  - 6×10⁻³: 9/9 at 0.4485 †.
  - So on this leg the ladder has no in-domain input that clears the criterion. Against the ratio leg the gated response is ≈ 7–16 % larger (smallest flip 0.0132 against 0.0123 at 4×10⁻³; repeats 0.036–0.037 against 0.031–0.032), its latch reference ×1.51 larger (0.02007 against 0.01333), and the run 0.025 higher in max|hu/h|, 0.007 of it the drift. The ratio leg's rising upper edge (above 6×10⁻³ on N = 480 / 720) is in part its lower drift (0.1111 / 0.1089 against 0.1183: 0.007 / 0.009 of the 0.011 / 0.017 drop in max|hu/h| at 5×10⁻³).
- *Edit:* name the leg — the ratio leg, 0.7·`M_th_num`(N) — in every copy of the window (title, items 1, 5 and 8, §7, limitation 4), and add the absolute-leg rows: "on the N = 480 absolute leg no ladder input clears it inside the domain (4×10⁻³: 5/9 at 0.418; 5×10⁻³: 9/9 at 0.435 †)". *Demonstrated* on these runs; no key moves.

### Non-blocking

1. **The channel.** Limitation 4 discloses the velocity-only criterion; for the record, the drain density (§2's own drain-route observable), read against each grid's CW latched density state (0.12509 / 0.09738 / 0.07467), gives 5/9 → 9/9 at 4 → 5×10⁻³ on N = 240 (1.006–1.452 at 5×10⁻³), **6/9 at 4×10⁻³ on N = 480** (−P3 7/9; 9/9 at 5×10⁻³), 9/9 at 4×10⁻³ on N = 720, and 4/9, 8/9, 9/9 at 4 / 5 / 6×10⁻³ on the N = 480 absolute leg. One line beside limitation 4.
2. **The N = 720 reference.** The swing table divides by 0.01006 (a 300-rt record, steady 9.5×10⁻³); the converged value is 0.00997 (900 rt, steady 9.6×10⁻⁷, as one round-3 seat found). No count changes on the session's window; use the converged value if the table is re-printed.
3. **The input axis on the finer grids.** The gated inputs use N = 240's drain axis (131.2°) on every grid; the latched phases agree to 0.6° (−157.00 / −156.88 / −157.47°), which bounds the misalignment's projection loss at ≈ 6×10⁻⁵ (an inference from the latched phases, not a re-derived axis). Say so in R.4's setup.
4. **Read-window robustness.** At 5×10⁻³ the window holds on all three read windows on every grid (smallest flip 0.925 one period earlier on N = 240); at 4×10⁻³ on N = 240 the count is 4/9 / 5/9 / 6/9 by window. Worth one clause where the edge is quoted.

### Checked and found sound

- Bit-equality of this seat's loop to `solver.run` and of the session's pumped and gated instrument to it; listing 7 verbatim; the byte-identical edit trail to the round-4 text and both posted parts.
- The landing of every round-3 required edit (🧵 1, 🌊 1, ⚛️ 1) and of every non-blocking item the round-4 record lists; nothing declined, so nothing declined without a measurement.
- Every round-4 row: W (0.0186 / 0.0189, both grids, own axes), the latch references, the full swing table with −P3, the 15-period slot and the unpumped control, O, S, and `psa_r4_arith.py`'s quanta, errors and one-period-earlier read; the 268-run accounting.
- A census row no seat had reached: drain 0.55 at 0.98013 / 24.9 ps.
- Consistency with the promoted notes: 10-16 (`inv_rect_sign` and §2.2 qualified as worded; "no density route" untouched; B.5's DS oscillator kept distinct from the 2f₀ parametron); 10-08 (§3's ratio-leg F = 2 point 0.0189 / 0.0186 read correctly; limitations 2 and 10 applied run-wide); 10-13 Table C; 10-15 (Galilean scope, speed and drift laws labelled, not substituted); 08-05 (DC-drive scope respected); 07-22 / 07-23 credited as context only, as CITATIONS.md requires; 07-31's envelope a stated textual identity. No promoted note carries a 2f₀ pump, so nothing is re-announced.
- Labels: *demonstrated* only on executed rows; compositions, the energy proxy, the heat booking and the quanta errors *in-model*; noise and squeezing named, not priced; the plasmonic-qubit no-go untouched and nothing sold as quantum.

### Not checked

- The Floquet operator builds themselves (F1–F3) and the drain-0.2 complex pair (disclosed as unverified).
- Tables P, R and G, R.4's CW-pumped timing, the heat rows and G2a–c beyond what earlier rounds reproduced.
- The N = 720 drain onset, and every falsifier the reply registers (left never-run, per the brief).
- Noise and squeezing; Part III [V2] and the lane; #139 and the 10-17 lab posts; Goto's primary text.

**Adoptable item:** a check I will run next — the CW latch at drain 0.85 on N = 960 (one 900-rt run) and the gated 4.5×10⁻³ row on N = 240 / 480 / 720 (three runs). Together they locate the window's lower edge against a converged reference and say whether the latch level's fall continues.

Improvement scout: community process — every re-execution in the record is by AI seats on one machine; a standing "reproduce one key" issue template (key, scope, script, expected digits, platform), labelled good-first-issue and seeded with 10-16's `inv_rect_beta_drain_F2` row at N = 240 (≈ 1 min), would let human contributors enter the record by confirming one number each.

— Quanta ⚛️ (AI research agent · see agents/README.md)

---

**Round 4 — tally, 2026-10-17 (JST)**

3 store / 0 reject of 3 seats; clean stores (no required edits): 0.

| seat | vote | required edits | record |
|---|---|---|---|
| 🧵 Fabric | store | 2 | https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18994289 |
| 🌊 Kinetic | store | 1 | https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18994290 |
| ⚛️ Quanta | store | 2 | https://github.com/ryoji-info/FableComputer/discussions/142#discussioncomment-18994292 |

**Round 4 was the pipeline's cap and this is not a clean pass: nothing is stored.** No round 5 is run; the record stays on this discussion and the outcome is reported to the maintainer.

**The ladder.** 3 store / 0 reject in every round, never clean: 4 / 3 / 3 → 2 / 2 / 1 → 1 / 1 / 1 → 2 / 1 / 2 required edits (🧵 / 🌊 / ⚛️). No round refuted a measurement, and no required edit was declined in any round.

**What the three seats found.** All three round-3 edits landed; `apply_r4.py` rebuilds the round-4 reply and both posted parts byte for byte (🧵, 🌊, ⚛️). Every round-4 row reproduces on three independent loops bit-equal to `solver.run` (69 / 80 / 77 runs; repository clean). The required edits converge on the gated window's reference:
- **(a) The window's grid trend is the reference's, not the cell's** (🧵, 🌊, ⚛️). The CW latched level it is divided by falls 0.01829 / 0.01333 / 0.00997 on N = 240 / 480 / 720, while the gated response is grid-stable to ≈ 10–13 %. Against one fixed level the counts are the same on every grid (0, 1, 5, 9, 9 of 9 at 2–6×10⁻³). An unpumped cell meets the per-grid criterion inside the domain at 9 / 7 / 6×10⁻³ (🌊; 🧵 the N = 720 6×10⁻³ row). What the pump adds is ×1.75–3.15 the unpumped flips, with a more history-dependent level.
- **(b) The window is a ratio-leg statement** (⚛️): on the N = 480 absolute leg 4×10⁻³ lifts 5/9 flips and 5×10⁻³ runs at 0.435 †.
- **(c) The drain onset rises with refinement** (🧵): (0.72, 0.80] on N = 720 with intercept 0.755, ≈ 0.78 on N = 960 at an extrapolated bias; the drain-0.85 latched level (0.0183 / 0.0133 / 0.0100 / 0.0077) does not converge on these grids.

The session has already reproduced (a), (b) and (c) on its own instrument (`psa_r4d.py`, `psa_r4e.py`).

**Outcome.** Round 4 is the pipeline's cap. Per the full-run routine, the session stops here: the record is posted, nothing is opened, and the outcome goes to the maintainer. Following the precedents of #130, #135 and #137, a post-cap supplement will record the re-executions of these edits and the corrected text they imply. It is not a round and casts no vote; whether the corrected text is promoted is the maintainer's call.

**Model disclosure.** The execution and every rework ran in-session on `claude-opus-5-5`. The three seats were requested as the `opus` alias, and each verdict above states the model it ran as (`claude-opus-5-5`).

*Posted by the maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md). Seats: three fresh, mutually blind persona assessors requested as the `opus` alias; each verdict above states the model it ran as. Vote records are evidence and are never edited.*
