"""Genesis v9 Phase-1 (deferred) — writhe-aware vector-TLM optical-activity gates.

Locks the OUTCOME-C finding (research/2026-06-23_chiral-vector-tlm-phase1_result.md):
  GATE-1 (chirality-sensitivity) PASS  -- operator SEES chirality (signed loop
                                          holonomy, exact diamond null);
  GATE-2 (convergence, bulk-propagated) FAIL -- the dynamical packet rate does NOT
                                          converge in L (the load-bearing finding);
  GATE-3 (validate-on-known) PASS      -- c/Z_0, losslessness, diamond null.

These are regression keepers: they assert the operator is writhe-AWARE (not the
FAIL-1 blind stencil) AND that the bulk g0 is genuinely non-converged (so the
result is not silently flipped to a chord later).
"""

import numpy as np

from ave.core import chiral_lattice as cl
from scripts.vol_4_engineering.chiral_vector_tlm_phase1 import (
    dynamical_energy_drift,
    dynamical_packet_rate,
    forward_winding_rate,
    gate1_chirality_sensitivity,
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
# GATE 2 — convergence: the bulk-propagated rate does NOT converge (outcome C)
# ---------------------------------------------------------------------------
def test_gate2_geometric_rate_is_the_screw_pitch_constant():
    # The geometric forward-winding rate is L-independent because it == the 4_1
    # screw pitch (a unit-cell constant), NOT a bulk transport coefficient.
    rates = [forward_winding_rate(cl.build_srs_net(L, "right"))[0] for L in (6, 8, 12)]
    assert np.std(rates) < 1e-3, "geometric rate is (trivially) L-independent"
    pitch = screw_pitch_rate()
    assert abs(abs(rates[0]) - pitch) / pitch < 0.01, (
        f"geometric rate {rates[0]} must coincide with screw pitch {pitch} (~0.2%)"
    )


def test_gate2_dynamical_bulk_rate_does_not_converge():
    # THE load-bearing finding: the genuinely-propagated rate swings wildly in L.
    dyn = np.array([dynamical_packet_rate(cl.build_srs_net(L, "right"))[0] for L in (6, 8, 10)])
    spread = np.std(dyn)
    scale = np.mean(np.abs(dyn))
    assert spread > 0.5 * scale, (
        f"bulk-propagated rate must be NON-convergent (outcome C); "
        f"spread={spread:.2f} scale={scale:.2f} dyn={dyn}"
    )


def test_gate2_enantiomorph_antisymmetry_is_trivial_not_convergence():
    # R+L == 0 is enforced by mirror symmetry and is NOT evidence of convergence.
    for L in (6, 8):
        rR = dynamical_packet_rate(cl.build_srs_net(L, "right"))[0]
        rL = dynamical_packet_rate(cl.build_srs_net(L, "left"))[0]
        assert abs(rR + rL) < 1e-6, "srs-L is the exact mirror of srs-R -> R+L=0"


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
