#!/usr/bin/env python3
"""The PRE-STRESSED srs ELASTIC-TENSOR arc — small-signal C_ij about a PRE-STRESSED DC Q-point.

[SAME-TENSOR-POINT] beyond-model TEST 1 of 2 — the initial/residual PRE-STRESS contribution.
Geometry-change (test 2) is HELD FIXED here (out of scope, the follow-on arc).

Prereg (FROZEN): research/2026-07-04_prestress-tensor_prereg_FROZEN.md (committed 6dba078e).

SKELETON — sections filled one commit at a time (incremental-write discipline).

═══════════════════════════════════════════════════════════════════════════════
THE SEAM THIS OPENS  (PR #521 § MODEL SCOPE, verbatim)
═══════════════════════════════════════════════════════════════════════════════
#521 closed [SAME-TENSOR-POINT] MODEL-BOUNDED: the saturated small-signal tensor is the cold tensor
at rho_eff, because Born-Huang (k_a,k_s)->C_ij is homogeneous degree-1 (overall S cancels in ratios).
Its MODEL SCOPE names two OMITTED, OPEN contributions a real DC-biased lattice carries:
  (a) initial/residual PRE-STRESS (bias pre-loads the bonds -> nonzero reference stress);
  (b) bias-induced GEOMETRY change (node/bond relaxation off the cold geometry).
THIS DRIVER computes (a) ONLY, at FIXED geometry. (b) is test 2 of 2.

The pre-stress term is NOT spring-softening: it adds a NEW transverse "string-tension" force constant
(T/l)(I - d^d^) per bond, T=Phi'(A) the integrated bond tension. That term does NOT scale as the
overall S factor, so it CAN break the degree-1 homogeneity that made #521 hold. That is why the test
is informative.

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (see prereg §1 — stated before any standard term)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : translational-u (Cauchy) sector of chiral srs-z3, PRE-STRESSED bond tensor.
           BOTH k_a, k_s are translational-u/CAPACITIVE (518 verbatim). Cosserat = STAGE 2.
  MODE   : SMALL-SIGNAL long-wave about a PRE-STRESSED DC Q-point (reference bond tension
           T=Phi'(A) != 0; cold ref had Phi'(0)=0 -- the separating axis from #521).
  REGIME : quasi-static about a STATIC DC bias. Op14 ON. PHASE-STATE = saturated S<1 WITH bias tension.
  DC/AC  : A is a STATIC DC bias (R2 varactor, node-up:118,:40,:145) -> NO <sin^2>=1/2 factor;
           reference tension = Phi'(A) at the static bias, factor 1 (derived, not hand-set).
  COORDS : operating-point knob (A_axial,A_shear) phase-space/reactance; tensor readout real-space.
           A46-clean on both.
  CLASS  : CONSISTENCY/MANIFESTATION. nu/Zener/(K/G) ratios (alpha-clean). EMERGENCE FORBIDDEN for
           any value: 2/7, 9.7734, 0.99479 are ALL visible targets -- NO tuning toward any.

THE DERIVED TENSION (prereg §2, sympy-verified):
  Phi''(a) = k0*S(a) = k0*sqrt(1-a^2)   (Ax4 kernel AS DIFFERENTIAL STIFFNESS)
  T(A) = Phi'(A) = INT_0^A k0*sqrt(1-a^2) da = k0*( A*sqrt(1-A^2) + arcsin A ) / 2,  Phi'(0)=0.
  Phi'(A) -> k0*pi/4 as A->1 (FINITE tension at the yield wall; tangent stiffness -> 0).

THE INITIAL-STRESS FORM (prereg §3, Born-Huang/Wallace, validated PC2):
  Phi_bond = Phi''*(d^d^) + (T/l)*(I - d^d^),  l = per-bond |d| (read from geometry).
  The (T/l)(I-d^d^) transverse "string tension" term IS the pre-stress physics at lattice level.

Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/prestress_elastic_tensor.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

# REUSE the cold arc's PROVEN Born-Huang extraction pieces unmodified where possible
# (identical pipeline is what licenses the pre-stressed number).
from scripts.vol_1_foundations.srs_elastic_tensor import (  # noqa: E402
    _cubic_gamma_row,
    moduli_from_Cij,
    simple_cubic_ref,
    srs_primitive,
)

from ave.axioms.scale_invariant import saturation_factor  # noqa: E402
from ave.core.constants import ALPHA, NU_VAC  # noqa: E402


# ---------------------------------------------------------------------------
# CANON ANCHORS (imported / read-off -- NOT tuned)
# ---------------------------------------------------------------------------
RHO_COLD = 1.0
RHO_STAR_IMPORTED = 9.7734          # cold nu=2/7 <=> K=2G locus, GR-imported (read-off only)
NU_2_7 = float(NU_VAC)              # the visible-target Poisson ratio (= 2/7)
A_CORE_SQRT_ALPHA = float(np.sqrt(ALPHA))   # A1 mass-core operating point (def-vyvsn1)
A_WALL_518_CROSSING = 0.99479       # #518 shear-loads crossing amplitude (VISIBLE TARGET, read-off)


# ===========================================================================
# THE DERIVED BOND TENSION (prereg §2) -- Phi'(A), sympy-verified
# ===========================================================================
def bond_tension(A: float | np.ndarray, k0: float = 1.0) -> np.ndarray:
    """Integrated bond tension T(A)=Phi'(A)=k0*(A*sqrt(1-A^2)+arcsin A)/2, Phi'(0)=0.

    From Phi''(a)=k0*sqrt(1-a^2) (Ax4 kernel as DIFFERENTIAL stiffness) by direct integration
    (prereg §2, symbolically verified). No hand-set factor; the DC-bias convention (node-up:118)
    sets the time-average factor to 1. Phi'(A)->k0*pi/4 as A->1 (finite tension at yield).
    """
    Aa = np.asarray(A, dtype=float)
    # arcsin domain guard (A in [0,1]); the sweep never exceeds 1 (sub-yield to the wall)
    Aa = np.clip(Aa, 0.0, 1.0)
    return k0 * (Aa * np.sqrt(np.clip(1.0 - Aa ** 2, 0.0, 1.0)) + np.arcsin(Aa)) / 2.0


# ===========================================================================
# PLACEHOLDERS -- filled in subsequent commits (incremental-write discipline)
# ===========================================================================
def prestress_christoffel(*args, **kwargs):  # noqa: D401
    """[filled next commit] internal-strain-relaxed acoustic Christoffel WITH pre-stress term."""
    raise NotImplementedError


def extract_prestress_Cij(*args, **kwargs):  # noqa: D401
    """[filled next commit] fit cubic (C11,C12,C44) on the PRE-STRESSED acoustic tensor."""
    raise NotImplementedError


def run_positive_controls(*args, **kwargs):  # noqa: D401
    """[filled next commit] PC1 zero-bias recovery + PC2 analytic stressed-lattice + PC3 homogeneity."""
    raise NotImplementedError


def residual_node_forces(*args, **kwargs):  # noqa: D401
    """[filled next commit] net force at each node from the bias tensions at COLD geometry.

    The GEOMETRY-COUPLED discriminator (prereg §6 branch ii, §9): reading A (self-balancing) vs
    reading B (unbalanced -> geometry-coupled). Nonzero residual above floor => [GEOMETRY-COUPLED].
    """
    raise NotImplementedError


def run_sweep(*args, **kwargs):  # noqa: D401
    """[filled next commit] both channel assignments, full A_wall ladder, Delta-nu map readout."""
    raise NotImplementedError


def main():  # noqa: D401
    """[filled last commit] validate-on-known HALT gate, residual-force check, sweep, bin verdict."""
    print("SKELETON -- sections fill in subsequent commits.")


if __name__ == "__main__":
    main()
