# -*- coding: utf-8 -*-
"""Check of a run without noise or spread against the expected bits, pair by pair, at the moment that matters:
when the next pairs take their decision (the first full 1-ps window after the next clock phase has come on; the
arrays LE and PE of chain4.py).  A pair is right when, on its own axis, every defined slot (slot 0 left out) has
the expected sign.  The older check of an_chain3.py reads the last window of a pair's on-time instead; in a gate
with several links the phase at that late moment is pulled by the pairs it drives, although every pair that
copies it has long decided.
    early_ref(d, m, si) -> right [pair] (bool), margin [pair] (smallest projection over mean level), level [pair] (mV)"""
import numpy as np


def early_ref(d, m, si, run=None):
    s = m["SET"][si]
    tp = m["topo"][s["topo"]]
    ex = np.array(m["expect"][s["topo"]])
    ns, n = ex.shape
    ok = ex >= 0
    ok[0] = False
    e = np.where(ok, 2.0 * ex - 1.0, 0.0)
    ir = np.where((d["tags"] == si) & d["ref"])[0][0] if run is None else run
    dep = np.array(tp["depth"], float)
    fd = s.get("fd", 0) or m["f_ref"]
    t0 = (np.arange(ns)[:, None] + 1.0 + dep[None, :] / 4.0) * s["T"]
    te = np.ceil(t0 + 0.25 * s["T"] + 1.0) + 0.5                       # middle of the window that chain4 reads
    rot = np.exp(-2j * np.pi * (fd - m["f_ref"]) * te)
    L = d["LE"][ir, :ns]
    z = L * np.exp(1j * d["PE"][ir, :ns]) * rot
    ax = (e * z).sum(0)
    pr = np.real(z * np.conj(ax)[None, :]) / np.maximum(np.abs(ax), 1e-12)[None, :] * e
    right = np.array([bool((pr[ok[:, k], k] > 0).all()) if ok[:, k].any() else True for k in range(n)])
    level = np.array([float(1e3 * L[ok[:, k], k].mean()) if ok[:, k].any() else 0.0 for k in range(n)])
    lowest = np.array([float(1e3 * L[ok[:, k], k].min()) if ok[:, k].any() else 0.0 for k in range(n)])
    margin = np.array([float(pr[ok[:, k], k].min() / max(L[ok[:, k], k].mean(), 1e-12)) if ok[:, k].any() else 1.0 for k in range(n)])
    return right, margin, level, lowest
