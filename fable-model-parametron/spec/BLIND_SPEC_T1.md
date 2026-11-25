# Specification of a logic fabric of pumped pairs of resonant-tunnelling diodes at a 1.076-THz carrier (for an independent rebuild)

This document stands alone. All values are physical values of the circuit to be simulated. Units: V, mA, ohm, fF, pH, ps. Nothing here is a measured device.

## 1. One cell: a balanced pair

Two identical halves, called + and -, hang on one supply node S.

    clock source v_clk(t) -- R_b -- node S           node S -- C_b -- ground
    node S -- contact resistor rho -- junction -- pad P+        (the same for P-)
    pad -- C_p -- ground
    pad -- half winding (L_h, series R_L) -- grounded centre tap
    pad -- R_k -- stub node -- C_s -- ground        (a drive current, where present, enters at the stub node)

- The junction is a capacitor C_d in parallel with a conduction current i_x. The junction voltage v_j is counted from the supply side to the pad side.
- Conduction current with a first-order delay: d i_x / dt = (frac * I_full(v_j) - i_x) / tau_d.
- The two half windings are coupled. The mode with opposite currents in the two halves (the odd mode) sees L_odd = L_h (1 + k) per half, and the mode with equal currents sees L_h (1 - k). With i_L counted from pad to tap: v_p(+) - R_L i_L(+) = L_h di_L(+)/dt - k L_h di_L(-)/dt, and the same with + and - exchanged.

Diode law of the full device (mA, with v = V / 1.667):

    I_full(V) = 0.9333 * [ A (sp(a) - sp(b)) (pi/2 + atan((C - n1 v) / D)) + H (exp(n2 v / VT) - 1) + 2.218 tanh(v / 0.05) ]
    a = (B - C + n1 v) / VT,   b = (B - C - n1 v) / VT,   sp(x) = ln(1 + exp(x)),   VT = 0.025852
    A = 3.541, B = 0.1002, C = 0.1480, D = 0.02606, n1 = 0.2882, n2 = 0.1843, H = 0.007984

It has a peak of about 25.4 mA near 0.75 V and a valley of about 11.4 mA near 1.30 V.

Values of the cell:

| Quantity | Value |
|---|---|
| frac | 0.25 (each diode is a quarter of the full device) |
| C_d | 0.5233 fF |
| rho | 12 ohm |
| tau_d | 0.02093 ps |
| C_p | 2.8256 fF |
| L_odd per half | 5.5047 pH |
| k | 0.3 |
| R_L | 9.29 ohm, in series with each half winding; it also carries the diode's direct current |
| R_b | 2.5 ohm |
| C_b | 1.000 fF |
| R_k | 1 ohm |
| C_s | 0.1465 fF |

## 2. Signal, clock, pump

- The signal of a pair is the odd-mode voltage: half the difference of the two stub-node voltages. The bit is its sign against a reference oscillation at the carrier frequency.
- Carrier f_d = 1.076 THz, so one carrier period is 0.92937 ps. Pump at exactly 2 f_d = 2.152 THz.
- Every pair has a clock depth d, a whole number from 0 upward. The supply of a pair of clock depth d is

      v_clk(t) = V_s * win(t - d T / 4) * (1 + p cos(2 * 2 pi f_d t + pi (q + 1.5 d)))

  with period T = 14.50 ps and q = 0.25. win is periodic with period T. It rises from 0 to 1 over 3.0 ps as a raised cosine centred on the start of the period, stays at 1, and falls in the same way centred on 0.75 T. So a pair is on for three quarters of every period, and the pump phase steps by three quarters of a turn from one clock depth to the next.
- V_s is the supply level and p the pump level. The nominal point is V_s = 0.94 V and p = 0.25.
- Slot s of a pair of clock depth d is the period that starts at t = s T + d T / 4.

## 3. Links and drives

- A link joins two pairs through their inductors only: a mutual inductance M = -0.06 * L_odd between the odd modes of the two pairs. In winding terms: the voltage across winding + of pair b gains 0.5 M (di_L(a,+)/dt - di_L(a,-)/dt), winding - gains the negative of that, and the same from b to a. A reversed link has M = +0.06 * L_odd.
- Pairs that share no link do not couple.
- A driven pair gets a current +I_s cos(2 pi f_d t) into its + stub node and -I_s cos(2 pi f_d t) into its - stub node, with I_s = 0.4 mA, positive for a 1 and negative for a 0. The drive of slot s is on from 0.25 T before the pair's slot starts until the pair switches off.
- What a layout is meant to do: a pair with one link into it copies the sign of the pair before it, and through a reversed link it takes the opposite sign. A pair with three links into it takes the majority. A pair takes its sign while its supply comes on, from the pairs whose clock depth is one less.

## 4. Layouts

**(a) A row of sixteen.** Pairs 0 to 15; pair n has clock depth n and is linked to pair n + 1. Pair 0 is driven with the bit pattern 1 0 1 1 0 0 1 0, repeated.

**(c) A bit-serial adder on two rails, twenty pairs.** Every signal exists on two pairs, a pair "t" that carries the bit and a pair "c" that carries its complement. No link is reversed.

| Pairs | Clock depth | Take their sign from |
|---|---|---|
| At, Bt | 0 | driven: operands a and b |
| Ac, Bc | 0 | driven: the complements of a and b |
| Ct, Cc | 0 | the loop: links X3t-Cc and X3c-Ct |
| Mt | 1 | At, Bt, Ct |
| Mc | 1 | Ac, Bc, Cc |
| Gt | 1 | At, Bt, Cc |
| Gc | 1 | Ac, Bc, Ct |
| Kt | 1 | Ct |
| Kc | 1 | Cc |
| St | 2 | Mc, Gt, Kt |
| Sc | 2 | Mt, Gc, Kc |
| X2t | 2 | Mt |
| X2c | 2 | Mc |
| X3t | 3 | X2t |
| X3c | 3 | X2c |
| Ft | 3 | St |
| Fc | 3 | Sc |

That makes twenty-eight links. Ct has clock depth 0, so in every period it starts a quarter period after X3 has started. The meaning: M is the carry, majority(a, b, c); it goes round the loop and is the c of the next slot. S is the sum bit. With the operands entering least significant bit first, one bit per slot, the stream at St should be the sum of the two operand streams read as numbers. Operands, 32 slots:

    a: 0 1 1 1 0 1 1 0 0 1 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0
    b: 0 1 1 0 1 0 0 1 1 0 1 0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0 1 0 1 0 0

Slot 0 has a = b = 0, which clears the carry.

**(r) A four-bit ripple-carry adder on one rail, fifty-three pairs.** It adds two four-bit numbers and a carry-in in every slot.

- C_0 is a driven pair of clock depth 0 that carries the carry-in.
- For each bit i = 0, 1, 2, 3 there are two driven pairs of clock depth 0 that carry the operand bits a_i and b_i. Each is followed by a row of 2 i buffer pairs of clock depths 1 to 2 i, each linked to the one before. The last pair of each row is called A_i or B_i and has clock depth 2 i. For i = 0 there is no buffer and the driven pairs themselves are A_0 and B_0.
- Stage i has five pairs:

| Pair | Clock depth | Takes its sign from |
|---|---|---|
| M_i | 2 i + 1 | A_i, B_i, C_i |
| G_i | 2 i + 1 | A_i, B_i, and C_i through a reversed link |
| K_i | 2 i + 1 | C_i |
| S_i | 2 i + 2 | M_i through a reversed link, G_i, K_i |
| C_(i+1) | 2 i + 2 | M_i |

- That makes 1 + (2 + 6 + 10 + 14) + 4 * 5 = 53 pairs and 68 links.
- The meaning: M_i is the carry out of bit i and S_i is the sum bit. S_0 to S_3 and C_4 together are the five-bit sum of the two numbers and the carry-in. Slot s of each output pair, counted by its own clock depth, belongs to the operands of slot s.
- Operands, 32 slots each:

      c0: 1 0 0 1 1 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0
      a0: 0 1 1 1 0 1 0 1 1 0 1 1 0 0 0 0 1 1 0 1 0 0 1 1 0 1 1 0 0 1 0 1
      b0: 0 1 1 0 0 0 0 0 0 0 1 1 1 1 0 0 1 1 1 1 0 0 1 0 0 1 1 0 0 1 1 0
      a1: 1 0 1 1 1 1 0 0 0 1 1 0 0 0 1 0 0 1 1 0 1 1 0 0 1 0 0 0 1 0 1 1
      b1: 1 1 1 0 1 1 1 1 1 1 1 0 0 1 1 0 0 1 0 0 1 0 0 0 0 1 1 1 1 0 0 0
      a2: 1 1 1 1 0 0 1 1 0 1 1 0 1 1 0 0 0 1 1 1 0 1 1 0 1 0 0 1 0 1 0 1
      b2: 0 0 1 0 0 1 0 0 1 0 1 0 1 0 0 0 0 1 0 1 1 1 1 1 0 0 0 1 0 0 1 0
      a3: 0 1 1 1 1 0 0 0 1 0 1 1 0 1 0 0 1 1 1 0 0 1 0 1 1 1 1 0 0 0 1 1
      b3: 1 0 1 0 1 0 0 1 0 1 1 1 0 0 1 0 1 1 0 1 0 1 0 0 1 0 0 0 1 1 0 0

Leave slot 0 out of every count in every layout.

## 5. When a pair is read

A pair matters at the moment the pairs after it take their decision. Read each pair's phase in a window of about one carrier period to a few carrier periods that starts a little after a quarter period into its slot, and judge it there. Later in its on-time a pair with several links is pulled by the pairs it feeds.

## 6. Spread and noise

- Inductance spread: each pair's L_odd is multiplied by 1 + 0.03 g, with g a standard normal number per pair.
- Noise at 353 K: the thermal noise of every resistor, and the shot noise of each diode's conduction current, with the full shot-noise power 2 q i_x.
