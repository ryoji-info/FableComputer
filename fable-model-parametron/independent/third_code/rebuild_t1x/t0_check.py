import sys, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
from sim import *

V = np.linspace(0, 1.6, 16001)
I = Ifull(V)
ip = np.argmax(I[V < 1.0]); print("peak", I[ip], V[ip])
m = (V > 1.0); iv = np.argmin(I[m]); print("valley", I[m][iv], V[m][iv])
# derivative check
dd = (Ifull(V + 1e-6) - Ifull(V - 1e-6)) / 2e-6
print("dI check", np.max(np.abs(dd - dIfull(V))))
for vs in [0.86, 0.9, 0.94, 1.0, 1.1, 1.2]:
    x = dc_state(np.array([vs]))
    print(vs, "vj", x[0, 1], "I per diode", x[0, 3], "vS", x[0, 0], "slope", frac * dIfull(x[0, 1]) * 1e3, "mS")
# timing of layout c
lay = layout_c()
t = time.time()
tr, rec, xf = simulate(lay, np.full(16, 0.94), np.full(16, 0.25), np.zeros((16, lay.N)), np.zeros(16), 1, Tc / 128, -2.0, 30.0, 4)
print("time for 32 ps B=16:", time.time() - t)
