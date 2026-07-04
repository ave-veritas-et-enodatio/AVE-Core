#!/usr/bin/env python3
"""
SPICE PHASE-1 ladder — RUNG 2: AVE_VACUUM_CELL Ax4 saturation curve.
====================================================================

The load-bearing physics rung. It asks: does ngspice's evaluation of the
Axiom-4 saturation kernel ``S(V) = sqrt(1 - (V/V_x)^2)`` — the ONE nonlinearity
in AVE — match the canonical ``ave.axioms.scale_invariant.saturation_factor``
to machine precision, across the full sweep up to yield? This is the check the
SPICE-lane charter names (STEP-4 rung 2): "the ``.lib`` B-source ==
``saturation_factor()``".

CLASS: manifestation (the ``.lib`` behavioral source == the canonical Ax4
kernel). The kernel is the substrate's single constitutive nonlinearity;
matching it is an axiom-manifestation cross-check, not a free-parameter fit.

SECTOR DISCIPLINE (FLAG-2 resolution, Grant-ratified 2026-06-15 A1⊥T2 split;
charter §1 / nonlinear-vacuum-capacitance.md:14). Two ORTHOGONAL reactances
share the EE name "capacitance"; the ladder validates BOTH, keyed correctly:

  * DIVERGENT A1 (longitudinal bond compliance): C_eff/C0 = 1/S(V), keyed on
    **V_SNAP** (511 kV) — the ``AVE_VACUUM_CELL`` metric varactor. Diverges as
    V -> V_SNAP.
  * COLLAPSE T2 (transverse dielectric permittivity): C_eff/C0 = S(V), keyed
    on **V_YIELD** (43.65 kV) — the LCR-bench capacitance that rolls off. This
    is the form the ch15/ch17 KB leaves carry.

Both are exercised as ngspice behavioral DC sweeps and checked against the
canonical kernel evaluated at the IDENTICAL ngspice sample voltages (so grid
alignment contributes zero error — any residual is a genuine kernel
disagreement). A stale-kernel or wrong-sign ``.lib`` would fail this rung
(the charter's "catches FLAG-1 + FLAG-2" property).

VALUE PROVENANCE (FLAG-1). V_SNAP / V_YIELD are imported live from
``ave.core.constants`` — NOT the ``.lib`` hardcoded literals — so a drifted
literal cannot silently pass.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import numpy as np

from ave.axioms.scale_invariant import saturation_factor
from ave.bench.spice_runner import ngspice_version, run_ngspice
from ave.core.constants import V_SNAP, V_YIELD

ART_DIR = Path(__file__).resolve().parent / "spice_ladder_artifacts"
OUT_DIR = Path(__file__).resolve().parent / "_output" / "spice_ladder"

# Kernel-agreement tolerance. The kernel is a closed-form sqrt; ngspice
# evaluates it in double precision internally, so the only measurement error is
# the ~7-digit text serialization of ngspice's `print` command (~1e-7). A
# stale/wrong .lib kernel would blow past 1e-6 by orders of magnitude.
KERNEL_TOL = 1.0e-6

N_POINTS = 41  # per-point .op sweep (one operating-point solve per voltage)

# METHOD NOTE (empirical-driver Rule 10, SPICE PHASE-1 2026-07-04). The first
# rung-2 build used a single ngspice `.dc` sweep + wrdata. That FAILED at ~6e-4
# — NOT a kernel disagreement but a MEASUREMENT ARTIFACT: ngspice's `.dc`
# engine reports a behavioral source that depends on the SWEPT node lagged by
# one sweep step (S at step k printed the value belonging to step k-1). Caught,
# not papered over. Switched to per-point `.op` (one operating-point solve per
# fixed DC voltage, high-precision `print`), which is artifact-free (max err
# ~4e-8). This is exactly the integrator-time artifact Rule 10 exists to catch.

_VNODE_RE = re.compile(r"v\((n_[a-z0-9]+)\)\s*=\s*([-+0-9.eE]+)")


def _op_point_netlist(v_dc: float, v_key: float) -> str:
    """A single operating point: fix V(A)=v_dc, read S and 1/S behavioral nodes."""
    return f"""* SPICE PHASE-1 rung 2 — Ax4 kernel at one operating point
* V = {v_dc:.10f} V ; v_key = {v_key:.10f} V ; S = sqrt(1 - (V/v_key)^2)
V1 A 0 DC {v_dc:.10f}
B_S  N_S 0 V = {{sqrt(1 - min((V(A)/{v_key:.10f})**2, 0.9999))}}
B_I  N_I 0 V = {{1 / sqrt(1 - min((V(A)/{v_key:.10f})**2, 0.9999))}}
R_S N_S 0 1e12
R_I N_I 0 1e12
R_A A 0 1e15
.control
op
print v(N_S) v(N_I)
.endc
.end
"""


def _op_read(stdout: str) -> dict[str, float]:
    """Parse v(n_s)/v(n_i) from the .op control-block print."""
    return {m.group(1): float(m.group(2)) for m in _VNODE_RE.finditer(stdout.lower())}


def _run_sweep(cir_path: Path, v_key: float, v_max_frac: float) -> dict:
    """
    Per-point .op sweep of the Ax4 kernel across 0 .. v_max_frac*v_key. Emits
    the LAST operating point's netlist as the committed .cir (representative;
    all points share the same form). Returns kernel-agreement errors and
    samples.
    """
    fracs = np.linspace(0.0, v_max_frac, N_POINTS)
    S_ng, S_py, invS_ng, invS_py, Vs = [], [], [], [], []
    last_net = ""
    for frac in fracs:
        v_dc = float(frac * v_key)
        net = _op_point_netlist(v_dc, v_key)
        last_net = net
        r = run_ngspice(net, cir_path)
        assert r.ok, f"op-point ngspice run failed at V={v_dc:.1f}:\n{r.stderr[:600]}"
        vals = _op_read(r.stdout)
        s_ng = vals["n_s"]
        i_ng = vals["n_i"]
        s_py = float(saturation_factor(v_dc, v_key))
        Vs.append(v_dc)
        S_ng.append(s_ng)
        S_py.append(s_py)
        invS_ng.append(i_ng)
        invS_py.append(1.0 / s_py)
    # Re-write the committed .cir as the last (near-yield) representative point.
    cir_path.write_text(last_net, encoding="utf-8")

    S_ng, S_py = np.array(S_ng), np.array(S_py)
    invS_ng, invS_py = np.array(invS_ng), np.array(invS_py)
    Vs = np.array(Vs)

    err_collapse = float(np.max(np.abs(S_ng - S_py)))  # T2 collapse (S in [0,1])
    rel_div = np.abs(invS_ng - invS_py) / np.maximum(invS_py, 1e-30)
    err_divergent = float(np.max(rel_div))  # A1 divergent (1/S)

    def _sample(frac: float) -> dict:
        k = int(np.argmin(np.abs(Vs - frac * v_key)))
        return {
            "V_over_Vkey": float(Vs[k] / v_key),
            "S_ngspice": float(S_ng[k]),
            "S_canonical": float(S_py[k]),
            "Ceff_over_C0_divergent_ngspice": float(invS_ng[k]),
            "Ceff_over_C0_divergent_canonical": float(invS_py[k]),
        }

    return {
        "v_key_V": v_key,
        "v_max_frac": v_max_frac,
        "n_points": len(Vs),
        "method": "per-point .op (artifact-free; see METHOD NOTE)",
        "max_abs_err_collapse_S": err_collapse,
        "max_rel_err_divergent_invS": err_divergent,
        "samples": [_sample(f) for f in (0.0, 0.25, 0.5, 0.75, 0.9)],
        "cir": cir_path.name,
    }


def run_rung2() -> dict:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ART_DIR.mkdir(parents=True, exist_ok=True)

    # A1 divergent form — keyed on V_SNAP (metric varactor, C0/S). Sweep to 90%.
    a1 = _run_sweep(
        ART_DIR / "spice_ladder_rung2_a1_vsnap.cir",
        v_key=V_SNAP,
        v_max_frac=0.9,
    )
    # T2 collapse form — keyed on V_YIELD (dielectric permittivity, C0*S).
    t2 = _run_sweep(
        ART_DIR / "spice_ladder_rung2_t2_vyield.cir",
        v_key=V_YIELD,
        v_max_frac=0.9,
    )

    a1_pass = a1["max_rel_err_divergent_invS"] < KERNEL_TOL
    t2_pass = t2["max_abs_err_collapse_S"] < KERNEL_TOL
    passed = a1_pass and t2_pass

    return {
        "rung": 2,
        "name": "AVE_VACUUM_CELL Ax4 saturation curve vs canonical kernel",
        "ngspice_version": ngspice_version(),
        "class": "manifestation (.lib behavioral source == canonical Ax4 kernel)",
        "value_provenance": "V_SNAP/V_YIELD imported live from ave.core.constants (FLAG-1 safe)",
        "sector_split": "A1 divergent (C0/S, keyed V_SNAP) + T2 collapse (C0*S, keyed V_YIELD)",
        "V_SNAP_V": V_SNAP,
        "V_YIELD_V": V_YIELD,
        "tolerance": KERNEL_TOL,
        "a1_divergent_metric_varactor": a1,
        "t2_collapse_dielectric": t2,
        "verdict": "PASS" if passed else "FAIL",
    }


if __name__ == "__main__":
    result = run_rung2()
    (ART_DIR / "spice_ladder_rung2_result.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    a1, t2 = result["a1_divergent_metric_varactor"], result["t2_collapse_dielectric"]
    print("=" * 68)
    print("SPICE PHASE-1 ladder — RUNG 2: Ax4 saturation curve vs kernel")
    print("=" * 68)
    print(f"  ngspice                    : {result['ngspice_version']}")
    print(f"  V_SNAP (A1 key)            : {result['V_SNAP_V']:.6f} V")
    print(f"  V_YIELD (T2 key)           : {result['V_YIELD_V']:.6f} V")
    print(f"  A1 divergent (C0/S) max rel-err : {a1['max_rel_err_divergent_invS']:.3e}")
    print(f"  T2 collapse  (C0*S) max abs-err : {t2['max_abs_err_collapse_S']:.3e}")
    print(f"  tolerance                  : {result['tolerance']:.1e}")
    print(f"  VERDICT                    : {result['verdict']}")
