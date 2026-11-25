# -*- coding: utf-8 -*-
"""r4: the bit-serial adder with a stored carry on two rails (20 pairs, layout sdaddx), and what a capacitor
across every link does.

What it shows.
  1. Runs without noise or spread at 0.94 V and at 1.015 V, each without the link capacitors (cc = 0, the
     design) and with them (cc = 0.02 model fF, 0.096 fF in the 225-GHz circuit, with every node B padded to
     ground up to the pair with the most links, as in the older batches named chain_d*).  For each: pairs
     right and the weakest level, read in two ways:
       (a) the model's own reading when the next pairs decide (refcheck.py; the first full 1-model-ps window
           that starts 1 ps or more after the next clock phase has come on), lowest over the defined bits
           of slots 1 to 31, and the same over every pair and slot as the session's comparison printed it;
       (b) the common reading of the session's comparison of codes (a record not in this package): the
           complex amplitude of the odd stub voltage at the carrier over 2 carrier periods from
           slot start + d T/4 + T/4 + 2.0 ps (physical), lowest over every pair and slots 1 to 31.
  2. A few runs at 0.94 V with the physical noise of the 225-GHz circuit and a 3 % spread of the inductance,
     without the capacitors: wrong decisions, wrong sum bits and wrong sums (a run with any wrong sum bit).
The operands are the 32-slot streams of BLIND_SPEC_T1.md; the carry goes round a loop of four pairs that is
closed across the two rails.  The noise differs from that of the session's batches (numpy against the
generator of the graphics processor, and double against single precision), so the noisy counts are to be
compared as counts.  Every number is a result of the model.  Run time on the reference computer: about 4 minutes.
usage: python r4_serial_adder.py
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

NRUN = 16
C4 = batch.start(20)
R = batch._state["R"]

# record the odd stub voltage of the first four runs (the four runs without noise) every 20 steps, as the
# session's trace runner did (a script that is not in this package); the run itself is not changed
REC, TR = [], []
_run = R.run


def run_rec(fab, t_end, vclk_fn, iB_fn, win=1.0, progress=None):
    step0, cnt = fab.step, [0]

    def step(vclk, iB=0.0):
        step0(vclk, iB)
        cnt[0] += 1
        if cnt[0] % 20 == 0:
            REC.append(np.asarray(fab.odd_B())[:4].astype(np.float32))
            TR.append(cnt[0] * fab.dt)
    fab.step = step
    return _run(fab, t_end, vclk_fn, iB_fn, win=win, progress=progress)


R.run = run_rec
CASES = [(0.94, 0.0), (1.015, 0.0), (0.94, 0.02), (1.015, 0.02)]
SET = [cellbase.setting("sdaddx", V=v, cc=cc, N=0, grp="no noise or spread, %.3f V, cc %g" % (v, cc)) for v, cc in CASES]
SET.append(cellbase.setting("sdaddx", N=NRUN, scale=cellbase.PHYS_NOISE, lsig=0.03, grp="0.940 V, physical noise, inductance spread 3 %"))
m, arr = batch.run(SET, "r4_serial")
res = analysis.seq(m, arr)
tp = m["topo"]["sdaddx"]
names, dep = tp["names"], np.array(tp["depth"], float)
d = arr[0]
print("r4: serial adder on two rails, 20 pairs, 28 links, carry loop closed across the rails, cell F, pump 25 %, links 6 %")

# the common reader of the session's code comparison (not in this package, and not analysis/common.py), on the recorded traces
KT, FDp = 69.28 / 14.5, 0.2252
t_ph = KT * (np.array(TR) - 14.5)
X = np.array(REC, np.float64)                      # [sample, run, pair]
dtp = t_ph[1] - t_ph[0]
T_P = 69.28


def common_levels(bi, dl=2.0, ncar=2.0, nsl=32):
    Z = np.zeros((len(names), nsl), complex)
    for s in range(nsl):
        t0 = s * T_P + dep * T_P / 4 + T_P / 4 + dl
        for mq in range(len(names)):
            sel = (t_ph >= t0[mq]) & (t_ph < t0[mq] + ncar / FDp)
            Z[mq, s] = (2 * dtp / (ncar / FDp)) * np.sum(X[sel, bi, mq] * np.exp(-2j * np.pi * FDp * t_ph[sel]))
    return Z


print("\n1. Runs without noise or spread")
print("   supply   cc (model fF)  pairs right  margin  lowest (a) defined bits  lowest (a) all  lowest (b) common  weakest pair (b)  level of St (a)")
low_b = {}
for si, (v, cc) in enumerate(CASES):
    r = res[si]
    ir = np.where((d["tags"] == si) & d["ref"])[0][0]
    le_all = 1e3 * d["LE"][ir, 1:32].min()
    Z = common_levels(si)
    L = 1e3 * np.abs(Z[:, 1:])
    mq, s_ = np.unravel_index(np.argmin(L), L.shape)
    low_b[(v, cc)] = L.min()
    print("   %.3f V  %-13g  %2d of %2d     %.3f   %6.1f mV                %6.1f mV        %6.1f mV          %-4s slot %-2d      %6.1f mV"
          % (v, cc, r["ref_right"], r["n"], r["margin"], r["level_min"], le_all, L.min(), names[mq], s_ + 1, r["level_S"]))
for v in (0.94, 1.015):
    print("   at %.3f V the capacitors lower the weakest level (b) by %.1f %%" % (v, 100 * (1 - low_b[(v, 0.02)] / low_b[(v, 0.0)])))
print("   session record of the comparison of codes, not in this package (numpy, double precision, reading (b)): without the capacitors 205.1 mV at 0.94 V and 266.5 mV at 1.015 V;")
print("   with them 198.0 and 196.9 mV.  Reading (a) over every pair and slot, with them: 195.7 and 186.5 mV.  Second code as written: 200.9 and 263.9 mV.")
print("   session, graphics processor, reading (a) on defined bits, without the capacitors: 203.6 mV at 0.94 V (chain_g30), 252.5 mV at 1.015 V (chain_g31)")

r = res[4]
print("\n2. %d runs at 0.94 V with physical noise and a 3 %% spread of the inductance, no link capacitors" % NRUN)
print("   pairs right without noise or spread: %d of %d" % (r["ref_right"], r["n"]))
print("   wrong decisions: %d of %d, in %d of %d runs" % (r["wrong"], r["n_dec"], r["runs_wrong"], r["runs"]))
print("   wrong sum bits (St): %d of %d; wrong sums (runs with a wrong sum bit): %d of %d" % (r["wrong_S"], r["n_S"], r["wrong_words"], r["n_words"]))
print("   rms phase error of St %.2f deg, of the worst pair %.2f deg" % (r["dev_S"], r["dev_max"]))
print("   session, chain_g30 (graphics processor), 16 runs: 0 wrong decisions of 9920, 0 wrong sums of 16")
# the sum the adder computes: operands and the expected sum stream, and the stream the reference run carries
S = C4.SEQ
ns = len(S["sa1"])
E = np.array(m["expect"]["sdaddx"])
St = tp["outs"][0]
A_ = sum(S["sa1"][s] << s for s in range(ns))
B_ = sum(S["sb1"][s] << s for s in range(ns))
Sx = sum(int(E[s, St]) << s for s in range(1, ns) if E[s, St] >= 0)
print("\n   operands as 32-bit numbers, least significant bit first: a = %d, b = %d, a + b = %d; expected St stream (slots 1 to 31) = %d; equal: %s"
      % (A_, B_, A_ + B_, Sx, (A_ + B_) % (1 << ns) == Sx))
