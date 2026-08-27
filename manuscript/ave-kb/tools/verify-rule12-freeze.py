#!/usr/bin/env python3
"""Rule-12 append-only GATE: machine freeze stamps + unstamped-note detector.

Rule 12 is the corpus's append-only discipline. Once a record is merged its body
is FROZEN; a correction is made by APPENDING a dated note, never by editing the
body. The rule is load-bearing precisely because an append-only violation cannot
be repaired after the fact -- once the body has been silently rewritten, the only
honest move left is to append a note admitting it.

Until this file existed the invariant was carried by a SENTENCE (a note claiming
"body above PRESERVED unedited") plus whoever bothered to re-prove it by hand.
A receipt is not a gate: an in-place edit above a frozen boundary broke nothing
that fired. This is the gate.


THE STAMP
---------
A Rule-12 note carries a machine-readable freeze stamp on its own line. It is an
HTML comment, so it renders invisibly in Markdown and in the rendered PDFs::

    <!-- rule12-freeze: base=<40-hex> region=above|below lines=<N> bytes=<M> sha256=<64-hex> -->

  ``base``    the 40-character commit SHA at which the frozen bytes are
              authoritative -- what the body ACTUALLY was when it was frozen.
  ``region``  which side of the stamp the frozen bytes are on. Both note shapes
              in this corpus are covered:
                * ``above`` -- the appended-dated-note shape ("body above
                  preserved verbatim"): the N lines immediately ABOVE the stamp.
                * ``below`` -- the retraction-banner shape (a red header at the
                  top of a record, "body preserved below"): the N lines
                  immediately BELOW the stamp.
  ``lines``   the extent of the frozen region in lines.
  ``bytes``   the extent of the same region in bytes.
  ``sha256``  SHA-256 of the exact bytes of that region.


WHY BOTH EXTENT UNITS, AND WHY A HASH ON TOP OF THEM
-----------------------------------------------------
Neither extent unit is exact on its own, and they fail in OPPOSITE directions:

  * A LINE COUNT is the unit a Markdown append actually happens in -- appending
    a note adds whole lines -- so it is the only unit in which "the boundary" is
    even well-defined, and it is robust to everything below the boundary. But it
    is BLIND above the boundary: a 42-line region stays 42 lines when a word,
    a number or a whole sentence inside it is rewritten in place. A line count
    alone would have missed the exact failure this gate exists to catch.
  * A BYTE COUNT moves under most within-line edits, so it covers the line
    count's blind spot -- but it does not locate a line boundary (you cannot say
    "append below line M-bytes-in" in a line-oriented format), and it is fooled
    by any EQUAL-LENGTH substitution: ``0.42`` -> ``0.43``, ``PASS`` -> ``FAIL``,
    ``+`` -> ``-``. Those are precisely the edits a rescue would make.

So the stamp carries all three and the check is EXACT, not tolerant:

  * ``sha256`` over the exact byte range carries the EXACTNESS. Nothing above
    is trusted to be sufficient; the hash is what actually decides.
  * ``lines`` LOCATES the boundary in the unit appends use, so a legitimate
    append is expressible and the gate can stay quiet under it.
  * ``bytes`` PINS the same boundary in the unit the hash is computed over.

Requiring all three is not belt-and-braces for its own sake -- it makes a red
gate DIAGNOSTIC instead of merely loud. The mismatch pattern names the failure:

    lines match, bytes differ                -> a within-line edit above the boundary
    lines differ                             -> a line inserted into / deleted from the region
    lines match, bytes match, sha differs    -> an equal-length substitution
    all three match, base blob disagrees     -> the stamp's base SHA is wrong/tampered

A gate that can only say "hash mismatch" invites the reader to assume the stamp
rotted. One that can say "42 lines both sides, 3 bytes shorter, first difference
at line 17" is naming a Rule-12 violation.


WHAT THE CHECK DOES, PER STAMP
------------------------------
  1. Extract EXACTLY ``lines`` lines on the stamp's declared side. Fewer
     available -> FAIL (the frozen region was truncated).
  2. Byte length must equal ``bytes``.
  3. SHA-256 must equal ``sha256``.
  4. ``base`` must resolve to a commit AND that commit must contain this path.
  5. The extracted byte run must occur as a CONTIGUOUS LINE-RUN in the file's
     blob at ``base``.

Step 5 is deliberately offset-tolerant and content-exact. Line numbers legally
move: appending a retraction banner at the TOP of a record (the sanctioned
Rule-12 shape) pushes every frozen body below it down. Anchoring the comparison
to a fixed line offset would turn that sanctioned move into a false red, and a
gate that cries wolf on the correct behaviour gets switched off. Anchoring it to
the exact BYTES makes the position irrelevant and the content non-negotiable:
the frozen run must still be there, contiguous, unedited, at ``base``. An
edge-deletion that would leave a shorter run contiguous is caught by (1)+(2)
before this step is reached.


THE UNSTAMPED-NOTE DETECTOR -- what makes this a gate and not a checklist
-------------------------------------------------------------------------
A checker that only validates stamped files is blind to the exact failure it
exists to prevent: a Rule-12 note that never got a stamp. Validating only what
volunteered to be validated is a checklist wearing a gate's clothes.

So the scan ALSO finds Rule-12 notes in PROSE and fails on any that no stamp
serves. The phrasings are SURVEYED from the corpus, not invented -- see
``NOTE_MARKERS`` / ``PRESERVE_VERBS`` / ``DIRECTION_WORDS`` below, each with the
live corpus shapes they were read off. A prose note is recognised when a
Rule-12 MARKER (``Rule 12`` / ``Rule-12`` / ``append-only``) co-occurs on one
line with a DIRECTIONAL PRESERVATION ASSERTION -- a preservation verb bound to
an ``above`` / ``below`` direction word.

The directional requirement is load-bearing and is not a convenience: a note
that does not say WHICH WAY its frozen body lies cannot be stamped at all, since
``region`` has no defensible value. It also separates a real freeze note from
the far more common MENTION of the rule (``Rule 12: retract, do not refill``,
``per Rule 12, git is the trail``, ``a Rule-12 sibling``), which asserts nothing
about bytes in the file it appears in. Measured over the tracked Markdown corpus
at the time of writing: 799 files mention Rule 12 in some form, 551 pair that
mention with some preservation word, and 267 carry a DIRECTIONAL preservation
assertion. Only the third set makes a claim a machine can check.

SERVED-BY-A-STAMP is per NOTE, not per file. A file with eight notes and one
stamp would pass a per-file rule while seven bodies went unguarded. A note at
line L is served when a stamp sits within ``SERVE_WINDOW`` lines of L with no
OTHER note line between them (the stamp belongs to its nearest note), or when L
falls inside some stamp's frozen region (a note that has itself been frozen by a
later note's stamp is already covered).


SCOPE, AND THE ALLOW-LIST
-------------------------
``rule12-freeze-config.json`` carries:

  ``enforced_globs``  where an unstamped prose note is a HARD FAIL. Outside it,
                      unstamped notes are COUNTED and PRINTED as a census, never
                      hidden -- an unenforced surface that is invisible is a
                      hole; one that prints its own size every build is a queue.
  ``allow_list``      narrowly scoped, per-ENTRY, each requiring ``path``,
                      ``match`` (a verbatim substring of the note line, so an
                      entry cannot silently widen to cover a different note),
                      ``class`` and ``reason``. An entry missing any of those is
                      itself a FAIL: an allow-list that accepts a bare path is a
                      mute button.

Allow-list ``class`` values are constrained (``ALLOWED_CLASSES``). One of them,
``known-pre-existing-violation``, exists because of the flag-don't-fix rule: a
record whose frozen body has ALREADY drifted must NOT be repaired in place --
repairing it would compound the violation by destroying the evidence. It is
recorded, its diff is preserved in the entry, and it is routed.


SCOPE HONESTY -- what this gate CANNOT catch
--------------------------------------------
  * **A body that drifted BEFORE it was stamped.** The backfill derives each
    stamp from git history rather than from prose, so a pre-existing drift is
    DETECTED at stamping time and routed -- but a stamp minted today can only
    freeze today's bytes forward. It cannot restore what was already lost.
  * **A note whose prose avoids every surveyed phrasing.** A freeze asserted in
    wording no corpus record has ever used is not recognised. The survey is
    reported (``--census``) so the recognised set stays auditable.
  * **A stamp whose ``base`` is a commit that itself already carried the drift.**
    The gate proves body-at-HEAD == body-at-base. If base is chosen after the
    damage, both sides agree and the gate is green on a corrupted body. This is
    why the backfill takes ``base`` from ``git blame`` on the NOTE LINE -- the
    commit that introduced the note -- and never from HEAD.
  * **Prose that lies about which body it froze.** ``region``/``lines`` are what
    the machine checks; a note claiming to freeze more than its stamp covers is
    an overclaim this gate does not adjudicate.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
REPO = TOOLS_DIR.parents[2]
CONFIG_PATH = TOOLS_DIR / "rule12-freeze-config.json"

#: How far from a prose note a stamp may sit and still be read as serving it.
#: A Rule-12 note is often a multi-line blockquote; the stamp goes on the line
#: after the block. 40 lines is generous for that and far short of the distance
#: between two notes in any record measured during the backfill.
SERVE_WINDOW = 40

# ---------------------------------------------------------------------------
# THE STAMP
# ---------------------------------------------------------------------------

STAMP_RE = re.compile(
    r"<!--\s*rule12-freeze:\s*"
    r"base=(?P<base>[0-9a-f]{40})\s+"
    r"region=(?P<region>above|below)\s+"
    r"lines=(?P<lines>\d+)\s+"
    r"bytes=(?P<bytes>\d+)\s+"
    r"sha256=(?P<sha>[0-9a-f]{64})\s*-->"
)

#: A line that LOOKS like a freeze stamp but does not parse. Caught separately
#: and hard, because a malformed stamp is indistinguishable from a real one to
#: a human reader and would otherwise be silently skipped -- which is how a gate
#: rots into a no-op that still looks guarded in the diff.
STAMPISH_RE = re.compile(r"<!--\s*rule12-freeze\b")


def stamp_text(base: str, region: str, lines: int, nbytes: int, sha: str) -> str:
    return (
        f"<!-- rule12-freeze: base={base} region={region} "
        f"lines={lines} bytes={nbytes} sha256={sha} -->"
    )


@dataclass(frozen=True)
class Stamp:
    path: str
    line: int          # 1-based line number of the stamp itself
    base: str
    region: str        # "above" | "below"
    lines: int
    nbytes: int
    sha: str

    @property
    def region_span(self) -> tuple[int, int]:
        """1-based inclusive [first, last] line span of the frozen region."""
        if self.region == "above":
            return (self.line - self.lines, self.line - 1)
        return (self.line + 1, self.line + self.lines)


def sha256_of(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def split_keepends(text: str) -> list[str]:
    """Lines WITH their terminators, so a region's bytes are exactly its bytes.

    ``str.splitlines()`` discards the newline, and re-joining with ``"\\n"``
    silently normalises a file whose last line has no terminator -- which would
    make the hash a function of the SPLITTER rather than of the file. The frozen
    region is a byte range; it is extracted as one.
    """
    return text.splitlines(keepends=True)


def region_bytes(lines_kept: list[str], span: tuple[int, int]) -> str | None:
    """Return the exact text of 1-based inclusive ``span``, or None if short."""
    first, last = span
    if first < 1 or last > len(lines_kept) or last < first:
        return None
    return "".join(lines_kept[first - 1 : last])


# ---------------------------------------------------------------------------
# THE PROSE-NOTE DETECTOR (phrasings SURVEYED from the corpus, not guessed)
# ---------------------------------------------------------------------------
#
# Surveyed 2026-08-26 over every tracked *.md on origin/main. The three
# component vocabularies below were read off the live corpus; the counts are the
# measured frequency of the joined directional assertion, top shapes:
#
#     97x "above preserved"          59x "below preserved"
#     40x "preserved below"          39x "above is preserved"
#     35x "below is preserved"       14x "preserved above"
#     10x "preserved verbatim below"  8x "preserved verbatim above"
#      6x "frozen body below"         5x "preserved unchanged below"
#      3x "above is left byte-untouched"
#      2x "preserved unedited above"  2x "above this line untouched"
#
# Live examples of the two note SHAPES this recognises, quoted verbatim:
#
#   region=above (appended dated note):
#     "> **🔴 CORRECTION 2026-08-02 (Rule 12 -- the original item-5 wording is
#      preserved in the sentence above ...)**"
#     "## G-RULING ADDENDUM (2026-06-14, Rule 12 -- body above preserved verbatim)"
#     "> **🔴 TWO-\"3\"s DISAMBIGUATION (2026-06-10, Rule 12 -- line above
#      PRESERVED unedited; pre-adjudicated, Grant-ratified).**"
#
#   region=below (retraction banner at the head of a record):
#     "> 🔴 **QED-NORMALIZATION CORRECTION (2026-07-03; Rule-12 -- body preserved
#      below, git is the trail).**"
#     "> **🔴 FLAGGED 2026-07-19 (... Rule-12 -- Protocol-10 text below
#      PRESERVED verbatim).**"

#: The rule marker. ``append-only`` is included because the corpus states the
#: invariant both by rule number and by name.
NOTE_MARKERS = re.compile(r"rule[\s\-]?12|append[\s\-]?only", re.IGNORECASE)

#: Preservation verbs, surveyed. ``frozen`` and ``intact`` are in because
#: "the frozen body below" / "left intact above" both occur.
PRESERVE_VERBS = (
    r"(?:preserv\w*|verbatim|unedited|untouched|byte-untouched|byte-identical"
    r"|not\s+edited|not\s+rewritten|frozen|intact)"
)

#: Direction words. A note that names no direction cannot be stamped (``region``
#: would have no defensible value), so it is not in the recognised class.
DIRECTION_WORDS = r"(?:above|below|preceding|following)"

#: The join: a preservation verb bound to a direction, either order, within a
#: short window so an unrelated "below" later in a long line cannot manufacture
#: a match.
_GAP = r"(?:\W+\w+){0,6}\W+"
DIRECTIONAL_ASSERTION = re.compile(
    rf"(?:{PRESERVE_VERBS}{_GAP}{DIRECTION_WORDS})|(?:{DIRECTION_WORDS}{_GAP}{PRESERVE_VERBS})",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Note:
    path: str
    line: int
    text: str

    def direction(self) -> str | None:
        """Which way the note says its frozen body lies, or None if ambiguous.

        Ambiguity is REPORTED, never guessed: a note that says both "above" and
        "below" in one line is exactly the case where an automated stamp would
        freeze the wrong bytes and then certify them forever.
        """
        m = DIRECTIONAL_ASSERTION.search(self.text)
        if not m:
            return None
        frag = m.group(0).lower()
        has_above = re.search(r"\b(?:above|preceding)\b", frag) is not None
        has_below = re.search(r"\b(?:below|following)\b", frag) is not None
        if has_above and not has_below:
            return "above"
        if has_below and not has_above:
            return "below"
        return None


def find_notes(path: str, text: str) -> list[Note]:
    out: list[Note] = []
    for i, line in enumerate(text.splitlines(), 1):
        if STAMPISH_RE.search(line):
            continue  # the stamp itself is not a prose note
        if NOTE_MARKERS.search(line) and DIRECTIONAL_ASSERTION.search(line):
            out.append(Note(path, i, line.rstrip("\n")))
    return out


def find_stamps(path: str, text: str) -> tuple[list[Stamp], list[str]]:
    """Parse stamps; a stamp-SHAPED line that does not parse is a hard finding."""
    stamps: list[Stamp] = []
    problems: list[str] = []
    for i, line in enumerate(text.splitlines(), 1):
        if not STAMPISH_RE.search(line):
            continue
        m = STAMP_RE.search(line)
        if not m:
            problems.append(
                f"{path}:{i}: MALFORMED freeze stamp -- looks like a rule12-freeze "
                f"stamp but does not parse. A stamp a machine skips is worse than no "
                f"stamp: it reads as guarded. Required form:\n"
                f"    {stamp_text('<40-hex>', 'above|below', 0, 0, '<64-hex>')}\n"
                f"  got: {line.strip()}"
            )
            continue
        stamps.append(
            Stamp(
                path=path,
                line=i,
                base=m.group("base"),
                region=m.group("region"),
                lines=int(m.group("lines")),
                nbytes=int(m.group("bytes")),
                sha=m.group("sha"),
            )
        )
    return stamps, problems


# ---------------------------------------------------------------------------
# GIT ACCESS
# ---------------------------------------------------------------------------


class GitError(RuntimeError):
    pass


def git_out(args: list[str], repo: Path) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=repo, capture_output=True, text=True, check=False
    )
    if proc.returncode != 0:
        raise GitError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout


def blob_at(repo: Path, commit: str, path: str) -> str | None:
    """File content at ``commit``, or None if the commit or the path is absent."""
    try:
        return git_out(["cat-file", "-p", f"{commit}:{path}"], repo)
    except GitError:
        return None


def commit_exists(repo: Path, commit: str) -> bool:
    try:
        kind = git_out(["cat-file", "-t", commit], repo).strip()
    except GitError:
        return False
    return kind == "commit"


# ---------------------------------------------------------------------------
# PER-STAMP VERIFICATION
# ---------------------------------------------------------------------------


def _contiguous_run_index(haystack: list[str], needle: list[str]) -> int:
    """Index of ``needle`` as a contiguous line-run in ``haystack``, else -1."""
    n = len(needle)
    if n == 0 or n > len(haystack):
        return -1
    first = needle[0]
    for i in range(len(haystack) - n + 1):
        if haystack[i] == first and haystack[i : i + n] == needle:
            return i
    return -1


def _first_difference(base_lines: list[str], live_lines: list[str]) -> tuple[int, str, str]:
    """First differing line between the two runs, aligned from the top.

    Returns (1-based offset within the region, base line, live line). Alignment
    is from the region's start because that is where a stamp anchors; a shifted
    region is reported as a difference at the shift point, which is the honest
    reading -- the bytes at that offset are not what was frozen.
    """
    for k in range(max(len(base_lines), len(live_lines))):
        b = base_lines[k] if k < len(base_lines) else "<region ends>"
        v = live_lines[k] if k < len(live_lines) else "<region ends>"
        if b != v:
            return (k + 1, b.rstrip("\n"), v.rstrip("\n"))
    return (0, "", "")


def _best_alignment(base_all: list[str], live: list[str]) -> list[str]:
    """The window of ``base_all`` that best matches ``live``, for diagnosis only.

    Picked by longest common prefix with ``live``; ties go to the earliest
    window. Used ONLY to say WHERE the first difference is -- never to decide
    pass/fail, which is settled by the exact contiguous-run search above.
    """
    n = len(live)
    if n == 0 or not base_all:
        return []
    best_i, best_score = 0, -1
    for i in range(max(1, len(base_all) - n + 1)):
        window = base_all[i : i + n]
        score = 0
        for a, b in zip(window, live):
            if a != b:
                break
            score += 1
        if score > best_score:
            best_i, best_score = i, score
    return base_all[best_i : best_i + n]


def verify_stamp(repo: Path, stamp: Stamp, live_text: str) -> list[str]:
    """Return findings for one stamp; empty list == the frozen region is intact."""
    findings: list[str] = []
    live_lines = split_keepends(live_text)
    span = stamp.region_span

    if stamp.lines <= 0:
        return [
            f"{stamp.path}:{stamp.line}: freeze stamp declares lines={stamp.lines} -- "
            f"a zero-extent freeze region certifies nothing and would pass forever."
        ]

    live_region = region_bytes(live_lines, span)
    if live_region is None:
        short_by = (1 - span[0]) if span[0] < 1 else (span[1] - len(live_lines))
        return [
            f"{stamp.path}:{stamp.line}: FROZEN REGION TRUNCATED -- the stamp declares "
            f"region={stamp.region} lines={stamp.lines}, but only {stamp.lines - short_by} "
            f"line(s) exist {stamp.region} the stamp in a {len(live_lines)}-line file "
            f"(the region would run to line {span[0] if span[0] < 1 else span[1]}). "
            f"{short_by} line(s) are GONE from the frozen body."
        ]

    live_bytes = len(live_region.encode("utf-8"))
    live_sha = sha256_of(live_region)

    if live_bytes != stamp.nbytes:
        findings.append(
            f"{stamp.path}:{stamp.line}: BYTE-EXTENT DRIFT -- stamp says bytes="
            f"{stamp.nbytes}, the {stamp.lines} line(s) {stamp.region} the stamp measure "
            f"{live_bytes} ({live_bytes - stamp.nbytes:+d}). The line count cannot move here "
            f"(exactly lines={stamp.lines} are read), so this is the extent signal a "
            f"line-count-only stamp is BLIND to. Three causes fit and the base-commit "
            f"comparison below discriminates: a WITHIN-LINE edit inside the region; the "
            f"region window SLIDING because lines were inserted/removed on the stamp's other "
            f"side; or the stamp's own `bytes` field being wrong."
        )
    if live_sha != stamp.sha:
        findings.append(
            f"{stamp.path}:{stamp.line}: HASH MISMATCH in the frozen region "
            f"(span {span[0]}-{span[1]}, region={stamp.region}, lines={stamp.lines})\n"
            f"    expected sha256 = {stamp.sha}\n"
            f"    actual   sha256 = {live_sha}"
        )
    return findings + _verify_against_base(repo, stamp, live_region, findings)


def _verify_against_base(
    repo: Path, stamp: Stamp, live_region: str, already: list[str]
) -> list[str]:
    """The half that makes the stamp a FREEZE and not a self-consistent checksum.

    Without this, ``sha256`` only says "these bytes hash to what this line says
    they hash to" -- and an editor who rewrites the body can recompute the hash.
    Comparing against the blob at ``base`` is what pins the bytes to HISTORY,
    which no working-tree edit can rewrite.
    """
    findings: list[str] = []

    if not commit_exists(repo, stamp.base):
        return [
            f"{stamp.path}:{stamp.line}: UNRESOLVABLE BASE -- base={stamp.base} is not a "
            f"commit in this repository. The freeze is anchored to nothing."
        ]

    base_text = blob_at(repo, stamp.base, stamp.path)
    if base_text is None:
        return [
            f"{stamp.path}:{stamp.line}: BASE COMMIT DOES NOT CONTAIN THIS PATH -- "
            f"base={stamp.base} resolves, but `{stamp.path}` does not exist there. Either "
            f"the base SHA is wrong/tampered or the record was renamed after freezing "
            f"(rename the stamp's base to a commit that carries the path)."
        ]

    base_lines = split_keepends(base_text)
    live_lines = split_keepends(live_region)

    if _contiguous_run_index(base_lines, live_lines) >= 0:
        if already:
            # Region matches history but not its own declared extent/hash: the
            # STAMP is stale, not the body. Say so, so the fix is not a rewrite.
            findings.append(
                f"{stamp.path}:{stamp.line}: (diagnosis) the region's bytes ARE present "
                f"verbatim at base={stamp.base[:12]} -- so the BODY is intact and the "
                f"STAMP's own extent/hash fields are what disagree. Recompute the stamp; "
                f"do NOT touch the body."
            )
        return findings

    aligned = _best_alignment(base_lines, live_lines)
    off, base_line, live_line = _first_difference(aligned, live_lines)
    span = stamp.region_span
    findings.append(
        f"{stamp.path}:{stamp.line}: *** RULE-12 VIOLATION -- the frozen region is NOT "
        f"byte-identical to `{stamp.path}` at base={stamp.base}.\n"
        f"    region      : {stamp.region}, lines {span[0]}-{span[1]} ({stamp.lines} lines, "
        f"{stamp.nbytes} bytes as stamped)\n"
        f"    expected sha: {stamp.sha}\n"
        f"    actual   sha: {sha256_of(live_region)}\n"
        f"    first differing line: offset {off} inside the frozen region "
        f"= line {span[0] + off - 1} of the file\n"
        f"      at base : {base_line[:200]}\n"
        f"      in tree : {live_line[:200]}\n"
        f"    Rule 12 is APPEND-ONLY: a body already merged is corrected by APPENDING a "
        f"dated note, never by editing it. Do NOT 'fix' the body to make this pass -- "
        f"that compounds the violation by destroying the evidence. Append a note, and "
        f"route the drift."
    )
    return findings


# ---------------------------------------------------------------------------
# CONFIG: SCOPE + ALLOW-LIST
# ---------------------------------------------------------------------------

#: Allow-list classes. A free-text class would let any entry justify itself; a
#: closed set forces each exemption into a named category a reviewer can audit.
ALLOWED_CLASSES = {
    "known-pre-existing-violation": (
        "the frozen body has ALREADY drifted. NOT repaired -- repairing it in place "
        "would compound the Rule-12 violation by destroying the evidence. The entry "
        "carries the diff and the routing."
    ),
    "not-a-freeze-note": (
        "the line matches the detector's phrasing but asserts nothing about bytes in "
        "THIS file -- e.g. a survey/triage doc quoting another record's note, or a "
        "convention doc describing the rule."
    ),
    "direction-not-determinable": (
        "the note names both directions (or neither) in one line, so `region` has no "
        "defensible value. Needs the record's author, not a guess."
    ),
    "generated-artifact": (
        "the file is generated, so a stamp would be rewritten by its generator."
    ),
}

REQUIRED_ENTRY_FIELDS = ("path", "match", "class", "reason")


@dataclass
class Config:
    enforced_globs: list[str]
    allow_list: list[dict]
    pending_on_landing: list[dict]

    def enforced(self, path: str) -> bool:
        return any(fnmatch.fnmatch(path, g) for g in self.enforced_globs)


def load_config(path: Path) -> tuple[Config, list[str]]:
    problems: list[str] = []
    raw = json.loads(path.read_text(encoding="utf-8"))
    entries = raw.get("allow_list", [])
    for idx, e in enumerate(entries):
        missing = [f for f in REQUIRED_ENTRY_FIELDS if not str(e.get(f, "")).strip()]
        if missing:
            problems.append(
                f"{path.name}: allow_list[{idx}] is missing required field(s) "
                f"{missing}. An allow-list entry without a verbatim `match` and a stated "
                f"`reason` is a mute button, not an exemption."
            )
        cls = e.get("class")
        if cls is not None and cls not in ALLOWED_CLASSES:
            problems.append(
                f"{path.name}: allow_list[{idx}] class={cls!r} is not one of "
                f"{sorted(ALLOWED_CLASSES)}."
            )
    cfg = Config(
        enforced_globs=list(raw.get("enforced_globs", [])),
        allow_list=entries,
        pending_on_landing=list(raw.get("pending_stamp_on_landing", [])),
    )
    if not cfg.enforced_globs:
        problems.append(
            f"{path.name}: enforced_globs is EMPTY -- the gate would enforce nothing "
            f"while still printing OK. An empty scope is a failure, never a pass."
        )
    return cfg, problems


def allowed(cfg: Config, note: Note) -> dict | None:
    """The allow-list entry covering this note, if any.

    Matching is BY PATH AND BY VERBATIM SUBSTRING of the note line, so an entry
    written for one note cannot silently widen to cover a different note that
    appears in the same file later.
    """
    for e in cfg.allow_list:
        if e.get("path") == note.path and str(e.get("match", "")) in note.text:
            return e
    return None


# ---------------------------------------------------------------------------
# SERVED-BY-A-STAMP
# ---------------------------------------------------------------------------


def served_by(note: Note, stamps: list[Stamp], notes: list[Note]) -> Stamp | None:
    """Which stamp serves ``note``, or None.

    A stamp serves the note NEAREST to it: within ``SERVE_WINDOW`` lines, with no
    other note line between the two. A note that lies inside some stamp's frozen
    region is also served -- it has already been frozen by a later note's stamp.
    """
    for s in stamps:
        lo, hi = s.region_span
        if lo <= note.line <= hi:
            return s
    other = [n.line for n in notes if n.line != note.line]
    best: Stamp | None = None
    best_d = SERVE_WINDOW + 1
    for s in stamps:
        d = abs(s.line - note.line)
        if d > SERVE_WINDOW:
            continue
        lo, hi = min(s.line, note.line), max(s.line, note.line)
        if any(lo < m < hi for m in other):
            continue
        if d < best_d:
            best, best_d = s, d
    return best


# ---------------------------------------------------------------------------
# THE SCAN
# ---------------------------------------------------------------------------


@dataclass
class ScanReport:
    failures: list[str]
    advisories: list[str]
    n_files: int = 0
    n_stamps: int = 0
    n_notes: int = 0
    n_notes_enforced: int = 0
    n_notes_served: int = 0
    n_notes_allowed: int = 0
    census_unstamped: list[Note] = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.census_unstamped is None:
            self.census_unstamped = []


def tracked_markdown(repo: Path) -> list[str]:
    out = git_out(["ls-files", "-z", "--", "*.md"], repo)
    return [p for p in out.split("\0") if p]


def scan(repo: Path, cfg: Config, paths: list[str] | None = None) -> ScanReport:
    rep = ScanReport(failures=[], advisories=[])
    files = paths if paths is not None else tracked_markdown(repo)
    for rel in files:
        fp = repo / rel
        try:
            text = fp.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        rep.n_files += 1

        stamps, stamp_problems = find_stamps(rel, text)
        rep.failures.extend(stamp_problems)
        rep.n_stamps += len(stamps)

        # (a) every stamp's frozen region must still be what it froze
        for s in stamps:
            rep.failures.extend(verify_stamp(repo, s, text))

        # (b) every prose note must be served by a stamp
        notes = find_notes(rel, text)
        rep.n_notes += len(notes)
        enforced = cfg.enforced(rel)
        for n in notes:
            if enforced:
                rep.n_notes_enforced += 1
            entry = allowed(cfg, n)
            if entry is not None:
                rep.n_notes_allowed += 1
                rep.advisories.append(
                    f"{n.path}:{n.line}: ALLOW-LISTED [{entry['class']}] {entry['reason']}"
                )
                continue
            if served_by(n, stamps, notes) is not None:
                rep.n_notes_served += 1
                continue
            if enforced:
                rep.failures.append(
                    f"{n.path}:{n.line}: UNSTAMPED RULE-12 NOTE -- this line asserts a "
                    f"frozen body in prose but no machine freeze stamp serves it, so "
                    f"nothing would fire if that body were edited.\n"
                    f"    note: {n.text.strip()[:200]}\n"
                    f"    fix : add a stamp adjacent to the note --\n"
                    f"          {stamp_text('<40-hex>', n.direction() or 'above|below', 0, 0, '<64-hex>')}\n"
                    f"          `--backfill --path {n.path}` computes it from git history.\n"
                    f"    or  : add a narrowly-scoped entry to {CONFIG_PATH.name} with a "
                    f"`match` substring, a `class` and a `reason`."
                )
            else:
                rep.census_unstamped.append(n)
    return rep


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

TAG = "[rule12]"


def report(rep: ScanReport, cfg: Config, census: bool) -> int:
    for a in rep.advisories:
        print(f"{TAG} advisory  {a}")
    for f in rep.failures:
        print(f"{TAG} FAIL  {f}")

    n_census = len(rep.census_unstamped)
    print(
        f"{TAG} scanned {rep.n_files} tracked Markdown file(s): "
        f"{rep.n_stamps} freeze stamp(s), {rep.n_notes} prose Rule-12 note(s) "
        f"({rep.n_notes_enforced} in enforced scope)."
    )
    print(
        f"{TAG} notes served by a stamp: {rep.n_notes_served}  "
        f"allow-listed: {rep.n_notes_allowed}  "
        f"outside enforced scope (census, non-gating): {n_census}"
    )
    if n_census:
        print(
            f"{TAG} the census is PRINTED, not hidden: an unenforced surface that is "
            f"invisible is a hole; one that prints its own size every build is a queue. "
            f"Run with --census to list it."
        )
    if census:
        for n in rep.census_unstamped:
            print(f"{TAG} census   {n.path}:{n.line}  {n.text.strip()[:160]}")
    for p in cfg.pending_on_landing:
        print(
            f"{TAG} pending  {p.get('path')} -- {p.get('reason')} "
            f"(owner: {p.get('owner', 'unassigned')})"
        )

    if rep.failures:
        print(f"{TAG} {len(rep.failures)} finding(s) -- the append-only invariant is NOT proven.")
        return 1
    print(
        f"{TAG} OK -- every freeze stamp's region is byte-identical to its base commit, "
        f"and every Rule-12 prose note in enforced scope is served by a stamp."
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Rule-12 append-only gate.")
    ap.add_argument("--repo", default=str(REPO), help="repository root")
    ap.add_argument("--config", default=str(CONFIG_PATH))
    ap.add_argument("--census", action="store_true",
                    help="list every out-of-scope unstamped note (non-gating)")
    ap.add_argument("--path", action="append", default=None,
                    help="limit the scan to these repo-relative paths (repeatable)")
    ap.add_argument("--backfill", action="store_true",
                    help="derive stamps from git history and WRITE them (see --dry-run)")
    ap.add_argument("--dry-run", action="store_true",
                    help="with --backfill: print what would be written, change nothing")
    ap.add_argument("--mutation-receipt", action="store_true",
                    help="prove the gate can both FIRE and STAY QUIET, on synthetic fixtures")
    args = ap.parse_args(argv)

    if args.mutation_receipt:
        return mutation_receipt()

    repo = Path(args.repo).resolve()
    cfg, cfg_problems = load_config(Path(args.config))
    if cfg_problems:
        for p in cfg_problems:
            print(f"{TAG} FAIL  {p}")
        return 1

    if args.backfill:
        return backfill(repo, cfg, args.path, dry_run=args.dry_run)

    rep = scan(repo, cfg, args.path)
    return report(rep, cfg, args.census)


# ---------------------------------------------------------------------------
# BACKFILL -- stamps derived from GIT HISTORY, never from prose
# ---------------------------------------------------------------------------
#
# A stamp minted from what a note CLAIMS ("body above preserved verbatim") would
# certify the claim rather than check it. So the backfill asks git instead:
#
#   1. `git blame` the NOTE LINE -> the commit that put it there. That commit is
#      the freeze event. (`base` is never HEAD. A stamp whose base is HEAD says
#      "today's bytes equal today's bytes" and is green on a body that was
#      corrupted yesterday.)
#   2. Locate the same note line in that commit's blob.
#   3. Walk OUTWARD from the note, one line at a time, comparing the working
#      tree against the base blob, and stop at the first difference. The run
#      that matched is what is PROVABLY still frozen -- which may be less than
#      the note claims. The stamp records the run, not the claim.
#   4. Cap the walk at the neighbouring Rule-12 note, so consecutive notes TILE
#      the record instead of overlapping: each note guards the body between it
#      and its neighbour, and every byte between the oldest note and the newest
#      is covered by exactly one stamp.
#
# When the walk stops SHORT of the cap, the difference is CLASSIFIED rather than
# assumed, because two very different things can stop it:
#
#   * INSERT-ONLY (lines added, none changed or removed) -- legitimate. Adding a
#     dated banner is the sanctioned Rule-12 move and it shifts every line below
#     it. Treating that as a violation would make the gate cry wolf on correct
#     behaviour, which is how gates get switched off.
#   * REPLACE or DELETE -- a body that was EDITED or had content REMOVED. That
#     is a live Rule-12 violation. It is REPORTED WITH ITS DIFF and NOT REPAIRED
#     (flag-don't-fix: repairing it in place would compound the violation by
#     destroying the evidence).

import difflib  # noqa: E402 -- kept beside the only section that uses it


def blame_map(repo: Path, path: str) -> dict[int, str]:
    """1-based line -> commit SHA that last touched it, for one file."""
    try:
        out = git_out(["blame", "--line-porcelain", "--", path], repo)
    except GitError:
        return {}
    mapping: dict[int, str] = {}
    for line in out.splitlines():
        m = re.match(r"^([0-9a-f]{40}) \d+ (\d+)(?: \d+)?$", line)
        if m:
            mapping[int(m.group(2))] = m.group(1)
    return mapping


def note_block_end(lines: list[str], start: int) -> int:
    """1-based line of the last line of the note block beginning at ``start``.

    A Rule-12 note is usually a Markdown blockquote spanning several lines. The
    block is the maximal run of ``>``-prefixed lines when the note line is one;
    otherwise the note line alone.
    """
    if not lines[start - 1].lstrip().startswith(">"):
        return start
    end = start
    while end < len(lines) and lines[end].lstrip().startswith(">"):
        end += 1
    return end


@dataclass
class Backfilled:
    note: Note
    base: str
    region: str
    span_lines: list[str]     # exact frozen lines (keepends)
    insert_at: int            # 1-based line the stamp is inserted BEFORE
    capped_at: str            # what stopped the walk
    drift: str | None         # non-None == a live Rule-12 violation candidate


def _classify_stop(base_seg: list[str], head_seg: list[str]) -> str | None:
    """None if the segments differ only by INSERTIONS; else a diff description."""
    sm = difflib.SequenceMatcher(a=base_seg, b=head_seg, autojunk=False)
    bad: list[str] = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "replace":
            bad.append(
                f"      REPLACED at base offset {i1 + 1}:\n"
                f"        was: {''.join(base_seg[i1:i2])[:240].rstrip()}\n"
                f"        now: {''.join(head_seg[j1:j2])[:240].rstrip()}"
            )
        elif tag == "delete":
            bad.append(
                f"      DELETED at base offset {i1 + 1}:\n"
                f"        was: {''.join(base_seg[i1:i2])[:240].rstrip()}"
            )
    return "\n".join(bad) if bad else None


def derive_stamp(
    repo: Path, note: Note, head_lines: list[str], notes: list[Note], blame: dict[int, str]
) -> tuple[Backfilled | None, str | None]:
    """Derive one note's stamp from history. Returns (stamp, reason-if-skipped)."""
    direction = note.direction()
    if direction is None:
        return None, "direction not determinable from the note line (says both, or neither)"

    base = blame.get(note.line)
    if not base:
        return None, "git blame produced no commit for the note line"

    base_text = blob_at(repo, base, note.path)
    if base_text is None:
        return None, f"path absent from the blamed commit {base[:12]} (renamed?)"
    base_lines = split_keepends(base_text)

    target = head_lines[note.line - 1]
    positions = [i + 1 for i, ln in enumerate(base_lines) if ln == target]
    if not positions:
        return None, f"the note line is not byte-present in its blamed commit {base[:12]}"
    b_line = min(positions, key=lambda p: abs(p - note.line))

    other = sorted(n.line for n in notes if n.line != note.line)

    if direction == "above":
        cap = max([m for m in other if m < note.line], default=0)
        insert_at = note.line
        h_idx, b_idx = note.line - 1, b_line - 1          # 0-based, exclusive end
        run: list[str] = []
        while h_idx - 1 >= cap and b_idx - 1 >= 0 and head_lines[h_idx - 1] == base_lines[b_idx - 1]:
            run.append(head_lines[h_idx - 1])
            h_idx -= 1
            b_idx -= 1
        run.reverse()
        stopped_by_cap = (h_idx <= cap)
        base_seg = base_lines[max(0, b_idx - 200) : b_idx]
        head_seg = head_lines[max(cap, h_idx - 200) : h_idx]
    else:
        h_end = note_block_end(head_lines, note.line)
        b_end = b_line + (h_end - note.line)
        nxt = min([m for m in other if m > note.line], default=len(head_lines) + 1)
        insert_at = h_end + 1
        h_idx, b_idx = h_end, b_end                        # 0-based start of body
        run = []
        while h_idx < nxt - 1 and b_idx < len(base_lines) and head_lines[h_idx] == base_lines[b_idx]:
            run.append(head_lines[h_idx])
            h_idx += 1
            b_idx += 1
        stopped_by_cap = (h_idx >= nxt - 1)
        base_seg = base_lines[b_idx : b_idx + 200]
        head_seg = head_lines[h_idx : min(nxt - 1, h_idx + 200)]

    if not run:
        return None, (
            f"ZERO provably-frozen lines adjacent to the note (base {base[:12]}): the very "
            f"line next to it already differs from history"
        )

    drift = None if stopped_by_cap else _classify_stop(base_seg, head_seg)
    capped = "neighbouring Rule-12 note / file edge" if stopped_by_cap else "content divergence"
    return (
        Backfilled(
            note=note,
            base=base,
            region=direction,
            span_lines=run,
            insert_at=insert_at,
            capped_at=capped,
            drift=drift,
        ),
        None,
    )


def backfill(repo: Path, cfg: Config, paths: list[str] | None, dry_run: bool) -> int:
    files = paths if paths is not None else tracked_markdown(repo)
    n_written = n_files = n_skipped = 0
    drifts: list[str] = []
    skips: list[str] = []

    for rel in sorted(files):
        fp = repo / rel
        try:
            text = fp.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if not cfg.enforced(rel):
            continue
        notes = find_notes(rel, text)
        if not notes:
            continue
        stamps, _ = find_stamps(rel, text)
        todo = [n for n in notes
                if served_by(n, stamps, notes) is None and allowed(cfg, n) is None]
        if not todo:
            continue

        head_lines = split_keepends(text)
        blame = blame_map(repo, rel)
        derived: list[Backfilled] = []
        for n in todo:
            bf, why = derive_stamp(repo, n, head_lines, notes, blame)
            if bf is None:
                n_skipped += 1
                skips.append(f"{n.path}:{n.line}: SKIPPED -- {why}\n    note: {n.text.strip()[:180]}")
                continue
            derived.append(bf)
            if bf.drift:
                drifts.append(
                    f"*** DRIFT: {n.path}:{n.line} -- the body this note froze at "
                    f"{bf.base[:12]} has CHANGED since. Only the {len(bf.span_lines)} "
                    f"line(s) adjacent to the note are provably still frozen; beyond that:\n"
                    f"{bf.drift}\n"
                    f"    NOT REPAIRED (flag-don't-fix). Route it; add a "
                    f"`known-pre-existing-violation` allow-list entry carrying this diff."
                )

        if not derived:
            continue

        # Bottom-up so an insertion never invalidates a lower line number.
        out = list(head_lines)
        for bf in sorted(derived, key=lambda b: b.insert_at, reverse=True):
            body = "".join(bf.span_lines)
            line = stamp_text(
                bf.base, bf.region, len(bf.span_lines), len(body.encode("utf-8")),
                sha256_of(body),
            )
            out.insert(bf.insert_at - 1, line + "\n")
            n_written += 1
            print(
                f"{TAG} stamp    {rel}:{bf.note.line} region={bf.region} "
                f"lines={len(bf.span_lines)} base={bf.base[:12]} (stopped by {bf.capped_at})"
            )
        n_files += 1
        if not dry_run:
            fp.write_text("".join(out), encoding="utf-8")

    for s in skips:
        print(f"{TAG} skip     {s}")
    for d in drifts:
        print(f"{TAG} {d}")
    print(
        f"{TAG} backfill{' (DRY RUN -- nothing written)' if dry_run else ''}: "
        f"{n_written} stamp(s) across {n_files} file(s); "
        f"{n_skipped} note(s) skipped; {len(drifts)} DRIFTED bod(y/ies) found."
    )
    return 0


# ---------------------------------------------------------------------------
# MUTATION RECEIPT -- both directions, on SYNTHETIC fixtures
# ---------------------------------------------------------------------------
#
# A gate that cannot fire is worse than no gate: it manufactures confidence.
# Every arm below either CATCHES a perturbation that must be caught or stays
# STABLE under a change that must not matter, and the mode exits non-zero if any
# arm behaves the other way.
#
# The can-it-STAY-QUIET arms are not padding. A gate that reds on the sanctioned
# Rule-12 move -- appending a dated note below a frozen body -- gets switched off
# within a week, and a switched-off gate protects nothing. The inverse class is
# the one most receipts omit, so it is built first here and it is the arm this
# fixture's structure is designed around.
#
# THE FIXTURES ENCODE NO AUTHORING CONTEXT. They are a throwaway git repository
# with invented content: no live line numbers from this tree, no dependence on
# the current branch's shape, no hash of this file's own source. Everything the
# receipt asserts is a property of the ALGORITHM, reproducible on a machine that
# has never seen this repository.

FIXTURE_BODY = """# Synthetic Record -- Widget Impedance Walk

## 1. Setup

The widget is driven at 400 Hz through a series reactance.
Measured: the port returns 12.5 ohm at the first crossing.

## 2. Result

The crossing is REPRODUCED on both benches.
Verdict: CONFIRMED.
"""

FIXTURE_OTHER = """# A File With No Rule-12 Note At All

Nothing here freezes anything. Editing it must not move the gate.
Second line of ordinary prose.
"""

FIXTURE_NOTE_1 = (
    "> **CORRECTION 2031-02-02 (Rule 12 -- the body above is PRESERVED unedited; "
    "git is the trail).** The 12.5 ohm reading was taken at the wrong port.\n"
)
FIXTURE_NOTE_2 = (
    "> **SECOND CORRECTION 2031-03-03 (Rule 12 -- everything above is preserved "
    "verbatim).** And the bench-two repeat used a different fixture.\n"
)


def _fx_git(tmp: Path, *args: str) -> str:
    return git_out(
        ["-c", "user.email=receipt@example.invalid", "-c", "user.name=receipt", *args], tmp
    )


def _fx_stamp_above(tmp: Path, rel: str, base: str, upto: int, insert_at: int) -> None:
    """Insert a correctly-derived region=above stamp before line ``insert_at``."""
    lines = split_keepends((tmp / rel).read_text(encoding="utf-8"))
    body = "".join(lines[insert_at - 1 - upto : insert_at - 1])
    line = stamp_text(base, "above", upto, len(body.encode("utf-8")), sha256_of(body))
    lines.insert(insert_at - 1, line + "\n")
    (tmp / rel).write_text("".join(lines), encoding="utf-8")


def _fx_build(tmp: Path) -> tuple[str, str, str]:
    """Build the fixture repo. Returns (c_pre, c_body, c_frozen)."""
    _fx_git(tmp, "init", "-q", "-b", "receipt")
    (tmp / "record.md").write_text("# Placeholder\n\nDifferent content entirely.\n", encoding="utf-8")
    _fx_git(tmp, "add", "-A")
    _fx_git(tmp, "commit", "-q", "-m", "pre")
    c_pre = _fx_git(tmp, "rev-parse", "HEAD").strip()

    (tmp / "record.md").write_text(FIXTURE_BODY, encoding="utf-8")
    (tmp / "other.md").write_text(FIXTURE_OTHER, encoding="utf-8")
    _fx_git(tmp, "add", "-A")
    _fx_git(tmp, "commit", "-q", "-m", "body")
    c_body = _fx_git(tmp, "rev-parse", "HEAD").strip()

    n_body = len(split_keepends(FIXTURE_BODY))
    with (tmp / "record.md").open("a", encoding="utf-8") as fh:
        fh.write("\n" + FIXTURE_NOTE_1)
    # The stamp goes at the BODY's edge, not at the note's: the blank line that
    # separates them arrived WITH the note and so is not part of what `c_body`
    # froze. Building the fixture's stamp by hand -- rather than by calling
    # `derive_stamp` -- keeps the receipt from testing the backfill against
    # itself, which would pass whether or not either half worked.
    _fx_stamp_above(tmp, "record.md", c_body, n_body, n_body + 1)
    _fx_git(tmp, "add", "-A")
    _fx_git(tmp, "commit", "-q", "-m", "freeze")
    c_frozen = _fx_git(tmp, "rev-parse", "HEAD").strip()
    return c_pre, c_body, c_frozen


def mutation_receipt() -> int:  # noqa: C901 -- one arm per branch, deliberately flat
    import shutil
    import tempfile

    cfg = Config(enforced_globs=["*.md"], allow_list=[], pending_on_landing=[])
    root = Path(tempfile.mkdtemp(prefix="rule12-receipt-"))
    ok = True
    try:
        tmp = root / "fixture"
        tmp.mkdir()
        c_pre, c_body, c_frozen = _fx_build(tmp)
        pristine = (tmp / "record.md").read_text(encoding="utf-8")
        other_pristine = (tmp / "other.md").read_text(encoding="utf-8")

        def run_scan() -> list[str]:
            return scan(tmp, cfg, ["record.md", "other.md"]).failures

        def reset() -> None:
            (tmp / "record.md").write_text(pristine, encoding="utf-8")
            (tmp / "other.md").write_text(other_pristine, encoding="utf-8")

        base_findings = run_scan()
        if base_findings:
            print(f"{TAG} RECEIPT ABORT: the unperturbed fixture already fails:")
            for f in base_findings:
                print(f"    {f}")
            return 1
        print(f"{TAG} receipt fixture built and GREEN unperturbed "
              f"(base commit {c_body[:12]}, freeze commit {c_frozen[:12]}).")

        def arm_catch(label: str, mutate) -> None:
            nonlocal ok
            reset()
            mutate()
            found = run_scan()
            if found:
                head = found[0].splitlines()[0]
                print(f"{TAG} receipt CAUGHT: {label}\n           -> {head[:190]}")
            else:
                print(f"{TAG} *** receipt MISSED: {label} -- the gate is a NO-OP for this class")
                ok = False

        def arm_quiet(label: str, mutate) -> None:
            nonlocal ok
            reset()
            mutate()
            found = run_scan()
            if found:
                print(f"{TAG} *** receipt FALSE-POSITIVE: {label} -- the gate reds on a "
                      f"legitimate change; it will be switched off\n           -> "
                      f"{found[0].splitlines()[0][:190]}")
                ok = False
            else:
                print(f"{TAG} receipt STABLE: {label}")

        def edit(fn):
            def go():
                p = tmp / "record.md"
                p.write_text(fn(p.read_text(encoding="utf-8")), encoding="utf-8")
            return go

        # ---- CAN-IT-STAY-QUIET arms first: the inverse class, built for. -----
        def legit_append() -> None:
            p = tmp / "record.md"
            with p.open("a", encoding="utf-8") as fh:
                fh.write("\n" + FIXTURE_NOTE_2)
            lines = split_keepends(p.read_text(encoding="utf-8"))
            prev_stamp = next(i for i, ln in enumerate(lines, 1) if STAMP_RE.search(ln))
            insert_at = len(lines) - 1          # before the blank that precedes note 2
            _fx_stamp_above(tmp, "record.md", c_frozen, insert_at - prev_stamp, insert_at)

        arm_quiet(
            "a LEGITIMATE Rule-12 append below the boundary (a second dated note, "
            "correctly stamped) leaves the first frozen region untouched",
            legit_append,
        )
        arm_quiet(
            "an edit to a file that carries NO Rule-12 note at all",
            lambda: (tmp / "other.md").write_text(
                other_pristine.replace("ordinary prose", "REWRITTEN prose"), encoding="utf-8"
            ),
        )

        # ---- CAN-IT-FIRE arms -------------------------------------------------
        arm_catch(
            "an EDIT ABOVE the freeze boundary (12.5 -> 21.53 ohm): the LINE COUNT is "
            "unchanged, so a line-count-only extent is blind; the byte extent moves",
            edit(lambda s: s.replace("12.5 ohm at the first", "21.53 ohm at the first", 1)),
        )
        arm_catch(
            "an EQUAL-LENGTH substitution above the boundary (CONFIRMED -> REFUTED!!); "
            "lines AND bytes both still match, so only the sha256 can see it",
            edit(lambda s: s.replace("Verdict: CONFIRMED.", "Verdict: REFUTED!!.", 1)),
        )
        arm_catch(
            "a DELETION inside the frozen region",
            edit(lambda s: s.replace("The crossing is REPRODUCED on both benches.\n", "", 1)),
        )
        arm_catch(
            "an INSERTION inside the frozen region",
            edit(lambda s: s.replace(
                "## 2. Result\n", "## 2. Result\n\nSmuggled sentence.\n", 1)),
        )
        arm_catch(
            "a TAMPERED BASE SHA pointing at a commit that does not carry these bytes",
            edit(lambda s: re.sub(r"base=[0-9a-f]{40}", f"base={c_pre}", s, count=1)),
        )
        arm_catch(
            "a TAMPERED BASE SHA pointing at no commit at all",
            edit(lambda s: re.sub(r"base=[0-9a-f]{40}", "base=" + "0" * 40, s, count=1)),
        )
        arm_catch(
            "a TAMPERED HASH in the stamp",
            edit(lambda s: re.sub(r"sha256=[0-9a-f]{64}", "sha256=" + "b" * 64, s, count=1)),
        )
        arm_catch(
            "a TAMPERED LINE EXTENT in the stamp (boundary silently moved)",
            edit(lambda s: re.sub(r"lines=(\d+)", lambda m: f"lines={int(m.group(1)) - 2}", s, 1)),
        )
        arm_catch(
            "a TAMPERED BYTE EXTENT in the stamp",
            edit(lambda s: re.sub(r"bytes=(\d+)", lambda m: f"bytes={int(m.group(1)) + 3}", s, 1)),
        )
        arm_catch(
            "a RULE-12 PROSE NOTE WITH NO STAMP -- the failure the gate exists to prevent",
            edit(lambda s: s + "\n" + FIXTURE_NOTE_2),
        )
        arm_catch(
            "a MALFORMED stamp (reads as guarded to a human, parses for no machine)",
            edit(lambda s: re.sub(r"sha256=[0-9a-f]{64}", "sha256=NOTAHASH", s, count=1)),
        )
        arm_catch(
            "a ZERO-EXTENT stamp, which would certify nothing and pass forever",
            edit(lambda s: re.sub(r"lines=\d+ bytes=\d+ sha256=[0-9a-f]{64}",
                                  "lines=0 bytes=0 sha256=" + "0" * 64, s, count=1)),
        )
        reset()
    finally:
        shutil.rmtree(root, ignore_errors=True)

    # ---- the allow-list must not be a mute button ---------------------------
    bad_cfg = Path(tempfile.mkdtemp(prefix="rule12-cfg-")) / "cfg.json"
    bad_cfg.write_text(json.dumps({
        "enforced_globs": ["*.md"],
        "allow_list": [{"path": "a.md", "match": "x"}],
    }), encoding="utf-8")
    _, probs = load_config(bad_cfg)
    if probs:
        print(f"{TAG} receipt CAUGHT: an allow-list entry with no `class`/`reason` "
              f"is rejected -- an exemption must state itself")
    else:
        print(f"{TAG} *** receipt MISSED: a reasonless allow-list entry was accepted; "
              f"the allow-list is a mute button")
        ok = False
    empty_cfg = bad_cfg.with_name("empty.json")
    empty_cfg.write_text(json.dumps({"enforced_globs": [], "allow_list": []}), encoding="utf-8")
    _, probs2 = load_config(empty_cfg)
    if probs2:
        print(f"{TAG} receipt CAUGHT: an EMPTY enforced scope is a failure, not a pass")
    else:
        print(f"{TAG} *** receipt MISSED: an empty enforced scope still reported OK")
        ok = False
    shutil.rmtree(bad_cfg.parent, ignore_errors=True)

    if ok:
        print(f"{TAG} MUTATION RECEIPT OK -- the gate fires on every violation class above "
              f"and stays quiet on the sanctioned append.")
        return 0
    print(f"{TAG} MUTATION RECEIPT FAILED -- at least one arm did not behave.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
