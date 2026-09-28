# -*- coding: utf-8 -*-
"""Depth re-run for the primary families with FULL-resolution series kept (float32 .npy),
so any per-stage window rule can be applied after the fact. J = -1 (kappa = 10^(-1/20)),
density plane, stages 2..DEPTH: MM (active chain), M0 (passive stage on the active chain),
00 (passive twin chain)."""
import sys, os, json, time
import numpy as np
from multiprocessing import Pool
SESSION = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SESSION)
from cascade_driver import *
OUT = os.path.join(SESSION, "depth"); os.makedirs(OUT, exist_ok=True)


def save(tag, cell):
    np.save(os.path.join(OUT, tag + "_t.npy"), cell["t"].astype(np.float32))
    for obs in ("cav", "drn_h", "drn_u"):
        np.save(os.path.join(OUT, f"{tag}_{obs}.npy"), cell[obs].astype(np.float32))


def job(cfg):
    t0 = time.time()
    m, N, seed, depth = cfg["m"], cfg["N"], cfg["seed"], cfg["depth"]
    bias = 0.7 * cfg["mth_num"]; kappa = 10 ** (-1 / 20.0)
    repT = 2.0 * m; nslots = 40; nrt = nslots * m
    bits = default_bits(nslots, seed)
    sig = make_sig_duty(bits, repT, F0N, 2e-3, duty=0.8, edge_rt=2.0)
    tag = cfg["tag"]
    c1M = run_cell(bias, N, nrt, source_clamp(sig)); save(f"{tag}_st1_M", c1M)
    c10 = run_cell(0.0, N, nrt, source_clamp(sig)); save(f"{tag}_st1_0", c10)
    actM, pas0 = c1M, c10
    for stage in range(2, depth + 1):
        _, nM = run_chain(None, bias, N, nrt, sig, kappa=kappa, plane="h", up=actM)
        _, nMx = run_chain(None, 0.0, N, nrt, sig, kappa=kappa, plane="h", up=actM)
        _, n0 = run_chain(None, 0.0, N, nrt, sig, kappa=kappa, plane="h", up=pas0)
        save(f"{tag}_st{stage}_MM", nM); save(f"{tag}_st{stage}_M0", nMx); save(f"{tag}_st{stage}_00", n0)
        actM, pas0 = nM, n0
        print(f"{tag} stage {stage} done [{time.time()-t0:.0f}s]", flush=True)
    json.dump({"cfg": cfg, "bias": bias, "bits": bits.tolist(), "repT": repT, "nslots": nslots, "dtM": c1M["dt"], "dt0": c10["dt"],
               "secs": time.time() - t0, "platform": platform_line()}, open(os.path.join(OUT, tag + ".json"), "w"))
    return tag


if __name__ == "__main__":
    cfgs = json.load(open(sys.argv[1]))
    with Pool(int(sys.argv[2]) if len(sys.argv) > 2 else 2) as pool:
        for tag in pool.imap_unordered(job, cfgs):
            print("DONE", tag, flush=True)
    print("DEPTH DONE", flush=True)
