"""Genesis v9 Phase-1 (deferred) — writhe-aware vector-TLM optical-activity gates.

Locks the RE-ADJUDICATED finding (research/2026-06-23_chiral-vector-tlm-phase1_result.md,
§0): OUTCOME A (CHANNEL OPEN), not the retracted outcome C.
  GATE-1 (chirality-sensitivity) PASS  -- operator SEES chirality (signed loop
                                          holonomy, exact diamond null);
  GATE-2 (convergence, bulk forward-channel) PASS -- the bulk forward-channel
                                          rotation rate CONVERGES to the 4_1 screw
                                          pitch, L-independent to machine precision,
                                          exact enantiomorph sign-flip, dynamically
                                          confirmed by the dispersion-free cascade;
  GATE-3 (validate-on-known) PASS      -- c/Z_0, losslessness, diamond null.

These are regression keepers: they assert the operator is writhe-AWARE (not the
FAIL-1 blind stencil), that the bulk g0 IS converged + signed (so the corrected
outcome is not silently flipped BACK to outcome C), and that the legacy packet
probe's transient-skip kills the spurious swing.
"""

import numpy as np

from ave.core import chiral_lattice as cl
from scripts.vol_4_engineering.chiral_vector_tlm_phase1 import (
    driven_cascade_rate,
    dynamical_energy_drift,
    dynamical_packet_rate,
    dynamical_packet_rate_steady,
    forward_winding_rate,
    gate1_chirality_sensitivity,
    gate2_convergence,
    gate3_validate_on_known,
    loop_holonomy,
    net_loop_holonomy,
    screw_pitch_rate,
)


# ---------------------------------------------------------------------------
# GATE 1 — chirality-sensitivity (the FAIL-1 guard)
# ---------------------------------------------------------------------------
def test_gate1_operator_sees_chirality_signed_and_equal():
    hR, _, _ = net_loop_holonomy(cl.build_srs_net(6, "right"))
    hL, _, _ = net_loop_holonomy(cl.build_srs_net(6, "left"))
    assert abs(hR) > 1e-3, f"srs-R holonomy must be nonzero, got {hR}"
    assert hR * hL < 0, "enantiomorphs must sign-flip"
    assert abs(hR + hL) < 1e-9, f"sign-flip must be magnitude-exact, |R+L|={abs(hR+hL):.2e}"


def test_gate1_diamond_null_emerges_exactly():
    hD, sD, _ = net_loop_holonomy(cl.build_diamond_net(6))
    assert abs(hD) < 1e-12, f"achiral diamond loop holonomy must be exactly 0, got {hD}"
    assert sD < 1e-12, "diamond per-ring spread must be 0 (no chirality anywhere)"


def test_gate1_not_writhe_blind_distinct_from_fail1():
    # The FAIL-1 artifact: spec_R == spec_L (writhe-blind). Here R != L by O(0.5 rad).
    hR, _, _ = net_loop_holonomy(cl.build_srs_net(6, "right"))
    hL, _, _ = net_loop_holonomy(cl.build_srs_net(6, "left"))
    assert abs(hR - hL) > 0.1, "operator must NOT be writhe-blind (FAIL-1 had spec_R~spec_L)"


def test_gate1_aggregate_pass():
    assert gate1_chirality_sensitivity().passed


# ---------------------------------------------------------------------------
# GATE 2 — convergence: the bulk forward-channel rate CONVERGES (outcome A)
# ---------------------------------------------------------------------------
def test_gate2_bulk_forward_channel_rate_converges_to_screw_pitch():
    # RE-ADJUDICATED: the bulk forward-channel rotation rate is L-independent to
    # machine precision AND equals the 4_1 screw pitch -- a converged bulk rate.
    rates = [forward_winding_rate(cl.build_srs_net(L, "right"))[0] for L in (6, 8, 10, 12)]
    assert np.std(rates) < 1e-3, (
        f"bulk forward-channel rate must CONVERGE in L (outcome A); std={np.std(rates):.2e}"
    )
    pitch = screw_pitch_rate()
    assert abs(abs(rates[0]) - pitch) / pitch < 0.01, (
        f"converged bulk rate {rates[0]} must coincide with screw pitch {pitch} (~0.2%)"
    )


def test_gate2_bulk_rate_enantiomorph_sign_flip_is_exact():
    # The converged bulk rate sign-flips exactly between enantiomorphs (signed g0).
    for L in (6, 8, 10):
        rR = forward_winding_rate(cl.build_srs_net(L, "right"))[0]
        rL = forward_winding_rate(cl.build_srs_net(L, "left"))[0]
        assert rR * rL < 0, "enantiomorphs must sign-flip"
        assert abs(rR + rL) < 1e-9, f"sign-flip must be magnitude-exact, |R+L|={abs(rR+rL):.2e}"


def test_gate2_dispersion_free_cascade_confirms_screw_pitch():
    # The deciding tool: a GENUINELY PROPAGATING wave (driven steady-state cascade)
    # inherits the screw-chain rotation -> refutes "the screw pitch never propagates."
    pitch = screw_pitch_rate()
    rR, _, r2R = driven_cascade_rate(cl.build_srs_net(8, "right"))
    rL, _, _ = driven_cascade_rate(cl.build_srs_net(8, "left"))
    assert r2R > 0.95, f"steady cascade must be cleanly linear, R^2={r2R:.3f}"
    assert abs(abs(rR) - pitch) / pitch < 0.05, (
        f"propagating-wave cascade rate {rR} must match screw pitch {pitch} (<5%)"
    )
    assert rR * rL < 0 and abs(rR + rL) < 1e-6, "cascade rate must sign-flip exactly"


def test_gate2_transient_skip_kills_the_outcome_c_swing():
    # The retracted outcome C was a launch-transient fit-window artifact: the legacy
    # probe swung +9.2/-26.9/+3.4/+2.8; skipping the transient collapses it to O(1)
    # with an exact enantiomorph sign-flip -- so the "non-convergence" was spurious.
    steady = [dynamical_packet_rate_steady(cl.build_srs_net(L, "right"))[0] for L in (6, 8, 10, 12)]
    assert all(abs(s) < 3.0 for s in steady), (
        f"transient-skipped steady rates must be O(1), not the +/-27 artifact; got {steady}"
    )
    for L in (6, 8):
        sR = dynamical_packet_rate_steady(cl.build_srs_net(L, "right"))[0]
        sL = dynamical_packet_rate_steady(cl.build_srs_net(L, "left"))[0]
        assert abs(sR + sL) < 1e-6, "transient-skipped steady rate must sign-flip exactly"


def test_gate2_legacy_packet_probe_is_a_known_artifact():
    # Guard: the legacy probe is retained for reproduction only. It fits the launch
    # transient (end=max(...,4)); its rates are NOT the bulk g0. This test documents
    # that the legacy probe is unstable (swings), so it is never used to adjudicate.
    legacy = np.array([dynamical_packet_rate(cl.build_srs_net(L, "right"))[0] for L in (6, 8, 10)])
    assert np.std(legacy) > 1.0, (
        f"legacy probe is expected to be artifact-unstable (kept for reproduction "
        f"only); if it has stabilized, re-audit the probe. got {legacy}"
    )


def test_gate2_aggregate_pass():
    assert gate2_convergence().passed


# ---------------------------------------------------------------------------
# GATE 3 — validate-on-known
# ---------------------------------------------------------------------------
def test_gate3_lossless_axiom3():
    drift = dynamical_energy_drift(cl.build_srs_net(4, "right"), nsteps=40)
    assert drift < 1e-10, f"writhe-aware vector-TLM must be lossless, drift={drift:.2e}"


def test_gate3_validate_on_known_pass():
    assert gate3_validate_on_known().passed


# ---------------------------------------------------------------------------
# Connection sanity — the bend (not local bond direction) carries the holonomy
# ---------------------------------------------------------------------------
def test_loop_holonomy_single_ring_matches_aggregate():
    net = cl.build_srs_net(6, "right")
    s = int(np.where(net.interior_mask)[0][0])
    ring = cl.shortest_ring(net, s)
    h = loop_holonomy(net, ring)
    assert abs(h - (-0.256776)) < 1e-3, f"single-ring holonomy {h} must match -0.2568"
