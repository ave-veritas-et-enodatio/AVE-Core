"""Tests for the TETHERED-PIVOT RE-RUN (x34b) — pre-reg 2026-07-10.

x34b freezes the CONTROL-SUBTRACTED EXCESS detector as THE primary rule A PRIORI (the #612
adversarial-review consequence 2), discloses the excess axis's saturation-zone blindness UP
FRONT, and scopes the banked verdict to the NON-SATURATED window so it does not rest on the
detector blind zone.

The pure-logic units (saturation onset, non-saturated-zone restriction, planted-violation
criteria, grid refinement) run on the DEFAULT gate. The live engine reads (detuning sweep,
dead-actuator sim) are @pytest.mark.engine_sim (research tier, off the PR-blocking gate per
#414). The FULL-resolution 29-pt run_x34b() is the RESEARCH ARTIFACT emitted by the driver
__main__ (research/2026-07-10_tethered-pivot-rerun_result.json), mirroring the #612 pattern;
the engine_sim tests here validate the same mechanics on a reduced config at low cost.
"""

from __future__ import annotations

from dataclasses import replace

import numpy as np
import pytest

from ave.solvers.tethered_pivot_winding import TetheredPivotConfig, detuning_sweep
from ave.solvers.tethered_pivot_x34b import (
    FRESH_SWEEP_OS,
    MEASURED_FRESH_RHO_FREE,
    REPRO_MARKS,
    _energy_gate_catches_pump,
    banked_pipeline_lock_proof,
    fresh_config,
    planted_violation_proofs,
    restricted_verdict,
    saturation_onset,
)


# ─────────────────────────────────────────────────────────────────────────────
# FRESH GRID (prereg §3) — a refinement of the #612 15-pt step-0.05 grid.
# ─────────────────────────────────────────────────────────────────────────────
def test_fresh_grid_is_refinement_of_612():
    """The fresh 29-pt step-0.025 grid CONTAINS the #612 15-pt step-0.05 grid as a subset
    (per-point reproduction checkable; the verdict is shown stable under refinement, not
    tuned to the exact #612 grid)."""
    fresh = set(FRESH_SWEEP_OS)
    grid_612 = TetheredPivotConfig().sweep_os
    assert len(FRESH_SWEEP_OS) == 29
    assert abs(FRESH_SWEEP_OS[0] - 0.70) < 1e-9
    assert abs(FRESH_SWEEP_OS[-1] - 1.40) < 1e-9
    missing = [g for g in grid_612 if not any(abs(g - f) < 1e-9 for f in fresh)]
    assert not missing, f"#612 points not in fresh grid: {missing}"
    assert fresh_config().sweep_os == FRESH_SWEEP_OS


# ─────────────────────────────────────────────────────────────────────────────
# SATURATION-ONSET RULE (prereg §2c) — frozen a priori, data-driven.
# ─────────────────────────────────────────────────────────────────────────────
def test_saturation_onset_finds_terminal_flat_plateau():
    """A free control that TRACKS (steep) then SATURATES flat has i_sat at the onset of
    the terminal flat plateau; the non-saturated window is the low-ω_s tracking portion."""
    os = np.array(FRESH_SWEEP_OS)
    rf = np.where(os < 1.0, 1.0 / os, 1.0)   # tracks then hard-saturates at 1.0
    i_sat = saturation_onset(rf)
    assert 0 < i_sat < len(rf) - 1, i_sat          # a real interior onset
    # every interval from i_sat onward is flat (< flat_tol); the onset is the FIRST such
    df = np.abs(np.diff(rf))
    assert np.all(df[i_sat:] < 0.03)
    assert df[i_sat - 1] >= 0.03                    # the interval before is NOT flat


def test_saturation_onset_no_terminal_flat_returns_full():
    """A free control whose every interval stays ABOVE the flat tolerance (never saturates)
    → no terminal flat run exists → i_sat = n_intervals ⇒ the full sweep is the
    non-saturated window (conservative — no blind zone carved out)."""
    os = np.array(FRESH_SWEEP_OS)
    rf_nonflat = np.cumsum(np.full(len(os), 0.05))  # |Δ|=0.05 > 0.03 everywhere
    assert saturation_onset(rf_nonflat) == len(rf_nonflat) - 1


# ─────────────────────────────────────────────────────────────────────────────
# NON-SATURATED-ZONE RESTRICTION (prereg §2c) — the banked verdict.
# ─────────────────────────────────────────────────────────────────────────────
def test_restricted_verdict_scopes_to_nonsat_window_and_reports_companions():
    """restricted_verdict banks the FROZEN excess axis on the non-saturated window and
    reports the full-sweep excess verdict + the complementary absolute disclosure read."""
    os = np.array(FRESH_SWEEP_OS)
    rf = np.where(os < 1.0, 1.0 / os, 1.0)
    ra = rf.copy()                                  # anchored == free ⇒ pure TRACK
    r = restricted_verdict(os, ra, rf)
    assert r["saturated"] is True
    assert r["nonsat_n_points"] >= 3
    assert r["banked_verdict"] in ("LOCK", "TRACK", "PARTIAL", "INCONCLUSIVE")
    # anchored identical to free ⇒ no excess plateaus ⇒ TRACK on both windows
    assert r["banked_verdict"] == "TRACK", r
    assert r["banked_excess_staircase"] < 0.2
    assert r["full_sweep_excess_verdict"] == "TRACK"
    # companions present
    for key in ("full_sweep_absolute_verdict", "full_sweep_absolute_staircase",
                "full_sweep_free_staircase", "onset_omega_s"):
        assert key in r


def test_plant_in_saturation_absolute_sees_excess_blind():
    """A genuine rational lock planted ENTIRELY in the free-control saturation zone is SEEN
    by the complementary ABSOLUTE axis (LOCK) but is INVISIBLE to the FROZEN excess axis
    (NOT LOCK — the plateau coincides with the flat free control and is subtracted out).
    This is the a-priori-disclosed asymmetry that motivates the non-saturated-zone bank."""
    os = np.array(FRESH_SWEEP_OS)
    rf = np.where(os < 1.0, 1.0 / os, 1.0)                       # saturating free control
    ra = np.where(os < 1.0, 1.0 / os,                            # tracks in the tracking zone
                  np.where(os < 1.2, 0.90, 0.60))                # LOCK planted in sat zone
    r = restricted_verdict(os, ra, rf)
    assert r["full_sweep_absolute_verdict"] == "LOCK"           # absolute SEES the lock
    assert r["full_sweep_excess_verdict"] != "LOCK"             # excess is BLIND to it
    # and the non-saturated window (where anchored==free) correctly reads TRACK
    assert r["banked_verdict"] == "TRACK", r


# ─────────────────────────────────────────────────────────────────────────────
# PLANTED-VIOLATION PROOFS (prereg §8) — pure-criteria portions on the default gate.
# ─────────────────────────────────────────────────────────────────────────────
def test_energy_planted_pump_caught_by_shipped_gate():
    """R3 (#626 review): the planted energy-pump proof exercises the SHIPPED `energy_ledger`
    gate (not an inline copy of its criterion). A monotone-growing clamp-ON energy trace,
    routed through the real energy_ledger via a patched solver trace, is flagged
    on_non_pumping == False, while the conserving clamp-OFF leg reads off_conserved == True."""
    eng = _energy_gate_catches_pump(TetheredPivotConfig(N=16, pml_thickness=3, a1_radius=4.5))
    assert eng["on_non_pumping"] is False           # the shipped gate CATCHES the pump
    assert eng["on_max_rel_energy_gain"] > 1e-9
    assert eng["off_conserved"] is True


def test_banked_pipeline_fires_lock_on_real_free_control():
    """R2 (#626 review): plant a GENUINE staircase lock as the anchored curve on the REAL
    fresh-sweep free control (with its 12/23 in-window staircase-blind intervals) and push it
    through the ACTUAL restricted_verdict pipeline (saturation_onset → window slice →
    lock_detector). The frozen excess axis MUST still bin LOCK — closing the fireability gap
    that the §2a plant (idealized never-flat free control) left open. Proves the observed
    TRACK is a real negative, not a blind miss in the banked window."""
    assert len(MEASURED_FRESH_RHO_FREE) == len(FRESH_SWEEP_OS) == 29
    proof = banked_pipeline_lock_proof()
    assert proof["fires_lock"] is True
    assert proof["banked_verdict"] == "LOCK"
    assert proof["banked_excess_staircase"] >= 0.4    # clears the LOCK bar despite blindness
    assert proof["banked_excess_jumps"] >= 1          # the jumps channel fires in-window
    assert proof["nonsat_n_points"] == 24


def test_detector_and_saturation_disclosure_pure():
    """The detector-separation + saturation-disclosure proofs are PURE (synthetic arrays,
    no engine step): a planted staircase reads LOCK, a planted line reads TRACK, and a
    planted lock in the free-control saturation zone is SEEN by the absolute axis but NOT by
    the frozen excess axis (lock_suppressed_by_excess). Asserted via validate_lock_detector
    directly (default gate) — the engine-touching dead-actuator proof is tested engine_sim."""
    from ave.solvers.tethered_pivot_winding import validate_lock_detector
    vlk = validate_lock_detector()
    assert vlk["planted_locked_verdict"] == "LOCK"
    assert vlk["planted_tracking_verdict"] == "TRACK"
    assert vlk["ok"] is True
    sz = vlk["saturation_zone"]
    assert sz["frozen_verdict"] == "LOCK"           # absolute SEES the sat-zone lock
    assert sz["amended_verdict"] != "LOCK"          # frozen excess axis is BLIND to it
    assert sz["lock_suppressed_by_excess"] is True


# ─────────────────────────────────────────────────────────────────────────────
# LIVE ENGINE READS (engine_sim) — reduced config, low cost.
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.engine_sim
def test_planted_violation_proofs_all_catch_live():
    """All frozen gates CATCH a planted violation end-to-end, including the live dead-actuator
    (branch='off' vs itself ⇒ actuator_live False), the SHIPPED energy_ledger pump proof (R3),
    and the banked-pipeline LOCK-fireability proof on the real free control (R2)."""
    proofs = planted_violation_proofs(TetheredPivotConfig(N=16, pml_thickness=3, a1_radius=4.5))
    assert proofs["dead_actuator"]["catches_violation"] is True
    assert proofs["dead_actuator"]["off_actuator_live"] is False
    assert proofs["energy_non_pumping"]["shipped_gate"] == "energy_ledger"
    assert proofs["energy_non_pumping"]["on_non_pumping_flag"] is False
    assert proofs["banked_pipeline_lock_fires"]["fires_lock"] is True
    assert proofs["banked_pipeline_lock_fires"]["banked_verdict"] == "LOCK"
    assert proofs["all_gates_catch_violations"] is True


@pytest.mark.engine_sim
def test_restricted_verdict_on_small_live_sweep():
    """A live (reduced N, few-point, short) detuning sweep flows through restricted_verdict
    and yields a well-formed banked verdict on the frozen excess axis — the mechanics run
    end-to-end on the real evolver (the full-resolution run is the driver artifact)."""
    cfg = replace(TetheredPivotConfig(), N=16, pml_thickness=3, a1_radius=4.5,
                  n_steps=150, sweep_os=(0.80, 0.90, 1.00, 1.10, 1.20, 1.30))
    sweep = detuning_sweep(cfg, branch="capacitive")
    os = np.array(sweep["os"], float)
    ra = np.array(sweep["rho_anchored"], float)
    rf = np.array(sweep["rho_free"], float)
    r = restricted_verdict(os, ra, rf)
    assert r["banked_verdict"] in ("LOCK", "TRACK", "PARTIAL", "INCONCLUSIVE")
    assert r["full_sweep_excess_verdict"] in ("LOCK", "TRACK", "PARTIAL", "INCONCLUSIVE")
    assert r["full_sweep_absolute_verdict"] in ("LOCK", "TRACK", "PARTIAL", "INCONCLUSIVE")
    assert set(REPRO_MARKS) >= {"excess_staircase", "track_R2"}   # marks are defined
