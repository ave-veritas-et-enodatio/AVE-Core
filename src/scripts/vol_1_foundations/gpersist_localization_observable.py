#!/usr/bin/env python3
"""G-PERSIST localization observable + φ-channel plant — thin Rule-14 driver.

FROZEN prereg: research/2026-07-14_gpersist-localization-observable_prereg_FROZEN.md
(freeze-by-push BEFORE this driver; the freeze commit precedes this file in git
history on analysis/gpersist-localization-observable).

The two KEEP-BOTH follow-ons named in the #670 RESULT §8 (frozen #670 E/φ axes
UNTOUCHED):

  1. LOCALIZATION OBSERVABLE — a boundary-insensitive per-sector spatial-
     concentration meter (participation ratio + density-peak core fraction),
     A1/energy ⊥ T2/Φ_link (never summed), over the PML-excluded interior,
     recorded per quiet step. Discriminates the enclosure fork:
       CONCENTRATING (energy tightens)   -> Reading B genesis-under-confinement
       LOOP-FILLING  (energy stays flat  -> Reading A wake-feeding (Grant's lean)
                      while φ inflates)
  2. φ-CHANNEL PLANT — sustains φ via a distributed external K4 pump WITHOUT
     clobbering the Cosserat state (the #670 review's missing negative control).
     Frozen criterion: φ sustained (fools the retention floor) AND the meter reads
     LOOP-FILLING (externally-fed) => the two-meter combo is un-foolable.

Carrier = the EXISTING loop_gap_harness rank-4 probe, re-run through an
INSTRUMENTED MIRROR LOOP built from the SAME primitives (make_engine / apply_seed
/ apply_bulk_probe_ic / freeze_converter_wall / step / snapshot_op14). No new
engine, no new stepper, no retune. Byte-parity vs run_loop_gap_probe is asserted
on a live cell (--parity) — the meter is measured on the SAME trajectory.

States fork DATA; Grant rules the fork. Does NOT re-open G-PERSIST ★RULED (that
flip rests on the fork-independent PML φ-dispersion trend).

Usage:
  python gpersist_localization_observable.py --parity N PML MODE FID
  python gpersist_localization_observable.py --cell   N PML MODE FID
  python gpersist_localization_observable.py --plant  N PML MODE FID
  python gpersist_localization_observable.py --aggregate
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

from ave.core.constants import ALPHA
from ave.core.genesis_v18_coupled import (
    P11_A_PERSIST_MIN,
    P11_E_PERSIST_MIN,
    snapshot_op14,
    tau_steps_k4,
)
from ave.core.loop_gap_harness import (
    PHI_BASELINE_FLOOR,
    make_engine,
    run_loop_gap_probe,
)
from ave.core.loop_gap_seeds import A_LOCK_DEFAULT, A_YIELD, apply_seed

PREREG = "research/2026-07-14_gpersist-localization-observable_prereg_FROZEN.md"
OUT_DIR = Path("assets/sim_outputs/gpersist_localization_observable")

LANDED_SEED_MODES = ("pair", "graded_a0", "photon_lock")
THETA = 0.10  # frozen meter-resolution floor (10% relative change)
CORE_RADII = (1.5, 2.0, 2.5)
PRIMARY_R = 2.0
SECTORS = ("energy", "energy_k4", "phi_link")


# ---------------------------------------------------------------------------
# The localization meter (FROZEN definition, prereg §The localization meter)
# ---------------------------------------------------------------------------
def _meter_snapshot(coupled) -> dict:
    """Per-sector spatial-concentration meter at the current engine state.

    A1/energy density = k4.get_energy_density() + cos.energy_density();
    T2/Φ_link density = Σ_port Phi_link²; over the PML-excluded interior mask.
    Never summed across sectors (A1 ⊥ T2). PR = raw participation ratio (effective
    participating sites); CF_r = fraction within radius r of the DENSITY PEAK
    (peak, not centroid) and of the geometric center.
    """
    mask = np.asarray(coupled._interior_mask(), dtype=bool)
    N = coupled.N
    k4 = coupled.k4
    e_k4 = np.asarray(k4.get_energy_density(), dtype=float)
    e_cos = np.asarray(coupled.cos.energy_density(), dtype=float)
    e_dens = e_k4 + e_cos
    phi_dens = np.sum(np.asarray(k4.Phi_link, dtype=float) ** 2, axis=-1)

    ax = np.arange(N)
    xx = ax[:, None, None]
    yy = ax[None, :, None]
    zz = ax[None, None, :]
    geom = (N // 2, N // 2, N // 2)
    M = int(mask.sum())
    out = {"M": M}
    for name, d in (("energy", e_dens), ("energy_k4", e_k4), ("phi_link", phi_dens)):
        dv = d[mask]
        s1 = float(dv.sum())
        s2 = float((dv * dv).sum())
        pr = (s1 * s1) / s2 if s2 > 0 else 0.0
        dm = np.where(mask, d, -np.inf)
        pk = tuple(int(v) for v in np.unravel_index(int(np.argmax(dm)), d.shape))
        total = s1
        row: dict = {"PR": pr, "PR_frac": (pr / M if M > 0 else 0.0), "peak": list(pk)}
        rr_pk = np.sqrt((xx - pk[0]) ** 2 + (yy - pk[1]) ** 2 + (zz - pk[2]) ** 2)
        rr_gm = np.sqrt(
            (xx - geom[0]) ** 2 + (yy - geom[1]) ** 2 + (zz - geom[2]) ** 2
        )
        for r in CORE_RADII:
            cp = mask & (rr_pk <= r)
            cg = mask & (rr_gm <= r)
            row[f"CF_peak_{r}"] = float(d[cp].sum()) / total if total > 0 else 0.0
            row[f"CF_geom_{r}"] = float(d[cg].sum()) / total if total > 0 else 0.0
        out[name] = row
    return out


def _trend(series: list[dict], sector: str, stat: str) -> dict:
    vals = [s[sector][stat] for s in series]
    start, end = vals[0], vals[-1]
    rel = (end - start) / abs(start) if abs(start) > 1e-30 else 0.0
    return {
        "start": round(start, 6),
        "end": round(end, 6),
        "rel_trend": round(rel, 6),
        "min": round(min(vals), 6),
        "max": round(max(vals), 6),
    }


# ---------------------------------------------------------------------------
# Instrumented mirror loop — SAME primitives as run_loop_gap_probe (Rule-14),
# plus per-quiet-step meter recording, plus the optional φ-channel plant.
# ---------------------------------------------------------------------------
def _build_engine(N: int, pml: int, mode: str):
    """Reproduce run_loop_gap_probe's engine construction byte-for-byte."""
    engine = make_engine(
        4, N=N, bulk_density_on=True, pml=pml, use_memristive_saturation=True
    )
    apply_seed(engine, mode, amp=None, a_lock=A_LOCK_DEFAULT, front_target=A_YIELD)
    engine.apply_bulk_probe_ic(amp=0.08)
    engine.freeze_converter_wall()
    return engine


def run_instrumented(
    N: int, pml: int, mode: str, fast: bool, *, plant: bool = False
) -> dict:
    """Mirror the frozen #670 drive/quiet schedule; record the meter per quiet step.

    plant=True: during EVERY quiet step, add a distributed external K4 pump
    (V_inc[interior,:] += √ALPHA) BEFORE stepping — sustains Φ_link accumulation
    WITHOUT calling apply_seed (Cosserat u/ω NOT clobbered). Mirrors the #670
    sabotage plant's quiet-loop structure with the same primitives.
    """
    t0 = time.time()
    engine = _build_engine(N, pml, mode)
    coupled = engine._coupled
    mask = np.asarray(coupled._interior_mask(), dtype=bool)
    amp_pump = float(np.sqrt(ALPHA))

    tau = tau_steps_k4(coupled, fast=fast)
    n_drive = max(6 if fast else 10, int(round(0.5 * tau)))
    n_quiet = max(10 if fast else 20, int(round(1.5 * tau)))
    n_total = n_drive + n_quiet

    obs0 = snapshot_op14(coupled)
    phi_baseline = max(obs0["phi_link_sq"], PHI_BASELINE_FLOOR)
    obs_driveoff = obs0
    series: list[dict] = []
    for t in range(1, n_total + 1):
        if plant and t > n_drive:
            coupled.k4.V_inc[mask, :] += amp_pump  # distributed external sustenance
        engine.step()
        obs_t = snapshot_op14(coupled)
        if t == 1:
            phi_baseline = max(obs_t["phi_link_sq"], PHI_BASELINE_FLOOR)
        if t <= n_drive:
            obs_driveoff = obs_t
        if t >= n_drive:  # drive-off snapshot + every quiet step
            m = _meter_snapshot(coupled)
            m["t"] = t
            m["phase"] = "drive_off" if t == n_drive else "quiet"
            m["H"] = float(obs_t["H"])
            m["phi_link_sq"] = float(obs_t["phi_link_sq"])
            series.append(m)
    obs_end = obs_t

    phi_drive = max(obs_driveoff["phi_link_sq"], phi_baseline)
    H_drive = max(obs_driveoff["H"], 1e-30)
    E_persist = obs_end["H"] / H_drive
    phi_persist = obs_end["phi_link_sq"] / phi_drive if phi_drive > 0 else 0.0

    trend = {}
    stats = ["PR", "PR_frac"] + [f"CF_peak_{r}" for r in CORE_RADII] + [
        f"CF_geom_{r}" for r in CORE_RADII
    ]
    for sec in SECTORS:
        trend[sec] = {stat: _trend(series, sec, stat) for stat in stats}

    return {
        "N": N,
        "pml": pml,
        "boundary": "torus" if pml == 0 else "PML",
        "seed_mode": mode,
        "fidelity": "smoke" if fast else "production",
        "plant": plant,
        "n_drive": n_drive,
        "n_quiet": n_quiet,
        "E_persist": float(E_persist),
        "phi_persist": float(phi_persist),
        "E_floor": P11_E_PERSIST_MIN,
        "phi_floor": P11_A_PERSIST_MIN,
        "M_interior": series[-1]["M"],
        "trend": trend,
        "series": series,
        "wall_seconds": round(time.time() - t0, 1),
        "prereg": PREREG,
    }


def _classify_cell(res: dict) -> dict:
    """Per-cell CONCENTRATING / LOOP-FILLING signature on the energy (A1) meter."""
    e = res["trend"]["energy"]
    pr_rel = e["PR"]["rel_trend"]
    cf_rel = e[f"CF_peak_{PRIMARY_R}"]["rel_trend"]
    concentrating = (pr_rel <= -THETA) or (cf_rel >= THETA)
    loop_filling = (pr_rel >= -THETA) and (cf_rel <= THETA)
    resolvable = (abs(pr_rel) >= THETA) or (abs(cf_rel) >= THETA)
    if not resolvable:
        sig = "INCONCLUSIVE"
    elif concentrating and not loop_filling:
        sig = "CONCENTRATING"
    elif loop_filling and not concentrating:
        sig = "LOOP-FILLING"
    else:
        sig = "MIXED"
    return {
        "PR_energy_rel_trend": pr_rel,
        "CF_energy_rel_trend": cf_rel,
        "phi_persist": round(res["phi_persist"], 4),
        "signature": sig,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _cell_path(N, pml, mode, fast, plant=False) -> Path:
    fid = "smoke" if fast else "prod"
    tag = "plant" if plant else "cell"
    return OUT_DIR / f"{tag}_N{N}_pml{pml}_{mode}_{fid}.json"


def _write(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True))


def cmd_parity(argv) -> None:
    """Live-fire parity: mirror loop E/φ must match run_loop_gap_probe (≤1e-6 rel)."""
    N, pml, mode, fid = int(argv[0]), int(argv[1]), argv[2], argv[3]
    fast = fid == "smoke"
    ref = run_loop_gap_probe(
        f"parity_N{N}_pml{pml}_{mode}",
        rank_target=4,
        seed_mode=mode,
        N=N,
        pml=pml,
        bulk_density_on=True,
        front_target=A_YIELD,
        n_drive_mult=0.5,
        n_quiet_mult=1.5,
        fast=fast,
    )
    mine = run_instrumented(N, pml, mode, fast, plant=False)
    dE = abs(mine["E_persist"] - ref.E_persist_ratio) / max(abs(ref.E_persist_ratio), 1e-30)
    dP = abs(mine["phi_persist"] - ref.phi_persist_ratio) / max(
        abs(ref.phi_persist_ratio), 1e-30
    )
    ok = dE <= 1e-6 and dP <= 1e-6
    print(
        f"[parity] N={N} pml={pml} {mode} {fid}: "
        f"ref E={ref.E_persist_ratio:.6f} phi={ref.phi_persist_ratio:.6f} | "
        f"mirror E={mine['E_persist']:.6f} phi={mine['phi_persist']:.6f} | "
        f"relΔE={dE:.2e} relΔφ={dP:.2e} -> {'PASS' if ok else 'FAIL'}",
        flush=True,
    )
    _write(
        OUT_DIR / f"parity_N{N}_pml{pml}_{mode}_{fid}.json",
        {
            "ref_E": ref.E_persist_ratio,
            "ref_phi": ref.phi_persist_ratio,
            "mirror_E": mine["E_persist"],
            "mirror_phi": mine["phi_persist"],
            "rel_dE": dE,
            "rel_dphi": dP,
            "parity_pass": bool(ok),
            "prereg": PREREG,
        },
    )
    if not ok:
        raise SystemExit("PARITY FAILED — meter is on a different trajectory; run void")


def cmd_cell(argv) -> None:
    N, pml, mode, fid = int(argv[0]), int(argv[1]), argv[2], argv[3]
    assert mode in LANDED_SEED_MODES, mode
    fast = fid == "smoke"
    res = run_instrumented(N, pml, mode, fast, plant=False)
    res["classification"] = _classify_cell(res)
    _write(_cell_path(N, pml, mode, fast), res)
    c = res["classification"]
    print(
        f"[cell] N={N} pml={pml} {mode:10s} {fid:5s} "
        f"E={res['E_persist']:.4f} phi={res['phi_persist']:.4f} "
        f"PR_trend={c['PR_energy_rel_trend']:+.3f} CF_trend={c['CF_energy_rel_trend']:+.3f} "
        f"-> {c['signature']} [{res['wall_seconds']}s]",
        flush=True,
    )


def cmd_plant(argv) -> None:
    N, pml, mode, fid = int(argv[0]), int(argv[1]), argv[2], argv[3]
    fast = fid == "smoke"
    free = run_instrumented(N, pml, mode, fast, plant=False)
    plant = run_instrumented(N, pml, mode, fast, plant=True)
    e = plant["trend"]["energy"]
    loop_filling = (e["PR"]["rel_trend"] >= -THETA) and (
        e[f"CF_peak_{PRIMARY_R}"]["rel_trend"] <= THETA
    )
    a = plant["phi_persist"] >= P11_A_PERSIST_MIN  # φ sustained (fools retention floor)
    b = loop_filling  # meter flags externally-fed
    if a and b:
        verdict = "UN-FOOLABLE_CONFIRMED"
    elif a and not b:
        verdict = "FOOLABLE_SURFACE"
    else:
        verdict = "INCONCLUSIVE_phi_not_sustained"
    out = {
        "N": N,
        "pml": pml,
        "boundary": "torus" if pml == 0 else "PML",
        "seed_mode": mode,
        "fidelity": "smoke" if fast else "production",
        "free_phi_persist": round(free["phi_persist"], 4),
        "free_E_persist": round(free["E_persist"], 4),
        "plant_phi_persist": round(plant["phi_persist"], 4),
        "plant_E_persist": round(plant["E_persist"], 4),
        "plant_phi_sustained": bool(a),
        "plant_meter_loop_filling": bool(b),
        "plant_PR_energy_rel_trend": e["PR"]["rel_trend"],
        "plant_CF_energy_rel_trend": e[f"CF_peak_{PRIMARY_R}"]["rel_trend"],
        "verdict": verdict,
        "free_classification": _classify_cell(free),
        "plant_trend_energy": plant["trend"]["energy"],
        "prereg": PREREG,
    }
    _write(_cell_path(N, pml, mode, fast, plant=True), out)
    print(
        f"[plant] N={N} pml={pml} {mode} {fid}: "
        f"free_phi={out['free_phi_persist']:.3f} plant_phi={out['plant_phi_persist']:.3f} "
        f"sustained={a} loop_filling={b} -> {verdict}",
        flush=True,
    )


def cmd_aggregate() -> None:
    cells = [json.loads(p.read_text()) for p in sorted(OUT_DIR.glob("cell_*.json"))]
    plants = [json.loads(p.read_text()) for p in sorted(OUT_DIR.glob("plant_*.json"))]

    torus = [
        c
        for c in cells
        if c["pml"] == 0
        and c["seed_mode"] in ("pair", "graded_a0")
        and c["fidelity"] == "production"
    ]
    sigs = {c["seed_mode"]: c["classification"]["signature"] for c in torus}
    uniq = set(sigs.values())
    if not sigs:
        fork_bin = "NO-DATA"
    elif len(uniq) == 1 and "MIXED" not in uniq and "INCONCLUSIVE" not in uniq:
        fork_bin = uniq.pop()
    elif uniq == {"INCONCLUSIVE"}:
        fork_bin = "INCONCLUSIVE"
    else:
        fork_bin = "MIXED"

    summary = {
        "battery": "gpersist_localization_observable",
        "prereg": PREREG,
        "theta": THETA,
        "primary_core_radius": PRIMARY_R,
        "torus_signatures": sigs,
        "fork_bin": fork_bin,
        "cells": [
            {
                "N": c["N"],
                "boundary": c["boundary"],
                "seed_mode": c["seed_mode"],
                "fidelity": c["fidelity"],
                "E_persist": round(c["E_persist"], 4),
                "phi_persist": round(c["phi_persist"], 4),
                "PR_energy": c["trend"]["energy"]["PR"],
                "CF_energy_peak_2p0": c["trend"]["energy"][f"CF_peak_{PRIMARY_R}"],
                "PR_phi_link": c["trend"]["phi_link"]["PR"],
                "classification": c["classification"],
            }
            for c in sorted(
                cells, key=lambda c: (c["N"], c["pml"], c["fidelity"], c["seed_mode"])
            )
        ],
        "plants": [
            {k: p[k] for k in p if k != "plant_trend_energy"} for p in plants
        ],
    }
    _write(OUT_DIR / "gpersist_localization_summary.json", summary)

    print("\n=== per-cell concentration (energy A1 meter) ===")
    for c in summary["cells"]:
        pr = c["PR_energy"]
        cf = c["CF_energy_peak_2p0"]
        print(
            f"  N={c['N']} {c['boundary']:6s} {c['fidelity']:10s} {c['seed_mode']:10s} "
            f"E={c['E_persist']:.3f} phi={c['phi_persist']:.3f} | "
            f"PR {pr['start']:.1f}->{pr['end']:.1f} ({pr['rel_trend']:+.3f}) "
            f"CF {cf['start']:.3f}->{cf['end']:.3f} ({cf['rel_trend']:+.3f}) "
            f"=> {c['classification']['signature']}"
        )
    print(f"\ntorus signatures: {sigs}")
    print(f"FORK BIN (torus pair+graded_a0): {fork_bin}")
    print("\n=== φ-channel plants ===")
    for p in plants:
        print(
            f"  N={p['N']} {p['boundary']:6s} {p['seed_mode']:10s} {p['fidelity']:10s}: "
            f"free_phi={p['free_phi_persist']:.3f} plant_phi={p['plant_phi_persist']:.3f} "
            f"sustained={p['plant_phi_sustained']} loop_filling={p['plant_meter_loop_filling']} "
            f"-> {p['verdict']}"
        )
    print(f"\nsummary -> {OUT_DIR / 'gpersist_localization_summary.json'}")


def main(argv) -> None:
    if not argv:
        print(__doc__)
        return
    cmd, rest = argv[0], argv[1:]
    if cmd == "--parity":
        cmd_parity(rest)
    elif cmd == "--cell":
        cmd_cell(rest)
    elif cmd == "--plant":
        cmd_plant(rest)
    elif cmd == "--aggregate":
        cmd_aggregate()
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
