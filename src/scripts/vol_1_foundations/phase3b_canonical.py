"""
Phase 3b X1-prime — canonical hedgehog at Regime II/III boundary.

Per §9 deep research findings in
research/_archive/L3_electron_soliton/32_phase3b_axiom_compliant_redesign.md:

  - Hedgehog (power-law) is the AVE-canonical envelope (Faddeev-Skyrme
    derived, cited by cosserat_field_3d.initialize_electron_2_3_sector).
    Gaussian + exponential are explicitly NON-topological per
    cosserat_field_3d.py:520.
  - The electron's amplitude is NOT a free parameter. Peak amplitude
    equals √3/2·π — the Regime II/III boundary per Axiom 4
    (cosserat_field_3d.py:514-518).
  - Node-level saturation (nonlinear=True) engages Axiom 4 at the
    scattering matrix, completing the corpus Axiom 4 implementation.

This run combines all three into the single canonical test:
  - Hedgehog envelope only (no non-topological alternatives)
  - strain_target = √3/2 ≈ 0.866 (Regime II/III canonical boundary)
  - nonlinear=True (full Axiom 4)
  - periodic BCs (pml=0)
  - op3_bond_reflection=True

Tests at N=72 (comparable to §8) and N=96 (plan-scoped) to check
N-scaling at the canonical condition.

Pre-registered expectation: Phase 3b closes if R/r converges to
φ² = 2.618 (Golden Torus, Ch 8 prediction) at canonical amplitude.
Other outcomes: R/r = 2.27-2.30 (classical K4 attractor from
convergence study — suggests spin-½ projection still needed);
R/r = 2.0 (classical full-Clifford); still R/r ~3.5 (mechanism
fundamentally incomplete).
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.core.constants import V_SNAP, ALPHA
from phase3b_axiom_compliant import op6_iteration
from tlm_electron_soliton_eigenmode import extract_alpha_inverse

PHI = (1.0 + np.sqrt(5.0)) / 2.0
SQRT3_OVER_2 = np.sqrt(3.0) / 2.0    # Regime II/III boundary per Axiom 4
ALPHA_INV_TARGET = 1.0 / ALPHA


def main():
    print("=" * 72)
    print("PHASE 3b X1-prime — canonical hedgehog + nonlinear=True")
    print("Amplitude: peak strain = √3/2 ≈ {:.4f} (Axiom 4 II/III boundary)"
          .format(SQRT3_OVER_2))
    print("Envelope: power-law hedgehog (AVE-canonical per "
          "cosserat_field_3d:486-519)")
    print("=" * 72)

    configs = [
        ("N=72 canonical", 72, 5),
        ("N=96 canonical", 96, 5),
    ]

    results = []
    for label, N, max_iter in configs:
        print(f"\n--- {label} ---")
        res = op6_iteration(
            envelope_name="hedgehog",
            strain_target=SQRT3_OVER_2,     # Regime II/III boundary
            N=N,
            n_steps=200,                      # more steps at canonical A
            max_iter=max_iter,
            pml_thickness=0,
            tol=0.01,
            nonlinear=True,                   # node-level Axiom 4
            seed_R=N / 4.0,                   # scale seed to N
            seed_r=(N / 4.0) / (PHI ** 2),    # seed at Golden Torus ratio
        )
        res["label"] = label
        res["N"] = N
        results.append(res)

    # --- Results ---
    print()
    print("=" * 72)
    print("X1-prime canonical results:")
    print("=" * 72)
    print(
        f"{'label':>20} {'N':>4} {'conv':>5} {'iter':>5} "
        f"{'R_final':>8} {'r_final':>8} {'R/r':>7} {'α⁻¹_geom':>10}"
    )
    for res in results:
        alpha = extract_alpha_inverse(res["final_R"], res["final_r"], c=3)
        alpha_inv = alpha["alpha_inv"] if alpha["valid"] else float("nan")
        print(
            f"{res['label']:>20} {res['N']:>4} "
            f"{'Y' if res['converged'] else 'N':>5} "
            f"{res['iterations']:>5} "
            f"{res['final_R']:>8.3f} {res['final_r']:>8.3f} "
            f"{res['final_R']/max(res['final_r'],1e-9):>7.3f} "
            f"{alpha_inv:>10.2f}"
        )

    # Pre-registered outcome evaluation
    print()
    print("Pre-registered outcome evaluation:")
    for res in results:
        rr = res["final_R"] / max(res["final_r"], 1e-9)
        if 2.5 < rr < 2.7:
            outcome = "✓ Golden Torus (R/r ≈ φ²) — Phase 3b closes"
        elif 2.2 < rr < 2.35:
            outcome = "≈ Classical K4 attractor (convergence study value) — spin-½ still needed"
        elif 1.85 < rr < 2.15:
            outcome = "≈ Classical full-Clifford (R/r = 2.0) — half-cover missing"
        elif 3.0 < rr < 4.0:
            outcome = "✗ Same regime as §8 — mechanism fundamentally incomplete"
        else:
            outcome = f"Unexpected R/r = {rr:.3f}"
        print(f"  {res['label']}  R/r = {rr:.3f}  →  {outcome}")

    # N-scaling between 72 and 96
    if len(results) >= 2:
        r_72 = results[0]["final_R"] / max(results[0]["final_r"], 1e-9)
        r_96 = results[1]["final_R"] / max(results[1]["final_r"], 1e-9)
        delta = r_96 - r_72
        print()
        print(f"N-scaling: R/r(N=72)={r_72:.3f}, R/r(N=96)={r_96:.3f}, "
              f"Δ={delta:+.3f}")
        if abs(delta) < 0.05:
            print("  → N-invariant within 2% — robust attractor")
        else:
            print(f"  → Changes by {abs(delta)/r_72*100:.1f}% — N-sensitive")

    # Save + plot
    save_dict = {}
    for res in results:
        tag = res["label"].replace(" ", "_").replace("=", "")
        traj = np.array(res["trajectory"])
        save_dict[f"{tag}_trajectory"] = traj
        save_dict[f"{tag}_converged"] = np.array([res["converged"]])
        save_dict[f"{tag}_final_R"] = np.array([res["final_R"]])
        save_dict[f"{tag}_final_r"] = np.array([res["final_r"]])
    np.savez("/tmp/phase3b_canonical.npz", **save_dict)

    # Simple 2-panel convergence plot
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), sharey=True)
    for ax, res in zip(axes, results):
        iters = [t[0] for t in res["trajectory"]]
        Rs = [t[1] for t in res["trajectory"]]
        rs = [t[2] for t in res["trajectory"]]
        ratio = [R / max(rr, 1e-9) for R, rr in zip(Rs, rs)]
        ax.plot(iters, ratio, "ko-", markersize=8, linewidth=2)
        ax.axhline(PHI ** 2, color="red", linestyle=":",
                   label=f"φ² = {PHI**2:.3f} (Ch 8 target)")
        ax.axhline(2.27, color="blue", linestyle=":",
                   label="2.27 (convergence study)")
        ax.axhline(2.0, color="green", linestyle=":",
                   label="2.0 (classical Clifford)")
        ax.set_xlabel("Op6 iteration")
        ax.set_ylabel("R/r")
        ax.set_title(
            f"{res['label']}  "
            f"[{'CONV' if res['converged'] else 'no conv'} at iter "
            f"{res['iterations']}]"
        )
        ax.grid(alpha=0.3)
        ax.set_ylim(1.5, 4.5)
        ax.legend(fontsize=8)

    plt.suptitle(
        "Phase 3b X1-prime — canonical hedgehog, nonlinear=True, "
        f"A = √3/2 ≈ {SQRT3_OVER_2:.3f}",
        y=1.02,
    )
    plt.tight_layout()
    plt.savefig("/tmp/phase3b_canonical.png", dpi=110)
    plt.close(fig)

    print()
    print("Raw data: /tmp/phase3b_canonical.npz")
    print("Figure:   /tmp/phase3b_canonical.png")


if __name__ == "__main__":
    main()
