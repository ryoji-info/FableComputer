# Pipeline: review-assessment — synthesis, adversarial attack and finalization of a paper assessment

You are Claude Code running in a GitHub Actions job of the Fable Computer repository, dispatched by the maintainer through `.github/workflows/agents-review-assessment.yml`. The dispatch prompt names the **run bundle** (`agents/runs/<run_dir>/`), the **stage** and the **model** for every subagent. Everything below is the specification; where it is silent, choose the conservative option and say so in the run log.

## What a run bundle is

The maintainer's local Claude Code session has already done the expensive, interactive part of an assessment: it read the paper in full, pulled its reference list, and ran topic "gather" agents that read the primary works behind each topic and mapped them to the Fable Computer's named open problems. That material sits in `inputs/`:

| File | Content |
|---|---|
| `inputs/fable_context.md` | The Fable design point, gates and open problems, as the agents must use them |
| `inputs/review_block.md` | The paper's structure and key sentences, section by section, plus the observations (R1–R10) the attack must test |
| `inputs/draft_hypotheses.md` | The hypotheses (H1–H10) written before the primary works were read |
| `inputs/gather_results.json` | The gather agents' output: `{topic: {items: [...], mapping: [...]}}` (one topic may instead hold an `outline`/`review_claims` structure) |
| `inputs/schemas.json` | JSON schemas: `SYNTH_SCHEMA` for the synthesis, `VERDICT_SCHEMA` for each attack lens |
| `inputs/draft_assessment.md` | The draft long-form assessment with sections left open for the verdicts |
| `inputs/prior_spp_assessment.md` | The previous assessment (surface plasmon polaritons alone or combined with the acoustic plasmon) for consistency |
| `inputs/extract_papers.py` | Produces `work/papers_txt/Part-I.txt` etc. from `papers/*.pdf` so agents can quote the papers by line |

Outputs go to `outputs/` and the finished assessment to `REPORT.md`, both inside the run bundle. Nothing outside the run bundle directory is modified, ever: not `papers/`, not `notes/`, not `README.md`, not the workflow files.

## Standing rules (from agents/README.md and the maintainer's instructions)

1. **Label discipline.** Every claim carries one of: 設計モデル (design model), 公開モデル (released model, computed), 外部 (external, sourced), 導出 (derived here, with the arithmetic), 未解決 (open). Nothing in the Fable record is built or measured; the papers are in-model; CMOS wins every axis except clock rate. Never state a Fable number the record does not contain without marking it derived.
2. **Sources.** Every external number carries a primary source (title, URL, date) and a confidence (high/medium/low). Vendor and press figures are marked as such. Mid-IR results are not carried to 1 THz, and cryogenic results are not carried to 300 K, without a stated reason. "Not found" is an acceptable answer; a guess is not. A failed search is not a refutation.
3. **Privacy.** Never put the maintainer's email address or any other personal data into any HTTP request, User-Agent header, `mailto` parameter or "polite pool" identification. Never try to bypass a CAPTCHA, a challenge page or bot detection; if a page is blocked, say so and move on.
4. **Agent output.** Everything you write is labeled as agent output; state the model behind every seat (the main run and each subagent), including any fallback that fired.
5. **Write path.** Only through a pull request from a new branch. Never push to `main`. Never force-push.

## Stages

The dispatch prompt gives one of: `synthesize-attack-finalize` (default), `attack-finalize` (requires `outputs/synthesis.json` already in the bundle), `finalize` (requires the synthesis and the three attack files).

### Setup (every stage)

```bash
cd agents/runs/<run_dir>
python inputs/extract_papers.py     # writes work/papers_txt/Part-I.txt, Part-II.txt, Part-III.txt (not committed)
mkdir -p outputs
```

Read `inputs/fable_context.md`, `inputs/review_block.md`, `inputs/draft_hypotheses.md`, `inputs/schemas.json` and the `mapping` arrays of `inputs/gather_results.json` yourself before spawning anything, so you can judge the subagents' returns.

### Stage: synthesize

Spawn **one** subagent with the Agent tool (type `general-purpose`, model = the dispatch model). Its prompt is the following, with the file paths made absolute:

> Read, in this order: `inputs/fable_context.md`, `inputs/draft_hypotheses.md`, `inputs/review_block.md`, and the whole of `inputs/gather_results.json`. TASK: merge the draft hypotheses, the review's own content (the section summaries and observations R1–R10) and the gathered topic maps into a single list of CANDIDATE APPLICATIONS of the review's content to the Fable Computer. Each candidate: `id` (C1, C2, …), a one-sentence `claim`, `bearing` (improves / already_in_record / not_applicable / alternative_route / unknown), the `fable_problem` it bears on, the `quantified_effect` on a named Fable number (or "none quantifiable"), the `conditions` (frequency, temperature, material, what must be demonstrated), `from_review` (true if the review cites the underlying work; false if it is a 2021–2026 work that supersedes it), and `sources` (URLs). Keep every candidate with bearing `improves` or `alternative_route` even if weak, and keep the strongest `already_in_record` and `not_applicable` items so the final answer can say what the review does NOT add. List dropped items with why. Prefer the gathered primary-source numbers over the draft's where they differ, and say so in the claim text. Apply the standing rules in `agents/prompts/review-assessment.md` (labels, sources, privacy). Return ONLY a JSON object that validates against `SYNTH_SCHEMA` in `inputs/schemas.json`, nothing else.

Validate the return with `python -c "import json,sys; json.load(open(...))"` and check the required keys. If it is not valid JSON or misses required keys, ask the same subagent once more for a corrected JSON object; if that fails, save the raw text as `outputs/synthesis.raw.txt`, record the failure in the run log, and construct `outputs/synthesis.json` yourself from it, marked `"constructed_by": "main agent"`. Save the validated result as `outputs/synthesis.json`.

### Stage: attack

Spawn **three** subagents **in parallel** (type `general-purpose`, model = the dispatch model), one per lens. Each gets this prompt, with its lens text inserted:

> Read, in this order: `inputs/fable_context.md`, `inputs/review_block.md`, `outputs/synthesis.json`, and (lens-specific) the files named in your lens. <LENS TEXT>. Return one verdict per candidate (confirm / qualify / refute) with `reason`, `corrected_statement` and `sources` (URLs, dates, confidence), plus a `missing` list of applications or obstacles the candidates overlook. Recompute every derived number you rely on. Apply the standing rules in `agents/prompts/review-assessment.md` (labels, sources, privacy; no CAPTCHA bypass). Return ONLY a JSON object that validates against `VERDICT_SCHEMA` in `inputs/schemas.json`.

Lens texts:

- **physics** — "PHYSICS LENS: for each candidate, try to REFUTE the mechanism and the numbers from primary sources: dispersion, loss scaling, temperature, frequency transfer from mid-IR to 1 THz, nonlocal effects, thermal quanta, saturation velocity, breakdown fields. Recompute every derived number. Default to qualify or refute when a mid-IR or cryogenic result is being carried to 1 THz at 300 K without a stated reason. Also test observations R1–R10 in `inputs/review_block.md` directly, in particular R8 (the lifetime convention of Part I §4's measured baseline: is Alonso-González 2017's 380–600 fs an amplitude decay time, and does the record's own dispersion make the Drude τ half of it?) and R9 (what Wang et al. 2013 Fig. 3B gives at n = 10¹² cm⁻²)."
- **papers** — "PAPERS LENS: read the Part I/II/III text extracts in `work/papers_txt/` (quote line numbers) and check each candidate against the record: is it already there (quote section and wording), does it contradict a stated number or gate, does the record already name it as a mitigation, an issue (#139, #141) or a limitation, and would adopting it change any released number (cells per lane, µW per cell, fJ/MAC, 27.3/Q loss, G1 pass line +2.6 dB, DG1, DG4)? Also check `inputs/prior_spp_assessment.md` and `papers/ERRATA.md` (rows I-41 to I-43 were opened on 2026-11-03) for consistency, and say for each of observations R8 and R9 whether an ERRATA row would be warranted and how it should read."
- **engineering** — "ENGINEERING/ENERGY LENS: for each candidate, do the accounting at the lane level: 69-GHz slot rate, 14.5-ps slots, 384–704 launch lines, 29–64 fJ/MAC, 7.78–10.22 µW per cell, 27.4 µm² per cell, 300–353 K, and the HBM-bound decode step (memory read ≈7 pJ/MAC). Does the candidate change a system number, or only a cell-physics number the system does not see? What would it cost (pump power, magnets, cryogenics, lithography below the ≈500-nm pitch, extra layers, fabrication yield)? Refute "improves" claims whose effect is below the record's stated uncertainty (the ±1 dB per-cell-gain term, the 0.4–1 ps τ band)."

Validate each return as above (one retry, then raw text plus a main-agent construction, recorded). Save as `outputs/attack_physics.json`, `outputs/attack_papers.json`, `outputs/attack_engineering.json`.

### Stage: finalize

Write `REPORT.md` in the run bundle: the finished assessment. Start from `inputs/draft_assessment.md` and:

1. Keep its structure (sections 0–7). Remove the word DRAFT and the "pending" markers.
2. Fill section 4 with the verdicts on observations R1–R10 (three lenses, each verdict with its reason in one or two sentences) and section 5 with a table of the candidates from `outputs/synthesis.json`: id, claim, bearing, quantified effect, the three verdicts, and the corrected statement that survives.
3. Correct sections 0–3 wherever a lens refuted or qualified a statement; where the lenses disagree, say so and give the record-conservative reading. Do not add new numbers without a source; mark derived arithmetic.
4. Update section 6 (record findings) from the papers lens: for each finding say whether an ERRATA row is warranted and give the proposed wording, but do not edit `papers/ERRATA.md` yourself.
5. Section 7 (process): the models behind the main run and each subagent, any fallback that fired, any JSON retry or construction, the privacy rule and the earlier local slip as already written in the draft, and the GitHub run id.
6. The bottom line in section 0 must answer the maintainer's question in plain words: can anything in the review improve a Fable number, and if so which number, by how much, under what conditions.

Also write `outputs/run_log.md` (what ran, in what order, models, turn counts if known, failures) and `outputs/pr_body.md` (the pull-request body: the bottom line in at most ten lines, what the Action did, the models, a link to `REPORT.md`, and the fallback disclosure if any).

### CI checks before committing

The repository's CI (`.github/workflows/ci.yml`) runs `python -m pytest tests/ -q`, `python ledger_listing.py` and `python ledger_sweep.py` on every pull request, and the sweep fails on any bare occurrence of a retired-claim signature in tracked `.md`/`.json`/`.py` files, your outputs included. Run all three from the repository root before committing. If the sweep reports an undisposed hit inside the run bundle, add a `CLEAN_LINE` entry to `ledger_sweep.py` for that file and a distinctive substring of the line, with a reason that says what the line actually asserts (this is the one edit outside the run bundle you may make, and the pull-request body must mention it); if the hit is a genuine bare assertion of a retired claim, fix the text instead.

### Commit and pull request (every stage that produced files)

```bash
git config user.name "claude[bot]"
git config user.email "41898282+claude[bot]@users.noreply.github.com"
git checkout -b agents/review-assessment-<run_dir>-<github run id>
git add agents/runs/<run_dir>/outputs agents/runs/<run_dir>/REPORT.md
git commit -m "agents: review assessment <run_dir> — <stage> (<model>)"
git push -u origin HEAD
gh pr create --base main --title "agents: review assessment — <run_dir> (<stage>)" --body-file agents/runs/<run_dir>/outputs/pr_body.md
```

Add only files under the run bundle. If `work/` exists, it is ignored by the bundle's `.gitignore`; never add it. If the push or the PR creation fails, print the branch name, the commit hash and the error in the job log and stop; do not retry with different credentials and do not push anywhere else.

## If something runs out

A subagent that stops early (turn cap, usage limit) is re-run once, fresh, with the same prompt; the loss is disclosed in `outputs/run_log.md` and in `REPORT.md` section 7. If the run itself cannot complete a stage, commit what exists under `outputs/` with `REPORT.md` absent, open the pull request as a draft (`gh pr create --draft`) with the state described in the body, and stop. Never publish a verdict from a seat that was cut off as if it were complete.
