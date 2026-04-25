"""
Coupled K4+Cosserat eigenmode finder — Round 6 followup F17-G.

Analog of `solve_eigenmode_self_consistent` (tlm_electron_soliton_eigenmode.py:668)
but operating on the full VacuumEngine3D with BOTH sectors seeded.

Per doc 66_ §17 the K4-only eigenmode finder is the AVE-native methodology
for finding standing-wave fixed points. K4-only is "exhausted" for the
electron per Vol 1 Ch 8:49-50 — the coupled K4+Cosserat is what should
host the bound (2,3) state. This function is the natural extension.

**Empirical caveat:** Path C (joint seed under undamped VacuumEngine3D
dynamics) showed catastrophic energy runaway — E grew 4 million× from seed
in 20 steps. So this function explicitly tracks energy and aborts on
runaway, treating divergence as an empirical finding rather than a bug.

Convergence taxonomy:
  - "converged": geometry stable to tolerance, topology preserved,
    energy bounded
  - "diverged": energy explosion (>energy_explosion_factor × seed E)
  - "topology_lost": geometry stable but N_crossings drifted off (2,3)
  - "max_iter_no_converge": ran out of iterations

Output: trajectory, final (R, r), final crossing count, convergence status.
"""
from __future__ import annotations

import sys
from dataclasses import dataclass

import numpy as np
import jax.numpy as jnp

from ave.core.constants import V_YIELD
from ave.topological.vacuum_engine import VacuumEngine3D
from ave.topological.cosserat_field_3d import _s11_density

sys.path.insert(0, "/Users/grantlindblom/AVE-staging/AVE-Core/src/scripts/vol_1_foundations")
from tlm_electron_soliton_eigenmode import (
    initialize_2_3_voltage_ansatz,
    extract_crossing_count_tlm,
    shell_envelope,
)


PHI = (1.0 + np.sqrt(5.0)) / 2.0
PHI_SQ = PHI ** 2


@dataclass
class CoupledEigenmodeResult:
    converged: bool
    status: str               # "converged" | "diverged" | "topology_lost" | "max_iter_no_converge"
    iterations: int
    trajectory: list          # list of (R, r, c, E, peak_omega) per outer iter
    final_R: float
    final_r: float
    final_c: int
    final_E: float
    final_peak_omega: float


def _compute_combined_magnitude(engine: VacuumEngine3D) -> np.ndarray:
    """Time-instant combined-magnitude scalar field for shell extraction.

    Sums squared field amplitudes across all three storage modes
    (strain via Cosserat u, curvature via Cosserat ω, pressure via K4
    V_inc) — the per-site total field energy density. Matches §14.1 / §17.2
    framing: A² = local energy density across electric, magnetic, and
    pressure-stored sectors.
    """
    cos = engine.cos
    k4 = engine.k4
    omega_mag_sq = np.sum(np.asarray(cos.omega) ** 2, axis=-1)
    u_mag_sq = np.sum(np.asarray(cos.u) ** 2, axis=-1)
    V_mag_sq = np.sum(np.asarray(k4.V_inc) ** 2, axis=-1)
    # Each contribution normalized to its own yield/scale, then summed.
    # ε² ↔ ε_yield²; κ² ↔ ω_yield² (curvature has same scale); V² ↔ V_SNAP².
    # u contribution is approximate (full ε requires gradient); for shell
    # extraction this is adequate as a localization indicator.
    eps_y2 = float(cos.epsilon_yield) ** 2
    om_y2 = float(cos.omega_yield) ** 2
    V_S2 = float(engine.V_SNAP) ** 2
    combined = u_mag_sq / max(eps_y2, 1e-30) + omega_mag_sq / max(om_y2, 1e-30) + V_mag_sq / max(V_S2, 1e-30)
    return np.sqrt(combined)


def _seed_both_sectors(
    engine: VacuumEngine3D,
    R: float,
    r: float,
    cos_amp_scale: float,
    k4_amplitude: float,
) -> None:
    """Seed (2,3) ansatz in both sectors, sharing winding phase θ=2φ+3ψ.

    Cosserat ω: hedgehog envelope at amplitude_scale (peak |ω|=0.3π
    when amp_scale=0.3464 per doc 34_ §9.4 / doc 66_ §14.3).

    K4 V_inc: chiral-phasor pattern via initialize_2_3_voltage_ansatz
    at amplitude k4_amplitude. Same θ winding.
    """
    engine.cos.initialize_electron_2_3_sector(
        R_target=R, r_target=r, use_hedgehog=True,
        amplitude_scale=cos_amp_scale,
    )
    initialize_2_3_voltage_ansatz(engine.k4, R=R, r=r, amplitude=k4_amplitude)


def _run_inner(
    engine: VacuumEngine3D,
    n_steps: int,
    energy_seed: float,
    energy_explosion_factor: float,
    rms_avg_last_n: int = 30,
) -> tuple[dict, bool]:
    """Run engine forward n_steps; accumulate combined-magnitude RMS over
    last rms_avg_last_n steps; track per-step energy for divergence detection.

    Returns (diagnostics, diverged_flag). On divergence, returns early.
    """
    nx = engine.cos.nx
    cx = (nx - 1) / 2.0
    cy = (nx - 1) / 2.0
    cz = (nx - 1) / 2.0

    rms_accumulator = np.zeros((nx, nx, nx), dtype=np.float64)
    rms_count = 0
    rms_start = max(1, n_steps - rms_avg_last_n + 1)

    energies = []
    diverged = False

    for step in range(1, n_steps + 1):
        engine.step()
        E_now = float(engine.cos.total_energy())
        energies.append(E_now)
        if abs(E_now) > energy_explosion_factor * abs(energy_seed):
            diverged = True
            break
        if step >= rms_start:
            mag = _compute_combined_magnitude(engine)
            rms_accumulator += mag ** 2
            rms_count += 1

    if rms_count > 0:
        rms_field = np.sqrt(rms_accumulator / rms_count)
    else:
        rms_field = _compute_combined_magnitude(engine)

    R_rms, r_rms = shell_envelope(rms_field, cx, cy, cz)
    c_extracted = extract_crossing_count_tlm(engine.k4, R_major=R_rms)
    peak_omega = float(np.max(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1)))
    final_E = energies[-1] if energies else 0.0

    return {
        "R_rms": float(R_rms),
        "r_rms": float(r_rms),
        "c": int(c_extracted),
        "E_final": final_E,
        "E_max": max(abs(e) for e in energies) if energies else 0.0,
        "peak_omega": peak_omega,
        "n_steps_run": len(energies),
        "energy_trajectory": energies,
    }, diverged


def solve_eigenmode_coupled_engine(
    N: int = 48,
    pml: int = 4,
    R_seed: float = 12.0,
    r_seed: float | None = None,
    cos_amp_scale: float = 0.3 / (np.sqrt(3.0) / 2.0),  # peak |ω|=0.3π per doc 34_ §9.4
    k4_amplitude: float = 0.9 * float(V_YIELD),
    n_steps: int = 50,
    max_iter: int = 4,
    tol: float = 5e-2,
    energy_explosion_factor: float = 100.0,
    verbose: bool = True,
) -> CoupledEigenmodeResult:
    """Iterative self-consistency loop on the COUPLED K4+Cosserat engine.

    Each outer iter: seed both sectors at (R_k, r_k) → undamped evolve
    n_steps → time-RMS combined-magnitude envelope → extract (R_{k+1},
    r_{k+1}) → check convergence on geometry + topology + energy.

    Termination:
    - converged: |ΔR/R| < tol AND |Δr/r| < tol AND c=3 AND not diverged
    - diverged: E grew > energy_explosion_factor × E_seed during inner
    - topology_lost: geometry stable but c ≠ 3 at convergence
    - max_iter_no_converge: ran out of iterations
    """
    if r_seed is None:
        r_seed = R_seed / PHI_SQ
    R_k = R_seed
    r_k = r_seed
    trajectory: list = []

    for outer in range(1, max_iter + 1):
        engine = VacuumEngine3D.from_args(N=N, pml=pml, temperature=0.0)
        _seed_both_sectors(engine, R_k, r_k, cos_amp_scale, k4_amplitude)
        E_seed = float(engine.cos.total_energy())

        if verbose:
            print(f"\n=== Outer iter {outer} ===")
            print(f"  seed (R, r) = ({R_k:.3f}, {r_k:.3f})  E_seed = {E_seed:.3e}")

        diag, diverged = _run_inner(
            engine, n_steps, E_seed, energy_explosion_factor,
            rms_avg_last_n=min(30, n_steps),
        )

        trajectory.append((R_k, r_k, diag["c"], diag["E_final"], diag["peak_omega"]))

        if verbose:
            print(f"  after {diag['n_steps_run']} steps: "
                  f"R_rms={diag['R_rms']:.3f}  r_rms={diag['r_rms']:.3f}  "
                  f"c={diag['c']}  E_max/E_seed={diag['E_max']/max(abs(E_seed),1e-30):.2e}  "
                  f"peak|ω|={diag['peak_omega']:.3f}")

        if diverged:
            if verbose:
                print(f"  → DIVERGED (energy > {energy_explosion_factor}×seed) at step {diag['n_steps_run']}")
            return CoupledEigenmodeResult(
                converged=False, status="diverged", iterations=outer,
                trajectory=trajectory,
                final_R=R_k, final_r=r_k, final_c=diag["c"],
                final_E=diag["E_final"], final_peak_omega=diag["peak_omega"],
            )

        # Convergence check
        if R_k > 0 and r_k > 0:
            dR_rel = abs(diag["R_rms"] - R_k) / R_k
            dr_rel = abs(diag["r_rms"] - r_k) / r_k
        else:
            dR_rel = dr_rel = float("inf")

        if verbose:
            print(f"  ΔR/R = {dR_rel:.3e}  Δr/r = {dr_rel:.3e}  (tol={tol:.0e})")

        if dR_rel < tol and dr_rel < tol:
            if diag["c"] == 3:
                return CoupledEigenmodeResult(
                    converged=True, status="converged", iterations=outer,
                    trajectory=trajectory,
                    final_R=diag["R_rms"], final_r=diag["r_rms"], final_c=diag["c"],
                    final_E=diag["E_final"], final_peak_omega=diag["peak_omega"],
                )
            else:
                return CoupledEigenmodeResult(
                    converged=False, status="topology_lost", iterations=outer,
                    trajectory=trajectory,
                    final_R=diag["R_rms"], final_r=diag["r_rms"], final_c=diag["c"],
                    final_E=diag["E_final"], final_peak_omega=diag["peak_omega"],
                )

        # Feedback
        R_k = diag["R_rms"]
        r_k = diag["r_rms"]
        # Guard against pathological (R, r) → 0
        if R_k < 1.0 or r_k < 0.5:
            if verbose:
                print(f"  → Geometry collapsed (R={R_k:.2f}, r={r_k:.2f}), aborting")
            return CoupledEigenmodeResult(
                converged=False, status="geometry_collapsed", iterations=outer,
                trajectory=trajectory,
                final_R=R_k, final_r=r_k, final_c=diag["c"],
                final_E=diag["E_final"], final_peak_omega=diag["peak_omega"],
            )

    return CoupledEigenmodeResult(
        converged=False, status="max_iter_no_converge", iterations=max_iter,
        trajectory=trajectory,
        final_R=R_k, final_r=r_k, final_c=trajectory[-1][2] if trajectory else 0,
        final_E=trajectory[-1][3] if trajectory else 0.0,
        final_peak_omega=trajectory[-1][4] if trajectory else 0.0,
    )


if __name__ == "__main__":
    print("=" * 78)
    print("  F17-G: Coupled K4+Cosserat eigenmode finder")
    print("  Per doc 66_ §17 — Round 6 followup")
    print("=" * 78)

    print("\n--- Run 1: Golden Torus seed, default amps, N=48 ---")
    result = solve_eigenmode_coupled_engine(
        N=48, R_seed=12.0,
        n_steps=50, max_iter=4, tol=5e-2,
        verbose=True,
    )

    print(f"\n=== Result ===")
    print(f"  status:       {result.status}")
    print(f"  converged:    {result.converged}")
    print(f"  iterations:   {result.iterations}")
    print(f"  final (R, r): ({result.final_R:.3f}, {result.final_r:.3f})  "
          f"R/r = {result.final_R / max(result.final_r, 1e-9):.3f}  "
          f"(target φ² = {PHI_SQ:.3f})")
    print(f"  final c:      {result.final_c}  (target 3)")
    print(f"  final E:      {result.final_E:.3e}")
    print(f"  final |ω|:    {result.final_peak_omega:.3f}")
    print(f"  trajectory:")
    for i, (R, r, c, E, w) in enumerate(result.trajectory):
        ratio = R / max(r, 1e-9)
        print(f"    iter {i}: R={R:.2f} r={r:.2f} R/r={ratio:.3f} c={c} E={E:.2e} |ω|={w:.2f}")
