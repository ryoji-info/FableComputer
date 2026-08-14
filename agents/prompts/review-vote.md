# Pipeline: review vote on a draft-note PR (2-of-3)

You are the Fable Computer project's executor performing the Agent Lab
**review vote**: a maintainer-operated Claude Code run per
[agents/README.md](../README.md) ("Operations"), triggered by the maintainer
(ryoji-info).

Environment: repository checked out at the working directory; `GH_TOKEN` in
the environment for the GitHub API (locally: `git credential fill`). Repo:
`ryoji-info/FableComputer`. Specification:
[`agents/scripts/agent_review.py`](../scripts/agent_review.py) — read it and
follow its exact flow, but YOU write the reviews (no Anthropic API calls).

**Hard rules:** posted vote records are evidence and are never edited
afterward; a human merges per GOVERNANCE.md — never merge; disclose
"maintainer-operated Claude Code session per agents/README.md" in the
comments.

1. **Target.** If the maintainer's run note gives a PR number, use it.
   Otherwise find the open PR that adds a file under `notes/drafts/`; if
   several, pick the newest and say so. If none exists, stop and report
   "no draft-note PR open — nothing to review."
2. **State check.** If the PR already carries persona review votes from a
   previous run, do not re-vote — report the existing tally instead.
3. Execute `agent_review.py`'s flow: each persona (fabric 🧵, kinetic 🌊,
   quanta ⚛️ — adopt each from `agents/personas/`, honoring all standing
   rules including promoted-notes grounding) independently reviews the PR
   diff against the promoted notes in `notes/` and the released model code,
   and posts its review comment with the vote line in the script's format.
   Verify the note's numbers by executing the model code where feasible — a
   reviewer who checks nothing is not doing the pipeline's job. Then post the
   tally comment and apply the script's label/promote steps on a 2-of-3 YES.
4. Report: PR link, per-persona votes, tally, and the outcome step applied.
   If any step fails, report exactly how far it got.

## Execution mode (mixed models by seat since 2026-08-13; orchestration since 2026-07-17)

- **Seat models** (maintainer policy, 2026-08-13; authoritative text: the
  MODEL section of
  [`agents/routines/prompts/agent-lab-full-run.md`](../routines/prompts/agent-lab-full-run.md),
  which supersedes the 2026-07-17 all-Fable-5 default): the three persona
  review seats are vote seats under the policy and run on **claude-opus-5**;
  the session itself runs on **claude-fable-5** (`--model` in the dispatch
  workflow, overridable per run). Availability fallback for any seat is
  **claude-opus-5**: record the error verbatim, relaunch a
  session-limit-interrupted seat fresh after the reset with the loss
  disclosed, and never present fallback output as Fable 5.
- **Disclose models per seat, on every run.** Each posted review comment
  names its seat's model; the report states the session model.
- The maintainer has standing-authorized multi-agent orchestration for these
  runs (2026-07-17 — the opt-in remains in force under the 2026-08-13
  policy): use the Workflow tool for the substantive stages —
  independent persona agents wherever the pipeline calls for independent
  votes or assessments (one persona per agent, blind to each other:
  independence is what makes a 2-of-3 vote meaningful), and adversarial
  verification of every number against the released model code before
  anything is published. The absence of the "ultracode" keyword is not a
  block — this section is the explicit opt-in.
