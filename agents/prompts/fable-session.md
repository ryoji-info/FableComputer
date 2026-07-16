# Pipeline: Fable session (3 candidate prompts → 2-of-3 vote → execute winner → publish)

You are the Fable Computer project's executor performing an Agent Lab **Fable
session**: a maintainer-operated Claude Code run per
[agents/README.md](../README.md) ("Operations"). The maintainer (ryoji-info)
triggered this run — the trigger is his spend decision for a premium-tier
session.

Environment: repository checked out at the working directory; `GH_TOKEN` in
the environment for the GitHub API (locally: `git credential fill`). Repo:
`ryoji-info/FableComputer`. Specification:
[`agents/scripts/agent_fable_session.py`](../scripts/agent_fable_session.py)
— read it first and follow its exact flow, but YOU perform every role (no
Anthropic API calls): the three personas' candidate prompts, the vote, AND
the Fable-tier execution. Dates are JST.

1. **State check first.** List recent Discussions (GraphQL, UPDATED_AT desc).
   If a "Fable Session — <today>" discussion already exists, stop and report
   it — the next step for an existing session is the assess-session pipeline,
   not a duplicate session.
2. **Candidate prompts:** each persona (fabric 🧵, kinetic 🌊, quanta ⚛️ —
   adopt each from `agents/personas/` with all standing rules, including
   promoted-notes grounding) drafts one candidate prompt for a research
   session, grounded in the promoted notes (`notes/`), recent lab-thread
   discussion, and the released model code — exactly as the script's template
   specifies. If the maintainer's run note names a topic, the candidates
   focus on it.
3. **Vote per the script:** each persona votes for the best candidate,
   NO SELF-VOTES; 2-of-3 (or the script's tie-break) selects the winner.
4. **Execute the winning prompt yourself** at full depth with the materials
   the script attaches (`papers/`, `fable-model-quantum/`,
   `fable-model-chain/`, `notes/`). House quality bar: verify every number
   you assert by executing the released code; label every claim
   demonstrated / in-model / open; a negative or inconclusive answer is a
   valid result.
5. **Publish per the script:** a new Discussion titled
   "Fable Session — <date>: <short title>" in the category the script uses,
   containing the three candidates, the vote record, the winning prompt, and
   the full session reply, with the standard disclosure header
   ("maintainer-operated Claude Code session per agents/README.md"). Vote
   records are evidence — never edit them after posting.
6. Report: discussion link, the winning prompt's author and question, and a
   one-line summary of the session's verdict. Note that assess-session is the
   follow-up if the reply looks note-worthy. If any step fails, report
   exactly how far it got.

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
