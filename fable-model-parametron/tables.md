# Tables of results

Rebuilt by `tables.py` from the stored runs in `runs/`. Every number is in-model. Only runs without link capacitors. A row of sixteen "holds" when every pair from 1 on is right without noise or spread, no decision at pair 14 is wrong and the rms phase error there is at most 8 degrees. A decision is wrong when its phase, read when the next pair decides, lies more than 90 degrees from that of the run without noise or spread. Slot 0 is left out of every count. A run is one draw of the spreads with its own noise.

## T-1. Rows of sixteen at the operating point

| condition | pairs right without noise or spread | runs | first-wrong events in decisions at risk | batch |
|---|---|---|---|---|
| no spread, no noise | 16 of 16 | 1 | 0 in 105 | g29 |
| inductance spread 3 %, no noise | 16 of 16 | 32 | 0 in 3,360 | g29 |
| inductance spread 3 %, physical noise | 16 of 16 | 32 | 0 in 3,360 | g29 |
| inductance spread 3 %, no noise, 0.880 V | 16 of 16 | 32 | 0 in 3,360 | g29 |
| inductance spread 3 %, no noise, 1.015 V | 16 of 16 | 32 | 0 in 3,360 | g29 |

0.94 V, 25 % pump, links 6 %, unless the line says otherwise. A first-wrong event is the first pair of a slot of a run, counted from pair 1, that is wrong. The decisions at risk are those up to that pair. Pairs right are read in the last window of the on-time, decisions when the next pair decides (an_count.py).

## T-2. Rows of sixteen: single tolerances and spreads

| what was varied | value | pairs right without noise or spread | rms phase error at pair 14 (deg) | wrong decisions at pair 14 | first-wrong events in decisions at risk | level at pair 14 (mV) | holds | batch |
|---|---|---|---|---|---|---|---|---|
| base | as designed, no spread | 16 of 16 | 0.3 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| base | as designed, inductance spread 3 % | 16 of 16 | 2.7 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| input phase against the pump, all pairs alike | -0.500 pi | 16 of 16 | 2.8 | 0 of 224 | 0 in 3,360 | 188 | yes | g28a |
| input phase against the pump, all pairs alike | -0.250 pi | 16 of 16 | 3.0 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| input phase against the pump, all pairs alike | +0.250 pi | 16 of 16 | 3.6 | 0 of 224 | 0 in 3,360 | 188 | yes | g28a |
| input phase against the pump, all pairs alike | +0.500 pi | 16 of 16 | 3.0 | 0 of 224 | 0 in 3,360 | 188 | yes | g28a |
| pump phase error from pair to pair | 10 degrees rms | 16 of 16 | 5.4 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| pump phase error from pair to pair | 20 degrees rms | 16 of 16 | 11.2 | 0 of 224 | 0 in 3,360 | 189 | no | g28a |
| pump phase error from pair to pair | 30 degrees rms | 16 of 16 | 14.9 | 0 of 224 | 0 in 3,360 | 189 | no | g28a |
| pump phase error from pair to pair | 45 degrees rms | 16 of 16 | 58.2 | 25 of 224 | 29 in 3,117 | 189 | no | g28a |
| pump phase error from pair to pair | 60 degrees rms | 16 of 16 | 86.2 | 61 of 224 | 78 in 2,872 | 189 | no | g28a |
| pump level error from pair to pair | 20 % rms | 16 of 16 | 3.3 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| pump level error from pair to pair | 30 % rms | 16 of 16 | 7.2 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| link strength | 2.0 % | 16 of 16 | 2.5 | 0 of 224 | 0 in 3,360 | 194 | yes | g28a |
| link strength | 3.0 % | 16 of 16 | 3.1 | 0 of 224 | 0 in 3,360 | 193 | yes | g28a |
| link strength | 4.5 % | 16 of 16 | 2.9 | 0 of 224 | 0 in 3,360 | 191 | yes | g28a |
| link strength | 7.5 % | 16 of 16 | 4.2 | 0 of 224 | 0 in 3,360 | 186 | yes | g28a |
| link strength | 9.0 % | 16 of 16 | 3.5 | 0 of 224 | 0 in 3,360 | 182 | yes | g28a |
| link strength | 12.0 % | 16 of 16 | 3.1 | 0 of 224 | 0 in 3,360 | 173 | yes | g28a |
| link strength error from link to link | 10 % rms | 16 of 16 | 3.2 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| link strength error from link to link | 20 % rms | 16 of 16 | 3.5 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| link strength error from link to link | 30 % rms | 16 of 16 | 4.0 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| inductance spread | 5 % | 16 of 16 | 5.6 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| inductance spread | 6 % | 16 of 16 | 6.1 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| inductance spread | 8 % | 16 of 16 | 9.1 | 0 of 224 | 0 in 3,360 | 189 | no | g28a |
| inductance spread | 10 % | 16 of 16 | 13.0 | 0 of 224 | 0 in 3,360 | 189 | no | g28a |
| diode spread | current 10 % from pair to pair | 16 of 16 | 2.7 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| diode spread | difference inside a pair 5 % | 16 of 16 | 3.3 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| clock timing error from pair to pair | 2 % of the period rms (1.4 ps) | 16 of 16 | 2.5 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| clock timing error from pair to pair | 5 % of the period rms (3.5 ps) | 16 of 16 | 4.7 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| clock timing error from pair to pair | 10 % of the period rms (6.9 ps) | 16 of 16 | 31.5 | 7 of 224 | 8 in 3,296 | 189 | no | g28a |
| every spread at once | inductance 3 %, diodes 5 %, inside a pair 2 %, pump phase 20 degrees, pump level 10 %, links 10 %, clock 2 % | 16 of 16 | 10.0 | 0 of 224 | 0 in 3,360 | 189 | no | g28a |
| clock | slot 38 ps, on for 0.75 | 16 of 16 | 2.4 | 0 of 224 | 0 in 3,360 | 176 | yes | g28a |
| clock | slot 48 ps, on for 0.75 | 16 of 16 | 3.9 | 0 of 224 | 0 in 3,360 | 199 | yes | g28a |
| clock | slot 57 ps, on for 0.75 | 16 of 16 | 2.7 | 0 of 224 | 0 in 3,360 | 187 | yes | g28a |
| clock | slot 81 ps, on for 0.75 | 16 of 16 | 3.1 | 0 of 224 | 0 in 3,360 | 187 | yes | g28a |
| clock | slot 96 ps, on for 0.75 | 16 of 16 | 2.8 | 0 of 224 | 0 in 3,360 | 185 | yes | g28a |
| clock | slot 69 ps, on for 0.50 | 16 of 16 | 3.0 | 0 of 224 | 0 in 3,360 | 184 | yes | g28a |
| clock | slot 69 ps, on for 0.60 | 16 of 16 | 3.4 | 0 of 224 | 0 in 3,360 | 189 | yes | g28a |
| carrier and pump against the tanks | -3 % in frequency | 16 of 16 | 3.1 | 0 of 224 | 0 in 3,360 | 167 | yes | g28a |
| carrier and pump against the tanks | -2 % in frequency | 16 of 16 | 2.8 | 0 of 224 | 0 in 3,360 | 175 | yes | g28a |
| carrier and pump against the tanks | +2 % in frequency | 16 of 16 | 3.5 | 0 of 224 | 0 in 3,360 | 197 | yes | g28a |
| carrier and pump against the tanks | +3 % in frequency | 16 of 16 | 3.6 | 0 of 224 | 0 in 3,360 | 200 | yes | g28a |
| noise, no spread | 1 times the physical noise power | 16 of 16 | 0.3 | 0 of 889 | 0 in 13,335 | 189 | yes | g28a |
| noise, no spread | 4.78 times the physical noise power | 16 of 16 | 0.7 | 0 of 889 | 0 in 13,335 | 189 | yes | g28a |
| noise, no spread | 16 times the physical noise power | 16 of 16 | 1.3 | 0 of 889 | 0 in 13,335 | 189 | yes | g28a |
| noise, no spread | 64 times the physical noise power | 16 of 16 | 2.6 | 0 of 889 | 0 in 13,335 | 189 | yes | g28a |
| noise, no spread | 256 times the physical noise power | 16 of 16 | 46.6 | 63 of 889 | 97 in 12,808 | 189 | no | g28a |
| noise, no spread | 1.02e+03 times the physical noise power | 16 of 16 | 112.0 | 408 of 889 | 805 in 5,871 | 189 | no | g28a |
| base | as designed, inductance spread 3 % | 16 of 16 | 3.8 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| supply level error from pair to pair | 1 % rms (9 mV) | 16 of 16 | 3.1 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| supply level error from pair to pair | 2 % rms (19 mV) | 16 of 16 | 3.2 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| supply level error from pair to pair | 3 % rms (28 mV) | 16 of 16 | 3.4 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| supply level error from pair to pair | 4 % rms (38 mV) | 16 of 16 | 2.8 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| supply level error from pair to pair | 5 % rms (47 mV) | 16 of 16 | 3.7 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| damping resistor spread from pair to pair | 5 % rms | 16 of 16 | 3.4 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| damping resistor spread from pair to pair | 10 % rms | 16 of 16 | 4.7 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| damping resistor spread from pair to pair | 20 % rms | 16 of 16 | 4.5 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| damping resistor spread from pair to pair | 30 % rms | 16 of 16 | 6.1 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| pump phase error per clock phase | 5 degrees rms | 16 of 16 | 3.3 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| pump phase error per clock phase | 10 degrees rms | 16 of 16 | 5.3 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| pump phase error per clock phase | 20 degrees rms | 16 of 16 | 8.6 | 0 of 224 | 0 in 3,360 | 189 | no | g34a |
| pump phase error per clock phase | 30 degrees rms | 16 of 16 | 11.0 | 0 of 224 | 0 in 3,360 | 189 | no | g34a |
| pump phase error per clock phase | 45 degrees rms | 16 of 16 | 32.5 | 6 of 224 | 14 in 3,225 | 189 | no | g34a |
| input phase against the pump, full turn | -0.875 pi | 16 of 16 | 3.4 | 0 of 224 | 0 in 3,360 | 188 | yes | g34a |
| input phase against the pump, full turn | -0.750 pi | 16 of 16 | 3.7 | 0 of 224 | 0 in 3,360 | 188 | yes | g34a |
| input phase against the pump, full turn | -0.625 pi | 16 of 16 | 2.9 | 0 of 224 | 0 in 3,360 | 188 | yes | g34a |
| input phase against the pump, full turn | -0.500 pi | 16 of 16 | 3.0 | 0 of 224 | 0 in 3,360 | 188 | yes | g34a |
| input phase against the pump, full turn | -0.375 pi | 16 of 16 | 3.1 | 0 of 224 | 0 in 3,360 | 188 | yes | g34a |
| input phase against the pump, full turn | -0.250 pi | 16 of 16 | 3.3 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| input phase against the pump, full turn | -0.125 pi | 16 of 16 | 2.9 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| input phase against the pump, full turn | +0.000 pi | 16 of 16 | 2.9 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| input phase against the pump, full turn | +0.125 pi | 16 of 16 | 3.4 | 0 of 224 | 0 in 3,360 | 188 | yes | g34a |
| input phase against the pump, full turn | +0.250 pi | 16 of 16 | 3.3 | 0 of 224 | 0 in 3,360 | 188 | yes | g34a |
| input phase against the pump, full turn | +0.375 pi | 16 of 16 | 3.3 | 0 of 224 | 0 in 3,360 | 188 | yes | g34a |
| input phase against the pump, full turn | +0.500 pi | 16 of 16 | 3.3 | 0 of 224 | 0 in 3,360 | 188 | yes | g34a |
| input phase against the pump, full turn | +0.625 pi | 16 of 16 | 3.5 | 0 of 224 | 0 in 3,360 | 188 | yes | g34a |
| input phase against the pump, full turn | +0.750 pi | 16 of 16 | 3.1 | 0 of 224 | 0 in 3,360 | 188 | yes | g34a |
| input phase against the pump, full turn | +0.875 pi | 16 of 16 | 66.0 | 31 of 224 | 31 in 2,926 | 188 | no | g34a |
| input phase against the pump, full turn | +1.000 pi | 16 of 16 | 42.8 | 13 of 224 | 13 in 3,178 | 188 | no | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | -0.875 pi | 16 of 16 | 22.4 | 7 of 448 | 8 in 6,610 | 188 | no | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | -0.750 pi | 16 of 16 | 2.6 | 0 of 448 | 0 in 6,720 | 188 | yes | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | -0.625 pi | 16 of 16 | 2.7 | 0 of 448 | 0 in 6,720 | 188 | yes | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | -0.500 pi | 16 of 16 | 2.4 | 0 of 448 | 0 in 6,720 | 188 | yes | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | -0.375 pi | 16 of 16 | 2.5 | 0 of 448 | 0 in 6,720 | 188 | yes | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | -0.250 pi | 16 of 16 | 2.6 | 0 of 448 | 0 in 6,720 | 189 | yes | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | -0.125 pi | 16 of 16 | 2.8 | 0 of 448 | 0 in 6,720 | 189 | yes | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | +0.000 pi | 16 of 16 | 2.7 | 0 of 448 | 0 in 6,720 | 189 | yes | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | +0.125 pi | 16 of 16 | 2.7 | 0 of 448 | 0 in 6,720 | 188 | yes | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | +0.250 pi | 16 of 16 | 2.6 | 0 of 448 | 0 in 6,720 | 188 | yes | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | +0.375 pi | 16 of 16 | 2.7 | 0 of 448 | 0 in 6,720 | 188 | yes | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | +0.500 pi | 16 of 16 | 2.7 | 0 of 448 | 0 in 6,720 | 188 | yes | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | +0.625 pi | 16 of 16 | 2.7 | 0 of 448 | 0 in 6,720 | 188 | yes | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | +0.750 pi | 16 of 16 | 32.8 | 15 of 448 | 17 in 6,482 | 188 | no | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | +0.875 pi | 16 of 16 | 91.0 | 117 of 448 | 121 in 5,030 | 188 | no | g34a |
| input phase against the pump, full turn, 64 times the noise power, no spread | +1.000 pi | 16 of 16 | 78.8 | 88 of 448 | 90 in 5,461 | 188 | no | g34a |
| combination | every spread at once with pump phase 10 degrees, plus supply level 1 % and damping resistor 5 % | 16 of 16 | 5.5 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| combination | every spread at once with pump phase 10 degrees, plus supply level 2 % and damping resistor 10 % | 16 of 16 | 6.2 | 0 of 224 | 0 in 3,360 | 189 | yes | g34a |
| noise, no spread | 128 times the physical noise power | 16 of 16 | 3.8 | 0 of 889 | 0 in 13,335 | 189 | yes | g54e |

0.94 V and a 25 % pump unless the line says otherwise. Phase error, wrong decisions and level at pair 14 are read when the next pair decides; the level is that of the run without noise or spread.

## T-3. Rows of sixteen with a 3 % spread of the inductance: supply levels at which the row holds

| pump level | scanned | holds | batch |
|---|---|---|---|
| 15 % | 0.850 to 1.105 V | 0.925 to 0.970 V | g28a |
| 20 % | 0.850 to 1.105 V | 0.895 to 1.000 V | g28a |
| 25 % | 0.850 to 1.105 V | 0.880 to 1.030 V | g28a |
| 30 % | 0.850 to 1.105 V | 0.865 to 1.045 V | g28a |
| 35 % | 0.850 to 1.105 V | 0.850 to 1.030 V (scan ends) | g28a |
| 40 % | 0.850 to 1.105 V | 0.850 to 0.985 V (scan ends) | g28a |

Steps of 15 mV. "(scan ends)" marks a range that reaches an end of the scan.

## T-4. Rows of sixteen at other carriers, with other diodes and contacts, and under other assumptions: supply levels at which the row holds

| set | cell | input phase against the aligned value | pump | scanned | holds | level at the middle of the widest range (mV) | batch |
|---|---|---|---|---|---|---|---|
| other carriers | c160 | -0.25 pi | 25 % | 0.865 to 1.015 V | 0.865 to 1.015 V | 200 | g32 |
| other carriers | c160 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.895 to 1.015 V | 212 | g32 |
| other carriers | c160 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.865 to 1.015 V | 200 | g32 |
| other carriers | c160 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.865 to 1.015 V | 199 | g32 |
| other carriers | c160 | +0.25 pi | 25 % | 0.865 to 1.015 V | 0.865 to 1.015 V | 199 | g32 |
| other carriers | c320 | -0.25 pi | 25 % | 0.865 to 1.015 V | 0.910 to 1.015 V | 184 | g32 |
| other carriers | c320 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.925 to 0.985 V | 175 | g32 |
| other carriers | c320 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.910 to 1.015 V | 184 | g32 |
| other carriers | c320 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.895 to 1.015 V | 188 | g32 |
| other carriers | c320 | +0.25 pi | 25 % | 0.865 to 1.015 V | 0.910 to 1.015 V | 184 | g32 |
| other carriers | c450 | -0.25 pi | 25 % | 0.875 to 1.025 V | 0.935 to 0.995 V | 152 | g32 |
| other carriers | c450 | +0.00 pi | 20 % | 0.875 to 1.025 V | 0.950 to 0.980 V | 142 | g32 |
| other carriers | c450 | +0.00 pi | 25 % | 0.875 to 1.025 V | 0.935 to 0.995 V | 152 | g32 |
| other carriers | c450 | +0.00 pi | 30 % | 0.875 to 1.025 V | 0.920 to 1.010 V | 158 | g32 |
| other carriers | c450 | +0.25 pi | 25 % | 0.875 to 1.025 V | 0.935 to 0.995 V | 151 | g32 |
| other carriers | c640 | -0.25 pi | 25 % | 0.885 to 1.035 V | none | 0 | g32 |
| other carriers | c640 | +0.00 pi | 20 % | 0.885 to 1.035 V | 0.975 to 0.990 V | 73 | g32 |
| other carriers | c640 | +0.00 pi | 25 % | 0.885 to 1.035 V | 0.975 to 0.990 V | 78 | g32 |
| other carriers | c640 | +0.00 pi | 30 % | 0.885 to 1.035 V | 0.975 to 0.990 V | 81 | g32 |
| other carriers | c640 | +0.25 pi | 25 % | 0.885 to 1.035 V | 0.975 to 0.990 V | 78 | g32 |
| other carriers | c450t35 | -0.25 pi | 25 % | 0.865 to 1.015 V | 0.925 to 0.985 V | 171 | g32 |
| other carriers | c450t35 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.940 to 0.970 V | 160 | g32 |
| other carriers | c450t35 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.925 to 0.985 V | 171 | g32 |
| other carriers | c450t35 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.910 to 1.000 V | 178 | g32 |
| other carriers | c450t35 | +0.25 pi | 25 % | 0.865 to 1.015 V | 0.925 to 0.985 V | 170 | g32 |
| other carriers | c640t35 | -0.25 pi | 25 % | 0.875 to 1.025 V | 0.950 to 0.965 V | 90 | g32 |
| other carriers | c640t35 | +0.00 pi | 20 % | 0.875 to 1.025 V | none | 0 | g32 |
| other carriers | c640t35 | +0.00 pi | 25 % | 0.875 to 1.025 V | 0.950 to 0.965 V | 90 | g32 |
| other carriers | c640t35 | +0.00 pi | 30 % | 0.875 to 1.025 V | 0.950 to 0.980 V | 138 | g32 |
| other carriers | c640t35 | +0.25 pi | 25 % | 0.875 to 1.025 V | 0.950 to 0.965 V | 90 | g32 |
| other carriers | c900t35 | -0.25 pi | 25 % | 0.885 to 1.035 V | none | 0 | g32 |
| other carriers | c900t35 | +0.00 pi | 20 % | 0.885 to 1.035 V | 0.975 to 0.990 V | 89 | g32 |
| other carriers | c900t35 | +0.00 pi | 25 % | 0.885 to 1.035 V | 0.960 to 0.990 V | 89 | g32 |
| other carriers | c900t35 | +0.00 pi | 30 % | 0.885 to 1.035 V | 0.990 V | 89 | g32 |
| other carriers | c900t35 | +0.25 pi | 25 % | 0.885 to 1.035 V | 0.975 to 1.005 V | 101 | g32 |
| other carriers | c1075t20 | -0.25 pi | 25 % | 0.895 to 1.045 V | none | 0 | g32 |
| other carriers | c1075t20 | +0.00 pi | 20 % | 0.895 to 1.045 V | none | 0 | g32 |
| other carriers | c1075t20 | +0.00 pi | 25 % | 0.895 to 1.045 V | none | 0 | g32 |
| other carriers | c1075t20 | +0.00 pi | 30 % | 0.895 to 1.045 V | none | 0 | g32 |
| other carriers | c1075t20 | +0.25 pi | 25 % | 0.895 to 1.045 V | none | 0 | g32 |
| variants of what is assumed | Ft50 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.895 to 1.000 V | 186 | g33 |
| variants of what is assumed | Ft50 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.880 to 1.015 V | 195 | g33 |
| variants of what is assumed | Ft50 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.865 to 1.015 V | 199 | g33 |
| variants of what is assumed | Ft200 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.910 to 1.000 V | 179 | g33 |
| variants of what is assumed | Ft200 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.895 to 1.015 V | 185 | g33 |
| variants of what is assumed | Ft200 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.880 to 1.015 V | 169 | g33 |
| variants of what is assumed | Ft300 | +0.00 pi | 20 % | 0.875 to 1.025 V | 0.920 to 1.010 V | 158 | g33 |
| variants of what is assumed | Ft300 | +0.00 pi | 25 % | 0.875 to 1.025 V | 0.905 to 1.025 V | 159 | g33 |
| variants of what is assumed | Ft300 | +0.00 pi | 30 % | 0.875 to 1.025 V | 0.890 to 1.025 V | 137 | g33 |
| variants of what is assumed | Fr1.5 | +0.00 pi | 20 % | 0.825 to 0.975 V | 0.870 to 0.960 V | 192 | g33 |
| variants of what is assumed | Fr1.5 | +0.00 pi | 25 % | 0.825 to 0.975 V | 0.855 to 0.975 V | 200 | g33 |
| variants of what is assumed | Fr1.5 | +0.00 pi | 30 % | 0.825 to 0.975 V | 0.840 to 0.975 V | 187 | g33 |
| variants of what is assumed | Fr6 | +0.00 pi | 20 % | 0.935 to 1.085 V | 0.965 to 1.085 V | 195 | g33 |
| variants of what is assumed | Fr6 | +0.00 pi | 25 % | 0.935 to 1.085 V | 0.950 to 1.085 V | 184 | g33 |
| variants of what is assumed | Fr6 | +0.00 pi | 30 % | 0.935 to 1.085 V | 0.935 to 1.085 V | 184 | g33 |
| variants of what is assumed | Fk1 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.895 to 1.015 V | 203 | g33 |
| variants of what is assumed | Fk1 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.880 to 1.015 V | 191 | g33 |
| variants of what is assumed | Fk1 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.865 to 1.015 V | 191 | g33 |
| variants of what is assumed | Fk5 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.895 to 1.015 V | 205 | g33 |
| variants of what is assumed | Fk5 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.880 to 1.015 V | 192 | g33 |
| variants of what is assumed | Fk5 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.865 to 1.000 V | 176 | g33 |
| variants of what is assumed | FRb5 | +0.00 pi | 20 % | 0.895 to 1.045 V | 0.925 to 1.030 V | 185 | g33 |
| variants of what is assumed | FRb5 | +0.00 pi | 25 % | 0.895 to 1.045 V | 0.910 to 1.045 V | 194 | g33 |
| variants of what is assumed | FRb5 | +0.00 pi | 30 % | 0.895 to 1.045 V | 0.895 to 1.045 V | 196 | g33 |
| variants of what is assumed | FCb4 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.895 to 1.000 V | 178 | g33 |
| variants of what is assumed | FCb4 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.880 to 1.015 V | 188 | g33 |
| variants of what is assumed | FCb4 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.865 to 1.015 V | 192 | g33 |
| 1.075-THz pairs with other diodes | j052t21 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.910 to 1.000 V | 200 | g39 |
| 1.075-THz pairs with other diodes | j052t21 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.895 to 1.015 V | 206 | g39 |
| 1.075-THz pairs with other diodes | j052t21 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.865 to 1.015 V | 192 | g39 |
| 1.075-THz pairs with other diodes | j080t21 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.925 to 0.970 V | 153 | g39 |
| 1.075-THz pairs with other diodes | j080t21 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.910 to 1.015 V | 188 | g39 |
| 1.075-THz pairs with other diodes | j080t21 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.895 to 1.015 V | 193 | g39 |
| 1.075-THz pairs with other diodes | j125t21 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.955 V | 127 | g39 |
| 1.075-THz pairs with other diodes | j125t21 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.940 to 0.985 V | 139 | g39 |
| 1.075-THz pairs with other diodes | j125t21 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.940 to 1.000 V | 171 | g39 |
| 1.075-THz pairs with other diodes | j170t21 | +0.00 pi | 20 % | 0.875 to 1.025 V | none | 0 | g39 |
| 1.075-THz pairs with other diodes | j170t21 | +0.00 pi | 25 % | 0.875 to 1.025 V | 0.950 to 0.965 V | 65 | g39 |
| 1.075-THz pairs with other diodes | j170t21 | +0.00 pi | 30 % | 0.875 to 1.025 V | 0.950 to 0.980 V | 122 | g39 |
| 1.075-THz pairs with other diodes | j250t21 | +0.00 pi | 20 % | 0.895 to 1.045 V | none | 0 | g39 |
| 1.075-THz pairs with other diodes | j250t21 | +0.00 pi | 25 % | 0.895 to 1.045 V | none | 0 | g39 |
| 1.075-THz pairs with other diodes | j250t21 | +0.00 pi | 30 % | 0.895 to 1.045 V | none | 0 | g39 |
| 1.075-THz pairs with other diodes | j052t35 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.910 to 1.000 V | 187 | g39 |
| 1.075-THz pairs with other diodes | j052t35 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.895 to 1.015 V | 193 | g39 |
| 1.075-THz pairs with other diodes | j052t35 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.880 to 1.015 V | 178 | g39 |
| 1.075-THz pairs with other diodes | j080t35 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.925 to 0.985 V | 164 | g39 |
| 1.075-THz pairs with other diodes | j080t35 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.910 to 1.000 V | 173 | g39 |
| 1.075-THz pairs with other diodes | j080t35 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.895 to 1.015 V | 178 | g39 |
| 1.075-THz pairs with other diodes | j125t35 | +0.00 pi | 20 % | 0.875 to 1.025 V | 0.950 to 0.965 V | 89 | g39 |
| 1.075-THz pairs with other diodes | j125t35 | +0.00 pi | 25 % | 0.875 to 1.025 V | 0.950 to 0.980 V | 138 | g39 |
| 1.075-THz pairs with other diodes | j125t35 | +0.00 pi | 30 % | 0.875 to 1.025 V | 0.935 to 0.980 V | 119 | g39 |
| 1.075-THz pairs with other diodes | j170t35 | +0.00 pi | 20 % | 0.875 to 1.025 V | 0.965 V | 86 | g39 |
| 1.075-THz pairs with other diodes | j170t35 | +0.00 pi | 25 % | 0.875 to 1.025 V | 0.965 V | 96 | g39 |
| 1.075-THz pairs with other diodes | j170t35 | +0.00 pi | 30 % | 0.875 to 1.025 V | 0.950 to 0.995 V | 103 | g39 |
| 1.075-THz pairs with other diodes | j052t50 | +0.00 pi | 20 % | 0.865 to 1.015 V | 0.910 to 1.015 V | 168 | g39 |
| 1.075-THz pairs with other diodes | j052t50 | +0.00 pi | 25 % | 0.865 to 1.015 V | 0.895 to 1.015 V | 173 | g39 |
| 1.075-THz pairs with other diodes | j052t50 | +0.00 pi | 30 % | 0.865 to 1.015 V | 0.895 to 1.015 V | 169 | g39 |
| 1.075-THz pairs with other diodes | j080t50 | +0.00 pi | 20 % | 0.875 to 1.025 V | 0.935 to 0.995 V | 157 | g39 |
| 1.075-THz pairs with other diodes | j080t50 | +0.00 pi | 25 % | 0.875 to 1.025 V | 0.920 to 1.010 V | 164 | g39 |
| 1.075-THz pairs with other diodes | j080t50 | +0.00 pi | 30 % | 0.875 to 1.025 V | 0.920 to 1.025 V | 166 | g39 |
| 1.075-THz pairs with other diodes | j125t50 | +0.00 pi | 20 % | 0.875 to 1.025 V | 0.965 to 0.980 V | 101 | g39 |
| 1.075-THz pairs with other diodes | j125t50 | +0.00 pi | 25 % | 0.875 to 1.025 V | 0.950 to 0.980 V | 111 | g39 |
| 1.075-THz pairs with other diodes | j125t50 | +0.00 pi | 30 % | 0.875 to 1.025 V | 0.950 to 0.995 V | 118 | g39 |
| 1.075-THz pairs with other diodes | j170t50 | +0.00 pi | 20 % | 0.885 to 1.035 V | 0.975 V | 77 | g39 |
| 1.075-THz pairs with other diodes | j170t50 | +0.00 pi | 25 % | 0.885 to 1.035 V | 0.975 to 0.990 V | 82 | g39 |
| 1.075-THz pairs with other diodes | j170t50 | +0.00 pi | 30 % | 0.885 to 1.035 V | none | 0 | g39 |
| 1.075-THz pairs with other contacts | j170r06t35 | +0.00 pi | 20 % | 0.835 to 0.985 V | none | 0 | g46 |
| 1.075-THz pairs with other contacts | j170r06t35 | +0.00 pi | 25 % | 0.835 to 0.985 V | none | 0 | g46 |
| 1.075-THz pairs with other contacts | j170r06t35 | +0.00 pi | 30 % | 0.835 to 0.985 V | 0.910 to 0.925 V | 84 | g46 |
| 1.075-THz pairs with other contacts | j250r06t35 | +0.00 pi | 20 % | 0.845 to 0.995 V | 0.905 to 0.965 V | 123 | g46 |
| 1.075-THz pairs with other contacts | j250r06t35 | +0.00 pi | 25 % | 0.845 to 0.995 V | 0.905 to 0.950 V; 0.980 V | 106 | g46 |
| 1.075-THz pairs with other contacts | j250r06t35 | +0.00 pi | 30 % | 0.845 to 0.995 V | 0.905 to 0.980 V | 120 | g46 |
| 1.075-THz pairs with other contacts | j250r03t35 | +0.00 pi | 20 % | 0.815 to 0.965 V | 0.890 to 0.920 V | 139 | g46 |
| 1.075-THz pairs with other contacts | j250r03t35 | +0.00 pi | 25 % | 0.815 to 0.965 V | 0.875 to 0.935 V | 149 | g46 |
| 1.075-THz pairs with other contacts | j250r03t35 | +0.00 pi | 30 % | 0.815 to 0.965 V | 0.875 to 0.965 V | 173 | g46 |
| 1.075-THz pairs with other contacts | j080r24t35 | +0.00 pi | 20 % | 0.945 to 1.095 V | 1.005 to 1.065 V | 150 | g46 |
| 1.075-THz pairs with other contacts | j080r24t35 | +0.00 pi | 25 % | 0.945 to 1.095 V | 0.990 to 1.080 V | 154 | g46 |
| 1.075-THz pairs with other contacts | j080r24t35 | +0.00 pi | 30 % | 0.945 to 1.095 V | 0.975 to 1.095 V | 154 | g46 |
| 1.075-THz pairs with other contacts | j052r24t35 | +0.00 pi | 20 % | 0.935 to 1.085 V | 0.980 to 1.070 V | 178 | g46 |
| 1.075-THz pairs with other contacts | j052r24t35 | +0.00 pi | 25 % | 0.935 to 1.085 V | 0.965 to 1.085 V | 180 | g46 |
| 1.075-THz pairs with other contacts | j052r24t35 | +0.00 pi | 30 % | 0.935 to 1.085 V | 0.950 to 1.085 V | 163 | g46 |
| 1.075-THz pairs with other contacts | j125r24t35 | +0.00 pi | 20 % | 0.955 to 1.105 V | 1.060 V | 83 | g46 |
| 1.075-THz pairs with other contacts | j125r24t35 | +0.00 pi | 25 % | 0.955 to 1.105 V | 1.045 to 1.060 V | 70 | g46 |
| 1.075-THz pairs with other contacts | j125r24t35 | +0.00 pi | 30 % | 0.955 to 1.105 V | none | 0 | g46 |

A 3 % spread of the inductance and the noise of each cell, 32 runs per supply level, steps of 15 mV. Cell names are those of the settings files.

## T-5. Adders without state

| layout | note | condition | pairs right without noise or spread | lowest level without noise or spread (mV) | wrong additions | runs with a wrong addition | wrong decisions of any pair | batch |
|---|---|---|---|---|---|---|---|---|
| four-bit adder, 53 pairs |  | as designed | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | inductance spread 3 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | inductance spread 5 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | every spread at once | 53 of 53 | 201 | 4 of 992 | 1 of 32 | 4 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | pump phase error 10 degrees | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | pump phase error 20 degrees | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | pump phase error 30 degrees | 53 of 53 | 201 | 45 of 992 | 4 of 32 | 218 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | pump phase error 45 degrees | 53 of 53 | 201 | 277 of 992 | 22 of 32 | 1,087 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | link strength error 10 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | link strength error 20 % | 53 of 53 | 201 | 101 of 992 | 13 of 32 | 140 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | link strength error 30 % | 53 of 53 | 201 | 428 of 992 | 32 of 32 | 964 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | clock timing error 2 % of the period | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | clock timing error 5 % of the period | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | pump level error 20 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | diode current spread 10 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | difference inside a pair 5 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | inductance 3 %, diodes 5 %, inside a pair 2 %, pump level 10 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | the same with links 10 % and clock 2 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | the same with pump phase 10 degrees | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | every spread at once, doubled except the inductance | 53 of 53 | 201 | 448 of 992 | 31 of 32 | 1,746 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | stray coupling 0.3 %, alternating sign | 53 of 53 | 198 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | stray coupling 0.6 %, alternating sign | 53 of 53 | 189 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | stray coupling 1.2 %, alternating sign | 53 of 53 | 168 | 0 of 992 | 0 of 32 | 0 of 52,576 | g28b |
| four-bit adder, 53 pairs |  | noise power x4.78 | 53 of 53 | 201 | 0 of 1,984 | 0 of 64 | 0 of 105,152 | g28b |
| four-bit adder, 53 pairs |  | noise power x16 | 53 of 53 | 201 | 0 of 1,984 | 0 of 64 | 0 of 105,152 | g28b |
| four-bit adder, 53 pairs |  | noise power x64 | 53 of 53 | 201 | 0 of 1,984 | 0 of 64 | 0 of 105,152 | g28b |
| eight-bit adder, 169 pairs |  | as designed | 169 of 169 | 197 | 0 of 992 | 0 of 32 | 0 of 167,648 | g28e |
| eight-bit adder, 169 pairs |  | inductance spread 3 % | 169 of 169 | 197 | 0 of 992 | 0 of 32 | 0 of 167,648 | g28e |
| eight-bit adder, 169 pairs |  | inductance spread 5 % | 169 of 169 | 197 | 0 of 992 | 0 of 32 | 0 of 167,648 | g28e |
| eight-bit adder, 169 pairs |  | every spread at once | 169 of 169 | 197 | 7 of 992 | 1 of 32 | 7 of 167,648 | g28e |
| four-bit adder on two rails, 106 pairs |  | as designed | 106 of 106 | 201 | 0 of 992 | 0 of 32 | 0 of 105,152 | g28g |
| four-bit adder on two rails, 106 pairs |  | inductance spread 3 % | 106 of 106 | 201 | 0 of 992 | 0 of 32 | 0 of 105,152 | g28g |
| four-bit adder on two rails, 106 pairs |  | inductance spread 5 % | 106 of 106 | 201 | 0 of 992 | 0 of 32 | 0 of 105,152 | g28g |
| four-bit adder on two rails, 106 pairs |  | every spread at once | 106 of 106 | 201 | 12 of 992 | 1 of 32 | 12 of 105,152 | g28g |
| four-bit adder on two rails, 106 pairs |  | stray coupling 0.3 %, alternating sign | 106 of 106 | 194 | 0 of 992 | 0 of 32 | 0 of 105,152 | g28g |
| four-bit adder on two rails, 106 pairs |  | stray coupling 0.6 %, alternating sign | 106 of 106 | 180 | 0 of 992 | 0 of 32 | 0 of 105,152 | g28g |
| four-bit adder on two rails, 106 pairs |  | stray coupling 1.2 %, alternating sign | 96 of 106 | 2 | 32 of 992 | 17 of 32 | 201 of 105,152 | g28g |
| four-bit adder, 53 pairs |  | supply level error 1 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | supply level error 2 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | supply level error 3 % | 53 of 53 | 201 | 34 of 992 | 3 of 32 | 36 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | damping resistor spread 5 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | damping resistor spread 10 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | damping resistor spread 20 % | 53 of 53 | 201 | 172 of 992 | 17 of 32 | 312 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | pump phase error per clock phase 5 degrees | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | pump phase error per clock phase 10 degrees | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | pump phase error per clock phase 20 degrees | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | input phase -0.250 pi | 53 of 53 | 199 | 0 of 992 | 0 of 32 | 0 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | input phase -0.125 pi | 53 of 53 | 199 | 0 of 992 | 0 of 32 | 0 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | input phase +0.125 pi | 53 of 53 | 199 | 0 of 992 | 0 of 32 | 0 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | input phase +0.250 pi | 53 of 53 | 199 | 0 of 992 | 0 of 32 | 0 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | every spread at once with pump phase 10 degrees, plus supply level 1 % and damping resistor 5 % | 53 of 53 | 201 | 31 of 992 | 3 of 32 | 67 of 52,576 | g34b |
| four-bit adder, 53 pairs |  | every spread at once with pump phase 10 degrees, plus supply level 2 % and damping resistor 10 % | 53 of 53 | 201 | 79 of 992 | 11 of 32 | 118 of 52,576 | g34b |
| four-bit adder, 53 pairs | other carriers | c160: inductance spread 3 % | 53 of 53 | 212 | 0 of 992 | 0 of 32 | 0 of 52,576 | g35a |
| four-bit adder, 53 pairs | other carriers | c160: every spread at once with pump phase 10 degrees | 53 of 53 | 212 | 0 of 992 | 0 of 32 | 0 of 52,576 | g35a |
| four-bit adder, 53 pairs | other carriers | c320: inductance spread 3 % | 53 of 53 | 200 | 0 of 992 | 0 of 32 | 0 of 52,576 | g35a |
| four-bit adder, 53 pairs | other carriers | c320: every spread at once with pump phase 10 degrees | 53 of 53 | 200 | 0 of 992 | 0 of 32 | 0 of 52,576 | g35a |
| four-bit adder, 53 pairs | other carriers | c450: inductance spread 3 % | 53 of 53 | 145 | 0 of 992 | 0 of 32 | 0 of 52,576 | g35a |
| four-bit adder, 53 pairs | other carriers | c450: every spread at once with pump phase 10 degrees | 53 of 53 | 145 | 26 of 992 | 7 of 32 | 29 of 52,576 | g35a |
| four-bit adder, 53 pairs | other carriers | c640: inductance spread 3 % | 53 of 53 | 73 | 117 of 992 | 20 of 32 | 192 of 52,576 | g35a |
| four-bit adder, 53 pairs | other carriers | c640: every spread at once with pump phase 10 degrees | 53 of 53 | 73 | 273 of 992 | 30 of 32 | 751 of 52,576 | g35a |
| four-bit adder, 53 pairs | other carriers | c450t35: inductance spread 3 % | 53 of 53 | 187 | 0 of 992 | 0 of 32 | 0 of 52,576 | g35a |
| four-bit adder, 53 pairs | other carriers | c450t35: every spread at once with pump phase 10 degrees | 53 of 53 | 187 | 0 of 992 | 0 of 32 | 0 of 52,576 | g35a |
| four-bit adder, 53 pairs | other carriers | c640t35: inductance spread 3 % | 53 of 53 | 78 | 0 of 992 | 0 of 32 | 0 of 52,576 | g35a |
| four-bit adder, 53 pairs | other carriers | c640t35: every spread at once with pump phase 10 degrees | 53 of 53 | 78 | 109 of 992 | 24 of 32 | 118 of 52,576 | g35a |
| four-bit adder, 53 pairs | other carriers | c900t35: inductance spread 3 % | 53 of 53 | 76 | 72 of 992 | 21 of 32 | 95 of 52,576 | g35a |
| four-bit adder, 53 pairs | other carriers | c900t35: every spread at once with pump phase 10 degrees | 53 of 53 | 76 | 356 of 992 | 30 of 32 | 869 of 52,576 | g35a |
| eight-bit adder, 169 pairs |  | noise power x16 | 169 of 169 | 197 | 0 of 1,984 | 0 of 64 | 0 of 335,296 | g36a |
| eight-bit adder, 169 pairs |  | noise power x64 | 169 of 169 | 197 | 1 of 1,984 | 1 of 64 | 2 of 335,296 | g36a |
| four-bit adder, 53 pairs |  | supply 0.880 V, inductance spread 3 % | 53 of 53 | 2 | 316 of 992 | 30 of 32 | 407 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | supply 0.895 V, inductance spread 3 % | 53 of 53 | 87 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | supply 0.910 V, inductance spread 3 % | 53 of 53 | 143 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | supply 0.970 V, inductance spread 3 % | 53 of 53 | 229 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | supply 0.985 V, inductance spread 3 % | 53 of 53 | 240 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | supply 1.000 V, inductance spread 3 % | 53 of 53 | 245 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | supply 1.015 V, inductance spread 3 % | 53 of 53 | 244 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | pump 15 %, inductance spread 3 % | 53 of 53 | 169 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | pump 20 %, inductance spread 3 % | 53 of 53 | 190 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | pump 30 %, inductance spread 3 % | 53 of 53 | 205 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | pump 35 %, inductance spread 3 % | 53 of 53 | 179 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | pump 40 %, inductance spread 3 % | 53 of 53 | 77 | 8 of 992 | 3 of 32 | 8 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | links 3.0 %, inductance spread 3 % | 53 of 53 | 171 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | links 4.5 %, inductance spread 3 % | 53 of 53 | 198 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | links 7.5 %, inductance spread 3 % | 53 of 53 | 191 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | links 9.0 %, inductance spread 3 % | 53 of 53 | 173 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | links 12.0 %, inductance spread 3 % | 41 of 53 | 3 | 447 of 992 | 32 of 32 | 1,580 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | slot 38 ps, inductance spread 3 % | 53 of 53 | 34 | 1 of 992 | 1 of 32 | 1 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | slot 48 ps, inductance spread 3 % | 53 of 53 | 162 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | slot 57 ps, inductance spread 3 % | 53 of 53 | 185 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| four-bit adder, 53 pairs |  | slot 81 ps, inductance spread 3 % | 53 of 53 | 200 | 0 of 992 | 0 of 32 | 0 of 52,576 | g37a |
| eight-bit adder, 169 pairs |  | supply 0.910 V, inductance spread 3 % | 169 of 169 | 142 | 0 of 992 | 0 of 32 | 0 of 167,648 | g37b |
| eight-bit adder, 169 pairs |  | supply 0.970 V, inductance spread 3 % | 169 of 169 | 227 | 0 of 992 | 0 of 32 | 0 of 167,648 | g37b |
| four-bit adder, 53 pairs |  | full set x 0.75 | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g40 |
| four-bit adder, 53 pairs |  | full set x 0.5 | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g40 |
| four-bit adder, 53 pairs |  | full set x 0.25 | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g40 |
| four-bit adder, 53 pairs |  | every spread at once with pump phase 10 degrees, plus supply level 1 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g40 |
| four-bit adder, 53 pairs |  | every spread at once with pump phase 10 degrees, plus damping resistor 5 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g40 |
| four-bit adder, 53 pairs |  | supply level error 1.5 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g40 |
| four-bit adder, 53 pairs |  | damping resistor spread 15 % | 53 of 53 | 201 | 64 of 992 | 7 of 32 | 70 of 52,576 | g40 |
| four-bit adder, 53 pairs |  | 1.075 THz: inductance spread 3 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g40 |
| four-bit adder, 53 pairs |  | 1.075 THz: inductance spread 5 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g40 |
| four-bit adder, 53 pairs |  | 1.075 THz: full set x 0.5 | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g40 |
| four-bit adder, 53 pairs |  | 1.075 THz: full set x 1 | 53 of 53 | 201 | 1 of 992 | 1 of 32 | 1 of 52,576 | g40 |
| eight-bit adder, 169 pairs |  | full set x 0.5 | 169 of 169 | 197 | 0 of 992 | 0 of 32 | 0 of 167,648 | g41 |
| eight-bit adder, 169 pairs |  | 1.075 THz: inductance spread 3 % | 169 of 169 | 197 | 0 of 992 | 0 of 32 | 0 of 167,648 | g41 |
| eight-bit adder, 169 pairs |  | 1.075 THz: inductance spread 5 % | 169 of 169 | 197 | 0 of 992 | 0 of 32 | 0 of 167,648 | g41 |
| eight-bit adder, 169 pairs |  | 1.075 THz: full set x 0.5 | 169 of 169 | 197 | 0 of 992 | 0 of 32 | 0 of 167,648 | g41 |
| eight-bit adder, 169 pairs |  | full set x 0.5 | 169 of 169 | 197 | 0 of 992 | 0 of 32 | 0 of 167,648 | g41x |
| eight-bit adder, 169 pairs |  | 1.075 THz: inductance spread 3 % | 169 of 169 | 197 | 0 of 992 | 0 of 32 | 0 of 167,648 | g41x |
| eight-bit adder, 169 pairs |  | 1.075 THz: inductance spread 5 % | 169 of 169 | 197 | 0 of 992 | 0 of 32 | 0 of 167,648 | g41x |
| eight-bit adder, 169 pairs |  | 1.075 THz: full set x 0.5 | 169 of 169 | 197 | 0 of 992 | 0 of 32 | 0 of 167,648 | g41x |
| eight-bit adder, 169 pairs |  | noise power x16 | 169 of 169 | 197 | 0 of 1,984 | 0 of 64 | 0 of 335,296 | g41x |
| eight-bit adder, 169 pairs |  | noise power x64 | 169 of 169 | 197 | 1 of 1,984 | 1 of 64 | 5 of 335,296 | g41x |
| four-bit adder, 53 pairs | other diodes | j052t21: inductance spread 3 % | 53 of 53 | 205 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j052t21: full set x 0.5 | 53 of 53 | 205 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j080t21: inductance spread 3 % | 53 of 53 | 204 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j080t21: full set x 0.5 | 53 of 53 | 204 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j125t21: inductance spread 3 % | 53 of 53 | 158 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j125t21: full set x 0.5 | 53 of 53 | 158 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j170t21: inductance spread 3 % | 53 of 53 | 3 | 307 of 992 | 32 of 32 | 398 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j170t21: full set x 0.5 | 53 of 53 | 3 | 606 of 992 | 32 of 32 | 1,310 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j052t35: inductance spread 3 % | 53 of 53 | 190 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j052t35: full set x 0.5 | 53 of 53 | 190 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j080t35: inductance spread 3 % | 53 of 53 | 191 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j080t35: full set x 0.5 | 53 of 53 | 191 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j125t35: inductance spread 3 % | 53 of 53 | 113 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j125t35: full set x 0.5 | 53 of 53 | 113 | 1 of 992 | 1 of 32 | 1 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j170t35: inductance spread 3 % | 53 of 53 | 26 | 211 of 992 | 31 of 32 | 252 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j170t35: full set x 0.5 | 53 of 53 | 26 | 319 of 992 | 32 of 32 | 554 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j052t50: inductance spread 3 % | 53 of 53 | 159 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j052t50: full set x 0.5 | 53 of 53 | 159 | 1 of 992 | 1 of 32 | 1 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j080t50: inductance spread 3 % | 53 of 53 | 177 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j080t50: full set x 0.5 | 53 of 53 | 177 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j125t50: inductance spread 3 % | 53 of 53 | 124 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j125t50: full set x 0.5 | 53 of 53 | 124 | 0 of 992 | 0 of 32 | 0 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j170t50: inductance spread 3 % | 53 of 53 | 72 | 76 of 992 | 24 of 32 | 159 of 52,576 | g44 |
| four-bit adder, 53 pairs | other diodes | j170t50: full set x 0.5 | 53 of 53 | 72 | 27 of 992 | 13 of 32 | 52 of 52,576 | g44 |
| four-bit adder, 53 pairs | other contacts | j170r06t35: inductance spread 3 % | 53 of 53 | 20 | 88 of 992 | 28 of 32 | 93 of 52,576 | g47 |
| four-bit adder, 53 pairs | other contacts | j170r06t35: full set x 0.5 | 53 of 53 | 20 | 360 of 992 | 31 of 32 | 585 of 52,576 | g47 |
| four-bit adder, 53 pairs | other contacts | j250r06t35: inductance spread 3 % | 53 of 53 | 91 | 80 of 992 | 18 of 32 | 111 of 52,576 | g47 |
| four-bit adder, 53 pairs | other contacts | j250r06t35: full set x 0.5 | 53 of 53 | 91 | 3 of 992 | 3 of 32 | 3 of 52,576 | g47 |
| four-bit adder, 53 pairs | other contacts | j250r03t35: inductance spread 3 % | 53 of 53 | 156 | 0 of 992 | 0 of 32 | 0 of 52,576 | g47 |
| four-bit adder, 53 pairs | other contacts | j250r03t35: full set x 0.5 | 53 of 53 | 156 | 0 of 992 | 0 of 32 | 0 of 52,576 | g47 |
| four-bit adder, 53 pairs | other contacts | j080r24t35: inductance spread 3 % | 53 of 53 | 153 | 0 of 992 | 0 of 32 | 0 of 52,576 | g47 |
| four-bit adder, 53 pairs | other contacts | j080r24t35: full set x 0.5 | 53 of 53 | 153 | 0 of 992 | 0 of 32 | 0 of 52,576 | g47 |
| four-bit adder, 53 pairs | other contacts | j052r24t35: inductance spread 3 % | 53 of 53 | 178 | 0 of 992 | 0 of 32 | 0 of 52,576 | g47 |
| four-bit adder, 53 pairs | other contacts | j052r24t35: full set x 0.5 | 53 of 53 | 178 | 0 of 992 | 0 of 32 | 0 of 52,576 | g47 |
| four-bit adder, 53 pairs | other contacts | j125r24t35: inductance spread 3 % | 53 of 53 | 75 | 90 of 992 | 26 of 32 | 210 of 52,576 | g47 |
| four-bit adder, 53 pairs | other contacts | j125r24t35: full set x 0.5 | 53 of 53 | 75 | 54 of 992 | 19 of 32 | 135 of 52,576 | g47 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.880 V, inductance spread 3 % | 53 of 53 | 2 | 473 of 992 | 32 of 32 | 754 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.895 V, inductance spread 3 % | 53 of 53 | 87 | 1 of 992 | 1 of 32 | 1 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.910 V, inductance spread 3 % | 53 of 53 | 143 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.970 V, inductance spread 3 % | 53 of 53 | 229 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.985 V, inductance spread 3 % | 53 of 53 | 240 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 1.000 V, inductance spread 3 % | 53 of 53 | 245 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 1.015 V, inductance spread 3 % | 53 of 53 | 244 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump 15 %, inductance spread 3 % | 53 of 53 | 169 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump 20 %, inductance spread 3 % | 53 of 53 | 190 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump 30 %, inductance spread 3 % | 53 of 53 | 205 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump 35 %, inductance spread 3 % | 53 of 53 | 179 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump 40 %, inductance spread 3 % | 53 of 53 | 77 | 22 of 992 | 7 of 32 | 27 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: links 3.0 %, inductance spread 3 % | 53 of 53 | 171 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: links 4.5 %, inductance spread 3 % | 53 of 53 | 198 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: links 7.5 %, inductance spread 3 % | 53 of 53 | 191 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: links 9.0 %, inductance spread 3 % | 53 of 53 | 173 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: links 12.0 %, inductance spread 3 % | 41 of 53 | 3 | 458 of 992 | 32 of 32 | 1,636 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: slot 38 ps, inductance spread 3 % | 53 of 53 | 34 | 52 of 992 | 25 of 32 | 53 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: slot 48 ps, inductance spread 3 % | 53 of 53 | 162 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: slot 57 ps, inductance spread 3 % | 53 of 53 | 185 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: slot 81 ps, inductance spread 3 % | 53 of 53 | 200 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply level error 1 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply level error 2 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply level error 3 % | 53 of 53 | 201 | 18 of 992 | 5 of 32 | 33 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: damping resistor spread 5 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: damping resistor spread 10 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: damping resistor spread 20 % | 53 of 53 | 201 | 100 of 992 | 14 of 32 | 173 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump phase error per clock phase 5 degrees | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump phase error per clock phase 10 degrees | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump phase error per clock phase 20 degrees | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: input phase -0.250 pi | 53 of 53 | 199 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: input phase -0.125 pi | 53 of 53 | 199 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: input phase +0.125 pi | 53 of 53 | 199 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: input phase +0.250 pi | 53 of 53 | 199 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply level error 1.5 %, inductance spread 3 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: damping resistor spread 15 %, inductance spread 3 % | 53 of 53 | 201 | 22 of 992 | 6 of 32 | 22 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump phase error 10 degrees, inductance spread 3 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump phase error 20 degrees, inductance spread 3 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump phase error 30 degrees, inductance spread 3 % | 53 of 53 | 201 | 7 of 992 | 2 of 32 | 20 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: link strength error 10 %, inductance spread 3 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: link strength error 20 %, inductance spread 3 % | 53 of 53 | 201 | 133 of 992 | 21 of 32 | 183 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: clock timing error 2 % of the period, inductance spread 3 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: clock timing error 5 % of the period, inductance spread 3 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump level error 20 %, inductance spread 3 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: diode current spread 10 %, inductance spread 3 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| four-bit adder, 53 pairs | 1-THz-class cell at its own noise | 1.075 THz: difference inside a pair 5 %, inductance spread 3 % | 53 of 53 | 201 | 0 of 992 | 0 of 32 | 0 of 52,576 | g48 |
| eight-bit adder, 169 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.910 V, inductance spread 3 % | 169 of 169 | 142 | 0 of 992 | 0 of 32 | 0 of 167,648 | g50 |
| eight-bit adder, 169 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.970 V, inductance spread 3 % | 169 of 169 | 227 | 0 of 992 | 0 of 32 | 0 of 167,648 | g50 |
| four-bit adder, 53 pairs | spread budget, 256 draws per line | 1.075 THz: full set x 1, without the capacitors, 256 runs | 53 of 53 | 201 | 23 of 7,936 | 7 of 256 | 23 of 420,608 | g52 |
| four-bit adder, 53 pairs | spread budget, 256 draws per line | 1.075 THz: full set x 0.75, without the capacitors, 256 runs | 53 of 53 | 201 | 3 of 7,936 | 1 of 256 | 3 of 420,608 | g52 |
| four-bit adder, 53 pairs | spread budget, 256 draws per line | 225 GHz noise: full set x 1, without the capacitors, 256 runs | 53 of 53 | 201 | 26 of 7,936 | 5 of 256 | 26 of 420,608 | g52 |
| four-bit adder, 53 pairs | spread budget, 256 draws per line | 1.075 THz: full set x 0.5, without the capacitors, 256 runs | 53 of 53 | 201 | 0 of 7,936 | 0 of 256 | 0 of 420,608 | g53 |
| four-bit adder, 53 pairs | spread budget, 256 draws per line | 1.075 THz: full set x 0.625, without the capacitors, 256 runs | 53 of 53 | 201 | 0 of 7,936 | 0 of 256 | 0 of 420,608 | g53 |
| four-bit adder, 53 pairs | spread budget, 256 draws per line | 1.075 THz: full set x 0.875, without the capacitors, 256 runs | 53 of 53 | 201 | 24 of 7,936 | 10 of 256 | 24 of 420,608 | g53 |
| four-bit adder, 53 pairs | spread budget, 256 draws per line | 225 GHz noise: full set x 0.5, without the capacitors, 256 runs | 53 of 53 | 201 | 0 of 7,936 | 0 of 256 | 0 of 420,608 | g53 |
| four-bit adder, 53 pairs | spread budget, 256 draws per line | 225 GHz noise: full set x 0.75, without the capacitors, 256 runs | 53 of 53 | 201 | 0 of 7,936 | 0 of 256 | 0 of 420,608 | g53 |
| four-bit adder, 53 pairs | raised noise, no spread | noise power x128 | 53 of 53 | 201 | 82 of 1,984 | 45 of 64 | 153 of 105,152 | g54a |
| four-bit adder, 53 pairs | raised noise, no spread | noise power x256 | 53 of 53 | 201 | 694 of 1,984 | 64 of 64 | 2,322 of 105,152 | g54a |
| eight-bit adder, 169 pairs | raised noise, no spread | noise power x128 | 169 of 169 | 197 | 192 of 1,984 | 61 of 64 | 752 of 335,296 | g54d |
| eight-bit adder, 169 pairs | raised noise, no spread | noise power x256 | 169 of 169 | 197 | 1,395 of 1,984 | 64 of 64 | 12,979 of 335,296 | g54d |

An addition is wrong when any output pair is wrong in that slot. A run has 31 additions. The run without noise or spread is judged when the next pairs decide (refcheck.py).

## T-6. Layouts with state: the serial adder and the accumulator

| layout | note | condition | pairs right without noise or spread | lowest level without noise or spread (mV) | wrong sums or words | runs with a wrong decision | wrong decisions of any pair | batch |
|---|---|---|---|---|---|---|---|---|
| serial adder, 20 pairs |  | as designed | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | inductance spread 3 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | inductance spread 5 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | every spread at once | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | pump phase error 10 degrees | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | pump phase error 20 degrees | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | pump phase error 30 degrees | 20 of 20 | 204 | 2 of 32 sums | 2 of 32 | 18 of 19,840 | g28c |
| serial adder, 20 pairs |  | pump phase error 45 degrees | 20 of 20 | 204 | 11 of 32 sums | 17 of 32 | 826 of 19,840 | g28c |
| serial adder, 20 pairs |  | link strength error 10 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | link strength error 20 % | 20 of 20 | 204 | 2 of 32 sums | 5 of 32 | 46 of 19,840 | g28c |
| serial adder, 20 pairs |  | link strength error 30 % | 20 of 20 | 204 | 16 of 32 sums | 21 of 32 | 1,412 of 19,840 | g28c |
| serial adder, 20 pairs |  | clock timing error 2 % of the period | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | clock timing error 5 % of the period | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | pump level error 20 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | diode current spread 10 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | difference inside a pair 5 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | inductance 3 %, diodes 5 %, inside a pair 2 %, pump level 10 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | the same with links 10 % and clock 2 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | the same with pump phase 10 degrees | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g28c |
| serial adder, 20 pairs |  | every spread at once, doubled except the inductance | 20 of 20 | 204 | 17 of 32 sums | 26 of 32 | 1,551 of 19,840 | g28c |
| serial adder, 20 pairs |  | noise power x4.78 | 20 of 20 | 204 | 0 of 127 sums | 0 of 127 | 0 of 78,740 | g28c |
| serial adder, 20 pairs |  | noise power x16 | 20 of 20 | 204 | 0 of 127 sums | 0 of 127 | 0 of 78,740 | g28c |
| serial adder, 20 pairs |  | noise power x64 | 20 of 20 | 204 | 0 of 127 sums | 0 of 127 | 0 of 78,740 | g28c |
| serial adder, 20 pairs |  | noise power x256 | 20 of 20 | 204 | 123 of 127 sums | 127 of 127 | 8,402 of 78,740 | g28c |
| accumulator of eight-bit words, 84 pairs |  | as designed | 84 of 84 | 188 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g28d |
| accumulator of eight-bit words, 84 pairs |  | inductance spread 3 % | 84 of 84 | 188 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g28d |
| accumulator of eight-bit words, 84 pairs |  | inductance spread 5 % | 84 of 84 | 188 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g28d |
| accumulator of eight-bit words, 84 pairs |  | every spread at once | 84 of 84 | 188 | 3 of 128 words | 1 of 32 | 503 of 82,880 | g28d |
| accumulator of eight-bit words, 84 pairs |  | noise power x4.78 | 84 of 84 | 188 | 0 of 256 words | 0 of 64 | 0 of 165,760 | g28d |
| accumulator of eight-bit words, 84 pairs |  | noise power x16 | 84 of 84 | 188 | 0 of 256 words | 0 of 64 | 0 of 165,760 | g28d |
| accumulator of eight-bit words, 84 pairs |  | pump phase error 20 degrees | 84 of 84 | 188 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g28d |
| accumulator of eight-bit words, 84 pairs |  | link strength error 20 % | 84 of 84 | 188 | 50 of 128 words | 17 of 32 | 9,360 of 82,880 | g28d |
| accumulator of eight-bit words, 84 pairs |  | clock timing error 5 % of the period | 84 of 84 | 188 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g28d |
| accumulator of eight-bit words, 84 pairs |  | every spread at once with pump phase 10 degrees | 84 of 84 | 188 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g28d |
| serial adder, 20 pairs |  | no spread, no noise | 20 of 20 | 204 | 0 of 1 sums | 0 of 1 | 0 of 620 | g30 |
| serial adder, 20 pairs |  | inductance spread 3 %, no noise | 20 of 20 | 204 | 0 of 16 sums | 0 of 16 | 0 of 9,920 | g30 |
| serial adder, 20 pairs |  | inductance spread 3 %, physical noise | 20 of 20 | 204 | 0 of 16 sums | 0 of 16 | 0 of 9,920 | g30 |
| serial adder, 20 pairs |  | supply 0.880 V, inductance spread 3 % | 20 of 20 | 29 | 18 of 32 sums | 23 of 32 | 680 of 19,840 | g31 |
| serial adder, 20 pairs |  | supply 0.895 V, inductance spread 3 % | 20 of 20 | 102 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | supply 0.910 V, inductance spread 3 % | 20 of 20 | 147 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | supply 0.970 V, inductance spread 3 % | 20 of 20 | 234 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | supply 0.985 V, inductance spread 3 % | 20 of 20 | 243 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | supply 1.000 V, inductance spread 3 % | 20 of 20 | 249 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | supply 1.015 V, inductance spread 3 % | 20 of 20 | 252 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | pump 15 %, inductance spread 3 % | 20 of 20 | 170 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | pump 20 %, inductance spread 3 % | 20 of 20 | 193 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | pump 30 %, inductance spread 3 % | 20 of 20 | 205 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | pump 35 %, inductance spread 3 % | 20 of 20 | 186 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | pump 40 %, inductance spread 3 % | 20 of 20 | 118 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | links 3.0 %, inductance spread 3 % | 20 of 20 | 178 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | links 3.0 %, noise power x64 | 20 of 20 | 178 | 125 of 127 sums | 127 of 127 | 12,185 of 78,740 | g31 |
| serial adder, 20 pairs |  | links 4.5 %, inductance spread 3 % | 20 of 20 | 199 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | links 4.5 %, noise power x64 | 20 of 20 | 199 | 30 of 127 sums | 52 of 127 | 698 of 78,740 | g31 |
| serial adder, 20 pairs |  | links 7.5 %, inductance spread 3 % | 20 of 20 | 195 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | links 7.5 %, noise power x64 | 20 of 20 | 195 | 0 of 127 sums | 0 of 127 | 0 of 78,740 | g31 |
| serial adder, 20 pairs |  | links 9.0 %, inductance spread 3 % | 20 of 20 | 179 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | links 9.0 %, noise power x64 | 20 of 20 | 179 | 0 of 127 sums | 0 of 127 | 0 of 78,740 | g31 |
| serial adder, 20 pairs |  | links 12.0 %, inductance spread 3 % | 16 of 20 | 2 | 30 of 32 sums | 32 of 32 | 999 of 19,840 | g31 |
| serial adder, 20 pairs |  | links 12.0 %, noise power x64 | 16 of 20 | 2 | 127 of 127 sums | 127 of 127 | 3,407 of 78,740 | g31 |
| serial adder, 20 pairs |  | slot 48 ps, inductance spread 3 % | 20 of 20 | 174 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | slot 57 ps, inductance spread 3 % | 20 of 20 | 188 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | slot 81 ps, inductance spread 3 % | 20 of 20 | 208 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g31 |
| serial adder, 20 pairs |  | supply level error 1 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g34c |
| serial adder, 20 pairs |  | supply level error 2 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g34c |
| serial adder, 20 pairs |  | supply level error 3 % | 20 of 20 | 204 | 0 of 32 sums | 1 of 32 | 42 of 19,840 | g34c |
| serial adder, 20 pairs |  | damping resistor spread 5 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g34c |
| serial adder, 20 pairs |  | damping resistor spread 10 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g34c |
| serial adder, 20 pairs |  | damping resistor spread 20 % | 20 of 20 | 204 | 2 of 32 sums | 6 of 32 | 259 of 19,840 | g34c |
| serial adder, 20 pairs |  | pump phase error per clock phase 5 degrees | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g34c |
| serial adder, 20 pairs |  | pump phase error per clock phase 10 degrees | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g34c |
| serial adder, 20 pairs |  | pump phase error per clock phase 20 degrees | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g34c |
| serial adder, 20 pairs |  | input phase -0.250 pi | 20 of 20 | 205 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g34c |
| serial adder, 20 pairs |  | input phase -0.125 pi | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g34c |
| serial adder, 20 pairs |  | input phase +0.125 pi | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g34c |
| serial adder, 20 pairs |  | input phase +0.250 pi | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g34c |
| serial adder, 20 pairs |  | every spread at once with pump phase 10 degrees, plus supply level 1 % and damping resistor 5 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g34c |
| serial adder, 20 pairs |  | every spread at once with pump phase 10 degrees, plus supply level 2 % and damping resistor 10 % | 20 of 20 | 204 | 3 of 32 sums | 5 of 32 | 92 of 19,840 | g34c |
| accumulator of eight-bit words, 84 pairs |  | supply level error 2 % | 84 of 84 | 188 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g34d |
| accumulator of eight-bit words, 84 pairs |  | damping resistor spread 10 % | 84 of 84 | 188 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g34d |
| accumulator of eight-bit words, 84 pairs |  | pump phase error per clock phase 10 degrees | 84 of 84 | 188 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g34d |
| accumulator of eight-bit words, 84 pairs |  | every spread at once with pump phase 10 degrees, plus supply level 1 % and damping resistor 5 % | 84 of 84 | 188 | 4 of 128 words | 2 of 32 | 549 of 82,880 | g34d |
| accumulator of eight-bit words, 84 pairs |  | supply 0.910 V, inductance spread 3 % | 84 of 84 | 137 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g34d |
| accumulator of eight-bit words, 84 pairs |  | supply 0.970 V, inductance spread 3 % | 84 of 84 | 220 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g34d |
| accumulator of eight-bit words, 84 pairs |  | pump 20 %, inductance spread 3 % | 84 of 84 | 177 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g34d |
| accumulator of eight-bit words, 84 pairs |  | pump 30 %, inductance spread 3 % | 84 of 84 | 192 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g34d |
| serial adder, 20 pairs | other carriers | c160: inductance spread 3 % | 20 of 20 | 216 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g35b |
| serial adder, 20 pairs | other carriers | c160: every spread at once with pump phase 10 degrees | 20 of 20 | 216 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g35b |
| serial adder, 20 pairs | other carriers | c320: inductance spread 3 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g35b |
| serial adder, 20 pairs | other carriers | c320: every spread at once with pump phase 10 degrees | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g35b |
| serial adder, 20 pairs | other carriers | c450: inductance spread 3 % | 20 of 20 | 149 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g35b |
| serial adder, 20 pairs | other carriers | c450: every spread at once with pump phase 10 degrees | 20 of 20 | 149 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g35b |
| serial adder, 20 pairs | other carriers | c640: inductance spread 3 % | 20 of 20 | 84 | 10 of 32 sums | 15 of 32 | 175 of 19,840 | g35b |
| serial adder, 20 pairs | other carriers | c640: every spread at once with pump phase 10 degrees | 20 of 20 | 84 | 24 of 32 sums | 26 of 32 | 1,815 of 19,840 | g35b |
| serial adder, 20 pairs | other carriers | c450t35: inductance spread 3 % | 20 of 20 | 190 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g35b |
| serial adder, 20 pairs | other carriers | c450t35: every spread at once with pump phase 10 degrees | 20 of 20 | 190 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g35b |
| serial adder, 20 pairs | other carriers | c640t35: inductance spread 3 % | 20 of 20 | 95 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g35b |
| serial adder, 20 pairs | other carriers | c640t35: every spread at once with pump phase 10 degrees | 20 of 20 | 95 | 9 of 32 sums | 14 of 32 | 134 of 19,840 | g35b |
| serial adder, 20 pairs | other carriers | c900t35: inductance spread 3 % | 20 of 20 | 81 | 14 of 32 sums | 19 of 32 | 389 of 19,840 | g35b |
| serial adder, 20 pairs | other carriers | c900t35: every spread at once with pump phase 10 degrees | 20 of 20 | 81 | 21 of 32 sums | 28 of 32 | 945 of 19,840 | g35b |
| serial adder, 20 pairs |  | slot 38 ps, inductance spread 3 % | 20 of 20 | 83 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g37d |
| serial adder, 20 pairs |  | c160: inductance spread 3 % | 20 of 20 | 216 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g37d |
| serial adder, 20 pairs |  | c160: every spread at once with pump phase 10 degrees | 20 of 20 | 216 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g37d |
| serial adder, 20 pairs |  | c320: inductance spread 3 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g37d |
| serial adder, 20 pairs |  | c320: every spread at once with pump phase 10 degrees | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g37d |
| serial adder, 20 pairs |  | c450: inductance spread 3 % | 20 of 20 | 149 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g37d |
| serial adder, 20 pairs |  | c450: every spread at once with pump phase 10 degrees | 20 of 20 | 149 | 0 of 32 sums | 1 of 32 | 2 of 19,840 | g37d |
| serial adder, 20 pairs |  | c640: inductance spread 3 % | 20 of 20 | 84 | 18 of 32 sums | 20 of 32 | 1,364 of 19,840 | g37d |
| serial adder, 20 pairs |  | c640: every spread at once with pump phase 10 degrees | 20 of 20 | 84 | 18 of 32 sums | 22 of 32 | 1,561 of 19,840 | g37d |
| serial adder, 20 pairs |  | c450t35: inductance spread 3 % | 20 of 20 | 190 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g37d |
| serial adder, 20 pairs |  | c450t35: every spread at once with pump phase 10 degrees | 20 of 20 | 190 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g37d |
| serial adder, 20 pairs |  | c640t35: inductance spread 3 % | 20 of 20 | 95 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g37d |
| serial adder, 20 pairs |  | c640t35: every spread at once with pump phase 10 degrees | 20 of 20 | 95 | 5 of 32 sums | 11 of 32 | 325 of 19,840 | g37d |
| serial adder, 20 pairs |  | c900t35: inductance spread 3 % | 20 of 20 | 81 | 10 of 32 sums | 17 of 32 | 547 of 19,840 | g37d |
| serial adder, 20 pairs |  | c900t35: every spread at once with pump phase 10 degrees | 20 of 20 | 81 | 19 of 32 sums | 27 of 32 | 679 of 19,840 | g37d |
| serial adder, 20 pairs |  | full set x 0.75 | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | full set x 0.5 | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | 1.075 THz: inductance spread 3 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | 1.075 THz: inductance spread 5 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | 1.075 THz: full set x 0.5 | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | 1.075 THz: full set x 1 | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j052t21: inductance spread 3 % | 20 of 20 | 205 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j052t21: full set x 0.5 | 20 of 20 | 205 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j080t21: inductance spread 3 % | 20 of 20 | 208 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j080t21: full set x 0.5 | 20 of 20 | 208 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j125t21: inductance spread 3 % | 20 of 20 | 160 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j125t21: full set x 0.5 | 20 of 20 | 160 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j170t21: inductance spread 3 % | 20 of 20 | 33 | 30 of 32 sums | 32 of 32 | 1,625 of 19,840 | g42 |
| serial adder, 20 pairs |  | j170t21: full set x 0.5 | 20 of 20 | 33 | 29 of 32 sums | 31 of 32 | 2,421 of 19,840 | g42 |
| serial adder, 20 pairs |  | j052t35: inductance spread 3 % | 20 of 20 | 190 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j052t35: full set x 0.5 | 20 of 20 | 190 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j080t35: inductance spread 3 % | 20 of 20 | 195 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j080t35: full set x 0.5 | 20 of 20 | 195 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j125t35: inductance spread 3 % | 20 of 20 | 123 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j125t35: full set x 0.5 | 20 of 20 | 123 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j170t35: inductance spread 3 % | 20 of 20 | 51 | 25 of 32 sums | 30 of 32 | 992 of 19,840 | g42 |
| serial adder, 20 pairs |  | j170t35: full set x 0.5 | 20 of 20 | 51 | 25 of 32 sums | 28 of 32 | 1,255 of 19,840 | g42 |
| serial adder, 20 pairs |  | j052t50: inductance spread 3 % | 20 of 20 | 165 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j052t50: full set x 0.5 | 20 of 20 | 165 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j080t50: inductance spread 3 % | 20 of 20 | 180 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j080t50: full set x 0.5 | 20 of 20 | 180 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j125t50: inductance spread 3 % | 20 of 20 | 132 | 1 of 32 sums | 1 of 32 | 2 of 19,840 | g42 |
| serial adder, 20 pairs |  | j125t50: full set x 0.5 | 20 of 20 | 132 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g42 |
| serial adder, 20 pairs |  | j170t50: inductance spread 3 % | 20 of 20 | 80 | 13 of 32 sums | 17 of 32 | 383 of 19,840 | g42 |
| serial adder, 20 pairs |  | j170t50: full set x 0.5 | 20 of 20 | 80 | 1 of 32 sums | 4 of 32 | 18 of 19,840 | g42 |
| accumulator of eight-bit words, 84 pairs |  | full set x 0.5 | 84 of 84 | 188 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g43 |
| accumulator of eight-bit words, 84 pairs |  | 1.075 THz: inductance spread 3 % | 84 of 84 | 188 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g43 |
| accumulator of eight-bit words, 84 pairs |  | 1.075 THz: inductance spread 5 % | 84 of 84 | 188 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g43 |
| accumulator of eight-bit words, 84 pairs |  | 1.075 THz: full set x 0.5 | 84 of 84 | 188 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g43 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.880 V, inductance spread 3 % | 20 of 20 | 29 | 30 of 32 sums | 32 of 32 | 1,460 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.895 V, inductance spread 3 % | 20 of 20 | 102 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.910 V, inductance spread 3 % | 20 of 20 | 147 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.970 V, inductance spread 3 % | 20 of 20 | 234 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.985 V, inductance spread 3 % | 20 of 20 | 243 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 1.000 V, inductance spread 3 % | 20 of 20 | 249 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 1.015 V, inductance spread 3 % | 20 of 20 | 252 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump 15 %, inductance spread 3 % | 20 of 20 | 170 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump 20 %, inductance spread 3 % | 20 of 20 | 193 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump 30 %, inductance spread 3 % | 20 of 20 | 205 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump 35 %, inductance spread 3 % | 20 of 20 | 186 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump 40 %, inductance spread 3 % | 20 of 20 | 118 | 1 of 32 sums | 3 of 32 | 34 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: links 3.0 %, inductance spread 3 % | 20 of 20 | 178 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: links 4.5 %, inductance spread 3 % | 20 of 20 | 199 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: links 7.5 %, inductance spread 3 % | 20 of 20 | 195 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: links 9.0 %, inductance spread 3 % | 20 of 20 | 179 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: links 12.0 %, inductance spread 3 % | 16 of 20 | 2 | 30 of 32 sums | 32 of 32 | 1,079 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: slot 48 ps, inductance spread 3 % | 20 of 20 | 174 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: slot 57 ps, inductance spread 3 % | 20 of 20 | 188 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: slot 81 ps, inductance spread 3 % | 20 of 20 | 208 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply level error 1 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply level error 2 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply level error 3 % | 20 of 20 | 204 | 2 of 32 sums | 3 of 32 | 8 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: damping resistor spread 5 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: damping resistor spread 10 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: damping resistor spread 20 % | 20 of 20 | 204 | 8 of 32 sums | 10 of 32 | 230 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump phase error per clock phase 5 degrees | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump phase error per clock phase 10 degrees | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump phase error per clock phase 20 degrees | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: input phase -0.250 pi | 20 of 20 | 205 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: input phase -0.125 pi | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: input phase +0.125 pi | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: input phase +0.250 pi | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump phase error 10 degrees, inductance spread 3 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump phase error 20 degrees, inductance spread 3 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump phase error 30 degrees, inductance spread 3 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: link strength error 10 %, inductance spread 3 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: link strength error 20 %, inductance spread 3 % | 20 of 20 | 204 | 7 of 32 sums | 12 of 32 | 487 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: clock timing error 2 % of the period, inductance spread 3 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: clock timing error 5 % of the period, inductance spread 3 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump level error 20 %, inductance spread 3 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: diode current spread 10 %, inductance spread 3 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| serial adder, 20 pairs | 1-THz-class cell at its own noise | 1.075 THz: difference inside a pair 5 %, inductance spread 3 % | 20 of 20 | 204 | 0 of 32 sums | 0 of 32 | 0 of 19,840 | g49 |
| accumulator of eight-bit words, 84 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.910 V, inductance spread 3 % | 84 of 84 | 137 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g51 |
| accumulator of eight-bit words, 84 pairs | 1-THz-class cell at its own noise | 1.075 THz: supply 0.970 V, inductance spread 3 % | 84 of 84 | 220 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g51 |
| accumulator of eight-bit words, 84 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump 20 %, inductance spread 3 % | 84 of 84 | 177 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g51 |
| accumulator of eight-bit words, 84 pairs | 1-THz-class cell at its own noise | 1.075 THz: pump 30 %, inductance spread 3 % | 84 of 84 | 192 | 0 of 128 words | 0 of 32 | 0 of 82,880 | g51 |
| serial adder, 20 pairs | raised noise, no spread | noise power x128 | 20 of 20 | 204 | 30 of 127 sums | 52 of 127 | 932 of 78,740 | g54b |
| accumulator of eight-bit words, 84 pairs | raised noise, no spread | noise power x64 | 84 of 84 | 188 | 1 of 256 words | 1 of 64 | 60 of 165,760 | g54c |
| accumulator of eight-bit words, 84 pairs | raised noise, no spread | noise power x128 | 84 of 84 | 188 | 97 of 256 words | 55 of 64 | 12,972 of 165,760 | g54c |
| accumulator of eight-bit words, 84 pairs | raised noise, no spread | noise power x256 | 84 of 84 | 188 | 233 of 256 words | 64 of 64 | 56,229 of 165,760 | g54c |

In the serial adder a run is one long sum, and it is wrong when any sum bit is wrong. In the accumulator a word is wrong when any of its sum bits is wrong.

## T-7. Rows of 92 pairs

| condition | pairs right without noise or spread | runs | slots counted | first-wrong events in decisions at risk | batch |
|---|---|---|---|---|---|
| as designed | 92 of 92 | 32 | 7 | 0 in 20,384 | g28f |
| inductance spread 3 % | 92 of 92 | 32 | 7 | 0 in 20,384 | g28f |
| inductance spread 5 % | 92 of 92 | 32 | 7 | 0 in 20,384 | g28f |
| every spread at once | 92 of 92 | 32 | 7 | 0 in 20,384 | g28f |
| no pump | 5 of 92 | 32 | 7 | 224 in 1,160 | g28f |

0.94 V, 25 % pump, links 6 %. Counted as in T-1. Without the pump a pair is right only by chance.

## T-8. Spread budget: the four-bit adder with the full set of nine spreads, or a fraction of it

| fraction of the full set | noise | failing runs | share, with its exact 95 % interval | wrong additions | bad pairs per thousand, with its interval | share of machines of 1,000 pairs right | share of machines of 10,000 pairs right | batch |
|---|---|---|---|---|---|---|---|---|
| 1 | 1-THz-class cell | 7 of 256 | 2.7 % (1.1 to 5.6 %) | 23 of 7,936 | 0.52 (0.21 to 1.05) | 0.60 | 0.006 | g52 |
| 0.75 | 1-THz-class cell | 1 of 256 | 0.39 % (0.01 to 2.2 %) | 3 of 7,936 | 0.07 (0.00 to 0.41) | 0.93 | 0.479 | g52 |
| 1 | 225-GHz cell | 5 of 256 | 2.0 % (0.64 to 4.5 %) | 26 of 7,936 | 0.37 (0.12 to 0.85) | 0.69 | 0.025 | g52 |
| 0.5 | 1-THz-class cell | 0 of 256 | 0.0 % (0.0 to 1.4 %) | 0 of 7,936 | 0.00 (0.00 to 0.27) | 1.00 | 1.000 | g53 |
| 0.625 | 1-THz-class cell | 0 of 256 | 0.0 % (0.0 to 1.4 %) | 0 of 7,936 | 0.00 (0.00 to 0.27) | 1.00 | 1.000 | g53 |
| 0.875 | 1-THz-class cell | 10 of 256 | 3.9 % (1.9 to 7.1 %) | 24 of 7,936 | 0.74 (0.36 to 1.33) | 0.48 | 0.001 | g53 |
| 0.5 | 225-GHz cell | 0 of 256 | 0.0 % (0.0 to 1.4 %) | 0 of 7,936 | 0.00 (0.00 to 0.27) | 1.00 | 1.000 | g53 |
| 0.75 | 225-GHz cell | 0 of 256 | 0.0 % (0.0 to 1.4 %) | 0 of 7,936 | 0.00 (0.00 to 0.27) | 1.00 | 1.000 | g53 |

0.94 V, 25 % pump, links 6 %, 53 pairs. The full set has nine rms spreads: inductance 3 %, diode current 5 %, difference inside a pair 2 %, pump phase 10 degrees, pump level 10 %, link strength 10 %, clock timing 2 % of the period, supply level 1 % and damping resistor 5 %. A fraction s multiplies each by s. A run fails when any of its 31 additions is wrong. The interval is the exact (Clopper-Pearson) binomial interval. Bad pairs per thousand is the failing share divided by 53. The two columns on machines assume that pairs fail independently, which no run has tested; no layout larger than 53 pairs has been run with 256 draws.

## Batches not in these tables

- g29a: copy of batch g29 (same result index and arrays, made by a comparison script under another name); nothing stored
- g29b (row, 16 pairs): results stored, but no analysis file for these tables (the checks of time step, stub grid and precision were compared by a separate session script)
- g29c (row, 16 pairs): results stored, but no analysis file for these tables (the checks of time step, stub grid and precision were compared by a separate session script)
- g30a: copy of batch g30 (same result index and arrays, made by a comparison script under another name); nothing stored
- g30b (serial adder, 20 pairs): results stored, but no analysis file for these tables (the checks of time step, stub grid and precision were compared by a separate session script)
- g38a (serial adder, 20 pairs): results stored, but no analysis file for these tables (the checks of time step, stub grid and precision were compared by a separate session script)
- g38b (serial adder, 20 pairs): results stored, but no analysis file for these tables (the checks of time step, stub grid and precision were compared by a separate session script)

Lines left out because they have link capacitors (cc > 0): g52: 1.075 THz: full set x 1, with the capacitors, 256 runs.

