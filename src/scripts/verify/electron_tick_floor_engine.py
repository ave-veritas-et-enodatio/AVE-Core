"""LEG B (engine) — the electron tick-floor: a conservative (lossless) coupled-cell phase
lattice hosting a div-N subharmonic (2,3) mode. Three blind measurements + kill-joints.

Prereg: research/2026-07-07_electron-tick-floor_prereg_FROZEN.md (model FROZEN there).

MODEL (frozen, declared METHOD-not-physics where numerical):
  Ensemble ("the carrier", mutual lock, NO master oscillator): M cells on a periodic ring,
  each a LOSSLESS rotator (phase-reduced intrinsic LC clock). SECOND-ORDER / inertial /
  HAMILTONIAN (Ax3-lossless -- NOT first-order Kuramoto, which relaxes to sync = a
  dissipative / gradient-descent reading = an SM leak; see prereg CP1):
      theta_i' = Omega_i
      Omega_i' = kappa_ens [sin(theta_{i+1}-theta_i) + sin(theta_{i-1}-theta_i)]
                 + [i in cluster] (eta*kappa_mode/(P N)) sin(N phi - theta_i)   (mode back-reaction)
  Mode ("the electron", div-N subharmonic with internal (2,3)): fundamental phase phi,
  internal angles alpha=2 phi, beta=3 phi (the phase-space (2,3) winding on the Clifford torus):
      phi' = Omega_mode
      Omega_mode' = (eta*kappa_mode/P) sum_{i in cluster} sin(theta_i - N phi)
  H = 0.5 sum Omega_i^2 + 0.5 Omega_mode^2 - kappa_ens sum_edges cos(theta_i-theta_j)
      - (eta*kappa_mode/(P N)) sum_cluster cos(theta_i - N phi)   is CONSERVED (leapfrog).
  eta = eta(N) is the div-N harmonic-dilution factor (how much N-th-harmonic content couples
  the subharmonic to its reference); eta=1 is "full harmonic" (default). Its N-scaling is the
  UNDER-DETERMINED physics fork surfaced to Grant (see the lock-range finding below).

  Ticks: marked when the EMERGENT ensemble mean phase Psi=arg(sum e^{i theta_i}) advances 2pi.
  The mode's (alpha,beta) are SAMPLED AT TICKS and windings counted with the discrete
  principal-branch estimator -- the branch that ALIASES exactly at the physical sampling floor.
  Integration is continuous (fine substep); tick-sampling is PHYSICAL. So aliasing is a property
  of the lattice tick granularity, NOT the integrator substep (dt-convergence proves this).

=============================================================================
FIREWALL (alpha-circularity knife): this ENTIRE path is alpha-clean. No physical constant is
imported. omega_ens, kappa_ens, kappa_mode, M, P are DIMENSIONLESS METHOD parameters; the FLOOR
result (N_min) is proved INDEPENDENT of all of them (pure representability). Homonym guard: N
(sampling count) != Q (=1/alpha coherence count). No alpha, m_e, lambdabar_C, lepton mass here.
=============================================================================

REGIME: cold lattice, lossless-reactive (H conserved), small-signal phase dynamics; discrete-time
leapfrog declared METHOD; the dt->0 convergence study proves the substep is not the answer's clock.
"""
from __future__ import annotations

import json
import math
import os
import sys
from dataclasses import dataclass, field

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# Canonical topological winding pair (2,3): phase-space winding INTEGERS, not constants.
K1_WINDING = 2
K2_WINDING = 3


# ---------------------------------------------------------------------------
def principal_angle(dtheta: float) -> float:
    """Wrap a phase increment into (-pi, pi] -- the discrete estimator's principal branch."""
    return (dtheta + math.pi) % (2.0 * math.pi) - math.pi


@dataclass
class LatticeConfig:
    M: int = 24                 # ensemble cells on the ring
    P: int = 4                  # cluster size (mode's host sub-cluster)
    kappa_ens: float = 1.0      # ensemble reactive coupling (sets signal speed)
    kappa_mode: float = 1.0     # mode<->cluster coupling (dimensionless method param)
    omega_ens: float = 1.0      # emergent common rotation rate (method unit; NOT a physical omega)
    eta_exponent: float = 0.0   # div-N harmonic dilution eta(N)=N**(-eta_exponent); 0 => full
    cluster: tuple = field(default_factory=lambda: (0, 1, 2, 3))

    def eta(self, N: int) -> float:
        return float(N) ** (-self.eta_exponent)


# ---------------------------------------------------------------------------
def _accel(theta: np.ndarray, phi: float, N: int, cfg: LatticeConfig):
    """Accelerations from the conserved Hamiltonian (exact gradients)."""
    M = cfg.M
    right = np.roll(theta, -1)
    left = np.roll(theta, 1)
    a_theta = cfg.kappa_ens * (np.sin(right - theta) + np.sin(left - theta))
    eta_kmode = cfg.eta(N) * cfg.kappa_mode
    cl = np.array(cfg.cluster)
    ref_err = N * phi - theta[cl]                       # (N phi - theta_i)
    a_theta[cl] += (eta_kmode / (cfg.P * N)) * np.sin(ref_err)
    a_phi = (eta_kmode / cfg.P) * float(np.sum(np.sin(theta[cl] - N * phi)))
    return a_theta, a_phi


def _energy(theta, Omega, phi, Omega_mode, N, cfg) -> float:
    right = np.roll(theta, -1)
    ke = 0.5 * float(np.sum(Omega ** 2)) + 0.5 * Omega_mode ** 2
    v_ens = -cfg.kappa_ens * float(np.sum(np.cos(theta - right)))  # each edge once (ring)
    cl = np.array(cfg.cluster)
    eta_kmode = cfg.eta(N) * cfg.kappa_mode
    v_mode = -(eta_kmode / (cfg.P * N)) * float(np.sum(np.cos(theta[cl] - N * phi)))
    return ke + v_ens + v_mode


def integrate(N: int, delta: float, cfg: LatticeConfig, n_periods: int = 4, n_sub: int = 32,
              perturb_cell: int | None = None, perturb_amp: float = 0.0,
              theta0_scatter: float = 0.0, seed: int = 0):
    """Leapfrog-integrate the coupled system for n_periods mode periods (= n_periods*N ticks).

    delta: fractional detuning of the mode from omega_ens/N (Omega_mode(0) = (omega_ens/N)(1+delta)).
    Returns the continuous trajectory + tick-sampled (alpha,beta) + lock/energy diagnostics.
    """
    rng = np.random.default_rng(seed)
    M = cfg.M
    theta = theta0_scatter * rng.standard_normal(M) if theta0_scatter else np.zeros(M)
    Omega = np.full(M, cfg.omega_ens)
    phi = 0.0
    Omega_mode = (cfg.omega_ens / N) * (1.0 + delta)
    if perturb_cell is not None:
        Omega[perturb_cell] += perturb_amp

    T_tick = 2.0 * math.pi / cfg.omega_ens
    dt = T_tick / n_sub
    n_steps = int(round(n_periods * N * n_sub))

    Psi_unwrap = 0.0
    prev_psi = math.atan2(float(np.sum(np.sin(theta))), float(np.sum(np.cos(theta))))
    t_arr = np.empty(n_steps + 1)
    Psi_arr = np.empty(n_steps + 1)
    alpha_arr = np.empty(n_steps + 1)
    beta_arr = np.empty(n_steps + 1)
    H_arr = np.empty(n_steps + 1)
    lock_err = np.empty(n_steps + 1)   # psi = N phi - Psi_unwrap (mode-vs-ensemble subharmonic error)

    a_theta, a_phi = _accel(theta, phi, N, cfg)
    for k in range(n_steps + 1):
        # record
        psi_now = math.atan2(float(np.sum(np.sin(theta))), float(np.sum(np.cos(theta))))
        Psi_unwrap += principal_angle(psi_now - prev_psi)
        prev_psi = psi_now
        t_arr[k] = k * dt
        Psi_arr[k] = Psi_unwrap
        alpha_arr[k] = K1_WINDING * phi
        beta_arr[k] = K2_WINDING * phi
        H_arr[k] = _energy(theta, Omega, phi, Omega_mode, N, cfg)
        lock_err[k] = N * phi - Psi_unwrap
        if k == n_steps:
            break
        # velocity-Verlet
        Omega += 0.5 * dt * a_theta
        Omega_mode += 0.5 * dt * a_phi
        theta += dt * Omega
        phi += dt * Omega_mode
        a_theta, a_phi = _accel(theta, phi, N, cfg)
        Omega += 0.5 * dt * a_theta
        Omega_mode += 0.5 * dt * a_phi

    # tick-sample (alpha,beta) at Psi = 2*pi*j crossings (PHYSICAL tick granularity)
    alpha_ticks, beta_ticks = _sample_at_ticks(Psi_arr, alpha_arr, beta_arr)
    w2 = _winding_from_ticks(alpha_ticks, n_periods)
    w3 = _winding_from_ticks(beta_ticks, n_periods)
    H0 = H_arr[0]
    dH = float(np.max(np.abs(H_arr - H0)) / (abs(H0) + 1e-30))
    # lock: subharmonic error bounded (librating) vs running (drift)
    lock_span = float(np.max(lock_err) - np.min(lock_err))
    locked = lock_span < math.pi  # bounded within a pendulum well
    return {
        "N": N, "delta": delta,
        "w2_measured": w2, "w3_measured": w3,
        "winding_pair_ok": (w2 == K1_WINDING and w3 == K2_WINDING),
        "n_ticks": len(alpha_ticks) - 1,
        "H_rel_drift": dH,
        "lock_span": lock_span, "locked": locked,
    }


def _sample_at_ticks(Psi: np.ndarray, alpha: np.ndarray, beta: np.ndarray):
    """Linear-interpolate (alpha,beta) at each Psi = 2*pi*j crossing."""
    two_pi = 2.0 * math.pi
    j = 1
    a_ticks, b_ticks = [], []
    # include the initial tick at Psi~0
    a_ticks.append(float(alpha[0]))
    b_ticks.append(float(beta[0]))
    for k in range(1, len(Psi)):
        while Psi[k] >= j * two_pi:
            frac = (j * two_pi - Psi[k - 1]) / (Psi[k] - Psi[k - 1] + 1e-30)
            a_ticks.append(float(alpha[k - 1] + frac * (alpha[k] - alpha[k - 1])))
            b_ticks.append(float(beta[k - 1] + frac * (beta[k] - beta[k - 1])))
            j += 1
    return np.array(a_ticks), np.array(b_ticks)


def _winding_from_ticks(x_ticks: np.ndarray, n_periods: int) -> int:
    """Discrete principal-branch winding: sum principal increments, divide by 2pi*n_periods."""
    if len(x_ticks) < 2:
        return 0
    inc = np.array([principal_angle(x_ticks[i + 1] - x_ticks[i]) for i in range(len(x_ticks) - 1)])
    total = float(np.sum(inc))
    return int(round(total / (2.0 * math.pi * n_periods)))


# ---------------------------------------------------------------------------
# MEASUREMENT (i): LOCK/DECAY vs N  (representability floor + lock)
# ---------------------------------------------------------------------------
def measurement_i(cfg: LatticeConfig, n_lo: int = 4, n_hi: int = 16,
                  spots=(20, 30), n_sub: int = 32) -> dict:
    """Blind N sweep. (i-a) representability: tick-sampled (alpha,beta) == (2,3)?
    (i-b) lock: mode stays div-N entrained (delta=0, exact tracking). Engine N_min = first
    N where the winding pair reads (2,3)."""
    Ns = list(range(n_lo, n_hi + 1)) + list(spots)
    rows = {}
    for N in Ns:
        r = integrate(N, delta=0.0, cfg=cfg, n_sub=n_sub)
        rows[N] = {"w2": r["w2_measured"], "w3": r["w3_measured"],
                   "pair_ok": r["winding_pair_ok"], "locked": r["locked"],
                   "H_drift": r["H_rel_drift"]}
    clean = [N for N in Ns if rows[N]["pair_ok"]]
    return {
        "sweep": {str(N): rows[N] for N in Ns},
        "engine_N_min": min(clean) if clean else None,
        "reads_at_N5": [rows[5]["w2"], rows[5]["w3"]] if 5 in rows else None,
        "reads_at_N6": [rows[6]["w2"], rows[6]["w3"]] if 6 in rows else None,
        "reads_at_N7": [rows[7]["w2"], rows[7]["w3"]] if 7 in rows else None,
    }


# ---------------------------------------------------------------------------
# MEASUREMENT (ii): [TOWER-EMERGES / TOWER-FAILS] -- strain kill-joint
# ---------------------------------------------------------------------------
def _max_locked_delta(N: int, cfg: LatticeConfig, n_sub: int = 24,
                      d_hi: float = 10.0, iters: int = 22) -> float:
    """Bisection for the largest |delta| that stays locked at division N (the conservative
    lock half-range in detuning units)."""
    lo, hi = 0.0, d_hi
    if integrate(N, delta=hi, cfg=cfg, n_sub=n_sub)["locked"]:
        return hi  # still locked at the sweep ceiling
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if integrate(N, delta=mid, cfg=cfg, n_sub=n_sub)["locked"]:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def measurement_ii(cfg: LatticeConfig, n_sub: int = 24) -> dict:
    """(a) GLOBAL uniform dilation (TOWER-EMERGES demo): scale all clocks by s=sqrt(1-A^2);
    the div-N ratio must stay EXACTLY intact and (2,3) survive. (b) LOCK-RANGE vs N: measure
    the conservative lock half-range and compare to the two candidate laws (first-order Adler
    kappa/N vs conservative pendulum ~2 sqrt(N kappa))."""
    # (a) global uniform dilation: re-price the whole locked tower's clock
    tower = {}
    for A2 in (0.05, 0.10, 0.20):
        s = math.sqrt(1.0 - A2)
        cfg_s = LatticeConfig(M=cfg.M, P=cfg.P, kappa_ens=cfg.kappa_ens,
                              kappa_mode=cfg.kappa_mode, omega_ens=cfg.omega_ens * s,
                              eta_exponent=cfg.eta_exponent, cluster=cfg.cluster)
        r = integrate(7, delta=0.0, cfg=cfg_s, n_sub=n_sub)
        tower[f"A2={A2:.2f}"] = {
            "s_sqrt(1-A2)": s,
            "winding_pair_ok": r["winding_pair_ok"],  # N=7 ratio intact after re-pricing
            "w2": r["w2_measured"], "w3": r["w3_measured"],
        }
    tower_verdict = "TOWER-EMERGES" if all(v["winding_pair_ok"] for v in tower.values()) else "TOWER-FAILS"

    # (b) lock-range vs N: conservative half-range, compared to the two laws
    lockrange = {}
    for N in (7, 8, 10, 12, 14, 16):
        d_lock = _max_locked_delta(N, cfg, n_sub=n_sub)
        lockrange[str(N)] = {
            "conservative_halfrange_delta": d_lock,
            "first_order_adler_kappa_over_N": cfg.kappa_mode / N,
            "pendulum_separatrix_2sqrt_Nk": 2.0 * math.sqrt(N * cfg.kappa_mode) / cfg.omega_ens,
        }
    return {
        "global_dilation": tower,
        "tower_verdict": tower_verdict,
        "lock_range_vs_N": lockrange,
    }


# ---------------------------------------------------------------------------
# MEASUREMENT (iii): [C-INVARIANT / C-VIOLATED] -- Michelson-class internal null
# ---------------------------------------------------------------------------
def _signal_speed(cfg: LatticeConfig, with_mode: bool, N: int = 7, n_sub: int = 40) -> float:
    """Perturb one cell's momentum; time the disturbance to reach the antipodal cell; speed =
    (ring distance) / (arrival time). Mode present or absent (kappa_mode=0)."""
    cfg_use = cfg if with_mode else LatticeConfig(M=cfg.M, P=cfg.P, kappa_ens=cfg.kappa_ens,
                                                  kappa_mode=0.0, omega_ens=cfg.omega_ens,
                                                  eta_exponent=cfg.eta_exponent, cluster=cfg.cluster)
    M = cfg_use.M
    src = M // 2  # perturb far from the cluster (cluster is 0..P-1)
    tgt = (src + M // 4) % M
    theta = np.zeros(M)
    Omega = np.full(M, cfg_use.omega_ens)
    Omega[src] += 0.2
    phi, Omega_mode = 0.0, cfg_use.omega_ens / N
    T_tick = 2.0 * math.pi / cfg_use.omega_ens
    dt = T_tick / n_sub
    baseline = cfg_use.omega_ens
    a_theta, a_phi = _accel(theta, phi, N, cfg_use)
    dist = abs(tgt - src)
    for k in range(3000):
        Omega += 0.5 * dt * a_theta
        Omega_mode += 0.5 * dt * a_phi
        theta += dt * Omega
        phi += dt * Omega_mode
        a_theta, a_phi = _accel(theta, phi, N, cfg_use)
        Omega += 0.5 * dt * a_theta
        Omega_mode += 0.5 * dt * a_phi
        if abs(Omega[tgt] - baseline) > 0.02:  # arrival threshold
            t_arrive = (k + 1) * dt
            return dist / t_arrive
    return float("nan")


def measurement_iii(cfg: LatticeConfig) -> dict:
    """Signal speed WITH vs WITHOUT the locked mode, and N-independence."""
    c_with_7 = _signal_speed(cfg, with_mode=True, N=7)
    c_without = _signal_speed(cfg, with_mode=False, N=7)
    c_with_12 = _signal_speed(cfg, with_mode=True, N=12)
    rel = abs(c_with_7 - c_without) / (abs(c_without) + 1e-30)
    rel_N = abs(c_with_7 - c_with_12) / (abs(c_with_7) + 1e-30)
    return {
        "c_without_mode": c_with_or_nan(c_without),
        "c_with_mode_N7": c_with_or_nan(c_with_7),
        "c_with_mode_N12": c_with_or_nan(c_with_12),
        "rel_diff_with_vs_without": rel,
        "rel_diff_N7_vs_N12": rel_N,
        "verdict": "C-INVARIANT" if (rel < 0.05 and rel_N < 0.05) else "C-VIOLATED",
    }


def c_with_or_nan(x):
    return None if (x is None or (isinstance(x, float) and math.isnan(x))) else x


# ---------------------------------------------------------------------------
# dt-CONVERGENCE (prove the integrator substep is NOT the answer's clock)
# ---------------------------------------------------------------------------
def dt_convergence(cfg: LatticeConfig) -> dict:
    """Engine N_min and a lock verdict must be invariant as n_sub increases (dt -> 0)."""
    out = {}
    for n_sub in (16, 32, 64, 128):
        mi = measurement_i(cfg, n_lo=5, n_hi=8, spots=(), n_sub=n_sub)
        out[str(n_sub)] = {"engine_N_min": mi["engine_N_min"],
                           "reads_N5": mi["reads_at_N5"], "reads_N7": mi["reads_at_N7"]}
    nmins = {v["engine_N_min"] for v in out.values()}
    return {"by_n_sub": out, "N_min_invariant": (len(nmins) == 1), "N_min_values": sorted(nmins)}


# ---------------------------------------------------------------------------
# RECONCILE GATES (each with a can-fire self-test, per ave.validation.reconcile_gate)
# ---------------------------------------------------------------------------
def reconcile_gates(engine_N_min, miii: dict, max_H_drift: float) -> dict:
    """G1: engine representability N_min reconciles with the INDEPENDENT analytic modular
    N_min (Leg A, different code path) -- exact integer match. G2: signal speed with the mode
    reconciles with the speed without it (Michelson-class internal null). Energy gate: the
    lossless (Ax3) H-drift is below the reactive floor. Each gate's halt is can-fire proven."""
    from ave.validation.reconcile_gate import ReconcileGate  # src on path
    from electron_tick_floor_sampling import n_min_analytic   # verify/ on path (Leg A)

    results = {}
    # G1 -- cross-leg floor reconciliation (independent path: modular arithmetic vs time-domain)
    g1 = ReconcileGate(label="G1 engine-N_min == analytic-N_min",
                       claimed=float(engine_N_min),
                       independent=lambda: float(n_min_analytic()),
                       rtol=0.0, atol=0.0)
    results["G1_floor"] = g1.enforce(prove_first=True).as_dict()
    # G2 -- c-invariance (mode present vs absent), Michelson-class null
    cw, cwo = miii["c_with_mode_N7"], miii["c_without_mode"]
    g2 = ReconcileGate(label="G2 c_with_mode == c_without_mode",
                       claimed=float(cw), independent=lambda: float(cwo), rtol=0.05, atol=1e-9)
    results["G2_c_invariance"] = g2.enforce(prove_first=True).as_dict()
    # energy gate -- Ax3 lossless (H conserved to reactive floor)
    results["energy_lossless"] = {
        "max_H_rel_drift": max_H_drift, "floor": 1e-10, "passed": max_H_drift < 1e-10,
    }
    if not results["energy_lossless"]["passed"]:
        raise AssertionError(f"ENERGY-HALT: |dH/H|={max_H_drift:.2e} exceeds the lossless floor 1e-10")
    return results


def run() -> dict:
    cfg = LatticeConfig()
    mi = measurement_i(cfg)
    mii = measurement_ii(cfg)
    miii = measurement_iii(cfg)
    dtc = dt_convergence(cfg)
    max_H_drift = max(v["H_drift"] for v in mi["sweep"].values())
    gates = reconcile_gates(mi["engine_N_min"], miii, max_H_drift)
    return {
        "leg": "B (engine)",
        "config": {"M": cfg.M, "P": cfg.P, "kappa_ens": cfg.kappa_ens,
                   "kappa_mode": cfg.kappa_mode, "omega_ens": cfg.omega_ens,
                   "eta_exponent": cfg.eta_exponent},
        "measurement_i_lock_decay": mi,
        "measurement_ii_tower_strain": mii,
        "measurement_iii_c_invariance": miii,
        "dt_convergence": dtc,
        "reconcile_gates": gates,
        "max_H_rel_drift": max_H_drift,
        "engine_N_min": mi["engine_N_min"],
    }


def main() -> None:
    out = run()
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "electron_tick_floor_engine.json"), "w") as f:
        json.dump(out, f, indent=2, default=str)
    mi = out["measurement_i_lock_decay"]
    print("LEG B (engine) verdict:")
    print(f"  (i)   engine N_min = {out['engine_N_min']}  "
          f"(N=5 reads {mi['reads_at_N5']}, N=6 {mi['reads_at_N6']}, N=7 {mi['reads_at_N7']})")
    print(f"  (ii)  {out['measurement_ii_tower_strain']['tower_verdict']} (global dilation, N intact)")
    print(f"  (iii) {out['measurement_iii_c_invariance']['verdict']}")
    print(f"  dt-convergence: N_min invariant = {out['dt_convergence']['N_min_invariant']} "
          f"{out['dt_convergence']['N_min_values']}")
    print(f"  max |dH/H| over sweep = {out['max_H_rel_drift']:.2e} (Ax3-lossless check)")


if __name__ == "__main__":
    main()
