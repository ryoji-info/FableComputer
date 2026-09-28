# -*- coding: utf-8 -*-
"""The '0'-slot residue the next cell receives, from the depth re-run's stored cell-1 series
(active drain density h[-1]-1; m = 30 and 28, N = 240, seed 7). Two denominators, both named
wherever a number is quoted:
  (a) the mean-'1' peak inside the PROMOTED window [0.25, 0.72]·repT (the promoted floor
      key's own denominator, so the ratio is comparable with max0_below_mean1_dB);
  (b) the mean-'1' peak inside the SAME sub-window (same phase of the slot).
'0' slots are split into those that follow a '1' (carrying its ring-down) and those that
follow a '0'. Also the '0'-slot energy over the mean '1'-slot energy (whole slot)."""
import numpy as np, json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "depth")
WINDOWS = ((0.25, 0.72, "promoted window"), (0.0, 0.25, "first quarter"), (0.0, 1.0, "whole slot"))


def compute(tag):
    meta = json.load(open(f"{D}/{tag}.json")); bits = np.array(meta["bits"]); repT = meta["repT"]; ns = meta["nslots"]
    t = np.load(f"{D}/{tag}_st1_M_t.npy").astype(float); x = np.load(f"{D}/{tag}_st1_M_drn_h.npy").astype(float)

    def pk(lo, hi):
        return np.array([np.max(np.abs(x[(t >= (k + lo) * repT) & (t < (k + hi) * repT)])) for k in range(ns)])[4:]
    b = bits[4:]; ones = b == 1; zeros = b == 0; prev1 = np.array([bits[k - 1] == 1 for k in range(4, ns)])
    ref_a = float(np.mean(pk(0.25, 0.72)[ones]))
    out = {"tag": tag, "mean1_windowed_peak_a": ref_a, "windows": {}}
    for lo, hi, lbl in WINDOWS:
        p = pk(lo, hi); ref_b = float(np.mean(p[ones]))
        a1 = float(np.max(p[zeros & prev1])); a0 = float(np.max(p[zeros & ~prev1]))
        out["windows"][lbl] = {"lo": lo, "hi": hi, "mean1_same_window_b": ref_b, "after1_peak": a1, "after0_peak": a0,
                               "after1_over_a_dB": 20 * np.log10(a1 / ref_a), "after1_over_b_dB": 20 * np.log10(a1 / ref_b),
                               "after0_over_a_dB": 20 * np.log10(a0 / ref_a), "after0_over_b_dB": 20 * np.log10(a0 / ref_b)}
    e = np.array([np.sum(x[(t >= k * repT) & (t < (k + 1) * repT)] ** 2) for k in range(ns)])[4:]
    out["energy_max_dB"] = float(10 * np.log10(np.max(e[zeros]) / np.mean(e[ones]))); out["energy_median_dB"] = float(10 * np.log10(np.median(e[zeros]) / np.mean(e[ones])))
    return out


if __name__ == "__main__":
    for tag in ("D_N240_m30_s7", "D_N240_m28_s7"):
        r = compute(tag); print(f"{tag}: (a) mean-'1' windowed peak {r['mean1_windowed_peak_a']:.6f}")
        for lbl, w in r["windows"].items():
            print(f"  {lbl:16s} [{w['lo']:.2f}, {w['hi']:.2f}]·repT: '0' after '1' peak {w['after1_peak']:.6f} -> over (a) {w['after1_over_a_dB']:7.2f} dB, over (b) same-window mean-'1' {w['mean1_same_window_b']:.6f}: {w['after1_over_b_dB']:7.2f} dB | '0' after '0': over (a) {w['after0_over_a_dB']:7.2f}, over (b) {w['after0_over_b_dB']:7.2f}")
        print(f"  '0'-slot energy over mean '1'-slot energy: max {r['energy_max_dB']:.2f} dB, median {r['energy_median_dB']:.2f} dB")
