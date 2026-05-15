"""
§10 Numeric Spot-Check — Volume 2: Subatomic Structure
========================================================

Independently verifies flagship constants from the physics engine
against manuscript-stated values in Volume 2.

Run: PYTHONPATH=src python src/scripts/peer_review/spot_check_vol2.py
"""

from ave.core.constants import (
    A_0,
    ALPHA_S,
    BARYON_LADDER,
    C_0,
    CROSSING_NUMBER_PROTON,
    D_PROTON,
    M_E,
    M_HIGGS_MEV,
    M_W_MEV,
    M_Z_MEV,
    PROTON_ELECTRON_RATIO,
    SIN2_THETA_W,
    e_charge,
)

# Derived proton mass from engine
m_p_derived_mev = PROTON_ELECTRON_RATIO * M_E * C_0**2 / (e_charge * 1e6)

# Baryon ladder entries
proton_entry = BARYON_LADDER.get(5, {})

CHECKS = [
    # (Name, Engine Value, Manuscript/CODATA Value, Unit, Tolerance %)
    ("m_p/m_e (Proton-Electron Ratio)", PROTON_ELECTRON_RATIO, 1836.153, "", 0.01),
    ("m_p (Proton Mass)", m_p_derived_mev, 938.272, "MeV", 0.01),
    ("sin²θ_W (Weak Mixing, On-Shell)", SIN2_THETA_W, 0.2222, "", 0.1),
    ("α_s (Strong Coupling)", ALPHA_S, 0.1214, "", 0.1),
    ("a₀ (Bohr Radius = ℓ/α)", A_0, 5.2918e-11, "m", 0.01),
    ("M_W (W Boson Mass)", M_W_MEV, 80377.0, "MeV", 1.0),
    ("M_Z (Z Boson Mass)", M_Z_MEV, 91188.0, "MeV", 3.0),
    ("M_H (Higgs Mass)", M_HIGGS_MEV, 125100.0, "MeV", 2.0),
    ("D_PROTON (Charge Radius)", D_PROTON, 0.8414, "fm", 0.1),
    ("Proton Crossing Number", CROSSING_NUMBER_PROTON, 5, "", 0.001),
]

print("=" * 90)
print("§10 NUMERIC SPOT-CHECK — Volume 2: Subatomic Structure")
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

    if abs(engine_val) > 1e6 or abs(engine_val) < 1e-3:
        e_str = f"{engine_val:.4e}"
        m_str = f"{target_val:.4e}"
    else:
        e_str = f"{engine_val:.6f}"
        m_str = f"{target_val:.6f}"

    print(f"  {name:<40s} {e_str:>14s} {m_str:>14s} {delta_pct:>9.4f}% {status:>6s}")

print("-" * 90)

# Baryon ladder summary
print("\n  Baryon Resonance Ladder (Torus Knot Spectrum):")
print(f"  {'c':<6s} {'Derived MeV':>14s} {'PDG MeV':>12s} {'Δ%':>8s}")
pdg_targets = {5: 938.272, 7: 1232.0, 9: 1600.0, 11: 1900.0, 13: 2190.0}
for c, entry in sorted(BARYON_LADDER.items()):
    pdg = pdg_targets.get(c, None)
    mass = entry["mass_mev"]
    if pdg:
        delta = abs(mass / pdg - 1.0) * 100.0
        print(f"  {c:<6d} {mass:>14.1f} {pdg:>12.1f} {delta:>7.2f}%")
    else:
        print(f"  {c:<6d} {mass:>14.1f} {'—':>12s} {'—':>8s}")

print(f"\nVERDICT: {'✅ ALL SPOT-CHECKS PASS' if all_pass else '❌ FAILURES DETECTED'}")
print()
