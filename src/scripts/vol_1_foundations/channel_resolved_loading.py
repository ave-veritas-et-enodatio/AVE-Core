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
    """Every 2nd-order loading term, sympy-verified with exact-zero residuals. No term is dropped
    without an order-proof. All quantities dimensionless (y0 in ell_node units, ell=1 default).

    The ledger of DERIVED factors (the ONLY factors allowed to enter -- knife clause):
      - <sin^2> = 1/2                                  (THE one 1/2; time-average of sin^2)
      - <y^2> = y0^2/2, <A_shear^2> from the y0<->A_shear dictionary
      - S(A) ~ 1 - A^2/(2 A_y^2)                        (Ax4 kernel Taylor; the /2)
      - soft denominator term = -k_s <A_shear^2>/(2 A_y^2)   (SOFTENING, S-shift)
      - stiff denominator term = +T/ell = +(k_a/ell) y0^2   (STIFFENING, #529 Part-1 geometric)
      - dD/k0 at A_y=1, k_a=k_s=k0, dictionary D1 (A_shear=y0/ell): +3/4 y0^2  (NO cancellation)
      - cancellation (dD=0) requires A_y=1/2 -- the KNIFE TELL (imported yield in a costume)
      - axial deformation OSCILLATION is 4th-order in y0 -> numerator S_axial untouched at 2nd order
    """
    import sympy as sp

    y0, ell, k0, ka, ks, Ay, t = sp.symbols("y0 ell k0 k_a k_s A_y t", positive=True)
    w = sp.symbols("omega", positive=True)
    residuals: dict[str, sp.Expr] = {}

    # (1) <sin^2> = 1/2 -- the one derived 1/2
    mean_sin2 = sp.integrate(sp.sin(w * t) ** 2, (t, 0, 2 * sp.pi / w)) / (2 * sp.pi / w)
    residuals["mean_sin2_minus_half"] = sp.simplify(mean_sin2 - sp.Rational(1, 2))

    # (2) <y^2> = y0^2 <sin^2> = y0^2/2
    mean_y2 = y0**2 * mean_sin2
    residuals["mean_y2_minus_y0sq_over_2"] = sp.simplify(mean_y2 - y0**2 / 2)

    # (3) Part-1 geometric chord tension T = (k_a/ell) y0^2 (#529 leading law, <sin^2>=1/2 folded in).
    #     Derived from the exact tent law's 2nd-order series: 1 - ell/sqrt(ell^2+4y^2 sin^2) ~
    #     (2 y^2 sin^2)/ell^2, time-averaged with <sin^2>=1/2 and multiplied by k_a*ell.
    yv = sp.symbols("y", positive=True)
    tent_integrand = 1 - ell / sp.sqrt(ell**2 + 4 * yv**2 * sp.sin(w * t) ** 2)
    tent_2nd = sp.series(tent_integrand, yv, 0, 3).removeO()  # (2 y^2 sin^2)/ell^2
    T_avg = k0 * ell * (sp.integrate(tent_2nd, (t, 0, 2 * sp.pi / w)) / (2 * sp.pi / w))
    T_avg = T_avg.subs(yv, y0)
    residuals["T_avg_minus_ka_y0sq_over_ell"] = sp.simplify(T_avg - k0 / ell * y0**2)

    # (4) S-kernel Taylor: S(A) = sqrt(1 - A^2/A_y^2) ~ 1 - A^2/(2 A_y^2) at 2nd order.
    A = sp.symbols("A", real=True)
    S_series = sp.series(sp.sqrt(1 - A**2 / Ay**2), A, 0, 3).removeO()
    residuals["S_taylor_minus_form"] = sp.simplify(S_series - (1 - A**2 / (2 * Ay**2)))

    # (5) soft denominator term: time-averaged shear-spring shift k_s*(S_shear_avg - 1).
    #     <A_shear^2> per dictionary D1 (angle) = (y0/ell)^2/2; the soft term = k_s*(-<A_shear^2>/(2 A_y^2)).
    mean_Ashear2_D1 = (y0 / ell) ** 2 * mean_sin2  # = (y0/ell)^2 / 2
    S_shear_avg_D1 = 1 - mean_Ashear2_D1 / (2 * Ay**2)
    soft_D1 = ks * (S_shear_avg_D1 - 1)
    residuals["soft_D1_minus_form"] = sp.simplify(soft_D1 - (-ks * (y0 / ell) ** 2 / (4 * Ay**2)))

    # (6) stiff denominator term = +T/ell = +(k_a/ell^2) y0^2
    stiff = T_avg / ell
    residuals["stiff_minus_form"] = sp.simplify(stiff - k0 / ell**2 * y0**2)

    # (7) THE COMPETITION: dD = soft + stiff at the Ax3 matched point k_a=k_s=k0.
    dD_D1 = soft_D1.subs(ks, k0) + stiff
    dD_over_k0_D1 = sp.simplify(dD_D1 / k0)
    residuals["dD_over_k0_D1_at_Ay1"] = sp.simplify(
        dD_over_k0_D1.subs({Ay: 1, ell: 1}) - sp.Rational(3, 4) * y0**2
    )  # +3/4 y0^2 at A_y=1: NO cancellation

    # (8) cancellation condition: dD=0 requires A_y = 1/2 (the knife tell).
    cancel_Ay = sp.solve(sp.Eq(sp.simplify(dD_over_k0_D1.subs(ell, 1)), 0), Ay)
    cancel_Ay = [s for s in cancel_Ay if s.is_positive]
    residuals["cancellation_requires_Ay_half"] = sp.simplify(cancel_Ay[0] - sp.Rational(1, 2)) if cancel_Ay else sp.Integer(1)

    # (9) axial deformation OSCILLATION is 4th-order (numerator untouched at 2nd order).
    #     Bond chord length under midspan transverse displacement y(t)=y0 sin(wt):
    #     L(t) = sqrt(ell^2 + y(t)^2) ~ ell + y(t)^2/(2 ell). The AXIAL strain oscillation about
    #     its own time-mean is L(t) - <L> = (y0^2/(2 ell))(sin^2 - <sin^2>). Its RMS^2 (the
    #     deformation amplitude^2 that would move the axial S-factor Q-point) is 4th-order in y0.
    L = sp.sqrt(ell**2 + (y0 * sp.sin(w * t)) ** 2)
    L2 = sp.series(L, y0, 0, 5).removeO()  # ell + y0^2 sin^2/(2 ell) - y0^4 sin^4/(8 ell^3) + ...
    L_mean = sp.integrate(L2, (t, 0, 2 * sp.pi / w)) / (2 * sp.pi / w)
    axial_osc = sp.expand(L2 - L_mean)  # the deformation OSCILLATION about the shifted rest length
    axial_osc_rms2 = sp.integrate(axial_osc**2, (t, 0, 2 * sp.pi / w)) / (2 * sp.pi / w)
    axial_osc_rms2 = sp.expand(sp.simplify(axial_osc_rms2))
    # leading order of the axial deformation-oscillation variance:
    axial_leading_order = sp.Poly(sp.series(axial_osc_rms2, y0, 0, 6).removeO(), y0).monoms()
    lowest_power = min(m[0] for m in axial_leading_order) if axial_leading_order else 0
    residuals["axial_osc_variance_is_4th_order"] = sp.Integer(0) if lowest_power >= 4 else sp.Integer(1)

    all_zero = all(bool(sp.simplify(r) == 0) for r in residuals.values())
    return {
        "residuals_all_zero": all_zero,
        "residuals": {k: str(v) for k, v in residuals.items()},
        "derived_factors": {
            "mean_sin2": "1/2 (DERIVED)",
            "S_taylor_coeff": "-1/(2 A_y^2) (DERIVED)",
            "soft_term": "-k_s <A_shear^2>/(2 A_y^2) = -k_s (y0/ell)^2/(4 A_y^2) [D1] (DERIVED, SOFTENING)",
            "stiff_term": "+k_a y0^2/ell^2 (DERIVED, STIFFENING, #529 Part-1)",
            "dD_over_k0_at_Ay1_D1": "+3/4 y0^2 (DERIVED -- NO cancellation at canonical yield)",
            "cancellation_condition": "A_y = 1/2 (KNIFE TELL: imported yield in a costume, NOT canon)",
            "axial_numerator": "S_axial y0-independent at 2nd order (axial deform oscillation 4th-order)",
        },
        "central_finding": (
            "At the canonical yield A_y=1 the traveling-wave denominator does NOT cancel: the geometric "
            "stiffening (+y0^2) dominates the saturation softening (-y0^2/4) by 4:1, so dD/k0=+3/4 y0^2. "
            "The traveling wave MOVES rho' (stiffens the denominator, rho' DOWN). Cancellation would "
            "require A_y=1/2, which is not the canonical yield -- NO theorem-cancellation at the physical "
            "operating point. The confined-mode asymmetry lives in the NUMERATOR (A_dc=sqrt(alpha) DC "
            "bias), not the hum."
        ),
    }


# ---------------------------------------------------------------------------------------
# (S2) PER-CHANNEL LOADING -- the axial numerator + the shear-adjacent denominator, both waves
# ---------------------------------------------------------------------------------------
def _mean_A_shear2(y0: float, dictionary: str, ell: float) -> float:
    """Time-averaged shear-channel deformation <A_shear^2> from the y0<->A_shear dictionary.

    The dictionary is UNDERDETERMINED by canon (prereg scope caveat b) -- both readings run
    (KEEP-BOTH). On srs ell=1 they COINCIDE; they diverge only if ell != 1.
      D1 (bond-angle):        A_shear = y0/ell  -> <A_shear^2> = (y0/ell)^2 / 2
      D2 (displacement-direct): A_shear = y0    -> <A_shear^2> = y0^2 / 2
    """
    if dictionary == "D1_angle":
        return (y0 / ell) ** 2 / 2.0
    if dictionary == "D2_displacement":
        return y0**2 / 2.0
    raise ValueError(f"unknown dictionary {dictionary!r}")


def channel_loading(y0: float, A_dc: float, dictionary: str, ell: float = 1.0,
                    k0: float = 1.0) -> dict:
    """The three per-channel remap inputs at FULL-KERNEL precision (not the truncated series),
    for a given transverse hum amplitude y0 and axial DC bias A_dc, under one dictionary.

    Per Grant 2026-07-05 (Q-point ruling), no-double-count:
      - NUMERATOR  (axial):  S_axial = saturation_factor(A_dc)  -- keyed on the DC deformation ONLY.
                             The hum y0 does NOT enter (axial deform oscillation 4th-order, S1 proof).
                             Radiation: A_dc=0 -> S_axial=1 (cold). Confined: A_dc=sqrt(alpha).
      - DENOMINATOR (shear-adjacent), TWO competing terms:
          soft:  k0 * S_shear, S_shear = saturation_factor(sqrt(<A_shear^2>))  -- <A^2>-keyed, SOFTENING.
                 The effective time-averaged shear stiffness under a <A>=0 hum with RMS^2=<A_shear^2>.
          stiff: +T/ell, T = resonant_tension_leading(y0) = (k0/ell) y0^2  -- geometric, STIFFENING,
                 the #529 Part-1 law IMPORTED (NOT re-derived). This is a STRESS -> denominator ONLY.

    Returns the pieces AND the assembled k_shear_eff = k0*S_shear + T/ell (the remap denominator).
    NB: S_shear is evaluated at the RMS deformation sqrt(<A_shear^2>) -- this is the full-kernel
    value the small-signal 2nd-order series (S1) approximates; the two are reconciled in PC-denominator.
    """
    # NUMERATOR -- axial S at the DC bias only (no-double-count; hum excluded)
    S_axial = float(saturation_factor(A_dc, yield_limit=A_Y))

    # DENOMINATOR soft -- shear S at the time-averaged RMS deformation of the transverse hum
    A_shear_rms = float(np.sqrt(_mean_A_shear2(y0, dictionary, ell)))
    S_shear = float(saturation_factor(A_shear_rms, yield_limit=A_Y))

    # DENOMINATOR stiff -- the #529 Part-1 geometric tension (IMPORTED), a STRESS
    T = float(resonant_tension_leading(y0, k_a=k0, ell=ell))  # = (k0/ell) y0^2

    k_shear_eff = k0 * S_shear + T / ell
    rho_prime = (S_axial / k_shear_eff) if k_shear_eff > 0 else float("inf")
    return {
        "y0": y0, "A_dc": A_dc, "dictionary": dictionary, "ell": ell,
        "A_shear_rms": A_shear_rms,
        "S_axial_numerator": S_axial,
        "S_shear_soft": S_shear, "k_shear_soft": k0 * S_shear,
        "T_stiff": T, "T_over_ell_stiff": T / ell,
        "k_shear_eff_denominator": k_shear_eff,
        "rho_prime": rho_prime,
    }


# ---------------------------------------------------------------------------------------
# (S3) THE PUMP-NULL CONSISTENCY GATE -- reproduce #529's uniform scalar <T> BEFORE channel-resolved
# ---------------------------------------------------------------------------------------
def consistency_gate_529(pos, bonds, rho, theta: float = 0.3, y0: float = 1.0,
                         ell: float = 1.0) -> dict:
    """THE PUMP-NULL CONSISTENCY GATE (prereg Requirement 3): before going channel-resolved, the
    framework MUST reproduce #529's finding -- the per-bond scalar <T> is UNIFORM and IDENTICAL for
    both wave types, = (k_a/ell) y0^2.

    HARD reconcile via the #528 helper ONLY: my channel-resolved stiff term T (the denominator's
    geometric piece, = resonant_tension_leading) vs the imported field_from_abcd_propagation
    (#529's genuinely Gamma-free ABCD-propagated traveling-wave field -- a DIFFERENT code path I do
    NOT reimplement). If they disagree I have a bookkeeping error, not a result: DISCREPANT-HALT.

    The can-fire self-test runs FIRST (enforce(prove_first=True)) on THIS real data pair -- the
    #521/#526/#527 dead-gate defect cannot recur. The independent reference is field-space ABCD
    propagation, NOT the defining identity T=(k_a/ell)y0^2 (that would be the #527 defect); the two
    are different assemblies that must agree the traveling wave carries the SAME uniform <T>.
    """
    # my channel-resolved stiff term (the T that enters the denominator), a per-bond scalar
    my_T = float(resonant_tension_leading(y0, k_a=1.0, ell=ell))  # = (k_a/ell) y0^2

    # the #529 Gamma-free path: propagate a pure forward wave through cascaded ABCD segments and read
    # the per-bond mean <T> from the FIELD directly (a genuinely independent assembly).
    ref = field_from_abcd_propagation(theta, y0=y0, ell=ell)
    ref_T = float(ref["T_bond_mean"])

    gate = ReconcileGate(
        label="PC-consistency-529-uniform-T",
        claimed=my_T,
        independent=ref_T,   # value (not the defining identity) from the ABCD field path
        rtol=1e-9,
    )
    res = gate.enforce(prove_first=True)   # can-fire self-test on THIS pair, THEN DISCREPANT-HALT

    return {
        "my_stiff_T_per_bond": my_T,
        "ref_field_from_abcd_T_bond_mean": ref_T,
        "reconciled": res.reconciled,
        "can_fire_proven": res.can_fire_proven,
        "max_rel_discrepancy": res.max_rel_discrepancy,
        "note": (
            "Reproduces #529: the per-bond scalar <T> is uniform (=(k_a/ell)y0^2) and identical to the "
            "Gamma-free ABCD traveling-wave field's <T>. This is the scalar-carrier death (scalar T can't "
            "discriminate); the CHANNEL-resolved question (does the RATIO rho' move differently) is S4."
        ),
    }


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
