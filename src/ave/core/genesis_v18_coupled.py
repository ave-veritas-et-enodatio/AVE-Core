"""
Genesis v18 — operator-native K4⊗Cosserat stack (LOOP GAP ranks 3–4).

**SUPERSEDED (2026-06-12):** use ``loop_gap_harness.py`` + rank profiles on
``VacuumEngine3D``. This module remains as shared seed/observable helpers until
Phase 2 migration completes. Do not add v19 — advance ranks on the harness.

Single platform: CoupledK4Cosserat with trilinear converter + Γ_bulk impedance
wall + memristive Op14 lag. Conservative ring-up (no srs add_drive pump).

Pre-reg: extends genesis-v11-loop-closure + v15b V_inc nucleation charter.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core.constants import ALPHA, R_II

# P11 quiescence thresholds — prereg proposed (genesis-v11-loop-closure); not CI-gated.
P11_E_PERSIST_MIN = 0.85
P11_A_PERSIST_MIN = 0.80
P11_THETA_PERSIST_MIN = 0.75
from ave.core.cross_sector_coupling import scale_cosserat_to_front
from ave.topological.k4_cosserat_coupling import (
    CoupledK4Cosserat,
    _cosserat_A_squared,
    _v_squared_per_site,
)

# P18 operator gates (proposed — freeze at Grant ratification).
P18_VINC_FLOOR = 1e-12
P18_GAMMA_MAX = -0.25  # Γ_bulk short engaged (Γ < this)
P18_PHI_GROW_MIN = 1.05  # Φ_link energy growth drive / t0
P18_RHO_MIN = 0.15  # cross-sector correlation at saturation front

COMPTON_DRIVE_MULTS = (1.0, 2.0, 4.0)
DEFAULT_QUIET_MULT = 4.0

# Impedance wall params (genesis-23 energize-lock analogue).
IMPEDANCE_CLAMP_K = 60.0
IMPEDANCE_CFL_SAFE = 0.25


@dataclass(frozen=True)
class V18P18Result:
    label: str
    n_drive_mult: float
    n_drive: int
    n_quiet: int
    impedance_on: bool
    converter_on: bool
    memristive_on: bool
    v_inc_peak: float
    phi_link_sq_driveoff: float
    phi_link_sq_end: float
    phi_growth: float
    gamma_min_drive: float
    rho_cross_end: float
    xl_over_xc_end: float
    H_driveoff: float
    H_end: float
    S_mean_driveoff: float
    S_mean_end: float
    E_persist_ratio: float
    phi_persist_ratio: float
    S_persist_delta: float
    p18_gamma_pass: bool
    p18_vinc_pass: bool
    p18_op14_pass: bool
    p11_pass: bool
    bin_label: str


def tau_steps_k4(sim: CoupledK4Cosserat, *, fast: bool = False) -> int:
    """Map τ_relax to scatter-step budget (v11 analogue on K4 dt)."""
    ratio = float(sim.k4.tau_relax / max(sim.k4.dt, 1e-30))
    base = max(20, int(round(25.0 * ratio)))
    return max(8, base // 4) if fast else base


def make_v18_engine(
    N: int,
    *,
    memristive: bool = True,
    impedance: bool = True,
    converter: bool = True,
    couple_v: bool = True,
) -> CoupledK4Cosserat:
    """Axiom-native coupled cell — one AVE_VACUUM_CELL per bond."""
    return CoupledK4Cosserat(
        N=N,
        pml=3,
        use_memristive_saturation=memristive,
        use_trilinear_converter=converter,
        converter_mode="trilinear",
        converter_freeze_wall=True,
        disable_cosserat_lc_force=True,
        couple_v_sector=couple_v,
        use_impedance_boundary=impedance,
        impedance_clamp_strength=IMPEDANCE_CLAMP_K,
        impedance_cfl_safety=IMPEDANCE_CFL_SAFE,
        impedance_implicit=True,
    )


def pair_seed_cosserat(sim: CoupledK4Cosserat, *, amp: float) -> None:
    """Saturated pair analogue at R_II front — conservative IC, no external pump."""
    N = sim.N
    cx, cy, cz = N // 2, N // 2, N // 2
    for dx, dy in ((0, 0), (1, 0)):
        ix = min(max(cx + dx, 0), N - 1)
        iy = min(max(cy + dy, 0), N - 1)
        env = np.exp(
            -(
                (np.arange(N)[:, None, None] - ix) ** 2
                + (np.arange(N)[None, :, None] - iy) ** 2
                + (np.arange(N)[None, None, :] - cz) ** 2
            )
            / (2.0 * 1.2**2)
        )
        sim.cos.u[..., 0] += amp * env
        sim.cos.omega[..., 2] += 0.5 * amp * env
    A_cos_sq = _cosserat_A_squared(
        sim.cos.u, sim.cos.omega, sim.cos.dx, sim.cos.omega_yield, sim.cos.epsilon_yield
    )
    sim.cos.u, sim.cos.omega = scale_cosserat_to_front(
        sim.cos.u, sim.cos.omega, A_cos_sq, target=R_II
    )
    sim.cos.u_dot[:] = 0.0
    sim.cos.omega_dot[:] = 0.0
    sim.k4.V_inc[:] = 0.0
    sim.k4.V_ref[:] = 0.0
    sim.k4.Phi_link[:] = 0.0


def _valid_mask(sim: CoupledK4Cosserat) -> np.ndarray:
    active = np.asarray(sim.k4.mask_active, dtype=bool)
    interior = np.asarray(sim._interior_mask(), dtype=bool)
    return active & interior


def total_H(sim: CoupledK4Cosserat) -> float:
    if sim.use_impedance_boundary:
        return float(sim.impedance_hamiltonian()["H"])
    return float(sim.total_hamiltonian())


def snapshot_op14(sim: CoupledK4Cosserat, *, omega_drive: float = 1.0) -> dict:
    """Op14 trading observables — not srs transverse peak."""
    k4 = sim.k4
    valid = _valid_mask(sim)
    Phi = k4.Phi_link
    V_inc = k4.V_inc

    phi_sq = float(np.sum(Phi[valid] ** 2)) if valid.any() else 0.0
    v_max = float(np.max(np.abs(V_inc[valid]))) if valid.any() else 0.0
    S = k4.S_field
    s_mean = float(S[valid].mean()) if valid.any() else 0.0

    gamma_min = 0.0
    if sim.use_impedance_boundary:
        gamma = sim._impedance_gamma_shared()
        gamma_min = float(gamma[valid].min()) if valid.any() else 0.0

    g_wall = sim._converter_wall_window()
    front = valid & (g_wall > 0.1)
    omega_mag = np.linalg.norm(sim.cos.omega, axis=-1)
    v_scalar = np.sqrt(_v_squared_per_site(V_inc))
    if int(front.sum()) > 4:
        a = v_scalar[front].ravel()
        b = omega_mag[front].ravel()
        if np.std(a) > 1e-15 and np.std(b) > 1e-15:
            rho = float(np.corrcoef(a, b)[0, 1])
        else:
            rho = 0.0
    else:
        rho = 0.0

    mask_A = k4.mask_A
    valid4 = np.broadcast_to((mask_A & valid)[..., None], V_inc.shape)
    absV = np.abs(V_inc[valid4])
    absPhi = np.abs(Phi[valid4])
    eps = 1e-30
    xl_xc = 0.0
    if absV.size > 0:
        XC = absV / (omega_drive * absPhi + eps)
        XL = (omega_drive * absPhi) / (absV + eps)
        xl_xc = float(np.median(XL / (XC + eps)))

    return {
        "H": total_H(sim),
        "E_k4": float(sim.k4_energy()),
        "H_cos": float(sim.cosserat_energy() + sim.cosserat_kinetic_energy()),
        "phi_link_sq": phi_sq,
        "v_inc_max": v_max,
        "S_mean": s_mean,
        "gamma_min": gamma_min,
        "rho_cross": rho,
        "xl_over_xc": xl_xc,
        "max_A_sq": float(sim.max_A_squared()),
        "H_couple": float(sim.converter_coupling_energy()),
    }


def _p11_pass(*, E_persist: float, phi_persist: float, S_delta: float) -> bool:
    """K4 remanence: H + Φ_link + memristive S lag after quiescence."""
    return (
        E_persist >= P11_E_PERSIST_MIN
        and phi_persist >= P11_A_PERSIST_MIN
        and S_delta >= P11_THETA_PERSIST_MIN * 0.05
    )


def _p18_op14_pass(phi_growth: float, rho: float, xl_xc: float) -> bool:
    return phi_growth >= P18_PHI_GROW_MIN and (rho >= P18_RHO_MIN or xl_xc > 0.5)


def run_p18_operator_cell(
    label: str,
    *,
    N: int = 14,
    amp: float | None = None,
    n_drive_mult: float = 2.0,
    n_quiet_mult: float = DEFAULT_QUIET_MULT,
    impedance_on: bool = True,
    converter_on: bool = True,
    memristive_on: bool = True,
    couple_v: bool = True,
    fast: bool = False,
) -> V18P18Result:
    """P18 — conservative converter ring-up + quiescence on unified K4⊗Cosserat."""
    if amp is None:
        amp = float(np.sqrt(ALPHA))

    sim = make_v18_engine(
        N,
        memristive=memristive_on,
        impedance=impedance_on,
        converter=converter_on,
        couple_v=couple_v,
    )
    pair_seed_cosserat(sim, amp=amp)
    sim.freeze_converter_wall()

    tau = tau_steps_k4(sim, fast=fast)
    n_drive = max(6 if fast else 10, int(round(n_drive_mult * tau)))
    n_quiet = max(10 if fast else 20, int(round(n_quiet_mult * tau)))
    n_total = n_drive + n_quiet

    obs0 = snapshot_op14(sim)
    phi0 = max(obs0["phi_link_sq"], 1e-30)
    H0 = max(obs0["H"], 1e-30)

    v_peak = obs0["v_inc_max"]
    gamma_min_drive = obs0["gamma_min"] if impedance_on else 0.0
    obs_driveoff = obs0

    for t in range(1, n_total + 1):
        sim.step()
        obs_t = snapshot_op14(sim)
        v_peak = max(v_peak, obs_t["v_inc_max"])
        if t <= n_drive:
            if impedance_on:
                gamma_min_drive = min(gamma_min_drive, obs_t["gamma_min"])
            obs_driveoff = obs_t
    obs_end = obs_t

    phi_drive = max(obs_driveoff["phi_link_sq"], phi0)
    phi_end = obs_end["phi_link_sq"]
    H_drive = max(obs_driveoff["H"], H0)
    H_end = obs_end["H"]
    S_drive = obs_driveoff["S_mean"]
    S_end = obs_end["S_mean"]

    phi_growth = phi_drive / phi0
    E_persist = H_end / H_drive if H_drive > 0 else 0.0
    phi_persist = phi_end / phi_drive if phi_drive > 0 else 0.0
    S_delta = abs(S_end - S_drive)

    p18_gamma = impedance_on and gamma_min_drive <= P18_GAMMA_MAX
    p18_vinc = v_peak > P18_VINC_FLOOR
    p18_op14 = converter_on and _p18_op14_pass(
        phi_growth, obs_end["rho_cross"], obs_end["xl_over_xc"]
    )
    p11 = _p11_pass(E_persist=E_persist, phi_persist=phi_persist, S_delta=S_delta)

    if p11 and p18_gamma and p18_vinc:
        bin_label = "REMANENCE-LANDED"
    elif p18_gamma and p18_vinc and p18_op14:
        bin_label = "OPERATOR-SET"
    elif p18_vinc:
        bin_label = "VINC-ONLY"
    else:
        bin_label = "ENGINE-GAP"

    return V18P18Result(
        label=label,
        n_drive_mult=n_drive_mult,
        n_drive=n_drive,
        n_quiet=n_quiet,
        impedance_on=impedance_on,
        converter_on=converter_on,
        memristive_on=memristive_on,
        v_inc_peak=v_peak,
        phi_link_sq_driveoff=phi_drive,
        phi_link_sq_end=phi_end,
        phi_growth=phi_growth,
        gamma_min_drive=gamma_min_drive,
        rho_cross_end=obs_end["rho_cross"],
        xl_over_xc_end=obs_end["xl_over_xc"],
        H_driveoff=H_drive,
        H_end=H_end,
        S_mean_driveoff=S_drive,
        S_mean_end=S_end,
        E_persist_ratio=E_persist,
        phi_persist_ratio=phi_persist,
        S_persist_delta=S_delta,
        p18_gamma_pass=p18_gamma,
        p18_vinc_pass=p18_vinc,
        p18_op14_pass=p18_op14,
        p11_pass=p11,
        bin_label=bin_label,
    )


def v18_gates(*, L: int = 14, smoke: bool = False) -> dict:
    """Full P18 battery — Compton sweep + ablations."""
    mults = (1.0,) if smoke else COMPTON_DRIVE_MULTS
    fast = smoke
    quiet_mult = 1.5 if smoke else DEFAULT_QUIET_MULT
    sweep: list[dict] = []
    for m in mults:
        r = run_p18_operator_cell(
            f"full_stack_{m}x",
            N=L,
            n_drive_mult=m,
            n_quiet_mult=quiet_mult,
            impedance_on=True,
            converter_on=True,
            memristive_on=True,
            fast=fast,
        )
        sweep.append(_result_to_dict(r))

    ablation_kw = dict(N=L, n_drive_mult=1.0, n_quiet_mult=quiet_mult, fast=fast)
    mem_off = run_p18_operator_cell(
        "memristive_OFF",
        memristive_on=False,
        **ablation_kw,
    )
    wall_off = run_p18_operator_cell(
        "impedance_OFF",
        impedance_on=False,
        **ablation_kw,
    )
    conv_off = run_p18_operator_cell(
        "converter_OFF",
        converter_on=False,
        **ablation_kw,
    )

    best = max(sweep, key=lambda d: d["E_persist_ratio"])
    any_p11 = any(d["p11_pass"] for d in sweep)
    any_operator = any(
        d["p18_gamma_pass"] and d["p18_vinc_pass"] and d["p18_op14_pass"] for d in sweep
    )

    if any_p11:
        verdict = "REMANENCE-LANDED"
    elif best["p18_gamma_pass"] and best["p18_vinc_pass"] and best["p18_op14_pass"]:
        verdict = "OPERATOR-SET-ONLY"
    elif best["p18_gamma_pass"] and best["p18_vinc_pass"]:
        verdict = "GAMMA-SET-ONLY"
    elif best["p18_vinc_pass"]:
        verdict = "PARTIAL"
    else:
        verdict = "ENGINE-GAP"

    return {
        "verdict": verdict,
        "P18_ringup_sweep": sweep,
        "P18_mem_ablation": _result_to_dict(mem_off),
        "P18_wall_ablation": _result_to_dict(wall_off),
        "P18_converter_ablation": _result_to_dict(conv_off),
        "best_arm": best["label"],
        "any_p11": any_p11,
        "any_operator_set": any_operator,
        "thresholds": {
            "P11_E": P11_E_PERSIST_MIN,
            "P11_phi": P11_A_PERSIST_MIN,
            "P18_VINC": P18_VINC_FLOOR,
            "P18_GAMMA": P18_GAMMA_MAX,
        },
    }


def _result_to_dict(r: V18P18Result) -> dict:
    return {
        "label": r.label,
        "n_drive_mult": r.n_drive_mult,
        "n_drive": r.n_drive,
        "n_quiet": r.n_quiet,
        "impedance_on": r.impedance_on,
        "converter_on": r.converter_on,
        "memristive_on": r.memristive_on,
        "v_inc_peak": r.v_inc_peak,
        "phi_growth": r.phi_growth,
        "gamma_min_drive": r.gamma_min_drive,
        "rho_cross_end": r.rho_cross_end,
        "xl_over_xc_end": r.xl_over_xc_end,
        "E_persist_ratio": r.E_persist_ratio,
        "phi_persist_ratio": r.phi_persist_ratio,
        "S_persist_delta": r.S_persist_delta,
        "p18_gamma_pass": r.p18_gamma_pass,
        "p18_vinc_pass": r.p18_vinc_pass,
        "p18_op14_pass": r.p18_op14_pass,
        "p11_pass": r.p11_pass,
        "bin_label": r.bin_label,
    }
