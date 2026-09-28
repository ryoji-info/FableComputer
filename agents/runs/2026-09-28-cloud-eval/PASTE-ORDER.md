# Paste order — what goes where (nothing in this directory has been posted)

Post in this order so the record reads as the routine would have written it. Every file is verbatim; do not edit the vote records.

## Stage 1 — "Agent Lab — 2026-09" (discussion #123), one comment each, in this order
1. `stage1-posts/fabric.md`
2. `stage1-posts/kinetic.md`
3. `stage1-posts/quanta.md`

(`*-record.md` and `stage1-posts/REPORT.md` are the run's evidence, not for posting.)

## Stage 2 — a new Discussion in the Agent Lab category
1. Title and body: `stage2-session/10-discussion-body.md` (the title is its first heading).
2. Comment 1: `stage2-session/02-losing-candidates.md` (the two candidates that did not win, in full).
3. Comment 2: `stage2-session/13-prepublication-checks.md` (the two blind check seats' records and what changed).
4. Comment 3 (split at 60,000 characters if needed): `stage2-session/11-reply.md`.
5. Comment 4: `stage2-session/12-listings.md` (the runnable sources).

(`01-candidates-and-vote.md` and `03-seat-records.md` are the vote's evidence — `01` duplicates the body's candidate/vote section for the run report; `03` carries the seats' prior-art checks and premise audits, worth posting as a fifth comment if the maintainer wants the audit public.)

## Stage 3 / Stage 4 — comments on the same session Discussion, in round order (every file verbatim; vote records are never edited)
1. Round 1 (stage 3): `stage3-assessment/round-1-fabric.md`, `round-1-kinetic.md`, `round-1-quanta.md` — one comment each — then `round-1-tally.md` (2 store with required edits / 1 reject → rework).
2. Round 2 (stage 4): `stage4-rework/round-2-record.md`; `round-2-reply.md` (**superseded** — post it for the record, headed as superseded, or link the file); then `round-2-fabric.md`, `round-2-kinetic.md`, `round-2-quanta.md`, `round-2-tally.md` (0 / 3).
3. Round 3: `stage4-rework/round-3-record.md`; `round-3-reply.md` (**superseded**; two comments at its marked split) with `round-3-tables-appendix.md` appended to the listings comment; then `round-3-fabric.md`, `round-3-kinetic.md`, `round-3-quanta.md`, `round-3-tally.md` (3 store with required edits / 0 reject → round 4).
4. Round 4 (the cap): `stage4-rework/round-4-record.md`; `round-4-reply.md` (**the text under assessment** — three comments at its marked splits) with `round-4-tables-appendix.md` (Tables 2b and 5) pasted into the listings comment before the sources; the rework listings `stage4-rework/listings/*.py` (rw_*.py, rw3_*.py, rw4_*.py, build_r*.py) as a further listings comment; then `round-4-fabric.md`, `round-4-kinetic.md`, `round-4-quanta.md`, `round-4-tally.md`.
5. Outcome: see `REPORT.md` (written when the round-4 verdict lands). If round 4 is a clean pass the note, its `notes/INDEX.md` row and the annotations are on this branch and the promotion PR carries the `agents:approved-2of3` label; the note file must carry the appendix tables (its §4 rests on Table 5), and any script-path promotion must not truncate at 60,000 characters (`agent_fable_assess.py`'s read) — the note is longer than that, as 08-13's (78k) and 08-02's (152k) are.
