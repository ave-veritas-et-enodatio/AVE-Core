#!/usr/bin/env python3
"""The SATURATED srs ELASTIC-TENSOR arc — small-signal Cauchy C_ij about a DC Q-point.

Grant-fired 2026-07-04 ("sweep all regimes" / KEEP-BOTH "record and do both").
Prereg (FROZEN): research/2026-07-04_saturated-elastic-tensor_prereg_FROZEN.md.

SKELETON — sections filled one commit at a time (incremental-write discipline).

═══════════════════════════════════════════════════════════════════════════════
THE SEAM THIS CLOSES  (PR #518 §6 scope flag, verbatim)
═══════════════════════════════════════════════════════════════════════════════
The COLD arc (srs_elastic_tensor.py, MERGED) computed the Cauchy C_ij as a
one-parameter family in rho=k_a/k_s; nu_Hill=2/7 <=> K=2G only at cold rho*=9.7734.
PR #518 (matter_stiffening_rho.py, MERGED 6d2ecdf4) computed the SATURATED RATIO
rho_eff = rho_cold*(S_axial/S_shear) but NOT the tensor, and flagged (its section 6):
  "driving the saturated rho_eff to 9.77 is NOT proven to land the same nu=2/7/K=2G
   elastic tensor ... the saturated C_ij(rho_eff) would need to be recomputed from the
   saturated bond stiffnesses (a Born-Huang run on the saturated Phi_b)."
This driver does exactly that: Born-Huang on the SATURATED Phi_b, swept across the full
operating-point regime, BOTH channel assignments, with two-hand cross-validation.

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (see prereg — stated before any standard term)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : translational-u (Cauchy) sector of chiral srs-z3, on the SATURATED bond
           tensor Phi_b(A) = k_a(A_axial)*(d^d^) + k_s(A_shear)*(I-d^d^). BOTH k_a and
           k_s are translational-u/CAPACITIVE springs (axial vs shear of the SAME bond;
           518 verbatim) -- NOT the eps-vs-mu photon pair. Cosserat = STAGE 2, not invoked.
  MODE   : SMALL-SIGNAL long-wave. The saturated k(A) are the differential (tangent) bond
           stiffnesses at the DC bias point (varactor picture, CLAUDE.md:75, INVARIANT-S2).
  REGIME : quasi-static about a DC bias. Op14 saturation ON. PHASE-STATE = saturated, S<1
           (the cold arc was S=1, saturation OFF -- this is the separating axis).
  COORDS : operating-point knob (A_axial,A_shear) in phase-space/reactance (518 verbatim);
           tensor readout (w(k)->C_ij->nu,Zener,K/G) in real-space/spatial-Brillouin. Each
           measured in ITS OWN matching coordinate (A46-clean on both).
  CLASS  : CONSISTENCY/MANIFESTATION. nu/Zener/(K/G) are ratios (alpha-clean on the verdict
           path). EMERGENCE FORBIDDEN for any value: 2/7, 9.7734, 0.99479 are ALL visible
           targets -- NO tuning toward any of them (the frozen bins + ledger are the guard).

THE LOAD-BEARING PHYSICS (prereg 0.6, tested in VS2/VS3):
  Born-Huang C_ij is homogeneous DEGREE-1 in (k_a,k_s). So:
   - dimensionless RATIOS (nu, Zener, K/G) are degree-0 -> depend ONLY on
     rho_eff = k_a*S_axial/(k_s*S_shear) = rho_cold*(S_axial/S_shear). Overall S drops out.
     => saturated nu(rho_eff) map == cold nu(rho) map with rho->rho_eff (SAME-TENSOR-POINT).
   - absolute moduli (K,G,C_ij,speeds) are degree-1 -> scale by overall S (floppy near yield).
   - sign(K) is scale-invariant for S>0 -> stability boundary at rho_eff (unshifted by S).

Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/saturated_elastic_tensor.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

# The saturated arc REUSES the cold arc's PROVEN Born-Huang extraction unmodified
# (the load-bearing point: identical pipeline is what licenses the saturated number).
from scripts.vol_1_foundations.srs_elastic_tensor import (  # noqa: E402
    extract_cubic_Cij,
    moduli_from_Cij,
    srs_primitive,
)

from ave.axioms.scale_invariant import saturation_factor, shear_modulus_ratio  # noqa: E402
from ave.core.constants import ALPHA, NU_VAC  # noqa: E402


# ---------------------------------------------------------------------------
# CANON ANCHORS (imported / read-off — NOT tuned)   [FILLED NEXT COMMIT]
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# The saturated per-channel stiffness maps (canon-forced, from #518)   [NEXT]
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Saturated tensor at an operating point   [NEXT]
# ---------------------------------------------------------------------------


# ===========================================================================
# DRIVER   [NEXT]
# ===========================================================================
def main():
    raise NotImplementedError("skeleton — filled in subsequent commits")


if __name__ == "__main__":
    main()
