"""Adder network of the addendum (rebuild16).  Generalises rebuild15 model.build to an arbitrary link list.
Units: V, mA, ohm, fF, pH, ps.
"""
import numpy as np
from model import *

NAMES = ['A', 'B', 'C', 'M', 'G', 'K', 'S', 'X2', 'X3', 'F']
DEPTH = np.array([0, 0, 0, 1, 1, 1, 2, 2, 3, 3])
P = {nm: i for i, nm in enumerate(NAMES)}
# (pair a, pair b, sign): sign +1 normal link M = -kfac*L ; -1 reversed M = +kfac*L
LINKS = [('A', 'M', 1), ('B', 'M', 1), ('C', 'M', 1), ('A', 'G', 1), ('B', 'G', 1), ('C', 'G', -1),
         ('C', 'K', 1), ('M', 'S', -1), ('G', 'S', 1), ('K', 'S', 1), ('M', 'X2', 1), ('X2', 'X3', 1),
         ('X3', 'C', 1), ('S', 'F', 1)]

A_OP = np.array([int(c) for c in '0 1 1 1 0 1 1 0 0 1 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0'.split()])
B_OP = np.array([int(c) for c in '0 1 1 0 1 0 0 1 1 0 1 0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0 1 0 1 0 0'.split()])


def loop_operands(nsl=32):
    """task 6: slot 0 a=b=0, slots 1,2 a=b=1 (sets carry), then a != b for 28 slots (a=1,b=0 and a=0,b=1 alternating),
    final slot a=b=0."""
    a = np.zeros(nsl, int); b = np.zeros(nsl, int)
    a[1:3] = 1; b[1:3] = 1
    for s in range(3, 31):
        if (s % 2):
            a[s] = 1
        else:
            b[s] = 1
    return a, b


def build_net(cell, Lodd, kfac=0.06, links=LINKS, Mmode='geo'):
    """Lodd: (10,) odd-mode inductance per pair.  Returns A (n x n), Li (inverse winding inductance matrix)."""
    Cp, _, RL = CELLS[cell]
    N = len(Lodd)
    n = NS * N
    A = np.zeros((n, n))
    Gr, Gb, Gk = 1000 / RHO, 1000 / RB, 1000 / RK
    W = 2 * N
    Lm = np.zeros((W, W))
    for m in range(N):
        Lh = Lodd[m] / (1 + KC)
        Lm[2 * m, 2 * m] = Lm[2 * m + 1, 2 * m + 1] = Lh
        Lm[2 * m, 2 * m + 1] = Lm[2 * m + 1, 2 * m] = -KC * Lh
    for (na, nb, sg) in links:
        a0, b0 = P[na], P[nb]
        Lref = np.sqrt(Lodd[a0] * Lodd[b0]) if Mmode == 'geo' else 0.5 * (Lodd[a0] + Lodd[b0])
        M = -sg * kfac * Lref
        for (a, b) in ((a0, b0), (b0, a0)):
            ap, am, bp, bm = 2 * a, 2 * a + 1, 2 * b, 2 * b + 1
            Lm[bp, ap] += 0.5 * M; Lm[bp, am] -= 0.5 * M
            Lm[bm, ap] -= 0.5 * M; Lm[bm, am] += 0.5 * M
    ev = np.linalg.eigvalsh(Lm)
    assert ev.min() > 0, 'inductance matrix not positive definite'
    Li = np.linalg.inv(Lm)
    for m in range(N):
        iS = idx(m, name='vS')
        A[iS, iS] += -Gb / CB
        for h in (0, 1):
            vj, ix, vp, vst, iL = [idx(m, h, s) for s in ('vj', 'ix', 'vp', 'vst', 'iL')]
            A[iS, iS] -= Gr / CB; A[iS, vj] += Gr / CB; A[iS, vp] += Gr / CB
            A[vj, iS] += Gr / CD; A[vj, vj] -= Gr / CD; A[vj, vp] -= Gr / CD; A[vj, ix] -= 1 / CD
            A[ix, ix] = -1 / TAU
            A[vp, iS] += Gr / Cp; A[vp, vj] -= Gr / Cp; A[vp, vp] -= (Gr + Gk) / Cp
            A[vp, iL] -= 1 / Cp; A[vp, vst] += Gk / Cp
            A[vst, vp] += Gk / CS; A[vst, vst] -= Gk / CS
    for w in range(W):
        iw = idx(w // 2, w % 2, 'iL')
        for w2 in range(W):
            A[iw, idx(w2 // 2, w2 % 2, 'vp')] += 1000 * Li[w, w2]
            A[iw, idx(w2 // 2, w2 % 2, 'iL')] -= RL * Li[w, w2]
    return A, Li


def logic(a, b):
    """expected bits per pair and slot; c of slot 0 unknown (-1)."""
    nsl = len(a)
    E = np.full((10, nsl), -1, int)
    c = -1
    maj = lambda x, y, z: int(x + y + z >= 2)
    for s in range(nsl):
        E[P['A'], s] = a[s]; E[P['B'], s] = b[s]
        if c < 0:
            Mv = 1 if (a[s] and b[s]) else (0 if (not a[s] and not b[s]) else -1)
            E[P['M'], s] = Mv; E[P['X2'], s] = Mv; E[P['X3'], s] = Mv
            E[P['G'], s] = Mv  # maj(a,b,not c) also fixed when a == b
        else:
            Mv = maj(a[s], b[s], c)
            E[P['C'], s] = c; E[P['K'], s] = c
            E[P['M'], s] = Mv; E[P['G'], s] = maj(a[s], b[s], 1 - c)
            E[P['S'], s] = maj(1 - Mv, E[P['G'], s], c); E[P['X2'], s] = Mv; E[P['X3'], s] = Mv
            E[P['F'], s] = E[P['S'], s]
        c = Mv
    return E


def sum_stream(a, b):
    nsl = len(a)
    va = sum(int(a[i]) << i for i in range(nsl)); vb = sum(int(b[i]) << i for i in range(nsl))
    s = va + vb
    return np.array([(s >> i) & 1 for i in range(nsl)]), va, vb, s
