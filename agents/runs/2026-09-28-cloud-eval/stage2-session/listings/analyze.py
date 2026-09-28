# -*- coding: utf-8 -*-
"""Score the cascade campaign under ONE window rule fixed before scoring.

Window rule (stated, applied identically to active and passive chains): stage k's
scoring window is the promoted [0.25, 0.72]*repT window delayed by (k-1)*L, where L is
the passive-chain stage latency measured ONCE per family from the passive twin chain
(J = -1, density plane, stage 2 vs cell 1) as the lag maximising the cross-correlation
of the |drn_h| envelopes, rounded to the stored 1/8-rt shift grid. The unshifted
(L = 0) reading is reported beside it as the sensitivity.
"""
import json, os, sys, math, glob
import numpy as np
SESSION = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SESSION)
from cascade_driver import metrics, floor_mode, RT_PS
RUNS = os.path.join(SESSION, "runs")
STRICT = 20 * math.log10(0.25641458774368575)   # -11.8211 dB
ROUND = -10.0


def idx(shifts, s):
    return int(np.argmin(np.abs(np.asarray(shifts) - s)))


def envelope_lag(a, b, t):
    """Lag (time units) maximising the cross-correlation of |a| and |b| envelopes (moving
    mean over ~one carrier period), b delayed relative to a. Positive = b lags a."""
    dt = t[1] - t[0]
    w = max(1, int(round(4.0 / dt)))          # one carrier period = 4 time units
    k = np.ones(w) / w
    ea = np.convolve(np.abs(a), k, mode="same"); eb = np.convolve(np.abs(b), k, mode="same")
    ea = ea - ea.mean(); eb = eb - eb.mean()
    nmax = int(round(12.0 / dt))              # search up to 6 rt
    best, bl = -np.inf, 0
    for lag in range(0, nmax):
        c = np.dot(ea[:len(ea) - lag], eb[lag:]) if lag else np.dot(ea, eb)
        if c > best: best, bl = c, lag
    return bl * dt


def peaktime_lag(bits, tp1, tp2, drop=4):
    b = np.asarray(bits[drop:]); d = np.asarray(tp2[drop:]) - np.asarray(tp1[drop:])
    return float(np.median(d[b == 1]))


def stage_scores(bits, upstream_pk, chain, ref, shift_idx, key_obs="cav"):
    """gain of `chain` over `ref` at the given shift index, for obs cav and drn_h, plus
    floors in both denominations, pp, eye (all on `chain`)."""
    out = {}
    for obs in ("cav", "drn_h"):
        r = metrics(bits, np.array(chain["pk_" + obs][shift_idx]), np.array(ref["pk_" + obs][shift_idx]))
        out[obs] = r
    out["floor_mode_drn_h"] = floor_mode(bits, np.array(chain["mode_drn_h"][shift_idx]))
    return out


def analyze_family(path):
    F = json.load(open(path)); cfg = F["cfg"]; bits = F["bits"]; shifts = F["cell1"]["M"]["shifts"]
    repT = F["repT"]; m = cfg["m"]; N = cfg["N"]; seed = cfg["seed"]; Jp = cfg.get("primary_J", -1)
    c1M, c10 = F["cell1"]["M"], F["cell1"]["0"]
    R = {"tag": cfg["tag"], "m": m, "N": N, "seed": seed, "bias": F["bias"], "repT": repT, "secs": F.get("secs")}
    # --- cell 1 (the promoted single-cell rows) ---
    R["cell1"] = {obs: metrics(bits, np.array(c1M["pk_" + obs][0]), np.array(c10["pk_" + obs][0])) for obs in ("cav", "drn_h")}
    R["cell1"]["floor_mode_drn_h"] = floor_mode(bits, np.array(c1M["mode_drn_h"][0]))
    # --- latency from the passive twin chain (rule) and the active chain (reported) ---
    p00 = F["chains"][f"J{Jp}_h_00"]; pMM = F["chains"][f"J{Jp}_h_MM"]
    t = np.array(c10["ds_t"])
    L_env_pas = envelope_lag(np.array(c10["ds_drn_h"]), np.array(p00["ds_drn_h"]), t)
    L_env_act = envelope_lag(np.array(c1M["ds_drn_h"]), np.array(pMM["ds_drn_h"]), np.array(c1M["ds_t"]))
    L_pk_pas = peaktime_lag(bits, c10["tpeak_drn_h"], p00["tpeak_drn_h"])
    L_pk_act = peaktime_lag(bits, c1M["tpeak_drn_h"], pMM["tpeak_drn_h"])
    L_rule = shifts[idx(shifts, L_env_pas)]
    R["latency"] = {"env_passive": L_env_pas, "env_active": L_env_act, "peak_passive": L_pk_pas, "peak_active": L_pk_act,
                    "rule_shift": L_rule, "rule_rt": L_rule / 2.0, "rule_ps": L_rule / 2.0 * RT_PS, "rule_frac_slot": L_rule / repT}
    s2 = idx(shifts, L_rule); s0 = 0
    # --- per junction class ---
    R["J"] = {}
    for key in F["chains"]:
        if not key.endswith("_MM") or "stage" in key: continue
        base = key[:-3]                         # e.g. J-1_h
        J = int(base.split("_")[0][1:]); plane = base.split("_")[1]
        MM = F["chains"][base + "_MM"]; M0 = F["chains"][base + "_M0"]; O0 = F["chains"][base + "_00"]
        kappa = 10 ** (J / 20.0)
        ent = {}
        for sname, si in (("rule", s2), ("unshifted", s0)):
            g_chain = stage_scores(bits, None, MM, O0, si)      # definition A: over the passive twin chain
            g_c2c = stage_scores(bits, None, MM, M0, si)        # cell-to-cell: cell 2 active vs passive on its real input
            g_up = stage_scores(bits, None, M0, O0, si)         # cell-1 gain as seen through a passive cell 2
            # absolute (port-to-port) definition B, drain density vs the 2e-3 launch amplitude
            amp = cfg.get("amp", 2e-3)
            def mean1(ch, obs, s):
                pk = np.array(ch["pk_" + obs][s]); b = np.asarray(bits[4:len(pk)]); return float(np.mean(pk[4:][b == 1]))
            T2_pas = 20 * math.log10(mean1(O0, "drn_h", si) / (kappa * mean1(c10, "drn_h", 0)))
            G1_abs = 20 * math.log10(mean1(c1M, "drn_h", 0) / amp)
            Gc_abs = 20 * math.log10(mean1(MM, "drn_h", si) / amp)
            T1_pas = 20 * math.log10(mean1(c10, "drn_h", 0) / amp)
            ent[sname] = {"chain_over_passive": g_chain, "cell2_on_real_input": g_c2c, "cell1_through_passive2": g_up,
                          "passive_transfer_stage2_dB": T2_pas, "passive_transfer_stage1_dB": T1_pas,
                          "G1_abs_dB": G1_abs, "Gchain_abs_dB": Gc_abs,
                          "G4_A_worst": g_chain["cav"]["G_worst1_dB"] / R["cell1"]["cav"]["G_worst1_dB"],
                          "G4_A_mean": g_chain["cav"]["G_mean1_dB"] / R["cell1"]["cav"]["G_mean1_dB"],
                          "G4_A_drnh_worst": g_chain["drn_h"]["G_worst1_dB"] / R["cell1"]["drn_h"]["G_worst1_dB"],
                          "G4_B_mean": Gc_abs / G1_abs,
                          "mean1_in_cell2": kappa * mean1(c1M, "drn_h", 0)}
        R["J"][f"{J}_{plane}"] = ent
    # --- depth extension ---
    R["depth"] = []
    for stage in range(2, 10):
        kMM = f"J{Jp}_h_MM" if stage == 2 else f"J{Jp}_h_stage{stage}_MM"
        if kMM not in F["chains"]: break
        kM0 = kMM.replace("_MM", "_M0"); k00 = kMM.replace("_MM", "_00")
        si = idx(shifts, min(shifts[-1], (stage - 1) * L_rule))
        MM, M0, O0 = F["chains"][kMM], F["chains"][kM0], F["chains"][k00]
        R["depth"].append({"stage": stage, "shift": shifts[si], "chain_over_passive": stage_scores(bits, None, MM, O0, si),
                           "cell_on_real_input": stage_scores(bits, None, MM, M0, si)})
    return R


def fmt(x, n=3):
    return "nan" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x:.{n}f}"


if __name__ == "__main__":
    files = sorted(glob.glob(os.path.join(RUNS, "*.json")))
    out = {}
    for p in files:
        R = analyze_family(p); out[R["tag"]] = R
        c = R["cell1"]["cav"]; L = R["latency"]
        print(f"\n=== {R['tag']}  m={R['m']} N={R['N']} seed={R['seed']} bias={R['bias']:.6f}  [{R['secs']}s]")
        print(f" cell1 cav: G_worst {c['G_worst1_dB']:.4f} G_mean {c['G_mean1_dB']:.4f} pp {c['pp_raw_dB']:.3f} eye {c['eye_dB']:+.2f} floor {c['max0_below_mean1_dB']:.4f} | drn_h floor {R['cell1']['drn_h']['max0_below_mean1_dB']:.4f} mode-floor {R['cell1']['floor_mode_drn_h']:.3f}")
        print(f" latency: env passive {L['env_passive']:.3f} / active {L['env_active']:.3f}; peak passive {L['peak_passive']:.3f} / active {L['peak_active']:.3f} -> rule shift {L['rule_shift']} units = {L['rule_rt']:.3f} rt = {L['rule_ps']:.3f} ps = {L['rule_frac_slot']:.3f} slot")
        for Jk, ent in sorted(R["J"].items(), key=lambda kv: (kv[0].split('_')[1], -int(kv[0].split('_')[0]))):
            e = ent["rule"]; ch = e["chain_over_passive"]; cc = e["cell2_on_real_input"]
            print(f"  J{Jk:>5}: chain/passive cav worst {ch['cav']['G_worst1_dB']:.3f} mean {ch['cav']['G_mean1_dB']:.3f} | G4_A worst {e['G4_A_worst']:.3f} mean {e['G4_A_mean']:.3f} (drn_h {e['G4_A_drnh_worst']:.3f}) G4_B {e['G4_B_mean']:.3f} | c2c cav worst {cc['cav']['G_worst1_dB']:.3f} mean {cc['cav']['G_mean1_dB']:.3f} | in-amp {e['mean1_in_cell2']:.5f} T2pas {e['passive_transfer_stage2_dB']:.2f} T1pas {e['passive_transfer_stage1_dB']:.2f} | st2 floor cav {ch['cav']['max0_below_mean1_dB']:.3f} drn_h {ch['drn_h']['max0_below_mean1_dB']:.3f} mode {ch['floor_mode_drn_h']:.3f} pp {ch['cav']['pp_raw_dB']:.3f} eye {ch['cav']['eye_dB']:+.2f}")
            u = ent["unshifted"]["chain_over_passive"]
            print(f"          unshifted: chain/passive cav worst {u['cav']['G_worst1_dB']:.3f} mean {u['cav']['G_mean1_dB']:.3f} floor cav {u['cav']['max0_below_mean1_dB']:.3f}")
        for d in R["depth"]:
            ch = d["chain_over_passive"]; cc = d["cell_on_real_input"]
            print(f"  stage {d['stage']} (shift {d['shift']}): chain/passive cav worst {ch['cav']['G_worst1_dB']:.3f} mean {ch['cav']['G_mean1_dB']:.3f} | stage-cell c2c worst {cc['cav']['G_worst1_dB']:.3f} mean {cc['cav']['G_mean1_dB']:.3f} | floor cav {ch['cav']['max0_below_mean1_dB']:.3f} drn_h {ch['drn_h']['max0_below_mean1_dB']:.3f} mode {ch['floor_mode_drn_h']:.3f} pp {ch['cav']['pp_raw_dB']:.3f} eye {ch['cav']['eye_dB']:+.2f}")
    json.dump(out, open(os.path.join(SESSION, "analysis.json"), "w"), indent=1)
