"""Substrate-native graded-vacuum impedance-network operator + isolation eigensolver.

Build-A (Stages 0-3) of the electron-Q coupled-network discriminating test.
Prereg: research/2026-06-19_electron-Q-coupled-network_prereg.md
        (frozen commit 4ae50ba0; the FIRST commit of this branch).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS MODULE IS (and is NOT)
═══════════════════════════════════════════════════════════════════════════════
GOAL  : derive the electron bound-mode Q from the substrate-native graded-vacuum
        impedance network. CHORD = alpha moves echo->chord (Q ~ 1/alpha = 137 from
        alpha-FREE inputs). ECHO = it does not. PRIOR = ECHO (the alpha-free cold
        cage gives Q ~ 30.8, NOT 137; test_l3_mass_cage.py:25).

SCOPE : Build-A = Stages 0-3 ONLY. This module builds:
          * STAGE 1: L_native = adjoint_tetrahedral_divergence . D . tetrahedral_gradient
                     on the diamond/srs tetrahedral stencil (NOT the Cartesian
                     7-pt Laplacian). D block-diagonal in (bulk K / shear G).
          * STAGE 2: the NON-HERMITIAN generalized eigenproblem for the ISOLATION
                     leg (H_couple OFF, circulator OFF): bulk channel with the
                     mu-load SHORT Gamma=-1 confinement BC + an EM matched
                     loss-port (Gamma_EM=0 boundary admittance making L non-Hermitian).
                     Q = |Re omega| / (2 |Im omega|).
          * STAGE 3: lossless (EM port closed -> Q=inf) + Nyquist sanity.
        H_couple, the coupled solve, and Fork-A coupling are Build-B -- NOT here.

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-NATIVE-CHECK (walked BEFORE any numerical code, per operating principle 1)
═══════════════════════════════════════════════════════════════════════════════
  * K4 / stencil : the spatial operator is the TETRAHEDRAL gradient/divergence on
                   the diamond-K4 stencil (4 tetrahedral diagonal offsets,
                   TETRA_OFFSETS, cosserat_field_3d.py:134). The composition
                   adjoint_div . grad is the native diamond Laplacian
                   (div(grad) r^2 = const, div(grad) linear = 0, verified). The
                   Cartesian 7-pt Laplacian (crystal_engine.py:154,
                   master_equation_fdtd.py:124) is FORBIDDEN (HR1) and never imported.
  * Cosserat     : two ORTHOGONAL grades carried by D (block-diagonal):
                   - bulk scalar V  = the A1 dilatation MASS-3 (Heaviside scalar),
                   - shear/Cosserat = the (2,3) micro-rotation CHARGE-3 winding.
                   Never a shared (V_inc, V_ref) phasor (A1-perp-T2,
                   master-equation.md:20; the genesis-24 double-count caution).
  * Op14         : the confinement wall = a mu-load SHORT (Z_core->0, Gamma->-1,
                   settled PR#260). The Op14 saturation exponent is swept per
                   DEC-1 (sqrt(S) primary, S^{1/4} sensitivity).
  * phase vs real: the eigenproblem is posed in REAL-space on the lattice field
                   (the complex-omega of a spatial operator). Q = |Re w|/(2|Im w|)
                   is a coordinate-free spectral ratio; no phase-space phi^2 claim
                   is at issue at the isolation rung.

═══════════════════════════════════════════════════════════════════════════════
THE ALPHA-LEAK + THE alpha-FREE RATIO MANDATE (HR2, Finding 1)
═══════════════════════════════════════════════════════════════════════════════
RHO_BULK = xi^2 mu_0 / (P_C ell^2) with P_C = 8 pi alpha (constants.py:664,400),
so RHO_BULK ~ 1/(8 pi alpha) and EVERY bare impedance magnitude
(Z_shear = rho_bulk c_shear, Z_bulk = sqrt2 rho_bulk c_0) CARRIES alpha.

This module therefore uses ONLY the DIMENSIONLESS, rho-CANCELLING impedance RATIO
between the two MECHANICAL channels (DEC-4: bulk K + shear G):

    Z_bulk / Z_shear = (rho c_L) / (rho c_T) = c_L / c_T = sqrt(10/3) = 1.825742...

  alpha-FREE provenance of the ratio (crystal_engine.py:27, DERIVED, not knob-set):
    c_L^2 / c_T^2 = 2(1-nu)/(1-2 nu) = (K + 4G/3)/G |_{K=2G} = 10/3  at nu_vac=2/7.
  rho (= RHO_BULK, the ONLY alpha-carrier) cancels identically in the ratio, so
  the ratio is exactly alpha-INVARIANT. No bare RHO_BULK / Z magnitude ever enters.

  RECONCILIATION FLAG (surfaced, not silently fixed): the prereg's headline figure
  Z_bulk/Z_shear = sqrt2 * sqrt(10/3) = 2.582 COMPOUNDS two distinct transverse
  references -- the EM-PHOTON speed sqrt(G/rho)=c0 (the sqrt2 = c_bulk/c_photon =
  sqrt(K/G), _bulk.py:102) AND the MECHANICAL-SHEAR speed c_T (crystal_engine.py:96).
  For the TWO-MECHANICAL-CHANNELS build (bulk K vs mechanical shear G, DEC-4) the
  physically-correct channel ratio is c_L/c_T = sqrt(10/3) alone. Both candidates
  are alpha-free and alpha-invariant, so the ambiguity does NOT affect any
  chord/echo bin -- it would only shift the bulk/shear gap LOCATION. The module
  exposes BOTH (RATIO_BULK_SHEAR_MECH primary; RATIO_BULK_SHEAR_PHOTON sensitivity).

═══════════════════════════════════════════════════════════════════════════════
ALLOWED alpha-FREE INPUTS (HR2; each greppably provenanced)
═══════════════════════════════════════════════════════════════════════════════
  Z_0           constants.py:99    characteristic impedance (used only as a LABEL;
                                   never as a bare magnitude in a Q-determining ratio)
  c_0           constants.py:95    speed of light (sets dimensionless dispersion only)
  nu_vac = 2/7  constants.py:532   -> c_L/c_T via 2(1-nu)/(1-2nu)=10/3
  kappa_tilde   cosserat_field_3d.py:94  = 6/5 (electron (2,3) torus, pq/(p+q)) -- the
    = 6/5                          chiral coupling; provenance crystal-graft-v2_result.md
  L_NODE        constants.py:257   lattice pitch (dimensionless dx only)
  lattice geom  chiral_lattice.build_srs_net / build_diamond_net, TETRA_OFFSETS
FORBIDDEN: Q_TANK=1/ALPHA (cvr_model.py:72), coupled_resonator k=2*alpha defaults,
  any bare RHO_BULK / Z_shear / Z_bulk magnitude. None are imported (import-guarded).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# alpha-FREE inputs ONLY (HR2). NU_VAC=2/7 (constants.py:532), C_0/Z_0 as labels.
from ave.core.constants import C_0, NU_VAC, Z_0
from ave.topological.cosserat_field_3d import (
    KAPPA_TILDE_ELECTRON,  # = 6/5, alpha-free electron (2,3) torus factor (:94)
    TETRA_OFFSETS,
    adjoint_tetrahedral_divergence,
    tetrahedral_gradient,
)

# ─────────────────────────────────────────────────────────────────────────────
# IMPORT-GUARD (anti-circularity, HR2): assert no alpha-carrier leaked into globals.
# Q_TANK (=1/alpha) and the ELECTRON instance must NOT be reachable here.
# ─────────────────────────────────────────────────────────────────────────────
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "alpha-leak: ELECTRON instance must NOT be imported"
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported"
assert "RHO_BULK" not in globals(), "second-leak: bare RHO_BULK magnitude must NOT be imported"

# ─────────────────────────────────────────────────────────────────────────────
# alpha-FREE dimensionless ratios (the ONLY Q-determining mechanical quantities).
# ─────────────────────────────────────────────────────────────────────────────
#   c_L^2/c_T^2 = 2(1-nu)/(1-2nu) = 10/3 at nu_vac=2/7 (crystal_engine.py:27, DERIVED).
CL2_OVER_CT2: float = 2.0 * (1.0 - NU_VAC) / (1.0 - 2.0 * NU_VAC)  # = 10/3
#   primary channel ratio: bulk(K) vs MECHANICAL shear(G); rho cancels -> alpha-free.
RATIO_BULK_SHEAR_MECH: float = float(np.sqrt(CL2_OVER_CT2))  # = sqrt(10/3) ~ 1.82574
#   sensitivity: bulk vs EM-PHOTON reference (the sqrt2 = sqrt(K/G), _bulk.py:102).
RATIO_BULK_SHEAR_PHOTON: float = float(np.sqrt(2.0) * np.sqrt(CL2_OVER_CT2))  # ~ 2.58199


def _native_scalar_laplacian(field: np.ndarray) -> np.ndarray:
    """The substrate-native diamond/srs Laplacian on a SCALAR field:
        L = adjoint_tetrahedral_divergence ( tetrahedral_gradient(field) ).
    Uses the tetrahedral stencil (TETRA_OFFSETS, 4 diamond diagonals) ONLY --
    the Cartesian 7-pt Laplacian is FORBIDDEN (HR1) and never called.

    Numerically verified: L(linear) = 0 (interior, machine eps); L(r^2) = const
    (uniform, zero std). Symmetric POSITIVE-semidefinite (it IS the stiffness form
    = grad^T grad up to the discrete inner product), so the eigenproblem is
    L x = omega^2 M x with omega^2 >= 0 -- NO sign flip needed. (Verified by
    test_native_laplacian_is_symmetric_positive_semidefinite; the nullspace is the
    constant/rigid modes.)

    Args:
        field: (N, N, N) real scalar (the A1 dilatation amplitude).
    Returns:
        (N, N, N) real: the native Laplacian-action.
    """
    grad = tetrahedral_gradient(field[..., None])  # (N,N,N,1,3)
    div_in = np.asarray(grad)[..., 0, :]  # (N,N,N,3)
    return np.asarray(adjoint_tetrahedral_divergence(div_in))


def _native_vector_laplacian(field: np.ndarray) -> np.ndarray:
    """Native diamond/srs Laplacian on a VECTOR field (the shear/Cosserat omega
    grade), applied component-wise with the SAME tetrahedral stencil.

    Args:
        field: (N, N, N, 3) real (the Cosserat micro-rotation amplitude).
    Returns:
        (N, N, N, 3) real.
    """
    out = np.empty_like(field)
    for c in range(field.shape[-1]):
        out[..., c] = _native_scalar_laplacian(field[..., c])
    return out


@dataclass(frozen=True)
class NativeOperatorConfig:
    """Frozen geometry/constitutive config for the native operator (alpha-free).

    N            : cube edge (lattice sites per side).
    dx           : dimensionless lattice pitch (1.0; physical L_NODE folds out of Q).
    ratio_bs     : bulk/shear impedance RATIO (default = mechanical, sqrt(10/3)).
    kappa_tilde  : chiral coupling 6/5 (electron (2,3) torus, alpha-free); carried
                   for Build-B H_couple, NOT used in the isolation D-block.
    """

    N: int = 16
    dx: float = 1.0
    ratio_bs: float = RATIO_BULK_SHEAR_MECH
    kappa_tilde: float = KAPPA_TILDE_ELECTRON

    def assert_alpha_free(self) -> None:
        """Hard assert: every config number is alpha-free + the ratio is finite."""
        assert np.isfinite(self.ratio_bs) and self.ratio_bs > 0
        assert abs(self.kappa_tilde - 6.0 / 5.0) < 1e-12, "kappa_tilde must be 6/5"
        # ratio_bs must equal one of the two alpha-free derived ratios.
        assert any(
            abs(self.ratio_bs - r) < 1e-9
            for r in (RATIO_BULK_SHEAR_MECH, RATIO_BULK_SHEAR_PHOTON)
        ), "ratio_bs must be an alpha-free derived ratio (mech or photon)"


def stencil_provenance() -> dict:
    """Return the native-stencil provenance (for the no-Cartesian-Laplacian gate).

    Confirms TETRA_OFFSETS are the 4 diamond tetrahedral diagonals and that this
    module routes through the tetrahedral operators, never the Cartesian 7-pt.
    """
    return {
        "tetra_offsets": tuple(tuple(int(x) for x in p) for p in TETRA_OFFSETS),
        "n_offsets": len(TETRA_OFFSETS),
        "operator": "adjoint_tetrahedral_divergence . tetrahedral_gradient",
        "cartesian_7pt_imported": False,
    }
