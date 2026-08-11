#!/usr/bin/env python3
"""R40 preserved-span detector — the R39 byte-fence guard, as CODE.

WHY THIS FILE EXISTS
--------------------
The R40 batch-1 demotion sweep stamps a status marker on live-canon lines.  R39
(`_orchestration/docket-entries/2026-08-09-ruling-r39-sixtags.md`) rules that Rule-12
PRESERVED SPANS are byte-fenced against ALL later passes, mechanical included, and that
their findings live in ledgers, not in-span.  A sweep therefore needs a detector that
answers: *is this stamped line inside a preserved span?*

Batch 1's first cut used a `+-25-line banner-prose window` and MISSED
`manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex:208` — a stamp inside the
Rule-12 preserved Q1-REVERT warningbox whose preservation declaration sits **32 lines below**
the stamp, at the box's closing paragraph.  A window cannot see that.  The replacement is
CONTAINER-AWARE.  This module is that detector, its batch-1 fixture numbers, and a committed
regression case proving it FIRES on the known breach.

WHAT IT IS NOT
--------------
Not an adjudicator.  It FLAGS candidates; every flag is hand-read.  Most flags are false
positives by construction (see the batch-1 record §2.1 for the adjudicated classes) — a
detector that only fired on true breaches would be tuned to the answer.

THE THREE AXES
--------------
(A) CONTAINERS, not windows.  For `.tex`: every `\\begin{X}` .. `\\end{X}` span enclosing the
    line, with **no environment allow-list**, PLUS **LaTeX sectioning containers**
    (`\\chapter` / `\\section` / `\\subsection` / `\\subsubsection` / `\\paragraph`), a span
    running to the next sectioning command of the same-or-higher level.  For `.md`: the
    enclosing blockquote run, the enclosing `^#{1,6}` section, the enclosing bullet block.
    For `.py`: the module docstring, the contiguous comment run, the enclosing `def`/`class`.
(B) The WHOLE container is scanned, at any distance.
(C) A widened DECLARATION VOCABULARY (`PRESERVE`).

SPEC EXTENSION 1 (2026-08-11, forced by an adversarial probe) — LaTeX SECTIONING.
    Without it the detector is blind wherever a Rule-12 banner governs prose that sits inside
    NO `\\begin{}` environment.  That shape is LIVE in the corpus at
    `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:288`: a `%` Rule-12
    banner governing the prose below it, inside `\\subsection` (:287) and inside no environment
    at all — the environment map around it jumps `\\end{resultbox}`@:273 -> `\\begin{figure}`@:299.
    `SECTIONING_PROBE` below pins that site as a live regression.

SPEC EXTENSION 2 (2026-08-11, same probe) — the bare `Rule 12:` QUOTE-AND-DATE form.
    A real declaration form that carries NO `preserv`/`verbatim` token, e.g.
    `*(2026-06-08 c_L reconciliation, Rule 12: the prior wording quoted ...)*`.  Live at
    `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md:43`,
    `.../lc-electrodynamics.md:28`, `src/ave/core/sonic_horizon_flow.py:6`, and
    `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/unified-engine-design-doctrine.md:353`.
    All are FALSE POSITIVES on hand-read, but the FORM is a real marker the scan could not see.

RESIDUAL BLIND SPOTS — DECLARED, NOT COVERED
--------------------------------------------
This detector does NOT cover, and a future pass must not read its clean run as completeness:
  * `\\begingroup` .. `\\endgroup` (and `{` .. `}` brace groups) — a TeX grouping that is
    neither a `\\begin{}` environment nor a sectioning command; a banner inside one is invisible.
  * Markdown PRE-HEADING front matter — a declaration in an HTML comment (`<!-- ... -->`) or in
    kb-frontmatter above the first `#` heading is only seen if the stamp shares that section.
  * Python MODULE-LEVEL declarations held in a sibling STRING CONSTANT (not the module
    docstring, not a `#` comment run) — e.g. `_PRESERVED_NOTE = \"\"\"... Rule 12 ...\"\"\"`.
  * Cross-FILE governance: a declaration in file A naming a span in file B.
Of the four out-of-list probe shapes raised at review, exactly ONE (LaTeX sectioning) is fixed
here; the other three are the blind spots above and are left uncovered ON PURPOSE, declared
rather than silently implied away.

USAGE
-----
    python research/drivers/r40_preserved_span_number_check.py                # gate (exit 0/1)
    python research/drivers/r40_preserved_span_number_check.py --mutation-receipt
    python research/drivers/r40_preserved_span_number_check.py --report       # human scan dump
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FIXTURE = os.path.join(
    REPO, "research/drivers/fixtures/r40b1_span_regression_08gw_28ee7a23.tex"
)

STAMP = re.compile(r"DEMOTED 2026-08-11|TAG DEMOTED 2026-08-11")

#: The declaration vocabulary.  Group 2 is SPEC EXTENSION 2.
PRESERVE = re.compile(
    # --- original vocabulary -------------------------------------------------
    r"preserved\s+verbatim|PRESERVED\s+VERBATIM|preserved\s+per\s+Rule|per\s+Rule[\s~]*12"
    r"|Rule[-~\s]?12\s+(?:preserv|walk-back|quote|KEEP)|is\s+preserved|are\s+preserved"
    r"|box\s+is\s+preserved|boxes\s+are\s+preserved|preserved\s+(?:above|below|here|unchanged)"
    r"|byte-fence|byte-fenced|quoted\s+verbatim\s+and\s+not\s+paraphrased|verbatim\s*\[sic\]"
    r"|do\s+NOT\s+delete|prior\s+(?:entry\s+text|wording|cell|value|edge|version)\s+.*preserv"
    r"|SUPERSEDED.*preserv|PRESERVED\b|KEEP-BOTH"
    # --- SPEC EXTENSION 2: the bare `Rule 12:` quote-and-date form -----------
    r"|Rule[-~\s]?12\s*\)?\s*:",
    re.I,
)

TEXENV = re.compile(r"\\(begin|end)\{([A-Za-z*]+)\}")
#: SPEC EXTENSION 1 — sectioning levels, outermost first.
SECTIONING = [
    ("chapter", re.compile(r"^\s*\\chapter\*?\{")),
    ("section", re.compile(r"^\s*\\section\*?\{")),
    ("subsection", re.compile(r"^\s*\\subsection\*?\{")),
    ("subsubsection", re.compile(r"^\s*\\subsubsection\*?\{")),
    ("paragraph", re.compile(r"^\s*\\paragraph\*?\{")),
]

#: Live corpus site pinning SPEC EXTENSION 1 (a `%` Rule-12 banner inside a
#: sectioning container and inside NO environment).
SECTIONING_PROBE = (
    "manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex",
    288,
)

# --------------------------------------------------------------------------- containers


def tex_containers(lines, ln):
    """Environment spans (no allow-list) + sectioning spans (EXTENSION 1) enclosing `ln`."""
    stack, spans = [], []
    for i, l in enumerate(lines, 1):
        for m in TEXENV.finditer(l):
            if m.group(1) == "begin":
                stack.append((m.group(2), i))
            else:
                for k in range(len(stack) - 1, -1, -1):
                    if stack[k][0] == m.group(2):
                        spans.append((f"env:{stack[k][0]}", stack[k][1], i))
                        stack.pop(k)
                        break
    out = [s for s in spans if s[1] <= ln <= s[2]]
    out += _sectioning_containers(lines, ln)
    return out


def _sectioning_containers(lines, ln, levels=None):
    """A sectioning command opens a span closed by the next same-or-higher-level command."""
    levels = SECTIONING if levels is None else levels
    marks = []
    for i, l in enumerate(lines, 1):
        for depth, (name, rx) in enumerate(levels):
            if rx.match(l):
                marks.append((i, depth, name))
                break
    out = []
    for idx, (start, depth, name) in enumerate(marks):
        end = len(lines)
        for j in range(idx + 1, len(marks)):
            if marks[j][1] <= depth:
                end = marks[j][0] - 1
                break
        if start <= ln <= end:
            out.append((f"sec:{name}", start, end))
    return out


def md_containers(lines, ln):
    out = []
    if lines[ln - 1].lstrip().startswith(">"):
        a = ln
        while a > 1 and lines[a - 2].lstrip().startswith(">"):
            a -= 1
        b = ln
        while b < len(lines) and lines[b].lstrip().startswith(">"):
            b += 1
        out.append(("blockquote", a, b))
    a = 1
    for i in range(ln, 0, -1):
        if re.match(r"^#{1,6} ", lines[i - 1]):
            a = i
            break
    b = len(lines)
    for i in range(ln + 1, len(lines) + 1):
        if re.match(r"^#{1,6} ", lines[i - 1]):
            b = i - 1
            break
    out.append(("section", a, b))
    a2 = ln
    while a2 > 1 and lines[a2 - 1].strip() and not re.match(r"^\s*[-*] ", lines[a2 - 1]):
        a2 -= 1
    b2 = ln
    while b2 < len(lines) and lines[b2].strip():
        b2 += 1
    out.append(("block", a2, b2))
    return out


def py_containers(lines, ln):
    out = []
    if lines and lines[0].startswith(('"""', "'''")):
        q = lines[0][:3]
        for i in range(1, len(lines)):
            if q in lines[i]:
                out.append(("module-docstring", 1, i + 1))
                break
    if lines[ln - 1].lstrip().startswith("#"):
        a = ln
        while a > 1 and lines[a - 2].lstrip().startswith("#"):
            a -= 1
        b = ln
        while b < len(lines) and lines[b].lstrip().startswith("#"):
            b += 1
        out.append(("comment-run", a, b))
    for i in range(ln, 0, -1):
        m = re.match(r"^(\s*)(def|class)\s+(\w+)", lines[i - 1])
        if m:
            ind = len(m.group(1))
            b = len(lines)
            for j in range(i + 1, len(lines) + 1):
                m2 = re.match(r"^(\s*)(def|class)\s", lines[j - 1])
                if m2 and len(m2.group(1)) <= ind:
                    b = j - 1
                    break
            out.append((f"{m.group(2)} {m.group(3)}", i, b))
            break
    return out


def containers_for(path, lines, ln):
    if path.endswith(".tex"):
        return tex_containers(lines, ln)
    if path.endswith(".py"):
        return py_containers(lines, ln)
    return md_containers(lines, ln)


def flags_for(path, lines, ln, preserve=PRESERVE):
    """Every (container, declaration-line) pair that would fence `ln`."""
    hits = []
    for name, a, b in containers_for(path, lines, ln):
        for i in range(a, min(b, len(lines)) + 1):
            if i != ln and preserve.search(lines[i - 1]):
                hits.append((name, a, b, i))
    return hits


# --------------------------------------------------------------------------- scan


def corpus_files():
    """The R40-B1 corpus surface: files this branch changed under manuscript/ + src/."""
    out = subprocess.run(
        ["git", "-C", REPO, "diff", "--name-only", "origin/main", "HEAD"],
        capture_output=True, text=True).stdout.split()
    return [f for f in out
            if (f.startswith("manuscript/") or f.startswith("src/"))
            and not f.startswith("manuscript/ave-kb/.index/")]


def scan(files, preserve=PRESERVE, live_only=True):
    """Scan stamped LIVE-CANON lines (above each file's origin/main EOF) for fencing."""
    n_scanned, flagged = 0, []
    for f in files:
        full = os.path.join(REPO, f)
        if not os.path.isfile(full):
            continue
        lines = open(full, encoding="utf-8").read().split("\n")
        norig = len(lines)
        if live_only:
            old = subprocess.run(["git", "-C", REPO, "show", f"origin/main:{f}"],
                                 capture_output=True, text=True).stdout.split("\n")
            if old and old[-1] == "":
                old = old[:-1]
            norig = len(old)
        for ln, l in enumerate(lines, 1):
            if ln > norig or not STAMP.search(l):
                continue
            n_scanned += 1
            hits = flags_for(f, lines, ln, preserve)
            if hits:
                flagged.append((f, ln, hits))
    return n_scanned, flagged


#: BATCH-1 FIXTURE.  Banked at the fix-pass tip; a change here is a real signal, not noise.
#: `pre_fix` is the same scan at 28ee7a23 (the breach still live) and is asserted by the
#: committed regression fixture rather than by re-checking out that commit.
FIXTURE_NUMBERS = {
    # Post-fix, POST-EXTENSION (this module as shipped).
    "post_fix_scanned": 60,
    "post_fix_flagged": 24,
    "post_fix_breaches": 0,
    # Post-fix, PRE-EXTENSION (the batch-1 record §2.1 scan, both extensions off) — kept so the
    # extensions' cost is auditable: they add 9 flags, ALL hand-adjudicated FALSE POSITIVE.
    "post_fix_flagged_pre_extension": 15,
    "extension_added_flags": 9,
    "extension_added_breaches": 0,
    # Pre-fix (28ee7a23), pre-extension: the state the committed regression fixture pins.
    "pre_fix_scanned": 61,
    "pre_fix_flagged_pre_extension": 16,
    "pre_fix_breaches": 1,
    "adjudicated_breach": "manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex:208",
}


def regression_fires_on_known_breach():
    """THE CAN-IT-FIRE PROOF.  Against the committed pre-fix export, the detector MUST flag
    the stamped line, and the flagging container MUST be the preserved warningbox."""
    lines = open(FIXTURE, encoding="utf-8").read().split("\n")
    stamped = [i for i, l in enumerate(lines, 1) if STAMP.search(l)]
    if len(stamped) != 1:
        return False, f"fixture must carry exactly one stamp, found {len(stamped)}"
    ln = stamped[0]
    hits = flags_for(FIXTURE, lines, ln)
    boxes = [h for h in hits if h[0] == "env:warningbox"]
    if not boxes:
        return False, f"detector did NOT fire on the known breach at fixture line {ln}"
    name, a, b, decl = boxes[0]
    if not (a < ln < b):
        return False, "stamp is not strictly inside the warningbox span"
    return True, f"fires at fixture:{ln} inside [{name} {a}-{b}] via declaration at :{decl}"


def sectioning_probe_covered():
    """SPEC EXTENSION 1 regression: the live probe-A site must resolve to a sectioning
    container AND to no environment container."""
    path, ln = SECTIONING_PROBE
    full = os.path.join(REPO, path)
    if not os.path.isfile(full):
        return False, f"probe file missing: {path}"
    lines = open(full, encoding="utf-8").read().split("\n")
    cs = containers_for(path, lines, ln)
    secs = [c for c in cs if c[0].startswith("sec:")]
    envs = [c for c in cs if c[0].startswith("env:")]
    if not secs:
        return False, f"{path}:{ln} resolved to NO sectioning container (extension 1 dead)"
    # The load-bearing container is the INNERMOST one: the \subsection the banner sits under.
    subs = [c for c in secs if c[0] == "sec:subsection"]
    if not subs:
        return False, f"{path}:{ln} has no \\subsection container — probe shape changed"
    if envs:
        return False, f"{path}:{ln} unexpectedly sits inside {envs} — probe shape changed"
    if not PRESERVE.search(lines[ln - 1]):
        return False, f"{path}:{ln} no longer carries a Rule-12 banner — probe shape changed"
    return True, (f"{path}:{ln} covered by {subs[0]} (innermost) among {len(secs)} "
                  f"sectioning container(s), in no environment")


def bare_rule12_form_seen():
    """SPEC EXTENSION 2 regression: the bare `Rule 12:` form must be matched, and must NOT
    have been matchable by the pre-extension vocabulary."""
    sample = "> *(2026-06-08 c_L reconciliation, Rule 12: the prior wording quoted the pure ...)*"
    old = re.compile(PRESERVE.pattern.rsplit("|Rule[-~\\s]?12\\s*\\)?\\s*:", 1)[0], re.I)
    if old.search(sample):
        return False, "the pre-extension vocabulary already matched — extension 2 is a no-op"
    if not PRESERVE.search(sample):
        return False, "extension 2 does not match its own live form"
    return True, "bare `Rule 12:` quote-and-date form matched, and was NOT matched before"


def run_gate(verbose=True):
    ok = True

    def say(good, label, detail):
        nonlocal ok
        ok = ok and good
        if verbose:
            print(f"  [{'PASS' if good else 'FAIL'}] {label}: {detail}")

    good, detail = regression_fires_on_known_breach()
    say(good, "regression / can-it-fire on the known breach", detail)
    good, detail = sectioning_probe_covered()
    say(good, "spec extension 1 (LaTeX sectioning)", detail)
    good, detail = bare_rule12_form_seen()
    say(good, "spec extension 2 (bare `Rule 12:` form)", detail)

    n, flagged = scan(corpus_files())
    say(n == FIXTURE_NUMBERS["post_fix_scanned"],
        "stamped live-canon lines scanned",
        f"{n} (fixture {FIXTURE_NUMBERS['post_fix_scanned']})")
    say(len(flagged) == FIXTURE_NUMBERS["post_fix_flagged"],
        "flagged for hand-adjudication",
        f"{len(flagged)} (fixture {FIXTURE_NUMBERS['post_fix_flagged']}; "
        f"{FIXTURE_NUMBERS['post_fix_flagged_pre_extension']} pre-extension "
        f"+ {FIXTURE_NUMBERS['extension_added_flags']} added by the extensions, all adjudicated FP)")
    breach = [f"{f}:{ln}" for f, ln, _ in flagged
              if f == "manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex"
              and ln == 208]
    say(not breach, "the adjudicated breach stays reversed",
        f"{FIXTURE_NUMBERS['adjudicated_breach']} absent from the live scan"
        if not breach else f"RE-APPEARED: {breach}")
    return ok, n, flagged


def mutation_receipt():
    """Every perturbation of the detector's own load-bearing structure must trip the gate."""
    print("[r40-span] MUTATION RECEIPT — each perturbation must FAIL the checker")
    results = []

    # M1 — drop SPEC EXTENSION 1 (sectioning containers).
    saved = list(SECTIONING)
    SECTIONING.clear()
    good, _ = sectioning_probe_covered()
    results.append(("M1 drop LaTeX-sectioning containers", not good))
    SECTIONING.extend(saved)

    # M2 — drop SPEC EXTENSION 2 (the bare `Rule 12:` form).
    old_vocab = re.compile(PRESERVE.pattern.rsplit("|Rule[-~\\s]?12\\s*\\)?\\s*:", 1)[0], re.I)
    sample = "> *(2026-06-08 c_L reconciliation, Rule 12: the prior wording quoted ...)*"
    results.append(("M2 drop the bare `Rule 12:` vocabulary", not old_vocab.search(sample)))

    # M3 — neutralise EVERY declaration form in the fixture (the detector's own vocabulary is
    # used as the eraser, so no form can survive by omission): the regression must stop firing.
    # NOTE: the fixture carries FOUR distinct declaration forms, and the box is fenced by the
    # EARLIEST of them (`verbatim [sic]` at fixture:32), not by the `preserved verbatim` at :69 —
    # erasing only the obvious one leaves the flag standing, which is exactly what this mutation
    # is here to catch.
    lines = open(FIXTURE, encoding="utf-8").read().split("\n")
    mutated = [PRESERVE.sub("XXXXXXX", l) for l in lines]
    stamped = [i for i, l in enumerate(mutated, 1) if STAMP.search(l)]
    still = flags_for(FIXTURE, mutated, stamped[0]) if stamped else []
    results.append(("M3 neutralise every fixture declaration", not still))

    # M4 — move the fixture stamp OUT of the warningbox: the regression must stop firing.
    moved = list(lines)
    si = [i for i, l in enumerate(moved, 1) if STAMP.search(l)][0]
    ei = [i for i, l in enumerate(moved, 1) if "\\end{warningbox}" in l][0]
    moved[si - 1] = moved[si - 1].replace(
        " \\textbf{[DEMOTED 2026-08-11 --- R40-B1; dated demotion note at the end of this chapter]}", "")
    moved.insert(ei, "Outside the box. \\textbf{[DEMOTED 2026-08-11 --- R40-B1; moved by M4]}")
    st = [i for i, l in enumerate(moved, 1) if STAMP.search(l)][0]
    out_hits = [h for h in flags_for(FIXTURE, moved, st) if h[0] == "env:warningbox"]
    results.append(("M4 move the stamp outside the box", not out_hits))

    allgood = True
    for label, tripped in results:
        print(f"  [{'OK' if tripped else 'BROKEN'}] {label} -> "
              f"{'checker FAILS (good)' if tripped else 'checker still passes (BAD)'}")
        allgood = allgood and tripped
    if not allgood:
        print("[r40-span] MUTATION RECEIPT FAILED — a perturbed detector still reports clean.")
        return 1
    print("[r40-span] MUTATION RECEIPT OK: every perturbation trips the checker.")
    return 0


def main():
    if "--mutation-receipt" in sys.argv:
        return mutation_receipt()
    print("[r40-span] R40 preserved-span detector (R39 byte-fence guard)")
    ok, n, flagged = run_gate()
    if "--report" in sys.argv:
        print(f"\n  scan dump — {n} stamped live-canon lines, {len(flagged)} flagged:")
        for f, ln, hits in flagged:
            seen = set()
            print(f"    {f}:{ln}")
            for name, a, b, decl in hits:
                if (name, a, b) in seen:
                    continue
                seen.add((name, a, b))
                print(f"        [{name} {a}-{b}] declaration at :{decl}")
    if not ok:
        print("[r40-span] FAILED")
        return 1
    print(f"[r40-span] OK — {n} stamped lines, {len(flagged)} flagged, 0 breaches; "
          "regression fires on the known breach; both spec extensions live.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
