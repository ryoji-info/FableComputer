# -*- coding: utf-8 -*-
"""Consolidated listing.  Run from the repository root.
   python3 LISTING.py validate | analytic | bulk | vn | corner | wp2 | ladder
                    | census90 | all | cell <tag> <N> <cfl> <i_start>
Python 3.11.2 / numpy 2.4.6 / macOS arm64.  fable-model-chain/ imported UNEDITED."""
import sys, math, cmath, statistics as st
sys.path.insert(0, 'fable-model-chain')
import numpy as np
import constants as C, ds_cell as DS, kinetic as K, solver as SOL, run_all

s = DS.plasmon_speed(); L = DS.cell_length(s); tau = C.tau(C.Tcap)
Mth = DS.M_threshold(L, s, tau)                       # 0.14708333333333332
TAU_N = tau * s / L                                   # 3.39943342776204
NU0 = (C.vF**2 * K.tau_ee(C.Tcap) / 4.0) / (L * s)    # 07-22's DC kinematic viscosity
INVISCID = 0.149313                                   # results.json M_th_num_inviscid_limit
MTHNUM = 0.16894319463373791                          # results.json M_th_num (seed 1, 90 rt)
HDRM = 0.2                                            # solver.py's (uncommented) cmax pad
Z = np.zeros((2, 2))

# ---- 1. the LF diffusion MATRIX and the 07-22 scalar it IS ---------------------------
def Amat(M):
    return np.array([[0.0, 1.0], [1 - M * M, 2 * M]])

def D_LF(N, cfl, M):
    """q_t + A q_x = D q_xx  with  D = (dx^2/2dt)(I - nu^2 A^2),  nu = dt/dx."""
    dx = 1.0 / N; dt = cfl * dx / (1.0 + abs(M) + HDRM); nu = dt / dx
    return (dx * dx / (2 * dt)) * (np.eye(2) - nu * nu * Amat(M) @ Amat(M))

def nu_num_0722(N, cfl=0.4, M=Mth):
    """07-22 sec2's characteristic-averaged scalar, verbatim from its own listing."""
    dx = 1.0 / N; cmax = 1 + abs(M) + HDRM; dt = cfl * dx / cmax; pref = dx**2 / (2 * dt)
    return 0.5 * (pref * (1 - ((1 + M) * dt / dx)**2) + pref * (1 - ((1 - M) * dt / dx)**2))

def g_of_cfl(cfl, M):                                  # nu_num = dx * g(cfl, M)
    cmax = 1 + abs(M) + HDRM
    return (cmax / (2 * cfl)) * (1 - (cfl / cmax)**2 * (1 + M * M))

def cfl_for(gt, M):                                    # invert g -> the iso-nu partner
    cmax = 1 + abs(M) + HDRM; a = 1 + M * M
    return ((-2 * gt + math.sqrt(4 * gt * gt + 4 * a)) / (2 * a)) * cmax

# ---- 2. BULK-ONLY MODEL: two physical branches + the two inviscid DS wall conditions --
def _mode_det(w, M, D, tau_n=TAU_N, Dp=None):
    """Dp (default D) is the matrix used for the polarization vectors."""
    r = 1.0 / tau_n
    W11 = np.array([D[0,0], 0+0j, -1j*w]);            W12 = np.array([D[0,1], 1j, 0+0j])
    W21 = np.array([D[1,0], 1j*(1-M*M), -M*r]);       W22 = np.array([D[1,1], 2j*M, -1j*w+r])
    ks = np.roots(np.polysub(np.polymul(W11, W22), np.polymul(W12, W21)))
    ks = ks[np.argsort(np.abs(ks))][:2]
    P = D if Dp is None else Dp
    ph = []
    for k in ks:
        a = P[0,0]*k*k - 1j*w;                    b = P[0,1]*k*k + 1j*k
        c = P[1,0]*k*k + 1j*k*(1-M*M) - M/tau_n;  d = P[1,1]*k*k + 2j*k*M - 1j*w + 1.0/tau_n
        v1 = np.array([b, -a]); v2 = np.array([d, -c])
        v = v1 if np.linalg.norm(v1) >= np.linalg.norm(v2) else v2
        ph.append(v / np.linalg.norm(v))
    return ph[0][0]*ph[1][1]*cmath.exp(1j*ks[1]) - ph[1][0]*ph[0][1]*cmath.exp(1j*ks[0])

def mode_omega(M, D, tau_n=TAU_N):
    w0 = math.pi*(1-M*M)/2.0 + 0.05j; w1 = w0*(1+1e-4) + 1e-5j
    f0 = _mode_det(w0, M, D, tau_n); f1 = _mode_det(w1, M, D, tau_n)
    for _ in range(80):
        if abs(f1 - f0) < 1e-300: break
        w2 = w1 - f1*(w1-w0)/(f1-f0); w0, f0, w1 = w1, f1, w2
        f1 = _mode_det(w1, M, D, tau_n)
        if abs(w1 - w0) < 1e-13: break
    return w1

def M_th_bulk(D_of_M, lo=0.05, hi=0.40, iters=60):
    for _ in range(iters):
        mid = 0.5*(lo+hi)
        lo, hi = (mid, hi) if mode_omega(mid, D_of_M(mid)).imag < 0 else (lo, mid)
    return 0.5*(lo+hi)

def Dmom(nu, M):                 # momentum-only nu*d2u/dx2, linearized about (1, M)
    return nu * np.array([[0.0, 0.0], [-M, 1.0]])

def Dmom_m(nu, M):               # same-trace comparator nu*d2(dm)/dx2 (claim 3b)
    return nu * np.array([[0.0, 0.0], [0.0, 1.0]])

# ---- 3. EXACT linearized one-step operator (07-12-boundary-factor App. B) -------------
def blocks(M, N, cfl, tau_n=TAU_N, relax="euler", closure="released"):
    dx = 1.0/N; dt = cfl*dx/(1+abs(M)+HDRM); nu = dt/dx; sd = dt/tau_n
    A = Amat(M); P = 0.5*(np.eye(2)-nu*A); Q = 0.5*(np.eye(2)+nu*A)
    if relax == "euler":  R = np.array([[1.0,0.0],[sd*M, 1-sd]])
    else:                 E = math.exp(-sd); R = np.array([[1.0,0.0],[M*(1-E), E]])
    if   closure == "released":    S = np.array([[0.,0.],[-M,1.]]);      Dg = np.array([[1.,0.],[0.,0.]])
    elif closure == "mirror":      S = np.array([[-1.,0.],[-2*M,1.]]);   Dg = np.array([[1.,0.],[0.,-1.]])
    elif closure == "mirror_src":  S = np.array([[-1.,0.],[-2*M,1.]]);   Dg = np.array([[1.,0.],[0.,0.]])
    elif closure == "mirror_drn":  S = np.array([[0.,0.],[-M,1.]]);      Dg = np.array([[1.,0.],[0.,-1.]])
    return A, P, Q, R, S, Dg, dt

def build_T(M, N, cfl, **kw):
    A, P, Q, R, S, Dg, dt = blocks(M, N, cfl, **kw)
    T = np.zeros((2*N, 2*N))
    def put(j, jc, mat):
        for a in range(2):
            for b in range(2): T[j+a*N, jc+b*N] += mat[a, b]
    for j in range(N):
        put(j, j+1, R@P) if j+1 <= N-1 else put(j, N-1, R@P@Dg)
        put(j, j-1, R@Q) if j-1 >= 0    else put(j, 0,   R@Q@S)
    return T, dt

def dominant(M, N, cfl, **kw):
    T, dt = build_T(M, N, cfl, **kw); ev = np.linalg.eigvals(T)
    lam = ev[np.argmax(np.abs(ev))]
    return abs(lam)**(2.0/dt), abs(np.angle(lam))/dt/(2*math.pi)

def M_th_lin(N, cfl=0.4, lo=0.10, hi=0.30, iters=30, **kw):
    for _ in range(iters):
        mid = 0.5*(lo+hi); T, _ = build_T(mid, N, cfl, **kw)
        lo, hi = (mid, hi) if max(abs(np.linalg.eigvals(T))) < 1 else (lo, mid)
    return 0.5*(lo+hi)

# ---- 3b. 07-12-effective-loop's von Neumann chain (sec0 claim 10) ---------------------
def loop_analytic(M):
    """(1+M)/(1-M) * exp(-t_rt / 2 tau_n), t_rt = 2, at the ZERO-DRIFT length.
       NO 1/(1-M^2) drift factor -- that was this memo's own earlier error."""
    return (1 + M) / (1 - M) * math.exp(-2.0 / (2 * TAU_N))

def a_d_int(M, f, N=240, cfl=0.4):
    """07-12-effective-loop sec2's interior von Neumann round-trip factor."""
    dx = 1.0/N; dt = cfl*dx/(1+abs(M)+HDRM); tot = 0.0
    for sg in (+1, -1):
        c = 1 + sg*M; nu = c*dt/dx; xi = 2*math.pi*f/c*dx
        tot += 0.5*math.log(1 - (1-nu*nu)*math.sin(xi)**2) * ((1.0/c)/dt)
    return math.exp(tot)

def solve_vn(N, ln_ab, cfl=0.4):
    lo, hi = 0.05, 0.40
    for _ in range(200):
        m = 0.5*(lo+hi)
        f = loop_analytic(m)*a_d_int(m, (1-m*m)/4, N=N, cfl=cfl)*math.exp(ln_ab) - 1.0
        lo, hi = (m, hi) if f < 0 else (lo, m)
    return 0.5*(lo+hi)

# ---- 4. the estimator: released logic, WIDENED bracket at the RELEASED node spacing ---
XS8 = np.linspace(1.05, 1.30, 8); STEP = XS8[1] - XS8[0]
def xnode(i):  return XS8[i] if 0 <= i <= 7 else 1.05 + i*STEP

def released_scan(N, nrt, seed, cfl):
    g = [SOL.growth_rate(x*Mth, N=N, n_roundtrips=nrt, seed=seed, cfl=cfl) for x in XS8]
    for i in range(7):
        if g[i] < 0 <= g[i+1]:
            return (XS8[i] + (XS8[i+1]-XS8[i])*(-g[i])/(g[i+1]-g[i]))*Mth, g
    return float('nan'), g

def widened_scan(N, nrt, seed, cfl, i_start, span=8):
    cache = {}
    def G(i):
        if i not in cache:
            cache[i] = float(SOL.growth_rate(xnode(i)*Mth, N=N, n_roundtrips=nrt,
                                             seed=seed, cfl=cfl))
        return cache[i]
    i = i_start
    while G(i) >= 0 and i > i_start - span: i -= 1
    if G(i) >= 0: return float('nan'), cache
    j = i + 1
    while G(j) < 0 and j < i + span: j += 1
    if G(j) < 0: return float('nan'), cache
    return (xnode(j-1) + (xnode(j)-xnode(j-1))*(-G(j-1))/(G(j)-G(j-1)))*Mth, cache

CELLS = [("A",240,0.400000,2), ("B",480,0.213755,2), ("C",720,0.144494,2),
         ("D",480,0.400000,0), ("E",960,0.213929,0), ("F",720,0.400000,0),
         ("G",240,0.200000,7), ("H",240,0.300000,4), ("I",240,0.500000,1),
         ("J",120,0.400000,6), ("K",960,0.400000,-1),
         ("L",360,0.400000,1), ("M",120,0.200000,16)]      # L, M measured by the checkers
MED = {"A":0.1687658795,"B":0.1680689399,"C":0.1678627280,"D":0.1588334587,
       "E":0.1585121120,"F":0.1556041775,"G":0.1912244214,"H":0.1761747951,
       "I":0.1642730737,"J":0.1900370478,"K":0.1540090045,
       "L":0.1621003583,"M":0.2416750895}                  # measured, mode 'cell'
LADDER_N   = [120, 240, 480, 720, 960]
LADDER_MED = [0.1900370478, 0.1687658795, 0.1588334587, 0.1556041775, 0.1540090045]
LADDER_OP  = [0.19002573, 0.16876409, 0.15883385, 0.15561613, 0.15402374]

def do_validate():
    print("[V] DRIVER VALIDATION -- nothing below is trusted until these pass")
    r0 = run_all.measure_Mth_num(); r1, _ = released_scan(240, 90, 1, 0.4)
    r2, cache = widened_scan(240, 90, 1, 0.4, 2)
    print("    run_all.measure_Mth_num()  = %r" % r0)
    print("    released 8-node scan       = %r  equal: %s" % (r1, r1 == r0))
    print("    widened scan (nodes %s) = %r  equal: %s" % (sorted(cache), r2, r2 == r0))
    print("    results.json M_th_num      = 0.16894319463373791  equal: %s"
          % (r0 == 0.16894319463373791))
    la, fl = dominant(0.7*MTHNUM, 240, 0.4); lp, flp = dominant(1e-9, 240, 0.4)
    print("    operator l_a = %.6f (07-12-boundary-factor App.B 0.910958), line %.6f (0.244513)" % (la, fl))
    print("    operator l_p = %.6f (0.724999),                            line %.6f (0.247862)" % (lp, flp))
    print("    M_th,lin(240,0.4) = %.6f (07-12-boundary-factor 0.168764)" % M_th_lin(240, 0.4, iters=44))

def do_bulk():
    print("\n[2] THE FACTOR 2 IS A TRACE IDENTITY (sec0 claim 3), k = pi")
    print("    tr(A^2) = 2 + 2 M^2  =>  0.5 tr D = (dx^2/2dt)(1 - nu^2(1+M^2)) == 07-22's scalar")
    print("    max|0.5trD/nu_num - 1| over 4x4x4 lattice = %.2e  (machine eps on an IDENTITY)" % max(
        abs(nu_num_0722(N,c,M)/(0.5*np.trace(D_LF(N,c,M))) - 1)
        for N in (240,480,720,960) for c in (0.2,0.3,0.4,0.5) for M in (0.10,Mth,0.169,0.25)))
    for withS in (True, False):
        print("    relaxation %s" % ("ON" if withS else "OFF"))
        for nu in (1e-2, 1e-3, 1e-4):
            for M in (1e-4, 0.05, 0.10, 0.149313, 0.20, 0.30):
                k = math.pi
                S = (1.0/TAU_N)*np.array([[0.,0.],[M,-1.]]) if withS else Z
                base = -1j*k*Amat(M) + S
                def dmp(D):
                    e0 = np.linalg.eigvals(base); e1 = np.linalg.eigvals(base - k*k*D)
                    e0 = e0[np.argsort(-e0.real)]; e1 = e1[np.argsort(-e1.real)]
                    return e0.real - e1.real
                a = dmp(D_LF(240,0.4,M)); b = dmp(Dmom(nu,M)); c = dmp(nu*np.eye(2))
                nn = 0.5*np.trace(D_LF(240,0.4,M)); bb = dmp(Dmom(nn,M))
                if nu == 1e-2:
                    print("      M=%.6f sum(D_LF/mom)=%.12f  per-branch iso/mom=%.9f,%.9f  D_LF/mom=%.6f,%.6f"
                          % (M, a.sum()/bb.sum(), (c/dmp(Dmom(nu,M)))[0], (c/dmp(Dmom(nu,M)))[1],
                             (a/bb)[0], (a/bb)[1]))
                else:
                    assert abs(c.sum()/dmp(Dmom(nu,M)).sum() - 2.0) < 1e-10
    print("\n[3b] the CAVITY table, and that its M-dependence is the CLOSURE not the bulk")
    print("    M         full/mom   iso(nu I)/mom   same-trace nu d2(dm)/mom   iso/mom no-relax   (2-r)/asym")
    for M in (1e-4, 0.05, 0.10, 0.149313, 0.20, 0.30):
        nn = 0.5*np.trace(D_LF(240,0.4,M)); I = nn*np.eye(2)
        w0 = mode_omega(M, Z).imag; d = lambda D: w0 - mode_omega(M, D).imag
        big = 1e9; w0b = mode_omega(M, Z, tau_n=big)
        dn = lambda D: w0b.imag - mode_omega(M, D, tau_n=big).imag
        r_full = d(D_LF(240,0.4,M))/d(Dmom(nn,M)); r_iso = d(I)/d(Dmom(nn,M))
        r_m = d(I)/d(Dmom_m(nn,M)); r_nr = dn(I)/dn(Dmom(nn,M))
        asym = ((1+M)/(1-M))**2 - 1
        print("    %.6f  %8.5f  %12.6f  %20.6f  %17.6f   %8.5f"
              % (M, r_full, r_iso, r_m, r_nr, (2-r_iso)/asym if asym > 1e-6 else float('nan')))

def do_vn():
    print("\n[claim 10] 07-12-effective-loop reproduces EXACTLY from its stated inputs")
    print("    loop_analytic(M_th_num) = %.9f   (note sec3: 1.048112)" % loop_analytic(MTHNUM))
    print("    loop_analytic(M_run)    = %.9f   (note sec4: 0.945034)" % loop_analytic(0.7*MTHNUM))
    drift = lambda M: (1+M)/(1-M)*math.exp(-2.0/(2*TAU_N*(1-M*M)))
    print("    with a spurious 1/(1-M^2) in the exponent: %.9f / %.9f  <- this memo's earlier error"
          % (drift(MTHNUM), drift(0.7*MTHNUM)))
    print("    a_d,int driven  (M=0.118260, f=0.25)     = %.6f  (note 0.966897)" % a_d_int(0.118260, 0.25))
    print("    a_d,int thresh  (M=M_th_num, f=(1-M^2)/4)= %.6f  (note 0.964253)"
          % a_d_int(MTHNUM, (1-MTHNUM**2)/4))
    print("    a_d,int passive (M=0, f=0.25)            = %.6f  (note 0.972957)" % a_d_int(0.0, 0.25))
    ab = 1.0/(loop_analytic(MTHNUM)*a_d_int(MTHNUM, (1-MTHNUM**2)/4))
    print("    a_b calibrated at N=240                  = %.7f  (note 0.98947)" % ab)
    print("    l_a = %.6f (note 0.9041); interior-only limit %.6f (note 0.9138)"
          % (loop_analytic(0.7*MTHNUM)*a_d_int(0.118260,0.25)*ab,
             loop_analytic(0.7*MTHNUM)*a_d_int(0.118260,0.25)))
    lnab = math.log(ab)
    print("    sec7 branch  boundary ~ dx  : %.6f  (note 0.1573)" % solve_vn(480, lnab/2))
    print("    sec7 branch  boundary ~ dx^2: %.6f  (note 0.1560)" % solve_vn(480, lnab/4))
    print("    measured N=480: 0.158748 (07-12-predictions-resolved) / 0.1588334587 (cell D here)")
    print("\n    WHY both branches missed: only 16.2 %% of a_b is clamp placement")
    for N in (240, 480, 720):
        M = M_th_lin(N, 0.4, iters=40)
        v = loop_analytic(M)*a_d_int(M, (1-M*M)/4, N=N)
        rho = dominant(M, N, 0.4)[0]; rhom = dominant(M, N, 0.4, closure="mirror")[0]
        tot = -math.log(rho/v); cl = math.log(rhom/rho)
        print("      N=%3d  operator-vs-vonNeumann residue %.4f %%/rt = clamp %.4f %% + non-clamp %.4f %%"
              " ; clamp*N = %.4f" % (N, 100*tot, 100*cl, 100*(tot-cl), cl*N))
    for name, M in (("M_th_num", MTHNUM), ("M_run = 0.7 M_th_num", 0.7*MTHNUM)):
        rr = dominant(M,240,0.4)[0]; mm = dominant(M,240,0.4,closure="mirror")[0]
        print("      clamp cost at %-20s = %.4f %%/rt  -> %.1f %% of a_b's %.4f %%/rt"
              % (name, 100*math.log(mm/rr), 100*math.log(mm/rr)/(-100*math.log(ab)), -100*math.log(ab)))
    cl240 = math.log(dominant(M_th_lin(240,0.4,iters=40),240,0.4,closure="mirror")[0]
                     / dominant(M_th_lin(240,0.4,iters=40),240,0.4)[0])
    rest = -lnab - cl240
    print("    corrected branch (clamp ~ dx, non-clamp frozen)      -> %.6f" % solve_vn(480, -(cl240/2 + rest)))
    print("    corrected branch (operator's own N=480 non-clamp)    -> %.6f" % solve_vn(480, -(cl240/2 + 0.00760)))

def do_analytic():
    print("\n[1] the D matrix at the shipped point, all four normalizations")
    D = D_LF(240, 0.4, MTHNUM); pr = (1/240)*(1+MTHNUM+HDRM)/(2*0.4)
    Dn = D/pr; tr = np.trace(Dn); md = 0.5*(Dn[0,0]+Dn[1,1]); ev = np.linalg.eigvals(Dn)
    print("    prefactor = %.9e\n" % pr, Dn)
    print("    offdiag/trace  %.5f %.5f | offdiag/mean-diag %.5f %.5f | diag-aniso/mean-diag %.5f"
          " | eig spread/mean %.5f" % (Dn[0,1]/tr, Dn[1,0]/tr, Dn[0,1]/md, Dn[1,0]/md,
                                       (Dn[0,0]-Dn[1,1])/md, (max(ev)-min(ev))/np.mean(ev)))
    print("    true Courant = %.6f" % (0.4/(1+MTHNUM+HDRM)))
    for M in (Mth, MTHNUM):
        cm0 = 1+M; r = 0.4/cm0
        print("    cmax pad inflates nu_num by %.3f %% at M=%.8f"
              % (100*(g_of_cfl(0.4,M)/((cm0/0.8)*(1-r*r*(1+M*M))) - 1), M))
    for N in (240,480,720):
        print("    N=%3d nu_num=%.4e nu_num/nu0=%.4f  (07-22 vote record: 0.418/0.209/0.139)"
              % (N, nu_num_0722(N), nu_num_0722(N)/NU0))
    print("    N*(coefficient) = %.2f  (visc_numerical_crossover_N ~ 100)" % (240*nu_num_0722(240)/NU0))
    print("\n[2] bulk-only anchor, Validation 2 decomposed, threshold-matched crossover")
    M0 = M_th_bulk(lambda M: Z)
    drive = lambda M: ((s**2-(M*s)**2)/(2*s*L))*math.log((s+M*s)/(s-M*s))
    lo, hi = 1e-5, 0.5
    for _ in range(200):
        m = 0.5*(lo+hi); lo, hi = (m, hi) if drive(m) < 1/(2*tau) else (lo, m)
    dsz = 0.5*(lo+hi)
    print("    bulk-only D=0 = %.9f ; ds_increment zero = %.10f ; diff %.2e" % (M0, dsz, M0-dsz))
    a = M_th_bulk(lambda M: D_LF(480,0.4,M)); b = M_th_bulk(lambda M: D_LF(480,0.4,M)+Dmom(NU0,M))
    S0, S1 = 0.15884, 0.18063                        # 07-22 sec3, QUOTED not re-run
    print("    model  %.6f -> %.6f  shift %+.6e (%.2f %%)" % (a, b, b-a, 100*(b/a-1)))
    print("    solver %.5f  -> %.5f   shift %+.6e (%.2f %%)   [QUOTED from 07-22 sec3]"
          % (S0, S1, S1-S0, 100*(S1/S0-1)))
    print("    baseline offset %+.2e ; shift offset %+.2e (%.1f %%) ; sum = value offset %+.2e"
          % (a-S0, (b-a)-(S1-S0), 100*((b-a)-(S1-S0))/(S1-S0), (a-S0)+((b-a)-(S1-S0))))
    print("    equal-shift model %% would be %.2f -> baseline explains %.2f pp of the %.2f pp gap"
          % (100*(S1-S0)/a, 100*(S1-S0)/a - 100*(S1/S0-1), 100*(b/a-1) - 100*(S1/S0-1)))
    tgt = M_th_bulk(lambda M: Dmom(NU0, M)); lo, hi = 40.0, 400.0
    for _ in range(50):
        mid = 0.5*(lo+hi)
        lo, hi = (mid, hi) if M_th_bulk(lambda M: D_LF(mid,0.4,M)) > tgt else (lo, mid)
    print("    momentum-only nu0 threshold %.7f ; bulk-only-vs-bulk-only N* = %.1f" % (tgt, 0.5*(lo+hi)))
    Mi, p, A = _ladder_fit(LADDER_N, LADDER_MED)
    print("    MEASURED-ladder equal-threshold grid = %.1f  (07-22 caveat ~240)"
          % ((A/(tgt-Mi))**(1.0/p)))
    print("    total-shift ratio grid = %.1f" % (240*(MED['A']-INVISCID)/(tgt-M0)))
    for N,cfl in ((240,0.4),(480,0.4),(720,0.4),(240,0.2),(240,0.5)):
        mb = M_th_bulk(lambda M: D_LF(N,cfl,M))
        mm = M_th_bulk(lambda M: Dmom(0.5*np.trace(D_LF(N,cfl,M)), M))
        print("    threshold ratio at N=%3d cfl=%.1f : %.4f" % (N, cfl, (mb-M0)/(mm-M0)))
    print("\n[5] DECOMPOSITION over the thirteen cells, and the two factorizations")
    for tag, N, cfl, _i in CELLS:
        mb = M_th_bulk(lambda M: D_LF(N,cfl,M))
        mr = M_th_lin(N,cfl);                      mm = M_th_lin(N,cfl,closure="mirror")
        ms = M_th_lin(N,cfl,closure="mirror_src"); md = M_th_lin(N,cfl,closure="mirror_drn")
        me = M_th_lin(N,cfl,relax="exact")
        dM = MED[tag]-INVISCID; bulk = mb-M0; cl = mr-mm; sp = mr-me
        oth = (mr-mb)-cl-sp;    est = MED[tag]-mr; p = lambda x: 100*x/dM
        assert abs(bulk+(M0-INVISCID)+cl+sp+oth+est - dM) < 1e-12
        print("  %s N=%4d cfl=%.6f dM=%.4e | bulk %.3e %5.2f%% | clamps %.3e %5.2f%% "
              "(src %.4e / drn %.4e, additivity %+.1e) | split %.2e %5.2f%% | other %.3e %5.2f%% | est %+.1e %5.2f%%"
              % (tag,N,cfl,dM, bulk,p(bulk), cl,p(cl), mr-ms, mr-md, (mr-ms)+(mr-md)-cl,
                 sp,p(sp), oth,p(oth), est,p(est)))
        print("      M_bulk=%.8f M_lin=%.8f mirror=%.8f |M_lin-meas|=%.2e other/bulk=%.3f%% clamps/dx=%.4f"
              % (mb, mr, mm, abs(est), 100*oth/bulk, cl*N))
    N, cfl, tag = 240, 0.4, "A"
    mb = M_th_bulk(lambda M: D_LF(N,cfl,M)); mr = M_th_lin(N,cfl)
    mm = M_th_lin(N,cfl,closure="mirror"); me = M_th_lin(N,cfl,relax="exact")
    mu = M_th_bulk(lambda M: Dmom(0.5*np.trace(D_LF(N,cfl,M)), M)) - M0
    dM = MED[tag]-INVISCID; dM0 = MED[tag]-Mth; B = INVISCID-Mth
    bulk = mb-M0; cl = mr-mm; sp = mr-me; oth = (mr-mb)-cl-sp
    c1 = bulk; c2 = c1+oth; c3 = c2+cl; c4 = c3+sp        # cumulative partial sums
    print("    mu (mom-only bulk-only shift at the same LAPLACIAN coefficient) = %.7e" % mu)
    print("    numerics factor  dM/mu = %.5f" % (dM/mu))
    print("      = %.5f (mass) x %.5f (higher-order) x %.5f (clamps) x %.5f (split) x %.5f (est+base)"
          % (c1/mu, c2/c1, c3/c2, c4/c3, dM/c4))
    print("      product check = %.5f" % ((c1/mu)*(c2/c1)*(c3/c2)*(c4/c3)*(dM/c4)))
    print("    07-22-referenced dM0/mu = %.5f  =  B/mu %.5f  +  dM/mu %.5f"
          % (dM0/mu, B/mu, dM/mu))
    print("    with the registered M_th_num instead of M-bar: %.5f = %.5f + %.5f"
          % ((MTHNUM-Mth)/mu, B/mu, (MTHNUM-INVISCID)/mu))
    print("    07-22-referenced shares: baseline %.2f / bulk %.2f / remainder %.2f / clamps %.2f"
          " / split %.2f / est %.2f %%"
          % (100*B/dM0, 100*bulk/dM0, 100*oth/dM0, 100*cl/dM0, 100*sp/dM0, 100*(MED[tag]-mr)/dM0))
    nu0shift = M_th_bulk(lambda M: Dmom(NU0,M))-M0
    print("    nu0/nu_num(240) = %.4f ; mom-only shift ratio nu0:nu_num = %.4f ; dM/(nu0 shift) = %.4f"
          % (NU0/nu_num_0722(240), nu0shift/mu, dM/nu0shift))

def do_corner():
    print("\n[5] drain/source over the SAMPLED LATTICE (sec0 claim 5) -- 9 x 5")
    print("N     cfl    both        source      drain       drain/source   clamps/dx")
    for N in (120, 150, 180, 240, 300, 360, 480, 720, 960):
        for c in (0.2, 0.25, 0.3, 0.4, 0.5):
            if N >= 720 and c in (0.25, 0.3): continue
            if N == 720 and c == 0.5: continue
            mr = M_th_lin(N, c, iters=26); mm = M_th_lin(N, c, iters=26, closure="mirror")
            ms = M_th_lin(N, c, iters=26, closure="mirror_src")
            md = M_th_lin(N, c, iters=26, closure="mirror_drn")
            print("%4d  %.2f  %.4e  %.4e  %.4e  %8.3f      %.4f"
                  % (N, c, mr-mm, mr-ms, mr-md, (mr-md)/(mr-ms), (mr-mm)*N), flush=True)

def do_wp2():
    print("\n[11] WP2: is the clamp bias a resolution FLOOR or a common-mode OFFSET?")
    print("    move the threshold with tau_n and re-measure the drain term at fixed (N, cfl)")
    prev = None
    for sc in (0.94, 0.97, 1.00, 1.03, 1.06):
        tn = TAU_N*sc
        mr = M_th_lin(240, 0.4, iters=40, tau_n=tn)
        md = M_th_lin(240, 0.4, iters=40, tau_n=tn, closure="mirror_drn")
        d = mr - md
        slope = "" if prev is None else "%.5f" % ((d-prev[1])/(mr-prev[0]))
        print("    tau_n x %.2f  M_th,lin %.8f  drain term %.6e  d(drain)/dM_th %s"
              % (sc, mr, d, slope), flush=True)
        prev = (mr, d)
    for N in (240, 960):
        mr = M_th_lin(N, 0.4, iters=32); md = M_th_lin(N, 0.4, iters=32, closure="mirror_drn")
        print("    absolute drain term at N=%3d: %.4e  -> N for 1e-4 by dx-linearity from here: %.0f"
              % (N, mr-md, N*(mr-md)/1e-4))

def _ladder_fit(Ns, Ms, cap=None):
    best = None; hi = min(Ms) - 1e-7
    if cap is not None: hi = min(hi, cap)
    x = [math.log(N) for N in Ns]; n = len(x); sx = sum(x); sxx = sum(a*a for a in x)
    i = 0
    while True:
        Minf = 0.140 + i*1e-7; i += 1
        if Minf > hi: break
        y = [math.log(M - Minf) for M in Ms]
        sy = sum(y); sxy = sum(a*b for a, b in zip(x, y))
        b = (n*sxy - sx*sy)/(n*sxx - sx*sx); a0 = (sy - b*sx)/n
        r2 = sum((yy-(a0+b*xx))**2 for xx, yy in zip(x, y))
        if best is None or r2 < best[0]: best = (r2, Minf, -b, math.exp(a0))
    return best[1], best[2], best[3]

def do_ladder():
    print("\n[6.2] five-rung ladder fits -- the UNRESTRICTED optimum, and the capped one")
    for nm, Ms in (("measured", LADDER_MED), ("operator", LADDER_OP)):
        Mi, p, A = _ladder_fit(LADDER_N, Ms)
        print("    %s unrestricted : M_inf = %.6f  p = %.4f  A = %.4f" % (nm, Mi, p, A))
        Mi, p, A = _ladder_fit(LADDER_N, Ms, cap=INVISCID)
        print("    %s capped at %.6f : M_inf = %.6f  p = %.4f  <- the earlier 'free' fit"
              % (nm, INVISCID, Mi, p))
        y = [math.log(M - Mth) for M in Ms]; x = [math.log(N) for N in LADDER_N]
        n = len(x); sx = sum(x); sy = sum(y); sxx = sum(a*a for a in x)
        sxy = sum(a*b for a, b in zip(x, y))
        print("    %s fixed at 0.147083 : p = %.4f" % (nm, -(n*sxy-sx*sy)/(n*sxx-sx*sx)))
    def fit3(m1, m2, m3, N1=240, N2=480, N3=720):
        f = lambda p: (m1-m2)/(m2-m3) - (N1**-p - N2**-p)/(N2**-p - N3**-p)
        a, b = 0.02, 10.0
        for _ in range(300):
            c = 0.5*(a+b)
            if f(a)*f(c) <= 0: b = c
            else: a = c
        p = 0.5*(a+b); return p, m1 - (m1-m2)/(N1**-p - N2**-p)*N1**-p
    print("    08-06's three-rung bisection on my 240-rt medians: p = %.4f, M_inf = %.5f (registered 1.0433 / 0.14947)"
          % fit3(0.1687658795, 0.1588334587, 0.1556041775))
    print("    08-06's three-rung bisection on my  90-rt medians: p = %.4f, M_inf = %.5f (registered 1.0582 / 0.14949)"
          % fit3(0.1689394678, 0.1588313831, 0.1555731855))

def do_census90():
    print("\n[claim 11] RELEASED 8-node bracket, N=240, cfl=0.2, n_roundtrips=90, seeds 1-8")
    ceiling = 1.30*Mth; vals = []
    for sd in range(1, 9):
        M, g = released_scan(240, 90, sd, 0.2); vals.append(M)
        print("    seed %d -> %-22r node7 growth %+.4e  all-negative: %s  %s"
              % (sd, M, g[7], all(x < 0 for x in g),
                 "" if M != M else "%.4f %% below ceiling" % (100*(ceiling-M)/ceiling)), flush=True)
    fin = [v for v in vals if v == v]
    print("    finite at %d/8 seeds ; nan at seeds %s ; ceiling %.11f"
          % (len(fin), [i+1 for i, v in enumerate(vals) if v != v], ceiling))
    print("    six-finite median %.10f (the eight-seed 0.1911620568 needs the WIDENED bracket)"
          % st.median(fin))

def do_cell(tag, N, cfl, i0, nrt=240, nseed=8):
    v = []
    for sd in range(1, nseed+1):
        M, cache = widened_scan(N, nrt, sd, cfl, i0); v.append(M)
        print("   %s seed %d -> %.10f  nodes %s" % (tag, sd, M, sorted(cache)), flush=True)
    v = sorted(v)
    print("   %s N=%d cfl=%.6f  median %.10f  sd %.3e  range %.3e"
          % (tag, N, cfl, st.median(v), st.pstdev(v), v[-1]-v[0]))

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if mode in ("validate", "all"): do_validate()
    if mode in ("bulk",     "all"): do_bulk()
    if mode in ("vn",       "all"): do_vn()
    if mode in ("analytic", "all"): do_analytic()
    if mode in ("corner",   "all"): do_corner()
    if mode in ("wp2",      "all"): do_wp2()
    if mode in ("ladder",   "all"): do_ladder()
    if mode in ("census90", "all"): do_census90()
    if mode == "cell": do_cell(sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]))
    if mode == "all":
        for tag, N, cfl, i0 in CELLS: do_cell(tag, N, cfl, i0)