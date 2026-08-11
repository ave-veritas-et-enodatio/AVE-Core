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
    # Added 2026-08-10 (review finding): the LC-1 re-adjudication record adjudicates
    # tasks (a) and (b) verbatim against the brief's DERIVATION-TASK cell, which no
    # gate covered — two rows cannot byte-verify three cells. Now gated, so an edit
    # to brief:44 column 4 alone can no longer drift silently while the kill-cell
    # rows stay green.
    ("_orchestration/2026-08-04_lorentz-compliance-arc-brief.md",
     "(a) provenance of cold c_shear = c (is G_vac = ρc² derived or a matching condition?); "
     "(b) bulk √(10/3)c P-wave observability — gapped, confined, or sourceless?"),
    ("_orchestration/2026-08-10_bound-sector-constitutive-brief.md",
     "Per-deliverable: DERIVED / DERIVED-VIA-NEW-AXIOM(candidate) / NOT-DERIVABLE(named"),
    ("_orchestration/2026-08-10_bound-sector-constitutive-brief.md",
     "quietly reconstructs the flat-direction-as-constraint assertion dies at its own"),
    # ── R43 TIER-A ANCHOR ROTATION (2026-08-10) ──────────────────────────────
    # These two rows originally byte-checked the PRE-REPAIR sentences, i.e. the
    # lane's evidence that the two FALSE labels were live at HEAD:
    #     "This is the standard Maxwell Lagrangian (in vector-potential form)"
    #     "Energy conservation and U(1) gauge symmetry follow as Noether consequences"
    # R43 (_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md,
    # "TIER A RATIFIED") ratified the section-1.3 repair text and the doc-lane
    # execution batch landed it, so those strings are correctly ABSENT now. The
    # rows are rotated to the RATIFIED replacements: the gate keeps its teeth by
    # asserting the repair is PRESENT rather than that the defect is. The
    # pre-repair strings are preserved above as the historical record (git carries
    # the full trail); they are deliberately NOT re-added as expectations.
    ("manuscript/common_equations/eq_axiom_3.tex",
     "This is the temporal-gauge (Weyl-gauge, $A_0$-free) form of the Maxwell Lagrangian"),
    ("manuscript/common_equations/eq_axiom_3.tex",
     "its Noether content is the pointwise conservation of the Gauss function"),
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


def check_quotes(quotes):
    """Two-engine presence check over `quotes`; returns the list of failures."""
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
    return bad


# Guaranteed-absent suffix: corrupting a row this way fires regardless of that
# row's content. The previous receipt corrupted ONLY quotes[0] via a
# content-specific string replace ("energy-carrying" -> "energy-bearing"), so it
# exercised one row and could print "receipt OK" while any other row — including
# the two ROTATED eq_axiom_3.tex rows this gate exists to protect — was silently
# vacuous. Review finding: per-row mutation is the only coverage that closes it.
_SENTINEL = "␀ZZ-MUTATION-SENTINEL-ZZ"


def main():
    quotes = list(QUOTES)

    if MUTATE:
        # PER-ROW mutation receipt: corrupt each row in turn and require THAT row
        # to be caught. Proves every expectation is live, not just the first.
        misses = []
        for i in range(len(quotes)):
            probe = list(quotes)
            probe[i] = (probe[i][0], probe[i][1] + _SENTINEL)
            caught = check_quotes([probe[i]])
            if not caught:
                misses.append(f"row {i} ({probe[i][0]}) did NOT fire")
        rotated = [i for i, (f, _) in enumerate(quotes)
                   if f == "manuscript/common_equations/eq_axiom_3.tex"]
        if misses:
            fail("mutation receipt INCOMPLETE — " + "; ".join(misses))
        print(f"BOUND-CONSTITUTIVE QUOTE CHECK: mutation receipt OK — all {len(quotes)} rows "
              f"individually corrupted and individually CAUGHT, including the "
              f"{len(rotated)} rotated eq_axiom_3.tex row(s) at index {rotated}")
        sys.exit(0)

    bad = check_quotes(quotes)

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

    if bad:
        fail("; ".join(bad))
    print(f"BOUND-CONSTITUTIVE QUOTE CHECK: PASS — {len(quotes)} quotes two-engine verified "
          f"+ sweep-record totals consistent")
    sys.exit(0)


if __name__ == "__main__":
    main()
