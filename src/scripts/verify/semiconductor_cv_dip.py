"""Semiconductor device-analysis techniques mapped onto the vacuum cell (Task #17).

CONSISTENCY-class re-expression of the Axiom-4 kernel + varactor canon in
device-physics (BJT/MOSFET/GaN) vocabulary. Originates NO new dimensionful
number; every value is imported from ``ave.core.constants``.

REGIME: cold lattice, quasi-static HELD bias, small-signal probe;
Ax3-lossless below the pair-production threshold.

The vacuum cell carries TWO orthogonal capacitances (A1 perp T2,
``master-equation.md``:20; the Grant-ratified sector split, ``CLAUDE.md``:73):

  - A1 longitudinal bond compliance  C_eff = C0 / S(V/V_snap),  DIVERGES at
    V_snap = m_e c^2 / e ~= 511 kV  (nonlinear-vacuum-capacitance.md:18).
    Device reading: turn-on / channel-inversion capacitance (pair production
    IS channel formation).

  - T2 transverse dielectric  eps_eff = eps0 * S(V/V_yield),  ROLLS OFF to
    zero at V_yield = sqrt(alpha) * V_snap ~= 43.65 kV.
    Device reading: reverse-biased depletion varactor (polarization runs out).

The pair (V_snap : V_yield) maps to a MOSFET (V_th : V_BD,ox).

Deliverables (see research/2026-07-07_semiconductor-cv-dip_RESULT.md):
  (a) operational definitions (chord/secant vs tangent dQ/dV) for A1 and T2
  (b) the vacuum C-V datasheet curve (this driver's figure)
  (c) the perp/parallel eigenmode check vs the birefringence Letter (sympy)
  (d) network composition across the K4 z=3 series-L / shunt-C ladder
  (e) split C-V (terminal-pair selection separating T2 pol. from A1 compliance)
  (f) frequency dispersion (posed, not forced)
  (g) technique-transfer table

Run:  PYTHONPATH=src python src/scripts/verify/semiconductor_cv_dip.py
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import ALPHA, V_SNAP, V_YIELD

# =============================================================================
# section 1: canonical kernel + the two sector capacitances
# =============================================================================
# The single Axiom-4 quarter-arc kernel S(A) = sqrt(1 - A^2) governs BOTH
# sectors; they differ only in which voltage keys the argument A.


def kernel_S(a: np.ndarray | float) -> np.ndarray:
    """Axiom-4 saturation kernel S(A) = sqrt(1 - A^2), A = V/V_key.

    Returns NaN above rupture (|A| > 1) — the medium ceases to support the
    reactance (Regime IV). This is honest: the kernel has no real value there.
    """
    a = np.asarray(a, dtype=float)
    inside = 1.0 - a**2
    return np.where(inside >= 0.0, np.sqrt(np.abs(inside)), np.nan)


def a1_argument(v: np.ndarray | float) -> np.ndarray:
    """A1 longitudinal bond-compliance kernel argument A = V / V_snap.

    A1 keys on V_snap (nonlinear-vacuum-capacitance.md:18) — NEVER V_yield.
    """
    return np.asarray(v, dtype=float) / V_SNAP


def t2_argument(v: np.ndarray | float) -> np.ndarray:
    """T2 transverse-permittivity kernel argument A_V = V / V_yield.

    T2 keys on V_yield (the Cosserat self-trap wall, def-vyvsn1) — NEVER V_snap.
    """
    return np.asarray(v, dtype=float) / V_YIELD


# =============================================================================
# section 2: operational definitions — chord/secant vs tangent dQ/dV
# =============================================================================
# Device physics pins a capacitance BY THE MEASUREMENT. Two distinct objects:
#   - CHORD / SECANT (large-signal)  : the constitutive value C = Q/V at bias.
#   - TANGENT (small-signal)          : the differential C_ss = dQ/dV at bias.
# The C-V *definition* crowns the TANGENT as "the small-signal capacitance"
# (device-circuit-models.md:60, A1-scoped; round-3 RESULT for T2).


# ---- A1 longitudinal bond compliance (keyed V_snap) ----
# Constitutive charge on the A1 bond:  Q_A1(V) = C0 * V / S(V/V_snap)
# (the compliance C0/S DIVERGES as V -> V_snap).


def a1_chord_over_c0(v: np.ndarray | float) -> np.ndarray:
    """A1 large-signal chord/secant compliance  C_chord/C0 = 1 / S(V/V_snap).

    device-circuit-models.md:60 verbatim: "the large-signal chord/secant
    varactor C_eff = C0/S". Diverges at V_snap ~= 511 kV.
    """
    return 1.0 / kernel_S(a1_argument(v))


def a1_tangent_over_c0(v: np.ndarray | float) -> np.ndarray:
    """A1 small-signal tangent compliance  C_ss/C0 = dQ/dV = 1 / S(V/V_snap)^3.

    device-circuit-models.md:60 verbatim: "the small-signal differential
    C_ss = dQ/dV = C0/S^3". This is THE small-signal compliance (crowned).
    d/dV [ V / S(V/V_snap) ] = 1/S^3   (sympy-verified in the RESULT).
    """
    s = kernel_S(a1_argument(v))
    return 1.0 / s**3


# ---- T2 transverse permittivity (keyed V_yield) ----
# Constitutive displacement on the T2 channel: D(V) ~ eps0 * S(V/V_yield) * V.
# The permittivity eps_eff = eps0 * S ROLLS OFF to zero at V_yield.


def t2_chord_over_eps0(v: np.ndarray | float) -> np.ndarray:
    """T2 large-signal chord permittivity  eps_chord/eps0 = S(V/V_yield).

    The constitutive value (round-3 RESULT: chord C0*S(A0) -> leading 1-1/2 A0^2).
    Rolls off to 0 at V_yield ~= 43.65 kV.
    """
    return kernel_S(t2_argument(v))


def t2_tangent_over_eps0(v: np.ndarray | float) -> np.ndarray:
    """T2 small-signal tangent permittivity  eps_ss/eps0 = d(S*V)/dV = S - A_V^2/S.

    The dQ/dV differential of the T2 constitutive D ~ eps0*S(A_V)*V
    (round-3 RESULT: tangent C0*(S - A0^2/S) -> leading 1 - 3/2 A0^2). This is
    THE small-signal T2 permittivity (crowned) and, per deliverable (c), it is
    the PARALLEL polarization eigenmode of the birefringence Letter.
    """
    a = t2_argument(v)
    s = kernel_S(a)
    # s -> 0 at V_yield: the tangent -> -inf (the constitutive rolloff's slope
    # blows up as the polarization runs out). NaN at exact boundary is honest.
    with np.errstate(divide="ignore", invalid="ignore"):
        return s - a**2 / s


# --- section 3: the C-V datasheet curve (both branches, log-V) --------------
# (filled in a later commit)


# --- section 4: the perp/parallel eigenmode check vs the Letter (sympy) ------
# (filled in a later commit)


# --- section 5: network composition (K4 z=3 loaded-line ladder) -------------
# (filled in a later commit)


def main() -> None:
    """Run all sections and emit the datasheet figure + JSON summary."""
    raise NotImplementedError  # filled in a later commit


if __name__ == "__main__":
    main()
