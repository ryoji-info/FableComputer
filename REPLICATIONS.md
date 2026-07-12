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
| 2026-07-12 | R. Furui (maintainer), via Claude Fable 5 session | Pre-registered prediction resolutions: retuned-cavity gain, N=480 threshold, half-bias gain, thermal-only BER | Windows 11, CPython + numpy | ✅ **4/4 CONFIRMED** (9.2246 dB; 0.158748; 5.1291 dB; 5.494×10⁻¹²) | [notes/drafts/2026-07-12-predictions-resolved.md](notes/drafts/2026-07-12-predictions-resolved.md); runner embedded there |

## Independent ports

| Date | Who | Language / stack | Coverage | Result | Notes / link |
|---|---|---|---|---|---|
| — | *yours here* | | | | |

## Bench gates (G1–G5, QG1–QG5)

No experimental attempts yet. The pre-registered pass/fail protocols are
specified in Part I §10 and Part II; see [ROADMAP.md](ROADMAP.md) WP4. When
attempts begin, each gets a row here: lab, gate, pre-registered threshold,
outcome.
