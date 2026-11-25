"""usage: cross.py TAG RULELAYOUT  judge a clean run against the link-rule logic of another layout (window 0)"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
from ana import *

R = load(sys.argv[1]); rl = sys.argv[2]
names = layout(R['layout'])[0]
E = rules(rl, A_OP, B_OP)
for iw in range(len(R['windows'])):
    J = judge(R['Zw'][iw, 0, 0], E)
    print('%s judged against link rules of %s, window %s: all right %s, wrong %d of %d, max dev %.1f deg, min ratio %.3f' % (
        sys.argv[1], rl, R['windows'][iw].tolist(), bool(J['right_all'].all()), int((~J['right']).sum()), J['right'].size,
        J['maxdev'].max(), J['ratio'].min()))
J = judge(R['Zw'][0, 0, 0], rules(R['layout'][0] + '1', A_OP, B_OP))
for nm in names:
    if nm.startswith(('C', 'M', 'X2', 'X3')) and not nm.endswith('c'):
        m = names.index(nm)
        Es = rules(R['layout'][0] + '1', A_OP, B_OP)[m, 1:]
        act = np.where(J['right'][m], Es, 1 - Es)
        print('  %-3s intended %s' % (nm, ''.join(map(str, Es))))
        print('      actual   %s' % ''.join(map(str, act)))
