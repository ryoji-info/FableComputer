"""Write plain-text extracts of the three Fable Computer papers for the assessment agents.

Run from anywhere inside the repository:  python inputs/extract_papers.py
Output: <run bundle>/work/papers_txt/Part-I.txt, Part-II.txt, Part-III.txt (work/ is git-ignored).
Uses the PDFs in papers/ (pypdf); falls back to the .docx (python-docx) if a PDF is missing.
"""
import os, sys, glob, re

here = os.path.dirname(os.path.abspath(__file__))
run_dir = os.path.dirname(here)
root = run_dir
while root and not os.path.isdir(os.path.join(root, 'papers')):
    parent = os.path.dirname(root)
    if parent == root:
        sys.exit('papers/ directory not found above ' + here)
    root = parent
out_dir = os.path.join(run_dir, 'work', 'papers_txt')
os.makedirs(out_dir, exist_ok=True)

def pdf_text(path):
    import pypdf
    r = pypdf.PdfReader(path)
    return '\n'.join((p.extract_text() or '') for p in r.pages)

def docx_text(path):
    import docx
    d = docx.Document(path)
    parts = [p.text for p in d.paragraphs]
    for t in d.tables:
        for row in t.rows:
            parts.append(' | '.join(c.text for c in row.cells))
    return '\n'.join(parts)

for part in ('I', 'II', 'III'):
    pdf = os.path.join(root, 'papers', 'Fable-Computer-Part-%s.pdf' % part)
    dx = os.path.join(root, 'papers', 'Fable-Computer-Part-%s.docx' % part)
    if os.path.exists(pdf):
        text, src = pdf_text(pdf), pdf
    elif os.path.exists(dx):
        text, src = docx_text(dx), dx
    else:
        cands = glob.glob(os.path.join(root, 'papers', '*Part-%s*' % part))
        sys.exit('no file for Part %s; candidates: %s' % (part, cands))
    text = text.replace('\x00', '')
    dst = os.path.join(out_dir, 'Part-%s.txt' % part)
    open(dst, 'w', encoding='utf-8').write(text)
    print('%s -> %s (%d chars, %d lines)' % (os.path.relpath(src, root), os.path.relpath(dst, root), len(text), text.count('\n') + 1))
