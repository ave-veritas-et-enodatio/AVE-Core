"""
Genesis v9 Phase-0 — REAL-dynamics smokes (executable gates).

Companion to test_chiral_lattice_smokes.py. These gates exercise the *dynamical*
smoke observers in ave.core.chiral_lattice_dynamics:

  Smoke A (CONSISTENCY GATE):  the lattice change must not break the physics that
    already worked. Energy is conserved (analytically: CONNECT is a permutation
    and S is orthogonal => the step is unitary; dynamically: closed-system drift),
    and the small-k scalar dispersion reproduces the canonical 3D link-line TLM
    network-velocity invariant c0/c_link = 1/sqrt(3) on the chiral srs net AND the
    cubic diamond reference, identically between enantiomorphs.

  Smoke B (OPTICAL ACTIVITY):  a transverse polarization frame parallel-
    transported along the exact 4_1 screw orbit carries a nonzero, MIRROR-ODD
    rotation (flips sign exactly under x->-x). Its per-length RATE does NOT cleanly
    converge at Phase-0 (discrete 4-gon-per-turn + end effects, ~9% wobble) — the
    converged dynamical rate is the Phase-1 vector-TLM deliverable. The load-bearing
    SIGNED, converged Phase-0 channel is the reflection-odd ring-writhe pseudoscalar;
    a single independently-found screw axis is handedness-ambiguous (asserted),
    because both enantiomorph space groups contain screw axes of both senses.

Every test FINDS the property from the constructed net / transport and asserts the
MEASURED value (v7 law — nothing by fiat). PHASE-0 scaffold, NO genesis run.
"""

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_dynamics as cld

_NETS = lambda L=6: {  # noqa: E731
    "srs-R": cl.build_srs_net(L, "right"),
    "srs-L": cl.build_srs_net(L, "left"),
    "diamond": cl.build_diamond_net(L),
}


# ─── Smoke A — consistency gate ──────────────────────────────────────────────
def test_connect_is_permutation_all_nets():
    """CONNECT bijection => unitary step => exact energy conservation (analytic)."""
    for nm, net in _NETS(4).items():
        assert cld.connect_is_permutation(net), f"{nm}: CONNECT must be a permutation"


def test_energy_conserved_all_nets():
    """Closed-system TLM energy drift is negligible on every net (dynamical)."""
    for nm, net in _NETS(6).items():
        drift = cld.energy_drift(net, steps=200)
        assert drift < 1e-10, f"{nm}: energy drift {drift:.2e} exceeds 1e-10"


def test_network_velocity_matches_analytic_c0():
    """Small-k dispersion reproduces the 3D-TLM invariant c0/c_link = 1/sqrt(3)
    on the chiral net AND the cubic reference (the achiral did-not-break-it gate)."""
    target = cld.ANALYTIC_NETWORK_FACTOR  # 1/sqrt(3)
    for nm, net in _NETS(8).items():
        f = cld.network_velocity_factor(net, n_steps=600)["factor"]
        assert abs(f - target) / target < 0.02, (
            f"{nm}: network factor {f:.4f} != analytic 1/sqrt3 {target:.4f}"
        )


def test_dispersion_is_enantiomorph_invariant():
    """The scalar wave speed is an ACHIRAL observable: srs-right == srs-left.
    Chirality must NOT change it (the load-bearing consistency signature)."""
    fR = cld.network_velocity_factor(cl.build_srs_net(8, "right"), n_steps=600)["factor"]
    fL = cld.network_velocity_factor(cl.build_srs_net(8, "left"), n_steps=600)["factor"]
    assert abs(fR - fL) < 1e-3, f"enantiomorph speeds differ: {fR:.5f} vs {fL:.5f}"


def test_dispersion_linear_at_small_k():
    """Non-dispersive at small k: c(k) is k-independent within tolerance."""
    for nm, net in _NETS(8).items():
        spread = cld.network_velocity_factor(net, n_steps=600)["linearity_spread"]
        assert spread < 0.02, f"{nm}: small-k dispersion non-linear, spread={spread:.3f}"


# ─── Smoke B — optical activity ──────────────────────────────────────────────
def test_transverse_transport_nonzero_and_mirror_odd():
    """The ROBUST, EXACT transverse-channel content: the Bishop-transport rotation
    along the exact 4_1 screw orbit is nonzero, and under the explicit mirror
    (x->-x) Delta_theta/L flips sign EXACTLY with magnitude preserved (and so does
    the helix's signed torsion). This is the genuine signed, mirror-odd rotation.

    NOTE (honest, not asserted as a pass): the per-length RATE itself does NOT
    cleanly converge at Phase-0 — the discrete 4-gon-per-turn orbit gives ~9%
    end/discreteness wobble (see module docstring B2). The converged dynamical
    rate is the Phase-1 vector-TLM deliverable; the converged SIGNED Phase-0
    channel is the writhe (next test)."""
    cR = cld.screw_orbit_helix("right", n_turns=3)
    cM = cR.copy()
    cM[:, 0] = -cM[:, 0]  # explicit mirror = the true left enantiomorph helix
    _, _, rR = cld.bishop_transport_rotation(cR)
    _, _, rM = cld.bishop_transport_rotation(cM)
    assert abs(rR) > 1e-3, "transport rotation must be nonzero on the chiral helix"
    assert rR * rM < 0, "mirror must flip the rotation sign"
    assert abs(rR + rM) < 1e-9 * abs(rR), f"mirror magnitude mismatch: {rR:.6f} vs {rM:.6f}"
    assert cld.helix_signed_torsion(cR) * cld.helix_signed_torsion(cM) < 0, "torsion must flip"


def test_single_screw_axis_is_handedness_ambiguous_but_writhe_is_clean():
    """HONEST limitation, asserted: a single independently-found screw axis does
    NOT discriminate handedness (srs-R 4_1 and srs-L 4_3 orbit-helices share sign),
    while the reflection-odd ring-writhe pseudoscalar DOES (clean sign-flip,
    zero on the achiral control)."""
    # (1) independently-found screw axes do NOT flip sign -> ambiguous
    _, _, rR = cld.bishop_transport_rotation(cld.screw_orbit_helix("right", 3))
    _, _, rL = cld.bishop_transport_rotation(cld.screw_orbit_helix("left", 3))
    assert rR * rL > 0, "expected the single-screw-axis channel to be handedness-ambiguous"
    # (2) the reflection-odd writhe IS the clean signed discriminator
    wR, _, _, _ = cl.net_ring_writhe(cl.build_srs_net(6, "right"))
    wL, _, _, _ = cl.net_ring_writhe(cl.build_srs_net(6, "left"))
    wD, _, _, _ = cl.net_ring_writhe(cl.build_diamond_net(6))
    assert wR * wL < 0 and abs(wR + wL) < 1e-2 * abs(wR), "writhe must sign-flip + match"
    assert abs(wD) < 0.05 * abs(wR), "achiral control writhe must be ~0"
