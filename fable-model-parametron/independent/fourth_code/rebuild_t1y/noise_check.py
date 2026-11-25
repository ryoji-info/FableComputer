# equipartition check of the thermal-noise injection: one pair with supply 0 (diodes nearly off)
import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
import rtdsim as R
lay = R.Layout(['P'], [0], {}, [])
for dt in (0.0145, 0.00725):
    sim = R.Sim(lay, dt, np.array([[R.LODD]]), constant_supply=True)
    out = sim.run(0.0, 400.0, 0.0, 0.0, noise_f=1.0, seeds=[5], rec_even=True)
    v = out['odd'][0, :, 0].astype(float); t = out['t']
    m = t > 20
    var_odd = v[m].var()
    nav = int(round(0.116 / dt))
    vf = np.convolve(v[m], np.ones(nav) / nav, mode='valid')
    # power within 0.9-1.25 THz from the spectrum of the odd voltage
    vv = v[m] - v[m].mean(); F = np.fft.rfft(vv); fr = np.fft.rfftfreq(len(vv), dt)
    Pw = np.abs(F) ** 2 / len(vv) ** 2 * 2
    band = (fr > 0.9) & (fr < 1.25)
    print('   filtered(0.116 ps) var %.3e ; band 0.9-1.25 THz power %.3e ; total below 5 THz %.3e' % (vf.var(), Pw[band].sum(), Pw[fr < 5].sum()))
    # odd-mode stub voltage: (v+ - v-)/2 -> var = kT/(2 C_node) if each pad node holds kT/C
    kT = R.KB * R.TEMP
    Cn = (R.CP + R.CS + R.CD) * 1e-15
    print('dt', dt, 'sim var_odd %.3e V^2' % var_odd, ' kT/(2C) with C=Cp+Cs+Cd: %.3e' % (kT / (2 * Cn)),
          ' with C=Cp+Cs: %.3e' % (kT / (2 * (R.CP + R.CS) * 1e-15)))
