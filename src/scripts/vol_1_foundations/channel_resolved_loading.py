"""Channel-resolved loading — does rho' preserve for the traveling wave, move for the confined mode?

Prereg (FROZEN): research/2026-07-05_channel-resolved-loading_prereg_FROZEN.md
Successor to the merged NEGATIVE #529 (scalar <T> can't distinguish matter from radiation).

THE QUESTION (channel-resolved, per the frozen prereg): per bond, decompose the time-averaged bias
into the AXIAL channel (numerator S_axial) and the SHEAR-adjacent slot (denominator S_shear + T/ell)
for (i) a matched CW TRAVELING transverse wave and (ii) a CONFINED Gamma=-1 standing mode; adjudicate
whether rho' = S_axial / (S_shear + T/ell) is preserved for (i) and moved for (ii).

GRANT 2026-07-05 (Q-point ruling, verbatim in prereg): S keyed on DEFORMATION-toward-snap, NOT stress.
  - Numerator S_axial UNTOUCHED by a <A>=0 transverse wave (axial deformation 4th-order).
  - NO-DOUBLE-COUNT: the tension T is a STRESS; it enters ONLY the denominator +T/ell term, never an
    S-factor. Keying S on stress double-counts and corrupts the PC2-validated #526 form.
  - Denominator carries TWO competing 2nd-order terms: soft (k_s*S shift, <A^2> keying) + stiff (+T/ell).

CONSUMES (import only; NEVER edits -- concurrency-safe):
  #526  prestress_elastic_tensor : _prestress_tensor_at, bond_tension, extract_prestress_Cij  (the remap)
  #527  bond_force_sign_rule     : _remap_at_signed_T                                          (signed-T remap)
  #529  resonant_tension_law     : field_from_abcd_propagation, resonant_tension_leading        (Gamma-free T)
  Ax4   scale_invariant          : saturation_factor                                            (S kernel)
  #528  ave.validation.reconcile_gate : ReconcileGate                                           (the ONLY gate)

Driver is skeleton-first (this commit); physics lands one section per commit.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

# --- CONSUME #526 remap (import only) --------------------------------------------------
from scripts.vol_1_foundations.prestress_elastic_tensor import (  # noqa: E402
    bond_tension,
    extract_prestress_Cij,
    moduli_from_Cij,
)

# --- CONSUME #529 Gamma-free traveling-wave field (import only) ------------------------
from scripts.vol_1_foundations.resonant_tension_law import (  # noqa: E402
    field_from_abcd_propagation,
    resonant_tension_leading,
)
from scripts.vol_1_foundations.srs_elastic_tensor import srs_primitive  # noqa: E402

# --- Ax4 kernel + canon anchors (import only) -----------------------------------------
from ave.axioms.scale_invariant import saturation_factor  # noqa: E402
from ave.core.constants import ALPHA  # noqa: E402

# --- #528 reconcile-gate: the ONLY acceptable discrepancy gate -------------------------
from ave.validation.reconcile_gate import ReconcileGate  # noqa: E402

# ---------------------------------------------------------------------------------------
# CANON ANCHORS (imported / read-off -- NOT tuned)
# ---------------------------------------------------------------------------------------
A_Y = 1.0                                   # canonical yield (def-vyvsn1)
A_CORE_SQRT_ALPHA = float(np.sqrt(ALPHA))   # A1 mass-core DC bias (def-vyvsn1, alpha-echo)
RHO_COLD = 1.0                              # Ax3 cold ratio (knob-free, PR#516)
ARC_STAR_BAND = (0.70, 0.96)               # #527 in-regime bow band (elastica .. tent edge)

_OUT = Path(__file__).with_suffix("").parent / "_output" / "channel_resolved_loading.json"


# ---------------------------------------------------------------------------------------
# (S1) SYMBOLIC BACKBONE -- every 2nd-order loading term, sympy-verified (exact-zero residuals)
# ---------------------------------------------------------------------------------------
def symbolic_backbone() -> dict:
    """Placeholder -- lands next commit. Verifies: <sin^2>=1/2; T=(k_a/ell)y0^2 (Part-1);
    soft term = -k_s y0^2/(4 A_y^2) (S-Taylor + <A^2> keying); dD/k0 = 3/4 y0^2 at A_y=1;
    cancellation requires A_y=1/2 (the knife tell); axial deform 4th-order (numerator untouched)."""
    raise NotImplementedError("symbolic_backbone lands next commit")


# ---------------------------------------------------------------------------------------
# (S2) PER-CHANNEL LOADING -- the axial numerator + the shear-adjacent denominator, both waves
# ---------------------------------------------------------------------------------------
def channel_loading(y0: float, A_dc: float, dictionary: str, ell: float = 1.0) -> dict:
    """Placeholder -- lands after the symbolic backbone."""
    raise NotImplementedError("channel_loading lands after S1")


# ---------------------------------------------------------------------------------------
# (S3) THE PUMP-NULL CONSISTENCY GATE -- reproduce #529's uniform scalar <T> BEFORE channel-resolved
# ---------------------------------------------------------------------------------------
def consistency_gate_529(pos, bonds, rho) -> dict:
    """Placeholder -- the HARD reconcile against field_from_abcd_propagation (#529 Gamma-free path)."""
    raise NotImplementedError("consistency_gate_529 lands after S2")


# ---------------------------------------------------------------------------------------
# (S4) THE TWO CASES THROUGH THE REMAP -- rho'_travel and rho'_conf, banded over y0 (log grid)
# ---------------------------------------------------------------------------------------
def rho_prime_both_cases(pos, bonds, rho) -> dict:
    """Placeholder -- feeds both cases through the #526 remap; rho'-shift per case, banded."""
    raise NotImplementedError("rho_prime_both_cases lands after S3")


# ---------------------------------------------------------------------------------------
# (S5) POSITIVE CONTROLS -- HALT-gated, each an INDEPENDENT reference path (#528 helper only)
# ---------------------------------------------------------------------------------------
def run_positive_controls(pos, bonds, rho) -> dict:
    """Placeholder -- PC-consistency / PC-cold / PC-numerator / PC-denominator-independent."""
    raise NotImplementedError("run_positive_controls lands after S4")


# ---------------------------------------------------------------------------------------
# (S6) BIN SELECTOR -- verbatim from the FROZEN prereg; no fall-through
# ---------------------------------------------------------------------------------------
def select_bin(cases: dict) -> dict:
    """Placeholder -- routes to CHANNEL-DISCRIMINATOR-DERIVED / SYMMETRIC-BOTH / ASYMMETRIC-BOTH /
    UNDERDETERMINED per the frozen routing table; final else = UNDERDETERMINED (no fall-through)."""
    raise NotImplementedError("select_bin lands last")


def _write(out: dict) -> None:
    _OUT.parent.mkdir(parents=True, exist_ok=True)
    _OUT.write_text(json.dumps(out, indent=2))


def main() -> int:
    pos, bonds, rho = srs_primitive("right")
    ell = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds]))
    out: dict = {
        "prereg": "research/2026-07-05_channel-resolved-loading_prereg_FROZEN.md",
        "geometry": {"n_bonds": len(bonds), "ell": ell, "rho": rho},
        "anchors": {"A_y": A_Y, "A_core_sqrt_alpha": A_CORE_SQRT_ALPHA, "rho_cold": RHO_COLD},
    }
    # sections land one per commit; skeleton exits clean.
    _write(out)
    print("skeleton: geometry + anchors written; physics sections land per-commit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
