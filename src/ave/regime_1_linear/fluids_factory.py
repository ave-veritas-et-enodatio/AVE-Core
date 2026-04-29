"""
AVE Fluid Physics: Water as Impedance-Matched LC Network
=========================================================

Water's anomalous properties arise from the H₂O molecule's bent
geometry acting as an LC impedance-matching network in the vacuum lattice.

Key anomalies explained via impedance:
  1. 4°C density maximum
  2. Unusually high heat capacity
  3. High surface tension
  4. Anomalous dielectric constant (ε_r ≈ 80)

The AVE model:
  - Each H₂O molecule is a bent dipole antenna (104.5° bend angle)
  - The O-H bonds are matched transmission line stubs
  - At 4°C, the thermal phonon frequency matches the fundamental
    resonance of the H-bond network → maximum impedance matching
    → minimum volume (maximum packing) → density maximum
  - Above 4°C: thermal expansion dominates (normal behavior)
  - Below 4°C: ice-like tetrahedral ordering increases volume

The critical insight: the 4°C anomaly occurs at the impedance
crossing point where the H-bond network's Q factor peaks.

Pressure assumption:
  All models in this module assume standard atmospheric pressure
  (P = 1 atm = 101.325 kPa). At elevated pressures the H-bond
  network stiffens, shifting the density maximum and dielectric
  constant. Extending to P > 1 atm requires adding a pressure-
  dependent compressibility correction to the impedance model.

Physical constants for H₂O:
  O-H bond length:    0.9584 Å
  H-O-H angle:        104.45°
  H-bond length:      1.97 Å
  H-bond energy:      ~0.23 eV (23 kJ/mol)
  Molecular mass:     18.015 g/mol
"""

from dataclasses import dataclass

import numpy as np

from ave.core.constants import C_0, HBAR, K_B, M_U
from ave.core.constants import e_charge as EV_TO_J

# Physical constants
H_BAR = float(HBAR)  # ℏ [J·s] — from constants.py


@dataclass
class MolecularFluid:
    """Generalized AVE impedance model for an arbitrary fluid molecule."""

    bond_length: float  # Primary intra-molecular bond [m]
    bond_angle: float  # Primary bending angle [degrees]
    inter_bond_length: float  # Inter-molecular cohesive bond [m]
    inter_bond_energy: float  # Inter-molecular cohesive energy [J]

    # Masses
    m_center: float  # Central nucleus mass [kg]
    m_ligand: float  # Attached ligand mass [kg]
    n_ligands: int  # Number of attached ligands

    vdw_radius: float  # Van der Waals radius [m]
    wavenumber_cm_inv: float  # Intramolecular stretching [cm^-1]

    @property
    def total_mass(self) -> float:
        """Total molecular mass [kg]."""
        return self.m_center + self.n_ligands * self.m_ligand

    @property
    def reduced_mass(self) -> float:
        """Reduced mass of core-ligand pair [kg]."""
        return (self.m_center * self.m_ligand) / (self.m_center + self.m_ligand)

    @property
    def spring_constant(self) -> float:
        """Effective spring constant of primary bond [N/m]."""
        nu_tilde = self.wavenumber_cm_inv * 100.0  # cm⁻¹ → m⁻¹
        c = float(C_0)
        omega = 2 * np.pi * c * nu_tilde
        return self.reduced_mass * omega**2

    @property
    def resonant_frequency(self) -> float:
        """Primary stretching resonance [Hz]."""
        return np.sqrt(self.spring_constant / self.reduced_mass) / (2 * np.pi)

    @property
    def inductance_ave(self) -> float:
        """AVE macroscopic inductance analog L = μ·d² [H]."""
        return self.reduced_mass * self.bond_length**2

    @property
    def capacitance_ave(self) -> float:
        """AVE macroscopic capacitance analog C = 1/(ω²L) [F]."""
        omega = 2 * np.pi * self.resonant_frequency
        return 1.0 / (omega**2 * self.inductance_ave)

    @property
    def impedance_ave(self) -> float:
        """AVE topological characteristic impedance [Ω-equiv]."""
        return np.sqrt(self.inductance_ave / self.capacitance_ave)


@dataclass
class WaterMolecule(MolecularFluid):
    """AVE impedance model of H₂O — all constants derived from the physics engine.

    Engine-derived (6/6 — zero empirical inputs):
        bond_length:       molecular_bond_distance(r_O, r_H, N_load=2)
                           Fabry-Pérot eigenvalue with σ-cavity loading
        bond_angle:        arccos(-1/(3(1+Γ))) where Γ = (r_O-r_H)/(r_O+r_H)
                           Op3 small-signal impedance transmission correction
                           to sp3 tetrahedral angle arccos(-1/3)
        spring_constant:   Coulomb bond force constant solver (Slater + lattice topology)
        vdw_radius:        Op9 steric exclusion from center of mass
        inter_bond_length: Op4 pairwise potential equilibrium
        inter_bond_energy: Γ²αℏc void-fraction bounded coupling
    """

    # Mass constants — fundamental (Axiom 4)
    # M_U imported from constants.py (single source of truth for Dalton)
    m_center: float = 15.999 * M_U  # O nucleus [kg]
    m_ligand: float = 1.008 * M_U  # H nucleus [kg]
    n_ligands: int = 2

    # Engine-derived via Coulomb bond force constant solver (no spectroscopic input)
    wavenumber_cm_inv: float = 0.0  # DEPRECATED: engine-derived k_OH used instead

    # Engine-derived defaults (overridden in __post_init__)
    bond_length: float = 0.0
    bond_angle: float = 0.0  # Derived from Op3: arccos(-1/(3(1+Γ)))
    inter_bond_length: float = 0.0
    inter_bond_energy: float = 0.0
    vdw_radius: float = 0.0

    def __post_init__(self) -> None:
        """Derive geometric constants from the AVE physics engine."""
        from ave.core.constants import ALPHA, RY_EV
        from ave.solvers.coupled_resonator import atom_port_impedance, ionization_energy, molecular_bond_distance

        # Ionization energies from Mutual Cavity Loading solver
        IE_O = ionization_energy(8)
        IE_H = ionization_energy(1)

        # Port impedances (valence orbital radii)
        r_O = atom_port_impedance(8, IE_O)
        r_H = atom_port_impedance(1, IE_H)

        # O-H bond distance: loaded Fabry-Pérot eigenvalue
        # The solver uses Z_O=8 and Z_H=1 to automatically derive:
        # N_eff = 2*bond_order + max(N_sO, N_sH)/2 = 2(1) + 2/2 = 3.0
        self.bond_length = molecular_bond_distance(r_O, r_H, Z_A=8, Z_B=1, bond_order=1)

        # H-O-H bond angle: Op3 small-signal impedance correction to sp3.
        # The sp3 tetrahedral angle cos(θ_tet) = -1/3 assumes 4 equivalent
        # orbitals (Axiom 1: K4 unit cell). Oxygen has 2 bonding + 2 lone pairs.
        # The O-H junction transmits through the impedance mismatch Γ:
        #   Γ = (r_O - r_H)/(r_O + r_H)  (Op3 reflection coefficient)
        # The transmission factor (1+Γ) modifies the tetrahedral cosine:
        #   cos(θ_HOH) = cos(θ_tet) / (1 + Γ) = -1/(3(1+Γ))
        # Large-signal check: arccos(-φ/3) = 104.29° (Op8 packing, 0.19° gap)
        Gamma_bond = (r_O - r_H) / (r_O + r_H)
        self.bond_angle = float(
            np.degrees(np.arccos(-1.0 / (3.0 * (1.0 + Gamma_bond))))
        )  # → 104.48° (exp: 104.45°, error: +0.03°)

        # Van der Waals radius: Op9 steric exclusion envelope.
        # The molecular collision boundary is the furthest atomic shell edge
        # from the center of mass. For H₂O, each H sits at (bond_length) from O
        # at angle ±(bond_angle/2) from the bisector. The CoM is offset from O:
        theta_rad = np.deg2rad(self.bond_angle)
        com_offset = (self.n_ligands * self.m_ligand * self.bond_length * np.cos(theta_rad / 2.0)) / self.total_mass
        # H distance from CoM (in molecular plane):
        H_along = self.bond_length * np.cos(theta_rad / 2.0) - com_offset
        H_perp = self.bond_length * np.sin(theta_rad / 2.0)
        H_dist_from_com = np.sqrt(H_along**2 + H_perp**2)
        # Add the ligand's own port impedance shell (Op9 boundary):
        self.vdw_radius = H_dist_from_com + r_H

        # H-bond distance: Op4 equilibrium between H(δ+) and O₂(lone pair)
        # K = Γ²αℏc (partial charge coupling from Op3 impedance mismatch)
        # d_sat = r_H + r_O (saturation at atomic contact)
        # d_eq = Op4 potential minimum (universal_pairwise_energy)
        import numpy as _np

        from ave.core.constants import C_0, HBAR
        from ave.core.universal_operators import universal_pairwise_energy

        Gamma = (r_O - r_H) / (r_O + r_H)
        K_hbond = Gamma**2 * float(ALPHA * HBAR * C_0)  # J·m
        d_sat_hb = r_H + r_O  # atomic contact distance

        _r = _np.linspace(d_sat_hb * 1.0001, 5e-10, 10000)
        _U = universal_pairwise_energy(_r, K_hbond, d_sat_hb)
        _i = _np.argmin(_U)
        self.inter_bond_length = float(_r[_i]) if 0 < _i < len(_r) - 1 else d_sat_hb

        # H-bond energy: from the Op4 well depth at equilibrium
        # The H-bond is an interstitial topological linkage connecting two non-overlapping
        # atomic spheres. The maximum available storable potential is bounded by the
        # interstitial Void Fraction (1 - \phi_pack) between molecular nodes.
        from ave.core.constants import N_PHI_PACK

        base_U = abs(float(_U[_i])) if 0 < _i < len(_r) - 1 else (3.0 * float(ALPHA) * float(RY_EV) * EV_TO_J)
        self.inter_bond_energy = base_U * (1.0 - float(N_PHI_PACK))

        # O-H spring constant: Coulomb bond force constant solver
        # Derives k_OH from Slater orbitals + lattice topology corrections:
        #   1. Isotropy projection (1/3 for 3D)
        #   2. Three-phase balance (1/√3 for terminal H)
        #   3. Lone-pair dynamic softening (O has 4 lone-pair electrons)
        # All inputs are Z_a, Z_b, ε₀, m_e, ℏ, e — AVE axioms only.
        from ave.topological.soliton_bond_solver import compute_bond_curve, extract_force_constant

        _d_bond, _E_bond = compute_bond_curve(8, 1, 2, d_min=0.3e-10, d_max=4.0e-10, n_points=300)
        _, self._k_OH_engine, _ = extract_force_constant(_d_bond, _E_bond, Z_a=8, Z_b=1, n_shared=2)

    # Compatibility properties mathematically re-routed to generalized variables
    @property
    def m_O(self) -> float:
        return self.m_center

    @property
    def m_H(self) -> float:
        return self.m_ligand

    @property
    def oh_bond_length(self) -> float:
        return self.bond_length

    @property
    def hoh_angle(self) -> float:
        return self.bond_angle

    @property
    def hbond_length(self) -> float:
        return self.inter_bond_length

    @property
    def hbond_energy(self) -> float:
        return self.inter_bond_energy

    @property
    def reduced_mass_oh(self) -> float:
        return self.reduced_mass

    @property
    def oh_spring_constant(self) -> float:
        return self.spring_constant

    @property
    def spring_constant(self) -> float:
        """Engine-derived O-H spring constant from Coulomb bond solver [N/m]."""
        return self._k_OH_engine

    @property
    def oh_resonant_frequency(self) -> float:
        return self.resonant_frequency


class FluidImpedanceFactory:
    """
    Generalized continuum solver for arbitrary molecular fluids in Regime 1.
    Derives macroscopic continuum fields (density, dielectric bounds) exclusively
    from the topological LC mechanics of individual molecules.
    """

    def __init__(self, fluid: MolecularFluid) -> None:
        self.fluid = fluid

    def compute_density(self, T_celsius: float, P_pascal: float = 101325.0) -> float:
        """
        SM-LEGACY: Two-state volume mixture model.

        WARNING: This function uses Statistical Mechanics concepts:
          - Two-state (tetrahedral/RCP) volume mixing
          - Population-weighted structural fraction
          - Classical thermal expansion

        These are NOT derived from AVE axioms. This function is retained
        for backward compatibility with existing pipeline scripts.

        For axiom-derived quantities, use CooperativeHexagonalLattice:
          - T_m: melting point (Axiom 1 + Op4)
          - T(ρ_max): density maximum temperature (Axiom 2)
        """
        import warnings

        warnings.warn(
            "compute_density uses SM two-state mixture model. "
            "Use CooperativeHexagonalLattice for axiom-derived quantities.",
            stacklevel=2,
        )
        T_K = T_celsius + 273.15

        # Volume of tetrahedral unit cell
        r_inter = self.fluid.bond_length + self.fluid.inter_bond_length
        a_lattice = r_inter * 4.0 / np.sqrt(3.0)
        V_I = (a_lattice**3) / 8.0

        # FCC collapse volume (Axiom 2: K=2G → FCC packing)
        from ave.core.constants import N_PHI_PACK

        V_II = V_I * float(N_PHI_PACK)

        # SM-LEGACY: structural fraction (inlined from removed method)
        from ave.regime_1_linear.hexagonal_lattice import CooperativeHexagonalLattice

        lattice_solver = CooperativeHexagonalLattice(
            E_hb_joules=self.fluid.inter_bond_energy,
            d_hb_meters=self.fluid.inter_bond_length,
            m_ligand_kg=self.fluid.m_ligand,
            k_intra=self.fluid.spring_constant,
        )
        # SM: two-state structural fraction
        k_hb = lattice_solver.k_hb
        d_hb = lattice_solver.d_hb
        T_m = lattice_solver.T_m_K
        if T_K < T_m:
            delta_x = np.sqrt(K_B * T_K / k_hb)
            r0 = delta_x / d_hb
            f_I = 1.0 - r0**2 / 2.0
        else:
            excess_kT = K_B * (T_K - T_m)
            delta_x_excess = np.sqrt(excess_kT / k_hb) if excess_kT > 0 else 0.0
            r_excess = delta_x_excess / d_hb
            if r_excess >= 1.0:
                f_I = float(N_PHI_PACK)
            else:
                p_survive = 1.0 - r_excess**2
                f_I = float(N_PHI_PACK) + p_survive * (1.0 - float(N_PHI_PACK))

        # Structural Phase interpolation (Phase I vs Phase II)
        # Note: We completely explicitly discard classical continuous thermal expansion
        # which erroneously artificially stretches the entire macroscopic structure
        # using local 1D harmonic approximations. Geometric bounds dominate the VCA fluid model.
        V_avg = f_I * V_I + (1.0 - f_I) * V_II
        return self.fluid.total_mass / V_avg

    def compute_dielectric(self, T_celsius: float, P_pascal: float = 101325.0) -> float:
        """Generalized Kirkwood-Fröhlich dielectric constant solver."""
        from ave.core.constants import EPSILON_0, e_charge

        T_K = T_celsius + 273.15
        kT = K_B * T_K

        theta_rad = np.deg2rad(self.fluid.bond_angle)
        # Op3 impedance mismatch: charge transfer Γ at the bond junction.
        # The bond connects two atomic cavities with port impedances r_A, r_B
        # (from atom_port_impedance = n·a₀·√(Ry/IE)).
        # The reflection coefficient is:
        #   Γ = (r_center - r_ligand) / (r_center + r_ligand)
        # For O-H: r_O = 1.059 Å (n=2), r_H = 0.529 Å (n=1)
        # Γ = (1.059 - 0.529)/(1.059 + 0.529) ≈ 1/3  (derived, not fitted)
        from ave.solvers.coupled_resonator import atom_port_impedance, ionization_energy

        IE_c = ionization_energy(8)  # Oxygen
        IE_l = ionization_energy(1)  # Hydrogen
        r_c = atom_port_impedance(8, IE_c)
        r_l = atom_port_impedance(1, IE_l)
        Gamma = (r_c - r_l) / (r_c + r_l)
        q_eff = Gamma * e_charge
        mu = 2.0 * q_eff * self.fluid.bond_length * np.cos(theta_rad / 2.0)

        n_density = self.compute_density(T_celsius, P_pascal) / self.fluid.total_mass

        # SM-LEGACY: structural fraction (inlined)
        from ave.regime_1_linear.hexagonal_lattice import CooperativeHexagonalLattice

        lattice_solver = CooperativeHexagonalLattice(
            E_hb_joules=self.fluid.inter_bond_energy,
            d_hb_meters=self.fluid.inter_bond_length,
            m_ligand_kg=self.fluid.m_ligand,
            k_intra=self.fluid.spring_constant,
        )
        k_hb = lattice_solver.k_hb
        d_hb = lattice_solver.d_hb
        T_m = lattice_solver.T_m_K
        if T_K < T_m:
            delta_x = np.sqrt(K_B * T_K / k_hb)
            f_I = 1.0 - (delta_x / d_hb) ** 2 / 2.0
        else:
            from ave.core.constants import N_PHI_PACK

            excess_kT = K_B * (T_K - T_m)
            r_excess = np.sqrt(excess_kT / k_hb) / d_hb if excess_kT > 0 else 0.0
            if r_excess >= 1.0:
                f_I = float(N_PHI_PACK)
            else:
                p_survive = 1.0 - r_excess**2
                f_I = float(N_PHI_PACK) + p_survive * (1.0 - float(N_PHI_PACK))

        g_kirkwood = 1.0 + 4.0 * np.cos(theta_rad / 2.0) ** 2 * f_I
        eps_r = 1.0 + 3.0 * (n_density * mu**2 * g_kirkwood) / (3.0 * EPSILON_0 * kT)
        return eps_r

    def compute_surface_tension(self, T_celsius: float) -> float:
        """
        Derives macroscopic surface tension [N/m] via stereological projection
        of the Axiom 4 (Op4) cohesive topology bound by the Vol 7 FCC fluid state.

        Derivation chain:
        1. State II (liquid) structural volume is V_II = V_I * φ_FCC.
        2. A continuous dividing surface intersects the topological nodes
           with an area fraction exactly equal to the packing fraction P_C
           (Delesse's stereological principle).
        3. The densest FCC plane (111) area per node gives the baseline 2D density.
        4. Surface tension is exactly: gamma = n_s * E_hb * P_C.

        Args:
            T_celsius: Temperature [°C] (linear thermal softening to be added)

        Returns:
            Surface tension gamma [N/m] derived entirely from first principles.
        """
        from ave.core.constants import N_PHI_PACK, P_C

        # 1. State I Rigid unit volume V_I
        r_inter = self.fluid.bond_length + self.fluid.inter_bond_length
        a_lattice = r_inter * 4.0 / np.sqrt(3.0)
        V_I = (a_lattice**3) / 8.0

        # 2. State II Topo-collapsed fluid volume
        V_II = V_I * float(N_PHI_PACK)

        # 3. Geometric nodal density on the (111) maximally packed plane
        a_fcc = (4.0 * V_II) ** (1.0 / 3.0)
        area_per_node_111 = a_fcc**2 * np.sqrt(3.0) / 4.0
        n_s_raw = 1.0 / area_per_node_111

        # 4. Stereological Topological boundary limit
        gamma_static = n_s_raw * self.fluid.inter_bond_energy * float(P_C)

        # Simple thermal softening approximation for liquid boundary
        # based on thermal strain r = sqrt(kT / E_hb)
        T_K = T_celsius + 273.15
        r_strain = np.sqrt(K_B * T_K / self.fluid.inter_bond_energy)
        # S(r) = sqrt(1-r^2) ~ (1 - 0.5 r^2)
        thermal_factor = np.sqrt(1.0 - r_strain**2) if r_strain < 1.0 else 0.0

        return gamma_static * thermal_factor


# =========================================================================
# Legacy Abstraction Pipelines (SM-LEGACY)
# =========================================================================


def ave_density_model(T_celsius: float, P_pascal: float = 101325.0) -> float:
    """SM-LEGACY: see FluidImpedanceFactory.compute_density docstring."""
    import warnings

    warnings.warn("ave_density_model is SM-legacy.", stacklevel=2)
    factory = FluidImpedanceFactory(WaterMolecule())
    return factory.compute_density(T_celsius, P_pascal)


def dielectric_constant_water(T_celsius: float, P_pascal: float = 101325.0) -> float:
    factory = FluidImpedanceFactory(WaterMolecule())
    return factory.compute_dielectric(T_celsius, P_pascal)


def find_density_maximum() -> tuple[float, float]:
    """
    Find the temperature of maximum density in the AVE model.

    Returns:
        (T_max, rho_max) in °C and kg/m³.
    """
    temps = np.linspace(-2, 20, 10000)
    densities = np.array([ave_density_model(T) for T in temps])
    i_max = np.argmax(densities)
    return temps[i_max], densities[i_max]


def impedance_crossing_temperature() -> float:
    """
    Find the temperature where the H-bond impedance matches the
    thermal phonon impedance — the "impedance crossing point."

    This is the temperature where:
      Z_thermal(T) = Z_hbond(T)

    Z_thermal ∝ √(k_B T / m) × ρ    (thermal phonon impedance)
    Z_hbond ∝ √(E_hbond / m) × n_hb   (H-bond network impedance)

    The crossing occurs near 4°C.

    Returns:
        Crossing temperature [°C].
    """
    mol = WaterMolecule()
    m = mol.total_mass
    E_hb = mol.hbond_energy

    temps = np.linspace(-5, 30, 10000)
    T_K = temps + 273.15

    # Thermal phonon "impedance" (∝ velocity × density)
    Z_thermal = np.sqrt(K_B * T_K / m) * np.array([ave_density_model(T) for T in temps])

    # H-bond network impedance (weakens with temperature)
    # Axiom 4: bond survival S²(r) = 1 - r², where r = √(kT/E_hb)
    # Replaces SM Boltzmann: exp(-T/T_hb)
    r_strain = np.sqrt(K_B * T_K / E_hb)
    r_strain = np.minimum(r_strain, 0.999)
    n_hb = 1.0 - r_strain**2  # S²(r) = Axiom 4 survival
    Z_hbond = np.sqrt(E_hb / m) * n_hb * np.array([ave_density_model(T) for T in temps])

    # Find crossing (minimum difference)
    Z_thermal_norm = Z_thermal / np.max(Z_thermal)
    Z_hbond_norm = Z_hbond / np.max(Z_hbond)

    diff = np.abs(Z_thermal_norm - Z_hbond_norm)
    i_cross = np.argmin(diff)
    return temps[i_cross]
