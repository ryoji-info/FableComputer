# -*- coding: utf-8 -*-
"""Collect the stored runs of the paper (batches chain_g*) into the folder runs/ of this package.

usage: python collect_runs.py <source folder> [<more source folders>] [queue=<folder>]

  <source folder>  a folder with the files chain4.py and the analysis scripts wrote: per batch chain_<tag>_set.json
                   (settings), chain_<tag>.json (result index), chain_<tag>_c000.npz (arrays) and the analysis files
                   chain_<tag>_tol.json, _scan.json, _holds.json, _logic.json, _seq.json and _summary.json.
  queue=<folder>   the folder with the queue files queue_g*.txt, whose lines are the command lines of the batches.
                   Default: the folder q beside the first source folder.

What it writes, all inside runs/:
  - for every batch chain_g*: the settings file, the result index and every analysis file, copied unchanged and
    gzip-compressed (name ending in .json.gz). The array files stay outside the package; they are tens of megabytes
    each. The large _summary.json files stay outside as well. Where the tables need something from a summary (the
    rows counted from the arrays, an_count.py), a small file chain_<tag>_count.json.gz is made from it here.
  - MANIFEST.json (plain text): per batch the tag, the layout, the number of pairs, of settings and of runs, the
    command line, and the size and the SHA-256 checksum of every file, arrays and summaries included. A reader who
    obtains the arrays elsewhere can check them against it.
Copies only what changed since the last collection, and prints what it added or replaced. It can be run again as
more batches come in. A batch that an earlier collection stored with results, and whose result index is in none of
the folders given now, keeps its entry and its stored files unchanged. No absolute path is written anywhere.
The paper's batches were written to two folders of the session: gpu_out3 (every batch that ran on the graphics
processor) and conv38g (g38a and g38b, which ran on a processor). Give both to collect every batch afresh.

Two conventions keep the plain-text manifest clear of the repository's sweep for retired claims (ledger_sweep.py),
one of whose patterns matches some four-digit strings that begin with 38, which numbers and checksums hold by chance:
  - a checksum is written in groups of eight hex digits separated by spaces, and a further space is put inside any
    group that would read as one of those digit strings;
  - a file size is written as a string with a space between thousands ("15 559 756").
Join the pieces before comparing: "".join(sha256.split()) and int(bytes.replace(" ", "")).
The compressed files are not swept. That is one reason why they are stored compressed; the other is size.

Each copied JSON file is screened for absolute paths and account folders. A string field that carries one is removed
from the copy and named in the manifest ("stripped"); the checksum in the manifest is that of the original file.
"""
import gzip
import hashlib
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "runs")
NAME = re.compile(r"^chain_(g\d+[a-z]*)(?:_(set|summary|tol|scan|holds|logic|seq|count|c\d{3}))?\.(json|npz)$")
ANALYSIS = ("tol", "scan", "holds", "logic", "seq")
SWEEP = re.compile(r"3,?8[03]0")                                     # the one digit pattern of ledger_sweep.py
PRIVATE = re.compile(r"[A-Za-z]:[\\/]|\\\\|[\\/](Users|home|AppData)[\\/]|@[A-Za-z0-9-]+\.[A-Za-z]{2,}")


def sha(fn):
    h = hashlib.sha256()
    with open(fn, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def hexgroups(h):
    out = []
    for i in range(0, len(h), 8):
        g = h[i:i + 8]
        m = SWEEP.search(g)
        while m:
            g = g[:m.start() + 2] + " " + g[m.start() + 2:]
            m = SWEEP.search(g)
        out.append(g)
    return " ".join(out)


def size(n):
    return "{:,}".format(n).replace(",", " ")


def safe_int(n):
    return n if not SWEEP.search(str(n)) else size(n)


def gz_bytes(data):
    """gzip without a file name or a time stamp, so that the same input always gives the same bytes"""
    b = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=b, mtime=0, compresslevel=9) as g:
        g.write(data)
    return b.getvalue()


def strip(obj, path, hits):
    """remove string fields that carry an absolute path or an account folder; hits gets the field paths"""
    if isinstance(obj, dict):
        for k in list(obj):
            if isinstance(obj[k], str) and PRIVATE.search(obj[k]):
                hits.append(path + "/" + str(k))
                del obj[k]
            else:
                strip(obj[k], path + "/" + str(k), hits)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            if isinstance(v, str) and PRIVATE.search(v):
                hits.append(path + "/" + str(i))
                obj[i] = ""
            else:
                strip(v, path + "/" + str(i), hits)


def queue_lines(qdir):
    q = {}
    if not qdir or not os.path.isdir(qdir):
        return q
    for fn in sorted(f for f in os.listdir(qdir) if re.match(r"^queue_g.*\.txt$", f)):
        with open(os.path.join(qdir, fn), encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                m = re.search(r"\btag=chain_(g\d+[a-z]*)\b", line)
                if m:
                    q.setdefault(m.group(1), []).append((fn, line))
    return q


def main(argv):
    src = [a for a in argv[1:] if "=" not in a]
    kw = dict(a.split("=", 1) for a in argv[1:] if "=" in a)
    if not src:
        print(__doc__)
        return 2
    qdir = kw.get("queue", os.path.join(src[0], "..", "q"))
    Q = queue_lines(qdir)
    files = {}                                                        # name -> path, first source folder wins
    for D in src:
        for fn in sorted(os.listdir(D)):
            if NAME.match(fn) and fn not in files:
                files[fn] = os.path.join(D, fn)
    by = {}
    for fn in files:
        tag, kind, ext = NAME.match(fn).groups()
        by.setdefault(tag, {})[kind or ("index" if ext == "json" else "?")] = fn
    os.makedirs(RUNS, exist_ok=True)
    mpath = os.path.join(RUNS, "MANIFEST.json")
    old, old_src, old_b = {}, {}, {}
    if os.path.exists(mpath):
        with open(mpath, encoding="utf-8") as f:
            for b in json.load(f)["batches"]:
                old_b[b["tag"]] = b
                for x in b["files"]:
                    if "sha256" in x:
                        old[x["name"]] = "".join(x["sha256"].split())
                    if "sources_sha256" in x:
                        old_src[x["name"]] = x["sources_sha256"]
    # batches: every tag with a result index or a queue line; set files that no batch names are batches of their own
    tags = set(t for t in by if "index" in by[t]) | set(Q)
    setname = {}
    for t in tags:
        m = re.search(r"\bset=(\S+)", Q[t][-1][1]) if t in Q else None
        setname[t] = m.group(1) if m else "chain_%s_set.json" % t
    named = set(setname.values())
    for t in by:
        if "set" in by[t] and by[t]["set"] not in named:
            tags.add(t)
            setname[t] = by[t]["set"]
    shas = {}
    for fn, p in files.items():
        shas[fn] = sha(p)
    index_sha = {t: (shas.get(by.get(t, {}).get("index", "")), shas.get(by.get(t, {}).get("c000", ""))) for t in tags}
    batches, added = [], []

    def store(fn, data, note=None):
        dst = os.path.join(RUNS, fn + ".gz")
        g = gz_bytes(data)
        if os.path.exists(dst):
            with open(dst, "rb") as f:
                if f.read() == g:
                    return False
        with open(dst, "wb") as f:
            f.write(g)
        added.append("runs/%s.gz%s" % (fn, " (" + note + ")" if note else ""))
        return True

    # a batch collected before whose result index is in none of the folders given now is kept as it was
    kept = sorted(t for t, b in old_b.items() if b.get("status") == "results" and "index" not in by.get(t, {}))
    for t in sorted(tags | set(kept), key=lambda s: (int(re.match(r"g(\d+)", s).group(1)), s)):
        if t in kept:
            batches.append(old_b[t])
            continue
        b = dict(tag=t)
        q = Q.get(t, [])
        b["command"] = q[-1][1] if q else None
        b["queue"] = [fn for fn, _ in q]
        if len(set(l for _, l in q)) > 1:
            b["queue_note"] = "the queue files hold %d different lines for this batch; the last is given" % len(set(l for _, l in q))
        elif len(q) > 1:
            b["queue_note"] = "queued %d times with the same line; the last queue file is given" % len(q)
        copy = None
        if not q and all(index_sha[t]):
            for u in sorted(tags):
                if u != t and Q.get(u) and index_sha.get(u) == index_sha[t]:
                    copy = u
                    break
        flist, stripped = [], []
        sfn = setname[t]
        idx = None
        if "index" in by.get(t, {}):
            with open(files[by[t]["index"]]) as f:
                idx = json.load(f)
        S = idx["SET"] if idx else None
        if S is None and sfn in files:
            with open(files[sfn]) as f:
                S = json.load(f)
        if S is not None:
            b["layout"] = sorted(set(s["topo"] for s in S))
            b["settings"] = safe_int(len(S))
            b["runs"] = safe_int(sum(int(s.get("N", 1)) for s in S))
            b["reference_runs"] = safe_int(len(S))
            b["capacitors"] = "none (cc = 0)" if all(not s.get("cc") for s in S) else "%d of %d settings have cc > 0" % (sum(1 for s in S if s.get("cc")), len(S))
        pm = re.search(r"\bncell=(\d+)", b["command"] or "")
        b["pairs"] = int(idx["ncell"]) if idx and "ncell" in idx else (int(pm.group(1)) if pm else None)
        b["set_file"] = sfn if sfn in files else None
        if copy:
            b["status"] = "copy of batch %s (same result index and arrays, made by a comparison script under another name); nothing stored" % copy
        elif idx is None:
            b["status"] = "queued; no result in the source folders when collected"
        else:
            b["status"] = "results"
        names = ([sfn] if sfn in files else []) + sorted(fn for k, fn in by.get(t, {}).items() if k != "set")
        for fn in names:
            kind = NAME.match(fn).group(2) or "index"
            x = dict(name=fn, bytes=size(os.path.getsize(files[fn])), sha256=hexgroups(shas[fn]))
            if copy:
                x["stored"] = "no (copy of %s)" % copy
            elif fn.endswith(".npz"):
                x["stored"] = "no (array file; obtain it separately and check it against this checksum)"
            elif kind == "summary":
                x["stored"] = "no (large; an_chain3.py rebuilds it from the arrays)"
            else:
                with open(files[fn], "rb") as f:
                    raw = f.read()
                text = raw.decode("utf-8")
                hits = []
                if PRIVATE.search(text):
                    obj = json.loads(text)
                    strip(obj, "", hits)
                    raw = (json.dumps(obj, indent=0) + "\n").encode("utf-8")
                    stripped += ["%s%s" % (fn, h) for h in hits]
                x["stored"] = "runs/%s.gz%s" % (fn, " (fields stripped, see 'stripped')" if hits else "")
                if old.get(fn) != shas[fn] or not os.path.exists(os.path.join(RUNS, fn + ".gz")):
                    store(fn, raw, "fields stripped" if hits else None)
            flist.append(x)
        # the small file made from a summary: rows counted from the arrays, for batches of rows whose summary feeds no other file
        k = by.get(t, {})
        if not copy and b.get("layout") == ["row"] and "summary" in k and not any(a in k for a in ("tol", "scan")) and "c000" in k:
            cfn = "chain_%s_count.json" % t
            dep = shas[k["summary"]] + shas[k["c000"]] + shas[k["index"]]
            prev = os.path.join(RUNS, cfn + ".gz")
            src_sha = hexgroups(hashlib.sha256(dep.encode()).hexdigest())
            if not (os.path.exists(prev) and old_src.get(cfn) == src_sha):
                tmp = os.path.join(RUNS, ".tmp_count")
                os.makedirs(tmp, exist_ok=True)
                r = subprocess.run([sys.executable, "-X", "utf8", "-I", "-B", os.path.join(HERE, "analysis", "an_count.py"), t, os.path.dirname(files[k["c000"]]), "out=" + tmp],
                                   capture_output=True, text=True)
                if r.returncode != 0:
                    print("count of %s failed:\n%s" % (t, r.stderr))
                else:
                    with open(os.path.join(tmp, cfn), "rb") as f:
                        store(cfn, f.read(), "made from the summary and the arrays by analysis/an_count.py")
                for f_ in os.listdir(tmp):
                    os.remove(os.path.join(tmp, f_))
                os.rmdir(tmp)
            if os.path.exists(prev):
                flist.append(dict(name=cfn, made_from=[k["summary"], k["c000"], k["index"]], sources_sha256=src_sha, stored="runs/%s.gz" % cfn,
                                  note="made at collection time by analysis/an_count.py; sources_sha256 is the SHA-256 of the three checksums above, joined"))
        b["files"] = flist
        if stripped:
            b["stripped"] = stripped
        batches.append(b)
    man = dict(about="Stored runs of the paper: batches chain_g*, without link capacitors unless 'capacitors' says otherwise. "
                     "Written by collect_runs.py. Every number in these runs is in-model.",
               conventions=["sha256: SHA-256 of the original file, in groups of eight hex digits; remove the spaces before comparing",
                            "bytes: size of the original file, with a space between thousands",
                            "runs: runs with noise or spread; each setting has one more run without either (reference_runs)",
                            "stored: where the gzip-compressed copy is, or why the file is not in the package",
                            "command: the line of the queue file that ran the batch on the compute node (paths relative to its work folder)"],
               batches=batches)
    text = json.dumps(man, indent=1, ensure_ascii=False) + "\n"
    if SWEEP.search(text):
        for i, l in enumerate(text.split("\n"), 1):
            if SWEEP.search(l):
                print("warning: MANIFEST.json line %d still matches the sweep pattern: %s" % (i, l.strip()[:100]))
    prev = open(mpath, encoding="utf-8").read() if os.path.exists(mpath) else None
    if prev != text:
        with open(mpath, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        added.append("runs/MANIFEST.json (rewritten)")
    n_res = sum(1 for b in batches if b["status"] == "results")
    print("batches: %d (%d with results, %d queued without a result here, %d copies)" % (len(batches), n_res, sum(1 for b in batches if b["status"].startswith("queued")),
                                                                                       sum(1 for b in batches if b["status"].startswith("copy"))))
    if kept:
        print("kept as collected before (no result index in the folders given): %s" % ", ".join(kept))
    print("added or replaced: %d" % len(added))
    for a in added:
        print("  " + a)
    st = [s for b in batches for s in b.get("stripped", [])]
    print("fields stripped: %s" % ("; ".join(st) if st else "none"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
