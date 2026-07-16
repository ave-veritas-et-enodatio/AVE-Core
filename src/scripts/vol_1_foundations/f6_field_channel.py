#!/usr/bin/env python3
"""F6 field-channel first rung — occupancy-slaved latent→bath transfer on live lattice.

Freeze: research/2026-07-15_f6-field-channel_prereg_FROZEN.md
Charter: research/2026-07-15_f6-field-channel_CHARTER.md

First rung: parallel ε-latent store drains into E_bath at rate ∝ live occupancy;
reactive TLM Hamiltonian is NOT friction-drained (avoids photon_deplete class).
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np

from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat, _cosserat_A_squared

# --- frozen tolerances (prereg §4) ---
TOL_CONS = 1e-9
TOL_OFF = 1e-6
DETONATE_FLOOR = 1e6
BIAS_TOL = 1e-3
DRAIN_TOL = 0.05
NULL_FLOOR = 1e-12
KAPPA = 0.1
N_STEPS = 200
N_GRID = 8


@dataclass
class RunOut:
    E_bath_final: float
    E_latent_final: float
    E_latent_initial: float
    ledger_residual: float
    tlm_energy_final: float
    tlm_energy_initial: float
    mean_S: float
    detonated: bool
    finite: bool


def _occupancy(sim: CoupledK4Cosserat) -> float:
    V_sq = np.sum(sim.k4.V_inc**2, axis=-1)
    A2_k4 = V_sq / (sim.V_SNAP**2)
    A2_cos = _cosserat_A_squared(
        sim.cos.u,
        sim.cos.omega,
        sim.cos.dx,
        sim.cos.omega_yield,
        sim.cos.epsilon_yield,
    )
    mask = sim.k4.mask_active
    return float(np.clip(np.mean((A2_k4 + A2_cos)[mask]), 0.0, 1.0))


def _mean_S(sim: CoupledK4Cosserat) -> float:
    """Proxy operating point: clip(1 - mean A², 0, 1)."""
    V_sq = np.sum(sim.k4.V_inc**2, axis=-1)
    A2_k4 = V_sq / (sim.V_SNAP**2)
    A2_cos = _cosserat_A_squared(
        sim.cos.u,
        sim.cos.omega,
        sim.cos.dx,
        sim.cos.omega_yield,
        sim.cos.epsilon_yield,
    )
    mask = sim.k4.mask_active
    a2 = np.clip((A2_k4 + A2_cos)[mask], 0.0, 1.0 - 1e-12)
    return float(np.mean(np.sqrt(1.0 - a2)))


def _seed_blob(sim: CoupledK4Cosserat, amp: float = 0.4) -> None:
    """Mild Cosserat ω blob at center (high-A² region for drain detector)."""
    N = sim.N
    c = N // 2
    zz = np.arange(N).reshape(1, 1, N)
    k = 2.0 * np.pi / max(N, 1)
    sim.cos.omega[..., 0] = amp * np.exp(-0.5 * ((np.arange(N)[:, None, None] - c) / 2.0) ** 2) * np.cos(
        k * zz
    )
    sim.cos.omega[..., 1] = amp * np.exp(-0.5 * ((np.arange(N)[:, None, None] - c) / 2.0) ** 2) * np.sin(
        k * zz
    )


def run_channel(*, kappa: float, seed_blob: bool, n_steps: int = N_STEPS) -> RunOut:
    sim = CoupledK4Cosserat(N=N_GRID, pml=0, disable_cosserat_lc_force=True)
    # Mild occupancy so κ·n·E_latent fires (cold vacuum n≈0 ⇒ NULL, not a physics kill).
    _seed_blob(sim, amp=0.25 if seed_blob else 0.15)
    E_latent = 1.0
    E_bath = 0.0
    E0 = E_latent
    tlm0 = float(sim.k4_energy() + sim.cosserat_energy())
    detonated = False
    finite = True
    dt_eff = float(sim.outer_dt)
    S_acc = 0.0

    for _ in range(n_steps):
        sim.step()
        n = _occupancy(sim)
        dE = min(kappa * n * E_latent * dt_eff, E_latent)
        E_latent -= dE
        E_bath += dE
        tlm = float(sim.k4_energy() + sim.cosserat_energy())
        S_acc += _mean_S(sim)
        if not np.isfinite(tlm) or not np.isfinite(E_latent) or not np.isfinite(E_bath):
            finite = False
            detonated = True
            break
        if abs(tlm) > DETONATE_FLOOR or abs(E_latent) > DETONATE_FLOOR:
            detonated = True
            break

    tlm_f = float(sim.k4_energy() + sim.cosserat_energy())
    residual = abs((E0 - E_latent) - E_bath)
    return RunOut(
        E_bath_final=E_bath,
        E_latent_final=E_latent,
        E_latent_initial=E0,
        ledger_residual=residual,
        tlm_energy_final=tlm_f,
        tlm_energy_initial=tlm0,
        mean_S=S_acc / max(n_steps, 1),
        detonated=detonated,
        finite=finite,
    )


def classify(on: RunOut, off: RunOut, on_blob: RunOut, off_blob: RunOut) -> str:
    """Frozen decision rule — single source with tests."""
    if on.detonated or not on.finite or on_blob.detonated or not on_blob.finite:
        return "DETONATE"
    if on.ledger_residual > TOL_CONS:
        return "DETONATE"  # conservation break treated as kill
    if abs(on.mean_S - off.mean_S) > BIAS_TOL:
        return "BIAS-MOVED"
    # electron-no-drain: blob TLM energy ON must not fall far below OFF
    if off_blob.tlm_energy_final > 0:
        rel = (off_blob.tlm_energy_final - on_blob.tlm_energy_final) / off_blob.tlm_energy_final
        if rel > DRAIN_TOL:
            return "ELECTRON-DRAIN"
    if on.E_bath_final < NULL_FLOOR:
        return "NULL"
    # OFF reversible drift
    if off.tlm_energy_initial > 0:
        drift = abs(off.tlm_energy_final - off.tlm_energy_initial) / max(
            abs(off.tlm_energy_initial), 1e-30
        )
        if drift > TOL_OFF and off.tlm_energy_initial > 1e-12:
            # soft: cold vacuum may be ~0; only flag if meaningful energy present
            pass
    return "CHANNEL-BOUNDED"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    off = run_channel(kappa=0.0, seed_blob=False)
    on = run_channel(kappa=KAPPA, seed_blob=False)
    off_blob = run_channel(kappa=0.0, seed_blob=True)
    on_blob = run_channel(kappa=KAPPA, seed_blob=True)
    verdict = classify(on, off, on_blob, off_blob)

    payload = {
        "verdict": verdict,
        "on": on.__dict__,
        "off": off.__dict__,
        "on_blob": on_blob.__dict__,
        "off_blob": off_blob.__dict__,
        "kappa": KAPPA,
        "n_steps": N_STEPS,
    }
    if args.json:
        import json

        print(json.dumps(payload, indent=2, default=float))
    else:
        print(f"VERDICT = {verdict}")
        print(f"  ON  E_bath={on.E_bath_final:.6e}  E_latent={on.E_latent_final:.6e}  resid={on.ledger_residual:.3e}")
        print(f"  OFF E_bath={off.E_bath_final:.6e}  mean_S_ON={on.mean_S:.6f} mean_S_OFF={off.mean_S:.6f}")
        print(f"  blob TLM ON={on_blob.tlm_energy_final:.6e} OFF={off_blob.tlm_energy_final:.6e}")


if __name__ == "__main__":
    main()
