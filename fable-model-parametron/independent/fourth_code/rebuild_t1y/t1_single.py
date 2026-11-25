import sys, json, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
import rtdsim as R

OUT = __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "t1_results.json")
DT = 0.0145
TEND = 300.0

lay = R.Layout(['P'], [0], {}, [])

def dc_point(Vs):
    Rt = 2 * R.RB + R.RHO + R.RL
    f = lambda vj: vj - (Vs - Rt * R.FRAC * R.Ifull(vj))
    lo, hi = 0.0, Vs
    # check for multiple roots on a fine grid
    g = np.linspace(0, Vs, 20001)
    fv = f(g)
    roots = np.where(np.sign(fv[:-1]) != np.sign(fv[1:]))[0]
    vjs = []
    for r0 in roots:
        a, b = g[r0], g[r0 + 1]
        for _ in range(60):
            m = 0.5 * (a + b)
            if np.sign(f(m)) == np.sign(f(a)): a = m
            else: b = m
        vjs.append(0.5 * (a + b))
    return vjs

def init_state(Vs, vj, seed_amp, phi):
    x = np.zeros(R.NV)
    ix = R.FRAC * R.Ifull(vj)
    x[R.ix_S(0)] = Vs - 2 * R.RB * ix
    Z = np.sqrt(R.LODD / (R.CP + R.CS))  # kohm
    for h, sg in ((0, 1.0), (1, -1.0)):
        x[R.ix_vj(0, h)] = vj - sg * seed_amp * np.cos(phi)
        x[R.ix_ix(0, h)] = ix
        x[R.ix_vP(0, h)] = R.RL * ix + sg * seed_amp * np.cos(phi)
        x[R.ix_vst(0, h)] = R.RL * ix + sg * seed_amp * np.cos(phi)
        x[R.ix_iL(0, h)] = ix + sg * seed_amp / Z * np.sin(phi)
    return x

def analyse(out):
    t = out['t']; v = out['odd'][0, :, 0].astype(float)
    ve = out['even'][0, :, 0].astype(float)
    # last 30 ps
    m = t > t[-1] - 30
    amp_end = 0.5 * (v[m].max() - v[m].min())
    m0 = t < 5
    amp0 = 0.5 * (v[m0].max() - v[m0].min())
    even_pp = 0.5 * (ve[m].max() - ve[m].min())
    # frequency from zero crossings in last 30 ps
    vv = v[m]; tt = t[m]
    zc = np.where((vv[:-1] < 0) & (vv[1:] >= 0))[0]
    tz = tt[zc] - vv[zc] * (tt[zc + 1] - tt[zc]) / (vv[zc + 1] - vv[zc])
    f = (len(tz) - 1) / (tz[-1] - tz[0]) if len(tz) > 2 else float('nan')
    # phase vs cos(2 pi fd t) in last 6 carrier periods
    m2 = t > t[-1] - 6 * R.TC
    X = 2 * np.mean(v[m2] * np.exp(-1j * 2 * np.pi * R.FD * t[m2]))
    # envelope at 100 ps and 200 ps
    def amp_at(tc):
        mm = (t > tc - 5) & (t < tc + 5)
        return 0.5 * (v[mm].max() - v[mm].min())
    return dict(amp0=amp0, amp_end=amp_end, even_end=even_pp, f_THz=f, phase_deg=float(np.degrees(np.angle(X))),
                levelX=float(abs(X)), amp100=amp_at(100), amp200=amp_at(200))

res = {'scan': [], 'pump': []}
mode = sys.argv[1] if len(sys.argv) > 1 else 'scan'
if mode == 'scan':
    sim = R.Sim(lay, DT, np.array([[R.LODD]]), constant_supply=True)
    for Vs in np.round(np.arange(0.90, 1.2001, 0.01), 3):
        roots = dc_point(Vs)
        vj = roots[0]
        x0 = init_state(Vs, vj, 1e-3, 0.0)[None, :]
        t0 = time.time()
        out = sim.run(0.0, TEND, Vs, 0.0, x0=x0, rec_even=True)
        a = analyse(out)
        a.update(Vs=float(Vs), dc_roots=[float(r) for r in roots], secs=time.time() - t0)
        print(json.dumps(a)); sys.stdout.flush()
        res['scan'].append(a)
    json.dump(res, open(OUT.replace('.json', '_scan.json'), 'w'), indent=1)
elif mode == 'pump':
    Vs = 0.94; p = 0.25
    sim = R.Sim(lay, DT, np.array([[R.LODD]]), constant_supply=True)
    vj = dc_point(Vs)[0]
    for k in range(12):
        phi = 2 * np.pi * k / 12
        x0 = init_state(Vs, vj, 1e-3, phi)[None, :]
        out = sim.run(0.0, TEND, Vs, p, x0=x0, rec_even=True)
        a = analyse(out); a.update(seed_phase_deg=30 * k)
        print(json.dumps(a)); sys.stdout.flush()
        res['pump'].append(a)
    json.dump(res, open(OUT.replace('.json', '_pump.json'), 'w'), indent=1)
