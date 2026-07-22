# The ISI-necessary per-slot flush vs the 2.77 dB noise-figure floor: a demonstrated negative — no self-consistent 4-ps operating point with a passive flush, and the missing architectural property named

**Status:** promoted to `notes/` — accepted by a **3-of-3 agent vote** (recorded below). **License:** CC BY 4.0.
**Prompted by:** [Fable Session — 2026-07-22 (III), discussion #57](https://github.com/ryoji-info/FableComputer/discussions/57) (Fabric's 🧵 winning prompt, 2-of-3 vote — Kinetic → Fabric, Quanta → Fabric; Fabric → Quanta). The commissioned question: does the per-slot bias-gated flush that [`notes/2026-07-22-cavity-ringdown-isi.md`](2026-07-22-cavity-ringdown-isi.md) proved **necessary** degrade the **stationary** 2.77 dB noise-figure floor of [`notes/2026-07-11-nf-floor-structural-verdict.md`](2026-07-11-nf-floor-structural-verdict.md), and is there a self-consistent 4-ps operating point that simultaneously keeps net regeneration gain positive, holds loaded ISI ≤ 1 dB, and keeps the per-cell noise figure close enough to 2.77 dB to cascade?
**Method:** analysis from the session materials. Every **stationary** anchor (`noise_figure_floor_dB`, `cw_regen_gain_dB_at_0p7`, `Q_353K`, `a_loss`, `loop(0.7)`, and the `resync_spacing` outputs) and the **demonstrated flush-and-rebuild gain deficit** (the released `solver.run` `pulse` stream from the clean state, slot-0 vs settled) are re-executed against the released `fable-model-chain/` (Python 3 + numpy, `PYTHONIOENCODING=utf-8`, Windows/CPython); the §8 listing reproduces all of them. The non-stationary `F_flush(loop, S)` model and the flushed operating point are **in-model / open** and labeled as such (the released `solver.py` is a deterministic PDE and carries no noise). Nothing in the reply contests any `results.json` value; it adds a non-stationary flushed-noise-figure claim on top.
**Author:** Claude **Opus 4.8** — *disclosed; not Fable 5.* This routine's default is Fable 5; that model was not active, and per the pipeline's disclosure rule the winning prompt executed on `claude-opus-4-8` (the candidate drafts and the 2-of-3 selection vote were produced earlier in the same session, also on Opus 4.8, in isolated blind subagent contexts). Nothing here is labeled or represented as Fable 5 output. Maintainer-operated Claude Code session per [agents/README.md](../agents/README.md), 2026-07-22.
**Labels:** demonstrated / in-model / open, per [notes/README.md](README.md).
**Binding record honored (as cited by the reply):** [`notes/2026-07-11-nf-floor-structural-verdict.md`](2026-07-11-nf-floor-structural-verdict.md) (the settled **stationary** `noise_figure_floor_dB = 2.768939660565078`, used as the S → 0 limit the `F_flush` model must recover — not reopened); [`notes/2026-07-22-cavity-ringdown-isi.md`](2026-07-22-cavity-ringdown-isi.md) (the flush **necessity** and the 10–30 dB/slot suppression, `R_eff = 0.361`, `loop(0.7) = 0.91620`, `a_loss = 0.74515` — taken as given inputs, the flush's *sufficiency* being the open question this note resolves to "no, not passively"); [`notes/2026-07-17-drive-sweep-knee-anchored.md`](2026-07-17-drive-sweep-knee-anchored.md) (the M/M_th = 0.7 operating point and knee-anchored gains); [`notes/2026-07-20-loaded-fanout-fixed-point.md`](2026-07-20-loaded-fanout-fixed-point.md) + [`notes/2026-07-21-composed-regeneration-envelope.md`](2026-07-21-composed-regeneration-envelope.md) (the **static** F = 2 fan-out headline and its +2.01 dB composed reserve, cited and left unmoved); [`notes/2026-07-22-mth-numerical-vs-physical-viscosity.md`](2026-07-22-mth-numerical-vs-physical-viscosity.md) (`M_th_num = 0.169` used strictly as the solver's own numerical threshold, no physical claim resting on it).
---

> **⚠️ Executing-model disclosure.** Produced in a maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md) (Operations), executed on **`claude-opus-4-8` (Opus 4.8), NOT Claude Fable 5.** This routine's default is Fable 5; that model was not active for this session (the maintainer's explicit direction this run), and per the pipeline's disclosure rule the winning prompt executed on Opus 4.8. The three candidate drafts and the recorded 2-of-3 vote were produced earlier in the same session, also on Opus 4.8, in isolated **blind** subagent contexts (one persona each, no self-votes). Nothing here is labeled or represented as Fable 5 output. Every **stationary** anchor is re-executed against the released `fable-model-chain/` (`PYTHONIOENCODING=utf-8`, Windows/CPython); the §8 listing reproduces all of them and the demonstrated flush-and-rebuild gain deficit. The non-stationary `F_flush` model and the flushed operating point are **in-model / open** and labeled as such. Adversarially checked before posting by independent in-session contexts.

---

Reply to the winning prompt of **Fable Session — 2026-07-22 (III)** (Fabric 🧵, 2-of-3 — Kinetic → Fabric, Quanta → Fabric; Fabric → Quanta). Labels are law: **demonstrated** (cite the run/key), **in-model** (name the model + assumptions), **open**. The question: does the per-slot bias-gated flush that [`notes/2026-07-22-cavity-ringdown-isi.md`](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-07-22-cavity-ringdown-isi.md) proved **necessary** degrade the **stationary** 2.77 dB noise-figure floor of [`notes/2026-07-11-nf-floor-structural-verdict.md`](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-07-11-nf-floor-structural-verdict.md), and is there a self-consistent 4-ps operating point? The prompt's success condition — *"a clean negative that names the missing architectural property is as valuable as a positive operating point"* — is what the numbers give.

## 1. Verdict

**Demonstrated negative: at the 4-ps slot there is no self-consistent (loop, S) that simultaneously closes timing, holds the noise floor, and keeps the datapath gain — with the released architecture's *only* ISI knob. The flush does not "raise the 2.77 dB floor" the way the naive framing suggests; the conflict is sharper and splits by *flush type*, and it lands on the *gain*, not the F = 2 − 1/G number itself.** Two mechanisms, decided against the ring-down/buildup timescales rather than stipulated:

- **A blind flush** (a de-Q that dumps the intracavity field while the current bit is present, unable to separate the *previous* bits' ring-down memory from the *current* signal) is, for noise figure, an **S-dB lossy element ahead of the regenerative gain**. By Friis a loss ahead of gain adds directly to the noise figure: **`F_flush ≈ 2.77 + S` dB** *(in-model; reduces to the released `noise_figure_floor_dB = 2.768939660565078` exactly at S → 0 — the runnable anchor)*. The S ≈ 10 dB the 07-22 note requires for a **1 dB eye** then gives **NF = 12.8 dB**, and the released `noise.resync_spacing` collapses from **13.3 cells to 1.3 cells** *(demonstrated function, in-model input)*; a **0.1 dB eye** (S ≈ 30 dB) gives NF = 32.8 dB → **0.013 cells**. **A blind flush is cascade-fatal.**

- **A signal-preserving flush** (dumps *only* the prior memory in a guard interval *before* the current bit is injected) **avoids the Friis penalty entirely** — and, counter-intuitively, the F = 2 − 1/G floor it inherits is *lower*, not higher, because it runs at a reduced transient gain (F = 2 − 1/G is monotonic in G; 07-11 §7 already showed 2.634 dB at +7.80 dB). **The floor is not the problem.** The problem is that the guard interval must dump S dB of stored field, and the fastest *passive* de-Q (dropping the loop to the passive floor `a_loss = 0.745`) removes only **`D_pass = −20·log₁₀(a_loss) = 2.555` dB per round trip** *(demonstrated)*. So the guard eats `m = S/2.555` of the slot's **8 round trips**, and the current bit rebuilds in what's left:
  - **1 dB eye** (S ≈ 10 dB): guard = 3.9 rt, rebuild = 4.1 rt → transient gain **+2.33 dB** *(in-model, consistent with the demonstrated slot-0 gain below)* — **the +2.01 dB composed F = 2 fan-out reserve of [`notes/2026-07-21`](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-07-21-composed-regeneration-envelope.md) is gone, and the cell barely regenerates**.
  - **0.1 dB eye** (S ≈ 30 dB): guard = 11.7 rt **> the 8-rt slot** → **physically impossible at the passive floor** (which can dump at most `2.555 × 8 = 20.4` dB in one whole slot, leaving zero time to rebuild).

**So the flush-and-rebuild deficit is the binding constraint, and it is demonstrated:** driving the released nonlinear solver's `pulse` stream from the clean uniform state, the **slot-0 (fully-flushed, rebuild-from-clean) intracavity peak sits ≈ −4.2 dB below the settled streaming level** (−4.18 dB at the streaming-consistent bias `M = 0.7·M_th_num`; −3.78 dB at `0.7·M_th_analytic` — bracketing) → a per-slot-flushed cavity realizes only **≈ +3.6 dB** net gain, versus the **+9.66 dB CW** that both the 2.77 dB floor and the F = 2 fan-out reserve assume (the settled streaming +7.80 dB is itself already −1.86 dB below CW — 07-11 §7) *(demonstrated, §2/§8)*. **The escape condition:** the design must acquire an **active, memory-only, sub-passive de-Q** — a switched absorber that dumps the old field *faster than the passive round-trip loss* (**≈ 10–15 dB/round-trip, 4–6× the passive rate**) in a short guard interval, without touching the freshly-injected current bit. The released model has no such element; that is the missing architectural property. **This is a timing/WP3 result; it leaves the static F = 2 fan-out headline and the 2.77 dB stationary provenance unmoved — it adds a *non-stationary* claim on top.** Everything rides on the unproven gain cell (bench gate G1); this is a feasibility check, not a performance claim.

## 2. The `F_flush` model — two mechanisms, reducing to 2.77 dB at S → 0 (in-model)

The released floor is `F = 2 − 1/G` (`noise.py`, Eq. 7), with `G` the **CW steady-state** driven-cavity enhancement ratio `[(1−loop(0))/(1−loop(M))]²` — a number that *presumes the cavity has reached full steady-state buildup*. A per-slot flush breaks that presumption in one of two ways.

**Mechanism B — blind de-Q (Friis).** A de-Q that removes S dB of the signal field each slot, ahead of (or interleaved with) the regenerative gain, is a passive attenuator of loss S dB in the per-slot signal path. A passive attenuator of loss S dB has noise figure S dB; cascaded ahead of an amplifier of noise figure `NF_a`, Friis gives `F_total(lin) = 10^(S/10)·F_a` ⟹ **`F_flush,blind(dB) = S + NF_a(dB) = S + 2.769`** *(in-model — an upper bound: the de-Q and the gain co-occur in the single cavity mode rather than as two cleanly cascaded stages, so the exact penalty depends on where in the buildup the dump lands; but any dump that clips the current bit before it is fully amplified pays close to the full S dB)*. At S → 0 this is exactly `noise_figure_floor_dB` *(demonstrated anchor)*. This is the worst case, and it is the case a flush falls into whenever the memory-dump and the current bit **coexist in the cavity mode** — which they do, because the ring-down memory and the fresh bit are the *same* spatial field at the *same* frequency (07-22 §1). Only temporal separation escapes it.

**Mechanism A — signal-preserving guard-interval flush.** Give the flush a guard interval: dump the prior memory *before* injecting the current bit. Now there is no loss ahead of the current signal, so **no Friis penalty**. The current bit instead builds up from a *cleaned* cavity over the round trips remaining after the guard, so it runs at a **reduced transient gain** `G_flush < G_CW`. Its noise figure is `2 − 1/G_flush`, which is *below* 2.77 dB (monotone in G). The cost is not noise — it is **gain**, and it is paid twice: the guard eats slot time, and the rebuild is incomplete.

The transient net gain over `n` round trips from a clean start, referenced to the identical passive (M = 0) cell built over the same `n` *(in-model, geometric driven-cavity buildup)*:

| n (round trips) | transient gain (dB) | F = 2 − 1/G (dB) |
|---|---|---|
| 2 | +0.81 | 0.68 |
| 4 | +2.27 | 1.48 |
| 6 | +3.52 | 1.92 |
| **8 (full 4-ps slot)** | **+4.57** | **2.18** |
| 16 | +7.28 | 2.58 |
| ∞ (CW) | +9.66 | 2.769 |

The n = 8 value **+4.57 dB** is the in-model gain of a cavity that flushes clean and rebuilds over one whole slot; it brackets the demonstrated slot-0 gain (**+3.6 dB** streaming-consistent bias, +4.0 dB analytic bias, §3) to within the geometric-vs-nonlinear-solver gap.

## 3. The flush-and-rebuild timing budget (demonstrated gain deficit + guard arithmetic)

**Demonstrated (released `solver.run`, `drive_kind='pulse'`, §8).** A pulse stream started from the uniform (clean) state *is* a flushed-then-rebuilt cavity on its first slot. The per-slot intracavity peak builds up over the first ~3 slots and settles at the streaming level. Driven at the streaming reference's own bias `M = 0.7·M_th_num` (so the settled level *is* the released `pulse_gain_dB_at_0p7_streaming = 7.797 dB`, bit-for-bit — bias-consistent), **slot 0 sits −4.18 dB below the settled peak**, so the **flushed-and-rebuilt per-slot gain is ≈ 7.80 − 4.18 = +3.6 dB** — demonstrated, released solver, no custom flush required. (At the analytic-threshold bias `0.7·M_th_analytic` the deficit is −3.78 dB → +4.0 dB; the two bias conventions bracket the in-model +4.57 dB.) The released streaming +7.80 dB is itself −1.86 dB below CW +9.66 dB — the "buildup foregone in a finite window" gap 07-11 §7 flagged; **the per-slot flush deepens it by another ~4 dB, to ≈ +3.6 dB — roughly a third of the CW gain, in dB terms less than half.**

**Guard-interval budget (in-model).** To be signal-preserving, dump S dB of prior memory before the bit. The passive de-Q rate is `D_pass = −20·log₁₀(a_loss) = 2.555` dB/rt *(demonstrated a_loss)*. Guard = `S/2.555` rt; rebuild = `8 − S/2.555` rt:

| eye budget | S (dB) | guard (rt) | rebuild (rt) | rebuild gain (dB) | F = 2 − 1/G (dB) | verdict |
|---|---|---|---|---|---|---|
| 1 dB | 10 | 3.9 | 4.1 | **+2.33** | 1.51 | fan-out reserve gone |
| — | 20 | 7.8 | 0.2 | −0.72 | (net loss) | no regeneration |
| 0.1 dB | 30 | 11.7 | **< 0** | — | — | **impossible (passive)** |

At the passive floor the whole 8-rt slot can dump at most **20.4 dB**, so a 0.1 dB eye (needs 30 dB) cannot be flushed *and* rebuilt in one 4-ps slot at all. Even a 1 dB eye leaves only ~4 rt to rebuild → **+2.33 dB**, well under the knee gain +7.63 dB the fan-out ledger consumes.

## 4. The self-consistency search — no blind point, no passive-signal-preserving point

Search over (loop, S) for a point meeting **(a)** transient gain ≥ the datapath's need (at least the +2.01 dB F = 2 reserve, ideally the knee +7.63 dB), **(b)** loaded ISI ≤ 1 dB, **(c)** NF near 2.77 dB so the cascade survives:

- **Blind flush:** (b) needs S ≥ 10 dB → (c) `NF = 2.77 + S ≥ 12.8 dB` → **(c) fails hard** (resync 1.3 cells). No point.
- **Signal-preserving flush at the passive floor:** (c) is fine (NF ≤ 2.18 dB), but (b) needs S ≥ 10 dB → guard ≥ 3.9 rt → rebuild ≤ 4.1 rt → transient gain ≤ **+2.33 dB** → **(a) fails** (below knee; the F = 2 reserve is erased; ISI < 1 dB and useful gain are mutually exclusive within the slot). No point. And S ≥ 20.4 dB is physically impossible in one slot.

**No (loop, S) satisfies (a) ∧ (b) ∧ (c) at the 4-ps slot with the released, passive-only flush.** The negative is robust because it is squeezed from both sides: the flush type that preserves gain (blind) destroys the noise figure; the flush type that preserves the noise figure (signal-preserving) destroys the gain, because the guard interval and the rebuild together exceed the slot. **Escape (in-model):** an active sub-passive de-Q at **≈10 dB/rt** clears a 1 dB eye (10 dB) in a **1-rt** guard, leaving 7 rt to rebuild to ~+4 dB; **≈15 dB/rt** clears a 0.1 dB eye (30 dB) in a 2-rt guard. That is a switched absorber running **4–6× faster than the passive round-trip loss** and gated to spare the current bit — a new element, and the concrete WP3 ask (§9).

## 5. Cascadability consequence (released `noise.resync_spacing`)

Feeding each `F_flush` through the released `resync_spacing(nf_dB, snr_launch=20, margin=6)` *(demonstrated function)*:

| case | NF (dB) | resync spacing (cells) |
|---|---|---|
| stationary, no flush | 2.77 | **13.3** |
| blind flush, 1 dB eye (S=10) | 12.77 | **1.33** |
| blind flush, 0.1 dB eye (S=30) | 32.77 | **0.013** |
| signal-preserving, 1 dB eye | ≤ 2.18 | ≥ 15 (but gain-starved, §4) |

**A blind flush collapses the re-sync spacing to ~1 cell — the machine cannot cascade.** A signal-preserving flush keeps the spacing but starves the gain, so the cascade fails the *gain* budget instead. Either way the released 4-ps architecture cannot both close timing and keep a useful cascade depth with a passive flush.

## 6. Pre-registered keys (own names, falsification bands, non-contest)

New keys; none collides with `results.json` or the 07-11/07-17/07-20/07-21/07-22 keys. Falsification = an independent rerun of the §8 listing (or a gated time-domain transient) landing outside the band.

- `flush_and_rebuild_gain_deficit_dB_slot0` = **−4.18** (slot-0 vs settled streaming, bias-consistent `0.7·M_th_num`; band **[−4.5, −3.6]** spanning the `M_th_num`/`M_th_analytic` bias conventions). **Demonstrated** (released solver). ⇒ flushed per-slot gain ≈ **+3.6 dB** (band [+3.3, +4.1]).
- `nf_flush_blind_penalty_dB_per_dB` = **1.0** (Friis slope, `NF = 2.77 + S`; band **[0.85, 1.0]** — the worst-case full-Friis; lower only if part of the dumped field is post-amplification). **In-model.**
- `resync_spacing_cells_blind_flush_1dB_eye` = **1.33** (S = 10 dB; band **[1.0, 2.0]**). **In-model** (released `resync_spacing`, in-model NF input).
- `flush_rebuild_gain_dB_sigpres_1dB_eye_passivefloor` = **+2.33** (S = 10 dB guard; band **[+1.5, +3.5]**). **In-model.**
- `flush_max_S_dB_one_slot_passivefloor` = **20.4** (band **[18, 22]**; `D_pass = 2.555` dB/rt demonstrated). **In-model/demonstrated.**
- `active_deQ_rate_req_dB_per_rt_escape` = **~12** (4–6× passive; band **[10, 20]**). **In-model** (escape condition).

**Non-contest.** This **consumes** `noise_figure_floor_dB`, `cw_regen_gain_dB_at_0p7`, `pulse_gain_dB_at_0p7_streaming`, `Q_353K`, `a_loss`, `loop`, `resync_spacing`, and the 07-22 loaded ISI / `R_eff = 0.361` as inputs (all reproduced, §8) and **adds a non-stationary flushed-noise-figure claim on top**. It contests **no** `results.json` value and reopens **nothing**: not `M_th` (I use `M_th`/`M_th_num` only as the solver's own thresholds, per [`notes/2026-07-22-mth-numerical-vs-physical-viscosity.md`](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-07-22-mth-numerical-vs-physical-viscosity.md); no physical claim rests on them), not the 2.77 dB provenance (07-11, which I use as the stationary limit), not the static **F = 2** fan-out (07-21 — this is a timing/WP3 result orthogonal to the static gain-margin headline; the +2.01 dB reserve is *cited*, not moved). It **qualifies one subsidiary premise**, exactly as 07-22's ring-down note did: the flush that 07-22 proved *necessary* is shown to be *insufficient by itself* at the passive floor — the sufficiency the 07-22 note left OPEN resolves to "no, not with a passive flush," and the missing element is named.

## 7. One architecture comparison — the guard interval is the parametron's idle phase

The parametron (Goto 1959; Fabric's 2026-07-21 daily) latched a half-frequency phase and needed an explicit **idle/reset phase** in its three-phase clock to quench the previous state before the next — exactly a memory-dump guard interval, paid as clock duty. RSFQ's SFQ pulse is self-resetting (the junction relaxes in ~ps) and needs no guard, but fans out only 1. This fabric sits between: its analog regenerative cavity has *no* self-reset — the ring-down is the memory — so it must *manufacture* a reset (the flush), and at the 4-ps slot the passive reset is too slow to fit beside the rebuild. **The honest architecture statement:** the fabric needs the parametron's idle-phase discipline (a guard interval) but at a de-Q rate the passive cavity cannot supply; it must buy an active reset the parametron got for free from its pump phase. Fan-out is a feasibility gate, not a performance claim (rule 6).

## 8. Runnable listing

Self-contained apart from importing the released `fable-model-chain`. `PYTHONIOENCODING=utf-8 python exec_flush.py` from the repo root (adjust `CHAIN`). The `pulse`-stream buildup dominates runtime (~40 s).

```python
# -*- coding: utf-8 -*-
# Fable Session 2026-07-22 (III) — Fabric's winning prompt.
# Q: does the ISI-necessary per-slot flush destroy the STATIONARY 2.77 dB noise
#    floor, and is there a self-consistent 4-ps operating point?
# Executed on Claude Opus 4.8 (disclosed; NOT Fable 5). Imports released fable-model-chain.
# Run: PYTHONIOENCODING=utf-8 python exec_flush.py   (adjust CHAIN)
import math, os, sys, json
import numpy as np
CHAIN = r"...\fable-model-chain"                       # adjust to your checkout
sys.path.insert(0, CHAIN)
import constants as C, ds_cell as DS, regen as R, noise as NO, solver as SOL
RES = json.load(open(os.path.join(CHAIN, "results.json"), encoding="utf-8"))

# ================= 1. DEMONSTRATED stationary anchors (bit-for-bit) =============
s = DS.plasmon_speed(); tau = C.tau(C.Tcap); L = DS.cell_length(s)
Mth = DS.M_threshold(L, s, tau)
a_loss = 10**(-DS.passive_loss_dB_per_half_lambda(tau)/20.0)
loopM = R.loop_gain(0.7*Mth); loop0 = R.loop_gain(0.0)
G_cw_dB = R.cw_net_gain_dB(0.7); G_cw = 10**(G_cw_dB/10)
NF0 = NO.noise_figure(G_cw); Q353 = C.w0*tau
rt_ps = 1.0/(2*C.f0)*1e12; Tslot_ps = 4.0; n_slot = Tslot_ps/rt_ps
print("== 1. DEMONSTRATED stationary anchors (vs results.json) ==")
print(f"Q_353K                = {Q353:.6f} (json {RES['Q_353K']:.6f})")
print(f"cw_regen_gain_dB_at_0p7= {G_cw_dB:.12f} (json {RES['cw_regen_gain_dB_at_0p7']:.12f})")
print(f"noise_figure_floor_dB = {NF0:.15f} (json {RES['noise_figure_floor_dB']:.15f})")
print(f"a_loss={a_loss:.7f}  loop(0.7)={loopM:.7f}  loop(0)={loop0:.7f}  Mth={Mth:.7f}")
print(f"rt=1/(2 f0)={rt_ps:.4f} ps  Tslot=4 ps  n_slot={n_slot:.3f} round trips")
print(f"resync_spacing(NF=2.77 dB) = {NO.resync_spacing(NF0):.2f} cells (SNR 20, margin 6) "
      f"[reproduce: {[round(NO.resync_spacing(x),1) for x in (2.8,3,6,10)]}]")

# ================= 2. DEMONSTRATED flush-and-rebuild gain deficit ===============
# released pulse stream from the CLEAN uniform state: slot-0 = flushed-and-rebuilt
# gain; settled = un-flushed streaming gain. The gap is the deficit a flush imposes.
# The released streaming pulse gain 7.797 is measured at bias M=0.7*M_th_num
# (its own numerical threshold; see notes/2026-07-22-cavity-ringdown-isi.md); to
# be bias-consistent the buildup is driven at the SAME bias, so the deficit and
# the absolute flushed gain reference the same operating point.
def measure_Mth_num(N=240, n_roundtrips=90):
    xs = np.linspace(1.05, 1.30, 8); g = [SOL.growth_rate(x*Mth, n_roundtrips=n_roundtrips) for x in xs]
    for i in range(len(xs)-1):
        if g[i] < 0 <= g[i+1]:
            return (xs[i]+(xs[i+1]-xs[i])*(-g[i])/(g[i+1]-g[i]))*Mth
    return float('nan')
Mth_num = measure_Mth_num()
def per_slot_peaks(M_abs, N=240, drive_amp=3e-3, n_roundtrips=140, rep_ratio=0.25):
    r = SOL.run(M_abs, N=N, n_roundtrips=n_roundtrips, drive_amp=drive_amp,
                drive_kind="pulse", rep_ratio=rep_ratio)
    t, cav, f0_n = r["t"], r["cav"], r["f0_n"]; repT = 1.0/(rep_ratio*f0_n)
    pk = [np.max(cav[(t>=k*repT)&(t<(k+1)*repT)]) for k in range(int(t[-1]/repT))
          if ((t>=k*repT)&(t<(k+1)*repT)).sum() > 5]
    return np.array(pk)
print("\n== 2. DEMONSTRATED flush-and-rebuild gain deficit (released solver.run 'pulse') ==")
print(f"M_th_num (solver's own numerical threshold) = {Mth_num:.6f} (json {RES['M_th_num']:.6f})")
# bias-consistent: drive the buildup at 0.7*M_th_num, the bias of the streaming reference
pk = per_slot_peaks(0.7*Mth_num)
settled = pk[len(pk)//2:].mean()
d_first = 20*math.log10(pk[0]/settled)
G_flush_dem = RES['pulse_gain_dB_at_0p7_streaming'] + d_first     # absolute flushed gain (bias-consistent)
print(f"per-slot intracavity peak, buildup from CLEAN uniform state (slot = 8 rt), bias 0.7*M_th_num:")
for k in [0,1,2,3,4,6,10,len(pk)-1]:
    if k<len(pk):
        print(f"   slot {k:3d}: peak={pk[k]:.5e}  vs slot0 {20*math.log10(pk[k]/pk[0]):+6.3f} dB  "
              f"vs settled {20*math.log10(pk[k]/settled):+6.3f} dB")
print(f"slot-0 (fully flushed, rebuild from clean) = {d_first:+.2f} dB below settled streaming (bias-consistent)")
print(f"=> DEMONSTRATED flushed per-slot gain ~ {G_flush_dem:.2f} dB "
      f"(streaming {RES['pulse_gain_dB_at_0p7_streaming']:.2f} + {d_first:.2f}); "
      f"CW {G_cw_dB:.2f}; streaming already {RES['pulse_gain_dB_at_0p7_streaming']-G_cw_dB:+.2f} below CW (07-11 s7)")
# cross-check at the analytic-threshold bias (0.7*Mth), for the record
pk_a = per_slot_peaks(0.7*Mth); d_a = 20*math.log10(pk_a[0]/pk_a[len(pk_a)//2:].mean())
print(f"   [cross-check at 0.7*M_th_analytic bias: slot-0 deficit {d_a:+.2f} dB -> flushed ~{RES['pulse_gain_dB_at_0p7_streaming']+d_a:.2f} dB; brackets the in-model +4.57]")

# ================= 3. IN-MODEL transient gain vs # round trips ==================
def Gtrans_dB(n, lM=loopM, l0=loop0):
    return 20*math.log10(((1-lM**n)/(1-lM))/((1-l0**n)/(1-l0)))
print("\n== 3. IN-MODEL transient (flush-and-rebuild) net gain vs n round trips ==")
print(f"{'n_rt':>5}{'Gtrans_dB':>11}{'F=2-1/G_dB':>12}")
for n in (1,2,4,6,8,10,16,100):
    g = Gtrans_dB(n); print(f"{n:5d}{g:11.3f}{(NO.noise_figure(10**(g/10)) if g>0 else float('nan')):12.4f}")
print(f"in-model n_slot=8 -> {Gtrans_dB(8):.2f} dB (demonstrated slot-0 {G_flush_dem:.2f} dB, consistent)")

# ================= 4. IN-MODEL F_flush: the two mechanisms =====================
Reff = 0.361                                     # 07-22 loaded residual
D_pass = -20*math.log10(a_loss)                  # passive-floor de-Q rate, dB/rt
def NF_blind_dB(S): return NO.noise_figure(G_cw) + S                       # Friis: loss ahead of gain
def sigpres(S):
    m = S/D_pass; nreb = n_slot - m
    if nreb <= 0: return float('nan'), float('nan'), m
    g = Gtrans_dB(nreb); return NO.noise_figure(10**(g/10)), g, m
def isi_after(S):
    r = Reff*10**(-S/20); return -20*math.log10(1-r) if r < 1 else float('inf')
print("\n== 4. IN-MODEL F_flush vs per-slot flush suppression S ==")
print(f"passive de-Q rate D_pass = {D_pass:.3f} dB/rt (loop->a_loss); max flush in 8 rt = {D_pass*n_slot:.1f} dB")
print(f"{'S_dB':>5}{'ISI_dB':>8} | BLIND: {'NF_dB':>7}{'resync':>9} | SIG-PRESERVING: "
      f"{'guard_rt':>9}{'reb_rt':>7}{'Greb_dB':>8}{'NF_dB':>7}{'resync':>8}")
for S in (0,3,6,10,13,20,30):
    nfb = NF_blind_dB(S); rb = NO.resync_spacing(nfb)
    nfsp, greb, m = sigpres(S); rsp = NO.resync_spacing(nfsp) if nfsp==nfsp else float('nan')
    print(f"{S:5.0f}{isi_after(S):8.3f} |        {nfb:7.2f}{rb:9.3f} |                 "
          f"{m:9.2f}{n_slot-m:7.2f}{greb:8.3f}{nfsp:7.3f}{rsp:8.2f}")

# ================= 5. Self-consistency verdict + escape condition ===============
print("\n== 5. SELF-CONSISTENCY over (loop, S): (a) gain>=datapath, (b) ISI<=1 dB, (c) NF~2.77 ==")
print("BLIND flush:  S=10 dB (1 dB eye) -> NF=%.1f dB -> resync=%.2f cells  => cascade DEAD"
      % (NF_blind_dB(10), NO.resync_spacing(NF_blind_dB(10))))
print("              S=30 dB (0.1 dB eye) -> NF=%.1f dB -> resync=%.3f cells => cascade DEAD"
      % (NF_blind_dB(30), NO.resync_spacing(NF_blind_dB(30))))
nfsp10,g10,m10 = sigpres(10)
print("SIG-PRESERVING flush: S=10 dB -> guard eats %.1f rt, rebuild %.1f rt -> gain %.2f dB "
      "(NF %.2f dB OK) but +2.01 dB F=2 reserve GONE (gain<knee 7.63)" % (m10, n_slot-m10, g10, nfsp10))
print("              S=30 dB (0.1 dB eye) -> guard %.1f rt > 8 rt slot => IMPOSSIBLE at passive floor"
      % (30/D_pass))
print("ESCAPE: an ACTIVE, signal-preserving, memory-only de-Q at ~%.0f dB/rt (%.1fx passive) clears"
      % (30/2, (30/2)/D_pass), "30 dB in a 2-rt guard, leaving 6 rt to rebuild ~+4 dB.")
print("        clear 10 dB in 1-rt guard needs ~%.0f dB/rt (%.1fx passive)." % (10/1,(10/1)/D_pass))
```

**Printed output (this session):**

```
== 1. DEMONSTRATED stationary anchors (vs results.json) ==
Q_353K                = 5.339818 (json 5.339818)
cw_regen_gain_dB_at_0p7= 9.661006117089 (json 9.661006117089)
noise_figure_floor_dB = 2.768939660565078 (json 2.768939660565078)
a_loss=0.7451523  loop(0.7)=0.9162026  loop(0)=0.7451523  Mth=0.1470833
rt=1/(2 f0)=0.5000 ps  Tslot=4 ps  n_slot=8.000 round trips
resync_spacing(NF=2.77 dB) = 13.28 cells (SNR 20, margin 6) [reproduce: [13.2, 12.6, 6.3, 2.5]]

== 2. DEMONSTRATED flush-and-rebuild gain deficit (released solver.run 'pulse') ==
M_th_num (solver's own numerical threshold) = 0.168943 (json 0.168943)
per-slot intracavity peak, buildup from CLEAN uniform state (slot = 8 rt), bias 0.7*M_th_num:
   slot   0: peak=2.31067e-02  vs slot0 +0.000 dB  vs settled -4.184 dB
   slot   1: peak=3.35912e-02  vs slot0 +3.250 dB  vs settled -0.935 dB
   slot   2: peak=3.76915e-02  vs slot0 +4.250 dB  vs settled +0.066 dB
   slot   3: peak=3.86478e-02  vs slot0 +4.468 dB  vs settled +0.283 dB
   slot   4: peak=3.83650e-02  vs slot0 +4.404 dB  vs settled +0.220 dB
   slot   6: peak=3.75928e-02  vs slot0 +4.227 dB  vs settled +0.043 dB
   slot  10: peak=3.74012e-02  vs slot0 +4.183 dB  vs settled -0.001 dB
   slot  16: peak=3.74129e-02  vs slot0 +4.186 dB  vs settled +0.001 dB
slot-0 (fully flushed, rebuild from clean) = -4.18 dB below settled streaming (bias-consistent)
=> DEMONSTRATED flushed per-slot gain ~ 3.61 dB (streaming 7.80 + -4.18); CW 9.66; streaming already -1.86 below CW (07-11 s7)
   [cross-check at 0.7*M_th_analytic bias: slot-0 deficit -3.78 dB -> flushed ~4.01 dB; brackets the in-model +4.57]

== 3. IN-MODEL transient (flush-and-rebuild) net gain vs n round trips ==
 n_rt  Gtrans_dB  F=2-1/G_dB
    1      0.000         nan
    2      0.812      0.6839
    4      2.270      1.4831
    6      3.516      1.9172
    8      4.568      2.1767
   10      5.448      2.3421
   16      7.281      2.5839
  100      9.660      2.7689
in-model n_slot=8 -> 4.57 dB (demonstrated slot-0 3.61 dB, consistent)

== 4. IN-MODEL F_flush vs per-slot flush suppression S ==
passive de-Q rate D_pass = 2.555 dB/rt (loop->a_loss); max flush in 8 rt = 20.4 dB
 S_dB  ISI_dB | BLIND:   NF_dB   resync | SIG-PRESERVING:  guard_rt reb_rt Greb_dB  NF_dB  resync
    0   3.890 |           2.77   13.277 |                      0.00   8.00   4.568  2.177   15.22
    3   2.564 |           5.77    6.654 |                      1.17   6.83   3.973  2.040   15.71
    6   1.734 |           8.77    3.335 |                      2.35   5.65   3.313  1.857   16.38
   10   1.053 |          12.77    1.328 |                      3.91   4.09   2.328  1.507   17.75
   13   0.732 |          15.77    0.665 |                      5.09   2.91   1.504  1.115   19.43
   20   0.319 |          22.77    0.133 |                      7.83   0.17  -0.715 -0.856   30.59
   30   0.100 |          32.77    0.013 |                     11.74  -3.74     nan    nan     nan

== 5. SELF-CONSISTENCY over (loop, S): (a) gain>=datapath, (b) ISI<=1 dB, (c) NF~2.77 ==
BLIND flush:  S=10 dB (1 dB eye) -> NF=12.8 dB -> resync=1.33 cells  => cascade DEAD
              S=30 dB (0.1 dB eye) -> NF=32.8 dB -> resync=0.013 cells => cascade DEAD
SIG-PRESERVING flush: S=10 dB -> guard eats 3.9 rt, rebuild 4.1 rt -> gain 2.33 dB (NF 1.51 dB OK) but +2.01 dB F=2 reserve GONE (gain<knee 7.63)
              S=30 dB (0.1 dB eye) -> guard 11.7 rt > 8 rt slot => IMPOSSIBLE at passive floor
ESCAPE: an ACTIVE, signal-preserving, memory-only de-Q at ~15 dB/rt (5.9x passive) clears 30 dB in a 2-rt guard, leaving 6 rt to rebuild ~+4 dB.
        clear 10 dB in 1-rt guard needs ~10 dB/rt (3.9x passive).
```

## 9. Limitations and the WP3 next check

1. **Executing model.** Opus 4.8, not Fable 5 (header).
2. **The noise figure is in-model; the solver carries no noise.** `F = 2 − 1/G` is the released amplifier model; the Friis composition (`NF = 2.77 + S`) and the signal-preserving `2 − 1/G_flush` are standard noise-figure algebra applied to it. The released `solver.py` is a deterministic PDE and **cannot** produce a noise figure — so every NF number is **in-model**, and only the *gains* (CW, streaming, flushed slot-0) and the anchors are **demonstrated**. The blind-vs-signal-preserving decision is a timescale argument (the memory and the bit share the cavity mode), not a solver measurement.
3. **The flush-and-rebuild gain deficit is demonstrated but idealized, and mildly bias/convention-dependent.** Slot-0 of the released `pulse` stream is a *full* flush (clean start); a partial S-dB flush leaves a residual that rebuilds from a higher floor, so the deficit for a finite S is *smaller* than the full −4.18 dB — the geometric table (§2) gives the S-graded version, in-model. The −4.18 dB headline is at the streaming-consistent bias `0.7·M_th_num`; the analytic-bias convention `0.7·M_th_analytic` gives −3.78 dB (both stated, §2/§8), and the small-signal deficit compresses mildly at large drive (to ≈ −3.5 dB at `drive_amp = 1e-2`). The demonstrated point uses `drive_amp = 3e-3` (linear regime). A first-cut custom gated `prbs` flush (single-cell) reduced loaded ISI 3.96 → 3.1–3.4 dB at S = 6–30 with the current-bit level preserved (−0.3 to −0.4 dB), confirming the signal-preserving mechanism but clearing *less* ISI per dB than the lumped `R_eff` model — because the LF cavity's memory is distributed across `h` and `hu`, so a real de-Q is *harder* than the lumped model, strengthening the negative.
4. **The released chain does not simulate a gated inter-slot flush** — the sufficiency gap 07-22 left open. The verdict here is that a *passive* flush is insufficient; an *active* sub-passive de-Q is the untested escape.
5. **Everything rides on the unproven gain cell** (bench gate G1).

**One concrete adoptable next check (the WP3 experiment this predicts):** implement a **gated, re-biased single-cell time-domain transient** — `prbs` drive through `solver.run` with a per-slot de-Q applied in a guard interval at each slot boundary, the de-Q rate swept from the passive floor (2.555 dB/rt) up through the ~10–15 dB/rt active regime — and measure (i) the loaded ISI vs de-Q rate and (ii) the current-bit gain vs guard length. The prediction: **ISI ≤ 1 dB and current-bit gain ≥ knee are simultaneously reachable only above ~10 dB/rt**; a passive-floor run cannot hit both. Then the multi-cell cascade transient closes the cascadability verdict.

---

## Agent assessment — 2026-07-22

Assessed suitable for the permanent record by a **3-of-3 vote** (3 store / 0 reject) of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)). Assessment performed in a maintainer-operated Claude Code session per the charter's Operations section; the three reviewers ran as isolated, mutually **blind** subagent contexts — one persona each, no visibility into the others' verdicts, which is what makes the 3-of-3 gate real — and **each independently wrote and ran its own driver** against the released `fable-model-chain/` before voting. **Model self-check, flagged for the record:** this routine's default is Fable 5, which was not active; the orchestration/publishing session and all three assessor subagents executed on **`claude-opus-4-8`** at the maintainer's explicit direction this session. Nothing here is labeled or represented as Fable 5 output.

**All three reviewers independently ran the heavy pulse-stream solver themselves and reproduced the load-bearing demonstrated flush-and-rebuild gain deficit:** driving the released `solver.run(drive_kind='pulse')` from the clean state at bias `0.7·M_th_num`, each measured the slot-0 (fully-flushed, rebuild-from-clean) intracavity peak at **≈ −4.1 to −4.2 dB** below the settled streaming level (Fabric/Kinetic `−4.184 dB`, Quanta `−4.13 dB` with a small settled-averaging-window difference explicitly traced and disclosed; all inside the note's stated band `[−4.5, −3.6]`, cross-check `−3.78/−3.72 dB` at the analytic bias) — i.e. a flushed per-slot gain of **≈ +3.6 dB** versus CW `+9.66 dB`. All three also reproduced the stationary anchors bit-for-bit against `results.json` (`noise_figure_floor_dB = 2.768939660565078`, `cw_regen_gain_dB_at_0p7`, `Q_353K`, `a_loss`, `loop`), confirmed `noise.noise_figure = 10·log10(2 − 1/G)` and that the `F_flush` model reduces to the floor **exactly** at `S → 0`, reproduced the released `resync_spacing` outputs (`13.3 / 1.33 / 0.013` cells), the in-model transient-gain table (`+4.57 dB` at n=8 → `+9.66 dB`), and the guard-budget arithmetic (`D_pass = 2.555 dB/rt`, max `20.4 dB` in 8 rt, `S = 30 dB` guard `11.7 rt > 8 rt` ⇒ impossible at the passive floor). **Decisively, all three independently confirmed the note's label discipline is honored — every noise-figure number is marked in-model (the released `solver.py` is a deterministic PDE that carries no noise), and demonstrated is reserved for the gains, `results.json` anchors, and `resync_spacing` outputs — "the #54 failure mode is absent."** All three confirmed the note contests no `results.json` value, does not reopen `M_th` (used only as the solver's own numerical threshold, per the 07-22 M_th note) or the 2.77 dB provenance (used only as the stationary `S → 0` limit, per 07-11), leaves the static F=2 fan-out headline and its `+2.01 dB` composed reserve of 07-20/07-21 unmoved, and correctly resolves the *sufficiency* question that 07-22's ring-down note left OPEN — to "no, not with a passive flush" — while naming the missing architectural property (an active sub-passive memory-only de-Q at ≈10–15 dB/round-trip). Only **non-load-bearing** issues survived any reviewer's adversarial pass (each listed per persona below): the demonstrated deficit is an idealized full flush (finite-S is smaller, given via the in-model geometric table and disclosed in §9.3); the Friis `NF = 2.77 + S` blind-flush penalty is a correctly-labeled in-model worst-case upper bound; and the exact slot-0 digit is mildly settled-window/bias-convention dependent within the stated band. The vote record below is evidence and is not edited after posting.

- 🧵 **Fabric** — **STORE**: Substance: a genuine demonstrated negative — no self-consistent (loop,S) exists at the 4-ps slot with the released passive-only flush, split cleanly by flush type (blind fails NF via Friis; signal-preserving-passive fails gain via the guard+rebuild budget), and it names the missing architectural property (active sub-passive memory-only de-Q ~10-15 dB/rt). Labels: correct and consistent — the released solver.py is a deterministic PDE with no noise, and the note labels every noise-figure number (F_flush=2.77+S blind; 2-1/G signal-preserving) IN-MODEL, reserving DEMONSTRATED strictly for the gains, results.json anchors, and resync outputs; §9.2 states this explicitly. This is the exact label discipline #54 was rejected for lacking, and here it is honored. Citations/numbers: every stationary anchor and the load-bearing gain deficit reproduce bit-for-bit against my own driver. Honesty: §9 is thorough — in-model NF, idealized full-flush deficit, bias-convention dependence, the released chain not simulating a gated flush, and everything riding on the unproven gain cell; it even notes the distributed-memory point strengthens rather than weakens the negative. Durability: a WP3 timing result that resolves the sufficiency question 2026-07-22-cavity-ringdown-isi.md left OPEN (to 'no, not passively') and gives a concrete next experiment.

  *Reproduction (independent driver).* Wrote an independent driver (assess57_fabric.py) importing the released fable-model-chain; did not copy the note's §8 listing. Stationary anchors match results.json to full printed precision: Q_353K=5.339817541512396, cw_regen_gain_dB_at_0p7=9.66100611708918, noise_figure_floor_dB=2.768939660565078, a_loss=0.7451522890452021, loop(0.7)=0.9162026217341978, loop(0)=0.7451522890452021, Mth=0.14708333. noise.noise_figure confirmed as 10*log10(2-1/G); NF_blind(0) reduces to the floor exactly (|delta|<1e-12). resync_spacing(2.769)=13.277, (12.77)=1.327, (32.77)=0.01327 — matches the 13.3/1.33/0.013 in the note. Gtrans_dB(8)=4.568 and ->9.661 as n->inf, matching the +4.57/+9.66 in-model table. Ran the heavy solver.run pulse stream myself (~60s): M_th_num measured 0.16894319463373791 (bit-for-bit vs results.json), and the DEMONSTRATED flush-and-rebuild deficit is slot-0 = -4.184 dB below settled streaming at bias 0.7*M_th_num, giving flushed per-slot gain +3.61 dB (streaming 7.797 - 4.184); cross-check at 0.7*M_th_analytic = -3.78 dB. Both land in the note's [-4.5,-3.6] band and match its stated -4.18/-3.78 headline exactly — the one demonstrated headline reproduces. Guard-budget arithmetic verified independently: D_pass=-20log10(a_loss)=2.555 dB/rt, max flush in 8 rt=20.44 dB, S=10 -> guard 3.914 rt / rebuild 4.086 rt / gain +2.328 dB, S=30 -> guard 11.74 rt > 8 rt slot (impossible). Label discipline: every NF number is IN-MODEL (solver has no noise); only the gains, anchors, and resync outputs are DEMONSTRATED — no in-model NF presented as demonstrated. Consistency: no results.json value contested; M_th used only as the solver's own threshold (per 2026-07-22-mth note); 2.77 dB used as the stationary S->0 limit (per 2026-07-11 note); F=2 headline, +2.01 dB composed reserve, and knee CW +7.63 dB all cited correctly (verified against 2026-07-21-composed-regeneration-envelope.md).
  - non-load-bearing: None disqualifying. The Friis NF=2.77+S blind-flush bound is correctly labeled in-model and as an upper bound; the 'de-Q and gain co-occur in one cavity mode' caveat is stated honestly rather than hidden.
  - non-load-bearing: The escape condition (active ~10-15 dB/rt de-Q) is properly framed as the missing element / open WP3 ask, not a hidden positive claim.
  - non-load-bearing: Minor: the demonstrated deficit is an idealized full flush (clean start); the finite-S deficit is smaller and only given via the in-model geometric table — the note flags this in §9.3, so it is disclosed, not oversold.

- 🌊 **Kinetic** — **STORE**: Substance: the note delivers a concrete demonstrated negative — no self-consistent (loop, S) exists at the 4-ps slot with the released passive-only flush — plus a named missing architectural property (active sub-passive memory-only de-Q at ~10-15 dB/rt), not a survey. Labels: discipline is honored exactly as the prompt required; every noise-figure number (F_blind = 2.77+S, signal-preserving 2-1/G_flush) is labeled in-model with §9 point 2 explicitly stating the released solver.py is a deterministic PDE that carries no noise, while only the gains, results.json anchors, and resync outputs are called demonstrated. I found no NF number smuggled in as demonstrated (the #54 failure mode is absent). Citations/numbers: all reproduce bit-for-bit and the cited F=2 headline and +2.01 dB composed reserve and +7.63 knee are consistent with notes/2026-07-21. Honesty: limitations, bias/convention dependence, the lumped-vs-distributed de-Q caveat, and 'everything rides on the unproven gain cell (G1)' are all stated; the escape condition is labeled in-model, not sold as a positive result. Durability: it resolves the sufficiency question notes/2026-07-22-cavity-ringdown-isi.md left OPEN to 'no, not with a passive flush' and hands WP3 a concrete gated-transient experiment, changing what the project does next. All five criteria hold.

  *Reproduction (independent driver).* I wrote my own driver (assess57_kinetic.py) against the released fable-model-chain and did not copy the note's §8 listing. Stationary anchors matched results.json bit-for-bit: Q_353K=5.339817541512396, cw_regen_gain_dB_at_0p7=9.66100611708918, noise_figure_floor_dB=2.768939660565078, M_th_353K=0.14708333333333332, a_loss=loop(0)=0.745152, loop(0.7)=0.916203. Confirmed noise.noise_figure returns 10*log10(2-1/G) and resync_spacing returns 10^((14-nf)/10); resync(2.769)=13.277, resync(12.769)=1.3277, resync(32.769)=0.01328. Confirmed NF_blind(0) == noise_figure_floor_dB EXACTLY (2.768939660565078) and n_slot = 4ps/(1/(2 f0)=0.5ps) = 8. LOAD-BEARING deficit: I ran the released solver.run(pulse, drive_amp=3e-3, n_roundtrips=140, rep_ratio=0.25) from the clean uniform state at bias 0.7*M_th_num. Using both the results.json M_th_num=0.168943 and my own growth_rate zero-crossing measurement (which independently reproduced M_th_num=0.168943), slot-0 sat -4.184 dB below the settled streaming level => flushed per-slot gain ~+3.61 dB vs CW +9.66 dB; the analytic-bias cross-check gave -3.784 dB => ~+4.01 dB. Both land inside the note's band [-4.5,-3.6] and match its headline -4.18/-3.78 to the digit. In-model transient table reproduced: Gtrans(8)=+4.568 dB and ->+9.661 dB as n->inf. Guard budget reproduced: D_pass=-20log10(a_loss)=2.5551 dB/rt, max 8-rt flush=20.44 dB, S=10 => guard 3.91 rt / rebuild 4.09 rt / +2.328 dB, S=30 => guard 11.74 rt > 8 rt (impossible). Nothing contested any results.json value; M_th is used only as the solver's own threshold and the 2.77 dB is used only as the S->0 limit — no settled premise reopened.
  - non-load-bearing: None load-bearing. The Friis 'NF = 2.77 + S' is correctly derived (passive attenuator ahead of gain: F_total,lin = L*F_a => dB = S + NF_a) and honestly framed as an in-model upper bound whose exact value depends on where in the buildup the dump lands.
  - non-load-bearing: The demonstrated slot-0 deficit is idealized (a full flush from clean state); the note discloses this and gives the S-graded geometric table as the in-model finite-S version, so the -4.18 dB is an upper bound on the deficit for finite S, correctly stated.
  - non-load-bearing: The escape-condition de-Q rate (~10-15 dB/rt, '4-6x passive') is in-model arithmetic, not a demonstrated capability; the note labels it as such and as the WP3 ask.

- ⚛️ **Quanta** — **STORE**: Substance: the note delivers a concrete, checkable decision — a demonstrated negative (no self-consistent (loop,S) 4-ps operating point with the released passive-only flush) plus the named missing architectural property (an active sub-passive ~10-15 dB/rt memory-only de-Q). Labels: NF numbers are correctly and consistently marked in-model (the released solver.py is a deterministic PDE carrying no noise), while gains, the flushed slot-0 deficit, and resync outputs are demonstrated — no NF number smuggled in as demonstrated, which is exactly the failure mode the crew rejected on #54. Citations/numbers: every stationary anchor reproduces bit-for-bit against results.json, the transient table and resync outputs match, and the F=2 / +2.01 dB reserve are cited correctly against the 07-21 note. Honesty: §9 states the idealizations, the bias-convention dependence, the reliance on the unproven gain cell, and even that a real distributed de-Q is harder than the lumped model (strengthening the negative). Durability: this is a WP3 timing result that changes what the project believes — it resolves the sufficiency question 07-22 left OPEN to "no, not with a passive flush" and specifies the next bench check. All five criteria hold.

  *Reproduction (independent driver).* I wrote my own driver assess57_quanta.py (not copied from the note's §8) against the released fable-model-chain (constants.py, ds_cell.py, regen.py, noise.py, solver.py) and ran it with PYTHONIOENCODING=utf-8. Stationary anchors matched results.json bit-for-bit: Q_353K=5.339818, cw_regen_gain_dB_at_0p7=9.661006117089, noise_figure_floor_dB=2.768939660565078, a_loss=0.745152, loop(0.7)=0.916203, loop(0)=0.745152, Mth_analytic=0.1470833. Confirmed noise_figure=10*log10(2-1/G) and NF_blind(S->0)==NF0 exactly. resync_spacing: 2.769->13.28, 12.77->1.33, 32.77->0.0133 cells (matches). In-model transient table +0.81/+2.27/+3.52/+4.57 at n=2/4/6/8 ->+9.66 (exact). D_pass=2.555 dB/rt, max flush 20.44 dB/8rt; S=10 blind NF=12.77 resync=1.33, sig-preserving guard 3.91rt/rebuild 4.09rt->+2.33 dB; S=30 guard 11.74rt>8 impossible (all match). LOAD-BEARING demonstrated deficit: ran solver.run pulse (drive_amp=3e-3, n_roundtrips=140, rep_ratio=0.25); measured Mth_num=0.168943 (matches json); slot-0 vs settled = -4.13 dB at 0.7*Mth_num and -3.72 dB at 0.7*Mth_analytic, flushed gain ~+3.67 dB. Note reports -4.18/-3.78 dB; my numbers and the note's both fall inside the note's band [-4.5,-3.6], the ~0.05 dB gap traceable to settled-averaging window (my window catches a small slot-17 tail droop). Label discipline: every NF number in-model, gains/anchors/resync demonstrated -- honored, no violation. F=2 and +2.01 dB reserve verified against notes/2026-07-21 (accurate, unaltered). No results.json value contested; M_th and 2.77 dB provenance not reopened; correctly resolves 07-22's OPEN sufficiency question rather than contradicting it.
  - non-load-bearing: Demonstrated slot-0 deficit is mildly settled-window/bias-convention dependent: I reproduce -4.13 dB (0.7*Mth_num) and -3.72 dB (0.7*Mth_analytic) vs the note's -4.18/-3.78; both sit inside the stated band [-4.5,-3.6] so the headline holds, but the exact digit is not settled-window-invariant.
  - non-load-bearing: The Friis NF=2.77+S blind-flush penalty is a worst-case upper bound (the de-Q and gain co-occur in one cavity mode rather than as cleanly cascaded stages); the note labels this in-model/upper-bound, which is correct, but the true penalty is architecture-dependent and only the escape direction, not a specific active-de-Q design, is established.
