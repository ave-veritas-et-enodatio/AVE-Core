"""
A1-Cosserat Convergence Engine — Stage-1.5 α-FREE two-sector convergence
=========================================================================

The substrate-complete-engine spec's first two sectors (engine-capability-map.md
§4 DESIGN PROPOSAL, §5 build-order DAG), built α-FREE for the winding-emergence
lane (prereg: research/2026-06-16_stage15-alphafree-winding-emergence-prereg.md).

WHY THIS ENGINE EXISTS (the gap it closes):
  Stage-1 (boundary_mqj_selftrap_zwall_gate.py, e0d240e7) proved the coupled
  VacuumEngine3D returns c_eff(V)-STRUCTURAL-GAP: its scalar is the read-only
  PROJECTION v_scalar_from_v_inc(V_inc) (cross_sector_coupling.py:226) — NO
  independent A1 field — so its wall is the TRANSVERSE Meissner softening proxy
  Z_eff=√(S_μ/S_ε)≈Z₀, NOT the longitudinal A1 stiffening tank Z_tank→0
  (engine-capability-map.md:45,79).

  The PRIOR scalar-bulk single-grid arc (crystal_engine.py → graft-v2/3/4,
  2026-06-09/10) is a CLOSED NEGATIVE on the (2,3) WINDING: the scalar
  Master-Equation bulk has NO multi-component U(1)-fibre carrier; its shear-curl
  Ω_w carries the helicity 0-form CHARGE but not the knot WINDING (w_tor=0 AND
  w_pol=0; research/2026-06-09_crystal-engine_result.md §2,§5). That result
  itself SURFACED the synthesis (its §5, flagged for Grant): graft the conserved
  c_eff(V) cage onto the VECTOR K4/Cosserat micro-rotation sector — the
  multi-component carrier the scalar bulk lacks.

THIS ENGINE IS THAT SYNTHESIS (capability-map §3.1 firewall: irrotational ↮
winding → TWO coupled sectors):
  Sector A — the A1 cage (continuum-scalar FDTD): an INDEPENDENT, integrated,
    α-FREE longitudinal scalar field V(r,t) with the Master-Equation stiffening
    kernel ∂²V/∂t² = c_eff²(V)·∇²V, c_eff(V)=c₀·(1−A²)^(−¼)→∞, A=|V|/V_yield with
    V_yield=1.0 (GENERIC natural unit, NOT √α·V_snap). This is the longitudinal
    Z_tank=√(L/C_comp)→0 stiffening cage the projection could NOT host.
  Sector B — the winding (K4-tetrahedral Cosserat): the VECTOR CosseratField3D
    (u, omega) micro-rotation on the K4 diamond A/B sublattice (omega_yield=π,
    k_hopf=π/3 = the (2,3)/Q_H=6 anchor) — the U(1)-fibre carrier the scalar
    bulk lacked. α-FREE.
  Shared-front coupling — ONE conserved Hamiltonian term (energize-LOCK, NOT a
    one-way pump; the crystal_engine ADD-2 pattern, the genesis-24 detonation
    fixed): the A1 saturation FRONT g_front(A_V) localizes a gyrotropic exchange
    between the bulk-velocity ∂_tV and the Cosserat micro-rotation rate — CP10
    boundary-localized, NOT a bulk-volume force, so no |ω| blow-up.

α-FREE IS LOAD-BEARING. No ALPHA / KAPPA_CHIRAL / V_yield=√α·V_snap /
delta_lock_fraction=α enters ANY update equation. The non-α geometric inputs
(NU_VAC=2/7, R_II=√3/2, omega_yield=π, k_hopf=π/3, κ̃=6/5=pq/(p+q)) are
ave-canonical-source / topology-derived.

TWO-GRID RECONCILIATION (the core challenge):
  Both sectors share the same N³ Cartesian extent, but live on DIFFERENT grids:
  Sector A's scalar field lives on EVERY cell (continuum FDTD); Sector B's
  Cosserat field lives ONLY on the K4 diamond A/B sublattice (mask_alive). The
  coupling restricts the exchange to alive sites and to the saturation front
  (CP10), and uses the EXACT velocity-pair rotation (conservative) so the shared
  front exchanges energy reversibly between the two grids.
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import NU_VAC, R_II
from ave.core.master_equation_fdtd import MasterEquationFDTD
from ave.topological.cosserat_field_3d import CosseratField3D
from ave.topological.vacuum_engine import _cosserat_A_squared


class A1CosseratConvergenceEngine:
    """α-FREE two-sector convergence engine: an INDEPENDENT c_eff(V) longitudinal
    A1 cage (Sector A, continuum-scalar FDTD) coupled to the VECTOR Cosserat
    micro-rotation winding carrier (Sector B, K4-tetrahedral) through ONE
    conserved saturation-front exchange term.

    Built incrementally (Stage-1.5 build-order DAG):
      Layer (a): Sector A self-traps standalone (longitudinal Z_tank→0).
      Layer (b): Sector A ⊗ Sector B coupled; stable (no blow-up, ledger flat).
      Layer (c): generic precursor seed; α-free emergence probe.
    """

    def __init__(
        self,
        N: int,
        dx: float = 0.5,
        V_yield: float = 1.0,
        c0: float = 1.0,
        cfl_safety: float = 0.30,
        pml_thickness: int = 4,
        A_cap: float = 0.99,
        S_min: float = 0.05,
        kappa_tilde: float = 6.0 / 5.0,
        front_center: float = R_II,
        front_width: float = 0.18,
        couple_on: bool = True,
        coupling_support: str = "front",
    ):
        """
        Args (Sector A inherits MasterEquationFDTD's; new ones are coupling):
            V_yield:      saturation field per node — 1.0 GENERIC natural unit
                          (α-FREE; NOT √α·V_snap). Load-bearing.
            kappa_tilde:  shared-front gyrotropic exchange coupling = pq/(p+q)=6/5
                          (the (2,3) topology; α-FREE — NOT κ_chiral=1.2α).
            front_center: A_V-value of the saturation front where the exchange
                          engages — R_II=√3/2 (the Non-Linear→Saturated boundary;
                          α-FREE geometric; CP10 boundary-localized).
            front_width:  Gaussian half-width of that shell in A_V-units.
            couple_on:    master switch for the shared-front exchange. False ⇒
                          the two sectors evolve independently (Layer-(a) baseline
                          + the converter-OFF control for energize-LOCK proofs).
        """
        self.N = int(N)
        self.dx = float(dx)
        self.V_yield = float(V_yield)
        self.c0 = float(c0)
        self.A_cap = float(A_cap)
        self.S_min = float(S_min)
        self.kappa_tilde = float(kappa_tilde)
        self.front_center = float(front_center)
        self.front_width = float(front_width)
        self.couple_on = bool(couple_on)
        if coupling_support not in ("front", "saturated_interior"):
            raise ValueError("coupling_support must be 'front' or 'saturated_interior'")
        self.coupling_support = coupling_support
        self.pml_thickness = int(pml_thickness)

        # Branch-speed tie (α-free, geometric): the bulk c_L and the transverse
        # Cosserat shear speed relate by ν_vac=2/7 at K=2G (c_L²/c_T²=10/3).
        # Used only to set a consistent Cosserat CFL relative to the bulk.
        self.cL2_over_cT2 = 2.0 * (1.0 - NU_VAC) / (1.0 - 2.0 * NU_VAC)

        # ── Sector A — the INDEPENDENT α-free c_eff(V) longitudinal A1 cage ──
        # The validated v14 Mode-I bulk-trap kernel as a STANDALONE integrated
        # scalar field (NOT a projection). This is the longitudinal Z_tank→0
        # stiffening cage VacuumEngine3D's v_scalar_from_v_inc could not host.
        self.A = MasterEquationFDTD(
            N=self.N, dx=self.dx, V_yield=self.V_yield, c0=self.c0,
            cfl_safety=cfl_safety, pml_thickness=self.pml_thickness,
            A_cap=self.A_cap, S_min=self.S_min,
        )
        # The bulk timestep (Sector A governs the global outer dt; the faster
        # branch under saturation, c_eff_max=c0/√S_min, already set it in A.dt).
        self.dt = float(self.A.dt)

        # ── Sector B — the VECTOR K4/Cosserat micro-rotation winding carrier ──
        # The U(1)-fibre / multi-component carrier the scalar bulk lacked
        # (crystal_engine_result.md §5). α-FREE (omega_yield=π, epsilon_yield=1).
        # Lives on the K4 diamond A/B sublattice (mask_alive) — the second grid.
        self.B = CosseratField3D(
            self.N, self.N, self.N, dx=self.dx,
            use_saturation=True, pml_thickness=self.pml_thickness,
        )
        # Sub-cycle the Cosserat sector if its CFL is tighter than the bulk dt
        # (the two-grid temporal reconciliation: each grid integrated stably).
        c_omega_max = self.c0 / np.sqrt(self.cL2_over_cT2 * self.S_min)
        dt_cos = cfl_safety * self.dx / (c_omega_max * np.sqrt(3.0))
        # Cosserat sub-cycle: enough sub-steps that the Cosserat CFL is satisfied
        # at the (smaller) bulk outer dt. The force-based coupling (frozen once
        # per outer step) does NOT need an additionally-fine exchange sub-cycle.
        self.n_sub_cos = max(1, int(np.ceil(self.dt / max(dt_cos, 1e-30))))
        self.dt_sub_cos = self.dt / self.n_sub_cos

        self.time = 0.0
        self.step_count = 0
        self.coupling_work = 0.0  # accumulated shared-front exchange work (witness)

        # interior mask shared by both grids (PML-excluded; A-Rule 10 corollary)
        self._interior = self._build_interior_mask()

    # ── Convenience read-throughs to Sector A's field (the A1 cage) ──
    @property
    def V(self) -> np.ndarray:
        return self.A.V

    @property
    def V_prev(self) -> np.ndarray:
        return self.A.V_prev

    @property
    def omega(self) -> np.ndarray:
        return self.B.omega

    @property
    def omega_dot(self) -> np.ndarray:
        return self.B.omega_dot

    def _build_interior_mask(self) -> np.ndarray:
        """PML-excluded interior cells (A-Rule 10 corollary — PML cells are
        frozen-absorbing artifact, never interior physics)."""
        p = self.pml_thickness
        m = np.zeros((self.N, self.N, self.N), dtype=bool)
        m[p:self.N - p, p:self.N - p, p:self.N - p] = True
        return m

    # ══════════════════════════════════════════════════════════════════════
    # SECTOR A — the α-free A1 c_eff(V) longitudinal cage (Layer (a))
    # ══════════════════════════════════════════════════════════════════════
    def strain_A_V(self) -> np.ndarray:
        """A_V = |V|/V_yield — the longitudinal-bulk strain (the A1 operating
        point along the Axiom-4 kernel)."""
        return np.abs(self.A.V) / self.V_yield

    def saturation_S(self) -> np.ndarray:
        """S(A_V) = √(1−A_V²), clipped to [S_min, 1] (the Axiom-4 kernel on the
        A1 longitudinal field)."""
        return self.A.saturation_kernel(self.A.V)

    def Z_tank_longitudinal(self) -> np.ndarray:
        """THE LONGITUDINAL A1 TANK IMPEDANCE Z_tank = √(L/C_comp) per cell —
        the load-bearing Stage-1.5 readout (phase-space coordinate, A46), NOT a
        real-space field magnitude.

        Substrate-native derivation (INVARIANT-S2 Q1=B, Grant-ratified): the A1
        longitudinal bond compliance is C_comp = C₀/S(A_V) (the stretch-reactance
        that SOFTENS/diverges as the bond yields). With the bond inductance L=L₀
        fixed (a static stretch has no ∂B/∂t to load the μ-sector), the
        longitudinal tank impedance is
            Z_tank/Z₀ = √(L/C_comp)/√(L₀/C₀) = √(C₀/C_comp) = √S(A_V).
        → 0 as A_V → 1 (the saturated core stiffens; C_comp→∞ ⇒ Z_tank→0). This
        is the TRUE stiffening confinement the transverse Meissner proxy
        (Z_eff=√(S_μ/S_ε)≈Z₀) could not show. DISTINCT from the transverse-T2
        wave impedance √(μ/ε) (the two orthogonal reactances, master-equation.md:20).
        """
        return np.sqrt(self.saturation_S())

    def S_mu_S_eps_split(self) -> dict:
        """The transverse S_μ/S_ε split (correction 3), reported ALONGSIDE the
        longitudinal Z_tank so the two orthogonal reactances are not conflated.

        On the A1-only longitudinal cage there is no independent μ/ε drive — a
        static longitudinal stretch loads the ε/capacitive (compliance) sector
        only (S_ε = S(A_V); the bench-LCR C_diel = ε_eff·A/d ∝ S rolls off),
        while the μ/microrotational sector is UNLOADED on this sector (S_μ = 1,
        no ∂B/∂t). So the TRANSVERSE Meissner proxy here is
            Z_eff/Z₀ = √(S_μ/S_ε) = √(1/S) ≥ 1  (RISES — the softening proxy,
        the exact reading Stage-1's coupled VacuumEngine3D returned ≈Z₀/↑). The
        LONGITUDINAL Z_tank=√S (above) is the orthogonal reactance that FALLS.
        Reporting both makes the orthogonality explicit (INVARIANT-S2)."""
        S = self.saturation_S()
        interior = self._interior
        S_eps = S
        S_mu = np.ones_like(S)
        Z_eff_transverse = np.sqrt(S_mu / np.maximum(S_eps, self.S_min))
        Z_tank_long = np.sqrt(S)
        return {
            "S_eps_min_interior": float(S_eps[interior].min()),
            "S_mu_interior": 1.0,
            "Z_eff_transverse_max_interior": float(Z_eff_transverse[interior].max()),
            "Z_tank_long_min_interior": float(Z_tank_long[interior].min()),
        }

    # ── Seeds (CP8 — generative precursors, NOT planted finished electron) ──
    def seed_bulk_blob(self, center, sigma, frac):
        """Seed a sub-yield localized longitudinal blob (A_V=frac at the peak) —
        a generic precursor mass (NOT a planted (2,3)). Stationary start
        (∂_tV=0) so the self-trap forms from the c_eff(V) dynamics, not from an
        injected velocity. Used for the Layer-(a) standalone self-trap."""
        cx, cy, cz = center
        i, j, k = np.indices((self.N, self.N, self.N))
        r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2) * self.dx
        env = 1.0 / np.cosh(r / sigma)
        amp = float(frac) * self.V_yield
        self.A.V[:] = amp * env
        self.A.V_prev[:] = self.A.V.copy()

    def seed_cosserat_photon(self, center, sigma, wavelength, amplitude,
                             direction=(1, 0, 0), helicity=1.0, axis=2):
        """CP8 — seed a GENERIC transverse helical ω-photon on the VECTOR
        Cosserat sector with NO planted (2,3). The winding (if any) must
        SELF-FORM from the coupled dynamics. Delegates to the validated
        CosseratField3D seeder."""
        self.B.initialize_gaussian_wavepacket_omega(
            center, sigma=sigma, direction=direction, wavelength=wavelength,
            amplitude=amplitude, axis=axis, helicity=helicity,
        )

    # ── Sector-A energy ledger (the candidate m_e c² latent heat) ──
    def bulk_energy_conserved(self) -> float:
        """The variable-coefficient conserved energy of the A1 cage:
        E = ½∫(∂_tV)²/c_eff² + ½∫|∇V|²  (kinetic weighted by 1/c_eff² — the
        nonlinear-breather-correct form; the naive ½c0²|∇V|² grows spuriously).
        PML-excluded (A-Rule 10)."""
        pV = (self.A.V - self.A.V_prev) / self.A.dt
        c_eff_sq = self.A.c_eff_squared(self.A.V)
        gx, gy, gz = np.gradient(self.A.V, self.dx)
        dens = 0.5 * pV**2 / np.maximum(c_eff_sq, 1e-30) + 0.5 * (gx**2 + gy**2 + gz**2)
        return float((dens * self._interior).sum())

    def bulk_energy_naive(self) -> float:
        """E_V = ½∫(∂_tV)² + ½∫c0²(∇V)² (the simple ledger — reported for the
        boundedness / detonation gate, genesis-24-comparable). PML-excluded."""
        pV = (self.A.V - self.A.V_prev) / self.A.dt
        gx, gy, gz = np.gradient(self.A.V, self.dx)
        dens = 0.5 * pV**2 + 0.5 * (self.c0**2) * (gx**2 + gy**2 + gz**2)
        return float((dens * self._interior).sum())

    def step_sector_A_only(self):
        """Advance ONLY Sector A (the standalone c_eff(V) cage) — the Layer-(a)
        self-trap, byte-equivalent to the known-positive MasterEquationFDTD
        breather. No Cosserat coupling. The numerical-adequacy reference."""
        self.A.step()
        self.time += self.A.dt
        self.step_count += 1

    # ══════════════════════════════════════════════════════════════════════
    # SHARED-FRONT COUPLING — the two-grid reconciliation (Layer (b))
    # ══════════════════════════════════════════════════════════════════════
    def _front_window(self) -> np.ndarray:
        """g_coupling(A_V): the support where the cross-sector exchange engages,
        restricted to alive K4 sites (the second grid; two-grid reconciliation).

        coupling_support='front' (DEFAULT, CP10 boundary-localized): a thin band
          at A_V≈R_II=√3/2 (the Non-Linear→Saturated boundary). Zero in vacuum
          and in the deep frozen core — NOT a bulk-volume coupling (anti-pump).
          FINDING (Layer b): this shell and the winding curl Ξ have DISJOINT
          support (the curl lives at the trap interior, not the front), so the
          bulk source f_V=−κ̃·g·Ξ ≡ 0 — the front coupling is inert on the winding.

        coupling_support='saturated_interior' (controlled variant, labeled): a
          smooth ramp over the SATURATED region (A_V above the front center),
          so the coupling support OVERLAPS the winding curl at the trap interior.
          Tests whether interior-overlap coupling is stable (the front-vs-interior
          design fork the Layer-b finding surfaces — for Grant/auditor, NOT an
          implementer pivot)."""
        A_V = self.strain_A_V()
        if self.coupling_support == "front":
            g = np.exp(-((A_V - self.front_center) ** 2) / (2.0 * self.front_width**2))
        else:  # saturated_interior: smooth sigmoid ramp on for A_V ≳ front_center
            g = 0.5 * (1.0 + np.tanh((A_V - self.front_center) / self.front_width))
        return g * self.B.mask_alive.astype(g.dtype)

    def _axial_unit(self) -> int:
        """The Cosserat micro-rotation component the bulk reactance couples to —
        the axial (propagation-direction) micro-rotation ω_z, the U(1)-fibre /
        poloidal-'3' carrier (the carrier the SCALAR bulk lacked,
        crystal_engine_result.md §5). Fixed to axis z (the photon seed's
        helicity axis); chirality sign parked (achiral-OK)."""
        return 2

    def _cosserat_axial_curl(self) -> np.ndarray:
        """Ξ = (∇×ω)·n̂ along the photon axis n̂=ẑ — the Cosserat micro-rotation
        CURL, the poloidal-'3' / U(1)-fibre carrier the SCALAR bulk lacked. For
        n̂=ẑ: (∇×ω)_z = ∂_x ω_y − ∂_y ω_x. This is a POSITION-like field (a
        spatial derivative of ω), so coupling the bulk POTENTIAL V to it gives a
        CONSERVATIVE potential coupling (forces on accelerations — the
        crystal_engine ADD-2 energize-LOCK structure), NOT a velocity rotation
        across two mismatched-time integrators (which pumped)."""
        wy_x = (np.roll(self.B.omega[..., 1], -1, axis=0) - np.roll(self.B.omega[..., 1], 1, axis=0)) / (2.0 * self.dx)
        wx_y = (np.roll(self.B.omega[..., 0], -1, axis=1) - np.roll(self.B.omega[..., 0], 1, axis=1)) / (2.0 * self.dx)
        return wy_x - wx_y

    def _coupling_forces(self):
        """The CONSERVATIVE shared-front coupling — ONE Hamiltonian term
            H_c = κ̃ ∫ g_front(A_V) · V · Ξ  d³r,   Ξ = (∇×ω)·ẑ,
        with g_front>0 ONLY at the saturation front (CP10 boundary; α-free κ̃=6/5).
        The reciprocal forces are its functional derivatives (energize-LOCK — the
        continuum energy cancellation is EXACT; the genesis-24/velocity-rotation
        pump AVOIDED because BOTH coupled quantities are POSITION-like, so the
        force enters each sector's OWN Verlet acceleration at a consistent
        time-centering):
            f_V       = −δH_c/δV   = −κ̃ g Ξ        (sources V from the winding curl)
            f_ω_y     = −δH_c/δω_y = −κ̃ ∂_x(g V)   (reciprocal back-reaction onto ω,
            f_ω_x     = −δH_c/δω_x = +κ̃ ∂_y(g V)    from δΞ/δω = the curl adjoint)
        Returns (f_V scalar field, f_omega (...,3) vector field). f_ω lives on
        the K4 alive sublattice via g_front's mask (two-grid spatial restriction).
        """
        g = self._front_window()                 # already masked to alive sites
        gV = g * self.A.V
        Xi = self._cosserat_axial_curl()
        f_V = -self.kappa_tilde * g * Xi
        f_omega = np.zeros_like(self.B.omega)
        dgV_dx = (np.roll(gV, -1, axis=0) - np.roll(gV, 1, axis=0)) / (2.0 * self.dx)
        dgV_dy = (np.roll(gV, -1, axis=1) - np.roll(gV, 1, axis=1)) / (2.0 * self.dx)
        f_omega[..., 1] = -self.kappa_tilde * dgV_dx
        f_omega[..., 0] = +self.kappa_tilde * dgV_dy
        return f_V, f_omega

    def _coupling_energy(self) -> float:
        """H_c = κ̃∫ g·V·Ξ over the interior (the conversion ledger term, kept
        for the joint H = E_bulk + H_cosserat + H_c conservation check)."""
        g = self._front_window()
        Xi = self._cosserat_axial_curl()
        return float((self.kappa_tilde * g * self.A.V * Xi * self._interior).sum())

    def step_coupled(self):
        """One coupled outer step (Layer (b) two-grid reconciliation) — the
        CONSERVATIVE force-based coupling (crystal_engine ADD-2 energize-LOCK
        structure, NOT the pumping velocity-rotation):

          1. compute the reciprocal front-coupling forces (f_V, f_ω) from the
             SINGLE Hamiltonian term H_c = κ̃∫ g·V·Ξ (functional derivatives);
          2. advance Sector A (c_eff(V) cage) one bulk Verlet step WITH f_V added
             to its acceleration (the winding curl sources the bulk at the front);
          3. advance Sector B (vector Cosserat) its sub-cycled Verlet steps WITH
             f_ω added each sub-step (the bulk back-reacts onto ω at the front).

        Both forces enter each sector's OWN Verlet acceleration — a conservative
        potential coupling at consistent time-centering. Two-grid reconciliation:
        TEMPORAL = Cosserat sub-cycled at its own stable dt; SPATIAL = the
        coupling forces are front-localized + alive-masked (CP10, two grids)."""
        f_V, f_omega = self._coupling_forces()
        if self.couple_on:
            # Sector A: leapfrog with the extra front source on the acceleration.
            c_eff_sq = self.A.c_eff_squared(self.A.V)
            L = self.A._laplacian(self.A.V)
            a_V = c_eff_sq * L + f_V
            V_new = 2.0 * self.A.V - self.A.V_prev + (self.A.dt**2) * a_V
            V_new *= self.A.damping
            self.A.V_prev = self.A.V.copy()
            self.A.V = V_new
            self.A.time += self.A.dt
            self.A.step_count += 1
        else:
            self.A.step()

        # Sector B: sub-cycled Verlet; inject the (frozen-this-outer-step) f_ω as
        # a constant front force each sub-step via a direct half-kick wrapper
        # (a_ω += f_ω/I_ω). The force is frozen once per outer step (the
        # moving-front anti-pump cadence — recomputing it every sub-step pumps,
        # cosserat step docstring §7), matching the bulk's once-per-outer cadence.
        a_omega_ext = (f_omega / self.B.I_omega) if self.couple_on else None
        for _ in range(self.n_sub_cos):
            self._cosserat_substep_with_force(a_omega_ext)

        self.coupling_work += float((self._coupling_energy()))
        self.time += self.A.dt
        self.step_count += 1

    def _cosserat_substep_with_force(self, a_omega_ext):
        """One Cosserat velocity-Verlet sub-step with an EXTERNAL constant ω-force
        a_omega_ext (the frozen front back-reaction) added to both half-kicks —
        a conservative augmentation of CosseratField3D.step (the force is a
        gradient of the potential H_c, so it integrates conservatively in Verlet).
        If a_omega_ext is None (couple_off), reduces to the bare Cosserat step."""
        if a_omega_ext is None:
            self.B.step(dt=self.dt_sub_cos)
            return
        dt = self.dt_sub_cos
        a_u, a_w = self.B._accel()
        a_w = a_w + a_omega_ext
        self.B.u_dot = self.B.u_dot + 0.5 * dt * a_u
        self.B.omega_dot = self.B.omega_dot + 0.5 * dt * a_w
        self.B._zero_velocities_outside_alive()
        self.B.u = self.B.u + dt * self.B.u_dot
        self.B.omega = self.B.omega + dt * self.B.omega_dot
        self.B._zero_outside_alive()
        a_u_new, a_w_new = self.B._accel()
        a_w_new = a_w_new + a_omega_ext
        self.B.u_dot = self.B.u_dot + 0.5 * dt * a_u_new
        self.B.omega_dot = self.B.omega_dot + 0.5 * dt * a_w_new
        self.B._zero_velocities_outside_alive()
        self.B.time += dt

    # ── coupled-system witnesses (ave-conserved-vs-pumped) ──
    def omega_max_interior(self) -> float:
        """peak |ω| over alive interior sites (the C-state blow-up witness)."""
        w = np.asarray(self.B.omega) * self._interior[..., None]
        return float(np.abs(w).max())

    def omega_dot_max_interior(self) -> float:
        """peak |ω̇| (the L-state of the reactance pair, A-Rule 10)."""
        wd = np.asarray(self.B.omega_dot) * self._interior[..., None]
        return float(np.abs(wd).max())

    def total_hamiltonian(self) -> float:
        """The FULL coupled Hamiltonian witness: the Cosserat sector's own
        total_hamiltonian() (kinetic + gradient potential, NOT sum(ω²)) PLUS the
        bulk cage's conserved energy. ave-conserved-vs-pumped: a flat/decaying
        ledger = passive (energize-LOCK); a climbing ledger = PUMP."""
        return float(self.B.total_hamiltonian()) + self.bulk_energy_conserved()

