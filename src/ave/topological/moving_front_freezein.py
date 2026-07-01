"""Moving-front freeze-in: a spatially-PROPAGATING yield-crossing front that
freezes in a PRE-EXISTING real-space ω-defect via the BEMF-blocked-dω/dt
mechanism.

Frozen prereg: research/2026-06-30_moving-front-freezein_prereg_FROZEN.md
(SHA-pinned 7b97e76d, off main eaadeaf1).

SECTOR/REGIME (prereg §0): MODE = cosmological crystallization front. REGIME =
propagating yield-crossing V through V_yield sweeping at v_front, at/near
saturation A→1 at the front. PHASE-STATE = transitional. The native mechanism is
BEMF-blocked unwinding via the diverging L_eff Lenz back-EMF near S→0 — NOT a
Kibble-Zurek import (dark-wake-bemf:54).

DERIVED FREEZE-DIRECTION (prereg §2.3): FAST crossing
(Δt_cross = ℓ_front/v_front ≲ τ_relax) → S lags low → L_eff/BEMF block on dω/dt
PERSISTS → FREEZE. SLOW crossing → S tracks S_eq → block lifts → HEAL.

Reuse (anti-rebuild, Rule 14): CoupledK4Cosserat (k4_cosserat_coupling.py) with
its ALREADY-IMPLEMENTED per-cell relaxation ODE dS/dt=(S_eq−S)/τ_relax
(k4_tlm.py:283). The NEW pieces here (prereg §3):
  1. a MOVING spatial yield boundary V(x,t) = ramp centred on x_front(t)=x0+v·t,
     driven into k4.V_inc (prior work: STATIC valve only);
  2. a memristive-lagged front-clamp on dω/dt keyed to the LAGGED S(t) relaxation
     state (k4.S_field), so L_eff(S(t)) carries the fast→freeze asymmetry — the
     existing _freeze_clamp_omega0_shared reads INSTANTANEOUS S_eq and has no
     memory.

COORDINATE DISCIPLINE (Guard 3): real-space ω-defect ONLY. The freeze detector
is a real-space contour winding on the ω-field. This does NOT deliver the (2,3)
phase-space winding (separate open winder-primitive gate).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from ave.core import constants as C
from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat


__all__ = [
    "FrontConfig",
    "MovingFrontFreezeIn",
    "seed_omega_defect",
    "lossless_defect_check",
]


# =====================================================================
# Front configuration
# =====================================================================
@dataclass
class FrontConfig:
    """Moving yield-crossing front parameters (native units, τ_relax = 1).

    The front is a down-crossing (heal) boundary in the strain field r = V/V_SNAP:
    AHEAD of the front (x > x_front) the cell is in the slipstream (r > 1, S ≈ 0);
    BEHIND (x < x_front) it has re-solidified (r < 1, S recovering). The boundary
    sweeps in +x at v_front. Each cell experiences a local down-crossing over a
    window Δt_cross ≈ ℓ_front / v_front.

    Per prereg §2.3 the discriminator is Δt_cross / τ_relax; τ_relax = 1 native.
    """

    N: int = 24
    pml: int = 4
    # Front geometry (lattice units).
    ell_front: float = 2.0          # spatial thickness of the crossing ramp [cells]
    v_front: float = 1.0            # front sweep speed [cells / native-time]
    x0_frac: float = 0.30           # initial front position (fraction of interior)
    # Strain amplitudes (r = V/V_SNAP): ahead saturated, behind solid.
    r_ahead: float = 1.20           # slipstream strain ahead of front (r > 1)
    r_behind: float = 0.30          # re-solidified strain behind front (r < 1)
    # Integration.
    n_pre: int = 40                 # lossless pre-front steps (Guard 1 check)
    n_post_compton: float = 120.0   # post-front recording length [Compton periods]
    record_every: int = 1

    @property
    def dt_cross(self) -> float:
        """Local down-crossing window duration Δt_cross = ℓ_front / v_front."""
        return self.ell_front / max(self.v_front, 1e-12)

    @property
    def dt_cross_over_tau(self) -> float:
        """The prereg §2.3 discriminator, τ_relax = 1 in native units."""
        return self.dt_cross / C.TAU_RELAX_NATIVE

    @property
    def regime(self) -> str:
        """Mechanism-predicted regime (prereg §2.3)."""
        return "FAST→FREEZE" if self.dt_cross_over_tau <= 1.0 else "SLOW→HEAL"


# =====================================================================
# Pre-existing ω-defect seed (Guard 1: TRAP-not-CREATE)
# =====================================================================
def seed_omega_defect(sim: CoupledK4Cosserat, *, R_major: float = 5.0,
                      amp: float = 0.6, sigma: float = 2.0) -> None:
    """Seed a PRE-EXISTING topologically-nontrivial real-space ω-fluctuation,
    aligned to the detector geometry of extract_crossing_count.

    Guard 1 (TRAP-not-CREATE): this installs the defect BEFORE the front arrives,
    as an initial condition on the ω-field — the front will later TRAP it, not
    source it.

    Geometry (matched to extract_shell_radii / extract_crossing_count): the major
    ring lies in the x–y plane centred on the grid at radius R_major; the winding
    is a 2π turn of arg(ω_x, ω_y) around the POLOIDAL loop (parameterised by the
    angle in the (ρ_xy − R, z) plane). This is the real-space 0₁-class ω-loop the
    detector reads (verified Q=1 on this pattern).

    Coordinate discipline (Guard 3): a REAL-SPACE ω-defect. No claim on the (2,3)
    phase-space winding.
    """
    cos = sim.cos
    nx, ny, nz = cos.nx, cos.ny, cos.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0
    i = cos._i.astype(float)
    j = cos._j.astype(float)
    k = cos._k.astype(float)
    rho_xy = np.sqrt((i - cx) ** 2 + (j - cy) ** 2)
    # Poloidal angle in the (ρ_xy − R, z) plane.
    pol = np.arctan2(k - cz, rho_xy - R_major)
    env = amp * np.exp(-((rho_xy - R_major) ** 2 + (k - cz) ** 2) / (2.0 * sigma**2))
    # 2π poloidal winding of (ω_x, ω_y) — extract_crossing_count's contour read.
    cos.omega[..., 0] += env * np.cos(pol)
    cos.omega[..., 1] += env * np.sin(pol)
    cos.omega *= cos.mask_alive[..., None]


def lossless_defect_check(N: int = 24, pml: int = 0, n_steps: int = 6,
                          **seed_kw) -> dict:
    """Guard 1 verification: the seeded defect must PRE-EXIST under LOSSLESS
    (conservative, front-off) evolution with energy conserved — no net injection
    sourced the winding (prereg §4 G1).

    IMPLEMENTATION NOTE (Rule 10 integrator-time finding, 2026-06-30): the bare
    ω-loop is a DISPERSING wave packet, not a stationary soliton — it radiates and
    the winding decays on its own over ~τ_disperse (≈ sub-Compton on small grids).
    So G1 is checked over a SHORT lossless window (n_steps within τ_disperse), and
    a separate `bare_dispersion_baseline()` records how long the winding survives
    WITHOUT any front. G1's job is only to certify (i) the defect EXISTS at seeding
    (Q0 >= 1) and (ii) it is NOT front-sourced (energy conserved, front off) — a
    dispersing-but-present defect is "present, not created". The persistence
    question (does the front HOLD it past τ_disperse) is the discriminator, not G1.
    PML defaults to 0 here so the lossless energy check is not confounded by PML
    absorption (Rule-10 PML-exclusion corollary).
    """
    sim = CoupledK4Cosserat(
        N=N, pml=pml,
        use_memristive_saturation=False,   # conservative: no memristive dissipation
        use_impedance_boundary=False,      # front OFF — no clamp, no drive
        disable_cosserat_lc_force=True,    # isolate: pure Cosserat evolution
        couple_v_sector=False,             # V-sector zeroed: no K4 energy input
    )
    seed_omega_defect(sim, **seed_kw)
    Q0 = sim.total_topological_charge()
    H0 = sim.total_hamiltonian()
    for _ in range(n_steps):
        sim.step()
    Q_short = sim.total_topological_charge()
    H1 = sim.total_hamiltonian()
    rel_drift = abs(H1 - H0) / max(abs(H0), 1e-30)
    return {
        "Q0": int(Q0),
        "Q_short": int(Q_short),
        "H0": float(H0),
        "H1": float(H1),
        "rel_drift": float(rel_drift),
        # G1 PASS: defect exists at seed AND is not front-sourced (energy
        # conserved over the short lossless window, front off).
        "passes_G1": bool(Q0 >= 1 and rel_drift <= 1e-2),
    }


def bare_dispersion_baseline(N: int = 24, pml: int = 3, n_steps: int = 30,
                             **seed_kw) -> dict:
    """Record how many Compton periods the seeded defect survives under LOSSLESS
    front-OFF evolution — the τ_disperse baseline the memristive arm must BEAT
    to count as a freeze (prereg §4 G3/G5). The defect naturally disperses; a
    freeze = holding Q past this baseline.
    """
    sim = CoupledK4Cosserat(
        N=N, pml=pml,
        use_memristive_saturation=False,
        use_impedance_boundary=False,
        disable_cosserat_lc_force=True,
        couple_v_sector=False,
    )
    seed_omega_defect(sim, **seed_kw)
    Q_pre = sim.total_topological_charge()
    T_compton = 2.0 * np.pi * C.TAU_RELAX_NATIVE
    dt = sim.outer_dt
    held = 0
    for _ in range(n_steps):
        if sim.total_topological_charge() >= Q_pre and Q_pre >= 1:
            held += 1
        else:
            break
        sim.step()
    return {
        "Q_pre": int(Q_pre),
        "tau_disperse_compton": float(held * dt / T_compton),
        "held_steps": int(held),
    }


# =====================================================================
# The moving-front orchestrator over CoupledK4Cosserat
# =====================================================================
@dataclass
class FreezeInResult:
    """Time-series + summary of one moving-front run."""

    arm: str
    cfg: FrontConfig
    Q_pre: int
    Q_series: list = field(default_factory=list)       # winding vs step
    x_front_series: list = field(default_factory=list)
    S_min_at_defect: list = field(default_factory=list)  # lagged S at defect site
    t_series: list = field(default_factory=list)
    # summary
    Q_end: int = 0
    persisted_compton: float = 0.0
    front_passed_defect: bool = False


class MovingFrontFreezeIn:
    """Orchestrates a moving yield-crossing front over CoupledK4Cosserat.

    Two arms (prereg §3 / Guard 2):
      arm="bare"  → use_memristive_saturation=False (control, must LOCK/heal)
      arm="memristive" → use_memristive_saturation=True + lagged front-clamp
                          (must FREEZE for fast v_front)

    The front is a moving down-crossing boundary imposed on the K4 strain field:
    V(x,t) sets r = V/V_SNAP = r_ahead ahead of x_front(t), r_behind behind it,
    with a smooth ramp of width ell_front. It is injected into k4.V_inc every
    outer step; the K4 relaxation ODE (k4_tlm.py:283) then lags S(t) behind
    S_eq(r) — the source of the fast→freeze asymmetry (prereg §2.3).
    """

    def __init__(self, cfg: FrontConfig, arm: str = "memristive", *,
                 seed_kw: dict | None = None):
        assert arm in ("bare", "memristive")
        self.cfg = cfg
        self.arm = arm
        self.sim = CoupledK4Cosserat(
            N=cfg.N, pml=cfg.pml,
            use_memristive_saturation=(arm == "memristive"),
            use_impedance_boundary=True,     # the ω node-clamp (front-gate) is ON
            disable_cosserat_lc_force=True,  # A28: avoid the runaway channel
            couple_v_sector=True,            # V-sector front drives the clamp
        )
        # Seed the PRE-EXISTING defect (Guard 1). Ring centred at grid centre,
        # matched to the extract_crossing_count detector geometry.
        self.seed_kw = dict(R_major=min(5.0, 0.35 * cfg.N), amp=0.6, sigma=2.0)
        if seed_kw:
            self.seed_kw.update(seed_kw)
        seed_omega_defect(self.sim, **self.seed_kw)
        self.Q_pre = self.sim.total_topological_charge()
        # Defect-ring y-band centre (grid centre); front sweeps +y over it.
        self._defect_y = (cfg.N - 1) / 2.0
        # Front-clamp override (memristive-lagged) install.
        if arm == "memristive":
            self._install_lagged_clamp()

    # -----------------------------------------------------------------
    # Moving V(x,t) yield-crossing front → k4.V_inc
    # -----------------------------------------------------------------
    def _x_front(self, t: float) -> float:
        cfg = self.cfg
        x0 = cfg.pml + cfg.x0_frac * (cfg.N - 2 * cfg.pml)
        return x0 + cfg.v_front * t

    def _impose_front(self, t: float) -> None:
        """Set k4.V_inc so the strain field r = V/V_SNAP realises the moving
        down-crossing: r_ahead (x>x_front, slipstream) → r_behind (x<x_front,
        solid) with a tanh ramp of width ell_front. Drives the FRONT sweeping
        along +y (the ring axis) so it passes over the seeded defect ring.
        """
        cfg = self.cfg
        k4 = self.sim.k4
        j = self.sim.cos._j.astype(float)   # sweep axis = y (defect ring axis)
        xf = self._x_front(t)
        # tanh down-crossing: ahead (j > xf) → r_ahead; behind (j < xf) → r_behind
        ramp = 0.5 * (1.0 + np.tanh((j - xf) / max(cfg.ell_front, 1e-6)))
        r_field = cfg.r_behind + (cfg.r_ahead - cfg.r_behind) * ramp
        V_mag = r_field * k4.V_SNAP
        # Distribute the scalar voltage magnitude evenly across the 4 ports so
        # |V_inc| = V_mag (the strain read in _update_z_local_field uses the
        # port-norm). Only on active sites.
        per_port = V_mag / 2.0   # sqrt(4)=2 → port-norm equals V_mag
        vinc = np.zeros_like(k4.V_inc)
        vinc[..., :] = per_port[..., None]
        vinc[~k4.mask_active] = 0.0
        k4.V_inc = vinc

    # -----------------------------------------------------------------
    # Memristive-lagged front-clamp (the NEW engine piece, prereg §3.1)
    # -----------------------------------------------------------------
    def _install_lagged_clamp(self) -> None:
        """Replace the front-clamp so the ω-block Ω₀(r) is keyed to the LAGGED
        S(t) (k4.S_field) rather than the instantaneous S_eq. This is what lets
        L_eff(S(t)) = Z_0/√S(t) carry the fast→freeze memory (prereg §2.3): on a
        fast crossing S(t) lags low → Z_eff stays large → Γ stays < 0 → the
        node-clamp stays ON through and beyond the geometric crossing → dω/dt
        blocked → FREEZE.

        The stock _freeze_clamp_omega0_shared builds Γ from _update_saturation_
        kernels (instantaneous). We monkeypatch the bound method on this instance
        only, reusing the same skin-smoothing + clamp-strength wiring.
        """
        sim = self.sim
        cos = sim.cos
        TETRA = _tetra_offsets()

        def lagged_clamp() -> np.ndarray:
            # Lagged S from the K4 memristive relaxation state (already updated
            # by _update_z_local_field at the top of step()).
            S_lag = np.clip(sim.k4.S_field, 1e-6, 1.0)
            Z_eff = 1.0 / np.sqrt(S_lag)            # Z_0 = 1 native
            gamma = (Z_eff - 1.0) / (Z_eff + 1.0)   # >0 as S<1 (μ-side short)
            # relu(+Γ): S<1 (saturated) → Γ>0 → clamp ON (block dω/dt).
            weight = np.maximum(0.0, gamma)
            for _ in range(sim.impedance_skin_smoothing):
                acc = weight.copy()
                for p in TETRA:
                    acc = acc + np.roll(weight, shift=(-p[0], -p[1], -p[2]),
                                        axis=(0, 1, 2))
                weight = acc / (1 + len(TETRA))
            weight = weight * cos.mask_alive.astype(weight.dtype)
            cos._clamp_weight = weight
            return np.sqrt((sim.impedance_clamp_strength / cos.I_omega)
                           * np.maximum(weight, 0.0))

        sim._freeze_clamp_omega0_shared = lagged_clamp  # type: ignore[method-assign]

    # -----------------------------------------------------------------
    # Run
    # -----------------------------------------------------------------
    def run(self) -> FreezeInResult:
        cfg = self.cfg
        res = FreezeInResult(arm=self.arm, cfg=cfg, Q_pre=self.Q_pre)
        # T_Compton ≈ 2π·τ_relax; outer_dt in native units.
        T_compton = 2.0 * np.pi * C.TAU_RELAX_NATIVE
        dt = self.sim.outer_dt
        n_post = int(np.ceil(cfg.n_post_compton * T_compton / max(dt, 1e-12)))
        # Front transit: only needs to CLEAR the defect ring + a margin (the
        # ring poloidal extent + a few cells), NOT sweep the whole grid. This
        # keeps the slow-front step count bounded — the post-window (persistence
        # observation AFTER the front cleared) is where the freeze/heal read
        # happens, and the front-clear margin fixes where that window starts.
        # (Rule-10 efficiency finding: sweeping to the far edge made slow fronts
        # intractable while adding no physics past clear+margin.)
        ring_extent = self.seed_kw.get("R_major", 5.0) + 3.0 * self.seed_kw.get("sigma", 2.0)
        y_clear = self._defect_y + ring_extent
        t_clear = (y_clear - self._x_front(0.0)) / max(cfg.v_front, 1e-12)
        n_front = int(np.ceil(t_clear / max(dt, 1e-12)))
        n_total = n_front + n_post

        t = 0.0
        for step_i in range(n_total):
            self._impose_front(t)
            self.sim.step()
            t = self.sim.time
            if step_i % cfg.record_every == 0:
                Q = self.sim.total_topological_charge()
                res.Q_series.append(int(Q))
                res.x_front_series.append(float(self._x_front(t)))
                res.t_series.append(float(t))
                # lagged S sampled at the defect ring band (front-passage probe).
                res.S_min_at_defect.append(self._S_at_defect())
            if self._x_front(t) >= self._defect_y and not res.front_passed_defect:
                res.front_passed_defect = True

        res.Q_end = self.sim.total_topological_charge()
        res.persisted_compton = self._persistence_compton(res, T_compton, dt)
        return res

    def _S_at_defect(self) -> float:
        """Min lagged S in the defect-ring y-band (front-passage/BEMF probe)."""
        S = self.sim.k4.S_field
        j = self.sim.cos._j
        band = np.abs(j.astype(float) - self._defect_y) <= 2.0
        alive = self.sim.k4.mask_active & band
        return float(S[alive].min()) if alive.any() else 1.0

    def _persistence_compton(self, res: FreezeInResult, T_compton: float,
                             dt: float) -> float:
        """How many Compton periods the defect held Q >= Q_pre AFTER the front
        cleared it (prereg §4 G3).

        Rule-10 robustness: extract_crossing_count is jittery on a dispersing
        field (flickers 0↔2). We read persistence via a rolling window: the
        defect counts as "held" at step i if the median Q over a 3-sample window
        centred on i is >= Q_pre. This suppresses single-sample dropouts without
        rescuing a genuinely-healed defect (a healed field's window-median → 0).
        PML-excluded winding read is intrinsic to extract_crossing_count (contour
        on the interior ring, well inside the PML).
        """
        Q = res.Q_series
        if not Q or res.Q_pre < 1:
            return 0.0
        cleared = [i for i, x in enumerate(res.x_front_series)
                   if x >= self._defect_y]
        if not cleared:
            return 0.0
        i0 = cleared[0]

        def win_med(i: int) -> float:
            lo, hi = max(0, i - 1), min(len(Q), i + 2)
            return float(np.median(Q[lo:hi]))

        held = 0
        for i in range(i0, len(Q)):
            if win_med(i) >= res.Q_pre:
                held += 1
            else:
                break
        return held * dt / T_compton


def _tetra_offsets():
    """Local import shim for the K4 tetrahedral neighbour offsets (skin smoothing
    reuse). Falls back to the 6-neighbour stencil if the symbol moves."""
    try:
        from ave.topological.k4_cosserat_coupling import TETRA_OFFSETS
        return TETRA_OFFSETS
    except Exception:  # pragma: no cover
        return [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
                (0, -1, 0), (0, 0, 1), (0, 0, -1)]
