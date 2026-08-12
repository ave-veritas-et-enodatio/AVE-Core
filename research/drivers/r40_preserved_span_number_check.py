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



# ──────────────────────────────────────────────────────────────────────────
# R40 BATCH-2a FORWARD-GUARD ADJUDICATIONS (2026-08-11).
#
# 58 stamped lines this batch ADDED were flagged by the live forward guard. Every one
# was hand-read against its own declaration BEFORE any registration, and the reading is
# recorded per entry below. TWO of the 58 were GENUINE and are deliberately NOT
# registered: manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-
# equation.md:20 and :26 sit under that file's :40 declaration, verbatim "all notes
# above PRESERVED unedited" (and :36 "bullets above PRESERVED unedited"). Their stamps
# were REMOVED and both rows were routed to the file's EOF ledger with the span byte-
# untouched, per R39. The 56 registered below are hand-adjudicated FALSE POSITIVE.
#
# SCALING CAVEAT, surfaced not fixed. The registry keys on the full stripped line bytes,
# and this batch's flagged lines have a MEDIAN length of ~718 characters (longest
# 12910). 56 keys is therefore ~65 kB of literal blob, which is not hand-auditable by a
# reviewer and re-flags on any re-wrap. The per-site adjudication table in
# _orchestration/2026-08-12_r40-sweep-batch2a.md is the reviewable record; this block is
# the machine half. Re-keying the registry (e.g. on the anchor's claim-quote, or on
# (file, stamp-token, short digest)) is a gate-design change and is ROUTED, not taken
# here.
#
# Class summary of the 56: 3 SELF-MATCH on this batch's own EOF note; 13 declaration
# holds the prior wording INSIDE a %/# comment while the stamped line carries the live
# replacement; 12 KEEP-BOTH matched in SENSE (ii) (both-objects-retained), adjudicated
# per site and never class-excluded; 10 declaration preserves an inline superseded
# quotation on its own line; 10 declaration names a DIFFERENT identified object (a
# printed figure, a status line, a candidate, a table); 8 pure lexical match on a
# physics sentence or on a ruling record preserved elsewhere.
#
# ──────────────────────────────────────────────────────────────────────────
GUARD_ADJUDICATED_FP.update({
    # manuscript/ave-kb/common/historical-precedents.md:22 -- decl :21 preserves "the line
    # above" (= :20); the stamped line is the NEXT top-level bullet, live canon.
    ('manuscript/ave-kb/common/historical-precedents.md',
     '- **The electron is where it returns:** saturation is a volumetric/longitudinal effect (the breathing 7th DOF at `A→1`, `Z→0`, `Γ=−1`). The longitudinal scalar Heaviside discarded re-engages as the *confined* state. Vector calculus describes radiation but loses matter. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**'),
    # manuscript/ave-kb/common/index.md:70 -- decl :49 is a DIFFERENT table row whose
    # "(both preserved)" names two other leaf docs; pure lexical match.
    ('manuscript/ave-kb/common/index.md',
     '| [The Port Register — per-channel × per-port map](port-register.md) | NO-CLAIM register/discipline leaf (WALK-WORDING ratified by the 2026-07-20 firing): the per-channel × per-port map of the graded-vacuum medium — *whether, here and now, a configuration delivers energy out through which of the four channels*, radiative ($\\mathrm{Re}(Z)>0$, port-not-valve, Ax3-legal) vs reactive (stores-and-returns) vs closed, each row tagged by provenance (axiom-forced / emergent-configurational / instrument-engineered). **14 rows** (4 inherent channels + 9 known ports + 1 explicitly-OPEN Q1). Carries the **FLAG-A** channel-3 speed split ($\\sqrt2\\,c$ PORT/impedance mode vs $\\sqrt{10/3}\\,c$ radiative P-wave) as a column, and the **DM-halo NOT-A-PORT** reactive-near-field resolution. Q1 (does the A1/bulk channel open an independent far-field radiative port for gravitating sources?) stays OPEN pending a Grant/auditor sector-ownership ruling. Promoted from `research/2026-07-20_port-register_draft.md` (#753). 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |'),
    # manuscript/ave-kb/common/physics-lineage-map.md:244 -- decl :239 preserves "the
    # sentence above" inside its own row; :244 is a different table row.
    ('manuscript/ave-kb/common/physics-lineage-map.md',
     '| Elastic-solid pathologies (planet drag; unwanted longitudinal mode) | STANDING | Drag: nothing to drag — matter is medium-constituted. Longitudinal: mode KEPT but non-propagating (A1 confined; myth-guard forbids the "Heaviside deleted a physical mode" overclaim, `the-abandoned-interior.md:22`); non-observation of longitudinal vacuum radiation constrains AVE exactly as it did MacCullagh 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |'),
    # manuscript/ave-kb/common/port-register.md:75 -- decl :77 matches KEEP-BOTH in SENSE
    # (ii) (both-objects-retained, 'what survives = reactive'); it preserves nothing.
    # Site-adjudicated per the batch-1 class correction.
    ('manuscript/ave-kb/common/port-register.md',
     '| P7 | **F6 scalar collar** (instrument-engineered; piston-geometry) | 3 (A1 dilatation-port projection) | **instrument-engineered** (the F6 bath-meter collar $=$ a fixed shell of active lattice sites, Caldeira–Leggett bilinear, scalar dilatation-port read $q=\\Sigma\\,\\mathrm{mean}_p V_{inc}$) | **REACTIVE when bath-coupled (stores-returns) / RADIATIVE only under a deliberate lossy $\\mathrm{Re}(Z)$ friction-plant termination** | **instrument-class** (a coarse acknowledged port) | **RULED R3 2026-07-20 (ratified walk).** The real T2 sink couples as a **PHASED ARRAY** (many independent local contacts, statically-random per-contact phases) — *composing with, not contradicting* #734\'s "effectively-constant" aggregate (**piston $=$ aggregate; array $=$ port geometry**); #734 structural-inexpressibility **rescopes to instrument-class**; phase-carrying build **LICENSED but PARKED**. `[canon, #749 merged 2026-07-20]` docket ENTRY 27 R3 + `research/2026-07-16_f6-bath-meter_CHARTER.md:39`. **Two-method:** #749 docket R3 + charter §coupling. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |'),
    # manuscript/ave-kb/common/port-register.md:76 -- decl :77, same KEEP-BOTH sense (ii)
    # reading as :75; preserves nothing.
    ('manuscript/ave-kb/common/port-register.md',
     '| P8 | **J(ω) scope-split** (a register ROW-CLASS, not a single port) | 3/4 (z=3 srs bath) | **emergent-configurational, scope-dependent** (the same physics is port-closed or port-open depending on the sampled scope) | **0D cell $\\to$ REACTIVE-leaning (recurs, returns within the window) / ∞-lattice $\\to$ "RADIATIVE" only for the super-Ohmic (C2) coupling model (drains via Op3 transduction — still Ax3-lossless microscopically, not a resistor)** | **0D $\\approx$ port-CLOSED config; ∞-lattice $\\approx$ port-OPEN config — but see the RE-BANK** | **CANONICAL (#751 merged 2026-07-20) — with a currency correction.** `research/2026-07-20_jomega-derivation_result.md` §0.1/§4.1: the **frozen driven criterion lands bin (iii) DEGENERATE / UNDETERMINED** ((a-ledger) 0/4 cells, (b-ledger) only the C2 super-Ohmic ∞-lattice) — the clean quantitative split (70–95% / 0–10%) came ONLY from a **post-hoc undriven ring-down** (NOT the frozen prereg) and its "0–10% / coupling-scale-robust / unambiguous" grade is **🔴 RE-BANKED** (§0.3, §4.2). **What survives:** only the ORDERING (0D returns more than ∞-lattice) is coupling-scale-robust; the transfer magnitude tracks the undetermined coupling prefactor. This row-class still formalizes "port-open vs port-closed is a *scope* statement, not a property of the channel," but the quantitative half is UNDETERMINED. **Two-method:** #751 §0.1 frozen-output + §4.1 ledger table. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |'),
    # manuscript/ave-kb/common/port-register.md:87 -- decl :95 introduces the superseded
    # verdict text carried AT :95 itself; :87 is the live Q1 register row whose current
    # verdict is the :93 REVERTED line.
    ('manuscript/ave-kb/common/port-register.md',
     '| **Q1** | **A1 bulk channel — far-field radiative port for gravitating sources** | 3 (A1 bulk; radiative speed $\\sqrt{10/3}\\,c$ per FLAG-A) | **the load-bearing UNFORCED CHOICE** (band-map channel 3 is a *gapless propagating* branch — does a mass quadrupole open an *independent far-field radiative port* into it?) | **Reading A — RADIATIVE, DERIVED-OPEN** *(was "UNRULED — Reading-dependent")* | **★REVERTED 2026-07-20 → Reading-A LIVE** *(was RULED-CONDITIONAL; was the register\'s first explicitly-OPEN row)* | **★REVERTED 2026-07-20 per this row\'s own clause — Reading-A is the standing state; the pulsar exclusion is LIVE against the framework.** The make-or-break mechanical $\\nabla\\!\\cdot\\!u$ common-mode derivation returned **NONE-DERIVES** at review grade (#761 merged @ `caa51c17`, `research/2026-07-20_mechanical-commonmode-derivation_result.md` §5): the A1-dilatation rides the gapless P-branch, the binary drives it at quadrupole order, and the EM Gauss-kill is *structurally blocked* from $\\nabla\\!\\cdot\\!u$ by the bulk restoring force $K\\neq0$ — firing this row\'s own conditional clause. **Verbatim clause that fired** (`[sic]`, from the superseded RULED-CONDITIONAL text preserved below): *"if NONE-DERIVES this ruling REVERTS and the banked Reading-A exclusion (falsification ledger; 9–110σ pulsar) goes live."* Standing physics is now **Reading A** (independent far-field bulk radiative port + O(1) coupling); the banked exclusion is **LIVE** — excluded at **9–110σ (Hulse-Taylor)** / **100–1400× (double-pulsar)** (falsification ledger, entry `q1-reading-A-radiative-bulk-port`, promoted LIVE 2026-07-20). A clean closed-negative against the gravitational bulk sector (Rule 11 honest closure), NOT a softening. **Forward path (a separate FUTURE ruling, not a softening of this revert):** the envelope-sector reduction lane (`research/envelope-sector-reduction`, in flight) is the routed derivation that could later ground a re-open with a **DERIVED** coupling; a re-open needs its own Grant ruling. **Receipts:** #761 result §5 CONSEQUENCE + docket ENTRY 37 + ENTRY 2026-07-20-q1-revert-execution. *(Superseded RULED-CONDITIONAL text — preserved verbatim per Rule 12; do NOT delete Grant\'s ruling text:)* **RULED-CONDITIONAL (Grant 2026-07-20, #756 merged — Reading B = standing physics: no far-field radiative port for gravitating sources; the halo is its complete story).** CONDITIONAL: stands on the make-or-break derivation (mechanical ∇·u common-mode + cold-regime emptying — per re-banked #758 the candidate T_d structure\'s closing step is currently UN-DERIVED, clm-9kd2t3 do-not-build); if NONE-DERIVES this ruling REVERTS and the banked Reading-A exclusion (falsification ledger; 9–110σ pulsar) goes live. Receipts: docket ENTRY 32 (ruling) + the #758 re-bank. *(Superseded: "UNRULED — Grant/auditor sector-ownership adjudication (FLAG-1 / band-map D5; docket ENTRY 29 §Q1)" — preserved per Rule 12.)* `[canon, #750 merged 2026-07-20]` frames it (off-main); companion `research/2026-07-20_q1-pulsar-hardening.md` hardens it against pulsar timing. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |'),
    # manuscript/ave-kb/common/translation-tables/translation-circuit.md:960 -- decl :959
    # is the adjacent G2 row carrying KEEP-BOTH in SENSE (ii) against the :157
    # seismological-S row; preserves nothing.
    ('manuscript/ave-kb/common/translation-tables/translation-circuit.md',
     '| **G3** | **ch-3 (the $A_1$ bulk-longitudinal / dilatation line) is the compression line.** Gapless; FLAG-A two-speed split — PORT/impedance $\\sqrt2\\,c$ vs RADIATIVE far-field $\\sqrt{10/3}\\,c$ | **The COMMON mode** of the same two-conductor line — the even/scalar part referenced to ground; the mode a common-mode choke *does* see. ★**MODE IDENTITY ONLY — this row asserts nothing about what drives it** | **PRIOR ART, canon-consistent — NOT a mint.** [`port-register.md`](../port-register.md):37 already names $A_1$ the *"common-mode scalar/longitudinal (dilatation, mass)"*. **Consistency-class.** ★**The walk\'s "radial-AC-driven" drive restriction is STRUCK; the drive question is OPEN and adversarial to a standing negative — do NOT cite this row as licensing a drive claim in either direction. ★**TWO riders ride this row, both in §12.3** — the second is **FLAG-W, the line\'s unresolved TERMINATION:** `research/2026-08-03_coldq-polar-family_result.md`:170 asks *"At the saturation radius, does the vacuum\'s compression line vent, or does it dead-end?"* and records *"Three canonical leaves, two opposite answers, no repair made"*, **ROUTED TO GRANT, UNRESOLVED**. A named line with an open termination carries its flag** **(a) analytic irrep derivation** — [`k4-port-irrep-decomposition.md`](../../vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md):11 (*"The K4 4-port amplitude space decomposes under the tetrahedral group"*). **(b) INDEPENDENT engine eigen-decomposition** — `src/ave/solvers/node_scattering_multiplicity.py`:81, the all-ones port-sum vector is the single *"+1 eigenvector (the COMMON MODE = symmetric breathing channel"*; corroborated at `research/2026-06-20_node-2domain-nport.md`:61 (shear on a *"separate, differential/deviatoric axis"*) and `:63` (*"from the common-mode dilatation"*). Channel row: [`port-register.md`](../port-register.md):49 (*"two distinct physical longitudinal modes, both retained"*). **★Two-method is (a) vs (b)** — derivation vs separately-run numerics. *(Same 2026-08-07 correction as G2: the old "`:37` + `:49`" pairing was one file read twice and is withdrawn.)* ★**Drive-side state, both riders: §12.3.** 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |'),
    # manuscript/ave-kb/common/vocabulary-register.md:891 -- decls :885/:892 preserve
    # prior STATUS and prior VERIFICATION strings inline inside their own parentheticals;
    # :891 is the live open-ambiguity-flag line.
    ('manuscript/ave-kb/common/vocabulary-register.md',
     '- **open-ambiguity-flag:** ★ROUTED-OPEN — the u/A **transverse** identity-collapse candidate (are the EM and mechanical-transverse sectors two meters on ONE bench object, or two distinct fields?) is a **frontier-queue open question**, gated on the **GW170817 two-distinct-signals** observational test (bulk radiates at $\\sqrt{10/3}\\cdot c \\approx 1.83c$ vs the $|\\Delta v|/c \\lesssim 10^{-15}$ coincidence bound — `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md` §2 item 1b). This register entry adjudicates the **LONGITUDINAL split ONLY** (def-l0ngdu); it takes **NO position** on the transverse collapse. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**'),
    # manuscript/ave-kb/common/wall-taxonomy.md:433 -- decl :437 is a live currency /
    # fence-re-point pointer whose 'preserved' names the 2026-08-05 v1 RULING RECORD under
    # _orchestration/, not any span in this file.
    ('manuscript/ave-kb/common/wall-taxonomy.md',
     "> **FLAG-W dissolution.** [`bulk-impedance-at-saturation-boundary.md`](../vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md):39,:48–55 ($\\Gamma_{bulk}\\to-1$) and [`saturating-modulus-and-backreaction.md`](../vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md):59 (bulk rigid) are plane/projection/profile-relative statements, **not a contradiction**. The ch15 step $Z_{bulk}=\\rho_{bulk}c_{bulk}\\to0$ multiplies a vanishing speed by the CONSTANT density — valid only under the RHO-A profile; under canon's $\\rho_{eff}=\\rho_0/S^3$ (that leaf's own :73; FORK-3(b), fenced, un-adjudicated) the same $c_{bulk}\\to0$ coexists with $Z_{bulk}=\\sqrt{K\\rho_{eff}}\\to\\infty$. Open physics = the constitutive grading near the wall ($\\rho(A)$: FORK-3(b) — **its axial run has now LANDED (2026-08-05) and returned `ROOT-NOT-CERTIFIED` with NO physics bin adjudicated, so the fork is still OPEN and none of that lane's figures may be quoted**; $K(A)$). Declaration blocks sit at the foot of both leaves. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**"),
    # manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-
    # gap.md:159 -- decl :158 preserves 'the ADJUDICATION-PENDING note above + the
    # line-145 body'; :159 sits INSIDE the new G2-RESOLVED note that :158 opens - live
    # prose of that pass, not the preserved body.
    ('manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md',
     '> - **Which side is canonical:** the photon is the **massless transverse-TRANSLATIONAL $u$** family — so **line 145\'s "$A_1$ (scalar/longitudinal/translational $u$) is massless" had the RIGHT sector-family (translational)**; the *inversion the note flags* is resolved in favor of "photon = translational-$u$", NOT the microrotational-$\\omega$ side. The one refinement: the photon is the **transverse** subset of the translational branches (the massless shear pair at $c=\\sqrt{G/\\rho}$), NOT the $A_1$ *longitudinal* mode (which dissipates via Gauss). So :145\'s "$A_1$ … translational $u$ … massless … the photon" is **corrected to** "the massless *transverse*-translational $u$ pair is the photon; $A_1$ longitudinal dissipates". The "$T_2$ (microrotational $\\omega$) carries the mass-gap" half of :145 is likewise re-read: the **gapped $\\omega$ is the mechanical Cosserat sector** (the winding\'s home), which is consistent — it was never the photon. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**'),
    # manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/index.md:27 -- decl
    # :20 is a Rule-12 value re-pin parenthetical inside a DIFFERENT table row (rho_bulk),
    # preserving a struck numeral; it does not reach :27.
    ('manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/index.md',
     '| Longitudinal (P) Wave | $c_L = \\sqrt{(K_{vac}+\\tfrac{4}{3}G_{vac})/\\rho_{bulk}} = \\sqrt{10/3}\\,c \\approx 1.83c$ at $K=2G$ ($\\nu=2/7$; canonical vol_2 Ch 7). Prior $\\sqrt{2}\\,c = \\sqrt{K/\\rho}$ = bulk-modulus dilatational speed (omits $4G/3$ shear) — 2026-06-08 c_L reconciliation 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |'),
    # manuscript/ave-kb/vol1/dynamics/index.md:28 -- decl :25, same rho_bulk value-re-pin
    # parenthetical shape as ch4-index:27; a struck numeral, not a span.
    ('manuscript/ave-kb/vol1/dynamics/index.md',
     '| Longitudinal (P) Wave | $c_L = \\sqrt{(K_{vac}+\\tfrac{4}{3}G_{vac})/\\rho_{bulk}} = \\sqrt{10/3}\\,c \\approx 1.83c$ at $K=2G$ ($\\nu=2/7$; canonical vol_2 Ch 7). Prior $\\sqrt{2}\\,c = \\sqrt{K/\\rho}$ = bulk-modulus dilatational speed (omits $4G/3$ shear) — 2026-06-08 c_L reconciliation 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |'),
    # manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-
    # resonator-coverage.md:190 -- decl :158 is a fork-status cell carrying KEEP-BOTH in
    # SENSE (ii) (Fork-A both arms retained); preserves nothing.
    ('manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md',
     '| E.1 | **bulk/shear impedance-ratio projection-split** — `1.826 = √(10/3)` (channel-correct, two mechanical channels on their own ρc axis) vs `2.582 = √2·√(10/3)` (frozen prereg; the `√2` is the EM-photon `√(K/G)` reference compounded into the mechanical-shear arm). Both **α-free**, both **α-invariant** | — | **RESOLVED (Grant-ratified 2026-06-19)** — the network bulk/shear coupling uses `1.826 = √(10/3)` (channel-correct, two mechanical channels). Frozen prereg `2.582 = √2·√(10/3)` PRESERVED verbatim per Rule-12 (the `√2` compounds the EM-photon `√(K/G)` reference; superseded for the network-coupling use by `1.826`, NOT deleted) | moves NO chord/echo bin, only the bulk/shear gap LOCATION. Solver primary already `RATIO_BULK_SHEAR_MECH = √(10/3)` (`graded_vacuum_network.py:122`, default at `:178`); `2.582` retained as `RATIO_BULK_SHEAR_PHOTON` sensitivity (`:124`). `2026-06-19_electron-Q-coupled-network_result.md`:112–142 (FLAG 1); projection-map seam 4 = RESOLVED=1.826 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |'),
    # manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-
    # resonator-coverage.md:197 -- decl :158, same KEEP-BOTH sense (ii) reading as :190.
    ('manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md',
     '`boundary-observables-m-q-j.md`:19-23) and the wave-channel triple (EM/shear/bulk, 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**'),
    # manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-
    # masses.md:38 -- decl :46 preserves 'Prior form of this note' inline inside its own
    # parenthetical; :38 is the live repaired prose.
    ('manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md',
     '> **Why the old premise was false.** It read *"Because the vacuum substrate is incompressible ($K = 2G$) …"*. The vacuum at $K = 2G$ is **definitively compressible**: the isotropic relation $\\nu = (3K - 2G)/(2(3K+G))$ gives $\\nu_{\\text{Hill}} = 4G/14G = \\mathbf{2/7}$ at $K = 2G$, and $\\nu = 1/2$ is reached **only** in the limit $K \\to \\infty$ — **no finite $K$ is incompressible**. `K = 2G` is the corpus\'s *finite-modulus* trace-reversal lock, not a rigidity statement (`common/q-g47-substrate-scale-cosserat-closure.md:28`; GR-imported per PR [#261](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/261)). 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**'),
    # manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-
    # masses.md:42 -- decl :46 as at :38; and :48 is a FLAGGED-NOT-FIXED finding note, not
    # a preservation declaration.
    ('manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md',
     '> **The correct available premise (the ruled replacement).** The irrotational component sources **no transverse observable**: $\\nabla \\times \\nabla\\Lambda \\equiv 0$ and $\\oint \\nabla\\Lambda \\cdot d\\boldsymbol{\\ell} = 0$ hold at **any** $\\nu$, including $\\nu_{\\text{vac}} = 2/7$. The substrate-native grounding is the corpus\'s **adjudicated longitudinal-sector split**, [`../../../common/vocabulary-register.md`](../../../common/vocabulary-register.md)`:867` (`def-l0ngdu`; the quoted clauses below are at `:870`): the mechanical dilatation $\\nabla\\cdot\\mathbf{u}$ is **DYNAMICAL** — it carries a genuine bulk restoring force $\\tfrac12 K(\\nabla\\cdot\\mathbf{u})^2$ and rides the gapless lattice-computed P-branch — while the EM longitudinal $\\nabla\\cdot\\mathbf{A}$ is **GAUGE**, the curl-only EM Lagrangian giving it no restoring force. Verbatim: *"**One word each way — $\\nabla\\cdot\\mathbf{u}$ propagates; $\\nabla\\cdot\\mathbf{A}$ is gauge.**"* That split is the substrate-native reason the shift is unobservable, and it needs no compressibility assumption. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**'),
    # manuscript/ave-kb/vol3/claim-quality.md:122 -- decl :118 reads 'Corrected bullets
    # are below the banner; the original bullets are preserved beneath them' - :122 is one
    # of the CORRECTED bullets (the list at :120 is headed 'Specific Claims (corrected -
    # channel-split)'); the preserved originals sit further beneath.
    ('manuscript/ave-kb/vol3/claim-quality.md',
     '- Confinement of the BH interior is a **lattice phase transition** ($G_{shear} \\to 0$, shear restoring force vanishes). This **is** a shear-channel impedance collapse: $Z_{shear} = \\rho\\,c_{shear} \\to 0 \\Rightarrow \\Gamma_{shear} = -1$ (Op3), and likewise $Z_{bulk} \\to 0 \\Rightarrow \\Gamma_{bulk} = -1$ at the dielectric rupture. The earlier "NOT an impedance mismatch / $\\Gamma = 0$" wording is the **EM channel only** ($Z_{EM} \\equiv Z_0$ under SYM scaling, $\\Gamma_{EM} = 0$); it does not govern the shear/bulk channels. **⚑ FLAG-CANON REPAIRED 2026-08-05 — CHANNEL-SCOPED (kernel-collapse re-scope ruling — [`2026-08-05-ruling-kernel-collapse-rescope.md`](../../../_orchestration/docket-entries/2026-08-05-ruling-kernel-collapse-rescope.md)`:10`–`:21`, PR #897, **landed**; receipts PR #888 and PR #890, both Tier-2-verified). The repair is a SCOPE, not a sign.** [`research/2026-08-04_coldq-axial-rhob_result.md`](../../../research/2026-08-04_coldq-axial-rhob_result.md):332 recorded that substituting this entry\'s own `:124` statement ($\\rho_{eff} \\to \\infty$ as $\\varepsilon_{11} \\to 1$) into the $Z_{shear} = \\rho\\,c_{shear}$ step above **inverts** the conclusion to $\\Gamma_{shear} = +1$ (measured there as $Z_{shear} \\propto 1/S$). **The repaired form does not run through $Z = \\rho c$ at all, which is why the substitution no longer bites.** At any strain-saturation wall, every transport coupling riding the **strain kernel** — $G$, $K$ on **both** branches of the open density fork, and the $u\\!\\leftrightarrow\\!\\phi$ coupling $G_c$ — **disconnects at the last bond**: total reflection, with the phase **computed from the branch-derived row at the declared plane**, and **independent of the density profile**. The density branch therefore does not move the **mirror**; what it moves is the **delay** through which that mirror reaches anybody. **Certification carried, not compressed (standing print-certification rule, 2026-08-05):** the three load-bearing theorems are measured **exact** — stiffness, residual, beyond-wall spread and RHO-A$-$RHO-B separation all `0.0`, *not a tolerance* — while the discrete **row** is **`ROW-NOT-CERTIFIED`** pending the named `G-RHO2` repair, which gates the *off-limit* sensitivity only ([`research/2026-08-05_last-bond-kernel-collapse_result.md`](../../../research/2026-08-05_last-bond-kernel-collapse_result.md):24,:27,:78). **The rotational channel is CARVED OUT:** $\\gamma\\,S_\\kappa$ is **unwalled at $r_{sat}$**, its own wall being a $\\kappa$-*amplitude* surface this DC strain bias does not reach ($S_\\kappa$(wall) measured `1` to every digit double precision carries at physical gradients, `0.999979916516139` only at an unphysical one-node ceiling — [`research/2026-08-05_srs-twist-coefficient_result.md`](../../../research/2026-08-05_srs-twist-coefficient_result.md):318,:325). **⚑ CROSS-GRADE FENCE, and it is NOT in #897\'s ruled text (added by the doc lane 2026-08-05; the omission at the ruling is routed to Grant):** the carve-out rides the **separate-kernel (L∞-across-grades)** member of an **open** fork — canon records the **cross-grade combine rule as underdetermined at $O(\\alpha)$** ([`common/axiom-register.md`](../common/axiom-register.md):190,:232); under L∞ the strain grade sets the wall and $S_\\kappa$ is untouched, under **normalized-L2-across-grades** every grade rides ONE kernel and the carve-out does **not** stand, and the primary receipt *"does not choose the member"* ([`research/2026-08-05_last-bond-kernel-collapse_result.md`](../../../research/2026-08-05_last-bond-kernel-collapse_result.md):30). **Still open, and not closed by this repair:** the **cross-grade combine rule** (above); FORK-3(b); the **sign** remains plane-relative by the full inversion (`G-PLANE` $= 2.0$ across a one-node plane shift); and the `:124` bullet below is **byte-preserved**, not rewritten. Canonical: [`wall-taxonomy.md`](../common/wall-taxonomy.md) §10.2. **⚑ CURRENCY 2026-08-06 — WHICH RUN THIS QUOTES (doc-lane refresh pass).** The `ROW-NOT-CERTIFIED` state above is the **v1 run\'s** verdict and stands as that run\'s true measurement — `research/2026-08-05_last-bond-kernel-collapse_result.md`:24, *"`G-RHO2` FAILS on an injection point this lane sized wrong at freeze"*. **It is superseded as the CURRENT state:** the repair that v1\'s own §1.3 named — inject `k_0 = ε·ω·Z_1`, not `ε·k_cold` — has run, and TASK 2 is **`ROW-CERTIFIED`**. Read from the landed result document itself, not from a PR title: `research/2026-08-05_last-bond-g-rho2-rerun_result.md`:30, *"`G-RHO2` PASSES. TASK 2 of the last-bond lane is `ROW-CERTIFIED`."* — fitted exponent inside the **unchanged** v1 acceptance interval (PR `#902`, merge commit `b06cbeb1`). **What this does NOT do:** a certified **row** does not certify the **premise scan**, which stays `SCAN-NOT-CERTIFIED` with no bin adjudicated; and it licenses no compressed *"confirmed"* wording here — that stays docket-only. **⚑ FENCE RE-POINT, 2026-08-06 — this routing note now points at the v2 record.** The citable ruled text is the versioned re-issue [`2026-08-06-ruling-kernel-collapse-rescope-v2.md`](../../../_orchestration/docket-entries/2026-08-06-ruling-kernel-collapse-rescope-v2.md):13–29, which **carries the cross-grade combine-member fence inside the ruled text itself**; the 2026-08-05 v1 record is preserved and gains a dated pointer to it. **The earlier *"the omission is at the RULING … routed to Grant for a possible re-issue"* language is RESOLVED — the re-issue happened**, so the fence is now carried AT THE RULING and no print site has to supply it. **Nothing about the physics moves:** the carve-out is still conditional on the per-grade (L∞-across-grades) member, and the cross-grade combine rule is still canon-OPEN. Delta declaration (three deltas from v1, all declared) and the CORRECTED engine-residence map: [`2026-08-06-ruling-kernel-collapse-rescope-v2-correction.md`](../../../_orchestration/docket-entries/2026-08-06-ruling-kernel-collapse-rescope-v2-correction.md) C1/C2 — the engine codes the saturation amplitude **three** ways across two live functionals plus a separate objective, so *"the member the engine actually codes"* is over-broad; the carve-out\'s receipt is STRUCTURAL, not numerical. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**'),
    # manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-
    # large-signal.md:59 -- decl :90 is a def-tk1xfm status-sync striking the PRIOR STATUS
    # in place (KEEP-BOTH); :59 is a mixed-domain impedance sentence, not that status
    # line.
    #   READING EXTENDED 2026-08-12 at review, to dispose of a declaration THE GATE NEVER
    #   SAW. This file also carries, at :8, `> QED-NORMALIZATION CORRECTION (2026-07-03;
    #   Rule-12 -- body preserved below, git is the trail).` -- a DOWNWARD region-delimiting
    #   form. The detector cannot see it: :8 sits in markdown PRE-HEADING front matter (the
    #   first `##` is at :20), which is a DECLARED blind spot of this module, so its absence
    #   from the flag set is not evidence of anything. Hand-read: the banner's own NEXT
    #   sentence (:9) names its object -- "The OQ-1 differential coefficient
    #   \"$7.5/\alpha^3\approx1.93\times10^7$\" below" -- so "body preserved below" is
    #   SELF-SCOPED to the OQ-1 coefficient passage, an identifiable object DIFFERENT from
    #   :59's mixed-domain impedance sentence in the SS0 port/sector table.
    #   CONSISTENCY WITH THE ROUTED CASES, since the standards look asymmetric otherwise:
    #   this batch's stated rule is that a fence needs a declaration that DELIMITS a region
    #   AND an anchor inside it, and that where the named object plausibly INCLUDES the
    #   anchor the row is ROUTED rather than argued. :8 names a different object in its very
    #   next sentence -> stamp. engine-capability-map.md:29/:31's banners name NO object at
    #   all ("body preserved", full stop) -> routed. Same rule, opposite inputs.
    #   * PENDING GRANT QUESTION, flagged not assumed: whether a whole-body "preserved
    #   below" banner fences LATER STATUS STAMPS at all, as opposed to fencing rewrites of
    #   the body. This registration does NOT presume an answer -- it rests on :8's
    #   self-scoping, which holds under either ruling.
    ('manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md',
     '> deviatoric-shear rows are **mechanical** ($Z_{\\mathrm{bulk}}$, $Z_{\\mathrm{shear}}$ — $\\rho\\times$speed, 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**'),
    # manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-
    # solitons.md:123 -- decl :126 is an ADDITIVE KEEP-BOTH resultbox (sense ii); decl
    # :135 preserves 'the graft-v3 candidate above', a different identified object.
    # Neither fences :123.
    ('manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md',
     '- **$Z_{\\mathrm{bulk}}=\\rho_{\\mathrm{bulk}}\\,c_{\\mathrm{bulk}}=\\sqrt2\\,\\rho_{\\mathrm{bulk}}\\,c_0$** at $K=2G$ ($\\Gamma_{\\mathrm{bulk}}\\to-1$) — the **MASS-"3"** channel (A1 dilatation); its confinement surface ([def-cf1srf](../../../common/vocabulary-register.md)) is the $\\Gamma=-1$ cage-wall derived above ($Z_{core}\\to0$). 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**'),
    # manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md:201 --
    # decl :209 preserves 'the original status line above' (= :207) and :218 'every prior
    # status line above'; :201 is a routing cross-link pointer, not a status line.
    ('manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md',
     '> **↗ Electrical-vs-mechanical projection-conflation map** (`research/2026-06-19_electrical-mechanical-projection-map.md`): the EM (Ω) ↔ mechanical (ρc) seams in this section are **NOT one artifact to dissolve** — 1 fixed units-conflation (`Z_bulk` mis-scope, #296) + 6 genuine distinctions the corpus holds. EM↔mechanical is a real impedance-DOMAIN boundary the ξ_topo transducer BRIDGES (units change), not a separation to resolve away; bulk↔shear is same-domain ($H_{\\mathrm{couple}}$). The unified network buys HYGIENE, not a derivation; α stays echo. The 1.826-vs-2.582 ratio (seam 4) is OPEN pending Grant. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**'),
    # manuscript/backmatter/07_universal_saturation_kernel.tex:144 -- decl :77 is a %
    # comment holding a prior TABLE CELL verbatim inside itself; decl :142 says the prior
    # wording is preserved IN THE GIT TRAIL, which is not an in-file fence.
    # Chapter/section containers reach both.
    ('manuscript/backmatter/07_universal_saturation_kernel.tex',
     "Because that comparison is against \\textbf{GR exact} --- i.e.\\ against \\emph{theory}, not against a measurement --- the former grade ``the most direct cross-scale \\emph{experimental} validation'' is \\textbf{withdrawn}, with no replacement superlative. The honest booking of the same row is the one in the A-034 anchor table of Backmatter Ch~\\ref{app:verification} (\\S\\ref{sec:a034_empirical_anchors}): ``GR exact ($\\omega_R M_g = 18/49$), $1.7\\%$''. \\textbf{Toroidal-vs-fundamental carve (2026-08-05).} Where this chapter calls the ring-down ``the saturation cavity's fundamental resonance mode'', read \\emph{a} cavity mode: the only certified instrument in the arc computes the \\textbf{toroidal} branch (odd-parity, purely shear) and explicitly declines to call it the fundamental, while the \\textbf{spheroidal} branch (even-parity, P and SV coupled, so the compressional A1 dilatation channel and the shear channel move together) is \\textbf{not built anywhere in this arc} and is the branch that in the elastodynamic analogue carries the lower-frequency, longer-lived $\\ell = 2$ fundamental. \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/common_equations/eq_axiom_4.tex:55 -- decl :41 is the physics table row
    # 'Impedance preserved' - a pure lexical match, the class batch 1 named at
    # 03_macroscopic_relativity.tex:11.
    ('manuscript/common_equations/eq_axiom_4.tex',
     '\\item \\textbf{Particles:} The electron is a real-space \\textbf{$0_1$ unknot} (\\emph{no} self-intersection). Its \\textbf{rest mass is the A1 dilatation sector} at $V_{snap}$ ($m_e c^2 = $ trapped acoustic-compression energy; \\texttt{def-vyvsn1}, PR\\,\\#260) --- \\emph{not} a $\\mu$-short at a torus-knot self-intersection. The confining $\\Gamma = -1$\\gammaundeclared{} wall is the transverse Cosserat ($T_2$) self-trap at $V_{yield}$, inside which the A1 mass core operates \\emph{sub}-saturated at $A = \\sqrt{\\alpha} \\approx 0.085$. The magnetic-vs-capacitive $\\Gamma = -1$\\gammaundeclared{} fork is a \\textbf{degenerate sign / spin selector} (chirality-set, $|\\Gamma| = 1$\\gammaundeclared{} both ways), \\emph{not} the mass mechanism (B3-degenerate, PR\\,\\#260). \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}'),
    # manuscript/frontmatter/00_foreword.tex:10 -- decl :126 preserves 'the original
    # bullet wording' of a DIFFERENT bullet 116 lines below; a chapter-container reach.
    ('manuscript/frontmatter/00_foreword.tex',
     "\\noindent \\textbf{Thread 1 --- A longitudinal channel.} Maxwell's 1873 \\emph{Treatise}~\\cite{maxwell1873treatise} expressed parts of electrodynamics in Hamilton's quaternion notation~\\cite{hamilton1853lectures} (the equations listed in quaternion form at the chapter ends, not written exclusively in them); Heaviside and Gibbs~\\cite{heaviside_emtheory, gibbs_wilson1901vector} subsequently recast the theory in the \\texttt{grad}/\\texttt{div}/\\texttt{curl} vector calculus that became standard. This reformulation preserved the physics --- the scalar (divergence) information is retained through Gauss's law --- so no degree of freedom was lost in the change of notation. Standard electrodynamics nonetheless admits no longitudinal, compressional wave in vacuum: the free photon is purely transverse. AVE \\emph{adds} such a mode as a hypothesis --- the longitudinal bulk-scalar (``A1'') sector of a material vacuum, analogous to a pressure (P-)wave in an elastic solid --- proposed as the carrier of rest mass ($m_e c^2$ as trapped longitudinal compression energy). The quaternion-era scalar grade is noted here as historical precedent for treating a scalar channel on equal footing, not as a physical mode that was removed. \\kbleaf{ave-kb/common/historical-precedents.md} (Root 1) and \\kbleaf{ave-kb/common/the-abandoned-interior.md} are the canonical lineage homes. \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_1_foundations/chapters/02_macroscopic_moduli.tex:16 -- decl :15 is a
    # % comment HOLDING the prior wording verbatim inside itself; :16 is the live
    # replacement wording that comment records.
    ('manuscript/vol_1_foundations/chapters/02_macroscopic_moduli.tex',
     'A classical Cauchy elastic solid supports transverse waves only if its longitudinal branch is deleted outright: the longitudinal speed $c_L^2 = (\\lambda + 2\\mu)/\\rho$ must vanish, forcing $\\lambda = -2\\mu$. However, the bulk modulus of a Cauchy solid is $K = \\lambda + \\frac{2}{3}\\mu$. Substituting the zero-longitudinal condition yields: \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}'),
    # manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:105 -- decl
    # :25 governs the two commented-out bullets directly below it (:26-31); decl :142
    # preserves a printed FIGURE. Neither reaches :105; chapter/section containers do.
    ('manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex',
     "\\emph{Sector disambiguation (A1 $\\perp$ T2, per PR\\#260 / \\texttt{master-equation.md}:95).} The magnetic-branch $\\Gamma \\to -1$\\gammaundeclared{} named above is the chirality/spin \\textbf{sign-selector} ($\\mu$-first $\\Rightarrow \\Gamma=-1$\\gammaundeclared{} vs $\\varepsilon$-first $\\Rightarrow \\Gamma=+1$\\gammaundeclared{} are the spin-conjugate signs); it is mute on the mass sector. The invariant rest mass is the \\textbf{$A_1$ longitudinal-dilatation} confinement ($Z_{bulk} \\to 0 \\Rightarrow \\Gamma_{bulk} = -1$ at the bulk cage), a separate grade from the $T_2$ charge-winding. The ``two 3s'' are orthogonal --- \\emph{mass} $= A_1$ dilatation; \\emph{charge} $= T_2$ Cosserat winding --- so ``rest mass'' here is not generated by the magnetic/charge sector; reading confinement as proceeding \\emph{via} the charge sector would wire the mass-cage into the $T_2$ winding and break the $A_1 \\perp T_2$ orthogonality. The magnetic-vs-electric fork is degenerate on the equilibrium observables ($Z = Z_0\\sqrt{S}$, $|\\Gamma|=1$\\gammaundeclared{} both ways); the asymmetry is chirality-set, not substrate-forced. \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:359 -- decl
    # :352 is a % comment holding the prior wording of its own passage; decl :25 governs
    # :26-31. Neither fences :359.
    ('manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex',
     'At the $K_{vac}=2G_{vac}$ operating point (equivalently Poisson ratio $\\nu_\\text{Hill}=2/7$ --- GR-imported through $K = 2G$, not derived; \\kbleaf{ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md}:146) the longitudinal P-wave carries the $4G/3$ shear term; the pure bulk-modulus dilatational speed $\\sqrt{K_{vac}/\\rho_{bulk}}=\\sqrt{2}\\,c$ omits it. Because $c_L > c$, the longitudinal mode carries only phase information, not \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}'),
    # manuscript/vol_2_subatomic/chapters/05_electroweak_gauge_theory.tex:51 -- decl :84
    # is a % Rule-12 banner holding the prior wording of the phrase directly above :84;
    # the chapter container is what reaches :51.
    ('manuscript/vol_2_subatomic/chapters/05_electroweak_gauge_theory.tex',
     "\\noindent\\textbf{Premise note (2026-08-03).} The step above deliberately does \\emph{not} assume an incompressible substrate. The vacuum at $K = 2G$ is \\textbf{definitively compressible}: the isotropic relation $\\nu = (3K - 2G)/(2(3K+G))$ gives $\\nu_{\\text{Hill}} = 4G/14G = 2/7$ at $K = 2G$, and $\\nu = 1/2$ is reached only as $K \\to \\infty$, so \\emph{no} finite $K$ is incompressible. Incompressibility would in fact be needed to claim that an irrotational addition produces no local compression---$\\nabla\\cdot(\\nabla\\Lambda) = \\nabla^2\\Lambda \\neq 0$ for general $\\Lambda$---which is why that leg is dropped rather than rescued. The gauge conclusion does not depend on it: invariance of $\\nabla\\times\\mathbf{A}$ and of every winding/linking integer follows from $\\nabla\\times\\nabla\\Lambda \\equiv 0$ and $\\oint\\nabla\\Lambda\\cdot d\\boldsymbol{\\ell} = 0$ at \\emph{any} $\\nu$. The substrate-native grounding is the corpus's adjudicated longitudinal-sector split (\\kbleaf{ave-kb/common/vocabulary-register.md}, \\texttt{def-l0ngdu}): the mechanical dilatation $\\nabla\\cdot\\mathbf{u}$ is \\textbf{dynamical}---it carries the bulk restoring force $\\tfrac12 K(\\nabla\\cdot\\mathbf{u})^2$ and rides the propagating P-branch---while the EM longitudinal $\\nabla\\cdot\\mathbf{A}$ is \\textbf{gauge}, the curl-only EM Lagrangian giving it no restoring force. One word each way: $\\nabla\\cdot\\mathbf{u}$ propagates; $\\nabla\\cdot\\mathbf{A}$ is gauge. \\textbf{That split is load-bearing here, not decoration---it is what closes the $\\mathbf{E}$ leg.} The struck clause was this section's only (and garbled) $\\mathbf{E}$ coverage: it labelled $-\\partial_t\\mathbf{A}$ ``localised compression'' when $-\\partial_t\\mathbf{A}$ is the electric field. Without a replacement the chain would cover $\\mathbf{B}$ and the topological integers but leave $\\mathbf{E}$ open, since $\\delta\\mathbf{E} = -\\partial_t\\nabla\\Lambda \\neq 0$ pointwise. The textbook cancellation is \\emph{not} available in this section's variables---there is no scalar-potential companion here to absorb $\\varphi \\to \\varphi - \\partial_t\\Lambda$---so the closure is substrate-native instead: $\\delta\\mathbf{E}$ is irrotational, hence purely EM-longitudinal, and a channel with no restoring force stores no energy and exerts no force. \\textbf{[SUPERSEDED 2026-08-10 --- that last clause is the step that failed; see immediately below.]}\\quad \\textbf{SECOND FAILURE AT THIS STEP (dated note, 2026-08-10, R43 item (c); repair prose LANE-AUTHORED against Tier-2 finding C22 --- no ratified text was supplied for this item, unlike the Axiom-3 repair).} \\emph{This is the second time the electric leg of this section's U(1) argument has failed, and it is recorded plainly rather than folded into the repair.} \\textbf{First failure (2026-08-03):} the step rested on ``the vacuum substrate is incompressible ($K = 2G$)'' --- a premise that is simply false at any finite $K$; it was struck, and the \\texttt{def-l0ngdu} no-restoring-force clause was promoted from grounding-decoration to a load-bearing step of the chain (step 3$'$) to close $\\mathbf{E}$ in its place. \\textbf{Second failure (2026-08-10):} that replacement clause is \\emph{itself} false. ``A channel with no restoring force stores no energy'' does not hold for time-dependent $\\Lambda$: no restoring force means no \\emph{potential} term, but the \\emph{kinetic} term $\\tfrac12\\varepsilon_0|\\partial_t\\mathbf{A}_L|^2$ stores energy in exactly that channel. Both repairs targeted the same load-bearing joint --- the $\\mathbf{E}$ leg --- and both substituted a claim that had not been machine-checked before it was made load-bearing. The step is therefore \\textbf{rescoped rather than re-patched a third time}: only the residual time-independent family is derived here, and canon holds \\textbf{no valid derivation of any full U(1) family} --- the residual time-independent family is the only exact symmetry statement available, and supplying the first correct one is what the Axiom-3 repair does. Basis: the bound-constitutive lane's Tier-2 finding C22 and its consequence-audit flag (a), at \\texttt{research/2026-08-10\\_bound-constitutive\\_result.md}; ruling at \\texttt{\\_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md} (which names ``the twice-failed ch05 paragraph'' in its companion S+G record). \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:41 -- decl
    # :161 is a % comment holding prior wording for its own passage; the chapter container
    # spans :1-4203, which is the whole reach.
    ('manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex',
     "By contrast, an electron ($0_1$ unknot) is a massive topological defect. It represents a permanent macroscopic \\textbf{Impedance Mismatch} ($\\Gamma = -1$\\gammaundeclared{}) to the linear vacuum. It does not travel as a shear wave at $c_0$; instead, its motion displaces the lattice, generating longitudinal acoustic pressure waves governed by the vacuum's \\textbf{Bulk Modulus}. \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:239 --
    # decl :161 as at :41 - a % comment holding prior wording for a different passage;
    # chapter-container reach.
    ('manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex',
     'An $s$-orbital ($l=0$) is a pure longitudinal (compressional) breathing mode projecting force exclusively onto the scalar Bulk modulus ($K$). For an element such as Helium ($1s^2$) or Beryllium ($2s^2$), there are strictly zero $p$-electrons. The transverse (shear) spatial axes are entirely empty. \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}'),
    # manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:383 --
    # decl :161 (prior wording, different passage) and :2575 ('Architecture preserved.', a
    # physics heading); chapter/section-container reach.
    ('manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex',
     "This is \\emph{not} 377~$\\Omega$. The electron interacts with the vacuum's bulk modulus (acoustic impedance), not the shear modulus (electromagnetic impedance). This $Z_{LC} = 12$~$\\Omega$ is the reason atomic physics operates in the \\emph{low-impedance} regime---the electron's circuit impedance is $Z_{LC}/Z_0 \\approx 0.033 = \\alpha/\\pi$, consistent with the fine structure constant governing all electromagnetic coupling. \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex:163 -- decl :142
    # is the PHYSICS sentence 'the transverse impedance ratio is preserved across all
    # gravitational gradients' - the exact lexical class batch 1 adjudicated at this same
    # file.
    ('manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex',
     'This positive bulk resistance guarantees that the spatial substrate is \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}'),
    # manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex:31 -- the
    # stamped line IS a live dated Number-correction note; the declarations it reaches
    # (:70, :82, :169, :291) each preserve a DIFFERENT object - printed figures, a
    # superseded comparison table, a ruling record.
    ('manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex',
     "\\noindent\\textbf{Number correction (2026-07-21, ringdown MATCH-ARTIFACT + Grant Ruling B1; printed figures above/below preserved per Rule 12).} The $-0.45\\%$/$-0.47\\%$ spinning-remnant figures printed throughout this section are \\textbf{frame-mixed compensating-error artifacts}: a corrupt Kerr QNM reference table $\\times$ a source-vs-detector-frame mass mismatch cancelled a genuine $\\approx -10\\%$ below-Kerr deficit into a spurious sub-percent match (canon-corrected 2026-07-20, MATCH-ARTIFACT; the ``outperforms GR for $\\tau$'' contrast rode the same compensation and is retracted). On the frame-independent dimensionless comparator the retired v2 mapping sits $-9.5\\%$ below true Kerr. \\textbf{Under Grant Ruling B1 (2026-07-21)} the v1$\\leftrightarrow$v2 fork is ruled, re-selecting \\textbf{v1} as the standing spinning-$\\omega_R$ mapping at $+2.63\\%$ mean (catalog spins; mapping-conditional, disclosed-phenomenological, consistency-class --- \\emph{not} a zero-parameter benchmark), with $\\tau$ a $-5.4\\%$ open near-miss tension. The cold $\\ell=2$ eigenvalue $18/49$ ($-1.69\\%$, zero free parameters) is untouched and remains the only forward-prediction content here. Receipts: \\kbleaf{ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md} ``GRANT RULING B1''; research \\kbleaf{ligo-ringdown-driver-design.md} \\S 7--10 banners. \\textbf{Extended 2026-07-30 (Grant ruling; printed occurrences below preserved per Rule 12).} The companion \\emph{validation-scope} claim quoted from \\texttt{clm-395gps} at four points in this chapter --- that the Kerr quality factor ``matches GR sub-2\\% only for $a_* = 0.3$--$0.8$'' (``10--18\\% frequency error otherwise'') --- is \\textbf{likewise RETRACTED under Ruling B1 (2026-07-21)}: it was computed against the same corrupt Kerr reference tables and source-frame masses (\\#774); the truth-source card has since struck it (\\kbleaf{manuscript/ave-kb/vol3/claim-quality.md} \\texttt{clm-395gps}, at \\texttt{:204}); and the corrected picture is that the topological flat $Q = \\ell = 2$ is scoped to the $a_* = 0$ cold anchor --- it would fail at $\\bar{D}_Q = -38\\%$ at catalog spins --- while the spin-refined m$\\Omega$ law lands at $-5.44\\%$ (Resultbox) / $-4.57\\%$ (ZAMO), an open near-miss tension rather than a validated sub-2\\% band. \\textbf{Per-occurrence reconciliation EXECUTED 2026-08-05} (manuscript-reconciliation program, \\#780): the four printed occurrences of the ``validated only for $a_* = 0.3$--$0.8$'' / ``matches GR sub-2\\%'' claim --- in the A-034 anchor paragraph above, in the post-hoc-scope box, in the Phase-4 spin-sweep paragraph and in the $Q = \\ell$ closing note --- each now carry the retraction \\emph{at the site}, with no replacement number at any of them. \\textbf{Current status of the cold eigenvalue's derivation (2026-08-05, current-status note, \\textbf{RE-ISSUED} at this date --- this is not a retraction of $18/49$ and not a hold on this chapter).} \\emph{Why it is re-issued:} the ruled three-clause form this note executes was staged with a second clause reading that FORK-3(b) was \\emph{owed} an axial run; that run had already landed when the note first printed, so the clause is re-issued here against the post-run state rather than carried stale. Each clause below is stated at its own \\textbf{certification line}, and no clause is compressed to a bare ``confirmed''. Three things are true at once and must be read together. (i) A \\textbf{certified} instrument for the graded saturation cavity's \\emph{axial} ($\\ell = 2$ toroidal) shear pole now exists --- its certification line reads \\textsc{root-certified}, with twelve of twelve gates passing and twelve of twelve fireability self-tests firing --- and \\textbf{its computed pole does not land at $18/49$}; its pre-registered rider fired, falsifying $r_{eff} = r_{sat}/(1 + \\nu_{vac})$ \\emph{as a derivation of the eigenfrequency} while leaving the eigenvalue's other legs untouched (\\kbleaf{research/2026-08-03\\_coldq-pole-v2.4-root\\_result.md}; that document propagates to no leaf and mints no claim id --- it is cited here as current status, not imported as canon). (ii) The alternative density branch of the profile (FORK-3(b), $\\rho_{eff} = \\rho_0/S^3$) is \\textbf{not owed an axial run --- it has HAD one}, and running it adjudicated nothing. Its certification line reads \\textsc{root-not-certified} \\emph{on every configuration that has a root}; three self-tests failed to fire on thresholds that lane sized wrong at freeze, and the lane records that the thresholds are \\textbf{not} retuned and \\textbf{no physics bin is adjudicated}. So \\textbf{the fork is still open} --- open \\emph{because the run adjudicated nothing}, not because the run is outstanding --- and none of that lane's figures may be quoted (\\kbleaf{research/2026-08-04\\_coldq-axial-rhob\\_result.md}). (iii) The \\textbf{polar (spheroidal) family is not adjudicated at all, and the reason is instrument-class}: its certification line reads \\textsc{solver-not-certified}, with \\textbf{no physics bin --- \\texttt{BIN-P1}, \\texttt{BIN-P2} (the split), \\texttt{BIN-P3} --- adjudicated at any precedence level}, and found \\emph{no} stable root on any configuration for a mechanism its own pre-registration named in advance --- two channels radiating at different speeds mean a single shear-channel outgoing factor leaves the bulk channel's residual amplitude suppressed \\emph{beyond all orders}, and a polynomial (Chebyshev) basis in that lane's compactified radial coordinate cannot resolve it. \\textbf{The singular point is at the outer boundary, not at the wall}: in that lane's coordinate the compactified \\emph{infinity} $A = 0$ is where the unbalanced $(k_P^2 - k_S^2)$ term diverges like $1/A^2$, making $A = 0$ an irregular singular point of the radial equation, with the residual bulk-outgoing amplitude going as $e^{-c/A}$ --- smooth at that endpoint with every derivative zero, so every polynomial coefficient sees essentially nothing of it. The saturation wall sits at the \\emph{other} end of that interval and is not implicated; the lane's pre-registered wall-singularity bin \\texttt{BIN-PF-WALLSING} was in fact \\textbf{never evaluated}, its indicial analysis being part of the unrun set. This is a limitation of that instrument at radial infinity, not a statement about the wall or about the cavity (\\kbleaf{research/2026-08-03\\_coldq-polar-family\\_result.md} \\S 1.3, \\S 2.2, \\S 3). \\textbf{Consequently no axial-vs-polar splitting is claimed anywhere in this chapter: that number does not exist.} \\textbf{Kernel-collapse pointer (added with the re-issue, 2026-08-05; certification status carried at the sentence, per the standing print-certification rule).} A separate lane has since asked what \\emph{terminates} the wall, and it bears on the three clauses above chiefly through what it does \\textbf{not} settle. On the derived route every transport coupling that rides the Axiom-4 strain kernel is graded to zero at the last bond, so the region beyond the wall is \\emph{removed from the algebra} rather than out-weighed. \\textbf{Its certification state, carried with it:} the three load-bearing disconnection theorems are \\textbf{measured exact} --- the last-bond stiffness, the residual $|\\Gamma_{LB} + 1|$, the spread over the entire beyond-wall grid and the separation between the two density branches each measure exactly zero, a measurement and not a tolerance --- and the continuum-disjointness task is \\textbf{certified} with its bin adjudicated; but the \\textbf{discrete row's certification is PENDING} the named \\texttt{G-RHO2} repair (that task reports \\textsc{row-not-certified} on an injection point sized wrong at freeze), and the premise scan reports \\textsc{scan-not-certified} and adjudicates no bin. \\textbf{None of it is a bare ``confirmed''} (\\kbleaf{research/2026-08-05\\_last-bond-kernel-collapse\\_result.md}). The measured $\\Gamma = -1$\\gammaundeclared{} is a \\textbf{last-bond-plane} statement --- the same lane measures a full short$\\leftrightarrow$open inversion one node outward, at a crossover it also shows does not fire at physical parameters --- so it travels with its plane or it does not travel. \\textbf{What it does NOT do to clause (ii):} the kernel-collapse route makes the wall's \\emph{end condition} density-branch-independent, while the eigenvalue this chapter prints rides the \\emph{approach} profile, and FORK-3(b) is an approach-profile fork. \\textbf{The fork stays open and clause (ii) is unchanged by it.} Ruling records, cited as pointers rather than summarised into print: \\kbleaf{\\_orchestration/docket-entries/2026-08-05-ruling-flag-causal-kernel-collapse.md} together with its status addendum, and the measured re-scope receipts \\kbleaf{\\_orchestration/docket-entries/2026-08-05-ruling-flag-causal-rescope-receipts.md}, which demote the ruling from universal to \\textbf{channel-scoped} (the rotational transport is carved out --- it reaches the wall untouched) and record that the final disposition word was not on the record at the date they were written. \\textbf{Currency, 2026-08-06:} both of those readings have since moved and are corrected here rather than carried stale --- the final disposition word \\emph{is} on the record (the FINAL FORM re-scope ruling, \\kbleaf{\\_orchestration/docket-entries/2026-08-05-ruling-kernel-collapse-rescope.md}), and the canonical home for the kernel-collapse block, \\kbleaf{ave-kb/common/wall-taxonomy.md} \\S 10.2, \\textbf{has landed}, so this paragraph now points at a live anchor. \\textbf{Nothing in the certification content moves}: the discrete row remains \\textsc{row-not-certified} pending the named \\texttt{G-RHO2} repair. \\textbf{And the carve-out does not travel unfenced} --- ``the rotational transport reaches the wall untouched'' rides the separate-kernel ($L^\\infty$-across-grades) member of an \\emph{open} fork, canon recording the cross-grade combine rule as underdetermined at $O(\\alpha)$ (\\kbleaf{ave-kb/common/axiom-register.md}); on the normalized-L2 member the carve-out does not stand. \\textbf{Toroidal-vs-fundamental carve (mandatory wherever this chapter says ``ring-down mode'').} The certified instrument computes the \\textbf{toroidal} branch --- odd-parity, purely shear --- and explicitly declines to call it the fundamental. The \\textbf{spheroidal} branch (even-parity, with the P and SV polarizations \\emph{coupled}, so the compressional A1 dilatation channel and the shear channel move together) is \\textbf{not built anywhere in this arc}, and it is the branch that in the elastodynamic analogue carries the lower-frequency, longer-lived $\\ell = 2$ fundamental. Read ``the ring-down mode'' in this chapter as \\emph{a} cavity mode, not as a demonstrated fundamental. \\textbf{Currency 2026-08-06 --- which run this quotes (doc-lane refresh pass).} The \\textsc{row-not-certified} state above is the \\textbf{v1 run's} verdict and stands as that run's true measurement (\\kbleaf{research/2026-08-05\\_last-bond-kernel-collapse\\_result.md}:24). \\textbf{It is superseded as the current state:} the repair that v1's own \\S1.3 named --- inject $k_0 = \\varepsilon\\,\\omega\\,Z_1$, not $\\varepsilon\\,k_{cold}$ --- has run, and TASK~2 is \\textsc{row-certified}, read from the landed result document itself rather than from a PR title (\\kbleaf{research/2026-08-05\\_last-bond-g-rho2-rerun\\_result.md}:30; PR~\\#902, merge commit \\texttt{b06cbeb1}). A certified \\emph{row} does \\textbf{not} certify the \\emph{premise scan}, which stays \\textsc{scan-not-certified} with no bin adjudicated, and no compressed ``confirmed'' wording is licensed here. \\textbf{Fence re-point, 2026-08-06 --- this routing note now points at the v2 record.} The citable ruled text is the versioned re-issue \\kbleaf{\\_orchestration/docket-entries/2026-08-06-ruling-kernel-collapse-rescope-v2.md}:13--29, which \\textbf{carries the cross-grade combine-member fence inside the ruled text itself}; the 2026-08-05 v1 record is preserved and gains a dated pointer to it. \\textbf{The earlier ``the omission is at the ruling \\ldots routed to Grant for a possible re-issue'' language is resolved --- the re-issue happened}, so the fence is now carried at the ruling and no print site has to supply it. \\textbf{Nothing about the physics moves:} the carve-out is still conditional on the per-grade ($L^\\infty$-across-grades) member and the cross-grade combine rule is still canon-OPEN. Delta declaration and the corrected engine-residence map: \\kbleaf{\\_orchestration/docket-entries/2026-08-06-ruling-kernel-collapse-rescope-v2-correction.md} C1/C2 --- the engine codes the saturation amplitude \\textbf{three} ways across two live functionals plus a separate objective, so ``the member the engine actually codes'' is over-broad and the carve-out's receipt is \\textsc{structural}, not numerical. \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex:57 --
    # chapter/section reach to :31 and :70, which preserve printed figures and a ruling
    # record respectively - neither is this prose.
    ('manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex',
     "Critically, gravity is \\textbf{Symmetric in the EM-transverse channel}: the EM characteristic impedance $Z_{EM}(r) = \\sqrt{\\mu'(r)/\\varepsilon'(r)} = Z_0$ is \\textit{invariant} at all radii, because both $\\mu'$ and $\\varepsilon'$ scale identically with $n(r)$. There is \\textbf{no EM impedance mismatch} and \\textbf{no EM reflection coefficient} ($\\Gamma_{EM} = 0$ everywhere under SYM scaling); here $Z_0 \\equiv Z_{EM}$ only, and the shear and bulk channels carry separate impedances $Z_{shear}$ and $Z_{bulk}$. The EM channel sees the standard GR horizon where the transverse refractive index $n(r) - 1 = 2GM/(c^2 r)$ reaches unity at the Schwarzschild radius $r_s = 2GM/c^2$ ($n \\to \\infty$), but it is matched, not reflected. The $\\Gamma = -1$\\gammaundeclared{} total-reflection wall lives instead in the shear and bulk channels at the radial-strain unity radius $r_{sat} = 7GM/c^2 = 3.5\\,r_s$, where $G_{shear} \\to 0$ and $Z_{shear}, Z_{bulk} \\to 0$. This is the fundamental distinction between the electron's confinement (bulk-channel TIR, $\\Gamma_{bulk} = -1$ at the knot boundary where $Z_{bulk} \\to 0$) and the black hole's confinement. \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex:68 --
    # chapter/section/subsection reach to :31 and :70, same reading as :57.
    ('manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex',
     "The saturated interior therefore acts as a \\textbf{perfect reflector for shear waves}. The phase transition eliminates the shear restoring force ($G_{shear} \\to 0$, $c_{shear} \\to 0$), which \\textbf{is} a shear-channel impedance collapse: $Z_{shear} = \\rho\\,c_{shear} \\to 0 \\Rightarrow \\Gamma_{shear} = -1$. The bulk-longitudinal channel collapses with it ($c_{bulk} \\to 0 \\Rightarrow Z_{bulk} \\to 0 \\Rightarrow \\Gamma_{bulk} = -1$), while the EM-transverse channel remains matched ($\\Gamma_{EM} = 0$). This is identical to the vanishing of transverse acoustic modes at a solid--liquid boundary, which is exactly $Z_{shear} \\to 0$ at the interface. \\textbf{Sign-relativity declaration (2026-08-05; Grant ruling 2026-08-04).} That bulk step is \\textbf{profile-conditional and its declarations must travel with it}: $Z_{bulk} = \\rho_{bulk} c_{bulk} \\to 0$ multiplies a vanishing speed by the \\emph{constant} density, which is the RHO-A branch; on the fenced $\\rho_{eff} = \\rho_0/S^3$ branch (FORK-3(b), \\textbf{open}) the same $c_{bulk} \\to 0$ coexists with $Z_{bulk} = \\sqrt{K\\rho_{eff}} \\to \\infty$. Axiom~3 forces only $|\\Gamma| = 1$\\gammaundeclared{}; a signed $\\Gamma$ additionally requires its \\textbf{reference plane} (a quarter-wave of graded skin inverts short$\\leftrightarrow$open) and its \\textbf{projection} (the same cutoff presents $Z \\to \\infty$ on the series-graded branch and $Z \\to 0$ on the shunt-graded branch), and \\textbf{the sign is computed from the branch-derived wall row, never chosen}. Full declaration: Vol~9 \\S``Graded Vacuum Impedance Network'' (Device Circuit Models); canonical \\kbleaf{ave-kb/common/wall-taxonomy.md} \\S10. \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex:344 --
    # decl :291 preserves 'the table above' (its own superseded comparison table) and :31
    # the printed figures; :344 is a later scope paragraph.
    ('manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex',
     "\\noindent\\textbf{Scope --- the carve this prediction lives or dies on, and it is a channel carve, not a hedge.} The three-strike result above kills \\textbf{the medium-latch channel only}. It is \\emph{not} a prediction that no memory is observed, and it is \\emph{not} in tension with the GR value, because \\textbf{the GR memory is source-side}: the wave's energy density is \\emph{even} in $h$, so $\\langle h^2\\rangle \\neq 0$ rectifies trivially, and that energy sources the A1 dilatation channel. \\textbf{Whether AVE reproduces the GR/Christodoulou value through that flux channel is an OPEN derivation} --- it may; it has not been done. Read the null strictly: the substrate's own constitutive nonlinearity latches nothing. \\textbf{The flux channel is not covered by this null and is not claimed either way.} \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_3_macroscopic/chapters/21_black_hole_interior_regime_iv.tex:200 --
    # decl :207's 'the 2026-08-05 v1 record is preserved' names a RULING RECORD under
    # _orchestration/, not a span in this chapter.
    ('manuscript/vol_3_macroscopic/chapters/21_black_hole_interior_regime_iv.tex',
     '$Z_{bulk} = \\rho_{bulk} c_{bulk} \\to 0$ is the constant-$\\rho$ (RHO-A) \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}'),
    # manuscript/vol_9_vacuum_datasheet/chapters/02_absolute_maximum_ratings.tex:105 --
    # decl :88 carries KEEP-BOTH in SENSE (ii) (two B_snap / E_yield readings retained
    # side by side); preserves nothing.
    ('manuscript/vol_9_vacuum_datasheet/chapters/02_absolute_maximum_ratings.tex',
     'The bulk compressional wave speed obeys $c_{bulk}^2 = c_0^2\\,[\\,1 + \\bar{\\rho}/(1 - \\bar{\\rho}^2)\\,]$ (canonical relation at sibling-repo \\kbleaf{AVE-Propulsion/manuscript/vol\\_propulsion/chapters/04\\_superluminal\\_transit.tex}:86; $\\bar{\\rho} = \\delta\\rho/\\rho_0$ the normalized volumetric strain, $\\bar{\\rho} \\in [-1, 1]$). Setting $c_{bulk} = 0$ gives $1 + \\bar{\\rho}/(1-\\bar{\\rho}^2) = 0 \\Rightarrow \\bar{\\rho}^2 - \\bar{\\rho} - 1 = 0$, whose negative root is \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}'),
    # manuscript/vol_9_vacuum_datasheet/chapters/03a_device_circuit_models.tex:79 -- decl
    # :49 is explicitly sense (ii): 'Which operating point (KEEP-BOTH --- two distinct
    # quantities)'.
    ('manuscript/vol_9_vacuum_datasheet/chapters/03a_device_circuit_models.tex',
     "\\noindent The graded vacuum impedance network is the equivalent-circuit model of the medium drawn as three wired reactance channels --- $Z_{\\mathrm{EM}} \\equiv Z_0$ (the matched radiative port, $\\Gamma_{\\mathrm{EM}}=0$), $Z_{\\mathrm{shear}}=\\rho_{\\mathrm{bulk}}\\,c_{\\mathrm{shear}}$ (deviatoric $G$, $\\Gamma_{\\mathrm{shear}}\\to-1$, the charge-``3'' Cosserat winding), and $Z_{\\mathrm{bulk}}=\\rho_{\\mathrm{bulk}}\\,c_{\\mathrm{bulk}}=\\sqrt{2}\\,\\rho_{\\mathrm{bulk}}\\,c_0$ at $K=2G$ ($\\Gamma_{\\mathrm{bulk}}\\to-1$, the mass-``3'' A1 dilatation) --- coupled through a chiral circulator and terminated at confinement surfaces. \\textbf{Mixed impedance domains:} only $Z_{\\mathrm{EM}}\\equiv Z_0$ is an \\emph{electrical} impedance ($\\Omega$); $Z_{\\mathrm{shear}}$ and $Z_{\\mathrm{bulk}}$ are \\emph{mechanical/acoustic} ($\\rho\\times$speed) and are \\emph{not} in $Z_0$ units (writing ``$Z_{\\mathrm{bulk}}=\\sqrt2\\,Z_0$'' is the electrical-vs-mechanical mis-scope the three-impedance law warns against). The channels are co-equal in role but in different domains, so EM$\\leftrightarrow$mechanical coupling requires a transducer, not a direct wire (the TKI-transformer, \\texttt{def-tk1xfm}: RATIFIED SOLID 2026-07-21, exact below the band edge $\\omega\\tau\\ll1$; identity-by-translation, \\emph{not} a derived mechanism), while the bulk$\\leftrightarrow$shear inter-grade coupling is the conserved $H_{\\mathrm{couple}}$. This is a \\textbf{consistency re-expression} of the three-impedance law, not a new substrate primitive (per \\textsc{invariant-n1} the network is the circuit model, not a substrate-object noun). Full content, the $\\mathcal{M},\\mathcal{J},\\mathcal{Q}$ map (the one-to-one correspondence does not hold), the forks, and the open-gate registry live in \\kbleaf{ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md} \\S6. The per-DOF node constitutive layer \\emph{beneath} the scalar cell --- each translation DOF an $(L_i,C_i)$ reactance, from which one circuit yields isotropic-co-scale achromaticity, deviatoric birefringence, and the $(q\\,\\ell_{\\mathrm{node}})$ dispersion tell --- is documented in \\kbleaf{ave-kb/vol9/ch3-pin-port-configuration/per-dof-vacuum-node-circuit.md}. \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_9_vacuum_datasheet/chapters/03a_device_circuit_models.tex:148 -- decl
    # :49, same explicit KEEP-BOTH sense (ii) reading as :79.
    ('manuscript/vol_9_vacuum_datasheet/chapters/03a_device_circuit_models.tex',
     "\\medskip\\noindent\\textbf{The two-port read at the electron (native-engine render).} The same A1-mass-``3'' / $T_2$-charge-``3'' two-port, evaluated at the electron, is the figure below: a \\textsc{consistency} re-expression of passing on-main engine output (\\texttt{\\seqsplit{src/scripts/vol\\_9\\_device/two\\_natured\\_electron\\_figure.py}}; every curve is actual engine output, no hand-drawn array). The charge is the deformation-invariant $(2,3)$ linking integer $\\mathcal{Q}=\\mathrm{Link}(\\partial\\Omega,F)=3$ ($\\alpha$-free, from \\texttt{compute\\_Q\\_link}; the $Q=137$ slot stays EMPTY), the mass is the $\\Gamma=-1$\\gammaundeclared{}-boundary-confined A1 dilatation cavity mode ($\\omega_{\\mathrm{fork\\,b}}=2.84$, lossless; mass $=$ A1 is the ratified grade-assignment of \\kbleaf{ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md}, not a driver measurement), and the real-space body is the topologically trivial $0_1$ unknot (the $(2,3)$ winding is a \\emph{phase-space} Clifford-torus winding, not a real-space knot). The two natures are \\textbf{orthogonal} ($A_1\\perp T_2$), not nested: the joint dynamical locus (a coupled bound mode / a phase-space orbit carrying the charge) tested NEGATIVE, so no binding curve is drawn. \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_9_vacuum_datasheet/chapters/04_dc_electrical_characteristics.tex:117
    # -- SELF-MATCH: the only declaration (:202) lies inside the dated EOF note THIS pass
    # appended; it fences nothing. Batch-1 named this class at
    # bulk_rarefaction_sector.py:129.
    ('manuscript/vol_9_vacuum_datasheet/chapters/04_dc_electrical_characteristics.tex',
     'Bulk-longitudinal & $Z_{\\mathrm{bulk}} = \\rho_{\\mathrm{bulk}}\\,c_{\\mathrm{bulk}}$ & $\\sqrt{2}\\,\\rho_{\\mathrm{bulk}}\\,c_0$ & $\\Gamma_{\\mathrm{bulk}} \\to -1$ \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]} \\\\'),
    # manuscript/vol_9_vacuum_datasheet/chapters/09_mechanical_characteristics.tex:61 --
    # decl :63 is the % SQRT(10/3) SCOPE TAG, which HOLDS the prior wording verbatim
    # inside the comment (:63-70); :61 carries the live current wording that replaced it.
    ('manuscript/vol_9_vacuum_datasheet/chapters/09_mechanical_characteristics.tex',
     '\\textbf{Bulk-modulus dilatational speed} $= \\sqrt{K_{vac}/\\rho_{bulk}} = \\sqrt{2}\\,c_0$ at $K=2G$ --- the A1-scalar port-mode (drops the $4G/3$ shear term), \\emph{not} the solid P-wave. Source: \\kbleaf{src/ave/core/constants.py} (\\texttt{V\\_LONG}); \\kbleaf{03a\\_device\\_circuit\\_models.tex}:106. See the P-wave row below. \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]} \\\\'),
    # manuscript/vol_9_vacuum_datasheet/chapters/09_mechanical_characteristics.tex:104 --
    # decl :63 as at :61 - the prior wording lives inside the comment, not on this line.
    ('manuscript/vol_9_vacuum_datasheet/chapters/09_mechanical_characteristics.tex',
     "\\textbf{Node-model channel tags (cross-reference to the 2-domain N-port).} The mechanical primitives above are the two CONFINED channels of the corrected graded-vacuum-impedance-network device model (Ch.~\\ref{ch:vol9_pin_port_configuration} \\S Device Circuit Models; canonical at \\kbleaf{device-circuit-models.md}:143--149). The \\textbf{bulk channel} carries the \\textbf{MASS-``3''} (the A1 dilatation: $m_e c^2$ = trapped acoustic compression energy), with mechanical impedance $Z_{bulk} = \\rho_{bulk}\\, c_{bulk} = \\sqrt{2}\\,\\rho_{bulk}\\, c_0$ at $K = 2G$ and $\\Gamma_{bulk} \\to -1$ (CONFINED). The \\textbf{shear channel} carries the \\textbf{CHARGE-``3''} (the orthogonal Cosserat $(2,3)$ micro-rotation winding; charge $=$ Beltrami helicity), with $Z_{shear} = \\rho_{bulk}\\, c_{shear}$ and $\\Gamma_{shear} \\to -1$ (CONFINED). The EM channel ($Z_{EM} \\equiv Z_0 = \\sqrt{\\mu_0/\\varepsilon_0} \\approx 376.73\\,\\Omega$, $\\Gamma_{EM} = 0$) is the sole external MATCHED radiative PORT --- not a mechanical primitive of this chapter, and crucially NOT in $Z_0$ units: $Z_{bulk}$ and $Z_{shear}$ are \\emph{mechanical/acoustic} impedances ($\\rho \\times$ speed, Pa$\\cdot$s/m), $\\sim$12 orders of magnitude off $Z_0$ and a unit change away --- writing ``$Z_{bulk} = \\sqrt{2}\\, Z_0$'' is the canonical electrical-vs-mechanical mis-scope (units discipline per \\kbleaf{device-circuit-models.md}:139). $A1 \\perp T2$: the mass (A1 dilatation) and charge/spin (Cosserat micro-rotation) grades are orthogonal, never wired into one shared $(V_{inc}, V_{ref})$ phasor (the two-``3''s fence, \\kbleaf{master-equation.md}:20). \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_9_vacuum_datasheet/chapters/09_mechanical_characteristics.tex:246 --
    # decl :63 as at :61, reached by the chapter container 185 lines away.
    ('manuscript/vol_9_vacuum_datasheet/chapters/09_mechanical_characteristics.tex',
     "The bulk-modulus dilatational mode $v_{bulk}=\\sqrt2\\,c_0$ (\\S\\ref{sec:vol9_mech_wave_speeds}) supports a discrete bound cavity mode when confined: the A1 dilatation breather, the mass-``3'' of the two-natured electron (Ch.~\\ref{ch:vol9_pin_port_configuration}; Fig.~\\ref{fig:vol9_two_natured_electron}). This section records its \\textbf{spatial mode spectrum} --- the FFT of the most-bound A1 eigenvector taken over the real-space \\emph{radial} coordinate (the mode's shape in space). It is a \\textsc{consistency}-class re-expression of the same on-main eigenvector used in Ch.~\\ref{ch:vol9_pin_port_configuration} (\\texttt{\\seqsplit{src/scripts/vol\\_9\\_device/a1\\_radial\\_fft.py}}; every array is actual engine output, not a new claim). \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_9_vacuum_datasheet/chapters/11_topological_characteristics.tex:40 --
    # decl :25 is the % T2-PHOTON FAMILY CORRECTION holding the prior wording verbatim
    # inside the comment; :40 is live prose.
    ('manuscript/vol_9_vacuum_datasheet/chapters/11_topological_characteristics.tex',
     "The group-theoretic foundation for the mass-vs-photon channel split is the K4 4-port irrep decomposition $V_{\\text{4-port}} = A_1 \\oplus T_2$ (canonical at \\kbleaf{ave-kb/vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md}): the K4-TLM scattering matrix $S = \\tfrac{1}{2}\\mathbf{1} - I$ has eigenvalues $\\{+1, -1, -1, -1\\}$, splitting into the $A_1$ scalar common-mode (longitudinal $u$, propagating at $\\sqrt{2}\\,c_0$ --- the mass / dilatation channel) and the $T_2$ traceless triplet (propagating at $c_0$). \\textbf{The label $T_2$ names two physically distinct objects} (\\texttt{def-t2ph01}; Grant ruling G2, 2026-07-03), separated by their massless-vs-gapped mass status: sense~(1) is the \\emph{massless transverse-translational $u$-family} --- \\textbf{this is the photon}; sense~(2) is the \\emph{gapped} Cosserat microrotational $\\boldsymbol{\\omega}$ family --- the home of the static $(2,3)$ winding and of the electron's bound massive mode at saturation --- which is \\emph{not} the photon. $A_1 \\perp T_2$ is the canonical orthogonality fence (\\kbleaf{master-equation.md}:20). \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_9_vacuum_datasheet/chapters/13_application_examples.tex:180 -- decl
    # :158 is the % def-tk1xfm STATUS FLIP holding prior wording inside the comment; decl
    # :64 'Z_0 is preserved interior-wide' is a physics sentence.
    ('manuscript/vol_9_vacuum_datasheet/chapters/13_application_examples.tex',
     "\\item \\textbf{Three wired reactance channels} (Ch.~\\ref{ch:vol9_pin_port_configuration} \\S Device Circuit Models; canonical at \\kbleaf{device-circuit-models.md}:141--149): the EM channel $Z_{EM} \\equiv Z_0 = \\sqrt{\\mu_0/\\varepsilon_0} \\approx 376.73\\,\\Omega$ ($\\Gamma_{EM} = 0$, matched), the shear channel $Z_{shear} = \\rho_{bulk}\\, c_{shear}$ ($\\Gamma_{shear} \\to -1$, confined --- the CHARGE-``3''), and the bulk channel $Z_{bulk} = \\sqrt{2}\\,\\rho_{bulk}\\, c_0$ at $K = 2G$ ($\\Gamma_{bulk} \\to -1$, confined --- the MASS-``3''). \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}"),
    # manuscript/vol_9_vacuum_datasheet/chapters/14_phase_diagrams.tex:28 -- decl :48
    # preserves a specific QUOTED passage ('supercooled pre-geodesic plasma') under the
    # 2026-08-06 carve - a different, identified quotation.
    ('manuscript/vol_9_vacuum_datasheet/chapters/14_phase_diagrams.tex',
     '\\item \\textbf{Bulk dilatation $\\bar\\rho$} (horizontal axis) --- the mean compression/rarefaction of the substrate relative to its cold-lattice reference. Rarefying $\\bar\\rho$ toward the EOS softening root drives the bulk (compressional) wave speed $c_{bulk}^2 \\to 0$, past which the medium can no longer support a compressional restoring force. \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}'),
    # manuscript/vol_9_vacuum_datasheet/chapters/16_cross_volume_reference.tex:86 -- SELF-
    # MATCH: the only declarations (:302, :338, :340) lie inside the dated EOF note THIS
    # pass appended; they fence nothing.
    ('manuscript/vol_9_vacuum_datasheet/chapters/16_cross_volume_reference.tex',
     '$v_{bulk}$ ($A_1$) & Bulk-modulus dilatational speed $\\sqrt{2}\\,c_0$ (A1-scalar port-mode; \\emph{not} the solid P-wave $c_L=\\sqrt{10/3}\\,c_0$ --- KEEP-BOTH, Ch.~9) & 9 & Vol 3 (derived-numerology); \\texttt{clm-uu1qbo} & \\kbleaf{src/ave/core/constants.py} \\texttt{V\\_LONG} \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]} \\\\'),
    # manuscript/vol_9_vacuum_datasheet/chapters/17_engine_requirements.tex:38 -- decl
    # :160 is an ADDITIVE test-status update tagged 'Rule-12 KEEP-BOTH, additive' - sense
    # (ii); it preserves nothing and governs the canaries it names.
    ('manuscript/vol_9_vacuum_datasheet/chapters/17_engine_requirements.tex',
     '1 & $c_{eff}(V)$ wave-speed modulation \\textbf{per sector} in the \\emph{propagation} step, not only $Z(V)$ at scatter & Ch.~\\ref{ch:vol9_ac_electrical_characteristics} \\S Temporal ($c_{EM}, c_{shear}, c_{bulk}$) & $Z(V)$-only-at-scatter engine: the saturation wall never engages ($\\Gamma = -1$\\gammaundeclared{} TIR wall never forms; no bound state) & \\kbleaf{substrate-native-check} \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]} \\\\'),
    # manuscript/vol_9_vacuum_datasheet/chapters/17_engine_requirements.tex:52 -- decl
    # :160, same additive KEEP-BOTH sense (ii) reading as :38.
    ('manuscript/vol_9_vacuum_datasheet/chapters/17_engine_requirements.tex',
     '12 & \\textbf{The medium must carry the DOF the excitation needs}: the transverse-only carrier ($2$ DOF) cannot host mass (L3 longitudinal) or charge (L4 micro-rotation); those need the full $6$-DOF Cosserat node & Ch.~\\ref{ch:vol9_pin_port_configuration} DOF table; Ch.~\\ref{ch:vol9_mechanical_characteristics} & The srs vector-TLM renders $2$ transverse DOF only (\\texttt{(N,degree,2)}); testing charge-genesis on a $2$-DOF carrier is structurally void (\\kbleaf{engine-capability-map}) & \\kbleaf{ave-representation-capability-check} \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]} \\\\'),
    # manuscript/vol_9_vacuum_datasheet/chapters/17_engine_requirements.tex:101 -- decl
    # :160, same additive KEEP-BOTH sense (ii) reading as :38.
    ('manuscript/vol_9_vacuum_datasheet/chapters/17_engine_requirements.tex',
     '(\\kbleaf{test\\_l3\\_mass\\_cage.py}), which extends past the valid-medium L0--L2 layers into the \\emph{bound longitudinal-bulk} (A1 scalar) cage --- the mass precursor. It \\textbf{POSITS} a saturated A1-scalar core (consistency-class; positing is legitimate --- it is not self-formation) and tests what the corpus says a bound electron-cage must exhibit. \\textbf{A1 SCALAR ONLY} throughout (\\texttt{converter\\_on=False} --- the two-3s guard, \\kbleaf{master-equation.md}:20: never read charge/spin/$\\mu$ off the scalar cage). The electron is the \\kbleaf{BoundResonator} instance-1 (\\kbleaf{electron-bound-resonator-coverage}). \\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}'),
    # manuscript/vol_9_vacuum_datasheet/figures/k4_irrep_decomposition.tex:38 -- decl :52
    # is the % RULING-21 CORRECTION holding the PRIOR node wording verbatim inside the
    # comment; :38 is the live TikZ node (and its stamp is a trailing % comment, so the
    # drawn figure is byte-unchanged in render terms).
    ('manuscript/vol_9_vacuum_datasheet/figures/k4_irrep_decomposition.tex',
     '{$A_1$ (1D, eigenvalue $+1$)\\\\basis $(1,1,1,1)/2$ — scalar / longitudinal\\\\$\\leftrightarrow$ translational $u$;\\;\\; speed $\\sqrt{2}\\,c_0$\\\\\\textbf{MASS / dilatation channel}};  % [DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION; dated note at the end of this file]'),
    # manuscript/vol_9_vacuum_datasheet/figures/k4_irrep_decomposition.tex:72 -- decl :52
    # as at :38 - prior wording held inside the comment; :72 is the live node.
    ('manuscript/vol_9_vacuum_datasheet/figures/k4_irrep_decomposition.tex',
     "{Op3 asymmetric \\emph{transduction} (RULED 2026-07-19): the $A_1$ \\emph{mode} empties into the $T_2$ irreps by lossless power-conserving scatter (Gauss's law forbids longitudinal EM in vacuum) --- mode-projection loss $\\neq$ system loss; $T_2$ settles into the quasi-stable photon pattern.};  % [DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION; dated note at the end of this file]"),
    # manuscript/vol_9_vacuum_datasheet/figures/moduli_relationship.tex:36 -- decl :14 is
    # the % K=2G PROVENANCE CORRECTION holding the prior node AND prior caption verbatim
    # inside the comment; :36 is the live node.
    ('manuscript/vol_9_vacuum_datasheet/figures/moduli_relationship.tex',
     '\\node[box, fill=orange!12] (pwave) at (5.4,0.3) {\\textbf{solid longitudinal P-wave}\\\\$c_L = \\sqrt{(K + 4G/3)/\\rho} = \\sqrt{10/3}\\,c_0$\\\\$\\approx 1.83\\,c_0$ (keeps the $4G/3$ term)};  % [DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION; dated note at the end of this file]'),
    # src/ave/core/observable_battery.py:539 -- decl :10 is a module-docstring KEEP-BOTH
    # in SENSE (ii) ('it redefines none'); preserves nothing.
    ('src/ave/core/observable_battery.py',
     'lam = (4.0 / 3.0) * G   # λ = K − ⅔G, with K = 2G (cfl_dt convention) → (4/3)G  [DEMOTED 2026-08-11 - R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]'),
    # src/ave/core/sonic_horizon_flow.py:22 -- decl :6 is the bare `Rule 12:` quote-and-
    # date form describing a PREDECESSOR result's gating - batch-1 spec-extension-2 class,
    # already adjudicated FP at this file.
    ('src/ave/core/sonic_horizon_flow.py',
     'no anti-restoring runaway). A `c=0` void is automatically a `Z_bulk=ρ·c→0`  [DEMOTED 2026-08-11 - R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]'),
    # src/ave/solvers/srs_cage_winding.py:313 -- SELF-MATCH: the only declaration (:512)
    # lies inside the dated EOF note THIS pass appended; it fences nothing.
    ('src/ave/solvers/srs_cage_winding.py',
     'self.a_A1 : (n_nodes,) complex  — the A1 bulk-dilatation breather (MASS).  [DEMOTED 2026-08-11 - R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]'),
})


if __name__ == "__main__":
    sys.exit(main())
