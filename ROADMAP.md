<img src="branding/boogie-sorbet-monogram.svg" alt="" width="72" align="right">

# Roadmap

Organized around the science, not calendar quarters. Each work package is
scoped so that a person or small group could adopt it. Status values:
`open` · `active` · `done`.

## Work packages

### WP1 — Harden the reduced-order chains (`open`, good first work)

The transparent model chains are the project's foundation; make them harder
to break.

- Grid-refinement study of the shallow-water solver: the numerically diffused
  threshold M_th,num → the **exact inviscid** threshold ≈0.149313 as Δx → 0
  (+1.52 % above the small-M analytic 0.147083), *not* the analytic value; the
  kinetic threshold within 07-13's closure is 0.165 [0.154, 0.169]
  (`fable-model-chain/solver.py`; see
  [notes/2026-07-22-mth-numerical-vs-physical-viscosity.md](notes/2026-07-22-mth-numerical-vs-physical-viscosity.md)).
  In-model, the single-rate kinetic operator finds no threshold below the Landau
  ceiling at 353 K for A ≤ 1 when the electrons shed their drift heat, and whether
  graphene's own electron fluid has one is open
  ([notes/2026-10-15-graphene-fluid-threshold-turns-on-current-channel.md](notes/2026-10-15-graphene-fluid-threshold-turns-on-current-channel.md)).
  The ladder has since been run at eight seeds on N = 240/480/720 (fitted order
  1.04–1.06, intercepts within 0.13 % of the inviscid value; an ill-conditioned
  three-rung fit) and on five rungs to N = 960 (order 1.036–1.070; only the
  exponent survives) —
  [notes/2026-08-06-mth-num-record-length-and-fit-convention.md](notes/2026-08-06-mth-num-record-length-and-fit-convention.md),
  [notes/2026-08-07-mth-num-excess-decomposition.md](notes/2026-08-07-mth-num-excess-decomposition.md).
  Still to do: a fourth rung below N ≈ 860 at a third refinement ratio and the
  pre-registered N = 1440 iso-ν census; pin `measure_Mth_num`'s round trips,
  seed, cfl and fit convention and emit its eight-seed spread; and, as the CI
  check, the operator collapse law (|Δ| ≤ 5×10⁻⁵, against the 240-round-trip
  eight-seed census) in place of the first-order assertion 07-22 §5 requested.
- `measure_Mth_num` on finer grids: threaded to N, its scan floor
  (1.05·M_th_353K) sits above the inviscid limit, so the scan returns nan at
  N = 960 at all eight seeds (demonstrated; the released run never trips it,
  inheriting N = 240). Proposed fix: explicit N, x_lo and seed arguments that
  keep today's result bit-for-bit, an adaptive floor, a guard covering both
  ends of the bracket on both the N and cfl axes that raises instead of
  returning nan, and seed-pinned N = 240/480 tests
  ([notes/2026-08-02-where-the-released-threshold-bracket-stops-working-a-scanned.md](notes/2026-08-02-where-the-released-threshold-bracket-stops-working-a-scanned.md) §3;
  08-06 §9).
- The hard-coded 0.118 bias literal in `run_all.py` and `thermal.py` does not
  track M_th,num; fixing it is a versioned edit to the released chain
  ([notes/2026-08-07-mth-num-excess-decomposition.md](notes/2026-08-07-mth-num-excess-decomposition.md) §9).
- Absolute calibration of the per-pulse gain against the CW regenerative
  transfer (`regen.py` vs `solver.py`).
- Tighten the disorder-yield criterion's free parameters and document their
  sensitivity (`disorder.py`).
- Junction-loss sensitivity: elevate the −1 dB vs −3 dB junction band from a
  results.json side-entry to a first-class reported band (both parts).
- The record-audit artifacts `ledger_listing.py` (numeric claims) and
  `ledger_sweep.py` (defect-signature sweep, must report `UNDISPOSED HITS: 0`)
  run in CI on every PR, together with `tests/` pinning the published
  `results.json` keys — the standing WP1 deliverable, now delivered for the
  audit surface and extendable to the rest.
- Independent ports (Julia, Rust, JAX) as living cross-checks; CI that runs
  every self-check on every PR.

### WP2 — The Boltzmann–Maxwell tier (`open`, the big one)

Part I, Section 10: a full kinetic + electromagnetic solve that owns
electromagnetic coupling and absolute calibration — replacing the reduced-order
chain's calibration assumptions with computed values, and certifying (or
correcting) the regenerative gain figures.

- First deliverable is a **scoping note**: equations, solver strategy,
  resolution requirements, and an honest compute budget (core-hours), so the
  work package can be costed and free research-compute programs approached.
  Workstation-feasible resolution first if the budget demands it.

### WP3 — Pulsed clock synthesis (`open`)

The fabric's clock is a phase-stable THz pulse train; the demonstrated
precedent is a continuous-wave microcomb-photomixing chain (Part I, §3.2).
Design the pulsed extension: architecture, component list, phase budget, and
what a tabletop validation would cost.

Since this package was written the record fixes, in-model, what the clock must
deliver: a duty-0.8, data-gated burst with raised-cosine edges of two round trips
at the 69 GHz gated point, costing ×3.4–4.9 the energy per '1' of the released
burst on the launch/clock subsystem
([notes/2026-07-31-physical-launch-gated-frontier.md](notes/2026-07-31-physical-launch-gated-frontier.md));
a phase budget each cell spends at 12–21° per 1 % of detuning
([notes/2026-10-13-phase-is-not-the-easier-half-for-the-cell.md](notes/2026-10-13-phase-is-not-the-easier-half-for-the-cell.md));
if the inverters are interferometric (amplitude encoding), each clock pulse within
10.1–12.3° of its input, by grid and tightening under refinement
([notes/2026-10-16-no-density-route-to-a-not-in-the-released-cell.md](notes/2026-10-16-no-density-route-to-a-not-in-the-released-cell.md));
and, for phase encoding, two coherent lines — a 2f₀ pump phase-locked to the f₀
reference — and a carrier referenced to absolute time
([notes/2026-10-17-a-pumped-cell-restores-phase-in-a-narrow-window.md](notes/2026-10-17-a-pumped-cell-restores-phase-in-a-narrow-window.md)).
Which source supplies it (RTD, photomixer, silicon harmonic source or the cell
itself) is an open design question:
[issue #139](https://github.com/ryoji-info/FableComputer/issues/139).

### WP4 — The bench experiment (`open`, needs lab partners)

Part I, Section 10 specifies a five-gate pre-registered pass/fail protocol
(G1–G5); Part II adds its quantum gates (QG1–QG5); Part III (draft) adds
DG1–DG5 and TG1–TG5, with G1, L0 and QG1–QG3 as prerequisites (its Table T10).
A promoted note proposes re-issuing G1 as G1a (existence) and G1b (a knee
report) with every convention pinned; adoption is the maintainer's, and Part I's
repository copy keeps one pre-registered G1 row and records the re-issue as a
proposal ([notes/2026-08-01-bench-gate-g1-reissued.md](notes/2026-08-01-bench-gate-g1-reissued.md)).
Under those pins the promoted notes register bench discriminants — shapes a
measurement must match, not pass/fail gates: DG1-S (10-08), PHX-1…3 (10-13),
D1–D4 (10-15), D-INV-1/2 (10-16) and D-PSA-1/2 (10-17). G1's calibration
presupposes a measurable DS threshold, whose existence at 353 K is open
(10-15). No pass threshold moves. The single most
informative outcome in the program, pass **or** fail, is the first cascade of
two room-temperature plasmonic gain cells.

- Cost out the protocol: equipment list, sample requirements, beam time.
- Structured outreach to experimental graphene/THz groups — the pitch is a
  fully specified, falsifiable, pre-registered experiment; the call for an
  experimental partner is open as
  [issue #97](https://github.com/ryoji-info/FableComputer/issues/97).
- Per the [Charter](CHARTER.md) §5: experiments run inside host labs' own
  safety regimes under written agreement.
- The "measurement wanted" issue distilling the three sub-threshold
  linewidth signatures of
  [notes/2026-07-18-boundary-channel-bench-discriminants.md](notes/2026-07-18-boundary-channel-bench-discriminants.md)
  — near-model linewidth ≈27.6 GHz, a temperature sweep for the Knudsen
  exponent *p*, and a drift sweep for the drain sign — into a one-page
  protocol is **open as [issue #88](https://github.com/ryoji-info/FableComputer/issues/88)**
  (2026-08-01). Part I §10 already assigns those tests to WP1/WP4; the
  remaining work on this bullet is finding the lab.

### WP6 — Part III scoping (`active` — first manuscript drafted, October 2026; v1.1, not yet deposited)

Part III is the architecture chapter. A first manuscript — *A Ternary Language Model on
the Regenerative Graphene-Plasmon Fabric* (papers/, with `fable-model-ternary/`) — embeds
Ternary Bonsai 2 27B as a streaming matrix-multiply coprocessor and ends at one loaded-margin
measurement (gate DG1). The record already fixes several of its inputs, and this work
package remains scoping — it adds no new physics, though the October notes grade its
inputs (below):

- **The operating point is a gated slot.** F = 2 logic does not close at a
  4-ps slot at any de-Q rate, and the ≈0.1 THz headline across three closing
  configurations (E1 no flush, 79–92 GHz; E2 passive guard, 98–128 GHz; E3
  active de-Q, 100–148 GHz, worth ≈+10 % over E2 and 0 % at its 81 GHz
  demonstrated-calibrated corner) holds only under the pulse-knee convention —
  [notes/2026-07-23-reset-switch-adjudication.md](notes/2026-07-23-reset-switch-adjudication.md).
  With a physical launch confined to its slot and gated by the data (duty 0.8,
  raised-cosine edges of two round trips), the F = 2 frontier is 69 GHz (band
  63–74 GHz), an in-model composition over demonstrated rungs at 67–71 GHz and
  the slot Part III uses; 91 GHz survives only as an F = 1 wire, and E2 and E3
  have not been re-run under a physical launch —
  [notes/2026-07-31-physical-launch-gated-frontier.md](notes/2026-07-31-physical-launch-gated-frontier.md).
  At the bench's ratio bias the frontier is neither confirmed nor moved: the
  '0'-slot floor binds there, and its specification must be imported —
  [notes/2026-08-01-ratio-bias-gain-table.md](notes/2026-08-01-ratio-bias-gain-table.md),
  [notes/2026-08-02-zero-floor-spec-dissolved.md](notes/2026-08-02-zero-floor-spec-dissolved.md).
- **The gain leg is set by drive duration, not slot length.** The released
  3-cycle burst falls 0.9–3.0 dB short of F = 2 at every slot —
  [notes/2026-07-25-e1-burst-scaling-proviso.md](notes/2026-07-25-e1-burst-scaling-proviso.md);
  for physical drives its ncyc ≈ 12 point (≈71–91 GHz) is superseded by the
  gated launch above, which costs ×3.4–4.9 the energy per '1' and ×1.25–1.30
  the time-averaged launch power of the released burst (demonstrated waveform
  integrals) on the launch/clock subsystem; the absolute launch energy is open,
  because the launch-coupling efficiency is unquantified.
- **Prerequisite:** `solver.run` must forward `ncyc` to `_pulse_train`, and gain
  a duty gate, before E1 or the gated launch is expressible in the released
  chain at all (WP1; 07-31 §7).
- **Sequencing gate:** the boundary channel is contact-gated on σ_c, so Part III's
  margins are conditional on one sub-threshold linewidth measurement, which Part
  III carries as its prerequisite gate L0 after G1 (the protocol is
  [issue #88](https://github.com/ryoji-info/FableComputer/issues/88); WP4 above) —
  [notes/2026-07-18-boundary-channel-contact-gated.md](notes/2026-07-18-boundary-channel-contact-gated.md).
- **The October notes, folded into Part III v1.1 (in-model unless a note labels a row demonstrated: the 10-13 burst delay and the 10-16 interference window are demonstrated on the released solver).** DG1's
  bookings assume a rail-scale '1' that the record's deciding inputs never
  receive (they carry 1.5–277 quanta), no booking passes warm at a delivered
  swing, and DG1 must report the input-referred swing, DG1-S
  ([notes/2026-10-08-no-rail-scale-one-at-deciding-inputs.md](notes/2026-10-08-no-rail-scale-one-at-deciding-inputs.md)).
  A 12-ps burst is delayed 2.7–4.0 ps per cell by its energy centroid (2.0–7.3 ps
  across envelope estimators), so the 92-cell path holds 13–37 slots in flight
  at 69 GHz, not 2.1
  ([notes/2026-10-13-phase-is-not-the-easier-half-for-the-cell.md](notes/2026-10-13-phase-is-not-the-easier-half-for-the-cell.md)).
  The lane's 783 inverters have no released mechanism: in the amplitude encoding
  the options are interference within 10.1–12.3° by grid, an external gain stage,
  or a dual-rail lane that has not been counted
  ([notes/2026-10-16-no-density-route-to-a-not-in-the-released-cell.md](notes/2026-10-16-no-density-route-to-a-not-in-the-released-cell.md)).
  Under phase encoding a 2f₀-pumped cell restores phase only in narrow windows
  and, gated in the slot, re-levels no bit
  ([notes/2026-10-17-a-pumped-cell-restores-phase-in-a-narrow-window.md](notes/2026-10-17-a-pumped-cell-restores-phase-in-a-narrow-window.md)).
  G1's calibration by approach to self-oscillation is unavailable at 353 K in
  the single-rate kinetic operator
  ([notes/2026-10-15-graphene-fluid-threshold-turns-on-current-channel.md](notes/2026-10-15-graphene-fluid-threshold-turns-on-current-channel.md)).
  The module's clock source, material gap and CMOS boundary are open design
  questions, issues [#139](https://github.com/ryoji-info/FableComputer/issues/139),
  [#140](https://github.com/ryoji-info/FableComputer/issues/140) and
  [#141](https://github.com/ryoji-info/FableComputer/issues/141).
- **Open design choice, not a claim:** an F = 1 transport and retiming layer
  over a gated 67–71 GHz logic layer — 4-ps slots (07-23's E4 ping-pong
  transport, itself open) for a clock ratio of up to ≈3.7×, or a gated 91-GHz
  F = 1 wire for ≈1.3× (07-31 §0 item 6) — a two-clock architecture the
  record explicitly leaves to the crew.

### WP5 — Part II extensions (`open`)

Launch-coupling efficiency and absolute noise calibration (owned jointly with
WP2); the 16-slot averaging mode's architecture cost; junction-quality
sensitivity at the cold operating points.

## Community milestones (measured by events, not dates)

1. Repository public, licensed, reproducible by strangers — with a DOI per
   release.
2. First external merged PR; first independent reproduction logged in
   [REPLICATIONS.md](REPLICATIONS.md) by someone unknown to the project.
3. First engagement by an external physicist on the substance (issue,
   critique, or endorsement) — and one **formal academic collaboration or
   affiliation**, which unlocks preprint endorsement, grant eligibility, and
   lab access in one move.
4. Preprint posted (arXiv cond-mat/app-ph once endorsement is secured; the
   Zenodo DOIs already protect priority), and the manuscripts submitted to a
   peer-reviewed venue.
5. Second maintainer on board; fiscal-host application (requires an
   organization-owned repo and two admins).
6. First funded work: compute for WP2 and bounties on WP1, decided by the
   process in [GOVERNANCE.md](GOVERNANCE.md).
7. A lab formally committed to a bench gate from WP4.

## Not on this roadmap

Tokens, blockchains, or paid membership of any kind (see
[Charter](CHARTER.md) §3) — and any claim of demonstrated hardware until a
bench gate passes.
