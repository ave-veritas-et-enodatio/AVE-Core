#!/usr/bin/env python3
"""Gating number check for the A_g derivation lane (R46 derive-first).

Re-verifies every verdict-bearing numeral of the lane against the driver JSON
with independent arithmetic (math module — the second engine). Supports
--mutation-receipt: perturbs a loaded value in memory and MUST detect it,
proving the checker is live. Auto-discovered by the make-verify umbrella.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
JSON = os.path.join(HERE, "ag_derivation_lane_results.json")

MUTATE = "--mutation-receipt" in sys.argv


def fail(msg):
    print(f"AG-DERIVATION NUMBER CHECK: FAIL — {msg}")
    sys.exit(1)


def main():
    with open(JSON) as f:
        r = json.load(f)

    if MUTATE:
        # deliberately corrupt the verdict-bearing chain coefficient; MUST be caught
        r["C3"]["f_chain_SI_float"] = 7.0

    checks = []
    c1, c2, c3 = r["C1"], r["C2"], r["C3"]
    K = r["constants"]

    # The two READINGS differ by 4π (preserved arithmetic); under the CANON-DECLARED
    # convention (gordon-optical-metric.md:25, clm-rd9cjm — Tier-2 repair) f = 7
    # exactly and the consumers AGREE.
    checks.append(("f_chain(plain-density reading) == 7/(4*pi)",
                   abs(c3["f_chain_SI_float"] - 7.0 / (4.0 * math.pi)) < 1e-12
                   and c3["f_chain_SI_exact"] == "7/(4*pi)"))
    checks.append(("readings ratio == 4*pi",
                   abs(c3["profile_over_chain_ratio_float"] - 4.0 * math.pi) < 1e-12
                   and c3["profile_over_chain_ratio_exact"] == "4*pi"))
    checks.append(("f_profile == 7", c3["f_profile_exact"] == "7"))
    checks.append(("f_chain under CANON convention == 7 exactly",
                   c3["f_chain_CANON_convention_exact"] == "7"
                   and abs(c3["f_chain_CANON_convention_float"] - 7.0) < 1e-12))
    checks.append(("consumers AGREE under canon convention",
                   c3["consumers_agree_under_canon_convention"] is True))

    # C3 receipts: discrete Gauss flux identity (point exact; blob to outer-loop tol)
    for k, v in c3["native_flux_receipt_exact"].items():
        checks.append((f"point flux identity {k}", abs(v["ratio"] - 1.0) < 1e-12))
    for k, v in c3["two_way_blob"]["flux_receipt"].items():
        checks.append((f"blob flux identity {k}", abs(v["ratio"] - 1.0) < 1e-4))

    # negative control: 7-pt Laplacian sees the bare GF (1/(4πr)) where it provably exists
    checks.append(("7pt control near b/exp ≈ 1",
                   abs(c3["control_7pt"]["b_over_expected_near"] - 1.0) < 0.01))
    checks.append(("7pt control far b/exp ≈ 1",
                   abs(c3["control_7pt"]["b_over_expected_far"] - 1.0) < 0.01))

    # sublattice diagnosis: interior zero fraction exactly 15/16; blob fit ≈ 1
    checks.append(("interior zero fraction ≈ 15/16 (site-count granularity)",
                   abs(c3["native_sublattice_zero_fraction_interior"] - 15.0 / 16.0) < 1e-3))
    checks.append(("point-source class fit ≈ 16x (sublattice diagnostic)",
                   14.0 < c3["native_relax"]["b_over_expected_near"] < 17.0))
    checks.append(("blob site-averaged fit ≈ 1 (all classes fed)",
                   abs(c3["two_way_blob"]["b_over_expected_DIAGNOSTIC"] - 1.0) < 0.10))

    # C2: exact coefficient + numeric cross-check + independent A_g recomputation
    checks.append(("m_add coeff == 8*pi/(3*r_c**3)",
                   c2["m_add_coeff_over_rhoB2"].replace(" ", "") == "8*pi/(3*r_c**3)"))
    checks.append(("C2 numeric cross-check <= 1e-8",
                   c2["numeric_cross_check_rel_err"] <= 1e-8))
    p = c2["params_ENG_CHOICE"]
    for chi in (1, 10):
        ag_indep = math.sqrt(
            3.0 * chi * p["M_b_kg"] * p["r_c_m"] ** 3 * K["C_0"] ** 4
            / (8.0 * math.pi * c2["rho_bulk_SI"] * 49.0 * K["G"] ** 2 * p["M_b_kg"] ** 2)
        )
        checks.append((f"A_g(chi={chi}) independent recompute",
                       abs(ag_indep - c2[f"A_g_required_chi_{chi}"]) / ag_indep < 1e-12))
        checks.append((f"c_pure(chi={chi}) = A_g/l_node²",
                       abs(c2[f"A_g_required_chi_{chi}"] / K["L_NODE"] ** 2
                           - c2[f"c_pure_chi_{chi}"]) / c2[f"c_pure_chi_{chi}"] < 1e-12))
    checks.append(("c_pure(chi=1) is ~57 OOM off pure-number scale",
                   1e56 < c2["c_pure_chi_1"] < 1e59))
    checks.append(("solar-surface dress strain >> yield under C2 A_g",
                   c2["exhibit_dress_strain_at_solar_surface"] > 1e9))

    # C1: bridge reproduces the internal relation; no absolute anchor found.
    # ⚑ Tier-2 (receipts lens): the ABSENCE itself must be asserted — engine
    # agreement alone would pass even if both engines found 50 hits.
    checks.append(("C1 bridge == internal relation", c1["bridge_matches_internal_relation"] is True))
    checks.append(("C1 engines agree on every pattern",
                   all(c1["sweep_engines_agree_on_presence"].values())))
    checks.append(("C1 absence asserted: zero 'B(M) =' sites",
                   c1["sweep_grep_hit_counts"][r"B\(M\)\s*="] == 0
                   and c1["sweep_py_hit_counts"][r"B\(M\)\s*="] == 0))
    checks.append(("C1 absence asserted: zero 'u0 = B' sites",
                   c1["sweep_grep_hit_counts"][r"u.?0\s*=\s*B"] == 0
                   and c1["sweep_py_hit_counts"][r"u.?0\s*=\s*B"] == 0))
    checks.append(("C1 absence asserted: zero 'dress amplitude' sites (lane-excluded)",
                   c1["sweep_grep_hit_counts"]["dress amplitude"] == 0))
    # blob fit: the ONLY native GF-amplitude measurement (Tier-2 3′) — bank its
    # honest quality; it separates 1x from 16x, no tighter claim.
    checks.append(("blob fit R² banked honestly (≈0.88 class, not ≥0.99)",
                   0.80 < c3["two_way_blob"]["fit_diagnostic"]["R2"] < 0.95))
    checks.append(("point leg converged flag is False (structural: no shell can "
                   "form at max_A ~ 1e-3; criterion is shell-radius stationarity)",
                   c3["native_relax"]["converged"] is False))
    sw = r["C3_convention_sweep"]
    checks.append(("C3c REPAIRED: liveness control matched by the 4πMc pattern",
                   sw["liveness_known_positive_matched"][
                       r"4\s*(\\,)?\s*(\\pi|π)\s*(\\,)?\s*M\s*c"] is True))
    checks.append(("C3c REPAIRED: BOTH canonical declaration sites found",
                   any("gordon-optical-metric.md:25" in h for h in sw["declaration_found"])
                   and any("03_macroscopic_relativity.tex:38" in h for h in sw["declaration_found"])))
    checks.append(("C3c REPAIRED: two engines agree on every pattern",
                   all(sw["engines_agree_on_presence"].values())))
    checks.append(("C3c REPAIRED: clm-rd9cjm trail non-empty (claim-id walk ran)",
                   len(sw["clm_rd9cjm_trail"]) > 0))

    # constants sanity (canonical import path, not hard-coded)
    checks.append(("L_NODE == hbar/(m_e c)",
                   abs(K["L_NODE"] - K["L_NODE_check_hbar_mec"]) / K["L_NODE"] < 1e-15))

    bad = [name for name, ok in checks if not ok]
    if MUTATE:
        if bad:
            print(f"AG-DERIVATION NUMBER CHECK: mutation receipt FIRES ({len(bad)} detector(s): {bad[:2]}) — checker is live")
            sys.exit(0)
        fail("mutation receipt did NOT fire — checker is dead")
    if bad:
        fail(f"{len(bad)} check(s) failed: {bad}")
    print(f"AG-DERIVATION NUMBER CHECK: PASS ({len(checks)} checks green)")


if __name__ == "__main__":
    main()
