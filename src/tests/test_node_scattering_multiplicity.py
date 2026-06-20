"""Bedrock + anchor tests for the Node-Scattering Multiplicity Gate (scope b).

Prereg:  research/2026-06-20_node-scattering-containment-gate_prereg.md (commit f87914fa).
Result:  research/2026-06-20_node-scattering-containment-gate_result.md.

These tests ASSERT the frozen validate-on-known anchors (prereg §2) and the HALT
conditions (prereg §5). The bedrock is PURE LINEAR ALGEBRA on the actual srs /
diamond bond-graph CONNECT map -- NOT the dense TETRA_OFFSETS cube.

  * §2a bare spectrum: S3 -> {+1x1, -1x2}, S4 -> {+1x1, -1x3}  (the distinctness)
  * §2b photon anchor: srs differential multiplicity (2) == photon transverse DOF
  * §2c winding anchor: seeded (2,3) reproduces Q_link=3; null -> 0
  * §2d alpha-free: alpha->2alpha leaves the spectrum + Q bit-identical
  * H1 distinctness: srs (deg 3) and diamond (deg 4) are STRUCTURALLY different.
"""

import importlib

import numpy as np

from ave.solvers.node_scattering_multiplicity import (
    assemble_global_scattering,
    bedrock_validate_on_known,
    common_mode_projector,
    differential_projector,
    global_spectrum,
    local_scatter_spectrum,
    operators_are_distinct,
)
from ave.core.chiral_lattice import build_diamond_net, build_srs_net


# ─────────────────────────────────────────────────────────────────────────────
# §2a — bare-spectrum validate-on-known (the distinctness witness)
# ─────────────────────────────────────────────────────────────────────────────
def test_s3_bare_spectrum_plus1_minus1x2():
    """S3 = (2/3)J - I -> eigenvalues {+1 x1, -1 x2}; differential mult = 2."""
    s = local_scatter_spectrum(3)
    assert s["mult_plus1"] == 1
    assert s["mult_minus1"] == 2
    assert s["differential_multiplicity"] == 2
    assert s["spectrum_is_canonical"]
    assert s["S_squared_is_identity"]
    assert sorted(np.round(s["eigenvalues"], 9)) == [-1.0, -1.0, 1.0]


def test_s4_bare_spectrum_plus1_minus1x3():
    """S4 = (1/2)J - I -> eigenvalues {+1 x1, -1 x3}; differential mult = 3."""
    s = local_scatter_spectrum(4)
    assert s["mult_plus1"] == 1
    assert s["mult_minus1"] == 3
    assert s["differential_multiplicity"] == 3
    assert s["spectrum_is_canonical"]
    assert s["S_squared_is_identity"]
    assert sorted(np.round(s["eigenvalues"], 9)) == [-1.0, -1.0, -1.0, 1.0]


def test_common_mode_is_the_port_sum():
    """The single +1 eigenvector is the symmetric port-sum (the common mode =
    Grant's bulk-saturation channel, Fork B)."""
    for n in (3, 4):
        s = local_scatter_spectrum(n)
        assert s["common_mode_is_port_sum"], f"n={n}: +1 mode is not the port-sum"


# ─────────────────────────────────────────────────────────────────────────────
# §2b — photon corpus anchor: srs differential multiplicity == 2 transverse DOF
# ─────────────────────────────────────────────────────────────────────────────
def test_srs_differential_multiplicity_matches_photon_transverse_dof():
    """The srs (degree-3) differential multiplicity = 2 = the photon's 2 transverse
    polarizations (src/tests/engine_acceptance/test_l1_photon.py:243-268;
    engine-acceptance-suite.md:178)."""
    srs_diff_mult = local_scatter_spectrum(3)["differential_multiplicity"]
    photon_transverse_dof = 2  # corpus anchor (verified in the prereg ledger)
    assert srs_diff_mult == photon_transverse_dof


# ─────────────────────────────────────────────────────────────────────────────
# §2c — winding-sector anchor: seeded (2,3) reproduces the charge-"3" integer
# ─────────────────────────────────────────────────────────────────────────────
def test_winding_anchor_2_3_reproduces_Q3_and_null_is_zero():
    """Seed a known (p,q)=(2,3) winding on the Cosserat omega-grade; the
    differential (phase-winding) operator must reproduce Q_link=3 (poloidal = q),
    w_tor=2 (toroidal = p); the omega=0 null must give Q=0. (charge_quantization,
    omega-grade only, A1-perp-T2.)"""
    from ave.topological.charge_quantization import (
        compute_Q_link,
        seed_pq_winding,
    )

    N, R, r = 32, 7.0, 2.3
    res = compute_Q_link(seed_pq_winding(N, 2, 3, R, r), R, r)
    assert res["Q_link"] == 3, f"expected Q_link=3, got {res['Q_link']}"
    assert res["w_tor"] == 2, f"expected w_tor=2 (toroidal p), got {res['w_tor']}"
    null = compute_Q_link(np.zeros((N, N, N, 3)), R, r)
    assert null["Q_link"] == 0


# ─────────────────────────────────────────────────────────────────────────────
# §2d — alpha-free invariance (the load-bearing, frame-independent anchor)
# ─────────────────────────────────────────────────────────────────────────────
def test_bare_spectrum_is_alpha_free_by_construction():
    """S_n contains no alpha: doubling ALPHA leaves the spectrum bit-identical
    (the operators don't import ALPHA -- structural alpha-invariance)."""
    import ave.core.constants as C
    import ave.solvers.node_scattering_multiplicity as nsm

    s3_a = local_scatter_spectrum(3)["eigenvalues"]
    s4_a = local_scatter_spectrum(4)["eigenvalues"]
    alpha0 = C.ALPHA
    try:
        C.ALPHA = 2.0 * alpha0
        importlib.reload(nsm)
        s3_b = nsm.local_scatter_spectrum(3)["eigenvalues"]
        s4_b = nsm.local_scatter_spectrum(4)["eigenvalues"]
    finally:
        C.ALPHA = alpha0
        importlib.reload(nsm)
    assert np.allclose(s3_a, s3_b)
    assert np.allclose(s4_a, s4_b)


def test_winding_integer_is_alpha_invariant():
    """Q_link under alpha->2alpha: |dQ/Q| < 1e-6 (frame-independent anchor)."""
    import ave.core.constants as C
    import ave.topological.charge_quantization as cq

    N, R, r = 32, 7.0, 2.3
    Q_a = cq.compute_Q_link(cq.seed_pq_winding(N, 2, 3, R, r), R, r)["Q_link"]
    alpha0 = C.ALPHA
    try:
        C.ALPHA = 2.0 * alpha0
        importlib.reload(cq)
        Q_b = cq.compute_Q_link(cq.seed_pq_winding(N, 2, 3, R, r), R, r)["Q_link"]
    finally:
        C.ALPHA = alpha0
        importlib.reload(cq)
    assert abs(Q_b - Q_a) / max(abs(Q_a), 1) < 1e-6


# ─────────────────────────────────────────────────────────────────────────────
# H1 — distinctness: srs (n=3) and diamond (n=4) are STRUCTURALLY different
# ─────────────────────────────────────────────────────────────────────────────
def test_srs_and_diamond_are_distinct_operators():
    """HALT-condition H1 must NOT fire: srs (deg 3) and diamond (deg 4) assemble
    operators of DIFFERENT dimension AND different differential multiplicity --
    NOT the identical dense-cube collapse the prior build had."""
    srs = build_srs_net(L=2)
    dia = build_diamond_net(L=4)
    dist = operators_are_distinct(srs, dia)
    assert dist["distinct"]
    assert not dist["collapse_detected"]
    assert dist["diff_mult_a"] != dist["diff_mult_b"]
    M_srs = assemble_global_scattering(srs)
    M_dia = assemble_global_scattering(dia)
    assert M_srs.shape != M_dia.shape  # 192 vs 64 DOF


def test_assembled_lattice_operators_are_orthogonal():
    """𝓢 = C @ (I (x) S_n) is a product of a reflection and a permutation, so it is
    orthogonal -- all eigenvalues lie on the unit circle (operator well-formed)."""
    for net in (build_srs_net(L=2), build_diamond_net(L=4)):
        spec = global_spectrum(net)
        assert spec["is_orthogonal"]
        assert spec["all_eigs_unit_modulus"]


# ─────────────────────────────────────────────────────────────────────────────
# Projector sanity (the sector fixed FROM THE OPERATOR, prereg §3.1)
# ─────────────────────────────────────────────────────────────────────────────
def test_differential_and_common_projectors_partition_identity():
    """P_{-1} + P_{+1} = I, each idempotent, ranks n-1 and 1."""
    for n in (3, 4):
        Pm = differential_projector(n)
        Pp = common_mode_projector(n)
        assert np.allclose(Pm + Pp, np.eye(n))
        assert np.allclose(Pm @ Pm, Pm)
        assert np.allclose(Pp @ Pp, Pp)
        assert round(np.trace(Pm)) == n - 1  # differential rank
        assert round(np.trace(Pp)) == 1      # common-mode rank


# ─────────────────────────────────────────────────────────────────────────────
# The Stage-1 runner: PROCEED (no HALT)
# ─────────────────────────────────────────────────────────────────────────────
def test_bedrock_validate_on_known_proceeds():
    """The full Stage-1 bedrock runner bins PROCEED (all HALT gates clear)."""
    out = bedrock_validate_on_known()
    assert out["status"] == "PROCEED", out.get("halt_reasons")
    assert out["S3"]["differential_multiplicity"] == 2
    assert out["S4"]["differential_multiplicity"] == 3
    assert not out["distinctness"]["collapse_detected"]


# ═════════════════════════════════════════════════════════════════════════════
# STAGE 2 — the SHOWN port->grade embedding (phase-space-coordinate-check)
# ═════════════════════════════════════════════════════════════════════════════
def test_port_to_realspace_embedding_separates_scalar_from_vector():
    """The SHOWN map: COMMON MODE (+1) carries the SCALAR grade (port-sum) with
    ZERO real-space vector; the DIFFERENTIAL (-1) modes carry ZERO scalar but a
    nonzero real-space VECTOR. Both nets are force-balanced (bond sum = 0)."""
    from ave.solvers.node_scattering_multiplicity import port_to_realspace_embedding

    for net, deg in ((build_srs_net(L=2), 3), (build_diamond_net(L=4), 4)):
        emb = port_to_realspace_embedding(net)
        # force-balanced node: bond directions sum to zero
        assert emb["bond_direction_sum_max"] < 1e-9
        # common mode = pure scalar (sqrt(degree)), no real-space vector
        assert abs(emb["common_mode_scalar_content_mean"] - np.sqrt(deg)) < 1e-9
        assert emb["common_mode_realspace_vector_norm_mean"] < 1e-9
        # differential = zero scalar, nonzero real-space vector
        assert emb["differential_scalar_content_mean"] < 1e-9
        assert emb["differential_realspace_vector_norm_mean"] > 0.5


# ═════════════════════════════════════════════════════════════════════════════
# STAGE 2 — the Fork-A verdict = REFUTE-R3 (pinned pre-registered negative)
# ═════════════════════════════════════════════════════════════════════════════
def test_fork_a_verdict_is_refute_r3():
    """The Fork-A test bins REFUTE-R3: the longitudinal A1 dilatation SCALAR lives
    in the COMMON-MODE (+1) sector, NOT the differential P_{-1} sector, so the
    pre-committed prediction (longitudinal confinement needs the diamond's 3rd
    DIFFERENTIAL mode) is refuted at the sector level. This is a PINNED scientific
    result (Rule 11 honest closure) -- NOT a relaxed bin. Re-binning to CHORD
    would require the longitudinal scalar to be a differential object, which the
    SHOWN embedding falsifies (differential scalar content ~1e-16)."""
    from ave.solvers.node_scattering_multiplicity import fork_a_test

    fa = fork_a_test()
    assert fa["verdict"] == "REFUTE-R3"
    sec = fa["sector_question_a"]
    assert sec["longitudinal_A1_scalar_in_common_mode_+1"] is True
    assert sec["longitudinal_A1_scalar_in_differential_P-1_srs"] is False
    assert sec["longitudinal_A1_scalar_in_differential_P-1_diamond"] is False
    # the multiplicity distinction is real (2 vs 3) but MOOT for longitudinal
    assert fa["multiplicity_question_b"]["srs_differential_multiplicity"] == 2
    assert fa["multiplicity_question_b"]["diamond_differential_multiplicity"] == 3


# ═════════════════════════════════════════════════════════════════════════════
# HONEST MARKER (Rule-12 scope correction, 2026-06-20, adversarial-auditor):
# the Fork-A verdict is a PROJECTOR TAUTOLOGY, not a discriminating test.
# ═════════════════════════════════════════════════════════════════════════════
def test_fork_a_verdict_is_invariant_under_bond_unit_scramble():
    """The Fork-A REFUTE-R3 verdict is INVARIANT under arbitrary bond_unit
    scrambling -- and THIS INVARIANCE IS PRECISELY WHY THE VERDICT IS A SECTOR-
    ALGEBRA FACT, NOT A DISCRIMINATING PHYSICAL TEST.

    The verdict logic in fork_a_test reads ONLY differential_scalar_content /
    common_mode_scalar_content, which are pure S_n = (2/n)J - I projector
    identities: the differential (-1) sector is orthogonal to the all-ones common
    mode so its scalar content is |a.ones| = 0 BY CONSTRUCTION; the common-mode
    (+1) scalar content is sqrt(degree) BY CONSTRUCTION. Neither reads bond_unit.
    Therefore scrambling every bond_unit vector -- which genuinely changes the
    geometry (it DESTROYS force-balance: bond_direction_sum goes 0 -> nonzero and
    common_mode_realspace_vector_norm goes ~0 -> nonzero) -- leaves the verdict-
    driving scalar quantities BIT-UNCHANGED, so the verdict could only ever come
    out R3, for ANY lattice, with NO physics in the decision.

    This is the permanent honest marker for the adversarial-auditor finding: R3 is
    TRUE (the isotropic/longitudinal A1 scalar IS the +1 common mode, orthogonal to
    the differential sector), but it is true BY DEFINITION, not because a test
    discriminated it. Fork-A was MISCAST -- it presupposed longitudinal confinement
    lives in the differential sector; the algebra shows it does not. See the
    result-doc Sec.2/Sec.5 Rule-12 corrections.
    """
    from ave.solvers.node_scattering_multiplicity import (
        fork_a_test,
        port_to_realspace_embedding,
    )

    # Baseline (unscrambled) verdict + verdict-driving quantities.
    fa0 = fork_a_test()
    base_diff_srs = fa0["embedding_srs"]["differential_scalar_content_mean"]
    base_diff_dia = fa0["embedding_diamond"]["differential_scalar_content_mean"]
    base_cm_srs = fa0["embedding_srs"]["common_mode_scalar_content_mean"]
    base_cm_dia = fa0["embedding_diamond"]["common_mode_scalar_content_mean"]
    assert fa0["verdict"] == "REFUTE-R3"

    def _scramble(net, seed):
        rng = np.random.default_rng(seed)
        for u in range(net.n_nodes):
            bu = net.bond_unit[u]
            for p in range(len(bu)):
                v = rng.standard_normal(3)
                bu[p] = v / (np.linalg.norm(v) + 1e-30)
        return net

    srs = _scramble(build_srs_net(L=2), seed=111)
    dia = _scramble(build_diamond_net(L=4), seed=222)
    emb_srs = port_to_realspace_embedding(srs)
    emb_dia = port_to_realspace_embedding(dia)

    # (i) The scramble GENUINELY changed the geometry: force-balance is destroyed,
    #     so the bond-direction sum and the common-mode real-space VECTOR are now
    #     nonzero (they WERE ~0 on the real, force-balanced nets).
    assert emb_srs["bond_direction_sum_mean"] > 1e-6
    assert emb_srs["common_mode_realspace_vector_norm_mean"] > 1e-6

    # (ii) Yet the verdict-driving SCALAR quantities are BIT-UNCHANGED -- they are
    #      projector identities that do NOT read bond_unit.
    assert emb_srs["differential_scalar_content_mean"] == base_diff_srs
    assert emb_dia["differential_scalar_content_mean"] == base_diff_dia
    assert emb_srs["common_mode_scalar_content_mean"] == base_cm_srs
    assert emb_dia["common_mode_scalar_content_mean"] == base_cm_dia

    # (iii) ... so the verdict is INVARIANT under the scramble (recompute the exact
    #       verdict logic from fork_a_test on the scrambled embeddings).
    tol = 1e-9
    lid_srs = emb_srs["differential_scalar_content_mean"] > tol
    lid_dia = emb_dia["differential_scalar_content_mean"] > tol
    licm = (
        emb_srs["common_mode_scalar_content_mean"] > tol
        and emb_dia["common_mode_scalar_content_mean"] > tol
    )
    scrambled_verdict = "REFUTE-R3" if (licm and not (lid_srs or lid_dia)) else "OTHER"
    assert scrambled_verdict == fa0["verdict"] == "REFUTE-R3", (
        "verdict must be scramble-invariant -- it is a projector tautology"
    )
