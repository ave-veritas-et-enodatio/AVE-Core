#!/usr/bin/env python3
"""
Running Fine-Structure Constant from Axiom 4 Dynamic Capacitive Yielding
=========================================================================
STATUS: EXPLORATORY — Does NOT reproduce QED running. See HANDOFF P2.8.

The $q^2 → Δφ$ mapping is not yet derived from first principles.
The discrete hop model collapses all energies above m_e c^2 to depth=1,
producing negligible running. This script documents the investigation
and identifies the specific blocker for future work.

Demonstrates that the "running" of α (vacuum polarization) emerges from
the AVE lattice via nonlinear capacitive yielding (Axiom 4).

PHYSICAL MECHANISM (from KB: electron-unknot.md):
    The baseline α ≈ 1/137.036 is the infrared (zero-strain) coupling.
    As probe energy increases, the local strain Δφ on each lattice node
    increases. Axiom 4 dynamic capacitive yielding:

        C_eff(Δφ) = C_0 / sqrt(1 - (Δφ/α)^2)

    This nonlinear capacitance increase lowers the local impedance Z:
        Z_eff = sqrt(L/C_eff) = Z_0 × sqrt(1 - (Δφ/α)^2)^(1/2)

    The effective coupling (which IS the impedance ratio α = Z_particle/Z_0)
    therefore increases:
        α_eff(Δφ) = α / sqrt(1 - (Δφ/α)^2)

    The strain Δφ at momentum transfer q is the probe's field amplitude
    normalised to the saturation limit. For a point-like probe at distance
    r = ℏ/(m_e c × depth), the strain scales as:
        Δφ/α = α / depth    (one α per hop of Coulomb screening)

ENGINE METHOD:
    We evaluate α_eff by computing the strain at each depth and applying
    the Axiom 4 yielding formula. The radial tree admittance solver is
    used to compute the network S_11 with strain-modified branch
    admittances y_branch(depth) = ν_vac / sqrt(1 - (α/depth)^2).

VALIDATION:
    QED running:  α(0)     ≈ 1/137.036  (Thomson limit)
                  α(M_Z)   ≈ 1/128.9    (LEP measurement at 91.2 GeV)
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import numpy as np

from ave.core.constants import ALPHA, C_0, M_E, e_charge


def alpha_eff_axiom4(energy_mev: float) -> dict:
    """
    Compute effective α at a given energy scale using Axiom 4 yielding.

    The probe energy E sets the spatial resolution: r = ℏc/E.
    The number of lattice hops at this scale: depth = r / l_node = m_e c^2 / E.
    The strain per node at this depth: Δφ = α × (m_e c^2 / E) / depth = α.

    More precisely, the Coulomb field of the probe deposits strain α per
    lattice hop. Over N hops inward from the probe to the vertex, the
    cumulative strain compounds. The effective admittance of each branch
    at depth d is modified by the local Axiom 4 yielding:

        y_eff(d) = ν_vac / sqrt(1 - (α/d)^2)

    where α/d is the fractional strain at depth d (deeper = less strained).
    """
    # Energy → depth: how many lattice hops does this energy correspond to?
    me_c2_mev = M_E * C_0**2 / (e_charge * 1e6)  # ≈ 0.511 MeV
    depth_continuous = me_c2_mev / energy_mev if energy_mev > 0 else 1000
    depth = max(1, int(round(depth_continuous)))

    # Build the tree with strain-modified branch admittances
    # At each shell d (from origin), the local strain is α/d
    # The Axiom 4 yielding modifies the branch admittance:
    #   y_branch(d) = ν_vac / sqrt(1 - (α/d)^2)
    # For the uniform-tree builder, we use the average effective admittance
    # across all shells.

    # Compute the cumulative Axiom 4 α_eff directly from the yielding formula
    # This is the exact KB formula: C_eff = C_0 / sqrt(1 - (Δφ/α)^2)
    # At momentum transfer q with N screening hops:
    # Each hop contributes strain α to the traversed lattice cells
    # The TOTAL accumulated strain from N hops of Coulomb screening:
    #   Δφ_total / α = sum_{d=1}^{depth} (1/d^2) ≈ π²/6 for large depth
    # For finite depth: partial sum of Basel series

    # Partial sum of 1/d^2 from d=1 to depth
    partial_basel = sum(1.0 / d**2 for d in range(1, depth + 1))

    # The strain ratio (dimensionless)
    strain_ratio = ALPHA * partial_basel

    # Axiom 4 dynamic yielding
    if strain_ratio >= 1.0:
        # Full saturation — Landau pole
        alpha_eff = float("inf")
        inv_alpha = 0.0
    else:
        alpha_eff = ALPHA / np.sqrt(1.0 - strain_ratio**2)
        inv_alpha = 1.0 / alpha_eff

    return {
        "energy_mev": energy_mev,
        "depth": depth,
        "partial_basel": partial_basel,
        "strain_ratio": strain_ratio,
        "alpha_eff": alpha_eff,
        "inv_alpha_eff": inv_alpha,
    }


def main():
    print("=" * 72)
    print("  AVE ENGINE: Running α from Axiom 4 Dynamic Capacitive Yielding")
    print("=" * 72)
    print()
    print("  Mechanism: C_eff(Δφ) = C_0 / sqrt(1 - (Δφ/α)²)")
    print("  Strain accumulates as α × Σ(1/d²) over d lattice hops.")
    print()

    # Compute at key energy scales
    energies_mev = [
        0.001,  # Thomson limit (optical)
        0.511,  # Electron mass
        1.0,  # 1 MeV
        10.0,  # 10 MeV
        100.0,  # 100 MeV
        1000.0,  # 1 GeV
        10000.0,  # 10 GeV
        80379.0,  # M_W
        91188.0,  # M_Z
        200000.0,  # 200 GeV
    ]

    print(f"  {'E (MeV)':>10}  {'Depth':>6}  {'Σ(1/d²)':>10}  {'Strain':>10}" f"  {'α_eff':>12}  {'1/α_eff':>8}")
    print("  " + "-" * 66)

    for e in energies_mev:
        r = alpha_eff_axiom4(e)
        if r["inv_alpha_eff"] > 0:
            print(
                f"  {r['energy_mev']:10.1f}  {r['depth']:6d}"
                f"  {r['partial_basel']:10.4f}  {r['strain_ratio']:10.6f}"
                f"  {r['alpha_eff']:12.8f}  {r['inv_alpha_eff']:8.3f}"
            )
        else:
            print(
                f"  {r['energy_mev']:10.1f}  {r['depth']:6d}"
                f"  {r['partial_basel']:10.4f}  {r['strain_ratio']:10.6f}"
                f"  {'SATURATED':>12}  {'∞':>8}"
            )

    print()
    print("  REFERENCE (PDG):")
    print(f"    α(0)     = 1/137.036  (Thomson limit)")
    print(f"    α(M_Z)   = 1/128.9    (LEP measurement)")
    print(f"    α(∞)     → Landau pole (QED prediction)")
    print()

    # Direct comparison at M_Z
    r_mz = alpha_eff_axiom4(91188.0)
    print(f"  AT M_Z ({r_mz['energy_mev']:.0f} MeV):")
    print(f"    AVE:  1/α_eff = {r_mz['inv_alpha_eff']:.3f}")
    print(f"    PDG:  1/α     = 128.9")
    if r_mz["inv_alpha_eff"] > 0:
        error = (r_mz["inv_alpha_eff"] - 128.9) / 128.9 * 100
        print(f"    Deviation:    {error:+.2f}%")
    print()
    print("=" * 72)


if __name__ == "__main__":
    main()
