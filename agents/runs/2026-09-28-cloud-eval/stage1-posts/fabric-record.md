# Fabric 🧵 — stage-1 evidence record, 2026-09-28 (run 1)

Status: **posted**. Drafter seat requested on `claude-opus-5-5`; check seat(s) on the Fable alias (Fable 5.1 in this session). Final word count 470.

## Drafter: prior-art check

I searched notes/ (all 39 notes, their appended vote records and INDEX.md) for these terms: energy_per_add, fJ, "per addition", "energy per add", energy/add, block_power, 0.355, 0.466, energy-per, joule, "energy.*slot", pJ, aJ. Results:
(a) 08-07 mth-num-excess-decomposition line 688 prices the upper end's dependence on the 0.118 literal (−1.109 % if updated) at a fixed 4-ps slot. It never rescales to a different clock.
(b) 07-31 physical-launch-gated-frontier §0.5 prices the launch-energy multiplier (×3.4–4.9 per '1', ×1.25–1.30 time-averaged power). It states that the launch cost is excluded from energy_per_add_fJ and that the thermal record (power) is untouched. It does not re-denominate the fabric-side energy per addition at the stretched slot.
(c) 07-23 reset-switch prices the K1 Joule multiplier (4.6× slot-averaged) and lists E4's "2× area & energy". Neither rescales energy_per_add.
(d) 07-16 and 07-17 carry aJ quanta and pulse energies (the knee band 0.0148–0.0335 aJ), which I consume.
No note, INDEX row, ERRATA row (ERRATA.md has no rows), ROADMAP line or REVISION-HISTORY entry records that energy_per_add_fJ / Part I's "≈0.35–0.5 fJ at one addition per 4 ps" is denominated at the slot where F = 2 is retired, or gives its value at 0.1 THz or at the 69 [63, 74] GHz gated frontier. ROADMAP.md line 89 and REVISION-HISTORY I-4 list the launch-energy/duty cost as open; that is the launch-side cost, not the fabric-side bias energy.
I also searched tests/, ledger_*.py, ROADMAP.md, .github/ and notes/ for mutmut or mutation testing (for the scout). The only hits were GraphQL "mutation" strings in agents/scripts. tests/test_published_claims.py has 12 test functions, and none matches energy|thermal.
I checked the scout against this week's three recent scouts (passive interconnect, elasticity register, isolation/nonreciprocity) and it is distinct from all three.
Discussion #124 is cited only as an unpromoted session output. Its question is not re-run.

## Drafter: citations checked

- notes/2026-07-23-reset-switch-adjudication.md (INDEX row): "the defensible headline is ≈0.1 THz logic". This supports the ≈0.1 THz row, 10 ps.
- notes/2026-07-31-physical-launch-gated-frontier.md §0.3: "Composed key: `f_max_F2_gated_GHz` = 69, band [63, 74]; the demonstrated-rung window is 67–71 GHz" (rungs m = 28 / 30, with §1 "rt = 0.5 ps"). §0.5: "the cost lands on the launch/clock subsystem, which `energy_per_add_fJ` explicitly excludes ... the fabric-side thermal record ... is untouched". §2: "bias 0.7·M_th_analytic = 0.10295833333333332". These support the rows, the "thermal record untouched / power does not move" reading, and the low-end bias.
- notes/2026-08-01-ratio-bias-gain-table.md (INDEX row): the table "re-measured in the requirement's own (ratio) convention", with "the bias fork survives the continuum". This supports "the open bias fork" and 0.7·M_th_num as the ratio convention.
- notes/2026-08-07-mth-num-excess-decomposition.md line 688/690: "`energy_per_add_fJ`'s upper end is `P·slot` with `P ∝ v₀²` ... computed from the hard-coded 0.118" and "`0.118` is a hard-coded literal at run_all.py:54". This supports "literal flagged by 08-07".
- notes/2026-07-17-what-the-38-quanta-knee-denominates-after-the-july-plane-aud.md line 27: "`pulse_energy_knee_aJ` = 0.0254 becomes a band 0.0148–0.0335 aJ", with the knee on the launch/drive plane (input-referred). This supports the 0.0148–0.0335 aJ input-referred knee energy.
- Part I (papers/Fable-Computer-Part-I.docx), abstract, §8.1 and Table 5, quoted in the verification log. This supports the quoted "closes at ≈0.1 THz", "~0.4 fJ per addition", "at one addition per 4 ps" and "CMOS-class, not below it".
- Kinetic 🌊 2026-09-02 post (#123, run context): the scout proposing a finite-difference elasticity register ∂ln(key)/∂ln(param). It is referenced, not relied on.
- Discussion #124 (unpromoted session output, run context): "The two-segment operator has no supermode below the single-cell threshold at any clamp strength, at matched Δx resolution". It is cited explicitly as unpromoted.
- ECL/CML static-current energy economics is stated as textbook behaviour with no paper cited. The post says so.
- The optical clock tap passage is from Part I §9 (docx extraction: "needs only enough optical energy to swing the local n_bias across n_th"). It is paraphrased, not quoted, in the post.

## Drafter: verification log

```
Platform: Linux x86_64, `python3 -c "import sys,numpy;print(sys.version, numpy.__version__)"` -> `3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0] 2.4.6`.

The script is /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/fabric/energy_slot.py. It imports the released fable-model-chain constants, thermal and run_all (as a module only; main() is not executed and results.json is not rewritten). It recomputes P_op = TH.joule_kW_cm2(C.n_op, RA.v0, RA.tau353) and P_hi = TH.joule_kW_cm2(C.n_op, 0.118*RA.s, RA.tau353) exactly as run_all.main does, then calls TH.energy_per_add(P, slot=...). Command: `cd <scratch>/seats/fabric && python3 energy_slot.py`. Output:
slot default s: 4e-12 f_sym: 250000000000.0
signature: (P_mW, slot=4e-12)
block_power_mW [0.08869188924579102, 0.11649972849513038] committed [0.08869188924579102, 0.11649972849513039]
E@4ps [0.3547675569831641, 0.4659989139805215] committed [0.3547675569831641, 0.4659989139805216]
  rel dev 0.0
  rel dev 2.382458394895665e-16
  rel dev 0.0
  rel dev 1.1912291974478325e-16
bias M op, hi: 0.10295833333333332 0.118  0.7*M_th_353K = 0.10295833333333332  0.7*M_th_num = 0.11826023624361653
[orchestrator note, not seat output: the 0.25 THz / 4-ps row below is the retired design baseline — F = 2 logic at the 4-ps slot was retired by notes/2026-07-23-reset-switch-adjudication.md; the row is quoted to price it, not to assert it]
0.25 THz (4 ps baseline)         slot=  4.000 ps  E=[0.3548, 0.4660] fJ  x1.0000
0.1 THz (07-23 headline)         slot= 10.000 ps  E=[0.8869, 1.1650] fJ  x2.5000
74 GHz (gated band top)          slot= 13.514 ps  E=[1.1985, 1.5743] fJ  x3.3784
m=28 rung, 14 ps (71.4 GHz)      slot= 14.000 ps  E=[1.2417, 1.6310] fJ  x3.5000
69 GHz (f_max_F2_gated_GHz)      slot= 14.493 ps  E=[1.2854, 1.6884] fJ  x3.6232
m=30 rung, 15 ps (66.7 GHz)      slot= 15.000 ps  E=[1.3304, 1.7475] fJ  x3.7500
63 GHz (gated band bottom)       slot= 15.873 ps  E=[1.4078, 1.8492] fJ  x3.9683
91 GHz F=1 wire                  slot= 10.989 ps  E=[0.9746, 1.2802] fJ  x2.7473
per-cell bias energy per slot 4.000 ps = 50.681 aJ; / pulse_energy_knee_aJ 0.025395 = 1996; vs band 0.0148-0.0335 -> 1513-3424
per-cell bias energy per slot 14.493 ps = 183.627 aJ; / pulse_energy_knee_aJ 0.025395 = 7231; vs band 0.0148-0.0335 -> 5481-12407

Relative deviation from the committed results.json: block_power_mW 0.0 (lower) and 1.19e-16 (upper); energy_per_add_fJ 0.0 (lower) and 2.38e-16 (upper). Gate: rel ≤ 1e-12, passed. Exact equality holds on the lower ends only, so the post never says "bit-equal".
The rt = 0.5 ps (m = 28 -> 14 ps, m = 30 -> 15 ps) and the 07-31 gain-leg bias 0.7·M_th_analytic = 0.10295833333333332 are from 07-31 §1–§2 and match the op-bias printed above.
Source reads: thermal.py line 38 `def energy_per_add(P_mW, slot=C.slot)`; constants.py `f_sym = 0.25e12`, `slot = 1.0/f_sym`; run_all.py line 99 calls TH.energy_per_add(P_block) with no slot; run_all.py line 54 has the 0.118 literal.
[orchestrator note, not seat output: the manuscript passages quoted below name the 4-ps slot / 0.25 THz design baseline, retired for F = 2 logic by notes/2026-07-23-reset-switch-adjudication.md; the post treats that as an errata-class observation]
Manuscript text was extracted with `unzip -p papers/Fable-Computer-Part-I.docx word/document.xml | sed 's/<[^>]*>//g' | grep`. It contains the abstract "fan-out-2 logic closes at ≈0.1 THz rather than at the 4-ps slot (Section 6.2) — at ~0.4 fJ per addition on the fabric side", §8.1 "≈ 0.35–0.5 fJ per addition at one addition per 4 ps. This is CMOS-class, not below it.", and Table 5 "Energy per addition (fabric side) ≈ 0.35–0.5 fJ". README.md line 30: "one addition per 4-picosecond slot ... at roughly 0.4 femtojoules per addition".
The count of 12 test functions comes from `grep -c "def test" tests/test_published_claims.py` -> 12. No tracked file was modified (`git status --short` was empty).
```

## Drafter: seat model note

The maintainer requested this drafting seat on claude-opus-5-5 for this run (the 2026-08-13 policy's Opus seat). It is not Fable 5. It ran in a Linux x86_64 / Python 3.11.15 / numpy 2.4.6 cloud container.

## Check seat round 1 — verdict: **clear**

### Defects

- [minor] claim: | 71 / 67 GHz rungs | 14 / 15 ps | 1.242–1.631 / 1.330–1.748 |
  - measured: 15 ps (m=30, 66.7 GHz)     slot=15.0000 ps  fJ/add = 1.330378 - 1.747496 ; full: 1.7474959274269561 ; rounded 3dp: 1.33 1.747
  - fix: Change 1.748 to 1.747 (0.11649972849513039 mW × 15 ps = 1.7474959 fJ rounds down at three decimals).
- [minor] claim: at 69 GHz each biased cell dissipates 183.6 aJ per slot. […] so the bias outweighs the signal ×5,500–12,400.
  - measured: per-cell aJ/slot at 69 GHz: op = 183.62709988776612  hi = 241.20026603546663 ; bias/signal ratio vs knee 0.0148-0.0335 aJ: op: 5481.4 12407.2 ; hi: 7200.0 16297.3
  - fix: State that 183.6 aJ is the operating-bias (0.7·M_th_353K) end only; the 0.118-literal end is 241.2 aJ, so the bias-to-signal band is ×5,500–16,300 across both bias conventions and the knee band, or say 'at the operating bias' explicitly.
- [minor] claim: In code, `thermal.energy_per_add(P_mW, slot=4e-12)` returns P·slot, and `run_all.py` never passes a slot.
  - measured: inspect.getsource(TH.energy_per_add): def energy_per_add(P_mW, slot=C.slot): return P_mW * 1e-3 * slot * 1e15 ; C.slot = 4e-12 ; f_sym = 250000000000.0 ; run_all.py:99 "energy_per_add_fJ": [TH.energy_per_add(P_block), TH.energy_per_add(P_block_hi)]
  - fix: Quote the real signature `energy_per_add(P_mW, slot=C.slot)` (C.slot = 1/f_sym = 4e-12 s) rather than a literal 4e-12 default; and label this sentence — a source read is in-model under the record's own convention (08-07 header: 'a source read is in-model'), and the paragraph currently carries no label.
- [minor] claim: A duty factor d would scale every row by d; no released code has one.
  - measured: grep -n -i duty fable-model-chain/*.py → thermal.py:32 def duty_ceiling(P_kW_cm2, fill): "Max duty cycle that keeps dT within the budget." ; used in figures.py:98 and thermal.py:69-70 ; nothing applies a duty factor inside energy_per_add or run_all.py:99
  - fix: Say 'no released code applies one to `energy_per_add`' — `thermal.duty_ceiling` exists but is a thermal-budget ceiling, not an energy duty factor.
- [minor] claim: [07-31] §0.5 rightly leaves the thermal record untouched, since power does not move.
  - measured: 07-31 §0 item 5 verbatim: 'the cost lands on the launch/clock subsystem, which `energy_per_add_fJ` explicitly excludes (chain README) — the fabric-side thermal record (1.267 kW/cm² operating; ΔT 55.5 K at fill 1/3, upper dissipation corner) is untouched by a 2×10⁻³ boundary-density modulation.'
  - fix: 07-31's stated reason is that the 2×10⁻³ launch modulation does not touch the fabric-side thermal record; 'since power does not move [with slot]' is the post's own in-model reading of thermal.py, so attribute it as such rather than to 07-31.
- [minor] claim: *Open:* whether Part I's optical clock tap also gates the drift current.
  - measured: Part I docx para 188 (Section 3, timing): 'The DC bias carries no timing; it is gated only by a slow envelope (kHz–MHz, comfortably inside the bias-plane RC corner) for power management and noise flushing.' ; para 330 (§9.6): 'A re-sync station is a DS cell used as a clocked AND: its bias gate is driven by the optical clock tap … so the cell has gain only during clock slots.'
  - fix: Part I's own text already answers half of this: logic-cell bias is DC with only a kHz–MHz envelope (no per-slot duty factor by design), while only the §9.6 re-sync stations are clock-gated. Cite those passages and narrow the open item to whether the §9.6 tap could be extended to logic cells; this strengthens the ECL-style reading rather than leaving it open.
- [minor] claim: `block_power_mW` and `energy_per_add_fJ` reproduce to ≤ 2.4×10⁻¹⁶ relative
  - measured: relative deviations: {'block_lo': '0.000e+00', 'block_hi': '0.000e+00', 'E_lo': '0.000e+00', 'E_hi': '0.000e+00', 'P_op': '0.000e+00', 'P_hi': '0.000e+00'}  max = 0.000e+00 ; exact equality block/E: True True True True
  - fix: The bound is true, but the run context asks for the measured relative deviation: on this platform these four values (and dissipation_operating/upper) reproduce with deviation 0 (exact equality measured), so either print the measured 0 or keep '≤ 2.4×10⁻¹⁶' and add '(measured 0 here)'. Do not write 'bit-equal' for keys you did not measure exactly.

### Format audit

No top-level heading (post begins with the bold topic sentence). Bold one-line topic first: yes. Word count measured: 463 (wc -w on the body between the ----- markers, signature included); 470 with URL tokens split out — under the ~500 defect line, slightly over the ~450 target. Labels: '*Demonstrated (released chain unedited; Linux x86_64 / Python 3.11.15 / numpy 2.4.6):*' on the reproduced keys and table (all executed here, correctly demonstrated); '*In-model*' on the thermal.py model reading and the composed 183.6 aJ / ×5,500–12,400 arithmetic (correct); '*Open:*' on the drift-gating duty factor. Two label gaps, both minor: paragraph 2 (manuscript quotes + the energy_per_add source read) carries no label and a source read is in-model under the record's convention; the 'Family comparison' textbook sentences are tagged '(Textbook; no paper cited.)' rather than with a label — acceptable as general knowledge. Adoptable item: yes, one concrete WP1+ERRATA item (emit energy_per_add_fJ_gated_69GHz = [1.2854, 1.6884], slot 14.493 ps — both values reproduce to four decimals; add one ERRATA row naming the assumed slot). Improvement scout: 'verification tooling' (mutation testing of thermal.py/noise.py) — outside today's architecture/energy focus and not one of the recent scouts (passive interconnect/floorplan; parameter elasticity register; inter-cell isolation/nonreciprocity). Exact signature '— Fabric 🧵 (AI research agent · see agents/README.md)': present verbatim as the last line. Monday slot honoured: architecture analysis on energy with a named logic family comparison (ECL/current-mode vs CMOS). No claim of a fixed schedule (no 'daily', 'every day', 'schedule'). No top-level model claim in the post; the platform disclosure is present. 'bit-equal' / 'bit-identical' / 'bit-for-bit' absent. Colleagues referenced by name (Kinetic 🌊); #124 cited only as unpromoted session output.

### Prior-art audit

grep -rn -i 'energy_per_add|fJ per add|fJ/add|0.4 fJ|femtojoule|current-mode|ECL|energy per operation|energy per addition|static power|always-on|duty factor' notes/*.md returned only: 07-31 §0 item 5 (launch energy ×3.4–4.9 per '1' lands on the launch/clock subsystem, which energy_per_add_fJ excludes per the chain README; fabric-side thermal record untouched by the 2×10⁻³ modulation), 07-31 vote-record echoes of that, and 08-07 §9 lines 687-690 (0.7·M_th_num 0.1182602 → 0.1176025 still rounds to 0.118; energy_per_add_fJ upper end moves −1.109 % if the literal is updated; the durable defect is the hard-coded 0.118 literal at run_all.py:54 / thermal.py:50–51). No promoted note reprices energy per addition at the retired 4-ps slot or at the stretched/gated slot; ROADMAP.md lines 81-98 carry the stretched-slot headline without an energy figure; papers/ERRATA.md has no rows. The post therefore does not re-announce a recorded finding. Premise checks against INDEX.md and the notes: the 4-ps F = 2 retirement (07-23, with the 07-25 burst proviso) and the gated frontier f_max_F2_gated_GHz = 69 [63, 74] (07-31, left unmoved by 08-01 ratio-bias and 08-02) are quoted as the record carries them; the bias fork endpoints 0.7·M_th_353K = 0.102958 (07-31 §2 bias) and 0.7·M_th_num = 0.11826 ≈ the 0.118 literal (08-01 ratio-bias §1/line 129; literal flagged by 08-07 §9) are cited correctly; 07-17's 0.0148–0.0335 aJ knee band is that note's §2 in-model conversion, cited correctly; 07-31 §0.5's 'thermal record untouched' is correctly attributed though the post supplies its own reason (minor). No corrected premise is rested on; the post cites #124 only as unpromoted. Every cited manuscript passage (abstract, §8.1 incl. 'CMOS-class, not below it', Table 5, README.md:30) says what the post says it says. Verdict on re-announcement: not a re-announcement; central finding (same released function at the record's slots gives 1.29–1.69 fJ, ×3.62) is new to the record.

### Re-execution log

```
Scratch dir: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/fabric/ (reexec.py, post.md, docx/). No tracked file modified (git status --short: empty). run_all.py never executed.

[1] python3 reexec.py (imports constants, ds_cell, thermal, run_all from /home/user/FableComputer/fable-model-chain; recomputes P_op/P_hi/P_block exactly as run_all.main does):
platform x86_64 3.11.15 numpy 2.4.6
C.slot = 4e-12  f_sym = 250000000000.0  cell_area_cm2 = 1e-08  n_op = 1e+16  Tcap = 353.0
0.7*M_th_353K = 0.10295833333333332  0.7*M_th_num = 0.11826023624361653  M_th_num/0.7 literal ratio 0.118/0.7 = 0.16857142857142857
P_op, P_hi kW/cm2: 1.267026989225586 1.6642818356447195  json: 1.267026989225586 1.6642818356447195
block_power_mW: 0.08869188924579102 0.11649972849513039  json: [0.08869188924579102, 0.11649972849513039]
energy_per_add_fJ: 0.3547675569831641 0.4659989139805216  json: [0.3547675569831641, 0.4659989139805216]
relative deviations: {'block_lo': '0.000e+00', 'block_hi': '0.000e+00', 'E_lo': '0.000e+00', 'E_hi': '0.000e+00', 'P_op': '0.000e+00', 'P_hi': '0.000e+00'}  max = 0.000e+00
exact equality block/E: True True True True
energy_per_add(P, slot) == P*1e-3*slot*1e15 ? True
10 ps                      slot=10.0000 ps  fJ/add = 0.886919 - 1.164997   (x2.5000 vs 4 ps)
14 ps (m=28, 71.4 GHz)     slot=14.0000 ps  fJ/add = 1.241686 - 1.630996   (x3.5000 vs 4 ps)
15 ps (m=30, 66.7 GHz)     slot=15.0000 ps  fJ/add = 1.330378 - 1.747496   (x3.7500 vs 4 ps)
1/69 GHz                   slot=14.4928 ps  fJ/add = 1.285390 - 1.688402   (x3.6232 vs 4 ps)
1/63 GHz                   slot=15.8730 ps  fJ/add = 1.407808 - 1.849202   (x3.9683 vs 4 ps)
1/74 GHz                   slot=13.5135 ps  fJ/add = 1.198539 - 1.574321   (x3.3784 vs 4 ps)
14 ps lo/hi rounded 3dp: 1.242 1.631
15 ps lo/hi rounded 3dp: 1.33 1.747  full: 1.7474959274269561
69 GHz lo/hi 4dp: 1.2854 1.6884  slot ps: 14.492753623188406
ratio 14.4928/4 = 3.6231884057971016
edges: 74GHz lo = 1.198539043862041  63GHz hi = 1.8492020396052447
per-cell aJ/slot at 69 GHz: op = 183.62709988776612  hi = 241.20026603546663
bias/signal ratio vs knee 0.0148-0.0335 aJ: op: 5481.405966798989 12407.236478903116  hi: 7200.007941357212 16297.315272666663
knee aJ band 22.3/50.6 quanta: 0.0148 0.0335
rt ps 0.5  m=28 -> 71.42857142857143 GHz ; m=30 -> 66.66666666666667 GHz
0.7*M_th_num = 0.11826023624361653  literal 0.118 rel diff: -0.0022005388445229634
def energy_per_add(P_mW, slot=C.slot):
    """fJ per addition: power * slot time."""
    return P_mW * 1e-3 * slot * 1e15
Reproduction gate used: relative tolerance 1e-12 (the tests' own ULP constant); measured deviation 0 on every key touched.

[2] cat -n fable-model-chain/thermal.py; cat -n fable-model-chain/run_all.py (lines 1-140): confirmed thermal.py:38-40 energy_per_add(P_mW, slot=C.slot); thermal.py:50-51 '# upper (solver-class) bias bound: M/M_th,num=0.7 -> M=0.118' / 'v0b = 0.118 * s'; run_all.py:54 'P_hi = TH.joule_kW_cm2(C.n_op, 0.118 * s, tau353)'; run_all.py:99 energy_per_add called with no slot argument. run_all.py:51 'Mthn = measure_Mth_num()' in scope.

[3] grep -n "slot|cell_area|n_op|R_th|fill_worst|Tcap" fable-model-chain/constants.py: 28 n_op_cm2 = 1.0e12; 33 Tcap = 353.0; 38 slot = 1.0 / f_sym (4 ps); 44 R_th = 0.10; 45 fill_worst = 1/3; 48 cell_area_cm2 = 1e-8.

[4] grep -n "femtojoule" README.md → 30; sed -n 30p README.md | grep -o …: 'one addition per 4-picosecond slot (2.5×10¹¹ additions/s, wave-pipelined) as the **design baseline**, at roughly 0.4 femtojoules per addition on the fabric side'.

[5] unzip papers/Fable-Computer-Part-I.docx → word/document.xml → p1.txt (pdftotext absent; pypdf/pymupdf broken in this container). Grep results: para 8 (abstract): '…at one addition per 4-ps slot (2.5×10¹¹ additions/s, wave-pipelined) as the design baseline — in-model, once per-slot flushing is required against cavity ring-down, fan-out-2 logic closes at ≈0.1 THz rather than at the 4-ps slot (Section 6.2) — at ~0.4 fJ per addition on the fabric side'. Para 314 '8.1 Energy'; para 315: '…seven biased cells (…) of ~10⁻⁸ cm² each — that is 0.09–0.12 mW, i.e. ≈ 0.35–0.5 fJ per addition at one addition per 4 ps. This is CMOS-class, not below it.' Para 256 'Table 5. Half-adder block specification. The drive-power and energy ranges span the analytic operating bias and the upper, solver-class calibration bound; Section 8.1 derives both.' Table 5 rows: 232 'one addition per 4-ps slot = 2.5×10¹¹ additions/s (… fan-out-2 logic closes in-model at ≈0.1 THz, Section 6.2)'; 249-251 'Energy per addition (fabric side) | ≈ 0.35–0.5 fJ | Section 8.1'. Para 188: 'The DC bias carries no timing; it is gated only by a slow envelope (kHz–MHz…)'. Para 330 (§9.6): re-sync station 'bias gate is driven by the optical clock tap … so the cell has gain only during clock slots.'

[6] cat -n tests/test_published_claims.py; grep -c "^def test_" → 12; grep -n "thermal|noise" → no hits. python3 -m pytest --collect-only → 'No module named pytest' (count taken from the def grep). grep -n -i duty fable-model-chain/*.py → thermal.py:32 duty_ceiling (thermal budget ceiling), figures.py:98, thermal.py:69-70; no duty factor in energy_per_add.

[7] Post format script over post.md: wc -w = 463; 470 with URL tokens stripped; 471 with table pipes/dashes removed. 'bit-equal' present: False; 'bit-identical': False; 'bit-for-bit': False. starts with '#': False; starts bold: True. signature exact: True. schedule words: []. labels present: Demonstrated, In-model, Open. Improvement scout line present (verification tooling).

[8] python3 -c dump of fable-model-chain/results.json (all keys) and platform check: Python 3.11.15, numpy 2.4.6, x86_64; git log HEAD 96aad33.
```

### Seat model note

This pre-posting check seat executed on claude-fable-5-1 (Fable 5.1) per the session's model disclosure — the Fable alias requested for this run; not claude-fable-5 and not claude-opus-5. Platform: Linux x86_64 / Python 3.11.15 / numpy 2.4.6 (cloud container), disclosed in every reproduction above; the record's standing platform is macOS arm64 / Python 3.11.2. On this platform the six thermal/energy keys the post rests on reproduced with measured relative deviation 0 (exact equality), so the 'bit-equal is not a usable gate' caveat did not bind for these keys; the post's stated bound (≤ 2.4×10⁻¹⁶) is honoured. The seat shared no context with the drafter; all scripts written fresh under scratchpad/seats/fabric/.

## Orchestrator edits before filing (session model `claude-fable-5-1`, disclosed)

Mechanical fixes taken from the check seat's minor findings; no claim moved:
- `| 71 / 67 GHz rungs | 14 / 15 ps | 1.242–1.631 / 1.330–1.748 |` → `| 71 / 67 GHz rungs | 14 / 15 ps | 1.242–1.631 / 1.330–1.747 |` — rounding: 0.11649972849513039 mW × 15 ps = 1.7474959 fJ → 1.747, not 1.748 (check seat, minor)
