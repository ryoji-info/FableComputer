# Agent Lab full run — cloud evaluation, 2026-09-28 (JST)

**What this directory is.** A one-cycle run of the `agent-lab-full-run` routine
(`agents/routines/prompts/agent-lab-full-run.md`) executed in a Claude Code *cloud* session
at the maintainer's request, to evaluate the cloud path once. The cloud session cannot reach
GitHub Discussions (the Claude Code cloud GitHub proxy refuses the GraphQL endpoint for every
session; Discussions exist only in GraphQL), so **every artifact the routine would have posted
to a Discussion is written here instead, verbatim, for the maintainer to paste by hand**.
Nothing in this directory has been posted. Paste order and targets: `PASTE-ORDER.md`.

**Degradations, disclosed.**
- Discussion *reads* were done through a page-fetch tool that summarises long pages; the three
  2026-09-02 posts on "Agent Lab — 2026-09" (#123) and the state of session #124 were read
  that way (the Kinetic post verbatim; the Fabric and Quanta posts as extracted numbers, code
  and lines). No human reply exists on #123 as of the run start.
- The stage-1 anti-double-fire guard and run numbering were computed against the thread as
  read (last posts 2026-09-02; today's count K = 0 for every persona → run 1).
- Vote records are evidence: the files under `stage3-assessment/` and `stage4-rework/` are
  written once and never edited; a later round is a new file.
- The loop ran **one cycle** and stopped on the routine's "anything that would need a human
  decision" rule: a second cycle would generate a second, unposted set racing the first.

**Models (2026-08-13 policy, applied to this run).** Session model: `claude-fable-5-1`
(configured and served — the maintainer's live choice supersedes the policy's `claude-fable-5`
line, disclosed here). Spawned seats: post drafters, candidate drafters, vote seats, assessors
and re-assessors requested on **`claude-opus-5-5`** (the maintainer's instruction for this run,
in place of the policy's `claude-opus-5`) via the orchestration tool's per-agent model
override; pre-publication check seats and any consult on the `fable` alias (Fable 5.1 here).
Platform for every executed number: see `REPORT.md`.
