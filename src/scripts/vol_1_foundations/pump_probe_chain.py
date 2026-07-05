"""HONEST NONLINEAR DYNAMICS MODULE — 2-DOF pump-probe chain.

POST-REVIEW STATUS (orchestrator review of PR #532, 2026-07-05): the pump adjudication
is INVALID — the measured tangent-stiffness observable is LAB-FRAME (it feels the axial
spring through the bond slope, a kinematic tilt term neither frozen bond-frame arm
modeled). Proven: `LinearChain` (no kernel, no Jensen) reproduces the pump verdict to
~2e-6, and `cycle_mean_config_stiffness` reads COLD at the cycle-mean config. So NO
bond-frame arm is excluded/confirmed; the #526 T-slot fork REMAINS OPEN. What survives
(the real product): the BOND-FRAME instrument-liveness control (uniform stretch reads
k_s+T/L to 6 digits), the kinematic-tilt characterization (`tilt_decomposition`), and
the boundary-artifact documentation (`cycle_mean_config_stiffness(free_drive_end=...)`).
See `research/2026-07-05_pump-probe-tslot_result.md` §HONEST RE-ANALYSIS + §REQUIREMENTS.

The module ran the FULL NONLINEAR DYNAMICS of a 2-DOF-per-node chain (NO slot bookkeeping;
the dynamics respond however the geometry+kernel dictate); the failure was in the READOUT
(lab-frame vs bond-frame), not the integration.

THE #531 TAUTOLOGY GUARD (binding): this module MUST NOT import
`pump_probe_predictions.py` (the slot-formula prediction module). The probe stiffness
is measured from the time-domain response ONLY. The #528 ReconcileGate compares this
module's measured output against the prediction module's frozen arms.

Construction (FROZEN prereg 2026-07-05_pump-probe-tslot_prereg_FROZEN.md):
  - N-node chain, 2 DOF/node: longitudinal u_i, transverse y_i, rest spacing a0=1.
  - Bond length L_i = √((a0 + u_{i+1} − u_i)² + (y_{i+1} − y_i)²)  ← the ONLY
    transverse↔axial coupling source (NOT a T/ℓ term inserted by hand).
  - Axial constitutive law = canonical kernel potential Φ, Φ''(a)=k0√(1−a²),
    Φ'(A)=k0(A√(1−A²)+arcsin A)/2 (integrate once).
  - H = Σ ½ m(u̇²+ẏ²) + Σ_bond Φ(A_bond); transverse stiffness inherited ENTIRELY
    from Φ through the geometry.
  - Symplectic velocity-Verlet integration; absorbing boundaries; SWR measured.
  - Slow weak transverse probe measures effective transverse stiffness / phase
    velocity in the measurement window.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# ── kernel-unit conventions (same as #526/#529/#531) ─────────────────────────
K0 = 1.0
ELL = 1.0     # rest bond spacing a0
K_A = 1.0     # axial spring scale (kernel units)
K_S = 1.0     # transverse (shear soft) spring scale


# ── the canonical kernel (the dynamics own their kernel; NOT imported) ───────
def bond_tension(amplitude):
    """Φ'(A) = k0·(A√(1−A²)+arcsin A)/2 — the canonical kernel potential's first
    derivative. Independent re-impl (NOT imported from the prediction module)."""
    a = np.asarray(amplitude, dtype=float)
    return K0 * (a * np.sqrt(np.clip(1.0 - a**2, 0.0, 1.0)) + np.arcsin(np.clip(a, -1.0, 1.0))) / 2.0


def _saturation(strain):
    """S(A) = √(1 − A²) — the Ax4 kernel (A_yield = 1 in kernel units). The ONLY
    nonlinearity; keyed here on the LOCAL transverse strain of the shear channel."""
    a = np.asarray(strain, dtype=float)
    return np.sqrt(np.clip(1.0 - a**2, 0.0, 1.0))


def kernel_potential(amplitude):
    """Φ(A) = ∫₀^A Φ'(s) ds — the axial constitutive energy (Φ(0)=Φ'(0)=0).
    Closed form of the double integral of k0√(1−a²):
        Φ(A) = k0/4·[ A²·arcsin(A)/? ]  — done by parts, but the DYNAMICS never need
    Φ itself (only its A-gradient Φ'). Provided for the energy diagnostic via a
    per-bond quadrature (stable, avoids a second closed-form derivation)."""
    a = np.atleast_1d(np.asarray(amplitude, dtype=float))
    out = np.empty_like(a)
    # Φ(A) = ∫₀^A Φ'(s) ds; Φ' is smooth on [-1,1]; use fixed Gauss-Legendre.
    xg, wg = np.polynomial.legendre.leggauss(24)
    for i, Ai in enumerate(a.ravel()):
        s = 0.5 * Ai * (xg + 1.0)      # map [-1,1] → [0, Ai]
        out.ravel()[i] = 0.5 * Ai * np.sum(wg * bond_tension(s))
    return out.reshape(a.shape) if out.shape else float(out)


# ── the honest chain ─────────────────────────────────────────────────────────
@dataclass
class ChainState:
    u: np.ndarray
    y: np.ndarray
    vu: np.ndarray
    vy: np.ndarray


class PumpProbeChain:
    """2-DOF-per-node nonlinear chain with symplectic integration + absorbing ends.

    Nodes 0..N-1 along x. Bonds i = (i, i+1). Node 0 is the DRIVE (Dirichlet, set by
    the pump/probe drivers); the far end optionally has a damped sponge so waves
    absorb (traveling-wave regime) rather than reflect (standing-wave regime).
    """

    def __init__(self, n_nodes: int, mass: float = 1.0, sponge_width: int = 0,
                 sponge_gamma: float = 0.0, shear_saturates: bool = True):
        self.n = int(n_nodes)
        self.m = float(mass)
        self.sponge_width = int(sponge_width)
        self.sponge_gamma = float(sponge_gamma)
        # KEYING FORK (surfaced to Grant): does a transverse displacement wave strain
        # the shear channel (softening k_s·S(A_shear), keying A / True) or leave it
        # unstrained (k_s constant, keying B / False)? The verdict is sensitive to this;
        # BOTH run through the identical pipeline (KEEP-BOTH). See the result doc.
        self.shear_saturates = bool(shear_saturates)
        # per-node damping profile: 0 in the interior, ramps up in the far sponge.
        self.gamma = np.zeros(self.n)
        if self.sponge_width > 0 and self.sponge_gamma > 0:
            k = np.arange(self.sponge_width)
            ramp = self.sponge_gamma * (k / max(self.sponge_width - 1, 1)) ** 2
            self.gamma[self.n - self.sponge_width:] = ramp

    def bond_lengths(self, u, y):
        """L_i = √((a0 + Δu)² + Δy²) for every bond — the honest coupling source."""
        du = u[1:] - u[:-1]
        dy = y[1:] - y[:-1]
        dx = ELL + du
        L = np.sqrt(dx * dx + dy * dy)
        return L, dx, dy

    def forces(self, u, y):
        """Per-node (F_u, F_y) — the honest srs bond force, matching the CANONICAL
        force-constant matrix Φ_bond = k_a·(d̂⊗d̂) + [k_s + T/ℓ]·(I−d̂⊗d̂)
        (`prestress_elastic_tensor.py:124`), realized as time-domain forces:

          (1) AXIAL bond force: tension T = Φ'(A_bond) along the bond, A_bond = L−a0.
              Its transverse component T·(Δy/L) is the STRING-TENSION term — it emerges
              from the bond-length geometry, NOT inserted by hand. Zero at cold (T=0).
          (2) SHEAR spring (the k_s·(I−P) block, the COLD transverse restoring
              stiffness): a saturating transverse bending spring resisting the discrete
              transverse curvature. Its stiffness is k_s·S(A_shear) with S the Ax4
              kernel keyed on the LOCAL transverse strain — so whether the pump shifts
              it is decided by the DYNAMICS, not a slot rule.

        The COLD baseline transverse stiffness a probe feels is exactly k_s (the shear
        spring at zero strain); the string-tension term ADDS on top under load. This is
        the #526 form `k_shear_eff = k_s·S(A_shear) + T/ℓ` realized dynamically."""
        L, dx, dy = self.bond_lengths(u, y)
        A = L - ELL
        T = bond_tension(A)             # scalar axial tension per bond, Φ'(A)
        ux = dx / L
        uy = dy / L
        Fu = np.zeros(self.n)
        Fy = np.zeros(self.n)
        # (1) axial bond force (string-tension coupling emerges here)
        Fu[:-1] += T * ux
        Fy[:-1] += T * uy
        Fu[1:] -= T * ux
        Fy[1:] -= T * uy
        # (2) saturating shear spring: transverse bending force = −k_s·S(A_shear)·(curv)
        #     discrete curvature at interior node i: c_i = y[i-1] − 2 y[i] + y[i+1]
        #     (the (I−P) transverse restoring block; a real cold shear stiffness).
        curv = y[:-2] - 2.0 * y[1:-1] + y[2:]           # length n-2, for nodes 1..n-2
        # local transverse strain keying the saturation: the bond-angle |Δy|/L
        # averaged over the two bonds meeting at node i (Ax4 kernel, emergent).
        if self.shear_saturates:
            # KEYING A. MAJOR-b (orchestrator review PR #532): as coded this force is
            # NON-HAMILTONIAN — the position-dependent stiffness k_s·S(A_shear)·curv is
            # NOT the gradient of any potential (∂F_i/∂y_j ≠ ∂F_j/∂y_i), so it violates
            # Ax3-lossless in the bulk. It is a PHYSICS-INVALID arm and is flagged as
            # such; a valid saturating shear arm must derive the force from a potential
            # ½Σ k_s·∫S dy². The review notes keying B (Hamiltonian) is canon-favored.
            shear_strain = 0.5 * (np.abs(dy[:-1]) / L[:-1] + np.abs(dy[1:]) / L[1:])
            k_shear_local = K_S * _saturation(shear_strain)  # k_s·S(A_shear), keying A
        else:
            k_shear_local = K_S                              # k_s constant, keying B (Hamiltonian)
        Fy[1:-1] += k_shear_local * curv                 # restoring: −k·(−curv) form
        return Fu, Fy

    def step_verlet(self, state: ChainState, dt: float, drive=None, t=0.0):
        """One symplectic velocity-Verlet step. `drive(t)` may set node-0 (u,y)
        Dirichlet (returns (u0, y0) or None). Sponge damping (if any) applied as a
        velocity-Verlet-consistent drag in the far layer."""
        u, y, vu, vy = state.u, state.y, state.vu, state.vy
        Fu, Fy = self.forces(u, y)
        au = Fu / self.m - self.gamma * vu
        ay = Fy / self.m - self.gamma * vy
        # half-kick, drift, recompute, half-kick
        vu_half = vu + 0.5 * dt * au
        vy_half = vy + 0.5 * dt * ay
        u_new = u + dt * vu_half
        y_new = y + dt * vy_half
        if drive is not None:
            d = drive(t + dt)
            if d is not None:
                u0, y0 = d
                u_new[0] = u0
                y_new[0] = y0
        Fu2, Fy2 = self.forces(u_new, y_new)
        au2 = Fu2 / self.m - self.gamma * vu_half
        ay2 = Fy2 / self.m - self.gamma * vy_half
        vu_new = vu_half + 0.5 * dt * au2
        vy_new = vy_half + 0.5 * dt * ay2
        if drive is not None and d is not None:
            # node-0 velocity follows the drive derivative (kept consistent, not free)
            vu_new[0] = (u_new[0] - u[0]) / dt
            vy_new[0] = (y_new[0] - y[0]) / dt
        return ChainState(u_new, y_new, vu_new, vy_new)

    def energy(self, state: ChainState) -> float:
        """H = Σ ½ m(vu²+vy²) + Σ_bond Φ(A_bond) + shear-spring energy.
        (The shear-spring energy uses the linear ½k_s(Δy)² form; the saturation is a
        stiffness modulation, and for the drift diagnostic the linear energy is a
        stable proxy — the drift gate is applied to the UNDRIVEN closed chain where
        the saturation shift over the window is negligible.)"""
        L, _, dy = self.bond_lengths(state.u, state.y)
        A = L - ELL
        kinetic = 0.5 * self.m * np.sum(state.vu**2 + state.vy**2)
        potential = float(np.sum(kernel_potential(A)))
        shear = 0.5 * K_S * float(np.sum(dy**2))
        return float(kinetic + potential + shear)

    # ── SWR measurement (hidden-reflection guard) ────────────────────────────
    def measure_swr(self, y_amp_profile: np.ndarray, i0: int, i1: int) -> float:
        """Standing-wave ratio in [i0,i1): max transverse amplitude / min amplitude
        of the spatial envelope. SWR≈1 ⟹ traveling; SWR≫1 ⟹ reflection contamination."""
        env = np.abs(y_amp_profile[i0:i1])
        env = env[env > 1e-14]
        if env.size == 0:
            return float("nan")
        return float(np.max(env) / np.max([np.min(env), 1e-14]))

    # ── THE CONSUMED OBSERVABLE: effective transverse stiffness a slow probe sees
    def transverse_tangent_stiffness(self, u, y, node: int, delta: float = 1e-6) -> float:
        """The adiabatic (Ω→0) transverse stiffness a slow probe feels at `node`:
        −∂F_y(node)/∂y(node), measured by a central finite-difference test-displacement
        on the LIVE configuration (the dynamics' own force, no formula). This is what
        an infinitely-slow weak probe reads. Cycle-averaged over the pump, it is the
        CONSUMED observable."""
        yp = y.copy()
        yp[node] += delta
        ym = y.copy()
        ym[node] -= delta
        Fyp = self.forces(u, yp)[1][node]
        Fym = self.forces(u, ym)[1][node]
        return float(-(Fyp - Fym) / (2.0 * delta))


def _phi_prime_local(A):
    """Local Φ' for the analytic tangent-stiffness cross-check (module-private)."""
    return bond_tension(A)


# ── the three states, one measurement ────────────────────────────────────────
def run_three_states(*, n_nodes=600, dt=0.005, n_periods=200, pump_omega=1.2,
                     y0_pump=0.1428, y0_bias=0.1428, probe_node=200,
                     sponge_width=200, sponge_gamma=0.5, mass=1.0,
                     shear_saturates=True, a_dc_bias=None):
    """(a) COLD, (b) DC-BIAS, (c) PUMP traveling wave — SAME measurement
    (cycle-averaged transverse tangent stiffness at the probe node, ratio to cold).

    Parameters validated by the convergence sweep (dt-converged to 5 digits at
    dt=0.005; SWR≈1 in the interior at n_periods=200, sponge_width=200, γ=0.5;
    probe-node- and δ-independent). `shear_saturates` is the KEYING FORK (A vs B).
    `a_dc_bias` defaults to √α (the #526 A1 op-point) for the uniform-stretch control.

    Returns the measured probe stiffness for each state + diagnostics (SWR, drift).
    Measured from the time-domain response ONLY (the #531 tautology guard: no slot
    formulas consumed).
    """
    if a_dc_bias is None:
        a_dc_bias = float(np.sqrt(0.0072973525693))   # √α, def-vyvsn1 (Class-C echo)
    chain = PumpProbeChain(n_nodes, mass=mass, sponge_width=sponge_width,
                           sponge_gamma=sponge_gamma, shear_saturates=shear_saturates)
    period = 2 * np.pi / pump_omega
    n_steps = int(np.ceil(n_periods * period / dt))
    n_meas_periods = 20
    meas_start = int((n_periods - n_meas_periods) * period / dt)

    results: dict = {"params": dict(
        n_nodes=n_nodes, dt=dt, n_periods=n_periods, pump_omega=pump_omega,
        y0_pump=y0_pump, y0_bias=y0_bias, probe_node=probe_node,
        sponge_width=sponge_width, sponge_gamma=sponge_gamma, mass=mass,
        shear_saturates=shear_saturates, a_dc_bias=a_dc_bias)}

    # ── (a) COLD: quiescent chain; stiffness at rest = the instrument's ZERO ──
    # The measured tangent stiffness carries a fixed stencil convention factor (2×
    # for the 2-neighbor curvature stencil); we report the CONVENTION-FREE ratio
    # k_trans / k_trans_cold, so COLD ≡ 1.000 and DC-bias / pump are ratios to it.
    u0 = np.zeros(n_nodes)
    y0 = np.zeros(n_nodes)
    k_cold_raw = chain.transverse_tangent_stiffness(u0, y0, probe_node)
    results["cold"] = {"k_trans_raw": k_cold_raw, "k_trans": 1.0}

    # ── (b) DC-BIAS liveness — TWO controls (KEEP-BOTH) ──────────────────────
    #   (b1) uniform axial pre-stretch A_dc (the CLEAN #526 static-DC picture: every
    #        bond stretched to A_dc, y=0, shear-channel UNSTRAINED). Isolates the
    #        string-tension term T/ℓ; matches the merged #526 form k_s + T/L bit-exact.
    #        This is the PRIMARY liveness control (proves the probe sees a real T).
    #   (b2) the FROZEN-prereg held bow (alternating +y/−y relaxed). Confounds the
    #        shear channel (Rule-10 finding); reported as a secondary control.
    u_s = a_dc_bias * np.arange(n_nodes)
    y_s = np.zeros(n_nodes)
    k_stretch_raw = chain.transverse_tangent_stiffness(u_s, y_s, probe_node)
    Ls, _, _ = chain.bond_lengths(u_s, y_s)
    T_dc = float(bond_tension(Ls[probe_node] - ELL))
    results["dc_bias_stretch"] = {
        "k_trans_raw": k_stretch_raw,
        "k_trans": k_stretch_raw / k_cold_raw,
        "a_dc": a_dc_bias,
        "T_dc": T_dc,
        "merged_526_form": float(1.0 + T_dc / Ls[probe_node]),   # k_s + T/L, ratio
    }
    u_b, y_b = _relax_held_bow(chain, y0_bias)
    k_bias_raw = chain.transverse_tangent_stiffness(u_b, y_b, probe_node)
    results["dc_bias_heldbow"] = {
        "k_trans_raw": k_bias_raw,
        "k_trans": k_bias_raw / k_cold_raw,
        "note": "zig-zag bow confounds shear softening + tension (Rule-10 finding)",
    }

    # ── (c) PUMP traveling transverse wave: drive node 0, absorb at far end ───
    results["pump"] = _run_pump(chain, dt, n_steps, pump_omega, y0_pump, probe_node,
                                meas_start, sponge_width, k_cold_raw)

    # undriven closed-chain drift diagnostic (the honest symplectic-drift gate)
    results["energy_drift_undriven"] = _undriven_drift(n_nodes, dt, n_steps, mass, y0_pump)

    return results


def _relax_held_bow(chain: PumpProbeChain, y_bias: float, n_relax: int = 4000,
                    dt: float = 0.02):
    """Impose a static alternating transverse bow (Dirichlet on y for all nodes) and
    relax u to mechanical equilibrium (damped dynamics on u only). Returns (u, y)."""
    n = chain.n
    y = y_bias * (-1.0) ** np.arange(n)
    y[0] = 0.0
    y[-1] = 0.0   # clamp ends so the bow is interior
    u = np.zeros(n)
    vu = np.zeros(n)
    gamma = 0.4
    for _ in range(n_relax):
        Fu = chain.forces(u, y)[0]
        au = Fu / chain.m - gamma * vu
        vu = vu + dt * au
        u = u + dt * vu
        u[0] = 0.0
        u[-1] = 0.0
    return u, y


def _run_pump(chain: PumpProbeChain, dt, n_steps, omega, y0, probe_node,
              meas_start, sponge_width, k_cold_raw):
    """Drive a transverse pump at node 0; integrate; cycle-average the transverse
    tangent stiffness at the probe node over the measurement window; measure SWR.
    Returns the CONVENTION-FREE ratio k_trans / k_trans_cold (the arm observable)."""
    n = chain.n
    state = ChainState(np.zeros(n), np.zeros(n), np.zeros(n), np.zeros(n))
    ramp_periods = 10.0

    def drive(t):
        # transverse pump only (u0 free at 0); smooth ramp-on to avoid a shock front
        ramp = min(1.0, t / (ramp_periods * 2 * np.pi / omega))
        return (0.0, ramp * y0 * np.sin(omega * t))

    k_samples = []
    y_env_max = np.zeros(n)
    t = 0.0
    for step in range(n_steps):
        state = chain.step_verlet(state, dt, drive=drive, t=t)
        t += dt
        if step >= meas_start:
            k_samples.append(chain.transverse_tangent_stiffness(state.u, state.y, probe_node))
            y_env_max = np.maximum(y_env_max, np.abs(state.y))
    # SWR over the interior traveling region (exclude sponge + near-drive transient)
    i0 = 20
    i1 = n - sponge_width - 5
    env = y_env_max[i0:i1]
    env = env[env > 1e-6 * y0]
    swr = float(np.max(env) / max(np.min(env), 1e-12)) if env.size else float("nan")
    k_raw = float(np.mean(k_samples)) if k_samples else float("nan")
    return {
        "k_trans_raw": k_raw,
        "k_trans": k_raw / k_cold_raw,
        "k_trans_std_raw": float(np.std(k_samples)) if k_samples else float("nan"),
        "k_trans_std": float(np.std(k_samples)) / k_cold_raw if k_samples else float("nan"),
        "swr": swr,
        "n_meas_samples": len(k_samples),
        "pump_env_at_probe": float(y_env_max[probe_node]),
    }


def _undriven_drift(n_nodes, dt, n_steps, mass, y0):
    """Energy drift of the UNDRIVEN closed chain (no drive, no sponge) seeded with a
    transverse displacement of scale y0 — the honest symplectic-drift gate."""
    chain = PumpProbeChain(n_nodes, mass=mass, sponge_width=0, sponge_gamma=0.0)
    y = y0 * np.sin(2 * np.pi * np.arange(n_nodes) / 16.0)
    y[0] = 0.0
    y[-1] = 0.0
    state = ChainState(np.zeros(n_nodes), y.copy(), np.zeros(n_nodes), np.zeros(n_nodes))
    E0 = chain.energy(state)
    # MAJOR-d (orchestrator review PR #532): drift over the FULL n_steps window the
    # prereg specified, NOT a truncated 6-period window. The max drift over the whole
    # window is the honest gate value (a late-window blow-up must not be hidden).
    max_drift = 0.0
    for step in range(n_steps):
        state = chain.step_verlet(state, dt, drive=None)
        if step % 500 == 0:
            max_drift = max(max_drift, abs((chain.energy(state) - E0) / E0) if E0 else 0.0)
    E1 = chain.energy(state)
    return max(max_drift, abs((E1 - E0) / E0) if E0 else float("nan"))


# ═════════════════════════════════════════════════════════════════════════════
# POST-REVIEW ANALYSIS (orchestrator review of PR #532, 2026-07-05) — the three
# reproductions that INVALIDATE the original adjudication. These characterize what
# the lab-frame observable actually measured; they are the arc's real product.
# ═════════════════════════════════════════════════════════════════════════════

class LinearChain(PumpProbeChain):
    """CRITICAL-1 control: a LINEAR axial spring (force = k_a·(L−1), NO kernel Φ',
    NO concavity, NO Jensen) + a constant shear spring. If the pump verdict is a
    kinematic tilt-projection, this reproduces it; if it were Jensen rectification
    (which requires the concave kernel), this would give nothing. Result: reproduces
    the nonlinear keying-B verdict to ~2e-6 — the effect is KINEMATIC, not Jensen."""

    def forces(self, u, y):
        L, dx, dy = self.bond_lengths(u, y)
        A = L - ELL
        T = K_A * A                       # LINEAR axial spring — no kernel, no concavity
        ux = dx / L
        uy = dy / L
        Fu = np.zeros(self.n)
        Fy = np.zeros(self.n)
        Fu[:-1] += T * ux
        Fy[:-1] += T * uy
        Fu[1:] -= T * ux
        Fy[1:] -= T * uy
        curv = y[:-2] - 2.0 * y[1:-1] + y[2:]
        Fy[1:-1] += K_S * curv            # constant shear spring
        return Fu, Fy


def tilt_decomposition(chain: PumpProbeChain, *, probe_node=200, dt=0.005,
                       pump_omega=1.2, y0=0.1428, n_periods=200):
    """CRITICAL-1 decomposition at the probe node, cycle-averaged over the window:
    the tangent stiffness splits into (shear spring) + (bond-frame string tension)
    + (lab-frame KINEMATIC TILT ⟨Φ''(A)·u_y²⟩ — the axial spring felt through the
    bond slope). Returns the three channel means (fractions over cold) + the total."""
    period = 2 * np.pi / pump_omega
    n_steps = int(np.ceil(n_periods * period / dt))
    meas_start = int((n_periods - 20) * period / dt)
    state = ChainState(np.zeros(chain.n), np.zeros(chain.n), np.zeros(chain.n), np.zeros(chain.n))
    ramp = 10.0 * period

    def drive(t):
        return (0.0, min(1.0, t / ramp) * y0 * np.sin(pump_omega * t))

    i = probe_node
    shear, tension, tilt = [], [], []
    t = 0.0
    for step in range(n_steps):
        state = chain.step_verlet(state, dt, drive=drive, t=t)
        t += dt
        if step >= meas_start:
            L, dx, dy = chain.bond_lengths(state.u, state.y)
            A = L - ELL

            def pair(b):
                return 0.5 * (b[i - 1] + b[i])

            tension.append(pair(bond_tension(A)) / pair(L))
            tilt.append(pair(np.sqrt(np.clip(1 - A**2, 0, 1))) * pair((dy / L) ** 2))
            if chain.shear_saturates:
                shear.append(_saturation(0.5 * (abs(dy[i - 1]) / L[i - 1] + abs(dy[i]) / L[i])))
            else:
                shear.append(1.0)
    return {
        "shear_frac": float(np.mean(shear) - 1.0),
        "tension_frac": float(np.mean(tension)),
        "kinematic_tilt_frac": float(np.mean(tilt)),
    }


def cycle_mean_config_stiffness(chain: PumpProbeChain, *, probe_node=200, dt=0.005,
                                pump_omega=1.2, y0=0.1428, n_periods=200,
                                free_drive_end=False):
    """CRITICAL-2 readout: accumulate the cycle-MEAN configuration (⟨u⟩, ⟨y⟩) over
    the window and read the tangent stiffness AT it, plus the mean bond strain at the
    probe. If the mean-config stiffness reads COLD (≈1) and ⟨A_bond⟩ is not a positive
    bulk deposit, there is NO deposited DC bias the slow probe feels. `free_drive_end`
    releases the node-0 longitudinal pin (drive sets y0 only) — the boundary control."""
    period = 2 * np.pi / pump_omega
    n_steps = int(np.ceil(n_periods * period / dt))
    meas_start = int((n_periods - 20) * period / dt)
    state = ChainState(np.zeros(chain.n), np.zeros(chain.n), np.zeros(chain.n), np.zeros(chain.n))
    ramp = 10.0 * period

    def drive(t):
        return (0.0, min(1.0, t / ramp) * y0 * np.sin(pump_omega * t))

    umean = np.zeros(chain.n)
    ymean = np.zeros(chain.n)
    cnt = 0
    t = 0.0
    for step in range(n_steps):
        state = _step_free_end(chain, state, dt, drive, t) if free_drive_end \
            else chain.step_verlet(state, dt, drive=drive, t=t)
        t += dt
        if step >= meas_start:
            umean += state.u
            ymean += state.y
            cnt += 1
    umean /= cnt
    ymean /= cnt
    k_cold = chain.transverse_tangent_stiffness(np.zeros(chain.n), np.zeros(chain.n), probe_node)
    k_mean = chain.transverse_tangent_stiffness(umean, ymean, probe_node) / k_cold
    A_profile = chain.bond_lengths(umean, ymean)[0] - ELL
    return {
        "k_trans_at_cycle_mean": float(k_mean),
        "A_bond_at_probe": float(A_profile[probe_node]),
        "A_bond_profile": [float(A_profile[j]) for j in (20, 100, probe_node, 380)],
        "free_drive_end": free_drive_end,
    }


def _step_free_end(chain, state, dt, drive, t):
    """Velocity-Verlet step with node-0 longitudinal pin RELEASED (only y0 driven).
    The boundary control for CRITICAL-2 (the Dirichlet u[0]=0 pin injects an arbitrary
    mean axial force; freeing it sign-flips the apparent deposit)."""
    u, y, vu, vy = state.u, state.y, state.vu, state.vy
    Fu, Fy = chain.forces(u, y)
    au = Fu / chain.m - chain.gamma * vu
    ay = Fy / chain.m - chain.gamma * vy
    vuh = vu + 0.5 * dt * au
    vyh = vy + 0.5 * dt * ay
    un = u + dt * vuh
    yn = y + dt * vyh
    d = drive(t + dt)
    if d is not None:
        yn[0] = d[1]                     # ONLY y0 driven; u0 FREE (no pin)
    Fu2, Fy2 = chain.forces(un, yn)
    au2 = Fu2 / chain.m - chain.gamma * vuh
    ay2 = Fy2 / chain.m - chain.gamma * vyh
    vun = vuh + 0.5 * dt * au2
    vyn = vyh + 0.5 * dt * ay2
    if d is not None:
        vyn[0] = (yn[0] - y[0]) / dt
    return ChainState(un, yn, vun, vyn)


def honest_band(shear_saturates=True):
    """MAJOR-c: the honest band from the WINDOW non-convergence + node sweep, not the
    optimistic 0.30%. Returns the measured spread over n_periods {160,200,240,280} and
    over probe_node {150,200,300}. The band is 3× the max residual."""
    windows = [run_three_states(shear_saturates=shear_saturates, n_periods=n)["pump"]["k_trans"]
               for n in (160, 200, 240, 280)]
    nodes = [run_three_states(shear_saturates=shear_saturates, probe_node=nd)["pump"]["k_trans"]
             for nd in (150, 200, 300)]
    window_spread = float(max(windows) - min(windows))
    node_spread = float(max(nodes) - min(nodes))
    residual = max(window_spread, node_spread)
    return {
        "window_spread": window_spread,
        "node_spread": node_spread,
        "residual_floor": residual,
        "band_3x": 3.0 * residual,
    }


# ═════════════════════════════════════════════════════════════════════════════
# ADJUDICATION — POST-REVIEW: the observable is LAB-FRAME MIXED, so no bond-frame
# arm can be excluded/confirmed. The bin is [ADJUDICATION-INVALID]. The gate that
# survives is the BOND-FRAME LIVENESS control (an independent reference path).
# ═════════════════════════════════════════════════════════════════════════════

# HONEST BAND (MAJOR-c): the window non-convergence spread (~0.5%) is the residual
# floor, not the optimistic dt-only 0.30%. Measured this session: window spread
# 0.0049, node spread ~0.001. Band = 3× max ≈ 0.66% (still < 2.04% separation, but
# the observable is INVALID regardless — the band question is moot for the fork).
DERIVED_BAND = 3.0e-3        # the dt/window/node floor for the LIVENESS gate only
HONEST_BAND = 6.6e-3         # the pump observable's honest band (window non-convergence)


class DiscrepantHaltBin(AssertionError):
    """The bin selector's loud halt: a measured state contradicts a structural
    invariant (e.g. COLD ≠ 1, or the DC-bias liveness control fails to see tension)."""


def adjudicate(*, shear_saturates=True, band=DERIVED_BAND, verbose=False):
    """POST-REVIEW (orchestrator PR #532): the pump observable is LAB-FRAME MIXED — it
    feels the axial spring through the bond slope (the kinematic tilt term), which
    neither frozen (bond-frame) arm modeled. Proven: a LINEAR chain reproduces the
    pump verdict to ~2e-6 (tilt_decomposition + LinearChain), and the cycle-MEAN config
    reads COLD (cycle_mean_config_stiffness). So NO bond-frame arm can be excluded or
    confirmed — the bin is [ADJUDICATION-INVALID] and the #526 fork REMAINS OPEN.

    The structural liveness HALTs (COLD≠1, blind instrument) and the BOND-FRAME liveness
    control still gate — that control (the uniform-stretch DC-bias reading k_s+T/L) is
    the arc's real surviving product. Returns (bin, results, gate_diagnostics)."""
    from scripts.vol_1_foundations import pump_probe_predictions as pred  # SEPARATE module

    res = run_three_states(shear_saturates=shear_saturates)

    # ── structural liveness HALTs (before any bin) ───────────────────────────
    if abs(res["cold"]["k_trans"] - 1.0) > 1e-9:
        raise DiscrepantHaltBin(f"COLD k_trans={res['cold']['k_trans']} ≠ 1 — instrument zero broken.")
    live = res["dc_bias_stretch"]["k_trans"]
    if live - 1.0 <= band:
        raise DiscrepantHaltBin(
            f"DC-BIAS liveness FAILED: stretch k_trans={live:.6f} does not exceed cold by >band "
            f"({band}) — the probe is BLIND to a genuine static tension. HALT.")
    # BOND-FRAME liveness reconcile: the uniform-stretch reading vs an INDEPENDENT
    # reference computed by the prediction module (a DIFFERENT code path — MAJOR-e).
    # pred.bond_tension + pred.saturation reassemble k_s·S(0)+T/L from scratch; the
    # dynamics' merged_526_form is its own force-model readout. Two independent paths.
    A_dc = res["dc_bias_stretch"]["a_dc"]
    L_dc = 1.0 + A_dc                     # uniform stretch: L = 1 + A_dc
    indep_liveness = float(pred.saturation(0.0) + pred.bond_tension(A_dc) / L_dc)
    from ave.validation.reconcile_gate import ReconcileGate
    ReconcileGate(
        label="PC_DC_LIVENESS_bondframe_independent",
        claimed=res["dc_bias_stretch"]["k_trans"],
        independent=indep_liveness,      # prediction-module reassembly, different path
        rtol=1e-4, atol=0.0,
    ).enforce()

    # ── the fork verdict: INVALID (lab-frame observable) ─────────────────────
    tilt = tilt_decomposition(PumpProbeChain(res["params"]["n_nodes"],
                                             sponge_width=res["params"]["sponge_width"],
                                             sponge_gamma=res["params"]["sponge_gamma"],
                                             shear_saturates=shear_saturates),
                              probe_node=res["params"]["probe_node"])
    binv = "ADJUDICATION-INVALID"        # lab-frame observable; fork stays OPEN
    gate = {
        "bin": binv,
        "reason": "lab-frame observable (kinematic tilt dominates); neither bond-frame arm testable",
        "k_meas_labframe": res["pump"]["k_trans"],
        "kinematic_tilt_frac": tilt["kinematic_tilt_frac"],
        "shear_frac": tilt["shear_frac"],
        "bondframe_tension_frac": tilt["tension_frac"],
        "bondframe_liveness": res["dc_bias_stretch"]["k_trans"],
        "bondframe_liveness_independent_ref": indep_liveness,
        "swr": res["pump"]["swr"],
        "honest_band_note": "window non-convergence ~0.5%; the lab-frame observable is invalid regardless",
    }
    if verbose:
        print(f"keying {'A' if shear_saturates else 'B'}: [{binv}] "
              f"lab-frame pump={res['pump']['k_trans']:.6f} "
              f"(kinematic tilt={tilt['kinematic_tilt_frac']:+.4f} DOMINATES; "
              f"bond-frame tension={tilt['tension_frac']:+.4f}); fork OPEN")
    return binv, res, gate


if __name__ == "__main__":
    import json
    out = {}
    for keying in (True, False):
        binv, res, gate = adjudicate(shear_saturates=keying, verbose=True)
        out[f"keying_{'A' if keying else 'B'}"] = {"bin": binv, "gate": gate}
    # CRITICAL controls
    lin = LinearChain(600, sponge_width=200, sponge_gamma=0.5)
    r_lin = _run_pump(lin, 0.005, int(200 * 2 * np.pi / 1.2 / 0.005), 1.2, 0.1428, 200,
                      int(180 * 2 * np.pi / 1.2 / 0.005), 200,
                      lin.transverse_tangent_stiffness(np.zeros(600), np.zeros(600), 200))["k_trans"]
    out["CRITICAL1_linear_chain_reproduces"] = {"linear_pump_ratio": r_lin}
    out["CRITICAL2_cycle_mean_pinned"] = cycle_mean_config_stiffness(
        PumpProbeChain(600, sponge_width=200, sponge_gamma=0.5, shear_saturates=True))
    out["CRITICAL2_cycle_mean_free_end"] = cycle_mean_config_stiffness(
        PumpProbeChain(600, sponge_width=200, sponge_gamma=0.5, shear_saturates=True),
        free_drive_end=True)
    out["MAJORc_honest_band"] = honest_band(shear_saturates=True)
    print(json.dumps(out, indent=2, default=float))
