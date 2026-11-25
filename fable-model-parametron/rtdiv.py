# -*- coding: utf-8 -*-
"""Current-voltage law of the resonant-tunnelling diode.

Form: Schulman, De Los Santos, Chow (IEEE EDL 17, 220, 1996).  The central coefficients are a fit to a
central InGaAs/AlAs diode of the 1-2 THz oscillator family (peak 25 mA/um^2 at 0.45 V, valley
10 mA/um^2 at 0.78 V), made in the study that preceded this model.  J in mA/um^2, V in volts.
The exponent temperature is kept at 300 K.
variant() scales the current, stretches the voltage axis and adds an odd current jvalley_add tanh(v / 0.05).
The design uses variant(0.9333, 1.667, 2.218), read as mA per full device: a peak of 25.4 mA near 0.75 V
and a valley of 11.4 mA near 1.30 V, the per-device figures of a published 0.45-THz source.  Each diode of
the pair carries the fraction "area" (0.25) of that current.

Works with numpy arrays and with torch tensors (pass xp=torch).
"""
import math
import numpy as np

VT300 = 0.025852

CENTRAL = dict(A=3.541, B=0.1002, C=0.1480, D=0.02606, n1=0.2882, n2=0.1843, H=0.007984,
               jscale=1.0, vscale=1.0, jvalley_add=0.0)


def J(V, p=CENTRAL, xp=np):
    """Current density (mA/um^2) at junction voltage V (volts)."""
    v = V / p["vscale"]
    a = (p["B"] - p["C"] + p["n1"] * v) / VT300
    b = (p["B"] - p["C"] - p["n1"] * v) / VT300
    # log(1+exp(x)) written stably
    sp_a = xp.where(a > 30.0, a, xp.log1p(xp.exp(xp.clip(a, -60.0, 30.0)))) if xp is np else \
        xp.nn.functional.softplus(a)
    sp_b = xp.where(b > 30.0, b, xp.log1p(xp.exp(xp.clip(b, -60.0, 30.0)))) if xp is np else \
        xp.nn.functional.softplus(b)
    j1 = p["A"] * (sp_a - sp_b) * (math.pi / 2 + xp.arctan((p["C"] - p["n1"] * v) / p["D"]))
    e2 = p["n2"] * v / VT300
    j2 = p["H"] * (xp.exp(xp.clip(e2, -60.0, 40.0)) - 1.0)
    jv = p["jvalley_add"] * xp.tanh(v / 0.05)        # optional excess (valley) current, odd in V
    return p["jscale"] * (j1 + j2 + jv)


def variant(jscale=1.0, vscale=1.0, jvalley_add=0.0):
    p = dict(CENTRAL)
    p.update(jscale=jscale, vscale=vscale, jvalley_add=jvalley_add)
    return p


def features(p=CENTRAL):
    """Peak, valley, steepest slope and the cubic-average conductance of the law."""
    V = np.linspace(0.0, 1.3 * p["vscale"], 26001)
    j = J(V, p)
    g = np.gradient(j, V)
    ip = int(np.argmax(j[: int(0.75 * len(V))]))
    iv = ip + int(np.argmin(j[ip:]))
    ig = ip + int(np.argmin(g[ip:iv + 1]))
    Vp, Jp, Vv, Jv = V[ip], j[ip], V[iv], j[iv]
    return dict(Vp=Vp, Jp=Jp, Vv=Vv, Jv=Jv, PVCR=Jp / Jv, dV=Vv - Vp, dJ=Jp - Jv,
                g_min=g[ig], V_gmin=V[ig], g_cubic=1.5 * (Jp - Jv) / (Vv - Vp),
                g0=g[1], J_at_gmin=j[ig])


def describing(Vb, A, p=CENTRAL, nth=256):
    """Quasi-static describing function of the diode at DC junction voltage Vb and RF amplitude A
    (arrays broadcast).  Returns (mean current density, fundamental conductance per area)."""
    th = (np.arange(nth) + 0.5) * (2 * math.pi / nth)
    c = np.cos(th)
    Vb = np.asarray(Vb, float)[..., None]
    A = np.asarray(A, float)[..., None]
    j = J(Vb + A * c, p)
    jdc = j.mean(-1)
    with np.errstate(divide="ignore", invalid="ignore"):
        geff = 2.0 * (j * c).mean(-1) / A[..., 0]
    return jdc, geff


if __name__ == "__main__":
    for name, p in (("central", CENTRAL), ("high current (x2)", variant(2.0, 1.0)),
                    ("narrow voltage (x0.7)", variant(1.0, 0.7)), ("low current (x0.2)", variant(0.2, 1.0))):
        f = features(p)
        print("%-22s peak %.1f mA/um2 at %.3f V, valley %.1f at %.3f V, ratio %.2f, width %.3f V, steepest %.1f mS/um2 at %.3f V "
              "(J there %.1f), cubic average %.1f, slope at 0 V %.1f" %
              (name, f["Jp"], f["Vp"], f["Jv"], f["Vv"], f["PVCR"], f["dV"], f["g_min"], f["V_gmin"], f["J_at_gmin"],
               -f["g_cubic"], f["g0"]))
    f = features()
    print("\ndescribing function of the central diode: fundamental conductance (mS/um2) by DC bias (rows) and RF amplitude (columns)")
    amps = np.array([0.005, 0.02, 0.04, 0.06, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30])
    print("  Vb\A   " + "".join("%8.3f" % a for a in amps) + "    J_dc(A=0)  J_dc(A=0.1)")
    for Vb in (0.30, 0.38, 0.42, 0.45, 0.48, 0.52, 0.535, 0.56, 0.60, 0.65, 0.70, 0.75, 0.78, 0.82, 0.86, 0.90):
        jdc, ge = describing(np.full(amps.shape, Vb), amps)
        print("  %.3f  " % Vb + "".join("%8.1f" % x for x in ge) + "    %7.2f   %7.2f" % (J(np.array(Vb)), jdc[5]))
    print("\npower per siemens at the steepest point: %.3f V^2 ; with the cubic-average conductance and mid-point bias: %.3f V^2" %
          (f["V_gmin"] * f["J_at_gmin"] / -f["g_min"], 0.5 * (f["Vp"] + f["Vv"]) * 0.5 * (f["Jp"] + f["Jv"]) / f["g_cubic"]))
