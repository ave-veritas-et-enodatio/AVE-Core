"""
Phase 3b axiom-compliant redesign — Op6 self-consistency + seed
independence + periodic BCs.

Pre-registration in
research/_archive/L3_electron_soliton/32_phase3b_axiom_compliant_redesign.md
recorded BEFORE this script is run (per flag-don't-fix discipline).

Grid (compute-constrained, smaller than plan's 5×3×6):
  - 3 envelopes {hedgehog, gaussian, exponential}
  - 3 amplitudes targeting strains {0.2, 0.3, 0.48}
  - 3 Op6 iterations maximum per (envelope, amplitude)
  - 150 TLM steps per inner iteration
  - N = 72 (compromise between plan's 96 and prior 64 for compute)
  - pml_thickness = 0 (periodic toroidal wrap)
  - op3_bond_reflection = True (Axiom 4 saturation at bonds)

Outputs
  /tmp/phase3b_axiom_compliant.npz       — raw convergence trajectories
  /tmp/phase3b_convergence_traces.png    — 3×3 grid of R_k, r_k per iter
  /tmp/phase3b_seed_independence.png     — cross-envelope at each amplitude
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.core.k4_tlm import K4Lattice3D
from ave.core.constants import V_SNAP, ALPHA
from tlm_electron_soliton_eigenmode import (
    initialize_2_3_voltage_ansatz,
    initialize_2_3_voltage_ansatz_gaussian,
    initialize_2_3_voltage_ansatz_exponential,
    shell_envelope, extract_alpha_inverse,
)

PHI = (1.0 + np.sqrt(5.0)) / 2.0
ALPHA_INV_TARGET = 1.0 / ALPHA

# Envelope registry (name -> initializer function)
ENVELOPES = {
    "hedgehog": initialize_2_3_voltage_ansatz,
    "gaussian": initialize_2_3_voltage_ansatz_gaussian,
    "exponential": initialize_2_3_voltage_ansatz_exponential,
}


def op6_iteration(
    envelope_name: str,
    strain_target: float,
    N: int = 72,
    n_steps: int = 150,
    max_iter: int = 3,
    pml_thickness: int = 0,
    tol: float = 0.01,
    seed_R: float = 18.0,
    seed_r: float = 6.87,   # seed R/r = φ²
    nonlinear: bool = False,   # node-level Axiom 4 saturation
) -> dict:
    """One Op6 self-consistency loop with a specified envelope.

    Per-iteration: build lattice, initialize ansatz at (R_k, r_k),
    evolve n_steps, extract new (R, r) from time-averaged V_phys² RMS
    over the last 80 steps, feed back. Converge when |ΔR/R| and
    |Δr/r| < tol.

    Q-extraction is done post-hoc (after this loop returns),
    NOT inside the loop — the loop targets (R, r), Q is derived
    from the converged geometry for tiered reporting.
    """
    init_fn = ENVELOPES[envelope_name]
    amplitude = strain_target * float(V_SNAP) / np.pi

    R_k = seed_R
    r_k = seed_r
    trajectory = [(0, R_k, r_k)]   # (iter, R, r)
    R_rms_history = []
    energy_history = []

    for it in range(1, max_iter + 1):
        lattice = K4Lattice3D(
            N, N, N, dx=1.0,
            pml_thickness=pml_thickness,
            nonlinear=nonlinear,
            op3_bond_reflection=True,
        )
        init_fn(lattice, R=R_k, r=r_k, amplitude=amplitude)

        cx = (lattice.nx - 1) / 2.0
        cy = (lattice.ny - 1) / 2.0
        cz = (lattice.nz - 1) / 2.0

        rms_accum = np.zeros(lattice.V_inc.shape[:3], dtype=np.float64)
        rms_count = 0
        rms_start = max(1, n_steps - 80 + 1)

        energy_init = float(np.sum(lattice.V_inc ** 2) +
                            np.sum(lattice.V_ref ** 2))

        for step in range(1, n_steps + 1):
            lattice.step()
            if step >= rms_start:
                V_phys = lattice.V_inc + lattice.V_ref
                rms_accum += np.sum(V_phys ** 2, axis=-1)
                rms_count += 1

        energy_final = float(np.sum(lattice.V_inc ** 2) +
                             np.sum(lattice.V_ref ** 2))
        V_rms = np.sqrt(rms_accum / max(rms_count, 1))
        R_new, r_new = shell_envelope(V_rms, cx, cy, cz)

        trajectory.append((it, R_new, r_new))
        R_rms_history.append((R_new, r_new))
        energy_history.append((energy_init, energy_final))

        dR_rel = abs(R_new - R_k) / max(R_k, 1e-9)
        dr_rel = abs(r_new - r_k) / max(r_k, 1e-9)
        print(
            f"    iter {it}: "
            f"seed({R_k:5.2f},{r_k:5.2f}) → ({R_new:5.2f},{r_new:5.2f})  "
            f"R/r={R_new/max(r_new,1e-9):5.3f}  "
            f"ΔR/R={dR_rel:.2%}  Δr/r={dr_rel:.2%}  "
            f"E_decay={(1 - energy_final/max(energy_init,1e-30))*100:.1f}%"
        )

        if dR_rel < tol and dr_rel < tol:
            print(f"    → converged at iteration {it}")
            return {
                "envelope": envelope_name,
                "strain_target": strain_target,
                "converged": True,
                "iterations": it,
                "trajectory": trajectory,
                "final_R": R_new,
                "final_r": r_new,
                "R_rms_history": R_rms_history,
                "energy_history": energy_history,
            }

        R_k, r_k = R_new, r_new

    return {
        "envelope": envelope_name,
        "strain_target": strain_target,
        "converged": False,
        "iterations": max_iter,
        "trajectory": trajectory,
        "final_R": R_k,
        "final_r": r_k,
        "R_rms_history": R_rms_history,
        "energy_history": energy_history,
    }


def plot_convergence_grid(results, out_path):
    """3×3 grid — envelope on rows, amplitude on columns.
    Each subplot: R/r vs Op6 iteration."""
    envs = list(ENVELOPES.keys())
    amps = sorted({r["strain_target"] for r in results})

    fig, axes = plt.subplots(len(envs), len(amps),
                             figsize=(4.5 * len(amps), 3.5 * len(envs)),
                             sharey=True)
    if len(envs) == 1:
        axes = np.array([axes])
    if len(amps) == 1:
        axes = axes[:, np.newaxis]

    for i, env in enumerate(envs):
        for j, amp in enumerate(amps):
            ax = axes[i, j]
            hit = [r for r in results
                   if r["envelope"] == env and r["strain_target"] == amp]
            if hit:
                res = hit[0]
                iters = [t[0] for t in res["trajectory"]]
                R_vals = [t[1] for t in res["trajectory"]]
                r_vals = [t[2] for t in res["trajectory"]]
                ratio = [R / max(rr, 1e-9) for R, rr in zip(R_vals, r_vals)]
                ax.plot(iters, ratio, "o-", markersize=7, linewidth=1.5)
                ax.axhline(PHI ** 2, color="red", linestyle=":", alpha=0.6,
                           label=f"φ²={PHI**2:.3f}")
                status = "CONV" if res["converged"] else "no conv"
                ax.set_title(
                    f"{env}, A_target={amp}  [{status} at iter {res['iterations']}]",
                    fontsize=9,
                )
            ax.set_xlabel("Op6 iteration")
            if j == 0:
                ax.set_ylabel("R/r")
            ax.grid(alpha=0.3)
            ax.set_ylim(1.5, 5.5)
            if i == 0 and j == 0:
                ax.legend(fontsize=7, loc="best")

    plt.suptitle("Phase 3b axiom-compliant — Op6 convergence per (envelope, amplitude)",
                 y=1.00)
    plt.tight_layout()
    plt.savefig(out_path, dpi=110)
    plt.close(fig)


def plot_seed_independence(results, out_path):
    """One panel per amplitude; three envelope trajectories overlaid.
    If the three overlap and converge, seed-independence is met."""
    amps = sorted({r["strain_target"] for r in results})
    fig, axes = plt.subplots(1, len(amps),
                             figsize=(5 * len(amps), 4.5), sharey=True)
    if len(amps) == 1:
        axes = [axes]

    colors = {"hedgehog": "C0", "gaussian": "C1", "exponential": "C2"}
    for j, amp in enumerate(amps):
        ax = axes[j]
        for env in ENVELOPES.keys():
            hit = [r for r in results
                   if r["envelope"] == env and r["strain_target"] == amp]
            if hit:
                res = hit[0]
                iters = [t[0] for t in res["trajectory"]]
                R_vals = [t[1] for t in res["trajectory"]]
                r_vals = [t[2] for t in res["trajectory"]]
                ratio = [R / max(rr, 1e-9) for R, rr in zip(R_vals, r_vals)]
                ax.plot(iters, ratio, "o-", color=colors[env],
                        label=env, markersize=7, linewidth=1.5)
        ax.axhline(PHI ** 2, color="red", linestyle=":", alpha=0.6,
                   label=f"φ²={PHI**2:.3f}")
        ax.set_title(f"A_target = {amp}")
        ax.set_xlabel("Op6 iteration")
        if j == 0:
            ax.set_ylabel("R/r")
        ax.grid(alpha=0.3)
        ax.set_ylim(1.5, 5.5)
        ax.legend(fontsize=8)

    plt.suptitle("Seed-independence test — three envelopes at each amplitude",
                 y=1.02)
    plt.tight_layout()
    plt.savefig(out_path, dpi=110)
    plt.close(fig)


def main():
    print("=" * 72)
    print("PHASE 3b AXIOM-COMPLIANT REDESIGN")
    print("Pre-registered in research/_archive/L3_electron_soliton/"
          "32_phase3b_axiom_compliant_redesign.md")
    print("=" * 72)

    envelopes = list(ENVELOPES.keys())
    amplitudes = [0.2, 0.3, 0.48]
    N = 72
    n_steps = 150
    max_iter = 3

    print(f"\nGrid: {len(envelopes)} envelopes × {len(amplitudes)} amplitudes"
          f" × up to {max_iter} Op6 iterations")
    print(f"Lattice: N={N}, pml=0 (periodic), op3_bond_reflection=True")
    print(f"Inner: {n_steps} TLM steps per iteration")
    print(f"Seed: Golden Torus (R=18, r=6.87, R/r=φ²)")

    results = []
    for env in envelopes:
        for amp in amplitudes:
            print(f"\n--- envelope={env}, strain_target={amp} ---")
            res = op6_iteration(
                envelope_name=env,
                strain_target=amp,
                N=N,
                n_steps=n_steps,
                max_iter=max_iter,
            )
            results.append(res)

    # ------------------------------------------------------------------
    # Report: Q tiers at converged (R, r) per run
    # ------------------------------------------------------------------
    print()
    print("=" * 72)
    print("RESULTS per (envelope, amplitude)")
    print("=" * 72)
    print(
        f"{'env':>12} {'A_tgt':>6} {'conv':>5} {'iter':>5} "
        f"{'R_final':>8} {'r_final':>8} {'R/r':>7} "
        f"{'α⁻¹_geom':>10}"
    )
    for res in results:
        alpha = extract_alpha_inverse(res["final_R"], res["final_r"], c=3)
        alpha_inv = alpha["alpha_inv"] if alpha["valid"] else float("nan")
        print(
            f"{res['envelope']:>12} {res['strain_target']:>6} "
            f"{'Y' if res['converged'] else 'N':>5} "
            f"{res['iterations']:>5} "
            f"{res['final_R']:>8.3f} {res['final_r']:>8.3f} "
            f"{res['final_R']/max(res['final_r'],1e-9):>7.3f} "
            f"{alpha_inv:>10.2f}"
        )

    # Seed-independence check per amplitude
    print()
    print("Seed-independence (cross-envelope spread at same amplitude):")
    for amp in amplitudes:
        at_amp = [r for r in results if r["strain_target"] == amp]
        if not at_amp:
            continue
        R_final = [r["final_R"] for r in at_amp]
        r_final = [r["final_r"] for r in at_amp]
        ratio = [R / max(rr, 1e-9) for R, rr in zip(R_final, r_final)]
        R_spread = (max(R_final) - min(R_final)) / max(np.mean(R_final), 1e-9)
        ratio_spread = (max(ratio) - min(ratio)) / max(np.mean(ratio), 1e-9)
        seed_indep = R_spread < 0.05 and ratio_spread < 0.05
        print(
            f"  A_target={amp}:  "
            f"R_final range [{min(R_final):.3f}, {max(R_final):.3f}]  "
            f"R/r range [{min(ratio):.3f}, {max(ratio):.3f}]  "
            f"ΔR/mean={R_spread:.2%}  Δ(R/r)/mean={ratio_spread:.2%}  "
            f"{'✓ seed-indep' if seed_indep else '✗ NOT seed-indep'}"
        )

    # Verdict per pre-registered predictions
    print()
    print("Pre-registered prediction evaluation:")
    all_converged = all(r["converged"] for r in results)
    any_converged = any(r["converged"] for r in results)
    same_point_at_any_amp = False
    for amp in amplitudes:
        at_amp = [r for r in results if r["strain_target"] == amp
                  and r["converged"]]
        if len(at_amp) == 3:
            R_final = [r["final_R"] for r in at_amp]
            r_final = [r["final_r"] for r in at_amp]
            ratio = [R / max(rr, 1e-9) for R, rr in zip(R_final, r_final)]
            if (max(R_final) - min(R_final)) / max(np.mean(R_final), 1e-9) < 0.05:
                same_point_at_any_amp = True
                break
    golden_match = False
    for res in results:
        if res["converged"]:
            ratio_r = res["final_R"] / max(res["final_r"], 1e-9)
            if 2.5 < ratio_r < 2.7:
                golden_match = True
                break
    if same_point_at_any_amp and golden_match:
        verdict = "P1 confirmed: eigenmode + Golden Torus found"
    elif same_point_at_any_amp:
        verdict = "P3 confirmed: eigenmode found, R/r ≠ φ² (photonic Hopfion)"
    elif not any_converged:
        verdict = "P2 confirmed: no eigenmode in this config"
    else:
        verdict = "Ambiguous: partial convergence, no consistent seed-independence"
    print(f"  → {verdict}")

    # Save raw data
    save_dict = {}
    for res in results:
        tag = f"{res['envelope']}_{res['strain_target']}"
        traj = np.array(res["trajectory"])  # (n_iter+1, 3)
        save_dict[f"{tag}_trajectory"] = traj
        save_dict[f"{tag}_converged"] = np.array([res["converged"]])
        save_dict[f"{tag}_final_R"] = np.array([res["final_R"]])
        save_dict[f"{tag}_final_r"] = np.array([res["final_r"]])
    np.savez("/tmp/phase3b_axiom_compliant.npz", **save_dict)

    plot_convergence_grid(results, "/tmp/phase3b_convergence_traces.png")
    plot_seed_independence(results, "/tmp/phase3b_seed_independence.png")

    print()
    print("Raw data: /tmp/phase3b_axiom_compliant.npz")
    print("Figures:  /tmp/phase3b_convergence_traces.png")
    print("          /tmp/phase3b_seed_independence.png")


if __name__ == "__main__":
    main()