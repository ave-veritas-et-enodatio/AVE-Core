"""ave.validation — the reusable verdict-hardening harness.

ENGINE-HARDENING ARC item 2 (`_orchestration/2026-07-04_engine-upgrade-program.md`
§2). Extracts the proven gate machinery — which had been re-implemented ad hoc in
one driver after another — into a single reusable library, so every future
null/disperse/does-not-exist verdict passes the SAME certified guards before it is
believed. Each utility carries its live-fire provenance in its module docstring.

The six guards, and the failure each retires:

  (a) planted_source       — positive-control runner: push a KNOWN-nonzero signal
                             through the SAME pipeline callable and assert the
                             instrument registers it. Retires the blind-null read
                             (a "zero" that the observable could never have shown
                             nonzero). Live-fire: the localization-readjudication
                             srs positive-control eigenmode.
  (b) structural_degeneracy — detect observables that are forced to a value by the
                             graph/symmetry regardless of physics: global-sum on a
                             closed graph (nullspace-annihilated), symmetry-forced
                             zeros. Retires the Stage-1 blind global-sum readout.
  (c) runtime_independence  — stub a dependency to return garbage; demand the
                             output is BIT-IDENTICAL. Proves no forbidden quantity
                             is routed into the result by construction, name-
                             independently. Live-fire: the em_readout RHS
                             Q_link-stub bit-identity check.
  (d) equation_audit        — live import-closure scan + anchored allowlists +
                             consumed-forbidden-constant guard. Retires the
                             smuggled-constant (α-into-the-RHS) failure. Lifted +
                             generalized from the #482-era em_readout driver.
  (e) spectral_liveness     — re-export of ave.solvers.spectral_liveness (already a
                             first-class module): the seed's nullspace-energy
                             fraction read BEFORE its persistence verdict.
  (f) reconcile_gate        — a claimed quantity vs an INDEPENDENT recomputation
                             (different code path, NOT the defining identity) at a
                             registered tolerance, with a can-fire self-test that
                             injects a synthetic discrepancy and asserts the
                             DISCREPANT-HALT triggers. Retires the checklist-
                             masquerading-as-a-gate failure caught by adversarial
                             review in THREE consecutive arcs (#521 dead-else,
                             #526 unreachable halt, #527 identity-recheck).
                             Live-fire: the #527 fix-round independent ν-reconcile.

α-CLEAN: this package imports NO physical constant on its own path. The
equation-audit guard NAMES forbidden constants (as strings to scan for) but never
imports their values.
"""

from __future__ import annotations

from ave.validation.equation_audit import (
    EquationAuditResult,
    audit_solve_path,
    import_closure_modules,
    scan_forbidden_constants,
)
from ave.validation.planted_source import (
    PlantedSourceResult,
    planted_source_control,
    project_out_nullspace,
)
from ave.validation.reconcile_gate import (
    DeadGateError,
    DiscrepantHalt,
    ReconcileGate,
    ReconcileGateResult,
    assert_reconciled,
    reconcile,
)
from ave.validation.runtime_independence import (
    RuntimeIndependenceResult,
    assert_runtime_independent,
    stub_and_compare,
)
from ave.validation.spectral_liveness import (
    SpectralLiveness,
    localized_eigenmode,
    spectral_liveness,
)
from ave.validation.structural_degeneracy import (
    StructuralDegeneracyResult,
    detect_global_sum_degeneracy,
    detect_symmetry_forced_zero,
)

__all__ = [
    # (a) planted-source positive control
    "planted_source_control",
    "PlantedSourceResult",
    "project_out_nullspace",
    # (b) structural-degeneracy checks
    "detect_global_sum_degeneracy",
    "detect_symmetry_forced_zero",
    "StructuralDegeneracyResult",
    # (c) runtime-independence
    "assert_runtime_independent",
    "stub_and_compare",
    "RuntimeIndependenceResult",
    # (d) equation-audit
    "audit_solve_path",
    "scan_forbidden_constants",
    "import_closure_modules",
    "EquationAuditResult",
    # (e) spectral-liveness (re-export)
    "spectral_liveness",
    "localized_eigenmode",
    "SpectralLiveness",
    # (f) reconcile-gate
    "ReconcileGate",
    "ReconcileGateResult",
    "DiscrepantHalt",
    "DeadGateError",
    "reconcile",
    "assert_reconciled",
]
