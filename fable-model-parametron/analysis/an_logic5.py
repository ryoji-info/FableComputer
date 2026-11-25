# -*- coding: utf-8 -*-
"""Ripple-carry adders (layouts without state) of a batch of chain4.py. Writes chain_<tag>_logic.json.

Per setting:
  - the run without noise or spread, judged when the next pairs decide (refcheck.early_ref): pairs right, smallest
    margin, lowest level;
  - additions with a wrong output bit, and in how many runs (a run is one draw of the spreads with its own noise);
  - wrong decisions of any pair, and runs with any wrong decision;
  - which kind of pair erred first in the failing runs ("first").
Slot 0 is left out. A decision is wrong when its phase, read when the next pair decides, lies more than 90 degrees
from that of the run without noise or spread.
The code is that of the session script of the same name; only its input and output changed (see common.py).
usage: python an_logic5.py <tag> [<array folder>] [out=<folder>] [-q]"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True                  # no __pycache__ folder inside the package
import numpy as np
import refcheck
from common import args, load_json, load_npz

tag, D, OUT = args(sys.argv)
quiet = "-q" in sys.argv
m = load_json(tag + ".json", OUT, D)
d = load_npz(os.path.join(D, tag + "_c000.npz"))
out = []
for si, s in enumerate(m["SET"]):
    if not np.any(d["tags"] == si):
        continue
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
    wa = W[:, :, outs].any(2)                                   # [run, slot] an output bit wrong
    kinds = {}
    for r in range(W.shape[0]):
        if W[r].any():
            sl, pr = np.where(W[r])
            k = pr[np.argmin(sl + dep[pr] / 4.0)]
            kd = "".join(ch for ch in names[k].split(".")[0] if not ch.isdigit())
            kinds[kd] = kinds.get(kd, 0) + 1
    row = dict(grp=s.get("grp", ""), topo=s["topo"], V=s.get("V"), pump=s.get("pump"), km=s.get("km"), T=s.get("T"), ref_right=int(ok.sum()), n=int(len(ok)), margin=float(mg.min()),
               level_min=float(lo.min()), wrong_add=int(wa.sum()), n_add=int(wa.size), runs_wrong_add=int(wa.any(1).sum()), wrong=int(W.sum()), n_dec=int(W.size),
               runs_wrong=int(W.any((1, 2)).sum()), runs=int(len(iN)), first=kinds)
    out.append(row)
    if not quiet:
        print("%-78s %s%3d/%3d right, margin %5.2f, lowest %4.0f mV | additions %4d of %5d wrong in %2d of %3d runs | decisions %5d of %6d, runs %3d | first %s" %
              (row["grp"][:78], "" if row["ref_right"] == row["n"] else "WRONG WITHOUT NOISE ", row["ref_right"], row["n"], row["margin"], row["level_min"], row["wrong_add"], row["n_add"],
               row["runs_wrong_add"], row["runs"], row["wrong"], row["n_dec"], row["runs_wrong"], dict(sorted(kinds.items(), key=lambda kv: -kv[1]))))
with open(os.path.join(OUT, tag + "_logic.json"), "w") as f_:
    json.dump(out, f_, indent=0)
