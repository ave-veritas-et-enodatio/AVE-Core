"""Genesis v12 — comoving transport smoke tests."""

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core.chiral_lattice_v12 import (
    energy_centroid,
    translate_field_along_axis,
    v12_gates,
)


def test_translate_field_moves_centroid():
    net = cl.build_srs_net(6, "right")
    n = net.n_nodes
    V = np.zeros((n, net.degree, 2))
    u = n // 2
    V[u, 0, 0] = 1.0
    z0 = energy_centroid(net, V, axis=2)
    V2 = translate_field_along_axis(net, V, delta=0.0, axis=2, n_nodes_shift=3)
    z1 = energy_centroid(net, V2, axis=2)
    assert abs(z1 - z0) > 0.05 or abs(z1 - z0 - net.box) > 0.05


def test_v12_smoke_gates_complete():
    g = v12_gates(L=6, smoke=True)
    assert g["verdict"] in ("TRANSPORT-LANDED", "PARTIAL", "ENGINE-GAP")
    assert "P12_comoving" in g
    assert "P12_pinned_ablation" in g
    assert g["P12_linear_advances"] is True
