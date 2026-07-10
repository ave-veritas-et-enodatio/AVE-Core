"""Tests for the TETHERED-PIVOT mode-locking test (pre-reg 2026-07-09).

The dynamical orbit solves are @pytest.mark.engine_sim (research-tier time-evolution,
off the PR-blocking gate per #414). The cheap lock-detector / validate-on-known units
run on the default gate (they are fast and load-bearing — the detector MUST separate a
planted staircase from a planted line before any engine read is trusted).

VERDICT (two-axis, KEEP-BOTH per adversarial-review restatement 2026-07-09):
PARTIAL (frozen prereg-§6 detector) / TRACK (post-hoc control-subtracted axis). On the
frozen config the anchored sweep gives staircase_fraction 0.4286 (== free 0.4286),
jump_count 1, track_R2 0.9799 — which fails BOTH the frozen LOCK bar (≥0.5) and TRACK
bar (<0.2), so the PREREGISTERED detector returns PARTIAL. Only the post-hoc
control-subtracted axis (excess_staircase 0.0714) reads TRACK. Signatures 2 (no excess
hysteresis) and 3 (no cap↔mag flip) fire NULL cleanly; the clamp is a live,
dissipative-not-pumping actuator (dead-actuator + energy gates pass).
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.solvers.phase_space_winding import PhaseSpaceWindingConfig, build_seeded_sim
from ave.solvers.tethered_pivot_winding import (
    TetheredPivotConfig,
    anchor_mask,
    dead_actuator_gate,
    energy_ledger,
    lock_detector,
    run_tethered_pivot,
    validate_lock_detector,
)


# ─────────────────────────────────────────────────────────────────────────────
# VALIDATE-ON-KNOWN (fast, default gate) — the lock-detector must separate a
# planted staircase (LOCK) from a planted linear rotation number (TRACK).
# ─────────────────────────────────────────────────────────────────────────────
def test_lock_detector_separates_staircase_from_line():
    """The detector reads a planted STAIRCASE as LOCK and a planted LINEAR as TRACK.
    If it can't, every engine read is void (pre-reg §7)."""
    out = validate_lock_detector()
    assert out["planted_locked_verdict"] == "LOCK", out
    assert out["planted_tracking_verdict"] == "TRACK", out
    assert out["ok"]


def test_excess_axis_is_lock_suppressing_in_saturation_zone():
    """NEUTRALITY-SCOPE gate (KEEP-BOTH, adversarial-review restatement): a GENUINE lock
    planted in the free-control SATURATION zone reads LOCK on the FROZEN prereg-§6
    absolute axis but PARTIAL (NOT LOCK) on the POST-HOC control-subtracted excess axis
    (excess→0 — the plateaus coincide with the flat free control). This certifies the
    excess axis is LOCK-SUPPRESSING there, i.e. biased toward the TRACK/negative read;
    the amended-axis neutrality claim is scoped to the tracking zone only."""
    sz = validate_lock_detector()["saturation_zone"]
    assert sz["frozen_verdict"] == "LOCK", sz          # frozen absolute SEES the lock
    assert sz["amended_verdict"] != "LOCK", sz         # excess axis does NOT
    assert sz["excess_staircase"] == 0.0, sz           # plateaus subtracted out
    assert sz["lock_suppressed_by_excess"] is True, sz


def test_lock_detector_control_subtracts_shared_flatness():
    """The detector is CONTROL-SUBTRACTED: a plateau the FREE control ALSO has is NOT
    an anchor effect. A staircase-vs-line reads LOCK (excess plateaus); an
    anchored-curve identical to its free control reads TRACK even if BOTH are flat
    (the shared saturation is baseline-subtracted). Guards the exact blind spot that
    made the control-blind detector mis-bin PARTIAL."""
    os = np.linspace(0.7, 1.4, 15)
    staircase = np.where(os < 1.0, 1.5, 0.5)          # one big jump at os=1.0
    line = 1.0 / os
    d_stair = lock_detector(os, staircase, line)      # anchored=staircase vs free=line
    assert d_stair["excess_jumps"] >= 1
    assert d_stair["excess_staircase"] >= 0.4
    assert d_stair["amended_verdict"] == "LOCK"        # excess (amended) axis
    assert d_stair["verdict"] == "LOCK"                # alias of the amended axis
    # a FLAT anchored curve whose FREE control is EQUALLY flat ⇒ the AMENDED axis reads
    # TRACK (excess≈0), even though the ABSOLUTE staircase_fraction is high enough that
    # the FROZEN axis reads LOCK — the exact axis-divergence the KEEP-BOTH restatement
    # exposes (the shared-flatness / saturation case).
    flat_shared = np.where(os < 1.0, 1.2, 1.0)
    d_flat = lock_detector(os, flat_shared, flat_shared.copy())
    assert d_flat["staircase_fraction"] >= 0.4          # absolute flatness IS high
    assert d_flat["frozen_verdict"] == "LOCK"           # frozen absolute axis bins LOCK
    assert d_flat["excess_staircase"] < 0.2             # but none of it is anchor-induced
    assert d_flat["amended_verdict"] == "TRACK"         # amended axis subtracts it out
    assert d_flat["verdict"] == "TRACK"                 # alias of the amended axis


def test_anchor_mask_has_field_support():
    """The equatorial node-plane M must sit on the winding host (non-empty, with real
    field support) — else the clamp is a dead actuator on an empty set (pre-reg §7)."""
    ps = PhaseSpaceWindingConfig(N=20, R=7.0, r=2.3, a1_radius=5.5, pml_thickness=3)
    sim = build_seeded_sim(ps)
    m = anchor_mask(sim, z_anchor=1.0)
    assert m.sum() > 20, f"anchor mask too small: {int(m.sum())} cells"
    assert float(np.abs(sim.b_w[m]).mean()) > 0.1, "anchor mask has no field support"


# ─────────────────────────────────────────────────────────────────────────────
# GATES — dead-actuator + energy (engine_sim: they step the solver).
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.engine_sim
def test_dead_actuator_clamp_collapses_pinned_quadrature():
    """DEAD-ACTUATOR gate: the pinned quadrature's variance over M COLLAPSES vs
    unclamped (var_ratio<0.05) for BOTH branches — the clamp demonstrably constrains
    (it is not a dead actuator, pre-reg §7)."""
    cfg = TetheredPivotConfig(N=16, pml_thickness=3, a1_radius=4.5)
    cap = dead_actuator_gate(cfg, branch="capacitive", n_steps=50)
    mag = dead_actuator_gate(cfg, branch="magnetic", n_steps=50)
    assert cap["actuator_live"], cap
    assert mag["actuator_live"], mag
    # the OTHER quadrature must NOT be pinned (the clamp is one-quadrature, not a sink)
    assert cap["var_clamped"] < 1e-12
    assert mag["var_clamped"] < 1e-12


@pytest.mark.engine_sim
def test_energy_ledger_off_conserves_on_non_pumping():
    """ENERGY gate: clamp OFF conserves the joint norm to #417 standard (<1e-6); clamp
    ON is monotone NON-PUMPING (the projection only removes norm) — so a lock could
    never be a pumped artifact (pre-reg §7)."""
    cfg = TetheredPivotConfig(N=16, pml_thickness=3, a1_radius=4.5)
    eng = energy_ledger(cfg, branch="capacitive", n_steps=80)
    assert eng["off_conserved"], eng
    assert eng["off_max_rel_drift"] < 1e-6
    assert eng["on_non_pumping"], eng
    assert eng["on_max_rel_energy_gain"] <= 1e-9
    assert eng["on_removed_norm_frac"] >= 0.0   # dissipative (never negative = never pumps)


# ─────────────────────────────────────────────────────────────────────────────
# THE VERDICT — two-axis (KEEP-BOTH): frozen PARTIAL / amended TRACK (engine_sim).
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.engine_sim
def test_full_verdict_two_axis_frozen_partial_amended_track():
    """The committed verdict is TWO-AXIS (adversarial-review restatement): the FROZEN
    prereg-§6 detector returns PARTIAL (Signature-1 staircase_fraction 0.4286 fails both
    the LOCK bar ≥0.5 and the TRACK bar <0.2), and only the POST-HOC control-subtracted
    axis returns TRACK (excess_staircase 0.0714). Every supporting gate holds
    (lock-detector validated, dead-actuator live both branches, energy
    conserved/non-pumping); Signatures 2 (no excess hysteresis) and 3 (no cap↔mag flip)
    fire NULL cleanly."""
    res = run_tethered_pivot(TetheredPivotConfig())
    # two-axis top-level verdicts
    assert res["frozen_verdict"] == "PARTIAL", f"{res['frozen_verdict']}: {res['reason']}"
    assert res["amended_verdict"] == "TRACK", f"{res['amended_verdict']}: {res['reason']}"
    assert "PARTIAL (frozen prereg-6 detector)" in res["verdict"], res["verdict"]
    assert "TRACK (post-hoc control-subtracted axis)" in res["verdict"], res["verdict"]
    assert res["validate_on_known"]["ok"]
    # the disclosed saturation-zone LOCK-suppression of the amended axis
    assert res["validate_on_known"]["saturation_zone"]["lock_suppressed_by_excess"] is True
    assert res["dead_actuator"]["capacitive"]["actuator_live"]
    assert res["dead_actuator"]["magnetic"]["actuator_live"]
    assert res["energy_ledger"]["on_non_pumping"]
    # signature 1: FROZEN absolute axis PARTIAL; AMENDED excess axis TRACK
    det = res["signature_1_mode_locking"]["detector"]
    assert det["frozen_verdict"] == "PARTIAL"
    assert det["amended_verdict"] == "TRACK"
    assert det["staircase_fraction"] >= 0.2      # fails frozen TRACK bar (<0.2)
    assert det["staircase_fraction"] < 0.5       # fails frozen LOCK bar (>=0.5)
    assert det["track_R2"] >= 0.9
    assert det["excess_staircase"] < 0.2
    # signature 2: no EXCESS hysteresis over the free control; signature 3: no flip
    assert not res["signature_2_hysteresis"]["hysteresis_seen"]
    assert not res["signature_3_termination_flip"]["flip_seen"]
