"""
AVE MODULE: Regime IV — Universal Topological Rupture Solver
============================================================
This module enforces the mathematical boundaries of Axiom 4: Dielectric Saturation.
When the dimensionless saturation parameter `r` (shear strain, voltage ratio, etc.)
reaches or exceeds 1.0, the underlying LC vacuum lattice physically ruptures.

DERIVATION OF c_eff AND Z_eff — First Principles
-------------------------------------------------

Two physically distinct saturation symmetry cases exist.  The solver reports
both explicitly so callers can select the appropriate quantity.

CASE A — ASYMMETRIC saturation (dielectric-only, e.g. EM wave in strong field):
    ε_eff = ε₀ · S           (permittivity collapses with strain)
    μ_eff = μ₀              (permeability unchanged)
    Z_EM  = √(μ₀ / ε₀·S) = Z₀ / √S   (impedance RISES — medium opaque)
    c_EM  = 1/√(μ₀ · ε₀·S) = c₀ / √S  (EM phase velocity RISES)

    Physical note: c > c₀ is not superluminal information — it is the
    phase velocity of evanescent modes in a collapsing dielectric.
    No energy propagates superluminally; the group velocity → 0.

CASE B — SYMMETRIC saturation (both μ and ε scale by S, e.g. BH interior):
    ε_eff = ε₀ · S
    μ_eff = μ₀ · S
    Z_sym  = √(μ₀·S / ε₀·S) = Z₀            (impedance INVARIANT)
    c_EM_sym = 1/√(μ₀·S · ε₀·S) = c₀ / S    (EM phase velocity RISES as S→0)

    The impedance-invariance of symmetric saturation is documented in the
    LIVING_REFERENCE "Confinement theorem" and is the reason the BH interior
    shows Γ=0 for transverse EM perturbations (perfect absorber, not reflector).

SHEAR WAVE / GW PROPAGATION (applies in both cases):
    Transverse shear waves (gravitational waves, phonons, soliton group velocity)
    travel at the SHEAR speed, not the EM phase speed.  The shear modulus is:
        G_shear = G₀ · S        (Axiom 4: shear stiffness collapses with strain)

    The shear wave speed is derived from v = √(G/ρ):
        c_shear = c₀ · √(G_shear/G₀) = c₀ · √S = c₀ · (1−r²)^{1/4}

    As S → 0: c_shear → 0  (GWs freeze, solitons stop → rest mass).
    This is the "wave packet freezes" entry in the Axiom 4 table.

SUMMARY — which quantity maps to which physical observable:
    c_EM_asym  = c₀ / √S   — EM phase velocity in dielectric-only collapse
    c_EM_sym   = c₀ / S    — EM phase velocity in symmetric (BH) collapse
    c_shear    = c₀ · √S   — GW / soliton group velocity in ALL cases
    Z_EM_asym  = Z₀ / √S   — EM impedance in dielectric-only collapse
    Z_sym      = Z₀         — EM impedance in symmetric collapse (invariant)

In Regime IV (r >= 1.0):
    S = 0: all constitutive parameters vanish.
    c_shear = 0: topology melted, no transverse propagation.
    Z_asym → ∞ (dielectric void), Z_sym = Z₀ (perfect absorber, Γ=0).
"""

from __future__ import annotations


import numpy as np
from ave.core.constants import C_0, Z_0, EPSILON_0, MU_0
from ave.core.universal_operators import universal_saturation


class TopologicalRuptureSolver:
    @staticmethod
    def evaluate_rupture_state(r_param: float | np.ndarray) -> dict:
        """
        Evaluate the macroscopic state variables of a system at saturation r.

        Args:
            r_param: The dimensionless Axiom 4 stress ratio (r = A / A_c).
                     r = 0: linear regime.  r = 1: rupture boundary.  r > 1: ruptured interior.

        Returns:
            Dictionary of effective state variables.  Key derivations (see module docstring):

            - 'S'           : Axiom 4 saturation factor √(1−r²) ∈ [0,1]
            - 'is_ruptured' : bool array, True where r ≥ 1.0

            SYMMETRIC saturation (both μ and ε scale by S — applies to BH interior,
            symmetric gravity, particle confinement):
            - 'eps_eff_sym' : ε₀·S  — permittivity
            - 'mu_eff_sym'  : μ₀·S  — permeability
            - 'Z_sym'       : Z₀    — impedance INVARIANT (S cancels)
            - 'c_EM_sym'    : c₀/S  — EM phase velocity (rises as S→0; BH interior)

            ASYMMETRIC saturation (only ε scales by S — applies to EM waves in E-field):
            - 'eps_eff_asym': ε₀·S  — permittivity collapses
            - 'mu_eff_asym' : μ₀    — permeability unchanged
            - 'Z_asym'      : Z₀/√S — impedance rises (medium opaque)
            - 'c_EM_asym'   : c₀/√S — EM phase velocity rises (evanescent modes)

            SHEAR WAVE / GW speed (domain-independent — from G_shear = G₀·S):
            - 'c_shear'     : c₀·√S = c₀·(1−r²)^(1/4) → 0 at rupture
              This is the 'wave packet freezes' quantity in the Axiom 4 table.
              Governs: gravitational waves, acoustic phonons, soliton group velocity.
        """
        r_arr = np.atleast_1d(np.asarray(r_param, dtype=float))
        S = np.array([universal_saturation(float(x), 1.0) for x in r_arr])
        S_safe = np.maximum(S, 1e-14)  # guard for division at exact rupture boundary

        is_ruptured = r_arr >= 1.0

        # ── SYMMETRIC saturation (both μ,ε scale by S) ────────────────────────
        eps_eff_sym = float(EPSILON_0) * S
        mu_eff_sym = float(MU_0) * S
        Z_sym = np.full_like(S, float(Z_0))  # Z₀ exactly (S cancels)
        c_EM_sym = float(C_0) / S_safe  # c₀/S → ∞ inside BH

        # ── ASYMMETRIC saturation (only ε scales by S) ────────────────────────
        eps_eff_asym = float(EPSILON_0) * S
        mu_eff_asym = np.full_like(S, float(MU_0))
        Z_asym = float(Z_0) / np.sqrt(S_safe)  # Z₀/√S → ∞ (opaque)
        c_EM_asym = float(C_0) / np.sqrt(S_safe)  # c₀/√S → ∞ (evanescent)

        # ── SHEAR WAVE / GW speed — from G_shear = G₀·S ═══════════════════════
        # Derivation: c_shear = √(G_shear/ρ) = c₀·√(G₀·S/G₀) = c₀·√S
        # Equivalently: c₀·(1−r²)^(1/4) since √S = (1−r²)^(1/4)
        # This → 0 at rupture: topology melted, transverse propagation ceases.
        c_shear = float(C_0) * np.sqrt(S)  # c₀·√S = c₀·(1−r²)^{1/4}

        return {
            "r": r_arr,
            "S": S,
            "is_ruptured": is_ruptured,
            # symmetric
            "eps_eff_sym": eps_eff_sym,
            "mu_eff_sym": mu_eff_sym,
            "Z_sym": Z_sym,
            "c_EM_sym": c_EM_sym,
            # asymmetric
            "eps_eff_asym": eps_eff_asym,
            "mu_eff_asym": mu_eff_asym,
            "Z_asym": Z_asym,
            "c_EM_asym": c_EM_asym,
            # shear / GW
            "c_shear": c_shear,
            # backward-compat alias (was 'c_eff' = c_shear in original code)
            "c_eff": c_shear,
            "eps_eff": eps_eff_asym,  # backward-compat: was eps_eff_asym
            "Z_eff": Z_asym,  # backward-compat: was Z_asym
        }
