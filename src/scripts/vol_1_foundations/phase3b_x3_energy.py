"""
Phase 3b X3 — energy minimization on rich Cosserat functional.

Pre-registered in research/_archive/L3_electron_soliton/33_phase3b_x3_energy_analysis.md.

Test: does `relax_to_ground_state()` on the Cosserat field (with Op10 + Hopf +
reflection + saturation-modulated elastic terms) select the electron when
`relax_s11()` selects the photon?

Seeds — identical to X2-prime for direct comparison:
  R/r = 2.0, 2.618 (φ²), 4.0    (3 seeds; 3.5 added if compute budget allows)

Diagnostics at convergence (built-in + post-hoc module functions):
  - R/r via extract_shell_radii
  - c via extract_crossing_count
  - total energy, total S11
  - external vs at-shell |Γ|² (post-hoc via _s11_density + radial mask)
  - saturation amplitude A² at shell (post-hoc from ε, κ)
  - Λ decomposition (Op10, reflection, Hopf) post-hoc per term

Outputs:
  /tmp/phase3b_x3_energy.npz    — raw data
  /tmp/phase3b_x3_energy.png    — figure
"""
from __future__ import annotations

import numpy as np
import jax.numpy as jnp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.topological.cosserat_field_3d import (
    CosseratField3D,
    _s11_density, _op10_density, _hopf_density, _reflection_density,
    _compute_strain, _compute_curvature,
)

PHI = (1.0 + np.sqrt(5.0)) / 2.0


def post_hoc_diagnostics(solver: CosseratField3D) -> dict:
    """Compute shell-boundary Γ, saturation A² at shell, and Λ decomposition
    on the converged state via module-level density functions."""
    u = jnp.asarray(solver.u)
    w = jnp.asarray(solver.omega)
    mask = jnp.asarray(solver.mask_alive)
    dx = solver.dx
    om_y = float(solver.omega_yield)
    eps_y = float(solver.epsilon_yield)

    # Local |Γ|² density at each site
    gamma_sq = np.asarray(
        _s11_density(u, w, dx, om_y, eps_y) * mask.astype(jnp.float64)
    )

    # Saturation amplitude A² field
    eps = _compute_strain(u, w, dx)
    kappa = _compute_curvature(w, dx)
    eps_sq = np.asarray(jnp.sum(eps * eps, axis=(-1, -2)))
    kappa_sq = np.asarray(jnp.sum(kappa * kappa, axis=(-1, -2)))
    A_sq = eps_sq / (eps_y ** 2) + kappa_sq / (om_y ** 2)
    A_sq = np.where(np.asarray(mask), A_sq, 0.0)

    # Λ decomposition — integrate each term separately
    vol_element = dx ** 3
    op10_field = np.asarray(_op10_density(w, dx) * mask.astype(jnp.float64))
    hopf_field = np.asarray(_hopf_density(w, dx) * mask.astype(jnp.float64))
    refl_field = np.asarray(
        _reflection_density(u, w, dx, om_y, eps_y) * mask.astype(jnp.float64)
    )
    Lambda_Op10 = float(op10_field.sum()) * vol_element
    Lambda_Hopf = float(hopf_field.sum()) * vol_element
    Lambda_refl = float(refl_field.sum()) * vol_element

    # Shell mask — radial annulus around soliton center at z-equator slab
    R, r = solver.extract_shell_radii()
    nx, ny, nz = solver.nx, solver.ny, solver.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0
    ix = np.indices((nx, ny, nz))
    xs = ix[0] - cx; ys = ix[1] - cy; zs = ix[2] - cz
    rho_xy = np.sqrt(xs ** 2 + ys ** 2)
    rho_tube = np.sqrt((rho_xy - R) ** 2 + zs ** 2)
    shell_mask = (rho_tube <= r) & (rho_tube > 0)        # inside tube
    exterior_mask = (rho_tube > 2 * r)                    # clearly outside

    shell_gamma_sq_max = float(gamma_sq[shell_mask & np.asarray(mask)].max()) \
        if (shell_mask & np.asarray(mask)).sum() > 0 else 0.0
    exterior_gamma_sq_sum = float(gamma_sq[exterior_mask & np.asarray(mask)].sum())
    total_gamma_sq_sum = float(gamma_sq.sum())
    shell_A_sq_max = float(A_sq[shell_mask & np.asarray(mask)].max()) \
        if (shell_mask & np.asarray(mask)).sum() > 0 else 0.0

    return {
        "R": float(R),
        "r": float(r),
        "shell_gamma_sq_max": shell_gamma_sq_max,
        "exterior_gamma_sq_sum": exterior_gamma_sq_sum,
        "total_gamma_sq_sum": total_gamma_sq_sum,
        "shell_A_sq_max": shell_A_sq_max,
        "Lambda_Op10": Lambda_Op10,
        "Lambda_Hopf": Lambda_Hopf,
        "Lambda_refl": Lambda_refl,
    }


def run_seed(label: str, R_target: float, r_target: float,
             N: int = 72, max_iter: int = 500) -> dict:
    print(f"\n--- seed {label}: R={R_target}, r={r_target:.3f}, "
          f"R/r={R_target/r_target:.3f} ---")
    solver = CosseratField3D(N, N, N, dx=1.0, use_saturation=True)
    solver.initialize_electron_2_3_sector(
        R_target=R_target, r_target=r_target, use_hedgehog=True,
    )

    R0, r0 = solver.extract_shell_radii()
    c0 = solver.extract_crossing_count()
    E0 = float(solver.total_energy())
    S11_0 = float(solver.total_s11())
    print(f"  Initial: (R, r) = ({R0:.3f}, {r0:.3f}), R/r = "
          f"{R0/max(r0,1e-9):.3f}, c = {c0}")
    print(f"           E = {E0:.4e}, S11 = {S11_0:.4e}")

    print(f"  Running relax_to_ground_state(max_iter={max_iter}, tol=1e-8, "
          f"lr=0.01)...")
    result = solver.relax_to_ground_state(
        max_iter=max_iter, tol=1e-8, initial_lr=0.01,
        verbose=False, track_topology_every=25,
    )

    R_f, r_f = solver.extract_shell_radii()
    c_f = solver.extract_crossing_count()
    E_f = float(solver.total_energy())
    S11_f = float(solver.total_s11())
    ratio_f = R_f / max(r_f, 1e-9)
    print(f"  Final:   (R, r) = ({R_f:.3f}, {r_f:.3f}), R/r = "
          f"{ratio_f:.3f}, c = {c_f}")
    print(f"           E = {E_f:.4e} (Δ = {E_f-E0:+.4e}), "
          f"S11 = {S11_f:.4e} [{result['iterations']} iter, "
          f"{'conv' if result['converged'] else 'no conv'}]")

    # Post-hoc diagnostics
    diag = post_hoc_diagnostics(solver)
    shell_ext_ratio = diag["exterior_gamma_sq_sum"] / max(
        diag["total_gamma_sq_sum"], 1e-30)
    print(f"  Post-hoc: shell |Γ|²_max = {diag['shell_gamma_sq_max']:.3f}, "
          f"exterior/total = {shell_ext_ratio:.3%}")
    print(f"            shell A²_max = {diag['shell_A_sq_max']:.3f}  "
          f"(→1 means TIR engaged)")
    print(f"            Λ: Op10={diag['Lambda_Op10']:.3e}, "
          f"refl={diag['Lambda_refl']:.3e}, Hopf={diag['Lambda_Hopf']:.3e}")
    print(f"            Ch 8 targets: 4π²={4*np.pi**2:.2f}, π={np.pi:.2f}, "
          f"4π³={4*np.pi**3:.2f}")

    out = dict(result)
    out.update({
        "label": label,
        "R_target": R_target,
        "r_target": r_target,
        "R_initial": float(R0),
        "r_initial": float(r0),
        "c_initial": int(c0),
        "E_initial": E0,
        "S11_initial": S11_0,
        "R_final": float(R_f),
        "r_final": float(r_f),
        "c_final": int(c_f),
        "E_final": E_f,
        "S11_final": S11_f,
        **diag,
    })
    return out


def classify(res: dict) -> str:
    R, r, c = res["R_final"], res["r_final"], res["c_final"]
    ratio = R / max(r, 1e-9)
    shell_gamma = res["shell_gamma_sq_max"]
    ext_ratio = res["exterior_gamma_sq_sum"] / max(
        res["total_gamma_sq_sum"], 1e-30)
    shell_A = res["shell_A_sq_max"]

    if not res["converged"]:
        return "P_X3d: no convergence"
    if c != 3:
        return f"P_X3d: c changed to {c}"
    # Topology + convergence OK. Check geometry + Γ structure.
    if 2.5 < ratio < 2.7:
        if shell_gamma > 0.9 and ext_ratio < 0.05:
            return "P_X3a ✓ Golden Torus + TIR shell + external match — ELECTRON"
        return f"P_X3a partial (R/r=φ² but Γ structure not confirmed: " \
               f"shell_Γ²={shell_gamma:.2f}, ext_frac={ext_ratio:.2%})"
    # Non-φ² ratio
    if shell_gamma > 0.9 and ext_ratio < 0.05:
        return f"P_X3b: bound state at R/r={ratio:.3f} (≠ φ²)"
    return f"P_X3b/c: R/r={ratio:.3f}, shell_Γ²={shell_gamma:.2f}, " \
           f"A²={shell_A:.2f}, ext={ext_ratio:.2%}"


def main():
    print("=" * 72)
    print("PHASE 3b X3 — Cosserat energy minimization (rich functional)")
    print("Pre-registered in research/_archive/L3_electron_soliton/"
          "33_phase3b_x3_energy_analysis.md")
    print("=" * 72)

    N = 72
    R_target = 18.0
    seeds = [
        ("R/r=2.0 (classical)",  R_target, R_target / 2.0),
        ("R/r=2.618 (φ²)",       R_target, R_target / (PHI ** 2)),
        ("R/r=4.0 (far)",        R_target, R_target / 4.0),
        # R/r=3.5 added only if wall clock permits
    ]

    results = []
    for label, R_t, r_t in seeds:
        res = run_seed(label, R_t, r_t, N=N, max_iter=500)
        results.append(res)

    # Summary table
    print()
    print("=" * 72)
    print("X3 SUMMARY")
    print("=" * 72)
    print(f"{'seed':>22} {'R/r_f':>6} {'c':>2} {'shell_Γ²':>9} "
          f"{'ext/tot':>9} {'A²_shell':>9} {'E_final':>11} {'iter':>5}")
    for res in results:
        ratio = res["R_final"] / max(res["r_final"], 1e-9)
        ext_frac = res["exterior_gamma_sq_sum"] / max(
            res["total_gamma_sq_sum"], 1e-30)
        print(
            f"{res['label']:>22} {ratio:>6.3f} {res['c_final']:>2} "
            f"{res['shell_gamma_sq_max']:>9.3f} {ext_frac:>9.3%} "
            f"{res['shell_A_sq_max']:>9.3f} {res['E_final']:>11.3e} "
            f"{res['iterations']:>5}"
        )

    print()
    print("Verdicts:")
    for res in results:
        print(f"  {res['label']:>22} → {classify(res)}")

    # Save
    save = {}
    for res in results:
        tag = res["label"].replace(" ", "_").replace("(", "").replace(")", "") \
            .replace("/", "_").replace(".", "p").replace("=", "_") \
            .replace("²", "sq")
        save[f"{tag}_energy_history"] = np.array(res["energy_history"]) \
            if "energy_history" in res else np.array(res.get("s11_history", []))
        for key in ["R_final", "r_final", "c_final", "E_final", "S11_final",
                    "shell_gamma_sq_max", "exterior_gamma_sq_sum",
                    "total_gamma_sq_sum", "shell_A_sq_max",
                    "Lambda_Op10", "Lambda_Hopf", "Lambda_refl"]:
            save[f"{tag}_{key}"] = np.array([res[key]])
        if res.get("trajectory"):
            save[f"{tag}_steps"] = np.array([t["step"] for t in res["trajectory"]])
            save[f"{tag}_R_traj"] = np.array([t["R"] for t in res["trajectory"]])
            save[f"{tag}_r_traj"] = np.array([t["r"] for t in res["trajectory"]])
            save[f"{tag}_c_traj"] = np.array([t["c"] for t in res["trajectory"]])
    np.savez("/tmp/phase3b_x3_energy.npz", **save)

    # Plot: R/r vs step + energy history
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    colors = plt.cm.viridis(np.linspace(0, 0.9, len(results)))

    ax = axes[0]
    for res, color in zip(results, colors):
        traj = res.get("trajectory", [])
        if traj:
            steps = [0] + [t["step"] for t in traj]
            ratios = [res["R_initial"] / max(res["r_initial"], 1e-9)]
            ratios += [t["R"] / max(t["r"], 1e-9) for t in traj]
            ax.plot(steps, ratios, "o-", color=color,
                    label=res["label"], markersize=5)
    ax.axhline(PHI ** 2, color="red", linestyle="--", linewidth=2,
               label=f"φ² = {PHI**2:.3f}")
    ax.axhline(2.0, color="gray", linestyle=":", label="classical 2.0")
    ax.set_xlabel("energy gradient step")
    ax.set_ylabel("R/r")
    ax.set_title("R/r trajectory per seed (energy min)")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    ax = axes[1]
    for res, color in zip(results, colors):
        hist_key = "energy_history"
        if hist_key not in res:
            hist_key = "s11_history"
        hist = np.array(res.get(hist_key, []))
        if len(hist):
            # The energy may go negative due to Hopf topological term; abs for log plot
            ax.plot(np.abs(hist - hist[-1]) + 1e-30,
                    color=color, label=res["label"], linewidth=1)
    ax.set_yscale("log")
    ax.set_xlabel("gradient step")
    ax.set_ylabel("|E - E_final| (log)")
    ax.set_title("Energy relaxation progress")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    plt.suptitle("Phase 3b X3 — Cosserat energy min + seed independence",
                 y=1.02)
    plt.tight_layout()
    plt.savefig("/tmp/phase3b_x3_energy.png", dpi=110)
    plt.close(fig)

    print()
    print("Raw data: /tmp/phase3b_x3_energy.npz")
    print("Figure:   /tmp/phase3b_x3_energy.png")


if __name__ == "__main__":
    main()