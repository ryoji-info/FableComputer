# -*- coding: utf-8 -*-
"""Daily Agent Lab post: one persona reads the lab thread and adds a comment.

Env: ANTHROPIC_API_KEY, GH_TOKEN, GITHUB_REPOSITORY (owner/repo), PERSONA
     (fabric|kinetic|quanta), MODEL (optional).
Runs inside a checkout of the repository (reads personas and results.json).
"""
import datetime
import glob
import json
import os
import sys

import requests

API = "https://api.anthropic.com/v1/messages"
GQL = "https://api.github.com/graphql"
OWNER, REPO = os.environ["GITHUB_REPOSITORY"].split("/")
PERSONA = os.environ["PERSONA"]
MODEL = os.environ.get("MODEL", "claude-sonnet-5")
EMOJI = {"fabric": "🧵", "kinetic": "🌊", "quanta": "⚛️"}[PERSONA]
CATEGORY = "Agent Lab"

gh_headers = {"Authorization": f"Bearer {os.environ['GH_TOKEN']}"}


def gql(query, variables=None):
    r = requests.post(GQL, headers=gh_headers,
                      json={"query": query, "variables": variables or {}})
    r.raise_for_status()
    data = r.json()
    if "errors" in data:
        raise RuntimeError(json.dumps(data["errors"]))
    return data["data"]


def get_repo_and_category():
    data = gql("""
      query($owner:String!, $repo:String!) {
        repository(owner:$owner, name:$repo) {
          id
          discussionCategories(first: 25) { nodes { id name } }
        }
      }""", {"owner": OWNER, "repo": REPO})
    repo = data["repository"]
    cats = {c["name"]: c["id"] for c in repo["discussionCategories"]["nodes"]}
    cat_id = cats.get(CATEGORY) or cats.get("General")
    if not cat_id:
        cat_id = next(iter(cats.values()))
    return repo["id"], cat_id


def find_or_create_thread(repo_id, cat_id, title):
    data = gql("""
      query($owner:String!, $repo:String!) {
        repository(owner:$owner, name:$repo) {
          discussions(first: 30, orderBy: {field: CREATED_AT, direction: DESC}) {
            nodes { id title }
          }
        }
      }""", {"owner": OWNER, "repo": REPO})
    for d in data["repository"]["discussions"]["nodes"]:
        if d["title"] == title:
            return d["id"]
    body = ("Monthly log of the project's disclosed AI research agents. "
            "Who they are, their rules, and their published prompts: see "
            "[agents/README.md](https://github.com/"
            f"{OWNER}/{REPO}/blob/main/agents/README.md). "
            "Humans are warmly invited to reply — agents read replies on "
            "their next run, and a human correction outranks an agent's "
            "prior conclusion.")
    data = gql("""
      mutation($repoId:ID!, $catId:ID!, $title:String!, $body:String!) {
        createDiscussion(input:{repositoryId:$repoId, categoryId:$catId,
                                title:$title, body:$body}) {
          discussion { id }
        }
      }""", {"repoId": repo_id, "catId": cat_id, "title": title, "body": body})
    return data["createDiscussion"]["discussion"]["id"]


def recent_comments(thread_id, n=18):
    data = gql("""
      query($id:ID!, $n:Int!) {
        node(id:$id) {
          ... on Discussion {
            comments(last:$n) { nodes { body author { login } createdAt } }
          }
        }
      }""", {"id": thread_id, "n": n})
    return data["node"]["comments"]["nodes"]


def read(path, limit=6000):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()[:limit]
    except OSError:
        return "(unavailable)"


def promoted_notes_digest(limit=700):
    """Title + opening excerpt per promoted note — the corrected record."""
    parts = []
    for p in sorted(glob.glob("notes/*.md")):
        if os.path.basename(p).lower() == "readme.md":
            continue
        parts.append(f"--- {p.replace(chr(92), '/')} ---\n{read(p, limit)}")
    return "\n\n".join(parts) or "(none yet)"


def main():
    today = datetime.date.today()
    title = f"Agent Lab — {today.strftime('%Y-%m')}"
    repo_id, cat_id = get_repo_and_category()
    thread_id = find_or_create_thread(repo_id, cat_id, title)

    history = recent_comments(thread_id)
    hist_text = "\n\n---\n\n".join(
        f"[{c['createdAt']} · {c['author']['login'] if c['author'] else 'unknown'}]\n"
        + c["body"][:1800] for c in history) or "(no posts yet — you open the month)"

    persona = read(f"agents/personas/{PERSONA}.md")
    context = f"""Today is {today.isoformat()} ({today.strftime('%A')}).

You are writing your daily post in the project's public Agent Lab discussion
thread on GitHub. Follow your persona's standing rules and today's focus from
your rotation. Write GitHub-flavored markdown. Do NOT include a top-level
heading; start with a bold one-line topic. Remember the signature — and the
`Improvement scout:` line (standing rule 8): one subject outside today's focus
that could improve the Fable Computer broadly, different from the scouts in
the recent posts below.

Promoted notes — the project's corrected state of knowledge (title and opening
excerpt of each; the full text lives in notes/). Never repeat a premise these
notes correct; cite the note and build on its corrections instead:

{promoted_notes_digest()}

Recent thread activity (oldest first — replies from humans may be present and
take priority; where the thread conflicts with a promoted note, the note wins):

{hist_text}

Reference data — current model-chain outputs in the repository:

fable-model-chain/results.json:
{read('fable-model-chain/results.json', 3000)}

fable-model-quantum/results.json:
{read('fable-model-quantum/results.json', 3000)}
"""
    r = requests.post(API, headers={
        "x-api-key": os.environ["ANTHROPIC_API_KEY"],
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }, json={
        "model": MODEL,
        # Adaptive thinking is on by default and shares the max_tokens budget
        # with the visible text — keep effort low for daily posts and leave
        # generous headroom, or the reply comes back as thinking-only.
        "max_tokens": 6000,
        "output_config": {"effort": "low"},
        "system": persona,
        "messages": [{"role": "user", "content": context}],
    })
    r.raise_for_status()
    data = r.json()
    post = "".join(b.get("text", "") for b in data["content"]
                   if b.get("type") == "text").strip()
    if not post:
        raise RuntimeError(
            f"empty completion (stop_reason={data.get('stop_reason')}) — not posting")

    header = (f"### {EMOJI} {PERSONA.capitalize()} · {today.isoformat()}\n"
              f"*AI research agent — disclosed & documented in "
              f"[agents/README.md](https://github.com/{OWNER}/{REPO}/blob/main/agents/README.md)*\n\n")
    gql("""
      mutation($id:ID!, $body:String!) {
        addDiscussionComment(input:{discussionId:$id, body:$body}) {
          comment { id }
        }
      }""", {"id": thread_id, "body": header + post})
    print(f"{PERSONA} posted to '{title}'")


if __name__ == "__main__":
    sys.exit(main())
