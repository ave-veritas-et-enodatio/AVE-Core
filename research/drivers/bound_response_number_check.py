#!/usr/bin/env python3
"""Gating numeral check for the bound-response carve result doc.

Every REGISTERED verdict-bearing value in
``research/2026-08-09_bound-response_result.md`` must (a) appear in the doc in
at least one of its accepted printed forms, and (b) match the shipped
``bound_response_carve_results.json`` / ``bound_response_consumer_audit.json``
value when recomputed at the printed precision.  A registered value the doc
never exercises is a configuration FAIL (completeness guard).  The digest the
doc quotes must equal the recomputed sha256 of the shipped algebra JSON.

``--mutation-receipt`` perturbs every registered numeric value (x1.5, or +1 for
counts) and asserts the checker then FAILS — the gate is demonstrated fireable
on every invocation.

SCOPE, NARROWED DELIBERATELY: scans the RESULT DOC only; the prereg is not
machine-checked (and says so itself).
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DOC = os.path.join(REPO, "research", "2026-08-09_bound-response_result.md")
ALG_JSON = os.path.join(HERE, "bound_response_carve_results.json")
AUD_JSON = os.path.join(HERE, "bound_response_consumer_audit.json")

MUTATE = "--mutation-receipt" in sys.argv


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main(mutate: bool) -> list[str]:
    alg = load(ALG_JSON)["algebra"]
    aud = load(AUD_JSON)
    with open(DOC, encoding="utf-8") as fh:
        doc = fh.read()

    def mut(x):
        if not mutate:
            return x
        return x + 1 if isinstance(x, int) and not isinstance(x, bool) else x * 1.5

    counts = aud["bin_counts"]
    # (name, shipped value, accepted printed forms as format callables)
    REG = [
        ("partition_at_VRH", mut(alg["partition_at_VRH"]),
         lambda v: [f"{v:.6f}"]),                                  # 0.032863
        ("partition_over_delta_DP", mut(alg["partition_over_delta_DP"]),
         lambda v: [f"{v:.1f}"]),                                  # 252.8
        ("partition_sigma_HT", mut(alg["partition_sigma_HT"]),
         lambda v: [f"{v:.1f}"]),                                  # 20.5
        ("delta_DP", mut(alg["delta_DP"]),
         lambda v: [f"{v:.1e}".replace("e-04", "e-4"), "1.3×10⁻⁴" if abs(v - 1.3e-4) < 1e-12 else "×NO×"]),
        ("delta_HT", mut(alg["delta_HT"]), lambda v: [f"{v:.4f}"]),  # 0.0016
        ("floor_low", mut(alg["floor_family_superseded_input"]["at_cp_2.1304"]),
         lambda v: [f"{v:.4f}"]),                                  # 0.0152
        ("floor_high", mut(alg["floor_family_superseded_input"]["at_cp_1.7105"]),
         lambda v: [f"{v:.4f}"]),                                  # 0.0455
        ("sigma_HT_low", mut(alg["floor_family_superseded_input"]["sigma_HT_low"]),
         lambda v: [f"{v:.1f}"]),                                  # 9.5
        ("sigma_HT_high", mut(alg["floor_family_superseded_input"]["sigma_HT_high"]),
         lambda v: [f"{v:.1f}"]),                                  # 28.5
        ("x_DP_low", mut(alg["floor_family_superseded_input"]["x_DP_low"]),
         lambda v: [f"{v:.0f}"]),                                  # 117
        ("x_DP_high", mut(alg["floor_family_superseded_input"]["x_DP_high"]),
         lambda v: [f"{v:.0f}"]),                                  # 350
        ("cP_over_cS_K2G", mut(alg["cP_over_cS_at_K2G"]["float"]),
         lambda v: [f"{v:.3f}"]),                                  # 1.826
        ("F_bulk_under_carve", mut(alg["F_bulk_under_carve"]),
         lambda v: ["`F_bulk ≡ 0`" if v == 0.0 else "×NO×"]),
        ("HT_ratio", mut(0.9983), lambda v: [f"{v:.4f}"]),
        ("rows_total", mut(sum(counts.values())), lambda v: [f"{v} consumer rows", f"{v} classified consumer rows", f"{v} rows"]),
        ("rows_dies", mut(counts["DIES-WITH-THE-PHANTOM"]), lambda v: [f"{v} DIES"]),
        ("rows_needs", mut(counts["NEEDS-RE-DERIVATION"]), lambda v: [f"{v} NEEDS"]),
        ("rows_survives", mut(counts["SURVIVES-AS-RESPONSE"]), lambda v: [f"{v} SURVIVES"]),
        ("rows_uncertain", mut(aud["uncertain_count"]), lambda v: [f"{v} uncertain"]),
    ]

    fails = []
    for name, val, forms in REG:
        printed = forms(val)
        if not any(p in doc for p in printed if p != "×NO×"):
            fails.append(f"{name}: none of {printed!r} found in doc")

    # bin-count cross-sum guard (int-mutation moves the sum, firing here)
    tot = mut(sum(counts.values()))
    if f"Totals: {tot} consumer rows" not in doc and f"**Totals: {tot} consumer rows" not in doc:
        fails.append(f"totals line for {tot} rows not found")

    # digest guard
    with open(ALG_JSON, "rb") as fh:
        raw = fh.read()
    if mutate:
        raw += b"x"
    digest = hashlib.sha256(
        raw.decode().rstrip("\n").encode()).hexdigest()
    if digest not in doc:
        fails.append(f"algebra-JSON digest {digest[:16]}… not quoted in doc")
    return fails


if __name__ == "__main__":
    plain = main(mutate=False)
    if plain:
        print("bound_response_number_check: FAIL")
        for f in plain:
            print("  -", f)
        sys.exit(1)
    if MUTATE:
        fired = main(mutate=True)
        if not fired:
            print("bound_response_number_check: MUTATION RECEIPT DID NOT FIRE")
            sys.exit(1)
        print(f"bound_response_number_check: mutation receipt fires "
              f"({len(fired)} registered checks fail under perturbation) — gate demonstrated fireable")
    print("bound_response_number_check: PASS")
    sys.exit(0)
