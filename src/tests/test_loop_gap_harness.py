"""LOOP GAP unified harness smoke tests."""

from ave.core.loop_gap_harness import (
    RANK_NAMES,
    engine_config_for_rank,
    loop_gap_battery,
    run_loop_gap_probe,
)


def test_rank_profiles_cumulative():
    c1 = engine_config_for_rank(1)
    c4 = engine_config_for_rank(4)
    assert c1.use_trilinear_converter
    assert c1.use_impedance_boundary
    assert not c1.use_memristive_saturation
    assert c4.use_memristive_saturation


def test_loop_gap_probe_runs():
    r = run_loop_gap_probe(
        "smoke",
        N=10,
        rank_target=4,
        seed_mode="photon_lock",
        n_drive_mult=0.5,
        n_quiet_mult=1.5,
        fast=True,
    )
    assert r.rank_target == 4
    assert r.seed_mode == "photon_lock"
    assert r.n_drive >= 6
    assert r.v_inc_peak >= 0.0
    assert r.phi_growth < 1e6


def test_graded_a0_seed_runs():
    r = run_loop_gap_probe(
        "graded",
        N=10,
        seed_mode="graded_a0",
        n_drive_mult=0.5,
        n_quiet_mult=1.5,
        fast=True,
    )
    assert r.seed_mode == "graded_a0"


def test_loop_gap_battery_smoke():
    g = loop_gap_battery(N=10, smoke=True)
    assert g["harness"] == "loop_gap_harness"
    assert g["srs_genesis"] == "FROZEN_v17"
    assert g["verdict"] in (
        "REMANENCE-LANDED",
        "OPERATOR-SET-ONLY",
        "PARTIAL",
        "ENGINE-GAP",
    )
    assert len(g["rank_sweep"]) >= 1
    assert "heal" in g
    assert RANK_NAMES[4] == "remanence"
