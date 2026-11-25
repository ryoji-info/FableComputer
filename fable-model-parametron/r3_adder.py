# -*- coding: utf-8 -*-
"""r3: the four-bit ripple-carry adder of 53 pairs on one rail at the operating point (0.94 V, pump 25 %,
links 6 %, no link capacitors).

What it shows.
  1. The run without noise or spread: pairs right when the next pairs decide (refcheck.py), the smallest
     margin and the lowest level of any pair, and the 31 additions it carries.
  2. A few runs with the physical noise of the 225-GHz circuit and a 3 % spread of the tank inductance:
     wrong additions (a slot in which any output pair S_0 to S_3 or C_4 is wrong) and wrong decisions.
Each run adds the same 31 pseudo-random pairs of four-bit numbers and a carry-in, one per slot after slot 0.
The noise differs from that of the session's batches (numpy against the generator of the graphics processor,
and double against single precision), so the noisy counts are to be compared as counts.
Every number is a result of the model.  Run time on the reference computer: about 5 minutes.
usage: python r3_adder.py
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

NRUN = 8
C4 = batch.start(53)
SET = [cellbase.setting("radd4", N=NRUN, scale=cellbase.PHYS_NOISE, lsig=0.03, grp="physical noise, inductance spread 3 %")]
m, arr = batch.run(SET, "r3_adder")
r = analysis.logic(m, arr)[0]
tp = m["topo"]["radd4"]
names = tp["names"]
d = arr[0]
ir = np.where(d["ref"])[0][0]
ok, mg, lv, lo = analysis.refcheck.early_ref(d, m, 0)
print("r3: four-bit ripple-carry adder, 53 pairs, 68 links (8 reversed), cell F, 0.94 V, pump 25 %, links 6 %, no link capacitors")
print("\n1. Run without noise or spread, judged when the next pairs decide")
print("   pairs right: %d of %d; smallest margin %.3f; lowest level of any pair in any counted slot %.1f mV" % (r["ref_right"], r["n"], r["margin"], r["level_min"]))
kinds = {}
for k, nm in enumerate(names):
    kd = "".join(ch for ch in nm.split(".")[0] if not ch.isdigit())
    kinds.setdefault(kd, []).append(lo[k])
print("   lowest level by kind of pair (mV): " + ", ".join("%s %.1f" % (kd, min(v)) for kd, v in sorted(kinds.items())))
wk = int(np.argmin(lo))
print("   the lowest is pair %s" % names[wk])
# the additions: operand bits from the inputs, sum from the output pairs of the reference run (sign on the pair's own axis)
S = C4.SEQ
ns = len(S["c0"])
E = np.array(m["expect"]["radd4"])
outs = tp["outs"]
a = [sum(S["a%d" % i][s] << i for i in range(4)) for s in range(ns)]
b = [sum(S["b%d" % i][s] << i for i in range(4)) for s in range(ns)]
c = [S["c0"][s] for s in range(ns)]
want = [a[s] + b[s] + c[s] for s in range(ns)]
exp_sum = [sum(int(E[s, k]) << q for q, k in enumerate(outs)) for s in range(ns)]
print("   expected bits of the outputs equal a + b + c_in in every slot: %s" % (exp_sum == want))
dist = len(set((a[s], b[s], c[s]) for s in range(1, ns)))
print("   31 counted additions, %d of them different: " % dist + " ".join("%d+%d+%d=%d" % (a[s], b[s], c[s], want[s]) for s in range(1, ns)))
print("\n2. %d runs with physical noise and a 3 %% spread of the inductance" % NRUN)
print("   wrong additions: %d of %d, in %d of %d runs" % (r["wrong_add"], r["n_add"], r["runs_wrong_add"], r["runs"]))
print("   wrong decisions of any pair: %d of %d, in %d runs; first wrong by kind of pair: %s" % (r["wrong"], r["n_dec"], r["runs_wrong"], r["first"] or "none"))
print("\nSession, batches of the graphics processor (single precision), the same rules:")
print("   no noise or spread at 0.94 V (every 0.94-V line of chain_g34b, chain_g40, chain_g48): 53 of 53 right, smallest margin 0.852, lowest level 200.5 mV")
print("   physical noise and 3 % spread, 32 runs: 0 wrong additions of 992 at 0.94 V (chain_g28b) and at 0.910 and 0.970 V (chain_g37a).")
print("   At the noise of the 1-THz-class cell and 3 % spread, 0.94 V: 0 of 992 (chain_g40)")
