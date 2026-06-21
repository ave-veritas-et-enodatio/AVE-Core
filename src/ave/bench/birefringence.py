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
engineering scale from the validated #195 chiral-grid result.

Canonical leaves:
  manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md  (clm-pp3qwf)
  manuscript/ave-kb/common/engine-capability-map.md:44  (optical-activity +-75.462 deg/unit, #195)
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
    """AVE index shift, leading term only: delta_n ~ -(1/4)(E/E_YIELD)^2."""
    A = np.asarray(E, dtype=float) / E_YIELD
    return -C_AVE_LEADING * A**2


# ============================================================================
# QED RETARDANCE (Euler-Heisenberg one-loop; LITERATURE baseline)
# ============================================================================
def delta_n_qed(E: np.ndarray | float, a_eh: float = 7.0 / 45.0) -> np.ndarray:
    """QED Euler-Heisenberg index shift (LITERATURE): a_EH * alpha^2 * (E/E_CRIT)^2.

    The standard one-loop weak-field vacuum-birefringence form. a_eh defaults to
    the single-mode parallel coefficient 7/45. alpha^2-loop-suppressed against
    the Schwinger field E_CRIT.
    """
    return a_eh * ALPHA**2 * (np.asarray(E, dtype=float) / E_CRIT) ** 2


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
    """Field-INDEPENDENT retardance ratio delta_n_AVE/delta_n_QED = 1/(4 a_EH alpha^3).

    Both responses are E^2-leading, so the ratio is constant in E — the
    discriminator is the COEFFICIENT. Uses the substrate identity
    (E_CRIT/E_YIELD)^2 = 1/alpha (verified by substrate_identity_holds).
    """
    return 1.0 / (4.0 * a_eh * ALPHA**3)


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
