# -*- coding: utf-8 -*-
"""Round-2 re-executions from stored campaign data and the released loop model (no new solver runs)."""
import sys, os, json, math
import numpy as np
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, S)
sys.path.insert(0, "/home/user/FableComputer/fable-model-chain")
from cascade_driver import metrics, floor_mode
import regen, constants as C
A = json.load(open(S + "/analysis.json"))
def R(tag): return json.load(open(f"{S}/runs/{tag}.json"))
print("=== D2: is the drain velocity slaved to the drain density? (depth series, cell 1 active, cfl 0.4)")
for tag, M in (("D_N240_m30_s7", 0.11826023624361658), ("D_N240_m28_s7", 0.11826023624361658)):
    h = np.load(f"{S}/depth/{tag}_st1_M_drn_h.npy").astype(float); u = np.load(f"{S}/depth/{tag}_st1_M_drn_u.npy").astype(float)
    sl = float(np.dot(h, u) / np.dot(h, h)); resid = float(np.linalg.norm(u - sl * h) / np.linalg.norm(u))
    print(f" {tag}: LS slope du/dh = {sl:.5f}  (-M = {-M:.5f}); relative residual {resid:.3f}; |du|/|dh| rms ratio {np.sqrt(np.mean(u**2)/np.mean(h**2)):.5f}")
print("=== D2: passive and active drain-velocity mean-'1' (promoted window, shift 0), N = 240 vs 480, m = 30 seed 7")
for tag in ("N240_m30_s7", "N480_m30_s7", "N240_m28_s7", "N480_m28_s7"):
    F = R(tag); b = np.array(F["bits"])[4:]
    p0 = np.array(F["cell1"]["0"]["pk_drn_u"][0])[4:]; pM = np.array(F["cell1"]["M"]["pk_drn_u"][0])[4:]; ph = np.array(F["cell1"]["M"]["pk_drn_h"][0])[4:]
    v0 = np.mean(p0[b == 1]); vM = np.mean(pM[b == 1]); hM = np.mean(ph[b == 1]); k = 10 ** (-1 / 20)
    print(f" {tag}: passive drain-u mean-'1' {v0:.4e} ({20*math.log10(v0/2e-3):+.2f} dB over launch); active {vM:.5f} ({20*math.log10(vM/2e-3):+.2f} dB); active drain-h {hM:.5f}; cell-2 input at J=-1: density {k*hM:.5f} vs velocity {k*vM:.5f} -> gap {20*math.log10(hM/vM):.2f} dB; 20log10(1/M) = {20*math.log10(1/F['bias']):.2f}")
r240 = np.mean(np.array(R("N240_m30_s7")["cell1"]["0"]["pk_drn_u"][0])[4:][np.array(R("N240_m30_s7")["bits"])[4:] == 1]); r480 = np.mean(np.array(R("N480_m30_s7")["cell1"]["0"]["pk_drn_u"][0])[4:][np.array(R("N480_m30_s7")["bits"])[4:] == 1])
print(f" passive drain-u ratio N240/N480 = {r240/r480:.3f} (first order in dx -> 2)")
for tag in ("N240_m30_s7", "N480_m30_s7"):
    e = A[tag]["J"]["-1_u"]["rule"]; print(f" velocity plane G4_A ({tag}): worst {e['G4_A_worst']:.3f} mean {e['G4_A_mean']:.3f}; c2c worst {e['cell2_on_real_input']['cav']['G_worst1_dB']:.3f}; chain/passive worst {e['chain_over_passive']['cav']['G_worst1_dB']:.3f}")
print("=== D3: seed spread vs window rounding (chain worst-'1' cav gain over passive twin chain, G4_A = chain dB / single dB at promoted window)")
def chain_gain(F, key, sh_idx):
    b = F["bits"]; MM = F["chains"][key + "_MM"]; OO = F["chains"][key + "_00"]
    g = metrics(b, np.array(MM["pk_cav"][sh_idx]), np.array(OO["pk_cav"][sh_idx]))["G_worst1_dB"]
    s = metrics(b, np.array(F["cell1"]["M"]["pk_cav"][0]), np.array(F["cell1"]["0"]["pk_cav"][0]))["G_worst1_dB"]
    return g, s, g / s
for tag in ("N240_m30_s7", "N240_m30_s11", "N240_m30_s13", "N240_m28_s7", "N240_m28_s13", "N480_m30_s7", "N720_m30_s7", "N480_m28_s7"):
    try: F = R(tag)
    except FileNotFoundError: continue
    sh = F["cell1"]["M"]["shifts"]; i50 = sh.index(5.0); i525 = sh.index(5.25); rule = A[tag]["latency"]["rule_rt"]
    for J in ("J-1_h", "J-6_h"):
        if J + "_MM" not in F["chains"]: continue
        g1, s, r1 = chain_gain(F, J, i50); g2, _, r2 = chain_gain(F, J, i525)
        print(f" {tag} {J}: rule {rule} rt | at 2.5 rt: chain {g1:.3f} G4 {r1:.3f} | at 2.625 rt: chain {g2:.3f} G4 {r2:.3f} | delta {g2-g1:+.3f} dB, {r2-r1:+.3f} in G4 | single {s:.4f}")
print("=== D12: peak-vs-slot-mode floor gap by channel (cell 1, promoted window)")
for tag in ("N240_m30_s7", "N240_m28_s7"):
    c = A[tag]["cell1"]; print(f" {tag}: cav {c['cav']['max0_below_mean1_dB']:.4f} drn_h {c['drn_h']['max0_below_mean1_dB']:.4f} mode {c['floor_mode_drn_h']:.4f} -> cav-mode gap {c['cav']['max0_below_mean1_dB']-c['floor_mode_drn_h']:.2f}, drn_h-mode gap {c['drn_h']['max0_below_mean1_dB']-c['floor_mode_drn_h']:.2f}")
print("=== D7: latency arithmetic (m = 30, N = 240, passive cell)")
dt0 = 0.4 / 240 / 1.2; print(f" passive dt = {dt0:.6e} units; half-step = {dt0/2:.3e} units = {dt0/4:.3e} rt; dx per transit = {1/240:.4e} units = {1/480:.3e} rt; measured excess 0.0243 rt = {0.0486:.4f} units = {0.0486/dt0:.1f} steps")
print("=== D8: released loop model, loaded-drain illustration (in-model)")
s, tau, L, Mth, a_loss = regen._cavity()
Mb = 0.11826023624361658; loop_r = regen.loop_gain(Mb); loop_a = regen.loop_gain(0.7 * Mth)
print(f" a_loss {a_loss:.16f}; loop at ratio bias {loop_r:.4f}; at analytic 0.7*M_th {loop_a:.4f}; unloaded open-end buildup 2/(1-a_loss) = {2/(1-a_loss):.3f} = {20*math.log10(2/(1-a_loss)):+.2f} dB; 1/(1-a_loss) = {20*math.log10(1/(1-a_loss)):+.2f} dB")
for J in (0, -1, -3, -6):
    T = 10 ** (J / 10); r = math.sqrt(max(0.0, 1 - T)); t = math.sqrt(T)
    print(f" J={J:+d}: |t|^2={T:.3f} |r|={r:.3f}: loaded loop (ratio bias) {loop_r*r:.3f} / (analytic) {loop_a*r:.3f}; drive delivered |t|/(1-a_loss|r|) = {20*math.log10(t/(1-a_loss*r)):+.2f} dB; drain standing-wave density (1+|r|)/(1-a_loss|r|) = {20*math.log10((1+r)/(1-a_loss*r)):+.2f} dB; CW regen gain at ratio bias, loaded: {20*math.log10((1-regen.loop_gain(0.0)*r)/(1-loop_r*r)):+.2f} dB (unloaded {20*math.log10((1-regen.loop_gain(0.0))/(1-loop_r)):+.2f})")
print("=== D5: launch pin: 2e-3 / knee 0.01203 =", 2e-3 / 0.01203)
