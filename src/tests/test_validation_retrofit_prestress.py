"""RETROFIT DEMO — the (f) reconcile-gate on the prestress driver's VS4 exact-collapse.

Demonstration consumer for `ave.validation.ReconcileGate` (the follow-on flagged in
the #527 fix round: three consecutive arcs — #521 dead-else, #526 unreachable halt,
#527 identity-recheck — shipped a loud halt that could not fire). The prestress
driver's VS4 gate is the cleanest real reconcile in the corpus:

  claimed     = the PRESTRESSED tensor (C11, C12, C44) from extract_prestress_Cij
                at (k_a, k_s, T);
  independent = the COLD tensor from extract_cubic_Cij at the SHIFTED spring
                k_s + T/l — a DIFFERENT assembler (the #527-fix reference pattern),
                NOT the defining identity;
  tolerance   = rtol 1e-9 (the VS4 exact-collapse criterion, unchanged).

THE ADOPTION (the copy-paste target, wired into the driver at run_positive_controls):
    gate = ReconcileGate(label=..., claimed=<prestressed C_ij>,
                         independent=<cold assembler at shifted spring>, rtol=1e-9)
    gate.prove_can_fire()      # liveness: synthetic discrepancy MUST fire the halt
    ok = gate.check().passed   # feeds the driver's existing HALT aggregation

Each test is one arm of the discipline: exact on truth / fires on a corrupted
remap / plumbing live-fire proven / driver records the gate provenance. The
#526-merged [MAP-DEFORMED] verdict flow is untouched (same criterion, same PASS
aggregation). α-CLEAN; CONSISTENCY class (instrument-hardening, not a physics claim).
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.validation import DiscrepantHalt, ReconcileGate
from scripts.vol_1_foundations.prestress_elastic_tensor import (
    extract_prestress_Cij,
    run_positive_controls,
)
from scripts.vol_1_foundations.srs_elastic_tensor import extract_cubic_Cij, srs_primitive

CIJ = ("C11", "C12", "C44")
KA, KS, T = 9.7734, 1.0, 0.3  # a VS4 probe point (mid-sweep, both terms live)


@pytest.fixture(scope="module")
def srs():
    return srs_primitive("right")


def _vs4_gate(srs, shift_scale=1.0):
    """The driver's VS4 reconcile, parameterized so a test can corrupt the remap."""
    pos, bonds, rho = srs
    ell = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds]))
    pre = extract_prestress_Cij(pos, bonds, k_axial=KA, k_shear=KS, T_per_bond=T, rho=rho)
    return ReconcileGate(
        label=f"VS4 retrofit demo (shift_scale={shift_scale})",
        claimed=np.array([pre[k] for k in CIJ]),
        independent=lambda: np.array(
            [extract_cubic_Cij(pos, bonds, k_axial=KA,
                               k_shear=KS + shift_scale * T / ell, rho=rho)[k] for k in CIJ]),
        rtol=1e-9,
    )


def test_vs4_gate_reconciles_on_truth(srs):
    """POSITIVE: the true remap (k_s -> k_s + T/l) reconciles the prestressed tensor
    against the independently-assembled cold tensor to the VS4 criterion, with the
    can-fire proof run first (enforce default)."""
    res = _vs4_gate(srs).enforce()
    assert res.passed and res.can_fire_proven
    assert res.max_rel_discrepancy < 1e-9  # the exact-collapse mechanism fact


def test_vs4_gate_halts_on_corrupted_remap(srs):
    """NEGATIVE (the gate CAN fire on a live track): a corrupted remap (wrong shift,
    k_s + 0.5*T/l) breaks the reconcile — the loud DISCREPANT-HALT must raise. This
    is the arm the #521/#526/#527 first drafts could not exercise."""
    with pytest.raises(DiscrepantHalt):
        _vs4_gate(srs, shift_scale=0.5).enforce(prove_first=False)


def test_vs4_gate_selftest_proves_can_fire(srs):
    """The liveness self-test on the REAL driver quantities: a synthetic discrepancy
    injected through the same comparator+halt path fires the halt."""
    proof = _vs4_gate(srs).prove_can_fire()
    assert proof.passed and proof.can_fire_proven


def test_driver_records_gate_provenance(srs):
    """CONSUMER-SIDE WIRING: the retrofitted driver runs the gate inside its own
    positive-control block, proves liveness once per run, records the provenance,
    and its PASS aggregation (and hence the merged verdict flow) is unchanged."""
    pos, bonds, rho = srs
    pc = run_positive_controls(pos, bonds, rho)
    vs4 = pc["VS4_exact_collapse_to_shifted_shear_spring"]
    assert vs4["PASS"] and pc["ALL_PASS"]
    gate_meta = vs4["reconcile_gate"]
    assert gate_meta["library"] == "ave.validation.ReconcileGate"
    assert gate_meta["selftest_can_fire_proven"] is True
    assert gate_meta["rtol"] == 1e-9
    # the per-case criterion is byte-compatible with the pre-retrofit VS4 record
    assert all(c["prestress_vs_cold_shifted_rel_err"] < 1e-9 for c in vs4["cases"])
