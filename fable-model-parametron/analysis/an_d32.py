# -*- coding: utf-8 -*-
"""Rows of sixteen of a scan batch: per cell, input phase and pump level, the supply levels at which the row holds.
Writes chain_<tag>_holds.json.

A row holds at a supply level when every pair is right without noise or spread, no decision at pair 14 is wrong and
the rms phase error there is at most 8 degrees. Supply levels are scanned in steps of 15 mV; neighbouring levels
that hold are joined into one range. "(scan ends)" marks a range that reaches an end of the scan, so that its true
end may lie further out. Also given: the level at the middle of the widest range, and the levels at which every pair
is right and no decision is wrong, whatever the phase error.
Reads chain_<tag>_scan.json, written by an_scan4.py (or the stored copy in runs/). It does not read the array files.
The code is that of the session script of the same name; only its input and output changed (see common.py).
usage: python an_d32.py <tag> [<array folder>] [out=<folder>]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True                  # no __pycache__ folder inside the package
from common import args, load_json

tag, D, OUT = args(sys.argv)
scan = load_json(tag + "_scan.json", OUT, D)
names = list(dict.fromkeys(x["cell"].split(" at ")[0] for x in scan))
out = []
for nm in names:
    for pph in sorted(set(x["extra"]["pph"] for x in scan if x["cell"].startswith(nm + " at "))):
        for pump in sorted(set(x["pump"] for x in scan)):
            rows = sorted((x["V"], x) for x in scan if x["cell"].startswith(nm + " at ") and abs(x["pump"] - pump) < 1e-9 and abs(x["extra"]["pph"] - pph) < 1e-9)
            if not rows:
                continue
            vs = [v for v, x in rows]
            hv = [v for v, x in rows if x["right"] == x["of"] and x["wrong"] == 0 and x["dev"] <= 8.0]
            runs, cur = [], []
            for v in hv:
                if cur and abs(v - cur[-1] - 0.015) < 1e-6:
                    cur.append(v)
                else:
                    if cur:
                        runs.append(cur)
                    cur = [v]
            if cur:
                runs.append(cur)
            txt = "; ".join(("%.3f to %.3f V" % (r[0], r[-1]) if len(r) > 1 else "%.3f V" % r[0]) + (" (scan ends)" if abs(r[-1] - vs[-1]) < 1e-6 or abs(r[0] - vs[0]) < 1e-6 else "") for r in runs) or "none"
            best = max(runs, key=len) if runs else []
            lev = dict(rows).get(best[(len(best) - 1) // 2])["level"] if best else 0.0
            nowrong = [v for v, x in rows if x["right"] == x["of"] and x["wrong"] == 0]
            out.append(dict(cell=nm, pph=pph, pump=pump, scanned=[vs[0], vs[-1]], holds=runs, level=lev, no_wrong=nowrong))
            print("%-9s input %.2f pi  pump %2.0f %%  scanned %.3f to %.3f V  holds: %-52s level %3.0f mV | right and no wrong decision at: %s" %
                  (nm, pph, 100 * pump, vs[0], vs[-1], txt, lev, (("%.3f to %.3f" % (nowrong[0], nowrong[-1])) + (" (%d of %d levels)" % (len(nowrong), len(vs)))) if nowrong else "none"))
with open(os.path.join(OUT, tag + "_holds.json"), "w") as f_:
    json.dump(out, f_, indent=0)
