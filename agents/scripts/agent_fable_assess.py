# -*- coding: utf-8 -*-
"""Assess a Fable reply stored in notes/drafts/: the three agents each review
the note independently and vote 2-of-3 on whether it is suitable for the
permanent record.

- >= 2 'store'  -> a PR is opened that promotes the note from notes/drafts/ to
                   notes/ with the recorded votes appended (a human merges,
                   per GOVERNANCE.md).
- <  2 'store'  -> an issue is opened with the verdicts, recommending rework
                   or removal. Nothing is changed automatically.

Env: ANTHROPIC_API_KEY, GH_TOKEN, GITHUB_REPOSITORY, MODEL (optional),
     NOTE_PATH (optional -- defaults to the newest .md in notes/drafts/).
Runs inside a checkout of the repository.
"""
import base64
import datetime
import glob
import json
import os
import re

import requests

API = "https://api.anthropic.com/v1/messages"
REST = "https://api.github.com"
OWNER, REPO = os.environ["GITHUB_REPOSITORY"].split("/")
MODEL = os.environ.get("MODEL", "claude-sonnet-5")
NOTE_PATH = os.environ.get("NOTE_PATH", "").strip()
PERSONAS = ["fabric", "kinetic", "quanta"]
EMOJI = {"fabric": "🧵", "kinetic": "🌊", "quanta": "⚛️"}

gh = {"Authorization": f"Bearer {os.environ['GH_TOKEN']}",
      "Accept": "application/vnd.github+json"}

STANDARD = """Assessment standard for storing a note in the project's
permanent record (notes/ -- see notes/README.md):
1. Substance: the note delivers a concrete, checkable result -- a derivation,
   calibration, refutation, or decision -- not a survey or restatement.
2. Epistemic labels: claims are marked demonstrated / in-model / open,
   correctly and consistently applied.
3. Citations and numbers: precise, and consistent with the repository's model
   chains where they overlap (reference outputs are provided below).
4. Honesty: limitations and uncertainty are stated; nothing is oversold. A
   negative or corrective result stated honestly is highly storable.
5. Durability: someone doing WP1-WP5 work would consult this. It changes what
   the project believes or does next.
Vote 'store' only if all five hold. Vote 'reject' otherwise. You are choosing
what enters the permanent record; be the project's skeptic, not its fan."""


def read(path, limit=8000):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()[:limit]
    except OSError:
        return "(unavailable)"


def claude(system, user, max_tokens=4000):
    r = requests.post(API, headers={
        "x-api-key": os.environ["ANTHROPIC_API_KEY"],
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }, json={"model": MODEL, "max_tokens": max_tokens, "system": system,
             "messages": [{"role": "user", "content": user}]}, timeout=600)
    r.raise_for_status()
    data = r.json()
    text = "".join(b.get("text", "") for b in data["content"]
                   if b.get("type") == "text").strip()
    if not text:
        raise RuntimeError(f"empty completion (stop_reason={data.get('stop_reason')})")
    return text


def parse_json(raw):
    return json.loads(raw[raw.find("{"): raw.rfind("}") + 1])


def find_note():
    if NOTE_PATH:
        if not os.path.isfile(NOTE_PATH):
            raise SystemExit(f"NOTE_PATH not found: {NOTE_PATH}")
        return NOTE_PATH
    drafts = [p for p in glob.glob("notes/drafts/*.md")
              if os.path.basename(p).lower() != "readme.md"]
    if not drafts:
        raise SystemExit("No notes in notes/drafts/ to assess.")
    return max(drafts, key=os.path.getmtime).replace("\\", "/")


def main():
    today = datetime.date.today()
    path = find_note()
    note = read(path, 60000)
    print(f"assessing: {path} ({len(note)} chars)")

    context = f"""A reply produced by Claude Fable 5 has been placed in the
repository's draft notes at `{path}`. Assess whether it is suitable for the
project's permanent record.

{STANDARD}

THE NOTE TO ASSESS ({path}):

{note}

Reference -- current model-chain outputs for consistency checks:
{read('fable-model-chain/results.json', 2500)}
{read('fable-model-quantum/results.json', 2500)}

Return ONLY JSON:
{{"vote": "store|reject", "reasons": "<3-6 sentences>",
  "top_issues": ["<specific problems, if any>"]}}"""

    votes = {}
    for p in PERSONAS:
        persona = read(f"agents/personas/{p}.md")
        votes[p] = parse_json(claude(persona, context))
        print(f"{p}: {votes[p].get('vote')}")

    stores = sum(1 for v in votes.values() if v.get("vote") == "store")
    vote_md = "\n".join(
        f"- {EMOJI[p]} **{p.capitalize()}** — **{str(votes[p].get('vote', '?')).upper()}**: "
        f"{votes[p].get('reasons', '')}"
        + ("".join(f"\n  - {i}" for i in votes[p].get("top_issues", [])))
        for p in PERSONAS)
    basename = os.path.basename(path)

    if stores < 2:
        r = requests.post(f"{REST}/repos/{OWNER}/{REPO}/issues", headers=gh, json={
            "title": f"Agent assessment: {basename} not suitable to store ({stores}/3)",
            "body": (f"The agent crew assessed [`{path}`](https://github.com/{OWNER}/{REPO}/blob/main/{path}) "
                     f"and fewer than 2 of 3 voted to store it.\n\n{vote_md}\n\n"
                     f"Recommended: rework the note to address the issues above, or "
                     f"remove it from `notes/drafts/`. Nothing was changed automatically.\n\n"
                     f"*Assessment per [agents/README.md](https://github.com/{OWNER}/{REPO}/blob/main/agents/README.md); "
                     f"the humans decide, per GOVERNANCE.md.*"),
        })
        r.raise_for_status()
        print(f"rejected {stores}/3 — issue: {r.json()['html_url']}")
        return

    # ---- accepted: PR that promotes drafts/ -> notes/ -------------------
    new_path = f"notes/{basename}"
    branch = f"agents/promote-{today.isoformat()}-{re.sub(r'[^a-z0-9]+', '-', basename.lower())[:32]}"
    assessment = (f"\n\n---\n\n## Agent assessment — {today.isoformat()}\n\n"
                  f"Assessed suitable for the permanent record by a **{stores}-of-3 "
                  f"vote** of the project's disclosed AI research crew "
                  f"([agents/README.md](../agents/README.md)):\n\n{vote_md}\n")
    promoted = note + assessment

    main_sha = requests.get(f"{REST}/repos/{OWNER}/{REPO}/git/ref/heads/main",
                            headers=gh).json()["object"]["sha"]
    requests.post(f"{REST}/repos/{OWNER}/{REPO}/git/refs", headers=gh,
                  json={"ref": f"refs/heads/{branch}", "sha": main_sha}).raise_for_status()

    # delete the draft on the branch, then create the promoted copy
    old = requests.get(f"{REST}/repos/{OWNER}/{REPO}/contents/{path}?ref={branch}",
                       headers=gh).json()
    requests.delete(f"{REST}/repos/{OWNER}/{REPO}/contents/{path}", headers=gh, json={
        "message": f"Promote {basename}: remove draft copy",
        "sha": old["sha"], "branch": branch,
    }).raise_for_status()
    requests.put(f"{REST}/repos/{OWNER}/{REPO}/contents/{new_path}", headers=gh, json={
        "message": f"Promote {basename} to notes/ (agent vote {stores}/3)",
        "content": base64.b64encode(promoted.encode()).decode(),
        "branch": branch,
    }).raise_for_status()

    pr = requests.post(f"{REST}/repos/{OWNER}/{REPO}/pulls", headers=gh, json={
        "title": f"Promote to notes/: {basename} (agent vote {stores}/3)",
        "head": branch, "base": "main",
        "body": (f"The agent crew assessed `{path}` and voted **{stores}/3 to "
                 f"store** it in the permanent record. This PR moves it to "
                 f"`{new_path}` with the votes appended.\n\n{vote_md}\n\n"
                 f"The vote is the quality gate — **a human merges**, per "
                 f"GOVERNANCE.md."),
    })
    pr.raise_for_status()
    pr_data = pr.json()
    requests.post(f"{REST}/repos/{OWNER}/{REPO}/labels", headers=gh,
                  json={"name": "agents:approved-2of3", "color": "6B4FA0"})
    requests.post(f"{REST}/repos/{OWNER}/{REPO}/issues/{pr_data['number']}/labels",
                  headers=gh, json={"labels": ["agents:approved-2of3"]})
    print(f"accepted {stores}/3 — PR: {pr_data['html_url']}")


if __name__ == "__main__":
    main()
