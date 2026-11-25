# -*- coding: utf-8 -*-
"""check_identity: the packaged runner against the runner as it ran.

The folder identity/ holds three settings and the arrays that the session's own code (chain4.py, runs3.py and
fdtd3.py with the older design modules they imported) wrote for them with the numpy backend, on the computer
on which this package was made:
  id29   the first setting of batch chain_g29: a row of 16 at the operating point, no noise, no spread
  id30   the first setting of batch chain_g30: the serial adder on two rails (20 pairs), no noise, no spread
  id29n  the same row with 2 runs of physical noise, every spread of the model at once (inductance 3 %, diode
         current 5 %, difference inside a pair 2 %, pump phase 10 degrees per pair and per clock phase, pump
         level 10 %, link strength 10 %, clock timing 2 %, supply level 1 %, damping resistor 5 %) and the link
         capacitors cc = 0.02, so that every noise and spread generator and the capacitor path are used
This script runs the packaged chain4.py on the same settings (numpy backend, default job arguments, which are
those of the batches) and compares every stored array bit for bit.  On another computer the last bits of
floating-point results may differ; the script then prints the largest difference.
Run time on the reference computer: about 3 minutes.
usage: python check_identity.py
"""
import os
import shutil
import subprocess
import sys
import tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import numpy as np

CASES = (("id29", 16), ("id30", 20), ("id29n", 16))
out = tempfile.mkdtemp(prefix="parametron_id_")
allsame = True
try:
    for tag, ncell in CASES:
        shutil.copy(os.path.join(HERE, "identity", tag + "_set.json"), out)
        subprocess.run([sys.executable, "-X", "utf8", "-I", "-B", os.path.join(HERE, "chain4.py"), "chain", "out=" + out, "set=%s_set.json" % tag,
                        "tag=" + tag, "ncell=%d" % ncell], check=True, stdout=subprocess.DEVNULL)
        with np.load(os.path.join(HERE, "identity", tag + "_c000.npz")) as f_:
            a = {k: f_[k] for k in f_.files}
        with np.load(os.path.join(out, tag + "_c000.npz")) as f_:
            b = {k: f_[k] for k in f_.files}
        print("%s (%d pairs, %d runs):" % (tag, ncell, len(a["tags"])))
        for k in sorted(a):
            x, y = a[k], b[k]
            same = x.dtype == y.dtype and x.shape == y.shape and x.tobytes() == y.tobytes()
            allsame &= same
            dif = 0.0 if same or x.dtype == bool else float(np.abs(x.astype(np.float64) - y.astype(np.float64)).max())
            print("   %-4s %-8s %-12s bitwise equal: %s%s" % (k, x.dtype, str(x.shape), "yes" if same else "no", "" if same else ", largest difference %.3g" % dif))
finally:
    shutil.rmtree(out, True)
print("every array bitwise equal: %s" % ("yes" if allsame else "no"))
