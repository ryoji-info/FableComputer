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
     were created originally.
  B. --register: patch the registry file directly. Only works if the app has created it
     already (i.e. you have at least one routine on this machine). A timestamped backup
     is written first, and the app must be restarted to pick up the change.
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

    for r in selected:
        tid = r["id"]
        src = PROMPTS / f"{tid}.md"
        if not src.exists():
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
        print(f"  {action} {dest}  ({len(content)} chars, schedule: {r['schedule']})")

    # ---- registration -------------------------------------------------------
    print()
    if args.register:
        regs = find_registry()
        if len(regs) != 1:
            print(f"! --register needs exactly one registry file; found {len(regs)}.")
            print("  Create one routine through the app first (or use the paste-in block below),")
            print("  then re-run with --register.")
        else:
            reg = regs[0]
            data = json.loads(reg.read_text(encoding="utf-8"))
            existing = {t["id"]: t for t in data.get("scheduledTasks", [])}
            for r in selected:
                fresh = r["id"] not in existing
                entry = existing.get(r["id"], {"id": r["id"]})
                entry["cwd"] = repo
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
                print(f"  would patch {reg} ({len(selected)} routines)")
            else:
                stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
                backup = reg.with_suffix(f".json.bak-{stamp}")
                shutil.copy2(reg, backup)
                reg.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
                print(f"  patched {reg}")
                print(f"  backup  {backup}")
                print("  RESTART Claude Code for the app to pick this up.")
        print()

    print("=" * 78)
    print("To register the schedules the supported way, paste this to Claude Code")
    print("with this repository open:")
    print("=" * 78)
    print()
    print("Please register these scheduled tasks on this machine. For each one, use the")
    print(f"prompt body in agents/routines/prompts/<id>.md verbatim, substituting {{{{REPO}}}} with")
    print(f"{repo} and {{{{PLATFORM_NOTE}}}} with \"{note}\"")
    print(f"and set the working directory to {repo}:")
    print()
    for r in selected:
        sched = ("no schedule — manual/Run-now only" if r["schedule"] == "manual"
                 else f"cron {r['schedule'][5:]} (local time)" if r["schedule"].startswith("cron:")
                 else f"one-time at {r['schedule'][5:]}")
        print(f"  - {r['id']}: {sched}")
        if r.get("displayName"):
            print(f"    display name: {r['displayName']}")
        print(f"    description: {r['description']}")
        if r.get("useWorktree"):
            print(f"    run in a git worktree: yes")
    print()
    if skipped:
        print("Not requested (disabled in the export): "
              + ", ".join(r["id"] for r in skipped))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
