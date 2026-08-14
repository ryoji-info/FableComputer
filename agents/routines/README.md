<img src="../../branding/boogie-sorbet-monogram.svg" alt="" width="72" align="right">

# Routines as code

The Agent Lab's pipelines are run by **Claude Code routines** (scheduled tasks) on the
maintainer's machines — the Windows box, and since 2026-08 the Mac, imported from this
very directory — see [`agents/README.md`](../README.md), "Operations". A routine
lives in the app as a folder containing a `SKILL.md` prompt, plus an entry in an
app-managed registry holding its schedule, working directory and enabled flag.

That is machine-local state, so it does not travel with a `git clone`. **This directory
is the portable form**: the prompts as reviewable files, the schedules as a manifest, and
two scripts to move them between machines.

> The [`.github/workflows/agents-*.yml`](../../.github/workflows) files are a *different*
> path — the original API-key implementations, kept as manually dispatchable fallbacks.
> Those are already code and already portable; nothing here affects them.

## What is in here

| file | what it is |
|---|---|
| `routines.json` | manifest: one entry per routine — id, display name, description, schedule, enabled, worktree flag, working directory |
| `prompts/<id>.md` | the routine's prompt body, verbatim, with machine-specific strings tokenized |
| `export_routines.py` | regenerate the two above from this machine's live routines |
| `install_routines.py` | materialize the routines on another machine, any OS |

Two placeholders keep the prompts OS-neutral:

| token | becomes |
|---|---|
| `{{REPO}}` | the absolute path of the `FableComputer` checkout on the target machine |
| `{{PLATFORM_NOTE}}` | `On Windows always set PYTHONIOENCODING=utf-8 for python.` / `On macOS use python3 …` / the Linux equivalent |

## Exporting (from the machine that last edited a routine)

Since 2026-08 both machines carry the lab — the Windows box and the Mac — so run the
export on whichever machine the routine was last edited on in the app; `exported_from`
in the manifest records which one produced the current files. The interpreter is
`python` on Windows, `python3` on the Mac.

```bash
python agents/routines/export_routines.py
```

It reads the app registry and each `SKILL.md`, tokenizes, and rewrites `routines.json`
and `prompts/`. Commit the result.

**The export is additive.** A routine that is already in `routines.json` but is not
installed on the machine you are exporting from is *carried forward untouched*, and the
run says so. That is what makes exporting from a second machine safe: a routine you chose
not to install on the Mac must not be deleted from the record just because you exported
from there. Likewise, a routine whose `SKILL.md` cannot be read keeps its committed copy
rather than losing it, and the run exits non-zero so the gap is visible.

When you genuinely did delete a routine in the app and want it gone from the export:

```bash
python agents/routines/export_routines.py --prune
```

Routines belonging to *other* checkouts are ignored, so `--repo` cannot accidentally drag
another project's routines — or their absolute paths — into this repository. A staleness
check is available:

```bash
python agents/routines/export_routines.py --check   # exit 1 if the export is behind
```

Run that after editing a routine in the app — **it cannot run in CI**, because CI has no
app registry to compare against. Treat it as a local habit, not a gate. What CI *does*
check is that whatever the export produced is portable and installable:
[`tests/test_routines_export.py`](../../tests/test_routines_export.py) installs the
manifest into a sandbox for macOS, Linux and Windows in turn.

## Importing on a second machine

This procedure is not hypothetical: it brought the lab up on the maintainer's Mac in
2026-08, and both machines now carry all five routines. The steps below are written for
macOS; substitute the credential helper and paths for Linux.

Prerequisites: this repository cloned, Claude Code installed, **Python ≥ 3.10** (both
scripts write files with an explicit newline mode, which is 3.10+), and a **GitHub token
reachable from `git credential fill`** — the routines get their token that way rather than
from `gh`, so on macOS store a PAT once with the `osxkeychain` helper:

```bash
git config --global credential.helper osxkeychain
printf 'protocol=https\nhost=github.com\nusername=<you>\npassword=<token>\n\n' | git credential approve
printf 'protocol=https\nhost=github.com\n' | git credential fill   # should print password=…
```

The routines use the token inline — `TOKEN=$(printf … | git credential fill …)` per
command — and never write it to a file; a 2026-08-13 violation of that rule by one
interrupted seat was remediated and disclosed in discussion #117's round-2 record. Keep
it that way on any machine you import to.

Then install:

```bash
python3 agents/routines/install_routines.py --dry-run   # look first
python3 agents/routines/install_routines.py
```

This writes `~/.claude/scheduled-tasks/<id>/SKILL.md` for each routine with the tokens
substituted for macOS, and prints a **paste-ready request**. Registration — the schedule,
working directory and enabled flag — lives in the app registry, and there are two ways to
finish it:

**A. Ask Claude Code (recommended).** Paste the printed block into Claude Code with this
repository open. It calls the scheduled-task tool once per routine, which is exactly how
these routines were created in the first place, and the app picks them up immediately.

"With this repository open" is not a nicety: the creation tool has no working-directory
parameter and records the *creating session's* cwd, so a paste from a session rooted
anywhere else silently registers every routine with the wrong working directory — and
the stage prompts resolve `agents/…`, `notes/`, `papers/` relative to it (only the
full-run prompt defends itself, resolving paths against `{{REPO}}`). This bit during the
2026-08 Mac import. If it happens, fix the cwd afterwards with `--register` (app quit
first), which rewrites it directly.

That tool accepts a task id, prompt, description, schedule and notification preference —
and nothing else. So two things the block *cannot* ask it to do, and says so instead:

- **A disabled routine has to be created and then paused**, because there is no `enabled`
  parameter on creation. The block spells that out for any disabled routine in the
  manifest; silence there would read as "enabled" and put a retired schedule back into
  service. (The current export carries none — the retired cron routine was deleted
  outright on 2026-07-31 rather than kept disabled.)
- **Display name and worktree flag are set in the app's per-task Edit form**, the same
  place as the model picker. The block lists the values to type in. `--register` sets both
  directly, which is the one respect in which path B is more complete than path A.

**B. `--register`.** Patches the registry file directly, after writing a timestamped
backup. For a routine that does not exist yet it writes the full entry the app expects —
schedule, working directory, enabled flag, display name, worktree flag, and a `createdAt`
stamp — so the routine appears named and dated rather than blank. It needs the registry to
exist already (i.e. at least one routine created on that machine).

**Quit Claude Code before running it.** The app owns that file and rewrites it in full
from its own in-memory state whenever a task changes — not only on exit. This is observed,
not theoretical: on 2026-07-31 a display name written directly into the registry was
discarded a few minutes later when the app processed an unrelated task deletion. Anything
you patch underneath a running app should be treated as provisional until you have
confirmed it in the sidebar. Prefer path A, and set display names in the Edit form.

## Things worth knowing

- **Definition travels; history does not.** The export carries what a routine *is* — its
  prompt, schedule, display name (including the `1.`–`5.` ordering prefixes),
  enabled flag, worktree flag and working directory. It deliberately leaves behind the
  app's runtime record for this machine: `createdAt`, `lastRunAt`, `lastScheduledFor`,
  `notifySessionId`. So a freshly installed routine has no run history on the new machine,
  which is correct — it has not run there.
- **Run-completion notifications do not transfer.** The app records the notification
  subscription as a *session* id, which means nothing on another machine. A freshly
  created routine notifies whichever session created it (the tool's default); pass
  `notifyOnCompletion: false` when registering if you would rather it stayed quiet.
- **The prompts assert nothing about the machine they run on.** They did once —
  `agent-lab-posts` used to state that the `gh` CLI was not installed, which is true on the
  Windows box and would be false on a Mac that has it. That sentence now reads "do not rely
  on the `gh` CLI", which is an instruction rather than a claim, and holds anywhere. If you
  add a machine-specific fact to a routine, either make it an instruction like that one or
  give it a placeholder; the two existing tokens are the only ones the installer resolves.
- **Routines only run while Claude Code is open.** A due routine that was missed fires on
  next launch.
- **Per-seat models travel with the export; the app's model picker does not.** Since
  2026-08-13 the model assignment lives inside the prompts — the MODEL section of
  [`prompts/agent-lab-full-run.md`](prompts/agent-lab-full-run.md) is the authoritative
  policy text: session execution, pre-publication check seats and reworks on
  `claude-fable-5`; post drafters, candidate drafters, vote seats and
  assessors/re-assessors on `claude-opus-5`; a Fable seat that errors or exhausts falls
  back to `claude-opus-5`, disclosed, never relabelled. That text is exported and
  installed like any prompt line, so the policy arrives on a second machine intact. What
  is *not* exported is the app's per-routine model picker, which sets only the *session*
  model — `claude-fable-5` under the policy; set it per routine on the new machine
  (per-task Edit form). The honesty guarantee is unchanged and extended: every seat
  self-reports the model that actually ran it, in the run report and per-seat in
  everything published, so a wrong picker shows up in the record rather than silently.
- **Tool approvals are per-machine.** The first run of each routine on a new machine will
  prompt for the tools it needs (git, python, the GitHub API). Approving once sticks for
  that routine, so a "Run now" on each is a good way to pre-approve before relying on
  them.
- **Nothing runs on a schedule.** All five routines are manual/Run-now — the four stage
  pipelines plus `agent-lab-full-run`, which chains them (posts → fable session → assess
  → rework, looping). The lab has had no cron since 2026-08-08: `agent-lab-daily-posts`,
  the retired `0 7 * * *` posts pipeline, was deleted on 2026-07-31, and the full run's
  brief six-hourly schedule (2026-08-05) was retired on 2026-08-08. Every run is started
  by hand, at roughly daily cadence as compute allows. If you ever do
  disable a routine rather than delete it, `install_routines.py` skips disabled routines
  unless you pass `--include-disabled`, and the registration block asks for them with no
  schedule at all.
- **The prompts are the contract — and on models, the full run's MODEL section outranks
  them.** Each stage prompt defers to `agents/scripts/*.py` as the specification for its
  pipeline and starts with a duplicate/state check, so running a routine twice, or on a
  second machine, does not double-post. That is what makes a two-machine setup safe. One
  carve-out since 2026-08-13: the MODEL section in
  [`prompts/agent-lab-full-run.md`](prompts/agent-lab-full-run.md) supersedes every model
  line in the stage prompts and in the scripts' templates (the assessor briefing in
  `agent_fable_assess.py` still hardcodes "produced by Claude Fable 5"; a run briefs
  assessors with the actual executing model instead).
- **Both machines share one GitHub repository.** Nothing prevents you from running the
  same routine on the Mac and on Windows; the state checks are the guard, and the record
  (Discussions, PRs, `notes/`) is the single source of truth.
