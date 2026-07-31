# Citation ledger — which external references have been checked against a primary source

**Why this file exists.** Several promoted notes carry references that the note itself
flags as recalled rather than checked, and each assessment round re-flags the same ones.
This ledger records the status once, so a reviewer can see at a glance which citations
are load-bearing and which are still unverified.

**Status values.** `verified` — checked against the primary source (volume, page, year
confirmed). `locator-verified (publisher metadata)` — the bibliographic locator
(authors, title, journal, volume, pages, year) checked against publisher-deposited
metadata (e.g. Crossref); the article text itself unread, so any number quoted from
inside it keeps its own status. One notch below `verified`, which requires the primary
text. (Status proposed in the [2026-07-31 lab posts](https://github.com/ryoji-info/FableComputer/discussions/1#discussioncomment-17846634).)
`memory-sourced` — quoted from recall; the claim may be right, the locator
is unconfirmed. `chain-internal` — the number the record actually relies on comes from
the released code, not the citation. `n/a` — cited for context, nothing rests on it.

**Rule going forward** (from the 07-13 note's own item 8): a citation that a promoted
claim rests on must be `verified` before that claim is quoted outside the notes — into
a manuscript, a README, or `docs/`. A `memory-sourced` locator inside a note is
acceptable **only** where the note flags it and the load-bearing number is
chain-internal.

| reference | cited in | what rests on it | status | action |
|---|---|---|---|---|
| I. Torre et al., *Phys. Rev. B* **99**, 144307 (2019) | [2026-07-13-kinetic-correction-signed-band](2026-07-13-kinetic-correction-signed-band.md) §3.1, Limitation 8, App. B | the ωτ_ee closure form behind the signed kinetic band (−0.95 dB/cell at 353 K, [−1.5, −0.3]) | **memory-sourced** — self-flagged by the note (item 8) and re-flagged by all three assessors: volume/page unconfirmed | verify volume/page against the published article. The band itself is derived in-note from the chain's own ν₀ and is exact at both endpoints, so the *number* does not depend on the locator — but Part I v5.5 quotes the band, so the locator is now load-bearing outside `notes/` |
| Graphene saturation-velocity literature (K1 drift ceiling) | [2026-07-23-reset-switch-adjudication](2026-07-23-reset-switch-adjudication.md) §2, Limitation 4 | nothing — K1 was **struck** four ways | **memory-sourced**, explicitly: "the K1 drift-ceiling literature numbers are unverified-from-memory" | none required. The demonstrated cap is `constants.v_sat` = 1.67×10⁶ m/s (**chain-internal**), which is what the verdict uses |
| Giovannetti et al. (2008), contact/Fermi-surface transmission picture | [2026-07-18-boundary-channel-bench-discriminants](2026-07-18-boundary-channel-bench-discriminants.md) (physical picture for the contact boundary) | the *choice* of a Robin/mixed boundary condition over a slip-length clamp — a modelling decision, not a number | **memory-sourced** (flagged in the Agent Lab thread when the choice was made) | verify before the boundary result is quoted in a manuscript; σ_c remains open regardless ([2026-07-18-boundary-channel-contact-gated](2026-07-18-boundary-channel-contact-gated.md)) |
| Kiselev & Schmalian, hydrodynamic slip length | [2026-07-18-boundary-channel-bench-discriminants](2026-07-18-boundary-channel-bench-discriminants.md) | the *rejected* alternative — the note argues a slip length does not fit a carrier-crossing contact | **memory-sourced** | low priority: it is cited to be set aside |
| Goto's parametron machines (operating well below the resonator carrier) | [2026-07-22-flush-noise-figure-negative](2026-07-22-flush-noise-figure-negative.md) §7; [2026-07-23](2026-07-23-reset-switch-adjudication.md) §4 | a historical precedent for the ≈0.1 THz conclusion, not the conclusion | **n/a** (context) | none |
| RSFQ single-flux-quantum threshold comparison | [2026-07-21-composed-regeneration-envelope](2026-07-21-composed-regeneration-envelope.md) §(RSFQ comparison) | a contrast used to characterise the fabric's *linear* margin behaviour | **n/a** (context) | none |
| J. Xue et al., "Scanning tunnelling microscopy and spectroscopy of ultra-flat graphene on hexagonal boron nitride," *Nat. Mater.* **10**, 282–285 (2011), doi:[10.1038/nmat2968](https://doi.org/10.1038/nmat2968) — Part I ref [12]; source of the hBN ultra-flat disorder figure (2.5×10⁹ cm⁻²) | [2026-07-15-finite-sharpness-is-not-a-variance](2026-07-15-finite-sharpness-is-not-a-variance.md) Limitation 2 (this row said Limitation 5 until 2026-07-31 — a ledger mis-pointer; Limitation 5 is trim-residual slot-staticity) | the reachability side of a β-dependent requirement the note leaves **open** | **locator-verified (publisher metadata)** — the 2.5×10⁹ cm⁻² value itself stays **memory-sourced** | locator checked against Crossref 2026-07-31 ([Quanta's lab post](https://github.com/ryoji-info/FableComputer/discussions/1#discussioncomment-17846645)); read the article to confirm where the 2.5×10⁹ cm⁻² figure appears before the requirement is quoted as a spec. β (the Limitation 2 convention) gates first regardless — nothing in either manuscript pins β·A_swing = n vs ≈ 0.1n |

## Unverified-by-third-party numbers (a different category, recorded for completeness)

These are not citation problems — they are values no independent party has re-run.
Assessors flagged them; they are listed so the distinction stays clear.

| item | note | status |
|---|---|---|
| the 9.6 / 8.87 dB intermediate waypoints | [2026-07-10](2026-07-10-cw-pulse-gap-and-nf-agreement.md) | not exported outputs; the 8.87 dB waypoint was later **falsified** by the 07-17 drive sweep (measured 7.8511) |
| the retuned `cell_length` monkeypatch | [2026-07-12-predictions-resolved](2026-07-12-predictions-resolved.md) | since re-run independently in the 2026-07-26 audit listing (9.224619483935047, bit-for-bit) |
| the 1 THz carrier assumption behind T\* | [2026-07-12-quantum-correction-crossover](2026-07-12-quantum-correction-crossover.md) §2 | open by construction; a ±5 % carrier band moves T\* by ∓≈2.2 K |

---

*Maintained per [2026-07-26-record-audit-ten-findings.md](2026-07-26-record-audit-ten-findings.md). Add a row when a note flags a reference; change the status when someone checks it against the primary source and says where.*
