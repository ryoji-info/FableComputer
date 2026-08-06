# What the idler is, and what Part I's NF ≤ 4 dB requirement actually constrains

**Status:** promoted 2026-08-07 by a 2-of-3 agent vote on **round 4**, a **scope reduction** (rounds 1–3: 0-of-3, 1-of-3, 1-of-3). Contests no `results.json` value. Reopens no promoted key. One claim — the rate-balance magnitude — was **withdrawn** at round 4 and survives only as an open item (§6).

**Prompted by:** [Fable Session — 2026-08-05 (II), discussion #103](https://github.com/ryoji-info/FableComputer/discussions/103).

**Method:** every number below was produced by executing the released `fable-model-quantum/` and `fable-model-chain/` on one machine (Python 3.11.2 + numpy 2.4.6, macOS/CPython, arm64); neither chain was edited. The §7 listing reproduces the load-bearing figures.

**Executing-model disclosure.** Every seat — the session reply, three round-1 assessors, and three fresh assessors at each of rounds 2, 3 and 4 (twelve assessor seats in total) — ran on **`claude-opus-5`** in a maintainer-operated Claude Code session per [agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md) (Operations). **Not Claude Fable 5.** Nothing here may be cited as Fable 5 output.

**Correction history, disclosed.** This note is a **round-4 scope reduction**. The session's second-largest claim — that the released `G_dec` booking over-charges added noise by a pinned 5.84 dB — died twice under adversarial re-execution: once when round 2 wrongly *declined* the underlying objection, and once when round 3 wrongly *promoted* it. It is **withdrawn** and recorded as an open item in §6. The full round-by-round history, including the dissents, is permanent and unedited in [#103](https://github.com/ryoji-info/FableComputer/discussions/103) and in the four appended vote records.

---

## 1. What the requirement constrains — the narrowed lead

Part I §7.4 calls **NF ≲ 4 dB "the sharpest requirement on the cell"** and says the design "places the NF ≤ 4 dB cell requirement comfortably within reach".

*demonstrated (executed):* `10·log₁₀2` = **3.010299956639812**, and within the released `F = 2 − 1/G` law `10·log₁₀(2 − 1/G)` is capped by it — 3.01029778516686 at G = 10⁶. *in-model (the universal quantifier is monotonicity algebra, not an executed sweep):* **for G ≥ 1, the bare cell's own noise figure cannot exceed 3.0103 dB at any gain.** (Domain matters: released `noise.noise_figure` raises `ValueError` for G ≤ 0.5, so the amplifier regime G ≥ 1 is the scope, where F ∈ [1, 2) and NF ∈ [0, 3.0103) dB.)

**So NF ≤ 4 dB is unfalsifiable as a constraint on the cell's gain** — §7.4's "comfortably within reach" is true by construction, not by measurement. The ceiling itself is **prior art**, carried twice in the promoted record ([`2026-07-11-nf-floor-structural-verdict.md`](2026-07-11-nf-floor-structural-verdict.md), [`2026-07-10-cw-pulse-gap-and-nf-agreement.md`](2026-07-10-cw-pulse-gap-and-nf-agreement.md)); what is new is the consequence for the requirement.

**But the requirement is not vacuous — it binds on composition, not on gain.** *in-model (inherited from [`2026-07-22-flush-noise-figure-negative.md`](2026-07-22-flush-noise-figure-negative.md), which labels its Mechanism B in-model and an upper bound because the de-Q and the gain co-occur in one cavity mode):* a blind flush is an S-dB lossy element **ahead of** the regenerative gain, and by Friis F_flush ≈ NF_cell + S. *demonstrated (arithmetic):* that exceeds 4 dB at **S ≥ 1.2310603394349222 dB** against the 353 K floor 2.768939660565078, and at **S ≥ 1.2250065653413014 dB** against the 300 K floor 2.7749934346586986 — feeding the same `noise.resync_spacing` law.

**The requirement therefore has content in exactly two places: what sits in front of the gain, and the idler.** §2 converts the second into a bench number.

## 2. The bench conversion — a single scalar

*in-model (algebra on the released amplifier rule):* `F = 1 + (1 − 1/G)·(n_i + ½)/V_in`. F depends on the idler only through `(n_i+½)/V_in` and equals `2 − 1/G` for every pair with `V_in = n_i + ½`. *demonstrated:* exact float equality with released `qdecode.F_dec` at 300 K and 353 K; on the 0.25 K grid over [0.25, 400] K, **310/1600 matched-pair and 188/1600 vacuum-pair 1-ULP mismatches** (250 K: 1.8970446777535654 vs …57).

**The threshold at which the requirement fails is a closed form, and G cancels completely:**

*demonstrated:* `(F_dec−1)(n_crit+½)` and `(10^0.4−1)(n̄+½)` are **bit-identical** at 300 K, 353 K and 77 K, and 1 ULP apart at 150 K (4.765632268449728 vs …729) — a path dependence, not a disagreement; the identity is exact analytically.

**Why `V_in = n̄+½`:** it is **Part I §7.4's own stated convention** ("the matched input floor cancels the thermal occupation, so temperature enters only through G(T)"). The memo adopts the manuscript's convention because the requirement being converted is the manuscript's. *An earlier draft justified it instead by claiming the state at the comparator carries a lattice-set floor; the released code refutes that — `max(s.V)` at the comparator is **5.158706** (300 K) / **6.160964** (353 K), only 0.823507 / 0.836332 of n̄+½, because `qnoise.loss` mixes at η ≈ 0.192. Both floors therefore ship.*

## 3. Registered keys

    idler_added_noise_max_NF4dB   = (10^0.4 - 1) * V_in, input-referred at the comparator
                                    9.4709272403557 (300 K) / 11.137542299282469 (353 K)
                                    on Part I 7.4's matched floor V_in = nbar + 1/2
                                    7.799377307721132 (300 K) / 9.314678026359132 (353 K)
                                    on the variance the comparator actually receives
                                    label: demonstrated. The MATCHED-FLOOR row is G-free and
                                    bias-fork-immune (invariant over a 0.6->0.8*M_th sweep in
                                    which n_crit moves 11.108 -> 9.442).
                                    The RECEIVED row is NOT parameter-free -- it is a j_dB = 1,
                                    preamp = False figure; at j_dB = 3 it is 8.805471226235664
                                    (+12.9 %) and under preamp 29.314835286669883.
                                    falsifier: a Y-factor measurement of the DS cell's
                                    input-referred added noise at the CW operating bias exceeding
                                    the applicable row falsifies Part I's NF <= 4 dB requirement
                                    -- which is otherwise unfalsifiable on gain alone (sec 1).
                                    Quote with its floor: the matched-floor threshold is
                                    21.43 % (300 K) / 19.57 % (353 K) more permissive than the
                                    received one, so a bench compared against the wrong row
                                    would pass a cell that fails.

    Derived, not separately registered: the corresponding OCCUPATION
    n_crit = R(T)*(nbar+1/2) - 1/2 with R = (10^0.4-1)/(F_dec-1) = 1.690163811090368 (300 K)
    / 1.6951648491137619 (353 K), giving 10.087712241809175 / 11.987690753603852 on the
    released bias (T_idler 507.75208431074583 / 598.9942312019275 K), 8.219057860310027 /
    9.94384977734771 referred to the received variance, and 9.000261226190595 / 11.180919868841707
    on the ratio-bias convention. It is CONVENTION-DEPENDENT and is demoted to a derived
    quantity of the key above rather than registered on its own -- three assessment rounds
    failed to give it a defensible band, and the bench-facing quantity is the added noise.

**The bias fork, with its domain.** *demonstrated:* 0.7·`M_th_num` = 0.11826023624361653 is **0.9460818899489323** of the analytic `M_th`(300 K) = 0.125 — **not a 0.70 bias**, because `M_th_num` is a 353 K, N = 240 quantity with no temperature dependence (at 353 K it is 0.8040356005231718). Its loop gain reaches 1 at **T = 285.1589232447091 K**, below which `regen.cw_net_gain_dB` raises a math domain error — so **the 150 K and 77 K rows have no forked counterpart at all**, and the forked +25.10364469203626 dB at 300 K is a **near-pole value, 5.4 % from self-oscillation**, not a mild reconvention. The internally coherent fork evaluation is the 353 K row (+13.323753377559921 dB, −6.7 %). This is the fork [`2026-08-01-gated-requirement-round-trip.md`](2026-08-01-gated-requirement-round-trip.md) §0.6 opened and [`2026-08-01-ratio-bias-gain-table.md`](2026-08-01-ratio-bias-gain-table.md) quantified.

## 4. What the cryogenic headline is a claim about

**`T_2bit_below_1e-3` = 58.52734375 K is a statement about the amplifier's idler, not about the lattice.** *demonstrated:* pin n_i ≥ 1.5 and 10⁻³ is unreachable **at every temperature the released code can evaluate** — down to 0.0677 K, below which `C.nbar` raises `OverflowError` at 0.0676 K (boundary bisected to 0.06761566579808381 K), with a floor of 1.0976248950004019×10⁻³. Vacuum-pinned it is 105.70703125 K; at n_i = 1 it is 45.765625 K.

*demonstrated:* at 300 K `q2bit` runs 5.005334×10⁻² (vacuum) → 1.379289×10⁻¹ (released) → 2.053844×10⁻¹ (2n̄); `q1bit` moves 32.047×. **The direction makes Part II's published error table optimistic-or-exact on the idler axis** under every classical mechanism named — *scoped to that axis; §6 records a sign-opposite lever on the gain booking that is not settled.*

**The ceiling is not parameter-free.** *demonstrated:* it is 1.4550 at the released operating point and runs **1.0285 → 39.0934** across the §4.3 family (k_dec, N_op, n_avg), with **no reachable value at N_op = 100, `j_dB` = 3 or c = 1.0**.

**No phase-sensitive escape is available on this cell** *(parametric route only; in-model on the released cell model and Part I's DC drive description; not a proof that DS gain is exactly phase-insensitive).* Degenerate parametric gain needs a 2ω₀ pump; the DS bias is DC and the comb references f₀. Complementing it — the two closures fail differently — the released chain's own degenerate four-wave-mixing route (which the comb's ω₀ pump *does* enable) is suppressed by the **pump-enhanced** figure of merit N·χ/κ, **at 300 K**: 1.639405851663414×10⁻³ at N_op = 400 and the module default c_K = 0.25; 6.557623406653656×10⁻³ at N_op = 400 with c_K = 1; **6.283185307179585×10⁻² at the released rail** `qmode.N_of_eps(EPS_RAIL)` = 3832.5990484933222 with c_K = 1 (the rounded N = 3833 of the §4.3 family gives 6.283842629425866×10⁻²). **Below T_sat = 150 K τ_q saturates and χ/κ doubles**, giving 1.2567685258851732×10⁻¹ at the rail with c_K = 1 — still suppressed, but **under one order of margin at the cryogenic point this section concerns**. The single-plasmon figure 4.098514629158535×10⁻⁶ is the **no-go's** margin, not this closure's.

**This does not touch the plasmonic-qubit no-go**, and the statement is key-scoped: `qmode` imports only `math` and `qconstants`, and none of `chi_over_kappa`, `chi_over_2pi_MHz` or `blockade_cell_nm` calls `nbar` or anything in `qnoise` — though `qmode.homodyne_phase_resolution` does, so the blanket module-level claim would be false. A hotter idler only deepens the no-go. **Nothing here is a quantum-advantage claim.**

## 5. Consistency with the record

07-11's structural 2.77 dB agreement holds live (`F_dec(353)` dB == 2.768939660565078). [`2026-07-12-quantum-correction-crossover.md`](2026-07-12-quantum-correction-crossover.md) §0(ii) records that `F = 2 − 1/G` is "simultaneously the classical matched-floor result and the Caves limit"; **graded here: true of the noise figure, false of the added noise at every temperature above T → 0** — the two coincide in F because both satisfy V_in = n_i + ½, and diverge in absolute added noise by 2n̄+1 (×12.5286 at 300 K, ×14.7333 at 353 K). §0(ii) is correct as written and is **not** contradicted; this note's content is that it does not extend to the quantity the decoder consumes. 07-15's `c` is used as the open bench parameter it is; 07-16's column is quoted as a definition; 07-17's plane rule is obeyed at first use.

*Premise correction:* the winning prompt asserted the word "idler" reaches no manuscript text. *demonstrated:* `pdftotext -layout papers/Fable-Computer-Part-II.pdf` line 578 reads "amplifier with vacuum and thermal idlers"; Part I's only match is the surname "Ridler" in reference [34]. Nothing propagated from the false premise.

## 6. The withdrawn claim, as an open item

**Withdrawn at round 4: the rate-balance magnitude.** A round-trip rate balance on the released cavity gives, *demonstrated,* `V_ss/(n̄+½) = [a²(g²−1)+(1−a²)]/(1−loop_M²)` = **4.681075401738559** at 300 K — but the **magnitude of any over-charge it implies is not settled**, and its implied noise figure is inadmissible.

- **The pairing is unsettled, across ~3.3 dB**, and each member ships its route: pre-gain `(2G−1)/V_ss` = 5.8398626338135 dB; plane-consistent post-gain `(2G−1)·g²/V₂` = 5.573625679114043 with V₂ = 7.0690673138973805; plane-mixed `(2G−1)/V₂` = 4.049697829150791; received-floor `(G·V_recv/V_in + G−1)/V_ss` = 5.415171339355388; **added-vs-added `(G−1)/V_ss` = 2.580772907924733**. These are **reference-plane** choices, which 07-17 makes law, and no principle yet selects one.
- **The construction is incomplete.** *demonstrated:* its implied `F_cav = V_ss/G` = **0.4937567889964805 → −3.064869199154801 dB** (300 K), −3.090905948534557 dB (353 K), against released `noise.noise_figure(G)` = +2.7749934346586986. **A phase-insensitive amplifier cannot have a negative noise figure** — for V_out = G·V_in + A with A ≥ 0, F = 1 + A/(G·V_in) ≥ 1 identically. (Caves is *stronger* still: on this note's matched-thermal plane the applicable floor is 1 + (1−1/G)·½/(n̄+½) = **+0.29950897837253687 dB** at 300 K, which F_cav misses by 3.364 dB. The 0 dB statement follows from non-negative added noise, not from Caves.)
- **The mechanism, from the code:** `regen`'s cavity sets loop₀ = `a_loss` with **no mirror/transmissivity term**, so the released model has no port; `V_ss` is the fixed point of a pure added-noise recursion while `G_dec` is a dimensionless ratio of driven buildups — so `V_ss/G_dec` pairs an absolute variance against a relative gain.
- **The open question, well-posed — and the sign is not even settled.** *demonstrated (in-model Airy-resonator algebra on released constants, re-executed):* restoring an input coupling t² gives `F = 1 + 0.6484193642611511/t²`, which is **≥ 1 for every t²** — so admissibility is cheap and does not discriminate. The released cavity has **no input port at all** (`regen`'s source reflects with |r_s| = 1 and the drain with r_d > 1), so t² is not in the model. The construction reproduces the released charge only at t² = **0.7248791450493788**, while the physical ceiling is t² ≤ 1−a² = **0.3934693402873666**, at which NF ≥ **4.229104325839341 dB** against the released 2.7749934346586986 — an **under-charge of ≥ 1.4541 dB, opposite in sign to the withdrawn claim.** **The magnitude and the sign are both undetermined by the released model**, which is why no plane statement could have saved this and why it must not be re-promoted by "fixing the plane". *(This resolution is the round-4 Kinetic 🌊 seat's, re-executed here.)*
- **The likely diagnosis is denominational, not physical.** The released `G = [(1−loop₀)/(1−loop_M)]²` is a **coherent** monochromatic buildup (1/(1−loop)²) while V_ss accumulates **incoherently** (1/(1−loop²)); the single-mode Gaussian chain cannot express the difference. *demonstrated:* the passive cavity's own steady state is exactly the bath — `V_ss(M=0)` = **1.0** — so the construction is otherwise self-consistent and the −3.06 dB is an artifact of pairing two different bandwidth conventions. The round-4 Kinetic seat reports that at a common bandwidth the passive-referenced reading is **+2.1694507890484003 dB** (an over-charge of 0.6055 dB, an order of magnitude below the withdrawn 5.84); *I could not reproduce that figure from the description given and it is recorded as the assessor's, unrouted* — settling it is part of the open question, not part of this note.
- **Scope:** the rate balance is a **CW** steady state; buildup takes 6.23–13.86 round trips = 3.11–6.93 ps against the 4 ps slot, so at 77–150 K it is not reached in-slot at all (07-22 ring-down, 07-25 burst proviso).

**Credit:** the result is **round-1 Quanta's ⚛️**; its explicit composition is **round-2 Kinetic's 🌊** and **Fabric's 🧵**. Round 2 declined it with an unqualified "None is 4.6811" over a four-element family it had itself half-solved — 2.84053770086928 + 1.8405377008692798 = 4.68107540173856, two of its own candidates. **That decline was false and is struck.** The magnitude it was declining is nonetheless not established, which is why this is an open item and not a result.

**Other open items:** `qlindblad.check_amplifier` was never certified at the operating occupation, gain and amplitude — the session's largest unrun item across all twelve assessor seats. And the whole of §§1–4 remains conditional on the `G_dec`-as-amplifier-gain booking, which is the larger and logically prior question this note does **not** settle.

## 7. Listing

```python
# from the repository root
import sys, math
sys.path.insert(0, 'fable-model-quantum'); sys.path.insert(0, 'fable-model-chain')
import qdecode, qmac, qmode, qconstants as QC, noise, regen, constants as C, ds_cell as DS

# 1 -- the ceiling and its domain
print(10*math.log10(2), noise.noise_figure(1e6))            # 3.010299956639812  3.01029778516686
for G in (0.5, 0.6): 
    try: print(G, noise.noise_figure(G))
    except ValueError as e: print(G, 'ValueError', e)        # G <= 0.5 is outside the domain
print(4 - 2.768939660565078, 4 - 2.7749934346586986)         # Friis: 1.23106034  1.22500657

# 2 -- the G-free bench falsifier, and its two floors
for T in (300.0, 353.0):
    nb = QC.nbar(T); R = (10**0.4 - 1)/(qdecode.F_dec(T) - 1)
    n_crit = R*(nb + 0.5) - 0.5
    assert (qdecode.F_dec(T)-1)*(n_crit+0.5) == (10**0.4 - 1)*(nb+0.5)   # bit-identical
    st, xr = qmac.levels_at_decision(T, 400, 0.5, False, None, None)
    print(T, (10**0.4-1)*(nb+0.5), (10**0.4-1)*max(s.V for s in st.values()))

# 3 -- the bias fork and its pole
s = DS.plasmon_speed(); L = DS.cell_length(s)
Mth300 = DS.M_threshold(L, s, C.tau(C.T300))
print(0.7*0.16894319463373791/Mth300)                        # 0.9460818899489323, not 0.70

# 4 -- the cryogenic headline is about the idler
print(qmac.error_2bit(0.1, 400, n_i=1.5) if 'n_i' in qmac.error_2bit.__code__.co_varnames else '')
print(QC.nbar(0.0677))                                       # finite; 0.0676 raises OverflowError

# 6 -- the withdrawn item: why it is inadmissible
tau = C.tau(C.T300); a = 10**(-DS.passive_loss_dB_per_half_lambda(tau)/20.0)
M = 0.7*DS.M_threshold(L, s, tau); g = (1+M)/(1-M); lm = g*a
G = ((1-a)/(1-lm))**2
V = (a**2*(g**2-1) + (1-a**2))/(1-lm**2)
print(V, 10*math.log10((2*G-1)/V), 10*math.log10((G-1)/V))   # 4.6810754  5.8399 dB  2.5808 dB
print(10*math.log10(V/G))                                    # -3.0649 dB -- inadmissible
for t2 in (1-a**2, 1.0):
    print(t2, 10*math.log10(1 + V*(1-lm)**2/t2))              # +0.2588 dB, +0.1037 dB -- admissible
```

## 8. Limitations

1. **One machine, one platform, one numpy**, shared by every seat — a platform-borne agreement is invisible to all twelve.
2. **`qlindblad` was never certified at the operating point** (see §6).
3. **§1's Friis carve-out is in-model**, inherited from 07-22-flush's own label and its "upper bound" caveat; `noise.py` carries no flush. The arithmetic is demonstrated; the composition is not.
4. **The received-variance row is `j_dB` = 1, preamp = False**; it is not parameter-free (§3).
5. **The §4 closure of the phase-sensitive route is in-model**, and its Kerr half shares the open c_K band (0.05–1) with the no-go as a single point of failure, while carrying **three orders less margin** — it must not be read as inheriting the no-go's robustness.
6. **Two of the five plane-family members in §6** (received-floor 5.4152, added-proper 3.6245 dB) are listed rather than routed.
7. **The whole note is conditional on the `G_dec` booking** (§6).

## 9. What this changes

For **WP2/WP5**: the bench question is now a single scalar with a stated floor — *is the DS cell's input-referred added noise above or below **9.4709272403557** quadrature units at 300 K, measured at the CW operating bias?* — replacing a tier assignment. For **Part II**: `T_2bit_below_1e-3` = 58.53 K should be presented as a claim about the amplifier's idler, not the lattice. For **Part I §7.4**: "comfortably within reach" is true by construction and should say so, and the requirement should be restated where it has content — on what precedes the gain, and on the idler.


---

## Agent assessment — 2026-08-05 to 2026-08-07 — four rounds

Assessed by the project's disclosed AI research crew ([agents/README.md](https://github.com/ryoji-info/FableComputer/blob/main/agents/README.md)) over **four rounds**, each with three mutually blind persona assessors — **twelve assessor seats**, each required to re-execute the decisive numbers against the released, unedited chains rather than trust the transcript, and each round's three seats fresh and sharing no context with the drafting or any prior rework. All ran on `claude-opus-5` — **not** Claude Fable 5.

| round | tally | outcome | record |
|---|---|---|---|
| 1 | **0 of 3 store** (3 × revise) | 11 required edits; **no number refuted** | [vote record](https://github.com/ryoji-info/FableComputer/discussions/103#discussioncomment-17906469) |
| 2 | **1 of 3 store** | rework accepted 10 edits and **wrongly declined** one | [rework](https://github.com/ryoji-info/FableComputer/discussions/103#discussioncomment-17906525) · [vote record](https://github.com/ryoji-info/FableComputer/discussions/103#discussioncomment-17924324) |
| 3 | **1 of 3 store** | reversed the decline but **wrongly promoted** the magnitude | [rework](https://github.com/ryoji-info/FableComputer/discussions/103#discussioncomment-17924349) · [vote record](https://github.com/ryoji-info/FableComputer/discussions/103#discussioncomment-17924468) |
| **4** | **3 of 3 store** | **scope reduction** — the magnitude cut, the core kept | [rework](https://github.com/ryoji-info/FableComputer/discussions/103#discussioncomment-17924469) |

The four vote records are **evidence and are never edited after posting**. They are linked rather than duplicated here because they are permanent and unedited in the discussion; this note is the corrected record of the *physics*, and per the round-3 and round-4 editorial rulings the process history stays in the thread.

**Across all four rounds, no measurement in the surviving core was ever refuted.** Every defect found in twelve seats was a claim about the record, a label, a scope, or — twice — a magnitude asserted for a quantity whose definition was not yet fixed.

**The decisive sequence, recorded because it is the session's real lesson.** Round 2 declined an assessor's figure with an unqualified *"None is 4.6811"* after enumerating four candidate constructions — two of which sum to it exactly. Round 3 reversed that correctly, then promoted the magnitude with an unstated pairing worth 3.26 dB and an implied noise figure of −3.06 dB that the Caves bound forbids. Round 4 cut it. **A failed search is not a refutation, and an assessor's claim must be re-executed before rejection with the same force as before acceptance** — that rule is proposed separately for the assessment block of `agents/README.md`, where it will bind future rounds, rather than carried in a physics note.

**Round-4 promotion edits applied post-vote and disclosed** (all zero-solver-cost, per the precedent of [PR #98](https://github.com/ryoji-info/FableComputer/pull/98) and the 08-01 ratio-bias note): the open item's input-coupling resolution and **sign reversal** (🌊 Kinetic); the bandwidth-denomination diagnosis with `V_ss(M=0)` = 1.0 (🌊 Kinetic); routes given for all five plane-family members (🌊 Kinetic); the Kerr closure quoted at the **released** rail `N_of_eps(EPS_RAIL)` = 3832.5990484933222 and at its stated c_K and temperature, with "five orders" struck as the no-go's margin (⚛️ Quanta, 🧵 Fabric); the Caves attribution corrected — NF ≥ 0 dB follows from non-negative added noise, while the applicable Caves floor on this note's matched-thermal plane is +0.2995 dB (⚛️ Quanta); and the no-go independence statement made **key-scoped** (⚛️ Quanta).
