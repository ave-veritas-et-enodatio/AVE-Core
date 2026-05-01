"""
LL-descent validation of Cosserat (2,3) eigenmode.

Per validate_cosserat_electron_soliton.py findings note:
  "Plain gradient descent does not preserve topology under lattice tearing.
   A topology-preserving variant (constrained gradient, projected descent,
   or Landau-Lifshitz-style precession-plus-damping) may be required."

This driver tests Landau-Lifshitz-style projected descent on the omega field:
  - Plain gradient on u (translation is unconstrained)
  - PROJECTED gradient on omega: dE_dw_perp = dE_dw - (omega·dE_dw)/|omega|² · omega
    (perpendicular to omega per cell; preserves |omega|² to first order in lr)

Hypothesis: plain gradient gets stuck at R/r=3.0 (14.6% gap from φ²) at both
32³ and 64³ because amplitude decay routes the descent to a non-Golden-Torus
local minimum. LL-projected descent preserves |omega|² per cell, so the
(2,3) winding amplitude profile cannot dissipate. The geometry should settle
at the GLOBAL minimum (Golden Torus per Vol 1 Ch 8) instead of the
amplitude-decayed local minimum.

Compares: plain gradient (existing relax_to_ground_state) vs LL-projected
descent (this driver). Both at 32³ + 64³ if cheap enough.

Status: exploratory per Rule 11 (validates whether algorithm choice closes
the Cosserat ⚠ gap from doc 100 §11.2). NOT a permanent solver method;
if LL works, promote to CosseratField3D.relax_to_ground_state_topology_preserving().
"""
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.topological.cosserat_field_3d import CosseratField3D
from validate_cosserat_electron_soliton import golden_torus_grid_coords, R_GOLDEN_GRID


PHI = (1.0 + np.sqrt(5.0)) / 2.0
PHI_SQ = PHI ** 2


def relax_ll_descent(
    solver: CosseratField3D,
    max_iter: int = 1500,
    initial_lr: float = 1e-2,
    tol: float = 1e-8,
) -> dict:
    """LL-projected gradient descent.

    Plain gradient on u; projected gradient on omega (perpendicular to
    omega per cell, preserves |omega|² to first order). Backtracking line
    search same as solver.relax_to_ground_state().
    """
    lr = initial_lr
    E_prev = solver.total_energy()
    history = [E_prev]
    noise_floor = 1e-12 * max(abs(E_prev), 1.0)
    n_omega_preserve_violations = 0

    for step in range(max_iter):
        u_save = solver.u.copy()
        w_save = solver.omega.copy()

        dE_du, dE_dw = solver.energy_gradient()

        # LL projection: dE_dw_perp = dE_dw - (omega · dE_dw)/|omega|² · omega
        # Preserves |omega|² per cell to first order in lr.
        omega_sq = np.sum(solver.omega ** 2, axis=-1, keepdims=True) + 1e-20
        omega_dot_grad = np.sum(solver.omega * dE_dw, axis=-1, keepdims=True)
        dE_dw_perp = dE_dw - (omega_dot_grad / omega_sq) * solver.omega

        # |omega|² before
        w_norm_sq_before = np.sum(w_save ** 2, axis=-1)

        # Update
        solver.u = solver.u - lr * dE_du
        solver.omega = solver.omega - lr * dE_dw_perp
        solver._zero_outside_alive()

        # Verify |omega|² preservation (post-step)
        w_norm_sq_after = np.sum(solver.omega ** 2, axis=-1)
        active = solver.mask_alive
        if np.any(active):
            rel_change = np.abs(w_norm_sq_after[active] - w_norm_sq_before[active]) / (
                np.abs(w_norm_sq_before[active]) + 1e-20
            )
            mean_change = float(np.mean(rel_change))
            if mean_change > 1e-3:
                n_omega_preserve_violations += 1

        E_new = solver.total_energy()

        if E_new <= E_prev + noise_floor:
            rel_change = abs(E_new - E_prev) / max(abs(E_prev), 1e-12)
            history.append(E_new)
            if step > 10 and rel_change < tol:
                return {
                    "iterations": step + 1,
                    "final_energy": E_new,
                    "converged": True,
                    "energy_history": history,
                    "lr_final": lr,
                    "omega_preserve_violations": n_omega_preserve_violations,
                }
            lr = min(lr * 1.1, 1.0)
            E_prev = E_new
            noise_floor = 1e-12 * max(abs(E_prev), 1.0)
        else:
            solver.u = u_save
            solver.omega = w_save
            lr *= 0.5
            if lr < 1e-14:
                return {
                    "iterations": step + 1,
                    "final_energy": E_prev,
                    "converged": False,
                    "energy_history": history,
                    "lr_final": lr,
                    "omega_preserve_violations": n_omega_preserve_violations,
                }

    return {
        "iterations": max_iter,
        "final_energy": E_prev,
        "converged": False,
        "energy_history": history,
        "lr_final": lr,
        "omega_preserve_violations": n_omega_preserve_violations,
    }


def run_ll_test(nx: int, R_init: float, r_init: float, label: str,
                max_iter: int = 1500, initial_lr: float = 1e-2) -> dict:
    solver = CosseratField3D(nx, nx, nx, dx=1.0, use_saturation=True)
    solver.initialize_electron_2_3_sector(R_target=R_init, r_target=r_init)

    E_init = solver.total_energy()
    R_obs0, r_obs0 = solver.extract_shell_radii()
    c0 = solver.extract_crossing_count()

    t0 = time.time()
    result = relax_ll_descent(solver, max_iter=max_iter, initial_lr=initial_lr)
    dt = time.time() - t0

    R_final, r_final = solver.extract_shell_radii()
    c_final = solver.extract_crossing_count()
    Q = solver.extract_quality_factor()
    ratio = R_final / max(r_final, 1e-9)

    return {
        "label": label,
        "nx": nx,
        "init": (R_init, r_init),
        "initial_obs": (R_obs0, r_obs0, c0),
        "initial_E": E_init,
        "iterations": result["iterations"],
        "converged": result["converged"],
        "final_E": result["final_energy"],
        "final_R": R_final,
        "final_r": r_final,
        "final_c": c_final,
        "final_Q": Q,
        "ratio": ratio,
        "ratio_gap_pct": abs(ratio - PHI_SQ) / PHI_SQ * 100,
        "wall_s": dt,
        "omega_violations": result.get("omega_preserve_violations", 0),
    }


def print_run(info: dict) -> None:
    print(f"\n--- {info['label']} (nx={info['nx']}) ---")
    print(f"  Init (target):     R={info['init'][0]:.4f}, r={info['init'][1]:.4f}")
    print(f"  Init (observed):   R={info['initial_obs'][0]:.4f}, r={info['initial_obs'][1]:.4f}, c={info['initial_obs'][2]}")
    print(f"  Wall:              {info['wall_s']:.1f}s")
    print(f"  Iterations:        {info['iterations']}")
    print(f"  Converged:         {info['converged']}")
    print(f"  Final (R,r):       ({info['final_R']:.4f}, {info['final_r']:.4f})")
    print(f"  Final c:           {info['final_c']}")
    print(f"  R/r:               {info['ratio']:.4f}   (target φ²={PHI_SQ:.4f})")
    print(f"  R/r gap:           {info['ratio_gap_pct']:.2f}%")
    print(f"  Q (grid units):    {info['final_Q']:.3f}")
    print(f"  ω-preserve viols:  {info['omega_violations']} (>1e-3 fractional drift)")


def main():
    print("=" * 72)
    print("  LL-projected descent vs plain gradient (Cosserat (2,3) eigenmode)")
    print("=" * 72)
    print("  Plain-gradient baseline (per validate_cosserat_electron_soliton.py):")
    print("    32³ near-Golden:  R/r=3.000  gap 14.6%  c=3 ✓")
    print("    32³ perturbed:    R/r=5.250  gap 100.5% c=3 ✓")
    print("    64³ near-Golden:  R/r=3.000  gap 14.59% c=3 ✓ (this session)")
    print()
    print("  Hypothesis: LL-projected descent preserves |omega|² per cell,")
    print("  preventing amplitude-decay route to non-Golden local minimum.")
    print()

    R_exact, r_exact = golden_torus_grid_coords(R_GOLDEN_GRID)
    print(f"  Target geometry:   R={R_exact:.4f}, r={r_exact:.4f}, R/r={PHI_SQ:.4f}")

    print("\n=== 32³ + LL near-Golden ===")
    info_32_near = run_ll_test(
        nx=32, R_init=R_exact, r_init=r_exact,
        label="32³ LL near-Golden", max_iter=1500, initial_lr=1e-2,
    )
    print_run(info_32_near)

    print("\n=== 32³ + LL perturbed ===")
    info_32_pert = run_ll_test(
        nx=32, R_init=R_exact * 1.3, r_init=r_exact * 0.7,
        label="32³ LL perturbed", max_iter=1500, initial_lr=1e-2,
    )
    print_run(info_32_pert)

    print("\n" + "=" * 72)
    print("  COMPARISON (32³)")
    print("=" * 72)
    print(f"{'seed':<20} {'method':<12} {'R/r':<10} {'gap %':<10} {'c':<3}")
    print(f"{'near-Golden':<20} {'plain':<12} {'3.0000':<10} {'14.59':<10} {'3':<3}")
    print(f"{'near-Golden':<20} {'LL':<12} {info_32_near['ratio']:.4f}     {info_32_near['ratio_gap_pct']:5.2f}      {info_32_near['final_c']:<3}")
    print(f"{'perturbed':<20} {'plain':<12} {'5.2500':<10} {'100.50':<10} {'3':<3}")
    print(f"{'perturbed':<20} {'LL':<12} {info_32_pert['ratio']:.4f}     {info_32_pert['ratio_gap_pct']:5.2f}      {info_32_pert['final_c']:<3}")


if __name__ == "__main__":
    main()
