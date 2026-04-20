"""
Phase-3 α⁻¹ validation via Ch 8 dimensionless ratios.

Per the chirality-accounting resolution (research/L3_electron_soliton/10_):
impedance Z_0 is a scalar (chirality enters only as coupling sign, not
as Z magnitude), so the α⁻¹ validation reduces to checking whether the
three dimensionless Ch 8 ratios emerge from the relaxed Cosserat field:

    1. (R - r) / d         → 1/2    (self-avoidance)
    2. R · r / d^2          → 1/4    (screening / spin-1/2 half-cover)
    3. d_grid               = Nyquist scale (tube diameter in lattice cells)

If these three hold, the multipole Q-factor in natural units (d = 1) is
structurally α⁻¹ = 4π³ + π² + π = 137.0363038 by pure geometry.

The script runs the dual-run protocol at 64³ (where topology is preserved
per earlier finding), extracts the three ratios, and reports deviations
from Ch 8 targets.
"""
import numpy as np

from ave.topological.cosserat_field_3d import CosseratField3D


PHI = (1.0 + np.sqrt(5.0)) / 2.0
ALPHA_COLD_INV = 4 * np.pi**3 + np.pi**2 + np.pi


def golden_torus_grid_coords(R_grid: float) -> tuple[float, float]:
    """Rescale (φ/2, (φ-1)/2) so that R matches R_grid in lattice cells."""
    scale = R_grid / (PHI / 2.0)
    return scale * (PHI / 2.0), scale * ((PHI - 1.0) / 2.0)


def extract_ch8_ratios(solver: CosseratField3D) -> dict:
    """
    Extract R, r, d from the relaxed field and compute Ch 8's three
    dimensionless ratios.

    R = grid-cell location of peak |ω| in the xy plane at z = center
        (major axis of the toroidal shell)
    r = HWHM of |ω| radial profile in the transverse direction
        (approximation to minor tube radius)
    d = estimated tube diameter from |ω| cross-section along the
        minor axis ≈ 2r (if Ch 8 interpretation is "r is tube radius")
    """
    R, r_hwhm = solver.extract_shell_radii()
    # Ch 8 convention: r is the minor-tube radius, d is the diameter.
    # My extractor returns HWHM ≈ 0.83 r_target; multiply by a consistent
    # factor if needed. For now, treat r_hwhm as a rough proxy for
    # "tube half-width," with d_grid ≈ 2·r_hwhm·(calibration factor).
    # Simplest first-pass: assume r_hwhm ≈ r_minor and d ≈ 2 r.
    r = r_hwhm
    d = 2.0 * r
    c = solver.extract_crossing_count()

    # The three Ch 8 ratios:
    ratio_sa = (R - r) / d if d > 1e-9 else float("inf")      # target 1/2
    ratio_scr = R * r / (d * d) if d > 1e-9 else float("inf")  # target 1/4
    Q_grid = solver.extract_quality_factor()
    # Q in natural units (rescaled by 1/d²):
    Q_natural = 16 * np.pi**3 * (R * r) / (d * d) + 4 * np.pi**2 * (R * r) / (d * d) + np.pi
    return {
        "R": R,
        "r": r,
        "d": d,
        "c": c,
        "ratio_self_avoidance": ratio_sa,
        "ratio_screening": ratio_scr,
        "Q_grid": Q_grid,
        "Q_natural": Q_natural,
        "alpha_inv_target": ALPHA_COLD_INV,
    }


def run_single(nx: int, R_init: float, r_init: float, label: str,
               max_iter: int = 500, lr: float = 0.01) -> dict:
    solver = CosseratField3D(nx, nx, nx, dx=1.0, use_saturation=True)
    solver.initialize_electron_2_3_sector(R_target=R_init, r_target=r_init)

    initial = extract_ch8_ratios(solver)
    result = solver.relax_to_ground_state(
        max_iter=max_iter,
        tol=1e-8,
        initial_lr=lr,
        verbose=False,
    )
    final = extract_ch8_ratios(solver)
    return {
        "label": label,
        "init_target": (R_init, r_init),
        "initial_ratios": initial,
        "final_ratios": final,
        "iterations": result["iterations"],
        "converged": result["converged"],
        "final_energy": result["final_energy"],
    }


def print_report(info: dict) -> None:
    print(f"\n--- {info['label']} ---")
    print(f"  Init target: R_init = {info['init_target'][0]:.3f}, r_init = {info['init_target'][1]:.3f}")
    print(f"  Iterations: {info['iterations']}, converged: {info['converged']}")
    print(f"  Final energy: {info['final_energy']:.3e}")
    print(f"                {'INITIAL':>14} {'FINAL':>14} {'TARGET':>14}")
    for key, target in [
        ("R", None),
        ("r", None),
        ("d", None),
        ("c", 3),
        ("ratio_self_avoidance", 0.5),
        ("ratio_screening", 0.25),
        ("Q_natural", ALPHA_COLD_INV),
    ]:
        init_v = info['initial_ratios'][key]
        final_v = info['final_ratios'][key]
        init_str = f"{init_v:.4f}" if isinstance(init_v, float) else f"{init_v}"
        final_str = f"{final_v:.4f}" if isinstance(final_v, float) else f"{final_v}"
        target_str = "—" if target is None else (f"{target:.4f}" if isinstance(target, float) else f"{target}")
        print(f"  {key:>22} {init_str:>14} {final_str:>14} {target_str:>14}")


def main():
    print("=" * 78)
    print("  Phase-3 α⁻¹ validation via Ch 8 dimensionless ratios")
    print("=" * 78)
    print("  Approach: compute (R-r)/d, R·r/d², Q_natural from relaxed field")
    print("  Target:   0.5000, 0.2500, 137.0363 at Golden Torus")
    print("  Resolved: scalar Z₀ per research/L3_electron_soliton/10_.")

    NX = 64
    R_exact, r_exact = golden_torus_grid_coords(16.0)
    print(f"  Grid: {NX}³   R_init (Golden): {R_exact:.3f}, r_init: {r_exact:.3f}")
    print()

    # Run 1: exact Golden Torus initialization
    info1 = run_single(
        nx=NX,
        R_init=R_exact,
        r_init=r_exact,
        label="Run 1: initialize at exact Golden Torus",
        max_iter=500,
    )
    print_report(info1)

    # Run 2: perturbed start (R +30%, r -30%)
    info2 = run_single(
        nx=NX,
        R_init=R_exact * 1.3,
        r_init=r_exact * 0.7,
        label="Run 2: perturbed off-Golden (R +30%, r -30%)",
        max_iter=500,
    )
    print_report(info2)

    # Acceptance check against Phase-2 tolerances (09_ §5)
    print("\n" + "=" * 78)
    print("  ACCEPTANCE CHECK against Phase-2 tolerances (09_ §5)")
    print("=" * 78)
    print("  Target: |ratio_self_avoidance - 0.5| < 1e-3")
    print("          |ratio_screening      - 0.25| < 1e-3")
    print("          c = 3 (integer exact)")
    print("          |Q_natural - 137.0363| < 1e-3")
    print()

    for info in (info1, info2):
        f = info['final_ratios']
        sa_err = abs(f['ratio_self_avoidance'] - 0.5)
        scr_err = abs(f['ratio_screening'] - 0.25)
        Q_err = abs(f['Q_natural'] - ALPHA_COLD_INV)
        c_ok = (f['c'] == 3)
        sa_ok = sa_err < 1e-3
        scr_ok = scr_err < 1e-3
        Q_ok = Q_err < 1e-3
        all_ok = sa_ok and scr_ok and c_ok and Q_ok
        verdict = "PASS" if all_ok else "FAIL"
        print(f"  {info['label']}:  {verdict}")
        print(f"    self-avoidance: {f['ratio_self_avoidance']:.4f}  (err {sa_err:.2e})  {'✓' if sa_ok else '✗'}")
        print(f"    screening:      {f['ratio_screening']:.4f}  (err {scr_err:.2e})  {'✓' if scr_ok else '✗'}")
        print(f"    crossings:      {f['c']}                 (expected 3)  {'✓' if c_ok else '✗'}")
        print(f"    Q_natural:      {f['Q_natural']:.4f}  (err {Q_err:.2e})  {'✓' if Q_ok else '✗'}")


if __name__ == "__main__":
    main()
