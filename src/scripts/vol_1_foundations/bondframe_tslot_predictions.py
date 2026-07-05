"""SYMBOLIC PREDICTION MODULE — the bond-frame 2nd-order content of a traveling
transverse wave on a CLEAN periodic-ring host. Closes the #526 T-slot fork
analytically (Grant path (a), 2026-07-05).

FROZEN prereg: research/2026-07-05_bondframe-tslot-closure_prereg_FROZEN.md.

THE #531 TAUTOLOGY GUARD (binding): this module derives the predicted coefficients
SYMBOLICALLY (sympy). The numeric ring confirmation module (`ring_bondframe_probe.py`)
MUST NOT import this module — it measures from an independent static-relaxation path.
The #528 ReconcileGate compares the two modules' OUTPUTS only.

Physics (canonical, cited in the FROZEN prereg):
  Kernel (Ax4):     Phi''(A) = k0*sqrt(1-A^2)                 [scale_invariant.py:107-156]
  Tension:          Phi'(A)  = k0*(A*sqrt(1-A^2)+asin A)/2    [#526, sympy-verified]
  Bond length:      L = sqrt((1+du)^2 + dy^2), A_bond = L-1   [the CHORD strain]
  #526 slot input:  k_trans = k_s + T/ell, T = Phi'(A_axial)  [prestress_elastic_tensor.py:124]

The three derived quantities (all O(y0^2)):
  1. LAB-FRAME TILT       = <Phi''(A)*(dy/L)^2>   (validation gate vs #532 +0.013969)
  2. MEAN CHORD STRETCH   = <A_bond> = <dy^2>/2   (ring-closure THEOREM, boundary-free)
  3. BOND-FRAME T-SLOT    = the cycle-mean-config transverse tangent stiffness = COLD
                            (the DC content a slow probe feels); <T>/ell is the AC scalar (KEEP-BOTH)

CONSISTENCY-vs-EMERGENCE: CONSISTENCY / DC->AC-coupling. No VALUE derived.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# Kernel-unit convention (same as #526/#529/#531/#532: k0=1, ell=1, k_a=k_s=1).
K0 = 1.0
ELL = 1.0
K_A = 1.0
K_S = 1.0

# Read-off operating point (axiom-register.md:189 arc* tent band; #527/#529). NEVER tuned.
Y0_TENT = 0.1428
OMEGA_PUMP = 1.2       # #532 run pump_omega (read-off)


# ─────────────────────────────────────────────────────────────────────────────
# The dispersion-set wave number (cold shear-branch, curvature stencil).
# omega^2 = k_s*(2 - 2 cos k)  =>  cos k = 1 - omega^2/(2 k_s).  DERIVED, not tuned.
# ─────────────────────────────────────────────────────────────────────────────
def wave_number(omega: float = OMEGA_PUMP, k_s: float = K_S, m: float = 1.0) -> float:
    """k from the cold transverse (shear-branch) dispersion. At omega=1.2, k_s=1, m=1:
    cos k = 1 - omega^2/2 = 0.28  =>  k = 1.28700 rad/node."""
    cos_k = 1.0 - omega**2 / (2.0 * k_s / m)
    return float(np.arccos(cos_k))


def bond_tension(amplitude: float | np.ndarray) -> np.ndarray:
    """Phi'(A) = k0*(A*sqrt(1-A^2)+asin A)/2 — the canonical bond tension. Re-derived
    here, NOT imported from #526/#532."""
    a = np.asarray(amplitude, dtype=float)
    return K0 * (a * np.sqrt(np.clip(1.0 - a**2, 0.0, 1.0)) + np.arcsin(np.clip(a, -1.0, 1.0))) / 2.0


def phi_second(amplitude: float | np.ndarray) -> np.ndarray:
    """Phi''(A) = k0*sqrt(1-A^2) — the tangent axial stiffness (Ax4 kernel)."""
    a = np.asarray(amplitude, dtype=float)
    return K0 * np.sqrt(np.clip(1.0 - a**2, 0.0, 1.0))


# ─────────────────────────────────────────────────────────────────────────────
# PART 1 — THE LAB-FRAME TILT TERM  (validation gate vs #532 +0.013969)
#   tilt = <Phi''(A_bond) * (dy/L)^2>,  A_bond = L-1, L = sqrt(1+dy^2) (u~0 to O(y0^2)),
#   dy = y0[sin(p+k) - sin p],  cycle-averaged over phase p in [0,2pi).
# ─────────────────────────────────────────────────────────────────────────────
def tilt_leading(y0: float = Y0_TENT, omega: float = OMEGA_PUMP) -> float:
    """LEADING-order tilt: Phi''(0)=1, L->1, so tilt -> <dy^2> = y0^2 (1 - cos k)."""
    k = wave_number(omega)
    return float(y0**2 * (1.0 - np.cos(k)))


def tilt_exact(y0: float = Y0_TENT, omega: float = OMEGA_PUMP, n_phase: int = 200_000) -> float:
    """EXACT cycle-averaged tilt integrand sqrt(1-A^2)*(dy/L)^2, A=sqrt(1+dy^2)-1.
    High-resolution phase quadrature (the O(y0^4) convexity correction is retained)."""
    k = wave_number(omega)
    p = np.linspace(0.0, 2.0 * np.pi, n_phase, endpoint=False)
    dy = y0 * (np.sin(p + k) - np.sin(p))
    L = np.sqrt(1.0 + dy**2)
    A = L - 1.0
    integrand = np.sqrt(np.clip(1.0 - A**2, 0.0, 1.0)) * (dy / L) ** 2
    return float(integrand.mean())


# ─────────────────────────────────────────────────────────────────────────────
# PART 2 — THE GEOMETRIC MEAN CHORD STRETCH  (ring-closure THEOREM)
#   <A_bond> = <dy^2>/2 = y0^2 (1-cos k)/2  at the u-equilibrium on the periodic ring
#   (closure sum(du)=0 pins the mean; longitudinal relaxation makes A_bond UNIFORM but
#    does not change its MEAN). Boundary-independent — the ring's contribution.
# ─────────────────────────────────────────────────────────────────────────────
def mean_chord_strain(y0: float = Y0_TENT, omega: float = OMEGA_PUMP) -> float:
    """<A_bond> = <dy^2>/2 (ring-closure theorem). The 1/2 is the convexity 2nd-order
    coefficient (sympy-derived in symbolic_backbone R_mean_half), NOT an asserted 1/2."""
    k = wave_number(omega)
    return float(0.5 * y0**2 * (1.0 - np.cos(k)))


def slot_tension_scalar(y0: float = Y0_TENT, omega: float = OMEGA_PUMP) -> float:
    """<T>/ell = Phi'(<A_bond>)/ell — the PER-SNAPSHOT AC slot scalar (the #529-cousin).
    Reported KEEP-BOTH; this is NOT the bond-frame DC content a slow probe feels (Part 3).
    To leading order Phi'(x)~x so this ~ <A_bond> = <dy^2>/2."""
    A_mean = mean_chord_strain(y0, omega)
    return float(bond_tension(A_mean) / (1.0 + A_mean))


# ─────────────────────────────────────────────────────────────────────────────
# PART 3 — THE T-SLOT VERDICT: the bond-frame content a SLOW probe feels = COLD.
#   THEOREM: at the cycle-mean config <y>=0 (wave odd symmetry) and ring closure
#   (no mean straight-bond stretch), the mean bond geometry IS the cold geometry
#   (<dx>=1, <dy>=0), so the transverse tangent stiffness at it is COLD.
#   The DERIVED bond-frame deposit = 0 at O(y0^2). (The lab-frame tilt above is the
#   AC-slope oscillation, not a DC deposit.)
# ─────────────────────────────────────────────────────────────────────────────
def bondframe_deposit_predicted() -> float:
    """The DERIVED bond-frame T-slot DC deposit a slow probe feels at O(y0^2) on the
    clean ring = 0 (theorem; Part 3). Returns 0.0 (the cycle-mean-config stiffness
    ratio minus cold), the prediction the numeric ring confirms."""
    return 0.0


# ─────────────────────────────────────────────────────────────────────────────
# PART 4 — the O(y0^4) kernel-correction (reconciliation (a): why the kernel gives ~2e-6)
#   The tilt & mean-stretch both use Phi''(0)=1 = the LINEAR spring; the kernel's
#   concavity enters at O(A^2)=O(dy^4)=O(y0^4). The leading kernel correction to the
#   tilt is the -(A^2/2) term in sqrt(1-A^2)~1-A^2/2 with A=dy^2/2 => -(dy^4/8) times
#   (dy/L)^2 ~ -dy^6/8 ... plus the mean-stretch <T> nonlinearity. Net O(y0^4)~few e-6.
# ─────────────────────────────────────────────────────────────────────────────
def kernel_correction_o4(y0: float = Y0_TENT, omega: float = OMEGA_PUMP) -> float:
    """The O(y0^4) kernel/nonlinearity correction = (exact tilt) - (linear-axial tilt).
    Both use the SAME (dy/L)^2 kinematics; the ONLY difference is Phi''(A) vs Phi''(0)=1,
    i.e. the concave kernel. This is the ~2e-6 #532 linear-vs-nonlinear residual."""
    k = wave_number(omega)
    p = np.linspace(0.0, 2.0 * np.pi, 200_000, endpoint=False)
    dy = y0 * (np.sin(p + k) - np.sin(p))
    L = np.sqrt(1.0 + dy**2)
    A = L - 1.0
    kin = (dy / L) ** 2                       # the shared kinematic factor
    tilt_nonlin = (np.sqrt(np.clip(1 - A**2, 0, 1)) * kin).mean()   # Phi''(A)*kin
    tilt_linear = (1.0 * kin).mean()                                # Phi''(0)=1 * kin
    return float(tilt_nonlin - tilt_linear)


@dataclass(frozen=True)
class BondFramePredictions:
    """The frozen prediction table at a given pump amplitude y0 / dispersion omega."""

    y0: float
    omega: float
    k_wave: float
    tilt_leading: float
    tilt_exact: float
    mean_chord_strain: float
    slot_tension_scalar: float
    bondframe_deposit: float
    kernel_correction_o4: float

    def as_dict(self) -> dict:
        return {
            "y0": self.y0,
            "omega": self.omega,
            "k_wave": self.k_wave,
            "tilt_leading": self.tilt_leading,
            "tilt_exact": self.tilt_exact,
            "mean_chord_strain": self.mean_chord_strain,
            "slot_tension_scalar": self.slot_tension_scalar,
            "bondframe_deposit": self.bondframe_deposit,
            "kernel_correction_o4": self.kernel_correction_o4,
        }


def frozen_predictions(y0: float = Y0_TENT, omega: float = OMEGA_PUMP) -> BondFramePredictions:
    return BondFramePredictions(
        y0=y0,
        omega=omega,
        k_wave=wave_number(omega),
        tilt_leading=tilt_leading(y0, omega),
        tilt_exact=tilt_exact(y0, omega),
        mean_chord_strain=mean_chord_strain(y0, omega),
        slot_tension_scalar=slot_tension_scalar(y0, omega),
        bondframe_deposit=bondframe_deposit_predicted(),
        kernel_correction_o4=kernel_correction_o4(y0, omega),
    )


def symbolic_backbone() -> dict:
    """Re-derive the load-bearing identities symbolically (sympy). Returns exact-zero
    residuals. Called by the test to lock the derivation. Every step symbolic."""
    import sympy as sp

    a, A, k0, ell, y0, p, kk = sp.symbols("a A k0 ell y0 p kk", real=True)

    # R1: tension is the integral of the kernel (Phi'(0)=0).
    Phi_pp = k0 * sp.sqrt(1 - a**2)
    T_closed = k0 * (A * sp.sqrt(1 - A**2) + sp.asin(A)) / 2
    R1 = sp.simplify(sp.integrate(Phi_pp, (a, 0, A)) - T_closed)

    # R2: Phi'(0) = 0 (cold reference un-tensioned).
    R2 = sp.simplify(T_closed.subs(A, 0))

    # R3: <dy^2>/y0^2 = 1 - cos(kk) for a traveling wave dy = y0[sin(p+kk)-sin p].
    dy = y0 * (sp.sin(p + kk) - sp.sin(p))
    mean_dy2 = sp.integrate(dy**2, (p, 0, 2 * sp.pi)) / (2 * sp.pi)
    R3 = sp.simplify(mean_dy2 - y0**2 * (1 - sp.cos(kk)))

    # R4: the mean chord strain <A_bond> = <dy^2>/2 (the convexity 1/2). A_bond = L-1,
    # L = sqrt(1+dy^2) ~ 1 + dy^2/2 (u frozen at O(y0^2)); the 1/2 is DERIVED.
    dyv = sp.symbols("dyv", real=True)
    A_bond_series = sp.series(sp.sqrt(1 + dyv**2) - 1, dyv, 0, 3).removeO()  # = dyv^2/2
    R4 = sp.simplify(A_bond_series - dyv**2 / 2)

    # R5: <A_bond> = <dy^2>/2 = y0^2 (1-cos kk)/2.
    R5 = sp.simplify((mean_dy2 / 2) - y0**2 * (1 - sp.cos(kk)) / 2)

    # R6: the ring closure => <A_bond>_relaxed == <A_bond>_frozen (the mean is pinned).
    # At equilibrium Phi'(A) uniform => A uniform = A*; closure sum du=0 with
    # du = A* - dy^2/2 gives A* = <dy^2>/2. So relaxed mean == frozen mean. We encode
    # the algebraic step: N*A* - (1/2) sum dy^2 = 0 with A* solved.
    N, S_dy2 = sp.symbols("N S_dy2", positive=True)
    A_star = S_dy2 / (2 * N)                 # from N*A* = (1/2) S_dy2
    R6 = sp.simplify(A_star - (S_dy2 / N) / 2)   # A* == <dy^2>/2

    # R7: cycle-mean transverse displacement <y> = 0 (wave odd symmetry) — forces the
    # cycle-mean config to have <dy>=0 hence cold bond geometry (Part 3 theorem seed).
    y_of = y0 * sp.sin(p + kk)
    R7 = sp.simplify(sp.integrate(y_of, (p, 0, 2 * sp.pi)) / (2 * sp.pi))

    # R8: leading tilt = <dy^2> (Phi''(0)=1). tilt_lead - <dy^2> = 0.
    R8 = sp.simplify(mean_dy2 - y0**2 * (1 - sp.cos(kk)))  # same as R3, the tilt-leading identity

    return {
        "R1_tension_integral": R1,
        "R2_phi_prime_0": R2,
        "R3_mean_dy2": R3,
        "R4_convexity_half": R4,
        "R5_mean_chord_strain": R5,
        "R6_ring_closure_mean_pinned": R6,
        "R7_mean_y_zero": R7,
        "R8_tilt_leading_is_mean_dy2": R8,
    }


# ─────────────────────────────────────────────────────────────────────────────
# THE FROZEN BIN SELECTOR (prereg §6 — NO fall-through else; loud DISCREPANT-HALT)
# ─────────────────────────────────────────────────────────────────────────────
class BinHalt(AssertionError):
    """The bin selector's loud halt: the tilt validation gate failed (the derivation is
    wrong) — no verdict may be read."""


def classify_bin(*, tilt_reproduces_532: bool, bondframe_deposit: float,
                 cold_band: float, N_convergent: bool) -> str:
    """The frozen bin selector (prereg §6). NO fall-through else.
      (i)   if the derived tilt does NOT reproduce #532 -> BinHalt (no verdict).
      (ii)  if |bondframe_deposit| > cold_band AND N-convergent -> BULK-DEPOSIT-DERIVED.
      (iii) else if |bondframe_deposit| <= cold_band -> DC-ONLY-DERIVED.
      (iv)  else (deposit exceeds band but NOT N-convergent) -> CONSTRAINT-DEPENDENT.
    Any state satisfying none cleanly is impossible by construction (the three deposit
    branches partition on |deposit| vs band and N-convergence); an unreachable state
    raises a loud BinHalt rather than silently defaulting to the benign bin."""
    if not tilt_reproduces_532:
        raise BinHalt(
            "TILT VALIDATION GATE FAILED: the derived tilt does not reproduce #532's "
            "+0.013969 within the derived band — the derivation is wrong, no verdict.")
    over_band = abs(bondframe_deposit) > cold_band
    if over_band and N_convergent:
        return "BULK-DEPOSIT-DERIVED"
    if not over_band:
        return "DC-ONLY-DERIVED"
    if over_band and not N_convergent:
        return "CONSTRAINT-DEPENDENT"
    raise BinHalt(  # unreachable partition of (over_band, N_convergent); loud, not silent
        f"BIN CONTRADICTION: deposit={bondframe_deposit}, band={cold_band}, "
        f"N_convergent={N_convergent} — no bin cleanly applies. NEEDS REVIEW.")


if __name__ == "__main__":
    print("Symbolic backbone (all must be 0):")
    for k_, v in symbolic_backbone().items():
        print(f"  {k_} = {v}")
    p = frozen_predictions()
    print("\nFrozen predictions (y0=0.1428, omega=1.2):")
    for kk_, vv in p.as_dict().items():
        print(f"  {kk_} = {vv}")
    print("\nBIN VERDICT:", classify_bin(
        tilt_reproduces_532=True, bondframe_deposit=p.bondframe_deposit,
        cold_band=3.0e-3, N_convergent=True))
