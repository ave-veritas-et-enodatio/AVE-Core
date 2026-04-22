"""
Phase 3b amplitude sweep — test the predicted photon→electron transition
as drive amplitude crosses Axiom-4 saturation threshold.

Pre-registered predictions (from 30_photon_identification.md §6.2):

  - strain A ≪ √(2α) ≈ 0.121 (Regime I):
      Bound state is photonic. α⁻¹ → 184.7 (extrapolated classical
      Hopfion Q), energy decays monotonically, A₁ mode zero, T₂ survives.
  - strain A ≈ √(2α) (Regime I/II boundary):
      Transition regime. Local saturation engages intermittently.
      α⁻¹ intermediate.
  - strain A > √3/2 ≈ 0.866 (Regime III):
      Full saturation confinement. α⁻¹ → 137. Energy bounded (standing
      wave). TIR boundary engaged.

Measurements per amplitude:
  - α⁻¹ from extract_alpha_inverse(R_rms, r_rms, c=3)
  - T₂ eigenvalues (port correlation across shell)
  - Achieved strain max(v_total)/V_SNAP
  - Energy decay fraction
  - Shell geometry (R_rms, r_rms)

Outputs:
  - /tmp/phase3b_sweep.npz (raw data)
  - /tmp/phase3b_sweep.png (multi-panel visualization)
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")   # headless
import matplotlib.pyplot as plt

from ave.core.k4_tlm import K4Lattice3D
from ave.core.constants import V_SNAP, V_YIELD, ALPHA
from tlm_electron_soliton_eigenmode import (
    initialize_2_3_voltage_ansatz, shell_envelope, extract_alpha_inverse,
)

PHI = (1.0 + np.sqrt(5.0)) / 2.0
ALPHA_INV_TARGET = 137.036
ALPHA_INV_PHOTON_EST = 184.7


def run_at_strain(strain_target: float, N: int = 64, n_steps: int = 300,
                  R: float = 16.0, r: float = 6.108,
                  pml_thickness: int = 6) -> dict:
    """Run TLM at an amplitude scaled to hit strain_target = v_max/V_SNAP.

    Returns per-run diagnostics including Q-factor, T2 eigenvalues,
    achieved strain, energy decay, and shell geometry.
    """
    # Amplitude scaled directly against V_SNAP. The envelope formula
    # multiplies amplitude by π/(1 + (rho_tube/r)²), so the peak envelope
    # equals amplitude · π. Setting the peak V_inc ≈ strain_target·V_SNAP.
    amplitude = strain_target * float(V_SNAP) / np.pi

    lattice = K4Lattice3D(
        N, N, N, dx=1.0,
        pml_thickness=pml_thickness,
        nonlinear=False,
        op3_bond_reflection=True,
    )
    initialize_2_3_voltage_ansatz(lattice, R=R, r=r, amplitude=amplitude)

    cx = (lattice.nx - 1) / 2.0
    cy = (lattice.ny - 1) / 2.0
    cz = (lattice.nz - 1) / 2.0

    V_mag_init = np.sqrt(np.sum(lattice.V_inc ** 2, axis=-1))
    energy_init = float(np.sum(V_mag_init ** 2))
    energy_trace = [energy_init]

    # RMS accumulator over final 100 steps for shell-geometry extraction
    rms_accumulator = np.zeros(lattice.V_inc.shape[:3], dtype=np.float64)
    rms_count = 0
    rms_start = max(1, n_steps - 100 + 1)

    max_strain_seen = 0.0

    for step in range(1, n_steps + 1):
        lattice.step()
        if step >= rms_start:
            V_phys_sq = np.sum((lattice.V_inc + lattice.V_ref) ** 2, axis=-1)
            rms_accumulator += V_phys_sq
            rms_count += 1
        # Track peak strain across the run
        v_total = np.sqrt(np.sum(lattice.V_inc ** 2, axis=-1))
        max_strain_seen = max(max_strain_seen, float(v_total.max() / V_SNAP))
        if step % 50 == 0:
            V_mag = np.sqrt(np.sum(lattice.V_inc ** 2, axis=-1))
            energy_trace.append(float(np.sum(V_mag ** 2)))

    energy_final = energy_trace[-1]

    # Shell geometry from V_phys² RMS
    V_rms = np.sqrt(rms_accumulator / rms_count)
    R_rms, r_rms = shell_envelope(V_rms, cx, cy, cz)

    # Q-factor from the three-mode decomposition at measured (R_rms, r_rms)
    alpha = extract_alpha_inverse(R_rms, r_rms, c=3)
    alpha_inv = alpha["alpha_inv"] if alpha["valid"] else float("nan")

    # T₂ eigenvalues: port correlation across shell sites
    mask_active = lattice.mask_A | lattice.mask_B
    V_total_sq_final = np.sum(lattice.V_inc ** 2 + lattice.V_ref ** 2, axis=-1)
    V_total_sq_active = V_total_sq_final * mask_active
    peak = float(V_total_sq_active.max())
    shell_mask = (V_total_sq_active > 0.3 * peak) & mask_active
    n_shell = int(shell_mask.sum())
    if n_shell > 4:
        V_inc_shell = lattice.V_inc[shell_mask]
        # Guard against constant columns that break corrcoef
        col_var = np.var(V_inc_shell, axis=0)
        if np.all(col_var > 1e-30):
            corr = np.corrcoef(V_inc_shell.T)
            eigvals_corr = np.sort(np.linalg.eigvalsh(corr))[::-1]
        else:
            eigvals_corr = np.array([np.nan] * 4)
    else:
        eigvals_corr = np.array([np.nan] * 4)

    return {
        "strain_target": strain_target,
        "amplitude": amplitude,
        "max_strain": max_strain_seen,
        "energy_init": energy_init,
        "energy_final": energy_final,
        "energy_trace": np.array(energy_trace),
        "R_rms": R_rms,
        "r_rms": r_rms,
        "alpha_inv": alpha_inv,
        "eigvals_corr": eigvals_corr,
        "n_shell": n_shell,
    }


def main():
    print("=" * 72)
    print("PHASE 3b AMPLITUDE SWEEP — photon → electron transition")
    print("=" * 72)
    print(f"Pre-registered predictions:")
    print(f"  strain ≪ √(2α) ≈ 0.121: α⁻¹ → {ALPHA_INV_PHOTON_EST:.1f} (photon)")
    print(f"  strain > √3/2 ≈ 0.866: α⁻¹ → {ALPHA_INV_TARGET:.3f} (electron)")
    print()

    strain_targets = [
        1e-6,    # deep photon regime (previous run's scale)
        1e-3,    # still Regime I, well below threshold
        0.05,    # Regime I, approaching boundary
        0.121,   # √(2α) — Regime I/II boundary
        0.3,     # Regime II (yielding)
        0.5,     # Regime II mid
        0.866,   # √3/2 — Regime II/III boundary
        0.95,    # Regime III (near rupture)
    ]

    results = []
    for i, target in enumerate(strain_targets):
        print(f"[{i+1}/{len(strain_targets)}] strain_target = {target:.3e} ...",
              end=" ", flush=True)
        res = run_at_strain(target)
        results.append(res)
        decay_pct = (res["energy_init"] - res["energy_final"]) \
            / max(res["energy_init"], 1e-30) * 100
        print(f"α⁻¹ = {res['alpha_inv']:7.2f}  "
              f"strain_max = {res['max_strain']:.3e}  "
              f"R/r = {res['R_rms']/max(res['r_rms'],1e-9):.3f}  "
              f"decay = {decay_pct:5.1f}%")

    print()
    print("=" * 72)
    print(f"{'target':>10s} {'strain':>10s} {'α⁻¹':>9s} {'R_rms':>7s} "
          f"{'r_rms':>7s} {'R/r':>7s} {'decay %':>8s} {'λ_min':>9s}")
    for r in results:
        decay = (r["energy_init"] - r["energy_final"]) \
            / max(r["energy_init"], 1e-30) * 100
        lam_min = r["eigvals_corr"][-1] if not np.isnan(r["eigvals_corr"][0]) \
            else float("nan")
        rr = r["R_rms"] / max(r["r_rms"], 1e-9)
        print(f"{r['strain_target']:10.3e} {r['max_strain']:10.3e} "
              f"{r['alpha_inv']:9.3f} {r['R_rms']:7.2f} {r['r_rms']:7.2f} "
              f"{rr:7.3f} {decay:8.2f} {lam_min:9.4f}")

    # ------------------------------------------------------------------
    # Save raw data
    # ------------------------------------------------------------------
    np.savez(
        "/tmp/phase3b_sweep.npz",
        strain_targets=np.array([r["strain_target"] for r in results]),
        strain_actual=np.array([r["max_strain"] for r in results]),
        alpha_inv=np.array([r["alpha_inv"] for r in results]),
        R_rms=np.array([r["R_rms"] for r in results]),
        r_rms=np.array([r["r_rms"] for r in results]),
        energy_init=np.array([r["energy_init"] for r in results]),
        energy_final=np.array([r["energy_final"] for r in results]),
        eigvals_corr=np.array([r["eigvals_corr"] for r in results]),
    )

    # ------------------------------------------------------------------
    # Visualization: 6-panel figure
    # ------------------------------------------------------------------
    fig, axes = plt.subplots(2, 3, figsize=(15, 9))

    strain_x = np.array([max(r["max_strain"], 1e-10) for r in results])
    alpha_y = np.array([r["alpha_inv"] for r in results])

    # Panel 1: α⁻¹ vs strain (THE main result)
    ax = axes[0, 0]
    ax.semilogx(strain_x, alpha_y, "ko-", markersize=8, linewidth=1.5)
    ax.axhline(ALPHA_INV_TARGET, color="red", linestyle="--",
               label=f"electron (α⁻¹ = {ALPHA_INV_TARGET})")
    ax.axhline(ALPHA_INV_PHOTON_EST, color="blue", linestyle="--",
               label=f"classical Hopfion (≈ {ALPHA_INV_PHOTON_EST})")
    ax.axvline(np.sqrt(2 * ALPHA), color="gray", alpha=0.4, linestyle=":")
    ax.axvline(np.sqrt(3) / 2, color="gray", alpha=0.4, linestyle=":")
    ax.set_xlabel("max strain A = max|V_inc|/V_SNAP")
    ax.set_ylabel("α⁻¹ (extracted)")
    ax.set_title("Panel 1: Q-factor vs drive strain\n"
                 "(THE test — does Q shift toward 137 under saturation?)")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", fontsize=8)

    # Panel 2: T₂ eigenvalues vs strain
    ax = axes[0, 1]
    eigs = np.array([r["eigvals_corr"] for r in results])
    for i in range(4):
        ax.semilogx(strain_x, eigs[:, i], "o-",
                    label=f"λ_{i+1}", markersize=6)
    ax.axvline(np.sqrt(2 * ALPHA), color="gray", alpha=0.4, linestyle=":")
    ax.axvline(np.sqrt(3) / 2, color="gray", alpha=0.4, linestyle=":")
    ax.set_xlabel("max strain A")
    ax.set_ylabel("port-correlation eigenvalue")
    ax.set_title("Panel 2: Port-correlation spectrum\n"
                 "(λ_4 → 0 = A₁ dissipated; three T₂ modes survive)")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", fontsize=8)

    # Panel 3: Shell R/r vs strain
    ax = axes[0, 2]
    R_y = np.array([r["R_rms"] for r in results])
    r_y = np.array([r["r_rms"] for r in results])
    R_over_r = R_y / np.maximum(r_y, 1e-9)
    ax.semilogx(strain_x, R_over_r, "go-", markersize=8)
    ax.axhline(PHI ** 2, color="red", linestyle="--",
               label=f"φ² = {PHI**2:.3f} (Golden Torus)")
    ax.axhline(2.27, color="blue", linestyle="--",
               label="TLM photon ≈ 2.27")
    ax.axhline(2.0, color="orange", linestyle="--",
               label="full Clifford ≈ 2.0")
    ax.axvline(np.sqrt(2 * ALPHA), color="gray", alpha=0.4, linestyle=":")
    ax.axvline(np.sqrt(3) / 2, color="gray", alpha=0.4, linestyle=":")
    ax.set_xlabel("max strain A")
    ax.set_ylabel("R/r (shell aspect)")
    ax.set_title("Panel 3: Shell geometry vs strain")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", fontsize=8)

    # Panel 4: energy decay %
    ax = axes[1, 0]
    decay_y = np.array([
        (r["energy_init"] - r["energy_final"])
        / max(r["energy_init"], 1e-30) * 100
        for r in results
    ])
    ax.semilogx(strain_x, decay_y, "mo-", markersize=8)
    ax.axvline(np.sqrt(2 * ALPHA), color="gray", alpha=0.4, linestyle=":",
               label="√(2α) = Regime II onset")
    ax.axvline(np.sqrt(3) / 2, color="gray", alpha=0.4, linestyle=":",
               label="√3/2 = Regime III")
    ax.set_xlabel("max strain A")
    ax.set_ylabel("energy decay (%)")
    ax.set_title("Panel 4: Energy decay\n"
                 "(decreases → confined standing wave)")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", fontsize=8)

    # Panel 5: energy traces (time evolution per amplitude)
    ax = axes[1, 1]
    n_traces = len(results)
    cmap = plt.cm.viridis
    for i, r in enumerate(results):
        norm_trace = r["energy_trace"] / max(r["energy_trace"][0], 1e-30)
        t = np.arange(len(norm_trace)) * 50   # 50-step sample interval
        ax.plot(t, norm_trace, color=cmap(i / max(n_traces - 1, 1)),
                label=f"A = {r['max_strain']:.2e}", alpha=0.8)
    ax.set_xlabel("simulation step")
    ax.set_ylabel("energy / energy(0)")
    ax.set_title("Panel 5: Energy traces by drive level")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", fontsize=6)

    # Panel 6: regime diagram as a text/summary
    ax = axes[1, 2]
    ax.axis("off")
    summary_lines = [
        "PHASE 3b PRE-REGISTERED PREDICTIONS",
        "",
        f"Photon (A ≪ √2α):       α⁻¹ → {ALPHA_INV_PHOTON_EST}",
        f"Electron (A > √3/2):     α⁻¹ → {ALPHA_INV_TARGET}",
        "",
        "MEASURED:",
    ]
    for r in results:
        summary_lines.append(
            f"  A={r['max_strain']:7.2e}  α⁻¹={r['alpha_inv']:6.2f}  "
            f"R/r={r['R_rms']/max(r['r_rms'], 1e-9):5.2f}"
        )
    summary_lines.append("")
    # Verdict
    alpha_low = alpha_y[0]   # smallest strain
    alpha_high = alpha_y[-1]  # largest strain
    delta_alpha = alpha_high - alpha_low
    if abs(alpha_high - ALPHA_INV_TARGET) < 10:
        summary_lines.append("VERDICT: Q → 137 at high strain ✓")
    elif delta_alpha < 0 and abs(alpha_high - alpha_low) > 20:
        summary_lines.append(f"VERDICT: Q shifts downward by "
                             f"{abs(delta_alpha):.1f} — partial mechanism")
    elif abs(delta_alpha) < 5:
        summary_lines.append(
            "VERDICT: Q stable across strain — mechanism not engaging")
    else:
        summary_lines.append(
            f"VERDICT: Q shifts by {delta_alpha:+.1f} — inspect further")
    ax.text(0.05, 0.95, "\n".join(summary_lines),
            transform=ax.transAxes, va="top", family="monospace", fontsize=8)

    plt.tight_layout()
    out_png = "/tmp/phase3b_sweep.png"
    plt.savefig(out_png, dpi=110)
    print()
    print(f"Raw data:   /tmp/phase3b_sweep.npz")
    print(f"Plot:       {out_png}")


if __name__ == "__main__":
    main()
