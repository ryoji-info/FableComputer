# -*- coding: utf-8 -*-
"""Runnable listing for the repository improvement ledger (Fable session 2026-07-26 (III)).

Reproduces every claim the note labels *demonstrated*. Paired with ledger_sweep.py
(Artifact 2), which carries the defect-signature completeness sweep.

    cd <repo root> && PYTHONIOENCODING=utf-8 python ledger_listing.py

Pure Python: no subprocess, no grep, every file opened with an explicit encoding, so
the output does not depend on the shell locale. Seconds to run; no solver stepping.
"""
import importlib, inspect, json, pathlib, re, sys

sys.path.insert(0, "fable-model-chain")
sys.path.insert(0, "fable-model-quantum")
R = lambda p: pathlib.Path(p).read_text(encoding="utf-8", errors="replace")
H = lambda n, t: print(f"\n--- {n}. {t} " + "-" * max(0, 58 - len(t)))

# 1 - regen._cavity does not forward f0 (07-25 WP1 item 3)
H(1, "_cavity does not forward f0")
import constants as C, ds_cell, regen
print("  cell_length(s)  =", ds_cell.cell_length(ds_cell.plasmon_speed()))
print("  pulse_gain(0.7) =", regen.pulse_net_gain_dB(0.7))
C.f0 = 2e12; importlib.reload(regen)
print("  after constants.f0 = 2e12:")
print("  cell_length(s)  =", ds_cell.cell_length(ds_cell.plasmon_speed()), "<- unchanged")
print("  pulse_gain(0.7) =", regen.pulse_net_gain_dB(0.7), "<- sign flip")
C.f0 = 1e12; importlib.reload(regen)

# 2/3 - solver.run never forwards ncyc; rep_ratio is dead
H(2, "solver.run has no ncyc; rep_ratio is dead")
import solver
print("  'ncyc' in signature(run):", "ncyc" in inspect.signature(solver.run).parameters)
print("  _pulse_train call sites:",
      [l.strip()[:52] for l in inspect.getsource(solver.run).splitlines() if "_pulse_train(" in l])
print("  _pulse_train default ncyc:", inspect.signature(solver._pulse_train).parameters["ncyc"].default)
print("  pulse_gain over rep_ratio:", [regen.pulse_net_gain_dB(0.7, rep_ratio=r) for r in (0.05, 0.25, 0.9, 3.0)])

# 4 - the avg16 column is an ideal-sampler identity; variance is not the probability
H(4, "avg16 identity: variance vs probability")
import qmac, qdecode
states, xr = qmac.levels_at_decision(300, 400)
V_sig, V_amp = max(s.V for s in states.values()), qdecode.decoder_amp_noise(300)
V_static = qdecode.threshold_band_variance(xr)
V = qmac.decision_variance(states, xr, 300, n_avg=16)
e16 = qmac.error_2bit(300, 400, n_avg=16)
print(f"  V_sig={V_sig:.6f} V_amp={V_amp:.6f} V_static={V_static:.6f}")
print("  decision VARIANCE   =", V)
print("  symbol-error PROB   =", e16)
print("  == results.json avg16_2bit_300K:", e16 == json.loads(R("fable-model-quantum/results.json"))["avg16_2bit_300K"])
print("  == error_2bit(300,6400,n_avg=1):", e16 == qmac.error_2bit(300, 6400, n_avg=1))

# 5 - null in the T_*_below_* keys means "floor above target at every T"
H(5, "threshold_temperature returns None by design")
q = json.loads(R("fable-model-quantum/results.json"))
print("  T_2bit_below_1e-6:", q["T_2bit_below_1e-6"], " T_2bit_below_1e-9:", q["T_2bit_below_1e-9"])
print("  quantum_floor.2bit:", q["quantum_floor"]["2bit"], "> 1e-6:", q["quantum_floor"]["2bit"] > 1e-6)

# 6 - compression at the two planes the ledger must distinguish
H(6, "compression: which plane the 0.06 dB belongs to")
import cell
for a in (2e-3, 3e-3, 0.0116):
    print(f"  cell.compression_dB({a}) = {cell.compression_dB(a)}")

# 7 - the phantom second-order scheme
H(7, "phantom MacCormack option")
print("  'MacCormack' in solver.py:", "MacCormack" in R("fable-model-chain/solver.py"))
print("  steppers present:", [n for n in dir(solver) if "step" in n.lower()])

# 8 - what the manuscripts do and do not cite (whitespace-normalized)
H(8, "manuscript greps, raw vs normalized")
print("  NOTE: the promoted 2026-07-26 note measured these against Part I v5.6 / Part II v1.7,")
print("  where every count below was 0. Non-zero counts today are the v6.0/v2.0 corrections")
print("  landing (the timing thread is now cited), not a failed reproduction.")
try:
    from pypdf import PdfReader
    for path, pats in (("papers/Fable-Computer-Part-I.pdf",
                        ["2026-07-2", "loaded fan-out", "burst-scaling", "Quantifying the residual data ISI"]),
                       ("papers/Fable-Computer-Part-II.pdf",
                        ["flush", "ring-down", "ringdown", "reset", "one MAC per 4-ps slot"])):
        raw = "\n".join((p.extract_text() or "") for p in PdfReader(path).pages)
        nrm = re.sub(r"\s+", " ", re.sub(r"-\s*\n\s*", "", raw))
        m = re.search(r'Revision v[0-9.]+', nrm)
        # since the v6.0/v2.0 revision the manuscripts carry no version statement;
        # versions live in papers/REVISION-HISTORY.md
        print(f"  {path}  ({m.group(0) if m else 'no in-document version statement (v6.0/v2.0 convention)'})")
        for p in pats:
            print(f"    {p!r:40s} raw={len(re.findall(re.escape(p), raw, re.I)):2d} normalized={len(re.findall(re.escape(p), nrm, re.I)):2d}")
except ImportError:
    print("  (pypdf missing - skipped)")
print("\n(The defect-signature sweep lives in ledger_sweep.py - Artifact 2.)")
