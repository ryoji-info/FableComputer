# -*- coding: utf-8 -*-
"""Part 3: the steelman — downstream threshold mismatch referred back through
the comparator's incremental gain. This DOES scale as x_range/k. What is c?"""
import math
import qconstants as C
import qmode, qnoise as Q, qdecode, qmac, qerrors

x_rail = math.sqrt(2 * qerrors.N_RAIL)


def parts(T, N_op=400):
    st, xr = qmac.levels_at_decision(T, N_op)
    V_slot = max(s.V for s in st.values()) + qdecode.decoder_amp_noise(T)
    lv = [st[(0, 0)].x, 0.5 * (st[(0, 1)].x + st[(1, 0)].x), st[(1, 1)].x]
    return lv, V_slot, xr


print("STEELMAN: an output-referred error d_y (downstream threshold mismatch, or")
print("the trim loop's residual read at the output) refers back to the input as")
print("   d_x = d_y / (dA_out/dA_in)|_th ,   dA_out/dA_in = A_pump*g_max*k/(2*A_swing)")
print("   => d_x = [2*d_y/(x_rail*g_max)] * (x_range/k)   -- the 1/k scaling IS real.")
print()
for T in (353, 300, 4):
    lv, V_slot, xr = parts(T)
    g_max = math.sqrt(qdecode.G_dec(T))
    gain = x_rail * g_max * 16.0 / (2 * xr)
    print("  T=%3d K: g_max=%.3f  comparator gain at threshold dA_out/dA_in = %.1f" % (T, g_max, gain))
print()

T = 300.0
lv, V_slot, xr = parts(T)
g_max = math.sqrt(qdecode.G_dec(T))
d = 0.5 * (lv[1] - lv[0])
V16 = V_slot / 16.0
print("At 300 K:  x_rail = %.2f  g_max = %.3f  x_range = %.3f  half-gap d = %.3f"
      % (x_rail, g_max, xr, d))
print()
print("  c  ==  2*d_y/(x_rail*g_max)   for a given output-referred mismatch d_y:")
for frac in (0.001, 0.01, 0.05, 0.10, 0.4614):
    dy = frac * x_rail
    c = 2 * dy / (x_rail * g_max)
    sig = c * xr / 16.0
    V = V16 + sig ** 2
    p = 0.75 * math.erfc(d / math.sqrt(2 * V))
    print("   d_y = %6.2f%% of rail -> c = %.5f -> sigma_static = %.4f -> q2bit_avg16 = %.4e"
          % (100 * frac, c, sig, p))
print()
c_code = 1 / math.sqrt(12)
dy_code = c_code * x_rail * g_max / 2
print("  The CODE's c = 1/sqrt(12) = %.4f implies d_y = %.2f = %.1f %% of the rail"
      % (c_code, dy_code, 100 * dy_code / x_rail))
print("  i.e. an output-referred mismatch of ~half the logic swing on a TRIMMED cell.")
print("  A 1%%-of-rail mismatch gives c = %.5f, i.e. %.0fx smaller in amplitude,"
      % (2 * 0.01 * x_rail / (x_rail * g_max), c_code / (2 * 0.01 / g_max)))
print("  %.0fx smaller in variance." % ((c_code / (2 * 0.01 / g_max)) ** 2))
print()
print("GENERALISED FLOOR:  sigma_static = c*x_range/k, d = x_range/4")
print("  p_floor(c,k) = 0.75*erfc( k / (4*sqrt(2)*c) )")
print("  check: c = 1/sqrt(12) -> k/(4*sqrt(2)/sqrt(12)) = sqrt(3/8)*k  (the promoted note's form)")
for c in (1 / math.sqrt(12), 0.1, 0.0294, 0.00625):
    arg = 16.0 / (4 * math.sqrt(2) * c)
    fl = 0.75 * math.erfc(arg) if arg < 27 else 0.0
    print("   c = %.5f -> p_floor(k=16) = %s" % (c, ("%.4e" % fl) if fl > 0 else "< 1e-300 (none)"))
print()
print("  cross-check vs promoted note 2026-07-14 sec.3: 0.75*erfc(sqrt(3/8)*16) = %.4e"
      % (0.75 * math.erfc(math.sqrt(3.0 / 8.0) * 16)))
