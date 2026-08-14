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
   not a duplicate session. (Inside the full-run routine this gate is
   relaxed to a 90-minute anti-duplicate guard with roman-numeral titles —
   project precedent: four sessions on 2026-07-26; the standalone stop here
   stays conservative on purpose.)
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
5. **Pre-publication check — before anything is published** (practice since
   2026-08-12/13): spawn two independent check seats, blind to each other
   and sharing no context with the execution, to adversarially verify the
   reply's key numbers against the released code and its epistemic labels
   against the promoted notes. Fix every defect that reproduces before
   publishing, and record in the transcript that the checks ran and what
   they changed. Catching defects here is this pipeline's job — the
   assessment pipeline judges the reply as published.
6. **Publish per the script:** a new Discussion titled
   "Fable Session — <date>: <short title>" in the category the script uses,
   containing the three candidates, the vote record, the winning prompt, the
   check records, and the full session reply, with the standard disclosure
   header ("maintainer-operated Claude Code session per agents/README.md")
   plus a per-seat model line (candidates, vote, execution, checks). Vote
   records are evidence — never edit them after posting.
7. Report: discussion link, the winning prompt's author and question, what
   the check seats changed, and a one-line summary of the session's verdict.
   Note that assess-session is the follow-up if the reply looks note-worthy.
   If any step fails, report exactly how far it got.

## Execution mode (mixed models by seat since 2026-08-13; orchestration since 2026-07-17)

- **Seat models** (maintainer policy, 2026-08-13; authoritative text: the
  MODEL section of
  [`agents/routines/prompts/agent-lab-full-run.md`](../routines/prompts/agent-lab-full-run.md),
  which supersedes the 2026-07-17 all-Fable-5 default): candidate-drafter
  seats and vote seats run on **claude-opus-5**; the execution of the
  winning prompt runs on the session model, **claude-fable-5** (`--model` in
  the dispatch workflow, overridable per run); the pre-publication check
  seats run on **claude-fable-5**. Role language is not model language:
  "YOU perform every role" governs who does the work, not which model runs
  it — candidates and votes stay independent, mutually blind spawned seats,
  no self-votes. Availability fallback for any seat is **claude-opus-5**:
  record the error verbatim, relaunch a session-limit-interrupted seat fresh
  after the reset with the loss disclosed, and never present fallback output
  as Fable 5.
- **Disclose models per seat, on every run.** The published session
  Discussion carries a per-seat model line — candidates, vote, execution,
  checks — in addition to the standard disclosure header. Never label
  another model's output "Fable 5", and label Fable 5's contribution as
  Fable 5.
- The maintainer has standing-authorized multi-agent orchestration for these
  runs (2026-07-17 — the opt-in remains in force under the 2026-08-13
  policy): use the Workflow tool for the substantive stages —
  independent persona agents wherever the pipeline calls for independent
  votes or assessments (one persona per agent, blind to each other:
  independence is what makes a 2-of-3 vote meaningful), and adversarial
  verification of every number against the released model code before
  anything is published. The absence of the "ultracode" keyword is not a
  block — this section is the explicit opt-in.
