#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Install the exported routines (Claude Code scheduled tasks) on this machine.

    python3 agents/routines/install_routines.py                # write task files, print next step
    python3 agents/routines/install_routines.py --dry-run       # show what would happen
    python3 agents/routines/install_routines.py --register      # also patch the app registry
    python3 agents/routines/install_routines.py --include-disabled

What it does without --register (the safe default):

  * writes  ~/.claude/scheduled-tasks/<id>/SKILL.md  for each routine — this is where the
    app keeps a routine's prompt, so the content is installed and reviewable;
  * substitutes {{REPO}} with this checkout and {{PLATFORM_NOTE}} with the note for this
    OS, so a Windows-authored routine reads correctly on macOS;
  * prints a paste-ready request you can hand to Claude Code to register the schedules.

Registration (the schedule, working directory and enabled flag) lives in an app-managed
registry, not in the task folder. Two ways to complete it:

  A. Ask Claude Code (recommended, fully supported): paste the block this script prints.
     Claude calls the scheduled-task tool once per routine, which is exactly how these
     were created originally. That tool takes taskId / prompt / description / schedule /
     notifyOnCompletion and nothing else, so a routine's display name and worktree flag
     are listed separately for the app's Edit form, and a disabled routine has to be
     created and then paused — the creation call has no "enabled" parameter.
  B. --register: patch the registry file directly. Only works if the app has created it
     already (i.e. you have at least one routine on this machine). QUIT Claude Code first
     — it owns that file and can overwrite the patch on exit. A timestamped backup is
     written before the patch.

Exit status is non-zero if any routine could not be fully installed, so an unattended run
does not look like it succeeded.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import glob
import json
import pathlib
import platform
import shutil
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
MANIFEST = HERE / "routines.json"
PROMPTS = HERE / "prompts"

PLATFORM_NOTES = {
    "Windows": "On Windows always set PYTHONIOENCODING=utf-8 for python.",
    "Darwin": "On macOS use `python3` (not `python`); PYTHONIOENCODING=utf-8 is unnecessary but harmless.",
    "Linux": "On Linux use `python3`; PYTHONIOENCODING=utf-8 is unnecessary but harmless.",
}
REGISTRY_ROOTS = {
    "Windows": "AppData/Roaming/Claude/claude-code-sessions",
    "Darwin": "Library/Application Support/Claude/claude-code-sessions",
    "Linux": ".config/Claude/claude-code-sessions",
}


def find_registry() -> list[pathlib.Path]:
    root = REGISTRY_ROOTS.get(platform.system())
    if not root:
        return []
    base = pathlib.Path.home() / root
    return [pathlib.Path(p) for p in glob.glob(str(base / "**/scheduled-tasks.json"), recursive=True)]


def render(body: str, repo: str, note: str) -> str:
    return body.replace("{{REPO}}", repo).replace("{{PLATFORM_NOTE}}", note)


def routine_cwd(routine: dict, repo: str) -> str:
    """A routine's working directory. Almost always this checkout, but the manifest can
    record a literal path for a routine that deliberately runs somewhere else."""
    return (routine.get("cwd") or "{{REPO}}").replace("{{REPO}}", repo)


def describe_schedule(schedule: str) -> str:
    if schedule == "manual":
        return "no schedule — manual/Run-now only"
    if schedule.startswith("cron:"):
        return f"cron {schedule[5:]} (local time)"
    return f"one-time at {schedule[5:]}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", help="path to the FableComputer checkout (default: this file's repo)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--register", action="store_true", help="also patch the app registry")
    ap.add_argument("--include-disabled", action="store_true")
    args = ap.parse_args()

    if not MANIFEST.exists():
        print(f"manifest not found: {MANIFEST}", file=sys.stderr)
        return 2
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    routines = manifest["routines"]

    repo = str(pathlib.Path(args.repo).resolve()) if args.repo else str(HERE.parents[1])
    if not (pathlib.Path(repo) / "papers").is_dir():
        print(f"! {repo} does not look like the FableComputer checkout "
              f"(no papers/ directory). Pass --repo.", file=sys.stderr)
        return 2

    system = platform.system()
    note = PLATFORM_NOTES.get(system, PLATFORM_NOTES["Linux"])
    tasks_dir = pathlib.Path.home() / ".claude" / "scheduled-tasks"

    selected = [r for r in routines if r["enabled"] or args.include_disabled]
    selected_ids = {r["id"] for r in selected}
    skipped = [r for r in routines if r["id"] not in selected_ids]

    print(f"target OS   : {system}")
    print(f"repo        : {repo}")
    print(f"tasks folder: {tasks_dir}")
    print(f"routines    : {len(selected)} to install"
          + (f", {len(skipped)} skipped (disabled)" if skipped else ""))
    print()

    installed: list[dict] = []
    failures: list[str] = []
    for r in selected:
        tid = r["id"]
        src = PROMPTS / f"{tid}.md"
        if not src.exists():
            # do NOT keep it in the set to register: the registry would point filePath at
            # a SKILL.md that was never written
            failures.append(f"{tid}: prompts/{tid}.md missing — not installed, not registered")
            print(f"  ! {tid}: prompts/{tid}.md missing — skipped", file=sys.stderr)
            continue
        body = render(src.read_text(encoding="utf-8"), repo, note)
        desc = r["description"].replace("\n", " ")
        content = f"---\nname: {tid}\ndescription: {desc}\n---\n\n{body}"
        dest = tasks_dir / tid / "SKILL.md"
        action = "would write" if args.dry_run else "wrote"
        if not args.dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8", newline="\n")
        installed.append(r)
        state = "" if r["enabled"] else ", DISABLED"
        print(f"  {action} {dest}  ({len(content)} chars, schedule: {r['schedule']}{state})")

    # ---- registration -------------------------------------------------------
    print()
    if args.register:
        regs = find_registry()
        if len(regs) != 1:
            print(f"! --register needs exactly one registry file; found {len(regs)}.")
            print("  Create one routine through the app first (or use the paste-in block below),")
            print("  then re-run with --register.")
            failures.append(f"--register did nothing: found {len(regs)} registry files, need 1")
        else:
            reg = regs[0]
            data = json.loads(reg.read_text(encoding="utf-8"))
            existing = {t["id"]: t for t in data.get("scheduledTasks", [])}
            for r in installed:
                fresh = r["id"] not in existing
                entry = existing.get(r["id"], {"id": r["id"]})
                entry["cwd"] = routine_cwd(r, repo)
                entry["enabled"] = bool(r["enabled"])
                entry["filePath"] = str(tasks_dir / r["id"] / "SKILL.md")
                entry["useWorktree"] = bool(r.get("useWorktree", False))
                if r.get("displayName"):
                    entry["displayName"] = r["displayName"]
                if fresh:
                    # the app stores createdAt as epoch milliseconds; a new entry without
                    # it can render without a date, so stamp it here rather than omit it
                    entry["createdAt"] = int(time.time() * 1000)
                entry.pop("cronExpression", None)
                entry.pop("fireAt", None)
                if r["schedule"].startswith("cron:"):
                    entry["cronExpression"] = r["schedule"][5:]
                elif r["schedule"].startswith("once:"):
                    entry["fireAt"] = r["schedule"][5:]
                existing[r["id"]] = entry
            data["scheduledTasks"] = list(existing.values())
            if args.dry_run:
                print(f"  would patch {reg} ({len(installed)} routines)")
            else:
                stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
                backup = reg.with_suffix(f".json.bak-{stamp}")
                shutil.copy2(reg, backup)
                reg.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
                print(f"  patched {reg}")
                print(f"  backup  {backup}")
                print("  Claude Code must be RESTARTED to pick this up — and if it was")
                print("  running just now, quit it and re-apply: it owns this file.")
        print()

    print("=" * 78)
    print("To register the schedules the supported way, paste this to Claude Code")
    print("with this repository open:")
    print("=" * 78)
    print()
    print("Please create these scheduled tasks on this machine. For each one, use the")
    print(f"prompt body in agents/routines/prompts/<id>.md verbatim, substituting {{{{REPO}}}} with")
    print(f"{repo} and {{{{PLATFORM_NOTE}}}} with \"{note}\"")
    print(f"and set the working directory to {repo}:")
    print()
    for r in installed:
        print(f"  - {r['id']}")
        print(f"    description: {r['description']}")
        if r["enabled"]:
            print(f"    schedule: {describe_schedule(r['schedule'])}")
        else:
            # The creation tool has no `enabled` parameter, so "create it with the cron,
            # then disable it" would leave the schedule live between the two calls and
            # depends on the second one happening. A retired routine is registered with no
            # schedule instead: the manifest still records what it used to run on.
            print("    schedule: NONE — create it with no schedule at all.")
            print(f"    (It is retired and disabled; the export records its old "
                  f"{describe_schedule(r['schedule'])}, which must not be recreated.)")
        cwd = routine_cwd(r, repo)
        if cwd != repo:
            print(f"    working directory: {cwd}  (not this checkout)")
    print()

    # The creation tool takes taskId / prompt / description / schedule / notifyOnCompletion
    # and nothing else, so these two cannot be part of the request above. Say where they
    # do get set rather than asking for something that cannot be done.
    named = [r for r in installed if r.get("displayName")]
    worktree = [r for r in installed if r.get("useWorktree")]
    if named or worktree:
        print("Two fields the creation tool cannot set — set them afterwards in the app's")
        print("per-task Edit form (same place as the model picker):")
        for r in named:
            print(f"  display name   {r['id']} -> {r['displayName']}")
        for r in worktree:
            print(f"  worktree       {r['id']} -> run in a git worktree")
        print()
    if skipped:
        print("Not requested (disabled in the export): "
              + ", ".join(r["id"] for r in skipped))
        print()
    if failures:
        print("! not everything was installed:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
