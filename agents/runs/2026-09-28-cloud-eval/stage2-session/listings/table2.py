# -*- coding: utf-8 -*-
"""Table 2 — boundary-driven single cell at the MATCHED input amplitude.
For each (family, J): A* = kappa * mean-'1' drain-density peak of active cell 1 (the amplitude
cell 2 actually receives); run the single cell with the 07-31 duty-0.8 launch at amp = A*
(same PRBS, same bias, same grid), active and passive; report G_worst1 / G_mean1 (cav and drn_h).
"""
import sys, os, json, time
import numpy as np
from multiprocessing import Pool
SESSION = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SESSION)
from cascade_driver import *
OUT = os.path.join(SESSION, "table2.jsonl")


def job(cfg):
    t0 = time.time()
    m, N, seed, amp, bias = cfg["m"], cfg["N"], cfg["seed"], cfg["amp"], cfg["bias"]
    repT = 2.0 * m; nslots = 40; nrt = nslots * m
    bits = default_bits(nslots, seed)
    sig = make_sig_duty(bits, repT, F0N, amp, duty=0.8, edge_rt=2.0)
    cM = run_cell(bias, N, nrt, source_clamp(sig)); c0 = run_cell(0.0, N, nrt, source_clamp(sig))
    mM = slot_windows(cM["t"], repT, nslots); m0 = slot_windows(c0["t"], repT, nslots)
    res = dict(cfg)
    for obs in ("cav", "drn_h"):
        res[obs] = metrics(bits, slot_peaks(cM[obs], mM), slot_peaks(c0[obs], m0))
    res["secs"] = round(time.time() - t0, 1)
    return res


if __name__ == "__main__":
    cfgs = json.load(open(sys.argv[1])); nproc = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    with open(OUT, "a") as f, Pool(nproc) as pool:
        for r in pool.imap_unordered(job, cfgs):
            f.write(json.dumps(r) + "\n"); f.flush()
            print({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items() if k in ("tag", "J", "amp", "secs")}, r["cav"]["G_worst1_dB"], r["cav"]["G_mean1_dB"], flush=True)
    print("TABLE2 DONE", flush=True)
