# Gate: reproduce 08-12 §1 gate 1 (M_th_num ladder) and gate 2 (the 08-02 §3.2 m=30, N=240
# duty-0.8 ratio-bias row: 8.287855791924017 / -11.828336851447219 / -11.775002445226676),
# then time one run.
import sys, time, json
sys.path.insert(0, "/tmp/claude-0/-home-user-FableComputer/6d749e7d-f55c-50b5-abe1-bec020fcd928/scratchpad/session")
from cascade_driver import *
t0 = time.time()
R = json.load(open(CHAIN + "/results.json"))
m240 = mth_num(240)
print("M_th_num(240) =", repr(m240), " results.json", repr(R["M_th_num"]), " rel", abs(m240 - R["M_th_num"]) / R["M_th_num"], f"[{time.time()-t0:.0f}s]", flush=True)
m, N = 30, 240
repT = 2.0 * m; nslots = 40; nrt = nslots * m
bits = default_bits(nslots, 7)
bias = 0.7 * m240
sig = make_sig_duty(bits, repT, F0N, 2e-3, duty=0.8, edge_rt=2.0)
t1 = time.time()
cM = run_cell(bias, N, nrt, source_clamp(sig))
t2 = time.time()
c0 = run_cell(0.0, N, nrt, source_clamp(sig))
t3 = time.time()
masksM = slot_windows(cM["t"], repT, nslots); masks0 = slot_windows(c0["t"], repT, nslots)
for obs in ("cav", "drn_h", "drn_u"):
    r = metrics(bits, slot_peaks(cM[obs], masksM), slot_peaks(c0[obs], masks0))
    print(obs, {k: (round(v, 12) if isinstance(v, float) else v) for k, v in r.items()}, flush=True)
print("targets (08-02 §3.2 / 08-12 gate 2): cav_u gain 8.287855791924017, floors cav_u -11.828336851447219 drn_h -11.775002445226676")
print(f"timing: active run {t2-t1:.1f}s, passive run {t3-t2:.1f}s, steps {len(cM['t'])} / {len(c0['t'])}; dt {cM['dt']:.6e} / {c0['dt']:.6e}")
print("platform:", platform_line())
