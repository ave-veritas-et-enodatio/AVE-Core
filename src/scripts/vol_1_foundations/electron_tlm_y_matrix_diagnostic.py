"""
Phase B — TLM-extracted Y-matrix diagnostic for the L3 electron.

Item 2 of `L3_PHASE3_NEXT_STEPS_PLAN_20260421.md` Phase B step.

Runs the existing TLM electron-soliton script (Phase 3 from prior
sessions) and adds a diagnostic that:

1. Identifies the 3 crossings of the (2,3) winding using the projected-
   coincidence detector (validated in Phase A
   electron_y_matrix_prototype.py).
2. Extracts the local impedance Z_eff/Z_0 at each crossing site from
   the TLM lattice's `z_local_field` (populated by op3_bond_reflection).
3. Builds a 3x3 chirality-signed Y-matrix using these TLM-derived
   impedances.
4. Computes lambda_min(S^dagger S) as a bound-state diagnostic.
5. Reports the trajectory across multiple TLM amplitudes.

Pre-registered prediction: at the amplitude where the (2,3) eigenmode
is closest to bound, lambda_min should be smallest. The amplitude
producing minimum lambda_min should also produce extracted alpha^-1
closest to 137.

This is a DIAGNOSTIC (not yet an iterative outer loop). If the
diagnostic shows lambda_min has a clear minimum vs amplitude that
correlates with alpha^-1 -> 137, that validates the framework before
implementing the full Phase C outer loop.
"""

import numpy as np

from ave.core.constants import ALPHA, ALPHA_COLD_INV
from ave.core.universal_operators import (
    universal_eigenvalue_target,
    universal_ymatrix_to_s,
)

# Import from the existing TLM script (run_tlm_electron) and Phase A
# prototype (find_crossings).
from scripts.vol_1_foundations.tlm_electron_soliton_eigenmode import (
    run_tlm_electron,
    extract_alpha_inverse,
    PHI,
)
from scripts.vol_1_foundations.electron_y_matrix_prototype import (
    find_crossings,
    generate_torus_knot_path,
    knot_tangent,
)


def extract_z_at_crossings(lattice, crossings, path):
    """Extract local impedance Z_eff/Z_0 from the TLM lattice at each
    crossing midpoint.

    The lattice has `z_local_field[i, j, k]` populated by Op3-bond-reflection
    pre-step (per `_update_z_local_field` at k4_tlm.py:196-221).

    For each crossing, take the midpoint of (path[i], path[j]) in 3D
    Cartesian, find the nearest active K4 lattice site, and read
    z_local_field there.

    Returns array of length N_crossings of normalized impedances.
    """
    cx = (lattice.nx - 1) / 2.0
    cy = (lattice.ny - 1) / 2.0
    cz = (lattice.nz - 1) / 2.0

    if not hasattr(lattice, "z_local_field"):
        # Force a z_local_field update (must have run TLM with op3_bond_reflection)
        lattice._update_z_local_field()

    z_at = []
    for i, j, _, _ in crossings:
        midpoint = (path[i] + path[j]) / 2.0
        # Lattice indexing: midpoint is in normalized units (Golden Torus
        # natural units); scale to lattice coords.
        # The TLM uses lattice units where dx=1 and the soliton's R_lat is
        # set explicitly; we assume the midpoint coords are in the same
        # lattice units (scaled to fit the TLM box).
        # For safety, clip to box and round to nearest cell.
        ix = int(round(midpoint[0] + cx))
        iy = int(round(midpoint[1] + cy))
        iz = int(round(midpoint[2] + cz))
        ix = max(0, min(lattice.nx - 1, ix))
        iy = max(0, min(lattice.ny - 1, iy))
        iz = max(0, min(lattice.nz - 1, iz))
        z_local = float(lattice.z_local_field[ix, iy, iz])
        z_at.append(z_local)

    return np.array(z_at)


def build_tlm_y_matrix(crossings, z_at_crossings, p, q):
    """Build chirality-signed Y matrix using TLM-extracted impedances.

    Encoding (per chirality projection sub-theorem 3.1.1 with TLM-
    derived per-crossing impedances):
      Y_ii = 1 / Z_local_i   (admittance at crossing i, from TLM)
      Y_ij = -chi_i * chi_j * alpha / (Z_local_i * Z_local_j)^0.5
             (chirality-signed coupling, normalized to mean impedance)

    The bound-state condition lambda_min(S^dagger S) = 0 holds when
    the impedance pattern across the 3 crossings creates a perfect
    standing wave on the (2,3) topological sector.
    """
    N = len(crossings)
    Y = np.zeros((N, N), dtype=complex)

    chi = np.array([c[2] for c in crossings])
    z = z_at_crossings

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            # Mutual admittance: chirality-signed, normalized
            Y[i, j] = -chi[i] * chi[j] * ALPHA / np.sqrt(z[i] * z[j])
        # Self admittance: TLM-derived local + sum of off-diagonals
        Y[i, i] = 1.0 / z[i] - np.sum(Y[i, :])

    return Y


def compute_lambda_min(Y):
    """Compute lambda_min(S^dagger S) from Y via Op5 + Op6."""
    S = universal_ymatrix_to_s(Y, Y0=1.0)
    return float(universal_eigenvalue_target(S))


def diagnose_amplitude_sweep(N=48, R_lat=12.0, r_lat=4.58, p=2, q=3,
                             amplitudes=None, n_steps=200,
                             pml_thickness=0):
    """Sweep TLM amplitude, compute lambda_min and alpha^-1 at each."""
    if amplitudes is None:
        amplitudes = [0.05, 0.10, 0.20, 0.40, 0.60, 0.80, 0.95]

    # Lattice-scale R, r need to be converted to "natural Golden Torus
    # units" where R = phi/2 ≈ 0.809 for crossing detection. Since the
    # TLM evolves at lattice scale (R_lat ≈ 12 cells), the crossings are
    # at lattice coords scaled accordingly.
    # Generate crossings in lattice coords using R_lat, r_lat.
    n_path_points = 1000
    path, t_param = generate_torus_knot_path(p, q, R_lat, r_lat, n_path_points)
    tangents = knot_tangent(p, q, R_lat, r_lat, t_param)

    # Crossing thresholds scaled by lattice
    xy_thresh = 0.5  # ~ half a lattice cell
    z_sep_thresh = 1.0  # at least one lattice cell
    cluster_radius = 5.0  # several cells

    crossings = find_crossings(
        path, t_param, tangents,
        xy_threshold=xy_thresh,
        z_separation_threshold=z_sep_thresh,
        path_separation_threshold=1.0,
        cluster_radius=cluster_radius,
    )
    print(f"\nFound {len(crossings)} crossings at lattice scale "
          f"(R_lat={R_lat}, r_lat={r_lat})")
    for k, (i, j, chi, d) in enumerate(crossings):
        mid = (path[i] + path[j]) / 2.0
        print(f"  Crossing {k+1}: t=({t_param[i]:.3f}, {t_param[j]:.3f}) "
              f"chi={chi:+.0f}  midpoint=({mid[0]:+.2f}, {mid[1]:+.2f}, {mid[2]:+.2f})")

    if len(crossings) < 3:
        print(f"WARN: expected 3 crossings, found {len(crossings)}. Check thresholds.")
        return []

    # Sweep amplitudes
    print(f"\n{'amp/V_SNAP':<14}{'R_rms':<10}{'r_rms':<10}{'R/r':<10}"
          f"{'alpha_inv':<14}{'lambda_min':<14}{'Q_est':<10}")
    print("-" * 82)

    results = []
    for amp in amplitudes:
        # Run TLM
        result = run_tlm_electron(
            N=N, R=R_lat, r=r_lat, n_steps=n_steps,
            amplitude=amp, pml_thickness=pml_thickness,
            sample_every=n_steps + 1,  # suppress per-step prints
            verbose=False, op3_bond_reflection=True,
            rms_avg_last_n=max(50, n_steps // 3),
        )
        R_rms = result["R_rms"]
        r_rms = result["r_rms"]
        Rr_ratio = R_rms / max(r_rms, 1e-9)
        alpha_dict = extract_alpha_inverse(R_rms, r_rms, c=3)
        alpha_inv = alpha_dict["alpha_inv"] if alpha_dict["valid"] else float("nan")

        # Extract impedances at crossings
        lattice = result["lattice"]
        z_at = extract_z_at_crossings(lattice, crossings, path)

        # Build Y, compute lambda_min
        Y = build_tlm_y_matrix(crossings, z_at, p, q)
        lambda_min = compute_lambda_min(Y)
        Q_est = 1.0 / np.sqrt(lambda_min + 1e-30)

        results.append({
            "amp": amp,
            "R_rms": R_rms,
            "r_rms": r_rms,
            "R_over_r": Rr_ratio,
            "alpha_inv": alpha_inv,
            "lambda_min": lambda_min,
            "Q_est": Q_est,
            "z_at_crossings": z_at,
        })
        print(f"{amp:<14.2f}{R_rms:<10.3f}{r_rms:<10.3f}{Rr_ratio:<10.3f}"
              f"{alpha_inv:<14.3f}{lambda_min:<14.6e}{Q_est:<10.2f}")

    return results


def main():
    print("=" * 82)
    print("Phase B — TLM-extracted Y-matrix diagnostic for L3 electron")
    print("=" * 82)
    print(f"\nTarget: alpha^-1 = {ALPHA_COLD_INV:.4f} = 4*pi^3 + pi^2 + pi (Ch 8)")
    print(f"Pre-registered prediction: minimum lambda_min should correlate")
    print(f"with alpha^-1 closest to 137 across the amplitude sweep.")

    # Use lattice-scale (R, r) close to the 96^3 Golden-Torus-proportioned
    # geometry from earlier sessions: R/r ~ phi^2 = 2.618.
    PHI_SQ = PHI ** 2  # ~ 2.618
    R_lat = 12.0
    r_lat = R_lat / PHI_SQ  # = 4.583

    results = diagnose_amplitude_sweep(
        N=48,
        R_lat=R_lat,
        r_lat=r_lat,
        amplitudes=[0.10, 0.30, 0.50, 0.70, 0.90],
        n_steps=200,
    )

    print("\n" + "=" * 82)
    print("PHASE B INTERPRETATION")
    print("=" * 82)

    if not results:
        print("No results to interpret (crossing detection failed).")
        return

    # Find amplitude with minimum lambda_min
    min_idx = int(np.argmin([r["lambda_min"] for r in results]))
    min_result = results[min_idx]
    # Find amplitude with alpha_inv closest to 137
    alpha_diffs = [abs(r["alpha_inv"] - ALPHA_COLD_INV) for r in results]
    closest_alpha_idx = int(np.argmin(alpha_diffs))
    closest_alpha_result = results[closest_alpha_idx]

    print(f"\nAmplitude with min lambda_min:    "
          f"amp={min_result['amp']:.2f}  "
          f"lambda_min={min_result['lambda_min']:.4e}  "
          f"alpha^-1={min_result['alpha_inv']:.3f}")
    print(f"Amplitude with alpha^-1 ~ 137:    "
          f"amp={closest_alpha_result['amp']:.2f}  "
          f"alpha^-1={closest_alpha_result['alpha_inv']:.3f}  "
          f"lambda_min={closest_alpha_result['lambda_min']:.4e}")

    if min_idx == closest_alpha_idx:
        print("\nPASS: lambda_min minimum coincides with alpha^-1 closest to 137.")
        print("The Y-matrix diagnostic correctly predicts the bound state.")
    else:
        print("\nINFORMATIVE: lambda_min minimum and alpha^-1 ~ 137 occur at")
        print("different amplitudes. Y-matrix construction needs refinement,")
        print("or the TLM hasn't reached the bound state at any tested amplitude.")
        print("Phase C (full eigenvalue-driven outer loop) is the next step.")


if __name__ == "__main__":
    main()
