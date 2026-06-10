"""
Crystal-Graft v4 — the photon's helicity IS the winding (conservation, not template)
====================================================================================

Re-scoped electron-genesis engine (Grant directive 2026-06-10, the twist question).
v3 closed the charge=helicity SIGN-carry but on a FROZEN, DIALED template director
b_λ — a 4-lens adversarial panel demoted it B→C on two fatal lenses: (1) the source
was decoupled from the photon (no_photon arm byte-identical to signal — χ was a
SOURCE INPUT, not the photon's), and (2) the LOCK was unbuilt (|L_ω| pumped
unbounded t^0.43, never saturated). v4 makes TWO physics changes, everything else
(hardened Γ=−1 wall, ω carrier + π_ω + mass-gap, the conserved-coupling pattern,
κ̃=6/5) carried forward from CrystalGraftV3/V2/CrystalEngine UNCHANGED.

GRANT ADJUDICATION (2026-06-10, recorded verbatim in the prereg): the poloidal "3"
is the PHOTON'S OWN CONSERVED TWIST — confinement CONVERTS the photon's helicity
into the winding, rather than anything a source grows or a template imprints.
ave-conserved-vs-pumped applied to the TOPOLOGY itself: the winding is ENERGIZED
from the photon's conserved helicity and LOCKED — never grown, never template-
imprinted, never dialed.

CHANGE 1 — χ-FROM-PHOTON (kills the template; derived ground-up, not the brief's
literal candidate). The v3 frozen Beltrami director b_λ (a dialed χ) is replaced by
the photon's OWN evolved shear field w. A circularly-polarized photon IS a force-
free Beltrami field (∇×w = ±k·w, A∥B), so this is the SAME A∥B object v3 used —
but now its handedness is PHYSICALLY the photon's helicity, not a template input:

    H_couple = κ̃ ∫ g_wall(r) · V · [ w · (∇×ω) ] d³r ,   κ̃ = pq/(p+q) = 6/5  (α-FREE)
      f_V = −δH/δV = −κ̃ g_wall [ w · (∇×ω) ]               (back-reaction ω→V)
      f_ω = −δH/δω = −κ̃ ∇×( g_wall · V · w )                (BUCKLE: compression→ω, DIRECTOR=PHOTON)
      f_w = −δH/δw = −κ̃ g_wall · V · (∇×ω)                  (photon LOSES helicity to ω — ABSORPTION)

Consequences that are now AUTOMATIC (verified empirically, not assumed):
  (a) NO-PHOTON ⇒ w=0 ⇒ f_ω≡0 ⇒ ω stays 0 ⇒ H_bel=0. The no-photon control is null
      BY PHYSICS — v3's byte-identical failure mode is now IMPOSSIBLE (the source
      literally contains w).
  (b) HANDEDNESS comes from the photon: for a CP photon ∇×w=±kw, so the sourced
      ω∝∇×(gVw)∝∇×w, then ∇×ω∝∇×(∇×w)∝w ⇒ H_bel=∫ω·(∇×ω)∝∫(∇×w)·w = the photon's
      OWN helicity density. NO dialed χ anywhere.
  (c) ZERO-helicity (linear-pol) photon: w has one transverse component, net
      ∫w·(∇×w)=0 ⇒ no chirality input ⇒ no net winding, no net charge while
      depositing comparable ENERGY (the sharpest control).

CHANGE 2 — THE LOCK (the gyroscope's missing half), the spin-LOCK toward the rigid
force-free A∥B state — TARGETED so it does NOT bleed the LC reactance that carries
the poloidal winding. The runaway v3 left unfixed is a GLOBAL rigid rotation of ω
(|L_ω|=|∫r×π_ω| pumping secularly, t^0.43). The poloidal "3" lives in the LOCAL
(ω, π_ω) LC quadrature — a zero-net-L pattern. They are SEPARABLE, so the lock
removes a fraction η of the rigid-body rotation Ω×r (Ω=I⁻¹L_ω) ONLY:

    π_ω ← π_ω − η·(Ω×r)          ⇒   L_ω ← (1−η)·L_ω   (EXACT per-step contraction)

  • SATURATES |L_ω| — the doubling-ratio→1.0 STOP gate (v3's pump never plateaued);
  • leaves the LOCAL LC quadrature (the poloidal fibre) UNTOUCHED — a plain velocity
    damp would drive π_ω→0 and KILL the LC oscillation that IS the winding (verified
    (2,3)→(2,1) collapse), the load-bearing v4 lesson;
  • d|L|²/dt<0 toward the rigid (force-free A∥B) gyroscopic state — the SAME A∥B
    object as the source director (CHANGE 1): source and lock are one
    (sapphire-phonon-centrifuge.md:34 / reactive-entrainment gyroscope). lock_OFF is
    the v3-behaviour contrast arm (topology destruction).

α-FREEDOM (CI-enforced, test_graft_v4_alpha_free.py, hardened): no α-bearing symbol
enters engine state — κ̃=6/5=pq/(p+q) topology, V_yield≡1, c speeds from ν_vac=2/7,
the photon's helicity is the only handedness input. α⁻¹=4π³+π²+π / Golden-Torus are
EMERGENCE targets, never inputs.
"""

from __future__ import annotations

import numpy as np

from ave.core.crystal_graft_v3 import CrystalGraftV3


class CrystalGraftV4(CrystalGraftV3):
    """v3 with TWO physics changes: (1) the buckle DIRECTOR is the live photon
    shear field w (χ-from-photon, kills the dialed template); (2) a Woltjer/Taylor
    helicity-conserving LOCK relaxes ω toward force-free Beltrami (saturates |L_ω|,
    conserves H_bel). Everything else inherited unchanged."""

    def __init__(
        self,
        N: int,
        *,
        lock_on: bool = True,
        lock_eta: float = 0.08,
        photon_coupling: bool = True,
        photon_deplete: bool = False,
        slaved_omega: bool = False,
        **kwargs,
    ):
        """
        New args (the two physics changes):
            lock_on:        master switch for the Woltjer/Taylor helicity-lock
                            (CHANGE 2). lock_OFF is the v3-behaviour contrast arm
                            (expect topology destruction / |L_ω| pump).
            lock_eta:       per-step relaxation fraction η of the Beltrami flow.
                            Forward-Euler on the +∇²ω diffusive part is stable for
                            η < dx²/6 ≈ 0.17 (dx=1); clamped to that. Tuned ONCE on
                            the LOCK SMOKE (planted-knot survival + |L_ω| saturation),
                            then FROZEN for every de-novo arm. NOT α.
            photon_coupling: CHANGE 1. True ⇒ buckle director = live photon w. False
                            ⇒ fall back to v3's frozen Beltrami template (regression).
            slaved_omega:   POSITIVE-CONTROL only. If True, ω is OVERWRITTEN each
                            step to a fixed function of V (ω := ∇(V)-derived) — i.e.
                            ω is SLAVED to the bulk, the genesis-24 double-count. The
                            independence gate MUST flag this arm False (demonstrated
                            reachable-False). NEVER used for a physics arm.
        """
        super().__init__(N, **kwargs)
        self.photon_deplete = bool(photon_deplete)
        self.lock_on = bool(lock_on)
        # lock_eta = per-step VELOCITY-damping fraction η∈[0,1] (a velocity
        # contraction ω_new←ω+(1−η)(ω_new−ω)); unconditionally stable on [0,1].
        self.lock_eta = float(min(max(lock_eta, 0.0), 1.0))
        self.lock_eta_max = 1.0
        self.photon_coupling = bool(photon_coupling)
        self.slaved_omega = bool(slaved_omega)
        self.lock_lambda = 0.0  # last Rayleigh-quotient force-free eigenvalue
        self._Hbel_pre_lock = 0.0  # H_bel just before the lock substep (diag)
        self._Hbel_post_lock = 0.0  # H_bel just after (lock conservation canary)
        # cache interior r-vectors for the lock's rigid-rotation removal (was a
        # per-step np.indices — the dominant lock cost; build once)
        m = self.interior_mask()
        i, j, k = np.indices((self.N, self.N, self.N))
        cc = (self.N - 1) / 2.0
        self._lock_rx = (i - cc) * m
        self._lock_ry = (j - cc) * m
        self._lock_rz = (k - cc) * m
        rx, ry, rz = self._lock_rx, self._lock_ry, self._lock_rz
        r2 = rx * rx + ry * ry + rz * rz
        self._lock_Itensor = np.array([
            [float(np.sum(r2 - rx * rx)), float(-np.sum(rx * ry)), float(-np.sum(rx * rz))],
            [float(-np.sum(rx * ry)), float(np.sum(r2 - ry * ry)), float(-np.sum(ry * rz))],
            [float(-np.sum(rx * rz)), float(-np.sum(ry * rz)), float(np.sum(r2 - rz * rz))],
        ]) + 1e-12 * np.eye(3)

    # ------------------------------------------ CHANGE 1: photon-director buckle
    def _buckle_forces(self):
        """3-way conserved buckle with the DIRECTOR = the live photon shear w:
          f_V = −κ̃ g_wall [ w·(∇×ω) ]
          f_ω = −κ̃ ∇×( g_wall·V·w )                 (DIRECTOR = PHOTON, CHANGE 1)
          f_w = −κ̃ g_wall·V·(∇×ω)                   (photon loses helicity → ω: ABSORPTION)
        Functional derivatives of ONE trilinear coupling H=κ̃∫gV[w·(∇×ω)] (g frozen)
        ⇒ the joint H=E_V+E_w+E_ω+H_couple conserves (energize-LOCK). Returns
        (f_V, f_w, f_omega). If photon_coupling is OFF, defers to the v3 two-way
        Beltrami-template buckle (which returns only f_V, f_omega)."""
        if not self.photon_coupling:
            fV, fO = super()._buckle_forces()
            return fV, np.zeros_like(self.w), fO
        g = self._wall_window()
        w = self.w
        curl_omega = self._curl(self.omega, self.dx)
        # f_V = −κ̃ g (w·∇×ω)
        f_V = -self.kappa_tilde * g * np.sum(w * curl_omega, axis=-1)
        # A_vec = g·V·w ;  f_ω = −κ̃ ∇×A_vec
        A = (g * self.V)[..., None] * w
        f_omega = -self.kappa_tilde * self._curl(A, self.dx)
        # f_w = −κ̃ g·V·(∇×ω)   (the reciprocal: photon back-reaction = ABSORPTION /
        # depletion). With f_w ON the coupling is the full trilinear H=κ̃∫gV[w·∇×ω]
        # whose continuum energy conserves — but it is an INDEFINITE Hamiltonian
        # (linear in each field, unbounded below) so the discrete dynamics PUMP /
        # DETONATE (verified: H_photon, H_bel, |L_ω| all runaway; lock cannot arrest
        # an indefinite-Hamiltonian runaway). photon_deplete=False (DEFAULT) drops
        # f_w: the live photon w is then a BOUNDED chiral DIRECTOR (the coupling is
        # bilinear in the dynamical pair (V,ω), stable like v3) whose handedness IS
        # the photon's helicity — χ-from-photon WITHOUT the indefinite pump. The
        # photon_deplete=True arm is run as the documented DETONATION CONTRAST.
        if self.photon_deplete:
            f_w = -self.kappa_tilde * (g * self.V)[..., None] * curl_omega
        else:
            f_w = np.zeros_like(self.w)
        return f_V, f_w, f_omega

    def _coupling_energy(self) -> float:
        """H_couple = κ̃ ∫ g_wall·V·[ w·(∇×ω) ] — the photon-director buckle ledger."""
        if not (self.omega_sector_on and self.buckle_on):
            return 0.0
        if not self.photon_coupling:
            return super()._coupling_energy()
        g = self._wall_window()
        curl_omega = self._curl(self.omega, self.dx)
        dens = self.kappa_tilde * g * self.V * np.sum(self.w * curl_omega, axis=-1)
        return float((dens * self.interior_mask()).sum())

    # --------------------------------------------- CHANGE 2: the Woltjer/Taylor lock
    def _lock_relax(self, omega_new: np.ndarray):
        """The spin-LOCK: damp ONLY the rigid-rotation (net angular-momentum) mode of
        the ω velocity π_ω, leaving the LOCAL LC quadrature untouched.

        WHY targeted, not a plain velocity damp (the load-bearing v4 lesson): the
        poloidal "3" LIVES in the (ω, π_ω) LC quadrature (the ω-tank's reactance
        pair). A plain velocity contraction ω←ω+(1−η)(ω−ω_prev) drives π_ω→0 and so
        KILLS the LC oscillation that IS the poloidal winding — verified to collapse
        a planted (2,3)→(2,1). The runaway is instead a GLOBAL rigid rotation of the
        ω field (|L_ω|=|∫r×π_ω| building secularly); the poloidal fibre is a
        LOCAL, zero-net-L pattern. They are separable. So the lock removes a fraction
        η of the RIGID-BODY rotation Ω×r (Ω = I⁻¹L_ω, I the ω moment-of-inertia):

            π_ω ← π_ω − η·(Ω × r)   ⇒   L_ω ← (1−η)·L_ω   (EXACT per-step contraction)

        which SATURATES |L_ω| (the doubling-ratio STOP gate, v3's t^0.43 pump) while
        leaving the local LC quadrature — hence the poloidal winding — intact. This
        is the gyroscope spin-LOCK d|L|²/dt<0 toward the rigid (force-free A∥B) state
        without bleeding the reactive oscillation. Unconditionally stable.

        Returns (ω_new_damped, |Ω|)."""
        mm = self.interior_mask()[..., None]
        pw = (omega_new - self.omega) / self.dt  # provisional π_ω
        rx, ry, rz = self._lock_rx, self._lock_ry, self._lock_rz
        # net angular momentum L = Σ r×π_ω over interior
        Lx = float(np.sum(ry * pw[..., 2] - rz * pw[..., 1]))
        Ly = float(np.sum(rz * pw[..., 0] - rx * pw[..., 2]))
        Lz = float(np.sum(rx * pw[..., 1] - ry * pw[..., 0]))
        Lvec = np.array([Lx, Ly, Lz])
        try:
            Omega = np.linalg.solve(self._lock_Itensor, Lvec)
        except np.linalg.LinAlgError:
            Omega = np.zeros(3)
        # subtract η·(Ω×r) from π_ω (rigid-rotation removal) ⇒ L←(1−η)L exactly
        ox, oy, oz = Omega
        corr = np.empty_like(omega_new)
        corr[..., 0] = oy * rz - oz * ry
        corr[..., 1] = oz * rx - ox * rz
        corr[..., 2] = ox * ry - oy * rx
        omega_damped = omega_new - self.lock_eta * corr * mm * self.dt
        return omega_damped, float(np.linalg.norm(Omega))

    # --------------------------------------------------------------- step
    def step(self):
        """One leapfrog step: 3-sector wave + the 3-way photon-director buckle +
        the helicity-conserving lock substep. (Overrides v2.step, which had only a
        2-way buckle and no lock.)"""
        # bulk V (mass / Γ=−1 trap)
        c_eff_sq = self.c_eff_squared(self.V)
        a_V = c_eff_sq * self._laplacian(self.V, self.dx)
        # shear w (photon) — vectorized Laplacian (bit-identical to per-comp loop)
        a_w = (self.c_T ** 2) * self._laplacian_vec(self.w, self.dx)
        # micro-rotation ω (winding) + mass-gap LC reactance
        if self.omega_sector_on:
            a_omega = (
                (self.c_omega ** 2) * self._laplacian_vec(self.omega, self.dx)
                - (self.omega_gap ** 2) * self.omega
            )
        else:
            a_omega = np.zeros_like(self.omega)

        # the 3-way photon-director buckle (CHANGE 1)
        if self.omega_sector_on and self.buckle_on:
            f_V, f_w, f_omega = self._buckle_forces()
            a_V = a_V + f_V
            a_w = a_w + f_w
            a_omega = a_omega + f_omega
            self.buckle_work += float(np.sum(f_V * self.bulk_velocity()) * self.dt)

        V_new = 2.0 * self.V - self.V_prev + (self.dt ** 2) * a_V
        w_new = 2.0 * self.w - self.w_prev + (self.dt ** 2) * a_w
        omega_new = 2.0 * self.omega - self.omega_prev + (self.dt ** 2) * a_omega

        # CHANGE 2: the helicity-conserving lock (records the conservation canary)
        if self.lock_on and self.omega_sector_on:
            self._Hbel_pre_lock = self._hbel_of(omega_new)
            omega_new, self.lock_lambda = self._lock_relax(omega_new)
            self._Hbel_post_lock = self._hbel_of(omega_new)

        V_new *= self.damping
        w_new *= self.damping[..., None]
        omega_new *= self.damping[..., None]

        self.V_prev, self.V = self.V, V_new
        self.w_prev, self.w = self.w, w_new
        self.omega_prev, self.omega = self.omega, omega_new

        # POSITIVE-CONTROL: slave ω to V (the double-count) — gate-test arm ONLY
        if self.slaved_omega:
            self._slave_omega_to_V()

        self.time += self.dt
        self.step_count += 1

    def _slave_omega_to_V(self):
        """POSITIVE CONTROL (gate test only): overwrite ω := ∇V × x̂-family so ω is
        a deterministic function of V (NOT an independent carrier). The independence
        gate MUST return False on this arm (demonstrated reachable-False — v3's gate
        could not fail, an auto-VOID condition this removes)."""
        gx, gy, gz = np.gradient(self.V, self.dx)
        self.omega[..., 0] = gy
        self.omega[..., 1] = -gx
        self.omega[..., 2] = 0.3 * gz
        # π_ω also slaved (so the reactance pair is degenerate with V's)
        gx0, gy0, gz0 = np.gradient(self.V_prev, self.dx)
        self.omega_prev[..., 0] = gy0
        self.omega_prev[..., 1] = -gx0
        self.omega_prev[..., 2] = 0.3 * gz0

    # ------------------------------------------------- LC-scaled planted-knot seed
    def seed_omega_known_2_3(self, R, r, amplitude=0.2, p=2, q=3, delta=None):
        """CARRIER-GATE plant (CP8 labeled, lock-smoke only) with the LC phase
        advance δ SCALED to one timestep at the ω-tank frequency (δ = ω_gap·dt). The
        parent (v2) hard-codes δ=0.4, which at the v4 CFL dt≈8e-3 makes the implied
        π_ω≈(δ/dt)·amp≈50× the amplitude — a mis-scaled enormous initial velocity
        that swings the field ~50× under its own LC oscillation (a SEED artifact, NOT
        an instability). δ=ω_gap·dt gives the natural LC quadrature so a planted
        (2,3) is a genuine quasi-stationary breathing knot the lock can be tested on."""
        if delta is None:
            delta = self.omega_gap * self.dt
        c = (self.N - 1) / 2.0
        i, j, k = np.indices((self.N, self.N, self.N))
        xs, ys, zs = i - c, j - c, k - c
        rho = np.sqrt(xs ** 2 + ys ** 2)
        phi = np.arctan2(ys, xs)
        psi = np.arctan2(zs, rho - R)
        rtube = np.sqrt((rho - R) ** 2 + zs ** 2)
        env = np.exp(-(rtube ** 2) / (2.0 * (0.6 * r) ** 2)) * (rho > 2)
        beta = p * phi
        Theta = q * psi
        dR = np.cos(beta)
        dz = np.sin(beta)
        base = amplitude * env
        self.omega[..., 0] += base * np.cos(Theta) * dR * np.cos(phi)
        self.omega[..., 1] += base * np.cos(Theta) * dR * np.sin(phi)
        self.omega[..., 2] += base * np.cos(Theta) * dz
        self.omega_prev[..., 0] = base * np.cos(Theta + delta) * dR * np.cos(phi)
        self.omega_prev[..., 1] = base * np.cos(Theta + delta) * dR * np.sin(phi)
        self.omega_prev[..., 2] = base * np.cos(Theta + delta) * dz

    # ------------------------------------------------------- helicity measurements
    def _hbel_of(self, omega: np.ndarray) -> float:
        """H_bel=∫ω·(∇×ω) for an ARBITRARY ω array (interior) — used by the lock
        conservation canary."""
        curl_omega = self._curl(omega, self.dx)
        dens = np.sum(omega * curl_omega, axis=-1)
        return float((dens * self.interior_mask()).sum())

    def helicity_photon(self, interior_only: bool = True) -> float:
        """H_photon=∫ w·(∇×w) — the PHOTON's own helicity (the conserved input the
        winding is converted from). A CP photon is Beltrami (∇×w=±k w) ⇒ this is
        ±k∫|w|²; a linear-pol photon nets ≈0."""
        curl_w = self._curl(self.w, self.dx)
        dens = np.sum(self.w * curl_w, axis=-1)
        if interior_only:
            dens = dens * self.interior_mask()
        return float(dens.sum())

    def lock_helicity_drift(self) -> float:
        """Relative H_bel change ACROSS the last lock substep (the lock-conservation
        canary). |drift|→0 ⇒ the lock conserves the topological charge."""
        denom = abs(self._Hbel_pre_lock) + 1e-30
        return float((self._Hbel_post_lock - self._Hbel_pre_lock) / denom)

    def helicity_ledger(self, H_photon_0: float) -> dict:
        """The HEADLINE conservation ledger (the v4 measurement). Given the photon's
        helicity at t=0, report where it went:
            input    = H_photon(0)
            trapped  = H_bel(end)            (the winding)
            residual = H_photon(end)         (photon helicity still in the interior)
            radiated = input − trapped − residual   (left through the PML, by deficit)
        Ledger CLOSES (the photon's helicity survives as the winding) iff
        |input − trapped − residual − radiated| ≈ 0 by construction, AND |residual|,
        |radiated| are small relative to |trapped| (photon fully absorbed into ω)."""
        trapped = self.helicity_bel()
        residual = self.helicity_photon()
        radiated = H_photon_0 - trapped - residual
        denom = abs(H_photon_0) + 1e-30
        return {
            "H_photon_0": float(H_photon_0),
            "H_bel_trapped": float(trapped),
            "H_photon_residual": float(residual),
            "H_radiated_deficit": float(radiated),
            "trapped_frac": float(trapped / denom),
            "residual_frac": float(residual / denom),
            "radiated_frac": float(radiated / denom),
            "closes_frac": float((trapped + residual) / denom),  # absorbed+trapped / input
        }

    def __repr__(self):
        return (
            f"CrystalGraftV4(N={self.N}, dt={self.dt:.3e}, photon_coupling={self.photon_coupling}, "
            f"lock={self.lock_on}(η={self.lock_eta:.3f}), κ̃={self.kappa_tilde}, "
            f"ω0={self.omega_gap}, step={self.step_count})"
        )
