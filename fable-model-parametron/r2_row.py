# -*- coding: utf-8 -*-
"""r2: a row of sixteen pairs at the operating point (0.94 V, pump 25 %, links 6 %, no link capacitors).

What it shows.
  1. The run without noise or spread (the reference run): which pairs are right, the level of every pair
     when the next pair takes its decision and at the end of its on-time, and the phase step per link.
  2. Runs with the physical noise of the 225-GHz circuit and a 3 % spread of the tank inductance from pair
     to pair: wrong decisions (a decision is wrong when its phase lies more than 90 degrees from the
     reference run's), the rms phase error, the first-wrong events, and whether the row "holds" by the
     rule of the paper (all reference pairs 1 to 15 right, no wrong decision at pair 14, rms phase error at
     pair 14 at most 8 degrees).
Pair 0 is driven with the pattern 1 0 1 1 0 0 1 0, once; slot 0 is left out of every count.
The noise differs from that of the session's batches (numpy against the generator of the graphics processor,
and double against single precision), so the noisy counts are to be compared as counts.
Every number is a result of the model.  Run time on the reference computer: about 2 minutes.
usage: python r2_row.py
"""
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import numpy as np
import batch
import analysis
import cellbase

NRUN = 32
batch.start(16)
SET = [cellbase.setting("row", N=NRUN, scale=cellbase.PHYS_NOISE, lsig=0.03, grp="physical noise, inductance spread 3 %")]
m, arr = batch.run(SET, "r2_row")
r = analysis.rows(m, arr)[0]
d = arr[0]
ir = np.where(d["ref"])[0][0]
print("r2: row of 16 pairs, cell F, 0.94 V, pump 25 %, links 6 %, pump step 0.75 turn, period 69.3 ps, no link capacitors")
print("\n1. Run without noise or spread")
print("   pairs right (pattern on each pair's own axis, end of the on-time): %d of 16; pairs 1 to 15 all right: %s" % (sum(r["ref_ok"]), all(r["ref_ok"][1:])))
print("   smallest margin of pairs 1 to 15 (smallest projection over mean level): %.3f" % min(r["margin"][1:]))
print("   level per half when the next pair decides (mV), pairs 0 to 15: " + " ".join("%.1f" % x for x in r["levelE_mV"]))
print("   level per half at the end of the on-time (mV), pairs 0 to 15:  " + " ".join("%.1f" % x for x in r["level_mV"]))
print("   phase step per link at the moment of decision (deg), links 0-1 to 14-15: " + " ".join("%.1f" % x for x in r["phase_step_deg"]))
print("   median phase step %.2f deg (the pump step of 0.75 turn of pump phase is 135 deg of carrier phase)" % np.median(r["phase_step_deg"]))
print("   frequency of the last pair late in its on-time (phase step between its last two windows) %.5f model THz (%.2f GHz); mean supply power %.2f mW per pair" % (r["f_last"], r["f_last"] / cellbase.K * 1e3, r["P_mW"]))
print("\n2. %d runs with physical noise and a 3 %% spread of the inductance (%d decisions per pair)" % (NRUN, r["n_dec"]))
print("   wrong decisions at pair 14: %d of %d; at pairs 1 to 15: %d of %d" % (r["wrong_k"], r["n_dec"], r["wrong_all"], 15 * r["n_dec"]))
print("   rms phase error at decision, pairs 1 to 15 (deg): " + " ".join("%.2f" % x for x in r["dev_early_deg"][1:]))
print("   first-wrong events: %d in %d decisions at risk" % (r["events"], r["risk"]))
print("   row holds: %s" % ("yes" if r["holds"] else "no"))
print("\nSession, batch chain_g29 (graphics processor, single precision), the same rules:")
print("   no noise or spread: 16 of 16 right; level at pair 14 230.0 mV when the next pair decides, 188.6 mV at the end of the on-time; phase step 132.7 to 135.2 deg")
print("   32 runs, physical noise and 3 % spread: 0 wrong of 224 at pair 14, rms phase error 3.88 deg at pair 14, 0 first-wrong events in 3360, holds")
