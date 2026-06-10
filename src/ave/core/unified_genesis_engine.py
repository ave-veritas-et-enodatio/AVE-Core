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

    # ------------------------------------------------------------------- step
    def step(self):
        """Inherited V/w/ω/buckle/lock step (UNCHANGED), then — only if the bulk
        sector is on — the ρ̄/u rarefaction substep. bulk_density_on=False ⇒
        byte-identical to CrystalGraftV4.step()."""
        super().step()
        if self.bulk_density_on:
            self._bulk_step()

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
