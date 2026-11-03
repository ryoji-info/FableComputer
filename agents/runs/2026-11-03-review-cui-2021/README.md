# Run bundle: assessment of Cui, Wang & Sun, "Graphene plasmon for optoelectronics" (Rev. Phys. 6, 100054, 2021) against the Fable Computer record

**Question (maintainer, 2026-11-03):** can anything in this review be applied to improve the Fable Computer's performance?

**What this directory is.** The input half of a two-part assessment. The maintainer's local Claude Code session (2026-11-03) read the review in full from the publisher PDF, pulled its 198 references from Crossref, and ran eight topic "gather" agents (Claude Opus 5.5) that read the primary works behind the review's topics and mapped them to the record's named open problems. Those results are in `inputs/`. The second half — one synthesis agent, three adversarial attack lenses (physics, papers, engineering) and the finalization — runs in GitHub Actions through `.github/workflows/agents-review-assessment.yml`, following `agents/prompts/review-assessment.md`, and writes `outputs/` and `REPORT.md` here through a pull request.

**How to run it.** Actions → "Agent Lab — assess a paper against the record (synthesis + attack)" → Run workflow, with `run_dir` = `2026-11-03-review-cui-2021`, stage `synthesize-attack-finalize`, model Claude Opus 5.5 (default). The job takes roughly one to two hours and opens a pull request; a human merges.

**Inputs.**

| File | Content |
|---|---|
| `inputs/fable_context.md` | Design point, gates, open problems and rules for the agents |
| `inputs/review_block.md` | The review's structure and key sentences, and observations R1–R10 for the attack |
| `inputs/draft_hypotheses.md` | Hypotheses H1–H10 written before the primary works were read |
| `inputs/gather_results.json` | The eight gather agents' sourced items and mappings (local workflow `wf_4c07f683-31e`) |
| `inputs/schemas.json` | JSON schemas for the synthesis and the verdicts |
| `inputs/draft_assessment.md` | Draft long-form assessment, sections 4–5 left for the verdicts |
| `inputs/prior_spp_assessment.md` | The 2026-11-03 assessment of surface plasmon polaritons alone or combined with the acoustic plasmon, for consistency |
| `inputs/extract_papers.py` | Produces `work/papers_txt/` from `papers/*.pdf` (not committed) |

**What is not here.** The review itself (CC BY-NC-ND 4.0; read it at https://doi.org/10.1016/j.revip.2021.100054) and the local text extracts of it. `inputs/review_block.md` carries its content section by section.

**Provenance and disclosures.** Gather agents: Claude Opus 5.5, 2026-11-03, in the maintainer's local session; four of them were run before and four after an interruption. Two gather agents placed the maintainer's email address in HTTP request headers (Crossref "polite pool" User-Agent on about six requests; one arXiv download); no other service received it, and the pipeline prompt forbids it. Everything in this bundle is agent output labeled as such; nothing in the record was changed by it.
