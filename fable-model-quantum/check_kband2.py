# -*- coding: utf-8 -*-
"""Part 2: Appendix-A yield consequence of k_dec=16, and the bounded column."""
import math, sys
import numpy as np
sys.path.insert(0, "../fable-model-chain")
import qconstants as C
import qmode, qnoise as Q, qdecode, qmac, qerrors

x_rail = math.sqrt(2 * qerrors.N_RAIL)
TEMPS = (353, 300, 150, 77, 48, 20, 4)


def parts(T, N_op=400):
    st, xr = qmac.levels_at_decision(T, N_op)
    V_slot = max(s.V for s in st.values()) + qdecode.decoder_amp_noise(T)
    lv = [st[(0, 0)].x, 0.5 * (st[(0, 1)].x + st[(1, 0)].x), st[(1, 1)].x]
    return lv, V_slot, xr


print("A. APPENDIX-A YIELD RULE vs the k_dec=16 requirement")
print("   Part-I / disorder.py: k_eff = n/sqrt((n/k0)^2 + sigma^2), K0=8, K_MIN=5")
print("   k_eff <= k0 ALWAYS (a puddle can only broaden) -> k_eff>=16 needs k0>=16.")
n = 1e12                                   # cm^-2
for target, k0 in [(5, 8), (8, math.inf), (16, math.inf), (80, math.inf),
                   (80, 160.0), (80, 100.0)]:
    if math.isinf(k0):
        s_crit = n / target
        tag = "k0 -> inf (necessary condition)"
    else:
        s_crit = n * math.sqrt(1.0 / target**2 - 1.0 / k0**2)
        tag = "k0 = %.0f" % k0
    print("   k_eff >= %3.0f, %-32s : sigma <= %.3e cm^-2  (= %.4f n)"
          % (target, tag, s_crit, s_crit / n))
print("   literature puddle sigma: 2.5e9 (ultra-flat hBN) .. 4.0e10 (typical encapsulated)")
print()
print("   Part-I quotes sigma <= 0.16 n = 1.6e11 for the k>=8 / k_min=5 logic rule.")
print("   k_dec=16 at the LADDER plane == k=80 at the CELL plane (x_rail/x_r = 5.0)")
print("   -> sigma <= n/80 = 1.25e10 cm^-2 : a %.1fx tightening; the typical-encapsulated"
      % (0.16 / (1.0 / 80)))
print("      end of Part-I's own literature band (4e10) MISSES by %.1fx." % (4e10 / 1.25e10))
print()

# MC yield under the disorder.py ensemble, at the tightened criterion
import disorder as D
rng = np.random.default_rng(11)
logs = rng.uniform(np.log(2.5e9), np.log(4e10), 200000)
sig = np.exp(logs)
for k0, kmin, label in [(8.0, 5.0, "Part-I logic rule  (k0=8,  k_min=5)"),
                        (100.0, 80.0, "ladder k_dec=16    (k0=100, k_min=80)"),
                        (160.0, 80.0, "ladder k_dec=16    (k0=160, k_min=80)")]:
    s_crit = n * math.sqrt(1.0 / kmin**2 - 1.0 / k0**2)
    y = float(np.mean(sig < s_crit))
    print("   MC yield, literature ensemble, %-38s : %5.1f %%" % (label, 100 * y))
print()

print("B. BOUNDED CORRECTED COLUMN (band is deterministic: drop it; add metastability)")
print("   %3s | %11s | %11s | %11s | %11s" % ("T", "published", "LOWER (c=0)", "margin UB", "ratio pub/LB"))
for T in TEMPS:
    lv, V_slot, xr = parts(T)
    V16 = V_slot / 16.0
    s16 = math.sqrt(V16)
    q = lambda z: 0.5 * math.erfc(z / math.sqrt(2))
    d1 = 0.5 * (lv[1] - lv[0]); d2 = 0.5 * (lv[2] - lv[1])
    p_drop = 0.25 * q(d1 / s16) + 0.5 * (q(d1 / s16) + q(d2 / s16)) + 0.25 * q(d2 / s16)
    g_max = math.sqrt(qdecode.G_dec(T))
    gain_cmp = x_rail * g_max * 16.0 / (2 * xr)
    gain_logic = x_rail * g_max * 8.0 / (2 * x_rail)
    dcrit = (x_rail / 2) / (gain_cmp * gain_logic)
    phi = lambda z: math.exp(-0.5 * z * z) / math.sqrt(2 * math.pi)
    p_meta = sum(pr * 2 * dcrit * phi(d_ / s16) / s16
                 for d_, pr in ((d1, 0.25), (d1, 0.5), (d2, 0.5), (d2, 0.25)))
    lb = p_drop + p_meta
    de1, de2 = d1 - xr / 16.0, d2 - xr / 16.0
    ub = 0.25 * q(de1 / s16) + 0.5 * (q(de1 / s16) + q(de2 / s16)) + 0.25 * q(de2 / s16)
    pub = qmac.error_2bit(T, 400, n_avg=16)
    print("   %3d | %11.4e | %11.4e | %11.4e | %11.3e"
          % (T, pub, lb, ub, pub / lb))
print()
print("C. WHAT COLLAPSES THE RANGE: the trim residual c = delta_n_th/dn")
print("   sigma_trim = c * x_range/k_dec ; the code's /12 <=> c = 0.2887, Gaussian.")
lv, V_slot, xr = parts(300)
d = 0.5 * (lv[1] - lv[0]); V16 = V_slot / 16
for c in (0.0, 0.01, 0.03, 0.1, 0.2887, 0.5):
    V = V16 + (c * xr / 16.0) ** 2
    print("   c = %.4f -> sigma_trim = %.4f (%.2f %% of range) -> q2bit_avg16(300K) = %.4e"
          % (c, c * xr / 16, 100 * c / 16, 0.75 * math.erfc(d / math.sqrt(2 * V))))
