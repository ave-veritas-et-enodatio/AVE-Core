"""CI adjoint-consistency + ∂∂=0 gate over the registered operator sets.

ENGINE-HARDENING ARC item 1 (`_orchestration/2026-07-04_engine-upgrade-program.md`
§1). Parameterized over `ave.topological.operator_registry.OPERATOR_SETS`: every
discrete operator set a LIVE solver may drive a verdict on must be a genuine
adjoint pair (`div = adjoint_sign · gradᵀ`) and, where it carries a 2-complex,
satisfy the ∂∂ = 0 composition identity — to the precision the set declares
(exact-integer for the pure-incidence DEC set; machine for the float
permutation-difference sets).

This is the standing generalization of the fix the DEC theorem made for the
curl-class: the retired Stage-1b `_srs_curl_nodes`/`_srs_node_divergence` pair
was NON-adjoint (div∘curl RMS ≈ 0.35). Had this gate existed, an attempt to
register + drive a verdict on that pair would fail here, not at post-merge review.

Deterministic; canonical constants only; sub-second (small test instances).
Gating-lane (not engine_sim).
"""

import importlib

import numpy as np
import pytest

from ave.topological.operator_registry import (
    OPERATOR_SETS,
    SCOPE_TAGGED_HEURISTICS,
    _adjoint_residual,
    _dd_residual,
    registered_names,
)

_SETS_BY_NAME = {s.name: s for s in OPERATOR_SETS}
_IDS = list(_SETS_BY_NAME)


@pytest.fixture(scope="module")
def _built():
    """Assemble every registered set once (small test instances)."""
    return {s.name: s.build() for s in OPERATOR_SETS}


# ─────────────────────────────────────────────────────────────────────────────
# Registry sanity
# ─────────────────────────────────────────────────────────────────────────────
def test_registry_nonempty_and_named():
    assert len(OPERATOR_SETS) >= 4, "at least the 4 canonical sets must be registered"
    names = registered_names()
    assert len(names) == len(set(names)), "operator-set names must be unique"
    assert {"srs_dec", "srs_incidence", "diamond_native_cage", "gw_native"} <= set(names)


def test_carriers_are_declared_vocabulary():
    allowed = {"srs-z3", "diamond-z4", "cartesian-reference", "k-space"}
    for s in OPERATOR_SETS:
        assert s.carrier in allowed, f"{s.name}: undeclared carrier {s.carrier!r}"
        assert s.adjoint_sign in (+1, -1), f"{s.name}: adjoint_sign must be ±1"
        assert s.exactness in ("exact_integer", "machine")


# ─────────────────────────────────────────────────────────────────────────────
# THE adjoint-consistency check (div = adjoint_sign · gradᵀ) — parameterized
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("name", _IDS)
def test_adjoint_consistency(name, _built):
    s = _SETS_BY_NAME[name]
    if not s.adjoint_pair:
        pytest.skip(f"{name}: not an adjoint pair by declaration")
    ops = _built[name]
    assert "grad" in ops and "div" in ops, f"{name}: adjoint set must build grad + div"
    res = _adjoint_residual(ops["grad"], ops["div"], s.adjoint_sign)
    tol = s.tolerance()
    assert res <= tol, (
        f"{name} (carrier={s.carrier}): div ≠ {s.adjoint_sign:+d}·gradᵀ — "
        f"‖div − sign·gradᵀ‖={res:.3e} > tol={tol:.0e}. "
        f"A non-adjoint operator pair (the Stage-1b failure class) driving a verdict."
    )


# ─────────────────────────────────────────────────────────────────────────────
# THE ∂∂ = 0 check (curl∘grad = 0, div∘curl_adj = 0) — parameterized
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("name", _IDS)
def test_dd_zero(name, _built):
    s = _SETS_BY_NAME[name]
    if not s.dd_zero:
        pytest.skip(f"{name}: no 2-complex ∂∂ composition registered")
    ops = _built[name]
    tol = s.tolerance()
    # div∘curl_adj = −∂₁∂₂ (the curl-class charge-neutrality THEOREM's operator)
    res = _dd_residual(ops["dd_compose"])
    assert res <= tol, f"{name}: div∘curl_adj ≠ 0 — ‖·‖={res:.3e} > tol={tol:.0e}"
    # curl∘grad = ∂₂ᵀ∂₁ᵀ = (∂₁∂₂)ᵀ (the transpose identity)
    if "dd_compose_2" in ops:
        res2 = _dd_residual(ops["dd_compose_2"])
        assert res2 <= tol, f"{name}: curl∘grad ≠ 0 — ‖·‖={res2:.3e} > tol={tol:.0e}"


def test_srs_dec_dd_is_exact_integer_zero(_built):
    """The DEC set's ∂∂ must be EXACTLY integer zero (not a machine near-zero) —
    the property that makes the curl-class charge-neutrality a THEOREM, not a fit."""
    ops = _built["srs_dec"]
    dd = ops["dd_compose"]
    dense = dd.toarray() if hasattr(dd, "toarray") else np.asarray(dd)
    assert np.count_nonzero(dense) == 0, "div∘curl_adj must be exactly zero everywhere"
    # and its dtype path must be integer-clean (values are exact ±1 incidence products)
    assert np.array_equal(dense, np.round(dense)), "DEC ∂∂ entries must be exact integers"


# ─────────────────────────────────────────────────────────────────────────────
# Reconciliation: the srs solver Laplacian == the DEC scalar Laplacian (−L0)
# ─────────────────────────────────────────────────────────────────────────────
def test_srs_incidence_reconciles_to_dec_laplacian():
    """L_srs = BᵀB must equal −L0 = ∂₁∂₁ᵀ EXACTLY (the srs_dec.py:99-106 claim)."""
    from ave.core.chiral_lattice import build_srs_net
    from ave.solvers.srs_cage_winding import assemble_L_srs, build_incidence
    from ave.topological.srs_dec import build_srs_dec

    net = build_srs_net(L=3)
    B, bonds = build_incidence(net)
    L_srs = assemble_L_srs(B, bonds, np.ones(net.n_nodes)).toarray()

    dec = build_srs_dec(L=3)
    neg_L0 = (-dec.laplacian_0).toarray()  # −L0 = ∂₁∂₁ᵀ

    # both are node×node; same bond set + orientation ⇒ exact match.
    assert L_srs.shape == neg_L0.shape
    assert np.allclose(L_srs, neg_L0, atol=1e-12), (
        f"L_srs ≠ −L0: max diff {np.max(np.abs(L_srs - neg_L0)):.3e} " "(the DEC↔solver reconciliation is BROKEN)"
    )


# ─────────────────────────────────────────────────────────────────────────────
# Provenance guard: no LIVE src/ave/ solver may import a scope-tagged non-adjoint
# heuristic (the operators explicitly excluded from the registry).
# ─────────────────────────────────────────────────────────────────────────────
def test_scope_tagged_heuristics_not_imported_by_live_ave_solvers():
    """The retired non-adjoint operators (`_srs_curl_nodes`, `_srs_node_divergence`)
    live in src/scripts/ (drivers), NOT src/ave/. Assert no src/ave/ module defines
    or imports them — so no library solver can drive a verdict on the failed pair."""
    import pathlib

    ave_root = pathlib.Path(__file__).resolve().parents[1] / "ave"
    assert ave_root.is_dir(), f"ave source root not found at {ave_root}"

    banned = ("_srs_curl_nodes", "_srs_node_divergence")
    offenders = []
    for py in ave_root.rglob("*.py"):
        text = py.read_text()
        for b in banned:
            # a real def/import (not a comment/docstring mention). The DEC-alternative
            # pointer in operator_registry mentions the NAMES in strings — allowed;
            # a def/import is not.
            if (f"def {b}" in text) or (f"import {b}" in text) or (f", {b}" in text and "from " in text):
                offenders.append(f"{b}@{py.relative_to(ave_root)}")
    assert not offenders, (
        "a live src/ave/ solver defines/imports a scope-tagged non-adjoint heuristic: "
        f"{offenders}. These must stay in src/scripts/ (retired instruments)."
    )


def test_scope_tagged_heuristics_documented():
    """Every scope-tagged heuristic must record a DEC-alternative pointer."""
    assert SCOPE_TAGGED_HEURISTICS, "the scope-tagged inventory must not be empty"
    for name, meta in SCOPE_TAGGED_HEURISTICS.items():
        for key in ("site", "why_not_registered", "dec_alternative", "status"):
            assert key in meta and meta[key], f"{name}: missing {key}"


# ─────────────────────────────────────────────────────────────────────────────
# The registered modules actually import (the registry points at real code).
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("name", _IDS)
def test_registered_module_importable(name):
    s = _SETS_BY_NAME[name]
    mod = importlib.import_module(s.module)
    assert mod is not None
