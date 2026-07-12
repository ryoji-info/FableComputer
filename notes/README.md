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

**Pre-registered predictions.** A note that predicts the outcome of a run
that does not yet exist must give the predicted quantity **its own name** —
never an existing `results.json` key or published figure's name (predict
`pulse_gain_dB_at_0p7_streaming_retuned`, not
`pulse_gain_dB_at_0p7_streaming`). The note must state which existing
outputs the prediction does *not* contest, and give an explicit
falsification band. A prediction that shares a name with a reference output
reads as a contradiction of the record and will fail review for that reason
alone — this rule exists because exactly that happened
([issue #13](https://github.com/ryoji-info/FableComputer/issues/13)). When
the predicted run later lands, its measured value enters `results.json`
under the new key, and the note's prediction is marked resolved
(confirmed / falsified) in a follow-up or revision.

**New computed quantities ship their computation.** A note whose claims rest
on a construction that is not already in the released chains — a derived
operator, a new solver, a nontrivial numerical evaluation — must include the
computation itself: a self-contained runnable listing (or a script committed
alongside the note), with expected outputs stated so a reviewer can verify
every headline number by running it. Formulas alone meet this bar only when
a reader can re-derive each number from them directly. Results computed on
apparatus the reader cannot run or rebuild will fail review for that reason
alone, whatever their internal consistency — this rule exists because
exactly that happened
([issue #18](https://github.com/ryoji-info/FableComputer/issues/18)). The
*demonstrated* label may be applied to such results only in the form
"demonstrated (runnable, see listing)" — the label carries an artifact, not
an assertion.

All notes are licensed **CC BY 4.0** (see [LICENSING.md](../LICENSING.md)).
Notes are working documents, not peer-reviewed publications — treat them as
the project treats everything: a starting point for scrutiny.
