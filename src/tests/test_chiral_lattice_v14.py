"""Genesis v14 — cavity + comoving transport smoke tests."""

from ave.core import chiral_lattice as cl
from ave.core.chiral_lattice_v14 import run_p14_stack_cell, v14_gates, v14b_gates


def test_p14_full_stack_runs():
    net = cl.build_srs_net(8, "right")
    cell = run_p14_stack_cell(
        net, "smoke", bulk_wall=True, comoving=True, n_steps=30, tau_steps=8
    )
    assert cell.bulk_wall_on
    assert cell.comoving_on
    assert cell.E_frac_interior >= 0.0


def test_p14_pinned_vs_comoving_gain_smoke():
    net = cl.build_srs_net(8, "right")
    full = run_p14_stack_cell(
        net, "full", bulk_wall=True, comoving=True, n_steps=40, tau_steps=8
    )
    pinned = run_p14_stack_cell(
        net, "pinned", bulk_wall=True, comoving=False, n_steps=40, tau_steps=8
    )
    assert full.centroid_disp >= 0.0
    assert pinned.centroid_disp >= 0.0


def test_v14_smoke_gates_complete():
    g = v14_gates(L=6, smoke=True)
    assert g["verdict"] in (
        "TRANSPORT-IN-CAVITY-LANDED",
        "PARTIAL",
        "CAVITY-BREAK",
        "ENGINE-GAP",
    )
    assert "P14_full_stack" in g
    assert "P14_pinned_cavity" in g
    assert "P14_op3_only_wall" in g
    assert "P14_boost_sweep_gain" in g


def test_v14b_pocket_peak_field():
    net = cl.build_srs_net(8, "right")
    cell = run_p14_stack_cell(
        net, "full", bulk_wall=True, comoving=True, n_steps=30, tau_steps=8
    )
    assert cell.peak_metric == "pocket"
    assert cell.peak_pocket_retention >= 0.0


def test_v14b_smoke_gates():
    g = v14b_gates(L=6, smoke=True)
    assert g["verdict"] in (
        "TRANSPORT-IN-CAVITY-LANDED",
        "PARTIAL",
        "CAVITY-BREAK",
        "ENGINE-GAP",
    )
    assert "P14b_peak_pocket" in g
