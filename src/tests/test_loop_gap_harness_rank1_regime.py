"""D-lite OP-2 instrument + smoke baseline (rank-1 FROZEN charter)."""

import pytest
import numpy as np

from ave.core.bulk_rarefaction_sector import gamma_bulk_smith_min, interior_mask
from ave.core.loop_gap_harness import (
    OP2_VINC_FLOOR,
    loop_gap_dlite_battery,
    run_loop_gap_probe,
)
from ave.core.loop_gap_seeds import A_YIELD


def test_gamma_bulk_smith_cold_lattice_negative():
    N = 8
    rho = np.zeros((N, N, N))
    m = interior_mask(N, pml=0)
    gamma_min = gamma_bulk_smith_min(rho, m, c0=1.0, c2_floor=1e-3, eps_den=1e-6)
    # Z = c0, Z_ref = sqrt(2) c0 ⇒ Γ < 0 at cold lattice
    assert gamma_min < -0.05


def test_dlite_probe_fields():
    r = run_loop_gap_probe(
        "dlite_fields",
        N=10,
        rank_target=1,
        seed_mode="photon_lock",
        bulk_density_on=True,
        front_target=A_YIELD,
        n_drive_mult=0.5,
        n_quiet_mult=1.5,
        fast=True,
    )
    assert r.target_a_front == A_YIELD
    assert r.achieved_a_front_seed == pytest.approx(A_YIELD, rel=0.05)
    assert "gamma_bulk_min" in r.channel_tags["bulk"]
    assert r.regime_valid
    assert r.op2_bin in {
        "OP-2-LANDED",
        "OP-2-PARTIAL",
        "ENGINE-GAP",
        "ENGINE-GAP_POST_RUPTURE",
    }


def test_dlite_battery_smoke():
    out = loop_gap_dlite_battery(N=10)
    assert out["harness_phase"] == "D-lite"
    assert out["target_a_front"] == A_YIELD
    primary = next(a for a in out["arms"] if a["label"] == "B1_photon_yield")
    assert primary["achieved_a_front_seed"] == pytest.approx(A_YIELD, rel=0.05)
    assert primary["bulk_density_on"] is True
    assert "gamma_bulk_min_drive" in primary
    assert out["ablations"]["bulk_OFF"]["bulk_density_on"] is False
    # Thesis expectation: V_inc nucleation gap on transverse-only engine
    assert primary["v_inc_peak"] < OP2_VINC_FLOOR
