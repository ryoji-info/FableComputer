# Errata for the deposited manuscripts

**Status: three outstanding rows for Part I (I-41 … I-43), against v6.1; none for Part II
or Part III.** The deposits of 29 October 2026 — Part I v6.1, Part II v2.1 and Part III
v1.1 — are the repository copies in [`papers/`](.), so no correction from a promoted note
is missing from a current deposit. The three rows, opened on 3 November 2026, are checks
of Part I's own citations against their primary sources — a table note stronger than the
work it cites, a coupling efficiency that a cited work does report, and a sentence whose
citation does not support it; no promoted note binds them (see 'Outstanding rows'). The
30 rows for Part I (I-11 … I-40, against v6.0) and 19 for Part II (II-6 … II-24, against
v2.0) that this file carried until the October deposits are discharged and preserved, row
by row, at the end of the v6.1 and v2.1 blocks of
[`REVISION-HISTORY.md`](REVISION-HISTORY.md) — nothing was deleted. Part III has no rows:
v1.1 postdates every promoted note in the record (the latest is dated 2026-10-17) and none
has been promoted since. Rows that the October notes would have required against the
deposited v1.0 ([10.5281/zenodo.23132802](https://doi.org/10.5281/zenodo.23132802), 4 October 2026)
were never opened, because this file then recorded v1.0 as undeposited; v1.1 folds those
notes.

| paper | deposited version | Zenodo DOI |
|---|---|---|
| Part I | v6.1 (29 October 2026) | [10.5281/zenodo.23758795](https://doi.org/10.5281/zenodo.23758795) |
| Part II | v2.1 (29 October 2026) | [10.5281/zenodo.23758729](https://doi.org/10.5281/zenodo.23758729) |
| Part III | v1.1 (29 October 2026) | [10.5281/zenodo.23758679](https://doi.org/10.5281/zenodo.23758679) |

## What this file is for

The manuscripts are living documents: findings promoted into [`notes/`](../notes/) are
folded back into them in periodic revisions, each archived under its own version DOI.
Between a promotion and the next deposit there can be a gap — a claim the deposited text
still makes that the record has retired. **This file is where that gap is recorded**, one
row per correction, naming the passage, what the deposited text says, what the record
says, and the binding note. It is not a revision: the manuscripts change only by the
maintainer's hand, and re-archiving is a maintainer release decision
([GOVERNANCE.md](../GOVERNANCE.md)).

Until the v6.0 / v2.0 deposits (July 2026) this file carried **fifteen** such rows — ten
for Part I, five for Part II — from the July 2026 record audit
([`notes/2026-07-26-record-audit-ten-findings.md`](../notes/2026-07-26-record-audit-ten-findings.md),
promoted 3-of-3). Those rows are now discharged, and they are preserved as the row-by-row
content of the v6.0 / v2.0 revisions in
[`REVISION-HISTORY.md`](REVISION-HISTORY.md) — nothing was deleted.

Between those deposits and the v6.1 / v2.1 deposits (29 October 2026) it carried
**forty-nine** rows — thirty for Part I (I-11 … I-40), nineteen for Part II (II-6 … II-24),
the corrections the record required between the two deposits. They were discharged the
same way on 2 November 2026 and are preserved as the row-by-row tables that close the
v6.1 and v2.1 blocks of [`REVISION-HISTORY.md`](REVISION-HISTORY.md).

## When to add a row

When a promoted note retires or qualifies something a **deposited** manuscript states.
Give the passage, quote the deposited text, state what the record says, and link the
note. Remove the row when a revision carrying the correction is deposited, moving it into
[`REVISION-HISTORY.md`](REVISION-HISTORY.md) under that revision.

If you are reading a manuscript and want the corrected state of knowledge, the entry
point is [`notes/INDEX.md`](../notes/INDEX.md): where a note and a manuscript disagree,
**the note wins**.

---

## Outstanding rows

### Part I — against the deposited v6.1

Three rows, opened on 3 November 2026 from a maintainer-operated review session (whether
surface plasmon polaritons could replace or complement the acoustic-plasmon bit; the
adversarial papers lens of that session, verdicts 5, 9 and 16). They differ from every
earlier row in one respect, stated plainly: **no promoted note binds them.** Each is a check
of a Part I sentence against the primary source it cites or should cite — the arXiv text
or the journal abstract, fetched on 3 November 2026 and quoted in the last column. The
v6.1 block of [`REVISION-HISTORY.md`](REVISION-HISTORY.md) records that corrections no
promoted note binds were, at that revision, carried in the block and not as rows; these
three are entered as rows by the maintainer's decision because each names one deposited
sentence and the source that contradicts or qualifies it, which is what a row is for. None
changes a released number, a pass threshold or a model target: I-41 and I-42 correct what
the text attributes to cited work, I-43 corrects a citation. Page numbers are those of the
deposited v6.1 PDF; 'external' marks a fact taken from the cited source.

| # | passage | what the deposited text says | what the record says | binding note |
|---|---|---|---|---|
| I-41 | Table 3 'Plasmon mode', p.10; the §3.1 stack caveat, p.7; §9.1, p.37 | "acoustic / gate-screened (metal top gate)" — "required for confinement and gate programmability [4]" | Confinement, yes; gate programmability, no — and [4] does not say so. [4] gated the **unscreened** mode with a THz-transparent ZnO top gate (V_ZnO = −3 to 3 V, n = −6.2 to 7.9×10¹¹ cm⁻², at 4 K) and obtained the acoustic mode under its Ti/Au gate, as §3.1 already states (external). Tu et al., Commun. Mater. 1, 7 (2020) set the size, position and resonance frequency of THz plasmon cavities electrically through a patterned 20-nm ZnO back gate of ≈90 % THz transmission across their 1.3–10 THz range (external); Ju et al., Nat. Nanotechnol. 6, 630 (2011) tuned graphene micro-ribbon plasmon resonances over a broad terahertz range by ribbon width and in-situ electrostatic (ion-gel) doping (external). What the metal gate at d = 10 nm is required for is the confinement of Eq. (1), the ≈1-V, sub-µm segment programming of §3.1, and the gate-referenced AC short at the source end that the DS boundary condition of §9.1 uses — a THz-transparent gate supplies neither the confinement nor that AC ground. Accurate wording: "required for confinement and for ≈1-V, sub-µm metal-gate programmability (and for the gate-referenced source short of §9.1)". No number moves | No promoted note. Primary sources (fetched 2026-11-03): arXiv:2311.02821v2 ([4]; text: "We fabricated two devices with different top-gate structures: one had a ZnO gate and the other had a standard metal (Ti/Au) gate. The ZnO top gate is transparent in the GHz and THz range … This enables us to investigate plasmons free from the gate screening (unscreened plasmons) while tuning the carrier density"; section 'Unscreened graphene plasmons in a ZnO gate device'); arXiv:1911.08672v1 = [10.1038/s43246-019-0002-9](https://doi.org/10.1038/s43246-019-0002-9) (abstract: "control size, position, and frequency of plasmon cavities"; Supplementary §1: transmittance "about 90% … in the whole range of our experiment between 1.3 to 10 THz"); [10.1038/nnano.2011.146](https://doi.org/10.1038/nnano.2011.146) (abstract: resonances "tuned over a broad terahertz frequency range by changing micro-ribbon width and in situ electrostatic doping"; the ion gel is acknowledged there; the body is paywalled and is not quoted). SPP review of 3 November 2026, papers lens, verdict 5 |
| I-42 | §3.2, p.8; §9.5, p.39; with §3.3, p.9, and Table 6 'Launch/read-out coupling', p.35 (Table 2, p.6, gives [4]'s condition) | "that coupling efficiency is unquantified by any cited work" (§3.2); "no cited work quantifies the coupling efficiency" (§9.5); §3.3: "What no cited work supplies is the transducer from the stripline's micron-scale mode into the ~100×-confined acoustic-plasmon mode"; Table 6: "efficiency into the acoustic mode … unquantified" | Ref. [4] does quantify an electrical-pulse-to-plasmon conversion on its stack, at 4 K: a lower bound η = (I_plasmon/I_input)² that "can exceed 0.35" for the unscreened (ZnO-gated) plasmon at high carrier density — "~30%" in the arXiv abstract, "35%" in the journal abstract — and "can be as large as 0.03" for the acoustic (Au-gated) plasmon once its 21-µm propagation length is divided out (z ≈ 0.56); its authors credit the absence of a momentum mismatch for the high values and name the CPW-to-graphene impedance mismatch as the limit — large in the Au-gated device (the velocity difference and the gate itself), smaller under the THz-transparent ZnO gate (external). What no cited work quantifies is the coupling from a photomixer or stripline into the acoustic mode at 300 K on this stack, which is the open item that §3.3, Table 6 and the calibration sequence of §10 name. §3.2 and §9.5 do not hold as written; §3.3 and Table 6 hold with that scope. The 20-dB budget, the §9.5 mitigations and every released number are unchanged | No promoted note. Primary source (fetched 2026-11-03): arXiv:2311.02821v2 ([4]), section 'Conversion efficiency of graphene plasmon excitation' and Figure 5 ("For unscreened plasmons, η can exceed 0.35 at high carrier densities. For acoustic plasmons, since the propagation length is 21 µm, z ~ 0.56 and η can be as large as 0.03"; "In the ZnO gate device … the transparent ZnO gate in the THz range result in a smaller impedance mismatch and thus a higher conversion efficiency"; Methods: "All measurements were performed at 4 K in a vacuum"); the Nat. Electron. 7, 537 (2024) abstract ("can also reach 35% due to the absence of a momentum mismatch"). SPP review of 3 November 2026, papers lens, verdict 9 — which had expected the ≈3 % acoustic figure to exist only in secondary text; it is in [4]'s main text |
| I-43 | §4, the lifetime-row paragraph, p.11; reference [41], p.53 | "gate-metal ohmic loss, not included in τ, adds to the budget at small d [41]" | [41] does not support the sentence. Woessner et al., Nat. Mater. 14, 421 (2015) imaged mid-infrared (CO₂-laser s-SNOM) plasmons in an hBN(7 nm)/graphene/hBN(46 nm) stack on 285-nm SiO₂ over a Si back gate, with metal only in the side contacts and the probe tip, and assign the damping to graphene's thermal phonons and hBN dielectric loss; it has no metal top gate and no treatment of gate-metal loss (external). Works that do treat the gate's loss: Principi et al., Phys. Rev. B 98, 035427 (2018) — Landau damping of acoustic graphene plasmons by particle-hole excitations in the metal gate, with metal nonlocality, found "surprisingly weak", Q exceeding 10² — and Dias et al., Phys. Rev. B 97, 245405 (2018) — metal nonlocality in a metal-film/hBN/graphene stack, which lowers the graphene-plasmon loss below the local prediction (external, abstracts). The loss itself stays unquantified: the manuscript specifies the gate only as a "segmented Au gate lattice", with no thickness or resistivity, and no released number includes it. The correction is to the citation; no number moves | No promoted note. Primary sources (fetched 2026-11-03): arXiv:1409.5674v1 ([41]; "The h-BN(7 nm)–graphene–h-BN(46 nm) stack … lies on top of an oxidized silicon wafer, used as a backgate"; Methods: "vacuum–SiO2(285 nm)–h-BN(46 nm)–graphene–h-BN(7 nm)–vacuum"; abstract: "the main damping channels as intrinsic thermal phonons in the graphene and dielectric losses in the h-BN"); arXiv:1802.06797 = [10.1103/PhysRevB.98.035427](https://doi.org/10.1103/PhysRevB.98.035427) (abstract); arXiv:1804.06478 = [10.1103/PhysRevB.97.245405](https://doi.org/10.1103/PhysRevB.97.245405) (abstract). SPP review of 3 November 2026, papers lens, verdict 16 |

When a promoted note next retires or qualifies something the deposited v6.1 / v2.1 / v1.1
texts state, its row goes here.
