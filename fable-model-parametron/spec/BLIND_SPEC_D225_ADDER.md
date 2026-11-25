# Addendum to the specification of the pumped pair at 225 GHz: a bit-serial adder with a stored carry

Read `BLIND_SPEC_D225.md` first. Everything there holds, with these settings and this layout. Units as there.

## 1. Settings

- Cell F. Supply level V_s = 0.94 V. Pump level p = 0.25.
- Clock as specified: period T = 69.28 ps, a pair on for 0.75 T, edges of 14.3 ps.
- Pump phase of a pair of clock depth d: the supply is

      v_clk(t) = V_s * win(t - d T / 4) * (1 + p cos(2 * 2 pi f_d t + pi (q + d)))

  with q = 0.25. (The first specification had q = 1. The value of q sets how the drive of the input pairs lies against the pump.)
- Drive of an input pair: as specified for pair 0 of the row. A current +I_s cos(2 pi f_d t) into its + stub node and -I_s cos(2 pi f_d t) into its - stub node, I_s = 0.4 mA, positive for a 1 and negative for a 0. The drive of slot s is on from 0.25 T before the pair's period starts until the pair switches off.

## 2. Layout: ten pairs

| Pair | Name | Clock depth | Takes its sign from |
|---|---|---|---|
| 0 | A | 0 | driven: operand a |
| 1 | B | 0 | driven: operand b |
| 2 | C | 0 | X3 |
| 3 | M | 1 | A, B, C |
| 4 | G | 1 | A, B, and C through a reversed link |
| 5 | K | 1 | C |
| 6 | S | 2 | M through a reversed link, G, K |
| 7 | X2 | 2 | M |
| 8 | X3 | 3 | X2 |
| 9 | F | 3 | S |

- A link is the mutual inductance of the first specification between the odd modes of the two pairs, M = -0.06 * L_odd. A reversed link has M = +0.06 * L_odd.
- There are fourteen links: A-M, B-M, C-M, A-G, B-G, C-G (reversed), C-K, M-S (reversed), G-S, K-S, M-X2, X2-X3, X3-C, S-F. Pairs that share no link do not couple.
- The link X3-C closes a loop of four pairs, C, M, X2, X3, one in each clock phase. C has clock depth 0, so in every period it starts a quarter period after X3 has started.

## 3. What the layout is meant to do

- A pair with one link into it copies the sign of that pair; through a reversed link it takes the opposite sign. A pair with three links into it takes the majority.
- M = majority(a, b, c) is the carry. It goes round the loop and is the c of the next slot.
- S = majority(not M, G, K) with G = majority(a, b, not c) and K = c. That is the sum bit a xor b xor c.
- So with the operands entering least significant bit first, one bit per slot, the stream at S should be the sum of the two operand streams read as numbers.

## 4. Operands: 32 slots

    a: 0 1 1 1 0 1 1 0 0 1 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0
    b: 0 1 1 0 1 0 0 1 1 0 1 0 1 0 0 1 0 1 1 0 1 0 0 0 1 0 0 1 0 1 0 0

- Slot 0 has a = b = 0, which clears the carry whatever the loop held before.
- In slots 3 to 10 the two operand bits differ, so the loop must keep a 1 for eight slots. In slots 12 to 19 it must keep a 0.
- Leave slot 0 out of every count.

## 5. When a pair is read

A pair matters at the moment the pairs after it take their decision. Read each pair's phase in a window of about one carrier period to a few carrier periods that starts a little after a quarter period into its on-time, and judge it there. Later in its on-time a pair with several links is pulled by the pairs it feeds.
