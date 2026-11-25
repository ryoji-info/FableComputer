# Independent codes

This folder holds the codes that other modellers wrote from the specifications in `../spec/`, so that the words
"independent code" in the paper can be checked. None of them uses the code of this package. Every number below is
in-model, and each is taken from the report named beside it. The reports of the codes themselves
(`third_code/REPORT.txt`, `fourth_code/REPORT.txt`) and the logs are shipped. The design report of the session and
its later findings note (`FINDINGS_after_outline.md`) are records of the session and are not in this package; the
figures taken from them are quoted here in full, so that they can be compared with a rerun of the codes.

There are three codes besides the model of this package, not five.

| Folder | What it is | Written from |
|---|---|---|
| `second_code/rebuild15`, `rebuild16`, `rebuild18a`, `rebuild18b` | the second code, in four stages | `BLIND_SPEC_D225.md`, then its two addenda |
| `second_code_at_478/rb478` | the second code run at the noise of the 1-THz-class cell | the same, with a noise factor of 4.78 |
| `third_code/rebuild_t1x` | the third code | `BLIND_SPEC_T1.md` alone |
| `fourth_code/rebuild_t1y` | the fourth code | `BLIND_SPEC_T1.md` alone |

## The second code is one code in four stages

The four folders of `second_code` and the two of `second_code_at_478` share one cell model file, `model.py`. The six
copies are identical (the same SHA-256 checksum, first 16 hex digits 20acd67aaafe6920). The first modeller wrote it.
The later three were told to copy it, check it against the specification and extend it. So these folders are one
second code in four stages, not four codes. The earlier report spoke of four independent rebuilds; that was wrong,
and the paper must say "one second code".

- `rebuild15` (first stage): the pair and the row of sixteen, from `BLIND_SPEC_D225.md`, with the first pump step of
  half a turn. Cell F oscillates by itself from 0.97 to 1.14 V, at 224.3 GHz and 277 mV; this package's model has
  0.97 to 1.14 V, 224.7 GHz and 283 mV. Rows agree at their lower ends within one step of 15 mV; the upper ends lie up
  to five steps higher at pumps of 15 and 20 %, because the two codes differ in what a misaligned input costs.
  Source: section 18 of the design report, first table.
- `rebuild16` (second stage): the serial adder on one rail with the first pump step, from `BLIND_SPEC_D225_ADDER.md`.
  Every pair is right, the decoded sum is the sum, and 32 runs with noise and a 3 % spread of the inductance show no
  wrong decision. Source: section 18 of the design report.
- `rebuild18a` (third stage): rows with the adopted pump step of three quarters of a turn, from
  `BLIND_SPEC_D225_STEP.md`. With the input aligned and a 25 % pump the row holds from 0.880 to 1.030 V (this model:
  0.880 to 1.015 V with the capacitors, 0.880 to 1.030 V without them). Level at pair 14 when the next pair decides
  229 mV. The axis turns by 135.0 degrees from one pair to the next. Source: section 18 of the design report.
- `rebuild18b` (fourth stage): the serial adder with the adopted step. The straight loop returns the carry inverted;
  the reversed or crossed link repairs it, as in this model. Lowest level 201 mV, smallest margin 0.88. With noise and
  a 3 % spread: 0 wrong of 19,840 decisions in 32 runs; clean from 0.895 to 1.015 V; errs at 0.880 V; clean at
  pumps of 15 and 35 %, errs at 40 %; clean with links of 3 to 9 %, fails at 12 %. Source: section 18 of the design
  report. Without noise, its weakest level is 201, 251, 261 and 264 mV at 0.940, 0.985, 1.000 and 1.015 V, and 194,
  231, 226 and 198 mV with this model's link capacitors added. Source: `FINDINGS_after_outline.md`, section 1.

### At the noise of the 1-THz-class cell

`second_code_at_478/rb478` runs the code of `rebuild18a` (in `a/`) and `rebuild18b` (in `b/`) at 4.78 times the
noise power of the 225-GHz cell, which is the 1-THz-class cell's own noise through the exact change of units. The
queue files `queue_rb*.txt` hold the command lines; `logs/` holds the printed tables of the runs. Serial adder with
a 3 % spread, 32 runs per line (`logs/rbb_st478r.log`): at 0.880 V 999 wrong decisions of 19,840, 24 runs with a
wrong sum; from 0.895 to 1.015 V no wrong decision; at a 40 % pump 28 wrong decisions in 7 runs, 5 runs with a wrong
sum; no wrong decision at pumps of 15 to 35 %. Rows of sixteen hold from 0.880 to 1.030 V. At 16 times the noise of
the 225-GHz cell with the 3 % spread, the serial adder is clean from 0.910 to 1.015 V and from 15 to 35 % of pump.
Source: `FINDINGS_after_outline.md`, section 3, and the logs.

## The third and the fourth code

Each was written in one sitting by a modeller who had `BLIND_SPEC_T1.md` and nothing else of the study, and who did
not see the other's work. Each derived the noise from the thermal and shot-noise powers in the cell's own units.
Their reports are `third_code/REPORT.txt` and `fourth_code/REPORT.txt`. Both use a second-order implicit
integrator (BDF2) and their own time step, checked by halving.

Third code (`rebuild_t1x`):
- The lone pair oscillates by itself from 0.97 to 1.14 V. With a 25 % pump at 0.94 V it locks at exactly half the
  pump frequency, 196 mV, on two phases 180 degrees apart, 6 of 12 starts on each.
- Serial adder on two rails, without noise or spread: every pair right at every supply level from 0.880 to 1.015 V;
  lowest level 201.6 mV at 0.94 V and 263.2 mV at 1.015 V.
- With noise and a 3 % spread, 16 draws per level: 724 wrong decisions at 0.880 V, in 16 runs, 13 with a wrong sum;
  none from 0.895 to 1.015 V; none at pumps of 15 and 35 %; at 40 %, 51 wrong decisions in 6 runs, 5 with a wrong sum.
- Row of sixteen with noise and spread: no wrong decision from 0.880 to 1.015 V; 6 in one run at 1.030 V.
- At 16 times the noise, no spread: 14 wrong decisions of 19,840, in 1 run of 32, and no wrong sum.

Fourth code (`rebuild_t1y`):
- The lone pair oscillates by itself from 0.97 to 1.14 V. With a 25 % pump at 0.94 V it locks at half the pump,
  195 mV, on two phases, 6 of 12 starts on each.
- Four-bit adder of 53 pairs, without noise or spread: every pair right from 0.895 to 1.015 V and every sum right;
  lowest level 196.4 mV at 0.94 V.
- With noise and a 3 % spread, 32 draws: no wrong decision of 52,576 at 0.895, 0.94 and 1.000 V; at 1.015 V 14
  wrong decisions in 2 runs. The spread alone causes them; noise alone does not.
- Serial adder: lowest level 195.9 mV at 0.94 V without noise; with noise and spread, no wrong decision at 0.94 and
  1.000 V; at 1.015 V 56 wrong decisions, all in one run, whose pair Mt had its inductance drawn 3.57 standard
  deviations high.

Beyond these lines no other code has checked the specification. The full set of spreads, the eight-bit adder, the
accumulator and the single tolerances at the 1-THz-class noise were run by this package's model only.

## What is shipped and what is not

- Shipped: every script, and the small text results (`.txt`, `.json`, `.log`) that each code wrote.
- Not shipped: the array files (`.npz`) and Python caches. A script that reads an array file needs its producer run
  first. The reports say which run makes which file.
- Changed: only the folder names written into the code. In `rebuild_t1x` and `rebuild_t1y` every script had the
  absolute path of its own folder in a `sys.path.insert` line, and three scripts (`run_lay.py`, `analyse.py` and
  `t1_single.py` of the fourth code) had it in the name of their result folder or file. Each now finds its own
  folder with `os.path.dirname(os.path.abspath(__file__))`. The two reports had the same absolute folder names; they
  now give the folder name alone. Nothing else changed. The other folders had no absolute path.

## Checks run from this folder

One short run per code, started from its place here, on the computer the package was made on. Run them with `python -B`, or Python leaves a `__pycache__` folder beside each code:
- Second code: `second_code/rebuild15/check0.py` prints the diode law (peak 25.39 mA at 0.750 V, valley 11.40 mA at
  1.300 V) and the small-signal modes of cells B, D and F (cell F: the odd mode grows from 1.00 to 1.10 V and decays
  at 0.95 and 1.15 V). And `second_code/rebuild18b/run2.py` with one noiseless point of the serial adder on two rails
  (0.94 V, 25 % pump, links 6 %; 9 s), read by `clean.py`: every pair right, the decoded sum is the sum, lowest level
  201.0 mV. `run2.py` writes a result file `res/run_<tag>.npz` and appends one line to the shipped
  `res/timing.log`; after the check the result file was deleted and the log was restored as shipped. A reader who runs
  the check will see both changes. All six copies of `model.py` import.
- Third code: `third_code/rebuild_t1x/t0_check.py`: the diode law (peak 25.39 mA at 0.750 V), the operating points
  from 0.86 to 1.20 V, and 32 ps of the serial adder for 16 runs (3 s).
- Fourth code: `fourth_code/rebuild_t1y/iter_check.py`: the serial adder without noise, run with 3 and with 6
  iterations of the diode term; phases differ by 1.7e-5 degrees and levels by 1.7e-5 mV (24 s).
