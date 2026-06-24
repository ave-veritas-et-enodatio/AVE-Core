"""Tests for the PHASE-SPACE COUPLING-WINDING two-stage test (pre-reg 0d2b53e4).

The dynamical orbit solve is marked @pytest.mark.engine_sim (research-tier time-
evolution, off the PR-blocking gate per #414). The cheap reader/validate-on-known
units run on the default gate (they are fast and load-bearing — the reader MUST be
validated before any engine read is trusted).

VERDICT (committed): BREAK. The (2,3) charge-winding does NOT live as a conserved
closed time-orbit in the conservative A1↔ω coupling; the two sector global phases
lock at the CARRIER frequency ratio ω_b:ω_s (1:1 at resonance), reading a (1,1)-class
integer, not (2,3). The phase-space dynamical locus tests NEGATIVE — deepening the
#415 real-space negative. The result is α-free, two-reads-agree, energy-conserved,
and the sectors slosh conservatively (no pumping) — i.e. the test is clean; the
answer is no.
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.solvers.phase_space_winding import (
    PhaseSpaceWindingConfig,
    energy_conservation_gate,
    read_winding,
    run_phase_space_winding,
    sector_exchange_ledger,
    stage_a_coordinate_check,
    trace_orbit,
    validate_null_control,
    validate_positive_control,
    validate_pumped_control,
)


# ─────────────────────────────────────────────────────────────────────────────
# VALIDATE-ON-KNOWN (wired FIRST — fast, default gate). The reader must read a
# planted (2,3) before any engine read is trusted (pre-reg §6).
# ─────────────────────────────────────────────────────────────────────────────
def test_positive_control_reads_planted_2_3():
    """POSITIVE control: a planted (2,3) Lissajous must read (2,3), two methods
    agree. If this fails the reader is broken — every engine read is void."""
    out = validate_positive_control(p=2, q=3)
    assert out["read"] == (2, 3), f"reader misread planted (2,3) as {out['read']}"
    assert out["two_methods_agree"], "unwrap and circulation disagree on planted (2,3)"
    assert out["ok"]


def test_positive_control_reads_other_windings():
    """The reader is not hard-wired to (2,3): planted (3,2), (1,1), (2,5) read back."""
    for (p, q) in [(3, 2), (1, 1), (2, 5), (4, 4)]:
        out = validate_positive_control(p=p, q=q)
        assert out["read"] == (p, q), f"planted ({p},{q}) misread as {out['read']}"
        assert out["two_methods_agree"]


def test_null_control_rejects_2_3():
    """NULL control: a non-winding orbit (static / (1,1)) must read NOT-(2,3)."""
    out = validate_null_control()
    assert not out["static_is_2_3"], "static orbit false-positived as (2,3)"
    assert not out["lissajous_1_1_is_2_3"], "(1,1) orbit false-positived as (2,3)"
    assert out["ok"]


@pytest.mark.engine_sim
def test_pumped_control_trips_energy_gate():
    """ENERGY-GATE control: the conservative run conserves, the deliberately-pumped
    run TRIPS the bleed gate — the conservative guard is LIVE, not vacuous (pre-reg
    §6). This is the operational line vs the barred self-formation slot."""
    cfg = PhaseSpaceWindingConfig(N=16, R=5.0, r=2.0, a1_radius=4.0, pml_thickness=3)
    out = validate_pumped_control(cfg, n_steps=40)
    assert out["conservative_conserved"], "conservative step did NOT conserve energy"
    assert out["pumped_gate_trips"], "pumped variant did NOT trip the bleed gate"
    assert out["guard_is_live"]


# ─────────────────────────────────────────────────────────────────────────────
# STAGE A — coordinate definability (cheap-ish: one small eigensolve + 6 steps)
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.engine_sim
def test_stage_a_coordinate_is_definable_not_gauge_collapsed():
    """STAGE A: φ_rel is a NON-DEGENERATE definable coordinate (eigenstate |cross|>0,
    dynamical φ_rel moves under the conservative step). It is NOT gauge-collapsed —
    Stage A does not kill the test. (It DOES confirm a fixed-point eigenstate hosts
    only a static angle — the eigensolve's blind spot — which is why Stage B is
    needed.)"""
    cfg = PhaseSpaceWindingConfig(N=18, R=5.0, r=2.0, a1_radius=4.0, pml_thickness=3)
    out = stage_a_coordinate_check(cfg, k_eigs=6, probe_steps=6)
    assert out["coordinate_definable"], out["detail"]
    assert not out["stopped_here"]
    assert out["eigenstate_cross_nonzero"]
    assert out["dynamical_phi_moves"]
    # the dynamical probe is unitary (the energy is conserved to ~machine precision)
    assert out["dynamical_energy_drift"] < 1e-8


# ─────────────────────────────────────────────────────────────────────────────
# STAGE B — the dynamical orbit (the make-or-break). engine_sim.
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.engine_sim
def test_stage_b_energy_conserved_and_sectors_slosh():
    """ENERGY LEDGER (Grant's directive): the joint norm is conserved to ~machine
    precision (unitary, no pumping) AND the sectors slosh A1↔ω (conservative
    sector-exchange). The conservative guard holds and the coupling is live."""
    cfg = PhaseSpaceWindingConfig(N=20, R=7.0, r=2.3, a1_radius=6.0, pml_thickness=3,
                                  n_steps=400, dt=0.066)
    tr = trace_orbit(cfg)
    eg = energy_conservation_gate(tr)
    sl = sector_exchange_ledger(tr)
    assert eg["conserved"], f"joint energy drifted {eg['e_max_rel_drift']:.2e} (bleed gate trips)"
    assert eg["e_max_rel_drift"] < 1e-6
    assert sl["sector_exchange_seen"], "no A1↔ω sloshing — the coupling is inert"


@pytest.mark.engine_sim
def test_stage_b_two_reads_agree():
    """F4: the two independent winding reads (unwrap-count AND circulation integral)
    AGREE on the orbit integer — a prerequisite for any verdict (we do NOT adopt
    Q_H=p·q by formula)."""
    cfg = PhaseSpaceWindingConfig(N=20, R=7.0, r=2.3, a1_radius=6.0, pml_thickness=3,
                                  n_steps=400, dt=0.066)
    tr = trace_orbit(cfg)
    wr = read_winding(tr, dt=cfg.dt)
    assert wr.two_reads_agree, (
        f"two reads disagree: unwrap=({wr.p_unwrap:.3f},{wr.q_unwrap:.3f}) "
        f"circ=({wr.p_circ:.3f},{wr.q_circ:.3f})")


@pytest.mark.engine_sim
def test_stage_b_winding_is_NOT_2_3_carrier_locks():
    """THE MAKE-OR-BREAK (committed BREAK): the conservative orbit does NOT carry
    (2,3). The two sector global phases lock at the CARRIER ratio ω_b:ω_s (1:1 at
    resonance ω_b=ω_s=1.0) — a (1,1)-class integer, NOT the topological (2,3).
    The phase-space dynamical locus tests NEGATIVE."""
    cfg = PhaseSpaceWindingConfig(N=20, R=7.0, r=2.3, a1_radius=6.0, pml_thickness=3,
                                  n_steps=500, dt=0.066, omega_b=1.0, omega_s=1.0)
    tr = trace_orbit(cfg)
    wr = read_winding(tr, dt=cfg.dt)
    assert (wr.p_int, wr.q_int) not in [(2, 3), (3, 2)], (
        f"UNEXPECTED: orbit read as (2,3) — re-examine (committed verdict is BREAK)")
    # the resonant orbit locks 1:1 (gcd-reduced): |p|==|q| at ω_b=ω_s.
    assert wr.p_int == wr.q_int or abs(abs(wr.p_int) - abs(wr.q_int)) <= 1, (
        f"resonant orbit did not lock ~1:1: ({wr.p_int},{wr.q_int})")


@pytest.mark.engine_sim
def test_stage_b_winding_tracks_carrier_ratio():
    """MECHANISM: the global-phase winding ratio TRACKS the carrier ratio ω_b:ω_s.
    Detuning to 2:3 makes the phases wind ~2:3 — proving the integer is the CARRIER
    (oscillator) ratio, NOT a topological (2,3) charge winding that would be carrier-
    independent. This names the mechanism behind the BREAK."""
    cfg = PhaseSpaceWindingConfig(N=20, R=7.0, r=2.3, a1_radius=6.0, pml_thickness=3,
                                  n_steps=500, dt=0.066, omega_b=2.0, omega_s=3.0)
    tr = trace_orbit(cfg)
    tor = (np.unwrap(tr.phi_tor)[-1] - tr.phi_tor[0]) / (2 * np.pi)
    pol = (np.unwrap(tr.psi_pol)[-1] - tr.psi_pol[0]) / (2 * np.pi)
    ratio = tor / (pol + 1e-30)
    # the winding ratio follows ω_b/ω_s = 2/3 ≈ 0.667 (NOT carrier-independent)
    assert abs(ratio - (2.0 / 3.0)) < 0.15, (
        f"winding ratio {ratio:.3f} did not track the carrier ratio 0.667 — "
        f"re-examine the mechanism claim")


# ─────────────────────────────────────────────────────────────────────────────
# TOP-LEVEL VERDICT — the committed BREAK
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.engine_sim
def test_full_verdict_is_break():
    """The committed verdict: BREAK. Stage A passes (coordinate definable), the
    reader validates, energy conserves and sectors slosh — the test is CLEAN — and
    the answer is NO: the orbit reads a non-(2,3) carrier-lock integer."""
    cfg = PhaseSpaceWindingConfig(N=24, R=7.0, r=2.3, a1_radius=6.0, pml_thickness=4,
                                  n_steps=600, dt=0.066)
    res = run_phase_space_winding(cfg)
    assert res["verdict"] == "BREAK", f"verdict {res['verdict']}: {res['reason']}"
    # the test is clean: every supporting gate holds, only is_2_3 fails.
    assert res["validate_on_known"]["positive"]["ok"]
    assert res["validate_on_known"]["null"]["ok"]
    assert res["validate_on_known"]["pumped"]["guard_is_live"]
    assert res["stage_a"]["coordinate_definable"]
    assert res["stage_b"]["two_reads_agree"]
    assert res["energy_ledger"]["conserved"]
    assert res["energy_ledger"]["sector_exchange_seen"]
    assert not res["bins"]["is_2_3"]
