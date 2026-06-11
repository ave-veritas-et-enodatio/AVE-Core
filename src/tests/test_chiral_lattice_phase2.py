"""Genesis v9 Phase-2 — Op14/Op3 vector-TLM + P5/P6 gate machinery."""

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_vector as clv
from ave.core.chiral_lattice_vector_sat import (
    chirality_charge_proxy,
    connect_op3,
    phase2_gates,
    plant_23_ansatz,
    run_p5_hosting,
    vector_tlm_step_sat,
    z_local_from_V,
)


def test_op3_connect_preserves_energy_one_step():
    net = cl.build_srs_net(6, "right")
    S = cl.scatter_matrix(net.degree)
    V = plant_23_ansatz(net) * 0.3
    for op3 in (False, True):
        Vt = V.copy()
        E0 = clv.vector_energy(Vt)
        Vt, _ = vector_tlm_step_sat(net, Vt, S, op14=True, op3=op3, chiral_rotation=False)
        drift = abs(clv.vector_energy(Vt) - E0) / E0
        assert drift < 1e-10, f"op3={op3} one-step drift={drift:.2e}"


def test_op14_raises_z_local_under_large_amplitude():
    V_lo = np.zeros((4, 3, 2))
    V_lo[0, 0, 0] = 0.1
    V_hi = V_lo.copy()
    V_hi[0, 0, 0] = 0.85
    assert z_local_from_V(V_hi)[0] > z_local_from_V(V_lo)[0]


def test_op3_mixing_differs_from_permutation():
    net = cl.build_srs_net(4, "right")
    V_ref = np.random.randn(net.n_nodes, net.degree, 2) * 0.2
    z = z_local_from_V(V_ref)
    z[:] = np.linspace(1.0, 2.5, net.n_nodes)
    plain = connect_op3(net, V_ref, z, op3=False)
    mixed = connect_op3(net, V_ref, z, op3=True)
    assert not np.allclose(plain, mixed)


def test_p5_hosting_runs():
    net = cl.build_srs_net(6, "right")
    r = run_p5_hosting(net, n_steps=100)
    assert r.n_steps == 100
    assert np.isfinite(r.energy_ratio_end)


def test_phase2_smoke_gates_complete():
    g = phase2_gates(L=6, smoke=True)
    assert "P5" in g and "P6_cells" in g
    assert g["engine_class"] == "discrete srs TLM + Op14/Op3"
    assert len(g["P6_cells"]) == 4


def test_plant_23_has_chirality_charge():
    net = cl.build_srs_net(6, "right")
    V = plant_23_ansatz(net)
    assert abs(chirality_charge_proxy(V)) > 1e-6
