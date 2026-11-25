import sys, json
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
import rtdsim as R
import layouts as LY

D = __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "res")
DELTA = 0.75 * np.pi
SL = np.arange(1, 32)

def get_lay(name):
    return LY.layout_r() if name == 'r' else LY.layout_c()

def axis0(lay, X):
    acc = 0j
    for k, bv in lay.drive.items():
        for s in SL:
            ph = np.angle(X[k, s]) + (0 if bv[s] else np.pi)
            acc += np.exp(1j * ph)
    return np.angle(acc)

def decode(lay, X, ax0):
    ax = ax0 + DELTA * lay.depth
    proj = np.real(X * np.exp(-1j * ax)[:, None])
    bitsm = (proj > 0).astype(int)
    off = np.angle(X * np.exp(-1j * ax)[:, None])  # angle from + axis
    offax = np.minimum(np.abs(off), np.pi - np.abs(off))  # distance from the axis line
    return bitsm, offax

def nf_report(name, tag):
    lay = get_lay(name)
    z = np.load('%s/%s_%s.npz' % (D, name, tag))
    X = z['X'][0]
    E = LY.expected(lay)
    ax0 = axis0(lay, X)
    bm, offax = decode(lay, X, ax0)
    wrong = (bm[:, SL] != E[:, SL])
    rep = dict(Vs=float(z['Vs']), axis0_deg=float(np.degrees(ax0)), n_wrong=int(wrong.sum()), total=int(wrong.size))
    rep['wrong_pairs'] = sorted(set(lay.names[i] for i in np.where(wrong.any(1))[0]))
    rep['wrong_list'] = [(lay.names[i], int(SL[j])) for i, j in zip(*np.where(wrong))][:40]
    lev = np.abs(X[:, SL]) * 1e3
    i, j = np.unravel_index(np.argmin(lev), lev.shape)
    rep['min_level_mV'] = float(lev[i, j]); rep['min_level_at'] = (lay.names[i], int(SL[j]))
    rep['max_level_mV'] = float(lev.max())
    kinds = {}
    for k in sorted(set(lay.kind)):
        idx = [q for q in range(lay.N) if lay.kind[q] == k]
        sub = lev[idx]
        a, b = np.unravel_index(np.argmin(sub), sub.shape)
        kinds[k] = (round(float(sub[a, b]), 1), lay.names[idx[a]], int(SL[b]))
    rep['min_level_by_kind'] = kinds
    rep['max_off_axis_deg'] = float(np.degrees(offax[:, SL].max()))
    io = np.unravel_index(np.argmax(offax[:, SL]), offax[:, SL].shape)
    rep['max_off_axis_at'] = (lay.names[io[0]], int(SL[io[1]]))
    if name == 'r':
        o = lay.outputs
        val = sum(bm[o[q], SL] * (2 ** q) for q in range(5))
        ops = LY.OPS_R
        want = ops['c0'][SL] + sum((ops['a%d' % q][SL] + ops['b%d' % q][SL]) * 2 ** q for q in range(4))
        rep['sum_ok_slots'] = int((val == want).sum())
        rep['sum_bad_slots'] = [int(s) for s in SL[val != want]]
    else:
        st = lay.names.index('St')
        ops = LY.OPS_C
        A = sum(int(ops['a'][s]) << s for s in range(32)); Bn = sum(int(ops['b'][s]) << s for s in range(32))
        Ssum = A + Bn
        want = np.array([(Ssum >> s) & 1 for s in range(32)])
        rep['St_stream_ok_slots'] = int((bm[st, SL] == want[SL]).sum())
        rep['St_bad_slots'] = [int(s) for s in SL[bm[st, SL] != want[SL]]]
        rep['St_equals_logic_E'] = bool((E[st] == want)[SL].all())
    return rep, X

def noisy_report(name, tag_nf, tags):
    lay = get_lay(name)
    Xn = np.load('%s/%s_%s.npz' % (D, name, tag_nf))['X'][0]
    Xs = np.concatenate([np.load('%s/%s_%s.npz' % (D, name, t))['X'] for t in tags])
    draws = np.concatenate([np.load('%s/%s_%s.npz' % (D, name, t))['draws'] for t in tags])
    dphi = np.angle(Xs[:, :, SL] * np.conj(Xn[None, :, SL]))
    wrong = np.abs(dphi) > np.pi / 2
    rep = dict(ndraws=int(len(draws)), draws=[int(d) for d in draws], wrong=int(wrong.sum()), total=int(wrong.size))
    rep['runs_with_wrong'] = int(wrong.any(axis=(1, 2)).sum())
    out = lay.outputs
    rep['slots_output_wrong'] = int(wrong[:, out, :].any(axis=1).sum())
    per = wrong.sum(axis=(0, 2))
    rep['wrong_by_pair'] = {lay.names[i]: int(per[i]) for i in np.where(per > 0)[0]}
    rep['wrong_per_run'] = [int(w) for w in wrong.sum(axis=(1, 2))]
    lev = np.abs(Xs[:, :, SL]) * 1e3
    rep['min_level_mV'] = float(lev.min())
    # nominal decode check: also bits on axis vs expected
    E = LY.expected(lay)
    ax0 = axis0(lay, Xn)
    werr = 0
    for b in range(len(draws)):
        bm, _ = decode(lay, Xs[b], ax0)
        werr += int((bm[:, SL] != E[:, SL]).sum())
    rep['wrong_vs_logic_on_nominal_axis'] = werr
    rep['max_abs_dphi_deg_nonwrong'] = float(np.degrees(np.abs(dphi[~wrong]).max()))
    rep['p99_abs_dphi_deg'] = float(np.degrees(np.percentile(np.abs(dphi), 99)))
    return rep

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'nf':
        rep, X = nf_report(sys.argv[2], sys.argv[3])
        print(json.dumps(rep, indent=1))
    elif mode == 'noisy':
        rep = noisy_report(sys.argv[2], sys.argv[3], sys.argv[4:])
        print(json.dumps(rep, indent=1))
    elif mode == 'dtcheck':
        name, ta, tb = sys.argv[2], sys.argv[3], sys.argv[4]
        Xa = np.load('%s/%s_%s.npz' % (D, name, ta))['X'][0][:, SL]
        Xb = np.load('%s/%s_%s.npz' % (D, name, tb))['X'][0][:, SL]
        dph = np.degrees(np.abs(np.angle(Xa * np.conj(Xb))))
        dl = np.abs(np.abs(Xa) - np.abs(Xb)) * 1e3
        rl = dl / (np.abs(Xb) * 1e3)
        print(json.dumps(dict(max_dphase_deg=float(dph.max()), mean_dphase_deg=float(dph.mean()),
                              max_dlevel_mV=float(dl.max()), max_rel_dlevel=float(rl.max())), indent=1))
