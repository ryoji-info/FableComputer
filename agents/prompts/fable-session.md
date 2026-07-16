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
