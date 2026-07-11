<img src="branding/boogie-sorbet-monogram.svg" alt="" width="72" align="right">

# Contributing

Thank you for looking. This project's claims live or die on scrutiny, so
**every kind of serious engagement is a contribution** — including the kind
that proves something wrong.

## First: run the models

```bash
git clone https://github.com/ryoji-info/FableComputer.git
cd FableComputer/fable-model-chain
python run_all.py --json      # Part I  — every manuscript number
cd ../fable-model-quantum
python run_all.py --json      # Part II — every manuscript number
```

Requirements: Python 3.11+, `numpy`, `matplotlib` (figures only). Each module
also runs standalone and prints a self-check against the manuscript values.

## What counts as a substantive contribution

- **A reproduction report.** Run a model chain on your machine and report the
  outcome in [REPLICATIONS.md](REPLICATIONS.md) via PR — including version,
  platform, and any numbers that *didn't* match. A failed reproduction is at
  least as valuable as a successful one.
- **A technical critique.** A documented argument that an assumption is
  wrong, a derivation has an error, or a cited precedent doesn't support what
  it's cited for. Open an issue with the specifics. The manuscripts state
  exactly which assumptions are load-bearing (Part I §2; Part II §§2–3, 8).
- **Code.** Solver improvements (grid refinement of the shallow-water solver,
  calibration of the per-pulse gain, tightening the disorder-yield criterion),
  ports (e.g. Julia), tests, CI, packaging.
- **The big open builds.** The Boltzmann–Maxwell simulation tier and the
  pulsed-clock synthesis design — see [ROADMAP.md](ROADMAP.md).
- **Documentation, translation, review.** Anything that makes the work easier
  to check.

Substantive contributions are the path to voting membership
([GOVERNANCE.md](GOVERNANCE.md)) and, where they meet the criteria, to
co-authorship on resulting papers ([AUTHORSHIP.md](AUTHORSHIP.md)).

## Ground rules for changes

- **Claims match evidence.** Model results are labeled *in-model*; measured
  results cite their source; speculation is labeled speculation. This
  discipline is the project's main asset — PRs that erode it will be asked to
  reword before anything else is reviewed.
- **Reproducibility is non-negotiable.** A change to a model must keep
  `run_all.py --json` running and update `results.json` and the self-checks
  it touches, with the change explained in the PR.
- **Match the codebase's style.** Plain Python, `numpy` only in the model
  chains, transparent formulas over clever abstractions, physics comments
  where a constant or approximation comes from a manuscript equation.
- **Review windows.** Non-trivial PRs stay open at least 72 hours for review
  (lazy consensus — see [GOVERNANCE.md](GOVERNANCE.md)).
- **Disclose substantial AI assistance** in the PR description — the same
  rule the manuscripts follow on page one. It affects review attention, not
  acceptance.

## Response promise

Every issue and PR gets a human response within **24 hours** (usually much
faster). If the project ever can't keep that promise, this file will say so.

## Conduct

Rigorous skepticism of the work is expected; hostility toward people is not.
See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
