# -*- coding: utf-8 -*-
"""Reading rules of the paper, applied to a batch written by chain4.py.

The code of each function is that of the session's analysis scripts, put into functions so that the
listings can call it: rows() is an_chain3.py (phase keying) with the row table of an_tol4.py, seq() is
an_seq4.py, logic() is an_logic5.py, and refcheck.py is shipped unchanged.

The rules.
  - Slot 0 is left out of every count: it follows a clock cycle without data.
  - A decision of a pair in a slot is read when the next pairs take theirs: the phase PE of the first full
    1-ps window that starts 1 ps or more after the next clock phase has come on.
  - A decision is wrong when that phase lies more than 90 degrees from the phase of the run without noise
    or spread of the same setting (the reference run) in the same slot and pair.
  - The reference run itself is checked against the expected bits, pair by pair, on the pair's own axis
    (the sum of its phasors with the expected signs): "right" when every counted slot has the expected sign.
    Rows use the last window of the on-time for this (an_chain3.py); layouts with gates and state use the
    moment of decision (refcheck.py).
  - A row holds when all reference pairs 1 to n-1 are right, no decision at pair n-2 is wrong and the rms
    phase error at pair n-2 over runs and slots is at most 8 degrees (an_tol4.py).
  - An addition is wrong when any output pair is wrong in that slot (an_logic5.py).  In the serial adder a
    sum is wrong when the sum pair St is wrong (an_seq4.py); a run with any wrong sum bit is a wrong word.
usage: python analysis.py rows|seq|logic <folder> <tag>      (prints one line per setting)
"""
import json
import math
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True                  # no __pycache__ folder inside the package
import numpy as np
import refcheck


def load(D, tag):
    """The batch index <tag>.json and its arrays, merged over the chunks: (m, {setting index: arrays})."""
    m = json.load(open(os.path.join(D, tag + ".json")))
    arr = {}
    for ci, sis in enumerate(m["chunks"]):
        fn = os.path.join(D, "%s_c%03d.npz" % (tag, ci))
        if os.path.exists(fn):
            with np.load(fn) as f_:
                d = {k_: f_[k_] for k_ in f_.files}
            for si in sis:
                arr[si] = d
    return m, arr


def rows(m, arr):
    """an_chain3.py (phase keying) and an_tol4.py: one dict per setting."""
    SET = m["SET"]
    EXP = {t: np.array(v) for t, v in m["expect"].items()}
    F_REF = m["f_ref"]
    NC = int(m.get("ncell", 8))
    SKIP = 1
    out = []
    for si, s in enumerate(SET):
        if si not in arr:
            continue
        d = arr[si]
        tg, rf = d["tags"], d["ref"]
        ex = EXP[s["topo"]]
        ns = ex.shape[0]
        e = 2.0 * ex - 1.0
        sl = slice(SKIP, ns)
        ir = np.where((tg == si) & rf)[0][0]
        iN = np.where((tg == si) & ~rf)[0]
        LLr, PHr = d["LL"][ir, sl], d["PH"][ir, sl]
        e, ex = e[sl], ex[sl]
        fd = s.get("fd", 0) or F_REF
        dep = np.array(m["topo"][s["topo"]]["depth"], float)
        t0 = (np.arange(ns)[:, None] + 1.0 + dep[None, :NC] / 4.0) * s["T"]
        wl = np.floor(t0 + s.get("duty", 0.65) * s["T"] - 2.0) + 0.5
        rot = np.exp(-2j * np.pi * (fd - F_REF) * wl)[sl]
        zr = LLr * np.exp(1j * PHr) * rot
        r = dict(si=si, N=len(iN), P_mW=float(d["P"][ir]), level_mV=[float(1e3 * LLr[:, k].mean()) for k in range(NC)])
        dph = np.angle(np.exp(1j * (d["PH"][ir, sl, NC - 1] - d["PH2"][ir, sl, NC - 1])))
        r["f_last"] = float(F_REF + np.median(dph) / (2 * math.pi))
        r["levelE_mV"] = [float(1e3 * d["LE"][ir, sl, k].mean()) for k in range(NC)]
        ce = np.exp(1j * (d["PE"][iN, sl] - d["PE"][ir, sl][None]))
        r["dev_early_deg"] = [float(np.degrees(np.sqrt(np.mean(np.angle(ce[:, :, k]) ** 2)))) if len(iN) else 0.0 for k in range(NC)]
        r["err_early"] = [float((np.real(ce[:, :, k]) < 0).mean()) if len(iN) else 0.0 for k in range(NC)]
        ax = (e * zr).sum(0)
        pr = np.real(zr * np.conj(ax)[None, :]) / np.maximum(np.abs(ax), 1e-12)[None, :] * e
        r["ref_ok"] = [bool((pr[:, k] > 0).all()) for k in range(NC)]
        r["margin"] = [float(pr[:, k].min() / max(LLr[:, k].mean(), 1e-12)) for k in range(NC)]
        r["n_dec"] = int(len(iN) * (ns - SKIP))
        # an_tol4.py
        W = np.real(np.exp(1j * (d["PE"][iN, 1:ns] - d["PE"][ir, 1:ns][None]))) < 0          # [run, slot, pair]
        Wv = W.copy()
        Wv[:, :, 0] = False
        nc = W.shape[2]
        first = np.where(Wv.any(2), Wv.argmax(2), nc)
        r["events"], r["risk"] = int((first < nc).sum()), int(np.minimum(first, nc - 1).sum())
        k = nc - 2
        r["wrong_k"] = int(round(r["err_early"][k] * r["n_dec"]))
        r["wrong_all"] = int((W & (np.arange(nc) > 0)[None, None, :]).sum())
        r["dev_k"] = r["dev_early_deg"][k]
        r["holds"] = bool(all(r["ref_ok"][1:]) and r["wrong_k"] == 0 and r["dev_k"] <= 8.0)
        # added for the listings: the phase step per link in the reference run, at the moment of decision
        # (phase PE of pair k+1 less that of pair k, averaged over the counted slots as unit phasors; in a row
        # both pairs carry the same bit, so this is the turn of the axis from one clock phase to the next)
        r["phase_step_deg"] = [float(np.degrees(np.angle(np.mean(np.exp(1j * (d["PE"][ir, sl, k + 1] - d["PE"][ir, sl, k]))))))
                               for k in range(NC - 1)]
        out.append(r)
    return out


def seq(m, arr):
    """an_seq4.py: one dict per setting."""
    SET = m["SET"]
    EXP = {t: np.array(v) for t, v in m["expect"].items()}
    F_REF = m["f_ref"]
    out = []
    for si, s in enumerate(SET):
        if si not in arr:
            continue
        d = arr[si]
        tg, rf = d["tags"], d["ref"]
        tp = m["topo"][s["topo"]]
        ex = EXP[s["topo"]]
        ns, n = ex.shape
        ok = ex >= 0
        ok[0] = False
        e = np.where(ok, 2.0 * ex - 1.0, 0.0)
        ir = np.where((tg == si) & rf)[0][0]
        iN = np.where((tg == si) & ~rf)[0]
        dep = np.array(tp["depth"], float)
        fd = s.get("fd", 0) or F_REF
        t0 = (np.arange(ns)[:, None] + 1.0 + dep[None, :] / 4.0) * s["T"]
        wl = np.floor(t0 + s.get("duty", 0.65) * s["T"] - 2.0) + 0.5
        rot = np.exp(-2j * np.pi * (fd - F_REF) * wl)
        LLr = d["LL"][ir, :ns]
        zr = LLr * np.exp(1j * d["PH"][ir, :ns]) * rot
        ax = (e * zr).sum(0)
        pr = np.real(zr * np.conj(ax)[None, :]) / np.maximum(np.abs(ax), 1e-12)[None, :] * e
        ref_ok = np.array([bool((pr[ok[:, k], k] > 0).all()) for k in range(n)])
        S = tp["outs"][0]
        late_right = int(ref_ok.sum())
        ref_ok, marg, lev, lowest = refcheck.early_ref(d, m, si)
        r = dict(si=si, topo=s["topo"], grp=s.get("grp", ""), n=n, runs=int(len(iN)), ref_right=int(ref_ok.sum()), margin=float(marg.min()),
                 late_right=late_right, level_S=float(lev[S]), level_min=float(lowest.min()), P_mW=float(d["P"][ir]),
                 wrong_ref_pairs=[tp["names"][k] for k in range(n) if not ref_ok[k]] if "names" in tp else [],
                 lowest_by_pair={tp["names"][k]: float(lowest[k]) for k in range(n)} if "names" in tp else {})
        if len(iN):
            ce = np.exp(1j * (d["PE"][iN, :ns] - d["PE"][ir, :ns][None]))
            wrong = (np.real(ce) < 0) & ok[None]
            dev = np.angle(ce)
            r["n_dec"] = int(ok.sum() * len(iN))
            r["wrong"] = int(wrong.sum())
            r["runs_wrong"] = int(wrong.any((1, 2)).sum())
            r["n_S"] = int(ok[:, S].sum() * len(iN))
            r["wrong_S"] = int(wrong[:, :, S].sum())
            r["dev_S"] = float(np.degrees(np.sqrt((dev[:, ok[:, S], S] ** 2).mean())))
            r["dev_max"] = float(max(np.degrees(np.sqrt((dev[:, ok[:, k], k] ** 2).mean())) for k in range(n) if ok[:, k].any()))
            W = tp.get("word", 0)
            if W:
                ws = wrong[:, :, S]
                nw = ns // W
                wword = np.array([ws[:, w * W:(w + 1) * W].any(1) for w in range(nw)]).T
                r["n_words"] = int(wword.size)
                r["wrong_words"] = int(wword.sum())
            else:
                r["n_words"] = int(len(iN))
                r["wrong_words"] = int(wrong[:, :, S].any(1).sum())
        out.append(r)
    return out


def logic(m, arr):
    """an_logic5.py: one dict per setting."""
    out = []
    for si, s in enumerate(m["SET"]):
        if si not in arr:
            continue
        d = arr[si]
        tp = m["topo"][s["topo"]]
        names = tp.get("names") or [str(i) for i in range(len(tp["depth"]))]
        dep = np.array(tp["depth"])
        E = np.array(m["expect"][s["topo"]])
        ns = E.shape[0]
        outs = tp["outs"]
        ir = np.where((d["tags"] == si) & d["ref"])[0][0]
        iN = np.where((d["tags"] == si) & ~d["ref"])[0]
        W = np.real(np.exp(1j * (d["PE"][iN, 1:ns] - d["PE"][ir, 1:ns][None]))) < 0
        W &= (E[1:ns] >= 0)[None]
        ok, mg, lv, lo = refcheck.early_ref(d, m, si)
        wa = W[:, :, outs].any(2)
        kinds = {}
        for r_ in range(W.shape[0]):
            if W[r_].any():
                sl, pr = np.where(W[r_])
                k = pr[np.argmin(sl + dep[pr] / 4.0)]
                kd = "".join(ch for ch in names[k].split(".")[0] if not ch.isdigit())
                kinds[kd] = kinds.get(kd, 0) + 1
        out.append(dict(si=si, grp=s.get("grp", ""), topo=s["topo"], ref_right=int(ok.sum()), n=int(len(ok)), margin=float(mg.min()),
                        level_min=float(lo.min()), wrong_add=int(wa.sum()), n_add=int(wa.size), runs_wrong_add=int(wa.any(1).sum()), wrong=int(W.sum()),
                        n_dec=int(W.size), runs_wrong=int(W.any((1, 2)).sum()), runs=int(len(iN)), first=kinds))
    return out


if __name__ == "__main__":
    kind, D, tag = sys.argv[1], sys.argv[2], sys.argv[3]
    m, arr = load(D, tag)
    for r in {"rows": rows, "seq": seq, "logic": logic}[kind](m, arr):
        print(json.dumps({k: v for k, v in r.items() if not isinstance(v, (list, dict)) or k in ("ref_ok", "first")}))
