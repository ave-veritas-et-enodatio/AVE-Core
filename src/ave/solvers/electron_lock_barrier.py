"""ELECTRON-LOCK RECONNECTION-BARRIER TEST — does GENUINE confinement rescue the
(2,3) winding from being a carrier-ratio ECHO?

FROZEN PRE-REG: research/2026-07-08_electron-lock-barrier_prereg.md.

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS (the last-swing of the electron-lock effort)
═══════════════════════════════════════════════════════════════════════════════
The PINCER (both loci already read AGAINST Reading B, grep-confirmed):
  • REAL-SPACE winding HOLDS but is INERT (research/2026-06-24_engine-s1-winding-
    dof_result.md:25) — same arc's S3 is DISPERSE-FALSIFIED (research/2026-06-24_
    engine-s3-cavity-pinning_result.md:4,50): "even with the winding demonstrably
    conserved, the coupling does not pin the core."
  • PHASE-SPACE winding reads as the LC CARRIER FREQUENCY RATIO, not topology
    (#417 BREAK, research/2026-06-24_engine-phase-space-winding_result.md:29). The
    load-bearing discriminator was CARRIER-RATIO DETUNING: detune ω_b:ω_s and the
    "(2,3)" tracks CONTINUOUSLY (1:1→0.93, 2:3→0.65, 3:2→1.54, 1:2→0.48). A
    topological integer CANNOT slide; a carrier ratio does exactly that.
  • Production `coupled_cage_winding` `rigid_template` mode CANNOT unwind (frozen
    ê_w, conserved BY CONSTRUCTION); a "held" there is a data-structure artifact.

The ONE un-run version is the BARRIER: every prior run measured whether a LABEL
stayed constant; NONE measured whether there is an ENERGY BARRIER against a REAL
reconnection. Pre-test physics (walked with Grant, ruled): "a knot holds because
untying it COSTS energy, losslessly — not because a bookkeeping integer is
conserved."

═══════════════════════════════════════════════════════════════════════════════
THE ASSEMBLY (reuse, anti-rebuild Rule 14)
═══════════════════════════════════════════════════════════════════════════════
Evolve a reconnection-capable (FREE / dispersive-vector-class) director — so
unwinding is physically POSSIBLE — WITH a moving-Γ=−1 confinement wall ON.
ENERGY-CONSERVING integrator only (UNITARY Crank–Nicolson/Cayley), so NO
numerical damping can fake a hold (Ax3-lossless; "no damping fakes a pin"). Read
winding in PHASE-SPACE (the Clifford torus, where the claim lives and where #417
bit) AND in real-space (compute_Q_link, the reconnection observable).

  • Spine: `CoupledCageWinding` in `winding_mode="dispersive_vector"` — the free ω
    director that CAN reconnect (the honest arm; rigid_template is frozen-by-
    construction and is used ONLY as a PROTECTED-reachable bin-liveness control).
  • Wall: `ConfinedCageWinding` (below) adds the moving-Γ=−1 confinement wall as a
    HERMITIAN reactive on-site potential U_conf(x) = K·g(x) on the ω-block
    diagonal. This is the UNITARY-scheme faithful analog of
    `cosserat_field_3d.py`'s `use_impedance_boundary` reactive clamp
    V_clamp = ½K·relu(−Γ)·|ω|² (`cosserat_field_3d.py:1920`) — a LOSSLESS,
    energy-STORING reflective short keyed on the MOVING saturation front, NOT the
    singular bulk `_reflection_density` term (the genesis-24 detonation, CP10).
    Being a REAL diagonal it keeps the CN/Cayley propagator EXACTLY UNITARY ⇒
    joint energy conserved to GMRES tolerance (~1e-10) — the rigor guard.

  ⚑ HONEST FLAG (BC-not-bulk / substrate-native): the literal
    `CosseratField3D.use_impedance_boundary` is a velocity-Verlet clamp on a
    DIFFERENT field representation (the JAX Cosserat u/ω) and its Meissner Γ=−1
    comes from the asymmetric (S_μ,S_ε) split, which the scalar unitary spine does
    not carry. On the spine the wall is realized as the reactive Op17-bounded
    moving-front confinement POTENTIAL (the Hermitian analog of the V_clamp term),
    keyed on the ω-sector's own saturation front. This preserves the brief's HARD
    requirement — "energy-conserving integrator only (unitary)", which the
    velocity-Verlet hard-clamp CANNOT pass (its own docstring reports ~1e4–1e5×
    runaway at default dt). The correspondence is V_clamp; the μ/ε provenance is
    replaced by the |ω|-front proxy — stated, not smoothed.

═══════════════════════════════════════════════════════════════════════════════
α-CLEAN / PHASE-ONLY
═══════════════════════════════════════════════════════════════════════════════
The phase-space observable is a pure arg() (dimensionless). No ALPHA / Q_TANK /
V_SNAP / KAPPA_CHIRAL_ELECTRON on the verdict path. Constants may enter ONLY as
off-path scale anchors (the scale-invariance gate proves the α-echo magnitude in
V_yield does NOT reach the verdict). An AST firewall scan asserts no ALPHA/M_E
NAME token in any verdict-path function.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy import sparse

# REUSE (anti-rebuild, Rule 14): the S3 conservative unitary evolver + the α-free
# saturation-front gate + the electron seed; the real-space winding reader.
from ave.solvers.coupled_cage_winding import (
    CoupledCageWinding,
    CoupledCageWindingConfig,
    front_gate,
)
from ave.topological.charge_quantization import compute_Q_link

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard triad (import-time). An α-carrier leaking here fails the import.
# The verdict observable is a pure arg(); no α-carrier may reach the verdict path.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the chord path"
assert "M_E" not in globals(), "α-leak: M_E must NOT be on the verdict path"
assert "KAPPA_CHIRAL_ELECTRON" not in globals(), "α-leak: KAPPA_CHIRAL_ELECTRON forbidden"


# ═════════════════════════════════════════════════════════════════════════════
# THE WALL — the moving-Γ=−1 reactive confinement, as a Hermitian on-site
# potential on the unitary spine (keeps CN/Cayley EXACTLY unitary).
# ═════════════════════════════════════════════════════════════════════════════
class ConfinedCageWinding(CoupledCageWinding):
    """`CoupledCageWinding` + a moving-Γ=−1 reactive confinement wall.

    The wall is a Hermitian on-site potential U_conf(x) = clamp_strength·g(x) added
    to the ω-sector diagonal block, where g(x) is a MOVING saturation-front weight
    ∈ [0,1]. Because U_conf is a REAL diagonal, the generator H stays Hermitian ⇒
    the Crank–Nicolson/Cayley propagator stays EXACTLY UNITARY ⇒ the joint energy
    ‖a_A1‖²+‖ω‖² is conserved to GMRES tolerance. This is the unitary-scheme analog
    of `cosserat_field_3d.py:1920`'s reactive V_clamp = ½K·relu(−Γ)·|ω|² — a
    lossless, energy-storing reflective short, NOT damping (Ax3: no damping fakes a
    pin) and NOT the singular bulk `_reflection_density` term (BC-not-bulk).

    `wall_form` selects the moving-front weight g(x):
      • "off"          — U_conf ≡ 0 (the wall-OFF control; Arm 1 / negative bin).
      • "omega_front"  — g = front_gate(|ω|/ω_yield): a reflective SHELL at the
                         ω-sector saturation front (the μ-side short locus, where
                         the ω-photon focuses); drives ω→node there. DEFAULT.
      • "a1_front"     — g = front_gate(|a_A1|/V_yield): the A1-core saturation
                         front (the same R_II=4/7 shell the coupling port uses).
      • "seed_cavity"  — g = 1 − w_amp0/max(w_amp0): a STATIC reflective box around
                         the seeded winding torus (a strong-confinement stress arm).
    """

    def __init__(self, cfg: CoupledCageWindingConfig, *, clamp_strength: float = 0.0,
                 wall_form: str = "omega_front", omega_yield: float = 1.0):
        super().__init__(cfg)
        self.clamp_strength = float(clamp_strength)
        self.wall_form = str(wall_form)
        self.omega_yield = float(omega_yield)
        self._wmax = 1.0  # set by seed_winding

    def seed_winding(self, *, amplitude: float = 1.0):
        super().seed_winding(amplitude=amplitude)
        self._wmax = max(1e-9, float(self.w_amp0.max()))

    def _omega_amp(self) -> np.ndarray:
        """|ω|(x) from the evolving field (dispersive_vector: a_w; rigid: b_w·ê_w)."""
        if self.winding_mode == "rigid_template":
            return np.abs(self.b_w)
        return np.sqrt(np.sum(np.abs(self.a_w) ** 2, axis=-1))

    def wall_weight(self) -> np.ndarray:
        """g(x) ∈ [0,1] — the MOVING confinement-front weight (α-free; pure ratio)."""
        if self.wall_form == "off" or self.clamp_strength == 0.0:
            return np.zeros((self.N, self.N, self.N), dtype=np.float64)
        if self.wall_form == "omega_front":
            A_omega = self._omega_amp() / max(self._wmax, 1e-9)
            return front_gate(A_omega)
        if self.wall_form == "a1_front":
            return front_gate(self.strain())
        if self.wall_form == "seed_cavity":
            return 1.0 - (self.w_amp0 / max(self._wmax, 1e-9))
        raise ValueError(f"unknown wall_form '{self.wall_form}'")

    def _conf_diag(self) -> np.ndarray:
        """U_conf(x) = clamp_strength·g(x), flattened to the ω-block ordering."""
        return (self.clamp_strength * self.wall_weight()).reshape(self.ndof)

    def _assemble_H(self):
        """Parent H (native-Laplacian blocks + on-site A1↔ω coupling) + the reactive
        confinement potential on the ω-block diagonal. Real diagonal ⇒ Hermitian ⇒
        unitary ⇒ energy conserved exactly."""
        H = super()._assemble_H()
        if self.clamp_strength == 0.0 or self.wall_form == "off":
            return H
        nd = self.ndof
        U = self._conf_diag()
        if self.winding_mode == "rigid_template":
            full = np.concatenate([np.zeros(nd), U])
        else:  # dispersive_vector: 4·nd state, ω = blocks 1,2,3
            full = np.concatenate([np.zeros(nd), U, U, U])
        return (H + sparse.diags(full, format="csr")).tocsr()

    def wall_energy(self) -> float:
        """V_clamp = ½·clamp_strength·Σ g(x)·|ω(x)|² — the reactive wall storage (the
        energy the winding must pay INTO the wall). The unitary-scheme analog of
        `cosserat_field_3d.py:1944` (impedance_hamiltonian V_clamp)."""
        g = self.wall_weight()
        return 0.5 * self.clamp_strength * float(np.sum(g * self._omega_amp() ** 2))


# ═════════════════════════════════════════════════════════════════════════════
# THE READERS (phase-space Clifford torus + real-space winding) — all α-free
# ═════════════════════════════════════════════════════════════════════════════
def toroidal_phase(sim: CoupledCageWinding) -> float:
    """φ = arg(Σ_x a_A1) — the A1 (mass-sector) global phase; counts the "2".
    Pure argument ⇒ α-free."""
    return float(np.angle(complex(np.sum(sim.a_A1))))


def poloidal_phase(sim: CoupledCageWinding) -> float:
    """ψ — the ω (charge-sector) global phase along the winding template; counts
    the "3". dispersive_vector: arg(Σ_x ê_w·a_w) (the ω-sector projected onto the
    seeded template); rigid_template: arg(Σ_x b_ω). Pure argument ⇒ α-free."""
    if sim.winding_mode == "rigid_template":
        return float(np.angle(complex(np.sum(sim.b_w))))
    proj = np.sum(sim.e_w * sim.a_w, axis=-1)  # ê_w·a_w per site
    return float(np.angle(complex(np.sum(proj))))


def real_space_winding_raw(sim: CoupledCageWinding) -> float:
    """compute_Q_link fractional read on the reconnection-capable director
    Re(a_w) (dispersive_vector) or the |b_ω|·ê_w reconstruction (rigid). The
    FRACTIONAL Q_link_raw exposes partial/mid-slip winding (the reconnection
    observable)."""
    director = sim.omega_field()
    q = compute_Q_link(director, sim.cfg.R, sim.cfg.r)
    return float(q["Q_link_raw"])


def _net_turns(phase_series: list[float]) -> float:
    """Net turns of a wrapped phase series via np.unwrap (α-free)."""
    seg = np.unwrap(np.asarray(phase_series))
    return float((seg[-1] - seg[0]) / (2.0 * np.pi))


# ═════════════════════════════════════════════════════════════════════════════
# CONFIG + BUILD
# ═════════════════════════════════════════════════════════════════════════════
@dataclass
class BarrierConfig:
    """Frozen barrier-test config. Reuses the #417 V_yield transverse operating
    point (A1 core wide so the front reaches the winding torus R)."""

    N: int = 24
    pml_thickness: int = 4
    V_yield: float = 1.0            # scale anchor (scale-invariance gate doubles it)
    a1_amplitude: float = 0.60
    a1_radius: float = 6.0
    R: float = 7.0
    r: float = 2.3
    dt: float = 0.066
    n_steps: int = 300              # real-space arms (liveness/hold) window
    detune_steps: int = 200         # phase-space detuning-gate window (carrier ratio)
    qlink_stride: int = 10          # real-space Q_link checkpoint stride
    clamp_strength: float = 30.0    # the confinement-wall strength K
    wall_form: str = "omega_front"
    omega_b: float = 1.0
    omega_s: float = 1.0
    detune_pairs: tuple = ((1, 1), (2, 3), (3, 2), (1, 2))
    barrier_n_lambda: int = 21


def _coupled_cfg(bc: BarrierConfig, *, winding_mode: str, winding_on: bool,
                 omega_b: float | None = None, omega_s: float | None = None,
                 V_yield: float | None = None) -> CoupledCageWindingConfig:
    return CoupledCageWindingConfig(
        N=bc.N, pml_thickness=bc.pml_thickness,
        V_yield=bc.V_yield if V_yield is None else V_yield,
        R=bc.R, r=bc.r, dt=bc.dt,
        winding_mode=winding_mode, winding_on=winding_on,
        omega_b=bc.omega_b if omega_b is None else omega_b,
        omega_s=bc.omega_s if omega_s is None else omega_s,
    )


def build_sim(bc: BarrierConfig, *, wall_form: str, clamp_strength: float,
              winding_mode: str = "dispersive_vector", winding_on: bool = True,
              omega_b: float | None = None, omega_s: float | None = None,
              V_yield: float | None = None) -> ConfinedCageWinding:
    """Seed the already-formed electron (A1 sech mass + (2,3) winding template)
    with the confinement wall configured. SEED, never FORM."""
    ccfg = _coupled_cfg(bc, winding_mode=winding_mode, winding_on=winding_on,
                        omega_b=omega_b, omega_s=omega_s, V_yield=V_yield)
    Vy = bc.V_yield if V_yield is None else V_yield
    sim = ConfinedCageWinding(ccfg, clamp_strength=clamp_strength, wall_form=wall_form)
    # Scale the WHOLE seed (BOTH sectors) uniformly with V_yield: the strain
    # A=|a_A1|/V_yield (front geometry) AND the RELATIVE A1↔ω coupling are then
    # invariant, so the linear dynamics rescale uniformly and every arg() is
    # bitwise scale-invariant (the α-echo magnitude in V_yield divides out — the
    # scale-invariance gate's whole point).
    s = Vy / bc.V_yield
    sim.seed_A1_sech(amplitude=bc.a1_amplitude * s, radius=bc.a1_radius)
    sim.seed_winding(amplitude=s)
    return sim


# ═════════════════════════════════════════════════════════════════════════════
# EVOLVE + TRACE (one conservative run → phase-space phases, real-space winding,
# energy ledger)
# ═════════════════════════════════════════════════════════════════════════════
def evolve_and_trace(sim: ConfinedCageWinding, n_steps: int, *,
                     qlink_stride: int = 1) -> dict:
    """Conservatively step()-evolve; trace the two Clifford phases (every step, α-
    free), the joint norm (conservation gate), the reactive wall energy, and — when
    `qlink_stride` > 0 — the real-space Q_link_raw at a checkpoint stride (0, every
    stride, final). `qlink_stride == 0` ⇒ phase-only (the fast detuning-gate path;
    compute_Q_link is the per-step bottleneck)."""
    tor = [toroidal_phase(sim)]
    pol = [poloidal_phase(sim)]
    e_norm = [sim.total_energy()]
    v_clamp = [sim.wall_energy()]
    gmres = [int(sim.last_gmres_info)]
    do_rs = qlink_stride > 0
    raw = [real_space_winding_raw(sim)] if do_rs else []
    raw_steps = [0] if do_rs else []
    for n in range(1, n_steps + 1):
        sim.step()
        tor.append(toroidal_phase(sim))
        pol.append(poloidal_phase(sim))
        e_norm.append(sim.total_energy())
        v_clamp.append(sim.wall_energy())
        gmres.append(int(sim.last_gmres_info))
        if do_rs and (n % qlink_stride == 0 or n == n_steps):
            raw.append(real_space_winding_raw(sim))
            raw_steps.append(n)
    e0 = e_norm[0]
    h_drift = float(np.max(np.abs(np.asarray(e_norm) - e0)) / (abs(e0) + 1e-30))
    out = {
        "tor_phase": tor, "pol_phase": pol,
        "e_norm": e_norm, "v_clamp": v_clamp, "gmres": gmres,
        "tor_turns": _net_turns(tor), "pol_turns": _net_turns(pol),
        "h_drift": h_drift, "conserved": bool(h_drift < 1e-5),
    }
    if do_rs:
        out.update({
            "q_raw": raw, "q_raw_steps": raw_steps,
            "q_raw_0": raw[0], "q_raw_final": raw[-1],
            "q_raw_drop": float(abs(raw[0]) - abs(raw[-1])),
        })
    return out


# ═════════════════════════════════════════════════════════════════════════════
# BARRIER HOMOTOPY — the energy cost to force a partial unwind
# ═════════════════════════════════════════════════════════════════════════════
def _winding_homotopy_field(bc: BarrierConfig, lam: float) -> np.ndarray:
    """ω_λ(x): the (2,3) director with winding phase scaled by (1−λ). λ=0 ⇒ the
    fully-wound seed (byte-identical to seed_pq_winding(2,3)); λ=1 ⇒ θ≡0 (unwound,
    uniform director). Same torus geometry + K4 diamond mask as seed_pq_winding."""
    N, R, r = bc.N, bc.R, bc.r
    c = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    x, y, z = i - c, j - c, k - c
    rho = np.sqrt(x ** 2 + y ** 2)
    rtube = np.sqrt((rho - R) ** 2 + z ** 2)
    phi = np.arctan2(y, x)
    psi = np.arctan2(z, rho - R)
    r_opt = r if r > 0 else 1.0
    env = (np.sqrt(3.0) / 2.0) * np.pi / (1.0 + (rtube / r_opt) ** 2)
    theta = (1.0 - lam) * (2.0 * phi + 3.0 * psi)
    om = np.zeros((N, N, N, 3), dtype=np.float64)
    om[..., 0] = env * np.cos(theta)
    om[..., 1] = env * np.sin(theta)
    mask = ((i % 2 == 0) & (j % 2 == 0) & (k % 2 == 0)) | ((i % 2 == 1) & (j % 2 == 1) & (k % 2 == 1))
    return om * mask[..., None]


def _elastic_gradient_energy(sim: ConfinedCageWinding, omega_vec: np.ndarray) -> float:
    """E_grad(ω) = Σ_c ω_c† L_D ω_c — the native (K4) elastic gradient energy the
    winding stores on the FIXED confined-core stiffness D=1/S(A1_seed). Real SPD ⇒
    E_grad ≥ 0. This is the energy that a winding gradient costs; unwinding lowers
    it (∇θ→0) unless a barrier opposes."""
    from ave.solvers.native_cage_imex import assemble_L_D

    D = sim.stiffness_D().reshape(sim.ndof)
    L_D = assemble_L_D(sim.Grad, sim.Div, D)
    nd = sim.ndof
    E = 0.0
    for c in range(3):
        w = omega_vec[..., c].reshape(nd)
        E += float(w @ (L_D @ w))
    return E


def _wall_energy_of(sim: ConfinedCageWinding, omega_vec: np.ndarray,
                    extra_barrier: float = 0.0) -> float:
    """V_clamp = ½K Σ g(x)·|ω|² for a GIVEN director (the reactive wall storage).
    g keyed on the field's own |ω|-front (omega_front) or the static forms.
    `extra_barrier` injects a SYNTHETIC unwound-state penalty (bin-liveness only):
    a fictitious double-well that makes the unwound end higher-energy, proving the
    barrier-measure CAN report barrier>budget."""
    amp = np.sqrt(np.sum(omega_vec ** 2, axis=-1))
    if sim.wall_form == "omega_front":
        g = front_gate(amp / max(sim._wmax, 1e-9))
    elif sim.wall_form == "a1_front":
        g = front_gate(sim.strain())
    elif sim.wall_form == "seed_cavity":
        g = 1.0 - (sim.w_amp0 / max(sim._wmax, 1e-9))
    else:
        g = np.zeros_like(amp)
    return 0.5 * sim.clamp_strength * float(np.sum(g * amp ** 2)) + extra_barrier


def measure_barrier(bc: BarrierConfig, *, wall_form: str, clamp_strength: float,
                    budget: float, synthetic_barrier: float = 0.0) -> dict:
    """Arm 4: the adiabatic-homotopy barrier. Build ω_λ (fully-wound → unwound);
    at each λ compute H_conf(λ) = E_grad(ω_λ) + V_clamp(ω_λ); barrier = max_λ
    [H_conf(λ) − H_conf(0)]. protected = barrier > budget. `synthetic_barrier`
    (>0) injects a fictitious unwound-penalty (bin-liveness: PROTECTED reachable)."""
    sim = build_sim(bc, wall_form=wall_form, clamp_strength=clamp_strength)
    lams = np.linspace(0.0, 1.0, bc.barrier_n_lambda)
    H = []
    for lam in lams:
        om = _winding_homotopy_field(bc, float(lam))
        eg = _elastic_gradient_energy(sim, om)
        # synthetic penalty grows toward the unwound end (peaks at λ=1)
        vb = _wall_energy_of(sim, om, extra_barrier=synthetic_barrier * lam)
        H.append(eg + vb)
    H = np.asarray(H)
    barrier = float(np.max(H - H[0]))
    return {
        "lambda": lams.tolist(), "H_conf": H.tolist(),
        "H_wound": float(H[0]), "H_unwound": float(H[-1]),
        "barrier_height": barrier, "budget": float(budget),
        "barrier_gt_budget": bool(barrier > budget),
        "downhill": bool(H[-1] <= H[0]),
    }


# ═════════════════════════════════════════════════════════════════════════════
# THE FOUR ARMS
# ═════════════════════════════════════════════════════════════════════════════
def arm1_liveness(bc: BarrierConfig) -> dict:
    """Arm 1: free director, wall OFF, winding OFF, zero drive. MUST unwind (the
    reconnection channel is open) — else the test is VACUOUS ⇒ HALT."""
    sim = build_sim(bc, wall_form="off", clamp_strength=0.0, winding_on=False)
    tr = evolve_and_trace(sim, bc.n_steps, qlink_stride=bc.qlink_stride)
    tr["channel_open"] = bool(tr["q_raw_drop"] > 0.5)  # winding measurably unwinds
    tr["arm"] = "1_liveness"
    return tr


def arm2_hold(bc: BarrierConfig, arm1_drop: float) -> dict:
    """Arm 2: free director, wall ON, winding ON, zero drive, tuned to (2,3). Does
    the real-space (2,3) HOLD (unwind measurably LESS than Arm 1)?"""
    sim = build_sim(bc, wall_form=bc.wall_form, clamp_strength=bc.clamp_strength,
                    winding_on=True)
    tr = evolve_and_trace(sim, bc.n_steps, qlink_stride=bc.qlink_stride)
    # holds iff the confined winding retains substantially more than the free one
    tr["holds"] = bool(tr["q_raw_drop"] < 0.5 * max(arm1_drop, 1e-9))
    tr["integer_stable"] = bool(round(tr["q_raw_final"]) == round(tr["q_raw_0"]))
    tr["arm"] = "2_hold"
    # budget for the barrier = the natural reactive-wall fluctuation over the free
    # (unforced) conservative evolution — how much energy nature spontaneously
    # moves through the wall channel without any forced unwind.
    vc = np.asarray(tr["v_clamp"])
    tr["wall_fluctuation_budget"] = float(np.max(np.abs(vc - vc[0])))
    return tr


def classify_detuning(ratios: list[float], carrier_ratios: list[float]) -> dict:
    """The DECISIVE discriminator (#417): does the phase-space winding ratio TRACK
    the carrier ratio ω_b/ω_s (ECHO) or stay carrier-PINNED (TOPOLOGICAL)?

    PRIMARY metric = the Pearson CORRELATION between the winding ratio and the
    carrier ratio across the detuning sweep. This is MASQUERADE-PROOF: a strong
    confinement wall adds its OWN frequency to the ω-sector, which COMPRESSES the
    ratio SLOPE (shrinks ratio_spread) and could fool a spread-only test into a
    false "pin" — but it does NOT remove the carrier-DEPENDENCE (the ratio stays
    monotonic in ω_b/ω_s). Only a genuine topological lock makes the ratio
    carrier-INVARIANT (zero correlation). So:
      • corr > +0.7                        ⇒ "tracks"  (ECHO; carrier-dependent)
      • |corr| < 0.3 AND spread compressed ⇒ "pinned"  (TOPOLOGICAL candidate)
      • else                               ⇒ "ambiguous"
    Also reports the linear slope (ratio vs carrier) — an echo has positive slope
    even when the wall compresses it. Pure ratios of args ⇒ α-free."""
    r = np.asarray(ratios, dtype=float)
    cr = np.asarray(carrier_ratios, dtype=float)
    carrier_spread = float(cr.max() - cr.min())
    ratio_spread = float(r.max() - r.min())
    track_residual = float(np.mean(np.abs(r - cr)))
    if r.std() < 1e-12 or cr.std() < 1e-12:
        corr = 0.0
    else:
        corr = float(np.corrcoef(r, cr)[0, 1])
    slope = float(np.polyfit(cr, r, 1)[0]) if cr.std() > 1e-12 else 0.0
    tracks = bool(corr > 0.7)
    pinned = bool(abs(corr) < 0.3 and ratio_spread < 0.25 * carrier_spread)
    if tracks:
        verdict = "tracks"
    elif pinned:
        verdict = "pinned"
    else:
        verdict = "ambiguous"
    return {
        "ratios": [float(x) for x in r], "carrier_ratios": [float(x) for x in cr],
        "carrier_spread": carrier_spread, "ratio_spread": ratio_spread,
        "track_residual": track_residual, "correlation": corr, "slope": slope,
        "classification": verdict,
    }


def _detune_sweep(bc: BarrierConfig, *, winding_mode: str, clamp_strength: float,
                  wall_form: str, V_yield: float | None = None) -> tuple[list, dict]:
    """Sweep ω_b:ω_s; phase-only trace; ratio = tor_turns/pol_turns; classify."""
    rows = []
    for (ob, os_) in bc.detune_pairs:
        if winding_mode == "dispersive_vector":
            sim = build_sim(bc, wall_form=wall_form, clamp_strength=clamp_strength,
                            winding_on=True, omega_b=float(ob), omega_s=float(os_),
                            V_yield=V_yield)
        else:  # rigid_template — the clean #417 phase-space read (arg Σ b_ω)
            ccfg = _coupled_cfg(bc, winding_mode="rigid_template", winding_on=True,
                                omega_b=float(ob), omega_s=float(os_), V_yield=V_yield)
            Vy = bc.V_yield if V_yield is None else V_yield
            s = Vy / bc.V_yield
            sim = ConfinedCageWinding(ccfg, clamp_strength=clamp_strength, wall_form=wall_form)
            sim.seed_A1_sech(amplitude=bc.a1_amplitude * s, radius=bc.a1_radius)
            sim.seed_winding(amplitude=s)
        tr = evolve_and_trace(sim, bc.detune_steps, qlink_stride=0)
        ratio = tr["tor_turns"] / (tr["pol_turns"] + 1e-30)
        rows.append({"omega_b": ob, "omega_s": os_, "carrier_ratio": ob / os_,
                     "tor_turns": tr["tor_turns"], "pol_turns": tr["pol_turns"],
                     "winding_ratio": float(ratio), "h_drift": tr["h_drift"],
                     "conserved": tr["conserved"]})
    cls = classify_detuning([x["winding_ratio"] for x in rows],
                            [x["carrier_ratio"] for x in rows])
    return rows, cls


def arm3_detuning_killgate(bc: BarrierConfig) -> dict:
    """Arm 3 (DECISIVE): the phase-space carrier-ratio detuning kill-gate. Sweep
    ω_b:ω_s and read the Clifford winding ratio = tor_turns/pol_turns.

    PRIMARY = the reconnection-capable dispersive_vector director, wall ON (the
    brief's literal assembly). REFERENCE = the rigid_template clean #417 phase read
    (arg Σ b_ω) at wall ON AND wall OFF — the exact #417 comparison + confinement.
    The wall-ON-vs-OFF rigid contrast makes the decisive statement explicit: does
    the confinement wall convert the carrier-tracking (echo) into a topological
    pin? The classification is correlation-based (masquerade-proof)."""
    disp_rows, disp_cls = _detune_sweep(bc, winding_mode="dispersive_vector",
                                        clamp_strength=bc.clamp_strength, wall_form=bc.wall_form)
    rig_on_rows, rig_on_cls = _detune_sweep(bc, winding_mode="rigid_template",
                                            clamp_strength=bc.clamp_strength, wall_form=bc.wall_form)
    rig_off_rows, rig_off_cls = _detune_sweep(bc, winding_mode="rigid_template",
                                              clamp_strength=0.0, wall_form="off")
    return {
        "arm": "3_detuning_killgate",
        # the PRIMARY (reconnection-capable) verdict-deciding classification:
        "rows": disp_rows, **disp_cls,
        "primary_mode": "dispersive_vector (reconnection-capable), wall ON",
        "rigid_wall_on": {"rows": rig_on_rows, **rig_on_cls},
        "rigid_wall_off_reference": {"rows": rig_off_rows, **rig_off_cls},
        "all_conserved": bool(all(x["conserved"] for x in disp_rows + rig_on_rows + rig_off_rows)),
    }


# ═════════════════════════════════════════════════════════════════════════════
# DISCIPLINE GATES
# ═════════════════════════════════════════════════════════════════════════════
_VERDICT_PATH_FUNCS = (
    "toroidal_phase", "poloidal_phase", "real_space_winding_raw", "_net_turns",
    "evolve_and_trace", "classify_detuning", "_detune_sweep", "arm3_detuning_killgate",
    "measure_barrier", "_route_verdict", "run_electron_lock_barrier",
)


def firewall_ast_scan() -> dict:
    """AST-scan the verdict-path functions for any ALPHA/M_E/m_e NAME token — must
    be ABSENT (constants may enter only as off-path scale anchors)."""
    import ast
    import inspect
    import sys

    forbidden = {"ALPHA", "M_E", "m_e", "Q_TANK", "V_SNAP", "KAPPA_CHIRAL_ELECTRON"}
    mod = sys.modules[__name__]
    hits = []
    for name in _VERDICT_PATH_FUNCS:
        fn = getattr(mod, name)
        tree = ast.parse(inspect.getsource(fn))
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id in forbidden:
                hits.append(f"{name}:{node.id}")
            if isinstance(node, ast.Attribute) and node.attr in forbidden:
                hits.append(f"{name}:.{node.attr}")
    return {"clean": bool(not hits), "hits": hits, "scanned": list(_VERDICT_PATH_FUNCS)}


def scale_invariance_check(bc: BarrierConfig) -> dict:
    """The verdict must be identical at datasheet V_yield and at 2×V_yield (the
    α-echo magnitude in V_yield must NOT reach the verdict). The seed amplitude is
    scaled WITH V_yield so the strain A=|a_A1|/V_yield (hence the front geometry and
    all dynamics) is invariant — the verdict is set by the dimensionless strain
    profile, and V_yield's Volts DIVIDE OUT. We compare the Arm-3 detuning
    classification (reconnection-capable primary) at V_yield=1.0 and 2.0."""
    _, cls1 = _detune_sweep(bc, winding_mode="dispersive_vector",
                            clamp_strength=bc.clamp_strength, wall_form=bc.wall_form,
                            V_yield=bc.V_yield)
    _, cls2 = _detune_sweep(bc, winding_mode="dispersive_vector",
                            clamp_strength=bc.clamp_strength, wall_form=bc.wall_form,
                            V_yield=2.0 * bc.V_yield)
    return {"class_V": cls1["classification"], "corr_V": cls1["correlation"],
            "class_2V": cls2["classification"], "corr_2V": cls2["correlation"],
            "scale_invariant": bool(cls1["classification"] == cls2["classification"])}


def _route_verdict(detune_class: str, barrier_gt_budget: bool, arm2_holds: bool) -> str:
    """The pre-registered verdict routing (frozen prereg §3). Arm 3 is decisive."""
    if detune_class == "tracks":
        return "ECHO"
    if detune_class == "pinned" and barrier_gt_budget and arm2_holds:
        return "PROTECTED"
    return "NOT-PROTECTED"


def bin_liveness() -> dict:
    """Show each verdict bin is REACHABLE by the routing so the negative is
    informative (not a dead branch): synthetic per-arm inputs routing to
    PROTECTED, ECHO, NOT-PROTECTED."""
    return {
        "ECHO_reachable": bool(_route_verdict("tracks", False, False) == "ECHO"),
        "PROTECTED_reachable": bool(_route_verdict("pinned", True, True) == "PROTECTED"),
        "NOT_PROTECTED_reachable": bool(_route_verdict("pinned", False, False) == "NOT-PROTECTED"),
    }


def detuning_can_fire(bc: BarrierConfig) -> dict:
    """The gate CAN report 'tracks' (feed the frozen-template config #417 showed
    tracks) AND 'pinned' (a synthetic phase-locked config)."""
    # (i) frozen-template rigid config, wall OFF — #417 showed this TRACKS.
    _, tracks_cls = _detune_sweep(bc, winding_mode="rigid_template",
                                  clamp_strength=0.0, wall_form="off")
    # (ii) synthetic PINNED: winding ratio constant regardless of carrier.
    pinned_cls = classify_detuning([0.667] * len(bc.detune_pairs),
                                   [ob / os_ for (ob, os_) in bc.detune_pairs])
    return {
        "can_report_tracks": bool(tracks_cls["classification"] == "tracks"),
        "tracks_probe": tracks_cls,
        "can_report_pinned": bool(pinned_cls["classification"] == "pinned"),
        "pinned_probe": pinned_cls,
    }


# ═════════════════════════════════════════════════════════════════════════════
# TOP-LEVEL DRIVER
# ═════════════════════════════════════════════════════════════════════════════
def run_electron_lock_barrier(bc: BarrierConfig | None = None) -> dict:
    """Run the full reconnection-barrier test and route the verdict per the frozen
    prereg §3: [PROTECTED] / [ECHO] / [NOT-PROTECTED] (or HALT/INCONCLUSIVE)."""
    bc = bc or BarrierConfig()
    out: dict = {"config": {k: v for k, v in bc.__dict__.items()}}

    # ── Arm 1: liveness (channel open?) ──
    a1 = arm1_liveness(bc)
    out["arm1_liveness"] = a1
    if not a1["channel_open"]:
        out["verdict"] = "HALT"
        out["reason"] = ("Arm 1 liveness FAILED: the reconnection channel does not open "
                         f"(q_raw_drop={a1['q_raw_drop']:.3f} ≤ 0.5) — the test is VACUOUS.")
        return out
    if not a1["conserved"]:
        out["verdict"] = "INCONCLUSIVE"
        out["reason"] = f"Arm 1 energy leak: H-drift={a1['h_drift']:.2e} ≥ 1e-5 (numerics, not physics)."
        return out

    # ── Arm 2: hold? ──
    a2 = arm2_hold(bc, a1["q_raw_drop"])
    out["arm2_hold"] = a2

    # ── Arm 3: the DECISIVE detuning kill-gate ──
    a3 = arm3_detuning_killgate(bc)
    out["arm3_detuning_killgate"] = a3

    # ── Arm 4: barrier (budget = Arm-2 free wall-fluctuation) ──
    a4 = measure_barrier(bc, wall_form=bc.wall_form, clamp_strength=bc.clamp_strength,
                         budget=a2["wall_fluctuation_budget"])
    out["arm4_barrier"] = a4

    # ── discipline gates ──
    out["gates"] = {
        "firewall": firewall_ast_scan(),
        "scale_invariance": scale_invariance_check(bc),
        "bin_liveness": bin_liveness(),
        "detuning_can_fire": detuning_can_fire(bc),
        "energy_conservation": {
            "arm1_h_drift": a1["h_drift"], "arm2_h_drift": a2["h_drift"],
            "arm3_all_conserved": a3["all_conserved"],
            "all_below_1e-5": bool(a1["conserved"] and a2["conserved"] and a3["all_conserved"]),
        },
        "bc_not_bulk": {
            "wall": "Op17-bounded moving-front reactive V_clamp analog (Hermitian on-site potential)",
            "not_bulk_reflection_density": True,
            "wall_form": bc.wall_form,
        },
        "phase_space_locus": {"reader": "arg(Σ ê_w·a_w) poloidal + arg(Σ a_A1) toroidal — Clifford torus"},
    }

    # ── route the verdict (Arm 3 decisive) ──
    verdict = _route_verdict(a3["classification"], a4["barrier_gt_budget"], a2["holds"])
    out["verdict"] = verdict

    # surface any real-space / phase-space locus DISAGREEMENT (flag-don't-fix)
    locus_disagree = bool(a2["holds"] and a3["classification"] == "tracks")
    out["locus_disagreement"] = locus_disagree

    if verdict == "ECHO":
        out["reason"] = (
            "Arm 3 detuning TRACKS the carrier ratio ω_b:ω_s "
            f"(ratios {[round(x['winding_ratio'],3) for x in a3['rows']]} vs carrier "
            f"{[round(x['carrier_ratio'],3) for x in a3['rows']]}) — #417 confirmed on a "
            "harder test. Confinement does NOT rescue the topology; the phase-space "
            "(2,3) is the LC carrier ratio. Reading B closes NEGATIVE. Per Rule 12 this "
            "RETRACTS to 'confinement installs no reconnection barrier' — it does NOT walk "
            "back charge=Link(∂Ω,F) nor mass=A1 (#260).")
    elif verdict == "PROTECTED":
        out["reason"] = (
            "Arm 3 detuning-INVARIANT (pinned) AND Arm 4 barrier>budget AND Arm 2 holds "
            "— confinement installs a lossless topological barrier; the electron holds "
            "because untying costs energy. Reading B survives the last swing.")
    else:  # NOT-PROTECTED
        fails = []
        if a3["classification"] != "pinned":
            fails.append(f"detuning={a3['classification']}")
        if not a4["barrier_gt_budget"]:
            fails.append(f"barrier({a4['barrier_height']:.3g})≤budget({a4['budget']:.3g})")
        if not a2["holds"]:
            fails.append(f"Arm2 disperses like Arm1 (drop {a2['q_raw_drop']:.2f} vs {a1['q_raw_drop']:.2f})")
        out["reason"] = ("confinement protects neither the winding nor installs a barrier "
                         f"(failing: {fails}); Reading B closes NEGATIVE. Retract-not-refill.")
    return out


if __name__ == "__main__":
    import json

    print("ELECTRON-LOCK RECONNECTION-BARRIER TEST")
    print("=" * 72)
    res = run_electron_lock_barrier(BarrierConfig())
    print(f"VERDICT: {res['verdict']}")
    print(f"REASON : {res['reason']}")
