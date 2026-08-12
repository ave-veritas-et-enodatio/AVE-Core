#!/usr/bin/env python3
"""R40 STUCK-row note guard — a STUCK-POINT row must assert NO resolution, ever.

WHY THIS FILE EXISTS
--------------------
R40 batch 2a left two NEEDS-RE-DERIVATION rows UNACTIONED because their resolution
pointer is genuinely ambiguous, and routed them to Grant under the stop-and-ask
protocol.  The per-file EOF notes are machine-generated, and the generator emitted
its boilerplate ``**Resolution.**`` paragraph for EVERY row regardless of
disposition — so both STUCK rows landed in the corpus asserting the very pointer
the batch had refused to assert (and one of them additionally carried a
``BIAS-DEBT`` rider over a carrier that a prior Grant ruling had already placed in
a different sector).

That is **substitution-not-retraction at row level**: a slot that should have been
left empty was refilled with generator boilerplate.  Prose review caught it; no
gate could, because no gate knew the rule.  This module is that rule, as code.

THE RULE
--------
A row entry marked ``NOT STAMPED — STUCK-POINT`` must carry, between its own
header and the next row entry (or the end of its note):

  * NO resolution clause  — no ``**Resolution.**`` / ``RESOLUTION:`` paragraph,
    and no sentence naming Axiom 5 / clause G / the bound response as this row's
    replacement;
  * NO rider or scope tag — no ``BIAS-DEBT``, ``PAST-WALL`` or ``R49`` tag.

A row entry that IS stamped, or that is byte-fence ROUTED to a ledger, is
UNAFFECTED: those rows are demoted, and naming their pointer is the whole job.
The guard therefore has to discriminate, not just search — which is what the
negative control below proves.

WHAT IT IS NOT
--------------
Not a judgement about whether a row SHOULD be stuck.  It only enforces that a row
declared stuck is left empty.  Choosing the bin is a physics call and stays with
Grant.

USAGE
-----
    python research/drivers/r40_stuck_row_note_guard_number_check.py
    python research/drivers/r40_stuck_row_note_guard_number_check.py --mutation-receipt
"""
from __future__ import annotations

import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#: A generated row entry header, markdown form and comment form.
ROW_MD = re.compile(r"^- \*\*`:(\d+)`\*\* — (.*)$")
ROW_CM = re.compile(r"^\s*[%#]\s+:(\d+)\s+family:\s*(.*)$")

STUCK_MARK = re.compile(r"NOT STAMPED\s*[—-]{1,2}\s*STUCK-POINT", re.I)

#: What a stuck row must NOT contain.
RESOLUTION = re.compile(
    r"\*\*Resolution\.\*\*|(?<![A-Za-z])RESOLUTION:"
    r"|under Axiom 5 clause G|the demoted carrier is",
    re.I,
)
TAGS = re.compile(r"BIAS-DEBT|PAST-WALL|R49[- ]4[Pπ]I|R49 4π-CONVENTION")


def note_rows(lines):
    """Yield (lineno, header_text, body_lines) for every generated row entry."""
    starts = []
    for i, l in enumerate(lines, 1):
        m = ROW_MD.match(l) or ROW_CM.match(l)
        if m:
            starts.append((i, l))
    for k, (i, hdr) in enumerate(starts):
        end = starts[k + 1][0] - 1 if k + 1 < len(starts) else len(lines)
        yield i, hdr, lines[i:end]


def violations_in(path, lines):
    """Every stuck row in `lines` that asserts a resolution or carries a tag."""
    out = []
    for lineno, hdr, body in note_rows(lines):
        if not STUCK_MARK.search(hdr):
            continue
        why = []
        if RESOLUTION.search(hdr) or any(RESOLUTION.search(b) for b in body):
            why.append("asserts a resolution clause")
        if TAGS.search(hdr) or any(TAGS.search(b) for b in body):
            why.append("carries a rider/scope tag")
        if why:
            out.append((path, lineno, "; ".join(why)))
    return out


def corpus_files():
    out = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in {".git", ".venv", "__pycache__", "node_modules"}]
        for fn in files:
            if os.path.splitext(fn)[1] in {".md", ".tex", ".py"}:
                out.append(os.path.relpath(os.path.join(root, fn), REPO))
    return sorted(out)


def scan():
    n_stuck, viol = 0, []
    for rel in corpus_files():
        try:
            lines = open(os.path.join(REPO, rel), encoding="utf-8").read().split("\n")
        except (OSError, UnicodeDecodeError):
            continue
        if not any(STUCK_MARK.search(l) for l in lines):
            continue
        for _, hdr, _ in note_rows(lines):
            if STUCK_MARK.search(hdr):
                n_stuck += 1
        viol += violations_in(rel, lines)
    return n_stuck, viol


# --------------------------------------------------------------------- fixtures

#: A synthetic STUCK row that DOES carry the boilerplate — the shape that shipped.
#: The guard MUST flag it, or it cannot have caught the real defect.
SYNTHETIC_BAD = """- **`:95`** — **NOT STAMPED — STUCK-POINT, routed to Grant** (the pointer is ambiguous). *(family: probe)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  a probe quote
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**.

- **`:180`** — stamped at `:180`. *(family: probe-2)*
""".split("\n")

#: A synthetic STAMPED row carrying the SAME boilerplate — legitimate, and the
#: guard MUST NOT flag it.  Without this control the guard could be a bare grep
#: for "Resolution." and would fail every correctly-demoted row in the batch.
SYNTHETIC_GOOD = """- **`:180`** — stamped at `:180`. *(family: probe)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  a probe quote
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**.
""".split("\n")

#: A synthetic STUCK row cleaned to the required shape — must NOT flag.
SYNTHETIC_CLEAN = """- **`:95`** — **NOT STAMPED — STUCK-POINT, routed to Grant** (the pointer is ambiguous). *(family: probe)*
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  a probe quote
  ```

  **Routed to Grant — no resolution is asserted here.** This entry names no pointer, carries no rider and carries no tag.
""".split("\n")


def run_gate(verbose=True):
    ok = True

    def say(good, label, detail):
        nonlocal ok
        ok = ok and good
        if verbose:
            print(f"  [{'PASS' if good else 'FAIL'}] {label}: {detail}")

    bad = violations_in("<synthetic-bad>", SYNTHETIC_BAD)
    say(len(bad) == 1, "can-it-fire on a synthetic STUCK row carrying the boilerplate",
        f"{len(bad)} flagged" + (f" ({bad[0][2]})" if bad else " — THE GUARD IS DEAD"))
    good = violations_in("<synthetic-good>", SYNTHETIC_GOOD)
    say(not good, "negative control: a STAMPED row may assert its resolution",
        f"{len(good)} flagged (must be 0 — a demoted row NAMES its pointer)")
    clean = violations_in("<synthetic-clean>", SYNTHETIC_CLEAN)
    say(not clean, "a correctly-cleaned STUCK row passes", f"{len(clean)} flagged")

    n_stuck, viol = scan()
    say(n_stuck > 0, "STUCK rows found in the corpus (an empty scan is not a clean scan)",
        f"{n_stuck} stuck row entr(ies) scanned")
    say(not viol, "no STUCK row asserts a resolution or carries a tag",
        f"{len(viol)} violation(s)" + ("" if not viol else ": "
        + "; ".join(f"{p}:{ln} ({w})" for p, ln, w in viol)))
    return ok


def mutation_receipt():
    print("[r40-stuck] MUTATION RECEIPT — perturbations must trip; behavioral probes must hold")
    results = []
    # M1 — blind the STUCK marker: the synthetic bad row must stop flagging.
    saved = STUCK_MARK.pattern
    globals()["STUCK_MARK"] = re.compile(r"\bZZZZ-NEVER-MATCHES\b")
    results.append(("M1 blind the STUCK marker", not violations_in("x", SYNTHETIC_BAD)))
    globals()["STUCK_MARK"] = re.compile(saved, re.I)
    # M2 — blind the resolution vocabulary: the tag half must still catch the bad row.
    saved_r = RESOLUTION.pattern
    globals()["RESOLUTION"] = re.compile(r"\bZZZZ-NEVER-MATCHES\b")
    v = violations_in("x", SYNTHETIC_BAD)
    results.append(("M2 blind the resolution vocabulary (tag half must still fire)",
                    len(v) == 1 and "tag" in v[0][2]))
    globals()["RESOLUTION"] = re.compile(saved_r, re.I)
    # M3 — blind the tag vocabulary: the resolution half must still catch it.
    saved_t = TAGS.pattern
    globals()["TAGS"] = re.compile(r"\bZZZZ-NEVER-MATCHES\b")
    v = violations_in("x", SYNTHETIC_BAD)
    results.append(("M3 blind the tag vocabulary (resolution half must still fire)",
                    len(v) == 1 and "resolution" in v[0][2]))
    globals()["TAGS"] = re.compile(saved_t)
    # M4 — row-boundary integrity: the NEXT row's resolution must not be attributed
    # to the stuck row.  Clean stuck row followed by a stamped row that has one.
    mixed = SYNTHETIC_CLEAN + SYNTHETIC_GOOD
    results.append(("M4 a later stamped row's resolution is not charged to the stuck row",
                    not violations_in("x", mixed)))
    allgood = True
    for label, tripped in results:
        print(f"  [{'OK' if tripped else 'BROKEN'}] {label} -> "
              f"{'probe holds (good)' if tripped else 'probe FAILS (BAD)'}")
        allgood = allgood and tripped
    if not allgood:
        print("[r40-stuck] MUTATION RECEIPT FAILED")
        return 1
    print("[r40-stuck] MUTATION RECEIPT OK: every perturbation trips and every probe holds.")
    return 0


def main():
    if "--mutation-receipt" in sys.argv:
        return mutation_receipt()
    print("[r40-stuck] R40 STUCK-row note guard (a stuck row asserts no resolution)")
    ok = run_gate()
    if not ok:
        print("[r40-stuck] FAILED")
        return 1
    print("[r40-stuck] OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
