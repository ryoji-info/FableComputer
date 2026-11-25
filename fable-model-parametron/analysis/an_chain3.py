# -*- coding: utf-8 -*-
"""Rows of pairs: read every run of a batch and count wrong decisions. Writes chain_<tag>_summary.json.

The reading, in plain words.
  - A slot is one clock cycle. Slot 0 follows a cycle without data and is left out of every count.
  - The run without noise or spread of a setting is its reference run.
  - Phase keying (mode "psk", every batch of the paper). A decision of a pair in a slot is the phasor of the last
    full 1-ps window of its on-time. It is counted wrong when it points more than 90 degrees away from the phasor
    of the reference run in the same slot and pair ("err_ref"). It is also counted wrong, separately, when it has
    the wrong sign on the pair's own axis, which is the sum of the phasors of that run with the expected signs
    ("err_own"; this reading does not see a turn that is common to all slots).
  - The phase at the moment the next pair decides (arrays PE) gives "dev_early_deg" (rms phase error against the
    reference run) and "err_early" (share of wrong decisions) per pair. The tables of the paper use these.
  - The reference run itself is checked against the expected bits on its own axis ("ref_ok"). "margin" is its
    smallest projected level over its mean level.
  - On/off keying (mode "ook", older batches only): the level of the last window against one threshold per pair,
    the best one.
  - Also per setting: the frequency of the last pair in the reference run, from the phase step between its last
    two windows ("f_last"), and the mean supply power ("P_mW").
The code is that of the session script of the same name. Only its input and output changed: the index may be
gzip-compressed and the output folder can be chosen (see common.py).
usage: python an_chain3.py <tag> [<array folder>] [out=<folder>] [-v]"""
import json
import math
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True                  # no __pycache__ folder inside the package
from common import args, load_json, load_npz

TAG, D, OUT = args(sys.argv)
VERB = "-v" in sys.argv
m = load_json(TAG + ".json", OUT, D)
SET = m["SET"]
EXP = {t: np.array(v) for t, v in m["expect"].items()}
F_REF = m["f_ref"]
NC = int(m.get("ncell", 8))
SKIP = 1                                                  # slots left out of every count: the first slot follows a cycle without data
res = [None] * len(SET)
for ci in range(len(m["chunks"])):
    fn = os.path.join(D, "%s_c%03d.npz" % (TAG, ci))
    if not os.path.exists(fn):
        continue
    d = load_npz(fn)                                     # read every array once
    tg, rf = d["tags"], d["ref"]
    for si in m["chunks"][ci]:
        s = SET[si]
        ex = EXP[s["topo"]]
        ns = ex.shape[0]
        e = 2.0 * ex - 1.0                                   # [slot, pair]
        sl = slice(SKIP, ns)
        ir = np.where((tg == si) & rf)[0][0]
        iN = np.where((tg == si) & ~rf)[0]
        LLr, PHr = d["LL"][ir, sl], d["PH"][ir, sl]
        e, ex = e[sl], ex[sl]
        fd = s.get("fd", 0) or F_REF                       # the reader runs at F_REF: take out the turn a tone at fd makes from slot to slot
        dep = np.array(m["topo"][s["topo"]]["depth"], float) if "topo" in m and s["topo"] in m["topo"] else np.zeros(NC)
        t0 = (np.arange(ns)[:, None] + 1.0 + dep[None, :NC] / 4.0) * s["T"]          # start of each pair's on-time in each slot
        wl = np.floor(t0 + s.get("duty", 0.65) * s["T"] - 2.0) + 0.5                  # middle of the last full 1-ps window that is read
        rot = np.exp(-2j * np.pi * (fd - F_REF) * wl)[sl]                            # [slot, pair]: the windows sit on a 1-ps grid
        zr = LLr * np.exp(1j * PHr) * rot
        out = dict(si=si, N=len(iN), P_mW=float(d["P"][ir]), level_mV=[float(1e3 * LLr[:, k].mean()) for k in range(NC)])
        dph = np.angle(np.exp(1j * (d["PH"][ir, sl, NC - 1] - d["PH2"][ir, sl, NC - 1]))) if "PH2" in d else np.zeros(ns)
        out["f_last"] = float(F_REF + np.median(dph) / (2 * math.pi))
        z = d["LL"][iN, sl] * np.exp(1j * d["PH"][iN, sl]) * rot[None]    # [run, slot, pair]
        if "PE" in d:                                        # phase when the next pair takes its decision
            ce = np.exp(1j * (d["PE"][iN, sl] - d["PE"][ir, sl][None]))
            out["dev_early_deg"] = [float(np.degrees(np.sqrt(np.mean(np.angle(ce[:, :, k]) ** 2)))) for k in range(NC)]
            out["err_early"] = [float((np.real(ce[:, :, k]) < 0).mean()) for k in range(NC)]
        if s["mode"] == "psk":
            ax = (e * zr).sum(0)
            pr = np.real(zr * np.conj(ax)[None, :]) / np.maximum(np.abs(ax), 1e-12)[None, :] * e
            out["ref_ok"] = [bool((pr[:, k] > 0).all()) for k in range(NC)]
            out["margin"] = [float(pr[:, k].min() / max(LLr[:, k].mean(), 1e-12)) for k in range(NC)]
            if len(iN):
                c = z * np.conj(zr)[None]
                out["err_ref"] = [float((np.real(c[:, :, k]) < 0).mean()) for k in range(NC)]
                axn = (e[None] * z).sum(1)                    # [run, pair]
                po = np.real(z * np.conj(axn)[:, None, :]) * e[None]
                out["err_own"] = [float((po[:, :, k] < 0).mean()) for k in range(NC)]
                dev = np.angle(c)
                out["dev_deg"] = [float(np.degrees(np.sqrt(np.mean(dev[:, :, k] ** 2)))) for k in range(NC)]
                out["drop"] = [float((np.abs(z[:, :, k]) < 0.5 * np.abs(zr[None, :, k])).mean()) for k in range(NC)]
                out["n_dec"] = int(len(iN) * (ns - SKIP))
        else:
            ones, zeros = ex > 0, ex == 0
            out["ref_ok"] = [bool(LLr[ones[:, k], k].min() > 2.0 * max(LLr[zeros[:, k], k].max(), 1e-4)) if zeros[:, k].any() and ones[:, k].any() else False for k in range(NC)]
            out["margin"] = [float((LLr[ones[:, k], k].min() - LLr[zeros[:, k], k].max()) / max(LLr[ones[:, k], k].mean(), 1e-12)) if zeros[:, k].any() and ones[:, k].any() else 0.0 for k in range(NC)]
            if len(iN):
                a = d["LL"][iN, sl]
                er, mi, fa = [], [], []
                for k in range(NC):
                    hi, lo = a[:, ones[:, k], k].ravel(), a[:, zeros[:, k], k].ravel()
                    if len(hi) == 0 or len(lo) == 0:
                        er.append(float("nan")); mi.append(float("nan")); fa.append(float("nan"))
                        continue
                    ths = np.linspace(0.005, 0.12, 116)
                    tot = np.array([((hi < t).sum() + (lo >= t).sum()) / (len(hi) + len(lo)) for t in ths])
                    j = int(np.argmin(tot))
                    er.append(float(tot[j])); mi.append(float((hi < ths[j]).mean())); fa.append(float((lo >= ths[j]).mean()))
                out["err_ref"], out["miss"], out["false"] = er, mi, fa
                out["err_own"] = er
                out["n_dec"] = int(len(iN) * (ns - SKIP))
        res[si] = out
with open(os.path.join(OUT, TAG + "_summary.json"), "w") as f_:
    json.dump(dict(SET=SET, res=res), f_, indent=1)

keys = ("design", "fx", "topo", "T", "duty", "cc", "mode", "scale", "fano", "jsig", "jpair", "lsig", "pump", "pph", "pstep", "fd")
print("%d settings, %d analysed" % (len(SET), sum(r is not None for r in res)))
hdr = "design     fx    topo   T    mode scale  jsig jpair lsig pump pph pstep |  P mW  f THz | ref ok  margin | wrong per pair (reference decode), pairs 0..7                    | rms phase dev (deg)"
print(hdr)
for si, s in enumerate(SET):
    r = res[si]
    if r is None:
        continue
    ok = "".join("y" if x else "n" for x in r["ref_ok"])
    mg = min(r["margin"][1:]) if s["topo"] != "adder" else min(r["margin"][3:])
    if not s.get("Is", 0.4):
        continue                                             # runs without input have no reference phase
    show = list(range(NC)) if NC <= 8 else [0, 1, 2, 3] + list(range(5, NC, 4))
    er = " ".join("%7.1e" % r["err_ref"][k] for k in show) if "err_ref" in r else ""
    dv = " ".join("%3.0f" % r["dev_deg"][k] for k in show) if "dev_deg" in r else ""
    if "dev_early_deg" in r:
        dv += " | early " + " ".join("%3.0f" % r["dev_early_deg"][k] for k in show)
    if VERB:
        print("%-9s %.3f %-5s %4.1f %-4s %5.1f %5.3f %5.3f %5.3f %4.2f %4.2f %4.2f | %5.2f %.4f | %s %5.2f | %s | %s" %
              (s["design"], s["fx"], s["topo"], s["T"], s["mode"], s["scale"], s["jsig"], s["jpair"], s["lsig"], s["pump"], s.get("pph", 0), s.get("pstep", 0), r["P_mW"], r["f_last"], ok, mg, er, dv))
