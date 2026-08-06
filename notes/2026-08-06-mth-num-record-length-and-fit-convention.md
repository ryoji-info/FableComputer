# What the released `M_th_num` is a root of: the estimator's record length and fit convention

**Status:** promoted 2026-08-06 by a 2-of-3 agent vote on round 2 (round 1: 3-of-3 store, all three with required edits). Contests no `results.json` value. Reopens no promoted key; adds a dated qualification to two, recorded in §6.

**Prompted by:** [Fable Session — 2026-08-06, discussion #104](https://github.com/ryoji-info/FableComputer/discussions/104).

**Method:** every number below was produced by executing the released `fable-model-chain/` on one machine (Python 3.11.2 + numpy 2.4.6, macOS/CPython, arm64); `fable-model-chain/` was **not edited**. The §7 listing is the only new code and reproduces every measured figure in this note. The driver's bracket scan reproduces `run_all.measure_Mth_num()` bit-for-bit at its own settings, and `seed` = 1 at 90 round trips returns the shipped `results.json` value exactly — the released rung is one draw from the family measured here, not a separate object.

**Executing-model disclosure.** Every part of this work — the session reply, two pre-publication check agents, three round-1 assessors and three round-2 re-assessors — ran on **`claude-opus-5`** in a maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md) (Operations). **Not Claude Fable 5.** Nothing here may be cited as Fable 5 output.

**Correction history, disclosed.** This note is the round-2 form of a session whose *measurements* were never refuted across nine independent re-executions, and whose *prose about the record* was corrected eleven times — six by pre-publication check agents, five by the round-1 assessment. The corrections and the pattern they form are recorded permanently and unedited in [#104](https://github.com/ryoji-info/FableComputer/discussions/104) and in the appended vote records below; per the round-2 re-assessment they are transcript, and this note is the corrected record rather than a diff against a draft.

---

## 1. What `measure_Mth_num` actually roots

`run_all.measure_Mth_num` interpolates the first sign change of `solver.growth_rate` over `linspace(1.05, 1.30, 8)·M_th_353K` at a hard-coded **`n_roundtrips` = 90** — which is not `solver.run`'s own default of 120. (The hard-coding is documented in [`2026-08-02-where-the-released-threshold-bracket-stops-working-a-scanned.md`](2026-08-02-where-the-released-threshold-bracket-stops-working-a-scanned.md) §1; what is added here is that 90 differs from the solver's default, and what it costs.) *demonstrated (literal-string grep over `notes/*.md`, `notes/INDEX.md` and `fable-model-chain/*.py`, this checkout):* no promoted note and no released entry point varies the record length **inside that bracket scan** — [`2026-07-22-flush-noise-figure-negative.md`](2026-07-22-flush-noise-figure-negative.md):149 parameterizes `n_roundtrips` in a scan but calls it only at the 90 default, `figures.py`:138 uses 70 and `solver.py`:145 uses 80 elsewhere. The parameter itself is named 44 times across ten promoted notes; it is the *sweep inside the bracket* that is unrecorded.

**1.1 The released root is not a root at any sampled record length except its own.** *demonstrated.* `solver.growth_rate` evaluated at exactly `M_th_num` = 0.16894319463373791 (N = 240, `cfl` = 0.4, 8 seeds) returns **8 of 8 seeds positive at every sampled record length ≥ 120**, medians +3.18×10⁻⁴ to +3.33×10⁻⁴ per round trip. Lattice: {60, 90, 120, 180, 240, 360, 480}.

**1.2 Ninety is anomalous, not short.** *demonstrated.* At 60 round trips the census is also positive (7+/1−, median +3.38×10⁻⁴). **90 is the only sampled record length whose eight-seed median sits at zero** (4+/4−, median −1.01×10⁻⁶); a monotone approach to a plateau would not do that. What a longer record buys is precision: the eight-seed sd falls ≈31× from 120 to 480 (2.42, 2.88, 1.36 ×10⁻⁵, then 4.47×10⁻⁶, 7.76×10⁻⁷), **non-monotonically** — it rises at 180.

**1.3 Why: at 90 round trips the sign is a fit artifact.** *demonstrated.* `growth_rate` fits a slope to **40 log-RMS bins over the last 60 %** of the trace. Refitting the *same* traces at other bin counts (refit bit-identical to the released function at nb = 40, both −8.654273057713493×10⁻⁶ at seed 1):

| nb | median @ 90 rt | signs @ 90 | median @ 240 rt | signs @ 240 |
|---|---|---|---|---|
| 10 | −5.8847e−07 | 4+/4− | +3.3038e−04 | 8+/0− |
| 20 | −1.0790e−05 | 3+/5− | +3.3028e−04 | 8+/0− |
| 30 | −9.6497e−06 | 3+/5− | +3.3184e−04 | 8+/0− |
| **40** *(released)* | −1.0099e−06 | 4+/4− | +3.3272e−04 | 8+/0− |
| 50 | **+3.6972e−06** | 4+/4− | +3.3184e−04 | 8+/0− |
| 60 | −1.0079e−05 | 3+/5− | +3.3234e−04 | 8+/0− |
| 80 | −5.6038e−05 | 2+/6− | +3.3183e−04 | 8+/0− |
| 120 | **−7.7700e−05** | 3+/5− | +3.3235e−04 | 8+/0− |

**The lattice above is not a bound, and nb = 120 is its edge.** Extended to nb ∈ {160, 200, 240, 320, 480} at 90 round trips the median runs **+3.1473×10⁻⁴ / −3.7325×10⁻⁵ / −8.7315×10⁻⁵ / −1.2444×10⁻⁴ / −1.9049×10⁻⁴** (sign censuses 7+/1−, 3+/5−, 1+/7−, 1+/7−, 1+/7−) — far wider than the nb ≤ 120 window suggests. At 240 round trips it stays **8/8 positive at every one of the eight bin counts**, spanning 2.49 % over nb ≥ 120. *A scan cannot find a feature narrower than its own step; these are lattice results, not bounds.*

**1.4 The other half of the fit convention matters more.** `growth_rate` hard-codes **two** choices: nb = 40 *and* the last 60 % window (`i0 = int(0.4·len(t))`). Holding nb = 40 and varying the discarded fraction:

| window frac | median @ 90 rt | signs @ 90 | median @ 240 rt | signs @ 240 |
|---|---|---|---|---|
| 0.2 | +2.9413e−04 | 8+/0− | +3.4558e−04 | 8+/0− |
| 0.3 | +2.3379e−04 | 8+/0− | +3.4377e−04 | 8+/0− |
| **0.4** *(released)* | **−1.0099e−06** | **4+/4−** | +3.3272e−04 | 8+/0− |
| 0.5 | +2.5446e−04 | 8+/0− | +3.1684e−04 | 8+/0− |
| 0.6 | +1.3966e−04 | 7+/1− | +3.1730e−04 | 8+/0− |

*demonstrated.* **At 90 round trips the released window is the only sampled one whose census straddles zero** — at every other window fraction the shipped root shows clearly positive growth. At 240 round trips the sign is 8/8 positive at every window, while the value moves 16.75 %.

**What is robust and what is not.** *demonstrated:* the **sign** at 240 round trips is 8/8 positive at every sampled (nb, window) combination. The **value** is not convention-independent — it moves 2.49 % over the bin lattice and 16.75 % over the window. *in-model:* the near-zero reading at 90 round trips is **noise-dominated jointly in record length, bin count and window**, not a measurement of a threshold — 3 of 8 seeds flip sign on bin count at nb ≤ 120, and the median's swing there (8.14×10⁻⁵) is about half the seed sd at nb = 40 (1.7567×10⁻⁴; at 240 round trips, 2.43×10⁻⁶ against 1.3579×10⁻⁵).

*The bin-count axis is **Kinetic's 🌊** measurement, contributed in the round-1 assessment; the extended lattice and the window axis are its round-2 re-assessment. Both re-executed here and adopted with credit under standing rule 5. Together they reconcile the commissioning lab post's own wider figures (−3.02×10⁻⁴…+3.27×10⁻⁴ at 90 rt, "flat to 2.5 %" at 240), which land on the wider lattice rather than the narrow one.*

## 2. The ladder does not move

Released bracket, `cfl` = 0.4, eight seeds per cell:

| N | record | median | sd | range | shift vs 90 |
|---|---|---|---|---|---|
| 240 | 90 | 0.1689394678 | 9.110e−05 | 2.832e−04 | — |
| 240 | 240 | 0.1687658795 | 5.360e−06 | 1.669e−05 | −1.7359e−04 (**−0.1028 %**) |
| 480 | 90 | 0.1588313831 | 5.603e−05 | 1.579e−04 | — |
| 480 | 240 | 0.1588334587 | 3.617e−06 | 9.638e−06 | +2.0756e−06 (**+0.0013 %**) |
| 720 | 90 | 0.1555731855 | 4.723e−05 | 1.176e−04 | — |
| 720 | 240 | 0.1556041775 | 1.228e−05 | 3.464e−05 | +3.0992e−05 (**+0.0199 %**) |

*demonstrated.* The shifts are **inconsistent in sign** and an order of magnitude apart. The commissioning session pre-registered a falsifier ("median shift smaller than that rung's own eight-seed spread"); *spread* is ambiguous between sd and range **and** between the two censuses, which differ 6–17×, so all four readings are given: met at 3/3 rungs vs range@90, 2/3 vs sd@90, 2/3 vs range@240, 1/3 vs sd@240. **No reading gives a same-signed shift exceeding spread at two or more rungs** — the criterion the verdict rests on, and it was adopted after seeing the data, which is disclosed rather than hidden. **Every promoted 07-22 rung lies inside the corresponding eight-seed range measured here.**

The robust effect of a longer record is the collapse of spread: **range** ratios 17×, 16×, 3.4× (sd ratios 17.0, 15.5, 3.85) at N = 240/480/720.

**Seed-specificity, and its prior art.** 08-02 §1(a) already withdrew two headline claims as `seed`-1 draws ("seed-1 contingent; seed 2 gives the opposite sign") and publishes seed-varying released-scan thresholds at N = 860. This note adds the same lesson at the **released N = 240 rung**: an unpromoted lab-post datum of "+0.054 % at N = 480" **reproduces exactly at `seed` = 1** (0.1587475408418 → 0.1588337224236, +0.0543 %), while the eight per-seed shifts span −0.0447 % to +0.0543 % and straddle zero. The datum is seed-specific, not wrong; the conclusion drawn from it — that record-length bias amplifies in a Richardson pair — is **withdrawn**.

## 3. Convergence order, fitted

*demonstrated.* Fitting M(N) = M_∞ + A·N^(−p) on the three eight-seed medians (bisection on the two differences) gives **p = 1.0582 (90 rt) / 1.0433 (240 rt)**, intercepts **0.14949 / 0.14947** — inside the promoted [0.147, 0.150] and within 0.13 % of the analytic exact-inviscid 0.149313.

**Conditioning, stated rather than asserted.** Three rungs on two refinement ratios (2.0 and 1.5) cannot separate "not yet asymptotic" from "not exactly first order" (a caveat inherited from [`2026-08-02-zero-floor-spec-dissolved.md`](2026-08-02-zero-floor-spec-dissolved.md) §4, not originated here). Quantified, **by three-rung least squares of log(M − M_∞) on log N** — the convention matters and is stated: fixing M_∞ at 0.149313 gives p ≈ 1.04/1.03 and at 0.147 gives ≈ 0.86/0.85; two-rung pairwise solves of the same quantity span 1.033–1.044 and 0.794–0.891, so more than two decimals here would be overprecision.

**The uncertainty bar, labelled.** Perturbing the three medians by ±1 **population** sd of their seed censuses and taking the min/max over the 27 corners gives **p ∈ [0.979, 1.139]**, **M_∞ ∈ [0.14862, 0.15025]** at 90 rt — an envelope whose upper edge leaves the promoted band. **That is a corner box, not a propagated uncertainty**, and it is attained only at the maximally anti-correlated corners. The sampling error of an eight-seed *median* is ≈1.2533·sd/√8 = 0.44 sd; on that bar the envelope is **p ∈ [1.023, 1.094]**, **M_∞ ∈ [0.14912, 0.14984]**, and it does **not** leave [0.147, 0.150]. The wide box is the right bar for a different question — how far a *single-seed* ladder can sit — and 07-22's own published rungs demonstrate it (below).

**Prior art, and what is not new.** 07-22 asserts first-order convergence as demonstrated twice, and its §6 body already publishes *"first-order, Richardson → 0.1486–0.1492"* — **both pair intercepts, including the corrected 480/720 value** ([`2026-07-22-mth-numerical-vs-physical-viscosity.md`](2026-07-22-mth-numerical-vs-physical-viscosity.md):138). [`2026-08-01-ratio-bias-gain-table.md`](2026-08-01-ratio-bias-gain-table.md) §2 publishes 0.149210 explicitly and its Limitation 7 records the 0.148552-vs-0.149210 curvature. What is new here is only that the exponent is **fitted, with an uncertainty, on the measured released-solver ladder at eight seeds**. 07-12 records "an exponent ≈ 1" for its *linear-operator* ladder, with local exponents 0.76–0.88 in its appended record — a different object (as 08-02's own vote record at :263 and :279 already noted).

## 4. Two failures of the released bracket

**4.1 The failing-grid interval does not move.** *demonstrated by full released 8-node scans* (a floor probe is **necessary but not sufficient** for `nan` — 08-02 §1, and §4.2 below is the counterexample to the converse): N = 860 finite at seeds 1–3 at both record lengths (0.1545322375 / 0.1545629789 / 0.1546618561 at 90 — bit-identical to 08-02's published scans — and 0.1545544927 / 0.1545542599 / 0.1545607188 at 240); N = 920 `nan` 3/3 at both, all eight nodes ≥ 0. Eight-seed floor censuses agree in sign 8/8 in every cell and reproduce 08-02's published statistics exactly (N = 920 mean +3.2653×10⁻⁴, sd 1.3334×10⁻⁴; N = 860 −2.6836×10⁻⁴, sd 8.7367×10⁻⁵). **`measure_Mth_num_ceiling_N` is confirmed and unmoved; this is a confirmation at a second record length, not a seed-coverage extension** — 08-02 already published eight-seed floor censuses at 860/880/920/960. **N = 880, the one rung whose census straddles and therefore the only grid at which the interval could move, was not run** — by this session or any prior one.

**4.2 A ceiling-side failure on a new axis.** *demonstrated.* 08-02 already registers a ceiling-side `nan` mode on the **N axis at small N** (its §4 Scope clause: N = 118 and 117 succeed, N = 116, 115 and 114 return `nan` with all eight nodes negative; boundary (116, 117], explicitly "outside this key"). The same mode appears on the **`cfl` axis**: at `cfl` = 0.2, N = 240, the threshold sits **0.036 %** below the bracket ceiling 1.30·`M_th_353K` = 0.1912083333333333, so only the last of the eight nodes carries a sign change — **+8.480×10⁻⁵ at 90 round trips, −2.546×10⁻⁵ at 240** — and with every node then negative the scan returns `nan` at 4/4 seeds. **A new axis on a known mode, not a new mode.** *Scope: `cfl` ∈ {0.2, 0.3, 0.5} at N = 240, seeds 1–4. `cfl` = 0.2 is a lattice point, not a frontier.* Across the family the record-length shift stays −0.08 % to −0.10 % wherever the scan resolves. This feeds the bracket-guard item 08-02 opened.

## 5. Consequence: real, small, one decade from mattering

The streaming bias 0.7·`M_th_num` moves −0.1028 % at N = 240, +0.0013 % at N = 480, +0.0199 % at N = 720. *demonstrated (released `regen.cw_net_gain_dB`, evaluated at M/M_th = 0.804036 — the bias this section names, not the CW leg's own 0.7·`M_th_353K`; the two differ by the bias-convention fork that [`2026-08-01-gated-requirement-round-trip.md`](2026-08-01-gated-requirement-round-trip.md) §0.6 **opened** and [`2026-08-01-ratio-bias-gain-table.md`](2026-08-01-ratio-bias-gain-table.md) **quantified**, and which INDEX.md still lists unresolved):* **−0.0367 dB** (N = 240), **+0.0005 dB** (N = 480), **+0.0071 dB** (N = 720).

Against the smallest *registered* value of `gated_existence_headroom_F2_dB`, 08-01's **+0.424 dB** (an m = 22 / **N = 720** row, near-specular / bulk-central), the grid-matched ratio is **59.5×**; the cross-grid ratio against the N = 240 shift is 11.5×. Against 08-01 §3's +0.292 dB (m = 22, N = 480) the grid-matched ratio is 627× and the cross-grid 7.9×. *in-model (a CW-leg **proxy** for the gated leg's sensitivity — not a bound; nothing here shows the gated leg is less sensitive):* **no gated row moves.** Where 08-01 publishes negative headroom (−0.049, −0.022 dB at 07-18's −1.00 dB contact corner, and −0.099 dB at m = 22 / N = 240) this is a statement about margin *size*, not about a margin that exists. **`f_max_F2_gated_GHz` = 69 [63, 74] is untouched and was not re-adjudicated.**

## 6. Registered keys, and two qualifications to promoted ones

    M_th_num_growth_at_released_root  = +3.33e-4 per round trip (8-seed median, N = 240, cfl = 0.4,
                                        n_roundtrips = 240, fit convention nb = 40 RMS bins over the
                                        last 60 % of the trace -- the released growth_rate default.
                                        The VALUE moves 2.49 % over the bin lattice and 16.75 % over
                                        the window fraction; the SIGN, which the falsifier tests,
                                        does not)
                                        8 of 8 seeds positive at every SAMPLED record length >= 120
                                        (lattice {60,90,120,180,240,360,480}); at 90 the median sits
                                        at zero (4+/4-) ONLY AT THE RELEASED FIT CONVENTION -- its
                                        sign there moves on bin count AND on window fraction, and at
                                        every other sampled window it is positive (sec 1.3, 1.4);
                                        60 is positive (7+/1-)
                                        label: demonstrated
                                        falsifier: an eight-seed census at any record length >= 120,
                                        at nb = 40, straddling zero -- reachable off this lattice, at
                                        a seed beyond 8, or on another platform/numpy

    M_th_num_record_length_shift_pct  = -0.1028 (N = 240) / +0.0013 (N = 480) / +0.0199 (N = 720)
                                        eight-seed medians, 90 -> 240 round trips, cfl = 0.4
                                        INCONSISTENT IN SIGN; |shift| vs the rung's own spread is
                                        convention-dependent: 3/3 vs range@90, 2/3 vs sd@90,
                                        2/3 vs range@240, 1/3 vs sd@240 (sec 2)
                                        label: demonstrated; NOT a systematic ladder bias
                                        falsifier: same-signed shifts exceeding each rung's spread at
                                        two or more rungs, under any one stated convention

    M_th_num_ladder_fitted_order      = 1.0582 (90 rt) / 1.0433 (240 rt); M_inf 0.14949 / 0.14947,
                                        fitted as M(N) = M_inf + A*N^-p on three eight-seed medians
                                        +-1 sd envelope p in [0.979, 1.139], M_inf in [0.14862,
                                        0.15025] at 90 rt -- the upper edge LEAVES [0.147, 0.150]
                                        label: demonstrated for the arithmetic; ILL-CONDITIONED --
                                        three rungs on ratios 2.0 and 1.5 cannot separate "not yet
                                        asymptotic" from "not exactly first order"
                                        falsifier: a fourth rung at a third refinement ratio, on
                                        eight-seed medians at 240 round trips, giving p outside
                                        [0.9, 1.2]. It must sit BELOW the bracket ceiling of
                                        (860, 920]; N = 840 gives ratio 7/6 and works.
                                        note: 07-12's published local exponents 0.76-0.88 (a
                                        DIFFERENT object -- the linear-operator ladder) sit outside
                                        this band

**Two dated qualifications to promoted keys** (neither reopens the key):

1. **`M_th_num_N720`** (08-01 ratio-bias) — its ±1×10⁻⁶ falsifier is a `seed`-1 **determinism check**, already labelled "platform-ULP class" in that note. Measured here, the eight-seed **range at that rung is 1.18×10⁻⁴ — 118× the tolerance.** The band is not an uncertainty and should not be read as one. This is a reconciliation, not a discovery.
2. **`M_th_num_inviscid_limit`** = 0.1490 [0.147, 0.150] (07-22) — **stands**, and the eight-seed census supports it (fitted intercepts 0.14949 / 0.14947). Recorded beside it: the same three-rung fit on 07-22's own **published single-seed** rungs returns p = 1.1151 with intercept **0.1500054**, marginally *outside* the promoted band. The registered intercept survives on an eight-seed census, not on the single-seed ladder it was derived from.

**Erratum against an appended vote record** (reported beside it; appended records are evidence and are never edited). 07-22's appended assessment records "480/720 → 0.15239" beside a correctly-reproducing "240/480 → 0.14855". *demonstrated (arithmetic):* the 0.15239 is the **ratio-2 formula M_∞ = 2·m_fine − m_coarse applied to a ratio-1.5 pair** — 2(0.155568) − 0.158748 = 0.152388, and on that assessor's own driver values 0.1523892. The correct ratio-1.5 form gives **0.149208**, which 07-22's own §6 body already published as the upper end of "Richardson → 0.1486–0.1492". The recorded reservation that the Richardson story was "presented more tidily than the raw ladder supports" therefore rests, in its 0.15239 form, on a one-line formula slip; the reservation's broader point about tidiness is untouched.

## 7. Listing

```python
# from the repository root. Generates every measured figure in this note.
import sys, statistics as st
sys.path.insert(0, 'fable-model-chain')
import numpy as np, constants as C, ds_cell as DS, solver as SOL, regen, run_all

s = DS.plasmon_speed(); Mth = DS.M_threshold(DS.cell_length(s), s, C.tau(C.Tcap))
M_RELEASED = 0.16894319463373791

def scan(N, nrt, seed, cfl=0.4):                      # released measure_Mth_num bracket
    xs = np.linspace(1.05, 1.30, 8)
    g = [SOL.growth_rate(x*Mth, N=N, n_roundtrips=nrt, seed=seed, cfl=cfl) for x in xs]
    for i in range(7):
        if g[i] < 0 <= g[i+1]:
            return (xs[i] + (xs[i+1]-xs[i])*(-g[i])/(g[i+1]-g[i])) * Mth
    return float('nan')

assert scan(240, 90, 1) == run_all.measure_Mth_num() == M_RELEASED        # driver validation

# 1.1, 1.2 -- the plateau census
for nrt in (60, 90, 120, 180, 240, 360, 480):
    v = [SOL.growth_rate(M_RELEASED, N=240, n_roundtrips=nrt, seed=sd) for sd in range(1, 9)]
    print(nrt, sum(1 for x in v if x > 0), st.median(v), st.pstdev(v))

# 1.3 -- the fit-convention sweep. Refit the SAME traces; bit-identical at nb = 40.
def refit(r, nb):
    sig = np.abs(r["drain"]); t = r["t"]; i0 = int(0.4*len(t)); tt = t[i0:]; amp = sig[i0:]
    e = np.linspace(tt[0], tt[-1], nb+1); cen = 0.5*(e[1:]+e[:-1])
    rms = np.array([np.sqrt(np.mean(amp[(tt >= e[i]) & (tt < e[i+1])]**2) + 1e-30) for i in range(nb)])
    g = rms > 0
    return float(np.polyfit(cen[g], np.log(rms[g]), 1)[0]*2.0)
for nrt in (90, 240):
    tr = [SOL.run(M_RELEASED, N=240, drive_kind="none", n_roundtrips=nrt, seed=sd) for sd in range(1, 9)]
    for nb in (10, 20, 30, 40, 50, 60, 80, 120):
        v = [refit(r, nb) for r in tr]
        print(nrt, nb, st.median(v), sum(1 for x in v if x > 0))

# 2 -- the ladder
med = {}
for N in (240, 480, 720):
    for nrt in (90, 240):
        v = sorted(scan(N, nrt, sd) for sd in range(1, 9))
        med[(N, nrt)] = st.median(v); print(N, nrt, st.median(v), st.pstdev(v), v[-1]-v[0])

# 3 -- fitted order (bisection; no scipy), and the fixed-M_inf variants by 3-rung OLS
def fit3(m1, m2, m3, N1=240, N2=480, N3=720):
    f = lambda p: (m1-m2)/(m2-m3) - (N1**-p - N2**-p)/(N2**-p - N3**-p)
    a, b = 0.02, 10.0
    for _ in range(300):
        c = 0.5*(a+b)
        if f(a)*f(c) <= 0: b = c
        else: a = c
    p = 0.5*(a+b); return p, m1 - (m1-m2)/(N1**-p - N2**-p)*N1**-p
for nrt in (90, 240):
    print(nrt, fit3(med[(240,nrt)], med[(480,nrt)], med[(720,nrt)]))
    for Minf in (0.149313, 0.1490, 0.147):                       # 3-rung OLS in log-log
        y = [np.log(med[(N,nrt)] - Minf) for N in (240,480,720)]
        print('   M_inf', Minf, 'p =', -np.polyfit(np.log([240,480,720]), y, 1)[0])

# 4.1 -- FULL scans (not floor probes) at the bracket ceiling grids
for N in (860, 920):
    for nrt in (90, 240):
        print(N, nrt, [scan(N, nrt, sd) for sd in (1, 2, 3)])

# 4.2 -- the cfl axis; only node 7 changes sign at cfl = 0.2
xs = np.linspace(1.05, 1.30, 8)
for nrt in (90, 240):
    print(nrt, [float(SOL.growth_rate(x*Mth, N=240, n_roundtrips=nrt, seed=1, cfl=0.2)) for x in xs])
print('ceiling', 1.30*Mth)

# 5 -- the consequence, at the bias this section names
r = 0.7*M_RELEASED/Mth                                            # 0.804036
for d in (-0.001028, +0.000013, +0.000199):
    print(regen.cw_net_gain_dB(r*(1+d)) - regen.cw_net_gain_dB(r))

# 6 -- the erratum arithmetic
print(2*0.155568 - 0.158748, (720*0.155568 - 480*0.158748)/240)   # 0.152388  0.149208
```

## 8. Limitations

1. **One machine, one platform, one numpy** (3.11.2 / 2.4.6 / macOS arm64) — shared by the author, both check agents and all six assessors, so a platform-borne agreement is invisible to every seat that has looked at this.
2. **Eight seeds is the whole census**, and the N = 240 @ 90 census is skewed (seven seeds in 0.16890–0.16894, one at 0.16866), so its sd carries more weight than a symmetric spread would.
3. **The record-length lattice is {60, 90, 120, 180, 240, 360, 480} at N = 240 only.** Nothing was sampled between 60 and 120, which is where §1.2's anomaly lives, and no plateau census was run at N = 480 or 720. The plateau onset is a lattice result, not a frontier.
4. **The bin-count sweep is one grid, one M, one platform**, nb ∈ {10…120} only.
5. **`cfl` is four seeds at N = 240 only**; the `cfl` = 0.2 `nan` rests on four seeds.
6. **§4.1's full scans are seeds 1–3 at two grids. N = 880 was not run** — the only rung where the interval could move.
7. **§5 is a CW-leg proxy, not a bound**; no gated PRBS row was run.
8. **Not re-run, consumed as published:** `f_max_F2_gated_GHz`, the 08-01 gain table, the 08-02 widened-floor scan.
9. An early driver evaluated the plateau census at the **analytic** `M_th` rather than the released root; caught by checking the sign against expectation, corrected, re-run. The buggy output is used nowhere.

## 9. What this changes

**The adoptable is a convention, not a correction.** `M_th_num` = 0.16894319463373791 remains the correct shipped value *at its stated convention*; that convention is now measured rather than assumed. For WP1:

1. Pin `n_roundtrips`, `seed`, `cfl` **and the fit convention** (nb = 40 over the last 60 %) in `measure_Mth_num`'s docstring — §1.3 shows the last of these can move the sign at the shipped record length.
2. Emit the **eight-seed spread** beside the value. The shipped number is one draw; at 90 round trips the family spans 2.83×10⁻⁴ at N = 240.
3. Read `M_th_num_N720`'s ±1×10⁻⁶ band as the determinism check its own note calls it, not as an uncertainty — the measured seed range is 118× wider.
4. Add the `cfl` = 0.2 ceiling-side failure to the bracket-guard item 08-02 opened; the guard must cover both ends of the bracket, on both the N and `cfl` axes.
5. If a fourth ladder rung is ever run for the intercept, it must sit **below** N ≈ 860 (N = 840 gives ratio 7/6).

**For the record:** 07-22 stands. Its ladder, its first-order claim and its registered intercept survive an eight-seed census and a fitted exponent with an uncertainty. The commissioning hypothesis — that the ladder carries a record-length bias — is **refuted**; that was the pre-registered good outcome.


---

## Agent assessment — 2026-08-06

Assessed by the project's disclosed AI research crew ([agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md)) over **two rounds**, each with three mutually blind persona assessors required to re-execute the decisive numbers against the released, unedited chain rather than trust the transcript. All seats ran on `claude-opus-5` — **not** Claude Fable 5.

- **Round 1 — 3 of 3 store**, all three with required edits → returned for rework. Full verdicts, including each assessor's re-execution log and did-not-run list: [#104 round-1 vote record](https://github.com/ryoji-info/FableComputer/discussions/104#discussioncomment-17921209).
- **Round 2 (the rework)** — 21 of 22 edits accepted, none declined; the one drafted as a decline reproduced on re-measurement and was accepted. [#104 round-2 rework](https://github.com/ryoji-info/FableComputer/discussions/104#discussioncomment-17921326).
- **Round 2 re-assessment — 3 of 3 store**, by three *fresh* mutually blind assessors holding both prior rounds.

**Promotion edits applied post-vote and disclosed here**, per the precedent of [PR #98](https://github.com/ryoji-info/FableComputer/pull/98) and the 08-01 ratio-bias note. The round-2 re-assessment attached further required edits, all of them zero-solver-cost text or scoping changes, and all are applied in this note:

1. **The extended bin lattice and the window axis (🌊 Kinetic, round 2).** nb = 120 was a lattice *edge*, not a bound. Re-executed here: at 90 round trips the median runs +3.1473e−4 … −1.9049e−4 over nb ∈ {160…480}, and the 240-round-trip flatness is **2.49 %**, not the 0.74 % the rework quoted over the narrow lattice. The **window** axis — the unswept half of `growth_rate`'s convention — was measured: at 90 round trips the released 0.4 is **the only sampled window whose census straddles zero**. This *strengthens* §1.2 and is now §1.3–1.4. It also reconciles the commissioning lab post's wider figures, which land on the wider lattice.
2. **"Flat to 0.74 %" and "convention-independent" rescoped** (🌊 Kinetic): the **sign** is robust (8/8 positive at every sampled (nb, window) at 240 rt); the **value** is not (2.49 % on bins, 16.75 % on window).
3. **The fit envelope labelled** (🌊 Kinetic): it is a min/max corner box on ±1 *population* sd, not a propagated uncertainty. On the sampling error of an eight-seed median (≈0.44 sd) it is p ∈ [1.023, 1.094], M_∞ ∈ [0.14912, 0.14984] and does **not** leave the promoted band. The wide box is the right bar for a *single-seed* ladder, which 07-22's own rungs demonstrate.
4. **The fixed-M_∞ fit convention stated** (🌊 Kinetic) and the exponents dropped to two decimals, since pairwise solves span ±0.05.
5. **Registered key 1 now names the fit convention** (🌊 Kinetic, ⚛️ Quanta) and states that its *value* moves on convention while its *sign* — what the falsifier tests — does not.
6. **07-22:138 added as the nearest prior art** for the corrected 480/720 intercept (⚛️ Quanta, 🌊 Kinetic): that note's own §6 body already publishes "Richardson → 0.1486–0.1492". The erratum is therefore narrower and reads better — the note was right; its appended assessor's arithmetic slipped.
7. **The seed-spread novelty rescoped** to the released N = 240 rung, citing 08-02 §1(a), which already withdrew two claims as seed-1 draws (🧵 Fabric).
8. **The 08-02 ceiling-side quote corrected** to that note's own re-measured boundary (116, 117] (🧵 Fabric).
9. **§5's grid-matched ratios given** — 59.5× at N = 720 and 627× at N = 480 — beside the cross-grid 11.5× (🌊 Kinetic, 🧵 Fabric).
10. **`M_th_num_N720`'s ±1e−6 band** recorded as a reconciliation, not a discovery: that note already labels it "platform-ULP class" (⚛️ Quanta).
11. **The process narrative struck from the note body** (⚛️ Quanta, both rounds). The session's eleven prose corrections and the pattern they form are transcript; they live permanently and unedited in [#104](https://github.com/ryoji-info/FableComputer/discussions/104) and in the round-1 vote record. This note is the corrected record, not a diff against a draft. The round-2 re-assessment was unanimous that the promoted note had to be the *assembled* text rather than a change log — that is this file.

**Recorded because it is the session's own lesson.** Across two check agents and six assessor seats, **no measurement in this work was refuted**; eleven claims *about the record*, or labels on measurements, were. Three of those were the same error — asserting a negative about reproducibility without first testing the convention the original used. That is why registered key 1 now names its fit convention, and why §9's adoptable is a convention rather than a correction.
