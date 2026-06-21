"""
Node circulator coupling — the shear↔bulk (charge↔mass) coupling as a
NORM-PRESERVING ROTATION (a skew-Hermitian / gyrotropic GENERATOR).
=====================================================================

THE ONE REMAINING LIVE PATH FOR FORK-A.

Fork-A (`device-circuit-models.md`:210-215) asks: does the mass channel (bulk /
A1 dilatation) couple to the charge channel (shear / Cosserat micro-rotation) via
a conserved H_couple, or is it galvanic ISOLATION? Every potential-energy coupling
tried so far DETONATES or is INERT:

  • graft-v3 / graft-v4 trilinear potential  H = κ̃ ∫ g·V·[w·(∇×ω)]  is INDEFINITE
    (linear in each of V, w, ω ⇒ unbounded below). The conserve-and-transfer arm
    (`photon_deplete=True`) DETONATES (`H_bel −4107`); the bounded arm transfers
    ~2 % and is inert (`research/2026-06-10_graft-v4-photon-helicity_result.md` §6).
  • The named escape (graft-v4 §9, 2nd bullet): "a BOUNDED, helicity-TRANSFERRING
    coupling — norm-preserving H_photon↔H_bel exchange ... an orthogonal field-space
    rotation à la the crystal_engine converter, rather than a trilinear potential."

THE ESCAPE REALIZED HERE.  A circulator / gyrator is a NON-RECIPROCAL, LOSSLESS
element whose coupling is ANTISYMMETRIC/SKEW. Formulate the coupling NOT as a
potential V-term but as a SKEW-HERMITIAN GENERATOR on the two mode AMPLITUDES:

    d/dt [a_bulk; a_shear] = -i H [a_bulk; a_shear],     H Hermitian,

        H = [[ ω_b      ,  -i Ω(χ) ],
             [ +i Ω(χ)* ,   ω_s     ]]

The OFF-DIAGONAL Ω is the circulator rate; e^{-iHt} is UNITARY ⇒
|a_bulk|² + |a_shear|² is conserved EXACTLY, regardless of depletion — there is no
indefinite-Hamiltonian pump because the generator is anti-Hermitian by construction,
not a trilinear potential. The non-reciprocity / circulation SENSE is sourced from
the I4₁32 lattice CHIRALITY (the sign of χ), the SAME handedness phase the idealized
S-matrix circulator carries (`node_2domain_nport.py`:376 `chiral_circulator_S`,
S = [[0, e^{+iθ}], [−e^{−iθ}, 0]]). This driver builds the TIME-DOMAIN GENERATOR
whose frequency-domain shadow is that S-matrix.

THE TWO MODES (pinned from the corpus, phase-space coordinates — A46 discipline):
  • a_bulk  = the A1 dilatation / BULK-COMPRESSION mode. Its |a_bulk|² IS the trapped
              bulk energy E_V = "the latent MASS" (crystal_engine.py:354). Real-space
              scalar V, longitudinal "3".
  • a_shear = the Cosserat micro-rotation POLOIDAL-CIRCULATION mode — the LOCAL
              (ω, π_ω) LC quadrature that IS the poloidal winding / the CHARGE "3"
              (crystal_graft_v4.py:46-47). PHASE-SPACE reactance pair, NOT the
              orthogonal global rigid rotation L_ω the previous INERT lock targeted.

The complex amplitude a = q + i·p/ω is the analytic-signal of an LC reactance pair
(q = displacement, p = momentum); |a|² = the mode energy / ω. The skew generator
rotates ENERGY between the two |a|², which is exactly the bounded, norm-preserving,
helicity-transferring exchange the trilinear potential could not deliver.

α-FREEDOM: the circulator RATE magnitude uses the topological converter
κ̃ = 6/5 = pq/(p+q) (`cross_sector_coupling.py`:23, α-FREE — NOT κ_chiral=1.2α);
the chirality PHASE uses θ_χ = 2π·ν_vac (ν_vac = 2/7, α-free, the same gyrotropic
phase as `node_2domain_nport.py`:473). No α-bearing literal enters any rate, energy,
or amplitude. CI-style guard: `assert_alpha_free()`.

FOUR GATES (each PASS/FAIL reported honestly; a circulator that ALSO fails on the
winding CLOSES Fork-A as ISOLATION — a real, valuable negative):
  (A) CONSERVE      — |a_bulk|²+|a_shear|² conserved to machine precision; no pump.
  (B) TRANSFER      — energy actually FLOWS bulk↔shear; transfer-fraction ≫ 2 %.
  (C) LOCK-ON-WIND  — the coupling acts on the POLOIDAL WINDING amplitude (charge
                      mode), and coupling-ON differs from coupling-OFF ON THAT
                      observable (else it is the same inert failure).
  (D) MOTION→MASS   — bulk-compression energy (mass) scales with the shear
                      CIRCULATION RATE (more circulation ⇒ more trapped compression
                      ⇒ more effective mass), winding (charge) fixed.

SELF-SKEPTICAL DISCIPLINE: every gate guards against the way the previous efforts
FOOLED THEMSELVES — INERT-LOCK (ON≡OFF on the winding), TAUTOLOGICAL-TRANSFER
(closure identity not a measured flow), VACUOUS-CONSERVATION (norm conserved because
the coupling does nothing), and FORCED-vs-IMPOSED (is the non-reciprocity FORCED by
the chiral lattice or IMPOSED by hand?).

Driver: research/2026-06-20_node-circulator-coupling.md
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np

# ── canonical, α-free constants only ────────────────────────────────────────
from ave.core.constants import NU_VAC, M_E, C_0, HBAR
from ave.core.cross_sector_coupling import KAPPA_TILDE  # 6/5 = pq/(p+q), α-free

_OUT = Path(__file__).resolve().parent / "_output" / "node_circulator_coupling.json"


# ═════════════════════════════════════════════════════════════════════════════
# 0.  α-FREEDOM GUARD  (no α-bearing literal in any rate / energy / amplitude)
# ═════════════════════════════════════════════════════════════════════════════
def assert_alpha_free() -> None:
    """HALT if any α-bearing canonical symbol leaked into the engine constants
    this driver uses. κ̃=6/5 topology + θ_χ=2π·ν_vac (ν_vac=2/7) are the ONLY
    coupling inputs; both are α-free. (Mirrors the graft-v* CI gates.)"""
    # κ̃ must be the topological 6/5 = pq/(p+q), NOT κ_chiral = 1.2·α.
    if not np.isclose(KAPPA_TILDE, 6.0 / 5.0, rtol=0, atol=1e-15):
        raise AssertionError(f"κ̃={KAPPA_TILDE} is not the α-free 6/5 topology")
    # The chirality phase is θ_χ = 2π·ν_vac with ν_vac = 2/7 (α-free).
    if not np.isclose(NU_VAC, 2.0 / 7.0, rtol=0, atol=1e-15):
        raise AssertionError(f"ν_vac={NU_VAC} is not the α-free 2/7")
    # κ̃ ≈ 1.2 numerically COINCIDES with κ_chiral=1.2α·(1/α)? No — guard the
    # actual α-taint: 1.2·α ≈ 8.76e-3 ≪ 1, so κ̃=1.2 cannot be the α-biased value.
    from ave.core.constants import ALPHA
    kappa_chiral_alpha = 1.2 * ALPHA
    if np.isclose(KAPPA_TILDE, kappa_chiral_alpha, rtol=1e-6):
        raise AssertionError("κ̃ collapsed onto the α-tainted κ_chiral=1.2α")


# The two α-free coupling inputs, named once.
THETA_CHI: float = 2.0 * np.pi * NU_VAC  # chirality phase, = node_2domain_nport.py:473
KAPPA_RATE: float = KAPPA_TILDE          # topological converter rate scale, α-free


# ═════════════════════════════════════════════════════════════════════════════
# 1.  THE SKEW-HERMITIAN GENERATOR  (the circulator, NOT a potential)
# ═════════════════════════════════════════════════════════════════════════════
def circulator_generator(
    omega_b: float, omega_s: float, rate: float, chi: int
) -> np.ndarray:
    """The 2×2 HERMITIAN generator with a chirality-sourced SKEW off-diagonal.

        H = [[ ω_b              ,  Ω·e^{+i·χ·θ_χ} ],
             [ Ω·e^{-i·χ·θ_χ}   ,  ω_s            ]]

    where Ω = rate is the circulator coupling rate and χ ∈ {+1, −1, 0} is the
    lattice handedness (matter / antimatter / achiral). H is Hermitian
    (H = H†) so e^{-iHt} is UNITARY — the energy/norm |a_b|²+|a_s|² is conserved
    EXACTLY for ANY ω_b, ω_s, Ω. This is the crux: there is no indefinite
    potential, the generator is anti-Hermitian-by-construction.

    THE NON-RECIPROCITY: the off-diagonal carries the chirality PHASE χ·θ_χ
    (θ_χ = 2π·ν_vac). The instantaneous coupling H_bs = Ω·e^{+iχθ_χ} vs
    H_sb = Ω·e^{-iχθ_χ} differ by the SIGN of the phase — the gyrotropic phase
    a circulator routes power around. When ωᵦ ≠ ωₛ this phase makes the
    transfer DIRECTION (which mode fills first) chirality-dependent. χ=0 ⇒
    real off-diagonal ⇒ reciprocal Rabi flop (no preferred direction). The
    phase here is the time-domain GENERATOR whose unitary S-matrix shadow is
    `node_2domain_nport.py`:376  S = [[0, e^{+iθ}], [−e^{−iθ}, 0]].
    """
    if chi not in (-1, 0, 1):
        raise ValueError("chi must be -1, 0, or +1 (handedness selector)")
    phase = chi * THETA_CHI
    off = rate * np.exp(1j * phase)
    H = np.array(
        [[omega_b, off], [np.conj(off), omega_s]],
        dtype=complex,
    )
    # Hermiticity is the load-bearing property — assert it.
    assert np.allclose(H, H.conj().T), "generator is not Hermitian"
    return H


def _propagator(H: np.ndarray, dt: float) -> np.ndarray:
    """Exact 2×2 unitary propagator U = e^{-iHdt} via eigen-decomposition
    (H Hermitian ⇒ U unitary to machine precision — no Trotter error)."""
    evals, evecs = np.linalg.eigh(H)
    phases = np.exp(-1j * evals * dt)
    return evecs @ np.diag(phases) @ evecs.conj().T


def evolve(a0: np.ndarray, H: np.ndarray, dt: float, n_steps: int) -> np.ndarray:
    """Unitary trajectory a_k = U^k a0, U = e^{-iHdt}. Returns shape
    (n_steps+1, 2) complex amplitudes [a_bulk, a_shear] at each step."""
    U = _propagator(H, dt)
    traj = np.empty((n_steps + 1, 2), dtype=complex)
    a = np.asarray(a0, dtype=complex).copy()
    traj[0] = a
    for k in range(1, n_steps + 1):
        a = U @ a
        traj[k] = a
    return traj


def mode_energies(traj: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """|a_bulk|² (∝ trapped bulk / MASS energy) and |a_shear|² (∝ poloidal
    winding / CHARGE-circulation energy) along the trajectory."""
    return np.abs(traj[:, 0]) ** 2, np.abs(traj[:, 1]) ** 2


# ═════════════════════════════════════════════════════════════════════════════
# GATE A — CONSERVE
# ═════════════════════════════════════════════════════════════════════════════
def gate_A_conserve(
    omega_b: float = 1.0,
    omega_s: float = 1.3,
    rate: float = 0.3,
    chi: int = +1,
    dt: float = 0.05,
    n_steps: int = 40000,
) -> dict:
    """GATE A — CONSERVE.  Unitary evolution ⇒ N = |a_b|²+|a_s|² conserved to
    machine precision over a LONG run, and |L|/H bounded (no pump). Axiom-3
    lossless. This is conservation BY CONSTRUCTION — Gate B proves it is not
    VACUOUS (energy genuinely exchanges).

    'pump' = secular growth of total norm. We start from a generic (both modes
    loaded, random phase) state, evolve long, and report (i) max norm drift,
    (ii) the late-time linear slope of N(t) (a pump would have slope ≫ 0)."""
    rng = np.random.default_rng(7)
    a0 = rng.standard_normal(2) + 1j * rng.standard_normal(2)
    H = circulator_generator(omega_b, omega_s, rate, chi)
    traj = evolve(a0, H, dt, n_steps)
    nb, ns = mode_energies(traj)
    N = nb + ns
    norm_drift = float(np.max(np.abs(N - N[0])))
    # late-time slope of N(t) — the pump signature (per-step). Fit last 25 %.
    tail = N[int(0.75 * len(N)):]
    t = np.arange(len(tail), dtype=float)
    slope = float(np.polyfit(t, tail, 1)[0])
    # |L|/H bounded: the off-diagonal "angular-momentum-like" current
    # j(t) = 2·Im(a_b* a_s) — its max amplitude relative to N (must be O(1)).
    j = 2.0 * np.imag(np.conj(traj[:, 0]) * traj[:, 1])
    j_over_N = float(np.max(np.abs(j)) / N[0])
    passed = (norm_drift < 1e-9) and (abs(slope) < 1e-12) and (j_over_N < 2.0)
    return {
        "norm_drift": norm_drift,
        "late_slope_per_step": slope,
        "j_over_N_max": j_over_N,
        "N_initial": float(N[0]),
        "n_steps": n_steps,
        "passed": bool(passed),
        "verdict": "PASS — norm conserved to machine precision, no pump"
        if passed
        else "FAIL — pump / norm drift detected",
    }


# ═════════════════════════════════════════════════════════════════════════════
# GATE B — TRANSFER
# ═════════════════════════════════════════════════════════════════════════════
def gate_B_transfer(
    omega_b: float = 1.0,
    omega_s: float = 1.0,
    rate: float = 0.3,
    chi: int = +1,
    dt: float = 0.05,
    n_steps: int = 40000,
) -> dict:
    """GATE B — TRANSFER.  Load energy into the BULK mode ONLY (a_shear(0)=0);
    measure how much energy FLOWS into the shear mode. The transfer fraction is
    max_t |a_shear(t)|² / N — a MEASURED energy flow between INDEPENDENT channels
    (not a closure identity: a_shear starts EMPTY, so any |a_shear|²>0 is energy
    that physically arrived from a_bulk through the off-diagonal). This guards
    the TAUTOLOGICAL-TRANSFER failure mode (graft-v4's radiated≔closure bin).

    Must be ≫ the failed 2 %. For a 2-mode skew rotation the max transfer is
        f_max = Ω² / (Ω² + Δ²/4),    Δ = ω_b − ω_s   (Rabi formula),
    so RESONANT (Δ=0) ⇒ 100 % complete sloshing; detuned ⇒ throttled. We report
    both the resonant and a detuned case so the throttling mechanism is explicit.
    """
    a0 = np.array([1.0 + 0j, 0.0 + 0j])  # bulk loaded, shear EMPTY
    H = circulator_generator(omega_b, omega_s, rate, chi)
    traj = evolve(a0, H, dt, n_steps)
    nb, ns = mode_energies(traj)
    N0 = nb[0] + ns[0]
    transfer_frac = float(np.max(ns) / N0)
    # Rabi prediction (analytic, independent of the integrator) — validate-on-known.
    Delta = omega_b - omega_s
    f_rabi = rate**2 / (rate**2 + (Delta / 2.0) ** 2)
    rabi_match = bool(np.isclose(transfer_frac, f_rabi, rtol=1e-3, atol=1e-3))
    # the shear mode genuinely OSCILLATES (Rabi flop) — count zero-up-crossings
    # of ns − ns.mean() as a non-vacuity witness (it is not a static offset).
    centered = ns - ns.mean()
    sign = np.sign(centered)
    crossings = int(np.sum((sign[:-1] < 0) & (sign[1:] >= 0)))
    passed = (transfer_frac > 0.5) and rabi_match and (crossings >= 1)
    return {
        "transfer_fraction": transfer_frac,
        "vs_failed_2pct": f"{transfer_frac/0.02:.0f}x the failed 2%",
        "rabi_prediction": float(f_rabi),
        "rabi_match": rabi_match,
        "shear_oscillation_crossings": crossings,
        "Delta_detuning": float(Delta),
        "passed": bool(passed),
        "verdict": "PASS — energy flows bulk->shear, matches Rabi, oscillates"
        if passed
        else "FAIL — no real transfer / not a measured flow",
    }


def transfer_vs_detuning(
    rate: float = 0.3, chi: int = +1, dt: float = 0.05, n_steps: int = 60000
) -> list[dict]:
    """Sweep the bulk-shear detuning Δ = ω_b − ω_s; the transfer fraction must
    follow the Rabi throttle Ω²/(Ω²+Δ²/4). This is the load-bearing mechanism
    for Gate D (motion→mass): detuning is set by the operating point."""
    omega_b = 1.0
    rows = []
    for Delta in [0.0, 0.2, 0.5, 1.0, 2.0]:
        omega_s = omega_b - Delta
        a0 = np.array([1.0 + 0j, 0.0 + 0j])
        H = circulator_generator(omega_b, omega_s, rate, chi)
        traj = evolve(a0, H, dt, n_steps)
        _, ns = mode_energies(traj)
        f = float(np.max(ns))
        f_rabi = rate**2 / (rate**2 + (Delta / 2.0) ** 2)
        rows.append(
            {"Delta": float(Delta), "transfer_frac": f, "rabi": float(f_rabi),
             "match": bool(np.isclose(f, f_rabi, rtol=2e-2, atol=2e-3))}
        )
    return rows


# ═════════════════════════════════════════════════════════════════════════════
# GATE C — LOCK-ON-WINDING (ON vs OFF)
# ═════════════════════════════════════════════════════════════════════════════
def gate_C_lock_on_winding(*args, **kwargs):
    raise NotImplementedError


# ═════════════════════════════════════════════════════════════════════════════
# GATE D — MOTION → MASS
# ═════════════════════════════════════════════════════════════════════════════
def gate_D_motion_to_mass(*args, **kwargs):
    raise NotImplementedError


# ═════════════════════════════════════════════════════════════════════════════
# FORCED-vs-IMPOSED verdict
# ═════════════════════════════════════════════════════════════════════════════
def forced_vs_imposed(*args, **kwargs):
    raise NotImplementedError


# ═════════════════════════════════════════════════════════════════════════════
# VALIDATE-ON-KNOWN
# ═════════════════════════════════════════════════════════════════════════════
def validate_on_known() -> dict:
    raise NotImplementedError


# ═════════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════════
def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
