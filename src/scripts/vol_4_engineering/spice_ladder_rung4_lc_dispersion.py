#!/usr/bin/env python3
"""
SPICE PHASE-1 ladder — RUNG 4: 1D LC-chain dispersion ω(k).
===========================================================

An N-cell LC transmission-line ladder (series L per bond, shunt C per node)
is the lumped-network 1D lattice. Its discrete dispersion is the textbook

    ω(k) = 2 ω_0 |sin(k a / 2)|,     ω_0 = 1/√(LC),

where a is the cell pitch and k a ∈ (0, π] is the phase advance PER CELL. This
is the discrete-lattice band (a cutoff at ω_max = 2 ω_0 where k a = π — the
Brillouin-zone edge), NOT the continuum ω = c k line. Recovering it from
ngspice `.AC` is the lane's first WAVE cross-check.

CLASS: manifestation (the ngspice `.AC` phase-per-cell == the analytic
LC-ladder band). PHASE-SPACE-COORDINATE-CHECK: both the measurement and the
prediction live in the SAME coordinate — a lumped-network ω-vs-(phase-per-cell)
dispersion. No real-space-Cartesian-vs-phase-space mismatch (A46): this rung
does not touch a φ² substrate claim; it validates that ngspice reproduces the
discrete-lattice band, which is the substrate-native transmission-line the SPICE
lane owns.

Method. Drive node 0 of an N-cell ladder with a 1 V AC source through a
matched-ish termination; sweep frequency; read the COMPLEX node voltages
(wrdata emits freq, real, imag per node in `.AC`). The phase advance per cell,
Δφ = arg(V_{m+1}/V_m), gives the measured k a at each ω. Compare the measured
ω(ka) against the analytic band across the pass-band. A driven lossy ladder has
a reflected wave; to isolate the FORWARD travelling-wave phase we use a long
chain and read cells in the interior away from both ends, and terminate in the
ladder's characteristic impedance Z_c = √(L/C) to suppress the reflection.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ave.bench.spice_runner import ngspice_version, read_wrdata, run_ngspice

ART_DIR = Path(__file__).resolve().parent / "spice_ladder_artifacts"
OUT_DIR = Path(__file__).resolve().parent / "_output" / "spice_ladder"

# Dispersion-match tolerance: the analytic band is exact; ngspice .AC is a
# linear solve, so error is the phase-extraction discretization + finite-chain
# reflection residual. Expect a few % in ka; bound at 5%.
DISPERSION_TOL = 5.0e-2


def _ladder_netlist(dat_path: Path, n_cells: int, L: float, C: float, freqs: np.ndarray) -> str:
    """
    N-cell LC ladder: node 0 driven, series L to next node, shunt C to ground
    at each node, terminated in Z_c = sqrt(L/C). Reads the COMPLEX voltage at
    every node via wrdata (.AC => freq, re, im per node).
    """
    Zc = np.sqrt(L / C)
    f0, f1 = float(freqs[0]), float(freqs[-1])
    npts = len(freqs)
    lines = [
        "* SPICE PHASE-1 rung 4 — 1D LC-ladder dispersion",
        f"* {n_cells} cells, L={L:.6e} H, C={C:.6e} F, Zc={Zc:.4f} ohm",
        f"* omega_0 = 1/sqrt(LC) = {1.0/np.sqrt(L*C):.6e} rad/s",
        "V1 N0 0 AC 1",
        f"Rs N0 NA {Zc:.6f}",  # source series impedance ~ Zc (soft launch)
    ]
    # bond m connects node m -> node m+1 via series L; shunt C at each node.
    # NA is the first ladder node after the source resistor.
    lines.append(f"L0 NA N1 {L:.6e}")
    lines.append(f"C0 NA 0 {C:.6e}")
    for m in range(1, n_cells):
        lines.append(f"L{m} N{m} N{m+1} {L:.6e}")
        lines.append(f"C{m} N{m} 0 {C:.6e}")
    # terminate the last node in Zc (matched load => forward-only wave)
    lines.append(f"C{n_cells} N{n_cells} 0 {C:.6e}")
    lines.append(f"Rterm N{n_cells} 0 {Zc:.6f}")

    # wrdata every node NA..N{n_cells}
    node_probes = "v(NA) " + " ".join(f"v(N{m})" for m in range(1, n_cells + 1))
    lines += [
        f".ac lin {npts} {f0:.6e} {f1:.6e}",
        ".control",
        "run",
        f"wrdata {dat_path} {node_probes}",
        ".endc",
        ".end",
    ]
    return "\n".join(lines) + "\n"


def run_rung4(n_cells: int = 40, L: float = 1e-6, C: float = 1e-9) -> dict:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ART_DIR.mkdir(parents=True, exist_ok=True)

    omega0 = 1.0 / np.sqrt(L * C)
    f_max = 2.0 * omega0 / (2.0 * np.pi)  # ladder cutoff f = omega_max/2pi
    # Sample the pass-band up to ~85% of cutoff (near ka=pi the group velocity
    # -> 0 and the finite chain + phase-unwrap get noisy).
    freqs = np.linspace(0.03 * f_max, 0.85 * f_max, 60)

    dat = OUT_DIR / "spice_ladder_rung4_dispersion.dat"
    cir = ART_DIR / "spice_ladder_rung4_dispersion.cir"
    net = _ladder_netlist(dat, n_cells, L, C, freqs)
    r = run_ngspice(net, cir)
    assert r.ok, f"LC-ladder .AC ngspice run failed:\n{r.stderr[:800]}"

    # wrdata columns: per node -> (freq, re, im). Node order: NA, N1..N{n}.
    n_nodes = n_cells + 1  # NA + N1..N{n_cells}
    col_names: list[str] = []
    for j in range(n_nodes):
        col_names += [f"f{j}", f"re{j}", f"im{j}"]
    cols = read_wrdata(dat, col_names)
    f = cols["f0"]

    # Build complex node voltages V[node, freq].
    V = np.array([cols[f"re{j}"] + 1j * cols[f"im{j}"] for j in range(n_nodes)])

    # Measure phase advance per cell in the INTERIOR (avoid source + load ends).
    lo, hi = n_nodes // 4, 3 * n_nodes // 4  # interior window
    ka_meas = np.zeros(len(f))
    for fi in range(len(f)):
        # phase of each interior node
        phases = np.unwrap(np.angle(V[lo : hi + 1, fi]))
        # linear fit: phase vs cell index => slope = -ka (forward wave)
        idx = np.arange(len(phases))
        slope = np.polyfit(idx, phases, 1)[0]
        ka_meas[fi] = abs(slope)

    omega = 2.0 * np.pi * f
    # analytic ka for each omega: omega = 2 omega0 sin(ka/2) => ka = 2 asin(omega/(2 omega0))
    arg = np.clip(omega / (2.0 * omega0), 0.0, 1.0)
    ka_analytic = 2.0 * np.arcsin(arg)

    # Compare where the analytic ka is well-defined (< ~0.9 pi) and measurable.
    valid = (ka_analytic > 0.05) & (ka_analytic < 0.9 * np.pi)
    rel_err = np.abs(ka_meas[valid] - ka_analytic[valid]) / ka_analytic[valid]
    max_rel_err = float(np.max(rel_err))
    med_rel_err = float(np.median(rel_err))

    passed = max_rel_err < DISPERSION_TOL

    def _samples() -> list[dict]:
        out = []
        for target in (0.25, 0.5, 0.75):
            k = int(np.argmin(np.abs(ka_analytic - target * np.pi)))
            out.append(
                {
                    "omega_over_omega0": float(omega[k] / omega0),
                    "ka_analytic": float(ka_analytic[k]),
                    "ka_measured": float(ka_meas[k]),
                    "rel_error": float(abs(ka_meas[k] - ka_analytic[k]) / ka_analytic[k]),
                }
            )
        return out

    return {
        "rung": 4,
        "name": "1D LC-chain dispersion omega(k) vs analytic band",
        "ngspice_version": ngspice_version(),
        "class": "manifestation (ngspice .AC phase-per-cell == analytic LC-ladder band)",
        "coordinate_note": "lumped-network omega-vs-(phase-per-cell); measurement + prediction in matching coords (phase-space-coordinate-check ok)",
        "n_cells": n_cells,
        "L_henry": L,
        "C_farad": C,
        "omega0_rad_s": omega0,
        "cutoff_omega_over_omega0": 2.0,
        "n_freqs": len(f),
        "max_rel_err_ka": max_rel_err,
        "median_rel_err_ka": med_rel_err,
        "tolerance": DISPERSION_TOL,
        "samples": _samples(),
        "cir": cir.name,
        "verdict": "PASS" if passed else "FAIL",
    }


if __name__ == "__main__":
    result = run_rung4()
    (ART_DIR / "spice_ladder_rung4_result.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    print("=" * 68)
    print("SPICE PHASE-1 ladder — RUNG 4: 1D LC-chain dispersion")
    print("=" * 68)
    print(f"  ngspice            : {result['ngspice_version']}")
    print(f"  chain              : {result['n_cells']} cells")
    print(f"  omega_0            : {result['omega0_rad_s']:.6e} rad/s")
    print(f"  max rel-err in ka  : {result['max_rel_err_ka']:.3e}")
    print(f"  median rel-err ka  : {result['median_rel_err_ka']:.3e}")
    print(f"  tolerance          : {result['tolerance']:.1e}")
    for s in result["samples"]:
        print(f"    omega/omega0={s['omega_over_omega0']:.3f}  ka_an={s['ka_analytic']:.4f}  "
              f"ka_meas={s['ka_measured']:.4f}  err={s['rel_error']:.2e}")
    print(f"  VERDICT            : {result['verdict']}")
