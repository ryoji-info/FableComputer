<img src="branding/boogie-sorbet-monogram.svg" alt="" width="72" align="right">

# Replication Tracker

Every attempt to reproduce this project's results — model reruns, independent
ports, and (eventually) bench experiments — is logged here, **whatever the
outcome**. A failed reproduction with details is one of the most valuable
contributions this project can receive.

To add a row, open a pull request. Include enough detail that someone else
could investigate a mismatch: OS, Python version, package versions, and which
self-checks passed or failed.

## Model chains

| Date | Who | What | Platform | Result | Notes / link |
|---|---|---|---|---|---|
| 2026-06 | R. Furui (author) | `fable-model-chain` full run (`run_all.py --json`) | Python 3.11 | ✅ matches manuscript v5 (Zenodo v5f) | Baseline; `results.json` in repo |
| 2026-07 | R. Furui (author) | `fable-model-quantum` full run (`run_all.py --json`) | Python 3.11 | ✅ matches manuscript Part II | Baseline; `results.json` in repo |
| 2026-07-12 | R. Furui (maintainer), via Claude Fable 5 session | `pulse_gain_dB_at_0p7_streaming` + `classical_BER_300K` baseline re-runs | Windows 11, CPython + numpy | ✅ bit-for-bit (7.7967069614868425; 3.6059121172811077e-11) | Precondition for the prediction resolutions below |
| 2026-07-12 | R. Furui (maintainer), via Claude Fable 5 session | Pre-registered prediction resolutions: retuned-cavity gain, N=480 threshold, half-bias gain, thermal-only BER | Windows 11, CPython + numpy | ✅ **4/4 CONFIRMED** (9.2246 dB; 0.158748; 5.1291 dB; 5.494×10⁻¹²) | [notes/2026-07-12-predictions-resolved.md](notes/2026-07-12-predictions-resolved.md); runner embedded there |

## Pre-registered keys

Predictions this project registered *before* running them, with what the run returned.
A falsified prediction is a result, not an embarrassment — three of the rows below are
falsifications and each one moved the record.

| key / quantity | registered value | falsified if | outcome | source |
|---|---|---|---|---|
| retuned streaming gain | 8.77 ± 0.35 dB | outside 8.2–9.3 dB | **9.2246 dB** — outside the central band (that grading stands), inside the stated refutation limits | [07-11](notes/2026-07-11-retuned-streaming-gain-prediction.md) |
| retuned streaming gain (re-registered) | 9.05 ± 0.30 dB | outside the band | ✅ **confirmed** at 9.2246 dB | [07-12 exact operator](notes/2026-07-12-boundary-factor-exact-operator.md) |
| `M_th_num` at N = 480 | 0.1590 ± 0.0010 | outside the band | ✅ **confirmed** at 0.158748 | [07-12 resolved](notes/2026-07-12-predictions-resolved.md) |
| `M_th_num_inviscid_limit` | 0.1490 [0.147, 0.150] | outside the band | ✅ **confirmed** at 0.149313 — and it is *not* the analytic 0.147083 | [07-22 viscosity](notes/2026-07-22-mth-numerical-vs-physical-viscosity.md) |
| `M_th_kinetic_353K` | 0.165 [0.154, 0.169] | outside the band | in-model; now emitted in `results.json` | [07-22 viscosity](notes/2026-07-22-mth-numerical-vs-physical-viscosity.md) |
| von Neumann sharpened partition | 8.69 ± 0.20 dB | outside 8.3–9.1 dB | ⛔ **falsified by its own criterion** (9.2246 dB) | [07-12 von Neumann](notes/2026-07-12-effective-loop-von-neumann.md) |
| per-slot-peak streaming waypoint | ≈8.87 dB | — | ⛔ **falsified**: measured 7.8511 dB | [07-17 drive sweep](notes/2026-07-17-drive-sweep-knee-anchored.md) |
| drive-amplitude compression bucket | 0.2–0.8 dB | — | ⛔ **falsified**: measured 0.062 dB | [07-17 drive sweep](notes/2026-07-17-drive-sweep-knee-anchored.md) |
| `A_SAT_eff` (drive plane) | [0.0150, 0.0226] | outside the band | ✅ knee measured at 0.76–1.15 % source amplitude | [07-17 drive sweep](notes/2026-07-17-drive-sweep-knee-anchored.md) |
| `ringdown_isi_pp_dB_0p7_0p25THz` | 4.0 [2.0, 4.5] | a rerun of its own §6 listing, or a loaded/gated transient, outside the band | ⚠️ **scoped**: the stricter burst-window convention measured 4.90 and 4.91 | [07-22 ring-down](notes/2026-07-22-cavity-ringdown-isi.md) |
| `f_max_F2_flushed_THz` | 0.115 [0.079, 0.153] | outside the band | ⚠️ carries the burst-length proviso — the centre is reached at no measured burst length | [07-23](notes/2026-07-23-reset-switch-adjudication.md), [07-25](notes/2026-07-25-e1-burst-scaling-proviso.md) |
| decoder averaging floor at k = 16 | (¾)erfc(k/(4√2·c)) = 8.73×10⁻⁴⁴ at c = 1/√12 | — | emitted as `avg16_floor_c_kdec`, parameterized in **c and k jointly** — the k-only form was withdrawn | [07-14](notes/2026-07-14-q2bit-avg16-averaging-convention.md), [07-15](notes/2026-07-15-finite-sharpness-is-not-a-variance.md) |

## Reproducing on a different platform — read this first

The committed `results.json` files were generated on **Windows / CPython**. Platform
libm implementations differ in the last bits, so a faithful rerun on Linux or macOS can
land **1 ULP** away from a stored value. CI caught exactly this: `avg16_2bit_300K`
recomputed on Linux as `4.7022673057229145e-07` against the stored
`4.702267305722915e-07`.

**That is a match, not a mismatch.** `tests/test_published_claims.py` pins published
values with a relative tolerance of `1e-12` — about four orders of magnitude tighter
than any claim in the record depends on. Identities computed twice inside one
interpreter (for example `error_2bit(300, 400, n_avg=16) == error_2bit(300, 6400,
n_avg=1)`) are asserted **exactly**, because that comparison is platform-free. If you
log a reproduction, please say which platform you used and quote the digits you saw.

## Independent ports

| Date | Who | Language / stack | Coverage | Result | Notes / link |
|---|---|---|---|---|---|
| — | *yours here* | | | | |

## Bench gates (G1–G5, QG1–QG5)

No experimental attempts yet. The pre-registered pass/fail protocols are
specified in Part I §10 and Part II; see [ROADMAP.md](ROADMAP.md) WP4. When
attempts begin, each gets a row here: lab, gate, pre-registered threshold,
outcome.
