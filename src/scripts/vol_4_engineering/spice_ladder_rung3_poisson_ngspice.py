#!/usr/bin/env python3
"""
SPICE PHASE-1 ladder — RUNG 3: Poisson cross-check, now with REAL ngspice.
==========================================================================

The charter's rung 3 was "DONE" in the pilot
(`spice_lane_pilot_poisson.py`) — but only in NUMPY: the pilot built the
identical MNA matrix ngspice would build and matched it to a graph-Laplacian
solve at 7.55e-15, while ngspice itself never ran (charter §3 caveat). This
rung **closes that loop**: it re-runs the pilot's resistor-network `.cir`
through the actual ngspice `.OP` engine and compares the node potentials
against BOTH numpy paths.

CLASS: consistency. `.OP` builds `G v = i` (the conductance/weighted
graph-Laplacian with the ground row/col deleted — the principled neutrality
fix, charter design-(e)). A three-way agreement (ngspice ⟷ numpy-MNA ⟷
graph-Laplacian) is a genuine cross-engine consistency check: the pilot's
numpy MNA is now confirmed to be exactly what a real SPICE engine solves.

Method. Reuse the pilot's `build_random_resistor_graph` / `solve_mna` /
`solve_laplacian_pinned` / `emit_netlist` (imported, not reimplemented — the
pilot IS the reusable harness, charter design-(g)). Run the emitted `.cir`
through ngspice, parse the `.OP` node voltages, and diff against the numpy
solves at the SAME nodes.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

from ave.bench.spice_runner import ngspice_version, parse_op_voltages, run_ngspice

ART_DIR = Path(__file__).resolve().parent / "spice_ladder_artifacts"

# ngspice .OP vs numpy: both solve the SAME linear system in double precision
# (the numpy MNA<->Laplacian pair agrees at 7.55e-15, the pilot's dense-double
# floor). The ngspice-vs-numpy diff is bounded by ngspice's `print` TEXT
# SERIALIZATION, not the solve. Confirmed empirically: at the default ~7 sig
# figs the diff is 3.7e-7 V; bumping to `set numdgt=15` shrinks it to 4.2e-10 V
# (the residual TRACKS the print precision => it IS a serialization artifact,
# NOT a solver difference — ngspice sparse-LU .OP == numpy dense MNA). The
# driver uses numdgt=15 and a tolerance comfortably above that 4e-10 floor.
POISSON_ABS_TOL = 1.0e-8  # volts — above the numdgt=15 print floor (~4e-10)


def _load_pilot():
    """Import the pilot module by path (it lives in scripts/, not a package)."""
    pilot_path = Path(__file__).resolve().parent / "spice_lane_pilot_poisson.py"
    spec = importlib.util.spec_from_file_location("spice_lane_pilot_poisson", pilot_path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_rung3(n: int = 24, seed: int = 20260703) -> dict:
    ART_DIR.mkdir(parents=True, exist_ok=True)
    pilot = _load_pilot()

    # Same graph the pilot verified in numpy (default n/seed).
    L, edges = pilot.build_random_resistor_graph(n, seed)
    ground = 0
    inject = {n - 1: 1.0e-3}  # 1 mA into the far node

    v_mna = pilot.solve_mna(L, ground, inject)
    v_lap = pilot.solve_laplacian_pinned(L, ground, inject)

    # Emit the ngspice-ready .cir from the pilot, then rewrite its .control
    # block to print each node in the unambiguous v(Nk) form (the pilot's
    # `print all` emits bare `nk = ...` which is harder to disambiguate). The
    # ELEMENTS (resistors + current source) are the pilot's verbatim emission —
    # the physics under test is unchanged; only the output directive differs.
    base = pilot.emit_netlist(edges, ground, inject)
    print_lines = " ".join(f"v(N{k})" for k in range(n) if k != ground)
    netlist_lines = []
    for line in base.splitlines():
        if line.strip() == "run":
            netlist_lines.append("set numdgt=15")  # full-precision .OP print
            netlist_lines.append("run")
        elif line.strip() == "print all":
            netlist_lines.append(f"print {print_lines}")
        else:
            netlist_lines.append(line)
    netlist = "\n".join(netlist_lines) + "\n"

    cir_path = ART_DIR / "spice_ladder_rung3_poisson.cir"
    r = run_ngspice(netlist, cir_path)
    assert r.ok, f"Poisson .OP ngspice run failed:\n{r.stderr[:800]}"

    # ngspice node names: N<k> for k != ground, node 0 for ground.
    op_volts = parse_op_voltages(r.stdout)  # keys lowercased, e.g. "n5"
    v_ngspice = np.zeros(n)
    missing = []
    for k in range(n):
        if k == ground:
            v_ngspice[k] = 0.0
            continue
        key = f"n{k}"
        if key not in op_volts:
            missing.append(key)
        else:
            v_ngspice[k] = op_volts[key]
    assert not missing, f"ngspice .OP did not report nodes: {missing}\nstdout:\n{r.stdout[:600]}"

    max_ng_vs_mna = float(np.max(np.abs(v_ngspice - v_mna)))
    max_ng_vs_lap = float(np.max(np.abs(v_ngspice - v_lap)))
    max_mna_vs_lap = float(np.max(np.abs(v_mna - v_lap)))

    passed = (max_ng_vs_mna < POISSON_ABS_TOL) and (max_ng_vs_lap < POISSON_ABS_TOL)

    return {
        "rung": 3,
        "name": "Poisson .OP cross-check — real ngspice vs numpy MNA vs Laplacian",
        "ngspice_version": ngspice_version(),
        "class": "consistency (real SPICE .OP == numpy MNA == graph-Laplacian)",
        "n_nodes": n,
        "n_edges": len(edges),
        "seed": seed,
        "ground_node": ground,
        "inject_mA": {str(k): v * 1e3 for k, v in inject.items()},
        "max_abs_diff_ngspice_vs_mna_V": max_ng_vs_mna,
        "max_abs_diff_ngspice_vs_laplacian_V": max_ng_vs_lap,
        "max_abs_diff_mna_vs_laplacian_V": max_mna_vs_lap,
        "tolerance_V": POISSON_ABS_TOL,
        "closes_pilot_caveat": (
            "pilot matched MNA<->Laplacian at 7.55e-15 in numpy but ngspice "
            "never ran (charter §3 caveat); this rung closes the loop with the "
            "live ngspice-46 .OP engine"
        ),
        "cir": cir_path.name,
        "verdict": "PASS" if passed else "FAIL",
    }


if __name__ == "__main__":
    result = run_rung3()
    (ART_DIR / "spice_ladder_rung3_result.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    print("=" * 68)
    print("SPICE PHASE-1 ladder — RUNG 3: Poisson .OP, real ngspice")
    print("=" * 68)
    print(f"  ngspice                     : {result['ngspice_version']}")
    print(f"  graph                       : {result['n_nodes']} nodes, {result['n_edges']} edges")
    print(f"  max|v_ngspice - v_MNA|      : {result['max_abs_diff_ngspice_vs_mna_V']:.3e} V")
    print(f"  max|v_ngspice - v_Laplacian|: {result['max_abs_diff_ngspice_vs_laplacian_V']:.3e} V")
    print(f"  max|v_MNA - v_Laplacian|    : {result['max_abs_diff_mna_vs_laplacian_V']:.3e} V  (pilot path)")
    print(f"  tolerance                   : {result['tolerance_V']:.1e} V")
    print(f"  VERDICT                     : {result['verdict']}")
