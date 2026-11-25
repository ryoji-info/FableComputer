# -*- coding: utf-8 -*-
"""Run chain4.py from a script: start(ncell) loads the runner for layouts of ncell pairs, run(SET, tag) runs a
list of settings into a batch and returns (m, arrays) as analysis.load() does.

chain4.py reads its job arguments and builds its layouts when it is imported, so one process serves one
number of pairs.  The progress lines of the runner are not printed (quiet=True), so that a listing prints
the same text on every run.
"""
import json
import os
import sys
import tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
_state = {}


def start(ncell, out=None, quiet=True, **jobargs):
    """Import the runner for layouts of ncell pairs.  out: folder for the batch files (default: a new
    temporary folder).  jobargs: further job arguments of runs3.py (backend, dt, seed, pseed, ...)."""
    if "C4" in _state:
        if _state["ncell"] != ncell:
            raise RuntimeError("this process already runs layouts of %d pairs" % _state["ncell"])
        return _state["C4"]
    if out is None:                                           # a temporary folder, removed when the process ends
        out = tempfile.mkdtemp(prefix="parametron_")
        import atexit
        import shutil
        atexit.register(shutil.rmtree, out, True)
    argv = ["chain4.py", "chain", "ncell=%d" % ncell, "out=%s" % out] + ["%s=%s" % kv for kv in jobargs.items()]
    saved = sys.argv
    sys.argv = argv
    try:
        import runs3 as R
        import chain4 as C4
    finally:
        sys.argv = saved
    if quiet:
        R.LOG = C4.LOG = lambda *a: None
    _state.update(C4=C4, R=R, ncell=ncell, out=out)
    return C4


def run(SET, tag):
    """Run the settings SET (list of dicts) as batch <tag> in the output folder; returns (m, arrays)."""
    C4, R = _state["C4"], _state["R"]
    fn = tag + "_set.json"
    json.dump(SET, open(os.path.join(R.OUT, fn), "w"), indent=1)
    R.args["set"], R.args["tag"] = fn, tag
    for f in os.listdir(R.OUT):                               # a batch file that exists would be skipped: start afresh
        if f.startswith(tag + "_c") and f.endswith(".npz"):
            os.remove(os.path.join(R.OUT, f))
    C4.exp_chain()
    import analysis
    return analysis.load(R.OUT, tag)
