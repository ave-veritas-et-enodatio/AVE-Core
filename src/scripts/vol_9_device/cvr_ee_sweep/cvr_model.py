"""
CVR model — the substrate-native Vacuum-Circuit-Analysis constitutive spine.
===========================================================================

The shared, importable model behind the six CVR EE-sweep views. Every curve in
``cvr_ee_sweep.py`` is a projection of this one constitutive law + the H(s)
spine. Pure functions, no plotting, canonical constants only.

CANONICAL ANCHORS (verify-before-cite; grep these in manuscript/ave-kb):
  - Kernel S(A)=sqrt(1-(A/A_yield)^2)               INVARIANT-S2 (Axiom 4)
  - Varactor  C_eff(A)=C0/S(A)                      nonlinear-vacuum-capacitance.md;
                                                     translation-circuit.md:111-112
  - Two speeds c_EM=c0/S, c_shear=c0*sqrt(S)        INVARIANT-S2; universal_operators.py:969
  - ELECTRON = MAGNETIC branch mu_eff->0 => Z->0    master-equation.md:78-79 (clm-lv3uw1);
              => Gamma=-1 (short, trapped knot)      translation-circuit.md:115; photon-ee-mapping.md S2
  - alpha = 1/Q (per-cycle leak)                    theorem-3-1-q-factor.md:15,38,81
  - |Gamma|^2 = 1 - alpha (AVE-DISTINCT)            the wall falls short of the unit
                                                     circle by exactly alpha = radiative leak
  - omega_C = c0/ell_node                           AC datasheet ch5:37
  - H(s) pole pair s = -alpha*w0/2 +/- j*w_d        AUDITOR_STATE H(s) spine

TWO CARRIED FLAGS (flag-don't-fix — see _orchestration/2026-06-13_cvr-ee-sweep-doc.md):
  (1) SECTOR ATTRIBUTION (AUDITOR_STATE FLAG-2): the Z->0/Gamma=-1 wall has two
      corpus routes — magnetic (mu_eff->0, PRIMARY, clm-lv3uw1) vs capacitive
      (C_eff->inf, resonant-lc-solitons.md:29-39, clm-kezk9z). BOTH give the SAME
      Z(A)=Z0*sqrt(S) trajectory, so the computed curves are robust; the flag is a
      prose ATTRIBUTION matter (which constitutive parameter moves), not a curve fork.
  (2) EXPONENT DEFECT (master_equation_fdtd.py:165): the engine returns n=S^0.25 but
      the in-code FLAG says physical n=c0/c_eff=S^0.5 (since c_eff^2=c0^2/S). The
      engine understates wall depth. We expose BOTH (n_engine, n_physical) and the
      derived Gamma so any figure can show the gap and caption the understatement.
  (3) S_min / A_cap clip (graft-v2 apparatus floor): magnitudes are bench-capped, not
      physical wall depth — carried via S_MIN / A_CAP and the clip in saturation_kernel().
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import (
    ALPHA,
    ALPHA_COLD_INV,
    C_0,
    EPSILON_0,
    L_NODE,
    MU_0,
    V_SNAP,
    V_YIELD,
    Z_0,
)

# --- Apparatus floor (carry the graft-v2 clip; master_fdtd_phasor_bridge.py:66) ---
S_MIN: float = 0.05  # kernel clip floor — magnitudes below this are apparatus-capped
A_CAP: float = 0.99  # amplitude cap A=|V|/V_yield <= A_CAP

# --- Derived substrate quantities (from canonical primitives; not hard-coded) ---
OMEGA_C: float = C_0 / L_NODE  # bond LC natural frequency [rad/s] ~ 7.76e20 (AC ch5:37)
Q_TANK: float = 1.0 / ALPHA  # electron tank Q = alpha^-1 ~ 137.04 (theorem-3-1-q-factor.md)


# ---------------------------------------------------------------------------
# Constitutive law (Axiom 4 saturation kernel + its EE projections)
# ---------------------------------------------------------------------------
def saturation_kernel(A: np.ndarray, *, clip: bool = True) -> np.ndarray:
    """S(A) = sqrt(1 - A^2), the canonical Axiom-4 quarter-arc kernel.

    A = |V| / V_yield is the per-node amplitude ratio (A_yield == 1 in these
    normalized units). With ``clip=True`` the result is floored at S_MIN and A
    is capped at A_CAP — carrying the graft-v2 apparatus floor so figures cannot
    mistake a bench-capped magnitude for physical wall depth.
    """
    A = np.asarray(A, dtype=float)
    if clip:
        A = np.minimum(A, A_CAP)
    S = np.sqrt(np.clip(1.0 - A**2, 0.0, 1.0))
    if clip:
        S = np.maximum(S, S_MIN)
    return S


def c_em(A: np.ndarray) -> np.ndarray:
    """Maxwell phase velocity c_EM(A) = c0 / S(A)  (enters alpha; INVARIANT-S2).

    Diverges as A->1 (S->0): this is the c_eff->inf that self-creates the wall.
    """
    return C_0 / saturation_kernel(A)


def c_shear(A: np.ndarray) -> np.ndarray:
    """Mechanical / group / rest-mass velocity c_shear(A) = c0*sqrt(S(A)).

    Canonical at universal_operators.py:969 (= c0*(1-A^2)^(1/4)). Freezes to 0 as
    A->1 — the clock-freeze / Schwarzschild reduction.
    """
    return C_0 * np.sqrt(saturation_kernel(A))


def n_physical(A: np.ndarray) -> np.ndarray:
    """Physical refractive index n = c0/c_eff = S^0.5  (the CORRECTED exponent).

    From the master-equation c_eff^2 = c0^2/S => c_eff = c0/sqrt(S) => n = sqrt(S).
    """
    return np.sqrt(saturation_kernel(A))


def n_engine(A: np.ndarray) -> np.ndarray:
    """Engine refractive index n = S^0.25  (master_equation_fdtd.py:165, AS-CODED).

    Carries the FLAGGED exponent defect: this UNDERSTATES the wall depth relative
    to n_physical = S^0.5. Exposed so figures show the gap and caption it.
    """
    return saturation_kernel(A) ** 0.25


def c_eff_capacitance(A: np.ndarray, C0: float = 1.0) -> np.ndarray:
    """Vacuum varactor C_eff(A) = C0 / S(A)  (diverges as A->1).

    nonlinear-vacuum-capacitance.md; resonant-lc-solitons.md:32; translation-circuit.md:111.
    Default C0=1 returns the dimensionless C_eff/C0 ratio for plotting.
    """
    return C0 / saturation_kernel(A)


# ---------------------------------------------------------------------------
# Impedance + reflection (the magnetic-branch wall)
# ---------------------------------------------------------------------------
def z_core(A: np.ndarray) -> np.ndarray:
    """Core impedance Z_core(A) = Z0 * sqrt(S(A))  ->  0 as A->1 (Gamma=-1 short).

    SECTOR-ATTRIBUTION FLAG (robust either way): the magnetic branch gives
    Z=sqrt(mu_eff/eps0)=sqrt(mu0 S/eps0)=Z0*sqrt(S); the capacitive route gives
    Z~1/sqrt(C_eff)~sqrt(S). SAME trajectory — only the moved parameter differs.
    """
    return Z_0 * np.sqrt(saturation_kernel(A))


def gamma_of_A(A: np.ndarray) -> np.ndarray:
    """Reflection Gamma(A) = (Z_core - Z0)/(Z_core + Z0) at the core/ambient boundary.

    Op3 (operators.md:43). A->1: Gamma->-1 (perfect short, TIR). A=0: Gamma=0 (matched,
    the free photon). resonant-lc-solitons.md:42-46.
    """
    Zc = z_core(A)
    return (Zc - Z_0) / (Zc + Z_0)


def gamma_mag_sq_leak(alpha: float = ALPHA) -> float:
    """|Gamma|^2 = 1 - alpha  — the AVE-DISTINCT per-cycle radiative-leak relation.

    The electron wall is NOT a perfect short: it leaks exactly alpha (= 1/Q) of the
    stored energy per cycle (theorem-3-1-q-factor.md:81), so the reflected power is
    1-alpha and |Gamma| = sqrt(1-alpha) ~ 0.99635 sits just INSIDE the unit circle.
    alpha is the hair Gamma falls short of |Gamma|=1.
    """
    return 1.0 - alpha


def A_at_electron_wall(alpha: float = ALPHA) -> float:
    """The residual amplitude A* where |Gamma|^2 = 1-alpha (the electron operating wall).

    Solve |Gamma| = (1 - sqrt(S))/(1 + sqrt(S)) = sqrt(1-alpha) for sqrt(S), then
    A* = sqrt(1 - S^2). The wall sits at sqrt(S*) ~ alpha/4 (small-alpha), i.e. a tiny
    but NON-ZERO residual impedance — the radiative leak made geometric.
    """
    g = np.sqrt(1.0 - alpha)
    sqrtS = (1.0 - g) / (1.0 + g)
    S = sqrtS**2
    return float(np.sqrt(max(0.0, 1.0 - S**2)))


# ---------------------------------------------------------------------------
# The H(s) spine — 2x2 chiral transfer function
# ---------------------------------------------------------------------------
def omega_local(A0: float) -> float:
    """Operating-point resonance omega_local(A0) = omega_C * S(A0)  (Op14 detuning).

    op14-local-clock-modulation.md: omega_local = omega_global*sqrt(1-A^2)=omega_C*S(A0).
    The varactor bias A0 detunes the tank down; A0->1 freezes it (omega_local->0).
    """
    return OMEGA_C * float(saturation_kernel(np.array(A0)))


def poles(A0: float = 0.0, Q: float = Q_TANK) -> tuple[complex, complex]:
    """Pole pair of the 2nd-order LC resonator: s = -w0/(2Q) +/- j*w0*sqrt(1-1/(4Q^2)).

    With Q = 1/alpha the real part is -alpha*w0/2 (the radiative linewidth = the leak),
    matching the AUDITOR_STATE H(s) spine. w0 = omega_local(A0).
    """
    w0 = omega_local(A0)
    sigma = w0 / (2.0 * Q)
    wd = w0 * np.sqrt(max(0.0, 1.0 - 1.0 / (4.0 * Q**2)))
    return complex(-sigma, wd), complex(-sigma, -wd)


def H_scalar(s: np.ndarray, A0: float = 0.0, Q: float = Q_TANK) -> np.ndarray:
    """Co-polarized 2nd-order resonator H(s) = w0^2 / (s^2 + (w0/Q) s + w0^2).

    DERIVED: poles at -alpha*w0/2 +/- j w_d (Q=1/alpha leak). Bode: peak Q=1/alpha at
    w0, bandwidth BW = w0/Q = alpha*w0.
    """
    w0 = omega_local(A0)
    s = np.asarray(s, dtype=complex)
    return w0**2 / (s**2 + (w0 / Q) * s + w0**2)


def H_chiral(
    s: complex | np.ndarray,
    A0: float = 0.0,
    Q: float = Q_TANK,
    chi: float = 0.30,
) -> np.ndarray:
    """2x2 chiral transfer matrix in the (L,R) circular-handedness basis.

    H = [[H_co,        chi*H_cross],
         [-chi*H_cross, H_co      ]]      (skew off-diagonal = parity-odd winding)

    DERIVED part: the diagonal co-pol resonance H_co (= H_scalar) and its pole pair.
    STATED / AVE-DISTINCT-candidate: the off-diagonal chiral coupling. The (2,3)
    winding makes the L<->R conversion NON-RECIPROCAL (S_LR != S_RL*) — the
    parity-odd selection rule. ``chi`` is the winding coupling fraction; its MAGNITUDE
    needs the chiral-crystal engine (cubic FDTD averages chirality out — AUDITOR_STATE
    FLAG-4). Here it is a STRUCTURAL placeholder demonstrating the broken reciprocity,
    not a derived magnitude.
    """
    w0 = omega_local(A0)
    s = np.asarray(s, dtype=complex)
    H_co = w0**2 / (s**2 + (w0 / Q) * s + w0**2)
    # cross term carries a 90deg (j) winding phase => skew-Hermitian off-diagonal
    H_cross = 1j * w0 * (w0 / Q) / (s**2 + (w0 / Q) * s + w0**2)
    out = np.empty((2, 2) + np.shape(s), dtype=complex)
    out[0, 0] = H_co
    out[1, 1] = H_co
    out[0, 1] = chi * H_cross
    out[1, 0] = -chi * H_cross
    return out


# ---------------------------------------------------------------------------
# Canonical-source self-check (ave-canonical-source: verify before any output)
# ---------------------------------------------------------------------------
def verify_constants() -> dict:
    """Cross-check imported canonical constants against their derived identities.

    Raises AssertionError on drift (the 10-OOM-error guard). Returns a summary dict.
    """
    assert abs(Z_0 - np.sqrt(MU_0 / EPSILON_0)) < 1e-6, "Z_0 drift"
    # CODATA alpha agrees with the derived Golden-Torus cold value to delta_strain;
    # both imported/derived (no hard-coded constant — DAG anti-cheat clean).
    assert abs(1.0 / ALPHA - ALPHA_COLD_INV) < 1e-2, "CODATA-alpha vs cold-alpha drift"
    assert abs(ALPHA_COLD_INV - (4 * np.pi**3 + np.pi**2 + np.pi)) < 1e-9, "ALPHA_COLD_INV drift"
    assert abs(V_YIELD - np.sqrt(ALPHA) * V_SNAP) < 1e-3, "V_YIELD drift"
    assert abs(OMEGA_C - C_0 / L_NODE) < 1e-3, "OMEGA_C drift"
    # the AVE-distinct relation, sanity:
    assert abs(gamma_mag_sq_leak() - (1.0 - ALPHA)) < 1e-12
    return {
        "Z_0_ohm": Z_0,
        "alpha_inv": 1.0 / ALPHA,
        "alpha_cold_inv": ALPHA_COLD_INV,
        "V_yield_kV": V_YIELD / 1e3,
        "V_snap_kV": V_SNAP / 1e3,
        "omega_C_rad_s": OMEGA_C,
        "Q_tank": Q_TANK,
        "gamma_mag_sq_leak": gamma_mag_sq_leak(),
        "A_at_electron_wall": A_at_electron_wall(),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(verify_constants(), indent=2))
