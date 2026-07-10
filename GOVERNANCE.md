# Governance

*One page, honestly stated. This file describes how the project is governed
**today**, and names the written triggers that change it as the community
grows. Plans are labeled as plans. No blockchain, no tokens — see the
[Charter](CHARTER.md), §3.*

## Today: maintainer-led, in public

The project currently has one maintainer (**Ryoji Furui**). Pretending a
one-person project is decentralized would be theater; instead, the
maintainer's authority is exercised in public and narrows automatically at
the thresholds written below.

- **Day-to-day technical decisions** happen by *lazy consensus* in issues and
  pull requests: non-trivial changes stay open for review at least **72
  hours**; silence is consent; the maintainer merges.
- **Significant decisions** (anything affecting scope, governance, money, or
  external commitments) start as a `[PROPOSAL]` thread in GitHub Discussions
  (open ≥ 72 hours), and where consensus isn't clear, move to a `[VOTE]`
  thread: votes are **signed comments** (+1 / 0 / −1 from a GitHub account —
  not reactions, which are editable and unattributed), open ≥ 72 hours.
- Every non-trivial decision is recorded as a numbered, **append-only
  decision record** in `decisions/` (created with the first record):
  context, options, outcome, tally, and a link to the thread. Records are
  superseded, never edited.

## Membership: earned, not bought

A **voting member** is someone with (a) at least one merged substantive
contribution — code, review, a documented reproduction, a technical critique
that changed something, documentation — and (b) an endorsement from an
existing member (the maintainer, initially), recorded by a pull request to
`MEMBERS.md` (created with the first member) citing both. The git history is
the membership register.

There are no fees and nothing to purchase. The maintainer may reject
bad-faith membership PRs (e.g. trivial-commit farming) with public reasons.

## Money: transparent by construction

Until a fiscal host exists, the project pools **no funds** at all — and per
the [Charter](CHARTER.md) §2, nothing is ever distributed as profit. Once a
fiscal host holds a community treasury, every spend follows the same
five-step process:

1. **Proposal** — a written spending proposal (amount, deliverable, payee,
   timeline, reporting duty) filed from a public template.
2. **Rubric review** — 2–3 voting members score it publicly against a published,
   frozen rubric (scientific merit, feasibility, cost, openness of outputs,
   roadmap fit).
3. **Vote** — a 7-day `[VOTE]` among voting members; passing requires **⅔ approval** with a
   **quorum of more than half the member roll**. The tally is committed to
   the repository by someone other than the proposer.
4. **Payment** — executed only as a fiscal-host expense linking the decision
   record, on the host's public ledger. Recipients owe a short public report.
5. **Ledger** — mirrored quarterly into a human-readable `TREASURY.md`.

The rubric and proposal template are published before the first round and
never changed mid-round.

## Integrity measures

- Vote threads are snapshotted to an independent archive (archive.org) before
  tallying; governance records are included in the project's periodic DOI
  snapshots (Zenodo).
- The repository is mirrored to a second forge and archived by Software
  Heritage, so no single platform (or person) holds the only copy.
- As soon as a second maintainer exists, administrative control of the GitHub
  organization, funds, and domains moves to two-person control, and this file
  records who holds it.

## Written triggers (the growth contract)

| Trigger | What changes |
|---|---|
| **First voting member** | `MEMBERS.md` begins. (The decision log begins earlier, with the first recorded decision.) |
| **First community treasury (fiscal host in place)** | The five-step spending process above becomes binding; the rubric and proposal template are published first. With fewer than five voting members, the existing roll plus the maintainer score and vote — small, but recorded. |
| **~10 voting members** | A Reviewer role may be added by decision record. |
| **15 voting members** | A 3-person **steering group** is elected by ranked ballot restricted to the member roll (nomination period, ballots committed to the repo). Steering owns budget and governance; the maintainer remains technical lead. |
| **Any physical experiment** | A safety & replication policy is adopted *first*; experiments run only inside host labs' own safety regimes under written agreement (Charter §5). |

## AI research agents

The project operates a small, fully disclosed crew of AI research agents (see
[agents/README.md](agents/README.md)): they post daily in a dedicated
Discussions category, draft weekly technical notes, and review each other's
drafts with a recorded 2-of-3 vote. Their status under this governance is
simple: **they are tools operated under the maintainer's authority, not
members.** Their activity earns no membership, their vote applies only as a
quality gate on agent-drafted notes, and every change to the repository —
including promoted notes — still lands through the human process above. Their
system prompts, schedules, and code are published in the repository; every
post is labeled as agent output; and a human correction outranks any agent
conclusion.

## Disputes and code of conduct

Code of Conduct reports go to **info@ryoji.info** (see
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)). A complaint that concerns the
maintainer cannot be judged by the maintainer: it goes to an outside neutral
contact, who will be named in this file before community recruiting begins.

## Amending this file

This file and the [Charter](CHARTER.md) are amended by a **75% supermajority**
of voting members (quorum: more than half the roll). Until five voting members
exist, the maintainer may amend them — with two exceptions no maintainer
amendment can loosen: the Charter's non-distribution rule (§2) and its
no-crypto scope (§3), which always require the 75% member supermajority. Each
maintainer amendment is logged as a decision record — the log, not trust, is
the guarantee.
