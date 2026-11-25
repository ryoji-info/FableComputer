# -*- coding: utf-8 -*-
"""r5: the change of units.  The 225-GHz design and the 1-THz-class cell are one circuit: every time,
capacitance and inductance of the 225-GHz circuit is divided by K = 1.075 / 0.225 to give the 1-THz-class
cell, and every frequency is multiplied by K.  Resistances, voltages, currents and the diode law stay.
The model runs in the units of the 1-THz-class cell; with the noise power factor 1/K it is the 225-GHz
circuit at its own temperature, with factor 1 the 1-THz-class cell at the same temperature.

What it shows.
  1. The cell table in both sets of physical values.
  2. One short run of two linked pairs (a constant supply of 0.94 V with the 25 % pump, a drive tone into
     the first pair for the first quarter of the run, thermal and shot noise), once in the units of the
     1-THz-class cell (noise factor 1/K) and once in the units of the 225-GHz circuit (every value scaled,
     noise factor 1).  The two traces of the odd signals are compared sample by sample, the second taken at
     K times the time.  They agree to rounding: the step matrices of the two runs are the same numbers.
Every number is a result of the model.  Run time on the reference computer: about 10 seconds.
usage: python r5_units.py
"""
import math
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import numpy as np
import cellbase
import fdtd3
import rtdiv

K = cellbase.K
C = cellbase.CELL_F
IV = rtdiv.variant(*cellbase.IV)
print("r5: the change of units, K = 1.075 / 0.225 = %.6f" % K)

# ---------------------------------------------------------------- 1. the cell table
Lh = C["Lodd"] / (1 + C["kL"])
Cst = C["l"] / (C["Z0"] * 1e-3 * C["s"])
Lst = C["Z0"] * 1e-3 / C["s"] * C["l"]
f0 = cellbase.F_CARRIER
rows = [
    ("diode capacitance C_d", "fF", C["cd"] * C["area"], K),
    ("diode delay tau_d", "ps", C["tau_d"], K),
    ("contact rho", "ohm", 1e3 * C["rho"], 1),
    ("pad capacitor C_p", "fF", C["Cp"], K),
    ("tank per half (C_d + C_p)", "fF", C["cd"] * C["area"] + C["Cp"], K),
    ("odd-mode inductance per half L_odd", "pH", 1e3 * C["Lodd"], K),
    ("half winding L_h", "pH", 1e3 * Lh, K),
    ("coupling of the half windings k", "", C["kL"], 1),
    ("damping resistor R_L (in series with each half)", "ohm", 1e3 * C["RL"], 1),
    ("supply resistor R_b", "ohm", 1e3 * C["Rb"], 1),
    ("supply node capacitance C_b", "fF", C["Cb"], K),
    ("coupler R_k", "ohm", 1e3 * C["Rk"], 1),
    ("stub capacitance (4 sections, in all)", "fF", Cst, K),
    ("stub inductance (in all)", "pH", 1e3 * Lst, K),
    ("link: mutual inductance, 6 % of L_odd", "pH", 0.06 * 1e3 * C["Lodd"], K),
    ("carrier", "GHz", 1e3 * f0, 1.0 / K),
    ("pump (twice the carrier)", "GHz", 2e3 * f0, 1.0 / K),
    ("clock period", "ps", 14.5, K),
    ("clock edge (raised cosine)", "ps", 3.0, K),
    ("on-time (0.75 of the period)", "ps", 0.75 * 14.5, K),
    ("time step of the integrator", "ps", 0.0025, K),
    ("reading window", "ps", 1.0, K),
    ("supply level", "V", 0.94, 1),
    ("pump level (25 % of the supply)", "mV", 235.0, 1),
    ("drive current of an input pair", "mA", 0.4, 1),
    ("diode peak current (a quarter of the full device)", "mA", 0.25 * rtdiv.features(IV)["Jp"], 1),
    ("model noise factor 'scale' for this circuit at 353 K", "", 1.0, 1.0 / K),
]
print("\n1. Cell table: 1-THz-class cell (the model's units) and 225-GHz circuit")
print("   %-50s %-5s %14s %14s" % ("quantity", "unit", "1-THz class", "225 GHz"))
for nm, u, v, f in rows:
    print("   %-50s %-5s %14.5g %14.5g" % (nm, u, v, v * f))
print("   The noise factor: a capacitance K times larger has K times less kT/C noise power, and the shot-noise")
print("   bandwidth is K times smaller, so the 225-GHz circuit has 1/K = %.4f of the noise power of the 1-THz-class cell." % (1 / K))


# ---------------------------------------------------------------- 2. one short run in both units
def two_pairs(scale_t, noise):
    """Two linked pairs; scale_t = 1 for the 1-THz-class units, K for the 225-GHz circuit."""
    par = dict(C)
    for k in ("cd", "tau_d", "Cp", "Cb", "Lodd", "tau"):
        par[k] = C[k] * scale_t
    par["s"] = C["s"] / scale_t                          # stub: same length, K times slower, so L' and C' are K times larger
    fab = fdtd3.PairFabric(1, 2, N=4, dt=0.0025 * scale_t, iv=IV, mlinks=[(0, 1)], mk=np.array([-0.06, 0.0, 0.0, 0.0]), **par)
    fab.enable_noise(T=353.0, fano=1.0, scale=noise, seed=3)
    wd = fdtd3.W0 * f0 / scale_t
    half = np.array([1.0, -1.0]).reshape(1, 1, 2)
    drive = np.array([1.0, 0.0]).reshape(1, 2, 1)
    t_end = 30.0 * scale_t
    nst = int(round(t_end / fab.dt))
    out = np.zeros((nst, 2))
    for i in range(nst):
        t = (i + 1) * fab.dt
        ramp = min(1.0, t / (3.0 * scale_t))
        v = 0.94 * ramp * (1.0 + 0.25 * math.cos(2 * wd * t + 0.25 * math.pi))
        iB = 0.4 * drive * half * math.cos(wd * t) * (1.0 if t < 7.5 * scale_t else 0.0)
        fab.step(v, iB)
        out[i] = np.asarray(fab.odd_B())[0]
    return out, fab


a, fa = two_pairs(1.0, 1.0 / K)
b, fb = two_pairs(K, 1.0)
print("\n2. Two linked pairs, 30 model ps (%.1f ps in the 225-GHz circuit), %d steps, noise of the 225-GHz circuit in both" % (30 * K, len(a)))
print("   step matrices: largest relative difference of P between the two units %.2e, of Q against Q of the 225-GHz run divided by K %.2e"
      % (np.abs(fa.P - fb.P).max() / np.abs(fa.P).max(), np.abs(fa.Q - fb.Q / K).max() / np.abs(fa.Q).max()))
for p in (0, 1):
    big = np.abs(a[:, p]).max()
    dif = np.abs(a[:, p] - b[:, p]).max()
    print("   pair %d: largest odd signal %.1f mV; largest difference between the two traces %.3e mV (%.1e of the signal)" % (p, 1e3 * big, 1e3 * dif, dif / big))
for j in (1000, 4000, 8000, 11999):
    print("   sample %5d, t = %6.3f model ps = %7.3f ps: pair 0 %+.9f V / %+.9f V, pair 1 %+.9f V / %+.9f V"
          % (j, (j + 1) * 0.0025, (j + 1) * 0.0025 * K, a[j, 0], b[j, 0], a[j, 1], b[j, 1]))
print("   (each pair of numbers: 1-THz-class units / 225-GHz units at K times the time)")
