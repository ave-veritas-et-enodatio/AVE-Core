"""
Unified Genesis Engine (v5) — the merged carrier for the seeded-snap build
==========================================================================

Genesis-v5 (Grant-ratified design 2026-06-10; prereg
`research/2026-06-10_genesis-v5-seeded-snap_prereg.md`). This is COMPONENT 1 of
the incremental build: the UNIFIED engine that carries, in ONE class, the DOFs
that until now lived in two SEPARATE, incompatible engines.

REPRESENTATION-CAPABILITY CHECK (substrate-native-check CP2; recorded before the
first line of numerical code — see the agent return). The prior carriers:

  • `CrystalGraftV4` (3D)  carries  scalar V + STIFFENING c_eff²=c₀²/√(1−A²) trap
    (the crystal/graft branch), the Cosserat ω carrier + π_ω + mass-gap, the
    photon w + chiral H_couple (κ̃=6/5). It has NO bulk density ρ̄, NO continuity
    equation, NO advective velocity, and its EOS is the OPPOSITE branch from the
    cavitation snap (core SATURATES A→1, c_eff→∞).

  • `CavitationFlow2D` / `SonicHorizonFlow2D` (2D) carry the bulk density ρ̄ + the
    RAREFACTION EOS c²=c₀²(1+ρ̄/(1−ρ̄²))→0 at ρ̄_cav=−1/φ, the advective velocity
    (u,v), circulation Γ, the exact-EOS pressure() ledger, and the snap state
    machine (cav_mask). They are 2D and carry NO V/w/ω.

THE GAPS THE MERGE LACKS (named before building):
  GAP-A  the rarefaction bulk-density DOF ρ̄ + the rarefaction EOS + exact
         pressure ledger — ABSENT from graft-v4 (opposite EOS branch).
  GAP-B  the bulk ADVECTIVE transport velocity u (3-vector) that hosts
         circulation and drives the centrifugal rarefaction deficit — ABSENT
         from graft-v4 (whose only "velocity" is the irrotational scalar C-state
         (V−V_prev)/dt; the Cosserat ω is micro-rotation, a SEPARATE DOF).
  GAP-C  the cross-sector COUPLINGS (seed-V↔ρ̄, ω↔u) — specified by NO inherited
         engine (a NEW physics surface; FLAGGED for adjudication, default OFF so
         inherited V/w/ω evolution is byte-identical when the bulk sector is
         dormant — the component-1 known-null).
  GAP-D  3D rotation organized along an axis for the collimation columns —
         supplied by the new 3D u field (the columnarity observer reads it).

This component ADDS the 3D rarefaction bulk-density sector (ρ̄, u, EOS, exact
pressure ledger) as a NEW, additively-integrated DOF ALONGSIDE the unchanged
V/w/ω. Master switch `bulk_density_on` (default False) ⇒ `step()` is byte-for-
byte `CrystalGraftV4.step()` (the inherited-physics-unchanged HARD CONSTRAINT).

ave-apparatus-floor-attribution: every new numerical knob (c2_floor, rho_floor,
eps_den, nu_art_bulk, rho_diff) is a CLIP suspect, named here, swept in the
prereg §5 grid; a verdict that TRACKS one is APPARATUS, not physics.

substrate-native-check: CP1 dynamical FDTD/RK2 (no minimization); CP2 the COUPLED
bulk-K(ρ̄,u) ⊗ longitudinal-V ⊗ Cosserat-ω ⊗ shear-w channel; CP4 ρ̄ measured in
real-space (its own coordinate), the winding in phase-space (the parent's
extractor); CP7 PML/interior-excluded density-peak sampling; CP9 ρ̄ is
DYNAMICALLY integrated (continuity), not the algebraic centrifugal formula; CP10
the snap (component 2) is a per-cell boundary state machine, NOT a bulk force.
"""

from __future__ import annotations

import numpy as np

from ave.core.crystal_graft_v4 import CrystalGraftV4

# Candidate cavitation floor (CANDIDATE-CLAIM, Propulsion-derived; cite as
# candidate, never canonical — prereg §0.2). PHI is the only canonical anchor.
PHI = (1.0 + np.sqrt(5.0)) / 2.0
RHO_CAV = -1.0 / PHI  # = (1−√5)/2 ≈ −0.6180339887 ; c_bulk²(ρ̄_cav)=0


class UnifiedGenesisEngine(CrystalGraftV4):
    """CrystalGraftV4 + a 3D rarefaction bulk-density sector (ρ̄, u_adv, the
    rarefaction EOS, the exact pressure ledger). The inherited V/w/ω/buckle/lock
    sectors are untouched; with `bulk_density_on=False` the step is byte-
    identical to the parent."""

    def __init__(
        self,
        N: int,
        *,
        bulk_density_on: bool = False,
        c2_floor: float = 1e-3,
        rho_floor: float = -0.95,
        eps_den: float = 1e-6,
        nu_art_bulk: float = 5e-4,
        rho_diff: float = 5e-4,
        # --- D1 SNAP state machine (component 2; off by default) ---
        snap_on: bool = False,
        rho_cav: float = RHO_CAV,
        chi_shock: float = 1.0,
        delta_heal: float = 0.0,
        snap_payback_rate: float = 1.0,
        **kwargs,
    ):
        """
        New (bulk-density rarefaction sector) args:
            bulk_density_on: master switch for the ρ̄/u sector. False ⇒ the engine
                             IS CrystalGraftV4 byte-for-byte (the known-null).
            c2_floor:        hyperbolicity floor c_bulk²=max(c²_raw,c2_floor·c₀²).
                             CLIP suspect K1. The snap (component 2) overrides to
                             0 (clamp at exactly zero = the Z_bulk→0 reflector).
            rho_floor:       ρ̄=max(ρ̄,rho_floor) keeps (1+ρ̄),(1−ρ̄²)>0. CLIP N-class.
            eps_den:         (1−ρ̄²) denominator guard. CLIP suspect.
            nu_art_bulk:     +nu_art·∇²u momentum stabilizer. THE D8 attribution
                             knob (K1 in the prereg): dissipates Γ — swept.
            rho_diff:        +rho_diff·∇²ρ̄ mass-diffusion stabilizer (smears the
                             deficit — conservative direction).
        """
        super().__init__(N, **kwargs)
        self.bulk_density_on = bool(bulk_density_on)
        # apparatus knobs (CLIP suspects — inventoried, swept §5)
        self.c2_floor = float(c2_floor)
        self.rho_floor = float(rho_floor)
        self.eps_den = float(eps_den)
        self.nu_art_bulk = float(nu_art_bulk)
        self.rho_diff = float(rho_diff)

        Nn = self.N
        # the NEW DOFs (GAP-A, GAP-B): bulk volumetric density + advective velocity
        self.rho_bar = np.zeros((Nn, Nn, Nn), dtype=np.float64)
        self.u_adv = np.zeros((Nn, Nn, Nn, 3), dtype=np.float64)

        # cell-centered coordinates for the energize helpers (3D, centered on grid)
        cc = (self.N - 1) / 2.0
        i, j, k = np.indices((Nn, Nn, Nn))
        self._bx = (i - cc) * self.dx
        self._by = (j - cc) * self.dx
        self._bz = (k - cc) * self.dx
        self._brho_cyl = np.sqrt(self._bx ** 2 + self._by ** 2)  # cyl radius ⟂ z
        self._br = np.sqrt(self._bx ** 2 + self._by ** 2 + self._bz ** 2)

        # bookkeeping telltales (apparatus)
        self.clip_rho_hits = 0
        self.clip_c2_hits = 0
        self.bulk_step_count = 0

        # ---------- D1 SNAP state machine (CP10 per-cell boundary; component 2) ----
        # CLIP suspects (prereg §5): N1 rho_cav (candidate −1/φ), N3 chi_shock
        # (latent-tally fraction; 0 = elastic control), N2 delta_heal (re-entry
        # width). The snap is hysteresis-by-BOOKKEEPING: re-entry requires the
        # tally PAID BACK (NO new EOS — the EOS is the inherited rarefaction one;
        # the reflector is the EOS's own c²(ρ̄_cav)=0 with c2_floor=0).
        self.snap_on = bool(snap_on)
        self.rho_cav = float(rho_cav)        # N1
        self.chi_shock = float(chi_shock)    # N3
        self.delta_heal = float(delta_heal)  # N2
        self.snap_payback_rate = float(snap_payback_rate)
        self.snap_mask = np.zeros((Nn, Nn, Nn), dtype=bool)
        self.latent_ledger = np.zeros((Nn, Nn, Nn), dtype=np.float64)  # held-out per cell
        self.paid_ledger = np.zeros((Nn, Nn, Nn), dtype=np.float64)    # paid-back per cell
        # cumulative scalar ledgers (energy bookkeeping; the tally must close)
        self.E_latent_held = 0.0   # currently held out of the dynamics (sum of latent_ledger)
        self.E_latent_restored = 0.0  # paid-back-and-returned (cumulative)
        self.E_diss_snap = 0.0     # shock-class one-way (chi_shock·void-KE)
        self.mass_clamp = 0.0      # |mass| added by the void-floor clamp (honesty)
        self.snap_events = 0
        self.unsnap_events = 0
        if self.snap_on:
            self._build_U_table()

    # ----------------------------------------------------- bulk EOS (rarefaction)
    def c_bulk2_raw(self, rho: np.ndarray) -> np.ndarray:
        """Unclipped rarefaction-stiffness EOS c_bulk²(ρ̄)=c₀²(1+ρ̄/(1−ρ̄²)).
        Softens on rarefaction (ρ̄<0), crosses 0 at ρ̄_cav=−1/φ (the candidate
        cavitation floor); stiffens on compression (ρ̄>0)."""
        denom = 1.0 - rho ** 2
        denom = np.where(np.abs(denom) < self.eps_den,
                         np.sign(denom) * self.eps_den + self.eps_den, denom)
        return (self.c0 ** 2) * (1.0 + rho / denom)

    def c_bulk2(self, rho: np.ndarray) -> np.ndarray:
        """c_bulk² with the hyperbolicity floor (clipped). The snap (component 2)
        sets c2_floor=0 ⇒ clamp at EXACTLY zero below the locus = the reflector."""
        return np.maximum(self.c_bulk2_raw(rho), self.c2_floor * self.c0 ** 2)

    def pressure(self, rho: np.ndarray) -> np.ndarray:
        """Exact EOS integral p(ρ̄)=ρ₀c₀²[ρ̄−½ln(1−ρ̄²)] (ρ₀≡1). The D6 longitudinal-
        burst detector reads this ledger (cavitation_flow.py:165–166 parity)."""
        arg = np.maximum(1.0 - rho ** 2, self.eps_den)
        return (self.c0 ** 2) * (rho - 0.5 * np.log(arg))

    # ----------------------------------------- exact EOS internal energy ε(ρ̄)
    def _build_U_table(self):
        """ε(ρ)=ρ∫_1^ρ p(s)/s² ds (s≡ρ=1+ρ̄), p the exact EOS integral. The latent
        tally and the snap energy bookkeeping use THIS internal energy — the same
        convention sonic_horizon_flow validated by free-run KE+PE conservation."""
        rb = np.linspace(-0.999, 3.0, 40001)
        rho = 1.0 + rb
        p = self.pressure(rb)
        integrand = p / rho ** 2
        i0 = int(np.argmin(np.abs(rb)))
        cum = np.zeros_like(rb)
        for i in range(i0 + 1, len(rb)):
            cum[i] = cum[i - 1] + 0.5 * (integrand[i] + integrand[i - 1]) * (rho[i] - rho[i - 1])
        for i in range(i0 - 1, -1, -1):
            cum[i] = cum[i + 1] + 0.5 * (integrand[i] + integrand[i + 1]) * (rho[i] - rho[i + 1])
        self._U_rb = rb
        self._U_eps = rho * cum

    def U_density(self, rho_bar):
        """Exact EOS internal-energy density ε(ρ̄) (table interp)."""
        return np.interp(rho_bar, self._U_rb, self._U_eps)

    # ----------------------------------------------- 3D bulk differential ops
    @staticmethod
    def _d(f: np.ndarray, axis: int, dx: float) -> np.ndarray:
        return (np.roll(f, -1, axis=axis) - np.roll(f, 1, axis=axis)) / (2.0 * dx)

    def _div3(self, mx, my, mz) -> np.ndarray:
        return self._d(mx, 0, self.dx) + self._d(my, 1, self.dx) + self._d(mz, 2, self.dx)

    def _bulk_rhs(self, rho, u):
        """RHS of the 3D barotropic bulk-density flow (port of CavitationFlow2D._rhs):
            ∂ρ̄/∂t = −∇·[(1+ρ̄)u] + rho_diff·∇²ρ̄
            ∂u/∂t = −(u·∇)u − [c²/(1+ρ̄)]∇ρ̄ + nu_art·∇²u
        Conserved invariant (Kelvin, barotropic, inviscid): circulation Γ."""
        ux, uy, uz = u[..., 0], u[..., 1], u[..., 2]
        # continuity
        one_p = 1.0 + rho
        div_m = self._div3(one_p * ux, one_p * uy, one_p * uz)
        drho_dt = -div_m + self.rho_diff * self._laplacian(rho, self.dx)
        # momentum
        c2 = self.c_bulk2(rho)
        pref = c2 / np.maximum(one_p, self.eps_den)
        drx = self._d(rho, 0, self.dx)
        dry = self._d(rho, 1, self.dx)
        drz = self._d(rho, 2, self.dx)
        du = np.empty_like(u)
        for comp, (dudc, drc) in enumerate(
            ((u[..., 0], drx), (u[..., 1], dry), (u[..., 2], drz))
        ):
            adv = (ux * self._d(dudc, 0, self.dx)
                   + uy * self._d(dudc, 1, self.dx)
                   + uz * self._d(dudc, 2, self.dx))
            du[..., comp] = (-adv - pref * drc
                             + self.nu_art_bulk * self._laplacian(dudc, self.dx))
        return drho_dt, du

    def _bulk_step(self):
        """RK2 (midpoint) integration of the bulk-density sector + PML damp +
        clip telltales. Called by step() only when bulk_density_on."""
        dt = self.dt
        k1r, k1u = self._bulk_rhs(self.rho_bar, self.u_adv)
        rm = self.rho_bar + 0.5 * dt * k1r
        um = self.u_adv + 0.5 * dt * k1u
        k2r, k2u = self._bulk_rhs(rm, um)
        self.rho_bar = self.rho_bar + dt * k2r
        self.u_adv = self.u_adv + dt * k2u
        # reuse the parent's PML/edge absorber (CP7 — the bulk sector vents the
        # same boundary as V/w/ω); interior measurement uses interior_mask()
        self.rho_bar *= self.damping
        self.u_adv *= self.damping[..., None]
        # clip telltales (apparatus — counted in the interior so we know if they bit)
        m = self.interior_mask()
        below = (self.rho_bar < self.rho_floor) & m
        self.clip_rho_hits += int(np.count_nonzero(below))
        np.maximum(self.rho_bar, self.rho_floor, out=self.rho_bar)
        c2raw = self.c_bulk2_raw(self.rho_bar)
        self.clip_c2_hits += int(np.count_nonzero((c2raw < self.c2_floor * self.c0 ** 2) & m))
        self.bulk_step_count += 1

    # ------------------------------------------------------- D1 SNAP machine (CP10)
    def _tally_latent_and_snap(self, newly):
        """A cell newly crossing ρ̄≤ρ̄_cav: TALLY its latent (reversible internal-
        energy released crossing to the void floor + χ_shock of its advective KE),
        REMOVE it from the dynamics, clamp the cell to the void floor (the
        Z_bulk→0 reflector with c2_floor=0). Hysteresis-by-bookkeeping: the latent
        is HELD until paid back."""
        rb_before = self.rho_bar[newly]
        # reversible internal-energy released crossing to the floor
        d_eps = np.abs(self.U_density(rb_before) - self.U_density(self.rho_cav))
        # shock-class void KE removed (one-way)
        rho_full = 1.0 + rb_before
        ke_void = 0.5 * rho_full * np.sum(self.u_adv[newly] ** 2, axis=-1)
        latent_cell = (d_eps + self.chi_shock * ke_void) * self.dx ** 3
        self.latent_ledger[newly] = latent_cell
        self.paid_ledger[newly] = 0.0
        self.E_latent_held += float(np.sum(latent_cell))
        e_shock = float(np.sum(self.chi_shock * ke_void) * self.dx ** 3)
        # D2 VENT: the shock-removed void KE drains as a longitudinal pulse into
        # the seed (near-field) + a spherical remainder (radiated); else it is a
        # pure one-way dissipative sink (component-2 behavior).
        if getattr(self, "vent_into_seed", False):
            self._vent_to_seed(e_shock)
        else:
            self.E_diss_snap += e_shock
        # remove the crossing KE (shock), clamp to the void floor (track added mass)
        self.u_adv[newly] *= (1.0 - self.chi_shock)
        self.mass_clamp += float(np.sum(np.clip(self.rho_cav - rb_before, 0.0, None)) * self.dx ** 3)
        self.rho_bar[newly] = self.rho_cav
        self.snap_mask[newly] = True
        self.snap_events += int(np.count_nonzero(newly))

    def _snap_step(self):
        """Per-cell snap state machine (normal↔snapped), interior only (CP7).
          1. newly-snapping cells (ρ̄≤ρ̄_cav, not yet snapped) ⇒ tally + clamp.
          2. already-snapped cells ⇒ enforced void (reflector BC) + over-pressure
             payback accrual.
          3. cells whose tally is PAID BACK ⇒ un-snap (re-enter above the floor;
             the held latent is RESTORED to the dynamics ledger). NO new EOS."""
        m = self.interior_mask()
        # (1) crossings
        below = (self.rho_bar <= self.rho_cav) & m & ~self.snap_mask
        if below.any():
            self._tally_latent_and_snap(below)
        if not self.snap_mask.any():
            return
        cm = self.snap_mask
        # (2) enforce the boundary-class void (reflector: ρ̄ held at floor, u killed)
        self.rho_bar[cm] = self.rho_cav
        self.u_adv[cm] = 0.0
        # over-pressure payback: the surrounding medium does work against the void.
        # neighbor-mean pressure minus the void pressure; positive ⇒ pushing in.
        p = self.pressure(self.rho_bar)
        p_neigh = (np.roll(p, 1, 0) + np.roll(p, -1, 0)
                   + np.roll(p, 1, 1) + np.roll(p, -1, 1)
                   + np.roll(p, 1, 2) + np.roll(p, -1, 2)) / 6.0
        over = np.clip(p_neigh - self.pressure(np.array(self.rho_cav)), 0.0, None)
        self.paid_ledger[cm] += over[cm] * self.dx ** 3 * self.snap_payback_rate * self.dt
        # (3) un-snap the paid-up cells (re-enter above floor; restore the latent)
        paid_up = cm & (self.paid_ledger >= self.latent_ledger) & (self.latent_ledger > 0.0)
        if paid_up.any():
            restored = float(np.sum(self.latent_ledger[paid_up]))
            self.E_latent_held -= restored
            self.E_latent_restored += restored
            self.rho_bar[paid_up] = self.rho_cav + self.delta_heal
            self.snap_mask[paid_up] = False
            self.latent_ledger[paid_up] = 0.0
            self.paid_ledger[paid_up] = 0.0
            self.unsnap_events += int(np.count_nonzero(paid_up))

    def hand_snap_region(self, mask: np.ndarray, rho_set: float | None = None):
        """CALIBRATION (D6 F0d — 'a known case'): hand-open a snapped pocket. Sets
        the region below the floor and runs ONE snap detection so it tallies +
        clamps exactly as a dynamical crossing would. Returns the tallied latent."""
        if rho_set is None:
            rho_set = self.rho_cav - 0.05
        before = self.E_latent_held
        self.rho_bar[mask & self.interior_mask()] = rho_set
        self._snap_step()
        return self.E_latent_held - before

    # ============================================ D5 DRIVE (FOC d/q chiral photon)
    def drive_chiral_photon(self, helicity: int = +1, sigma: float = 5.0,
                            wavelength: float = 8.0, amplitude: float = 0.05,
                            axis: int = 2, center=None,
                            bemf_arm: bool = False, tau_zx_arm: bool = False):
        """D5 DRIVE: inject the FOC-framed chiral transverse photon (the v4 field-
        derived source, the inherited seed_photon) along `axis` (the FOC/spin
        axis). helicity=±1 sets the handedness (the q-axis torque sign = charge
        sign provenance). Arms: bemf_arm (the κ_L=6/5 reaction-half = the lock's
        inertia, centered-step) and tau_zx_arm (Fork-A literal τ_zx radiation-
        reaction feedback) — each its OWN switch, metered, swept (prereg §3)."""
        if center is None:
            c = (self.N - 1) / 2.0
            center = (c, c, c)
        direction = [0, 0, 0]
        direction[axis] = 1
        self.seed_photon(center, sigma=sigma, wavelength=wavelength,
                         amplitude=amplitude, helicity=float(helicity),
                         direction=tuple(direction))
        self.foc_axis = int(axis)
        self.drive_helicity = int(np.sign(helicity)) or 1
        self.bemf_arm = bool(bemf_arm)
        self.tau_zx_arm = bool(tau_zx_arm)
        self._bemf_work = 0.0
        self._tau_zx_work = 0.0

    def _foc_unit_vectors(self, axis: int):
        """Cylindrical ê_ρ (radial ⟂ axis = the d/flux direction) and ê_φ
        (azimuthal = the q/torque direction) about `axis`."""
        if axis == 2:
            a1, a2 = self._bx, self._by
        elif axis == 1:
            a1, a2 = self._bx, self._bz
        else:
            a1, a2 = self._by, self._bz
        rho = np.sqrt(a1 ** 2 + a2 ** 2) + 1e-12
        e_rho = np.zeros((self.N, self.N, self.N, 3))
        e_phi = np.zeros((self.N, self.N, self.N, 3))
        # map the two in-plane axes back to (x,y,z) component indices
        idx = {2: (0, 1), 1: (0, 2), 0: (1, 2)}[axis]
        e_rho[..., idx[0]] = a1 / rho
        e_rho[..., idx[1]] = a2 / rho
        e_phi[..., idx[0]] = -a2 / rho
        e_phi[..., idx[1]] = a1 / rho
        return e_rho, e_phi

    def foc_dq_project(self, F: np.ndarray, axis: int | None = None) -> dict:
        """Project a vector field F onto the FOC d-axis (cyl-radial = FLUX/core-
        rarefaction role) and q-axis (cyl-azimuthal = TORQUE/circulation spin-up
        role). Returns the d/q POWERS (∫|·|²) and the SIGNED net q-torque (its sign
        = the spin-up handedness)."""
        if axis is None:
            axis = getattr(self, "foc_axis", 2)
        e_rho, e_phi = self._foc_unit_vectors(axis)
        m = self.interior_mask()
        Fd = np.sum(F * e_rho, axis=-1)
        Fq = np.sum(F * e_phi, axis=-1)
        P_d = float(np.sum((Fd ** 2) * m) * self.dx ** 3)
        P_q = float(np.sum((Fq ** 2) * m) * self.dx ** 3)
        net_q = float(np.sum(Fq * m) * self.dx ** 3)  # signed torque sense
        return {"P_d": P_d, "P_q": P_q, "net_q_torque": net_q}

    def foc_dq_meter(self) -> dict:
        """Meter the DRIVE's two roles separately: the buckle force f_ω (the
        photon's action on the winding carrier) split into d (flux/rarefaction)
        and q (torque/spin-up). The net q-torque SIGN tracks the drive helicity
        (the charge-sign provenance — the v4 RH↔LH sign-carry)."""
        if not (self.omega_sector_on and self.buckle_on and self.photon_coupling):
            return {"P_d": 0.0, "P_q": 0.0, "net_q_torque": 0.0, "helicity": 0}
        _, f_w, f_omega = self._buckle_forces()
        out = self.foc_dq_project(f_omega)
        out["helicity"] = int(getattr(self, "drive_helicity", 0))
        # the HANDEDNESS channel is the photon's QUADRATIC helicity (flips with the
        # CP helicity — the v4 sign-carry); the net LINEAR q-torque is symmetry-
        # balanced (~0). Both reported so the meter does not over-claim the torque.
        out["photon_helicity"] = self.helicity_photon()
        return out

    def bemf_power(self) -> float:
        """The κ_L=6/5 BEMF reaction-half power = the energy the lock removes from
        the rigid-rotation mode per step (the lock's inertia; it appears only
        against CHANGES — D8). The inherited lock_relax is an EXACT per-step
        contraction (centered/unconditionally-stable — the velocity-dependent-
        force integration mandate is already satisfied)."""
        if not (self.lock_on and self.omega_sector_on):
            return 0.0
        # H_bel conservation canary doubles as the BEMF metering hook
        return float(self._Hbel_pre_lock - self._Hbel_post_lock)

    # ------------------------------------------------------- pocket observers (CP7)
    def pocket_cells(self) -> int:
        return int(np.count_nonzero(self.snap_mask))

    def pocket_frac(self) -> float:
        return self.pocket_cells() / float(np.count_nonzero(self.interior_mask()))

    def snap_ledger(self) -> dict:
        return {
            "pocket_cells": self.pocket_cells(),
            "snap_events": self.snap_events,
            "unsnap_events": self.unsnap_events,
            "E_latent_held": self.E_latent_held,
            "E_latent_restored": self.E_latent_restored,
            "E_diss_snap": self.E_diss_snap,
            "mass_clamp": self.mass_clamp,
        }

    # ------------------------------------------------------------------- step
    def step(self):
        """Inherited V/w/ω/buckle/lock step (UNCHANGED), then — only if the bulk
        sector is on — the ρ̄/u rarefaction substep, then — only if snap_on — the
        D1 per-cell snap state machine. bulk_density_on=False ⇒ byte-identical to
        CrystalGraftV4.step()."""
        super().step()
        if self.bulk_density_on:
            self._bulk_step()
            if self.snap_on:
                self._snap_step()

    # ------------------------------------------- energize (ENERGIZE+LOCK; never pump)
    def energize_rotation_column(self, M_edge: float, R_core: float,
                                 axis: int = 2, taper_frac: float = 0.15):
        """Set an initial solid-body rotation COLUMN about `axis` (default z, so the
        collimation columns lie along the spin axis — GAP-D): v_θ=Ω r (cyl r about
        the axis), smooth radial taper. M_edge=Ω·R_core/c₀ is the swept DRIVE
        amplitude; circulation Γ≈2πΩR² is the CONSERVED invariant set ONCE
        (ave-conserved-vs-pumped). ρ̄ starts at 0 (the deficit EMERGES — CP9)."""
        Omega = M_edge * self.c0 / R_core
        # cylindrical coordinates about the chosen axis
        if axis == 2:
            a1, a2 = self._bx, self._by  # ⟂ plane (x,y), spin about z
        elif axis == 1:
            a1, a2 = self._bx, self._bz
        else:
            a1, a2 = self._by, self._bz
        rc = np.sqrt(a1 ** 2 + a2 ** 2)
        env = np.ones_like(rc)
        taper = taper_frac * self.N * self.dx
        ramp = (rc - R_core) / max(taper, 1e-12)
        env = np.where(rc <= R_core, 1.0,
                       np.clip(0.5 * (1.0 + np.cos(np.pi * np.clip(ramp, 0, 1))), 0.0, 1.0))
        env = np.where(rc > R_core + taper, 0.0, env)
        # solid body about axis: v = Ω(−a2, a1) in the ⟂ plane
        self.u_adv[:] = 0.0
        if axis == 2:
            self.u_adv[..., 0] = -Omega * a2 * env
            self.u_adv[..., 1] = Omega * a1 * env
        elif axis == 1:
            self.u_adv[..., 0] = -Omega * a2 * env
            self.u_adv[..., 2] = Omega * a1 * env
        else:
            self.u_adv[..., 1] = -Omega * a2 * env
            self.u_adv[..., 2] = Omega * a1 * env
        self.rho_bar[:] = 0.0
        return Omega

    def energize_radial_breather(self, ke_target: float, R_core: float,
                                 taper_frac: float = 0.15):
        """Curl-free DIVERGING radial drive (ζ=0) with a chosen KE — the matched-
        energy, no-circulation control (no centrifugal deficit should form)."""
        r = self._br + 1e-12
        env = np.ones_like(r)
        taper = taper_frac * self.N * self.dx
        ramp = (r - R_core) / max(taper, 1e-12)
        env = np.where(r <= R_core, 1.0,
                       np.clip(0.5 * (1.0 + np.cos(np.pi * np.clip(ramp, 0, 1))), 0.0, 1.0))
        env = np.where(r > R_core + taper, 0.0, env)
        ur = self._bx / r * env
        vr = self._by / r * env
        wr = self._bz / r * env
        ke_unit = 0.5 * float(np.sum(ur ** 2 + vr ** 2 + wr ** 2)) * self.dx ** 3
        amp = np.sqrt(ke_target / max(ke_unit, 1e-30))
        self.u_adv[:] = 0.0
        self.u_adv[..., 0] = amp * ur
        self.u_adv[..., 1] = amp * vr
        self.u_adv[..., 2] = amp * wr
        self.rho_bar[:] = 0.0
        return amp

    def despin_bulk(self, factor: float = 0.0):
        """De-energize the bulk advective circulation (the P2 forced-de-spin arm /
        the hysteresis test). factor=0 ⇒ full de-spin."""
        self.u_adv *= factor

    # ------------------------------------------------------- D2 SEED (Lane-1 V)
    def seed_lane1(self, center=None, sigma: float = 4.0, frac: float = 0.85,
                   vent_into_seed: bool = False, vent_near_frac: float = 0.5):
        """D2 SEED: a Lane-1 saturated region carrying a STANDING longitudinal V
        (the genesis-24 trap machinery, A_cap-class). Plants the inherited
        topology-NULL bulk seed (V only; NO (2,3) planted — CP8 precursor-only)
        and arms the VENT: the snap's latent PULSE drains into this seed.

        ave-conserved-vs-pumped: the standing V is ENERGIZED+LOCKED once (stationary
        ∂_tV=0 start), never CW-pumped. frac is the swept saturation depth
        (A²_V=frac²; engineering-choice, genesis-24 grid {0.30,0.60,0.85,0.95}).

        FLAG (flag-don't-fix): `vent_into_seed` instantiates the GAP-C cross-sector
        coupling (snap ledger → seed V) that NO inherited engine specifies — it is
        the D2-RATIFIED coupling (the directive), hypothesis-class, switchable and
        energy-accounted; default OFF so the seed alone is the inherited physics."""
        if center is None:
            c = (self.N - 1) / 2.0
            center = (c, c, c)
        # the inherited topology-null saturated bulk seed (helical=False ⇒ no winding)
        self.seed_bulk(center, sigma=sigma, frac=frac, helical=False)
        # seed window (normalized Gaussian) — the vent's near-field target
        cx, cy, cz = center
        r2 = (self._bx / self.dx + (self.N - 1) / 2.0 - cx) ** 2 \
            + (self._by / self.dx + (self.N - 1) / 2.0 - cy) ** 2 \
            + (self._bz / self.dx + (self.N - 1) / 2.0 - cz) ** 2
        self._seed_window = np.exp(-r2 / (2.0 * sigma ** 2))
        self.seed_frac = float(frac)
        self.vent_into_seed = bool(vent_into_seed)
        self.vent_near_frac = float(min(max(vent_near_frac, 0.0), 1.0))
        self.E_vent_to_seed = 0.0
        self.E_vent_radiated = 0.0

    def seed_certificate(self) -> dict:
        """CP8 precursor-only certificate: the seed is V-populated but topology-
        NULL. |H_bel|≈0 (no (2,3) planted), ω≡0, A²_V≈frac², ∂_tV≈0 (standing).
        A non-null H_bel / nonzero ω here would auto-VOID the run (a forbidden
        topology seeder fired)."""
        m = self.interior_mask()
        A2 = (np.abs(self.V) / self.V_yield) ** 2
        w = getattr(self, "_seed_window", np.ones_like(self.V))
        denom = float(np.sum(w * m)) + 1e-30
        A2_seed = float(np.sum(A2 * w * m) / denom)   # window-weighted average
        A2_peak = float(np.max(A2 * m))               # core depth (= frac², genesis-24)
        hbel = float(abs(self.helicity_bel())) if self.omega_sector_on else 0.0
        omega_max = float(np.max(np.abs(self.omega)))
        dvdt_max = float(np.max(np.abs((self.V - self.V_prev) / self.dt)))
        topology_null = (hbel < 1e-12) and (omega_max < 1e-12)
        return {
            "A2_seed": A2_seed,
            "A2_peak": A2_peak,
            "frac2": float(self.seed_frac ** 2) if hasattr(self, "seed_frac") else None,
            "H_bel_abs": hbel,
            "omega_max": omega_max,
            "dVdt_max": dvdt_max,
            "topology_null": bool(topology_null),
            "passes": bool(topology_null and A2_seed > 0.0),
        }

    def _vent_to_seed(self, e_vent: float):
        """Deliver an impulsive LONGITUDINAL pulse of energy `e_vent` into the
        seed: a ∂_tV velocity kick over the seed window carries vent_near_frac
        (near-field); the remainder is tracked as radiated (spherical remainder).
        Energy-accounted (driver-honesty: a labeled model coupling — the GAP-C
        surface)."""
        if e_vent <= 0.0 or not getattr(self, "vent_into_seed", False):
            return
        w = self._seed_window
        e_near = self.vent_near_frac * e_vent
        norm = float(np.sum((w ** 2) * self.interior_mask())) * self.dx ** 3 + 1e-30
        dv = np.sqrt(2.0 * e_near / norm)  # kick amplitude s.t. ½∫(dv·w)²dV = e_near
        # add dv·w to ∂_tV = (V−V_prev)/dt  ⇒  V_prev -= dv·w·dt
        self.V_prev = self.V_prev - dv * w * self.dt
        self.E_vent_to_seed += e_near
        self.E_vent_radiated += (1.0 - self.vent_near_frac) * e_vent

    # ----------------------------------------------------- bulk observers (CP6/CP7)
    def bulk_vorticity_z(self) -> np.ndarray:
        """ζ_z = ∂_x u_y − ∂_y u_x (the spin-axis vorticity component)."""
        return self._d(self.u_adv[..., 1], 0, self.dx) - self._d(self.u_adv[..., 0], 1, self.dx)

    def bulk_circulation_z(self, radius_frac: float = 0.6) -> float:
        """Γ_z = ∬ζ_z dA over a mid-plane disk (the conserved-invariant check)."""
        z = self.bulk_vorticity_z()
        mid = self.N // 2
        a1, a2 = self._bx[:, :, mid], self._by[:, :, mid]
        rc = np.sqrt(a1 ** 2 + a2 ** 2)
        mask = (rc < radius_frac * 0.5 * self.N * self.dx)
        return float(np.sum(z[:, :, mid][mask]) * self.dx ** 2)

    def rho_core(self):
        """Deepest (most-negative) ρ̄ in the PML/interior-excluded region, sampled
        at the density MINIMUM (CP7 — for a rarefying core this IS the peak of
        |deficit|, not a centroid+offset)."""
        m = self.interior_mask()
        masked = np.where(m, self.rho_bar, np.inf)
        idx = np.unravel_index(int(np.argmin(masked)), masked.shape)
        return float(self.rho_bar[idx]), (int(idx[0]), int(idx[1]), int(idx[2]))

    def c2_core(self):
        rc, _ = self.rho_core()
        rca = np.array(rc)
        return float(self.c_bulk2_raw(rca)), float(self.c_bulk2(rca))

    def bulk_kinetic_energy(self) -> float:
        rho_full = 1.0 + self.rho_bar
        return float(0.5 * np.sum(rho_full * np.sum(self.u_adv ** 2, axis=-1)) * self.dx ** 3)

    def bulk_compression_pe(self) -> float:
        """Labeled linear-acoustic PE proxy ½c₀²∫ρ̄² (exact in linear regime;
        driver-honesty: a proxy near the floor — use the exact pressure ledger D6)."""
        return float(0.5 * self.c0 ** 2 * np.sum(self.rho_bar ** 2) * self.dx ** 3)

    def bulk_pressure_integral(self) -> float:
        """∫p(ρ̄) dV over the interior — the EXACT-EOS bulk ledger the D6 flash
        detector differentiates (the longitudinal-burst signature lives here)."""
        m = self.interior_mask()
        return float(np.sum(self.pressure(self.rho_bar) * m) * self.dx ** 3)

    def bulk_snapshot(self) -> dict:
        rc, idx = self.rho_core()
        c2raw, c2cl = self.c2_core()
        return {
            "t": self.time,
            "step": self.step_count,
            "bulk_step": self.bulk_step_count,
            "rho_core": rc,
            "core_idx": list(idx),
            "c2_core_raw": c2raw,
            "c2_core_clipped": c2cl,
            "bulk_KE": self.bulk_kinetic_energy(),
            "bulk_PE_proxy": self.bulk_compression_pe(),
            "bulk_p_integral": self.bulk_pressure_integral(),
            "Gamma_z": self.bulk_circulation_z(),
            "clip_rho_hits": self.clip_rho_hits,
            "clip_c2_hits": self.clip_c2_hits,
            "max_abs_u": float(np.max(np.abs(self.u_adv))),
        }

    def __repr__(self):
        return (
            f"UnifiedGenesisEngine(N={self.N}, dt={self.dt:.3e}, "
            f"bulk_density={self.bulk_density_on}, photon_coupling={self.photon_coupling}, "
            f"lock={self.lock_on}(η={self.lock_eta:.3f}), κ̃={self.kappa_tilde}, step={self.step_count})"
        )
