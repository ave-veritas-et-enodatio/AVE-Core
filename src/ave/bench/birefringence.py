"""birefringence.py — vacuum-birefringence bench physics: AVE vs QED.

The forward physics layer for the vacuum-birefringence bench-model gate (the
testing-pivot "bankable number"). Three observables, all forward from
``ave.core.constants`` (no fit, no free parameter, no inverse-solve):

  1. AVE RETARDANCE      delta_n_ave(E)  — the Axiom-4 saturating-permittivity
                         index shift  delta_n = sqrt(S) - 1 = (1 - A^2)^(1/4) - 1,
                         A = E/E_YIELD. NEGATIVE (vacuum softens), E^2-LEADING
                         (NOT E^4 — the historical E^4 framing was a sqrt(eps)
                         conflation, retracted; see vacuum-birefringence-e4.md:20
                         and birefringence_coefficient_discriminator.py).

  2. QED RETARDANCE      delta_n_qed(E)  — the Euler-Heisenberg one-loop vacuum
                         birefringence,  delta_n = a_EH * alpha^2 * (E/E_CRIT)^2,
                         the PVLAS/BMV baseline. Also E^2-LEADING. The PVLAS
                         vacuum magnetic birefringence constant A_e is the
                         validate-on-known anchor (recovers 1.32e-24 T^-2).

  3. AVE OPTICAL-ACTIVITY ROTATION  theta_ave(L) — the PARITY-ODD polarization-
                         plane twist of the chiral srs (I4_1 32) lattice
                         (def-0pt1ac; +-75.462 deg/unit, #195). This is the
                         CLEANEST discriminator: QED vacuum produces ZERO
                         polarization rotation (parity-even), so a NONZERO,
                         enantiomorph-sign-flipping rotation is AVE-distinct with
                         no QED counterpart.

DISCRIMINATOR SUMMARY (ave-discrimination-check, SM-counterfactual per channel):
  retardance   : both AVE and QED give an E^2-leading delta_n; the discriminator
                 is the COEFFICIENT (AVE O(1)/4 vs QED a_EH*alpha^2), a
                 field-INDEPENDENT ratio ~1/(4 a_EH alpha^3) ~ 10^6. QED-counter:
                 a same-coefficient delta_n.
  rotation     : AVE predicts a nonzero parity-odd rotation theta != 0 with a
                 SIGN that flips between lattice enantiomorphs and is ZERO on the
                 achiral control; QED predicts theta == 0 IDENTICALLY (no vacuum
                 optical activity). QED-counter: theta == 0. This is the
                 zero-vs-nonzero discriminator, the strongest kind.

CONSISTENCY-VS-EMERGENCE (per-observable classification):
  delta_n_ave FORM (E^2-leading, sqrt-S kernel)  : MANIFESTATION of Axiom 4.
  delta_n_ave COEFFICIENT (-1/4)                 : MANIFESTATION (O(1), kernel-set).
  rotation FORM (parity-odd, sign-flips, achiral-null) : MANIFESTATION of the
                 chiral I4_1 32 space group (Axiom 1) — AVE-distinct CHORD.
  rotation MAGNITUDE (deg per length)            : the bare-lattice rate rides a
                 tagged engineering scale (ETA_ROT_PER_WRITHE) and the lattice
                 writhe density; it is NOT a forced number — reported as a band /
                 bare-lattice ceiling, never headlined as a pinned coefficient
                 (the magnitude rides the alpha-echo family, ave-evidence-framing).
  delta_n_qed                                    : NON-AVE LITERATURE BASELINE.
  A_e (1.32e-24 T^-2 recovery)                   : VALIDATE-ON-KNOWN (recover the
                 PVLAS textbook constant or the model is wrong; HALT).

DISCIPLINE: every AVE physical constant imported from ave.core.constants. The
QED Euler-Heisenberg prefactor band (a_EH) and the PVLAS A_e closed form are
LABELED non-AVE literature inputs (Heisenberg-Euler 1936; Rizzo/PVLAS), NOT
AVE-derived and NOT fit. The optical-activity bare-lattice rate is a tagged
engineering scale (ETA_ROT_PER_WRITHE); the +-75.46 deg/unit #195 magnitude is
an engineering decree, NOT a derived/bankable transport (demoted PR #374 — the
substrate-DERIVED bulk g0 = the 4_1 screw pitch, geometric; k->0 continuum
mapping PENDING). The QUALITATIVE chiral-grid facts (signed / enantiomorph-odd /
diamond-null / writhe-sourced / lossless reciprocal gyrator) stay SOLID.

Canonical leaves:
  manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md  (clm-pp3qwf)
  manuscript/ave-kb/common/engine-capability-map.md:44  (optical-activity +-75.46 deg/unit #195 magnitude DEMOTED to ETA-decree engineering scale, PR #374)
  manuscript/ave-kb/common/vocabulary-register.md:522   (def-0pt1ac optical-activity fence)
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core.constants import (
    ALPHA,
    C_0,
    E_CRIT,
    E_YIELD,
    HBAR,
    L_NODE,
    M_E,
    MU_0,
    e_charge,
)

# ----------------------------------------------------------------------------
# NON-AVE LITERATURE INPUTS (the only non-AVE numbers in this module).
# ----------------------------------------------------------------------------
# QED Euler-Heisenberg weak-field vacuum-birefringence prefactor band a_EH in
#   delta_n_QED = a_EH * alpha^2 * (E / E_CRIT)^2.
# Standard single-mode values (Heisenberg-Euler 1936; the forms quoted for
# PVLAS/BMV magnetic birefringence, translated to a static electric field via
# the B -> E/c energy-density equivalence, c*B_crit == E_CRIT exactly):
#   parallel mode      n_par  - 1 = (7/45) alpha^2 (E/E_crit)^2
#   perpendicular mode n_perp - 1 = (4/45) alpha^2 (E/E_crit)^2
#   differential       n_par - n_perp = (3/45) alpha^2 (E/E_crit)^2
# The PVLAS differential A_e form (below) corresponds to an effective
# a_EH = 3 A_e B_crit^2 / alpha^2 ~ 1.454 (the "order-of-magnitude EH"
# convention flagged in research/2026-06-04_birefringence-coefficient-prereg.md
# section 5.2). Both conventions are surfaced; physics verdict is identical.
A_EH_LITERATURE: dict[str, float] = {
    "single-mode parallel  (7/45)": 7.0 / 45.0,
    "single-mode perp      (4/45)": 4.0 / 45.0,
    "differential birefr.  (3/45)": 3.0 / 45.0,
    "PVLAS A_e differential (~1.45)": 3.0
    * (2.0 * ALPHA**2 * HBAR**3 / (45.0 * MU_0 * M_E**4 * C_0**5))
    * (M_E**2 * C_0**2 / (e_charge * HBAR)) ** 2
    / ALPHA**2,
}

# AVE index-shift leading coefficient: delta_n ~ -(1/4) A^2  =>  |c_AVE| = 1/4.
C_AVE_LEADING: float = 0.25

# Optical-activity bare-lattice rate (TAGGED ENGINEERING SCALE, not a forced
# number). The validated chiral srs grid gives a Bishop-frame polarization-plane
# rotation of +-75.462 deg per lattice node-span on the bare chiral vacuum
# (#195, def-0pt1ac). Sign flips between enantiomorphs; identically zero on the
# achiral diamond control. We expose it as deg-per-node and deg-per-metre
# (dividing by L_NODE) so a bench path-length can be applied; the magnitude is a
# bare-lattice CEILING (the bench-realizable chirality density is apparatus-set
# and unpinned), the FORM (parity-odd, sign-flipping, achiral-null) is the
# AVE-distinct content.
OPTICAL_ACTIVITY_DEG_PER_NODE: float = 75.462


@dataclass(frozen=True)
class BirefringencePoint:
    """A single (field, observable) point of the bench model.

    Attributes
    ----------
    E : float
        Applied / probe electric field [V/m].
    A : float
        Per-node saturation amplitude A = E / E_YIELD (dimensionless).
    dn_ave : float
        AVE retardance index shift (negative; full sqrt-S arc).
    dn_ave_leading : float
        AVE retardance, leading term -1/4 A^2.
    dn_qed : float
        QED Euler-Heisenberg retardance at the reference a_EH.
    ratio : float
        |dn_ave| / dn_qed (the coefficient discriminator, ~10^6).
    """

    E: float
    A: float
    dn_ave: float
    dn_ave_leading: float
    dn_qed: float
    ratio: float


# ============================================================================
# AVE RETARDANCE (Axiom-4 saturating permittivity; E^2-leading)
# ============================================================================
def delta_n_ave_exact(E: np.ndarray | float) -> np.ndarray:
    """AVE index shift from the FULL Axiom-4 kernel: delta_n = (1 - A^2)^(1/4) - 1.

    A = E / E_YIELD. The wave-speed identity n = sqrt(eps_eff/eps0) = sqrt(S) on
    the universal saturation kernel S = sqrt(1 - A^2) (eps strained, mu = mu0).
    Negative (the vacuum softens, n drops), E^2-leading. Returns NaN where
    A >= 1 (past yield, the optical observable is undefined).

    NUMERICAL PRECISION (the small-A catastrophic-cancellation guard): the naive
    (1 - A^2)^(1/4) - 1 loses all significant digits for A << 1 (it subtracts two
    near-1 floats and underflows to 0.0 well before the physical signal vanishes
    — e.g. at A ~ 1e-8 the true shift is ~ -2.5e-17 but the naive form returns
    0.0). We evaluate it as expm1(0.25 * log1p(-A^2)), exact to machine precision
    across A in [0, 1) — this is what makes the small-field (lab-magnet, weak-E)
    entries non-zero and trustworthy rather than a spurious 0.
    """
    A2 = (np.asarray(E, dtype=float) / E_YIELD) ** 2
    # Clamp the log1p argument away from -1 in the past-yield branch (A2 >= 1)
    # so np.where's unused branch does not emit a domain RuntimeWarning; the
    # result there is overwritten by NaN regardless.
    safe = np.where(A2 < 1.0, A2, 0.0)
    return np.where(A2 < 1.0, np.expm1(0.25 * np.log1p(-safe)), np.nan)


def delta_n_ave_leading(E: np.ndarray | float) -> np.ndarray:
    """AVE ISOTROPIC single-arm index shift, leading term: delta_n_iso ~ -(1/4)(E/E_YIELD)^2.

    NOTE: this is the COMMON-MODE shift a birefringence instrument rejects, not
    the falsifier observable. For the par-perp birefringence use
    delta_n_ave_differential (the falsifier observable, -1/2 A^2).
    """
    A = np.asarray(E, dtype=float) / E_YIELD
    return -C_AVE_LEADING * A**2


def delta_n_ave_differential_exact(E: np.ndarray | float) -> np.ndarray:
    """AVE par-perp BIREFRINGENCE delta_n_bir = n_par - n_perp (FALSIFIER observable).

    Under a linearly-polarized pump the scalar Ax-4 kernel becomes a uniaxial
    probe tensor eps_ij = eps delta_ij + 2 eps' E0_i E0_j (optic axis || pump;
    eps' = d eps / d(E^2)). The two eigen-indices are
        n_perp = sqrt(S)         = (1 - A^2)^(1/4),
        n_par  = sqrt(S - A^2/S) = sqrt((1 - 2 A^2) / sqrt(1 - A^2)),
    and the birefringence the polarimeter measures is their DIFFERENCE
        delta_n_bir = n_par - n_perp  ->  -(1/2) A^2 to leading order
    (exactly 2x the isotropic single-arm shift; DERIVED, OQ-1 Step 1). Returns
    NaN past yield (A^2 >= 1/2 for n_par, A^2 >= 1 for n_perp).
    """
    A2 = (np.asarray(E, dtype=float) / E_YIELD) ** 2
    safe1 = np.where(A2 < 1.0, A2, 0.0)
    S = np.sqrt(1.0 - safe1)
    n_perp = np.where(A2 < 1.0, np.sqrt(S), np.nan)
    par_arg = np.where(A2 < 0.5, (1.0 - 2.0 * safe1) / S, np.nan)
    n_par = np.where(A2 < 0.5, np.sqrt(par_arg), np.nan)
    return n_par - n_perp


def delta_n_ave_differential(E: np.ndarray | float) -> np.ndarray:
    """AVE par-perp birefringence, leading term: delta_n_bir ~ -(1/2)(E/E_YIELD)^2.

    The matched falsifier observable (exactly 2x the isotropic single-arm
    delta_n_ave_leading). DERIVED from the uniaxial probe tensor (OQ-1 Step 1).
    """
    A = np.asarray(E, dtype=float) / E_YIELD
    return -0.5 * A**2


# ============================================================================
# QED RETARDANCE (Euler-Heisenberg one-loop; LITERATURE baseline)
# ============================================================================
def delta_n_qed(E: np.ndarray | float, a_eh: float = 7.0 / 45.0) -> np.ndarray:
    """QED Euler-Heisenberg index shift (LITERATURE): a_EH * alpha^2 * (E/E_CRIT)^2.

    The standard one-loop weak-field vacuum-birefringence form. a_eh defaults to
    the single-mode parallel coefficient 7/45. alpha^2-loop-suppressed against
    the Schwinger field E_CRIT.

    ==== NORMALIZATION CORRECTION (2026-07-03) — READ BEFORE USING FOR PREDICTION ====
    The a_eh = 3/45 = 0.0667 DIFFERENTIAL convention this function was called with
    in the birefringence-campaign drivers is UNDERSTATED by exactly 1/(2*pi*alpha)
    = 21.81 relative to the module's OWN PVLAS-anchored magnetic leg
    (delta_n_qed_magnetic, whose A_e recovers the textbook 1.32e-24 T^-2). At the
    E<->cB duality point the leading Euler-Heisenberg (E^2-B^2)^2 invariant gives
    IDENTICAL differentials, so delta_n_qed(E_crit, 3/45) MUST equal
    delta_n_qed_magnetic(B_crit) -- it does not (3.55e-6 vs 7.74e-5). The bug is in
    the module comment's "B -> E/c translation": that translation gives the
    A_e-derived coefficient alpha/(30*pi) = 1.454*alpha^2, NOT 3/45. The
    arbiter-validated electric leg is delta_n_qed_electric_pvlas() below; use THAT
    for any prediction. This raw a_eh form is retained for the historical/traceability
    calls and for the single-mode 7/45, 4/45 bracket coefficients only.
    """
    return a_eh * ALPHA**2 * (np.asarray(E, dtype=float) / E_CRIT) ** 2


def delta_n_qed_electric_pvlas(E: np.ndarray | float, *, geometry: str = "propagating") -> np.ndarray:
    """QED electric-field vacuum-birefringence differential, ANCHORED to the PVLAS
    magnetic leg (the arbiter-validated normalization; corrects the 3/45 leg).

    Two external arbiters pin this coefficient (2026-07-03 reconciliation):
      (a) PVLAS A_e cross-check via E<->cB duality. The magnetic differential is
          3 A_e B^2; at B=B_crit it equals 3 A_e B_crit^2 = alpha/(30*pi)
          = 1.454*alpha^2 (analytic; A_e recovers 1.32e-24 T^-2). The leading
          Euler-Heisenberg (E^2-B^2)^2 invariant is E<->cB symmetric, so the
          STATIC-E differential coefficient equals the magnetic one:
              delta_n_static = (alpha/(30*pi)) (E/E_crit)^2.
      (b) The BIREF@HIBEF LoI Eq.19 focus form N'/N = (4 alpha^2/225)(I_L/I_S)^2
          (z/lambda)^2 reproduces to ~1e-12 at 1e21 W/cm^2 and implies, for a
          PROPAGATING plane-wave pump (E and B co-moving, BOTH invariants active),
          a differential a FACTOR 2 larger:
              delta_n_propagating = (alpha/(15*pi)) (E/E_crit)^2.

    geometry="propagating" (default) returns the LoI-matched plane-wave value
    alpha/(15*pi) -- the correct value for a HIBEF-type optical pump and the
    CONSERVATIVE (larger-QED) choice. geometry="static" returns the pure-static-E
    duality value alpha/(30*pi) (the PVLAS-magnetic-matched number).

    LABELED non-AVE literature closed form; NOT an AVE prediction.
    """
    if geometry == "propagating":
        coeff = ALPHA / (15.0 * np.pi)
    elif geometry == "static":
        coeff = ALPHA / (30.0 * np.pi)
    else:
        raise ValueError(f"geometry must be 'propagating' or 'static', got {geometry!r}")
    return coeff * (np.asarray(E, dtype=float) / E_CRIT) ** 2


def vacuum_magnetic_birefringence_constant() -> float:
    """The PVLAS vacuum MAGNETIC birefringence constant A_e [T^-2].

    Closed form A_e = 2 alpha^2 hbar^3 / (45 mu0 m_e^4 c^5). This is the
    VALIDATE-ON-KNOWN anchor: it must recover the textbook A_e ~ 1.32e-24 T^-2
    (PVLAS/Rizzo). The magnetic differential shift is delta_n = 3 A_e B^2.
    LABELED non-AVE literature closed form (built from CODATA constants in
    ave.core.constants), NOT an AVE prediction.
    """
    return 2.0 * ALPHA**2 * HBAR**3 / (45.0 * MU_0 * M_E**4 * C_0**5)


def delta_n_qed_magnetic(B: np.ndarray | float) -> np.ndarray:
    """QED Euler-Heisenberg MAGNETIC differential birefringence: 3 A_e B^2.

    The PVLAS/BMV observable (B in Tesla). delta_n = 3 A_e B^2 with A_e the
    vacuum magnetic birefringence constant. LITERATURE baseline.
    """
    A_e = vacuum_magnetic_birefringence_constant()
    return 3.0 * A_e * np.asarray(B, dtype=float) ** 2


# ============================================================================
# AVE OPTICAL-ACTIVITY ROTATION (parity-odd; the clean QED-zero discriminator)
# ============================================================================
def optical_activity_rate_deg_per_m(handedness: str = "right") -> float:
    """Bare-lattice optical-activity (gyrotropy) rate [deg/m].

    The validated chiral srs Bishop-frame rotation is +-75.462 deg per lattice
    node-span (#195, def-0pt1ac). Converting per-node to per-metre divides by
    L_NODE. handedness 'right' -> +, 'left' -> -, sign-flipping between
    enantiomorphs (the parity-odd signature). This is a bare-lattice CEILING
    (full-chirality vacuum); the bench-realizable rate rides the apparatus
    chirality density and is unpinned.
    """
    sign = +1.0 if handedness == "right" else -1.0
    return sign * OPTICAL_ACTIVITY_DEG_PER_NODE / L_NODE


def optical_activity_rotation_deg(
    path_length_m: float, handedness: str = "right", *, chirality_fraction: float = 1.0
) -> float:
    """Accumulated optical-activity rotation [deg] over a probe path.

    theta = (rate_deg_per_m) * path_length * chirality_fraction.

    chirality_fraction (default 1.0 = bare full-chirality lattice CEILING) is the
    fraction of the bare-lattice writhe density the apparatus realizes; it is an
    explicit, unpinned apparatus parameter (NOT an AVE-forced number). The
    parity-odd FORM (theta != 0, sign-flips with handedness, zero for the achiral
    control) is the AVE-distinct content; QED predicts theta == 0 identically.
    """
    rate = optical_activity_rate_deg_per_m(handedness)
    return rate * path_length_m * chirality_fraction


def optical_activity_rotation_qed(path_length_m: float) -> float:
    """QED vacuum optical-activity rotation [deg] — IDENTICALLY ZERO.

    QED vacuum is parity-even: no natural optical activity, no polarization-plane
    rotation under a static field (only retardance/ellipticity). This is the
    SM-counterfactual for the rotation channel: theta_QED == 0 at any path
    length. A measured nonzero, enantiomorph-sign-flipping rotation has NO QED
    explanation.
    """
    return 0.0 * path_length_m


# ============================================================================
# CROSSOVER / COEFFICIENT DISCRIMINATOR
# ============================================================================
def coefficient_ratio(a_eh: float = 7.0 / 45.0) -> float:
    """Field-INDEPENDENT SINGLE-ARM retardance ratio delta_n_AVE_iso/delta_n_QED.

    The AVE SCALAR single-arm (isotropic) index shift delta_n_iso ~ -(1/4) A^2
    over the QED single-mode coefficient a_eh:
        delta_n_AVE_iso / delta_n_QED = 1 / (4 a_EH alpha^3).
    Both responses are E^2-leading, so the ratio is constant in E.

    NOTE (FLAG-A adjudicated 2026-06-21): this is the ISOTROPIC single-arm
    comparison, NOT the falsifier headline. A birefringence instrument measures
    the par-perp DIFFERENTIAL (use coefficient_ratio_differential), which rejects
    the common-mode isotropic shift. coefficient_ratio(7/45) ~ 4.14e6 pairs the
    AVE single-arm against the QED PARALLEL single-mode (mismatched observables);
    it is retained for traceability only. Uses the substrate identity
    (E_CRIT/E_YIELD)^2 = 1/alpha (verified by substrate_identity_holds).
    """
    return 1.0 / (4.0 * a_eh * ALPHA**3)


def coefficient_ratio_differential() -> float:
    """Field-INDEPENDENT MATCHED par-perp DIFFERENTIAL ratio (SUPERSEDED value).

    ==== SUPERSEDED (2026-07-03) — this returns the WRONG-NORMALIZATION 7.5/alpha^3.
    The QED denominator (3/45) alpha^2 is understated by 1/(2*pi*alpha) = 21.81
    (see delta_n_qed correction note). The corrected, arbiter-validated ratio is
    coefficient_ratio_differential_pvlas() below. This function is retained ONLY so
    historical callers do not break; do NOT use its value in any prediction. ====

    AVE differential delta_n_bir = n_par - n_perp ~ -(1/2) A^2  (DERIVED; UNAFFECTED
    by the correction). Paired against the understated QED (3/45) alpha^2 it gave
        (1/2) / ((3/45) alpha^2) * (E_CRIT/E_YIELD)^2 = 7.5/alpha^3 ~ 1.93e7 (WRONG).
    """
    return (0.5 / ((3.0 / 45.0) * ALPHA**2)) * (E_CRIT / E_YIELD) ** 2


def coefficient_ratio_differential_pvlas(*, geometry: str = "propagating") -> float:
    """Field-INDEPENDENT MATCHED par-perp DIFFERENTIAL ratio (CORRECTED, arbiter-anchored).

    The AVE differential (numerator) is UNCHANGED: delta_n_bir ~ -(1/2) A^2, whose
    coefficient of (E/E_crit)^2 is (1/2)(E_crit/E_yield)^2 = 1/(2 alpha) (substrate
    identity (E_crit/E_yield)^2 = 1/alpha).

    The QED denominator is the PVLAS-anchored electric leg
    (delta_n_qed_electric_pvlas):
        propagating (LoI-matched, default): alpha/(15*pi) (E/E_crit)^2
            => ratio = [1/(2 alpha)] / [alpha/(15 pi)] = 15*pi/(2 alpha^2)
                     = 7.5*pi/alpha^2 ~ 4.42e5.
        static (PVLAS-magnetic-matched):    alpha/(30*pi) (E/E_crit)^2
            => ratio = 15*pi/alpha^2 ~ 8.85e5.

    The FORM (tree-O(1)/2 saturation vs an alpha^2 loop) is the AVE-distinct chord;
    the MAGNITUDE is an alpha-echo (symmetric standard: QED is equally alpha-rooted).
    Falsifier LOGIC unchanged: AVE ~7 OOM above the polarimeter floor, corrected QED
    still ~4 OOM below it.
    """
    ave_num = 0.5 * (E_CRIT / E_YIELD) ** 2  # = 1/(2 alpha)
    if geometry == "propagating":
        qed_coeff = ALPHA / (15.0 * np.pi)
    elif geometry == "static":
        qed_coeff = ALPHA / (30.0 * np.pi)
    else:
        raise ValueError(f"geometry must be 'propagating' or 'static', got {geometry!r}")
    return ave_num / qed_coeff


def substrate_identity_holds() -> bool:
    """Verify the substrate identity (E_CRIT/E_YIELD)^2 == 1/alpha (the ratio
    collapse). Also c*B_crit == E_CRIT. Returns True if both hold."""
    B_crit = M_E**2 * C_0**2 / (e_charge * HBAR)
    return bool(
        np.isclose((E_CRIT / E_YIELD) ** 2, 1.0 / ALPHA)
        and np.isclose(C_0 * B_crit, E_CRIT)
    )


def bench_point(E: float, a_eh: float = 7.0 / 45.0) -> BirefringencePoint:
    """Assemble a single BirefringencePoint at field E [V/m]."""
    dn_ave = float(delta_n_ave_exact(E))
    dn_lead = float(delta_n_ave_leading(E))
    dn_q = float(delta_n_qed(E, a_eh))
    ratio = abs(dn_ave) / dn_q if dn_q > 0 else float("inf")
    return BirefringencePoint(
        E=float(E),
        A=float(E / E_YIELD),
        dn_ave=dn_ave,
        dn_ave_leading=dn_lead,
        dn_qed=dn_q,
        ratio=ratio,
    )
