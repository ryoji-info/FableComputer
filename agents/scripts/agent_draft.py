# -*- coding: utf-8 -*-
"""Weekly note draft: the rotating author-agent compiles the lab's recent work
into a technical note and opens a pull request into notes/drafts/.

Env: ANTHROPIC_API_KEY, GH_TOKEN, GITHUB_REPOSITORY, MODEL (optional).
Prints the created PR number to stdout (last line) for the review job.
"""
import datetime
import json
import os
import re

import requests

API = "https://api.anthropic.com/v1/messages"
GQL = "https://api.github.com/graphql"
REST = "https://api.github.com"
OWNER, REPO = os.environ["GITHUB_REPOSITORY"].split("/")
MODEL = os.environ.get("MODEL", "claude-sonnet-5")
PERSONAS = ["fabric", "kinetic", "quanta"]
EMOJI = {"fabric": "🧵", "kinetic": "🌊", "quanta": "⚛️"}

gh = {"Authorization": f"Bearer {os.environ['GH_TOKEN']}",
      "Accept": "application/vnd.github+json"}


def gql(query, variables=None):
    r = requests.post(GQL, headers=gh, json={"query": query, "variables": variables or {}})
    r.raise_for_status()
    data = r.json()
    if "errors" in data:
        raise RuntimeError(json.dumps(data["errors"]))
    return data["data"]


def lab_comments(max_threads=2, per_thread=60):
    data = gql("""
      query($owner:String!, $repo:String!, $n:Int!) {
        repository(owner:$owner, name:$repo) {
          discussions(first: 10, orderBy: {field: CREATED_AT, direction: DESC}) {
            nodes { title comments(last:$n) { nodes { body createdAt } } }
          }
        }
      }""", {"owner": OWNER, "repo": REPO, "n": per_thread})
    texts = []
    kept = 0
    for d in data["repository"]["discussions"]["nodes"]:
        if d["title"].startswith("Agent Lab — ") and kept < max_threads:
            kept += 1
            for c in d["comments"]["nodes"]:
                texts.append(f"[{c['createdAt']}]\n{c['body'][:2000]}")
    return "\n\n---\n\n".join(texts) or "(lab is empty)"


def read(path, limit=8000):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()[:limit]
    except OSError:
        return "(unavailable)"


def main():
    today = datetime.date.today()
    author = PERSONAS[today.isocalendar().week % 3]
    persona = read(f"agents/personas/{author}.md")

    prompt = f"""Today is {today.isoformat()}. You are this week's rotating author.

Compile the Agent Lab's recent work into ONE short technical note for the
project's notes/ collection. Requirements:

- 800–1500 words, GitHub markdown.
- Begin with this exact metadata block, filled in:

  ---
  title: <specific, modest title>
  author: {author.capitalize()} {EMOJI[author]} (AI research agent, Fable Computer project)
  date: {today.isoformat()}
  status: draft — pending agent review (2-of-3) and human merge
  license: CC BY 4.0
  ---

- One clearly stated question or result; not a survey of everything.
- Every claim labeled demonstrated / in-model / open. Citations precise.
- A "Limitations and open items" section is mandatory.
- No hype. A negative or inconclusive result is acceptable and valuable.

Recent Agent Lab material:

{lab_comments()}

Reference: current model-chain outputs:
{read('fable-model-chain/results.json', 2500)}
{read('fable-model-quantum/results.json', 2500)}

Return ONLY the note's markdown, starting with the metadata block."""

    r = requests.post(API, headers={
        "x-api-key": os.environ["ANTHROPIC_API_KEY"],
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }, json={"model": MODEL, "max_tokens": 12000, "system": persona,
             "messages": [{"role": "user", "content": prompt}]})
    r.raise_for_status()
    data = r.json()
    note = "".join(b.get("text", "") for b in data["content"]
                   if b.get("type") == "text").strip()
    if not note:
        raise RuntimeError(
            f"empty completion (stop_reason={data.get('stop_reason')}) — no draft created")

    m = re.search(r"^title:\s*(.+)$", note, re.M)
    slug = re.sub(r"[^a-z0-9]+", "-", (m.group(1) if m else "note").lower()).strip("-")[:60]
    path = f"notes/drafts/{today.isoformat()}-{slug}.md"
    branch = f"agents/note-{today.isoformat()}"

    main_sha = requests.get(f"{REST}/repos/{OWNER}/{REPO}/git/ref/heads/main",
                            headers=gh).json()["object"]["sha"]
    requests.post(f"{REST}/repos/{OWNER}/{REPO}/git/refs", headers=gh,
                  json={"ref": f"refs/heads/{branch}", "sha": main_sha}).raise_for_status()
    import base64
    requests.put(f"{REST}/repos/{OWNER}/{REPO}/contents/{path}", headers=gh, json={
        "message": f"Agent Lab draft note: {slug}",
        "content": base64.b64encode(note.encode()).decode(),
        "branch": branch,
    }).raise_for_status()

    pr = requests.post(f"{REST}/repos/{OWNER}/{REPO}/pulls", headers=gh, json={
        "title": f"Agent Lab note ({today.isoformat()}): {slug}",
        "head": branch, "base": "main",
        "body": ("Weekly technical note drafted by the project's disclosed AI research "
                 f"crew (author this week: {author.capitalize()} {EMOJI[author]}).\n\n"
                 "Pipeline: all three agents will review and vote (2-of-3 to promote); "
                 "**a human merges** per GOVERNANCE.md. Charter: "
                 f"https://github.com/{OWNER}/{REPO}/blob/main/agents/README.md"),
    })
    pr.raise_for_status()
    print(pr.json()["number"])


if __name__ == "__main__":
    main()
