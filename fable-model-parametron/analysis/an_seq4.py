# -*- coding: utf-8 -*-
"""Layouts with state (the serial adder "sadd"/"sdadd"/"sdaddx" and the accumulators "sacc<W>"/"sdacc<W>" of chain4.py):
read every run and count wrong decisions, wrong sum bits and wrong words. Writes chain_<tag>_seq.json.

The reading, in plain words.
  - A decision of a pair in a slot is its phase when the next pair takes its decision. It is wrong when it lies more
    than 90 degrees from the phase of the run without noise or spread of the same setting (the reference run).
  - Entries that the layout leaves undefined are left out: the stored bits before the first word has gone round, the
    carry before the first slot, and slot 0.
  - The reference run itself is checked against the expected bits, pair by pair on the pair's own axis, at that same
    moment (refcheck.py). The number of pairs that are also right in the last window of their on-time is kept as
    "late_right".
  - A sum bit is the decision of the sum pair (the first output of the layout). A word is wrong when any of its sum
    bits is wrong. In the serial adder the whole run is one long sum.
  - "first_wrong_at" counts, per run with a wrong decision, the pair whose wrong decision came first in time.
The code is that of the session script of the same name; only its input and output changed (see common.py).
usage: python an_seq4.py <tag> [<array folder>] [out=<folder>] [-v]"""
import json
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True                  # no __pycache__ folder inside the package
import refcheck
from common import args, load_json, load_npz

TAG, D, OUT = args(sys.argv)
VERB = "-v" in sys.argv
m = load_json(TAG + ".json", OUT, D)
SET = m["SET"]
EXP = {t: np.array(v) for t, v in m["expect"].items()}
F_REF = m["f_ref"]
out = []
for ci in range(len(m["chunks"])):
    fn = os.path.join(D, "%s_c%03d.npz" % (TAG, ci))
    if not os.path.exists(fn):
        continue
    d = load_npz(fn)
    tg, rf = d["tags"], d["ref"]
    for si in m["chunks"][ci]:
        s = SET[si]
        tp = m["topo"][s["topo"]]
        ex = EXP[s["topo"]]                                  # [slot, pair], -1 where not defined
        ns, n = ex.shape
        ok = ex >= 0
        ok[0] = False                                        # slot 0 follows a clock cycle without data
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
        lev = np.array([float(1e3 * LLr[ok[:, k], k].mean()) if ok[:, k].any() else 0.0 for k in range(n)])
        marg = np.array([float(pr[ok[:, k], k].min() / max(LLr[ok[:, k], k].mean(), 1e-12)) if ok[:, k].any() else 1.0 for k in range(n)])
        S = tp["outs"][0]
        late_right = int(ref_ok.sum())                      # the older check: the last window of a pair's on-time
        ref_ok, marg, lev, lowest = refcheck.early_ref(d, m, si)        # the check that counts: when the next pairs decide
        r = dict(si=si, topo=s["topo"], grp=s.get("grp", ""), cell=s.get("cell", ""), n=n, runs=int(len(iN)), ref_right=int(ref_ok.sum()), margin=float(marg.min()),
                 late_right=late_right, level_S=float(lev[S]), level_min=float(lowest.min()), P_mW=float(d["P"][ir]),
                 wrong_ref_pairs=[tp["names"][k] for k in range(n) if not ref_ok[k]] if "names" in tp else [])
        if len(iN):
            ce = np.exp(1j * (d["PE"][iN, :ns] - d["PE"][ir, :ns][None]))            # [run, slot, pair]
            wrong = (np.real(ce) < 0) & ok[None]
            dev = np.angle(ce)
            r["n_dec"] = int(ok.sum() * len(iN))
            r["wrong"] = int(wrong.sum())
            r["runs_wrong"] = int(wrong.any((1, 2)).sum())
            r["n_S"] = int(ok[:, S].sum() * len(iN))
            r["wrong_S"] = int(wrong[:, :, S].sum())
            r["dev_S"] = float(np.degrees(np.sqrt((dev[:, ok[:, S], S] ** 2).mean())))
            r["dev_max"] = float(max(np.degrees(np.sqrt((dev[:, ok[:, k], k] ** 2).mean())) for k in range(n) if ok[:, k].any()))
            lp = tp.get("loop", [])
            if lp:
                r["wrong_loop"] = int(wrong[:, :, lp].sum())
                r["n_loop"] = int(ok[:, lp].sum() * len(iN))
            W = tp.get("word", 0)
            if W:
                ws = wrong[:, :, S]                                                  # [run, slot]
                nw = ns // W
                wword = np.array([ws[:, w * W:(w + 1) * W].any(1) for w in range(nw)]).T      # [run, word]
                r["n_words"] = int(wword.size)
                r["wrong_words"] = int(wword.sum())
                r["wrong_words_by_word"] = wword.sum(0).tolist()
            else:
                r["n_words"] = int(len(iN))                                          # one long sum per run
                r["wrong_words"] = int(wrong[:, :, S].any(1).sum())
            # which pairs err first: per run the earliest wrong decision in absolute time
            first = {}
            tt = np.arange(ns)[:, None] + dep[None, :] / 4.0
            for q in range(len(iN)):
                if wrong[q].any():
                    js, ks = np.where(wrong[q])
                    a = int(np.argmin(tt[js, ks]))
                    nm = tp["names"][ks[a]] if "names" in tp else str(ks[a])
                    first[nm] = first.get(nm, 0) + 1
            r["first_wrong_at"] = first
        out.append(dict(r, set={k: s.get(k) for k in ("design", "V", "fx", "T", "duty", "pump", "pph", "km", "kmsg", "lsig", "jsig", "jpair", "scale", "kst", "N", "fd")}))
out.sort(key=lambda r: r["si"])
with open(os.path.join(OUT, TAG + "_seq.json"), "w") as f_:
    json.dump(out, f_, indent=0)
print("%d settings analysed" % len(out))
print("layout   group / cell                               | pairs right without noise | margin | level S, lowest (mV) | runs | wrong decisions (all pairs) | runs with any | wrong sum bits | wrong words | phase error S, worst pair (deg)")
for r in out:
    s = r["set"]
    lab = ("%s %s" % (r["grp"], r["cell"])).strip()
    cond = "V %.3f pump %.2f link %.3f spread %.3f noise x%.2f T %.1f" % (s.get("V") or 0.0, s["pump"], abs(s["km"]), s.get("lsig") or 0.0, s["scale"], s["T"])
    if r["runs"]:
        print("%-7s %-42s | %3d of %3d | %5.2f | %4.0f %4.0f | %4d | %6d of %8d | %4d | %5d of %6d | %4d of %5d | %4.1f %4.1f   %s" %
              (r["topo"], (lab + " " + cond)[:42], r["ref_right"], r["n"], r["margin"], r["level_S"], r["level_min"], r["runs"], r["wrong"], r["n_dec"], r["runs_wrong"], r["wrong_S"], r["n_S"],
               r["wrong_words"], r["n_words"], r["dev_S"], r["dev_max"], cond))
    else:
        print("%-7s %-42s | %3d of %3d | %5.2f | %4.0f %4.0f | no runs with noise   %s" % (r["topo"], lab[:42], r["ref_right"], r["n"], r["margin"], r["level_S"], r["level_min"], cond))
    if VERB and (r["wrong_ref_pairs"] or r.get("first_wrong_at")):
        print("        wrong without noise: %s | first wrong decision at: %s" % (", ".join(r["wrong_ref_pairs"]) or "none", r.get("first_wrong_at")))
