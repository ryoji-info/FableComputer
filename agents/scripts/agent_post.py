# -*- coding: utf-8 -*-
"""Agent Lab post: one persona reads the lab thread and adds a comment.

May run several times per day (scheduled and/or manual). Each run posts a
fresh, run-numbered set unless the persona already posted within the last 10
minutes (anti-double-fire guard), so retries and racing runs don't duplicate.
Reads notes/ and papers/ for recent changes so posts engage the latest state.

Env: ANTHROPIC_API_KEY, GH_TOKEN, GITHUB_REPOSITORY (owner/repo), PERSONA
     (fabric|kinetic|quanta), MODEL (optional).
Runs inside a checkout of the repository (reads personas and results.json).
"""
import datetime
import glob
import json
import os
import subprocess
import sys

import requests

API = "https://api.anthropic.com/v1/messages"
GQL = "https://api.github.com/graphql"
OWNER, REPO = os.environ["GITHUB_REPOSITORY"].split("/")
PERSONA = os.environ["PERSONA"]
MODEL = os.environ.get("MODEL", "claude-opus-4-8")
EMOJI = {"fabric": "🧵", "kinetic": "🌊", "quanta": "⚛️"}[PERSONA]
CATEGORY = "Agent Lab"

gh_headers = {"Authorization": f"Bearer {os.environ['GH_TOKEN']}"}


JST = datetime.timezone(datetime.timedelta(hours=9))


def today_jst():
    """The project runs on Japan time; Actions runners are UTC. The 06:00 JST
    cron fires at 21:00 the previous UTC day, so dating by the runner's clock
    labels artifacts with yesterday's date."""
    return datetime.datetime.now(JST).date()


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
          discussions(first: 50, orderBy: {field: UPDATED_AT, direction: DESC}) {
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


def recent_changes(paths, n=12):
    """Recent git changes under the given paths, so posts engage the latest
    state of notes/ and papers/ rather than stale content. Degrades to a
    placeholder if git is unavailable or the checkout is too shallow (in CI,
    the workflow checks out with fetch-depth: 0 so history is present)."""
    try:
        out = subprocess.run(
            ["git", "log", f"-n{n}", "--date=short", "--format=%ad %s",
             "--", *paths],
            capture_output=True, text=True, timeout=30)
        return out.stdout.strip() or "(no recent changes)"
    except Exception:
        return "(unavailable)"


def papers_manifest():
    """The manuscripts in papers/ — binary (.docx/.pdf), cited by URL and never
    excerpted inline; listed so personas reference the right ones."""
    try:
        files = sorted(f for f in os.listdir("papers") if not f.startswith("."))
        return "\n".join(files) or "(none)"
    except OSError:
        return "(unavailable)"


def run_number_and_guard(history, today):
    """Count today's posts by this persona (for the (run N) suffix) and guard
    against an accidental double-fire. Returns the run number to use, or None
    if a post by this persona is less than 10 minutes old (skip — a retry or a
    concurrent run just made it). Headers may carry an optional (run N) suffix,
    so match on the "### <emoji> <Persona> · <today>" prefix only."""
    prefix = f"### {EMOJI} {PERSONA.capitalize()} · {today.isoformat()}"
    now = datetime.datetime.now(datetime.timezone.utc)
    todays = [c for c in history if c["body"].startswith(prefix)]
    for c in todays:
        created = datetime.datetime.fromisoformat(
            c["createdAt"].replace("Z", "+00:00"))
        if now - created < datetime.timedelta(minutes=10):
            return None
    return len(todays) + 1


def main():
    today = today_jst()
    title = f"Agent Lab — {today.strftime('%Y-%m')}"
    repo_id, cat_id = get_repo_and_category()
    thread_id = find_or_create_thread(repo_id, cat_id, title)

    history = recent_comments(thread_id)

    # Multiple runs per day are allowed; only guard an accidental double-fire.
    run_no = run_number_and_guard(history, today)
    if run_no is None:
        print(f"{PERSONA} posted <10 min ago — skipping (anti-double-fire guard)")
        return

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

Recent changes in notes/ and papers/ — check for updates and engage anything
new (a note may not be reflected in the thread yet; a paper may have been
revised). notes/ outrank any manuscript passage they correct (standing rule 10):

{recent_changes(['notes', 'papers'])}

Manuscripts currently in papers/ (cite by URL; binary, not excerpted here):

{papers_manifest()}

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
        # Adaptive thinking must be requested explicitly: Sonnet 5 defaults to
        # adaptive, but Opus 4.8 runs WITHOUT thinking when the param is omitted.
        # Thinking shares the max_tokens budget with the visible text — keep
        # effort low for daily posts and leave generous headroom.
        "thinking": {"type": "adaptive"},
        "max_tokens": 6000,
        "output_config": {"effort": "low"},
        "system": persona,
        "messages": [{"role": "user", "content": context}],
    }, timeout=600)
    r.raise_for_status()
    data = r.json()
    post = "".join(b.get("text", "") for b in data["content"]
                   if b.get("type") == "text").strip()
    if not post:
        raise RuntimeError(
            f"empty completion (stop_reason={data.get('stop_reason')}) — not posting")

    # Run 1 keeps the plain date; same-day repeats get a "(run N)" suffix.
    date_label = today.isoformat() if run_no == 1 else f"{today.isoformat()} (run {run_no})"
    header = (f"### {EMOJI} {PERSONA.capitalize()} · {date_label}\n"
              f"*AI research agent — disclosed & documented in "
              f"[agents/README.md](https://github.com/{OWNER}/{REPO}/blob/main/agents/README.md)*\n\n")
    gql("""
      mutation($id:ID!, $body:String!) {
        addDiscussionComment(input:{discussionId:$id, body:$body}) {
          comment { id }
        }
      }""", {"id": thread_id, "body": header + post})
    print(f"{PERSONA} posted to '{title}' (run {run_no})")


if __name__ == "__main__":
    sys.exit(main())
