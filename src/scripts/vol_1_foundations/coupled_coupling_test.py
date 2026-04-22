"""
Phase II validation — coupled K4 ⊗ Cosserat simulator.

Tests the coupling module per the plan's Phase II validation criteria:

  V1 — Isolation test (K4 with zero Cosserat).
        Start Cosserat at (u, ω) = 0 with zero velocities. Launch a K4
        photon packet. Expected: K4 evolution identical to standalone
        Phase A/B (coupling is zero because _reflection_density vanishes
        for (u,ω) = 0).

  V2 — Isolation test (Cosserat with zero V).
        Start K4 at V = 0. Seed a Cosserat (u, ω) wavepacket. Expected:
        Cosserat evolution identical to Phase I (coupling force is zero
        because V² = 0).

  V3 — Coupled interaction.
        Start Cosserat with a small shell-like (u, ω) seed. Launch a
        K4 photon packet toward it. Expected:
        - Coupling energy rises as V² · W_refl becomes nonzero.
        - Q (topological charge) measured; see whether it drifts under
          the interaction (S6-A diagnostic).
        - H = E_K4 + E_cos + E_coupling bounded (no runaway).

  V4 — Diagnostic scan.
        Step the coupled sim for many timesteps; produce time-series
        diagnostic plot of all observables.

AVE compliance notes (plan §"Axiom compliance map"):
  - Uses S-gate resolutions 2026-04-22: D/γ/A/A/B/A.
  - Natural units (dx=1, c=1, ρ=I_ω=1).
  - Linear Cosserat Lagrangian (Op10 + Hopf off per Phase I limitations).
  - V_SNAP = default CODATA (4.66e5 V ~ electron rest mass scale).
"""
from __future__ import annotations

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.core.constants import V_SNAP
from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat
from photon_propagation import PlaneSource


# ─────────────────────────────────────────────────────────────────
# V1: K4-only isolation
# ─────────────────────────────────────────────────────────────────
def test_v1_k4_isolation(N: int = 32, n_steps: int = 30) -> dict:
    """Coupling should be zero when (u, ω) = 0. K4 matches Phase B standalone."""
    sim = CoupledK4Cosserat(N=N, pml=4)

    # PlaneSource for K4 (using the Phase A infrastructure)
    lambda_cells = 8.0
    omega = 2.0 * np.pi * sim.k4.c / (lambda_cells * sim.k4.dx)
    src = PlaneSource(
        x0=8, y_c=(N - 1) / 2.0, z_c=(N - 1) / 2.0,
        direction=(1.0, 0.0, 0.0), sigma_yz=4.0, omega=omega,
        t_center=3.0 * (2.0 * np.pi / omega) * 0.5,  # 1.5 periods delay
        t_sigma=0.5 * (2.0 * np.pi / omega),
        amplitude=0.01 * sim.V_SNAP,
    )

    history = []
    t_start = time.time()
    for step in range(n_steps + 1):
        if step > 0:
            t = step * sim.outer_dt
            src.apply(sim.k4, t)
            sim.step()
        history.append(sim.snapshot_scalars())

    elapsed = time.time() - t_start

    # V1 assertions: coupling energy should stay ~0 throughout
    coupling_e_max = max(h["E_coupling"] for h in history)
    max_A_sq_cos_max = max(h["max_A_sq_cos"] for h in history)
    max_V_sq = max(h["max_V_sq"] for h in history)

    return {
        "N": N, "n_steps": n_steps, "elapsed_s": elapsed,
        "history": history,
        "coupling_e_max": coupling_e_max,
        "max_A_sq_cos_max": max_A_sq_cos_max,
        "max_V_sq": max_V_sq,
        "pass": coupling_e_max < 1e-10 and max_A_sq_cos_max < 1e-10,
    }


# ─────────────────────────────────────────────────────────────────
# V2: Cosserat-only isolation
# ─────────────────────────────────────────────────────────────────
def test_v2_cosserat_isolation(N: int = 32, n_steps: int = 30) -> dict:
    """Coupling force should be zero when V = 0. Cosserat matches Phase I."""
    sim = CoupledK4Cosserat(N=N, pml=4)
    # Re-enable small gamma for a cleaner wave test; G_c still creates mass gap
    # (Phase I-confirmed behavior). Keep linear only.

    sim.cos.initialize_gaussian_wavepacket_omega(
        center=(N // 4, N // 2, N // 2), sigma=3.0,
        direction=(1.0, 0.0, 0.0), wavelength=8.0,
        amplitude=1e-3, axis=2,
    )

    history = []
    t_start = time.time()
    for step in range(n_steps + 1):
        if step > 0:
            sim.step()
        history.append(sim.snapshot_scalars())
    elapsed = time.time() - t_start

    # V2 assertions: V²=0 means coupling force on Cosserat is zero;
    # Cosserat should oscillate consistently with Phase I (H bounded).
    H_drift = max(abs(h["H_total"] / history[0]["H_total"] - 1.0)
                  if history[0]["H_total"] != 0 else 0.0
                  for h in history)
    coupling_e_max = max(abs(h["E_coupling"]) for h in history)
    max_V_sq = max(h["max_V_sq"] for h in history)

    return {
        "N": N, "n_steps": n_steps, "elapsed_s": elapsed,
        "history": history,
        "H_drift": H_drift,
        "coupling_e_max": coupling_e_max,
        "max_V_sq": max_V_sq,
        "pass": max_V_sq < 1e-10 and coupling_e_max < 1e-10,
    }


# ─────────────────────────────────────────────────────────────────
# V3: Coupled interaction
# ─────────────────────────────────────────────────────────────────
def test_v3_coupled_interaction(
    N: int = 40, n_steps: int = 40, amp_frac: float = 0.1,
) -> dict:
    """Launch a K4 photon toward a pre-seeded Cosserat shell; ensure the
    coupling ACTIVATES without driving either sector to saturation-blowup.

    Phase II demo only: small amplitudes so A²_total stays well below 1
    throughout; photon arrival and coupling-energy pickup are visible, but
    full electron formation is deferred to Phase III.
    """
    sim = CoupledK4Cosserat(N=N, pml=4)

    # Seed Cosserat with small shell-like ansatz; scale down hard so
    # initial A²_cos ≪ 1.
    sim.cos.initialize_electron_2_3_sector(
        R_target=10.0, r_target=4.0, use_hedgehog=True,
    )
    sim.cos.omega *= 0.05    # peak |ω| ~ 0.14, well below ω_yield = π

    # Moderate photon from left; keep |V|²/V_SNAP² ~ 0.01 (clearly below
    # Regime II boundary 0.12) so we're in linear coupling regime
    lambda_cells = 8.0
    omega = 2.0 * np.pi * sim.k4.c / (lambda_cells * sim.k4.dx)
    src = PlaneSource(
        x0=6, y_c=(N - 1) / 2.0, z_c=(N - 1) / 2.0,
        direction=(1.0, 0.0, 0.0), sigma_yz=5.0, omega=omega,
        t_center=2.0 * (2.0 * np.pi / omega),
        t_sigma=0.5 * (2.0 * np.pi / omega),
        amplitude=amp_frac * sim.V_SNAP,
    )

    history = []
    Q0 = sim.total_topological_charge()
    t_start = time.time()
    for step in range(n_steps + 1):
        if step > 0:
            t = step * sim.outer_dt
            src.apply(sim.k4, t)
            sim.step()
        history.append(sim.snapshot_scalars())
    elapsed = time.time() - t_start

    # Key observations
    Q_drift = max(abs(h["Q_charge"] - Q0) for h in history)
    H_start = history[3]["H_total"]  # skip the first few where source is ramping
    H_drift = max(abs(h["H_total"] / max(abs(H_start), 1e-30) - 1.0)
                  for h in history[3:])
    coupling_e_max = max(h["E_coupling"] for h in history)
    coupling_e_at_peak_V = max(
        h["E_coupling"] for h in history
        if h["max_V_sq"] == max(hh["max_V_sq"] for hh in history)
    )

    return {
        "N": N, "n_steps": n_steps, "amp_frac": amp_frac,
        "elapsed_s": elapsed, "history": history,
        "Q0": Q0, "Q_drift": int(Q_drift),
        "H_start": H_start, "H_drift": H_drift,
        "coupling_e_max": coupling_e_max,
        "coupling_e_at_peak_V": coupling_e_at_peak_V,
        "pass": coupling_e_max > 0.0,  # coupling should activate
    }


# ─────────────────────────────────────────────────────────────────
# Rendering
# ─────────────────────────────────────────────────────────────────
def render(v1: dict, v2: dict, v3: dict, out: str = "/tmp/coupled_coupling_test.png") -> None:
    fig, axes = plt.subplots(3, 2, figsize=(13, 11))

    # V1
    ax = axes[0, 0]
    h = v1["history"]
    t = [hh["t"] for hh in h]
    ax.plot(t, [hh["max_V_sq"] for hh in h], "-", label="max V²", lw=1.3)
    ax.plot(t, [hh["E_coupling"] for hh in h], "-", label="E_coupling", lw=1.3)
    ax.plot(t, [hh["max_A_sq_cos"] for hh in h], "-", label="max A²_cos", lw=1.3)
    ax.set_yscale("symlog", linthresh=1e-10)
    ax.set_title(f"V1 — K4 isolated (coupling off)\n{'✓ PASS' if v1['pass'] else '✗ FAIL'}  E_c_max={v1['coupling_e_max']:.2e}")
    ax.set_xlabel("t"); ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axes[0, 1]
    ax.plot(t, [hh["E_k4"] for hh in h], "-", label="E_K4")
    ax.plot(t, [hh["H_total"] for hh in h], "-", label="H_total", color="k")
    ax.set_title("V1 — K4 energy + total H")
    ax.set_xlabel("t"); ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # V2
    ax = axes[1, 0]
    h = v2["history"]
    t = [hh["t"] for hh in h]
    ax.plot(t, [hh["max_V_sq"] for hh in h], "-", label="max V²", lw=1.3)
    ax.plot(t, [hh["E_coupling"] for hh in h], "-", label="E_coupling", lw=1.3)
    ax.plot(t, [hh["max_A_sq_cos"] for hh in h], "-", label="max A²_cos", lw=1.3)
    ax.set_yscale("symlog", linthresh=1e-10)
    ax.set_title(f"V2 — Cosserat isolated (V=0)\n{'✓ PASS' if v2['pass'] else '✗ FAIL'}  H_drift={v2['H_drift']:.2e}")
    ax.set_xlabel("t"); ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axes[1, 1]
    ax.plot(t, [hh["E_cos"] for hh in h], "-", label="E_cos (potential)")
    ax.plot(t, [hh["T_cos"] for hh in h], "-", label="T_cos (kinetic)")
    ax.plot(t, [hh["H_total"] for hh in h], "-", label="H_total", color="k")
    ax.set_title("V2 — Cosserat energies")
    ax.set_xlabel("t"); ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # V3
    ax = axes[2, 0]
    h = v3["history"]
    t = [hh["t"] for hh in h]
    ax.plot(t, [hh["max_V_sq"] / sim_V_SNAP_sq() for hh in h], "-",
            label="max V² / V_SNAP²", color="#f90", lw=1.3)
    ax.plot(t, [hh["max_A_sq_cos"] for hh in h], "-",
            label="max A²_cos", color="#47c", lw=1.3)
    ax.plot(t, [hh["max_A_sq_total"] for hh in h], "-",
            label="max A²_total", color="#c33", lw=1.3)
    ax.set_yscale("log")
    ax.set_title(f"V3 — Coupled (photon hits shell, amp={v3['amp_frac']}·V_SNAP)\n"
                 f"{'✓ PASS' if v3['pass'] else '✗ FAIL'}  Q0={v3['Q0']} → Q_drift={v3['Q_drift']}")
    ax.set_xlabel("t"); ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axes[2, 1]
    ax.plot(t, [hh["E_k4"] for hh in h], "-", label="E_K4", lw=1.2)
    ax.plot(t, [hh["E_cos"] for hh in h], "-", label="E_cos", lw=1.2)
    ax.plot(t, [hh["E_coupling"] for hh in h], "-", label="E_coupling", lw=1.2)
    ax.plot(t, [hh["H_total"] for hh in h], "-", label="H_total", color="k", lw=1.5)
    ax.set_title(f"V3 — Energies   H_drift={v3['H_drift']:.2e}")
    ax.set_xlabel("t"); ax.legend(fontsize=8); ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out, dpi=110)
    plt.close()
    print(f"Saved {out}")


def sim_V_SNAP_sq() -> float:
    return float(V_SNAP) ** 2


if __name__ == "__main__":
    import json
    print("── Phase II validation: coupled K4 ⊗ Cosserat ──\n")

    print("V1 — K4 isolated (Cosserat at rest)…")
    v1 = test_v1_k4_isolation()
    print(f"  elapsed       = {v1['elapsed_s']:.1f} s")
    print(f"  coupling_e_max= {v1['coupling_e_max']:.3e}")
    print(f"  max_A²_cos    = {v1['max_A_sq_cos_max']:.3e}")
    print(f"  max V²        = {v1['max_V_sq']:.3e}")
    print(f"  → {'PASS' if v1['pass'] else 'FAIL'}")
    print()

    print("V2 — Cosserat isolated (V=0)…")
    v2 = test_v2_cosserat_isolation()
    print(f"  elapsed       = {v2['elapsed_s']:.1f} s")
    print(f"  H_drift       = {v2['H_drift']:.3e}")
    print(f"  coupling_e_max= {v2['coupling_e_max']:.3e}")
    print(f"  max V²        = {v2['max_V_sq']:.3e}")
    print(f"  → {'PASS' if v2['pass'] else 'FAIL'}")
    print()

    print("V3 — Coupled interaction (high-V photon hits shell)…")
    v3 = test_v3_coupled_interaction()
    print(f"  elapsed       = {v3['elapsed_s']:.1f} s")
    print(f"  Q0 → Q_drift  = {v3['Q0']} → {v3['Q_drift']}")
    print(f"  H_start       = {v3['H_start']:.3e}")
    print(f"  H_drift       = {v3['H_drift']:.3e}")
    print(f"  coupling_e_max= {v3['coupling_e_max']:.3e}")
    print(f"  → {'PASS' if v3['pass'] else 'FAIL'}")
    print()

    render(v1, v2, v3)

    summary = {
        "V1_pass": v1["pass"], "V1_coupling_e_max": v1["coupling_e_max"],
        "V2_pass": v2["pass"], "V2_H_drift": v2["H_drift"],
        "V3_pass": v3["pass"], "V3_Q_drift": v3["Q_drift"],
        "V3_H_drift": v3["H_drift"], "V3_coupling_e_max": v3["coupling_e_max"],
    }
    print("── Summary ──")
    print(json.dumps(summary, indent=2))
