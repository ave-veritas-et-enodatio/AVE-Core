"""FROZEN PREDICTION MODULE — the two arms' predicted probe transverse stiffness.

THE #531 TAUTOLOGY GUARD (binding): this module computes the ARM DC_ONLY / ARM
EXTENDED predictions from the MERGED slot laws (Φ', ⟨T⟩=(k_a/ℓ)y₀², k_trans =
k_s + T/ℓ). The honest-dynamics driver (`pump_probe_chain.py`) MUST NOT import this
module. The #528 ReconcileGate compares the two modules' OUTPUTS only. Keeping the
prediction code and the dynamics code in separate modules is the guard the #531
review demanded (the measurement must not consume the slot formulas it adjudicates).

All laws re-derived symbolically here (sympy), NOT imported from the #526/#529 drivers,
so the prediction is an independent statement of the merged laws.

Physics (canonical, cited in the FROZEN prereg 2026-07-05_pump-probe-tslot_prereg_FROZEN.md):
  Kernel (Ax4):   Φ''(a) = k0·√(1−a²)                     [scale_invariant.py:107-156]
  Tension:        Φ'(A)  = k0·(A√(1−A²)+arcsin A)/2       [#526, sympy-verified]
  Cycle-avg:      ⟨T⟩    = (k_a/ℓ)·y0²   (⟨sin²⟩=½)        [#529 Part-1]
  Transverse eff. stiffness a slow probe feels on a bond (merged #526/#531):
                  k_trans = k_s·S(A_shear) + T/ℓ

α-NOTE: A_bias default = √α is a Class-C echo READ-OFF (def-vyvsn1), never tuned.

CONSISTENCY-vs-EMERGENCE: CONSISTENCY / DC-internal. No VALUE derived.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# Kernel-unit convention (same as #526/#529/#531: k0=1 units into ρ, ℓ=1 on srs,
# both k_a and k_s the translational-u capacitive springs of the same bond).
K0 = 1.0
ELL = 1.0
K_A = 1.0
K_S = 1.0

# In-regime bow ceilings (READ-OFF, axiom-register.md:189 arc* band; #527/#529).
Y0_TENT = 0.1428       # tent edge (arc* = 0.96)
Y0_ELASTICA = 0.4153   # elastica edge (arc* = 0.70)


def bond_tension(amplitude: float | np.ndarray) -> np.ndarray:
    """Φ'(A) = k0·(A√(1−A²)+arcsin A)/2 — the canonical kernel potential's first
    derivative (the bond tension). Re-derived here, NOT imported from #526."""
    a = np.asarray(amplitude, dtype=float)
    return K0 * (a * np.sqrt(np.clip(1.0 - a**2, 0.0, 1.0)) + np.arcsin(np.clip(a, -1.0, 1.0))) / 2.0


def saturation(amplitude: float | np.ndarray) -> np.ndarray:
    """S(A) = √(1 − (A/A_yield)²), A_yield = 1 in kernel units (Ax4)."""
    a = np.asarray(amplitude, dtype=float)
    return np.sqrt(np.clip(1.0 - a**2, 0.0, 1.0))


def k_trans_cold() -> float:
    """(a) COLD: pump off. k_trans = k_s·S(0) + Φ'(0)/ℓ = k_s."""
    return float(K_S * saturation(0.0) + bond_tension(0.0) / ELL)


def held_bow_geometry(y_bias: float) -> tuple[float, float]:
    """Honest held-bow geometry (alternating +y/−y, u=0): L = √(1 + (2 y_bias)²),
    axial strain A_bond = L − 1. Returns (L, A_bond). This uses the SAME bond-length
    function the dynamics use — the whole point of the liveness control."""
    L = float(np.sqrt(1.0 + (2.0 * y_bias) ** 2))
    return L, L - 1.0


def k_trans_dc_liveness(y_bias: float) -> float:
    """(b) DC-BIAS liveness (held static bow y_bias): the merged #526 form with BOTH
    terms (constitutive-at-Q + T/ℓ geometric). This is the structural-null stencil
    guard prediction — the probe MUST see this nonzero excess over cold."""
    L, A_bond = held_bow_geometry(y_bias)
    T_dc = float(bond_tension(A_bond))
    return float(K_S * saturation(A_bond) + T_dc / L)


def k_trans_pump_dc_only() -> float:
    """(c) PUMP, ARM DC_ONLY: the pump's mean bow is 0, so T = Φ'(0) = 0 in the slot;
    the traveling wave loads nothing; the probe recovers cold stiffness."""
    return k_trans_cold()


def k_trans_pump_extended(y0: float) -> float:
    """(c) PUMP, ARM EXTENDED: the cycle-averaged rectified ⟨T⟩ = (k_a/ℓ)y0² enters
    the slot; the probe reads stiffer than cold."""
    return float(K_S + (K_A / ELL) * y0**2)


def arm_separation(y0: float) -> float:
    """Fractional transverse-stiffness separation between the arms = (k_a/ℓ)y0²/k_s."""
    return float((K_A / ELL) * y0**2 / K_S)


@dataclass(frozen=True)
class FrozenPredictions:
    """The frozen prediction table at a given pump amplitude y0."""

    y0: float
    cold: float
    dc_liveness: float
    pump_dc_only: float
    pump_extended: float
    separation_frac: float

    def as_dict(self) -> dict:
        return {
            "y0": self.y0,
            "cold": self.cold,
            "dc_liveness": self.dc_liveness,
            "pump_dc_only": self.pump_dc_only,
            "pump_extended": self.pump_extended,
            "separation_frac": self.separation_frac,
            "velocity_separation_frac": float(np.sqrt(1.0 + self.separation_frac) - 1.0),
        }


def frozen_predictions(y0: float = Y0_TENT) -> FrozenPredictions:
    return FrozenPredictions(
        y0=y0,
        cold=k_trans_cold(),
        dc_liveness=k_trans_dc_liveness(y0),
        pump_dc_only=k_trans_pump_dc_only(),
        pump_extended=k_trans_pump_extended(y0),
        separation_frac=arm_separation(y0),
    )


def symbolic_backbone() -> dict:
    """Re-derive the 5 load-bearing identities symbolically (sympy). Returns the
    exact-zero residuals. Called by the test to lock the derivation."""
    import sympy as sp

    a, A, k0, l, k_a, y0, theta = sp.symbols("a A k0 l k_a y0 theta", positive=True)
    Phi_dd = k0 * sp.sqrt(1 - a**2)
    T_closed = k0 * (A * sp.sqrt(1 - A**2) + sp.asin(A)) / 2
    T_integral = sp.integrate(Phi_dd, (a, 0, A))
    mean_sin2 = sp.integrate(sp.sin(theta) ** 2, (theta, 0, 2 * sp.pi)) / (2 * sp.pi)
    T_pump_lead = 2 * (k_a / l) * (y0**2 * mean_sin2)
    return {
        "R1_tension_integral": sp.simplify(T_integral - T_closed),
        "R2_phi_prime_0": sp.simplify(T_closed.subs(A, 0)),
        "R3_phi_prime_1_minus_pik0_4": sp.simplify(T_closed.subs(A, 1) - k0 * sp.pi / 4),
        "R4_mean_sin2_minus_half": sp.simplify(mean_sin2 - sp.Rational(1, 2)),
        "R5_pump_lead_minus_law": sp.simplify(T_pump_lead - k_a / l * y0**2),
    }


if __name__ == "__main__":
    resid = symbolic_backbone()
    print("Symbolic backbone (all must be 0):")
    for k, v in resid.items():
        print(f"  {k} = {v}")
    for y0 in (Y0_TENT, Y0_ELASTICA):
        p = frozen_predictions(y0)
        print(f"\ny0={y0}:")
        for kk, vv in p.as_dict().items():
            print(f"  {kk} = {vv}")
