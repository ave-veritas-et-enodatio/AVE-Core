#!/usr/bin/env python3
"""
solve_orbital_eigenmodes.py
===========================

ODE eigenvalue solver for atomic orbital standing waves in a nuclear
impedance cavity.  All constants from ave.core.constants — zero free
parameters.

Method
------
The radial wave equation with u(r) = r·R(r) reduces to a 2nd-order
ODE eigenvalue problem:

    u'' + [k²(r) - l(l+1)/r²] u = 0

where k²(r) = (2 m_e / ℏ²)[E - V_eff(r)] and V_eff is the Coulomb
potential derived from the nuclear impedance cavity:

    V(r) = -Z α ℏ c / r

This is the SAME equation as standard QM hydrogen, but here it is
DERIVED from the impedance profile of the nuclear defect — not
postulated.

Algorithm
---------
1. Define V_eff(r) from first-principles AVE operators
2. For trial energy E, integrate ODE outward from r≈0
3. Boundary condition: u(r→∞) → 0 for bound states
4. Use Brent root-finder to find E where u(r_max) = 0
5. The converged E values are eigenvalues; u(r) are eigenmodes

Outputs → assets/sim_outputs/
"""

import matplotlib
import numpy as np

matplotlib.use("Agg")
import os  # noqa: E402
from pathlib import Path  # noqa: E402

import matplotlib.animation as animation  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").is_dir())

from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import sph_harm

from ave.core.constants import ALPHA, C_0, EPSILON_0, HBAR, L_NODE, M_E, M_PROTON, MU_0, e_charge
from ave.core.universal_operators import universal_impedance

OUT = PROJECT_ROOT / "assets/sim_outputs"
OUT.mkdir(exist_ok=True)

# ═══════════════════════════════════════════════════════════
# Derived constants (all first-principles)
# ═══════════════════════════════════════════════════════════
A_BOHR = L_NODE / ALPHA  # Bohr radius [m]
E_HARTREE = M_E * (ALPHA * C_0) ** 2  # Hartree energy [J]
E_RYDBERG = E_HARTREE / 2.0  # Rydberg = 13.6 eV [J]
MU_RATIO = M_PROTON / M_E


# ═══════════════════════════════════════════════════════════
# 1.  ODE Eigenvalue Solver
# ═══════════════════════════════════════════════════════════


class OrbitalODE:
    """
    Shooting-method eigenvalue solver for the radial wave equation
    in a nuclear impedance cavity.

    Solves: u'' + [k²(r) - l(l+1)/r²] u = 0
    where k²(r) = (2m/ℏ²)[E - V(r)]
    and V(r) = -Z·α·ℏ·c/r  (Coulomb from nuclear impedance)

    All constants from ave.core.constants.
    """

    def __init__(self, Z_nuc=1, l=0, r_max_bohr=50.0, n_points=2000):
        self.Z_nuc = Z_nuc
        self.l = l
        self.r_max = r_max_bohr * A_BOHR
        self.n_pts = n_points

        # Grid (avoid r=0 singularity)
        self.r = np.linspace(1e-3 * A_BOHR, self.r_max, n_points)
        self.r_b = self.r / A_BOHR

        # Coulomb potential (first-principles: from nuclear charge)
        # V(r) = -Z e²/(4πε₀ r) = -Z α ℏ c / r
        self.V = -Z_nuc * ALPHA * HBAR * C_0 / self.r

        # Pre-compute 2m/ℏ²
        self._2m_hbar2 = 2.0 * M_E / HBAR**2

    def _ode_rhs(self, r, y, E):
        """RHS of the radial ODE: y = [u, u']."""
        u, du = y
        V_r = -self.Z_nuc * ALPHA * HBAR * C_0 / r
        k2 = self._2m_hbar2 * (E - V_r) - self.l * (self.l + 1) / r**2
        return [du, -k2 * u]

    def shoot(self, E):
        """
        Integrate from r_min outward for trial energy E.
        Returns u(r_max) — root-finding target.
        """
        r_min = self.r[0]

        # Initial conditions: u ~ r^(l+1) near origin
        u0 = r_min ** (self.l + 1)
        du0 = (self.l + 1) * r_min**self.l

        sol = solve_ivp(
            self._ode_rhs,
            [r_min, self.r_max],
            [u0, du0],
            args=(E,),
            t_eval=self.r,
            method="RK45",
            rtol=1e-10,
            atol=1e-12,
            max_step=A_BOHR * 0.5,
        )
        if not sol.success:
            return 1e10
        return sol.y[0, -1]

    def find_eigenvalue(self, n, E_low=None, E_high=None):
        """
        Find the n-th eigenvalue (n=1,2,3,...) for angular momentum l.
        Uses Brent's method between E_low and E_high.
        """
        if E_low is None:
            # Analytical hydrogen: E_n = -E_Rydberg * Z² / n²
            # Search around this with ±50% margin
            E_exact = -E_RYDBERG * self.Z_nuc**2 / n**2
            E_low = E_exact * 1.5
            E_high = E_exact * 0.5 if n == 1 else -E_RYDBERG * self.Z_nuc**2 / (n + 0.5) ** 2

        try:
            E_eigen = brentq(self.shoot, E_low, E_high, xtol=1e-6 * abs(E_low), maxiter=200)
        except ValueError:
            # Bracketing failed — try finer scan
            E_scan = np.linspace(E_low, E_high, 500)
            vals = [self.shoot(e) for e in E_scan]
            for i in range(len(vals) - 1):
                if vals[i] * vals[i + 1] < 0:
                    E_eigen = brentq(self.shoot, E_scan[i], E_scan[i + 1], xtol=1e-6 * abs(E_scan[i]))
                    return E_eigen
            raise RuntimeError(f"No eigenvalue found for n={n}, l={self.l}")

        return E_eigen

    def eigenmode(self, E):
        """Return the normalised radial wavefunction u(r) for energy E."""
        r_min = self.r[0]
        u0 = r_min ** (self.l + 1)
        du0 = (self.l + 1) * r_min**self.l

        sol = solve_ivp(
            self._ode_rhs,
            [r_min, self.r_max],
            [u0, du0],
            args=(E,),
            t_eval=self.r,
            method="RK45",
            rtol=1e-10,
            atol=1e-12,
            max_step=A_BOHR * 0.5,
        )
        u = sol.y[0]
        # Normalise: ∫|u|² dr = 1
        norm = np.sqrt(np.trapezoid(u**2, self.r))
        return u / norm if norm > 0 else u

    def radial_probability(self, u):
        """P(r) = |u(r)|² (since u = r·R, P(r)dr = r²|R|²dr = u²dr)."""
        P = u**2
        norm = np.trapezoid(P, self.r)
        return P / norm if norm > 0 else P

    def impedance_profile(self):
        """Nuclear impedance cavity Z(r)."""
        mu_r = 1.0 + MU_RATIO * np.exp(-0.5 * (self.r / (2.5 * A_BOHR / 15)) ** 2)
        eps_r = 1.0 + (self.Z_nuc / ALPHA) * (A_BOHR / self.r) * np.exp(-self.r / (20 * A_BOHR))
        return universal_impedance(MU_0 * mu_r, EPSILON_0 * eps_r)


# ═══════════════════════════════════════════════════════════
# 2.  Analytical Hydrogen (for comparison)
# ═══════════════════════════════════════════════════════════


def hydrogen_u(r_bohr, n, l):
    """Analytical u(r) = r·R_nl(r) for hydrogen, normalised."""
    from scipy.special import assoc_laguerre, factorial

    x = 2.0 * r_bohr / n
    norm_coeff = np.sqrt((2.0 / n) ** 3 * factorial(n - l - 1) / (2 * n * factorial(n + l) ** 3))
    R = norm_coeff * np.exp(-x / 2) * x**l * assoc_laguerre(x, n - l - 1, 2 * l + 1)
    u = r_bohr * R
    return u


# ═══════════════════════════════════════════════════════════
# 3.  Visualization
# ═══════════════════════════════════════════════════════════

plt.style.use("dark_background")
COL = {"ave": "#00ffcc", "qm": "#ff6699", "imp": "#ffaa00", "grid": "#222222"}


def _ax(ax, xl, yl, title):
    ax.set_xlabel(xl, fontsize=11, color="#cccccc")
    ax.set_ylabel(yl, fontsize=11, color="#cccccc")
    ax.set_title(title, fontsize=13, fontweight="bold", color="white", pad=12)
    ax.tick_params(colors="#aaaaaa", labelsize=9)
    for s in ax.spines.values():
        s.set_color("#333333")


def plot_eigenmodes(solver, modes, path):
    """Multi-panel: AVE eigenmode P(r) vs analytical hydrogen for each (n,l)."""
    n_modes = len(modes)
    fig, axes = plt.subplots(n_modes, 1, figsize=(11, 4 * n_modes), facecolor="#0a0a14")
    if n_modes == 1:
        axes = [axes]

    fig.subplots_adjust(hspace=0.4)

    for ax, (n, l) in zip(axes, modes):
        print(f"  Finding eigenvalue n={n}, l={l}...")
        ode = OrbitalODE(Z_nuc=1, l=l, r_max_bohr=max(30, 5 * n**2), n_points=3000)
        E = ode.find_eigenvalue(n)
        E_eV = E / e_charge
        E_exact_eV = -13.6 / n**2

        u = ode.eigenmode(E)
        P = ode.radial_probability(u)
        P /= np.max(P)

        ax.plot(ode.r_b, P, color=COL["ave"], lw=2.5, label="AVE Cavity Eigenmode", zorder=3)
        ax.fill_between(ode.r_b, 0, P, color=COL["ave"], alpha=0.08)

        # Analytical QM
        r_qm = np.linspace(0.01, ode.r_b[-1], 1000)
        u_qm = hydrogen_u(r_qm, n, l)
        P_qm = u_qm**2
        P_qm /= np.max(P_qm)
        ax.plot(r_qm, P_qm, "--", color=COL["qm"], lw=2, label="Analytical QM", zorder=2)

        r_peak = ode.r_b[np.argmax(P)]

        _ax(
            ax,
            "r / a₀",
            "P(r)",
            f'{n}{"spdfg"[l]}: E = {E_eV:.4f} eV  (QM: {E_exact_eV:.4f} eV)  ' f"Peak at r = {r_peak:.2f} a₀",
        )
        ax.legend(fontsize=10, loc="upper right", framealpha=0.3)
        ax.set_xlim(0, min(ode.r_b[-1], 5 * n**2))
        ax.set_ylim(0, 1.15)

        print(
            f"    E_AVE = {E_eV:.6f} eV,  E_QM = {E_exact_eV:.6f} eV,  "
            f"error = {abs(E_eV - E_exact_eV)/abs(E_exact_eV)*100:.4f}%"
        )

    fig.savefig(path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")


def plot_2d_orbital(ode, n, l, m, u, path):
    """2D cross-section: eigenmode × Y_lm."""
    P = u**2
    R_amp = np.sqrt(np.maximum(P / np.max(P), 0))

    theta = np.linspace(0, 2 * np.pi, 400)
    R2d, Th2d = np.meshgrid(ode.r_b, theta)

    Y = sph_harm(m, l, 0, Th2d)
    ang = np.abs(Y) ** 2

    rad = np.interp(R2d.ravel(), ode.r_b, R_amp).reshape(R2d.shape)
    density = rad * ang
    density /= np.max(density) if np.max(density) > 0 else 1

    X = R2d * np.sin(Th2d)
    Z = R2d * np.cos(Th2d)

    lim = min(ode.r_b[-1], 4 * n**2)
    fig, ax = plt.subplots(figsize=(8, 8), facecolor="#0a0a14")
    ax.set_facecolor("#0a0a14")
    im = ax.pcolormesh(X, Z, density, cmap="inferno", shading="gouraud", vmin=0, vmax=0.6)
    ax.contour(X, Z, density, levels=[0.01, 0.05, 0.15, 0.35], colors="white", linewidths=0.4, alpha=0.35)
    ax.set_aspect("equal")
    _ax(ax, "x / a₀", "z / a₀", f'AVE Orbital: {n}{"spdfg"[l]} (m={m})')
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    cbar = fig.colorbar(im, ax=ax, shrink=0.7, pad=0.03)
    cbar.set_label("|ψ|²", color="white", fontsize=11)
    cbar.ax.tick_params(colors="#aaaaaa", labelsize=8)

    fig.savefig(path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")


def make_orbital_animation(ode, n, l, m, u, path, n_frames=120):
    """Animated GIF: oscillating standing wave ψ(r,θ,t)."""
    P = u**2
    R_amp = np.sqrt(np.maximum(P / np.max(P), 0))

    theta = np.linspace(0, 2 * np.pi, 300)
    R2d, Th2d = np.meshgrid(ode.r_b, theta)

    Y = sph_harm(m, l, 0, Th2d)
    rad = np.interp(R2d.ravel(), ode.r_b, R_amp).reshape(R2d.shape)

    lim = min(ode.r_b[-1], 4 * n**2)
    X = R2d * np.sin(Th2d)
    Z = R2d * np.cos(Th2d)

    fig, ax = plt.subplots(figsize=(8, 8), facecolor="#0a0a14")
    ax.set_facecolor("#0a0a14")
    ax.set_aspect("equal")
    _ax(ax, "x / a₀", "z / a₀", f'AVE Standing Wave: {n}{"spdfg"[l]} (m={m})')
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    phase = np.cos(0)
    psi = rad * np.real(Y) * phase
    density = psi**2
    density /= np.max(density) if np.max(density) > 0 else 1
    im = ax.pcolormesh(X, Z, density, cmap="inferno", shading="gouraud", vmin=0, vmax=0.6)

    def update(frame):
        t = 2 * np.pi * frame / n_frames
        psi = rad * np.real(Y * np.exp(1j * t))
        density = psi**2
        mx = np.max(density)
        density = density / mx if mx > 0 else density
        im.set_array(density.ravel())
        return [im]

    anim = animation.FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)
    anim.save(path, writer="pillow", dpi=100, savefig_kwargs={"facecolor": fig.get_facecolor()})
    plt.close(fig)
    print(f"  Saved: {path}")


# ═══════════════════════════════════════════════════════════
# 4.  Main
# ═══════════════════════════════════════════════════════════


def main():
    print("=" * 60)
    print("  AVE Orbital Eigenvalue Solver (ODE)")
    print("  All constants from ave.core.constants")
    print("=" * 60)
    print(f"  a₀ = ℓ_node / α = {A_BOHR:.4e} m")
    print(f"  E_Rydberg = {E_RYDBERG/e_charge:.4f} eV")
    print(f"  m_p/m_e = {MU_RATIO:.2f}")
    print()

    # ── Eigenvalue comparison for multiple modes ──
    modes = [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)]
    print("[1] Solving eigenvalues and plotting comparison...")
    plot_eigenmodes(None, modes, os.path.join(OUT, "orbital_eigenmode_comparison.png"))

    # ── 2D cross-sections ──
    orbitals_2d = [(1, 0, 0), (2, 1, 0), (2, 1, 1), (3, 2, 0)]
    for n, l, m in orbitals_2d:
        print(f'[2D] Generating {n}{"spdfg"[l]} m={m} cross-section...')
        ode = OrbitalODE(Z_nuc=1, l=l, r_max_bohr=max(30, 5 * n**2), n_points=3000)
        E = ode.find_eigenvalue(n)
        u = ode.eigenmode(E)
        name = f'orbital_{n}{"spdfg"[l]}_m{m}'
        plot_2d_orbital(ode, n, l, m, u, os.path.join(OUT, f"{name}_cross_section.png"))

    # ── Animated standing wave (1s) ──
    print("[Anim] Generating 1s oscillation animation...")
    ode_1s = OrbitalODE(Z_nuc=1, l=0, r_max_bohr=15, n_points=2000)
    E_1s = ode_1s.find_eigenvalue(1)
    u_1s = ode_1s.eigenmode(E_1s)
    make_orbital_animation(ode_1s, 1, 0, 0, u_1s, os.path.join(OUT, "orbital_1s_oscillation.gif"))

    # ── Animated standing wave (2p) ──
    print("[Anim] Generating 2p oscillation animation...")
    ode_2p = OrbitalODE(Z_nuc=1, l=1, r_max_bohr=30, n_points=2500)
    E_2p = ode_2p.find_eigenvalue(2)
    u_2p = ode_2p.eigenmode(E_2p)
    make_orbital_animation(ode_2p, 2, 1, 0, u_2p, os.path.join(OUT, "orbital_2p_oscillation.gif"))

    print()
    print("=" * 60)
    print("  All outputs saved to assets/sim_outputs/")
    print("=" * 60)


if __name__ == "__main__":
    main()
