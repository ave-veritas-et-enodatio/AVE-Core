"""Genesis v18 — operator-native CoupledK4Cosserat smoke tests."""

from ave.core.genesis_v18_coupled import (
    make_v18_engine,
    pair_seed_cosserat,
    run_p18_operator_cell,
    snapshot_op14,
)


def test_v18_engine_observables_finite():
    sim = make_v18_engine(10)
    pair_seed_cosserat(sim, amp=0.3)
    sim.freeze_converter_wall()
    obs = snapshot_op14(sim)
    assert obs["H"] > 0.0
    assert obs["max_A_sq"] >= 0.0


def test_p18_full_stack_runs():
    r = run_p18_operator_cell(
        "smoke",
        N=10,
        n_drive_mult=0.5,
        n_quiet_mult=1.5,
        impedance_on=True,
        converter_on=True,
        memristive_on=True,
        fast=True,
    )
    assert r.impedance_on
    assert r.converter_on
    assert r.v_inc_peak >= 0.0
    assert r.n_drive >= 6
