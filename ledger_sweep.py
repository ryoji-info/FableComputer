# -*- coding: utf-8 -*-
"""Defect-signature sweep for the Fable Computer record audit (2026-07-26 (IV)).

Answers the assessors' three objections to the previous sweep:
  * file set: adds .pdf/.docx/.json/.yml/.txt and docs/, and stops silently
    excluding .github/ (the old SKIP tested the substring ".git");
  * granularity: dispositions are keyed by FILE:LINE, so a NEW occurrence of a
    covered signature in a covered file is reported, not auto-absorbed;
  * honesty: prints the file set it actually read, and what it cannot see.

    cd <repo root> && PYTHONIOENCODING=utf-8 python ledger_sweep.py

Pure Python (no subprocess/grep); .pdf via pypdf, .docx via zipfile+re, both
optional. notes/ is swept but exempted: promoted notes quote retired claims by
design, so their hits are counted separately rather than requiring an owner.
"""
import json, pathlib, re, zipfile

SIGS = {
    "intracavity":            r"intracavity",
    "charge-memory reading":  r"charge[- ]memory|averages as 1/|buys the 2-bit|averaging over 16 slots",
    "'five decades'":         r"five decades",
    "M_th claim or value":    r"analytic as .x|. analytic as|M_?th_?num\s*=\s*0\.169|M_th,num . 0\.17|Mth_num = 0\.169",
    "unqualified knee/rail":  r"38 (?:plasmons|quanta|intracavity)|1[- ]dB (?:compression )?knee|1 dB at .?.?1 ?%|3,?8[03]0|linear range ends near 38",
    "0.25 THz / 4-ps logic":  r"4-p(?:ico)?second slot|4-ps slot|2\.5\s*.\s*10.. additions|per 4-ps|0\.25[- ]THz|0\.25 THz",
    "phantom 2nd-order":      r"MacCormack",
    "stale version / erratum": r"One known erratum|v5\.5|v1\.6|v5\.2|v1\.2",
}

# (path, line) -> owning finding/entry, or a stated reason it is clean.
DISPOSED = {
    ("fable-model-quantum/qmac.py", 24): "F5/IMP-007 plane mislabel",
    ("fable-model-quantum/qmac.py", 65): "F5/IMP-007 plane mislabel",
    ("fable-model-quantum/qmac.py", 107): "F5/IMP-060 charge-memory docstring",
    ("fable-model-quantum/qerrors.py", 34): "F5/IMP-065 (0.25 THz slot in the same docstring)",
    ("fable-model-quantum/qerrors.py", 35): "F5/IMP-065 charge-memory docstring",
    ("fable-model-quantum/qerrors.py", 36): "F5/IMP-065 charge-memory docstring",
    ("fable-model-quantum/make_manuscript.py", 202): "F5/IMP-007",
    ("fable-model-quantum/make_manuscript.py", 299): "F5/IMP-007",
    ("fable-model-quantum/make_manuscript.py", 456): "F7 dead generator",
    ("fable-model-quantum/make_manuscript.py", 491): "F7 dead generator",
    ("fable-model-quantum/make_manuscript.py", 548): "F5/IMP-007",
    ("fable-model-quantum/make_manuscript.py", 558): "F7 dead generator",
    ("fable-model-quantum/make_manuscript.py", 605): "F5/IMP-007",
    ("fable-model-quantum/make_manuscript.py", 760): "F5/IMP-007",
    ("fable-model-quantum/qmode.py", 17): "F5/IMP-007",
    ("fable-model-quantum/qmode.py", 97): "F5/IMP-007",
    ("fable-model-quantum/figures.py", 39): "F5/IMP-007",
    ("fable-model-quantum/README.md", 25): "F5/IMP-007",
    ("fable-model-quantum/README.md", 36): "F5/IMP-007",
    ("fable-model-quantum/README.md", 48): "F5/IMP-005 avg16 bullet",
    ("fable-model-chain/cell.py", 44): "F5/IMP-007",
    ("fable-model-chain/regen.py", 13): "clean: names the driven-cavity 1/(1-loop) enhancement",
    ("fable-model-chain/solver.py", 20): "F5/IMP-015 phantom scheme",
    ("fable-model-chain/solver.py", 65): "clean: solver.run's cav observable",
    ("fable-model-chain/solver.py", 99): "clean: solver.run's cav observable",
    ("fable-model-chain/figures.py", 28): "F6 shipped Figure 8 hardcodes M_th_num",
    ("fable-model-chain/figures.py", 160): "F6 shipped Figure 8 runs at 0.7*Mth_num",
    ("fable-model-chain/figures.py", 163): "F6 Figure 8 panel D label (0.25 THz train)",
    ("fable-model-chain/figures.py", 164): "F6 Figure 8 caption 'M_th,num ~ 0.17'",
    ("fable-model-chain/figures.py", 165): "F6 Figure 8 caption 'M_th,num ~ 0.17'",
    ("fable-model-chain/README.md", 45): "F5/IMP-059",
    ("fable-model-chain/README.md", 46): "F5/IMP-063",
    ("README.md", 28): "F2/IMP-057 front-page slot rate",
    ("README.md", 30): "F2/IMP-062 unqualified knee/rail",
    ("README.md", 40): "F1/IMP-041 stale version",
    ("README.md", 41): "F1/IMP-041 stale version",
    ("README.md", 45): "F1/IMP-058 stale version + false erratum",
    ("CITATION.cff", 26): "F1/IMP-040", ("CITATION.cff", 34): "F1/IMP-040",
    ("CITATION.cff", 47): "F1/IMP-040",
    ("agents/README.md", 126): "F1/IMP-041 (v5.2/v1.2)",
    ("agents/README.md", 127): "F1/IMP-041 (v5.2/v1.2)",
    ("agents/personas/fabric.md", 11): "F8/IMP-067 persona carries retired framing",
    ("agents/personas/quanta.md", 10): "F8/IMP-067 persona carries retired framing",
    ("ROADMAP.md", 17): "F5/IMP-059 second target",
    ("papers/Fable-Computer-Part-I.pdf", 0): "F2/F3 + Part I deltas (IMP-001/002/008/009/013/014)",
    ("papers/Fable-Computer-Part-I.docx", 0): "F2/F3 + Part I deltas (docx twin)",
    ("papers/Fable-Computer-Part-II.pdf", 0): "F2/F4 + Part II deltas (IMP-004/010/011/012)",
    ("papers/Fable-Computer-Part-II.docx", 0): "F2/F4 + Part II deltas (docx twin)",
    ("fable-model-chain/README.md", 44): "F5/IMP-059 (the claim spans 44-45)",
    ("fable-model-quantum/README.md", 49): "F5/IMP-005 (the bullet spans 48-50)",
    ("README.md", 34): "clean: Figure 8 caption describes the figure's content; the figure is F6",
    ("docs/Fable-Computer-Introduction.pdf", 0): "F9 public on-ramp: retired claims + stale versions",
    ("docs/Fable-Computer-Introduction.docx", 0): "F9 public on-ramp: retired claims + stale versions",
    ("docs/Fable-Computer-Community-Guidelines.pdf", 0): "F9 stale versions",
    ("docs/Fable-Computer-Community-Guidelines.docx", 0): "F9 stale versions",
}
EXEMPT_DIRS = ("notes",)          # the record itself: quoting retired claims is its job
SKIP_DIRS = (".git", "__pycache__", "figures", ".pytest_cache")
SKIP_FILES = ("ledger_listing.py", "ledger_sweep.py")
EXT = (".md", ".py", ".cff", ".json", ".yml", ".yaml", ".txt", ".pdf", ".docx")


def text_of(p: pathlib.Path):
    """Return (lines, kind). Binary formats collapse to one pseudo-line 0."""
    if p.suffix == ".pdf":
        try:
            from pypdf import PdfReader
            t = "\n".join((pg.extract_text() or "") for pg in PdfReader(str(p)).pages)
            return [re.sub(r"\s+", " ", re.sub(r"-\s*\n\s*", "", t))], "pdf"
        except Exception as e:
            return None, f"unreadable ({type(e).__name__})"
    if p.suffix == ".docx":
        try:
            with zipfile.ZipFile(p) as z:
                xml = z.read("word/document.xml").decode("utf-8", "replace")
            return [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", xml))], "docx"
        except Exception as e:
            return None, f"unreadable ({type(e).__name__})"
    return p.read_text(encoding="utf-8", errors="replace").split("\n"), "text"


files, undisposed, exempt_hits, unreadable = [], [], 0, []
for f in sorted(pathlib.Path(".").rglob("*")):
    if not f.is_file() or f.suffix not in EXT:
        continue
    parts = f.parts
    if any(d in parts for d in SKIP_DIRS) or f.name in SKIP_FILES:
        continue
    p = f.as_posix()
    lines, kind = text_of(f)
    if lines is None:
        unreadable.append(f"{p} [{kind}]"); continue
    files.append(p)
    exempt = parts[0] in EXEMPT_DIRS
    for name, rx in SIGS.items():
        for i, l in enumerate(lines, 1):
            if not re.search(rx, l, re.I):
                continue
            if exempt:
                exempt_hits += 1
                continue
            ln = 0 if kind in ("pdf", "docx") else i
            owner = DISPOSED.get((p, ln))
            if owner:
                print(f"  {p}:{ln:<4} [{name}] -> {owner}")
            else:
                undisposed.append(f"{p}:{ln} [{name}]")

print(f"\n  files read: {len(files)}   ({sum(1 for p in files if p.startswith('notes/'))} in notes/, exempt)")
print(f"  signature hits inside notes/ (exempt, the record itself): {exempt_hits}")
if unreadable:
    print("  UNREADABLE (declared, not silently skipped):")
    for u in unreadable: print("   ", u)
print(f"\n  UNDISPOSED HITS: {len(undisposed)}")
for u in undisposed:
    print("   ***", u)
print("""
  What this instrument cannot do, stated so a zero is not over-read:
   - it certifies only that every occurrence of these 8 signatures in the file
     set above has a named owner; it does NOT certify the owner is correct;
   - signature classes the record has produced but that have no textual tell -
     numeric bands, code behaviour, link integrity, missing keys, absent files -
     are invisible to it (they are found by reading, and most entries are of
     that kind);
   - binary formats are collapsed to one pseudo-line, so .pdf/.docx hits are
     file-level, not line-level;
   - notes/ is swept but exempt by construction.
  Falsify it by adding a signature, widening EXT, or shrinking the exemptions.""")
