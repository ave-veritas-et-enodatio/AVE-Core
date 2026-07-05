"""HONEST NONLINEAR DYNAMICS MODULE — 2-DOF pump-probe chain.

Adjudicates the #526 T-slot scope fork (DC_ONLY vs EXTENDED) by running the FULL
NONLINEAR DYNAMICS of a 2-DOF-per-node chain and MEASURING what a slow transverse
probe sees through a traveling pump. NO slot bookkeeping. The dynamics do not know
how terms were divided between S and T; they just respond.

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
            shear_strain = 0.5 * (np.abs(dy[:-1]) / L[:-1] + np.abs(dy[1:]) / L[1:])
            k_shear_local = K_S * _saturation(shear_strain)  # k_s·S(A_shear), keying A
        else:
            k_shear_local = K_S                              # k_s constant, keying B
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
    steps = min(n_steps, 6000)
    for _ in range(steps):
        state = chain.step_verlet(state, dt, drive=None)
    E1 = chain.energy(state)
    return abs((E1 - E0) / E0) if E0 else float("nan")


# ── ADJUDICATION: the #528 ReconcileGate compares DYNAMICS vs PREDICTION outputs ──
#    (the two are SEPARATE modules — the #531 tautology guard. This adjudicator
#     IMPORTS the prediction module here ONLY to compare its frozen numbers against
#     the dynamics' measured output; the dynamics themselves never import it.)

# derived tolerance band (convergence sweep, this session): 3× the summed residual
# floor (dt 7e-7 + window 5e-5 + node-to-node ~1e-3, SWR=1.003) = 3e-3 = 0.30%.
# The band is strictly below the 2.04% arm separation ⟹ the arms are resolvable.
DERIVED_BAND = 3.0e-3


class DiscrepantHaltBin(AssertionError):
    """The bin selector's loud halt: a measured state contradicts a structural
    invariant (e.g. COLD ≠ 1, or the DC-bias liveness control fails to see tension)."""


def adjudicate(*, shear_saturates=True, band=DERIVED_BAND, verbose=False):
    """Run the three states, compare the measured PUMP probe stiffness against the
    two frozen arms via the #528 ReconcileGate, and select the bin. No fall-through
    else; DISCREPANT-HALT reachable (COLD-not-1 or liveness-fail HALTs before any
    verdict is read). Returns (bin, results, gate_diagnostics)."""
    from ave.validation.reconcile_gate import ReconcileGate
    from scripts.vol_1_foundations import pump_probe_predictions as pred  # SEPARATE module

    res = run_three_states(shear_saturates=shear_saturates)
    y0 = res["params"]["y0_pump"]

    # ── structural liveness HALTs (before any bin) ───────────────────────────
    if abs(res["cold"]["k_trans"] - 1.0) > 1e-9:
        raise DiscrepantHaltBin(f"COLD k_trans={res['cold']['k_trans']} ≠ 1 — instrument zero broken.")
    # PC-DC-LIVENESS: the uniform-stretch control MUST see the tension term (>band above cold)
    live = res["dc_bias_stretch"]["k_trans"]
    if live - 1.0 <= band:
        raise DiscrepantHaltBin(
            f"DC-BIAS liveness FAILED: stretch k_trans={live:.6f} does not exceed cold by >band "
            f"({band}) — the probe is BLIND to a genuine static tension. No pump null is bookable. HALT.")
    # and it must reconcile with the merged #526 form (independent: pred.k_trans_dc_liveness
    # is a DIFFERENT code path — the prediction module's held-bow form; the uniform-stretch
    # form is checked against its own analytic k_s+T/L, computed in the dynamics as merged_526_form).
    ReconcileGate(
        label="PC_DC_LIVENESS_vs_526form",
        claimed=res["dc_bias_stretch"]["k_trans"],
        independent=res["dc_bias_stretch"]["merged_526_form"],
        rtol=1e-4, atol=0.0,
    ).enforce()

    # ── the two frozen arms (from the SEPARATE prediction module) ────────────
    k_dc_only = pred.k_trans_pump_dc_only()       # 1.000000
    k_extended = pred.k_trans_pump_extended(y0)   # 1.020392
    k_meas = res["pump"]["k_trans"]

    def within(a, b):
        return abs(a - b) <= band

    matches_dc_only = within(k_meas, k_dc_only)
    matches_extended = within(k_meas, k_extended)

    if matches_dc_only and not matches_extended:
        binv = "DC-ONLY-CONFIRMED"
    elif matches_extended and not matches_dc_only:
        binv = "EXTENDED-CONFIRMED"
    elif not matches_dc_only and not matches_extended:
        binv = "NEITHER"
    else:
        # matches BOTH ⟹ the band is wider than the separation ⟹ cannot resolve
        binv = "UNRESOLVED"

    gate = {
        "k_meas": k_meas, "k_dc_only": k_dc_only, "k_extended": k_extended,
        "band": band, "sep_from_dc_only": abs(k_meas - k_dc_only),
        "sep_from_extended": abs(k_meas - k_extended),
        "matches_dc_only": matches_dc_only, "matches_extended": matches_extended,
        "excludes_dc_only": not matches_dc_only,
        "swr": res["pump"]["swr"], "drift": res["energy_drift_undriven"],
    }
    if verbose:
        print(f"keying {'A' if shear_saturates else 'B'}: PUMP={k_meas:.6f} "
              f"band=±{band} DC_ONLY={k_dc_only:.6f} EXT={k_extended:.6f} → [{binv}]")
    return binv, res, gate


if __name__ == "__main__":
    import json
    out = {}
    for keying in (True, False):
        binv, res, gate = adjudicate(shear_saturates=keying, verbose=True)
        out[f"keying_{'A' if keying else 'B'}"] = {"bin": binv, "gate": gate, "results": res}
    print(json.dumps(out, indent=2, default=float))
