"""
Phase-3 validation: does the Cosserat field solver relax to the Golden
Torus from the (2,3) topological sector?

Dual-run protocol per research/_archive/L3_electron_soliton/09_ §4:
  1. Initialize near-exact Golden Torus geometry -> relax -> measure.
  2. Initialize deliberately off-Golden -> relax -> measure.

Both runs should converge to the same (R, r) ratio if the Lagrangian
dynamically selects the Golden Torus.

Validation targets (dimensionless ratios; see note on absolute Q below):
  R / r -> phi^2 ≈ 2.618     (Golden Torus uniqueness)
  (R - r) / d -> 1/2          (Ch 8 self-avoidance at crossings)
  c = 3                       (preserved crossing count)

Absolute alpha^-1 = 4 pi^3 + pi^2 + pi ≈ 137.036 requires working in
Ch 8's natural units where R = phi/2 ≈ 0.81 and r = (phi-1)/2 ≈ 0.31.
On a discrete lattice with ell_node = 1 these are sub-unit; to resolve,
we use dx < 1 and express R, r in grid cells. The MULTIPOLE structure
is scale-free — extracted Q scales predictably with dx — so the
physics claim is validated by the dimensionless ratios, and Q is
reported for completeness.
"""
import numpy as np

from ave.topological.cosserat_field_3d import CosseratField3D


PHI = (1.0 + np.sqrt(5.0)) / 2.0
R_GOLDEN_GRID = 8.0   # grid-cell units; corresponds to ~phi/2 when dx = phi/(2 * R_grid)
R_OVER_R_TARGET = PHI**2  # = phi/(phi-1) — expected (R/r) ratio


def golden_torus_grid_coords(R_grid: float) -> tuple[float, float]:
    """Rescale (phi/2, (phi-1)/2) to put R at R_grid lattice cells."""
    scale = R_grid / (PHI / 2.0)
    return scale * (PHI / 2.0), scale * ((PHI - 1.0) / 2.0)


def run_relaxation(
    nx: int,
    R_init: float,
    r_init: float,
    label: str,
    max_iter: int = 500,
    initial_lr: float = 1e-3,
    use_saturation: bool = True,
) -> dict:
    solver = CosseratField3D(nx, nx, nx, dx=1.0, use_saturation=use_saturation)
    solver.initialize_electron_2_3_sector(R_target=R_init, r_target=r_init)

    E_init = solver.total_energy()
    R_init_obs, r_init_obs = solver.extract_shell_radii()
    c_init = solver.extract_crossing_count()

    result = solver.relax_to_ground_state(
        max_iter=max_iter,
        tol=1e-8,
        initial_lr=initial_lr,
        verbose=False,
    )

    R_final, r_final = solver.extract_shell_radii()
    c_final = solver.extract_crossing_count()
    Q = solver.extract_quality_factor()

    return {
        "label": label,
        "init": (R_init, r_init),
        "initial_E": E_init,
        "initial_observed": (R_init_obs, r_init_obs, c_init),
        "iterations": result["iterations"],
        "converged": result["converged"],
        "final_E": result["final_energy"],
        "final_R": R_final,
        "final_r": r_final,
        "final_c": c_final,
        "final_Q": Q,
    }


def print_run_summary(info: dict) -> None:
    label = info["label"]
    print(f"\n--- {label} ---")
    print(f"  Initial (R, r) target:  ({info['init'][0]:.3f}, {info['init'][1]:.3f})")
    print(f"  Initial (R, r, c) obs:  ({info['initial_observed'][0]:.3f}, {info['initial_observed'][1]:.3f}, c={info['initial_observed'][2]})")
    print(f"  Initial energy:         {info['initial_E']:.6e}")
    print(f"  Iterations:             {info['iterations']}")
    print(f"  Converged:              {info['converged']}")
    print(f"  Final energy:           {info['final_E']:.6e}")
    print(f"  Final (R, r):           ({info['final_R']:.3f}, {info['final_r']:.3f})")
    print(f"  Final c:                {info['final_c']}")
    print(f"  Final Q (grid units):   {info['final_Q']:.3f}")
    if info['final_r'] > 1e-6:
        ratio = info['final_R'] / info['final_r']
        print(f"  R/r ratio:              {ratio:.4f}   (target phi^2 = {PHI**2:.4f})")


def main():
    print("=" * 72)
    print("  Phase-3 Cosserat soliton validation (dual-run protocol)")
    print("=" * 72)

    # Grid setup.
    NX = 32
    R_exact, r_exact = golden_torus_grid_coords(R_GOLDEN_GRID)
    print(f"  Grid:                   {NX}^3")
    print(f"  Exact Golden Torus:     R = {R_exact:.4f}, r = {r_exact:.4f} (grid cells)")
    print(f"  Expected R/r:           {R_exact / r_exact:.4f} (= phi^2)")
    print(f"  Expected (R-r):         {R_exact - r_exact:.4f}")

    print("  Saturation kernel: ACTIVE. Gradient computed via jax.value_and_grad.")

    # Run 1: initialize near exact Golden Torus.
    info_exact = run_relaxation(
        nx=NX,
        R_init=R_exact,
        r_init=r_exact,
        label="Run 1: exact Golden Torus initial guess",
        max_iter=1500,
        initial_lr=1e-2,
    )
    print_run_summary(info_exact)

    # Run 2: deliberately off-Golden.
    info_perturbed = run_relaxation(
        nx=NX,
        R_init=R_exact * 1.3,
        r_init=r_exact * 0.7,
        label="Run 2: perturbed off-Golden (R +30%, r -30%)",
        max_iter=1500,
        initial_lr=1e-2,
    )
    print_run_summary(info_perturbed)

    # Validation report.
    print("\n" + "=" * 72)
    print("  Validation report")
    print("=" * 72)

    for info in (info_exact, info_perturbed):
        ratio = info['final_R'] / max(info['final_r'], 1e-9)
        ratio_error = abs(ratio - PHI**2) / PHI**2
        c_match = (info['final_c'] == 3)
        print(f"  {info['label']}:")
        print(f"    R/r:           {ratio:.4f}   (target {PHI**2:.4f}, rel err {ratio_error*100:.1f}%)")
        print(f"    c preserved?   {c_match}   (target 3, got {info['final_c']})")
        print(f"    Relaxation:    {'converged' if info['converged'] else 'hit iter limit'}")

    print()
    print("=" * 72)
    print("  FINDINGS (Phase-3 pass, saturation ON via JAX autograd)")
    print("=" * 72)
    print("  Good: energy no longer decays to vacuum (was ~1e-13 without")
    print("  saturation; is O(10-100) with saturation). Saturation kernel")
    print("  is providing a real energy barrier.")
    print()
    print("  Problem: (2,3) topology does not survive gradient descent at")
    print("  32^3 resolution. c goes from 3 -> 0 in both runs; R/r ratio")
    print("  does not converge to phi^2. The field is unwinding through")
    print("  the discrete lattice faster than saturation can prevent it.")
    print()
    print("  Likely causes (Phase-3 investigation items):")
    print("  1. Grid too coarse for stable (2,3) winding (try 64^3, 96^3).")
    print("  2. dx = 1.0 too coarse relative to tube minor radius r ~ 3.")
    print("     Refinement via dx < 1 and rescaled R/r may help.")
    print("  3. Plain gradient descent does not preserve topology under")
    print("     lattice tearing. A topology-preserving variant (constrained")
    print("     gradient, projected descent, or Landau-Lifshitz-style")
    print("     precession-plus-damping) may be required.")
    print("  4. c-extraction diagnostic may not be robust to shell")
    print("     deformation. Cross-check via Op11 topological-curl integral.")


if __name__ == "__main__":
    main()
