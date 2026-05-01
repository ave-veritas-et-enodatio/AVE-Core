"""
Lorentzian-fit closure of Cosserat scaffold-preservation ⚠ per doc 100 §17.4 Path 1.

Auditor proposed (§17.4):
  Path 1 (cheap, ~10 min): Direct scaffold check via amplitude profile fit.
  After relaxation, fit the binned profile to a Lorentzian
      peak / (1 + ((rho - R_fit) / r_fit)²).
  If R_fit ≈ R_target and r_fit ≈ r_target, scaffold is preserved.
  If they shifted, scaffold deformed.

This driver:
  1. Initializes the canonical (2,3) Sutcliffe ansatz at the seeded (R, r).
  2. Captures the t=0 amplitude profile (the scaffold-as-seeded baseline).
  3. Runs relax_to_ground_state for the same iter budget as the canonical
     validator (1500 iters, lr=1e-2).
  4. Captures the t=final amplitude profile.
  5. Lorentzian-fits both binned profiles via scipy.optimize.curve_fit.
  6. Compares (R_seed, r_seed) → (R_fit_t0, r_fit_t0) → (R_fit_relax, r_fit_relax).

Decision rule per §17.4:
  - If R_fit_relax / R_target within 5% AND r_fit_relax / r_target within 5%
    → scaffold preserved (⚠ → ✅)
  - Else → scaffold deformed (⚠ remains, with quantitative deformation report)

The HWHM-based extract_shell_radii (line 1435) reports R/r=3.0 at the GT seed.
This driver tests whether the HWHM convention shifts the apparent r relative to
a fitted Lorentzian half-width.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import curve_fit

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.topological.cosserat_field_3d import CosseratField3D
from validate_cosserat_electron_soliton import golden_torus_grid_coords, R_GOLDEN_GRID


PHI = (1.0 + np.sqrt(5.0)) / 2.0
PHI_SQ = PHI ** 2


def lorentzian(rho: np.ndarray, peak: float, R_fit: float, r_fit: float, baseline: float) -> np.ndarray:
    return baseline + peak / (1.0 + ((rho - R_fit) / r_fit) ** 2)


def build_amplitude_profile(solver: CosseratField3D) -> tuple[np.ndarray, np.ndarray]:
    omega_mag = np.sqrt(np.sum(solver.omega ** 2, axis=-1))
    cx, cy, cz = (solver.nx - 1) / 2.0, (solver.ny - 1) / 2.0, (solver.nz - 1) / 2.0
    kz = int(round(cz))

    slice_z = omega_mag[:, :, kz]
    xs = solver._i[:, :, kz] - cx
    ys = solver._j[:, :, kz] - cy
    rho = np.sqrt(xs ** 2 + ys ** 2)

    rho_flat = rho.flatten()
    mag_flat = slice_z.flatten()
    rho_max = float(rho.max())
    n_bins = max(8, int(round(rho_max)))
    edges = np.linspace(0.0, rho_max, n_bins + 1)
    hist, _ = np.histogram(rho_flat, bins=edges, weights=mag_flat)
    counts, _ = np.histogram(rho_flat, bins=edges)
    with np.errstate(divide="ignore", invalid="ignore"):
        profile = np.where(counts > 0, hist / np.maximum(counts, 1), 0.0)
    centers = 0.5 * (edges[:-1] + edges[1:])
    return centers, profile


def fit_lorentzian(centers: np.ndarray, profile: np.ndarray, R_seed: float, r_seed: float) -> dict:
    peak0 = float(profile.max())
    base0 = float(np.percentile(profile, 10))
    p0 = [peak0 - base0, R_seed, r_seed, base0]

    bounds_lo = [0.0, 0.0, 0.1, 0.0]
    bounds_hi = [10.0 * peak0 + 1e-6, float(centers.max()), float(centers.max()), peak0]

    try:
        popt, pcov = curve_fit(lorentzian, centers, profile, p0=p0, bounds=(bounds_lo, bounds_hi), maxfev=10000)
        peak_fit, R_fit, r_fit, base_fit = popt
        sigma = np.sqrt(np.diag(pcov))
        residuals = profile - lorentzian(centers, *popt)
        rss = float(np.sum(residuals ** 2))
        tss = float(np.sum((profile - profile.mean()) ** 2))
        r_squared = 1.0 - rss / max(tss, 1e-20)
        return {
            "ok": True,
            "peak": float(peak_fit),
            "R_fit": float(R_fit),
            "r_fit": float(r_fit),
            "baseline": float(base_fit),
            "R_sigma": float(sigma[1]),
            "r_sigma": float(sigma[2]),
            "r_squared": r_squared,
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}


def run_lorentzian_test(nx: int, R_target: float, r_target: float, label: str,
                        max_iter: int = 1500, lr: float = 1e-2) -> dict:
    print(f"\n--- {label} (nx={nx}) ---")
    print(f"  Target (seed):     R={R_target:.4f}, r={r_target:.4f}")

    solver = CosseratField3D(nx, nx, nx, dx=1.0, use_saturation=True)
    solver.initialize_electron_2_3_sector(R_target=R_target, r_target=r_target)

    centers0, profile0 = build_amplitude_profile(solver)
    R_obs0, r_obs0 = solver.extract_shell_radii()
    fit0 = fit_lorentzian(centers0, profile0, R_target, r_target)

    print(f"  t=0 HWHM extract:  R={R_obs0:.4f}, r={r_obs0:.4f}")
    if fit0["ok"]:
        print(f"  t=0 Lorentz fit:   R={fit0['R_fit']:.4f} ± {fit0['R_sigma']:.4f}, "
              f"r={fit0['r_fit']:.4f} ± {fit0['r_sigma']:.4f}, R²={fit0['r_squared']:.4f}")
    else:
        print(f"  t=0 Lorentz fit FAILED: {fit0['error']}")

    t0 = time.time()
    result = solver.relax_to_ground_state(max_iter=max_iter, initial_lr=lr)
    dt = time.time() - t0
    print(f"  Relaxation:        {dt:.1f}s, {result['iterations']} iters, converged={result['converged']}")

    centers1, profile1 = build_amplitude_profile(solver)
    R_obs1, r_obs1 = solver.extract_shell_radii()
    fit1 = fit_lorentzian(centers1, profile1, R_target, r_target)

    print(f"  t=relax HWHM:      R={R_obs1:.4f}, r={r_obs1:.4f}")
    if fit1["ok"]:
        print(f"  t=relax Lorentz:   R={fit1['R_fit']:.4f} ± {fit1['R_sigma']:.4f}, "
              f"r={fit1['r_fit']:.4f} ± {fit1['r_sigma']:.4f}, R²={fit1['r_squared']:.4f}")
        R_dev = abs(fit1['R_fit'] - R_target) / R_target * 100
        r_dev = abs(fit1['r_fit'] - r_target) / r_target * 100
        print(f"  R deviation:       {R_dev:.2f}%  (5% threshold)")
        print(f"  r deviation:       {r_dev:.2f}%  (5% threshold)")
        scaffold_ok = R_dev < 5.0 and r_dev < 5.0
        print(f"  SCAFFOLD STATUS:   {'✅ preserved' if scaffold_ok else '⚠ deformed'}")
    else:
        print(f"  t=relax Lorentz fit FAILED: {fit1['error']}")
        scaffold_ok = False

    return {
        "label": label,
        "nx": nx,
        "R_target": R_target,
        "r_target": r_target,
        "t0_hwhm": (R_obs0, r_obs0),
        "t0_lorentz": fit0,
        "t1_hwhm": (R_obs1, r_obs1),
        "t1_lorentz": fit1,
        "iterations": result["iterations"],
        "converged": result["converged"],
        "wall_s": dt,
        "scaffold_preserved": scaffold_ok if fit1["ok"] else None,
        "centers_t0": centers0,
        "profile_t0": profile0,
        "centers_t1": centers1,
        "profile_t1": profile1,
    }


def main():
    print("=" * 72)
    print("  Lorentzian-fit closure of Cosserat scaffold-preservation ⚠")
    print("  Per doc 100 §17.4 Path 1 — auditor recommendation")
    print("=" * 72)
    print()
    print("Decision rule:")
    print("  R_fit_relax within 5% of R_target AND r_fit_relax within 5%")
    print("  of r_target → scaffold preserved (⚠ → ✅)")
    print("  Else → scaffold deformed (⚠ remains, with quantitative report)")
    print()

    R_GT, r_GT = golden_torus_grid_coords(R_GOLDEN_GRID)
    print(f"Reference Golden Torus (grid): R={R_GT:.4f}, r={r_GT:.4f}, R/r={PHI_SQ:.4f}")

    results = []
    results.append(run_lorentzian_test(
        nx=32, R_target=R_GT, r_target=r_GT,
        label="32³ Golden Torus seed",
    ))
    results.append(run_lorentzian_test(
        nx=32, R_target=R_GT * 1.3, r_target=r_GT * 0.7,
        label="32³ perturbed seed (R+30%, r-30%)",
    ))

    print()
    print("=" * 72)
    print("  CLOSURE SUMMARY")
    print("=" * 72)
    print(f"{'seed':<35} {'R_fit/R_tgt':<12} {'r_fit/r_tgt':<12} {'R²':<8} {'verdict':<15}")
    for res in results:
        if res["t1_lorentz"]["ok"]:
            R_ratio = res["t1_lorentz"]["R_fit"] / res["R_target"]
            r_ratio = res["t1_lorentz"]["r_fit"] / res["r_target"]
            r_sq = res["t1_lorentz"]["r_squared"]
            verdict = "✅ preserved" if res["scaffold_preserved"] else "⚠ deformed"
        else:
            R_ratio = float("nan")
            r_ratio = float("nan")
            r_sq = float("nan")
            verdict = "fit FAILED"
        print(f"{res['label']:<35} {R_ratio:<12.4f} {r_ratio:<12.4f} {r_sq:<8.4f} {verdict:<15}")

    print()
    print("=" * 72)
    print("  HWHM vs Lorentzian convention comparison (§17.4 hypothesis)")
    print("=" * 72)
    print(f"{'seed':<35} {'HWHM_r':<10} {'Lorentz_r':<12} {'ratio':<10}")
    for res in results:
        if res["t1_lorentz"]["ok"]:
            r_hwhm = res["t1_hwhm"][1]
            r_lor = res["t1_lorentz"]["r_fit"]
            ratio = r_hwhm / max(r_lor, 1e-9)
            print(f"{res['label']:<35} {r_hwhm:<10.4f} {r_lor:<12.4f} {ratio:<10.4f}")

    return results


if __name__ == "__main__":
    main()
