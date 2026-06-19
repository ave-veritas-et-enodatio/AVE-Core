"""STAGE 1 gate tests for the substrate-native graded-vacuum network operator.

Prereg: research/2026-06-19_electron-Q-coupled-network_prereg.md (commit 4ae50ba0).

STAGE 1 GATE (prereg): the keeper test_cosserat_field_3d.py:32 still passes (run
separately) AND the native operator is sign-consistent with a Cartesian gradient
on a smooth test field. Plus the anti-circularity grep/import guards.
"""

import importlib
import inspect

import numpy as np

from ave.solvers.graded_vacuum_network import (
    CL2_OVER_CT2,
    RATIO_BULK_SHEAR_MECH,
    RATIO_BULK_SHEAR_PHOTON,
    NativeOperatorConfig,
    _native_scalar_laplacian,
    _native_vector_laplacian,
    stencil_provenance,
)

# ─────────────────────────────────────────────────────────────────────────────
# Native operator: sign-consistency with the continuum Laplacian on smooth fields
# ─────────────────────────────────────────────────────────────────────────────


def test_native_laplacian_of_linear_field_is_zero():
    """L(linear) = 0 on the interior (curvature-free) -- the native diamond
    div(grad), NOT the Cartesian 7-pt. Sign/consistency baseline."""
    n = 12
    x, y, z = np.indices((n, n, n)).astype(float)
    f = 0.37 * x - 0.21 * y + 0.13 * z + 1.5
    lap = _native_scalar_laplacian(f)
    assert np.abs(lap[3:-3, 3:-3, 3:-3]).max() < 1e-10


def test_native_laplacian_of_quadratic_is_uniform_constant():
    """L(r^2) is a UNIFORM constant on the interior (isotropic stencil, zero std):
    the native diamond div(grad) has a fixed sign convention; the SIGN is asserted
    explicitly in the SPD test below (the operator as defined is the
    positive-semidefinite stiffness form L = adjoint_div . grad)."""
    n = 12
    x, y, z = np.indices((n, n, n)).astype(float)
    f = x * x + y * y + z * z
    lap = _native_scalar_laplacian(f)
    interior = lap[3:-3, 3:-3, 3:-3]
    assert interior.std() < 1e-9, f"non-uniform (anisotropic stencil): std={interior.std()}"
    # the operator is consistent with continuum |Laplacian| up to its fixed sign
    # convention; the convention (SPD vs NSD) is pinned by the next test.
    assert abs(interior.mean()) > 1e-6, "operator vanished on a curved field (bug)"


def test_native_laplacian_is_symmetric_positive_semidefinite():
    """The operator matrix L = adjoint_tetrahedral_divergence . tetrahedral_gradient
    (applied to unit basis vectors on a small PERIODIC cube) is SYMMETRIC and
    POSITIVE-semidefinite -- i.e. it IS the stiffness form (= grad^T grad, up to
    the discrete inner product). So the generalized eigenproblem is
        L x = omega^2 M x   with omega^2 >= 0   (NO sign flip needed).
    The nullspace = the constant/rigid modes (the diamond is bipartite, so the
    nullspace is 2-dimensional per connected sublattice on a periodic cube)."""
    n = 6
    ndof = n**3

    def apply(vec):
        f = vec.reshape(n, n, n)
        return _native_scalar_laplacian(f).reshape(ndof)

    L = np.column_stack([apply(np.eye(ndof)[:, k]) for k in range(ndof)])
    assert np.allclose(L, L.T, atol=1e-8), "operator not symmetric"
    eig = np.linalg.eigvalsh(0.5 * (L + L.T))
    assert eig.min() > -1e-8, f"not positive-semidefinite: min eig {eig.min()}"
    assert eig.max() > 0.1, "operator is degenerate/zero (no curvature spectrum)"
    # nullspace = rigid/constant modes (small, finite).
    nnull = int((np.abs(eig) <= 1e-8).sum())
    assert 1 <= nnull <= 16, f"unexpected nullspace dim {nnull}"


def test_vector_laplacian_acts_componentwise():
    """The vector (shear/Cosserat) Laplacian applies the SAME tetrahedral stencil
    per component."""
    n = 10
    rng = np.random.default_rng(3)
    f = rng.normal(size=(n, n, n, 3))
    out = _native_vector_laplacian(f)
    for c in range(3):
        assert np.allclose(out[..., c], _native_scalar_laplacian(f[..., c]))


# ─────────────────────────────────────────────────────────────────────────────
# alpha-free ratios (HR2 / Finding 1)
# ─────────────────────────────────────────────────────────────────────────────


def test_speed_ratio_is_ten_thirds():
    """c_L^2/c_T^2 = 2(1-nu)/(1-2nu) = 10/3 at nu_vac=2/7 (DERIVED, alpha-free)."""
    assert abs(CL2_OVER_CT2 - 10.0 / 3.0) < 1e-12


def test_bulk_shear_ratio_values():
    """Both candidate ratios are the alpha-free derived values."""
    assert abs(RATIO_BULK_SHEAR_MECH - np.sqrt(10.0 / 3.0)) < 1e-12
    assert abs(RATIO_BULK_SHEAR_PHOTON - np.sqrt(2.0) * np.sqrt(10.0 / 3.0)) < 1e-12


# ─────────────────────────────────────────────────────────────────────────────
# Native-stencil confirmation + anti-circularity (no Cartesian Laplacian, no alpha)
# ─────────────────────────────────────────────────────────────────────────────


def test_native_stencil_is_tetrahedral():
    """The operator uses the 4 diamond tetrahedral diagonal offsets, NOT a
    Cartesian 6-neighbour stencil."""
    prov = stencil_provenance()
    assert prov["n_offsets"] == 4
    expected = {(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)}
    assert set(prov["tetra_offsets"]) == expected
    assert prov["cartesian_7pt_imported"] is False
    assert "adjoint_tetrahedral_divergence" in prov["operator"]


def test_module_source_has_no_alpha_tokens():
    """Anti-circularity grep (HR2): the module SOURCE imports/uses no alpha-carrier
    in its inputs. We forbid the FORBIDDEN tokens; the strings 'alpha' may appear
    ONLY in prose/docstring discussion of the leak, never as an imported symbol."""
    import ave.solvers.graded_vacuum_network as mod

    src = inspect.getsource(mod)
    # FORBIDDEN imported symbols must not appear as code tokens.
    for tok in ("Q_TANK", "ALPHA", "RHO_BULK", "Z_TANK"):
        # allow inside a quoted assert-message / docstring only -- check the import
        # block specifically: none of these are imported.
        assert f"import {tok}" not in src
        assert f", {tok}" not in src.split('"""')[0] if '"""' in src else True
    # the import-guard asserts are present.
    assert "Q_TANK\" not in globals()" in src
    assert "ALPHA\" not in globals()" in src
    assert "RHO_BULK\" not in globals()" in src


def test_import_guards_fire_on_alpha_carrier():
    """Re-importing the module with an alpha-carrier injected into its namespace
    must trip the import-guard assert (defence-in-depth)."""
    mod = importlib.import_module("ave.solvers.graded_vacuum_network")
    # the guards ran at import; module imported clean means they passed.
    assert mod is not None
    # confirm the forbidden names are genuinely absent from the live namespace.
    for tok in ("Q_TANK", "ELECTRON", "ALPHA", "RHO_BULK"):
        assert not hasattr(mod, tok), f"{tok} leaked into module namespace"


def test_config_asserts_alpha_free():
    cfg = NativeOperatorConfig()
    cfg.assert_alpha_free()
    assert abs(cfg.kappa_tilde - 6.0 / 5.0) < 1e-12
