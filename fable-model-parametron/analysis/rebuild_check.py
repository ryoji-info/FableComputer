# -*- coding: utf-8 -*-
"""Rebuild the stored analysis files of the paper's batches from their array files, and compare.

usage: python rebuild_check.py <array folder> [<tag> ...]

<array folder> holds the files chain_<tag>_c000.npz (they are not in the package; runs/MANIFEST.json has their
checksums). Without tags, every batch of runs/MANIFEST.json whose array file is in that folder is rebuilt.
For each batch the scripts of this folder are run in a temporary folder, in the order the session ran them:
  an_chain3.py then an_tol4.py         for a batch with a _tol file (rows of sixteen, tolerances)
  an_chain3.py, an_scan4.py, an_d32.py for a batch with _scan and _holds files (rows at other carriers)
  an_chain3.py then an_count.py        for a batch with a _count file (rows counted from the arrays)
  an_logic5.py                         for a batch with a _logic file (adders without state)
  an_seq4.py                           for a batch with a _seq file (layouts with state)
Each file written is compared with the stored copy in runs/ (decompressed) and with the checksum of the original in
the manifest. A summary file is compared with its checksum only, since the package does not store it.
"bitwise equal" means the same bytes. "equal apart from line ends" means the same text once line ends are made
alike: the stored files were written on Windows, which ends each line with two characters.
The array files are checked against the manifest first; a batch whose array file differs is skipped.
"""
import gzip
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(os.path.dirname(HERE), "runs")
PY = [sys.executable, "-X", "utf8", "-I", "-B"]                   # -B: no __pycache__ folder inside the package


def sha(fn):
    h = hashlib.sha256()
    with open(fn, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    A = argv[1]
    want = [t if not t.startswith("chain_") else t[6:] for t in argv[2:]]
    with open(os.path.join(RUNS, "MANIFEST.json"), encoding="utf-8") as f:
        man = json.load(f)
    tot = dict(files=0, bitwise=0, lineends=0, differ=0)
    for b in man["batches"]:
        t = b["tag"]
        if want and t not in want:
            continue
        if b["status"] != "results":
            if want:
                print("%-5s not rebuilt: %s" % (t, b["status"]))
            continue
        files = {x["name"]: x for x in b["files"]}
        kinds = [k for k in ("tol", "scan", "holds", "logic", "seq", "count") if "chain_%s_%s.json" % (t, k) in files]
        npz = "chain_%s_c000.npz" % t
        if not kinds:
            if not want:
                continue
            print("%-5s no analysis file is stored for this batch" % t)
            continue
        if not os.path.exists(os.path.join(A, npz)):
            if want:
                print("%-5s array file not in %s" % (t, A))
            continue
        if sha(os.path.join(A, npz)) != "".join(files[npz]["sha256"].split()):
            print("%-5s array file differs from the manifest: skipped" % t)
            continue
        tmp = tempfile.mkdtemp(prefix="rebuild_")
        try:
            steps = []
            if any(k in kinds for k in ("tol", "scan", "count")):
                steps.append(("an_chain3.py", "summary"))
            steps += [{"tol": ("an_tol4.py", "tol"), "scan": ("an_scan4.py", "scan"), "holds": ("an_d32.py", "holds"), "logic": ("an_logic5.py", "logic"),
                       "seq": ("an_seq4.py", "seq"), "count": ("an_count.py", "count")}[k] for k in kinds]
            res = []
            for script, kind in steps:
                r = subprocess.run(PY + [os.path.join(HERE, script), t, A, "out=" + tmp], capture_output=True, text=True)
                fn = "chain_%s_%s.json" % (t, kind)
                p = os.path.join(tmp, fn)
                if r.returncode != 0 or not os.path.exists(p):
                    res.append("%s: FAILED (%s)" % (fn, (r.stderr.strip().split("\n") or ["?"])[-1]))
                    tot["differ"] += 1
                    continue
                with open(p, "rb") as f:
                    new = f.read()
                x = files.get(fn, {})
                if x.get("stored", "").startswith("runs/"):
                    with gzip.open(os.path.join(RUNS, fn + ".gz"), "rb") as f:
                        ref = f.read()
                    how = "against the stored copy"
                else:
                    ref = None
                    how = "against the manifest checksum"
                same_sha = "sha256" in x and hashlib.sha256(new).hexdigest() == "".join(x["sha256"].split())
                if (ref is not None and new == ref) or (ref is None and same_sha):
                    verdict = "bitwise equal"
                    tot["bitwise"] += 1
                elif ref is not None and new.replace(b"\r\n", b"\n") == ref.replace(b"\r\n", b"\n"):
                    verdict = "equal apart from line ends"
                    tot["lineends"] += 1
                elif ref is None and "sha256" in x and hashlib.sha256(new.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")).hexdigest() == "".join(x["sha256"].split()):
                    verdict = "equal apart from line ends"
                    tot["lineends"] += 1
                else:
                    verdict = "DIFFERS"
                    tot["differ"] += 1
                tot["files"] += 1
                res.append("%s %s (%s)" % (fn, verdict, how))
            print("%-5s %s" % (t, "; ".join(res)))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    for t in want:
        if t not in [b["tag"] for b in man["batches"]]:
            print("%-5s not rebuilt: no such batch in runs/MANIFEST.json" % t)
    print("files rebuilt: %d; bitwise equal %d; equal apart from line ends %d; different or failed %d"
          % (tot["files"], tot["bitwise"], tot["lineends"], tot["differ"]))
    return 0 if tot["differ"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
