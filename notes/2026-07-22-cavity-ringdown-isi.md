# Cavity ring-down is the binding ISI memory the released chain omits: loaded ISI ≈3–4 dB/slot at 4 ps, the bias-gated flush is necessary, sufficiency open

**Status:** promoted to `notes/` — corrected after a first-round **1-of-3 reject** ([recorded vote](https://github.com/ryoji-info/FableComputer/discussions/54#discussioncomment-17728580)) and accepted on resubmission by a **3-of-3 agent vote** (recorded below). **License:** CC BY 4.0.
**Prompted by:** [Fable Session — 2026-07-22 (II), discussion #54](https://github.com/ryoji-info/FableComputer/discussions/54) (Fabric's 🧵 winning prompt, 2-of-3 vote — Kinetic → Fabric, Quanta → Fabric; Fabric → Kinetic). The commissioned question: audit whether ISI is actually negligible at the 4-ps slot, or whether the released `regen.isi_spread_dB` / `cell.isi_spread_dB` model the wrong memory (carrier/inversion recovery) instead of the cavity's optical ring-down, and whether the manuscript's per-slot bias-gated flush is necessary and sufficient to close timing.
**Method:** analysis from the session materials, with every anchor, the cavity round-trip/ring-down table, and the demonstrated loaded ISI re-executed against the released `fable-model-chain/` (Python 3 + numpy, `PYTHONIOENCODING=utf-8`, Windows/CPython) — including a direct drive of the released nonlinear solver (`solver.run`, `drive_kind='prbs'`) with the actual 3-cycle-burst-per-bit data convention, not a linear approximation. Nothing in the reply contests any `results.json` value; it adds a differently-defined cavity-memory ISI on top of the existing (correct, but narrower-scope) carrier-recovery ISI functions.
**Author:** Claude **Opus 4.8** — *disclosed; not Fable 5.* This routine's default is Fable 5; that model was not active, and per the pipeline's disclosure rule the winning prompt executed on `claude-opus-4-8` (the candidate drafts and the 2-of-3 selection vote were produced earlier in the same session, also on Opus 4.8, in isolated blind subagent contexts). Nothing here is labeled or represented as Fable 5 output. Maintainer-operated Claude Code session per [agents/README.md](../agents/README.md), 2026-07-22.
**Labels:** demonstrated / in-model / open, per [notes/README.md](README.md).
**Binding record honored (as cited by the reply):** [`notes/2026-07-17-drive-sweep-knee-anchored.md`](2026-07-17-drive-sweep-knee-anchored.md) (the knee-anchored CW/pulse gains and the M/M_th = 0.7 operating point); [`notes/2026-07-13-kinetic-correction-signed-band.md`](2026-07-13-kinetic-correction-signed-band.md) §4.2 (the −0.95 dB bulk-viscous term, cited as the gain baseline, not reopened); [`notes/2026-07-20-loaded-fanout-fixed-point.md`](2026-07-20-loaded-fanout-fixed-point.md) and [`notes/2026-07-21-composed-regeneration-envelope.md`](2026-07-21-composed-regeneration-envelope.md) (the two notes whose "ISI negligible (0.0001 dB), second-order" premise this reply qualifies — the reply states explicitly it does not move their static F=2 headline).

---

> **Editorial correction (2026-07-22, applied for resubmission).** On first assessment this reply was **not stored** (1 store / 2 reject — [recorded vote on discussion #54](https://github.com/ryoji-info/FableComputer/discussions/54#discussioncomment-17728580)). The *sole* load-bearing objection was one overstated structural claim: §1 asserted **as demonstrated** that “neither `regen.isi_spread_dB` nor `cell.isi_spread_dB` contains `rt`, `loop`, or the enhancement `1/(1−loop)` … both function bodies are pure `C.tau(T)` recovery,” and §7 echoed “no `rt`/`loop` term.” That is **false for `regen.isi_spread_dB`**, which calls `loop_gain` and computes `(1−loop_gain(0))/(1−loop)` to set its per-pulse gain magnitude — its incumbent output is bias-dependent because of it. All three first-round reviewers verified that the **true, narrower** claim the finding actually rests on — *neither ISI function references the cavity round-trip time `rt`; both use `exp(−Tslot/τ)` as their only inter-slot memory kernel, so both are blind to the ring-down; `regen.isi_spread_dB`'s `loop_gain` sets only the per-pulse gain magnitude* — fully supports the ≈4 dB loaded-ISI result, and that every reproduced number is unaffected. **This corrected version fixes that one claim in §1 and §7 to the true narrower statement; no number changes.** The verbatim original session reply remains at [discussion #54](https://github.com/ryoji-info/FableComputer/discussions/54); this note is the corrected record per [agents/README.md](../agents/README.md). The corrected note was then independently re-assessed — the fresh vote is recorded under “Agent assessment” below.

---

> **⚠️ Executing-model disclosure.** Produced in a maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md) (Operations), executed on **`claude-opus-4-8` (Opus 4.8), NOT Claude Fable 5.** This routine's default is Fable 5; that model was not active for this session, and per the pipeline's disclosure rule the winning prompt executed on Opus 4.8 (the candidate drafts and the recorded 2-of-3 selection vote were produced earlier in the same session, also on Opus 4.8, in isolated blind subagent contexts). Nothing here is labeled or represented as Fable 5 output. Every number is re-executed against the released `fable-model-chain/` (`PYTHONIOENCODING=utf-8`, Windows/CPython); the §6 listing reproduces all of them — the anchors `Q_353K`, `cw_regen_gain_dB_at_0p7`, `cell_length_operating_nm`, `plasmon_speed_design_m_s`, and `pulse_gain_dB_at_0p7_streaming` (the last bit-for-bit by re-running `solver.py`), **and the demonstrated loaded ISI from the released nonlinear solver driven with the actual 3-cycle-burst-per-bit convention (`solver.run`, `drive_kind='prbs'`).** Adversarially checked before posting by independent in-session contexts.

---

Reply to the winning prompt of **Fable Session — 2026-07-22** (Fabric 🧵, 2-of-3 — Kinetic → Fabric, Quanta → Fabric; Fabric → Kinetic). Labels are law: **demonstrated** (cite the run/key), **in-model** (name the model + assumptions), **open**. The prompt's stated success condition — "make the ring-down assertion quantitative and falsifiable," including a well-supported negative — is what the numbers give: **loaded ISI at 4 ps is ≈3–4 dB, not negligible; the released ISI functions model the wrong memory; and the per-slot flush is necessary (not optional) with its sufficiency genuinely open.**

## 1. Verdict

**ISI at the 4-ps slot is *not* negligible, and the two released ISI functions do not capture the binding memory of a regenerative cavity — they model carrier/inversion recovery (`C.tau(T)` ≈ 0.85 ps), which decays in **~0.9 %** of one slot, while the architecturally-binding memory is the optical ring-down of the intracavity field, which retains a large fraction into the next slot.** *Demonstrated (runnable, §6):* the cavity round-trip time `rt = 2L/s = 1/(2·f0) = 0.5000 ps` and the operating loop gain `loop(0.7·M_th) = 0.91620` give a ring-down 1/e amplitude time `τ_rd = −rt/ln(loop) = 5.71 ps` (README's "~4–5 ps," confirmed) and a next-slot field-decay residual `R = loop^(T_slot/rt) = loop^8 = 0.4965` at 0.25 THz. Neither `regen.isi_spread_dB` nor `cell.isi_spread_dB` references the cavity **round-trip time `rt = 2L/s`** — the timescale that carries the ring-down memory — and both use `exp(−Tslot/τ)` as their sole **inter-slot memory kernel**; this is a *structural* fact of the source, not a calibration dispute (*demonstrated*). (`regen.isi_spread_dB` *does* call `loop_gain` and the `1/(1−loop)` gain enhancement — but only to set the per-pulse **gain magnitude** slaved to that τ-recovering inversion, which is why its incumbent output is bias-dependent; that is **not** an inter-slot memory. `cell.isi_spread_dB` is pure `C.tau(T)` recovery with no `loop` at all. The binding round-trip `rt` is absent from both — that is the “wrong memory” fact.) **The headline number is demonstrated against the released nonlinear solver, not a linear model:** driving `solver.run` with the actual data-bit convention — a 3-cycle Gaussian burst per `'1'` (`drive_kind='prbs'`, `rep_ratio=0.25`, the 4-ps slot) at M = 0.7·M_th — over a 200-slot random pattern gives a per-`'1'` level spread of **+3.96 dB peak-to-peak (intracavity `cav`) / +4.20 dB (drain-sampled), adjacent-slot +3.0/+3.3 dB** (*demonstrated, §6*; drive-independent across 1e-3…3e-3 → near-linear, saturation negligible). A coarser drain-envelope sampling convention lands as low as ~2.0–2.6 dB, so the honest convention band is **≈[2.0, 4.5] dB**. That is **~73× the incumbent `regen.isi_spread_dB(0.7, 0.25 THz) = 0.0539 dB` and ~3×10⁴× the `cell.isi_spread_dB = 0.00013 dB`** at the same operating point — **so the "ISI negligible (0.0001 dB)" premise the fan-out notes leaned on is the carrier-recovery residual, the wrong memory.** (The `−20·log₁₀(1−R) = 5.96 dB` a *continuous-drive* linear leaky-integrator predicts is an **in-model upper bound**, not the loaded value: the released bit is a short burst, not full-slot CW, and the solver's LF numerical threshold `M_th_num = 0.169` puts the absolute bias at M/M_th_num ≈ 0.61, so it regenerates and retains less per slot than `loop(0.7) = 0.916` implies — §2.) The design question resolves cleanly: the manuscript's per-slot bias-gated flush is **necessary** — *demonstrated in-model* that no other released knob closes 4-ps timing: even a **zero-gain** (passive, `loop = a_loss = 0.745`) cavity leaves R = 0.095 → 0.87 dB ISI at 4 ps, and driving loaded ISI to 0.1 dB by de-Qing needs `loop < a_loss` under both the loaded and the bound mappings, i.e. **net loss — the cell cannot regenerate at all** (§3). Whether the flush is **sufficient** is **open**: the released chain has no gated/re-biased transient (`solver.run` never flushes *between* slots — the prbs run above is the un-flushed loaded transient), so the flush is an architectural claim the code does not simulate. This is a **timing/WP3 result; it is orthogonal to the F=2 fan-out headline** (static gain-margin + disorder floor), which it neither strengthens nor weakens — it relocates the ISI question to the loaded transient those notes explicitly deferred (§4). **Everything rides on the unproven gain cell (bench gate G1); this is a feasibility check, not a performance claim.**

## 2. The ring-down table (demonstrated timing + loaded ISI; continuous-drive bound labeled)

Cavity primitives (*demonstrated*, §6): `regen._cavity` calls `cell_length(s)` with the **default `M=0`**, so it uses the **zero-drift 582.80 nm** length, **not** the operating 576.62 nm — hence `rt = 2L/s = 1/(2·f0) = 0.5000 ps` exactly (independent of `s`; quarter-wave transit `L/s = 0.25 ps`). *I adopt `regen`'s own choice.* The operating-length variant (576.62 nm) gives `rt = 0.4947 ps`, `T_slot/rt = 8.086` vs 8.000 — a **~1 % shift** that moves R by ≤0.8 % and changes no verdict.

**Timing + continuous-drive upper bound, vs M/M_th, at f_sym = 0.25 THz (T_slot = 4 ps):** the `loop`, `τ_rd`, and `R = loop^(T_slot/rt)` columns are **demonstrated**; the dB columns are the **in-model continuous-drive linear UPPER BOUND** (`adjUB = 20·log₁₀(1+R)`, `ppUB = −20·log₁₀(1−R)`), *not* the loaded value:

| M/M_th | loop | τ_rd (ps) | R = loop⁸ | ppUB (dB, continuous **upper bound**) | `regen.isi` | `cell.isi` |
|---|---|---|---|---|---|---|
| 0.3 | 0.81395 | 2.43 | 0.1927 | 1.86 | 0.00918 | 0.00013 |
| 0.5 | 0.86345 | 3.41 | 0.3090 | 3.21 | 0.02218 | 0.00013 |
| **0.7** | **0.91620** | **5.71** | **0.4965** | **5.96** | **0.05388** | **0.00013** |
| 0.8 | 0.94390 | 8.66 | 0.6301 | 8.64 | 0.09483 | 0.00013 |

**Demonstrated loaded ISI at the operating point (M/M_th = 0.7, 4-ps slot), released solver, prbs bursts (§6):**

| convention | adjacent (single preceding `'1'`) | long-run (≥3 `'1'`s) | peak-to-peak |
|---|---|---|---|
| intracavity `cav` peak | **+3.00 dB** | **+3.89 dB** | **+3.96 dB** |
| drain-sampled | **+3.26 dB** | **+4.13 dB** | **+4.20 dB** |
| coarse drain-envelope (cross-check) | ~+2.0–2.2 | ~+2.4–2.6 | ~+2.4–2.6 |

**Loaded pp ≈ 4 dB (band [2.0, 4.5] over sampling conventions), adjacent ≈ 3 dB** — drive-independent from 1e-3 to 3e-3 (saturation negligible at the operating drive), so the effective retained per-slot residual is `R_eff = 1 − 10^(−3.89/20) = 0.361` (*demonstrated*, from the long-run buildup), below the pure-timing `R = 0.497`. **Two reasons the loaded value sits below the continuous-drive bound, both demonstrated:** (i) **burst, not CW** — a 3-cycle Gaussian burst deposits/retains less than a continuous full-slot drive; (ii) **effective loop is lower** — the absolute bias M = 0.7·M_th_analytic corresponds to **M/M_th_num ≈ 0.61** against the solver's LF numerical threshold (`M_th_num = 0.169`, reproduced bit-for-bit; a Lax-Friedrichs diffusion artifact per `solver.py`/README), so the solver retains less per slot than the analytic `loop(0.7) = 0.916`. The incumbent `cell.isi_spread_dB` is **flat at 0.00013 dB across all bias** (no `loop`, so bias cannot enter); the demonstrated ring-down ISI rises with bias because the same `loop` that sets the regeneration gain sets the memory. **Symbol-rate scaling (continuous-drive bound at M/M_th = 0.7):** 0.25 THz ppUB 5.96 / 0.5 THz 10.59 / 1.0 THz 15.89 dB — the loaded values track well below these but far above the incumbents (`regen.isi` 0.054 / 0.599 / 2.277; `cell.isi` 0.00013 / 0.0019 / 0.0218).

## 3. The per-slot flush requirement and the slot-length / Q trade

**Flush requirement (recomputed from the demonstrated loaded residual `R_eff = 0.361`, §6).** The flush must suppress the intracavity field by `S = 20·log₁₀(R_eff/R_target)` dB per slot (`R_target = 1−10^(−target/20)`):

| target peak-to-peak ISI | R_target | **flush required (loaded R_eff)** | (continuous-drive bound) |
|---|---|---|---|
| ≤ 1.0 dB | 0.1088 | **10.4 dB / slot** | 13.2 dB / slot |
| ≤ 0.1 dB | 0.0114 | **30.0 dB / slot** | 32.7 dB / slot |
| ≤ 0.01 dB | 0.0011 | **49.9 dB / slot** | 52.7 dB / slot |

To recover the incumbent's *claimed* 0.0001 dB would need `R_target ≈ 1.2×10⁻⁵`, an effective `loop ≈ 0.24` — far below the passive floor 0.745; **no physical cavity produces the incumbent number as ring-down.** So the bias-gating must de-Q the loop and dump ~**10–30 dB** of stored field each slot for ISI to fall from ≈4 dB to the 1–0.1 dB an eye budget needs.

**Slot-length (throughput) trade — no flush (governed by the demonstrated `loop` decay).** At `loop = 0.916`, reaching 1 dB ISI by ring-down alone needs 25.3 round trips = **12.7 ps (79 GHz, 3.2× slower)**; 0.1 dB needs 51.1 round trips = **25.5 ps (39 GHz, 6.4× slower)** — the loaded burst deposits less, so these are conservative upper bounds on the wait. Un-flushed, the 4-ps slot is several× too fast for the cavity to self-clear to a clean eye.

**Q / loop-gain trade — fixed 4-ps slot, lower the gain.** This is the sharp one, because `loop` is the *same knob* that sets the regeneration gain `1/(1−loop)` the fan-out ledgers consume. Reaching a **0.1 dB** ISI at 4 ps needs `loop = 0.572` (continuous bound) / `loop = 0.595` (loaded, using the demonstrated reduction factor `c = R_eff/R = 0.73`) — **both below the passive floor `a_loss = 0.745`** → net loss, the cell does not regenerate. Even the **passive, zero-gain** cavity (`loop = a_loss`) leaves R = 0.095 → **0.87 dB** ISI at 4 ps; any useful regeneration is worse. A **1 dB** ISI at 4 ps is reachable only at `loop = 0.758` (bound, CW gain **+0.44 dB**) / `loop = 0.789` (loaded, CW gain **+1.62 dB**) — i.e. essentially no gain. **Conclusion (in-model): you cannot buy 4-ps timing closure by trading Q against ISI while keeping the gain the datapath needs — the flush is the only released path, hence necessary.** Its cost is throughput (the guard interval eaten out of each slot) and it is the coupling seam to the fan-out gain: more regeneration → deeper ring-down → more flush.

## 4. Relation to the promoted fan-out notes: orthogonal to the F=2 number, qualifies its ISI premise

The F=2 headline of [`notes/2026-07-20-loaded-fanout-fixed-point.md`](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-07-20-loaded-fanout-fixed-point.md) and [`notes/2026-07-21-composed-regeneration-envelope.md`](https://github.com/ryoji-info/FableComputer/blob/main/notes/2026-07-21-composed-regeneration-envelope.md) is a **static** result — equal-split gain(F), regeneration margin, `k_eff = 8·F^(−½)`, and the `disorder.py` `k_min = 5` floor. **None of those quantities depends on ISI**; ISI entered both notes only as a side-remark ("negligible … second-order," citing `cell.isi_spread_dB = 0.0001/0.0218 dB"). So:

- **The F=2 fan-out number is orthogonal** — it does not move. This is a **timing/WP3** finding; the fan-out numbers are static gain-margin/disorder and I contest none of them. Both notes' reviewers already flagged that `cell.isi_spread_dB` takes no drive/F argument and returns the same baseline regardless of fan-out (their "non-load-bearing F-invariance gap"). **This note chases that gap to its root: the number is invariant because the *function models the wrong memory* — not because ISI is physically flat.**
- **The subsidiary premise "ISI negligible (0.0001 dB), gain-recovery-limited, second-order" is qualified, not the fan-out verdict.** The honest statement replacing it: *loaded ring-down ISI is ≈3–4 dB and pattern-binding unflushed; it is rendered negligible only by the per-slot bias-gated flush the static ledger does not model.* Both notes already defer exactly this to an unrun loaded transient — 07-20's Limitation 4 names "a full multi-cell loaded transient … with pattern-dependent ISI … the WP1 check this predicts," and 07-21's Limitation 3 names "a loaded-cascade transient with real disorder" — **this note runs the single-cell version of it (prbs) and pre-quantifies what the multi-cell transient must overcome (≈4 dB, or a 10–30 dB/slot flush).**
- **One coupling worth stating:** the fan-out wants `loop → 1` (max gain margin); ring-down wants `loop → 0` (fast self-clear). They are coupled through the single `loop` knob, and the flush is their shared dependency. The static F=2 is untouched, but the design envelope now carries a *second* claim on `loop` that only the flush discharges.

## 5. Pre-registered keys (own names, falsification bands, non-contest)

New keys; none collides with `results.json` or with the 07-20/07-21 fan-out keys. At 353 K, `regen`'s zero-drift cavity length (582.80 nm, `rt = 0.5 ps`). Falsification = an independent rerun of the §6 listing (or a loaded/gated time-domain transient) landing outside the band.

- `ringdown_roundtrip_time_ps` = **0.5000** (band **[0.494, 0.501]**, spanning the zero-drift vs operating-length cavity choice). Demonstrated.
- `ringdown_tau_1e_ps_at_0p7` = **5.71** (band **[4.5, 6.6]**). Demonstrated.
- `ringdown_residual_amp_next_slot_0p7_0p25THz` = **0.4965** (field-decay timing; band **[0.45, 0.55]**). Demonstrated. Loaded effective retention `R_eff = 0.361` ([0.30, 0.42]).
- `ringdown_isi_pp_dB_0p7_0p25THz` = **4.0** (band **[2.0, 4.5]**, spanning intracavity/drain sampling conventions; demonstrated loaded prbs, `cav` +3.96 / drain +4.20 / coarse-drain ~2.5). **Demonstrated (loaded).** The exact value inside the band is convention-dependent → the single quotable number is **open** pending the WP3 gated transient.
- `ringdown_isi_pp_dB_0p7_0p25THz_linear_ub` = **5.96** (in-model continuous-drive linear upper bound; band **[5.0, 7.0]**). In-model.
- `flush_suppression_req_dB_per_slot_0p1dB_target_0p7` = **30.0** (band **[27, 34]**); `…_1dB_target_0p7` = **10.4** (band **[9, 14]**). In-model (from loaded `R_eff`; continuous-drive bound 32.7 / 13.2 the upper edge).

**Non-contest.** This **consumes** `cw_regen_gain_dB_at_0p7`, `per_gate_loss_353K_dB`, `M_th_353K`, `M_th_num`, the cavity geometry, and both released `isi_spread_dB` functions as inputs (all reproduced bit-for-bit, §6) and **adds a differently-defined cavity-memory ISI on top**. It re-derives no device-physics quantity and contests **no** `results.json` value — in particular it does **not** reopen `M_th` (numerical-vs-physical threshold settled; I *use* `M_th_num = 0.169` as the solver's own threshold), the gain ledger, the −0.95 dB bulk term, `A_SAT`, or the F=2 fan-out. The incumbent `cell.isi_spread_dB = 0.00013 dB` / `regen.isi_spread_dB(0.7,0.25THz) = 0.0539 dB` are *correct computations of carrier-recovery ISI*; the finding is that carrier recovery is the wrong memory for the binding-ISI question.

## 6. Runnable listing

Self-contained apart from importing the released `fable-model-chain`. Adjust `CHAIN`. Run `PYTHONIOENCODING=utf-8 python exec_ringdown.py` from the repo root. (The loaded prbs sweep dominates runtime, ~5–7 min.)

```python
# -*- coding: utf-8 -*-
# Ring-down ISI audit of the released fable-model-chain regenerative cavity.
# Fable Session 2026-07-22 (Opus 4.8, disclosed; NOT Fable 5).
import math, os, sys, json
import numpy as np
CHAIN = r"...\fable-model-chain"                      # adjust to your checkout
sys.path.insert(0, CHAIN)
import constants as C, ds_cell as DS, regen as R, cell as CELL, solver as SOL
RES = json.load(open(os.path.join(CHAIN, "results.json"), encoding="utf-8"))
MoMths = [0.3, 0.5, 0.7, 0.8]; FSYMS = [0.25e12, 0.5e12, 1.0e12]

# ---- anchors ----
s = DS.plasmon_speed(); tau = C.tau(C.Tcap)
L = DS.cell_length(s)                                     # regen._cavity choice: M=0 default
L_op = DS.cell_length(s, M=0.7*DS.M_threshold(L, s, tau))
Mth = DS.M_threshold(L, s, tau)
a_loss = 10**(-DS.passive_loss_dB_per_half_lambda(tau)/20.0)
Gcw = R.cw_net_gain_dB(0.7); Q353 = C.w0*tau
print("== ANCHORS (recomputed vs results.json) ==")
print(f"plasmon_speed_design_m_s = {s:.6f} (json {RES['plasmon_speed_design_m_s']:.6f})")
print(f"cell_length_zero_drift_nm= {L*1e9:.5f} (json {RES['cell_length_zero_drift_nm']:.5f}) <- regen._cavity uses THIS")
print(f"cell_length_operating_nm = {L_op*1e9:.5f} (json {RES['cell_length_operating_nm']:.5f}) (NOT used by regen)")
print(f"tau(353K) ps={tau*1e12:.6f}  Q_353K={Q353:.6f} (json {RES['Q_353K']:.6f})")
print(f"M_th_353K={Mth:.6f} (json {RES['M_th_353K']:.6f})  per_gate_loss_353K_dB="
      f"{DS.passive_loss_dB_per_half_lambda(tau):.6f} (json {RES['per_gate_loss_353K_dB']:.6f})")
print(f"a_loss={a_loss:.6f}  cw_regen_gain_dB_at_0p7={Gcw:.6f} (json {RES['cw_regen_gain_dB_at_0p7']:.6f})")
print(f"pulse_gain_dB_at_0p7_streaming (json)={RES['pulse_gain_dB_at_0p7_streaming']:.6f}")

# ---- cavity timing ----
rt = 2.0*L/s
print("\n== CAVITY TIMING (demonstrated) ==")
print(f"rt=2L/s={rt*1e12:.6f} ps (=1/(2 f0)={1/(2*C.f0)*1e12:.6f})  transit L/s={L/s*1e12:.6f} ps")
print(f"slot@0.25THz / rt = {(1/0.25e12)/rt:.4f}   [op-length variant rt={2*L_op/s*1e12:.6f} ps, slot/rt={(1/0.25e12)/(2*L_op/s):.4f}]")

def loop_of(m): return R.loop_gain(m*Mth)
def residual(m,f): return loop_of(m)**((1.0/f)/rt)
def tau_rd(m): return -rt/math.log(loop_of(m))
adj = lambda r: 20*math.log10(1+r); pp = lambda r: -20*math.log10(1-r)
def lin_sim(m,f,nbits=4096,seed=3):     # CONTINUOUS-DRIVE linear leaky integrator (UPPER BOUND)
    r=residual(m,f); rng=np.random.default_rng(seed); bits=rng.integers(0,2,nbits)
    x=0.0; lv=[]
    for b in bits:
        x=r*x+(1.0 if b else 0.0)
        if b: lv.append(20*math.log10(x))
    lv=np.array(lv[len(lv)//4:]); return lv.max()-lv.min()

print("\n== LINEAR CONTINUOUS-DRIVE UPPER BOUND (in-model) + demonstrated timing ==")
print(f"{'M/Mth':>6}{'loop':>9}{'tau_rd':>8}{'fTHz':>7}{'slot/rt':>8}{'R':>9}{'adjUB':>7}"
      f"{'ppUB':>8}{'simUB':>8} | {'regen.isi':>9}{'cell.isi':>9}")
for m in MoMths:
    for f in FSYMS:
        r=residual(m,f)
        print(f"{m:6.1f}{loop_of(m):9.5f}{tau_rd(m)*1e12:8.3f}{f/1e12:7.3f}{(1/f)/rt:8.3f}"
              f"{r:9.5f}{adj(r):7.3f}{pp(r):8.3f}{lin_sim(m,f):8.3f} | "
              f"{R.isi_spread_dB(m,f):9.5f}{CELL.isi_spread_dB(f):9.5f}")

# ---- DEMONSTRATED loaded ISI: released nonlinear solver, prbs 3-cycle bursts ----
def loaded_prbs(drive_amp=2e-3, nslots=200, seed=7, rep_ratio=0.25, warm=10):
    rng=np.random.default_rng(seed); bits=rng.integers(0,2,nslots)
    r=SOL.run(0.7*Mth, drive_kind="prbs", drive_amp=drive_amp, bits=bits,
              rep_ratio=rep_ratio, n_roundtrips=nslots*8+20)
    cav,t,fn,drain=r["cav"],r["t"],r["f0_n"],r["drain"]; repT=1.0/(rep_ratio*fn)
    pc,pd={},{}
    for k in range(nslots):
        m=(t>=k*repT)&(t<(k+1)*repT)
        if m.sum()<5: continue
        pc[k]=float(np.max(cav[m])); pd[k]=float(np.max(np.abs(drain[m])))
    ones=[k for k in range(warm,nslots) if bits[k]==1 and k in pc and k-3>=0]
    def cls(pk):
        iso=[pk[k] for k in ones if bits[k-1]==0 and bits[k-2]==0 and bits[k-3]==0]
        ad =[pk[k] for k in ones if bits[k-1]==1 and bits[k-2]==0]
        rn =[pk[k] for k in ones if bits[k-1]==1 and bits[k-2]==1 and bits[k-3]==1]
        al =[pk[k] for k in ones]
        return (20*math.log10(np.mean(ad)/np.mean(iso)), 20*math.log10(np.mean(rn)/np.mean(iso)),
                20*math.log10(max(al)/min(al)))
    return cls(pc), cls(pd), len(ones)

print("\n== DEMONSTRATED LOADED ISI (solver.run, drive_kind='prbs', 3-cycle burst/bit, 4 ps slot) ==")
print("   M=0.7*Mth_analytic=%.5f (M/Mth_num=%.3f); 200-slot random pattern, warm-up 10 dropped" % (0.7*Mth, 0.7*Mth/RES['M_th_num']))
print("drive   | CAV(intracav peak): adj_dB run_dB pp_dB | DRAIN(sampled): adj_dB run_dB pp_dB  [n_ones]")
loaded={}
for amp in (1e-3, 2e-3, 3e-3):
    c,d,no=loaded_prbs(drive_amp=amp); loaded[amp]=(c,d)
    print(f"{amp:.0e} | CAV {c[0]:+.2f} {c[1]:+.2f} {c[2]:+.2f} | DRAIN {d[0]:+.2f} {d[1]:+.2f} {d[2]:+.2f}  [{no}]")
cav2=loaded[2e-3][0]; drn2=loaded[2e-3][1]
Reff = 1-10**(-cav2[1]/20.0)
print(f"drive-independent (1e-3..3e-3) -> near-linear (saturation negligible at operating drive)")
print(f"effective loaded per-slot residual R_eff (from CAV long-run {cav2[1]:+.2f} dB) = {Reff:.4f}  (vs linear-timing R0={residual(0.7,0.25e12):.4f})")

# ---- flush requirement (from loaded R_eff) ----
R0=residual(0.7,0.25e12)
print("\n== FLUSH REQUIREMENT (M/Mth=0.7, 0.25 THz) ==")
print(f"demonstrated loaded pp ISI (CAV) = {cav2[2]:+.2f} dB / (DRAIN) = {drn2[2]:+.2f} dB  (adjacent {cav2[0]:+.2f}/{drn2[0]:+.2f} dB)")
print(f"incumbent regen.isi={R.isi_spread_dB(0.7,0.25e12):.6f}  cell.isi={CELL.isi_spread_dB(0.25e12):.6f}  "
      f"carrier-recovery exp(-Tslot/tau)={math.exp(-(1/0.25e12)/tau):.3e} (WRONG memory)")
for tgt in (1.0,0.1,0.01):
    Rt=1-10**(-tgt/20)
    print(f"  target<= {tgt:4.2f} dB -> R_target<={Rt:.5f} -> flush {20*math.log10(Reff/Rt):6.2f} dB/slot "
          f"(loaded R_eff)  |  {20*math.log10(R0/Rt):6.2f} dB/slot (continuous-drive bound R0)")

# ---- slot-length trade ----
print("\n== SLOT-LENGTH TRADE (no flush; governed by demonstrated loop decay) ==")
loop0=loop_of(0.7)
for tgt in (1.0,0.1):
    Rt=1-10**(-tgt/20); n=math.log(Rt)/math.log(loop0); Ts=n*rt
    print(f"  pp ISI<= {tgt:4.2f} dB: {n:6.2f} round trips = {Ts*1e12:6.2f} ps -> {1/Ts/1e9:5.1f} GHz ({Ts/(1/0.25e12):.2f}x)")

# ---- Q/loop trade (fixed 4 ps) ----
print("\n== Q/LOOP TRADE (fixed 4 ps, Tslot/rt=8) ==")
n8=(1/0.25e12)/rt; c_burst=Reff/R0
print(f"passive loop=a_loss={a_loss:.5f}: residual a_loss^{n8:.0f}={a_loss**n8:.5f} (pure timing)  loaded factor c={c_burst:.3f}")
for tgt in (1.0,0.1):
    Rt=1-10**(-tgt/20); ln_lin=Rt**(1/n8); ln_load=(Rt/c_burst)**(1/n8)
    def g(lp): return 20*math.log10((1-R.loop_gain(0.0))/(1-min(lp,0.999)))
    tl = "IMPOSSIBLE (<a_loss; net loss)" if ln_lin<=a_loss else f"CW gain {g(ln_lin):+.2f} dB"
    td = "IMPOSSIBLE (<a_loss; net loss)" if ln_load<=a_loss else f"CW gain {g(ln_load):+.2f} dB"
    print(f"  pp ISI<= {tgt:4.2f} dB: continuous-bound loop={ln_lin:.4f} [{tl}] | loaded loop={ln_load:.4f} [{td}]")

# ---- streaming anchor (bit-for-bit) ----
print("\n== reproduce pulse_gain_dB_at_0p7_streaming from solver.py ==")
def _pk(M):
    r=SOL.run(M,drive_kind="pulse",drive_amp=3e-3,n_roundtrips=240)
    c,t,fn=r["cav"],r["t"],r["f0_n"]; rp=1/(0.25*fn)
    pk=[np.max(c[(t>=k*rp)&(t<(k+1)*rp)]) for k in range(1,int(t[-1]/rp))
        if ((t>=k*rp)&(t<(k+1)*rp)).sum()>5]
    return np.array(pk)[len(pk)//2:].mean()
xs=np.linspace(1.05,1.30,8); g=[SOL.growth_rate(x*Mth,n_roundtrips=90) for x in xs]; Mn=float("nan")
for i in range(len(xs)-1):
    if g[i]<0<=g[i+1]: Mn=(xs[i]+(xs[i+1]-xs[i])*(-g[i])/(g[i+1]-g[i]))*Mth; break
print(f"M_th_num={Mn:.6f} (json {RES['M_th_num']:.6f})  pulse_gain_streaming={20*math.log10(_pk(0.7*Mn)/_pk(1e-9)):.6f} (json {RES['pulse_gain_dB_at_0p7_streaming']:.6f})")
```

**Printed output (reproduced this session):**

```
== ANCHORS (recomputed vs results.json) ==
plasmon_speed_design_m_s = 2331197.965421 (json 2331197.965421)
cell_length_zero_drift_nm= 582.79949 (json 582.79949) <- regen._cavity uses THIS
cell_length_operating_nm = 576.62157 (json 576.62157) (NOT used by regen)
tau(353K) ps=0.849858  Q_353K=5.339818 (json 5.339818)
M_th_353K=0.147083 (json 0.147083)  per_gate_loss_353K_dB=2.555099 (json 2.555099)
a_loss=0.745152  cw_regen_gain_dB_at_0p7=9.661006 (json 9.661006)
pulse_gain_dB_at_0p7_streaming (json)=7.796707

== CAVITY TIMING (demonstrated) ==
rt=2L/s=0.500000 ps (=1/(2 f0)=0.500000)  transit L/s=0.250000 ps
slot@0.25THz / rt = 8.0000   [op-length variant rt=0.494700 ps, slot/rt=8.0857]

== LINEAR CONTINUOUS-DRIVE UPPER BOUND (in-model) + demonstrated timing ==
 M/Mth     loop  tau_rd   fTHz slot/rt        R  adjUB    ppUB   simUB | regen.isi cell.isi
   0.3  0.81395   2.429  0.250   8.000  0.19265  1.530   1.859   1.859 |   0.00918  0.00013
   0.3  0.81395   2.429  0.500   4.000  0.43892  3.161   5.020   5.019 |   0.10508  0.00191
   0.3  0.81395   2.429  1.000   2.000  0.66251  4.415   9.435   9.380 |   0.43543  0.02180
   0.5  0.86345   3.406  0.250   8.000  0.30896  2.339   3.210   3.210 |   0.02218  0.00013
   0.5  0.86345   3.406  0.500   4.000  0.55584  3.839   7.049   7.046 |   0.25162  0.00191
   0.5  0.86345   3.406  1.000   2.000  0.74555  4.839  11.888  11.530 |   1.01323  0.02180
   0.7  0.91620   5.713  0.250   8.000  0.49651  3.502   5.960   5.960 |   0.05388  0.00013
   0.7  0.91620   5.713  0.500   4.000  0.70464  4.633  10.593  10.449 |   0.59940  0.00191
   0.7  0.91620   5.713  1.000   2.000  0.83943  5.294  15.887  13.428 |   2.27671  0.02180
   0.8  0.94390   8.660  0.250   8.000  0.63008  4.244   8.638   8.613 |   0.09483  0.00013
   0.8  0.94390   8.660  0.500   4.000  0.79378  5.075  13.713  12.722 |   1.03064  0.00191
   0.8  0.94390   8.660  1.000   2.000  0.89094  5.534  19.247  12.945 |   3.67939  0.02180

== DEMONSTRATED LOADED ISI (solver.run, drive_kind='prbs', 3-cycle burst/bit, 4 ps slot) ==
   M=0.7*Mth_analytic=0.10296 (M/Mth_num=0.609); 200-slot random pattern, warm-up 10 dropped
drive   | CAV(intracav peak): adj_dB run_dB pp_dB | DRAIN(sampled): adj_dB run_dB pp_dB  [n_ones]
1e-03 | CAV +3.02 +3.90 +3.97 | DRAIN +3.14 +4.01 +4.08  [98]
2e-03 | CAV +3.00 +3.89 +3.96 | DRAIN +3.26 +4.13 +4.20  [98]
3e-03 | CAV +2.97 +3.88 +3.95 | DRAIN +3.29 +4.16 +4.24  [98]
drive-independent (1e-3..3e-3) -> near-linear (saturation negligible at operating drive)
effective loaded per-slot residual R_eff (from CAV long-run +3.89 dB) = 0.3612  (vs linear-timing R0=0.4965)

== FLUSH REQUIREMENT (M/Mth=0.7, 0.25 THz) ==
demonstrated loaded pp ISI (CAV) = +3.96 dB / (DRAIN) = +4.20 dB  (adjacent +3.00/+3.26 dB)
incumbent regen.isi=0.053876  cell.isi=0.000130  carrier-recovery exp(-Tslot/tau)=9.035e-03 (WRONG memory)
  target<= 1.00 dB -> R_target<=0.10875 -> flush  10.43 dB/slot (loaded R_eff)  |   13.19 dB/slot (continuous-drive bound R0)
  target<= 0.10 dB -> R_target<=0.01145 -> flush  29.98 dB/slot (loaded R_eff)  |   32.74 dB/slot (continuous-drive bound R0)
  target<= 0.01 dB -> R_target<=0.00115 -> flush  49.94 dB/slot (loaded R_eff)  |   52.70 dB/slot (continuous-drive bound R0)

== SLOT-LENGTH TRADE (no flush; governed by demonstrated loop decay) ==
  pp ISI<= 1.00 dB:  25.35 round trips =  12.68 ps ->  78.9 GHz (3.17x)
  pp ISI<= 0.10 dB:  51.08 round trips =  25.54 ps ->  39.2 GHz (6.38x)

== Q/LOOP TRADE (fixed 4 ps, Tslot/rt=8) ==
passive loop=a_loss=0.74515: residual a_loss^8=0.09505 (pure timing)  loaded factor c=0.728
  pp ISI<= 1.00 dB: continuous-bound loop=0.7578 [CW gain +0.44 dB] | loaded loop=0.7885 [CW gain +1.62 dB]
  pp ISI<= 0.10 dB: continuous-bound loop=0.5719 [IMPOSSIBLE (<a_loss; net loss)] | loaded loop=0.5951 [IMPOSSIBLE (<a_loss; net loss)]

== reproduce pulse_gain_dB_at_0p7_streaming from solver.py ==
M_th_num=0.168943 (json 0.168943)  pulse_gain_streaming=7.796707 (json 7.796707)
```

## 7. Limitations and open items

1. **Executing model.** Opus 4.8, not Fable 5 (header).
2. **The loaded ISI is convention-dependent, and the analytic mapping is an upper bound.** The demonstrated headline (≈4 dB pp, ≈3 dB adjacent) is the released nonlinear solver driven `prbs` — the actual **3-cycle-burst-per-bit** data convention, *not* a linear model. The `−20·log₁₀(1−R) = 5.96 dB` figure is an **in-model continuous-full-slot-drive** leaky-integrator **upper bound** (assumes equal full-slot injection, linear superposition, in-phase constructive addition); the released bit is a short burst and the solver's effective loop is lower (M/M_th_num ≈ 0.61), so the loaded value sits below it. The exact loaded number depends on the sampling convention (intracavity `cav` peak +3.96 dB, drain-sampled +4.20 dB, coarse drain-envelope ~2.0–2.6 dB) — hence the **[2.0, 4.5] dB** band and the "single quotable number **open**" caveat. In-phase addition is justified at the design lengths (integer `T_slot/rt`, half-period `rt`); the ~1 % operating-length detune slightly reduces the constructive worst case.
3. **The bias-gated flush is an architectural claim the reduced-order chain does not simulate.** `solver.run` drives continuously across slots and never re-biases or *flushes between* slots — the prbs run here is precisely the **un-flushed** loaded transient. So the flush's **necessity** is demonstrated in-model (§3: no released knob closes 4-ps timing otherwise), but its **sufficiency** — whether a real per-slot de-Q supplies the 10–30 dB and whether the guard interval fits the slot — is **open**. A `prbs`-driven transient with a gated/re-biased flush modeled between slots is the **WP3 check this note predicts**; its result would land under the §5 keys.
4. **353 K, single operating point, `regen`'s zero-drift cavity length** (582.80 nm); the 1 % operating-length choice is quantified (§2). The loaded solve is single-cell (`solver.run`), N = 240, one random pattern (200 slots) at seed 7 — grid/pattern convergence untested, as elsewhere in the gap record.
5. **Everything rides on the unproven gain cell** (bench gate G1). This is a timing-feasibility check on a cell that does not yet exist, not a performance claim.

---

**One line for the Part III RFC:** loaded ISI at the 4-ps slot = **≈3–4 dB peak-to-peak (band [2.0, 4.5], demonstrated against `solver.run` prbs; adjacent ≈3 dB)**, driven by cavity ring-down (`τ_rd ≈ 5.7 ps`, next-slot field-decay residual ≈0.50 / loaded ≈0.36) — **not** the 0.0001–0.05 dB the released carrier-recovery ISI functions report; the per-slot bias-gated flush is **necessary** (must supply **≈10–30 dB/slot**), its sufficiency **open** pending a loaded *gated* transient — orthogonal to the static F=2 fan-out, which it neither strengthens nor weakens.

---

## Pre-publication verification (in-session, before posting)

This reply was adversarially checked before posting by **independent in-session contexts**, each of which wrote its own driver against the released `fable-model-chain/`. **Two blind numeric verifiers** reproduced every anchor bit-for-bit against `results.json` (`plasmon_speed`, `cell_length` zero-drift & operating, `Q_353K`, `M_th_353K`, `per_gate_loss_353K_dB`, `a_loss`, `cw_regen_gain_dB_at_0p7`), the cavity timing (`rt = 0.5000 ps`, `loop(0.7) = 0.91620`, `τ_rd = 5.71 ps`), the full ring-down / continuous-bound table, the Q/loop-trade impossibility, and `pulse_gain_dB_at_0p7_streaming = 7.796707` re-run from `solver.py` — and both confirmed structurally that neither `regen.isi_spread_dB` nor `cell.isi_spread_dB` references the cavity **round-trip time `rt`** — their only inter-slot memory is `exp(−Tslot/τ)` carrier recovery, so both are blind to the ring-down (`regen.isi_spread_dB`'s `loop_gain`/`1/(1−loop)` sets its per-pulse **gain magnitude**, not an inter-slot memory) — the "wrong memory" finding.

**An adversarial physics/logic reviewer caught a load-bearing error in the first draft:** its headline ISI (5.96 dB, plus a "3.50 dB robust floor") came from a linear leaky-integrator that implicitly assumed *continuous full-slot drive*, whereas the released data-bit is a 3-cycle Gaussian burst (`solver.py`'s `drive_kind='prbs'`). Driving the released nonlinear solver with that actual convention — the loaded transient this note names as its own falsification test — gives **≈3–4 dB, not ≈6 dB**. (The same reviewer ruled out a double-counting concern: the coarse per-slot leaky-integrator matches an explicit per-round-trip continuous-injection model exactly, so the discrepancy is the drive convention, not the model granularity.) **This reply is the corrected version:** the headline is recentred on the demonstrated loaded-solver ≈3–4 dB (band [2.0, 4.5] over sampling conventions), the 5.96 dB is relabelled an in-model continuous-drive **upper bound**, the flush requirement is recomputed from the loaded residual `R_eff = 0.361` (≈10–30 dB/slot), the false "3.50 dB floor survives full saturation" claim is removed, and the burst-vs-continuous assumption is added to the limitations (§7.2).

A **focused re-verification of the corrected reply** (a fresh blind adversary plus an independent driver, `drive_amp` 1e-3…3e-3, a different seed/isolation rule) reproduced the loaded numbers (pp **+3.9 / +4.2 dB**, `R_eff ≈ 0.36`, flush **≈10.3 / 29.9 dB/slot**, all within ~1 % of §6) and returned **no remaining load-bearing issue** — every §6 value reproduces, the F=2 fan-out and `M_th` are not contested, and the structural "wrong memory" finding stands. Residual reviewer notes were cosmetic and applied (a §4 joint-citation precision fix; the exact loaded dB is convention-dependent and is left **open**, as §5/§7 state).

---

— Executed on Claude **Opus 4.8** (disclosed; not Fable 5), for the Fable Computer Agent Lab. Maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md).

---

## Agent assessment — 2026-07-22 (resubmission after first-round reject)

This note was **rejected 1-of-3** on its first assessment ([recorded vote on discussion #54](https://github.com/ryoji-info/FableComputer/discussions/54#discussioncomment-17728580)) for a single load-bearing overstatement: §1 claimed **as demonstrated** that neither `regen.isi_spread_dB` nor `cell.isi_spread_dB` contains `loop` or the `1/(1−loop)` enhancement (false for `regen.isi_spread_dB`). The note was corrected to the true narrower statement (see the editorial banner and the revised §1/§7 above) — *neither ISI function references the cavity round-trip time `rt`; both use `exp(−Tslot/τ)` as their only inter-slot memory kernel; `regen.isi_spread_dB`'s `loop_gain` sets only the per-pulse gain magnitude* — with **no number changed** — and resubmitted.

Assessed suitable for the permanent record by a **3-of-3 vote** (3 store / 0 reject) of the project's disclosed AI research crew ([agents/README.md](../agents/README.md)). Assessment performed in a maintainer-operated Claude Code session per the charter's Operations section; the three reviewers ran as isolated, mutually **blind** subagent contexts — one persona each, no visibility into the others' verdicts — and **each independently wrote and ran its own driver** against the released `fable-model-chain/` before voting. **Model self-check, flagged for the record:** this routine's default is Fable 5, which was not active; the orchestration/publishing session and all three assessor subagents executed on **`claude-opus-4-8`** at the maintainer's explicit direction this session. Nothing here is labeled or represented as Fable 5 output.

**Decisively for this resubmission, all three reviewers independently read the source of `regen.isi_spread_dB` and `cell.isi_spread_dB` (`inspect.getsource`) and confirmed the corrected structural claim is now literally true:** neither function references the cavity round-trip time `rt = 2L/s`; both use `exp(−Tslot/τ)` as their only inter-slot memory kernel; `regen.isi_spread_dB` *does* call `loop_gain` and `(1−loop_gain(0))/(1−loop)` but purely for the per-pulse **gain magnitude** (its output rises with bias `0.0092 → 0.0948` across `M/M_th = 0.3 → 0.8`, while `cell.isi_spread_dB` is loop-free and flat at `0.00013`) — so both are blind to the ring-down. **Each confirmed no lingering false structural statement survives anywhere in the note** (§1, §2, §5, §7, the pre-publication section, and the RFC one-liner all checked). All three also reproduced every anchor bit-for-bit against `results.json`, the cavity timing (`rt = 0.5000 ps`, `loop(0.7) = 0.91620`, `τ_rd = 5.71 ps`, `R = loop⁸ = 0.4965`), and the demonstrated loaded ISI by driving `solver.run(drive_kind='prbs')` themselves on a reduced random pattern (CAV pp `≈ +3.93 dB` / drain `≈ +4.17 dB`, inside the claimed `[2.0, 4.5] dB` band and within ~1 % of the note's 200-slot `+3.96/+4.20`), plus the flush arithmetic (`10.4 / 30.0 / 49.9 dB/slot`). All three confirmed the note contests no `results.json` value, does not reopen `M_th`, and stays orthogonal to the static F=2 fan-out headline of 07-20/07-21. Only **non-load-bearing** issues survived any reviewer's adversarial pass (each listed per persona below) — the convention-dependent `[2.0, 4.5] dB` band, the single operating point / untested grid-pattern convergence, and one process-framing note on the editorial banner. The vote record below is evidence and is not edited after posting.

- 🧵 **Fabric** — **STORE**: Substance: the note delivers a concrete, checkable quantitative result — loaded ring-down ISI at the 4-ps slot is ~4 dB peak-to-peak (band [2.0,4.5]) vs the incumbent carrier-recovery functions' 0.054/0.00013 dB, with the per-slot flush shown necessary (~10-30 dB/slot) and its sufficiency left open. Epistemic labels are correct and consistent: demonstrated is reserved for executed numbers (anchors, timing, loaded solver), the continuous-drive 5.96 dB is explicitly an in-model upper bound rather than the headline, the exact loaded dB is left convention-dependent/open, and flush sufficiency is explicitly open (§7.3). Citations and numbers are precise and consistent with results.json where they overlap; I reproduced every anchor bit-for-bit and confirmed the note contests no results.json value and does not reopen M_th. Honesty is exemplary — the executing-model disclosure, the editorial banner transparently recording the first-round reject and its single fix, the burst-vs-continuous caveat, and the "rides on the unproven gain cell" limitation are all present. Durability holds: WP1/WP3 work would consult this because it relocates the ISI question to the loaded transient the promoted fan-out notes explicitly deferred, qualifying their "ISI negligible" side-premise without touching the static F=2 headline. Decisively for this resubmission, the corrected structural claim is now literally true against the source and no false overstatement survives my read of the whole note.

  *Reproduction (independent driver).* I wrote my own driver (assess54c_fabric.py) and ran it against the released fable-model-chain. STRUCTURAL CORRECTION CHECK via inspect.getsource: regen.isi_spread_dB references 'rt'=False, uses exp(-Tslot/tau)=True, calls loop_gain=True, uses (1-loop_gain(0.0))=True; cell.isi_spread_dB references 'rt'=False, uses exp(-Tslot/tau)=True, loop/loop_gain=False. This confirms the corrected claim literally: (i) neither references rt=2L/s; (ii) both use exp(-Tslot/tau) as inter-slot kernel; (iii) regen DOES call loop_gain and (1-loop_gain(0))/(1-loop) for per-pulse gain magnitude only (source lines 108-110), so its output is bias-dependent, not an inter-slot memory; (iv) cell is loop-free. The original §1 claim ('neither contains loop, both pure C.tau recovery') was false for regen; the corrected narrower claim is true, and I found no lingering false structural statement anywhere (§1,§2,§5,§7, pre-pub, RFC line). ANCHORS bit-for-bit: plasmon_speed 2331197.965421, L_zero_drift 582.79949, L_op 576.62157, Q_353K 5.339818, M_th_353K 0.147083, per_gate_loss 2.555099, cw_regen_gain 9.661006, a_loss 0.745152. TIMING: rt=0.5000 ps, loop(0.7)=0.916203, tau_rd=5.71 ps, R=loop^8=0.4965. INCUMBENTS: regen.isi(0.7,0.25THz)=0.053876, cell.isi=0.000130; regen rises with bias 0.00918->0.09483 while cell flat at 0.00013 — direct evidence the corrected 'wrong memory' claim is right. LOADED solver.run prbs on a reduced 50-slot random pattern (seed 7, warm-up 8, said reduced): CAV pp +3.93, DRAIN pp +4.17, adjacent +3.0/+3.2, drive-independent 1e-3..3e-3 — inside the note's [2.0,4.5] band and within ~1% of the note's 200-slot +3.96/+4.20. FLUSH arithmetic: R_eff=0.361 gives 10.42 and 29.98 dB/slot (note 10.4/30.0). STREAMING: M_th_num 0.168943 and pulse_gain_streaming 7.796707 both bit-for-bit. No discrepancy of any sign or order of magnitude; only sub-1% reduced-slot Monte-Carlo differences.
  - non-load-bearing: Editorial banner asserts 'all three first-round reviewers verified the narrower claim' — a process claim I cannot independently verify, but it is framing, not a technical/storability defect.
  - non-load-bearing: The headline loaded number (~4 dB) is single-cell, single-pattern, single operating point at 353 K with grid/pattern convergence untested — the note states this honestly (§7.4), and leaves the exact quotable value open, so it is a stated limitation rather than an overstatement.
  - non-load-bearing: The [2.0,4.5] dB band spans sampling conventions (intracavity/drain/coarse-drain) that differ by ~2x; the note correctly declines to pin a single number, which is the right call but means the RFC one-liner carries a wide band.

- 🌊 **Kinetic** — **STORE**: Substance: a concrete, checkable timing result — released ISI functions model carrier recovery (exp(-Tslot/tau), ~0.9% of a slot) while the binding memory is cavity ring-down, giving loaded ISI ~4 dB vs incumbent 0.05/0.0001 dB, making the per-slot flush necessary with sufficiency open. Labels are correctly applied: demonstrated reserved for executed numbers (anchors, timing, loaded prbs), the 5.96 dB continuous-drive figure is explicitly an in-model upper bound and not the headline, the exact loaded dB is left convention-dependent/open, and flush sufficiency is open. Citations/numbers reproduce bit-for-bit against results.json and the source. Honesty is strong: convention band [2.0,4.5], burst-vs-CW caveat, single operating point, and 'everything rides on the unproven gain cell G1' are all stated. Durability: it relocates the ISI question to the loaded WP3 transient the fan-out notes deferred and pre-quantifies what that transient must overcome, changing what the project believes about the 'ISI negligible' premise. The sole first-round defect is now fixed accurately and completely — no false structural claim survives my source read.

  *Reproduction (independent driver).* Wrote my own driver (assess54c_kinetic.py) against the released fable-model-chain. Anchors match results.json bit-for-bit: plasmon_speed 2331197.965421, L_zero_drift 582.79949 nm, L_operating 576.62157 nm, Q_353K 5.339818, M_th_353K 0.147083, per_gate_loss 2.555099, cw_regen_gain 9.661006, M_th_num 0.168943, a_loss 0.745152. Timing: rt=0.500000 ps (=1/(2f0)), loop(0.7 Mth)=0.916203, tau_rd=5.71 ps, R=loop^8=0.496515. Incumbents: regen.isi(0.7,0.25THz)=0.053876, cell.isi=0.000130. CORRECTED STRUCTURAL CLAIM confirmed by inspect.getsource: regen.isi_spread_dB references rt/2L=False, calls loop_gain=True, uses exp(-Tslot/tau)=True; cell.isi_spread_dB references rt/2L=False, calls loop_gain=False (loop-free), uses exp(-Tslot/tau)=True — i.e. all four points (i)-(iv) literally true, and the original 'both pure C.tau recovery / no loop' claim was indeed false for regen. Bias-dependence confirmed: regen.isi rises 0.009184/0.022183/0.053876/0.094830 across M/Mth 0.3->0.8 while cell.isi is flat 0.000130 (direct evidence loop_gain sets per-pulse gain magnitude in regen and cell is loop-free). Reduced 50-slot prbs drive of solver.run(0.7*Mth,'prbs'): CAV pp +3.93 dB / DRAIN pp +4.17 dB, adjacent +2.98/+3.24, R_eff=0.3613 (note: cav +3.96/drain +4.20/R_eff 0.361 — within ~1%, inside [2.0,4.5] band, ~73x the incumbent). Flush arithmetic 20*log10(R_eff/R_target): 10.43/29.98/49.94 dB/slot, matching note's 10.4/30.0/49.9. No order-of-magnitude or sign discrepancy anywhere.
  - non-load-bearing: Loaded ISI headline is convention-dependent (cav +3.96 / drain +4.20 / coarse ~2.5 dB); the note handles this honestly with the [2.0,4.5] band and an explicit 'single quotable number open' caveat, but the exact figure remains unsettled pending the WP3 gated transient.
  - non-load-bearing: The bias-gated flush's sufficiency is genuinely open — solver.run never flushes between slots, so the ~10-30 dB/slot requirement is computed from the un-flushed transient and the guard-interval fit is unmodeled; correctly labeled open.
  - non-load-bearing: Single operating point (0.7 M_th, 353 K), single-cell N=240, one random pattern; grid/pattern convergence untested, as the note states.

- ⚛️ **Quanta** — **STORE**: Substance: the note delivers a concrete, checkable, corrective result -- loaded ring-down ISI at the 4-ps slot is ~4 dB pp (band [2.0,4.5]), roughly 73x the incumbent regen.isi and ~3e4x cell.isi, driven against the released nonlinear solver, with a necessary-but-open-sufficiency flush finding. Epistemic labels are correctly applied: the demonstrated loaded ~4 dB is executed, the 5.96 dB continuous-drive figure is labeled an in-model upper bound (not the headline), the exact loaded number is left convention-dependent/open, and flush sufficiency is explicitly open. Citations and numbers are precise and reproduce bit-for-bit against results.json and the model chain; the note contests no results.json value and does not reopen M_th. Honesty is strong -- it repeatedly foregrounds that everything rides on the unproven gain cell and that the flush is an architectural claim the code does not simulate. Durability holds: a WP3 timing worker (or anyone consuming the fan-out notes' "ISI negligible" premise) must consult this, since it relocates the ISI question to the loaded transient those notes deferred. The single first-round defect is now fixed to the true narrower claim and no lingering false structural statement survives a full-note read.

  *Reproduction (independent driver).* I wrote my own driver (assess54c_quanta.py) and inspected the source directly. CORRECTION CHECK confirmed literally true: inspect.getsource shows regen.isi_spread_dB does NOT reference rt (=2L/s), uses exp(-Tslot/tau) as its only inter-slot memory (inv = 1-(1-inv)*rec), and DOES call loop_gain plus (1-loop_gain(0.0))/(1-loop) purely for per-pulse gain magnitude -- confirmed bias-dependent since its output rises 0.00918/0.02218/0.05388/0.09483 across M/Mth=0.3/0.5/0.7/0.8; cell.isi_spread_dB is loop-free (no loop token), uses exp(-Tslot/tau), no rt, flat 0.000130 across all bias. Anchors bit-for-bit: s=2331197.965421, L_zero=582.79949 nm, L_op=576.62157 nm, Q_353K=5.339818, M_th_353K=0.147083, per_gate_loss=2.555099 dB, cw_regen_gain=9.661006 dB, a_loss=0.745152 -- all match results.json. Timing: rt=2L/s=0.500000 ps = 1/(2 f0), loop(0.7 Mth)=0.91620, tau_rd=5.7131 ps, R=loop^8=0.49651. Incumbents: regen.isi(0.7,0.25THz)=0.053876, cell.isi=0.000130. Loaded solver.run(prbs) on a reduced 50-slot random pattern (seed 7, warm-up 6) gives adj=+2.98 dB, pp=+3.93 dB at drive 2e-3, drive-independent 1e-3..3e-3 -- inside the note's [2.0,4.5] band and within ~1% of its +3.00/+3.96; clearly order-of-magnitude above the 0.054/0.00013 incumbents. Flush arithmetic from R_eff=0.361: 10.42/29.98/49.93 dB/slot, matching the note's 10.4/30.0/49.9. M_th_num=0.168943 (json match), M/Mth_num at 0.7 = 0.609. Nothing did not match.
  - non-load-bearing: Minor: the note reports a 200-slot random pattern at seed 7 for the headline loaded numbers; a reader cannot regenerate the exact +3.96/+4.20 without rerunning the full listing, though my reduced 50-slot run reproduces it closely (pp +3.93, adj +2.98).
  - non-load-bearing: The headline [2.0,4.5] dB band spans sampling conventions (intracavity cav vs drain vs coarse-drain) that differ by ~2 dB; the note honestly labels the single quotable number open, but the wide band means the practical takeaway is 'order-of-magnitude, not 0.0001 dB' rather than a sharp value.
  - non-load-bearing: R_eff=0.361 is derived from one long-run CAV number and then propagated into the flush and Q/loop tables; it is a reasonable but single-pattern estimate (grid/pattern convergence untested, as the note states in Limitation 4).
