"""F17-K bootstrap calibration (B) — constants-level scalar verification.

Per the single-bond test finding (`single_bond_q_test.py`): bare K4-TLM
single-bond doesn't manifest LC-tank Compton resonance — it gives 2-step
scatter+connect grid dispersion. The LC-tank physics of Vol 4 Ch 1 is a
CONTINUUM analog that requires the Cosserat sector for kinetic inductance.

This script does the (B) constants-level verification: compute L_e, C_e,
R_TIR from engine constants and check that the corpus formulas for
ω = ω_Compton and Q = 1/α = 137.036 are self-consistent. No simulation;
just constants check via the algebraic chain in doc 16_/17_:

    L_e   = ξ_topo⁻² · m_e   = (ℓ_node/e)² · m_e
    ω·L_e = ℏ/e²                                       (doc 16_)
    R_TIR = Z_0/(4π)         (saturation-boundary impedance)
    Q     = ω·L_e / R_TIR    = 1/α

If these all wire up to the SI experimental values (m_e, e, c, ℏ), the
bootstrap chain is calibration-clean. If anything is off by a factor,
that's a load-bearing finding for any further numerical claim.
"""
from __future__ import annotations
import sys

sys.path.insert(0, "/Users/grantlindblom/AVE-staging/AVE-Core/src")

import numpy as np
from ave.core.constants import (
    C_0, M_E, e_charge, HBAR, ALPHA, Z_0, L_NODE,
)


def main() -> None:
    print("=" * 78)
    print("  Bootstrap calibration (B): constants-level Q = 1/α verification")
    print("=" * 78)

    # ─── SI input constants ──────────────────────────────────────────────
    print("\n  SI input constants:")
    print(f"    c       = {C_0:.6e} m/s")
    print(f"    m_e     = {M_E:.6e} kg")
    print(f"    e       = {e_charge:.6e} C")
    print(f"    ℏ       = {HBAR:.6e} J·s")
    print(f"    Z_0     = {Z_0:.4f} Ω")
    print(f"    α (CODATA) = {ALPHA:.6e}")
    print(f"    ℓ_node  = ℏ/(m_e·c) = {L_NODE:.6e} m")

    # ─── Derived quantities ──────────────────────────────────────────────
    print("\n  Derived (corpus formulas):")
    xi_topo = e_charge / L_NODE
    print(f"    ξ_topo  = e/ℓ_node = {xi_topo:.6e} C/m")

    L_e = (L_NODE / e_charge) ** 2 * M_E  # = ξ_topo⁻² · m_e
    print(f"    L_e     = ξ_topo⁻²·m_e = (ℓ_node/e)²·m_e = {L_e:.6e} H")

    omega_compton = M_E * C_0 ** 2 / HBAR
    print(f"    ω_C     = m_e·c²/ℏ = {omega_compton:.6e} rad/s")

    R_TIR = Z_0 / (4 * np.pi)
    print(f"    R_TIR   = Z_0/(4π) = {R_TIR:.4f} Ω")

    # ─── Identity check: ω_C · L_e =? ℏ/e² ───────────────────────────────
    print("\n  Identity check: ω_C·L_e vs ℏ/e² (doc 16_)")
    omega_L = omega_compton * L_e
    h_over_e2 = HBAR / e_charge ** 2
    print(f"    ω_C · L_e        = {omega_L:.6e} Ω")
    print(f"    ℏ/e²             = {h_over_e2:.6e} Ω (Klitzing/2π)")
    print(f"    Ratio            = {omega_L / h_over_e2:.6f}  (expect 1.0 if formulas consistent)")
    relative_error_1 = abs(omega_L - h_over_e2) / h_over_e2
    print(f"    Relative error   = {relative_error_1:.3e}")

    # ─── Q-factor calculation ────────────────────────────────────────────
    print("\n  Q-factor calculation:")
    Q_corpus = omega_L / R_TIR
    Q_alpha_inv = 1.0 / ALPHA
    print(f"    Q = ω_C·L_e / R_TIR = {omega_L:.4e} / {R_TIR:.4f} = {Q_corpus:.4f}")
    print(f"    1/α (CODATA)        = {Q_alpha_inv:.4f}")
    print(f"    Ratio Q/Q_α         = {Q_corpus / Q_alpha_inv:.6f}  (expect 1.0)")
    relative_error_2 = abs(Q_corpus - Q_alpha_inv) / Q_alpha_inv
    print(f"    Relative error      = {relative_error_2:.3e}")

    # ─── Z_0 cross-check via α definition ────────────────────────────────
    print("\n  Cross-check: α = e²·Z_0 / (4π·ℏ)")
    alpha_from_Z0 = e_charge ** 2 * Z_0 / (4 * np.pi * HBAR)
    print(f"    α (computed) = e²·Z_0/(4π·ℏ) = {alpha_from_Z0:.6e}")
    print(f"    α (constant) = {ALPHA:.6e}")
    print(f"    Ratio        = {alpha_from_Z0 / ALPHA:.6f}")

    # ─── C_e extraction via ω = 1/√(LC) ──────────────────────────────────
    print("\n  Bond capacitance C_e (via ω = 1/√(L_e·C_e)):")
    C_e_from_omega = 1.0 / (omega_compton ** 2 * L_e)
    print(f"    C_e          = 1/(ω_C²·L_e) = {C_e_from_omega:.6e} F")

    # Cross-check: C_e should equal ε_0·ℓ_node²/ℓ_node = ε_0·ℓ_node up to
    # geometric factors (parallel-plate capacitor approximation at bond scale)
    epsilon_0 = 1.0 / (Z_0 * C_0)
    C_e_geometric = epsilon_0 * L_NODE
    print(f"    ε_0·ℓ_node   = {C_e_geometric:.6e} F  (parallel-plate approx)")
    print(f"    Ratio        = {C_e_from_omega / C_e_geometric:.4f}  "
          f"(expect ~1 up to π factors per Vol 4 Ch 1)")

    # ─── Summary ─────────────────────────────────────────────────────────
    print("\n" + "=" * 78)
    print("  SUMMARY")
    print("=" * 78)
    if relative_error_1 < 1e-10 and relative_error_2 < 1e-10:
        verdict = "PASS"
    elif relative_error_1 < 1e-6 and relative_error_2 < 1e-6:
        verdict = "PASS (numerical precision)"
    else:
        verdict = "FAIL"
    print(f"  Identity  ω·L_e = ℏ/e²   : {'✓' if relative_error_1 < 1e-6 else '✗'} "
          f"(rel_err={relative_error_1:.2e})")
    print(f"  Identity  Q     = 1/α    : {'✓' if relative_error_2 < 1e-6 else '✗'} "
          f"(rel_err={relative_error_2:.2e})")
    print(f"  Verdict: {verdict}")

    print(f"\n  Bootstrap-chain calibration: {verdict}")
    print(f"    The corpus Q-factor formula (ω·L_e/R_TIR = 1/α = 137.036) is")
    print(f"    self-consistent at the SI input-constants level. ω_C·L_e =")
    print(f"    ℏ/e² (Klitzing/2π) holds as a definitional identity from")
    print(f"    L_e = ξ_topo⁻²·m_e + ℓ_node = ℏ/(m_e·c).")
    print(f"")
    print(f"    Note: this is an ALGEBRAIC verification, not empirical. The")
    print(f"    formulas wire up consistently because they're chained through")
    print(f"    the SI constants (m_e, e, c, ℏ). Empirical Q manifestation in")
    print(f"    the lattice would require a working bound-state Compton")
    print(f"    resonance — which F17-K v3(i) showed is NOT linearly stable")
    print(f"    in the coupled engine at Golden Torus.")


if __name__ == "__main__":
    main()
