# -*- coding: utf-8 -*-
"""Pin the published numbers and the record's standing corrections.

These tests exist because the repository's claims live in `results.json` and in the
manuscripts, and until now nothing checked that a refactor left them intact. They are
deliberately narrow: each one either pins a value that appears in a published artifact,
or asserts a correction that a promoted note requires.

Run:  PYTHONIOENCODING=utf-8 python -m pytest -q
Requested by ROADMAP WP1 ("CI that runs every self-check on every PR") and by
notes/2026-07-22-mth-numerical-vs-physical-viscosity.md, which asks for exactly the
M_th assertions below. See notes/2026-07-26-record-audit-ten-findings.md.
"""
import json
import math
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "fable-model-chain"))
sys.path.insert(0, str(ROOT / "fable-model-quantum"))

CHAIN = json.loads((ROOT / "fable-model-chain" / "results.json").read_text(encoding="utf-8"))
QUANT = json.loads((ROOT / "fable-model-quantum" / "results.json").read_text(encoding="utf-8"))


# --------------------------------------------------------------- published values

def test_quantum_avg16_column_is_pinned():
    """The headline avg16 column, bit-for-bit."""
    import qmac
    assert qmac.error_2bit(300, 400, n_avg=16) == QUANT["avg16_2bit_300K"]


def test_avg16_is_an_ideal_sampler_identity_not_an_accumulator():
    """16 slots at N=400 is exactly 1 slot at N=6400 — the identity that shows the
    column is bookkeeping, not physics (notes/2026-07-16-no-physical-avg16-accumulator)."""
    import qmac
    assert qmac.error_2bit(300, 400, n_avg=16) == qmac.error_2bit(300, 6400, n_avg=1)


def test_decision_variance_is_a_variance_not_a_probability():
    """Guards the conflation that a 2026-07-26 assessment caught: the decision
    variance is ~0.77 quadrature units; the symbol error is ~4.7e-7."""
    import qmac
    states, xr = qmac.levels_at_decision(300, 400)
    V = qmac.decision_variance(states, xr, 300, n_avg=16)
    assert 0.7 < V < 0.8
    assert qmac.error_2bit(300, 400, n_avg=16) < 1e-6


def test_quantum_floor_explains_the_null_threshold_keys():
    """`null` in T_*_below_* means the floor sits above the target at every
    temperature — not "not computed"."""
    import qerrors
    assert QUANT["T_2bit_below_1e-6"] is None
    assert QUANT["quantum_floor"]["2bit"] > 1e-6
    assert qerrors.threshold_temperature is not None  # the function exists


def test_chain_headline_gains_are_pinned():
    import regen
    assert regen.pulse_net_gain_dB(0.7) == pytest.approx(6.258296289342312, rel=0, abs=1e-12)
    assert CHAIN["pulse_gain_dB_at_0p7_streaming"] == pytest.approx(7.7967069614868425, abs=1e-12)


def test_cascade_per_cell_matches_the_notes_self_check():
    """gain(F=1, A_SAT=0.02) reproduces the shipped 0-dB-junction entry — the number
    the promoted fan-out notes compute at (notes/2026-07-20, notes/2026-07-21)."""
    assert CHAIN["cascade_per_cell_dB"]["0"] == pytest.approx(8.401641447428242, abs=1e-9)


# ------------------------------------------------- corrections a note requires

def test_M_th_num_is_not_mistaken_for_the_physical_threshold():
    """notes/2026-07-22-mth-numerical-vs-physical-viscosity.md, verbatim request:
    assert the shipped LF threshold is not read as physical, and that the physical
    kinetic threshold is the 0.165 band."""
    lf = CHAIN["M_th_num"]
    analytic = CHAIN["M_th_353K"]
    assert lf == pytest.approx(0.168943, abs=5e-6), "the shipped coarse-grid LF value"
    assert analytic == pytest.approx(0.147083, abs=5e-6), "the small-M analytic value"
    # the LF value is NOT the physical threshold, and not the analytic one either
    assert not math.isclose(lf, 0.165, abs_tol=1e-3)
    assert not math.isclose(lf, analytic, abs_tol=1e-3)
    # the inviscid limit sits between them, nearer the analytic value
    inviscid = 0.149313
    assert analytic < inviscid < lf


def test_no_second_order_scheme_is_advertised():
    """notes/2026-07-26 finding 5: solver.py advertised a MacCormack option that does
    not exist. If a second-order stepper is ever added, this test should be updated
    deliberately rather than silently."""
    import solver
    src = (ROOT / "fable-model-chain" / "solver.py").read_text(encoding="utf-8")
    steppers = [n for n in dir(solver) if "step" in n.lower()]
    assert steppers == ["_step_LF"], steppers
    if "MacCormack" in src:
        assert "No second-order" in src, "MacCormack may only appear in the disclaimer"


def test_the_three_tracked_code_defects_are_still_described_accurately():
    """notes/2026-07-25 tracks three defects. This test does not fix them — it pins
    the state so that fixing one forces an update here, and so the note's claims stay
    true while they remain open."""
    import inspect
    import regen
    import solver
    # (1) solver.run does not forward ncyc
    assert "ncyc" not in inspect.signature(solver.run).parameters
    # (2) rep_ratio is accepted and unused
    vals = {regen.pulse_net_gain_dB(0.7, rep_ratio=r) for r in (0.05, 0.25, 0.9, 3.0)}
    assert len(vals) == 1
    # (3) _cavity does not forward f0: cell_length is import-time bound
    import constants as C
    import ds_cell
    before = ds_cell.cell_length(ds_cell.plasmon_speed())
    C.f0 = 2e12
    try:
        assert ds_cell.cell_length(ds_cell.plasmon_speed()) == before
    finally:
        C.f0 = 1e12


def test_plane_labels_are_present_where_the_record_requires_them():
    """notes/2026-07-17: the knee is a launch/drive-plane quantity. Guards against a
    regression to the retired 'intracavity' wording in released source."""
    # A line may mention "intracavity" only while disclaiming it or naming the plane.
    OK = ("mislabel", "not an intracavity", "NEITHER", "launch", "drive plane", "drive-plane")
    for rel in ("fable-model-quantum/qmac.py", "fable-model-quantum/qmode.py"):
        src = (ROOT / rel).read_text(encoding="utf-8")
        for line in src.splitlines():
            if "intracavity" in line and not any(k in line for k in OK):
                pytest.fail(f"{rel}: unqualified 'intracavity' -> {line.strip()[:90]}")
