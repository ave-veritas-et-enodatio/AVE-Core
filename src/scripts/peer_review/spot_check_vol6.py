"""
§10 Numeric Spot-Check — Volume 6: Periodic Table
====================================================

Independently verifies flagship nuclear constants from the physics engine
against manuscript-stated values in Volume 6.

Run: PYTHONPATH=src python src/scripts/peer_review/spot_check_vol6.py
"""

from ave.core.constants import (
    ALPHA_HC,
    B_DEUTERON_PREDICTED,
    D_INTRA_ALPHA,
    D_NN_EIGENVALUE,
    D_PROTON,
    HBAR_C_MEV_FM,
    K_COUPLING,
    K_MUTUAL,
)

CHECKS = [
    # (Name, Engine Value, Manuscript/Target Value, Unit, Tolerance %)
    ("d (Proton Charge Radius)", D_PROTON, 0.8414, "fm", 0.1),
    ("D_intra (Alpha Tetrahedral Edge)", D_INTRA_ALPHA, 2.379, "fm", 0.1),
    ("d_nn (Eigenvalue NN Distance)", D_NN_EIGENVALUE, 2.056, "fm", 0.5),
    ("B_deuteron (Deuteron Binding)", B_DEUTERON_PREDICTED, 2.2246, "MeV", 2.0),
    ("αℏc (Coulomb Coupling)", ALPHA_HC, 1.440, "MeV·fm", 0.5),
    ("K_coupling (Mutual Inductance)", K_COUPLING, 0.01476, "", 0.5),
    ("K_mutual (Pairwise Binding)", K_MUTUAL, 11.337, "MeV·fm", 2.0),
    ("ℏc (Conversion Factor)", HBAR_C_MEV_FM, 197.33, "MeV·fm", 0.01),
]

print("=" * 90)
print("§10 NUMERIC SPOT-CHECK — Volume 6: Periodic Table")
print("=" * 90)
print()
print(f"{'Constant':<42s} {'Engine':>14s} {'Target':>14s} {'Δ%':>10s} {'Status':>8s}")
print("-" * 90)

all_pass = True
for name, engine_val, target_val, unit, tol_pct in CHECKS:
    if target_val == 0:
        delta_pct = 0.0 if engine_val == 0 else float("inf")
    else:
        delta_pct = abs(engine_val / target_val - 1.0) * 100.0

    status = "✅" if delta_pct <= tol_pct else "❌"
    if status == "❌":
        all_pass = False

    e_str = f"{engine_val:.6f}" if abs(engine_val) < 1e6 else f"{engine_val:.4e}"
    m_str = f"{target_val:.6f}" if abs(target_val) < 1e6 else f"{target_val:.4e}"

    print(f"  {name:<40s} {e_str:>14s} {m_str:>14s} {delta_pct:>9.4f}% {status:>6s}")

print("-" * 90)
print(f"\nVERDICT: {'✅ ALL SPOT-CHECKS PASS' if all_pass else '❌ FAILURES DETECTED'}")
print()
