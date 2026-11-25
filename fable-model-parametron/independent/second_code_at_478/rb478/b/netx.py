"""Layouts (b1),(b2),(c1),(c2) of BLIND_SPEC_D225_STEP, general network builder, rule evaluator.
Units: V, mA, ohm, fF, pH, ps.  model.py copied from rebuild16 (checked against spec 1)."""
import numpy as np
from model import *

A_OP = np.array([int(c) for c in '0 1 1 1 0 1 1 0 0 1 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0'.split()])
B_OP = np.array([int(c) for c in '0 1 1 0 1 0 0 1 1 0 1 0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0 1 0 1 0 0'.split()])


def layout(name):
    """returns names, depth array, links [(a,b,sign)] (sign +1: M=-k L, -1: reversed M=+k L),
    drives {pair: (operand 'a'/'b', polarity +1/-1)}, sum pair name"""
    if name in ('b1', 'b2'):
        names = ['A', 'B', 'C', 'M', 'G', 'K', 'S', 'X2', 'X3', 'F']
        depth = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3]
        links = [('A', 'M', 1), ('B', 'M', 1), ('C', 'M', 1), ('A', 'G', 1), ('B', 'G', 1), ('C', 'G', -1),
                 ('C', 'K', 1), ('M', 'S', -1), ('G', 'S', 1), ('K', 'S', 1), ('M', 'X2', 1), ('X2', 'X3', 1),
                 ('X3', 'C', 1 if name == 'b1' else -1), ('S', 'F', 1)]
        drives = {'A': ('a', 1), 'B': ('b', 1)}
        spair = 'S'
    elif name in ('c1', 'c2'):
        names = ['At', 'Bt', 'Ac', 'Bc', 'Ct', 'Cc', 'Mt', 'Mc', 'Gt', 'Gc', 'Kt', 'Kc',
                 'St', 'Sc', 'X2t', 'X2c', 'X3t', 'X3c', 'Ft', 'Fc']
        depth = [0] * 6 + [1] * 6 + [2] * 4 + [3] * 4
        src = {'Mt': ['At', 'Bt', 'Ct'], 'Mc': ['Ac', 'Bc', 'Cc'], 'Gt': ['At', 'Bt', 'Cc'], 'Gc': ['Ac', 'Bc', 'Ct'],
               'Kt': ['Ct'], 'Kc': ['Cc'], 'St': ['Mc', 'Gt', 'Kt'], 'Sc': ['Mt', 'Gc', 'Kc'], 'X2t': ['Mt'],
               'X2c': ['Mc'], 'X3t': ['X2t'], 'X3c': ['X2c'], 'Ft': ['St'], 'Fc': ['Sc']}
        links = [(s, p, 1) for p, ss in src.items() for s in ss]
        if name == 'c1':
            links += [('X3t', 'Ct', 1), ('X3c', 'Cc', 1)]
        else:
            links += [('X3t', 'Cc', 1), ('X3c', 'Ct', 1)]
        drives = {'At': ('a', 1), 'Bt': ('b', 1), 'Ac': ('a', -1), 'Bc': ('b', -1)}
        spair = 'St'
    else:
        raise ValueError(name)
    return names, np.array(depth), links, drives, spair


def build_net(cell, Lodd, names, links, kfac=0.06):
    """Lodd (N,), links by name.  Link M = -sign*kfac*sqrt(La*Lb) (geometric mean under spread)."""
    P = {nm: i for i, nm in enumerate(names)}
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
        M = -sg * kfac * np.sqrt(Lodd[a0] * Lodd[b0])
        for (a, b) in ((a0, b0), (b0, a0)):
            ap, am, bp, bm = 2 * a, 2 * a + 1, 2 * b, 2 * b + 1
            Lm[bp, ap] += 0.5 * M; Lm[bp, am] -= 0.5 * M
            Lm[bm, ap] -= 0.5 * M; Lm[bm, am] += 0.5 * M
    assert np.allclose(Lm, Lm.T)
    assert np.linalg.eigvalsh(Lm).min() > 0, 'inductance matrix not positive definite'
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


def rules(lname, a, b):
    """Expected bits per pair and slot from the stated rules (one link: copy; reversed: opposite; three: majority).
    A pair of depth d>0 takes its inputs from depth d-1 in the same slot; depth 0 (the loop pair) from depth 3 of the
    previous slot.  -1 = undetermined (slot 0 loop pair)."""
    names, depth, links, drives, _ = layout(lname)
    P = {nm: i for i, nm in enumerate(names)}
    N, nsl = len(names), len(a)
    E = np.full((N, nsl), -1, int)
    srcs = {nm: [] for nm in names}
    for (x, y, sg) in links:
        # direction: from lower depth (cyclically previous) to the other
        dx, dy = depth[P[x]], depth[P[y]]
        if (dx + 1) % 4 == dy:
            srcs[y].append((x, sg))
        elif (dy + 1) % 4 == dx:
            srcs[x].append((y, sg))
        else:
            raise ValueError('link between non-adjacent depths')
    ops = {'a': a, 'b': b}
    order = sorted(range(N), key=lambda m: depth[m])
    for s in range(nsl):
        for m in order:
            nm = names[m]
            if nm in drives:
                op, pol = drives[nm]
                E[m, s] = ops[op][s] if pol > 0 else 1 - ops[op][s]
                continue
            vals = []
            for (x, sg) in srcs[nm]:
                ss = s if depth[m] > 0 else s - 1
                v = E[P[x], ss] if ss >= 0 else -1
                if v >= 0 and sg < 0:
                    v = 1 - v
                vals.append(v)
            if len(vals) == 1:
                E[m, s] = vals[0]
            else:
                n1 = sum(v == 1 for v in vals); n0 = sum(v == 0 for v in vals)
                E[m, s] = 1 if n1 >= 2 else (0 if n0 >= 2 else -1)
    return E


def sum_bits(a, b):
    nsl = len(a)
    va = sum(int(a[i]) << i for i in range(nsl)); vb = sum(int(b[i]) << i for i in range(nsl))
    s = va + vb
    return np.array([(s >> i) & 1 for i in range(nsl)]), va, vb, s
