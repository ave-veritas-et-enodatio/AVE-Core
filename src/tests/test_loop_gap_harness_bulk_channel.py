"""Phase 2b — bulk rarefaction sector on LOOP GAP harness (GAP-A port)."""

import numpy as np

from ave.core.bulk_rarefaction_sector import BulkRarefactionSector, c_bulk2_clipped
from ave.core.loop_gap_harness import run_loop_gap_probe
from ave.topological.vacuum_engine import VacuumEngine3D


def test_bulk_sector_rk2_evolve():
    sec = BulkRarefactionSector(12, dx=1.0, pml=2)
    sec.apply_probe_ic(amp=0.12)
    rho0 = sec.rho_bar.copy()
    for _ in range(8):
        sec.step(0.04)
    assert np.max(np.abs(sec.rho_bar - rho0)) > 0.0
    snap = sec.snapshot()
    assert snap["rho_bar_min"] < -1e-4


def test_vacuum_engine_bulk_off_no_sector():
    eng = VacuumEngine3D.from_args(N=10, pml=2, bulk_density_on=False)
    assert eng.bulk is None
    for _ in range(5):
        eng.step()
    snap = eng.bulk_snapshot()
    assert snap["rho_bar_min"] == 0.0
    assert snap["bulk_steps"] == 0.0


def test_vacuum_engine_bulk_on_steps():
    eng = VacuumEngine3D.from_args(N=10, pml=2, bulk_density_on=True)
    assert eng.bulk is not None
    eng.apply_bulk_probe_ic(amp=0.1)
    for _ in range(10):
        eng.step()
    snap = eng.bulk_snapshot()
    assert eng.bulk.step_count == 10
    assert snap["rho_bar_min"] < 0.0


def test_f0_harness_bulk_off_matches_legacy_metrics():
    """KEEP-BOTH: bulk_density_on=False leaves EM/shear path unchanged."""
    r = run_loop_gap_probe(
        "f0_bulk_off",
        N=10,
        rank_target=1,
        seed_mode="pair",
        bulk_density_on=False,
        n_drive_mult=0.5,
        n_quiet_mult=1.0,
        fast=True,
    )
    assert not r.bulk_density_on
    assert r.rho_bar_min_end == 0.0
    assert r.c_bulk2_min_end == 0.0
    assert r.v_inc_peak >= 0.0


def test_f1_bulk_on_differs_from_off():
    off = run_loop_gap_probe(
        "f1_off",
        N=10,
        rank_target=1,
        seed_mode="pair",
        bulk_density_on=False,
        n_drive_mult=0.5,
        n_quiet_mult=1.0,
        fast=True,
    )
    on = run_loop_gap_probe(
        "f1_on",
        N=10,
        rank_target=1,
        seed_mode="pair",
        bulk_density_on=True,
        n_drive_mult=0.5,
        n_quiet_mult=1.0,
        fast=True,
    )
    assert on.rho_bar_min_end < off.rho_bar_min_end
    assert on.channel_primary in ("bulk+EM+shear", "EM+shear", "proxy+EM+shear")


def test_c_bulk2_eos_at_probe():
    rho = np.array([-0.08])
    c2 = c_bulk2_clipped(rho, c0=1.0, c2_floor=1e-3, eps_den=1e-6)
    assert float(c2[0]) < 1.0


def test_bulk_circulation_ic_rarefies():
    sec = BulkRarefactionSector(14, dx=1.0, pml=2)
    sec.energize_rotation_column(m_edge=0.8, r_core=2.0, axis=2)
    assert float(np.max(np.abs(sec.u_adv))) > 0.0
    assert float(np.max(sec.rho_bar)) == 0.0
    rho0 = sec.rho_bar.copy()
    for _ in range(12):
        sec.step(0.05)
    assert np.min(sec.rho_bar) < float(np.min(rho0))


def test_f2_channel_tags_on_bulk_probe():
    r = run_loop_gap_probe(
        "f2_tags",
        N=10,
        rank_target=1,
        seed_mode="pair",
        bulk_density_on=True,
        bulk_seed="probe",
        n_drive_mult=0.5,
        n_quiet_mult=1.0,
        fast=True,
    )
    assert "EM" in r.channel_tags
    assert "bulk" in r.channel_tags
    assert "proxy" in r.channel_tags
    assert r.rank1b_pass
