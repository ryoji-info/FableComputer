# check that 3 fixed-point iterations on the diode term are enough: compare with 6 on layout (c), nominal, no noise
import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
import rtdsim as R, layouts as LY
lay = LY.layout_c()
t1 = 31 * R.TP + 3 * R.TP / 4 + R.RD_START + R.RD_LEN + 0.3
res = []
for nit in (3, 6):
    sim = R.Sim(lay, 0.0145, np.full((1, lay.N), R.LODD))
    out = sim.run(-4.0, t1, 0.94, 0.25, niter=nit)
    res.append(R.read_slots(out['t'], out['odd'][0], lay.depth)[:, 1:32])
d = np.degrees(np.abs(np.angle(res[0] * np.conj(res[1]))))
print('max phase change %.2e deg, max level change %.2e mV' % (d.max(), 1e3 * np.abs(np.abs(res[0]) - np.abs(res[1])).max()))
