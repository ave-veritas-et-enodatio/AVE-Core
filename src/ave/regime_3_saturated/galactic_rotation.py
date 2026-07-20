"""
AVE Galactic Rotation: Flat Curves from Vacuum Yield Stress
============================================================

A-034 instance (canonical 2026-05-15): this module implements the MOND
catalog row — local Newtonian acceleration g_N serves as A, MOND scale a_0
serves as A_yield. Same kernel S(A) = √(1−A²) as atomic dielectric breakdown
and BCS B_c(T). See: backmatter Ch 7 (Universal Saturation-Kernel Catalog);
L5 A-034.

The "dark matter problem" vanishes in the AVE framework. Flat galaxy
rotation curves are a direct consequence of the vacuum's Bingham-plastic
rheology: below a critical shear rate, the LC lattice resists differential
rotation via its unbroken mutual inductance. This resistance contributes
an effective gravitational acceleration floor that exactly mimics a
dark matter halo — with zero free parameters.

The mechanism:
  1. Stars in a galaxy orbit within the vacuum LC lattice
  2. Differential orbital velocity creates a SHEAR in the lattice
  3. If shear < saturation threshold: the lattice's mutual inductance
     resists shear → appears as extra gravitational attraction (dark matter)
  4. If shear > saturation threshold: inductance saturates → zero drag
     → conservative Keplerian orbits (inner galaxy)

The crossover radius r_c where v_circular = √(a₀ × r) defines the
MONDian acceleration scale:

    a₀ = (G × M_galaxy × σ_yield)^(1/2) / r_c

This emerges naturally from AVE's Axiom 4 (dielectric saturation).

Key prediction: The MOND acceleration scale a₀ ≈ 1.2×10⁻¹⁰ m/s²
is NOT a free parameter — it emerges from the vacuum's yield stress
and the galaxy's baryonic mass alone.

References:
    - Milgrom (1983): MOND phenomenology
    - McGaugh et al. (2016): Radial Acceleration Relation
    - SPARC database: Lelli et al. (2016)
"""

from dataclasses import dataclass

import numpy as np

from ave.axioms.scale_invariant import saturation_factor
from ave.core.constants import C_0, H_INFINITY, M_SUN, G

# ======================================================
# Critical Acceleration Limit — Axiomatically Derived
# Derived from the fundamental Topological Unknot Expansion (H_INFINITY)
# a₀ = c × H∞ / (2π)  ≈ 1.07×10⁻¹⁰ m/s²
# NO empirical telescope parameter is used.
# ======================================================
A0_LATTICE = float(C_0) * float(H_INFINITY) / (2 * np.pi)


@dataclass
class GalaxyModel:
    """
    Exponential disk galaxy model.

    Attributes:
        name: Galaxy identifier.
        M_disk: Total baryonic disk mass [kg].
        R_d: Disk scale length [m].
        M_bulge: Bulge mass [kg] (default 0).
        R_b: Bulge effective radius [m].
        distance: Distance from Earth [m] (for reference).
    """

    name: str
    M_disk: float  # kg
    R_d: float  # m (disk scale length)
    M_bulge: float = 0  # kg
    R_b: float = 0  # m
    distance: float = 0  # m

    def enclosed_mass_disk(self, r: float) -> float:
        """
        Enclosed disk mass at radius r for an exponential disk.

        M(r) = M_disk × [1 - (1 + r/R_d) × exp(-r/R_d)]

        Freeman (1970) exponential disk profile.
        """
        x = r / self.R_d
        return self.M_disk * (1 - (1 + x) * np.exp(-x))

    def enclosed_mass_bulge(self, r: float) -> float:
        """Hernquist bulge: M(r) = M_b × r² / (r + R_b)²"""
        if self.M_bulge <= 0:
            return 0.0
        return self.M_bulge * r**2 / (r + self.R_b) ** 2

    def enclosed_mass_total(self, r: float) -> float:
        """Total baryonic enclosed mass at radius r."""
        return self.enclosed_mass_disk(r) + self.enclosed_mass_bulge(r)

    def newtonian_velocity(self, r: float) -> float:
        """
        Newtonian circular velocity (baryons only, no dark matter).
        v_N = √(G × M(r) / r)
        """
        M = self.enclosed_mass_total(r)
        if r <= 0 or M <= 0:
            return 0.0
        return np.sqrt(G * M / r)

    def newtonian_acceleration(self, r: float) -> float:
        """Newtonian centripetal acceleration g_N = G×M(r)/r²."""
        M = self.enclosed_mass_total(r)
        if r <= 0:
            return 0.0
        return G * M / r**2


# Exclusively enforce the Axiom 4 derivation. Empirical shortcuts are banned.


def ave_saturation_acceleration(
    g_N: float | np.ndarray,
    a0: float = A0_LATTICE,
) -> float | np.ndarray:
    r"""
    Axiom 4 derivation of MOND: lattice drag via dielectric saturation.

    .. math::
        g_{eff} = g_N + \sqrt{g_N \cdot a_0} \cdot
                  \sqrt{1 - \min(g_N / a_0,\; 1)^2}

    Kernel argument A = g_N/a_0 (quadratic kernel, clipped); the leading
    \sqrt{g_N \cdot a_0} is the deep-MOND drag prefactor slot — a distinct
    position from the kernel argument (#748 R3 + #754 trace). This matches the
    code below (saturation_factor → universal_saturation = √(1 − (A)²)).

    Physical mechanism:
      - The vacuum LC lattice has mutual inductance η₀.
      - The kernel argument (saturation amplitude / A1 strain) is the LOCAL
        FIELD normalized by the yield field: A = g_N/a₀ (LINEAR in g_N), which
        gives the QUADRATIC kernel S = √(1 − (g_N/a₀)²). The √(g_N·a₀) prefactor
        below is a DISTINCT slot — the deep-MOND drag coefficient — NOT the
        kernel argument; a strain ∝ √(g_N) is the KINETIC (v/c) amplitude family
        (a separate node coordinate), not this saturation strain. Corrected
        toward A = g_N/a₀ per #748 R3
        (research/2026-07-20_mond-kernel-adjudication_result.md §2 + Errata-R3)
        + the #754 A1-amplitude trace
        (research/2026-07-20_a1-amplitude-trace_result.md §2, verdict A=g_N-FORCED).
      - When g_N < a₀, the lattice is unsaturated: η_eff ≈ η₀.
        The unsaturated lattice drags on orbiting mass → "dark matter".
      - When g_N ≥ a₀, the lattice saturates: η_eff → 0.
        No drag → conservative Keplerian orbits.

    The saturation_factor √(1 − (g_N/a₀)²) is the SAME operator that
    (quadratic kernel, A = g_N/a₀; #748 R3 + #754 trace):
      - Confines particles (Pauli exclusion)
      - Drives FDTD field updates
      - Creates plasma cutoff
      - Defines bond energies

    Asymptotic limits:
      - g_N → 0:   g_eff → √(g_N · a₀)     (deep MOND)
      - g_N → a₀:  g_eff → g_N + 0 = g_N    (Newtonian)
      - g_N > a₀:  g_eff = g_N               (Newtonian)

    Args:
        g_N: Newtonian gravitational acceleration [m/s²] (scalar or array).
        a0: Critical acceleration scale [m/s²].

    Returns:
        Effective acceleration including lattice drag [m/s²].
    """
    g_N = np.asarray(g_N, dtype=float)
    scalar = g_N.ndim == 0
    g_N = np.atleast_1d(g_N)

    # Saturation factor: S = √(1 − (g_N/a₀)²), clipped at a₀ (quadratic
    # kernel, A = g_N/a₀; #748 R3 + #754 trace)
    S = saturation_factor(g_N, a0)  # clips to 0 when g_N ≥ a₀

    # Lattice drag contribution: ∝ √(g_N · a₀) × unsaturated fraction
    g_drag = np.sqrt(np.maximum(g_N * a0, 0.0)) * S

    g_eff = g_N + g_drag
    return float(g_eff[0]) if scalar else g_eff


def ave_rotation_velocity(galaxy: GalaxyModel, r: float, a0: float = A0_LATTICE) -> float:
    """
    AVE-predicted rotation velocity at radius r.

    v_AVE = √(g_eff × r)

    where g_eff includes the universal lattice drag contribution.

    Args:
        galaxy: Galaxy model.
        r: Galactocentric radius [m].
        a0: Critical acceleration.

    Returns:
        Circular velocity [m/s].
    """
    g_N = galaxy.newtonian_acceleration(r)
    g_eff = ave_saturation_acceleration(g_N, a0)
    return np.sqrt(g_eff * r)


def radial_acceleration_relation(g_N: np.ndarray, a0: float = A0_LATTICE) -> np.ndarray:
    """
    The Radial Acceleration Relation (RAR): g_obs vs g_bar.

    McGaugh et al. (2016) discovered empirically that:
        g_obs = g_bar / (1 - exp(-√(g_bar/a₀)))

    AVE strictly derives this from first principles via Axiom 4 saturation:
        g_obs = g_bar + √(g_bar × a₀) × √(1 - (g_bar/a₀)²)
        (quadratic kernel, A = g_bar/a₀; √(g_bar·a₀) = deep-MOND drag
        prefactor slot — #748 R3 + #754 trace)

    Args:
        g_N: Array of Newtonian (baryonic) accelerations [m/s²].
        a0: Critical acceleration.

    Returns:
        Array of observed (effective) accelerations [m/s²].
    """
    return ave_saturation_acceleration(g_N, a0)


# Emitted: derive_a0_from_cosmology (Empirical Hubble shortcut banned).


# ======================================================
# Catalog of well-studied galaxies
# ======================================================

KPC = 3.0857e19  # m

GALAXY_CATALOG = {
    "Milky Way": GalaxyModel(
        name="Milky Way",
        M_disk=5.0e10 * M_SUN,
        R_d=2.6 * KPC,
        M_bulge=1.5e10 * M_SUN,
        R_b=0.6 * KPC,
        distance=0,
    ),
    "M31 (Andromeda)": GalaxyModel(
        name="M31 (Andromeda)",
        M_disk=7.0e10 * M_SUN,
        R_d=5.3 * KPC,
        M_bulge=3.0e10 * M_SUN,
        R_b=1.0 * KPC,
        distance=778 * KPC,
    ),
    "NGC 3198": GalaxyModel(
        name="NGC 3198",
        M_disk=3.0e10 * M_SUN,
        R_d=3.0 * KPC,
        M_bulge=0,
        R_b=0,
        distance=13300 * KPC,
    ),
    "UGC 2885": GalaxyModel(
        name="UGC 2885",
        M_disk=2.0e11 * M_SUN,
        R_d=12.0 * KPC,
        M_bulge=3.0e10 * M_SUN,
        R_b=2.0 * KPC,
        distance=76000 * KPC,
    ),
    "DDO 154 (dwarf)": GalaxyModel(
        name="DDO 154",
        M_disk=5.0e8 * M_SUN,
        R_d=1.0 * KPC,
        M_bulge=0,
        R_b=0,
        distance=3700 * KPC,
    ),
}
