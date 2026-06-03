"""
alpha_cosserat_binding_test.py — α Class-2 lift, Cosserat micropolar engine.

Re-run of the electron binding + geometry-selection test for the α Class-2 lift,
this time on the FULL Cosserat micropolar engine (CosseratField3D — has the
micro-spin ω DOF + omega_yield = π saturation + S11-min relaxation), NOT vector
Maxwell. The prior FDTD run (analysis/alpha-cell-count) found the generic (2,3)
E-seed DISPERSED; diagnosis: the (2,3) is a Cosserat micro-spin (ω) winding and
vector Maxwell has no independent microrotation DOF (Ax 1, KB CLAUDE.md
INVARIANT-S2: "3 microrotational -> B; Cosserat rotational DOF IS the
substrate-native origin of intrinsic spin"). The Cosserat lattice IS that DOF.

CLAIM UNDER TEST
----------------
The minimal stable Cosserat soliton on the chiral K4 lattice (latched by Ax4
saturation, omega_yield = pi) should DYNAMICALLY SELECT the (2,3) winding +
R*r ~ 1/4 (R/r ~ phi^2) WITHOUT being seeded there. If it does, alpha = 1/Q is
geometric and the embedding is derived, not posited.

MEASUREMENT COORDINATE (per epic brief section 8, the A46 fix)
--------------------------------------------------------------
PRIMARY measure is in the (u, omega) Cosserat reactance plane (phase-space), NOT
real-space lattice cells. Winding (p,q) read from the omega micro-spin field via
the engine extract_crossing_count (phase-winding of omega_x + i*omega_y around
toroidal contours). R*r read from the (u, omega) reactance content (see measure).

  *** LOAD-BEARING COORDINATE FLAG (surfaced to Grant; flag-don't-fix) ***
  The corpus phi^2-Golden-Torus PHASE-SPACE claim (doc 28 section 3, 5.1) lives
  in the K4 (V_inc, V_ref) bond phasor space, and the engine docstrings
  (cosserat_field_3d.py:876-877, 1028-1029) state the (2,3) phase-space winding
  is "NOT in scope of Cosserat sector; lives in K4 V-tank." The (u, omega)
  Cosserat reactance plane this driver measures is a DIFFERENT phase-space -- it
  tests whether the Cosserat MICRO-SPIN sector independently selects (2,3)+1/4 in
  its own reactance coordinates. Outcome here does not transfer to the K4-V-tank
  claim and vice-versa; this is a parallel sector test per the epic brief
  re-scope, not the doc-28 canonical (V_inc,V_ref) test. See report.

HARD GUARDS (enforced at runtime by _self_audit_no_forbidden_tokens)
--------------------------------------------------------------------
  - NO IMPOSED GEOMETRY: generic seed (round neutral R/r), NOT the Golden Torus
    (R=phi/2, r=(phi-1)/2) / R*r=1/4 / Clifford embedding. No PHI / R_GOLDEN_TORUS.
  - NO alpha/CHARGE IN ANY MEASURE: forbid {ALPHA, ALPHA_COLD, ALPHA_COLD_INV,
    V_SNAP, XI_TOPO, e_charge, PHI, R_GOLDEN_TORUS} as inputs to the
    geometry/cell measures. omega_yield (= pi, alpha-free) for confinement only.
  - FORWARD-NOT-FIT: report whatever (p,q), R*r, N come out. No tuning.
  - S11-MIN, not energy-gradient (substrate-native). Threshold-free N_eff;
    exclude boundary/PML cells.

OUTCOMES
--------
  A (LIFT):       binds from generic seed AND selects (2,3) + R*r~1/4 in (u,omega)
                  phase-space, alpha-free -> the lattice forces the embedding.
  B (RELOCATION): (2,3)+1/4 only if seeded there.
  C (FAIL):       binds but selects different (p,q) or R*r.
  INCONCLUSIVE:   doesn't bind even on Cosserat -> the L3 hard problem persists.

Branch: analysis/alpha-cosserat-binding (off main; do NOT merge).
Skills: substrate-native-check, phase-space-coordinate-check,
ave-canonical-source, ave-driver-script-honesty.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.cosserat_field_3d import CosseratField3D

# ----------------------------------------------------------------------
# alpha-free configuration (NO Golden-Torus / alpha / charge constants)
# ----------------------------------------------------------------------
N_LATTICE = 48          # interior lattice cells per axis
PML = 4                 # Cosserat-sector PML thickness (cells); excluded everywhere
MAX_ITER = 1500         # relax_s11 budget
SEED_AMPLITUDE = 0.30   # peak |omega| seed amplitude (fraction of omega_yield);
                        #   the bound-state amplitude per doc 34_ section 9.4
                        #   X4a/X4b; NOT a geometric posit (a confinement set-point).

# Generic, ROUND-NEUTRAL seed geometry. NOT the Golden Torus.
#   Golden Torus would be R/r ~ 2.618, R*r = 1/4. We seed AWAY from that: a
#   generic standard torus R/r = 3, R/r both set only by lattice fit (R ~ N/4).
#   These are the "do NOT pre-set" values; relax_s11 must MOVE them if it
#   selects anything.
R_SEED_GENERIC = float(N_LATTICE) / 4.0     # ~ 12 cells -- lattice-fit, not phi
R_OVER_r_SEED = 3.0                         # generic round ratio (!= phi^2)
r_SEED_GENERIC = R_SEED_GENERIC / R_OVER_r_SEED

RNG_SEED = 20260602     # random-direction baseline seed


# ----------------------------------------------------------------------
# Runtime guard: forbidden-token self-audit (mirrors the prior FDTD driver)
# ----------------------------------------------------------------------
# The geometry / cell / winding measures must NOT consume alpha, charge, PHI, or
# the Golden-Torus constants as inputs. This scans THIS source file's measure
# functions (by name) for any forbidden token, so a future edit that smuggles
# alpha into a measure trips the guard at runtime, not at review time.
_FORBIDDEN_TOKENS = (
    "ALPHA", "ALPHA_COLD", "ALPHA_COLD_INV", "V_SNAP", "XI_TOPO",
    "e_charge", "E_CHARGE", "PHI", "R_GOLDEN_TORUS", "GOLDEN_TORUS",
)
# Functions whose bodies are forbidden from referencing the tokens above.
# (Seeders + measures + adjudication. The module docstring legitimately NAMES
#  phi/Golden-Torus to describe the guard, so the docstring is excluded by
#  scanning function source only.)
_GUARDED_FUNCS = (
    "seed_generic_2_3_omega",
    "seed_random_baseline",
    "measure_winding_pq",
    "measure_Rr_phase_space",
    "measure_binding_fwhm",
    "measure_neff_participation",
    "adjudicate",
)


def _self_audit_no_forbidden_tokens() -> None:
    """Scan the guarded functions source for forbidden tokens. Hard-fail if any
    geometry/cell/winding measure consumes alpha / charge / PHI / Golden-Torus."""
    import ast
    import inspect
    import textwrap

    # Resolve this module robustly (works whether run as __main__ or imported
    # under any name): use the audit function's own module record.
    this_mod = sys.modules.get(_self_audit_no_forbidden_tokens.__module__)
    if this_mod is None:  # last-resort fallback
        this_mod = sys.modules[__name__]

    forbidden = set(_FORBIDDEN_TOKENS)
    violations: list[str] = []
    for fname in _GUARDED_FUNCS:
        fn = getattr(this_mod, fname, None)
        if fn is None:
            continue
        # Parse the function and collect IDENTIFIERS actually used in code --
        # ast.Name (variable/constant refs) and ast.Attribute (x.ALPHA). This
        # ignores comments AND docstrings/explanatory string literals, so a NOTE
        # that NAMES a forbidden token (to describe the guard) does not self-trip;
        # only a token USED AS A VALUE in a measure is caught.
        tree = ast.parse(textwrap.dedent(inspect.getsource(fn)))
        used: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                used.add(node.id)
            elif isinstance(node, ast.Attribute):
                used.add(node.attr)
        hits = sorted(used & forbidden)
        for tok in hits:
            violations.append(f"{fname}: forbidden token '{tok}'")
    if violations:
        raise RuntimeError(
            "GUARD TRIPPED -- forbidden token in a geometry/cell/winding measure:\n  "
            + "\n  ".join(violations)
        )
    print("  [guard] token self-audit PASS: no alpha/charge/PHI/Golden-Torus in measures")


def _build_solver() -> CosseratField3D:
    """Cosserat micropolar engine, alpha-free. Total grid = interior + 2*PML so
    the interior is N_LATTICE cells with a PML collar excluded from all
    measures. use_saturation=True activates the omega_yield = pi Ax4 latch."""
    n_total = N_LATTICE + 2 * PML
    return CosseratField3D(
        n_total, n_total, n_total,
        dx=1.0,
        use_saturation=True,
        pml_thickness=PML,
    )


# ----------------------------------------------------------------------
# Seeders
# ----------------------------------------------------------------------
def seed_generic_2_3_omega(solver: CosseratField3D) -> None:
    """Seed a GENERIC (2,3) micro-spin (omega) winding at round-neutral (R, r) --
    NOT the Golden Torus. Also seed the u displacement sector with the same
    winding (the C-state of the translational LC pair) so the (u, omega)
    reactance plane is populated on both axes from the start.

    The (2,3) winding (theta = 2*phi + 3*psi) is the topological CLASS we seed;
    whether relax_s11 PRESERVES (2,3) or selects a different (p,q) is the test.
    The (R, r) are generic (R/r = 3, R*r = R_SEED*r_SEED != 1/4); whether
    relax_s11 moves them toward R*r = 1/4 is the test."""
    # omega sector (L-state of the rotational LC pair) -- generic (2,3).
    solver.initialize_2_3_torus_knot_sector(
        R_target=R_SEED_GENERIC,
        r_target=r_SEED_GENERIC,
        use_hedgehog=True,
        amplitude_scale=SEED_AMPLITUDE,
    )
    omega_seed = solver.omega.copy()
    # u sector (C-state of the translational LC pair) -- same generic (2,3).
    solver.initialize_u_displacement_2_3_sector(
        R_target=R_SEED_GENERIC,
        r_target=r_SEED_GENERIC,
        amplitude_scale=0.5 * SEED_AMPLITUDE,
    )
    # initialize_u_... zeros omega; restore the omega seed so BOTH are populated.
    solver.omega = omega_seed
    solver._zero_outside_alive()


def seed_random_baseline(solver: CosseratField3D) -> None:
    """Random-direction baseline: same per-site |omega| energy budget as the
    generic seed but RANDOM orientation (no toroidal winding). This is the
    dispersal control -- a non-topological blob should NOT bind. Built by taking
    the generic seed magnitude profile and randomizing the direction at each
    site."""
    rng = np.random.default_rng(RNG_SEED)
    # Reuse the generic seed magnitude envelope (so the energy budget matches).
    solver.initialize_2_3_torus_knot_sector(
        R_target=R_SEED_GENERIC,
        r_target=r_SEED_GENERIC,
        use_hedgehog=True,
        amplitude_scale=SEED_AMPLITUDE,
    )
    mag = np.sqrt(np.sum(solver.omega**2, axis=-1, keepdims=True))  # (N,N,N,1)
    rand_dir = rng.normal(size=solver.omega.shape)                  # (N,N,N,3)
    rand_norm = np.sqrt(np.sum(rand_dir**2, axis=-1, keepdims=True))
    rand_norm = np.where(rand_norm > 1e-12, rand_norm, 1.0)
    solver.omega = mag * (rand_dir / rand_norm)
    # match the u-sector budget too, randomized
    mag_u = 0.5 * mag
    rand_dir_u = rng.normal(size=solver.u.shape)
    rand_norm_u = np.sqrt(np.sum(rand_dir_u**2, axis=-1, keepdims=True))
    rand_norm_u = np.where(rand_norm_u > 1e-12, rand_norm_u, 1.0)
    solver.u = mag_u * (rand_dir_u / rand_norm_u)
    solver._zero_outside_alive()


# ----------------------------------------------------------------------
# Measures
# ----------------------------------------------------------------------
def _interior_mask(solver: CosseratField3D) -> np.ndarray:
    """Boolean (N,N,N) mask: alive sites strictly inside the PML collar.
    PML cells (d < pml_thickness from any face) are EXCLUDED -- they carry
    frozen-absorbing artifact, not interior physics (Rule 10 corollary)."""
    nx, ny, nz = solver.nx, solver.ny, solver.nz
    i, j, k = solver._i, solver._j, solver._k
    p = solver.pml_thickness
    d = np.minimum.reduce([
        np.minimum(i, nx - 1 - i),
        np.minimum(j, ny - 1 - j),
        np.minimum(k, nz - 1 - k),
    ])
    return solver.mask_alive & (d >= p)


def measure_winding_pq(solver: CosseratField3D) -> dict:
    """Read the (p, q) winding of the relaxed omega micro-spin field.

    q (the toroidal/poloidal winding around the minor cycle) is the engine
    extract_crossing_count -- the phase winding of omega_x + i*omega_y around
    toroidal contours. p (winding around the major cycle / azimuthal) is read
    by the same phase-unwrap on the major ring. This is the (2,3)-vs-other
    selection axis, measured ON the omega field where the Cosserat winding lives.
    NO alpha / charge / geometry constants enter."""
    q = int(solver.extract_crossing_count())

    # p: azimuthal winding of (omega_x, omega_y) phase around the major ring at
    # the dominant shell radius, on the mid-plane.
    R_found, _ = solver.extract_shell_radii()
    cx, cy, cz = (solver.nx - 1) / 2.0, (solver.ny - 1) / 2.0, (solver.nz - 1) / 2.0
    n_phi = 256
    phis = np.linspace(0.0, 2.0 * np.pi, n_phi, endpoint=False)
    xs = cx + R_found * np.cos(phis)
    ys = cy + R_found * np.sin(phis)
    zs = cz + np.zeros_like(phis)
    ix = np.clip(xs.astype(int), 0, solver.nx - 2)
    iy = np.clip(ys.astype(int), 0, solver.ny - 2)
    iz = np.clip(zs.astype(int), 0, solver.nz - 2)
    ox = solver.omega[ix, iy, iz, 0]
    oy = solver.omega[ix, iy, iz, 1]
    amp = np.sqrt(ox**2 + oy**2)
    if float(amp.max()) < 1e-12:
        p = 0
        p_reliable = 0.0
    else:
        phase = np.unwrap(np.arctan2(oy, ox))
        p = int(round(abs((phase[-1] - phase[0]) / (2.0 * np.pi))))
        p_reliable = float(amp.min() / max(amp.max(), 1e-12))

    return {
        "p_major_winding": p,
        "q_minor_winding": q,
        "p_reliability": p_reliable,
        "is_2_3": bool(p == 2 and q == 3),
    }


def measure_Rr_phase_space(solver: CosseratField3D) -> dict:
    """PRIMARY measure (A46 phase-space fix): R, r, and the product R*r in the
    (u, omega) Cosserat reactance plane, NOT real-space lattice cells.

    The (u, omega) reactance pair is the Cosserat LC: u = translational
    (C-state-analog) and omega = microrotational (L-state-analog). For the
    relaxed soliton, the reactance-plane torus is characterized by, at each
    alive interior site, the joint amplitude pair (|u|, |omega|). The mode traces
    a closed locus in this plane (a torus in phase-space); its geometry is:
       R_phase = radius of the locus centroid from the (u, omega) origin
                 (the standing reactance the mode parks on)
       r_phase = RMS spread of the locus about that centroid (the swing)
    The corpus phase-space claim is R_phase / r_phase ~ phi^2 (R*r ~ 1/4 in
    natural reactance units). We report whatever comes out -- forward, not fit.

    NOTE: 'omega' is the variable name solver.omega (NOT the alpha-bearing
    constants the guard forbids); the guard scans for alpha/charge/PHI tokens,
    which do not appear here."""
    interior = _interior_mask(solver)
    u_mag = np.sqrt(np.sum(solver.u**2, axis=-1))[interior]       # |u| per site
    w_mag = np.sqrt(np.sum(solver.omega**2, axis=-1))[interior]   # |omega| per site

    # Energy-weight the locus by the joint reactive content so empty-vacuum
    # sites (|u|=|omega|=0) do not dominate the centroid.
    weight = u_mag**2 + w_mag**2
    wsum = float(weight.sum())
    if wsum < 1e-30:
        return {
            "R_phase": 0.0, "r_phase": 0.0, "R_times_r_phase": 0.0,
            "R_over_r_phase": 0.0, "n_active_sites": 0,
        }
    # Reactance-plane coordinates: (a, b) = (|u|, |omega|). Normalize each axis
    # to its weighted RMS so the plane is dimensionless reactance (u and omega
    # carry different natural units; the torus geometry is in normalized
    # reactance, matching the corpus dimensionless R/r claim).
    a_rms = np.sqrt(float(np.sum(weight * u_mag**2) / wsum)) or 1.0
    b_rms = np.sqrt(float(np.sum(weight * w_mag**2) / wsum)) or 1.0
    a = u_mag / a_rms
    b = w_mag / b_rms
    # Radial coordinate of each site in the normalized reactance plane.
    radius = np.sqrt(a**2 + b**2)
    R_phase = float(np.sum(weight * radius) / wsum)               # centroid radius
    var = float(np.sum(weight * (radius - R_phase) ** 2) / wsum)
    r_phase = float(np.sqrt(max(var, 0.0)))                       # RMS swing
    return {
        "R_phase": R_phase,
        "r_phase": r_phase,
        "R_times_r_phase": R_phase * r_phase,
        "R_over_r_phase": R_phase / max(r_phase, 1e-12),
        "n_active_sites": int((weight > 1e-12 * weight.max()).sum()),
    }


def measure_binding_fwhm(solver: CosseratField3D) -> dict:
    """Binding (real-space): the energy-density FWHM of the relaxed |omega|^2
    distribution, interior-only. A bound soliton holds a finite FWHM; a
    dispersing blob spreads toward the (interior) box size. Returns the FWHM
    (in cells) of the radial |omega|^2 profile about the field's energy
    centroid, plus the peak-localization fraction (top-K density vs total)."""
    interior = _interior_mask(solver)
    w2 = np.sum(solver.omega**2, axis=-1)
    w2_int = np.where(interior, w2, 0.0)
    total = float(w2_int.sum())
    if total < 1e-30:
        return {"fwhm_cells": float(solver.nx), "peak_frac_top64": 0.0, "total_w2": 0.0}

    # density-peak sampling (not centroid-of-shell): top-K interior cells.
    flat = w2_int.ravel()
    k = min(64, int((flat > 0).sum()))
    topk = np.sort(flat)[-k:] if k > 0 else np.array([0.0])
    peak_frac = float(topk.sum() / total)

    # radial FWHM about the energy centroid (interior).
    idx = np.indices(w2_int.shape)
    cx = float((idx[0] * w2_int).sum() / total)
    cy = float((idx[1] * w2_int).sum() / total)
    cz = float((idx[2] * w2_int).sum() / total)
    rr = np.sqrt((idx[0] - cx) ** 2 + (idx[1] - cy) ** 2 + (idx[2] - cz) ** 2)
    rr_int = rr[interior]
    w2_vals = w2[interior]
    rmax = float(rr_int.max()) if rr_int.size else float(solver.nx)
    nb = max(8, int(round(rmax)))
    edges = np.linspace(0.0, rmax, nb + 1)
    hist, _ = np.histogram(rr_int, bins=edges, weights=w2_vals)
    centers = 0.5 * (edges[:-1] + edges[1:])
    if hist.max() <= 0:
        return {"fwhm_cells": float(solver.nx), "peak_frac_top64": peak_frac, "total_w2": total}
    half = 0.5 * hist.max()
    above = centers[hist >= half]
    fwhm = float(above[-1] - above[0]) if above.size >= 2 else 0.0
    return {"fwhm_cells": fwhm, "peak_frac_top64": peak_frac, "total_w2": total}


def measure_neff_participation(solver: CosseratField3D) -> dict:
    """SECONDARY (REAL-space; the 137 claim is phase-space per A46 -- report,
    do NOT over-interpret). Threshold-free participation number of the relaxed
    |omega|^2 density, interior-only (PML excluded):
        N_eff = (sum rho)^2 / sum(rho^2)     [inverse participation ratio]
    This is the effective number of cells carrying the mode. NO alpha / charge /
    geometry constants enter -- it is a pure functional of the density."""
    interior = _interior_mask(solver)
    rho = np.sum(solver.omega**2, axis=-1)[interior].astype(np.float64)
    s1 = float(rho.sum())
    s2 = float((rho**2).sum())
    if s2 < 1e-300 or s1 <= 0.0:
        return {"n_eff": 0.0, "n_interior_cells": int(interior.sum())}
    return {"n_eff": float(s1 * s1 / s2), "n_interior_cells": int(interior.sum())}


def _saturation_at_peaks(solver: CosseratField3D, k: int = 32) -> dict:
    """Op14 local-clock diagnostic: A^2_local = (|omega| / omega_yield)^2 at the
    top-K interior density sites, and the implied local clock factor
    sqrt(1 - A^2). omega_yield is alpha-free (= pi). Reports whether the mode is
    saturation-latched (A^2 -> 1 freezes the local clock)."""
    interior = _interior_mask(solver)
    w_mag = np.sqrt(np.sum(solver.omega**2, axis=-1))
    w_int = np.where(interior, w_mag, 0.0).ravel()
    kk = min(k, int((w_int > 0).sum()))
    if kk == 0:
        return {"A2_local_mean": 0.0, "A2_local_max": 0.0, "clock_factor_min": 1.0}
    top = np.sort(w_int)[-kk:]
    A2 = (top / solver.omega_yield) ** 2
    return {
        "A2_local_mean": float(A2.mean()),
        "A2_local_max": float(A2.max()),
        "clock_factor_min": float(np.sqrt(max(0.0, 1.0 - A2.max()))),
    }


def adjudicate(generic: dict, baseline: dict) -> dict:
    """Map the measured results to outcome A / B / C / INCONCLUSIVE.

    Binding criterion: the generic-seed mode holds a finite FWHM AND localizes
    (top-K density fraction) markedly better than the random-direction baseline.
    Selection criterion: (p, q) == (2, 3) AND R*r_phase within tolerance of 1/4.

    A (LIFT):       binds AND selects (2,3) AND R*r_phase ~ 1/4.
    B (RELOCATION): (handled by the separate seeded-at-GT control in a follow-up
                    run; this single-driver run reports A vs C vs INCONCLUSIVE.
                    A 'B' verdict requires the GT-seeded control, flagged below.)
    C (FAIL):       binds but (p,q) != (2,3) OR R*r_phase far from 1/4.
    INCONCLUSIVE:   does not bind (disperses like / worse than baseline).
    NO alpha / charge / geometry constants enter the adjudication."""
    gb = generic["binding"]
    bb = baseline["binding"]
    gpq = generic["winding"]
    grr = generic["Rr_phase"]

    # Binding: finite FWHM that is a meaningful fraction below interior box size,
    # AND better peak-localization than the random baseline.
    box = float(N_LATTICE)
    finite_fwhm = (gb["fwhm_cells"] > 0.0) and (gb["fwhm_cells"] < 0.75 * box)
    localizes_better = gb["peak_frac_top64"] > 1.25 * max(bb["peak_frac_top64"], 1e-9)
    holds_energy = gb["total_w2"] > 0.5 * bb["total_w2"]  # not drained to PML
    binds = bool(finite_fwhm and localizes_better and holds_energy)

    is_23 = bool(gpq["is_2_3"])
    # R*r ~ 1/4 tolerance (forward-not-fit: 20% band, reported regardless).
    rr = grr["R_times_r_phase"]
    rr_quarter = bool(abs(rr - 0.25) <= 0.20 * 0.25) if rr > 0 else False

    if not binds:
        outcome = "INCONCLUSIVE"
        reason = (
            "Does NOT bind even on the Cosserat engine -- the generic (2,3) "
            "micro-spin seed disperses (FWHM/localization not better than the "
            "random baseline). The L3 bound-state hard problem persists: the "
            "lattice-as-modeled does not bind the (2,3) Cosserat soliton from a "
            "generic seed."
        )
    elif is_23 and rr_quarter:
        outcome = "A"
        reason = (
            "LIFT: binds from a generic seed AND selects (p,q)=(2,3) with "
            "R*r_phase ~ 1/4 in the (u,omega) reactance plane, alpha-free -- the "
            "lattice forces the embedding. (Confirm vs a GT-seeded control to "
            "rule out coincidental selection; see B-control flag.)"
        )
    else:
        outcome = "C"
        bits = []
        if not is_23:
            bits.append(f"selected (p,q)=({gpq['p_major_winding']},{gpq['q_minor_winding']}) != (2,3)")
        if not rr_quarter:
            bits.append(f"R*r_phase = {rr:.4f} (not ~1/4)")
        reason = (
            "FAIL: binds but does NOT select the corpus embedding -- "
            + "; ".join(bits)
            + ". alpha = 1/Q is not THIS Cosserat mode's geometric selection."
        )

    return {
        "outcome": outcome,
        "reason": reason,
        "binds": binds,
        "binding_detail": {
            "finite_fwhm": finite_fwhm,
            "localizes_better_than_baseline": localizes_better,
            "holds_energy_vs_baseline": holds_energy,
        },
        "selects_2_3": is_23,
        "R_times_r_phase": rr,
        "R_times_r_near_quarter": rr_quarter,
    }


def _run_arm(name: str, seeder) -> dict:
    """Seed -> relax_s11 (S11-min) -> measure. Returns the pre/post bundle."""
    print(f"\n--- arm: {name} ---", flush=True)
    solver = _build_solver()
    seeder(solver)

    pre = {
        "winding": measure_winding_pq(solver),
        "Rr_phase": measure_Rr_phase_space(solver),
        "binding": measure_binding_fwhm(solver),
        "neff": measure_neff_participation(solver),
        "s11": solver.total_s11(),
    }
    print(
        f"  seed:  (p,q)=({pre['winding']['p_major_winding']},"
        f"{pre['winding']['q_minor_winding']})  "
        f"R*r_phase={pre['Rr_phase']['R_times_r_phase']:.4f}  "
        f"FWHM={pre['binding']['fwhm_cells']:.2f}  "
        f"peakfrac={pre['binding']['peak_frac_top64']:.4f}  "
        f"N_eff={pre['neff']['n_eff']:.1f}  S11={pre['s11']:.4e}",
        flush=True,
    )

    result = solver.relax_s11(
        max_iter=MAX_ITER, tol=1e-8, initial_lr=0.01, verbose=False,
    )

    post = {
        "winding": measure_winding_pq(solver),
        "Rr_phase": measure_Rr_phase_space(solver),
        "binding": measure_binding_fwhm(solver),
        "neff": measure_neff_participation(solver),
        "saturation": _saturation_at_peaks(solver),
        "s11": result["final_s11"],
        "s11_converged": bool(result["converged"]),
        "s11_iters": int(result["iterations"]),
    }
    print(
        f"  relax: (p,q)=({post['winding']['p_major_winding']},"
        f"{post['winding']['q_minor_winding']})  "
        f"R*r_phase={post['Rr_phase']['R_times_r_phase']:.4f}  "
        f"R/r_phase={post['Rr_phase']['R_over_r_phase']:.3f}  "
        f"FWHM={post['binding']['fwhm_cells']:.2f}  "
        f"peakfrac={post['binding']['peak_frac_top64']:.4f}  "
        f"N_eff={post['neff']['n_eff']:.1f}",
        flush=True,
    )
    print(
        f"         S11 {pre['s11']:.4e} -> {post['s11']:.4e}  "
        f"[{post['s11_iters']} iter, conv={post['s11_converged']}]  "
        f"A^2_local(max)={post['saturation']['A2_local_max']:.3f}  "
        f"clock_min={post['saturation']['clock_factor_min']:.3f}",
        flush=True,
    )
    return {"pre": pre, "post": post}


def main() -> None:
    print("=" * 78, flush=True)
    print("  alpha Class-2 lift -- Cosserat micropolar binding + geometry selection")
    print("  Engine: CosseratField3D (micro-spin omega DOF, omega_yield=pi, S11-min)")
    print(f"  N_interior={N_LATTICE}  PML={PML}  max_iter={MAX_ITER}")
    print("=" * 78, flush=True)

    _self_audit_no_forbidden_tokens()

    print(
        f"\n  Generic seed (NOT Golden Torus): R={R_SEED_GENERIC:.3f}, "
        f"r={r_SEED_GENERIC:.3f}, R/r={R_OVER_r_SEED:.2f}, "
        f"R*r={R_SEED_GENERIC * r_SEED_GENERIC:.3f} (!= 1/4), "
        f"peak|omega|={SEED_AMPLITUDE:.3f}*omega_yield",
        flush=True,
    )

    generic = _run_arm("GENERIC (2,3) micro-spin seed", seed_generic_2_3_omega)
    baseline = _run_arm("RANDOM-direction baseline", seed_random_baseline)

    verdict = adjudicate(generic["post"], baseline["post"])

    print("\n" + "=" * 78, flush=True)
    print("  ADJUDICATION")
    print("=" * 78, flush=True)
    print(f"  OUTCOME: {verdict['outcome']}")
    print(f"  {verdict['reason']}")
    print()
    print("  --- measure summary (relaxed generic-seed mode) ---")
    gp = generic["post"]
    print(
        f"  PRIMARY (phase-space, A46 fix): (p,q)=("
        f"{gp['winding']['p_major_winding']},{gp['winding']['q_minor_winding']})"
        f"  R*r_phase={gp['Rr_phase']['R_times_r_phase']:.4f}"
        f"  R/r_phase={gp['Rr_phase']['R_over_r_phase']:.3f}"
    )
    print(
        f"  BINDING (real-space): FWHM={gp['binding']['fwhm_cells']:.2f} cells"
        f"  peak_frac={gp['binding']['peak_frac_top64']:.4f}  "
        f"(baseline peak_frac={baseline['post']['binding']['peak_frac_top64']:.4f})"
    )
    print(
        f"  SECONDARY (REAL-space N_eff; 137 claim is phase-space, do NOT "
        f"over-interpret): N_eff={gp['neff']['n_eff']:.1f} of "
        f"{gp['neff']['n_interior_cells']} interior cells"
    )
    print()
    print("  *** B-control flag: a full Outcome-B (relocation) verdict requires a")
    print("      SECOND run seeded AT the Golden Torus (R/r=phi^2) to check that")
    print("      (2,3)+1/4 appears ONLY when seeded there. This driver runs the")
    print("      generic + random arms; the GT-seeded control is a separate run.")
    print()
    print("  *** Coordinate flag (flag-don't-fix): the corpus phi^2 phase-space")
    print("      claim (doc 28 5.1) is in K4 (V_inc,V_ref), NOT the (u,omega)")
    print("      Cosserat plane measured here. See module docstring + report.")

    return {"generic": generic, "baseline": baseline, "verdict": verdict}


if __name__ == "__main__":
    main()
