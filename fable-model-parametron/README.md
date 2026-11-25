# Fable Computer, Part IV: the parametron model

Runnable companion to *The Fable Computer, Part IV: A Parametron of Pumped Resonant-Tunnelling-Diode Pairs*.
It is the time-domain circuit model of the paper: logic made of pairs of resonant-tunnelling diodes (RTDs) on
metal inductors. Each pair is biased just below its own oscillation threshold and pumped at twice its carrier,
so that it oscillates on one of two phases half a turn apart: a parametron. Pairs are linked through their
inductors and clocked in four phases. The package runs rows, ripple-carry adders, a serial adder with a
stored carry and an accumulator, and reads them by the rules of the paper.

Pure Python. It needs only `numpy`. The `torch` backend (`backend=torch`) is an option and is imported
only when asked for.

## Quick start

```bash
python r1_pair.py           # one pair: own oscillation range, the pump makes two phases, table P-1 (~2 min)
python r1_pair.py cell=c160 # the same for a pair tuned to a 160-GHz carrier with a 320-GHz pump (~2 min; output in r1_pair_c160.out)
python r2_row.py            # a row of sixteen at the operating point, without and with noise and spread (~2 min)
python r3_adder.py          # the four-bit ripple-carry adder of 53 pairs (~5 min)
python r4_serial_adder.py   # the serial adder on two rails, with and without link capacitors (~4 min)
python r5_units.py          # the change of units between the 225-GHz circuit and the 1-THz-class cell (~10 s)
python r6_spread_budget.py  # the spread budget of the four-bit adder from the stored runs, and four draws judged (~3 min)
python r7_tables.py         # the tables of results rebuilt from the stored runs, with a digest (a few seconds)
python check_identity.py    # the packaged runner against the runner as it ran, bit for bit (~3 min)
```

Each listing prints every number it computes, with a header that says what it shows. The `.out` file beside
it is the reference output on the computer the package was made on (Windows 11, Python 3.11, numpy 2.4;
the run times above are from there). The listings run from any folder, also as
`python -X utf8 -I rN_<name>.py`. Seeds are fixed, so a second run prints the same. The listings that run
batches (`r2`, `r3`, `r4`, `r6` and `check_identity.py`) and `analysis/rebuild_check.py` write their batch files into a
new folder in the system's temporary folder (named `parametron_...` or `rebuild_...`) and remove it when they end.
No listing writes inside the package.

A batch of your own runs as the batches of the paper did:

```bash
python chain4.py chain out=<folder> set=<settings>.json tag=<name> ncell=<pairs>
python analysis.py rows|seq|logic <folder> <name>
```

`cellbase.setting()` makes a setting at the operating point; `MODEL.md` lists the keys.

## Modules

| File | Role |
|------|------|
| `chain4.py` | the runner: layouts, expected bits, clock, pump and drive, batches of runs; writes `<tag>.json` and `<tag>_c<k>.npz` |
| `runs3.py` | job arguments, building a batch of pairs with their spreads, the integration loop, the reader of levels and phases |
| `fdtd3.py` | the integrator of the pairs: stubs, lumped equations, inductance matrix and links, noise |
| `rtdiv.py` | the current-voltage law of the diode |
| `cellbase.py` | frozen values of cell F, of the operating point and of the change of units, with where each came from |
| `analysis.py`, `refcheck.py` | the reading rules of the paper (right, wrong decision, row holds, wrong addition, wrong sum) |
| `batch.py` | runs `chain4.py` from a script; used by the listings |
| `r1_pair.py` to `r7_tables.py` | the listings, each with its `.out` |
| `collect_runs.py`, `runs/` | the stored runs of the paper, gzip-compressed, and `runs/MANIFEST.json` with the checksum of every file |
| `tables.py`, `tables.md` | every table of results, rebuilt from `runs/` alone |
| `analysis/` | the session's analysis scripts (`an_chain3.py`, `an_tol4.py`, `an_scan4.py`, `an_d32.py`, `an_seq4.py`, `an_logic5.py`, `refcheck.py`), `an_count.py`, and `rebuild_check.py`, which rebuilds the stored analysis files from the arrays |
| `spec/` | the specifications the independent codes were written from |
| `independent/` | the independent codes, with a `README.md` that says what each is, ran and found |
| `check_identity.py`, `identity/` | three settings and the arrays the original code wrote for them, and the script that compares |
| `MODEL.md` | the model in equations and words: circuit, units and both sets of values, clock, pump, links, integrator, noise, spreads, layouts, reading rules |

## Key numbers of the listings

All at 0.94 V, a 25 % pump and links of 6 %, without link capacitors, physical noise of the 225-GHz circuit.

| Listing | Result in the model |
|---|---|
| `r1_pair.py` | the pair oscillates by itself from 0.97 to 1.14 V; with a 25 % pump at 0.94 V it settles on two phases half a turn apart (six of twelve starts on each), at 193 mV, 29 ps after the start of a seed that lasts 28.7 ps (6 model ps); all 63 entries of table P-1 come out as stored. With `cell=c160`, the pair tuned to 160 GHz: it oscillates by itself from 0.97 to 1.14 V, and with a 10 % pump at 0.94 V it is on two phases 47 ps after the start of a seed of 40.3 ps; all 63 entries of the session's table R-9 come out as stored |
| `r2_row.py` | 16 of 16 pairs right; 230 mV per half when the next pair decides; phase step 135 degrees per link; 0 wrong decisions of 3,360 in 32 runs with a 3 % inductance spread; the row holds |
| `r3_adder.py` | 53 of 53 pairs right, lowest level 200.5 mV; 0 wrong additions of 248 in 8 runs with a 3 % spread |
| `r4_serial_adder.py` | weakest level 205.1 and 266.5 mV at 0.94 and 1.015 V without link capacitors, 198.0 and 196.9 mV with them (common reading); 0 wrong sums in 16 runs |
| `r5_units.py` | the two sets of units give the same traces to 1e-13 of the signal |
| `r6_spread_budget.py` | with all nine spreads at once the four-bit adder fails in 7 of 256 draws at the noise of the 1-THz-class cell (2.7 %, exact 95 % interval 1.1 to 5.6 %) and in 5 of 256 at the noise of the 225-GHz circuit; at seven eighths of every spread 10 of 256 (3.9 %, 1.9 to 7.1 %), more than with the full set, so the failures do not fall steadily as the spreads shrink; at three quarters 1 of 256, at five eighths and at one half none |
| `r7_tables.py` | eight tables rebuilt from the stored runs, equal to `tables.md` |

## Provenance

The model was written and run in a maintainer-operated Claude Code session in November 2026. The reported
batches ran on a graphics processor with the `torch` backend in single precision. The listings of this
package run on a processor with the `numpy` backend in double precision, and draw their noise from another
generator, so their noisy counts are checked as counts, not bit for bit. Runs without noise or spread
agree with the stored arrays of the batches to within 0.01 mV in level and 0.01 degree in phase, for every
pair and every counted slot (slot 1 and up) of the row of sixteen and of the serial adder (the first settings of
`chain_g29` and `chain_g30`). In slot 0, which no count uses, the levels of the serial adder differ by up to
0.08 mV. The mean supply power of a run (`P` in the arrays, used by no table) agrees to 1e-6 for the serial
adder but differs by 0.1 % for the row (7.1707 mW here, 7.1636 mW stored). The session's own code on the numpy
backend gives the same 7.1707 mW (`identity/id29`), so the difference lies between the two backends; its cause
was not found.

The code is the code as it ran, with the smallest edits that make it public and self-contained: docstrings
and comments rewritten to describe this design, no dependence on the older design modules or on the helpers
of the compute node, numpy as the default backend, and the job arguments of the batches as defaults.
`check_identity.py` shows that the stored arrays are bitwise unchanged on this computer.

The batches of the paper are the batches named `chain_g*`. They have no link capacitors (`cc = 0`). Older
batches named `chain_d*` carried a small capacitor across every link by an oversight; they are not part of
the paper's results, and `r4_serial_adder.py` shows what that capacitor does.

This model is not one of the released model chains of Parts I to III and does not extend them.

## Stored runs

`runs/` holds the batches of the paper, named `chain_g*`: for each, the settings, the result index and every
analysis file, gzip-compressed (`.json.gz`), and `runs/MANIFEST.json`, which gives per batch the layout, the number
of pairs, settings and runs, the command line it ran with, and the size and SHA-256 checksum of every file. The
array files (`chain_<tag>_c000.npz`, up to 55 MB each) and the large `_summary.json` files are not in the package;
the manifest lets a reader check a copy obtained elsewhere. The checksums are written in groups of eight hex digits
and the sizes with a space between thousands (see the docstring of `collect_runs.py`); remove the spaces before
comparing.

```bash
python tables.py                                   # writes tables.md from runs/ alone
python analysis/rebuild_check.py <array folder>    # rebuilds every stored analysis file from the arrays and compares
python collect_runs.py <batch folder> [<more folders>] [queue=<folder>]   # refreshes runs/ when more batches come in
```

The batches were written to two folders of the session: `gpu_out3`, which holds every batch that ran on the
graphics processor, and `conv38g`, which holds g38a and g38b (their command lines in the manifest say so). This
package was collected with `python collect_runs.py <session>/model/gpu_out3 <session>/model/conv38g`. A batch that
an earlier collection stored with results keeps its entry and its files when its folder is not given.

`tables.md` has eight tables: rows of sixteen at the operating point, single tolerances of rows, the supply range
of rows per pump level, rows at other carriers and with other diodes and contacts, adders, layouts with state, rows
of 92 pairs, and the spread budget with exact binomial intervals. Every line names its batch. Batches that were
queued but have no result in `runs/` are listed at the end, not filled in. When this package was made, 49 batches
were known: 47 with results, none queued without a result, and 2 copies of other batches under another name
(g29a, g30a). `analysis/rebuild_check.py` rebuilt all 55 analysis and summary files of the 42 batches that have
one from their arrays, every one bitwise equal (`analysis/rebuild_check.out`). The other five batches with
results (g29b, g29c, g30b, g38a, g38b) are the checks of time step, stub grid and precision; they have no analysis
file, and `MODEL.md`, section 8, gives what they show.

All `chain_g*` batches have no link capacitors, except one line of batch g52 that has them for comparison; the
tables leave it out and say so. The stored arrays are single precision from the graphics processor with the
`torch` noise generator, except those of g38a and g38b, which ran in double precision with `numpy` on a processor.

## Independent codes

`spec/` holds the four specifications that other modellers worked from: `BLIND_SPEC_D225.md` with its two addenda
for the 225-GHz circuit, and the stand-alone `BLIND_SPEC_T1.md` for the 1-THz-class cell. `independent/` holds what
they wrote. There are three codes besides this model:

- the second code, one code in four stages that share one cell model file (`independent/second_code/rebuild15`,
  `rebuild16`, `rebuild18a`, `rebuild18b`), and the same code run at the noise of the 1-THz-class cell
  (`independent/second_code_at_478`);
- the third and the fourth code, each written from `BLIND_SPEC_T1.md` alone by a modeller who saw nothing else of
  the study (`independent/third_code`, `independent/fourth_code`, each with its report).

`independent/README.md` says what each code is, what it ran and what it found, with the sources of its numbers, and
which short check was run from its place in this package. Only folder names in the code were changed. Array files
and caches are not shipped.

## Reproducibility caveat

Every number is in-model. No device, pump source, clock or contact of this kind has been built. The pump,
the clock, the inputs and the outputs are ideal sources in the model. The diode law is a fitted form scaled
to published per-device figures; the diode delay, the contact and the inductor's damping are assumptions of
the design. Counts of wrong decisions come from tens of runs and bound rates only loosely.
