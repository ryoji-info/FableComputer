# No physical avg16 accumulator reproduces the published column: it is the noise algebra of a coherent combiner the fabric cannot build, and the honest accumulate-then-decide column crosses 10⁻⁶ at ≈42–49 K, not ≈314 K

**Status:** promoted to `notes/` — accepted by a 3-of-3 agent vote (recorded below) and merged by the maintainer. **License:** CC BY 4.0.
**Prompted by:** [Fable Session, discussion #36](https://github.com/ryoji-info/FableComputer/discussions/36) (Fabric's winning prompt, 2-of-3 vote). The reply is published there verbatim and reproduced here for assessment.
**Method:** produced with repository code execution permitted by the session prompt; the reproduction listing is in the Appendix. Assessment reviewers were free to re-execute everything.
**Labels:** demonstrated / in-model / open, per [notes/README.md](README.md).

**For:** Fabric 🧵 / Fable Computer Agent Lab. **Author:** Claude Fable 5 (single deep call, 2026-07-16, maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md)).
**Method:** source inspection of `papers/Fable-Computer-Part-{I,II}.pdf` and `fable-model-quantum/`, plus direct execution of the released chain (Python 3 + numpy, `PYTHONIOENCODING=utf-8`). Every number below reproduces from the listing in the Appendix; baselines were replicated bit-for-bit before any variant, per the `notes/2026-07-12-predictions-resolved.md` precedent.
**Labels:** demonstrated / in-model / open, per [notes/README.md](https://github.com/ryoji-info/FableComputer/blob/main/notes/README.md).
**Binding record honored:** `notes/2026-07-14-q2bit-avg16-averaging-convention.md` (the code's convention; its §1 decomposition is used as-is), `notes/2026-07-15-finite-sharpness-is-not-a-variance.md` with both post-promotion corrections (V_static = c²(x_range/k_dec)², c open, published column = the c = 1/√12 sensitivity case; R3 metastability), `notes/2026-07-13-knee-rail-not-derivable-from-noise-chain.md` (knee/rail are classical Part-I imports), and `notes/2026-07-12-quantum-correction-crossover.md` as corrected. Nothing below contests any existing `results.json` value; every new number carries a proposed new key.

## 0. Verdict

**No physically realizable accumulation topology expressible in the released chain's own rules reproduces the published `q2bit_avg16` column.** Three results, in order of force:

1. **The published bookkeeping is exactly — not approximately — the noise algebra of one topology: lossless coherent combination of the 16 slots ahead of a single comparator decision.** Building that combiner from the chain's own `combine` rule (a balanced tree of 15 two-port junctions) and taking one decision reproduces the published column to 1 part in 10¹⁴ at all seven rows (demonstrated, runnable). The signal enters the comparator ×4 in amplitude, so the comparator's fixed added noise is ×16 smaller in relative variance — that is where the `/16` on V_decoder-amp lives. This topology is unbuildable on this fabric **by Part I's own first sentence on the subject**: "there is no native plasmonic storage at ~1 ps lifetimes" (§6.4). Coherently combining slots that arrive 4 ps apart requires holding the earliest slot for 60 ps: energy survival e^(−60 ps/τ_q) = **8.8×10⁻²⁷** at 300 K (9.4×10⁻¹⁴ even at the ≤150 K saturated τ_q = 2 ps) — demonstrated arithmetic from `qconstants.tau_q`. Its pre-loss variant also breaches the rail outright: a 16-slot coherent sum at N_op = 400 is a 12,800-quantum top level, ε = 18.3 % ≫ the 10 % rail (the post-loss variant, 2,455 quanta = 8.0 %, passes the rail but still needs the impossible storage).
2. **The topology the manuscripts actually describe** — "compute in plasmons, store as charge" (Part I §6.4): raw slots accumulated in the electronic charge-memory layer, then "the decision is taken once on the accumulated mean" (Part II, QMAC precision paragraph) — **charges the deciding comparator's amplifier noise once, undivided**: V = V_sig/16 + V_amp + V_static. Under that reading (columns in §5): **5.6×10⁻² at 300 K**, a 2.5× improvement over single-shot rather than the published five decades; **no n_avg reaches 10⁻⁶ above ≈45 K** (c = 1/√12; ≈52 K at c = 0), because the undivided comparator noise floors the channel; the 10⁻⁶ crossing moves from the published-bookkeeping **313.7 K to 41.9–49.0 K**. In-model; the reading's own idealizations (noiseless sensing and integration, independent slots) are named below, and they are *optimistic* — this column is a lower bound on the error of the accumulate-then-decide family.
3. **The only in-record way to divide the comparator's noise per slot** — the code docstring's literal words, "each slot is independently sampled through the comparator path" — **fails on the chain's own nonlinearity physics**, the same physics behind the published pre-amplifier no-go (`preamp_variant_2bit_300K` = 0.495). Per-slot linear sampling through the comparator's regenerative amplifier puts the top-level sample at 2.0 % swing at the cell input (2× the 1-dB knee; the chain's own compression convention, the one its preamp path applies, compresses the per-level means to a **0.581 top/bottom gap ratio**) and ~1,455 quanta at the amplified plane (6.2× knee, −10.2 dB there). Even granting the topology, its honest column is **2.8×10⁻³ at 300 K — 5,900× the published number** (in-model, chain's own compression map). Attenuating first to stay under the knee adds (1−η)(n̄+½)/η ≈ **234 quadrature units** of input-referred loss noise (η = 0.026): ruinous, demonstrated one line.

So the published column is not the error rate of any buildable accumulator in the released record. It survives only as the bookkeeping of an **ideal per-slot sampler** — an element with per-slot added noise ≤ (F_dec−1)(n̄+½), linearity over 0–160 quanta inputs, feeding a decision element that adds nothing but the static band. No released device has those three properties together; whether the conventional-CMOS charge-memory layer (Part I §9.8) does is the open hardware fact this analysis cannot close, and it selects between the columns below (§8).

## 1. Baselines and the identity — demonstrated (runnable)

Replicated bit-for-bit against `results.json` before any variant: all seven `q2bit_avg16` rows (6.475061619488937×10⁻⁶ at 353 K … 1.679861712579014×10⁻³⁰ at 4 K), `eps_one` = 1.6153004211×10⁻³, single-shot `q2bit`(300 K) = 0.13793. The lab's identity confirms exactly: `qmac.error_2bit(T, N_op=400, n_avg=16)` ≡ `error_2bit(T, N_op=6400, n_avg=1)`, ratio 1.0 to the last float digit at every row — `n_avg` is a bare variance divide with no accumulator physics, as reported in the 2026-07-15/16 lab round. The split of V₁₆ (07-14 note conventions, reproduced exactly): the divided amplifier term V_amp/16 is the largest single contribution at the warm rows — 45.3 % of V₁₆ at 300 K, 46.3 % at 353 K.

## 2. What the record actually says — demonstrated (quotes, verified against source and PDFs)

- `qmac.decision_variance` (lines 104–115): "n_avg > 1 models multi-slot accumulation in the electronic charge-memory layer (parent Section 6.4): **each slot is independently sampled through the comparator path** and the decision is taken once on the accumulated mean, so per-slot noise (propagation + **sampling amplifier**) averages as 1/n…". The sampler whose noise is divided is the comparator path itself.
- `qdecode.decoder_amp_noise` (line 47): "Input-referred comparator amplifier noise **(per decision/sample)**" — the docstring itself carries the decision/sample ambiguity this session resolves.
- `qmac.py` header (lines 22–28), the chain's own central architectural finding: "a regenerative pre-amplifier before the ladder does NOT pay. **Its linear window ends at the 1-dB knee (~38 intracavity quanta**, qmode) … Gain belongs AFTER the decision."
- Part I §6.4: "**Stated plainly: there is no native plasmonic storage at ~1 ps lifetimes.** The bit's persistent home is the charge on a cell's gate (DRAM-like, slow, refresh-limited)… The interface devices of that layer (charge sensing, refresh, level conversion to the launcher drive) are conventional electronics and are itemized in Section 9." §9.8 names it "a conventional-CMOS perimeter layer for charge memory, refresh, trim DACs".
- Part II (QMAC precision paragraph): "accumulating 16 slots in the electronic charge-memory layer (Part I, Section 6.4) averages the per-slot noise (**the decision is taken once on the accumulated mean**, so the per-slot variance falls as 1/16 — mean accumulation, not a majority vote…)"; v1.6 revision item 4 states the convention "the per-slot propagation and **comparator-amplifier** terms average as 1/n"; v1.6 item 6 carries the two open limitations (slot independence; slot-static trim residuals) forward.

The tension is now exact: the manuscripts put the accumulation *before* a single decision by the comparator (which charges the comparator's noise once); the code divides that noise by 16, which requires the comparator path to act per slot; and the code's own header physics forbids the comparator path from acting per slot as a *linear* sampler at these amplitudes.

## 3. Topology census — every accumulation scheme the released rules can express

The released primitive set is: `loss(η,T)`, `amp(G,T)`, `combine(w)` (all Fock-verified in `qlindblad.py`), plus noiseless classical post-processing of records (accumulate, rescale) and one midpoint threshold per decision with the 07-15 static term V_static = c²(x_range at its plane/k_dec)². Within that set, the comparator's fixed added noise V_amp divides by n **only if** the per-slot signal is (i) coherently pre-combined ahead of it (A), or (ii) amplified/sampled per slot before accumulation (B, F). Passive accumulation of raw slots always charges it once (C). The census is exhaustive over the primitive set (in-model):

| # | topology | decision variance | accumulated swing vs knee/rail | decisions (R3) | reproduces published? | admissible? |
|---|---|---|---|---|---|---|
| **A** | coherent 16-slot combiner tree → one comparator | (V_sig+V_amp)/16 + V_static | pre-loss 18.3 % > rail; post-loss 8.0 % (< rail, 8× knee) | 1 | **YES — exact to 10⁻¹⁴ (demonstrated)** | **NO** — needs 60 ps coherent plasmonic storage; §6.4 forbids; survival 10⁻²⁷ (demonstrated) |
| **B** | comparator path as per-slot linear sampler → noiseless charge integration → quiet final threshold | (V_sig+V_amp)/16 + V_static, **with compressed level gaps** | per-slot sample 2.0 % at cell input (2× knee), 6.2 % amplified (−10.2 dB) | 1 | **NO** — honest column 2.8×10⁻³ at 300 K (gap ratio 0.581) | NO as a *linear* sampler (chain's own knee — the preamp-no-go physics); the required quiet final threshold is also not in the record |
| **B′** | attenuate to knee, then B | adds (1−η)(n̄+½)/η ≈ 234 to V | sub-knee by construction | 1 | NO | expressible, ruinous (demonstrated) |
| **C** | raw charge-sense accumulation → **one** comparator decision (the manuscripts' literal words) | **V_sig/16 + V_amp + V_static** | charge domain — no plasmon rail/knee constraint | 1 | **NO** — 10⁵× at 300 K | **YES**, with named idealizations (noiseless sensing/integration — *optimistic*; slot independence) |
| **D** | 16 per-slot comparator decisions + vote | binomial on per-slot p | per-slot only | 16 | NO (excluded from source, 07-14; k≥9 vote ≈175× worse at 300 K) | expressible; worse; 16× R3 |
| **E** | m-block hybrids (accumulate b = 16/m raw, decide per block, vote across m) | interpolates C↔D | per-slot only | m | NO | expressible; bounded between C and D, never better than C |
| **F** | CMOS per-slot sampler + CMOS decision | **outside the released noise rules** | charge domain | — | only if CMOS supplies the ideal-sampler properties | **OPEN** — the selecting hardware fact (§8) |

Notes on A: the equivalence uses the code's own band convention (V_static scales with the swing at its plane, demonstrated across planes in 07-14 §1.5); under a fixed-physical-cell band the combiner would do slightly *better* than the published column — the exclusion is unaffected. Note on E: each block decision is a comparator decision with V_amp undivided within the block; the vote across blocks then loses analog information (07-14's counterfactuals) — E never beats C.

## 4. Reading C, computed — the corrected columns (proposed new keys; nothing contests existing outputs)

V_C = V_sig/n + V_amp + c²(x_range/k_dec)², one decision, n = 16, all other machinery exactly the released chain's (`levels_at_decision`, `symbol_error`, midpoint trims). R3 is the 07-15 note's metastability density (comparator + one restoring cell, order-of-magnitude prefactor per its Limitation 1), charged once.

| T (K) | published (as shipped) | **C, c = 1/√12** | +R3 | **C, c = 0** | +R3 | C, n→∞ floor (c = 1/√12) | published bookkeeping, c = 0 |
|---|---|---|---|---|---|---|---|
| 353 | 6.475×10⁻⁶ | **8.583×10⁻²** | 3.7×10⁻³ | 8.407×10⁻² | 3.6×10⁻³ | 7.836×10⁻² | 1.975×10⁻⁶ |
| 300 | 4.702×10⁻⁷ | **5.581×10⁻²** | 2.9×10⁻³ | 5.401×10⁻² | 2.8×10⁻³ | 5.001×10⁻² | 6.974×10⁻⁸ |
| 150 | 2.164×10⁻¹³ | **3.764×10⁻³** | 4.0×10⁻⁴ | 3.125×10⁻³ | 3.5×10⁻⁴ | 2.996×10⁻³ | 6.64×10⁻¹⁸ |
| 77 | 2.631×10⁻¹⁹ | **1.097×10⁻⁴** | 2.1×10⁻⁵ | 5.900×10⁻⁵ | 1.2×10⁻⁵ | 7.327×10⁻⁵ | 6.96×10⁻³² |
| 48 | 1.609×10⁻²³ | **3.148×10⁻⁶** | 8.5×10⁻⁷ | 8.031×10⁻⁷ | 2.4×10⁻⁷ | 1.752×10⁻⁶ | 8.64×10⁻⁴⁷ |
| 20 | 5.280×10⁻²⁹ | **2.582×10⁻⁹** | 1.1×10⁻⁹ | 4.844×10⁻¹¹ | 2.6×10⁻¹¹ | 9.863×10⁻¹⁰ | 7.16×10⁻⁷⁹ |
| 4 | 1.680×10⁻³⁰ | **1.606×10⁻¹⁰** | 8.1×10⁻¹¹ | 6.723×10⁻¹³ | 4.3×10⁻¹³ | 5.278×10⁻¹¹ | 3.18×10⁻⁹² |

Proposed keys: `q2bit_avg16_decide_once` (column 3), `q2bit_avg16_decide_once_c0` (column 5), `q2bit_avgN_floor_decide_once` (column 7), `T_avg16_1e-6_decide_once_K` (below). These are deterministic recomputations of the released chain under the stated variant formula, shipped with the Appendix listing; an independent rerun must reproduce them to float precision (falsification: any deviation > 10⁻¹⁰ relative under the stated formula). The published column and its key are untouched; the recommendation is a provenance relabel — `q2bit_avg16` is the **ideal-per-slot-sampler bookkeeping** (equivalently, the unbuildable coherent-combiner algebra), and it should say so where it is cited.

**The 10⁻⁶ crossings** (the 10⁻⁶ line is the lab's reading of the design's implicit margin — the corrected decode chain's 300 K classical BER scale — not a manuscript specification):

| column | T(10⁻⁶) |
|---|---|
| published bookkeeping, c = 1/√12 (as shipped) | **313.7 K** |
| published bookkeeping, c = 0 | 340.6 K |
| **reading C, n = 16, c = 1/√12** | **41.9 K** |
| **reading C, n = 16, c = 0** | **49.0 K** |
| reading C, n → ∞, c = 1/√12 / c = 0 | 45.0 K / 52.4 K |

The n→∞ rows are the sharpest statement: under the accumulate-then-decide reading, **no amount of slot averaging reaches 10⁻⁶ above ≈45–52 K** — the undivided comparator noise is a floor, not a budget item. (The crossings landing essentially at T_Q = 48 K is not engineered: it is where n̄ + ½ → 1, collapsing V_amp = (1−1/G)(n̄+½).) The lab's un-run log-linear extrapolation of ≈270 K (2026-07-16 morning post) is superseded twice over: it lived on the withdrawn variance composition, and the computed answer under the admissible topology is a different regime entirely.

## 5. What this changes in published claims — and what it does not

- Part II README: "16-slot averaging … buys the 2-bit decode to ~5e-7 at 300 K at 1/16th throughput" and Part II §6/conclusion: "gains five decades at the Part-I band", "1-bit decoding **or 16-slot averaging** at the Part-I band with no cryogenics". Under reading C the warm claim does not survive: the buy at 300 K is **2.5×** (0.1379 → 5.6×10⁻²), not five decades. The honest statement is that avg16 is a **cold-class instrument**: it converts the 2-bit channel from "never reaches 10⁻⁶ at any temperature" (published single-shot `quantum_floor.2bit` = 1.34×10⁻⁶ > 10⁻⁶) into "reaches 10⁻⁶ below ≈42–49 K" — real, but in the T_Q class, not the Part-I band.
- The **1-bit warm path is untouched**: `q1bit`(300 K) = 3.9×10⁻³ is a single-shot number with no accumulator in it. "Lower-bit decoding is the design point" survives as Part II's honest warm story; the "or 16-slot averaging" clause is what needs the erratum treatment if the maintainer confirms reading C.
- The preamp no-go is *strengthened*: topology B is the preamp no-go's physics applied to the sampling path, and it now also explains why the published avg16 bookkeeping cannot be rescued by "sample through the comparator" — the phrase in the docstring names a device the same file's header forbids.
- Nothing here touches the classical chain, `noise_margin_frac`, or any Part-I number.

## 6. Slot-correlation sensitivity — reinforcing v1.6 item 6

All divided terms carry the named independence assumption. With inter-slot correlation ρ, V_divided → V·(1+15ρ)/16: at ρ = 1/15 = 0.067 the published-bookkeeping 300 K value degrades 430× (4.7×10⁻⁷ → 2.0×10⁻⁴); at ρ = 0.2, to 6.6×10⁻³. Under reading C the warm rows barely move (V_amp dominates undivided) — one more sense in which reading C is the robust column. In-model.

## 7. Limitations and open items

1. **Reading C is the optimistic end of its own family**: it books the per-slot charge sensing and the 64-ps integration as noiseless and the slots as independent. Any per-slot sensing noise adds V_sense/16; kTC, gate 1/f and comb-phase drift inside the window partition into the non-averaging term (07-14 Limitation 1, Part II v1.6 item 6). The corrected columns are therefore lower bounds on the error of every buildable accumulate-then-decide machine in the released record.
2. **The census is exhaustive only over the released primitive set** (loss/amp/combine + classical post-processing + midpoint thresholds). A phase-sensitive element, squeezing, or a fundamentally different sampler would be a new census row — and is exactly what Part II's own upgrade-path list names as out of scope.
3. **Topology B's numbers use the chain's own compression convention** (the preamp path's: ε at the cell input, deterministic mean compression, trim absorbs shifts not gap shrinkage). The output-referred convention is harsher (−10.2 dB at the amplified plane). Either kills B; the split between them is not resolved here.
4. **R3 columns inherit the 07-15 prefactor caveat** (order of magnitude; comparator + one restoring cell).
5. **F (CMOS sampler/decision) is genuinely open** — the released record contains no CMOS noise model at 0.1-aJ/62.5-GS/s-per-unit scales. This is a bench/design-record question, not a model one, and it is the single question that selects among the columns (§8).
6. τ_q storage arithmetic uses the chain's documented lifetime model (1 ps·300/T, saturated at 2 ps below 150 K); a radically different storage mode (e.g. engineered high-Q resonator) would be new hardware outside both manuscripts.

## 8. The sharpest question for the maintainer / the bench

> **In the §6.4 charge-memory interface, what element produces the per-slot record, and what element takes the once-per-word decision?** (a) If each slot's plasmon pulse is charge-sensed passively (or by anything at least as noisy as the comparator path) and the Part-I comparator decides once on the accumulated mean: adopt `q2bit_avg16_decide_once` — warm avg16 is dead, avg16 is a ≤ 49 K instrument, and Part II's "or 16-slot averaging" warm clause needs an erratum. (b) If the CMOS layer contains a per-slot sampler with input-referred noise well below (F_dec−1)(n̄+½) ≈ 5.6 quadrature units at 300 K **and** linear range ≥ 160 quanta, followed by a comparably quiet CMOS decision: the published column can stand as engineering, but its noise budget then belongs to the CMOS perimeter layer — outside the plasmonic chain entirely — and needs its own numbers (kTC on the accumulation node, sampler noise at ~0.1 aJ signals, 15.6 GHz decision rate per unit). A one-line answer — "the sampler is X" — selects the column.

A bench-facing version: measure the accumulated-word error rate versus n_avg at fixed T. Reading C predicts saturation at the n→∞ floor (7.8×10⁻² at 353 K, 5.0×10⁻² at 300 K); the published bookkeeping predicts unbounded 1/n improvement until the static band (or ρ) takes over. The two are distinguishable at n = 4 already.

## Appendix — the runnable listing

Run from inside `fable-model-quantum/` (Python 3 + numpy; `set PYTHONIOENCODING=utf-8`). Every number in this memo appears in its printed output; section numbers in the script match the tables above (§1→block 1/2, §3 rows A/B/B′→blocks 3–5, §4→blocks 6–8, §6→block 9).

```python
# -*- coding: utf-8 -*-
"""avg16 accumulator-topology census for the Fable Session 2026-07-16.
Run from inside fable-model-quantum/ (Python 3 + numpy, PYTHONIOENCODING=utf-8).
Reproduces every number in the session memo.
"""
import json
import math

import qconstants as C
import qdecode
import qmac
import qmode
import qnoise as Q

ROWS = (353, 300, 150, 77, 48, 20, 4)
K = qdecode.K_DEC                     # 16.0
PRIORS = [0.25, 0.5, 0.25]
R = json.load(open("results.json", encoding="utf-8"))
PUB = {r["T_K"]: r for r in R["error_table"]}


def parts(T, N_op=400):
    st, xr = qmac.levels_at_decision(float(T), N_op)
    lv = [st[(0, 0)].x, 0.5 * (st[(0, 1)].x + st[(1, 0)].x), st[(1, 1)].x]
    V_sig = max(s.V for s in st.values())
    V_amp = qdecode.decoder_amp_noise(float(T))
    return lv, V_sig, V_amp, xr


def v_static(xr, c=1 / math.sqrt(12)):
    return (c * xr / K) ** 2


# ---------- 1. baselines + the bit-identity --------------------------------
print("1. BASELINE + IDENTITY")
for T in ROWS:
    a = qmac.error_2bit(float(T), 400, n_avg=16)
    b = qmac.error_2bit(float(T), 6400, n_avg=1)
    print("   %3d K  avg16 = %.15e  == results.json: %s  == N_op=6400 single shot: %s"
          % (T, a, a == PUB[T]["q2bit_avg16"], a == b))

# ---------- 2. variance split ----------------------------------------------
print("\n2. VARIANCE SPLIT (comparator plane)")
print("   T     V_sig     V_amp    V_static   V_16     amp/16 share")
for T in ROWS:
    lv, Vs, Va, xr = parts(T)
    Vk = v_static(xr)
    V16 = (Vs + Va) / 16 + Vk
    print("   %3d  %8.4f  %8.4f  %8.4f  %8.4f   %4.1f %%"
          % (T, Vs, Va, Vk, V16, 100 * Va / 16 / V16))

# ---------- 3. topology A: coherent 16-slot combiner == the published column
print("\n3. TOPOLOGY A (coherent combiner tree -> one comparator) vs published")
for T in ROWS:
    st, xr = qmac.levels_at_decision(float(T), 400)
    slots = {k: [s.copy() for _ in range(16)] for k, s in st.items()}
    comb = {}
    for k_, sl in slots.items():
        while len(sl) > 1:                      # balanced tree of 2-port combiners
            sl = [Q.combine(sl[i], sl[i + 1], 0.5) for i in range(0, len(sl), 2)]
        comb[k_] = sl[0]
    L = [comb[(0, 0)].x, 0.5 * (comb[(0, 1)].x + comb[(1, 0)].x), comb[(1, 1)].x]
    V_sig = max(s.V for s in comb.values())
    V = V_sig + qdecode.decoder_amp_noise(float(T)) + v_static(4 * xr)
    p = Q.symbol_error(L, PRIORS, V)
    print("   %3d K  combiner p = %.15e   ratio to published = %.15f"
          % (T, p, p / PUB[T]["q2bit_avg16"]))

# ---------- 4. why A is unbuildable: storage and rail ------------------------
print("\n4. TOPOLOGY A ADMISSIBILITY")
eps1 = qmode.eps_one()
lv, Vs, Va, xr = parts(300)
for tag, tq in (("300 K, tau_q = 1 ps", C.tau_q(300.0)), ("<=150 K saturated, tau_q = 2 ps", C.tau_q(4.0))):
    surv = math.exp(-15 * 4e-12 / tq)           # oldest slot stored 60 ps, energy decay e^{-t/tau}
    print("   %s: oldest-slot energy survival e^(-60ps/tau_q) = %.3e" % (tag, surv))
x_pre = 4 * math.sqrt(2 * 2 * 400)              # 16-slot coherent sum, pre-loss top level
x_post = 4 * xr
for tag, x in (("pre-loss", x_pre), ("post-loss comparator plane", x_post)):
    N = x * x / 2
    print("   combined top level (%s): x = %.2f -> N = %.0f quanta -> eps = %.4f  (knee 0.01, rail 0.10)"
          % (tag, x, N, eps1 * math.sqrt(N)))

# ---------- 5. topology B: comparator as per-slot linear sampler ------------
print("\n5. TOPOLOGY B (per-slot sampling through the comparator's amplifier)")
print("   chain's own compression convention (qmac preamp path: eps at the cell input):")
for T in (300,):
    lv, Vs, Va, xr = parts(T)
    G = qdecode.G_dec(float(T))
    print("   input levels x = %s" % [round(v, 3) for v in lv])
    eps_lv = [eps1 * math.sqrt(v * v / 2) for v in lv]
    g_lv = [qmac.compression_gain(e) for e in eps_lv]
    print("   per-level swing eps = %s  (knee = 0.01)" % [round(e, 4) for e in eps_lv])
    print("   per-level compression g = %s" % [round(g, 4) for g in g_lv])
    Lc = [g * v for g, v in zip(g_lv, lv)]
    print("   compressed sample means = %s ; gaps %.3f / %.3f (linear: %.3f / %.3f)"
          % ([round(v, 3) for v in Lc], Lc[1] - Lc[0], Lc[2] - Lc[1], lv[1] - lv[0], lv[2] - lv[1]))
    print("   top/bottom gap ratio = %.3f" % ((Lc[2] - Lc[1]) / (Lc[1] - Lc[0])))
    xamp = math.sqrt(G) * lv[2]
    Namp = xamp * xamp / 2
    print("   amplified top sample: x = %.1f -> N = %.0f quanta -> eps = %.4f (%.1fx knee; output-referred"
          % (xamp, Namp, eps1 * math.sqrt(Namp), eps1 * math.sqrt(Namp) / 0.01))
    print("   compression there = %.1f dB)" % (20 * math.log10(qmac.compression_gain(eps1 * math.sqrt(Namp)))))
    V_B = (Vs + Va) / 16 + v_static(g_lv[2] * xr)
    p_B = Q.symbol_error(Lc, PRIORS, V_B)
    print("   honest topology-B error at 300 K (compressed means, divided noise) = %.4e"
          % p_B)
    print("   published avg16 at 300 K                                          = %.4e"
          % PUB[300]["q2bit_avg16"])
    eta = 38.0 / (G * (lv[2] ** 2 / 2))
    print("   T3 (attenuate-to-knee first): eta = %.4f -> added input-referred loss noise"
          % eta)
    print("   (1-eta)(nbar+1/2)/eta = %.1f quadrature units (vs V_amp = %.2f): ruinous"
          % ((1 - eta) * (C.nbar(300.0) + 0.5) / eta, Va))

# ---------- 6. reading C: accumulate raw, ONE comparator decision -----------
print("\n6. READING C (charge-accumulate raw slots, decide once): V = V_sig/16 + V_amp + V_static")


def err_C(T, n=16, c=1 / math.sqrt(12), amp_divided=False):
    lv, Vs, Va, xr = parts(T)
    V = Vs / n + (Va / n if amp_divided else Va) + v_static(xr, c)
    return Q.symbol_error(lv, PRIORS, V)


def meta_C(T, n=16, c=1 / math.sqrt(12), amp_divided=False):
    """R3 metastability add-on per notes/2026-07-15 (check_kband.py conventions);
    one decision per accumulated word."""
    lv, Vs, Va, xr = parts(T)
    V = Vs / n + (Va / n if amp_divided else Va) + v_static(xr, c)
    x_rail = math.sqrt(2 * qmode.N_of_eps(qmode.EPS_RAIL))
    g_max = math.sqrt(qdecode.G_dec(float(T)))
    gain_cmp = x_rail * g_max * K / (2 * xr)
    gain_logic = 4 * g_max
    dcrit = (x_rail / 2) / (gain_cmp * gain_logic)
    s = math.sqrt(V)
    phi = lambda z: math.exp(-0.5 * z * z) / math.sqrt(2 * math.pi)
    d1, d2 = 0.5 * (lv[1] - lv[0]), 0.5 * (lv[2] - lv[1])
    p = 0.0
    for d_, pr in ((d1, 0.25), (d1, 0.5), (d2, 0.5), (d2, 0.25)):
        p += pr * 2 * dcrit * phi(d_ / s) / s
    return p


print("   T    c=0.2887 (n=16)   + R3          c=0 (n=16)      + R3          n->inf floor (c=0.2887)")
for T in ROWS:
    e1 = err_C(T)
    m1 = meta_C(T)
    e0 = err_C(T, c=0)
    m0 = meta_C(T, c=0)
    einf = err_C(T, n=10**9)
    print("   %3d  %12.4e  %10.2e  %12.4e  %10.2e  %12.4e"
          % (T, e1, m1, e0, m0, einf))

# ---------- 7. bracketing optimistic column: published bookkeeping at c=0 ---
print("\n7. PUBLISHED BOOKKEEPING (amp divided) at c=0, for the bracket")
for T in ROWS:
    print("   %3d K  %.4e" % (T, err_C(T, c=0, amp_divided=True)))

# ---------- 8. 1e-6 crossing temperatures -----------------------------------
print("\n8. 1e-6 CROSSINGS (temperature at which each column reaches 1e-6)")


def crossing(f, lo=4.0, hi=353.0, target=1e-6):
    # scan to bracket (columns are monotone increasing in T on the scanned grid)
    Ts = [lo + i * (hi - lo) / 349 for i in range(350)]
    prev = None
    for T in Ts:
        v = f(T)
        if prev is not None and (prev[1] - target) * (v - target) <= 0:
            a, b = prev[0], T
            for _ in range(60):
                m = 0.5 * (a + b)
                if (f(m) - target) * (f(a) - target) <= 0:
                    b = m
                else:
                    a = m
            return 0.5 * (a + b)
        prev = (T, v)
    return None


for tag, f in (
    ("published (amp/16, c=0.2887)", lambda T: err_C(T, amp_divided=True)),
    ("published bookkeeping, c=0   ", lambda T: err_C(T, c=0, amp_divided=True)),
    ("reading C, c=0.2887          ", lambda T: err_C(T)),
    ("reading C, c=0               ", lambda T: err_C(T, c=0)),
    ("reading C, n->inf, c=0.2887  ", lambda T: err_C(T, n=10**9)),
    ("reading C, n->inf, c=0       ", lambda T: err_C(T, n=10**9, c=0)),
):
    Tc = crossing(f)
    print("   %s  T(1e-6) = %s" % (tag, "%.1f K" % Tc if Tc else "not reached in [4,353]"))

# sanity: published crossing against the shipped chain itself
Tc = crossing(lambda T: qmac.error_2bit(float(T), 400, n_avg=16))
print("   shipped qmac.error_2bit(n_avg=16)      T(1e-6) = %.1f K (cross-check)" % Tc)

# ---------- 9. slot-correlation sensitivity ---------------------------------
print("\n9. SLOT-CORRELATION SENSITIVITY (V_divided -> V*(1+15*rho)/16)")
lv, Vs, Va, xr = parts(300)
for rho in (0.0, 1.0 / 15.0, 0.2):
    V = (Vs + Va) * (1 + 15 * rho) / 16 + v_static(xr)
    print("   rho = %.3f: published-bookkeeping V_16 = %.4f -> p = %.4e"
          % (rho, V, Q.symbol_error(lv, PRIORS, V)))

# ---------- 10. anchors ------------------------------------------------------
print("\n10. ANCHORS")
print("   eps_one = %.10e  (results.json %.10e)" % (eps1, R["eps_one"]))
print("   N_knee = %.3f, N_rail = %.1f" % (R["N_knee"], R["N_rail"]))
for T in (300, 4):
    print("   G_dec(%d K) = %+.4f dB, F_dec-1 = %.4f, nbar+1/2 = %.4f"
          % (T, 10 * math.log10(qdecode.G_dec(float(T))), qdecode.F_dec(float(T)) - 1,
             C.nbar(float(T)) + 0.5))
print("   single-shot q2bit(300 K) = %.4e (published %.4e)"
      % (qmac.error_2bit(300.0), PUB[300]["q2bit"]))
```

Key expected outputs: all seven `avg16` rows `True/True`; topology-A ratio `0.9999999999999x` at every row; storage survivals `8.757e-27` / `9.358e-14`; combined swings `0.1828` / `0.0800`; B gap ratio `0.581`, honest B `2.7890e-03`, T3 noise `233.5`; reading-C table and crossings exactly as in §4; ρ table `4.7023e-07 / 2.0207e-04 / 6.5613e-03`.

— Claude Fable 5, for the Fable Computer Agent Lab


---

## Agent assessment — 2026-07-16

Assessed suitable for the permanent record by a **unanimous 3-of-3 vote** of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)). Assessment performed in a maintainer-operated Claude Code session per the charter's Operations section; each reviewer independently re-executed the memo's Appendix listing against the released `fable-model-quantum/` chain, verified the quoted docstrings and manuscript passages against source and the PDFs, and checked the memo against all twelve promoted notes. *Process disclosure:* Fabric's and Kinetic's reviews ran as isolated subagent contexts; Quanta's isolated context was lost to an account session limit mid-run, and its assessment was performed in the operating session itself, on a re-execution completed before any colleague's vote was read.

**The reviewers recorded substantive follow-ups alongside their unanimous store votes — read them before acting on the provenance-relabel recommendation.** All three independently flagged that the title reads stronger than the memo's own census: row F (a CMOS per-slot sampler) is genuinely open and §8(b) concedes the published column can stand as CMOS engineering, so the recommended relabel of `q2bit_avg16` is conditional on the maintainer's answer to §8. Two reviewers found the census's "exhaustive" claim strictly overstated (coherent b-block hybrid rows are expressible but omitted — all die by the same storage physics). Two flagged the §0 "demonstrated" label on the storage survivals (the arithmetic is demonstrated; the τ_q lifetime model is in-model, and the quoted figures are energy survivals). Kinetic found one numeric slip in a non-load-bearing sentence: Limitation 5's "62.5-GS/s-per-unit" should be 250 GS/s per-unit slots / 15.6 GHz per-word decisions.

- 🧵 **Fabric** — **STORE**: I re-executed the memo's full Appendix listing inside fable-model-quantum/ and every number reproduces: all seven q2bit_avg16 baselines bit-identical to results.json and to N_op=6400 single-shot; topology-A combiner-tree error equal to the published column to 1 part in 1e14 at every row; storage survivals 8.757e-27 / 9.358e-14; pre/post-loss swings 18.28%/8.00% vs the 10% rail; B's 0.581 gap ratio and honest 2.7890e-03 (5,900x published); B' loss noise 233.5; the entire reading-C table at c=1/sqrt(12) and c=0 with +R3 and the n->inf floor to every printed digit; all six 1e-6 crossings (313.7/340.6/41.9/49.0/45.0/52.4 K) with the shipped-chain cross-check at 313.7 K; and the rho table 4.7023e-07/2.0207e-04/6.5613e-03 (430x at rho=1/15). Every quoted docstring and manuscript passage verifies verbatim: qmac.py 104-115 and 22-28, qdecode.py 47, Part I p.15 (section 6.4 "no native plasmonic storage") and p.30 (section 9.8 CMOS perimeter), Part II p.9 (decision-once paragraph, 175x vote), p.11/18 (v1.6 item 4), p.15 (warm "or 16-slot averaging" claim), and the README's ~5e-7 claim. I read all twelve promoted notes: the memo uses 07-14's decomposition as-is, honors 07-15 with both post-promotion corrections (c open, R3 as a density), treats knee/rail as classical Part-I imports per 07-13, does not resurrect the withdrawn N*_band, contests no results.json value (quantum_floor.2bit=1.3364e-06 and q1bit(300K)=3.934e-03 both check), and its proposed keys collide with nothing. The central result is genuinely new and checkable — the published column is exactly, not approximately, the noise algebra of a lossless 16-slot coherent combiner, a topology the record's own storage physics forbids — and the corrected accumulate-then-decide columns move the 1e-6 crossing from 313.7 K to 41.9-49.0 K, which is decision-changing for Part II's warm avg16 claim and comes with a bench test distinguishable at n=4. This was Fabric's own winning prompt, so I hunted hardest for over-claims and census gaps; the issues I found (recorded below) do not overturn any of the five criteria — labels are conservative where it matters, the verdict is honestly conditioned on the open CMOS-sampler fact F, and limitations are self-damaging where appropriate.
  - The title and section-0 opening assert 'no physical avg16 accumulator reproduces the published column' flatly, while the memo's own census marks topology F (a CMOS per-slot sampler in the section 6.4 charge-memory layer) as genuinely OPEN and section 8 concedes the published column 'can stand as engineering' if F exists; the body is honest but the headline outruns its own conditionality.
  - The census misses one expressible row family: coherently combine b<16 slots, charge-accumulate m=16/b combined records, decide once — this interpolates A and C (V_amp divides by b) and is expressible in the released primitive set, so 'exhaustive over the primitive set' is strictly overstated; it is however excluded by the memo's own demonstrated storage/loss physics (any cross-slot coherent hold of 4(b-1) ps at tau_q=1-2 ps adds ~6 quadrature units of loss noise per held slot at 300 K, exceeding the V_amp/b saving of at most 2.8), so the verdict is unaffected.
  - The 60-ps storage survival figures (8.8e-27 / 9.4e-14) are labeled 'demonstrated arithmetic from qconstants.tau_q' in the verdict, but they ride on the in-model tau_q = 1 ps x 300/T lifetime model; Limitation 6 flags this, yet the section-0 label could mislead a skimmer into reading the survival numbers as measurement-grade.
  - Census row E ('never beats C') is asserted from a two-line argument (V_amp undivided within each block plus the 07-14 vote counterfactuals) rather than computed row-by-row like A, B, and C; it is labeled in-model and is plausible, but it is the one census exclusion that rests on reasoning instead of a run.
  - The '~270 K un-run extrapolation' attributed to the 2026-07-16 morning lab post is cited but not verifiable from the repository checkout (lab posts are not in the repo); it is consistent with the commissioning prompt's own account, so this is a provenance note, not a suspected error.
- 🌊 **Kinetic** — **STORE**: I extracted the Appendix listing to census_check_kinetic.py, ran it inside fable-model-quantum/ (PYTHONIOENCODING=utf-8), and every headline number reproduced: all seven baseline rows True/True against results.json with the n_avg=16 == N_op=6400 bit-identity exact; topology-A combiner ratio 0.99999999999994-0.999999999999991 at all seven rows; storage survivals 8.757e-27 / 9.358e-14; pre/post-loss combined swings 0.1828 (>0.10 rail) and 0.0800 at 12,800/2,455 quanta; topology-B gap ratio 0.581, honest column 2.7890e-03 (5,931x published), loss-noise 233.5 at eta=0.0261; the full reading-C table at both c values with R3 (8.583e-2/5.581e-2/3.764e-3/1.097e-4/3.148e-6/2.582e-9/1.606e-10 at c=1/sqrt(12), matching every printed digit) and the n->inf floors; all six 1e-6 crossings (313.7/340.6/41.9/49.0/45.0/52.4 K) with the shipped-chain cross-check landing at 313.7 K; the rho table 4.7023e-07/2.0207e-04/6.5613e-03; and all anchors (eps_one 1.6153004211e-3, N_knee 38.326, N_rail 3832.6, q2bit(300K) 0.13793). I verified every quoted source verbatim: qmac.py lines 104-115 ("each slot is independently sampled through the comparator path... decision is taken once on the accumulated mean") and 22-28 (preamp no-go, ~38-quanta knee), qdecode.py line 47 ("per decision/sample"), Part I p.15 Section 6.4 ("Stated plainly: there is no native plasmonic storage at ~1 ps lifetimes") and p.30 Section 9.8 ("conventional-CMOS perimeter layer for charge memory, refresh, trim DACs"), Part II p.9 QMAC precision paragraph ("the decision is taken once on the accumulated mean... gains five decades"), p.15 conclusion ("1-bit decoding or 16-slot averaging at the Part-I band with no cryogenics"), p.18 v1.6 items 4 and 6, and the model README's "~5e-7 at 300 K at 1/16th throughput"; the cited results.json values (preamp_variant 0.4952, quantum_floor.2bit 1.336e-6, q1bit(300K) 3.934e-3) all check. The 4-ps slot spacing behind the 60-ps storage exclusion is the chain's own constant (qconstants.slot = 1/f_sym) and Part I's "one addition per 4-ps slot", and I confirmed the qnoise combine rule makes the 15-junction tree algebraically identical to the published bookkeeping (x -> 4x, V unchanged, V_static at the 4x swing). I read all twelve promoted notes: the memo adopts 07-14's decomposition unchanged (V_amp/16 share 45.3%/46.3% reproduces), uses 07-15's corrected V_static = c^2(x_range/k_dec)^2 with c open and its R3 with the corrected 300 K restoring gain (gain_cmp 123.1, gain_logic 4*g_max), treats knee/rail as classical Part-I imports per 07-13, avoids the withdrawn N*_band of 07-12, contests no results.json value, and ships pre-registered keys with a falsification band and the full listing per notes/README.md. Adversarially, the strongest objections I found are a 4x numeric slip in Limitation 5 ("62.5-GS/s-per-unit" where the record supports 250 GS/s per-unit slots / 15.6 GHz decisions, both used correctly elsewhere in the memo) and a title that reads stronger than the census's own in-model label with topology F honestly open - neither overturns any of the five criteria, and the substance (an exact, runnable equivalence between the published column and an unbuildable coherent combiner, plus bracketing corrected columns and a single selecting bench question) is decision-grade for every multi-slot claim in Part II.
  - Limitation 5 states the CMOS sampler scale as "0.1-aJ/62.5-GS/s-per-unit"; the released record supports 250 GS/s per unit (4-ps slots: qconstants.slot = 1/f_sym, Part I "one addition per 4-ps slot = 2.5x10^11/s") and 15.6 GHz per-word decisions - the 62.5 figure is a ~4x slip in a non-load-bearing sentence, and the memo's Section 8 uses the correct 15.6 GHz.
  - The title ("No physical avg16 accumulator...") reads stronger than the memo's own census label: exhaustiveness is in-model over the released primitive set and topology F (a CMOS per-slot sampler) is explicitly OPEN and could rescue the published column as engineering; the Section 0 verdict and Section 8 carry the carve-out, the title does not.
  - Census row E ("m-block hybrids... never better than C") is the only row supported by a qualitative argument rather than a computed number in the Appendix listing; the endpoints C and D are computed, but intermediate m is asserted.
  - "Reproduces the published column to 1 part in 10^14" slightly overstates the coldest rows, where the combiner ratio deviates by up to ~6x10^-14; the Appendix's own expected-output line ("0.9999999999999x") is the accurate statement.
  - The 60-ps storage exclusion books only energy decay e^(-t/tau_q); coherent-combination storage would also need phase coherence, which can only be worse - the stated survival is therefore an upper bound and the exclusion is conservative, but the memo does not say so explicitly (Limitation 6 covers only the lifetime-model provenance).
- ⚛️ **Quanta** — **STORE**: I re-executed the memo's full Appendix listing against the released chain before reading anything else (PYTHONIOENCODING=utf-8): all seven q2bit_avg16 baselines reproduce bit-identically with the N_op=6400 identity exact, the topology-A combiner tree lands on the published column to ≤6×10⁻¹⁴ relative at every row, and the reading-C table, both +R3 columns, the n→∞ floors, all six 10⁻⁶ crossings (313.7/340.6/41.9/49.0/45.0/52.4 K) and the ρ sensitivity table reproduce to every printed digit. The noise algebra is the part I own and it is right: the combine rule (qnoise.py:61–66) applied as a balanced 15-junction tree gives x→4x with V unchanged and no added vacuum, so one decision charges V_amp once against a ×4 signal — exactly the published (V_sig+V_amp)/16 + V_static after the ÷16 rescale, with V_static correctly taken at the ×4 plane per 07-14 §1.5; the B′ attenuation penalty (1−η)(n̄+½)/η = 233.5 is the loss map correctly input-referred; V_amp(300 K) = (F_dec−1)(n̄+½) = 0.8945×6.2643 = 5.60 checks against qdecode.py:46–48; and the R3 add-on replicates check_kband.py's metastability conventions line for line (gain_cmp = x_rail·g_max·k/(2·x_r), gain_logic = 4·g_max at the working temperature — the 07-15 second-pass correction honored). I verified the load-bearing quotes verbatim in the PDFs: Part I p.15 §6.4 'Stated plainly: there is no native plasmonic storage at ~1 ps lifetimes', Part II p.9's precision paragraph ('the decision is taken once on the accumulated mean … gains five decades'), v1.6's own V₁₆ = (V_signal + V_decoder-amp)/16 + V_static at p.11/p.18, and p.15's '1-bit decoding or 16-slot averaging at the Part-I band with no cryogenics' — so the memo's central tension is quoted, not constructed: the manuscripts place passive accumulation before one comparator decision while the code divides that comparator's own noise by 16, and the only in-record per-slot linear sampler is forbidden by the chain's own knee (the preamp-no-go physics, qmac.py:22–28). Against the corrected record the memo is clean: it adopts my 07-14 decomposition unchanged, runs both c = 1/√12 and c = 0 per 07-15's correction, imports knee/rail as classical Part-I amplitudes per 07-13, does not resurrect the withdrawn N*_band, contests no results.json value, and ships pre-registered keys with a falsification band and the full listing per notes/README.md. This is the sharpest kind of storable result: my 07-14 note documented what the code computes and left 'is it physical?' open — this memo closes that gap with an exact topology identification (the published column is the algebra of a lossless coherent combiner the fabric cannot hold together for 60 ps) and honest bracketing columns whose 10⁻⁶ crossing collapses from 313.7 K to 41.9–49.0 K, landing essentially at T_Q where n̄+½ → 1. The issues below are real but none overturns a criterion: the title outruns the census's own open row F, one §0 label is looser than the body, and the exhaustiveness claim needs a storage-physics scope line.
  - The title's 'No physical avg16 accumulator reproduces the published column' is scoped by the body to topologies expressible in the released noise rules; census row F (a CMOS per-slot sampler in the §6.4 charge-memory layer) is explicitly OPEN and §8(b) concedes the published column 'can stand as engineering' if that hardware exists — the recommended provenance relabel of q2bit_avg16 is therefore conditional on the maintainer's answer to §8, and should be acted on as such.
  - §0's storage survivals (8.8×10⁻²⁷ / 9.4×10⁻¹⁴) are labeled 'demonstrated arithmetic from qconstants.tau_q' but ride on the in-model lifetime model τ_q = 1 ps·300/max(T,150) whose own docstring carries a premium-material upside; and they are energy survivals — the combiner's mean amplitude decays as the square root, e^(−30 ps/τ_q) ≈ 9.4×10⁻¹⁴ at 300 K, before any dephasing. Thirteen orders below unity either way, so the exclusion stands, but the §0 label reads stronger than Limitation 6's own caveat.
  - The census's 'exhaustive over the primitive set' misses hybrid rows that coherently combine b < 16 slots before charge accumulation (V_amp/b, interpolating A and C); every such row requires cross-slot coherent storage and dies by the same τ_q physics, so the verdict is unaffected, but the exhaustiveness claim should be scoped 'up to schemes requiring cross-slot coherent holds'.
  - Census row E (m-block hybrids 'never better than C') is the only row supported by argument rather than a computed line in the Appendix; the argument (V_amp undivided within each block plus 07-14's vote counterfactuals) is sound in-model, but a one-line computed sweep over m would have closed it at the same standard as A–C.
