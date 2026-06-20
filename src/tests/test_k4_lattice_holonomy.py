"""Tests for the K4 lattice-holonomy operator — double-cover FROM CONNECTIVITY.

Carrier-sector PREREQUISITE (charter `_orchestration/2026-06-20_carrier-sector-charter.md`).
The substrate-native upgrade of the #299 analytic-rotor representability probe.

Validate-on-known (HALT if fail):
  (i)  contractible loop → +I (zero curvature on faces);
  (ii) a 2π-effecting closed link-path → −I (the double-cover emerging from the
       product of lattice-link A4 rotations).

Anti-tautology (load-bearing):
  (a) the holonomy path does NOT import/call the analytic axis-angle rotor;
  (b) scrambling the connectivity (per-link Frank assignment) CHANGES the −I.
"""

import numpy as np

from ave.core.chiral_lattice import build_diamond_net
from ave.topological.k4_lattice_holonomy import (
    PORTS,
    a4_rotation_group,
    disclination_frank_permutation,
    holonomy_of_path,
    loop_plane,
    probe_lattice_doublecover,
    quat_mul,
    repeat_loop,
    rotation_from_port_permutation,
    rotation_matrix_to_quaternion,
    shortest_closed_loop,
    uses_analytic_qbody,
)

ATOL = 1e-9


# ─────────────────────────────────────────────────────────────────────────────
# Group-theory foundations: A4 rotations from port-permutations, the 2T lift.
# ─────────────────────────────────────────────────────────────────────────────
def test_a4_group_has_12_proper_rotations():
    """The A4 port-permutation group is the 12 proper tetrahedral rotations."""
    group = a4_rotation_group()
    assert len(group) == 12  # k4-rotation-group.md §3-§4: |A4| = 12
    for perm, R in group.items():
        assert np.allclose(R @ R.T, np.eye(3), atol=ATOL), f"{perm} not orthogonal"
        assert np.isclose(np.linalg.det(R), 1.0, atol=ATOL), f"{perm} det != +1"


def test_odd_permutation_is_refused_as_reflection():
    """An ODD permutation (a reflection in T_d \\ T) is refused — chord guard."""
    # (0,1,3,2) is an odd permutation (a single transposition of 2 elements).
    import pytest

    with pytest.raises(ValueError, match="ODD"):
        rotation_from_port_permutation((0, 1, 3, 2))


def test_c3_vertex_rotation_lifts_to_minus_I_on_cube():
    """The C3 (120°) vertex rotation has order 3 in SO(3) but order 6 in SU(2).

    R³ = I (closed SO(3) loop) but q³ = −I — the seed of the double-cover.
    """
    perm = disclination_frank_permutation(0)  # (0,2,3,1)
    R = rotation_from_port_permutation(perm)
    q = rotation_matrix_to_quaternion(R)
    R3 = R @ R @ R
    q3 = quat_mul(quat_mul(q, q), q)
    assert np.allclose(R3, np.eye(3), atol=ATOL)  # SO(3): closed
    assert np.allclose(q3, [-1.0, 0.0, 0.0, 0.0], atol=ATOL)  # SU(2): −I


def test_ports_are_canonical_tetrahedral_basis():
    """PORTS match k4_tlm.py:80-86 / k4-rotation-group.md:17."""
    assert PORTS.shape == (4, 3)
    for i in range(4):
        assert np.isclose(np.linalg.norm(PORTS[i]), np.sqrt(3.0), atol=ATOL)
        for j in range(4):
            if i != j:
                assert np.isclose(np.dot(PORTS[i], PORTS[j]), -1.0, atol=ATOL)


# ─────────────────────────────────────────────────────────────────────────────
# VALIDATE-ON-KNOWN (i): contractible loop → +I.
# ─────────────────────────────────────────────────────────────────────────────
def test_contractible_loop_is_identity():
    """A real lattice face with NO defect threading it → holonomy = +I (1e-9)."""
    net = build_diamond_net(L=8)
    loop = shortest_closed_loop(net, 0)
    res = holonomy_of_path(net, loop, defect=None)  # flat connection
    assert res["closed"]
    assert res["so3_is_identity"]
    assert res["n_cut_crossings"] == 0
    assert np.allclose(res["q"], [1.0, 0.0, 0.0, 0.0], atol=ATOL)
    assert res["holonomy_sign"] > 0.0


def test_contractible_loop_with_defect_outside_is_identity():
    """Defect seeded OUTSIDE the loop → still +I (the loop does not encircle it)."""
    net = build_diamond_net(L=8)
    loop = shortest_closed_loop(net, 0)
    centroid, normal, in_plane = loop_plane(net, loop)
    defect = {
        "origin": centroid + in_plane * net.box * 0.5,  # shift out of the loop
        "axis": normal,
        "cut_dir": in_plane,
        "frank_port": 0,
    }
    res = holonomy_of_path(net, loop, defect=defect)
    assert res["n_cut_crossings"] == 0
    assert res["holonomy_sign"] > 0.0
    assert np.allclose(res["q"], [1.0, 0.0, 0.0, 0.0], atol=ATOL)


# ─────────────────────────────────────────────────────────────────────────────
# VALIDATE-ON-KNOWN (ii): a 2π-effecting closed link-path → −I.
# ─────────────────────────────────────────────────────────────────────────────
def test_2pi_from_links_is_minus_I():
    """Encircling the seeded disclination 3× nets a 2π SO(3) loop → −I (1e-9).

    The −I is the PRODUCT of lattice-link A4 Frank rotations: 3 single-encircle
    C3 (120°) rotations compose to R³ = I in SO(3) but q³ = −I in SU(2).
    """
    net = build_diamond_net(L=8)
    loop = shortest_closed_loop(net, 0)
    centroid, normal, in_plane = loop_plane(net, loop)
    defect = {"origin": centroid, "axis": normal, "cut_dir": in_plane, "frank_port": 0}

    enc1 = holonomy_of_path(net, repeat_loop(loop, 1), defect=defect)
    enc3 = holonomy_of_path(net, repeat_loop(loop, 3), defect=defect)
    enc6 = holonomy_of_path(net, repeat_loop(loop, 6), defect=defect)

    # single encircle = the genuine C3 120° (NOT identity in SO(3))
    assert enc1["n_cut_crossings"] == 1
    assert not enc1["so3_is_identity"]
    assert np.allclose(np.abs(enc1["q"]), [0.5, 0.5, 0.5, 0.5], atol=ATOL)

    # 3× encircle = 2π SO(3) loop → −I
    assert enc3["n_cut_crossings"] == 3
    assert enc3["so3_is_identity"]  # R³ = I
    assert enc3["holonomy_sign"] < 0.0
    assert np.allclose(enc3["q"], [-1.0, 0.0, 0.0, 0.0], atol=ATOL)

    # 6× encircle = 4π → +I (the spinor returns)
    assert enc6["so3_is_identity"]
    assert enc6["holonomy_sign"] > 0.0
    assert np.allclose(enc6["q"], [1.0, 0.0, 0.0, 0.0], atol=ATOL)


# ─────────────────────────────────────────────────────────────────────────────
# ANTI-TAUTOLOGY (a): no analytic axis-angle rotor in the holonomy code path.
# ─────────────────────────────────────────────────────────────────────────────
def test_no_analytic_qbody_rotor():
    """AST proof: the module does not import/call the analytic rotor (q_body etc.).

    The mentions of the rotor in docstrings/comments are anti-tautology PROSE; the
    AST check ignores comments and confirms the executable code is rotor-free.
    """
    assert uses_analytic_qbody() is False


def test_holonomy_self_reports_no_qbody():
    """The holonomy result self-reports uses_analytic_qbody = False."""
    net = build_diamond_net(L=8)
    loop = shortest_closed_loop(net, 0)
    res = holonomy_of_path(net, loop, defect=None)
    assert res["uses_analytic_qbody"] is False


# ─────────────────────────────────────────────────────────────────────────────
# ANTI-TAUTOLOGY (b): scrambling the connectivity CHANGES the holonomy.
# ─────────────────────────────────────────────────────────────────────────────
def test_connectivity_scramble_changes_holonomy():
    """Scrambling the per-link Frank assignment (→ identity) kills the −I → +I.

    If the −I survived a connectivity scramble unchanged, it would be
    convention-baked (the tautology). It does NOT survive — proving the holonomy
    reads the lattice link-rotations, not a baked half-angle convention.
    """
    net = build_diamond_net(L=8)
    loop = shortest_closed_loop(net, 0)
    centroid, normal, in_plane = loop_plane(net, loop)
    defect = {"origin": centroid, "axis": normal, "cut_dir": in_plane, "frank_port": 0}

    base = holonomy_of_path(net, repeat_loop(loop, 3), defect=defect)
    scrambled = holonomy_of_path(
        net, repeat_loop(loop, 3), defect=defect, frank_override=(0, 1, 2, 3)
    )
    assert base["holonomy_sign"] < 0.0  # baseline −I
    assert scrambled["holonomy_sign"] > 0.0  # scramble → +I
    assert base["holonomy_sign"] != scrambled["holonomy_sign"]


def test_scramble_to_different_a4_element_changes_holonomy():
    """Scrambling the Frank rotation to a C2 edge element changes the result.

    The C2 edge rotation (1,0,3,2) = (01)(23) has order 2 in SO(3); encircling 3×
    does NOT net the identity (unlike the C3), so both the SO(3) closure and the
    sign differ from the C3 baseline — the holonomy depends on WHICH A4 element.
    """
    net = build_diamond_net(L=8)
    loop = shortest_closed_loop(net, 0)
    centroid, normal, in_plane = loop_plane(net, loop)
    defect = {"origin": centroid, "axis": normal, "cut_dir": in_plane, "frank_port": 0}

    base = holonomy_of_path(net, repeat_loop(loop, 3), defect=defect)
    c2 = holonomy_of_path(
        net, repeat_loop(loop, 3), defect=defect, frank_override=(1, 0, 3, 2)
    )
    assert base["so3_is_identity"]  # C3 cubed = I
    assert not c2["so3_is_identity"]  # C2 cubed = C2 (≠ I)
    assert not np.allclose(base["q"], c2["q"], atol=ATOL)


# ─────────────────────────────────────────────────────────────────────────────
# Top-level probe verdict.
# ─────────────────────────────────────────────────────────────────────────────
def test_probe_lattice_doublecover_passes():
    """The bundled probe returns VERDICT = PASS (all gates + both anti-tautology)."""
    r = probe_lattice_doublecover(L=8)
    assert r["verdict"] == "PASS"
    assert r["uses_analytic_qbody"] is False
    assert r["scramble_changes_holonomy"] is True
    assert r["contractible_sign"] > 0.0
    assert r["encircle3_sign"] < 0.0
    assert r["encircle3_so3_is_identity"] is True


def test_probe_stable_across_lattice_size():
    """The −I and the verdict are stable across lattice sizes (not an L artifact).

    L ≥ 8 required: at L = 6 the diamond's shortest fundamental cycle WRAPS the
    small torus (unwrapped diameter > box), so it is not a clean LOCAL face and
    the contractible-loop gate's geometry is ill-defined (a real small-lattice
    limitation, NOT a holonomy bug — the encircle-3× = −I still holds at L = 6).
    """
    for L in (8, 10, 12):
        r = probe_lattice_doublecover(L=L)
        assert r["verdict"] == "PASS", f"L={L} did not PASS"
        assert r["encircle3_sign"] < 0.0, f"L={L} 2π-loop not −I"


def test_2pi_minus_I_holds_even_on_small_wrapping_lattice():
    """The load-bearing physics (encircle-3× → −I) is robust even at L = 6.

    Documents that the L = 6 probe FAIL is purely the contractible-face geometry
    (torus-wrapping loop), not the double-cover: the 2π-from-links −I survives.
    """
    net = build_diamond_net(L=6)
    loop = shortest_closed_loop(net, 0)
    centroid, normal, in_plane = loop_plane(net, loop)
    defect = {"origin": centroid, "axis": normal, "cut_dir": in_plane, "frank_port": 0}
    enc3 = holonomy_of_path(net, repeat_loop(loop, 3), defect=defect)
    assert enc3["holonomy_sign"] < 0.0
    assert enc3["so3_is_identity"]
