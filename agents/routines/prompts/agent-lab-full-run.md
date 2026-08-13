Run the Fable Computer Agent Lab's pipeline end to end, in one session, in this exact order:

  Stage 1 — "1. Agent lab posts"          → ~/.claude/scheduled-tasks/agent-lab-posts/SKILL.md
  Stage 2 — "2. Agent lab fable session"  → ~/.claude/scheduled-tasks/agent-lab-fable-session/SKILL.md
  Stage 3 — "3. Agent lab assess session" → ~/.claude/scheduled-tasks/agent-lab-assess-session/SKILL.md
  Stage 4 — REWORK (below; no separate SKILL.md — this prompt is its specification)

For stages 1–3, Read that SKILL.md in full and execute its body faithfully as if it were your own prompt — that file is the single source of truth for everything except model choice (the MODEL section below supersedes the stage prompts' model, seat-model and model-disclosure language), so never work from a summary, from this prompt's paraphrase, or from memory of a previous run. Finish a stage completely, including producing its report, before starting the next.

WORKING DIRECTORY. This task may not have the repo as its cwd. The repo is {{REPO}} (github.com/ryoji-info/FableComputer). Resolve every repo-relative path in the stage prompts (agents/…, notes/, papers/, fable-model-chain/, fable-model-quantum/) against that absolute path, and either cd into the repo first or pass -C {{REPO}} to git. {{PLATFORM_NOTE}} GitHub token when needed: TOKEN=$(printf "protocol=https\nhost=github.com\n" | git credential fill 2>/dev/null | grep '^password=' | cut -d= -f2), then Authorization: Bearer for REST/GraphQL; do not rely on the gh CLI.

MODEL (maintainer request, 2026-08-13 — supersedes the 2026-08-05 "this pipeline runs on Claude Opus 5" paragraph, and supersedes ALL model language in the three stage prompts: their "meant to run on Claude Fable 5" lines, their model self-checks' disclosure conditionals, and the relayed 2026-07-17 "run all routines on Fable 5 ultracode by default" instruction — that relay's orchestration opt-in remains in force; only its model default is superseded). This pipeline runs MIXED, BY SEAT, per the 2026-08-13 cost/performance review of the community record: the premium model goes to the single-seat, highest-leverage stages; the multi-seat volume stages run on Opus 5.

- **Session model: `claude-fable-5`.** The maintainer sets it with /model before Run now. Main-loop work — orchestration, stage 2's execution of the winning prompt, and stage 4's reworks — runs on the session model. If the maintainer has the running session on a different model, that live choice supersedes this line for that run: proceed on it, disclose the actual model, and do not report a wrong-model condition, ask the maintainer to fix a model picker, or let the model check stop or alter a stage.
- **Per-seat model overrides — set explicitly on every spawn; never let a seat silently inherit the session model:**
  - Stage 1 post drafters; stage 2 candidate drafters and vote seats; stage 3 assessors; stage 4 re-assessors → `model: "opus"` (claude-opus-5).
  - Pre-publication check seats — stage 2's independent check agents ("adversarially verify its key numbers … BEFORE publishing") AND stage 1's optional pre-posting check agent → `model: "fable"` (claude-fable-5).
  - Stage 4's Fable 5 consult → `model: "fable"` as before (see ESCALATION; its per-run budget still applies).
- **Role language is not model language.** Stage-prompt phrases like stage 2's "YOU perform every role" govern who does the work, not which model runs it: candidates, votes, assessments and re-assessments stay independent, mutually blind spawned seats per ORCHESTRATION, on the models above. Stage 1's solo-drafting allowance remains permitted, but the default under this policy is spawned Opus drafter seats; a post drafted in-session runs on the session model and must be disclosed as such in the run report.
- **Fallback (precedented: 2026-07-18 lost the execution to Opus 4.8 mid-vote; 2026-08-12 lost three assessor seats mid-round).** If Fable 5 errors or its credits exhaust mid-run, fall back to `claude-opus-5` for the affected seat(s), record the error verbatim, and never present fallback output as Fable 5. A mid-run Fable exhaustion is a disclosed degradation of the affected seats, not by itself a stop — the LOOP section's credits-exhaustion stop applies when the run as a whole can no longer proceed.
- **Honesty rule — unchanged and extended to per-seat disclosure.** In anything PUBLISHED — the Fable Session transcript above all — disclose the executing model truthfully, seat by seat: which model produced the posts, the candidates and votes, the execution, the pre-publication checks, each assessment round, each rework, and any consult. Never label output "Fable 5" when another model produced it, and label Fable 5's contribution as Fable 5. State the session model once at the top of the final report, plus a one-line per-stage seat-model summary. Stage 2's "if you are not Fable 5" disclosure conditional is superseded: per-seat disclosure applies on every run, including all-nominal ones.
- **The stage templates and agents/scripts/ predate this policy — extend or correct them at run time, never follow them into a mislabel.** The stage-2 transcript template discloses only the execution model: add one per-seat model line to the published session discussion (candidates, votes, execution, checks). The assessor briefing template in agents/scripts/agent_fable_assess.py hardcodes that the reply was "produced by Claude Fable 5": brief assessors with the reply's ACTUAL executing model whenever they differ (e.g. after a fallback). The stage-1 lab-post header names no model — keep that header exactly as the stage prompt mandates and record the drafting seat's model in the run report instead.

ORCHESTRATION. The stage prompts carry the maintainer's standing opt-in for multi-agent orchestration; honour it where they specify it, because it is load-bearing, not decorative — stage 2's candidate prompts, stage 3's three assessments and stage 4's re-assessments must come from INDEPENDENT agents blind to each other, or the 2-of-3 vote is not a real vote. No self-votes. Verify asserted numbers by executing the released code.

SEQUENCING. Stage 2 refuses to run if a "Fable Session — <today JST>" discussion already exists (as relaxed below); stage 3 targets the latest UNASSESSED session. That is the intended chain, so run them in order and let each stage's own state check decide. A stage stopping on its own state check (nothing due, already posted, already assessed) is a NORMAL outcome, not a failure: record it and continue to the next stage. If a stage fails part-way, record exactly how far it got and still attempt the remaining stages. Never push to main; promotion goes through a PR that a human merges.

---

# STAGE 4 — REWORK THE REJECTION

**Trigger.** Run this stage whenever stage 3 ends in anything other than a clean pass: fewer than 2 of 3 `store` votes, **or** a pass whose accepting assessors attached required edits. A rejection is not the end of the pipeline — it is the point of it. The crew's job is to get the result right, not to record that it was wrong.

**Also run it on a standing rejection.** If stage 3 stops because everything is already assessed, check whether the most recent assessed session was *rejected* and never reworked. If so, that session is stage 4's target and the stage runs on it. Prefer the newest unreworked rejection; do not rework a session the maintainer has closed out.

## Round discipline — this is a court record, not a draft

Round 1 is stage 3's verdict. Rework rounds are 2, 3 and 4.

- **Posted vote records are evidence and are NEVER edited or deleted.** Each round posts its own record; earlier rounds are linked, not rewritten. If a fix would require altering a posted record, do not make it — stop and report instead.
- **Hard cap at round 4.** Precedent (PR #98, 2026-08-02): after three rounds of 3 × revise, the maintainer's direction was to **cut the note to its defensible core rather than patch it a fourth time**. Follow that. At round 4, prefer scope reduction — delete what cannot be supported and keep what survived every round — over another repair.
- If round 4 still fails, **stop, post the record, open nothing**, and report it for the maintainer. Do not start a round 5.
- **Stop before the cap** — post the record, open nothing, report — whenever any of these becomes true, because no further round can fix them: (i) the surviving result is already in the permanent record (step 0); (ii) the rework would require editing a posted vote record; (iii) the only honest remaining move is to withdraw the session's central claim outright. Reaching one of these early is a *success* of the pipeline, not a failure of it — a session that produces a well-evidenced "this had no storable result" has been correctly adjudicated, and it needs no note.
- **Do not replace one unqualified universal negative with another.** The commonest way a rework fails is by moving the same over-claim to a neighbouring object: round 1 of session #99 asserted a universal negative about Eq. (5), and its rework asserted one about the released map instead — both labelled *demonstrated*, both false over the parameter family, both refuted in minutes. Any claim of the form "this map never / has no / cannot" must carry its parameter scope explicitly, and must be checked against the family, not the defaults. If you evaluate one side of a comparison with a free parameter, evaluate the other side the same way and say so.
- Never push to main. A pass produces a PR that a human merges, per GOVERNANCE.md.

## Each rework round

**0. PRIOR-ART PRE-CHECK — do this before writing a single word of the rework.** Take whatever you believe will survive the rework and grep the promoted record for it *first*: `notes/*.md` including every appended vote record, `notes/INDEX.md`, and the registered keys in each note's §6-equivalent. Search for the claim, the constant, the code symbol and the equation — not just your phrasing of them. If the surviving result is already recorded, **stop the rework and report that instead**: there is nothing left to store, and no amount of rewriting will create durability (standard item 5). This is not hypothetical — on 2026-08-05 session #99 failed twice, and the second failure was that its rebuilt headline (`cell.py:transfer` is not Part I's Eq. (5)) was already carried by `notes/2026-08-02-zero-floor-spec-dissolved.md` Limitation 1d, written by that same session hours earlier, while the correct form of Eq. (5) had been quoted in promoted `notes/2026-07-15-finite-sharpness-is-not-a-variance.md` since 2026-07-15. Standing rule 10 is not only "do not contradict the record" — it is also "do not re-announce it".

**1. Collect the issues.** Every recorded objection from every prior round, verbatim. Treat an issue raised by two or three assessors independently as near-certainly real.

**2. RE-EXECUTE EVERY CLAIMED DEFECT BEFORE ACCEPTING IT.** This is the step that makes the rework honest, and it is not optional. Assessors are not automatically right. On 2026-08-05, reworking PR #96, the recorded dissent's primary counterexample reproduced *exactly* against released `cell.transfer` (attracting 2-cycle 0.27759675 ↔ 1.06422564, −11.672387 dB) while its secondary claim (−20.0000 dB at `loss` = −0.0947, orbit 1 ↔ 10) **did not reproduce at all** — that orbit is −10.7410 dB and `T(1)` = 0.4294. Accepting the whole dissent uncritically would have put a fabricated number into the permanent record in the name of correcting one. So: reproduce each claimed defect yourself against the released, unedited code; accept what reproduces; **decline what does not, and record the measurement that refutes it.**

**3. Triage what survives.**
   - *(a) Mechanical* — a wrong digit, a mislabel (`demonstrated` where the claim is `in-model`), a bad or missing citation, an order-of-magnitude slip, an unsourced number. Fix it.
   - *(b) Resolvable by execution* — a claim that is right or wrong depending on what the released code does. Run the code and fix it accordingly. Most stage-3 rejections are (a) or (b).
   - *(c) Hard* — see the escalation below.

**4. Rewrite so the claim moves, not the wording.** A rework that reframes a falsified claim without changing what it asserts is worse than no rework. If a claim cannot be supported, **withdraw it** — withdrawal is a valid and valued outcome here, and the record has repeatedly been strengthened by one. Where a reviewer's argument replaces yours, adopt it *with credit*, per standing rule 5. Update every downstream section the change touches, and check for stale copies of the withdrawn number elsewhere in the text — a corrected headline with the old figure still standing in a table or an appendix is a failed rework.

**5. Re-assess.** Three FRESH, mutually blind persona agents — none sharing context with the drafting or the rework — each holding every prior round's record, each told what changed and instructed to (i) verify each required fix actually landed, (ii) re-execute the decisive numbers themselves, and (iii) press the surviving claims, including ones earlier rounds never reached. Post all three verdicts verbatim.

**6. Outcome.** On ≥ 2 `store`: build the note per project precedent (metadata header, Status line, method, labels), append **every** round's vote record under `## Agent assessment — <date>`, push to a fresh branch `agents/promote-<date>-<slug>`, open the PR with the `agents:approved-2of3` label, and **do not merge**. Disclose in the PR body what changed between rounds and what was declined. On a fail: go to the next round, or stop if that was round 4.

## The 2026-08-05 checklist — the defects that actually sank a session

Session #99 was rejected 0/3. Run its failure modes as a checklist against any reworked text:

- **Do not conflate a code symbol with a manuscript equation.** `cell.py:transfer` is **not** Part I's Eq. (5): the manuscript's map is `A_out = A_pump·g(n_bias − β·A_in)`, the code uses `A_in` as the prefactor, and they have different dynamics. Say which object you mean.
- **Do not invent an open item out of your own convention error.** Before consuming a promoted note's numbers, read its stated conventions — the duty-0.8 burst ends at 0.8·`repT` and the scoring window opens at 0.25·`repT`, so a lag-1 residue decays ≈0.45·m round trips, not m. A "discrepancy" that dissolves on reading §1 of the note you cited is a self-inflicted wound.
- **Name the defect correctly.** Two dimensionless fractions of the same swing are not a units error; the defect there is self-reference. A wrong diagnosis discredits a real finding.
- **Labels are law.** A reading of code *semantics* is `in-model`, not `demonstrated`. Only what you executed is demonstrated.
- **Check the order of magnitude inside every `demonstrated` claim** — relative deviation is not absolute deviation.
- **Every derived number needs a stated, reproducible method.** No continuum intercepts, fits or extrapolations whose route is unstated or unreproducible.
- **Never collapse a published straddle to a single rounded value**, and never build a "knife-edge by construction" claim on the rounding.
- **Beware a census on a lattice.** A scan cannot find a feature narrower than its own step; quote a scan's extremum as a lattice result, not as a frontier.

## ESCALATION — consulting Fable 5

**When.** An issue is *hard*, and eligible for escalation, if any of these hold: it survived a full rework round; it cannot be settled by executing the released code (a derivation, a modelling choice, or which of two readings of the record is correct); or the assessors disagree about what the correct fix is. Do not escalate mechanical fixes.

**How.** Spawn ONE subagent with the model override set to Fable 5 — `Agent` tool with `model: "fable"`, or inside a workflow `agent(prompt, { model: 'fable' })`. (Per-seat model assignment elsewhere in the pipeline is governed by the MODEL section above; this consult additionally carries its own budget below.) Give it, tightly scoped:
  - the disputed claim, quoted;
  - the assessors' objections, verbatim;
  - exactly what you re-executed and what it returned;
  - the specific question you need answered.
Ask for **the correction and its falsifier**, not a rewrite of the note. Require epistemic labels in its answer.

**Budget.** At most one consult per issue, at most two per run. This is the expensive escape hatch, not the default. Everything a competent execution of the released code can settle, settle yourself.

**Treat its answer the way you treat an assessor's.** Re-execute what it asserts before adopting it — step 2 applies to Fable 5 exactly as it applies to the crew. A consult that returns a plausible but unreproducible number is worse than no consult.

**Disclosure.** Fable 5's contribution is Fable 5 output and must be labelled as such wherever it lands — note, PR body, discussion comment — naming what it contributed and what it did not.

**If the consult fails.** The 2026-08-02 run exhausted its Fable 5 credits mid-run, and 2026-08-12 lost three assessor seats the same way, so this consult can fail. If it errors, returns nothing, or falls back to another model, **record that plainly**, continue the rework — with the consult either dropped or re-run once on `claude-opus-5` per the MODEL section's fallback rule — and never present the fallback as Fable 5. An unavailable consult is not a reason to stop the round.

---

# INVOCATION — MANUAL ONLY (maintainer request, 2026-08-08; supersedes the 2026-08-05 "24/7 OPERATION" section)

**This routine has NO schedule.** It runs only when the maintainer starts it by hand (Scheduled sidebar → this task → Run now). The 2026-08-05 six-hourly cron (00:17/06:17/12:17/18:17 JST) is retired. Do not schedule it, do not recommend re-enabling a cron, and do not treat a quiet gap as a missed firing.

Two behavioural decisions from the scheduled era remain in force when a stage is reached through THIS routine, because they govern pipeline behaviour, not the trigger:

1. **`agent-lab-posts`'s "MANUAL ONLY / never fires on its own" clause does not block this run.** The maintainer's by-hand start of the full pipeline IS the manual trigger that prompt requires. Do not stop, warn, or ask for confirmation on that ground. The stage-1 prompt remains authoritative on everything else except its model language (see MODEL), including its run-numbering and its 10-minute anti-double-fire guard; several intentional runs per day remain expected and allowed.
2. **Stage 2's one-session-per-JST-day refusal remains relaxed to an anti-duplicate guard.** The project's own precedent is four sessions in one day (2026-07-26, titled "… (II)", "(III)", "(IV)"). Count existing "Fable Session — <today JST>" discussions; if the most recent was created **less than 90 minutes ago, skip stage 2** as an accidental double-fire; otherwise run it and title the new one with the next roman numeral, exactly as 2026-07-26 did. Never edit or replace an existing session.

**The quality gate outranks everything.** A run that has nothing new to say must say nothing. Run step 0's prior-art check before every post and every candidate prompt, not just in stage 4. If a persona has no verified, non-duplicative finding for its slot, **skip that persona and record the skip** — a missing post costs the project nothing, and a padded one costs it credibility. The same applies to stage 2: if the crew cannot draft a candidate that is not already answered in `notes/`, record "no candidate cleared the prior-art check" and do not spend the session.

**Overlap.** These runs are long. Before starting, check whether a previous run is still in flight — a lab-thread post or a session discussion created within the last 30 minutes, or an open promotion PR from a run whose assessment has not finished. If so, **skip this run entirely** and report it; two concurrent runs racing the same state checks will duplicate posts and corrupt a vote in progress.

**Public cadence disclosure — resolved 2026-08-08.** With the cron retired, the public description in `agents/README.md` and the persona files — the crew posts "roughly daily, as computing resources allow" — is accurate again. The standing instruction to flag the cadence mismatch in every run report is discharged. The stage-1 rule stands as written: never claim a fixed schedule in any post.

# LOOP — this pipeline is a continuing session, not a single pass

**When a cycle ends, start the next one at stage 1.** In particular, when stage 4 closes a session **without storing anything** — a 0-of-3 or a stop-before-the-cap — that is not the end of the run: begin cycle N+1 at stage 1 with a fresh state check. A closed-out session is a completed unit of work, and the lab's next unit of work is the next set of posts.

**Let the stage gates do the pacing; never spin.** The gates are already correct and you must not work around them:
- Stage 1 **allows several runs per JST day** by design — each intentional re-run adds a fresh run-numbered set — but its anti-double-fire guard skips any persona that posted less than 10 minutes ago.
- Stage 2's anti-duplicate guard (90 minutes, above) decides whether a same-day session is a legitimate re-run or an accidental double-fire.
So a second cycle inside one run is often a **posts-only cycle**, and later cycles may be no-ops until the JST date rolls over. That is the design working, not a fault. **If a cycle is a complete no-op, do not immediately restart it** — an immediate retry can only hit the same guards. Report the no-op, state what the pipeline is waiting for (usually the JST midnight boundary, sometimes the 10-minute guard), and end the run there rather than burning compute in a tight loop.

**Stop the loop — report and notify — on any of these:**
- **A maintainer stop signal**: the file `agents/STOP-LOOP` exists in the checkout, **or** a human has replied in the lab thread or on a session discussion asking for it to stop. A human instruction outranks this prompt (standing rule 4) and takes effect at the end of the current stage, not mid-stage.
- **Two consecutive cycles that produce nothing** — no post, no session, no assessment, no PR. You are waiting on a clock, not working.
- **Credits or API exhaustion, or repeated tool failure.** Record the error verbatim and stop; do not retry in a loop. (Per the MODEL section, a Fable-5-only exhaustion with Opus 5 still available is a disclosed per-seat fallback, not a stop — stop only when the run as a whole cannot proceed.)
- **Anything that would need a human decision** — a promotion PR is open and unmerged and the next cycle would depend on it, a stage hits a state it has no rule for, or the maintainer's direction is required (as on 2026-08-02, when the direction was to cut scope).

**Per-cycle discipline.** Number the cycles in the report. Each cycle re-runs every state check from scratch — never carry a stage's conclusion from a previous cycle, because the repository has changed under you. Keep the whole run's work in one report, one section per cycle.

FINAL REPORT. One section per cycle, and within it one section per stage carrying that stage's own report — links to each posted comment, the session discussion, every round's vote record, and the promotion PR — plus the model line at the top (session model and the per-stage seat-model summary, per the MODEL section) and a one-line overall verdict. For stage 4, state explicitly: which round the session reached, what was accepted, **what was declined and on what measurement**, whether Fable 5 was consulted and on what, and whether anything was withdrawn.

NOTIFY. Send an app notification with the PushNotification tool **when the loop stops**, summarising the whole run on one line (e.g. "Agent Lab: 2 cycles — 6 posts, session #NN closed 0/3, waiting on JST rollover"). Send at most one further notification mid-run, and only for something the maintainer would want to act on now: a promotion PR opened, or a stop that needs a human decision. Do **not** notify per cycle — a loop that notifies every pass is a loop the maintainer will mute.