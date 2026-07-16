# -*- coding: utf-8 -*-
"""Fable 5 / Fabric prompt: is V_k = (x_range/k)^2/12 a valid conversion?
Run from inside fable-model-quantum/.  Python 3 + numpy.
"""
import math
import numpy as np
import qconstants as C
import qmode, qnoise as Q, qdecode, qmac, qerrors

TEMPS = (353, 300, 150, 77, 48, 20, 4)
KDEC = 16.0
PRIORS = (0.25, 0.5, 0.25)


def parts(T, N_op=400):
    st, xr = qmac.levels_at_decision(T, N_op)
    V_slot = max(s.V for s in st.values()) + qdecode.decoder_amp_noise(T)
    lv = [st[(0, 0)].x, 0.5 * (st[(0, 1)].x + st[(1, 0)].x), st[(1, 1)].x]
    return lv, V_slot, xr


def sym_err_shift(lv, V, u1=0.0, u2=0.0):
    """3-level symbol error, thresholds at midpoints + offsets u1,u2."""
    s = math.sqrt(V)
    t1 = 0.5 * (lv[0] + lv[1]) + u1
    t2 = 0.5 * (lv[1] + lv[2]) + u2
    q = lambda z: 0.5 * math.erfc(z / math.sqrt(2))
    e = 0.25 * q((t1 - lv[0]) / s)
    e += 0.5 * (q((lv[1] - t1) / s) + q((t2 - lv[1]) / s))
    e += 0.25 * q((lv[2] - t2) / s)
    return e


# ---------- 0. tanh(u/dn)/2+1/2 is the logistic CDF, scale dn/2; tangent width 2dn
u = np.linspace(-8, 8, 200001)
dn = 1.0
tanh_cdf = 0.5 * (1 + np.tanh(u / dn))
logi = 1.0 / (1 + np.exp(-u / (dn / 2)))
print("0. tanh-form vs logistic CDF (s=dn/2): max|diff| = %.3e" % np.max(np.abs(tanh_cdf - logi)))
slope0 = np.gradient(tanh_cdf, u)[len(u) // 2]
print("   max slope = %.6f   tangent-extrapolated band 1/slope = %.6f dn  (=> 2*dn)"
      % (slope0, 1.0 / slope0 / dn))
print("   => band in input amplitude = 2*dn/beta = 2*A_swing/k   (cell.py line 71: 0.5*(1-2/k)) OK")
print("   qdecode uses range/k, i.e. HALF the tangent band.\n")

# ---------- 1. reference plane
x_rail = math.sqrt(2 * qerrors.N_RAIL)
print("1. REFERENCE PLANE")
print("   N_rail = %.1f quanta -> x_rail (Part-I logic swing) = %.3f" % (qerrors.N_RAIL, x_rail))
for T in (353, 300, 4):
    _, _, xr = parts(T)
    print("   T=%3d K: ladder x_range = %6.3f  | x_rail/x_range = %.3f" % (T, xr, x_rail / xr))
_, _, xr300 = parts(300)
print("   Part-I cell used AS-IS on the ladder range (beta, dn untouched):")
for k_logic in (8, 16):
    print("      k_logic=%2d at cell plane -> k_dec = %.2f at ladder plane  (regen floor ~5)"
          % (k_logic, k_logic * xr300 / x_rail))
print("   To reach k_dec=16 on the ladder range you need cell-plane sharpness "
      "%.1f" % (16 * x_rail / xr300))
print("   i.e. (beta/dn)_dec / (beta/dn)_logic = %.2f"
      % ((KDEC / xr300) / (8.0 / x_rail)))
print()

# ---------- 2. published column reproduces
print("2. PUBLISHED COLUMN (reproduce)")
for T in TEMPS:
    print("   %3d K  q2bit_avg16 = %.6e" % (T, qmac.error_2bit(T, 400, n_avg=16)))
print()

# ---------- 3. the four readings
print("3. READINGS  (N_op=400, n_avg=16)")
hdr = "   %3s | %11s | %11s | %11s | %11s | %11s"
print(hdr % ("T", "published", "band drop", "unif-convol", "margin", "meta"))
rows = []
# Gauss-Legendre nodes for the uniform average
gx, gw = np.polynomial.legendre.leggauss(400)
for T in TEMPS:
    lv, V_slot, xr = parts(T)
    V16 = V_slot / 16.0
    Vpub = qmac.decision_variance(*(lambda st, x: (st, x))(*qmac.levels_at_decision(T, 400)),
                                  T, 16)
    p_pub = qmac.error_2bit(T, 400, n_avg=16)

    # (a) band dropped entirely
    p_drop = sym_err_shift(lv, V16)

    # (b) the docstring's OWN model used correctly: threshold offset
    #     u ~ Uniform(-a, a), a = xr/(2k)  (so Var = (xr/k)^2/12), CONVOLVED
    a = xr / (2 * KDEC)
    us = a * gx
    ws = gw / 2.0
    p_unif = 0.0
    for u1, w1 in zip(us, ws):
        for u2, w2 in zip(us, ws):
            pass
    # separable: do each boundary independently
    q = lambda z: 0.5 * math.erfc(z / math.sqrt(2))
    s16 = math.sqrt(V16)
    d1 = 0.5 * (lv[1] - lv[0])
    d2 = 0.5 * (lv[2] - lv[1])
    e1 = sum(w * (0.25 * q((d1 + uu) / s16) + 0.5 * q((d1 - uu) / s16))
             for uu, w in zip(us, ws))
    e2 = sum(w * (0.5 * q((d2 + uu) / s16) + 0.25 * q((d2 - uu) / s16))
             for uu, w in zip(us, ws))
    p_unif = e1 + e2

    # (c) butterfly-margin reading: d_eff = d - (tangent band)/2 = d - xr/k
    de1, de2 = d1 - xr / KDEC, d2 - xr / KDEC
    p_marg = 0.25 * q(de1 / s16) + 0.5 * (q(de1 / s16) + q(de2 / s16)) + 0.25 * q(de2 / s16)

    # (d) metastability: comparator incremental gain at threshold
    #     dA_out/dA_in = A_pump*g_max*k/(2*A_swing);  A_pump ~ x_rail, g_max = sqrt(G_CW)
    g_max = math.sqrt(qdecode.G_dec(T))
    gain_cmp = x_rail * g_max * KDEC / (2 * xr)
    gain_logic = x_rail * g_max * 8.0 / (2 * x_rail)     # downstream logic cell
    dcrit1 = (x_rail / 2) / (gain_cmp * gain_logic)      # comparator + ONE more cell
    phi = lambda z: math.exp(-0.5 * z * z) / math.sqrt(2 * math.pi)
    # P(|x - t| < dcrit) summed over the levels adjacent to each threshold
    p_meta = 0.0
    for d_, pr in ((d1, 0.25), (d1, 0.5), (d2, 0.5), (d2, 0.25)):
        p_meta += pr * 2 * dcrit1 * phi(d_ / s16) / s16
    rows.append((T, p_pub, p_drop, p_unif, p_marg, p_meta, dcrit1, gain_cmp))
    print("   %3d | %11.4e | %11.4e | %11.4e | %11.4e | %11.4e"
          % (T, p_pub, p_drop, p_unif, p_marg, p_meta))
print()
print("   (metastability uses dcrit = (rail/2)/(G_cmp*G_logic), comparator + 1 restoring cell;")
print("    deeper paths shrink dcrit by ~%.1f per further cell at 300 K, ~%.1f at 4 K)"
      % (4 * math.sqrt(qdecode.G_dec(300)), 4 * math.sqrt(qdecode.G_dec(4))))
print("   d_crit(300K) = %.4f in x units; comparator incremental gain at threshold = %.1f"
      % (rows[1][6], rows[1][7]))
print()

# ---------- 4. floors
print("4. FLOORS  (V_slot -> 0, i.e. n_avg -> inf or T -> 0)")
lv, V_slot, xr = parts(300)
d = 0.5 * (lv[1] - lv[0])
print("   code (Gaussian-additive V_static):  p_floor = 0.75*erfc(sqrt(3/8)*k) = %.4e"
      % (0.75 * math.erfc(math.sqrt(3.0 / 8.0) * KDEC)))
for Vs in (V_slot / 16, V_slot / 1e4, V_slot / 1e8, 0.0):
    a = xr / (2 * KDEC)
    s_ = math.sqrt(Vs) if Vs > 0 else 1e-12
    q = lambda z: 0.5 * math.erfc(z / math.sqrt(2))
    e = sum(w * (0.75 * q((d - uu) / s_) + 0.75 * q((d + uu) / s_))
            for uu, w in zip(a * gx, gw / 2.0))
    print("   uniform offset used CORRECTLY (convolved), V_slot/n=%.3e -> p = %.4e" % (Vs, e))
print("   uniform half-width a = xr/(2k) = %.4f  vs half-gap d = %.4f  -> a/d = %.4f < 1"
      % (xr / (2 * KDEC), d, (xr / (2 * KDEC)) / d))
print("   => bounded offset, |u| < d always => NO FLOOR.  Gaussianizing invents the 8.7e-44 floor.")
print("   logistic offset scale s = xr/(2k): d/s = %.4f = k/2 exactly -> floor ~ exp(-d/s)"
      % (d / (xr / (2 * KDEC))))
print()

# ---------- 5. what the published V_static means as a trim residual
print("5. THE PUBLISHED V_static RE-READ AS A TRIM RESIDUAL")
for T in (353, 300, 4):
    lv, V_slot, xr = parts(T)
    Vst = qdecode.threshold_band_variance(xr)
    print("   T=%3d K: V_static=%.4f -> sigma_trim = %.4f in x  = %.2f %% of ladder range"
          % (T, Vst, math.sqrt(Vst), 100 * math.sqrt(Vst) / xr))
print("   sigma_trim = c * xr/k_dec with c = 1/sqrt(12) = %.4f" % (1 / math.sqrt(12)))
print("   c = delta_n_th / dn  => the code assumes the trim locates n_th to %.1f %% of the"
      % (100 / math.sqrt(12)))
print("   tanh transition width. That is a TRIM-LOOP claim, not a property of k.")
print()

# ---------- 6. margin model: the replacement design rule
print("6. REPLACEMENT DESIGN RULE (tangent band must clear the level gap)")
print("   band = 2*xr/k ; level gap = xr/2 ; need band < gap => k > 4")
for k in (4, 6, 8, 12, 16, 24, 32):
    print("   k=%2d: d_eff/d = 1 - 4/k = %+.3f" % (k, 1 - 4.0 / k))
