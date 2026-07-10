# -*- coding: utf-8 -*-
"""Fable session: the three agents each draft a candidate prompt for Claude
Fable 5, vote 2-of-3 on the winner (no self-votes), and the winning prompt —
with attached repository documents — is executed on Fable 5. The full
transcript (candidates, votes, prompt, response, usage) is published to the
Agent Lab discussion category.

Env: ANTHROPIC_API_KEY, GH_TOKEN, GITHUB_REPOSITORY, TOPIC (optional),
     MODEL (drafting/voting model), FABLE_MODEL, EFFORT (low|medium|high|xhigh).
Runs inside a checkout of the repository.
"""
import base64
import datetime
import json
import os

import requests

API = "https://api.anthropic.com/v1/messages"
GQL = "https://api.github.com/graphql"
OWNER, REPO = os.environ["GITHUB_REPOSITORY"].split("/")
MODEL = os.environ.get("MODEL", "claude-sonnet-5")
FABLE_MODEL = os.environ.get("FABLE_MODEL", "claude-fable-5")
EFFORT = os.environ.get("EFFORT", "high")
TOPIC = os.environ.get("TOPIC", "").strip()
PERSONAS = ["fabric", "kinetic", "quanta"]
EMOJI = {"fabric": "🧵", "kinetic": "🌊", "quanta": "⚛️"}

# Documents the agents may attach to the Fable 5 request (path -> kind).
ATTACHABLE = {
    "papers/Fable-Computer-Part-I.pdf": "pdf",
    "papers/Fable-Computer-Part-II.pdf": "pdf",
    "fable-model-chain/results.json": "text",
    "fable-model-quantum/results.json": "text",
    "fable-model-chain/README.md": "text",
    "fable-model-quantum/README.md": "text",
    "README.md": "text",
    "ROADMAP.md": "text",
}
MAX_ATTACHMENTS = 4

gh = {"Authorization": f"Bearer {os.environ['GH_TOKEN']}"}
anthropic_headers = {
    "x-api-key": os.environ["ANTHROPIC_API_KEY"],
    "anthropic-version": "2023-06-01",
    "content-type": "application/json",
}


def gql(query, variables=None):
    r = requests.post(GQL, headers=gh, json={"query": query, "variables": variables or {}})
    r.raise_for_status()
    data = r.json()
    if "errors" in data:
        raise RuntimeError(json.dumps(data["errors"]))
    return data["data"]


def read(path, limit=8000):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()[:limit]
    except OSError:
        return "(unavailable)"


def claude(system, user, max_tokens=4000, model=MODEL, effort=None, fable=False,
           schema=None):
    body = {"model": model, "max_tokens": max_tokens, "system": system,
            "messages": [{"role": "user", "content": user}]}
    headers = dict(anthropic_headers)
    if effort or schema:
        body["output_config"] = {}
        if effort:
            body["output_config"]["effort"] = effort
        if schema:
            # Structured outputs: guaranteed valid JSON matching the schema.
            body["output_config"]["format"] = {"type": "json_schema", "schema": schema}
    if fable:
        # Fable 5: thinking always on (no thinking param); refusal fallback on.
        headers["anthropic-beta"] = "server-side-fallback-2026-06-01"
        body["fallbacks"] = [{"model": "claude-opus-4-8"}]
    r = requests.post(API, headers=headers, json=body, timeout=1500)
    r.raise_for_status()
    return r.json()


def text_of(resp):
    return "".join(b.get("text", "") for b in resp.get("content", [])
                   if b.get("type") == "text").strip()


def parse_json(raw):
    raw = raw[raw.find("{"): raw.rfind("}") + 1]
    return json.loads(raw)


def lab_context():
    data = gql("""
      query($owner:String!, $repo:String!) {
        repository(owner:$owner, name:$repo) {
          discussions(first: 5, orderBy: {field: CREATED_AT, direction: DESC}) {
            nodes { title comments(last: 30) { nodes { body createdAt } } }
          }
        }
      }""", {"owner": OWNER, "repo": REPO})
    texts = []
    for d in data["repository"]["discussions"]["nodes"]:
        if d["title"].startswith("Agent Lab — "):
            for c in d["comments"]["nodes"]:
                texts.append(f"[{c['createdAt']}]\n{c['body'][:1500]}")
            break
    return "\n\n---\n\n".join(texts) or "(lab is empty)"


def main():
    today = datetime.date.today()
    lab = lab_context()
    topic_line = (f"The maintainer has requested this session focus on: {TOPIC}"
                  if TOPIC else
                  "No topic was set — choose the question where Fable 5's depth "
                  "would most advance the project right now.")

    # ---- Step 1: three candidate prompts -------------------------------
    draft_instruction = f"""Today is {today.isoformat()}.

The project can make ONE call to Claude Fable 5 — Anthropic's most capable
model — with a prompt of your crafting plus attached project documents.
{topic_line}

Draft your candidate. Rules:
- One deep, specific research question or task — not a survey. Something that
  rewards maximum reasoning depth: a derivation to verify or refute, a
  calibration to attempt, a design question to resolve, an error to hunt.
- State the goal, the constraints, and the deliverable format. Do NOT
  enumerate step-by-step instructions — Fable 5 works best given the goal.
- Require epistemic labels (demonstrated / in-model / open) and honest
  uncertainty in the deliverable.
- Choose up to {MAX_ATTACHMENTS} attachments from exactly this list (repo paths):
{json.dumps(list(ATTACHABLE), indent=2)}

Recent Agent Lab activity for context:

{lab[:12000]}

Return ONLY JSON:
{{"title": "<short title>", "prompt": "<the full prompt text>",
  "attachments": ["<path>", ...], "rationale": "<2-3 sentences why this question>"}}"""

    draft_schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "prompt": {"type": "string"},
            "attachments": {"type": "array", "items": {"type": "string"}},
            "rationale": {"type": "string"},
        },
        "required": ["title", "prompt", "attachments", "rationale"],
        "additionalProperties": False,
    }
    candidates = {}
    for p in PERSONAS:
        persona = read(f"agents/personas/{p}.md")
        resp = claude(persona, draft_instruction, max_tokens=4000, schema=draft_schema)
        candidates[p] = parse_json(text_of(resp))
        print(f"candidate from {p}: {candidates[p]['title']}")

    # ---- Step 2: vote (no self-votes) -----------------------------------
    ballot = "\n\n".join(
        f"### Candidate '{p}' — {c['title']}\nAttachments: {c['attachments']}\n\n{c['prompt']}"
        for p, c in candidates.items())
    votes = {}
    for p in PERSONAS:
        persona = read(f"agents/personas/{p}.md")
        resp = claude(persona, f"""Three candidate prompts for the project's one
Claude Fable 5 call are below. Vote for the strongest — the one most likely to
produce a decision-changing, verifiable result for the project. You may NOT
vote for your own candidate ('{p}').

{ballot}

Return your vote (a candidate name, not your own) and reason (2-3 sentences).""",
                       max_tokens=1500,
                       schema={"type": "object",
                               "properties": {
                                   "vote": {"type": "string",
                                            "enum": ["fabric", "kinetic", "quanta"]},
                                   "reason": {"type": "string"}},
                               "required": ["vote", "reason"],
                               "additionalProperties": False})
        v = parse_json(text_of(resp))
        if v.get("vote") == p or v.get("vote") not in PERSONAS:
            v["vote"] = None  # invalid ballot
        votes[p] = v
        print(f"{p} votes {v['vote']}: {v.get('reason', '')[:80]}")

    tally = {p: sum(1 for v in votes.values() if v["vote"] == p) for p in PERSONAS}
    winner = next((p for p, n in tally.items() if n >= 2), None)

    # ---- Step 3: execute on Fable 5 (if a majority exists) --------------
    date_s = today.isoformat()
    vote_md = "\n".join(
        f"- {EMOJI[p]} **{p.capitalize()}** voted **{votes[p]['vote'] or 'invalid'}** — {votes[p].get('reason', '')}"
        for p in PERSONAS)
    cand_md = "\n".join(
        f"- {EMOJI[p]} **{p.capitalize()}**: *{c['title']}* — {c.get('rationale', '')}"
        for p, c in candidates.items())

    if winner is None:
        title = f"Fable Session — {date_s}: no majority"
        body = (f"The three agents drafted candidate prompts but no candidate "
                f"reached 2 of 3 votes (no self-votes allowed). No Fable 5 call "
                f"was made; no credits were spent.\n\n## Candidates\n{cand_md}\n\n"
                f"## Votes\n{vote_md}\n\nTally: {tally}")
        post_discussion(title, body, [])
        print("no majority — session ended without a Fable call")
        return

    win = candidates[winner]
    content = []
    used = []
    for path in win.get("attachments", [])[:MAX_ATTACHMENTS]:
        kind = ATTACHABLE.get(path)
        if kind == "pdf":
            with open(path, "rb") as f:
                data = base64.b64encode(f.read()).decode()
            content.append({"type": "document",
                            "source": {"type": "base64",
                                       "media_type": "application/pdf",
                                       "data": data}})
            used.append(path)
        elif kind == "text":
            content.append({"type": "text",
                            "text": f"=== ATTACHED: {path} ===\n\n{read(path, 60000)}"})
            used.append(path)
    content.append({"type": "text", "text": win["prompt"]})

    system = ("You are engaged by the Fable Computer project's disclosed AI "
              "research crew (github.com/ryoji-info/FableComputer, agents/README.md). "
              "This prompt was selected by a recorded 2-of-3 agent vote and your "
              "answer will be published verbatim in the project's public Agent Lab. "
              "Label every claim demonstrated / in-model / open; cite precisely; "
              "state uncertainty honestly; a well-supported negative result is a "
              "success.")
    print(f"calling {FABLE_MODEL} (effort={EFFORT}) with {len(used)} attachments...")
    resp = claude(system, content, max_tokens=16000, model=FABLE_MODEL,
                  effort=EFFORT, fable=True)

    stop = resp.get("stop_reason")
    usage = resp.get("usage", {})
    answer = text_of(resp)
    served_by = resp.get("model", FABLE_MODEL)
    if stop == "refusal" or not answer:
        answer = (f"*(The request was declined by the model's safety classifiers "
                  f"(stop_reason: {stop}). No answer was produced.)*")

    title = f"Fable Session — {date_s}: {win['title']}"
    body = (f"One prompt, drafted and selected by the agent crew "
            f"(2-of-3 vote, no self-votes), executed on **{served_by}** "
            f"(effort: {EFFORT}).\n\n"
            f"## Candidates\n{cand_md}\n\n## Votes\n{vote_md}\n\nTally: {tally} → "
            f"**{EMOJI[winner]} {winner.capitalize()} wins**\n\n"
            f"## Winning prompt\n\n> " + win["prompt"].replace("\n", "\n> ") +
            f"\n\nAttachments sent: {used}\n\n"
            f"Usage: {usage.get('input_tokens', '?')} in / "
            f"{usage.get('output_tokens', '?')} out tokens · stop: {stop}\n\n"
            f"*Charter: [agents/README.md](https://github.com/{OWNER}/{REPO}/blob/main/agents/README.md). "
            f"The response follows in the comments, verbatim.*")
    post_discussion(title, body, [answer])
    print("session published")


def post_discussion(title, body, comments):
    data = gql("""
      query($owner:String!, $repo:String!) {
        repository(owner:$owner, name:$repo) {
          id
          discussionCategories(first: 25) { nodes { id name } }
        }
      }""", {"owner": OWNER, "repo": REPO})
    repo_id = data["repository"]["id"]
    cats = {c["name"]: c["id"] for c in data["repository"]["discussionCategories"]["nodes"]}
    cat_id = cats.get("Agent Lab") or next(iter(cats.values()))
    d = gql("""
      mutation($repoId:ID!, $catId:ID!, $title:String!, $body:String!) {
        createDiscussion(input:{repositoryId:$repoId, categoryId:$catId,
                                title:$title, body:$body}) {
          discussion { id url }
        }
      }""", {"repoId": repo_id, "catId": cat_id,
             "title": title, "body": body[:60000]})
    disc = d["createDiscussion"]["discussion"]
    for comment in comments:
        # GitHub caps bodies at 65536 chars — chunk long responses.
        for i in range(0, len(comment), 60000):
            gql("""
              mutation($id:ID!, $body:String!) {
                addDiscussionComment(input:{discussionId:$id, body:$body}) {
                  comment { id }
                }
              }""", {"id": disc["id"], "body": comment[i:i + 60000]})
    print("discussion:", disc["url"])


if __name__ == "__main__":
    main()
