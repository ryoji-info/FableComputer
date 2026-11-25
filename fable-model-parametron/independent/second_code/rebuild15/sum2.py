import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
here = os.path.dirname(os.path.abspath(__file__))
fn = sys.argv[1] if len(sys.argv) > 1 else 'item2_D_222.npz'
d = np.load(os.path.join(here, fn))
Vs, p, Z, tb = d['Vs'], d['p'], d['Z'], d['tblk']
VsL = np.unique(Vs); pL = np.unique(p)
deg = 180 / np.pi
print('Vs     p    amp_med(V) amp_min amp_max  locked  nphase  phases(deg, vs cos(w t))   settle med/max (ps)  drift(deg/100ps,max)')
for pv in pL:
    for v in VsL:
        s = np.where((Vs == v) & (p == pv))[0]
        z = Z[:, s]
        amp = np.abs(z[-50:]).mean(0)
        osc = amp > 0.005
        ph = np.angle(z)
        # drift over last 400 ps
        k400 = int(round(400 / (tb[1] - tb[0])))
        dph = np.angle(z[-1] * np.conj(z[-1 - k400])) * deg / 4.0
        locked = osc & (np.abs(dph) < 1.0)
        fin = ph[-1]
        # cluster final phases (only oscillating runs)
        cl = []
        for f in fin[osc]:
            for c in cl:
                if abs(np.angle(np.exp(1j * (f - c)))) < 10 / deg:
                    break
            else:
                cl.append(f)
        # settle: last block where |phase - final| > 5 deg or amp < 0.5 final amp
        st = []
        for j in range(len(s)):
            if not osc[j]:
                continue
            bad = (np.abs(np.angle(z[:, j] * np.exp(-1j * fin[j]))) > 5 / deg) | (np.abs(z[:, j]) < 0.5 * amp[j])
            ib = np.where(bad)[0]
            st.append(tb[ib[-1] + 1] if len(ib) else tb[0])
        st = np.array(st)
        cls = ' '.join('%.0f' % (np.mod(c * deg, 360)) for c in sorted(np.mod(cl, 2 * np.pi)))
        print('%.3f %.2f  %.4f %.4f %.4f  %2d/12  %d  [%s]  %s  %.2f' % (
            v, pv, np.median(amp), amp.min(), amp.max(), locked.sum(), len(cl), cls,
            ('%.0f/%.0f' % (np.median(st), st.max())) if len(st) else '-', np.abs(dph).max()))
