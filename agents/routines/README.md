<img src="../../branding/boogie-sorbet-monogram.svg" alt="" width="72" align="right">

# Routines as code

The Agent Lab's pipelines are run by **Claude Code routines** (scheduled tasks) on the
maintainer's machine — see [`agents/README.md`](../README.md), "Operations". A routine
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

## Exporting (on the machine that has the routines)

```bash
python3 agents/routines/export_routines.py
```

It reads the app registry and each `SKILL.md`, tokenizes, and rewrites `routines.json`
and `prompts/`. Commit the result.

**The export is additive.** A routine that is already in `routines.json` but is not
installed on the machine you are exporting from is *carried forward untouched*, and the
run says so. That is what makes exporting from a second machine safe: the Mac has never
installed the retired `agent-lab-daily-posts`, and an export from there must not silently
delete it. Likewise, a routine whose `SKILL.md` cannot be read keeps its committed copy
rather than losing it, and the run exits non-zero so the gap is visible.

When you genuinely did delete a routine in the app and want it gone from the export:

```bash
python3 agents/routines/export_routines.py --prune
```

Routines belonging to *other* checkouts are ignored, so `--repo` cannot accidentally drag
another project's routines — or their absolute paths — into this repository. A staleness
check is available:

```bash
python3 agents/routines/export_routines.py --check   # exit 1 if the export is behind
```

Run that after editing a routine in the app — **it cannot run in CI**, because CI has no
app registry to compare against. Treat it as a local habit, not a gate. What CI *does*
check is that whatever the export produced is portable and installable:
[`tests/test_routines_export.py`](../../tests/test_routines_export.py) installs the
manifest into a sandbox for macOS, Linux and Windows in turn.

## Importing on a Mac

Prerequisites: this repository cloned, Claude Code installed, `python3` available, and a
**GitHub token reachable from `git credential fill`** — the routines get their token that
way rather than from `gh`, so on macOS store a PAT once with the `osxkeychain` helper:

```bash
git config --global credential.helper osxkeychain
printf 'protocol=https\nhost=github.com\nusername=<you>\npassword=<token>\n\n' | git credential approve
printf 'protocol=https\nhost=github.com\n' | git credential fill   # should print password=…
```

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
these routines were created in the first place, and the app picks them up immediately. The
block states each routine's **enabled flag explicitly**, including "must not fire" for a
disabled one — silence there would read as "enabled", which for a routine carrying a
retired cron expression would put that schedule back into service.

**B. `--register`.** Patches the registry file directly, after writing a timestamped
backup. For a routine that does not exist yet it writes the full entry the app expects —
schedule, working directory, enabled flag, display name, worktree flag, and a `createdAt`
stamp — so the routine appears named and dated rather than blank. It needs the registry to
exist already (i.e. at least one routine created on that machine). **Quit Claude Code
before running it**: the app owns that file and can overwrite the patch when it exits.
Use it when you want no interactive step; prefer A otherwise.

## Things worth knowing

- **Definition travels; history does not.** The export carries what a routine *is* — its
  prompt, schedule, display name (including the `1.` / `2.` / `3.` ordering prefixes),
  enabled flag, worktree flag and working directory. It deliberately leaves behind the
  app's runtime record for this machine: `createdAt`, `lastRunAt`, `lastScheduledFor`,
  `notifySessionId`. So a freshly installed routine has no run history on the new machine,
  which is correct — it has not run there.
- **Routines only run while Claude Code is open.** A due routine that was missed fires on
  next launch.
- **The per-routine model picker is app state and is not exported.** These routines are
  written to run on Fable 5 and to *self-report* the model they actually ran on, so a
  wrong picker shows up in the run report rather than silently. Set it per routine on the
  new machine if you care which model runs them.
- **Tool approvals are per-machine.** The first run of each routine on the Mac will prompt
  for the tools it needs (git, python, the GitHub API). Approving once sticks for that
  routine, so a "Run now" on each is a good way to pre-approve before relying on them.
- **`agent-lab-daily-posts` is exported disabled.** It is the retired cron version of the
  posts routine, superseded by the manual `agent-lab-posts`; `install_routines.py` skips
  disabled routines unless you pass `--include-disabled`. Since 2026-07-27 nothing in the
  lab runs on a schedule — every run is started by hand, at roughly daily cadence as
  compute allows.
- **The prompts are the contract.** Each one defers to `agents/scripts/*.py` as the
  specification for its pipeline and starts with a duplicate/state check, so running a
  routine twice, or on a second machine, does not double-post. That is what makes a
  two-machine setup safe.
- **Both machines share one GitHub repository.** Nothing prevents you from running the
  same routine on the Mac and on Windows; the state checks are the guard, and the record
  (Discussions, PRs, `notes/`) is the single source of truth.
