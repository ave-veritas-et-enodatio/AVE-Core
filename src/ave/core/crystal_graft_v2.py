"""
Crystal-Graft v2 — the winding gets its OWN Cosserat-ω carrier
==============================================================

Re-scoped electron-genesis engine (Grant directive 2026-06-09). Fixes the
genesis-24 / crystal double-count that self-inflicted ``w_pol=0``.

THE DIAGNOSIS (verified this session, prereg §0):
    The prior crystal engine read the (2,3) winding from
    ``phase_space_vinc_vref`` = (V, ∂_tV/ω, V, −∂_tV/ω) — V_inc and V_ref are
    BOTH projections of the SAME scalar V (one complex scalar V+i∂_tV traces a
    CIRCLE, not a torus). One of the two windings is structurally forced to 0.
    (master_fdtd_phasor_bridge.py:14-18; k4_tlm.py:346 V_ref=0.5·ΣV_inc−V_inc.)

THE FIX — THREE ORTHOGONAL SECTORS (A1 ⊥ T2):
    (V)  bulk DILATATION breather = MASS. c_eff(V)=c0·S^{−1/2}→∞ in the
         saturated core (EM-transverse index n_EM=S^{+1/2}→0; sign-lock
         w35sn2bq3, 2026-06-17 — ½ power, the legacy S^{1/4} was an exponent
         defect) self-creates a HARDENED Γ=−1 acoustic wall. Reused from
         CrystalEngine. The "3"-as-MASS object.
    (w)  transverse SHEAR photon (c_T). Carries the seed helicity h (chirality).
    (ω)  Cosserat MICRO-ROTATION winding sector — NEW, INDEPENDENT U(1). Its
         OWN 3-vector field + OWN conjugate momentum π_ω=∂_tω + OWN mass-gap
         LC reactance ω_0² (couple-stress). NOT downstream of V_inc. The "3"-as-
         WINDING object. (2,3) = ω polarization-direction toroidal "2" + ω
         LC-phase poloidal "3"; charge = Beltrami helicity ∫ω·(∇×ω).

ADD-2 — the conserved chiral compression→micro-rotation BUCKLE:
    At the Γ=−1 wall the blocked longitudinal energy buckles (column→helix)
    into the ω CIRCULATION. ONE Hamiltonian coupling term:

        H_couple = κ̃ ∫ g_wall(r) · V · [n̂_χ · (∇×ω)] d³r,   κ̃=6/5 (α-FREE)

    sources the micro-VORTICITY ∇×ω (= the winding carrier, helicity density)
    from the compression. Forces are the functional derivatives (total
    H=E_V+E_ω+H_couple conserves by construction — energize-LOCK, NOT a pump):
        f_V = −δH/δV = −κ̃ g_wall [n̂_χ·(∇×ω)]      (back-reaction ω→V)
        f_ω = −δH/δω = −κ̃ ∇×(g_wall V n̂_χ)         (BUCKLE: compression→circulation)
    g_wall>0 ONLY at the saturation front (CP10 boundary, not bulk). n̂_χ=h·x̂
    carries the handedness (matter/antimatter sign). Centrosymmetric (h-symmetric
    or κ̃=0) ⇒ net sourced helicity = 0 by construction.

NO-QED / canonical only: κ̃=6/5=pq/(p+q) the (2,3) topology (α-free, NOT 1.2α);
V_yield≡1; branch moduli from ν_vac=2/7 (c_L²/c_T²=10/3). Golden-torus
(R·r=¼, R/r=φ², α⁻¹=4π³+π²+π) are EMERGENCE targets, never inputs.
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import R_II
from ave.core.crystal_engine import CrystalEngine


class CrystalGraftV2(CrystalEngine):
    """3-sector engine: bulk V (mass) ⊗ shear w (photon) ⊗ INDEPENDENT
    micro-rotation ω (winding) + conserved compression→circulation buckle."""

    def __init__(
        self,
        N: int,
        *,
        c_omega: float | None = None,
        omega_gap: float = 1.0,
        omega_sector_on: bool = True,
        buckle_on: bool = True,
        wall_center: float | None = None,
        wall_width: float = 0.12,
        S_min: float = 1e-4,
        **kwargs,
    ):
        """
        New (ω-sector) args — the independent winding carrier:
            c_omega:     ω-sector wave speed (couple-stress). Default = c_T
                         (shear-family). NOT α.
            omega_gap:   ω_0 mass-gap = the ω tank's OWN inductive restoring
                         (the decoupled reactance). This is what makes the ω
                         LC tank independent of the bulk V — the ONLY ω knob,
                         and it is NOT α. Set near the breather-shell resonance.
            omega_sector_on: master switch for the ω carrier.
            buckle_on:   master switch for ADD-2 (the compression→ω buckle).
            wall_center: A-value of the Γ=−1 wall where the buckle engages
                         (default R_II=√3/2, the Non-Linear→Saturated front).
            wall_width:  Gaussian half-width of that shell in A-units.
            S_min:       saturation floor (sets the wall hardness ceiling:
                         Γ_min,floor = (S_min^{1/2}−1)/(S_min^{1/2}+1), from the
                         wall index n = √S → 0 ⇒ Γ → −1; consistent with the
                         ½-power register c_eff = c₀/√S_min at :108). Smaller ⇒
                         harder wall, smaller dt. Named engineering knob.
                         [Prior docstring said S_min^{1/4} — a stale Family-E
                         (1−A²)^{1/8} exponent; corrected 2026-07-14, quarter-
                         power map §Family-E. Descriptive only — no Γ_floor code
                         in this file, so no impl change.]
        """
        # the bulk/shear branches come from CrystalEngine; turn OFF its old
        # shear→bulk converter (we use the NEW ω-sector buckle instead).
        kwargs.setdefault("converter_on", False)
        super().__init__(N, S_min=S_min, **kwargs)

        self.omega_sector_on = bool(omega_sector_on)
        self.buckle_on = bool(buckle_on)
        self.c_omega = float(c_omega) if c_omega is not None else float(self.c_T)
        self.omega_gap = float(omega_gap)
        self.wall_center = float(wall_center) if wall_center is not None else float(R_II)
        self.wall_width = float(wall_width)

        Nn = self.N
        self.omega = np.zeros((Nn, Nn, Nn, 3), dtype=np.float64)
        self.omega_prev = np.zeros((Nn, Nn, Nn, 3), dtype=np.float64)

        # CFL must also respect the ω branch + the mass-gap; re-derive dt as the
        # min over all three branches (bulk c_eff_max, shear c_T, ω c_omega).
        c_eff_max = self.c0 / np.sqrt(self.S_min)
        c_branch_max = max(c_eff_max, self.c_T, self.c_omega)
        # mass-gap angular freq also bounds the explicit step: dt < 2/ω_0
        dt_wave = self.cfl_safety_dx() / (c_branch_max * np.sqrt(3.0))
        dt_gap = 1.8 / max(self.omega_gap, 1e-9)
        self.dt = min(dt_wave, dt_gap)

        self.buckle_work = 0.0  # ∫ f_V·∂_tV dt residual monitor
        self._g_wall_frozen = None  # set by freeze_wall_window() for exact H_couple

    def cfl_safety_dx(self) -> float:
        # CrystalEngine computed dt with cfl_safety*dx; recover that product.
        # (cfl_safety not stored on parent; reconstruct from parent dt is fragile
        #  — use a fixed 0.30 safety consistent with parent default.)
        return 0.30 * self.dx

    # ------------------------------------------------------- wall window
    def _wall_window(self) -> np.ndarray:
        """g_wall(r): thin shell at A≈wall_center (the Γ=−1 saturation front,
        CP10 boundary — NOT a bulk volume). Zero in vacuum (A→0) and in the deep
        frozen core (A→1). This is where the buckle engages.

        If freeze_wall_window() was called, returns the FROZEN geometric shell —
        which makes H_couple EXACTLY bilinear in (V, ω) so the functional-
        derivative forces conserve total H exactly (a live A-dependent g(V) would
        require the ∂g/∂V term, which an explicit leapfrog drops → spurious
        pump). For a quasi-static breather the front barely moves, so the frozen
        shell is the honest conservative rendering (substrate-native CP10)."""
        if self._g_wall_frozen is not None:
            return self._g_wall_frozen
        A = self.strain_field()
        return np.exp(-((A - self.wall_center) ** 2) / (2.0 * self.wall_width**2))

    def freeze_wall_window(self):
        """Snapshot the current saturation-front shell into a FIXED geometric
        window so H_couple becomes exactly bilinear (energy-conserving buckle).
        Call after seeding the breather, before stepping."""
        A = self.strain_field()
        self._g_wall_frozen = np.exp(-((A - self.wall_center) ** 2) / (2.0 * self.wall_width**2)).copy()

    # ------------------------------------------------------ curl operator
    @staticmethod
    def _curl(F: np.ndarray, dx: float) -> np.ndarray:
        """∇×F for a 3-vector field F (central differences, periodic via roll —
        interior is what we read; PML damps the wrap)."""
        Fx, Fy, Fz = F[..., 0], F[..., 1], F[..., 2]

        def d(a, axis):
            return (np.roll(a, -1, axis=axis) - np.roll(a, 1, axis=axis)) / (2.0 * dx)

        cx = d(Fz, 1) - d(Fy, 2)
        cy = d(Fx, 2) - d(Fz, 0)
        cz = d(Fy, 0) - d(Fx, 1)
        # write into a preallocated array instead of np.stack (one fewer full-
        # array copy per curl — bit-identical values, same shape/dtype/order)
        out = np.empty(F.shape, dtype=cx.dtype)
        out[..., 0] = cx
        out[..., 1] = cy
        out[..., 2] = cz
        return out

    # --------------------------------------------------------- ADD-2 buckle
    def _buckle_forces(self):
        """The conserved chiral compression→micro-rotation buckle (ADD-2).

        H_couple = κ̃ ∫ g_wall·V·[n̂_χ·(∇×ω)] d³r,  n̂_χ = h·x̂.
          f_V = −κ̃ g_wall [n̂_χ·(∇×ω)]            (back-reaction ω→V)
          f_ω = −κ̃ ∇×(g_wall·V·n̂_χ)               (BUCKLE: compression→circulation)
        Functional derivatives of ONE bilinear coupling ⇒ total H conserves
        (energize-LOCK). Sources the micro-VORTICITY (winding carrier) from the
        blocked compression at the wall."""
        g = self._wall_window()
        h = self.helicity
        curl_omega = self._curl(self.omega, self.dx)
        # n̂_χ = h·x̂ ⇒ n̂_χ·(∇×ω) = h·(∇×ω)_x
        f_V = -self.kappa_tilde * g * (h * curl_omega[..., 0])
        # A = g·V·n̂_χ = (g·V·h, 0, 0);  f_ω = −κ̃ ∇×A
        A = np.zeros_like(self.omega)
        A[..., 0] = g * self.V * h
        f_omega = -self.kappa_tilde * self._curl(A, self.dx)
        return f_V, f_omega

    def _coupling_energy(self) -> float:
        """H_couple = κ̃ ∫ g_wall·V·[n̂_χ·(∇×ω)] — the buckle ledger term."""
        if not (self.omega_sector_on and self.buckle_on):
            return 0.0
        g = self._wall_window()
        curl_omega = self._curl(self.omega, self.dx)
        dens = self.kappa_tilde * g * self.V * (self.helicity * curl_omega[..., 0])
        return float((dens * self.interior_mask()).sum())

    # --------------------------------------------------------------- step
    def step(self):
        """One leapfrog step of all three sectors + the conserved buckle."""
        # bulk V (the mass / Γ=−1 trap) — same nonlinear c_eff dynamics
        c_eff_sq = self.c_eff_squared(self.V)
        a_V = c_eff_sq * self._laplacian(self.V, self.dx)
        # shear w (photon) — linear vector wave (vectorized Laplacian, bit-identical)
        a_w = (self.c_T**2) * self._laplacian_vec(self.w, self.dx)
        # micro-rotation ω (winding) — OWN wave eq + OWN mass-gap LC reactance
        if self.omega_sector_on:
            a_omega = (
                (self.c_omega**2) * self._laplacian_vec(self.omega, self.dx)
                - (self.omega_gap**2) * self.omega
            )
        else:
            a_omega = np.zeros_like(self.omega)

        # ADD-2 buckle (conservative, boundary-localized)
        if self.omega_sector_on and self.buckle_on:
            f_V, f_omega = self._buckle_forces()
            a_V = a_V + f_V
            a_omega = a_omega + f_omega
            self.buckle_work += float(np.sum(f_V * self.bulk_velocity()) * self.dt)

        V_new = 2.0 * self.V - self.V_prev + (self.dt**2) * a_V
        w_new = 2.0 * self.w - self.w_prev + (self.dt**2) * a_w
        omega_new = 2.0 * self.omega - self.omega_prev + (self.dt**2) * a_omega

        V_new *= self.damping
        w_new *= self.damping[..., None]
        omega_new *= self.damping[..., None]

        self.V_prev, self.V = self.V, V_new
        self.w_prev, self.w = self.w, w_new
        self.omega_prev, self.omega = self.omega, omega_new
        self.time += self.dt
        self.step_count += 1

    # --------------------------------------------------- ω reactance pair
    def omega_velocity(self) -> np.ndarray:
        """π_ω = ∂_tω (the L-state of the INDEPENDENT ω reactance pair, CP6).
        This is genuinely independent of V — ω evolves under its own wave eq."""
        return (self.omega - self.omega_prev) / self.dt

    def omega_energy(self, interior_only: bool = True) -> float:
        """E_ω = ½∫|π_ω|² + ½∫c_ω²|∇ω|² + ½∫ω_0²|ω|²  (kinetic + gradient +
        mass-gap potential = the full ω-tank energy)."""
        pw = self.omega_velocity()
        dens = 0.5 * np.sum(pw**2, axis=-1)
        for comp in range(3):
            gx, gy, gz = np.gradient(self.omega[..., comp], self.dx)
            dens += 0.5 * (self.c_omega**2) * (gx**2 + gy**2 + gz**2)
        dens += 0.5 * (self.omega_gap**2) * np.sum(self.omega**2, axis=-1)
        if interior_only:
            dens = dens * self.interior_mask()
        return float(dens.sum())

    def stencil_energy(self) -> dict:
        """Energy measured with operators CONSISTENT with the dynamics (the
        7-point _laplacian L and the roll-central-diff _curl) so the semi-
        discrete coupled system conserves E_V+E_ω+H_couple EXACTLY (continuous
        time); the leapfrog then conserves it to a bounded O(dt²). Using
        np.gradient instead (a different discrete gradient than the L stencil)
        injects a spurious basis-mismatch 'drift' that is NOT a pump.

        For a wave eq V̈=c²LV (L neg-semidef), the conserved energy is
        E = ½Σ(∂_tV)² − ½c²Σ V·(LV). Linear-bulk c²=c0²; the nonlinear bulk uses
        the local c_eff² inside the stencil energy as the variable-coefficient
        analogue (reported separately as E_V_lin for the strict linear check)."""
        m = self.interior_mask()
        pV = self.bulk_velocity()
        LV = self._laplacian(self.V, self.dx)
        E_V_lin = 0.5 * np.sum((pV**2) * m) - 0.5 * (self.c0**2) * np.sum((self.V * LV) * m)
        pO = self.omega_velocity()
        E_omega = 0.5 * np.sum(np.sum(pO**2, axis=-1) * m)
        for comp in range(3):
            LO = self._laplacian(self.omega[..., comp], self.dx)
            E_omega += -0.5 * (self.c_omega**2) * np.sum((self.omega[..., comp] * LO) * m)
        E_omega += 0.5 * (self.omega_gap**2) * np.sum(np.sum(self.omega**2, axis=-1) * m)
        H_c = self._coupling_energy()
        return {
            "E_V_lin": float(E_V_lin),
            "E_omega": float(E_omega),
            "H_couple": float(H_c),
            "H_total": float(E_V_lin + E_omega + H_c),
        }

    def total_energy_3sector(self, interior_only: bool = True) -> float:
        """H = E_V + E_ω + H_couple — the joint ledger. Conservative buckle ⇒
        flat (energize-LOCK); a pump ⇒ drifts/detonates (genesis-24)."""
        return self.bulk_energy(interior_only) + self.omega_energy(interior_only) + self._coupling_energy()

    def helicity_bel(self, interior_only: bool = True) -> float:
        """Beltrami helicity H_bel = ∫ ω·(∇×ω) — the CHARGE (charge=helicity).
        Conserved invariant (energize-LOCK). Centrosymmetric baseline ⇒ 0."""
        curl_omega = self._curl(self.omega, self.dx)
        dens = np.sum(self.omega * curl_omega, axis=-1)
        if interior_only:
            dens = dens * self.interior_mask()
        return float(dens.sum())

    def spin_L_omega(self) -> float:
        """|L_ω| = |∫ r×π_ω| over interior — the conserved micro-rotation angular
        momentum (energize-LOCK ⇒ bounded; pump ⇒ |L|~t, genesis-24's 5→43)."""
        pw = self.omega_velocity()
        m = self.interior_mask()
        i, j, k = np.indices((self.N, self.N, self.N))
        c = (self.N - 1) / 2.0
        rx, ry, rz = (i - c) * m, (j - c) * m, (k - c) * m
        Lx = np.sum(ry * pw[..., 2] - rz * pw[..., 1])
        Ly = np.sum(rz * pw[..., 0] - rx * pw[..., 2])
        Lz = np.sum(rx * pw[..., 1] - ry * pw[..., 0])
        return float(np.sqrt(Lx**2 + Ly**2 + Lz**2))

    def omega_intensity(self) -> dict:
        """ω-field boundedness monitor (PML-excluded) — the detonation gate."""
        m = self.interior_mask()
        oi = self.omega * m[..., None]
        return {
            "Eomega_field": float(np.sum(oi**2)),
            "max_omega": float(np.max(np.abs(oi))),
            "Lomega": self.spin_L_omega(),
            "Hbel": self.helicity_bel(),
        }

    # ------------------------------------------------- ω-sector seeding
    def seed_omega_known_2_3(self, R, r, amplitude=0.2, p=2, q=3):
        """STRUCTURAL-GATE seed (SMOKE-3a): plant a KNOWN (p,q)=(2,3) winding in
        the ω carrier to prove the carrier+extractor can READ a nonzero w_pol
        (the old scalar bulk read (*,0)). On a torus shell:
            polarization-direction (toroidal/base) winds p× around φ,
            LC phase (poloidal/fibre) winds q× around ψ.
        Sets ω (C-state) and ω_prev (so π_ω carries the LC quadrature ⇒ the
        fibre phase is genuinely populated, not V_inc≡Φ_link degenerate)."""
        c = (self.N - 1) / 2.0
        i, j, k = np.indices((self.N, self.N, self.N))
        xs, ys, zs = i - c, j - c, k - c
        rho = np.sqrt(xs**2 + ys**2)
        phi = np.arctan2(ys, xs)
        psi = np.arctan2(zs, rho - R)
        rtube = np.sqrt((rho - R) ** 2 + zs**2)
        env = np.exp(-(rtube**2) / (2.0 * (0.6 * r) ** 2)) * (rho > 2)
        # base "2": the transverse-ω polarization direction d̂ = cos(pφ)·ê_R +
        #   sin(pφ)·ê_z winds p× around the major circle φ.
        # fibre "3": the LC phase Θ = qψ winds q× around the minor circle ψ; set
        #   via ω (C-state ∝ cosΘ) and ω_prev (so π_ω ∝ sinΘ ⇒ a genuine,
        #   populated LC quadrature — the ω tank's OWN phase, not slaved to V).
        beta = p * phi
        Theta = q * psi
        dR = np.cos(beta)
        dz = np.sin(beta)
        base = amplitude * env
        # Cartesian components of base·cos(Θ)·d̂,  ê_R=(cosφ,sinφ,0), ê_z=(0,0,1)
        self.omega[..., 0] += base * np.cos(Theta) * dR * np.cos(phi)
        self.omega[..., 1] += base * np.cos(Theta) * dR * np.sin(phi)
        self.omega[..., 2] += base * np.cos(Theta) * dz
        delta = 0.4  # LC phase advance over one dt ⇒ π_ω ∝ sinΘ
        self.omega_prev[..., 0] = base * np.cos(Theta + delta) * dR * np.cos(phi)
        self.omega_prev[..., 1] = base * np.cos(Theta + delta) * dR * np.sin(phi)
        self.omega_prev[..., 2] = base * np.cos(Theta + delta) * dz

    def __repr__(self):
        return (
            f"CrystalGraftV2(N={self.N}, dt={self.dt:.3e}, c_L={self.c0}, "
            f"c_T={self.c_T:.4f}, c_ω={self.c_omega:.4f}, ω0={self.omega_gap}, "
            f"κ̃={self.kappa_tilde}, S_min={self.S_min:.1e}, "
            f"ω_on={self.omega_sector_on}, buckle={self.buckle_on}, "
            f"step={self.step_count})"
        )
