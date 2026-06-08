#!/usr/bin/env python3
r"""Native AVE electron model — corpus 4-property joint seed on VacuumEngine3D.

SCOPE NOTE (driver-honesty): tests whether the canonical identification stack
(§ electron-identification.md) PERSISTS under coupled K4+Cosserat dynamics.
Does NOT claim forward derivation of m_e or α. α is comparison-only.

Model stack (substrate-native, no manual snap):
  Layer 1 — Cosserat: 0₁ unknot sector (`initialize_electron_unknot_sector`)
  Layer 3 — K4 bond LC: (2,3) quadrature phasor (`initialize_quadrature_2_3_eigenmode`)
  Geometry — Golden Torus R,r from `ave.core.constants` (not fitted)

Variants:
  canonical_subyield   — amp=0.48 (photon-side of yield threshold)
  canonical_saturated  — amp=0.92 (electron TIR target regime)
  bench_snap_reference — genesis snap protocol (external intervention control)

Output:
  src/scripts/vol_1_foundations/_output/native_electron_model_results.json
  assets/sim_outputs/native_electron_model_phasor.png (saturated arm)
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from electron_genesis_phasor_gif import (  # noqa: E402
    _pca_ellipse,
    _sample_phasor,
    _shell_mask,
)
from native_electron_propagation import (  # noqa: E402
    apply_co_moving_longitudinal_drive,
    energy_centroid,
    interior_mask,
)
from native_k4_gamma_ceiling import (  # noqa: E402
    GAMMA_FULL_TIR,
    bond_gamma_min,
    seed_sech_v_inc,
    verify_canonical_sources,
)
from tlm_electron_soliton_eigenmode import (  # noqa: E402
    initialize_quadrature_2_3_eigenmode,
)

from ave.core.constants import (  # noqa: E402
    ALPHA_COLD,
    PHI,
    R_GOLDEN_TORUS,
    R_GOLDEN_TORUS_MINOR,
    RR_GOLDEN_TORUS,
)
from ave.topological.vacuum_engine import VacuumEngine3D  # noqa: E402
from ave_path_util import sim_output  # noqa: E402

OUT_DIR = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())
OUT_DIR = OUT_DIR / "src" / "scripts" / "vol_1_foundations" / "_output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

N_LATTICE = 32
PML = 4
N_STEPS = 800
CADENCE = 2
SHELL_RADIUS = 6
SAMPLE_PORT = 0
PHI_SQ = PHI * PHI

# Genesis bench control
TRIGGER_X = 14.0
CX0_FRAC = 0.28
V_DRIVE_PRE = 0.04
SEED_RADIUS = 2.5

ALPHA_T = float(ALPHA_COLD)
GAMMA_TARGET = -math.sqrt(1.0 - ALPHA_T)
R_OVER_R_TOL = 0.15

PORT_VECTORS = np.array(
    [[+1, +1, +1], [+1, -1, -1], [-1, +1, -1], [-1, -1, +1]],
    dtype=int,
)


def _build_engine() -> VacuumEngine3D:
    return VacuumEngine3D.from_args(
        N=N_LATTICE,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )


def _find_central_bond(engine: VacuumEngine3D) -> tuple[tuple[int, int, int], int]:
    nx = engine.k4.nx
    cx = nx // 2
    for di in range(-3, 4):
        for dj in range(-3, 4):
            for dk in range(-3, 4):
                i, j, k = cx + di, cx + dj, cx + dk
                if not (PML <= i < nx - PML and PML <= j < nx - PML and PML <= k < nx - PML):
                    continue
                if not engine.k4.mask_A[i, j, k]:
                    continue
                for port in range(4):
                    p = PORT_VECTORS[port]
                    ib, jb, kb = i + p[0], j + p[1], k + p[2]
                    if engine.k4.mask_B[ib, jb, kb]:
                        return (i, j, k), port
    raise RuntimeError("no central A-B bond")


def _seed_canonical(engine: VacuumEngine3D, *, amplitude: float) -> None:
    """Joint Golden-Torus (2,3) phasor + 0₁ unknot ω — no external snap."""
    initialize_quadrature_2_3_eigenmode(
        engine.k4,
        R=float(R_GOLDEN_TORUS),
        r=float(R_GOLDEN_TORUS_MINOR),
        amplitude=amplitude,
        chirality=1.0,
    )
    engine.cos.initialize_electron_unknot_sector(
        R_target=float(R_GOLDEN_TORUS),
        r_target=float(R_GOLDEN_TORUS_MINOR),
        amplitude_scale=min(amplitude, 1.0),
        use_hedgehog=True,
    )


def _run_evolution(
    engine: VacuumEngine3D,
    *,
    n_steps: int,
    drive: bool = False,
    snap_at_x: float | None = None,
    trap_amp: float | None = None,
) -> dict[str, Any]:
    n = N_LATTICE
    cy0 = cz0 = n // 2
    cx0 = int(CX0_FRAC * n)
    mask = interior_mask(n, PML) & engine.k4.mask_active
    bond_a, bond_port = _find_central_bond(engine)

    snap_step: int | None = None
    last_cx = float(cx0)
    records: list[dict[str, Any]] = []
    bond_vi: list[float] = []
    bond_vr: list[float] = []

    omega0 = float(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1).max())
    e0 = float(np.sum(np.asarray(engine.k4.V_inc) ** 2 + np.asarray(engine.k4.V_ref) ** 2))

    for step in range(n_steps + 1):
        if step % CADENCE == 0:
            engine._coupled._update_z_local_total()
            z = np.asarray(engine.k4.z_local_field)
            v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
            cx, _, _ = energy_centroid(v_sq, mask)
            if np.isfinite(cx):
                last_cx = cx
            core = (
                min(max(int(round(last_cx)), PML), n - PML - 1),
                cy0,
                cz0,
            )
            gamma = bond_gamma_min(z, engine.k4.mask_active, core, SHELL_RADIUS)
            vi, vr = _sample_phasor(engine, core, SAMPLE_PORT, shell_radius=SHELL_RADIUS)
            ax, ay, az = bond_a
            bvi = float(engine.k4.V_inc[ax, ay, az, bond_port])
            bvr = float(engine.k4.V_ref[ax, ay, az, bond_port])
            bond_vi.append(bvi)
            bond_vr.append(bvr)

            omega = np.asarray(engine.cos.omega)
            u = np.asarray(engine.cos.u)
            sh = _shell_mask(v_sq.shape, core, SHELL_RADIUS, engine.k4.mask_active)
            omega_shell = float(np.mean(np.linalg.norm(omega[sh], axis=-1))) if np.any(sh) else 0.0
            u_shell = float(np.mean(np.linalg.norm(u[sh], axis=-1))) if np.any(sh) else 0.0
            e_tot = float(np.sum(v_sq))
            e_shell_frac = float(np.sum(v_sq[sh]) / max(e_tot, 1e-30)) if np.any(sh) else None

            records.append(
                {
                    "step": step,
                    "gamma_min": gamma,
                    "eps_gamma": float(1.0 - gamma**2) if gamma is not None else None,
                    "shell_phasor": [vi, vr],
                    "bond_phasor": [bvi, bvr],
                    "omega_shell_mean": omega_shell,
                    "u_shell_mean": u_shell,
                    "e_shell_fraction": e_shell_frac,
                    "cx": last_cx,
                }
            )

        if (
            snap_at_x is not None
            and trap_amp is not None
            and snap_step is None
            and step < n_steps
            and last_cx >= snap_at_x
        ):
            core = (
                min(max(int(round(last_cx)), PML), n - PML - 1),
                cy0,
                cz0,
            )
            seed_sech_v_inc(engine, core, trap_amp, SEED_RADIUS)
            engine.cos.initialize_electron_unknot_sector(
                R_target=0.5, r_target=0.25, amplitude_scale=min(trap_amp, 1.0)
            )
            snap_step = step
            last_cx = float(core[0])

        if step < n_steps:
            if drive and snap_step is None:
                apply_co_moving_longitudinal_drive(engine, last_cx, V_DRIVE_PRE)
            engine.step()

    omega_f = float(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1).max())
    ef = float(np.sum(np.asarray(engine.k4.V_inc) ** 2 + np.asarray(engine.k4.V_ref) ** 2))
    try:
        crossing_c = int(engine.cos.extract_crossing_count())
    except Exception:
        crossing_c = None

    shell_vi = np.array([r["shell_phasor"][0] for r in records], dtype=float)
    shell_vr = np.array([r["shell_phasor"][1] for r in records], dtype=float)
    bond_vi_a = np.array(bond_vi, dtype=float)
    bond_vr_a = np.array(bond_vr, dtype=float)

    pca_shell = _pca_ellipse(shell_vi, shell_vr)
    pca_bond = _pca_ellipse(bond_vi_a, bond_vr_a)

    gammas = [r["gamma_min"] for r in records if r["gamma_min"] is not None]
    gamma_min = float(min(gammas)) if gammas else None
    gamma_final = gammas[-1] if gammas else None
    eps_mean = float(
        np.mean([r["eps_gamma"] for r in records if r["eps_gamma"] is not None])
    ) if records else None

    tir_held = bool(
        gamma_min is not None
        and gamma_min <= GAMMA_FULL_TIR
        and (gamma_final is None or gamma_final <= -0.95)
    )
    localized = bool(
        records
        and records[-1]["e_shell_fraction"] is not None
        and records[-1]["e_shell_fraction"] > 0.35
    )
    t2_dominant = bool(
        records
        and records[-1]["omega_shell_mean"] is not None
        and records[-1]["u_shell_mean"] is not None
        and records[-1]["omega_shell_mean"] > 3.0 * max(records[-1]["u_shell_mean"], 1e-12)
    )
    rr_shell_ok = bool(
        math.isfinite(pca_shell["R_over_r"])
        and abs(pca_shell["R_over_r"] - PHI_SQ) / PHI_SQ < R_OVER_R_TOL
    )
    rr_bond_ok = bool(
        math.isfinite(pca_bond["R_over_r"])
        and abs(pca_bond["R_over_r"] - PHI_SQ) / PHI_SQ < R_OVER_R_TOL
    )

    props = {
        "P1_unknot_localized": localized,
        "P2_shell_Rr_near_phi_sq": rr_shell_ok,
        "P2_bond_Rr_near_phi_sq": rr_bond_ok,
        "P3_TIR_held": tir_held,
        "P4_T2_omega_dominates_u": t2_dominant,
    }
    n_pass = sum(1 for v in props.values() if v)

    if n_pass >= 4:
        verdict, outcome = "MODEL_FOUR_PROPERTY_PASS", "A"
    elif tir_held and localized and n_pass >= 2:
        verdict, outcome = "MODEL_TRAP_PARTIAL_IDENTIFICATION", "B"
    elif tir_held:
        verdict, outcome = "MODEL_TIR_ONLY_NOT_FULL_ELECTRON", "C"
    else:
        verdict, outcome = "MODEL_FAILS_CANONICAL_PERSISTENCE", "D"

    return {
        "n_steps": n_steps,
        "snap_step": snap_step,
        "n_samples": len(records),
        "golden_torus_R": float(R_GOLDEN_TORUS),
        "golden_torus_r": float(R_GOLDEN_TORUS_MINOR),
        "R_times_r": float(RR_GOLDEN_TORUS),
        "phi_sq_target": PHI_SQ,
        "omega_peak_initial": omega0,
        "omega_peak_final": omega_f,
        "omega_persistence_ratio": omega_f / max(omega0, 1e-30),
        "energy_ratio_final_initial": ef / max(e0, 1e-30),
        "crossing_count_c": crossing_c,
        "gamma_min": gamma_min,
        "gamma_final": gamma_final,
        "gamma_target_for_alpha": GAMMA_TARGET,
        "eps_gamma_mean": eps_mean,
        "abs_eps_minus_alpha": abs(eps_mean - ALPHA_T) if eps_mean is not None else None,
        "pca_shell": pca_shell,
        "pca_bond": pca_bond,
        "property_checks": props,
        "properties_passed": n_pass,
        "verdict": verdict,
        "outcome": outcome,
        "alpha_used_as_input": False,
        "comparison_only_alpha": ALPHA_T,
        "records_tail": records[-5:],
    }


def _seed_bench(engine: VacuumEngine3D) -> None:
    cx0 = int(CX0_FRAC * N_LATTICE)
    cy0 = cz0 = N_LATTICE // 2
    seed_sech_v_inc(engine, (cx0, cy0, cz0), 0.48, SEED_RADIUS)
    engine.cos.initialize_electron_unknot_sector(
        R_target=0.5, r_target=0.25, amplitude_scale=0.48
    )


def render_phasor_png(shell_vi: np.ndarray, shell_vr: np.ndarray, bond_vi: np.ndarray, bond_vr: np.ndarray, title: str, out_path: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))
    fig.patch.set_facecolor("#0a0a12")
    for ax, vi, vr, label in zip(
        axes,
        [shell_vi, bond_vi],
        [shell_vr, bond_vr],
        ["shell-mean phasor", "central bond phasor"],
        strict=True,
    ):
        ax.set_facecolor("#111118")
        ax.plot(vi, vr, color="#00e5ff", lw=0.9, alpha=0.85)
        ax.plot(vi[-1], vr[-1], "o", color="#ffeb3b", markersize=7)
        ax.axhline(0, color="#444", lw=0.5)
        ax.axvline(0, color="#444", lw=0.5)
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlabel(r"$V_{\mathrm{inc}}$")
        ax.set_ylabel(r"$V_{\mathrm{ref}}$")
        ax.set_title(label, color="#ddd", fontsize=10)
        ax.tick_params(colors="#aaa")
    fig.suptitle(title, color="#eee", fontsize=11)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)


def run_variant(name: str, *, amplitude: float | None, bench: bool = False) -> dict[str, Any]:
    engine = _build_engine()
    if bench:
        _seed_bench(engine)
        row = _run_evolution(
            engine,
            n_steps=N_STEPS,
            drive=True,
            snap_at_x=TRIGGER_X,
            trap_amp=1.25,
        )
        row["variant"] = name
        row["seed"] = "genesis_bench_snap"
        row["amplitude_V_SNAP"] = 0.48
        return row

    assert amplitude is not None
    _seed_canonical(engine, amplitude=amplitude)
    row = _run_evolution(engine, n_steps=N_STEPS, drive=False)
    row["variant"] = name
    row["seed"] = "golden_torus_quadrature_plus_unknot"
    row["amplitude_V_SNAP"] = amplitude
    return row


def classify(rows: list[dict[str, Any]]) -> dict[str, Any]:
    canon = [r for r in rows if r["seed"] == "golden_torus_quadrature_plus_unknot"]
    best = max(canon, key=lambda r: r["properties_passed"], default=None)
    sat = next((r for r in rows if r["variant"] == "canonical_saturated"), None)
    if best and best["outcome"] == "A":
        agg = "NATIVE_MODEL_IDENTIFICATION_LANDED"
    elif sat and sat["property_checks"]["P3_TIR_held"]:
        agg = "NATIVE_MODEL_TIR_WITHOUT_FULL_FOUR_PROPERTY"
    elif best and best["property_checks"]["P3_TIR_held"]:
        agg = "NATIVE_MODEL_PARTIAL_TRAP"
    else:
        agg = "NATIVE_MODEL_NOT_SELF_SUSTAINING"
    return {
        "aggregate_verdict": agg,
        "best_canonical_variant": best["variant"] if best else None,
        "best_properties_passed": best["properties_passed"] if best else None,
        "bench_reference_verdict": next(
            (r["verdict"] for r in rows if r["variant"] == "bench_snap_reference"),
            None,
        ),
    }


def main() -> None:
    verify_canonical_sources()
    print("Native AVE electron model (4-property joint seed)")
    print(f"  Golden Torus R={R_GOLDEN_TORUS:.4f} r={R_GOLDEN_TORUS_MINOR:.4f} Rr={RR_GOLDEN_TORUS:.4f}")

    rows = [
        run_variant("canonical_subyield", amplitude=0.48),
        run_variant("canonical_saturated", amplitude=0.92),
        run_variant("bench_snap_reference", amplitude=None, bench=True),
    ]

    # PNG from saturated arm — re-run lightweight for full trajectory arrays
    engine = _build_engine()
    _seed_canonical(engine, amplitude=0.92)
    n = N_LATTICE
    cy0 = cz0 = n // 2
    mask = interior_mask(n, PML) & engine.k4.mask_active
    bond_a, bond_port = _find_central_bond(engine)
    shell_vi, shell_vr, bond_vi, bond_vr = [], [], [], []
    for step in range(N_STEPS + 1):
        if step % CADENCE == 0:
            engine._coupled._update_z_local_total()
            v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
            cx, _, _ = energy_centroid(v_sq, mask)
            core = (min(max(int(round(cx)), PML), n - PML - 1), cy0, cz0)
            vi, vr = _sample_phasor(engine, core, SAMPLE_PORT, shell_radius=SHELL_RADIUS)
            shell_vi.append(vi)
            shell_vr.append(vr)
            ax, ay, az = bond_a
            bond_vi.append(float(engine.k4.V_inc[ax, ay, az, bond_port]))
            bond_vr.append(float(engine.k4.V_ref[ax, ay, az, bond_port]))
        if step < N_STEPS:
            engine.step()

    png_path = sim_output("native_electron_model_phasor.png")
    sat = rows[1]
    render_phasor_png(
        np.array(shell_vi),
        np.array(shell_vr),
        np.array(bond_vi),
        np.array(bond_vr),
        f"Native electron model @ amp=0.92  {sat['verdict']}  pass={sat['properties_passed']}/4",
        png_path,
    )

    classification = classify(rows)
    payload = {
        "prereg": "research/2026-06-08_native-electron-model-prereg.md",
        "model_description": (
            "Joint Golden-Torus (2,3) quadrature phasor + 0₁ unknot ω on "
            "VacuumEngine3D; zero drive; no PairNucleationGate; α comparison-only."
        ),
        "rows": rows,
        "classification": classification,
    }
    out_json = OUT_DIR / "native_electron_model_results.json"
    out_json.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")

    for row in rows:
        print(
            f"  {row['variant']}: {row['verdict']} ({row['outcome']})"
            f"  pass={row['properties_passed']}/4"
            f"  Γ_min={row['gamma_min']}"
            f"  ε̄={row['eps_gamma_mean']}"
            f"  shell R/r={row['pca_shell']['R_over_r']:.3f}"
            f"  bond R/r={row['pca_bond']['R_over_r']:.3f}"
        )
    print(f"  aggregate: {classification['aggregate_verdict']}")
    print(f"  png: {png_path}")
    print(f"  json: {out_json}")


if __name__ == "__main__":
    main()
