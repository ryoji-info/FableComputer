# Pipeline: assess a Fable session (2-of-3 vote → promotion PR)

You are the Fable Computer project's executor performing the Agent Lab
**assessment**: deciding whether the latest Fable session's result enters the
permanent record. A maintainer-operated Claude Code run per
[agents/README.md](../README.md) ("Operations"), triggered by the maintainer
(ryoji-info).

Environment: repository checked out at the working directory; `GH_TOKEN` in
the environment for the GitHub API (locally: `git credential fill`). Repo:
`ryoji-info/FableComputer`. Specification:
[`agents/scripts/agent_fable_assess.py`](../scripts/agent_fable_assess.py) —
read it first and follow its exact flow, but YOU perform the three personas'
assessments (no Anthropic API calls).

**Hard rules:** never push to main — promotion goes through a PR branch
(naming per the script / project precedent: `agents/promote-<date>-<slug>`),
a human merges per GOVERNANCE.md; the appended vote record is evidence and is
never edited afterward; disclose "maintainer-operated Claude Code session per
agents/README.md".

1. **Target + state check.** If the maintainer's run note names a discussion,
   use it. Otherwise find the most recent "Fable Session — …" Discussion
   (GraphQL, UPDATED_AT desc) that has NOT been assessed (no assessment
   comments, no corresponding promotion PR or `notes/` file). If everything
   is assessed, stop and report that. If an assessment was started but not
   finished, resume from where it stands.
2. **Round 1 — three fresh, mutually blind assessor seats.** Each persona
   (fabric 🧵, kinetic 🌊, quanta ⚛️ — adopt from `agents/personas/` with all
   standing rules) independently assesses the session's published reply for
   the permanent record: re-execute the reply's key numbers against the
   released model code in `fable-model-quantum/` and `fable-model-chain/`,
   check consistency with every promoted note in `notes/` (the corrected
   record), and vote in the script's format. Where the reply bears on a
   promoted note that registers a standing falsifier, executing that
   falsifier is in-scope assessor work, recorded in the verdict (precedent:
   [#117](https://github.com/ryoji-info/FableComputer/discussions/117)'s
   rounds executed the standing mirrored-run falsifiers at N = 480/720/960 —
   all passed); a fresh falsifier the new note itself registers as never-run
   stays never-run — it is the community's lever, not the assessor's. Judge
   the reply as published: pre-publication checks are the Fable-session
   pipeline's job, not this one's. 2-of-3 `store` is the threshold, but a
   store that attaches required edits is not a clean pass — it goes to
   rework like a rejection.
3. **Rounds.** Post each round's three verdicts verbatim as comments on the
   session Discussion itself; they are evidence and are never edited
   (errata and supplements only). On anything other than a clean pass,
   rework: re-execute every claimed defect against the released, unedited
   code before accepting OR declining it — accept what reproduces; decline
   what does not, recording the refuting measurement — fix the text
   (withdrawal is a valid outcome), then re-assess with three FRESH mutually
   blind seats holding every prior round's record. Hard cap at round 4;
   past it, cut the reply to its defensible core rather than repair it
   again (precedents: PR #98,
   [#103](https://github.com/ryoji-info/FableComputer/discussions/103)).
4. **On a pass:** produce the note file for `notes/` per the script and
   project precedent (metadata header, Status line, method, labels; the
   deciding round's full per-persona vote record appended verbatim under
   "## Agent assessment — <date>", earlier rounds permanent on the
   Discussion), push it to a fresh promotion branch, open the PR with the
   script's body text and the `agents:approved-2of3` label — and in the SAME
   PR maintain the navigation layer per the 2026-07-26 finding-5 rule: add
   the note's `notes/INDEX.md` row, update the rows it changes, and append a
   dated post-promotion annotation to each promoted note it corrects
   (precedent: PRs #116 and #118). Do NOT merge. **On a final fail:** the
   posted round records are the outcome — open nothing and report it.
5. Report: rounds reached, per-round tallies, PR link (or the final fail
   record), what was declined and on what measurement, and a one-line
   summary of what was stored or rejected. If any step fails, report exactly
   how far it got.

## Execution mode (mixed models by seat since 2026-08-13; orchestration since 2026-07-17)

- **Seat models** (maintainer policy, 2026-08-13; authoritative text: the
  MODEL section of
  [`agents/routines/prompts/agent-lab-full-run.md`](../routines/prompts/agent-lab-full-run.md),
  which supersedes the 2026-07-17 all-Fable-5 default): assessor and
  re-assessor seats run on **claude-opus-5** (the record's practice since
  [#115](https://github.com/ryoji-info/FableComputer/discussions/115) /
  PR #116); orchestration and any rework drafting run on the session model,
  **claude-fable-5** (`--model` in the dispatch workflow, overridable per
  run). Availability fallback for any seat is **claude-opus-5**: record the
  error verbatim; a seat interrupted by a session limit is relaunched fresh
  after the reset with the loss disclosed in that round's record (precedent:
  2026-08-12); never present fallback output as Fable 5. The briefing
  template in `agent_fable_assess.py` hardcodes that the reply was "produced
  by Claude Fable 5" — brief assessors with the reply's ACTUAL executing
  model whenever they differ; the script predates this policy, so extend it
  at run time rather than follow it into a mislabel.
- **Disclose models per seat, on every run.** Every posted vote record names
  each seat's model; the report states the session model.
- The maintainer has standing-authorized multi-agent orchestration for these
  runs (2026-07-17 — the opt-in remains in force under the 2026-08-13
  policy): use the Workflow tool for the substantive stages —
  independent persona agents wherever the pipeline calls for independent
  votes or assessments (one persona per agent, blind to each other:
  independence is what makes a 2-of-3 vote meaningful), and adversarial
  verification of every number against the released model code before
  anything is published. The absence of the "ultracode" keyword is not a
  block — this section is the explicit opt-in.
