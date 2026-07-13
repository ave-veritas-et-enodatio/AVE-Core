#!/usr/bin/env python3
"""Genesis N≥14 persistence battery (the G-PERSIST gate) — thin Rule-14 driver.

FROZEN prereg: research/2026-07-13_genesis-npersist-n14-battery_prereg_FROZEN.md
(freeze-by-push BEFORE this driver; the freeze commit precedes this file in git
history on analysis/genesis-npersist-n14-battery).

Handoff: _orchestration/2026-07-13_genesis-npersist-battery-handoff.md

Re-runs the #655 D2 persistence battery at N≥14 AND closed-box, all three landed
seed modes × both fidelities × both boundaries, to convert the boundary-confounded
N=10 read into a boundary-clean G-PERSIST adjudication.

Carrier = the EXISTING loop_gap_harness rank-4 probe. The ONLY change vs the
banked #655 D2 is two knobs: ``N`` and ``pml`` (pml=3 banked absorbing shell;
pml=0 fully-reflecting closed box). No new engine, no genesis_v{N}, no retune,
no detector change. Detector = frozen #655 P11 gate
(E_persist ≥ 0.85 AND φ_persist ≥ 0.80).

(B) node-birth (N→N+1) stays firewalled: this reads (A) fixed-N only.

Usage:
  # one measurement cell -> writes one JSON (parallel-friendly)
  python genesis_npersist_battery.py --cell N PML MODE FID   (FID: smoke|prod)
  # one sabotage negative-control -> writes one JSON
  python genesis_npersist_battery.py --plant N MODE PML
  # aggregate all cell JSONs -> summary JSON + adjudication table
  python genesis_npersist_battery.py --aggregate
  # run the whole frozen grid serially (slow; reproducibility/CI)
  python genesis_npersist_battery.py --all
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

from ave.core.genesis_v18_coupled import (
    P11_A_PERSIST_MIN,
    P11_E_PERSIST_MIN,
    snapshot_op14,
)
from ave.core.loop_gap_harness import _to_dict, make_engine, run_loop_gap_probe
from ave.core.loop_gap_seeds import A_LOCK_DEFAULT, A_YIELD, apply_seed

PREREG = "research/2026-07-13_genesis-npersist-n14-battery_prereg_FROZEN.md"
OUT_DIR = Path("assets/sim_outputs/genesis_npersist_battery")

# The three landed fixed-N seed modes (loop_gap_seeds.SeedMode).
LANDED_SEED_MODES: tuple[str, ...] = ("pair", "graded_a0", "photon_lock")

# Frozen boundary knobs: pml=3 = banked PML absorber; pml=0 = reflecting closed box.
PML_BANKED = 3
PML_CLOSED = 0

# Frozen grid (prereg §Mission). N=10 PML-only = reproduction anchor;
# N=14 both boundaries both fidelities = primary matched-N battery;
# N=16 both boundaries production = PML N-trend endpoint + closed-box box-size guard.
FROZEN_GRID: tuple[tuple[int, int, bool], ...] = tuple(
    # (N, pml, fast)
    [(10, PML_BANKED, fast) for fast in (True, False)]
    + [(14, pml, fast) for pml in (PML_BANKED, PML_CLOSED) for fast in (True, False)]
    + [(16, pml, False) for pml in (PML_BANKED, PML_CLOSED)]
)


def _persists(E: float, phi: float) -> bool:
    """Frozen #655 P11 detector — byte-unchanged floors."""
    return bool(E >= P11_E_PERSIST_MIN and phi >= P11_A_PERSIST_MIN)


def run_cell(N: int, pml: int, mode: str, fast: bool) -> dict:
    """One measurement cell — the banked #655 D2 config, only N and pml changed.

    d2 config (frozen off #654 §Gates 2): rank 4, bulk_density_on, front_target=
    A_YIELD, n_drive_mult=0.5, n_quiet_mult=1.5. fast=True SMOKE / fast=False prod.
    """
    t0 = time.time()
    r = run_loop_gap_probe(
        f"npersist_N{N}_pml{pml}_{mode}",
        N=N,
        pml=pml,
        rank_target=4,
        seed_mode=mode,
        bulk_density_on=True,
        front_target=A_YIELD,
        n_drive_mult=0.5,
        n_quiet_mult=1.5,
        fast=fast,
    )
    d = _to_dict(r)
    d.update(
        cell="measurement",
        N=N,
        pml=pml,
        boundary="closed_box" if pml == 0 else "PML",
        fidelity="smoke" if fast else "production",
        interior_sites=(N - 2 * pml) ** 3 if pml > 0 else N**3,
        E_persist=float(r.E_persist_ratio),
        phi_persist=float(r.phi_persist_ratio),
        persists=_persists(r.E_persist_ratio, r.phi_persist_ratio),
        E_floor=P11_E_PERSIST_MIN,
        phi_floor=P11_A_PERSIST_MIN,
        wall_seconds=round(time.time() - t0, 1),
        prereg=PREREG,
    )
    return d


def run_sabotage_plant(N: int, mode: str, pml: int = PML_CLOSED) -> dict:
    """Pre-registered adversarial negative control (prereg §Sabotage plant).

    Acts on the EVOLVED field, not a post-hoc arithmetic reduction: runs the real
    integrator, then during the quiet window RE-INJECTS the seed each step so
    energy is externally sustained ("disable the drive-off"). A valid detector
    must then FALSELY report a high E_persist / PASS — proving E_persist is read
    off the integrator's output and that a real (non-sustained) PASS is genuine.
    A plant that only rescales the printed ratio is rejected by the prereg.

    Mirrors the frozen probe's drive/quiet split at SMOKE budget using the SAME
    primitives (make_engine / apply_seed / snapshot_op14 / step) — no new stepper.
    """
    t0 = time.time()
    n_drive, n_quiet = 6, 12  # smoke-class budget (probe: n_total ≈ 18 at smoke)

    def _seed(eng):
        apply_seed(eng, mode, a_lock=A_LOCK_DEFAULT, front_target=A_YIELD)

    # --- honest control: free evolution (no re-injection), matched budget ---
    eng = make_engine(4, N=N, bulk_density_on=True, pml=pml)
    c = eng._coupled
    _seed(eng)
    eng.freeze_converter_wall()
    for _ in range(n_drive):
        eng.step()
    obs_d = snapshot_op14(c)
    for _ in range(n_quiet):
        eng.step()
    obs_e = snapshot_op14(c)
    free_E = obs_e["H"] / max(obs_d["H"], 1e-30)
    free_phi = (
        obs_e["phi_link_sq"] / obs_d["phi_link_sq"] if obs_d["phi_link_sq"] > 0 else 0.0
    )

    # --- sabotage: re-inject the seed EVERY quiet step (sustained forcing) ---
    engp = make_engine(4, N=N, bulk_density_on=True, pml=pml)
    cp = engp._coupled
    _seed(engp)
    engp.freeze_converter_wall()
    for _ in range(n_drive):
        engp.step()
    obs_dp = snapshot_op14(cp)
    for _ in range(n_quiet):
        _seed(engp)  # <-- external sustenance: the plant
        engp.step()
    obs_ep = snapshot_op14(cp)
    plant_E = obs_ep["H"] / max(obs_dp["H"], 1e-30)
    plant_phi = (
        obs_ep["phi_link_sq"] / obs_dp["phi_link_sq"]
        if obs_dp["phi_link_sq"] > 0
        else 0.0
    )

    plant_false_pass = _persists(plant_E, plant_phi)  # prereg criterion: full AND-gate
    free_pass = _persists(free_E, free_phi)
    # SCOPE HONESTY (adversarial review PR #670, finding #5): the prereg's criterion
    # for a valid plant is that the full AND-detector FALSELY PASSES. Re-injecting the
    # seed clobbers the Cosserat state and zeroes phi_link_sq (plant_phi -> 0), so the
    # AND-gate FAILS on phi ⇒ `plant_false_pass` is False for every plant. What the
    # plant DOES establish is that the E-CHANNEL is integrator-coupled (plant_E lifts
    # far above the free run under sustained forcing) — but the E-channel is exactly
    # the channel that is degenerate in the closed box (E_persist ≡ 1 identity). The
    # LOAD-BEARING phi-channel is NOT exercised (the plant destroys phi rather than
    # sustaining it). A proper phi-channel negative control (sustain phi WITHOUT
    # clobbering the Cosserat state) is a follow-on, alongside the localization axis.
    e_channel_integrator_coupled = plant_E > free_E + 1e-6
    return {
        "cell": "sabotage_plant",
        "N": N,
        "pml": pml,
        "boundary": "closed_box" if pml == 0 else "PML",
        "mode": mode,
        "free_E_persist": float(free_E),
        "free_phi_persist": float(free_phi),
        "free_pass": free_pass,
        "plant_E_persist": float(plant_E),
        "plant_phi_persist": float(plant_phi),
        # prereg criterion (full AND-gate false-PASS): False for all (phi clobbered)
        "plant_false_pass": plant_false_pass,
        # what the plant actually establishes: E-channel integrator coupling only
        "e_channel_integrator_coupled": e_channel_integrator_coupled,
        "phi_channel_exercised": False,  # re-injection zeroes phi; not tested here
        "n_drive": n_drive,
        "n_quiet": n_quiet,
        "wall_seconds": round(time.time() - t0, 1),
        "prereg": PREREG,
        "note": (
            "plant re-injects seed each quiet step (external sustenance on the "
            "evolved field). It CLOBBERS phi (plant_phi->0), so plant_false_pass is "
            "False under the prereg's full-AND-gate criterion; it establishes only "
            "E-channel integrator coupling (plant_E >> free_E), NOT the load-bearing "
            "phi channel. Prior meaning: a valid detector reports a materially higher/false "
            "PASS vs the free run"
        ),
    }


def _cell_path(N: int, pml: int, mode: str, fast: bool) -> Path:
    fid = "smoke" if fast else "prod"
    return OUT_DIR / f"cell_N{N}_pml{pml}_{mode}_{fid}.json"


def _write(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True))


def cmd_cell(argv: list[str]) -> None:
    N, pml, mode, fid = int(argv[0]), int(argv[1]), argv[2], argv[3]
    assert mode in LANDED_SEED_MODES, mode
    assert fid in ("smoke", "prod"), fid
    fast = fid == "smoke"
    d = run_cell(N, pml, mode, fast)
    _write(_cell_path(N, pml, mode, fast), d)
    print(
        f"[cell] N={N} pml={pml} {mode:10s} {fid:5s} "
        f"E={d['E_persist']:.4f} phi={d['phi_persist']:.4f} "
        f"persists={d['persists']} [{d['wall_seconds']}s]",
        flush=True,
    )


def cmd_plant(argv: list[str]) -> None:
    N, mode = int(argv[0]), argv[1]
    pml = int(argv[2]) if len(argv) > 2 else PML_CLOSED
    d = run_sabotage_plant(N, mode, pml)
    _write(OUT_DIR / f"plant_N{N}_pml{pml}_{mode}.json", d)
    print(
        f"[plant] N={N} pml={pml} {mode}: free_E={d['free_E_persist']:.4f} "
        f"plant_E={d['plant_E_persist']:.4f} false_pass={d['plant_false_pass']} "
        f"E_coupled={d['e_channel_integrator_coupled']} [{d['wall_seconds']}s]",
        flush=True,
    )


def cmd_aggregate() -> None:
    cells = sorted(OUT_DIR.glob("cell_*.json"))
    rows = [json.loads(p.read_text()) for p in cells]
    plants = [json.loads(p.read_text()) for p in sorted(OUT_DIR.glob("plant_*.json"))]

    # Per-fidelity bins (frozen), at each (N, boundary). bin (i) A-SUPPORTED iff
    # ≥1 landed mode persists; else (ii) A-WEAKENED.
    def bin_for(N, pml, fid):
        grp = [r for r in rows if r["N"] == N and r["pml"] == pml and r["fidelity"] == fid]
        if not grp:
            return None
        n_pass = sum(1 for r in grp if r["persists"])
        return {
            "N": N,
            "pml": pml,
            "boundary": "closed_box" if pml == 0 else "PML",
            "fidelity": fid,
            "n_modes": len(grp),
            "n_persist": n_pass,
            "bin": "i_A_SUPPORTED" if n_pass >= 1 else "ii_A_WEAKENED",
            "modes": {r["seed_mode"]: round(r["E_persist"], 4) for r in grp},
            "phi": {r["seed_mode"]: round(r["phi_persist"], 4) for r in grp},
        }

    bins = []
    for N in sorted({r["N"] for r in rows}):
        for pml in sorted({r["pml"] for r in rows if r["N"] == N}):
            for fid in ("smoke", "production"):
                b = bin_for(N, pml, fid)
                if b:
                    bins.append(b)

    # Boundary-artifact axis: closed vs PML at matched N (production primary).
    boundary_axis = []
    for N in sorted({r["N"] for r in rows}):
        for fid in ("smoke", "production"):
            pml_grp = {r["seed_mode"]: r for r in rows if r["N"] == N and r["pml"] == PML_BANKED and r["fidelity"] == fid}
            cb_grp = {r["seed_mode"]: r for r in rows if r["N"] == N and r["pml"] == PML_CLOSED and r["fidelity"] == fid}
            if not (pml_grp and cb_grp):
                continue
            per_mode = {}
            for m in LANDED_SEED_MODES:
                if m in pml_grp and m in cb_grp:
                    per_mode[m] = {
                        "PML_E": round(pml_grp[m]["E_persist"], 4),
                        "closed_E": round(cb_grp[m]["E_persist"], 4),
                        "PML_persists": pml_grp[m]["persists"],
                        "closed_persists": cb_grp[m]["persists"],
                        "recovers": (not pml_grp[m]["persists"]) and cb_grp[m]["persists"],
                    }
            boundary_axis.append({"N": N, "fidelity": fid, "per_mode": per_mode})

    summary = {
        "battery": "genesis_npersist_n14",
        "prereg": PREREG,
        "handoff": "_orchestration/2026-07-13_genesis-npersist-battery-handoff.md",
        "detector": {"E_floor": P11_E_PERSIST_MIN, "phi_floor": P11_A_PERSIST_MIN,
                     "rule": "E_persist>=E_floor AND phi_persist>=phi_floor"},
        "n_cells": len(rows),
        "per_fidelity_bins": bins,
        "boundary_artifact_axis": boundary_axis,
        "sabotage_plants": plants,
        "cells": rows,
    }
    _write(OUT_DIR / "genesis_npersist_battery_summary.json", summary)

    # Human table.
    print("\n=== per-cell (E_persist / phi_persist / persists) ===")
    for r in sorted(rows, key=lambda r: (r["N"], r["pml"], r["fidelity"], r["seed_mode"])):
        print(
            f"  N={r['N']:2d} {r['boundary']:10s} {r['fidelity']:10s} "
            f"{r['seed_mode']:10s} E={r['E_persist']:.4f} phi={r['phi_persist']:.4f} "
            f"-> {'PASS' if r['persists'] else 'fail'}  (interior {r['interior_sites']})"
        )
    print("\n=== per-fidelity bins (i A-SUPPORTED / ii A-WEAKENED) ===")
    for b in bins:
        print(f"  N={b['N']:2d} {b['boundary']:10s} {b['fidelity']:10s} "
              f"{b['n_persist']}/{b['n_modes']} -> {b['bin']}")
    print("\n=== boundary-artifact axis (closed vs PML, matched N) ===")
    for ba in boundary_axis:
        for m, v in ba["per_mode"].items():
            print(f"  N={ba['N']:2d} {ba['fidelity']:10s} {m:10s} "
                  f"PML_E={v['PML_E']:.4f}({'P' if v['PML_persists'] else 'f'}) "
                  f"closed_E={v['closed_E']:.4f}({'P' if v['closed_persists'] else 'f'}) "
                  f"recovers={v['recovers']}")
    print("\n=== sabotage plants ===")
    for p in plants:
        print(f"  N={p['N']} pml={p['pml']} {p['mode']}: free_E={p['free_E_persist']:.4f} "
              f"plant_E={p['plant_E_persist']:.4f} false_pass={p['plant_false_pass']} "
              f"E_coupled={p.get('e_channel_integrator_coupled', p.get('valid_negative_control'))}")
    print(f"\nsummary -> {OUT_DIR / 'genesis_npersist_battery_summary.json'}")


def cmd_all() -> None:
    for (N, pml, fast) in FROZEN_GRID:
        for mode in LANDED_SEED_MODES:
            cmd_cell([str(N), str(pml), mode, "smoke" if fast else "prod"])
    cmd_aggregate()


def main(argv: list[str]) -> None:
    if not argv:
        print(__doc__)
        return
    cmd, rest = argv[0], argv[1:]
    if cmd == "--cell":
        cmd_cell(rest)
    elif cmd == "--plant":
        cmd_plant(rest)
    elif cmd == "--aggregate":
        cmd_aggregate()
    elif cmd == "--all":
        cmd_all()
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
