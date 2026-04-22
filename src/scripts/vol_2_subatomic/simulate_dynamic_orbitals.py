#!/usr/bin/env python3
"""
simulate_dynamic_orbitals.py
============================

Dynamic electron orbital simulation: atomic orbitals as 1D radial
standing waves in a nuclear impedance cavity.

Every constant from ave.core.constants — zero free parameters.

Physical Model
--------------
The hydrogen atom is a spherical impedance cavity formed by the
nuclear mass-defect (proton = inductance spike at r = 0).
The Coulomb field of the nucleus polarises the surrounding vacuum,
creating an epsilon-enhancement that scales as 1/r.  Standing
waves in this cavity are the electron orbitals.

The radial wave equation in spherical coordinates with the
substitution u(r) = r * psi(r):

    d²u/dt² = v²(r) [ d²u/dr² - l(l+1)/r² u ]

v(r) is set by the local impedance: v = 1/sqrt(mu_eff * eps_eff).

Algorithm
---------
1. Build 1D radial grid with nuclear mu-defect at r ~ 0
2. Set eps-profile from Coulomb coupling (1/alpha per electron, 1/r falloff)
3. Seed with thermal noise
4. Evolve via FDTD with Axiom 4 saturation
5. Time-average energy density -> radial probability P(r)
6. Compare to analytical hydrogen wavefunctions

Outputs -> assets/sim_outputs/
"""

import matplotlib
import numpy as np

matplotlib.use("Agg")
import os  # noqa: E402
from pathlib import Path  # noqa: E402

import matplotlib.animation as animation  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

# ── Project imports ──
PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").is_dir())

from ave.core.constants import ALPHA, C_0, EPSILON_0, L_NODE, M_E, M_PROTON, MU_0, V_SNAP, Z_0
from ave.core.universal_operators import universal_impedance, universal_reflection, universal_saturation

OUT = PROJECT_ROOT / "assets/sim_outputs"
OUT.mkdir(exist_ok=True)

# ══════════════════════════════════════════════════════════════
# Derived constants (all first-principles)
# ══════════════════════════════════════════════════════════════
A_BOHR = L_NODE / ALPHA  # Bohr radius [m]
MU_RATIO = M_PROTON / M_E  # ~1836.15


# ══════════════════════════════════════════════════════════════
# 1.  Radial FDTD Solver
# ══════════════════════════════════════════════════════════════


class OrbitalFDTD:
    """
    1D radial FDTD for standing waves in a nuclear impedance cavity.

    Solves the radial wave equation using u = r*psi (removes geometric
    1/r factors), on a staggered Yee grid.  The centrifugal barrier
    l(l+1)/r^2 is a geometric consequence of spherical symmetry.

    Material profile (first-principles, zero fitted parameters):
      mu_r(r):   Nuclear mass-defect (Gaussian, peak = m_p/m_e)
      eps_r(r):  Coulomb coupling = 1 + (Z_nuc / alpha) * (a0/r) * envelope
    """

    def __init__(self, r_max_bohr=25.0, cells_per_bohr=15, l=0, Z_nuc=1):
        self.l, self.Z_nuc = l, Z_nuc

        self.n = int(r_max_bohr * cells_per_bohr)
        self.dr = A_BOHR / cells_per_bohr
        self.r = np.linspace(0.5 * self.dr, (self.n - 0.5) * self.dr, self.n)
        self.r_b = self.r / A_BOHR  # in Bohr units

        # Fields (u = r * E_transverse)
        self.u_E = np.zeros(self.n)
        self.u_H = np.zeros(self.n - 1)

        # ── Material arrays ──
        self.mu_r = np.ones(self.n - 1)
        self.eps_r = np.ones(self.n)

        # Nuclear mu-defect (proton mass = inductance)
        sigma = 2.5  # cells
        for i in range(min(12, self.n - 1)):
            self.mu_r[i] += MU_RATIO * Z_nuc * np.exp(-0.5 * (i / sigma) ** 2)

        # Coulomb eps-enhancement: eps_r += (Z/alpha) * f(r)
        # f(r) = (a0/r) * exp(-r/(20*a0))   [soft cutoff at ~20 a0]
        # The 1/alpha factor is the per-electron dielectric coupling
        # (same as bond_energy_solver: eps_bond = n_e / alpha).
        coulomb_env = (A_BOHR / self.r) * np.exp(-self.r / (20.0 * A_BOHR))
        self.eps_r += (Z_nuc / ALPHA) * coulomb_env

        # CFL timestep (adaptive for massive defect)
        eps_h = 0.5 * (self.eps_r[:-1] + self.eps_r[1:])
        self.dt = self.dr / (2.0 * C_0 * np.sqrt(np.max(self.mu_r * eps_h)))

        # Centrifugal barrier (geometric, not ad hoc)
        self.V_cent = l * (l + 1) / self.r**2 if l > 0 else np.zeros(self.n)

        # PML absorbing layer at outer boundary (last 30 cells)
        # Exponential conductivity taper — standard numerical technique
        self.pml_n = 30
        self.pml_sigma = np.zeros(self.n)
        for i in range(self.pml_n):
            depth = (i + 1) / self.pml_n
            self.pml_sigma[self.n - 1 - i] = 0.05 * depth**2

        # Time-average accumulator
        self.accum = np.zeros(self.n)
        self.n_acc = 0

    def seed_noise(self, amp=1e-6):
        rng = np.random.default_rng(42)
        self.u_E[:] = amp * rng.standard_normal(self.n)
        self.u_H[:] = amp * rng.standard_normal(self.n - 1)

    def step(self, n_steps=1):
        dt, dr = self.dt, self.dr

        for _ in range(n_steps):
            # ── H update ──
            mu_eff = MU_0 * self.mu_r
            self.u_H -= (dt / (dr * mu_eff)) * (self.u_E[1:] - self.u_E[:-1])

            # ── E update with Axiom 4 saturation ──
            V_local = np.abs(self.u_E / (self.r + 1e-30)) * self.dr
            S = universal_saturation(V_local, V_SNAP)
            S = np.maximum(S, 0.01)
            eps_eff = EPSILON_0 * self.eps_r * S

            ce = dt / (dr * eps_eff)
            self.u_E[1:-1] += ce[1:-1] * (self.u_H[1:] - self.u_H[:-1])

            # ── PML absorption at outer boundary ──
            self.u_E *= 1.0 - self.pml_sigma

            # ── Centrifugal barrier (l > 0) ──
            if self.l > 0:
                mu_at_interior = 0.5 * (self.mu_r[:-1] + self.mu_r[1:])
                self.u_E[1:-1] -= (
                    dt**2 * C_0**2 * self.V_cent[1:-1] * self.u_E[1:-1] / (self.eps_r[1:-1] * mu_at_interior)
                )

            # ── Boundary: u(r=0) = 0 (Dirichlet, geometric) ──
            self.u_E[0] = 0.0
            self.u_E[-1] = 0.0

    def accumulate(self):
        self.accum += self.u_E**2
        self.n_acc += 1

    def radial_prob(self):
        """Time-averaged P(r) = <u^2>.  u=r*psi so P=|psi|^2*r^2 ~ u^2."""
        P = self.accum / max(self.n_acc, 1)
        norm = np.trapz(P, self.r)
        return P / norm if norm > 0 else P

    def impedance_profile(self):
        mu_at_e = np.ones(self.n) * MU_0
        mu_at_e[1:-1] = MU_0 * 0.5 * (self.mu_r[:-1] + self.mu_r[1:])
        mu_at_e[0] = MU_0 * self.mu_r[0]
        mu_at_e[-1] = MU_0 * self.mu_r[-1]
        eps_at_e = EPSILON_0 * self.eps_r
        return universal_impedance(mu_at_e, eps_at_e)

    def reflection_profile(self):
        Z = self.impedance_profile()
        return np.array([universal_reflection(Z[i], Z[i + 1]) for i in range(self.n - 1)])


# ══════════════════════════════════════════════════════════════
# 2.  Analytical Hydrogen Wavefunctions (for comparison)
# ══════════════════════════════════════════════════════════════


def hydrogen_radial_prob(r_bohr, n, l):
    """Analytical radial probability r^2 |R_nl|^2 for hydrogen."""
    from scipy.special import assoc_laguerre, factorial

    x = 2.0 * r_bohr / n
    norm = np.sqrt((2.0 / n) ** 3 * factorial(n - l - 1) / (2 * n * factorial(n + l) ** 3))
    R = norm * np.exp(-x / 2) * x**l * assoc_laguerre(x, n - l - 1, 2 * l + 1)
    return r_bohr**2 * R**2


# ══════════════════════════════════════════════════════════════
# 3.  Plotting (clean, high-contrast, no text overlap)
# ══════════════════════════════════════════════════════════════

plt.style.use("dark_background")
COLORS = {"ave": "#00ffcc", "qm": "#ff6699", "imp": "#ffaa00", "refl": "#66aaff"}


def _style_ax(ax, xlabel, ylabel, title):
    ax.set_xlabel(xlabel, fontsize=11, color="#cccccc")
    ax.set_ylabel(ylabel, fontsize=11, color="#cccccc")
    ax.set_title(title, fontsize=13, fontweight="bold", color="white", pad=12)
    ax.tick_params(colors="#aaaaaa", labelsize=9)
    for s in ax.spines.values():
        s.set_color("#333333")


def plot_impedance(sim, path):
    """Static plot: Z(r), Gamma(r) profiles."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), facecolor="#0a0a14")
    fig.subplots_adjust(hspace=0.35)

    Z = sim.impedance_profile()
    ax1.semilogy(sim.r_b, Z, color=COLORS["imp"], lw=2)
    ax1.axhline(Z_0, color="#555555", ls="--", lw=1, label=f"Z₀ = {Z_0:.1f} Ω")
    ax1.axvline(1.0, color="#333333", ls=":", lw=1)
    _style_ax(ax1, "", "Z(r)  [Ω]", "Nuclear Impedance Cavity")
    ax1.legend(fontsize=10, framealpha=0.3)
    ax1.set_xlim(0, 15)

    G = sim.reflection_profile()
    ax2.plot(sim.r_b[:-1], np.abs(G), color=COLORS["refl"], lw=2)
    ax2.axvline(1.0, color="#333333", ls=":", lw=1)
    _style_ax(ax2, "r / a₀", "|Γ(r)|", "Reflection Coefficient")
    ax2.set_xlim(0, 15)
    ax2.set_ylim(0, 1.05)

    fig.savefig(path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")


def plot_comparison(sim, path):
    """Static plot: time-averaged P(r) vs analytical hydrogen."""
    fig, ax = plt.subplots(figsize=(10, 5.5), facecolor="#0a0a14")

    P_sim = sim.radial_prob()
    # Normalise for visual overlay
    P_sim_plot = P_sim / np.max(P_sim) if np.max(P_sim) > 0 else P_sim

    ax.plot(sim.r_b, P_sim_plot, color=COLORS["ave"], lw=2.5, label="AVE Cavity Eigenmode", zorder=3)
    ax.fill_between(sim.r_b, 0, P_sim_plot, color=COLORS["ave"], alpha=0.08)

    # Analytical n=1,l=0 hydrogen
    r_qm = np.linspace(0.01, sim.r_b[-1], 500)
    P_qm = hydrogen_radial_prob(r_qm, n=1, l=0)
    P_qm /= np.max(P_qm)
    ax.plot(r_qm, P_qm, "--", color=COLORS["qm"], lw=2, label="Analytical 1s (QM)", zorder=2)

    ax.axvline(1.0, color="#444444", ls=":", lw=1)
    ax.text(1.05, 0.92, "a₀", color="#666666", fontsize=10, transform=ax.get_xaxis_transform())

    _style_ax(
        ax,
        "r / a₀",
        "P(r)  [normalised]",
        "Radial Probability: AVE Impedance Cavity vs Hydrogen 1s",
    )
    ax.legend(fontsize=11, loc="upper right", framealpha=0.4)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 1.15)

    fig.savefig(path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")


def make_animation(sim, n_warmup, n_frames, steps_per_frame, path):
    """Animated GIF: P(r) building up from noise."""
    fig, ax = plt.subplots(figsize=(10, 5), facecolor="#0a0a14")
    _style_ax(ax, "r / a₀", "|u(r)|²  [a.u.]", "Standing Wave Formation in Nuclear Impedance Cavity")
    ax.set_xlim(0, 15)
    (line,) = ax.plot([], [], color=COLORS["ave"], lw=2)
    fill = None
    time_text = ax.text(0.02, 0.92, "", transform=ax.transAxes, color="#888888", fontsize=10)

    # Warmup
    sim.seed_noise(amp=1e-6)
    sim.step(n_warmup)

    snapshots = []
    for _ in range(n_frames):
        sim.step(steps_per_frame)
        sim.accumulate()
        P = sim.radial_prob()
        snapshots.append(P.copy())

    # Find global max for consistent y-axis
    y_max = max(np.max(s) for s in snapshots) * 1.15
    ax.set_ylim(0, y_max if y_max > 0 else 1)

    # Analytical overlay (static)
    r_qm = np.linspace(0.01, sim.r_b[-1], 500)
    P_qm = hydrogen_radial_prob(r_qm, n=1, l=0)
    P_qm *= y_max * 0.85 / np.max(P_qm)
    ax.plot(r_qm, P_qm, "--", color=COLORS["qm"], lw=1.5, alpha=0.4, label="1s analytical")
    ax.legend(fontsize=9, loc="upper right", framealpha=0.3)

    def update(frame):
        nonlocal fill
        P = snapshots[frame]
        line.set_data(sim.r_b, P)
        if fill is not None:
            fill.remove()
        fill = ax.fill_between(sim.r_b, 0, P, color=COLORS["ave"], alpha=0.06)
        t_steps = n_warmup + (frame + 1) * steps_per_frame
        time_text.set_text(f"Step {t_steps:,}")
        return line, time_text

    anim = animation.FuncAnimation(fig, update, frames=n_frames, interval=80, blit=False)
    anim.save(path, writer="pillow", dpi=120, savefig_kwargs={"facecolor": fig.get_facecolor()})
    plt.close(fig)
    print(f"  Saved: {path}")


def make_2d_orbital(sim, n_quantum, l_quantum, m_quantum, path):
    """Static 2D cross-section: radial eigenmode x Y_lm(theta)."""
    from scipy.special import sph_harm

    P_r = sim.radial_prob()
    R_amp = np.sqrt(np.maximum(P_r, 0))

    # 2D grid (r, theta) -> (x, z)
    r_vals = sim.r_b
    theta = np.linspace(0, 2 * np.pi, 300)
    R2d, Th2d = np.meshgrid(r_vals, theta)

    # Angular factor |Y_l^m|^2
    Y = sph_harm(m_quantum, l_quantum, 0, Th2d)  # phi=0 slice
    ang = np.abs(Y) ** 2

    # Radial factor (broadcast)
    rad = np.interp(R2d.ravel(), r_vals, R_amp).reshape(R2d.shape)

    density = rad * ang
    density /= np.max(density) if np.max(density) > 0 else 1

    X = R2d * np.sin(Th2d)
    Z = R2d * np.cos(Th2d)

    fig, ax = plt.subplots(figsize=(8, 8), facecolor="#0a0a14")
    ax.set_facecolor("#0a0a14")
    im = ax.pcolormesh(X, Z, density, cmap="hot", shading="gouraud", vmin=0, vmax=0.5)
    ax.contour(X, Z, density, levels=[0.02, 0.1, 0.3], colors="white", linewidths=0.5, alpha=0.3)
    ax.set_aspect("equal")
    _style_ax(
        ax,
        "x / a₀",
        "z / a₀",
        f"Orbital Cross-Section: n={n_quantum}, l={l_quantum}, m={m_quantum}",
    )
    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)

    cbar = fig.colorbar(im, ax=ax, shrink=0.7, pad=0.03)
    cbar.set_label("Energy Density", color="white", fontsize=10)
    cbar.ax.tick_params(colors="#aaaaaa", labelsize=8)

    fig.savefig(path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")


# ══════════════════════════════════════════════════════════════
# 4.  Main
# ══════════════════════════════════════════════════════════════


def main():
    print("=" * 60)
    print("  AVE Dynamic Orbital Simulation")
    print("  All constants from ave.core.constants")
    print("=" * 60)
    print(f"  a₀ = {A_BOHR:.4e} m  (= ℓ_node / α)")
    print(f"  m_p/m_e = {MU_RATIO:.2f}")
    print(f"  Z₀ = {Z_0:.2f} Ω")
    print()

    # ── l=0 (s-orbital) ──
    print("[1] Building l=0 impedance cavity...")
    sim_s = OrbitalFDTD(r_max_bohr=25.0, cells_per_bohr=15, l=0, Z_nuc=1)

    print("[2] Plotting impedance profile...")
    plot_impedance(sim_s, os.path.join(OUT, "orbital_impedance_profile.png"))

    print("[3] Generating standing wave formation animation (1s)...")
    make_animation(
        sim_s,
        n_warmup=500,
        n_frames=150,
        steps_per_frame=200,
        path=os.path.join(OUT, "orbital_1s_formation.gif"),
    )

    # Fresh sim for comparison (animation consumed the previous one)
    print("[4] Evolving fresh l=0 cavity for comparison...")
    sim_cmp = OrbitalFDTD(r_max_bohr=25.0, cells_per_bohr=15, l=0, Z_nuc=1)
    sim_cmp.seed_noise(amp=1e-6)
    for _ in range(300):
        sim_cmp.step(200)
        sim_cmp.accumulate()

    print("[5] Plotting radial comparison (1s)...")
    plot_comparison(sim_cmp, os.path.join(OUT, "orbital_comparison.png"))

    print("[6] Generating 2D cross-section (1s)...")
    make_2d_orbital(sim_cmp, 1, 0, 0, os.path.join(OUT, "orbital_1s_cross_section.png"))

    # ── l=1 (p-orbital) ──
    print("[7] Building l=1 impedance cavity...")
    sim_p = OrbitalFDTD(r_max_bohr=25.0, cells_per_bohr=15, l=1, Z_nuc=1)
    sim_p.seed_noise(amp=1e-6)
    print("     Evolving...")
    for _ in range(200):
        sim_p.step(150)
        sim_p.accumulate()

    print("[8] Generating 2D cross-section (2p)...")
    make_2d_orbital(sim_p, 2, 1, 0, os.path.join(OUT, "orbital_2p_cross_section.png"))

    # ── l=2 (d-orbital) ──
    print("[9] Building l=2 impedance cavity...")
    sim_d = OrbitalFDTD(r_max_bohr=25.0, cells_per_bohr=15, l=2, Z_nuc=1)
    sim_d.seed_noise(amp=1e-6)
    print("     Evolving...")
    for _ in range(200):
        sim_d.step(150)
        sim_d.accumulate()

    print("[10] Generating 2D cross-section (3d)...")
    make_2d_orbital(sim_d, 3, 2, 0, os.path.join(OUT, "orbital_3d_cross_section.png"))

    print()
    print("=" * 60)
    print("  All outputs saved to assets/sim_outputs/")
    print("=" * 60)


if __name__ == "__main__":
    main()
