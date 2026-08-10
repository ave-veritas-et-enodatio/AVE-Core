#!/usr/bin/env python3
"""Driver for the bound-response carve lane (R38).

Two jobs, both deterministic, no RNG, engine ``src/ave`` byte-untouched:

1. ALGEBRA RECEIPTS -- the identities the result doc consumes, recomputed from
   first principles (fractions/sqrt), including the #919/#930 partition family
   reproduced as SUPERSEDED-INPUT record (the imported reading's own numbers,
   quoted to show what the carve un-fires -- NOT lane-native derivations), and
   the LC-1 receipt that the longitudinal superluminality is G-driven
   (c_P/c_S = sqrt(4/3) at K=0), so no VALUE of K un-fires the kill -- only the
   constraint class does.

2. CONSUMER SWEEP (gate G-CONSUMER-2M) -- two named engines (GNU ``grep -rniE``
   via subprocess + Python ``re``) over the CANON scope (``manuscript/`` +
   ``src/ave/``) and, separately tagged, the RECORD scope (``research/`` +
   ``_orchestration/``, frozen-snapshot/Q2 class -- enumerated for completeness,
   never reclassified).  Per-family file:line hits, per-engine, with the
   known-positive control set gating instrument liveness (a sweep that misses
   the known propagating-claim sites is dead; no absence claim banks from it).

Output: ``bound_response_carve_results.json`` (sorted keys, deterministic).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(HERE, "bound_response_carve_results.json")

# ---------------------------------------------------------------- algebra ---


def algebra() -> dict:
    """Exact identities, then floats. K and G enter as symbols via ratios."""
    # Poisson ratio nu = (3K - 2G) / (2(3K + G)) at K = 2G  ->  4G/14G = 2/7.
    K_over_G = Fraction(2, 1)
    nu = (3 * K_over_G - 2) / (2 * (3 * K_over_G + 1))
    assert nu == Fraction(2, 7)
    # Volumetric trace factor of a uniaxial response: (1 - 2 nu) = 3/7.
    trace_factor = 1 - 2 * nu
    assert trace_factor == Fraction(3, 7)
    # P/S speed ratio squared: (K + 4G/3)/G.
    cP2_over_cS2_K2G = K_over_G + Fraction(4, 3)          # = 10/3
    cP2_over_cS2_K0 = Fraction(0, 1) + Fraction(4, 3)     # = 4/3 (K = 0)
    assert cP2_over_cS2_K2G == Fraction(10, 3)
    # The imported partition family: F = (2/3) (c_S/c_P)^5.
    def partition(cp_over_cs: float) -> float:
        return (2.0 / 3.0) * (1.0 / cp_over_cs) ** 5

    cp_vrh = float(cP2_over_cS2_K2G) ** 0.5               # 1.8257418583505538
    part_vrh = partition(cp_vrh)                          # 0.03286335345031
    # #919 speed-reading spread endpoints (SUPERSEDED-INPUT record):
    part_100 = partition(1.7105)                          # ~0.0455
    part_min = partition(2.1304)                          # ~0.0152
    # Seismology external anchor (Aki-Richards import, q1 section 6):
    #   E_S/E_P = (3/2) (V_p/V_s)^5 at Poisson solid V_p/V_s = sqrt(3).
    es_over_ep = 1.5 * (3.0 ** 0.5) ** 5                  # ~23.38
    # Comparators (frozen, #930 prereg section 4 provenance):
    delta_HT = 0.0016
    delta_DP = 1.3e-4
    return {
        "nu_at_K2G": {"exact": "2/7", "float": float(nu)},
        "trace_factor_1_minus_2nu": {"exact": "3/7", "float": float(trace_factor)},
        "cP_over_cS_at_K2G": {"exact": "sqrt(10/3)", "float": cp_vrh},
        "cP_over_cS_at_K0": {"exact": "sqrt(4/3)",
                             "float": float(cP2_over_cS2_K0) ** 0.5},
        "sqrt2": 2.0 ** 0.5,
        "partition_at_VRH": part_vrh,
        "partition_over_delta_DP": part_vrh / delta_DP,   # ~252.8
        "partition_sigma_HT": part_vrh / delta_HT,        # ~20.5
        "floor_family_superseded_input": {
            "at_cp_2.1304": part_min,                     # ~0.0152
            "at_cp_1.7105": part_100,                     # ~0.0455
            "sigma_HT_low": part_min / delta_HT,          # ~9.5
            "sigma_HT_high": part_100 / delta_HT,         # ~28.5
            "x_DP_low": part_min / delta_DP,              # ~117
            "x_DP_high": part_100 / delta_DP,             # ~350
        },
        "aki_richards_ES_over_EP_poisson": es_over_ep,
        "delta_HT": delta_HT,
        "delta_DP": delta_DP,
        "F_bulk_under_carve": 0.0,
    }


# ------------------------------------------------------------------ sweep ---

# Pattern families.  Each: (family key, ERE pattern, optional same-line context
# ERE).  Case-insensitive both engines.  The context filter guards against
# keyword-only noise (e.g. "10/3" as a date).
FAMILIES = [
    ("F1_radiative_P", r"sqrt\{?\(?10/3|10/3\}?\)?\s*(\\,)?\s*c|1\.8257|1\.826|P-?wave|compressional",
     r"bulk|longitudinal|dilatat|speed|c_L|c_P|radiat|wave"),
    ("F2_vlong_sqrt2", r"V_\{?LONG\}?|bulk.?sound|sqrt\{?2\}?\s*(\\,)?\s*(\\?,)?\s*c[^a-z]|1\.4142",
     r"bulk|longitudinal|dilatat|A_?1|port|speed"),
    ("F3_partition", r"kappa_?env|Aki|seismolog|seismic\s+partition|E_S\s*/\s*E_P|23\.4|\(2/3\)\s*\(\s*c_S\s*/\s*c_P",
     None),
    ("F4_zbulk_wall", r"Z_\{?bulk\}?|c_\{?bulk\}?|Gamma_\{?bulk\}?",
     None),
    ("F5_propagates", r"propagat\w+\s+P-?branch|P-?branch|bulk\s+restoring\s+force|K\s*\(?\s*(\\nabla|∇)\s*(\\cdot|·)|(\\nabla|∇)\s*(\\cdot|·)\s*(\\mathbf\{)?u\}?\s+propagates",
     None),
    ("F6_reading_A", r"Reading[- ]A|bulk\s+radiative\s+port|scalar[- ]GW|bulk\s+admixture",
     None),
    ("F7_vsnap_mech", r"V_\{?snap\}?",
     r"longitudinal|A_?1|compliance|tank|mechanical|bulk"),
    ("F8_regime4_bulk", r"Regime[- ]?IV|regime_4",
     r"bulk|longitudinal|c_P|compression|dilatat"),
]

CANON_SCOPES = [("manuscript", ["*.md", "*.tex"]), ("src/ave", ["*.py"])]
RECORD_SCOPES = [("research", ["*.md"]), ("_orchestration", ["*.md"])]
EXCLUDE_DIRS = {"research/_archive", ".git"}

# Known-positive controls (instrument liveness): (path-substring, family).
CONTROLS = [
    ("manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md", "F5_propagates"),
    ("manuscript/ave-kb/common/port-register.md", "F1_radiative_P"),
    ("manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md", "F1_radiative_P"),
    ("manuscript/ave-kb/vol3/gravity/ch08-gravitational-waves/gw-propagation-lossless.md", "F6_reading_A"),
]


def _excluded(path: str) -> bool:
    rel = os.path.relpath(path, REPO)
    return any(rel.startswith(x) for x in EXCLUDE_DIRS)


def sweep_grep(scope: str, globs: list[str], pattern: str, context: str | None) -> list[str]:
    """Engine 1: GNU/BSD grep -rniE, one invocation per family per scope."""
    cmd = ["grep", "-rniE", pattern, os.path.join(REPO, scope)]
    for g in globs:
        cmd.insert(2, "--include=" + g)
    cmd.insert(2, "--exclude-dir=_archive")
    cmd.insert(2, "--exclude-dir=.git")
    proc = subprocess.run(cmd, capture_output=True, text=True)
    hits = []
    ctx = re.compile(context, re.IGNORECASE) if context else None
    for line in proc.stdout.splitlines():
        try:
            path, lineno, text = line.split(":", 2)
        except ValueError:
            continue
        if _excluded(path):
            continue
        if ctx and not ctx.search(text):
            continue
        hits.append(f"{os.path.relpath(path, REPO)}:{lineno}")
    return sorted(set(hits))


def sweep_re(scope: str, globs: list[str], pattern: str, context: str | None) -> list[str]:
    """Engine 2: Python re, independent file walk."""
    pat = re.compile(pattern, re.IGNORECASE)
    ctx = re.compile(context, re.IGNORECASE) if context else None
    exts = tuple(g.lstrip("*") for g in globs)
    hits = []
    for root, dirs, files in os.walk(os.path.join(REPO, scope)):
        dirs[:] = [d for d in dirs if d not in (".git", "_archive")]
        for fn in files:
            if not fn.endswith(exts):
                continue
            path = os.path.join(root, fn)
            if _excluded(path):
                continue
            try:
                with open(path, encoding="utf-8", errors="replace") as fh:
                    for i, line in enumerate(fh, 1):
                        if pat.search(line) and (not ctx or ctx.search(line)):
                            hits.append(f"{os.path.relpath(path, REPO)}:{i}")
            except OSError:
                continue
    return sorted(set(hits))


def run_sweep() -> dict:
    out = {"canon": {}, "record": {}, "controls": {}, "engine_names":
           {"engine1": "grep -rniE (system grep, one invocation per family/scope)",
            "engine2": "python re (independent os.walk)"}}
    for tag, scopes in (("canon", CANON_SCOPES), ("record", RECORD_SCOPES)):
        for fam, pat, ctx in FAMILIES:
            g_hits: list[str] = []
            r_hits: list[str] = []
            for scope, globs in scopes:
                g_hits += sweep_grep(scope, globs, pat, ctx)
                r_hits += sweep_re(scope, globs, pat, ctx)
            g_hits, r_hits = sorted(set(g_hits)), sorted(set(r_hits))
            union = sorted(set(g_hits) | set(r_hits))
            out[tag][fam] = {
                "engine1_count": len(g_hits),
                "engine2_count": len(r_hits),
                "union_count": len(union),
                "engines_disagree": sorted(set(g_hits) ^ set(r_hits)),
                "union": union,
            }
    # Liveness controls: each control site must appear in BOTH engines' canon
    # hits for its family.
    for path_sub, fam in CONTROLS:
        fam_union = out["canon"][fam]["union"]
        fam_disagree = set(out["canon"][fam]["engines_disagree"])
        found = [h for h in fam_union if h.startswith(path_sub)]
        both = [h for h in found if h not in fam_disagree]
        out["controls"][f"{path_sub}|{fam}"] = {
            "found": bool(found), "found_by_both_engines": bool(both),
            "sites": found[:5]}
    out["instrument_live"] = all(v["found_by_both_engines"]
                                 for v in out["controls"].values())
    return out


def main() -> int:
    result = {"algebra": algebra(), "sweep": run_sweep()}
    blob = json.dumps(result, indent=1, sort_keys=True, ensure_ascii=False)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(blob + "\n")
    digest = hashlib.sha256(blob.encode()).hexdigest()
    print(f"wrote {os.path.relpath(OUT, REPO)}  sha256={digest}")
    print(f"instrument_live={result['sweep']['instrument_live']}")
    for fam, d in result["sweep"]["canon"].items():
        print(f"  canon {fam}: e1={d['engine1_count']} e2={d['engine2_count']} "
              f"union={d['union_count']} disagree={len(d['engines_disagree'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
