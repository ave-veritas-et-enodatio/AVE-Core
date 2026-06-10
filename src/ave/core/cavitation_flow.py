"""
Cavitation-Core Bulk-Flow — the rarefaction-stiffness branch of the BULK sector
================================================================================

Substrate-native compressible-flow integrator for the AVE **bulk volumetric (K)**
density sector, built to probe whether a self-circulating core, rarefied by its
OWN rotation (centrifugal pressure deficit), reaches the CANDIDATE cavitation
floor and what happens there.

Why a NEW engine (substrate-native-check CP2, representation-capability):
  - `master_equation_fdtd.MasterEquationFDTD` is a SCALAR potential field
    (∇×∇V ≡ 0) → irrotational → cannot host circulation; and it implements the
    *stiffening* saturation kernel c²=c₀²/√(1−A²), NOT the rarefaction relation.
  - `lbm_3d.LBM3DEngine` is INCOMPRESSIBLE (constant density) → cannot host
    density rarefaction at all.
  Neither can represent "a circulating flow whose core rarefies." This engine
  carries a vector velocity u AND a compressible density ρ̄, so circulation
  (conserved, energize+lock) and rarefaction (the bulk-density observable)
  coexist.

GOVERNING EOS (the rarefaction-stiffness branch — CANDIDATE-CLAIM, NOT canonical):
    c_bulk²(ρ̄) = c₀² (1 + ρ̄/(1 − ρ̄²))
  (AVE-Propulsion .../04_superluminal_transit.tex:86,89; Ax4, "not a free
  parameter"; bulk-mode freeze-point per AVE-Core temporal-values:30,39).
  Rarefaction side (ρ̄<0): SOFTENS, crosses zero at the candidate cavitation floor
    ρ̄_cav = (1−√5)/2 = −1/φ ≈ −0.6180339887   (PHI canonical, constants.py:199)
  Below ρ̄_cav: c_bulk² < 0 = TENSILE FAILURE = the substrate-bulk-density pocket
  (FIREWALL: a FOURTH object — NOT Rayleigh-Plesset, NOT photon bubble, NOT Γ=−1).

GOVERNING EQUATIONS (2-D, barotropic, inviscid bulk-density flow):
    ∂ρ̄/∂t = −∇·[(1+ρ̄) u]                       (continuity, full nonlinear)
    ∂u/∂t  = −(u·∇)u − [c_bulk²(ρ̄)/(1+ρ̄)] ∇ρ̄    (momentum = −∇p/ρ)
  Conserved invariant (Kelvin, barotropic): vorticity ζ=∂ₓv−∂_yu, circulation Γ.
  d|Γ|/dt = 0 in the inviscid limit → ENERGIZE + LOCK (ave-conserved-vs-pumped),
  never pumped. The drive sets the INITIAL circulation once.

APPARATUS INVENTORY — the CLIP suspects (rarefaction analog of S_min/A_cap).
Every numerical floor/clip/epsilon is a named knob, swept in the STEP-3 gate; a
verdict that TRACKS one of these is APPARATUS (CLIP), not physics:
    c2_floor   : c_bulk² = max(c_bulk², c2_floor·c₀²)   [hyperbolicity floor]
    rho_floor  : ρ̄ = max(ρ̄, rho_floor)                  [keeps (1+ρ̄),(1−ρ̄²)>0]
    eps_den    : (1 − ρ̄²) guarded by +eps_den            [denominator epsilon]
    nu_art     : +nu_art·∇²u momentum stabilizer          [dissipates Γ — conservative]
    rho_diff   : +rho_diff·∇²ρ̄ mass-diffusion stabilizer  [smears deficit — conservative]
    cfl        : dt = cfl·dx/c_eff_max                     [timestep safety]
    N, sponge  : grid resolution / absorbing-ring width    [resolution / boundary]
Both stabilizers (nu_art, rho_diff) bias AGAINST deep rarefaction (they suppress,
never manufacture, a deficit) — the conservative direction for a FLASH-vs-CLIP study.

substrate-native-check: CP1 dynamical wave-propagation (no minimization); CP2 BULK-K
vector-flow sector; CP4 real-space ρ̄ is the matching coordinate (NOT phase-space);
CP6 reactance pair = compression-PE ↔ KE tracked; CP7 PML/sponge-excluded
density-minimum sampling; CP9 ρ̄_core is DYNAMICALLY integrated (continuity), NOT the
algebraic centrifugal formula; CP10 stiffness collapse rendered in the EOS wave-speed,
not as a bulk confining force.
"""

from __future__ import annotations

import numpy as np

# Candidate cavitation floor, from PHI (the only canonical anchor; floor is CANDIDATE).
PHI = (1.0 + np.sqrt(5.0)) / 2.0
RHO_CAV = -1.0 / PHI  # = (1−√5)/2 ≈ −0.6180339887 ; c_bulk²(ρ̄_cav)=0


class CavitationFlow2D:
    """2-D compressible bulk-density flow with the AVE rarefaction-softening EOS."""

    def __init__(
        self,
        N: int = 192,
        L: float = 1.0,
        c0: float = 1.0,
        cfl: float = 0.25,
        sponge_width: int = 20,
        sponge_rate: float = 0.30,
        # --- APPARATUS KNOBS (CLIP suspects) ---
        c2_floor: float = 1e-3,
        rho_floor: float = -0.95,
        eps_den: float = 1e-6,
        nu_art: float = 2e-3,
        rho_diff: float = 5e-4,
    ):
        self.N = int(N)
        self.L = float(L)
        self.dx = self.L / self.N
        self.c0 = float(c0)
        self.cfl = float(cfl)
        self.sponge_width = int(sponge_width)
        self.sponge_rate = float(sponge_rate)
        # apparatus knobs
        self.c2_floor = float(c2_floor)
        self.rho_floor = float(rho_floor)
        self.eps_den = float(eps_den)
        self.nu_art = float(nu_art)
        self.rho_diff = float(rho_diff)

        # coordinates (cell-centered), indexing[i,j] = [y,x]
        c = (np.arange(self.N) + 0.5) * self.dx
        self.x = c - 0.5 * self.L
        self.y = c - 0.5 * self.L
        self.X, self.Y = np.meshgrid(self.x, self.y)  # X[i,j]=x_j, Y[i,j]=y_i
        self.R = np.sqrt(self.X**2 + self.Y**2)

        # state
        self.rho = np.zeros((self.N, self.N))  # ρ̄ (normalized volumetric strain)
        self.u = np.zeros((self.N, self.N))    # u_x
        self.v = np.zeros((self.N, self.N))    # u_y

        # CFL: deepest physical c_eff is ~c0 (softens toward 0); fastest is the
        # compression side. We bound by the max linear/compression speed seen so far,
        # but use a fixed conservative dt off the linear c0 plus a safety for advection.
        # c_eff_max ~ a few c0 near rim compression; use 3·c0 envelope.
        self.c_eff_max = 3.0 * self.c0
        self.dt = self.cfl * self.dx / (self.c_eff_max * np.sqrt(2.0))

        # sponge mask (absorbing ring near domain edge); interior = measurement region
        self._build_sponge()
        self.t = 0.0
        self.step_count = 0
        # bookkeeping of whether clips bit (apparatus telltales)
        self.clip_rho_hits = 0
        self.clip_c2_hits = 0

    # ---- geometry / sponge ----
    def _build_sponge(self):
        i, j = np.indices((self.N, self.N))
        d = np.minimum(np.minimum(i, self.N - 1 - i), np.minimum(j, self.N - 1 - j))
        w = self.sponge_width
        s = np.zeros((self.N, self.N))
        if w > 0:
            inb = d < w
            s[inb] = self.sponge_rate * ((w - d[inb]) / w) ** 2
        self.sponge = s  # per-step damping rate field
        self.interior = d >= w  # measurement mask (PML/sponge-excluded, CP7)

    # ---- differential operators (periodic stencil; sponge handles edges) ----
    def _ddx(self, f):
        return (np.roll(f, -1, axis=1) - np.roll(f, 1, axis=1)) / (2.0 * self.dx)

    def _ddy(self, f):
        return (np.roll(f, -1, axis=0) - np.roll(f, 1, axis=0)) / (2.0 * self.dx)

    def _lap(self, f):
        return (
            np.roll(f, 1, axis=0) + np.roll(f, -1, axis=0)
            + np.roll(f, 1, axis=1) + np.roll(f, -1, axis=1)
            - 4.0 * f
        ) / (self.dx**2)

    # ---- EOS (the rarefaction-stiffness branch) ----
    def c_bulk2_raw(self, rho):
        """Unclipped c_bulk²(ρ̄)/1 (in units of c₀²·... actually returns c_bulk², physical)."""
        denom = 1.0 - rho**2
        denom = np.where(np.abs(denom) < self.eps_den, np.sign(denom) * self.eps_den + self.eps_den, denom)
        return (self.c0**2) * (1.0 + rho / denom)

    def c_bulk2(self, rho):
        """c_bulk² with the hyperbolicity floor applied (clipped)."""
        raw = self.c_bulk2_raw(rho)
        floor = self.c2_floor * self.c0**2
        return np.maximum(raw, floor)

    def pressure(self, rho):
        """p(ρ̄) = ρ₀c₀²[ρ̄ − ½ ln(1−ρ̄²)] (ρ₀≡1 natural units). Exact integral of c_bulk²."""
        arg = np.maximum(1.0 - rho**2, self.eps_den)
        return (self.c0**2) * (rho - 0.5 * np.log(arg))

    # ---- RHS of the PDE system ----
    def _rhs(self, rho, u, v):
        drho_dx = self._ddx(rho)
        drho_dy = self._ddy(rho)
        # continuity: ∂ρ̄/∂t = −∇·[(1+ρ̄)u]  + conservative mass diffusion
        mx = (1.0 + rho) * u
        my = (1.0 + rho) * v
        div_m = self._ddx(mx) + self._ddy(my)
        drho_dt = -div_m + self.rho_diff * self._lap(rho)
        # momentum: ∂u/∂t = −(u·∇)u − [c²/(1+ρ̄)]∇ρ̄ + ν_art∇²u
        c2 = self.c_bulk2(rho)
        pref = c2 / np.maximum(1.0 + rho, self.eps_den)
        adv_u = u * self._ddx(u) + v * self._ddy(u)
        adv_v = u * self._ddx(v) + v * self._ddy(v)
        du_dt = -adv_u - pref * drho_dx + self.nu_art * self._lap(u)
        dv_dt = -adv_v - pref * drho_dy + self.nu_art * self._lap(v)
        return drho_dt, du_dt, dv_dt

    def step(self):
        """One RK2 (midpoint) timestep + sponge + clips (clips counted as telltales)."""
        dt = self.dt
        k1r, k1u, k1v = self._rhs(self.rho, self.u, self.v)
        rm = self.rho + 0.5 * dt * k1r
        um = self.u + 0.5 * dt * k1u
        vm = self.v + 0.5 * dt * k1v
        k2r, k2u, k2v = self._rhs(rm, um, vm)
        self.rho = self.rho + dt * k2r
        self.u = self.u + dt * k2u
        self.v = self.v + dt * k2v
        # sponge (absorb outgoing acoustic; relax rho→0, u,v→0 in the ring)
        damp = 1.0 - self.sponge * dt
        self.u *= damp
        self.v *= damp
        self.rho *= damp
        # clips (apparatus) — count hits in the interior so we know if they bit
        below = self.rho < self.rho_floor
        self.clip_rho_hits += int(np.count_nonzero(below & self.interior))
        np.maximum(self.rho, self.rho_floor, out=self.rho)
        c2raw = self.c_bulk2_raw(self.rho)
        self.clip_c2_hits += int(np.count_nonzero((c2raw < self.c2_floor * self.c0**2) & self.interior))
        self.t += dt
        self.step_count += 1

    # ---- energizing (ENERGIZE + LOCK; never pumped) ----
    def energize_solid_body(self, M_edge: float, R_core: float, taper: float = 0.15):
        """Set an initial solid-body rotation column: v_θ = Ω r (r<R), smooth taper.

        M_edge = Ω·R_core/c₀ is the edge Mach number (the swept DRIVE AMPLITUDE).
        Circulation Γ ≈ 2π Ω R² is the CONSERVED invariant; this sets it ONCE.
        ρ̄ starts at 0 (the deficit must EMERGE dynamically — CP9).
        """
        Omega = M_edge * self.c0 / R_core
        r = self.R
        # smooth radial envelope: full inside R_core, cosine taper to 0 over `taper`
        env = np.ones_like(r)
        ramp = (r - R_core) / (taper * self.L)
        env = np.where(r <= R_core, 1.0, np.clip(0.5 * (1.0 + np.cos(np.pi * np.clip(ramp, 0, 1))), 0.0, 1.0))
        env[r > R_core + taper * self.L] = 0.0
        # solid-body: v_θ = Ω r → (u,v) = Ω(−y, x)·env
        self.u = -Omega * self.Y * env
        self.v = Omega * self.X * env
        self.rho = np.zeros_like(self.rho)
        return Omega

    def energize_radial_breather(self, ke_target: float, R_core: float, taper: float = 0.15):
        """Curl-free DIVERGING radial drive (ζ=0) with the SAME kinetic energy as a
        vortex run — the matched-energy, no-circulation control. u = amp·r̂·env(r)."""
        r = self.R + 1e-12
        env = np.ones_like(r)
        ramp = (r - R_core) / (taper * self.L)
        env = np.where(r <= R_core, 1.0, np.clip(0.5 * (1.0 + np.cos(np.pi * np.clip(ramp, 0, 1))), 0.0, 1.0))
        env[r > R_core + taper * self.L] = 0.0
        ur = self.X / r * env
        vr = self.Y / r * env
        # normalize to ke_target (ρ̄=0 ⇒ ρ=1)
        ke_unit = 0.5 * np.sum(ur**2 + vr**2) * self.dx**2
        amp = np.sqrt(ke_target / max(ke_unit, 1e-30))
        self.u = amp * ur
        self.v = amp * vr
        self.rho = np.zeros_like(self.rho)
        return amp

    def despin(self, factor: float = 0.0):
        """De-energize: scale the velocity field (kill the circulation). factor=0 ⇒
        full de-spin. Used for the HYSTERESIS test (does ρ̄_core recover, or persist?)."""
        self.u *= factor
        self.v *= factor

    # ---- observers (CP6/CP7) ----
    def vorticity(self):
        return self._ddx(self.v) - self._ddy(self.u)

    def circulation(self, radius_frac: float = 0.6):
        """Total enclosed circulation Γ = ∮u·dl = ∬ζ dA over a disk (conserved check)."""
        z = self.vorticity()
        mask = self.R < (radius_frac * 0.5 * self.L)
        return float(np.sum(z[mask]) * self.dx**2)

    def angular_momentum(self):
        rho_full = 1.0 + self.rho
        return float(np.sum(rho_full * (self.X * self.v - self.Y * self.u)) * self.dx**2)

    def kinetic_energy(self):
        rho_full = 1.0 + self.rho
        return float(0.5 * np.sum(rho_full * (self.u**2 + self.v**2)) * self.dx**2)

    def compression_pe(self):
        """C-state proxy: linear acoustic PE ½ρ₀c₀²∫ρ̄² (exact in linear regime; a
        labeled proxy near the floor — driver-honesty)."""
        return float(0.5 * self.c0**2 * np.sum(self.rho**2) * self.dx**2)

    def total_energy(self):
        return self.kinetic_energy() + self.compression_pe()

    def rho_core(self):
        """Deepest (most-negative) ρ̄ in the PML/sponge-excluded interior (CP7)."""
        masked = np.where(self.interior, self.rho, np.inf)
        idx = np.unravel_index(np.argmin(masked), masked.shape)
        return float(self.rho[idx]), idx

    def c2_core(self):
        rc, idx = self.rho_core()
        return float(self.c_bulk2_raw(np.array(rc))), float(self.c_bulk2(np.array(rc)))

    def snapshot(self):
        rc, idx = self.rho_core()
        c2raw, c2cl = self.c2_core()
        return {
            "t": self.t,
            "step": self.step_count,
            "rho_core": rc,
            "core_idx": [int(idx[0]), int(idx[1])],
            "c2_core_raw": c2raw,
            "c2_core_clipped": c2cl,
            "KE": self.kinetic_energy(),
            "PE": self.compression_pe(),
            "E_total": self.total_energy(),
            "Gamma": self.circulation(),
            "L": self.angular_momentum(),
            "clip_rho_hits": self.clip_rho_hits,
            "clip_c2_hits": self.clip_c2_hits,
            "max_abs_u": float(np.max(np.abs(self.u))),
        }

    def is_stable(self):
        return np.all(np.isfinite(self.rho)) and np.all(np.isfinite(self.u)) and float(np.max(np.abs(self.u))) < 50.0 * self.c0
