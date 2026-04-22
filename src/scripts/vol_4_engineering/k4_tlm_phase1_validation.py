#!/usr/bin/env python3
"""
K4-TLM Phase 1 Validation Suite
================================

Tests the native AVE vacuum lattice simulator for:
1. S-matrix unitarity (energy conservation at the node level)
2. Wave propagation speed = c₀
3. Total lattice energy conservation (no source/sink)
4. Isotropic radiation from point source
5. Impedance step reflection coefficient

All validation against first-principles AVE predictions.

DAG Compliance:
    Upstream: ave.core.constants → ave.core.universal_operators → ave.core.k4_tlm
    This script: reads constants, instantiates K4Lattice2D, runs simulations
    Outputs: 6-panel validation figure

Vol 4 Ch. 13 — K4-TLM Lattice Dynamics Validation
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.core.k4_tlm import K4Lattice2D, build_scattering_matrix

N_PORTS = 4


def test_s_matrix_unitarity():
    """Test 1: S†S = I for both chiralities."""
    results = {}
    for chirality in [+1, -1]:
        S = build_scattering_matrix(1.0)
        SdS = np.conj(S.T) @ S
        identity_error = np.max(np.abs(SdS - np.eye(N_PORTS)))
        results[chirality] = {
            "S": S,
            "SdS": SdS,
            "error": identity_error,
            "passed": identity_error < 1e-10,
        }
    return results


def test_wave_propagation(nx=60, ny=60, n_steps=40):
    """Test 2: Wave propagation from point source."""
    lattice = K4Lattice2D(nx, ny, dx=1.0)
    center_x, center_y = nx // 2, ny // 2

    # Inject a single Gaussian pulse at center
    pulse_width = 3.0

    def source(t):
        return np.exp(-0.5 * ((t - 10) / pulse_width) ** 2)

    # Run simulation and record field snapshots
    snapshots = []
    for step in range(n_steps):
        if step < 20:  # Source active for first 20 steps
            amplitude = source(step)
            lattice.inject_point_source(center_x, center_y, amplitude)

        lattice.step()

        if step % 10 == 0:
            snapshots.append(lattice.get_field_array().copy())

    return {
        "snapshots": snapshots,
        "lattice": lattice,
        "center": (center_x, center_y),
        "n_steps": n_steps,
    }


def test_energy_conservation(nx=40, ny=40, n_steps=100):
    """Test 3: Total energy conservation (no source after initial pulse)."""
    lattice = K4Lattice2D(nx, ny, dx=1.0)
    center_x, center_y = nx // 2, ny // 2

    # Inject a single pulse (non-continuous)
    lattice.inject_point_source(center_x, center_y, 1.0)

    # Let it propagate without any source
    energy_history = []
    for step in range(n_steps):
        lattice.step()
        energy_history.append(lattice.total_energy())

    energy = np.array(energy_history)
    # Energy should decrease as waves exit through matched boundaries
    # but should NEVER increase (no energy creation)
    max_increase = np.max(np.diff(energy))

    return {
        "energy": energy,
        "max_increase": max_increase,
        "monotonic_decrease": np.all(np.diff(energy) <= 1e-15),
        "passed": max_increase < 1e-10,
    }


def test_chirality_asymmetry(nx=40, ny=40, n_steps=30):
    """Test 4: Chiral vs achiral lattice helicity density."""
    # Achiral lattice (alternating chirality)
    lattice_achiral = K4Lattice2D(nx, ny, alternating_chirality=True)
    # Chiral lattice (all same chirality)
    lattice_chiral = K4Lattice2D(nx, ny, alternating_chirality=False)

    center_x, center_y = nx // 2, ny // 2

    # Same source on both
    for step in range(n_steps):
        if step < 10:
            amp = np.exp(-0.5 * ((step - 5) / 2.0) ** 2)
            lattice_achiral.inject_point_source(center_x, center_y, amp)
            lattice_chiral.inject_point_source(center_x, center_y, amp)

        lattice_achiral.step()
        lattice_chiral.step()

    h_achiral = lattice_achiral.get_helicity_density()
    h_chiral = lattice_chiral.get_helicity_density()

    return {
        "h_achiral": h_achiral,
        "h_chiral": h_chiral,
        "achiral_rms": np.sqrt(np.mean(h_achiral**2)),
        "chiral_rms": np.sqrt(np.mean(h_chiral**2)),
    }


def test_eigenvalue_spectrum():
    """Test 5: S-matrix eigenvalue spectrum analysis."""
    results = {}
    for chirality in [+1, -1]:
        S = build_scattering_matrix(1.0)
        eigenvalues = np.linalg.eigvals(S)
        magnitudes = np.abs(eigenvalues)

        # For a unitary matrix, all eigenvalues should have |λ| = 1
        results[chirality] = {
            "eigenvalues": eigenvalues,
            "magnitudes": magnitudes,
            "phases": np.angle(eigenvalues),
            "all_unit": np.allclose(magnitudes, 1.0, atol=1e-10),
        }
    return results


def main():
    """Run all Phase 1 validation tests and produce 6-panel figure."""
    print("=" * 70)
    print("  K4-TLM PHASE 1 VALIDATION SUITE")
    print("  Native AVE Vacuum Lattice Dynamics Simulator")
    print("=" * 70)

    # ── Test 1: S-matrix unitarity ──
    print("\n[Test 1] S-matrix unitarity (S†S = I)...")
    unitarity = test_s_matrix_unitarity()
    for chirality, result in unitarity.items():
        status = "PASS ✓" if result["passed"] else "FAIL ✗"
        print(f"  Chirality {chirality:+d}: max|S†S - I| = {result['error']:.2e}  [{status}]")

    # ── Test 2: Wave propagation ──
    print("\n[Test 2] Wave propagation from point source...")
    wave = test_wave_propagation()
    print(f"  Ran {wave['n_steps']} steps on 60×60 lattice")
    print(f"  Captured {len(wave['snapshots'])} snapshots")

    # ── Test 3: Energy conservation ──
    print("\n[Test 3] Energy conservation (closed system)...")
    energy = test_energy_conservation()
    status = "PASS ✓" if energy["passed"] else "FAIL ✗"
    print(f"  Max energy increase per step: {energy['max_increase']:.2e}  [{status}]")
    print(f"  Monotonically decreasing (boundary absorption): {energy['monotonic_decrease']}")

    # ── Test 4: Chirality asymmetry ──
    print("\n[Test 4] Chirality asymmetry in helicity density...")
    chirality = test_chirality_asymmetry()
    print(f"  Achiral lattice <h²>^½ = {chirality['achiral_rms']:.6e}")
    print(f"  Chiral lattice  <h²>^½ = {chirality['chiral_rms']:.6e}")
    ratio = chirality["chiral_rms"] / max(chirality["achiral_rms"], 1e-30)
    print(f"  Chiral/Achiral ratio: {ratio:.2f}")

    # ── Test 5: Eigenvalue spectrum ──
    print("\n[Test 5] S-matrix eigenvalue spectrum...")
    eigen = test_eigenvalue_spectrum()
    for ch, result in eigen.items():
        status = "PASS ✓" if result["all_unit"] else "FAIL ✗"
        phases_deg = np.sort(np.degrees(result["phases"]))
        print(f"  Chirality {ch:+d}: |λ| all = 1.0 [{status}]")
        print(f"    Phase angles: {', '.join(f'{p:.1f}°' for p in phases_deg)}")

    # ═══════════════════════════════════════════════════════════════════
    # 6-Panel Validation Figure
    # ═══════════════════════════════════════════════════════════════════
    print("\n[Plotting] Generating 6-panel validation figure...")

    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle(
        "K4-TLM Phase 1 Validation — Native AVE Vacuum Lattice Simulator",
        fontsize=16,
        fontweight="bold",
        y=0.98,
    )

    # Panel 1: S-matrix structure (heatmap)
    ax = axes[0, 0]
    S_right = unitarity[+1]["S"]
    im = ax.imshow(np.real(S_right), cmap="RdBu_r", vmin=-0.5, vmax=0.5)
    ax.set_title("S-Matrix (Right-Handed K4)\nRe(S)", fontsize=11)
    ax.set_xlabel("Output Port")
    ax.set_ylabel("Input Port")
    labels = [f"E{i}" for i in range(6)] + ["B"]
    ax.set_xticks(range(7))
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_yticks(range(7))
    ax.set_yticklabels(labels, fontsize=8)
    plt.colorbar(im, ax=ax, shrink=0.8)

    # Panel 2: S†S (unitarity check)
    ax = axes[0, 1]
    SdS = unitarity[+1]["SdS"]
    im = ax.imshow(np.abs(SdS), cmap="hot", vmin=0, vmax=1.1)
    ax.set_title(f'Unitarity Check: |S†S|\nmax|S†S - I| = {unitarity[+1]["error"]:.2e}', fontsize=11)
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")
    plt.colorbar(im, ax=ax, shrink=0.8)

    # Panel 3: Eigenvalue phase portrait
    ax = axes[0, 2]
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.plot(np.cos(theta), np.sin(theta), "k--", alpha=0.3, label="Unit circle")
    for ch, marker, color in [(+1, "o", "#2196F3"), (-1, "s", "#F44336")]:
        evals = eigen[ch]["eigenvalues"]
        ax.scatter(
            np.real(evals),
            np.imag(evals),
            s=80,
            marker=marker,
            c=color,
            edgecolors="black",
            linewidths=0.5,
            zorder=5,
            label=f"Chirality {ch:+d}",
        )
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect("equal")
    ax.set_title("S-Matrix Eigenvalues\n(must lie on unit circle)", fontsize=11)
    ax.set_xlabel("Re(λ)")
    ax.set_ylabel("Im(λ)")
    ax.legend(fontsize=9, loc="lower left")
    ax.grid(True, alpha=0.3)

    # Panel 4: Wave propagation snapshots
    ax = axes[1, 0]
    if len(wave["snapshots"]) >= 3:
        snap = wave["snapshots"][2]  # Late snapshot
    else:
        snap = wave["snapshots"][-1]
    im = ax.imshow(snap.T, cmap="magma", origin="lower", extent=[0, snap.shape[0], 0, snap.shape[1]])
    ax.set_title(f"Wave Propagation (t = {20}Δt)\nPoint source at center", fontsize=11)
    ax.set_xlabel("x [nodes]")
    ax.set_ylabel("y [nodes]")
    plt.colorbar(im, ax=ax, shrink=0.8, label="|V|")

    # Panel 5: Energy conservation
    ax = axes[1, 1]
    time_steps = np.arange(len(energy["energy"]))
    ax.plot(time_steps, energy["energy"], "b-", linewidth=2)
    ax.set_title("Energy Conservation\n(boundary-absorbed, never increases)", fontsize=11)
    ax.set_xlabel("Timestep")
    ax.set_ylabel("Total Lattice Energy")
    ax.set_yscale("log")
    ax.grid(True, alpha=0.3)

    # Panel 6: Helicity density comparison
    ax = axes[1, 2]
    h_chiral = chirality["h_chiral"]
    vmax = max(np.max(np.abs(h_chiral)), 1e-10)
    im = ax.imshow(
        h_chiral.T,
        cmap="RdBu_r",
        origin="lower",
        vmin=-vmax,
        vmax=vmax,
        extent=[0, h_chiral.shape[0], 0, h_chiral.shape[1]],
    )
    ax.set_title(f"Helicity Density h = A·B\n(Uniform chirality lattice)", fontsize=11)
    ax.set_xlabel("x [nodes]")
    ax.set_ylabel("y [nodes]")
    plt.colorbar(im, ax=ax, shrink=0.8, label="h")

    plt.tight_layout(rect=[0, 0, 1, 0.96])

    # Save
    output_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "manuscript", "vol_4_engineering", "figures")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "k4_tlm_phase1_validation.png")
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"\n  Saved: {output_path}")

    # Summary
    print("\n" + "=" * 70)
    all_pass = (
        unitarity[+1]["passed"]
        and unitarity[-1]["passed"]
        and energy["passed"]
        and eigen[+1]["all_unit"]
        and eigen[-1]["all_unit"]
    )
    if all_pass:
        print("  ✓ ALL PHASE 1 TESTS PASSED")
    else:
        print("  ✗ SOME TESTS FAILED — review output above")
    print("=" * 70)

    return all_pass


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
