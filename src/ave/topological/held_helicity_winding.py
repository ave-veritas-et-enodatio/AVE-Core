"""OPTION C′ — the NO-WORK Beltrami-helicity HOLD (the conserved charge, held conservatively).

This is the C′ amendment to OPTION C (prereg `2026-06-15_passive-eigenmode-solve.md` §9.1,
Grant-greenlit 2026-06-16). It is built ALONGSIDE `held_bc_winding.py` (OPTION C, the per-cell
director-template hold that DISQUALIFIED — it pumped 56× by overwriting local ω-directions against
the free gradient flow). C is preserved intact (KEEP-BOTH / audit-trail discipline); C′ holds a
DIFFERENT object by a DIFFERENT mechanism.

WHAT C HELD (wrong object): a real-space per-cell DIRECTOR TEMPLATE (`WindingHold`), re-aligned each
    step → fought the free dynamics → did gradient-W work → 56× pump → DISQUALIFY.

WHAT C′ HOLDS (the corpus charge): the conserved **Beltrami helicity** `H_bel = ∫ ω·(∇×ω) dV`
    (`master-equation.md`, two-"3"s disambiguation block, verbatim: "charge = Beltrami helicity
    H_bel = ∫ω·(∇×ω)") — a single GLOBAL scalar invariant on the independent Cosserat-ω carrier.

═════════════════════════════════════════════════════════════════════════════════════════════════
🔴 LOAD-BEARING SPEC-vs-CODE CONFLICT (flag-don't-fix; surfaced before scaffolding, 2026-06-16):
═════════════════════════════════════════════════════════════════════════════════════════════════
    §9.1 gives the LITERAL formula  `H_bel(omega) = sum(_beltrami_helicity(omega, dx)) * dx**3`.
    BUT the engine's `cosserat_field_3d._beltrami_helicity` returns the NORMALIZED handedness
    density  h_local = ω·(∇×ω) / (|ω|·|∇×ω|) ∈ [−1, +1]  (a per-cell handedness, doc 54_ §6),
    NOT the raw helicity density ω·(∇×ω) the corpus integral `∫ω·(∇×ω)dV` calls for.

    Measured on the planted (2,3) traveling seed (N=26, R=5, r=2.5, dx=0.5, amp=0.3):
      • sum(_beltrami_helicity)*dx³  = 137.19  — but 125.5 (91.5%) of that is VACUUM-CELL ARTIFACT
        (cells where |ω|≈0, the eps_h=1e-12 regularizer manufacturing spurious handedness); only
        11.7 comes from the actual shell. Its ∇_ω is stiff (‖grad‖≈5.6e6), vacuum-cell dominated.
        The 137≈1/α resemblance is a COINCIDENCE (it tracks the vacuum-cell count of the box), NOT
        the corpus charge.
      • ∫ω·(∇×ω)dV (RAW)             = 2.1e-4 — the verbatim corpus object: smooth (‖grad‖≈0.71),
        scales as s² in ω (as helicity must), robust 0.269 on the (1,1) Beltrami control. Small on
        the (2,3) plant because the SIGNED helicity nearly cancels (shell density −5.1e-3,
        |density| integral 0.34 — there IS structure, it is sign-cancellation, not absence).

    RESOLUTION (per the brief: "§9.1 wins; flag the conflict, don't silently diverge"): §9.1's
    PROSE intent ("hold the conserved H_bel = ∫ω·(∇×ω), the corpus's actual charge") and its
    LITERAL Python formula CONFLICT, because the named engine helper is normalized. The corpus
    charge — the object `master-equation.md` defines and §9.1's prose names — is the RAW integral.
    C′ HOLDS THE RAW INTEGRAL `H_bel_raw = ∫ω·(∇×ω)dV` as the conserved charge, and ALSO records
    the spec-literal normalized-sum each step for transparency / audit. The held target is the raw
    integral. This conflict is reported to the orchestrator (do not silently pick one).
═════════════════════════════════════════════════════════════════════════════════════════════════

MECHANISM (NO-WORK constraint — energy-neutral BY CONSTRUCTION, unlike C where it was only
    measured and failed):
      g       = ∇_ω H_bel      (gradient of the helicity scalar wrt the ω field; jax.grad)
      e       = ∇_ω E_ω        (gradient of the ω-sector energy = the ω part of the Hamiltonian)
      g_perp  = g − (⟨g,e⟩/⟨e,e⟩) e     (Gram-Schmidt: remove the energy-changing component)
      ω      += λ g_perp       (λ from a 1-D Newton/line-solve on the scalar H_bel(λ) = target)
    Because g_perp ⊥ e, to first order  dE = ⟨e, λ g_perp⟩ = 0  → energy-neutral BY DESIGN. The
    residual second-order curvature is why the FULL-Hamiltonian ledger is STILL verified (the
    `ave-conserved-vs-pumped` witness = eng_w.total_hamiltonian(), NOT sum(ω²) which the C
    false-positive guard-bug read — fixed in commit 86c1a641).

SUBSTRATE-NATIVE WALK (substrate-native-check v1.2, done BEFORE this code):
  CP1 (dynamics)   : the ω-carrier evolves via velocity-Verlet step() (wave propagation). C′ adds a
                     CONSTRAINT correction after the free step — NOT a gradient-descent settle, NOT
                     energy minimization (Rule 6 SM-leak avoided).
  CP2 (sector)     : Cos-sector (Cosserat ω), the INDEPENDENT carrier. H_bel is a Cosserat-sector
                     invariant. The A1 (V_inc,V_ref) phasor is NEVER read or written (G0-clean).
  CP3 (objective)  : AVE-native — a Lagrange constraint on a conserved invariant, projected ⊥ the
                     ω-sector energy gradient. NOT energy-basin minimization.
  CP4 (phase-space): H_bel and ∇_ω H_bel are computed on the ω field directly, the same coordinate
                     the corpus charge=helicity claim lives in. The (2,3) PAIR is read on the
                     (ω, π_ω) phasor (extract_2_3_omega_fast), never real-space lattice-Cartesian.
  CP9 (dynamical)  : the field evolves freely via the engine's OWN step(); the H_bel correction is
                     applied to the EVOLVED state (a projection of the evolved field), not a re-seed.
  CP10 (boundary)  : the correction is a GLOBAL SCALAR constraint closed by a line-solve, NOT a bulk
                     confining force ∝ dS/dA (which is singular at the wall and detonates).

CARRIER DISCIPLINE (load-bearing): operates ONLY on eng_w.omega / eng_w.omega_dot (the independent
    Cosserat-ω carrier). NEVER reads or writes the A1 (V_inc, V_ref) phasor — preserves the G0
    double-count-clean result (`master-equation.md`: never wire the winding into (V_inc, V_ref)).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import jax
import jax.numpy as jnp
import numpy as np

from ave.topological.cosserat_field_3d import (
    _beltrami_helicity,
    _tetrahedral_curl,
)


# ============================================================================
# section: the conserved Beltrami-helicity INTEGRAL (the corpus charge)
# ============================================================================
def H_bel_raw(omega: jnp.ndarray, dx: float) -> jnp.ndarray:
    """The CORPUS CHARGE: the Beltrami-helicity INTEGRAL  H_bel = ∫ ω·(∇×ω) dV.

    `master-equation.md` (two-"3"s disambiguation, verbatim): "charge = Beltrami helicity
    H_bel = ∫ω·(∇×ω)". Discretized as  sum_cells( ω·(∇×ω) ) · dx³  with the SAME tetrahedral
    curl operator the engine uses (`_tetrahedral_curl`, cosserat_field_3d.py). This is the RAW
    (un-normalized) helicity density — quadratic in ω, smooth, scales as s² under ω→sω — NOT the
    normalized handedness `_beltrami_helicity` (see the module-header SPEC-vs-CODE conflict).

    A single global scalar (jnp 0-d array, jax.grad-differentiable wrt omega)."""
    curl = _tetrahedral_curl(omega, dx)
    return jnp.sum(jnp.sum(omega * curl, axis=-1)) * dx**3


def H_bel_normalized_sum(omega: jnp.ndarray, dx: float) -> jnp.ndarray:
    """The SPEC-LITERAL §9.1 formula  sum(_beltrami_helicity(omega,dx)) * dx³ — recorded for
    TRANSPARENCY/audit ONLY, NOT held. This sums the NORMALIZED handedness h_local ∈ [−1,+1]
    (`_beltrami_helicity`), which is dominated by vacuum cells (≈91% artifact on the (2,3) seed;
    see the module-header conflict block). The held charge is `H_bel_raw`, not this."""
    return jnp.sum(_beltrami_helicity(omega, dx)) * dx**3


# jax.grad of the corpus charge wrt the ω field (the constraint gradient g = ∇_ω H_bel).
# jitted: the curl + sum are pure jnp; differentiating is exact (no FD).
_grad_H_bel_raw = jax.jit(jax.grad(H_bel_raw), static_argnums=())


def grad_H_bel(omega: np.ndarray, dx: float) -> np.ndarray:
    """g = ∇_ω H_bel_raw — the gradient of the corpus charge wrt the ω field, as numpy.

    For the symmetric bilinear H = Σ ω·(∇×ω)·dx³, ∇_ω H = (∇×ω + ∇×^T ω)·dx³; jax.grad gets this
    exactly via the tetrahedral-curl adjoint. Returned numpy (the engine state is numpy)."""
    g = _grad_H_bel_raw(jnp.asarray(omega), float(dx))
    return np.asarray(g)


# ============================================================================
# section: the NO-WORK helicity-hold ledger (ave-conserved-vs-pumped witness)
# ============================================================================
@dataclass
class HelicityLedger:
    """Per-application ledger of the NO-WORK H_bel hold. The load-bearing pump
    witness is the FULL omega-sector total_hamiltonian (kinetic + gradient
    potential) BEFORE/AFTER each correction — NOT sum(omega^2) (the C false-
    positive guard-bug: the amplitude is held ~bounded so it is blind to a
    gradient-potential pump; fixed commit 86c1a641). We also record the held
    charge (H_bel_raw before/after), the orthogonality residual cos(g_perp, e)
    (= the no-work design check), and the spec-literal normalized-sum (audit)."""
    n_applications: int = 0
    H_total_before: list = field(default_factory=list)   # eng_w.total_hamiltonian() pre-correction
    H_total_after: list = field(default_factory=list)    # eng_w.total_hamiltonian() post-correction
    H_bel_before: list = field(default_factory=list)     # raw helicity charge pre-correction
    H_bel_after: list = field(default_factory=list)      # raw helicity charge post-correction
    H_bel_target: list = field(default_factory=list)     # the (2,3)-seed target charge
    cos_gperp_e: list = field(default_factory=list)       # orthogonality residual (design check)
    lambda_used: list = field(default_factory=list)       # the line-solve step
    H_norm_sum_after: list = field(default_factory=list)  # spec-literal §9.1 (transparency only)

    def record(self, *, H0, H1, Hb0, Hb1, Htgt, cos_res, lam, Hnorm):
        self.n_applications += 1
        self.H_total_before.append(float(H0))
        self.H_total_after.append(float(H1))
        self.H_bel_before.append(float(Hb0))
        self.H_bel_after.append(float(Hb1))
        self.H_bel_target.append(float(Htgt))
        self.cos_gperp_e.append(float(cos_res))
        self.lambda_used.append(float(lam))
        self.H_norm_sum_after.append(float(Hnorm))

    def summary(self) -> dict:
        if self.n_applications == 0:
            return {"n_applications": 0, "note": "hold never applied"}
        Hb_a = np.array(self.H_total_after)
        Hb_b = np.array(self.H_total_before)
        # per-application injected total-energy (post − pre correction): the no-work residual
        dE = Hb_a - Hb_b
        # the held charge: did the hold actually CLOSE the gap to target?
        hbel_after = np.array(self.H_bel_after)
        hbel_tgt = np.array(self.H_bel_target)
        tgt_scale = float(np.median(np.abs(hbel_tgt))) if np.median(np.abs(hbel_tgt)) > 1e-30 else 1.0
        charge_err = np.abs(hbel_after - hbel_tgt) / (tgt_scale + 1e-30)
        return {
            "n_applications": self.n_applications,
            # --- no-work design check: the orthogonality residual cos(g_perp, e) ~ 0 ---
            "orthogonality_cos_max_abs": float(np.max(np.abs(self.cos_gperp_e))),
            "orthogonality_cos_mean_abs": float(np.mean(np.abs(self.cos_gperp_e))),
            # --- the load-bearing pump witness: total-energy injection per correction ---
            "total_injection_per_app_mean": float(np.mean(dE)),
            "total_injection_per_app_max": float(np.max(dE)),
            "total_injection_cumulative": float(np.sum(dE)),
            # --- did the constraint hold the charge to target? ---
            "charge_rel_err_to_target_mean": float(np.mean(charge_err)),
            "charge_rel_err_to_target_max": float(np.max(charge_err)),
            "H_bel_target_median": tgt_scale,
            # --- the line-solve step magnitudes ---
            "lambda_abs_mean": float(np.mean(np.abs(self.lambda_used))),
            "lambda_abs_max": float(np.max(np.abs(self.lambda_used))),
            # --- spec-literal §9.1 normalized-sum (transparency; NOT the held charge) ---
            "H_norm_sum_after_median": float(np.median(self.H_norm_sum_after)),
        }


# ============================================================================
# section: the NO-WORK Beltrami-helicity HOLD (the load-bearing C′ operator)
# ============================================================================
@dataclass
class HelicityHold:
    """The NO-WORK H_bel hold (A-reusable). After each free engine step, restore the
    conserved Beltrami-helicity charge H_bel_raw = ∫ω·(∇×ω)dV to its (2,3)-seed target
    via a correction projected ⊥ the ω-sector energy gradient — energy-neutral BY
    CONSTRUCTION (the Gram-Schmidt no-work design), then VERIFIED via the full-Hamiltonian
    ledger (ave-conserved-vs-pumped).

    USAGE (the C′ driver):
        hold = HelicityHold.from_engine(eng_w, dx)   # captures the (2,3)-seed target H_bel
        ...
        step_coupled(eng_V, eng_w, dx)               # the carrier evolves FREELY (CP9)
        hold.apply(eng_w)                            # restore H_bel ⊥ energy grad (no-work)

    NEVER touches eng_V / the A1 (V_inc,V_ref) phasor (G0-clean; master-equation.md)."""

    dx: float
    H_bel_target: float
    ledger: HelicityLedger = field(default_factory=HelicityLedger)
    # line-solve controls
    max_newton: int = 12
    tol_rel: float = 1e-6

    @classmethod
    def from_engine(cls, eng_w, dx: float) -> "HelicityHold":
        """Capture the (2,3)-seed's conserved charge as the held target. This is the
        charge the seed plants; the hold restores the EVOLVED field back to it each step."""
        H0 = float(H_bel_raw(jnp.asarray(eng_w.omega), float(dx)))
        return cls(dx=float(dx), H_bel_target=H0)

    def _energy_grad_omega(self, eng_w) -> np.ndarray:
        """e = ∇_ω E_ω — the gradient of the ω-sector energy the engine's step() actually
        integrates (energy_gradient() → the SATURATED functional, use_saturation default).
        Making the correction ⊥ THIS vector ⇒ no work against the real dynamical energy."""
        _, dE_dw = eng_w.energy_gradient()
        return np.asarray(dE_dw)

    def apply(self, eng_w, *, record: bool = True) -> None:
        """Restore H_bel to target via a NO-WORK correction (the load-bearing op).

        Order (CP9): the engine's step() has ALREADY advanced (omega, omega_dot) freely;
        this corrects the EVOLVED omega field back to the conserved-charge target along the
        energy-orthogonal direction g_perp.

          g       = ∇_ω H_bel_raw                                  (the constraint gradient)
          e       = ∇_ω E_ω        (= energy_gradient()[1])        (the energy gradient)
          g_perp  = g − (⟨g,e⟩/⟨e,e⟩) e                            (Gram-Schmidt; ⊥ e)
          omega  += λ g_perp,  λ : H_bel_raw(omega + λ g_perp) = target   (1-D Newton)

        Because g_perp ⊥ e, to first order dE = ⟨e, λ g_perp⟩ = 0 — neutral BY DESIGN. The
        ledger records the FULL total_hamiltonian before/after (the pump witness) so a
        residual-curvature pump still DISQUALIFIES."""
        dx = self.dx
        omega = np.asarray(eng_w.omega)
        alive = eng_w.mask_alive[..., None].astype(omega.dtype)

        if record:
            H0 = float(eng_w.total_hamiltonian())
            Hb0 = float(H_bel_raw(jnp.asarray(omega), dx))

        g = grad_H_bel(omega, dx) * alive          # ∇_ω H_bel  (corpus charge)
        e = self._energy_grad_omega(eng_w) * alive  # ∇_ω E_ω    (dynamical energy)

        ee = float(np.sum(e * e))
        ge = float(np.sum(g * e))
        if ee > 1e-30:
            g_perp = g - (ge / ee) * e              # remove the energy-changing component
        else:
            g_perp = g                              # degenerate: no energy gradient to fight
        g_perp = g_perp * alive

        # orthogonality residual (the no-work design check): cos(g_perp, e) must be ~0
        gp_norm = float(np.sqrt(np.sum(g_perp * g_perp)))
        e_norm = float(np.sqrt(ee))
        cos_res = (float(np.sum(g_perp * e)) / (gp_norm * e_norm)) if (gp_norm > 1e-30 and e_norm > 1e-30) else 0.0

        # 1-D Newton/line-solve: find λ so H_bel_raw(omega + λ g_perp) = target.
        lam = self._line_solve_lambda(omega, g_perp, dx, self.H_bel_target)
        omega_new = (omega + lam * g_perp) * alive
        eng_w.omega = omega_new

        if record:
            H1 = float(eng_w.total_hamiltonian())
            Hb1 = float(H_bel_raw(jnp.asarray(omega_new), dx))
            Hnorm = float(H_bel_normalized_sum(jnp.asarray(omega_new), dx))
            self.ledger.record(H0=H0, H1=H1, Hb0=Hb0, Hb1=Hb1, Htgt=self.H_bel_target,
                               cos_res=cos_res, lam=lam, Hnorm=Hnorm)

    def _line_solve_lambda(self, omega, g_perp, dx, target) -> float:
        """1-D Newton on the scalar f(λ) = H_bel_raw(omega + λ g_perp) − target.

        H_bel_raw is QUADRATIC in omega, so f(λ) is quadratic in λ:
            f(λ) = a λ² + b λ + c,   c = H_bel_raw(omega) − target.
        We fit (a,b) from f(0), f(±h) (3-point) and take the root of the quadratic nearest
        λ=0 (the minimal-displacement correction). Falls back to Newton iterations if the
        quadratic is degenerate. Bounded by a max |λ| so a near-singular b can't detonate."""
        def f(lam):
            return float(H_bel_raw(jnp.asarray(omega + lam * g_perp), dx)) - target

        gp2 = float(np.sum(g_perp * g_perp))
        if gp2 < 1e-30:
            return 0.0
        # characteristic scale for the probe step h: bring λ·|g_perp| to ~unit field change
        h = 1.0 / np.sqrt(gp2)
        f0 = f(0.0)
        if abs(f0) <= self.tol_rel * (abs(target) + 1e-30):
            return 0.0  # already on target
        fp = f(h)
        fm = f(-h)
        a = (fp + fm - 2.0 * f0) / (2.0 * h * h)     # ½ f''
        b = (fp - fm) / (2.0 * h)                     # f'
        c = f0
        lam = self._quad_root_nearest_zero(a, b, c)
        if lam is None:
            # degenerate quadratic → Newton fallback
            lam = 0.0
            for _ in range(self.max_newton):
                val = f(lam)
                if abs(val) <= self.tol_rel * (abs(target) + 1e-30):
                    break
                d = (f(lam + h) - f(lam - h)) / (2.0 * h)
                if abs(d) < 1e-30:
                    break
                lam = lam - val / d
        # bound the step so a near-flat b can't blow the field up
        lam_cap = 50.0 * h
        return float(np.clip(lam, -lam_cap, lam_cap))

    @staticmethod
    def _quad_root_nearest_zero(a, b, c):
        """Root of a λ² + b λ + c = 0 nearest λ=0 (minimal-displacement correction)."""
        if abs(a) < 1e-30:
            if abs(b) < 1e-30:
                return None
            return -c / b
        disc = b * b - 4.0 * a * c
        if disc < 0.0:
            return None  # no real root (constraint unreachable along this ray) → Newton/fallback
        sq = np.sqrt(disc)
        r1 = (-b + sq) / (2.0 * a)
        r2 = (-b - sq) / (2.0 * a)
        return r1 if abs(r1) <= abs(r2) else r2

    def is_energy_neutral(self, *, frac_tol: float = 0.02) -> tuple[bool, dict]:
        """The DISQUALIFY decision (ave-conserved-vs-pumped). The witness is the FULL
        total_hamiltonian TRAJECTORY ramp (read by the driver via ledger.H_total_after),
        NOT sum(omega^2). Here we report the per-application no-work residual + the
        orthogonality design check. A hold whose total_hamiltonian trajectory RAMPS
        (driver's _omega_energy_trajectory_ramp on H_total_after) → DISQUALIFY."""
        s = self.ledger.summary()
        if s.get("n_applications", 0) == 0:
            return True, s
        # design-level neutrality: the per-correction injection should be small AND the
        # orthogonality residual ~0 (the no-work construction held to numerical precision).
        ortho_ok = s["orthogonality_cos_max_abs"] < 1e-6
        s["orthogonality_no_work_ok"] = bool(ortho_ok)
        s["frac_tol"] = frac_tol
        s["DISQUALIFY_decided_by"] = "driver _omega_energy_trajectory_ramp(ledger.H_total_after)"
        return ortho_ok, s
