"""
§10 Numeric Spot-Check — Volume 1: Foundations
================================================

Independently verifies flagship constants from the physics engine
against manuscript-stated values in Volume 1.

Run: PYTHONPATH=src python src/scripts/peer_review/spot_check_vol1.py
"""
import sys
sys.path.insert(0, "src")

from ave.core.constants import (
    ALPHA, HBAR, C_0, M_E, e_charge, L_NODE, A_0, RY_EV,
    XI_TOPO, Z_0, V_SNAP, V_YIELD, E_YIELD, T_EM,
    NU_VAC, P_C, SIN2_THETA_W, N_PHI_PACK, MU_0, EPSILON_0,
    ISOTROPIC_PROJECTION, Z_COORDINATION, G,
)

# ─── Manuscript stated values (from Vol 1 chapters) ────────────────────
CHECKS = [
    # (Name, Engine Value, Manuscript Value, Unit, Tolerance %)
    ("α⁻¹ (Fine-Structure Inverse)",       1.0 / ALPHA,       137.036,      "",       0.001),
    ("ℓ_node (Lattice Pitch)",              L_NODE,             3.8616e-13,  "m",      0.01),
    ("a₀ (Bohr Radius)",                    A_0,                5.2918e-11,  "m",      0.01),
    ("Ry (Rydberg Energy)",                 RY_EV,              13.606,      "eV",     0.01),
    ("ξ_topo (Topological Charge Density)", XI_TOPO,            4.149e-7,    "C/m",    0.1),
    ("Z₀ (Vacuum Impedance)",               Z_0,                376.73,      "Ω",      0.01),
    ("V_snap (Nodal Breakdown)",            V_SNAP,             511000.0,    "V",      0.01),
    ("V_yield (Kinetic Yield)",             V_YIELD,            43652.0,     "V",      0.1),
    ("E_yield (Macroscopic Field Limit)",   E_YIELD,            1.13e17,     "V/m",    1.0),
    ("T_EM (String Tension)",               T_EM,               0.212,       "N",      1.0),
    ("ν_vac (Poisson Ratio)",               NU_VAC,             2.0/7.0,     "",       0.001),
    ("P_C (Packing Fraction 8πα)",          P_C,                0.1834,      "",       0.1),
    ("sin²θ_W (Weak Mixing)",               SIN2_THETA_W,       2.0/9.0,     "",       0.001),
    ("φ_FCC (Close-Pack Fraction)",         N_PHI_PACK,         0.7405,      "",       0.01),
    ("1/7 (Isotropic Projection)",          ISOTROPIC_PROJECTION, 1.0/7.0,   "",       0.001),
]

# ─── Report ─────────────────────────────────────────────────────────────
print("=" * 90)
print("§10 NUMERIC SPOT-CHECK — Volume 1: Foundations")
print("=" * 90)
print()
print(f"{'Constant':<42s} {'Engine':>14s} {'Manuscript':>14s} {'Δ%':>10s} {'Status':>8s}")
print("-" * 90)

all_pass = True
for name, engine_val, manuscript_val, unit, tol_pct in CHECKS:
    if manuscript_val == 0:
        delta_pct = 0.0 if engine_val == 0 else float('inf')
    else:
        delta_pct = abs(engine_val / manuscript_val - 1.0) * 100.0

    status = "✅" if delta_pct <= tol_pct else "❌"
    if status == "❌":
        all_pass = False

    # Format based on magnitude
    if abs(engine_val) > 1e6 or abs(engine_val) < 1e-3:
        e_str = f"{engine_val:.4e}"
        m_str = f"{manuscript_val:.4e}"
    else:
        e_str = f"{engine_val:.6f}"
        m_str = f"{manuscript_val:.6f}"

    print(f"  {name:<40s} {e_str:>14s} {m_str:>14s} {delta_pct:>9.4f}% {status:>6s}")

print("-" * 90)
print(f"\nVERDICT: {'✅ ALL SPOT-CHECKS PASS' if all_pass else '❌ FAILURES DETECTED'}")
print()
