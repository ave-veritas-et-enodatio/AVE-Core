"""Genesis v11 — memristive lag + P11 quiescence smoke tests."""

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_vector as clv
from ave.core.chiral_lattice_v11 import (
    MemState,
    backward_euler_s,
    s_eq_from_amplitude,
    vector_tlm_step_v11,
    v11_gates,
)
from ave.core.chiral_lattice_v10 import V10RunState


def test_backward_euler_relaxes_toward_eq():
    s_lag = np.array([1.0, 0.9])
    s_eq = np.array([0.5, 0.5])
    s_new = backward_euler_s(s_lag, s_eq, tau_steps=10.0, memristive=True)
    assert np.all(s_new < s_lag)
    assert np.all(s_new > s_eq - 1e-9)


def test_memristive_instant_limit_matches_eq():
    s_lag = np.array([1.0])
    s_eq = np.array([0.4])
    s_new = backward_euler_s(s_lag, s_eq, tau_steps=10.0, memristive=False)
    assert np.allclose(s_new, s_eq)


def test_v11_step_updates_s_lag():
    net = cl.build_srs_net(4, "right")
    S = cl.scatter_matrix(net.degree)
    V = clv.launch_linear_packet(net) * 0.4
    v10 = V10RunState(chi_shock=0.25)
    v10.reset(net.n_nodes)
    mem = MemState()
    mem.reset(V)
    s0 = mem.S_lag.copy()
    V2, diag = vector_tlm_step_v11(
        net, V, S, v10, mem, memristive=True, tau_steps=5.0, snap=False
    )
    assert V2.shape == V.shape
    assert diag["memristive"] is True
    assert not np.allclose(mem.S_lag, s0) or np.max(s_eq_from_amplitude(np.sqrt(diag["max_A2"]))) < 1.0


def test_v11_smoke_gates_complete():
    g = v11_gates(L=6, smoke=True, chi_shock=0.5)
    assert "P6_cells" in g
    assert len(g["P6_cells"]) == 4
    assert "P11_memristive_ablation" in g
    assert "v10_replay" in g
    assert g["verdict"] in ("LANDED", "PARTIAL", "LOOP GAP OPEN")
    assert g["engine_class"].startswith("discrete srs TLM")
