"""A3 universe-return gates (prereg FROZEN push-first — commit cfd2e690)."""

from __future__ import annotations

import sys
from pathlib import Path

from ave.core.categorization import ClaimClass

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts" / "vol_1_foundations"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from universe_return_a3 import (  # noqa: E402
    DELTA_E_ABS,
    OMEGA_RET,
    LeaveTakeReport,
    ReturnArmReport,
    SabotageReport,
    _shell_only_mask,
    adjudicate,
    run_interior_sabotage,
    run_leave_take,
    run_null_arm,
    run_shell_face_diag_arm,
    run_shell_return_arm,
    run_suite,
)


def test_leave_take_a1_green():
    _, leave = run_leave_take(N=12, n_clear=300)
    assert leave.passive
    assert leave.R_pass


def test_shell_return_received_frozen_shell_only():
    """R7: the ENFORCING arm is the FROZEN shell-ONLY drive (prereg 'applied on
    the shell only'). It still fires (ΔE_int ≫ floor) without driving inside the
    interior ΔE mask."""
    leave, shell = run_shell_return_arm(N=12, n_clear=300, n_ret=120)
    assert leave.R_pass
    assert shell.source_is_exterior
    assert shell.delta_E_int > DELTA_E_ABS


def test_shell_only_mask_excludes_interior_face():
    """R7: the frozen shell-only mask does NOT overlap the Rule-10 interior
    (unlike the shell+face diagnostic, which drives inside the ΔE mask)."""
    import numpy as np

    from universe_return_a3 import NativeCageIMEX, NativeCageIMEXConfig

    eng = NativeCageIMEX(NativeCageIMEXConfig(N=12, dx=0.5, pml_thickness=4, port_sigma=0.05))
    mask = _shell_only_mask(eng) > 0.5
    # shell-only support has zero overlap with the interior measurement region.
    assert not np.any(mask & eng.interior)


def test_null_differenced_is_enforcing_per_arm_reception_diagnostic():
    """R8: per-arm reception is diagnostic (the null's own `received` is unreliable
    slosh); the ENFORCING criterion is signal − null, which clears the floor."""
    _, shell = run_shell_return_arm(N=12, n_clear=300, n_ret=120)
    null = run_null_arm(N=12, n_clear=300, n_ret=120)
    # Enforcing discrimination is robustly positive and huge vs the floor.
    assert (shell.delta_E_int - null.delta_E_int) > DELTA_E_ABS
    assert (shell.delta_E_int - null.delta_E_int) > 100 * DELTA_E_ABS


def test_shell_face_diag_is_separate_leg():
    """R7 KEEP-BOTH: the shell+face diagnostic arm exists as a labeled separate
    leg and drives inside the interior mask (exterior-attributed but diagnostic)."""
    diag = run_shell_face_diag_arm(N=12, n_clear=300, n_ret=120)
    assert diag.source == "shell_face_diag"
    assert diag.source_is_exterior


def test_interior_sabotage_trips():
    sab = run_interior_sabotage(N=12, n_clear=300, n_ret=120)
    assert sab.trips_as_sabotage
    assert sab.source_is_exterior is False


def test_adjudicate_bins_frozen():
    leave = LeaveTakeReport(True, 1e-4, True, 1.0, 1e-4, 0.01, ClaimClass.CONSISTENCY.value)
    shell = ReturnArmReport(
        "shell", True, 0.1, 0.01, 0.11, 1e-4, 0.2, 2.0, True, ClaimClass.CONSISTENCY.value
    )
    null = ReturnArmReport(
        "null", False, 0.0, 0.01, 0.01, 1e-4, 1e-4, 1.0, False, ClaimClass.CONSISTENCY.value
    )
    sab = SabotageReport(True, False, 0.05, ClaimClass.CONSISTENCY.value)
    assert (
        adjudicate(leave=leave, shell=shell, null=null, sabotage=sab) == "i_RETURN_RECEIVED"
    )
    weak = SabotageReport(False, False, 0.0, ClaimClass.CONSISTENCY.value)
    assert (
        adjudicate(leave=leave, shell=shell, null=null, sabotage=weak) == "ii_RETURN_WEAK"
    )


def test_omega_ret_frozen_slow():
    assert abs(OMEGA_RET - 0.3) < 1e-12


def test_run_suite_fast_bin_i():
    out = run_suite(fast=True)
    assert out["bin"] == "i_RETURN_RECEIVED"
    assert out["refuse_claim_class"] == ClaimClass.EMERGENCE.value
    # R7: enforcing arm is the frozen shell-only drive; diagnostic leg present.
    assert "shell_face_diag_return" in out
    assert out["shell_return"]["delta_E_int"] > DELTA_E_ABS
    # R8: the enforcing criterion is signal − null (per-arm reception is diagnostic).
    assert out["delta_vs_null"] > DELTA_E_ABS
    assert "null_systematic_note" in out
    assert out["sabotage"]["trips_as_sabotage"]
