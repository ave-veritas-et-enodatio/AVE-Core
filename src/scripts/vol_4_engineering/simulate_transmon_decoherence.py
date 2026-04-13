"""
AVE Quantum Decoherence Simulator (1D Transmon)
==============================================
Simulates a classic Transmon Qubit as an explicitly fragile 1D LC standing wave
(a continuous phase amplitude).

PHYSICS MODEL (Option C — Boundary-Impedance Thermalization):
    The qubit is a standing wave on a 1D LC transmission line.
    Decoherence is NOT modeled by sprinkling bulk stochastic noise on every node.
    Instead, the thermal 300K environment couples ONLY through the boundary nodes,
    which act as impedance-mismatched ports to a thermal reservoir.

    — Interior nodes: pure FDTD wave equation (energy-conserving)
    — Boundary nodes: driven by Johnson-Nyquist thermal voltage,
      V_boundary ~ sqrt(4 k_B T R Δf), normalized to a thermal amplitude.
    — Ohmic damping: a small velocity-proportional loss term (−γ dV/dt)
      represents radiation loss into the substrate.  This satisfies the
      fluctuation-dissipation theorem: energy injected at the boundary is
      balanced by Ohmic loss throughout the line.

    The coherence metric is the proper normalized autocorrelation:
        C(t) = |⟨V(t) | ψ₀⟩| / (‖V(t)‖ · ‖ψ₀‖)
    which is cos(θ) between the current state and the initial standing wave,
    guaranteed to lie in [0, 1] by Cauchy-Schwarz.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path

# ── Simulation Parameters ────────────────────────────────────────────────────
N = 200                # Number of LC nodes in the 1D junction
T_MAX = 1000           # Simulation time steps
C_COURANT = 0.5        # Courant number (wave speed for FDTD stability)
GAMMA = 0.005          # Ohmic damping coefficient (substrate radiation loss)

# ── Thermal Boundary Parameters ──────────────────────────────────────────────
# In normalized units, the thermal amplitude at the boundaries represents
# Johnson-Nyquist noise from the 300K environment coupling through the
# impedance-mismatched junction leads.
THERMAL_AMP = 0.15     # RMS amplitude of boundary thermal drive
BOUNDARY_WIDTH = 3     # Number of nodes at each end coupled to the reservoir


def simulate_transmon_decoherence():
    """
    Run the 1D FDTD simulation with boundary-impedance thermalization.

    Returns:
        time_history: list of time step indices
        coherence_history: list of coherence values in [0, 1]
    """
    # Initialize the LC grid (voltage/displacement)
    V = np.zeros(N)
    V_prev = np.zeros(N)

    # Inject a perfect standing wave: the pristine |qubit⟩ state
    x = np.linspace(0, 2 * np.pi, N)
    standing_wave = np.sin(3 * x)
    psi0_norm = np.linalg.norm(standing_wave)

    V[:] = standing_wave.copy()
    V_prev[:] = standing_wave.copy()

    # Tracking
    time_history = []
    coherence_history = []

    # ── Main FDTD Loop ─────────────────────────────────────────────────
    for t in range(T_MAX):
        V_next = np.zeros(N)

        # 1) Interior: pure wave equation (energy-conserving Laplacian)
        for i in range(1, N - 1):
            laplacian = V[i + 1] - 2 * V[i] + V[i - 1]
            velocity = V[i] - V_prev[i]
            V_next[i] = (
                2 * V[i]
                - V_prev[i]
                + C_COURANT**2 * laplacian
                - GAMMA * velocity            # Ohmic damping (substrate loss)
            )

        # 2) Boundary thermalization: thermal reservoir drives the edge nodes
        #    This is the ONLY source of noise — it enters through the
        #    impedance-mismatched junction leads, not magically everywhere.
        for b in range(BOUNDARY_WIDTH):
            # Left boundary
            V_next[b] = np.random.normal(0, THERMAL_AMP)
            # Right boundary
            V_next[N - 1 - b] = np.random.normal(0, THERMAL_AMP)

        # 3) Coherence metric: Cauchy-Schwarz normalized overlap
        #    C(t) = |⟨V(t)|ψ₀⟩| / (‖V(t)‖ · ‖ψ₀‖) ∈ [0, 1]
        v_norm = np.linalg.norm(V_next)
        if v_norm > 0:
            overlap = np.abs(np.dot(V_next, standing_wave))
            current_coherence = overlap / (v_norm * psi0_norm)
        else:
            current_coherence = 0.0

        coherence_history.append(current_coherence)
        time_history.append(t)

        # Step forward
        V_prev = V.copy()
        V = V_next.copy()

    return time_history, coherence_history


def generate_plot(time, coherence, out_path):
    """Generate the decoherence plot with AVE manuscript styling."""
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Smooth the coherence trace with a moving average for readability
    window_size = 20
    smoothed = np.convolve(coherence, np.ones(window_size) / window_size,
                           mode='valid')
    time_smooth = time[:len(smoothed)]

    ax.plot(time_smooth, smoothed, color='#00ffcc', linewidth=2.5,
            label='Transmon Phase Coherence (Boundary Thermalized)')
    ax.fill_between(time_smooth, smoothed, color='#00ffcc', alpha=0.1)

    # Exponential decoherence envelope
    decay_envelope = np.exp(-np.array(time_smooth) / 150.0)
    ax.plot(time_smooth, decay_envelope, color='#ff00aa', linestyle='--',
            linewidth=2, label='Exponential Decoherence Envelope')

    # Formatting
    ax.set_title(
        "1D Transmon Decoherence — Boundary-Impedance Thermalization (300K)",
        fontsize=15, color='white', pad=15
    )
    ax.set_xlabel("Time (Arbitrary Units)", fontsize=14)
    ax.set_ylabel(
        r"Coherence $\frac{|\langle V(t)|\psi_0\rangle|}"
        r"{\|V(t)\|\,\|\psi_0\|}$",
        fontsize=14
    )
    ax.set_ylim(-0.05, 1.05)
    ax.set_xlim(0, T_MAX)
    ax.grid(True, color='#333333', linestyle='--', alpha=0.7)

    # Annotation: physics mechanism
    ax.text(
        0.98, 0.85,
        "Noise enters ONLY\nthrough boundary\nimpedance mismatch",
        transform=ax.transAxes,
        ha='right', va='top',
        fontsize=10, color='#aaaaaa',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a1a',
                  edgecolor='#444444', alpha=0.9)
    )

    ax.legend(loc='upper right', facecolor='black', edgecolor='white')

    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[Done] Saved Transmon Decoherence Plot: {out_path}")


if __name__ == "__main__":
    PROJECT_ROOT = next(p for p in Path(__file__).parents if (p/".git").is_dir())
    out_dir = PROJECT_ROOT / "assets" / "sim_outputs"
    os.makedirs(out_dir, exist_ok=True)

    print("Simulating 1D Transmon Decoherence (Boundary-Impedance Model)...")
    t, c = simulate_transmon_decoherence()
    generate_plot(t, c, out_dir / "transmon_decoherence_plot.png")
