#!/usr/bin/env python3
"""R40 quote-claim STRENGTH check — the preamble and the row labels may not diverge.

WHY THIS FILE EXISTS
--------------------
One defect recurred THREE TIMES at three levels of the same document, and each fix
was scoped to the instance that had been found rather than to the class:

  1. ONE hand-typed quote in the batch record was labelled byte-exact and was in
     fact fabricated  -> fixed at the instance;
  2. ALL 185 generated ROW LABELS said byte-exact over markup-reduced strings
     (95 of 185 byte-exact, 90 not)  -> fixed at the row level;
  3. ALL 109 note PREAMBLES said "Corpus text quoted below is byte-exact and is
     never reworded", five to eleven lines ABOVE the row labels just corrected
     -> found only by a third reviewer.

The engines that verify these quotes are REDUCTION engines (they normalise markup
and whitespace); they establish CONTENT PRESENCE at the anchor and cannot
establish byte-identity.  So a note must not claim byte-identity anywhere.  More
importantly, a note must make ONE strength claim: if the preamble and the row
labels disagree, a reader is licensed to believe the stronger one.

THIS CHECK IS THE CLASS-LEVEL FIX.  It asserts, per note:

  * no STRONG claim (byte-exact / byte-identical / verbatim-at-HEAD) about the
    quoted corpus text appears in the preamble OR in a row label; and
  * the preamble and the row labels agree in strength — a note whose preamble says
    byte-exact while its rows say content-verified FAILS.

BOTH CARRIER FORMS ARE COVERED.  Markdown notes write the preamble on one line;
`%`/`#` comment notes WRAP it across lines with the marker repeated, so a
whitespace-flattening search that is blind to the comment marker sees only the
markdown ones.  That exact blind spot under-counted this defect 109 -> 62 during
review (both the implementing lane and a verifying lane hit it), which is why the
scanner below normalises the comment marker BEFORE matching, and why the
`marker_blindness_probe` pins the failure mode as a live regression.

WHAT IT IS NOT
--------------
Not an opinion about which convention is right.  Whether R40 notes should print
markup-reduced quotes under a weak label, or regenerate byte-exact quotes from
file bytes under a strong one, is a CONVENTION question routed to Grant.  This
check enforces only that a note does not claim MORE than its engines verified,
and that it claims the SAME thing throughout.  Under a future ruling that
regenerates quotes byte-exact, `STRONG` becomes legal and this module's
expectation flips in ONE place (`ALLOW_STRONG`), deliberately.

USAGE
-----
    python research/drivers/r40_quote_claim_strength_number_check.py
    python research/drivers/r40_quote_claim_strength_number_check.py --mutation-receipt
"""
from __future__ import annotations

import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#: Flip to True only under a ruling that regenerates quotes byte-exact from file bytes.
ALLOW_STRONG = False

#: A note is identified by its generated header, in either carrier.
NOTE_MARK = re.compile(
    r"R40 batch-2a — NEEDS-RE-DERIVATION status note"
    r"|R40 batch-2a --- NEEDS-RE-DERIVATION status note"
)

#: The preamble sentence, in EITHER strength, AFTER comment-marker normalisation.
PREAMBLE = re.compile(r"Corpus text quoted (?:below|in the notes) is (.{0,120}?); it is never reworded"
                      r"|Corpus text quoted (?:below|in the notes) is byte-exact and is never reworded")

#: A generated row label, in either carrier and either strength.
ROW_LABEL = re.compile(r"Quoted claim[^\n]{0,120}?:|QUOTE \([^)]{0,120}?\):")

#: STRONG = claims byte-identity with the cited artifact.  Deliberately narrow: it
#: must not fire on "byte-identical to the bank", which is a true and different claim.
STRONG = re.compile(
    r"byte-exact at HEAD|byte-exact and is never reworded|byte-exact at the cited line\b"
    r"|byte-identical at HEAD|verbatim at HEAD",
    re.I,
)
#: WEAK = claims content presence under markup reduction.
WEAK = re.compile(r"content[- ]verified at HEAD", re.I)


def strip_comment_markers(text: str) -> str:
    """Join `%`/`#` comment continuations so a wrapped sentence matches as one string.

    THIS IS THE LOAD-BEARING LINE OF THE MODULE.  Without it the scan sees 62 of
    109 preambles and reads clean — the precise under-count that let level 3 ship,
    and that a verifying lane hit independently.
    """
    return re.sub(r"\n[ \t]*[%#][ \t]*", " ", text)


def flatten(text: str) -> str:
    """Collapse ALL wrapping — both carriers wrap their preamble, markdown across
    plain newlines and `%`/`#` notes across marker-prefixed ones."""
    return re.sub(r"\s+", " ", strip_comment_markers(text))


def claims_in(text: str):
    """(preamble_strength, row_label_strengths) for one note-bearing document."""
    flat = flatten(text)
    pre = []
    for m in PREAMBLE.finditer(flat):
        seg = m.group(0)
        pre.append("STRONG" if STRONG.search(seg) else ("WEAK" if WEAK.search(seg) else "UNKNOWN"))
    rows = []
    for m in ROW_LABEL.finditer(flat):
        seg = m.group(0)
        rows.append("STRONG" if STRONG.search(seg) else ("WEAK" if WEAK.search(seg) else "UNKNOWN"))
    return pre, rows


def violations_in(path: str, text: str):
    out = []
    if not NOTE_MARK.search(flatten(text)):
        return out
    pre, rows = claims_in(text)
    if not ALLOW_STRONG:
        if "STRONG" in pre:
            out.append((path, "PREAMBLE makes a STRONG (byte-identity) claim the engines cannot support"))
        if "STRONG" in rows:
            out.append((path, "a ROW LABEL makes a STRONG (byte-identity) claim the engines cannot support"))
    levels = set(pre) | set(rows)
    if len({l for l in levels if l != "UNKNOWN"}) > 1:
        out.append((path, f"preamble and row labels DISAGREE in strength: preamble={sorted(set(pre))} "
                          f"rows={sorted(set(rows))}"))
    return out


#: SELF-EXCLUSION, declared.  The checker modules carry BOTH the compliant and the
#: violating shapes as fixtures, so scanning them would make every checker flag
#: itself — the self-referential-gate failure class.  Excluding them is safe here
#: and the reason is measurable: all 109 R40-B2a notes live under `manuscript/` and
#: `src/ave/`, and ZERO live under `research/drivers/`.  If a future batch ever
#: appends a note to a driver, this exclusion becomes a real blind spot and must be
#: narrowed to the fixture constants rather than the file.
SELF_EXCLUDE = re.compile(r"^research/drivers/.*_number_check\.py$")


def corpus_files():
    out = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in {".git", ".venv", "__pycache__", "node_modules"}]
        for fn in files:
            if os.path.splitext(fn)[1] in {".md", ".tex", ".py"}:
                rel = os.path.relpath(os.path.join(root, fn), REPO)
                if not SELF_EXCLUDE.match(rel):
                    out.append(rel)
    return sorted(out)


def scan():
    n_notes = n_pre_md = n_pre_cm = 0
    viol = []
    for rel in corpus_files():
        try:
            text = open(os.path.join(REPO, rel), encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            continue
        if not NOTE_MARK.search(flatten(text)):
            continue
        n_notes += 1
        # count the preamble per carrier, to keep BOTH forms visible in the receipt
        # carrier split: a markdown preamble matches once ordinary wrapping is
        # collapsed; a comment-form one needs the `%`/`#` markers stripped first.
        if PREAMBLE.search(re.sub(r"\s+", " ", text)):
            n_pre_md += 1
        elif PREAMBLE.search(flatten(text)):
            n_pre_cm += 1
        viol += violations_in(rel, text)
    return n_notes, n_pre_md, n_pre_cm, viol


# ------------------------------------------------------------------ fixtures

_MD_WEAK = """## R40 batch-2a — NEEDS-RE-DERIVATION status note (2026-08-11)
speed**. Corpus text quoted below is reproduced from the banked audit and is
**content-verified at HEAD (markup-reduced, not byte-identical)**; it is never reworded.

- **`:12`** — stamped at `:12`.
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
"""

#: The shipped level-3 defect: preamble STRONG, rows WEAK.  MUST FIRE.
_MD_DRIFT = _MD_WEAK.replace(
    "reproduced from the banked audit and is\n**content-verified at HEAD (markup-reduced, not byte-identical)**; it is never reworded.",
    "byte-exact and is never reworded.")

#: The same drift in COMMENT form, wrapped exactly as the generator wraps it.
#: A marker-blind scanner sees nothing here — that is the point.
_CM_DRIFT = """% R40 batch-2a --- NEEDS-RE-DERIVATION status note (2026-08-11)
% of propagation delay / finite propagation speed. Corpus text quoted below is byte-exact and is
% never reworded.
%
%   :12  family: probe
%       QUOTE (content verified at HEAD; markup-reduced from the banked audit): a probe quote
"""

_CM_WEAK = """% R40 batch-2a --- NEEDS-RE-DERIVATION status note (2026-08-11)
% of propagation delay / finite propagation speed. Corpus text quoted below is reproduced
% from the banked audit and is CONTENT-VERIFIED AT HEAD (markup-reduced, not byte-identical);
% it is never reworded.
%
%   :12  family: probe
%       QUOTE (content verified at HEAD; markup-reduced from the banked audit): a probe quote
"""


def marker_blindness_probe():
    """Pin the under-count as a live regression: a marker-BLIND scan must miss the
    comment-form drift that the marker-AWARE scan catches."""
    blind = re.sub(r"\s+", " ", _CM_DRIFT)          # flattens whitespace, keeps `%`
    seen_blind = bool(re.search(
        r"Corpus text quoted below is byte-exact and is never reworded", blind))
    seen_aware = bool(re.search(
        r"Corpus text quoted below is byte-exact and is never reworded",
        strip_comment_markers(_CM_DRIFT)))
    return (not seen_blind) and seen_aware


def run_gate(verbose=True):
    ok = True

    def say(good, label, detail):
        nonlocal ok
        ok = ok and good
        if verbose:
            print(f"  [{'PASS' if good else 'FAIL'}] {label}: {detail}")

    v = violations_in("<synthetic-md-drift>", _MD_DRIFT)
    say(bool(v), "can-it-fire — markdown note, preamble STRONG / rows WEAK",
        f"{len(v)} flagged" + (f" ({v[0][1]})" if v else " — THE CHECK IS DEAD"))
    v = violations_in("<synthetic-comment-drift>", _CM_DRIFT)
    say(bool(v), "can-it-fire — COMMENT-FORM note (the wrapped, marker-prefixed carrier)",
        f"{len(v)} flagged" + (f" ({v[0][1]})" if v else " — the marker blind spot is BACK"))
    say(not violations_in("<synthetic-md-weak>", _MD_WEAK),
        "negative control — markdown note, both WEAK", "0 flagged")
    say(not violations_in("<synthetic-comment-weak>", _CM_WEAK),
        "negative control — comment note, both WEAK", "0 flagged")
    say(marker_blindness_probe(),
        "marker-blindness regression (a flattening scan blind to `%`/`#` MISSES it)",
        "blind scan misses, marker-aware scan catches — the 109->62 under-count is pinned")

    n_notes, n_md, n_cm, viol = scan()
    say(n_notes > 0, "notes found in the corpus (an empty scan is not a clean scan)",
        f"{n_notes} note-bearing file(s)")
    say(n_md + n_cm == n_notes,
        "every note's preamble is seen in ONE of the two carriers",
        f"markdown-form {n_md} + comment-form {n_cm} = {n_md + n_cm} of {n_notes}")
    say(not viol, "no note over-claims, and no note's preamble and row labels disagree",
        f"{len(viol)} violation(s)" + ("" if not viol else ": "
        + "; ".join(f"{p} ({w})" for p, w in viol[:6])))
    return ok


def mutation_receipt():
    print("[r40-strength] MUTATION RECEIPT — perturbations must trip; probes must hold")
    results = []
    # M1 — disable comment-marker normalisation: the comment-form drift must go unseen.
    # NB: this rebinds `strip_comment_markers`, which is what `flatten()` actually calls.
    # The first cut of this probe rebound the back-compat ALIAS instead and therefore
    # perturbed nothing while reporting a pass — a mutation probe that cannot reach the
    # code path is exactly the false receipt this module exists to prevent, so the miss
    # is recorded here rather than silently repaired.
    global strip_comment_markers
    saved = strip_comment_markers
    strip_comment_markers = lambda t: t           # noqa: E731
    results.append(("M1 disable comment-marker normalisation (comment drift must go BLIND)",
                    not violations_in("x", _CM_DRIFT)))
    strip_comment_markers = saved
    # M2 — blind the STRONG vocabulary: the markdown drift must stop firing.
    global STRONG
    saved_s = STRONG
    STRONG = re.compile(r"ZZZZ-NEVER-MATCHES")
    results.append(("M2 blind the STRONG vocabulary", not violations_in("x", _MD_DRIFT)))
    STRONG = saved_s
    # M3 — the note marker gates the scan: text without it is never judged.
    results.append(("M3 a document with no note header is not judged",
                    not violations_in("x", _MD_DRIFT.replace(
                        "R40 batch-2a — NEEDS-RE-DERIVATION status note", "unrelated prose"))))
    # M4 — ALLOW_STRONG flips the expectation in exactly one place (the convention hook),
    # and even then a preamble/row DISAGREEMENT must still fire.
    global ALLOW_STRONG
    ALLOW_STRONG = True
    still = violations_in("x", _MD_DRIFT)
    ALLOW_STRONG = False
    results.append(("M4 under ALLOW_STRONG the over-claim is legal but the DISAGREEMENT still fires",
                    bool(still) and all("DISAGREE" in w for _, w in still)))
    allgood = True
    for label, tripped in results:
        print(f"  [{'OK' if tripped else 'BROKEN'}] {label} -> "
              f"{'probe holds (good)' if tripped else 'probe FAILS (BAD)'}")
        allgood = allgood and tripped
    if not allgood:
        print("[r40-strength] MUTATION RECEIPT FAILED")
        return 1
    print("[r40-strength] MUTATION RECEIPT OK: every perturbation trips and every probe holds.")
    return 0


def main():
    if "--mutation-receipt" in sys.argv:
        return mutation_receipt()
    print("[r40-strength] R40 quote-claim strength check (preamble and row labels may not diverge)")
    ok = run_gate()
    if not ok:
        print("[r40-strength] FAILED")
        return 1
    print("[r40-strength] OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
