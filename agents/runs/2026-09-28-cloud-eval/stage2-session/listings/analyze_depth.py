# -*- coding: utf-8 -*-
"""Table 3 from the depth re-run: per-stage gain over the passive twin chain, stage-cell
gain on its real input, '0'-floors (peak cav / peak drn_h / slot-mode drn_h), '1' pp, eye and
latency, under the window rule shift_k = (k-1)*L with L from the passive twin chain
(envelope cross-correlation), plus the unshifted and active-lag variants as sensitivities."""
import sys, os, json, math, glob
import numpy as np
SESSION = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SESSION)
from cascade_driver import metrics, floor_mode, slot_windows, slot_peaks, slot_modes, F0N, RT_PS
from analyze import envelope_lag
D = os.path.join(SESSION, "depth")


def load(tag, st):
    t = np.load(f"{D}/{tag}_{st}_t.npy").astype(float)
    return {"t": t, **{o: np.load(f"{D}/{tag}_{st}_{o}.npy").astype(float) for o in ("cav", "drn_h", "drn_u")}}


def score(cell, ref, bits, repT, nslots, shift):
    mk = slot_windows(cell["t"], repT, nslots, shift=shift); mr = slot_windows(ref["t"], repT, nslots, shift=shift)
    out = {o: metrics(bits, slot_peaks(cell[o], mk), slot_peaks(ref[o], mr)) for o in ("cav", "drn_h")}
    a, _ = slot_modes(cell["drn_h"], cell["t"], mk, F0N, repT, 0.8, shift=shift)
    out["floor_mode_drn_h"] = floor_mode(bits, a)
    return out


def run(tag):
    meta = json.load(open(f"{D}/{tag}.json")); bits = meta["bits"]; repT = meta["repT"]; ns = meta["nslots"]
    c1M, c10 = load(tag, "st1_M"), load(tag, "st1_0")
    stages = sorted({int(f.split("_st")[1].split("_")[0]) for f in glob.glob(f"{D}/{tag}_st*_MM_t.npy")})
    st2_00 = load(tag, "st2_00"); st2_MM = load(tag, "st2_MM")
    ds = max(1, len(c10["t"]) // 20000)
    L_pas = envelope_lag(c10["drn_h"][::ds], st2_00["drn_h"][::ds], c10["t"][::ds])
    L_act = envelope_lag(c1M["drn_h"][::ds], st2_MM["drn_h"][::ds], c1M["t"][::ds])
    res = {"tag": tag, "L_passive": L_pas, "L_active": L_act, "stages": {}}
    print(f"=== {tag}: L_passive {L_pas:.3f} units ({L_pas/2:.3f} rt, {L_pas/2*RT_PS:.3f} ps, {L_pas/repT:.3f} slot); L_active {L_act:.3f}")
    s1 = score(c1M, c10, bits, repT, ns, 0.0)
    print(f" stage 1: G_worst {s1['cav']['G_worst1_dB']:.3f} G_mean {s1['cav']['G_mean1_dB']:.3f} floor cav {s1['cav']['max0_below_mean1_dB']:.3f} drn_h {s1['drn_h']['max0_below_mean1_dB']:.3f} mode {s1['floor_mode_drn_h']:.3f} pp {s1['cav']['pp_raw_dB']:.3f} eye {s1['cav']['eye_dB']:+.2f}")
    res["stages"][1] = {"rule": s1}
    for k in stages:
        MM, M0, O0 = load(tag, f"st{k}_MM"), load(tag, f"st{k}_M0"), load(tag, f"st{k}_00")
        ent = {}
        for name, sh in (("rule", (k - 1) * L_pas), ("unshifted", 0.0), ("active_lag", (k - 1) * L_act)):
            sh = min(sh, 0.9 * repT - 0.72 * repT)   # keep the window inside the slot
            g = score(MM, O0, bits, repT, ns, sh); c = score(MM, M0, bits, repT, ns, sh)
            ent[name] = {"shift": sh, "chain_over_passive": g, "cell_on_real_input": c}
        res["stages"][k] = ent
        g = ent["rule"]["chain_over_passive"]; c = ent["rule"]["cell_on_real_input"]
        print(f" stage {k} (shift {ent['rule']['shift']:.2f}): chain/passive worst {g['cav']['G_worst1_dB']:.3f} mean {g['cav']['G_mean1_dB']:.3f} | stage-cell worst {c['cav']['G_worst1_dB']:.3f} mean {c['cav']['G_mean1_dB']:.3f} | floor cav {g['cav']['max0_below_mean1_dB']:.3f} drn_h {g['drn_h']['max0_below_mean1_dB']:.3f} mode {g['floor_mode_drn_h']:.3f} pp {g['cav']['pp_raw_dB']:.3f} eye {g['cav']['eye_dB']:+.2f} | mean1 drn_h {g['drn_h']['mean1_level']:.4f}")
        u = ent["unshifted"]["chain_over_passive"]; a = ent["active_lag"]["chain_over_passive"]
        print(f"          unshifted: worst {u['cav']['G_worst1_dB']:.3f} floor cav {u['cav']['max0_below_mean1_dB']:.3f} eye {u['cav']['eye_dB']:+.2f} | active-lag (shift {ent['active_lag']['shift']:.2f}): worst {a['cav']['G_worst1_dB']:.3f} floor cav {a['cav']['max0_below_mean1_dB']:.3f} eye {a['cav']['eye_dB']:+.2f}")
    return res


if __name__ == "__main__":
    tags = sorted({os.path.basename(p)[:-5] for p in glob.glob(f"{D}/*.json")})
    out = {t: run(t) for t in tags}
    json.dump(out, open(os.path.join(SESSION, "analysis_depth.json"), "w"), indent=1)
