"""
Phase 1 — Baryon Ladder Extension to c=5-25.

Per [doc 98 §3.1](research/L3_electron_soliton/98_framework_decision_ii_mass_spectrum_activation.md):
extends `BARYON_LADDER` from c=5,7,9,11,13 (current production) to c=5-25 (odd
crossing numbers) covering remaining PDG baryon resonances.

Uses existing `_compute_i_scalar_dynamic(crossing_number=c)` from
`src/ave/core/constants.py:580` + ladder formula:
  ratio = i_scalar / (1 - V_TOROIDAL_HALO · P_C) + 1
  mass = ratio · m_e

NO MODIFICATIONS to constants.py — runs the existing solver for new c values
and reports. If results validate against PDG, second-step is to extend the
TORUS_KNOT_CROSSING_NUMBERS list in constants.py.

Per the corpus mapping ([constants.py:644-650](../../src/ave/core/constants.py)):
  c=5  → Proton (938 MeV)
  c=7  → Δ(1232)
  c=9  → Δ(1620)
  c=11 → Δ(1950)
  c=13 → N(2250)

This extends to: c=15, 17, 19, 21, 23, 25 — predicting masses for matching
candidates among PDG-listed Δ + N* resonances above 2250 MeV.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import (
    M_E, C_0, e_charge,
    V_TOROIDAL_HALO, P_C,
    BARYON_LADDER,
    _compute_i_scalar_dynamic,
)


_KG_TO_MEV: float = C_0**2 / (e_charge * 1e6)


# PDG resonance candidates above the c=13 N(2250) state.
# Curated list of Δ and N* states (2250 MeV+) for c=15-25 mapping.
# Source: PDG Listing 2024, baryon section.
PDG_CANDIDATES_HIGH_MASS = [
    # (mass_mev, name, J^P, status)
    (2300, "N(2300)", "1/2+", "**"),
    (2420, "Δ(2420)", "11/2+", "****"),
    (2570, "N(2570)", "5/2-", "**"),
    (2600, "N(2600)", "11/2-", "***"),
    (2700, "N(2700)", "13/2+", "**"),
    (2750, "Δ(2750)", "13/2-", "**"),
    (2950, "Δ(2950)", "15/2+", "**"),
    (3000, "N(3000)", "?", "*"),     # speculative
]


def main():
    print("=" * 80, flush=True)
    print("  Phase 1 — Baryon Ladder Extension: c=5-25 (odd crossings)")
    print("  Per doc 98 §3.1 mass-spectrum activation")
    print("=" * 80, flush=True)

    # Verify current ladder still reproduces
    print("\n  Current production ladder (constants.py BARYON_LADDER):")
    print(f"  {'c':>3} {'i_scalar':>14} {'ratio':>14} {'mass (MeV)':>14}")
    for c, data in sorted(BARYON_LADDER.items(), key=lambda x: int(x[0])):
        print(f"  {c:>3} {data['i_scalar']:>14.4f} {data['ratio']:>14.4f} "
              f"{data['mass_mev']:>14.4f}")

    # Extend to c=15-25
    extended_c_values = [15, 17, 19, 21, 23, 25]
    extended_ladder = {}

    print(f"\n  Computing extension for c={extended_c_values}...")
    print(f"  {'c':>3} {'i_scalar':>14} {'ratio':>14} {'mass (MeV)':>14}")

    # Reproduce existing ladder values for cross-check
    for c in [5, 7, 9, 11, 13] + extended_c_values:
        if c == 5:
            from ave.core.constants import I_SCALAR_1D
            i_scalar = I_SCALAR_1D
        else:
            i_scalar = _compute_i_scalar_dynamic(crossing_number=c)
        x_core = i_scalar / (1.0 - V_TOROIDAL_HALO * P_C)
        ratio = x_core + 1.0
        mass_mev = ratio * M_E * _KG_TO_MEV
        extended_ladder[c] = {
            'i_scalar': float(i_scalar),
            'ratio': float(ratio),
            'mass_mev': float(mass_mev),
        }
        marker = " (extension)" if c in extended_c_values else ""
        print(f"  {c:>3} {i_scalar:>14.4f} {ratio:>14.4f} {mass_mev:>14.4f}{marker}")

    # Cross-check: existing ladder reproducible
    print("\n  Reproducibility check vs production BARYON_LADDER:")
    for c in [5, 7, 9, 11, 13]:
        existing_mass = BARYON_LADDER[c]['mass_mev']
        new_mass = extended_ladder[c]['mass_mev']
        diff = abs(new_mass - existing_mass)
        diff_pct = diff / existing_mass * 100
        status = "✓ MATCH" if diff_pct < 0.0001 else f"✗ DRIFT ({diff_pct:.4e}%)"
        print(f"    c={c}: production={existing_mass:.4f}, "
              f"new={new_mass:.4f} {status}")

    # Map predicted masses to PDG candidates
    print("\n  PDG candidate matching for extended c values:")
    print(f"  {'c':>3} {'predicted (MeV)':>16} {'closest PDG':>20} "
          f"{'PDG mass':>10} {'error %':>10} {'match status':>20}")

    matches = []
    for c in extended_c_values:
        pred_mass = extended_ladder[c]['mass_mev']

        # Find nearest PDG candidate
        closest = min(PDG_CANDIDATES_HIGH_MASS,
                       key=lambda r: abs(r[0] - pred_mass))
        pdg_mass, pdg_name, jp, stars = closest
        error_pct = (pred_mass - pdg_mass) / pdg_mass * 100

        if abs(error_pct) < 3.0:
            status = "STRONG"
        elif abs(error_pct) < 7.0:
            status = "MODERATE"
        else:
            status = "WEAK"

        matches.append({
            "c": c,
            "predicted_mass_mev": pred_mass,
            "closest_pdg_name": pdg_name,
            "closest_pdg_mass_mev": pdg_mass,
            "error_pct": error_pct,
            "match_status": status,
            "pdg_jp": jp,
            "pdg_stars": stars,
        })

        print(f"  {c:>3} {pred_mass:>16.2f} {pdg_name:>20} "
              f"{pdg_mass:>10} {error_pct:>+10.2f} {status:>20}")

    # Summary statistics
    print("\n  EXTENSION SUMMARY:")
    extension_errors = [m["error_pct"] for m in matches]
    print(f"    States added: {len(matches)}")
    print(f"    Max |error| %: {max(abs(e) for e in extension_errors):.2f}")
    print(f"    Mean |error| %: {np.mean([abs(e) for e in extension_errors]):.2f}")

    strong_count = sum(1 for m in matches if m["match_status"] == "STRONG")
    moderate_count = sum(1 for m in matches if m["match_status"] == "MODERATE")
    weak_count = sum(1 for m in matches if m["match_status"] == "WEAK")
    print(f"    STRONG matches (|err|<3%): {strong_count}/{len(matches)}")
    print(f"    MODERATE matches (3%<|err|<7%): {moderate_count}/{len(matches)}")
    print(f"    WEAK matches (|err|>7%): {weak_count}/{len(matches)}")

    # Verdict
    print(f"\n  PHASE 1 VERDICT:")
    if max(abs(e) for e in extension_errors) < 5.0 and weak_count == 0:
        print("    Extension PASSES at ±5% target — clean ladder out to c=25.")
        print("    Recommend: extend TORUS_KNOT_CROSSING_NUMBERS in constants.py.")
    elif strong_count + moderate_count >= len(matches) * 0.7:
        print("    Extension PARTIAL — most matches reasonable, some weak.")
        print("    Investigate weak matches before committing extension.")
    else:
        print("    Extension shows substantial drift at high-c.")
        print("    Constrain ladder to current c=5-13 unless drift mechanism understood.")

    # Output
    out = {
        "test": "Phase 1 baryon ladder extension c=5-25",
        "current_production_ladder": {str(c): BARYON_LADDER[c] for c in BARYON_LADDER},
        "extended_ladder": {str(c): extended_ladder[c] for c in extended_ladder},
        "extension_c_values": extended_c_values,
        "pdg_matches": matches,
        "summary": {
            "states_added": len(matches),
            "max_abs_error_pct": float(max(abs(e) for e in extension_errors)),
            "mean_abs_error_pct": float(np.mean([abs(e) for e in extension_errors])),
            "strong_matches": strong_count,
            "moderate_matches": moderate_count,
            "weak_matches": weak_count,
        },
    }
    out_path = Path(__file__).parent / "baryon_ladder_extension_c5_c25_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
