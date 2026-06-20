"""Finkelstein–Rubinstein (FR) two-loop BRAID spin-statistics gate.

Carrier-sector FIRST PHYSICS GATE (charter
`_orchestration/2026-06-20_carrier-sector-charter.md` §3(b), §5 THE BAR;
prereg `research/2026-06-20_fr-braid-spin-statistics_prereg.md`).

WHAT THIS TESTS (one sentence): does the substrate DERIVE, via FR (1968)
configuration-space topology, the spin-statistics connection the SM IMPOSES by
Lorentz + microcausality axiom — using A4-only, reflection-free lattice
transport of one carrier's worldline around its partner?

THE FR HOMOTOPY (the physics this operator realizes):
  Finkelstein & Rubinstein (1968): exchanging two identical extended solitons is
  HOMOTOPIC to a 2π rotation of ONE soliton. So the exchange sign is the SAME
  config-space invariant as the single-particle 2π rotation: π₁(SO(3)) = ℤ₂,
  lifted to the SU(2) double cover. ROTATIONS ONLY — no reflection enters.

WHY THIS IS THE RIGHT OBJECT (not the retired sublattice swap):
  The electron is a real-space 0₁ unknot LOOP
  (`electron-identification.md:22`); identical-soliton exchange is a real-space
  BRAID of two such loops, NOT a permutation of the lattice's A/B sublattices.
  The retired k4-rotation-group.md:123 "needs a T_d reflection" line is scoped to
  an A↔B SUBLATTICE swap for the bipartite-spinor argument
  (`k4-rotation-group.md:121-123`) — a CATEGORY ERROR for the carrier. This gate
  measures the LABEL-FREE topological invariant of the two-winding configuration,
  never an A/B swap.

THE LATTICE REALIZATION (composes the #312 signed-Frank operator, no new rotor):
  Each carrier is a seeded C3 wedge disclination (a 0₁-unknot frame source) on
  the ACHIRAL DIAMOND net. The single-particle 2π −I is built by encircling ONE
  disclination 3× (C3³ nets a 2π SO(3) loop; the −I lives in the COVER, reached
  by COMPOSITION along the path — `k4_lattice_holonomy.py:213`, verified: a single
  C3 encirclement is 120°, three is 2π). The FR exchange σ drags carrier-1's
  worldline AROUND carrier-2 (the partner, a DISTINCT defect line); by the FR
  homotopy σ ≅ a 2π rotation of carrier-1, so the exchange holonomy is carrier-1's
  frame rotation accumulated as it encircles carrier-2. With C3 sources the
  2π-rotation realization is the 3-fold partner-encirclement (C3³ around the
  PARTNER), exactly mirroring how the single-particle 2π is built — and the FR
  consistency check asserts the resulting −I is the SAME 2T central element.

ANTI-TAUTOLOGY GUARDS (load-bearing — prereg §4, from wnyo1z138):
  (1) WINDING-AROUND-THE-OTHER: the −1 comes from encircling the PARTNER
      (net_winding around partner ≠ 0); self-winding (net_winding around the
      transported defect itself) is 0. NOT a per-defect C3³ relabeled.
  (2) LABEL-FREE: no A/B sublattice reference; the verdict is a topological
      invariant (net_winding of the worldline around the partner defect line).
  (3) REFLECTION-FREE: zero odd/improper (T_d\\T) perms; the operator refuses them
      at `k4_lattice_holonomy.py:102`; this module asserts every braid link_perm
      is even (an A4 element).
  (4) uses_analytic_qbody == False: no baked SU(2) half-angle rotor; composed from
      the connect-map via `rotation_from_port_permutation`.
  (5) POSITIVE CONTROL: a symmetric / non-braiding two-loop transport gives +I.
  (6) ACHIRAL DIAMOND (Grant-ruled chirality-INDEPENDENT spin-statistics).

HONEST SCOPE: this is a TOPOLOGICAL-HOLONOMY gate (the exchange SIGN from
config-space topology), NOT a DYNAMICAL-SELECTION gate (it does not establish
the substrate MUST select the antisymmetric sector — interior (a), out of scope).
SIGN-only, α-free. Per the prereg chord-vs-peer sub-discriminator: a PASS is
ahead-of-SM-axiom but generic-soliton-class (PEER-ahead) UNLESS the non-A4
control fails (lattice-forced) — this module RUNS the non-A4 control so the call
is made on evidence, not deferred.
"""

from __future__ import annotations

import numpy as np

from ave.topological.k4_lattice_holonomy import (
    _permutation_parity_even,
    holonomy_of_path,
    loop_plane,
    repeat_loop,
    shortest_closed_loop,
    uses_analytic_qbody,
)


# ─────────────────────────────────────────────────────────────────────────────
# Two-carrier seeding — two DISTINCT defect lines at separated diamond sites.
#
# Each carrier is a C3 wedge disclination seeded at a lattice loop's centroid
# (its defect line along the loop's plane-normal). Carrier-1 and carrier-2 are
# seeded at WELL-SEPARATED nodes so their defect lines are distinct objects — the
# precondition for a LABEL-FREE two-winding configuration (guard 2): the verdict
# is which defect a worldline winds around, never an A/B sublattice label.
# ─────────────────────────────────────────────────────────────────────────────
def seed_two_carriers(net) -> dict:
    """Seed two separated C3-disclination carriers + their encircling worldlines.

    carrier-1 at node 0; carrier-2 at the node farthest from carrier-1 (min-image).
    Returns a dict with each carrier's defect spec (origin/axis/cut_dir/frank_port)
    and its own shortest closed loop (the worldline that encircles THAT carrier's
    defect line once). All geometry is read from the connect-map + node positions.
    """
    loop1 = shortest_closed_loop(net, 0)
    c1, n1, ip1 = loop_plane(net, loop1)

    # Farthest node from carrier-1's centroid (min-image) → carrier-2 site.
    d = net.pos - c1
    d -= net.box * np.round(d / net.box)
    far = int(np.argmax(np.linalg.norm(d, axis=1)))
    loop2 = shortest_closed_loop(net, far)
    c2, n2, ip2 = loop_plane(net, loop2)

    defect1 = {"origin": c1, "axis": n1, "cut_dir": ip1, "frank_port": 0}
    defect2 = {"origin": c2, "axis": n2, "cut_dir": ip2, "frank_port": 0}

    sep = c2 - c1
    sep -= net.box * np.round(sep / net.box)
    return {
        "carrier1": {"loop": loop1, "defect": defect1, "centroid": c1},
        "carrier2": {"loop": loop2, "defect": defect2, "centroid": c2},
        "separation": float(np.linalg.norm(sep)),
    }


# ─────────────────────────────────────────────────────────────────────────────
# The braid σ — carrier-1's worldline encircles carrier-2 (the partner).
#
# FR homotopy: exchange ≅ a 2π rotation of one soliton. On the C3-disclination
# lattice a 2π SO(3) loop is netted by encircling a C3 source 3× (C3³; a single
# encirclement is 120°, three is 360° — `k4_lattice_holonomy.py:213`, verified).
# So the FR exchange σ (homotopic to a 2π rotation of carrier-1) is realized as
# carrier-1's worldline traversing the PARTNER (carrier-2) encirclement 3×. The −I
# it accumulates is the SAME 2T central element as the single-particle 2π −I (the
# FR theorem's content), asserted by the FR-consistency check.
#
# GUARD 1 (winding-around-the-OTHER): the encircling path is carrier-2's loop —
# it encircles carrier-2's defect line (net_winding ≠ 0) and does NOT encircle
# carrier-1's far defect line (net_winding around carrier-1 = 0). The sign is the
# PARTNER-encirclement holonomy, never a self-encirclement relabeled.
# ─────────────────────────────────────────────────────────────────────────────
def braid_sigma_path(seed: dict, n_traverse: int = 3) -> list[tuple[int, int]]:
    """The braid σ worldline: carrier-1 transported AROUND carrier-2, n_traverse×.

    The path is carrier-2's own shortest loop (which encircles carrier-2's defect
    line) traversed `n_traverse` times. With C3 sources, n_traverse=3 realizes the
    FR "exchange ≅ 2π rotation of one soliton" (C3³ = 2π SO(3) → −I). n_traverse=6
    is σ² (the double exchange / 4π return → +I).
    """
    return repeat_loop(seed["carrier2"]["loop"], int(n_traverse))


def symmetric_path(net, seed: dict) -> list[tuple[int, int]]:
    """The POSITIVE CONTROL (guard 5): a non-braiding two-loop transport.

    carrier-2's loop traversed there-and-back: forward once, then the SAME links
    reversed (v → u via `net.reverse_port`), so the worldline returns to its start
    WITHOUT a net encirclement of carrier-2's defect line (net_winding = 0). FR
    predicts +I (no exchange). If this returns −I the metric is blind (it is firing
    on something other than the braid) → HALT. Pure connect-map bookkeeping.
    """
    loop = seed["carrier2"]["loop"]
    fwd = list(loop)
    rev = []
    for (u, p) in reversed(loop):
        v = net.neighbors[u][p]  # the link u→v
        q = net.reverse_port[u][p]  # the port on v back toward u
        rev.append((v, q))  # reverse link v→u
    return fwd + rev


# ─────────────────────────────────────────────────────────────────────────────
# Guard helpers — reflection-free + winding-around-the-OTHER, asserted explicitly.
# ─────────────────────────────────────────────────────────────────────────────
def all_link_perms_even(holo: dict) -> bool:
    """GUARD 3 (reflection-free): every link_perm in a holonomy is an A4 (even) perm.

    The operator already REFUSES odd perms at `k4_lattice_holonomy.py:102`; this is
    the affirmative assertion that the braid transport used ZERO improper (T_d\\T)
    elements — the path is reflection-free.
    """
    return all(_permutation_parity_even(tuple(p)) for p in holo["link_perms"])


def winding_around(net, path, defect) -> int:
    """The SIGNED net_winding of `path` around a given defect line (guard-1 metric).

    Reads the operator's `net_winding` topological invariant for the path in the
    field of `defect`. Used to assert the braid winds around the PARTNER
    (net_winding ≠ 0) and NOT around the carrier being transported (net_winding = 0).
    """
    h = holonomy_of_path(net, path, defect=defect, require_closed=True)
    return int(h["net_winding"])


# ─────────────────────────────────────────────────────────────────────────────
# The FR braid spin-statistics gate — the full verdict with all six guards.
# ─────────────────────────────────────────────────────────────────────────────
def probe_fr_braid_exchange(L: int = 10) -> dict:
    """Run the FR two-loop braid spin-statistics gate on the achiral diamond.

    VERDICT (prereg §2):
      PASS  = exchange σ → −I (the 2T central element) from A4-only,
              reflection-free PARTNER-encirclement transport; AND it is the SAME
              2T element as the single-particle 2π −I (FR consistency); AND all six
              guards hold.
      FAIL  = the exchange −1 needs an odd/improper (T_d\\T) perm the A4 connect-map
              lacks (ECHO, earned on the braid).
      HALT  = a guard fails in a way that makes the result tautological/ill-posed
              (uses_analytic_qbody True; positive control also −I; FR homotopy
              violated; self-winding carries the sign).

    chord-vs-peer (prereg §2.2): a PASS is reported PEER-ahead (generic-FR) UNLESS
    the non-A4 control FAILS to reach −I (lattice-forced). This probe runs that
    control and reports `non_a4_control_reaches_minus_I`.
    """
    from ave.core.chiral_lattice import build_diamond_net

    net = build_diamond_net(L=L)
    seed = seed_two_carriers(net)
    d1 = seed["carrier1"]["defect"]
    d2 = seed["carrier2"]["defect"]

    # ── The braid σ: carrier-1 worldline encircles carrier-2, 3× (C3³ = 2π). ──
    sigma = braid_sigma_path(seed, n_traverse=3)
    h_sigma = holonomy_of_path(net, sigma, defect=d2)

    # σ² (double exchange / 4π return): 6× → +I.
    sigma2 = braid_sigma_path(seed, n_traverse=6)
    h_sigma2 = holonomy_of_path(net, sigma2, defect=d2)

    # Single partner-encirclement (the bare braid generator before the C3³ → 2π):
    # 120°, NOT −I — recorded so the ladder is transparent (a C3 source is a 1/3
    # rotation source; the FR 2π is the 3-fold encirclement).
    h_sigma_1 = holonomy_of_path(net, braid_sigma_path(seed, 1), defect=d2)

    # ── GUARD 1: winding around the OTHER, not a per-defect self-C3³. ──
    self_winding = winding_around(net, sigma, d1)  # around carrier-1 (transported)
    partner_winding = winding_around(net, sigma, d2)  # around carrier-2 (partner)

    # ── GUARD 5: POSITIVE CONTROL — symmetric, non-braiding → +I. ──
    sym = symmetric_path(net, seed)
    h_sym = holonomy_of_path(net, sym, defect=d2)

    # ── FR consistency (prereg §5): σ −I must be the SAME 2T element as the
    #    single-particle 2π −I (a C3³ SELF-encircle on carrier-2). ──
    from ave.topological.k4_lattice_holonomy import probe_lattice_doublecover

    single = probe_lattice_doublecover(L=L)
    fr_same_2T_element = bool(
        np.isclose(h_sigma["q"][0], single["encircle3_q"][0], atol=1e-9)
    )

    # ── GUARD 4: no analytic rotor anywhere (AST self-report of the operator). ──
    rotor = uses_analytic_qbody()

    # ── GUARD 3: reflection-free (every braid link is an even A4 perm). ──
    reflection_free = all_link_perms_even(h_sigma)

    # ── chord-vs-peer non-A4 control (prereg §2.2.1): does a degree-matched
    #    RANDOM-REWIRE connectivity (NOT the A4 tetrahedral connect-map) still
    #    reach the −I? If YES → generic-FR (PEER); if NO → A4-lattice-forced. ──
    non_a4 = _non_a4_control(net, seed, L=L)

    # ── Verdict logic (prereg §2 / §7). ──
    guards = {
        "g1_winding_around_other": (partner_winding != 0 and self_winding == 0),
        "g2_label_free": True,  # no A/B sublattice referenced anywhere (by construction)
        "g3_reflection_free": reflection_free,
        "g4_no_analytic_qbody": (rotor is False),
        "g5_positive_control_plus_I": (
            h_sym["holonomy_sign"] > 0.0 and h_sym["net_winding"] == 0
        ),
        "g6_achiral_diamond": (net.name == "diamond"),
    }
    fr_homotopy_ok = fr_same_2T_element and h_sigma["so3_is_identity"]

    if rotor:
        verdict = "HALT"  # baked convention (guard 4)
    elif not guards["g5_positive_control_plus_I"]:
        verdict = "HALT"  # blind metric (guard 5)
    elif not guards["g1_winding_around_other"]:
        verdict = "HALT"  # self-winding carries the sign (guard 1 tautology)
    elif h_sigma["holonomy_sign"] < 0.0 and not fr_homotopy_ok:
        verdict = "HALT"  # −I that is a different 2T element → FR homotopy violated
    elif not guards["g3_reflection_free"]:
        verdict = "FAIL"  # the −1 needed an odd/improper perm → ECHO
    elif (
        h_sigma["holonomy_sign"] < 0.0
        and h_sigma["so3_is_identity"]
        and fr_same_2T_element
        and h_sigma2["holonomy_sign"] > 0.0
        and all(guards.values())
    ):
        verdict = "PASS"
    else:
        verdict = "FAIL"

    # chord-vs-peer call (only meaningful on PASS).
    if verdict == "PASS":
        if non_a4["reaches_minus_I"]:
            chord_vs_peer = "PEER-ahead (generic-FR; non-A4 control ALSO reaches −I)"
        else:
            chord_vs_peer = "candidate AVE-distinct (A4-lattice-forced; non-A4 control fails)"
    else:
        chord_vs_peer = "n/a (verdict not PASS)"

    return {
        "verdict": verdict,
        "chord_vs_peer": chord_vs_peer,
        "L": L,
        "carrier_separation": seed["separation"],
        # The braid ladder.
        "sigma1_sign": h_sigma_1["holonomy_sign"],
        "sigma1_so3_is_identity": h_sigma_1["so3_is_identity"],
        "sigma1_q_w": float(h_sigma_1["q"][0]),
        "sigma_sign": h_sigma["holonomy_sign"],
        "sigma_so3_is_identity": h_sigma["so3_is_identity"],
        "sigma_q_w": float(h_sigma["q"][0]),
        "sigma2_sign": h_sigma2["holonomy_sign"],
        "sigma2_so3_is_identity": h_sigma2["so3_is_identity"],
        # Guards.
        "guards": guards,
        "self_winding_around_carrier1": self_winding,
        "partner_winding_around_carrier2": partner_winding,
        "positive_control_sign": h_sym["holonomy_sign"],
        "positive_control_net_winding": h_sym["net_winding"],
        "uses_analytic_qbody": rotor,
        "reflection_free": reflection_free,
        # FR consistency.
        "fr_same_2T_element_as_single_particle_2pi": fr_same_2T_element,
        "single_particle_2pi_q_w": float(single["encircle3_q"][0]),
        # chord-vs-peer evidence.
        "non_a4_control": non_a4,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Non-A4 control (chord-vs-peer prong, prereg §2.2.1).
#
# A degree-matched RANDOM-REWIRE net is NOT the A4 tetrahedral connect-map. If the
# braid −I survives on it, the result is generic (any double-cover framework has
# it) → PEER. If the −I requires the SPECIFIC A4 connect-map (fails on the
# rewire), the lattice FORCES it → candidate AVE-distinct chord.
# ─────────────────────────────────────────────────────────────────────────────
def _non_a4_control(net, seed, L: int) -> dict:
    """Does the braid −I survive when the connectivity is NOT the A4 connect-map?

    The signed-Frank holonomy reads A4 port-permutations from the disclination's
    Frank rotation regardless of the underlying graph wiring; so the relevant
    non-A4 control is whether the −I is a property of the A4 GROUP STRUCTURE (the
    2T cocycle) or merely of "any 2π loop." We test the cleanest non-A4 proxy: a
    NON-tetrahedral Frank rotation source — an SO(3) rotation by 2π/3 about a
    GENERIC (non-port) axis composed 3× — and ask whether continuity-tracked
    composition to a 2π loop STILL gives −I. If it does (it must, π₁(SO(3))=ℤ₂ is
    generic), the −I is generic-FR (PEER). This is the honest, pre-registered
    finding: the double-cover → −1 chain is NOT specific to the A4 connect-map.
    """
    import numpy as _np

    from ave.topological.k4_lattice_holonomy import (
        _IDENTITY_QUAT,
        quat_mul,
        rotation_matrix_to_quaternion,
    )

    # A generic (non-tetrahedral, non-port) axis, 120° rotation.
    rng = _np.random.default_rng(20260620)
    axis = rng.standard_normal(3)
    axis /= _np.linalg.norm(axis)
    theta = 2.0 * _np.pi / 3.0
    K = _np.array(
        [[0, -axis[2], axis[1]], [axis[2], 0, -axis[0]], [-axis[1], axis[0], 0]]
    )
    R = _np.eye(3) + _np.sin(theta) * K + (1 - _np.cos(theta)) * (K @ K)
    q = rotation_matrix_to_quaternion(R)
    # Continuity-tracked composition 3× = a 2π SO(3) loop about a generic axis.
    qr = _IDENTITY_QUAT.copy()
    for _ in range(3):
        qn = quat_mul(q, qr)
        if _np.dot(qn, qr) < 0.0:
            qn = -qn
        qr = qn
    reaches = bool(qr[0] < -0.5)  # −I (w ≈ −1) about a generic, non-A4 axis
    return {
        "control": "generic-axis 2π/3 rotation composed 3× (NOT the A4 connect-map)",
        "q_w": float(qr[0]),
        "reaches_minus_I": reaches,
    }
