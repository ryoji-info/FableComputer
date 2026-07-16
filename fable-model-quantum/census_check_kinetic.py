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
