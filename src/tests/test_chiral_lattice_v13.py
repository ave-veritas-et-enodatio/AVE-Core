"""Genesis v13 — bulk-wall eigen-cavity smoke tests."""

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core.chiral_lattice_v13 import (
    apply_bulk_wall_z_local,
    compton_pocket_mask,
    energy_fraction_in_pocket,
    run_p13_cavity_cell,
    v13_gates,
)


def test_compton_pocket_mask_nonempty():
    net = cl.build_srs_net(8, "right")
    mask = compton_pocket_mask(net)
    assert mask.sum() > 0
    assert np.all(mask <= net.interior_mask)


def test_bulk_wall_raises_exterior_z():
    z = np.array([1.0, 2.0, 3.0, 4.0])
    mask = np.array([True, True, False, False])
    z2 = apply_bulk_wall_z_local(z, mask, z_wall=10.0)
    assert z2[0] == 1.0
    assert z2[2] >= 10.0
    assert z2[3] >= 10.0


def test_wall_on_improves_confinement_smoke():
    net = cl.build_srs_net(8, "right")
    on = run_p13_cavity_cell(net, "on", bulk_wall=True, n_steps=40, tau_steps=8)
    off = run_p13_cavity_cell(net, "off", bulk_wall=False, n_steps=40, tau_steps=8)
    assert on.E_frac_interior >= off.E_frac_interior - 0.05


def test_v13_smoke_gates_complete():
    g = v13_gates(L=6, smoke=True)
    assert g["verdict"] in ("LOCALIZATION-LANDED", "PARTIAL", "ENGINE-GAP")
    assert "P13_wall_on" in g
    assert "P13_wall_off_ablation" in g
    assert g["P13_ablation_fails"] is True
