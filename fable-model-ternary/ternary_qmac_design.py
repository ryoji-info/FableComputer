# -*- coding: utf-8 -*-
"""Ternary accelerator on the Part II quantum-analog fabric: design listing.

Companion to The Fable Computer, Part III (Section 6). Written for a design study of
2026-10-03 whose section numbers the headers below keep; every number of Part III's
Section 6 is printed here. ternary_qmac_design.out next to this file is the reference output.

Run from anywhere inside the repository:   python ternary_qmac_design.py
(Python 3 + numpy; a few seconds.) The released chains are imported READ-ONLY: no
bytecode is written, nothing in fable-model-quantum/ or fable-model-chain/ is
edited, and run_all.py is never imported or run.

In-model extensions (everything else is a released call):
  [E1] K-input combiner: balanced binary tree of the released qnoise.combine
       (w = n_left / n_total). Every arm first passes ceil(log2 K) - 1 extra
       junction levels, each a released junction plus (default) the released
       quarter-wave, so all arms see the same path.
  [E2] Comparator fan-out to K comparators: 3.0 dB per halving (log2 K) plus
       ceil(log2 K) junction levels, each with the released quarter-wave.
       K = 2 is qmac.fanout_dB exactly.
  [E3] Decision: released midpoint thresholds, worst-case symbol variance
       (qmac.decision_variance's convention), decoder_amp_noise, and
       V_static = c^2 (x_range / k_dec)^2 (released form at c = 1/sqrt(12)).
  [E4] Operating point: N_op is capped by N_rail at a stated plane. The rail is
       anchored at no plane in the record (notes/2026-07-17 weekly, section 4),
       so two readings are carried: P2 = top level at the combiner output (the
       first plane where the sum exists as one field) and P1 = the pre-loss
       launch sum K * N_op (the reading notes/2026-07-16 checked first).
  [E5] Cells: K comparators + thermometer-to-binary logic + alignment buffers
       in the record's idiom; accounting variants are carried explicitly.
  [E6] Signed tile: K_t phase-encoded trit arms (pi phase = -1, gated = 0)
       plus a coherent offset arm at combiner weight 1/2.
  [E7] Relaunch: inside a counter tree every input is a regenerated logic
       output. '1' = a rail pulse, '0' = the cell's unsaturated output, i.e.
       released qnoise.amp(vacuum, G_dec(T)); both pass a released loss from
       the rail down to N_op, then the released input transit.
  [E8] Cell dissipation: released Joule form P = n m* v0^2 / tau
       (fable-model-chain/thermal.py) with the tracked bias v0 = 0.7 M_th s,
       M_th proportional to 1/tau, and the quantum chain's tau_q(T): P ~ tau^-3.
       Part II section 1: below ~255 K the hydrodynamic closure is unevaluated,
       so every cold-side cell figure is uncertified.
"""
import json
import math
import os
import sys

sys.dont_write_bytecode = True


def _repo_root():
    if os.environ.get("FABLE_REPO"):
        return os.environ["FABLE_REPO"]
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "fable-model-quantum")):
            return d
        d = os.path.dirname(d)
    raise SystemExit("run this script from inside the FableComputer repository")


ROOT = _repo_root()
sys.path.insert(0, os.path.join(ROOT, "fable-model-quantum"))

import numpy as np                 # noqa: E402
import qconstants as C             # noqa: E402
import qdecode                     # noqa: E402
import qerrors                     # noqa: E402
import qmac                        # noqa: E402
import qmode                       # noqa: E402
import qnoise as Q                 # noqa: E402

RQ = json.load(open(os.path.join(ROOT, "fable-model-quantum", "results.json"), encoding="utf-8"))
RC = json.load(open(os.path.join(ROOT, "fable-model-chain", "results.json"), encoding="utf-8"))
N_RAIL = qerrors.N_RAIL
K_DEC = qdecode.K_DEC
X_RAIL = math.sqrt(2 * N_RAIL)
TEMPS = (4.0, 20.0, 48.0, 77.0, 150.0, 300.0)
OUT = {}


def hdr(s):
    print("\n" + "=" * 100 + "\n" + s + "\n" + "=" * 100)


# --------------------------------------------------------------------------- [E1]-[E7]
def qwave(T):
    return C.loss_dB_per_half_lambda(T) / 2.0


def fanout_K_dB(K, T, j_dB, xprop=True, mp=False):
    """[E2]; K = 2 reproduces qmac.fanout_dB (3.0 + j + quarter-wave) exactly."""
    nj = 1 if mp else math.ceil(math.log2(K))
    nq = nj if xprop else 1
    return 3.0 * math.log2(K) + j_dB * nj + nq * C.loss_dB_per_half_lambda(T) / 2.0


def extra_levels(K, mp=False):
    return 0 if mp else max(math.ceil(math.log2(K)) - 1, 0)


def arm(on, T, N_op, j_dB, relaunch, snr=None, V0=None):
    """One input arm up to the combiner input."""
    if not relaunch:
        return qmac._propagate(N_op if on else 0, T, snr, N_op, j_dB)      # released quiet launch
    if on:
        st = Q.GState(N=N_RAIL)                                              # restored '1' at the rail
    else:
        st = Q.amp(Q.GState(N=0), qdecode.G_dec(T), T)                      # unsaturated '0' [E7]
        if V0 is not None:
            st.V = V0
    st = Q.loss(st, N_op / N_RAIL, T)                                        # relaunch attenuator
    return Q.loss_dB(st, qmac.input_transit_dB(T, j_dB), T)


def combine_tree(states):
    if len(states) == 1:
        return states[0]
    m = len(states) // 2
    return Q.combine(combine_tree(states[:m]), combine_tree(states[m:]), w=m / len(states))


def v_static(x_range, c):
    if c is None:                                                            # released, c = 1/sqrt(12)
        return qdecode.threshold_band_variance(x_range)
    return c * c * (x_range / K_DEC) ** 2


def tile(K, T, N_op, relaunch=True, xprop=True, c=None, j_dB=None, snr=None, p1=0.5, mp=False,
         dcrit=0.0, V0=None):
    """K-input unsigned counter tile (levels s = 0..K). Returns dict with the symbol
    error p (plus R3 metastability if dcrit > 0), levels, V, N_top, half-gap."""
    jj = qmac.JUNCTION_DB if j_dB is None else j_dB
    ne = extra_levels(K, mp)
    xs, Vs, N_top = [], [], None
    for s in range(K + 1):
        arms = [arm(i < s, T, N_op, j_dB, relaunch, snr, V0) for i in range(K)]
        if ne:
            arms = [Q.loss_dB(a, ne * (jj + (qwave(T) if xprop else 0.0)), T) for a in arms]
        st = combine_tree(arms)
        if s == K:
            N_top = st.x ** 2 / 2.0
        st = Q.loss_dB(st, fanout_K_dB(K, T, jj, xprop, mp), T)
        xs.append(st.x)
        Vs.append(st.V)
    xr = max(xs)
    V = (max(Vs) + qdecode.decoder_amp_noise(T)) / 1 + v_static(xr, c)
    pri = [math.comb(K, s) * p1 ** s * (1 - p1) ** (K - s) for s in range(K + 1)]
    p = Q.symbol_error(xs, pri, V)
    half = (xs[1] - xs[0]) / 2.0
    if dcrit:
        sig = math.sqrt(V)
        dens = math.exp(-0.5 * (half / sig) ** 2) / math.sqrt(2 * math.pi) / sig
        p += sum(pr * ((s > 0) + (s < K)) for s, pr in enumerate(pri)) * 2 * dcrit * dens
    return {"p": p, "x": xs, "V": V, "N_top": N_top, "half": half}


def n_op(K, T, plane="P2", **kw):
    """[E4] rail-referenced N_op. P2: top level at the combiner output = N_rail
    (exact: the tile is linear in amplitude). P1: pre-loss launch sum K*N_op = N_rail."""
    if plane == "P1":
        return N_RAIL / K
    kw = {k: v for k, v in kw.items() if k in ("relaunch", "xprop", "j_dB", "mp")}
    return 1000.0 * N_RAIL / tile(K, T, 1000.0, **kw)["N_top"]


CONV = {     # name: (plane, tile kwargs)
    "REF":  ("P2", dict(relaunch=True, xprop=True)),
    "CONS": ("P1", dict(relaunch=True, xprop=True)),
    "PERM": ("P2", dict(relaunch=False, xprop=False, c=0.02, mp=True)),
}


def qfa(T, conv="REF", plane=None, **over):
    """QFA-3 at a named convention, with one-at-a-time overrides."""
    pl, kw = CONV[conv]
    kw = dict(kw, **over)
    return tile(3, T, n_op(3, T, plane or pl, **kw), **kw)


def signed_tile(Kt, T, N_op, j_dB=None, pz=1.0 / 3.0):
    """[E6] quiet-launched signed trits + coherent offset arm (weight 1/2, K_t*N_op)."""
    jj = qmac.JUNCTION_DB if j_dB is None else j_dB
    ne = extra_levels(Kt)
    xs, Vs, N_top = [], [], None
    for s in range(-Kt, Kt + 1):
        vals = [1 if s > 0 else -1] * abs(s) + [0] * (Kt - abs(s))
        arms = []
        for v in vals:
            st = qmac._propagate(N_op if v else 0, T, None, N_op, j_dB)
            if v < 0:
                st.x = -st.x
            if ne:
                st = Q.loss_dB(st, ne * (jj + qwave(T)), T)
            arms.append(st)
        off = qmac._propagate(Kt * N_op, T, None, N_op, j_dB)
        st = Q.loss_dB(Q.combine(combine_tree(arms), off, 0.5), jj + qwave(T), T)
        if s == Kt:
            N_top = st.x ** 2 / 2.0
        st = Q.loss_dB(st, fanout_K_dB(2 * Kt, T, jj), T)
        xs.append(st.x)
        Vs.append(st.V)
    V = max(Vs) + qdecode.decoder_amp_noise(T) + v_static(xs[-1] - xs[0], None)
    d = {0: 1.0}
    for _ in range(Kt):
        nd = {}
        for a, pa in d.items():
            for v, pv in ((-1, (1 - pz) / 2), (0, pz), (1, (1 - pz) / 2)):
                nd[a + v] = nd.get(a + v, 0.0) + pa * pv
        d = nd
    return {"p": Q.symbol_error(xs, [d[s] for s in range(-Kt, Kt + 1)], V), "N_top": N_top}


def wallace(heights):
    """Greedy Wallace reduction with 3:2 counters until every column is <= 2 high."""
    h, cnt, stages = dict(heights), {}, 0
    while max(h.values()) > 2:
        stages += 1
        nh = {}
        for c in sorted(h):
            k = h[c] // 3
            cnt[c] = cnt.get(c, 0) + k
            nh[c] = nh.get(c, 0) + h[c] - 2 * k
            nh[c + 1] = nh.get(c + 1, 0) + k
        h = {c: v for c, v in nh.items() if v > 0}
    return cnt, h, stages


def bisect_T(f, target, lo=4.0, hi=400.0, tol=0.01):
    """Highest T in [lo, hi] with f(T) <= target (f increasing in T); None if f(lo) > target."""
    if f(lo) > target:
        return None
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if f(mid) <= target:
            lo = mid
        else:
            hi = mid
    return lo


# ============================================================================ §0
hdr("§0  RELEASED ANCHORS (demonstrated: released calls, unedited chain)")
print(f"N_rail = {N_RAIL:.4f} quanta (x_rail = {X_RAIL:.3f}); eps_one = {qmode.eps_one():.10e}; "
      f"k_dec = {K_DEC:.0f}; E_quantum = {C.E_quantum:.4e} J")
for T in (300.0, 77.0, 4.0):
    print(f"T = {T:5.0f} K: qmac.error_2bit = {qmac.error_2bit(T):.4e}, error_1bit = {qmac.error_1bit(T):.4e}, "
          f"classical_ber = {qerrors.classical_ber(T):.4e}, G_dec = {10*math.log10(qdecode.G_dec(T)):.2f} dB, "
          f"decoder_amp_noise = {qdecode.decoder_amp_noise(T):.4f}, nbar = {C.nbar(T):.4g}, tau_q = {C.tau_q(T)*1e12:.3f} ps")
print(f"results.json: N_op_default = {RQ['N_op_default']}, pulse_energy_rail_aJ = {RQ['pulse_energy_rail_aJ']:.4f}; "
      f"chain dissipation (353 K, operating/upper) = {RC['dissipation_operating_kW_cm2']:.4f}/"
      f"{RC['dissipation_upper_kW_cm2']:.4f} kW/cm^2, hydro_expiry_K = {RC['hydro_expiry_K']:.1f}")

# ============================================================================ §1
hdr("§1  THE K-INPUT COUNTER TILE AND ITS VALIDATION (demonstrated, runnable)")
n_ok = 0
for T in (300.0, 77.0, 4.0):
    for N in (400.0, 800.0):
        for j in (None, 3.0):
            for snr in (None, 20.0):
                for xp in (True, False):
                    a = tile(2, T, N, relaunch=False, xprop=xp, j_dB=j, snr=snr)["p"]
                    b = qmac.error_2bit(T, N, launch_snr_dB=snr, j_dB=j)
                    assert a == b, (T, N, j, snr, xp, a, b)
                    n_ok += 1
print(f"K = 2, quiet launch: tile == released qmac.error_2bit BIT-FOR-BIT at {n_ok} points "
      f"(T 300/77/4 K x N_op 400/800 x junction 1/3 dB x launch quiet/20 dB x both propagation conventions)")
for T in (300.0, 77.0, 4.0):
    assert fanout_K_dB(2, T, qmac.JUNCTION_DB) == qmac.fanout_dB(T)
print("[E2] fanout_K_dB(2) == qmac.fanout_dB at 300/77/4 K (exact)")
for K in (3, 5):
    d = tile(K, 77.0, 400.0)
    gaps = [d["x"][i + 1] - d["x"][i] for i in range(K)]
    print(f"K = {K}: levels equally spaced at 77 K (max gap deviation {max(gaps) - min(gaps):.1e}); "
          f"every arm sees the same path")
for T in (300.0, 77.0):                          # 4 K rates (1e-6 and below) are under 2e6-sample resolution
    d = tile(2, T, 400.0, relaunch=False)
    mc = Q.verify_mc(d["x"], [0.25, 0.5, 0.25], d["V"], nsamp=2_000_000, seed=7)
    d3 = qfa(T)
    mc3 = Q.verify_mc(d3["x"], [1 / 8, 3 / 8, 3 / 8, 1 / 8], d3["V"], nsamp=2_000_000, seed=7)
    print(f"  released verify_mc at {T:3.0f} K: K=2 analytic {d['p']:.4e} vs MC {mc:.4e}; "
          f"QFA-3 (REF) analytic {d3['p']:.4e} vs MC {mc3:.4e} (2e6 samples)")

# ============================================================================ §2
hdr("§2  THE COUNTER FRONTIER AND THE SPLIT LAW (in-model)")
print("conventions: REF = P2 plane, relaunched inputs [E7], quarter-wave per extra level, c = 1/sqrt(12);")
print("             CONS = REF at the P1 plane; PERM = quiet launch, P2, junction-only levels, multiport, c = 0.02")
print("bits removed per decode = K - ceil(log2(K+1)): K=2 -> 0 (half adder), K=3 -> 1 (full adder), K=4 -> 1, "
      "K=5 -> 2, K=6 -> 3, K=7 -> 4")
print(f"{'K':>2} {'N_op P2':>8} {'N_op P1':>8} " + " ".join(f"{('REF %g K' % T):>11}" for T in (4.0, 20.0, 77.0, 300.0))
      + f" {'PERM 4 K':>11}")
FRONT = {}
for K in range(2, 8):
    row = []
    for T in (4.0, 20.0, 77.0, 300.0):
        p = tile(K, T, n_op(K, T, "P2", relaunch=True, xprop=True), relaunch=True, xprop=True)["p"]
        FRONT[(K, T)] = p
        row.append(f"{p:11.3e}")
    pp = tile(K, 4.0, n_op(K, 4.0, "P2", relaunch=False, xprop=False, mp=True),
              relaunch=False, xprop=False, c=0.02, mp=True)["p"]
    FRONT[(K, "PERM")] = pp
    print(f"{K:>2} {n_op(K, 4.0, 'P2', relaunch=True, xprop=True):8.1f} {n_op(K, 4.0, 'P1'):8.1f} "
          + " ".join(row) + f" {pp:11.3e}")
print("\nsplit law (77 K, quiet launch): per-comparator spacing^2 = (2 N_op/K) eta_in eta_extra eta_fo(K); "
      "with the P2 cap it is 2 N_rail eta_fo(K) / K^2 (eta_fo carries the 1/K split, so roughly K^-3)")
for K in (2, 3, 4, 8):
    T = 77.0
    e_in = 10 ** (-qmac.input_transit_dB(T) / 10)
    e_x = 10 ** (-extra_levels(K) * (qmac.JUNCTION_DB + qwave(T)) / 10)
    e_fo = 10 ** (-fanout_K_dB(K, T, qmac.JUNCTION_DB) / 10)
    d = tile(K, T, 400.0, relaunch=False)
    nr = n_op(K, T, "P2", relaunch=False, xprop=True)
    dr = tile(K, T, nr, relaunch=False)
    print(f"  K = {K}: spacing^2 at N_op = 400: {(2*d['half'])**2:9.4f} (formula {2*400/K*e_in*e_x*e_fo:9.4f}); "
          f"at P2: {(2*dr['half'])**2:9.3f} (formula {2*N_RAIL*e_fo/K**2:9.3f})")

# ============================================================================ §3
hdr("§3  HOW TO ENCODE THE TERNARY PRODUCT (in-model)")
print("(a) phase-native signed trits + coherent offset arm [E6], quiet launch, rail at P2:")
for T in (4.0, 77.0):
    for Kt in (1, 2):
        nm = 1000.0 * N_RAIL / signed_tile(Kt, T, 1000.0)["N_top"]
        p = signed_tile(Kt, T, nm)["p"]
        print(f"   T = {T:3.0f} K, K_t = {Kt}: {2*Kt+1} levels on {2*Kt} comparators, N_op = {nm:6.1f}, p = {p:.3e}"
              + ("  (K_t = 1 sums nothing: one trit in, one trit out)" if Kt == 1 else ""))
        OUT[f"signed_Kt{Kt}_{int(T)}K"] = p
    pq = tile(3, T, n_op(3, T, "P2", relaunch=False, xprop=True), relaunch=False)["p"]
    OUT[f"qfa3_quiet_P2_{int(T)}K"] = pq
    print(f"   compare at {T:3.0f} K, same quiet conventions: QFA-3 p = {pq:.3e}")
print("(b) dual-rail balanced ternary, popcount first, then 3^j recombination (5 trits span only +-121:")
print("    int8 needs a 6th trit or a requantisation to 243 levels; both counts below are lower bounds):")
pc_cnt, pc_fin, _ = wallace({0: 32})
n_pc = sum(pc_cnt.values())
for ntr in (5, 6):
    rows = {}
    for j in range(ntr):
        v = 3 ** j
        for k in range(10):
            if (v >> k) & 1:
                for c, hgt in pc_fin.items():
                    rows[c + k] = rows.get(c + k, 0) + 2 * hgt
    rc, _, _ = wallace(rows)
    tot = 2 * ntr * n_pc + sum(rc.values())
    print(f"   {ntr} trits: {2*ntr} rail-planes x {n_pc} counters + {sum(rc.values())} recombination counters "
          f"= {tot} counters per 32-MAC block")
    OUT[f"counters_b5t_{ntr}trits"] = tot
CNT, FIN, STAGES = wallace({b: 32 for b in range(8)})
N_CNT = sum(CNT.values())
CPA_W = max(FIN) + 1
print(f"(c) two's-complement bit columns, ternary weight as a select: {N_CNT} counters, {STAGES} stages, "
      f"{CPA_W}-bit final adder -> (b) costs {OUT['counters_b5t_5trits']/N_CNT:.2f}-"
      f"{OUT['counters_b5t_6trits']/N_CNT:.2f}x more")

# ============================================================================ §4
hdr("§4  THE QFA-3 TILE: OPERATING ENVELOPE (in-model)")
QF = {cv: {} for cv in CONV}
print(f"{'T':>6} | {'REF: N_op':>9} {'half/sig':>8} {'p':>10} | {'CONS: N_op':>10} {'p':>10} | "
      f"{'PERM: N_op':>10} {'p':>10}")
for T in TEMPS:
    r = {}
    for cv, (pl, kw) in CONV.items():
        nn = n_op(3, T, pl, **kw)
        d = tile(3, T, nn, **kw)
        QF[cv][T] = d["p"]
        r[cv] = (nn, d)
    print(f"{T:6.0f} | {r['REF'][0]:9.1f} {r['REF'][1]['half']/math.sqrt(r['REF'][1]['V']):8.2f} "
          f"{r['REF'][1]['p']:10.3e} | {r['CONS'][0]:10.1f} {r['CONS'][1]['p']:10.3e} | "
          f"{r['PERM'][0]:10.1f} {r['PERM'][1]['p']:10.3e}")
for cv in CONV:
    for T in (4.0, 20.0, 77.0):
        OUT[f"qfa3_{cv}_{int(T)}K"] = QF[cv][T]
print("threshold temperatures (p <= target below T):")
for tg in (1e-3, 1e-4, 1e-5, 1e-6):
    s = []
    for cv, (pl, kw) in CONV.items():
        tt = bisect_T(lambda T: tile(3, T, n_op(3, T, pl, **kw), **kw)["p"], tg)
        s.append(f"{cv} {('%.2f K' % tt) if tt else 'none'}")
        OUT[f"qfa3_T_below_{tg:.0e}_{cv}"] = tt
    print(f"   p <= {tg:.0e}: " + ", ".join(s))
print("one-at-a-time sensitivities from REF:")
for T in (4.0, 77.0):
    nr = n_op(3, T, "P2", relaunch=True, xprop=True)
    s = {
        "REF": QF["REF"][T],
        "c = 0.02": qfa(T, c=0.02)["p"],
        "c = 0": qfa(T, c=0.0)["p"],
        "quiet launch (no relaunch noise)": qfa(T, relaunch=False)["p"],
        "junction-only extra levels": qfa(T, xprop=False)["p"],
        "multiport junctions": qfa(T, mp=True)["p"],
        "P1 plane (CONS)": QF["CONS"][T],
        "N_op = 800": tile(3, T, 800.0)["p"],
        "N_op = 400": tile(3, T, 400.0)["p"],
        "-3 dB junctions (rail re-solved)": qfa(T, j_dB=3.0)["p"],
        "inputs one with prob. 1/3": tile(3, T, nr, p1=1 / 3)["p"],
        "+R3, dcrit 0.0289 (07-15)": qfa(T, dcrit=0.0289)["p"],
        "+R3, dcrit 0.089 (rail-clamped)": qfa(T, dcrit=0.089)["p"],
    }
    print(f"   {T:3.0f} K:")
    for k, v in s.items():
        print(f"      {k:36s} {v:.3e}")
    OUT[f"qfa3_sens_{int(T)}K"] = s
print("noise requirements:")
for T in (4.0, 20.0):
    pq = qfa(T, relaunch=False)["p"]
    nr = n_op(3, T, "P2", relaunch=True, xprop=True)
    V0_def = Q.amp(Q.GState(N=0), qdecode.G_dec(T), T).V
    lo, hi = 0.5, V0_def
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if tile(3, T, nr, V0=mid)["p"] > 2 * pq:
            hi = mid
        else:
            lo = mid
    print(f"   {T:3.0f} K: unsaturated '0' output of a regenerative cell: V0 = {V0_def:.3f} "
          f"(sigma = {100*math.sqrt(V0_def)/X_RAIL:.2f} % of the rail swing); keeping p within 2x of the quiet-launch "
          f"value ({pq:.3e}) needs V0 <= {lo:.3f} (sigma <= {100*math.sqrt(lo)/X_RAIL:.2f} % of the swing)")
    OUT[f"zero_sigma_now_pct_{int(T)}K"] = 100 * math.sqrt(V0_def) / X_RAIL
    OUT[f"zero_sigma_max_pct_{int(T)}K"] = 100 * math.sqrt(lo) / X_RAIL
    nq = n_op(3, T, "P2", relaunch=False, xprop=True)
    lo2, hi2 = 0.0, 120.0
    for _ in range(80):
        mid = 0.5 * (lo2 + hi2)
        if tile(3, T, nq, relaunch=False, snr=mid)["p"] > 2 * pq:
            lo2 = mid
        else:
            hi2 = mid
    print(f"         comb-launched (quiet) '1' amplitude jitter, released additive convention: p within 2x needs "
          f"S >= {hi2:.2f} dB, sigma_rel <= {100*10**(-hi2/20):.3f} %; at the coded 20 dB p = "
          f"{tile(3, T, nq, relaunch=False, snr=20.0)['p']:.3e}")
    OUT[f"launch_sigma_rel_max_pct_{int(T)}K"] = 100 * 10 ** (-hi2 / 20)
nr4 = n_op(3, 4.0, "P2", relaunch=True, xprop=True)
print(f"relaunch attenuation rail -> N_op(REF) = {10*math.log10(N_RAIL/nr4):.2f} dB; pulse energy at "
      f"{nr4:.0f} quanta = {nr4*C.E_quantum*1e18:.3f} aJ; -3 dB junctions re-solve the P2 rail to N_op = "
      f"{n_op(3, 4.0, 'P2', relaunch=True, xprop=True, j_dB=3.0):.1f}")
OUT["qfa3_N_op_REF_cold"] = nr4

# ============================================================================ §5
hdr("§5  THE LANE: 32-wide int8 x ternary block sum as a Wallace tree (in-model)")
K_DOT, BLK = 5120, 32
NB = K_DOT // BLK
P0 = 1 / 3                                       # ASSUMPTION: share of zero weights
print(f"tree: {N_CNT} 3:2 counters over {STAGES} stages; per column {dict(sorted(CNT.items()))}; "
      f"{CPA_W}-bit digital ripple adder")


def q80(x):
    """Q8_0-style absmax-per-32 quantiser: returns int8 values and scales."""
    xb = x.reshape(-1, 32)
    sc = np.abs(xb).max(1, keepdims=True) / 127.0
    return np.rint(xb / sc).astype(np.int64).reshape(x.shape), sc


YS, A2 = {}, {}
for dist in ("gauss", "t4"):
    r = np.random.default_rng(7)
    for K in (5120, 17408):
        s, e, a2 = 0.0, 0.0, []
        for _ in range(200):
            x = r.standard_t(4, K) if dist == "t4" else r.normal(0, 1, K)
            wv = r.choice([-1, 0, 1], size=K, p=[(1 - P0) / 2, P0, (1 - P0) / 2])
            qi, sc = q80(x)
            xq = (qi.reshape(-1, 32) * sc).reshape(-1)
            y = (wv * x).sum()
            s += y * y
            e += ((wv * xq).sum() - y) ** 2
            a2.append(np.mean(qi.astype(float) ** 2))
        YS[(K, dist)] = 10 * math.log10(s / e)
        if K == 5120:
            A2[dist] = float(np.mean(a2))
print("tolerance proxy (the model's own tolerance is open): dot-product SNR of the runtime's own Q8_0 "
      "quantisation (absmax per 32, ternary weights): " + ", ".join(f"K={K} {d} {v:.1f} dB" for (K, d), v in YS.items()))
print(f"int8 activation rms under that quantiser: gauss {math.sqrt(A2['gauss']):.1f}, t4 {math.sqrt(A2['t4']):.1f} LSB "
      f"(the first draft's 127/4 = 31.75 understated the signal)")
OUT["q80_yardstick_dB"] = {f"{K}_{d}": v for (K, d), v in YS.items()}
TARGET = 41.0      # analog error power no larger than the yardstick's quantisation error
SIG = {d: K_DOT * (1 - P0) * A2[d] for d in A2}


def lane_snr(p_q, p_d, bstar, dist="t4"):
    ev = sum(n * (p_q if c <= bstar else p_d) * 4 ** c for c, n in CNT.items())
    ev += sum(p_d * 4 ** c for c in range(CPA_W))               # digital ripple adder
    ev *= NB
    return 10 * math.log10(SIG[dist] / ev) if ev > 0 else float("inf")


rng = np.random.default_rng(20261003)
NTR = 20000
w = rng.choice([-1, 0, 1], size=(NTR, BLK), p=[(1 - P0) / 2, P0, (1 - P0) / 2])
a_int, _ = q80(rng.normal(0, 1, NTR * BLK))
a = a_int.reshape(NTR, BLK)
exact = (w * a).sum(1)
a8 = a & 0xFF
sel = np.where(w == 1, a8, np.where(w == -1, (~a8) & 0xFF, 0))        # (p AND a) OR (n AND NOT a)
n_neg = (w == -1).sum(1)


def run_tree(t_err):
    col = {b: [((sel[:, i] >> b) & 1) ^ (1 if b == 7 else 0) for i in range(BLK)] for b in range(8)}
    occ, ana = np.zeros(4), 0.0
    while max(len(v) for v in col.values()) > 2:
        nxt = {}
        for c in sorted(col):
            bits = col[c]
            k = len(bits) // 3
            for i in range(k):
                s = bits[3 * i] + bits[3 * i + 1] + bits[3 * i + 2]
                occ += np.bincount(s, minlength=4)
                ana += 4 ** c * float(np.mean(((s > 0).astype(float) + (s < 3)) * t_err))
                if t_err > 0:
                    rr = rng.random(NTR)
                    s = s + ((rr < t_err) & (s < 3)).astype(np.int64) - ((rr >= 1 - t_err) & (s > 0)).astype(np.int64)
                nxt.setdefault(c, []).append(s & 1)
                nxt.setdefault(c + 1, []).append(s >> 1)
            nxt.setdefault(c, []).extend(bits[3 * k:])
        col = nxt
    total = sum((2 ** c) * sum(b) for c, b in col.items())
    return total + n_neg - BLK * 2 ** 7, occ / occ.sum(), ana


tot0, occ, _ = run_tree(0.0)
assert np.array_equal(tot0, exact), "tree is not exact"
print(f"functional tree exact on {NTR} random blocks: select = one's complement for w = -1, sign bit inverted, "
      f"block constants (+n_neg, -32*128) applied in CMOS")
print(f"measured counter-level occupancy (s=0..3): {np.round(occ, 4)} vs Binomial(3,1/2) [0.125 0.375 0.375 0.125]")
t_mc = 2e-3
tot, _, ana = run_tree(t_mc)
err = (tot - exact).astype(float)
p_eff = sum(occ[s] * t_mc * ((s > 0) + (s < 3)) for s in range(4))
p_bin = t_mc * 1.75
print(f"error model check at per-boundary tail {t_mc}: MC variance/block {err.var():.1f} (mean {err.mean():+.3f}) vs "
      f"analytic sum of 4^c E[err^2] {ana:.1f} (ratio {err.var()/ana:.3f}); occupancy p {p_eff:.3e} vs Binomial p "
      f"{p_bin:.3e} (budget conservative by x{p_bin/p_eff:.3f})")
bias = (NB * err.mean()) ** 2 / (NB * err.var() + (NB * err.mean()) ** 2)
print(f"coherent bias over {NB} blocks at this inflated rate: {bias:.2%} of the error power (scales with p)")

P_D_A = {T: 11 * qerrors.classical_ber(T) for T in TEMPS}         # booking A: 11 decisions per digital FA
print(f"\ndot-product SNR at K = {K_DOT} (Q8_0-quantised activations, 1/3 zero weights; t4 / gauss), target {TARGET:.0f} dB:")
BSTAR = {}
for cv in CONV:
    print(f"   {cv}:")
    for T in TEMPS:
        pq = QF[cv][T]
        res = []
        for dist in ("t4", "gauss"):
            allq = lane_snr(pq, P_D_A[T], 99, dist)
            bs = max([b for b in range(-1, 13) if lane_snr(pq, P_D_A[T], b, dist) >= TARGET] or [-1])
            res.append((allq, bs, sum(n for c, n in CNT.items() if c <= bs)))
        BSTAR[(cv, T)] = res[0][1:]
        print(f"      {T:5.0f} K: all-QFA tree {res[0][0]:6.1f} / {res[1][0]:6.1f} dB | b* = {res[0][1]:2d} / "
              f"{res[1][1]:2d} -> analog counters {res[0][2]:3d} / {res[1][2]:3d} of {N_CNT}")
        OUT[f"lane_{cv}_{int(T)}K"] = {"snr_allqfa_t4": res[0][0], "snr_allqfa_gauss": res[1][0],
                                      "bstar_t4": res[0][1], "nqfa_t4": res[0][2]}

FA_REC, FA_ALN, QFA_C, HYB = 15, 18, 12, 4
SEL, FAN = BLK * 8 * 4, BLK * 2 * 6
RS = (1 + 1 / 24, 1 + 1 / 10)


def lane_cells(n_qfa, fa=FA_REC, qc=QFA_C, hyb=0, sel=True, hi=False):
    mixed = 0 < n_qfa < N_CNT
    base = (SEL + FAN if sel else 0) + n_qfa * (qc + (hyb if mixed else 0)) + (N_CNT - n_qfa) * fa + CPA_W * fa
    return base * RS[1 if hi else 0]


ACC = {
    "record idiom (FA 15, QFA 12, select on fabric)": dict(),
    "+ hybrid QFA->FA alignment (+4 per QFA)": dict(hyb=HYB),
    "FA 18 (wave-pipelined composition)": dict(fa=FA_ALN),
    "FA 18 + select in CMOS": dict(fa=FA_ALN, sel=False),
}
print(f"\ncommon cells: select stage {SEL} (4 per product bit), weight fan-out {FAN}, {CPA_W}-bit ripple adder, "
      f"re-sync every 24..10 gates")
print("cell saving vs the all-digital lane at the SAME temperature, per accounting (REF, t4 b*):")
LANES = {"TQ-4 (4 K)": 4.0, "TQ-20 (20 K)": 20.0, "TQ-77 (77 K)": 77.0}
SAVE = {}
for acc, kw in ACC.items():
    row = []
    for name, T in LANES.items():
        nq = BSTAR[("REF", T)][1]
        sv = 1 - lane_cells(nq, **kw) / lane_cells(0, **kw)
        SAVE[(acc, name)] = sv
        row.append(f"{name} {sv:+7.2%} ({nq} QFA)")
    print(f"   {acc:48s}: " + "; ".join(row))
for name in LANES:
    vals = [SAVE[(acc, name)] for acc in ACC]
    OUT[f"cell_saving_range_{name.split()[0]}"] = [min(vals), max(vals)]
print("same accounting with every counter analog (the most an all-QFA tree could save, if its errors allowed it):")
for acc, kw in ACC.items():
    print(f"   {acc:48s}: {1 - lane_cells(N_CNT, **kw) / lane_cells(0, **kw):+7.2%}")
d_lo, d_hi = lane_cells(0), lane_cells(0, hi=True)
print(f"all-digital lane (record idiom): {d_lo:.0f}-{d_hi:.0f} cells, {d_lo*12*16/7/1e6:.3f}-{d_hi*12*16/7/1e6:.3f} mm^2")

# ============================================================================ §6
hdr("§6  COOLING, SYSTEM AND THE BOOKING FORK (in-model / arithmetic)")
TAU353 = C.tau_q(353.0)


def p_cell(T, upper=False):
    """[E8] W per biased cell: chain's 353 K value scaled as tau^-3 (tracked bias)."""
    base = RC["dissipation_upper_kW_cm2" if upper else "dissipation_operating_kW_cm2"] * 1e3 * 1e-8
    return base * (TAU353 / C.tau_q(T)) ** 3


print(f"per-cell dissipation [E8]: 353 K {p_cell(353.0)*1e6:.2f} uW (the chain's stored value), 300 K "
      f"{p_cell(300.0)*1e6:.2f}-{p_cell(300.0, True)*1e6:.2f} uW, <=150 K {p_cell(77.0)*1e6:.3f} uW "
      f"(ratio to 300 K: {p_cell(77.0)/p_cell(300.0):.4f}); uncertified below ~255 K (Part II section 1)")
print(f"all-digital lane at 300 K: {d_lo*p_cell(300.0)*1e3:.1f}-{d_hi*p_cell(300.0, True)*1e3:.1f} mW")
W = {T: (300.0 - T) / T for T in (77.0, 20.0, 4.0)}
print("Carnot work per watt removed (300 K ambient): " + ", ".join(f"{T:.0f} K {W[T]:.3f}" for T in W))
print("wall-plug power relative to the warm all-digital lane (record-idiom cells):")
print(f"   {'lane':14s} {'equal dissipation, Carnot':>26s} {'Joule model, Carnot':>20s} "
      f"{'Joule model: Carnot fraction needed':>36s}")
for name, T in list(LANES.items()) + [("digital @77 K", 77.0)]:
    nq = BSTAR[("REF", T)][1] if name.startswith("TQ") else 0
    cr = lane_cells(nq) / lane_cells(0)
    eq = cr * (1 + W[T])
    jm = cr * (p_cell(T) / p_cell(300.0)) * (1 + W[T])
    need = W[T] / (1 / (cr * p_cell(T) / p_cell(300.0)) - 1)
    print(f"   {name:14s} {eq:26.2f} {jm:20.3f} {('%.1f %%' % (100*need)) if need <= 1 else 'beyond Carnot':>36s}")
    OUT[f"wallplug_{name.split()[0]}"] = {"equal": eq, "joule": jm, "carnot_fraction_needed": need}
print("(any cold win is a cooling win: the cold all-digital lane needs about the same cooler as the analog hybrid)")
print("break-even cold-cell dissipation ratio r = P_cell(77 K)/P_cell(300 K) vs cooler efficiency (fraction of Carnot);")
print(f"the Joule model [E8] predicts r = {p_cell(77.0)/p_cell(300.0):.3f}:")
for name, nq in (("TQ-77", BSTAR[("REF", 77.0)][1]), ("digital @77 K", 0)):
    cr = lane_cells(nq) / lane_cells(0)
    print(f"   {name:14s}: " + ", ".join(f"{int(100*eta)} % -> r <= {1/(cr*(1 + W[77.0]/eta)):.4f}"
                                        for eta in (1.0, 0.4, 0.3, 0.2, 0.1)))
    OUT[f"r_max_{name.split()[0]}"] = {eta: 1 / (cr * (1 + W[77.0] / eta)) for eta in (1.0, 0.4, 0.3, 0.2, 0.1)}

MATS = [(10240, 5120, 48), (6144, 5120, 48), (5120, 6144, 48), (12288, 5120, 16), (1024, 5120, 16),
        (1024, 5120, 16), (5120, 6144, 16), (17408, 5120, 64), (17408, 5120, 64), (5120, 17408, 64),
        (248320, 5120, 1)]
MACS = sum(n * k * c for n, k, c in MATS)
STREAM_B = 5_668_531_648            # PTQ1_0 bytes streamed per token (external input)
F_SLOT = 69e9                        # gated F = 2 frontier (notes/2026-07-31, in-model); unmodelled cold
tps_lane = BLK * F_SLOT / MACS
print(f"\nsystem (external workload inputs): {MACS:,d} ternary MACs/token, {STREAM_B/1e9:.3f} GB/token streamed; "
      f"one lane = {tps_lane:.2f} tok/s at {F_SLOT/1e9:.0f} GHz")
for bw in (0.5e12, 1e12, 3e12):
    tps = bw / STREAM_B
    nl = math.ceil(tps / tps_lane)
    print(f"   {bw/1e12:.1f} TB/s -> {tps:6.1f} tok/s (memory-bound) -> {nl} lanes; operand launch "
          f"{nl*(BLK*2 + BLK*8)*F_SLOT/1e12:.1f} Tb/s (320 lines/lane; no on-fabric storage)")
print(f"   lane cells at 300 K, full utilisation: {lane_cells(0)*p_cell(300.0)/tps_lane*1e3:.2f} mJ/token; "
      f"in-fabric photons at {nr4:.0f} quanta, 10 bits/MAC, 50 % ones: {MACS*5*nr4*C.E_quantum*1e6:.3f} uJ/token")

print("\nbooking fork for the digital lane's decisions:")
print("   A = released qerrors.classical_ber (rail restored after every split, Part I); "
      "B = this note's [E4]/[E7] QMAC calculus applied to a rail-referenced half-adder decode (an in-model reading)")
P_HA_B = {T: tile(2, T, n_op(2, T, "P2", relaunch=True, xprop=True), relaunch=True, xprop=True)["p"] for T in TEMPS}
for T in TEMPS:
    print(f"   {T:5.0f} K: A {qerrors.classical_ber(T):.3e} | B {P_HA_B[T]:.3e} | all-digital lane SNR (t4, incl. ripple adder) "
          f"A {lane_snr(0, P_D_A[T], -1):7.1f} dB, B {lane_snr(0, 2 * P_HA_B[T], -1):7.1f} dB")
tb = bisect_T(lambda T: -lane_snr(0, 2 * tile(2, T, n_op(2, T, "P2", relaunch=True, xprop=True),
                                               relaunch=True, xprop=True)["p"], -1), -TARGET)
print(f"   under B the all-digital lane meets {TARGET:.0f} dB only below {tb:.1f} K")
OUT["dref_T_meets_target_bookingB_K"] = tb
OUT["ha_decode_bookingB_300K"] = P_HA_B[300.0]

# ============================================================================ §7
hdr("§7  PRE-REGISTERED PREDICTIONS (new key names; contest no results.json value)")
PRED = {
    "qfa3_err_4K_p2_relaunch_c0289": OUT["qfa3_REF_4K"],
    "qfa3_err_20K_p2_relaunch_c0289": OUT["qfa3_REF_20K"],
    "qfa3_err_77K_p2_relaunch_c0289": OUT["qfa3_REF_77K"],
    "qfa3_err_4K_p1_relaunch_c0289": OUT["qfa3_CONS_4K"],
    "qfa3_err_4K_p2_quiet_c002_multiport": OUT["qfa3_PERM_4K"],
    "qfa3_N_op_p2_relaunch_cold": OUT["qfa3_N_op_REF_cold"],
    "qfa3_T_below_1e-4_p2_relaunch_c0289_K": OUT["qfa3_T_below_1e-04_REF"],
    "relaunch_zero_sigma_max_pct_4K": OUT["zero_sigma_max_pct_4K"],
    "tq_allqfa_snr_dB_4K_p2_relaunch_t4": OUT["lane_REF_4K"]["snr_allqfa_t4"],
    "tq_bstar_77K_p2_relaunch_t4": OUT["lane_REF_77K"]["bstar_t4"],
    "tq77_carnot_fraction_needed_joule": OUT["wallplug_TQ-77"]["carnot_fraction_needed"],
    "ha_decode_error_bookingB_300K": OUT["ha_decode_bookingB_300K"],
}
clash = sorted((set(PRED) & set(RQ)) | (set(PRED) & set(RC)))
assert not clash, clash
for k, v in PRED.items():
    print(f"   {k:42s} = {v!r}")
print("no key collides with fable-model-quantum/ or fable-model-chain/ results.json")
print("\nreleased chains imported read-only; nothing written to the repository")
