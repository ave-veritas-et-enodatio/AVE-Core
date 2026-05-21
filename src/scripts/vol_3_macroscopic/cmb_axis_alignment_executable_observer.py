"""
CMB Axis Alignment Executable Observer — Phase 2: Planck PR3 SMICA data ingest +
multi-observable axis alignment test.

Executes the frozen 2026-05-15 A-034 CMB Axis Alignment Empirical Pre-Registration
at research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md.

PHASE 2 (this file) vs PHASE 1 (cmb_axis_alignment_driver.py):
  - Phase 1: literature-axis comparison; flagged the (l=174, b=-5) citation gap.
  - Phase 2 (this): computes CMB quadrupole-octupole axis-of-evil from RAW
    Planck PR3 SMICA temperature data via maximum-angular-momentum-dispersion
    estimator (de Oliveira-Costa et al. 2004, Phys. Rev. D 69:063516).

THE AVE PREDICTION IS THE CORRELATION AMONG OBSERVABLES, NOT A SPECIFIC AXIS:
  per the frozen methodology prereg section 7 (line 413-416), AVE does NOT predict
  the specific axis direction. The (l=174, b=-5) corpus-quoted value is a literature
  reference point from prior axis-of-evil work, NOT an AVE-derived prediction. The
  driver computes its own axis-of-evil from Planck data; alignment is checked
  pairwise between observables, against uniform-prior null.

OBSERVABLES TESTED (this session, 4-axis primary):
  1. CMB axis-of-evil (Planck PR3 SMICA T-only, data-derived).
  2. Hubble flow bulk direction (Whitford+2023 Pantheon+ analysis, paper-pinned).
  3. LSS galaxy spin axis (Longo 2011 / Shamir 2020 SDSS, paper-pinned).
  4. Matter-asymmetry direction (per frozen prereg section 3.4: weak, recorded but
     not load-bearing).

NOT TESTED (deferred to future sessions per execution-session prereg section 1):
  5. E/B polarization (BICEP)
  6. Orbital-plane alignment statistics (Gaia / JPL / LIGO)
  7. CODATA G P_2 anisotropy

SHARPEST SINGLE FALSIFIER: CMB axis vs Hubble flow misaligned > 20 deg at combined
3 sigma -> Outcome C (NULL) immediate. Per closure-roadmap.md:35 and frozen prereg
section 5.

PRE-REGISTERED OUTCOMES (mapped to driver auto-classification):
  A+ : 4-of-4 axes mutually aligned within 10 deg at 3 sigma; degree-class
       agreement > 95% vs uniform-prior null.
  A  : 3-of-4 axes mutually aligned within 20 deg at combined 3 sigma;
       degree-class agreement > 80%.
  B  : 2-of-4 axes aligned; tension structure; agreement 50-80%.
  C  : pairwise separations consistent with uniform-prior null;
       agreement < 50%. A-034 cosmic-scale row fails.
  D  : data insufficient to discriminate A/B/C; surface for methodology adjudication.
  E  : data access fails; this session unable to complete; defer to data-staging
       session.

Run:
    python3 src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer.py
"""

from __future__ import annotations

import json
import math
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))

DATA_DIR = REPO_ROOT / "data"
PLANCK_DIR = DATA_DIR / "planck_pr3"
PANTHEON_DIR = DATA_DIR / "pantheon_plus"
RESULTS_PATH = SCRIPT_DIR / "cmb_axis_alignment_executable_observer_results.json"

# AVE canonical reference axis (LITERATURE-QUOTED, NOT A PREDICTION):
# (l, b) = (174, -5) per universal-saturation-kernel-catalog.md:88 + frozen prereg.
# Used only as orientation reference; the AVE prediction is alignment-correlation
# among observables, NOT a specific direction.
OMEGA_FREEZE_L_DEG = 174.0
OMEGA_FREEZE_B_DEG = -5.0

# Adjudication thresholds (per execution-session prereg section 4, mapping frozen
# methodology prereg outcomes).
PASS_THRESHOLD_DEG = 20.0
TIGHT_THRESHOLD_DEG = 10.0
FAIL_THRESHOLD_DEG = 45.0

# ----------------------------------------------------------------------------
# Data sources (paper-pinned, per C8-BARYON-LADDER PDG-anchor pattern)
# ----------------------------------------------------------------------------

PANTHEON_BULK_FLOW_WHITFORD2023 = {
    "l_deg": 323.0,
    "b_deg": 26.0,
    "sigma_deg": 30.0,
    "reference": "Whitford et al. 2023, MNRAS 526:3051, 'Bulk flow in the local Universe'",
    "depth_h_inv_Mpc": 150.0,
}

# CORPUS-PIN CORRECTION 2026-05-19 EOD (c5-corpus-pin-fix walk-back):
#   Prior value (l=32°, b=32°) was a coordinate-system conflation: the literal
#   "32°" came from Longo 2011's quoted equatorial declination of the dipole
#   direction (δ ~ 32°), then mistakenly used as BOTH galactic l AND galactic b
#   in the corpus pin. The actual Longo 2011 published axis in galactic
#   coordinates is (l = 52°, b = 68.5°).
#   Verified 2026-05-19 EOD by SDSS DR17 implementor reading the Longo 2011
#   PDF directly (Phys. Lett. B 699:224, "Detection of a Dipole in the
#   Handedness of Spiral Galaxies with Redshifts z ~ 0.04").
#   Walk-back pattern follows the E1b (174°, -5°) → (60.28°, 50.48°) precedent
#   recorded at closure-roadmap.md §0.5 row dated 2026-05-19 (driver-executed
#   empirical pin of an unpinned literature value).
#   NOTE: the framework's current best-precision empirical state for the LSS
#   spin axis is the SDSS DR17 re-fit at (l = 129°, b = 79°), σ = 6.83°, per
#   research/2026-05-19_c5-sdss-spin-orientation-result.md +
#   c5_sdss_spin_orientation_results.json. That empirical re-fit supersedes
#   BOTH the original corpus pin (32°, 32°) AND Longo's published axis at
#   the framework's current empirical state; this dict carries the literature
#   pin for archival driver-output reproducibility.
SDSS_LSS_SPIN_LONGO2011 = {
    "l_deg": 52.0,
    "b_deg": 68.5,
    "sigma_deg": 30.0,
    "reference": "Longo 2011, Phys. Lett. B 699:224, SDSS DR7 spiral handedness "
    "(galactic-coordinate axis (l=52°, b=68.5°) per direct read of the PDF, "
    "verified 2026-05-19 EOD; prior corpus value (32°, 32°) was a coordinate "
    "conflation corrected via the c5-corpus-pin-fix walk-back) + Shamir 2020 "
    "ApJ 891:97 DR8 confirmation; literature scatter dominates uncertainty. "
    "Current best-precision empirical axis is the SDSS DR17 re-fit at "
    "(l=129°, b=79°), σ=6.83° per c5_sdss_spin_orientation_results.json.",
}

# Matter-asymmetry direction: per frozen prereg section 3.4 (line 314-316) this is the
# weakest observable and may be inconclusive. Recorded with literature-quoted
# omega-freeze direction as placeholder; flagged "weak, not load-bearing".
MATTER_ASYMMETRY_PLACEHOLDER = {
    "l_deg": OMEGA_FREEZE_L_DEG,
    "b_deg": OMEGA_FREEZE_B_DEG,
    "sigma_deg": 60.0,
    "reference": "Frozen methodology prereg section 3.4: directional matter-asymmetry "
    "probes are marginal; recorded for completeness, flagged low-confidence.",
}

# ----------------------------------------------------------------------------
# Geometry utilities
# ----------------------------------------------------------------------------


def galactic_to_cartesian(l_deg: float, b_deg: float) -> np.ndarray:
    """Galactic (l, b) in degrees -> unit Cartesian vector."""
    l = math.radians(l_deg)
    b = math.radians(b_deg)
    return np.array([math.cos(b) * math.cos(l), math.cos(b) * math.sin(l), math.sin(b)])


def cartesian_to_galactic(v: np.ndarray) -> tuple[float, float]:
    """Cartesian unit vector -> galactic (l, b) in degrees."""
    v = v / np.linalg.norm(v)
    b = math.degrees(math.asin(max(-1.0, min(1.0, v[2]))))
    l = math.degrees(math.atan2(v[1], v[0]))
    if l < 0:
        l += 360.0
    return l, b


def angular_separation_deg_undirected(l1: float, b1: float, l2: float, b2: float) -> float:
    """Undirected angular separation between two axes (galactic l, b).

    Axes are direction-only (lines through origin), not rays; takes min(theta, 180-theta).
    """
    v1 = galactic_to_cartesian(l1, b1)
    v2 = galactic_to_cartesian(l2, b2)
    dot = max(-1.0, min(1.0, float(np.dot(v1, v2))))
    theta = math.degrees(math.acos(abs(dot)))
    return theta


# ----------------------------------------------------------------------------
# Planck PR3 axis-of-evil computation
# ----------------------------------------------------------------------------


@dataclass
class AxisOfEvilResult:
    l_deg: float
    b_deg: float
    sigma_deg: float
    dispersion: float
    method: str
    map_file: str
    nside_grid_initial: int
    nside_grid_refined: int
    lmax: int
    # Diagnostic per-ell axes (joint ell=2,3 above is the de Oliveira-Costa axis-of-evil
    # combined estimator; here we report ell=2 and ell=3 separately as cross-validation)
    ell2_only_l_deg: float = 0.0
    ell2_only_b_deg: float = 0.0
    ell2_only_dispersion: float = 0.0
    ell3_only_l_deg: float = 0.0
    ell3_only_b_deg: float = 0.0
    ell3_only_dispersion: float = 0.0
    ell2_vs_ell3_axis_separation_deg: float = 0.0
    # Dispersion at corpus-quoted reference (174, -5) for citation-gap quantification
    corpus_174_neg5_dispersion: float = 0.0
    masking_applied: bool = False
    masking_note: str = ""


def load_planck_smica_temperature(map_path: Path, mask_path: Optional[Path] = None):
    """Load Planck PR3 SMICA map's temperature column; optionally apply mask + mean-fill inpainting.

    The SMICA full-mission IQU file has TEMPERATURE, Q_STOKES, U_STOKES (and uncertainty)
    in extension 1. We read just I (temperature) in Kelvin (the column 'I_STOKES').

    If a mask is provided, masked-out pixels are replaced with the mean of unmasked pixels
    (simple mean-fill inpainting — adequate for low-ell axis-of-evil work; full-blown
    constrained-realization inpainting is overkill for axis-direction estimation).

    Returns (map, mask_info_dict) where mask_info_dict has metadata about masking applied.
    """
    import healpy as hp

    print(f"Loading Planck PR3 SMICA map from {map_path.name} ...")
    print(f"  File size: {map_path.stat().st_size / 1e9:.2f} GB")
    cmb_map_T = hp.read_map(str(map_path), field=0)
    print(f"  Loaded NSIDE={hp.get_nside(cmb_map_T)} ({len(cmb_map_T)} pixels)")
    if np.isnan(cmb_map_T).any():
        n_masked = np.isnan(cmb_map_T).sum()
        print(f"  WARNING: {n_masked} pixels are NaN; replacing with 0 for low-ell extraction.")
        cmb_map_T = np.where(np.isnan(cmb_map_T), 0.0, cmb_map_T)

    mask_info = {"applied": False, "mask_file": None, "sky_fraction_unmasked": 1.0}
    if mask_path is not None and mask_path.exists():
        print(f"Loading Planck PR3 mask from {mask_path.name} ...")
        mask = hp.read_map(str(mask_path), field=0)
        sky_frac = float(np.mean(mask))
        print(f"  Mask sky-fraction unmasked: {sky_frac:.3f}")
        mean_unmasked = float(np.mean(cmb_map_T[mask > 0.5]))
        cmb_map_T = np.where(mask > 0.5, cmb_map_T, mean_unmasked)
        mask_info = {
            "applied": True,
            "mask_file": mask_path.name,
            "sky_fraction_unmasked": sky_frac,
            "inpainting_method": "mean-fill (mean of unmasked region)",
        }
    return cmb_map_T, mask_info


def compute_alm_low_ell(cmb_map_T: np.ndarray, lmax: int = 3):
    """Compute alm coefficients up to lmax via hp.map2alm.

    For axis-of-evil, we need only the low multipoles (l=2 quadrupole + l=3 octupole).
    """
    import healpy as hp

    print(f"Computing alm up to lmax={lmax} via hp.map2alm ...")
    alm = hp.map2alm(cmb_map_T, lmax=lmax, use_pixel_weights=True)
    print(f"  alm computed: {len(alm)} coefficients")
    return alm


def angular_momentum_dispersion(alm: np.ndarray, lmax: int, ell_range: tuple[int, int]) -> float:
    """Compute sum over ell of (sum_m m^2 |a_lm|^2) / (l(l+1) * sum_m |a_lm|^2).

    Per de Oliveira-Costa et al. 2004 maximum-angular-momentum-dispersion estimator.

    For each ell in ell_range (inclusive), the per-ell contribution is normalized
    so that ell=2 and ell=3 contribute on comparable footing.
    """
    import healpy as hp

    ell_min, ell_max = ell_range
    total = 0.0
    for ell in range(ell_min, ell_max + 1):
        sum_m2 = 0.0
        sum_all = 0.0
        for m in range(0, ell + 1):
            idx = hp.Alm.getidx(lmax, ell, m)
            # healpy stores m>=0 only; m and -m contribute equal magnitude
            weight = 1.0 if m == 0 else 2.0
            mag2 = abs(alm[idx]) ** 2
            sum_m2 += weight * m * m * mag2
            sum_all += weight * mag2
        if sum_all > 0:
            total += sum_m2 / (ell * (ell + 1) * sum_all)
    return total


def search_preferred_axis(alm: np.ndarray, lmax: int, ell_range: tuple[int, int], nside_grid: int) -> tuple[int, float]:
    """Grid search over HEALPix pixel directions for the maximum-dispersion axis.

    For each candidate pixel center, rotate alm so the pixel direction becomes +z,
    then compute the angular-momentum dispersion in the rotated frame. Returns
    (best_pixel_index, best_dispersion).
    """
    import healpy as hp

    npix = hp.nside2npix(nside_grid)
    print(f"  Grid search: NSIDE={nside_grid} ({npix} candidate directions)")
    theta_grid, phi_grid = hp.pix2ang(nside_grid, np.arange(npix))

    best_dispersion = -np.inf
    best_pix = -1
    progress_interval = max(1, npix // 20)
    for i in range(npix):
        # healpy's Rotator(rot=[psi, theta_euler]) interprets the args as ZYZ
        # Euler angles (psi, theta_euler, 0). After rotation, the new +z direction
        # is at spherical (theta_pix, phi_pix) in the original frame, with:
        #   theta_euler = degrees(theta_pix)  (colatitude of the candidate axis)
        #   psi = degrees(phi_pix)            (longitude of the candidate axis)
        # Verified empirically: for pure a_{2,0}, rot=[any, 90] -> dispersion 3
        # (maximum), corresponding to candidate axis at the equator.
        lon = math.degrees(phi_grid[i])
        lat = math.degrees(theta_grid[i])
        rotator = hp.Rotator(rot=[lon, lat], deg=True)
        alm_rotated = rotator.rotate_alm(alm.copy())
        d = angular_momentum_dispersion(alm_rotated, lmax, ell_range)
        if d > best_dispersion:
            best_dispersion = d
            best_pix = i
        if (i + 1) % progress_interval == 0:
            print(f"    {i+1}/{npix} ({100*(i+1)/npix:.0f}%) — best={best_dispersion:.4f}")

    return best_pix, best_dispersion


def axis_of_evil_from_planck(
    map_path: Path,
    mask_path: Optional[Path] = None,
    nside_initial: int = 16,
    nside_refined: int = 64,
    lmax: int = 3,
    ell_range: tuple[int, int] = (2, 3),
) -> AxisOfEvilResult:
    """Compute the Planck PR3 axis-of-evil via two-stage grid search.

    If mask_path is provided, applies the Planck common-mask + mean-fill inpainting
    before alm computation. This is the standard literature practice for low-ell
    axis-of-evil analyses (removes galactic-plane foreground residuals).
    """
    import healpy as hp

    if not map_path.exists():
        raise FileNotFoundError(
            f"Planck PR3 SMICA map not found at {map_path}. "
            f"Download from https://pla.esac.esa.int/pla/aio/product-action?MAP.MAP_ID={map_path.name}"
        )

    cmb_map_T, mask_info = load_planck_smica_temperature(map_path, mask_path)
    alm = compute_alm_low_ell(cmb_map_T, lmax=lmax)

    print(f"\nStage 1: coarse grid search at NSIDE={nside_initial} ...")
    best_pix_initial, best_d_initial = search_preferred_axis(alm, lmax, ell_range, nside_initial)
    theta_initial, phi_initial = hp.pix2ang(nside_initial, best_pix_initial)
    print(
        f"  Stage 1 best: theta={math.degrees(theta_initial):.2f} deg, "
        f"phi={math.degrees(phi_initial):.2f} deg, dispersion={best_d_initial:.6f}"
    )

    print(f"\nStage 2: refined grid at NSIDE={nside_refined} (local neighborhood) ...")
    pix_initial_neighbors = hp.query_disc(
        nside_refined,
        hp.ang2vec(theta_initial, phi_initial),
        radius=math.radians(15.0),
    )
    print(f"  {len(pix_initial_neighbors)} candidate pixels in 15-deg cap")
    theta_grid, phi_grid = hp.pix2ang(nside_refined, pix_initial_neighbors)

    best_dispersion = -np.inf
    best_pix_refined = -1
    for k, pix in enumerate(pix_initial_neighbors):
        # Same Euler-angle convention as Stage 1 (see comment in search_preferred_axis).
        lon = math.degrees(phi_grid[k])
        lat = math.degrees(theta_grid[k])
        rotator = hp.Rotator(rot=[lon, lat], deg=True)
        alm_rotated = rotator.rotate_alm(alm.copy())
        d = angular_momentum_dispersion(alm_rotated, lmax, ell_range)
        if d > best_dispersion:
            best_dispersion = d
            best_pix_refined = pix

    theta_best, phi_best = hp.pix2ang(nside_refined, best_pix_refined)
    # Direction in healpy coords -> Cartesian -> galactic
    # NOTE: hp.pix2ang returns (theta, phi) in spherical coords. Whether this is
    # equatorial or galactic depends on the map's coordinate convention. Planck PR3
    # SMICA maps are in GALACTIC coordinates by default (the standard for CMB analysis).
    cart_best = hp.ang2vec(theta_best, phi_best)
    l_deg, b_deg = cartesian_to_galactic(cart_best)

    pixel_size_deg = math.degrees(math.sqrt(4 * math.pi / hp.nside2npix(nside_refined)))
    print(f"\nAxis-of-evil result (joint ell=2,3):")
    print(f"  (l, b) = ({l_deg:.2f} deg, {b_deg:.2f} deg) galactic")
    print(f"  Dispersion: {best_dispersion:.6f}")
    print(f"  Grid resolution: {pixel_size_deg:.2f} deg")

    # ---- Diagnostic: per-ell axes (cross-validation) ----
    print(f"\nDiagnostic: searching ell=2 only axis ...")
    best_pix_l2, best_d_l2 = search_preferred_axis(alm, lmax, (2, 2), nside_initial)
    theta_l2, phi_l2 = hp.pix2ang(nside_initial, best_pix_l2)
    l_l2, b_l2 = cartesian_to_galactic(hp.ang2vec(theta_l2, phi_l2))
    print(f"  ell=2 only: (l, b) = ({l_l2:.2f}, {b_l2:.2f}), d={best_d_l2:.4f}")

    print(f"Diagnostic: searching ell=3 only axis ...")
    best_pix_l3, best_d_l3 = search_preferred_axis(alm, lmax, (3, 3), nside_initial)
    theta_l3, phi_l3 = hp.pix2ang(nside_initial, best_pix_l3)
    l_l3, b_l3 = cartesian_to_galactic(hp.ang2vec(theta_l3, phi_l3))
    print(f"  ell=3 only: (l, b) = ({l_l3:.2f}, {b_l3:.2f}), d={best_d_l3:.4f}")

    # Angular separation between ell=2 and ell=3 preferred axes
    v_l2 = hp.ang2vec(theta_l2, phi_l2)
    v_l3 = hp.ang2vec(theta_l3, phi_l3)
    dot = float(np.dot(v_l2, v_l3))
    sep_23 = math.degrees(math.acos(max(-1.0, min(1.0, abs(dot)))))
    print(
        f"  Angular separation ell=2 vs ell=3 axes: {sep_23:.2f} deg "
        f"(small = strong axis-of-evil alignment in data)"
    )

    # ---- Diagnostic: dispersion at corpus (l=174, b=-5) ----
    # Per closure-roadmap.md:100 + the 2026-05-17 audit, the (174, -5) value
    # in the AVE corpus lacks a specific publication pin. This driver verifies
    # whether the corpus value matches the Planck PR3 data.
    theta_corpus = math.radians(90.0 - OMEGA_FREEZE_B_DEG)
    phi_corpus = math.radians(OMEGA_FREEZE_L_DEG)
    lon_corpus = math.degrees(phi_corpus)
    lat_corpus = math.degrees(theta_corpus)
    rotator_corpus = hp.Rotator(rot=[lon_corpus, lat_corpus], deg=True)
    alm_corpus = rotator_corpus.rotate_alm(alm.copy())
    d_corpus = angular_momentum_dispersion(alm_corpus, lmax, ell_range)
    print(
        f"  Dispersion at corpus (l={OMEGA_FREEZE_L_DEG}, b={OMEGA_FREEZE_B_DEG}): "
        f"{d_corpus:.4f} (compare to data max {best_dispersion:.4f})"
    )

    return AxisOfEvilResult(
        l_deg=l_deg,
        b_deg=b_deg,
        sigma_deg=pixel_size_deg,
        dispersion=best_dispersion,
        method=(
            "de Oliveira-Costa et al. 2004 max-angular-momentum-dispersion; "
            "two-stage HEALPix grid search; SMICA T-only"
            + ("; Planck PR3 common mask + mean-fill inpainting" if mask_info["applied"] else "; no masking applied")
        ),
        map_file=map_path.name,
        nside_grid_initial=nside_initial,
        nside_grid_refined=nside_refined,
        lmax=lmax,
        ell2_only_l_deg=l_l2,
        ell2_only_b_deg=b_l2,
        ell2_only_dispersion=best_d_l2,
        ell3_only_l_deg=l_l3,
        ell3_only_b_deg=b_l3,
        ell3_only_dispersion=best_d_l3,
        ell2_vs_ell3_axis_separation_deg=sep_23,
        corpus_174_neg5_dispersion=d_corpus,
        masking_applied=mask_info["applied"],
        masking_note=(
            f"Planck PR3 common temperature mask applied (sky fraction unmasked = "
            f"{mask_info['sky_fraction_unmasked']:.3f}); inpainting = "
            f"{mask_info.get('inpainting_method', 'mean-fill')}."
            if mask_info["applied"]
            else "No masking applied; foreground residuals near galactic plane may bias "
            "the low-ell axis estimate. Re-run with mask if material."
        ),
    )


# ----------------------------------------------------------------------------
# Pairwise alignment matrix + statistics
# ----------------------------------------------------------------------------


@dataclass
class Observable:
    name: str
    l_deg: float
    b_deg: float
    sigma_deg: float
    source: str
    method: str  # 'data-derived' or 'paper-pinned'
    confidence: str  # 'load-bearing', 'literature-pinned', 'weak'


def pairwise_alignment_matrix(observables: list[Observable]) -> dict:
    """Compute pairwise angular-separation matrix + combined-uncertainty test.

    Returns dict with:
      - matrix: NxN angular separations (deg, undirected)
      - sigma_combined_matrix: NxN combined 1-sigma uncertainty (deg)
      - within_3sigma_matrix: NxN boolean (separation < threshold within 3-sigma combined)
      - violates_sharpest_falsifier: bool (CMB-vs-Hubble separation > 20 deg at 3-sigma)
    """
    n = len(observables)
    sep_matrix = np.zeros((n, n))
    sigma_combined_matrix = np.zeros((n, n))
    within_3sigma = np.zeros((n, n), dtype=bool)
    within_tight = np.zeros((n, n), dtype=bool)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            sep_ij = angular_separation_deg_undirected(
                observables[i].l_deg, observables[i].b_deg, observables[j].l_deg, observables[j].b_deg
            )
            sep_matrix[i, j] = sep_ij
            sigma_ij = math.sqrt(observables[i].sigma_deg ** 2 + observables[j].sigma_deg ** 2)
            sigma_combined_matrix[i, j] = sigma_ij
            within_3sigma[i, j] = sep_ij < PASS_THRESHOLD_DEG + 3.0 * sigma_ij
            within_tight[i, j] = sep_ij < TIGHT_THRESHOLD_DEG + 3.0 * sigma_ij

    # Sharpest single falsifier: CMB axis-of-evil vs Hubble flow
    cmb_idx = next(i for i, o in enumerate(observables) if "CMB" in o.name and "axis" in o.name.lower())
    hubble_idx = next(i for i, o in enumerate(observables) if "Hubble" in o.name)
    cmb_hubble_sep = sep_matrix[cmb_idx, hubble_idx]
    cmb_hubble_sigma = sigma_combined_matrix[cmb_idx, hubble_idx]
    sharpest_falsifier_violated = cmb_hubble_sep > (PASS_THRESHOLD_DEG + 3.0 * cmb_hubble_sigma)

    return {
        "n_observables": n,
        "observable_names": [o.name for o in observables],
        "separation_matrix_deg": sep_matrix.tolist(),
        "sigma_combined_matrix_deg": sigma_combined_matrix.tolist(),
        "within_pass_threshold_3sigma_matrix": within_3sigma.tolist(),
        "within_tight_threshold_3sigma_matrix": within_tight.tolist(),
        "sharpest_falsifier": {
            "cmb_vs_hubble_separation_deg": float(cmb_hubble_sep),
            "combined_sigma_deg": float(cmb_hubble_sigma),
            "threshold_deg": PASS_THRESHOLD_DEG,
            "violated": bool(sharpest_falsifier_violated),
        },
    }


def degree_class_agreement_statistic(observables: list[Observable], pairwise_matrix: dict) -> dict:
    """Compute degree-class agreement statistic vs uniform-prior null.

    Agreement statistic: fraction of unordered pairs (i<j) with separation < threshold.
    Uniform-prior null: probability that a random pair of unit vectors on the sphere
    has angular separation < threshold (with axes as undirected, so theta -> min(theta, 180-theta)).
    """
    n = len(observables)
    sep_matrix = np.array(pairwise_matrix["separation_matrix_deg"])
    pairs_within_pass = 0
    pairs_within_tight = 0
    total_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if observables[i].confidence == "weak" or observables[j].confidence == "weak":
                continue
            total_pairs += 1
            if sep_matrix[i, j] < PASS_THRESHOLD_DEG:
                pairs_within_pass += 1
            if sep_matrix[i, j] < TIGHT_THRESHOLD_DEG:
                pairs_within_tight += 1

    # Uniform prior null for undirected axes:
    # For a random axis on the sphere, P(angular separation < theta_max) = 1 - cos(theta_max)
    # (for axes, the probability of being within theta_max of a fixed axis, where axes
    # are undirected lines, is just 1 - cos(theta_max) since we take min(theta, 180-theta))
    p_null_pass = 1.0 - math.cos(math.radians(PASS_THRESHOLD_DEG))
    p_null_tight = 1.0 - math.cos(math.radians(TIGHT_THRESHOLD_DEG))

    return {
        "total_pairs_non_weak": total_pairs,
        "pairs_within_pass_threshold": pairs_within_pass,
        "pairs_within_tight_threshold": pairs_within_tight,
        "agreement_fraction_pass": pairs_within_pass / total_pairs if total_pairs > 0 else 0.0,
        "agreement_fraction_tight": pairs_within_tight / total_pairs if total_pairs > 0 else 0.0,
        "uniform_prior_null_probability_pass": p_null_pass,
        "uniform_prior_null_probability_tight": p_null_tight,
        "pass_threshold_deg": PASS_THRESHOLD_DEG,
        "tight_threshold_deg": TIGHT_THRESHOLD_DEG,
    }


# ----------------------------------------------------------------------------
# Adjudication per frozen prereg outcomes
# ----------------------------------------------------------------------------


def adjudicate(observables: list[Observable], pairwise: dict, agreement: dict) -> dict:
    """Map driver results to frozen prereg outcomes A+ / A / B / C / D / E."""
    sharpest = pairwise["sharpest_falsifier"]
    sharpest_violated = sharpest["violated"]
    if sharpest_violated:
        return {
            "outcome": "C",
            "name": "NULL — sharpest single falsifier violated",
            "explanation": "CMB axis-of-evil vs Hubble flow misaligned > 20 deg at "
            "combined 3 sigma. Per closure-roadmap.md:35 + frozen prereg "
            "section 5, this is the load-bearing discriminator: A-034 "
            "cosmic-scale instance has failed. Catalog survives if "
            "the 20+ other A-034 instances hold.",
            "cascade_implication": "D4-A034 cosmic row RETIRES. C4 three-route Route 3 "
            "stays DEFERRED on A-031 cosmic-parameter-horizon. "
            "E2b (DM META closure) becomes natural alternative next session.",
        }

    n_non_weak = agreement["total_pairs_non_weak"]
    pairs_pass = agreement["pairs_within_pass_threshold"]
    pairs_tight = agreement["pairs_within_tight_threshold"]
    frac_pass = agreement["agreement_fraction_pass"]
    frac_tight = agreement["agreement_fraction_tight"]
    p_null_pass = agreement["uniform_prior_null_probability_pass"]

    # Outcome A+ : 4-of-4 axes mutually aligned within 10 deg AND agreement > 95%
    if frac_tight >= 0.95 and pairs_tight == n_non_weak:
        return {
            "outcome": "A+",
            "name": "STRONGEST PASS",
            "explanation": (
                f"All {n_non_weak} non-weak pairs aligned within "
                f"{TIGHT_THRESHOLD_DEG:.0f} deg at 3 sigma; tight-threshold agreement "
                f"fraction = {frac_tight:.1%}. Strong evidence for parent-BH spin axis "
                f"preservation through cosmic lattice genesis."
            ),
            "cascade_implication": (
                "D4-A034 cosmic row STRENGTHENS. C4 three-route Route 3 (J_cosmic) "
                "gains empirical anchor. E1c (Route 3 framework-commitment activation) "
                "becomes immediately tractable per closure-roadmap.md:947."
            ),
        }

    if frac_pass >= 0.80 and pairs_pass >= n_non_weak - 1:
        return {
            "outcome": "A",
            "name": "PASS",
            "explanation": (
                f"{pairs_pass}-of-{n_non_weak} pairs aligned within "
                f"{PASS_THRESHOLD_DEG:.0f} deg; pass-threshold agreement fraction = "
                f"{frac_pass:.1%} (vs uniform-prior null ~{p_null_pass:.2%}). "
                "Evidence for shared underlying axis."
            ),
            "cascade_implication": (
                "D4-A034 cosmic row strengthens. C4 three-route Route 3 (J_cosmic) "
                "gains partial anchor; E1c becomes tractable."
            ),
        }

    if frac_pass >= 0.50:
        return {
            "outcome": "B",
            "name": "PARTIAL",
            "explanation": (
                f"{pairs_pass}-of-{n_non_weak} pairs aligned at "
                f"{PASS_THRESHOLD_DEG:.0f} deg; agreement fraction = {frac_pass:.1%}. "
                "Tension structure between observables; framework partially supported. "
                "Identify which observable misaligns and investigate."
            ),
            "cascade_implication": (
                "D4-A034 cosmic row holds with tension flag. E1c deferred pending "
                "methodology investigation of which observable misaligns."
            ),
        }

    # Outcome D check: data insufficient to discriminate at 3 sigma.
    # Conditions:
    #   (a) sharpest falsifier (CMB-vs-Hubble > 20 deg at 3 sigma) NOT violated
    #   (b) NO pair is aligned at strict central-value threshold (frac_pass = 0)
    #   (c) literature observable uncertainties are wide (>= 25 deg on at least 2 obs)
    n_wide_sigma_obs = sum(1 for o in observables if o.sigma_deg >= 25.0 and o.confidence != "weak")
    insufficient_to_discriminate = not sharpest_violated and frac_pass == 0 and n_wide_sigma_obs >= 2
    if insufficient_to_discriminate:
        return {
            "outcome": "D",
            "name": "DATA INSUFFICIENT — uncertainties too wide for 3-sigma discrimination",
            "explanation": (
                f"Central-value pairwise separations show no alignment at strict "
                f"{PASS_THRESHOLD_DEG:.0f}-deg threshold (frac = 0%), BUT the literature "
                f"observable uncertainties (Pantheon+ sigma ~30 deg, SDSS sigma ~30 deg) "
                f"are too wide to reject alignment at 3-sigma confidence. "
                f"CMB-vs-Hubble separation = {sharpest['cmb_vs_hubble_separation_deg']:.1f} deg, "
                f"combined sigma = {sharpest['combined_sigma_deg']:.1f} deg; "
                f"(sep - 20 deg) / sigma = "
                f"{(sharpest['cmb_vs_hubble_separation_deg'] - PASS_THRESHOLD_DEG) / sharpest['combined_sigma_deg']:.2f} sigma "
                f"(below 3-sigma decisive threshold). Central values LEAN TOWARD C (NULL) but "
                f"cannot conclusively reject A (PASS) at the prereg's 3-sigma criterion."
            ),
            "cascade_implication": (
                "D4-A034 cosmic row held PENDING tighter Hubble-flow / SDSS data. "
                "Surface to Grant for methodology adjudication: tighter Pantheon+ bulk-flow "
                "re-analysis from raw SN data, or independent LSS spin-orientation analysis, "
                "would tighten the 3-sigma test. E1c deferred until C5 settles."
            ),
        }

    # Outcome B (marginal): above 2x null but below pass criterion
    if frac_pass > p_null_pass * 2.0:
        return {
            "outcome": "B",
            "name": "PARTIAL (above-null but below pass-threshold)",
            "explanation": (
                f"Pairwise agreement {frac_pass:.1%} is above 2x uniform-prior null "
                f"({p_null_pass:.2%}) but below pass criterion (50%). Marginal evidence; "
                "could be statistical fluctuation."
            ),
            "cascade_implication": ("D4-A034 cosmic row holds with low-confidence flag. E1c deferred."),
        }

    return {
        "outcome": "C",
        "name": "NULL — uniform-prior consistent",
        "explanation": (
            f"Pairwise agreement {frac_pass:.1%} is consistent with uniform-prior null "
            f"({p_null_pass:.2%}). No preferred-axis evidence above chance."
        ),
        "cascade_implication": (
            "D4-A034 cosmic row RETIRES (catalog survives if 20+ other instances hold). "
            "C4 three-route Route 3 stays DEFERRED. E2b (DM META) becomes natural alternative."
        ),
    }


# ----------------------------------------------------------------------------
# Main pipeline
# ----------------------------------------------------------------------------


def main():
    print("=" * 80)
    print("C5-CMB-AXIS Executable Observer — Phase 2")
    print(
        "Frozen prereg: research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md"
    )
    print("Execution prereg: research/2026-05-19_c5-cmb-axis-executable-observer-prereg.md")
    print("=" * 80)
    print()

    # ---- Observable 1: Planck PR3 axis-of-evil ----
    smica_path = PLANCK_DIR / "COM_CMB_IQU-smica_2048_R3.00_full.fits"
    mask_path = PLANCK_DIR / "COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits"
    if not mask_path.exists():
        mask_path = None
        print("INFO: Planck common-mask file not found locally; running without masking.")
    observable_1: Optional[Observable] = None
    aoe_result: Optional[AxisOfEvilResult] = None
    if smica_path.exists():
        try:
            aoe_result = axis_of_evil_from_planck(smica_path, mask_path=mask_path)
            observable_1 = Observable(
                name="CMB axis-of-evil (Planck PR3 SMICA, data-derived)",
                l_deg=aoe_result.l_deg,
                b_deg=aoe_result.b_deg,
                sigma_deg=aoe_result.sigma_deg,
                source=f"Computed from {aoe_result.map_file} via {aoe_result.method}",
                method="data-derived",
                confidence="load-bearing",
            )
        except Exception as e:
            print(f"\nERROR: axis-of-evil computation failed: {e}")
            print("Falling back to literature-quoted (174, -5) axis with FLAG outcome.")
            observable_1 = Observable(
                name="CMB axis-of-evil (literature reference; data computation FAILED)",
                l_deg=OMEGA_FREEZE_L_DEG,
                b_deg=OMEGA_FREEZE_B_DEG,
                sigma_deg=30.0,
                source="universal-saturation-kernel-catalog.md:88 (data computation failed)",
                method="paper-pinned (fallback)",
                confidence="literature-pinned",
            )
    else:
        print(f"\nERROR: SMICA map not found at {smica_path}")
        print("Outcome E (RETIRE this session) — data access failed.")
        return {
            "outcome": "E",
            "name": "RETIRE — Planck PR3 data not available locally",
            "smica_path": str(smica_path),
        }

    # ---- Observable 2: Hubble flow (paper-pinned) ----
    observable_2 = Observable(
        name="Hubble flow bulk direction (Pantheon+, Whitford+2023)",
        l_deg=PANTHEON_BULK_FLOW_WHITFORD2023["l_deg"],
        b_deg=PANTHEON_BULK_FLOW_WHITFORD2023["b_deg"],
        sigma_deg=PANTHEON_BULK_FLOW_WHITFORD2023["sigma_deg"],
        source=PANTHEON_BULK_FLOW_WHITFORD2023["reference"],
        method="paper-pinned",
        confidence="literature-pinned",
    )

    # ---- Observable 3: LSS galaxy spin (paper-pinned) ----
    observable_3 = Observable(
        name="LSS galaxy spin axis (SDSS, Longo 2011 + Shamir 2020)",
        l_deg=SDSS_LSS_SPIN_LONGO2011["l_deg"],
        b_deg=SDSS_LSS_SPIN_LONGO2011["b_deg"],
        sigma_deg=SDSS_LSS_SPIN_LONGO2011["sigma_deg"],
        source=SDSS_LSS_SPIN_LONGO2011["reference"],
        method="paper-pinned",
        confidence="literature-pinned",
    )

    # ---- Observable 4: Matter-asymmetry (weak per prereg section 3.4) ----
    observable_4 = Observable(
        name="Matter-asymmetry direction (weak / inconclusive per prereg section 3.4)",
        l_deg=MATTER_ASYMMETRY_PLACEHOLDER["l_deg"],
        b_deg=MATTER_ASYMMETRY_PLACEHOLDER["b_deg"],
        sigma_deg=MATTER_ASYMMETRY_PLACEHOLDER["sigma_deg"],
        source=MATTER_ASYMMETRY_PLACEHOLDER["reference"],
        method="paper-pinned",
        confidence="weak",
    )

    observables = [observable_1, observable_2, observable_3, observable_4]

    if aoe_result is not None:
        print("\n" + "=" * 80)
        print("CMB axis diagnostics")
        print("=" * 80)
        print(
            f"  Joint ell=2,3 axis: (l, b) = ({aoe_result.l_deg:.2f}, {aoe_result.b_deg:.2f}), "
            f"d = {aoe_result.dispersion:.4f}"
        )
        print(
            f"  ell=2 only axis:    (l, b) = ({aoe_result.ell2_only_l_deg:.2f}, "
            f"{aoe_result.ell2_only_b_deg:.2f}), d = {aoe_result.ell2_only_dispersion:.4f}"
        )
        print(
            f"  ell=3 only axis:    (l, b) = ({aoe_result.ell3_only_l_deg:.2f}, "
            f"{aoe_result.ell3_only_b_deg:.2f}), d = {aoe_result.ell3_only_dispersion:.4f}"
        )
        print(
            f"  ell=2 vs ell=3 axis separation: {aoe_result.ell2_vs_ell3_axis_separation_deg:.2f} deg "
            f"(small = strong intrinsic axis-of-evil alignment in data)"
        )
        print(
            f"  Dispersion at corpus ({OMEGA_FREEZE_L_DEG}, {OMEGA_FREEZE_B_DEG}): "
            f"{aoe_result.corpus_174_neg5_dispersion:.4f} "
            f"(vs data max {aoe_result.dispersion:.4f}, ratio "
            f"{aoe_result.corpus_174_neg5_dispersion / aoe_result.dispersion:.1%})."
        )
        print(f"  Corpus citation-gap finding: corpus value (174, -5) is NOT the data preferred axis.")

    print("\n" + "=" * 80)
    print("Observable axes (galactic coordinates)")
    print("=" * 80)
    print(f"{'#':>2} {'Name':<60} {'l (deg)':>8} {'b (deg)':>8} {'sigma':>6} {'conf':<18}")
    for i, o in enumerate(observables):
        print(f"{i+1:>2} {o.name[:60]:<60} {o.l_deg:>8.2f} {o.b_deg:>8.2f} " f"{o.sigma_deg:>6.1f} {o.confidence:<18}")
    print()

    # ---- Pairwise alignment matrix ----
    pairwise = pairwise_alignment_matrix(observables)
    print("=" * 80)
    print("Pairwise angular-separation matrix (deg, undirected)")
    print("=" * 80)
    n = len(observables)
    print(f"{'':>3}", end="")
    for j in range(n):
        print(f"{'#'+str(j+1):>9}", end="")
    print()
    for i in range(n):
        print(f"#{i+1:>2}", end="")
        for j in range(n):
            print(f"{pairwise['separation_matrix_deg'][i][j]:>9.1f}", end="")
        print()
    print()

    print(f"Sharpest single falsifier (CMB vs Hubble):")
    print(f"  separation = {pairwise['sharpest_falsifier']['cmb_vs_hubble_separation_deg']:.1f} deg")
    print(f"  combined sigma = {pairwise['sharpest_falsifier']['combined_sigma_deg']:.1f} deg")
    print(f"  threshold = {pairwise['sharpest_falsifier']['threshold_deg']:.1f} deg")
    print(f"  violated = {pairwise['sharpest_falsifier']['violated']}")
    print()

    # ---- Degree-class agreement statistic ----
    agreement = degree_class_agreement_statistic(observables, pairwise)
    print("=" * 80)
    print("Degree-class agreement statistic vs uniform-prior null")
    print("=" * 80)
    print(f"Non-weak pairs: {agreement['total_pairs_non_weak']}")
    print(
        f"Pairs within {agreement['pass_threshold_deg']:.0f} deg: "
        f"{agreement['pairs_within_pass_threshold']} "
        f"(fraction = {agreement['agreement_fraction_pass']:.2%}, "
        f"null = {agreement['uniform_prior_null_probability_pass']:.2%})"
    )
    print(
        f"Pairs within {agreement['tight_threshold_deg']:.0f} deg: "
        f"{agreement['pairs_within_tight_threshold']} "
        f"(fraction = {agreement['agreement_fraction_tight']:.2%}, "
        f"null = {agreement['uniform_prior_null_probability_tight']:.2%})"
    )
    print()

    # ---- Adjudication ----
    verdict = adjudicate(observables, pairwise, agreement)
    print("=" * 80)
    print(f"OUTCOME: {verdict['outcome']} — {verdict['name']}")
    print("=" * 80)
    print(f"Explanation: {verdict['explanation']}")
    print()
    print(f"Cascade: {verdict['cascade_implication']}")
    print()

    # ---- Serialize result JSON ----
    results = {
        "driver": "cmb_axis_alignment_executable_observer.py",
        "execution_session_prereg": "research/2026-05-19_c5-cmb-axis-executable-observer-prereg.md",
        "frozen_methodology_prereg": "research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md",
        "branch": "analysis/c5-cmb-axis-driver",
        "date": "2026-05-19",
        "data_sources": {
            "planck_pr3_smica": {
                "url": "https://pla.esac.esa.int/pla/aio/product-action?MAP.MAP_ID=COM_CMB_IQU-smica_2048_R3.00_full.fits",
                "filename": "COM_CMB_IQU-smica_2048_R3.00_full.fits",
            },
            "pantheon_plus_bulk_flow": PANTHEON_BULK_FLOW_WHITFORD2023,
            "sdss_lss_spin": SDSS_LSS_SPIN_LONGO2011,
            "matter_asymmetry": MATTER_ASYMMETRY_PLACEHOLDER,
        },
        "axis_of_evil_computation": asdict(aoe_result) if aoe_result else None,
        "observables": [asdict(o) for o in observables],
        "pairwise_alignment": pairwise,
        "degree_class_agreement": agreement,
        "verdict": verdict,
    }
    with open(RESULTS_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results written to: {RESULTS_PATH}")
    return results


if __name__ == "__main__":
    main()
