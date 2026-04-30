"""
Phase 1.5 — J^P Pattern Check for Baryon Ladder Matches.

Per auditor 2026-04-30 Flag 2: mass-only matching is vulnerable to coincidence;
J^P (spin-parity) pre-registration validation against PDG strengthens substantively.

Per [Vol 2 Ch 2:232](manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex):
    "Higher (2,q) torus knots carry more topological winding, corresponding to
     higher intrinsic spin — precisely the states the ladder selects."

The corpus has QUALITATIVE prediction (higher c → higher J) but no explicit
formula in code. This script:

1. Documents the J^P of each matched PDG state
2. Tests empirical-fit pattern J = (c-4)/2 for odd c
3. Reports match rate for J vs parity vs combined J^P
4. Issues forward predictions for c=21,23,25

Honest scope per A43 v30+v31: J = (c-4)/2 is **post-hoc empirical fit** to the
match data, NOT a pre-registered corpus-derived formula. Strengthens mass-only
claims to mass+J-pattern but doesn't promote to "corpus-derived prediction"
without algebraic-topology derivation work (estimated 1-2 days separately).
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import BARYON_LADDER, M_E, C_0, e_charge

_KG_TO_MEV: float = C_0**2 / (e_charge * 1e6)


# Matched PDG states with verified J^P from PDG 2024
# [c, predicted_mass_MeV, pdg_name, pdg_mass, pdg_jp, pdg_status]
MATCHES = [
    (5,  938.254, "proton",   938.272, "1/2+",  "****"),
    (7,  1261.0,  "Δ(1232)",  1232,    "3/2+",  "****"),
    (9,  1582.2,  "Δ(1620)",  1620,    "1/2-",  "****"),   # corpus identification
    (11, 1894.9,  "Δ(1950)",  1950,    "7/2+",  "****"),
    (13, 2194.6,  "N(2250)",  2250,    "9/2-",  "****"),   # per BARYON_LADDER docstring
    (15, 2478.0,  "Δ(2420)",  2420,    "11/2+", "****"),
    (17, 2741.8,  "Δ(2750)",  2750,    "13/2-", "**"),
    (19, 2983.1,  "Δ(2950)",  2950,    "15/2+", "**"),
]

# Forward predictions (c=21,23,25)
FORWARD = [
    (21, 3199.1),
    (23, 3387.0),
    (25, 3544.1),
]


def predicted_j_from_pattern(c: int) -> tuple[int, int]:
    """Empirical fit pattern J = (c-4)/2 for odd c.
    Returns (numerator, denominator) of J as fraction.
    e.g., c=5 → (1, 2) meaning J=1/2."""
    return (c - 4, 2)


def parse_pdg_jp(jp_str: str) -> tuple[tuple[int, int], str]:
    """Parse "1/2+" → ((1,2), "+") or "11/2-" → ((11,2), "-")."""
    parity = jp_str[-1]
    j_str = jp_str[:-1]
    num, den = j_str.split("/")
    return ((int(num), int(den)), parity)


def main():
    print("=" * 80, flush=True)
    print("  J^P Pattern Check for Baryon Ladder Matches")
    print("  Auditor 2026-04-30 Flag 2: mass-only → mass+J^P validation")
    print("=" * 80, flush=True)

    print(f"\n  Corpus pattern (Vol 2 Ch 2:232): higher c → higher J (qualitative)")
    print(f"  Empirical fit pattern (this script, post-hoc): J = (c-4)/2")
    print()

    print(f"  {'c':>3} {'predicted (MeV)':>16} {'PDG state':>12} {'PDG J^P':>10} "
          f"{'fit J':>8} {'J match':>10} {'parity match (vs +)':>22}")

    j_match_count = 0
    parity_match_count_pos = 0
    full_jp_match_count = 0
    total = len(MATCHES)

    detailed = []
    for c, pred_mass, name, pdg_mass, pdg_jp, status in MATCHES:
        pred_j_num, pred_j_den = predicted_j_from_pattern(c)
        (obs_j_num, obs_j_den), obs_parity = parse_pdg_jp(pdg_jp)

        j_match = (pred_j_num == obs_j_num and pred_j_den == obs_j_den)
        # The corpus pattern doesn't predict parity explicitly; tracking + as default
        parity_match = (obs_parity == "+")
        full_match = j_match and parity_match

        if j_match:
            j_match_count += 1
        if parity_match:
            parity_match_count_pos += 1
        if full_match:
            full_jp_match_count += 1

        fit_j_str = f"{pred_j_num}/{pred_j_den}"
        j_status = "✓" if j_match else "✗"
        p_status = "✓" if parity_match else "✗"

        print(f"  {c:>3} {pred_mass:>16.1f} {name:>12} {pdg_jp:>10} "
              f"{fit_j_str:>8} {j_status:>10} {p_status:>22}")

        detailed.append({
            "c": c,
            "predicted_mass_mev": pred_mass,
            "pdg_state": name,
            "pdg_mass_mev": pdg_mass,
            "pdg_jp": pdg_jp,
            "pdg_status": status,
            "fit_j": f"{pred_j_num}/{pred_j_den}",
            "j_match": bool(j_match),
            "parity_observed": obs_parity,
            "parity_assumed_positive_match": bool(parity_match),
            "full_jp_match": bool(full_match),
        })

    print(f"\n  J pattern match rate: {j_match_count}/{total} = {j_match_count/total*100:.1f}%")
    print(f"  Parity-positive match rate: {parity_match_count_pos}/{total} = "
          f"{parity_match_count_pos/total*100:.1f}%")
    print(f"  Full J^P (J + positive parity) match: {full_jp_match_count}/{total} = "
          f"{full_jp_match_count/total*100:.1f}%")

    # Forward predictions
    print(f"\n  FORWARD PREDICTIONS (c=21, 23, 25 — falsifiable):")
    print(f"  {'c':>3} {'predicted (MeV)':>16} {'predicted J':>12} "
          f"{'predicted parity':>20} {'falsifiable test':>40}")
    forward_predictions = []
    for c, pred_mass in FORWARD:
        fit_num, fit_den = predicted_j_from_pattern(c)
        # Parity prediction: pattern alternates somewhat; default to + per the
        # observed positive-parity dominance in established matches
        pred_parity = "+"
        falsifiable = (
            f"if exists at {pred_mass:.0f} MeV with J={fit_num}/{fit_den}{pred_parity}"
        )
        print(f"  {c:>3} {pred_mass:>16.1f} {fit_num}/{fit_den:>12} "
              f"{pred_parity:>20} {falsifiable:>40}")
        forward_predictions.append({
            "c": c, "predicted_mass_mev": pred_mass,
            "predicted_j_numerator": fit_num,
            "predicted_j_denominator": fit_den,
            "predicted_parity_assumed": pred_parity,
            "falsifiable_signature": falsifiable,
        })

    # Verdict
    print(f"\n  VERDICT")
    print(f"=" * 80)
    if j_match_count >= 6:
        print(f"  J pattern (J = (c-4)/2) holds for {j_match_count}/{total} states.")
        print(f"  This SUBSTANTIALLY STRENGTHENS mass-only matching.")
    else:
        print(f"  J pattern holds for only {j_match_count}/{total} states; weak.")

    print(f"\n  HONEST SCOPE (per A43 v30+v31):")
    print(f"  - J = (c-4)/2 is post-hoc empirical fit, NOT pre-registered corpus formula")
    print(f"  - Manuscript has QUALITATIVE 'higher c → higher J' (Vol 2 Ch 2:232)")
    print(f"  - Algebraic-topology J-from-torus-knot derivation NOT in code (~1-2 day work)")
    print(f"  - Parity not predicted by current pattern; observed mostly + with c=9,13,17 as -")
    print(f"  - Forward predictions c=21,23,25 are FALSIFIABLE pre-registrations")

    out = {
        "test": "J^P pattern check on baryon ladder matches",
        "corpus_anchor": "Vol 2 Ch 2:232 (qualitative higher c → higher J)",
        "empirical_fit_pattern": "J = (c-4)/2 for odd c (post-hoc fit)",
        "matched_states": detailed,
        "forward_predictions": forward_predictions,
        "j_match_rate": f"{j_match_count}/{total}",
        "parity_positive_match_rate": f"{parity_match_count_pos}/{total}",
        "full_jp_match_rate": f"{full_jp_match_count}/{total}",
        "honest_scope": [
            "J = (c-4)/2 is post-hoc empirical fit, NOT pre-registered",
            "Algebraic-topology J-from-torus-knot derivation NOT in code",
            "Parity not predicted; observed mostly + with c=9,13,17 as -",
            "Forward predictions c=21,23,25 are falsifiable",
        ],
    }
    out_path = Path(__file__).parent / "baryon_jp_pattern_check_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
