r"""
1D FDTD Bond Energy Solver — First-Principles Force Constants
=============================================================

Computes the total electromagnetic energy E(d) of two nuclear defects
(massive nodes) embedded in the AVE nonlinear vacuum lattice, as a
function of their separation distance d.

The bond force constant k = d²E/dd² is extracted at the energy minimum,
giving a zero-parameter derivation of covalent bond stiffness.

Physical Model
--------------
- Each nucleus is a localized μ_eff enhancement: μ_local = μ₀ · (m_atom/m_e)
  representing trapped rotational inertia (mass = inductance).
- The space between nuclei experiences Axiom 4 dielectric saturation:
  ε_eff = ε₀ · √(1 - (V/V_snap)²)
- Shared electrons are modeled as n_e additional charge carriers in the
  bond region, providing capacitive coupling.
- The equilibrium bond length emerges where attractive dielectric coupling
  balances repulsive μ-saturation at short range.

Algorithm
---------
1. Set up 1D lattice with two massive defect sites
2. Initialize a standing wave (thermal seed) and evolve to equilibrium
3. Record total EM energy at each separation
4. Fit E(d) and extract k = d²E/dd² at the minimum
"""

from __future__ import annotations

import numpy as np

from ave.axioms.scale_invariant import saturation_factor
from ave.core.constants import ALPHA, B_SNAP, C_0, EPSILON_0, L_NODE, M_E
from ave.core.constants import M_U as _DA  # kg per Dalton — single source of truth
from ave.core.constants import MU_0, V_SNAP


class BondFDTD1D:
    """
    1D nonlinear FDTD solver for computing bond energetics.

    The lattice pitch is ℓ_node = ℏ/(m_e·c) ≈ 3.86e-13 m.
    Each cell is one vacuum LC node.

    CFL: dt = dx / (2 · c / √(max(μ_r·ε_r))) to handle massive defects.
    """

    def __init__(self, n_cells: int, dx: float = L_NODE, damping: float = 0.0):
        self.n = n_cells
        self.dx = dx

        # Field arrays
        self.E = np.zeros(n_cells)
        self.H = np.zeros(n_cells - 1)

        # Material arrays (relative)
        self.mu_r = np.ones(n_cells - 1)
        self.eps_r = np.ones(n_cells)

        # Damping coefficient for equilibration (0 = lossless)
        self.damping = damping

        # dt will be set after defects are placed
        self._dt_set = False
        self.dt = dx / (2.0 * C_0)

    def _update_dt(self):
        """Recompute dt based on the maximum μ_r·ε_r product (adaptive CFL)."""
        # Local wave speed: v = c / √(μ_r · ε_r_avg)
        # ε at H-nodes = average of adjacent E-nodes
        eps_at_h = 0.5 * (self.eps_r[:-1] + self.eps_r[1:])
        max_product = np.max(self.mu_r * eps_at_h)
        slowdown = np.sqrt(max_product)
        self.dt = self.dx / (2.0 * C_0 * slowdown)
        self._dt_set = True

    def place_nuclear_defect(self, site: int, mass_kg: float, n_resonators: int = 0):
        """
        Place a massive nuclear defect at the given lattice site.

        The nucleus enhances local μ by m/m_e (mass = inductance).
        Shared electrons enhance local ε in the bond region.
        """
        mu_enhancement = mass_kg / M_E

        # Spread over ~5 cells (Gaussian-like) to soften the defect
        spread = {-2: 0.05, -1: 0.25, 0: 1.0, 1: 0.25, 2: 0.05}
        for offset, weight in spread.items():
            idx = site + offset
            if 0 <= idx < self.n - 1:
                self.mu_r[idx] += mu_enhancement * weight

        # Electrons enhance local ε
        if n_resonators > 0:
            eps_enhancement = n_resonators * (1.0 / ALPHA)
            for offset, weight in spread.items():
                idx = site + offset
                if 0 <= idx < self.n:
                    self.eps_r[idx] += eps_enhancement * weight

        # Recompute CFL
        self._update_dt()

    def _epsilon_eff(self):
        """Local ε with Axiom 4 saturation."""
        V_local = np.abs(self.E) * self.dx
        return EPSILON_0 * self.eps_r * saturation_factor(V_local, V_SNAP)

    def _mu_eff(self):
        """Local μ with Axiom 4 saturation."""
        B_local = MU_0 * np.abs(self.H)
        return MU_0 * self.mu_r * saturation_factor(B_local, B_SNAP)

    def seed_thermal_field(self, amplitude: float = 1e-12):
        """Initialize with very low-amplitude thermal noise."""
        rng = np.random.default_rng(42)
        # Scale to V_SNAP/dx for E, B_SNAP/μ₀ for H — but at tiny amplitude
        self.E[:] = amplitude * V_SNAP * rng.standard_normal(self.n) / self.dx
        self.H[:] = amplitude * B_SNAP * rng.standard_normal(self.n - 1) / MU_0

    def step(self, n_steps: int = 1):
        """Advance the simulation with adaptive CFL and optional damping."""
        if not self._dt_set:
            self._update_dt()

        damp = 1.0 - self.damping  # per-step damping factor

        for _ in range(n_steps):
            # Update H
            mu_eff = self._mu_eff()
            ch = self.dt / (self.dx * mu_eff)
            self.H[:] -= ch * (self.E[1:] - self.E[:-1])
            self.H[:] *= damp

            # Absorbing BCs
            self.E[0] = self.E[1]
            self.E[-1] = self.E[-2]

            # Update E
            eps_eff = self._epsilon_eff()
            ce = self.dt / (self.dx * eps_eff)
            self.E[1:-1] += ce[1:-1] * (self.H[1:] - self.H[:-1])
            self.E[1:-1] *= damp

    def total_energy(self) -> float:
        """U = Σ (½ε_eff|E|² + ½μ_eff|H|²) · dx"""
        eps_eff = self._epsilon_eff()
        mu_eff = self._mu_eff()
        u_e = 0.5 * eps_eff * self.E**2 * self.dx
        u_m = 0.5 * mu_eff * self.H**2 * self.dx
        return float(np.sum(u_e) + np.sum(u_m))

    def structural_energy(self) -> float:
        """
        Compute the STRUCTURAL energy of the lattice configuration.

        This is the energy stored in the μ and ε profile itself — independent
        of the field amplitudes. It represents the rest-mass + coupling energy
        of the defects.

        For a vacuum LC lattice with enhanced μ and ε at defect sites:
          E_struct = Σ ½ · (μ_eff(i) · ε_eff(i)) · ℓ_node² · c²

        This captures the mass-energy (mc²) at each node plus the dielectric
        coupling energy between nodes.
        """
        # At zero fields, ε_eff = ε₀·ε_r and μ_eff = μ₀·μ_r
        # Energy per cell: ½ · μ₀·μ_r · ε₀·ε_r · dx² · c²
        #                = ½ · μ_r·ε_r · (μ₀·ε₀) · dx² · c²
        #                = ½ · μ_r·ε_r · dx² / c²  · c²
        #                  (since μ₀·ε₀ = 1/c²)
        #                = ½ · μ_r·ε_r · dx²

        # But we want the COUPLING energy — the difference between
        # the energy with both defects vs the sum of isolated defects.
        # For the structural profile, this comes from the ε_r overlap
        # in the bond region.

        # Use the geometric mean for H-node ε
        eps_at_h = 0.5 * (self.eps_r[:-1] + self.eps_r[1:])
        product = self.mu_r * eps_at_h

        # Energy density per cell: scales with √(μ·ε) × rest energy
        # E_node = m_e·c² × √(μ_r·ε_r) × dx/ℓ_node
        E_per_cell = M_E * C_0**2 * np.sqrt(product) * (self.dx / L_NODE)

        return float(np.sum(E_per_cell))


def compute_bond_energy_curve(
    mass_a_kg: float,
    mass_b_kg: float,
    n_shared_electrons: int,
    d_min_m: float = 0.5e-10,
    d_max_m: float = 4.0e-10,
    n_points: int = 100,
    lattice_padding: int = 200,
    use_fdtd: bool = False,
    n_equilibration_steps: int = 2000,
) -> tuple:
    """
    Compute total energy vs separation for two nuclear defects.

    Two modes:
      - Structural (default): compute energy from the μ·ε profile only.
        Fast, deterministic, no numerical stability issues.
      - FDTD: evolve fields and measure total EM energy.
        Captures dynamic effects but requires stability tuning.
    """
    d_range = np.linspace(d_min_m, d_max_m, n_points)
    energies = np.zeros(n_points)

    # Compute isolated defect energies (for subtraction)
    iso_a = BondFDTD1D(2 * lattice_padding)
    iso_a.place_nuclear_defect(lattice_padding, mass_a_kg, n_resonators=0)
    E_iso_a = iso_a.structural_energy()

    iso_b = BondFDTD1D(2 * lattice_padding)
    iso_b.place_nuclear_defect(lattice_padding, mass_b_kg, n_resonators=0)
    E_iso_b = iso_b.structural_energy()

    E_isolated = E_iso_a + E_iso_b

    for i, d in enumerate(d_range):
        n_bond_cells = max(3, int(round(d / L_NODE)))
        n_total = n_bond_cells + 2 * lattice_padding

        solver = BondFDTD1D(n_total, damping=0.01 if use_fdtd else 0.0)

        site_a = lattice_padding
        site_b = lattice_padding + n_bond_cells

        n_e_each = n_shared_electrons // 2
        solver.place_nuclear_defect(site_a, mass_a_kg, n_resonators=n_e_each)
        solver.place_nuclear_defect(site_b, mass_b_kg, n_resonators=n_e_each)

        # Shared electron cloud in bond region
        eps_bond = n_shared_electrons * (1.0 / ALPHA)
        for j in range(site_a, site_b + 1):
            if 0 <= j < n_total:
                solver.eps_r[j] += eps_bond * 0.5
        solver._update_dt()

        if use_fdtd:
            solver.seed_thermal_field(amplitude=1e-15)
            solver.step(n_equilibration_steps)
            e_samples = []
            for _ in range(50):
                solver.step(20)
                e_samples.append(solver.total_energy())
            energies[i] = np.mean(e_samples)
        else:
            # Structural energy: coupling via μ·ε profile
            E_coupled = solver.structural_energy()
            energies[i] = E_coupled - E_isolated  # Bond energy = coupling energy

    return d_range, energies


def extract_force_constant(d_array, E_array):
    """
    Extract equilibrium distance and force constant from an E(d) curve.

    Returns:
        d_eq: Equilibrium separation [m] (at energy minimum).
        k: Force constant [N/m] (second derivative at minimum).
        E_min: Minimum energy [J].
    """
    i_min = np.argmin(E_array)
    d_eq = d_array[i_min]
    E_min = E_array[i_min]

    dd = d_array[1] - d_array[0]
    if 1 < i_min < len(d_array) - 2:
        # 5-point stencil for smoother second derivative
        k = (
            -E_array[i_min - 2]
            + 16 * E_array[i_min - 1]
            - 30 * E_array[i_min]
            + 16 * E_array[i_min + 1]
            - E_array[i_min + 2]
        ) / (12 * dd**2)
    elif 0 < i_min < len(d_array) - 1:
        k = (E_array[i_min + 1] - 2 * E_array[i_min] + E_array[i_min - 1]) / dd**2
    else:
        # Fit a parabola
        i_lo = max(0, i_min - 5)
        i_hi = min(len(d_array), i_min + 6)
        coeffs = np.polyfit(d_array[i_lo:i_hi], E_array[i_lo:i_hi], 2)
        k = 2 * coeffs[0]
        d_eq = -coeffs[1] / (2 * coeffs[0])
        E_min = np.polyval(coeffs, d_eq)

    return d_eq, abs(k), E_min


# ═══════════════════════════════════════════════════════════
# ATOMIC MASSES (CODATA 2018)
# ═══════════════════════════════════════════════════════════

NUCLEAR_MASSES = {
    "H": 1.00794 * _DA,
    "C": 12.0107 * _DA,
    "N": 14.0067 * _DA,
    "O": 15.9994 * _DA,
    "S": 32.065 * _DA,
}

# Bond definitions: (atom_a, atom_b, n_shared_electrons)
BOND_DEFS = {
    "C-H": ("C", "H", 2),
    "C-C": ("C", "C", 2),
    "C=C": ("C", "C", 4),
    "C-N": ("C", "N", 2),
    "C~N": ("C", "N", 3),  # peptide bond (partial double, amide)
    "C=O": ("C", "O", 4),
    "C-O": ("C", "O", 2),
    "N-H": ("N", "H", 2),
    "O-H": ("O", "H", 2),
    "S-H": ("S", "H", 2),
    "C-S": ("C", "S", 2),
    "S-S": ("S", "S", 2),
}

# Known IR-derived force constants for comparison [N/m]
KNOWN_K = {
    "C-H": 494,
    "C-C": 354,
    "C=C": 965,
    "C-N": 461,
    "C~N": 640,
    "C=O": 1170,
    "C-O": 489,
    "N-H": 641,
    "O-H": 745,
    "S-H": 390,
    "C-S": 253,
    "S-S": 236,
}

# Known crystallographic bond lengths for comparison [m]
KNOWN_D = {
    "C-H": 1.09e-10,
    "C-C": 1.54e-10,
    "C=C": 1.34e-10,
    "C-N": 1.47e-10,
    "C~N": 1.33e-10,
    "C=O": 1.23e-10,
    "C-O": 1.43e-10,
    "N-H": 1.01e-10,
    "O-H": 0.96e-10,
    "S-H": 1.34e-10,
    "C-S": 1.82e-10,
    "S-S": 2.05e-10,
}


if __name__ == "__main__":
    print("=" * 70)
    print("  AVE Bond Energy Solver — First-Principles Force Constants")
    print("=" * 70)
    print(f"  Lattice pitch: ℓ_node = {L_NODE:.4e} m")
    print(f"  V_snap = {V_SNAP:.4e} V,  B_snap = {B_SNAP:.4e} T")
    print(f"  m_e = {M_E:.4e} kg,  α = {ALPHA:.6e}")

    print("\n" + "=" * 70)
    print(f"  {'Bond':>6}  {'d_eq (Å)':>10}  {'d_known':>8}  " f"{'k (N/m)':>10}  {'k_known':>8}  {'k_ratio':>8}")
    print("-" * 70)

    for bond, (atom_a, atom_b, n_e) in BOND_DEFS.items():
        d, E = compute_bond_energy_curve(
            NUCLEAR_MASSES[atom_a],
            NUCLEAR_MASSES[atom_b],
            n_e,
            d_min_m=0.5e-10,
            d_max_m=3.5e-10,
            n_points=80,
            lattice_padding=200,
        )

        d_eq, k_pred, E_min = extract_force_constant(d, E)
        k_known = KNOWN_K[bond]
        d_known = KNOWN_D[bond]

        print(
            f"  {bond:>6}  {d_eq*1e10:>10.3f}  {d_known*1e10:>8.2f}  "
            f"{k_pred:>10.1f}  {k_known:>8}  {k_pred/k_known:>8.3f}"
        )
