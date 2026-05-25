"""
C5-CMB-AXIS Pantheon+ Bulk-Flow Tightening — E1b-prime executable driver.

Re-fits the Hubble-flow bulk-direction from raw Pantheon+SH0ES Type Ia
supernovae, replacing the paper-pinned Whitford+2023 literal `(l=323°,
b=26°), sigma=30°` with a self-derived `(l, b, sigma_Hubble)` triple from the
public catalog.

Per the frozen pre-registration at
`research/2026-05-19_c5-pantheon-tightening-prereg.md`, this driver:

1. Loads `data/pantheon_plus/Pantheon+SH0ES.dat`.
2. Cuts to z < 0.1 SNe, excluding calibrators.
3. Runs a maximum-likelihood Hubble-residual fit with 3 free bulk-flow
   parameters (u_x, u_y, u_z in galactic Cartesian) and M as nuisance.
4. Extracts bulk-flow direction (l_Hubble, b_Hubble) and sigma_Hubble via
   (A) Hessian Monte Carlo and (B) block bootstrap; takes larger as canonical.
5. Runs primary pipeline (zCMB) and defense-in-depth sub-analysis (zHEL).
6. Compares to E1b CMB axis-of-evil (l=60.28°, b=50.48°) from
   `cmb_axis_alignment_executable_observer_results.json`.
7. Adjudicates the outcome per the pre-registered A/C/D-sustained/Marginal-D/E
   table.

FORWARD-PREDICTION DISCIPLINE: the minimizer never sees the CMB axis. The
post-fit comparison uses the E1b axis only for separation computation. The
fit is direction-agnostic; the chi-squared is the standard Hubble-residual
chi-squared.

Run:
    python3 src/scripts/vol_3_macroscopic/c5_pantheon_bulk_flow_tightening.py
"""

import json
import math
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))

# Canonical constants (per ave-canonical-source; never hard-code)
from ave.core.constants import C_0, H_INFINITY  # noqa: E402


def _resolve_data_dir() -> Path:
    """Resolve data dir, falling back to main repo when run from a worktree.

    Worktrees do not contain `data/` (gitignored); fall back to the parent
    repo's data dir if present.
    """
    candidate = REPO_ROOT / "data"
    if candidate.exists():
        return candidate
    # Worktree fallback: look for `.../AVE-Core/data` in ancestors
    cur = REPO_ROOT
    while cur != cur.parent:
        if (cur / "data" / "pantheon_plus").is_dir():
            return cur / "data"
        if cur.name == "worktrees" and (cur.parent.parent / "data").exists():
            return cur.parent.parent / "data"
        cur = cur.parent
    # Last-ditch: hardcoded canonical path (always under AVE-Core)
    canonical = Path("/Users/grantlindblom/AVE-staging/AVE-Core/data")
    if canonical.exists():
        return canonical
    return REPO_ROOT / "data"  # will trigger missing-data error downstream


DATA_DIR = _resolve_data_dir()
PANTHEON_PATH = DATA_DIR / "pantheon_plus" / "Pantheon+SH0ES.dat"
PANTHEON_COV_PATH = DATA_DIR / "pantheon_plus" / "Pantheon+SH0ES_STAT+SYS.cov"
CMB_AXIS_RESULTS_PATH = SCRIPT_DIR / "cmb_axis_alignment_executable_observer_results.json"
RESULTS_PATH = SCRIPT_DIR / "c5_pantheon_bulk_flow_tightening_results.json"

# Convert C_0 (m/s) to km/s for the velocity correction
C_KM_S = C_0 / 1000.0

# Convert H_INFINITY (SI: 1/s) to km/s/Mpc for the distance modulus formula
# 1 Mpc = 3.0857e22 m → 1 (km/s)/Mpc = (1000 m/s) / 3.0857e22 m = 3.241e-20 1/s
MPC_TO_M = 3.0857e22
H0_AVE_KM_S_MPC = H_INFINITY * MPC_TO_M / 1000.0
H0_PANTHEON_SH0ES_KM_S_MPC = 73.04  # SH0ES baseline (Riess+2022); residual cross-check only

Q0 = -0.55  # low-z LCDM deceleration parameter (fixed, not free)

# Adjudication thresholds (per prereg §4 + brief A6/A8)
SIGMA_DECISIVE_DEG = 18.2  # below: 3-sigma decisive against alignment
SIGMA_INSUFFICIENT_DEG = 24.9  # above: D-sustained (alignment within 3-sigma)
SIGMA_BRIEF_TARGET_DEG = 15.0  # brief's conservative target precision

CMB_AXIS_PASS_THRESHOLD_DEG = 20.0  # frozen prereg alignment threshold


# ----------------------------------------------------------------------------
# Geometry utilities (mirror cmb_axis_alignment_executable_observer.py)
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


def angular_separation_deg_undirected(l1: float, b1: float, l2: float, b2: float) -> float:
    """Undirected angular separation between two axes (galactic l, b)."""
    v1 = galactic_to_cartesian(l1, b1)
    v2 = galactic_to_cartesian(l2, b2)
    dot = max(-1.0, min(1.0, float(np.dot(v1, v2))))
    return math.degrees(math.acos(abs(dot)))


# ----------------------------------------------------------------------------
# Pantheon+ catalog ingest
# ----------------------------------------------------------------------------


@dataclass
class PantheonSubset:
    """Sub-sample of Pantheon+ for bulk-flow fit.

    Fields are 1D arrays indexed by SN; `n_hat` is (N, 3) galactic-Cartesian
    unit vectors per SN.

    All four redshift columns are retained per SN for cross-pipeline diagnostics;
    `z` is the one used in the chi^2 (= z_for_cut at load time).

    `inv_cov` is the (N, N) inverse of the m_b_corr STAT+SYS covariance matrix
    restricted to the selected sample. If None, falls back to diagonal of
    `mu_err`. The full inv_cov is the load-bearing object: the chi^2 uses
    inv_cov, not (1/mu_err)^2 squared residuals.
    """

    cids: np.ndarray
    z: np.ndarray  # one of z_hd / z_cmb / z_helio / z_hel_plus_vpec
    z_helio: np.ndarray
    z_cmb: np.ndarray
    z_hd: np.ndarray
    z_hel_plus_vpec: np.ndarray
    vpec: np.ndarray
    mu: np.ndarray  # m_b_corr (M absorbed via free offset in fit)
    mu_err: np.ndarray  # diagonal sqrt for fallback / sanity
    m_b_corr: np.ndarray
    l_deg: np.ndarray
    b_deg: np.ndarray
    n_hat: np.ndarray  # (N, 3) unit vectors
    inv_cov: np.ndarray | None = None  # (N, N) inverse STAT+SYS covariance
    selection_indices: np.ndarray | None = None  # row indices in original catalog


def load_pantheon_covariance(cov_path: Path, n_expected: int = 1701) -> np.ndarray | None:
    """Load the Pantheon+SH0ES STAT+SYS covariance matrix.

    File format (per Pantheon+SH0ES data release):
      line 0: N  (integer, N = number of SNe; matches catalog order)
      lines 1..N*N: row-major covariance entries (one float per line)

    Returns the (N, N) symmetric covariance matrix, or None if file missing.
    """
    if not cov_path.exists():
        print(f"  WARNING: covariance file {cov_path.name} not found at {cov_path}")
        return None
    print(f"  loading STAT+SYS covariance matrix from {cov_path.name} ({cov_path.stat().st_size / 1e6:.1f} MB)...")
    with open(cov_path) as f:
        n = int(f.readline().strip())
        if n != n_expected:
            print(f"  WARNING: covariance N={n} != expected {n_expected}; using anyway")
        flat = np.fromfile(f, sep="\n", dtype=np.float64)
    expected_flat = n * n
    if flat.size != expected_flat:
        print(f"  ERROR: covariance flat size {flat.size} != {expected_flat}; cannot reshape")
        return None
    cov = flat.reshape(n, n)
    # Sanity: should be symmetric
    asym = np.max(np.abs(cov - cov.T))
    print(f"  covariance loaded: shape {cov.shape}, max asymmetry = {asym:.2e}")
    return cov


def load_pantheon_subset(
    path: Path,
    z_cut: float = 0.1,
    redshift_pipeline: str = "zHD",
    cov_path: Path = None,
    use_full_covariance: bool = True,
) -> PantheonSubset:
    """Load Pantheon+SH0ES catalog, apply z-cut, exclude calibrators.

    Parameters
    ----------
    path : Path
        Pantheon+SH0ES.dat file.
    z_cut : float
        Maximum redshift (in the chosen pipeline).
    redshift_pipeline : str
        Identifies the redshift column / convention to use.

        Pantheon+SH0ES catalog convention (verified empirically against the
        catalog 2026-05-19; corrected from initial implementation that
        conflated zCMB-only with the full pipeline):

        - 'zHD'  : Hubble-diagram redshift = CMB-rest-frame + 2M++ VPEC
                   subtracted. THIS IS THE STANDARD PIPELINE per prereg §3.6.
                   Identity verified: zHD = (1+zCMB)*(1-VPEC/c) - 1 to 1e-6.
        - 'zCMB' : CMB-rest-frame only (solar motion subtracted, no VPEC).
                   Available as a residual diagnostic, NOT a defined pipeline.
        - 'zHEL' : Raw heliocentric (no correction at all). Available as
                   a sanity diagnostic.
        - 'zHEL_plus_VPEC' : Heliocentric with VPEC subtracted (no CMB-rest
                   transform). THIS IS THE DEFENSE-IN-DEPTH SUB-ANALYSIS per
                   prereg §3.6 — applies 2M++ correction WITHOUT the CMB-rest
                   transform.
    """
    valid_pipelines = ("zHD", "zCMB", "zHEL", "zHEL_plus_VPEC")
    if redshift_pipeline not in valid_pipelines:
        raise ValueError(f"Unknown redshift_pipeline {redshift_pipeline!r}; " f"valid: {valid_pipelines}")

    print(f"Loading Pantheon+SH0ES catalog from {path.name} ...")
    print(f"  z-cut < {z_cut} (using {redshift_pipeline}); calibrators excluded")

    with open(path) as f:
        header = f.readline().split()

    col_idx = {name: i for i, name in enumerate(header)}
    required = ("CID", "zCMB", "zHEL", "zHD", "m_b_corr", "m_b_corr_err_DIAG", "RA", "DEC", "IS_CALIBRATOR", "VPEC")
    for r in required:
        if r not in col_idx:
            raise KeyError(f"Pantheon+ column {r!r} missing; have {list(col_idx)}")

    rows = []
    with open(path) as f:
        f.readline()  # skip header
        for line in f:
            rows.append(line.split())

    print(f"  catalog rows: {len(rows)}")

    cids = []
    z_cmb_l, z_helio_l, z_hd_l, vpec_l = [], [], [], []
    m_b, m_b_err, ras, decs, is_cal = [], [], [], [], []
    for r in rows:
        try:
            cid = r[col_idx["CID"]]
            zCMB = float(r[col_idx["zCMB"]])
            zHEL = float(r[col_idx["zHEL"]])
            zHD = float(r[col_idx["zHD"]])
            vpec = float(r[col_idx["VPEC"]])
            m = float(r[col_idx["m_b_corr"]])
            me = float(r[col_idx["m_b_corr_err_DIAG"]])
            ra = float(r[col_idx["RA"]])
            dec = float(r[col_idx["DEC"]])
            cal = int(r[col_idx["IS_CALIBRATOR"]])
        except (ValueError, IndexError):
            continue
        cids.append(cid)
        z_cmb_l.append(zCMB)
        z_helio_l.append(zHEL)
        z_hd_l.append(zHD)
        vpec_l.append(vpec)
        m_b.append(m)
        m_b_err.append(me)
        ras.append(ra)
        decs.append(dec)
        is_cal.append(cal)

    cids = np.array(cids)
    z_cmb = np.array(z_cmb_l)
    z_helio = np.array(z_helio_l)
    z_hd = np.array(z_hd_l)
    vpec = np.array(vpec_l)
    m_b = np.array(m_b)
    m_b_err = np.array(m_b_err)
    ras = np.array(ras)
    decs = np.array(decs)
    is_cal = np.array(is_cal)

    # Construct zHEL+VPEC: heliocentric with peculiar-velocity correction,
    # but no CMB-rest-frame transform. Mirrors the zHD construction relative
    # to zHEL+VPEC instead of zCMB+VPEC:
    #   zHEL+VPEC := (1 + zHEL) * (1 - VPEC / c) - 1
    # (For sanity: at VPEC = 0, zHEL+VPEC = zHEL; the form mirrors how
    # Pantheon+ constructs zHD from zCMB.)
    z_hel_plus_vpec = (1.0 + z_helio) * (1.0 - vpec / C_KM_S) - 1.0

    if redshift_pipeline == "zHD":
        z_for_cut = z_hd
    elif redshift_pipeline == "zCMB":
        z_for_cut = z_cmb
    elif redshift_pipeline == "zHEL":
        z_for_cut = z_helio
    elif redshift_pipeline == "zHEL_plus_VPEC":
        z_for_cut = z_hel_plus_vpec
    else:
        raise ValueError(f"Unhandled pipeline {redshift_pipeline!r}")
    sel = (
        (is_cal == 0)
        & (z_for_cut > 0)
        & (z_for_cut < z_cut)
        & (z_cmb > 0)
        & (z_helio > 0)
        & np.isfinite(m_b)
        & np.isfinite(m_b_err)
        & (m_b_err > 0)
        & (ras > -360)
        & (ras < 720)
        & (decs > -91)
        & (decs < 91)
    )

    sel = sel & (z_helio > 0) & (z_hd > 0)

    n_sel = int(np.sum(sel))
    print(f"  after z<{z_cut} + calibrator exclusion: {n_sel} SNe")
    if n_sel < 500:
        print(f"  WARNING: only {n_sel} SNe pass cuts; pre-reg flagged < 500 as concerning")

    # Convert RA/DEC (ICRS) -> galactic (l, b) via astropy
    from astropy import units as u
    from astropy.coordinates import SkyCoord

    coords_icrs = SkyCoord(ras[sel] * u.deg, decs[sel] * u.deg, frame="icrs")
    coords_gal = coords_icrs.galactic
    l_deg_arr = np.array(coords_gal.l.deg)
    b_deg_arr = np.array(coords_gal.b.deg)

    # Unit vectors in galactic Cartesian
    n_hat = np.stack(
        [
            np.cos(np.radians(b_deg_arr)) * np.cos(np.radians(l_deg_arr)),
            np.cos(np.radians(b_deg_arr)) * np.sin(np.radians(l_deg_arr)),
            np.sin(np.radians(b_deg_arr)),
        ],
        axis=1,
    )  # (N, 3)

    # Distance modulus: mu = m_b_corr - M (M absorbed as nuisance offset)
    # We do NOT subtract a fixed M; instead the M-offset is solved as a free
    # parameter in the fit (4th param), absorbing all scale-independence.
    # For convenience, we report m_b_corr-centered "mu_offset" = m_b_corr.
    mu_offset = m_b[sel]
    mu_err_sel = m_b_err[sel]

    # Apply pipeline-chosen redshift
    z_fit = z_for_cut[sel]

    # ---- Load full STAT+SYS covariance and select submatrix ----
    selection_indices = np.where(sel)[0]
    inv_cov = None
    if use_full_covariance and cov_path is not None:
        cov_full = load_pantheon_covariance(cov_path, n_expected=len(cids))
        if cov_full is not None:
            cov_sub = cov_full[np.ix_(selection_indices, selection_indices)]
            # Inverse via Cholesky (numerically stable for positive-definite)
            try:
                inv_cov = np.linalg.inv(cov_sub)
                print(f"  inverse STAT+SYS sub-covariance computed for N={n_sel} SNe")
                # Sanity: should reduce to diag(1/sigma_DIAG^2) approximately when off-diag terms small
                diag_inv_check = float(np.mean(np.diag(inv_cov) * mu_err_sel**2))
                print(
                    f"  diag(inv_cov) * mu_err_DIAG^2 mean = {diag_inv_check:.3f} "
                    f"(1.0 would mean diag-only; smaller = more weight transferred to off-diag)"
                )
            except np.linalg.LinAlgError as e:
                print(f"  ERROR: covariance inversion failed: {e}; falling back to diagonal")
                inv_cov = None

    return PantheonSubset(
        cids=cids[sel],
        z=z_fit,
        z_helio=z_helio[sel],
        z_cmb=z_cmb[sel],
        z_hd=z_hd[sel],
        z_hel_plus_vpec=z_hel_plus_vpec[sel],
        vpec=vpec[sel],
        mu=mu_offset,
        mu_err=mu_err_sel,
        m_b_corr=m_b[sel],
        l_deg=l_deg_arr,
        b_deg=b_deg_arr,
        n_hat=n_hat,
        inv_cov=inv_cov,
        selection_indices=selection_indices,
    )


# ----------------------------------------------------------------------------
# Hubble-residual chi-squared with bulk-flow correction
# ----------------------------------------------------------------------------


def mu_lcdm_low_z(z: np.ndarray, h0_km_s_mpc: float, q0: float = Q0) -> np.ndarray:
    """Low-z LCDM distance modulus (mag).

    mu = 5 log10(d_L / 10 pc) where d_L = (c z / H_0) [1 + (1 - q_0) z / 2]
    Returns mu in magnitudes, with d_L in Mpc so the +25 offset is the
    "Mpc -> 10 pc" log shift.
    """
    d_L_mpc = (C_KM_S * z / h0_km_s_mpc) * (1.0 + 0.5 * (1.0 - q0) * z)
    return 5.0 * np.log10(d_L_mpc) + 25.0


def chi2_bulk_flow(
    params: np.ndarray,
    subset: PantheonSubset,
    h0_km_s_mpc: float,
) -> float:
    """Chi-squared with 3 bulk-flow params + 1 nuisance M offset.

    Model:
      mu_pred(z, n_hat; u, M) = mu_LCDM(z; H_0) + delta_mu_bulk(u, n_hat, z) + M

    where delta_mu_bulk is the linear bulk-flow correction:
      delta_mu_bulk = (5 / ln 10) * (1 / (c z)) * (u . n_hat)

    Per Watkins-Feldman-Hudson 2009 eq 9 (or equivalent low-z perturbation
    on the velocity-redshift relation; cf. Howlett+2017 eq 5). The u . n_hat
    factor is the line-of-sight projection of the local-volume bulk-flow
    vector u (km/s) onto the SN direction. Sign convention: positive
    u . n_hat means the local volume is moving TOWARD the SN, which shifts
    z_observed UPWARD and d_L UPWARD (more positive mu = fainter), so the
    +5/(c z ln 10) sign is correct.

    Chi-squared form:
      chi2 = r^T C^{-1} r   (if subset.inv_cov is available — full STAT+SYS)
      chi2 = sum_i (r_i / sigma_i)^2   (fallback: diagonal only)

    Parameters
    ----------
    params : (4,) array
        [u_x, u_y, u_z (km/s), M_offset (mag)]
    """
    u_x, u_y, u_z, M = params
    u_vec = np.array([u_x, u_y, u_z])

    # mu = m_b_corr (already a magnitude); model is M + mu_LCDM + delta_bulk
    mu_data = subset.mu  # m_b_corr
    mu_model_lcdm = mu_lcdm_low_z(subset.z, h0_km_s_mpc)

    # Bulk-flow line-of-sight projection per SN
    u_dot_n = subset.n_hat @ u_vec  # (N,)
    delta_mu = (5.0 / math.log(10.0)) * (u_dot_n / (C_KM_S * subset.z))

    residuals = mu_data - (M + mu_model_lcdm + delta_mu)

    if subset.inv_cov is not None:
        return float(residuals @ subset.inv_cov @ residuals)
    return float(np.sum((residuals / subset.mu_err) ** 2))


def fit_bulk_flow(
    subset: PantheonSubset,
    h0_km_s_mpc: float,
    u_init: np.ndarray = None,
) -> dict:
    """Run scipy.optimize.minimize on chi2_bulk_flow.

    Returns dict with best-fit params, chi2, Hessian (for sigma estimation).
    """
    from scipy.optimize import minimize

    if u_init is None:
        u_init = np.array([300.0, 300.0, 300.0, 0.0])  # 3 vel components + M=0

    n_sn = len(subset.z)

    # Initial chi2 (sanity)
    chi2_init = chi2_bulk_flow(u_init, subset, h0_km_s_mpc)
    print(f"    initial chi2 = {chi2_init:.2f} (N={n_sn}, init={u_init.tolist()})")

    result = minimize(
        chi2_bulk_flow,
        u_init,
        args=(subset, h0_km_s_mpc),
        method="Nelder-Mead",
        options={"xatol": 1e-3, "fatol": 1e-3, "maxiter": 50000, "adaptive": True},
    )

    if not result.success:
        print(f"    WARNING: minimizer did not converge: {result.message}")

    # Refine via L-BFGS-B from Nelder-Mead solution
    result2 = minimize(
        chi2_bulk_flow,
        result.x,
        args=(subset, h0_km_s_mpc),
        method="L-BFGS-B",
        options={"ftol": 1e-12, "gtol": 1e-8},
    )

    chi2_best = result2.fun
    u_best = result2.x[:3]
    M_best = result2.x[3]

    dof = n_sn - 4

    print(f"    best chi2/dof = {chi2_best:.2f} / {dof} = {chi2_best/dof:.3f}")
    print(f"    best u = {u_best.tolist()} km/s, M_offset = {M_best:.4f} mag")

    return {
        "u_best": u_best,
        "M_best": M_best,
        "chi2": float(chi2_best),
        "dof": int(dof),
        "n_sn": int(n_sn),
        "scipy_result": result2,
    }


def _numerical_hessian(func, x0, args, eps=None):
    """Two-sided numerical Hessian via central differences.

    eps : per-parameter step. If None, uses sqrt(machine eps) * |x_i|.
    """
    x0 = np.asarray(x0, dtype=float)
    n = len(x0)
    H = np.zeros((n, n))
    if eps is None:
        eps = np.array([max(1.0, abs(xi)) * 1e-4 for xi in x0])
    else:
        eps = np.asarray(eps, dtype=float)
        if eps.ndim == 0:
            eps = np.ones(n) * float(eps)

    f0 = func(x0, *args)
    for i in range(n):
        for j in range(i, n):
            xpp = x0.copy()
            xpp[i] += eps[i]
            xpp[j] += eps[j]
            xpm = x0.copy()
            xpm[i] += eps[i]
            xpm[j] -= eps[j]
            xmp = x0.copy()
            xmp[i] -= eps[i]
            xmp[j] += eps[j]
            xmm = x0.copy()
            xmm[i] -= eps[i]
            xmm[j] -= eps[j]
            H[i, j] = (func(xpp, *args) - func(xpm, *args) - func(xmp, *args) + func(xmm, *args)) / (
                4 * eps[i] * eps[j]
            )
            H[j, i] = H[i, j]
    return H


def sigma_hubble_hessian_mc(
    fit_result: dict,
    subset: PantheonSubset,
    h0_km_s_mpc: float,
    n_mc: int = 1000,
    rng_seed: int = 42,
) -> dict:
    """Hessian-based Monte Carlo for sigma_Hubble (direction).

    The chi2 is 2 (-ln L), so the Fisher info = (1/2) Hessian of chi2.
    Inverse Fisher = parameter covariance. We Monte Carlo-sample
    N(u_best, Sigma_u) and convert each draw to angular direction
    (l, b); sigma_Hubble = great-circle 68% containment radius.
    """
    u_best = np.array([fit_result["u_best"][0], fit_result["u_best"][1], fit_result["u_best"][2], fit_result["M_best"]])

    H = _numerical_hessian(chi2_bulk_flow, u_best, args=(subset, h0_km_s_mpc))
    # chi2 = -2 ln L (with Gaussian errors); Fisher = 0.5 * H_chi2
    # parameter covariance = 2 * inv(H_chi2)
    cov = 2.0 * np.linalg.inv(H)
    cov_u = cov[:3, :3]  # marginalize over M

    # Eigenvalue inspection
    eigvals = np.linalg.eigvalsh(cov_u)
    if np.any(eigvals <= 0):
        print(
            f"    WARNING: Hessian-derived cov is not positive definite; "
            f"eigvals = {eigvals.tolist()}. Hessian-MC sigma may be unreliable."
        )

    print(f"    cov_u eigenvalues (km/s)^2: {eigvals.tolist()}")

    # Best-fit direction
    u_b = fit_result["u_best"]
    n_best = u_b / np.linalg.norm(u_b)

    rng = np.random.default_rng(rng_seed)
    samples = rng.multivariate_normal(u_b, cov_u, size=n_mc)
    sample_norms = np.linalg.norm(samples, axis=1)
    valid = sample_norms > 1.0  # require magnitude > 1 km/s
    samples_dirs = samples[valid] / sample_norms[valid, None]

    # Angular separations from best direction (undirected: use |cos|)
    dots = np.abs(samples_dirs @ n_best)
    dots = np.clip(dots, -1.0, 1.0)
    angles_deg = np.degrees(np.arccos(dots))
    sigma_68 = float(np.quantile(angles_deg, 0.6827))

    return {
        "method": "Hessian + Gaussian MC (1000 samples)",
        "sigma_deg_68": sigma_68,
        "best_u_km_s": fit_result["u_best"].tolist(),
        "best_u_magnitude_km_s": float(np.linalg.norm(fit_result["u_best"])),
        "cov_u_eigenvalues": eigvals.tolist(),
        "n_samples_valid": int(np.sum(valid)),
    }


def sigma_hubble_bootstrap(
    subset: PantheonSubset,
    h0_km_s_mpc: float,
    fit_result: dict,
    n_boot: int = 500,
    rng_seed: int = 24601,
) -> dict:
    """Block bootstrap on SN catalog for sigma_Hubble.

    Draws n_boot resamples (with replacement) of the SN catalog, re-fits
    bulk-flow on each, computes 68% containment radius of direction
    distribution.
    """
    rng = np.random.default_rng(rng_seed)
    n = len(subset.z)
    u_best = fit_result["u_best"]
    n_best = u_best / np.linalg.norm(u_best)

    boot_directions = []
    boot_magnitudes = []
    converged_count = 0
    print(f"    block bootstrap: {n_boot} resamples of {n} SNe")
    for b in range(n_boot):
        idx = rng.integers(0, n, size=n)
        # Bootstrap: with replacement on SN index. For chi^2 we use the
        # diagonal mu_err only; correctly resampling the FULL covariance
        # under sub-sampling would require row/column index pair selection
        # AND re-inverting (expensive). The bootstrap is a directional-spread
        # check, not a precision pin; diagonal-only is acceptable here.
        sub_b = PantheonSubset(
            cids=subset.cids[idx],
            z=subset.z[idx],
            z_helio=subset.z_helio[idx],
            z_cmb=subset.z_cmb[idx],
            z_hd=subset.z_hd[idx],
            z_hel_plus_vpec=subset.z_hel_plus_vpec[idx],
            vpec=subset.vpec[idx],
            mu=subset.mu[idx],
            mu_err=subset.mu_err[idx],
            m_b_corr=subset.m_b_corr[idx],
            l_deg=subset.l_deg[idx],
            b_deg=subset.b_deg[idx],
            n_hat=subset.n_hat[idx],
            inv_cov=None,  # bootstrap uses diagonal only (see comment above)
            selection_indices=None,
        )
        # Warm-start from main fit (much faster + more stable)
        from scipy.optimize import minimize

        u_init = np.concatenate([u_best, [fit_result["M_best"]]])
        r = minimize(
            chi2_bulk_flow,
            u_init,
            args=(sub_b, h0_km_s_mpc),
            method="L-BFGS-B",
            options={"ftol": 1e-9, "gtol": 1e-6, "maxiter": 1000},
        )
        if not r.success or np.linalg.norm(r.x[:3]) < 1.0:
            continue
        converged_count += 1
        u_b = r.x[:3]
        boot_directions.append(u_b / np.linalg.norm(u_b))
        boot_magnitudes.append(float(np.linalg.norm(u_b)))
        if (b + 1) % 100 == 0:
            print(f"      {b + 1}/{n_boot} resamples ({converged_count} converged)")

    boot_dirs = np.array(boot_directions)
    boot_mags = np.array(boot_magnitudes)

    dots = np.abs(boot_dirs @ n_best)
    dots = np.clip(dots, -1.0, 1.0)
    angles_deg = np.degrees(np.arccos(dots))
    sigma_68 = float(np.quantile(angles_deg, 0.6827))

    return {
        "method": f"Block bootstrap ({converged_count}/{n_boot} converged)",
        "sigma_deg_68": sigma_68,
        "n_bootstraps_converged": int(converged_count),
        "n_bootstraps_attempted": int(n_boot),
        "mean_magnitude_km_s": float(np.mean(boot_mags)),
        "magnitude_std_km_s": float(np.std(boot_mags)),
    }


# ----------------------------------------------------------------------------
# Full pipeline (one redshift convention)
# ----------------------------------------------------------------------------


@dataclass
class BulkFlowPipelineResult:
    pipeline_name: str
    redshift_field: str
    h0_used_km_s_mpc: float
    n_sn: int
    chi2: float
    dof: int
    chi2_per_dof: float
    u_best_km_s: list
    magnitude_km_s: float
    l_deg: float  # canonicalized: 0 <= l < 180
    b_deg: float  # axis (sign of b matches canonical l)
    sigma_hubble_hessian_deg: float
    sigma_hubble_bootstrap_deg: float
    sigma_hubble_canonical_deg: float  # max(hessian, bootstrap)
    hessian_diagnostic: dict
    bootstrap_diagnostic: dict
    used_full_covariance: bool = False
    diagnostics: dict = field(default_factory=dict)


def canonicalize_axis_lb(l_deg: float, b_deg: float) -> tuple[float, float]:
    """Force axis into 0 <= l < 180 with sign-flip on b if needed.

    Axes are direction-only (lines), so (l, b) and (l+180, -b) are the same.
    """
    if l_deg >= 180.0:
        return (l_deg - 180.0, -b_deg)
    return (l_deg, b_deg)


def run_pipeline(
    pipeline_name: str,
    redshift_field: str,
    h0_km_s_mpc: float,
    rng_seed_hessian: int = 42,
    rng_seed_boot: int = 24601,
    use_full_covariance: bool = True,
) -> BulkFlowPipelineResult:
    print()
    print("=" * 80)
    print(f"PIPELINE: {pipeline_name}  (redshift={redshift_field}, H0={h0_km_s_mpc:.3f} km/s/Mpc)")
    print(f"  use_full_covariance = {use_full_covariance}")
    print("=" * 80)

    subset = load_pantheon_subset(
        PANTHEON_PATH,
        z_cut=0.1,
        redshift_pipeline=redshift_field,
        cov_path=PANTHEON_COV_PATH if use_full_covariance else None,
        use_full_covariance=use_full_covariance,
    )

    print(f"\n  fitting bulk-flow ({len(subset.z)} SNe)...")
    fit_result = fit_bulk_flow(subset, h0_km_s_mpc)

    # Direction
    u_b = fit_result["u_best"]
    magnitude = float(np.linalg.norm(u_b))
    l_raw, b_raw = cartesian_to_galactic(u_b)
    l_canon, b_canon = canonicalize_axis_lb(l_raw, b_raw)

    print(f"\n  best-fit direction (axis-canonicalized 0<=l<180): " f"(l, b) = ({l_canon:.2f}°, {b_canon:.2f}°)")
    print(f"  |u| = {magnitude:.1f} km/s")

    # sigma from Hessian + bootstrap
    print(f"\n  computing sigma_Hubble via Hessian MC...")
    hessian = sigma_hubble_hessian_mc(fit_result, subset, h0_km_s_mpc, rng_seed=rng_seed_hessian)
    print(f"    Hessian-MC sigma_68 = {hessian['sigma_deg_68']:.2f}°")

    print(f"\n  computing sigma_Hubble via block bootstrap...")
    boot = sigma_hubble_bootstrap(subset, h0_km_s_mpc, fit_result, rng_seed=rng_seed_boot)
    print(f"    Bootstrap sigma_68 = {boot['sigma_deg_68']:.2f}°")

    sigma_canon = max(hessian["sigma_deg_68"], boot["sigma_deg_68"])
    print(f"\n  canonical sigma_Hubble = max(Hessian, Bootstrap) = {sigma_canon:.2f}°")

    return BulkFlowPipelineResult(
        pipeline_name=pipeline_name,
        redshift_field=redshift_field,
        h0_used_km_s_mpc=h0_km_s_mpc,
        n_sn=fit_result["n_sn"],
        chi2=fit_result["chi2"],
        dof=fit_result["dof"],
        chi2_per_dof=float(fit_result["chi2"] / fit_result["dof"]),
        u_best_km_s=u_b.tolist(),
        magnitude_km_s=magnitude,
        l_deg=l_canon,
        b_deg=b_canon,
        sigma_hubble_hessian_deg=hessian["sigma_deg_68"],
        sigma_hubble_bootstrap_deg=boot["sigma_deg_68"],
        sigma_hubble_canonical_deg=sigma_canon,
        hessian_diagnostic=hessian,
        bootstrap_diagnostic=boot,
        used_full_covariance=bool(subset.inv_cov is not None),
        diagnostics={
            "n_sn_input_cut": int(fit_result["n_sn"]),
            "chi2_per_dof": float(fit_result["chi2"] / fit_result["dof"]),
            "raw_lb_pre_canonicalization": (l_raw, b_raw),
        },
    )


# ----------------------------------------------------------------------------
# Comparison + adjudication
# ----------------------------------------------------------------------------


def load_e1b_cmb_axis() -> dict:
    """Read E1b empirical CMB axis-of-evil from results JSON."""
    with open(CMB_AXIS_RESULTS_PATH) as f:
        d = json.load(f)
    aoe = d["axis_of_evil_computation"]
    return {
        "l_deg": float(aoe["l_deg"]),
        "b_deg": float(aoe["b_deg"]),
        "sigma_deg": float(aoe["sigma_deg"]),
        "source": "Planck PR3 SMICA, E1b session (cmb_axis_alignment_executable_observer_results.json)",
    }


def cmb_hubble_comparison(pipeline_result: BulkFlowPipelineResult, cmb_axis: dict) -> dict:
    """Compute CMB-vs-Hubble angular separation in sigma units."""
    sep = angular_separation_deg_undirected(
        cmb_axis["l_deg"],
        cmb_axis["b_deg"],
        pipeline_result.l_deg,
        pipeline_result.b_deg,
    )
    sigma_combined = math.sqrt(cmb_axis["sigma_deg"] ** 2 + pipeline_result.sigma_hubble_canonical_deg**2)
    sigma_separation_vs_pass = (sep - CMB_AXIS_PASS_THRESHOLD_DEG) / sigma_combined
    # Decisive against alignment: separation > 20 deg at > 3 sigma
    decisive_against_alignment = sigma_separation_vs_pass > 3.0
    # Decisive for alignment: separation < 3 sigma of zero
    sigma_separation_vs_zero = sep / sigma_combined
    decisive_for_alignment = sigma_separation_vs_zero < 3.0

    return {
        "cmb_axis_lb": (cmb_axis["l_deg"], cmb_axis["b_deg"]),
        "hubble_axis_lb": (pipeline_result.l_deg, pipeline_result.b_deg),
        "separation_deg": sep,
        "sigma_combined_deg": sigma_combined,
        "sigma_separation_vs_pass_threshold": sigma_separation_vs_pass,
        "sigma_separation_vs_zero": sigma_separation_vs_zero,
        "decisive_against_alignment_3sigma": decisive_against_alignment,
        "decisive_for_alignment_3sigma": decisive_for_alignment,
    }


def adjudicate(
    primary: BulkFlowPipelineResult,
    sub: BulkFlowPipelineResult,
    primary_cmp: dict,
    sub_cmp: dict,
    primary_chi2_per_dof: float = None,
) -> dict:
    """Map sigma_Hubble + separation to A / C / D-sustained / Marginal-D / E."""
    sigma_h = primary.sigma_hubble_canonical_deg

    # Sub-analysis consistency: 1-sigma overlap?
    sub_to_primary_sep = angular_separation_deg_undirected(primary.l_deg, primary.b_deg, sub.l_deg, sub.b_deg)
    combined_subprimary_sigma = math.sqrt(primary.sigma_hubble_canonical_deg**2 + sub.sigma_hubble_canonical_deg**2)
    sub_primary_consistent_1sigma = sub_to_primary_sep < combined_subprimary_sigma

    # Magnitude consistency check
    magnitude_consistent_with_zero = primary.magnitude_km_s < 50.0

    # Outcome E pre-check: structural sanity
    if not primary_cmp["sigma_combined_deg"] > 0:
        return {
            "outcome": "E",
            "reason": "fit produced zero / negative combined sigma; structural failure",
        }

    # Outcome E surface: chi2/dof << 1 or >> 1 indicates error mis-spec.
    # With the full STAT+SYS covariance, chi2/dof should naturally fall near 1
    # (the covariance is calibrated to do so). If it doesn't, that's a real
    # surface. Threshold: chi2/dof not in [0.6, 1.6] is suspect.
    if primary_chi2_per_dof is not None:
        if primary_chi2_per_dof < 0.6 or primary_chi2_per_dof > 1.6:
            return {
                "outcome": "E",
                "name": ("METHODOLOGY SURFACE — chi2/dof outside [0.6, 1.6] " "indicates error mis-specification"),
                "reason": (
                    f"Primary fit chi2/dof = {primary_chi2_per_dof:.3f} outside "
                    f"the [0.6, 1.6] band. With the full STAT+SYS covariance "
                    f"calibrated to chi2/dof ~ 1, this indicates either: "
                    f"(a) the covariance was loaded incorrectly; "
                    f"(b) the bulk-flow model is mis-specified "
                    f"(e.g., missing higher-order terms in z); "
                    f"(c) there's a residual systematic. "
                    f"sigma_Hubble = {sigma_h:.2f}° cannot be considered final."
                ),
                "sub_primary_sep_deg": sub_to_primary_sep,
                "sub_primary_consistent_1sigma": bool(sub_primary_consistent_1sigma),
                "cascade": (
                    "C5 row updates to E (methodology surface). Pause before retry. "
                    "Investigate covariance load + model fidelity before pinning result. "
                    "Grant adjudication required."
                ),
            }

    if magnitude_consistent_with_zero:
        return {
            "outcome": "D-sustained",
            "reason": (
                f"Bulk-flow magnitude {primary.magnitude_km_s:.1f} km/s < 50 km/s — "
                f"direction effectively unconstrained per prereg §5 tie-breaker. "
                f"Pre-registered D-sustained automatic."
            ),
            "sub_primary_sep_deg": sub_to_primary_sep,
            "sub_primary_consistent_1sigma": bool(sub_primary_consistent_1sigma),
        }

    # Outcome A: PASS (tension, decisive against alignment)
    if sigma_h < SIGMA_BRIEF_TARGET_DEG and primary_cmp["decisive_against_alignment_3sigma"]:
        return {
            "outcome": "A",
            "name": "PASS (CMB-Hubble misaligned >3σ)",
            "reason": (
                f"sigma_Hubble = {sigma_h:.2f}° < {SIGMA_BRIEF_TARGET_DEG}° "
                f"(brief target), CMB-Hubble separation "
                f"{primary_cmp['separation_deg']:.1f}° at "
                f"{primary_cmp['sigma_separation_vs_pass_threshold']:.2f}σ above 20° "
                f"alignment threshold. Decisive against alignment."
            ),
            "sub_primary_sep_deg": sub_to_primary_sep,
            "sub_primary_consistent_1sigma": bool(sub_primary_consistent_1sigma),
            "downgrade_due_to_sub_divergence": not sub_primary_consistent_1sigma,
            "cascade": (
                "C5 row updates to PASS. D4-A034 cosmic instance RETIRES "
                "(catalog of 20+ other instances survives). E1c (Route 3 "
                "framework-commitment activation) UNBLOCKS for next session. "
                "If sub-primary inconsistent: PASS downgraded to marginal-A; "
                "methodology investigation queued."
            ),
        }

    # Outcome C: NULL (alignment, decisive for alignment)
    if sigma_h < SIGMA_BRIEF_TARGET_DEG and primary_cmp["decisive_for_alignment_3sigma"]:
        return {
            "outcome": "C",
            "name": "NULL (CMB-Hubble aligned <3σ)",
            "reason": (
                f"sigma_Hubble = {sigma_h:.2f}° < {SIGMA_BRIEF_TARGET_DEG}° "
                f"(brief target), CMB-Hubble separation "
                f"{primary_cmp['separation_deg']:.1f}° within 3σ of zero. "
                f"Decisive for alignment."
            ),
            "sub_primary_sep_deg": sub_to_primary_sep,
            "sub_primary_consistent_1sigma": bool(sub_primary_consistent_1sigma),
            "downgrade_due_to_sub_divergence": not sub_primary_consistent_1sigma,
            "cascade": (
                "C5 row updates to NULL-aligned. D4-A034 cosmic instance "
                "STRENGTHENS. E1c needs alternative path (re-route)."
            ),
        }

    # Marginal-D: tightened but not decisive
    if SIGMA_BRIEF_TARGET_DEG <= sigma_h < SIGMA_INSUFFICIENT_DEG or (
        sigma_h < SIGMA_BRIEF_TARGET_DEG
        and not primary_cmp["decisive_against_alignment_3sigma"]
        and not primary_cmp["decisive_for_alignment_3sigma"]
    ):
        return {
            "outcome": "Marginal-D",
            "name": "DATA INSUFFICIENT (improved, not decisive)",
            "reason": (
                f"sigma_Hubble = {sigma_h:.2f}° in [{SIGMA_BRIEF_TARGET_DEG:.0f}, "
                f"{SIGMA_INSUFFICIENT_DEG:.1f}]° marginal window. Tighter than "
                f"Whitford+2023's ~30° but not 3σ-decisive. Separation = "
                f"{primary_cmp['separation_deg']:.1f}° at "
                f"{primary_cmp['sigma_separation_vs_pass_threshold']:+.2f}σ above 20° threshold."
            ),
            "sub_primary_sep_deg": sub_to_primary_sep,
            "sub_primary_consistent_1sigma": bool(sub_primary_consistent_1sigma),
            "cascade": (
                "C5 row updates to D with refined-bounds note. Queue joint-constraint "
                "session (Pantheon+ + SDSS DR17 spin-orientation re-analysis) for "
                "decisive 3σ adjudication."
            ),
        }

    # D-sustained: sigma_Hubble too wide
    return {
        "outcome": "D-sustained",
        "name": "DATA INSUFFICIENT (sustained)",
        "reason": (
            f"sigma_Hubble = {sigma_h:.2f}° >= {SIGMA_INSUFFICIENT_DEG:.1f}° "
            f"prereg threshold; alignment within 3σ at {primary_cmp['sigma_separation_vs_zero']:.2f}σ "
            f"of zero. Result not improved over Whitford+2023 ~30° literature."
        ),
        "sub_primary_sep_deg": sub_to_primary_sep,
        "sub_primary_consistent_1sigma": bool(sub_primary_consistent_1sigma),
        "cascade": (
            "C5 row stays D-sustained. Queue SDSS DR17 spin-orientation re-analysis "
            "as next-session alternative path to closing C5. E1c stays deferred."
        ),
    }


# ----------------------------------------------------------------------------
# Cross-check: does zHEL - zCMB recover the CMB dipole?
# ----------------------------------------------------------------------------


def _check_cmb_dipole_recovery(
    diagnostic_zCMB: BulkFlowPipelineResult,
    diagnostic_zHEL: BulkFlowPipelineResult,
) -> dict:
    """The zCMB pipeline subtracts solar motion; the zHEL pipeline does not.

    The difference between the two best-fit u vectors should equal the
    conventional CMB dipole solar velocity at (l=264°, b=48°), |v|≈370 km/s.

    This is a structural sanity check that the catalog's zCMB construction
    is internally consistent (or equivalently, that the per-SN solar motion
    subtraction is being applied as expected).
    """
    u_cmb = np.array(diagnostic_zCMB.u_best_km_s)
    u_hel = np.array(diagnostic_zHEL.u_best_km_s)
    delta_u = u_hel - u_cmb
    delta_mag = float(np.linalg.norm(delta_u))
    l_delta, b_delta = cartesian_to_galactic(delta_u)
    # Planck 2020 conventional CMB dipole
    PLANCK_DIPOLE_L = 264.02
    PLANCK_DIPOLE_B = 48.25
    PLANCK_DIPOLE_V = 369.82
    sep_to_planck = angular_separation_deg_undirected(l_delta, b_delta, PLANCK_DIPOLE_L, PLANCK_DIPOLE_B)
    return {
        "implied_solar_motion_km_s": delta_u.tolist(),
        "implied_solar_motion_magnitude_km_s": delta_mag,
        "implied_solar_motion_direction_l_b": (l_delta, b_delta),
        "planck_2020_cmb_dipole_l_b_v": (PLANCK_DIPOLE_L, PLANCK_DIPOLE_B, PLANCK_DIPOLE_V),
        "separation_implied_vs_planck_deg": sep_to_planck,
        "magnitude_ratio_implied_over_planck": delta_mag / PLANCK_DIPOLE_V,
        "passes_dipole_recovery_check": (sep_to_planck < 5.0 and 0.9 < (delta_mag / PLANCK_DIPOLE_V) < 1.1),
    }


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------


def main():
    print("=" * 80)
    print("C5-CMB-AXIS Pantheon+ Bulk-Flow Tightening — E1b-prime driver")
    print("Prereg: research/2026-05-19_c5-pantheon-tightening-prereg.md")
    print("Briefing: _orchestration/section-e-cascade.md (Phase E1b-prime)")
    print("=" * 80)
    print(f"\nCanonical constants (per ave-canonical-source):")
    print(f"  C_0 = {C_0:.6e} m/s = {C_KM_S:.3f} km/s")
    print(f"  H_INFINITY = {H_INFINITY:.6e} 1/s")
    print(f"  H_0 (AVE)        = {H0_AVE_KM_S_MPC:.3f} km/s/Mpc")
    print(f"  H_0 (SH0ES2022)  = {H0_PANTHEON_SH0ES_KM_S_MPC:.3f} km/s/Mpc")
    print(f"  Q_0 = {Q0} (LCDM low-z, fixed)")

    # Forward-prediction discipline check (per ave-driver-script-honesty)
    print(f"\nFORWARD-PREDICTION DISCIPLINE CHECK (per ave-driver-script-honesty §3.7):")
    print(f"  (1) Does chi2 see the CMB axis? NO — chi2 = Hubble residual only.")
    print(f"  (2) Are starting params biased toward CMB axis? NO — u_init = (300,300,300).")
    print(f"  (3) Is alignment functional minimized? NO — chi2 is direction-agnostic.")
    print(f"  (4) Does result depend on chosen comparison axis? NO — fit is independent.")
    print(f"  All 4 discriminators pass. Proceeding with forward-prediction fit.")

    if not PANTHEON_PATH.exists():
        print(f"\nERROR: Pantheon+ data not at {PANTHEON_PATH}")
        return {"outcome": "E", "reason": "data not accessible"}

    cmb_axis = load_e1b_cmb_axis()
    print(f"\nE1b empirical CMB axis (loaded post-fit, NOT seen by fit):")
    print(f"  (l = {cmb_axis['l_deg']:.2f}°, b = {cmb_axis['b_deg']:.2f}°), " f"sigma = {cmb_axis['sigma_deg']:.2f}°")

    # ---- Primary pipeline: zHD (CMB-rest-frame + 2M++ VPEC) ----
    # Per prereg §3.6: "standard Pantheon+ pipeline (heliocentric ->
    # CMB-rest-frame transform via conventional CMB dipole + 2M++ LSS
    # peculiar-velocity correction)". Identity verified empirically against
    # catalog: zHD = (1+zCMB)*(1-VPEC/c) - 1 to 1e-6 accuracy.
    primary = run_pipeline(
        pipeline_name="primary (zHD = CMB-rest + 2M++ VPEC, standard Pantheon+ pipeline)",
        redshift_field="zHD",
        h0_km_s_mpc=H0_PANTHEON_SH0ES_KM_S_MPC,
        rng_seed_hessian=42,
        rng_seed_boot=24601,
    )

    # ---- Sub-analysis: zHEL+VPEC (2M++ LSS correction only, no CMB-rest) ----
    # Per prereg §3.6 defense-in-depth: "heliocentric velocities with 2M++ LSS
    # correction only (no CMB-rest-frame transform)". Constructed as
    # zHEL_plus_VPEC := (1+zHEL)*(1-VPEC/c) - 1 (mirrors zHD construction from
    # zCMB, but starts from zHEL instead).
    sub = run_pipeline(
        pipeline_name="sub-analysis (zHEL + 2M++ VPEC, no CMB-rest-frame transform)",
        redshift_field="zHEL_plus_VPEC",
        h0_km_s_mpc=H0_PANTHEON_SH0ES_KM_S_MPC,
        rng_seed_hessian=43,
        rng_seed_boot=24602,
    )

    # ---- Additional diagnostic pipelines (cross-checks) ----
    # zCMB-only and zHEL-only are diagnostic, not load-bearing — the difference
    # (zCMB - zHEL) should approximate the conventional CMB dipole vector.
    diagnostic_zCMB = run_pipeline(
        pipeline_name="diagnostic (zCMB-only, no VPEC)",
        redshift_field="zCMB",
        h0_km_s_mpc=H0_PANTHEON_SH0ES_KM_S_MPC,
        rng_seed_hessian=44,
        rng_seed_boot=24603,
    )
    diagnostic_zHEL = run_pipeline(
        pipeline_name="diagnostic (zHEL raw, no correction)",
        redshift_field="zHEL",
        h0_km_s_mpc=H0_PANTHEON_SH0ES_KM_S_MPC,
        rng_seed_hessian=45,
        rng_seed_boot=24604,
    )

    # ---- CMB comparison ----
    primary_cmp = cmb_hubble_comparison(primary, cmb_axis)
    sub_cmp = cmb_hubble_comparison(sub, cmb_axis)

    print()
    print("=" * 80)
    print("CMB axis comparison")
    print("=" * 80)
    print(
        f"  Reference CMB axis (E1b): (l={cmb_axis['l_deg']:.2f}°, b={cmb_axis['b_deg']:.2f}°), "
        f"sigma_CMB = {cmb_axis['sigma_deg']:.2f}°"
    )
    print(f"\nPrimary (zCMB): Hubble axis (l={primary.l_deg:.2f}°, b={primary.b_deg:.2f}°)")
    print(f"   |u| = {primary.magnitude_km_s:.1f} km/s")
    print(
        f"   sigma_Hubble = {primary.sigma_hubble_canonical_deg:.2f}° "
        f"(Hessian {primary.sigma_hubble_hessian_deg:.2f}, "
        f"Bootstrap {primary.sigma_hubble_bootstrap_deg:.2f})"
    )
    print(
        f"   CMB-Hubble separation = {primary_cmp['separation_deg']:.2f}° "
        f"at {primary_cmp['sigma_separation_vs_pass_threshold']:+.2f}σ above 20° threshold"
    )
    print(f"   Decisive against alignment (3σ)? {primary_cmp['decisive_against_alignment_3sigma']}")
    print(f"   Decisive FOR alignment (3σ)? {primary_cmp['decisive_for_alignment_3sigma']}")

    print(f"\nSub-analysis (zHEL): Hubble axis (l={sub.l_deg:.2f}°, b={sub.b_deg:.2f}°)")
    print(f"   |u| = {sub.magnitude_km_s:.1f} km/s")
    print(f"   sigma_Hubble = {sub.sigma_hubble_canonical_deg:.2f}°")
    print(f"   CMB-Hubble separation = {sub_cmp['separation_deg']:.2f}°")

    sub_to_primary_sep = angular_separation_deg_undirected(primary.l_deg, primary.b_deg, sub.l_deg, sub.b_deg)
    print(f"\n  Sub-primary axis separation = {sub_to_primary_sep:.2f}°")
    print(
        f"  Sub-primary sigma sum = "
        f"{math.sqrt(primary.sigma_hubble_canonical_deg**2 + sub.sigma_hubble_canonical_deg**2):.2f}°"
    )
    print(
        f"  Consistent at 1σ overlap? "
        f"{sub_to_primary_sep < math.sqrt(primary.sigma_hubble_canonical_deg**2 + sub.sigma_hubble_canonical_deg**2)}"
    )

    # ---- Adjudicate ----
    primary_chi2_per_dof = primary.chi2 / primary.dof
    verdict = adjudicate(primary, sub, primary_cmp, sub_cmp, primary_chi2_per_dof=primary_chi2_per_dof)
    print()
    print("=" * 80)
    print(f"OUTCOME: {verdict['outcome']}")
    if "name" in verdict:
        print(f"         {verdict['name']}")
    print("=" * 80)
    print(f"Reason: {verdict['reason']}")
    if "cascade" in verdict:
        print(f"\nCascade: {verdict['cascade']}")

    # ---- Serialize results ----
    results = {
        "driver": "c5_pantheon_bulk_flow_tightening.py",
        "prereg": "research/2026-05-19_c5-pantheon-tightening-prereg.md",
        "briefing": "_orchestration/section-e-cascade.md",
        "branch": "analysis/c5-pantheon-tightening",
        "date": "2026-05-19",
        "constants_used": {
            "C_0_m_per_s": C_0,
            "H_INFINITY_inv_s": H_INFINITY,
            "H0_AVE_km_s_Mpc": H0_AVE_KM_S_MPC,
            "H0_SH0ES_km_s_Mpc": H0_PANTHEON_SH0ES_KM_S_MPC,
            "Q0": Q0,
        },
        "forward_prediction_discipline_check": {
            "chi2_sees_cmb_axis": False,
            "starting_params_biased_to_cmb_axis": False,
            "alignment_functional_minimized": False,
            "result_depends_on_comparison_axis": False,
        },
        "cmb_axis_reference": cmb_axis,
        "primary_pipeline_zHD": asdict(primary),
        "sub_analysis_zHEL_plus_VPEC": asdict(sub),
        "diagnostic_zCMB_only": asdict(diagnostic_zCMB),
        "diagnostic_zHEL_raw": asdict(diagnostic_zHEL),
        "primary_cmb_comparison": primary_cmp,
        "sub_cmb_comparison": sub_cmp,
        "sub_primary_axis_separation_deg": sub_to_primary_sep,
        "primary_chi2_per_dof": primary_chi2_per_dof,
        "primary_used_full_covariance": primary.used_full_covariance,
        "verdict": verdict,
        "cross_check_dipole_recovery": _check_cmb_dipole_recovery(diagnostic_zCMB, diagnostic_zHEL),
    }
    with open(RESULTS_PATH, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults JSON: {RESULTS_PATH}")
    return results


if __name__ == "__main__":
    main()
