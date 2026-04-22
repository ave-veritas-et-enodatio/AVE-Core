#!/usr/bin/env python3
"""
K4-TLM Phase 2: Wire Antenna Resonance Analysis
=================================================

Simulates wire loop and torus knot antennas on the 2D K4-TLM lattice.
Validates resonant frequency via FFT of probe voltage against the
analytical prediction f_res = c/(2·L_wire).

Tests:
1. Rectangular loop antenna — resonance from FFT
2. (2,3) Trefoil knot (2D projection) — chiral coupling
3. Frequency comparison: loop vs knot
4. Helicity density maps for chiral vs achiral topologies

DAG Compliance:
    Upstream: ave.core.constants → ave.core.k4_tlm
    This script: instantiates lattice, generates wire paths, runs sims
    Outputs: 9-panel wire antenna analysis figure

Vol 4 Ch. 13 — K4-TLM Wire Antenna Validation
"""

import os
import sys

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from ave.core.constants import ALPHA  # noqa: E402
from ave.core.k4_tlm import K4Lattice2D  # noqa: E402


def generate_loop_path(cx, cy, radius, n_points=200):
    t = np.linspace(0, 2 * np.pi, n_points)
    x = cx + radius * np.cos(t)
    y = cy + radius * np.sin(t)
    path = []
    for i in range(len(x)):
        path.append((int(round(x[i])), int(round(y[i]))))
    unique_path = []
    for pt in path:
        if not unique_path or pt != unique_path[-1]:
            unique_path.append(pt)
    return unique_path


def generate_torus_knot_path_2d(cx, cy, R, r, p, q, n_points=300):
    t = np.linspace(0, 2 * np.pi, n_points)
    x = cx + (R + r * np.cos(q * t)) * np.cos(p * t)
    y = cy + (R + r * np.cos(q * t)) * np.sin(p * t)
    path = []
    for i in range(len(x)):
        path.append((int(round(x[i])), int(round(y[i]))))
    unique_path = []
    for pt in path:
        if not unique_path or pt != unique_path[-1]:
            unique_path.append(pt)
    return unique_path


def simulate_wire_antenna(
    nx, ny, wire_path, n_steps=500, source_freq_norm=0.1, probe_offset=5, alternating_chirality=True
):
    """
    Run a wire antenna simulation on the K4-TLM lattice.

    Injects CW sinusoidal current along the wire path and records
    the voltage at a probe point offset from the wire center.

    Args:
        nx, ny: Lattice dimensions.
        wire_path: List of (x, y) wire node coordinates.
        n_steps: Number of timesteps.
        source_freq_norm: Normalized source frequency (0 to 0.5).
        probe_offset: Distance from wire center to probe point.
        alternating_chirality: Lattice chirality pattern.

    Returns:
        dict with 'probe', 'time', 'wire_path', 'field_snapshot',
        'helicity', 'energy'
    """
    lattice = K4Lattice2D(nx, ny, alternating_chirality=alternating_chirality)

    # Find wire center for probe placement
    cx = int(np.mean([p[0] for p in wire_path]))
    cy = int(np.mean([p[1] for p in wire_path]))
    probe_x = min(cx + probe_offset, nx - 2)
    probe_y = cy

    omega = 2 * np.pi * source_freq_norm  # Normalized angular frequency

    probe_data = []
    energy_data = []

    for step in range(n_steps):
        # CW sinusoidal source along wire
        amplitude = np.sin(omega * step) * 0.1
        lattice.inject_wire_current(wire_path, amplitude, direction_port="auto")

        lattice.step()

        # Record probe
        probe_data.append(lattice.get_field(probe_x, probe_y))
        energy_data.append(lattice.total_energy())

    return {
        "probe": np.array(probe_data),
        "energy": np.array(energy_data),
        "time": np.arange(n_steps),
        "wire_path": wire_path,
        "field_snapshot": lattice.get_field_array(),
        "helicity": lattice.get_helicity_density(),
        "wire_length": len(wire_path),
        "lattice": lattice,
    }


def broadband_simulation(nx, ny, wire_path, n_steps=800, alternating_chirality=True):
    """
    Broadband (Gaussian pulse) simulation for FFT-based resonance detection.

    Injects a short Gaussian pulse along the wire and records the
    time-domain response at a probe point. The FFT of the probe signal
    reveals the resonant frequencies.

    Returns:
        dict with 'probe', 'fft_freq', 'fft_power', 'f_peak'
    """
    lattice = K4Lattice2D(nx, ny, alternating_chirality=alternating_chirality)

    cx = int(np.mean([p[0] for p in wire_path]))
    cy = int(np.mean([p[1] for p in wire_path]))
    probe_x = min(cx + 3, nx - 2)
    probe_y = cy

    pulse_width = 5.0
    pulse_center = 15.0

    probe_data = []

    for step in range(n_steps):
        # Gaussian pulse (broadband excitation)
        if step < 50:
            amplitude = np.exp(-0.5 * ((step - pulse_center) / pulse_width) ** 2) * 0.5
            lattice.inject_wire_current(wire_path, amplitude, direction_port="auto")

        lattice.step()
        probe_data.append(lattice.get_field(probe_x, probe_y))

    probe = np.array(probe_data)

    # FFT analysis
    # Window the signal to reduce spectral leakage
    window = np.hanning(len(probe))
    probe_windowed = probe * window

    fft = np.fft.rfft(probe_windowed)
    fft_power = np.abs(fft) ** 2
    fft_freq = np.fft.rfftfreq(len(probe))  # Normalized frequency (0 to 0.5)

    # Find peak frequency (skip DC)
    fft_power_no_dc = fft_power.copy()
    fft_power_no_dc[:3] = 0  # Skip very low frequencies
    f_peak_idx = np.argmax(fft_power_no_dc)
    f_peak = fft_freq[f_peak_idx]

    return {
        "probe": probe,
        "fft_freq": fft_freq,
        "fft_power": fft_power,
        "f_peak": f_peak,
        "wire_length": len(wire_path),
        "field_snapshot": lattice.get_field_array(),
        "helicity": lattice.get_helicity_density(),
    }


def main():
    """Run Phase 2 wire antenna analysis and produce 9-panel figure."""
    print("=" * 70)
    print("  K4-TLM PHASE 2: WIRE ANTENNA RESONANCE ANALYSIS")
    print("  Native AVE Vacuum Lattice Dynamics Simulator")
    print("=" * 70)

    NX, NY = 80, 80
    CENTER_X, CENTER_Y = NX // 2, NY // 2

    # ── 1. Rectangular Loop Antenna ──
    print("\n[1] Rectangular loop antenna (radius=8)...")
    loop_path = generate_loop_path(CENTER_X, CENTER_Y, radius=8)
    loop_result = broadband_simulation(NX, NY, loop_path, n_steps=800)
    print(f"    Wire length: {loop_result['wire_length']} nodes")
    print(f"    Resonant frequency (FFT peak): f = {loop_result['f_peak']:.4f} (normalized)")
    expected_f_loop = 0.5 / loop_result["wire_length"]  # f = c/(2L), c_norm=1
    print(f"    Predicted f_res = c/(2L) = {expected_f_loop:.4f}")

    # ── 2. (2,3) Trefoil Torus Knot ──
    print("\n[2] (2,3) Trefoil torus knot...")
    trefoil_path = generate_torus_knot_path_2d(CENTER_X, CENTER_Y, R=12, r=5, p=2, q=3, n_points=300)
    trefoil_result = broadband_simulation(NX, NY, trefoil_path, n_steps=800)
    print(f"    Wire length: {trefoil_result['wire_length']} nodes")
    print(f"    Resonant frequency (FFT peak): f = {trefoil_result['f_peak']:.4f}")
    expected_f_trefoil = 0.5 / trefoil_result["wire_length"]
    print(f"    Predicted f_res = c/(2L) = {expected_f_trefoil:.4f}")

    # ── 3. (3,5) Torus Knot (higher winding) ──
    print("\n[3] (3,5) Torus knot...")
    knot_35_path = generate_torus_knot_path_2d(CENTER_X, CENTER_Y, R=12, r=5, p=3, q=5, n_points=400)
    knot_35_result = broadband_simulation(NX, NY, knot_35_path, n_steps=800)
    print(f"    Wire length: {knot_35_result['wire_length']} nodes")
    print(f"    Resonant frequency (FFT peak): f = {knot_35_result['f_peak']:.4f}")
    expected_f_35 = 0.5 / knot_35_result["wire_length"]
    print(f"    Predicted f_res = c/(2L) = {expected_f_35:.4f}")

    # ── 4. Chiral vs Achiral comparison for trefoil ──
    print("\n[4] Chirality comparison (trefoil on chiral vs achiral lattice)...")
    trefoil_chiral = broadband_simulation(NX, NY, trefoil_path, n_steps=800, alternating_chirality=False)
    delta_f = abs(trefoil_chiral["f_peak"] - trefoil_result["f_peak"])
    print(f"    Achiral lattice f_peak: {trefoil_result['f_peak']:.4f}")
    print(f"    Chiral lattice  f_peak: {trefoil_chiral['f_peak']:.4f}")
    print(f"    Δf/f = {delta_f / max(trefoil_result['f_peak'], 1e-10):.4e}")

    # Chiral coupling prediction from AVE
    p_knot, q_knot = 2, 3
    alpha = float(ALPHA)
    predicted_shift = alpha * p_knot * q_knot / (p_knot + q_knot)
    print(f"    AVE predicted Δf/f = α·pq/(p+q) = {predicted_shift:.4e}")

    # ═══════════════════════════════════════════════════════════════════
    # 9-Panel Analysis Figure
    # ═══════════════════════════════════════════════════════════════════
    print("\n[Plotting] Generating 9-panel wire antenna analysis...")

    fig, axes = plt.subplots(3, 3, figsize=(18, 16))
    fig.suptitle(
        "K4-TLM Phase 2 — Wire Antenna Resonance Analysis\n" "Native AVE Vacuum Lattice Dynamics Simulator",
        fontsize=15,
        fontweight="bold",
        y=0.99,
    )

    # ── Row 1: Wire geometries ──

    # Panel 1: Loop antenna geometry + field
    ax = axes[0, 0]
    field = loop_result["field_snapshot"]
    im = ax.imshow(field.T, cmap="magma", origin="lower", extent=[0, NX, 0, NY])
    lx = [p[0] for p in loop_path] + [loop_path[0][0]]
    ly = [p[1] for p in loop_path] + [loop_path[0][1]]
    ax.plot(lx, ly, "c-", linewidth=1.5, alpha=0.8, label="Wire")
    ax.set_title("Rectangular Loop\n(radius = 8 nodes)", fontsize=11)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(fontsize=8)

    # Panel 2: Trefoil geometry + field
    ax = axes[0, 1]
    field = trefoil_result["field_snapshot"]
    im = ax.imshow(field.T, cmap="magma", origin="lower", extent=[0, NX, 0, NY])
    tx = [p[0] for p in trefoil_path] + [trefoil_path[0][0]]
    ty = [p[1] for p in trefoil_path] + [trefoil_path[0][1]]
    ax.plot(tx, ty, "c-", linewidth=1.0, alpha=0.8, label="Wire")
    ax.set_title("(2,3) Trefoil Knot\n(R=12, r=5)", fontsize=11)
    ax.set_xlabel("x")
    ax.legend(fontsize=8)

    # Panel 3: (3,5) knot geometry + field
    ax = axes[0, 2]
    field = knot_35_result["field_snapshot"]
    im = ax.imshow(field.T, cmap="magma", origin="lower", extent=[0, NX, 0, NY])
    kx = [p[0] for p in knot_35_path] + [knot_35_path[0][0]]
    ky = [p[1] for p in knot_35_path] + [knot_35_path[0][1]]
    ax.plot(kx, ky, "c-", linewidth=0.8, alpha=0.8, label="Wire")
    ax.set_title("(3,5) Torus Knot\n(R=12, r=5)", fontsize=11)
    ax.set_xlabel("x")
    ax.legend(fontsize=8)

    # ── Row 2: FFT spectra ──

    # Panel 4: Loop FFT
    ax = axes[1, 0]
    freq = loop_result["fft_freq"]
    power = loop_result["fft_power"]
    ax.plot(freq[1:], power[1:] / np.max(power[1:]), "b-", linewidth=1.5)
    ax.axvline(
        loop_result["f_peak"],
        color="r",
        linestyle="--",
        alpha=0.7,
        label=f"f_peak = {loop_result['f_peak']:.3f}",
    )
    ax.axvline(
        expected_f_loop,
        color="g",
        linestyle=":",
        alpha=0.7,
        label=f"c/(2L) = {expected_f_loop:.3f}",
    )
    ax.set_title("Loop FFT Spectrum", fontsize=11)
    ax.set_xlabel("Normalized Frequency")
    ax.set_ylabel("Power (norm.)")
    ax.legend(fontsize=8)
    ax.set_xlim(0, 0.25)
    ax.grid(True, alpha=0.3)

    # Panel 5: Trefoil FFT
    ax = axes[1, 1]
    freq = trefoil_result["fft_freq"]
    power = trefoil_result["fft_power"]
    ax.plot(freq[1:], power[1:] / np.max(power[1:]), "b-", linewidth=1.5)
    ax.axvline(
        trefoil_result["f_peak"],
        color="r",
        linestyle="--",
        alpha=0.7,
        label=f"f_peak = {trefoil_result['f_peak']:.3f}",
    )
    ax.axvline(
        expected_f_trefoil,
        color="g",
        linestyle=":",
        alpha=0.7,
        label=f"c/(2L) = {expected_f_trefoil:.3f}",
    )
    ax.set_title("(2,3) Trefoil FFT", fontsize=11)
    ax.set_xlabel("Normalized Frequency")
    ax.legend(fontsize=8)
    ax.set_xlim(0, 0.25)
    ax.grid(True, alpha=0.3)

    # Panel 6: (3,5) Knot FFT
    ax = axes[1, 2]
    freq = knot_35_result["fft_freq"]
    power = knot_35_result["fft_power"]
    ax.plot(freq[1:], power[1:] / np.max(power[1:]), "b-", linewidth=1.5)
    ax.axvline(
        knot_35_result["f_peak"],
        color="r",
        linestyle="--",
        alpha=0.7,
        label=f"f_peak = {knot_35_result['f_peak']:.3f}",
    )
    ax.axvline(expected_f_35, color="g", linestyle=":", alpha=0.7, label=f"c/(2L) = {expected_f_35:.3f}")
    ax.set_title("(3,5) Knot FFT", fontsize=11)
    ax.set_xlabel("Normalized Frequency")
    ax.legend(fontsize=8)
    ax.set_xlim(0, 0.25)
    ax.grid(True, alpha=0.3)

    # ── Row 3: Helicity + comparison ──

    # Panel 7: Trefoil helicity density (achiral lattice)
    ax = axes[2, 0]
    h = trefoil_result["helicity"]
    vmax = max(np.max(np.abs(h)), 1e-10)
    im = ax.imshow(h.T, cmap="RdBu_r", origin="lower", vmin=-vmax, vmax=vmax, extent=[0, NX, 0, NY])
    ax.plot(tx, ty, "k-", linewidth=0.5, alpha=0.4)
    ax.set_title("Helicity h (Achiral Lattice)\nTrefoil (2,3)", fontsize=11)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.colorbar(im, ax=ax, shrink=0.8)

    # Panel 8: Trefoil helicity density (chiral lattice)
    ax = axes[2, 1]
    h = trefoil_chiral["helicity"]
    vmax = max(np.max(np.abs(h)), 1e-10)
    im = ax.imshow(h.T, cmap="RdBu_r", origin="lower", vmin=-vmax, vmax=vmax, extent=[0, NX, 0, NY])
    ax.plot(tx, ty, "k-", linewidth=0.5, alpha=0.4)
    ax.set_title("Helicity h (Chiral Lattice)\nTrefoil (2,3)", fontsize=11)
    ax.set_xlabel("x")
    plt.colorbar(im, ax=ax, shrink=0.8)

    # Panel 9: Frequency comparison bar chart
    ax = axes[2, 2]
    labels = ["Loop\n(□)", "(2,3)\nTrefoil", "(3,5)\nKnot"]
    f_peaks = [loop_result["f_peak"], trefoil_result["f_peak"], knot_35_result["f_peak"]]
    f_preds = [expected_f_loop, expected_f_trefoil, expected_f_35]
    wire_lens = [
        loop_result["wire_length"],
        trefoil_result["wire_length"],
        knot_35_result["wire_length"],
    ]

    x_pos = np.arange(3)
    # bars1 = ax.bar(x_pos - 0.15, f_peaks, 0.3, label="FFT Peak", color="#2196F3")  # bulk lint fixup pass
    # bars2 = ax.bar(x_pos + 0.15, f_preds, 0.3, label="c/(2L)", color="#4CAF50", alpha=0.7)  # bulk lint fixup pass
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Normalized Frequency")
    ax.set_title("Resonant Frequency Comparison\nFFT vs c/(2L)", fontsize=11)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3, axis="y")

    # Add wire length annotations
    for i, wl in enumerate(wire_lens):
        ax.annotate(
            f"L={wl}",
            (x_pos[i], max(f_peaks[i], f_preds[i]) + 0.002),
            ha="center",
            fontsize=8,
            color="gray",
        )

    plt.tight_layout(rect=[0, 0, 1, 0.96])

    # Save
    output_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "manuscript", "vol_4_engineering", "figures")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "k4_tlm_phase2_wire_antenna.png")
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"\n  Saved: {output_path}")

    # Summary
    print("\n" + "=" * 70)
    print("  PHASE 2 ANALYSIS COMPLETE")
    print(
        f"  Loop:    L={loop_result['wire_length']},   f_peak={loop_result['f_peak']:.4f},"
        f"  c/(2L)={expected_f_loop:.4f}"
    )
    print(
        f"  Trefoil: L={trefoil_result['wire_length']},  f_peak={trefoil_result['f_peak']:.4f},"
        f"  c/(2L)={expected_f_trefoil:.4f}"
    )
    print(
        f"  (3,5):   L={knot_35_result['wire_length']},  f_peak={knot_35_result['f_peak']:.4f},"
        f"  c/(2L)={expected_f_35:.4f}"
    )
    print(f"  Chiral shift Δf/f: {delta_f / max(trefoil_result['f_peak'], 1e-10):.4e}")
    print(f"  AVE prediction:    {predicted_shift:.4e}")
    print("=" * 70)

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
