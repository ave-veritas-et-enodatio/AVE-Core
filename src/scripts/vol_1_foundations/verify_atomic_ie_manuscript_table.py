"""
Verify ionization_energy_e2k(Z) reproduces the manuscript validation table.

Locks in the substrate-native restoration arc (doc 100 §10.16-§10.29) by failing
on any drift beyond ±0.5% from the manuscript table. The 14 reference values
were generated against `ionization_energy_e2k(Z)` at parent-repo commit 0401388
(2026-04-09) per A47 v11c commit-SHA-anchoring discipline.

Reference table source:
    manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/
        ionization-energy-validation.md

Empirical verification chain:
    Ax 1 (LC Network) → Helmholtz solution → |ψ|² standing-wave amplitude
    Ax 2 (Gauss)     → CDF screening σ_n(r) → Z_eff(r)
    Op3 (reflection) → Phase B Hopf coupling, Correction B at saturated boundary
    Op5/Op6 (cascade)→ Phase A½ ABCD stub at inner port
    Op10 (junction)  → co-resonant boundary Op10 with c=2 fixed crossings
    Ax 3 (least action) → S_11=0 eigenvalue criterion
    Ax 4 (saturation)→ Op14 + r_yield boundary

If this verify script fails:
    The IE solver has drifted from manuscript-table reproducibility. Either
    (a) re-derive the manuscript table against the current solver and update
    the table values + their SHA pin, or (b) revert the solver change that
    caused the drift. Per A47 v11d, any solver change replacing axiom-chain-
    anchored docstrings with non-derivation hand-waves should have been
    flagged at PR time before reaching merge.

This file: src/scripts/vol_1_foundations/verify_atomic_ie_manuscript_table.py
"""

import sys

from ave.solvers.radial_eigenvalue import ionization_energy_e2k


# Manuscript validation table values (eV).
# Source: manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/
#         ionization-energy-validation.md
# Computed against ionization_energy_e2k(Z) at parent-repo SHA 0401388
# (2026-04-09 manuscript-add commit). Pinned here per A47 v11c discipline.
MANUSCRIPT_IE_TABLE_eV = {
    1:  13.606,
    2:  24.370,
    3:   5.525,
    4:   9.280,
    5:   8.065,
    6:  11.406,
    7:  14.465,
    8:  13.618,
    9:  17.194,
    10: 21.789,
    11:  5.071,
    12:  7.591,
    13:  5.937,
    14:  8.147,
}

# Tolerance per A47 v11c manuscript-vs-code drift discipline.
# Set to 0.5% — manuscript text claims "±2.8% maximum error with zero adjustable
# parameters", but reproducibility against the manuscript-add solver state is
# what we lock here, not experimental agreement. The 0.5% gate catches drift
# from the pinned solver state without false-flagging the small corrections
# applied post-manuscript (e.g., 3c4870c Hopf back-EMF: O at -0.14% from table).
TOLERANCE_FRAC = 0.005  # 0.5%


def verify():
    print("=" * 60)
    print("AVE Atomic Ionization Energy — Manuscript Table Verifier")
    print("Locks in substrate-native restoration arc per doc 100 §10.16+")
    print("=" * 60)
    print()
    print(f"Tolerance: ±{TOLERANCE_FRAC * 100:.1f}% per A47 v11c discipline")
    print(f"Reference: parent-repo SHA 0401388 (2026-04-09 manuscript-add)")
    print()
    print(f"{'Z':>3} {'Element':<3} {'Table':>10} {'Code':>10} {'Gap%':>8} {'Status':<6}")
    print("-" * 50)

    elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F",
                "Ne", "Na", "Mg", "Al", "Si"]
    failed = 0
    max_gap = 0.0

    for Z in sorted(MANUSCRIPT_IE_TABLE_eV.keys()):
        table_val = MANUSCRIPT_IE_TABLE_eV[Z]
        code_val = ionization_energy_e2k(Z)
        if isinstance(code_val, tuple):
            code_val = code_val[0]
        gap = abs(code_val - table_val) / table_val
        max_gap = max(max_gap, gap)
        status = "✓" if gap <= TOLERANCE_FRAC else "✗ FAIL"
        if gap > TOLERANCE_FRAC:
            failed += 1
        print(f"{Z:>3} {elements[Z-1]:<3} {table_val:>10.4f} "
              f"{code_val:>10.4f} {gap*100:>+7.3f}% {status:<6}")

    print("-" * 50)
    print()

    if failed == 0:
        print(f"[Verify] PASS — all {len(MANUSCRIPT_IE_TABLE_eV)} elements "
              f"within ±{TOLERANCE_FRAC*100:.1f}%, max gap {max_gap*100:.3f}%")
        return 0
    else:
        print(f"[Verify] FAIL — {failed}/{len(MANUSCRIPT_IE_TABLE_eV)} "
              f"elements exceed ±{TOLERANCE_FRAC*100:.1f}% tolerance")
        print()
        print("Drift detection: solver has diverged from manuscript-table state.")
        print("Per A47 v11d: any solver change replacing axiom-chain-anchored")
        print("docstrings with hand-waves should have been flagged at PR time.")
        print("See research/_archive/L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md")
        return 1


if __name__ == "__main__":
    sys.exit(verify())
