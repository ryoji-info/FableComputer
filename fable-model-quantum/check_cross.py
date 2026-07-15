# -*- coding: utf-8 -*-
import numpy as np, qmac, qdecode
def sh(T):
    states, xr = qmac.levels_at_decision(float(T), 400)
    Vs = max(s.V for s in states.values()) + qdecode.decoder_amp_noise(float(T))
    Vk = qdecode.threshold_band_variance(xr)
    return Vk/(Vs/16+Vk), Vs/16, Vk
# scan downward from 77 to 48 for share crossing 50%
prev=None
for T in np.arange(48,78,0.05):
    s,_,_=sh(T)
    if prev is not None and (prev-0.5)*(s-0.5)<=0:
        print(f"share=50% crossing near T={T:.2f}  share={s:.4f}")
    prev=s
for T in (52.0,52.3,52.5):
    s,a,b=sh(T); print(f"T={T}: share={100*s:.2f}%  Vslot/16={a:.4f}  Vstat={b:.4f}")
