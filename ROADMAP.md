# Roadmap

Organized around the science, not calendar quarters. Each work package is
scoped so that a person or small group could adopt it. Status values:
`open` · `active` · `done`.

## Work packages

### WP1 — Harden the reduced-order chains (`open`, good first work)

The transparent model chains are the project's foundation; make them harder
to break.

- Grid-refinement study of the shallow-water solver: confirm the
  numerically diffused threshold M_th,num → analytic as Δx → 0
  (`fable-model-chain/solver.py`).
- Absolute calibration of the per-pulse gain against the CW regenerative
  transfer (`regen.py` vs `solver.py`).
- Tighten the disorder-yield criterion's free parameters and document their
  sensitivity (`disorder.py`).
- Junction-loss sensitivity: elevate the −1 dB vs −3 dB junction band from a
  results.json side-entry to a first-class reported band (both parts).
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
