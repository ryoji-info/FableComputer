import sys, os, json, time
SESSION = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SESSION)
from cascade_driver import mth_num, platform_line
t0 = time.time()
mth = {}
for N in (240, 480):
    mth[N] = float(mth_num(N)); print(f"M_th_num({N}) = {mth[N]!r}  [{time.time()-t0:.0f}s]", flush=True)
json.dump(mth, open(os.path.join(SESSION, "mth_num.json"), "w"))
cfgs = []
for m in (28, 30):
    cfgs.append({"tag": f"N480_m{m}_s7", "m": m, "N": 480, "seed": 7, "mth_num": mth[480], "depth": 2, "primary_J": -1})
for seed in (7, 11, 13):
    for m in (30, 28):
        cfgs.append({"tag": f"N240_m{m}_s{seed}", "m": m, "N": 240, "seed": seed, "mth_num": mth[240],
                     "depth": 4 if seed == 7 else 2, "primary_J": -1})
json.dump(cfgs, open(os.path.join(SESSION, "families.json"), "w"), indent=1)
print(f"{len(cfgs)} families written; platform {platform_line()}", flush=True)
