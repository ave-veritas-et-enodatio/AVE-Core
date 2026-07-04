"""Derive the end-to-end per-bond axial FORCE per loading path from the canonical
fixed-arc-length K4 microfoundation, and feed both arms through the MERGED #526
remap machinery (consumed, not reimplemented).

RESOLVES the OPEN SIGN FORK left by PR #526 (research/2026-07-04_prestress-tensor_result.md
:53-60,278-294,365-371): the sign of the end-to-end bond force, un-adjudicated there
(T>0 stretched-pair assumed vs canonical T<0 bowed-strut compression).

PREREG (FROZEN, committed BEFORE this driver):
  research/2026-07-04_bond-force-sign-rule_prereg_FROZEN.md

THE PHYSICS (from A^2+S^2=arc*^2, axiom-register.md:189, NOT the pair-potential analogy):
  arm (a) TRANSVERSE PLUCK (T2 response): chord clamped at ell, bow y driven ->
          the stretched arc pulls the ends together -> TENSION (T>0), 2nd-order in y.
  arm (b) AXIAL END-LOAD (A1 load): chord driven below ell, bow free to buckle ->
          the strut resists compression -> COMPRESSION (T<0), plateau P_c=k_b*ell/4.
  The two arms give OPPOSITE-sign forces. cap-vs-uncap in the #526 remap
  (k_shear_eff = S_shear + T/ell) depends on sign(T) ALONE.

ORCHESTRATOR RULING (prereg, verbatim): Reading (b) -- run BOTH magnitude laws
banded per arm (four tracks); the sign is the verdict, the magnitude is a bands
question. Neither law baked as "the" law.

Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/bond_force_sign_rule.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

# CONSUME the merged #526 remap machinery (do NOT reimplement).
from scripts.vol_1_foundations.prestress_elastic_tensor import (  # noqa: E402
    bond_tension,          # #526 Phi'(A) = k0(A sqrt(1-A^2)+arcsin A)/2, sympy-verified
    extract_prestress_Cij,  # the pre-stressed Born-Huang tensor (transverse (T/l)(I-P))
    _prestress_tensor_at,   # full pre-stressed tensor + moduli + rho'/rho_eff at (A_ax,A_sh)
)
from scripts.vol_1_foundations.srs_elastic_tensor import (  # noqa: E402
    extract_cubic_Cij,
    moduli_from_Cij,
    srs_primitive,
)
from ave.axioms.scale_invariant import saturation_factor  # noqa: E402
from ave.core.constants import ALPHA, NU_VAC  # noqa: E402


# ---------------------------------------------------------------------------
# CANON ANCHORS (imported / read-off -- NEVER tuned; anti-tune ledger row 10)
# ---------------------------------------------------------------------------
RHO_STAR_IMPORTED = 9.7734                 # cold nu=2/7 <=> K=2G locus, GR-imported (read-off)
NU_2_7 = float(NU_VAC)                      # = 2/7, visible knife target
A_CORE_SQRT_ALPHA = float(np.sqrt(ALPHA))  # A1 mass-core operating point sqrt(alpha)
# arc* band -> delta_y band (axiom-register.md:189: 0.89-0.96 tent, x0.79 elastica)
ARC_STAR_BAND = (0.70, 0.96)               # delta_y band for magnitude reporting (#526 ledger)


# ===========================================================================
# PLACEHOLDERS -- filled in subsequent commits (incremental-write discipline)
# ===========================================================================
# (1) THE TWO ARMS -- end-to-end force per loading path (symbolic backbone + numeric)
# (2) POSITIVE CONTROLS (HALT-gated)
# (3) THE FOUR TRACKS -- rho'/nu per {arm} x {magnitude law} through the remap
# (4) THE BIN SELECTOR -- no fall-through else; DISCREPANT-HALT reachable
# (5) main()


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit("scaffold only -- physics filled in subsequent commits")
