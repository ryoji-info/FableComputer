# Specification of a pumped pair of resonant-tunnelling diodes at 225 GHz (for an independent rebuild)

All values are physical. Units: V, mA, ohm, fF, pH, ps. Nothing here is a measured device. The diode figures are fitted to published per-device figures of one 0.45-THz source; the rest are design choices.

## 1. One cell: a balanced pair

Two identical halves, called + and -, hang on one supply node S.

    clock source v_clk(t) -- R_b -- node S           node S -- C_b -- ground
    node S -- contact resistor rho -- junction -- pad P+        (the same for P-)
    pad -- C_p -- ground
    pad -- half winding (L_h, series R_L) -- grounded centre tap
    pad -- R_k -- stub node -- C_s -- ground        (the launcher current, where present, enters at the stub node)

- The junction is a capacitor C_d in parallel with a conduction current i_x. The junction voltage v_j is counted from the supply side to the pad side.
- Conduction current with a first-order delay: d i_x / dt = (frac * I_full(v_j) - i_x) / tau_d.
- The two half windings are coupled so that the mode with opposite currents in the two halves (the odd mode) sees L_odd = L_h (1 + k) per half and the mode with equal currents sees L_h (1 - k). With i_L counted from pad to tap: v_p(+) - R_L i_L(+) = L_h di_L(+)/dt - k L_h di_L(-)/dt, and the same with + and - exchanged.

Diode law of the full device (mA, with v = V / 1.667):

    I_full(V) = 0.9333 * [ A (sp(a) - sp(b)) (pi/2 + atan((C - n1 v) / D)) + H (exp(n2 v / VT) - 1) + 2.218 tanh(v / 0.05) ]
    a = (B - C + n1 v) / VT,   b = (B - C - n1 v) / VT,   sp(x) = ln(1 + exp(x)),   VT = 0.025852
    A = 3.541, B = 0.1002, C = 0.1480, D = 0.02606, n1 = 0.2882, n2 = 0.1843, H = 0.007984

It has a peak of about 25.4 mA near 0.75 V and a valley of about 11.4 mA near 1.30 V.

Common values: frac = 0.25 (each diode is a quarter of the full device), C_d = 2.5 fF, rho = 12 ohm, tau_d = 0.100 ps, k = 0.3, R_b = 2.5 ohm, C_b = 4.78 fF, R_k = 1 ohm, C_s = 0.7 fF.

Three candidate cells:

| Cell | C_p (fF) | L_odd per half (pH) | R_L (ohm) | Remark |
|---|---|---|---|---|
| B | 21.5 | 17.84 | 6.31 | tank 24 fF per half with the junction, quality factor 4 |
| D | 13.5 | 24.60 | 11.59 | tank 16 fF per half, quality factor 3 |
| F | 13.5 | 26.30 | 9.29 | tank 16 fF per half, quality factor 4 |

R_L stands for an inductor with a damping resistor. It is in series with the winding, so it also carries the diode's direct current.

## 2. Signal, clock, pump

- The signal of a pair is the odd-mode voltage: half the difference of the two stub-node voltages. The bit is its sign against a reference oscillation at the carrier frequency.
- Carrier f_d = 225.2 GHz. Pump at exactly 2 f_d = 450.4 GHz.
- The supply of a pair of clock depth d is

      v_clk(t) = V_s * win(t - d T / 4) * (1 + p cos(2 * 2 pi f_d t + pi (1 + d)))

  with period T = 69.28 ps. win is periodic with period T. It rises from 0 to 1 over 14.3 ps as a raised cosine centred on the start of the period, stays at 1, and falls in the same way centred on 0.75 T. So a pair is on for three quarters of every period, and the pump phase steps by half a turn from one clock depth to the next.
- V_s is the supply level and p the pump level (0.10 to 0.30).

## 3. A row

- Pairs 0 to 15 in a row; pair n has clock depth n.
- Neighbouring pairs are linked through their inductors only: a mutual inductance M = -0.06 * L_odd between the odd modes of the two pairs. In winding terms: the voltage across winding + of pair b gains 0.5 M (di_L(a,+)/dt - di_L(a,-)/dt), and winding - gains the negative of that, and the same from b to a.
- Pair 0 is driven: a current +I_s cos(2 pi f_d t) into its + stub node and -I_s cos(2 pi f_d t) into its - stub node, I_s = 0.4 mA, with the sign of I_s set by the bit of the slot. The drive of slot s is on from 0.25 T before pair 0's period starts until pair 0 switches off.
- Bit pattern: 1 0 1 1 0 0 1 0, repeated.
- A pair decides its sign while its supply comes on. Read the phase of each pair near the end of its on-time, and compare slots that carry a 1 with slots that carry a 0.

## 4. Spread and noise

- Inductance spread: each pair's L_odd is multiplied by 1 + 0.03 g, with g a standard normal number per pair.
- Noise at 353 K: thermal noise of every resistor and shot noise 2 q i_x of each diode's conduction current.
