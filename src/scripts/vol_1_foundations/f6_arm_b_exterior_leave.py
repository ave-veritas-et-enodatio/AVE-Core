#!/usr/bin/env python3
"""F6 mode-count Arm B — G0 face-port exterior leave → exterior multi-mode ledger.

Freeze: research/2026-07-16_f6-arm-b-exterior-leave_prereg_FROZEN.md
Charters: research/2026-07-15_f6-mode-count-door_CHARTER.md
          research/2026-07-16_f6-frontier-map_CHARTER.md

SCOPE NOTE (2026-07-16): classify bins frozen here; knobs match prereg §4.
G0 only — face ports are convenience, not orthogonal cosmology. Not Re(Z).
Even CHANNEL-BOUNDED does not claim DE lifecycle / F6 / crystallization.
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
    pml_thickness: int
    # Post-equilibration soft-ledger baseline (2026-07-16 fix). The V_inc-only
    # seed is not a valid V_inc/V_ref equilibrium; total energy settles after
    # step 1 (OFF: exactly 2·E0). The ledger must be booked vs this equilibrated
    # field, not the raw seed E0 (which produced the spurious ~3.73 "messy"
    # figure). Defaults to 0.0 so hand-built RunOut() fixtures fall back to
    # E_field_initial in classify().
    E_field_equil: float = 0.0


def _protect_mask(lat: K4Lattice3D, center, radius: float) -> np.ndarray:
    ii, jj, kk = np.indices((lat.nx, lat.ny, lat.nz))
    c = np.array(center)
    r2 = (ii - c[0]) ** 2 + (jj - c[1]) ** 2 + (kk - c[2]) ** 2
    return (r2 <= radius**2) & lat.mask_active


def _face_mask(lat: K4Lattice3D) -> np.ndarray:
    """Depth-1 box faces (G0 convenience — not normal-to-front cosmology)."""
    ii, jj, kk = np.indices((lat.nx, lat.ny, lat.nz))
    face = (
        (ii == 0)
        | (ii == lat.nx - 1)
        | (jj == 0)
        | (jj == lat.ny - 1)
        | (kk == 0)
        | (kk == lat.nz - 1)
    )
    return face & lat.mask_active


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
    """Peak-normalized density-CONTRAST statistic — NOT the Ax-4 saturation S.

    A² here is normalized by the in-mask PEAK density, so the hottest site
    always reads a2=1 (contrast S=0) at ANY amplitude. This is a
    profile-SHAPE contrast, NOT the canonical saturation S(A)=√(1−(A/A_yield)²)
    referenced to V_SNAP. Measured true core saturation stays S≥0.99
    (A²_max≈0.021 vs V_SNAP=1.0) — deep sub-yield — everywhere in the run.
    The BIAS-MOVED bin therefore gates a density-profile-shape change, not an
    absolute saturation-bias move. (Same `_mean_S` is verbatim in Arm A / #711;
    the relabel applies there too — cross-cite, do not touch that branch here.)
    """
    dens = lat.get_energy_density()
    peak = dens[mask].max() if np.any(mask) else 0.0
    a2 = np.clip(dens[mask] / (peak + 1e-30), 0.0, 1.0 - 1e-12)
    if a2.size == 0:
        return 1.0
    return float(np.mean(np.sqrt(1.0 - a2)))


def _n_occ(bath_modes: np.ndarray) -> int:
    return int(np.count_nonzero(bath_modes > MODE_FLOOR))


def _credit_modes(bath_modes: np.ndarray, delta: float) -> None:
    if delta <= 0.0:
        return
    order = np.argsort(bath_modes)
    take = order[:N_SPREAD]
    bath_modes[take] += delta / float(N_SPREAD)


def _arm_b_transfer(
    lat: K4Lattice3D,
    ports: np.ndarray,
    bath_modes: np.ndarray,
    *,
    kappa: float,
    credit_modes: bool = True,
) -> tuple[float, int]:
    """Face-port packet remove + optional exterior mode credit.

    Returns (delta_energy, n_port_sites). credit_modes=False is the
    FRICTION-RENAMED sabotage plant (scalar leave without mode fill).
    """
    if kappa <= 0.0:
        return 0.0, 0
    dens = lat.get_energy_density()
    dens_p = dens.copy()
    dens_p[~ports] = 0.0
    if float(dens_p.max()) <= 0.0:
        return 0.0, 0

    active_ports = ports & (dens > 0.0)
    if not np.any(active_ports):
        return 0.0, 0

    delta_field = dens.copy()
    delta_field[~active_ports] = 0.0
    delta_field[active_ports] = np.minimum(PACKET * dens[active_ports], dens[active_ports] * 0.5)
    delta = float(delta_field.sum())
    if delta <= 0.0:
        return 0.0, 0

    E_p = float(dens[active_ports].sum())
    if E_p <= 0.0:
        return 0.0, 0
    scale = float(np.sqrt(max(1.0 - delta / E_p, 0.0)))
    # Prefer outgoing V_ref scale; keep V_inc consistent for soft ledger.
    lat.V_ref[active_ports] *= scale
    lat.V_inc[active_ports] *= scale

    if credit_modes:
        _credit_modes(bath_modes, delta)

    return delta, int(np.count_nonzero(active_ports))


def run_once(
    *,
    kappa: float,
    seed: int = SEED,
    n_steps: int = N_STEPS,
    credit_modes: bool = True,
    pml_thickness: int = 0,
) -> RunOut:
    lat = K4Lattice3D(
        N,
        N,
        N,
        nonlinear=True,
        op3_bond_reflection=True,
        V_SNAP=1.0,
        pml_thickness=pml_thickness,
    )
    center = (N // 2, N // 2, N // 2)
    core = _protect_mask(lat, center, CORE_R)
    face = _face_mask(lat)
    ports = face & ~core
    rng = np.random.default_rng(seed)
    _seed(lat, center, rng)

    bath_modes = np.zeros(M_MODES, dtype=float)
    scalar_bath = 0.0
    n_occ0 = _n_occ(bath_modes)

    E0 = float(lat.total_energy())
    E_core0 = float(lat.get_energy_density()[core].sum())
    # Baseline for the soft ledger: the equilibrated field, captured after the
    # first stepper equilibration (post-step-1, pre-transfer) rather than the raw
    # V_inc-only seed E0. See RunOut.E_field_equil.
    E_equil = E0
    detonated = False
    finite = True
    S_acc = 0.0
    n_events = 0

    for step_i in range(n_steps):
        lat.step()
        if step_i == 0:
            E_equil = float(lat.total_energy())
        d, ne = _arm_b_transfer(
            lat, ports, bath_modes, kappa=kappa, credit_modes=credit_modes
        )
        if not credit_modes:
            scalar_bath += d
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
    soft = abs((E_equil - Ef) - E_bath)
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
        pml_thickness=pml_thickness,
        E_field_equil=E_equil,
    )


def classify(on: RunOut, off: RunOut) -> str:
    """Production bins (prereg §2). PML sponge control is not CHANNEL-BOUNDED here."""
    if on.detonated or not on.finite:
        return "DETONATE"
    if on.E_bath < NULL_FLOOR:
        # Sponge can drop field energy with E_bath=0 → still not a pass.
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
    base_equil = on.E_field_equil if on.E_field_equil > 0.0 else on.E_field_initial
    if on.soft_ledger > TOL_SOFT_LEDGER_FRAC * max(base_equil, 1e-12):
        return "DETONATE"
    return "CHANNEL-BOUNDED"


def sponge_control_verdict() -> str:
    """Standard NEGATIVE control: PML ON, ports OFF (κ=0).

    This is a construction-forced negative control, NOT a liveness/positive-
    control demonstration. With κ=0, `_arm_b_transfer` returns (0,0) and
    E_bath≡0, so `classify()` short-circuits to NULL (E_bath<NULL_FLOOR)
    BEFORE the CHANNEL-BOUNDED path is reachable — verified across
    pml∈{0,2,4,6} (E_field vanishes 7.68→1.7e-16, E_bath stays 0, verdict NULL
    every time). The expected, entailed outcome is NULL; the SPONGE-COSTUME
    branch below is therefore not fireable by this control (it documents the
    κ-off branch, not detector liveness). Genuine mode-count liveness rests on
    the separate FRICTION-RENAMED sabotage plant (`--sabotage-friction`).
    """
    off = run_once(kappa=0.0, seed=SEED, pml_thickness=0)
    sponge = run_once(kappa=0.0, seed=SEED, pml_thickness=2)
    v = classify(sponge, off)
    # SPONGE-COSTUME detector: if someone treated sponge as ON transfer, bins say NULL
    # (E_bath=0) or FRICTION — never CHANNEL-BOUNDED without exterior modes.
    if v == "CHANNEL-BOUNDED":
        return "SPONGE-COSTUME"
    return f"SPONGE-CONTROL-OK ({v})"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--json", action="store_true")
    p.add_argument(
        "--sabotage-friction",
        action="store_true",
        help="credit scalar exterior bath only (FRICTION-RENAMED plant)",
    )
    p.add_argument(
        "--sponge-control",
        action="store_true",
        help="report PML-without-ports control (must not CHANNEL-BOUNDED)",
    )
    args = p.parse_args()
    credit = not args.sabotage_friction
    off = run_once(kappa=0.0, seed=SEED, credit_modes=True, pml_thickness=0)
    on = run_once(kappa=KAPPA, seed=SEED, credit_modes=credit, pml_thickness=0)
    verdict = classify(on, off)
    sponge = sponge_control_verdict() if args.sponge_control else None
    payload = {
        "verdict": verdict,
        "on": on.__dict__,
        "off": off.__dict__,
        "credit_modes": credit,
        "sponge_control": sponge,
        "geometry_fork": "G0",
    }
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
            f"ΔN_occ={on.N_occ_final - on.N_occ_initial}  "
            f"geometry=G0"
        )
        if sponge is not None:
            print(f"  sponge_control: {sponge}")


if __name__ == "__main__":
    main()
