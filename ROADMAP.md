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
  physical kinetic threshold is 0.165 [0.154, 0.169]
  (`fable-model-chain/solver.py`; see
  [notes/2026-07-22-mth-numerical-vs-physical-viscosity.md](notes/2026-07-22-mth-numerical-vs-physical-viscosity.md)).
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

### WP4 — The bench experiment (`open`, needs lab partners)

Part I, Section 10 specifies a five-gate pre-registered pass/fail protocol
(G1–G5); Part II adds its quantum gates (QG1–QG5). The single most
informative outcome in the program, pass **or** fail, is the first cascade of
two room-temperature plasmonic gain cells.

- Cost out the protocol: equipment list, sample requirements, beam time.
- Structured outreach to experimental graphene/THz groups — the pitch is a
  fully specified, falsifiable, pre-registered experiment.
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

### WP6 — Part III scoping (`open`)

Part III is the architecture chapter. The record already fixes several of its
inputs, and this work package is scoping only — no new physics:

- **The operating point is a stretched slot.** F = 2 logic does not close at a
  4-ps slot at any de-Q rate; the defensible in-model headline is ≈0.1 THz,
  across three closing configurations (E1 no flush, 79–92 GHz; E2 passive
  guard, 98–128 GHz; E3 active de-Q, 100–148 GHz, worth ≈+10 % over E2 and 0 %
  at its 81 GHz demonstrated-calibrated corner) —
  [notes/2026-07-23-reset-switch-adjudication.md](notes/2026-07-23-reset-switch-adjudication.md).
- **The gain leg is set by drive duration, not slot length.** The released
  3-cycle burst falls 0.9–3.0 dB short of F = 2 at every slot; closure needs
  ncyc ≈ 12 (7.851 dB, ≈71–91 GHz), and the launch-energy/duty-cycle cost is
  open —
  [notes/2026-07-25-e1-burst-scaling-proviso.md](notes/2026-07-25-e1-burst-scaling-proviso.md).
- **Prerequisite:** `solver.run` must forward `ncyc` to `_pulse_train` before
  E1 is expressible in the released chain at all (WP1).
- **Sequencing gate:** the boundary channel is contact-gated on σ_c, so the
  Part III margin chapter waits on one sub-threshold linewidth measurement
  (WP4 above) —
  [notes/2026-07-18-boundary-channel-contact-gated.md](notes/2026-07-18-boundary-channel-contact-gated.md).
- **Open design choice, not a claim:** 4-ps slots as an F = 1 transport and
  retiming layer over a ≈0.1 THz logic layer — a two-clock architecture the
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
