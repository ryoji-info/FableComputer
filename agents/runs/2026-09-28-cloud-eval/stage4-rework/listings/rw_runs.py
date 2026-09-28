# -*- coding: utf-8 -*-
"""Round-2 re-executions that need new solver runs (m = 30, N = 240, seed 7, ratio bias, J = -1 unless stated):
  (A) cfl sensitivity (Kinetic R5/T4, R8/T7): cell 1 active/passive and the J = -1 chain (MM, M0, 00) at cfl 0.2 and 0.8,
      bias held at the released-convention 0.7*M_th_num(240) (measured at cfl 0.4) -- Kinetic's construction;
  (B) J = -25 chain at cfl 0.4 (MM, 00) for the window-placement scan (Quanta R1);
  (C) the gated-input ablation (Quanta T8): cell 2 driven by cell 1's output with (i) the '0'-slot residue zeroed by a
      1-rt raised-cosine cut at each '0'-slot start, (ii) additionally everything after 0.8*repT of each '1' slot removed.
Full-resolution series saved as float32 .npy under rework/series/."""
import sys, os, json, time, math
import numpy as np
from multiprocessing import Pool
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, S)
from cascade_driver import *
OUT = os.path.join(S, "rework", "series"); os.makedirs(OUT, exist_ok=True)
m, N, seed = 30, 240, 7
BIAS = 0.7 * json.load(open(os.path.join(S, "mth_num.json")))["240"]
repT = 2.0 * m; nslots = 40; nrt = nslots * m
bits = default_bits(nslots, seed)
sig = make_sig_duty(bits, repT, F0N, 2e-3, duty=0.8, edge_rt=2.0)


def save(tag, cell):
    np.save(f"{OUT}/{tag}_t.npy", cell["t"].astype(np.float32))
    for obs in ("cav", "drn_h", "drn_u"):
        np.save(f"{OUT}/{tag}_{obs}.npy", cell[obs].astype(np.float32))
    json.dump({"dt": cell["dt"], "n": len(cell["t"])}, open(f"{OUT}/{tag}.json", "w"))


def load(tag):
    return {"t": np.load(f"{OUT}/{tag}_t.npy").astype(float), **{o: np.load(f"{OUT}/{tag}_{o}.npy").astype(float) for o in ("cav", "drn_h", "drn_u")},
            "dt": json.load(open(f"{OUT}/{tag}.json"))["dt"]}


def gate_series(up, kind):
    """Return a copy of `up` with drn_h multiplied by the ablation gate."""
    t = up["t"]; g = np.ones_like(t); cut = 2.0  # 1 rt = 2 time units
    for k in range(nslots):
        x0 = k * repT
        if bits[k] == 0:
            # raised-cosine fall over the first 1 rt of the '0' slot, then zero
            sel = (t >= x0) & (t < x0 + cut); g[sel] = 0.5 * (1 + np.cos(np.pi * (t[sel] - x0) / cut))
            g[(t >= x0 + cut) & (t < x0 + repT)] = 0.0
        elif kind == "duty":
            x1 = x0 + 0.8 * repT
            sel = (t >= x1) & (t < x1 + cut); g[sel] = 0.5 * (1 + np.cos(np.pi * (t[sel] - x1) / cut))
            g[(t >= x1 + cut) & (t < x0 + repT)] = 0.0
    out = dict(up); out["drn_h"] = up["drn_h"] * g; return out


def stageA(job):
    tag, M, cfl = job; t0 = time.time()
    c = run_cell(M, N, nrt, source_clamp(sig), cfl=cfl); save(tag, c)
    return tag, time.time() - t0, c["dt"], len(c["t"])


def stageB(job):
    tag, M, cfl, uptag, kappa, gate = job; t0 = time.time()
    up = load(uptag)
    if gate: up = gate_series(up, gate)
    _, c2 = run_chain(None, M, N, nrt, sig, kappa=kappa, plane="h", cfl=cfl, up=up); save(tag, c2)
    return tag, time.time() - t0, c2["dt"], len(c2["t"])


if __name__ == "__main__":
    k1 = 10 ** (-1 / 20.0); k25 = 10 ** (-25 / 20.0)
    A = [(f"c1M_cfl{c}", BIAS, c) for c in (0.2, 0.4, 0.8)] + [(f"c10_cfl{c}", 0.0, c) for c in (0.2, 0.4, 0.8)]
    B = []
    for c in (0.2, 0.4, 0.8):
        B += [(f"J1_MM_cfl{c}", BIAS, c, f"c1M_cfl{c}", k1, None), (f"J1_M0_cfl{c}", 0.0, c, f"c1M_cfl{c}", k1, None), (f"J1_00_cfl{c}", 0.0, c, f"c10_cfl{c}", k1, None)]
    B += [("J25_MM_cfl0.4", BIAS, 0.4, "c1M_cfl0.4", k25, None), ("J25_00_cfl0.4", 0.0, 0.4, "c10_cfl0.4", k25, None),
          ("J1_MM_abl_zero_cfl0.4", BIAS, 0.4, "c1M_cfl0.4", k1, "zero"), ("J1_MM_abl_duty_cfl0.4", BIAS, 0.4, "c1M_cfl0.4", k1, "duty")]
    with Pool(4) as pool:
        for r in pool.imap_unordered(stageA, A): print("A", r, flush=True)
    with Pool(4) as pool:
        for r in pool.imap_unordered(stageB, B): print("B", r, flush=True)
    print("RUNS DONE", platform_line(), flush=True)
