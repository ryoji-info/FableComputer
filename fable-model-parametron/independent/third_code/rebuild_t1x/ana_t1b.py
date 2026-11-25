import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
from sim import *
from ana_t1 import env, freq

fn = sys.argv[1] if len(sys.argv) > 1 else 'res/t1b.npz'
d = np.load(fn); t = d['t']; v = d['v']
dt = t[1] - t[0]; n = int(round(Tc / dt))
m = len(t) // n
# phasor per carrier period at f_d
tt = t[:m * n].reshape(m, n); vv = v[:m * n].reshape(m, n, -1)
Zp = (2.0 / n) * np.einsum('mn,mnb->mb', np.exp(-1j * om * tt), vv)
tc = tt[:, n // 2]
Vs = d['Vs']; p = d['p']
print("p     Vs   osc  f_THz(last50ps)  level_mV  nphase  phases_deg            settle_ps(median/max)  min/max level over seeds")
for pp in sorted(set(p)):
    for vs in sorted(set(Vs)):
        idx = np.where((p == pp) & (Vs == vs))[0]
        Zend = Zp[-5:, idx].mean(axis=0)
        amp = np.abs(Zend) * 1e3
        osc = amp > 1.0
        fs = [freq(t[t > t[-1] - 50], v[t > t[-1] - 50, b]) for b in idx]
        # phase stability over last 50 ps
        dph = np.abs(np.angle(Zp[-50:, idx] / Zp[-1, idx][None]))
        stable = dph.max(axis=0) < np.deg2rad(5)
        ph = np.angle(Zend, deg=True)
        # cluster phases, 20 deg tolerance
        cl = []
        for k in range(len(idx)):
            if not osc[k]:
                continue
            for c in cl:
                if abs(((ph[k] - c[0] + 180) % 360) - 180) < 20:
                    c[1] += 1; break
            else:
                cl.append([ph[k], 1])
        # settling: first time after which |Z - Zend| < 0.1 |Zend| for all later periods
        st = []
        for k, b in enumerate(idx):
            err = np.abs(Zp[:, b] - Zend[k]) > 0.1 * np.abs(Zend[k])
            w = np.where(err)[0]
            st.append(np.nan if (not osc[k] or (len(w) and w[-1] + 1 >= m)) else (tc[w[-1] + 1] if len(w) else 0.0))
        st = np.array(st)
        print("%.2f %.2f  %2d/12  %.4f..%.4f  %.1f  %d  %s  stable_last50ps %d/12  settle %.1f/%.1f  amp %.1f..%.1f" % (
            pp, vs, osc.sum(), np.nanmin(fs), np.nanmax(fs), amp.mean(), len(cl),
            ' '.join('%.1f(x%d)' % (c[0], c[1]) for c in cl), stable.sum(), np.median(st), st.max(), amp.min(), amp.max()))
