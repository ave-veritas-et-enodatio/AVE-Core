"""Pytest gates for the transverse per-directed-bond graded scatter (Stage 1).

Prereg: research/2026-08-24_transverse-gamma-meanstest_prereg_FROZEN.md
(SS4.0 T1/T2 module gates, SS4.2 shared-kernel receipt, SS5 CS-7-swap, CT-1).
These are the VOID-linked module gates (prereg SS8 V1): the driver may not run
unless this file is green.
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.chiral_lattice import build_srs_net, scalar_tlm_step, scatter_matrix
from ave.solvers.transverse_graded_scatter import (
    BondTables,
    bond_admittance,
    energy_Y,
    gate_cs7_reconcile,
    gate_ct1_vertex,
    gate_so2_equivariance,
    gate_t1a_global_uniform,
    gate_t1b_boundary_set,
    saturation_kernel,
    scatter_coeffs,
    vector_graded_step,
)


@pytest.fixture(scope="module")
def net():
    return build_srs_net(L=4, enantiomorph="right")


@pytest.fixture(scope="module")
def tables(net):
    return BondTables(net)


def slab_field(tables, A, lo=1.0, hi=3.0):
    """Per-bond slab grading: A on bonds fully inside (lo, hi) cells, else cold."""
    x0, x1 = tables.b_x0, tables.b_x0 + tables.b_dx
    lo_x, hi_x = np.minimum(x0, x1), np.maximum(x0, x1)
    Ab = np.zeros(tables.n_bonds)
    Ab[(lo_x > lo) & (hi_x < hi)] = A
    return Ab


# ---------------------------------------------------------------------------
# The shared kernel (prereg SS4.2 receipt — bit-equality, no import of ave_chart
# into the scatter path)
# ---------------------------------------------------------------------------
def test_kernel_bit_equal_to_ave_chart():
    from ave.viz.ave_chart import saturation_kernel as chart_kernel

    A = np.concatenate([np.linspace(0.0, 1.0, 4001), [0.9682, 0.99, 1.0]])
    assert np.array_equal(saturation_kernel(A), chart_kernel(A))


def test_loading_maps_reciprocal_and_exact():
    A = np.array([0.0, 0.5, 0.9, 0.99])
    S = saturation_kernel(A)
    Ymag = bond_admittance(A, "magnetic")
    Yelec = bond_admittance(A, "electric")
    assert np.allclose(Ymag, 1.0 / np.sqrt(S), rtol=0, atol=0)
    assert np.allclose(Yelec, np.sqrt(S), rtol=0, atol=0)
    # reciprocal pair: z_mag * z_elec = 1  <=>  Ymag * Yelec = 1
    assert np.allclose(Ymag * Yelec, 1.0, atol=1e-15)
    # cold bond is matched under BOTH maps
    assert Ymag[0] == 1.0 and Yelec[0] == 1.0


def test_load_string_guard_raises():
    with pytest.raises(ValueError, match="sign-lock"):
        bond_admittance(np.array([0.5]), "electirc")  # typo must raise


# ---------------------------------------------------------------------------
# T1 cancellation gates (epic guard 4; VOID-linked)
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("load", ["magnetic", "electric"])
@pytest.mark.parametrize("A", [0.0, 0.9])
def test_t1a_global_uniform_collapses_to_bedrock(net, tables, load, A):
    g = gate_t1a_global_uniform(net, tables, A, load)
    assert g["pass"], g


@pytest.mark.parametrize("load", ["magnetic", "electric"])
def test_t1b_deviation_set_equals_mixed_admittance_set(tables, load):
    g = gate_t1b_boundary_set(tables, slab_field(tables, 0.9), load)
    assert g["pass"], g


def test_t1b_fires_negative_on_uniform_field(tables):
    """Both-directions fireability: a global-uniform field has an EMPTY mixed set
    and must FAIL T1(b) (n_deviating == 0)."""
    g = gate_t1b_boundary_set(tables, np.full(tables.n_bonds, 0.9), "magnetic")
    assert not g["pass"] and g["n_deviating"] == 0


# ---------------------------------------------------------------------------
# T2 / SO(2) equivariance (component-scalar loading fence) + decoupling
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("load", ["magnetic", "electric"])
def test_so2_equivariance_graded(net, tables, load):
    g = gate_so2_equivariance(net, tables, slab_field(tables, 0.9), load, steps=50)
    assert g["pass"], g


@pytest.mark.parametrize("load", ["magnetic", "electric"])
def test_component1_stays_identically_zero(net, tables, load):
    a_nodes = scatter_coeffs(tables.port_admittance(slab_field(tables, 0.9), load))
    conn = net.connect_index()
    rng = np.random.default_rng(3)
    V = np.zeros((net.n_nodes, net.degree, 2))
    V[:, :, 0] = rng.standard_normal((net.n_nodes, net.degree))
    for _ in range(100):
        V = vector_graded_step(V, a_nodes, conn)
    assert float(np.max(np.abs(V[:, :, 1]))) == 0.0


def test_all_cold_reproduces_scalar_trajectory(net, tables):
    """CS-4 form: the vector graded machinery with ALL bonds cold reproduces the
    uniform-scatter SCALAR trajectory on component 0 to <= 1e-12."""
    a_nodes = scatter_coeffs(tables.port_admittance(np.zeros(tables.n_bonds), "magnetic"))
    conn = net.connect_index()
    S_uni = scatter_matrix(net.degree)
    rng = np.random.default_rng(5)
    Vs = rng.standard_normal((net.n_nodes, net.degree))
    Vv = np.zeros((net.n_nodes, net.degree, 2))
    Vv[:, :, 0] = Vs
    dev = 0.0
    for _ in range(200):
        Vs = scalar_tlm_step(net, Vs, S_uni, conn)
        Vv = vector_graded_step(Vv, a_nodes, conn)
        dev = max(dev, float(np.max(np.abs(Vv[:, :, 0] - Vs))))
    assert dev <= 1e-12, dev


# ---------------------------------------------------------------------------
# E_Y losslessness (prereg SS4.1; the V2 norm)
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("load", ["magnetic", "electric"])
def test_energy_Y_conserved_under_graded_step(net, tables, load):
    Y_port = tables.port_admittance(slab_field(tables, 0.9), load)
    a_nodes = scatter_coeffs(Y_port)
    conn = net.connect_index()
    rng = np.random.default_rng(11)
    V = rng.standard_normal((net.n_nodes, net.degree, 2))
    E0 = energy_Y(V, Y_port)
    drift = 0.0
    for _ in range(200):
        V = vector_graded_step(V, a_nodes, conn)
        drift = max(drift, abs(energy_Y(V, Y_port) - E0) / E0)
    assert drift < 1e-12, drift


def test_both_end_ports_share_bond_admittance(net, tables):
    Y_port = tables.port_admittance(slab_field(tables, 0.9), "electric")
    for u in range(net.n_nodes):
        for p, v in enumerate(net.neighbors[u]):
            q = net.neighbors[v].index(u)
            assert Y_port[u, p] == Y_port[v, q]


# ---------------------------------------------------------------------------
# CS-7 reconcile vs the guarded in-tree reference + the SWAP demonstration
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("load", ["magnetic", "electric"])
@pytest.mark.parametrize("A", [0.5, 0.9])
def test_cs7_reconcile_against_udi(load, A):
    g = gate_cs7_reconcile(A, load)
    assert g["pass"], g


@pytest.mark.parametrize("built,declared", [("magnetic", "electric"), ("electric", "magnetic")])
def test_cs7_swap_fails_both_directions(built, declared):
    """CS-7-swap (VOID-linked module gate): the reconcile must FAIL when the
    built map and the declared label disagree — in BOTH directions."""
    from ave.core.universal_operators import universal_dynamic_impedance

    A = 0.9
    S = float(saturation_kernel(np.asarray(A)))
    Y_built = float(bond_admittance(np.asarray(A), built))
    Y_ref_declared = 1.0 / float(universal_dynamic_impedance(1.0, S, load=declared))
    assert abs(Y_built - Y_ref_declared) > 1e-3


# ---------------------------------------------------------------------------
# CT-1 implementation identity (NOT a transverse-vertex measurement; SS2.6)
# ---------------------------------------------------------------------------
def test_ct1_vertex_identity():
    g = gate_ct1_vertex()
    assert g["pass"], g
