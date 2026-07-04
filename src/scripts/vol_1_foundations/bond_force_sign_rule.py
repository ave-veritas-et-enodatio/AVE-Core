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
# (1) THE TWO ARMS -- end-to-end force per loading path
#     Derived from A^2+S^2=arc*^2 (axiom-register.md:189), sympy-verified in
#     symbolic_backbone(); the numeric evaluators below are the same closed forms.
# ===========================================================================
# TENSION is defined POSITIVE (pulls ends together); COMPRESSION NEGATIVE
# (pushes ends apart / resists imposed shortening). This is the sign convention
# that flows straight into the #526 remap: T>0 grows k_shear_eff (caps rho'),
# T<0 shrinks it (uncaps). The convention is stated once, here.


def arm_a_pluck_tension(y: float, k_a: float = 1.0, ell: float = 1.0) -> float:
    """ARM (a) TRANSVERSE PLUCK (T2 response): end-to-end TENSION, chord clamped.

    Chord held at ell; transverse bow driven to amplitude y. To bow the strut the
    arc lengthens from ell to 2*sqrt((ell/2)^2+y^2) (tent geometry), stretching the
    material line -> axial tension k_a*(arc-ell). Its chord-directed component
    (the force pulling the clamped ends together) is:

        T_a(y) = k_a*ell*(1 - ell/sqrt(ell^2 + 4 y^2))    [POSITIVE = tension]

    Leading order T_a -> (2 k_a/ell) y^2 (2nd-order geometric). T_a(0)=0 exactly
    (guitar-string slack limit; POSITIVE CONTROL PC-a1).
    """
    return float(k_a * ell * (1.0 - ell / np.sqrt(ell ** 2 + 4.0 * y ** 2)))


def arm_a_pluck_tension_leading(y: float, k_a: float = 1.0, ell: float = 1.0) -> float:
    """The elementary small-y fixed-ends string result 2 k_a y^2 / ell (PC-a2 target)."""
    return float(2.0 * k_a * y ** 2 / ell)


def arm_b_endload_force(A: float, k0: float = 1.0) -> float:
    """ARM (b) AXIAL END-LOAD (A1 load): end-to-end COMPRESSION.

    Chord driven below natural length; bow free to equilibrate on the fixed-arc
    constraint -> the strut buckles and RESISTS compression. The end-to-end axial
    force has the SAME MAGNITUDE LAW as #526's Phi'(A) (the axial constitutive
    tension to change the bond's axial coordinate against the kernel stiffness
    Phi''=k0 sqrt(1-A^2)), but the SIGN is COMPRESSIVE because the bond is being
    shortened, not stretched:

        F_b(A) = -|Phi'(A)| = -bond_tension(A)      [NEGATIVE = compression]

    This is the ONLY difference between arm (b) and #526: #526 used +|Phi'(A)|
    (tensile sign); the fixed-arc-length end-load derivation gives the same
    magnitude with the compressive sign. bond_tension is the merged #526 function
    (consumed, not reimplemented) -- PC-recon gates this tie bit-exactly.
    """
    return float(-bond_tension(A, k0=k0))


def arm_b_plateau_buckling_load(k_b: float = 1.0, ell: float = 1.0) -> float:
    """ARM (b) post-buckling plateau P_c = k_b*ell/4 (buckling-load analog, kernel units).

    FINITE compressive force as bow->0+ (Euler plateau; POSITIVE CONTROL PC-b1).
    The 1/4 is a MECHANICAL tent-geometry factor: (1/2 bend-energy prefactor)
    x (1/2 tent half-chord chain). NOT the canon-distinguished 1/4 (a pinned-pinned
    elastica gives pi^2 instead). KNIFE=noise (result doc coincidence discipline).
    Returned NEGATIVE (compressive) to match the arm_b sign convention.
    """
    return float(-k_b * ell / 4.0)


def arm_b_prebuckle_hooke(u: float, k_a: float = 1.0) -> float:
    """ARM (b) pre-buckling Hooke branch -k_a*u (compressive, ->0 as u->0; PC-b2)."""
    return float(-k_a * u)


def arm_a_magnitude(A: float, law: str, k_a: float = 1.0, ell: float = 1.0) -> float:
    """Arm (a) TENSION magnitude under a chosen magnitude LAW (orchestrator Reading (b)).

    law='geometric' -> the arm's own 2nd-order pluck tension T_a(A) (bow=A).
    law='phi_prime'  -> the #526 |Phi'(A)| law (the alternative banded law).
    Both signed POSITIVE (tension). Neither is baked as "the" law (prereg cond. 1).
    """
    if law == "geometric":
        return arm_a_pluck_tension(A, k_a=k_a, ell=ell)
    if law == "phi_prime":
        return float(+bond_tension(A))          # #526 magnitude, tensile sign
    raise ValueError(f"unknown arm-a magnitude law {law!r}")


def arm_b_magnitude(A: float, law: str, k_a: float = 1.0, ell: float = 1.0) -> float:
    """Arm (b) COMPRESSION magnitude under a chosen magnitude LAW (orchestrator Reading (b)).

    law='phi_prime'  -> -|Phi'(A)| (the #526-law magnitude, compressive sign).
    law='geometric'  -> the 2nd-order geometric law -T_a(A) (compressive sign).
    Both signed NEGATIVE (compression). Neither is baked as "the" law (prereg cond. 1).
    """
    if law == "phi_prime":
        return float(-bond_tension(A))
    if law == "geometric":
        return float(-arm_a_pluck_tension(A, k_a=k_a, ell=ell))
    raise ValueError(f"unknown arm-b magnitude law {law!r}")


def symbolic_backbone() -> dict:
    """Sympy verification of EVERY derivative/chain-rule step (prereg PC-dim, cond).

    Returns a dict of exact-zero residuals; main() HALTs if any is not exactly 0.
    """
    import sympy as sp

    A, y, u, ell, k_a, k_b, k0, c, a = sp.symbols(
        "A y u ell k_a k_b k0 c a", positive=True
    )
    out = {}

    # (0) the axial constitutive energy: Phi'' = k0 sqrt(1-a^2) integrates to #526's Phi'
    Phi_p = sp.integrate(k0 * sp.sqrt(1 - a ** 2), (a, 0, A))
    Phi_p_526 = k0 * (A * sp.sqrt(1 - A ** 2) + sp.asin(A)) / 2
    out["phi_prime_matches_526"] = sp.simplify(Phi_p - Phi_p_526)          # == 0
    Phi = sp.integrate(Phi_p_526, (A, 0, y))
    out["phi_energy_at_0"] = sp.simplify(Phi.subs(y, 0))                    # == 0
    out["phi_prime_at_0"] = sp.simplify(sp.diff(Phi, y).subs(y, 0))         # == 0 (un-tensioned)
    out["phi_second_at_0_minus_k0"] = sp.simplify(
        sp.diff(Phi, y, 2).subs(y, 0) - k0
    )                                                                       # == 0 (Maxwell)

    # (a) arm (a) pluck: T_a = k_a*ell*(1 - ell/sqrt(ell^2+4y^2)); T_a(0)=0; leading 2 k_a y^2/ell
    T_a = k_a * ell * (1 - ell / sp.sqrt(ell ** 2 + 4 * y ** 2))
    out["arm_a_at_0"] = sp.simplify(T_a.subs(y, 0))                         # == 0 (PC-a1)
    lead = sp.series(T_a, y, 0, 4).removeO()
    out["arm_a_leading_minus_2ka_y2_over_ell"] = sp.simplify(
        sp.limit(lead / y ** 2, y, 0) - 2 * k_a / ell
    )                                                                       # == 0 (PC-a2)
    # derive T_a from energy independently: U = (1/2)k_a(arc-ell)^2 + (1/2)k_b y^2;
    # chord-component of internal tension = k_a*(arc-ell)*cos(angle):
    arc = 2 * sp.sqrt((ell / 2) ** 2 + y ** 2)
    T_internal = k_a * (arc - ell)
    cos_ang = (ell / 2) / sp.sqrt((ell / 2) ** 2 + y ** 2)
    out["arm_a_from_energy"] = sp.simplify(T_internal * cos_ang - T_a)      # == 0

    # (b) arm (b) buckling plateau: U_b=(1/2)k_b S^2, S^2=(ell/2)^2-(c/2)^2, F_out=-dU/dc
    S2 = (ell / 2) ** 2 - (c / 2) ** 2
    U_b = sp.Rational(1, 2) * k_b * S2
    F_out = -sp.diff(U_b, c)
    out["arm_b_F_out_minus_kb_c_over_4"] = sp.simplify(F_out - k_b * c / 4)  # == 0
    out["arm_b_plateau_minus_kb_ell_over_4"] = sp.simplify(
        F_out.subs(c, ell) - k_b * ell / 4
    )                                                                       # == 0 (PC-b1)
    # the 1/4 trace (condition 4): (1/2 prefactor) x (1/2 half-chord chain)
    out["quarter_factor_trace"] = sp.simplify(
        sp.Rational(1, 2) * sp.Rational(1, 2) - sp.Rational(1, 4)
    )                                                                       # == 0

    # (b pre-buckle) Hooke: U_ax=(1/2)k_a u^2, F=dU/du=k_a u, ->0 as u->0
    U_ax = sp.Rational(1, 2) * k_a * u ** 2
    out["arm_b_prebuckle"] = sp.simplify(sp.diff(U_ax, u) - k_a * u)        # == 0 (PC-b2)
    out["arm_b_prebuckle_at_0"] = sp.simplify(sp.diff(U_ax, u).subs(u, 0))  # == 0

    return {k: v for k, v in out.items()}


# ===========================================================================
# PLACEHOLDERS -- filled in subsequent commits (incremental-write discipline)
# ===========================================================================
# (2) POSITIVE CONTROLS (HALT-gated)
# (3) THE FOUR TRACKS -- rho'/nu per {arm} x {magnitude law} through the remap
# (4) THE BIN SELECTOR -- no fall-through else; DISCREPANT-HALT reachable
# (5) main()


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit("physics WIP -- controls/tracks/bins/main in subsequent commits")
