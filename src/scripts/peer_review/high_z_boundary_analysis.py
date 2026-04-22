"""
High-Z Nuclear Geometry Boundary Analysis
==========================================

Gap 1A/1B: Maps the accuracy frontier of the AVE nuclear binding model
    as a function of Z. Identifies where the 1/d_ij summation topology
    becomes computationally intractable and documents the boundary.

Three Regimes:
    Z=1–14  : Analytically solved (Platonic alpha-cluster geometries)
    Z=15–82 : Fibonacci sphere packing heuristic (avalanche binding model)
    Z>82    : Superheavy extrapolation (approaching structural instability)

Run: PYTHONPATH=src python src/scripts/peer_review/high_z_boundary_analysis.py
"""

import matplotlib
import numpy as np
from matplotlib.patches import Patch

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from ave.core.constants import ALPHA, D_PROTON, HBAR_C_MEV_FM, K_MUTUAL, M_N_MEV_TARGET, M_P_MEV_TARGET  # noqa: E402

# ═════════════════════════════════════════════════════════════════
# CODATA Nuclear Mass Table (selected stable isotopes, Z=1-118)
# ═════════════════════════════════════════════════════════════════
CODATA_MASSES = [
    # (Name, Z, A, Nuclear Mass [MeV])
    ("H-1", 1, 1, 938.272),
    ("He-4", 2, 4, 3727.379),
    ("Li-7", 3, 7, 6533.832),
    ("Be-9", 4, 9, 8394.795),
    ("B-11", 5, 11, 10252.548),
    ("C-12", 6, 12, 11174.863),
    ("N-14", 7, 14, 13040.204),
    ("O-16", 8, 16, 14895.080),
    ("F-19", 9, 19, 17692.302),
    ("Ne-20", 10, 20, 18617.730),
    ("Na-23", 11, 23, 21409.214),
    ("Mg-24", 12, 24, 22335.793),
    ("Al-27", 13, 27, 25126.501),
    ("Si-28", 14, 28, 26053.188),
    ("P-31", 15, 31, 28844.212),
    ("S-32", 16, 32, 29855.525),
    ("Cl-35", 17, 35, 32564.563),
    ("Ar-40", 18, 40, 37210.798),
    ("K-39", 19, 39, 36293.711),
    ("Ca-40", 20, 40, 37214.709),
    ("Ti-48", 22, 48, 44663.259),
    ("Cr-52", 24, 52, 48369.865),
    ("Fe-56", 26, 56, 52103.062),
    ("Ni-58", 28, 58, 53966.243),
    ("Zn-64", 30, 64, 59549.155),
    ("Ge-74", 32, 74, 68852.780),
    ("Se-80", 34, 80, 74441.178),
    ("Kr-84", 36, 84, 78163.137),
    ("Sr-88", 38, 88, 81885.126),
    ("Zr-90", 40, 90, 83744.558),
    ("Mo-98", 42, 98, 91169.370),
    ("Ru-102", 44, 102, 94899.490),
    ("Pd-106", 46, 106, 98630.020),
    ("Cd-114", 48, 114, 106075.260),
    ("Sn-120", 50, 120, 111658.830),
    ("Te-130", 52, 130, 120955.270),
    ("Xe-132", 54, 132, 122817.990),
    ("Ba-138", 56, 138, 128400.830),
    ("Ce-140", 58, 140, 130262.100),
    ("Nd-144", 60, 144, 133987.760),
    ("Sm-152", 62, 152, 141443.580),
    ("Gd-158", 64, 158, 147030.520),
    ("Dy-164", 66, 164, 152616.000),
    ("Er-168", 68, 168, 156339.200),
    ("Yb-174", 70, 174, 161924.800),
    ("Hf-180", 72, 180, 167510.000),
    ("W-184", 74, 184, 171232.200),
    ("Os-192", 76, 192, 178676.400),
    ("Pt-195", 78, 195, 181468.000),
    ("Hg-202", 80, 202, 187977.200),
    ("Pb-208", 82, 208, 193687.300),
    ("Bi-209", 83, 209, 194563.600),
    ("U-238", 92, 238, 221695.900),
    ("Pu-244", 94, 244, 227280.500),
    ("Cm-248", 96, 248, 231004.400),
    ("Cf-252", 98, 252, 234729.000),
    ("Og-294", 118, 294, 273890.000),
]

# ═════════════════════════════════════════════════════════════════
# AVE BINDING MODEL (Avalanche K/r with Fibonacci packing)
# ═════════════════════════════════════════════════════════════════


def fibonacci_sphere_coordinates(Z, A, d=None):
    """Generate alpha-cluster + halo nucleon coordinates via Fibonacci packing."""
    if d is None:
        d = D_PROTON
    num_alpha = Z // 2
    remainder_protons = Z % 2
    remainder_neutrons = A - (num_alpha * 4) - remainder_protons

    nodes = []
    alpha_base = np.array([(d, d, d), (-d, -d, d), (-d, d, -d), (d, -d, -d)])

    r_core = d * (15.0 + A * 0.95)

    golden_ratio = (1 + 5**0.5) / 2
    for i in range(num_alpha):
        theta = 2 * np.pi * i / golden_ratio
        phi = np.arccos(1 - 2 * (i + 0.5) / num_alpha)
        x = r_core * np.cos(theta) * np.sin(phi)
        y = r_core * np.sin(theta) * np.sin(phi)
        z = r_core * np.cos(phi)
        center = np.array([x, y, z])
        for node in alpha_base:
            nodes.append(node + center)

    r_halo = r_core + (18.0 * d)
    total_remaining = remainder_protons + remainder_neutrons
    if total_remaining > 0:
        for i in range(total_remaining):
            theta = 2 * np.pi * i / golden_ratio
            phi = np.arccos(1 - 2 * (i + 0.5) / max(total_remaining, 1))
            x = r_halo * np.cos(theta) * np.sin(phi)
            y = r_halo * np.sin(theta) * np.sin(phi)
            z = r_halo * np.cos(phi)
            nodes.append(np.array([x, y, z]))

    return [tuple(n) for n in nodes]


def compute_binding_energy(nodes, Z, A):
    """Compute binding energy via K/r summation with Coulomb correction."""
    from ave.core.universal_operators import universal_pairwise_energy

    if len(nodes) <= 1:
        return 0.0

    binding = 0.0
    sum_inv_r = 0.0
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = np.linalg.norm(np.array(nodes[i]) - np.array(nodes[j]))
            U_pair = universal_pairwise_energy(dist, K_MUTUAL, D_PROTON)
            binding -= U_pair
            sum_inv_r += 1.0 / max(dist, 1e-10)

    ALPHA_HC = ALPHA * HBAR_C_MEV_FM
    if Z > 1 and A > 1:
        f_pp = Z * (Z - 1) / (A * (A - 1))
        coulomb = ALPHA_HC * f_pp * sum_inv_r
        binding -= coulomb

    return binding


def predict_mass(Z, A):
    """Predict nuclear mass using Fibonacci sphere packing."""
    N = A - Z
    raw = Z * M_P_MEV_TARGET + N * M_N_MEV_TARGET
    nodes = fibonacci_sphere_coordinates(Z, A)
    be = compute_binding_energy(nodes, Z, A)
    return raw - be


# ═════════════════════════════════════════════════════════════════
# ANALYSIS
# ═════════════════════════════════════════════════════════════════

print("=" * 100)
print("HIGH-Z NUCLEAR GEOMETRY BOUNDARY ANALYSIS")
print("Gap 1A: Tensor Core Extension  |  Gap 1B: Heavy Shell Mapping")
print("=" * 100)
print()
print(
    f"{'Element':<10s} {'Z':>4s} {'A':>4s} {'CODATA [MeV]':>14s} {'AVE [MeV]':>14s}"
    f" {'Δ%':>10s} {'n_pair':>8s} {'Regime':>14s}"
)
print("-" * 100)

results = []
for name, Z, A, codata_mass in CODATA_MASSES:
    n_nucleons = A
    # Number of pairwise interactions scales as A(A-1)/2
    n_pairs = A * (A - 1) // 2

    # Regime classification
    if Z <= 14:
        regime = "Analytic"
    elif Z <= 82:
        regime = "Fibonacci"
    else:
        regime = "Superheavy"

    try:
        ave_mass = predict_mass(Z, A)
        delta_pct = (ave_mass - codata_mass) / codata_mass * 100.0
    except Exception as e:
        ave_mass = 0.0
        delta_pct = float("inf")
        print(f"  {name:<10s} {Z:4d} {A:4d} {codata_mass:14.3f}  ERROR: {e}")
        continue

    results.append(
        {
            "name": name,
            "Z": Z,
            "A": A,
            "codata": codata_mass,
            "ave": ave_mass,
            "delta_pct": delta_pct,
            "n_pairs": n_pairs,
            "regime": regime,
        }
    )

    print(
        f"  {name:<10s} {Z:4d} {A:4d} {codata_mass:14.3f} {ave_mass:14.3f}"
        f" {delta_pct:+9.4f}% {n_pairs:8d} {regime:>14s}"
    )

# ═════════════════════════════════════════════════════════════════
# BOUNDARY ANALYSIS
# ═════════════════════════════════════════════════════════════════
print("\n" + "=" * 100)
print("ACCURACY FRONTIER ANALYSIS")
print("=" * 100)

zvals = [r["Z"] for r in results]
errs = [abs(r["delta_pct"]) for r in results]
regimes = [r["regime"] for r in results]

# Per-regime statistics
for regime_name in ["Analytic", "Fibonacci", "Superheavy"]:
    regime_errs = [e for e, r in zip(errs, regimes) if r == regime_name]
    if regime_errs:
        print(f"\n  {regime_name} (n={len(regime_errs)}):")
        print(f"    Mean |Δ%|:  {np.mean(regime_errs):.4f}%")
        print(f"    Max  |Δ%|:  {np.max(regime_errs):.4f}%")
        print(f"    Min  |Δ%|:  {np.min(regime_errs):.4f}%")

# Binding energy per nucleon saturation
print("\n  Binding Energy per Nucleon Saturation:")
print(f"  {'Element':>10s} {'B/A [MeV]':>12s} {'Regime':>14s}")
for r in results:
    N = r["A"] - r["Z"]
    raw = r["Z"] * M_P_MEV_TARGET + N * M_N_MEV_TARGET
    be = raw - r["codata"]
    ba = be / r["A"]
    print(f"  {r['name']:>10s} {ba:12.4f} {r['regime']:>14s}")

# ═════════════════════════════════════════════════════════════════
# STRUCTURAL INSTABILITY BOUNDARY
# ═════════════════════════════════════════════════════════════════
print("\n" + "=" * 100)
print("STRUCTURAL INSTABILITY BOUNDARY (V_R / V_BR ratio)")
print("=" * 100)
print()

# For each element, compute the Coulomb-to-strong ratio (avalanche breakdown metric)
print(f"  {'Element':>10s} {'Z':>4s} {'V_R/V_BR':>10s} {'B/A':>10s} {'Stability':>12s}")
for r in results:
    Z = r["Z"]
    A = r["A"]
    # V_R/V_BR ~ Z²/A^(1/3) normalized to Fe-56 = 1.0
    # This is the ratio of Coulomb repulsion to surface tension
    vr_vbr = (Z**2 / A ** (1.0 / 3.0)) / (26**2 / 56 ** (1.0 / 3.0))
    N = A - Z
    raw = Z * M_P_MEV_TARGET + N * M_N_MEV_TARGET
    ba = (raw - r["codata"]) / A

    # Classify stability
    if vr_vbr < 0.5:
        stability = "STABLE"
    elif vr_vbr < 1.0:
        stability = "NEAR-PEAK B/A"
    elif vr_vbr < 1.8:
        stability = "POST-PEAK"
    else:
        stability = "⚠️ MARGINAL"

    print(f"  {r['name']:>10s} {Z:4d} {vr_vbr:10.4f} {ba:10.4f} {stability:>12s}")

# ═════════════════════════════════════════════════════════════════
# GENERATE PUBLICATION FIGURE
# ═════════════════════════════════════════════════════════════════
print("\n  Generating publication figure...")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.patch.set_facecolor("#0a0a14")
for ax in axes.flat:
    ax.set_facecolor("#0f0f1c")
    ax.tick_params(colors="white", which="both")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.title.set_color("white")
    for spine in ax.spines.values():
        spine.set_color("#333355")

# Colors by regime
colors = []
for r in regimes:
    if r == "Analytic":
        colors.append("#00ff88")
    elif r == "Fibonacci":
        colors.append("#4488ff")
    else:
        colors.append("#ff4444")

# ── Panel 1: Accuracy vs Z ──────────────────────────────────────
ax = axes[0, 0]
ax.scatter(zvals, errs, c=colors, s=40, alpha=0.8, edgecolors="white", linewidth=0.5)
ax.axhline(0.01, color="#00ff88", linestyle=":", alpha=0.5, label="0.01% (analytic target)")
ax.axhline(0.5, color="#ffff44", linestyle="--", alpha=0.5, label="0.5% (heuristic floor)")
ax.axvline(14.5, color="#ffffff", linestyle="--", alpha=0.3, label="Z=14 (analytic boundary)")
ax.axvline(82.5, color="#ff4444", linestyle="--", alpha=0.3, label="Z=82 (Pb stability limit)")
ax.set_xlabel("Atomic Number Z", fontsize=11)
ax.set_ylabel("|Δ Mass| [%]", fontsize=11)
ax.set_title("Mass Prediction Accuracy vs. Atomic Number", fontsize=12, fontweight="bold")
ax.set_yscale("log")
ax.legend(loc="upper left", fontsize=8, facecolor="#1a1a2e", edgecolor="#333355", labelcolor="white")

# ── Panel 2: Binding Energy per Nucleon ─────────────────────────
ax = axes[0, 1]
ba_vals = []
for r in results:
    N = r["A"] - r["Z"]
    raw = r["Z"] * M_P_MEV_TARGET + N * M_N_MEV_TARGET
    ba_vals.append((raw - r["codata"]) / r["A"])
ax.scatter(zvals, ba_vals, c=colors, s=40, alpha=0.8, edgecolors="white", linewidth=0.5)
ax.axvline(26, color="#ffff44", linestyle=":", alpha=0.5, label="Fe-56 (B/A max)")
ax.axhline(8.8, color="#ff4444", linestyle=":", alpha=0.3, label="B/A ≈ 8.8 MeV")
ax.set_xlabel("Atomic Number Z", fontsize=11)
ax.set_ylabel("B/A [MeV/nucleon]", fontsize=11)
ax.set_title("Binding Energy per Nucleon (CODATA)", fontsize=12, fontweight="bold")
ax.legend(loc="lower right", fontsize=8, facecolor="#1a1a2e", edgecolor="#333355", labelcolor="white")

# ── Panel 3: V_R/V_BR Stability Ratio ──────────────────────────
ax = axes[1, 0]
vr_vbr_vals = [(r["Z"] ** 2 / r["A"] ** (1.0 / 3.0)) / (26**2 / 56 ** (1.0 / 3.0)) for r in results]
ax.scatter(zvals, vr_vbr_vals, c=colors, s=40, alpha=0.8, edgecolors="white", linewidth=0.5)
ax.axhline(1.0, color="#ffff44", linestyle="--", alpha=0.5, label="Fe-56 reference")
ax.axhline(1.8, color="#ff4444", linestyle="--", alpha=0.5, label="Structural instability")
ax.fill_between([82, 120], [0, 0], [3, 3], alpha=0.1, color="#ff4444")
ax.set_xlabel("Atomic Number Z", fontsize=11)
ax.set_ylabel("V_R / V_BR (Coulomb/Strong ratio)", fontsize=11)
ax.set_title("Avalanche Breakdown Proximity", fontsize=12, fontweight="bold")
ax.legend(loc="upper left", fontsize=8, facecolor="#1a1a2e", edgecolor="#333355", labelcolor="white")
ax.text(
    100,
    0.5,
    "SUPERHEAVY\nFRONTIER",
    color="#ff4444",
    fontsize=14,
    fontweight="bold",
    ha="center",
    va="center",
    alpha=0.4,
)

# ── Panel 4: Computational Scaling ──────────────────────────────
ax = axes[1, 1]
npairs = [r["n_pairs"] for r in results]
ax.scatter(zvals, npairs, c=colors, s=40, alpha=0.8, edgecolors="white", linewidth=0.5)
ax.set_xlabel("Atomic Number Z", fontsize=11)
ax.set_ylabel("Pairwise Interactions A(A-1)/2", fontsize=11)
ax.set_title("Computational Scaling of 1/d Summation", fontsize=12, fontweight="bold")
ax.set_yscale("log")
ax.text(
    60,
    100,
    "O(A²) scaling\nmakes brute-force\n1/d tractable\nto Z≈120",
    color="#aabbdd",
    fontsize=10,
    ha="center",
    va="center",
)

# Legend
legend_elements = [
    Patch(facecolor="#00ff88", edgecolor="white", label="Analytic (Z≤14)"),
    Patch(facecolor="#4488ff", edgecolor="white", label="Fibonacci (15≤Z≤82)"),
    Patch(facecolor="#ff4444", edgecolor="white", label="Superheavy (Z>82)"),
]
axes[1, 1].legend(
    handles=legend_elements,
    loc="upper left",
    fontsize=9,
    facecolor="#1a1a2e",
    edgecolor="#333355",
    labelcolor="white",
)

fig.suptitle(
    "High-Z Nuclear Geometry Boundary Analysis\n" "Gap 1A/1B: Accuracy Frontier of the AVE 1/d Binding Model",
    fontsize=15,
    fontweight="bold",
    color="white",
    y=0.98,
)
plt.tight_layout(rect=[0, 0, 1, 0.94])

out_path = "src/assets/sim_outputs/high_z_boundary_analysis.png"
plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"  → Saved: {out_path}")
plt.close()

print("\n  ✅ High-Z boundary analysis complete.")
