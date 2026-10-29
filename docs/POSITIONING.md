<img src="../branding/boogie-sorbet-monogram.svg" alt="" width="72" align="right">

# Where this fabric wins, and where it does not

A short, honest positioning note for a reader deciding whether the Fable Computer is
relevant to their problem. Everything here is **in-model** — the design rests on a gain
cell no one has built (bench gate G1), and nothing below should be read as measured
hardware. The numbers are quoted at the [reference operating point](../README.md#the-reference-operating-point).

## The one-sentence version

A clocked, regenerative graphene-plasmon fabric is interesting **because every gate is
the same physical object and is designed to restore its own logic levels** — and it is *not*
interesting as a general-purpose processor, a memory technology, or a qubit host.

## Where it plausibly wins

- **Wave-rate logic at the edge of the electronic clock ceiling.** By design, restoration
  happens in the device physics rather than in a separate latch, so depth costs latency
  but not signal integrity — though in-model each cell delays a 12-ps gated burst by
  2.7–4.0 ps (energy centroid) and moves its carrier phase 12–21° per 1 % of detuning
  ([10-13](../notes/2026-10-13-phase-is-not-the-easier-half-for-the-cell.md)). In-model,
  fan-out-2 logic does not close at the 4-ps slot once per-slot flushing against cavity
  ring-down is required ([07-23](../notes/2026-07-23-reset-switch-adjudication.md)); with
  a physical, slot-confined, data-gated launch its frontier is **69 GHz (band 63–74 GHz)**
  ([07-31](../notes/2026-07-31-physical-launch-gated-frontier.md)), with the '0'-slot floor
  specification and bias convention behind it still open
  ([08-01](../notes/2026-08-01-ratio-bias-gain-table.md),
  [08-02](../notes/2026-08-02-zero-floor-spec-dissolved.md)) — more than a decade above
  CMOS clock rates and more than a decade below the 1-THz carrier.
- **One-cell gate libraries — as designed, not yet as computed.** In Part I's design,
  inversion is a bias choice, not a different device, so a fabrication process that
  yields one good cell yields the whole logic family. In-model the released cell does not
  bear this out: it compresses rather than thresholds (two summed '1's read only
  2.6–3.3 dB above one); its rectification has the accumulating sign, so a plasmonic
  input cannot invert it (an external bias swing can, behind an electrical gain stage of
  ×8–73 or Part I's optical tap); and in the amplitude encoding the cell's own NOT is
  destructive interference with the clock pulse, held within 10.1–12.3° by grid and at
  best marginally restoring, while under phase encoding NOT is a half-period delay
  ([10-16](../notes/2026-10-16-no-density-route-to-a-not-in-the-released-cell.md),
  [10-17](../notes/2026-10-17-a-pumped-cell-restores-phase-in-a-narrow-window.md)).
  Disorder-limited yield is still a first-order risk, but its rule assumes a
  swing-induced shift β·A_swing = n where the released cell gives ≈0.02·n, so gate
  physics is open as well.
- **Analog interference, decoded on-chip.** Below the compression knee the same fabric
  is a linear interferometer: it multiplies by transmission amplitudes and sums by
  superposition, then digitizes with its own threshold cells (threshold cells by design;
  in-model the released cell compresses rather than thresholds, so how the decoder's
  cells are to be built is open — Part II, Section 5). For 1–2-bit tensor products at
  low precision that is a genuinely short datapath.
- **Energy per operation, on the fabric side.** ~0.4 fJ per addition excludes the clock
  chain and read-out — a fabric-side figure, useful for comparing fabrics, not systems.
  The physical gated launch costs ×3.4–4.9 the energy per '1' and ×1.25–1.30 the
  time-averaged launch power of the released burst, on the subsystem this figure
  excludes; the wall-plug launch energy is open
  ([07-31](../notes/2026-07-31-physical-launch-gated-frontier.md)).

## Where it does not win, and will not

- **Qubits.** Excluded, not merely hard: the single-plasmon Kerr nonlinearity falls
  short of the loss rate by roughly five orders of magnitude, and the blockade would
  demand ~3-nm cells. This is the project's own no-go and it is not expected to move.
- **Memory.** There is no native plasmonic storage at ~1-ps lifetimes. The persistent
  bit lives as gate charge — DRAM-like, slow, refresh-limited. Anything memory-bound is
  a poor fit by construction. (In-model a 2f₀-pumped cell is, above an onset that rises with
  grid refinement, a latching parametric oscillator that holds and re-levels a bit under a
  CW pump; gated in the slot it re-levels none —
  [10-17](../notes/2026-10-17-a-pumped-cell-restores-phase-in-a-narrow-window.md).)
- **Deep combinational logic.** Regeneration buys cascadability, but the composed gain
  envelope caps practical fan-out at **F = 2** ([07-21](../notes/2026-07-21-composed-regeneration-envelope.md));
  the disorder ceiling F ≤ 2.56 and the erosion k_eff = 8·F^(−1/2) assume a sharpness
  k₀ = 8 that the released cell does not deliver (0.18–0.26 on Eq. (5)'s tanh scale for
  a density coupling; in-model, [10-16](../notes/2026-10-16-no-density-route-to-a-not-in-the-released-cell.md)).
  Wide fan-out spends buffer tiles, not headroom.
- **High-precision analog.** At the design pulse energy, shot noise affords 1–2 bits per shot. Per-shot 2-bit
  decoding is a cold-class mode; averaging 16 slots is *ideal-sampler bookkeeping* and
  reaches 10⁻⁶ only below ≈45 K, so it is not a room-temperature buy
  ([07-16](../notes/2026-07-16-no-physical-avg16-accumulator.md)).
- **Cryogenic-free quantum advantage.** Below ≈20 K the error curves stop improving:
  that floor is the standard quantum limit, and observing it is a pre-registered gate
  rather than a problem to engineer away.

## What would change the picture

| if this turns out… | then |
|---|---|
| G1 fails — no room-temperature cascade of two gain cells | the program's central premise is falsified, and that is the point of pre-registering it |
| graphene's own electron fluid has no DS threshold at 353 K (open; in-model the single-rate kinetic operator finds none for A ≤ 1 with the drift heat shed — [10-15](../notes/2026-10-15-graphene-fluid-threshold-turns-on-current-channel.md)) | there is no sub-threshold operating point to bias, and G1's calibration by approach to self-oscillation and its 0.7 × threshold pin are unavailable |
| the contact conductance σ_c lands at the diffuse end | the boundary channel costs ≈−3 dB (Kn²) to ≲−10 dB (Kn) and the margin story changes qualitatively ([07-18](../notes/2026-07-18-boundary-channel-contact-gated.md)) |
| an imported '0'-slot floor specification passes at the bench's ratio bias (the released chain cannot fix it — [08-02](../notes/2026-08-02-zero-floor-spec-dissolved.md)) | the 69 GHz (band 63–74 GHz) frontier is confirmed rather than open; at that bias today, under the round spec, 67 GHz (the robust rung) clears it by 0.88 dB and 71 GHz is a 0.31-dB fail at its fitted convergence order (in-model; [08-01](../notes/2026-08-01-ratio-bias-gain-table.md), [08-02](../notes/2026-08-02-zero-floor-spec-dissolved.md)) |
| the comparator trim coefficient *c* measures small | the decoder's static term shrinks and cold-class precision improves; *c* is an open bench quantity, not a derived one |

## How to read the rest of the repository

Start with the [Introduction](Fable-Computer-Introduction.pdf) (six pages), then
[Part I](../papers/Fable-Computer-Part-I.pdf) for the machine,
[Part II](../papers/Fable-Computer-Part-II.pdf) for the quantum extension and
[Part III](../papers/Fable-Computer-Part-III.pdf) (draft, not yet deposited) for the
ternary-model embedding. The
**corrected state of knowledge lives in [`notes/`](../notes/)** — start at
[`notes/INDEX.md`](../notes/INDEX.md), which maps every note to what it settled and
what later notes did to it. Where a note and a manuscript disagree, the note wins;
[`papers/ERRATA.md`](../papers/ERRATA.md) reports whether any adopted correction is not
yet in the current Zenodo deposit, and
[`papers/REVISION-HISTORY.md`](../papers/REVISION-HISTORY.md) records every revision and
its DOI.
