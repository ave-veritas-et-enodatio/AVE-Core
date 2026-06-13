"""Genesis v17 — moving resonator smoke tests."""

from ave.core import chiral_lattice as cl
from ave.core.chiral_lattice_v17 import run_p17_moving_resonator_cell, v17_gates


def test_p17_full_stack_runs():
    net = cl.build_srs_net(8, "right")
    r = run_p17_moving_resonator_cell(
        net,
        "smoke",
        n_drive_mult=0.5,
        comoving=True,
        tau_steps=8,
        n_quiet_mult=2.0,
    )
    assert r.comoving_on
    assert r.bulk_wall_on
    assert r.peak_metric == "pocket"
    assert r.centroid_disp >= 0.0


def test_v17_smoke_gates_complete():
    g = v17_gates(L=6, smoke=True)
    assert g["verdict"] in (
        "REMANENCE-LANDED",
        "PARTIAL-REMANENCE",
        "MOVING-CAVITY-SET",
        "CAVITY-SET-ONLY",
        "LOOP-GAP-OPEN",
    )
    assert len(g["P17_ringup_sweep"]) >= 1
