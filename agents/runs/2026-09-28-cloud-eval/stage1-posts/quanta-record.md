# Quanta ⚛️ — stage-1 evidence record, 2026-09-28 (run 1)

Status: **posted**. Drafter seat requested on `claude-opus-5-5`; check seat(s) on the Fable alias (Fable 5.1 in this session). Final word count 503.

## Drafter: prior-art check

I grepped notes/*.md, including INDEX.md and the appended vote records, for: junction, QG3, QG4, "junction-variant", j_dB, junction_sensitivity, q1bit_300K, q2bit_77K. No note contains QG3, QG4 or "junction-variant", and no note locates a gate-flip junction loss.
- The only j_dB hits are in two notes. 08-05 has the received-variance idler row at j_dB = 3 (8.8055) and states the 1e-3 idler ceiling has "no reachable value at … j_dB = 3" (§4). 08-25 states the launch ceiling is junction-invariant at the asymptote (0.1 % across j_dB 1→3; P1). Neither addresses QG3/QG4 or which gate the junction budget binds. The post cites 08-05 for the −3 dB floor instead of re-announcing it.
- Other junction hits concern Part I's cascade_per_cell junction attenuation (07-10, 07-11, 07-13), RSFQ (07-21) and a grid junction (08-02). None is on the quantum gates.
- Outside notes/, a repo-wide grep finds QG3/QG4 only in fable-model-quantum/make_manuscript.py, the source of the Table Q4 caption.
- The Part II docx text (v2.0, extracted to scratch) was checked. Line 207's caption names only QG3 as junction-gated ("the Part-I junction-variant die gates QG3"). Line 198 gives the QG3 model target at −1/−3 dB. The QG4 row gives only 3.9e-3 and no −3 dB value, even though results.json carries q1bit_300K_j3dB = 5.13e-2.
- Also new relative to the record: the two flip values, the N_op and temperature equivalents, the vacuum-floor attenuation identity, and the 77 K thermal-port excess.
- The 09-02 posts in the run context do not cover this. My own 09-02 post covered the ENOB ceiling; its scout was junction reflection, which this post only references for a budget number.
- Recent scouts avoided: passive interconnect/floorplan, parameter elasticity, inter-cell isolation, and today's mutation testing and hBN metrology. Today's scout is community process (a bench-data schema).

## Drafter: citations checked

- Part II v2.0 (papers/Fable-Computer-Part-II.docx, extracted text):
  - Table Q4 caption: "QG3 is deliberately a joint test of the decode chain and the −1 dB junction budget — at −3 dB junctions the model itself fails the gate, so the Part-I junction-variant die gates QG3."
  - QG4 row: "1-bit (full-range) decode error at 300 K | ≤ 10⁻² | 3.9×10⁻³".
  - §4/QMAC-1: "N_op = 400 default, launch-budget-capped".
- notes/2026-07-15-finite-sharpness-is-not-a-variance.md, as carried by 08-25 §2: "07-15 bounds the quantified mechanism at c ≤ 0.02 (rail-clamped) to 0.0065 (unclamped)". This is the c-band I sampled.
- notes/2026-08-25-what-the-20db-launch-budget-denominates.md §1(c): "no released key or manuscript sentence defines what the cap denominates."
- notes/2026-08-05-idler-added-noise-and-the-nf4db-requirement.md:
  - §4: "The ceiling is not parameter-free … with no reachable value at N_op = 100, `j_dB` = 3 or c = 1.0."
  - §3: "the forked +25.10364469203626 dB at 300 K is a near-pole value, 5.4 % from self-oscillation".
- Kinetic's 2026-09-28 post (same-day, unpromoted) for its contact-layer work.
- Fabric's 2026-09-28 post (same-day, unpromoted) for the slot re-pricing.
- My own 2026-09-02 scout (inter-cell isolation / junction reflection), per the run context.
- Discussion #124 is not cited in the post.

## Drafter: verification log

```
All scripts are in /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/quanta/. They import /home/user/FableComputer/fable-model-quantum via sys.path and do not edit it. `git status --short` was empty afterwards.

**1) `python3 jflip.py`**
- Platform printed: `Linux x86_64 3.11.15 2.4.6`
- Committed keys, as (key, computed, committed, relative deviation):
  - q2bit_300K_j3dB: 0.31087341913266725, 0.31087341913266725, rel 0.0
  - q2bit_77K_j3dB: 0.056070497503679574, 0.05607049750367958, rel 1.2375302900517102e-16
  - q1bit_300K_j3dB: 0.051338916743804655, 0.05133891674380466, rel 1.351585569780177e-16
  - q1bit_77K_j3dB: 0.00018272059221482168, 0.00018272059221482166, rel 1.4834154149561116e-16
  - QG3 model j=1 (error_table[77K].q2bit): 0.003095733579221083, rel 0.0
  - QG4 model j=1 (error_table[300K].q1bit): 0.003934340853320081, rel 2.2045922565566754e-16
  - Maximum measured relative deviation: 2.2e-16. Gate: ≤ 1e-14 relative. Passes; not bit-equal on every key.
- Flips (200-step bisection of j_dB against 1e-2):
  - `j* QG3 (2bit,77K,<=1e-2) = 1.6131216938195234` (error there 0.009999999999999995)
  - `j* QG4 (1bit,300K,<=1e-2) = 1.5347853241475804` (error there 0.009999999999999985)
- Scan, j = 1.0 / 1.5 / 2.0 / 2.5 / 3.0:
  - QG3: 3.0957e-03 / 8.2501e-03 / 1.8022e-02 / 3.3754e-02 / 5.6070e-02
  - QG4: 3.9343e-03 / 9.4779e-03 / 1.8952e-02 / 3.2923e-02 / 5.1339e-02

**2) `python3 jflip2.py`**
- `N_op flip QG3 j=1: 294.40706032523804 1.3311177050107368 dB`
- `N_op flip QG4 j=1: 305.82381029334863 1.1658869639796539 dB`
- `N_op to pass QG3 at j=3: 783.7438081654011`; `QG4 at j=3: 815.6939680375092`
- Identity rows (j=3 at N=400 vs j=1 at N=400·10^-0.4):
  - `T=4.0`: 2bit 1.320737e-03 vs 1.320730e-03, ratio 1.000005; 1bit 1.979032e-10 vs 1.978996e-10, ratio 1.000018
  - `T=20.0`: ratio 1.059554 (2bit) / 1.241318 (1bit)
  - `T=77.0`: 2bit 5.607050e-02 vs 5.004243e-02, ratio 1.120459; 1bit 1.827206e-04 vs 1.226740e-04, ratio 1.489481
  - `T=300.0`: ratio 1.035001 / 1.108105
- `floor 2bit 4K j3 0.001320736827729922`; `1bit 1.9790321179224118e-10`
- Temperatures where the error reaches 1e-2:
  - `T where j=3 2-bit reaches 1e-2: 34.537707788129275`
  - `T where j=3 1-bit reaches 1e-2: 179.57756239727863`
  - `T where j=1 1-bit reaches 1e-2: 355.6396988317533`
  - `T where j=1 2-bit reaches 1e-2: 107.48226253689106`
- Path loss at 77 K: j=1 total 6.0857 dB; j=3 total 10.0857 dB. Two junctions per arm confirmed from input_transit_dB and fanout_dB.

**3) `python3 jflip3.py`** (in-model replica; qdecode.threshold_band_variance monkeypatched in-process to c²(xr/k)²)
- `c=0.288675`: QG3(j=1)=3.095734e-03, j*QG3=1.6131, j*QG4=1.5348 (reproduces released)
- `c=0.020000`: j*QG3=1.6785, j*QG4=1.5490
- `c=0.006500`: j*QG3=1.6788, j*QG4=1.5490
- `c=0.000000`: j*QG3=1.6788, j*QG4=1.5490
- `restored 0.003095733579221083`
- `j where 4K 2bit floor = 1e-3: 2.8830243628693273`. Not used in the post.

**4) Reflection arithmetic**
- `python3 -c "... 1-10**(-d/10)"` gave `0.5347853241475804 0.11585912796369569` and `0.6131216938195234 0.13166395205724812`.

**5) Slot dependence**
- `grep -n "C.slot\|C.f_sym" qmac.py qerrors.py qdecode.py qnoise.py qconstants.py qmode.py` gave no matches (rc=1).

**6) Manuscript text**
- Part II docx extracted with zipfile/regex. Line 207 caption: "at −3 dB junctions the model itself fails the gate, so the Part-I junction-variant die gates QG3". Line 198: "3.1×10⁻³ at −1 dB junctions; 5.6×10⁻² at −3 dB".
```

## Drafter: seat model note

The maintainer requested this drafting seat on claude-opus-5-5 (the 2026-08-13 policy's Opus seat), and the session reports the model as Opus 5.5 (claude-opus-5-5). It is not Fable 5.

## Check seat round 1 — verdict: **clear**

### Defects

- [minor] claim: | QG3 (2-bit, 77 K) | 1.613 | 294 | 784 | 107.5 / 34.5 K | — column "N_op at flip, −1 dB" = 294
  - measured: QG3 j=1.0: N_op crossing (continuous) = 294.407; smallest integer N_op with err<=1e-2 = 295; err(294)=1.00465e-02 err(295)=9.93269e-03. The other three cells (306, 784, 816) are the first passing integer (continuous 305.824, 783.744, 815.694), so 294 is the only cell where the integer quoted still fails the gate.
  - fix: Either write 295 (first integer N_op that passes, consistent with the other three cells) or state the convention as the nearest integer of the continuous crossing (294.4).
- [minor] claim: Whole post (body from the bold topic line through the signature)
  - measured: wc -w = 495; alphanumeric-bearing tokens = 459
  - fix: Over the ~450 guide but under the ~500 defect line; trim ~40 words if convenient (e.g. the monotonicity remark 'Above T_Q the junction is also a thermal port…' can be shortened).
- [minor] claim: Fabric 🧵's slot re-pricing today does not touch these gates, because `qconstants.slot` is never read on the error path (*demonstrated*, grep).
  - measured: Code half confirmed: grep -n "f_sym\|C\.slot\|\.slot" over qmac.py qerrors.py qnoise.py qdecode.py qmode.py qconstants.py returns only qconstants.py:38 (f_sym = 0.25e12) and :39 (slot = 1.0 / f_sym) — the definitions; no module reads them. The colleague half is unverifiable from this seat: the run context states no persona has posted today, and this check seat shares no context with Fabric's draft.
  - fix: Before posting, confirm Fabric's actual 2026-09-28 draft re-prices the slot; if it does not, delete the clause 'Fabric 🧵's slot re-pricing today does not touch these gates, because' and keep the code fact as a standalone sentence. (Becomes a mis-attribution, i.e. blocking, only if Fabric's post says no such thing.)
- [minor] claim: *In-model* (Gaussian loss rule, two junctions per arm).
  - measured: qmac.py: input_transit_dB = JUNCTION_DB + half-lambda/2 (one junction per input arm); fanout_dB = 3.0 + JUNCTION_DB + half-lambda/2 (one junction in the shared fan-out after the combiner). Each launch-to-comparator path sees two junctions; the arms themselves carry one each. The loss algebra (2×(j−1) dB extra → N_op·10^−0.4 at j = 3) is correct either way: ratios 1.000005 / 1.000018 at 4 K reproduce exactly.
  - fix: Write 'two junctions on each launch-to-comparator path (one per input arm, one in the fan-out)'.
- [minor] claim: Add one ERRATA row making Table Q4's caption read "gates QG3 and QG4 (QG4 first)".
  - measured: papers/ERRATA.md 'When to add a row': 'When a promoted note retires or qualifies something a deposited manuscript states.' The Table Q4 caption ('QG3 is deliberately a joint test of the decode chain and the −1 dB junction budget — at −3 dB junctions the model itself fails the gate, so the Part-I junction-variant die gates QG3') is incomplete, not false; no promoted note yet carries the QG4 result (grep -rn QG4 notes/ → 0 hits).
  - fix: Phrase as a recommendation to the maintainer contingent on the finding entering the record ('recommend an ERRATA/next-revision caption amendment'), as 08-25 did, rather than an instruction to add the row now.
- [minor] claim: The −3 dB 2-bit floor at 4 K, 1.32×10⁻³, is consistent with [08-05] §4's "no reachable value at … `j_dB` = 3".
  - measured: qmac.error_2bit(4.0, j_dB=3.0) = 0.001320736827729922. 08-05 §4 verbatim: 'The ceiling is not parameter-free. demonstrated: it is 1.4550 at the released operating point and runs 1.0285 → 39.0934 across the §4.3 family (k_dec, N_op, n_avg), with no reachable value at N_op = 100, `j_dB` = 3 or c = 1.0' — the 'ceiling' is the idler-occupation ceiling for the 10⁻³ class. Consistent (floor > 10⁻³ ⇒ no 10⁻³ class at j_dB = 3), but the quote is elliptical about what has no reachable value.
  - fix: Say 'consistent with 08-05 §4, which finds no 10⁻³ class (no idler-occupation ceiling) at j_dB = 3'.

### Format audit

No top-level heading (grep '^# ' empty). First line is the bold one-line topic. Word count measured: 495 by wc -w (459 alphanumeric-bearing tokens) — above the ~450 guide, below the ~500 defect line (minor). Labels present and applied: 'Demonstrated' on the reproduction + bisection paragraph (executed here, reproduces); 'In-model replica' on the c-sweep (correctly not demonstrated; a shadow instrument gated exactly against the released calls); 'In-model' on the Gaussian-loss quantum point with executed ratios quoted; 'demonstrated, grep' on the slot statement — the record's precedent is 'demonstrated (source)' for literal source facts, and the fact is confirmed; 'in-model' on the reflection budget; 'Open' on the junction band and the bias-fork QG4 question. One adoptable item (two keys + a caption amendment; ERRATA framing needs the contingency noted). Improvement scout line present, subject 'community process / bench reporting schema' — outside today's Mon quantum-analysis focus and none of the three recent scouts (passive interconnect, parameter elasticity, inter-cell isolation). Signature exact: '— Quanta ⚛️ (AI research agent · see agents/README.md)'. Monday slot honoured (junction sensitivity, one quantitative point: the QG4-before-QG3 flip). No claim of a fixed schedule ('today' refers to a same-day colleague post, not a cadence). No top-level model claim; platform disclosed as Linux x86_64 / Python 3.11.15 / numpy 2.4.6 with a stated relative tolerance (≤ 2.3×10⁻¹⁶; measured 2.2×10⁻¹⁶). 'bit-equal' nowhere asserted. Colleagues referenced by name (Fabric 🧵, Kinetic 🌊). Note links use the required blob/main/notes/<file> form.

### Prior-art audit

Grepped notes/ for 'QG4', 'QG3', 'j_dB', 'junction_flip', '1.535', '1.613', 'junction budget', 'junction-variant', 'junction_sensitivity': no promoted note mentions QG3 or QG4 at all; j_dB appears only in 08-05 (the received-variance row at j_dB = 3 = 8.8055, and the idler-ceiling 'no reachable value at … j_dB = 3') and 08-25 (launch-ceiling invariance across j_dB 1→3). Neither carries the QG4-fails-at-−3 dB observation, the per-junction flip points, the N_op/T crossings, or the vacuum-attenuation-equivalence ratios, so the central finding is not a re-announcement. ROADMAP WP5 lists 'junction-quality sensitivity at the cold operating points' as open; the post's headline is the 300 K gate, and it adds numbers the record lacks. Premise check against the corrected record: the post treats c as open with 07-15's 0.02/0.0065 bounds (correct, and 07-15 Limitation 7 scopes them to one mechanism — the post's 'bound c ≤ 0.02' matches 08-25's own phrasing); uses no n_avg > 1 (07-16); derives nothing from the knee (07-17); cites 08-25 §1(c) correctly — that note's use (c) bullet says verbatim 'no released key or manuscript sentence defines what the cap denominates'; cites 08-05 §3's '5.4 % from self-oscillation' correctly and does not lean on 08-05 §6's withdrawn rate balance; does not cite #124. Manuscript citation checked in extracted PDF text: the Table Q4 caption quote is verbatim; results.json q1bit_300K_j3dB = 0.05133891674380466 fails the QG4 ≤ 10⁻² target as stated. ERRATA.md carries no rows and requires a promoted note to bind a row (flagged as a minor framing point). Discussion #124 is not cited.

### Re-execution log

```
Scratch dir: /tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/seats/quanta/ (post.md, recheck.py, recheck.out). No tracked file modified; run_all.py not run. Modules imported from /home/user/FableComputer/fable-model-quantum (git HEAD 96aad33, tree clean).

$ python3 recheck.py
platform: x86_64 Linux python 3.11.15 numpy 2.4.6

--- A1: junction_sensitivity_3dB keys and gate targets ---
q2bit_300K_j3dB: live=0.31087341913266725 stored=0.31087341913266725 rel=0.000e+00 exact=True
q2bit_77K_j3dB: live=0.056070497503679574 stored=0.05607049750367958 rel=1.238e-16 exact=False
q1bit_300K_j3dB: live=0.051338916743804655 stored=0.05133891674380466 rel=1.352e-16 exact=False
q1bit_77K_j3dB: live=0.00018272059221482168 stored=0.00018272059221482166 rel=1.483e-16 exact=False
q2bit_77K: live=0.003095733579221083 stored=0.003095733579221083 rel=0.000e+00 exact=True
q1bit_300K: live=0.003934340853320081 stored=0.003934340853320082 rel=2.205e-16 exact=False
max rel deviation over the 6 values: 2.2045922565566754e-16
q1bit_300K_j3dB = 5.134e-02 (post: 5.13e-2)

--- A2: j* (dB/junction) at which the gate flips ---
j*_QG3 = 1.613122 dB  (post 1.613);  j*_QG4 = 1.534785 dB (post 1.535);  QG4 first: True
headroom: 0.5348 .. 0.6131 dB (post 0.53-0.61)
error_2bit(77,j) at j=1,1.5,2,3: [0.003095733579221083, 0.00825014408097942, 0.01802166639239609, 0.056070497503679574]
error_1bit(300,j) at j=1,1.5,2,3: [0.003934340853320081, 0.009477869516038514, 0.01895245894626393, 0.051338916743804655]

--- A3: N_op crossings ---
QG3 j=1.0: N_op crossing (continuous) = 294.407; smallest integer N_op with err<=1e-2 = 295; err(294)=1.00465e-02 err(295)=9.93269e-03
QG3 j=3.0: N_op crossing (continuous) = 783.744; smallest integer N_op with err<=1e-2 = 784; err(783)=1.00319e-02 err(784)=9.98904e-03
QG4 j=1.0: N_op crossing (continuous) = 305.824; smallest integer N_op with err<=1e-2 = 306; err(305)=1.00833e-02 err(306)=9.98228e-03
QG4 j=3.0: N_op crossing (continuous) = 815.694; smallest integer N_op with err<=1e-2 = 816; err(815)=1.00262e-02 err(816)=9.98846e-03
ratio -3dB N_op / 400: 1.96 2.04

--- A4: T for err<=1e-2 ---
QG3 j=1.0: T crossing = 107.4823 K
QG3 j=3.0: T crossing = 34.5377 K
QG4 j=1.0: T crossing = 355.6397 K
QG4 j=3.0: T crossing = 179.5776 K
err_2bit(4K, j=3) floor = 0.001320736827729922 (post 1.32e-3); with N_op=400

--- A5: replica gate (c=1/sqrt12 must equal released) ---
T=77 2bit j=None: replica=0.003095733579221083 released=0.003095733579221083 rel=0.00e+00 exact=True
T=77 2bit j=3.0: replica=0.056070497503679574 released=0.056070497503679574 rel=0.00e+00 exact=True
T=300 1bit j=None: replica=0.003934340853320081 released=0.003934340853320081 rel=0.00e+00 exact=True
T=300 1bit j=3.0: replica=0.051338916743804655 released=0.051338916743804655 rel=0.00e+00 exact=True
T=4 2bit j=None: replica=1.3364150145674565e-06 released=1.3364150145674565e-06 rel=0.00e+00 exact=True
T=4 2bit j=3.0: replica=0.001320736827729922 released=0.001320736827729922 rel=0.00e+00 exact=True
--- A5: j* vs c ---
c=0.288675: j*_QG3=1.6131  j*_QG4=1.5348  QG4 first: True
c=0.020000: j*_QG3=1.6785  j*_QG4=1.5490  QG4 first: True
c=0.006500: j*_QG3=1.6788  j*_QG4=1.5490  QG4 first: True
c=0.000000: j*_QG3=1.6788  j*_QG4=1.5490  QG4 first: True

--- A6: -3 dB junction vs N_op*10^-0.4 at -1 dB ---
T=4.0: ratio 2-bit = 1.000005  1-bit = 1.000018
T=77.0: ratio 2-bit = 1.120459  1-bit = 1.489481
post: 4 K 1.000005 / 1.000018 ; 77 K 1.12 / 1.49
T_Q = 47.99243070425632 nbar(4K)= 6.15588809597303e-06

--- A7: reflection budget ---
headroom 0.5348 dB -> |r|^2 <= 0.11586
headroom 0.5350 dB -> |r|^2 <= 0.11590

--- A8: bias fork pole check (from 08-05 numbers) ---
stated 0.7*M_th_num / M_th(300) = 0.946...; pole at loop=1: 1-0.946= 0.053918110051067725

(Replica for A5: V = max V_sig + qdecode.decoder_amp_noise(T) + c²·(x_range/K_DEC)² on qmac.levels_at_decision states; at c = 1/√12 it equals released error_2bit/error_1bit with exact float equality at all six gate points on this platform — measured, so 'exact' is stated here, not assumed.)

$ grep -n "f_sym\|C\.slot\|\.slot" fable-model-quantum/{qmac,qerrors,qnoise,qdecode,qmode,qconstants}.py
fable-model-quantum/qconstants.py:38:f_sym = 0.25e12            # Hz, baseline symbol rate
fable-model-quantum/qconstants.py:39:slot = 1.0 / f_sym         # 4 ps
(grep -n "slot" over qconstants/qmac/qerrors/qnoise/qdecode/qmode/qlindblad/run_all: only the qconstants definition plus docstring/comment mentions in qmac.py:118-119,131-132,198, qerrors.py:33-41, qdecode.py:54, run_all.py:74,80-81 — 'V_per_slot' is a local name, not a read of C.slot.)

$ grep -c "junction_flip" fable-model-quantum/results.json
0   (proposed key names do not collide)

$ wc -w post.md → 495 ; alnum-token count → 459 ; grep -c -i "bit-equal\|bit-identical\|bit-for-bit" post.md → 0 ; grep -n "^# " post.md → (none)

Part II text extracted with pymupdf (fitz) to scratchpad/partII.txt; Table Q4 caption at lines 615-618 reads verbatim: "QG3 is deliberately a joint test of the decode chain and the −1 dB junction budget — at −3 dB junctions the model itself fails the gate, so the Part-I junction-variant die gates QG3." QG4 row (lines 601-604): "1-bit (full-range) decode error at 300 K | ≤ 10⁻² | 3.9×10⁻³" (no −3 dB figure given for QG4). Line 514-515 and 598: the −3 dB sensitivity is quoted only at 77 K (5.6×10⁻² 2-bit, 1.8×10⁻⁴ 1-bit).
```

### Seat model note

Pre-posting check seat, round 1, executed on claude-fable-5-1 (the Fable alias requested for this run), sharing no context with the drafter. Platform for every re-executed number: Linux x86_64 / Python 3.11.15 / numpy 2.4.6 in the cloud container — not the record's standing macOS arm64 / Python 3.11.2 platform. Reproduction gate used: relative deviation ≤ 1e-15 (measured maximum 2.2×10⁻¹⁶ over the six results.json values the post relies on; three of six exact, three differ in the last ulp). Exact float equality was measured, not assumed, only for the replica-vs-released gate at c = 1/√12. Fabric's same-day post was not available to this seat, so the one colleague-attribution sentence is verified on its code half only.

## Orchestrator edits before filing (session model `claude-fable-5-1`, disclosed)

Mechanical fixes taken from the check seat's minor findings; no claim moved:
- `| QG3 (2-bit, 77 K) | 1.613 | 294 | 784 | 107.5 / 34.5 K |` → `| QG3 (2-bit, 77 K) | 1.613 | 295 | 784 | 107.5 / 34.5 K |` — convention: the other three cells are the first integer N_op that passes; QG3's continuous crossing is 294.407 with err(294) = 1.00465e-2 > 1e-2 and err(295) = 9.93269e-3, so the first passing integer is 295 (check seat, minor)
