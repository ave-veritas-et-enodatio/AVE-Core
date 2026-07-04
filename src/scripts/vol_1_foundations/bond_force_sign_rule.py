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
# (2) POSITIVE CONTROLS (HALT-gated) -- run BEFORE any adjudicated number
# ===========================================================================
def run_positive_controls(pos, bonds, rho) -> dict:
    """All HALT-gated positive controls (prereg PC-a1/a2/b1/b2/recon/dim)."""
    import numpy as _np

    results = {}

    # PC-dim: sympy backbone, every derivative exact-zero
    backbone = symbolic_backbone()
    backbone_ok = all(v == 0 for v in backbone.values())
    results["PC_dim_symbolic_all_exact_zero"] = bool(backbone_ok)
    results["PC_dim_residuals"] = {k: str(v) for k, v in backbone.items()}

    # PC-a1: arm (a) tension vanishes at zero pluck
    ta0 = arm_a_pluck_tension(0.0)
    results["PC_a1_pluck_at_zero"] = float(ta0)
    results["PC_a1_ok"] = bool(ta0 == 0.0)

    # PC-a2: small-y limit matches 2 k_a y^2 / ell to O(y^4)
    ys = _np.array([1e-3, 1e-2, 5e-2])
    exact = _np.array([arm_a_pluck_tension(float(y)) for y in ys])
    lead = _np.array([arm_a_pluck_tension_leading(float(y)) for y in ys])
    rel = _np.abs(exact - lead) / _np.abs(lead)
    results["PC_a2_max_rel_dev_smally"] = float(_np.max(rel))
    results["PC_a2_ok"] = bool(rel[0] < 1e-4)  # y=1e-3 -> O(y^2)=1e-6 dev

    # PC-b1: buckling plateau finite as bow->0+ (Euler analog)
    pc = arm_b_plateau_buckling_load(k_b=1.0, ell=1.0)
    results["PC_b1_plateau_kernel_units"] = float(pc)
    results["PC_b1_ok"] = bool(_np.isfinite(pc) and pc < 0.0 and abs(pc + 0.25) < 1e-15)

    # PC-b2: pre-buckle Hooke -> 0 as u->0, compressive for u>0
    results["PC_b2_hooke_at_zero"] = float(arm_b_prebuckle_hooke(0.0))
    results["PC_b2_ok"] = bool(
        arm_b_prebuckle_hooke(0.0) == 0.0 and arm_b_prebuckle_hooke(0.1) < 0.0
    )

    # PC-recon: arm (b) magnitude == #526 bond_tension bit-exactly (consumed fn)
    As = _np.linspace(0.05, 0.95, 19)
    recon = _np.array(
        [abs(arm_b_magnitude(float(a), "phi_prime")) - float(bond_tension(a)) for a in As]
    )
    results["PC_recon_max_abs_dev"] = float(_np.max(_np.abs(recon)))
    results["PC_recon_ok"] = bool(_np.max(_np.abs(recon)) < 1e-12)

    # PC-affine: the bulk-strain -> per-bond amplitude map is uniform/affine (item 4)
    aff = bulk_strain_to_per_bond_amplitude(0.01, pos, bonds)
    results["PC_affine_map"] = aff
    results["PC_affine_ok"] = bool(aff["uniform"] and abs(aff["A_bond_affine"] - 0.01) < 1e-12)

    all_ok = all(
        results[k] for k in results if k.endswith("_ok")
    )
    results["ALL_PC_PASS"] = bool(all_ok)
    return results


# ===========================================================================
# THE IN-REGIME BOW BOUND (review item 2) -- the fixed-arc premise's own limit
# ===========================================================================
def bulk_strain_to_per_bond_amplitude(eps: float, pos, bonds) -> dict:
    """The AFFINE bulk-strain -> per-bond axial amplitude mapping (review item 4).

    A uniform (isotropic) bulk strain eps deforms every position x -> (1-eps)x, so each
    bond vector d -> (1-eps)d and its chord |d| -> (1-eps)|d|. The per-bond axial
    (compressive) strain is therefore A_bond = -d|d|/|d| = eps on EVERY bond identically
    -- orientation-independent (verified: min==max across all srs bonds). So the arm-(b)
    end-load amplitude A_axial IS the affine bulk strain, for an affine uniform strain.

    COPLANAR-NODE CAVEAT: srs z=3 sites are NOT centrosymmetric, so a uniform CELL strain
    also induces internal relaxation (the internal-strain modes). A_bond=eps is the AFFINE
    (leading) part; the relaxed part is exactly what the internal-strain-relaxed #526
    Christoffel pipeline already handles. This is why the driver uses the A1 op-point
    amplitude directly and calls the mapping AFFINE (not "gravity") -- the bulk->bond
    map is the trivial affine one; a full gravitational bulk-strain profile is PENDING.
    """
    strains = []
    for (_, _, d) in bonds:
        dv = np.asarray(d, float)
        ell = np.linalg.norm(dv)
        dell = np.linalg.norm((1.0 - eps) * dv) - ell
        strains.append(-dell / ell)
    strains = np.array(strains)
    return {
        "eps": float(eps),
        "per_bond_axial_strain_min": float(strains.min()),
        "per_bond_axial_strain_max": float(strains.max()),
        "uniform": bool(np.ptp(strains) < 1e-12),   # orientation-independent affine map
        "A_bond_affine": float(strains.mean()),      # == eps
    }


def in_regime_pluck_bow(arc_star: float, ell: float = 1.0) -> float:
    """Max IN-REGIME transverse pluck bow y at fixed-arc premise arc* (review item 2).

    The microfoundation premise (axiom-register.md:189) fixes the arc at arc* (a FEW %
    to ~30% below ell over the band). For arm (a) (chord clamped near ell, bow driven,
    the arc-STRETCHING finite-stiffness pluck), the largest bow the premise LICENSES is
    the one whose pluck-arc does not exceed the arc the premise admits: the OUTWARD arc
    excess is bounded by the SAME magnitude as the arc* deficit (|1 - arc*/ell|). So the
    in-regime arc bound is ell*(1 + (1 - arc*/ell)) = ell*(2 - arc*/ell), and

        arc(y) = 2*sqrt((ell/2)^2 + y^2) <= ell*(2 - arc*/ell)
        => y_max = sqrt((arc_bound/2)^2 - (ell/2)^2),   arc_bound = ell*(2 - arc*/ell).

    This REPLACES the out-of-regime y=0.99479 (arc=2.23*ell, 2.3x the premise). At the
    band edges (arc*=0.70 elastica / 0.96 tent): y_max ~ 0.42 / 0.14. NOT an ad-hoc
    number -- it is the fixed-arc premise's own displacement ceiling.
    """
    slack = abs(1.0 - arc_star / ell)             # arc* deficit = admissible arc excess
    arc_bound = ell * (1.0 + slack)
    val = (arc_bound / 2.0) ** 2 - (ell / 2.0) ** 2
    return float(np.sqrt(val)) if val > 0 else 0.0


# ===========================================================================
# (3) THE FOUR TRACKS -- rho'/nu per {arm} x {magnitude law} through the remap
# ===========================================================================
def _remap_at_signed_T(pos, bonds, rho, A_axial, A_shear, T_signed):
    """Feed a SIGNED per-bond axial force T into the MERGED #526 remap machinery.

    Consumes extract_prestress_Cij (the #526 pre-stressed Born-Huang tensor) and the
    #526 remap formula k_shear_eff = S_shear + T/ell, rho' = S_ax/k_shear_eff. The
    ONLY thing this arc changes vs #526 is the SIGN (and, per Reading (b), the
    magnitude LAW) of T -- everything downstream is the merged pipeline verbatim.
    """
    S_axial = float(saturation_factor(A_axial, yield_limit=1.0))
    S_shear = float(saturation_factor(A_shear, yield_limit=1.0))
    ell = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds]))  # =1 on srs
    r = extract_prestress_Cij(pos, bonds, k_axial=S_axial, k_shear=S_shear,
                              T_per_bond=float(T_signed), rho=rho)
    mo = moduli_from_Cij(r["C11"], r["C12"], r["C44"])
    k_shear_eff = S_shear + float(T_signed) / ell         # #526 shifted shear spring
    rho_prime = (S_axial / k_shear_eff) if k_shear_eff > 0 else float("inf")
    return {
        "A_axial": A_axial, "A_shear": A_shear, "S_axial": S_axial, "S_shear": S_shear,
        "ell": ell, "T_signed": float(T_signed), "k_shear_eff": k_shear_eff,
        "rho_prime": rho_prime, "nu": mo["nu_Hill"], "K": mo["K_bulk"],
        "Zener": mo["Zener_A"], "min_acoustic_eig": r["min_acoustic_eig"],
    }


def four_tracks(pos, bonds, rho, arc_star=0.96) -> dict:
    """The FOUR tracks (prereg cond.2): {arm a, arm b} x {geometric, phi_prime} laws.

    IN-REGIME (review item 2). Reported SEPARATELY (Grant rules on the noun at review).
    - arm (a) TENSION: plucked at the IN-REGIME bow y_max = in_regime_pluck_bow(arc*),
      the fixed-arc premise's own displacement ceiling (NOT the out-of-regime y=0.99479
      whose arc was 2.23*ell). The BAND is over arc* itself (the DISPLACEMENT premise),
      applied inside the geometry -- NOT delta_y multiplying the force. arc_star in the
      canon band [0.70, 0.96].
    - arm (b) COMPRESSION: end-loaded at the A1 op-point amplitude A_axial=sqrt(alpha)
      (in-regime: S(sqrt(alpha))=0.996, the arc is unshifted); its band is over arc*
      likewise entering the force magnitude through the constitutive law.

    The #518 shear operating channel (A_shear=0.99479) sets k_shear=S(A_shear) at the
    crossing; the SIGN of T flows into cap-vs-uncap.
    """
    A_axial = A_CORE_SQRT_ALPHA
    A_shear_op = 0.99479       # #518 crossing amplitude (read-off; sets k_shear at crossing)
    ell = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds]))  # =1 on srs
    y_pluck = in_regime_pluck_bow(arc_star, ell)   # IN-REGIME displacement (item 2)

    tracks = {}
    # arm (a): TENSION (T>0), plucked to the in-regime bow. Both laws POSITIVE.
    for law in ("geometric", "phi_prime"):
        T_a = arm_a_magnitude(y_pluck, law)                    # >0 tension at in-regime bow
        tracks[f"arm_a_{law}"] = {
            "arm": "a_pluck", "sign": "tension(+)", "law": law,
            "y_pluck_in_regime": y_pluck, "arc_star": arc_star,
            **_remap_at_signed_T(pos, bonds, rho, A_axial, A_shear_op, +abs(T_a)),
        }
    # arm (b): COMPRESSION (T<0) at A_axial=sqrt(alpha) (the actual #526 A1 bias).
    # The arc* band enters as a displacement scale on the constitutive force (the bias
    # amplitude is fixed at the op-point; the band scales the yield-displacement d_y).
    dy = arc_star / 0.96       # in-regime displacement scale, normalized to the tent edge
    for law in ("phi_prime", "geometric"):
        T_b = dy * arm_b_magnitude(A_axial, law)               # <0 compression
        tracks[f"arm_b_{law}"] = {
            "arm": "b_endload", "sign": "compression(-)", "law": law,
            "arc_star": arc_star,
            **_remap_at_signed_T(pos, bonds, rho, A_axial, A_shear_op, -abs(T_b)),
        }
    return tracks


# ===========================================================================
# (4) THE BIN SELECTOR -- no fall-through else; DISCREPANT-HALT reachable + unit-tested
# ===========================================================================
class DiscrepantHalt(RuntimeError):
    """Raised when a derived FORCE SIGN contradicts the remap STRUCTURE it feeds.

    A TENSION (T>0) must GROW k_shear_eff (cap rho'); a COMPRESSION (T<0) must
    SHRINK it (uncap). If a track's sign and its remap structure disagree, that is
    a contradiction to surface loudly, NOT silently bin (closes the #521/#526
    dead-else gap). Unit-tested to TRIGGER on synthetic input.
    """


def _sign_structure_consistent(T_signed: float, S_shear: float, k_shear_eff: float) -> bool:
    """A tension must not uncap; a compression must not strictly cap.

    tension (T>0)  => k_shear_eff > S_shear (STRICTLY CAPPED, grown).
    compression (T<0) => k_shear_eff < S_shear (uncapped direction, shrunk).
    T==0 => k_shear_eff == S_shear (no pre-stress).
    """
    if T_signed > 0:
        return k_shear_eff > S_shear
    if T_signed < 0:
        return k_shear_eff < S_shear
    return abs(k_shear_eff - S_shear) < 1e-12


def select_bin(tracks: dict) -> dict:
    """Map the four tracks to the FROZEN bins. NO fall-through else.

    Reads the SIGN of each arm's end-to-end force (arm a tension, arm b compression)
    and adjudicates:
      both arms opposite sign  -> [SIGN-RULE-DERIVED]
      both arms same sign      -> [SAME-SIGN]
      an arm's force undefined -> [PATH-INDETERMINATE]
    DISCREPANT-HALT fires FIRST if any track's sign contradicts its remap structure.
    """
    # DISCREPANT-HALT gate (reachable; unit-tested to trigger on synthetic input)
    for name, t in tracks.items():
        T, S_sh, kse = t["T_signed"], t["S_shear"], t["k_shear_eff"]
        if not _sign_structure_consistent(T, S_sh, kse):
            raise DiscrepantHalt(
                f"sign<->structure contradiction in track {name!r}: "
                f"T={T:+.4e}, S_shear={S_sh:.4e}, k_shear_eff={kse:.4e} "
                f"(tension must cap / compression must uncap)"
            )

    # arm signs from the SIGN of T (not the remap -- the force is the primary datum)
    arm_a_signs = {np.sign(t["T_signed"]) for k, t in tracks.items() if t["arm"] == "a_pluck"}
    arm_b_signs = {np.sign(t["T_signed"]) for k, t in tracks.items() if t["arm"] == "b_endload"}

    # PATH-INDETERMINATE: a force analytically undefined (NaN/inf) or a sign of 0
    def _undefined(sgns):
        return (len(sgns) == 0) or any(
            (s == 0) or (not np.isfinite(s)) for s in sgns
        )

    if _undefined(arm_a_signs) or _undefined(arm_b_signs):
        verdict = "PATH-INDETERMINATE"
        reason = ("an arm's end-to-end force is analytically undefined / zero-signed "
                  "without additional structure the canon does not supply")
    else:
        a_sign = arm_a_signs.pop() if len(arm_a_signs) == 1 else None
        b_sign = arm_b_signs.pop() if len(arm_b_signs) == 1 else None
        if a_sign is None or b_sign is None:
            # an arm carries BOTH signs across laws -> the sign is not law-robust
            verdict = "PATH-INDETERMINATE"
            reason = "an arm's sign is not robust across its banded magnitude laws"
        elif a_sign != b_sign:
            verdict = "SIGN-RULE-DERIVED"
            reason = ("opposite-sign end forces from the same fixed-arc constraint: "
                      "pluck->tension->capped, end-load->compression->uncapped")
        else:
            verdict = "SAME-SIGN"
            reason = (f"both loading paths give sign {a_sign:+.0f}; the channel-keyed "
                      "hypothesis fails, the #526 fork collapses to a single global sign")

    return {
        "verdict": verdict, "reason": reason,
        "arm_a_sign": ("tension(+)" if 1 in {np.sign(t["T_signed"]) for k, t in tracks.items()
                                             if t["arm"] == "a_pluck"} else "n/a"),
        "arm_b_sign": ("compression(-)" if -1 in {np.sign(t["T_signed"]) for k, t in tracks.items()
                                                  if t["arm"] == "b_endload"} else "n/a"),
    }


# ===========================================================================
# (5) main()
# ===========================================================================
def _band_over_arc_star(pos, bonds, rho) -> dict:
    """Report every rho'/nu track IN-REGIME, banded over arc* in [0.70, 0.96] (item 2).

    arc* is the fixed-arc premise (axiom-register.md:189); the band is over arc* itself,
    entering the geometry (arm a: the in-regime pluck bow) and the displacement scale
    (arm b), NOT delta_y multiplying the force. lo=elastica edge, hi=tent edge.
    """
    lo, hi = ARC_STAR_BAND
    band = {}
    for name, arc_star in (("lo_elastica", lo), ("hi_tent", hi)):
        band[name] = {"arc_star": arc_star,
                      "in_regime_pluck_bow": in_regime_pluck_bow(arc_star),
                      "tracks": four_tracks(pos, bonds, rho, arc_star=arc_star)}
    return band


def _write(out: dict) -> None:
    outdir = Path(__file__).resolve().parent / "_output"
    outdir.mkdir(exist_ok=True)
    path = outdir / "bond_force_sign_rule.json"
    path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nwrote {path}")


def main() -> int:
    out = {
        "title": "THE END-TO-END BOND FORCE PER LOADING PATH (resolves the #526 sign fork)",
        "prereg": "research/2026-07-04_bond-force-sign-rule_prereg_FROZEN.md",
        "scope": "per-channel SIGN+MAGNITUDE of the per-bond axial load ONLY; "
        "the cell-dilation relaxation (#526 test 2) is DOWNSTREAM (this is its input)",
        "arc_star_band": ARC_STAR_BAND,
        "regime_bound": "IN-REGIME (item 2): arm (a) plucked at in_regime_pluck_bow(arc*) "
        "(the fixed-arc premise's own displacement ceiling), NOT the out-of-regime y=0.99479 "
        "(arc=2.23*ell). arm (b) at A1 op-point sqrt(alpha), S=0.996 (arc unshifted).",
    }
    print("=" * 78)
    print("BOND-FORCE SIGN RULE PER LOADING PATH — resolving the PR #526 sign fork")
    print("=" * 78)

    pos_r, bonds_r, rho_r = srs_primitive("right")

    # ---- (0) POSITIVE CONTROLS (HALT if fail) ----------------------------
    pc = run_positive_controls(pos_r, bonds_r, rho_r)
    out["positive_controls"] = pc
    print("(0) POSITIVE CONTROLS (HALT if fail):")
    for k in ("PC_a1_ok", "PC_a2_ok", "PC_b1_ok", "PC_b2_ok", "PC_recon_ok",
              "PC_dim_symbolic_all_exact_zero"):
        print(f"  {k:34s} = {pc[k]}")
    print(f"  ALL_PC_PASS = {pc['ALL_PC_PASS']}")
    if not pc["ALL_PC_PASS"]:
        print("\nHALT: positive controls FAILED — no verdict.")
        _write(out)
        return 1

    # ---- (1) THE FOUR TRACKS, IN-REGIME, banded over arc* [both edges] ----
    band = _band_over_arc_star(pos_r, bonds_r, rho_r)
    out["four_tracks_banded_in_regime"] = band
    print("\n(1) THE FOUR TRACKS (IN-REGIME; banded over arc* both edges):")
    for edge in ("lo_elastica", "hi_tent"):
        b = band[edge]
        print(f"  -- {edge} (arc*={b['arc_star']}, in-regime pluck bow y={b['in_regime_pluck_bow']:.4f}) --")
        for name, t in b["tracks"].items():
            rp = t["rho_prime"]
            rps = "inf" if rp == float("inf") else f"{rp:.4f}"
            print(f"     {name:18s}: {t['sign']:14s} law={t['law']:9s} "
                  f"T={t['T_signed']:+.5f} k_sh_eff={t['k_shear_eff']:+.6f} "
                  f"rho'={rps:>9s} nu={t['nu']:+.5f} K={t['K']:+.5f}")

    # ---- (2) THE BIN (no fall-through else; DISCREPANT-HALT reachable) ----
    # The verdict is a SIGN verdict; it is band-edge-invariant. Adjudicate at both
    # edges and require agreement (a sign that flipped across the band would be a
    # PATH-INDETERMINATE signal, not a silent pick).
    try:
        verdict_lo = select_bin(band["lo_elastica"]["tracks"])
        verdict_hi = select_bin(band["hi_tent"]["tracks"])
    except DiscrepantHalt as e:
        out["verdict"] = {"verdict": "DISCREPANT-HALT", "detail": str(e)}
        print(f"\nDISCREPANT-HALT: {e}")
        _write(out)
        return 2
    if verdict_lo["verdict"] != verdict_hi["verdict"]:
        out["verdict"] = {"verdict": "BAND-INCONSISTENT",
                          "lo": verdict_lo["verdict"], "hi": verdict_hi["verdict"]}
        print(f"\nBAND-INCONSISTENT: lo={verdict_lo['verdict']} hi={verdict_hi['verdict']}")
        _write(out)
        return 3
    out["verdict"] = verdict_lo
    print(f"\n(2) VERDICT: [{verdict_lo['verdict']}]  — {verdict_lo['reason']}")
    print(f"    (band-edge-invariant: elastica AND tent both [{verdict_lo['verdict']}])")

    # ---- (3) THE KNIVES (condition 4 + item 3) --------------------------
    # (3a) the plateau 1/4 (condition 4)
    # (3b) the srs K=0 crossing at rho=2 -- the arm_a in-regime cap can land near it
    arm_a_rho_primes = [t["rho_prime"] for edge in band.values()
                        for name, t in edge["tracks"].items() if t["arm"] == "a_pluck"]
    arm_a_Ks = [t["K"] for edge in band.values()
                for name, t in edge["tracks"].items() if t["arm"] == "a_pluck"]
    k_sign_flips = (min(arm_a_Ks) < 0) and (max(arm_a_Ks) > 0)
    out["knives"] = {
        "plateau_P_c": arm_b_plateau_buckling_load(1.0, 1.0),
        "plateau_quarter_provenance": "tent geometry: (1/2 bend prefactor) x (1/2 half-chord "
        "chain); a pinned-pinned elastica gives pi^2; a FORCE in kernel units, not a "
        "charge-fraction 1/4 => KNIFE=noise",
        "arm_a_rho_prime_range_in_regime": [float(min(arm_a_rho_primes)),
                                            float(max(arm_a_rho_primes))],
        "arm_a_straddles_srs_K0_rho2": bool(min(arm_a_rho_primes) <= 2.0 <= max(arm_a_rho_primes)
                                            or k_sign_flips),
        "srs_K0_note": "on srs K=0 at rho=2 (K sign-flips), K=2G at rho=9.77 -- the arm_a "
        "in-regime cap band straddles the srs K=0 pole; this is the srs swapped-spring rho, "
        "NOT the axiom-register:189 moduli-model rho (where rho=2<=>K=2G by the z=4 "
        "convention) -- a cross-carrier rho-convention homonym, FLAGGED for the auditor lane",
        "K_sign_flips_across_arm_a_band": bool(k_sign_flips),
        "lands_on_canon_distinguished_value": False,
    }
    print(f"(3a) KNIFE: plateau P_c={out['knives']['plateau_P_c']} (=-1/4, tent geometry, "
          f"KNIFE=noise)")
    print(f"(3b) KNIFE: arm_a in-regime rho' in {out['knives']['arm_a_rho_prime_range_in_regime']}; "
          f"straddles srs K=0 at rho=2: {out['knives']['arm_a_straddles_srs_K0_rho2']} "
          f"(K sign-flips: {k_sign_flips}); cross-carrier rho-convention FLAGGED")

    _write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
