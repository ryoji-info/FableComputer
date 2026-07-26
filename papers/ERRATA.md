# Errata for the deposited manuscripts

**What this file is.** The manuscripts in `papers/` are living documents, revised
periodically and archived on Zenodo under version DOIs. Between revisions the
community's promoted notes in [`notes/`](../notes/) sometimes retire or qualify a
claim the deposited text still makes. This file is the **note-keyed index of those
gaps**: one row per correction, naming the promoted note that binds it, the passage
it applies to, and what the record now says.

It is not a revision. The manuscripts themselves change only by the maintainer's
hand, and re-archiving on Zenodo is a maintainer release decision
([GOVERNANCE.md](../GOVERNANCE.md)). Until a revision lands, **this file is the
correct reading of the deposited text.**

**Shipped versions:** Part I **v6.0**, Part II **v2.0** (July 2026 reader-focused
revision; complete history in [REVISION-HISTORY.md](REVISION-HISTORY.md)). Most
recent Zenodo deposits: Part I v5.5 ([10.5281/zenodo.21369405](https://doi.org/10.5281/zenodo.21369405)),
Part II v1.6 ([10.5281/zenodo.21385646](https://doi.org/10.5281/zenodo.21385646)).

> **Status (July 2026): every row below is folded into the v6.0 / v2.0 repository
> copies.** The rows are retained because the *deposited* v5.5 / v1.6 PDFs still
> carry the original passages; until re-archiving, this file is the correct reading
> of the deposited text. Once the new versions are deposited, these rows clear.

**Provenance.** Every row below is carried by
[`notes/2026-07-26-record-audit-ten-findings.md`](../notes/2026-07-26-record-audit-ten-findings.md)
(promoted 3-of-3), whose ten findings this file discharges for the two manuscripts,
and by the 66-entry work order published at
[discussion #65](https://github.com/ryoji-info/FableComputer/discussions/65).
Corrections outside `papers/` were applied directly to the repository instead of
being listed here.

---

## Part I — folded into v6.0 (repository copy); applies to the deposited v5.5

| # | passage | what the deposited text says | what the record says | binding note |
|---|---|---|---|---|
| I-1 | §6.2(iii), p.14 | the ring-down's "data-dependent part is contained by the saturating rail at every cell and reset by the clocked re-sync stations", and quantifying residual data ISI "is an open item" | Neither half holds. The rail's compression at the pulse-run drive plane is **−0.043 dB at 2×10⁻³ / −0.097 dB at 3×10⁻³** (−1.259 dB at the cascade's own operating swing 0.0116), which cannot contain a **≈3–4 dB p-p** loaded ring-down swing; and Table 5 places "one station at the read-out boundary" against a required **per-slot, per-cell** flush, a granularity mismatch of 10–24×. The ISI magnitude is no longer open in-model. | [07-22 ring-down](../notes/2026-07-22-cavity-ringdown-isi.md) §1/§3 |
| I-2 | Abstract; Table 3, p.8; Table 5's throughput row | 0.25 THz baseline with fan-out-2 logic at a 4-ps slot | The clock-chain **design range** (0.2–0.5 THz) is not retired; **F = 2 logic closure at a 4-ps slot is.** No de-Q rate — including D = ∞ — closes the composed F = 2 ledger at 4 ps, because rebuild time binds. The defensible in-model headline is **≈0.1 THz logic**, across three closing configurations: **E1** no flush at all, 79–92 GHz; **E2** stretched slot + passive guard, 98–128 GHz; **E3** stretched slot + active de-Q, 100–148 GHz, worth ≈+10 % over E2 and **0 %** at its 81 GHz demonstrated-calibrated corner. | [07-23 reset-switch](../notes/2026-07-23-reset-switch-adjudication.md) §0/§4 |
| I-3 | Table 7, gate **G2**, pp.30–31 | "pulse-to-pulse gain spread at 0.2–0.25 THz \| pass < 1 dB \| model target < 0.1 dB (clock train)" | The model target is the retired incumbent figure; loaded ring-down ISI is ≈3–4 dB p-p at the 0.25 THz slot. The **pass threshold is pre-registered and does not move**; only the model expectation is wrong. The single quotable p-p value remains **open** (convention-dependent; the [2.0, 4.5] band was exceeded at 4.90 and 4.91 under a stricter burst-window convention). | [07-22 ring-down](../notes/2026-07-22-cavity-ringdown-isi.md) §5; [07-25](../notes/2026-07-25-e1-burst-scaling-proviso.md) §2 |
| I-4 | §3.2, pp.6–7; §6.2's "few-cycle 1-THz pulses at a 0.2–0.5 THz repetition rate" | 3-cycle launch bursts at 0.2–0.5 THz repetition | At the stretched operating point the gain leg is set by **drive duration, not slot length**: with the released fixed 3-cycle burst the per-'1' gain saturates **0.9–3.0 dB short of F = 2 at every slot**; closure needs **ncyc ≈ 12** slot-filling bursts (7.851 dB, ≈71–91 GHz). The 0.115 THz band centre is reached at no measured burst length, `solver.run` cannot express the configuration, and the launch-energy/duty-cycle cost is **open**. | [07-25](../notes/2026-07-25-e1-burst-scaling-proviso.md) §1–§2, §6.4 |
| I-5 | §7.3, p.20; Table 5's worst-path row; §7.2 | +8 dB/pulse streaming gain cascaded per stage | The +8 dB is the settled-train, per-slot-peak calibration figure — Part I labels the metric correctly at the Abstract, Table 6, Table B1 and Table 7/G1. What the deposited text does not carry is the **decomposition**: data-independent worst-case-'1' gain **≈+3.0 dB [2.9, 4.0]** plus a **≈+4.8 dB predecessor pedestal** (7.80 − 4.84 = 2.96 ≈ 3.05). For slot-rate logic the eye-forming gain is the former; the accumulation that lifts the figure is the same accumulation booked as ISI. | [07-25](../notes/2026-07-25-e1-burst-scaling-proviso.md) §1–§2 |
| I-6 | §6.3 Fan-out, pp.14–15 | "+8 dB against 3 dB split plus 1–3 dB junction loss leaves 2–4 dB of margin", with a corrected figure deliberately declined | **The declination stands and is vindicated** — the promoted fan-out notes compute at the 0-dB junction class only, and the two budgets net different loss items (the notes charge split + `per_gate_loss_353K_dB` = 2.555 dB and no junction; §6.3 charges split + 1–3 dB junction and no propagation), so the margins are not the same quantity. What may be added without contesting it: a citation of the composed envelope as the **0-dB-junction in-model reference point** (F = 2 reserve +2.01 dB [1.46, 2.66] near-specular CW, k_eff = 8·F^(−½), ceiling F ≤ 2.56), and a **slot-rate condition** on "fan-out-2 still closes across the signed band". | [07-20](../notes/2026-07-20-loaded-fanout-fixed-point.md), [07-21](../notes/2026-07-21-composed-regeneration-envelope.md) |
| I-7 | §5 "Saturating rails", p.11 | "1-dB gain compression at δρ/ρ₀ ≈ 1 % and ~14 dB compression at 10 %" — no reference plane | The 1 % is a **source/drive-plane** amplitude (measured 1.15×10⁻² pulse, 7.6×10⁻³ CW; A_SAT_eff ∈ [0.015, 0.023]). ε_rail = 0.10 is **anchored at neither plane**: the intracavity reading is measurement-contradicted (−0.35 dB at 10.05 % measured swing vs the model's −14.15 dB) and the drive-plane reading is unmeasured. | [07-17 plane audit](../notes/2026-07-17-what-the-38-quanta-knee-denominates-after-the-july-plane-aud.md) §4 |
| I-8 | §7.3, p.19; Appendix A, pp.40–41; Table B1's M_th row; **Figure 8's caption** | the solver threshold "converges to the analytic value at first order in Δx"; Figure 8 titled "regenerative operating point (M_th,num ≈ 0.17)" | The Δx→0 limit is the **exact inviscid threshold ≈0.149313** (pre-registered `M_th_num_inviscid_limit` = 0.1490 [0.147, 0.150]), +1.52 % above the small-M analytic 0.147083 — not the analytic value. The shipped 0.169 is coarse-grid Lax–Friedrichs over-diffusion and must not be read as physical; the **physical kinetic threshold is 0.165 [0.154, 0.169]**. (The figure generator `fable-model-chain/figures.py` has been corrected; `figures/fig8.png` awaits regeneration.) | [07-22 viscosity](../notes/2026-07-22-mth-numerical-vs-physical-viscosity.md) |
| I-9 | Abstract; §7.6 Table 6, "Kinetic validity" row | the boundary channel as "a separate and still-open ±1 dB allowance" | Carry §7.5's own rider, which the summary layers omit: **sign-open at the drain, loss-definite at the source, and potentially larger than ±1 dB for a diffuse contact** (−3 dB under Kn², ≲−10 dB under Kn). | [07-18 contact-gated](../notes/2026-07-18-boundary-channel-contact-gated.md) |
| I-10 | Table 7, gate **G1** | model target names tuning and estimator | Additive extension only, every pre-registered pass threshold unchanged: pin G1's **drive amplitude relative to the measured knee** (the operating drive sits 3.8× below the pulse knee; a 3× hotter bench drive erodes 0.5+ dB) and add the companion observables (knee at source amplitude ≈0.76–1.15 %; −1 dB at intracavity swing ≈14 ± 2 %). | [07-17 drive sweep](../notes/2026-07-17-drive-sweep-knee-anchored.md) §8 |

## Part II — folded into v2.0 (repository copy); applies to the deposited v1.6

| # | passage | what the deposited text says | what the record says | binding note |
|---|---|---|---|---|
| II-1 | §5, p.8; §6, pp.11–12; §8's dependencies paragraph | "one MAC per 4-ps slot, wave-pipelined like everything on this fabric"; "at 1/16th throughput (still 1.6×10¹⁰ MAC/s per unit)", with threats to "16 independent slot samples" listed as only comb-clock, gate 1/f and thermal drift | Both figures are **contingent on per-slot flush/reset closure**, which the classical record has adjudicated **negatively at 0.25 THz for F = 2** (in-model, across conventions). **Cavity ring-down memory belongs on the list of threats to slot-sample independence.** The timing basis a quantum throughput claim inherits is ≈0.1 THz with the burst proviso of I-4. The v1.7 text contains no occurrence of "flush", "ring-down" or "reset". | [07-22 ring-down](../notes/2026-07-22-cavity-ringdown-isi.md), [07-22 flush](../notes/2026-07-22-flush-noise-figure-negative.md), [07-23](../notes/2026-07-23-reset-switch-adjudication.md) |
| II-2 | Revision notes v1.6→v1.7, item 3, p.16 | the measured knee at "source-drive amplitude ≈1–1.2 %" | **≈0.76–1.15 %** (7.6×10⁻³ CW to 1.15×10⁻² pulse). The item is internally inconsistent as printed: its own "input-referred ≈22–51 quanta" requires the 0.76 % figure (ε₁ = 1.6153×10⁻³ ⇒ 22.3 and 50.6). Carried by the v2.0 fold and by the marked editorial note on the v1.6→v1.7 block in [REVISION-HISTORY.md](REVISION-HISTORY.md); the block itself is preserved verbatim (append-only). | [07-17 plane audit](../notes/2026-07-17-what-the-38-quanta-knee-denominates-after-the-july-plane-aud.md) |
| II-3 | §3.1, pp.3–4; §6's classical-digital paragraph | ε_rail = 0.10 / N_rail ≈ 3833, no anchoring caveat | v1.7 folded the **knee** half of the plane audit but not the **rail** half: the rail is anchored at neither plane (see I-7). | [07-17 plane audit](../notes/2026-07-17-what-the-38-quanta-knee-denominates-after-the-july-plane-aud.md) §4 |
| II-4 | Abstract, p.1; §1, p.2; §9 Conclusion | "the Part-I threshold cells themselves, re-programmed" | Qualify at all three headline sites, as §5 and Table QB1 already do: the two ladder comparators are a **redesign, not a re-trim** — k_dec ≥ 16 "is not reachable in-model by re-trimming a Part-I logic cell", and a re-trimmed cell presents k_dec ≈ 1.6–3.2. | Part II v1.6 §5 / Table QB1; [07-15](../notes/2026-07-15-finite-sharpness-is-not-a-variance.md) |
| II-5 | Appendix QA, p.23 | the convention string, the coefficient c and the generalised averaging floor "are queued together as machine-readable `results.json` keys" | The queue is **undischarged** — none of those keys exists among the shipped leaf keys. When emitted, the floor key must be **jointly parameterized in c and k_dec**; a k-only key (`q2bit_avg_floor_k16`) re-injects the dependence the v1.5→v1.6 revision block withdrew ("Warm and cold alike are contingent on c and on k_dec jointly"). | [07-14](../notes/2026-07-14-q2bit-avg16-averaging-convention.md) §3; [07-15](../notes/2026-07-15-finite-sharpness-is-not-a-variance.md) §4 |

## Already fixed in the shipped text — recorded so it is not re-opened

- The **≈250 K hydrodynamic-validity expiry** contradiction (Part II §1/§8 vs Part I §8.3) was **fixed in v1.7**: both passages now carry the retired-cliff language consistent with Part I v5.6 §8.3 (147–360 K band, "it is not a cliff", a smooth signed penalty).
- The **Table QA1 legacy repository link** was **fixed in v1.7**: the caption reads "Available at https://github.com/ryoji-info/FableComputer". `README.md` previously asserted this erratum was outstanding; that sentence has been removed.

## Generator note

`fable-model-quantum/make_manuscript.py` no longer reproduces Part II. It carries none of the manuscript's seven revision blocks, self-identifies as a companion to Part I "Revision v5", writes `../Fable-Computer-PartII-v1.docx` rather than into `papers/`, and has a single commit against eleven touching `papers/`. **Running it would emit a v1.0-era document, discarding seven revisions.** It is retained as a historical artifact and marked as such in its own header; `papers/` is hand-maintained.

---

*Maintained per [notes/2026-07-26-record-audit-ten-findings.md](../notes/2026-07-26-record-audit-ten-findings.md). Each row is removed when the corresponding revision lands and is re-archived.*
