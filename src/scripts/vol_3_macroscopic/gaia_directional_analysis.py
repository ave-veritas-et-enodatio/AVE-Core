"""
Gaia DR3 Directional Analysis — CMB-rest vs galactic-rest preferred-frame test.

SCOPE NOTE (2026-05-17 evening — directional analysis of substrate-equilibrium
velocity prediction):

Tests the 3D directional structure of the Gaia DR3 nearby thin-disk G/K dwarf
velocity distribution to discriminate between two interpretations of the
αc/(2π) ≈ 348 km/s substrate-equilibrium velocity prediction:

  - **Interpretation B-CMB (substrate equilibrium in CMB-rest)**: cluster
    aligned with CMB-dipole direction (l,b) = (264°, 48°); σ∥ << σ⊥ along
    this axis. This is the AVE-distinct positive prediction.
  - **Interpretation X-galactic (galactic dynamics dominates)**: cluster
    aligned with galactic-rotation direction (l,b) ≈ (90°, 0°) toward Cygnus;
    σ∥ << σ⊥ along this axis. Would falsify substrate-equilibrium claim.
  - **Interpretation isotropic**: no preferred axis. Falsifies BOTH (the σ=11
    cluster tightness already argued against pure random kinematics, but
    isotropic-with-coherent-magnitude would be a new puzzle).
  - **Interpretation cubic-aligned**: cluster preferentially aligned with
    cubic axes. Per framework's own (qℓ_node)⁴ suppression (~10⁻⁹⁶ at
    stellar wavelengths), this is predicted NULL — flagged as sanity-check
    expectation, NOT a positive test.

INPUTS (empirical, honestly labeled):
  - /tmp/gaia_nearby_gk.csv (29,466 stars, Gaia DR3 query 2026-05-17)
  - Sun's CMB velocity: 370 km/s toward (l,b) = (264°, 48°) (Planck 2018) —
    EMPIRICAL INPUT, not derived
  - IAU J2000 equatorial-to-galactic rotation matrix (standard)
  - Schönrich+ 2010 Sun-wrt-LSR velocity: (U,V,W) = (11.1, 12.24, 7.25) km/s

DERIVED (canonical, no fit):
  - αc/(2π) = 348.18 km/s substrate-equilibrium FLOOR (zero-parameter)
  - Per-star CMB-frame velocity vector (forward computation)
  - Cluster mean velocity vector + direction (statistical)
  - Anisotropy tensor (covariance of cluster) + eigendirections + eigenvalues
  - Angular distance between cluster mean direction and (CMB-dipole, galactic-rotation, cubic axes)

WHAT THIS SCRIPT DOES NOT DO:
  - No fit parameters. AVE prediction is forward.
  - No cubic-anisotropy positive test (framework predicts ~zero per (qℓ_node)⁴)
  - No retrofitting of cluster center to αc/(2π) — that would require
    additional physics not yet derived

OUTCOMES (pre-registered):
  - **A-CMB**: Cluster mean direction within ~10° of CMB-dipole direction
    + σ∥ ≤ σ⊥/2 → STRONG positive for substrate-equilibrium in CMB-rest
  - **B-MW**: Cluster mean direction within ~30° of galactic-rotation
    direction → SUBSTRATE-EQUILIBRIUM FALSIFIED; cluster reflects MW disk
    dynamics, αc/(2π) magnitude match is coincidence
  - **C-isotropic**: No preferred axis, but cluster tightness preserved →
    NEW PUZZLE (not falsification, but not validation either)
  - **D-cubic**: Aligned with cubic axes → either framework breaks own
    suppression (very unlikely) or detector/selection systematics
"""

import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from ave.core.constants import ALPHA, C_0


# AVE prediction
V_SUBSTRATE_MS = ALPHA * C_0 / (2 * np.pi)
V_SUBSTRATE_KMS = V_SUBSTRATE_MS / 1000.0


# Reference directions in galactic Cartesian (x → GC, y → galactic rotation, z → NGP)
def _galactic_unit_vector(l_deg: float, b_deg: float) -> np.ndarray:
    l, b = np.radians(l_deg), np.radians(b_deg)
    return np.array([np.cos(b) * np.cos(l), np.cos(b) * np.sin(l), np.sin(b)])


# Sun's CMB velocity (Planck 2018): magnitude 370 km/s toward (l,b) = (264°, 48°)
SUN_CMB_MAG_KMS = 370.0
SUN_CMB_DIR_GAL = _galactic_unit_vector(264.0, 48.0)
SUN_CMB_VEC_GAL = SUN_CMB_MAG_KMS * SUN_CMB_DIR_GAL

# Sun's LSR motion (Schönrich+ 2010): (U,V,W) = (11.1, 12.24, 7.25) km/s
SUN_LSR_UVW = np.array([11.1, 12.24, 7.25])

# CMB-dipole unit direction
CMB_DIPOLE_DIR = SUN_CMB_DIR_GAL.copy()

# Galactic-rotation direction (toward Cygnus): (l,b) = (90°, 0°)
GAL_ROTATION_DIR = _galactic_unit_vector(90.0, 0.0)

# Cubic-axes test set (Cartesian galactic axes)
CUBIC_AXES = [
    np.array([1.0, 0.0, 0.0]),  # +x (galactic center)
    np.array([0.0, 1.0, 0.0]),  # +y (rotation)
    np.array([0.0, 0.0, 1.0]),  # +z (NGP)
]


# IAU J2000 equatorial-to-galactic rotation matrix
R_EQ_TO_GAL = np.array([
    [-0.054876, -0.873437, -0.483835],
    [+0.494109, -0.444830, +0.746982],
    [-0.867666, -0.198076, +0.455984],
])


def parse_gaia_csv(path: Path) -> list[dict]:
    stars = []
    with path.open("r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                stars.append({k: float(row[k]) for k in [
                    "ra", "dec", "parallax", "pmra", "pmdec",
                    "radial_velocity",
                ]})
            except (ValueError, KeyError):
                continue
    return stars


def heliocentric_velocity_galactic(star: dict) -> np.ndarray:
    """Heliocentric velocity vector in galactic Cartesian (km/s)."""
    ra = np.radians(star["ra"])
    dec = np.radians(star["dec"])
    d_pc = 1000.0 / star["parallax"]
    v_alpha = 4.740470463e-3 * star["pmra"] * d_pc
    v_delta = 4.740470463e-3 * star["pmdec"] * d_pc
    v_r = star["radial_velocity"]

    cra, sra, cde, sde = np.cos(ra), np.sin(ra), np.cos(dec), np.sin(dec)
    v_eq = np.array([
        v_r * cde * cra - v_alpha * sra - v_delta * sde * cra,
        v_r * cde * sra + v_alpha * cra - v_delta * sde * sra,
        v_r * sde + v_delta * cde,
    ])
    return R_EQ_TO_GAL @ v_eq


def angle_between(v1: np.ndarray, v2: np.ndarray) -> float:
    """Angle between two vectors in degrees."""
    n1 = v1 / np.linalg.norm(v1)
    n2 = v2 / np.linalg.norm(v2)
    cos_theta = np.clip(np.dot(n1, n2), -1.0, 1.0)
    return float(np.degrees(np.arccos(cos_theta)))


def main() -> None:
    print("=" * 70)
    print("  GAIA DR3 DIRECTIONAL ANALYSIS")
    print("  CMB-rest vs galactic-rest preferred-frame test")
    print("=" * 70)
    print()
    print(f"AVE prediction: v_substrate FLOOR = αc/(2π) = {V_SUBSTRATE_KMS:.2f} km/s")
    print()
    print("Reference directions (galactic Cartesian unit vectors):")
    print(f"  CMB-dipole direction (l,b=264°,48°):     {CMB_DIPOLE_DIR}")
    print(f"  Galactic rotation direction (l,b=90°,0°): {GAL_ROTATION_DIR}")
    print(f"  Angle between CMB-dipole and rotation: {angle_between(CMB_DIPOLE_DIR, GAL_ROTATION_DIR):.1f}°")
    print()

    # Load Gaia data
    csv_path = Path("/tmp/gaia_nearby_gk.csv")
    if not csv_path.exists():
        print(f"ERROR: {csv_path} not found.")
        return
    stars = parse_gaia_csv(csv_path)
    print(f"Loaded {len(stars)} stars from {csv_path}")

    # Compute CMB-frame velocity vectors
    v_cmb_vecs = []
    v_lsr_mags = []  # for thin-disk subset selection
    for s in stars:
        v_helio_gal = heliocentric_velocity_galactic(s)
        v_cmb = v_helio_gal + SUN_CMB_VEC_GAL
        v_cmb_vecs.append(v_cmb)
        v_lsr_mags.append(np.linalg.norm(v_helio_gal + SUN_LSR_UVW))
    v_cmb_vecs = np.array(v_cmb_vecs)
    v_lsr_mags = np.array(v_lsr_mags)
    v_cmb_mags = np.linalg.norm(v_cmb_vecs, axis=1)

    # Cut to thin-disk subset (|v_LSR| < 30 km/s)
    thin_disk_mask = v_lsr_mags < 30.0
    v_thin = v_cmb_vecs[thin_disk_mask]
    print(f"Thin-disk subset (|v_LSR|<30): {len(v_thin)} stars")
    print()

    # Cluster mean direction + magnitude
    v_mean = np.mean(v_thin, axis=0)
    v_mean_mag = np.linalg.norm(v_mean)
    v_mean_dir = v_mean / v_mean_mag
    print(f"Cluster mean velocity vector: ({v_mean[0]:.1f}, {v_mean[1]:.1f}, {v_mean[2]:.1f}) km/s")
    print(f"Cluster mean magnitude: {v_mean_mag:.2f} km/s")
    print(f"Cluster mean direction: {v_mean_dir}")
    print()

    # Compare cluster mean direction vs reference directions
    print("Angular alignment of cluster mean direction with reference axes:")
    angle_cmb = angle_between(v_mean_dir, CMB_DIPOLE_DIR)
    angle_gal = angle_between(v_mean_dir, GAL_ROTATION_DIR)
    print(f"  vs CMB-dipole direction:   {angle_cmb:>6.2f}°")
    print(f"  vs galactic-rotation dir:  {angle_gal:>6.2f}°")
    for i, axis in enumerate(CUBIC_AXES):
        ax_name = ["+x (GC)", "+y (rot)", "+z (NGP)"][i]
        print(f"  vs cubic axis {ax_name}:    {angle_between(v_mean_dir, axis):>6.2f}°")
    print()

    # Anisotropy tensor (covariance of CMB-frame velocities about the cluster mean)
    v_centered = v_thin - v_mean
    cov = np.cov(v_centered.T)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)  # ascending
    # Sort descending
    order = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[order]
    eigenvectors = eigenvectors[:, order]

    print("Anisotropy tensor eigenvalues (km²/s², descending):")
    for i, ev in enumerate(eigenvalues):
        print(f"  λ_{i} = {ev:.2f}  (σ = {np.sqrt(ev):.2f} km/s)")
    print()
    print("Eigenvectors (in galactic Cartesian):")
    for i in range(3):
        print(f"  v_{i} = {eigenvectors[:, i]}")
        print(f"    angle to CMB-dipole:     {angle_between(eigenvectors[:, i], CMB_DIPOLE_DIR):>6.2f}°")
        print(f"    angle to galactic rot:   {angle_between(eigenvectors[:, i], GAL_ROTATION_DIR):>6.2f}°")
    print()

    # Decompose cluster spread along CMB-dipole vs perpendicular
    print("Cluster spread along reference axes (1D σ from variance projection):")
    for ref_name, ref_dir in [
        ("CMB-dipole", CMB_DIPOLE_DIR),
        ("galactic-rot", GAL_ROTATION_DIR),
    ]:
        # Variance along ref_dir
        v_proj_parallel = v_centered @ ref_dir
        sigma_parallel = float(np.std(v_proj_parallel))

        # Variance perpendicular (project onto plane perpendicular to ref_dir)
        v_perp = v_centered - np.outer(v_centered @ ref_dir, ref_dir)
        sigma_perp = float(np.linalg.norm(np.std(v_perp, axis=0)))

        ratio = sigma_perp / sigma_parallel if sigma_parallel > 0 else np.inf
        print(f"  {ref_name:<14s}: σ∥ = {sigma_parallel:>6.2f}, σ⊥ = {sigma_perp:>6.2f}, σ⊥/σ∥ = {ratio:>5.2f}")
    print()

    # Outcome categorization
    print("=" * 70)
    print("OUTCOME CATEGORIZATION")
    print("=" * 70)
    if angle_cmb < 10.0:
        outcome = "A-CMB — STRONG POSITIVE: cluster aligned within 10° of CMB-dipole"
    elif angle_cmb < 30.0:
        outcome = "A-CMB-broad — qualitative positive: aligned within 30° of CMB-dipole"
    elif angle_gal < 30.0:
        outcome = "B-MW — SUBSTRATE-EQUILIBRIUM FALSIFIED: aligned with galactic rotation"
    else:
        outcome = "C-other — cluster aligned with neither preferred axis (puzzle)"
    print(f"  {outcome}")
    print()
    print(f"Cluster mean direction in galactic (l, b): ({np.degrees(np.arctan2(v_mean_dir[1], v_mean_dir[0])) % 360:.1f}°, {np.degrees(np.arcsin(v_mean_dir[2])):.1f}°)")
    print(f"CMB-dipole direction in galactic (l, b):   (264.0°, 48.0°)")
    print()

    # Plot: cluster scatter projected onto CMB-dipole-aligned plane
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Plot 1: histogram of angles between each star's v_CMB direction and CMB-dipole direction
    v_thin_dirs = v_thin / np.linalg.norm(v_thin, axis=1, keepdims=True)
    angles_to_cmb = np.array([angle_between(d, CMB_DIPOLE_DIR) for d in v_thin_dirs])
    angles_to_gal = np.array([angle_between(d, GAL_ROTATION_DIR) for d in v_thin_dirs])
    axes[0].hist(angles_to_cmb, bins=60, range=(0, 180), alpha=0.6, color="red",
                 label=f"vs CMB-dipole (mean: {np.mean(angles_to_cmb):.1f}°)")
    axes[0].hist(angles_to_gal, bins=60, range=(0, 180), alpha=0.6, color="blue",
                 label=f"vs galactic-rotation (mean: {np.mean(angles_to_gal):.1f}°)")
    axes[0].axvline(angle_cmb, color="red", linestyle="--",
                    label=f"Cluster mean vs CMB-dipole: {angle_cmb:.1f}°")
    axes[0].axvline(angle_gal, color="blue", linestyle="--",
                    label=f"Cluster mean vs galactic-rot: {angle_gal:.1f}°")
    axes[0].set_xlabel("Angle from reference axis (degrees)", fontsize=11)
    axes[0].set_ylabel("# thin-disk stars", fontsize=11)
    axes[0].set_title(f"Per-star velocity direction distribution (N={len(v_thin)})")
    axes[0].legend(fontsize=9)
    axes[0].grid(alpha=0.3)

    # Plot 2: projection onto plane containing CMB-dipole direction
    # Define basis: e1 = CMB_DIPOLE_DIR, e2 = (any perpendicular), e3 = e1 × e2
    e1 = CMB_DIPOLE_DIR
    # pick perpendicular to e1 in the GR plane (galactic rotation direction component perpendicular to CMB-dipole)
    e2 = GAL_ROTATION_DIR - np.dot(GAL_ROTATION_DIR, e1) * e1
    e2 /= np.linalg.norm(e2)
    e3 = np.cross(e1, e2)

    v_e1 = v_thin @ e1
    v_e2 = v_thin @ e2
    axes[1].scatter(v_e1, v_e2, s=1, alpha=0.3, color="steelblue")
    axes[1].axvline(V_SUBSTRATE_KMS, color="red", linestyle="--", linewidth=2,
                    label=f"αc/(2π) FLOOR projected on CMB-dipole: {V_SUBSTRATE_KMS:.1f} km/s")
    axes[1].axvline(np.mean(v_e1), color="orange", linestyle="-", linewidth=2,
                    label=f"Cluster mean ∥ CMB-dipole: {np.mean(v_e1):.1f} km/s")
    axes[1].axhline(0.0, color="gray", linestyle=":", alpha=0.5)
    axes[1].set_xlabel("v ∥ CMB-dipole direction (km/s)", fontsize=11)
    axes[1].set_ylabel("v perpendicular (in galactic-rotation projection) (km/s)", fontsize=11)
    axes[1].set_title(f"Velocity projection onto CMB-dipole plane")
    axes[1].legend(fontsize=9, loc="lower right")
    axes[1].grid(alpha=0.3)
    axes[1].set_aspect("equal")

    plt.tight_layout()
    out_path = Path(__file__).parent.parent.parent / "assets" / "sim_outputs" / "gaia_directional_analysis.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved directional analysis plot to {out_path}")


if __name__ == "__main__":
    main()
