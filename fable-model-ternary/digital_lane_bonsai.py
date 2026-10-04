# -*- coding: utf-8 -*-
"""Ternary Bonsai 2 27B on the Part I digital fabric: lane design, a bit-exact try,
timing closure, and the error budget under the record's alternative bookings (v2.1).

v2.1 (Part III manuscript revision, 2026-10-04): prints both ends of the heat range at
300 K and 353 K, the booking-B mapping factor KAPPA_B_RATIO and the mapped B values, and
the runtime on the reference platform; no computed quantity changed.

Companion to The Fable Computer, Part III. Every digital-lane number of the
manuscript is printed here, section by section.

Run from anywhere inside the repository (or with FABLE_REPO=<repo root>):
    python digital_lane_bonsai.py            # Python 3 + numpy, about 21 s
The released chains are imported READ-ONLY (no bytecode written, nothing edited,
run_all.py never imported or run).

What is the record's and what is mine:
  * record (Part I section 6.5, Table 5): half adder = OR (low threshold), carry-AND
    (high threshold), NOT (inverting bias), delay buffer, output AND -- 5 active
    cells, depth 3, fan-out <= 2 -- plus 2 optional carry-alignment buffers
    (7 biased cells); "two half adders and an OR compose a full adder".
  * record: per-cell dissipation (fable-model-chain results.json, stored at the
    353 K cap, hydrodynamic tier; Part I 8.2 text gives the kinetic-corrected
    1.59-1.67 kW/cm^2), re-sync spacing law (fable-model-chain noise.resync_spacing),
    static noise margin law (fable-model-chain cell.static_noise_margin), the
    classical decision BER (fable-model-quantum qerrors.classical_ber, Part II's
    construction), F = 2 softening k_eff = 8 F^-1/2 (notes/2026-07-21, in-model),
    the gated F = 2 slot-rate frontier 69 [63, 74] GHz (notes/2026-07-31, in-model,
    adjudicated at the 353 K bias).
  * mine (labelled [D1]-[D8]):
    [D1] the lane netlist: 32 int8 x ternary products per slot (the runtime's Q8_0
         block), select (p AND a) OR (n AND NOT a), sign bit inverted, greedy
         Wallace tree of record full adders, 12-bit ripple adder; block constants
         (+n_neg, -32*128) and FP scales applied in CMOS.
    [D2] gate-level emulation with independent decision flips at probability BER.
    [D3] tau^-3 scaling of the stored 353 K dissipation to 300 K (tracked bias).
    [D4] activation broadcast to L lanes through F = 2 buffer trees.
    [D5] bookings A1-A3 (the released margin law with the 07-21 F = 2 softening,
         then the split and junction attenuation of Part I's worst path) and B
         (the QMAC calculus) as alternatives to the released booking A0.
    [D6] workload constants of the model (external: public config, file sizes).
    [D7] timing: a depth model of the same netlist; latch-free wave pipelining
         needs every live wire regenerated at every level (balancing buffers),
         with skew tolerance t, and a re-sync station on every wire crossing a
         cut every S levels.
    [D8] launch noise: Part II's launch_excess_variance added at the first
         decision after each launch.
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
import cell as CELL       # noqa: E402  (fable-model-chain)
import noise as NOISE     # noqa: E402  (fable-model-chain)

RC = json.load(open(os.path.join(ROOT, "fable-model-chain", "results.json"), encoding="utf-8"))
RQ = json.load(open(os.path.join(ROOT, "fable-model-quantum", "results.json"), encoding="utf-8"))
OUT = {}
T0 = time.time()
X_RAIL = math.sqrt(2 * qerrors.N_RAIL)


def hdr(s):
    print("\n" + "=" * 100 + "\n" + s + "\n" + "=" * 100)


def r2(v):
    return float(f"{v:.3g}")


# ============================================================================ §0
hdr("§0  RECORD ANCHORS (demonstrated: released values, unedited chains)")
P353 = RC["dissipation_operating_kW_cm2"] * 1e3 * 1e-8          # W per biased cell at 353 K, hydrodynamic
P353_HI = RC["dissipation_upper_kW_cm2"] * 1e3 * 1e-8
P353_KIN = (1.59e3 * 1e-8, 1.67e3 * 1e-8)                        # Part I 8.2 text: kinetic-corrected
R300 = (RC["M_th_300K"] / RC["M_th_353K"]) ** 2 * (QC.tau_q(353.0) / QC.tau_q(300.0))   # [D3]
P300, P300_HI = P353 * R300, P353_HI * R300
BER0 = {T: qerrors.classical_ber(T) for T in (300.0, 353.0, 77.0)}
F_SLOT, F_BAND = 69e9, (63e9, 74e9)
NF_FLOOR = RC["noise_figure_floor_dB"]
S_RS = (NOISE.resync_spacing(4.0), NOISE.resync_spacing(NF_FLOOR))
print(f"per biased cell at 353 K: {P353*1e6:.2f} uW (stored, hydrodynamic), {P353_HI*1e6:.2f} uW (upper bound); "
      f"Part I 8.2 kinetic-corrected {P353_KIN[0]*1e6:.1f}-{P353_KIN[1]*1e6:.1f} uW")
print(f"300 K by tracked-bias tau^-3 scaling [D3] x{R300:.4f}: {P300*1e6:.2f}-{P300_HI*1e6:.2f} uW "
      f"(hydrodynamic tier; the kinetic correction at 300 K is not evaluated in the record)")
print(f"Part I Table 5 half adder: 0.09-0.12 mW for 7 biased cells -> {7*P353*1e3:.4f}-{7*P353_HI*1e3:.4f} mW (match)")
print(f"static noise margin law (cell.py): k = 8 -> {CELL.static_noise_margin(8.0):.4f}; "
      f"F = 2 softened k_eff = 8/sqrt2 -> {CELL.static_noise_margin(8/math.sqrt(2)):.4f} (07-21: 0.221)")
print(f"classical decision BER (booking A0, released): 300 K {BER0[300.0]:.3e}, 353 K {BER0[353.0]:.3e}, "
      f"77 K {BER0[77.0]:.3e}")
print(f"re-sync spacing (released law; 08-25 sec. 5 item 5): NF 4 dB -> {S_RS[0]:.1f} cells, NF floor "
      f"{NF_FLOOR:.3f} dB -> {S_RS[1]:.1f} cells (Part I's '24' is not reachable)")
print(f"slot rate: gated F = 2 frontier {F_SLOT/1e9:.0f} GHz, band {F_BAND[0]/1e9:.0f}-{F_BAND[1]/1e9:.0f} GHz "
      f"(07-31, in-model, adjudicated at the 353 K bias); one slot = {1e12/F_SLOT:.1f} ps")

# ============================================================================ §1
hdr("§1  WORKLOAD PER DECODED TOKEN [D6] (external inputs, cross-checked)")
d_, Fd, V_ = 5120, 17408, 248320
MATS = [("GDN attn_qkv", 10240, d_, 48), ("GDN attn_gate", 6144, d_, 48), ("GDN ssm_out", d_, 6144, 48),
        ("ATT q+gate", 12288, d_, 16), ("ATT k", 1024, d_, 16), ("ATT v", 1024, d_, 16), ("ATT o", d_, 6144, 16),
        ("FFN gate", Fd, d_, 64), ("FFN up", Fd, d_, 64), ("FFN down", d_, Fd, 64), ("LM head", V_, d_, 1)]
MACS = sum(n * k * c for _, n, k, c in MATS)
tern_w = sum(n * k * c for _, n, k, c in MATS[:-1]) + 2 * V_ * d_
PTQ1, PQ2 = 5_946_648_928, 7_206_168_928
print(f"ternary MACs/token = {MACS:,d}; ternary weights incl. embedding = {tern_w:,d}; "
      f"(PQ2_0 - PTQ1_0 file bytes)/6*128 = {int((PQ2 - PTQ1) / 6 * 128):,d} -> match {tern_w == int((PQ2 - PTQ1) / 6 * 128)}")
STREAM = PTQ1 - V_ * d_ * 28 / 128 + d_ * 28 / 128
BLOCKS = MACS // 32
GDN_RW = 2 * (48 * 48 * 128 * 128 * 4 + 48 * 10240 * 3 * 4)
print(f"weights streamed per token (PTQ1_0, embedding table excluded) = {STREAM/1e9:.3f} GB; GDN state read+write "
      f"{GDN_RW/1e6:.0f} MB (+{GDN_RW/STREAM:.1%}); FP16 KV at 32k context +2.147 GB (+{2.147e9/STREAM:.0%})")
print(f"32-wide int8 x ternary block sums per token = {BLOCKS:,d}; FP16 weight-group scales = {MACS//128:,d}")

# ============================================================================ §2
hdr("§2  THE LANE [D1] AND ITS TIMING CLOSURE [D7] (in-model)")


def wallace(heights):
    h, cnt, stages, pt = dict(heights), {}, 0, 0
    while max(h.values()) > 2:
        stages += 1
        nh = {}
        for c in sorted(h):
            k = h[c] // 3
            cnt[c] = cnt.get(c, 0) + k
            pt += h[c] - 3 * k
            nh[c] = nh.get(c, 0) + h[c] - 2 * k
            nh[c + 1] = nh.get(c + 1, 0) + k
        h = {c: v for c, v in nh.items() if v > 0}
    return cnt, h, stages, pt


CNT, FIN, STAGES, N_PT = wallace({b: 32 for b in range(8)})
N_FA, CPA_W = sum(CNT.values()), max(FIN) + 1
HA_ACT, HA_BIASED = 5, 7
FA_BIASED = 2 * HA_BIASED + 1
SEL, SIGN, FAN = 32 * 8 * 4, 32, 32 * 2 * 6
LOGIC = SEL + SIGN + FAN + (N_FA + CPA_W) * FA_BIASED
print(f"logic cells: select {SEL} + sign {SIGN} + weight fan-out {FAN} + {(N_FA + CPA_W)} full adders x {FA_BIASED} "
      f"= {LOGIC}; Wallace {N_FA} FAs in {STAGES} stages ({N_PT} pass-through bit-stages) + {CPA_W}-bit ripple adder")

# ---- depth model of the same netlist [D7]
WIRES = []


class Wire:
    __slots__ = ("d", "last")

    def __init__(self, d):
        self.d, self.last = d, d
        WIRES.append(self)


def gate(*ins):
    ins = [x for x in ins if x is not None]              # constant-0 inputs carry no timing
    if not ins:
        return None
    d = max(x.d for x in ins) + 1
    for x in ins:
        x.last = max(x.last, d)
    return Wire(d)


def t_ha(a, b):
    o, c = gate(a, b), gate(a, b)
    s = gate(gate(o), gate(c))                           # DLY(OR) and NOT(AND) -> output AND
    return s, gate(gate(c))                              # carry through the two alignment buffers


def t_fa(a, b, ci):
    s1, c1 = t_ha(a, b)
    if ci is None:
        return s1, c1
    s, c2 = t_ha(s1, ci)
    return s, gate(c1, c2)


def build_timing():
    WIRES.clear()
    cols = {b: [] for b in range(8)}
    for i in range(32):
        trees = []
        for _ in range(2):                               # p and n launched at depth 0
            v = Wire(0)
            l1 = [gate(v), gate(v)]
            trees.append([gate(l1[0]), gate(l1[0]), gate(l1[1]), gate(l1[1])])
        P, N = trees
        for b in range(8):
            a = Wire(2)                                  # activation launch timed to the tree leaves
            x = gate(gate(P[b // 2], a), gate(N[b // 2], gate(a)))
            if b == 7:
                x = gate(x)
            cols[b].append(x)
    while max(len(v) for v in cols.values()) > 2:
        nxt = {}
        for c in sorted(cols):
            bits = cols[c]
            k = len(bits) // 3
            for i in range(k):
                s, co = t_fa(bits[3 * i], bits[3 * i + 1], bits[3 * i + 2])
                nxt.setdefault(c, []).append(s)
                nxt.setdefault(c + 1, []).append(co)
            nxt.setdefault(c, []).extend(bits[3 * k:])
        cols = nxt
    width = max(cols) + 1
    carry, outs = None, []
    for c in range(width):
        v = cols.get(c, [])
        s, carry = t_fa(v[0] if v else None, v[1] if len(v) > 1 else None, carry)
        outs.append(s)
    outs.append(carry)
    return outs


outs = build_timing()
depth = max(w.d for w in WIRES)
skews = [w.last - 1 - w.d for w in WIRES if w.last > w.d]
out_d = [o.d for o in outs if o is not None]
print(f"depth model: {len(WIRES)} wires, critical path {depth} cells (~{depth/3:.0f} ps at ~0.33 ps/cell = "
      f"{depth/3/(1e12/F_SLOT):.1f} slots); largest wait of a wire for its last consumer: {max(skews)} cells; "
      f"output bits span depths {min(out_d)}-{max(out_d)} (fixed per readout line, deskewed at the receiver)")
BAL = {}
for tol in (0, 4, 14):
    BAL[tol] = sum(max(0, w.last - 1 - w.d - tol) for w in WIRES)
print("balancing buffers to regenerate every waiting wire (latch-free wave pipeline): "
      + ", ".join(f"tolerance {t} cells -> {n:,d} (+{n/LOGIC:.0%})" for t, n in BAL.items()))
STN = {}
for S in S_RS:
    cuts = range(int(S), depth + 1, int(S))
    STN[S] = sum(sum(1 for w in WIRES if w.d <= c < w.last) for c in cuts)
print("re-sync stations (one per wire crossing each cut): " + ", ".join(f"spacing {S:.1f} -> {n:,d}"
                                                                         for S, n in STN.items())
      + f" (the earlier cell-fraction rule gave {LOGIC/24:.0f}-{LOGIC/10:.0f})")
LANE_T = {"t0": (LOGIC + BAL[0] + STN[S_RS[1]], LOGIC + BAL[0] + STN[S_RS[0]]),
          "t4": (LOGIC + BAL[4] + STN[S_RS[1]], LOGIC + BAL[4] + STN[S_RS[0]]),
          "t14": (LOGIC + BAL[14] + STN[S_RS[1]], LOGIC + BAL[14] + STN[S_RS[0]])}
for k, v in LANE_T.items():
    print(f"   timing-closed lane, {k}: {v[0]:,d}-{v[1]:,d} cells")
LANE = LANE_T["t0"]                                     # reference: record idiom, every wire regenerated
AREA_CELL = 12 * 16 / 7
print(f"reference lane (t = 0, as Part I's half adder balances its own paths with a DLY cell): {LANE[0]:,d}-{LANE[1]:,d} "
      f"cells, {LANE[0]*AREA_CELL/1e6:.3f}-{LANE[1]*AREA_CELL/1e6:.3f} mm^2")
POWER = {"300 K (tau^-3 scaled, hydrodynamic tier)": (P300, P300_HI),
         "353 K (kinetic-corrected, Part I 8.2)": P353_KIN}
for name, (pl, ph) in POWER.items():
    lo, hi = LANE[0] * pl, LANE[1] * ph
    print(f"lane power at {name}: {lo*1e3:.0f}-{hi*1e3:.0f} mW -> {lo/(32*F_SLOT)*1e15:.0f}-"
          f"{hi/(32*F_SLOT)*1e15:.0f} fJ/MAC at full utilisation")
OUT["lane_cells_t0"] = LANE

# ============================================================================ §3
hdr("§3  TRY: GATE-LEVEL EMULATION ON BONSAI-SHAPED MATRICES [D1][D2]")
P0 = 1 / 3                                         # ASSUMPTION: zero-weight share (unpublished)


def q80(x, blk=32):
    xb = x.reshape(-1, blk)
    d = (np.abs(xb).max(1) / 127.0).astype(np.float16).astype(np.float64)
    q = np.clip(np.rint(xb / d[:, None]), -127, 127).astype(np.int64)
    return q, d


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


def lane_blocks(w, q, fl, ha_err=0.0, rng_e=None, fl_launch=None):
    """Lane slots for rows w, q (n, 32): returns the 13-bit tree output."""
    if ha_err > 0:
        def ha_b(a, b, _fl):
            s = (a + b).astype(np.int64)
            r = rng_e.random(s.shape)
            t = ha_err / 1.5
            s = np.clip(s + ((r < t) & (s < 2)) - ((r > 1 - t) & (s > 0)), 0, 2)
            return (s & 1).astype(np.uint8), (s >> 1).astype(np.uint8)

        def FA(a, b, cin, _fl):
            s1, c1 = ha_b(a, b, _fl)
            s, c2 = ha_b(s1, cin, _fl)
            return s, (c1 | c2)
    else:
        FA = fa
    fL = fl_launch or (lambda v: v)
    a8 = (q & 0xFF).astype(np.int64)
    p = fL((w == 1).astype(np.uint8))
    nn = fL((w == -1).astype(np.uint8))

    def fan8(v):
        l1 = [fl(v), fl(v)]
        l2 = [fl(l1[0]), fl(l1[0]), fl(l1[1]), fl(l1[1])]
        return [l2[b // 2] for b in range(8)]
    P8, N8 = fan8(p), fan8(nn)
    cols = {}
    for b in range(8):
        abit = fL(((a8 >> b) & 1).astype(np.uint8))
        x = fl(fl(P8[b] & abit) | fl(N8[b] & fl(1 - abit)))
        if b == 7:
            x = fl(1 - x)
        cols[b] = [x[:, i] for i in range(32)]
    while max(len(v) for v in cols.values()) > 2:
        nxt = {}
        for c in sorted(cols):
            bits = cols[c]
            k = len(bits) // 3
            for i in range(k):
                s, co = FA(bits[3 * i], bits[3 * i + 1], bits[3 * i + 2], fl)
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
        s, carry = FA(A[c], B[c], carry, fl)
        out += s.astype(np.int64) << c
    return out + (carry.astype(np.int64) << width)


def run_matrix(N, K, ber=0.0, ha_err=0.0, p_launch=0.0, limit=None, dist="gauss", seed=0):
    r = np.random.default_rng(seed)
    W = r.choice(np.array([-1, 0, 1], dtype=np.int8), size=(N, K), p=[(1 - P0) / 2, P0, (1 - P0) / 2])
    sw = (np.abs(r.normal(0, 1, (N, K // 128))) * 0.02 + 0.01).astype(np.float16).astype(np.float64)
    x = r.standard_t(4, K) if dist == "t4" else r.normal(0, 1, K)
    q, d = q80(x)
    nb = K // 32
    rows = np.arange(N) if limit is None else np.sort(r.choice(N, size=limit, replace=False))
    chunk = max(1, 40000 // nb)
    fl, flL = Flip(ber, r), (Flip(p_launch, r) if p_launch > 0 else None)
    n_ok, n_tot, dv = 0, 0, []
    y_lane, y_q = np.empty(len(rows)), np.empty(len(rows))
    for r0 in range(0, len(rows), chunk):
        rr = rows[r0:r0 + chunk]
        wb = W[rr].reshape(-1, 32)
        qb = np.broadcast_to(q, (len(rr), nb, 32)).reshape(-1, 32)
        exact = (wb.astype(np.int64) * qb).sum(1)
        got = lane_blocks(wb, qb, fl, ha_err, r, flL) + (wb == -1).sum(1) - 32 * 128
        n_ok += int((got == exact).sum())
        n_tot += len(got)
        dv.append(got - exact)
        scale = d[None, :] * np.repeat(sw[rr], 4, axis=1)
        y_lane[r0:r0 + len(rr)] = (got.reshape(len(rr), nb) * scale).sum(1)
        y_q[r0:r0 + len(rr)] = (exact.reshape(len(rr), nb) * scale).sum(1)
    y_true = ((W[rows] * np.repeat(sw[rows], 128, axis=1)) * x[None, :]).sum(1)
    dv = np.concatenate(dv).astype(float)
    return {"exact_blocks": n_ok, "blocks": n_tot, "flips": fl.n + (flL.n if flL else 0), "y_lane": y_lane,
            "y_q": y_q, "y_true": y_true, "err_var_block": float(np.var(dv)), "err_mean_block": float(np.mean(dv))}


def snr(sig, err):
    e = np.mean(err ** 2)
    return float("inf") if e == 0 else 10 * math.log10(np.mean(sig ** 2) / e)


print("the netlist's exactness is also provable: every full adder keeps s + 2c = a + b + c_in, and each product's "
      "8-bit pattern (one's complement for w = -1, sign bit inverted) is an unsigned u in [0, 255], so the tree output "
      "U = sum(u) lies in [0, 8160] < 2^13; the emulation checks the implementation of that argument")
for name, N, K, lim in (("ATT k (full matrix)", 1024, 5120, None), ("GDN ssm_out (full matrix)", 5120, 6144, None),
                        ("FFN down (1,024 of 5,120 rows)", 5120, 17408, 1024)):
    t = time.time()
    st = run_matrix(N, K, limit=lim)
    ok = st["exact_blocks"] == st["blocks"]
    same = np.array_equal(st["y_lane"], st["y_q"])
    print(f"{name:32s}: {st['blocks']:9,d} block sums ({st['blocks']*32/1e6:5.1f} M MACs) through the gate-level "
          f"netlist in {time.time()-t:4.1f} s -> all exact: {ok}; CMOS scaling code reproduces the int8 reference: "
          f"{same}; vs unquantised float {snr(st['y_true'], st['y_q'] - st['y_true']):.1f} dB (Q8_0 only)")
    assert ok and same
print("(BER = 0: the threshold cells act as Boolean logic, so this is a netlist check, not a physics check)")

# ============================================================================ §4
hdr("§4  ERROR BUDGET [D2][D5][D8] (in-model)")
coef = []
for ber in (1e-5, 2e-5, 4e-5):
    st = run_matrix(1024, 5120, ber=ber, seed=11)
    coef.append(st["err_var_block"] / ber)
    print(f"cell-decision flips at BER {ber:.0e}: {st['flips']:,d} flips in {st['blocks']:,d} blocks -> per-unit-BER "
          f"block-sum error variance {coef[-1]:.3e}")
KAPPA = float(np.mean(coef))
print(f"kappa = {KAPPA:.2e} (spread {100*(max(coef)-min(coef))/KAPPA:.0f} %)")
coefL = []
for pl in (1e-4, 3e-4):
    st = run_matrix(1024, 5120, p_launch=pl, seed=13)
    coefL.append(st["err_var_block"] / pl)
    print(f"launched-bit flips at {pl:.0e}: {st['flips']:,d} flips -> per-unit-rate block-sum error variance "
          f"{coefL[-1]:.3e}")
KAPPA_L = float(np.mean(coefL))

YS, SIG = {}, {}
for dist in ("gauss", "t4"):
    r = np.random.default_rng(7)
    s_y, e_q, e_d = 0.0, 0.0, 0.0
    for _ in range(4000):
        x = r.standard_t(4, 5120) if dist == "t4" else r.normal(0, 1, 5120)
        wv = r.choice([-1, 0, 1], size=5120, p=[(1 - P0) / 2, P0, (1 - P0) / 2])
        q, dsc = q80(x)
        y = (wv * x).sum()
        yq = ((wv.reshape(-1, 32) * q).sum(1) * dsc).sum()
        s_y += y * y
        e_q += (yq - y) ** 2
        e_d += np.mean(dsc ** 2)
    YS[dist], SIG[dist] = 10 * math.log10(s_y / e_q), s_y / e_d
NB = 5120 // 32
print("Q8_0 yardstick (4,000 dot products, K = 5120): " + ", ".join(f"{k} {v:.1f} dB" for k, v in YS.items()))


def snr_from(rate, kap, dist="t4"):
    return 10 * math.log10(SIG[dist] / (NB * kap * rate)) if rate > 0 else float("inf")


CEIL = SIG["t4"] / (NB * KAPPA * 10 ** (YS["t4"] / 10))
CEIL_L = SIG["t4"] / (NB * KAPPA_L * 10 ** (YS["t4"] / 10))
print(f"ceilings (digital error power = the Q8_0 error power, t4): {CEIL:.1e} per cell decision; "
      f"{CEIL_L:.1e} per launched bit (10 dB below Q8_0: 10x lower)")
OUT["ceil_cell"], OUT["ceil_launch"] = CEIL, CEIL_L


def ber_booking(T, k, swing):
    """[D5] released margin law at sharpness k, decided on the swing x_rail * swing."""
    V = (2 - 1 / qdecode.G_dec(T)) * (QC.nbar(T) + 0.5)
    return Q.tail(CELL.static_noise_margin(k) * X_RAIL * swing, V)


KE = 8 / math.sqrt(2)
JN = 10 ** (-qmac.JUNCTION_DB / 20)
BOOK = {
    "A0 released (k 8, full rail)": lambda T: qerrors.classical_ber(T),
    "A1 F=2 k_eff (07-21), full rail": lambda T: ber_booking(T, KE, 1.0),
    "A2 A1 + split swing (-3 dB)": lambda T: ber_booking(T, KE, 1 / math.sqrt(2)),
    "A3 A2 + one junction (-1 dB)": lambda T: ber_booking(T, KE, JN / math.sqrt(2)),
}


def ha_bookingB(T):
    G = qdecode.G_dec(T)

    def arm(on, N):
        st = Q.GState(N=qerrors.N_RAIL) if on else Q.amp(Q.GState(N=0), G, T)
        st = Q.loss(st, N / qerrors.N_RAIL, T)
        return Q.loss_dB(st, qmac.input_transit_dB(T), T)

    def levels(N):
        xs, Vs, top = [], [], None
        for s in range(3):
            st = Q.combine(arm(s >= 1, N), arm(s >= 2, N), 0.5)
            if s == 2:
                top = st.x ** 2 / 2
            st = Q.loss_dB(st, qmac.fanout_dB(T), T)
            xs.append(st.x)
            Vs.append(st.V)
        return xs, Vs, top
    _, _, top = levels(1000.0)
    xs, Vs, _ = levels(min(qerrors.N_RAIL, 1000.0 * qerrors.N_RAIL / top))
    return Q.symbol_error(xs, [0.25, 0.5, 0.25], max(Vs) + qdecode.decoder_amp_noise(T)
                          + qdecode.threshold_band_variance(max(xs)))


print(f"\n{'booking':34s} {'300 K':>22s} {'353 K':>22s} {'77 K':>22s}   (BER per decision; lane digital-error SNR, t4)")
TAB = {}
for name, f in BOOK.items():
    row = []
    for T in (300.0, 353.0, 77.0):
        b = f(T)
        TAB[(name, T)] = (b, snr_from(b, KAPPA))
        row.append(f"{b:9.2e} {snr_from(b, KAPPA):6.1f} dB")
    print(f"{name:34s} " + "   ".join(f"{c:>22s}" for c in row))
rowB = []
for T in (300.0, 353.0, 77.0):
    pb = ha_bookingB(T)
    st = run_matrix(256, 5120, ha_err=pb, seed=21)
    s_b = snr(st["y_q"], st["y_lane"] - st["y_q"])
    TAB[("B", T)] = (pb, s_b)
    rowB.append(f"{pb:9.2e} {s_b:6.1f} dB")
# equivalent cell-BER per HA-decode error (from the 300 K emulation): maps B onto the same ceiling
s300 = TAB[("B", 300.0)][1]
eq_ber = SIG["t4"] / (NB * KAPPA * 10 ** (s300 / 10))
KAPPA_B_RATIO = eq_ber / TAB[("B", 300.0)][0]
print(f"{'B QMAC calculus (HA decode, emul.)':34s} " + "   ".join(f"{c:>22s}" for c in rowB))
print(f"B mapped onto the cell-decision axis through the 300 K emulation: KAPPA_B_RATIO = {KAPPA_B_RATIO:.4f} "
      f"(equivalent cell BER per HA-decode error); mapped lane SNR " + ", ".join(
          f"{T:.0f} K {snr_from(TAB[('B', T)][0] * KAPPA_B_RATIO, KAPPA):.1f} dB" for T in (300.0, 353.0, 77.0))
      + " (the direct 77 K emulation above sees ~25 error events)")
print(f"pass line: SNR >= {YS['t4']:.1f} dB (equal to Q8_0, t4), BER <= {CEIL:.1e}; 10 dB under Q8_0: BER <= {CEIL/10:.1e}")


def t_max(f, target):
    """Highest T in [4, 400] K with f(T) <= target (f increasing in T)."""
    lo, hi = 4.0, 400.0
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


print("highest temperature at which each booking meets the pass line (BER <= ceiling):")
for name, f in list(BOOK.items()) + [("B QMAC calculus (HA decode)", lambda T: ha_bookingB(T) * KAPPA_B_RATIO)]:
    tm = t_max(f, CEIL)
    print(f"   {name:34s}: {('below %.1f K' % tm) if tm and tm < 400 else ('above 400 K' if tm else 'never')}")
    OUT[f"T_pass_{name.split()[0]}"] = tm
OUT["booking_table"] = {f"{k[0]}|{int(k[1])}": v for k, v in TAB.items()}

print("\nlaunch noise [D8]: Part II's launch_excess_variance added at the first decision after each launch")
for T in (300.0, 353.0):
    V = (2 - 1 / qdecode.G_dec(T)) * (QC.nbar(T) + 0.5)
    for lab, k in (("k 8", 8.0), ("k_eff", KE)):
        m = CELL.static_noise_margin(k) * X_RAIL
        p20 = Q.tail(m, V + Q.launch_excess_variance(X_RAIL, 20.0))
        lo, hi = 0.0, 120.0
        for _ in range(100):
            mid = 0.5 * (lo + hi)
            if Q.tail(m, V + Q.launch_excess_variance(X_RAIL, mid)) > CEIL_L:
                lo = mid
            else:
                hi = mid
        print(f"   {T:.0f} K, {lab}: per-bit error at the coded 20 dB = {p20:.1e}; launch-bit ceiling {CEIL_L:.1e} "
              f"needs S >= {hi:.1f} dB (amplitude jitter <= {100*10**(-hi/20):.2f} % of the swing)"
              + ("" if hi < 119 else " -> unreachable: the cell's own noise already exceeds the ceiling"))
        OUT[f"launch_S_min_{int(T)}K_{lab.replace(' ', '')}"] = hi

# ============================================================================ §5
hdr("§5  SYSTEM: lanes, input/output, CMOS perimeter, heat, scale (in-model + arithmetic)")
tps_lane = 32 * F_SLOT / MACS
print(f"one lane = {tps_lane:.2f} tok/s at {F_SLOT/1e9:.0f} GHz (band {32*F_BAND[0]/MACS:.1f}-{32*F_BAND[1]/MACS:.1f})")
CFG = {}
for bw in (0.5e12, 1e12, 3e12):
    tps = bw / STREAM
    L = math.ceil(tps / tps_lane)
    bcast = 256 * (2 * L - 2)
    cells = (L * LANE[0] + bcast, L * LANE[1] + bcast)
    pw300 = (cells[0] * P300, cells[1] * P300_HI)
    pw353 = (cells[0] * P353_KIN[0], cells[1] * P353_KIN[1])
    CFG[bw] = dict(tps=tps, L=L, cells=cells, pw300=pw300, pw353=pw353)
    print(f"{bw/1e12:.1f} TB/s -> {tps:6.1f} tok/s -> {L} lanes ({tps/(L*tps_lane):.0%} busy); {cells[0]:,.0f}-"
          f"{cells[1]:,.0f} cells ({cells[0]*AREA_CELL/1e6:.2f}-{cells[1]*AREA_CELL/1e6:.2f} mm^2); fabric "
          f"{pw300[0]:.2f}-{pw300[1]:.2f} W (300 K), {pw353[0]:.2f}-{pw353[1]:.2f} W (353 K); "
          f"{pw300[0]/tps*1e3:.1f}-{pw353[1]/tps*1e3:.1f} mJ/token")
    print(f"      launch {64*L + 256} lines ({(64*L + 256)*F_SLOT/1e12:.1f} Tb/s), readout {13*L} lines "
          f"({13*L*F_SLOT/1e12:.2f} Tb/s); {(64*L + 256)/(32*L):.2f} launched bits per MAC computed")
r77 = (QC.tau_q(300.0) / QC.tau_q(77.0)) ** 3
for bw in (3e12,):
    c = CFG[bw]
    print(f"cooled to 77 K (Joule model [D3] extended below the hydrodynamic expiry, uncertified): cell power x{r77:.3f} "
          f"-> {c['pw300'][0]*r77:.3f}-{c['pw300'][1]*r77:.3f} W for the {c['L']} lanes; Carnot work at 77 K "
          f"x{(300-77)/77:.2f} -> wall-plug {c['pw300'][0]*r77*(1+(300-77)/77):.2f}-{c['pw300'][1]*r77*(1+(300-77)/77):.2f} "
          f"W at ideal cooling (x{r77*(1+(300-77)/77):.2f} the warm fabric power)")
fill = 1e-8 / (AREA_CELL * 1e-8)
for lab, (plo, phi) in (("300 K", (RC["dissipation_operating_kW_cm2"] * R300, RC["dissipation_upper_kW_cm2"] * R300)),
                        ("353 K kinetic", (1.59, 1.67))):
    print(f"heat: fill {fill:.1%} -> dT = {plo*1e3*fill*0.10:.1f}-{phi*1e3*fill*0.10:.1f} K at {plo:.2f}-{phi:.2f} kW/cm^2 "
          f"({lab}) vs the 55 K budget")
print("Part I's only system-scale figure is illustrative (8.1: 'a 1 W-class drive over 1e4-1e5 active cells'), not a cap")
lmax = max(L for L in range(1, 200) if L * LANE[0] + 256 * (2 * L - 2) <= 1e5)
print(f"within 1e5 cells: {lmax} timing-closed lanes -> {lmax*tps_lane:.0f} tok/s with batching (B >= "
      f"{math.ceil(lmax*tps_lane/(3e12/STREAM))} at 3 TB/s)")
print(f"\nCMOS perimeter per token: {3*BLOCKS/1e9:.2f} GFLOP of block-sum scaling ({3*BLOCKS*CFG[3e12]['tps']/1e12:.2f} "
      f"TFLOP/s at {CFG[3e12]['tps']:.0f} tok/s), n_neg popcounts {BLOCKS/1e6:.0f} M (fixed by the weights: "
      f"precompute and stream +{BLOCKS*6/8/STREAM:.1%}, or count in CMOS), FWHT 21.7-29.1 M adds, GDN ~151 M FP32 "
      f"MAC, attention 0.81 G MAC at 4k context")
print("reported decode rates (external): RTX 4090 86.0 tok/s (PTQ1_0 tg128), M5 Max 46.8 (press), RTX 5090 143 (press)")

# ============================================================================ §6
hdr("§6  PRE-REGISTERED NUMBERS (new key names; rounded to the precision the estimators support)")
PRED = {
    "dl_lane_cells_t0_low": LANE[0], "dl_lane_cells_t0_high": LANE[1],
    "dl_balancing_buffers_t0": BAL[0],
    "dl_kappa_int2_per_block_per_BER": r2(KAPPA),
    "dl_ber_ceiling_equal_q80_t4": r2(CEIL),
    "dl_snr_A0_300K_t4_dB": round(TAB[("A0 released (k 8, full rail)", 300.0)][1], 1),
    "dl_snr_A1_300K_t4_dB": round(TAB[("A1 F=2 k_eff (07-21), full rail", 300.0)][1], 1),
    "dl_snr_B_300K_dB": round(TAB[("B", 300.0)][1], 1),
    "dl_launch_S_min_300K_k8_dB": round(OUT["launch_S_min_300K_k8"], 1),
    "dl_lanes_for_3TBs": CFG[3e12]["L"],
    "dl_kappa_B_ratio_300K": round(KAPPA_B_RATIO, 4),
}
clash = sorted((set(PRED) & set(RQ)) | (set(PRED) & set(RC)))
assert not clash, clash
for k, v in PRED.items():
    print(f"   {k:36s} = {v}")
print(f"\nreleased chains imported read-only; nothing written to the repository; runtime {time.time()-T0:.0f} s")
