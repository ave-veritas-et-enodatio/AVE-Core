"""EM keying ROUND 2 — the WORKED-CELL keying derivation — gating tests.

FROZEN prereg: research/2026-07-05_em-keying-round2-worked-cell_prereg_FROZEN.md
(freeze commit e4312c43). Locks the load-bearing round-2 claims:

  STEP 0: the briefed NET-FLUX candidate is DEGENERATE (Poynting: <net flux>=-<dU/dt>=0
          for every steady state -> blinds the pump too -> killed by derivation).
  STEP 1: the LC energy ledger forces the FREQUENCY-INDEPENDENT AC-variance measure W_var
          (the reactive-energy swing amplitude is freq-independent), NOT the rate W_beat.
          CRUX: the mean deficit tracks the MEAN-SQUARE (DC-included) -> the E-side worked
          keying is SELECTED (DC-exclusion needs a missing epsilon-side Lenz-dual), the
          B-side is CANON-DERIVED (Lenz). The corpus tension is FLAGGED.
  physical-H falsifier: STATIC-IN-TIME atom -> W=0 -> shift=0 -> the round-1 killer
          dissolves with NO net-vs-local machinery. Null-liveness: a time-varying drive
          gives shift != 0.
  seven constraints: pump (both sub-bins, both norm arms), PVLAS/BMV, DeLLight, boost
          (lattice-frame-anchored), the NEW slow-drive open scale.
"""
import sys
from pathlib import Path

import numpy as np
import pytest

from ave.core.constants import E_YIELD, OMEGA_C, XI_TOPO, C_0

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "verify"))
import em_keying_round2_constraints as K  # noqa: E402
import em_keying_round2_derivation as D  # noqa: E402

E_C = E_YIELD


# ===================================================== STEP 0: net-flux candidate is degenerate
def test_step0_netflux_candidate_is_degenerate():
    """The briefed NET-FLUX candidate is DEGENERATE: <net flux>_cycle = -<dU/dt>_cycle = 0
    for a steady wave -> it blinds the STEADY PUMP as well as the atom -> kills Table I."""
    s0 = D.step0_netflux_degenerate_symbolic()
    assert s0["avg_dudt_over_cycle"] == 0
    assert s0["avg_netflux_over_cycle"] == 0  # zero for pump too -> DEGENERATE, killed at STEP 0


# ===================================================== STEP 1: the LC ledger forces W_var
def test_step1_worked_measures_vanish_for_held_nonzero_for_wave():
    """Both worked measures (W_var, W_beat) are ZERO for a held field, nonzero for a wave."""
    a = D.step1_lc_energy_ledger_symbolic()
    assert a["var_held"] == 0
    assert a["grad2_held"] == 0
    # wave: Var(E) = E0^2/2 (nonzero)
    import sympy as sp
    E0 = sp.symbols("E0", positive=True)
    assert sp.simplify(a["var_wave"] - E0**2 / 2) == 0


def test_step1_ledger_forces_W_var_freq_independent():
    """The reactive-energy swing amplitude is FREQUENCY-INDEPENDENT across sub-resonant drives
    -> the operating-point excursion the kernel keys on is the freq-independent AC-variance W_var,
    DERIVED from the LC energy ledger (NOT selected against Table I)."""
    d = D.demonstrate_swing_frequency_independence()
    swings = d["reactive_swing_amps"]
    w_vars = d["W_var_values"]
    w_beats = d["W_beat_values"]
    # swing amplitude identical across frequencies (freq-independent):
    for s in swings[1:]:
        assert s == pytest.approx(swings[0], rel=1e-9)
    # W_var identical (~0.5) across frequencies:
    for wv in w_vars:
        assert wv == pytest.approx(0.5, rel=1e-6)
    # W_beat scales as (w/wC)^2 -> collapses at low frequency (opposite behavior):
    assert w_beats[0] < w_beats[1] < w_beats[2]


def test_step1_verdict_is_worked_var():
    v = D.step1_which_measure_the_ledger_forces()
    assert v["forced_measure"] == "W_var"
    assert v["sub_bin"] == "[WORKED-VAR]"


def test_reconcile_gate_pathA_pathB_can_fire():
    """ReconcileGate: PATH A (symbolic W_var=1/2) reconciles with PATH B (numpy time-domain),
    with the can-fire self-test PROVEN on the real comparator+halt path (not a checklist)."""
    res = D.reconcile_pathA_pathB_W_var()
    assert res.reconciled is True
    assert res.can_fire_proven is True  # the halt plumbing was live-fire proven
    assert res.max_rel_discrepancy < 1e-4  # PATH A and PATH B agree within the derived tolerance


# ===================================================== STEP 1 CRUX: variance vs mean-square split
def test_step1_crux_mean_deficit_is_meansquare_DC_included():
    """THE CRUX (flag-don't-fix): the mean kernel deficit tracks the MEAN-SQUARE (DC-INCLUDED),
    NOT the variance. A held DC field gives a NONZERO deficit -> the DC IS included = the round-1
    key. So the E-side worked keying (DC-blind variance) is SELECTED, not derived: the ledger forces
    AC-engagement but not DC-EXCLUSION, which needs a missing epsilon-side Lenz-dual and contradicts
    corpus R2 (node-up:118 'a DC bias is a real operating point'). The B-side IS canon-derived (Lenz)."""
    x = D.step1_variance_vs_meansquare_the_crux()
    assert x["deficit_held_DC"] > 0.0  # DC IS included (mean-square) -> the round-1 key, NOT variance
    # the AC mean deficit tracks mean-square/2, not the (equal-here) variance:
    assert x["deficit_mean_AC"] == pytest.approx(x["meansquare_AC"] / 2.0, rel=5e-2)
    assert "worked-DERIVED" in x["B_side_verdict"]      # B-side: Lenz canon
    assert "worked-SELECTED" in x["E_side_verdict"]     # E-side: SELECTED, not derived
    assert "CONTRADICTS" in x["corpus_tension"]         # the tension is flagged


# ===================================================== the physical-H falsifier (fast slice)
def test_physical_atomic_H_is_static_in_time_worked_zero():
    """The physical muonic atom fields (Coulomb E, proton-dipole H) are STATIC IN TIME -> the
    WORKED content W = Var_t(E) = 0 everywhere -> BLIND. The round-1 killer (LOCAL pointwise E x H
    nonzero for the static H) DISSOLVES because the WORKED functional keys on the TIME variance, not
    the pointwise product -- NO net-vs-local machinery needed."""
    a = K.p3.A_MU
    for f in (0.1, 0.5, 1.0, 2.0):
        E_series = np.full(64, float(K.E_coulomb(f * a)))  # static in time
        W = K.worked_content_W(E_series, dt=1.0, mode="var")
        assert W == 0.0  # exactly zero (np.var of a constant array); BLIND for the right reason


def test_worked_functional_gates_the_consumed_observable():
    """GATE THE CONSUMED OBSERVABLE (pre-test Trigger 9): the mechanism consumes the TIME-VARIANCE
    of E at the cell; the control measures THAT variable. A static-in-time field -> W=0; a
    time-varying field -> W>0. The gate is on Var_t(E) (what the mechanism consumes), NOT a proxy."""
    static = np.full(128, 5.0e15)
    assert K.worked_content_W(static, dt=1.0, mode="var") == 0.0  # consumed variable = 0 for held
    t = np.linspace(0.0, 2 * np.pi, 128, endpoint=False)
    varying = 5.0e15 * np.cos(t)
    assert K.worked_content_W(varying, dt=t[1] - t[0], mode="var") > 0.0  # nonzero for worked


# ===================================================== constraint 2: the pump, both sub-bins
def test_constraint_pump_worked_var_unchanged_beat_collapses():
    """WORKED-VAR: Table I unchanged (freq-independent, NORM-YIELD tautological match).
    WORKED-BEAT: Table I collapses by (w_pump/wC)^2 ~ 9.2e-12. Opposite fates -> the VAR-vs-BEAT
    fork is real; STEP 1 forces VAR by the freq-independence of the reactive swing amplitude."""
    c2 = K.constraint_2_pump()
    assert c2["A2_letter"] == pytest.approx(5.9e-7, rel=2e-2)
    # WORKED-VAR/NORM-YIELD reproduces the Letter (Table I unchanged, tautological):
    assert c2["dn_bir_WORKED_VAR_yield"] == pytest.approx(c2["dn_bir_letter"], rel=1e-9)
    assert c2["Pflip_rescale_VAR_yield"] == pytest.approx(1.0, rel=1e-9)
    # WORKED-BEAT collapses by (w/wC)^2:
    assert c2["beat_suppression_factor"] == pytest.approx(3.033e-6**2, rel=1e-2)
    assert abs(c2["dn_bir_WORKED_BEAT_yield"]) < abs(c2["dn_bir_letter"]) * 1e-10  # ~10^11 below


def test_constraint_pump_norm_fork_open():
    """The norm fork is OPEN: NORM-YIELD gives 1 (tautological), NORM-CLOCK gives 1/(4pi). Neither
    substrate-forced (the round-1 tautology lesson: NORM-YIELD is DEFINED to match)."""
    c2 = K.constraint_2_pump()
    ratio = c2["dn_bir_WORKED_VAR_clock"] / c2["dn_bir_WORKED_VAR_yield"]
    assert ratio == pytest.approx(1.0 / (4.0 * np.pi), rel=1e-9)


# ===================================================== constraints 3/4/5/6/7
def test_constraint_pvlas_bmv_computed_zero():
    """S_B (Route C dual): computed A_I from physical dB/dt -> negligible -> dn_mu ~ 0. The B-side
    is worked-consistent (mu-inductor keyed on dB/dt via Lenz; static B not worked)."""
    c = K.constraint_3_4_magnetic()
    assert c["pvlas_A_I"] < 1e-20
    assert c["bmv_A_I"] < 1e-20
    assert c["pvlas_dn_mu"] == pytest.approx(0.0, abs=1e-40)


def test_constraint_dellight_worked_var_tautological():
    c = K.constraint_5_dellight()
    assert c["dn_iso_WORKED_VAR"] == pytest.approx(c["dn_iso_letter"], rel=1e-9)


def test_constraint_boost_blind_lattice_frame_anchored():
    """A boosted UNIFORM static field is CONSTANT at a lattice cell -> Var_t(E)=0 -> W=0 -> BLIND,
    lattice-frame-anchored FOR FREE (no aliasing story). This is the frame's role stated plainly,
    NOT a covariance claim; the round-1 CRITICAL-2 aliasing refutation is MOOT."""
    c = K.constraint_6_boost()
    assert c["W_boosted"] == 0.0  # constant at a lattice cell -> not worked
    assert "lattice-frame-anchored" in c["verdict"]


def test_constraint_slow_drive_is_open_scale():
    """The NEW slow-drive/quasi-static boundary: the sub-optical time-varying-E middle band has NO
    facility bound -> a DECLARED OPEN SCALE (not a free parameter). W_var is freq-independent for
    any w<<wC; the untested RF/THz worked-E band is the open scale."""
    c = K.constraint_7_slow_drive()
    assert c["verdict"] == "OPEN SCALE"
    assert len(c["unconstrained_middle_band_w_over_wC"]) >= 3
    # the middle band sits between the DC anchors and the optical pump:
    for w in c["unconstrained_middle_band_w_over_wC"].values():
        assert 0.0 < w < 1.0  # sub-resonant, time-varying


# ===================================================== homonym / sector guards
def test_no_mechanical_qpoint_numbers_in_worked_coefficient():
    """Sector guard: the EM worked coefficient (1, 1/(4pi)) must NOT be a mechanical Q-point number
    (2/7=0.2857, 9.7734, sqrt(8)=2.828)."""
    for forbidden in [2.0 / 7.0, 9.7734, np.sqrt(8.0)]:
        assert not np.isclose(K.C_W_YIELD, forbidden, rtol=1e-3)
        assert not np.isclose(K.C_W_CLOCK, forbidden, rtol=1e-3)


def test_i_max_route_c_dual_scale():
    """S_B dual: I_max = xi_topo * c = 124.384 A (Route C threshold, consumed by import)."""
    assert XI_TOPO * C_0 == pytest.approx(124.384, rel=1e-4)


# ===================================================== STANDING FALSIFIER (engine_sim)
@pytest.mark.engine_sim
def test_muonic_physical_H_worked_PASSES_by_derivation():
    """STANDING FALSIFIER — the round-2 successor to test_muonic_physical_H_CONSTRAINT_KILLED.

    The WORKED functional evaluated on the PHYSICAL atomic H(r) (proton dipole) + Coulomb E(r) --
    BOTH STATIC IN TIME -- gives worked content W = Var_t(E) = 0 IDENTICALLY -> S_E = 1 -> the level
    shift is 0 EXACTLY, under the 2.3 ueV CREMA window. This PASSES BY DERIVATION: the round-1 killer
    (the physical H makes the LOCAL pointwise E x H nonzero) DISSOLVES because the WORKED functional
    keys on the TIME variance of the field, not the pointwise product -- the atom is blind because its
    fields are static in TIME, with NO net-vs-local machinery.

    NULL-VERDICT LIVENESS (trigger 10): the IDENTICAL pipeline fed a TIME-VARYING drive returns a
    NONZERO shift -> the zero is physics (static-in-time -> not worked), not a bookkeeping zero for
    any field. This is the standing round-2 falsifier consuming MY worked functional."""
    c1 = K.constraint_1_muonic()
    # all physical-atom worked contents are exactly zero (static in time):
    assert all(v == 0.0 for v in c1["W_physical_at"].values())
    # the level shift is exactly zero -> PASSES the CREMA window BY DERIVATION:
    assert c1["passes"]
    assert c1["worst_abs_shift_ueV"] == 0.0
    assert c1["worst_abs_shift_ueV"] < c1["window_ueV"]
    # null-verdict liveness: a TIME-VARYING drive through the SAME pipeline gives a NONZERO shift:
    assert abs(c1["liveness_worked_shift_ueV"]) > 0.0
