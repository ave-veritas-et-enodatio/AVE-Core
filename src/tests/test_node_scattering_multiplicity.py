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
    polarizations (test_l1_photon.py:243-268; engine-acceptance-suite.md:178)."""
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
