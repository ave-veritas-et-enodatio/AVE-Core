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
    inverse_permutation,
    link_rotation_permutation,
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
# THE FIX (2026-06-20, Grant option a): the holonomy is HOMOTOPY-INVARIANT and
# CUT-GAUGE-INDEPENDENT — a direction-signed disclination holonomy, C3^(net_winding).
# ─────────────────────────────────────────────────────────────────────────────
def test_holonomy_is_homotopy_invariant():
    """A there-and-back / contractible path crossing the cut twice with CANCELLING
    direction (net winding 0) → holonomy = +I. THE FIX'S CORE ASSERTION.

    Built as the encircle-1 loop traversed FORWARD then REVERSED. It crosses the
    gauge cut twice (raw n_cut = 2) but in OPPOSITE directions, so net_winding = 0:
    the Frank C3 applied once and its INVERSE once cancel to identity. Before the
    fix this returned C3² ≠ I (q0 = −0.5, sign = −1) — cut-placement-dependent and
    NOT homotopy-invariant.
    """
    net = build_diamond_net(L=8)
    loop = shortest_closed_loop(net, 0)
    centroid, normal, in_plane = loop_plane(net, loop)
    defect = {"origin": centroid, "axis": normal, "cut_dir": in_plane, "frank_port": 0}

    # Reverse a directed link (a, p) → (neighbor, reverse_port) — a connect-map walk.
    def reverse_link(a, p):
        return (net.neighbors[a][p], net.reverse_port[a][p])

    reversed_loop = [reverse_link(u, p) for (u, p) in reversed(loop)]
    there_and_back = loop + reversed_loop

    res = holonomy_of_path(net, there_and_back, defect=defect)
    assert res["closed"]
    # Raw count is 2 (crosses the cut twice) — but in CANCELLING directions.
    assert res["n_cut_crossings"] == 2
    assert res["net_winding"] == 0  # the signed winding cancels
    # → holonomy is +I: homotopy-invariant.
    assert res["holonomy_sign"] == +1.0
    assert res["so3_is_identity"] is True
    assert np.allclose(res["R"], np.eye(3), atol=ATOL)
    assert np.allclose(res["q"], [1.0, 0.0, 0.0, 0.0], atol=ATOL)


def test_holonomy_cut_gauge_independent():
    """A FIXED winding-1 loop with the defect line through it gives the SAME single
    C3 holonomy as the gauge-cut direction is SWEPT around the axis — proving the
    holonomy is now a TRUE topological invariant, not cut-placement-dependent.

    The defect (origin = loop centroid, axis = loop normal) is FIXED; only the cut
    half-plane's azimuth (`cut_dir`, rotated about the axis) is swept. For every
    azimuth the winding-1 loop must give net_winding = 1 and the same |q| spinor
    (up to overall sign — the cover lift is fixed only up to ±) and the same SO(3).
    """
    net = build_diamond_net(L=8)
    loop = shortest_closed_loop(net, 0)
    centroid, normal, in_plane = loop_plane(net, loop)
    axis = normal / np.linalg.norm(normal)
    # Right-handed in-plane basis to rotate cut_dir within the plane ⟂ axis.
    e1 = in_plane - np.dot(in_plane, axis) * axis
    e1 = e1 / np.linalg.norm(e1)
    e2 = np.cross(axis, e1)

    ref_absq = None
    ref_R = None
    for theta in np.linspace(0.0, 2.0 * np.pi, 9, endpoint=False):
        cut_dir = np.cos(theta) * e1 + np.sin(theta) * e2
        defect = {"origin": centroid, "axis": axis, "cut_dir": cut_dir, "frank_port": 0}
        res = holonomy_of_path(net, repeat_loop(loop, 1), defect=defect)
        # A single encirclement is winding-1 regardless of where the cut sits.
        assert res["net_winding"] == 1, f"theta={theta}: net_winding {res['net_winding']} != 1"
        assert not res["so3_is_identity"]  # genuine C3, not identity
        if ref_absq is None:
            ref_absq = np.abs(res["q"])
            ref_R = res["R"]
        else:
            # |q| invariant up to overall sign; SO(3) rotation identical.
            assert np.allclose(np.abs(res["q"]), ref_absq, atol=ATOL), f"theta={theta} |q| drift"
            assert np.allclose(res["R"], ref_R, atol=ATOL), f"theta={theta} R drift"
    # The single C3 spinor (½(1,1,1,1) up to sign) — independent of cut placement.
    assert np.allclose(ref_absq, [0.5, 0.5, 0.5, 0.5], atol=ATOL)


# ─────────────────────────────────────────────────────────────────────────────
# THE FIX — unit: the inverse Frank rotation is PROGRAMMATIC, R(inv) ≈ R(frank).T.
# ─────────────────────────────────────────────────────────────────────────────
def test_inverse_frank_permutation_is_rotation_inverse():
    """`inverse_permutation` is the combinatorial inverse and gives R(inv) = R.T.

    The −1-crossing branch of `link_rotation_permutation` must apply the INVERSE
    Frank rotation, computed PROGRAMMATICALLY (not hardcoded) and verified to be
    the rotation inverse. No analytic rotor enters — it is still a port-permutation.
    """
    frank = disclination_frank_permutation(0)  # (0,2,3,1)
    inv = inverse_permutation(frank)
    # Combinatorial inverse: perm ∘ inv = identity (index map).
    assert tuple(inv[frank[i]] for i in range(4)) == (0, 1, 2, 3)
    R_frank = rotation_from_port_permutation(frank)
    R_inv = rotation_from_port_permutation(inv)
    assert np.allclose(R_inv, R_frank.T, atol=ATOL)  # rotation inverse
    assert np.allclose(R_frank @ R_inv, np.eye(3), atol=ATOL)

    # link_rotation_permutation: +1 → Frank, −1 → inverse, 0 → identity.
    assert link_rotation_permutation(0) == (0, 1, 2, 3)
    assert link_rotation_permutation(+1) == frank
    assert link_rotation_permutation(-1) == inv
    # frank_override applies on +1, its programmatic inverse on −1.
    c2 = (1, 0, 3, 2)  # self-inverse C2 edge element
    assert link_rotation_permutation(+1, frank_override=c2) == c2
    assert link_rotation_permutation(-1, frank_override=c2) == inverse_permutation(c2)


# ─────────────────────────────────────────────────────────────────────────────
# HARDENING (2a): the headline −I is INDEPENDENT of the continuity sign-flip.
# ─────────────────────────────────────────────────────────────────────────────
def test_minus_I_is_flip_independent():
    """The −I on the encircle-3× loop is NOT an artifact of the cover-continuity
    sign-flip in `holonomy_of_path`.

    The flip (`if np.dot(q_next, q_running) < 0.0: q_next = -q_next`) only
    re-charts q-vs-−q for continuity of the cover lift; it must NEVER fire on the
    encircle-3× (−I) loop. We assert both (i) the diagnostic flip counter is 0 on
    that loop, and (ii) the holonomy is still −I. Two facts together prove the −I
    is produced by the lattice-link A4 product, not by the re-charting step.

    Belt-and-suspenders: we ALSO recompute the raw left-to-right quaternion
    product with the flip DISABLED and confirm it equals the operator's `q` (up to
    the global ± that the flip would only have resolved for charting) — same −I.
    """
    net = build_diamond_net(L=8)
    loop = shortest_closed_loop(net, 0)
    centroid, normal, in_plane = loop_plane(net, loop)
    defect = {"origin": centroid, "axis": normal, "cut_dir": in_plane, "frank_port": 0}

    enc3 = holonomy_of_path(net, repeat_loop(loop, 3), defect=defect)

    # (i) the continuity sign-flip never fired on the −I loop.
    assert enc3["n_continuity_flips"] == 0
    # (ii) the holonomy is still −I.
    assert enc3["holonomy_sign"] < 0.0
    assert np.allclose(enc3["q"], [-1.0, 0.0, 0.0, 0.0], atol=ATOL)

    # Belt-and-suspenders: recompute the RAW product with NO flip and confirm −I.
    q_raw = np.array([1.0, 0.0, 0.0, 0.0])
    for perm in enc3["link_perms"]:
        R_link = rotation_from_port_permutation(perm)
        q_link = rotation_matrix_to_quaternion(R_link)
        q_raw = quat_mul(q_link, q_raw)
    assert np.allclose(q_raw, enc3["q"], atol=ATOL)  # flip changed nothing
    assert np.allclose(q_raw, [-1.0, 0.0, 0.0, 0.0], atol=ATOL)


# ─────────────────────────────────────────────────────────────────────────────
# HARDENING (2b): the holonomy SIGN is the SU(2) lift of C3^(net_winding) —
# period-6 in the SIGNED winding.
#
# This is the direction-signed (homotopy-invariant) operator (2026-06-20,
# Grant-adjudicated option a). For a MONOTONE encircling path (`repeat_loop`) every
# crossing has the SAME sign, so net_winding == raw n_cut == n and the C3^n
# period-6 sign law is UNCHANGED. The earlier "even count of 2/4 → sign −1, not +I"
# framing was about the RAW crossing count of NON-monotone paths; for a true
# topological invariant the relevant quantity is the SIGNED winding, and the
# there-and-back cancellation case (net winding 0 → +I, raw crossings 2) is now
# covered directly by `test_holonomy_is_homotopy_invariant`.
# ─────────────────────────────────────────────────────────────────────────────
def test_holonomy_sign_follows_encircle_count_mod_6():
    """Holonomy sign is the SU(2) lift of C3^(net_winding): period-6 in the winding.

    For the MONOTONE `repeat_loop` family net_winding == raw n_cut == n, so this
    pins the FULL period-6 sign law (incl. the n=2,4 → sign −1 cases). The signed
    winding equals the raw count here precisely because every crossing of a
    monotone encircling loop has the same direction sign.
    """
    net = build_diamond_net(L=8)
    loop = shortest_closed_loop(net, 0)
    centroid, normal, in_plane = loop_plane(net, loop)
    defect = {"origin": centroid, "axis": normal, "cut_dir": in_plane, "frank_port": 0}

    # winding from 0..6 via the repeat-loop family (single encircling defect).
    expected_q0 = {0: 1.0, 1: 0.5, 2: -0.5, 3: -1.0, 4: -0.5, 5: 0.5, 6: 1.0}
    expected_sign = {0: +1.0, 1: +1.0, 2: -1.0, 3: -1.0, 4: -1.0, 5: +1.0, 6: +1.0}
    expected_so3id = {0: True, 1: False, 2: False, 3: True, 4: False, 5: False, 6: True}

    for n in range(7):
        if n == 0:
            res = holonomy_of_path(net, loop, defect=None)
        else:
            res = holonomy_of_path(net, repeat_loop(loop, n), defect=defect)
            assert res["n_cut_crossings"] == n, f"n={n}: expected {n} crossings"
            # MONOTONE loop: every crossing same sign ⇒ net_winding == raw count.
            assert res["net_winding"] == n, f"n={n}: expected net_winding {n}"
        assert np.isclose(res["q"][0], expected_q0[n], atol=ATOL), f"n={n} q0"
        assert res["holonomy_sign"] == expected_sign[n], f"n={n} sign"
        assert res["so3_is_identity"] is expected_so3id[n], f"n={n} so3"

    # For the monotone family an even WINDING of 2 or 4 gives sign = −1, NOT +I;
    # only windings ≡ 0 (mod 6) give +I. (A there-and-back path with net winding 0
    # gives +I despite an even RAW count — see test_holonomy_is_homotopy_invariant.)
    res2 = holonomy_of_path(net, repeat_loop(loop, 2), defect=defect)
    res4 = holonomy_of_path(net, repeat_loop(loop, 4), defect=defect)
    assert res2["net_winding"] == 2 and res2["holonomy_sign"] < 0.0
    assert res4["net_winding"] == 4 and res4["holonomy_sign"] < 0.0


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


def test_minus_I_requires_genuine_winding_3_not_wrapping_artifact():
    """The −I is the winding-3 invariant — at L = 6 the wrapping loop is winding-1.

    CORRECTED by the homotopy-invariance fix (2026-06-20). The pre-fix test
    asserted enc3 → −I at L = 6 ("the 2π-from-links −I survives even on the small
    wrapping lattice"). That −I was a SIGN-BLIND RAW-COUNT ARTIFACT: at L = 6 the
    shortest fundamental cycle WRAPS the small torus and crosses the gauge cut
    THREE times in ONE traversal with directions [+1, −1, +1] — net winding +1, a
    genuine single encirclement. The old operator counted all three as +C3 (raw
    n_cut = 3) → C3³ = −I; the direction-signed operator nets them to C3¹ = the
    single C3 (sign +1, SO(3) ≠ I), the honest holonomy of a winding-1 loop.
    (The walker's unwrapped position then drifts off the fixed cut, so the n=3,6
    repeats add no further crossings — another tell that this loop is not a clean
    local encircling face.)

    The load-bearing winding-3 → −I physics is robust on a NON-wrapping local face
    (L ≥ 8): see `test_2pi_from_links_is_minus_I` and `test_probe_stable_across_
    lattice_size`. This test pins the corrected small-lattice behavior so a future
    regression toward the raw-count artifact is caught.
    """
    net = build_diamond_net(L=6)
    loop = shortest_closed_loop(net, 0)
    centroid, normal, in_plane = loop_plane(net, loop)
    defect = {"origin": centroid, "axis": normal, "cut_dir": in_plane, "frank_port": 0}
    enc3 = holonomy_of_path(net, repeat_loop(loop, 3), defect=defect)
    # Raw crossing count is 3 (the old artifact), but the |winding| is 1.
    assert enc3["n_cut_crossings"] == 3
    # |net_winding| == 1, NOT 3 — a single encirclement. The SIGN (±1, i.e. C3 vs
    # C3⁻¹) is an orientation GAUGE: it tracks which way shortest_closed_loop happens
    # to traverse this torus-wrapping cycle, which is environment-dependent (the
    # loop generator is not orientation-pinned). Only the magnitude is physical —
    # same reason np.abs(q) is used two lines below. (The headline winding-3 → −I is
    # orientation-robust because −I is central + self-inverse.)
    assert abs(enc3["net_winding"]) == 1  # the wrapping loop is a single encirclement
    assert enc3["holonomy_sign"] > 0.0  # C3¹ (either orientation has q0 = +0.5), NOT −I
    assert not enc3["so3_is_identity"]  # genuine 120° C3, not a closed 2π loop
    assert np.allclose(np.abs(enc3["q"]), [0.5, 0.5, 0.5, 0.5], atol=ATOL)
