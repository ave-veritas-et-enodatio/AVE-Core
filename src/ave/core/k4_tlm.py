"""
K4-TLM: Native AVE Vacuum Lattice Dynamics Simulator
=====================================================

Transmission Line Matrix method strictly adhering to AVE Axiom 1:
"The vacuum is an LC resonant network with K4 node topology."

This module abandons the classical FDTD 6-port cubic mappings and Lattice
Boltzmann fluid hacks. Instead, it strictly tiles 4-port LC junctions
(tetrahedral embedding) forming a bipartite Diamond lattice.

1. True Topology: Nodes connect to exactly 4 neighbors in tetrahedral formation.
2. Native Chirality: The bipartite A/B structural embedding naturally twists
   polarization without ad-hoc rotation matrices.
3. Perfect Energy Conservation: S = 0.5 * 1 - I (exact unitary junction).
4. Axiom 4 Gravity: Mass is a static topological boundary where S -> 0, causing
   Lense-Thirring via Op14 non-reciprocal impedance gradients.

All constants derived correctly from `ave.core.constants`.
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import C_0, V_YIELD

# ═══════════════════════════════════════════════════════════════════════════
# EXACT SCATTERING MATRIX (Op5)
# ═══════════════════════════════════════════════════════════════════════════


def build_scattering_matrix(z_local=1.0):
    """
    Build the 4x4 unitary scattering matrix for a true K4/Diamond junction.

    Derived from Op5: S = (I + Y)^-1 (I - Y).
    For a 4-port equal admittance junction, this reduces exactly to:
        S_ij = 0.5 - delta_ij

    Args:
        z_local: The normalized impedance of the node (Z_node / Z_0).
                 For an unstrained vacuum, z_local = 1.0.
                 Under Axiom 4 saturation, z_local increases.

    Returns:
        S: 4x4 unitary matrix
    """
    N = 4
    if abs(z_local - 1.0) < 1e-10:
        return 0.5 * np.ones((N, N), dtype=float) - np.eye(N, dtype=float)

    # Impedance weighting for strained vacuum
    y = 1.0 / z_local
    S = np.zeros((N, N), dtype=float)
    y_total = N * y
    for i in range(N):
        for j in range(N):
            S[i, j] = 2.0 * y / y_total
            if i == j:
                S[i, j] -= 1.0
    return S


# ═══════════════════════════════════════════════════════════════════════════
# K4 (DIAMOND) LATTICE 3D
# ═══════════════════════════════════════════════════════════════════════════


class K4Lattice3D:
    """
    3D lattice of K4 nodes embedded in a Cartesian grid.

    Structure: Diamond Lattice (bipartite FCC).
    Nodes exist only where (x + y + z) is EVEN (FCC condition).
    They alternate into Type A and Type B sublattices.

    Tetrahedral connection vectors:
        Type A joins B via:
            p0: (+1, +1, +1)
            p1: (+1, -1, -1)
            p2: (-1, +1, -1)
            p3: (-1, -1, +1)
        Type B joins A via exact negative vectors.

    This ensures that Port `i` on node Type A connects seamlessly to
    Port `i` on the neighboring Type B node. No reciprocity mapping needed!
    """

    def __init__(self, nx, ny, nz, dx=1.0, nonlinear=False, pml_thickness=0):
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.dx = dx
        self.nonlinear = nonlinear
        self.pml_thickness = pml_thickness

        # Dispersion: wave crossing a 4-port junction is exactly c0 = dx / (dt * sqrt(2))
        self.c = float(C_0)
        self.dt = dx / (self.c * np.sqrt(2.0))

        # State arrays shape: (nx, ny, nz, 4 ports)
        self.V_inc = np.zeros((nx, ny, nz, 4), dtype=float)
        self.V_ref = np.zeros((nx, ny, nz, 4), dtype=float)

        # Sublattice Masks
        idx_grid = np.indices((nx, ny, nz))
        i, j, k = idx_grid[0], idx_grid[1], idx_grid[2]

        # Structure: Diamond Lattice on a Cartesian grid.
        # diamond lattice = two interpenetrating FCC lattices.
        # FCC 1 (Type A): i,j,k all have the SAME parity (all even or all odd).
        same_parity = ((i % 2) == (j % 2)) & ((j % 2) == (k % 2))
        self.mask_A = same_parity & ((i + j + k) % 4 == 0)

        # Type B is Type A shifted by (+1, +1, +1)
        # B nodes have (i-1)+j-1+k-1 % 4 == 0, so i+j+k-3 % 4 == 0 -> i+j+k % 4 == 3
        # Which implies i, j, k do NOT have the same parity. Actually, B is shifted by exactly (1,1,1).
        # To make it simple: Diamond lattice active sites are exactly those where A has sum(i,j,k) % 4 == 0 (with same parity)
        # and B has sum(i,j,k) % 4 == 3 (with same parity? No! if A is all even, + (1,1,1) is all odd. sum is 3.
        # Wait, FCC A: (0,0,0), (0,1,1) -> sum(0,1,1)=2!
        # If A nodes are standard FCC: (i+j)%2 == 0 AND (j+k)%2 == 0.
        self.mask_A = ((i + j) % 2 == 0) & ((j + k) % 2 == 0)

        # B nodes are A nodes shifted by (1,1,1)
        # If A has i+j even, j+k even -> B has (i-1+j-1) even -> i+j-2 even -> i+j even!
        # And B has i+k even -> B has i+k etc.
        # What distinguishes A and B?
        # A nodes have i,j,k all EVEN or all ODD. But sum for A is always exactly 0 mod 4 if all even? No! (1,1,1) has sum 3.
        # A subset of FCC is not enough.
        # Let's map Diamond via parity of (i+j+k).
        # Actually: BCC lattice is i+j+k even. We can just use BCC!
        # If we just use BCC, A nodes are i+j+k EVEN. B nodes are i+j+k ODD.
        # Wait: in BCC, neighbors of A are (+1,+1,+1), (+1,-1,-1), etc?
        # Let's use the explicit K4 tetrahedral links I defined:
        # p0=(+1,+1,+1), p1=(+1,-1,-1), p2=(-1,+1,-1), p3=(-1,-1,+1)
        # If A connects to B via exactly these 4 vectors, the graph is a set of disjoint Diamond lattices if we aren't careful.
        # Let's just activate the nodes reachable by these links from (0,0,0).
        # From (0,0,0), A nodes are generated by any 2 links. Sum of 2 links = (+2,0,0), (-2,0,0), etc.
        # So A nodes have ALL EVEN coordinates.
        # B nodes are A nodes + (+1,+1,+1) etc. So B nodes have ALL ODD coordinates.
        self.mask_A = (i % 2 == 0) & (j % 2 == 0) & (k % 2 == 0)
        self.mask_B = (i % 2 == 1) & (j % 2 == 1) & (k % 2 == 1)
        self.mask_active = self.mask_A | self.mask_B

        # ---------------------------------------------------------
        # SPONGE PML DEFINITION
        # ---------------------------------------------------------
        # A gradual macroscopic attenuation field A(x) that damps V_ref natively.
        # Operates as a Perfectly Matched Layer because it preserves local Z0
        # scattering integrity per Axiom 1, while smoothly dissipating kinetic
        # wave energy before the Cartesian topological discontinuity.
        self.pml_mask = np.ones((nx, ny, nz, 1), dtype=float)
        if self.pml_thickness > 0:
            d_x = np.minimum(i, self.nx - 1 - i)
            d_y = np.minimum(j, self.ny - 1 - j)
            d_z = np.minimum(k, self.nz - 1 - k)
            d = np.minimum(np.minimum(d_x, d_y), d_z)
            pml_region = d < self.pml_thickness
            # Quadratic rolloff from 1.0 (interior) to 0.0 (edge)
            attenuation = 1.0 - ((self.pml_thickness - d[pml_region]) / self.pml_thickness) ** 2
            self.pml_mask[pml_region, 0] = np.maximum(0.0, attenuation)

        # Store index arrays for boundary severing
        self._i, self._j, self._k = i, j, k

        # Precompute the baseline scattering matrix
        self._S_base = build_scattering_matrix(1.0)
        if self.nonlinear:
            # We need a field of S-matrices if cells can dynamically change impedance
            self._S_field = np.broadcast_to(self._S_base[None, None, None, :, :], (nx, ny, nz, 4, 4)).copy()

        self.timestep = 0

        # For backward compatibility with validation scripts
        self.z_local_field = np.ones((nx, ny, nz), dtype=float)

    def _scatter_all(self):
        """Matrix-vector multiply to scatter incident pulses into reflected pulses."""
        if self.nonlinear:
            # Op14 Impedance Saturation
            v_total = np.sqrt(np.sum(self.V_inc**2, axis=-1))
            # V_YIELD = √α × V_SNAP is the macroscopic onset of Axiom 4
            # nonlinearity. V_SNAP (511 kV) is the absolute topological
            # destruction limit; V_YIELD (43.65 kV) is where the saturation
            # operator begins to bite at engineering scales.
            v_yield = float(V_YIELD)
            strain = v_total / v_yield

            strained = strain > 0.01
            if np.any(strained):
                # S factor limits fields
                S_factor = np.sqrt(np.maximum(0.0, 1.0 - np.minimum(strain, 1.0) ** 2))
                z_strained = 1.0 / np.maximum(S_factor**0.25, 1e-6)
                self.z_local_field[strained] = z_strained[strained]

                for idx in zip(*np.where(strained & self.mask_active)):
                    self._S_field[idx] = build_scattering_matrix(z_strained[idx])

            self.V_ref = np.einsum("...ij,...j->...i", self._S_field, self.V_inc)

        else:
            # Native Axiom 2 linear vacuum topological scattering
            # Algebraically equivalent to exact multi-port symmetric matrix multiply
            # with 0.5 - I scattering arrays, but significantly O(N) optimized.
            self.V_ref = 0.5 * np.sum(self.V_inc, axis=-1, keepdims=True) - self.V_inc

        # Ensure inactive sites remain exactly 0
        self.V_ref[~self.mask_active] = 0.0

        # Apply the Sponge PML attenuation mask to dissipate out-bound waves
        if self.pml_thickness > 0:
            self.V_ref *= self.pml_mask

    def _connect_all(self):
        """
        Propagate pulses across the tetrapod connections.

        Port 0 vector: A->B is (+1,+1,+1). Therefore A gets B's reflected pulse from (+1,+1,+1).
        Port 1 vector: A->B is (+1,-1,-1).
        Port 2 vector: A->B is (-1,+1,-1).
        Port 3 vector: A->B is (-1,-1,+1).
        """
        new_inc = np.zeros_like(self.V_inc)

        # A nodes receive from B nodes
        # Port 0: B is at (i+1, j+1, k+1)
        B_ref_shifted_0 = np.roll(self.V_ref[..., 0], shift=(-1, -1, -1), axis=(0, 1, 2))
        new_inc[self.mask_A, 0] = B_ref_shifted_0[self.mask_A]

        # Port 1: B is at (i+1, j-1, k-1)
        B_ref_shifted_1 = np.roll(self.V_ref[..., 1], shift=(-1, 1, 1), axis=(0, 1, 2))
        new_inc[self.mask_A, 1] = B_ref_shifted_1[self.mask_A]

        # Port 2: B is at (i-1, j+1, k-1)
        B_ref_shifted_2 = np.roll(self.V_ref[..., 2], shift=(1, -1, 1), axis=(0, 1, 2))
        new_inc[self.mask_A, 2] = B_ref_shifted_2[self.mask_A]

        # Port 3: B is at (i-1, j-1, k+1)
        B_ref_shifted_3 = np.roll(self.V_ref[..., 3], shift=(1, 1, -1), axis=(0, 1, 2))
        new_inc[self.mask_A, 3] = B_ref_shifted_3[self.mask_A]

        # B nodes receive from A nodes
        # Port 0: A is at (i-1, j-1, k-1)
        A_ref_shifted_0 = np.roll(self.V_ref[..., 0], shift=(1, 1, 1), axis=(0, 1, 2))
        new_inc[self.mask_B, 0] = A_ref_shifted_0[self.mask_B]

        # Port 1: A is at (i-1, j+1, k+1)
        A_ref_shifted_1 = np.roll(self.V_ref[..., 1], shift=(1, -1, -1), axis=(0, 1, 2))
        new_inc[self.mask_B, 1] = A_ref_shifted_1[self.mask_B]

        # Port 2: A is at (i+1, j-1, k+1)
        A_ref_shifted_2 = np.roll(self.V_ref[..., 2], shift=(-1, 1, -1), axis=(0, 1, 2))
        new_inc[self.mask_B, 2] = A_ref_shifted_2[self.mask_B]

        # Port 3: A is at (i+1, j+1, k-1)
        A_ref_shifted_3 = np.roll(self.V_ref[..., 3], shift=(-1, -1, 1), axis=(0, 1, 2))
        new_inc[self.mask_B, 3] = A_ref_shifted_3[self.mask_B]

        # Boundary matching (Discrete Topological Bond Severing)
        # If PML is active, the domain is physically cut (not a torus).
        # We enforce a true geometric boundary by severing the links that np.roll wrapped:
        if self.pml_thickness > 0:
            i, j, k = self._i, self._j, self._k

            # Port 0: A receives from +1, B receives from -1
            new_inc[self.mask_A & ((i == self.nx - 1) | (j == self.ny - 1) | (k == self.nz - 1)), 0] = 0.0
            new_inc[self.mask_B & ((i == 0) | (j == 0) | (k == 0)), 0] = 0.0

            # Port 1: A receives from +1, -1, -1; B receives from -1, +1, +1
            new_inc[self.mask_A & ((i == self.nx - 1) | (j == 0) | (k == 0)), 1] = 0.0
            new_inc[self.mask_B & ((i == 0) | (j == self.ny - 1) | (k == self.nz - 1)), 1] = 0.0

            # Port 2: A receives from -1, +1, -1; B receives from +1, -1, +1
            new_inc[self.mask_A & ((i == 0) | (j == self.ny - 1) | (k == 0)), 2] = 0.0
            new_inc[self.mask_B & ((i == self.nx - 1) | (j == 0) | (k == self.nz - 1)), 2] = 0.0

            # Port 3: A receives from -1, -1, +1; B receives from +1, +1, -1
            new_inc[self.mask_A & ((i == 0) | (j == 0) | (k == self.nz - 1)), 3] = 0.0
            new_inc[self.mask_B & ((i == self.nx - 1) | (j == self.ny - 1) | (k == 0)), 3] = 0.0

        self.V_inc = new_inc

    def step(self):
        """Execute one complete timestep."""
        self._scatter_all()
        self._connect_all()
        self.timestep += 1

    def run(
        self,
        n_steps,
        source_x=None,
        source_y=None,
        source_z=None,
        source_func=None,
        probe_x=None,
        probe_y=None,
        probe_z=None,
        record_energy=True,
    ):
        """Run the simulation for n_steps."""
        probe_data = []
        energy_data = []
        times = []

        for step in range(n_steps):
            if source_func is not None and source_x is not None:
                amp = source_func(self.timestep)
                self.inject_point_source(source_x, source_y, source_z, amp)

            self.step()

            if probe_x is not None:
                val = self.get_field(probe_x, probe_y, probe_z)
                probe_data.append(val)

            if record_energy:
                energy_data.append(self.total_energy())

            times.append(self.timestep * self.dt)

        result = {"time": np.array(times)}
        if probe_data:
            result["probe"] = np.array(probe_data)
        if energy_data:
            result["energy"] = np.array(energy_data)
        return result

    def inject_point_source(self, x, y, z, amplitude):
        """Isotropic point source into an active node."""
        if 0 <= x < self.nx and 0 <= y < self.ny and 0 <= z < self.nz:
            if self.mask_active[x, y, z]:
                amp = amplitude / 2.0  # sqrt(4) = 2
                self.V_inc[x, y, z, :] += amp

    def get_field(self, x, y, z):
        if 0 <= x < self.nx and 0 <= y < self.ny and 0 <= z < self.nz:
            return np.sqrt(np.sum(self.V_inc[x, y, z] ** 2))
        return 0.0

    def get_energy_density(self):
        """Compute structural scalar energy |V|^2."""
        return np.sum(self.V_inc**2 + self.V_ref**2, axis=-1)

    def total_energy(self):
        return np.sum(self.get_energy_density())

    def get_helicity_density(self):
        """
        Compute helicity density h = A.B in the diamond lattice.

        The native chirality of the bipartite mapping naturally generates left
        and right circulating sub-fields without manual twists.
        """
        # Port 0,2 are right-handed. Port 1,3 are left-handed based on tetrahedral pairs.
        v_right = self.V_inc[..., 0] + self.V_inc[..., 2]
        v_left = self.V_inc[..., 1] + self.V_inc[..., 3]
        h = v_right**2 - v_left**2
        # Type B sees inverted coordinates, creating alternating topological helicity
        h[self.mask_B] *= -1.0
        return h


# ═══════════════════════════════════════════════════════════════════════════
# 2D COMPATIBILITY LATTICE
# ═══════════════════════════════════════════════════════════════════════════


class K4Lattice2D(K4Lattice3D):
    """
    2D validation slice of the true Diamond Lattice.
    Overrides z to always be 0 (an active layer).
    Since Diamond lattice is purely 3D, a true 2D cut is just a projection.
    For backward compatibility with 2D validation tests, we instantiate a thin
    3D lattice and slice it.
    """

    def __init__(self, nx, ny, alternating_chirality=False, dx=1.0, nonlinear=False, pml_thickness=0):
        # We need a depth of 4 to securely wrap 3D parity links natively
        super().__init__(nx, ny, 4, dx=dx, nonlinear=nonlinear, pml_thickness=pml_thickness)
        self.my_z = 2

    def inject_point_source(self, x, y, amplitude=0):
        # ensure it injects into an active node
        z = self.my_z
        if not self.mask_active[x, y, z]:
            z -= 1
        super().inject_point_source(x, y, z, amplitude)

    def get_field(self, x, y):
        z = self.my_z
        if not self.mask_active[x, y, z]:
            z -= 1
        return super().get_field(x, y, z)

    def get_field_array(self):
        z_slice = self.my_z
        active = self.mask_active[:, :, z_slice]
        field = np.zeros((self.nx, self.ny))
        field[active] = np.sqrt(np.sum(self.V_inc[:, :, z_slice, :] ** 2, axis=-1))[active]
        return field

    def get_helicity_density(self):
        h = super().get_helicity_density()
        return h[:, :, self.my_z]

    def inject_wire_current(self, wire_path, amplitude, direction_port=0):
        """Legacy compatibility for RF antenna injection."""
        z = self.my_z
        for idx in range(len(wire_path)):
            x, y = wire_path[idx]
            if not self.mask_active[x, y, z]:
                # find nearest active z
                z_target = z - 1
            else:
                z_target = z
            if 0 <= x < self.nx and 0 <= y < self.ny:
                self.V_inc[x, y, z_target, 0] += amplitude / 2.0
                self.V_inc[x, y, z_target, 2] += amplitude / 2.0
