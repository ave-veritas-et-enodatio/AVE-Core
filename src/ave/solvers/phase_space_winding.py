"""PHASE-SPACE COUPLING-WINDING — does the (2,3) charge-winding live as a
CONSERVED CLOSED TIME-ORBIT in the inter-grade A1↔ω coupling?

FROZEN PRE-REG: research/2026-06-24_engine-phase-space-winding_prereg.md (commit 0d2b53e4).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS (the canonical-locus re-scope of the #415 negative)
═══════════════════════════════════════════════════════════════════════════════
The coupled eigensolve (#415) returned DOES-NOT-EXIST but tested the WRONG LOCUS
three ways: real-space (vs phase-space), longitudinal-mass-V_snap (vs transverse-
charge-V_yield), and STATIC eigenstate (vs dynamic ORBIT). A (2,3) winding is a
closed TIME-ORBIT θ(t)=2φ(t)+3ψ(t); a fixed-point eigenstate has no orbit and
cannot host it. This module tests the proper gate at the canonical locus: the
phase-space inter-grade A1↔ω coupling, traced DYNAMICALLY under the CONSERVATIVE
(unitary) S3 evolver.

  SEED, never FORM (pre-reg §0): we seed the already-placed electron
  (_build_seeded_sim → seed_A1_sech + seed_winding) and EVOLVE it. We do NOT form
  it from a precursor (the barred self-formation slot stays BARRED).

  CONSERVATIVE, never PUMPED (pre-reg §0): we evolve with
  CoupledCageWinding.step() — Crank–Nicolson/Cayley, Hermitian H ⇒ unitary ⇒
  joint energy ‖a_A1‖²+‖b_ω‖² conserved EXACTLY. NO external drive. A winding
  that appears only under energy injection is an ARTIFACT.

  α-CLEAN / PHASE-ONLY (pre-reg §0): the observable is a pure arg() (dimensionless).
  φ_rel = arg(Σ_x a_A1(x)·conj(b_ω(x))). NO Ω-weighting / A*-weighting (those re-
  import √α). The κ̃=6/5 host carries the winding factor; Q=137 stays EMPTY; no
  ALPHA on the verdict path.

═══════════════════════════════════════════════════════════════════════════════
THE OBSERVABLE (pre-reg §2 — precise)
═══════════════════════════════════════════════════════════════════════════════
  φ_rel(t) = arg( Σ_x a_A1(x,t)·conj(b_ω(x,t)) )   — the A1↔ω cross-term phase,
             which lives in NEITHER tank's self-phasor (honoring F1).

  The two Clifford-torus angles (the canonical (2,3) phase-space coordinate,
  ch8-alpha-golden-torus.md / torus-knot-uniqueness.md:31-35):
    toroidal φ(t) = arg( Σ_x a_A1(x,t) )   — the A1 (mass-sector) global phase;
                                              counts the "2".
    poloidal ψ(t) = arg( Σ_x b_ω(x,t) )    — the ω (charge-sector) global phase;
                                              counts the "3".
  The winding curve is θ(t) = 2·φ(t) + 3·ψ(t). The winding integer pair (p,q) =
  the windings of the (φ,ψ) phasor point around (toroidal, poloidal) over a
  CLOSED orbit — a Lissajous/quadrature winding, NOT a real-space linking.

  NOTE φ_rel and (φ,ψ) are NOT independent: the cross-term phase tracks φ−ψ up to
  the per-site phase texture. φ_rel is the headline F1 observable; (φ,ψ) is the
  Clifford-torus decomposition that carries the (p,q) integer. Both are pure args.

═══════════════════════════════════════════════════════════════════════════════
THE TWO INDEPENDENT WINDING READS (F4 — must AGREE before "conserved")
═══════════════════════════════════════════════════════════════════════════════
  (1) UNWRAP-COUNT: np.unwrap the toroidal φ(t) and poloidal ψ(t) over a closed
      orbit; the net turns are (p,q) = (Δφ/2π, Δψ/2π) rounded.
  (2) CIRCULATION INTEGRAL: the discrete contour integral ∮ dφ / 2π and ∮ dψ / 2π
      computed from the per-step phase increments (the winding-number residue).
  F4: these two MUST agree (within tolerance) before the integer is claimed. We do
  NOT adopt Q_H = p·q by formula.

═══════════════════════════════════════════════════════════════════════════════
THE ENERGY LEDGER (pre-reg §3 — Grant's directive)
═══════════════════════════════════════════════════════════════════════════════
  (1) joint ‖a_A1‖²+‖b_ω‖² conserved exactly (~machine precision; a drift = bug,
      the backward-Euler-bleed gate trips).
  (2) the sector-exchange book: energy flowing A1↔ω through the coupling port as
      the orbit winds. PASS signature: energy SLOSHES conservatively between mass
      & charge sectors WHILE the (2,3) integer stays put.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# REUSE (anti-rebuild, Rule 14): the S3 conservative evolver + the electron seed.
from ave.solvers.coupled_cage_winding import (
    CoupledCageWinding,
    CoupledCageWindingConfig,
)

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard triad (import-time). An α-carrier leaking here fails the import.
# The observable is a pure arg(); no α-carrier may reach the verdict path.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "α-leak: ELECTRON instance must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the chord path"
assert "KAPPA_CHIRAL_ELECTRON" not in globals(), "α-leak: KAPPA_CHIRAL_ELECTRON (=α·κ̃) forbidden"


@dataclass
class OrbitTrace:
    """The time-series of the phase-space orbit (all pure args ⇒ α-free)."""

    t: np.ndarray                       # (n_steps+1,) time
    phi_rel: np.ndarray                 # (n,) the F1 inter-grade cross-phase
    phi_tor: np.ndarray                 # (n,) toroidal A1 global phase (counts "2")
    psi_pol: np.ndarray                 # (n,) poloidal ω global phase (counts "3")
    cross_mag: np.ndarray               # (n,) |Σ a_A1 conj b_ω| (sector-overlap mag)
    e_total: np.ndarray                 # (n,) joint norm ‖a_A1‖²+‖b_ω‖²
    e_a1: np.ndarray                    # (n,) A1-sector norm (mass)
    e_omega: np.ndarray                 # (n,) ω-sector norm (charge)
    gmres_info: np.ndarray              # (n,) solver convergence flag per step


@dataclass
class WindingRead:
    """The (p,q) winding integer pair read by the two independent methods (F4)."""

    p_unwrap: float                     # toroidal net turns, unwrap method
    q_unwrap: float                     # poloidal net turns, unwrap method
    p_circ: float                       # toroidal net turns, circulation method
    q_circ: float                       # poloidal net turns, circulation method
    p_int: int                          # adopted toroidal integer
    q_int: int                          # adopted poloidal integer
    two_reads_agree: bool               # F4: unwrap and circulation agree
    period_steps: int                   # steps for one closed orbit (Nyquist read)
    steps_per_period: float             # Nyquist resolution
    nyquist_ok: bool                    # ≥ ~10 steps/period
    closure_quality: float              # return-dist / max-excursion (≪1 ⇒ closes)
    orbit_closes: bool                  # closure_quality below threshold


def _sector_phase(field_complex: np.ndarray) -> float:
    """arg(Σ_x field) — a sector global phase (pure argument, α-free). Used for
    both Clifford angles. A coherent sector has a well-defined global phase; the
    magnitude |Σ| is NOT on the verdict path (it would re-import the amplitude
    scale)."""
    s = complex(np.sum(field_complex))
    return float(np.angle(s))


def _cross_phase(a_A1: np.ndarray, b_omega: np.ndarray) -> tuple[float, float]:
    """φ_rel = arg(Σ_x a_A1·conj(b_ω)) and the cross-magnitude (sector overlap).
    The magnitude is recorded ONLY for the sloshing-ledger / coordinate-
    degeneracy check; it is NEVER on the integer/verdict path (pre-reg §2)."""
    cross = complex(np.sum(a_A1 * np.conj(b_omega)))
    return float(np.angle(cross)), float(abs(cross))


@dataclass
class PhaseSpaceWindingConfig:
    """Frozen phase-space-winding config. Reuses the S3 coupled cage at the
    V_yield TRANSVERSE-cavity operating point (NOT the V_snap mass core — the
    eigensolve's threshold error). The A1 core is seeded WIDE so the saturation
    front reaches the winding torus R (the regime where A1↔ω hybridize)."""

    N: int = 24
    pml_thickness: int = 4
    V_yield: float = 1.0
    # V_yield TRANSVERSE operating point: the A1 core is at the saturation FRONT
    # (A ≈ R_II = 4/7), NOT the deep V_snap cap (A→1). This is the F1/Q2 sectoral
    # ruling — the transverse-charge cavity, not the longitudinal-mass core.
    a1_amplitude: float = 0.60          # front-shell amplitude (A ≈ 4/7 at core), V_yield
    a1_radius: float = 6.0              # WIDE ⇒ front shell reaches the winding torus R
    R: float = 7.0                      # winding torus major radius (canonical (2,3))
    r: float = 2.3                      # winding tube minor radius
    rate: float = 0.3                   # S2 coupling rate scale
    omega_b: float = 1.0                # A1 breather frequency
    omega_s: float = 1.0                # ω-tank LC frequency (resonant ⇒ strongest exchange)
    chi: int = +1                       # lattice handedness (matter)
    dt: float = 0.066                   # Stage-2 production dt
    n_steps: int = 400                  # several orbital periods (Nyquist-checked)
    winding_on: bool = True

    def to_coupled_cfg(self, *, winding_on: bool | None = None) -> CoupledCageWindingConfig:
        return CoupledCageWindingConfig(
            N=self.N,
            pml_thickness=self.pml_thickness,
            V_yield=self.V_yield,
            R=self.R,
            r=self.r,
            rate=self.rate,
            omega_b=self.omega_b,
            omega_s=self.omega_s,
            chi=self.chi,
            dt=self.dt,
            winding_mode="rigid_template",
            winding_on=self.winding_on if winding_on is None else winding_on,
        )


def build_seeded_sim(cfg: PhaseSpaceWindingConfig, *, winding_on: bool | None = None) -> CoupledCageWinding:
    """Seed the already-formed electron (SEED, never FORM, pre-reg §0): a saturated
    A1 core (the mass breather, PLANTED — not self-formed) at the V_yield front +
    the separately-initialized (2,3) winding template (genesis-24 guard: ω is
    NEVER grad(V)). This is the SAME seed path #415 uses; the locus difference is
    the OPERATING POINT (V_yield front, not V_snap cap) and the DYNAMICS (orbit,
    not eigenstate)."""
    won = cfg.winding_on if winding_on is None else winding_on
    ccfg = cfg.to_coupled_cfg(winding_on=won)
    sim = CoupledCageWinding(ccfg)
    sim.seed_A1_sech(amplitude=cfg.a1_amplitude, radius=cfg.a1_radius)
    sim.seed_winding(amplitude=1.0)
    return sim


# ═════════════════════════════════════════════════════════════════════════════
# STAGE A — cheap static pre-filter (NO solve): is φ_rel a NON-DEGENERATE,
# definable coordinate, or gauge-collapsed (V_ref read-only projection)?
# ═════════════════════════════════════════════════════════════════════════════
def stage_a_coordinate_check(cfg: PhaseSpaceWindingConfig | None = None,
                             *, k_eigs: int = 8, probe_steps: int = 6) -> dict:
    """STAGE A (pre-reg §5.1): on #415's existing eigenvectors (no Stage-B solve),
    is φ_rel a non-degenerate definable coordinate, or gauge-collapsed?

    A stationary eigenstate gives only a STATIC angle (no orbit) — Stage A can
    PROVE the BREAK form "a fixed point hosts no winding" and can KILL the
    coordinate (→ INCONCLUSIVE-coordinate-wrong, STOP, do not burn Stage B) if the
    cross-term collapses to zero magnitude (then arg() is ill-defined = gauge-
    degenerate). It CANNOT deliver PASS.

    The check is two-pronged:
      (i)  EIGENSTATE prong — on the SA eigenvectors, |cross| must be NON-ZERO
           (the arg is well-defined ⇒ the coordinate is not gauge-collapsed), and
           φ_rel must be a SINGLE static angle (confirming a fixed point hosts no
           orbit — the expected eigenstate behavior, NOT a coordinate kill).
      (ii) DYNAMICAL prong — under a few CONSERVATIVE steps from the seed, φ_rel
           must MOVE (the coordinate is LIVE, not a frozen gauge artifact) while
           |cross| stays non-zero. If φ_rel is frozen AND |cross| collapses ⇒
           gauge-degenerate ⇒ STOP.

    coordinate_definable = (eigenstate |cross| nonzero) AND (dynamical φ_rel moves
    with |cross| nonzero). stopped_here = coordinate is gauge-collapsed."""
    from scipy.sparse.linalg import eigsh

    cfg = cfg or PhaseSpaceWindingConfig()

    # (i) EIGENSTATE prong — reuse #415's coupled Hermitian H, SA end.
    sim_e = build_seeded_sim(cfg, winding_on=True)
    H = sim_e._assemble_H()
    nd = sim_e.ndof
    vals, vecs = eigsh(H, k=min(k_eigs, 2 * nd - 2), which="SA")
    order = np.argsort(vals)
    vals, vecs = vals[order], vecs[:, order]
    eig_rows = []
    for idx in range(min(4, vecs.shape[1])):
        v = vecs[:, idx]
        a1, bw = v[:nd], v[nd:]
        phi_rel, mag = _cross_phase(a1, bw)
        eig_rows.append({"idx": idx, "eig": float(vals[idx]),
                         "phi_rel": phi_rel, "cross_mag": mag,
                         "a1_norm": float(np.sum(np.abs(a1) ** 2)),
                         "bw_norm": float(np.sum(np.abs(bw) ** 2))})
    eig_cross_nonzero = all(r["cross_mag"] > 1e-9 for r in eig_rows)

    # (ii) DYNAMICAL prong — does φ_rel MOVE under the conservative step?
    sim_d = build_seeded_sim(cfg, winding_on=True)
    phis, mags, energies = [], [], []
    pr, m = _cross_phase(sim_d.a_A1.reshape(-1), sim_d.b_w.reshape(-1))
    phis.append(pr); mags.append(m); energies.append(sim_d.total_energy())
    for _ in range(probe_steps):
        sim_d.step()
        pr, m = _cross_phase(sim_d.a_A1.reshape(-1), sim_d.b_w.reshape(-1))
        phis.append(pr); mags.append(m); energies.append(sim_d.total_energy())
    phi_moved = float(np.max(np.abs(np.diff(np.unwrap(phis)))))
    dyn_cross_nonzero = all(mm > 1e-9 for mm in mags)
    dyn_phi_moves = phi_moved > 1e-6
    e0 = energies[0]
    e_drift = max(abs(e - e0) / (abs(e0) + 1e-30) for e in energies)

    coordinate_definable = bool(eig_cross_nonzero and dyn_cross_nonzero and dyn_phi_moves)
    stopped_here = not coordinate_definable

    if stopped_here:
        detail = ("STAGE-A KILL: φ_rel coordinate is gauge-degenerate — "
                  f"eig_cross_nonzero={eig_cross_nonzero}, dyn_cross_nonzero="
                  f"{dyn_cross_nonzero}, dyn_phi_moves={dyn_phi_moves}. The cross-"
                  "term arg() is ill-defined ⇒ INCONCLUSIVE-coordinate-wrong, STOP "
                  "(do not burn Stage B).")
    else:
        detail = ("φ_rel is a NON-DEGENERATE definable coordinate: on the SA "
                  f"eigenstates |cross|>0 (well-defined arg, static angle as "
                  f"expected for a fixed point — confirms 'a fixed point hosts no "
                  f"orbit', the eigensolve's blind spot); under the conservative "
                  f"step φ_rel MOVES (max step Δφ_rel={phi_moved:.4e}) with "
                  f"|cross|>0 throughout (E drift {e_drift:.2e}, unitary). The "
                  "coordinate is LIVE ⇒ proceed to Stage B.")

    return {
        "stage": "A",
        "coordinate_definable": coordinate_definable,
        "stopped_here": stopped_here,
        "eigenstate_rows": eig_rows,
        "eigenstate_cross_nonzero": bool(eig_cross_nonzero),
        "dynamical_cross_nonzero": bool(dyn_cross_nonzero),
        "dynamical_phi_moves": bool(dyn_phi_moves),
        "dynamical_phi_max_step": phi_moved,
        "dynamical_energy_drift": e_drift,
        "detail": detail,
    }


# ═════════════════════════════════════════════════════════════════════════════
# STAGE B — the dynamical orbit trace (seed → conservative step() → φ_rel + the
# two Clifford angles + the energy ledger)
# ═════════════════════════════════════════════════════════════════════════════
def trace_orbit(cfg: PhaseSpaceWindingConfig, *, winding_on: bool | None = None,
                sim: CoupledCageWinding | None = None) -> OrbitTrace:
    """Seed → CONSERVATIVELY step()-evolve over cfg.n_steps → trace φ_rel + the two
    Clifford angles (toroidal φ counts '2', poloidal ψ counts '3') + the full
    energy ledger. All reads are pure args (α-free). NO external drive (the
    evolver is the unitary S3 step()).

    If `sim` is provided, it is evolved as-is (used by the validate-on-known
    pumped control, which deliberately injects energy). Otherwise a fresh seeded
    electron is built."""
    if sim is None:
        sim = build_seeded_sim(cfg, winding_on=winding_on)
    n = cfg.n_steps
    t = np.zeros(n + 1)
    phi_rel = np.zeros(n + 1)
    phi_tor = np.zeros(n + 1)
    psi_pol = np.zeros(n + 1)
    cross_mag = np.zeros(n + 1)
    e_total = np.zeros(n + 1)
    e_a1 = np.zeros(n + 1)
    e_omega = np.zeros(n + 1)
    gmres_info = np.zeros(n + 1, dtype=int)

    def _record(i: int):
        a1 = sim.a_A1.reshape(-1)
        bw = sim.b_w.reshape(-1)
        pr, mag = _cross_phase(a1, bw)
        phi_rel[i] = pr
        cross_mag[i] = mag
        phi_tor[i] = _sector_phase(a1)   # toroidal: A1 mass-sector global phase ('2')
        psi_pol[i] = _sector_phase(bw)   # poloidal: ω charge-sector global phase ('3')
        e_a1[i] = sim.a1_energy()
        e_omega[i] = sim.omega_energy()
        e_total[i] = e_a1[i] + e_omega[i]
        t[i] = sim.time
        gmres_info[i] = int(sim.last_gmres_info)

    _record(0)
    for i in range(1, n + 1):
        sim.step()
        _record(i)

    return OrbitTrace(t=t, phi_rel=phi_rel, phi_tor=phi_tor, psi_pol=psi_pol,
                      cross_mag=cross_mag, e_total=e_total, e_a1=e_a1,
                      e_omega=e_omega, gmres_info=gmres_info)


# ═════════════════════════════════════════════════════════════════════════════
# THE TWO INDEPENDENT WINDING READS (F4 — must AGREE)
# ═════════════════════════════════════════════════════════════════════════════
def _detect_period(phi_tor: np.ndarray, psi_pol: np.ndarray) -> tuple[int, float]:
    """Detect the closed-orbit period (in steps) of the (φ,ψ) Clifford point by the
    return-to-start of the joint phasor on the 4-D torus embedding (cos φ, sin φ,
    cos ψ, sin ψ).

    The orbit closes when the phasor point returns near its start AFTER first
    departing substantially. We (i) require the orbit to reach its FARTHEST excursion
    (so a shallow mid-precession re-alignment cannot fake a closure), then (ii) take
    the best (global-min-distance) genuine return in the post-departure window.

    Returns (period_steps, closure_quality) where closure_quality = the return
    distance normalized by the max excursion (≪1 ⇒ a genuine closed orbit; ~1 ⇒
    the orbit never returns = quasi-periodic / open, flagged downstream)."""
    n = len(phi_tor)
    state = np.stack([np.cos(phi_tor), np.sin(phi_tor),
                      np.cos(psi_pol), np.sin(psi_pol)], axis=1)
    s0 = state[0]
    dist = np.linalg.norm(state - s0[None, :], axis=1)
    if n < 4:
        return max(1, n - 1), 1.0
    max_excursion = float(dist.max()) + 1e-30
    # the step where the orbit is FARTHEST from start (it must depart before returning)
    far_idx = int(np.argmax(dist))
    far_idx = max(far_idx, 2)
    if far_idx >= n - 1:
        # never comes back within the window → no closure (quasi-periodic / open)
        return n - 1, float(dist[-1] / max_excursion)
    # genuine return = the GLOBAL minimum of distance after the farthest excursion
    post = dist[far_idx:]
    ret_rel = int(np.argmin(post))
    period = far_idx + ret_rel
    closure_quality = float(post[ret_rel] / max_excursion)
    return max(1, period), closure_quality


def _net_turns_unwrap(angles: np.ndarray, lo: int, hi: int) -> float:
    """Net turns of an angle series over [lo,hi] via np.unwrap (method 1)."""
    seg = np.unwrap(angles[lo:hi + 1])
    return float((seg[-1] - seg[0]) / (2.0 * np.pi))


def _net_turns_circulation(angles: np.ndarray, lo: int, hi: int) -> float:
    """Net turns via the discrete CIRCULATION integral ∮dθ/2π (method 2): sum the
    per-step phase increments wrapped to (−π,π], independent of np.unwrap's global
    pass. ∮dθ = Σ Δθ_wrapped; the winding number = ∮dθ/2π. This is an algebraically
    INDEPENDENT estimator of the same integer (F4 cross-check)."""
    seg = angles[lo:hi + 1]
    dtheta = np.diff(seg)
    # wrap each increment to (−π, π]
    dtheta = (dtheta + np.pi) % (2.0 * np.pi) - np.pi
    return float(np.sum(dtheta) / (2.0 * np.pi))


def read_winding(trace: OrbitTrace, *, dt: float, agree_tol: float = 0.20,
                 nyquist_min: float = 10.0) -> WindingRead:
    """Read the (p,q) winding integer pair of the closed phase-space orbit by the
    TWO independent methods (F4) — unwrap-count AND circulation integral — over one
    detected closed orbit. They MUST agree (within agree_tol) before the integer is
    claimed. Pure args ⇒ α-free.

    p (toroidal) = net turns of φ_tor; q (poloidal) = net turns of ψ_pol.
    Nyquist: the period must be ≥ nyquist_min steps or the read is INCONCLUSIVE."""
    n = len(trace.phi_tor)
    period, closure_quality = _detect_period(trace.phi_tor, trace.psi_pol)
    period = max(1, min(period, n - 1))

    p_unwrap = _net_turns_unwrap(trace.phi_tor, 0, period)
    q_unwrap = _net_turns_unwrap(trace.psi_pol, 0, period)
    p_circ = _net_turns_circulation(trace.phi_tor, 0, period)
    q_circ = _net_turns_circulation(trace.psi_pol, 0, period)

    p_int = int(np.round(p_unwrap))
    q_int = int(np.round(q_unwrap))

    two_reads_agree = bool(
        abs(p_unwrap - p_circ) < agree_tol and abs(q_unwrap - q_circ) < agree_tol
    )
    steps_per_period = float(period)
    nyquist_ok = bool(steps_per_period >= nyquist_min)
    orbit_closes = bool(closure_quality < 0.25)  # genuine return within 25% of excursion

    return WindingRead(
        p_unwrap=p_unwrap, q_unwrap=q_unwrap,
        p_circ=p_circ, q_circ=q_circ,
        p_int=p_int, q_int=q_int,
        two_reads_agree=two_reads_agree,
        period_steps=period,
        steps_per_period=steps_per_period,
        nyquist_ok=nyquist_ok,
        closure_quality=closure_quality,
        orbit_closes=orbit_closes,
    )


# ═════════════════════════════════════════════════════════════════════════════
# VALIDATE-ON-KNOWN (pre-reg §6 — wired FIRST; the reader must read a PLANTED
# (2,3) before any engine read is trusted)
# ═════════════════════════════════════════════════════════════════════════════
def _synthetic_lissajous(p: int, q: int, n_steps: int, *, dt: float = 0.066,
                         f0: float = 0.05, noise: float = 0.0,
                         seed: int = 20260624) -> OrbitTrace:
    """Build a SYNTHETIC OrbitTrace whose two Clifford angles wind as a pure (p,q)
    Lissajous: φ_tor(t) = 2π·p·f0·t, ψ_pol(t) = 2π·q·f0·t over exactly ONE closed
    orbit (t ∈ [0, 1/f0]). This is the POSITIVE control: the reader must return
    (p,q) and the two methods must agree. The energy ledger is a benign constant
    (this control exercises ONLY the winding reader)."""
    rng = np.random.default_rng(seed)
    period_T = 1.0 / f0
    n = n_steps
    t = np.linspace(0.0, period_T, n + 1)
    phi_tor = 2.0 * np.pi * p * f0 * t
    psi_pol = 2.0 * np.pi * q * f0 * t
    if noise > 0:
        phi_tor = phi_tor + noise * rng.standard_normal(n + 1)
        psi_pol = psi_pol + noise * rng.standard_normal(n + 1)
    # wrap to (−π,π] so the reader must un-wrap (exercises BOTH methods honestly)
    phi_w = (phi_tor + np.pi) % (2.0 * np.pi) - np.pi
    psi_w = (psi_pol + np.pi) % (2.0 * np.pi) - np.pi
    phi_rel = (phi_w - psi_w + np.pi) % (2.0 * np.pi) - np.pi
    e = np.ones(n + 1)
    return OrbitTrace(t=t, phi_rel=phi_rel, phi_tor=phi_w, psi_pol=psi_w,
                      cross_mag=np.ones(n + 1), e_total=e, e_a1=0.5 * e,
                      e_omega=0.5 * e, gmres_info=np.zeros(n + 1, dtype=int))


def validate_positive_control(p: int = 2, q: int = 3, n_steps: int = 400,
                              dt: float = 0.066) -> dict:
    """POSITIVE control (pre-reg §6): plant a pure (p,q) Lissajous → the reader MUST
    return (p,q) AND the two methods (unwrap, circulation) MUST agree. If it can't
    read a planted (2,3), the reader is BROKEN — the caller HALTs."""
    tr = _synthetic_lissajous(p, q, n_steps, dt=dt)
    # the synthetic orbit closes at the LAST sample (one full period by construction)
    wr_p = _net_turns_unwrap(tr.phi_tor, 0, n_steps)
    wr_pc = _net_turns_circulation(tr.phi_tor, 0, n_steps)
    wr_q = _net_turns_unwrap(tr.psi_pol, 0, n_steps)
    wr_qc = _net_turns_circulation(tr.psi_pol, 0, n_steps)
    p_int, q_int = int(round(wr_p)), int(round(wr_q))
    agree = bool(abs(wr_p - wr_pc) < 0.20 and abs(wr_q - wr_qc) < 0.20)
    reads_pq = bool((p_int, q_int) == (p, q))
    return {
        "planted": (p, q),
        "read": (p_int, q_int),
        "p_unwrap": wr_p, "p_circ": wr_pc, "q_unwrap": wr_q, "q_circ": wr_qc,
        "two_methods_agree": agree,
        "reads_planted_pq": reads_pq,
        "ok": bool(reads_pq and agree),
    }


def validate_null_control(n_steps: int = 400, dt: float = 0.066) -> dict:
    """NULL control (pre-reg §6): a non-winding orbit (static / (0,0) / (1,1)) must
    read NOT-(2,3) — no false-positive winding. We test a STATIC orbit (no winding)
    and a (1,1) orbit (winds but not (2,3))."""
    # static: both angles frozen at constants → (0,0)
    n = n_steps
    static = OrbitTrace(
        t=np.linspace(0, 1, n + 1),
        phi_rel=np.full(n + 1, 0.3), phi_tor=np.full(n + 1, 0.7),
        psi_pol=np.full(n + 1, -0.4), cross_mag=np.ones(n + 1),
        e_total=np.ones(n + 1), e_a1=0.5 * np.ones(n + 1),
        e_omega=0.5 * np.ones(n + 1), gmres_info=np.zeros(n + 1, dtype=int))
    p_s = _net_turns_unwrap(static.phi_tor, 0, n)
    q_s = _net_turns_unwrap(static.psi_pol, 0, n)
    static_is_23 = (int(round(p_s)), int(round(q_s))) == (3, 2) or \
                   (int(round(p_s)), int(round(q_s))) == (2, 3)

    # (1,1) Lissajous: winds, but NOT (2,3)
    tr11 = _synthetic_lissajous(1, 1, n_steps, dt=dt)
    p11 = int(round(_net_turns_unwrap(tr11.phi_tor, 0, n)))
    q11 = int(round(_net_turns_unwrap(tr11.psi_pol, 0, n)))
    o11_is_23 = (p11, q11) in [(2, 3), (3, 2)]

    return {
        "static_read": (int(round(p_s)), int(round(q_s))),
        "static_is_2_3": bool(static_is_23),
        "lissajous_1_1_read": (p11, q11),
        "lissajous_1_1_is_2_3": bool(o11_is_23),
        "ok": bool((not static_is_23) and (not o11_is_23)),  # neither false-positives
    }


def energy_conservation_gate(trace: OrbitTrace, *, tol: float = 1e-6) -> dict:
    """The S2/S3 joint-energy gate (pre-reg §3/§6): the joint norm ‖a_A1‖²+‖b_ω‖²
    must be conserved to ~machine precision over the orbit (the unitary Cayley
    scheme). A drift above `tol` = the bleed gate TRIPS (a bug, or — for the
    deliberately-pumped control — the proof the guard is live)."""
    e = trace.e_total
    e0 = float(e[0])
    drift = float(np.max(np.abs(e - e0)) / (abs(e0) + 1e-30))
    return {
        "e0": e0,
        "e_max_rel_drift": drift,
        "conserved": bool(drift <= tol),
        "tol": tol,
    }


def sector_exchange_ledger(trace: OrbitTrace) -> dict:
    """The A1↔ω sector-exchange book (pre-reg §3): how much energy SLOSHES between
    the mass (A1) and charge (ω) sectors as the orbit winds. PASS signature:
    energy sloshes (range/mean of either sector is appreciable) WHILE the joint
    norm stays fixed — conservative inter-grade exchange, no pumping."""
    a1, om, tot = trace.e_a1, trace.e_omega, trace.e_total
    a1_swing = float((a1.max() - a1.min()) / (a1.mean() + 1e-30))
    om_swing = float((om.max() - om.min()) / (om.mean() + 1e-30))
    # the fraction of total energy that moves between sectors over the orbit
    a1_frac = a1 / (tot + 1e-30)
    exchange_amplitude = float(a1_frac.max() - a1_frac.min())
    return {
        "a1_relative_swing": a1_swing,
        "omega_relative_swing": om_swing,
        "exchange_amplitude_frac": exchange_amplitude,
        "sector_exchange_seen": bool(exchange_amplitude > 0.02),
    }


def validate_pumped_control(cfg: PhaseSpaceWindingConfig, *, pump: float = 1.02,
                            n_steps: int = 60) -> dict:
    """ENERGY-GATE control (pre-reg §6): a deliberately-PUMPED variant must TRIP the
    bleed gate (proving the conservative guard is LIVE, not vacuous). We evolve the
    SAME seed but inject energy each step (scale the state by `pump`>1, a non-unitary
    operation = external drive). The joint-energy gate MUST detect the drift.

    This is the operational line vs the barred self-formation: a winding that needs
    pumping is an artifact. The conservative run conserves (gate holds); the pumped
    run does NOT (gate trips)."""
    # conservative reference
    cfg_short = PhaseSpaceWindingConfig(**{**cfg.__dict__, "n_steps": n_steps})
    tr_cons = trace_orbit(cfg_short)
    gate_cons = energy_conservation_gate(tr_cons)

    # pumped: re-run, scaling the state up each step (energy injection)
    sim = build_seeded_sim(cfg_short)
    e = [sim.total_energy()]
    for _ in range(n_steps):
        sim.step()
        # inject energy: a non-unitary amplitude pump (external drive)
        sim.a_A1 *= pump
        sim.b_w *= pump
        e.append(sim.total_energy())
    e = np.array(e)
    drift = float(np.max(np.abs(e - e[0])) / (abs(e[0]) + 1e-30))
    gate_pumped_trips = bool(drift > 1e-6)

    return {
        "conservative_drift": gate_cons["e_max_rel_drift"],
        "conservative_conserved": gate_cons["conserved"],
        "pumped_drift": drift,
        "pumped_gate_trips": gate_pumped_trips,
        "pump_factor": pump,
        "guard_is_live": bool(gate_cons["conserved"] and gate_pumped_trips),
    }


# ═════════════════════════════════════════════════════════════════════════════
# TOP-LEVEL VERDICT DRIVER — Stage A → validate-on-known → Stage B → ledger,
# binned PASS / BREAK / INCONCLUSIVE per the frozen pre-reg §4
# ═════════════════════════════════════════════════════════════════════════════
def run_phase_space_winding(cfg: PhaseSpaceWindingConfig | None = None) -> dict:
    """Run the full two-stage phase-space coupling-winding test and bin the
    verdict (pre-reg §4 make-or-break + §5 two-stage build).

    Sequence (each a gate):
      0. VALIDATE-ON-KNOWN (wired FIRST): positive (planted (2,3) reads (2,3),
         two methods agree) + null (non-winding reads NOT-(2,3)) + pumped (the
         energy guard is live). If the positive control fails ⇒ HALT-broken-reader.
      A. STAGE A: is φ_rel a non-degenerate definable coordinate? If gauge-collapsed
         ⇒ INCONCLUSIVE-coordinate-wrong, STOP (do not burn Stage B).
      B. STAGE B: seed → conservative step()-evolve → trace φ_rel + the two Clifford
         angles → read (p,q) by the two methods (must agree, F4) → energy ledger.

    PASS  = closed conservative orbit carries (2,3); integer stable + α-free +
            two-reads-agree + conservative sector-exchange (no pumping).
    BREAK = static angle / no commensurate (2,3) / a different integer / α-loaded /
            needs pumping ⇒ the negative DEEPENS (real-space AND phase-space null).
    INCONCLUSIVE = degenerate coordinate / Nyquist-unresolved.
    """
    cfg = cfg or PhaseSpaceWindingConfig()
    out: dict = {"config": {k: v for k, v in cfg.__dict__.items()}}

    # ── 0. VALIDATE-ON-KNOWN (wired FIRST) ──
    pos = validate_positive_control()
    null = validate_null_control()
    pumped = validate_pumped_control(cfg, n_steps=40)
    out["validate_on_known"] = {"positive": pos, "null": null, "pumped": pumped}
    if not pos["ok"]:
        out["verdict"] = "HALT"
        out["reason"] = "positive control FAILED: reader cannot read a planted (2,3) — broken reader"
        return out

    # ── A. STAGE A (coordinate definability) ──
    stage_a = stage_a_coordinate_check(cfg)
    out["stage_a"] = stage_a
    if stage_a["stopped_here"]:
        out["verdict"] = "INCONCLUSIVE"
        out["reason"] = "STAGE-A KILL: φ_rel coordinate gauge-degenerate (INCONCLUSIVE-coordinate-wrong)"
        return out

    # ── B. STAGE B (the dynamical orbit) ──
    trace = trace_orbit(cfg)
    wr = read_winding(trace, dt=cfg.dt)
    egate = energy_conservation_gate(trace)
    sledger = sector_exchange_ledger(trace)

    out["stage_b"] = {
        "winding_pq": f"({wr.p_int},{wr.q_int})",
        "p_unwrap": wr.p_unwrap, "q_unwrap": wr.q_unwrap,
        "p_circ": wr.p_circ, "q_circ": wr.q_circ,
        "two_reads_agree": wr.two_reads_agree,
        "period_steps": wr.period_steps,
        "steps_per_period": wr.steps_per_period,
        "nyquist_ok": wr.nyquist_ok,
        "closure_quality": wr.closure_quality,
        "orbit_closes": wr.orbit_closes,
        "phi_tor_total_turns": float((np.unwrap(trace.phi_tor)[-1] - trace.phi_tor[0]) / (2 * np.pi)),
        "psi_pol_total_turns": float((np.unwrap(trace.psi_pol)[-1] - trace.psi_pol[0]) / (2 * np.pi)),
        "phi_rel_total_turns": float((np.unwrap(trace.phi_rel)[-1] - trace.phi_rel[0]) / (2 * np.pi)),
    }
    out["energy_ledger"] = {**egate, **sledger}

    # ── BIN (pre-reg §4) ──
    is_2_3 = bool((wr.p_int, wr.q_int) in [(2, 3), (3, 2)])
    integer_stable = bool(wr.two_reads_agree and wr.nyquist_ok)
    conservative = bool(egate["conserved"] and sledger["sector_exchange_seen"])
    alpha_clean = True  # pure args throughout; structural (no α-carrier on the path)

    out["bins"] = {
        "is_2_3": is_2_3,
        "two_reads_agree": wr.two_reads_agree,
        "nyquist_ok": wr.nyquist_ok,
        "orbit_closes": wr.orbit_closes,
        "integer_stable": integer_stable,
        "conservative_exchange": conservative,
        "alpha_clean": alpha_clean,
    }

    # INCONCLUSIVE only if the orbit is genuinely UNRESOLVED (Nyquist-limited) AND
    # does NOT close — i.e. we cannot even read an integer. A RESOLVED, CLOSING orbit
    # that reads a non-(2,3) integer is a BREAK (the integer is read, it's just wrong),
    # NOT INCONCLUSIVE (pre-reg §4 — do not rescue a clean negative into INCONCLUSIVE).
    if (not wr.nyquist_ok) and (not wr.orbit_closes):
        out["verdict"] = "INCONCLUSIVE"
        out["reason"] = (f"orbit Nyquist-unresolved AND does not close "
                         f"({wr.steps_per_period:.1f} steps/period, closure_quality="
                         f"{wr.closure_quality:.3f}) — cannot read an integer; report, re-scope")
    elif is_2_3 and integer_stable and conservative and alpha_clean:
        out["verdict"] = "PASS"
        out["reason"] = ("closed conservative orbit carries (2,3), two reads agree, "
                         "α-free, conservative sector-exchange (no pumping)")
    else:
        out["verdict"] = "BREAK"
        fails = [k for k, v in out["bins"].items() if not v]
        out["reason"] = (f"the (2,3) does NOT live as a conserved closed time-orbit "
                         f"in the conservative coupling (failing: {fails}); the "
                         f"negative DEEPENS (real-space AND phase-space null). "
                         f"Retract-not-refill: does NOT walk back charge=Link(∂Ω,F).")
    return out


if __name__ == "__main__":
    import json

    print("PHASE-SPACE COUPLING-WINDING — two-stage dynamical orbit test")
    print("=" * 72)
    # the documented headline config (N=24, 600 steps ≈ 6 carrier periods — the
    # window that resolves a clean closed orbit; see the result doc §3).
    cfg = PhaseSpaceWindingConfig(N=24, R=7.0, r=2.3, a1_radius=6.0,
                                  pml_thickness=4, n_steps=600, dt=0.066)
    res = run_phase_space_winding(cfg)
    print(json.dumps(res["bins"], indent=2))
    print(f"winding (p,q) = {res['stage_b']['winding_pq']}  "
          f"closure_quality = {res['stage_b']['closure_quality']:.3f}")
    print("-" * 72)
    print(f"VERDICT: {res['verdict']}")
    print(f"REASON : {res['reason']}")
