# -*- coding: utf-8 -*-
"""Layouts of pumped pairs of resonant-tunnelling diodes under a four-phase clock: the runner of the model
(uses runs3.py and fdtd3.py).

usage: python chain4.py chain set=<settings json in the output folder> ncell=<pairs per run> [tag=<file stem>]
                        [n=<noisy runs per setting>] [maxruns=<runs per batch>] [out=<folder>] [backend=numpy|torch]
                        and the job arguments of runs3.py
The batches of the paper ran as
    python chain4.py chain backend=torch out=<folder> set=<tag>_set.json tag=<tag> ncell=<pairs> f=1.076
                     maxruns=16000 nseg=4 iv=0.9333,1.667,2.218
(the defaults of this package are those values, except the backend, which is numpy here).

Settings: a list of dicts with the keys of SET_DEFAULT plus design, V (supply level, volts) and ov (the cell
values; cellbase.setting() makes one at the operating point).  Each setting gets N runs with noise and
spreads, and one reference run without either.  Settings of every layout and clock period share batches
(sorted by duration); every batch is saved to its own file <tag>_c<k>.npz, and a batch whose file exists
is skipped (so a queue can be restarted).  <tag>.json holds the settings, the layouts and the expected bits.

A pair is two halves on a centre-tapped inductor with a grounded tap; each half has its own diode and a short
stub, and the signal is read and driven at the far end (node B) of the stubs.  A link is a mutual inductance
between the inductors of two pairs (key km, the coupling of the odd modes; -0.06 in the design).  With key
kmsg = 1 a link of sign -1 has the opposite mutual inductance and inverts.  The key cc (default 0, which is
the design) adds a capacitor cc (model fF) between the node B ends of every pair of linked pairs, straight or
crossed by the sign of the link, and pads every node B to ground so that each carries as much as the pair
with the most links.  That capacitor is not part of the design; it is kept to show its effect.

Layouts (key topo; a layout exists only when its number of pairs equals ncell):
  row, rowB, rowR   a row of ncell pairs, pair k at clock depth k, pattern A (rowB: inverted; rowR: sixteen slots)
  radd<n>           ripple-carry adder of n bits on one rail (radd4: 53 pairs, radd8: 169)
  rdd<n>            the same on two rails (rdd4: 106 pairs)
  sadd, saddx       bit-serial adder with a stored carry, one rail (10 pairs)
  sdadd, sdaddx     the same on two rails (20 pairs); the "x" forms close the carry loop across the rails
                    (two rails) or through a reversed link (one rail), as the pump step requires
  sacc<W>, sdacc<W> and their "x" forms: bit-serial accumulators of W bits (sdacc8x: 84 pairs)
  tree, adder, rx<off>, ax<off>, rz   layouts of an earlier study, kept unchanged (tree and adder need ncell 8)
Keying: mode 'psk' (a 0 is the tone with the opposite sign; the design) or 'ook' (a 0 is nothing).
Pump: the supply of a pair at clock depth d is multiplied by 1 + pump cos(2 w t + pi (pph + pstep d)),
w the carrier (so pstep is the step of the pump phase from one clock phase to the next, in units of pi;
the design has pph = 0.25 and pstep = 1.5).
Per run, slot and pair the files hold the largest level on the flat top (L), the level (LL) and the
phase (PH) of the last full 1-ps window of the flat top, the phase of the window before it (PH2), level and phase of the first
full window that starts 1 ps or more after the next pair's supply edge (LE, PE), and
the mean supply power per pair (P, mW).  Key fd of a setting: frequency of the input tone and half the
pump frequency (THz; 0 = the reference frequency of the reader).
Estimates only.
"""
import json
import math
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True                  # no __pycache__ folder inside the package
import numpy as np
import runs3 as R
import fdtd3

xp, LOG = R.xp, R.LOG
NCELL = int(R.args.get("ncell", "8"))            # pairs per run; a layout is built only when its number of pairs equals it
SEQ = {"A": [1, 0, 1, 1, 0, 0, 1, 0]}
SEQ["B"] = [1 - b for b in SEQ["A"]]                                # the inverted pattern
SEQ["R"] = [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1]          # a sixteen-slot pattern with every pair of neighbours
_ORD = [0, 7, 3, 4, 1, 6, 2, 5, 5, 2, 7, 0, 6, 1, 4, 3]            # the eight combinations of (a, b, c), twice, in two orders
SEQ["A3"] = [(v >> 2) & 1 for v in _ORD]
SEQ["B3"] = [(v >> 1) & 1 for v in _ORD]
SEQ["C3"] = [v & 1 for v in _ORD]
SEQ["S"] = [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0]          # a second sixteen-slot pattern: equal to R in 8 slots, opposite in 8
SEQ["U"] = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1]          # a third: every combination of (R, S, U) occurs in two slots


def _bits(seed, ns=32):
    """A fixed pseudo-random bit sequence (the same on every machine)."""
    x, out = (seed * 2654435761 + 12345) % 4294967296, []
    for _ in range(ns):
        x = (1103515245 * x + 12345) % 2147483648
        out.append((x >> 16) & 1)
    return out


def _radd(nb, ns=32):
    """n-bit ripple-carry adder.  Stage i takes A_i, B_i and the carry-in C_i, all at clock depth 2 i and all
    deciding pairs (A_i and B_i come through rows of buffers from inputs at depth 0; C_0 is an input):
        M_i = majority(A_i, B_i, C_i)        depth 2 i + 1     (the carry)
        G_i = majority(A_i, B_i, not C_i)    depth 2 i + 1
        K_i = C_i                            depth 2 i + 1     (a buffer)
        S_i = majority(not M_i, G_i, K_i)    depth 2 i + 2     (the sum bit)
        C_(i+1) = M_i                        depth 2 i + 2     (a buffer; for the last stage the carry-out)
    Fan-out: A_i and B_i 2, C_i 3, M_i 2.  Returns the layout and the names of the pairs."""
    links, depth, inputs, names = [], [], {}, []

    def new(name, d):
        names.append(name)
        depth.append(d)
        return len(names) - 1

    cin = new("C0", 0)
    inputs[cin] = "c0"
    SEQ["c0"] = _bits(900, ns)
    outs = []
    for i in range(nb):
        ends = []
        for nm in ("a", "b"):
            p = new("%s%d.0" % (nm, i), 0)
            key = "%s%d" % (nm, i)
            inputs[p] = key
            SEQ[key] = _bits((1 if nm == "a" else 2) * 100 + i, ns)
            for d in range(1, 2 * i + 1):
                q = new("%s%d.%d" % (nm, i, d), d)
                links.append((p, q, 1))
                p = q
            ends.append(p)
        M, G, K = new("M%d" % i, 2 * i + 1), new("G%d" % i, 2 * i + 1), new("K%d" % i, 2 * i + 1)
        links += [(ends[0], M, 1), (ends[1], M, 1), (cin, M, 1), (ends[0], G, 1), (ends[1], G, 1), (cin, G, -1), (cin, K, 1)]
        S = new("S%d" % i, 2 * i + 2)
        links += [(M, S, -1), (G, S, 1), (K, S, 1)]
        cin = new("C%d" % (i + 1), 2 * i + 2)
        links.append((M, cin, 1))
        outs.append(S)
    outs.append(cin)
    # stray neighbours in a simple placement: pairs are set on a grid, column = clock depth, row = order of
    # creation within the depth; two pairs that are neighbours on the grid (same column and adjacent rows, or
    # adjacent columns and the same or an adjacent row) and share no link count as stray neighbours
    row_of, cnt = [], {}
    for d in depth:
        row_of.append(cnt.get(d, 0))
        cnt[d] = cnt.get(d, 0) + 1
    linked = set((min(i, j), max(i, j)) for i, j, _ in links)
    mst = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if (i, j) in linked:
                continue
            if abs(depth[i] - depth[j]) <= 1 and abs(row_of[i] - row_of[j]) <= 1:
                mst.append((i, j))
    return dict(links=links, depth=depth, inputs=inputs, names=names, outs=outs, mst=mst, row=row_of)


def _radd_dual(nb, ns=32):
    """n-bit ripple-carry adder in dual rail: every signal x is carried by a pair xt (the bit) and a pair xc (its
    complement).  Stage i, all inputs at clock depth 2 i:
        Mt = majority(At, Bt, Ct)    Mc = majority(Ac, Bc, Cc)        the carry and its complement
        Gt = majority(At, Bt, Cc)    Gc = majority(Ac, Bc, Ct)
        Kt = Ct                      Kc = Cc                           buffers
        St = majority(Mc, Gt, Kt)    Sc = majority(Mt, Gc, Kc)         the sum bit and its complement
        C(i+1)t = Mt                 C(i+1)c = Mc                      buffers
    Every link is straight.  Fan-out at most three."""
    links, depth, inputs, names = [], [], {}, []

    def new(name, d):
        names.append(name)
        depth.append(d)
        return len(names) - 1

    def source(name, key, seed):
        """the two input pairs of a signal: the bit and its complement"""
        if key not in SEQ:
            SEQ[key] = _bits(seed, ns)
        if key + "n" not in SEQ:
            SEQ[key + "n"] = [1 - b for b in SEQ[key]]
        pt, pc = new(name + "t.0", 0), new(name + "c.0", 0)
        inputs[pt], inputs[pc] = key, key + "n"
        return pt, pc

    cin = source("C0", "c0", 900)
    outs = []
    for i in range(nb):
        ends = []
        for nm in ("a", "b"):
            pt, pc = source("%s%d" % (nm, i), "%s%d" % (nm, i), (1 if nm == "a" else 2) * 100 + i)
            for d in range(1, 2 * i + 1):
                qt, qc = new("%s%dt.%d" % (nm, i, d), d), new("%s%dc.%d" % (nm, i, d), d)
                links += [(pt, qt, 1), (pc, qc, 1)]
                pt, pc = qt, qc
            ends.append((pt, pc))
        (At, Ac), (Bt, Bc), (Ct, Cc) = ends[0], ends[1], cin
        d1 = 2 * i + 1
        Mt, Mc, Gt, Gc, Kt, Kc = (new("%s%d%s" % (g, i, r), d1) for g in "MGK" for r in "tc")
        links += [(At, Mt, 1), (Bt, Mt, 1), (Ct, Mt, 1), (Ac, Mc, 1), (Bc, Mc, 1), (Cc, Mc, 1),
                  (At, Gt, 1), (Bt, Gt, 1), (Cc, Gt, 1), (Ac, Gc, 1), (Bc, Gc, 1), (Ct, Gc, 1), (Ct, Kt, 1), (Cc, Kc, 1)]
        St, Sc = new("S%dt" % i, d1 + 1), new("S%dc" % i, d1 + 1)
        links += [(Mc, St, 1), (Gt, St, 1), (Kt, St, 1), (Mt, Sc, 1), (Gc, Sc, 1), (Kc, Sc, 1)]
        cin = (new("C%dt" % (i + 1), d1 + 1), new("C%dc" % (i + 1), d1 + 1))
        links += [(Mt, cin[0], 1), (Mc, cin[1], 1)]
        outs.append(St)
    outs.append(cin[0])
    row_of, cnt = [], {}
    for d in depth:
        row_of.append(cnt.get(d, 0))
        cnt[d] = cnt.get(d, 0) + 1
    linked = set((min(i, j), max(i, j)) for i, j, _ in links)
    mst = [(i, j) for i in range(len(names)) for j in range(i + 1, len(names))
           if (i, j) not in linked and abs(depth[i] - depth[j]) <= 1 and abs(row_of[i] - row_of[j]) <= 1]
    return dict(links=links, depth=depth, inputs=inputs, names=names, outs=outs, mst=mst, row=row_of)


SEQ["sz"] = [0] * 32                                                  # a constant 0
SEQ["sb"] = [int(c) for c in "11101101" "10111010" "10010111" "01011100"]   # four 8-bit numbers, least significant bit first: 183, 93, 233, 58
# operands of the serial adder.  Slot 0 resets the carry; slots 1 and 2 set it; in slots 3 to 10 the operand bits
# differ, so the loop must hold a 1 for eight slots; slot 11 clears it; in slots 12 to 19 it must hold a 0; then
# eleven pseudo-random slots and a last slot of zeros that brings the last carry out
SEQ["sa1"] = [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1] + _bits(71, 11) + [0]
SEQ["sb1"] = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0] + _bits(72, 11) + [0]
for _W in (4, 8):
    SEQ["sf%d" % _W] = [1 if j % _W == 0 else 0 for j in range(32)]   # 1 in the first slot of every word
    SEQ["sclr%d" % _W] = [1 if j < _W else 0 for j in range(32)]      # 1 during the first word: the stored number is cleared
for _k in ("sz", "sb", "sa1", "sb1", "sf4", "sf8", "sclr4", "sclr8"):
    SEQ[_k + "n"] = [1 - b for b in SEQ[_k]]


def _serial_add(dual):
    """Bit-serial adder.  Operands A and B enter least significant bit first, one bit per slot.
        M = majority(A, B, C)       the carry of this slot            (depth 1)
        G = majority(A, B, not C)                                     (depth 1)
        K = C                       a buffer                          (depth 1)
        S = majority(not M, G, K)   the sum bit                       (depth 2)
        M -> X2 -> X3 -> C          the carry goes round a loop of four pairs and is the C of the next slot
        F = S                       a pair that follows the sum       (depth 3)
    Single rail: two crossed links (C to G, M to S).  Dual rail: every signal on two pairs, no crossed link."""
    links, depth, inputs, names = [], [], {}, []

    def new(name, d, key=None):
        names.append(name)
        depth.append(d)
        if key:
            inputs[len(names) - 1] = key
        return len(names) - 1

    if not dual:
        A, B, C = new("A", 0, "sa1"), new("B", 0, "sb1"), new("C", 0)
        M, G, K = new("M", 1), new("G", 1), new("K", 1)
        S, X2 = new("S", 2), new("X2", 2)
        X3, F = new("X3", 3), new("F", 3)
        links += [(A, M, 1), (B, M, 1), (C, M, 1), (A, G, 1), (B, G, 1), (C, G, -1), (C, K, 1), (M, S, -1), (G, S, 1), (K, S, 1),
                  (M, X2, 1), (X2, X3, 1), (X3, C, 1), (S, F, 1)]
        return dict(links=links, depth=depth, inputs=inputs, names=names, outs=[S], mst=[], loop=[C, M, X2, X3])
    At, Ac, Bt, Bc = new("At", 0, "sa1"), new("Ac", 0, "sa1n"), new("Bt", 0, "sb1"), new("Bc", 0, "sb1n")
    Ct, Cc = new("Ct", 0), new("Cc", 0)
    Mt, Mc, Gt, Gc, Kt, Kc = (new(g + r, 1) for g in "MGK" for r in "tc")
    St, Sc, X2t, X2c = new("St", 2), new("Sc", 2), new("X2t", 2), new("X2c", 2)
    X3t, X3c, Ft, Fc = new("X3t", 3), new("X3c", 3), new("Ft", 3), new("Fc", 3)
    links += [(At, Mt, 1), (Bt, Mt, 1), (Ct, Mt, 1), (Ac, Mc, 1), (Bc, Mc, 1), (Cc, Mc, 1),
              (At, Gt, 1), (Bt, Gt, 1), (Cc, Gt, 1), (Ac, Gc, 1), (Bc, Gc, 1), (Ct, Gc, 1), (Ct, Kt, 1), (Cc, Kc, 1),
              (Mc, St, 1), (Gt, St, 1), (Kt, St, 1), (Mt, Sc, 1), (Gc, Sc, 1), (Kc, Sc, 1),
              (Mt, X2t, 1), (X2t, X3t, 1), (X3t, Ct, 1), (Mc, X2c, 1), (X2c, X3c, 1), (X3c, Cc, 1), (St, Ft, 1), (Sc, Fc, 1)]
    return dict(links=links, depth=depth, inputs=inputs, names=names, outs=[St], outc=[Sc], mst=[], loop=[Ct, Mt, X2t, X3t])


def _serial_acc(W, dual):
    """Bit-serial accumulator of W bits.  The number b enters least significant bit first, one bit per slot.
        A1 = Q and not clr        the stored number, cleared during the first word          (depth 1)
        C1 = C and not f          the carry, cleared in the first slot of every word        (depth 1)
        B1 = b                    a buffer                                                  (depth 1)
        M, G, K, S                the full adder of A1, B1 and C1                           (depths 2, 2, 2, 3)
        M -> X3 -> C              the carry loop: C is the carry of the slot before         (X3 depth 3, C depth 0)
        S -> D1 ... -> Q          a row of 4 W - 4 buffer pairs: Q is the sum bit of W slots before
    'and not' is a majority with a constant 0 and a crossed link (single rail) or the other rail (dual rail)."""
    links, depth, inputs, names = [], [], {}, []

    def new(name, d, key=None):
        names.append(name)
        depth.append(d)
        if key:
            inputs[len(names) - 1] = key
        return len(names) - 1

    nd = 4 * W - 4
    if not dual:
        b, f, clr, z = new("b", 0, "sb"), new("f", 0, "sf%d" % W), new("clr", 0, "sclr%d" % W), new("z", 0, "sz")
        C, Q = new("C", 0), new("Q", 0)
        A1, C1, B1 = new("A1", 1), new("C1", 1), new("B1", 1)
        M, G, K = new("M", 2), new("G", 2), new("K", 2)
        S, X3 = new("S", 3), new("X3", 3)
        links += [(Q, A1, 1), (clr, A1, -1), (z, A1, 1), (C, C1, 1), (f, C1, -1), (z, C1, 1), (b, B1, 1),
                  (A1, M, 1), (B1, M, 1), (C1, M, 1), (A1, G, 1), (B1, G, 1), (C1, G, -1), (C1, K, 1),
                  (M, S, -1), (G, S, 1), (K, S, 1), (M, X3, 1), (X3, C, 1)]
        prev = S
        for k in range(1, nd + 1):
            q = new("D%d" % k, 3 + k)
            links.append((prev, q, 1))
            prev = q
        links.append((prev, Q, 1))
        return dict(links=links, depth=depth, inputs=inputs, names=names, outs=[S], mst=[], word=W, loop=[C, C1, M, X3])
    src = {}
    for nm, key in (("b", "sb"), ("f", "sf%d" % W), ("clr", "sclr%d" % W), ("z", "sz")):
        src[nm] = (new(nm + "t", 0, key), new(nm + "c", 0, key + "n"))
    Ct, Cc, Qt, Qc = new("Ct", 0), new("Cc", 0), new("Qt", 0), new("Qc", 0)
    A1t, A1c, C1t, C1c, B1t, B1c = (new(g + r, 1) for g in ("A1", "C1", "B1") for r in "tc")
    Mt, Mc, Gt, Gc, Kt, Kc = (new(g + r, 2) for g in "MGK" for r in "tc")
    St, Sc, X3t, X3c = new("St", 3), new("Sc", 3), new("X3t", 3), new("X3c", 3)
    (bt, bc), (ft, fc), (clt, clc), (zt, zc) = src["b"], src["f"], src["clr"], src["z"]
    links += [(Qt, A1t, 1), (clc, A1t, 1), (zt, A1t, 1), (Qc, A1c, 1), (clt, A1c, 1), (zc, A1c, 1),
              (Ct, C1t, 1), (fc, C1t, 1), (zt, C1t, 1), (Cc, C1c, 1), (ft, C1c, 1), (zc, C1c, 1), (bt, B1t, 1), (bc, B1c, 1),
              (A1t, Mt, 1), (B1t, Mt, 1), (C1t, Mt, 1), (A1c, Mc, 1), (B1c, Mc, 1), (C1c, Mc, 1),
              (A1t, Gt, 1), (B1t, Gt, 1), (C1c, Gt, 1), (A1c, Gc, 1), (B1c, Gc, 1), (C1t, Gc, 1), (C1t, Kt, 1), (C1c, Kc, 1),
              (Mc, St, 1), (Gt, St, 1), (Kt, St, 1), (Mt, Sc, 1), (Gc, Sc, 1), (Kc, Sc, 1),
              (Mt, X3t, 1), (X3t, Ct, 1), (Mc, X3c, 1), (X3c, Cc, 1)]
    pt, pc = St, Sc
    for k in range(1, nd + 1):
        qt, qc = new("D%dt" % k, 3 + k), new("D%dc" % k, 3 + k)
        links += [(pt, qt, 1), (pc, qc, 1)]
        pt, pc = qt, qc
    links += [(pt, Qt, 1), (pc, Qc, 1)]
    return dict(links=links, depth=depth, inputs=inputs, names=names, outs=[St], outc=[Sc], mst=[], word=W, loop=[Ct, C1t, Mt, X3t])


def expected_seq(topo):
    """Bits each pair should carry, [slot, pair], for a layout that may have feedback.  A pair of depth d takes,
    in its slot j, the majority of its inputs; an input pair of depth d' is read in its slot j + (d - d' - 1) / 4.
    For a forward link that is the same slot, for a link that closes a loop an earlier one.  -1: not defined
    (a slot before the first one, or a majority that the defined inputs do not settle)."""
    tp = TOPO[topo]
    n = len(tp["depth"])
    ns = nslots(topo)
    E = -np.ones((ns, n), int)
    isin = set(int(c) for c in tp["inputs"])
    for c, k in tp["inputs"].items():
        E[:, int(c)] = np.array(SEQ[k])
    ins = {j: [(i, sg) for (i, jj, sg) in tp.get("llinks", tp["links"]) if jj == j] for j in range(n)}
    for j in range(n):
        for i, sg in ins[j]:
            assert (tp["depth"][j] - tp["depth"][i] - 1) % 4 == 0, (topo, i, j)
    for tt, s_, j in sorted((s_ + tp["depth"][j] / 4.0, s_, j) for s_ in range(ns) for j in range(n) if j not in isin):
        one = zero = 0
        for i, sg in ins[j]:
            sj = s_ + (tp["depth"][j] - tp["depth"][i] - 1) // 4
            v = E[sj, i] if 0 <= sj < ns else -1
            if v < 0:
                continue
            v = v if sg > 0 else 1 - v
            one += v
            zero += 1 - v
        m_ = len(ins[j])
        E[s_, j] = 1 if 2 * one > m_ else (0 if 2 * zero > m_ else -1)
    return E


TOPO = {
    "row": dict(links=[(i, i + 1, 1) for i in range(NCELL - 1)], depth=list(range(NCELL)), inputs={0: "A"}),
    "rowB": dict(links=[(i, i + 1, 1) for i in range(NCELL - 1)], depth=list(range(NCELL)), inputs={0: "B"}),
    "rowR": dict(links=[(i, i + 1, 1) for i in range(NCELL - 1)], depth=list(range(NCELL)), inputs={0: "R"}),
    "tree": dict(links=[(0, 1, 1), (1, 2, 1), (2, 3, 1), (2, 4, 1), (3, 5, 1), (4, 5, 1), (5, 6, 1), (6, 7, 1)],
                 depth=[0, 1, 2, 3, 3, 4, 5, 6], inputs={0: "A"}),
    "adder": dict(links=[(0, 3, 1), (1, 3, 1), (2, 3, 1), (0, 4, 1), (1, 4, 1), (2, 4, -1), (2, 5, 1), (3, 6, -1), (4, 6, 1), (5, 6, 1), (6, 7, 1)],
                  depth=[0, 0, 0, 1, 1, 1, 2, 3], inputs={0: "A3", 1: "B3", 2: "C3"}),
}
def _two_rows(off):
    """Two rows of NCELL / 2 pairs that share no link: a victim (pattern R, pairs 0 ...) and an aggressor
    (pattern S).  Victim pair k lies next to aggressor pair k + off, so the neighbour is off clock phases
    later than the victim pair it touches; 'mx' lists those pairs of neighbours."""
    m = NCELL // 2
    links = [(i, i + 1, 1) for i in range(m - 1)] + [(m + i, m + i + 1, 1) for i in range(m - 1)]
    return dict(links=links, depth=list(range(m)) + list(range(m)), inputs={0: "R", m: "S"},
                mx=[(k, m + k + off) for k in range(m) if 0 <= k + off < m])


def _adder_x(off):
    """The adder (pairs 0 to 7) and a row with other data (pattern S, pairs 8 ...) that shares no link with
    it.  The row's pair that runs off clock phases later than the sum lies next to the sum (pair 6, clock
    depth 2): 'mx' holds that one pair of neighbours."""
    ad = TOPO["adder"]
    m = NCELL - 8
    j = 2 + off
    inp = dict(ad["inputs"])
    inp[8] = "S"
    return dict(links=ad["links"] + [(8 + i, 8 + i + 1, 1) for i in range(m - 1)], depth=ad["depth"] + list(range(m)), inputs=inp,
                mx=[(6, 8 + j)] if 0 <= j < m else [])


def _three_rows():
    """Three rows of NCELL / 3 pairs side by side, all in step (pair k of each row in the same clock
    phase): the victim (pattern R, pairs 0 ...) between two rows with other data (S and U).  'mx': the
    neighbours straight across (victim k and pair k of each other row); 'mxd': the diagonal ones (pair
    k - 1 and k + 1 of each other row)."""
    m = NCELL // 3
    links = [(r * m + i, r * m + i + 1, 1) for r in range(3) for i in range(m - 1)]
    return dict(links=links, depth=list(range(m)) * 3, inputs={0: "R", m: "S", 2 * m: "U"},
                mx=[(k, r * m + k) for r in (1, 2) for k in range(m)],
                mxd=[(k, r * m + k + dk) for r in (1, 2) for k in range(m) for dk in (-1, 1) if 0 <= k + dk < m])


for _off in (-2, -1, 0, 1, 2):
    TOPO["rx%+d" % _off] = _two_rows(_off)
    if NCELL >= 13:
        TOPO["ax%+d" % _off] = _adder_x(_off)
if NCELL % 3 == 0 and NCELL >= 12:
    TOPO["rz"] = _three_rows()
for _nb in (1, 2, 3, 4, 6, 8):
    _tp = _radd(_nb)
    if len(_tp["names"]) == NCELL:
        TOPO["radd%d" % _nb] = _tp
for _nb in (1, 2, 3, 4):
    _tp = _radd_dual(_nb)
    if len(_tp["names"]) == NCELL:
        TOPO["rdd%d" % _nb] = _tp
for _du in (0, 1):
    _tp = _serial_add(_du)
    if len(_tp["names"]) == NCELL:
        TOPO["sdadd" if _du else "sadd"] = _tp
        _nm = _tp["names"]
        _x = dict(_tp, llinks=list(_tp["links"]))
        if _du:                                            # the two rails change places on the way back into the loop
            _sw = {(_nm.index("X3t"), _nm.index("Ct")): (_nm.index("X3c"), _nm.index("Ct")), (_nm.index("X3c"), _nm.index("Cc")): (_nm.index("X3t"), _nm.index("Cc"))}
            _x["links"] = [(_sw.get((i, j), (i, j))[0], j, sg) for (i, j, sg) in _tp["links"]]
        else:                                              # the link back into the loop is reversed
            _x["links"] = [(i, j, -sg if (i, j) == (_nm.index("X3"), _nm.index("C")) else sg) for (i, j, sg) in _tp["links"]]
        TOPO["sdaddx" if _du else "saddx"] = _x
    for _W in (4, 8):
        _tp = _serial_acc(_W, _du)
        if len(_tp["names"]) == NCELL:
            TOPO["%s%d" % ("sdacc" if _du else "sacc", _W)] = _tp
            _nm = _tp["names"]
            _x = dict(_tp, llinks=list(_tp["links"]))
            if _du:
                _sw = {(_nm.index("X3t"), _nm.index("Ct")): (_nm.index("X3c"), _nm.index("Ct")), (_nm.index("X3c"), _nm.index("Cc")): (_nm.index("X3t"), _nm.index("Cc"))}
                _x["links"] = [(_sw.get((i, j), (i, j))[0], j, sg) for (i, j, sg) in _tp["links"]]
            else:
                _x["links"] = [(i, j, -sg if (i, j) == (_nm.index("X3"), _nm.index("C")) else sg) for (i, j, sg) in _tp["links"]]
            TOPO["%s%dx" % ("sdacc" if _du else "sacc", _W)] = _x
for _t in ("row", "rowB", "rowR"):
    TOPO[_t]["m2"] = [(i, i + 2) for i in range(NCELL - 2)]         # second neighbours along a row
SET_DEFAULT = dict(topo="row", cc=0.0, T=26.0, duty=0.65, mode="psk", scale=1.0, fano=1.0, jsig=0.0, jpair=0.0, lsig=0.0, Is=0.4, N=1,
                   pump=0.0, pph=0.0, pstep=0.0, fd=0.0,
                   km=0.0, kmsg=0.0, keo=0.0, km2=0.0, kx=0.0, kxe=0.0, kxd=0.0, kst=0.0, kstsg=0.0)
# Magnetic coupling between the inductors of pairs (coefficients as in fdtd3.PairFabric, key mk):
#   km   odd mode to odd mode along every link of the layout (kmsg = 1: times the sign of the link)
#   keo  even current of either pair of a link to the odd mode of the other
#   km2  odd to odd between second neighbours of a row
#   kx   odd to odd between the neighbours of the rows of a layout rx, ax or rz; kxe: even to odd between them
#   kxd  odd to odd between the diagonal neighbours of the rows of a layout rz
#   kst  odd to odd between the stray neighbours of a layout (list 'mst'); kstsg = 0: one sign for all,
#        1: the sign alternates from one stray pair of the list to the next (a fixed, mixed pattern)
MAGKEYS = ("km", "keo", "km2", "kx", "kxe", "kxd", "kst")


def nodes(i, j, sg):
    return [(2 * i, 2 * j), (2 * i + 1, 2 * j + 1)] if sg > 0 else [(2 * i, 2 * j + 1), (2 * i + 1, 2 * j)]


def nslots(topo):
    return len(SEQ[next(iter(TOPO[topo]["inputs"].values()))])


def duration(s):
    return max(nslots(s["topo"]) + 3.5, nslots(s["topo"]) + 2.0 + max(TOPO[s["topo"]]["depth"]) / 4.0) * s["T"]


def expected_logic(topo):
    """Bits each pair should carry, [slot, pair], by reading the links as gates: a pair with one input copies it
    (a crossed link inverts), a pair with three takes their majority."""
    tp = TOPO[topo]
    n = len(tp["depth"])
    ns = nslots(topo)
    E = -np.ones((ns, n), int)
    for c, k in tp["inputs"].items():
        E[:, int(c)] = np.array(SEQ[k])
    for j in sorted(range(n), key=lambda q: tp["depth"][q]):
        if int(j) in [int(c) for c in tp["inputs"]]:
            continue
        ins = [(i, sg) for (i, jj, sg) in tp["links"] if jj == j]
        assert len(ins) >= 1, (topo, j, ins)
        assert all(tp["depth"][i] == tp["depth"][j] - 1 for i, _ in ins), (topo, j)
        v = sum(np.where(sg > 0, E[:, i], 1 - E[:, i]) for i, sg in ins)
        assert not (2 * v == len(ins)).any(), ("a tie at pair", topo, j)
        E[:, j] = (2 * v > len(ins)).astype(int)
    assert (E >= 0).all()
    return E


def expected(topo):
    """Bits each pair should carry, [slot, pair]."""
    if topo.startswith("radd") or topo.startswith("rdd"):
        return expected_logic(topo)
    if topo.startswith("sacc") or topo.startswith("sdacc") or topo in ("sadd", "sdadd", "saddx", "sdaddx"):
        return expected_seq(topo)
    if topo.startswith("row") or topo == "tree":
        return np.repeat(np.array(SEQ[TOPO[topo]["inputs"][0]])[:, None], NCELL, 1)
    if topo.startswith("rx"):
        m = NCELL // 2
        return np.concatenate([np.repeat(np.array(SEQ["R"])[:, None], m, 1), np.repeat(np.array(SEQ["S"])[:, None], NCELL - m, 1)], 1)
    if topo == "rz":
        m = NCELL // 3
        return np.concatenate([np.repeat(np.array(SEQ[k])[:, None], m, 1) for k in ("R", "S", "U")], 1)
    a, b, c = (np.array(SEQ[k]) for k in ("A3", "B3", "C3"))
    maj = lambda x, y, z: ((x + y + z) >= 2).astype(int)
    m1, m2 = maj(a, b, c), maj(a, b, 1 - c)
    s = maj(1 - m1, m2, c)
    add = np.stack([a, b, c, m1, m2, c, s, s], 1)
    if topo.startswith("ax"):
        return np.concatenate([add, np.repeat(np.array(SEQ["S"])[:, None], NCELL - 8, 1)], 1)
    return add


for _t in ("row", "tree", "adder"):
    if _t in TOPO and len(TOPO[_t]["depth"]) == NCELL and (_t != "row" or NCELL >= 2):
        if _t in ("tree", "adder") and NCELL != 8:
            continue
        assert (expected_logic(_t) == expected(_t)).all(), _t


def run_chunk(SET, sis):
    n = NCELL
    topos = sorted(set(SET[si]["topo"] for si in sis))
    ulinks = []                                            # union of the node links of the layouts in this batch (they carry the optional capacitor cc)
    for tname in topos:
        for (i, j, sg) in TOPO[tname]["links"]:
            for q in nodes(i, j, sg):
                if q not in ulinks:
                    ulinks.append(q)
    geo = {}
    for tname in topos:
        tp = TOPO[tname]
        deg = np.zeros(n)
        use = np.zeros(len(ulinks))
        for (i, j, sg) in tp["links"]:
            deg[i] += 1
            deg[j] += 1
            for q in nodes(i, j, sg):
                use[ulinks.index(q)] = 1.0
        ns = nslots(tname)
        seq = np.zeros((n, ns))
        isin = np.zeros(n)
        for c, k in tp["inputs"].items():
            seq[int(c)] = SEQ[k]
            isin[int(c)] = 1.0
        geo[tname] = dict(deg=deg, use=use, ns=ns, seq=seq, isin=isin, depth=np.array(tp["depth"], float))
    maxslot = max(g["ns"] for g in geo.values())
    rows, t_sel, isref = [], [], []
    col = {k: [] for k in ("cc", "T", "duty", "scale", "fano", "jsig", "jpair", "lsig", "Is", "sign0", "von", "pump", "pph", "pstep", "ns", "fd", "psig", "asig", "pgate", "tsig", "vsig", "rsig", "pline")}
    mat = {k: [] for k in ("use", "pad", "depth", "isin", "seq", "lrow")}
    for si in sis:
        s = SET[si]
        g = geo[s["topo"]]
        ce = float(g["deg"].max() * s["cc"] + s.get("cpad", 0.0))        # capacitance that cc and padding put on each node B (0 in the design)
        inf = R.cell_info(s["design"], ce)
        seqp = np.zeros((n, maxslot))
        seqp[:, :g["ns"]] = g["seq"]
        for k in range(s["N"] + 1):
            ref = (k == 0)
            rows.append(dict(design=s["design"], c_end=ce, **s.get("ov", {})))
            t_sel.append(si)
            isref.append(ref)
            for key in ("cc", "T", "duty", "Is", "fano", "pump", "pph", "pstep"):
                col[key].append(s[key])
            for key in ("scale", "jsig", "jpair", "lsig"):
                col[key].append(0.0 if ref else s[key])
            for key in ("psig", "asig", "tsig", "vsig", "rsig", "pline"):
                col[key].append(0.0 if ref else s.get(key, 0.0))
            col["pgate"].append(s.get("pgate", 0.0))
            col["sign0"].append(-1.0 if s["mode"] == "psk" else 0.0)
            if not s.get("V"):
                raise ValueError("setting %d gives no supply level V (volts); this package does not derive one from fx" % si)
            col["von"].append(s["V"])
            col["ns"].append(g["ns"])
            col["fd"].append(s["fd"] if s["fd"] > 0 else R.F_REF)
            mat["use"].append(g["use"] * s["cc"])
            if s.get("ownpad"):          # an earlier study retuned each pair's stub to its own number of links; not available here
                raise ValueError("key ownpad needs the stub retuning of an earlier study, which this package does not carry")
            else:
                mat["pad"].append((g["deg"].max() - g["deg"]) * s["cc"] + s.get("cpad", 0.0))
                mat["lrow"].append(np.full(n, s.get("ov", {}).get("l", inf["l"])))
            mat["depth"].append(g["depth"])
            mat["isin"].append(g["isin"])
            mat["seq"].append(seqp)
    Bq = len(rows)
    A = lambda key: np.array(col[key], float)
    Mx = lambda key: np.array(mat[key], float)
    padB = Mx("pad")[:, :, None] * np.ones((1, 1, 2))
    # ---- magnetic links: the union over the layouts of this batch, one row of four coefficients per run and link
    mag = {}
    if any(SET[si].get(k, 0.0) for si in sis for k in MAGKEYS):
        umag, mkc = [], []
        for tname in topos:
            tp = TOPO[tname]
            for q in [(min(i, j), max(i, j)) for (i, j, sg) in tp["links"]] + [tuple(x) for x in tp.get("m2", [])] + [tuple(x) for x in tp.get("mx", [])] \
                    + [tuple(x) for x in tp.get("mxd", [])] + [tuple(x) for x in tp.get("mst", [])]:
                if q not in umag:
                    umag.append(q)
        for si in sis:
            s, tp = SET[si], TOPO[SET[si]["topo"]]
            c4 = np.zeros((len(umag), 4))
            opp = set((min(a_, b_), max(a_, b_)) for a_, b_ in s.get("kmopp", []))      # links on which the coupling is reversed
            for (i, j, sg) in tp["links"]:
                q = umag.index((min(i, j), max(i, j)))
                c4[q, 0] += s["km"] * (sg if s["kmsg"] else 1.0) * (-1.0 if (min(i, j), max(i, j)) in opp else 1.0)
                c4[q, 1] += s["keo"]
                c4[q, 2] += s["keo"]
            for x in tp.get("m2", []):
                c4[umag.index(tuple(x)), 0] += s["km2"]
            for x in tp.get("mx", []):
                q = umag.index(tuple(x))
                c4[q, 0] += s["kx"]
                c4[q, 1] += s["kxe"]
                c4[q, 2] += s["kxe"]
            for x in tp.get("mxd", []):
                c4[umag.index(tuple(x)), 0] += s["kxd"]
            for q_, x in enumerate(tp.get("mst", [])):
                c4[umag.index(tuple(x)), 0] += s["kst"] * ((-1.0) ** q_ if s["kstsg"] else 1.0)
            if s.get("ksig"):                          # error of the link strength, fixed per run and link; none in the reference run
                _krng = np.random.default_rng(int(R.args.get("pseed", "11")) + 177 + si)
                for k_ in range(s["N"] + 1):
                    c4k = c4.copy()
                    if k_:
                        c4k[:, 0] *= 1.0 + s["ksig"] * _krng.standard_normal(len(umag))
                    mkc.append(c4k)
            else:
                mkc += [c4] * (s["N"] + 1)
        mag = dict(mlinks=umag, mk=np.array(mkc))
    if R.IV_ARG != "central":                             # diode law of the whole job: current scale, voltage stretch, added odd current (mA per full device)
        import rtdiv
        js_, vs_, jv_ = (float(x) for x in R.IV_ARG.split(","))
        mag = dict(mag, iv=rtdiv.variant(js_, vs_, jv_))
    _PF = fdtd3.PairFabric
    if any(SET[si].get("ownpad") for si in sis):          # stub length per pair instead of per run (not reached: ownpad is refused above)
        _lpair = Mx("lrow")[:, :, None] * np.ones((1, 1, 2))

        def _PF2(*a_, **k_):
            k_["l"] = _lpair
            return _PF(*a_, **k_)
        fdtd3.PairFabric = _PF2
    try:
        fab = R.build(rows, n=n, links=ulinks, linkC=Mx("use"), CpadB=padB,
                      jsig=A("jsig"), jpair=A("jpair"), lsig=A("lsig"), seed=int(R.args.get("pseed", "11")), rsig=A("rsig"), **mag)
    finally:
        fdtd3.PairFabric = _PF
    fab.enable_noise(T=353.0, fano=A("fano"), scale=A("scale"), seed=int(R.args.get("seed", "5")))
    _vrng = np.random.default_rng(int(R.args.get("pseed", "11")) + 377)                      # vsig: rms error of each pair's supply level; pline: rms error of the pump phase of each clock phase (rad)
    vs, T, du = fab._pair(A("von")[:, None] * (1.0 + A("vsig")[:, None] * _vrng.standard_normal((Bq, n)))), fab._pair(A("T")), fab._pair(A("duty"))
    _pl4 = A("pline")[:, None] * _vrng.standard_normal((Bq, 4))
    _trng = np.random.default_rng(int(R.args.get("pseed", "11")) + 277)                      # tsig: rms error of each pair's clock timing, in periods
    phase = fab._pair(Mx("depth") / 4.0 + A("tsig")[:, None] * _trng.standard_normal((Bq, n)))
    _prng = np.random.default_rng(int(R.args.get("pseed", "11")) + 77)                      # errors of the pump from pair to pair
    pump = fab._pair(A("pump")[:, None] * (1.0 + A("asig")[:, None] * _prng.standard_normal((Bq, n))))
    pph = fab._pair((A("pph")[:, None] + A("pstep")[:, None] * Mx("depth")) * math.pi + A("psig")[:, None] * _prng.standard_normal((Bq, n))
                    + np.take_along_axis(_pl4, Mx("depth").astype(int) % 4, 1))      # pump phase of each pair
    pgate = fab._pair(A("pgate"))
    g1_, g2_ = (pgate == 1.0) * 1.0, (pgate == 2.0) * 1.0       # 1: the clock gates the pump and the supply stays on; 2: the pump is added to the gated supply and stays on
    has_pump = bool(A("pump").any())
    wd = fab._arr(A("fd") * fdtd3.W0).reshape(-1, 1, 1)      # drive frequency of each run (rad/ps)
    wd2 = fab._pair(A("fd") * fdtd3.W0)
    Tnp, dunp, Isnp, s0np, nsnp = A("T"), A("duty"), A("Is"), A("sign0"), A("ns").astype(int)
    isin, seqm = Mx("isin"), Mx("seq")                    # [Bq, n], [Bq, n, maxslot]
    half = fab._arr(np.array([1.0, -1.0])).reshape(1, 1, 2)
    cache = dict(key=None, amp=None)
    ar = np.arange(Bq)

    def vclk(t):
        u = xp.remainder(t / T - phase, 1.0) if xp is not np else np.remainder(t / T - phase, 1.0)
        tt = u * T
        w = R.rc_t(tt, R.EDGE) - R.rc_t(tt - du * T, R.EDGE) + R.rc_t(tt - T, R.EDGE)
        r0 = min(1.0, t / 3.0)
        if has_pump:                                       # pgate = 1: the supply stays on and the clock gates the pump
            c2 = pump * xp.cos(2.0 * wd2 * t + pph)
            v = vs * r0 * ((w + (1.0 - w) * g1_) + c2 * (w + (1.0 - w) * g2_))    # pgate 0: V w (1 + c); 1: V (1 + c w); 2: V (w + c)
        else:
            v = vs * w * r0
        return v

    def iB(t):
        u_ = t / Tnp + 0.25                                # the input of slot s is on over [(s - 0.25) T, (s + duty) T)
        slot = np.floor(u_).astype(int)
        ok_ = (slot >= 1) & (slot <= nsnp) & ((u_ - slot) < (0.25 + dunp))
        if not ok_.any():
            return 0.0
        key = (slot.tobytes(), ok_.tobytes())
        if cache["key"] != key:
            b = seqm[ar, :, np.clip(slot - 1, 0, maxslot - 1)]                     # [Bq, n]
            a = np.where(b > 0, 1.0, s0np[:, None]) * isin * (ok_ * Isnp)[:, None]
            cache["key"], cache["amp"] = key, fab._arr(a)[..., None] * half
        return cache["amp"] * xp.cos(wd * t)

    t_end = float(max(duration(SET[si]) for si in sis))
    LOG("batch of %d runs of %d pairs (layouts %s, periods %s ps), %.0f ps" % (Bq, n, ",".join(topos), ",".join("%g" % x for x in sorted(set(Tnp.tolist()))), t_end))
    res = R.run(fab, t_end, vclk, iB, progress=50)
    amp, ph = res["amp"], res["ph"]
    tw = np.arange(amp.shape[0]) * 1.0
    Lm = np.zeros((Bq, maxslot, n), np.float32)
    Ll = np.zeros((Bq, maxslot, n), np.float32)
    Pl = np.zeros((Bq, maxslot, n), np.float32)
    Pp = np.zeros((Bq, maxslot, n), np.float32)
    Le = np.zeros((Bq, maxslot, n), np.float32)
    Pe = np.zeros((Bq, maxslot, n), np.float32)
    Pm = np.zeros(Bq, np.float32)
    tsel = np.array(t_sel)
    tnames = np.array([SET[si]["topo"] for si in t_sel])
    for tname in topos:
        g = geo[tname]
        for (Tq, dq) in sorted(set(zip(Tnp[tnames == tname].tolist(), dunp[tnames == tname].tolist()))):
            rsel = np.where((tnames == tname) & (Tnp == Tq) & (dunp == dq))[0]
            for j in range(g["ns"]):
                for k in range(n):
                    t0 = (j + 1 + g["depth"][k] / 4.0) * Tq
                    w_ = np.where((tw >= t0 + 2.0) & (tw + 1.0 <= t0 + dq * Tq - 1.0))[0]
                    if len(w_) == 0:
                        continue
                    Lm[rsel, j, k] = amp[w_][:, rsel, k].max(0)
                    Ll[rsel, j, k] = amp[w_[-1], rsel, k]
                    Pl[rsel, j, k] = ph[w_[-1], rsel, k]
                    Pp[rsel, j, k] = ph[w_[-2], rsel, k] if len(w_) > 1 else ph[w_[-1], rsel, k]
                    we = np.where(tw >= t0 + 0.25 * Tq + 1.0)[0]          # first full window after the next pair's supply has come on
                    Le[rsel, j, k] = amp[we[0], rsel, k]
                    Pe[rsel, j, k] = ph[we[0], rsel, k]
            Pm[rsel] = res["p"][int(2 * Tq):int(8 * Tq)][:, rsel, :].mean((0, 2))
    del fab
    return dict(L=Lm, LL=Ll, PH=Pl, PH2=Pp, LE=Le, PE=Pe, P=Pm, tags=tsel, ref=np.array(isref))


def exp_chain():
    SET = [dict(SET_DEFAULT, **s) for s in json.load(open(os.path.join(R.OUT, R.args["set"])))]
    if "n" in R.args:
        for s in SET:
            s["N"] = int(R.args["n"])
    maxruns = int(R.args.get("maxruns", "8000"))
    tag = R.args.get("tag", "chain")
    order = sorted(range(len(SET)), key=lambda si: (-duration(SET[si]), si))
    chunks, cur, cnt = [], [], 0
    for si in order:
        nr = SET[si]["N"] + 1
        if cur and cnt + nr > maxruns:
            chunks.append(cur)
            cur, cnt = [], 0
        cur.append(si)
        cnt += nr
    if cur:
        chunks.append(cur)
    used = sorted(set(s_["topo"] for s_ in SET))
    meta = dict(SET=SET, seq=SEQ, topo={t: TOPO[t] for t in used}, ncell=NCELL, iv=R.IV_ARG, chunks=chunks, expect={t: expected(t).tolist() for t in used}, f_ref=R.F_REF, edge=R.EDGE,
                info=R.info_json(sorted(set(s["design"] for s in SET))))
    json.dump(meta, open(os.path.join(R.OUT, tag + ".json"), "w"), indent=1)
    LOG("%d settings in %d batches" % (len(SET), len(chunks)))
    for ci, sis in enumerate(chunks):
        fn = os.path.join(R.OUT, "%s_c%03d" % (tag, ci))
        if os.path.exists(fn + ".npz"):
            LOG("batch %d exists, skipped" % ci)
            continue
        arr = run_chunk(SET, sis)
        np.savez_compressed(fn + ".tmp.npz", **arr)
        os.replace(fn + ".tmp.npz", fn + ".npz")
        LOG("saved batch %d of %d: %s" % (ci + 1, len(chunks), fn))


if __name__ == "__main__":
    import time
    t0_ = time.time()
    LOG("experiment", R.EXP, "backend", R.backend)
    exp_chain()
    LOG("done in %.0f s" % (time.time() - t0_))
