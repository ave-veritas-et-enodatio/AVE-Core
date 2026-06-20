"""apparatus.py — geometry -> per-node saturation amplitude, with FN breakdown ceiling.

FACTORED FROM: AVE-Core src/scripts/vol_4_engineering/qg42_vsign_deltaf.py
  - a_rms_local(g_geom, v_app, d_gap)            (qg42 :73-81)
  - G_geom = beta * Q_build decomposition        (qg42 :164-166)
  - j_fn(beta, e_gap) Fowler-Nordheim dark current (qg42 :122-129)
  - a_fn_safe_max() FN-safe local-A ceiling      (qg42 :132-139)
  - A_FN / B_FN / PHI_W / E_FN_SAFE_CEILING      (qg42 :113-119, LABELED inputs)
Cross-checked against: AVE-Core src/scripts/peer_review/experimental_noise_floor.py
  fowler_nordheim_current(V, d, beta, phi, A_emit) (:135-145).

Maps (geometry, drive voltage/field, gap) -> per-node saturation amplitude A_0,
with the DC field-emission breakdown onset as a hard-constraint helper.

The saturation amplitude A = E_local / E_YIELD is the local Axiom-4 quarter-arc
amplitude (qg42 :36). E_local = G_geom * V_app / d_gap, where the total
field-concentration G_geom = beta (geometric tip enhancement) * Q_build
(resonant field build-up). V_yield_apparatus = E_YIELD / G_geom is the applied
field that drives the per-node amplitude to A = 1 (the knee) — i.e. the
apparatus-scale voltage at which the LOCAL hot-spot reaches the per-node yield.

DISCIPLINE: E_YIELD imported from ave.core.constants (zero hardcoded SI yield
literals). The FN coefficients A_FN/B_FN/PHI_W/E_FN_SAFE_CEILING are LABELED
experimental inputs from the canonical experimental chapter
(17_noise_floor_boundary.tex), lifted verbatim from the qg42 exemplar
(:113-119); they are NOT AVE-derived physics and are tagged as such, matching
the exemplar's discipline note (qg42 :110-112).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core.constants import E_YIELD

# ----------------------------------------------------------------------------
# LABELED experimental inputs (NOT AVE-derived) — lifted verbatim from the qg42
# exemplar (:113-119), which itself reproduces 17_noise_floor_boundary.tex.
# These reproduce the canonical FN table (beta=3 SAFE, beta=6 MARGINAL,
# beta=50 DESTRUCTIVE) exactly. The experimental_noise_floor.py exemplar uses
# the identical A_FN/B_FN (:131-132).
# ----------------------------------------------------------------------------
A_FN: float = 1.54e-6   # A*eV/V^2          (17_noise_floor_boundary.tex:32)
B_FN: float = 6.83e9    # eV^-3/2 V/m       (same)
PHI_W: float = 4.5      # eV, tungsten work function (same)
# DC field-emission destruction caps the sustained local surface field at
# ~1.31e9 V/m (electropolished, beta~3, J_FN ~ 1.4e-18 A). This is the FN-safe
# DC surface-field ceiling per the tex table verdict (qg42 :116-119).
E_FN_SAFE_CEILING: float = 1.31e9   # V/m (DC surface field, electropolished beta~3)


@dataclass(frozen=True)
class ApparatusCoupling:
    """Geometry -> field-concentration mapping for a bench apparatus.

    Mirrors the qg42 PONDER operating-point decomposition (:164-166):
    G_geom = beta * Q_build, where beta is the geometric tip enhancement and
    Q_build is the resonant field build-up.

    Attributes
    ----------
    beta : float
        Geometric tip field-enhancement factor (beta = h/r for a tip; qg42 :164).
    q_build : float
        Resonant field build-up factor (qg42 :165). Set 1.0 for a DC / static
        apparatus with no resonant enhancement.
    d_gap : float
        Electrode gap [m].
    """

    beta: float
    q_build: float
    d_gap: float

    @property
    def g_geom(self) -> float:
        """Total field-concentration factor G_geom = beta * Q_build (qg42 :166)."""
        return self.beta * self.q_build

    def e_local(self, v_app: float) -> float:
        """Local hot-spot field E_local = G_geom * V_app / d_gap [V/m].

        This is the field after both geometric tip enhancement and resonant
        build-up (the E_local in qg42 :215).
        """
        return self.g_geom * v_app / self.d_gap

    def saturation_amplitude(self, v_app: float) -> float:
        """Per-node saturation amplitude A_0 = E_local / E_YIELD (qg42 :73-80, :36).

        A is the local Axiom-4 quarter-arc amplitude. A < 1 is the linear /
        nonlinear regime; A -> 1 is the knee.
        """
        return saturation_amplitude(self.g_geom, v_app, self.d_gap)

    def v_yield_apparatus(self) -> float:
        """Applied voltage driving the per-node amplitude to A = 1 (the knee).

        V_yield_apparatus = E_YIELD * d_gap / G_geom. At this applied voltage
        the LOCAL hot-spot field equals E_YIELD, so A = 1.
        """
        return v_yield_apparatus(self.g_geom, self.d_gap)

    def fn_dark_current_density(self, v_app: float) -> float:
        """Fowler-Nordheim dark-current density [A/m^2] at the macroscopic gap field.

        Uses the macroscopic gap field E_gap = V_app / d_gap with the tip
        enhancement beta (matches the qg42 j_fn(beta, e_gap) convention where
        e_gap is the macroscopic field and beta is applied inside; qg42 :122-129).
        """
        e_gap = v_app / self.d_gap
        return fn_dark_current(self.beta, e_gap)


def saturation_amplitude(g_geom: float, v_app: float, d_gap: float) -> float:
    """Local saturation amplitude A = G_geom * V_app / (d_gap * E_YIELD).

    FACTORED FROM qg42 a_rms_local (:73-81). A is the local Axiom-4 quarter-arc
    saturation amplitude (qg42 :36). G_geom = beta * Q_build is the total
    field-concentration factor.
    """
    return g_geom * v_app / (d_gap * E_YIELD)


def v_yield_apparatus(g_geom: float, d_gap: float) -> float:
    """Apparatus-scale yield voltage V = E_YIELD * d_gap / G_geom.

    The applied voltage at which the LOCAL hot-spot field reaches E_YIELD, i.e.
    the per-node saturation amplitude A = 1 (the knee). Inverse of
    saturation_amplitude at A = 1.
    """
    if g_geom == 0:
        raise ValueError("g_geom must be non-zero")
    return E_YIELD * d_gap / g_geom


def fn_dark_current(beta: float, e_gap: float) -> float:
    """Fowler-Nordheim dark-current density [A/m^2] (LABELED experimental input).

    FACTORED FROM qg42 j_fn (:122-129):
        J_FN = A_FN (beta E)^2 / phi * exp(-B_FN phi^1.5 / (beta E))
    Reproduces the 17_noise_floor_boundary.tex FN table. NOT an AVE prediction —
    the experimental field-emission breakdown ceiling, used as a hard constraint.

    Parameters
    ----------
    beta : float
        Field enhancement factor (geometric tip).
    e_gap : float
        Macroscopic gap field [V/m] (E_local = beta * e_gap).
    """
    b_e = beta * e_gap
    if b_e <= 0:
        return 0.0
    exponent = -B_FN * PHI_W**1.5 / b_e
    # Guard against underflow overflow (experimental_noise_floor.py:142 uses
    # the -700 cutoff; np.exp handles underflow to 0.0 cleanly here).
    if exponent < -700:
        return 0.0
    return float(A_FN * b_e**2 / PHI_W * np.exp(exponent))


def fn_safe_max_amplitude() -> float:
    """Max FN-safe local saturation amplitude A_max = E_FN_SAFE_CEILING / E_YIELD.

    FACTORED FROM qg42 a_fn_safe_max (:132-139). The DC field-emission
    destruction limit caps the sustained local surface field at the FN-safe
    ceiling; the corresponding A is the hard constraint on any DC-enhancement
    architecture.
    """
    return E_FN_SAFE_CEILING / E_YIELD


def fn_safe(beta: float, e_gap: float, j_threshold: float = 1.0e-18 / 1.0) -> bool:
    """Whether the local field is below the FN-safe DC surface-field ceiling.

    Hard-constraint helper: returns True if E_local = beta * e_gap is at or
    below E_FN_SAFE_CEILING (the electropolished beta~3 verdict, qg42 :116-119).
    The j_threshold parameter is accepted for callers that prefer a
    current-density gate, but the canonical gate is the field ceiling.
    """
    return (beta * e_gap) <= E_FN_SAFE_CEILING
