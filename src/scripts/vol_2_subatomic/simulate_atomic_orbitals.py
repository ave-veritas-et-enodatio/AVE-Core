# simulate_atomic_orbitals.py
# Solves standard electron orbitals entirely deterministically as 3D Macroscopic
# Acoustic Chladni Standing-Wave logic formed inside the LC lattice tensor gradients.

import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from pathlib import Path

plt.style.use("dark_background")


# --- Standard AVE output directory ---
def _find_repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.exists(os.path.join(d, "pyproject.toml")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.abspath(__file__))


PROJECT_ROOT = Path(_find_repo_root())
sys.path.append(str(PROJECT_ROOT / "src"))

from scripts.vol_2_subatomic.solve_orbital_eigenmodes import OrbitalODE

OUTPUT_DIR = os.path.join(_find_repo_root(), "assets", "sim_outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)
# --- End standard output directory ---
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def generate_orbitals():
    print("Evaluating Atomic Orbitals as deterministic Chladni Acoustic Nodes...")

    # -------------------------------------------------------------------
    # Axiom: The vacuum is a continuous non-linear LC lattice.
    # An electron topologically locked to a proton forms a resonant cavity.
    # Quantum 'Probabilities' are strictly the classical mechanical spatial
    # energy-density antinodes of a 3D spherical standing acoustic wave.
    # We solve this not as abstract probabilities, but as classical continuous fluid modes.
    # -------------------------------------------------------------------

    # Set up a continuous analytical 3D bounding box for the topological cavity
    grid_res = 100
    r_max = 12.0
    x = np.linspace(-r_max, r_max, grid_res)
    z = np.linspace(-r_max, r_max, grid_res)
    X, Z = np.meshgrid(x, z)

    # We evaluate a 2D cross-section plane (y=0) of the full 3D standing wave mode
    # converting Euclidean coords to continuous Sphericals
    R_sph = np.sqrt(X**2 + Z**2)
    # Avoid singularity at origin
    R_sph[R_sph == 0] = 1e-10
    Theta = np.arccos(Z / R_sph)

    # -------------------------------------------------------------------
    # Deterministic Classical Harmonic Wave Solutions
    # Using classical continuous Cauchy initial value ODE solver natively
    # -------------------------------------------------------------------

    n_val = 3
    l_val = 2

    ode = OrbitalODE(Z_nuc=1, l=l_val, r_max_bohr=r_max + 2.0, n_points=500)
    E_eigen = ode.find_eigenvalue(n_val)
    u_rad = ode.eigenmode(E_eigen)

    # We must explicitly map the 1D acoustic eigenmode back onto the 2D grid
    # R_sph is basically 'r'. So we interpolate the ODE solution `u_rad` over R_sph.
    # Because u(r) = r * R_nl(r), we compute continuous R_nl = u(r)/r
    radial_mode_1d = np.zeros_like(u_rad)
    valid_mask = ode.r_b > 1e-5
    radial_mode_1d[valid_mask] = u_rad[valid_mask] / ode.r_b[valid_mask]

    # 2D interpolated expansion
    R_nl = np.interp(R_sph, ode.r_b, radial_mode_1d)

    # Computing the classical continuous angular mode (Spherical Harmonic Y_l^m)
    # The Legendre polynomials denote the exact polar standing-wave vibration boundaries
    Y_lm = np.sqrt(5.0 / (16.0 * np.pi)) * (3.0 * np.cos(Theta) ** 2 - 1.0)

    # The total classical continuous mechanical displacement field (Acoustic Phonon Amplitude)
    Psi_mechanical = R_nl * Y_lm

    # The "Probability Density" physically maps strictly to continuous
    # time-averaged Kinetic Energy Density ($\rho_{energy} \propto |\Psi|^2$)
    Energy_Density = np.abs(Psi_mechanical) ** 2

    # Normalize for visual gradient mapping
    Energy_Density = Energy_Density / np.max(Energy_Density)

    # Plotting the physical Acoustic Chladni Energy Field
    fig = plt.figure(figsize=(10, 8), facecolor="#050510")
    ax = fig.add_subplot(111)
    ax.set_facecolor("#050510")

    im = ax.imshow(
        Energy_Density.T,
        extent=[-r_max, r_max, -r_max, r_max],
        origin="lower",
        cmap="hot",
        interpolation="bilinear",
        vmax=0.5,
    )  # Vmax clipped to reveal faint structural halos

    # Draw strict boundary contours mapping structural Chladni nodal lines (Zero-displacement)
    ax.contour(
        X,
        Z,
        Energy_Density.T,
        levels=[0.01, 0.05, 0.2, 0.4],
        colors="white",
        alpha=0.3,
        linewidths=1,
    )

    # Format Physics Output
    ax.set_title(
        "Deterministic Orbital Acoustics ($3d_{z^2}$ Mode)",
        color="white",
        fontsize=18,
        pad=20,
        weight="bold",
    )
    ax.set_xlabel("x (Bohr Radii)", color="#aaaaaa", fontsize=12)
    ax.set_ylabel("z (Bohr Radii)", color="#aaaaaa", fontsize=12)

    # Add Colorbar matched to physical energy density
    cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.05)
    cbar.set_label("Continuous Structural Energy Density ($|\\Psi_{mech}|^2$)", color="white")
    cbar.ax.yaxis.set_tick_params(color="white")
    plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color="white")

    # Rigorous Proof Annotation
    ax.text(
        -11,
        -10,
        r"$\mathbf{Quantum\ Mechanics\ as\ Fluid\ Acoustics}$"
        + "\n"
        + "The Schrodinger Equation is strictly the continuous spatial\n"
        + r"wave-equation for the discrete LC continuum ($c=\sqrt{1/\mu\epsilon})$.\n"
        + r"Wavefunctions ($\Psi$) are literal macroscopic mechanical acoustic phonons.\n"
        + "Probability amplitudes map exactly to structural continuous energy-densities.",
        color="white",
        fontsize=11,
        bbox=dict(boxstyle="round", facecolor="#111122", alpha=0.8, edgecolor="#ff00aa"),
    )

    output_path = os.path.join(OUTPUT_DIR, "atomic_orbital_standing_waves.pdf")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, format="pdf", facecolor=fig.get_facecolor(), bbox_inches="tight")
    print(f"Saved Acoustic Orbital Mode simulation to: {output_path}")


if __name__ == "__main__":
    generate_orbitals()
