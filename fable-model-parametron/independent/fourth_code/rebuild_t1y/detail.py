# details of a noisy point: wrong events and lowest levels
import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import numpy as np
import analyse as AN
name, nf = sys.argv[1], sys.argv[2]; tags = sys.argv[3:]
lay = AN.get_lay(name)
D = AN.D; SL = AN.SL
Xn = np.load('%s/%s_%s.npz' % (D, name, nf))['X'][0]
Xs = np.concatenate([np.load('%s/%s_%s.npz' % (D, name, t))['X'] for t in tags])
dr = np.concatenate([np.load('%s/%s_%s.npz' % (D, name, t))['draws'] for t in tags])
dphi = np.degrees(np.angle(Xs[:, :, SL] * np.conj(Xn[None, :, SL])))
lev = np.abs(Xs[:, :, SL]) * 1e3
w = np.abs(dphi) > 90
for b, i, j in zip(*np.where(w)):
    print('WRONG draw %d pair %s slot %d dphi %.0f level %.1f mV' % (dr[b], lay.names[i], SL[j], dphi[b, i, j], lev[b, i, j]))
flat = np.argsort(lev.ravel())[:15]
for f in flat:
    b, i, j = np.unravel_index(f, lev.shape)
    print('LOW draw %d pair %s slot %d level %.1f mV dphi %.0f' % (dr[b], lay.names[i], SL[j], lev[b, i, j], dphi[b, i, j]))
# per-draw min level
print('per-draw min level mV:', ' '.join('%d:%.0f' % (dr[b], lev[b].min()) for b in range(len(dr))))
# count of pair-slots below 100 mV
print('pair-slots below 100 mV:', int((lev < 100).sum()), ' below 50 mV:', int((lev < 50).sum()))
