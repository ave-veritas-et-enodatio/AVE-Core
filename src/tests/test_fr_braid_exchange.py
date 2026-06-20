"""Tests for the FR two-loop BRAID spin-statistics gate.

Carrier-sector FIRST PHYSICS GATE (charter §3(b), §5; prereg
`research/2026-06-20_fr-braid-spin-statistics_prereg.md`).

These tests are the validate-on-known ladder (prereg §5) + the six anti-tautology
guards (prereg §4) as assertions. A guard violation is a HALT, not a silent pass.

The headline finding (run-it-and-see, Rule 10): the exchange σ holonomy = −I from
A4-only, reflection-free PARTNER-encirclement transport — the SAME 2T element as
the single-particle 2π −I (FR homotopy). chord-vs-peer: PEER-ahead (generic-FR),
NOT an AVE-distinct chord, because the non-A4 control ALSO reaches −I.
"""

import numpy as np

from ave.core.chiral_lattice import build_diamond_net
from ave.topological.fr_braid_exchange import (
    all_link_perms_even,
    braid_sigma_path,
    probe_fr_braid_exchange,
    seed_two_carriers,
    symmetric_path,
    winding_around,
)
from ave.topological.k4_lattice_holonomy import holonomy_of_path

ATOL = 1e-9


# ─────────────────────────────────────────────────────────────────────────────
# Validate-on-known ladder (prereg §5).
# ─────────────────────────────────────────────────────────────────────────────
def test_two_carriers_are_separated():
    """Two DISTINCT defect lines at well-separated sites (label-free precondition)."""
    net = build_diamond_net(L=10)
    seed = seed_two_carriers(net)
    # carriers must be genuinely separated (not the same defect re-used).
    assert seed["separation"] > 2.0
    c1 = seed["carrier1"]["centroid"]
    c2 = seed["carrier2"]["centroid"]
    assert not np.allclose(c1, c2, atol=1.0)


def test_contractible_two_particle_path_is_plus_I():
    """Validate-on-known: contractible (no encirclement) → +I."""
    net = build_diamond_net(L=10)
    seed = seed_two_carriers(net)
    sym = symmetric_path(net, seed)
    h = holonomy_of_path(net, sym, defect=seed["carrier2"]["defect"])
    assert h["holonomy_sign"] > 0.0
    assert h["net_winding"] == 0


def test_braid_sigma_is_minus_I():
    """Validate-on-known + THE TEST: the braid σ exchange holonomy = −I."""
    net = build_diamond_net(L=10)
    seed = seed_two_carriers(net)
    sigma = braid_sigma_path(seed, n_traverse=3)  # C3³ partner-encircle = 2π
    h = holonomy_of_path(net, sigma, defect=seed["carrier2"]["defect"])
    assert h["holonomy_sign"] < 0.0
    assert h["so3_is_identity"]  # a genuine 2π SO(3) loop
    assert np.isclose(h["q"][0], -1.0, atol=ATOL)


def test_single_partner_encircle_is_120deg_not_minus_I():
    """Ladder transparency: a SINGLE C3 partner-encirclement is 120°, NOT −I.

    A C3 disclination is a 1/3-rotation source; the FR 2π (→ −I) is the 3-fold
    encirclement. This makes the C3³ → 2π construction transparent (not a fudge).
    """
    net = build_diamond_net(L=10)
    seed = seed_two_carriers(net)
    h1 = holonomy_of_path(net, braid_sigma_path(seed, 1), defect=seed["carrier2"]["defect"])
    assert h1["holonomy_sign"] > 0.0  # +cos(60°) = +0.5, not −1
    assert not h1["so3_is_identity"]  # 120°, not a closed 2π loop
    assert np.isclose(h1["q"][0], 0.5, atol=ATOL)


def test_braid_sigma_squared_is_plus_I():
    """Validate-on-known: σ² (double exchange / 4π return) → +I."""
    net = build_diamond_net(L=10)
    seed = seed_two_carriers(net)
    sigma2 = braid_sigma_path(seed, n_traverse=6)  # 6× = 4π-equivalent
    h = holonomy_of_path(net, sigma2, defect=seed["carrier2"]["defect"])
    assert h["holonomy_sign"] > 0.0
    assert h["so3_is_identity"]


def test_fr_homotopy_exchange_equals_single_particle_2pi():
    """FR consistency: the σ −I is the SAME 2T element as the single-particle 2π −I.

    This IS the Finkelstein–Rubinstein theorem's content — exchange ≅ 2π rotation
    of one soliton — made explicit on the lattice.
    """
    from ave.topological.k4_lattice_holonomy import probe_lattice_doublecover

    net = build_diamond_net(L=10)
    seed = seed_two_carriers(net)
    sigma = braid_sigma_path(seed, n_traverse=3)
    h = holonomy_of_path(net, sigma, defect=seed["carrier2"]["defect"])
    single = probe_lattice_doublecover(L=10)
    assert np.isclose(h["q"][0], single["encircle3_q"][0], atol=ATOL)


# ─────────────────────────────────────────────────────────────────────────────
# Anti-tautology guards (prereg §4) — the six, each as an assertion.
# ─────────────────────────────────────────────────────────────────────────────
def test_guard1_winding_around_the_other_not_self_C3cubed():
    """GUARD 1: the −1 comes from encircling the PARTNER, not a self-C3³.

    partner_winding (around carrier-2) ≠ 0; self_winding (around carrier-1, the
    transported defect) = 0. The sign is the partner-encirclement holonomy, never
    a single-particle self-encirclement relabeled "exchange."
    """
    net = build_diamond_net(L=10)
    seed = seed_two_carriers(net)
    sigma = braid_sigma_path(seed, n_traverse=3)
    partner = winding_around(net, sigma, seed["carrier2"]["defect"])
    self_w = winding_around(net, sigma, seed["carrier1"]["defect"])
    assert partner != 0  # winds around the partner
    assert self_w == 0  # does NOT self-encircle the transported carrier


def test_guard3_braid_is_reflection_free():
    """GUARD 3: every braid link_perm is an even (A4) perm — zero T_d\\T reflection."""
    net = build_diamond_net(L=10)
    seed = seed_two_carriers(net)
    h = holonomy_of_path(net, braid_sigma_path(seed, 3), defect=seed["carrier2"]["defect"])
    assert all_link_perms_even(h)


def test_guard4_no_analytic_qbody():
    """GUARD 4: no baked SU(2) half-angle rotor (AST self-report of the operator)."""
    from ave.topological.k4_lattice_holonomy import uses_analytic_qbody

    assert uses_analytic_qbody() is False
    # and the FR module itself does not import the cosserat analytic rotor.
    import ave.topological.fr_braid_exchange as mod

    src = open(mod.__file__).read()
    assert "cosserat_field_3d" not in src
    assert "q_body" not in src  # the analytic rotor variable name


def test_guard5_positive_control_is_plus_I():
    """GUARD 5: the symmetric / non-braiding control gives +I (metric not blind)."""
    net = build_diamond_net(L=10)
    seed = seed_two_carriers(net)
    h = holonomy_of_path(net, symmetric_path(net, seed), defect=seed["carrier2"]["defect"])
    assert h["holonomy_sign"] > 0.0
    assert h["net_winding"] == 0


def test_guard6_runs_on_achiral_diamond():
    """GUARD 6: the gate runs on the achiral diamond (Grant-ruled, chirality-indep)."""
    r = probe_fr_braid_exchange(L=10)
    assert r["guards"]["g6_achiral_diamond"] is True


# ─────────────────────────────────────────────────────────────────────────────
# Top-level verdict + chord-vs-peer (prereg §2).
# ─────────────────────────────────────────────────────────────────────────────
def test_verdict_is_pass_with_all_guards():
    """The headline: PASS, all six guards hold, FR consistency holds."""
    r = probe_fr_braid_exchange(L=10)
    assert r["verdict"] == "PASS"
    assert all(r["guards"].values())
    assert r["fr_same_2T_element_as_single_particle_2pi"] is True
    assert r["uses_analytic_qbody"] is False
    assert r["reflection_free"] is True
    assert r["sigma_sign"] < 0.0
    assert r["sigma2_sign"] > 0.0


def test_chord_vs_peer_call_is_honest_peer():
    """chord-vs-peer (prereg §2.2): the call is PEER-ahead (generic-FR), NOT a chord.

    The non-A4 control (a generic-axis 2π loop) ALSO reaches −I, so the
    double-cover → −1 chain is generic to any soliton/double-cover framework and is
    NOT forced specifically by the A4 connect-map. Honest ceiling: ahead-of-SM-axiom
    but generic-soliton-class. No chord inflation.
    """
    r = probe_fr_braid_exchange(L=10)
    assert r["non_a4_control"]["reaches_minus_I"] is True
    assert "PEER" in r["chord_vs_peer"]


def test_verdict_stable_across_lattice_size():
    """The verdict is not an L=10 artifact: PASS at L=8 and L=12 as well."""
    for L in (8, 12):
        r = probe_fr_braid_exchange(L=L)
        assert r["verdict"] == "PASS", f"L={L} verdict={r['verdict']}"
        assert r["sigma_sign"] < 0.0
        assert r["self_winding_around_carrier1"] == 0
        assert r["partner_winding_around_carrier2"] != 0
