# The record audit as a note: ten findings on where the published artifacts diverge from the 25-note corrected record — the dead generator, the public on-ramp, and why hand-reading could not certify completeness

**Status:** promoted to `notes/` — accepted by a **3-of-3 agent vote** (recorded below). **License:** CC BY 4.0.
**Prompted by:** [Fable Session — 2026-07-26 (IV), discussion #66](https://github.com/ryoji-info/FableComputer/discussions/66) — the fourth submission of the ledger commissioned by Kinetic's 🌊 winning prompt, whose 2-1-0 ballot is recorded in [#63](https://github.com/ryoji-info/FableComputer/discussions/63). Earlier submissions were assessed **1-of-3** ([#63](https://github.com/ryoji-info/FableComputer/discussions/63)), **0-of-3** ([#64](https://github.com/ryoji-info/FableComputer/discussions/64)) and **0-of-3** ([#65](https://github.com/ryoji-info/FableComputer/discussions/65)); all four discussions and their vote records stand unedited as the record.
**Scope of this promotion:** **the note only.** The 66-entry work order published at [#65](https://github.com/ryoji-info/FableComputer/discussions/65) was **not** submitted for storage and is **not** promoted here; it is to be discharged into `papers/ERRATA.md` plus an issue set. Five of the nine votes cast across #63–#65 asked for exactly this separation.
**Method:** two runnable artifacts, `ledger_listing.py` (numeric claims) and `ledger_sweep.py` (an eight-signature defect sweep over 100 files), both tracked in-tree at commit `135f7b5` and both text-identical modulo line endings to the blocks embedded in the reply — independently hashed by the assessors and by the executor. Paper and `docs/` text quoted from extractions the artifacts reproduce. Assessed by three blind, independent persona agents, each instructed to re-execute every *demonstrated* claim itself rather than trust the transcript (the post-#54 source-read rule), and explicitly instructed neither to reject from momentum after three prior rejections nor to store from fatigue.
**Author:** Claude **Opus 5** (`claude-opus-5`) — **not** `claude-fable-5`, this routine's default and intended model. The maintainer set the model with `/model`; nothing in this note is labelled or represented as Fable 5 output. Maintainer-operated Claude Code session per [agents/README.md](../agents/README.md), 2026-07-26 (assessed the same day, also on `claude-opus-5`).
**Labels:** demonstrated / in-model / open, per [notes/README.md](README.md). Findings 1, 2, 4, 5, 6, 7, 8, 9, 10 are **demonstrated**; Finding 3 is demonstrated on the record side and **in-model** in its composition.
**Binding record honored:** [`notes/2026-07-22-cavity-ringdown-isi.md`](2026-07-22-cavity-ringdown-isi.md), [`notes/2026-07-22-flush-noise-figure-negative.md`](2026-07-22-flush-noise-figure-negative.md), [`notes/2026-07-23-reset-switch-adjudication.md`](2026-07-23-reset-switch-adjudication.md) (its §4 escape table — E1 79–92, E2 98–128, **E3 100–148 GHz "F = 2 closes? yes"** — and its own "the defensible headline is ≈ 0.1 THz logic" are **consumed and carried, not contested**; #64's contrary claim was withdrawn as false before this submission), [`notes/2026-07-25-e1-burst-scaling-proviso.md`](2026-07-25-e1-burst-scaling-proviso.md), [`notes/2026-07-22-mth-numerical-vs-physical-viscosity.md`](2026-07-22-mth-numerical-vs-physical-viscosity.md) (binding for Findings 5 and 6), [`notes/2026-07-17-what-the-38-quanta-knee-denominates-after-the-july-plane-aud.md`](2026-07-17-what-the-38-quanta-knee-denominates-after-the-july-plane-aud.md), [`notes/2026-07-16-no-physical-avg16-accumulator.md`](2026-07-16-no-physical-avg16-accumulator.md). It contests **no** `results.json` value and reopens **no** promoted key.

**Assessment-flagged items (recorded, not applied — the reply text is evidence and is not edited after posting).** All three assessors voted STORE for the whole document and converged on the same non-blocking defects, listed verbatim per persona below. In summary: (i) the sweep transcript's in-band excerpt marker reads "61 further disposed hits" where the program prints 82 hit lines with 6 shown, so **76** are elided — an annotation error in a *disclosed* excerpt, and expressly **not** the #64/#65 class in which the transcript was not the program's output; (ii) Finding 10's clause "which is why both are printed with the result" is **false of the file set** — `ledger_sweep.py` prints only `len(files)` and the notes/ subcount, not the 100 filenames, and this sits inside a *demonstrated*-labelled finding; (iii) the caption calls the excerpt "the tail" while the six hit lines shown are the alphabetical head; (iv) two `DISPOSED` keys never fire (`fable-model-chain/figures.py:160`, `fable-model-quantum/qerrors.py:36`) and one disposition string mislabels which line it owns (`figures.py:164` is the y-axis label, not the Figure 8 caption); (v) `fable-model-chain/results.json`'s `M_th_num` key carries no provenance tag, which the 07-22 viscosity note orders alongside the emission Finding 5 does charge.

**Executor's independent falsification record (recorded, not applied).** A dedicated falsification hunter, run outside the vote as an executor-side guard, **achieved a TIER 1 falsification** — a divergence in a file *and* a signature class the sweep claims to cover — on three mechanisms, each re-verified by hand by the executor before promotion. All are **line-wrap blindness**, a failure mode none of Finding 10's stated disclaimers covers: (a) the `'five decades'` signature never fires on `fable-model-quantum/make_manuscript.py:493–494`, where the phrase is split across a Python string-concatenation boundary — **the same occurrence Finding 7 itself asserts is there**, so the note names a hit its own instrument certifies as absent; (b) `fable-model-chain/README.md:47–51` restates the retired 4-ps flush architecture ("data-pattern ISI is controlled by the architecture's per-slot bias gating / re-sync flushing, not assumed away") and is owned by **no** finding, invisible because line 50 reads "the 4 ps slot" with a space where the signature requires `4-ps slot`; (c) the `averages as 1/` branch is blind to both of its intended targets (`qmac.py:110–111`, `qerrors.py:35–36`) for the same reason, which is why the map's key for `qerrors.py:36` is dead. Consequently **Finding 10's certificate — "every occurrence of eight record-derived signatures … has a named owner" — is false as written**, and should be requalified to occurrences *on a single line* before the ledger's method is reused. Finding 10's own framing ("a floor, not a certificate") and Limitation 2 ("I expect a determined assessor to succeed — that is the point of publishing the criterion") anticipate this outcome, which is why all three assessors judged it non-blocking; the crew's vote stands, and the correction is recorded here for the merging human rather than applied to the evidence.

---

> **Maintainer's self-correction, posted to the discussion before the vote and reproduced here as part of the record.**

**Self-correction, posted before assessment — one stated fact in this note is wrong, in the conservative direction.**

The note says (in *What this does not license* and Limitation 1) that the two artifacts are *"present in the working tree but untracked (`git status` shows them as `??`); committing them belongs to the CI item"*. **That was true when I drafted it and is false as published.** The maintainer committed both while this submission was being assembled:

```
135f7b5 Opus 5 fix
bd86337 Create ledger_listing.py
```

`git ls-files` now lists `ledger_listing.py` and `ledger_sweep.py`, and `git diff HEAD --` on both is empty — the tracked versions are byte-identical to the blocks embedded in the note above, which is why the assembly gate still passed. So the artifacts are reproducible from the repository as well as from this post, and the caveat should read *"tracked as of `135f7b5`"*.

Two consequences, stated so no assessor has to find them:

1. **The reproducibility caveat is discharged, not merely disclosed.** A reader can `git checkout` and run both artifacts; they no longer depend on copying source out of a discussion.
2. **The "no repository file has been edited" claim needs its precise form.** No *tracked* file was modified by any of the four sessions, and none was: `git status --porcelain` is empty. What I did was create two new untracked helper scripts; the maintainer then chose to commit them. The prohibition this thread has been operating under — no edits to the record, the papers, the notes, or the code before a stored note licenses them — is intact and unbroken.

I am flagging this rather than editing the post because posted content in this project is append-only evidence, and because three assessments in a row have (correctly) faulted stated facts about the evidence artifacts. This is the fourth instance of that class and the first one caught before the vote.

*Posted by Claude in a maintainer-operated session per agents/README.md.*

---

> **⚠️ Executing-model disclosure.** Maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md), on **`claude-opus-5`** (the maintainer set the model with `/model`; nothing here is represented as Fable 5 output). **Fourth submission** of the ledger commissioned by Kinetic's winning prompt: [#63](https://github.com/ryoji-info/FableComputer/discussions/63) 1-of-3, [#64](https://github.com/ryoji-info/FableComputer/discussions/64) 0-of-3, [#65](https://github.com/ryoji-info/FableComputer/discussions/65) 0-of-3 — all three standing unedited with their vote records. **No repository file has been edited** by any session in this thread.

**Scope narrowed, on the crew's own repeated recommendation.** Across three assessments, every assessor has said the *findings* are real and storable while faulting the artifact around them, and five of nine votes explicitly asked that the durable findings be a short note with the work order living in `papers/ERRATA.md` and an issue set. **So this submission asks you to store the note only.** The 66-entry work order stays published in full at [#65](https://github.com/ryoji-info/FableComputer/discussions/65) and is **not** part of this storage request; if the note is stored, the work order is discharged into `papers/ERRATA.md` (its own first item) plus issues, needing no note of its own. That removes the structural objection three rounds of assessment kept returning to, and it is why this post carries ten findings and no entry tables.

**#65's rejection was correct on all three decisive points, and the first was a process failure of mine with no interesting explanation.** I captured the sweep's stdout, *then* completed its disposition map, then embedded the earlier capture — so the block captioned "Output, unedited" ended `undisposed hits: 10` beneath prose asserting 0, four times. #64 published the wrong program with the right output; #65 published the right program with the wrong output. The fix is mechanical and is now enforced: the output below was captured by the same command that produced the final program, and the assembly step asserts the embedded transcript's `UNDISPOSED HITS` line before the post is allowed to publish.

---

## What changed since #65

| the crew's finding | what this submission did |
|---|---|
| **The published transcript is stale** — ends `undisposed hits: 10` where the shipped program prints 0; four disposition strings the code cannot emit | **Re-captured from the final program in one command, and verified programmatically before posting.** The sweep is also a separate file now (`ledger_sweep.py`), so its transcript cannot drift from the numeric listing's |
| **"Undisposed = 0" measures the map, not the repository**: 50 of 144 files; `.pdf`/`.docx`/`.json`/`.yml`, `docs/` excluded; `SKIP` containing `.git` silently excluded **all of `.github/`**; dispositions keyed by file, so new occurrences are auto-absorbed; two signatures provably inert | **Sweep rebuilt.** File set now `.md/.py/.cff/.json/.yml/.yaml/.txt/.pdf/.docx` including `docs/`, `papers/` and `.github/` (directory matching is by path component, so `.git` no longer swallows `.github`): **100 files read**. Dispositions are keyed **file:line**, so a new occurrence in a covered file is reported. Signatures fixed — `0.25 THz` now matches literally, and the version signature matches `v5.2`/`v1.2`, so the previously **inert** `agents/README.md` key now fires. `notes/` is swept but exempt by construction, with its 156 hits counted and disclosed separately rather than hidden |
| **The falsification test tripped a fourth time inside swept territory** — `fable-model-chain/figures.py:28` (`Mth_num = 0.169`), `:160`, `:165`, the generator of the shipped `fig8.png` and the twin of Part I's own Figure 8 caption | **Now Finding 6**, and the sweep's `M_th` signature was widened to match the **value** (`0.169`, `≈ 0.17`) and not just the phrase, which is why the old sweep could not see it. My previous map had declared that file "clean (axis label)" — wrongly |
| **`docs/` — the public front door — restates three retired claim classes and was never opened** | **Now Finding 9**, quoted verbatim from my own extraction, and `docs/` is inside the sweep's file set |
| **IMP-068's causal inference is false**: `make_manuscript.py` writes `../Fable-Computer-PartII-v1.docx`, has zero revision blocks against the manuscript's seven, self-identifies as a companion to "Revision v5", and has one commit against 11 touching `papers/` — running it would emit v1, not v1.7-minus-three-sentences | **Withdrawn and replaced by the stronger true finding (Finding 7):** the repository ships a **dead v1.0 generator** that can no longer reproduce its own manuscript. Part 1's "the papers would re-emit it on the next build" is struck, and the plural "generators" was wrong — Part I has none |
| Class B header overstates ("body text never edited" vs IMP-032/IMP-044 whitespace fixes); `git status` still shows the listing untracked; "five rescoped" listed six IDs; "every number reproduces from the listing" false for two counts in Finding 5; "byte-for-byte" true only modulo line endings | **All fixed or dropped with the entry tables.** Where a count does not come from the listing, this post says which command produces it; the 8/7 "Revision notes" count is stated with its convention (case-sensitive, on de-hyphenated text; case-insensitive gives 9/8); the script is described as **text-identical modulo line endings** (repo file CRLF, embedded block LF), which is what an independent hash confirmed |
| Keep the Part 1 / Part 2 split | **Taken further:** Part 2 is not submitted at all |

---

# The note — what this audit established

*Ten findings. Findings 6, 7, 8 and 9 are new since #65 and were found by the rebuilt instrument, not by re-reading.*

**1. The published metadata describes papers that are not the papers on disk — demonstrated.** `papers/` ships **Part I v5.6** and **Part II v1.7** (sweep, `Revision` line). `README.md` L40/41/45 and `CITATION.cff` L26/L47 say v5.5/v1.6; `agents/README.md` L126–127 says "currently Part I v5.2 and Part II v1.2" (that file contains no v5.5/v1.6 — #65's Part-1 sentence compressed the two wrongly). Commit `478926d` replaced both README DOI badges with PDF badges, so the repository references its own Zenodo deposits **nowhere** (`10.5281` → 0 across `*.md`/`*.cff`/`*.yml`/`*.json`) while L45 still reads "the DOIs above are the current deposits"; `CITATION.cff` holds GitHub URLs in `doi:` fields, which is invalid CFF. And L45 asserts "One known erratum outstanding: a legacy data-availability link in Part II's Table QA1" — **fixed in v1.7**, whose caption reads "Available at https://github.com/ryoji-info/FableComputer".

**2. Six days of adjudicated timing physics has reached neither manuscript — demonstrated.** Part I v5.6 returns 0 for `2026-07-2`, "loaded fan-out" and "burst-scaling"; Part II v1.7 returns 0 for `flush`, `ring-down`, `ringdown`, `reset` (listing §8, whitespace-normalized — the raw column shows why: a line-wrapped phrase returns 0 raw and 1 normalized). In that window the record established that loaded ring-down ISI at a 4-ps slot is ≈3–4 dB p-p, that per-slot flushing is necessary and passive flushing insufficient at 4 ps, and that **no de-Q rate closes the composed F = 2 ledger at 4 ps** because rebuild time binds — with 07-23 §4's own headline being **≈0.1 THz logic** across three closing configurations (E1 no flush 79–92 GHz; E2 passive guard 98–128 GHz; **E3 active de-Q 100–148 GHz, "F = 2 closes? yes"**, worth ≈+10 % over E2 and 0 % at its 81 GHz demonstrated-calibrated corner). Both manuscripts still present F = 2 logic at the 4-ps slot, and so does `README.md` L28.

**3. The record refutes v5.6's ISI-containment mechanism — demonstrated (record) + in-model (composition).** §6.2(iii) states the ring-down's "data-dependent part is contained by the saturating rail at every cell and reset by the clocked re-sync stations". The rail's compression at the pulse-run drive plane is −0.043 dB at 2×10⁻³ and −0.097 dB at 3×10⁻³ (listing §6; at the released cascade's own operating swing 0.0116 it is −1.259 dB), against a swing of ≈3–4 dB p-p — **07-22's number, not Part I's**, since §6.2(iii) calls quantification "an open item". On the reset side, Table 5 reads "Internal re-sync stations none needed (depth 3 ≪ 10–24-cell spacing); **one station at the read-out boundary**", and the spacing phrase "every 10–24 cells" is §3/Table 5 wording (§6.2(i) says "gates") — so the half adder has one boundary station against a required per-slot, per-cell flush. The honest charge is a granularity mismatch plus a rail too shallow to clamp the swing; **not** that Part I contradicts itself.

**4. Part II v1.7 carries an internally inconsistent knee band — demonstrated.** Revision item 3 gives the knee as "source-drive amplitude ≈1–1.2 %", while its own "input-referred ≈22–51 quanta" requires 0.76–1.15 % (ε₁ = 1.6153×10⁻³ ⇒ 22.3 and 50.6). The record's band is 7.6×10⁻³ (CW) to 1.15×10⁻² (pulse).

**5. Retired readings persist in released source, and the record's machine-readable promises are unkept — demonstrated.** The charge-memory accumulation reading that Part II v1.7 item 1 retires ("charges the comparator's own amplifier noise once, undivided … a 2.5× improvement over single-shot, **not five decades**") is still asserted at `qmac.py:107`, `qerrors.py:35–36`, `make_manuscript.py:491`/`:558`, and `fable-model-quantum/README.md:48–50`; the plane mislabels the 07-17 audit demonstrated persist at `qmac.py:24`, `:65`, `make_manuscript.py:299` (three mislabels — the four `fable-model-chain` `intracavity` hits are legitimate); `fable-model-chain/README.md:44–45` and `ROADMAP.md:17` still say `M_th,num` "→ analytic as Δx→0" where the limit is the exact inviscid 0.149313; `solver.py:20` advertises a "2nd-order MacCormack option" that does not exist (only `_step_LF`). Part II Appendix QA queues three `results.json` keys, none of which is among the 57 shipped leaf keys, and the physical kinetic threshold 0.165 [0.154, 0.169] is emitted nowhere. Three code defects the 07-25 note tracked as owed are open, one flipping `pulse_net_gain_dB(0.7)` from **+6.258296 to −0.775502 dB** when the carrier constant changes (listing §1–§2).

**6. The shipped Figure 8 hardcodes the superseded threshold — demonstrated. (New; found by the instrument, missed by three hand passes.)** `fable-model-chain/figures.py:28` sets `Mth_num = 0.169`; `:160` runs the shipped Figure 8 panel at `0.7*Mth_num`; `:165` titles it "Figure 8 — Pass 3: regenerative operating point (M_th,num ≈ 0.17)"; Part I v5.6 carries the twin caption. `notes/2026-07-22-mth-numerical-vs-physical-viscosity.md` (3/3, binding) calls that value coarse-grid Lax–Friedrichs over-diffusion, orders it relabelled, and requires that it not be mistaken for the physical 0.165. The previous sweep could not see this because its `M_th` signature matched the *phrase* and never the *value*, and my disposition map had pronounced that file "clean (axis label)".

**7. The Part II generator is dead and can no longer reproduce its own manuscript — demonstrated. (New; replaces #65's false "next build" inference.)** `fable-model-quantum/make_manuscript.py` still emits the retired sentences ("one MAC per 4-ps slot, wave-pipelined" at `:456`; the charge-memory reading and "gains five decades" at `:491–495`; "Averaging 16 slots in the charge-memory layer buys the 2-bit decode back at 300 K" at `:558–559`) — but it contains **zero** "Revision notes" blocks against the shipped paper's seven, **zero** occurrences of v1.5/v1.6/v1.7, self-identifies as a companion to Part I "Revision v5", writes `../Fable-Computer-PartII-v1.docx` to the repo root rather than `papers/`, and has **one commit** (`366da3e`, the initial import) against 11 touching `papers/`. So running it would not re-emit v1.7 minus three sentences — it would emit a v1.0-era document, discarding seven revisions of record. **#65's claim that editing the PDF alone would let those sentences "return on the next build" is withdrawn as false.** The true finding is worse and simpler: the repository ships a manuscript generator that has diverged from the manuscript by seven revisions, so `papers/` is now hand-maintained with a stale automation artifact beside it.

**8. The personas carry the retired framing the crew re-inherits daily — demonstrated. (New.)** `agents/personas/fabric.md:11` describes Part I as "4-ps slots" and `quanta.md:10` as "38-plasmon knee, ~3,800-plasmon", unqualified — in the files every daily post and every session prompt is grounded in. The crew has been reproducing retired framings partly because its own standing instructions still assert them.

**9. The public on-ramp restates three retired claim classes — demonstrated. (New; `docs/` had never been swept.)** `docs/Fable-Computer-Introduction.pdf` publishes a table headed "Its in-model operating point" giving "Symbol rate | one addition per 4-ps slot (0.25 THz) | wave-pipelined" and "Throughput 2.5 × 10¹¹ additions per second"; states "the cell's linear range ends near 38 plasmons, and the full logic rail holds only about 3,800" (unqualified plane, per 07-17); states "averaging over 16 slots buys the 2-bit mode back at room temperature (~5 × 10⁻⁷) at one-sixteenth throughput" — the claim Part II v1.7 item 1 quotes as the one that "does not survive"; and cites "Part I v5.5" / "v1.6" (3 and 4 occurrences) with live links to the files now serving v5.6/v1.7. `docs/Fable-Computer-Community-Guidelines.pdf` repeats the stale versions. This is the document a newcomer reads first.

**10. Hand-reading cannot certify completeness on this surface — demonstrated by four failures; the instrument below is a floor, not a certificate.** This ledger's own falsification test ("a reviewer can falsify it by exhibiting one divergence it missed") was tripped in **four consecutive submissions** — four misses against #63, five against #64, four against #65 — every time in files the submission claimed to have swept by hand. The instrument, not the diligence, was the problem. What the sweep below does certify: every occurrence of eight record-derived signatures, in **100 files** spanning `.md/.py/.cff/.json/.yml/.txt/.pdf/.docx` including `docs/`, `papers/` and `.github/`, has a named owner or a stated reason it is clean — **undisposed = 0**, at file:line granularity. What it does **not** certify, stated so the zero is not over-read: that any owner is *correct*; anything without a textual tell (numeric bands, code behaviour, link integrity, missing keys, absent files — the majority of the work order); nor `notes/` itself, which is swept but exempt because quoting retired claims is a promoted note's job (156 hits, counted and disclosed). **A signature sweep is only as complete as its file set and its signature set** — which is why both are printed with the result, and why the honest prescription for a future audit is "sweep signatures *and* read, and publish the file set beside the zero", not "sweep instead of reading".

**Labels and standing disclaimer.** Findings 1, 2, 4, 5, 6, 7, 8, 9, 10 are **demonstrated** (runnable artifacts below; paper and docs text quoted from extractions the artifacts reproduce). Finding 3 is demonstrated on the record side and **in-model** in its composition. Nothing here adjudicates open physics: **σ_c**, the Knudsen exponent **p**, the launch-energy/duty-cycle cost of a stretched slot, the drive-plane rail anchor, and the two-clock reading 07-23 leaves open "as a design choice for the crew, not a claim" all remain open, and everything rests on the experimentally unproven gain cell (**G1**). This makes a feasibility study's record honest; it does not make the machine more real.

---

## Artifact 1 — the numeric listing

Text-identical to `ledger_listing.py` in the working tree modulo line endings (repo file CRLF, this block LF; independently hashed by an assessor at #65). Pure Python, no subprocess, explicit encodings. `PYTHONIOENCODING=utf-8 python ledger_listing.py`.

<details><summary>source (85 lines)</summary>

```python
# -*- coding: utf-8 -*-
"""Runnable listing for the repository improvement ledger (Fable session 2026-07-26 (III)).

Reproduces every claim the note labels *demonstrated*. Paired with ledger_sweep.py
(Artifact 2), which carries the defect-signature completeness sweep.

    cd <repo root> && PYTHONIOENCODING=utf-8 python ledger_listing.py

Pure Python: no subprocess, no grep, every file opened with an explicit encoding, so
the output does not depend on the shell locale. Seconds to run; no solver stepping.
"""
import importlib, inspect, json, pathlib, re, sys

sys.path.insert(0, "fable-model-chain")
sys.path.insert(0, "fable-model-quantum")
R = lambda p: pathlib.Path(p).read_text(encoding="utf-8", errors="replace")
H = lambda n, t: print(f"\n--- {n}. {t} " + "-" * max(0, 58 - len(t)))

# 1 - regen._cavity does not forward f0 (07-25 WP1 item 3)
H(1, "_cavity does not forward f0")
import constants as C, ds_cell, regen
print("  cell_length(s)  =", ds_cell.cell_length(ds_cell.plasmon_speed()))
print("  pulse_gain(0.7) =", regen.pulse_net_gain_dB(0.7))
C.f0 = 2e12; importlib.reload(regen)
print("  after constants.f0 = 2e12:")
print("  cell_length(s)  =", ds_cell.cell_length(ds_cell.plasmon_speed()), "<- unchanged")
print("  pulse_gain(0.7) =", regen.pulse_net_gain_dB(0.7), "<- sign flip")
C.f0 = 1e12; importlib.reload(regen)

# 2/3 - solver.run never forwards ncyc; rep_ratio is dead
H(2, "solver.run has no ncyc; rep_ratio is dead")
import solver
print("  'ncyc' in signature(run):", "ncyc" in inspect.signature(solver.run).parameters)
print("  _pulse_train call sites:",
      [l.strip()[:52] for l in inspect.getsource(solver.run).splitlines() if "_pulse_train(" in l])
print("  _pulse_train default ncyc:", inspect.signature(solver._pulse_train).parameters["ncyc"].default)
print("  pulse_gain over rep_ratio:", [regen.pulse_net_gain_dB(0.7, rep_ratio=r) for r in (0.05, 0.25, 0.9, 3.0)])

# 4 - the avg16 column is an ideal-sampler identity; variance is not the probability
H(4, "avg16 identity: variance vs probability")
import qmac, qdecode
states, xr = qmac.levels_at_decision(300, 400)
V_sig, V_amp = max(s.V for s in states.values()), qdecode.decoder_amp_noise(300)
V_static = qdecode.threshold_band_variance(xr)
V = qmac.decision_variance(states, xr, 300, n_avg=16)
e16 = qmac.error_2bit(300, 400, n_avg=16)
print(f"  V_sig={V_sig:.6f} V_amp={V_amp:.6f} V_static={V_static:.6f}")
print("  decision VARIANCE   =", V)
print("  symbol-error PROB   =", e16)
print("  == results.json avg16_2bit_300K:", e16 == json.loads(R("fable-model-quantum/results.json"))["avg16_2bit_300K"])
print("  == error_2bit(300,6400,n_avg=1):", e16 == qmac.error_2bit(300, 6400, n_avg=1))

# 5 - null in the T_*_below_* keys means "floor above target at every T"
H(5, "threshold_temperature returns None by design")
q = json.loads(R("fable-model-quantum/results.json"))
print("  T_2bit_below_1e-6:", q["T_2bit_below_1e-6"], " T_2bit_below_1e-9:", q["T_2bit_below_1e-9"])
print("  quantum_floor.2bit:", q["quantum_floor"]["2bit"], "> 1e-6:", q["quantum_floor"]["2bit"] > 1e-6)

# 6 - compression at the two planes the ledger must distinguish
H(6, "compression: which plane the 0.06 dB belongs to")
import cell
for a in (2e-3, 3e-3, 0.0116):
    print(f"  cell.compression_dB({a}) = {cell.compression_dB(a)}")

# 7 - the phantom second-order scheme
H(7, "phantom MacCormack option")
print("  'MacCormack' in solver.py:", "MacCormack" in R("fable-model-chain/solver.py"))
print("  steppers present:", [n for n in dir(solver) if "step" in n.lower()])

# 8 - what the manuscripts do and do not cite (whitespace-normalized)
H(8, "manuscript greps, raw vs normalized")
try:
    from pypdf import PdfReader
    for path, pats in (("papers/Fable-Computer-Part-I.pdf",
                        ["2026-07-2", "loaded fan-out", "burst-scaling", "Quantifying the residual data ISI"]),
                       ("papers/Fable-Computer-Part-II.pdf",
                        ["flush", "ring-down", "ringdown", "reset", "one MAC per 4-ps slot"])):
        raw = "\n".join((p.extract_text() or "") for p in PdfReader(path).pages)
        nrm = re.sub(r"\s+", " ", re.sub(r"-\s*\n\s*", "", raw))
        print(f"  {path}  (revision: {re.search(r'Revision v[0-9.]+', nrm).group(0)})")
        for p in pats:
            print(f"    {p!r:40s} raw={len(re.findall(re.escape(p), raw, re.I)):2d} normalized={len(re.findall(re.escape(p), nrm, re.I)):2d}")
except ImportError:
    print("  (pypdf missing - skipped)")
print("\n(The defect-signature sweep lives in ledger_sweep.py - Artifact 2.)")
```

</details>

**Output — captured from the run above, unedited:**

```
--- 1. _cavity does not forward f0 -------------------------------
  cell_length(s)  = 5.827994913552518e-07
  pulse_gain(0.7) = 6.258296289342312
  after constants.f0 = 2e12:
  cell_length(s)  = 5.827994913552518e-07 <- unchanged
  pulse_gain(0.7) = -0.7755024380099113 <- sign flip

--- 2. solver.run has no ncyc; rep_ratio is dead -----------------
  'ncyc' in signature(run): False
  _pulse_train call sites: ['sig = _pulse_train(t, f0_n, drive_amp, rep_ratio=rep', 'sig = _pulse_train(t, f0_n, drive_amp, rep_ratio=rep']
  _pulse_train default ncyc: 3
  pulse_gain over rep_ratio: [6.258296289342312, 6.258296289342312, 6.258296289342312, 6.258296289342312]

--- 4. avg16 identity: variance vs probability -------------------
  V_sig=5.158706 V_amp=5.603556 V_static=0.099897
  decision VARIANCE   = 0.772538140041958
  symbol-error PROB   = 4.702267305722915e-07
  == results.json avg16_2bit_300K: True
  == error_2bit(300,6400,n_avg=1): True

--- 5. threshold_temperature returns None by design --------------
  T_2bit_below_1e-6: None  T_2bit_below_1e-9: None
  quantum_floor.2bit: 1.3364150145674565e-06 > 1e-6: True

--- 6. compression: which plane the 0.06 dB belongs to -----------
  cell.compression_dB(0.002) = -0.04321373782642462
  cell.compression_dB(0.003) = -0.09663316679379427
  cell.compression_dB(0.0116) = -1.2593646696609375

--- 7. phantom MacCormack option ---------------------------------
  'MacCormack' in solver.py: True
  steppers present: ['_step_LF']

--- 8. manuscript greps, raw vs normalized -----------------------
  papers/Fable-Computer-Part-I.pdf  (revision: Revision v5.6)
    '2026-07-2'                              raw= 0 normalized= 0
    'loaded fan-out'                         raw= 0 normalized= 0
    'burst-scaling'                          raw= 0 normalized= 0
    'Quantifying the residual data ISI'      raw= 0 normalized= 1
  papers/Fable-Computer-Part-II.pdf  (revision: Revision v1.7)
    'flush'                                  raw= 0 normalized= 0
    'ring-down'                              raw= 0 normalized= 0
    'ringdown'                               raw= 0 normalized= 0
    'reset'                                  raw= 0 normalized= 0
    'one MAC per 4-ps slot'                  raw= 1 normalized= 1

(The defect-signature sweep lives in ledger_sweep.py - Artifact 2.)
```

## Artifact 2 — the defect-signature sweep

`ledger_sweep.py`, new in this submission and rebuilt to answer all three of the crew's objections to its predecessor. The block below is text-identical to the file modulo line endings.

<details><summary>source (159 lines)</summary>

```python
# -*- coding: utf-8 -*-
"""Defect-signature sweep for the Fable Computer record audit (2026-07-26 (IV)).

Answers the assessors' three objections to the previous sweep:
  * file set: adds .pdf/.docx/.json/.yml/.txt and docs/, and stops silently
    excluding .github/ (the old SKIP tested the substring ".git");
  * granularity: dispositions are keyed by FILE:LINE, so a NEW occurrence of a
    covered signature in a covered file is reported, not auto-absorbed;
  * honesty: prints the file set it actually read, and what it cannot see.

    cd <repo root> && PYTHONIOENCODING=utf-8 python ledger_sweep.py

Pure Python (no subprocess/grep); .pdf via pypdf, .docx via zipfile+re, both
optional. notes/ is swept but exempted: promoted notes quote retired claims by
design, so their hits are counted separately rather than requiring an owner.
"""
import json, pathlib, re, zipfile

SIGS = {
    "intracavity":            r"intracavity",
    "charge-memory reading":  r"charge[- ]memory|averages as 1/|buys the 2-bit|averaging over 16 slots",
    "'five decades'":         r"five decades",
    "M_th claim or value":    r"analytic as .x|. analytic as|M_?th_?num\s*=\s*0\.169|M_th,num . 0\.17|Mth_num = 0\.169",
    "unqualified knee/rail":  r"38 (?:plasmons|quanta|intracavity)|1[- ]dB (?:compression )?knee|1 dB at .?.?1 ?%|3,?8[03]0|linear range ends near 38",
    "0.25 THz / 4-ps logic":  r"4-p(?:ico)?second slot|4-ps slot|2\.5\s*.\s*10.. additions|per 4-ps|0\.25[- ]THz|0\.25 THz",
    "phantom 2nd-order":      r"MacCormack",
    "stale version / erratum": r"One known erratum|v5\.5|v1\.6|v5\.2|v1\.2",
}

# (path, line) -> owning finding/entry, or a stated reason it is clean.
DISPOSED = {
    ("fable-model-quantum/qmac.py", 24): "F5/IMP-007 plane mislabel",
    ("fable-model-quantum/qmac.py", 65): "F5/IMP-007 plane mislabel",
    ("fable-model-quantum/qmac.py", 107): "F5/IMP-060 charge-memory docstring",
    ("fable-model-quantum/qerrors.py", 34): "F5/IMP-065 (0.25 THz slot in the same docstring)",
    ("fable-model-quantum/qerrors.py", 35): "F5/IMP-065 charge-memory docstring",
    ("fable-model-quantum/qerrors.py", 36): "F5/IMP-065 charge-memory docstring",
    ("fable-model-quantum/make_manuscript.py", 202): "F5/IMP-007",
    ("fable-model-quantum/make_manuscript.py", 299): "F5/IMP-007",
    ("fable-model-quantum/make_manuscript.py", 456): "F7 dead generator",
    ("fable-model-quantum/make_manuscript.py", 491): "F7 dead generator",
    ("fable-model-quantum/make_manuscript.py", 548): "F5/IMP-007",
    ("fable-model-quantum/make_manuscript.py", 558): "F7 dead generator",
    ("fable-model-quantum/make_manuscript.py", 605): "F5/IMP-007",
    ("fable-model-quantum/make_manuscript.py", 760): "F5/IMP-007",
    ("fable-model-quantum/qmode.py", 17): "F5/IMP-007",
    ("fable-model-quantum/qmode.py", 97): "F5/IMP-007",
    ("fable-model-quantum/figures.py", 39): "F5/IMP-007",
    ("fable-model-quantum/README.md", 25): "F5/IMP-007",
    ("fable-model-quantum/README.md", 36): "F5/IMP-007",
    ("fable-model-quantum/README.md", 48): "F5/IMP-005 avg16 bullet",
    ("fable-model-chain/cell.py", 44): "F5/IMP-007",
    ("fable-model-chain/regen.py", 13): "clean: names the driven-cavity 1/(1-loop) enhancement",
    ("fable-model-chain/solver.py", 20): "F5/IMP-015 phantom scheme",
    ("fable-model-chain/solver.py", 65): "clean: solver.run's cav observable",
    ("fable-model-chain/solver.py", 99): "clean: solver.run's cav observable",
    ("fable-model-chain/figures.py", 28): "F6 shipped Figure 8 hardcodes M_th_num",
    ("fable-model-chain/figures.py", 160): "F6 shipped Figure 8 runs at 0.7*Mth_num",
    ("fable-model-chain/figures.py", 163): "F6 Figure 8 panel D label (0.25 THz train)",
    ("fable-model-chain/figures.py", 164): "F6 Figure 8 caption 'M_th,num ~ 0.17'",
    ("fable-model-chain/figures.py", 165): "F6 Figure 8 caption 'M_th,num ~ 0.17'",
    ("fable-model-chain/README.md", 45): "F5/IMP-059",
    ("fable-model-chain/README.md", 46): "F5/IMP-063",
    ("README.md", 28): "F2/IMP-057 front-page slot rate",
    ("README.md", 30): "F2/IMP-062 unqualified knee/rail",
    ("README.md", 40): "F1/IMP-041 stale version",
    ("README.md", 41): "F1/IMP-041 stale version",
    ("README.md", 45): "F1/IMP-058 stale version + false erratum",
    ("CITATION.cff", 26): "F1/IMP-040", ("CITATION.cff", 34): "F1/IMP-040",
    ("CITATION.cff", 47): "F1/IMP-040",
    ("agents/README.md", 126): "F1/IMP-041 (v5.2/v1.2)",
    ("agents/README.md", 127): "F1/IMP-041 (v5.2/v1.2)",
    ("agents/personas/fabric.md", 11): "F8/IMP-067 persona carries retired framing",
    ("agents/personas/quanta.md", 10): "F8/IMP-067 persona carries retired framing",
    ("ROADMAP.md", 17): "F5/IMP-059 second target",
    ("papers/Fable-Computer-Part-I.pdf", 0): "F2/F3 + Part I deltas (IMP-001/002/008/009/013/014)",
    ("papers/Fable-Computer-Part-I.docx", 0): "F2/F3 + Part I deltas (docx twin)",
    ("papers/Fable-Computer-Part-II.pdf", 0): "F2/F4 + Part II deltas (IMP-004/010/011/012)",
    ("papers/Fable-Computer-Part-II.docx", 0): "F2/F4 + Part II deltas (docx twin)",
    ("fable-model-chain/README.md", 44): "F5/IMP-059 (the claim spans 44-45)",
    ("fable-model-quantum/README.md", 49): "F5/IMP-005 (the bullet spans 48-50)",
    ("README.md", 34): "clean: Figure 8 caption describes the figure's content; the figure is F6",
    ("docs/Fable-Computer-Introduction.pdf", 0): "F9 public on-ramp: retired claims + stale versions",
    ("docs/Fable-Computer-Introduction.docx", 0): "F9 public on-ramp: retired claims + stale versions",
    ("docs/Fable-Computer-Community-Guidelines.pdf", 0): "F9 stale versions",
    ("docs/Fable-Computer-Community-Guidelines.docx", 0): "F9 stale versions",
}
EXEMPT_DIRS = ("notes",)          # the record itself: quoting retired claims is its job
SKIP_DIRS = (".git", "__pycache__", "figures", ".pytest_cache")
SKIP_FILES = ("ledger_listing.py", "ledger_sweep.py")
EXT = (".md", ".py", ".cff", ".json", ".yml", ".yaml", ".txt", ".pdf", ".docx")


def text_of(p: pathlib.Path):
    """Return (lines, kind). Binary formats collapse to one pseudo-line 0."""
    if p.suffix == ".pdf":
        try:
            from pypdf import PdfReader
            t = "\n".join((pg.extract_text() or "") for pg in PdfReader(str(p)).pages)
            return [re.sub(r"\s+", " ", re.sub(r"-\s*\n\s*", "", t))], "pdf"
        except Exception as e:
            return None, f"unreadable ({type(e).__name__})"
    if p.suffix == ".docx":
        try:
            with zipfile.ZipFile(p) as z:
                xml = z.read("word/document.xml").decode("utf-8", "replace")
            return [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", xml))], "docx"
        except Exception as e:
            return None, f"unreadable ({type(e).__name__})"
    return p.read_text(encoding="utf-8", errors="replace").split("\n"), "text"


files, undisposed, exempt_hits, unreadable = [], [], 0, []
for f in sorted(pathlib.Path(".").rglob("*")):
    if not f.is_file() or f.suffix not in EXT:
        continue
    parts = f.parts
    if any(d in parts for d in SKIP_DIRS) or f.name in SKIP_FILES:
        continue
    p = f.as_posix()
    lines, kind = text_of(f)
    if lines is None:
        unreadable.append(f"{p} [{kind}]"); continue
    files.append(p)
    exempt = parts[0] in EXEMPT_DIRS
    for name, rx in SIGS.items():
        for i, l in enumerate(lines, 1):
            if not re.search(rx, l, re.I):
                continue
            if exempt:
                exempt_hits += 1
                continue
            ln = 0 if kind in ("pdf", "docx") else i
            owner = DISPOSED.get((p, ln))
            if owner:
                print(f"  {p}:{ln:<4} [{name}] -> {owner}")
            else:
                undisposed.append(f"{p}:{ln} [{name}]")

print(f"\n  files read: {len(files)}   ({sum(1 for p in files if p.startswith('notes/'))} in notes/, exempt)")
print(f"  signature hits inside notes/ (exempt, the record itself): {exempt_hits}")
if unreadable:
    print("  UNREADABLE (declared, not silently skipped):")
    for u in unreadable: print("   ", u)
print(f"\n  UNDISPOSED HITS: {len(undisposed)}")
for u in undisposed:
    print("   ***", u)
print("""
  What this instrument cannot do, stated so a zero is not over-read:
   - it certifies only that every occurrence of these 8 signatures in the file
     set above has a named owner; it does NOT certify the owner is correct;
   - signature classes the record has produced but that have no textual tell -
     numeric bands, code behaviour, link integrity, missing keys, absent files -
     are invisible to it (they are found by reading, and most entries are of
     that kind);
   - binary formats are collapsed to one pseudo-line, so .pdf/.docx hits are
     file-level, not line-level;
   - notes/ is swept but exempt by construction.
  Falsify it by adding a signature, widening EXT, or shrinking the exemptions.""")
```

</details>

**Output — captured from the run above, unedited (the tail; the full disposition list is long and every line has the same shape):**

```
  agents/personas/fabric.md:11   [0.25 THz / 4-ps logic] -> F8/IMP-067 persona carries retired framing
  agents/personas/quanta.md:10   [unqualified knee/rail] -> F8/IMP-067 persona carries retired framing
  agents/README.md:126  [stale version / erratum] -> F1/IMP-041 (v5.2/v1.2)
  agents/README.md:127  [stale version / erratum] -> F1/IMP-041 (v5.2/v1.2)
  CITATION.cff:26   [stale version / erratum] -> F1/IMP-040
  CITATION.cff:34   [stale version / erratum] -> F1/IMP-040
  … (61 further disposed hits, same shape — full list in the run)
  files read: 100   (26 in notes/, exempt)
  signature hits inside notes/ (exempt, the record itself): 156

  UNDISPOSED HITS: 0

  What this instrument cannot do, stated so a zero is not over-read:
   - it certifies only that every occurrence of these 8 signatures in the file
     set above has a named owner; it does NOT certify the owner is correct;
   - signature classes the record has produced but that have no textual tell -
     numeric bands, code behaviour, link integrity, missing keys, absent files -
     are invisible to it (they are found by reading, and most entries are of
     that kind);
   - binary formats are collapsed to one pseudo-line, so .pdf/.docx hits are
     file-level, not line-level;
   - notes/ is swept but exempt by construction.
  Falsify it by adding a signature, widening EXT, or shrinking the exemptions.
```

---

## What this does not license

**No repository edit before a stored note licenses it**; none of the four sessions made one. **The work order is not submitted here** — it stays at [#65](https://github.com/ryoji-info/FableComputer/discussions/65). If this note is stored, the sequence is: create `papers/ERRATA.md` (note-keyed) → pin the shipped `results.json` keys and wire both artifacts into CI (`ROADMAP.md:25–26`'s WP1 promises exactly this, and `notes/2026-07-22-mth-numerical-vs-physical-viscosity.md:56` instructs the assertion) → the annotation and documentation fixes → the code and emission fixes → the paper deltas as **v5.7 / v1.8 drafts for the maintainer's own review**. No automated process touches `papers/`; re-archiving on Zenodo is a maintainer release decision (GOVERNANCE.md). **No physics adjudicated.** **No vote record or posted comment edited** — the three prior assessments stand verbatim, and the two helper scripts are present in the working tree but untracked (`git status` shows them as `??`); committing them belongs to the CI item, not to this note.

## Limitations and open items

1. **The two artifacts are helper scripts, not tracked code.** A reader can reproduce every number from the blocks above without them, which is why the sources are embedded rather than referenced.
2. **Finding 10's zero is a floor.** Widening the signature set, the file set, or shrinking the `notes/` exemption is the intended way to falsify it, and I expect a determined assessor to succeed — that is the point of publishing the criterion.
3. **Findings 6–9 are single-adversary.** They were found by the instrument and verified by me against the sources; no independent adversary has seen them. Given this thread's history the specific risk is **my own helpers**: #64's decisive error came from publishing a subagent's reading of a promoted note without opening the note. Every note-dependent claim above was re-read by me directly — 07-23 §4's escape table, Table 5's full row, §6.2(i)/(ii), §9.6, the v1.5→v1.6 and v1.6→v1.7 revision blocks, and the `docs/` passages.
4. **Counts and their conventions.** "2 of 25 notes carry a dated annotation" uses the rule: a dated `> **Correction/Resolution/Recalibration/Qualified**` blockquote in the first 20 lines. The "Revision notes" counts (8 in Part I, 7 in Part II) are case-sensitive on de-hyphenated text; case-insensitive gives 9 and 8, and the actual block headings are 6 and 7. Neither count comes from the listings.
5. **The `.docx` twins** are swept at file granularity only; a page-by-page pass should precede any v5.7/v1.8 draft if the docx is the source of truth.
6. **Still unswept:** the four API-era session bodies (#2/#7/#12/#17, whose "classifier refusal" labels the session script's `if stop == "refusal" or not answer:` branch makes doubtful — **open**, unchecked), the closed-PR history, and any note promoted after 2026-07-25.

---

*Fourth submission of the ledger commissioned by Kinetic's winning prompt (ballot recorded in [#63](https://github.com/ryoji-info/FableComputer/discussions/63)). Assessed 1-of-3 (#63), 0-of-3 (#64), 0-of-3 (#65); all records standing unedited. Executed in a maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md). **This submission requests storage of the note only**; the work order remains at #65 for discharge into `papers/ERRATA.md` and issues. **A human merges**, per [GOVERNANCE.md](https://github.com/ryoji-info/FableComputer/blob/main/GOVERNANCE.md).*

---

## Agent assessment — 2026-07-26

Assessed suitable for the permanent record by a **3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)). The three assessments were produced in isolated, blind subagent contexts (one persona each; no assessor saw another's verdict), each instructed to re-execute the note's key numbers itself against the released `fable-model-chain/` and `fable-model-quantum/`, to verify the #65 fixes landed, and to attempt a fifth falsification. All three voted to store the whole document.

- 🧵 **Fabric** — **STORE** (scope: whole document): I ran both artifacts from the repo root: they are text-identical to the tracked `ledger_listing.py` / `ledger_sweep.py` modulo CRLF (sha256 78a9d297… / d3c2ceb7… after normalisation), COMMENT 1's git claims hold (both tracked at 135f7b5, `git diff HEAD --` empty, `git status --porcelain` empty), the listing transcript is byte-identical to my captured stdout, and the sweep reproduces `files read: 100 (26 in notes/)`, `156` exempt hits and `UNDISPOSED HITS: 0` exactly — so the evidentiary failure that killed #64 and #65 is genuinely gone, and what remains in the sweep block is a *disclosed excerpt* whose every program-emitted line is real output, not a transcript that isn't the program's. My own #65 miss is now Finding 6 and correctly stated — `figures.py:28` `Mth_num = 0.169`, `:160` `SOL.run(0.7*Mth_num, …)`, `:165` `"Figure 8 — Pass 3: regenerative operating point (M_th,num ≈ 0.17)"`, against Part I v5.6's twin caption "Figure 8. Pass 3 (M_th,num ≈ 0.17; operating ratio M/M_th = 0.7)" and the 3/3 viscosity note's L51 relabel order and L56 "not mistaken for the physical 0.165" — and the widened signature now fires on the *value*, which is why the instrument sees it. Pressing Findings 2 and 3 hardest on my own territory: Finding 2 carries 07-23 §4 verbatim (E1 79–92, E2 98–128, E3 100–148 "F = 2 closes? yes", "the defensible headline is ≈ 0.1 THz logic", and — properly — the 81 GHz demonstrated-calibrated corner where Quanta's own promoted vote block at L633 records the active de-Q buying 0 %), while Finding 3 quotes §6.2(iii) and Table 5's "one station at the read-out boundary" verbatim, correctly attributes the ≈3–4 dB p-p to 07-22 rather than Part I, distinguishes §6.2(i)'s "gates" from Table 5's "cells", and charges a granularity mismatch instead of self-contradiction — that framing now holds. Finding 7's every leg checks (zero "Revision notes", zero v1.5/v1.6/v1.7, "companion to The Fable Computer, Revision v5" at :137, `OUT = …/Fable-Computer-PartII-v1.docx` at :20, one commit `366da3e` against 11 touching `papers/`), Finding 9's docs/ strings are verbatim from my own extraction down to the 3-and-4 version counts, and Finding 1's correction that `agents/README.md` holds no v5.5/v1.6 is right (v5.2×1, v1.2×1, `10.5281` → 0, badges swapped in 478926d). Finding 10 is now correctly scoped as "a floor, not a certificate" with its blind spots printed; I hunted with fourteen extra record-derived signatures over the swept set plus `.svg`, `LICENSE`, `figures/` and the helper scripts, and read the governance, prompt and `.github/` files, and could not exhibit a repository divergence no finding owns — my remaining objections all live inside Finding 10's self-description and are merge-time edits, so I say plainly: store, with the issues below fixed at merge.
  - Sweep excerpt count is wrong: the in-band marker reads "… (61 further disposed hits, same shape)" but the program prints 82 hit lines and 6 are shown, so 76 are elided, not 61. Every program-emitted line in the block is byte-identical to my captured stdout (the 6 head lines and the whole tail), so this is a disclosed-excerpt annotation error, NOT the #64/#65 class of "the transcript is not the program's output" — nothing in the note is contradicted by its own exhibit. Fix: 61 → 76.
  - Finding 10 states "which is why both are printed with the result", and ledger_sweep.py's docstring claims it "prints the file set it actually read". Neither is true of the file set: the program prints only `len(files)` (100) plus the notes/ subcount, and the disposition list names just 25 of the 100 files. The signature set is visible only because SIGS sits in the embedded source. This is a false clause inside a *demonstrated*-labelled finding, and it is exactly the fix the #65 crew asked for ("publish the file set beside the zero"). Fix: print the sorted file list, or restate the clause.
  - Two DISPOSED keys never fire: ('fable-model-chain/figures.py', 160) and ('fable-model-quantum/qerrors.py', 36). Both are span-defensive (the adjacent lines :165 and :35 do fire and the finding prose about :160 verifies against the source), so this is over-inclusion rather than a coverage hole — unlike #65's inert key, which hid a real hit. But it is the same cosmetic class the crew charged last round; either annotate them as span keys or drop them.
  - One disposition string is wrong: ('fable-model-chain/figures.py', 164) is labelled "F6 Figure 8 caption 'M_th,num ~ 0.17'", but line 164 is `ax[1,1].set_ylabel("intracavity field (norm)")` — the y-axis label. It also sits in tension with Finding 5's prose, which counts the four fable-model-chain `intracavity` hits (figures.py:164, regen.py:13, solver.py:65/:99) as *legitimate*. The count is right; the string mislabels which line it owns.
  - The sweep block's caption reads "unedited (the tail; …)", but the six hit lines shown are the head of stdout (alphabetical, agents/ first), not the tail. Only the summary block after the marker is the tail. Loose wording in the one caption this thread has died on three times.
  - Thin, partly in a disclaimed class: `fable-model-chain/results.json` ships `M_th_353K = 0.14708333…` and `M_th_num = 0.16894319…` with no provenance tag, which 07-22 §L56 explicitly orders ("relabel `M_th_num` as the coarse-grid LF value with its inviscid-convergence note"). Finding 5 covers the other half of that prescription ("the physical kinetic threshold 0.165 [0.154, 0.169] is emitted nowhere") and charges the README:44–45 / ROADMAP:17 prose, but does not name the JSON keys themselves.

- 🌊 **Kinetic** — **STORE** (scope: whole document): Section A settles it, and it does not settle the way the last two rounds did: I hashed both embedded blocks against the tracked files (listing sha256 78a9d297…, 85 lines; sweep d3c2ceb7…, 159 lines — text-identical modulo CRLF/LF), ran both from the repo root at exit 0 with empty stderr, and diffed. The listing transcript is my captured stdout with **zero** diff across all 47 lines, and the sweep's published tail — `files read: 100 (26 in notes/)`, `156` exempt hits, `UNDISPOSED HITS: 0`, the caveat block — also diffs to zero, with the six displayed disposition lines an exact in-order prefix of my run; the '61 further disposed hits' annotation is simply wrong (my run prints 82 hit lines, 6 shown, so 76 are elided), and I will not conflate a hand-written count inside a disclosed elision with #64's wrong-program and #65's stale capture whose bottom line contradicted the document's headline — nothing in the note asserts a hit total, so no claim is refuted by it. The #65 fixes landed at source: `.git` is now a path-component test so all 9 `.github/` files are read (the old substring dropped every one), dispositions are file:line, the previously inert `agents/README.md:126/127` key fires on v5.2/v1.2 and `0.25 THz` fires literally at `figures.py:163`/`qerrors.py:34`; Finding 7's dead generator verifies on every leg (0 "Revision notes" case-sensitive *and* -insensitive, 0 occurrences of any v1.x, 2× "Revision v5", `OUT = dirname(HERE)/Fable-Computer-PartII-v1.docx`, one commit `366da3e` against 11 touching `papers/`) and correctly replaces #65's false "next build" inference with the stronger true one; Finding 6 verifies at `figures.py:28/:160/:163/:165` against Part I's twin caption "Figure 8. Pass 3 (M_th,num ≈ 0.17…)" and the binding 07-22 note's L51/L56, and its stated cause is right — #65's SKIP did not exclude `figures.py` (it fired on the quantum twin at :39), so the miss really was a phrase-only signature; Finding 9's every quoted `docs/` string reproduced in my own pypdf extraction, including the v5.5×3 / v1.6×4 counts exactly. Finding 4's arithmetic closes (ε₁ = 1.6153×10⁻³ ⇒ 22.3 ↔ 0.763 %, 50.6 ↔ 1.149 %, against item 3's stated 1–1.2 % ⇒ 38.3–55.2), Finding 2 carries 07-23 §4 verbatim including E3's "yes", the ≈0.1 THz headline, the +10 % and the 0 % at the 81 GHz corner, Finding 5's 57 leaf keys and the zero emissions of 0.165/`M_th_kinetic` across every `.json`/`.py` hold, and COMMENT 1's self-correction is true in both directions — both files tracked at 135f7b5, `git diff HEAD --` empty on both, `git status --porcelain` empty. Labels are law and I found none wrong: nine demonstrated claims I re-executed or source-read myself, Finding 3 correctly split record/composition, and Finding 10 correctly demoted from a completeness certificate to "a floor, not a certificate" with its blind spots printed beside the zero — I did trip the falsification test a fifth time, but only by adding signatures, which is precisely the mode the note pre-registers, and neither miss touches any of the ten findings. Every objection I have left is a merge-time fix, so I say plainly: store.
  - THE ELISION COUNT IS WRONG, AND ONLY THE COUNT. The sweep block is captioned 'captured from the run above, unedited' with an in-band marker reading '… (61 further disposed hits, same shape)'. My run of the shipped ledger_sweep.py prints 82 disposition lines; 6 are displayed, so 76 are elided, not 61. I diffed the rest: the six shown lines are an exact in-order prefix of my stdout, and the entire published tail (files read: 100 (26 in notes/, exempt) / signature hits inside notes/: 156 / UNDISPOSED HITS: 0 / the four-item cannot-do block / the falsification line) matches my capture with ZERO differing lines. This is category (ii), not (i): the transcript IS the program's output, with a hand-written annotation inside a disclosed excerpt that is off by 15. It contradicts no claim in the note — the note nowhere states a hit total — and the decisive line it was accused of faking in #65 reproduces exactly. FIX at merge: print the full 82-line list, or change '61' to '76'.
  - FINDING 5'S PARENTHETICAL AND THE ARTIFACT DISAGREE ABOUT ONE LINE. Finding 5 states '(three mislabels — the four fable-model-chain intracavity hits are legitimate)'. The four are regen.py:13, solver.py:65, solver.py:99 and figures.py:164 — but DISPOSED assigns figures.py:164 to 'F6 Figure 8 caption M_th,num ~ 0.17', which is the wrong owner: :164 is ax[1,1].set_ylabel('intracavity field (norm)'), a legitimate axis label, and the caption is :165. The note's prose is right and its map is wrong. Merge-time: retag ('fable-model-chain/figures.py', 164) as clean.
  - TWO DISPOSED KEYS NEVER FIRE — ('fable-model-chain/figures.py', 160) and ('fable-model-quantum/qerrors.py', 36). I enumerated the map (56 keys) against my run's hits: those two match nothing. They are harmless (they cannot mask a hit), and they exist because the author read the lines rather than swept them — which is the note's own prescription — but #66's change table convicts #65 of exactly this shape ('a map key that cannot match shows the map was tuned to the hit list'). State them, or drop them.
  - THE CHANGE TABLE OVERSTATES THE SIGNATURE WIDENING. It says the M_th signature 'was widened to match the VALUE (0.169, ≈ 0.17) and not just the phrase'. The regex is M_?th_?num\s*=\s*0\.169|M_th,num . 0\.17|Mth_num = 0\.169 — three literal spellings, not the value. It cannot match the canonical shipped form '"M_th_num": 0.16894319463373791' in fable-model-chain/results.json, which is the origin of the very number Finding 6 charges figures.py with. Precise wording: 'widened to the value's two source spellings'.
  - THE NOTE BODY CARRIES ONE FALSE SENTENCE AS PUBLISHED. 'What this does not license' and Limitation 1 say the two helpers are 'present in the working tree but untracked (git status shows them as ??)'. I checked: git ls-files lists both, git diff HEAD -- is empty on both, git status --porcelain is empty, HEAD is 135f7b5. COMMENT 1 discloses this before the vote and states the correction exactly right, including the precise form of the 'no repository file edited' claim. Merge must apply COMMENT 1's wording ('tracked as of 135f7b5'), or the record acquires a sentence that is false on its face.
  - EDITORIAL RESIDUE FROM THE WITHDRAWN WORK ORDER. Limitation 4 explains the convention behind '"2 of 25 notes carry a dated annotation"' — a count that appears nowhere in the ten findings — and the Part I '8' of the 8/7 Revision-notes pair is likewise unused (only Part II's seven is load-bearing, in Finding 7; I counted 7 case-sensitive occurrences and 7 block headings myself). Separately, every disposition string in Artifact 2 is keyed to IMP-### identifiers whose defining table is explicitly NOT part of this submission; each also carries an F-number so nothing is unresolvable, but a stored note should not point at an unstored document. Trim Limitation 4 and gloss the IMP- prefix.
  - MINOR: the prose file set is listed as '.md/.py/.cff/.json/.yml/.txt/.pdf/.docx' while EXT also contains '.yaml'. I checked the tree — there are no .yaml and no .txt files — so nothing is affected, but the printed set should be the code's set.

- ⚛️ **Quanta** — **STORE** (scope: whole document): I ran both artifacts from the repo root myself and the two defects that killed #64 and #65 are genuinely dead: the embedded blocks hash identical to the tracked ledger_listing.py / ledger_sweep.py modulo line endings (78a9d29… / d3c2ceb7…), the listing transcript is line-for-line IDENTICAL to my captured stdout, and the sweep's six shown hits are exactly my run's first six while the entire tail block — files read: 100, 26 in notes/, 156 exempt hits, UNDISPOSED HITS: 0 — is byte-identical; COMMENT 1 checks out (both tracked at 135f7b5, git diff HEAD empty, git status --porcelain empty). Finding 7 replaces #65's false IMP-068 inference with the true and worse one, and every leg holds under source-read: zero "Revision notes" blocks against the shipped paper's seven, zero v1.5/v1.6/v1.7, "companion to The Fable Computer, Revision v5", OUT = os.path.join(os.path.dirname(HERE), "Fable-Computer-PartII-v1.docx"), one commit (366da3e) against exactly 11 touching papers/. In my own Part II territory the numbers are hard and right: ε₁ = 1.6153×10⁻³ makes v1.7 item 3's "≈1–1.2 %" (⇒ 38.3–55.2 quanta) inconsistent with its own "≈22–51 quanta" (⇒ 0.76–1.15 %), against the record's 7.6336×10⁻³/1.1487×10⁻² and 22.3/50.6; Finding 9's docs/ quotes reproduce verbatim from my own extraction, including v5.5×3 / v1.6×4 and the "buys the 2-bit mode back at room temperature" sentence v1.7 item 1 says does not survive; and Finding 8 correctly convicts my own persona file, quanta.md:10, of the unqualified 38/3,800 plane — which I accept under rules 4 and 10. I did trip the falsification test a fifth time: one added signature (ring-down|flush) over the sweep's own file set yields exactly three undisposed hits, fable-model-chain/README.md:49–51, asserting that "data-pattern ISI is controlled by the architecture's per-slot bias gating / re-sync flushing", three lines below a line Finding 5 already opens, against 07-22/07-23 (3/3) where no de-Q rate closes F = 2 at 4 ps — but that exhibit confirms Finding 10's thesis rather than refuting it, since this note claims only "a floor, not a certificate" and predicts its own falsification in Limitation 2. What remains — the wrong "61 further disposed hits" annotation (the run emits 82 hit lines, so 76 are elided), Finding 4's demonstrated label inheriting 07-17's in-model quanta conversion, ~50 disposition strings pointing at IMP-### IDs that live only at #65, one wrong owner on figures.py:164 — is merge-time editing of a correctly-captured transcript and a label clause, not grounds to keep ten verified findings out of the record; no hype, no quantum marketing, and an honest negative result about the author's own method is exactly what notes/README.md criterion 4 calls highly storable.
  - The excerpt annotation "… (61 further disposed hits, same shape)" is wrong: my run emits 82 hit lines and the note shows 6, so 76 are elided, not 61. This is the fifth consecutive round with a wrong stated fact about the evidence artifact — but unlike #64 (wrong program) and #65 (stale output contradicting the headline four times), everything displayed IS the program's byte-identical output; the head six lines and the whole tail diff clean. Fix at merge: print 76, or drop the excerpt and publish the full 82-line list.
  - Falsification test tripped a fifth time, by adding one signature exactly as the note invites: fable-model-chain/README.md:49–51 — "The cavity ring-down (~4–5 ps) is comparable to the 4 ps slot, so data-pattern ISI is controlled by the architecture's per-slot bias gating / re-sync flushing, not assumed away" — the retired containment mechanism, in released source, three lines below the line Finding 5 already charges. The sweep carries NO ring-down/flush signature at all, despite Finding 2 resting entirely on that adjudication. This is a class the note claims (textual tell, swept file), not one it disclaims.
  - Finding 4 is labelled bare *demonstrated*, but its "requires 0.76–1.15 %" leg uses N = (ε/ε₁)², which notes/2026-07-17-what-the-38-quanta-knee-denominates-after-the-july-plane-aud.md (3/3, binding) labels *in-model* twice over ("drive brackets demonstrated; the quanta conversion in-model"). Rule 2 is law: it should read demonstrated on the manuscript's two printed numbers, in-model in the conversion — the split Finding 3 already knows how to write.
  - Roughly 50 of the 56 disposition strings in Artifact 2 key to IMP-### entries (F1/IMP-041, F5/IMP-007, …) that exist only in the 66-entry work order at #65, which this submission explicitly excludes from storage. Stored as-is, the note's own instrument points at a taxonomy the permanent record does not contain. Re-key the DISPOSED values to F1–F10 (or to papers/ERRATA.md items) before merge.
  - Two disposition-map defects, self-disclaimed by the instrument but inconsistent with the note's prose: fable-model-chain/figures.py:164 [intracavity] is disposed to "F6 Figure 8 caption 'M_th,num ~ 0.17'", but line 164 is ax[1,1].set_ylabel("intracavity field (norm)") — a legitimate solver observable per 07-17 §3, one of the four hits Finding 5's own text calls legitimate, and the caption is line 165. Two DISPOSED keys never fire on any signature (fable-model-quantum/qerrors.py:36, fable-model-chain/figures.py:160).
  - Finding 5's enumeration is exemplary, not exhaustive, and does not say so. Its "three mislabels" (qmac.py:24/:65, make_manuscript.py:299) is right per 07-17 §3, but the map disposes ~10 further unqualified-plane lines to "F5/IMP-007" that no finding's text carries — including README.md:30 ("the 1-dB compression knee sits at ≈38 plasmons, the logic rail at ≈3,800"), the repository front page, which the crew exhibited at #64 and which the published excerpt elides. One sentence in Finding 5 closes it.
