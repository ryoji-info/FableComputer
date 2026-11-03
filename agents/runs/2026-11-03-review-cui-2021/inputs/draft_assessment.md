# Can "Graphene plasmon for optoelectronics" (Cui, Wang, Sun, Rev. Phys. 6, 100054, 2021) improve the Fable Computer? — assessment (DRAFT, 2026-11-03; sections 5–7 await the attack lenses)

Question (Ryoji, 2026-11-03): "I found a paper about SPP at sciencedirect.com/science/article/pii/S2405428321000034. Please assess whether any of it can be applied to improve the Fable Computer's performance." The PDF was supplied by the maintainer and read in the local session; it is not included in this bundle (CC BY-NC-ND); its content is summarized in inputs/review_block.md.

Method: the review's 20 pages were read in full (text extracted with pypdf; pages 1–3 also viewed as images). Its 198 references were pulled from Crossref. A 12-agent Opus workflow (wf_4c07f683-31e) then read the primary works behind each topic the review covers and mapped them to Fable's named open problems (eight gather agents: loss/lifetime, confinement, launch coupling, readout, gain alternatives, routing components, nonreciprocity/bilayer/hydrodynamics, review outline), merged the maps into candidate applications (one synthesis agent that also received the review's own content and the observations R1–R10 in `review_block.txt`), and attacked the candidates from three sides (physics, papers, engineering/energy). Labels: 設計モデル / 公開モデル / 外部 / 導出 (derived here) / 未解決.

## 0. Bottom line (preliminary; to be confirmed against the attack verdicts)

**Nothing in this review improves a Fable number.** It is a general, mid-infrared-centred overview of graphene plasmonics written for optoelectronic devices (absorbers, modulators, photodetectors, photonic crystals, nanolasers). It never treats the gate-screened (acoustic) mode that is Fable's bit, never mentions drift (Dyakonov–Shur) gain, and contains no analysis of a terahertz plasmon at 300 K. Its own modelling default, a Drude relaxation time of 10⁻¹³ s, would make a 1-THz plasmon overdamped (Q = 0.63), and its dispersion formula (its Eq. 7) is the unscreened branch that the previous assessment showed to be a worse bit than the acoustic one.

The one number in it that touches a Fable figure is the room-temperature acoustic-phonon-limited mobility it quotes, 2.0 × 10⁵ cm²/Vs at n = 10¹² cm⁻² (Chen et al. 2008). That is the intrinsic ceiling on the lifetime row, not a lever: Part I §4 already places its τ = 1 ps best case at ≈86,000 cm²/Vs and names the demonstrated envelope. Read against the primary data, the lifetime row sits inside the measured envelope of the best exfoliated hBN/graphene/hBN devices (0.93–1.20 ps at 10¹²), the phonon ceiling is 1.2–1.8 ps (Q 7.5–11), and the ×2.6 lifetime that Part I's single-rate kinetic operator needs to restore a 353 K threshold lies above that ceiling. So material quality can buy at most ≈×1.2–1.8 in τ, i.e. 1.8 → 1.2 dB per gate, and cannot by itself close the 353 K threshold question.

What the exercise did produce is a set of record findings from the primary works behind the review's topics (section 6), two of which look like errata candidates for Part I.

## 1. What the review is

| Section | Content | Bearing on Fable |
|---|---|---|
| 1.1 Surface plasmons | Metal SPP/LSP basics, k = k0√(εdεm/(εd+εm)), ohmic loss, TM only | none (metal SPPs: see the SPP assessment) |
| 1.2–1.3 Graphene | Tight-binding bands, Dirac cone, ambipolar transport, "mobility as high as 2.0 × 10⁵ cm²/Vs at 10¹² cm⁻² at room temperature based on phonon scattering", 2.3 % absorption, Pauli blocking below 2E_F | the mobility figure is the phonon ceiling on Fable's lifetime row (section 3) |
| 1.4 Observations | Fei 2012 and Chen 2012 nano-imaging (mid-IR, λp ≈ 200 nm, gate-tunable) | already in Part I's reference base |
| 2.1 Basic parameters | Kubo conductivity with τ "set as 10⁻¹³ s"; TE and TM sheet modes; unscreened λ_sp formula | the unscreened branch; τ default 10× below Fable's best case |
| 2.2 Nanoribbons, PIT | GNR resonance formula; Ju 2011 THz ribbons; plasmon-induced-transparency metamaterial (simulation) | localized resonances, not a propagating bit |
| 2.3 Bilayer | Domain-wall plasmon reflection (Jiang 2016, mid-IR expt); gapped-BLG domain-wall plasmons with ps lifetime (Hasdeo & Song 2017, theory); resonant gain under population inversion (Low, Chen & Basov 2018, theory, ≥ ~48 THz); the review swaps its refs [97]/[98] | mid-IR theory; see section 4 |
| 2.4 Twisted bilayer | Plasmon classes; s-SNOM: wavelength up and damping down with twist angle (Hu 2017, mid-IR); generation efficiency vs angle (theory) | see section 4 |
| 2.5–2.6 Multilayer, arrays | ABA trilayer optical/acoustic modes; BLG resonance strongest (Emani 2015); multilayer "supermodes" whose loss falls with layer count (simulations, mid-IR) | see section 4 |
| 2.7 vdW heterostructures | Ni 2018 (cryogenic, 1.6 ps lifetime, loss from the encapsulant); Dai 2015 / Kumar 2015 plasmon–phonon hybrids (hBN Reststrahlen) | Ni 2018 is Part I [42]; hBN phonons play no role at 1 THz |
| 3.1 Metamaterials | Emani 2012, Dabidian 2015, Ju 2011, Yan 2012 stacks; the review itself says this work "mainly focuses on the theoretical and numerical simulation stages" because micro-nano fabrication lags | absorbers and free-space modulators; not launch transducers (section 4) |
| 3.2 Photodetectors | Si-QD/graphene 10⁹ A/W (UV–NIR), 45 A/W mid-IR; Au-NP/graphene SWIR; Si–graphene hybrid metal-plasmonic waveguide PD >40 GHz, 0.4 A/W at 1.55 µm | optical-carrier detectors; no THz plasmon readout (section 4) |
| 3.3 Photonic crystals | GNR-array filter 37–53 THz (simulation); magnetic-field one-way edge plasmons (theory); hBN-encapsulated graphene on SiO₂ pillars: gate-switchable plasmonic bandgap, LDOS ×16 at 60 K (Xiong 2019, expt) | supports gate-defined routing in principle; cryogenic, mid-IR |
| 3.4 Lasers | ZnO–graphene superlattice Raman nanolaser; graphene nanospaser with quantum-well gain (proposal, mid-IR); graphene-tuned THz quantum cascade laser (Chakraborty 2016, cryogenic) | alternative gain routes, none at 1 THz / 300 K (section 4) |
| 4 Outlook | Generic | — |

Overlap with Fable's own reference base: of the review's 198 references only Woessner 2015 (Part I [41]) and Ni 2018 (Part I [42], Part II [14]) are cited by Parts I–III; Lundeberg 2017 (Part I [40]) appears in the review only through an editor's summary, and Ju 2011 only in ERRATA I-41. The review does not cite Alonso-González 2017, Lundeberg 2017 itself, Epstein 2020 or Principi 2011, i.e. none of the acoustic-mode literature Fable rests on; conversely Koppens 2011, Jablan 2009, Fei/Chen 2012 and Iranzo 2018 are in the review but not in the papers.

## 2. The review's mobility figure against Part I's lifetime row (導出)

τ = μE_F/(e v_F²) with E_F = 116.7 meV, v_F = 10⁶ m/s; Q = ωτ at 1 THz; per-gate (λp/2) loss 13.65/Q dB; M_th = 1/(8 f0 τ).

| Mobility at n = 10¹², 300 K | Source | τ | Q (1 THz) | Loss per gate | M_th |
|---|---|---|---|---|---|
| 86,000 | Part I §4 lifetime row (τ = 1 ps) | 1.00 ps | 6.3 | 2.17 dB | 0.125 |
| 80,000–103,000 | Purdie 2018 Fig. 7b, electrons/holes, 290 K | 0.93–1.20 ps | 5.9–7.5 | 2.3–1.8 dB | 0.13–0.10 |
| ≈90,500 | Wang 2013 Fig. 3B at n = 10¹² (the paper's 140,000 is its peak at n ≈ 0.1–0.3 × 10¹²) | 1.06 ps | 6.6 | 2.06 dB | 0.118 |
| 102,000 | Hwang & Das Sarma 2008, D = 19 eV | 1.20 ps | 7.5 | 1.82 dB | 0.104 |
| ≥125,000–156,000 | Morozov 2008 (ρ_S ≤ 50 Ω); Wang 2013 high-density ρ ≤ 40–45 Ω | ≥1.46–1.82 ps | ≥9.2–11.4 | ≤1.49–1.20 dB | ≤0.086–0.069 |
| 200,000 | Chen 2008, quoted by the review | 2.33 ps | 14.7 | 0.93 dB | 0.054 |
| 224,000 | what Part I §4's "×2.6 lifetime" to restore a 353 K threshold would need (300 K equivalent) | 2.6 ps | 16.4 | 0.83 dB | 0.048 |
| 10⁴ (review's τ = 10⁻¹³ s default; wafer-scale CVD stacks, Fukamachi 2023) | — | 0.1 ps | 0.63 | overdamped | 1.25 |

Reading: the design row is inside the best measured DC envelope, in its lower half; the acoustic-phonon ceiling band is 1.2–1.8 ps (Q 7.5–11; the review's 2 × 10⁵ is the top of the literature spread, which scales as the deformation potential squared); the ×2.6 the 353 K threshold needs is above the ceiling. Acoustic-phonon mobility scales roughly as 1/T, so at 353 K the ceiling is ≈1.4–2.0 ps. The measured room-temperature THz plasmon lifetimes under metal gates (Barcons Ruiz 2023 Fig. S7: momentum τ 0.18–0.48 ps; Alonso-González 2017: amplitude decay 0.38–0.6 ps) sit far below all of these, and the measured lifetime is a plasmon damping time under a thin Pd/AuPd gate that itself adds 14–27 % of the damping (image-current estimate), not a DC transport time.

## 3. Topic-by-topic mapping (gather results; batch A read in full, batch B and the attack verdicts pending)

### 3a. Loss and lifetime (review Sec. 1.3, 2.1, 2.7)
- Mid-IR Q values (Woessner γ⁻¹ ≈ 25 at RT; Ni 2018 cryogenic) do not transfer: in the mid-IR the damping is hBN dielectric loss, phonon emission and plasmon–phonon hybridization; at 1 THz those channels vanish (hBN tan δ ≈ 0.4–2.5 × 10⁻⁴, ≤0.16 % of the damping; derived from Woessner's Lorentz parameters) and phonon damping reduces to the DC transport rate (Principi 2014, q, ω → 0 limit).
- n = 10¹² already sits at the τ maximum of the best RT device (τ(n) from Wang 2013 Fig. 3B is flat at 1.01–1.06 ps over 0.5–1.5 × 10¹²); lowering n raises μ without lengthening τ.
- Scalable material: wafer-scale CVD-hBN/CVD-graphene (Fukamachi 2023) gives τ ≤ 0.12 ps (Q ≤ 0.75, overdamped); lab-scale CVD graphene in exfoliated hBN 0.35–0.57 ps (Q 2.2–3.6); De Fazio 2026 resonances only ≤ 90–130 K. Alternative route: Gebeyehu 2024 (decoupled CVD graphene on Cu(111)/sapphire, RT μ > 10⁵ once hBN-encapsulated; abstract only).
- Gate-metal ohmic loss (Part I §4, ERRATA I-43): image current = sheet current at qd = 0.027, so 1/τ_gate = R_s · n e² v_F²/E_F; thick Au (≥1–2 skin depths, 80–160 nm) adds 0.4 %; 30-nm Au 1.6 %; 15-nm Pd or AuPd gates, as used in every RT acoustic-THz experiment Part I cites, 14–27 % (Q 4.9–5.5, drive power ×1.3–1.6). Part I specifies no gate thickness; this is the one quantification the loss topic can add.

### 3b. Confinement (review Sec. 2.7, 4; Iranzo 2018)
- Gate distance d below 10 nm shortens the cell (576 → 436 nm at 5 nm, 403 at 4 nm; Eq. (1), ε_z 3.32), cuts area (27.4 → 16–21 µm² per cell at 5 nm) and cuts drive heat ∝ s³ (×0.44 at 5 nm: 3.4–4.5 µW per cell, 13–17 fJ/MAC). But P_cell/N = 4M²ħω/(ε²τ) is independent of d, so the same scaling removes decision quanta one-for-one: the loaded fan-out-2 fixed point 99–277 → 43–121 quanta at 5 nm against DG1's ≥406. Confinement trades energy for quanta; it does not improve DG1.
- Floors: direct tunnelling through hBN (Britnell 2012) sets d ≳ 1.3–1.7 nm for ms-class gate-charge retention; breakdown never binds (field set by n: 0.05–0.06 V/nm at any d); the ±1-layer speed error plus the first-sound shift stay inside the +48 % trim range only down to d ≈ 4.5–5 nm; the Landau ceiling meets the DS threshold at d ≈ 1–2.3 nm. The record's own d = 5 nm die exists (Part I §10, ERRATA I-40: no 353 K threshold in the kinetic operator).
- Eq. (1) reproduces Lundeberg 2017's measured speeds at 5.5–27 nm within 1–4 %; it is the nonlocal RPA result (Principi 2011), although Part I calls it "gated local-RPA" (labelling only). The first-sound speed deficit at 10 nm is −2.6 to −2.8 % (Barcons Ruiz Eq. 2), i.e. a +10–12 % density trim, against the record's ≈11 % kinetic deficit (+48 % trim): the larger in-model deficit must come from something other than the zero-to-first-sound crossover, which THz nanoscopy on the 10-nm stack could test.

### 3c. Launch coupling (review Sec. 2.2, 3.1, 3.3)
- The metasurface literature the review cites reaches 94–100 % absorption only by critical coupling into localized, dissipative resonances (Thongrattanasiri 2012 theory; Yao 2014 mid-IR; Lee 2019 94 % at 8.5 µm into an acoustic mode; Kakenov 2016 99 % at 2.8 THz, Drude). That maximizes dissipation in the resonator, the wrong target for a transducer into a propagating mode. No work couples free-space or stripline THz into a propagating gate-screened mode with a measured efficiency at 300 K.
- The only measured launch efficiency is Part I's own ref. [4] (Yoshioka 2024, now read in the primary text): η ≈ 0.03 per CPW–graphene interface for the Au-gated acoustic mode (35-nm hBN) and ≥ 0.35 for the ZnO-gated unscreened mode, at 4 K, limited by velocity/impedance mismatch (CPW ≈10⁸ m/s vs acoustic ≈3 × 10⁶). Required η from a 10-aJ/4-ps slot (15,092 quanta): 2.7 % for the 406-quanta decision floor, 3.8–4.9 % for the 576–737-quanta launch budget, ≈100 % for Part I §8.1's "~10 aJ per bit in the mode" reading; the two readings differ ×20–26 (record question).
- A resonant antenna-coupled gate segment built from the plasmon itself is bounded by η ≤ 1 − 2Q_L/Q_i (coupled-mode theory): at Q_i = 6.3, ≤37 % for Q_L = 2 (a 4-ps slot tolerates Q_L ≲ 3–4); at the measured RT Q_i 2.5–3.8, no segment with Q_L ≥ 1.25–1.9 exists. It cannot beat a broadband galvanic launch unless τ ≳ 1.3 ps.
- Taper route (hypothetical): 0.35 unscreened launch × (−1 to −3 dB) transition = 17.5–27.8 %, 2,640–4,200 quanta per 10-aJ slot, clearing the launch budget; pump per line falls from 36–41 mW (η 0.03, launch-budget reading) to 12–17 mW. No THz taper has been measured. A resonant free-space dipole at 1 THz on sapphire is ≈66 µm per port (≈115 cell lengths).

### 3d. Readout (review Sec. 3.2)
- The review's detectors are visible-to-mid-IR, metal-plasmonic or photogating devices (10⁹ A/W with 10¹² gain and >600 ns rise; 0.4 A/W above 40 GHz at 1.55 µm). None reads a 1-THz graphene plasmon.
- Incoherent graphene THz detectors (PTE, bolometric, DS rectifiers) at 300 K are Johnson-limited at 16 pW/√Hz (absorbed-referenced, Cai 2014) to 58–160 pW/√Hz; a 6.3 × 10⁻⁹ decision in a 34.5-GHz band then needs 0.25–2.5 fJ per 14.5-ps slot = 3.7 × 10⁵–3.7 × 10⁶ quanta, 900–9,000× the 406-quanta floor; 17.6 fW/√Hz would be needed. No graphene detector resolves a 14.5-ps slot in real time (best 110 ps FWHM, Cai 2014; 1–2 Gbit/s at a THz carrier, Soundarapandian 2026, against 105 Gbit/s at telecom). DS rectifiers are all read by kHz lock-in.
- An ideal square-law detector needs 400 quanta at 300 K and 476 at 353 K, reproducing the record's homodyne 406/477 within 1.5 %: the floor is the mode's own 5.76 thermal quanta, not the detector.
- Through a measured CPW–graphene port the read needs 406/η plasmon quanta: 13,500 at η 0.03, 1,160 at 0.35 (alternative route: a ZnO-gated read section; a resistive ZnO gate also lifted PTE bandwidth to 220 GHz in Yoshioka 2022). Per-slot photoconductive sampling at the demonstrated gate energy (1.19 nJ per pulse) would cost ≈82 W optical per readout line. Part III #141's rectification read is electronically adequate on paper (8–11 mV against 0.17–0.24 mV Johnson on a 50-Ω node) but keeps the ≈400-quanta floor; a single cell is not RC-limited (≈0.18 ps), the read node needs ≤92 fF on 50 Ω.
- Record point: Part I §9.8 calls every launch/readout member "room-temperature hardware", but both cited demonstrations are cryogenic equivalent-time samplers (Kusyak [7] data at 7 K, Yoshioka [4] at 4 K); Part I flags [4]'s 4 K but not [7]'s 7 K.

### 3e–3h. Gain alternatives, routing components, nonreciprocity/bilayer/hydrodynamics, review outline — pending (batch B).

## 4. The review's specific proposals against Fable (observations R1–R7; verdicts pending)
(R1 mobility ceiling; R2 unscreened default; R3 multilayer supermodes → heat ∝ N²; R4 gain routes mid-IR/cryogenic; R5 gate-defined crystals as evidence for junctions; R6 twisted bilayer and detectors; R7 fabrication immaturity.) To be filled from the synthesis and attack outputs.

## 5. Verdicts (pending)

## 6. Record findings from the primary works (not changed in the repository; candidates for ERRATA or notes)
1. **Lifetime convention of the RT baseline (Part I §4, Part III §2.2 / limitation 1).** "τ ≈ 0.4–0.6 ps, Q ≈ 2.5–3.8 [39, 40]" takes Alonso-González 2017's amplitude decay time (L_PC/v_g = 380–600 fs) as the Drude τ. For ω(ω + i/τ) = s²q² the amplitude decay time is 2τ, so in the record's own convention the [39] baseline is τ = 0.19–0.30 ps, Q = 1.2–1.9; [40] (Lundeberg 2017) gives no lifetime; Part I's own ref. [10] (Barcons Ruiz 2023 Fig. S7) gives momentum τ 0.18–0.48 ps at 295 K directly. Part I's duty arithmetic at the baseline would fall from 8–28 % to 0.9–3.5 %. (Pending physics-lens verification of the convention in [39].)
2. **The "140,000 cm²/Vs demonstrated envelope" (Part I §4) is Wang 2013's low-density peak**; at n = 10¹² the same device gives ≈90,500 (τ 1.06 ps). The phonon ceiling at 10¹² is 1.2–1.8 ps, not 1.6 ps from a single value.
3. **Gate-metal ohmic loss has no d-trend at 1 THz** (image current equals the sheet current once qd ≪ 1); its size is set by the gate's sheet resistance: 0.4 % for thick Au, 14–27 % for the 15-nm Pd/AuPd gates of the cited RT experiments. Part I specifies no gate thickness.
4. **Part I §9.8's "room-temperature hardware"**: Kusyak [7]'s data were taken at 7 K (Part I Table 2 flags [4]'s 4 K only).
5. **Two readings of the launch requirement** (576–737 quanta vs ≈10 aJ in the mode) differ ×20–26 in the transducer efficiency they imply (2.7–4.9 % vs ≈100 %).
6. **Eq. (1) is the nonlocal RPA result** (Principi 2011), not "gated local-RPA"; the design s = 2.33 × 10⁶ m/s corresponds to ε_z = 3.32, just below the 3.4–3.8 band quoted. Labelling only.
7. **First-sound deficit at d = 10 nm is 2.6–2.8 %** (Barcons Ruiz Eq. 2), 4–5× smaller than the record's ≈11 % kinetic deficit; a bench discriminant.
8. **Bandurin 2018** (not in the record) reports plasma-wave leakage into contacts and antennas broadening the resonance most at high density and low harmonic number, i.e. at the Fable cell's operating point: experimental support that the contact channel (issue #88, δ_b) matters.

## 7. Process notes
- Privacy: two workflow agents placed the user's email address in HTTP requests without being asked: the readout agent as a Crossref "polite pool" mailto in the User-Agent of about six api.crossref.org calls, and the confinement agent once in the User-Agent of an arXiv PDF download. No other service received it. The resumed synthesis/attack agents carry an explicit rule against this; the second gather batch ran with the original prompt.
- ScienceDirect's bot check was not bypassed; the full text came from the user-supplied PDF.
- The repository was read only; nothing in it was modified by this session (the errata session started earlier merged PR #145 separately).
