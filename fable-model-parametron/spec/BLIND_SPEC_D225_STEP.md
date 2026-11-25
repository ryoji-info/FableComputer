# Second addendum to the specification of the pumped pair at 225 GHz: another step of the pump phase

Read `BLIND_SPEC_D225.md` and `BLIND_SPEC_D225_ADDER.md` first. Everything there holds except what is changed here. Units as there.

## 1. The change

The supply of a pair of clock depth d is now

    v_clk(t) = V_s * win(t - d T / 4) * (1 + p cos(2 * 2 pi f_d t + pi (q + 1.5 d)))

with q = 0.25. The pump phase now steps by three quarters of a turn from one clock depth to the next. In the two earlier documents it stepped by half a turn, pi (1 + d) and pi (q + d).

Nothing else changes: cell F, f_d = 225.2 GHz, T = 69.28 ps, a pair on for 0.75 T, edges of 14.3 ps, a link M = -0.06 * L_odd, a reversed link M = +0.06 * L_odd, drive I_s = 0.4 mA as specified, positive for a 1 and negative for a 0.

## 2. Layouts

**(a) The row of sixteen** of the first specification: pair n has clock depth n, pair 0 is driven, bit pattern 1 0 1 1 0 0 1 0, repeated.

**(b) The ten-pair adder** of the first addendum, in two variants.

- (b1) Its fourteen links as listed there.
- (b2) The same, but the link X3-C is a reversed link. Everything else as in (b1).

**(c) A twenty-pair adder with two rails.** Every signal exists on two pairs, a pair "t" that carries the bit and a pair "c" that carries its complement. No link is reversed: every link has M = -0.06 * L_odd.

| Pairs | Clock depth | Take their sign from |
|---|---|---|
| At, Bt | 0 | driven: operands a and b |
| Ac, Bc | 0 | driven: the complements of a and b (a 1 where the operand has a 0) |
| Ct, Cc | 0 | the loop, see below |
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

The loop is closed in one of two ways.

- (c1) Straight: links X3t-Ct and X3c-Cc.
- (c2) Crossed: links X3t-Cc and X3c-Ct.

That makes twenty-eight links in either variant. Pairs that share no link do not couple.

## 3. Operands

As in the first addendum, 32 slots:

    a: 0 1 1 1 0 1 1 0 0 1 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0
    b: 0 1 1 0 1 0 0 1 1 0 1 0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0 1 0 1 0 0

Leave slot 0 out of every count.

## 4. When a pair is read

As in the first addendum: read each pair's phase in a window of about one to a few carrier periods that starts a little after a quarter period into its on-time, and judge it there.

## 5. Spread and noise

As in the first specification: each pair's L_odd is multiplied by 1 + 0.03 g, with g a standard normal number per pair; noise at 353 K, thermal noise of every resistor and shot noise 2 q i_x of each diode's conduction current.
