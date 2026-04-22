"""
Topological Geometry Combiner: combiner.py
-------------------------------------------
Physics engine module for docking, rotating, and geometrically fusing
fundamental topological defects (Protons/Neutrons) into composite
Atomic Nuclei (Helium, Lithium, etc.).
"""

import numpy as np


class NucleonCombiner:
    @staticmethod
    def rotate_mesh(mesh: np.ndarray, angles: tuple[float, float, float]) -> np.ndarray:
        """
        Rotates a 3D coordinate mesh [N, 3] by given Euler angles (rx, ry, rz) in radians.
        """
        rx, ry, rz = angles

        # X-axis rotation matrix
        Rx = np.array([[1, 0, 0], [0, np.cos(rx), -np.sin(rx)], [0, np.sin(rx), np.cos(rx)]])

        # Y-axis rotation matrix
        Ry = np.array([[np.cos(ry), 0, np.sin(ry)], [0, 1, 0], [-np.sin(ry), 0, np.cos(ry)]])

        # Z-axis rotation matrix
        Rz = np.array([[np.cos(rz), -np.sin(rz), 0], [np.sin(rz), np.cos(rz), 0], [0, 0, 1]])

        # Composite rotation (Rz * Ry * Rx)
        R = Rz.dot(Ry).dot(Rx)

        # Apply transformation: coordinates are row vectors (N x 3), so we multiply by R.T
        return mesh.dot(R.T)

    @staticmethod
    def translate_mesh(mesh: np.ndarray, shift: tuple[float, float, float]) -> np.ndarray:
        """
        Translates a 3D coordinate mesh [N, 3] by a given spatial vector (dx, dy, dz).
        """
        translation_vector = np.array(shift)
        return mesh + translation_vector

    @classmethod
    def assemble_cluster(cls, base_nucleon_generator, placements: list[dict]) -> list[dict]:
        """
        Assembles a complex nucleus by instantiating multiple base defects
        and arranging them according to a list of placement dictionaries.

        Args:
            base_nucleon_generator: Function pointer (e.g., generate_borromean_6_3_2)
            placements: List of dicts, e.g., [{'shift': (1,0,0), 'rot': (0,pi/2,0), 'color': '#ff0000'}]

        Returns:
            list of dicts containing combined meshes and metadata.
        """
        assembled_cluster = []

        for p in placements:
            # Generate the pristine defect (usually returning a list of rings)
            raw_rings = base_nucleon_generator(radius=1.0)
            shifted_rings = []

            for ring in raw_rings:
                # 1. Rotate
                if "rot" in p:
                    ring = cls.rotate_mesh(ring, p["rot"])
                # 2. Translate
                if "shift" in p:
                    ring = cls.translate_mesh(ring, p["shift"])

                shifted_rings.append(ring)

            assembled_cluster.append(
                {
                    "mesh": shifted_rings,
                    "color": p.get("color", "#ffffff"),
                    "label": p.get("label", "Nucleon"),
                }
            )

        return assembled_cluster
