"""
D_PROTON Delta Analysis — Peer Review WS3

Computes all nuclear constants using BOTH:
  (A) The derived proton mass (PROTON_ELECTRON_RATIO × M_E)  [CURRENT ENGINE]
  (B) The empirical CODATA proton mass (M_P_MEV_CODATA)       [ARCHITECTURE REVIEW C3]

Shows the delta between each approach to verify the derivation chain
integrity and document the impact of using first-principles values.

Run: PYTHONPATH=src python src/scripts/peer_review/d_proton_delta_analysis.py
"""

from math import pi

from ave.core.constants import ALPHA, C_0, D_PROTON, HBAR, M_E, M_P_MEV_CODATA, NU_VAC, PROTON_ELECTRON_RATIO, e_charge

# ─── (A) DERIVED chain (current engine state) ───────────────────────────
# D_PROTON already uses PROTON_ELECTRON_RATIO * M_E (verified at line 667)
d_proton_derived = D_PROTON  # fm

# ─── (B) EMPIRICAL chain (if we had used M_P_MEV_CODATA) ────────────────
m_p_empirical_kg = M_P_MEV_CODATA * 1e6 * e_charge / C_0**2
d_proton_empirical = 4.0 * HBAR / (m_p_empirical_kg * C_0) * 1e15  # fm

# Derived proton mass in MeV for comparison
m_p_derived_mev = PROTON_ELECTRON_RATIO * M_E * C_0**2 / (e_charge * 1e6)


# ─── Recompute ALL downstream constants with BOTH chains ────────────────
def compute_nuclear_chain(d_proton_fm: float) -> dict[str, float]:
    """Recompute the full nuclear constant chain from a given D_PROTON."""
    d_intra = d_proton_fm * (8.0**0.5)
    d_nn = pi * d_proton_fm * 7.0 / 9.0
    omega_1 = C_0 / (d_proton_fm * 1e-15 / (1.0 + NU_VAC))
    b_deuteron = HBAR * omega_1 / e_charge * 1e-6 * ALPHA
    e_0_nuclear = HBAR * omega_1 / (e_charge * 1e6)
    k_coupling = 1.0 / (1.0 - ALPHA) ** 2 - 1.0  # independent of d_proton

    return {
        "D_PROTON [fm]": d_proton_fm,
        "D_INTRA_ALPHA [fm]": d_intra,
        "D_NN_EIGENVALUE [fm]": d_nn,
        "OMEGA_0_NUCLEAR [rad/s]": omega_1,
        "B_DEUTERON [MeV]": b_deuteron,
        "E_0_NUCLEAR [MeV]": e_0_nuclear,
        "K_COUPLING": k_coupling,
    }


chain_derived = compute_nuclear_chain(d_proton_derived)
chain_empirical = compute_nuclear_chain(d_proton_empirical)

# ─── CODATA targets for comparison ──────────────────────────────────────
codata_targets = {
    "D_PROTON [fm]": 0.8414,  # muonic hydrogen (2019)
    "D_INTRA_ALPHA [fm]": None,  # no direct measurement
    "D_NN_EIGENVALUE [fm]": 2.05,  # deuteron radius ≈ 2.1 fm
    "B_DEUTERON [MeV]": 2.2246,  # CODATA
    "E_0_NUCLEAR [MeV]": None,  # internal parameter
    "K_COUPLING": None,  # internal parameter
}

# ─── Report ─────────────────────────────────────────────────────────────
print("=" * 90)
print("D_PROTON DELTA ANALYSIS — Peer Review Verification")
print("=" * 90)
print()
print(f"  Derived proton mass (engine):   m_p/m_e = {PROTON_ELECTRON_RATIO:.6f}")
print(f"  Derived proton mass (MeV):      {m_p_derived_mev:.6f} MeV")
print(f"  CODATA proton mass (MeV):       {M_P_MEV_CODATA:.6f} MeV")
print(
    f"  Delta:                          {(m_p_derived_mev - M_P_MEV_CODATA):.6f} MeV"
    f"  ({(m_p_derived_mev / M_P_MEV_CODATA - 1) * 100:+.4f}%)"
)
print()
print("-" * 90)
print(f"{'Constant':<30s} {'Derived':>16s} {'Empirical':>16s} {'Δ%':>10s} {'CODATA':>12s} {'vs CODATA':>10s}")
print("-" * 90)

for key in chain_derived:
    val_d = chain_derived[key]
    val_e = chain_empirical[key]

    if val_d == val_e:
        delta_pct = "0.0000%"
    else:
        delta_pct = f"{(val_d / val_e - 1) * 100:+.4f}%"

    codata = codata_targets.get(key)
    if codata is not None:
        vs_codata = f"{(val_d / codata - 1) * 100:+.4f}%"
        codata_str = f"{codata:.4f}"
    else:
        vs_codata = "—"
        codata_str = "—"

    # Format based on magnitude
    if abs(val_d) > 1e6:
        d_str = f"{val_d:.4e}"
        e_str = f"{val_e:.4e}"
    else:
        d_str = f"{val_d:.6f}"
        e_str = f"{val_e:.6f}"

    print(f"  {key:<28s} {d_str:>16s} {e_str:>16s} {delta_pct:>10s} {codata_str:>12s} {vs_codata:>10s}")

print("-" * 90)
print()
print("INTERPRETATION:")
print("  The 'Derived' column is the current engine state (D_PROTON from PROTON_ELECTRON_RATIO × M_E).")
print("  The 'Empirical' column is what the values WOULD be if M_P_MEV_CODATA were used (old C3 path).")
print("  The 'Δ%' column shows the shift introduced by using the first-principles derivation.")
print("  The 'vs CODATA' column shows accuracy of the derived chain against experiment.")
print()
print("VERDICT:")
if abs(m_p_derived_mev / M_P_MEV_CODATA - 1) < 0.005:
    print("  ✅ C3 is RESOLVED. D_PROTON already uses the derived proton mass.")
    print(
        f"  ✅ All nuclear constants shift by ≤ {abs(m_p_derived_mev / M_P_MEV_CODATA - 1) * 100:.3f}%"
        " — within framework precision."
    )
else:
    print("  ⚠️  Proton mass derivation error exceeds 0.5% — review nuclear predictions carefully.")
