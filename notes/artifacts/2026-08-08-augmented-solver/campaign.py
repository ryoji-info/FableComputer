# -*- coding: utf-8 -*-
"""Measurement campaign for the 2026-08-08 Fable session (augmented solver).
Regeneration run: deterministic (fixed seeds, fixed brackets), so this
reproduces the original 2026-08-08 archive bit-identically."""
import json
import os
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
_CHAIN = os.path.normpath(os.path.join(_HERE, '..', '..', '..', 'fable-model-chain'))
sys.path.insert(0, _CHAIN)   # lets augment.py's chain imports resolve repo-relatively
sys.path.insert(0, _HERE)    # lets `from augment import ...` resolve next to this file
from augment import (census, threshold, nu_num, partner_cfl, NU0, MTH353)

OUT = os.path.join(_HERE, 'campaign_results.json')
R = {}
CACHE = {}


def save():
    json.dump(R, open(OUT, 'w'), indent=1)


def tsec(t0):
    print(f"  [{time.time()-t0:.0f}s elapsed]", flush=True)


t0 = time.time()

# ---- Gate 3: cell A released census (must reproduce 0.1687658795) ----------
print("== GATE 3: cell A released census ==", flush=True)
R['A_rel'] = census(N=240, cfl=0.4, nu=0.0, start=2, cache=CACHE, label='A_rel')
save(); tsec(t0)

# ---- 07-22 confrontation, its own convention (seed 1, 90 rt, N=480) --------
print("== 07-22 confrontation ==", flush=True)
rel_90 = threshold(N=480, cfl=0.4, seed=1, n_roundtrips=90, nu=0.0, start=0, cache=CACHE)
aug_90 = threshold(N=480, cfl=0.4, seed=1, n_roundtrips=90, nu=NU0, start=5, cache=CACHE)
R['confront_0722'] = dict(released_widened8=rel_90, augmented_widened8=aug_90,
                          shift_pct=100 * (aug_90 / rel_90 - 1))
print(f"  90rt seed1 N=480: released={rel_90:.8f} augmented={aug_90:.8f} "
      f"shift={100*(aug_90/rel_90-1):+.2f}% (07-22 quoted: 0.15884 -> 0.18063, +13.72%)", flush=True)
save(); tsec(t0)

# ---- Cell A: augmented censuses (denominators + response exponent) ---------
print("== A augmented ==", flush=True)
for tag, nu, start in [('A_aug_nu0_over4', NU0 / 4, 4), ('A_aug_nu0_over2', NU0 / 2, 5),
                       ('A_aug_nu0', NU0, 7)]:
    R[tag] = census(N=240, cfl=0.4, nu=nu, start=start, cache=CACHE, label=tag)
    save(); tsec(t0)

# ---- Cell A: numerator partners (iso-dx cfl differencing) ------------------
print("== A partners ==", flush=True)
MA = R['A_rel']['median']
nuA = nu_num(240, 0.4, MA)
for tag, dnu, start in [('A_partner_nu0_over4', NU0 / 4, 5), ('A_partner_nu0_over2', NU0 / 2, 7)]:
    c2 = partner_cfl(240, 0.4, MA, dnu)
    print(f"  {tag}: nu_num(240,0.4,{MA:.6f})={nuA:.8f} + {dnu:.8f} -> cfl2={c2:.8f} "
          f"(check nu_num={nu_num(240, c2, MA):.8f})", flush=True)
    R[tag] = census(N=240, cfl=c2, nu=0.0, start=start, cache=CACHE, label=tag)
    R[tag]['cfl2'] = c2
    R[tag]['dnu'] = dnu
    save(); tsec(t0)

# ---- Cell G (240, 0.2): high-M family point --------------------------------
print("== G ==", flush=True)
R['G_rel'] = census(N=240, cfl=0.2, nu=0.0, start=7, cache=CACHE, label='G_rel')
save(); tsec(t0)
R['G_aug_nu0_over4'] = census(N=240, cfl=0.2, nu=NU0 / 4, start=8, cache=CACHE,
                              label='G_aug_nu0_over4')
save(); tsec(t0)
MG = R['G_rel']['median']
c2g = partner_cfl(240, 0.2, MG, NU0 / 4)
print(f"  G partner: nu_num(240,0.2,{MG:.6f})={nu_num(240, 0.2, MG):.8f} + {NU0/4:.8f} "
      f"-> cfl2={c2g:.8f}", flush=True)
R['G_partner_nu0_over4'] = census(N=240, cfl=c2g, nu=0.0, start=9, cache=CACHE,
                                  label='G_partner_nu0_over4')
R['G_partner_nu0_over4']['cfl2'] = c2g
R['G_partner_nu0_over4']['dnu'] = NU0 / 4
save(); tsec(t0)

# ---- Cell D (480, 0.4): low-M family point + modern 07-22 pair -------------
print("== D ==", flush=True)
R['D_rel'] = census(N=480, cfl=0.4, nu=0.0, start=0, cache=CACHE, label='D_rel')
save(); tsec(t0)
R['D_aug_nu0'] = census(N=480, cfl=0.4, nu=NU0, start=5, cache=CACHE, label='D_aug_nu0')
save(); tsec(t0)
R['D_aug_nu0_over4'] = census(N=480, cfl=0.4, nu=NU0 / 4, start=1, cache=CACHE,
                              label='D_aug_nu0_over4')
save(); tsec(t0)
MD = R['D_rel']['median']
c2d = partner_cfl(480, 0.4, MD, NU0 / 4)
print(f"  D partner: nu_num(480,0.4,{MD:.6f})={nu_num(480, 0.4, MD):.8f} + {NU0/4:.8f} "
      f"-> cfl2={c2d:.8f}", flush=True)
R['D_partner_nu0_over4'] = census(N=480, cfl=c2d, nu=0.0, start=4, cache=CACHE,
                                  label='D_partner_nu0_over4')
R['D_partner_nu0_over4']['cfl2'] = c2d
R['D_partner_nu0_over4']['dnu'] = NU0 / 4
save(); tsec(t0)

# ---- Crossover: N in {180, 300} at cfl 0.4, released + aug nu0 -------------
print("== crossover ==", flush=True)
R['N180_rel'] = census(N=180, cfl=0.4, nu=0.0, start=4, cache=CACHE, label='N180_rel')
save(); tsec(t0)
R['N180_aug_nu0'] = census(N=180, cfl=0.4, nu=NU0, start=8, cache=CACHE, label='N180_aug_nu0')
save(); tsec(t0)
R['N300_rel'] = census(N=300, cfl=0.4, nu=0.0, start=2, cache=CACHE, label='N300_rel')
save(); tsec(t0)
R['N300_aug_nu0'] = census(N=300, cfl=0.4, nu=NU0, start=6, cache=CACHE, label='N300_aug_nu0')
save(); tsec(t0)

# ---- Sensitivities at A, delta = nu0/2 (labeled: 8 seeds kept) -------------
print("== sensitivities ==", flush=True)
R['A_aug_nu0_over2_neumann'] = census(N=240, cfl=0.4, nu=NU0 / 2, bc='neumann',
                                      start=5, cache=CACHE, label='A_aug_nu0_over2_neumann')
save(); tsec(t0)
R['A_aug_nu0_over2_sub2x'] = census(N=240, cfl=0.4, nu=NU0 / 2, subcycle_factor=2.0,
                                    start=5, cache=CACHE, label='A_aug_nu0_over2_sub2x')
save(); tsec(t0)

print("== DONE ==", flush=True)
print(f"total {time.time()-t0:.0f}s", flush=True)
