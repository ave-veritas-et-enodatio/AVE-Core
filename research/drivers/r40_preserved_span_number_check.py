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

REPAIR (2026-08-11, post-merge) — THE SCAN SURFACE IS PINNED
------------------------------------------------------------
The first cut computed its 60/24 fixture numbers from `git diff origin/main HEAD` — a
branch-relative surface that reproduced them ONLY on the batch-1 branch itself.  The
moment #950 merged, that diff was empty on main (0 scanned vs fixture 60) and had a
different shape on every later branch: the gate hard-failed everywhere, blocking all
CI.  A gate whose fixture encodes its own branch's diff shape is the self-referential
twin of the gate-consuming-self-declared-fields class.  The repair splits the two jobs
the one scan was conflating:
  * The FIXTURE numbers are a property of the batch-1 merge commit (`BATCH1_MERGE`)
    and are re-derived from it, pinned, every run — stable on main and on any branch.
  * The CURRENT branch gets a LIVE FORWARD GUARD instead: any stamped line the branch
    ADDED (a `+` line of `origin/main..HEAD`, unified-0 hunks) landing inside a
    preserved container fails loudly and demands hand-adjudication.  (Second repair,
    same day, forced by the independent verify: the first cut derived the guard's
    surface from a line-number-vs-old-EOF proxy, which was inverted on BOTH sides —
    it re-flagged batch-1's landed, already-adjudicated stamps whenever a later
    branch touched one of their 19 files, and it was blind to stamps in NEW files,
    whose every line sat past the proxy's boundary.  The added-line set closes both:
    pre-existing stamps are not in it; a new file's lines all are.)  An adjudicated
    false positive is registered in `GUARD_ADJUDICATED_FP` with its reading.

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
  * The CONTAINER ARRIVING AFTER THE STAMP (forward guard only; 2026-08-11 delta
    re-verify N2): a branch that adds a preservation declaration AROUND an unchanged
    pre-existing stamped line creates a genuine fencing relationship the added-line
    guard cannot see — the stamp is not an added line.  The round-1 EOF-proxy guard
    would have caught this shape; narrowing to added lines traded it away, and the
    trade is declared here rather than silently implied away.
  * PATHS THE HEADER PARSER CANNOT EXTRACT (forward guard only; 2026-08-11 delta
    re-verify H1/H2): a path containing a space mis-keys under the greedy ` b/`
    split, and a git c-quoted path (non-ASCII, quotes, backslash) leaves the
    header unmatched — attribution is invalidated, never inherited.  Both fail
    OPEN (added lines under-scanned, never falsely flagged); 0 of 5165 tracked
    paths carry either shape today.
Of the four out-of-list probe shapes raised at the batch-1 review, exactly ONE (LaTeX
sectioning) was fixed then; the first four bullets above are that review's residue, and
the last two were added at the 2026-08-11 delta re-verifies.  All are left uncovered ON
PURPOSE, declared rather than silently implied away.

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


def corpus_files(base="origin/main", head="HEAD"):
    """The R40-B1 corpus surface: files changed base..head under manuscript/ + src/."""
    out = subprocess.run(
        ["git", "-C", REPO, "diff", "--name-only", base, head],
        capture_output=True, text=True).stdout.split()
    return [f for f in out
            if (f.startswith("manuscript/") or f.startswith("src/"))
            and not f.startswith("manuscript/ave-kb/.index/")]


def scan(files, preserve=PRESERVE, live_only=True, at_rev=None, old_rev="origin/main"):
    """Scan stamped lines added since `old_rev` (above each file's `old_rev` EOF) for fencing.

    `at_rev=None` reads the WORKING TREE (the live forward guard); a SHA reads that
    commit's blobs (the pinned batch-1 scan).  A file absent at `at_rev` / in the tree
    (a deletion in the diff) is skipped; a wrong `at_rev` yields 0 scanned, which the
    pinned fixture assertion then fails LOUDLY — there is no silent-pass path."""
    n_scanned, flagged = 0, []
    for f in files:
        if at_rev is None:
            full = os.path.join(REPO, f)
            if not os.path.isfile(full):
                continue
            lines = open(full, encoding="utf-8").read().split("\n")
        else:
            shown = subprocess.run(["git", "-C", REPO, "show", f"{at_rev}:{f}"],
                                   capture_output=True, text=True)
            if shown.returncode != 0:
                continue
            lines = shown.stdout.split("\n")
        norig = len(lines)
        if live_only:
            old = subprocess.run(["git", "-C", REPO, "show", f"{old_rev}:{f}"],
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


#: Forward-guard flags hand-adjudicated FALSE POSITIVE, keyed (file, stripped line
#: content — line numbers drift, bytes do not).  Each entry carries its reading as a
#: comment.  Empty until the guard's first real flag is adjudicated.
GUARD_ADJUDICATED_FP: set = set()


def _added_map_from_diff_text(text):
    """{path: head-side added-line set} from a whole unified-0 diff (pure; testable).

    Hunks are attributed to the `b/` path of the preceding `diff --git` header.  A
    pure rename block carries a `rename to` header and ZERO hunks, so it contributes
    nothing — which is the point (see `added_map_for`)."""
    added, cur = {}, None
    for line in text.split("\n"):
        if line.startswith("diff --git "):
            m = re.match(r"^diff --git a/.* b/(.*)$", line)
            # A header the extraction cannot parse (git c-quotes paths with
            # non-ASCII/quotes/backslashes) must INVALIDATE the attribution,
            # never leave the previous file's standing — else the quoted file's
            # hunks would be credited to its neighbor and could FALSE-FLAG it
            # (delta re-verify H2).  Unparseable headers therefore fail OPEN.
            cur = m.group(1) if m else None
            continue
        h = re.match(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@", line)
        if h and cur is not None:
            start = int(h.group(1))
            count = 1 if h.group(2) is None else int(h.group(2))
            added.setdefault(cur, set()).update(range(start, start + count))
    return added


def added_map_for(base="origin/main", head="HEAD"):
    """The branch's full added-line map, from ONE whole-diff invocation.

    Deliberately NO pathspec: a per-file pathspec filters the rename source out
    before git's rename detection runs, so a renamed file reads as brand-new and
    every pre-existing stamped line in it re-flags (probed 2026-08-11, delta
    re-verify N1).  Whole-diff with `-M`, a pure rename is `similarity index 100%`
    with zero hunks, and rename+edit yields exactly the real added lines."""
    out = subprocess.run(
        ["git", "-C", REPO, "diff", "--unified=0", "-M", base, head],
        capture_output=True, text=True).stdout
    return _added_map_from_diff_text(out)


def scan_added(files, base="origin/main", head="HEAD", preserve=PRESERVE,
               added_map=None, read_file=None):
    """THE FORWARD GUARD's scan: stamped lines the branch ADDED, container-checked.

    `added_map`/`read_file` exist so the mutation receipt can drive the decision
    logic in memory; the gate always calls with both None (git + working tree).
    A modified line is a delete+add in unified-0, so in-place stamp edits are
    scanned too; pre-existing (e.g. batch-1) stamps are never in the added set,
    and a pure rename contributes no hunks, so it re-flags nothing."""
    if added_map is None:
        added_map = added_map_for(base, head)
    n_scanned, flagged = 0, []
    for f in files:
        if read_file is None:
            full = os.path.join(REPO, f)
            if not os.path.isfile(full):
                continue
            lines = open(full, encoding="utf-8").read().split("\n")
        else:
            lines = read_file(f)
        add = added_map.get(f, set())
        for ln in sorted(add):
            if ln < 1 or ln > len(lines) or not STAMP.search(lines[ln - 1]):
                continue
            n_scanned += 1
            if (f, lines[ln - 1].strip()) in GUARD_ADJUDICATED_FP:
                continue
            hits = flags_for(f, lines, ln, preserve)
            if hits:
                flagged.append((f, ln, hits))
    return n_scanned, flagged


#: The batch-1 merge commit on main (#950).  The 60/24 numbers below are a property of
#: THIS commit's first-parent diff — NOT of whatever branch happens to run the gate.
#: (2026-08-11 repair: the first cut computed them from `origin/main..HEAD`, which
#: reproduced them only on the batch-1 branch itself; on main, and on every later
#: branch, that diff has a different shape and the gate hard-failed on 0 scanned.)
BATCH1_MERGE = "fcdd1efb001f2039d25122c5d0dd0e0e5ebd26f9"

#: BATCH-1 FIXTURE.  Banked at the fix-pass tip; a change here is a real signal, not noise.
#: `post_fix` numbers are re-derived every run from the PINNED `BATCH1_MERGE` scan.
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

    # --- THE PINNED BATCH-1 SCAN: the fixture numbers, re-derived from BATCH1_MERGE ---
    n, flagged = scan(corpus_files(BATCH1_MERGE + "^1", BATCH1_MERGE),
                      at_rev=BATCH1_MERGE, old_rev=BATCH1_MERGE + "^1")
    say(n == FIXTURE_NUMBERS["post_fix_scanned"],
        "stamped batch-1 lines scanned (pinned to the #950 merge)",
        f"{n} (fixture {FIXTURE_NUMBERS['post_fix_scanned']})")
    say(len(flagged) == FIXTURE_NUMBERS["post_fix_flagged"],
        "flagged for hand-adjudication (pinned batch-1 scan)",
        f"{len(flagged)} (fixture {FIXTURE_NUMBERS['post_fix_flagged']}; "
        f"{FIXTURE_NUMBERS['post_fix_flagged_pre_extension']} pre-extension "
        f"+ {FIXTURE_NUMBERS['extension_added_flags']} added by the extensions, all adjudicated FP)")
    breach = [f"{f}:{ln}" for f, ln, _ in flagged
              if f == "manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex"
              and ln == 208]
    say(not breach, "the adjudicated breach stays reversed",
        f"{FIXTURE_NUMBERS['adjudicated_breach']} absent from the pinned scan"
        if not breach else f"RE-APPEARED: {breach}")
    # --- THE LIVE FORWARD GUARD: stamped lines this branch ADDED (the `+` hunks of
    # origin/main..HEAD) must carry ZERO unadjudicated flags.  Pre-existing stamps —
    # batch-1's landed, adjudicated lines included — are not in the added set and are
    # never re-flagged, no matter which files the branch touches; a NEW file's lines
    # are all added, so a breach in a new file is fully scanned.  A flag demands
    # hand-adjudication; an adjudicated false positive is registered in
    # GUARD_ADJUDICATED_FP with its reading.
    n_live, flagged_live = scan_added(corpus_files())
    say(not flagged_live,
        "live forward guard (stamped lines this branch ADDED)",
        f"{n_live} added stamped line(s) scanned, 0 flagged"
        if not flagged_live else
        f"{n_live} scanned, {len(flagged_live)} FLAGGED — hand-adjudicate each "
        "(then register true FPs in GUARD_ADJUDICATED_FP): "
        + "; ".join(f"{f}:{ln}" for f, ln, _ in flagged_live))
    return ok, n, flagged


def mutation_receipt():
    """Every perturbation of the detector's own load-bearing structure must trip the gate."""
    print("[r40-span] MUTATION RECEIPT — detector perturbations must trip; behavioral probes must hold")
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

    # M5 — pin the batch-1 scan to the WRONG rev (the merge's parent, where the stamps
    # do not exist): the pinned fixture numbers must stop reproducing.
    wrong = BATCH1_MERGE + "^1"
    n5, _ = scan(corpus_files(wrong + "^1", wrong), at_rev=wrong, old_rev=wrong + "^1")
    results.append(("M5 pin the batch-1 scan to the wrong rev",
                    n5 != FIXTURE_NUMBERS["post_fix_scanned"]))

    # M6a — the guard MUST flag a breach in a NEW file: an in-memory .tex whose every
    # line is added (a new file's diff shape), with the stamp inside a declared box.
    # This is the exact probe the first cut's guard failed (it skipped new files).
    breach = ["\\begin{warningbox}",
              "This box is preserved verbatim per Rule~12.",
              "Text. \\textbf{[DEMOTED 2026-08-11 --- probe]}",
              "\\end{warningbox}", ""]
    n6a, fl6a = scan_added(["manuscript/_probe_new_file.tex"],
                           added_map={"manuscript/_probe_new_file.tex":
                                      set(range(1, len(breach) + 1))},
                           read_file=lambda f: list(breach))
    results.append(("M6a guard flags a breach in a NEW file", bool(fl6a)))

    # M6b — the guard MUST NOT flag a pre-existing stamp in a touched file: same
    # content, but the branch's added set does not contain the stamped line (the
    # batch-1 re-flag defect the first cut shipped).
    n6b, fl6b = scan_added(["manuscript/_probe_touched_file.tex"],
                           added_map={"manuscript/_probe_touched_file.tex": {5}},
                           read_file=lambda f: list(breach))
    results.append(("M6b guard ignores a pre-existing stamp in a touched file",
                    not fl6b and n6b == 0))

    # M6c — the whole-diff map parser: per-file hunk attribution, count-omitted-
    # means-1, count-0 (pure deletion) contributes nothing, and a PURE RENAME block
    # (similarity index 100%, no hunks) contributes nothing — the N1 shape.
    parsed = _added_map_from_diff_text(
        "diff --git a/manuscript/x.tex b/manuscript/x.tex\n"
        "@@ -10,2 +12,3 @@ ctx\n@@ -30 +40 @@\n@@ -50,2 +60,0 @@\n"
        "diff --git a/manuscript/old-name.md b/manuscript/new-name.md\n"
        "similarity index 100%\nrename from manuscript/old-name.md\n"
        "rename to manuscript/new-name.md\n"
        "diff --git a/src/y.py b/src/y.py\n@@ -5,0 +6,2 @@\n"
        "diff --git \"a/manuscript/e\\303\\251.tex\" \"b/manuscript/e\\303\\251.tex\"\n"
        "@@ -1,0 +2,2 @@\n")
    results.append(("M6c whole-diff map parser exact (incl. rename-no-hunks)",
                    parsed == {"manuscript/x.tex": {12, 13, 14, 40},
                               "src/y.py": {6, 7}}))

    # M6d — the GUARD_ADJUDICATED_FP registry is narrow: the correct (file, bytes)
    # key suppresses the flag; a wrong-file or wrong-bytes key must NOT.
    stamp_line = breach[2].strip()
    def _fp_probe(key):
        GUARD_ADJUDICATED_FP.add(key)
        try:
            _, fl = scan_added(["manuscript/_probe_new_file.tex"],
                               added_map={"manuscript/_probe_new_file.tex":
                                          set(range(1, len(breach) + 1))},
                               read_file=lambda f: list(breach))
        finally:
            GUARD_ADJUDICATED_FP.discard(key)
        return fl
    ok_key = not _fp_probe(("manuscript/_probe_new_file.tex", stamp_line))
    wrong_file = bool(_fp_probe(("manuscript/other.tex", stamp_line)))
    wrong_bytes = bool(_fp_probe(("manuscript/_probe_new_file.tex", "XXXX")))
    results.append(("M6d FP registry: right key suppresses, wrong file/bytes do not",
                    ok_key and wrong_file and wrong_bytes))

    allgood = True
    for label, tripped in results:
        print(f"  [{'OK' if tripped else 'BROKEN'}] {label} -> "
              f"{'probe holds (good)' if tripped else 'probe FAILS (BAD)'}")
        allgood = allgood and tripped
    if not allgood:
        print("[r40-span] MUTATION RECEIPT FAILED — a probe did not hold (perturbation un-caught or behavior wrong).")
        return 1
    print("[r40-span] MUTATION RECEIPT OK: every perturbation trips and every behavioral probe holds.")
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
    print(f"[r40-span] OK — pinned batch-1 scan: {n} stamped lines, {len(flagged)} flagged, "
          "0 breaches; live forward guard clean; "
          "regression fires on the known breach; both spec extensions live.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
