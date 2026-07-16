# -*- coding: utf-8 -*-
"""Agent review vote on a draft note PR: all three personas review
independently; 2-of-3 'accept' promotes the draft (label); a human merges.

Env: ANTHROPIC_API_KEY, GH_TOKEN, GITHUB_REPOSITORY, PR_NUMBER, MODEL (optional).
"""
import json
import os

import requests

API = "https://api.anthropic.com/v1/messages"
REST = "https://api.github.com"
OWNER, REPO = os.environ["GITHUB_REPOSITORY"].split("/")
PR = os.environ["PR_NUMBER"]
MODEL = os.environ.get("MODEL", "claude-opus-4-8")
PERSONAS = ["fabric", "kinetic", "quanta"]
EMOJI = {"fabric": "🧵", "kinetic": "🌊", "quanta": "⚛️"}

gh = {"Authorization": f"Bearer {os.environ['GH_TOKEN']}",
      "Accept": "application/vnd.github+json"}

STANDARD = """Review standard (published in agents/README.md):
1. Epistemic labels: every claim marked demonstrated / in-model / open, correctly.
2. Citations: precise and used for what they actually show.
3. Consistency: numbers must match the repository's model-chain outputs where applicable.
4. Modesty: no hype; limitations section present and honest.
5. Value: the note tells the community something it can use or build on.
Vote 'accept' only if all five hold. 'revise' for fixable issues; 'reject' if
the core content is wrong or empty. You vote independently; do not assume the
other reviewers' views."""


def read(path, limit=8000):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()[:limit]
    except OSError:
        return "(unavailable)"


def main():
    files = requests.get(f"{REST}/repos/{OWNER}/{REPO}/pulls/{PR}/files", headers=gh).json()
    target = next((f for f in files if f["filename"].startswith("notes/drafts/")), None)
    if not target:
        print("No draft note in this PR; skipping.")
        return
    raw = requests.get(target["raw_url"], headers=gh).text[:24000]

    votes = {}
    for p in PERSONAS:
        persona = read(f"agents/personas/{p}.md")
        r = requests.post(API, headers={
            "x-api-key": os.environ["ANTHROPIC_API_KEY"],
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }, json={
            "model": MODEL, "max_tokens": 12000, "system": persona,
            # explicit: Opus 4.8 runs without thinking if this is omitted
            "thinking": {"type": "adaptive"},
            "output_config": {"format": {"type": "json_schema", "schema": {
                "type": "object",
                "properties": {
                    "vote": {"type": "string", "enum": ["accept", "revise", "reject"]},
                    "reasons": {"type": "string"},
                    "top_issues": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["vote", "reasons", "top_issues"],
                "additionalProperties": False,
            }}},
            "messages": [{"role": "user", "content":
                f"{STANDARD}\n\nReview this draft note and return your verdict: "
                'vote (accept/revise/reject), reasons (3-6 sentences), '
                'top_issues (specific problems).\n\nDRAFT:\n\n' + raw}],
        })
        r.raise_for_status()
        text = "".join(b.get("text", "") for b in r.json()["content"]
                       if b.get("type") == "text").strip()
        text = text[text.find("{"): text.rfind("}") + 1]
        try:
            votes[p] = json.loads(text)
        except json.JSONDecodeError:
            votes[p] = {"vote": "revise", "reasons": "Unparseable review output.",
                        "top_issues": []}
        v = votes[p]
        body = (f"### {EMOJI[p]} {p.capitalize()} — review vote: **{v['vote'].upper()}**\n\n"
                f"{v['reasons']}\n\n"
                + ("".join(f"- {i}\n" for i in v.get("top_issues", [])))
                + f"\n*AI research agent (disclosed) — see agents/README.md*")
        requests.post(f"{REST}/repos/{OWNER}/{REPO}/issues/{PR}/comments",
                      headers=gh, json={"body": body}).raise_for_status()

    accepts = sum(1 for v in votes.values() if v["vote"] == "accept")
    passed = accepts >= 2
    label = "agents:approved-2of3" if passed else "agents:returned"
    requests.post(f"{REST}/repos/{OWNER}/{REPO}/labels", headers=gh,
                  json={"name": label, "color": "6B4FA0" if passed else "B23A1E"})
    requests.post(f"{REST}/repos/{OWNER}/{REPO}/issues/{PR}/labels",
                  headers=gh, json={"labels": [label]})
    tally = ", ".join(f"{p.capitalize()}: {votes[p]['vote']}" for p in PERSONAS)
    verdict = ("**Promoted by 2-of-3 vote** — awaiting human review and merge "
               "(the agents' vote is a quality gate, not an authority; see GOVERNANCE.md)."
               if passed else
               "**Returned to the lab** — fewer than 2 of 3 accepts; the author agent "
               "should address the recorded issues in a future draft.")
    requests.post(f"{REST}/repos/{OWNER}/{REPO}/issues/{PR}/comments", headers=gh,
                  json={"body": f"## Agent vote result\n\n{tally}\n\n{verdict}"}).raise_for_status()
    print(f"votes: {tally} -> {'PASS' if passed else 'RETURN'}")


if __name__ == "__main__":
    main()
