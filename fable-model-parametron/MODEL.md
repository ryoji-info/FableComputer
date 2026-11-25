# The model

This file writes out the model that the package runs, from the code. Every value and every equation here is what `fdtd3.py`, `runs3.py`, `chain4.py` and `rtdiv.py` compute. Nothing in it has been built or measured. Resonant-tunnelling diode is abbreviated RTD below.

## 1. What is modelled

A pair is two RTDs on one supply node. Each diode feeds one end of a centre-tapped inductor whose tap is grounded, and a capacitor at each end sets the frequency. The pair is biased just below the level at which it would oscillate by itself. A pump at twice its carrier frequency is added to its supply. With the pump the pair oscillates, with its two ends in antiphase, on one of two phases half a turn apart. That phase is the bit. Such a circuit is a parametron.

Pairs are linked by a small mutual inductance between their inductors. A four-phase clock switches them on and off in turn, so that each pair takes its phase from the pairs switched on a quarter period before it. A pair with one link copies its input; a pair with three links takes their majority; a link of the opposite sign inverts.

The pump, the clock, the inputs and the outputs are ideal sources in the model. They are not circuits.

## 2. Units, and the change of units

The code works in V, mA, fF, nH, kohm, ps and um.

The design is a 225-GHz circuit. The model runs it with every time divided by K = 1.075 / 0.225 = 4.7778, and with it every capacitance and every inductance. Resistances, voltages, currents and the diode law stay as they are. Frequencies are K times higher: the carrier of 225.2 GHz becomes 1.076 THz in the model. The same numbers, read as physical values, describe a second circuit: the 1-THz-class cell. So the model's own units are the units of the 1-THz-class cell, and `r5_units.py` shows that a run in either set of units gives the same traces to rounding.

The noise needs one more factor. A capacitance K times larger has K times less kT/C noise power, and the shot-noise bandwidth is K times smaller. So the 225-GHz circuit at its own temperature is the model with every noise power multiplied by 1/K = 0.2093 (the setting key `scale`). With `scale` = 1 the model is the 1-THz-class cell at the same temperature, 4.78 times the noise power.

The values of the cell, called cell F in the design study:

| Quantity | 1-THz-class cell (model units) | 225-GHz circuit |
|---|---|---|
| Diode capacitance C_d | 0.5233 fF | 2.50 fF |
| Diode delay tau_d | 0.02093 ps | 0.100 ps |
| Contact rho, per diode | 12 ohm | 12 ohm |
| Pad capacitor C_p, per half | 2.826 fF | 13.50 fF |
| Tank per half, C_d + C_p | 3.349 fF | 16.0 fF |
| Odd-mode inductance per half, L_odd | 5.504 pH | 26.30 pH |
| Half winding L_h = L_odd / (1 + k) | 4.234 pH | 20.23 pH |
| Coupling of the half windings k | 0.3 | 0.3 |
| Damping resistor R_L, in series with each half | 9.294 ohm | 9.294 ohm |
| Supply resistor R_b | 2.5 ohm | 2.5 ohm |
| Supply node capacitance C_b | 1.0 fF | 4.78 fF |
| Coupler R_k (C_k infinite) | 1 ohm | 1 ohm |
| Stub, in all (4 sections) | 0.1333 fF, 1.333 pH | 0.637 fF, 6.37 pH |
| Mutual inductance of a link, 6 % of L_odd | 0.330 pH | 1.58 pH |
| Carrier; pump | 1.076 THz; 2.152 THz | 225.2 GHz; 450.4 GHz |
| Clock period T; edges E | 14.5 ps; 3.0 ps | 69.3 ps; 14.3 ps |
| Time step dt | 0.0025 ps | 0.0119 ps |

R_L is omega L_odd / Q with omega = 2 pi 1.075 rad/ps and Q = 4. The tank's quality factor of 4 is a design choice: the damping is deliberate. The values are frozen in `cellbase.py`, which says where each came from. `cellbase.py` also holds a pair tuned to a 160-GHz carrier (`CELL_160`, with its own time scale `K_160` = 1.075 / 0.160), which `r1_pair.py cell=c160` runs alone; no batch uses it.

## 3. One pair

The pair has two halves, + (index 0) and - (index 1), and one supply node b. Per half:

    clock source v_clk -- R_b -- node b;        node b -- C_b -- ground
    node b -- rho -- junction (C_d in parallel with the conduction current i_x) -- pad p
    pad p -- C_p -- ground
    pad p -- R_L -- half winding L_h -- grounded centre tap     (the windings of + and - are coupled by k)
    pad p -- R_k -- node A of the stub -- 4 sections of line -- node B of the stub
    the drive current i_B enters at node B, and the level is read at node B

R_b and C_b are shared by the two halves. The state per half is V_A (stub node A), v_p (pad), v_j (junction), i_L (winding current, from pad to tap), v_k (a coupler capacitor, which stays at 0 because C_k is infinite), i_x, and the stub currents I_0 to I_3 and voltages V_1 to V_4, with V_4 at node B. The pair adds v_b.

**The stub** is a lossless line: Z0 = 100 ohm, speed 150 um/ps in model units, length 2 um, Drude time 1e6 ps. Per unit length L' = Z0 / s and C' = 1 / (Z0 s). Each of its 4 sections has 0.333 pH and 0.0333 fF in model units. Node A carries half a section's capacitance and node B the other half. The stub is short: its one-way delay is 0.013 model ps. It acts as a small capacitance behind R_k, and node B, where the signal is read and driven, sits behind a further 1.33 pH. The batches used 4 sections (job argument `nseg=4`, the default of this package).

The **coupler** joins the pad to node A through R_k = 1 ohm alone. Its time constant, 1.7e-5 ps, is far below the time step, and the trapezoidal step maps it onto an eigenvalue of -0.974 per step: V_A - v_p alternates in sign from step to step. Its effect on decisions was not tested.

## 4. The diode

The current of the full device, in mA, with v = V / 1.667:

    a = (B - C + n1 v) / VT,     b = (B - C - n1 v) / VT,     sp(x) = ln(1 + e^x)
    J(V) = 0.9333 [ A (sp(a) - sp(b)) (pi/2 + atan((C - n1 v) / D)) + H (exp(n2 v / VT) - 1) + 2.218 tanh(v / 0.05) ]
    A = 3.541, B = 0.1002, C = 0.1480, D = 0.02606, n1 = 0.2882, n2 = 0.1843, H = 0.007984, VT = 0.025852 V

It has a peak of 25.39 mA at 0.750 V and a valley of 11.40 mA at 1.300 V. One diode of the pair carries area x jscale x J(v_j), with area = 0.25, so its peak is 6.35 mA. jscale is 1, times the spreads of section 10. The law is set by the job argument `iv` (default 0.9333,1.667,2.218, as in every batch).

The conduction current follows the law with a first-order delay. Within a step v_j is held at its old value:

    i_x(n+1) = i_x(n) + (area jscale J(v_j(n)) - i_x(n)) (1 - exp(-dt / tau_d))

and the mid-step value (i_x(n) + i_x(n+1)) / 2 enters the junction equation.

## 5. The equations of a half

    C_A dV_A/dt = (v_p - V_A - v_k) / R_k - I_0
    C_p dv_p/dt = (V_A - v_p + v_k) / R_k + (v_b - v_j - v_p) / rho - i_L
    C_d dv_j/dt = (v_b - v_j - v_p) / rho - i_x
    di_L,h/dt   = sum over windings w of G(h, w) (v_p,w - R_L,w i_L,w)
    dv_k/dt     = 0                                              (C_k infinite)
    C_b dv_b/dt = (v_clk - v_b) / R_b - sum over both halves of (v_b - v_j - v_p) / rho

G is the inverse of the inductance matrix of the windings. Inside a pair that matrix is [[L_h, -k L_h], [-k L_h, L_h]], so the odd mode (opposite currents) sees L_h (1 + k) = L_odd per half and the even mode sees L_h (1 - k). In model units G(+, +) = 259.6 /nH and G(+, -) = 77.9 /nH.

The stub, for sections k = 0 to 3:

    L_seg dI_k/dt = -(V_k+1 - V_k) - (L_seg / tau) I_k
    C_seg dV_k/dt = I_k-1 - I_k                    (inner nodes)
    C_B dV_B/dt   = I_3 + i_B                      (node B)

C_B is the capacitance matrix of all node B ends of a run. In the design it is diagonal: each node B carries half a section. Section 6 describes the optional capacitors that make it full.

## 6. Links

A link of a layout is a triple (i, j, sign). It is a **mutual inductance between the odd modes** of pairs i and j:

    M_oo = mk0 sqrt(L_odd,i L_odd,j),      mk0 = km x sign  (key kmsg = 1)   or   mk0 = km  (kmsg = 0)

with km = -0.06 in the design, so M = -0.330 pH in model units (-1.58 pH in the 225-GHz circuit). A reversed link has +0.06 and inverts the bit. Single-rail layouts use kmsg = 1. Dual-rail layouts have only links of sign +1, so kmsg does not matter there. Winding + of j and winding + of i share 0.5 M_oo; winding + of j and winding - of i share -0.5 M_oo; and so on with the signs of an odd mode. With spreads, the L_odd in the formula are the spread values.

The inductance matrix of all windings of a run is inverted once, in double precision. Its blocks inside a pair enter the implicit step. The blocks between pairs, Goff, enter as an explicit source in di_L/dt, taken at mid-step by extrapolation from the last two steps:

    w = v_p - R_L i_L,      w_mid = 1.5 w(n) - 0.5 w(n-1) + e_L,      source += Goff w_mid

(e_L is the thermal noise of R_L, section 9).

**The capacitor cc is not part of the design.** The setting key `cc` (default 0) adds a capacitor of cc between the node B ends of every pair of linked pairs, + to + and - to - for sign +1 and crossed for sign -1. It also pads every node B to ground by (deg_max - deg) cc, so that each carries deg_max cc in all, where deg is the number of links of its pair and deg_max the largest in the layout. The batches of the paper (named `chain_g*`) have cc = 0. Older batches (named `chain_d*`) ran with cc = 0.02 model fF (0.096 fF in the 225-GHz circuit) by an oversight. Older texts of the study that describe link capacitors or "gaps" as part of the design describe that state. `r4_serial_adder.py` shows what cc = 0.02 does: it lowers the weakest level of the serial adder by about 3 % at 0.94 V and by about 26 % at 1.015 V.

The keys `kst`, `kstsg`, `km2`, `keo`, `kx`, `kxe` and `kxd` add stray couplings between pairs; all are 0 at the operating point.

## 7. Supply, clock, pump and drive

The edge function, with E = 3.0 model ps:

    R(x) = 0.5 - 0.5 cos(pi clip(x / E + 0.5, 0, 1))

A pair at clock depth d has the clock phase phi = d / 4 (plus the timing spread of section 10). With tau = T frac(t / T - phi), its window is

    w(t) = R(tau) - R(tau - delta T) + R(tau - T)

with T = 14.5 model ps and delta = 0.75 (key `duty`). The supply rises centred at the start of the pair's period and falls centred at delta T. The pump phase of the pair is

    theta = pi (pph + pstep d)

with pph = 0.25 and pstep = 1.5. So the pump phase steps by three quarters of a turn from one clock phase to the next, which is 135 degrees of carrier phase. With this step the seed that a link carries lands on the axis of the pair that receives it. The supply of the pair is

    v_clk(t) = V min(1, t / 3) w(t) (1 + p cos(2 (2 pi f_d) t + theta))

with V = 0.94 V, p = 0.25 and f_d = 1.076 model THz. The factor min(1, t / 3) is a start ramp over the first 3 model ps. The keys `pgate` = 1 and 2 select other ways of gating the pump; they are not used at the operating point.

**Drive.** An input pair has a sequence of bits. With u = t / T + 0.25 and s = floor(u), the drive is on when 1 <= s <= n_slots and u - s < 0.25 + delta, so over [(s - 0.25) T, (s + delta) T). Then

    i_B,+(t) = +I_s beta_s cos(2 pi f_d t),     i_B,-(t) = -i_B,+(t),     I_s = 0.4 mA

with beta_s = +1 for a 1 and -1 for a 0 (phase keying, mode `psk`), the bit being that of slot s - 1. The drive switches on and off without a ramp. Its phase is fixed, so the phase of the input against the pump is set through pph. Each pattern runs once per run.

**Run length.** A run lasts max(n_slots + 3.5, n_slots + 2 + d_max / 4) T. Every variable starts at zero at t = 0. There is no start kick: a run without noise starts from the drive alone.

## 8. The integrator

The time step is 0.0025 model ps (0.0119 ps in the 225-GHz circuit); the Courant number of the stub is 0.75. Within a step:

1. Stub currents from the old voltages, with Crank-Nicolson loss: I(n+1/2) = ((1 - alpha) I - (dt / L_seg) dV) / (1 + alpha), alpha = dt / (2 tau). Stub noise is added.
2. Inner stub nodes from the new currents.
3. Node B ends: V_B(n+1) = V_B(n) + dt C_B^-1 (I_3(n+1/2) + i_B(t_n+1)).
4. The diode current by the delay of section 4.
5. The clock at mid-step: (v_clk(t_n+1) + v_clk(t_n)) / 2.
6. Sources: -I_0(n+1/2) / C_A, -i_x,mid / C_d, v_clk,mid / (R_b C_b), the noise, and the inductive source between pairs.
7. The trapezoidal step of the eleven lumped variables of a pair: y(n+1) = (1 - dt M / 2)^-1 [(1 + dt M / 2) y(n) + dt src].

**Precision.** The numpy backend, the default of this package, runs everything in double precision. The torch backend runs the state, the step matrices, C_B^-1, the noise and the reader's sums in single precision. The inductance inverse is formed in double precision and cast. The reader's 4 x 4 solve is in double precision on both. Stored levels and phases are single precision on both. The reported batches ran on torch, on a graphics processor.

**Convergence.** Four stored batches of the paper repeat a batch at half the time step (dt = 0.00125 model ps), with the same settings and the same draws of the spreads, all without link capacitors: g29b against g29 (a row of sixteen at 0.88, 0.94 and 1.015 V), g29c against g29 (the same, with 8 stub sections instead of 4), g30b against g30 (the serial adder at 0.94 V) and g38b against g38a (the serial adder at 0.985, 1.000 and 1.015 V, with physical noise, on a processor in double precision). Over the counted slots (slot 1 and up) and the levels L, LL and LE of the reference runs, halving the step changes a level by at most 1.0 mV (1.3 %, the row at 0.88 V) in g29b and g29c, by at most 0.47 mV (0.22 %) in g30b and by at most 2.5 mV (1.3 %, at 1.015 V) in g38b. Phases change by at most 0.3 degree in g29b, g29c and g30b, and 1.4 degrees in g38b. In the runs with a spread and no noise of g29b and g29c, levels change by at most 3.2 mV (1.3 %, at 1.015 V) and phases by at most 1.05 degrees. No decision of these runs turns: no phase PE moves by more than 90 degrees. Read at the decision alone (LE and PE), which is the reading the paper quotes, the runs with a spread and no noise change by at most 0.19 degree and 0.1 % at 0.94 V, by at most 2.4 % in level at 0.88 V, where the levels are lowest, and by at most 1.0 % and 1.04 degrees at 1.015 V. (Runs with noise are not compared run by run, since a different step draws different noise.) The figures are computed from the stored arrays, which are not in the package; `runs/MANIFEST.json` holds their checksums. A larger figure, up to 13 % in the level of single pairs at 1.015 V, comes from the older batches with the link capacitors (`chain_d*`, the design report of the session, which is not in this package). It does not describe the paper's batches.

## 9. Noise

Temperature 353 K. Every source is white over one step; the common factor `scale` multiplies the power of every source (section 2). In the 225-GHz circuit (scale = 1/K) the per-step amplitudes of cell F are:

- Coupler R_k: sigma_v = sqrt(2 kB T R / dt) sqrt(scale) = 0.903 mV. It enters as e / R_k into node A and out of the pad.
- Contact rho: 3.13 mV, as a current e / rho into the pad and the junction and out of node b.
- Damping resistor R_L: 2.75 mV, a series voltage e_L in each winding, through G and Goff.
- Supply resistor R_b: 1.43 mV, as e / (R_b C_b) in dv_b/dt.
- Stub loss: sigma_I = sqrt(2 kB T dt / (L_seg tau)) sqrt(scale) = 3.9e-6 mA per section. Negligible.
- Shot noise of the conduction current: a charge step dq = sqrt(fano q |i_x| dt scale), with fano = 1, after the update of i_x. It gives the junction a jump of -dq g / C_d, g standard normal. At 5 mA dq = 6.5e-19 C and the jump is 1.24 mV.

One noise generator serves a batch (key `seed`, default 5). The two backends use different generators and so draw different noise. Draws are made per row of the batch, the reference runs included, so a run's draws depend on its place in the batch.

## 10. Spreads

All spreads are standard normal draws g, unbounded, one per run and pair unless stated, and zero in the reference run. The generators are numpy on both backends, from `pseed` (default 11).

- Inductance, `lsig`: L_odd times (1 + lsig g); both halves alike; L_h, L_even and the mutual inductances follow.
- Diode current, `jsig`: jscale times (1 + jsig g), both diodes alike.
- Difference inside a pair, `jpair`: the + diode times (1 + 0.5 jpair g), the - diode times (1 - 0.5 jpair g).
- Pump phase from pair to pair, `psig`: added to theta, in radians of pump phase. "10 degrees" is psig = 0.1745, which is 5 degrees of carrier phase.
- Pump phase of a clock phase, `pline`: four values per run, one per depth modulo 4, added to theta.
- Pump level, `asig`: p times (1 + asig g).
- Link strength, `ksig`: mk0 of every magnetic link times (1 + ksig g), per run and link. cc is not spread.
- Clock timing, `tsig`: phi shifted by tsig g periods; both edges move, the pump does not.
- Supply level, `vsig`: V times (1 + vsig g); the pump is relative and scales with it.
- Damping resistor, `rsig`: R_L times (1 + rsig g), both halves alike.

## 11. Layouts

A layout is a list of links (i, j, sign), a clock depth per pair, the input pairs with their bit sequences, and the outputs. A pair takes inputs only from pairs of depth d - 1 modulo 4. The job argument `ncell` sets the number of pairs of a run, and a layout exists only when its number of pairs equals it.

- **Row of n** (`row`): links (k, k+1, +1), depth k, input pair 0 with the pattern 1 0 1 1 0 0 1 0 (8 slots).
- **Ripple-carry adder of n bits on one rail** (`radd<n>`): stage i has M_i = majority(A_i, B_i, C_i), the carry; G_i = majority(A_i, B_i, not C_i); K_i = C_i, a buffer; S_i = majority(not M_i, G_i, K_i), the sum bit; and C_(i+1) = M_i, a buffer. A_i and B_i reach depth 2 i through rows of buffer pairs. The four-bit adder has 53 pairs and 68 links, 8 of them reversed; the eight-bit adder has 169 pairs. The operands are fixed 32-slot pseudo-random sequences.
- **The same on two rails** (`rdd<n>`): every signal on a pair "t" and a pair "c" for its complement; no link is reversed; 106 pairs for four bits.
- **Serial adder with a stored carry** (`sadd`, 10 pairs, one rail; `sdadd`, 20 pairs, two rails): the full adder of one stage, with the carry M going round a loop of four pairs M, X2, X3, C, one per clock phase, so that C carries the carry of the slot before. With the pump step of three quarters of a turn a bit carried once round such a loop comes back inverted. So the "x" forms reverse the link X3 to C (one rail) or cross it between the rails (two rails, `sdaddx`, the form the paper uses).
- **Accumulator of W bits** (`sacc<W>`, `sdacc<W>` and their "x" forms): the serial adder with its carry cleared at the start of every word and its sum fed back through 4 W - 4 buffer pairs; `sdacc8x` has 84 pairs.

**Expected bits.** Rows copy the input pattern. Ripple-carry adders read the links as gates. Layouts with a loop use the rule of `expected_seq`: in slot s, a pair of depth d reads an input of depth d' in slot s + floor((d - d' - 1) / 4), which is an earlier slot when the link closes a loop, and takes the majority of the defined inputs. A bit is undefined when that slot lies before slot 0 or the defined inputs tie, and undefined bits are left out of every count.

## 12. Reading

The signal of a pair is half the difference of its two node B voltages. It is fitted over windows of 1 model ps (400 steps, 4.78 ps in the 225-GHz circuit) with [1, tau, cos 2 pi f_ref t, sin 2 pi f_ref t], f_ref = 1.076 (job argument `f`). Level = hypot(c, s), phase = atan2(-s, c). For slot j and pair k let t0 = (j + 1 + d_k / 4) T. The runner stores per run, slot and pair:

- L, the largest level of the windows that start at or after t0 + 2 and end at or before t0 + delta T - 1 (the flat top); LL and PH, the level and phase of the last of them; PH2, the phase of the one before.
- LE and PE, the level and phase of the first window that starts at or after t0 + T / 4 + 1: just after the next clock phase has come on, when the pairs fed by this one take their decision.

Run 0 of each setting is the reference run, without noise or spread.

**Rules** (`analysis.py`, `refcheck.py`):

- Slot 0 is left out everywhere: it follows a clock cycle without data.
- A pair of the reference run is right when every counted slot has the expected sign on its own axis: axis = sum over slots of e_s z_s, with e = +1 or -1 for the expected bit and z the phasor, and right if every e_s Re(z_s conj(axis)) > 0. Rows check this with LL and PH (the end of the on-time); gates and layouts with state check it with LE and PE.
- A decision is wrong when Re exp(i (PE_noisy - PE_ref)) < 0: its phase lies more than 90 degrees from the reference run's.
- A row holds when all reference pairs 1 to n-1 are right, no decision at pair n-2 is wrong, and the rms phase difference at pair n-2 over runs and slots is at most 8 degrees.
- An addition of a ripple-carry adder is wrong when any output pair is wrong in that slot. In the serial adder a sum bit is wrong when St is wrong, and a sum (a run of 31 bits) is wrong when any of its bits is.

When the key `fd` differs from f_ref, the analysis takes out the turn a tone at fd makes against the reader.

## 13. Against the stand-alone specification

`BLIND_SPEC_T1.md` of the study specifies the same circuit in the units of the 1-THz-class cell, for codes written without this one. The model differs from it in these points:

- The specification has one stub node with C_s = 0.1465 fF to ground, where the signal is read and the drive enters. The model has a line of 4 sections, 0.133 fF and 1.33 pH in all, read and driven at its far end.
- The specification gives L_odd = 5.5047 pH; cell F has 5.5037 pH.
- The specification repeats the bit pattern of the row; the model runs it once.
- The model has the start ramp min(1, t / 3), which the specification does not mention.
- The specification asks for a reading window of one to a few carrier periods starting a little after a quarter period into the slot; the model reads 1-model-ps windows by the rules above.

Two other codes, one written from the specification of the 225-GHz design and its addenda (`spec/BLIND_SPEC_D225*.md`) and one from this one, give the weakest level of the serial adder without the link capacitors within about 2 % of this model at 0.94, 0.985, 1.000 and 1.015 V. The values, in mV, without noise or spread, read in the common way of the session's comparison of codes (reading (b) of `r4_serial_adder.py`):

| Supply level | 0.940 V | 0.985 V | 1.000 V | 1.015 V |
|---|---|---|---|---|
| This model, cc = 0 | 205.1 | 252.7 | 262.2 | 266.5 |
| Second code (`independent/second_code/rebuild18b`) | 200.9 | 250.8 | 260.9 | 263.9 |
| Third code (`independent/third_code/rebuild_t1x`, its own window of the same length) | 202 | 251 | 261 | 263 |

They come from the session's record of the comparison, which is not in this package. `r4_serial_adder.py` recomputes this model's values at 0.94 and 1.015 V; no listing recomputes those at 0.985 and 1.000 V. The largest difference is 2.1 %, at 0.94 V against the second code.

## 14. What the model leaves out

The pump source, the clock source, the drive and the output reading are ideal. There is no model of the wiring that would carry the pump and the clock, of the contacts, or of heating. The in-phase mode of a pair is integrated but not read by the analysis. The diode law is a fitted form, scaled to published per-device figures; the diode delay and the contact are assumptions. Every result of the package is a result of this model.
