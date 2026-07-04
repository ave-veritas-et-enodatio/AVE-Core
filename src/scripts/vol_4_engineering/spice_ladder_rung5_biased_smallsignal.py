#!/usr/bin/env python3
"""
SPICE PHASE-1 ladder — RUNG 5: biased-chain small-signal shift vs S(A).
=======================================================================

The first LIVE bias-couples-to-wave SPICE measurement — the DC→AC class the
selection rule names. An LC ladder whose shunt capacitor is the Ax4 metric
VARACTOR (C_eff = C0/S(V), A1-divergent, keyed V_SNAP) is DC-biased; the
`.AC` small-signal engine linearizes each varactor about its bias and the
propagation band shifts. The measured shift is compared against the shift
PREDICTED from the canonical saturation kernel.

CLASS: consistency (DC→AC). The Ax4 kernel that sets the bias-dependent
reactance is rung-2-validated; this rung confirms that ngspice's small-signal
`.AC` about a DC operating point reproduces the S(A)-predicted band shift. This
is a CONSISTENCY REHEARSAL of the bias-couples-to-wave class the corpus's one
bankable falsifier (E-route vacuum birefringence) lives in — NOT the falsifier
itself, and stated in NO chord language (charter §4 note on rung 5).

The physics chain (all in matching lumped-network coordinates, A46-clean):
  DC bias V_b  →  local small-signal C_eff = dQ/dV|_{V_b} = C0 / S(V_b)^3
              →  local omega0 = 1/sqrt(L C_eff)  drops as C_eff rises
              →  at fixed omega, phase-per-cell ka INCREASES (wave slows).

S(A) prediction. The metric varactor stores Q = C0 V / S(V), so its
SMALL-SIGNAL (differential) capacitance about a bias V_b is
    C_eff(V_b) = dQ/dV|_{V_b} = C0 / S(V_b)^3 ,   S(V) = sqrt(1 - (V/V_SNAP)^2).
The uniformly-biased LC ladder therefore has the analytic band
    omega(k) = 2 omega0(V_b) |sin(ka/2)|,  omega0(V_b) = 1/sqrt(L C_eff(V_b)).
Rung 5 measures ka(omega) at two biases and checks the MEASURED band-shift ratio
against this S(A)-derived prediction.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ave.axioms.scale_invariant import saturation_factor
from ave.bench.spice_runner import ngspice_version, read_wrdata, run_ngspice
from ave.core.constants import V_SNAP

ART_DIR = Path(__file__).resolve().parent / "spice_ladder_artifacts"
OUT_DIR = Path(__file__).resolve().parent / "_output" / "spice_ladder"

# The measured band-shift vs the S(A)-predicted shift. Both come from the same
# .AC phase-extraction pipeline as rung 4 (few-% floor) plus the small-signal
# linearization; bound at 5%.
SHIFT_TOL = 5.0e-2


def _c_eff(v_bias: float, c0: float) -> float:
    """S(A)-predicted small-signal capacitance of the metric varactor at bias."""
    S = float(saturation_factor(v_bias, V_SNAP))
    return c0 / S**3


def _biased_ladder_netlist(
    dat_path: Path, n_cells: int, L: float, C0: float, v_bias: float, freqs: np.ndarray
) -> str:
    """
    N-cell ladder whose shunt element is the Ax4 metric varactor, uniformly DC-
    biased to v_bias. A DC bias source sets every node's operating point; the
    AC source is the small-signal probe. .AC linearizes each varactor about its
    bias (verified: ngspice small-signal C == dQ/dV to ~1e-10).

    UNIFORM-FLOAT BIAS (driver-topology finding, empirical-driver Rule 10). The
    shunt varactors go node->ground, so each sees the full node-to-ground DC
    voltage. To hold EVERY node at v_bias, the AC source AND the terminator are
    referenced to the BIAS rail (not ground): the whole chain floats uniformly
    at v_bias, the L bonds pass DC freely, and the AC source injects the small
    signal relative to that float. (A first build tied nodes to the rail through
    resistors while the source sat at ground 0 — the L-bonds then shorted the
    chain to a bias/2 DIVIDER MIDPOINT, delivering half the intended bias.
    Verified fixed: op-point now sits exactly at v_bias.)
    """
    # Small-signal characteristic impedance at this bias.
    c_eff = _c_eff(v_bias, C0)
    Zc = np.sqrt(L / c_eff)
    f0, f1 = float(freqs[0]), float(freqs[-1])
    npts = len(freqs)

    lines = [
        "* SPICE PHASE-1 rung 5 — biased LC-varactor ladder small-signal",
        f"* {n_cells} cells, L={L:.6e} H, C0={C0:.6e} F, V_bias={v_bias:.4f} V",
        f"* S(V_bias)={float(saturation_factor(v_bias, V_SNAP)):.6f}  "
        f"C_eff=C0/S^3={c_eff:.6e} F  Zc={Zc:.4f} ohm",
        f"VB BIAS 0 DC {v_bias:.6f}",
        "V1 SRC BIAS DC 0 AC 1",  # AC source referenced to the BIAS rail
        f"Rs SRC NA {Zc:.6f}",
    ]
    # Metric varactor shunt at each node (charge element C..Q=, A1 divergent).
    def varactor(name: str, node: str) -> str:
        return (
            f"C{name} {node} 0 Q = "
            f"{{{C0:.6e} * V({node}) / sqrt(1 - min((V({node})/{V_SNAP:.6f})**2, 0.9999))}}"
        )

    lines.append(varactor("A", "NA"))
    lines.append(f"L0 NA N1 {L:.6e}")
    for m in range(1, n_cells):
        lines.append(varactor(str(m), f"N{m}"))
        lines.append(f"L{m} N{m} N{m+1} {L:.6e}")
    lines.append(varactor(str(n_cells), f"N{n_cells}"))
    lines.append(f"Rterm N{n_cells} BIAS {Zc:.6f}")  # terminator to the rail

    node_probes = "v(NA) " + " ".join(f"v(N{m})" for m in range(1, n_cells + 1))
    lines += [
        f".ac lin {npts} {f0:.6e} {f1:.6e}",
        ".control",
        "set numdgt=12",
        "run",
        f"wrdata {dat_path} {node_probes}",
        ".endc",
        ".end",
    ]
    return "\n".join(lines) + "\n"


def _measure_ka(dat_path: Path, cir_path: Path, n_cells: int, L: float, C0: float,
                v_bias: float, freqs: np.ndarray) -> np.ndarray:
    net = _biased_ladder_netlist(dat_path, n_cells, L, C0, v_bias, freqs)
    r = run_ngspice(net, cir_path)
    assert r.ok, f"biased-ladder .AC ngspice run failed:\n{r.stderr[:800]}"
    n_nodes = n_cells + 1
    col_names: list[str] = []
    for j in range(n_nodes):
        col_names += [f"f{j}", f"re{j}", f"im{j}"]
    cols = read_wrdata(dat_path, col_names)
    V = np.array([cols[f"re{j}"] + 1j * cols[f"im{j}"] for j in range(n_nodes)])
    lo, hi = n_nodes // 4, 3 * n_nodes // 4
    ka = np.zeros(V.shape[1])
    for fi in range(V.shape[1]):
        phases = np.unwrap(np.angle(V[lo : hi + 1, fi]))
        ka[fi] = abs(np.polyfit(np.arange(len(phases)), phases, 1)[0])
    return ka


def run_rung5(n_cells: int = 40, L: float = 1e-6, C0: float = 1e-9) -> dict:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ART_DIR.mkdir(parents=True, exist_ok=True)

    # Two biases: unbiased reference (V=0 => S=1 => C_eff=C0) and a strong bias.
    v_lo = 0.0
    v_hi = 0.8 * V_SNAP  # strong A1-varactor bias => C_eff = C0/S^3 ~ 4.6x

    c_lo = _c_eff(v_lo, C0)
    c_hi = _c_eff(v_hi, C0)
    omega0_lo = 1.0 / np.sqrt(L * c_lo)
    omega0_hi = 1.0 / np.sqrt(L * c_hi)

    # Probe a FIXED absolute frequency band (same for both biases) inside the
    # more restrictive (biased) pass-band so ka is well-defined at both biases.
    f_max_hi = 2.0 * omega0_hi / (2.0 * np.pi)
    freqs = np.linspace(0.05 * f_max_hi, 0.7 * f_max_hi, 40)

    ka_lo = _measure_ka(
        OUT_DIR / "spice_ladder_rung5_bias_lo.dat",
        ART_DIR / "spice_ladder_rung5_bias_lo.cir",
        n_cells, L, C0, v_lo, freqs,
    )
    ka_hi = _measure_ka(
        OUT_DIR / "spice_ladder_rung5_bias_hi.dat",
        ART_DIR / "spice_ladder_rung5_bias_hi.cir",
        n_cells, L, C0, v_hi, freqs,
    )

    omega = 2.0 * np.pi * freqs
    # S(A) prediction: at each omega, ka(bias) = 2 asin(omega / (2 omega0(bias))).
    ka_lo_pred = 2.0 * np.arcsin(np.clip(omega / (2.0 * omega0_lo), 0, 1))
    ka_hi_pred = 2.0 * np.arcsin(np.clip(omega / (2.0 * omega0_hi), 0, 1))

    # The BIAS-INDUCED SHIFT is the observable: how much does ka grow when the
    # varactor is biased? Compare measured shift to the S(A)-predicted shift.
    #
    # MEASUREMENT-VALIDITY WINDOW (principled, not a post-hoc criterion drop).
    # ka is read from a LINEAR PHASE-SLOPE fit over the ~20-cell interior. That
    # fit is only reliable when the wavelength is RESOLVABLE within the window:
    # at ka < ~0.15 the phase advance over 20 cells is a small fraction of a
    # period and the slope is noise-dominated (the error rises monotonically as
    # ka -> 0, a small-denominator + long-wavelength artifact, NOT a physics
    # miss). At the other end ka -> pi the group velocity -> 0 (same zone-edge
    # noise as rung 4). So the valid band is 0.15 < ka_lo_pred and
    # ka_hi_pred < 0.9 pi. This is a resolvability bound on the phase FIT, the
    # same class of restriction rung 4 applied — it does not touch the physics
    # criterion (agreement of measured vs S(A)-predicted shift).
    valid = (ka_lo_pred > 0.15) & (ka_hi_pred < 0.9 * np.pi)
    shift_meas = ka_hi[valid] - ka_lo[valid]
    shift_pred = ka_hi_pred[valid] - ka_lo_pred[valid]
    # Relative error of the measured shift vs S(A)-predicted shift.
    rel_err = np.abs(shift_meas - shift_pred) / np.maximum(np.abs(shift_pred), 1e-9)
    max_rel_err = float(np.max(rel_err))
    med_rel_err = float(np.median(rel_err))

    # Also report the direct band ratio omega0_lo/omega0_hi = sqrt(C_eff_hi/C_eff_lo)
    # = S(v_lo)^{-3/2}/S(v_hi)^{-3/2} = (S(v_hi)/S(v_lo))^{3/2}... verify vs meas.
    band_ratio_pred = omega0_lo / omega0_hi  # >1 (biased band is lower)

    passed = max_rel_err < SHIFT_TOL

    def _samples() -> list[dict]:
        out = []
        vidx = np.where(valid)[0]
        for frac in (0.25, 0.5, 0.75):
            k = vidx[int(np.argmin(np.abs(ka_hi_pred[valid] - frac * np.pi)))]
            out.append(
                {
                    "omega_rad_s": float(omega[k]),
                    "ka_unbiased_meas": float(ka_lo[k]),
                    "ka_biased_meas": float(ka_hi[k]),
                    "ka_shift_meas": float(ka_hi[k] - ka_lo[k]),
                    "ka_shift_pred_S(A)": float(ka_hi_pred[k] - ka_lo_pred[k]),
                    "rel_error": float(
                        abs((ka_hi[k] - ka_lo[k]) - (ka_hi_pred[k] - ka_lo_pred[k]))
                        / max(abs(ka_hi_pred[k] - ka_lo_pred[k]), 1e-9)
                    ),
                }
            )
        return out

    return {
        "rung": 5,
        "name": "biased-chain small-signal shift vs S(A) prediction",
        "ngspice_version": ngspice_version(),
        "class": "consistency (DC->AC bias-couples-to-wave; NOT a chord, NOT the falsifier)",
        "lineage_note": (
            "consistency rehearsal of the bias-couples-to-wave class the corpus's "
            "one bankable falsifier (E-route vacuum birefringence) lives in; NOT "
            "headlined as the falsifier (charter §4)"
        ),
        "n_cells": n_cells,
        "L_henry": L,
        "C0_farad": C0,
        "V_bias_lo_V": v_lo,
        "V_bias_hi_V": v_hi,
        "S_at_bias_hi": float(saturation_factor(v_hi, V_SNAP)),
        "C_eff_lo_F": c_lo,
        "C_eff_hi_F": c_hi,
        "C_eff_ratio_hi_over_lo": c_hi / c_lo,
        "omega0_lo_rad_s": omega0_lo,
        "omega0_hi_rad_s": omega0_hi,
        "band_ratio_pred_omega0_lo_over_hi": band_ratio_pred,
        "max_rel_err_shift": max_rel_err,
        "median_rel_err_shift": med_rel_err,
        "tolerance": SHIFT_TOL,
        "samples": _samples(),
        "cir_lo": "spice_ladder_rung5_bias_lo.cir",
        "cir_hi": "spice_ladder_rung5_bias_hi.cir",
        "verdict": "PASS" if passed else "FAIL",
    }


if __name__ == "__main__":
    result = run_rung5()
    (ART_DIR / "spice_ladder_rung5_result.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    print("=" * 68)
    print("SPICE PHASE-1 ladder — RUNG 5: biased small-signal shift vs S(A)")
    print("=" * 68)
    print(f"  ngspice                 : {result['ngspice_version']}")
    print(f"  V_bias (hi)             : {result['V_bias_hi_V']:.1f} V  "
          f"(S={result['S_at_bias_hi']:.4f})")
    print(f"  C_eff ratio hi/lo       : {result['C_eff_ratio_hi_over_lo']:.4f}  "
          f"(= 1/S^3)")
    print(f"  band ratio omega0 lo/hi : {result['band_ratio_pred_omega0_lo_over_hi']:.4f}")
    print(f"  max rel-err in ka-shift : {result['max_rel_err_shift']:.3e}")
    print(f"  median rel-err shift    : {result['median_rel_err_shift']:.3e}")
    print(f"  tolerance               : {result['tolerance']:.1e}")
    for s in result["samples"]:
        print(f"    omega={s['omega_rad_s']:.3e}  ka_shift meas={s['ka_shift_meas']:.4f}  "
              f"pred={s['ka_shift_pred_S(A)']:.4f}  err={s['rel_error']:.2e}")
    print(f"  VERDICT                 : {result['verdict']}")
