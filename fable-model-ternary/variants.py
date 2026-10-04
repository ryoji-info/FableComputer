# -*- coding: utf-8 -*-
"""Part III, Section 8: the levers — what a fabric-side alternative and a model-side
fine-tuning each buy on the digital lane. Companion to The Fable Computer, Part III.

Run from anywhere inside the repository (or with FABLE_REPO=<repo root>):
    python variants.py           # Python 3 + numpy, about 16 s
The released chains are imported READ-ONLY (no bytecode written, nothing edited,
run_all.py never imported or run). variants.out next to this file is the reference
output.

What is the record's and what is this script's:
  * record: the static-noise-margin law (fable-model-chain cell.static_noise_margin),
    the classical decision BER (fable-model-quantum qerrors.classical_ber), the matched
    amplifier noise (qdecode.G_dec, qconstants.nbar), the junction budget
    (qmac.JUNCTION_DB), the F = 2 softening k_eff = 8 F^-1/2 (notes/2026-07-21).
  * digital_lane_bonsai.py (this folder): the reference lane [D1] at 32 x 8 bits, its
    bookings A0-A3 [D5], the Q8_0 yardstick and the per-unit-BER error variance kappa.
  * this script, labelled [V1]-[V5] (all in-model, none in the record):
    [V1] the lane generalised to b activation bits and block width W (same netlist
         idiom: select, fan-out, greedy Wallace tree of 3:2 counters, ripple adder);
    [V2] a native threshold full adder (TFA): carry = MAJ3 as one enhancing-coupled
         threshold cell, sum = one threshold cell with enhancing a, b, c and a
         depleting (inhibitory) coupling of weight 2 from the carry, plus three
         alignment buffers -- 5 biased cells, depth 2, against the record idiom's
         2 HA + OR = 15 biased cells, depth 7. Part I section 5 supplies the
         ingredients (threshold on a sum of input fields; depleting coupling); the
         3-input fan-in and the weighted inhibitory input are NOT in the record;
    [V3] the yardstick for b-bit activations: the same absmax-per-32 quantiser at
         b bits (Q8_0 at b = 8), K = 5120, Student-t (nu = 4) and Gaussian activations,
         1/3 zero weights -- an assumption, as in the reference lane;
    [V4] kappa_b by gate-level emulation with injected decision flips (the reference
         lane's [D2] at b bits), and the resulting per-decision ceiling;
    [V5] the tolerance lever: the pass temperatures of bookings A0-A3 when the model
         tolerates fabric error power equal to 1x, 10x and 100x its own quantisation
         error (what an error-aware fine-tuning would have to deliver).
"""
import json
import math
import os
import sys
import time

sys.dont_write_bytecode = True


def _repo_root():
    if os.environ.get("FABLE_REPO"):
        return os.environ["FABLE_REPO"]
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "fable-model-quantum")):
            return d
        d = os.path.dirname(d)
    raise SystemExit("run inside the FableComputer repository or set FABLE_REPO")


ROOT = _repo_root()
sys.path.insert(0, os.path.join(ROOT, "fable-model-quantum"))
sys.path.insert(1, os.path.join(ROOT, "fable-model-chain"))
import numpy as np        # noqa: E402
import qconstants as QC   # noqa: E402
import qdecode            # noqa: E402
import qerrors            # noqa: E402
import qmac               # noqa: E402
import qnoise as Q        # noqa: E402
import cell as CELL       # noqa: E402

RC = json.load(open(os.path.join(ROOT, "fable-model-chain", "results.json"), encoding="utf-8"))
RQ = json.load(open(os.path.join(ROOT, "fable-model-quantum", "results.json"), encoding="utf-8"))
X_RAIL = math.sqrt(2 * qerrors.N_RAIL)
KE = 8 / math.sqrt(2)
JN = 10 ** (-qmac.JUNCTION_DB / 20)
F_SLOT = 69e9
P0 = 1 / 3                                   # ASSUMPTION: share of zero weights
K_DOT = 5120
MACS = 25_598_361_600                        # per token (digital_lane_bonsai.py section 1)
AREA_CELL = 12 * 16 / 7                      # um^2 per lattice site, Part I Table 5 idiom


def hdr(s):
    print("\n" + "=" * 100 + "\n" + s + "\n" + "=" * 100)


# --------------------------------------------------------------------------- [V1] the lane at (b, W)
def wallace(heights):
    """Greedy 3:2 reduction; returns counters per column, final heights, stages."""
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


def fanout_cells(leaves):
    """Cells of a fan-out-2 buffer tree delivering one launched bit to `leaves` consumers."""
    n, level = 0, 1
    while level < leaves:
        level *= 2
        n += level
    return n


IDIOM = {"record (2 HA + OR)": 15, "aligned (wave-pipelined composition)": 18, "TFA [V2]": 5}


def lane(b=8, W=32, idiom="record (2 HA + OR)", select_on_fabric=True):
    cnt, fin, stages = wallace({c: W for c in range(b)})
    n_fa = sum(cnt.values())
    width = max(fin) + 1
    fa_cells = IDIOM[idiom]
    sel = W * b * 4 + W if select_on_fabric else 0                 # 4 cells per product bit + sign NOT
    fan = W * 2 * fanout_cells(math.ceil(b / 2)) if select_on_fabric else 0
    tree = (n_fa + width) * fa_cells
    out_bits = math.ceil(math.log2(W * (2 ** b - 1) + 1))
    return {"b": b, "W": W, "idiom": idiom, "select": select_on_fabric, "counters": n_fa, "stages": stages,
            "adder_bits": width, "sel_cells": sel, "fan_cells": fan, "tree_cells": tree,
            "logic_cells": sel + fan + tree, "out_bits": out_bits, "per_column": dict(sorted(cnt.items()))}


def launched_bits_per_mac(b, W, L, select_on_fabric=True):
    """Operand launch per MAC with L lanes sharing one activation block [D4]: weights 2 bits
    per MAC per lane, activations b bits per MAC shared; products b bits per MAC per lane."""
    if select_on_fabric:
        return (2 * W * L + b * W) / (W * L)
    return (b * W * L) / (W * L)                                   # products launched, nothing shared


# --------------------------------------------------------------------------- [V3] yardstick at b bits
def quant(x, b, blk=32):
    xb = x.reshape(-1, blk)
    m = 2 ** (b - 1) - 1
    d = (np.abs(xb).max(1) / m).astype(np.float16).astype(np.float64)
    q = np.clip(np.rint(xb / d[:, None]), -m, m).astype(np.int64)
    return q, d


def yardstick(b, dist="t4", n=4000, seed=7):
    """Dot-product SNR of the b-bit quantiser alone at K = 5120 (returns SNR dB, signal in int^2)."""
    r = np.random.default_rng(seed)
    s_y, e_q, e_d = 0.0, 0.0, 0.0
    for _ in range(n):
        x = r.standard_t(4, K_DOT) if dist == "t4" else r.normal(0, 1, K_DOT)
        wv = r.choice([-1, 0, 1], size=K_DOT, p=[(1 - P0) / 2, P0, (1 - P0) / 2])
        q, d = quant(x, b)
        y = (wv * x).sum()
        yq = ((wv.reshape(-1, 32) * q).sum(1) * d).sum()
        s_y += y * y
        e_q += (yq - y) ** 2
        e_d += np.mean(d ** 2)
    return 10 * math.log10(s_y / e_q), s_y / e_d


# --------------------------------------------------------------------------- [V4] kappa_b by emulation
class Flip:
    def __init__(self, p, rng):
        self.p, self.rng, self.n = p, rng, 0

    def __call__(self, x):
        if self.p <= 0:
            return x
        f = self.rng.random(x.shape) < self.p
        self.n += int(f.sum())
        return x ^ f.astype(x.dtype)


def ha(a, b, fl):
    o = fl(a | b)
    c = fl(a & b)
    nc = fl(1 - c)
    od = fl(o)
    s = fl(od & nc)
    return s, fl(fl(c))


def fa(a, b, cin, fl):
    s1, c1 = ha(a, b, fl)
    s, c2 = ha(s1, cin, fl)
    return s, fl(c1 | c2)


def lane_blocks(w, q, fl, b):
    """The reference netlist [D1] at b activation bits: 13-bit-class tree output per block."""
    m = (1 << b) - 1
    ab = (q & m).astype(np.int64)
    p = (w == 1).astype(np.uint8)
    nn = (w == -1).astype(np.uint8)
    leaves = math.ceil(b / 2)

    def fan(v):
        cur = [v]
        while len(cur) < leaves:
            cur = [fl(x) for x in cur for _ in (0, 1)]
        return [cur[i // 2] for i in range(b)]
    P, N = fan(p), fan(nn)
    cols = {}
    for i in range(b):
        abit = ((ab >> i) & 1).astype(np.uint8)
        x = fl(fl(P[i] & abit) | fl(N[i] & fl(1 - abit)))
        if i == b - 1:
            x = fl(1 - x)
        cols[i] = [x[:, j] for j in range(w.shape[1])]
    while max(len(v) for v in cols.values()) > 2:
        nxt = {}
        for c in sorted(cols):
            bits = cols[c]
            k = len(bits) // 3
            for j in range(k):
                s, co = fa(bits[3 * j], bits[3 * j + 1], bits[3 * j + 2], fl)
                nxt.setdefault(c, []).append(s)
                nxt.setdefault(c + 1, []).append(co)
            nxt.setdefault(c, []).extend(bits[3 * k:])
        cols = nxt
    width = max(cols) + 1
    zero = np.zeros_like(cols[0][0])
    A = [cols[c][0] if len(cols.get(c, [])) > 0 else zero for c in range(width)]
    B = [cols[c][1] if len(cols.get(c, [])) > 1 else zero for c in range(width)]
    carry, out = zero, np.zeros(zero.shape, dtype=np.int64)
    for c in range(width):
        s, carry = fa(A[c], B[c], carry, fl)
        out += s.astype(np.int64) << c
    return out + (carry.astype(np.int64) << width)


def kappa(b, ber=2e-5, N=1024, K=K_DOT, seed=11):
    """Block-sum error variance per unit decision BER, and the BER = 0 exactness check."""
    r = np.random.default_rng(seed)
    W = r.choice(np.array([-1, 0, 1], dtype=np.int8), size=(N, K), p=[(1 - P0) / 2, P0, (1 - P0) / 2])
    x = r.normal(0, 1, K)
    q, _ = quant(x, b)
    nb = K // 32
    wb = W.reshape(-1, 32)
    qb = np.broadcast_to(q, (N, nb, 32)).reshape(-1, 32)
    exact = (wb.astype(np.int64) * qb).sum(1)
    const = (wb == -1).sum(1) - 32 * (1 << (b - 1))
    got0 = lane_blocks(wb, qb, Flip(0.0, r), b) + const
    assert np.array_equal(got0, exact), f"lane at b = {b} is not exact"
    fl = Flip(ber, r)
    got = lane_blocks(wb, qb, fl, b) + const
    dv = (got - exact).astype(float)
    return float(np.var(dv)) / ber, fl.n, len(exact)


# --------------------------------------------------------------------------- [D5] bookings, as released
def ber_booking(T, k, swing):
    V = (2 - 1 / qdecode.G_dec(T)) * (QC.nbar(T) + 0.5)
    return Q.tail(CELL.static_noise_margin(k) * X_RAIL * swing, V)


BOOK = {
    "A0 released (k 8, full rail)": lambda T: qerrors.classical_ber(T),
    "A1 F=2 k_eff, full rail": lambda T: ber_booking(T, KE, 1.0),
    "A2 A1 + split swing (-3 dB)": lambda T: ber_booking(T, KE, 1 / math.sqrt(2)),
    "A3 A2 + one junction (-1 dB)": lambda T: ber_booking(T, KE, JN / math.sqrt(2)),
}


def t_max(f, target, lo=4.0, hi=400.0):
    if f(lo) > target:
        return None
    if f(hi) <= target:
        return hi
    while hi - lo > 0.1:
        mid = 0.5 * (lo + hi)
        if f(mid) <= target:
            lo = mid
        else:
            hi = mid
    return lo


def fmt_T(t):
    return "never" if t is None else ("above 400 K" if t >= 400 else f"{t:.0f} K")


if __name__ == "__main__":
    T0 = time.time()
    hdr("§1  THE LANE AT b ACTIVATION BITS AND BLOCK WIDTH W [V1][V2] (in-model)")
    ref = lane()
    print(f"reference lane (b = 8, W = 32, record idiom): {ref['counters']} counters in {ref['stages']} stages, "
          f"{ref['adder_bits']}-bit adder, {ref['logic_cells']} logic cells "
          f"(select {ref['sel_cells']}, fan-out {ref['fan_cells']}, adders {ref['tree_cells']}); "
          f"{ref['out_bits']} output bits -- matches digital_lane_bonsai.py section 2")
    print("\nactivation bits b (W = 32):")
    print(f"{'b':>3} {'counters':>9} {'stages':>7} {'adder':>6} {'out bits':>9} | logic cells: "
          f"{'record':>7} {'aligned':>8} {'TFA':>6} {'TFA, select in CMOS':>20} | launched bits/MAC at L = 2/3/7")
    for b in (8, 6, 4, 2):
        rows = [lane(b, 32, idm) for idm in IDIOM]
        tfa_cmos = lane(b, 32, "TFA [V2]", select_on_fabric=False)
        lb = "/".join(f"{launched_bits_per_mac(b, 32, L):.2f}" for L in (2, 3, 7))
        print(f"{b:>3} {rows[0]['counters']:>9} {rows[0]['stages']:>7} {rows[0]['adder_bits']:>6} "
              f"{rows[0]['out_bits']:>9} | {rows[0]['logic_cells']:>19} {rows[1]['logic_cells']:>8} "
              f"{rows[2]['logic_cells']:>6} {tfa_cmos['logic_cells']:>20} | {lb}")
    print("\nblock width W (b = 8, record idiom):")
    print(f"{'W':>4} {'counters':>9} {'stages':>7} {'adder':>6} {'out bits':>9} {'logic cells':>12} "
          f"{'cells/MAC':>10} {'readout bits/MAC':>17} {'CMOS scaling GFLOP/token':>25}")
    for W in (32, 64, 128):
        d = lane(8, W)
        print(f"{W:>4} {d['counters']:>9} {d['stages']:>7} {d['adder_bits']:>6} {d['out_bits']:>9} "
              f"{d['logic_cells']:>12} {d['logic_cells']/W:>10.1f} {d['out_bits']/W:>17.3f} "
              f"{3*MACS/W/1e9:>25.2f}")
    print("\n[V2] the native threshold full adder: carry = MAJ3 (one threshold cell, enhancing a, b, c, high "
          "threshold); sum = one threshold cell with enhancing a, b, c and a depleting coupling of weight 2 from the "
          "carry; three alignment buffers; 5 biased cells, depth 2. The record's full adder is 2 HA + OR = 15 biased "
          "cells, depth 7. Neither the 3-input fan-in nor the weighted inhibitory input is in the record (open).")

    hdr("§2  THE YARDSTICK AND THE CEILING AT b BITS [V3][V4] (in-model; emulation runnable)")
    print("yardstick = dot-product SNR of the b-bit absmax-per-32 quantiser alone (K = 5120, 4,000 dot products, "
          "1/3 zero weights); kappa_b = block-sum error variance per unit decision BER (gate-level emulation, "
          "1,024 x 5,120 rows, BER 2e-5); ceiling = BER at which the lane's error power equals the quantiser's")
    NB = K_DOT // 32
    CEIL = {}
    print(f"{'b':>3} {'SNR t4':>8} {'SNR gauss':>10} {'kappa_b':>10} {'flips':>8} {'blocks':>8} "
          f"{'ceiling t4':>12} {'ceiling gauss':>14}")
    for b in (8, 6, 4, 2):
        ys_t, sig_t = yardstick(b, "t4")
        ys_g, sig_g = yardstick(b, "gauss")
        kap, nfl, nbl = kappa(b)
        c_t = sig_t / (NB * kap * 10 ** (ys_t / 10))
        c_g = sig_g / (NB * kap * 10 ** (ys_g / 10))
        CEIL[b] = (c_t, c_g, ys_t, ys_g, kap)
        print(f"{b:>3} {ys_t:>8.1f} {ys_g:>10.1f} {kap:>10.2e} {nfl:>8,d} {nbl:>8,d} {c_t:>12.1e} {c_g:>14.1e}")
    print("(b = 8 reproduces the reference lane's 42.5 dB / 45.5 dB yardstick, kappa 2.8e8 within its 13 % spread, "
          "and the 6.3e-9 ceiling; lower-bit activations relax the ceiling because the model's own quantisation "
          "error grows faster than the lane's error weights shrink)")

    hdr("§3  PASS TEMPERATURES OF THE BOOKINGS AT b BITS, AND THE TOLERANCE LEVER [V5] (in-model)")
    print("highest temperature at which each booking's per-decision BER stays below the ceiling (t4 yardstick)")
    print(f"{'booking':32s} " + " ".join(f"{('b = %d' % b):>12}" for b in (8, 6, 4, 2)))
    for name, f in BOOK.items():
        print(f"{name:32s} " + " ".join(f"{fmt_T(t_max(f, CEIL[b][0])):>12}" for b in (8, 6, 4, 2)))
    print("\ntolerance lever at b = 8: the model tolerates fabric error power equal to 1x / 10x / 100x its Q8_0 error "
          "(an error-aware fine-tuning target, not a record quantity)")
    print(f"{'booking':32s} {'1x':>12} {'10x':>12} {'100x':>12}")
    for name, f in BOOK.items():
        print(f"{name:32s} " + " ".join(f"{fmt_T(t_max(f, CEIL[8][0] * m)):>12}" for m in (1, 10, 100)))
    print("\nlane digital-error SNR at 300 K and 353 K for 10x / 100x tolerance is unchanged (the lane is the same); "
          "what moves is the pass line: 42.5 -> 32.5 -> 22.5 dB")

    hdr("§4  SUMMARY KEYS (new names; contest no results.json value)")
    PRED = {
        "p3_counters_b8_W32": ref["counters"],
        "p3_logic_cells_b8_W32_record": ref["logic_cells"],
        "p3_logic_cells_b4_W32_record": lane(4)["logic_cells"],
        "p3_logic_cells_b8_W32_TFA": lane(8, 32, "TFA [V2]")["logic_cells"],
        "p3_logic_cells_b4_W32_TFA_selectCMOS": lane(4, 32, "TFA [V2]", False)["logic_cells"],
        "p3_ceiling_b8_t4": float(f"{CEIL[8][0]:.3g}"),
        "p3_ceiling_b4_t4": float(f"{CEIL[4][0]:.3g}"),
        "p3_yardstick_b4_t4_dB": round(CEIL[4][2], 1),
        "p3_T_pass_A1_b8_K": round(t_max(BOOK["A1 F=2 k_eff, full rail"], CEIL[8][0]) or 0, 1),
        "p3_T_pass_A1_b4_K": round(t_max(BOOK["A1 F=2 k_eff, full rail"], CEIL[4][0]) or 0, 1),
        "p3_T_pass_A2_tol10_K": round(t_max(BOOK["A2 A1 + split swing (-3 dB)"], 10 * CEIL[8][0]) or 0, 1),
    }
    clash = sorted((set(PRED) & set(RQ)) | (set(PRED) & set(RC)))
    assert not clash, clash
    for k, v in PRED.items():
        print(f"   {k:40s} = {v}")
    print(f"\nreleased chains imported read-only; nothing written to the repository; runtime {time.time()-T0:.0f} s")
