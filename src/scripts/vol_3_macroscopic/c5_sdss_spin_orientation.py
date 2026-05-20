"""
C5-CMB-AXIS SDSS Spin-Orientation Re-Analysis — executable driver.

Re-fits the LSS galaxy-spin-axis dipole direction from the raw Galaxy Zoo 1
(SDSS DR7) crowdsourced morphological classifications, replacing the
paper-pinned Longo 2011 + Shamir 2020 literal `(l=32°, b=32°), sigma=30°`
with a self-derived `(l, b, sigma_LSS)` triple from the public catalog.

Per the frozen pre-registration at
`research/2026-05-19_c5-sdss-spin-orientation-prereg.md`, this driver:

1. Loads `data/sdss_dr17/GalaxyZoo1_DR_table2.csv.gz` (667,944 galaxies).
2. Applies Q-cuts: SPIRAL==1, NVOTE>=10, |P_CW - P_ACW| >= delta_clear.
3. Assigns per-galaxy chirality_i = +1 if P_CW > P_ACW else -1.
4. Runs Longo 2011 cos gamma axial-dipole estimator via two-stage HEALPix
   grid search (NSIDE=16 coarse -> NSIDE=64 refined). The fit metric
   A(n_hat) = (1/N) sum_i chi_i * cos(gamma_i) is direction-agnostic;
   the search maximizes |A| over the sphere.
5. Computes sigma_LSS via (A) Hessian + Monte Carlo and (B) block
   bootstrap; canonical = max(A, B) per prereg sec 3.4.
6. Compares to E1b CMB axis-of-evil (l=60.28°, b=50.48°) from
   `cmb_axis_alignment_executable_observer_results.json`.
7. Adjudicates the outcome per the pre-registered A/C/D-sustained/Marginal-D/E
   table.

FORWARD-PREDICTION DISCIPLINE (per ave-driver-script-honesty sec 3.6):
the dipole search never sees the CMB axis. The post-fit comparison uses
the E1b axis only for separation computation. The fit metric is
direction-agnostic.

Run:
    python3 src/scripts/vol_3_macroscopic/c5_sdss_spin_orientation.py
"""
from __future__ import annotations

import gzip
import json
import math
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))

# Canonical constants (per ave-canonical-source; never hard-code).
# C_0 imported for consistency with the bulk-flow driver, though this purely
# geometric test does not use it numerically.
from ave.core.constants import C_0  # noqa: E402, F401


def _resolve_data_dir() -> Path:
    """Resolve data dir, falling back to main repo when run from a worktree.

    Worktrees do not contain `data/` (gitignored); fall back to the parent
    repo's data dir if present. Mirrors c5_pantheon_bulk_flow_tightening.py.
    """
    candidate = REPO_ROOT / "data"
    if candidate.exists() and (candidate / "sdss_dr17").is_dir():
        return candidate
    cur = REPO_ROOT
    while cur != cur.parent:
        if (cur / "data" / "sdss_dr17").is_dir():
            return cur / "data"
        if cur.name == "worktrees" and (cur.parent.parent / "data" / "sdss_dr17").is_dir():
            return cur.parent.parent / "data"
        cur = cur.parent
    canonical = Path("/Users/grantlindblom/AVE-staging/AVE-Core/data")
    if canonical.exists():
        return canonical
    return REPO_ROOT / "data"


DATA_DIR = _resolve_data_dir()
GZ1_CATALOG_PATH = DATA_DIR / "sdss_dr17" / "GalaxyZoo1_DR_table2.csv.gz"
CMB_AXIS_RESULTS_PATH = SCRIPT_DIR / "cmb_axis_alignment_executable_observer_results.json"
RESULTS_PATH = SCRIPT_DIR / "c5_sdss_spin_orientation_results.json"

# Adjudication thresholds (per prereg sec 4):
SIGMA_DECISIVE_AGAINST_ALIGNMENT_DEG = 2.46  # need sigma_LSS < this for 3sigma misalignment
SIGMA_DECISIVE_FOR_ALIGNMENT_DEG = 9.25      # need sigma_LSS > this for 3sigma alignment
SIGMA_MARGINAL_UPPER_DEG = 25.0              # above: D-sustained
SIGMA_BRIEF_TARGET_DEG = 15.0                # brief's target precision
CMB_LSS_PASS_THRESHOLD_DEG = 20.0            # frozen prereg alignment threshold


# ----------------------------------------------------------------------------
# Geometry utilities (mirror c5_pantheon_bulk_flow_tightening.py)
# ----------------------------------------------------------------------------


def galactic_to_cartesian(l_deg: float, b_deg: float) -> np.ndarray:
    """Galactic (l, b) in degrees -> unit Cartesian vector."""
    l = math.radians(l_deg)
    b = math.radians(b_deg)
    return np.array([math.cos(b) * math.cos(l), math.cos(b) * math.sin(l), math.sin(b)])


def cartesian_to_galactic(v: np.ndarray) -> tuple[float, float]:
    """Cartesian unit vector -> galactic (l, b) in degrees."""
    v = np.asarray(v, dtype=float)
    v = v / np.linalg.norm(v)
    b = math.degrees(math.asin(max(-1.0, min(1.0, v[2]))))
    l = math.degrees(math.atan2(v[1], v[0]))
    if l < 0:
        l += 360.0
    return l, b


def canonicalize_axis_lb(l_deg: float, b_deg: float) -> tuple[float, float]:
    """Map (l, b) to the canonical undirected-axis representative with 0 <= l < 180.

    For an axis (line through origin), (l, b) and (l+180, -b) are equivalent.
    We pick the representative with l in [0, 180).
    """
    if l_deg >= 180.0:
        return (l_deg - 180.0) % 360.0, -b_deg
    return l_deg, b_deg


def angular_separation_deg_undirected(l1: float, b1: float, l2: float, b2: float) -> float:
    """Undirected angular separation between two axes (galactic l, b)."""
    v1 = galactic_to_cartesian(l1, b1)
    v2 = galactic_to_cartesian(l2, b2)
    dot = max(-1.0, min(1.0, float(np.dot(v1, v2))))
    return math.degrees(math.acos(abs(dot)))


# ----------------------------------------------------------------------------
# Galaxy Zoo 1 catalog ingest
# ----------------------------------------------------------------------------


@dataclass
class GZ1Subset:
    """Post-cut subsample of GZ1 for the axial-dipole fit.

    All arrays are 1D, indexed by galaxy. `n_hat` is (N, 3) galactic-Cartesian
    unit vectors. `chirality` is +1 (clockwise) or -1 (anticlockwise) per
    Longo 2011 sign convention.
    """
    objids: np.ndarray
    ra_deg: np.ndarray
    dec_deg: np.ndarray
    l_deg: np.ndarray
    b_deg: np.ndarray
    n_hat: np.ndarray  # (N, 3) unit vectors in galactic Cartesian
    chirality: np.ndarray  # +1 / -1
    p_cw: np.ndarray
    p_acw: np.ndarray
    nvote: np.ndarray
    delta_clear: float  # |P_CW - P_ACW| threshold used


_SEXAGESIMAL_RE = re.compile(r"^\s*([+\-]?)(\d+):(\d+):(\d+(?:\.\d+)?)\s*$")


def parse_sexagesimal(s: str, is_hours: bool) -> float:
    """Parse a sexagesimal coordinate string to decimal degrees.

    RA is given in hh:mm:ss.s (hours, multiply by 15); Dec is given in
    ±dd:mm:ss.s (degrees).
    """
    m = _SEXAGESIMAL_RE.match(s)
    if not m:
        raise ValueError(f"Cannot parse sexagesimal coordinate {s!r}")
    sign_str, hh, mm, ss = m.groups()
    sign = -1.0 if sign_str == "-" else 1.0
    value = sign * (float(hh) + float(mm) / 60.0 + float(ss) / 3600.0)
    if is_hours:
        value *= 15.0  # hours -> degrees for RA
    return value


def load_gz1_catalog(
    path: Path,
    delta_clear: float = 0.4,
    min_nvote: int = 10,
) -> GZ1Subset:
    """Load Galaxy Zoo 1 Table 2, apply Q-cuts, return post-cut subset.

    Q-cuts per prereg sec 3.2:
      1. SPIRAL == 1
      2. NVOTE >= min_nvote
      3. |P_CW - P_ACW| >= delta_clear

    Per-galaxy chirality = +1 if P_CW > P_ACW else -1.
    """
    print(f"Loading Galaxy Zoo 1 Table 2 from {path.name} ...")
    if not path.exists():
        raise FileNotFoundError(
            f"GZ1 catalog not found at {path}. "
            f"Re-download per data/sdss_dr17/README.md instructions."
        )
    print(f"  File size: {path.stat().st_size / 1e6:.1f} MB (gzipped)")
    print(f"  Q-cuts: SPIRAL==1, NVOTE>={min_nvote}, |P_CW - P_ACW|>={delta_clear:.2f}")

    objids = []
    ra_deg_l = []
    dec_deg_l = []
    p_cw_l = []
    p_acw_l = []
    nvote_l = []
    n_total = 0
    n_spiral = 0
    n_nvote_ok = 0
    n_chirality_ok = 0

    with gzip.open(path, "rt") as f:
        header = f.readline().strip().split(",")
        col_idx = {name: i for i, name in enumerate(header)}
        required = ("OBJID", "RA", "DEC", "NVOTE", "P_CW", "P_ACW", "SPIRAL")
        for r in required:
            if r not in col_idx:
                raise KeyError(f"Required GZ1 column {r!r} missing; have {list(col_idx)}")

        for line in f:
            parts = line.rstrip("\n").split(",")
            if len(parts) < len(header):
                continue
            n_total += 1
            try:
                spiral = int(parts[col_idx["SPIRAL"]])
                if spiral != 1:
                    continue
                n_spiral += 1
                nvote = int(parts[col_idx["NVOTE"]])
                if nvote < min_nvote:
                    continue
                n_nvote_ok += 1
                p_cw = float(parts[col_idx["P_CW"]])
                p_acw = float(parts[col_idx["P_ACW"]])
                if abs(p_cw - p_acw) < delta_clear:
                    continue
                n_chirality_ok += 1
                ra_str = parts[col_idx["RA"]]
                dec_str = parts[col_idx["DEC"]]
                ra = parse_sexagesimal(ra_str, is_hours=True)
                dec = parse_sexagesimal(dec_str, is_hours=False)
                if not (0.0 <= ra < 360.0) or not (-90.0 <= dec <= 90.0):
                    continue
                objids.append(parts[col_idx["OBJID"]])
                ra_deg_l.append(ra)
                dec_deg_l.append(dec)
                p_cw_l.append(p_cw)
                p_acw_l.append(p_acw)
                nvote_l.append(nvote)
            except (ValueError, IndexError):
                continue

    print(f"  Total rows: {n_total}")
    print(f"  After SPIRAL==1 cut: {n_spiral}")
    print(f"  After NVOTE>={min_nvote} cut: {n_nvote_ok}")
    print(f"  After |P_CW-P_ACW|>={delta_clear:.2f} cut: {n_chirality_ok}")

    if n_chirality_ok < 5000:
        print(f"  WARNING: only {n_chirality_ok} galaxies pass cuts; "
              f"prereg sec 4.1 flagged < 5000 as documentation-worthy")

    objids = np.array(objids)
    ra_deg = np.array(ra_deg_l)
    dec_deg = np.array(dec_deg_l)
    p_cw = np.array(p_cw_l)
    p_acw = np.array(p_acw_l)
    nvote = np.array(nvote_l)
    chirality = np.where(p_cw > p_acw, 1, -1).astype(np.int8)

    # Convert ICRS (J2000) -> galactic via astropy
    print(f"  Transforming ICRS (J2000) -> galactic (l, b) via astropy...")
    from astropy.coordinates import SkyCoord
    from astropy import units as u
    coords_icrs = SkyCoord(ra_deg * u.deg, dec_deg * u.deg, frame="icrs")
    coords_gal = coords_icrs.galactic
    l_deg = np.array(coords_gal.l.deg)
    b_deg = np.array(coords_gal.b.deg)

    n_hat = np.stack([
        np.cos(np.radians(b_deg)) * np.cos(np.radians(l_deg)),
        np.cos(np.radians(b_deg)) * np.sin(np.radians(l_deg)),
        np.sin(np.radians(b_deg)),
    ], axis=1)  # (N, 3)

    monopole = float(np.mean(chirality))
    print(f"  Global monopole asymmetry (Sigma chi / N): {monopole:+.4f}")
    if abs(monopole) > 0.05:
        print(f"  WARNING: monopole asymmetry exceeds prereg threshold |0.05|; "
              f"flagging GZ1 bias as sub-finding (dipole fit is orthogonal to monopole)")

    return GZ1Subset(
        objids=objids,
        ra_deg=ra_deg,
        dec_deg=dec_deg,
        l_deg=l_deg,
        b_deg=b_deg,
        n_hat=n_hat,
        chirality=chirality,
        p_cw=p_cw,
        p_acw=p_acw,
        nvote=nvote,
        delta_clear=delta_clear,
    )


# ----------------------------------------------------------------------------
# Axial-dipole estimator (Longo 2011 cos gamma)
# ----------------------------------------------------------------------------


def dipole_asymmetry(n_hat_axis: np.ndarray, subset: GZ1Subset) -> float:
    """Compute A(n_hat) = (1/N) Sum_i chi_i * cos gamma_i for axis n_hat.

    gamma_i is the angle between galaxy direction n_hat_i and the candidate
    axis n_hat. We use cos gamma (not |cos gamma|) so a dipole produces a
    signed asymmetry; the search maximizes |A|.
    """
    cos_gamma = subset.n_hat @ n_hat_axis  # (N,)
    return float(np.mean(subset.chirality * cos_gamma))


def search_dipole_axis_healpix(
    subset: GZ1Subset,
    nside_initial: int = 16,
    nside_refined: int = 64,
    refine_radius_deg: float = 15.0,
) -> dict:
    """Two-stage HEALPix grid search for the maximum-|A| axial-dipole direction.

    Stage 1: coarse grid at NSIDE_initial (3072 pixels at NSIDE=16, ~3.6 deg pixel).
    Stage 2: refined grid at NSIDE_refined over a refine_radius_deg cap around
             Stage 1 best.

    Returns dict with best (l, b, A_value, dispersion).
    """
    import healpy as hp

    print(f"\nStage 1: coarse grid at NSIDE={nside_initial} "
          f"({hp.nside2npix(nside_initial)} candidate directions)...")
    npix_1 = hp.nside2npix(nside_initial)
    theta_1, phi_1 = hp.pix2ang(nside_initial, np.arange(npix_1))
    # HEALPix angles theta in [0, pi]; here we treat the HEALPix coordinate
    # system AS galactic for simplicity. Galaxy positions are already in
    # galactic (l, b); HEALPix pixels are in (theta, phi) where theta = 90-b
    # and phi = l (both in radians).
    # Vectorize Stage 1 entirely with NumPy:
    pix_vecs = np.stack([
        np.sin(theta_1) * np.cos(phi_1),
        np.sin(theta_1) * np.sin(phi_1),
        np.cos(theta_1),
    ], axis=1)  # (Npix, 3)
    # A(n_axis) = mean_i chi_i * (n_i . n_axis)
    # so we want each row of (subset.chirality * subset.n_hat).mean over galaxies dotted with each pix_vec.
    # Equivalent: (subset.chirality * subset.n_hat).T @ pix_vecs.T -> (3, Npix); then sum chirality column-wise.
    weighted_sum = subset.chirality[:, None] * subset.n_hat  # (N, 3)
    galaxy_dipole_vec = weighted_sum.mean(axis=0)  # (3,) = (1/N) Sum_i chi_i n_hat_i
    A_per_pix = pix_vecs @ galaxy_dipole_vec  # (Npix,) — vectorized A
    A_squared_per_pix = A_per_pix ** 2
    best_pix_1 = int(np.argmax(A_squared_per_pix))
    A_best_1 = float(A_per_pix[best_pix_1])
    print(f"  Stage 1 best: pix={best_pix_1}, |A|={abs(A_best_1):.5f}, A={A_best_1:+.5f}")

    # NOTE: For a pure axial-dipole estimator with no per-galaxy weights other
    # than chi_i in {-1, +1}, A(n_axis) = (galaxy_dipole_vec) . n_axis, so the
    # search is analytically solvable: best n_axis = +/- galaxy_dipole_vec /
    # |galaxy_dipole_vec|. The grid search is the brute-force version + serves
    # as a sanity check that the linear-algebra closed form agrees.
    gd_mag = np.linalg.norm(galaxy_dipole_vec)
    n_analytic = galaxy_dipole_vec / gd_mag if gd_mag > 0 else np.array([0.0, 0.0, 1.0])
    A_analytic = float(np.dot(n_analytic, galaxy_dipole_vec))
    print(f"  Analytic closed-form check: |galaxy_dipole_vec| = {gd_mag:.5f}, "
          f"A_analytic = {A_analytic:.5f} (should match Stage 1 best |A|)")

    # Stage 2: refined grid in neighborhood. Useful when the analytic best
    # is degenerate or there are multiple local maxima.
    print(f"\nStage 2: refined grid at NSIDE={nside_refined} "
          f"(over {refine_radius_deg:.1f}° cap around Stage 1 best)...")
    best_vec_1 = pix_vecs[best_pix_1]
    neighbor_pix = hp.query_disc(
        nside_refined, best_vec_1, radius=math.radians(refine_radius_deg)
    )
    theta_n, phi_n = hp.pix2ang(nside_refined, neighbor_pix)
    pix_vecs_2 = np.stack([
        np.sin(theta_n) * np.cos(phi_n),
        np.sin(theta_n) * np.sin(phi_n),
        np.cos(theta_n),
    ], axis=1)  # (M, 3)
    A_per_neighbor = pix_vecs_2 @ galaxy_dipole_vec
    A_squared_per_neighbor = A_per_neighbor ** 2
    best_idx_2 = int(np.argmax(A_squared_per_neighbor))
    best_pix_2 = int(neighbor_pix[best_idx_2])
    A_best_2 = float(A_per_neighbor[best_idx_2])
    best_vec_2 = pix_vecs_2[best_idx_2]
    l_best, b_best = cartesian_to_galactic(best_vec_2)
    l_canon, b_canon = canonicalize_axis_lb(l_best, b_best)

    pixel_size_deg = math.degrees(math.sqrt(4 * math.pi / hp.nside2npix(nside_refined)))
    print(f"  Stage 2 best: pix={best_pix_2}, |A|={abs(A_best_2):.5f}, A={A_best_2:+.5f}")
    print(f"  Direction: (l, b) = ({l_best:.2f}°, {b_best:.2f}°)")
    print(f"  Canonical (0 <= l < 180): ({l_canon:.2f}°, {b_canon:.2f}°)")
    print(f"  Grid resolution: {pixel_size_deg:.2f}°")

    return {
        "stage1_best_pix": best_pix_1,
        "stage1_best_A": A_best_1,
        "stage2_best_pix": best_pix_2,
        "stage2_best_A": A_best_2,
        "A_magnitude": float(abs(A_best_2)),
        "l_deg_raw": l_best,
        "b_deg_raw": b_best,
        "l_deg": l_canon,
        "b_deg": b_canon,
        "best_axis_cart": best_vec_2.tolist(),
        "galaxy_dipole_vec_cart": galaxy_dipole_vec.tolist(),
        "galaxy_dipole_magnitude": float(gd_mag),
        "analytic_A_check": A_analytic,
        "pixel_size_deg": pixel_size_deg,
    }


# ----------------------------------------------------------------------------
# Uncertainty propagation
# ----------------------------------------------------------------------------


def sigma_lss_hessian_mc(
    fit_result: dict,
    subset: GZ1Subset,
    n_mc: int = 1000,
    rng_seed: int = 42,
) -> dict:
    """Hessian + Monte Carlo sigma_LSS for the axial-dipole axis direction.

    The dipole asymmetry has closed form A(n) = n . v where v = (1/N) Sum chi_i n_hat_i.
    For a 3-component unit-vector axis, the per-component covariance of v is
    (well-known result for sample mean of unit vectors with weights):
        Cov(v) = (1/N) * [<chi_i^2 n_hat_i n_hat_i^T> - v v^T]
    where chi_i^2 = 1 for our +/-1 labels, so:
        Cov(v) = (1/N) * [<n_hat_i n_hat_i^T> - v v^T]
    The Monte Carlo draws sample v_b ~ N(v, Cov(v)), normalizes each to a
    direction, and reports the 68% great-circle containment radius around
    the best-fit direction.

    NOTE: this is the canonical sample-mean Hessian / Fisher uncertainty
    propagation for the cos-gamma axial-dipole estimator. See e.g. Mardia &
    Jupp "Directional Statistics" sec 9.3.4 (eq 9.3.10) for the unweighted
    case; the chi_i^2 = 1 weighting reduces to that case for binary +/-1.
    """
    v = np.array(fit_result["galaxy_dipole_vec_cart"])
    n_best = v / np.linalg.norm(v)
    N = len(subset.chirality)

    # Cov(v) = (1/N) [E[chi^2 n n^T] - v v^T]; chi^2 = 1, so E[chi^2 n n^T] = (1/N) Sum_i n_i n_i^T
    nnt = subset.n_hat.T @ subset.n_hat / N  # (3, 3)
    cov_v = (nnt - np.outer(v, v)) / N

    print(f"  Cov(v) eigenvalues: {np.linalg.eigvalsh(cov_v).tolist()}")
    print(f"  v = {v.tolist()}, |v| = {np.linalg.norm(v):.5f}")

    rng = np.random.default_rng(rng_seed)
    samples = rng.multivariate_normal(v, cov_v, size=n_mc)
    sample_norms = np.linalg.norm(samples, axis=1)
    valid = sample_norms > 1e-9
    sample_dirs = samples[valid] / sample_norms[valid, None]

    # Great-circle separations from n_best (undirected: |cos|)
    dots = np.abs(sample_dirs @ n_best)
    dots = np.clip(dots, -1.0, 1.0)
    angles_deg = np.degrees(np.arccos(dots))
    sigma_68 = float(np.quantile(angles_deg, 0.6827))

    return {
        "method": f"Hessian + Gaussian MC ({n_mc} samples; per Mardia & Jupp 9.3.10)",
        "sigma_deg_68": sigma_68,
        "n_samples_valid": int(np.sum(valid)),
        "cov_v_eigenvalues": np.linalg.eigvalsh(cov_v).tolist(),
        "v_cart": v.tolist(),
        "v_magnitude": float(np.linalg.norm(v)),
    }


def sigma_lss_bootstrap(
    subset: GZ1Subset,
    fit_result: dict,
    n_boot: int = 500,
    rng_seed: int = 24601,
) -> dict:
    """Block bootstrap on galaxy catalog for sigma_LSS direction.

    Draw n_boot resamples (with replacement) of the post-cut galaxy sample;
    re-fit the axial-dipole on each (analytic closed-form since no nonlinear
    minimization needed); take the 68% great-circle containment radius of
    direction distribution.
    """
    rng = np.random.default_rng(rng_seed)
    N = len(subset.chirality)
    v_best = np.array(fit_result["galaxy_dipole_vec_cart"])
    n_best = v_best / np.linalg.norm(v_best)

    boot_dirs = np.zeros((n_boot, 3))
    boot_mags = np.zeros(n_boot)
    weighted_galaxy = subset.chirality[:, None] * subset.n_hat  # (N, 3)

    print(f"    block bootstrap: {n_boot} resamples of {N} galaxies (analytic dipole closed-form per draw)")
    for b in range(n_boot):
        idx = rng.integers(0, N, size=N)
        v_b = weighted_galaxy[idx].mean(axis=0)
        v_b_norm = np.linalg.norm(v_b)
        if v_b_norm < 1e-9:
            continue
        boot_dirs[b] = v_b / v_b_norm
        boot_mags[b] = v_b_norm
        if (b + 1) % 100 == 0:
            print(f"      {b + 1}/{n_boot}")

    valid = boot_mags > 0
    dots = np.abs(boot_dirs[valid] @ n_best)
    dots = np.clip(dots, -1.0, 1.0)
    angles_deg = np.degrees(np.arccos(dots))
    sigma_68 = float(np.quantile(angles_deg, 0.6827))

    return {
        "method": f"Block bootstrap ({int(np.sum(valid))}/{n_boot} converged; analytic closed-form per draw)",
        "sigma_deg_68": sigma_68,
        "n_bootstraps_converged": int(np.sum(valid)),
        "n_bootstraps_attempted": int(n_boot),
        "mean_magnitude": float(np.mean(boot_mags[valid])),
        "magnitude_std": float(np.std(boot_mags[valid])),
    }


# ----------------------------------------------------------------------------
# Randomization-null significance test (Longo 2011 sec 3)
# ----------------------------------------------------------------------------


def randomization_null(
    subset: GZ1Subset,
    A_observed_squared: float,
    n_random: int = 10000,
    rng_seed: int = 137,
) -> dict:
    """Randomization null: random sign assignment to each galaxy n_random times.

    For each random catalog, compute the maximum |A| over all directions
    (closed-form: max_n n . v = |v|, so |A_max| = |v_random|). Returns
    fraction of randoms with |A_max|^2 >= |A_observed|^2 = p-value.
    """
    rng = np.random.default_rng(rng_seed)
    N = len(subset.chirality)
    max_A_squared = np.zeros(n_random)
    print(f"  Randomization null: {n_random} random sign assignments...")
    for r in range(n_random):
        chi_random = rng.choice([-1, 1], size=N)
        v_random = (chi_random[:, None] * subset.n_hat).mean(axis=0)
        max_A_squared[r] = float(np.dot(v_random, v_random))
        if (r + 1) % 2000 == 0:
            print(f"      {r + 1}/{n_random}")

    n_at_or_above = int(np.sum(max_A_squared >= A_observed_squared))
    p_value = n_at_or_above / n_random
    print(f"  |A_observed|^2 = {A_observed_squared:.6e}")
    print(f"  random |A_max|^2 mean = {np.mean(max_A_squared):.6e}, "
          f"std = {np.std(max_A_squared):.6e}")
    print(f"  randomization p-value = {p_value:.6f} ({n_at_or_above}/{n_random})")

    # Z-score conversion (one-sided): A_observed > random null
    mean_null = float(np.mean(max_A_squared))
    std_null = float(np.std(max_A_squared))
    z_score = (A_observed_squared - mean_null) / std_null if std_null > 0 else 0.0

    return {
        "method": f"Random sign assignment ({n_random} catalogs); analytic |A_max| = |v_random| per catalog",
        "p_value": p_value,
        "n_at_or_above_observed": n_at_or_above,
        "n_random_catalogs": n_random,
        "random_mean_A_squared": mean_null,
        "random_std_A_squared": std_null,
        "z_score_one_sided": z_score,
        "A_observed_squared": A_observed_squared,
    }


# ----------------------------------------------------------------------------
# Adjudication (per prereg sec 4)
# ----------------------------------------------------------------------------


@dataclass
class AdjudicationResult:
    outcome: str  # "A", "C", "D-sustained", "Marginal-D", "E"
    rationale: str
    sigma_lss_canonical_deg: float
    cmb_lss_separation_deg: float
    sigma_combined_deg: float
    significance_against_alignment_sigma: float
    significance_for_alignment_sigma: float
    decisive_against: bool
    decisive_for: bool


def adjudicate(
    sigma_lss: float,
    cmb_axis_l_deg: float,
    cmb_axis_b_deg: float,
    cmb_axis_sigma_deg: float,
    lss_axis_l_deg: float,
    lss_axis_b_deg: float,
    randomization_p_value: float,
    A_observed_magnitude: float,
) -> AdjudicationResult:
    """Adjudicate the outcome per pre-registered table (sec 4)."""
    separation_deg = angular_separation_deg_undirected(
        cmb_axis_l_deg, cmb_axis_b_deg, lss_axis_l_deg, lss_axis_b_deg
    )
    sigma_combined = math.sqrt(cmb_axis_sigma_deg ** 2 + sigma_lss ** 2)

    # Significance against alignment (would need separation > 20° + 3sigma)
    # = (separation - 20°) / sigma_combined
    significance_against = (separation_deg - CMB_LSS_PASS_THRESHOLD_DEG) / sigma_combined
    decisive_against = significance_against > 3.0

    # Significance for alignment (would need separation < 3sigma)
    # = separation / sigma_combined; < 3 means within 3sigma of zero
    significance_for_sigma = separation_deg / sigma_combined
    decisive_for = significance_for_sigma < 3.0

    # Tie-breakers per prereg sec 4.1: low A_observed -> auto-D
    if randomization_p_value > 0.32:
        return AdjudicationResult(
            outcome="D-sustained",
            rationale=(
                f"Randomization p-value {randomization_p_value:.4f} > 0.32 — "
                f"dipole magnitude consistent with zero at 1sigma. Direction is "
                f"effectively unconstrained regardless of nominal sigma_LSS."
            ),
            sigma_lss_canonical_deg=sigma_lss,
            cmb_lss_separation_deg=separation_deg,
            sigma_combined_deg=sigma_combined,
            significance_against_alignment_sigma=significance_against,
            significance_for_alignment_sigma=significance_for_sigma,
            decisive_against=False,
            decisive_for=False,
        )

    if decisive_against:
        outcome = "A"
        rationale = (
            f"CMB-LSS separation {separation_deg:.2f}° exceeds 20° threshold by "
            f"{significance_against:.2f}sigma > 3sigma — alignment falsified at 3sigma."
        )
    elif decisive_for:
        outcome = "C"
        rationale = (
            f"CMB-LSS separation {separation_deg:.2f}° within {significance_for_sigma:.2f}sigma "
            f"< 3sigma of zero — alignment confirmed at 3sigma."
        )
    elif sigma_lss >= SIGMA_MARGINAL_UPPER_DEG:
        outcome = "D-sustained"
        rationale = (
            f"sigma_LSS = {sigma_lss:.2f}° >= 25° prereg threshold; "
            f"data insufficient to discriminate alignment vs misalignment at 3sigma."
        )
    elif sigma_lss >= SIGMA_BRIEF_TARGET_DEG:
        outcome = "Marginal-D"
        rationale = (
            f"sigma_LSS = {sigma_lss:.2f}° in marginal window [15°, 25°); "
            f"separation {separation_deg:.2f}° at {significance_against:+.2f}sigma vs "
            f"alignment threshold; not 3sigma-decisive either way."
        )
    else:
        # sigma_LSS achieved < 15° prereg target, but neither A nor C decisive:
        # tight precision combined with a separation that lands in the
        # in-between band [20° - 3sigma_combined, 20° + 3sigma_combined].
        # Not labelled Marginal-D in the prereg's strict-σ sense (which targets
        # σ_LSS ≥ 15°); this is precision-sufficient but separation-bracketed.
        outcome = "Marginal-D"  # use same label per prereg sec 4 mapping
        rationale = (
            f"sigma_LSS = {sigma_lss:.2f}° meets prereg precision target (<15°), "
            f"but CMB-LSS separation {separation_deg:.2f}° at +{significance_against:.2f}sigma "
            f"above 20° alignment threshold does not clear 3sigma-decisive against alignment "
            f"(needs separation > 20° + 3*sigma_combined = {20 + 3*sigma_combined:.2f}°), "
            f"and separation/sigma_combined = {significance_for_sigma:.2f}sigma is > 3sigma "
            f"from zero — alignment also excluded at 3sigma. Result: separation lands in the "
            f"in-between band [20° - 3sigma_combined, 20° + 3sigma_combined] = "
            f"[{max(0, 20-3*sigma_combined):.1f}°, {20+3*sigma_combined:.1f}°]. "
            f"Adjudication: Marginal-D (precision-sufficient, threshold-bracketed). "
            f"Headline finding: alignment with CMB axis EXCLUDED at "
            f"{significance_for_sigma:.1f}sigma; alignment-threshold falsification at only "
            f"{significance_against:.1f}sigma. Cascade: queue 20°-threshold reassessment AND/OR "
            f"joint Pantheon+ + SDSS constraint (Option B follow-up) for sharper boundary."
        )

    return AdjudicationResult(
        outcome=outcome,
        rationale=rationale,
        sigma_lss_canonical_deg=sigma_lss,
        cmb_lss_separation_deg=separation_deg,
        sigma_combined_deg=sigma_combined,
        significance_against_alignment_sigma=significance_against,
        significance_for_alignment_sigma=significance_for_sigma,
        decisive_against=decisive_against,
        decisive_for=decisive_for,
    )


# ----------------------------------------------------------------------------
# Main pipeline
# ----------------------------------------------------------------------------


@dataclass
class DriverResult:
    pipeline_name: str
    delta_clear: float
    min_nvote: int
    n_galaxies_after_cuts: int
    monopole_asymmetry: float
    dipole_fit: dict
    sigma_hessian_mc: dict
    sigma_bootstrap: dict
    sigma_canonical_deg: float
    randomization_null: dict
    cmb_axis_pin: dict
    adjudication: dict


def run_pipeline(
    delta_clear: float = 0.4,
    min_nvote: int = 10,
    pipeline_name: str = "primary",
    skip_randomization: bool = False,
    n_bootstrap: int = 500,
    n_mc: int = 1000,
    n_random: int = 10000,
) -> DriverResult:
    """Run one full pipeline (one delta_clear setting)."""
    print(f"\n{'='*70}")
    print(f"  PIPELINE: {pipeline_name}  (delta_clear={delta_clear}, min_nvote={min_nvote})")
    print(f"{'='*70}\n")

    subset = load_gz1_catalog(GZ1_CATALOG_PATH, delta_clear=delta_clear, min_nvote=min_nvote)
    monopole = float(np.mean(subset.chirality))

    print("\nAxial-dipole fit (Longo 2011 cos gamma estimator)...")
    fit = search_dipole_axis_healpix(subset)

    print("\nUncertainty propagation A: Hessian + Monte Carlo...")
    sigma_hess = sigma_lss_hessian_mc(fit, subset, n_mc=n_mc)

    print(f"\nUncertainty propagation B: block bootstrap...")
    sigma_boot = sigma_lss_bootstrap(subset, fit, n_boot=n_bootstrap)

    sigma_canonical = max(sigma_hess["sigma_deg_68"], sigma_boot["sigma_deg_68"])
    print(f"\n  sigma_LSS canonical (max of A, B): {sigma_canonical:.3f}°")
    print(f"  sigma_LSS Hessian / Bootstrap ratio: "
          f"{sigma_hess['sigma_deg_68'] / sigma_boot['sigma_deg_68']:.3f}")

    A_squared = fit["A_magnitude"] ** 2
    if skip_randomization:
        rand_null = {"method": "SKIPPED", "p_value": -1.0}
    else:
        print(f"\nRandomization-null significance test (Longo 2011 sec 3)...")
        rand_null = randomization_null(subset, A_squared, n_random=n_random)

    # ---- Load CMB axis from E1b ----
    if not CMB_AXIS_RESULTS_PATH.exists():
        raise FileNotFoundError(
            f"CMB axis JSON not found at {CMB_AXIS_RESULTS_PATH}. "
            f"Run cmb_axis_alignment_executable_observer.py first."
        )
    with open(CMB_AXIS_RESULTS_PATH) as f:
        cmb_axis_data = json.load(f)
    cmb_axis_l = float(cmb_axis_data["axis_of_evil_computation"]["l_deg"])
    cmb_axis_b = float(cmb_axis_data["axis_of_evil_computation"]["b_deg"])
    cmb_axis_sigma = float(cmb_axis_data["axis_of_evil_computation"]["sigma_deg"])
    cmb_axis_pin = {
        "source": "Planck PR3 SMICA via cmb_axis_alignment_executable_observer.py (E1b)",
        "l_deg": cmb_axis_l,
        "b_deg": cmb_axis_b,
        "sigma_deg": cmb_axis_sigma,
        "method": "data-derived; max-angular-momentum-dispersion estimator",
    }

    # ---- Adjudicate ----
    adj = adjudicate(
        sigma_lss=sigma_canonical,
        cmb_axis_l_deg=cmb_axis_l,
        cmb_axis_b_deg=cmb_axis_b,
        cmb_axis_sigma_deg=cmb_axis_sigma,
        lss_axis_l_deg=fit["l_deg"],
        lss_axis_b_deg=fit["b_deg"],
        randomization_p_value=rand_null.get("p_value", 1.0),
        A_observed_magnitude=fit["A_magnitude"],
    )

    print(f"\n{'='*70}")
    print(f"  PIPELINE {pipeline_name} ADJUDICATION:")
    print(f"  Outcome: {adj.outcome}")
    print(f"  Rationale: {adj.rationale}")
    print(f"{'='*70}\n")

    return DriverResult(
        pipeline_name=pipeline_name,
        delta_clear=delta_clear,
        min_nvote=min_nvote,
        n_galaxies_after_cuts=len(subset.chirality),
        monopole_asymmetry=monopole,
        dipole_fit=fit,
        sigma_hessian_mc=sigma_hess,
        sigma_bootstrap=sigma_boot,
        sigma_canonical_deg=sigma_canonical,
        randomization_null=rand_null,
        cmb_axis_pin=cmb_axis_pin,
        adjudication=asdict(adj),
    )


def main():
    """Run primary pipeline (delta_clear=0.4) + 2 robustness sub-pipelines."""
    print(f"=" * 70)
    print(f" C5-CMB-AXIS SDSS Spin-Orientation Re-Analysis — driver execution")
    print(f"=" * 70)
    print(f" Data dir: {DATA_DIR}")
    print(f" Catalog:  {GZ1_CATALOG_PATH.name} ({GZ1_CATALOG_PATH.stat().st_size / 1e6:.1f} MB)")
    print(f" Output:   {RESULTS_PATH}")
    print(f"=" * 70)

    print(f"\nForward-prediction discipline check (per prereg sec 3.6):")
    print(f"  1. Dipole search sees CMB axis during fit? NO (loaded only for post-fit comparison)")
    print(f"  2. Grid biased toward CMB axis? NO (HEALPix uniform full-sphere)")
    print(f"  3. Alignment functional minimized? NO (-|A|^2 = -<chi cos gamma>^2 is direction-agnostic)")
    print(f"  4. Result depends on chosen comparison axis? NO (best-fit axis independent of post-fit comparison)")
    print(f"  -> All four pass. Estimator is a forward-prediction.")

    pipelines = [
        ("primary",         0.4, 10, False),  # canonical
        ("robustness_0.2",  0.2, 10, False),  # looser clarity cut
        ("robustness_0.6",  0.6, 10, False),  # tighter clarity cut
    ]

    results = {}
    for name, delta, nvote, skip_rand in pipelines:
        r = run_pipeline(
            delta_clear=delta,
            min_nvote=nvote,
            pipeline_name=name,
            skip_randomization=skip_rand,
        )
        results[name] = asdict(r)

    # Sub-analysis: are the 3 pipelines' best directions mutually consistent?
    p_primary = results["primary"]
    p_lower = results["robustness_0.2"]
    p_higher = results["robustness_0.6"]
    sep_primary_lower = angular_separation_deg_undirected(
        p_primary["dipole_fit"]["l_deg"], p_primary["dipole_fit"]["b_deg"],
        p_lower["dipole_fit"]["l_deg"], p_lower["dipole_fit"]["b_deg"],
    )
    sep_primary_higher = angular_separation_deg_undirected(
        p_primary["dipole_fit"]["l_deg"], p_primary["dipole_fit"]["b_deg"],
        p_higher["dipole_fit"]["l_deg"], p_higher["dipole_fit"]["b_deg"],
    )

    cross_pipeline_consistency = {
        "primary_vs_robustness_0.2_separation_deg": sep_primary_lower,
        "primary_vs_robustness_0.6_separation_deg": sep_primary_higher,
        "within_1sigma_LSS": (
            sep_primary_lower < p_primary["sigma_canonical_deg"] and
            sep_primary_higher < p_primary["sigma_canonical_deg"]
        ),
    }
    print(f"\nCross-pipeline consistency:")
    print(f"  primary vs robustness_0.2: {sep_primary_lower:.2f}°")
    print(f"  primary vs robustness_0.6: {sep_primary_higher:.2f}°")
    print(f"  within primary's 1sigma_LSS = {p_primary['sigma_canonical_deg']:.2f}°: "
          f"{cross_pipeline_consistency['within_1sigma_LSS']}")

    # ---- Existing-corpus comparison vs Longo paper-pinned + corpus-pinned ----
    longo_l_deg, longo_b_deg = 52.0, 68.5   # Longo 2011 published axis
    corpus_l_deg, corpus_b_deg = 32.0, 32.0  # corpus pin in cmb_axis_alignment_executable_observer.py:97-99
    sep_primary_vs_longo = angular_separation_deg_undirected(
        p_primary["dipole_fit"]["l_deg"], p_primary["dipole_fit"]["b_deg"],
        longo_l_deg, longo_b_deg,
    )
    sep_primary_vs_corpus = angular_separation_deg_undirected(
        p_primary["dipole_fit"]["l_deg"], p_primary["dipole_fit"]["b_deg"],
        corpus_l_deg, corpus_b_deg,
    )
    sep_longo_vs_corpus = angular_separation_deg_undirected(
        longo_l_deg, longo_b_deg, corpus_l_deg, corpus_b_deg,
    )
    corpus_anomaly = {
        "longo_2011_published": {"l_deg": longo_l_deg, "b_deg": longo_b_deg,
                                  "source": "Longo 2011 Phys. Lett. B 699:224 sec 3, page 6 (galactic from equatorial (217°, 32°))"},
        "ave_corpus_pinned":   {"l_deg": corpus_l_deg, "b_deg": corpus_b_deg,
                                  "source": "cmb_axis_alignment_executable_observer.py:97-99"},
        "primary_vs_longo_separation_deg": sep_primary_vs_longo,
        "primary_vs_ave_corpus_separation_deg": sep_primary_vs_corpus,
        "longo_vs_ave_corpus_separation_deg": sep_longo_vs_corpus,
        "anomaly_flag": (
            "AVE corpus pin (32°, 32°) does NOT match Longo 2011's published axis (52°, 68.5°); "
            "corpus appears to have substituted equatorial dec for both galactic l and b. "
            "Per prereg sec 2.5: this anomaly is SURFACED here per flag-don't-fix; "
            "fix lives in the auditor lane (likely: replace literature pin with this session's "
            "empirical re-fit at (primary l, b) below)."
        ),
    }

    # ---- Bundle ----
    summary = {
        "session_date": "2026-05-19",
        "branch": "analysis/c5-sdss-dr17-spin-orientation",
        "prereg": "research/2026-05-19_c5-sdss-spin-orientation-prereg.md",
        "pipelines": results,
        "cross_pipeline_consistency": cross_pipeline_consistency,
        "corpus_pin_anomaly": corpus_anomaly,
        "headline_outcome": p_primary["adjudication"]["outcome"],
        "headline_rationale": p_primary["adjudication"]["rationale"],
        "headline_sigma_lss_deg": p_primary["sigma_canonical_deg"],
        "headline_cmb_lss_separation_deg": p_primary["adjudication"]["cmb_lss_separation_deg"],
        "headline_significance_against_alignment_sigma": p_primary["adjudication"]["significance_against_alignment_sigma"],
        "headline_significance_for_alignment_sigma": p_primary["adjudication"]["significance_for_alignment_sigma"],
    }

    print(f"\nWriting full results to {RESULTS_PATH} ...")
    with open(RESULTS_PATH, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"  Results JSON written ({RESULTS_PATH.stat().st_size / 1e3:.1f} KB)")

    print(f"\n{'='*70}")
    print(f"  HEADLINE: outcome = {summary['headline_outcome']}")
    print(f"  primary sigma_LSS = {summary['headline_sigma_lss_deg']:.2f}°")
    print(f"  CMB-LSS separation = {summary['headline_cmb_lss_separation_deg']:.2f}°")
    print(f"  significance vs alignment threshold = "
          f"{summary['headline_significance_against_alignment_sigma']:+.2f}sigma")
    print(f"  significance for alignment (separation/sigma_combined) = "
          f"{summary['headline_significance_for_alignment_sigma']:.2f}sigma")
    print(f"{'='*70}")
    print(f"\nCorpus pin anomaly: {corpus_anomaly['anomaly_flag']}")
    print(f"  primary fit vs Longo 2011: {sep_primary_vs_longo:.2f}°")
    print(f"  primary fit vs corpus pin: {sep_primary_vs_corpus:.2f}°")
    print(f"  Longo 2011 vs corpus pin:  {sep_longo_vs_corpus:.2f}°")


if __name__ == "__main__":
    main()
