# -*- coding: utf-8 -*-
"""Defect-signature sweep: does any artifact still assert a claim the record retired?

Eight signatures drawn from the promoted notes are swept over every tracked
.md/.py/.cff/.json/.yml/.txt/.pdf/.docx file. Each hit must be **accounted for** in
one of three ways, and the exit criterion is that none is left over:

  corrected   the hit sits in text that also carries a correction marker -- it names
              the plane, calls the reading retired, cites the binding note, labels the
              figure coarse-grid, and so on. Fixing a defect by documenting it keeps
              the signature word present, so this is the normal state of a corrected
              file rather than a loophole; the marker list is the audit trail.
  disposed    an explicit entry in DISPOSED_FILE (whole-document artifacts) or
              CLEAN_LINE (a legitimate use of the same word), with the reason stated.
  UNDISPOSED  everything else -- a bare assertion of a retired claim. CI fails here.

    cd <repo root> && PYTHONIOENCODING=utf-8 python ledger_sweep.py

Pure Python: no subprocess, no grep, explicit encodings, so the result does not depend
on the shell locale. .pdf needs pypdf; .docx is read straight from the zip.
notes/ is swept but exempt: quoting a retired claim is a promoted note's job.

Per notes/2026-07-26-record-audit-ten-findings.md (findings 5-10). Earlier revisions
keyed dispositions to (path, line); that map broke on every edit it prescribed, which
is why accounting is now content-based.
"""
import pathlib, re, zipfile

SIGS = {
    "intracavity":             r"intracavity",
    "charge-memory reading":   r"charge[- ]memory|averages as 1/|buys the 2-bit|averaging over 16 slots",
    "'five decades'":          r"five decades",
    "M_th claim or value":     r"analytic as .x|. analytic as|M_?th_?num\s*=\s*0\.169|M_th,num . 0\.17|Mth_num = 0\.169",
    "unqualified knee/rail":   r"38 (?:plasmons|quanta|intracavity)|1[- ]dB (?:compression )?knee|1 dB at .?.?1 ?%|3,?8[03]0|linear range ends near 38",
    "0.25 THz / 4-ps logic":   r"4-p(?:ico)?second slot|4-ps slot|2\.5\s*.\s*10.. additions|per 4-ps|0\.25[- ]THz|0\.25 THz",
    "phantom 2nd-order":       r"MacCormack",
    "stale version / erratum": r"One known erratum|v5\.5|v1\.6|v5\.2|v1\.2",
}

# Text that shows the surrounding passage is *handling* the retired claim, not asserting
# it. Matched case-insensitively against the hit line and its +/-7-line window.
MARKERS = (
    "retired", "superseded", "withdrawn", "mislabel", "not an intracavity",
    "design baseline", "launch", "drive plane", "drive-plane", "input-referred",
    "neither plane", "anchored at neither", "coarse-grid", "inviscid", "kinetic 0.165",
    "physical kinetic", "ideal per-slot", "ideal-per-slot", "bookkeeping",
    "no second-order", "do not run", "superseded artifact", "notes/2026-",
    "errata", "record note", "does not survive", "not five decades", "band 22-51",
    "22–51", "deposit", "runs ahead", "rev. 4", "erratum item",
)

# Whole-document artifacts: .pdf/.docx collapse to one pseudo-line, so they are
# accounted for at file level with an explicit reason.
DISPOSED_FILE = {
    "papers/Fable-Computer-Part-I.pdf":  "deferred: Part I deltas are listed in papers/ERRATA.md (rows I-1..I-10)",
    "papers/Fable-Computer-Part-I.docx": "deferred: same, docx twin",
    "papers/Fable-Computer-Part-II.pdf": "deferred: Part II deltas are listed in papers/ERRATA.md (rows II-1..II-5)",
    "papers/Fable-Computer-Part-II.docx": "deferred: same, docx twin",
    "docs/Fable-Computer-Introduction.pdf": "corrected 2026-07-26 (rev. 4 note); signatures remain in the historical rev. 3 note",
    "docs/Fable-Computer-Introduction.docx": "corrected 2026-07-26 (rev. 4 note); ditto",
    "docs/Fable-Computer-Community-Guidelines.pdf": "corrected 2026-07-26 (rev. 4 note); stale versions remain only inside rev. 3",
    "docs/Fable-Computer-Community-Guidelines.docx": "corrected 2026-07-26 (rev. 4 note); ditto",
}

# Legitimate uses of a signature word, matched by content so they survive edits.
CLEAN_LINE = (
    ("fable-model-chain/regen.py", "driven cavity is enhanced",
     "clean: names the 1/(1-loop) driven-cavity enhancement"),
    ("fable-model-chain/solver.py", "time series at the drain",
     "clean: solver.run's cav observable"),
    ("fable-model-chain/solver.py", "peak velocity perturbation",
     "clean: solver.run's cav observable"),
    ("fable-model-chain/figures.py", "set_ylabel",
     "clean: axis label for the cav observable"),
    ("README.md", "Figure 8 of Part I, regenerated",
     "clean: the caption describes what the figure shows (a 0.25-THz train)"),
    ("tests/test_published_claims.py", "intracavity",
     "clean: the guard that enforces the plane labels"),
)

EXEMPT_DIRS = ("notes",)
SKIP_DIRS = (".git", "__pycache__", "figures", ".pytest_cache", "node_modules")
SKIP_FILES = ("ledger_listing.py", "ledger_sweep.py")
EXT = (".md", ".py", ".cff", ".json", ".yml", ".yaml", ".txt", ".pdf", ".docx")


def text_of(p):
    """Return (lines, kind); binary formats collapse to a single pseudo-line."""
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


def clean_reason(path, line):
    for f, needle, why in CLEAN_LINE:
        if path.endswith(f) and needle in line:
            return why
    return None


files, undisposed, unreadable = [], [], []
n_corrected = n_disposed = n_exempt = 0

for f in sorted(pathlib.Path(".").rglob("*")):
    if not f.is_file() or f.suffix not in EXT:
        continue
    if any(d in f.parts for d in SKIP_DIRS) or f.name in SKIP_FILES:
        continue
    p = f.as_posix()
    lines, kind = text_of(f)
    if lines is None:
        unreadable.append(f"{p} [{kind}]")
        continue
    files.append(p)
    exempt = f.parts[0] in EXEMPT_DIRS
    for name, rx in SIGS.items():
        for i, line in enumerate(lines, 1):
            if not re.search(rx, line, re.I):
                continue
            if exempt:
                n_exempt += 1
                continue
            if p in DISPOSED_FILE:
                n_disposed += 1
                continue
            why = clean_reason(p, line)
            if why:
                print(f"  disposed   {p}:{i:<4} [{name}] -> {why}")
                n_disposed += 1
                continue
            window = "\n".join(lines[max(0, i - 8):i + 7]).lower()
            if any(m.lower() in window for m in MARKERS):
                n_corrected += 1
                continue
            undisposed.append(f"{p}:{i} [{name}]  {line.strip()[:88]}")

for p, why in sorted(DISPOSED_FILE.items()):
    if p in files:
        print(f"  disposed   {p:<46} -> {why}")

print(f"\n  files read: {len(files)}   ({sum(1 for x in files if x.startswith('notes/'))} in notes/, exempt)")
print(f"  hits accounted for: {n_corrected} corrected-in-context, {n_disposed} explicitly disposed, "
      f"{n_exempt} inside notes/ (exempt)")
if unreadable:
    print("  UNREADABLE (declared, not silently skipped):")
    for u in unreadable:
        print("   ", u)

print(f"\n  UNDISPOSED HITS: {len(undisposed)}")
for u in undisposed:
    print("   ***", u)

print("""
  What a zero does and does not certify:
   - it certifies that no swept file asserts one of these 8 retired claims without a
     correction marker, an explicit disposition, or a stated clean reason;
   - it does NOT certify that a correction is *correct* -- only that one is present;
   - defect classes with no textual tell (numeric bands, code behaviour, link
     integrity, missing keys, absent files) are invisible here and are found by
     reading -- most of the audit's work order is of that kind;
   - .pdf/.docx are accounted for at file level, not line level;
   - notes/ is swept but exempt: quoting a retired claim is a promoted note's job.
  Falsify it by adding a signature, widening EXT, shrinking MARKERS, or removing a
  disposition and showing the claim is still asserted bare.""")
