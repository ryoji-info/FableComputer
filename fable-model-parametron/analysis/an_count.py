# -*- coding: utf-8 -*-
"""Rows: pairs right without noise or spread, and first-wrong events, per setting. Writes chain_<tag>_count.json.

This is the count that the session's table script made for the rows of 92 pairs (batch g28f) straight from the
array files. It is written to a small file here so that tables.py needs no arrays.
  - "right" of "of": pairs right in the run without noise or spread, read in the last window of their on-time
    (ref_ok of an_chain3.py).
  - A first-wrong event is the first pair, counted from pair 1, whose decision in a slot of a run lies more than
    90 degrees from the run without noise or spread. "risk" is the number of decisions up to that pair, summed over
    runs and slots (all pairs but the driven one when no pair is wrong). Slot 0 is left out.
Needs chain_<tag>_summary.json, written by an_chain3.py, and the array files.
usage: python an_count.py <tag> [<array folder>] [out=<folder>]"""
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
d = load_npz(os.path.join(D, tag + "_c000.npz"))
rows = []
for si, (s, r) in enumerate(zip(S["SET"], S["res"])):
    if r is None:
        continue
    ns = len(m["expect"][s["topo"]])
    ir = np.where((d["tags"] == si) & d["ref"])[0][0]
    iN = np.where((d["tags"] == si) & ~d["ref"])[0]
    W = np.real(np.exp(1j * (d["PE"][iN, 1:ns] - d["PE"][ir, 1:ns][None]))) < 0
    W[:, :, 0] = False
    nc = W.shape[2]
    first = np.where(W.any(2), W.argmax(2), nc)
    rows.append(dict(grp=s.get("grp", ""), V=s.get("V"), pump=s.get("pump"), lsig=s.get("lsig", 0.0), scale=s.get("scale"), runs=int(len(iN)), slots=int(ns - 1),
                     right=int(sum(r["ref_ok"])), of=len(r["ref_ok"]), events=int((first < nc).sum()), risk=int(np.minimum(first, nc - 1).sum())))
    print("%-60s %d of %d right; %d first-wrong events in %d decisions at risk" % (rows[-1]["grp"][:60], rows[-1]["right"], rows[-1]["of"], rows[-1]["events"], rows[-1]["risk"]))
with open(os.path.join(OUT, tag + "_count.json"), "w") as f_:
    json.dump(rows, f_, indent=0)
