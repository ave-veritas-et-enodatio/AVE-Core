"""
Path C — L3 Phase-3 closure: dual-target convergence in the TLM.

Per `.claude/plans/read-the-collaboration-md-first-resilient-mccarthy.md`
§18 (Y-matrix audit + Path C plan, 2026-04-21 evening).

Drives `solve_eigenmode_dual_target()` with two scalar convergence targets:
  α⁻¹_measured(R, r, c) → 137.036 ± 1.5%   (Theorem 3.1)
  χ_measured(V_inc field) → α·6/5 ± 1.5%  (Sub-theorem 3.1.1)

Pre-registered prediction:
- At 48³, expect convergence within 12 outer iterations.
- At 96³, expect α⁻¹ ∈ [134.7, 139.3], χ ∈ [α·1.182, α·1.218].
- Both criteria met simultaneously at the converged amplitude.

If amplitude search oscillates without convergence: Phase-3 is open;
single-body bound state requires additional mechanism beyond TLM +
bond-Op3 + chirality-projection.

Falsification logged in prediction tracker
`.agents/handoffs/L3_PHASE3_SESSION_20260421.md` §2.4 regardless of outcome.
"""

import numpy as np

from ave.core.constants import V_YIELD, V_SNAP, ALPHA, ALPHA_COLD_INV
from scripts.vol_1_foundations.tlm_electron_soliton_eigenmode import (
    PHI,
    solve_eigenmode_dual_target,
)


def run_path_c(N: int, label: str, max_outer_iter: int = 12,
               n_steps: int = 200, pml_thickness: int = 0):
    """Run Path C dual-target convergence loop at lattice size N."""
    print()
    print("=" * 78)
    print(f"  Path C — L3 dual-target convergence at {N}³ ({label})")
    print("=" * 78)

    PHI_SQ = PHI ** 2  # ~ 2.618
    R_target = N / 4.0  # ~ N/4 lattice cells
    r_target = R_target / PHI_SQ
    amp_init = 0.5 * float(V_YIELD)

    print(f"  Geometry (held fixed): R = {R_target:.2f}, r = {r_target:.3f}, "
          f"R/r = {PHI_SQ:.4f} (Golden Torus)")
    print(f"  Initial amplitude: {amp_init:.3e} V (= 0.5 × V_YIELD)")
    print(f"  Targets: α⁻¹ → {ALPHA_COLD_INV:.4f}, χ → {ALPHA*6/5:.4e}")
    print(f"  Tolerance: 1.5% on both (per pre-registered prediction)")
    print(f"  Max outer iterations: {max_outer_iter}")

    result = solve_eigenmode_dual_target(
        N=N,
        R_target=R_target,
        r_target=r_target,
        amp_init=amp_init,
        n_steps=n_steps,
        pml_thickness=pml_thickness,
        max_outer_iter=max_outer_iter,
        tol=0.015,
        scale_exp=0.1,
        damping=0.5,
        verbose=True,
    )

    print()
    print("=" * 78)
    print(f"  Path C result at {N}³:")
    print("=" * 78)
    if result['converged']:
        print(f"  CONVERGED at iter {result['iterations']}/{max_outer_iter}")
        print(f"  Final amp:    {result['final_amp']:.4e}")
        print(f"  Final (R, r): ({result['final_R']:.3f}, {result['final_r']:.3f})")
        print(f"  Final α⁻¹:    {result['final_alpha_inv']:.3f} "
              f"(target {ALPHA_COLD_INV:.3f})")
        print(f"  Final χ:      {result['final_chi']:.4e} "
              f"(target {ALPHA*6/5:.4e})")
    else:
        print(f"  NOT converged within {max_outer_iter} iterations.")
        traj = result['trajectory']
        if traj:
            print(f"  Best α⁻¹ across trajectory: "
                  f"{min(abs(h['alpha_err']) for h in traj)*100:.2f}% off target")
            print(f"  Best χ:                     "
                  f"{min(abs(h['chi_err']) for h in traj)*100:.2f}% off target")

    return result


def main():
    print("=" * 78)
    print("  L3 PHASE-3 PATH C — Theorem 3.1 + Sub-theorem 3.1.1 in TLM")
    print("=" * 78)
    print()
    print("  This script tests the dual-target prediction:")
    print(f"    α⁻¹ = 4π³ + π² + π = {ALPHA_COLD_INV:.4f}  (Theorem 3.1)")
    print(f"    χ   = α·6/5 = {ALPHA*6/5:.4e}  (Sub-theorem 3.1.1)")
    print()
    print("  Single-body bound-state objective (no Y-matrix; per §18 audit).")

    # Quick convergence test at 48³
    result_48 = run_path_c(N=48, label="quick test", max_outer_iter=8,
                           n_steps=150)

    # Definitive run at 96³ only if 48³ shows progress
    if result_48['converged']:
        print("\n48³ converged — proceeding to 96³ for definitive number...")
        result_96 = run_path_c(N=96, label="definitive", max_outer_iter=12,
                               n_steps=200)
    else:
        # Check if 48³ at least made progress (errors trending down)
        traj = result_48.get('trajectory', [])
        if len(traj) >= 3:
            alpha_errs = [h['alpha_err'] for h in traj]
            making_progress = alpha_errs[-1] < alpha_errs[0] * 0.5
            if making_progress:
                print("\n48³ making progress but not converged in 8 iters — "
                      "trying 96³ with more iterations...")
                result_96 = run_path_c(N=96, label="definitive (more iters)",
                                       max_outer_iter=20, n_steps=200)
            else:
                print("\n48³ not making clear progress.")
                print("Documenting for falsification log; not running 96³.")
        else:
            print("\nInsufficient 48³ trajectory for trend analysis.")


if __name__ == "__main__":
    main()