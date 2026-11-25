# -*- coding: utf-8 -*-
"""r1: one pair of cell F on a constant supply, without clock and without neighbours.

What it shows.
  1. The diode law and the values of the cell.
  2. The pair's own oscillation range in supply level: below it the pair is silent, above it it oscillates
     by itself and keeps any phase.  Method of the design study (its scripts are not in this package): a small seed
     pulse at 2 model ps, the swing of the odd signal from 45 to 70 model ps, "oscillates" above 5 mV.
  3. Table P-1 of the session: supply levels 0.82 to 1.06 V and pumps of 0 to 40 % at twice the carrier.
     For each, twelve runs start from a small seed of twelve phases, which is removed after 6 model ps.
     Level after 520 to 570 ps (physical); "two phases" when the twelve runs end within 10 degrees of two
     phases half a turn apart; the settling time is when that was reached for good.
  4. The values set beside the session's stored table P-1 and beside BLIND_SPEC_T1.md.
Times are physical (225-GHz circuit) unless marked "model".  Every number is a result of the model.
Run time on the reference computer: about 2 minutes (numpy, double precision).
With cell=c160 the listing runs the 160-GHz pair of the paper's Sections 2.4 and 13 instead (cellbase.CELL_160,
with that pair's own time scale): parts 1 to 3, with the session's table R-9 in place of P-1.  Its seed of
6 model ps is 40.3 ps there, and its levels are read after 732 to 806 ps.
usage: python r1_pair.py [cell=c160]
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

CELL = dict(a.split("=", 1) for a in sys.argv[1:] if "=" in a).get("cell", "F")
if CELL not in ("F", "c160"):
    sys.exit("usage: python r1_pair.py [cell=c160]")
K = cellbase.K if CELL == "F" else cellbase.K_160
IV = rtdiv.variant(*cellbase.IV)
PAR = dict(cellbase.CELL_F if CELL == "F" else cellbase.CELL_160)
CIRC = "225-GHz circuit" if CELL == "F" else "160-GHz circuit"
if CELL == "F":
    print("r1: one pair of cell F on a constant supply")
    print("K = 1.075 / 0.225 = %.5f (model time = physical time / K)" % K)
else:
    print("r1: one pair of the 160-GHz cell (c160) on a constant supply, pump at 320 GHz")
    print("K = 1.075 / 0.160 = %.5f (model time = physical time / K)" % K)

# ---------------------------------------------------------------- 1. diode law and cell
f = rtdiv.features(IV)
print("\n1. Diode law per full device: peak %.2f mA at %.3f V, valley %.2f mA at %.3f V, peak-to-valley ratio %.2f, steepest slope %.2f mS at %.3f V"
      % (f["Jp"], f["Vp"], f["Jv"], f["Vv"], f["PVCR"], f["g_min"], f["V_gmin"]))
print("   one diode carries %.2f of it: peak %.3f mA, valley %.3f mA, steepest slope %.3f mS" % (PAR["area"], PAR["area"] * f["Jp"], PAR["area"] * f["Jv"], PAR["area"] * f["g_min"]))
Lh = PAR["Lodd"] / (1 + PAR["kL"])
print("   cell (model units / " + CIRC + "): C_d %.4f / %.3f fF, C_p %.4f / %.3f fF, L_odd %.4f / %.3f pH, L_h %.4f / %.3f pH, k %.2f,"
      % (PAR["cd"] * PAR["area"], PAR["cd"] * PAR["area"] * K, PAR["Cp"], PAR["Cp"] * K, 1e3 * PAR["Lodd"], 1e3 * PAR["Lodd"] * K, 1e3 * Lh, 1e3 * Lh * K, PAR["kL"]))
print("   R_L %.3f ohm, rho %.1f ohm, R_k %.1f ohm, R_b %.2f ohm, C_b %.3f / %.3f fF, tau_d %.5f / %.4f ps"
      % (1e3 * PAR["RL"], 1e3 * PAR["rho"], 1e3 * PAR["Rk"], 1e3 * PAR["Rb"], PAR["Cb"], PAR["Cb"] * K, PAR["tau_d"], PAR["tau_d"] * K))
wq = fdtd3.W0 * 1.075
print("   quality factor of the tank, omega L_odd / R_L at 1.075 model THz: %.3f" % (wq * PAR["Lodd"] * 1e3 / (1e3 * PAR["RL"])))


# ---------------------------------------------------------------- 2. own oscillation range (the method of the design study)
def run_free(par, V, t_end=70.0, seed_mV=0.5):
    V = np.atleast_1d(np.asarray(V, float))
    B = len(V)
    fab = fdtd3.PairFabric(B, 1, N=4, dt=0.0025, iv=IV, **par)
    nst = int(round(t_end / fab.dt))
    sig = np.zeros((nst, B))
    vs = V.reshape(B, 1)
    half = np.array([1.0, -1.0]).reshape(1, 1, 2)
    for i in range(nst):
        t = (i + 1) * fab.dt
        ramp = 0.5 * (1 - math.cos(math.pi * min(t / 3.0, 1.0)))
        v = vs * ramp
        iB = seed_mV * 1e-3 / 0.1 * half * math.exp(-((t - 2.0) / 0.5) ** 2) * math.cos(fdtd3.W0 * 1.075 * t) if seed_mV else 0.0
        fab.step(v, iB)
        sig[i] = np.asarray(fab.odd_B())[:, 0]
    return fab, sig


def measure(sig, dt, t0, t1):
    i0, i1 = int(t0 / dt), int(t1 / dt)
    x = sig[i0:i1]
    amp = 0.5 * (x.max(0) - x.min(0)) * 1e3
    fr = np.zeros(x.shape[1])
    for b in range(x.shape[1]):
        y = x[:, b] - x[:, b].mean()
        zc = np.where((y[:-1] < 0) & (y[1:] >= 0))[0]
        if len(zc) > 3:
            tz = (zc + (-y[zc]) / (y[zc + 1] - y[zc])) * dt
            fr[b] = (len(tz) - 1) / (tz[-1] - tz[0])
    return amp, fr


Vs = np.linspace(0.85, 1.25, 41)
fab, sig = run_free(PAR, Vs)
amp, fr = measure(sig, fab.dt, 45.0, 70.0)
osc = np.where(amp > 5.0)[0]
mid = osc[len(osc) // 2]
print("\n2. Own oscillation, no pump (supply 0.85 to 1.25 V in steps of 10 mV; swing from 45 to 70 model ps)")
print("   oscillates by itself from %.2f to %.2f V; at %.2f V: %.1f mV per half, %.5f model THz = %.1f GHz" % (Vs[osc[0]], Vs[osc[-1]], Vs[mid], amp[mid], fr[mid], fr[mid] / K * 1e3))
print("   swing (mV) by supply level: " + ", ".join("%.2f V %.1f" % (v, a) for v, a in zip(Vs, amp) if 0.90 <= v <= 1.20 and abs(round(v * 100) % 2) == 0))
if CELL == "F":
    print("   session record of cell F (not in this package): 0.97 to 1.14 V; at 1.06 V 283.2 mV, 1.07345 model THz (224.7 GHz)")
    print("   BLIND_SPEC_T1.md does not state the range; the two codes written from it found 0.97 to 1.14 V (independent/README.md)")
else:
    print("   session record of cell c160 (not in this package): 0.97 to 1.14 V; at 1.06 V 294.9 mV, 1.07310 model THz (159.7 GHz)")

# ---------------------------------------------------------------- 3. table P-1 (the method of the design study)
FD = 1.076
VS = np.array([0.82, 0.85, 0.88, 0.91, 0.94, 0.97, 1.00, 1.03, 1.06])
NPH = 12
T_END, T_SEED = 120.0, 6.0
P1 = {0.0: "silent|silent|silent|silent|silent|160 mV, any phase|224 mV, any phase|258 mV, any phase|279 mV, any phase",
      0.10: "silent|silent|silent|silent|143 mV, two phases, 38 ps|211 mV, two phases, 38 ps|247 mV, two phases, 67 ps|273 mV, two phases, 191 ps|291 mV, two phases, 263 ps",
      0.15: "silent|silent|silent|silent|171 mV, two phases, 33 ps|219 mV, two phases, 33 ps|251 mV, two phases, 48 ps|275 mV, two phases, 105 ps|272 mV, any phase",
      0.20: "silent|silent|silent|123 mV, two phases, 33 ps|185 mV, two phases, 29 ps|224 mV, two phases, 33 ps|252 mV, two phases, 43 ps|273 mV, two phases, 72 ps|231 mV, any phase",
      0.25: "silent|silent|58 mV, two phases, 33 ps|148 mV, two phases, 33 ps|193 mV, two phases, 29 ps|225 mV, two phases, 33 ps|248 mV, two phases, 38 ps|264 mV, two phases, 67 ps|229 mV, any phase",
      0.30: "silent|silent|107 mV, two phases, 33 ps|160 mV, two phases, 33 ps|195 mV, two phases, 33 ps|220 mV, two phases, 33 ps|235 mV, two phases, 38 ps|238 mV, two phases, 48 ps|silent",
      0.40: "silent|79 mV, two phases, 33 ps|124 mV, two phases, 33 ps|146 mV, two phases, 33 ps|143 mV, two phases, 33 ps|silent|silent|silent|silent"}
R9 = {0.0: "silent|silent|silent|silent|silent|177 mV, any phase|237 mV, any phase|270 mV, any phase|291 mV, any phase",
      0.10: "silent|silent|silent|silent|168 mV, two phases, 47 ps|225 mV, two phases, 54 ps|260 mV, two phases, 87 ps|285 mV, two phases, 195 ps|304 mV, two phases, 443 ps",
      0.15: "silent|silent|silent|108 mV, two phases, 47 ps|190 mV, two phases, 47 ps|233 mV, two phases, 54 ps|263 mV, two phases, 60 ps|287 mV, two phases, 336 ps|270 mV, any phase",
      0.20: "silent|silent|silent|152 mV, two phases, 47 ps|202 mV, two phases, 40 ps|237 mV, two phases, 54 ps|263 mV, two phases, 60 ps|283 mV, two phases, 94 ps|244 mV, any phase",
      0.25: "silent|silent|110 mV, two phases, 47 ps|169 mV, two phases, 47 ps|208 mV, two phases, 47 ps|236 mV, two phases, 47 ps|256 mV, two phases, 54 ps|268 mV, two phases, 60 ps|266 mV, two phases, 148 ps",
      0.30: "silent|58 mV, two phases, 47 ps|135 mV, two phases, 47 ps|176 mV, two phases, 47 ps|205 mV, two phases, 47 ps|224 mV, two phases, 47 ps|229 mV, two phases, 54 ps|23 mV, two phases, 67 ps|silent",
      0.40: "37 mV, two phases, 47 ps|101 mV, two phases, 47 ps|123 mV, two phases, 47 ps|74 mV, two phases, 47 ps|silent|silent|silent|silent|silent"}
STORED, TAB = (P1, "P-1") if CELL == "F" else (R9, "R-9")
print("\n3. Pumped pair, twelve starting phases (table %s).  Each entry: this run / the session's stored table %s" % (TAB, TAB))
match = total = 0
for pump in (0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40):
    B = len(VS) * NPH
    fab = fdtd3.PairFabric(B, 1, N=4, dt=0.0025, iv=IV, **PAR)
    nst = int(T_END / fab.dt)
    half = np.array([1.0, -1.0]).reshape(1, 1, 2)
    vs = np.repeat(VS, NPH).reshape(B, 1)
    ph0 = np.tile(np.arange(NPH) * 2 * math.pi / NPH, len(VS)).reshape(B, 1, 1)
    w, w2 = fdtd3.W0 * FD, 2 * fdtd3.W0 * FD
    nwin = int(T_END)
    zc = np.zeros((nwin, B), complex)
    cnt = np.zeros(nwin)
    acc2 = np.zeros(B, complex)
    idc = np.zeros(B)
    n0 = int(109.0 / fab.dt)
    for i in range(nst):
        t = (i + 1) * fab.dt
        ramp = 0.5 * (1 - math.cos(math.pi * min(t / 3.0, 1.0)))
        v = vs * ramp * (1.0 + pump * math.cos(w2 * t + math.pi))
        iB = 0.05 * half * np.cos(w * t + ph0) * (1.0 if t < T_SEED else 0.0)
        fab.step(v, iB)
        o = np.asarray(fab.odd_B())[:, 0]
        k = min(int(t), nwin - 1)
        zc[k] += o * np.exp(-1j * w * t)
        cnt[k] += 1
        if i >= n0:
            isup = np.asarray(fab.supply_current(v))[:, 0]
            acc2 += isup * np.exp(-1j * w2 * t)
            idc += isup
    z = 2 * zc / cnt[:, None]
    m = nst - n0
    I2 = 2 * acc2 / m
    Vp = vs[:, 0] * pump * np.exp(1j * math.pi)
    P2 = 0.5 * np.real(Vp * np.conj(I2))
    print("   pump %2.0f %%:" % (100 * pump))
    stored = STORED[pump].split("|")
    for a, V in enumerate(VS):
        sl = slice(a * NPH, (a + 1) * NPH)
        zz = z[:, sl]
        lev = 1e3 * np.abs(zz[-10:]).mean()
        d2 = np.angle(zz ** 2)
        sp = np.degrees(np.abs(np.angle(np.exp(1j * (d2 - d2[:, :1])))).max(1)) / 2.0
        okw = np.where(sp > 10.0)[0]
        t_set = (okw[-1] + 1) if len(okw) else 0
        fin = np.angle(zz[-1])
        k2 = np.round(((fin - fin[0]) % (2 * math.pi)) / math.pi) % 2
        two = bool(lev > 5 and sp[-1] <= 10.0)
        if lev <= 5:
            txt = "silent"
        elif two:
            txt = "%.0f mV, two phases, %.0f ps" % (lev, t_set * K)
        else:
            txt = "%.0f mV, any phase" % lev
        total += 1
        match += (txt == stored[a])
        extra = ("; %d and %d of 12 on the two phases, spread %.2f deg" % ((k2 == 0).sum(), (k2 == 1).sum(), sp[-1])) if two else ""
        print("      %.2f V: %-28s / %-28s | direct current %.2f mA, pump-frequency current %.2f mA, power from the pump source %+.4f mW%s"
              % (V, txt, stored[a], idc[sl].mean() / m, np.abs(I2[sl]).mean(), P2[sl].mean(), extra))
print("   %d of %d entries equal the stored table %s as printed" % (match, total, TAB))
if CELL != "F":
    sys.exit(0)          # part 4 sets cell F beside its specification

# ---------------------------------------------------------------- 4. against BLIND_SPEC_T1.md
print("\n4. Against BLIND_SPEC_T1.md (values of the 1-THz-class cell, which are the model's units)")
spec = [("C_d (fF)", 0.5233, PAR["cd"] * PAR["area"]), ("rho (ohm)", 12.0, 1e3 * PAR["rho"]), ("tau_d (ps)", 0.02093, PAR["tau_d"]),
        ("C_p (fF)", 2.8256, PAR["Cp"]), ("L_odd (pH)", 5.5047, 1e3 * PAR["Lodd"]), ("k", 0.3, PAR["kL"]), ("R_L (ohm)", 9.29, 1e3 * PAR["RL"]),
        ("R_b (ohm)", 2.5, 1e3 * PAR["Rb"]), ("C_b (fF)", 1.000, PAR["Cb"]), ("R_k (ohm)", 1.0, 1e3 * PAR["Rk"])]
for nm, sv, mv in spec:
    print("   %-11s specification %-8g model %.5g" % (nm, sv, mv))
Cst = 1.0 / (PAR["Z0"] * 1e-3 * PAR["s"]) * PAR["l"]
Lst = PAR["Z0"] * 1e-3 / PAR["s"] * PAR["l"]
print("   stub: the specification has one node with C_s = 0.1465 fF; the model has a line of 4 sections, %.4f fF and %.4f pH in all, read at its far end"
      % (Cst, 1e3 * Lst))
print("   specification: pump at exactly twice 1.076 THz, nominal point 0.94 V and 25 %; this listing at 0.94 V and 25 %: see the row \"pump 25 %\" above")
