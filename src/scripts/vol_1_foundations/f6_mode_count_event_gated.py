#!/usr/bin/env python3
"""F6 mode-count Arm A — event-gated occupancy → multi-mode bath + V-phase couple.

Freeze: research/2026-07-16_f6-mode-count-event-gated_prereg_FROZEN.md
Charter: research/2026-07-15_f6-mode-count-door_CHARTER.md

SCOPE NOTE (2026-07-16): classify bins are frozen in this file; knobs match
prereg §4. Does not claim CHANNEL-BOUNDED a priori. Not Re(Z) absorb.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np

from ave.core.k4_tlm import K4Lattice3D

# --- frozen tolerances (prereg §4) ---
TOL_SOFT_LEDGER_FRAC = 0.5
DETONATE_FLOOR = 1e6
BIAS_TOL = 5e-3
DRAIN_TOL = 0.05
NULL_FLOOR = 1e-12
MODE_FLOOR = 1e-15
OCC_THRESH = 0.35
PACKET = 0.08
N_SPREAD = 4
M_MODES = 64
KAPPA = 1.0
N_STEPS = 150
N = 12
CORE_R = 2.5
SEED = 1


@dataclass
class RunOut:
    E_bath: float
    E_field_final: float
    E_field_initial: float
    E_core_final: float
    E_core_initial: float
    soft_ledger: float
    mean_S_core: float
    N_occ_initial: int
    N_occ_final: int
    n_events: int
    detonated: bool
    finite: bool


def _protect_mask(lat: K4Lattice3D, center, radius: float) -> np.ndarray:
    ii, jj, kk = np.indices((lat.nx, lat.ny, lat.nz))
    c = np.array(center)
    r2 = (ii - c[0]) ** 2 + (jj - c[1]) ** 2 + (kk - c[2]) ** 2
    return (r2 <= radius**2) & lat.mask_active


def _seed(lat: K4Lattice3D, center, rng: np.random.Generator) -> None:
    ii, jj, kk = np.indices((lat.nx, lat.ny, lat.nz))
    env = np.exp(
        -((ii - center[0]) ** 2 + (jj - center[1]) ** 2 + (kk - center[2]) ** 2) / (2 * 1.2**2)
    )
    env[~lat.mask_active] = 0.0
    for p in range(4):
        lat.V_inc[..., p] += 0.08 * env / 2.0
    field = np.zeros_like(lat.V_inc)
    for _ in range(8):
        kv = rng.integers(1, lat.nx // 2, size=3) * (2 * np.pi / lat.nx) * rng.choice([-1, 1], size=3)
        phase = rng.uniform(0, 2 * np.pi)
        pw = np.cos(kv[0] * ii + kv[1] * jj + kv[2] * kk + phase)
        portw = rng.normal(size=4)
        for p in range(4):
            field[..., p] += 0.03 * pw * portw[p]
    field[~lat.mask_active] = 0.0
    lat.V_inc += field


def _mean_S(lat: K4Lattice3D, mask: np.ndarray) -> float:
    dens = lat.get_energy_density()
    peak = dens[mask].max() if np.any(mask) else 0.0
    a2 = np.clip(dens[mask] / (peak + 1e-30), 0.0, 1.0 - 1e-12)
    if a2.size == 0:
        return 1.0
    return float(np.mean(np.sqrt(1.0 - a2)))


def _n_occ(bath_modes: np.ndarray) -> int:
    return int(np.count_nonzero(bath_modes > MODE_FLOOR))


def _credit_modes(bath_modes: np.ndarray, delta: float) -> None:
    """Spread δ across N_SPREAD lowest-occupied slots (mode-count can rise)."""
    if delta <= 0.0:
        return
    order = np.argsort(bath_modes)
    take = order[:N_SPREAD]
    bath_modes[take] += delta / float(N_SPREAD)


def _phase_scramble(lat: K4Lattice3D, gated: np.ndarray, rng: np.random.Generator) -> None:
    """Energy-preserving port-phase scramble on gated sites (V-phase couple)."""
    if not np.any(gated):
        return
    # Per-port random signs — preserves Σ_p V_p² sitewise.
    signs = rng.choice([-1.0, 1.0], size=(int(np.count_nonzero(gated)), 4))
    for arr in (lat.V_inc, lat.V_ref):
        block = arr[gated]
        arr[gated] = block * signs


def _arm_a_transfer(
    lat: K4Lattice3D,
    unprot: np.ndarray,
    bath_modes: np.ndarray,
    rng: np.random.Generator,
    *,
    kappa: float,
    credit_modes: bool = True,
) -> tuple[float, int]:
    """Event-gated packet remove + optional mode credit + phase scramble.

    Returns (delta_energy, n_events). credit_modes=False is the FRICTION-RENAMED
    sabotage plant (scalar drain without mode fill).
    """
    if kappa <= 0.0:
        return 0.0, 0
    dens = lat.get_energy_density()
    dens_u = dens.copy()
    dens_u[~unprot] = 0.0
    peak = float(dens_u.max()) if np.any(unprot) else 0.0
    if peak <= 0.0:
        return 0.0, 0
    occ = dens_u / (peak + 1e-30)
    gated = unprot & (occ >= OCC_THRESH)
    if not np.any(gated):
        return 0.0, 0

    # Packet energy from gated sites
    delta_field = dens.copy()
    delta_field[~gated] = 0.0
    delta_field[gated] = np.minimum(PACKET * dens[gated], dens[gated] * 0.5)
    delta = float(delta_field.sum())
    if delta <= 0.0:
        return 0.0, 0

    E_g = float(dens[gated].sum())
    if E_g <= 0.0:
        return 0.0, 0
    scale = float(np.sqrt(max(1.0 - delta / E_g, 0.0)))
    for arr in (lat.V_inc, lat.V_ref):
        arr[gated] *= scale

    if credit_modes:
        _credit_modes(bath_modes, delta)
    # else: sabotage — energy removed, no mode credit (caller tracks scalar)

    _phase_scramble(lat, gated, rng)
    return delta, int(np.count_nonzero(gated))


def run_once(
    *,
    kappa: float,
    seed: int = SEED,
    n_steps: int = N_STEPS,
    credit_modes: bool = True,
) -> RunOut:
    lat = K4Lattice3D(N, N, N, nonlinear=True, op3_bond_reflection=True, V_SNAP=1.0)
    center = (N // 2, N // 2, N // 2)
    core = _protect_mask(lat, center, CORE_R)
    unprot = lat.mask_active & ~core
    rng = np.random.default_rng(seed)
    _seed(lat, center, rng)

    bath_modes = np.zeros(M_MODES, dtype=float)
    scalar_bath = 0.0  # used only when credit_modes=False
    n_occ0 = _n_occ(bath_modes)

    E0 = float(lat.total_energy())
    E_core0 = float(lat.get_energy_density()[core].sum())
    detonated = False
    finite = True
    S_acc = 0.0
    n_events = 0
    E_removed = 0.0

    for _ in range(n_steps):
        lat.step()
        d, ne = _arm_a_transfer(
            lat, unprot, bath_modes, rng, kappa=kappa, credit_modes=credit_modes
        )
        if credit_modes:
            pass  # energy already in bath_modes
        else:
            scalar_bath += d
        E_removed += d
        n_events += ne
        Et = float(lat.total_energy())
        S_acc += _mean_S(lat, core)
        if not np.isfinite(Et):
            finite = False
            detonated = True
            break
        if abs(Et) > DETONATE_FLOOR:
            detonated = True
            break

    Ef = float(lat.total_energy())
    E_core_f = float(lat.get_energy_density()[core].sum())
    E_bath = float(bath_modes.sum()) if credit_modes else float(scalar_bath)
    n_occ_f = _n_occ(bath_modes)
    soft = abs((E0 - Ef) - E_bath)
    return RunOut(
        E_bath=E_bath,
        E_field_final=Ef,
        E_field_initial=E0,
        E_core_final=E_core_f,
        E_core_initial=E_core0,
        soft_ledger=soft,
        mean_S_core=S_acc / max(n_steps, 1),
        N_occ_initial=n_occ0,
        N_occ_final=n_occ_f,
        n_events=n_events,
        detonated=detonated,
        finite=finite,
    )


def classify(on: RunOut, off: RunOut) -> str:
    if on.detonated or not on.finite:
        return "DETONATE"
    if on.E_bath < NULL_FLOOR:
        return "NULL"
    dN = on.N_occ_final - on.N_occ_initial
    if dN < 1:
        return "FRICTION-RENAMED"
    if abs(on.mean_S_core - off.mean_S_core) > BIAS_TOL:
        return "BIAS-MOVED"
    if off.E_core_final > 0:
        rel = (off.E_core_final - on.E_core_final) / off.E_core_final
        if rel > DRAIN_TOL:
            return "ELECTRON-DRAIN"
    if on.soft_ledger > TOL_SOFT_LEDGER_FRAC * max(on.E_field_initial, 1e-12):
        return "DETONATE"
    return "CHANNEL-BOUNDED"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--json", action="store_true")
    p.add_argument(
        "--sabotage-friction",
        action="store_true",
        help="credit scalar bath only (FRICTION-RENAMED plant)",
    )
    args = p.parse_args()
    credit = not args.sabotage_friction
    off = run_once(kappa=0.0, seed=SEED, credit_modes=True)
    on = run_once(kappa=KAPPA, seed=SEED, credit_modes=credit)
    verdict = classify(on, off)
    payload = {"verdict": verdict, "on": on.__dict__, "off": off.__dict__, "credit_modes": credit}
    if args.json:
        import json

        print(json.dumps(payload, indent=2, default=float))
    else:
        print(f"VERDICT = {verdict}")
        print(
            f"  ON  bath={on.E_bath:.6e} field={on.E_field_final:.6e} "
            f"core={on.E_core_final:.6e} N_occ={on.N_occ_final} events={on.n_events}"
        )
        print(
            f"  OFF bath={off.E_bath:.6e} field={off.E_field_final:.6e} "
            f"core={off.E_core_final:.6e}"
        )
        print(
            f"  soft_ledger={on.soft_ledger:.3e}  "
            f"ΔS_core={on.mean_S_core - off.mean_S_core:.3e}  "
            f"ΔN_occ={on.N_occ_final - on.N_occ_initial}"
        )


if __name__ == "__main__":
    main()
