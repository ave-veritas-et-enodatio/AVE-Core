#!/usr/bin/env python3
"""Smoke-fire ave.core.categorization guards (no heavy solves).

Usage:
  PYTHONPATH=src ./.venv/bin/python src/scripts/verify/categorization_smoke.py
"""

from __future__ import annotations

from ave.core.categorization import (
    CategorizationError,
    LedgerKind,
    LoadClass,
    PairingKind,
    WaveSpeedSlot,
    bare_junction_gamma,
    classify_ledger_pairing,
    difference_tone_allowed_subyield,
    effective_speeds,
    reciprocal_3port_s11_floor,
    require_load_class_for_alpha_invariance,
    require_wave_speed_slot,
)


def main() -> int:
    checks = []

    p = classify_ledger_pairing(LedgerKind.FAR_FIELD_FLUX, LedgerKind.TOTAL_ENERGY_ADD)
    checks.append(("flux↔ADD entailed", p.kind is PairingKind.ENTAILED))
    p2 = classify_ledger_pairing(LedgerKind.FAR_FIELD_FLUX, LedgerKind.ADM_DEFICIT)
    checks.append(("flux↔ADM fireable", p2.kind is PairingKind.FIREABLE))

    try:
        classify_ledger_pairing(LedgerKind.TOTAL_ENERGY_ADD, LedgerKind.ADM_DEFICIT)
        checks.append(("ADD↔ADM forbidden", False))
    except CategorizationError:
        checks.append(("ADD↔ADM forbidden", True))

    try:
        require_wave_speed_slot("fine_structure_alpha", WaveSpeedSlot.C_SHEAR)
        checks.append(("α refuses c_shear", False))
    except CategorizationError:
        checks.append(("α refuses c_shear", True))

    require_wave_speed_slot("schwarzschild_redshift", WaveSpeedSlot.C_SHEAR)
    checks.append(("Schwarzschild accepts c_shear", True))

    sym = effective_speeds(0.81, load=LoadClass.SYM)
    checks.append(("SYM Z/Z0=1", abs(sym["Z_over_Z0"] - 1.0) < 1e-15))
    require_load_class_for_alpha_invariance(LoadClass.SYM)
    checks.append(("SYM α-invariance ok", True))

    try:
        require_load_class_for_alpha_invariance(LoadClass.ASYM_EPS)
        checks.append(("ASYM blocks α-invariance", False))
    except CategorizationError:
        checks.append(("ASYM blocks α-invariance", True))

    checks.append(("difference tone forbidden", difference_tone_allowed_subyield() is False))
    checks.append(("Γ(z=3)=−1/3", abs(bare_junction_gamma(3) + 1.0 / 3.0) < 1e-15))
    checks.append(("|S11| floor=1/3", abs(reciprocal_3port_s11_floor(3) - 1.0 / 3.0) < 1e-15))

    print("categorization_smoke:")
    failed = 0
    for name, ok in checks:
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] {name}")
        if not ok:
            failed += 1
    print(f"  {len(checks) - failed}/{len(checks)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
