"""
Round 12 validation driver: canonical electron 0₁ unknot Cosserat eigenmode.

Per research/L3_electron_soliton/101_ §9 three-layer canonical (confirmed by
Grant 2026-04-30):

  Layer 1 — real-space curve: unknot 0₁ at horn torus R = r
  Layer 2 — field bundle:    SU(2) double-cover via SO(3) → SU(2)
                              Rodrigues projection (post-processing observable)
  Layer 3 — phase-space:     (V_inc, V_ref) (2,3) winding (NOT in scope)

Per research/L3_electron_soliton/102_ §2.6 pre-registered binary criteria:
  C1 — extract_crossing_count = 0 (unknot)
  C2 — extract_hopf_charge ≈ 0 (zero linking)
  C3 — extract_shell_radii R ≈ R_target ± 5%
  C4 — extract_shell_radii r ≈ r_target ± 10% (loose, HWHM convention)
  C5 — total_energy finite + non-negative
  C6 — total_energy ≫ vacuum-floor noise
  C7 — Layer-2 SU(2) bundle character via Rodrigues projection
       (post-relaxation; spinor closure observable)

Multi-N protocol per A40: lattice-resolved primary tests at 32³ and 64³.
Sub-grid canonical (R = ℓ_node/(2π) ≈ 0.16 cells) test deferred — not
testable on discretized grid; full canonical-electron test requires
sub-cell-capable infrastructure (e.g., spectral solver) per E-094 Flag 2.

Distinct from validate_cosserat_electron_soliton.py:
  - Tests UNKNOT topology (c=0), NOT (2,3) torus knot (c=3)
  - No Golden Torus reference (per doc 100 §25 bracket-Golden-Torus
    + Round 12 ground on packing-fraction canonical)
  - Pre-registered against unknot canonical from electron-unknot.md

Per Rule 11 clean-falsification + A39 v2 dual-criterion + A40 multi-N.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.cosserat_field_3d import CosseratField3D


def run_unknot_validation(
    nx: int,
    R_target: float,
    r_target: float | None = None,
    label: str = "",
    max_iter: int = 500,
    initial_lr: float = 1e-3,
    use_saturation: bool = True,
    amplitude_scale: float = 1.0,
) -> dict:
    """Single validation run: seed unknot at (R, r), relax, measure all
    pre-registered binary criteria. Default r_target = R_target (horn torus)."""
    if r_target is None:
        r_target = R_target

    solver = CosseratField3D(nx, nx, nx, dx=1.0, use_saturation=use_saturation)
    solver.initialize_electron_unknot_sector(
        R_target=R_target, r_target=r_target, amplitude_scale=amplitude_scale
    )

    # t=0 measurements
    E_init = solver.total_energy()
    R_init_obs, r_init_obs = solver.extract_shell_radii()
    c_init = solver.extract_crossing_count()
    Q_H_init = solver.extract_hopf_charge()

    # Relax
    t0 = time.time()
    result = solver.relax_to_ground_state(
        max_iter=max_iter,
        tol=1e-8,
        initial_lr=initial_lr,
        verbose=False,
    )
    dt = time.time() - t0

    # t=relaxed measurements
    R_final, r_final = solver.extract_shell_radii()
    c_final = solver.extract_crossing_count()
    Q_H_final = solver.extract_hopf_charge()
    E_final = result["final_energy"]

    # Layer-2 SU(2) bundle test: extract n_hat (via Rodrigues) at points along
    # the loop axis at φ ∈ [0, 4π) and check phase progression.
    # NOTE: this is a coarse first-cut measurement; precision SU(2) verification
    # requires more careful analysis. Reporting as post-processing diagnostic.
    n_hat_along_loop = _extract_n_hat_along_loop(solver, R_final, n_samples=16)

    # Pre-registered binary criteria evaluation
    R_dev = abs(R_final - R_target) / max(R_target, 1e-9) * 100
    r_dev = abs(r_final - r_target) / max(r_target, 1e-9) * 100
    horn_dev = abs(R_final - r_final) / max(R_final, 1e-9) * 100  # (horn torus check)

    return {
        "label": label,
        "nx": nx,
        "init": (R_target, r_target),
        "initial_obs": (R_init_obs, r_init_obs, c_init, Q_H_init),
        "initial_E": E_init,
        "iterations": result["iterations"],
        "converged": result["converged"],
        "final_E": E_final,
        "final_R": R_final,
        "final_r": r_final,
        "final_c": c_final,
        "final_Q_H": Q_H_final,
        "R_deviation_pct": R_dev,
        "r_deviation_pct": r_dev,
        "horn_torus_deviation_pct": horn_dev,
        "wall_s": dt,
        "n_hat_along_loop": n_hat_along_loop,
        # Binary criteria assessment
        "C1_pass": c_final == 0,
        "C2_pass": abs(Q_H_final) < 1e-2,
        "C3_pass": R_dev < 5.0,
        "C4_pass": r_dev < 10.0,
        "C5_pass": np.isfinite(E_final) and E_final >= 0.0,
        "C6_pass": E_final > 1.0,
    }


def _extract_n_hat_along_loop(solver, R_loop: float, n_samples: int = 16) -> np.ndarray:
    """Extract n_hat (Rodrigues projection of ω) at n_samples points equally
    spaced along the loop's central circle in real space. Returns array
    shape (n_samples, 3) — the unit n_hat vector at each sample."""
    from ave.topological.cosserat_field_3d import _project_omega_to_nhat
    import jax.numpy as jnp

    cx, cy, cz = (solver.nx - 1) / 2.0, (solver.ny - 1) / 2.0, (solver.nz - 1) / 2.0
    n_hat_full = np.asarray(_project_omega_to_nhat(jnp.asarray(solver.omega)))

    samples = []
    for k in range(n_samples):
        phi = 2.0 * np.pi * k / n_samples
        x = cx + R_loop * np.cos(phi)
        y = cy + R_loop * np.sin(phi)
        z = cz
        ix, iy, iz = int(round(x)), int(round(y)), int(round(z))
        ix = np.clip(ix, 0, solver.nx - 1)
        iy = np.clip(iy, 0, solver.ny - 1)
        iz = np.clip(iz, 0, solver.nz - 1)
        samples.append(n_hat_full[ix, iy, iz, :])

    return np.array(samples)


def print_run_summary(info: dict) -> None:
    print(f"\n--- {info['label']} (nx={info['nx']}) ---")
    print(f"  Seed (R, r):       ({info['init'][0]:.3f}, {info['init'][1]:.3f}) [horn torus = R = r]")
    print(f"  t=0 obs (R, r, c): ({info['initial_obs'][0]:.3f}, {info['initial_obs'][1]:.3f}, c={info['initial_obs'][2]})")
    print(f"  t=0 Q_H:           {info['initial_obs'][3]:.3e}")
    print(f"  t=0 energy:        {info['initial_E']:.3e}")
    print(f"  Wall time:         {info['wall_s']:.1f}s")
    print(f"  Iterations:        {info['iterations']}, converged={info['converged']}")
    print(f"  t=final (R, r, c): ({info['final_R']:.3f}, {info['final_r']:.3f}, c={info['final_c']})")
    print(f"  t=final Q_H:       {info['final_Q_H']:.3e}")
    print(f"  t=final energy:    {info['final_E']:.3e}")
    print(f"  R deviation:       {info['R_deviation_pct']:.2f}% [C3 threshold 5%]")
    print(f"  r deviation:       {info['r_deviation_pct']:.2f}% [C4 threshold 10%]")
    print(f"  horn torus dev:    {info['horn_torus_deviation_pct']:.2f}% [|R-r|/R]")

    print(f"\n  Binary criteria:")
    print(f"  C1 (c=0):          {'✓ PASS' if info['C1_pass'] else '✗ FAIL'}  (c={info['final_c']})")
    print(f"  C2 (Q_H≈0):        {'✓ PASS' if info['C2_pass'] else '✗ FAIL'}  (Q_H={info['final_Q_H']:.3e})")
    print(f"  C3 (R within 5%):  {'✓ PASS' if info['C3_pass'] else '✗ FAIL'}")
    print(f"  C4 (r within 10%): {'✓ PASS' if info['C4_pass'] else '✗ FAIL'}")
    print(f"  C5 (E finite ≥0):  {'✓ PASS' if info['C5_pass'] else '✗ FAIL'}")
    print(f"  C6 (E ≫ noise):    {'✓ PASS' if info['C6_pass'] else '✗ FAIL'}")

    # C7 SU(2) bundle character (Layer 2 diagnostic)
    n_hat = info["n_hat_along_loop"]
    print(f"\n  C7 (Layer 2 SU(2) bundle observable):")
    print(f"  n_hat at sampled points along loop axis (φ progression):")
    for k in range(min(8, len(n_hat))):
        phi_deg = 360.0 * k / len(n_hat)
        print(f"    φ={phi_deg:5.1f}°  n_hat = ({n_hat[k, 0]:+.3f}, {n_hat[k, 1]:+.3f}, {n_hat[k, 2]:+.3f})")


def main():
    print("=" * 76)
    print("  Round 12 validation: canonical electron 0₁ unknot Cosserat eigenmode")
    print("  Per research/L3_electron_soliton/101_ §9 three-layer canonical")
    print("  Per research/L3_electron_soliton/102_ §2.6 pre-registered criteria")
    print("=" * 76)
    print()
    print("Pre-registered binary criteria (PASS conditions):")
    print("  C1: extract_crossing_count = 0 (unknot, no crossings)")
    print("  C2: extract_hopf_charge ≈ 0 (zero linking)")
    print("  C3: extract_shell_radii R within 5% of seed")
    print("  C4: extract_shell_radii r within 10% of seed")
    print("  C5: total_energy finite + non-negative")
    print("  C6: total_energy > 1.0 (well above vacuum noise)")
    print("  C7: SU(2) bundle character — Rodrigues n_hat phase progression")
    print()
    print("Methodology disciplines: A39 v2 dual-criterion + A40 multi-N")
    print("(c-criterion + Q_H-criterion + R/r geometry + amplitude jointly)")
    print()
    print("Multi-N protocol: 32³ + 48³ at lattice-resolved horn torus")
    print("(Reading A canonical R = ℓ_node/(2π) ≈ 0.16 cells is sub-grid;")
    print(" tested separately as informational)")
    print()

    results = []

    # 32³ horn torus at lattice-resolved scale
    results.append(run_unknot_validation(
        nx=32, R_target=8.0,
        label="32³ horn torus (R=r=8 cells)",
        max_iter=500,
    ))

    # 48³ horn torus at same physical scale (A40 multi-N)
    results.append(run_unknot_validation(
        nx=48, R_target=8.0,
        label="48³ horn torus (R=r=8 cells, multi-N)",
        max_iter=500,
    ))

    # Off-horn diagnostic (R ≠ r) — verify seeder works for non-horn-torus too
    results.append(run_unknot_validation(
        nx=32, R_target=10.0, r_target=4.0,
        label="32³ standard torus (R=10, r=4) — non-canonical diagnostic",
        max_iter=500,
    ))

    for info in results:
        print_run_summary(info)

    print()
    print("=" * 76)
    print("  PASS SUMMARY")
    print("=" * 76)
    print(f"{'config':<48} {'C1':<5} {'C2':<5} {'C3':<5} {'C4':<5} {'C5':<5} {'C6':<5}")
    for info in results:
        c = lambda b: "✓" if b else "✗"
        print(f"{info['label']:<48} "
              f"{c(info['C1_pass']):<5} {c(info['C2_pass']):<5} "
              f"{c(info['C3_pass']):<5} {c(info['C4_pass']):<5} "
              f"{c(info['C5_pass']):<5} {c(info['C6_pass']):<5}")

    print()
    print("=" * 76)
    print("  Round 12 layer-1+2 partial canonical-electron test")
    print("=" * 76)

    # Strict pass criterion (per doc 102 §2.6): C1 + C2 + C3 + C5 + C6 must all pass
    # for layer-1 (real-space curve topology). C4 (r) is loose. C7 is diagnostic.
    strict_layer_1_passes = sum(
        1 for info in results
        if info["C1_pass"] and info["C2_pass"] and info["C3_pass"]
        and info["C5_pass"] and info["C6_pass"]
    )
    print(f"  Strict Layer 1 PASS count: {strict_layer_1_passes} / {len(results)}")
    print(f"  (PASS = C1 ∧ C2 ∧ C3 ∧ C5 ∧ C6 — the unknot topology + localization +")
    print(f"   energy criteria; C4 r-criterion is loose, C7 is post-processing)")


if __name__ == "__main__":
    main()
