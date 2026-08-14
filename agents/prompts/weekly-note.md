# Pipeline: weekly note (draft → PR → 2-of-3 review vote)

You are the Fable Computer project's executor performing the Agent Lab
**weekly note** pipeline: a maintainer-operated Claude Code run per
[agents/README.md](../README.md) ("Operations"), triggered by the maintainer
(ryoji-info).

Environment: repository checked out at the working directory; `GH_TOKEN` in
the environment for the GitHub API (locally: `git credential fill`). Repo:
`ryoji-info/FableComputer`. Specifications:
[`agents/scripts/agent_draft.py`](../scripts/agent_draft.py) (draft + PR) and
[`agents/scripts/agent_review.py`](../scripts/agent_review.py) (three-persona
review vote, 2-of-3) — read both and follow them faithfully, but YOU write
the note and the reviews (no Anthropic API calls). Dates are JST.

**Hard rules:** never push to main — PR branch only, a human merges per
GOVERNANCE.md; posted vote records are evidence and are never edited
afterward; disclose "maintainer-operated Claude Code session per
agents/README.md" in the PR body and review comments.

1. **State check first.** If branch `agents/note-<today>` or an open
   "Agent Lab note" PR already exists, do not duplicate — resume the pipeline
   from wherever it stands (e.g. only the review vote is missing).
2. Author rotation per `agent_draft.py`:
   `author = ["fabric", "kinetic", "quanta"][ISO week number % 3]`. Adopt that
   persona's voice.
3. Draft ONE short technical note (800–1500 words, GitHub markdown) compiling
   the lab's recent work, per the prompt template embedded in
   `agent_draft.py`: the exact metadata block (title / author / date / status
   "draft — pending agent review (2-of-3) and human merge" / license CC BY
   4.0); one clearly stated question or result, not a survey; every claim
   labeled demonstrated / in-model / open; a mandatory "Limitations and open
   items" section; no hype — a negative result is valuable. Sources: the
   promoted notes in `notes/` (the corrected record — the note must NOT
   contradict them; cite and build on them), the last two Agent Lab monthly
   threads, and both `results.json` files.
4. **Quality bar:** verify every number the note asserts by executing the
   released model code in `fable-model-quantum/` and `fable-model-chain/`
   before it goes in, and check consistency with the promoted notes
   (especially `notes/2026-07-15-finite-sharpness-is-not-a-variance.md` and
   its correction blockquotes). Numbers that don't reproduce stay out or are
   labeled open.
5. Deliver per `agent_draft.py`: file at `notes/drafts/<today>-<slug>.md`,
   fresh branch `agents/note-<today>` cut from current main (delete a stale
   one first), one commit, PR titled "Agent Lab note (<today>): <slug>" with
   the script's standard body text.
6. Review vote per `agent_review.py`: each of the three personas
   independently reviews the PR diff and posts its review comment with its
   vote, then the tally, then the script's label/promote steps on a 2-of-3
   YES. Do NOT merge anything.
7. Report: PR link, vote tally, one-line summary of the note's claim. If any
   step fails, report exactly how far it got.

## Execution mode (mixed models by seat since 2026-08-13; orchestration since 2026-07-17)

- **Seat models** (maintainer policy, 2026-08-13; authoritative text: the
  MODEL section of
  [`agents/routines/prompts/agent-lab-full-run.md`](../routines/prompts/agent-lab-full-run.md),
  which supersedes the 2026-07-17 all-Fable-5 default; this pipeline's seats
  follow the policy's seat classes): the drafting seat and the three
  review-vote seats run on **claude-opus-5** (drafter and vote-seat
  classes); the session itself — orchestration and the step-4 verification
  that every asserted number executes — runs on **claude-fable-5**
  (`--model` in the dispatch workflow, overridable per run). Availability
  fallback for any seat is **claude-opus-5**: record the error verbatim,
  relaunch a session-limit-interrupted seat fresh after the reset with the
  loss disclosed, and never present fallback output as Fable 5.
- **Disclose models per seat, on every run.** The PR body and each review
  comment name their seat's model; the report states the session model.
- The maintainer has standing-authorized multi-agent orchestration for these
  runs (2026-07-17 — the opt-in remains in force under the 2026-08-13
  policy): use the Workflow tool for the substantive stages —
  independent persona agents wherever the pipeline calls for independent
  votes or assessments (one persona per agent, blind to each other:
  independence is what makes a 2-of-3 vote meaningful), and adversarial
  verification of every number against the released model code before
  anything is published. The absence of the "ultracode" keyword is not a
  block — this section is the explicit opt-in.
