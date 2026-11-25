# -*- coding: utf-8 -*-
"""Table of a design scan of rows (settings with the key "cell"). Writes chain_<tag>_scan.json.

Per cell, supply level, pump level and link strength: the pairs right without noise or spread, and at pair 14 the rms
phase error, the wrong decisions and the level with the spread and noise of the setting. A star in the printed table
marks a row that holds (every pair right, no wrong decision at pair 14, phase error there at most 8 degrees).
Needs chain_<tag>_summary.json, written by an_chain3.py. It does not read the array files.
The code is that of the session script of the same name; only its input and output changed (see common.py).
usage: python an_scan4.py <tag> [<array folder>] [out=<folder>]"""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True                  # no __pycache__ folder inside the package
from common import args, load_json

tag, D, OUT = args(sys.argv)
S = load_json(tag + "_summary.json", OUT, D)
rows = []
for s, r in zip(S["SET"], S["res"]):
    if r is None:
        continue
    n = r.get("n_dec", 0)
    ok = r["ref_ok"]
    k = min(14, len(ok) - 2)
    rows.append(dict(cell=s.get("cell", "?"), V=s.get("V"), pump=s["pump"], km=s["km"], lsig=s.get("lsig", 0), right=int(sum(ok)), of=len(ok), margin=float(min(r["margin"][1:])),
                     dev=float(r["dev_early_deg"][k]), wrong=int(round(r["err_early"][k] * n)), n=n, level=float(r["level_mV"][k]), extra={kk: s[kk] for kk in ("duty", "T", "pph", "fd", "jsig", "scale") if kk in s}))
cells = list(dict.fromkeys(x["cell"] for x in rows))
pumps = sorted(set(x["pump"] for x in rows))
kms = sorted(set(x["km"] for x in rows), reverse=True)
print("per cell: rows = pump level, columns = link strength; entry = pairs right without noise or spread / phase error at pair 14 with the spread (deg) / wrong at pair 14 / level (mV)")
for c in cells:
    sel = [x for x in rows if x["cell"] == c]
    print("cell %s (supply %.2f V), spread %.0f %%:   links " % (c, sel[0]["V"], 100 * sel[0]["lsig"]) + "   ".join("%14s" % ("%.1f %%" % (100 * abs(k))) for k in kms))
    for p in pumps:
        line = []
        for k in kms:
            x = [y for y in sel if y["pump"] == p and y["km"] == k]
            if not x:
                line.append("%17s" % "-")
                continue
            x = x[0]
            line.append("%2d/%3.0f/%3d/%3.0f%s" % (x["right"], x["dev"], x["wrong"], x["level"], " *" if (x["right"] == x["of"] and x["wrong"] == 0 and x["dev"] <= 8) else "  "))
        print("   pump %2.0f %%: " % (100 * p) + "   ".join(line))
with open(os.path.join(OUT, tag + "_scan.json"), "w") as f_:
    json.dump(rows, f_, indent=0)
