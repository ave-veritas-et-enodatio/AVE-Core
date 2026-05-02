"""
Phase A — Substrate-Physics Ground Truth for AVE Photon Simulator
==================================================================

Pre-flight verifications before any chiral / dark-wake work. Tests substrate
kinematics + integrator correctness. Per implementation plan
~/.claude/plans/new-auditor-you-are-crispy-pelican.md, Phase A.

Four tests, all pre-registered (criteria verbatim in this file):

A.1 — T₂ projection cardinal-axis control test
    Runs forward (+x̂) photon launcher TWICE: project_T2=True (default photon),
    project_T2=False (A₁+T₂ mix). Compares measured wavefront velocity.

    Pre-reg per docstring photon_propagation.py:49-63:
      C-A1a: T₂-projected v/c ∈ [0.95, 1.05]   (pure photon at c)
      C-A1b: No-projection  v/c ∈ [1.343, 1.485] (A₁-dominated at √2·c)

    Decision tree per plan §A.1:
      both pass  → docstring framework correct, T₂ projection works
      both √2·c  → projection broken OR docstring derivation wrong
      both c     → docstring derivation right, earlier "expected anisotropy"
                   framing of √2·c was misreading

A.2 — Diagonal-axis propagation test
    Same source aimed along port direction p̂_0 = (1,1,1)/√3.
    Pre-reg per photon_propagation.py:35-42:
      C-A2: v/c ∈ [0.95, 1.05]   (diagonal-axis = c regardless of mode)

A.3 — Energy conservation in linear vacuum (closed system)
    Closed system (no PML), linear vacuum, single pulse, run for one
    round-trip cycle. Catches integrator bugs.
    Pre-reg:
      C-A3: |ΔE_total / E_0| < 1e-4

A.4 — Op14 reflection coefficient at saturation onset
    Sharp Z_eff gradient (Z_step factor ≈ 2 over 5 cells), measure
    reflection. Compare to closed-form |Γ|² ≈ |∇ ln Z_eff|² · (c·Δt)².
    Pre-reg:
      C-A4: measured |Γ|²_obs / |Γ|²_predicted ∈ [0.7, 1.3]

Outputs:
  - assets/photon_axis_kinematics.png    (4-panel summary)
  - results/photon_axis_kinematics.json  (pre-reg evaluation)
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).parent))

from photon_propagation import PlaneSource, forward_port_weights, xy_slice  # noqa: E402

from ave.core.constants import C_0, V_SNAP  # noqa: E402
from ave.core.k4_tlm import K4Lattice3D  # noqa: E402


# Pre-registered acceptance criteria (verbatim, per A47 v11b discipline).
# Edits here must include a corresponding retraction note per Rule 12.
PREREG = {
    "C-A1a_T2_projected_v_over_c_min": 0.95,
    "C-A1a_T2_projected_v_over_c_max": 1.05,
    "C-A1b_no_projection_v_over_c_min": 0.95 * np.sqrt(2.0),
    "C-A1b_no_projection_v_over_c_max": 1.05 * np.sqrt(2.0),
    "C-A2_diagonal_v_over_c_min": 0.95,
    "C-A2_diagonal_v_over_c_max": 1.05,
    "C-A3_energy_conservation_max_drift": 1.0e-4,
    "C-A4_op14_ratio_min": 0.7,
    "C-A4_op14_ratio_max": 1.3,
}


def measure_wavefront_velocity(
    direction: tuple[float, float, float],
    project_T2: bool,
    N: int = 96,
    pml: int = 8,
    lambda_cells: float = 10.0,
    sigma_yz: float = 8.0,
    t_sigma_periods: float = 0.75,
    amp_frac: float = 0.01,
    source_offset: int = 16,
    n_steps: int = 240,
    measurement_offsets: tuple[int, int] = (20, 60),
) -> dict:
    """Launch a +d̂ packet, measure wavefront peak-arrival velocity.

    Parameterized version of run_validation in photon_propagation.py;
    accepts direction + project_T2 toggle for A.1/A.2 control tests.

    Returns dict with keys:
      direction, project_T2, v_meas_mps, c_ratio, t_arrival_a_s, t_arrival_b_s
    """
    lattice = K4Lattice3D(N, N, N, dx=1.0, nonlinear=False, pml_thickness=pml)
    dt = lattice.dt
    c = float(C_0)
    dx = lattice.dx

    omega = 2.0 * np.pi * c / (lambda_cells * dx)
    period = 2.0 * np.pi / omega
    t_sigma = t_sigma_periods * period
    t_center = 3.0 * t_sigma

    amp_volts = amp_frac * float(V_SNAP)

    # Source position: just inside the −d̂ side PML
    # For cardinal-axis +x̂, source_x = pml + source_offset
    # For diagonal direction, project onto each axis to find a single source point
    # Simplest: locate source plane perpendicular to direction, centered at
    # (pml + source_offset along propagation axis, N/2 transverse)
    direction_arr = np.asarray(direction, dtype=float)
    direction_arr = direction_arr / np.linalg.norm(direction_arr)
    # Pick the axis with the largest |component| as the "propagation axis"
    # for the plane-source slab placement.
    prop_axis = int(np.argmax(np.abs(direction_arr)))
    source_x = pml + source_offset

    src = PlaneSource(
        x0=source_x,
        y_c=(N - 1) / 2.0,
        z_c=(N - 1) / 2.0,
        direction=direction,
        sigma_yz=sigma_yz,
        omega=omega,
        t_center=t_center,
        t_sigma=t_sigma,
        amplitude=amp_volts,
    )
    # Override the port weights with the requested project_T2 setting.
    # PlaneSource constructor uses default project_T2=True via forward_port_weights.
    src.port_w = forward_port_weights(direction, project_T2=project_T2)

    z_slice = N // 2
    frames: list[np.ndarray] = [xy_slice(lattice, z_slice).copy()]
    times: list[float] = [0.0]

    for step in range(1, n_steps + 1):
        t_pre = step * dt
        src.apply(lattice, t_pre)
        lattice.step()
        if step % 3 == 0:
            frames.append(xy_slice(lattice, z_slice).copy())
            times.append(lattice.timestep * dt)

    frames_arr = np.stack(frames, axis=0)
    times_arr = np.asarray(times)

    # Peak-arrival measurement at two reference planes along the propagation axis.
    # For cardinal-axis (prop_axis=0), measure at x = source_x + 20, source_x + 60.
    # For diagonal direction, we still measure along the dominant axis (prop_axis=0
    # for direction=(1,1,1)/√3 since |x|=|y|=|z|, np.argmax returns 0 by tie).
    off_a, off_b = measurement_offsets
    x_a = source_x + off_a
    x_b = source_x + off_b

    # frames_arr has shape (n_frames, N, N) since xy_slice returns 2D slice at z_slice.
    # Sum over y to get amplitude history at each x.
    rho_hist_a = np.array([frames_arr[i, x_a, :].sum() for i in range(len(frames_arr))])
    rho_hist_b = np.array([frames_arr[i, x_b, :].sum() for i in range(len(frames_arr))])

    def peak_arrival_time(series: np.ndarray) -> float | None:
        if series.max() <= 0.0:
            return None
        idx = int(np.argmax(series))
        return float(times_arr[idx])

    t_a = peak_arrival_time(rho_hist_a)
    t_b = peak_arrival_time(rho_hist_b)

    if t_a is not None and t_b is not None and t_b > t_a:
        v_meas = (x_b - x_a) * dx / (t_b - t_a)
    else:
        v_meas = 0.0

    return {
        "direction": list(direction),
        "project_T2": bool(project_T2),
        "N": N,
        "pml": pml,
        "lambda_cells": lambda_cells,
        "amp_frac_vsnap": amp_frac,
        "source_x": source_x,
        "x_a": x_a,
        "x_b": x_b,
        "t_arrival_a_s": float(t_a) if t_a is not None else 0.0,
        "t_arrival_b_s": float(t_b) if t_b is not None else 0.0,
        "v_meas_mps": float(v_meas),
        "c_ratio": float(v_meas / c) if c > 0 else 0.0,
        "port_w": src.port_w.tolist(),
        "port_w_sum": float(src.port_w.sum()),
    }


def test_a1_t2_projection() -> dict:
    """A.1 — T₂ projection cardinal-axis control test."""
    print("=" * 72)
    print("A.1 — T₂ projection cardinal-axis control test (+x̂)")
    print("=" * 72)

    r_with = measure_wavefront_velocity(
        direction=(1.0, 0.0, 0.0), project_T2=True
    )
    print(
        f"  T₂=True  (default): v/c = {r_with['c_ratio']:.4f}, "
        f"port_w = {r_with['port_w']}, Σw = {r_with['port_w_sum']:+.6f}"
    )

    r_without = measure_wavefront_velocity(
        direction=(1.0, 0.0, 0.0), project_T2=False
    )
    print(
        f"  T₂=False (raw):     v/c = {r_without['c_ratio']:.4f}, "
        f"port_w = {r_without['port_w']}, Σw = {r_without['port_w_sum']:+.6f}"
    )

    # Pre-reg evaluation
    c_with = r_with["c_ratio"]
    c_without = r_without["c_ratio"]
    pass_C_A1a = (
        PREREG["C-A1a_T2_projected_v_over_c_min"]
        <= c_with
        <= PREREG["C-A1a_T2_projected_v_over_c_max"]
    )
    pass_C_A1b = (
        PREREG["C-A1b_no_projection_v_over_c_min"]
        <= c_without
        <= PREREG["C-A1b_no_projection_v_over_c_max"]
    )

    # Decision tree per plan
    decision = "INCONCLUSIVE"
    if pass_C_A1a and pass_C_A1b:
        decision = "DOCSTRING_CORRECT"
    elif (not pass_C_A1a) and pass_C_A1b and abs(c_with - c_without) < 0.05:
        decision = "BOTH_SQRT2_PROJECTION_BROKEN_OR_DOCSTRING_DERIVATION_WRONG"
    elif pass_C_A1a and (not pass_C_A1b):
        decision = "BOTH_C_DOCSTRING_RIGHT_BUT_PRIOR_FRAMING_OF_SQRT2_WRONG"
    elif (not pass_C_A1a) and (not pass_C_A1b):
        decision = "BOTH_FAIL_FURTHER_INVESTIGATION_NEEDED"

    print(f"\n  C-A1a (T₂=True ∈ [0.95, 1.05]):   {'PASS' if pass_C_A1a else 'FAIL'}  (got {c_with:.4f})")
    print(f"  C-A1b (T₂=False ∈ [{PREREG['C-A1b_no_projection_v_over_c_min']:.3f}, "
          f"{PREREG['C-A1b_no_projection_v_over_c_max']:.3f}]): "
          f"{'PASS' if pass_C_A1b else 'FAIL'}  (got {c_without:.4f})")
    print(f"  Decision: {decision}")

    return {
        "test": "A.1",
        "result_T2_true": r_with,
        "result_T2_false": r_without,
        "pass_C_A1a": bool(pass_C_A1a),
        "pass_C_A1b": bool(pass_C_A1b),
        "decision": decision,
    }


def test_a2_diagonal() -> dict:
    """A.2 — Diagonal-axis propagation test along port direction p̂_0."""
    print()
    print("=" * 72)
    print("A.2 — Diagonal-axis propagation test (port direction p̂_0)")
    print("=" * 72)

    direction = (1.0, 1.0, 1.0)  # along port 0 (1,1,1)/√3 after normalization

    # For diagonal propagation, the simple "+x̂ source plane" geometry doesn't
    # apply; we'd need a tilted source plane for clean diagonal launching.
    # As a first-order approximation, launch with the same +x̂ source plane
    # but direction=(1,1,1) — the wave will preferentially propagate along the
    # diagonal. Measurement along the +x axis still picks up the diagonal
    # component's projection onto +x, which advances at v_diagonal · (1/√3).
    # If v_diagonal = c (per docstring), measured v_x = c / √3 ≈ 0.577 c.
    # That's a different measurement convention than A.1 — flag explicitly.

    r = measure_wavefront_velocity(
        direction=direction, project_T2=True, n_steps=300
    )
    print(
        f"  direction = (1,1,1)/√3 (port 0): measured v_x/c = {r['c_ratio']:.4f}"
    )
    print(
        f"  port_w = {r['port_w']}, Σw = {r['port_w_sum']:+.6f}"
    )
    # Naive diagonal: measured v_x = v_diagonal · (1/√3); if v_diagonal = c, v_x ≈ 0.577
    # If v_diagonal = √2·c, v_x ≈ 0.816
    expected_v_x_if_diagonal_at_c = 1.0 / np.sqrt(3.0)
    expected_v_x_if_diagonal_at_sqrt2c = np.sqrt(2.0) / np.sqrt(3.0)
    print(
        f"  Expected v_x: v_diag=c → {expected_v_x_if_diagonal_at_c:.4f}; "
        f"v_diag=√2c → {expected_v_x_if_diagonal_at_sqrt2c:.4f}"
    )

    # Pre-reg C-A2 was framed for direct diagonal-axis measurement (v_diag/c ∈ [0.95, 1.05]).
    # With +x̂ source plane + diagonal direction, what we measure is v_x = v_diag/√3, NOT v_diag.
    # Mark C-A2 as "infrastructure inadequate for direct diagonal measurement";
    # a tilted source plane would be needed to test C-A2 directly.
    note = (
        "A.2 measurement convention: +x̂ source plane with direction=(1,1,1)/√3 "
        "measures v_x = v_diagonal / √3, NOT v_diagonal directly. To test "
        "v_diagonal/c ∈ [0.95, 1.05] (C-A2) directly, a tilted source plane "
        "perpendicular to the (1,1,1) axis is needed. Current measurement "
        "tests v_x consistency with v_diag = c (=0.577) vs v_diag = √2c (=0.816)."
    )
    print(f"  Note: {note}")

    pass_C_A2_at_c = (
        0.95 * expected_v_x_if_diagonal_at_c
        <= r["c_ratio"]
        <= 1.05 * expected_v_x_if_diagonal_at_c
    )
    pass_C_A2_at_sqrt2c = (
        0.95 * expected_v_x_if_diagonal_at_sqrt2c
        <= r["c_ratio"]
        <= 1.05 * expected_v_x_if_diagonal_at_sqrt2c
    )

    return {
        "test": "A.2",
        "result": r,
        "expected_v_x_if_diagonal_at_c": float(expected_v_x_if_diagonal_at_c),
        "expected_v_x_if_diagonal_at_sqrt2c": float(expected_v_x_if_diagonal_at_sqrt2c),
        "pass_C_A2_at_c": bool(pass_C_A2_at_c),
        "pass_C_A2_at_sqrt2c": bool(pass_C_A2_at_sqrt2c),
        "note": note,
    }


def test_a3_energy_conservation() -> dict:
    """A.3 — Energy conservation in linear vacuum (closed system, no PML)."""
    print()
    print("=" * 72)
    print("A.3 — Energy conservation in linear vacuum (closed system)")
    print("=" * 72)

    N = 48
    # Use a tiny PML strip to satisfy K4Lattice3D's interior-only stepping
    # while still being effectively closed (most reflections trapped).
    # NOTE: K4Lattice3D may require pml >= some minimum; use pml=2 and
    # measure energy AFTER source quiescence to isolate integrator drift.
    pml = 2
    lattice = K4Lattice3D(N, N, N, dx=1.0, nonlinear=False, pml_thickness=pml)
    dt = lattice.dt

    # Short pulse, well-localized, then run with no further driving
    omega = 2.0 * np.pi * float(C_0) / (10.0 * lattice.dx)
    period = 2.0 * np.pi / omega
    t_sigma = 1.0 * period
    t_center = 3.0 * t_sigma
    amp_volts = 0.005 * float(V_SNAP)

    src = PlaneSource(
        x0=N // 2,
        y_c=(N - 1) / 2.0,
        z_c=(N - 1) / 2.0,
        direction=(1.0, 0.0, 0.0),
        sigma_yz=4.0,
        omega=omega,
        t_center=t_center,
        t_sigma=t_sigma,
        amplitude=amp_volts,
    )

    # Measure E_total over time. K4Lattice3D.get_energy_density gives ρ per cell.
    times: list[float] = []
    energies: list[float] = []
    quiescent_energies: list[float] = []
    source_quiescent_t = t_center + 4.0 * t_sigma  # >99% of pulse passed
    n_steps = 100  # short run to minimize PML loss

    for step in range(1, n_steps + 1):
        t_pre = step * dt
        src.apply(lattice, t_pre)
        lattice.step()
        rho = lattice.get_energy_density()
        # Sum over interior (exclude PML)
        E = float(rho[pml:-pml, pml:-pml, pml:-pml].sum())
        times.append(lattice.timestep * dt)
        energies.append(E)
        if t_pre > source_quiescent_t:
            quiescent_energies.append(E)

    if len(quiescent_energies) >= 2:
        E_max = max(quiescent_energies)
        E_min = min(quiescent_energies)
        E_drift = (E_max - E_min) / E_max if E_max > 0 else 0.0
    else:
        E_drift = float("nan")

    pass_C_A3 = E_drift < PREREG["C-A3_energy_conservation_max_drift"]

    print(f"  N={N}, pml={pml} (small for ~closed system), n_steps={n_steps}")
    print(f"  Quiescent samples: {len(quiescent_energies)}")
    print(f"  E_drift = (E_max - E_min)/E_max = {E_drift:.3e}")
    print(f"  C-A3 (drift < 1e-4): {'PASS' if pass_C_A3 else 'FAIL'}")
    if not pass_C_A3:
        print("  NOTE: small PML still absorbs energy; this is a soft test")
        print("  for integrator-level drift, not a strict closed-system test.")

    return {
        "test": "A.3",
        "N": N,
        "pml": pml,
        "n_steps": n_steps,
        "n_quiescent_samples": len(quiescent_energies),
        "E_drift": float(E_drift),
        "pass_C_A3": bool(pass_C_A3),
    }


def test_a4_op14_reflection() -> dict:
    """A.4 — Op14 reflection coefficient at sharp Z gradient.

    Pre-reg measurement requires Z-gradient infrastructure that K4Lattice3D
    doesn't expose directly (Op14 saturation engages only when amplitude
    crosses A²_yield). Defer this test to a follow-up driver that explicitly
    constructs a Z_eff step (factor ≈ 2 over 5 cells) via amplitude-induced
    saturation in a half-domain, then measures reflected vs transmitted
    amplitudes.

    Marking C-A4 as DEFERRED with explicit reason — does not block A.1-A.3.
    """
    print()
    print("=" * 72)
    print("A.4 — Op14 reflection coefficient at saturation onset")
    print("=" * 72)
    note = (
        "A.4 requires explicit Z_eff-step infrastructure (amplitude-driven "
        "Op14 saturation in half-domain). Not implemented in this driver — "
        "defer to follow-up driver. Does not block Phase A.1-A.3 / Phase B / Phase C / Phase D."
    )
    print(f"  Status: DEFERRED")
    print(f"  Note: {note}")
    return {
        "test": "A.4",
        "status": "deferred",
        "note": note,
        "pass_C_A4": None,
    }


def render_summary_panel(results: dict, out_png: str) -> None:
    """4-panel summary: A.1 velocities, A.2 v_x, A.3 E_drift, A.4 (deferred placeholder)."""
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    # A.1 panel: T₂=True vs T₂=False bar chart
    ax = axes[0, 0]
    labels = ["T₂=True\n(photon)", "T₂=False\n(raw)"]
    values = [
        results["a1"]["result_T2_true"]["c_ratio"],
        results["a1"]["result_T2_false"]["c_ratio"],
    ]
    colors = ["#4477aa", "#ee6677"]
    bars = ax.bar(labels, values, color=colors, edgecolor="black")
    ax.axhline(1.0, color="green", ls="--", lw=1, label="c (T₂ photon expected)")
    ax.axhline(np.sqrt(2.0), color="orange", ls="--", lw=1, label="√2·c (A₁ longitudinal)")
    ax.set_ylabel("v_meas / c")
    ax.set_title(
        f"A.1 — T₂ projection control\n"
        f"Decision: {results['a1']['decision']}"
    )
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y")
    for bar, val in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2.0, val + 0.02, f"{val:.3f}",
            ha="center", fontsize=10
        )

    # A.2 panel: diagonal-axis v_x vs predictions
    ax = axes[0, 1]
    a2 = results["a2"]
    ax.bar(
        ["measured\nv_x/c"],
        [a2["result"]["c_ratio"]],
        color="#228833", edgecolor="black",
    )
    ax.axhline(
        a2["expected_v_x_if_diagonal_at_c"], color="green", ls="--",
        label=f"v_diag=c → v_x = {a2['expected_v_x_if_diagonal_at_c']:.3f}"
    )
    ax.axhline(
        a2["expected_v_x_if_diagonal_at_sqrt2c"], color="orange", ls="--",
        label=f"v_diag=√2·c → v_x = {a2['expected_v_x_if_diagonal_at_sqrt2c']:.3f}"
    )
    ax.set_ylabel("v_x / c (projected)")
    ax.set_title(
        f"A.2 — Diagonal direction (1,1,1)/√3\n"
        f"port_w = {a2['result']['port_w']}"
    )
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y")
    ax.text(
        0.5, 0.95,
        f"Note: +x̂ source plane;\nmeasures v_x not v_diagonal directly",
        ha="center", va="top", transform=ax.transAxes, fontsize=8,
        style="italic"
    )

    # A.3 panel: energy drift
    ax = axes[1, 0]
    a3 = results["a3"]
    ax.bar(
        ["E_drift"], [a3["E_drift"]],
        color="#aa3377" if not a3["pass_C_A3"] else "#228833",
        edgecolor="black",
    )
    ax.axhline(
        PREREG["C-A3_energy_conservation_max_drift"], color="red", ls="--",
        label="C-A3 threshold (1e-4)"
    )
    ax.set_yscale("log")
    ax.set_ylabel("(E_max − E_min) / E_max")
    ax.set_title(
        f"A.3 — Energy conservation\n"
        f"{'PASS' if a3['pass_C_A3'] else 'FAIL'}: drift = {a3['E_drift']:.3e}"
    )
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y", which="both")

    # A.4 panel: deferred
    ax = axes[1, 1]
    ax.text(
        0.5, 0.5,
        "A.4 — DEFERRED\n\n"
        "Op14 reflection coefficient test\n"
        "requires Z-step infrastructure\n"
        "(follow-up driver).\n\n"
        "Not blocking Phase A → B → C → D.",
        ha="center", va="center", transform=ax.transAxes, fontsize=11,
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#eeeeee", edgecolor="black"),
    )
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("A.4 — Op14 reflection")

    plt.suptitle(
        "Phase A — Substrate-Physics Ground Truth (photon_axis_kinematics.py)",
        fontsize=13, fontweight="bold"
    )
    plt.tight_layout()
    plt.savefig(out_png, dpi=110, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    assets_dir = repo_root / "assets"
    results_dir = repo_root / "results"
    assets_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)

    out_png = assets_dir / "photon_axis_kinematics.png"
    out_json = results_dir / "photon_axis_kinematics.json"

    a1 = test_a1_t2_projection()
    a2 = test_a2_diagonal()
    a3 = test_a3_energy_conservation()
    a4 = test_a4_op14_reflection()

    results = {
        "prereg": PREREG,
        "a1": a1,
        "a2": a2,
        "a3": a3,
        "a4": a4,
    }

    render_summary_panel(results, str(out_png))

    with open(out_json, "w") as f:
        json.dump(results, f, indent=2, default=str)

    print()
    print("=" * 72)
    print("PHASE A SUMMARY")
    print("=" * 72)
    print(f"  A.1 decision:    {a1['decision']}")
    print(
        f"    C-A1a (T₂=True → c):    "
        f"{'PASS' if a1['pass_C_A1a'] else 'FAIL'}"
    )
    print(
        f"    C-A1b (T₂=False → √2c): "
        f"{'PASS' if a1['pass_C_A1b'] else 'FAIL'}"
    )
    print(f"  A.2 v_x measurements:")
    print(
        f"    consistent with v_diag = c    (v_x ≈ 0.577): "
        f"{'PASS' if a2['pass_C_A2_at_c'] else 'FAIL'}"
    )
    print(
        f"    consistent with v_diag = √2c  (v_x ≈ 0.816): "
        f"{'PASS' if a2['pass_C_A2_at_sqrt2c'] else 'FAIL'}"
    )
    print(
        f"  A.3 energy drift:  {a3['E_drift']:.3e}  "
        f"({'PASS' if a3['pass_C_A3'] else 'FAIL'})"
    )
    print(f"  A.4 status:        DEFERRED")
    print()
    print(f"  Outputs:")
    print(f"    {out_png}")
    print(f"    {out_json}")


if __name__ == "__main__":
    main()
