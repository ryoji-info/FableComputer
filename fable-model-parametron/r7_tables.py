# -*- coding: utf-8 -*-
"""r7: rebuild the tables of results from the stored runs and print a digest.

What it shows. tables.py builds every table from runs/ alone, with no array file. This listing builds them in
memory, prints the number of tables, the number of lines of each, the lines left out and the batches missing, and
the SHA-256 checksum of the text. It then compares the text with tables.md as shipped. It does not write any file.
If more batches are collected into runs/ later, the digest changes; run python tables.py to write the new tables.md.
Every number in the tables is in-model. Run time on the reference computer: a few seconds.
usage: python r7_tables.py
"""
import hashlib
import os
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import tables

text = tables.build()
lines = text.split("\n")
print("r7: tables of results rebuilt from runs/ (%d batches in runs/MANIFEST.json)" % len(tables.manifest()["batches"]))
heads = [i for i, l in enumerate(lines) if l.startswith("## ")]
nt = 0
for j, i in enumerate(heads):
    end = heads[j + 1] if j + 1 < len(heads) else len(lines)
    body = [l for l in lines[i + 1:end] if l.startswith("| ")]
    if lines[i].startswith("## T-"):
        nt += 1
        print("   %-100s %4d lines" % (lines[i][3:][:100], len(body) - 1))
    else:
        items = [l for l in lines[i + 1:end] if l.startswith("- ")]
        print("   %-100s %4d entries" % (lines[i][3:][:100], len(items)))
        for l in items:
            print("      " + l[2:][:150])
left = [l for l in lines if l.startswith("Lines left out")]
for l in left:
    print("   " + l[:200])
h = hashlib.sha256(text.encode("utf-8")).hexdigest()
print("tables: %d; characters: %d; lines: %d" % (nt, len(text), len(lines) - 1))
print("SHA-256 of the text (UTF-8, line ends LF): " + " ".join(h[i:i + 8] for i in range(0, 64, 8)))
fn = os.path.join(HERE, "tables.md")
if os.path.exists(fn):
    with open(fn, "rb") as f:
        print("tables.md as shipped: %s" % ("equal" if f.read() == text.encode("utf-8") else "differs (run python tables.py to rewrite it)"))
else:
    print("tables.md as shipped: missing")
