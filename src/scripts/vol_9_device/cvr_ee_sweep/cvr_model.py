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

from dataclasses import dataclass, field

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

# --- Class-invariant substrate scale (shared by EVERY excitation on M_A) -----
# OMEGA_C is the bond LC natural frequency of the lattice itself — NOT an
# electron-specific value. It is the class scale on which any SubstrateExcitation
# rings; it stays a module constant.
OMEGA_C: float = C_0 / L_NODE  # bond LC natural frequency [rad/s] ~ 7.76e20 (AC ch5:37)

# --- Electron INSTANCE value (factor-out target; NOT a universal default) -----
# Q_TANK is the ELECTRON's instance Q VALUE (= 1/alpha, derived from the
# electron's torus geometry 4*pi^3 + pi^2 + pi; clm-rtdmsn). It is legitimately
# electron-specific. The class-invariant FORM functions (poles / H_scalar /
# H_chiral) MUST NOT default to it as if it were universal — they take an
# explicit, required, keyword-only Q. The electron operating point is supplied
# only by the ELECTRON instance below. (alpha, by contrast, IS universal — it is
# the EM coupling, kept in gamma_mag_sq_leak() and NEVER renamed 1/Q.)
Q_TANK: float = 1.0 / ALPHA  # ELECTRON instance Q = alpha^-1 ~ 137.04 (clm-rtdmsn)


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


def poles(A0: float = 0.0, *, Q: float) -> tuple[complex, complex]:
    """Pole pair of the 2nd-order LC resonator: s = -w0/(2Q) +/- j*w0*sqrt(1-1/(4Q^2)).

    CLASS-INVARIANT FORM (the pole SHAPE / root-locus). ``Q`` is a REQUIRED
    keyword instance field — there is no electron default here: the form must
    accept ANY Q and move the pole accordingly (gate leg 2, dead-input test).
    With the electron's Q = 1/alpha the real part is -alpha*w0/2 (the radiative
    linewidth = the leak); supply it via the ELECTRON instance. w0 = omega_local(A0).
    """
    w0 = omega_local(A0)
    sigma = w0 / (2.0 * Q)
    wd = w0 * np.sqrt(max(0.0, 1.0 - 1.0 / (4.0 * Q**2)))
    return complex(-sigma, wd), complex(-sigma, -wd)


def H_scalar(s: np.ndarray, A0: float = 0.0, *, Q: float) -> np.ndarray:
    """Co-polarized 2nd-order resonator H(s) = w0^2 / (s^2 + (w0/Q) s + w0^2).

    CLASS-INVARIANT FORM. ``Q`` is a REQUIRED keyword instance field (no electron
    default). DERIVED: poles at -w0/(2Q) +/- j w_d; for the electron (Q=1/alpha)
    the leak is alpha. Bode: peak Q at w0, bandwidth BW = w0/Q. Supply the
    electron's Q via the ELECTRON instance.
    """
    w0 = omega_local(A0)
    s = np.asarray(s, dtype=complex)
    return w0**2 / (s**2 + (w0 / Q) * s + w0**2)


def H_chiral(
    s: complex | np.ndarray,
    A0: float = 0.0,
    *,
    Q: float,
    chi: float = 0.30,
) -> np.ndarray:
    """2x2 chiral transfer matrix in the (L,R) circular-handedness basis.

    CLASS-INVARIANT FORM. ``Q`` is a REQUIRED keyword instance field (no electron
    default); supply the electron's Q via the ELECTRON instance.

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
# The SubstrateExcitation class-tree (factor electron INSTANCE out of the FORMS)
# ---------------------------------------------------------------------------
# Field-def electron pilot (instance-1). The class-invariant FORMS above (the
# pole shape, root-locus, S(A), the Gamma_spinor wall) carry NO electron value;
# the electron operating point lives ONLY in the ELECTRON instance below. A
# different instance (different Q / omega_c) produces correspondingly different
# outputs; the electron reproduces today's numbers by plugging in its own values.
#
# THE Gamma-HOMONYM (LOAD-BEARING — labelled distinctly, NOT resolved here):
#   * GAMMA_SPINOR = -1  -> the topological 2pi->4pi spinor-sign / perfect-short
#       STABILITY wall (resonant-lc-solitons.md:64). Class-invariant: ALL
#       fermions have it (electron AND proton). This is NOT the EM leak.
#   * |Gamma_EM|^2 = 1 - alpha -> the EM RADIATIVE reflection (the wall falls
#       short of the unit circle by exactly alpha, the per-cycle leak;
#       cvr-reflection-smith.md:36). DEFAULT electron-scoped corollary.
#   The electron has BOTH. They share the glyph "Gamma" and the value -1/near-1
#   but are distinct objects; do not conflate. (See report open-item: whether the
#   resonant-lc-solitons.md impedance-short Gamma=-1 is identically the spinor
#   2pi->4pi sign is a pending human physics ruling — NOT decided in code.)


@dataclass(frozen=True)
class SubstrateExcitation:
    """Base of the substrate-excitation class-tree.

    Holds ONLY the class-invariant lattice scale (``omega_c``, the bond LC
    natural frequency shared by every excitation on M_A) and the class-invariant
    Gamma_spinor wall. It fixes NO operating point and NO Q — those are INSTANCE
    fields a concrete subclass supplies.

    Cavity-class discriminator (ave-cavity-class-identification): a BoundResonator
    (closed, high-Q, TIR-confined, |Gamma|->1, poles ride toward the jw axis) vs
    an OpenCosseratScrew (a radiating longitudinal Cosserat shear mode, contour
    integral != 0 — e.g. the AVE-Propulsion dark-wake antenna). The electron is a
    BoundResonator; the open-screw sibling is NOT instantiated in this pilot.
    """

    omega_c: float = OMEGA_C

    # Gamma_spinor = -1: the topological / perfect-short STABILITY wall (class-
    # invariant; ALL fermions). Distinct from the EM radiative leak |Gamma_EM|^2.
    GAMMA_SPINOR: float = field(default=-1.0, init=False)

    def saturation_kernel(self, A: np.ndarray, *, clip: bool = True) -> np.ndarray:
        """Class method S(A) = sqrt(1 - A^2) (Axiom-4 kernel; class-invariant)."""
        return saturation_kernel(A, clip=clip)


@dataclass(frozen=True)
class BoundResonator(SubstrateExcitation):
    """A bound high-Q LC resonator instance — the electron's cavity class.

    Adds the INSTANCE fields factored out of the class-invariant forms: the Q
    VALUE, the (p,q) torus winding label, and an instance name. The form methods
    bind ``self.Q`` into the module-level class-invariant forms — the instance is
    the ONLY place the operating Q enters.

    Canon-noun map: unknot dilatation-mass / Mass-Dilatation Resonator / Resonant
    LC Tank / 0_1 unknot + (2,3) winding. ("vortex ring" / "lossless pivot" are
    research-only, not canon.)
    """

    # Q is a REQUIRED keyword instance field — NO electron default at the class
    # level (gate leg 3: the class must not silently produce an electron). The
    # electron's Q VALUE is injected ONLY at the ELECTRON instance constructor
    # below (the one site the residual-default gate allows to carry it).
    Q: float = field(kw_only=True)  # INSTANCE Q value (electron = 1/alpha; clm-rtdmsn)
    pq: tuple[int, int] = field(default=(2, 3), kw_only=True)  # (p,q) winding label (electron-identification.md:27)
    name: str = field(default="electron", kw_only=True)

    def omega_local(self, A0: float) -> float:
        """Operating-point resonance omega_local(A0) = omega_c * S(A0)."""
        return self.omega_c * float(saturation_kernel(np.array(A0)))

    def poles(self, A0: float = 0.0) -> tuple[complex, complex]:
        """Instance pole pair — binds self.Q into the class-invariant form."""
        return poles(A0, Q=self.Q)

    def H_scalar(self, s: np.ndarray, A0: float = 0.0) -> np.ndarray:
        """Instance H(s) — binds self.Q into the class-invariant form."""
        return H_scalar(s, A0, Q=self.Q)

    def H_chiral(self, s: complex | np.ndarray, A0: float = 0.0, chi: float = 0.30) -> np.ndarray:
        """Instance 2x2 chiral H — binds self.Q into the class-invariant form."""
        return H_chiral(s, A0, Q=self.Q, chi=chi)

    def gamma_em_sq(self) -> float:
        """|Gamma_EM|^2 = 1 - alpha (electron-scoped EM radiative-leak corollary).

        DISTINCT from GAMMA_SPINOR (the class-invariant -1 wall). alpha is the
        UNIVERSAL EM coupling — this value does NOT depend on the instance Q
        (gate leg 2 holds it fixed). Default electron-scoped; do NOT promote to a
        universal class law (pending human physics ruling).
        """
        return gamma_mag_sq_leak()

    def A_wall(self) -> float:
        """Residual amplitude A* where |Gamma_EM|^2 = 1 - alpha (electron wall)."""
        return A_at_electron_wall()


# Instance-1 of the class-tree: the electron, plugging in its own Q value.
ELECTRON: BoundResonator = BoundResonator(Q=Q_TANK, pq=(2, 3), name="electron")


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
    # ELECTRON instance reproduces the electron operating point through the
    # factored class-invariant forms (instance == form-with-electron-Q). These
    # assertions add NO output — the returned dict is byte-identical to pre-pilot.
    assert ELECTRON.Q == Q_TANK, "ELECTRON instance Q drift"
    assert ELECTRON.poles()[0].real == poles(Q=Q_TANK)[0].real, "instance/form pole drift"
    assert ELECTRON.gamma_em_sq() == gamma_mag_sq_leak(), "instance |Gamma_EM|^2 drift"
    # |Gamma_EM|^2 is universal-alpha, NOT instance-Q dependent (gate-leg-2 guard):
    assert ELECTRON.gamma_em_sq() == BoundResonator(Q=50.0).gamma_em_sq(), "|Gamma_EM|^2 must not vary with Q"
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
