"""
Phase 3b X4 — constrained S11 at Ch 8 Golden Torus.

Per 34_x4_constrained_s11.md, three tests:

  X4a: amplitude sweep at Ch 8 Golden Torus (R/r = φ²). Geometry FIXED.
       At each amplitude, measure S11, shell |Γ|²_max, exterior |Γ|²_sum,
       shell A²_max. NO gradient descent.
       Pre-registered: some amplitude produces shell Γ²→1 AND ext Γ²→0.

  X4b: at X4a's best amplitude, run relax_s11 and measure drift.
       Pre-registered: stable R/r and shell Γ² under relaxation.

  X4c: classical control — amplitude sweep at R/r = 2.0 (full Clifford,
       no half-cover). Diagnostic: if classical also shows shell Γ→-1,
       then simulation cannot distinguish electron from classical Hopfion.

Output: /tmp/phase3b_x4.{npz,png}, /tmp/phase3b_x4_log.txt
"""
from __future__ import annotations

import numpy as np
import jax.numpy as jnp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.topological.cosserat_field_3d import (
    CosseratField3D,
    _s11_density, _compute_strain, _compute_curvature,
)

PHI = (1.0 + np.sqrt(5.0)) / 2.0
PI = np.pi


def post_hoc_gamma_and_A2(solver: CosseratField3D) -> dict:
    """Compute local |Γ|² and saturation A² fields on the converged state,
    return shell/exterior statistics."""
    u = jnp.asarray(solver.u)
    w = jnp.asarray(solver.omega)
    mask = jnp.asarray(solver.mask_alive)
    dx = solver.dx
    om_y = float(solver.omega_yield)
    eps_y = float(solver.epsilon_yield)

    gamma_sq = np.asarray(
        _s11_density(u, w, dx, om_y, eps_y) * mask.astype(jnp.float64)
    )
    eps = _compute_strain(u, w, dx)
    kappa = _compute_curvature(w, dx)
    eps_sq = np.asarray(jnp.sum(eps * eps, axis=(-1, -2)))
    kappa_sq = np.asarray(jnp.sum(kappa * kappa, axis=(-1, -2)))
    A_sq = eps_sq / (eps_y ** 2) + kappa_sq / (om_y ** 2)
    A_sq = np.where(np.asarray(mask), A_sq, 0.0)

    # Shell and exterior masks relative to soliton center
    R, r = solver.extract_shell_radii()
    nx, ny, nz = solver.nx, solver.ny, solver.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0
    ix = np.indices((nx, ny, nz))
    xs = ix[0] - cx; ys = ix[1] - cy; zs = ix[2] - cz
    rho_xy = np.sqrt(xs ** 2 + ys ** 2)
    rho_tube = np.sqrt((rho_xy - max(R, 1.0)) ** 2 + zs ** 2)
    shell_mask = (rho_tube <= max(r, 1.0)) & np.asarray(mask)
    exterior_mask = (rho_tube > 2 * max(r, 1.0)) & np.asarray(mask)

    return {
        "R": float(R), "r": float(r),
        "shell_gamma_sq_max": float(gamma_sq[shell_mask].max()) if shell_mask.any() else 0.0,
        "shell_gamma_sq_mean": float(gamma_sq[shell_mask].mean()) if shell_mask.any() else 0.0,
        "exterior_gamma_sq_sum": float(gamma_sq[exterior_mask].sum()),
        "total_gamma_sq_sum": float(gamma_sq.sum()),
        "shell_A_sq_max": float(A_sq[shell_mask].max()) if shell_mask.any() else 0.0,
        "shell_A_sq_mean": float(A_sq[shell_mask].mean()) if shell_mask.any() else 0.0,
    }


def measure_at_amplitude(R_target: float, r_target: float,
                         amp_target: float, N: int = 72) -> dict:
    """Init hedgehog at (R, r), scale ω field so peak amplitude = amp_target,
    measure S11 + post-hoc Γ/A² — NO gradient descent."""
    solver = CosseratField3D(N, N, N, dx=1.0, use_saturation=True)
    # Initialize — uses canonical peak amplitude √3/2 · π by default
    solver.initialize_electron_2_3_sector(
        R_target=R_target, r_target=r_target, use_hedgehog=True,
    )
    # Rescale the ω field to match amp_target as PEAK |ω|
    current_peak = float(np.max(np.sqrt(np.sum(solver.omega ** 2, axis=-1))))
    if current_peak > 1e-30:
        solver.omega *= amp_target / current_peak
    S11 = float(solver.total_s11())
    E = float(solver.total_energy())
    diag = post_hoc_gamma_and_A2(solver)
    c = int(solver.extract_crossing_count())
    return {
        "R_target": R_target, "r_target": r_target,
        "amp_target": amp_target,
        "S11": S11, "E": E, "c": c, **diag,
    }


def run_amplitude_sweep(label: str, R_target: float, r_target: float,
                        amplitudes: list[float], N: int = 72) -> list[dict]:
    """X4a / X4c — parameter sweep over amplitude at fixed geometry."""
    print(f"\n=== {label}: R/r = {R_target/r_target:.3f} "
          f"(R={R_target}, r={r_target:.3f}) ===")
    results = []
    for amp in amplitudes:
        r = measure_at_amplitude(R_target, r_target, amp, N=N)
        ext_frac = r["exterior_gamma_sq_sum"] / max(r["total_gamma_sq_sum"], 1e-30)
        print(
            f"  |ω|_peak={amp:.3f}: S11={r['S11']:.2e}  "
            f"shell_Γ²_max={r['shell_gamma_sq_max']:.3f}  "
            f"ext/tot={ext_frac:.2%}  "
            f"A²_max={r['shell_A_sq_max']:.2f}  c={r['c']}"
        )
        results.append(r)
    return results


def find_electron_amplitude(results: list[dict]) -> dict | None:
    """Per P_X4a.1 criteria: shell_Γ²_max ≥ 0.9 AND ext/total ≤ 0.1.
    Returns the best candidate (maximizing shell_Γ²_max subject to
    ext_frac ≤ 0.1) if any, else None."""
    candidates = []
    for r in results:
        ext_frac = r["exterior_gamma_sq_sum"] / max(r["total_gamma_sq_sum"], 1e-30)
        if r["shell_gamma_sq_max"] >= 0.9 and ext_frac <= 0.1:
            candidates.append((r["shell_gamma_sq_max"], r))
    if not candidates:
        return None
    candidates.sort(key=lambda x: -x[0])
    return candidates[0][1]


def run_relax_at_amplitude(R_target: float, r_target: float,
                           amp_target: float, N: int = 72,
                           max_iter: int = 200) -> dict:
    """X4b — initialize at (R, r, amp), run relax_s11, measure drift."""
    solver = CosseratField3D(N, N, N, dx=1.0, use_saturation=True)
    solver.initialize_electron_2_3_sector(
        R_target=R_target, r_target=r_target, use_hedgehog=True,
    )
    current_peak = float(np.max(np.sqrt(np.sum(solver.omega ** 2, axis=-1))))
    if current_peak > 1e-30:
        solver.omega *= amp_target / current_peak

    R0, r0 = solver.extract_shell_radii()
    S11_0 = float(solver.total_s11())
    diag0 = post_hoc_gamma_and_A2(solver)
    print(f"\n--- X4b relaxation from (R/r={R0/max(r0,1e-9):.3f}, "
          f"|ω|_peak={amp_target:.3f}) ---")
    print(f"  Initial: S11={S11_0:.3e}, shell_Γ²={diag0['shell_gamma_sq_max']:.3f}")

    result = solver.relax_s11(
        max_iter=max_iter, tol=1e-8, initial_lr=0.01,
        verbose=False, track_topology_every=25,
    )

    R_f, r_f = solver.extract_shell_radii()
    S11_f = float(solver.total_s11())
    diag_f = post_hoc_gamma_and_A2(solver)
    ext_frac_f = diag_f["exterior_gamma_sq_sum"] / max(diag_f["total_gamma_sq_sum"], 1e-30)
    drift_ratio = (R_f / max(r_f, 1e-9)) / (R0 / max(r0, 1e-9))
    print(f"  Final:   (R/r={R_f/max(r_f,1e-9):.3f}, drift={drift_ratio:.3f}x)")
    print(f"           S11={S11_f:.3e}, shell_Γ²={diag_f['shell_gamma_sq_max']:.3f}, "
          f"ext/tot={ext_frac_f:.2%}, iter={result['iterations']}")

    return {
        "R_initial": R0, "r_initial": r0, "S11_initial": S11_0,
        **{f"init_{k}": v for k, v in diag0.items()},
        "R_final": R_f, "r_final": r_f, "S11_final": S11_f,
        **{f"final_{k}": v for k, v in diag_f.items()},
        "iterations": result["iterations"],
        "converged": result["converged"],
    }


def plot_results(x4a: list[dict], x4c: list[dict], out_path: str) -> None:
    """4-panel figure: shell Γ² vs amp + ext frac vs amp + S11 vs amp +
    A² vs amp, comparing X4a (Golden Torus) vs X4c (classical)."""
    amps_a = [r["amp_target"] for r in x4a]
    amps_c = [r["amp_target"] for r in x4c]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    ax = axes[0, 0]
    ax.plot(amps_a, [r["shell_gamma_sq_max"] for r in x4a], "bo-",
            label="X4a: R/r = φ² (Ch 8 Golden Torus)")
    ax.plot(amps_c, [r["shell_gamma_sq_max"] for r in x4c], "gs-",
            label="X4c: R/r = 2.0 (classical full-Clifford)")
    ax.axhline(1.0, color="red", linestyle=":", label="|Γ|²=1 (TIR)")
    ax.axvline(np.sqrt(3)/2 * PI, color="gray", linestyle=":",
               label="Regime II/III = √3/2·π")
    ax.set_xlabel("peak |ω| amplitude")
    ax.set_ylabel("shell |Γ|²_max")
    ax.set_title("Shell |Γ|² — does it reach 1 (TIR) at any amplitude?")
    ax.grid(alpha=0.3); ax.legend(fontsize=8)

    ax = axes[0, 1]
    ax.plot(amps_a, [r["exterior_gamma_sq_sum"] / max(r["total_gamma_sq_sum"], 1e-30)
                     for r in x4a], "bo-", label="X4a φ²")
    ax.plot(amps_c, [r["exterior_gamma_sq_sum"] / max(r["total_gamma_sq_sum"], 1e-30)
                     for r in x4c], "gs-", label="X4c 2.0")
    ax.axhline(0.1, color="red", linestyle=":", label="0.1 threshold")
    ax.set_xlabel("peak |ω| amplitude")
    ax.set_ylabel("exterior |Γ|² fraction")
    ax.set_title("Exterior reflection fraction — low means vacuum-matched outside")
    ax.grid(alpha=0.3); ax.legend(fontsize=8)

    ax = axes[1, 0]
    ax.semilogy(amps_a, [r["S11"] for r in x4a], "bo-", label="X4a φ²")
    ax.semilogy(amps_c, [r["S11"] for r in x4c], "gs-", label="X4c 2.0")
    ax.set_xlabel("peak |ω| amplitude")
    ax.set_ylabel("total S11 (log)")
    ax.set_title("Total S11 — overall impedance mismatch integrated")
    ax.grid(alpha=0.3); ax.legend(fontsize=8)

    ax = axes[1, 1]
    ax.plot(amps_a, [r["shell_A_sq_max"] for r in x4a], "bo-", label="X4a φ²")
    ax.plot(amps_c, [r["shell_A_sq_max"] for r in x4c], "gs-", label="X4c 2.0")
    ax.axhline(1.0, color="red", linestyle=":", label="A²=1 (saturation onset)")
    ax.axhline(3/4, color="orange", linestyle=":", label="A²=3/4 (Regime II/III)")
    ax.set_xlabel("peak |ω| amplitude")
    ax.set_ylabel("shell A²_max (saturation)")
    ax.set_title("Shell saturation — A²→1 means TIR engaged (Axiom 4)")
    ax.grid(alpha=0.3); ax.legend(fontsize=8)

    plt.suptitle("Phase 3b X4 — amplitude sweep at Ch 8 constraints",
                 y=1.00)
    plt.tight_layout()
    plt.savefig(out_path, dpi=110)
    plt.close(fig)


def main():
    print("=" * 72)
    print("PHASE 3b X4 — constrained S11 at Ch 8 Golden Torus")
    print("Pre-registered in research/_archive/L3_electron_soliton/"
          "34_x4_constrained_s11.md")
    print("=" * 72)

    N = 72
    # Ch 8 Golden Torus: R/r = φ², scaled to N
    R_golden = N / 4.0              # = 18.0 for N=72
    r_golden = R_golden / (PHI ** 2)  # ≈ 6.875

    # Classical full-Clifford: R/r = 2.0
    R_classical = R_golden
    r_classical = R_golden / 2.0     # = 9.0

    # Amplitude sweep: Regime I through III boundary
    amplitudes = [0.3 * PI, 0.5 * PI, 0.7 * PI,
                  np.sqrt(3) / 2 * PI, PI, 1.2 * PI]
    print(f"\nLattice: N={N}, use_saturation=True")
    print(f"Golden Torus (X4a): R={R_golden:.3f}, r={r_golden:.3f}, "
          f"R/r={R_golden/r_golden:.3f}")
    print(f"Classical  (X4c): R={R_classical:.3f}, r={r_classical:.3f}, "
          f"R/r={R_classical/r_classical:.3f}")
    print(f"Amplitudes: {[f'{a:.3f}' for a in amplitudes]}")

    # X4a — Golden Torus sweep
    x4a = run_amplitude_sweep("X4a", R_golden, r_golden, amplitudes, N=N)

    # X4c — classical sweep
    x4c = run_amplitude_sweep("X4c", R_classical, r_classical, amplitudes, N=N)

    # Find electron amplitude per P_X4a.1
    electron_candidate = find_electron_amplitude(x4a)
    classical_candidate = find_electron_amplitude(x4c)

    print()
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    if electron_candidate:
        print(f"X4a electron candidate found: amp={electron_candidate['amp_target']:.3f}, "
              f"shell_Γ²={electron_candidate['shell_gamma_sq_max']:.3f}")
    else:
        print("X4a: NO amplitude met P_X4a.1 criteria (shell_Γ²≥0.9, ext_frac≤0.1)")

    if classical_candidate:
        print(f"X4c classical candidate found: amp={classical_candidate['amp_target']:.3f}, "
              f"shell_Γ²={classical_candidate['shell_gamma_sq_max']:.3f}")
    else:
        print("X4c: NO amplitude met criteria — classical geometry does NOT give TIR")

    # X4b — if X4a found a candidate, run relaxation from it
    x4b_result = None
    if electron_candidate:
        print()
        print("=" * 72)
        print("X4b — stability check at identified electron amplitude")
        print("=" * 72)
        x4b_result = run_relax_at_amplitude(
            R_golden, r_golden, electron_candidate["amp_target"],
            N=N, max_iter=200,
        )
    else:
        print()
        print("X4b skipped — no X4a candidate to check")

    # Pre-registered outcome evaluation
    print()
    print("Pre-registered outcome evaluation:")
    if electron_candidate and x4b_result:
        drift = (x4b_result["R_final"] / max(x4b_result["r_final"], 1e-9)) \
            / (x4b_result["R_initial"] / max(x4b_result["r_initial"], 1e-9))
        if abs(drift - 1.0) < 0.05 and \
           x4b_result["final_shell_gamma_sq_max"] >= 0.9:
            verdict = "P_X4a.1 + P_X4b: ELECTRON found and stable"
        elif abs(drift - 1.0) >= 0.05:
            verdict = (f"P_X4a.1 held but X4b showed R/r drift "
                       f"({drift:.3f}x); electron amplitude not stationary")
        else:
            verdict = "P_X4a.1 held but shell_Γ² collapsed under relaxation"
    elif electron_candidate:
        verdict = "P_X4a.1 partial — needs X4b to confirm stability"
    else:
        verdict = "P_X4a.2: no electron amplitude in hedgehog family at Golden Torus"

    if classical_candidate and electron_candidate:
        verdict += " | X4c ALSO found classical candidate — simulation " \
                   "CANNOT distinguish electron from classical Hopfion"
    elif classical_candidate and not electron_candidate:
        verdict += " | X4c found classical; X4a did not — " \
                   "simulation prefers classical geometry"

    print(f"  → {verdict}")

    # Save
    save = {"amplitudes": np.array(amplitudes)}
    for i, r in enumerate(x4a):
        for key in ["S11", "shell_gamma_sq_max", "exterior_gamma_sq_sum",
                    "total_gamma_sq_sum", "shell_A_sq_max", "E"]:
            save.setdefault(f"x4a_{key}", []).append(r[key])
    for i, r in enumerate(x4c):
        for key in ["S11", "shell_gamma_sq_max", "exterior_gamma_sq_sum",
                    "total_gamma_sq_sum", "shell_A_sq_max", "E"]:
            save.setdefault(f"x4c_{key}", []).append(r[key])
    save = {k: np.array(v) if isinstance(v, list) else v for k, v in save.items()}
    np.savez("/tmp/phase3b_x4.npz", **save)
    plot_results(x4a, x4c, "/tmp/phase3b_x4.png")

    print()
    print("Raw data: /tmp/phase3b_x4.npz")
    print("Figure:   /tmp/phase3b_x4.png")


if __name__ == "__main__":
    main()
