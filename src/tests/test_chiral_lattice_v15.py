"""Genesis v15 — latent nucleation smoke tests (vacuum native units)."""

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core.chiral_lattice_v13 import compton_pocket_mask
from ave.core.chiral_lattice_v15 import (
    latent_heat_inject_energy,
    run_p15_nucleation_cell,
    seed_saturated_node_pair,
    v15_gates,
    v15a_ablation_gates,
)
from ave.core.constants import ALPHA
from ave.core.genesis_lane_a_provenance import (
    E_NATIVE_SQRT_ALPHA,
    R_YIELD_KNEE_NATIVE,
    build_lane_a_provenance,
    cosmic_latent_native,
    field_energy_native,
    seed_amp_vsnap,
)


def test_cosmic_latent_negligible_vs_yield_native():
    c = cosmic_latent_native()
    assert c.ratio_to_yield < 1e-30
    assert abs(c.e_yield_kinetic_native - np.sqrt(ALPHA)) < 1e-12


def test_seed_amp_is_sqrt_alpha_vsnap():
    assert abs(seed_amp_vsnap() - E_NATIVE_SQRT_ALPHA) < 1e-12


def test_provenance_native_r_yield_targets():
    net = cl.build_srs_net(8, "right")
    pocket = compton_pocket_mask(net)
    prov = build_lane_a_provenance(net, pocket, smoke=True)
    assert prov.local.seed_r_yield == 1.0
    assert abs(prov.local.target_r_yield - R_YIELD_KNEE_NATIVE) < 1e-12
    assert prov.injection_path == "local_pair_ramp_native"


def test_latent_inject_raises_native_energy():
    V = np.ones((4, 3, 2)) * 0.1
    e0 = field_energy_native(V)
    mask = np.array([True, True, False, False])
    latent_heat_inject_energy(V, mask, delta_e_native=0.5)
    assert field_energy_native(V) > e0


def test_heal_cell_zero_seed():
    net = cl.build_srs_net(8, "right")
    pocket = compton_pocket_mask(net)
    prov = build_lane_a_provenance(net, pocket, smoke=True)
    r = run_p15_nucleation_cell(
        net, "heal", prov, latent_on=False, seed_mode="none", bulk_wall=False
    )
    assert r.A2_seed_peak < 1e-6
    assert r.r_yield_seed_peak < 1e-6


def test_v15_smoke_gates_complete():
    g = v15_gates(L=6, smoke=True)
    assert g["verdict"] in (
        "NUCLEATION-LANDED",
        "PARTIAL",
        "HEAL-CONFIRMED",
        "ENGINE-GAP",
    )
    assert "vacuum_native" in g["provenance"]["unit_system"]


def test_v15a_ablation_smoke_complete():
    g = v15a_ablation_gates(L=6, smoke=True)
    assert g["verdict"] in (
        "NUCLEATION-LANDED",
        "PARTIAL",
        "DISSIPATION-CONFIRMED",
        "HEAL-CONFIRMED",
        "ENGINE-GAP",
    )
    assert g["P15_H_heal_pass"]
    assert g["gain_r_yield"] >= 0.0
