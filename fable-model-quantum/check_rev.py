# -*- coding: utf-8 -*-
import math
from math import comb
import qmac, qdecode, qnoise as Q

def parts(T, N_op=400):
    states, xr = qmac.levels_at_decision(T, N_op)
    V_slot = max(s.V for s in states.values()) + qdecode.decoder_amp_noise(T)
    V_stat = qdecode.threshold_band_variance(xr)
    lv = [states[(0,0)].x, 0.5*(states[(0,1)].x + states[(1,0)].x), states[(1,1)].x]
    return lv, V_slot, V_stat, xr

print("=== Table: V_slot, V_static, V_16, static share, avg16 ===")
for T in (353, 300, 150, 77, 48, 20, 4):
    lv, Vs, Vk, xr = parts(T)
    V16 = Vs/16 + Vk
    avg16 = Q.symbol_error(lv, [.25,.5,.25], V16)
    print(f"T={T:4d}  Vslot={Vs:8.4f}  Vstat={Vk:.4f}  V16={V16:.4f}  share={100*Vk/V16:5.1f}%  avg16={avg16:.6e}")

print("\n=== q2bit (n_avg=1) for reproduction check ===")
for T in (300, 353, 4):
    print(f"T={T}: q2bit_avg16={qmac.error_2bit(T, n_avg=16):.6e}")

print("\n=== 1.5 reconciliation: pre-loss vs post-loss band ===")
for T in (300, 4):
    states, xr_post = qmac.levels_at_decision(T, 400)
    xr_pre = 2*math.sqrt(400)
    Vpre = (xr_pre/16)**2/12
    Vpost = (xr_post/16)**2/12
    ratio = (xr_pre/xr_post)**2
    print(f"T={T}: xr_pre={xr_pre}  Vpre={Vpre:.4f} (N/768={400/768:.4f})  xr_post={xr_post:.4f}  Vpost={Vpost:.4f}  ratio={ratio:.3f}")

print("\n=== closed-form floor ===")
for k in (8, 16, 32):
    lv, Vs, _, xr = parts(300)
    xrl = lv[2]
    cf = 0.75*math.erfc(math.sqrt(3/8)*k)
    num = Q.symbol_error(lv, [.25,.5,.25], (xrl/k)**2/12)
    print(f"k={k}: closed={cf:.4e}  numeric={num:.4e}")
