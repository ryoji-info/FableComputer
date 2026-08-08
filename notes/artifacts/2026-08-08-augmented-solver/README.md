# Artifacts — 2026-08-08 augmented-solver session
Measured artifacts of [`notes/2026-08-08-augmented-solver-decisive-experiment.md`](../../2026-08-08-augmented-solver-decisive-experiment.md)
(Fable Session [#110](https://github.com/ryoji-info/FableComputer/discussions/110)).

- `augment.py` — the instrument: released `solver.run(drive_kind='none')` transcribed, plus the
  sub-cycled momentum-only viscous sub-step; imports `fable-model-chain/` unedited. Committed
  **byte-identical to the note's §7 listing** (verified independently by two assessment seats); its
  machine-local `CHAIN` constant is therefore preserved — `campaign.py` prepends the repo-relative
  chain path before importing it, so the campaign runs from this directory on any checkout.
- `campaign.py` — the 19-census + confrontation campaign driver (paths repo-relative; ≈66 min).
- `campaign_results.json` — every census: median, `pstdev` sd, range, and all eight per-seed roots.

Provenance: the original session archive was lost to a machine-local scratchpad wipe mid-assessment;
this archive is a deterministic regeneration (fixed seeds, fixed brackets, same platform: Python 3.11.2,
numpy 2.4.6, macOS arm64), swept against the note's printed digits before the promoting PR opened
(sweep result in the PR body). Running `python3 campaign.py` here reproduces it on the same platform.
