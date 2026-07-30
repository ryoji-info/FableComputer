#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Export this machine's Claude Code scheduled tasks ("routines") to versioned code.

Reads the live tasks — the app's registry plus each task's SKILL.md — and writes a
portable, reviewable representation into this directory:

    routines.json      manifest: id, description, display name, schedule, enabled,
                       worktree flag, working directory
    prompts/<id>.md    the prompt body, with machine-specific strings tokenized

Only a routine's *definition* is exported. Runtime state the app records — createdAt,
lastRunAt, lastScheduledFor, notifySessionId — is deliberately left behind: it describes
this machine's history, not the routine.

Machine-specific strings become placeholders so the same files import cleanly on another
OS.  Tokens used:

    {{REPO}}            absolute path to the FableComputer checkout
    {{PLATFORM_NOTE}}   the one-sentence interpreter/encoding note

Run from anywhere:  python3 agents/routines/export_routines.py [--check] [--prune]

**The export is additive by default.** A routine that is already in routines.json but is
not installed on this machine is carried forward untouched, not deleted — otherwise
exporting from a second machine would quietly destroy every routine that machine happens
not to have. Pass --prune when you really did delete a routine in the app and want it gone.

--check exits non-zero if the exported files differ from the live tasks, so a pre-PR habit
can catch a routine that was edited in the app but never exported. It needs the app's
registry, so it cannot run in CI; the portability of what it produces is covered by
tests/test_routines_export.py instead.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import pathlib
import platform
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
PROMPTS = HERE / "prompts"
MANIFEST = HERE / "routines.json"

# The one-sentence platform note, per OS. Export replaces whichever variant it finds
# with {{PLATFORM_NOTE}}; install substitutes the variant for the target OS.
PLATFORM_NOTES = {
    "Windows": "On Windows always set PYTHONIOENCODING=utf-8 for python.",
    "Darwin": "On macOS use `python3` (not `python`); PYTHONIOENCODING=utf-8 is unnecessary but harmless.",
    "Linux": "On Linux use `python3`; PYTHONIOENCODING=utf-8 is unnecessary but harmless.",
}
# Older phrasings that mean the same thing and should also tokenize.
NOTE_VARIANTS = [
    "On Windows always set PYTHONIOENCODING=utf-8 for python.",
    "Windows: always PYTHONIOENCODING=utf-8 for python.",
    *PLATFORM_NOTES.values(),
]


def _norm(path: str) -> str:
    """Compare paths by meaning, not by spelling — slash flavour and case included."""
    return os.path.normcase(os.path.normpath(path))


def registry_paths() -> list[pathlib.Path]:
    """Where the app keeps its scheduled-task registry, per OS."""
    home = pathlib.Path.home()
    roots = {
        "Windows": home / "AppData/Roaming/Claude/claude-code-sessions",
        "Darwin": home / "Library/Application Support/Claude/claude-code-sessions",
        "Linux": home / ".config/Claude/claude-code-sessions",
    }
    root = roots.get(platform.system())
    if root is None or not root.exists():
        return []
    return [pathlib.Path(p) for p in glob.glob(str(root / "**/scheduled-tasks.json"), recursive=True)]


def load_registry() -> list[dict]:
    """Every registered task, one entry per id.

    There can be more than one registry file; the same routine appearing in two of them
    must collapse to one entry, or the manifest would list it twice while only one prompt
    body survives the write.
    """
    by_id: dict[str, dict] = {}
    for p in registry_paths():
        try:
            tasks = json.loads(p.read_text(encoding="utf-8")).get("scheduledTasks", [])
        except (OSError, json.JSONDecodeError) as e:
            print(f"  ! could not read {p}: {e}", file=sys.stderr)
            continue
        for t in tasks:
            tid = t.get("id")
            if not tid:
                continue
            if tid in by_id and by_id[tid] != t:
                print(f"  ! {tid} is registered more than once; taking the copy in {p}",
                      file=sys.stderr)
            by_id[tid] = t
    return list(by_id.values())


def tokenize(body: str, repo: str) -> str:
    """Replace machine-specific strings with placeholders."""
    for variant in NOTE_VARIANTS:
        body = body.replace(variant, "{{PLATFORM_NOTE}}")
    # the repo path, in whatever slash flavour it was written
    for form in {repo, repo.replace("\\", "/"), repo.replace("/", "\\")}:
        body = body.replace(form, "{{REPO}}")
    return body


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter, body). Frontmatter is dropped on export: the manifest owns
    name/description, and install regenerates it."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[: end + 4], text[end + 4 :].lstrip("\n")
    return "", text


def detect_repo(tasks: list[dict], override: str | None) -> str:
    """The checkout the routines run in — the string that becomes {{REPO}}.

    Deliberately does NOT fall back to a common ancestor of divergent working
    directories: the common ancestor of two different checkouts is their *parent*, and
    tokenizing a parent path would rewrite every prompt to a {{REPO}} that resolves one
    directory too high. Refuse and ask instead.
    """
    if override:
        repo = str(pathlib.Path(override).resolve())
    else:
        # group by meaning, so the same directory spelled two ways is still one directory
        spellings: dict[str, str] = {}
        for t in tasks:
            if t.get("cwd"):
                spellings.setdefault(_norm(t["cwd"]), t["cwd"])
        if not spellings:
            repo = str(pathlib.Path.cwd())
        elif len(spellings) == 1:
            repo = next(iter(spellings.values()))
        else:
            raise SystemExit(
                "! the routines have different working directories:\n    "
                + "\n    ".join(sorted(spellings.values()))
                + "\n  Pass --repo <path> to name the FableComputer checkout."
            )
    if not (pathlib.Path(repo) / "papers").is_dir():
        raise SystemExit(f"! {repo} is not a FableComputer checkout (no papers/). Pass --repo.")
    return repo


def partition_by_repo(tasks: list[dict], repo: str) -> tuple[list[dict], list[dict]]:
    """Split into (this checkout's routines, other projects' routines).

    Without this, an export run with --repo would commit unrelated projects' routines —
    and their untokenized absolute paths — into this repository.
    """
    mine, foreign = [], []
    for t in tasks:
        cwd = t.get("cwd")
        (mine if not cwd or _norm(cwd) == _norm(repo) else foreign).append(t)
    return mine, foreign


def build(tasks: list[dict], repo: str, prev_by_id: dict[str, dict], prune: bool):
    """Return (entries, bodies, problems) for the manifest and the prompt files."""
    entries: list[dict] = []
    bodies: dict[str, str] = {}
    problems: list[str] = []

    def keep_exported(tid: str, why: str) -> bool:
        """Reuse what is already committed rather than losing it."""
        f = PROMPTS / f"{tid}.md"
        if tid in prev_by_id and f.exists():
            entries.append(prev_by_id[tid])
            bodies[tid] = f.read_text(encoding="utf-8")
            print(f"  = {tid}: {why} — kept the exported copy")
            return True
        return False

    for t in sorted(tasks, key=lambda x: x["id"]):
        tid = t["id"]
        skill = pathlib.Path(t.get("filePath")
                             or (pathlib.Path.home() / ".claude/scheduled-tasks" / tid / "SKILL.md"))
        if not skill.exists():
            problems.append(f"{tid}: SKILL.md missing at {skill}")
            if not keep_exported(tid, "SKILL.md unreadable"):
                print(f"  ! {tid}: SKILL.md missing and nothing exported yet — skipped",
                      file=sys.stderr)
            continue
        fm, body = split_frontmatter(skill.read_text(encoding="utf-8"))
        desc = ""
        m = re.search(r"^description:\s*(.+)$", fm, re.M)
        if m:
            desc = m.group(1).strip()
        entries.append({
            "id": tid,
            # how the app labels the routine in its list; the numeric prefixes the
            # maintainer uses for ordering live in here, so it has to survive the trip
            "displayName": t.get("displayName") or "",
            "description": desc,
            # exactly one of these is meaningful; "manual" means run-now only
            "schedule": ("cron:" + t["cronExpression"]) if t.get("cronExpression")
                        else ("once:" + t["fireAt"]) if t.get("fireAt") else "manual",
            "enabled": bool(t.get("enabled", True)),
            "useWorktree": bool(t.get("useWorktree", False)),
            "cwd": "{{REPO}}" if t.get("cwd") and _norm(t["cwd"]) == _norm(repo)
                   else t.get("cwd", "{{REPO}}"),
        })
        bodies[tid] = tokenize(body, repo)

    # Routines this machine does not have. Carrying them forward is what makes exporting
    # from a second machine safe: the Mac has never installed the retired cron routine,
    # and an export from there must not delete it.
    handled = {e["id"] for e in entries}
    for tid in sorted(set(prev_by_id) - handled):
        if prune:
            print(f"  - {tid}: --prune — dropped from the export")
        elif not keep_exported(tid, "not registered on this machine"):
            problems.append(f"{tid}: in routines.json but prompts/{tid}.md is missing")

    entries.sort(key=lambda e: e["id"])
    return entries, bodies, problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if the exported files are stale (do not write)")
    ap.add_argument("--repo", help="the FableComputer checkout the routines run in "
                                   "(default: inferred from the routines' working directory)")
    ap.add_argument("--prune", action="store_true",
                    help="drop exported routines this machine's app does not have "
                         "(default: carry them forward untouched)")
    args = ap.parse_args()

    previous = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    prev_by_id = {r["id"]: r for r in previous.get("routines", [])}

    tasks = load_registry()
    if not tasks:
        print("No scheduled-task registry found for this OS — nothing to export.", file=sys.stderr)
        return 2

    repo = detect_repo(tasks, args.repo)
    tasks, foreign = partition_by_repo(tasks, repo)
    for t in sorted(foreign, key=lambda x: x["id"]):
        print(f"  · {t['id']}: runs in {t.get('cwd')}, not this checkout — ignored")
    if not tasks:
        print(f"! no routine runs in {repo} — nothing to export.", file=sys.stderr)
        return 2

    entries, bodies, problems = build(tasks, repo, prev_by_id, args.prune)

    manifest = {
        "note": ("Exported Claude Code routines (scheduled tasks) for the Fable Computer "
                 "Agent Lab. Import with install_routines.py; see README.md. Placeholders: "
                 "{{REPO}} = checkout path, {{PLATFORM_NOTE}} = interpreter/encoding note. "
                 "Definition only — the app's runtime state (createdAt, lastRunAt, "
                 "lastScheduledFor, notifySessionId) is intentionally not exported."),
        "exported_from": platform.system(),
        "routines": entries,
    }

    if args.check:
        stale = list(problems)
        if not MANIFEST.exists():
            stale.append("routines.json missing")
        else:
            # compare the whole manifest, not just the routines array — but ignore
            # exported_from, which legitimately differs by which OS ran the export
            drop = lambda d: {k: v for k, v in d.items() if k != "exported_from"}
            if drop(previous) != drop(manifest):
                stale.append("routines.json differs from the live registry")
        for tid, body in bodies.items():
            f = PROMPTS / f"{tid}.md"
            if not f.exists():
                stale.append(f"prompts/{tid}.md missing")
            elif f.read_text(encoding="utf-8") != body:
                stale.append(f"prompts/{tid}.md differs from the live SKILL.md")
        if stale:
            print("STALE export:")
            for s in stale:
                print("  -", s)
            print("\nRe-run without --check to refresh, then commit.")
            return 1
        print(f"export is current: {len(entries)} routines")
        return 0

    PROMPTS.mkdir(parents=True, exist_ok=True)
    # newline="\n" on every write: the export must be byte-identical whichever OS ran it
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="\n")
    for tid, body in bodies.items():
        (PROMPTS / f"{tid}.md").write_text(body, encoding="utf-8", newline="\n")
    # Only ever remove a prompt whose routine we just dropped on purpose. Never glob the
    # directory: a hand-written file in prompts/ is not ours to delete.
    for tid in sorted(set(prev_by_id) - {e["id"] for e in entries}):
        f = PROMPTS / f"{tid}.md"
        if f.exists():
            f.unlink()
            print(f"  removed prompts/{tid}.md (no longer an exported routine)")

    print(f"exported {len(entries)} routines to {HERE}")
    for e in entries:
        flag = "" if e["enabled"] else "  (disabled)"
        print(f"  {e['id']:26s} {e['schedule']:22s}{flag}")
    if problems:
        print("\n! the export is incomplete:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
