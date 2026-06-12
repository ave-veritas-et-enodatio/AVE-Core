"""Genesis v16 — cavity ring-up + P11 smoke tests."""

from ave.core import chiral_lattice as cl
from ave.core.chiral_lattice_v16 import run_p16_cavity_ringup_cell, v16_gates


def test_p16_cavity_cell_runs():
    net = cl.build_srs_net(8, "right")
    r = run_p16_cavity_ringup_cell(
        net, "smoke", n_drive_mult=0.5, tau_steps=8, n_quiet_mult=2.0
    )
    assert r.bulk_wall_on
    assert r.n_drive >= 10
    assert r.bin_label in (
        "REMANENCE-CANDIDATE",
        "CAVITY-SET",
        "CONFINED-NO-REMANENCE",
        "DISPERSED",
    )


def test_v16_smoke_gates_complete():
    g = v16_gates(L=6, smoke=True)
    assert g["verdict"] in (
        "REMANENCE-LANDED",
        "PARTIAL",
        "CAVITY-SET-ONLY",
        "LOOP-GAP-OPEN",
    )
    assert len(g["P16_ringup_sweep"]) >= 1
