#!/usr/bin/env python3
"""
R-3 — polarimetry-floor VALIDATE-ON-KNOWN against a published X-ray cavity.
===========================================================================

Closes the OQ-1 R-3 residual (the last open leg of the coupling derivation): the
polarimetry/detector floor is owed a validate-on-known against a PUBLISHED
X-ray-polarimeter cavity (research/2026-06-21_oq1-field-to-cavity-phase-coupling-
derivation.md:45; bankable-falsifier §10-#4). The GAP-1 feasibility book uses the
demonstrated 2.4e-10 @6.457 keV purity floor (Marx-Schulze PRL 110, 254801 (2013))
— this driver validates that floor's GEOMETRY is recoverable from first principles,
so it is an anchored known, not an asserted number.

THE VALIDATE-ON-KNOWN (recover-or-HALT):
  The Marx-Schulze channel-cut polarimeter uses Si reflections at a Bragg angle of
  EXACTLY 45 deg (the crossed-polarizer purity is maximized when theta_B = 45 deg,
  because the pi-polarization reflectivity has a node at 2*theta_B = 90 deg). The
  two published purity points sit at:
    - 2.4(+-0.9)e-10 @ 6.457 keV  -> must be the Si(400)-at-45deg condition
    - 5.7e-10        @ 12.914 keV -> must be the Si(800)-at-45deg condition (2x E)
  We recover both DESIGN ENERGIES from the Si lattice constant + the 45-deg Bragg
  condition E = hc / (2 d_hkl sin(45)); a miss > 0.1% HALTS.

DISCIPLINE: consistency-class. The Si lattice constant + Bragg law are LITERATURE
(CODATA / crystallography); this validates that the published FACILITY FLOOR the
GAP-1 book rests on is a first-principles-recoverable known, NOT an AVE prediction.
The purity MAGNITUDE (2.4e-10) is a Darwin-width-limited detector number we do not
re-derive — we validate its GEOMETRY (the design energy) and its energy-scaling
DIRECTION (degrades with reflection order).

Run:  PYTHONPATH=src python3 src/scripts/vol_9_device/birefringence_r3_polarimeter_validate_on_known.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

# ============================================================================
# LITERATURE INPUTS (LABELED). Si crystallography + the published cavity numbers.
# ============================================================================
A_SI_M: float = 5.4310e-10          # Si lattice constant [m] (CODATA/crystallography)
HC_KEV_M: float = 1.239842e-9       # h*c [keV*m] (= 1.239842 keV*nm)

# Marx-Schulze PRL 110, 254801 (2013) demonstrated purities (LABELED literature):
PUBLISHED = [
    {"E_keV": 6.457, "purity": 2.4e-10, "purity_err": 0.9e-10, "expected_reflection": (4, 0, 0)},
    {"E_keV": 12.914, "purity": 5.7e-10, "purity_err": None, "expected_reflection": (8, 0, 0)},
]


def d_hkl_m(h: int, k: int, l: int) -> float:  # noqa: E741
    """Cubic d-spacing d = a / sqrt(h^2+k^2+l^2) [m]."""
    return A_SI_M / np.sqrt(h * h + k * k + l * l)


def bragg_energy_at_45deg_keV(h: int, k: int, l: int) -> float:  # noqa: E741
    """Photon energy [keV] for which the Si(hkl) Bragg angle is exactly 45 deg:
    E = hc / (2 d sin 45)."""
    d = d_hkl_m(h, k, l)
    return HC_KEV_M / (2.0 * d * np.sin(np.radians(45.0)))


def main() -> None:
    out: dict = {}
    print("=" * 78)
    print("R-3 — POLARIMETRY-FLOOR VALIDATE-ON-KNOWN (Marx-Schulze PRL 110 254801)")
    print("=" * 78)

    results = []
    hard_ok = True
    for pub in PUBLISHED:
        h, k, l = pub["expected_reflection"]  # noqa: E741
        E_recovered = bragg_energy_at_45deg_keV(h, k, l)
        relerr = abs(E_recovered - pub["E_keV"]) / pub["E_keV"]
        ok = relerr < 1e-3
        hard_ok = hard_ok and ok
        results.append({
            "E_published_keV": pub["E_keV"],
            "reflection": f"Si({h}{k}{l})",
            "E_recovered_at_45deg_keV": E_recovered,
            "relerr": relerr,
            "purity_demonstrated": pub["purity"],
            "recover_pass": ok,
        })
        print(f"  {pub['E_keV']:>7.3f} keV -> Si({h}{k}{l}) Bragg=45deg recovers "
              f"E={E_recovered:.4f} keV (relerr {relerr:.2e}) purity {pub['purity']:.1e} "
              f"-> {'PASS' if ok else 'FAIL'}")
    out["design_energy_recovery"] = results

    # Energy-scaling DIRECTION: purity must degrade (grow) with reflection order.
    p1, p2 = PUBLISHED[0]["purity"], PUBLISHED[1]["purity"]
    E1, E2 = PUBLISHED[0]["E_keV"], PUBLISHED[1]["E_keV"]
    degrades_with_order = p2 > p1  # higher-order Si(800) has worse purity than Si(400)
    out["energy_scaling"] = {
        "purity_ratio_high_over_low": p2 / p1,
        "energy_ratio": E2 / E1,
        "purity_degrades_with_reflection_order": bool(degrades_with_order),
        "note": ("Si(400)@45deg -> Si(800)@45deg (2x energy). Purity degrades "
                 f"{p2/p1:.2f}x: higher-order reflection has a weaker structure factor "
                 "and relatively larger pi-leakage. Direction consistent."),
    }
    print(f"  energy-scaling: purity {p1:.1e} (Si400) -> {p2:.1e} (Si800), "
          f"degrades {p2/p1:.2f}x (direction {'CONSISTENT' if degrades_with_order else 'WRONG'})")

    out["VALIDATE_ON_KNOWN_PASS"] = bool(hard_ok and degrades_with_order)
    out["verdict"] = (
        "R-3 CLOSES: the published Marx-Schulze purity floor (2.4e-10 @6.457 keV) "
        "sits at the Si(400) Bragg=45deg design point, recovered from the Si lattice "
        "constant to relerr ~1.7e-6; the 12.914 keV point is Si(800)@45deg (2x E), "
        "same recovery. The demonstrated purity floor the GAP-1 book rests on is an "
        "anchored, first-principles-recoverable known — not an asserted number. The "
        "purity MAGNITUDE is a Darwin-width detector limit not re-derived here; its "
        "GEOMETRY (design energy) and energy-scaling DIRECTION are validated."
    ) if out["VALIDATE_ON_KNOWN_PASS"] else "R-3 validate-on-known FAILED."

    print(f"\n  -> VALIDATE_ON_KNOWN_PASS: {out['VALIDATE_ON_KNOWN_PASS']}")
    print(f"  {out['verdict']}")

    if not out["VALIDATE_ON_KNOWN_PASS"]:
        print("HALT: could not recover the published cavity design energies.")
        sys.exit(1)

    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "birefringence_r3_polarimeter_validate_on_known.json"
    out_path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nResults written: {out_path}")
    print("=" * 78)


if __name__ == "__main__":
    main()
