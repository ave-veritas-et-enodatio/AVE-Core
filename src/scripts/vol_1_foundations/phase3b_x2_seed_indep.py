"""
Phase 3b X2-prime — Cosserat S11 seed-independence test.

X2 (`phase3b_x2_cosserat.py`) seeded at canonical Golden Torus
(R/r = φ²) and found R/r ≈ 2.69-2.77 preserved under S11 relaxation.
The question: is this a genuine basin of attraction (minimum) or a
flat shoulder (the optimizer just stalls wherever we put it)?

Discriminating test: seed at several R/r values AWAY from φ² and check
whether S11 relaxation pulls them BACK to φ² (→ basin) or each stays
near its seed (→ flat landscape).

Seeds (all N=72, canonical hedgehog envelope):
  - R/r = 2.0   (classical full-Clifford: R·r=1/2 instead of 1/4)
  - R/r = 2.618 (φ² — positive control, should stay)
  - R/r = 3.5   (K4-TLM Gaussian-attractor value from §8)
  - R/r = 4.0   (intentionally far from φ²)

Pre-registered outcomes:
  - All relax to R/r ≈ φ² (within 5%)        → BASIN. Phase 3b closes.
  - Each stays near its seed (within 5%)      → FLAT. Ambiguous; need
                                                 energy-relaxation cross-check.
  - Mixed (some converge, some don't)         → inspect trajectories.
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.topological.cosserat_field_3d import CosseratField3D

PHI = (1.0 + np.sqrt(5.0)) / 2.0


def run_seed(R_target: float, r_target: float, label: str,
             N: int = 72, max_iter: int = 500) -> dict:
    """One Cosserat + S11 run from a specified (R, r) seed."""
    print(f"\n--- seed {label}: R={R_target}, r={r_target:.3f}, "
          f"R/r={R_target/r_target:.3f} ---")
    solver = CosseratField3D(N, N, N, dx=1.0, use_saturation=True)
    solver.initialize_electron_2_3_sector(
        R_target=R_target, r_target=r_target, use_hedgehog=True,
    )

    R0, r0 = solver.extract_shell_radii()
    c0 = solver.extract_crossing_count()
    S11_0 = solver.total_s11()
    print(f"  Initial: (R, r) = ({R0:.3f}, {r0:.3f}), R/r = "
          f"{R0/max(r0,1e-9):.3f}, c = {c0}, S11 = {S11_0:.4e}")

    result = solver.relax_s11(
        max_iter=max_iter, tol=1e-8, initial_lr=0.01,
        verbose=False, track_topology_every=50,
    )

    R_f, r_f = solver.extract_shell_radii()
    c_f = solver.extract_crossing_count()
    ratio_f = R_f / max(r_f, 1e-9)

    converged_text = "✓ converged" if result["converged"] else "✗ no conv"
    print(f"  Final:   (R, r) = ({R_f:.3f}, {r_f:.3f}), R/r = "
          f"{ratio_f:.3f}, c = {c_f}, S11 = {result['final_s11']:.4e}  "
          f"[{result['iterations']} iter, {converged_text}]")
    print(f"  Drift:   R/r {R0/max(r0,1e-9):.3f} → {ratio_f:.3f}  "
          f"Δ = {ratio_f - R0/max(r0,1e-9):+.3f}")

    result["label"] = label
    result["R_target"] = R_target
    result["r_target"] = r_target
    result["R_seed_extracted"] = float(R0)
    result["r_seed_extracted"] = float(r0)
    result["R_final"] = float(R_f)
    result["r_final"] = float(r_f)
    result["c_final"] = int(c_f)
    return result


def main():
    print("=" * 72)
    print("PHASE 3b X2-prime — Cosserat S11 seed-independence test")
    print("Question: is R/r ≈ φ² a basin of attraction, or a flat shoulder?")
    print("=" * 72)

    N = 72
    # R is constant (= N/4 = 18); r varies to set R/r
    R_target = 18.0
    seeds = [
        ("R/r=2.0 (classical)",   R_target, R_target / 2.0),
        ("R/r=2.618 (φ²)",        R_target, R_target / (PHI**2)),
        ("R/r=3.5 (K4 Gauss)",    R_target, R_target / 3.5),
        ("R/r=4.0 (far)",         R_target, R_target / 4.0),
    ]

    results = []
    for label, R_t, r_t in seeds:
        res = run_seed(R_t, r_t, label, N=N, max_iter=500)
        results.append(res)

    # Table
    print()
    print("=" * 72)
    print("X2-prime seed-independence summary")
    print("=" * 72)
    print(f"{'seed':>22} {'R/r_init':>9} {'R/r_final':>10} {'Δ R/r':>7} "
          f"{'c_f':>4} {'S11_final':>12} {'iter':>5}")
    for res in results:
        ratio_init = res["R_seed_extracted"] / max(res["r_seed_extracted"], 1e-9)
        ratio_final = res["R_final"] / max(res["r_final"], 1e-9)
        delta = ratio_final - ratio_init
        print(
            f"{res['label']:>22} "
            f"{ratio_init:>9.3f} {ratio_final:>10.3f} {delta:>+7.3f} "
            f"{res['c_final']:>4} {res['final_s11']:>12.4e} "
            f"{res['iterations']:>5}"
        )

    # Cluster check
    print()
    print("Pre-registered outcome evaluation:")
    final_ratios = [r["R_final"] / max(r["r_final"], 1e-9) for r in results]
    spread = (max(final_ratios) - min(final_ratios)) / max(np.mean(final_ratios), 1e-9)
    # How close to φ² did each end?
    dists = [abs(rr - PHI**2) / PHI**2 for rr in final_ratios]
    max_dist = max(dists)

    if max_dist < 0.05:
        verdict = ("P_BASIN: all seeds converged to R/r ≈ φ² within 5% — "
                   "Golden Torus is a genuine basin of attraction. Phase 3b closes.")
    elif spread < 0.05:
        verdict = ("MERGED (not at φ²): all seeds converged to the same "
                   f"R/r ≈ {np.mean(final_ratios):.3f}, which differs from φ² — "
                   "Cosserat has a single attractor that is NOT Ch 8's Golden Torus.")
    elif all(dist < 0.10 for dist in dists[:1]):  # check classical seed specifically
        verdict = ("Classical seed (2.0) close to φ² — partial basin toward φ² "
                   "but other seeds retained their values (flat landscape).")
    else:
        seeds_staying = sum(1 for res in results
                            if abs((res["R_final"]/max(res["r_final"],1e-9))
                                   - (res["R_seed_extracted"]/max(res["r_seed_extracted"],1e-9)))
                               / max(res["R_seed_extracted"]/max(res["r_seed_extracted"],1e-9), 1e-9)
                               < 0.05)
        if seeds_staying == len(results):
            verdict = ("P_FLAT: each seed stayed near its initial R/r — "
                       "S11 landscape is flat; every (2,3) hedgehog is a near-fixed-point. "
                       "Ambiguous; need energy-minimization cross-check.")
        else:
            verdict = "Mixed: inspect individual trajectories"
    print(f"  → {verdict}")

    # Save + plot
    save = {}
    for res in results:
        tag = res["label"].replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_").replace(".", "p").replace("=", "_")
        save[f"{tag}_s11_history"] = np.array(res["s11_history"])
        save[f"{tag}_R_final"] = np.array([res["R_final"]])
        save[f"{tag}_r_final"] = np.array([res["r_final"]])
        save[f"{tag}_c_final"] = np.array([res["c_final"]])
        if res["trajectory"]:
            save[f"{tag}_steps"] = np.array([t["step"] for t in res["trajectory"]])
            save[f"{tag}_R_traj"] = np.array([t["R"] for t in res["trajectory"]])
            save[f"{tag}_r_traj"] = np.array([t["r"] for t in res["trajectory"]])
    np.savez("/tmp/phase3b_x2_seed_indep.npz", **save)

    # Plot: R/r trajectory per seed
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    ax = axes[0]
    colors = plt.cm.viridis(np.linspace(0, 0.9, len(results)))
    for res, color in zip(results, colors):
        traj = res["trajectory"]
        if traj:
            steps = [0] + [t["step"] for t in traj]
            # First point is initial; recompute from stored initial
            ratios = [res["R_seed_extracted"] / max(res["r_seed_extracted"], 1e-9)]
            ratios += [t["R"] / max(t["r"], 1e-9) for t in traj]
            ax.plot(steps, ratios, "o-", color=color,
                    label=res["label"], markersize=5)
    ax.axhline(PHI**2, color="red", linestyle="--", linewidth=2,
               label=f"φ² = {PHI**2:.3f}")
    ax.axhline(2.0, color="gray", linestyle=":", label="classical 2.0")
    ax.set_xlabel("S11 gradient step")
    ax.set_ylabel("R/r")
    ax.set_title("R/r trajectory per seed — do they converge to φ² or stay?")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc="best")

    ax = axes[1]
    for res, color in zip(results, colors):
        hist = np.array(res["s11_history"])
        ax.semilogy(hist, color=color, label=res["label"], linewidth=1)
    ax.set_xlabel("gradient step")
    ax.set_ylabel("S11 (log)")
    ax.set_title("S11 minimization per seed")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    plt.suptitle("X2-prime — Cosserat S11 seed-independence test", y=1.02)
    plt.tight_layout()
    plt.savefig("/tmp/phase3b_x2_seed_indep.png", dpi=110)
    plt.close(fig)

    print()
    print("Raw data: /tmp/phase3b_x2_seed_indep.npz")
    print("Figure:   /tmp/phase3b_x2_seed_indep.png")


if __name__ == "__main__":
    main()
