# -*- coding: utf-8 -*-
"""Frozen values of the cell and of the operating point, in the scaled units of the model.

The model runs every time of the 225-GHz circuit divided by K = 1.075 / 0.225 (see MODEL.md, section 2).
Units: V, mA, fF, nH, kohm, ps, um.  In these units the circuit is also the 1-THz-class cell.

Where the values come from.
  CELL_F   the parameters of cell F, as tuned in the design study and stored with every batch of the paper
           in the "ov" entry of each setting.  They were made from these design choices: a quarter of the
           published 0.45-THz diode per diode (10 fF of capacitance and 3 ohm of contact for the full device),
           a tank of 16 fF per half at 225 GHz, a quality factor of 4, a coupling of the half windings of 0.3,
           a diode delay of 100 fs (all physical), each time, capacitance and inductance divided by K.
           R_L is omega L_odd / Q with omega = 2 pi 1.075 rad/ps.
  Ck, jscale
           the two values that the runner took from the older design modules and that the "ov" entry does
           not set.  Ck is infinite (a galvanic coupler: node A of the stub joins the pad through R_k alone)
           and jscale is 1.0 (the diode law is used as given).  The older modules gave these two values for
           every end capacitance they were asked about.
  IV       the diode law of the batches: the central law of rtdiv.py with its current times 0.9333, its
           voltage axis stretched by 1.667 and an added odd current of 2.218 tanh(v / 0.05), per full device.
           It gives a peak of 25.4 mA near 0.75 V and a valley of 11.4 mA near 1.30 V.

The older modules derived further values (for example a peak-point supply level, used when a setting gives
the supply as a factor "fx" instead of a level "V").  Every setting of the paper gives "V", so the package
asks for it.  Estimates only: nothing here is a measured device.
"""
import math

K = 1.075 / 0.225                       # time scale between the 225-GHz circuit and the model
F_CARRIER = 1.076                       # carrier of the batches in the model (THz); 225.2 GHz in the 225-GHz circuit
PHYS_NOISE = 1.0 / K                    # noise power factor of the 225-GHz circuit at 353 K ("scale"); 1.0 is the 1-THz-class cell
IV = (0.9333, 1.667, 2.218)             # diode law of the batches (current scale, voltage stretch, added odd current)

CELL_F = {"Z0": 100.0, "s": 150.0, "tau": 1000000.0, "l": 2.0, "area": 0.25, "cd": 2.0930232558139537,
          "tau_d": 0.020930232558139538, "rho": 0.012, "Rb": 0.0025, "Cb": 1.0, "Lodd": 0.005503702610480282,
          "kL": 0.3, "RL": 0.009293585532637455, "Cp": 2.8255813953488373, "Rk": 0.001}
BASE = dict(CELL_F, Ck=float("inf"), jscale=1.0)

# The 160-GHz pair of the paper's Sections 2.4 and 13 (cell "c160" of the design study), for r1_pair.py cell=c160.
# The same diode (2.5 fF, 100 fs and 12 ohm per diode, physical), a tank of 22.5 fF per half (20 fF of metal
# capacitor) and an odd-mode inductance of 37.70 pH per half, a quality factor of 4.  It has its own time scale:
# model time = physical time / K_160, so that its carrier is again 1.075 model THz.  No batch of the paper uses it.
K_160 = 1.075 / 0.160
CELL_160 = {"Z0": 100.0, "s": 150.0, "tau": 1000000.0, "l": 2.0, "area": 0.25, "cd": 1.4883720930232558,
            "tau_d": 0.014883720930232559, "rho": 0.012, "Rb": 0.0025, "Cb": 1.0, "Lodd": 0.005611688603701524,
            "kL": 0.3, "RL": 0.009475931334246972, "Cp": 2.9767441860465116, "Rk": 0.001}

# Names a setting may give as its "design".  The batches of the paper name "P2", the design of an older study
# whose values the "ov" entry replaced, except Ck and jscale, which are the same as here.
DESIGNS = {"F": BASE, "P2": BASE}


def cell_info(name, c_end=0.0):
    """Base values of a half and of a pair for the runner (the keys of runs3.KEYS_H and runs3.KEYS_P).
    c_end is accepted for the runner's call and has no effect: the stub is fixed, not retuned."""
    if name not in DESIGNS:
        raise KeyError("unknown design %r; this package knows %s" % (name, ", ".join(sorted(DESIGNS))))
    return dict(DESIGNS[name])


def info_json(names):
    return {nm: {k: (v if not (isinstance(v, float) and not math.isfinite(v)) else "inf") for k, v in cell_info(nm).items()} for nm in names}


def setting(topo, **over):
    """One setting at the operating point of the paper: cell F, supply 0.94 V, pump 25 % of the supply at twice
    the carrier, pump phase pi (0.25 + 1.5 d) at clock depth d, links of 6 % (mutual inductance only, no link
    capacitors), period 14.5 model ps (69.3 ps in the 225-GHz circuit), on for 0.75 of it, phase keying.
    No noise and no spread unless given: scale=PHYS_NOISE is the physical noise of the 225-GHz circuit,
    lsig=0.03 a 3 % spread of the tank inductance.  N is the number of runs with noise and spread; one more
    run without either (the reference) is always made."""
    s = dict(design="F", V=0.94, fd=F_CARRIER, T=14.5, duty=0.75, pump=0.25, pph=0.25, pstep=1.5, mode="psk",
             scale=0.0, N=0, kmsg=1.0, cc=0.0, km=-0.06, ov=dict(CELL_F), topo=topo)
    s.update(over)
    return s
