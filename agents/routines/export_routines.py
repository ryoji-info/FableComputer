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

Run from anywhere:  python3 agents/routines/export_routines.py [--check]

--check exits non-zero if the exported files differ from the live tasks, so CI (or a
pre-PR habit) can catch a routine that was edited in the app but never exported.
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
    out: list[dict] = []
    for p in registry_paths():
        try:
            out.extend(json.loads(p.read_text(encoding="utf-8")).get("scheduledTasks", []))
        except (OSError, json.JSONDecodeError) as e:
            print(f"  ! could not read {p}: {e}", file=sys.stderr)
    return out


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
        cwds = {t["cwd"] for t in tasks if t.get("cwd")}
        if not cwds:
            repo = str(pathlib.Path.cwd())
        elif len(cwds) == 1:
            repo = next(iter(cwds))
        else:
            raise SystemExit(
                "! the routines have different working directories:\n    "
                + "\n    ".join(sorted(cwds))
                + "\n  Pass --repo <path> to name the FableComputer checkout."
            )
    if not (pathlib.Path(repo) / "papers").is_dir():
        raise SystemExit(f"! {repo} is not a FableComputer checkout (no papers/). Pass --repo.")
    return repo


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if the exported files are stale (do not write)")
    ap.add_argument("--repo", help="the FableComputer checkout the routines run in "
                                   "(default: inferred from the routines' working directory)")
    args = ap.parse_args()

    tasks = load_registry()
    if not tasks:
        print("No scheduled-task registry found for this OS — nothing to export.", file=sys.stderr)
        return 2

    repo = detect_repo(tasks, args.repo)

    entries, bodies = [], {}
    for t in sorted(tasks, key=lambda x: x["id"]):
        tid = t["id"]
        skill = pathlib.Path(t.get("filePath") or (pathlib.Path.home() / ".claude/scheduled-tasks" / tid / "SKILL.md"))
        if not skill.exists():
            print(f"  ! {tid}: SKILL.md missing at {skill} — skipped", file=sys.stderr)
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
            "cwd": "{{REPO}}" if t.get("cwd") and os.path.normcase(t["cwd"]) == os.path.normcase(repo)
                   else t.get("cwd", "{{REPO}}"),
        })
        bodies[tid] = tokenize(body, repo)

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
        stale = []
        if not MANIFEST.exists():
            stale.append("routines.json missing")
        else:
            live = json.loads(MANIFEST.read_text(encoding="utf-8"))
            if live.get("routines") != entries:
                stale.append("routines.json differs from the live registry")
        for tid, body in bodies.items():
            f = PROMPTS / f"{tid}.md"
            if not f.exists():
                stale.append(f"prompts/{tid}.md missing")
            elif f.read_text(encoding="utf-8") != body:
                stale.append(f"prompts/{tid}.md differs from the live SKILL.md")
        for f in sorted(PROMPTS.glob("*.md")):
            if f.stem not in bodies:
                stale.append(f"prompts/{f.name} has no live routine (deleted in the app?)")
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
    for f in sorted(PROMPTS.glob("*.md")):          # drop prompts whose routine is gone
        if f.stem not in bodies:
            f.unlink()
            print(f"  removed stale prompts/{f.name}")

    print(f"exported {len(entries)} routines to {HERE}")
    for e in entries:
        flag = "" if e["enabled"] else "  (disabled)"
        print(f"  {e['id']:26s} {e['schedule']:22s}{flag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
