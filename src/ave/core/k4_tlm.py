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

Q-G47 SUBSTRATE-SCALE CLOSURE (Sessions 9-18, 2026-05-15 evening):
The K4 lattice + magic-angle operating point IS the substrate-scale instance
of A-034 (Universal Saturation-Kernel Strain-Snap Mechanism). The magic-
angle equation K(u_0*) = 2 G(u_0*) IS the substrate-scale expression of
S(A*) = 0 — i.e., the K4 lattice is "frozen at the saturation boundary"
where the substrate's linear response capacity vanishes and topological
reorganization (bound-state soliton stabilization) occurs.

Key results:
  - χ_K = 12 (K4 path-count multiplicity = |T| proper-rotation orbit size)
  - χ_G = 3 (T_t translational triplet dimension)
  - ℓ_c/ℓ_node ≈ √6 (Cosserat characteristic length / lattice spacing)
  - ξ_K2/ξ_K1 = 12 (axiom-level Cosserat moduli ratio, K4-symmetry-forced)

CONTINUOUS-SPRINGS FRAMING (per Grant 2026-05-15 evening): the discrete-bond
K4 lattice is a DISCRETIZATION of the continuous Cosserat micropolar field
(Axiom 1). Discrete bond stiffnesses (k_axial, k_θ) are samplings of the
continuous constitutive tensor (μ + κ, β + γ). The "bonds" between K4 nodes
are visualizations of the continuous stress field, not physical springs.

NAMESPACE CAVEAT: The "ξ" symbol used by Vol 3 Ch 1 for the Machian
impedance integral (ξ = 4π(R_H/ℓ_node)α⁻², magnitude ~10⁴³) is DISTINCT
from ξ_K1, ξ_K2 used at substrate scale here (Cosserat prefactors, O(1)).
Different scopes, same letter; explicitly disambiguated in
`manuscript/ave-kb/common/xi-topo-traceability.md`.

See: `manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md`
(KB canonical for Q-G47 Sessions 1-18 substrate-scale closure including
|T|=12 universality + ξ_K1, ξ_K2 namespace) +
`manuscript/backmatter/07_universal_saturation_kernel.tex` (A-034 canonical
catalog with substrate-scale K4 instance).
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import C_0, EPSILON_0, MU_0, P_C
from ave.core.constants import V_SNAP as _V_SNAP_MODULE
from ave.core.constants import V_YIELD, Z_0
from ave.core.universal_operators import universal_saturation

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

    def __init__(
        self,
        nx,
        ny,
        nz,
        dx=1.0,
        nonlinear=False,
        pml_thickness=0,
        op3_bond_reflection=False,
        use_memristive_saturation=False,
        tau_relax=None,
        V_SNAP=None,
    ):
        """
        Args:
            op3_bond_reflection: If True, applies Op3 reflection at each bond
                based on the local impedance mismatch between adjacent sites
                (Z_eff = Z_0/sqrt(S) per Op14). This extends the native TLM
                with strain-coupled wave reflection — the missing mechanism
                for bound solitons on the K4 substrate. Default False for
                backwards compatibility with existing validator scripts.
                See research/_archive/L3_electron_soliton/L3_PHASE3_SESSION_20260420
                handoff for the full AVE explanation.
            use_memristive_saturation: If True (opt-in), replaces the
                instantaneous Op14 `Z_eff = Z_0/√S_eq(V)` with the full
                memristive dynamics per doc 59_: integrates a per-cell
                saturation state S(t) via first-order relaxation
                `dS/dt = (S_eq(V) − S(t)) / τ_relax` with backward Euler.
                At ω·τ_relax << 1 (slow drive) this reduces to current Op14.
                Near yield or at simulation ω·τ_relax ~ 1 (Phase 5 regime),
                S(t) lags S_eq — giving the pinched-hysteresis loop.
                Default False preserves legacy behavior exactly.
            tau_relax: τ_relax = ℓ_node/c per Ax1+Ax3 derivation (doc 59_ §1).
                If None (default), computed from dx/c so units match self.dt.
                In SI mode: ≈ 3.34e-9 s. In native units (c=1, dx=1): = 1.0.
                Override only for tests exploring the fast/slow limit.
            V_SNAP: rupture voltage for saturation kernel normalization in
                `_update_z_local_field` and `_scatter_all`. If None (default),
                uses the module-level SI value (~511 kV). When K4Lattice3D is
                instantiated by CoupledK4Cosserat in engine natural-units
                context (engine V_SNAP=1), CoupledK4Cosserat passes 1.0 here
                so the saturation strain calculation matches the engine's
                V_SNAP convention. Pre-fix behavior (module-level always) was
                Flag-5e-A: K4 strain = V_inc / V_SNAP_SI gave ~10⁻⁶ at
                engine amp=0.9·V_SNAP_native, rendering saturation dormant
                in engine context. Default preserved for standalone SI usage.
        """
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.dx = dx
        self.nonlinear = nonlinear
        self.pml_thickness = pml_thickness
        self.op3_bond_reflection = op3_bond_reflection
        self.use_memristive_saturation = bool(use_memristive_saturation)
        # Saturation V_SNAP per Flag-5e-A fix. Default module-level for
        # standalone SI mode; CoupledK4Cosserat passes engine's natural-
        # unit value so strain calculation matches engine convention.
        self.V_SNAP = float(V_SNAP) if V_SNAP is not None else float(_V_SNAP_MODULE)

        # Dispersion: wave crossing a 4-port junction is exactly c0 = dx / (dt * sqrt(2))
        self.c = float(C_0)
        self.dt = dx / (self.c * np.sqrt(2.0))

        # τ_relax = ℓ_node / c = dx / c in whatever units dx, c are given.
        # Matches self.dt's unit system → dt/τ_relax = 1/√2 ≈ 0.707 is a
        # unit-system-invariant ratio. Engine override of self.c + self.dt
        # requires updating self.tau_relax to match (see CoupledK4Cosserat).
        self.tau_relax = float(tau_relax) if tau_relax is not None else (dx / self.c)

        # State arrays shape: (nx, ny, nz, 4 ports)
        self.V_inc = np.zeros((nx, ny, nz, 4), dtype=float)
        self.V_ref = np.zeros((nx, ny, nz, 4), dtype=float)

        # Per-bond magnetic flux linkage  Φ_link = ∫ V_bond dt
        # (Axiom 2, doc 54_ §3; Vol 4 Ch 1:223-227 memristance).
        # Stored at A-sites only — each entry is the flux on the directed
        # A→B bond along the corresponding port vector. B-sites mirror the
        # same physical bond. Accumulated in _connect_all between scatter
        # and port shift; bond voltage is V_avg = ½(V_ref_A + V_ref_B) per
        # doc 54_ §3/§9.2 so Φ counts both forward-going and backward-going
        # wave transit over the TLM time step dt.
        #
        # Read-only downstream of K4TLM; see ave.topological.vacuum_engine
        # BondObserver for diagnostics. Reset via engine.k4.reset_phi_link().
        self.Phi_link = np.zeros((nx, ny, nz, 4), dtype=float)

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

        # Memristive saturation state S(t). Always allocated for introspection;
        # only used in dynamics when use_memristive_saturation=True.
        # Initial state: S=1 (fully unsaturated), matches cold-vacuum V=0.
        # Per doc 59_ §9: dS/dt = (S_eq(V/V_SNAP) − S)/τ_relax.
        self.S_field = np.ones((nx, ny, nz), dtype=float)

    def _update_z_local_field(self):
        """Compute the local impedance at every active site from the current
        incident voltage magnitude. Needed by op3_bond_reflection to know
        the per-site Z_eff for bond-reflection calculations.

        Chain: |V_inc| -> strain A -> saturation S -> Z_eff = Z_0/sqrt(S).

        Normalization: strain A = |V_inc| / V_SNAP (absolute rupture voltage),
        NOT V_YIELD (engineering onset). This matches AVE's three-regime
        convention per the canonical reflection-profile three-regime convention:
          Regime I  (passband):    A < sqrt(2*alpha) ~ 0.121
          Regime II (transition):  sqrt(2*alpha) < A < sqrt(3)/2 ~ 0.866
          Regime III (stopband):   A > sqrt(3)/2, approaching A=1 (rupture)
        V_YIELD ~ sqrt(alpha) * V_SNAP falls inside Regime II, not at yield.
        """
        v_total = np.sqrt(np.sum(self.V_inc**2, axis=-1))
        v_snap = self.V_SNAP  # Flag-5e-A fix: use instance V_SNAP (defaults to module)
        strain = v_total / v_snap
        # S_eq = √(1 - A²) per Op2 (Ax4 saturation kernel).
        S_eq = np.sqrt(np.maximum(0.0, 1.0 - np.minimum(strain, 1.0) ** 2))

        if self.use_memristive_saturation:
            # Memristive Op14 (doc 59_ §9): S(t) lags S_eq with backward Euler
            # integration of dS/dt = (S_eq − S)/τ_relax.
            # S_{n+1} = (S_n·τ + dt·S_eq) / (τ + dt). Unconditionally stable.
            dt = self.dt
            tau = self.tau_relax
            self.S_field = (self.S_field * tau + dt * S_eq) / (tau + dt)
            S_used = self.S_field
        else:
            # Legacy instantaneous Op14: S = S_eq at each step.
            self.S_field = S_eq  # keep state consistent for introspection
            S_used = S_eq

        # Op14 canonical: Z_eff = Z_0 / sqrt(S), i.e., Z/Z_0 = 1/(1-A^2)^(1/4).
        # Prior code used S_factor**0.25 (= (1-A^2)^(1/8)) which is off by a factor
        # of 2 in the exponent; corrected to sqrt(S_factor) to match Op14.
        self.z_local_field = 1.0 / np.maximum(np.sqrt(S_used), 1e-6)
        # Inactive sites get baseline Z_0; they contribute nothing physically.
        self.z_local_field[~self.mask_active] = 1.0

    def _scatter_all(self):
        """Matrix-vector multiply to scatter incident pulses into reflected pulses."""
        if self.op3_bond_reflection:
            # Track z_local at every site (not just strained) so that
            # _connect_all can apply bond-level Op3 reflection. This is
            # lightweight (one pointwise operation on the full field).
            self._update_z_local_field()
        if self.nonlinear:
            # Op14 Impedance Saturation, anchored to V_SNAP per the three-regime
            # convention (the canonical reflection-profile three-regime convention):
            # regime boundaries at √(2α), √3/2, 1 all in units of V_SNAP.
            # V_YIELD falls inside regime II (at strain = √α ≈ 0.085), not at yield.
            # Corrected 2026-04-21 to match _update_z_local_field convention.
            v_total = np.sqrt(np.sum(self.V_inc**2, axis=-1))
            v_snap = self.V_SNAP  # Flag-5e-A fix: use instance V_SNAP
            strain = v_total / v_snap

            strained = strain > 0.01
            if np.any(strained):
                # Op2: S_eq = √(1 - A²), with A = strain/V_SNAP ∈ [0, 1]
                S_eq = np.sqrt(np.maximum(0.0, 1.0 - np.minimum(strain, 1.0) ** 2))

                if self.use_memristive_saturation:
                    # Memristive Op14 — S(t) lags S_eq with backward Euler
                    # (same integration used in _update_z_local_field).
                    # Doc 59_ §9. τ_relax = ℓ_node/c = 1 in native units.
                    dt = self.dt
                    tau = self.tau_relax
                    self.S_field = (self.S_field * tau + dt * S_eq) / (tau + dt)
                    S_used = self.S_field
                else:
                    self.S_field = S_eq
                    S_used = S_eq

                # Op14: Z_eff = Z_0/√S, i.e., (1-A²)^(-1/4) in natural units.
                # Previously used S_factor**0.25 which gave (1-A²)^(-1/8); off by 2×.
                z_strained = 1.0 / np.maximum(np.sqrt(S_used), 1e-6)
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

        If op3_bond_reflection is True, each bond applies Op3 reflection based
        on the impedance mismatch between the two endpoint sites' z_local.
        Unitary: V_inc_A[k] = Γ * V_ref_A[k] + T * V_ref_B[k], where
        Γ = (Z_B - Z_A)/(Z_B + Z_A), T = sqrt(1 - Γ²). Seen from B, the
        reflection is -Γ (opposite sign). Conserves total power.

        Before the port shift, accumulates per-bond magnetic flux linkage
        `Phi_link += V_avg · dt` where `V_avg = ½(V_ref_A + V_ref_B_shifted)`
        per doc 54_ §3. Flux is stored at A-sites only (canonical A→B
        direction); B-sites mirror the same physical bond.
        """
        new_inc = np.zeros_like(self.V_inc)

        # Port shifts: A-to-B direction vectors (each port)
        port_shifts = [
            (-1, -1, -1),  # Port 0: B is at (+1, +1, +1) → roll to bring B's val to A
            (-1, +1, +1),  # Port 1: B is at (+1, -1, -1)
            (+1, -1, +1),  # Port 2: B is at (-1, +1, -1)
            (+1, +1, -1),  # Port 3: B is at (-1, -1, +1)
        ]

        # ─────────────────────────────────────────────────────────────
        # Φ_link accumulation (doc 54_ §3). Runs before the port shift
        # so V_ref is still the just-scattered "during-transit" voltage.
        # Updated only at A-sites to avoid double-counting (A and B
        # share the same bond, indexed by the same port number).
        # ─────────────────────────────────────────────────────────────
        for port, shift_to_B in enumerate(port_shifts):
            V_A_ref = self.V_ref[..., port]
            V_B_shifted = np.roll(
                self.V_ref[..., port],
                shift=shift_to_B,
                axis=(0, 1, 2),
            )
            V_avg = 0.5 * (V_A_ref + V_B_shifted)
            # Accumulate flux linkage at A-sites only
            self.Phi_link[self.mask_A, port] += V_avg[self.mask_A] * self.dt

        if self.op3_bond_reflection:
            eps = 1e-12
            z_A_own = self.z_local_field  # local z at every site (A or B)
            for port, shift_to_B in enumerate(port_shifts):
                # Bring B's z_local and V_ref to A's location via roll
                z_B_at_A = np.roll(self.z_local_field, shift=shift_to_B, axis=(0, 1, 2))
                V_ref_B_at_A = np.roll(self.V_ref[..., port], shift=shift_to_B, axis=(0, 1, 2))
                V_ref_A_own = self.V_ref[..., port]
                gamma = (z_B_at_A - z_A_own) / (z_B_at_A + z_A_own + eps)
                T = np.sqrt(np.maximum(1.0 - gamma**2, 0.0))
                # At A-sites: V_inc = gamma * V_ref_A + T * V_ref_B (transmitted)
                new_inc[self.mask_A, port] = (gamma * V_ref_A_own + T * V_ref_B_at_A)[self.mask_A]

                # For B-sites receiving on the same port: the neighbor is the A-site
                # in the OPPOSITE direction.
                shift_to_A = tuple(-s for s in shift_to_B)
                z_A_at_B = np.roll(self.z_local_field, shift=shift_to_A, axis=(0, 1, 2))
                V_ref_A_at_B = np.roll(self.V_ref[..., port], shift=shift_to_A, axis=(0, 1, 2))
                V_ref_B_own = self.V_ref[..., port]
                # Seen from B: gamma_B = (Z_A - Z_B)/(Z_A + Z_B) = -gamma_AB
                gamma_B = (z_A_at_B - z_A_own) / (z_A_at_B + z_A_own + eps)
                T_B = np.sqrt(np.maximum(1.0 - gamma_B**2, 0.0))
                new_inc[self.mask_B, port] = (gamma_B * V_ref_B_own + T_B * V_ref_A_at_B)[self.mask_B]
        else:
            # Original pure-transmission connection (gamma = 0 everywhere)
            # A nodes receive from B nodes
            for port, shift_to_B in enumerate(port_shifts):
                B_ref_shifted = np.roll(self.V_ref[..., port], shift=shift_to_B, axis=(0, 1, 2))
                new_inc[self.mask_A, port] = B_ref_shifted[self.mask_A]
            # B nodes receive from A nodes (opposite shift)
            for port, shift_to_B in enumerate(port_shifts):
                shift_to_A = tuple(-s for s in shift_to_B)
                A_ref_shifted = np.roll(self.V_ref[..., port], shift=shift_to_A, axis=(0, 1, 2))
                new_inc[self.mask_B, port] = A_ref_shifted[self.mask_B]

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

    def reset_phi_link(self):
        """Reset per-bond flux linkage Phi_link to zero.

        Phi_link accumulates monotonically via _connect_all; this provides
        an explicit reset point (e.g., between sub-experiments in a driver
        script). Does not touch V_inc / V_ref.
        """
        self.Phi_link.fill(0.0)

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
