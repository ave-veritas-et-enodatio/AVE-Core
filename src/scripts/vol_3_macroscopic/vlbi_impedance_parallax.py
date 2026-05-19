"""
Vol 3 Macroscopic — VLBI Jupiter-grazing Shapiro delay + DAMA crystal-density ratios.

SCOPE NOTE (2026-05-16 audit): This script computes the STANDARD GR SHAPIRO DELAY
n(r) = 1 + 2GM/(rc^2) for a Jupiter-grazing radio path. It does NOT contain any
AVE-distinct operator (no a_0, no eta_eff, no saturation kernel, no xi_topo, no
substrate-physics term). The AVE corpus n(r) = 1 + 2GM/(rc^2) per
manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md:11
is "mathematically identical to the spatial transverse trace of the Gordon optical
metric" (line 14) — i.e., the GR Shapiro integrand. AVE and GR predict the same
Jupiter-grazing delay at O(GM/c^2 r).

Prior versions of this script printed "VLBI maps Dark Matter exactly as an LC
Saturation gradient" — that print statement was unsupported by the code (which
computes Shapiro, not any AVE-distinct DM observable). The C13-VLBI-DARK matrix
row that depended on this driver was retired/split 2026-05-16; the actual derived
AVE DM observables live in simulate_galactic_rotation_curve.py (a_0 + saturation
kernel) and simulate_bullet_cluster_fdtd.py (TT shockwave + a_0). See:
- manuscript/ave-kb/common/closure-roadmap.md §0.5 scope-correction changelog
- manuscript/ave-kb/common/divergence-test-substrate-map.md rows C13a/C13b/C13c

The DAMA section below computes the crystal-density ratio kappa = rho_crystal /
rho_bulk_vacuum but does NOT predict an annual-modulation amplitude. Per the C14
matrix row, the amplitude formula remains a TBD-pin derivation gap.

This script is retained as a Shapiro-baseline reference for any future AVE-distinct
VLBI-class derivation that would need to compute its prediction as a residual above
the GR Shapiro term.
"""

from ave.core.constants import C_0, RHO_BULK, G


def simulate_vlbi_and_dama_parallax() -> None:
    print("--- Vol 3 Macroscopic: VLBI Shapiro baseline + DAMA crystal-density ratios ---")
    print("(NOTE: This script computes standard GR Shapiro delay, not an AVE-distinct DM observable.")
    print(" See module docstring + closure-roadmap.md §0.5 for scope correction 2026-05-16.)")

    # 1. VLBI Jupiter Grazing — standard GR Shapiro delay
    print("\n[1. VLBI Jupiter Grazing — standard GR Shapiro reference baseline]")
    M_jupiter = 1.898e27  # kg
    R_jupiter = 71492  # m

    # n(r) = 1 + 2GM/(rc^2) — standard GR Shapiro integrand
    # AVE n(r) IS this function per Vol 3 Ch 3 Gordon-metric identity (audit 2026-05-16)
    delta_n_jup = (2 * G * M_jupiter) / (R_jupiter * C_0**2)
    print(f"Jupiter Impact Parameter Refractive Shift (Δn, GR/AVE identical): {delta_n_jup:.6e}")

    # Grazing telemetry path L ~ 2 * R_jupiter
    L_path = 2 * R_jupiter
    delay_s = (L_path * delta_n_jup) / C_0
    print(f"Shapiro Delay (Δt, GR/AVE identical): {delay_s * 1e6:.4f} μs")
    print("=> No AVE-distinct prediction at this order. Existing VLBI confirmations of GR Shapiro corroborate AVE = GR identity by construction.")

    # 2. DAMA crystal-density ratios — descriptive only, no amplitude derivation
    print("\n[2. DAMA crystal-density ratios — descriptive only]")
    print("AVE corpus claim (Vol 1 Ch 4 bullet-cluster.md): DAMA annual modulation amplitude")
    print("would scale with crystal-density-to-vacuum-bulk ratio kappa = rho_crystal / rho_bulk.")
    print("The amplitude formula itself is NOT derived in the corpus (C14 matrix row TBD-pin).")
    print(f"AVE Vacuum Bulk Density (RHO_BULK): {RHO_BULK:.2f} kg/m^3")

    crystals = {
        "NaI (DAMA)": 3.67e3,  # kg/m^3
        "Germanium (CDMS)": 5.32e3,
        "Sapphire (Proposed)": 3.98e3,
    }

    for name, density in crystals.items():
        kappa = density / RHO_BULK
        print(f"  {name} kappa = rho_crystal / RHO_BULK: {kappa:.6e}")

    print("\n=> RESULT: Crystal density ratios are computable but the DAMA-amplitude prediction itself is unfinished.")
    print("   Forward AVE-distinct DM observables with derivation chains live in:")
    print("   - simulate_galactic_rotation_curve.py (a_0 + saturation kernel)")
    print("   - simulate_bullet_cluster_fdtd.py (a_0 + TT shockwave)")


if __name__ == "__main__":
    simulate_vlbi_and_dama_parallax()
