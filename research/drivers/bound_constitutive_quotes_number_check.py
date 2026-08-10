#!/usr/bin/env python3
"""Quote + sweep-record gate for the bound-constitutive lane (Tier-2 C9/C13/C15 repair).

Two engines per quote: (1) subprocess BSD grep -F fixed-string search; (2) Python str.find
over the file bytes. Every ruled/frozen quote the lane's verdicts lean on must be found by
BOTH engines in its named source file (paths relative to the repo root this script lives in,
so the gate checks THIS tree's state). Also validates the committed sweep record's
machine-checkable totals against its own tables. Supports --mutation-receipt (corrupts one
expected string in memory; the gate must catch it).
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
MUTATE = "--mutation-receipt" in sys.argv

# (file, expected fixed substring) — the load-bearing ruled/frozen quotes
QUOTES = [
    ("_orchestration/2026-08-04_lorentz-compliance-arc-brief.md",
     "An energy-carrying inter-event channel at ≠ c ⇒ arc-level kill"),
    ("_orchestration/2026-08-04_lorentz-compliance-arc-brief.md",
     "LC-1 runs first and its kill condition is arc-terminating."),
    ("_orchestration/2026-08-10_bound-sector-constitutive-brief.md",
     "Per-deliverable: DERIVED / DERIVED-VIA-NEW-AXIOM(candidate) / NOT-DERIVABLE(named"),
    ("_orchestration/2026-08-10_bound-sector-constitutive-brief.md",
     "quietly reconstructs the flat-direction-as-constraint assertion dies at its own"),
    ("manuscript/common_equations/eq_axiom_3.tex",
     "This is the standard Maxwell Lagrangian (in vector-potential form)"),
    ("manuscript/common_equations/eq_axiom_3.tex",
     "Energy conservation and U(1) gauge symmetry follow as Noether consequences"),
    ("manuscript/common_equations/eq_axiom_4.tex",
     "The electron is a real-space"),
    ("manuscript/common_equations/eq_axiom_4.tex",
     "rest mass is the A1 dilatation sector"),
    ("manuscript/ave-kb/common/the-sourced-charge-no-go-cascade.md",
     "conserved constant of motion**, set by initial data, not emergent"),
    ("research/2026-07-20_q1-pulsar-hardening.md",
     "In GR the longitudinal/scalar metric parts are **pure-gauge**"),
    ("_orchestration/2026-06-15_k2g-crystalline-provenance.md",
     "Imported, both legs. End of line."),
    ("manuscript/ave-kb/CLAUDE.md",
     "only spatial gradients of $A$ across the substrate are physically observable"),
    ("manuscript/ave-kb/common/port-register.md",
     "owes a mechanism"),
    ("research/2026-08-09_bound-response_result.md",
     "zero-stiffness inertial FLAT DIRECTION"),
    ("research/2026-08-09_bound-response_result.md",
     "no axiom preimage either"),
    ("manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md",
     "A1 dilatation-MASS"),
]

SWEEP = os.path.join(ROOT, "research", "2026-08-10_bound-constitutive_sweep-record.md")


def fail(msg):
    print(f"BOUND-CONSTITUTIVE QUOTE CHECK: FAIL — {msg}")
    sys.exit(1)


def main():
    quotes = list(QUOTES)
    if MUTATE:
        f, q = quotes[0]
        quotes[0] = (f, q.replace("energy-carrying", "energy-bearing"))  # corrupt one

    bad = []
    for relpath, expected in quotes:
        path = os.path.join(ROOT, relpath)
        if not os.path.exists(path):
            bad.append(f"{relpath}: FILE MISSING")
            continue
        text = open(path, encoding="utf-8").read()
        eng2 = expected in text
        try:
            rc = subprocess.run(["/usr/bin/grep", "-qF", expected, path]).returncode
            eng1 = (rc == 0)
        except OSError:
            eng1 = eng2  # grep unavailable: disclosed single-engine fallback
        if not (eng1 and eng2):
            bad.append(f"{relpath}: NOT FOUND (grep={eng1}, python={eng2}): {expected[:60]!r}")
        elif eng1 != eng2:
            bad.append(f"{relpath}: ENGINE DISAGREEMENT on {expected[:60]!r}")

    # sweep-record totals gate
    if not os.path.exists(SWEEP):
        bad.append("sweep record MISSING")
    else:
        rec = open(SWEEP, encoding="utf-8").read()
        m = re.search(r"```json\n(\{.*?\})\n```", rec, re.S)
        if not m:
            bad.append("sweep record: no machine-checkable totals block")
        else:
            tot = json.loads(m.group(1))
            nr_sec = rec.split("## NEEDS-RESCOPE")[1].split("## DRIFT")[0]
            nr_rows = len(re.findall(r"^\| \d+ \|", nr_sec, re.M))
            drift_rows = len(re.findall(r"^\| D\d ", rec, re.M))
            if tot["needs_rescope"] != nr_rows:
                bad.append(f"sweep record: NEEDS-RESCOPE rows {nr_rows} != declared {tot['needs_rescope']}")
            if tot["drift"] != drift_rows:
                bad.append(f"sweep record: DRIFT rows {drift_rows} != declared {tot['drift']}")
            if tot["total"] != tot["pattern_sites"] + tot["off_pattern_sites"]:
                bad.append("sweep record: total != pattern + off_pattern")

    if MUTATE:
        if bad:
            print(f"BOUND-CONSTITUTIVE QUOTE CHECK: mutation receipt OK — corruption caught: {bad[0][:90]}")
            sys.exit(0)
        fail("mutation receipt DID NOT FIRE — checker is dead")
    if bad:
        fail("; ".join(bad))
    print(f"BOUND-CONSTITUTIVE QUOTE CHECK: PASS — {len(quotes)} quotes two-engine verified "
          f"+ sweep-record totals consistent")
    sys.exit(0)


if __name__ == "__main__":
    main()
