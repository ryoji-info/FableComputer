import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
import rtdsim as R

def bits(s):
    return np.array([int(c) for c in s.split()])

OPS_R = dict(
    c0=bits("1 0 0 1 1 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0"),
    a0=bits("0 1 1 1 0 1 0 1 1 0 1 1 0 0 0 0 1 1 0 1 0 0 1 1 0 1 1 0 0 1 0 1"),
    b0=bits("0 1 1 0 0 0 0 0 0 0 1 1 1 1 0 0 1 1 1 1 0 0 1 0 0 1 1 0 0 1 1 0"),
    a1=bits("1 0 1 1 1 1 0 0 0 1 1 0 0 0 1 0 0 1 1 0 1 1 0 0 1 0 0 0 1 0 1 1"),
    b1=bits("1 1 1 0 1 1 1 1 1 1 1 0 0 1 1 0 0 1 0 0 1 0 0 0 0 1 1 1 1 0 0 0"),
    a2=bits("1 1 1 1 0 0 1 1 0 1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 0 1 0 1"),
    b2=bits("0 0 1 0 0 1 0 0 1 0 1 0 1 0 0 0 0 1 0 1 1 1 1 1 0 0 0 1 0 0 1 0"),
    a3=bits("0 1 1 1 1 0 0 0 1 0 1 1 0 1 0 0 1 1 1 0 0 1 0 1 1 1 1 0 0 0 1 1"),
    b3=bits("1 0 1 0 1 0 0 1 0 1 1 1 0 0 1 0 1 1 0 1 0 1 0 0 1 0 0 0 1 1 0 0"),
)

OPS_C = dict(
    a=bits("0 1 1 1 0 1 1 0 0 1 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0"),
    b=bits("0 1 1 0 1 0 0 1 1 0 1 0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0 1 0 1 0 0"),
)


class Builder:
    def __init__(self):
        self.names, self.depth, self.drive, self.links = [], [], {}, []
    def add(self, name, d, drive=None):
        self.names.append(name); self.depth.append(d)
        i = len(self.names) - 1
        if drive is not None:
            self.drive[i] = np.array(drive)
        return i
    def link(self, a, b, sg=1):
        self.links.append((a, b, sg))
    def lay(self):
        return R.Layout(self.names, self.depth, self.drive, self.links)


def layout_r():
    b = Builder()
    C = [b.add('C0', 0, OPS_R['c0'])]
    kind = {}
    kind['C0'] = 'driven'
    Aend, Bend = [], []
    for i in range(4):
        for op, lst in (('a', Aend), ('b', Bend)):
            nm = '%s%d_drv' % (op, i) if i > 0 else op.upper() + '0'
            prev = b.add(nm, 0, OPS_R['%s%d' % (op, i)])
            kind[nm] = 'driven'
            for j in range(1, 2 * i + 1):
                nm = '%s%d_buf%d' % (op, i, j) if j < 2 * i else op.upper() + str(i)
                cur = b.add(nm, j)
                kind[nm] = 'buffer'
                b.link(prev, cur, 1)
                prev = cur
            lst.append(prev)
    for i in range(4):
        Ai, Bi, Ci = Aend[i], Bend[i], C[i]
        M = b.add('M%d' % i, 2 * i + 1); kind['M%d' % i] = 'M'
        G = b.add('G%d' % i, 2 * i + 1); kind['G%d' % i] = 'G'
        K = b.add('K%d' % i, 2 * i + 1); kind['K%d' % i] = 'K'
        for s in (Ai, Bi, Ci): b.link(s, M, 1)
        b.link(Ai, G, 1); b.link(Bi, G, 1); b.link(Ci, G, -1)
        b.link(Ci, K, 1)
        S = b.add('S%d' % i, 2 * i + 2); kind['S%d' % i] = 'S'
        b.link(M, S, -1); b.link(G, S, 1); b.link(K, S, 1)
        Cn = b.add('C%d' % (i + 1), 2 * i + 2); kind['C%d' % (i + 1)] = 'C'
        b.link(M, Cn, 1)
        C.append(Cn)
    lay = b.lay()
    lay.kind = [kind[n] for n in lay.names]
    lay.outputs = [lay.names.index(n) for n in ('S0', 'S1', 'S2', 'S3', 'C4')]
    return lay


def layout_c():
    b = Builder()
    a, bb = OPS_C['a'], OPS_C['b']
    At = b.add('At', 0, a); Bt = b.add('Bt', 0, bb)
    Ac = b.add('Ac', 0, 1 - a); Bc = b.add('Bc', 0, 1 - bb)
    Ct = b.add('Ct', 0); Cc = b.add('Cc', 0)
    Mt = b.add('Mt', 1); Mc = b.add('Mc', 1); Gt = b.add('Gt', 1); Gc = b.add('Gc', 1)
    Kt = b.add('Kt', 1); Kc = b.add('Kc', 1)
    St = b.add('St', 2); Sc = b.add('Sc', 2); X2t = b.add('X2t', 2); X2c = b.add('X2c', 2)
    X3t = b.add('X3t', 3); X3c = b.add('X3c', 3); Ft = b.add('Ft', 3); Fc = b.add('Fc', 3)
    for s in (At, Bt, Ct): b.link(s, Mt)
    for s in (Ac, Bc, Cc): b.link(s, Mc)
    for s in (At, Bt, Cc): b.link(s, Gt)
    for s in (Ac, Bc, Ct): b.link(s, Gc)
    b.link(Ct, Kt); b.link(Cc, Kc)
    for s in (Mc, Gt, Kt): b.link(s, St)
    for s in (Mt, Gc, Kc): b.link(s, Sc)
    b.link(Mt, X2t); b.link(Mc, X2c); b.link(X2t, X3t); b.link(X2c, X3c)
    b.link(St, Ft); b.link(Sc, Fc)
    b.link(X3t, Cc); b.link(X3c, Ct)
    lay = b.lay()
    assert len(lay.links) == 28
    lay.kind = ['driven'] * 4 + ['C'] * 2 + ['M', 'M', 'G', 'G', 'K', 'K', 'S', 'S', 'X', 'X', 'X', 'X', 'F', 'F']
    lay.outputs = [lay.names.index('St')]
    return lay


def layout_row(n):
    b = Builder()
    pat = np.array([1, 0, 1, 1, 0, 0, 1, 0] * 4)
    prev = b.add('R0', 0, pat)
    for j in range(1, n):
        cur = b.add('R%d' % j, j); b.link(prev, cur); prev = cur
    lay = b.lay(); lay.kind = ['driven'] + ['buffer'] * (n - 1); lay.outputs = []
    return lay


def expected(lay, nslots=32):
    """logic value (0/1) of every pair in every slot, labels judged on axis_d = axis_0 + d*Delta.
    A link from depth ds to depth dt: if dt == ds+1 same slot; if dt == ds+1-4 next slot and label inverted (4 Delta = pi)."""
    N = lay.N
    E = np.full((N, nslots), -1)
    for k, bitsv in lay.drive.items():
        E[k] = bitsv
    srcs = {i: [] for i in range(N)}
    for (a, b, sg) in lay.links:
        srcs[b].append((a, sg))
    order = sorted(range(N), key=lambda i: lay.depth[i])
    for s in range(nslots):
        changed = True
        it = 0
        while changed and it < 20:
            changed = False; it += 1
            for i in order:
                if i in lay.drive or not srcs[i]:
                    continue
                vals = []
                for (a, sg) in srcs[i]:
                    da, di = lay.depth[a], lay.depth[i]
                    if di == da + 1:
                        v = E[a, s]; inv = 0
                    elif di == da + 1 - 4:
                        v = E[a, s - 1] if s > 0 else -1; inv = 1
                    else:
                        raise ValueError('bad link depth')
                    if v < 0:
                        continue
                    v = v ^ inv
                    if sg < 0: v = 1 - v
                    vals.append(v)
                n1 = sum(vals); n0 = len(vals) - n1; L = len(srcs[i])
                if 2 * n1 > L: nv = 1
                elif 2 * n0 > L: nv = 0
                else: continue
                if E[i, s] != nv:
                    E[i, s] = nv; changed = True
    return E
