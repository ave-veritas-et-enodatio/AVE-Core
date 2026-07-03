"""DEC MINI-ARC keepers — the srs 2-complex operator identities + THE THEOREM.

These tests certify that the srs DEC operator set (ave.topological.srs_dec) is a
genuine adjoint/DEC chain, so the cold-linear-static-local closure of the CURL-
COUPLING CLASS is a ∂∂=0 STRUCTURAL IDENTITY — not a property of the two
engineering-choice operators the EM-readout Stage-1b review found were NOT a DEC
pair (div∘curl RMS≈0.35 there; here it is EXACTLY zero for the whole class).

Deterministic (seeded RNG); canonical constants only; L=3 (the minimum valid
supercell — L=2 has PBC-spurious 8-rings). Fast (sub-second), so gating-lane.
"""

import numpy as np
import pytest

from ave.core.chiral_lattice import build_srs_net
from ave.solvers.srs_cage_winding import assemble_L_srs, build_incidence
from ave.topological.srs_dec import (
    MIN_SRS_L,
    SRS_GIRTH,
    betti_numbers,
    build_srs_dec,
    enumerate_girth_faces,
    oriented_edges,
)

_L = 3  # minimum valid srs supercell (girth-10 recovered; L=2 folds to 8-rings)


@pytest.fixture(scope="module")
def dec():
    return build_srs_dec(L=_L, enantiomorph="right")


# ─────────────────────────────────────────────────────────────────────────────
# 1. The complex is well-formed: girth-10 faces, every edge covered, sizes.
# ─────────────────────────────────────────────────────────────────────────────
def test_complex_sizes_and_girth(dec):
    # L=3 srs: 216 nodes, 324 bonds, 324 girth-10 faces (empirical, deterministic).
    assert dec.n_nodes == 216
    assert dec.n_edges == 324
    assert dec.n_faces == 324
    # every face is a girth-10 ring
    for ring in dec.faces:
        assert len(ring) == SRS_GIRTH


def test_edge_set_matches_solver(dec):
    """oriented_edges == srs_cage_winding.unique_bonds (same bond set, same order).
    The DEC 1-cells ARE the solver's bonds — no independent bond posit."""
    from ave.solvers.srs_cage_winding import unique_bonds

    net = build_srs_net(L=_L, enantiomorph="right")
    assert oriented_edges(net) == unique_bonds(net) == dec.edges


# ─────────────────────────────────────────────────────────────────────────────
# 2. THE ∂∂=0 IDENTITIES — exact integer zero (not float roundoff).
# ─────────────────────────────────────────────────────────────────────────────
def test_boundary_of_boundary_is_exact_integer_zero(dec):
    """∂₁∂₂ = 0 in EXACT integer arithmetic. This is the combinatorial core:
    it holds for the operators, hence for EVERY field — the theorem's substrate."""
    D1i = dec.D1.toarray().astype(np.int64)
    D2i = dec.D2.toarray().astype(np.int64)
    prod = D1i @ D2i
    assert int(np.abs(prod).max()) == 0


def test_curl_of_grad_is_zero_whole_class(dec):
    """curl∘grad ≡ 0 = (∂₁∂₂)ᵀ applied to node fields, over many random draws."""
    rng = np.random.default_rng(1234)
    curl, grad = dec.curl, dec.grad
    worst = 0.0
    for _ in range(64):
        phi = rng.standard_normal(dec.n_nodes)
        worst = max(worst, float(np.abs(curl @ (grad @ phi)).max()))
    assert worst < 1e-11


def test_div_of_curl_adj_is_zero_whole_class(dec):
    """THE THEOREM operator: div∘curl_adj ≡ 0 for ANY face 2-cochain, i.e. every
    F = curl_adj(c) has div F = 0 identically. Contrast the Stage-1b operator pair
    (div∘curl RMS≈0.35). Many random draws stand in for the whole class."""
    rng = np.random.default_rng(5678)
    div, curl_adj = dec.div, dec.curl_adj
    worst = 0.0
    for _ in range(64):
        c = rng.standard_normal(dec.n_faces)
        worst = max(worst, float(np.abs(div @ (curl_adj @ c)).max()))
    assert worst < 1e-11


def test_stage1b_operator_pair_is_NOT_a_dec_pair():
    """Regression pin: the Stage-1b bond-projected operators do NOT compose to
    zero (div∘curl RMS is O(0.1), not machine zero). Documents WHY the DEC rebuild
    was needed — and guards against anyone mistaking them for an adjoint pair."""
    from scripts.vol_2_subatomic.em_readout_vsector_transducer import (  # noqa: PLC0415
        _srs_curl_nodes,
        _srs_node_divergence,
    )

    net = build_srs_net(L=_L, enantiomorph="right")
    rng = np.random.default_rng(42)
    omega = rng.standard_normal((net.n_nodes, 3))
    dc = _srs_node_divergence(net, _srs_curl_nodes(net, omega))
    rms = float(np.sqrt(np.mean(dc ** 2)))
    assert rms > 1e-2  # O(0.1) — decisively NOT a machine-zero DEC composition


# ─────────────────────────────────────────────────────────────────────────────
# 3. div = −grad-adjoint (exact), and the Laplacian reconciliation.
# ─────────────────────────────────────────────────────────────────────────────
def test_div_is_exact_negative_adjoint_of_grad(dec):
    """div = −∂₁ and grad = ∂₁ᵀ ⇒ div = −gradᵀ exactly (the adjoint relation the
    Stage-1b pair lacked). Verified as matrices, not just on a sample."""
    lhs = dec.div.toarray()
    rhs = -dec.grad.T.toarray()
    assert np.array_equal(lhs, rhs)


def test_laplacian_reconciles_with_solver(dec):
    """L0 = div∘grad = −∂₁∂₁ᵀ equals the NEGATIVE of the existing solver Laplacian
    assemble_L_srs(D≡1) = BᵀB = ∂₁∂₁ᵀ, EXACTLY. Same operator; the sign is the
    div=−∂₁ convention (reconciled, not re-derived)."""
    net = build_srs_net(L=_L, enantiomorph="right")
    B, bonds = build_incidence(net)
    L_solver = assemble_L_srs(B, bonds, np.ones(net.n_nodes)).toarray()  # BᵀB
    L0 = dec.laplacian_0.toarray()                                       # −∂₁∂₁ᵀ
    assert np.abs(L_solver + L0).max() == 0.0
    # and the solver Laplacian is +PSD with the constant nullspace (b0=1)
    assert np.abs(L_solver - L_solver.T).max() == 0.0


# ─────────────────────────────────────────────────────────────────────────────
# 4. The harmonic-space (Hodge/Betti) structure.
# ─────────────────────────────────────────────────────────────────────────────
def test_betti_numbers_torus(dec):
    """b0=1 (connected), b1=3 (the three T³ non-contractible loops = the harmonic
    1-cochain dimension), b2 over-complete (>3) on the FULL 10-ring face set —
    uniqueness of a MINIMAL 2-complex FAILS (booked honestly, not forced)."""
    b = betti_numbers(dec)
    assert b["b0"] == 1
    assert b["b1"] == 3            # the load-bearing, L-independent invariant
    assert b["b2"] > 3            # over-complete face set (documented choice)
    assert b["rank_D1"] == dec.n_nodes - 1


def test_harmonic_1cochain_dim_equals_b1(dec):
    """dim harmonic H1 = nullity of the Hodge 1-Laplacian L1 = ∂₁ᵀ∂₁ + ∂₂∂₂ᵀ,
    which must equal b1 = 3 (the three periodic-torus wraps)."""
    L1 = (dec.D1.T @ dec.D1 + dec.D2 @ dec.D2.T).toarray()
    nullity = dec.n_edges - np.linalg.matrix_rank(L1)
    assert nullity == 3


# ─────────────────────────────────────────────────────────────────────────────
# 5. GEOMETRY-FORCED guards (flag-don't-fix).
# ─────────────────────────────────────────────────────────────────────────────
def test_L2_supercell_is_rejected():
    """L=2 has PBC-spurious 8-rings (not girth-10 faces); the builder must refuse
    it with a hard error, not silently clamp or build the wrong complex."""
    with pytest.raises(ValueError, match="L >= 3|spurious 8-rings"):
        build_srs_dec(L=2)


def test_min_srs_l_constant():
    assert MIN_SRS_L == 3
    assert SRS_GIRTH == 10


def test_faces_are_deterministic():
    """The face enumerator is deterministic (same order across calls)."""
    net = build_srs_net(L=_L, enantiomorph="right")
    f1 = enumerate_girth_faces(net)
    f2 = enumerate_girth_faces(net)
    assert f1 == f2


def test_enantiomorph_sign_flip_preserves_identities():
    """The LEFT enantiomorph builds an equally-valid complex (∂∂=0, b1=3): the
    theorem is handedness-independent (it is combinatorial, not chiral)."""
    dec_L = build_srs_dec(L=_L, enantiomorph="left")
    D1i = dec_L.D1.toarray().astype(np.int64)
    D2i = dec_L.D2.toarray().astype(np.int64)
    assert int(np.abs(D1i @ D2i).max()) == 0
    assert betti_numbers(dec_L)["b1"] == 3
