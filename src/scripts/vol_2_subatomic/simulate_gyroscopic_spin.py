import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import os

# Physical parameters (normalized for visual clarity)
GAMMA = 1.0  # Gyromagnetic ratio
B0 = 2.0  # Static B-field in Z
B1 = 0.2  # RF pulse amplitude in X-Y plane
W_RF = GAMMA * B0  # Resonant RF frequency (Larmor Frequency)

# Duration to execute a pi-pulse (flip angle = pi)
OMEGA_RABI = GAMMA * B1
t_pi = np.pi / OMEGA_RABI

# Time array
t_span = (0, t_pi)
t_eval = np.linspace(0, t_pi, 1000)


def b_field(t):
    """External dynamic magnetic field combining B0 and circularly polarized B1"""
    return np.array([B1 * np.cos(W_RF * t), B1 * np.sin(W_RF * t), B0])


# ---------------------------------------------------------
# 1. CLASSICAL GYROSCOPE ODE
# dL/dt = gamma * L x B
# ---------------------------------------------------------
def classical_gyroscope_deriv(t, L):
    B = b_field(t)
    return GAMMA * np.cross(L, B)


# ---------------------------------------------------------
# 2. QUANTUM SCHRODINGER ODE (SU(2) Spinor)
# i * d|psi>/dt = H |psi>
# ---------------------------------------------------------
sig_x = np.array([[0, 1], [1, 0]], dtype=complex)
sig_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
sig_z = np.array([[1, 0], [0, -1]], dtype=complex)


def quantum_spinor_deriv(t, y):
    c0 = y[0] + 1j * y[1]
    c1 = y[2] + 1j * y[3]
    psi = np.array([c0, c1])

    B = b_field(t)
    H = -0.5 * GAMMA * (B[0] * sig_x + B[1] * sig_y + B[2] * sig_z)
    dpsi = -1j * np.dot(H, psi)

    return [dpsi[0].real, dpsi[0].imag, dpsi[1].real, dpsi[1].imag]


def main():
    print("Simulating Classical Gyroscopic Precession...")
    L0 = np.array([0.0, 0.0, 1.0])
    res_class = solve_ivp(classical_gyroscope_deriv, t_span, L0, t_eval=t_eval, rtol=1e-8, atol=1e-8)
    L_x, L_y, L_z = res_class.y

    print("Simulating Quantum Dirac Spinor (Hilbert Space)...")
    c0_init = 1.0 + 0j
    c1_init = 0.0 + 0j
    y0_q = [c0_init.real, c0_init.imag, c1_init.real, c1_init.imag]
    res_quant = solve_ivp(quantum_spinor_deriv, t_span, y0_q, t_eval=t_eval, rtol=1e-8, atol=1e-8)

    # Project complex spinor into Bloch Sphere Cartesian expectations
    c0 = res_quant.y[0] + 1j * res_quant.y[1]
    c1 = res_quant.y[2] + 1j * res_quant.y[3]

    S_x = (np.conj(c0) * c1 + np.conj(c1) * c0).real
    S_y = (-1j * np.conj(c0) * c1 + 1j * np.conj(c1) * c0).real
    S_z = np.abs(c0) ** 2 - np.abs(c1) ** 2

    # Verify zero mathematical delta
    error = np.max(np.abs(L_z - S_z))
    print(f"Maximum Deviation between Classical and Quantum models: {error:.2e}")

    print("Generating High-Fidelity Multi-Panel Visualization...")
    fig = plt.figure(figsize=(16, 12))
    gs = plt.GridSpec(2, 2, height_ratios=[1.5, 1])

    # ==========================================
    # Helper for 3D trajectory
    # ==========================================
    def plot_sphere(ax, title, color_line, x_data, y_data, z_data):
        ax.set_title(title, fontsize=16, pad=10, fontweight="bold")
        # Wireframe sphere
        u = np.linspace(0, 2 * np.pi, 25)
        v = np.linspace(0, np.pi, 25)
        x_sph = np.outer(np.cos(u), np.sin(v))
        y_sph = np.outer(np.sin(u), np.sin(v))
        z_sph = np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_wireframe(x_sph, y_sph, z_sph, color="black", alpha=0.04)

        # Axes
        ax.plot([-1.2, 1.2], [0, 0], [0, 0], color="gray", linestyle="-.", lw=1)
        ax.plot([0, 0], [-1.2, 1.2], [0, 0], color="gray", linestyle="-.", lw=1)
        ax.plot([0, 0], [0, 0], [-1.2, 1.2], color="gray", linestyle="-.", lw=1)

        # Plot continuous trace
        ax.plot(x_data, y_data, z_data, color=color_line, lw=1.5, alpha=0.6, label="Trajectory Trace")

        # Plot a few explicit vectors over time
        for idx in [0, len(x_data) // 4, len(x_data) // 2, 3 * len(x_data) // 4, -1]:
            ax.quiver(
                0,
                0,
                0,
                x_data[idx],
                y_data[idx],
                z_data[idx],
                color=color_line,
                alpha=0.9,
                arrow_length_ratio=0.1,
                lw=3,
            )

        ax.set_xlim([-1.2, 1.2])
        ax.set_ylim([-1.2, 1.2])
        ax.set_zlim([-1.2, 1.2])
        ax.set_xlabel("X (Precession Plane)")
        ax.set_ylabel("Y (Precession Plane)")
        ax.set_zlabel("Z (Spin Axis)")
        ax.set_box_aspect([1, 1, 1])
        ax.view_init(elev=15, azim=60)

    # Top Left: 3D Quantum Field
    ax1 = fig.add_subplot(gs[0, 0], projection="3d")
    plot_sphere(
        ax1,
        "Quantum Dirac Spinor\n(Bloch Sphere $|\psi\\rangle$ Expectation)",
        "royalblue",
        S_x,
        S_y,
        S_z,
    )

    # Top Right: 3D Classical Gyroscope
    ax2 = fig.add_subplot(gs[0, 1], projection="3d")
    plot_sphere(
        ax2,
        "Classical Macro-Gyroscope\n(Mechanical $3_1$ Defect Precession)",
        "darkorange",
        L_x,
        L_y,
        L_z,
    )

    # ==========================================
    # Bottom Left: Z-Axis Time Series (Spin Flip)
    # ==========================================
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.set_title("Time-Domain Verification: $Z$-Axis Spin Flipping", fontsize=14)
    ax3.plot(t_eval, S_z, color="royalblue", lw=6, alpha=0.4, label="Quantum $\\langle S_z \\rangle$")
    ax3.plot(t_eval, L_z, color="darkorange", lw=2, linestyle="--", label="Classical $L_z$")
    ax3.set_xlabel("Time (s)")
    ax3.set_ylabel("Z Projection (Spin State)")
    ax3.grid(True, alpha=0.3)
    ax3.legend(loc="upper right")

    # ==========================================
    # Bottom Right: XY Plane Precession
    # ==========================================
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.set_title("Time-Domain Verification: $XY$-Axis Larmor Resonance", fontsize=14)
    ax4.plot(t_eval, S_x, color="royalblue", lw=4, alpha=0.3, label="Quantum $\\langle S_x \\rangle$")
    ax4.plot(t_eval, L_x, color="darkorange", lw=1.5, linestyle="--", label="Classical $L_x$")
    ax4.plot(t_eval, S_y, color="purple", lw=4, alpha=0.3, label="Quantum $\\langle S_y \\rangle$")
    ax4.plot(t_eval, L_y, color="red", lw=1.5, linestyle="--", label="Classical $L_y$")
    ax4.set_xlabel("Time (s)")
    ax4.set_ylabel("Transverse Projection")
    ax4.grid(True, alpha=0.3)
    ax4.legend(loc="upper right", ncol=2)

    plt.tight_layout()

    # Save output
    os.makedirs("assets/sim_outputs", exist_ok=True)
    out_path = "assets/sim_outputs/quantum_spin_gyroscopic_precession.png"
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    print(f"Saved artifact successfully to: {out_path}")


if __name__ == "__main__":
    main()
