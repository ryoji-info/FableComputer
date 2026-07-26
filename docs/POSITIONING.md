<img src="../branding/boogie-sorbet-monogram.svg" alt="" width="72" align="right">

# Where this fabric wins, and where it does not

A short, honest positioning note for a reader deciding whether the Fable Computer is
relevant to their problem. Everything here is **in-model** — the design rests on a gain
cell no one has built (bench gate G1), and nothing below should be read as measured
hardware. The numbers are quoted at the [reference operating point](../README.md#the-reference-operating-point).

## The one-sentence version

A clocked, regenerative graphene-plasmon fabric is interesting **because every gate is
the same physical object and restores its own logic levels** — and it is *not*
interesting as a general-purpose processor, a memory technology, or a qubit host.

## Where it plausibly wins

- **Wave-rate logic at the edge of the electronic clock ceiling.** Restoration happens
  in the device physics rather than in a separate latch, so depth costs latency but not
  signal integrity. In-model, fan-out-2 logic closes at **≈0.1 THz** once per-slot
  flushing against cavity ring-down is required — a decade above CMOS clock rates and
  a decade below the 1-THz carrier ([07-23](../notes/2026-07-23-reset-switch-adjudication.md)).
- **One-cell gate libraries.** Inversion is a bias choice, not a different device. A
  fabrication process that yields one good cell yields the whole logic family — which is
  why disorder-limited yield, not gate design, is the fabric's first-order risk.
- **Analog interference, decoded on-chip.** Below the compression knee the same fabric
  is a linear interferometer: it multiplies by transmission amplitudes and sums by
  superposition, then digitizes with its own threshold cells. For 1–2-bit tensor
  products at low precision that is a genuinely short datapath.
- **Energy per operation, on the fabric side.** ~0.4 fJ per addition excludes the clock
  chain and read-out — a fabric-side figure, useful for comparing fabrics, not systems.

## Where it does not win, and will not

- **Qubits.** Excluded, not merely hard: the single-plasmon Kerr nonlinearity falls
  short of the loss rate by roughly five orders of magnitude, and the blockade would
  demand ~3-nm cells. This is the project's own no-go and it is not expected to move.
- **Memory.** There is no native plasmonic storage at ~1-ps lifetimes. The persistent
  bit lives as gate charge — DRAM-like, slow, refresh-limited. Anything memory-bound is
  a poor fit by construction.
- **Deep combinational logic.** Regeneration buys cascadability, but the composed
  envelope caps practical fan-out at **F = 2** with a disorder ceiling of F ≤ 2.56, and
  sharpness erodes as k_eff = 8·F^(−1/2) ([07-21](../notes/2026-07-21-composed-regeneration-envelope.md)).
  Wide fan-out spends buffer tiles, not headroom.
- **High-precision analog.** Shot noise affords 1–2 bits per shot. Per-shot 2-bit
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
| the contact conductance σ_c lands at the diffuse end | the boundary channel costs ≈−3 dB (Kn²) to ≲−10 dB (Kn) and the margin story changes qualitatively ([07-18](../notes/2026-07-18-boundary-channel-contact-gated.md)) |
| stretched-slot launch bursts prove energetically cheap | the ≈0.1 THz operating point becomes comfortable rather than marginal (the cost is currently **open** — [07-25](../notes/2026-07-25-e1-burst-scaling-proviso.md)) |
| the comparator trim coefficient *c* measures small | the decoder's static term shrinks and cold-class precision improves; *c* is an open bench quantity, not a derived one |

## How to read the rest of the repository

Start with the [Introduction](Fable-Computer-Introduction.pdf) (six pages), then
[Part I](../papers/Fable-Computer-Part-I.pdf) for the machine and
[Part II](../papers/Fable-Computer-Part-II.pdf) for the quantum extension. The
**corrected state of knowledge lives in [`notes/`](../notes/)** — start at
[`notes/INDEX.md`](../notes/INDEX.md), which maps every note to what it settled and
what later notes did to it. Where a note and a manuscript disagree, the note wins, and
[`papers/ERRATA.md`](../papers/ERRATA.md) lists the gaps that the deposited PDFs still
carry.
