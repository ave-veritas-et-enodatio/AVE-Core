"""
Phase 3b X2 — switch from K4-TLM to Cosserat field (u, omega) + S11 relax.

Per §9.5 + §10.6 of 32_phase3b_axiom_compliant_redesign.md:

  - K4-TLM (scalar port voltages) has exhausted its Axiom 4 implementation
    (§10.2: node-level saturation is mathematically a no-op for symmetric
    4-port junctions; bond-level Op3 is already fully engaged).
  - CosseratField3D carries explicit (u, omega) pair — the canonically-
    declared AVE substrate per scoping §2.
  - relax_s11() is the AVE-native minimization objective per collab rule 6
    ("its impedance. Why didn't you just ask me what the action of
    minimization was?").
  - initialize_electron_2_3_sector(use_hedgehog=True) uses the
    corpus-canonical AVE envelope + Regime II/III amplitude, no sweep.

This is the Phase 3b test within the current engine's capabilities.
If S11 minimization on the Cosserat field converges to R/r = φ² at the
(2,3) winding, Phase 3b closes. If not, Phase 1 items (full
Cosserat-Lagrangian with n̂↔ω identity closure) are required.

Pre-registered outcomes:
  P_X2a: R/r → φ² = 2.618, S11 → 0, c = 3 preserved  →  Phase 3b closes
  P_X2b: R/r stabilizes elsewhere (2.0, 2.27, etc.)  →  partial closure;
         specific R/r is the Cosserat attractor, not Ch 8's Golden Torus
  P_X2c: S11 doesn't converge / winding lost         →  mechanism still
         insufficient; Phase 1 Cosserat-Lagrangian full coupling needed
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.core.constants import ALPHA
from ave.topological.cosserat_field_3d import CosseratField3D

PHI = (1.0 + np.sqrt(5.0)) / 2.0
ALPHA_INV_TARGET = 1.0 / ALPHA


def run_cosserat_relax(
    N: int,
    R_target: float,
    r_target: float,
    max_iter: int = 500,
    tol: float = 1e-8,
    initial_lr: float = 0.01,
    track_every: int = 25,
    use_hedgehog: bool = True,
    verbose: bool = True,
) -> dict:
    """Initialize (2,3) sector and run S11 minimization."""
    print(f"  Creating CosseratField3D({N}, {N}, {N}, dx=1.0)")
    solver = CosseratField3D(N, N, N, dx=1.0, use_saturation=True)

    print(f"  initialize_electron_2_3_sector(R={R_target:.2f}, "
          f"r={r_target:.3f}, use_hedgehog={use_hedgehog})")
    solver.initialize_electron_2_3_sector(
        R_target=R_target, r_target=r_target, use_hedgehog=use_hedgehog,
    )

    # Initial diagnostics
    R0, r0 = solver.extract_shell_radii()
    c0 = solver.extract_crossing_count()
    S11_0 = solver.total_s11()
    print(f"  Initial: (R, r) = ({R0:.3f}, {r0:.3f}), R/r = "
          f"{R0/max(r0,1e-9):.3f}, c = {c0}, S11 = {S11_0:.4e}")

    print(f"  Running relax_s11(max_iter={max_iter}, tol={tol:.0e}, "
          f"lr={initial_lr})")
    result = solver.relax_s11(
        max_iter=max_iter,
        tol=tol,
        initial_lr=initial_lr,
        verbose=verbose,
        track_topology_every=track_every,
    )

    # Final state extraction
    R_f, r_f = solver.extract_shell_radii()
    c_f = solver.extract_crossing_count()

    result["N"] = N
    result["R_target"] = R_target
    result["r_target"] = r_target
    result["R_initial"] = float(R0)
    result["r_initial"] = float(r0)
    result["c_initial"] = int(c0)
    result["R_final"] = float(R_f)
    result["r_final"] = float(r_f)
    result["c_final"] = int(c_f)
    return result


def evaluate_outcome(res: dict) -> str:
    """Classify against pre-registered predictions."""
    R, r, c = res["R_final"], res["r_final"], res["c_final"]
    ratio = R / max(r, 1e-9)
    converged = res["converged"]
    if not converged:
        return f"P_X2c: no convergence (iter={res['iterations']}, lr={res['lr_final']:.2e})"
    if c != 3:
        return f"P_X2c: winding broken (c_final={c}, expected 3)"
    if 2.5 < ratio < 2.7:
        return f"P_X2a ✓ Golden Torus (R/r = {ratio:.3f} ≈ φ²)"
    if 2.2 < ratio < 2.35:
        return f"P_X2b: K4 classical attractor (R/r = {ratio:.3f} ≈ 2.27 convergence-study)"
    if 1.85 < ratio < 2.15:
        return f"P_X2b: full-Clifford classical (R/r = {ratio:.3f} ≈ 2.0)"
    return f"P_X2b: other attractor (R/r = {ratio:.3f})"


def plot_results(results: list, out_path: str) -> None:
    """3-panel per run × 2 runs: S11 history, R/r trajectory, c trajectory."""
    n = len(results)
    fig, axes = plt.subplots(n, 3, figsize=(15, 4.5 * n), squeeze=False)

    for row, res in enumerate(results):
        # Panel 1: S11 history
        ax = axes[row, 0]
        hist = np.array(res["s11_history"])
        ax.semilogy(hist, "b-", linewidth=1)
        ax.set_xlabel("gradient step")
        ax.set_ylabel("S11 (log)")
        ax.set_title(f"{res['label']} — S11 minimization"
                     f" [{'CONV' if res['converged'] else 'no conv'}]")
        ax.grid(alpha=0.3)

        # Panel 2: R/r trajectory
        ax = axes[row, 1]
        traj = res["trajectory"]
        if traj:
            steps = [t["step"] for t in traj]
            ratios = [t["R"] / max(t["r"], 1e-9) for t in traj]
            ax.plot(steps, ratios, "go-", markersize=5)
            ax.axhline(PHI**2, color="red", linestyle=":",
                       label=f"φ² = {PHI**2:.3f}")
            ax.axhline(2.27, color="blue", linestyle=":",
                       label="2.27 (conv study)")
            ax.axhline(2.0, color="orange", linestyle=":",
                       label="2.0 (classical)")
        ax.set_xlabel("gradient step")
        ax.set_ylabel("R/r")
        ax.set_title(f"{res['label']} — (R, r) trajectory")
        ax.grid(alpha=0.3)
        ax.legend(fontsize=8)

        # Panel 3: crossing count vs step
        ax = axes[row, 2]
        if traj:
            steps = [t["step"] for t in traj]
            cs = [t["c"] for t in traj]
            ax.plot(steps, cs, "ko-", markersize=5)
            ax.axhline(3, color="red", linestyle=":",
                       label="c=3 (electron target)")
        ax.set_xlabel("gradient step")
        ax.set_ylabel("crossing count c")
        ax.set_title(f"{res['label']} — topology preservation")
        ax.grid(alpha=0.3)
        ax.set_ylim(-0.5, 6)
        ax.legend(fontsize=8)

    plt.suptitle("Phase 3b X2 — Cosserat field (u, ω) + S11 relaxation",
                 y=1.00)
    plt.tight_layout()
    plt.savefig(out_path, dpi=110)
    plt.close(fig)


def main():
    print("=" * 72)
    print("PHASE 3b X2 — CosseratField3D + S11 minimization")
    print("Per §9.5 + §10.6 of 32_phase3b_axiom_compliant_redesign.md")
    print("=" * 72)

    # Two runs: N=72 (matches §8/X1), N=96 (plan-scoped)
    configs = [
        ("N=72 hedgehog", 72, 18.0, 18.0 / PHI**2),
        ("N=96 hedgehog", 96, 24.0, 24.0 / PHI**2),
    ]

    results = []
    for label, N, R_target, r_target in configs:
        print(f"\n--- {label} ---")
        res = run_cosserat_relax(
            N=N,
            R_target=R_target,
            r_target=r_target,
            max_iter=500,
            tol=1e-8,
            initial_lr=0.01,
            track_every=25,
            use_hedgehog=True,
            verbose=True,
        )
        res["label"] = label
        results.append(res)

    # Summary
    print()
    print("=" * 72)
    print("X2 RESULTS (Cosserat + S11)")
    print("=" * 72)
    print(f"{'label':>20} {'iter':>5} {'conv':>5} {'S11_final':>12} "
          f"{'R':>6} {'r':>6} {'R/r':>7} {'c':>3}")
    for res in results:
        rr = res["R_final"] / max(res["r_final"], 1e-9)
        print(
            f"{res['label']:>20} {res['iterations']:>5} "
            f"{'Y' if res['converged'] else 'N':>5} "
            f"{res['final_s11']:>12.4e} "
            f"{res['R_final']:>6.2f} {res['r_final']:>6.2f} "
            f"{rr:>7.3f} {res['c_final']:>3}"
        )

    # Outcome classification
    print()
    print("Pre-registered outcome evaluation:")
    for res in results:
        print(f"  {res['label']}:  {evaluate_outcome(res)}")

    # Save raw data
    save = {}
    for res in results:
        tag = res["label"].replace(" ", "_").replace("=", "")
        save[f"{tag}_s11_history"] = np.array(res["s11_history"])
        save[f"{tag}_converged"] = np.array([res["converged"]])
        save[f"{tag}_R_final"] = np.array([res["R_final"]])
        save[f"{tag}_r_final"] = np.array([res["r_final"]])
        save[f"{tag}_c_final"] = np.array([res["c_final"]])
        save[f"{tag}_iterations"] = np.array([res["iterations"]])
        if res["trajectory"]:
            save[f"{tag}_steps"] = np.array([t["step"] for t in res["trajectory"]])
            save[f"{tag}_R_traj"] = np.array([t["R"] for t in res["trajectory"]])
            save[f"{tag}_r_traj"] = np.array([t["r"] for t in res["trajectory"]])
            save[f"{tag}_c_traj"] = np.array([t["c"] for t in res["trajectory"]])
    np.savez("/tmp/phase3b_x2_cosserat.npz", **save)

    plot_results(results, "/tmp/phase3b_x2_cosserat.png")

    print()
    print("Raw data: /tmp/phase3b_x2_cosserat.npz")
    print("Figure:   /tmp/phase3b_x2_cosserat.png")


if __name__ == "__main__":
    main()
