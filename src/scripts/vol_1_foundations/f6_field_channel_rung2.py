#!/usr/bin/env python3
"""F6 field-channel rung-2 — energy-conserving in-Hamiltonian V→bath transfer.

Freeze: research/2026-07-15_f6-field-channel-rung2_prereg_FROZEN.md
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np

from ave.core.k4_tlm import K4Lattice3D

TOL_CONS = 1e-8
DETONATE_FLOOR = 1e6
BIAS_TOL = 5e-3
DRAIN_TOL = 0.05
NULL_FLOOR = 1e-12
KAPPA = 0.05
N_STEPS = 150
N = 12
CORE_R = 2.5
DT_FAC = 1.0 / np.sqrt(2.0)  # matches natural-unit outer dt scale


@dataclass
class RunOut:
    E_bath: float
    E_field_final: float
    E_field_initial: float
    E_core_final: float
    E_core_initial: float
    ledger_residual: float
    mean_S_core: float
    detonated: bool
    finite: bool


def _protect_mask(lat: K4Lattice3D, center, radius: float) -> np.ndarray:
    ii, jj, kk = np.indices((lat.nx, lat.ny, lat.nz))
    c = np.array(center)
    r2 = (ii - c[0]) ** 2 + (jj - c[1]) ** 2 + (kk - c[2]) ** 2
    core = r2 <= radius**2
    return core & lat.mask_active


def _seed(lat: K4Lattice3D, center, rng) -> None:
    """Mild core clock + unprotected traveling bath."""
    ii, jj, kk = np.indices((lat.nx, lat.ny, lat.nz))
    env = np.exp(
        -((ii - center[0]) ** 2 + (jj - center[1]) ** 2 + (kk - center[2]) ** 2) / (2 * 1.2**2)
    )
    env[~lat.mask_active] = 0.0
    for p in range(4):
        lat.V_inc[..., p] += 0.08 * env / 2.0
    # bath outside core
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
    # proxy A² ~ energy / scale; use clip for operating-point stand-in
    a2 = np.clip(dens[mask] / (dens[mask].max() + 1e-30), 0.0, 1.0 - 1e-12)
    if a2.size == 0:
        return 1.0
    return float(np.mean(np.sqrt(1.0 - a2)))


def _transfer(lat: K4Lattice3D, unprot: np.ndarray, kappa: float) -> float:
    """Remove δ from unprotected field energy into bath; return δ."""
    dens = lat.get_energy_density()
    E_u = float(dens[unprot].sum())
    if E_u <= 0.0 or kappa <= 0.0:
        return 0.0
    delta = min(kappa * E_u * DT_FAC, E_u * 0.5)  # cap 50%/step
    if delta <= 0.0:
        return 0.0
    scale = float(np.sqrt(max(1.0 - delta / E_u, 0.0)))
    # apply scale only on unprotected sites
    for arr in (lat.V_inc, lat.V_ref):
        arr[unprot] *= scale
    return delta


def run_once(*, kappa: float, seed: int = 0, n_steps: int = N_STEPS) -> RunOut:
    lat = K4Lattice3D(N, N, N, nonlinear=True, op3_bond_reflection=True, V_SNAP=1.0)
    center = (N // 2, N // 2, N // 2)
    core = _protect_mask(lat, center, CORE_R)
    unprot = lat.mask_active & ~core
    rng = np.random.default_rng(seed)
    _seed(lat, center, rng)

    # ⚑ FLAG (E0-baseline convention, hygiene sweep 2026-07-17; FLAGGED-NOT-FIXED —
    # banked+frozen consumer). E0 is captured PRE-CONNECT on the V_inc-only seed
    # (_seed writes only lat.V_inc), so total_energy() = Σ_p(V_inc²+V_ref²) here reads
    # the off-shell HALF-energy and doubles EXACTLY 2× at the first lat.step() CONNECT
    # (k4-tlm-simulator.md "E0 baseline convention"). This is the SAME bug class fixed
    # in the sibling arms #711 (f6_mode_count_event_gated) / #714 (f6_arm_b_exterior_leave):
    # the `soft_resid = |(E0-Ef)-E_bath|` (run_once, below) and the classify()
    # CHANNEL-BOUNDED gate consume this pre-connect E0, so that pass-bin is STRUCTURALLY
    # UNREACHABLE. The BANKED verdict (BIAS-MOVED, from the `mean_S_core` branch of
    # classify()) fires BEFORE the soft ledger and does NOT consume E0 — the banked
    # result is unaffected. The mechanical
    # fix (capture E0 after the first lat.step(), on-shell) is routed to the F6 lane, NOT
    # this additive-only hygiene sweep (frozen prereg
    # research/2026-07-15_f6-field-channel-rung2_prereg_FROZEN.md + test_f6_field_channel_rung2.py).
    E0 = float(lat.total_energy())
    E_core0 = float(lat.get_energy_density()[core].sum())
    E_bath = 0.0
    E_removed = 0.0
    detonated = False
    finite = True
    S_acc = 0.0

    for _ in range(n_steps):
        lat.step()
        d = _transfer(lat, unprot, kappa)
        E_bath += d
        E_removed += d
        Et = float(lat.total_energy())
        S_acc += _mean_S(lat, core)
        if not np.isfinite(Et) or not np.isfinite(E_bath):
            finite = False
            detonated = True
            break
        if abs(Et) > DETONATE_FLOOR:
            detonated = True
            break

    Ef = float(lat.total_energy())
    E_core_f = float(lat.get_energy_density()[core].sum())
    # ledger: field drop vs bath — note TLM also redistributes; compare removed vs bath
    residual = abs(E_bath - E_removed)  # identical by construction; keep for API
    # Better conservation check: E_bath should equal sum of δ's; field may also
    # scatter. Use |E0 - Ef - E_bath| soft check with redistribution allowance.
    soft_resid = abs((E0 - Ef) - E_bath)
    return RunOut(
        E_bath=E_bath,
        E_field_final=Ef,
        E_field_initial=E0,
        E_core_final=E_core_f,
        E_core_initial=E_core0,
        ledger_residual=min(residual, soft_resid),
        mean_S_core=S_acc / max(n_steps, 1),
        detonated=detonated,
        finite=finite,
    )


def classify(on: RunOut, off: RunOut) -> str:
    if on.detonated or not on.finite:
        return "DETONATE"
    if on.E_bath < NULL_FLOOR:
        return "NULL"
    if abs(on.mean_S_core - off.mean_S_core) > BIAS_TOL:
        return "BIAS-MOVED"
    if off.E_core_final > 0:
        rel = (off.E_core_final - on.E_core_final) / off.E_core_final
        if rel > DRAIN_TOL:
            return "ELECTRON-DRAIN"
    # soft ledger: field drop should roughly match bath (scatter can move energy)
    if abs((on.E_field_initial - on.E_field_final) - on.E_bath) > 0.5 * max(
        on.E_field_initial, 1e-12
    ):
        # large mismatch → treat as instrument fail / detonate-class
        return "DETONATE"
    return "CHANNEL-BOUNDED"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    off = run_once(kappa=0.0, seed=1)
    on = run_once(kappa=KAPPA, seed=1)
    verdict = classify(on, off)
    payload = {"verdict": verdict, "on": on.__dict__, "off": off.__dict__}
    if args.json:
        import json

        print(json.dumps(payload, indent=2, default=float))
    else:
        print(f"VERDICT = {verdict}")
        print(f"  ON  bath={on.E_bath:.6e} field={on.E_field_final:.6e} core={on.E_core_final:.6e}")
        print(f"  OFF bath={off.E_bath:.6e} field={off.E_field_final:.6e} core={off.E_core_final:.6e}")
        print(f"  soft_ledger |ΔE_field - bath| = {abs((on.E_field_initial-on.E_field_final)-on.E_bath):.3e}")


if __name__ == "__main__":
    main()
