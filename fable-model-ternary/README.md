<img src="../branding/boogie-sorbet-monogram.svg" alt="" width="72" align="right">

# Fable Computer, Part III — the ternary-model embedding listings

Runnable companion to *The Fable Computer, Part III: A Ternary Language Model on the
Regenerative Graphene-Plasmon Fabric*. It maps the ternary inner loop of Ternary Bonsai 2
27B onto the Part-I digital fabric (a bit-exact lane), onto the Part-II quantum-analog
fabric (a cold hybrid counter tree), and prices the levers on each. Pure Python; depends
only on `numpy` and (for figures) `matplotlib`. Every script imports the released
`fable-model-chain/` and `fable-model-quantum/` **read-only** — nothing in either is
edited, no bytecode is written, and `run_all.py` is never imported or run.

## Quick start

```bash
python digital_lane_bonsai.py    # the digital lane: netlist, bit-exact emulation, timing, bookings (~21 s)
python ternary_qmac_design.py    # the analog counter tree on the Part-II fabric (~2 s)
python variants.py               # the levers: activation bits, block width, a threshold full adder, tolerance (~16 s)
python figures.py                # regenerates Figures T1-T5 into figures/
```

Each listing prints every number of its manuscript section; the `.out` file beside it is
the reference output on this platform (macOS arm64, Python 3.11.2, numpy 2.4.6; runtimes about 21 s for the digital lane, 2 s for the analog tree and 16 s for the variants). Run from
anywhere inside the repository, or set `FABLE_REPO=<repo root>`.

## Modules

| File | Role | Key outputs |
|------|------|-------------|
| `digital_lane_bonsai.py` (v2.1) | the Part-I digital lane | 32-wide int8 × ternary block sum per slot; 5,160 logic cells, 8,169–8,455 timing-closed; bit-exact on 1.70 M Bonsai-shaped block sums; κ = 2.8×10⁸; pass line 6.3×10⁻⁹ per decision; bookings A0–A3 and B with their pass temperatures 394 / 292 / 144 / 114 / 59 K; launch SNR ≥ 28–33 dB; 2 / 3 / 7 lanes at 0.5 / 1 / 3 TB/s |
| `ternary_qmac_design.py` | the Part-II analog counter tree | K-input counter tile reproducing `qmac.error_2bit` bit-for-bit at K = 2; QFA-3 error 1.3×10⁻⁵ (4 K) … 0.15 (300 K); 184 / 154 / 65 / 15 analog-eligible counters of 236 at 4 / 20 / 77 / 300 K; cell saving ≤ 32 %; 77 K lane needs a ≥ 40 %-of-Carnot cooler |
| `variants.py` | the levers (Section 8) | lane size vs activation bits and block width; a native threshold full adder (5 cells vs 15); the yardstick and ceiling at b bits; pass temperatures at 4-bit activations and under 10× / 100× error tolerance |
| `figures.py` | figures | Figures T1–T5 |

## Provenance

`digital_lane_bonsai.py` and `ternary_qmac_design.py` are the two design studies executed
in a maintainer-operated Claude Code session on 2026-10-03 (each re-checked
by an independent adversarial verification agent before its second revision; their correction histories
are summarised in the manuscript's Appendix TA). `variants.py` and `figures.py` were written
for the manuscript. The Bonsai model facts are external inputs (the public model card and
configuration); the weights used in the emulations are synthetic, Bonsai-shaped matrices with
an assumed one-third share of zero weights — the emulation checks a netlist identity, not a
physical device.

## Reproducibility caveat

Every physical number is in-model: the record's released calculus plus the extensions named
[D1]–[D8], [E1]–[E8] and [V1]–[V5] in the scripts' headers. No cell, cascade, launcher or
readout exists; the regenerative gain cell itself (Part I bench gate G1) is experimentally
unproven. The single-platform caveat of the record applies.
