# -*- coding: utf-8 -*-
"""Rebuild the tables of results of the paper from the stored runs in runs/ alone, and write tables.md.

usage: python tables.py [out=<file>]          (default: tables.md beside this script)

It reads runs/MANIFEST.json and the gzip-compressed analysis files beside it. It needs no array file.
One table per kind of batch, every line with its batch:
  T-1  rows of sixteen at the operating point (batch g29)
  T-2  rows of sixteen: single tolerances and spreads (an_tol4.py)
  T-3  rows of sixteen with a 3 % spread of the inductance: supply levels at which the row holds, per pump level
  T-4  rows of sixteen at other carriers, with other diodes and contacts, and under other assumptions (an_d32.py)
  T-5  adders without state (an_logic5.py)
  T-6  layouts with state: the serial adder and the accumulator (an_seq4.py)
  T-7  rows of 92 pairs (an_count.py)
  T-8  the spread budget of the four-bit adder, with exact binomial intervals
Only runs without link capacitors are tabulated (cc = 0 in the settings). The one line of the stored runs that has
them (batch g52) is named under the tables and left out. Batches that are queued but have no result here, and
batches with results but no analysis file, are listed at the end. Nothing is filled in for them.
Every number is in-model.
"""
import gzip
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "runs")
STEP = 0.015

DESCR = {"radd4": "four-bit adder", "radd8": "eight-bit adder", "rdd4": "four-bit adder on two rails", "sdaddx": "serial adder",
         "sdacc8x": "accumulator of eight-bit words", "row": "row"}
NOTE = {"g32": "other carriers", "g33": "variants of what is assumed", "g39": "1.075-THz pairs with other diodes", "g46": "1.075-THz pairs with other contacts",
        "g35a": "other carriers", "g35b": "other carriers", "g44": "other diodes", "g47": "other contacts",
        "g48": "1-THz-class cell at its own noise", "g49": "1-THz-class cell at its own noise", "g50": "1-THz-class cell at its own noise",
        "g51": "1-THz-class cell at its own noise", "g52": "spread budget, 256 draws per line", "g53": "spread budget, 256 draws per line",
        "g54a": "raised noise, no spread", "g54b": "raised noise, no spread", "g54c": "raised noise, no spread", "g54d": "raised noise, no spread",
        "g54e": "raised noise, no spread"}


def runs_json(name):
    p = os.path.join(RUNS, name + ".gz")
    if not os.path.exists(p):
        return None
    with gzip.open(p, "rt") as f:
        return json.load(f)


def manifest():
    with open(os.path.join(RUNS, "MANIFEST.json"), encoding="utf-8") as f:
        return json.load(f)


def n(x):
    return "{:,}".format(x)


def pct(x):
    """a share in per cent: two decimals below 1 %, one above"""
    return "%.2f" % (100 * x) if 0 < 100 * x < 1 else "%.1f" % (100 * x)


def cdf(k, nn, p):
    return sum(math.comb(nn, i) * p ** i * (1 - p) ** (nn - i) for i in range(0, k + 1))


def cp(k, nn, a=0.05):
    """exact (Clopper-Pearson) interval of a binomial share k of nn, at confidence 1 - a, by bisection"""
    def solve(f, lo, hi):
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            if f(mid):
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)
    lo = 0.0 if k == 0 else solve(lambda p: 1 - cdf(k - 1, nn, p) < a / 2, 0.0, 1.0)
    hi = 1.0 if k == nn else solve(lambda p: cdf(k, nn, p) > a / 2, 0.0, 1.0)
    return lo, hi


def budget_rows(man=None):
    """lines of the spread budget: the four-bit adder with the full set of nine spreads (or a fraction of it), without
    link capacitors, from lines with 256 runs or more (batches of 32 runs cannot size a failing share of a few per cent). For each: failing runs (a run fails when any of its 31 additions is wrong), the share and its exact
    95 % interval, bad pairs per thousand, and the chance that a machine of 1,000 or 10,000 pairs is right IF pairs
    failed independently (an assumption)."""
    man = man or manifest()
    rows = []
    for b in man["batches"]:
        t = b["tag"]
        L = runs_json("chain_%s_logic.json" % t)
        if not L or b.get("layout") != ["radd4"]:
            continue
        cc = cc_of(t)
        for r in L:
            g = r["grp"]
            if "full set" not in g and "every spread at once" not in g:
                continue
            if cc.get(g) or r["runs"] < 256:
                continue
            k, nn = r["runs_wrong_add"], r["runs"]
            lo, hi = cp(k, nn)
            per_pair = k / nn / b["pairs"]
            m = re.search(r"full set x ([0-9.]+)", g)
            rows.append(dict(batch=t, line=g, fraction=float(m.group(1)) if m else 1.0, noise="1-THz-class cell" if g.startswith("1.075 THz") else ("225-GHz cell" if g.startswith("225 GHz") else "as in the batch"),
                             runs=nn, failing=k, share=k / nn, lo=lo, hi=hi, wrong_add=r["wrong_add"], n_add=r["n_add"], pairs=b["pairs"],
                             per_1000=1000 * per_pair, per_1000_lo=1000 * lo / b["pairs"], per_1000_hi=1000 * hi / b["pairs"],
                             ok_1000=(1 - per_pair) ** 1000, ok_10000=(1 - per_pair) ** 10000))
    return rows


_cc = {}


def cc_of(tag):
    """link capacitor of each setting of a batch, by its line name (grp)"""
    if tag not in _cc:
        S = runs_json("chain_%s_set.json" % tag)
        if S is None:
            idx = runs_json("chain_%s.json" % tag)
            S = idx["SET"] if idx else []
        d = {}
        for s in S:
            g = s.get("grp", "")
            d[g] = d.get(g, 0.0) or float(s.get("cc", 0.0) or 0.0)
        _cc[tag] = d
    return _cc[tag]


def ranges(hv, vs):
    if not hv:
        return "none"
    runs, cur = [], [hv[0]]
    for v in hv[1:]:
        if abs(v - cur[-1] - STEP) < 1e-6:
            cur.append(v)
        else:
            runs.append(cur)
            cur = [v]
    runs.append(cur)
    return "; ".join(("%.3f to %.3f V" % (r[0], r[-1]) if len(r) > 1 else "%.3f V" % r[0]) + (" (scan ends)" if abs(r[-1] - vs[-1]) < 1e-6 or abs(r[0] - vs[0]) < 1e-6 else "") for r in runs)


def build():
    man = manifest()
    B = {b["tag"]: b for b in man["batches"]}
    out, used, skipped_cc = [], set(), []
    P = out.append

    def table(title, head, rows, note=None):
        P("## " + title + "\n")
        P("| " + " | ".join(head) + " |")
        P("|" + "---|" * len(head))
        for r in rows:
            P("| " + " | ".join(str(x) for x in r) + " |")
        P("")
        if note:
            P(note + "\n")

    def has(t, kind):
        return any(x["name"] == "chain_%s_%s.json" % (t, kind) for x in B[t]["files"]) if t in B else False

    def keep(t, g):
        if cc_of(t).get(g):
            skipped_cc.append("%s: %s" % (t, g))
            return False
        return True

    P("# Tables of results\n")
    P("Rebuilt by `tables.py` from the stored runs in `runs/`. Every number is in-model. Only runs without link "
      "capacitors. A row of sixteen \"holds\" when every pair from 1 on is right without noise or spread, no decision "
      "at pair 14 is wrong and the rms phase error there is at most 8 degrees. A decision is wrong when its phase, read "
      "when the next pair decides, lies more than 90 degrees from that of the run without noise or spread. Slot 0 is "
      "left out of every count. A run is one draw of the spreads with its own noise.\n")

    # T-1 ------------------------------------------------------------------
    rows = []
    for t in sorted(B):
        if B[t]["status"] != "results" or B[t].get("layout") != ["row"] or B[t].get("pairs") != 16 or not has(t, "count"):
            continue
        for r in runs_json("chain_%s_count.json" % t):
            if keep(t, r["grp"]):
                rows.append([r["grp"], "%d of %d" % (r["right"], r["of"]), n(r["runs"]), "%s in %s" % (n(r["events"]), n(r["risk"])), t])
        used.add(t)
    if rows:
        table("T-1. Rows of sixteen at the operating point", ["condition", "pairs right without noise or spread", "runs", "first-wrong events in decisions at risk", "batch"], rows,
              "0.94 V, 25 % pump, links 6 %, unless the line says otherwise. A first-wrong event is the first pair of a slot of a run, counted from pair 1, that is wrong. "
              "The decisions at risk are those up to that pair. Pairs right are read in the last window of the on-time, decisions when the next pair decides (an_count.py).")

    # T-2 and T-3 ------------------------------------------------------------
    rows, rows3 = [], []
    for t in sorted(B):
        if not has(t, "tol"):
            continue
        T = runs_json("chain_%s_tol.json" % t)
        used.add(t)
        for x in T:
            if x["grp"] == "map" or not keep(t, x["grp"]):
                continue
            rows.append([x["grp"], x["what"], "%d of %d" % (x["right"], x["of"]), "%.1f" % x["dev"], "%s of %s" % (n(x["wrong"]), n(x["n"])),
                         "%s in %s" % (n(x["events"]), n(x["risk"])), "%.0f" % x["level"], "yes" if x["holds"] else "no", t])
        by = {}
        for x in T:
            if x["grp"] == "map" and abs(x["lsig"] - 0.03) < 1e-9:
                by.setdefault(x["pump"], {})[round(x["V"], 3)] = x
        for p in sorted(by):
            vs = sorted(by[p])
            rows3.append(["%.0f %%" % (100 * p), "%.3f to %.3f V" % (vs[0], vs[-1]), ranges([v for v in vs if by[p][v]["holds"]], vs), t])
    if rows:
        table("T-2. Rows of sixteen: single tolerances and spreads", ["what was varied", "value", "pairs right without noise or spread", "rms phase error at pair 14 (deg)",
                                                                      "wrong decisions at pair 14", "first-wrong events in decisions at risk", "level at pair 14 (mV)", "holds", "batch"], rows,
              "0.94 V and a 25 % pump unless the line says otherwise. Phase error, wrong decisions and level at pair 14 are read when the next pair decides; the level is that of the run without noise or spread.")
    if rows3:
        table("T-3. Rows of sixteen with a 3 % spread of the inductance: supply levels at which the row holds", ["pump level", "scanned", "holds", "batch"], rows3,
              "Steps of 15 mV. \"(scan ends)\" marks a range that reaches an end of the scan.")

    # T-4 ------------------------------------------------------------------
    rows = []
    for t in sorted(B, key=lambda s: (int(re.match(r"g(\d+)", s).group(1)), s)):
        if not has(t, "holds"):
            continue
        used.add(t)
        for x in runs_json("chain_%s_holds.json" % t):
            f = "; ".join(("%.3f to %.3f V" % (r[0], r[-1]) if len(r) > 1 else "%.3f V" % r[0]) for r in x["holds"]) or "none"
            rows.append([NOTE.get(t, ""), x["cell"], "%+.2f pi" % (x["pph"] - 0.25), "%.0f %%" % (100 * x["pump"]), "%.3f to %.3f V" % tuple(x["scanned"]), f, "%.0f" % x["level"], t])
    if rows:
        table("T-4. Rows of sixteen at other carriers, with other diodes and contacts, and under other assumptions: supply levels at which the row holds",
              ["set", "cell", "input phase against the aligned value", "pump", "scanned", "holds", "level at the middle of the widest range (mV)", "batch"], rows,
              "A 3 % spread of the inductance and the noise of each cell, 32 runs per supply level, steps of 15 mV. Cell names are those of the settings files.")

    # T-5 and T-6 ------------------------------------------------------------
    rows5, rows6 = [], []
    for t in sorted(B, key=lambda s: (int(re.match(r"g(\d+)", s).group(1)), s)):
        b = B[t]
        lay = "%s, %d pairs" % (DESCR.get(b["layout"][0], b["layout"][0]), b["pairs"]) if b.get("layout") else "?"
        if has(t, "logic"):
            used.add(t)
            for r in runs_json("chain_%s_logic.json" % t):
                if not keep(t, r["grp"]):
                    continue
                ref = "%d of %d" % (r["ref_right"], r["n"])
                rows5.append([lay, NOTE.get(t, ""), r["grp"], ref, "%.0f" % r["level_min"], "%s of %s" % (n(r["wrong_add"]), n(r["n_add"])),
                              "%d of %d" % (r["runs_wrong_add"], r["runs"]), "%s of %s" % (n(r["wrong"]), n(r["n_dec"])), t])
        if has(t, "seq"):
            used.add(t)
            for r in runs_json("chain_%s_seq.json" % t):
                if not keep(t, r["grp"]):
                    continue
                unit = "sums" if r["topo"].startswith(("sdadd", "sadd")) else "words"
                rows6.append([lay, NOTE.get(t, ""), r["grp"], "%d of %d" % (r["ref_right"], r["n"]), "%.0f" % r["level_min"],
                              "%s of %s %s" % (n(r.get("wrong_words", 0)), n(r.get("n_words", 0)), unit), "%d of %d" % (r.get("runs_wrong", 0), r["runs"]),
                              "%s of %s" % (n(r.get("wrong", 0)), n(r.get("n_dec", 0))), t])
    if rows5:
        table("T-5. Adders without state", ["layout", "note", "condition", "pairs right without noise or spread", "lowest level without noise or spread (mV)", "wrong additions",
                                             "runs with a wrong addition", "wrong decisions of any pair", "batch"], rows5,
              "An addition is wrong when any output pair is wrong in that slot. A run has 31 additions. The run without noise or spread is judged when the next pairs decide (refcheck.py).")
    if rows6:
        table("T-6. Layouts with state: the serial adder and the accumulator", ["layout", "note", "condition", "pairs right without noise or spread", "lowest level without noise or spread (mV)",
                                                                              "wrong sums or words", "runs with a wrong decision", "wrong decisions of any pair", "batch"], rows6,
              "In the serial adder a run is one long sum, and it is wrong when any sum bit is wrong. In the accumulator a word is wrong when any of its sum bits is wrong.")

    # T-7 ------------------------------------------------------------------
    rows = []
    for t in sorted(B):
        b = B[t]
        if b.get("layout") == ["row"] and b.get("pairs") and b["pairs"] > 16 and has(t, "count"):
            used.add(t)
            for r in runs_json("chain_%s_count.json" % t):
                if keep(t, r["grp"]):
                    rows.append([r["grp"], "%d of %d" % (r["right"], r["of"]), n(r["runs"]), "%d" % r["slots"], "%s in %s" % (n(r["events"]), n(r["risk"])), t])
    if rows:
        table("T-7. Rows of 92 pairs", ["condition", "pairs right without noise or spread", "runs", "slots counted", "first-wrong events in decisions at risk", "batch"], rows,
              "0.94 V, 25 % pump, links 6 %. Counted as in T-1. Without the pump a pair is right only by chance.")

    # T-8 ------------------------------------------------------------------
    rows = []
    for x in budget_rows(man):
        used.add(x["batch"])
        rows.append(["%g" % x["fraction"], x["noise"], "%d of %d" % (x["failing"], x["runs"]), "%s %% (%s to %s %%)" % (pct(x["share"]), pct(x["lo"]), pct(x["hi"])),
                     "%s of %s" % (n(x["wrong_add"]), n(x["n_add"])), "%.2f (%.2f to %.2f)" % (x["per_1000"], x["per_1000_lo"], x["per_1000_hi"]),
                     "%.2f" % x["ok_1000"], "%.3f" % x["ok_10000"], x["batch"]])
    if rows:
        table("T-8. Spread budget: the four-bit adder with the full set of nine spreads, or a fraction of it",
              ["fraction of the full set", "noise", "failing runs", "share, with its exact 95 % interval", "wrong additions", "bad pairs per thousand, with its interval",
               "share of machines of 1,000 pairs right", "share of machines of 10,000 pairs right", "batch"], rows,
              "0.94 V, 25 % pump, links 6 %, 53 pairs. The full set has nine rms spreads: inductance 3 %, diode current 5 %, difference inside a pair 2 %, pump phase 10 degrees, "
              "pump level 10 %, link strength 10 %, clock timing 2 % of the period, supply level 1 % and damping resistor 5 %. A fraction s multiplies each by s. "
              "A run fails when any of its 31 additions is wrong. The interval is the exact (Clopper-Pearson) binomial interval. "
              "Bad pairs per thousand is the failing share divided by 53. The two columns on machines assume that pairs fail independently, "
              "which no run has tested; no layout larger than 53 pairs has been run with 256 draws.")

    # what is not in the tables ----------------------------------------------
    P("## Batches not in these tables\n")
    miss = []
    for t in sorted(B, key=lambda s: (int(re.match(r"g(\d+)", s).group(1)), s)):
        b = B[t]
        lay = "%s, %s pairs" % (DESCR.get(b["layout"][0], b["layout"][0]), b.get("pairs")) if b.get("layout") else "layout unknown"
        if b["status"].startswith("queued"):
            miss.append("- %s (%s; %s): queued, no result in the stored runs" % (t, lay, NOTE.get(t, "") or "see its settings"))
        elif b["status"].startswith("copy"):
            miss.append("- %s: %s" % (t, b["status"]))
        elif t not in used:
            miss.append("- %s (%s): results stored, but no analysis file for these tables (the checks of time step, stub grid and precision were compared by a separate session script)" % (t, lay))
    for m_ in miss or ["- none"]:
        P(m_)
    P("")
    if skipped_cc:
        P("Lines left out because they have link capacitors (cc > 0): " + "; ".join(sorted(set(skipped_cc))) + ".\n")
    return "\n".join(out) + "\n"


def main(argv):
    kw = dict(a.split("=", 1) for a in argv[1:] if "=" in a)
    fn = kw.get("out", os.path.join(HERE, "tables.md"))
    text = build()
    with open(fn, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    heads = [l for l in text.split("\n") if l.startswith("## ")]
    print("%s: %d tables, %d characters" % (os.path.basename(fn), sum(1 for h in heads if h.startswith("## T-")), len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
