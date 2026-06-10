"""
Crystal-Graft BEMF — close the dark-wake/back-EMF loop as the INDUCTIVE
reaction-half of the chiral source coupling (Grant ratification 2026-06-10)
============================================================================

GRANT RATIFICATION (2026-06-10, recorded verbatim here and in the prereg): the
locked-motor unification — **BEMF = the payment** (drive balanced by back-EMF at
steady state), the **cavitation pocket = the compliance (C)**, the **C3 commit =
the latch** — are components of ONE circuit, not competitors. The v4 engine
computes a BEMF-class observable (`DarkWakeObserver`, τ_zx ∝ Z_local·∂|V|²/∂x in
`vacuum_engine.py:1457`; canon `dark-wake-bemf-foc-synthesis.md`) but NEVER feeds
it to dynamics ("OBSERVED-NOT-FED-BACK", electron-synthesis-epic §7). This module
closes that loop — but as PHYSICS, the REACTION-HALF of the source coupling
(Newton's 3rd law on the lattice / the functional-derivative-pair pattern v2's
H_couple validated), NOT an ad-hoc damper bolted on (which is exactly what the v4
rigid-rotation LOCK was — and the 4-lens panel demoted it C→LOCK-FAIL: the |L_ω|
doubling ratio 5.03/3.97/5.19 vs the 1.3 gate was η-INVARIANT, the linear-damper-
against-a-growing-source signature; the source never paid for its torque).

DERIVATION (ave-fundamental-ground-up-implementation — both halves from ONE term)
---------------------------------------------------------------------------------
The v4 source coupling is the CAPACITIVE (potential) half of the LC tank:

    H_couple = κ̃ ∫ g_wall(r) · V · [ w · (∇×ω) ] d³r            (FROZEN g, w live)
      f_V = −δH/δV = −κ̃ g [w·(∇×ω)]          (V↔ω reaction, present in v4)
      f_ω = −δH/δω = −κ̃ ∇×(g V w)            (the buckle: GROWS the circulation)

This conserves E_V+E_ω+H_couple, but |L_ω|=|∫r×π_ω| (the NET rigid rotation of ω)
pumps secularly (v4: ≈ t^2.2) — the buckle keeps injecting net rotation and there
is no INDUCTIVE term opposing the RATE of buildup. The missing reaction-half is the
INDUCTIVE (kinetic/velocity) mirror of the SAME coupling — a single Lagrangian
velocity-coupling term (the mutual-inductance / back-EMF energy):

    L_BEMF = κ_L ∫ g_wall(r) · [ w · (∇×ω) ] · V̇ d³r

Euler–Lagrange of this ONE term gives the conjugate pair (κ_L the gain):

    f_V^BEMF = −κ_L g [ w · (∇×π_ω) ]         (BACK-EMF on the source ∝ circulation
                                               RATE π_ω — this is −dΦ/dt, Lenz)
    f_ω^BEMF = +κ_L ∇×( g π_V w )             (forward inductive drive on ω ∝ source
                                               RATE π_V — Newton's-3rd conjugate)
                                               π_V = V̇,  π_ω = ω̇

Properties (verified, not assumed):
  • CONSERVATIVE / REACTIVE, not a damper. P_V^BEMF + P_ω^BEMF
    = ∫f_V^BEMF·π_V + ∫f_ω^BEMF·π_ω = −κ_L∫g[w·∇×π_ω]π_V + κ_L∫g π_V[w·∇×π_ω] = 0
    EXACTLY in the continuum (integration-by-parts of the curl). The BEMF channel
    does NO net work — it TRANSFERS reactively between source (V) and circulation
    (ω), exactly as a motor back-EMF stores/returns rather than dissipates. So a
    drop in H_total under this term is a NUMERICAL artifact (a damper in disguise),
    NOT the physics — the H_total ledger is the PAYS-vs-BOUNDS-WITHOUT-PAYING gate.
  • It is the LITERAL velocity-sector mirror of the v4 buckle (V→π_V in the drive,
    ω→π_ω in the reaction): capacitive buckle (C) + inductive BEMF (L) = the full
    reactive LC tank. This IS Grant's locked-motor unification, one circuit.
  • Lenz SIGN: κ_L>0 vs κ_L<0 is the falsifiable control. One sign OPPOSES the
    buildup (Lenz → bounds + pays), the opposite REINFORCES it (anti-Lenz →
    detonates FASTER than OFF). If the sign-flip does nothing, the feedback is
    INERT. The opposing sign is determined by a single frozen sign-probe (the sign
    for which the BEMF net-transfers source→circulation as |L_ω| grows), then
    FROZEN — NOT tuned per outcome.

RELATION TO THE OBSERVER (reconciliation, per the brief):
  The DarkWakeObserver meters τ_zx ∝ Z_local·∂|V|²/∂x — a V-SECTOR-ONLY proxy of
  the same Lenz back-reaction (the longitudinal shear behind the soliton; it cannot
  see the ω circulation directly). f_V^BEMF = −κ_L g[w·(∇×π_ω)] is the TRUE cross-
  sector dynamical reaction (it couples to the circulation RATE). They share the
  M_inertial≡L_drag / back-EMF physics; the FUNCTIONAL-DERIVATIVE form is the
  DYNAMICS, the observer τ_zx is the METER. A crystal-engine τ_zx proxy is computed
  here (tau_zx_proxy) purely as the cross-check meter — it is never fed to dynamics.

α-FREEDOM: κ_L inherits the κ̃=6/5=pq/(p+q) topology coupling (same geometry as the
buckle — the inductive half of the SAME mutual coupling). No α-bearing symbol enters
engine state. The Lenz sign is ±1.
"""

from __future__ import annotations

import numpy as np

from ave.core.crystal_graft_v4 import CrystalGraftV4


class CrystalGraftBEMF(CrystalGraftV4):
    """v4 + the INDUCTIVE back-EMF reaction-half of the buckle (the missing
    equilibration channel, fed back as PHYSICS). bemf_kappa=0 ⇒ feedback OFF
    (reproduces the v4 runaway); bemf_kappa>0/<0 ⇒ Lenz / anti-Lenz."""

    def __init__(
        self,
        N: int,
        *,
        bemf_kappa: float = 0.0,
        **kwargs,
    ):
        """
        bemf_kappa: signed inductive-coupling gain κ_L (the back-EMF gain). 0 ⇒
                    OFF (v4 contrast); +|κ_L| ⇒ one sign; −|κ_L| ⇒ the flipped
                    (anti-Lenz) sign. The Lenz (opposing) sign is set by the
                    frozen sign-probe in the driver, NOT tuned per outcome.
        """
        super().__init__(N, **kwargs)
        self.bemf_kappa = float(bemf_kappa)
        # BEMF ledger accumulators (the payment canary)
        self.bemf_work_V = 0.0     # Σ f_V^BEMF · π_V · dt  (power INTO source)
        self.bemf_work_omega = 0.0  # Σ f_ω^BEMF · π_ω · dt (power INTO circulation)
        self._last_bemf_emf = 0.0   # interior ‖f_V^BEMF‖  (the back-EMF magnitude)
        self._last_drive = 0.0      # interior ‖f_ω buckle‖ (the source drive magnitude)

    # ----------------------------------------------- the BEMF reaction-half
    def _bemf_forces(self):
        """The inductive back-EMF conjugate pair (functional derivatives of the
        ONE term L_BEMF = κ_L ∫ g [w·(∇×ω)] V̇):
            f_V^BEMF = −κ_L g [ w · (∇×π_ω) ]     (back-EMF on source ∝ circ. rate)
            f_ω^BEMF = +κ_L ∇×( g π_V w )          (drive on circ. ∝ source rate)
        Returns (f_V_bemf, f_omega_bemf). Uses the live photon w (same director as
        the buckle) and the FROZEN wall window g (so the pair is conservative —
        P_V+P_ω=0 in continuum; the H_total ledger is the discrete-drift canary)."""
        if self.bemf_kappa == 0.0 or not (self.omega_sector_on and self.buckle_on):
            z = np.zeros_like(self.V)
            return z, np.zeros_like(self.omega)
        g = self._wall_window()
        w = self.w
        pi_V = (self.V - self.V_prev) / self.dt          # π_V = V̇  (source current)
        pi_omega = (self.omega - self.omega_prev) / self.dt  # π_ω = ω̇ (circ. current)
        # f_V^BEMF = −κ_L g [w·(∇×π_ω)]
        curl_pi_omega = self._curl(pi_omega, self.dx)
        f_V = -self.bemf_kappa * g * np.sum(w * curl_pi_omega, axis=-1)
        # f_ω^BEMF = +κ_L ∇×(g π_V w)
        A = (g * pi_V)[..., None] * w
        f_omega = +self.bemf_kappa * self._curl(A, self.dx)
        return f_V, f_omega

    def tau_zx_proxy(self) -> np.ndarray:
        """Crystal-engine analog of the DarkWakeObserver meter
        τ_zx ∝ Z_local·∂|V|²/∂x, Z_local = Z0/√S (Op14). The OBSERVER (V-sector
        meter), NOT the dynamics — computed only for the reconciliation cross-check.
        Z0 absorbed into an overall scale (a meter, not fed back)."""
        S = self.saturation_kernel(self.V)
        z_local = 1.0 / np.sqrt(np.maximum(S, self.S_min))
        Vsq = self.V * self.V
        dVsq_dx = (np.roll(Vsq, -1, axis=0) - np.roll(Vsq, 1, axis=0)) / (2.0 * self.dx)
        return z_local * dVsq_dx

    # --------------------------------------------------------------- step
    def step(self):
        """v4 leapfrog + the INDUCTIVE BEMF reaction-half injected into the
        accelerations BEFORE the leapfrog update (so it is part of the dynamics,
        not a post-hoc velocity rescale like the v4 lock)."""
        c_eff_sq = self.c_eff_squared(self.V)
        a_V = c_eff_sq * self._laplacian(self.V, self.dx)
        a_w = np.empty_like(self.w)
        for comp in range(3):
            a_w[..., comp] = (self.c_T ** 2) * self._laplacian(self.w[..., comp], self.dx)
        a_omega = np.empty_like(self.omega)
        if self.omega_sector_on:
            for comp in range(3):
                a_omega[..., comp] = (
                    self.c_omega ** 2 * self._laplacian(self.omega[..., comp], self.dx)
                    - self.omega_gap ** 2 * self.omega[..., comp]
                )
        else:
            a_omega[:] = 0.0

        # v4 CHANGE 1: the capacitive photon-director buckle (the SOURCE coupling)
        if self.omega_sector_on and self.buckle_on:
            f_V, f_w, f_omega = self._buckle_forces()
            a_V = a_V + f_V
            a_w = a_w + f_w
            a_omega = a_omega + f_omega
            self.buckle_work += float(np.sum(f_V * self.bulk_velocity()) * self.dt)
            # drive magnitude (interior) for the drive≈BEMF steady-state check
            m = self.interior_mask()
            self._last_drive = float(np.sqrt(np.sum((f_omega ** 2).sum(axis=-1) * m)))

        # NEW: the INDUCTIVE BEMF reaction-half (the missing equilibration channel)
        if self.bemf_kappa != 0.0 and self.omega_sector_on and self.buckle_on:
            fV_bemf, fO_bemf = self._bemf_forces()
            pi_V = self.bulk_velocity()
            pi_omega = self.omega_velocity()
            m = self.interior_mask()
            self.bemf_work_V += float(np.sum(fV_bemf * pi_V * m) * self.dt)
            self.bemf_work_omega += float(np.sum(np.sum(fO_bemf * pi_omega, axis=-1) * m) * self.dt)
            self._last_bemf_emf = float(np.sqrt(np.sum((fV_bemf ** 2) * m)))
            a_V = a_V + fV_bemf
            a_omega = a_omega + fO_bemf

        V_new = 2.0 * self.V - self.V_prev + (self.dt ** 2) * a_V
        w_new = 2.0 * self.w - self.w_prev + (self.dt ** 2) * a_w
        omega_new = 2.0 * self.omega - self.omega_prev + (self.dt ** 2) * a_omega

        # v4 CHANGE 2: the rigid-rotation lock (kept available; the ad-hoc damper)
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

        if self.slaved_omega:
            self._slave_omega_to_V()

        self.time += self.dt
        self.step_count += 1

    # ----------------------------------------------------- BEMF diagnostics
    def bemf_ledger(self) -> dict:
        """The BEMF payment ledger. bemf_emf = the back-EMF magnitude (rises as
        circulation builds); drive = the buckle source-drive magnitude; the
        steady-state PAYMENT signature is drive≈bemf_emf. work_V/work_omega should
        be equal-and-opposite (reactive transfer, no net work) up to discrete
        drift."""
        return {
            "bemf_kappa": self.bemf_kappa,
            "bemf_emf": self._last_bemf_emf,
            "drive": self._last_drive,
            "work_V": self.bemf_work_V,
            "work_omega": self.bemf_work_omega,
            "work_imbalance": self.bemf_work_V + self.bemf_work_omega,
        }

    def __repr__(self):
        return (
            f"CrystalGraftBEMF(N={self.N}, dt={self.dt:.3e}, bemf_kappa={self.bemf_kappa:+.3f}, "
            f"lock={self.lock_on}(η={self.lock_eta:.3f}), photon_coupling={self.photon_coupling}, "
            f"κ̃={self.kappa_tilde}, ω0={self.omega_gap}, step={self.step_count})"
        )
