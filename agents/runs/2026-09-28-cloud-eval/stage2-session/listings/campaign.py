# -*- coding: utf-8 -*-
"""Fable Session 2026-09-28 — cascade campaign (families run in parallel).

One FAMILY = (m, N, seed): cell 1 active + passive (the promoted single-cell rows), then
cell 2 for every junction class J in dB (kappa = 10^(J/20)) in the three chains:
  MM : active cell 1 -> active cell 2      (the real cascade)
  M0 : active cell 1 -> passive cell 2     (cell 2's own reference on its real input)
  00 : passive cell 1 -> passive cell 2    (the passive twin chain, G4's reference)
plus the velocity-plane sensitivity at one J, and (primary family) a depth-4 extension.
Every run's per-slot peaks (cav, drn_h, drn_u) and drn_h slot-mode amplitudes are stored
for a grid of window shifts (0..2 rt in 0.125-rt steps), so the per-stage window rule is
fixed BEFORE scoring and applied identically to active and passive chains.
"""
import sys, os, json, time, math
import numpy as np
from multiprocessing import Pool
SESSION = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SESSION)
from cascade_driver import *

SHIFTS = np.arange(0.0, 8.01, 0.25)        # time units (0..4 rt); 0.25 = 1/8 rt
OUTDIR = os.path.join(SESSION, "runs")
os.makedirs(OUTDIR, exist_ok=True)


def score_all(cell, repT, nslots, f0n, duty=0.8):
    """Per-slot peaks / slot-mode amplitudes for every window shift, computed one shift at a
    time so the boolean masks are never all resident (the earlier version held
    33 shifts x 40 slots x nsteps booleans and was OOM-killed at N = 720)."""
    t = cell["t"]
    out = {"shifts": SHIFTS.tolist(), "nsteps": int(len(t)), "dt": float(cell["dt"]), "M": float(cell["M"])}
    for obs in ("cav", "drn_h", "drn_u"):
        out["pk_" + obs] = []
    out["mode_drn_h"] = []; out["phase_drn_h"] = []
    for sh in SHIFTS:
        mk = slot_windows(t, repT, nslots, shift=float(sh))
        for obs in ("cav", "drn_h", "drn_u"):
            out["pk_" + obs].append(slot_peaks(cell[obs], mk).tolist())
        a, p = slot_modes(cell["drn_h"], t, mk, f0n, repT, duty, shift=float(sh))
        out["mode_drn_h"].append(a.tolist()); out["phase_drn_h"].append(p.tolist())
        del mk
    tp = []
    for k in range(nslots):
        mk = (t >= k * repT) & (t < (k + 1) * repT)
        if mk.sum() > 3:
            i = int(np.argmax(np.abs(cell["drn_h"][mk]))); tp.append(float(t[mk][i] - k * repT))
        else:
            tp.append(float("nan"))
    out["tpeak_drn_h"] = tp
    step = max(1, len(t) // 20000)
    out["ds_step"] = step
    out["ds_t"] = t[::step].tolist(); out["ds_drn_h"] = cell["drn_h"][::step].tolist()
    return out


def family(cfg):
    t0 = time.time()
    m, N, seed = cfg["m"], cfg["N"], cfg["seed"]
    bias = 0.7 * cfg["mth_num"]
    amp = cfg.get("amp", 2e-3)
    Js = cfg.get("Js", [0, -1, -3, -6])
    repT = 2.0 * m; nslots = cfg.get("nslots", 40); nrt = nslots * m
    bits = default_bits(nslots, seed)
    sig = make_sig_duty(bits, repT, F0N, amp, duty=0.8, edge_rt=2.0)
    log = []
    def note(s):
        log.append(f"[{time.time()-t0:7.0f}s] {s}"); print(f"{cfg['tag']} {log[-1]}", flush=True)
    c1M = run_cell(bias, N, nrt, source_clamp(sig)); note("cell1 active done")
    c10 = run_cell(0.0, N, nrt, source_clamp(sig)); note("cell1 passive done")
    res = {"cfg": cfg, "bias": bias, "bits": bits.tolist(), "repT": repT, "nslots": nslots,
           "cell1": {"M": score_all(c1M, repT, nslots, F0N), "0": score_all(c10, repT, nslots, F0N)},
           "chains": {}}
    keep = {}
    for J in Js:
        kappa = 10 ** (J / 20.0)
        for label, M2, up in (("MM", bias, c1M), ("M0", 0.0, c1M), ("00", 0.0, c10)):
            _, c2 = run_chain(None, M2, N, nrt, sig, kappa=kappa, plane="h", up=up)
            key = f"J{J}_h_{label}"
            res["chains"][key] = score_all(c2, repT, nslots, F0N)
            if J == cfg.get("primary_J", -1):
                keep[label] = c2
            else:
                del c2
            note(f"{key} done")
    # velocity-plane sensitivity at the primary J (optional)
    Jp = cfg.get("primary_J", -1); kappa = 10 ** (Jp / 20.0)
    for label, M2, up in ((("MM", bias, c1M), ("M0", 0.0, c1M), ("00", 0.0, c10)) if cfg.get("plane_u", True) else ()):
        _, c2 = run_chain(None, M2, N, nrt, sig, kappa=kappa, plane="u", up=up)
        res["chains"][f"J{Jp}_u_{label}"] = score_all(c2, repT, nslots, F0N); note(f"J{Jp}_u_{label} done")
    # depth extension on the primary J, density plane: stages 3..depth
    depth = cfg.get("depth", 2)
    if depth > 2 and keep:
        actM = keep["MM"]; pas0 = keep["00"]
        for stage in range(3, depth + 1):
            _, nM = run_chain(None, bias, N, nrt, sig, kappa=kappa, plane="h", up=actM)      # active chain
            _, nMx = run_chain(None, 0.0, N, nrt, sig, kappa=kappa, plane="h", up=actM)      # passive stage on the active chain
            _, n0 = run_chain(None, 0.0, N, nrt, sig, kappa=kappa, plane="h", up=pas0)       # passive chain
            res["chains"][f"J{Jp}_h_stage{stage}_MM"] = score_all(nM, repT, nslots, F0N)
            res["chains"][f"J{Jp}_h_stage{stage}_M0"] = score_all(nMx, repT, nslots, F0N)
            res["chains"][f"J{Jp}_h_stage{stage}_00"] = score_all(n0, repT, nslots, F0N)
            actM, pas0 = nM, n0
            note(f"stage {stage} done")
    res["log"] = log; res["secs"] = round(time.time() - t0, 1); res["platform"] = platform_line()
    with open(os.path.join(OUTDIR, cfg["tag"] + ".json"), "w") as f:
        json.dump(res, f)
    return cfg["tag"], res["secs"]


if __name__ == "__main__":
    cfgs = json.load(open(sys.argv[1]))
    nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    print(f"{len(cfgs)} families, {nproc} workers, platform {platform_line()}", flush=True)
    with Pool(nproc) as pool:
        for tag, secs in pool.imap_unordered(family, cfgs):
            print(f"DONE {tag} in {secs:.0f}s", flush=True)
    print("ALL DONE", flush=True)
