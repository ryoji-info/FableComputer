<img src="../branding/boogie-sorbet-monogram.svg" alt="" width="72" align="right">

# Technical Notes

Short technical notes produced by the project — primarily by the disclosed
[Agent Lab](../agents/README.md) crew, but human-authored notes are equally
welcome via the same pipeline.

## Pipeline and status levels

1. **`notes/drafts/`** — a note under review. Agent-drafted notes arrive here
   weekly by pull request; replies from
   [Fable 5 sessions](../agents/README.md) are placed here by the maintainer.
2. **Agent vote** — all three agents review independently against the
   published standard and vote, **2 of 3 to promote**. For weekly drafts the
   vote is accept / revise / reject on the pull request (label
   `agents:approved-2of3`); anything less returns the draft to the lab with
   recorded dissent. For Fable 5 replies the vote is store / reject, recorded
   in the note itself; a passing vote opens a promotion pull request, a
   failing one opens an issue recommending rework or removal.
3. **`notes/`** — promoted notes, merged **by a human** per
   [GOVERNANCE.md](../GOVERNANCE.md). The agents' vote is a quality gate,
   not an authority over the repository.
4. **`papers/`** — promoted notes feed the next manuscript revision: the
   maintainer uses Claude Fable 5 to fold their corrections back into the
   papers and reviews and commits the result by hand, marked as a versioned
   community revision on the title page.

## Standards

Every note: claims labeled *demonstrated / in-model / open*; precise
citations; numbers consistent with the model chains where applicable; a
mandatory "Limitations and open items" section; no hype.

All notes are licensed **CC BY 4.0** (see [LICENSING.md](../LICENSING.md)).
Notes are working documents, not peer-reviewed publications — treat them as
the project treats everything: a starting point for scrutiny.
