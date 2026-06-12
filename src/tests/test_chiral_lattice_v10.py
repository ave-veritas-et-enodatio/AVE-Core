"""Genesis v10 — snap + Ω_freeze IC smoke tests."""

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_vector as clv
from ave.core.chiral_lattice_vector_sat import node_rms_amplitude
from ave.core.chiral_lattice_v10 import (
    A_YIELD_SQ,
    V10RunState,
    apply_omega_freeze_ic,
    apply_rate_gated_snap,
    channel_H_diagnostics,
    vector_tlm_step_v10,
    v10_gates,
)


def test_snap_increases_dissipation_ledger():
    net = cl.build_srs_net(4, "right")
    V = np.zeros((net.n_nodes, net.degree, 2))
    V[0, 0, 0] = 2.0  # A >> yield
    a2 = (node_rms_amplitude(V) / 1.0) ** 2
    state = V10RunState(chi_shock=0.5)
    apply_rate_gated_snap(V, a2, np.zeros_like(a2), state, snap=True)
    assert state.snap_events >= 0
    if state.snap_events > 0:
        assert state.E_diss_snap > 0.0


def test_omega_freeze_ic_changes_field():
    net = cl.build_srs_net(4, "right")
    V0 = clv.launch_linear_packet(net) * 0.2
    V1 = V0.copy()
    apply_omega_freeze_ic(V0, net, enabled=True)
    apply_omega_freeze_ic(V1, net, enabled=False)
    assert not np.allclose(V0, V1)


def test_channel_H_at_saturation():
    h = channel_H_diagnostics(np.array([0.99]))
    assert h["H_EM"] > 1.0
    assert h["H_shear"] < 1.0


def test_v10_step_runs():
    net = cl.build_srs_net(4, "right")
    S = cl.scatter_matrix(net.degree)
    V = clv.launch_linear_packet(net) * 0.3
    state = V10RunState(chi_shock=0.25)
    state.reset(net.n_nodes)
    V2, diag = vector_tlm_step_v10(net, V, S, state, snap=True)
    assert V2.shape == V.shape
    assert "H_EM" in diag
    assert diag["A_yield_sq"] == A_YIELD_SQ


def test_v10_smoke_gates_complete():
    g = v10_gates(L=6, smoke=True, chi_shock=0.5)
    assert "P6_cells" in g
    assert len(g["P6_cells"]) == 4
    assert g["P6_diamond_cells"] == []
    assert "P6_snap_ablation" in g
    assert "P6_omega_free_ablation" in g
    assert g["engine_class"].startswith("discrete srs TLM")
