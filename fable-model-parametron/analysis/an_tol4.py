# -*- coding: utf-8 -*-
"""Table of a tolerance batch of rows (settings with the keys "grp" and "what"). Writes chain_<tag>_tol.json.

Per setting: the pairs right without noise or spread; at the last pair but one (pair 14 of a row of sixteen) the rms
phase error and the wrong decisions with noise and spread; the first-wrong events; the level; and whether the row
holds. A row holds when every pair from 1 on is right without noise or spread, no decision at that pair is wrong
and its rms phase error is at most 8 degrees.
A first-wrong event is the first pair, counted from pair 1, that is wrong in a slot of a run. The decisions at risk
are the decisions up to that pair (or all of them when no pair is wrong).
Needs chain_<tag>_summary.json, written by an_chain3.py, and the array files.
The code is that of the session script of the same name; only its input and output changed (see common.py).
usage: python an_tol4.py <tag> [<array folder>] [out=<folder>]"""
import json
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True                  # no __pycache__ folder inside the package
from common import args, load_json, load_npz

tag, D, OUT = args(sys.argv)
S = load_json(tag + "_summary.json", OUT, D)
m = load_json(tag + ".json", OUT, D)
arr = {}
for ci, sis in enumerate(m["chunks"]):
    fn = os.path.join(D, "%s_c%03d.npz" % (tag, ci))
    if os.path.exists(fn):
        d = load_npz(fn)
        for si in sis:
            arr[si] = d
rows = []
nc = 0
for si, (s, r) in enumerate(zip(S["SET"], S["res"])):
    if r is None or si not in arr:
        continue
    d = arr[si]
    ns = len(m["expect"][s["topo"]])
    ir = np.where((d["tags"] == si) & d["ref"])[0][0]
    iN = np.where((d["tags"] == si) & ~d["ref"])[0]
    W = np.real(np.exp(1j * (d["PE"][iN, 1:ns] - d["PE"][ir, 1:ns][None]))) < 0          # [run, slot, pair]
    Wv = W.copy()
    Wv[:, :, 0] = False
    nc = W.shape[2]
    first = np.where(Wv.any(2), Wv.argmax(2), nc)
    ev, risk = int((first < nc).sum()), int(np.minimum(first, nc - 1).sum())
    ok = r["ref_ok"]
    k = nc - 2
    n = r.get("n_dec", 0)
    x = dict(grp=s.get("grp", ""), what=s.get("what", ""), cell=s.get("cell", ""), V=s.get("V"), pump=s["pump"], lsig=s.get("lsig", 0.0), scale=s.get("scale"), runs=int(len(iN)), right=int(sum(ok)), of=len(ok), margin=float(min(r["margin"][1:])), dev=float(r["dev_early_deg"][k]),
             dev_mid=float(r["dev_early_deg"][nc // 2]), wrong=int(round(r["err_early"][k] * n)), n=n, events=ev, risk=risk, level=float(r["level_mV"][k]), P=float(r["P_mW"]), f_last=float(r["f_last"]))
    x["holds"] = bool(all(ok[1:]) and x["wrong"] == 0 and x["dev"] <= 8.0)
    rows.append(x)
with open(os.path.join(OUT, tag + "_tol.json"), "w") as f_:
    json.dump(rows, f_, indent=0)
print("| what was varied | value | pairs right without noise or spread | phase error at pair %d (deg) | wrong at pair %d | first-wrong events in decisions at risk | level (mV) | holds |" % (nc - 2, nc - 2))
print("|---|---|---|---|---|---|---|---|")
for x in rows:
    if x["grp"] == "map":
        continue
    print("| %s | %s | %d of %d | %.0f | %d of %d | %d in %d | %.0f | %s |" % (x["grp"], x["what"], x["right"], x["of"], x["dev"], x["wrong"], x["n"], x["events"], x["risk"], x["level"], "yes" if x["holds"] else "no"))
