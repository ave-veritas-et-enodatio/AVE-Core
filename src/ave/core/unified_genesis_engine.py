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
        # --- v6 hygiene (D10/D11); ALL default to the v5 byte-identical path ---
        vent_mode: str = "kick",
        snap_accounting: str = "legacy",
        meissner_harden: float = 0.0,
        # --- v8 D17 SPARE-THE-FEEDSTOCK: how the snap quenches u_adv in snapped
        # cells. "inherited" = u_adv[cm]=0.0 EXACTLY as v6 (byte-identical default);
        # "wall_normal" = zero only the wall-normal component (project out u_n =
        # grad(rho)/|grad(rho)|), PRESERVE the tangential circulation feedstock;
        # "channel_live" = do NOT zero snapped shell cells bordering the D16
        # channel (the conducting tube stays live). A NEW knob ⇒ inventoried +
        # swept (ave-apparatus-floor-attribution v1.1; §5 row 2). The removed-KE
        # ledger (E_reflect) tallies ONLY what is actually removed (honest sink). ---
        snap_u_mode: str = "inherited",
        # --- v6 D9 transducer (chiral-boundary spin-orbit exchange BC); OFF by default ---
        transducer_on: bool = False,
        chi_exch: float = 0.02,
        bounce_thresh: float = 1.5,
        transduce_axis: int | None = None,
        # --- v6 PHASE-3 ω-recipient (the Cosserat winding channel wired back on) ---
        # omega_recipient_frac splits the extracted δL between the ω micro-rotation
        # carrier (frac) and the u_adv orbital circulation (1−frac). 0.0 ⇒ pure
        # u_adv = the PHASE-2 smoke / keeper byte-identical path. A NEW knob ⇒
        # inventoried + swept (ave-apparatus-floor-attribution v1.1; §210).
        omega_recipient_frac: float = 0.0,
        # --- v7 D13 QUADRATURE DEPOSIT (poloidal-projecting δπ_ω); OFF by default ---
        # quadrature_deposit=False ⇒ the v6 RIGID-azimuthal ω-deposit path is
        # byte-identical (the D-INHERIT keeper). When True the ω-deposit branch
        # ADDS a poloidal LC-quadrature winding on the g_wall shell (winding-capable
        # in the w_pol read coordinate — derived in the prereg §3 + this session's
        # plant-at-scale prototype). NEW knobs ⇒ inventoried + swept (§5).
        quadrature_deposit: bool = False,
        alpha_pol: float = 1.0,   # deposit-SHAPE knob: 0 ⇒ no poloidal (v6 rigid); 1 ⇒ full poloidal winding
        q_dep: int = 3,           # target poloidal winding order (the "3")
        p_dep: int = 2,           # toroidal director order (the "2")
        pol_R: float | None = None,  # reading-torus major radius (None ⇒ 0.22·N at build)
        pol_r: float | None = None,  # reading-torus minor radius (None ⇒ R/φ²)
        # --- v8 D15 POLYPHASE CONDUCTION (the rotating-field stator on the threaded
        # channel; OFF by default ⇒ the v6/v7 byte-identical path). A per-step
        # BOUNDARY deposit (CP10) of a TRAVELING poloidal π_ω wave on the channel-
        # wall contour, amplitude set BY the extracted photon δL (D13-FAITHFUL),
        # travel direction set BY the photon helicity (helicity-odd). N_phase=1 ⇒
        # the STANDING/pulsating single-phase control (the v7 reproduction). ---
        polyphase_on: bool = False,
        n_phase: int = 1,
        Omega_stator: float | None = None,  # default = q_dep*omega_gap (the §3.5(2) fast re-imprint)
        dep_R: float | None = None,          # the channel-derived major radius (driver sets from D16)
        dep_r: float = 3.0,                  # the minor circle (channel-wall thickness)
        dep_axis: int | None = None,         # the spin/threading axis (None ⇒ transduce axis)
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
        # v6 hygiene knobs (D10/D11) — default values reproduce the v5 path exactly
        self.vent_mode = str(vent_mode)            # "kick" (v5) | "absorbed" (D10a)
        self.snap_accounting = str(snap_accounting)  # "legacy" (v5) | "conservative" (D11)
        self.meissner_harden = float(meissner_harden)  # D10b per-cell threshold hardening
        # v8 D17 feedstock-sparing rendering (default = the v6 byte-identical path)
        self.snap_u_mode = str(snap_u_mode)
        # the D16 channel mask the driver sets from the topology gate (for
        # snap_u_mode="channel_live"); None ⇒ the rendering falls back to inherited.
        self.channel_mask = None
        self.snap_channel_border = 2  # cells of channel-wall shell kept live (mode b)
        # --- v6 D9 transducer (chiral-boundary spin-orbit exchange BC) ---
        # CP10 boundary-localized; OFF by default (the inherited byte-identical path).
        # chi_exch = the SWEPT per-step wall spin-extraction fraction (prereg §6.5);
        # bounce_thresh = the bounce-COUNT detector level (cosmetic, swept);
        # transduce_axis = the spin axis n̂ (None ⇒ foc_axis at transduce time).
        self.transducer_on = bool(transducer_on)
        self.chi_exch = float(chi_exch)
        self.bounce_thresh = float(bounce_thresh)
        self.transduce_axis = transduce_axis  # int or None
        self.omega_recipient_frac = float(min(max(omega_recipient_frac, 0.0), 1.0))
        # --- v7 D13 quadrature-deposit config (default OFF = v6 byte-identical) ---
        self.quadrature_deposit = bool(quadrature_deposit)
        self.alpha_pol = float(min(max(alpha_pol, 0.0), 1.0))
        self.q_dep = int(q_dep)
        self.p_dep = int(p_dep)
        _phi2 = ((1.0 + np.sqrt(5.0)) / 2.0) ** 2
        self.pol_R = float(pol_R) if pol_R is not None else 0.22 * self.N
        self.pol_r = float(pol_r) if pol_r is not None else self.pol_R / _phi2
        # v7 D13 ledgers (the poloidal winding is a SEPARATE, zero-net-axial-AM
        # helicity imprint added ON TOP of the v6 1:1 rigid AM transfer; its
        # accumulator is BOOKKEEPING, never the headline — the gross-vs-field rule):
        self.pol_deposit_accum = 0.0    # cumulative deposited poloidal amplitude tally (signed, helicity-odd)
        self.E_pol_deposit = 0.0        # cumulative energy placed in the poloidal winding (drawn from photon, ≥0)
        self.pol_deposit_events = 0     # steps the poloidal branch fired
        # --- v8 D15 polyphase conduction state (OFF default = byte-identical) ---
        self.polyphase_on = bool(polyphase_on)
        self.n_phase = int(n_phase)
        self.Omega_stator = (float(Omega_stator) if Omega_stator is not None
                             else None)  # resolved lazily against omega_gap
        self.dep_R = (float(dep_R) if dep_R is not None else None)
        self.dep_r = float(dep_r)
        self.dep_axis = dep_axis
        # D15 ledgers (the AM channel: amplitude IS the extracted photon δL)
        self.L_deposit_poloidal = 0.0   # cumulative δL routed into the traveling poloidal deposit
        self.S_photon_removed_poly = 0.0  # cumulative photon spin removed by the polyphase BC
        self.E_poly_photon_loss = 0.0   # energy removed from the photon (≥0)
        self.poly_events = 0            # steps the polyphase deposit fired
        self._poly_phase = 0.0          # the traveling temporal phase accumulator s_h·Ω·t
        # D9 ledgers (the AM channel closes 1:1 BY CONSTRUCTION; energy TRACKED):
        self.L_transferred = 0.0          # cumulative ΔL deposited (u_adv + ω, = removed)
        self.L_transferred_u = 0.0        # cumulative ΔL into u_adv orbital circulation
        self.L_transferred_omega = 0.0    # cumulative ΔL into the ω micro-rotation carrier
        self.S_photon_removed = 0.0       # cumulative photon spin removed (= L_transferred exactly)
        self.E_transduce_photon_loss = 0.0  # energy removed from the photon (≥0 by construction)
        self.E_transduce_bulk_gain = 0.0    # actual bulk-KE change from the u_adv deposit (±)
        self.E_transduce_omega_gain = 0.0   # actual ω-tank energy change from the ω deposit (±)
        self.E_transduce_absorbed = 0.0     # passive lossy-mirror sink = loss − gains (≥0 ⇒ no pump)
        self.transduce_events = 0           # steps the transducer fired
        self.snap_mask = np.zeros((Nn, Nn, Nn), dtype=bool)
        self.latent_ledger = np.zeros((Nn, Nn, Nn), dtype=np.float64)  # held-out per cell
        self.paid_ledger = np.zeros((Nn, Nn, Nn), dtype=np.float64)    # paid-back per cell
        # per-cell snap THRESHOLD + clamp value (the D10b Meissner hook lowers the
        # threshold; uniform = rho_cav ⇒ byte-identical to the v5 scalar path).
        self.rho_cav_field = np.full((Nn, Nn, Nn), self.rho_cav, dtype=np.float64)
        self.snap_clamp_val = np.full((Nn, Nn, Nn), self.rho_cav, dtype=np.float64)
        # cumulative scalar ledgers (energy bookkeeping; the tally must close)
        self.E_latent_held = 0.0   # currently held out of the dynamics (sum of latent_ledger)
        self.E_latent_restored = 0.0  # paid-back-and-returned (cumulative)
        self.E_diss_snap = 0.0     # shock-class one-way (chi_shock·void-KE)
        self.E_vent_absorbed = 0.0  # D10(a) conservative store (the vent-absorbed sink)
        self.E_reflect = 0.0       # D11 conservative: per-step reflector-BC KE removed
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
        # per-cell clamp floor: rho_cav (legacy/scalar) OR the cell's own threshold
        # (conservative/Meissner — set in _snap_step before this call).
        legacy = self.snap_accounting == "legacy"
        clamp = self.rho_cav if legacy else self.snap_clamp_val[newly]
        # reversible internal-energy released crossing to the (per-cell) floor
        d_eps = np.abs(self.U_density(rb_before) - self.U_density(clamp))
        # shock-class void KE removed (one-way)
        rho_full = 1.0 + rb_before
        ke_void = 0.5 * rho_full * np.sum(self.u_adv[newly] ** 2, axis=-1)
        if legacy:
            # v5 path (byte-identical): latent holds d_eps + chi·ke_void. NOTE the
            # chi·ke_void is ALSO booked to diss/vent below — the DOUBLE-COUNT D11
            # isolates (the shock KE is held AND dissipated; the +5.6% residual pump).
            latent_cell = (d_eps + self.chi_shock * ke_void) * self.dx ** 3
        else:
            # D11 conservative: latent holds ONLY the reversible internal energy
            # (the un-snap payback threshold); the shock KE is the IRREVERSIBLE
            # one-way destination, booked ONCE (de-double-count).
            latent_cell = d_eps * self.dx ** 3
        self.latent_ledger[newly] = latent_cell
        self.paid_ledger[newly] = 0.0
        self.E_latent_held += float(np.sum(latent_cell))
        e_shock = float(np.sum(self.chi_shock * ke_void) * self.dx ** 3)
        # VENT routing: D10(a) absorbed (conservative store, no V-kick — the pump
        # fix) | D2 vent-into-seed (the v5 ∂_tV kick = the Class-C pump trigger) |
        # pure one-way dissipative sink.
        if self.vent_mode == "absorbed":
            self.E_vent_absorbed += e_shock
        elif getattr(self, "vent_into_seed", False):
            self._vent_to_seed(e_shock)
        else:
            self.E_diss_snap += e_shock
        # remove the crossing KE (shock), clamp to the void floor (track added mass)
        self.u_adv[newly] *= (1.0 - self.chi_shock)
        self.mass_clamp += float(np.sum(np.clip(clamp - rb_before, 0.0, None)) * self.dx ** 3)
        self.rho_bar[newly] = clamp
        self.snap_mask[newly] = True
        self.snap_events += int(np.count_nonzero(newly))
        # D10(b) MEISSNER: each newly-snapped cell RAISES neighbors' snap threshold.
        if self.meissner_harden > 0.0:
            self._meissner_harden_neighbors(newly)

    def _meissner_harden_neighbors(self, newly):
        """D10(b) — each newly-snapped cell LOWERS (hardens) its 6-neighbors' snap
        threshold by `meissner_harden` (more-negative ⇒ a deeper deficit needed to
        snap). Floored at rho_floor (the integrable band). Negative feedback: the
        cascade front must reach ever-deeper deficits, so it NUCLEATES-AND-STOPS
        (real condensation). CP10: a per-cell BOUNDARY threshold, NOT a bulk force."""
        nb = np.zeros_like(self.snap_mask)
        for ax in range(3):
            nb |= np.roll(newly, 1, axis=ax) | np.roll(newly, -1, axis=ax)
        nb &= ~self.snap_mask & self.interior_mask()
        self.rho_cav_field[nb] -= self.meissner_harden
        np.maximum(self.rho_cav_field, self.rho_floor + 1e-3, out=self.rho_cav_field)

    def _snap_quench_u(self, cm):
        """D17 SPARE-THE-FEEDSTOCK — the post-snap u_adv values in snapped cells,
        per ``snap_u_mode``. Returns an (M,3) array (M = cm.sum()).

          "inherited"    u_adv = 0.0 EXACTLY (the v6 byte-identical path).
          "wall_normal"  zero only the wall-normal component (project out
                         û_n = ∇ρ̄/|∇ρ̄|), PRESERVE the tangential circulation — the
                         snap still kills the in/out shock but keeps the swirl
                         feedstock. Degenerate normal (|∇ρ̄|<eps) ⇒ full quench.
          "channel_live" keep u_adv in snapped shell cells bordering the D16
                         channel mask (the conducting tube stays live); zero the
                         rest. No channel mask set ⇒ inherited (fail-safe).

        CP10: this is a per-cell BOUNDARY state operation (the same boundary state
        machine the inherited snap is), NOT a bulk EOM force."""
        u_cm = self.u_adv[cm]
        mode = self.snap_u_mode
        if mode == "inherited" or u_cm.size == 0:
            return np.zeros_like(u_cm)
        if mode == "wall_normal":
            gx, gy, gz = np.gradient(self.rho_bar, self.dx)
            gn = np.stack([gx[cm], gy[cm], gz[cm]], axis=-1)
            mag = np.sqrt(np.sum(gn ** 2, axis=-1))
            # default PRESERVE: where ∇ρ̄ is degenerate (a flat deep-void interior)
            # NO wall normal is defined ⇒ there is no in/out shock to remove ⇒ keep
            # the circulation (the free-slip reflector kills only the no-penetration-
            # violating NORMAL component, not the tangential swirl feedstock).
            out = u_cm.copy()
            good = mag > 1e-9
            if np.any(good):
                nh = gn[good] / mag[good][:, None]
                u_good = u_cm[good]
                u_norm = np.sum(u_good * nh, axis=-1)[:, None] * nh
                out[good] = u_good - u_norm  # remove wall-normal, keep tangential
            return out
        if mode == "channel_live":
            if self.channel_mask is None:
                return np.zeros_like(u_cm)
            from scipy import ndimage
            border = ndimage.binary_dilation(
                np.asarray(self.channel_mask, dtype=bool),
                iterations=int(self.snap_channel_border))
            keep = border[cm]  # snapped cells adjacent to the channel
            out = np.zeros_like(u_cm)
            out[keep] = u_cm[keep]  # the channel-wall feedstock stays live
            return out
        return np.zeros_like(u_cm)  # unknown mode ⇒ inherited (fail-safe)

    def _snap_step(self):
        """Per-cell snap state machine (normal↔snapped), interior only (CP7).
          1. newly-snapping cells (ρ̄≤ρ̄_cav, not yet snapped) ⇒ tally + clamp.
          2. already-snapped cells ⇒ enforced void (reflector BC) + over-pressure
             payback accrual.
          3. cells whose tally is PAID BACK ⇒ un-snap (re-enter above the floor;
             the held latent is RESTORED to the dynamics ledger). NO new EOS."""
        m = self.interior_mask()
        legacy = self.snap_accounting == "legacy"
        # (1) crossings — per-cell threshold rho_cav_field (≡ rho_cav unless Meissner
        # hardened); broadcasting over a uniform field is byte-identical to the scalar.
        below = (self.rho_bar <= self.rho_cav_field) & m & ~self.snap_mask
        if below.any():
            if not legacy:
                # the cell clamps/holds at its own threshold (Meissner-aware)
                self.snap_clamp_val[below] = self.rho_cav_field[below]
            self._tally_latent_and_snap(below)
        if not self.snap_mask.any():
            return
        cm = self.snap_mask
        # (2) enforce the boundary-class void (reflector: ρ̄ held at floor, u killed
        # per the D17 rendering). D11 conservative: TALLY the reflector-removed KE
        # (one-way physical sink) so the ledger closes — the v5 legacy path destroys
        # it untallied. v8 D17: the rendering may PRESERVE part of u_adv (the spared
        # circulation feedstock); the tally counts ONLY the removed component so the
        # ledger stays honest whatever is spared (the F-CASCADE keeper depends on it).
        u_new_cm = self._snap_quench_u(cm)  # the post-snap u_adv in snapped cells
        if not legacy:
            removed = self.u_adv[cm] - u_new_cm
            self.E_reflect += float(np.sum(
                0.5 * (1.0 + self.rho_bar[cm]) * np.sum(removed ** 2, axis=-1)
            ) * self.dx ** 3)
            self.rho_bar[cm] = self.snap_clamp_val[cm]
        else:
            self.rho_bar[cm] = self.rho_cav
        self.u_adv[cm] = u_new_cm
        # over-pressure payback: the surrounding medium does work against the void.
        # neighbor-mean pressure minus the (per-cell) void pressure; positive ⇒ in.
        p = self.pressure(self.rho_bar)
        p_neigh = (np.roll(p, 1, 0) + np.roll(p, -1, 0)
                   + np.roll(p, 1, 1) + np.roll(p, -1, 1)
                   + np.roll(p, 1, 2) + np.roll(p, -1, 2)) / 6.0
        if legacy:
            over = np.clip(p_neigh - self.pressure(np.array(self.rho_cav)), 0.0, None)
        else:
            over = np.clip(p_neigh - self.pressure(self.snap_clamp_val), 0.0, None)
        self.paid_ledger[cm] += over[cm] * self.dx ** 3 * self.snap_payback_rate * self.dt
        # (3) un-snap the paid-up cells (re-enter above floor; restore the latent)
        paid_up = cm & (self.paid_ledger >= self.latent_ledger) & (self.latent_ledger > 0.0)
        if paid_up.any():
            restored = float(np.sum(self.latent_ledger[paid_up]))
            self.E_latent_held -= restored
            self.E_latent_restored += restored
            floor = self.rho_cav if legacy else self.snap_clamp_val[paid_up]
            self.rho_bar[paid_up] = floor + self.delta_heal
            self.snap_mask[paid_up] = False
            self.latent_ledger[paid_up] = 0.0
            self.paid_ledger[paid_up] = 0.0
            self.unsnap_events += int(np.count_nonzero(paid_up))

    # ===================================== D9 TRANSDUCER (chiral-boundary BC, CP10)
    def _transduce_axis(self) -> int:
        """The spin axis n̂ for the transducer: the explicit override, else the
        FOC/drive axis, else z (=2)."""
        if self.transduce_axis is not None:
            return int(self.transduce_axis)
        return int(getattr(self, "foc_axis", 2))

    def photon_spin_axial(self, axis: int | None = None, wall_weighted: bool = False) -> float:
        """The photon's axial mechanical SPIN  S_φ = ∫ (w × ∂_tw)·n̂ dV  (interior).
        For a CP shear photon S_φ ∝ −h·k·∫|w|² (HELICITY-ODD); a linear-pol
        (achiral) photon has one transverse component ⇒ S_φ ≡ 0. This is the
        depletable photon-helicity ledger the transducer pays from (the m-even
        keeper probe — it MUST separate ±helicity on a known seed)."""
        if axis is None:
            axis = self._transduce_axis()
        piw = (self.w - self.w_prev) / self.dt
        s_dens = np.cross(self.w, piw)[..., axis]
        weight = self.interior_mask().astype(np.float64)
        if wall_weighted:
            weight = weight * self._wall_window()
        return float(np.sum(s_dens * weight) * self.dx ** 3)

    def wall_photon_intensity(self) -> float:
        """I_wall = ∫ g_wall·|∂_tw|² dV — the wall-shell photon intensity. Its
        peaks COUNT the bounces (the per-bounce normalization; the bounce_thresh
        knob sets the count level — cosmetic, does not move the total transfer)."""
        piw = (self.w - self.w_prev) / self.dt
        gw = self._wall_window() * self.interior_mask()
        return float(np.sum(gw * np.sum(piw ** 2, axis=-1)) * self.dx ** 3)

    # ===================================================== v7 D13 quadrature deposit
    def _quadrature_deposit_pattern(self, amp, s_h, window):
        """Build the (δω, δπ_ω) LC-quadrature winding increment on `window` (the
        g_wall shell), about the z spin-axis, IN THE SAME (φ,ψ,d̂) coordinate the
        w_pol extractor reads (phase-space-coordinate-check A46):

          φ = arctan2(y,x) ;  ρ = √(x²+y²) ;  ψ = arctan2(z, ρ−pol_R)
          D = cos(p·φ)·ρ̂ + sin(p·φ)·ẑ           (the canonical unit director, |D|=1)
          δω    = amp·window·D·cos(q·ψ)           (C-state ω increment)
          δπ_ω  = amp·window·D·s_h·sin(q·ψ)        (L-state π_ω increment; quadrature)

        DERIVED + plant-at-scale-validated this session: this is the SAME functional
        form as the canonical planted-(2,3) (`seed_omega_known_2_3`) that the
        extractor is bit-validated to read as w_pol=q. The read coordinate PROVABLY
        requires the co-deposited C-state — a pure δπ_ω (the prereg §3.3 sketch)
        plants no ω·d̂ and reads w_pol=0 (validated: w_pol 3 with C-state vs 0
        without). So the v7 deposit is the FULL LC quadrature, NOT δπ_ω-only — a
        DERIVED strengthening of the prereg sketch (surfaced, flag-don't-fix).

        Zero net axial AM (the cos/sin(qψ) winding integrates out around ψ) ⇒ the
        lock's net-L removal does not drain it (the structural-block mechanism §3.4).
        s_h = sign(extracted dL) = handedness ⇒ the winding sign reverses RH↔LH
        (helicity-odd). Restricted to the z spin-axis (the extractor's torus axis;
        the genesis foc_axis=2) so the deposit + read share the coordinate."""
        p, q = self.p_dep, self.q_dep
        x, y, z = self._bx, self._by, self._bz
        rho = np.sqrt(x ** 2 + y ** 2)
        safe = rho > 1e-9
        inv = np.where(safe, 1.0 / np.where(safe, rho, 1.0), 0.0)
        phi = np.arctan2(y, x)
        psi = np.arctan2(z, rho - self.pol_R)
        dRr = np.cos(p * phi)
        dz = np.sin(p * phi)
        director = np.empty_like(self.omega)
        director[..., 0] = dRr * x * inv     # cos(pφ)·x̂·(x/ρ) = cos(pφ)·cosφ
        director[..., 1] = dRr * y * inv     # cos(pφ)·sinφ
        director[..., 2] = dz                # sin(pφ)
        base = (amp * window)[..., None] * director
        d_omega = base * np.cos(q * psi)[..., None]
        d_pi = base * (s_h * np.sin(q * psi))[..., None]
        return d_omega, d_pi

    def poloidal_quadrature_content(self, axis: int = 2, q: int | None = None):
        """The NET-FIELD poloidal-winding quantity the v7 survival gate measures
        (gross-vs-field §10), read in the MATCHING phase-space coordinate (A46):
        the signed chiral q-harmonic amplitude of the ω-tank LC quadrature
        Z=(ω·d̂)+i(π_ω·d̂) on the reading torus (pol_R, pol_r).

        Per toroidal walk: Park-project (ω,π_ω) onto the principal axis d̂ of the ω
        covariance over the minor circle (the extractor's d̂), form Z(ψ), take the
        ±q Fourier coefficients A_±q = ⟨Z·e∓iqψ⟩_ψ. Returns the median-over-walks
        C_pol = |A_+q|−|A_−q| (helicity-odd: +q vs −q dominance = the winding
        chirality). This is a FIELD measurement (MAIN−OFF of it = the net deposit),
        NOT the accumulator. axis kept for signature symmetry; z-torus per the
        extractor."""
        from ave.utils.fast_winding_extractor import interp_vec_batch
        if q is None:
            q = self.q_dep
        N = self.N
        c = (N - 1) / 2.0
        R, r = self.pol_R, self.pol_r
        n_walks, n_ang = 12, 240
        phi0 = np.linspace(0.0, 2 * np.pi, n_walks, endpoint=False)
        psis = np.linspace(0.0, 2 * np.pi, n_ang, endpoint=False)
        PHI0 = np.broadcast_to(phi0[:, None], (n_walks, n_ang))
        PSI2 = np.broadcast_to(psis[None, :], (n_walks, n_ang))
        pw = (self.omega - self.omega_prev) / self.dt
        op, vmask_o = interp_vec_batch(self.omega, c, R, r, PHI0, PSI2, N)
        pp, vmask_p = interp_vec_batch(pw, c, R, r, PHI0, PSI2, N)
        vmask = vmask_o & vmask_p
        cphi0, sphi0 = np.cos(phi0), np.sin(phi0)
        OeR = op[..., 0] * cphi0[:, None] + op[..., 1] * sphi0[:, None]
        Oz = op[..., 2]
        PeR = pp[..., 0] * cphi0[:, None] + pp[..., 1] * sphi0[:, None]
        Pz = pp[..., 2]
        eipq = np.exp(-1j * q * psis)   # for A_+q
        eimq = np.exp(+1j * q * psis)   # for A_-q
        c_list = []
        for wlk in range(n_walks):
            idx = np.nonzero(vmask[wlk])[0]
            if len(idx) < 16:
                continue
            O = np.stack([OeR[wlk, idx], Oz[wlk, idx]], axis=1)
            P = np.stack([PeR[wlk, idx], Pz[wlk, idx]], axis=1)
            cov = O.T @ O
            evals, evecs = np.linalg.eigh(cov)
            dhat = evecs[:, np.argmax(evals)]
            Z = (O @ dhat) + 1j * (P @ dhat)
            full = np.zeros(n_ang, dtype=complex)
            full[idx] = Z
            Apq = np.mean(full * eipq)
            Amq = np.mean(full * eimq)
            c_list.append(abs(Apq) - abs(Amq))
        return float(np.median(c_list)) if c_list else 0.0

    def _transducer_step(self):
        """D9 — the chiral-boundary spin-orbit exchange BC (prereg §6.1; CP10).

        A per-cell BOUNDARY operation on the g_wall shell ONLY (NOT a bulk EOM
        term — the v5 detonation lesson): per step the chiral wall torques the
        ANGULAR pair (the polar-conjugate of the snap's radial reflector). It
        (1) extracts photon axial spin Δs(r)=χ̃·g_wall(r)·s_density(r) by scaling
        π_w←π_w·(1−χ̃·g_wall) — s_density is LINEAR in π_w so the removed spin is
        EXACTLY δL=Σ Δs·dV; (2) deposits exactly δL into u_adv as a wall-localized
        azimuthal increment δu=Ω_add·(n̂×r)·g_wall, Ω_add=δL/I_wall. The AM ledger
        closes 1:1 BY CONSTRUCTION (bounded, depleting, no refilled source). The
        ENERGY is TRACKED (passive lossy mirror: E_absorb=loss−bulk_gain≥0 ⇒ no
        pump — ave-conserved-vs-pumped, the D11 discipline on the transducer)."""
        n = self._transduce_axis()
        chi = self.chi_exch
        gw = self._wall_window() * self.interior_mask()
        if chi == 0.0 or not np.any(gw > 0.0):
            return
        # --- the photon's axial spin density s = (w × π_w)·n̂ (linear in π_w) ---
        piw = (self.w - self.w_prev) / self.dt
        s_dens = np.cross(self.w, piw)[..., n]
        # per-cell extracted spin Δs = χ̃·g_wall·s_dens ; total δL (signed = handedness)
        extract_frac = chi * gw                       # the per-cell scaling depth (≤ χ̃)
        dL = float(np.sum(extract_frac * s_dens) * self.dx ** 3)
        # --- (2) DEPOSIT exactly δL into u_adv (orbital), wall-localized azimuthal ---
        rho_full = 1.0 + self.rho_bar
        # (n̂×r) deposited as du[c1]=Ω(−r2), du[c2]=Ω(+r1); r_⊥²=r1²+r2².
        if n == 2:
            r1, r2, c1, c2 = self._bx, self._by, 0, 1   # ẑ×r = (−y, x, 0)
        elif n == 1:
            r1, r2, c1, c2 = self._bz, self._bx, 2, 0   # ŷ×r = (z, 0, −x)
        else:
            r1, r2, c1, c2 = self._by, self._bz, 1, 2   # x̂×r = (0, −z, y)
        perp2 = r1 ** 2 + r2 ** 2
        I_wall = float(np.sum(rho_full * gw * perp2) * self.dx ** 3)
        if abs(I_wall) > 1e-30 and dL != 0.0:
            # SPLIT the extracted δL between the ω micro-rotation carrier (PHASE-3
            # winding channel) and the u_adv orbital circulation. frac=0 ⇒ pure
            # u_adv (the PHASE-2 smoke / keeper byte-identical path).
            f_om = self.omega_recipient_frac
            dL_u = (1.0 - f_om) * dL
            dL_om = f_om * dL
            ke_delta = 0.0
            e_omega_gain = 0.0
            e_pol_gain = 0.0  # v7 D13 poloidal-winding energy (drawn from photon-loss budget)
            # --- (2a) DEPOSIT dL_u into u_adv (orbital), wall-localized azimuthal ---
            if dL_u != 0.0:
                Omega_u = dL_u / I_wall
                # δu = Ω_u·(n̂×r)·g_wall : axial-symmetric azimuthal spin-up of the shell.
                du = np.zeros_like(self.u_adv)
                du[..., c1] = Omega_u * (-r2) * gw
                du[..., c2] = Omega_u * (r1) * gw
                u = self.u_adv
                ke_delta = float(np.sum(
                    rho_full * (np.sum(u * du, axis=-1) + 0.5 * np.sum(du ** 2, axis=-1))
                ) * self.dx ** 3)
                self.u_adv = u + du
            # --- (2b) DEPOSIT dL_om into the ω carrier as a wall-localized azimuthal
            # increment of π_ω (= the L-state of the ω reactance pair). I_wall_om uses
            # unit weight (ω is its own field, not advected by ρ). The axial ω angular
            # momentum increment ∫(r×δπ_ω)·n̂ = Ω_om·I_wall_om = dL_om EXACTLY. CP10:
            # this is a per-cell BOUNDARY operation on the g_wall shell (not an ω-EOM
            # term). It deposits a RIGID azimuthal rotation — it does NOT plant a
            # poloidal (2,3) winding (whether one EMERGES is the open T2 question). ---
            if dL_om != 0.0:
                I_wall_om = float(np.sum(gw * perp2) * self.dx ** 3)
                if abs(I_wall_om) > 1e-30:
                    Omega_om = dL_om / I_wall_om
                    dpi = np.zeros_like(self.omega)
                    dpi[..., c1] = Omega_om * (-r2) * gw
                    dpi[..., c2] = Omega_om * (r1) * gw
                    piw_om = (self.omega - self.omega_prev) / self.dt
                    e_omega_gain = float(np.sum(
                        np.sum(piw_om * dpi, axis=-1) + 0.5 * np.sum(dpi ** 2, axis=-1)
                    ) * self.dx ** 3)
                    # increase π_ω by dpi: ω_prev ← ω − (π_ω+dpi)·dt = ω_prev − dpi·dt
                    self.omega_prev = self.omega_prev - dpi * self.dt
                    self.L_transferred_omega += dL_om
                    # --- (2c) v7 D13: the POLOIDAL QUADRATURE WINDING (added ON TOP
                    # of the rigid 1:1 AM transfer above, so the v6 AM ledger is
                    # untouched). A zero-net-axial-AM (δω,δπ_ω) LC-quadrature on the
                    # g_wall shell, winding-capable in the w_pol read coordinate
                    # (DERIVED §3 + plant-at-scale-validated). The photon's mechanical
                    # axial AM still goes to the rigid mode (lock-drained, v6); its
                    # HELICITY is imprinted here as the poloidal winding the lock's
                    # net-L removal cannot drain (the structural-block mechanism). The
                    # poloidal energy is drawn from the photon-loss budget (passive:
                    # E_absorbed≥0 tracked). amp = α_pol·Ω_om·pol_r; sign = sign(dL_om)
                    # = handedness ⇒ helicity-odd winding. CP10 boundary-local. ---
                    if self.quadrature_deposit and self.alpha_pol > 0.0 and n == 2:
                        s_h = 1.0 if dL_om >= 0.0 else -1.0
                        amp_pol = self.alpha_pol * Omega_om * self.pol_r
                        d_om_pol, d_pi_pol = self._quadrature_deposit_pattern(
                            amp_pol, s_h, gw)
                        piw_om2 = (self.omega - self.omega_prev) / self.dt
                        e_pol_gain = float(np.sum(
                            np.sum(piw_om2 * d_pi_pol, axis=-1)
                            + 0.5 * np.sum(d_pi_pol ** 2, axis=-1)
                            + (self.omega_gap ** 2) * (
                                np.sum(self.omega * d_om_pol, axis=-1)
                                + 0.5 * np.sum(d_om_pol ** 2, axis=-1))
                        ) * self.dx ** 3)
                        # apply BOTH the C-state (δω) and L-state (δπ_ω) increments:
                        # ω ← ω+δω ;  ω_prev ← ω_prev+δω−δπ_ω·dt  (preserves π_ω+=δπ_ω)
                        self.omega = self.omega + d_om_pol
                        self.omega_prev = self.omega_prev + d_om_pol - d_pi_pol * self.dt
                        self.E_pol_deposit += abs(e_pol_gain)
                        self.E_transduce_omega_gain += e_pol_gain
                        # signed bookkeeping accumulator (NEVER the headline — §10)
                        self.pol_deposit_accum += s_h * amp_pol * float(
                            np.sum(gw) * self.dx ** 3)
                        self.pol_deposit_events += 1
                else:
                    dL_om = 0.0
            self.E_transduce_bulk_gain += ke_delta
            self.E_transduce_omega_gain += e_omega_gain
            self.L_transferred_u += dL_u
            self.L_transferred += (dL_u + dL_om)
            self.S_photon_removed += (dL_u + dL_om)
            # --- (1) the photon PAYS: scale π_w by (1−χ̃·g_wall) at the wall ---
            # the spin removed = dL = dL_u + dL_om (when both recipients are live the
            # extraction is scaled so the photon pays exactly what is deposited).
            pay_scale = (dL_u + dL_om) / dL  # =1 unless an ω deposit was dropped
            piw_loss = pay_scale * 0.5 * float(np.sum(
                np.sum(piw ** 2, axis=-1) * (1.0 - (1.0 - extract_frac) ** 2)
            ) * self.dx ** 3)
            self.E_transduce_photon_loss += piw_loss
            self.E_transduce_absorbed += (piw_loss - ke_delta - e_omega_gain - e_pol_gain)
            self.w_prev = self.w - (self.w - self.w_prev) * (
                1.0 - pay_scale * extract_frac)[..., None]
            self.transduce_events += 1

    def transducer_ledger(self) -> dict:
        """The D9 channel ledger (conservation-by-channel; numbers FROM the field).
        L_transferred ≡ S_photon_removed BY CONSTRUCTION (1:1 AM closure); the
        INDEPENDENT depletion evidence is the measured photon-spin change vs the
        free-drift floor (reported by the driver)."""
        ratio = (self.S_photon_removed / self.L_transferred
                 if abs(self.L_transferred) > 1e-30 else float("nan"))
        return {
            "L_transferred": self.L_transferred,
            "L_transferred_u": self.L_transferred_u,
            "L_transferred_omega": self.L_transferred_omega,
            "omega_recipient_frac": self.omega_recipient_frac,
            "S_photon_removed": self.S_photon_removed,
            "ledger_ratio_removed_over_transferred": ratio,
            "E_photon_loss": self.E_transduce_photon_loss,
            "E_bulk_gain": self.E_transduce_bulk_gain,
            "E_omega_gain": self.E_transduce_omega_gain,
            "E_absorbed_sink": self.E_transduce_absorbed,
            "passive_no_pump": bool(self.E_transduce_absorbed >= -1e-12),
            "transduce_events": self.transduce_events,
            "L_bulk_axial": self.angular_momentum_bulk(self._transduce_axis()),
            "L_omega_axial": self.angular_momentum_omega_axial(self._transduce_axis()),
            "S_photon_axial": self.photon_spin_axial(),
            # --- v7 D13 poloidal-winding channel (accumulator = BOOKKEEPING; the
            # headline is poloidal_quadrature_content (FIELD) — gross-vs-field §10) ---
            "quadrature_deposit": self.quadrature_deposit,
            "alpha_pol": self.alpha_pol,
            "q_dep": self.q_dep,
            "pol_deposit_accum": self.pol_deposit_accum,
            "E_pol_deposit": self.E_pol_deposit,
            "pol_deposit_events": self.pol_deposit_events,
            "C_pol_field": self.poloidal_quadrature_content(),
        }

    def angular_momentum_omega_axial(self, axis: int | None = None) -> float:
        """Axial angular momentum of the ω micro-rotation carrier's L-state,
        L_ω,n = ∫ (r×π_ω)·n̂ dV (interior). The SIGNED ω-channel AM the transducer
        deposits into (the helicity-odd recipient); spin_L_omega() is its magnitude."""
        if axis is None:
            axis = self._transduce_axis()
        pw = (self.omega - self.omega_prev) / self.dt
        m = self.interior_mask()
        if axis == 2:
            Ln = self._bx * pw[..., 1] - self._by * pw[..., 0]
        elif axis == 1:
            Ln = self._bz * pw[..., 0] - self._bx * pw[..., 2]
        else:
            Ln = self._by * pw[..., 2] - self._bz * pw[..., 1]
        return float(np.sum(Ln * m) * self.dx ** 3)

    # ===================================== D15 POLYPHASE CONDUCTION (CP10 stator BC)
    def _poly_geom(self):
        """The channel-wall torus window g_chan + the (p,q)-knot director D the
        extractor reads, in the deposit frame. R = the D16 channel-derived major
        radius (driver-set ``dep_R``), r = the channel-wall minor radius."""
        axis = int(self.dep_axis) if self.dep_axis is not None else self._transduce_axis()
        R = self.dep_R if self.dep_R is not None else (0.22 * self.N * self.dx)
        r = self.dep_r * self.dx
        others = [a for a in range(3) if a != axis]
        bx = [self._bx, self._by, self._bz]
        t1, t2, ax = bx[others[0]], bx[others[1]], bx[axis]
        rho = np.sqrt(t1 ** 2 + t2 ** 2)
        phi = np.arctan2(t2, t1)
        psi = np.arctan2(ax, rho - R)
        rtube = np.sqrt((rho - R) ** 2 + ax ** 2)
        g_chan = (np.exp(-(rtube ** 2) / (2.0 * (0.6 * r) ** 2))
                  * (rho > 2.0 * self.dx) * self.interior_mask())
        dR = np.cos(self.p_dep * phi)
        dax = np.sin(self.p_dep * phi)
        D = np.zeros(self.omega.shape)
        D[..., others[0]] = dR * np.cos(phi)
        D[..., others[1]] = dR * np.sin(phi)
        D[..., axis] = dax
        return axis, g_chan, psi, D

    def _polyphase_deposit_step(self):
        """D15 — the rotating-field STATOR boundary BC (CP10, prereg §3.2). Extract
        photon spin δL on the channel window (the photon PAYS), deposit a TRAVELING
        poloidal π_ω increment whose amplitude IS the extracted δL (D13-FAITHFUL,
        ``A_dep ∝ δL``) and whose travel direction is set by the photon helicity
        (helicity-odd: sign(δL) ⇒ +ψ vs −ψ travel). N_phase=1 ⇒ a STANDING pulsating
        single ψ-site (the v7 reproduction: DOF-incapable of a sustained winding).
        Boundary-local (the channel-wall window only) — NOT a bulk EOM term, so the
        v5 indefinite-Hamiltonian pump cannot recur. The AM channel closes 1:1 BY
        CONSTRUCTION (S_photon_removed_poly ≡ L_deposit_poloidal)."""
        axis, g_chan, psi, D = self._poly_geom()
        if not np.any(g_chan > 0.0) or self.chi_exch == 0.0:
            return
        piw = (self.w - self.w_prev) / self.dt
        s_dens = np.cross(self.w, piw)[..., axis]
        extract = self.chi_exch * g_chan
        dL = float(np.sum(extract * s_dens) * self.dx ** 3)  # signed = handedness
        if dL == 0.0:
            return
        s_h = 1.0 if dL > 0.0 else -1.0  # the photon helicity sets the phase sequence
        Omega = (self.Omega_stator if self.Omega_stator is not None
                 else self.q_dep * self.omega_gap)
        self._poly_phase = s_h * Omega * (self.step_count * self.dt)
        if self.n_phase >= 2:
            # the traveling poloidal wave cos(qψ − s_h Ω t) — the rotating field
            spatial = np.cos(self.q_dep * psi - self._poly_phase)
        else:
            # N_phase=1: a single pulsating ψ-site, no traveling ⇒ no ψ-winding
            dpsi = np.angle(np.exp(1j * psi))  # ψ wrapped to (−π,π]
            site = np.exp(-(dpsi ** 2) / (2.0 * (np.pi / 3.0) ** 2))
            spatial = site * np.cos(self._poly_phase)
        I_pol = float(np.sum(g_chan * np.sum(D ** 2, axis=-1)) * self.dx ** 3)
        if abs(I_pol) < 1e-30:
            return
        A_dep = dL / I_pol  # D13-FAITHFUL: the deposit amplitude IS the extracted δL
        dpi = (A_dep * g_chan * spatial)[..., None] * D
        # deposit into π_ω by lowering ω_prev (π_ω = (ω − ω_prev)/dt)
        self.omega_prev = self.omega_prev - dpi * self.dt
        # the photon PAYS exactly: scale π_w by (1 − χ̃·g_chan) on the window
        self.E_poly_photon_loss += 0.5 * float(np.sum(
            np.sum(piw ** 2, axis=-1) * (1.0 - (1.0 - extract) ** 2)) * self.dx ** 3)
        self.w_prev = self.w - (self.w - self.w_prev) * (1.0 - extract)[..., None]
        self.L_deposit_poloidal += dL
        self.S_photon_removed_poly += dL
        self.poly_events += 1

    def plant_polyphase_winding(self, *, mode="traveling", helicity=1,
                                amplitude=0.3, R=None, r=None, q=None, p=None,
                                axis=None):
        """CALIBRATION plant (D18 known-positive / K-PLANT-IN-CHANNEL) — add a clean
        (p,q) traveling/standing ω winding INTO the field at scale and set ω_prev so
        π_ω matches in the window. NOT a dynamical deposit; the look-inside known-
        positive the de-novo read is calibrated against (plant-at-scale INSIDE the
        geometry per the A46 hygiene)."""
        from ave.utils.fast_winding_extractor import planted_winding_field
        axis = (int(axis) if axis is not None
                else (int(self.dep_axis) if self.dep_axis is not None
                      else self._transduce_axis()))
        R = R if R is not None else (self.dep_R if self.dep_R is not None
                                     else 0.22 * self.N * self.dx)
        r = r if r is not None else self.dep_r
        q = int(q) if q is not None else self.q_dep
        p = int(p) if p is not None else self.p_dep
        om, piw = planted_winding_field(
            self.N, R / self.dx, r, q=q, p=p, amplitude=amplitude, mode=mode,
            helicity=helicity, omega_gap=self.omega_gap, dt=self.dt, axis=axis)
        self.omega = self.omega + om
        self.omega_prev = self.omega_prev + (om - piw * self.dt)
        return om, piw

    def polyphase_ledger(self) -> dict:
        """The D15 deposit ledger (conservation-by-channel; numbers FROM the field).
        S_photon_removed_poly ≡ L_deposit_poloidal BY CONSTRUCTION (1:1 closure)."""
        return {
            "L_deposit_poloidal": self.L_deposit_poloidal,
            "S_photon_removed_poly": self.S_photon_removed_poly,
            "E_poly_photon_loss": self.E_poly_photon_loss,
            "poly_events": self.poly_events,
            "n_phase": self.n_phase, "q_dep": self.q_dep,
            "Omega_stator": (self.Omega_stator if self.Omega_stator is not None
                             else self.q_dep * self.omega_gap),
            "ledger_faithful": bool(self.poly_events == 0 or abs(
                self.S_photon_removed_poly - self.L_deposit_poloidal)
                <= 1e-9 * max(abs(self.L_deposit_poloidal), 1e-30)),
        }

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

    # ===================================== D3/D4 collimation + twin observers (CP7)
    def _axial_field(self, axis: int):
        """The axial vorticity component about `axis` (the trapped-flux proxy the
        collimation organizes), interior-masked."""
        if axis == 2:
            f = self._d(self.u_adv[..., 1], 0, self.dx) - self._d(self.u_adv[..., 0], 1, self.dx)
        elif axis == 1:
            f = self._d(self.u_adv[..., 0], 2, self.dx) - self._d(self.u_adv[..., 2], 0, self.dx)
        else:
            f = self._d(self.u_adv[..., 2], 1, self.dx) - self._d(self.u_adv[..., 1], 2, self.dx)
        return f * self.interior_mask()

    def _interior_box(self):
        """The interior bounding box (PML/sponge excluded) as a 3-tuple of slices —
        so axial means are taken over the interior extent, NOT diluted by the
        masked boundary planes (CP7)."""
        m = self.interior_mask()
        ii = np.where(m.any(axis=2).any(axis=1))[0]
        jj = np.where(m.any(axis=2).any(axis=0))[0]
        kk = np.where(m.any(axis=1).any(axis=0))[0]
        return (slice(ii[0], ii[-1] + 1), slice(jj[0], jj[-1] + 1), slice(kk[0], kk[-1] + 1))

    def columnarity(self, axis: int | None = None, field: np.ndarray | None = None) -> float:
        """D3 collimation observable: how COLUMNAR (z-invariant, Taylor-column-like)
        the trapped flux is along `axis`. = Nax·∫|f̄|² / ∫|f|² over the INTERIOR box,
        f̄ the axial mean. 1 ⇒ a perfect column (z-invariant); ≈1/Nax ⇒ no axial
        coherence (the floor). A WATCHED observable with its own floor (not an
        assumed geometry)."""
        if axis is None:
            axis = getattr(self, "foc_axis", 2)
        f = self._axial_field(axis) if field is None else (field * self.interior_mask())
        f = f[self._interior_box()]  # interior extent only (no boundary-zero dilution)
        Nax = f.shape[axis]
        fbar = f.mean(axis=axis, keepdims=True)
        num = Nax * float(np.sum(fbar ** 2))
        den = float(np.sum(f ** 2)) + 1e-30
        return num / den

    @staticmethod
    def columnarity_floor(Nax: int) -> float:
        """The no-axial-coherence floor (a random/isotropic field): ≈1/Nax. A
        columnarity must CLEAR this to claim collimation (F0a-class gate)."""
        return 1.0 / float(Nax)

    def core_sense(self, axis: int | None = None, radius_frac: float = 0.25) -> float:
        """The SENSE of the dominant rotation = circulation over an INNER disk
        (strictly inside a column, so the boundary shear layer is excluded).
        positive ⇒ CCW/RH, negative ⇒ CW/LH. The handedness observable that the
        global ∫ζ (=0 by compact support) cannot give."""
        if axis is None:
            axis = getattr(self, "foc_axis", 2)
        f = self._axial_field(axis)
        mid = self.N // 2
        if axis == 2:
            sl = (slice(None), slice(None), mid); a1, a2 = self._bx[:, :, mid], self._by[:, :, mid]
        elif axis == 1:
            sl = (slice(None), mid, slice(None)); a1, a2 = self._bx[:, mid, :], self._bz[:, mid, :]
        else:
            sl = (mid, slice(None), slice(None)); a1, a2 = self._by[mid, :, :], self._bz[mid, :, :]
        rc = np.sqrt(a1 ** 2 + a2 ** 2)
        disk = rc < (radius_frac * 0.5 * self.N * self.dx)
        return float(np.sum(f[sl][disk]) * self.dx ** 2)

    def handedness_ledger(self, axis: int | None = None, tol: float = 0.1) -> dict:
        """D4/T5 twin ledger: split the axial vorticity into BOTH senses (ζ>0 / ζ<0)
        and report the GLOBAL handedness (their difference). For ANY compactly-
        supported flow ∫ζ=0 EXACTLY (the boundary shear layer carries the counter-
        circulation) — so global≈0 is the BORN-IN-PAIRS / Kelvin signature itself
        (the T5 global-handedness-ledger-zero check), NOT a degeneracy to debug.
        The dominant rotation SENSE is core_sense() (an inner disk); twin SEPARATION
        is twin_pocket_ledger()."""
        if axis is None:
            axis = getattr(self, "foc_axis", 2)
        f = self._axial_field(axis)
        dV = self.dx ** 3
        rh = float(np.sum(f[f > 0]) * dV)
        lh = float(-np.sum(f[f < 0]) * dV)
        net = rh - lh
        total = rh + lh + 1e-30
        return {
            "RH_vorticity": rh,
            "LH_vorticity": lh,
            "global_handedness": net,
            "abs_net_frac": abs(net) / total,
            "core_sense": self.core_sense(axis),
            "balanced": bool(abs(net) / total < tol),  # born-in-pairs (compact support)
        }

    def twin_pocket_ledger(self, axis: int | None = None) -> dict:
        """Classify the SNAP pockets by the local axial-vorticity sense at each
        snapped cell → RH-pocket vs LH-pocket cell counts (the dual-handedness
        pocket ledger; twin-pocket formation is a spec-sheet test, its absence an
        honest finding NOT a tweak target)."""
        if axis is None:
            axis = getattr(self, "foc_axis", 2)
        f = self._axial_field(axis)
        cm = self.snap_mask
        rh_cells = int(np.count_nonzero(cm & (f > 0)))
        lh_cells = int(np.count_nonzero(cm & (f < 0)))
        return {
            "RH_pocket_cells": rh_cells,
            "LH_pocket_cells": lh_cells,
            "twin_present": bool(rh_cells > 0 and lh_cells > 0),
            "total_pocket_cells": self.pocket_cells(),
        }

    def snap_ledger(self) -> dict:
        return {
            "pocket_cells": self.pocket_cells(),
            "snap_events": self.snap_events,
            "unsnap_events": self.unsnap_events,
            "E_latent_held": self.E_latent_held,
            "E_latent_restored": self.E_latent_restored,
            "E_diss_snap": self.E_diss_snap,
            "E_vent_absorbed": self.E_vent_absorbed,
            "E_reflect": self.E_reflect,
            "mass_clamp": self.mass_clamp,
        }

    # ----------------------------------------- v6 D11 unified energy bookkeeping
    def bulk_internal_energy(self, interior_only: bool = True) -> float:
        """∫ε(ρ̄)dV — the exact-EOS internal energy (the U-table). snap_on only;
        else falls back to the linear-acoustic PE proxy ½c₀²∫ρ̄² (v5 H_field parity)."""
        m = self.interior_mask() if interior_only else 1.0
        if getattr(self, "snap_on", False) and hasattr(self, "_U_rb"):
            return float(np.sum(self.U_density(self.rho_bar) * m) * self.dx ** 3)
        return float(0.5 * self.c0 ** 2 * np.sum((self.rho_bar ** 2) * m) * self.dx ** 3)

    def snap_energy_ledger_total(self) -> float:
        """Sum of ALL snap-energy destinations currently OUT of the field dynamics:
        held latent + dissipated + vented (seed/radiated) + absorbed (D10a) +
        reflector-removed (D11). EXCLUDES E_latent_restored (it returned to the
        field). The H_total bookkeeping term that must close the ledger."""
        return (self.E_latent_held + self.E_diss_snap
                + getattr(self, "E_vent_to_seed", 0.0) + getattr(self, "E_vent_radiated", 0.0)
                + self.E_vent_absorbed + self.E_reflect)

    def total_energy_unified(self, conserved: bool = True) -> float:
        """H_total across ALL sectors (V + shear-w + ω + coupling + bulk-KE +
        bulk-U) + the snap ledger.  conserved=True uses the master-equation
        INVARIANT bulk_energy_conserved for the V-sector (CP2 — the c_eff²-weighted
        energy); conserved=False uses the naive bulk_energy (the v5 functional the
        saturated-core breather grows — the D11 wrong-functional artifact)."""
        ev = self.bulk_energy_conserved(True) if conserved else self.bulk_energy(True)
        field = (ev + self.shear_energy(True) + self.omega_energy(True)
                 + self._coupling_energy() + self.bulk_kinetic_energy()
                 + self.bulk_internal_energy(True))
        return field + self.snap_energy_ledger_total()

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
            # D9 transducer: AFTER the bulk substep so u_adv exists to receive the
            # orbital AM; a per-cell BOUNDARY operation (CP10), not a bulk EOM term.
            if self.transducer_on:
                self._transducer_step()
            # D15 polyphase conduction: the traveling poloidal stator on the channel
            # wall; AFTER the transducer (its δL is the deposit amplitude source,
            # D13-FAITHFUL). A per-step BOUNDARY BC (CP10), never a bulk EOM term.
            if self.polyphase_on:
                self._polyphase_deposit_step()

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

    def angular_momentum_bulk(self, axis: int | None = None) -> float:
        """Bulk advective angular momentum about `axis`, L=∫ρ(r×u)·axis (interior).
        The T3 spin observable on the bulk-circulation channel."""
        if axis is None:
            axis = getattr(self, "foc_axis", 2)
        rho_full = 1.0 + self.rho_bar
        ux, uy, uz = self.u_adv[..., 0], self.u_adv[..., 1], self.u_adv[..., 2]
        if axis == 2:
            Lz = self._bx * uy - self._by * ux
        elif axis == 1:
            Lz = self._bz * ux - self._bx * uz
        else:
            Lz = self._by * uz - self._bz * uy
        return float(np.sum(rho_full * Lz * self.interior_mask()) * self.dx ** 3)

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
