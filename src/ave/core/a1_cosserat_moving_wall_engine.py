"""
A1-Cosserat MOVING-WALL Engine — Stage-1.6 CP8-safe OPEN route (α-FREE)
=======================================================================

Extends the Stage-1.5 α-free two-sector convergence engine
(a1_cosserat_convergence_engine.py) by adding an EXTERNAL moving Γ=−1 /
Op17-bounded reflecting wall ON SECTOR B (the photon's OWN Cosserat-ω sector).

WHY THIS ENGINE EXISTS (the gated question it answers):
  Stage-1.5 (c) (research/2026-06-16_stage15-alphafree-winding-emergence_result.md)
  proved an INTERNAL SPECTATOR cage cannot confine a *propagating* photon: the A1
  deep-saturated core is pure A1 dilatation = irrotational (∇×∇V≡0,
  engine-capability-map.md:57), so the winding curl Ξ=(∇×ω)·ẑ is structurally zero
  there, AND a propagating photon's curl is an extended axial structure that never
  co-locates with the compact cage core — it radiates out (|ω| 0.3→0.029) before
  the cage breathes deep. Result: f_V≡0, coupling_work=0 (the energize-LOCK loop
  is INERT — a STRUCTURAL null, adversarially confirmed, not a bug).

  THE STAGE-1.6 HYPOTHESIS: can an EXTERNAL moving Γ=−1 wall on SECTOR B confine
  the propagating photon so its winding curl CO-LOCATES with the cage core and the
  loop closes (coupling_work≠0, f_V≠0) — WITHOUT changing the seed (CP8-safety)?

THE ONE CHANGE vs Stage-1.5 (c): add the wall. The seed is UNCHANGED (the SAME
generic transverse ω-photon + sub-yield bulk; re-seeding a confined/co-located/
pre-wound precursor would install the answer = the held-BC C′ plant hazard).

THE WALL (precedent: analysis/2026-06-06-saturation-tir-moving-boundary, VERDICT
(II) — the moving Γ=−1 wall DID confine the Cosserat-ω photon, loc 0.97→0.94, held
vs both collapse and dispersion):
  Sector B is constructed with use_impedance_boundary=True (the Op3 Γ=−1 node-clamp
  on the μ-side saturation front) + impedance_implicit=True (the energy-conserving
  Strang/exact-LC-rotation integrator — the §7-fixed anti-pump path).

α-FREE ROUTING (load-bearing — Checkpoint 8/α-free inherited):
  The precedent's _impedance_gamma_field routes the chirality bias through
  KAPPA_CHIRAL_ELECTRON = α·κ̃_e (α-BEARING). This engine OVERRIDES that method at
  the instance level to kappa_chiral=0 (the symmetric/achromatic μ/ε limit), so the
  μ-side short is driven by the GENERIC curvature saturation A²_μ_base = κ²/ω_yield²
  (geometric, α-free) ONLY. Pre-build probe: α-free Γ_min=−0.084 ≈ α-chiral
  Γ_min=−0.083 — the α-chiral term is an α-scale perturbation; the wall is
  geometric. This is the same routing discipline Stage-1.5 used to route around the
  α-bearing VacuumEngine3D paths.

CP10 (Op17-bounded BC, not bulk force): the wall is |Γ|→1 as A→1. AMENDMENT-4
(2026-06-16, #273 ww8x96sci): realized as the K4-TLM UNITARY-SCATTER reflector
(impedance_unitary=True, default) — at the wall cells the (ω, ω̇/Ω₀) reactance
pair is decomposed into incident/reflected characteristic amplitudes and rotated
through the ORTHOGONAL [[Γ_w,T_w],[T_w,−Γ_w]] (Γ_w=relu(−Γ)∈[0,1], Γ_w²+T_w²=1),
so |output|=|input| EXACTLY — energy-honest, |ω|-bounded BY CONSTRUCTION, NO pump.
This SUPERSEDES the prior reactive node-clamp a_ω=−(K/I_ω)·relu(−Γ)·ω integrated
by _rotate_clamp: that harmonic spring (ω̈=−Ω₀²ω) has NO |ω| ceiling (Ω₀ stiffens
as the front sharpens), so it confined (Γ→−0.994) AND PUMPED (H climbs 4.3×10⁶)
together — a bulk restoring force (CP10 violation), kept selectable
(impedance_unitary=False) only as the motivating diagnostic. The wall co-moves
with the cage front: Γ is recomputed from the focusing ω-field every sub-step
(_freeze_clamp_weight re-frozen per sub-step) — a GENERIC rule (tracks the
saturation threshold), NOT hand-placed where the answer is.

The energize-LOCK coupling (Sector A ⊗ Sector B shared-front Hamiltonian term
H_c=κ̃∫g·V·Ξ) is INHERITED UNCHANGED from Stage-1.5. The only new physics in the
coupled step is that the Cosserat sub-cycle now ALSO applies the impedance clamp
(both the front back-reaction f_ω AND the wall node-clamp in one conservative
Verlet/Strang sub-step).
"""
from __future__ import annotations

import numpy as np
import jax.numpy as jnp

from ave.core.a1_cosserat_convergence_engine import A1CosseratConvergenceEngine
from ave.topological import cosserat_field_3d as _cf
from ave.topological.cosserat_field_3d import CosseratField3D, _tetrahedral_curl


def _alpha_free_gamma_field(self) -> np.ndarray:
    """α-FREE Op3 reflection-coefficient field Γ(r) — the kappa_chiral=0 limit.

    Identical to CosseratField3D._impedance_gamma_field EXCEPT the chirality bias
    is set to ZERO (kappa_chiral=0), so the μ-side short A²_μ = A²_μ_base =
    κ²/ω_yield² is driven by the GENERIC curvature saturation ONLY (geometric,
    α-free) — NOT the α-bearing KAPPA_CHIRAL_ELECTRON = α·κ̃_e bias.

    Bound to the Sector-B instance so the moving-wall path is α-free end-to-end
    (the Stage-1.6 α-free routing; mirrors Stage-1.5's route around VacuumEngine3D).
    The μ-side short (Γ<0) is the confining node; the ε-side open (Γ>0) is not.
    """
    u_j = jnp.asarray(self.u)
    w_j = jnp.asarray(self.omega)
    V_sq = jnp.zeros((self.nx, self.ny, self.nz), dtype=u_j.dtype)
    S_mu, S_eps = _cf._update_saturation_kernels(
        u_j, w_j, V_sq, self.dx,
        _cf.V_SNAP,            # ε-side V-term has V_sq=0, so V_SNAP drops out (α-free here)
        self.omega_yield,
        self.epsilon_yield,
        0.0,                   # kappa_chiral = 0 — THE α-free override (no α·κ̃ bias)
    )
    Z_eff = jnp.sqrt(S_mu / jnp.maximum(S_eps, 1e-12))  # Z₀ = 1
    gamma = (Z_eff - 1.0) / (Z_eff + 1.0)
    return np.asarray(gamma)


class A1CosseratMovingWallEngine(A1CosseratConvergenceEngine):
    """Stage-1.6 — the Stage-1.5 α-free two-sector engine PLUS an EXTERNAL α-free
    moving Γ=−1 / Op17-bounded reflecting wall on Sector B (the Cosserat-ω sector).

    All Stage-1.5 physics is inherited unchanged (Sector A c_eff(V) cage, Sector B
    Cosserat winding, the shared-front energize-LOCK coupling H_c=κ̃∫g·V·Ξ). The
    only addition is the wall: Sector B is built with the Op3 Γ=−1 node-clamp
    (use_impedance_boundary), its Γ field overridden to the α-free (kappa_chiral=0)
    geometric-curvature form, and the coupled Cosserat sub-step applies BOTH the
    front back-reaction f_ω AND the wall node-clamp conservatively.
    """

    def __init__(
        self,
        N: int,
        dx: float = 1.0,  # = ℓ_node (natural unit; Phase-20 dx-normalize). Was 0.5
                          # (2× OVERsampling of the SAME object, not load-bearing).
        V_yield: float = 1.0,
        c0: float = 1.0,
        cfl_safety: float = 0.30,
        pml_thickness: int = 4,
        A_cap: float = 0.99,
        S_min: float = 0.05,
        kappa_tilde: float = 6.0 / 5.0,
        front_center: float = None,  # inherit R_II default from parent
        front_width: float = 0.18,
        couple_on: bool = True,
        coupling_support: str = "front",
        # ── NEW: the moving Γ=−1 wall on Sector B ──
        wall_on: bool = True,
        impedance_clamp_strength: float = 400.0,
        impedance_skin_smoothing: int = 2,
        impedance_cfl_safety: float = 0.4,
        # ── amendment-4: K4-TLM UNITARY-SCATTER wall (energy-honest, |ω|-bounded)
        #    vs the harmonic node-clamp (no |ω| ceiling — confines AND pumps) ──
        impedance_unitary: bool = True,
        project_alive: bool = True,
    ):
        # Build the parent (Sector A cage + Sector B Cosserat + coupling). The
        # parent constructs self.B as a plain CosseratField3D; we REPLACE it with
        # an impedance-boundary CosseratField3D (same grid/masks), α-free.
        parent_kwargs = dict(
            N=N, dx=dx, V_yield=V_yield, c0=c0, cfl_safety=cfl_safety,
            pml_thickness=pml_thickness, A_cap=A_cap, S_min=S_min,
            kappa_tilde=kappa_tilde, front_width=front_width,
            couple_on=couple_on, coupling_support=coupling_support,
            project_alive=project_alive,
        )
        if front_center is not None:
            parent_kwargs["front_center"] = front_center
        super().__init__(**parent_kwargs)

        self.wall_on = bool(wall_on)
        self.impedance_clamp_strength = float(impedance_clamp_strength)
        self.impedance_unitary = bool(impedance_unitary)

        # ── REPLACE Sector B with an impedance-boundary CosseratField3D ──
        # Same N³ extent, same K4 A/B masks, same saturation. The wall lives on
        # Sector B's OWN μ-sector (the photon's sector), NOT Sector A.
        self.B = CosseratField3D(
            self.N, self.N, self.N, dx=self.dx,
            use_saturation=True, pml_thickness=self.pml_thickness,
            use_impedance_boundary=self.wall_on,
            impedance_clamp_strength=self.impedance_clamp_strength,
            impedance_skin_smoothing=int(impedance_skin_smoothing),
            impedance_implicit=True,                  # energy-conserving (§7-fixed) path
            impedance_cfl_safety=float(impedance_cfl_safety),
            impedance_unitary=self.impedance_unitary, # amendment-4 unitary scatter
            project_alive=self.project_alive,         # keystone RUNG-0 projection toggle
        )
        # α-FREE ROUTING: bind the kappa_chiral=0 Γ field to THIS instance, so the
        # moving wall is driven by the geometric curvature saturation κ²/ω_yield²
        # only (no α·κ̃ bias). The bound method shadows the class default.
        if self.wall_on:
            import types
            self.B._impedance_gamma_field = types.MethodType(_alpha_free_gamma_field, self.B)

        # The wall's reactive sub-dt may be tighter than the bulk dt; keep the
        # parent's Cosserat sub-cycle count (it already targets the saturated
        # branch CFL). The implicit impedance path further sub-divides internally
        # to impedance_cfl_safety·cfl_dt, so the wall is CFL-safe per sub-step.

    # ── wall diagnostics (the Sector-B Γ→rim read) ──
    def wall_gamma_field(self) -> np.ndarray:
        """The α-free Sector-B Γ(r) field (kappa_chiral=0 geometric-curvature)."""
        if not self.wall_on:
            return np.zeros((self.N, self.N, self.N))
        return self.B._impedance_gamma_field()

    def wall_gamma_min_interior(self) -> float:
        """min Γ over alive interior sites — the μ-short depth (Γ→−1 = the rim)."""
        g = self.wall_gamma_field()
        m = self.B.mask_alive & self._interior
        return float(g[m].min()) if m.sum() else 0.0

    def wall_front_peak(self) -> tuple:
        """The wall-front location = the most-reflective cell (argmin Γ over alive
        interior). Reported vs the photon |ω|² peak for the wall-provenance audit
        (b): they must CO-EVOLVE under the generic Γ rule, not be pinned."""
        if not self.wall_on:
            return (self.N // 2, self.N // 2, self.N // 2)
        g = self.wall_gamma_field()
        masked = np.where(self.B.mask_alive & self._interior, g, np.inf)
        if not np.isfinite(masked).any():
            return (self.N // 2, self.N // 2, self.N // 2)
        return tuple(int(x) for x in np.unravel_index(int(np.argmin(masked)), masked.shape))

    def omega_localization(self) -> float:
        """Fraction of interior alive |ω|² within r≤6 of the ω density-peak
        (CP7 density-peak sampling, PML-excluded). High+held = the wall confines;
        →0 = the photon dispersed/radiated. The Sector-B confinement read."""
        w2 = np.sum(np.asarray(self.B.omega) ** 2, axis=-1) * self.B.mask_alive * self._interior
        tot = w2.sum()
        if tot < 1e-30:
            return 0.0
        pk = np.unravel_index(int(np.argmax(w2)), w2.shape)
        ii, jj, kk = self.B._i, self.B._j, self.B._k
        r2 = (ii - pk[0]) ** 2 + (jj - pk[1]) ** 2 + (kk - pk[2]) ** 2
        return float((w2 * (r2 <= 36)).sum() / tot)

    def coupling_hamiltonian_full(self) -> float:
        """Full coupled-system Hamiltonian witness WITH the wall: the Cosserat
        impedance_hamiltonian (T + W_linear + V_clamp, the reactive wall storage)
        + the bulk cage's conserved energy + the cross-sector H_c. A flat/decaying
        ledger = passive (energize-LOCK + reactive wall); a climbing ledger = PUMP.
        ave-conserved-vs-pumped: the wall stores energy reactively (V_clamp), it
        does NOT inject it."""
        if self.wall_on:
            imp = self.B.impedance_hamiltonian()
            H_B = imp["H"]
        else:
            H_B = float(self.B.total_hamiltonian())
        return H_B + self.bulk_energy_conserved() + self._coupling_energy()

    # ── coupling-curl SUBLATTICE diagnostic (flag-don't-fix; a MEASUREMENT, not
    #    a change to the dynamics) ──
    def coupling_support_overlap(self) -> dict:
        """Diagnose WHY f_V may be zero: the support overlap between the A1
        saturation-front coupling window g (masked to ALIVE K4 sites) and the
        Cosserat axial curl Ξ — under BOTH the INHERITED Cartesian stencil
        (`_cosserat_axial_curl`, np.roll(±1)) AND the substrate-native
        tetrahedral stencil (`_tetrahedral_curl`, the K4-diamond operator
        `_impedance_gamma_field` + the Cosserat energy already use).

        FINDING (flag-don't-fix, for auditor/Grant — NOT silently merged into the
        wall test): the inherited Cartesian np.roll(±1) curl straddles the K4
        diamond's DEAD cells, placing |Ξ| ENTIRELY on the dead sublattice (alive
        |Ξ|=0), while g is masked to ALIVE — so g·Ξ ≡ 0 for ANY field (confined
        or not). The substrate-native tetrahedral curl places |Ξ| on the ALIVE
        sublattice, where g·Ξ overlaps. This refines the Stage-1.5 (c) 'photon
        radiates out' mechanism: the loop is inert even for a wall-CONFINED photon
        through the inherited Cartesian-curl coupling, by discretization — a
        substrate-native-check Ckpt-2 violation in the inherited coupling stencil.

        Returns the two overlap reads so the result doc can report the
        discriminator without the engine's dynamics being altered."""
        g = self._front_window()
        m = self._interior
        alive = self.B.mask_alive
        Xi_cart = self._cosserat_axial_curl()
        Xi_tet = np.asarray(_tetrahedral_curl(jnp.asarray(self.B.omega), self.dx))[..., 2]
        def overlap(Xi):
            return int(((g > 1e-9) & (np.abs(Xi) > 1e-9) & m).sum())
        return {
            "g_alive_cells": int(((g > 1e-9) & m).sum()),
            "Xi_cartesian_alive_max": float(np.abs(Xi_cart[alive & m]).max()) if (alive & m).sum() else 0.0,
            "Xi_cartesian_dead_max": float(np.abs(Xi_cart[(~alive) & m]).max()) if ((~alive) & m).sum() else 0.0,
            "Xi_tetrahedral_alive_max": float(np.abs(Xi_tet[alive & m]).max()) if (alive & m).sum() else 0.0,
            "Xi_tetrahedral_dead_max": float(np.abs(Xi_tet[(~alive) & m]).max()) if ((~alive) & m).sum() else 0.0,
            "gXi_cartesian_max": float(np.abs(g * Xi_cart * m).max()),
            "gXi_tetrahedral_max": float(np.abs(g * Xi_tet * m).max()),
            "overlap_cells_cartesian": overlap(Xi_cart),
            "overlap_cells_tetrahedral": overlap(Xi_tet),
        }

    # ── the coupled step WITH the moving wall ──
    def step_coupled(self):
        """One coupled outer step WITH the moving Γ=−1 wall on Sector B.

        Identical to the parent Stage-1.5 step_coupled (Sector A leapfrog with the
        front source f_V; Sector B sub-cycled with the front back-reaction f_ω)
        EXCEPT the Cosserat sub-cycle now ALSO applies the wall node-clamp. The
        wall Γ is re-frozen each Cosserat sub-step (the moving-front generic rule)
        and integrated by the exact LC rotation (conservative, anti-pump).

        Both the front back-reaction f_ω (a conservative gradient of H_c) and the
        wall node-clamp (a reactive node force, exactly integrated) act on Sector
        B's own Verlet/Strang sub-step at consistent time-centering — no pumping.
        """
        f_V, f_omega = self._coupling_forces()

        # ── Sector A: leapfrog with the front source f_V (unchanged from parent) ──
        if self.couple_on:
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

        # ── Sector B: sub-cycled, WITH the front back-reaction AND the wall ──
        a_omega_ext = (f_omega / self.B.I_omega) if self.couple_on else None
        for _ in range(self.n_sub_cos):
            if self.wall_on:
                self._cosserat_substep_wall(a_omega_ext)
            else:
                self._cosserat_substep_with_force(a_omega_ext)

        self.coupling_work += float(self._coupling_energy())
        self.time += self.A.dt
        self.step_count += 1

    def _cosserat_substep_wall(self, a_omega_ext):
        """One Cosserat sub-step WITH the moving Γ=−1 wall (impedance_implicit
        Strang split) AND the optional front back-reaction a_omega_ext.

        Mirrors CosseratField3D.step's implicit branch (kick / exact-rotate-drift /
        kick) but adds the constant front back-reaction a_omega_ext (a conservative
        gradient force) to each half-kick — exactly as the parent's
        _cosserat_substep_with_force adds it to the bare Verlet. The wall Γ is
        re-frozen at the start (the moving-front rule), and the (ω,ω̇) reactance
        pair is advanced by the exact LC rotation (energy-conserving, anti-pump)."""
        B = self.B
        # The implicit path internally sub-divides to impedance_cfl_safety·cfl_dt.
        dt = self.dt_sub_cos
        dt_safe = B.impedance_cfl_safety * B.cfl_dt
        n_sub = max(1, int(np.ceil(dt / max(dt_safe, 1e-30))))
        sub = dt / n_sub
        add = a_omega_ext  # constant over this outer step (frozen front force)
        for _ in range(n_sub):
            B._freeze_clamp_weight()           # re-evaluate the moving wall (generic rule)
            omega0 = B._clamp_omega0()
            a_u, a_w = B._bulk_accel()
            if add is not None:
                a_w = a_w + add
            # 1. half-kick (bulk force + front back-reaction)
            B.u_dot = B.u_dot + 0.5 * sub * a_u
            B.omega_dot = B.omega_dot + 0.5 * sub * a_w
            B._zero_velocities_outside_alive()
            # 2. drift u; turn the (ω, ω̇) reactance pair at the wall. amendment-4:
            #    the UNITARY scatter (|ω|-bounded, no pump — |output|=|input|)
            #    replaces the harmonic node-clamp `_rotate_clamp` (no |ω| ceiling,
            #    confines AND pumps) when impedance_unitary is set on Sector B.
            B.u = B.u + sub * B.u_dot
            if B.impedance_unitary:
                B._unitary_scatter(omega0)
            else:
                B._rotate_clamp(omega0, sub)
            B._zero_outside_alive()
            # 3. half-kick (bulk force + front back-reaction at the new state)
            a_u_new, a_w_new = B._bulk_accel()
            if add is not None:
                a_w_new = a_w_new + add
            B.u_dot = B.u_dot + 0.5 * sub * a_u_new
            B.omega_dot = B.omega_dot + 0.5 * sub * a_w_new
            B._zero_velocities_outside_alive()
            B.time += sub
