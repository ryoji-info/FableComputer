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
2. **Assessment per the script:** each persona (fabric 🧵, kinetic 🌊,
   quanta ⚛️ — adopt from `agents/personas/` with all standing rules)
   independently assesses the session's published reply for the permanent
   record: re-execute the reply's key numbers against the released model code
   in `fable-model-quantum/` and `fable-model-chain/`, check consistency with
   every promoted note in `notes/` (the corrected record), and vote in the
   script's format. 2-of-3 to store.
3. **On a pass:** produce the note file for `notes/` per the script and
   project precedent (metadata header, Status line, method, labels; the full
   per-persona assessment vote record appended verbatim under
   "## Agent assessment — <date>"), push it to a fresh promotion branch, open
   the PR with the script's body text and the `agents:approved-2of3` label.
   Do NOT merge. **On a fail:** post the vote record to the session
   discussion per the script and open nothing.
4. Report: vote tally, PR link (or the fail-record link), one-line summary of
   what was stored or rejected. If any step fails, report exactly how far it
   got.

## Execution mode (default since 2026-07-17)

- These runs default to **Claude Fable 5** (`--model claude-fable-5` in the
  dispatch workflow, overridable per run), with Opus 4.8 as the availability
  fallback. State the executing model in your report; if it is not Fable 5,
  flag that at the top. A transcript published by the Fable-session pipeline
  must always name the model that actually executed — never label output
  "Fable 5" if it is not.
- The maintainer has standing-authorized multi-agent orchestration for these
  runs (2026-07-17): use the Workflow tool for the substantive stages —
  independent persona agents wherever the pipeline calls for independent
  votes or assessments (one persona per agent, blind to each other:
  independence is what makes a 2-of-3 vote meaningful), and adversarial
  verification of every number against the released model code before
  anything is published. The absence of the "ultracode" keyword is not a
  block — this section is the explicit opt-in.
