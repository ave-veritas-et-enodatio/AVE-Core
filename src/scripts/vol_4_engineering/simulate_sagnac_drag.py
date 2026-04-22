import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import os
import pathlib

# Simulation Parameters for the Spacetime Vacuum Ring
N_NODES = 50  # Number of LC nodes in the continuous ring
L_0 = 1e-6  # Baseline Inductance per node (1 uH)
C_0 = 1e-12  # Baseline Capacitance per node (1 pF)

# The Sagnac / Lense-Thirring effect:
# A massive rotating object (like Earth) physically drags the mutual inductive frame of the vacuum.
# This creates a differential inductance for waves travelling with vs against the rotation.
SAGNAC_DRAG = 0.05  # 5% inductive asymmetry (highly exaggerated for visual clarity)


def sagnac_ring_model(y, t):
    """
    Simulates a closed ring of N LC transmission line nodes.
    y contains exactly 2*N elements:
    y[0 : N]   = V_c (Voltages at each node)
    y[N : 2*N] = I_l (Currents between nodes)
    """
    V = y[0:N_NODES]
    I = y[N_NODES : 2 * N_NODES]

    dV_dt = np.zeros(N_NODES)
    dI_dt = np.zeros(N_NODES)

    # Differential Inductance caused by Macroscopic Frame Dragging
    # L_forward (clockwise) = L_0 * (1 - drag)
    # L_backward (counter-clockwise) = L_0 * (1 + drag)
    # Since this is a 1D ring, current flowing + index is forward, - index is backward

    for i in range(N_NODES):
        # Current I[i] flows from node i to node (i+1)%N
        # If I > 0, wave is moving forward. If I < 0, wave is moving backward.

        # Determine directional inductance dynamically based on current flow
        if I[i] > 0:
            L_eff = L_0 * (1.0 - SAGNAC_DRAG)  # Traveling WITH the frame rotation (less drag)
        else:
            L_eff = L_0 * (1.0 + SAGNAC_DRAG)  # Traveling AGAINST the frame rotation (more drag)

        dI_dt[i] = (V[i] - V[(i + 1) % N_NODES]) / L_eff

        # Capacitance node updates based on incoming and outgoing currents
        # I[i-1] flows into node i, I[i] flows out of node i
        dV_dt[i] = (I[(i - 1) % N_NODES] - I[i]) / C_0

    return np.concatenate((dV_dt, dI_dt))


def run_sagnac_sim():
    print("[*] Running Sagnac Inductive Drag SPICE Model...")

    # We want to inject two identical photon packets at node 0
    # One traveling Left (Index N-1), One traveling Right (Index 1)

    t_end = 2.0e-6  # 2 microseconds
    t = np.linspace(0, t_end, 5000)

    y0 = np.zeros(2 * N_NODES)

    # Inject an identical "Photon" voltage spike at the starting nodes
    # Node 1 will propagate clockwise (Forward)
    # Node N-1 will propagate counter-clockwise (Backward)
    # Node 0 is the beam splitter

    y0[1] = 100.0  # 100V spike forward
    y0[N_NODES - 1] = 100.0  # 100V spike backward

    # Initial momentum (current injection)
    # Forward wave gets positive current, backward gets negative
    y0[N_NODES + 1] = 100.0 / np.sqrt(L_0 / C_0)
    y0[N_NODES + N_NODES - 1] = -100.0 / np.sqrt(L_0 / C_0)

    sol = odeint(sagnac_ring_model, y0, t)

    V_nodes = sol[:, 0:N_NODES]

    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.patch.set_facecolor("#0f0f0f")

    for ax in axes:
        ax.set_facecolor("#0f0f0f")
        ax.tick_params(colors="white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        ax.title.set_color("white")
        for spine in ax.spines.values():
            spine.set_color("#333333")

    # The detector is exactly at the opposite side of the ring (Node N/2)
    detector_node = N_NODES // 2

    # Plot 1: Wave Propagation Waterfall
    # Shows the two waves traveling around the ring
    extent = [0, N_NODES, t_end * 1e6, 0]
    # im = axes[0].imshow(V_nodes, aspect="auto", cmap="hot", extent=extent)  # bulk lint fixup pass
    axes[0].set_title("Photon Packet Propagation Through LC Vacuum Ring")
    axes[0].set_xlabel("Spatial LC Node Index")
    axes[0].set_ylabel("Time ($\\mu$s)")
    axes[0].axvline(detector_node, color="white", linestyle="--", linewidth=1, alpha=0.5)
    axes[0].text(detector_node + 1, 0.2, "Interferometer Detector", color="white", rotation=90)

    # Plot 2: The Interferometer readout at the detector (Node N/2)
    # In a standard vacuum, both waves arrive exactly simultaneously.
    # In a phase-dragged vacuum, the forward wave arrives first.
    V_detector = V_nodes[:, detector_node]

    axes[1].plot(t * 1e6, V_detector, color="#00ffcc", linewidth=2.0)
    axes[1].set_title("Detector Readout: Sagnac Arrival Time Phase Shift")
    axes[1].set_xlabel("Time ($\\mu$s)")
    axes[1].set_ylabel("Voltage Amplitude")
    axes[1].grid(True, alpha=0.2)

    # Annotate the two distinct peaks
    axes[1].annotate(
        "Co-rotating Wave\nArrives Early",
        xy=(t[np.argmax(V_detector[:2500])] * 1e6, 40),
        xytext=(0.2, 80),
        arrowprops=dict(facecolor="white", shrink=0.05),
        color="white",
        fontsize=10,
    )

    axes[1].annotate(
        "Counter-rotating Wave\nArrives Late",
        xy=(t[np.argmax(V_detector[2500:]) + 2500] * 1e6, 40),
        xytext=(1.2, 80),
        arrowprops=dict(facecolor="white", shrink=0.05),
        color="white",
        fontsize=10,
    )

    plt.tight_layout()

    project_root = pathlib.Path(str(pathlib.Path(__file__).parent.parent.parent.parent.absolute()))
    outdir = project_root / "spice_manual" / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "sagnac_inductive_drag.png"

    plt.savefig(target, dpi=150, facecolor="#0f0f0f")
    print(f"[*] Visualized Sagnac Effect: {target}")


if __name__ == "__main__":
    run_sagnac_sim()
