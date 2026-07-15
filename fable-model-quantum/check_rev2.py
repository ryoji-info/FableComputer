# -*- coding: utf-8 -*-
import math, json
from math import comb
import qmac, qdecode, qnoise as Q

def parts(T, N_op=400):
    states, xr = qmac.levels_at_decision(T, N_op)
    V_slot = max(s.V for s in states.values()) + qdecode.decoder_amp_noise(T)
    V_stat = qdecode.threshold_band_variance(xr)
    lv = [states[(0,0)].x, 0.5*(states[(0,1)].x + states[(1,0)].x), states[(1,1)].x]
    return lv, V_slot, V_stat, xr

print("=== counterfactuals: vote9, vote12, everything/16 ===")
for T in (353, 300, 150, 77, 20):
    lv, Vs, Vk, xr = parts(T)
    p1 = Q.symbol_error(lv, [.25,.5,.25], Vs+Vk)
    v9  = sum(comb(16,i)*p1**i*(1-p1)**(16-i) for i in range(9,17))
    v12 = sum(comb(16,i)*p1**i*(1-p1)**(16-i) for i in range(12,17))
    e16 = Q.symbol_error(lv, [.25,.5,.25], (Vs+Vk)/16)
    print(f"T={T:4d}  p1={p1:.5f}  vote9={v9:.3e}  vote12={v12:.3e}  all/16={e16:.3e}")

# crossover T where V_static = V_slot/16
print("\n=== crossover where Vstat = Vslot/16 ===")
import numpy as np
for T in np.arange(45,60,0.1):
    lv, Vs, Vk, xr = parts(float(T))
    if Vs/16 <= Vk:
        print(f"crossover near T={T:.1f}  Vslot/16={Vs/16:.4f} vs Vstat={Vk:.4f}")
        break

# k=8 degradation at 300K
print("\n=== k=8 degradation at 300 K ===")
lv, Vs, Vk, xr = parts(300)
V16_k16 = Vs/16 + (xr/16)**2/12
V16_k8  = Vs/16 + (xr/8)**2/12
e16 = Q.symbol_error(lv,[.25,.5,.25],V16_k16)
e8  = Q.symbol_error(lv,[.25,.5,.25],V16_k8)
print(f"k16 avg16={e16:.3e}  k8 avg16={e8:.3e}  ratio={e8/e16:.1f}")

# enob at 300K
print("\n=== enob ===")
print(f"analog_enob(300)={qmac.analog_enob(300):.3f}")

# results.json presence
print("\n=== results.json spot check ===")
d = json.load(open("results.json"))
def find(o,key,path=""):
    if isinstance(o,dict):
        for k,v in o.items():
            if k==key: print(f"  {path}/{k} = {v}")
            find(v,key,path+"/"+k)
    elif isinstance(o,list):
        for i,v in enumerate(o): find(v,key,path+f"[{i}]")
find(d,"q2bit_avg16")
