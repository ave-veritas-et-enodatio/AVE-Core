#!/usr/bin/env python3
"""iomega_law_number_check.py — standing verify gate for the I_omega(A)-law lane.

Checks, on every `make verify` (all gating; exit nonzero on any failure):
  1. NUMERALS   — the result doc's load-bearing numeric tokens reconcile against the two
                  shipped JSONs (hit counts, class totals, digests, p values, the FT-SCAN
                  sentinel cells, the two registry sizes).
  2. GATES      — RECONCILED, not consumed: every gate's DECLARED label is recomputed from
                  the JSON's own measured fields and a contradiction is a FAILURE
                  (gate-reconcile-not-declare; Tier-2 repair D1, 2026-08-06).
  3. LAW-RERUN  — iomega_law_check.py re-runs live and reproduces its shipped digest
                  (fast, pure-sympy; the scan driver is NOT re-run here — its G-DET
                  two-run receipt is banked in the result doc; its JSON is instead
                  integrity-checked by the numerals + gate-reconciliation + completeness
                  passes). The re-run also re-executes FT-A008/FT-PAIR, whose only shipped
                  field is `fires` — the live driver exits nonzero if either fails to fire,
                  which is the compensating control for those two (disclosed, not hidden).
  4. QUOTES     — the load-bearing cite registry below re-verifies at HEAD: each excerpt
                  occurs within +/-2 lines of its registered line (G-CITE) — plus
                  CITE-COMPLETE: every italic-quoted excerpt in the result-doc BODY must be
                  covered by a registry entry (so the registry size is the ONE measured
                  cite count, Tier-2 repair A1).
  5. MU-SITES   — the ~10 canon `mu_eff = mu_0 S` sites enumerated in the result doc's
                  section-1.1 name-scoping disclosure are verified at file:line
                  (Tier-2 repair A3).
  6. MUTATION   — every control declared in CONTROLS is exercised by at least one forced-false
                  receipt: the perturbed artifact is fed back through the SAME check code and
                  the named control must fire. A control that does not fire prints MISSED and
                  the run fails. No receipt is a tautology over an untouched artifact
                  (Tier-2 repair A11).
"""
from __future__ import annotations

import copy
import json
import re
import subprocess
import sys
from pathlib import Path

DRIVERS = Path(__file__).resolve().parent
REPO = DRIVERS.parents[1]
RESULT_DOC = REPO / "research/2026-08-06_iomega-law_result.md"
SCAN_JSON = DRIVERS / "iomega_law_scan_results.json"
CHECK_JSON = DRIVERS / "iomega_law_check_results.json"

FAIL: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        FAIL.append(msg)


# --- the load-bearing cite registry (G-CITE) -----------------------------------------
# (path, line, source_excerpt, body_form)
#   source_excerpt — verified verbatim at path:line (+/- WINDOW lines).
#   body_form      — how the result doc renders it, when the doc's rendering is NOT
#                    byte-identical to the source (de-bolded, de-wrapped, backticked, or
#                    quoted as a fragment). `None` = the doc renders it verbatim.
#                    Every divergence here is a disclosed re-rendering, not a drift.
QUOTE_REGISTRY = [
    ("manuscript/ave-kb/common/universal-saturation-kernel-catalog.md", 145,
     "All 26 catalog instances are SWING-typed.", None),
    ("manuscript/ave-kb/common/universal-saturation-kernel-catalog.md", 171, "pending A4", None),
    # A10 (Tier-2): the FLAG-IMAX-DISCREPANCY comparand.
    ("manuscript/ave-kb/common/universal-saturation-kernel-catalog.md", 171,
     "$I_{max}\\simeq116$ A", None),
    # FLAG-CEFF-CITE (Tier-2, surfaced not adjudicated): Op16's own verification claim.
    ("manuscript/ave-kb/common/operators.md", 56, "grep-verified explicit formula", None),
    # D3 (Tier-2): the frozen claim-to-check carried verbatim into the result doc.
    ("research/2026-08-06_iomega-law_prereg-FROZEN.md", 195,
     "invariant to any geometric density grading, so FLAG-PITCH cannot move the knife whichever way it",
     None),
    # A1 (Tier-2): the A-034 catalog's own "relativistic mass" swing-row note.
    ("manuscript/ave-kb/common/universal-saturation-kernel-catalog.md", 151,
     '("relativistic mass") currently hides among the', "relativistic mass"),
    ("manuscript/ave-kb/common/operators.md", 139,
     "the canonical μ-kernel is slew-KEYED", None),
    ("manuscript/common_equations/eq_calibration_constants.tex", 47,
     "per-node inductance (rotational inertia)", None),
    ("manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md",
     15, "I_{max} = \\xi_{topo}\\, c \\approx 124.4", None),
    ("manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md",
     29, "ideal relativistic inductor keyed on the", None),
    # A10 (Tier-2): the FLAG-IMAX-DISCREPANCY cite is :33, not :31.
    ("manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md",
     33, "I_{max}=\\xi_{topo}c\\approx124.4", None),
    ("manuscript/ave-kb/vol3/claim-quality.md", 451,
     "longitudinal inertia in 3D spherical collapse", None),
    ("manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex", 445,
     "longitudinal inertia scales with the Lorentz factor", None),
    ("manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md",
     16, "Topo-Relativistic Impedance Divergence", None),
    # A5 (Tier-2): RHO-B's WRITTEN keying is the static radial strain, not a rate.
    ("manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md",
     21, "S_{topo}(r) = \\sqrt{1 - \\varepsilon_{11}^2}", None),
    ("research/2026-07-31_qlaw-framing-challenge_walk.md", 1201,
     "two different substances, and canon must say so", None),
    ("manuscript/ave-kb/common/wall-taxonomy.md", 433, "the fork is still OPEN", None),
    # A1 (Tier-2): the ratified carve-out had NO cite anywhere in the body.
    ("manuscript/ave-kb/common/wall-taxonomy.md", 499,
     "unwalled at r_sat, its own wall being a κ-amplitude surface",
     "unwalled at `r_sat`, its own wall being a κ-amplitude surface"),
    ("research/2026-08-05_last-bond-kernel-collapse_result.md", 151,
     "carries no micro-rotation at all", None),
    ("_orchestration/docket-entries/2026-08-05-srs-twist-coefficient.md", 22,
     "zero free positional parameters", None),
    ("manuscript/ave-kb/common/axiom-register.md", 190, "underdetermined at $O(\\alpha)$", None),
    ("research/_archive/L5/axiom_derivation_status.md", 313,
     "cleanliness only, NOT load-bearing for closure", None),
    # A13 (Tier-2): BOTH of these were mis-attributed to axiom_derivation_status.md:313.
    # Their real home is the manual's doc-75 entry (Grant's one-sentence collapse + Diag A's
    # amplitude fence).
    ("research/_archive/L3_electron_soliton/VACUUM_ENGINE_MANUAL.md", 42,
     "rest mass saturates L, propagation saturates C", None),
    ("research/_archive/L3_electron_soliton/VACUUM_ENGINE_MANUAL.md", 42,
     "empirically negligible at relevant amplitudes", None),
    # A13 (Tier-2): doc 75's own Rule-12 framing note RETRACTS the "Ax 3" framing.
    ("research/_archive/L3_electron_soliton/75_cosserat_energy_conservation_violation.md", 3,
     'earlier versions of this doc framed the bug as "violates Ax 3 energy conservation."',
     None),
    ("research/2026-08-05_a008-factor-propagation_note.md", 175,
     "G_c/I_\\omega = \\omega_C^2 = 1", None),
    # A2 (Tier-2): the cold-point fence is the A-008 PREREG's row 2, and the result doc
    # renders it DE-WRAPPED (the source wraps it across :25-:26).
    ("research/2026-08-05_a008-factor-propagation_prereg-FROZEN.md", 26,
     "not reach into the saturated regime where omega would be graded",
     "does not reach into the saturated regime"),
    # A1 (Tier-2): the W6 operating-point block — both voices of link L-A.
    ("manuscript/ave-kb/CLAUDE.md", 75,
     "a mass-soliton carrying internal $\\mathbf{E}$ **and** $\\mathbf{B}$ (Symmetric Gravity)",
     None),
    ("manuscript/ave-kb/CLAUDE.md", 75,
     "It does **NOT** follow that any DC bias scales both sectors",
     "It does NOT follow that any DC bias scales both sectors"),
    # A1 (Tier-2): the G2 ruling's verbatim, and its eigenvector receipt.
    ("manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md", 158,
     "NOT the node micro-rotation", None),
    ("manuscript/ave-kb/vol1/claim-quality.md", 1142,
     "$\\omega$-frac max $2.5\\times10^{-7}$", None),
    # A4 (Tier-2): the canon leaf on L-A's FOR side.
    ("manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md", 15,
     "both constitutive parameters scale by the same factor $n \\cdot S$", None),
    ("manuscript/ave-kb/claim-quality.md", 160, "solidity: 0.85 (ok to build on)",
     "ok to build on"),
    # A1 (Tier-2): the v2 fence this lane honors.
    ("research/2026-08-06_approach-leak-v2_result.md", 379,
     "while the engine's `a = 2` stands", None),
    # A8 (Tier-2): the ratified z=3 production carrier the count-ratio lemma names.
    ("manuscript/ave-kb/common/vocabulary-register.md", 526,
     "is the **chiral srs z=3 net**", "the chiral srs z=3 net"),
    ("src/ave/topological/cosserat_field_3d.py", 761, "S_eps_sq = jnp.clip", None),
    ("src/ave/topological/cosserat_field_3d.py", 954, "phase-I placeholder", None),
    ("src/ave/topological/cosserat_field_3d.py", 967, "self.I_omega = float(I_omega)", None),
    ("src/scripts/vol_1_foundations/r8_diag_a_cosserat_wave_speed.py", 257,
     "add S factor to T_kinetic via ρ → ρ·S, I_ω → I_ω·S.", None),
]

# --- A3 (Tier-2): the canon `mu_eff = mu_0 S` sites enumerated in the section-1.1 -----
# name-scoping disclosure. These are cite-verified at file:line; they are NOT body quotes.
MU_EFF_SITES = [
    ("manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md",
     207, r"\mu_{eff}=\mu_0 S_\mu"),
    ("manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md",
     290, r"\mu_{eff}=\mu_0\,S(A)"),
    ("manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md",
     295, r"\mu_{eff}=\mu_0 S(A)\to0"),
    ("manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md",
     371, r"\mu_{eff}=\mu_0 S(A)"),
    ("manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md",
     143, r"\mu_{eff}=\mu_0 S(A)"),
    ("manuscript/backmatter/02_full_derivation_chain.tex", 156, r"\mu_{eff} = \mu_0\,S(A)"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex", 132,
     r"\mu_{eff} = \mu_0 S(A)"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/04_dc_electrical_characteristics.tex", 157,
     r"\mu_{eff}(A_0) = \mu_0\,S(A_0)"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex", 83,
     r"\mu_0\, S(A_0)"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex", 637,
     r"\mu_0\, S(A_0)"),
]

WINDOW = 2  # +/- lines


def quote_ok(path: str, line: int, excerpt: str) -> bool:
    try:
        lines = (REPO / path).read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return False
    lo = max(0, line - 1 - WINDOW)
    hi = min(len(lines), line + WINDOW)
    return excerpt in "\n".join(lines[lo:hi])


def norm(s: str) -> str:
    return " ".join(s.split())


def body_of(doc: str) -> str:
    """The result doc MINUS the Appendix (whose quotes are machine-emitted JSON verbatims)."""
    return doc.split("### Appendix")[0]


def body_quotes(doc: str) -> list[str]:
    return [norm(q) for q in re.findall(r'\*"(.+?)"\*', body_of(doc), flags=re.S)]


# --- CONTROLS: every id here must be exercised by a forced-false receipt --------------
CONTROLS = [
    "NUM-DIGEST-SCAN", "NUM-DIGEST-LAW", "NUM-CENSUS", "NUM-BLOBS", "NUM-FTSCAN-CELLS",
    "NUM-KNIFE", "NUM-KNIFE-ENGINES", "COUNT-REGISTRY", "COUNT-MU-SITES",
    "GATE-SCAN-RECONCILE", "GATE-NCP34-RECONCILE", "GATE-FTSCAN-RECONCILE",
    "GATE-LAW-RECONCILE", "COMPLETE-APPENDIX", "COMPLETE-CLASSTOTALS", "CITE-COMPLETE",
]

CENSUS = {"P-NC3": 6, "P-NC4": 0, "P-I3a": 14, "P-I3b": 19, "P-I3c": 34,
          "P-I4": 0, "P-I5": 67, "P-I6": 0, "P-CAT": 0}
KNIFE_WANT = {("ARM-0", "1"): "1/2", ("ARM-0", "2"): "1",
              ("ARM-1", "1"): "0", ("ARM-1", "2"): "1/2"}


# =====================================================================================
# GATE RECONCILIATION (Tier-2 repair D1) — recompute each gate's verdict from the JSON's
# OWN measured fields and treat any disagreement with the declared label as a FAILURE.
# A gate that consumes its own self-declared label is a checklist, not a gate.
# =====================================================================================
def scan_gate_truth(scan: dict) -> dict[str, tuple[bool, bool, str]]:
    """gate -> (declared, computed_from_measured_fields, evidence)."""
    pats = scan["patterns"]
    g_scan = all(bool(p["methods_agree"]) and p["method_a_hits"] == p["method_b_hits"]
                 for p in pats.values())
    g_scan_ev = "; ".join(
        f"{pid}: agree={p['methods_agree']} A={p['method_a_hits']} B={p['method_b_hits']}"
        for pid, p in sorted(pats.items()))

    nc = scan["gates"]["G-NC-P34"]
    g_nc = bool(nc["P3_byte_identical"]) and bool(nc["P4_byte_identical"])
    g_nc_ev = f"P3_byte_identical={nc['P3_byte_identical']} P4_byte_identical={nc['P4_byte_identical']}"

    ft = scan["gates"]["FT-SCAN"]
    g_ft = (list(ft["absent_counts"]) == [0, 0]
            and int(ft["present_counts"][0]) > 0
            and bool(ft["present_sets_identical"]))
    g_ft_ev = (f"absent_counts={ft['absent_counts']} present_counts={ft['present_counts']} "
               f"present_sets_identical={ft['present_sets_identical']}")

    return {
        "G-SCAN": (bool(scan["gates"]["G-SCAN"]["pass"]), g_scan, g_scan_ev),
        "G-NC-P34": (bool(nc["pass"]), g_nc, g_nc_ev),
        "FT-SCAN": (bool(ft["fires"]), g_ft, g_ft_ev),
    }


def law_gate_truth(law: dict) -> dict[str, tuple[bool, bool, str]]:
    """Same treatment for the law-stage JSON, for every gate that ships a measured field."""
    g = law["gates"]
    rows = [r for br in law["branches"] for r in br["knife_rows"]]

    knife = all(bool(r["engines_agree"]) for r in rows)
    a008 = all(bool(br["cold_point_pin_preserved"]) for br in law["branches"])
    pair = bool(g["G-PAIR"]["residual_zero"])
    ftknife = list(g["FT-KNIFE"]["b3_bins"]) == ["CHANNEL-OPENS", "CHANNEL-OPENS"]

    return {
        "G-KNIFE-ARITH": (bool(g["G-KNIFE-ARITH"]["pass"]), knife,
                          f"per-row engines_agree: {[r['engines_agree'] for r in rows]}"),
        "G-A008-COLD": (bool(g["G-A008-COLD"]["pass"]), a008,
                        "per-branch cold_point_pin_preserved: "
                        f"{[br['cold_point_pin_preserved'] for br in law['branches']]}"),
        "G-PAIR": (bool(g["G-PAIR"]["pass"]), pair,
                   f"residual_zero={g['G-PAIR']['residual_zero']}"),
        "FT-KNIFE": (bool(g["FT-KNIFE"]["fires"]), ftknife,
                     f"b3_bins={g['FT-KNIFE']['b3_bins']}"),
    }


def reconcile(truth: dict, control: str, stage: str) -> list[str]:
    out = []
    for gate, (declared, computed, evidence) in sorted(truth.items()):
        if declared != computed:
            out.append(f"{control}: {stage} gate {gate} DECLARED {declared} but its own "
                       f"measured fields compute {computed} — CONTRADICTION ({evidence})")
        elif not computed:
            out.append(f"{control}: {stage} gate {gate} is not green on its measured "
                       f"fields ({evidence})")
    return out


# =====================================================================================
# The artifact checks, as a PURE function of (doc, scan, law) so a mutation receipt can
# feed a perturbed copy back through the identical code path.
# =====================================================================================
def run_artifact_checks(doc: str, scan: dict, law: dict) -> list[str]:
    f: list[str] = []

    def c(cond: bool, msg: str) -> None:
        if not cond:
            f.append(msg)

    # --- 1. NUMERALS -----------------------------------------------------------------
    c(scan["digest_excluding_runtime"] in doc,
      "NUM-DIGEST-SCAN: scan digest missing from result doc")
    c(law["digest_excluding_runtime"] in doc,
      "NUM-DIGEST-LAW: law-check digest missing from result doc")
    for pid, expected in CENSUS.items():
        got = len(scan["patterns"][pid]["hits_union"])
        c(got == expected,
          f"NUM-CENSUS: {pid}: shipped JSON has {got} union hits, doc census says {expected}")
    c(scan["meta"]["tracked_blob_count"] == 5075 and "5075" in doc,
      "NUM-BLOBS: tracked-blob count 5075 mismatch (JSON vs doc)")

    # The section-1.1 FT-SCAN row must quote the JSON's OWN sentinel counts.
    ft = scan["gates"]["FT-SCAN"]
    ft_cell = f"`{list(ft['absent_counts'])}`; present `{list(ft['present_counts'])}` identical"
    c(ft_cell in doc,
      f"NUM-FTSCAN-CELLS: doc section-1.1 FT-SCAN row does not carry the shipped "
      f"sentinel counts {ft_cell!r}")

    for br in law["branches"]:
        arm = br["name"].split(" ")[0]
        for row in br["knife_rows"]:
            c(KNIFE_WANT.get((arm, row["a"])) == row["p"],
              f"NUM-KNIFE: {arm} a={row['a']}: shipped p={row['p']} != doc table")
            c(bool(row["engines_agree"]),
              f"NUM-KNIFE-ENGINES: {arm} a={row['a']}: engine pair disagrees")

    m = re.search(r"G-CITE registry: `(\d+)` entries", doc)
    c(m is not None and int(m.group(1)) == len(QUOTE_REGISTRY),
      f"COUNT-REGISTRY: doc states {m.group(1) if m else 'NO'} registry entries, "
      f"measured {len(QUOTE_REGISTRY)}")
    m = re.search(r"`(\d+)` canon `μ_eff = μ₀·S` sites", doc)
    c(m is not None and int(m.group(1)) == len(MU_EFF_SITES),
      f"COUNT-MU-SITES: doc states {m.group(1) if m else 'NO'} μ-sites, "
      f"measured {len(MU_EFF_SITES)}")

    # --- 2. GATES (reconciled, not consumed) -----------------------------------------
    for gate, (declared, computed, evidence) in sorted(scan_gate_truth(scan).items()):
        control = {"G-SCAN": "GATE-SCAN-RECONCILE",
                   "G-NC-P34": "GATE-NCP34-RECONCILE",
                   "FT-SCAN": "GATE-FTSCAN-RECONCILE"}[gate]
        if declared != computed:
            f.append(f"{control}: scan gate {gate} DECLARED {declared} but its own measured "
                     f"fields compute {computed} — CONTRADICTION ({evidence})")
        elif not computed:
            f.append(f"{control}: scan gate {gate} is not green on its measured fields "
                     f"({evidence})")
    f += reconcile(law_gate_truth(law), "GATE-LAW-RECONCILE", "law-stage")

    # --- 3. COMPLETENESS -------------------------------------------------------------
    doc_sites = set(re.findall(r"\| \d+ \| `([^`]+):(\d+)` \|", doc))
    missing = []
    for pid, p in scan["patterns"].items():
        for path, line, _text in p["hits_union"]:
            if (path, str(line)) not in doc_sites:
                missing.append(f"{pid} {path}:{line}")
    c(not missing,
      f"COMPLETE-APPENDIX: classification appendix missing {len(missing)} hits: {missing[:5]}")
    for token in ("'ARCHIVE-STAGED': 36", "'NON-LAW': 63", "'DISCOURSE': 41",
                  "CANON-LAW count: 0"):
        c(token in doc, f"COMPLETE-CLASSTOTALS: class-total token missing from doc: {token}")

    # --- 4. CITE-COMPLETE ------------------------------------------------------------
    forms = [norm(body if body is not None else src)
             for _p, _l, src, body in QUOTE_REGISTRY]
    for q in body_quotes(doc):
        c(any(form in q for form in forms),
          f"CITE-COMPLETE: body quote is not covered by any G-CITE registry entry: {q[:70]!r}")

    return f


# =====================================================================================
# MUTATION RECEIPTS (Tier-2 repairs D1 + A11)
# Each receipt perturbs ONE artifact and re-runs the SAME check code. The named control
# must fire; if it does not, the receipt prints MISSED and the run fails. No receipt
# asserts a property of an untouched artifact (the two tautological v1 receipts —
# "the mutated digest is not in the doc", "a phantom path is not in the site set" — are
# retired: neither perturbed anything the checker reads).
# =====================================================================================
def _mut_scan_digest(doc, scan, law):
    d = scan["digest_excluding_runtime"]
    scan["digest_excluding_runtime"] = d[:-1] + ("0" if d[-1] != "0" else "1")
    return doc, scan, law


def _mut_law_digest(doc, scan, law):
    d = law["digest_excluding_runtime"]
    law["digest_excluding_runtime"] = d[:-1] + ("0" if d[-1] != "0" else "1")
    return doc, scan, law


def _mut_census(doc, scan, law):
    scan["patterns"]["P-I3a"]["hits_union"].pop()
    return doc, scan, law


def _mut_blobs(doc, scan, law):
    scan["meta"]["tracked_blob_count"] = 5074
    return doc, scan, law


def _mut_ftscan_cells(doc, scan, law):
    return doc.replace("present `[2, 2]` identical", "present `[7, 7]` identical"), scan, law


def _mut_knife_p(doc, scan, law):
    law["branches"][0]["knife_rows"][0]["p"] = "3/2"
    return doc, scan, law


def _mut_knife_engines(doc, scan, law):
    law["branches"][0]["knife_rows"][0]["engines_agree"] = False
    law["gates"]["G-KNIFE-ARITH"]["pass"] = True  # declared green anyway
    return doc, scan, law


def _mut_registry_count(doc, scan, law):
    m = re.search(r"G-CITE registry: `(\d+)` entries", doc)
    return doc.replace(m.group(0), "G-CITE registry: `999` entries"), scan, law


def _mut_mu_count(doc, scan, law):
    m = re.search(r"`(\d+)` canon `μ_eff = μ₀·S` sites", doc)
    return doc.replace(m.group(0), "`999` canon `μ_eff = μ₀·S` sites"), scan, law


def _mut_gscan_agree(doc, scan, law):
    scan["patterns"]["P-I5"]["methods_agree"] = False   # measured field says DISAGREE
    scan["gates"]["G-SCAN"]["pass"] = True              # label still says PASS
    return doc, scan, law


def _mut_gscan_counts(doc, scan, law):
    scan["patterns"]["P-I5"]["method_a_hits"] = 66      # A != B
    scan["gates"]["G-SCAN"]["pass"] = True              # label still says PASS
    return doc, scan, law


def _mut_ncp34(doc, scan, law):
    scan["gates"]["G-NC-P34"]["P4_byte_identical"] = False
    scan["gates"]["G-NC-P34"]["pass"] = True            # label still says PASS
    return doc, scan, law


def _mut_ftscan_absent(doc, scan, law):
    scan["gates"]["FT-SCAN"]["absent_counts"] = [1, 1]  # absent sentinel WAS found
    scan["gates"]["FT-SCAN"]["fires"] = True            # label still says FIRES
    return doc, scan, law


def _mut_ftscan_present(doc, scan, law):
    scan["gates"]["FT-SCAN"]["present_counts"] = [0, 0]  # present sentinel NOT found
    scan["gates"]["FT-SCAN"]["present_sets_identical"] = False
    scan["gates"]["FT-SCAN"]["fires"] = True             # label still says FIRES
    return doc, scan, law


def _mut_law_pair(doc, scan, law):
    law["gates"]["G-PAIR"]["residual_zero"] = False
    law["gates"]["G-PAIR"]["pass"] = True               # label still says PASS
    return doc, scan, law


def _mut_appendix(doc, scan, law):
    # A REAL unclassified hit: inject a hit the Appendix cannot possibly carry.
    scan["patterns"]["P-CAT"]["hits_union"].append(
        ["manuscript/ave-kb/common/operators.md", 1, "injected unclassified hit"])
    return doc, scan, law


def _mut_classtotal(doc, scan, law):
    return doc.replace("'ARCHIVE-STAGED': 36", "'ARCHIVE-STAGED': 35"), scan, law


def _mut_cite_complete(doc, scan, law):
    marker = "## §8 — WHAT THIS LANE DOES NOT CLAIM"
    inject = '\n\nAn unregistered body quote: *"this excerpt is in no registry entry"*.\n\n'
    return doc.replace(marker, inject + marker), scan, law


RECEIPTS = [
    ("MUT-SCAN-DIGEST", "shipped scan digest perturbed", _mut_scan_digest, "NUM-DIGEST-SCAN"),
    ("MUT-LAW-DIGEST", "shipped law digest perturbed", _mut_law_digest, "NUM-DIGEST-LAW"),
    ("MUT-CENSUS", "one P-I3a union hit dropped", _mut_census, "NUM-CENSUS"),
    ("MUT-BLOBS", "tracked-blob count perturbed", _mut_blobs, "NUM-BLOBS"),
    ("MUT-FTSCAN-CELLS", "doc's FT-SCAN sentinel cell perturbed", _mut_ftscan_cells,
     "NUM-FTSCAN-CELLS"),
    ("MUT-KNIFE-P", "shipped ARM-0 a=1 p perturbed", _mut_knife_p, "NUM-KNIFE"),
    ("MUT-KNIFE-ENGINES", "a knife row's engine pair set to DISAGREE", _mut_knife_engines,
     "NUM-KNIFE-ENGINES"),
    ("MUT-REGISTRY-COUNT", "doc's stated registry size perturbed", _mut_registry_count,
     "COUNT-REGISTRY"),
    ("MUT-MU-COUNT", "doc's stated μ-site count perturbed", _mut_mu_count, "COUNT-MU-SITES"),
    ("MUT-GSCAN-AGREE", "G-SCAN DECLARED pass + a pattern's methods_agree=False",
     _mut_gscan_agree, "GATE-SCAN-RECONCILE"),
    ("MUT-GSCAN-COUNTS", "G-SCAN DECLARED pass + method_a_hits != method_b_hits",
     _mut_gscan_counts, "GATE-SCAN-RECONCILE"),
    ("MUT-NCP34", "G-NC-P34 DECLARED pass + P4 not byte-identical", _mut_ncp34,
     "GATE-NCP34-RECONCILE"),
    ("MUT-FTSCAN-ABSENT", "FT-SCAN DECLARED fires + absent sentinel found", _mut_ftscan_absent,
     "GATE-FTSCAN-RECONCILE"),
    ("MUT-FTSCAN-PRESENT", "FT-SCAN DECLARED fires + present sentinel empty",
     _mut_ftscan_present, "GATE-FTSCAN-RECONCILE"),
    ("MUT-LAW-PAIR", "G-PAIR DECLARED pass + residual_zero=False", _mut_law_pair,
     "GATE-LAW-RECONCILE"),
    ("MUT-APPENDIX", "an unclassified hit injected into the scan JSON", _mut_appendix,
     "COMPLETE-APPENDIX"),
    ("MUT-CLASSTOTAL", "doc's ARCHIVE-STAGED class total perturbed", _mut_classtotal,
     "COMPLETE-CLASSTOTALS"),
    ("MUT-CITE-COMPLETE", "an unregistered italic quote injected into the doc body",
     _mut_cite_complete, "CITE-COMPLETE"),
]


def run_receipts(doc: str, scan: dict, law: dict) -> list[str]:
    out: list[str] = []
    fired: set[str] = set()
    for rid, what, mutate, control in RECEIPTS:
        d2, s2, l2 = mutate(doc, copy.deepcopy(scan), copy.deepcopy(law))
        failures = run_artifact_checks(d2, s2, l2)
        if any(msg.startswith(control) for msg in failures):
            fired.add(control)
        else:
            out.append(f"MISSED — receipt {rid} ({what}) did not fire control {control}; "
                       f"the control is NOT load-bearing")
    for control in CONTROLS:
        if control not in fired:
            out.append(f"MISSED — control {control} is declared but no receipt exercises it")
    return out


def main() -> int:
    doc = RESULT_DOC.read_text(encoding="utf-8")
    scan = json.loads(SCAN_JSON.read_text(encoding="utf-8"))
    law = json.loads(CHECK_JSON.read_text(encoding="utf-8"))

    # 1-4. numerals + gate reconciliation + completeness + cite-completeness -----------
    FAIL.extend(run_artifact_checks(doc, scan, law))

    # 5. LAW-RERUN --------------------------------------------------------------------
    # Re-run live, compare digests, then RESTORE the shipped bytes so a `make verify`
    # never dirties the working tree (the re-run rewrites _runtime_sec). The live driver
    # exits nonzero unless every law-stage gate is green, which is the compensating
    # control for FT-A008 / FT-PAIR (the two gates shipping no measured field).
    shipped_bytes = CHECK_JSON.read_bytes()
    try:
        r = subprocess.run([sys.executable, str(DRIVERS / "iomega_law_check.py")],
                           capture_output=True, text=True, cwd=REPO)
        check(r.returncode == 0, f"LAW-RERUN: iomega_law_check.py re-run failed: {r.stdout[-300:]}")
        law2 = json.loads(CHECK_JSON.read_text(encoding="utf-8"))
        check(law2["digest_excluding_runtime"] == law["digest_excluding_runtime"],
              "LAW-RERUN: law-check re-run digest drifted")
    finally:
        CHECK_JSON.write_bytes(shipped_bytes)

    # 6. QUOTES (G-CITE) at HEAD ------------------------------------------------------
    for path, line, excerpt, _body in QUOTE_REGISTRY:
        check(quote_ok(path, line, excerpt),
              f"G-CITE: excerpt not within ±{WINDOW} lines of {path}:{line}: {excerpt[:50]!r}")

    # 7. MU-SITES (the section-1.1 A3 enumeration) ------------------------------------
    for path, line, token in MU_EFF_SITES:
        check(quote_ok(path, line, token),
              f"MU-SITE: token not within ±{WINDOW} lines of {path}:{line}: {token!r}")

    # 8. MUTATION receipts ------------------------------------------------------------
    FAIL.extend(run_receipts(doc, scan, law))
    # FT-CITE / FT-MU: forced-false IO controls — a registry entry aimed at the wrong line
    # (and a μ-site token aimed at the wrong line) must FAIL.
    p0, l0, e0, _b0 = QUOTE_REGISTRY[0]
    check(not quote_ok(p0, l0 + 7, e0 + "X"),
          "MISSED — FT-CITE: a perturbed registry entry did not fail")
    mp, ml, mt = MU_EFF_SITES[0]
    check(not quote_ok(mp, ml + 40, mt + "X"),
          "MISSED — FT-MU: a perturbed μ-site entry did not fail")

    if FAIL:
        print("[iomega_law_number_check] FAIL")
        for x in FAIL:
            print("  ✗", x)
        return 1
    print(f"[iomega_law_number_check] PASS — numerals + {len(CONTROLS)} reconciled/recomputed "
          f"controls + law-rerun + completeness "
          f"({sum(len(p['hits_union']) for p in scan['patterns'].values())} hits) + "
          f"{len(QUOTE_REGISTRY)} registry quotes + {len(MU_EFF_SITES)} μ-sites + "
          f"{len(RECEIPTS)} mutation receipts (all fired) + 2 forced-false cite receipts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
