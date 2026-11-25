# -*- coding: utf-8 -*-
"""r6: the spread budget of the four-bit ripple-carry adder (53 pairs), from the stored runs, and a few draws of
the nine spreads made here.

What it shows.
  1. From the stored runs (batches g52 and g53, 256 draws per line, without link capacitors): per line the failing
     draws, their share with its exact 95 % interval (Clopper-Pearson), wrong additions, bad pairs per thousand, and
     what the share would mean for machines of 1,000 and 10,000 pairs IF pairs failed independently. That
     independence is an assumption: no run has tested it, and no layout larger than 53 pairs has 256 draws.
  2. How one draw is made: one standard normal number per pair (per link for the link strength) for each of the nine
     spreads, times its rms value. Two draws are made here with
     numpy and their largest values are printed, to show the form of a draw.
  3. How a draw is judged: the model runs the adder with four draws of the full set at the noise of the 1-THz-class
     cell, as the line "full set x 1" of batch g52 does. The runner makes its own draws in the same way, from its own
     generators (pseed 11). A run fails when any of its 31 additions has a wrong output bit. Four runs cannot size a
     share of a few per cent; part 3 shows the rule, not the rate.
The noise of part 3 differs from that of the stored batches (numpy against the generator of the graphics processor,
double against single precision), so its counts are to be compared as counts.
Every number is a result of the model. Run time on the reference computer: about 3 minutes.
usage: python r6_spread_budget.py
"""
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import numpy as np
import tables

print("r6: spread budget of the four-bit ripple-carry adder, 53 pairs, cell F, 0.94 V, pump 25 %, links 6 %, no link capacitors")
print("\n1. From the stored runs (runs/), lines with 256 draws")
rows = tables.budget_rows()
print("   %-64s %-12s %-28s %-15s %-24s %s" % ("line", "failing", "share (exact 95 % interval)", "wrong additions", "bad pairs per thousand", "machines right, 1,000 / 10,000 pairs"))
for x in rows:
    print("   %-64s %3d of %3d   %-28s %3d of %5s     %-24s %.2f / %.3f   (%s)" % (
        x["line"][:64], x["failing"], x["runs"], "%s %% (%s to %s %%)" % (tables.pct(x["share"]), tables.pct(x["lo"]), tables.pct(x["hi"])),
        x["wrong_add"], "{:,}".format(x["n_add"]), "%.2f (%.2f to %.2f)" % (x["per_1000"], x["per_1000_lo"], x["per_1000_hi"]), x["ok_1000"], x["ok_10000"], x["batch"]))
full = [x for x in rows if x["fraction"] == 1.0 and x["noise"] == "1-THz-class cell"]
if full:
    x = full[0]
    p = x["share"] / x["pairs"]
    print("   Read per pair, %d failing draws of %d for %d pairs are %.2f bad pairs in a thousand (%.2f to %.2f)." % (x["failing"], x["runs"], x["pairs"], x["per_1000"], x["per_1000_lo"], x["per_1000_hi"]))
    print("   IF pairs failed independently (an assumption), a machine of N pairs would be right in (1 - %.2e)^N of builds:" % p)
    print("   " + ", ".join("N = %s: %.3f" % ("{:,}".format(N), (1 - p) ** N) for N in (53, 1000, 10000)))
edge = sorted((x["fraction"], x["failing"]) for x in rows if x["noise"] == "1-THz-class cell")
print("   Failing draws by fraction of the full set, 1-THz-class noise: " + ", ".join("%g: %d" % fx for fx in edge))

# 2 ---------------------------------------------------------------------
SIG = (("inductance", "lsig", 0.03, "pair"), ("diode current", "jsig", 0.05, "pair"), ("difference inside a pair", "jpair", 0.02, "pair"),
       ("pump phase (rad of pump phase)", "psig", np.radians(10.0), "pair"), ("pump level", "asig", 0.10, "pair"), ("link strength", "ksig", 0.10, "link"),
       ("clock timing (periods)", "tsig", 0.02, "pair"), ("supply level", "vsig", 0.01, "pair"), ("damping resistor", "rsig", 0.05, "pair"))
import batch
import analysis
import cellbase
C4 = batch.start(53)
NL = len(C4.TOPO["radd4"]["links"])                     # links of the four-bit adder
print("\n2. How a draw is made: two draws of the nine spreads, made here with numpy (seed 2026)")
rng = np.random.default_rng(2026)
for j in range(2):
    parts = []
    for name, key, rms, per in SIG:
        g = rng.standard_normal(53 if per == "pair" else NL)
        k = int(np.argmax(np.abs(g)))
        parts.append("%s %s %.2f sd (%s %d)" % (name, "%+.4f" % (rms * g[k]), g[k], per, k))
    print("   draw %d, largest value of each spread: " % (j + 1) + "; ".join(parts))
print("   Each value is the rms value of the spread times a standard normal number; it is not bounded. A run without noise or spread has none.")

# 3 ---------------------------------------------------------------------
NRUN = 4
S = cellbase.setting("radd4", N=NRUN, scale=1.0, lsig=0.03, jsig=0.05, jpair=0.02, psig=float(np.radians(10.0)), asig=0.1, ksig=0.1, tsig=0.02, vsig=0.01, rsig=0.05,
                     grp="1.075 THz: full set x 1, without the capacitors, %d runs" % NRUN)
m, arr = batch.run([S], "r6_budget")
r = analysis.logic(m, arr)[0]
d = arr[0]
tp = m["topo"]["radd4"]
E = np.array(m["expect"]["radd4"])
ns = E.shape[0]
ir = np.where((d["tags"] == 0) & d["ref"])[0][0]
iN = np.where((d["tags"] == 0) & ~d["ref"])[0]
W = np.real(np.exp(1j * (d["PE"][iN, 1:ns] - d["PE"][ir, 1:ns][None]))) < 0
W &= (E[1:ns] >= 0)[None]
wa = W[:, :, tp["outs"]].any(2)
print("\n3. How a draw is judged: %d runs of the full set at the noise of the 1-THz-class cell (scale 1.0), each with its own draw" % NRUN)
print("   run without noise or spread: %d of %d pairs right, lowest level %.1f mV" % (r["ref_right"], r["n"], r["level_min"]))
for q in range(len(iN)):
    lo = 1e3 * d["LE"][iN[q], 1:ns].min()
    print("   run %d: wrong decisions %d of %s, wrong additions %d of %d, lowest level %.1f mV: %s" % (
        q + 1, int(W[q].sum()), "{:,}".format(W[q].size), int(wa[q].sum()), wa.shape[1], lo, "fails" if wa[q].any() else "right"))
lo_, hi_ = tables.cp(r["runs_wrong_add"], r["runs"])
print("   failing runs: %d of %d (exact 95 %% interval %s to %s %%); the stored line with 256 draws is the rate to quote" % (
    r["runs_wrong_add"], r["runs"], tables.pct(lo_), tables.pct(hi_)))
