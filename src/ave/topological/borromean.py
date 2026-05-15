"""
Topological Generator Module: borromean.py
-------------------------------------------
Generates exact 3D parametric coordinate arrays for fundamental macroscopic
topological defects (knots and links) within the AVE discrete framework.

Includes:
- 0_1 Unknot (Fundamental Lepton / Electron)
- 3_1 Trefoil Knot (used in HOPF-01 antenna topology, NOT the electron)
- 6^3_2 Borromean Link (Fundamental Baryon / Proton)
"""

import numpy as np


class FundamentalTopologies:
    @staticmethod
    def generate_unknot_0_1(radius: float, resolution: int = 1000) -> np.ndarray:
        """
        Generates the 3D parametric coordinates of a 0_1 Unknot.
        In the AVE framework, this is the fundamental lepton topology:
        a single closed flux tube loop at minimum ropelength = 2π.

        The unknot has circumference ℓ_node and tube radius ℓ_node/(2π).
        Its mass is m_e = T_EM · ℓ_node / c².

        Args:
            radius (float): The characteristic radial scale of the loop.
            resolution (int): Number of coordinate points along the curve.

        Returns:
            np.ndarray: [N, 3] array of (x,y,z) spatial coordinates.
        """
        t = np.linspace(0, 2 * np.pi, resolution)

        # Simple torus loop (unknot) in the X-Y plane:
        x = radius * np.cos(t)
        y = radius * np.sin(t)
        z = np.zeros_like(t)

        coords = np.vstack((x, y, z)).T
        return coords

    @staticmethod
    def generate_trefoil_3_1(radius: float, resolution: int = 1000) -> np.ndarray:
        """
        Generates the 3D parametric coordinates of a 3_1 Trefoil Knot.
        NOTE: This is used for the HOPF-01 antenna topology and torus knot
        classification, NOT as the electron's ground-state topology (which
        is the unknot, see generate_unknot_0_1).

        Args:
            radius (float): The characteristic radial scale of the defect.
            resolution (int): Number of coordinate points along the curve.

        Returns:
            np.ndarray: [N, 3] array of (x,y,z) spatial coordinates.
        """
        t = np.linspace(0, 2 * np.pi, resolution)

        # Standard parametric trefoil:
        # x = (sin(t) + 2sin(2t)) * scale
        # y = (cos(t) - 2cos(2t)) * scale
        # z = -sin(3t) * scale

        x = radius * (np.sin(t) + 2.0 * np.sin(2.0 * t))
        y = radius * (np.cos(t) - 2.0 * np.cos(2.0 * t))
        z = radius * (-np.sin(3.0 * t))

        # Normalize the structural scale so 'radius' controls the maximum bounding extent
        max_extent = np.max(np.sqrt(x**2 + y**2 + z**2))
        scale_factor = radius / max_extent

        coords = np.vstack((x, y, z)).T * scale_factor
        return coords

    @staticmethod
    def generate_borromean_6_3_2(radius: float, eccentricity: float = 1.6, resolution: int = 1000) -> list[np.ndarray]:
        """
        Generates the 3D parametric coordinates of the 6^3_2 Borromean Link.
        Consists of three mutually interlocking independent discrete rings.
        In the AVE framework, this defines the topological geometry of the Proton.

        Args:
            radius (float): The bounding scale of the overall structure.
            eccentricity (float): Flattening of the individual elliptical links.
            resolution (int): Points per individual ring.

        Returns:
            list of np.ndarray: A list containing three [N, 3] coordinate arrays,
                                one for each intersecting loop.
        """
        # The Borromean rings can be parametrized as 3 mutually perpendicular,
        # undulating ellipses that interlock without touching.

        t = np.linspace(0, 2 * np.pi, resolution)

        # Undulation parameters to guarantee the over/under braided weaving
        # (Standard L-G topological formulation)
        base_r = radius

        # Ring 1 (Primarily along X-Y plane, undulating in Z)
        x1 = base_r * np.cos(t)
        y1 = base_r * eccentricity * np.sin(t)
        z1 = base_r * 0.3 * np.cos(3 * t)
        ring_1 = np.vstack((x1, y1, z1)).T

        # Ring 2 (Primarily along Y-Z plane, undulating in X)
        x2 = base_r * 0.3 * np.cos(3 * t)
        y2 = base_r * np.cos(t)
        z2 = base_r * eccentricity * np.sin(t)
        ring_2 = np.vstack((x2, y2, z2)).T

        # Ring 3 (Primarily along Z-X plane, undulating in Y)
        x3 = base_r * eccentricity * np.sin(t)
        y3 = base_r * 0.3 * np.cos(3 * t)
        z3 = base_r * np.cos(t)
        ring_3 = np.vstack((x3, y3, z3)).T

        return [ring_1, ring_2, ring_3]

    @staticmethod
    def generate_torus_knot_2q(q: int, R: float = 1.0, r: float = 0.4, resolution: int = 2000) -> np.ndarray:
        """
        Generates the 3D parametric coordinates of a (2,q) torus knot.

        In the AVE framework, these classify the baryon spectrum:
          q=3:  Trefoil     (baryon branch resonance, 637 MeV)
          q=5:  Cinquefoil  (proton, 938 MeV)
          q=7:  Septafoil   (Δ(1232), 1232 MeV)
          q=9:              (Δ(1620), 1620 MeV)
          q=11:             (Δ(1950), 1950 MeV)
          q=13:             (N(2250), 2250 MeV)

        Args:
            q (int): Winding number (must be odd, ≥ 3).
            R (float): Major radius of the torus.
            r (float): Minor radius of the torus (tube center orbit).
            resolution (int): Number of coordinate points along the curve.

        Returns:
            np.ndarray: [N, 3] array of (x,y,z) spatial coordinates.
        """
        if q < 3 or q % 2 == 0:
            raise ValueError(f"q must be odd and >= 3, got {q}")

        t = np.linspace(0, 2 * np.pi, resolution)
        p = 2  # All baryons are (2,q) torus knots

        x = (R + r * np.cos(q * t)) * np.cos(p * t)
        y = (R + r * np.cos(q * t)) * np.sin(p * t)
        z = r * np.sin(q * t)

        coords = np.vstack((x, y, z)).T
        return coords

    @staticmethod
    def generate_screw_dislocation(
        pitch_count: int, length: float = 1.0, radius: float = 0.1, resolution: int = 2000
    ) -> np.ndarray:
        """
        Generates the 3D parametric coordinates of a screw dislocation
        (helical coil).

        In the AVE framework, neutrinos are pure torsional (screw) defects:
          c=5:  ν₁ (24 meV, paired with proton)
          c=7:  ν₂ (17 meV, paired with Δ(1232))
          c=9:  ν₃ (13 meV, paired with Δ(1620))

        The crossing number c sets the number of helical turns per
        wavelength — a tighter pitch means a heavier neutrino.

        Args:
            pitch_count (int): Number of helical turns (= crossing number c).
            length (float): Total axial length of the helix.
            radius (float): Radius of the helical coil.
            resolution (int): Number of coordinate points along the curve.

        Returns:
            np.ndarray: [N, 3] array of (x,y,z) spatial coordinates.
        """
        t = np.linspace(0, 2 * np.pi * pitch_count, resolution)
        pitch = length / pitch_count  # axial advance per turn

        x = radius * np.cos(t)
        y = radius * np.sin(t)
        z = pitch * t / (2 * np.pi)

        coords = np.vstack((x, y, z)).T
        return coords
