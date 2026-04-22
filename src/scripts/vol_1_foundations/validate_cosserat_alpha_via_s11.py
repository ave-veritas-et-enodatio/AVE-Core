"""
Phase-3 α⁻¹ validation via S11 minimization on a 3D Cosserat field.

Per the reframing at end of 2026-04-20 session (see L3_PHASE3_SESSION_20260420
handoff): the electron soliton's ground state is a reactive LC tank, not an
energy minimum. The AVE-native objective is S11 minimization (equivalently
Q-factor maximization) at the soliton-bulk boundary.

The parametric S11 minimization is ALREADY verified in
    src/scripts/vol_1_foundations/ropelength_trefoil_golden_torus.py
converging to (R, r) = (φ/2, (φ-1)/2) to 7 decimal places from arbitrary
starts. This script lifts that to a 3D Cosserat field test: initialize the
(2,3) Sutcliffe ansatz parameterized by (R_target, r_target), use the field
to extract the geometric (R, r, d), compute the composite S11 free energy
from those extracted values, and minimize over (R_target, r_target) with
scipy.

If minimization converges to Golden Torus in (R_target, r_target), the
3D Cosserat field version tracks the parametric S11 result — which closes
Phase-3 at the field level via S11 minimization.

This is NOT gradient descent on the full field — the field-extractors
(extract_shell_radii, extract_crossing_count) are not differentiable wrt
the lattice values. Full field-level S11 minimization is the next-session
task and requires differentiable field extractors OR a native field-Gamma
formulation.
"""
import numpy as np
from scipy.optimize import minimize
from scipy.integrate import quad

from ave.topological.cosserat_field_3d import CosseratField3D


PHI = (1.0 + np.sqrt(5.0)) / 2.0
ALPHA_COLD_INV = 4.0 * np.pi**3 + np.pi**2 + np.pi
GOLDEN_R = PHI / 2.0
GOLDEN_r = (PHI - 1.0) / 2.0


def trefoil_speed_squared(t, R, r):
    """|dX/dt|² for the (2,3) torus knot ansatz."""
    return 4.0 * (R + r * np.cos(3.0 * t))**2 + 9.0 * r**2


def trefoil_arc_length(R, r):
    """Arc length L(R, r) of one full traversal of the (2,3) trefoil."""
    integrand = lambda t: np.sqrt(trefoil_speed_squared(t, R, r))
    L, _ = quad(integrand, 0.0, 2.0 * np.pi, limit=200)
    return L


def extract_field_geometry(solver, target_R, target_r):
    """
    Extract (R_field, r_field, d_field) from a relaxed (or initial) field.

    Uses the solver's existing diagnostic methods. Not differentiable wrt
    the field values — intended for scipy-style black-box minimization.
    """
    R_field, r_field = solver.extract_shell_radii()
    # d is the tube diameter. For the Sutcliffe ansatz with localization_sigma = r_target,
    # the natural d is 2 * r_field (tube diameter in grid cells).
    d_field = 2.0 * r_field if r_field > 0 else 1.0
    # Normalize to lattice-unit scale: divide by initial scale so we compare
    # to Ch 8 target values (R - r = 1/2, R·r = 1/4) in the SAME units.
    # Scale such that d -> 1 (Ch 8 Nyquist normalization).
    scale = 1.0 / max(d_field, 1e-6)
    return R_field * scale, r_field * scale, 1.0


def composite_s11_free_energy(R, r,
                               lambda_avoid=1e4,
                               lambda_screen=1e4):
    """
    Composite S11 free energy on the (2,3) trefoil (ropelength + constraints).
    Minimized parametrically by `ropelength_trefoil_golden_torus.py`.
    """
    L = trefoil_arc_length(R, r)
    pen_avoid = lambda_avoid * ((R - r) - 0.5)**2
    pen_screen = lambda_screen * (R * r - 0.25)**2
    return L + pen_avoid + pen_screen


def field_s11_objective(target_params, nx=48, verbose=False):
    """
    Objective: initialize the Cosserat field with the given (R_target, r_target)
    ansatz, extract the field's measured (R, r, d), compute the composite S11
    free energy at the extracted geometry.

    Returns the composite free energy value. scipy minimizes this over
    (R_target, r_target).

    If the Cosserat field tracks the parametric trefoil geometry, minimizing
    this should also converge to Golden Torus.
    """
    R_target, r_target = target_params
    # Reject obviously unphysical inputs
    if R_target <= r_target or r_target <= 0 or R_target <= 0:
        return 1e10
    # Target values are physical radii (Ch 8 natural units). Place them on
    # the grid with a scale factor so they're resolved.
    scale = 8.0  # grid cells per (R=phi/2) unit — gives ~6 cells at Golden r
    R_grid = R_target * scale
    r_grid = r_target * scale
    if R_grid + r_grid + 4 > nx / 2:
        return 1e10

    solver = CosseratField3D(nx, nx, nx, use_saturation=True)
    solver.initialize_electron_2_3_sector(R_target=R_grid, r_target=r_grid)
    R_field, r_field, d_field = extract_field_geometry(solver, R_grid, r_grid)
    if not np.isfinite(R_field) or not np.isfinite(r_field):
        return 1e10
    # Evaluate composite free energy in natural (d=1) units.
    F = composite_s11_free_energy(R_field, r_field,
                                   lambda_avoid=1e4, lambda_screen=1e4)
    if verbose:
        print(f"  (R_t, r_t) = ({R_target:.4f}, {r_target:.4f}) → "
              f"field (R, r, d) = ({R_field:.4f}, {r_field:.4f}, {d_field:.4f})  "
              f"F = {F:.4f}")
    return F


def main():
    print("=" * 78)
    print("  Phase-3 α⁻¹ validation via S11 minimization on 3D Cosserat field")
    print("=" * 78)
    print("  Method: scipy-minimize composite S11 free energy over Sutcliffe")
    print("          ansatz parameters (R_target, r_target); field-extracted")
    print("          (R, r, d) feeds the arc-length + avoidance + screening")
    print("          composite used by ropelength_trefoil_golden_torus.py.")
    print(f"  Golden Torus target: R = {GOLDEN_R:.6f}, r = {GOLDEN_r:.6f}")
    print(f"  α⁻¹ target:          {ALPHA_COLD_INV:.6f}")
    print()

    for initial_guess in [(1.0, 0.2), (0.7, 0.1), (1.3, 0.4)]:
        print(f"--- Initial guess: R = {initial_guess[0]}, r = {initial_guess[1]} ---")
        result = minimize(
            field_s11_objective,
            x0=np.array(initial_guess),
            args=(48, True),
            method='Nelder-Mead',
            options={'xatol': 1e-4, 'fatol': 1e-6, 'maxiter': 50},
        )
        R_found, r_found = result.x
        print(f"  Converged to:   R = {R_found:.6f}, r = {r_found:.6f}")
        print(f"  |R − φ/2| = {abs(R_found - GOLDEN_R):.4e}")
        print(f"  |r − (φ-1)/2| = {abs(r_found - GOLDEN_r):.4e}")
        print(f"  R·r = {R_found * r_found:.6f}  (target 0.25)")
        print(f"  R-r = {R_found - r_found:.6f}  (target 0.5)")
        alpha_inv = 16 * np.pi**3 * (R_found * r_found) + 4 * np.pi**2 * (R_found * r_found) + np.pi
        print(f"  Implied α⁻¹ = {alpha_inv:.6f}  (target {ALPHA_COLD_INV:.6f})")
        print()


if __name__ == "__main__":
    main()
