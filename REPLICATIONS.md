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
| 2026-06 | R. Furui (author) | `fable-model-chain` full run (`run_all.py --json`) | Python 3.11 | ✅ matches manuscript v5 | Baseline; `results.json` in repo |
| 2026-07 | R. Furui (author) | `fable-model-quantum` full run (`run_all.py --json`) | Python 3.11 | ✅ matches manuscript Part II | Baseline; `results.json` in repo |

## Independent ports

| Date | Who | Language / stack | Coverage | Result | Notes / link |
|---|---|---|---|---|---|
| — | *yours here* | | | | |

## Bench gates (G1–G5, QG1–QG5)

No experimental attempts yet. The pre-registered pass/fail protocols are
specified in Part I §10 and Part II; see [ROADMAP.md](ROADMAP.md) WP4. When
attempts begin, each gets a row here: lab, gate, pre-registered threshold,
outcome.
