"""PILOT-FIELD CONTROLS — the five HALT-gated controls (a)-(e), each wired through the
#528 ReconcileGate with can-fire proven on real paths.

FROZEN prereg: research/2026-07-05_pilot-field-comoving-companion_prereg_FROZEN.md §CONTROLS.

Each control reconciles a DRIVER-measured quantity against an INDEPENDENT reference
(the imported #534 analytic free/ring readings, the symbolic prediction, or a
different code path), NOT the quantity's own defining identity (the #527 defect the
ReconcileGate module docstring warns against). The can-fire self-test proves the halt
plumbing is live before every enforcement.

  (a) FILLED-ring limit (envelope -> whole ring) recovers #534's ring COLD reading.
  (b) OPEN-FREE-chain envelope recovers the free SOFT reading (0.9926-class) LOCALLY.
  (c) LINEAR-axial control: the contraction is GEOMETRIC (kernel ~ nothing at O(y0^2)).
  (d) envelope/ring sweep with the local-reading convergence quantified.
  (e) ENERGY-MOMENTUM LEDGER closure (the crank check) — saturation-consistent functional.

alpha-CLEAN: no physical constant on this path.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "src"))

from pilot_field_wavetrain import (  # noqa: E402
    contraction_depth,
    ledger_closure,
    run_wavetrain,
)
from ring_bondframe_probe import (  # noqa: E402
    open_chain_cyclemean,
    three_host_table,
)

from ave.validation.reconcile_gate import ReconcileGate  # noqa: E402


# ── control (a): FILLED-ring limit recovers #534 ring COLD (ratio -> 1.000000) ──
def control_a_filled_ring(band: float = 3e-3):
    """The filled-ring cycle-mean bond-frame reading must recover #534's COLD 1.000000.
    Claimed = the #534 three-host `ring` reading; independent = an exact 1.0 (the cold
    theorem the homogeneous-<dy^2> limit forces). Reconciles the filled limit to cold."""
    claimed = float(three_host_table()["ring"])
    gate = ReconcileGate(label="control-a-filled-ring-cold", claimed=claimed,
                         independent=1.0, rtol=0.0, atol=band)
    res = gate.enforce(prove_first=True)
    return {"claimed_ring_ratio": claimed, "reconciled": res.passed,
            "can_fire_proven": res.can_fire_proven, "band": band}


# ── control (b): OPEN-FREE-chain envelope recovers the free SOFT reading LOCALLY ──
def control_b_free_local(band_rel: float = 0.10):
    """The free open-chain LOCAL bond-frame reading must be SOFT by <dy^2>/2 (0.9926-class).
    Claimed = the imported #534 free-host cycle-mean reading; independent = the analytic
    1 - <dy^2>/2 free-host prediction (a DIFFERENT code path: the `pred_soft_free` closed
    form vs the relaxed-config measurement). Reconciles the free host to the SOFT theorem."""
    free = open_chain_cyclemean(n_nodes=1024, host="free")
    claimed = float(free["cyclemean_bondframe_k_ratio"])
    independent = float(free["pred_soft_free"])   # 1 - <dy^2>/2 (closed form, different path)
    gate = ReconcileGate(label="control-b-free-local-soft", claimed=claimed,
                         independent=independent, rtol=band_rel, atol=0.0)
    res = gate.enforce(prove_first=True)
    return {"claimed_free_ratio": claimed, "pred_soft": independent,
            "reconciled": res.passed, "can_fire_proven": res.can_fire_proven}


# ── control (c): LINEAR-axial vs nonlinear-kernel contraction (kernel ~ nothing) ──
def control_c_linear_axial(rho_bond: float = 2.0, band_rel: float = 0.05, fast: bool = True):
    """The contraction is GEOMETRIC (du = sqrt(1-dy^2)-1), not from the concave kernel.
    Claimed = the nonlinear-kernel DC contraction depth; independent = the LINEAR-axial
    run's depth (kernel OFF — a different force law). They must reconcile to O(y0^2) since
    the kernel enters only at O(y0^4)~O(A^2). Reconciles nonlinear vs linear-axial."""
    n_periods = 12.0 if fast else 16.0
    n_nodes = 768 if fast else 1024
    rn = run_wavetrain(n_nodes=n_nodes, rho_bond=rho_bond, l_env=60.0,
                       n_periods=n_periods, dt=0.02, linear_axial=False)
    rl = run_wavetrain(n_nodes=n_nodes, rho_bond=rho_bond, l_env=60.0,
                       n_periods=n_periods, dt=0.02, linear_axial=True)
    dn = float(contraction_depth(rn)["du_dc_min_under"])
    dl = float(contraction_depth(rl)["du_dc_min_under"])
    gate = ReconcileGate(label="control-c-linear-axial-geometric", claimed=dn,
                         independent=dl, rtol=band_rel, atol=1e-6)
    res = gate.enforce(prove_first=True)
    return {"nonlinear_depth": dn, "linear_axial_depth": dl,
            "rel_diff": abs(dn - dl) / (abs(dn) + 1e-30),
            "reconciled": res.passed, "can_fire_proven": res.can_fire_proven}


# ── control (d): envelope/ring sweep, local-reading convergence quantified ──
def control_d_scale_sweep(rho_bond: float = 4.0, fast: bool = True):
    """The local contraction depth -> -<dy^2>/2 and the compensating stretch -> 0 as
    L_env/N -> 0. Quantify: report the DC depth and the far-field stretch across the
    (L_env, N) grid. NOT a single-gate reconcile — a REPORTED convergence table (the
    [PILOT-CONFIRMED] verdict requires both; this control supplies the numbers)."""
    # vary L_env/N so the dilution is a real convergence, not fixed-ratio N-scaling:
    grid = [(80, 512), (80, 1024)] if fast else [(80, 512), (80, 1024), (80, 2048)]
    n_periods = 12.0 if fast else 18.0
    rows = []
    for (le, n) in grid:
        run = run_wavetrain(n_nodes=n, rho_bond=rho_bond, l_env=float(le),
                            n_periods=n_periods, dt=0.02)
        c = contraction_depth(run)
        rows.append({"L_env": le, "N": n, "L_env_over_N": le / n,
                     "du_dc_min_under": c["du_dc_min_under"],
                     "du_dc_far_mean": c["du_dc_far_mean"]})
    return {"rows": rows,
            "far_dilutes": bool(abs(rows[-1]["du_dc_far_mean"]) <= abs(rows[0]["du_dc_far_mean"]) + 1e-6)}


# ── control (e): ENERGY-MOMENTUM LEDGER closure (the crank check) ──
def control_e_ledger(rho_bond: float = 2.0, energy_band: float = 1e-3,
                     momentum_band: float = 1e-10, fast: bool = True):
    """Total energy (saturation-consistent functional) conserved and total longitudinal
    momentum conserved (closed ring) over the recording window. Claimed = the measured
    energy drift / momentum max; independent = 0 (perfect conservation, the closed-ring
    theorem). Reconciles the ledger to closure — the #532 no-linear-proxy flag honored
    (the axial potential is the rho-scaled Phi(A), not a linear proxy)."""
    n_periods = 12.0 if fast else 18.0
    n_nodes = 768 if fast else 1024
    run = run_wavetrain(n_nodes=n_nodes, rho_bond=rho_bond, l_env=60.0,
                        n_periods=n_periods, dt=0.02)
    ld = ledger_closure(run)
    g_e = ReconcileGate(label="control-e-energy-closure", claimed=ld["energy_drift_rel"],
                        independent=0.0, rtol=0.0, atol=energy_band)
    g_p = ReconcileGate(label="control-e-momentum-closure", claimed=ld["momentum_max_abs"],
                        independent=0.0, rtol=0.0, atol=momentum_band)
    re = g_e.enforce(prove_first=True)
    rp = g_p.enforce(prove_first=True)
    return {"energy_drift_rel": ld["energy_drift_rel"], "momentum_max_abs": ld["momentum_max_abs"],
            "energy_reconciled": re.passed, "momentum_reconciled": rp.passed,
            "can_fire_proven": bool(re.can_fire_proven and rp.can_fire_proven)}


def run_all_controls(fast: bool = True) -> dict:
    """Run all five controls. `fast=True` uses smaller rings / fewer periods for the
    fast test core; `fast=False` is the full-fidelity path (the slow test / __main__)."""
    return {
        "control_a_filled_ring": control_a_filled_ring(),
        "control_b_free_local": control_b_free_local(),
        "control_c_linear_axial": control_c_linear_axial(fast=fast),
        "control_d_scale_sweep": control_d_scale_sweep(fast=fast),
        "control_e_ledger": control_e_ledger(fast=fast),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_all_controls(fast=False), indent=2, default=float))
