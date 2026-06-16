"""The CONSERVATIVE (2,3)-winding HOLD — the held-BC machinery (OPTION C; A-reusable).

🔴 AUDIT HEADER (2026-06-15, OPTION C live-fire — Rule-12, body preserved below):
    The "ENERGY-NEUTRAL / CONSERVATIVE constraint" claim is FALSIFIED for the POTENTIAL
    (gradient/curvature) term. The magnitude-lock DOES hold the KINETIC energy + |omega|
    norm EXACTLY (verified to ~1e-14 / ~1e-16 — the kinetic guarantee is real). But the
    hard per-cell phase projection re-aligns the EVOLVED directions back to the smooth
    (2,3) template each step, which (a) injects gradient-potential energy, and (b) feeds a
    perpetual off-free-evolution state that the engine step() amplifies: the omega-sector
    total_hamiltonian RAMPS ~56x over a 1500-step coupled run (vs a FLAT free run) —
    a PUMP. Per the energy ledger summary()'s OWN cumulative-injection read, DISQUALIFY
    fires (correctly). A partial-blend (soft) hold was swept (g∈[0.01,0.5]) and finds NO
    conservative window: soft holds fail to MAINTAIN the (2,3) (frac~0.05) while hard holds
    PUMP — so this is NOT a fixable code bug but a structural property of hard-projecting
    the winding against free Cosserat-omega dynamics on this carrier.
    CONSEQUENCE: the DISQUALIFY pump-witness MUST be eng_w.total_hamiltonian() (the FULL
    kinetic+potential ledger, = HoldLedger.total_after), NOT sum(omega^2) / |omega| (the
    amplitude, which the magnitude-lock holds bounded BY CONSTRUCTION → blind to the pump).
    OPTION C BIN = DISQUALIFY. A (re)user (OPTION A) must NOT treat this hold as a
    conservative constraint; it is a hard projection that pumps. The body is preserved for
    the kinetic-lock machinery + the (correctly-firing) ledger guard.

PURPOSE (lane brief / prereg §9, OPTION C):
    The (2,3) winding is a CONSERVED TOPOLOGICAL INTEGER (charge — a topological
    boundary condition, held by definition; `substrate-native-terminology.md`
    "topology owns the integers"). The production seed-and-evolve driver let it
    DISPERSE — a category error (a topological integer does not "evolve and smooth
    to garbage"). This module HOLDS it: each step it re-imposes the (2,3) phase
    structure on the independent Cosserat-omega carrier, as a CONSERVATIVE
    constraint/projection — NOT an energy pump.

THE LOAD-BEARING REQUIREMENT (ave-conserved-vs-pumped — the DISQUALIFY guard):
    The hold MUST be ENERGY-NEUTRAL. If it injects energy (the omega-sector total
    energy ramps because of the projection, not the physics), a "persistent"
    breather is a PUMPED ARTIFACT, not a positive. This module therefore:
      (1) implements the hold as a per-cell PHASE-ONLY projection that preserves
          each cell's omega / omega_dot MAGNITUDE (so the per-cell kinetic energy
          density 1/2 I_omega |omega_dot|^2 is held cell-by-cell invariant), and
      (2) returns a per-application ENERGY LEDGER (the omega-sector total-energy
          delta the projection caused) so the caller can DISQUALIFY a pumping hold.

SUBSTRATE-NATIVE WALK (substrate-native-check v1.2; done BEFORE this code):
  CP6 (reactance pair) : the winding lives in the (omega, omega_dot) LC PHASOR — the
                         C-state (omega . dhat) + L-state (pi_omega . dhat) pair that
                         extract_2_3_omega_fast reads. The hold operates on this
                         phasor pair, NOT on a real-space scalar count.
  CP8 (held, not seeded): we re-IMPOSE the (2,3) each step (the imposed-BC framing,
                         prereg §7.1) — a topological integer held by definition,
                         not a one-shot IC that free-evolves (the production error).
  CP9 (dynamical)       : the field evolves freely via the engine's OWN step(); the
                         hold is a PROJECTION OF THE EVOLVED STATE back onto the
                         (2,3) template phase, applied after the dynamics — not an
                         algebraic re-seed of a static eigenvector.
  CP10 (boundary)       : the (2,3) winding IS the topological boundary condition
                         (charge); holding it is the BC enforcement the prereg
                         charters, not a bulk force term.

PHASE-SPACE DISCIPLINE (phase-space-coordinate-check, A46): the projection is a
    PHASE rotation in the (omega, omega_dot) phasor space — it re-aligns each cell's
    director to the (2,3) template's phase pattern (cos(q.psi), cos(p.phi) sign
    structure) while preserving the cell's phasor MAGNITUDE. It is NEVER a
    real-space lattice-Cartesian winding re-count, and it NEVER touches the A1
    (V_inc, V_ref) phasor (the genesis-24 double-count; G0-clean, preserved).

ENERGY-NEUTRALITY ARGUMENT (why this is a constraint, not a pump):
    The omega-sector energy is  E = K + W  with
      K (kinetic)   = 1/2 I_omega sum |omega_dot|^2   -- depends ONLY on per-cell |omega_dot|
      W (potential) = the curvature/strain functional  -- depends on omega AND its
                      spatial GRADIENTS (curvature ~ curl(omega)).
    The hold preserves each cell's |omega| and |omega_dot| EXACTLY (magnitude-locked).
    => K is held EXACTLY invariant cell-by-cell (kinetic neutrality is GUARANTEED).
    => W can shift, because re-aligning DIRECTIONS changes spatial gradients. The
       hold projects onto the SMOOTH (2,3) template (a low-curvature target), so it
       does NOT manufacture high-gradient structure; but exact W-neutrality is NOT
       guaranteed analytically => it MUST be MEASURED (the energy ledger), and a
       net-positive W injection that ramps over the run => DISQUALIFY. This module
       reports the ledger; the caller (the driver) reads it BEFORE persistence and
       DISQUALIFIES if it pumps. (ave-conserved-vs-pumped: verify, do not assume.)
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


# ============================================================================
# section: the (2,3) phase template (the held topological BC), built ONCE
# ============================================================================
@dataclass
class WindingTemplate:
    """The (p,q) phase template on the torus shell — the conserved topological
    BC the hold re-imposes. Built ONCE from the lattice geometry (N, R, r, p, q,
    axis); cached director unit-fields so the per-step projection is cheap and
    deterministic. This is the SAME torus-shell phase structure that
    planted_winding_field('traveling') seeds — so holding to this template holds
    EXACTLY the carrier the G4 gate certifies (extractor-matched)."""

    N: int
    R: float
    r: float
    p: int = 2
    q: int = 3
    axis: int = 2
    helicity: int = 1

    # cached fields (filled in __post_init__)
    env: np.ndarray = field(default=None, repr=False)            # smooth torus-shell envelope
    dir_now: np.ndarray = field(default=None, repr=False)        # (N,N,N,3) unit C-state director
    dir_l: np.ndarray = field(default=None, repr=False)          # (N,N,N,3) unit L-state director
    shell_mask: np.ndarray = field(default=None, repr=False)     # where the template is defined

    def __post_init__(self):
        self._build()

    def _build(self):
        """Build the (p,q) director templates EXACTLY as planted_winding_field does
        (so the hold re-imposes the G4-certified carrier's phase to the bit).

        The C-state director  ~  cos(q.psi) * [dR.cos(phi), dR.sin(phi), dax]
        The L-state director  ~  helicity * sin(q.psi) * [same direction unit]
        with dR=cos(p.phi), dax=sin(p.phi). We store the UNIT versions of the
        full 3-vector (C-state) and the spatial quadrature partner (L-state) so the
        projection re-imposes the (2,3) PHASE pattern while taking the per-cell
        magnitude from the LIVE evolved field (energy-neutral magnitude lock)."""
        N, R, r, p, q, axis = self.N, self.R, self.r, self.p, self.q, self.axis
        c = (N - 1) / 2.0
        idx = np.indices((N, N, N))
        others = [a for a in range(3) if a != axis]
        t1 = idx[others[0]] - c
        t2 = idx[others[1]] - c
        ax = idx[axis] - c
        rho = np.sqrt(t1 ** 2 + t2 ** 2)
        phi = np.arctan2(t2, t1)
        psi = np.arctan2(ax, rho - R)
        rtube = np.sqrt((rho - R) ** 2 + ax ** 2)
        env = np.exp(-(rtube ** 2) / (2.0 * (0.6 * r) ** 2)) * (rho > 2)

        beta = p * phi
        Theta = q * psi
        dR = np.cos(beta)
        dax = np.sin(beta)
        cphi = np.cos(phi)
        sphi = np.sin(phi)

        # base 3-vector DIRECTION (the spatial polarization-2 + axial structure)
        vec = np.zeros((N, N, N, 3))
        vec[..., others[0]] = dR * cphi
        vec[..., others[1]] = dR * sphi
        vec[..., axis] = dax
        vec_norm = np.linalg.norm(vec, axis=-1, keepdims=True)
        vec_unit = np.divide(vec, vec_norm, out=np.zeros_like(vec), where=vec_norm > 1e-12)

        s_h = int(np.sign(self.helicity)) if self.helicity != 0 else 0
        # C-state phase pattern cos(q.psi); L-state (spatial-quadrature partner)
        # helicity.sin(q.psi) -- the SAME advancing-quadrature structure the
        # 'traveling' plant uses (=> the extractor reads w_pol=q, sign=helicity).
        f_now = np.cos(Theta)
        f_l = s_h * np.sin(Theta)

        self.env = env
        self.shell_mask = env > (0.05 * float(env.max()) if env.max() > 0 else 0.0)
        # the (2,3)-phase-bearing director templates (UNIT direction x phase pattern)
        self.dir_now = vec_unit * f_now[..., None]   # C-state template (unit dir * cos(q psi))
        self.dir_l = vec_unit * f_l[..., None]        # L-state template (unit dir * h sin(q psi))
        # unit versions of the phase-bearing templates (the projection axes)
        dn_norm = np.linalg.norm(self.dir_now, axis=-1, keepdims=True)
        dl_norm = np.linalg.norm(self.dir_l, axis=-1, keepdims=True)
        self._dir_now_unit = np.divide(self.dir_now, dn_norm,
                                       out=np.zeros_like(self.dir_now), where=dn_norm > 1e-12)
        self._dir_l_unit = np.divide(self.dir_l, dl_norm,
                                     out=np.zeros_like(self.dir_l), where=dl_norm > 1e-12)


# ============================================================================
# section: the CONSERVATIVE hold projection (the load-bearing energy-neutral op)
# ============================================================================
@dataclass
class HoldLedger:
    """Per-application energy ledger of the hold (ave-conserved-vs-pumped guard).

    The hold preserves each cell's |omega| and |omega_dot| EXACTLY, so the KINETIC
    energy K = 1/2 I_omega sum|omega_dot|^2 is invariant BY CONSTRUCTION (kinetic
    delta is a numerical-zero check). The POTENTIAL W can shift (re-aligning
    directions changes spatial gradients); that delta is MEASURED here. A net
    positive delta that RAMPS over the run => the hold pumps => DISQUALIFY."""
    n_applications: int = 0
    kinetic_before: list = field(default_factory=list)
    kinetic_after: list = field(default_factory=list)
    total_before: list = field(default_factory=list)
    total_after: list = field(default_factory=list)
    omega_norm_before: list = field(default_factory=list)
    omega_norm_after: list = field(default_factory=list)

    def record(self, K0, K1, E0, E1, n0, n1):
        self.n_applications += 1
        self.kinetic_before.append(float(K0))
        self.kinetic_after.append(float(K1))
        self.total_before.append(float(E0))
        self.total_after.append(float(E1))
        self.omega_norm_before.append(float(n0))
        self.omega_norm_after.append(float(n1))

    def summary(self) -> dict:
        """The DISQUALIFY read: per-step injected energy + the cumulative ramp.

        injected_per_step = E_after(hold) - E_before(hold), the energy the
        projection ADDS each application. The cumulative sum is the total pumped
        energy over the run. We report both the absolute per-step injection and
        the injection NORMALIZED by the field energy scale (the pump fraction)."""
        if self.n_applications == 0:
            return {"n_applications": 0, "energy_neutral": True, "note": "hold never applied"}
        Kb = np.array(self.kinetic_before)
        Ka = np.array(self.kinetic_after)
        Eb = np.array(self.total_before)
        Ea = np.array(self.total_after)
        nb = np.array(self.omega_norm_before)
        na = np.array(self.omega_norm_after)
        # kinetic delta: must be ~numerical-zero (magnitude-locked by construction)
        dK = Ka - Kb
        # total-energy injection per application (the pump signal)
        dE = Ea - Eb
        # the field energy scale (median total energy) -> the pump FRACTION
        E_scale = float(np.median(np.abs(Eb))) if np.median(np.abs(Eb)) > 1e-30 else 1.0
        # |omega| magnitude lock: the per-cell norm sum must be preserved exactly
        d_norm = na - nb
        return {
            "n_applications": self.n_applications,
            # kinetic neutrality (guaranteed by the magnitude lock; numerical check)
            "kinetic_delta_max_abs": float(np.max(np.abs(dK))),
            "kinetic_delta_mean": float(np.mean(dK)),
            # the load-bearing pump signal: total-energy injection per application
            "total_injection_per_app_mean": float(np.mean(dE)),
            "total_injection_per_app_max": float(np.max(dE)),
            "total_injection_cumulative": float(np.sum(dE)),
            "total_injection_fraction_per_app_mean": float(np.mean(dE) / E_scale),
            "total_injection_fraction_cumulative": float(np.sum(dE) / E_scale),
            # omega-norm lock (|omega| preserved => energy-neutral by construction)
            "omega_norm_delta_max_abs": float(np.max(np.abs(d_norm))),
            "omega_norm_relative_drift_max": float(np.max(np.abs(d_norm)) / (np.median(nb) + 1e-30)),
            "energy_scale_median": E_scale,
        }


def _project_to_template_phase(field_vec: np.ndarray, dir_unit: np.ndarray,
                               shell_mask: np.ndarray) -> np.ndarray:
    """Phase-only projection (the ENERGY-NEUTRAL core, A46 phase-space discipline).

    For each cell in the template shell, replace the field vector's DIRECTION with
    the (2,3) template's unit director `dir_unit`, but KEEP the cell's MAGNITUDE
    |field_vec| EXACTLY. Outside the shell the field is left UNTOUCHED (the hold
    acts only where the topological BC is defined).

        held = |field_vec| * dir_unit          (in the shell)
        held = field_vec                        (outside the shell)

    => per-cell |held| == |field_vec| EXACTLY where dir_unit is a unit vector =>
       the per-cell energy-density MAGNITUDE is preserved (the magnitude lock).
    The DIRECTION carries the (2,3) phase (the held topological integer). This is a
    rotation of each cell's phasor onto the template axis, magnitude-preserving =>
    a CONSTRAINT, not a drive."""
    mag = np.linalg.norm(field_vec, axis=-1, keepdims=True)
    held = mag * dir_unit
    # only re-impose inside the template shell; preserve the field elsewhere
    m = shell_mask[..., None]
    return np.where(m, held, field_vec)


@dataclass
class WindingHold:
    """The held-BC operator (A-reusable). Wraps a WindingTemplate + a HoldLedger and
    applies the conservative (2,3) hold to a Cosserat-omega carrier each step.

    USAGE (the C driver; A reuses verbatim + adds the residual->0 eigensolve):
        hold = WindingHold.from_config(N, R, r, p=2, q=3, helicity=1)
        ...
        eng_w.step()                 # the carrier evolves FREELY (CP9 dynamical)
        hold.apply(eng_w)            # then the (2,3) is RE-IMPOSED (held BC),
                                     #   magnitude-locked => energy-neutral (verify
                                     #   via hold.ledger.summary()).

    apply() records the energy ledger (kinetic + total, before/after the hold) so the
    caller can DISQUALIFY a pumping hold BEFORE reading persistence."""

    template: WindingTemplate
    ledger: HoldLedger = field(default_factory=HoldLedger)

    @classmethod
    def from_config(cls, N, R, r, *, p=2, q=3, axis=2, helicity=1) -> "WindingHold":
        tmpl = WindingTemplate(N=N, R=R, r=r, p=p, q=q, axis=axis, helicity=helicity)
        return cls(template=tmpl)

    def _omega_sector_energy(self, eng_w) -> tuple[float, float, float]:
        """(kinetic K, total H, omega-norm-sum) of the omega carrier — the ledger
        quantities. K = 1/2 I_omega sum|omega_dot|^2 (the magnitude-locked part);
        H = total_hamiltonian = K_u + K_omega + W (the full ledger, including the
        gradient/curvature potential the projection CAN shift). omega-norm-sum =
        sum |omega| (the magnitude-lock witness — must be preserved exactly)."""
        mask = eng_w.mask_alive[..., None].astype(eng_w.omega_dot.dtype)
        K = 0.5 * eng_w.I_omega * float(np.sum((eng_w.omega_dot * mask) ** 2))
        H = float(eng_w.total_hamiltonian())
        n = float(np.sum(np.linalg.norm(eng_w.omega, axis=-1)))
        return K, H, n

    def apply(self, eng_w, *, record: bool = True) -> None:
        """Re-impose the (2,3) winding (the held topological BC) on the omega
        carrier, CONSERVATIVELY (magnitude-locked phase projection). Records the
        energy ledger if `record` (the DISQUALIFY guard).

        Order (CP9): the engine's step() has ALREADY advanced (omega, omega_dot)
        freely; this projects the EVOLVED state back onto the (2,3) template phase.
        Both the C-state (omega) and the L-state (omega_dot) are re-aligned to the
        template's C/L directors, preserving each cell's magnitude => the (omega,
        omega_dot) phasor's (2,3) winding is restored while the per-cell phasor
        magnitude (=> kinetic energy density) is held cell-by-cell invariant."""
        tmpl = self.template
        if record:
            K0, E0, n0 = self._omega_sector_energy(eng_w)

        alive = eng_w.mask_alive[..., None]
        # C-state: re-impose the cos(q.psi) director phase, magnitude-locked
        omega_held = _project_to_template_phase(eng_w.omega, tmpl._dir_now_unit, tmpl.shell_mask)
        # L-state: re-impose the helicity.sin(q.psi) quadrature partner, magnitude-locked
        omega_dot_held = _project_to_template_phase(eng_w.omega_dot, tmpl._dir_l_unit, tmpl.shell_mask)
        eng_w.omega = omega_held * alive
        eng_w.omega_dot = omega_dot_held * alive

        if record:
            K1, E1, n1 = self._omega_sector_energy(eng_w)
            self.ledger.record(K0, K1, E0, E1, n0, n1)

    def is_energy_neutral(self, *, frac_tol: float = 0.02) -> tuple[bool, dict]:
        """The DISQUALIFY decision (ave-conserved-vs-pumped). Energy-neutral if:
          (a) the |omega| magnitude lock holds (omega_norm relative drift ~ 0 — the
              projection preserved per-cell magnitudes, the kinetic guarantee), AND
          (b) the CUMULATIVE total-energy injection fraction stays below frac_tol
              (the projection did NOT ramp the omega-sector energy over the run).
        A hold that FAILS (b) is a PUMP => the run is DISQUALIFIED (a 'persistent'
        breather would be a pumped artifact, not a positive)."""
        s = self.ledger.summary()
        if s.get("n_applications", 0) == 0:
            return True, s
        norm_locked = s["omega_norm_relative_drift_max"] < 1e-9
        cumulative_neutral = abs(s["total_injection_fraction_cumulative"]) < frac_tol
        neutral = norm_locked and cumulative_neutral
        s["norm_lock_ok"] = bool(norm_locked)
        s["cumulative_neutral"] = bool(cumulative_neutral)
        s["frac_tol"] = frac_tol
        s["energy_neutral"] = bool(neutral)
        s["DISQUALIFY_if_pumps"] = not bool(neutral)
        return neutral, s
