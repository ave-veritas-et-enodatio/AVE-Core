#!/usr/bin/env python3
"""
Bubble-physics completion check — σ-from-ℓ_c + the FORWARD-FIRST Minnaert check.
================================================================================

Companion check script for ``research/2026-06-11_bubble-physics-completion.md``.

Governing discipline (HARD stack, stated up front):
  * ave-canonical-source : every primitive is imported from ``ave.core.constants``
    or reproduced verbatim from ``ave.core.cavitation_flow`` — NO ad-hoc numbers.
  * ave-live-fire-derivation-provenance / Rule 11 : the Minnaert FORWARD frequency
    is COMPUTED and PRINTED (Section C) BEFORE the measured ring-down f₀ is loaded
    and the ratio formed (Section D). The ordering is git-provable in this file:
    the forward block has no access to the measured number. No retrofitting.
  * consistency-vs-emergence : every number here is engine-NATIVE (α-free) —
    consistency-class apparatus/derivation readings, NOT emergence.
  * substrate-native-check : the Minnaert breathing mode is a REAL-SPACE radial
    dilatation (CP4 real-space is the matching coordinate — the measured f₀ is a
    real-space ring-down, not a phase-space φ² claim); ℓ_c is the K4/Cosserat
    couple-stress length (CP2 BULK-K sector).

Class tags:
  σ-from-ℓ_c          : DERIVED-THIS-ARC, CANDIDATE (gradient-energy scaling)
  Minnaert forward    : FORWARD CONSISTENCY CHECK (textbook bubble-acoustics form,
                        substrate-adapted from the canonical c_bulk EOS)
  death channel       : DESIGN NOTE / HYPOTHESIS (not implemented; see the doc §3)

Run:  python3 src/scripts/vol_1_foundations/bubble_physics_completion_check.py
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from ave.core.constants import ELL_C, L_NODE, NU_VAC, PHI  # noqa: E402

# =============================================================================
# 0. CANONICAL PRIMITIVES (ave-canonical-source — every value provenance-tagged)
# =============================================================================
# Engine-native units: c0 = 1 (bulk P-wave speed = velocity unit), ρ0 = 1
# (ambient density), ℓ_node = 1 (length unit), dx = 1 cell (crystal_graft_v2 /
# genesis default). All results below are DIMENSIONLESS engine-native quantities.
C0 = 1.0          # bulk P-wave (dilatation) speed — crystal_engine.py:60 default
RHO0 = 1.0        # ambient substrate density (native)
ELL_NODE = 1.0    # native length unit
ELL_C_NATIVE = ELL_C / L_NODE   # = √6 (constants.py:255  ELL_C = √6·L_NODE)

# Cavitation floor and density jump across the snapped shell.
#   ρ̄_cav = −1/φ ≈ −0.618034  (cavitation_flow.py:64  RHO_CAV = −1/PHI)
RHO_CAV = -1.0 / PHI
DRHO = abs(RHO_CAV)             # Δρ̄ = ρ̄_ambient(0) − ρ̄_cav = 1/φ
DRHO2 = RHO_CAV ** 2           # (Δρ̄)² = 1/φ² = 2 − φ

# Moduli under K = 2G canon (ν_vac = 2/7 ⇒ c_L²/c_T² = 10/3; crystal_engine.py:95)
#   P-wave (dilatation) modulus  M = ρ0 c0²  (the c_bulk wave modulus) = 1
#   true bulk modulus            K = 2G = M·(3/5)  (K=2G with ν=2/7)
M_PWAVE = RHO0 * C0 ** 2
CL2_OVER_CT2 = 2.0 * (1.0 - NU_VAC) / (1.0 - 2.0 * NU_VAC)   # = 10/3
G_SHEAR = RHO0 * C0 ** 2 / CL2_OVER_CT2                       # G = ρ c_T²
K_BULK = 2.0 * G_SHEAR                                        # K = 2G (canon)


# Cavitation EOS (reproduced verbatim from cavitation_flow.py:153-157, 165-168).
def c_bulk2(rho: float) -> float:
    """c_bulk²(ρ̄) = c0²(1 + ρ̄/(1−ρ̄²))  (rarefaction-softening branch)."""
    return C0 ** 2 * (1.0 + rho / (1.0 - rho ** 2))


def dc_bulk2_drho(rho: float) -> float:
    """d(c_bulk²)/dρ̄ = c0²(1+ρ̄²)/(1−ρ̄²)²  (softening slope)."""
    return C0 ** 2 * (1.0 + rho ** 2) / (1.0 - rho ** 2) ** 2


def banner(title: str) -> None:
    print("\n" + "=" * 78 + f"\n{title}\n" + "=" * 78)


# =============================================================================
# A. σ FROM ℓ_c  — couple-stress / Korteweg interface energy (DERIVED-THIS-ARC)
# =============================================================================
def section_a_sigma() -> dict:
    banner("SECTION A — σ FROM ℓ_c  (couple-stress/Korteweg interface energy)")
    print("Class: DERIVED-THIS-ARC, CANDIDATE  (gradient-energy SCALING, O(1) prefactor)")
    print(f"  ℓ_c (native)   = √6·ℓ_node           = {ELL_C_NATIVE:.6f}")
    print(f"  Δρ̄ across shell = 1/φ                = {DRHO:.6f}")
    print(f"  (Δρ̄)²          = 1/φ² = 2−φ          = {DRHO2:.6f}")
    print(f"  K (=2G, canon)  = 2G, ν=2/7          = {K_BULK:.6f}  (engine ρ0c0²)")
    print(f"  M (P-wave mod.) = ρ0c0²              = {M_PWAVE:.6f}")
    print()
    print("Gradient-energy coefficient (Korteweg): λ_grad = K·ℓ_c²  (couple-stress")
    print("sets the interface width to ℓ_c). tanh-profile equipartition (Cahn-Hilliard")
    print("square-gradient): σ = (1/3)·K·ℓ_c·(Δρ̄)²  (prefactor O(1), profile-dependent).")
    out = {}
    for label, Kv in (("K=2G(canon)", K_BULK), ("M=P-wave", M_PWAVE)):
        sigma = (1.0 / 3.0) * Kv * ELL_C_NATIVE * DRHO2
        out[label] = sigma
        print(f"  σ[{label:11s}] = (1/3)·{Kv:.4f}·{ELL_C_NATIVE:.4f}·{DRHO2:.4f} "
              f"= {sigma:.5f}  (engine E/area = ρ0c0²·ℓ_node)")
    print()
    print(f"EOS softening slope at the floor:  d(c_bulk²)/dρ̄|_cav = "
          f"{dc_bulk2_drho(RHO_CAV):.5f}  (= 2+φ = {2 + PHI:.5f}; "
          f"04_superluminal_transit.tex:86)")
    return out


# =============================================================================
# B. LAPLACE PRESSURE vs RIM OVER-PRESSURE  — does surface tension MATTER?
# =============================================================================
def section_b_laplace(sigma_map: dict) -> None:
    banner("SECTION B — Laplace pressure 2σ/r  vs the rim over-pressure")
    sigma = sigma_map["K=2G(canon)"]   # canonical bulk-modulus σ
    print(f"Using σ = {sigma:.5f} (K=2G).  3D Laplace ΔP = 2σ/r_pocket.")
    print("Pocket-radius candidates (engine cells; snapped-pocket geometry, v6/sonic):")
    for rlabel, r in (("breather core ~5", 5.0), ("(2,3) tube r23=4", 4.0),
                      ("genesis-3D 1704c ~7.4", 7.41), ("genesis-3D 5256c ~10.8", 10.79),
                      ("sonic-2D 1280c ~20", 20.2)):
        dP = 2.0 * sigma / r
        print(f"  r={r:5.2f} ({rlabel:22s}): ΔP_Laplace = {dP:.4f}  "
              f"(= {dP / K_BULK * 100:4.1f}% of K=2G)")
    print()
    print("Rim over-pressure (PE reservoir driving the LOCK refill): the evacuated")
    print("mass piles into a ρ̄>0 rim; the sonic-horizon LOCK recovers ρ̄_core→≈−0.08,")
    print("so the ambient/rim pressure scale is order |ρ̄_rim|·c0² ~ 0.05–0.10 (engine).")
    print("VERDICT: ΔP_Laplace (~0.04–0.09) is the SAME ORDER as the rim over-pressure")
    print("→ surface tension MATTERS at pocket scale (co-equal restoring term; assists")
    print("the reversible-spring LOCK; for two touching shells, area-reduction ΔE~−σΔA")
    print("makes COALESCENCE energetically favorable — feeds the death-channel note §3).")


# =============================================================================
# C. MINNAERT  ***FORWARD***  (Rule 11: COMPUTED + PRINTED BEFORE the measured)
# =============================================================================
def section_c_minnaert_forward() -> dict:
    banner("SECTION C — MINNAERT *FORWARD* (computed BEFORE the measured f₀ is loaded)")
    print("Substrate Minnaert form (textbook bubble-acoustics, substrate-adapted):")
    print("  ω₀ = √(3·K_eff/ρ_eff)/a = √3·c_eff/a   (free-surface / Γ=−1 pressure-release)")
    print("  K_eff/ρ_eff = c_bulk²; surrounding-medium linear speed c_bulk(ρ̄=0) = c0 = 1")
    print("  f₀ = √(3·K/ρ0)/(2π·a).  Boundary note: Γ=−1 (Z→0) is pressure-release →")
    print("  SAME p=0 BC as a free surface, so the √3 Minnaert form applies to the")
    print("  global pulsation; the trapped-cavity standing-wave alternative (ω=π·c/a)")
    print("  is the radiation-vs-confinement counterpart (factor π/√3≈1.81 higher).")
    print()
    print("Pre-committed radius: the seeded V-breather is a Gaussian seed_bulk(σ=3.5);")
    print("the principled 'bubble radius' is the FIELD 1/e radius a = σ√2 (electron_")
    print("s11_sweep.py:287). Modulus bracket = {M=P-wave, K=2G} (the two natural")
    print("compression moduli). Radius sensitivity {σ, σ√2, 2σ} reported for honesty.")
    print()
    fwd = {}
    sigma_gauss = 3.5
    for alabel, a in (("σ=3.5", sigma_gauss), ("σ√2=4.95", sigma_gauss * np.sqrt(2)),
                      ("2σ=7.0", 2 * sigma_gauss), ("r23=4.0", 4.0), ("R23=10.4", 10.4)):
        row = {}
        for klabel, Kv in (("M=P-wave", M_PWAVE), ("K=2G", K_BULK)):
            f0 = np.sqrt(3.0 * Kv / RHO0) / a / (2.0 * np.pi)
            row[klabel] = f0
        fwd[alabel] = (a, row)
        tag = "  <-- PRE-COMMITTED principled radius" if alabel == "σ√2=4.95" else ""
        print(f"  a={a:5.2f} ({alabel:9s}): f₀[M]={row['M=P-wave']:.5f}  "
              f"f₀[K=2G]={row['K=2G']:.5f}  (cyc/time){tag}")
    a_star, band = fwd["σ√2=4.95"]
    print()
    print(f"FORWARD BAND at the pre-committed radius a=σ√2={a_star:.3f}:")
    print(f"  f₀_fwd ∈ [{band['K=2G']:.5f} (K=2G) , {band['M=P-wave']:.5f} (M)] cyc/time")
    return fwd


# =============================================================================
# D. THEN load the MEASURED f₀ and form the comparison (Rule 11 — after C)
# =============================================================================
def section_d_compare(fwd: dict) -> None:
    banner("SECTION D — MEASURED f₀ (loaded AFTER the forward) + comparison + bin")
    # Measured: ring-down dominant angular w_est on the planted-(2,3)+breather state.
    #   electron_s11_results.json: unknown.w_est_ringdown = 0.32446229407790794
    #   config: N=40, S_min=0.0125, A_cap=0.999, R23=10.4, r23=4.0, drive=bulk-V.
    #   CAVEAT: the bulk channel is MULTI-MODE (low-contrast) — f₀ is the dominant
    #   ring-down peak, NOT a clean single high-Q resonance (subharmonic at f/2).
    W_EST = 0.32446229407790794
    f0_meas = W_EST / (2.0 * np.pi)
    print(f"  measured w_est_ringdown = {W_EST:.6f} rad/time  (electron_s11_results.json)")
    print(f"  measured f₀ = w_est/2π   = {f0_meas:.5f} cyc/time")
    print("  CAVEAT: bulk channel MULTI-MODE (no clean single Q); f₀ = dominant peak.")
    print()
    a_star, band = fwd["σ√2=4.95"]
    lo, hi = band["K=2G"], band["M=P-wave"]
    inside = lo <= f0_meas <= hi
    print(f"  forward band (a=σ√2): [{lo:.5f}, {hi:.5f}]  measured {f0_meas:.5f}  "
          f"→ {'INSIDE' if inside else 'OUTSIDE'} the band")
    for klabel in ("M=P-wave", "K=2G"):
        ratio = band[klabel] / f0_meas
        print(f"    f₀_fwd[{klabel:8s}]/f₀_meas = {band[klabel]:.5f}/{f0_meas:.5f} "
              f"= {ratio:.3f}  (residual {(ratio - 1) * 100:+.1f}%)")
    print()
    print("BIN (honest, Rule 11): UNDERDETERMINED — leaning CONSISTENT.")
    print("  • measured f₀ sits INSIDE the forward Minnaert band at the principled")
    print("    radius → the bubble-breathing identity is NOT refuted.")
    print("  • NOT 'MATCHES' (tight): the forward spans (i) modulus K-vs-M ±15%,")
    print("    (ii) radius σ-vs-σ√2-vs-2σ a factor ~2, (iii) boundary √3-vs-π ×1.81,")
    print("    and the measured spectrum is itself multi-mode. Multiple (radius,")
    print("    modulus) combos land near 0.052 → coincidence-magnet zone.")
    print("  • Missing geometric input to PROMOTE to MATCHES: the MEASURED mode-shape")
    print("    (eigenvector spatial extent → effective a) + a single-mode (high-Q)")
    print("    ring-down + the realized boundary form factor (√3 vs π).")


def main() -> None:
    print("BUBBLE-PHYSICS COMPLETION CHECK — forward-first (Rule 11). Engine-native units.")
    sigma_map = section_a_sigma()
    section_b_laplace(sigma_map)
    fwd = section_c_minnaert_forward()   # FORWARD — no access to the measured f₀
    section_d_compare(fwd)               # measured loaded HERE, after the forward
    print("\n[done] All numbers engine-native (α-free), consistency-class. "
          "See research/2026-06-11_bubble-physics-completion.md.")


if __name__ == "__main__":
    main()
