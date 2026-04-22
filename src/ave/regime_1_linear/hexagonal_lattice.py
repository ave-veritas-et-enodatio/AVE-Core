from __future__ import annotations

import numpy as np

from ave.core.constants import ALPHA, HBAR, K_B


class CooperativeHexagonalLattice:
    """
    H-Bond Eigenmode Solver for tetrahedral LC lattice networks.

    Derives the fundamental eigenmode of the bridging proton in the
    O-H···O hydrogen bond from pure AVE first principles:

      Axiom 1: The H-bond is an LC transmission line segment.
               L = m_H (proton mass), C = 1/k_hb (bond compliance)

      Op4:     k_hb = 2E_hb/d_hb² (harmonic curvature of the Op4 well)

      Eigenmode: ω₀ = √(k_series / m_H)
                 T_m = ℏω₀ / k_B

    This class provides ONLY axiom-derived quantities:
      - T_m_K: melting point from proton eigenmode
      - k_hb:  H-bond spring constant from Op4
      - z:     tetrahedral coordination (topological constant)
    """

    def __init__(
        self,
        E_hb_joules: float,
        d_hb_meters: float = None,
        m_ligand_kg: float = None,
        k_intra: float = None,
    ):
        """
        Args:
            E_hb_joules: H-bond energy [J] (from Op4 well depth)
            d_hb_meters: H-bond equilibrium distance [m] (from Op4 well position)
            m_ligand_kg: Mass of the bridging ligand [kg] (m_H for water)
            k_intra:     Intramolecular bond spring constant [N/m] (k_OH for water)
        """
        self.E_hb = E_hb_joules
        self.z = 4  # tetrahedral coordination (topological constant)

        # H-bond spring constant from harmonic approximation of Op4 well
        if d_hb_meters is not None:
            self.d_hb = d_hb_meters
            self.k_hb = 2.0 * self.E_hb / d_hb_meters**2
        else:
            self.d_hb = np.sqrt(2.0 * self.E_hb / 1.0)
            self.k_hb = 1.0

        # Proton Transfer Eigenmode → melting temperature
        # ω₀ = √(k_series / m_H)
        # T_m = ℏω₀ / k_B
        #
        # k_series = k_OH × k_hb / (k_OH + k_hb)
        # When k_OH >> k_hb: k_series ≈ k_hb (soft spring dominates)
        if m_ligand_kg is not None:
            if k_intra is not None:
                k_series = (k_intra * self.k_hb) / (k_intra + self.k_hb)
            else:
                k_series = self.k_hb
            omega_m = np.sqrt(k_series / m_ligand_kg)
            self.T_m_K = float(HBAR) * omega_m / K_B
        else:
            self.T_m_K = (self.E_hb * np.sqrt(2.0 * float(ALPHA))) / K_B

    def density_maximum_temperature(self) -> float:
        """
        Temperature of maximum density from the α-corrected eigenmode.

        The bare proton eigenmode gives T_m (melting point).
        Axiom 2 (α couples topology to impedance) red-shifts
        the effective resonance by one factor of α:

          T(ρ_max) = T_m × (1 − α)

        The lattice impedance loads the proton's LC resonance,
        pulling its natural frequency below the bare eigenfrequency.

        Returns:
            Temperature of maximum density [K]
        """
        return self.T_m_K * (1.0 - float(ALPHA))
