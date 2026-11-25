# -*- coding: utf-8 -*-
"""Helpers shared by the analysis scripts of this folder.

Every analysis script takes the same arguments:

    python an_<name>.py <tag> [<folder>] [out=<folder>]

  <tag>     the batch, for example g34b or chain_g34b
  <folder>  the folder that holds the array files chain_<tag>_c000.npz (default: the current folder)
  out=      the folder the script writes its analysis file to (default: <folder>)

A JSON file that a script reads (the result index chain_<tag>.json, or an analysis file written by an earlier
script) is looked for in the out folder, then in <folder>, then in the folder runs/ of this package. In each place
the plain file and the gzip-compressed file (name ending in .json.gz) are both accepted. So a reader who has the
array files only needs this package for the rest.
"""
import gzip
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(os.path.dirname(HERE), "runs")


def args(argv):
    """(tag, array folder, out folder) from the command line."""
    pos = [a for a in argv[1:] if not a.startswith("-") and "=" not in a]
    kw = dict(a.split("=", 1) for a in argv[1:] if "=" in a)
    tag = pos[0]
    if not tag.startswith("chain_"):
        tag = "chain_" + tag
    D = pos[1] if len(pos) > 1 else "."
    out = kw.get("out", D)
    os.makedirs(out, exist_ok=True)
    return tag, D, out


def find(name, *folders):
    """Path of the file name (or name.gz) in the folders given, then in runs/; None if it is nowhere."""
    for D in folders + (RUNS,):
        for n in (name, name + ".gz"):
            p = os.path.join(D, n)
            if os.path.exists(p):
                return p
    return None


def load_json(name, *folders):
    p = find(name, *folders)
    if p is None:
        raise FileNotFoundError("%s (looked in %s and in runs/)" % (name, ", ".join(folders)))
    if p.endswith(".gz"):
        with gzip.open(p, "rt") as f:
            return json.load(f)
    with open(p) as f:
        return json.load(f)


def load_npz(fn):
    """Every array of an npz file, read once; the file is closed at once (an open file cannot be deleted on Windows)."""
    import numpy as np
    with np.load(fn) as d:
        return {k: d[k] for k in d.files}
