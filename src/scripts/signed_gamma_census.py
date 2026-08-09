#!/usr/bin/env python3
"""Signed-Γ census — a corpus SURVEY INSTRUMENT, not a gate.

Why this exists
---------------
Two independent sweeps of "signed Γ" across the AVE corpus disagreed by ~4x:

  * an audit reported **~173 lines / 56 files** for a signed ``Γ … = -1`` of any
    channel across ``manuscript/**/*.tex``;
  * the ringdown-wave lane's re-derivation reported **746 lines / 197 files**
    (a looser variant, **810 / 203**);
  * both agreed exactly on a narrow ``Γ_bulk`` print register: **31 / 16**.

None of those three numbers is interpretable until the UNIVERSE is defined:
which roots, which file extensions, whether ``%``-comment lines count, whether
a bare ASCII ``Gamma`` identifier counts alongside ``\\Gamma`` and ``Γ``, how
far the relation operator may sit from the Γ token, whether ``+1`` counts as
"signed" alongside ``-1``, and whether the minus sign may be spelled U+2212.
Each of those is a knob, and the 4x gap lives entirely in the knob settings —
not in the corpus.

Three knobs turned out to carry real, quantified blind spots (all four presets
below reproduce their reported figure once the knob is stated):

  * **minus spelling.** An ASCII-hyphen-only sweep of ``manuscript/**/*.{tex,md}``
    misses **105 lines across 14 further files** that spell the sign U+2212.
    No error, no warning — the sites simply are not there.
  * **font-wrapped subscripts.** A subscript span written ``_\\{[^}]*\\}``
    cannot cross the inner brace of ``\\mathrm{...}``, so a
    ``\\Gamma_{\\mathrm{bulk}} = -1`` line is invisible to it. On the print
    corpus that is the difference between seeing 12 and 25 bulk-channel sites.
  * **file class.** ``manuscript/ave-kb/**/*.md`` restates the same claim
    across many leaves, so a per-line count over tex+md is simply not the same
    quantity as a per-line count over tex — most of the 4x is this.

This module makes every knob an explicit, named, defaulted, overridable flag,
and ships the three prior sweeps as reproducible ``--preset`` values. The point
is not to declare a winning count. **Nobody has ruled what the right count is.**
The point is that "signed Γ" is not a well-formed query until the universe is
stated, and after this module it can only be asked with the universe attached.

NOT A GATE
----------
Exit code 0 on any corpus content. There is no threshold, no pass/fail on the
count, and this is deliberately NOT wired into ``make verify``: gating on an
unadjudicated census is the checklist-not-a-gate defect. ``make gamma-census``
RUNS it; nothing FAILS on it. The only non-zero exit is code 3, reserved for
the instrument failing its OWN two-method self-check (below) — that is a bug in
this script, not a finding about the corpus.

The two-method self-check
-------------------------
This repo has a documented history of silent grep false-negatives: an unquoted
``--include=*.tex`` is glob-eaten by the shell and returns ZERO, and
``git grep -- 'path/**'`` returns ZERO on a ``**`` pathspec. A census built on
one scan method inherits whichever false-negative that method has.

So every run scans TWICE with independent engines:

  * **method A** — Python ``pathlib.rglob`` walk + ``re``;
  * **method B** — a subprocess ``grep -rnE`` (or ``git grep -InE``) pass.

The two ``(path, lineno)`` sets must be identical. If they are not, the script
prints the symmetric difference and exits 3. A census whose two methods
disagree is not a census. The self-check runs on the RAW detection set, before
any classification or filtering, because that is the layer where a scan bug
lives; classification differences would mask it.

Keeping both engines honest costs one design constraint: the detection regex
is authored in **POSIX-ERE-compatible** form — no lookarounds, no non-capturing
groups, no ``\\d``/``\\s`` shorthands. Everything that needs richer logic (the
trailing-digit guard that separates ``-1`` from ``-1.0``, channel naming,
sign extraction) happens in the Python CLASSIFIER after the match, where both
methods have already agreed on which lines are in play.

Classification axes
-------------------
Per site (one Γ occurrence, not one line):

  * ``channel``     — ``bulk`` / ``shear`` / ``EM`` / ``other:<token>`` /
                      ``unspecified`` (no subscript);
  * ``sign``        — ``-1`` / ``+1`` / ``0`` / ``other`` / ``none``;
  * ``rendered``    — ``True`` for typeset text, ``False`` for a comment line;
  * ``file_class``  — ``print_tex`` / ``kb_md`` / ``research`` / ``src`` /
                      ``other``.

``channel`` and ``rendered`` are first-class because both are load-bearing for
downstream slicing: a claim about the printed manuscript must not be counted
from a ``%``-commented draft line, and a claim about one channel must not be
counted from another's.

Usage
-----
    python src/scripts/signed_gamma_census.py --preset audit-2026-08-05
    python src/scripts/signed_gamma_census.py --preset wave-broad --json out.json
    python src/scripts/signed_gamma_census.py --reconcile      # all presets
    python src/scripts/signed_gamma_census.py --roots manuscript,research \\
        --ext .tex,.md --comments exclude --sites

Determinism: output is sorted by ``(path, lineno, column)`` and carries no
timestamp, so re-running at the same tree yields a byte-identical artifact.

Regression test: ``src/tests/test_signed_gamma_census.py``.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field, replace
from pathlib import Path

# --------------------------------------------------------------------------
# ERE-safe character-class primitives
#
# Three escape conventions differ between Python ``re`` and POSIX ERE INSIDE a
# bracket expression, and each one silently changes what matches rather than
# raising. All three were caught live by this module's own two-method
# self-check, so they are spelled out rather than hidden in the patterns:
#
#   1. ``[^\n]`` — POSIX bracket expressions do NOT honour ``\n`` as newline.
#      To grep, ``[^\n]`` is "neither a backslash nor the letter n", so it
#      cannot cross ``\mathrm{...}`` and silently drops every font-wrapped
#      subscript. Python reads it as "any char but newline". Use ``.``.
#   2. ``\t`` — likewise not an escape inside a POSIX bracket: ``[ \t]`` is
#      {space, backslash, t} to grep and {space, TAB} to Python. Use a LITERAL
#      tab character instead.
#   3. ``\\`` — a lone ``\`` inside a Python character class escapes the next
#      character, so a literal backslash needs to be doubled; ERE then sees a
#      harmless duplicate class member.
#
# Nothing below may reintroduce ``[^\n]`` or ``\t`` inside a bracket.
# --------------------------------------------------------------------------

_TAB = "\t"

#: Horizontal whitespace, literal-tab spelling.
HSPACE = "[ " + _TAB + "]"

#: Whitespace plus the LaTeX glue that routinely sits between a relation and
#: its value: ``$`` delimiters, ``\,``/``\!`` spacing macros, ``~`` ties.
MATH_GLUE = "[ " + _TAB + "$" + "\\\\" + "!~]"

#: "…and the next character is not a digit or a decimal point." This is the
#: ERE-expressible stand-in for the negative lookahead ``(?![0-9.])`` that
#: separates ``= -1`` from ``= -1.5`` / ``= -100``. Consuming one trailing
#: character is harmless for a line-set census and keeps both engines on the
#: byte-identical pattern.
MAGNITUDE_GUARD = "([^0-9.]|$)"


# --------------------------------------------------------------------------
# Universe knobs — the whole point of the module. Each is a named vocabulary
# with a documented default; presets are nothing but frozen knob settings.
# --------------------------------------------------------------------------

#: How the Γ token itself may be spelled. ``tex`` is the strictest (typeset
#: math only); ``all`` additionally admits a bare ASCII ``Gamma``, which is how
#: the symbol appears in Python identifiers and fenced code blocks — a real
#: source of the file-count inflation between the audit and the wave sweeps.
GAMMA_FORMS: dict[str, str] = {
    "tex": r"\\Gamma",
    "math": r"(\\Gamma|Γ)",
    "all": r"(\\Gamma|Γ|Gamma)",
}

#: What counts as "asserting a value". ``eq`` is bare equality; ``eqto`` adds
#: the limit arrows that the corpus uses for boundary conditions
#: (``\Gamma \to -1`` is at least as common as ``\Gamma = -1``); ``wide`` adds
#: the approximate/definitional relations.
#: ``any`` asserts nothing at all — it turns the query from "Γ is set to a
#: value" into "Γ of channel X is mentioned", which is the shape of the narrow
#: print-register question the two prior sweeps DID agree on.
RELATIONS: dict[str, str] = {
    "any": r"",
    "eq": r"=",
    "eqto": r"(=|\\to|\\rightarrow|→)",
    "wide": r"(=|\\to|\\rightarrow|→|->|\\equiv|\\approx|\\simeq)",
}

#: What may sit between the Γ token and the relation operator.
#: ``adjacent`` admits only a subscript (``\Gamma_{bulk} = -1``) — the honest
#: reading of "signed Γ of channel X". ``near`` admits up to 25 arbitrary
#: characters, which picks up ``|\Gamma_{bulk}|^2 = 1``-style lines. ``any``
#: admits the rest of the line, which means a line mentioning Γ anywhere and
#: ``= -1`` anywhere counts — the loosest reading, and demonstrably the one
#: that produces the largest of the three disputed numbers.
#: ``adjacent`` is deliberately the NARROW brace form ``_{...}`` that cannot
#: cross an inner ``}``. That means it MISSES ``\Gamma_{\mathrm{bulk}} = -1``,
#: because the inner ``}`` of ``\mathrm{bulk}`` terminates the span early.
#: This is not an oversight — it is exactly the behaviour needed to reproduce
#: the audit sweep, and preserving it is what makes the under-count visible as
#: a preset difference rather than an unexplained gap. ``adjacent-nested`` is
#: the repaired form and is the module DEFAULT.
GAPS: dict[str, str] = {
    "adjacent": r"(_\{[^}]{0,40}\}|_[A-Za-z0-9]{1,12})?" + HSPACE + "*",
    # `[^=]{0,40}` can span an inner `}` (so `_{\mathrm{bulk}}` is seen), at the
    # cost of also spanning a sibling token if one closes on a brace within 40
    # characters. Bounded and brace-terminated, so it stays far tighter than
    # `near`/`any`, but it is a widening and is named as one.
    "adjacent-nested": r"(_\{[^=]{0,40}\}|_[A-Za-z0-9]{1,12})?" + "[ " + _TAB + "$}|]*",
    "near": r".{0,25}",
    "any": r".*",
}

#: Which asserted values count as "signed". ``minus`` is ``-1`` only (the
#: short-circuit / hard-wall reflection); ``pm`` adds ``+1`` (the open-circuit
#: conjugate); ``pm0`` adds the matched-load ``0``.
#: Written as ALTERNATIONS rather than bracket expressions because ``−``
#: (U+2212) is multi-byte: inside ``[-−+]`` a byte-oriented grep would treat
#: its two bytes as two independent bracket members and could match a stray
#: continuation byte, desynchronising the two scan methods.
SIGN_SETS: dict[str, str] = {
    "any": r"",
    "minus": "MINUS" + HSPACE + "*1",
    "pm": "(MINUS|[+])" + HSPACE + "*1",
    "pm0": "((MINUS|[+])" + HSPACE + "*1|0)",
}

#: How a minus sign may be spelled. ``ascii`` is the hyphen-minus alone;
#: ``unicode`` additionally admits U+2212 MINUS SIGN.
#:
#: This is not a pedantic knob. On the manuscript tex+md universe the two
#: settings differ by ~105 lines across 14 additional files: an ASCII-only
#: signed-Γ grep is blind to every site that spells the sign U+2212, and those
#: sites are invisible with no error and no warning. Any sweep that reports a
#: signed-Γ count without stating this setting has an unquantified
#: false-negative floor.
MINUS_FORMS: dict[str, str] = {
    "ascii": "-",
    "unicode": "(-|−)",
}

#: What may sit between the relation operator and the value.
#: ``tight`` is whitespace and at most one ``$``; ``math`` additionally admits
#: LaTeX spacing macros (``\!``, ``\,``) and ``~`` ties, and any number of
#: ``$`` delimiters.
GLUE: dict[str, str] = {
    "tight": HSPACE + "*[$]?" + HSPACE + "*",
    "math": MATH_GLUE + "*",
}

#: Directories never walked, under any preset. Build output and caches are not
#: corpus; ``.git`` is not corpus.
ALWAYS_EXCLUDED_DIRS: tuple[str, ...] = (
    ".git",
    "build",
    "__pycache__",
    ".venv",
    ".pytest_cache",
    ".ruff_cache",
    "node_modules",
)

#: Channel vocabulary — LITERAL spellings only, case-folded.
#:
#: Deliberately NOT widened: mapping ``long`` / ``longitudinal`` / ``dilatation``
#: onto ``bulk``, or ``cosserat`` onto ``shear``, would be a physics judgement
#: about which named channel a subscript denotes. This module is an enumerator;
#: it reports what is written. Unrecognised subscripts surface as
#: ``other:<token>`` so the long tail stays countable and whoever adjudicates
#: the vocabulary can see exactly what they are folding.
CHANNEL_ALIASES: dict[str, tuple[str, ...]] = {
    "bulk": ("bulk",),
    "shear": ("shear",),
    "EM": ("em",),
}

#: Comment-line detection, per extension. Deliberately conservative: only a
#: line whose FIRST non-whitespace token opens a comment counts as a comment.
#: A trailing ``% …`` on an otherwise typeset line still renders most of its
#: content, so calling the whole line "not rendered" would be wrong.
COMMENT_PREFIXES: dict[str, tuple[str, ...]] = {
    ".tex": ("%",),
    ".md": ("<!--",),
    ".py": ("#",),
    ".yaml": ("#",),
    ".yml": ("#",),
}


@dataclass(frozen=True)
class Universe:
    """A fully-specified census question. Every knob, no defaults hidden."""

    roots: tuple[str, ...] = ("manuscript",)
    exts: tuple[str, ...] = (".tex",)
    gamma_form: str = "math"
    relation: str = "eqto"
    gap: str = "adjacent-nested"
    signs: str = "minus"
    minus_forms: str = "unicode"
    glue: str = "math"
    comments: str = "include"  # include | exclude | only
    exclude_globs: tuple[str, ...] = ()
    require_channel: bool = False
    channels: tuple[str, ...] = ()  # post-match filter; () = keep all
    sign_filter: tuple[str, ...] = ()  # post-match filter; () = keep all
    #: When True, ``= -1`` does NOT match ``= -1.5`` or ``= -100``. Off is the
    #: naive-grep behaviour, and the difference is worth ~100 lines under the
    #: loosest preset, so it is a knob rather than a hardcoded choice.
    magnitude_guard: bool = True

    def detection_regex(self) -> str:
        """The ERE-compatible detection pattern.

        Authored so that Python ``re``, GNU/BSD/u-grep ``-E`` and ``git grep -E``
        all accept it verbatim. No lookarounds, no ``(?:``, no ``\\s``/``\\d``,
        and no ``\\t``/``\\n`` inside a bracket expression.
        """
        sign_pattern = SIGN_SETS[self.signs].replace("MINUS", MINUS_FORMS[self.minus_forms])
        guard = MAGNITUDE_GUARD if (self.magnitude_guard and sign_pattern) else ""
        return (
            f"{GAMMA_FORMS[self.gamma_form]}"
            f"{GAPS[self.gap]}"
            f"{RELATIONS[self.relation]}"
            f"{GLUE[self.glue] if sign_pattern else ''}"
            f"{sign_pattern}"
            f"{guard}"
        )


@dataclass(frozen=True)
class Site:
    """One classified Γ occurrence."""

    path: str
    lineno: int
    column: int
    channel: str
    sign: str
    rendered: bool
    file_class: str
    #: The matched substring itself, and a window centred on it. The window is
    #: centred rather than taken from the start of the line because manuscript
    #: prose lines routinely run past 400 characters with the Γ token near the
    #: end — a head-truncated excerpt would show unrelated text and make the
    #: artifact look like it was full of false positives when it is not.
    matched: str
    excerpt: str

    def sort_key(self) -> tuple[str, int, int]:
        return (self.path, self.lineno, self.column)


# --------------------------------------------------------------------------
# File discovery (method A's half of the universe)
# --------------------------------------------------------------------------


def discover(repo: Path, universe: Universe) -> list[Path]:
    """Walk ``universe.roots`` and return the in-universe files, sorted.

    Deterministic: the returned order is the sorted repo-relative path order,
    so downstream site ordering does not depend on filesystem walk order.
    """
    found: set[Path] = set()
    for root in universe.roots:
        base = repo / root
        if not base.exists():
            continue
        if base.is_file():
            candidates = [base]
        else:
            candidates = [p for p in base.rglob("*") if p.is_file()]
        for path in candidates:
            rel = path.relative_to(repo)
            if any(part in ALWAYS_EXCLUDED_DIRS for part in rel.parts):
                continue
            if universe.exts and path.suffix not in universe.exts:
                continue
            if any(rel.match(glob) for glob in universe.exclude_globs):
                continue
            found.add(path)
    return sorted(found, key=lambda p: str(p.relative_to(repo)))


def is_comment_line(suffix: str, line: str) -> bool:
    """True when the line's first non-whitespace token opens a comment.

    Conservative on purpose — see ``COMMENT_PREFIXES``. A ``.tex`` line reading
    ``  % \\Gamma_{bulk} = -1`` is not rendered; ``$\\Gamma=-1$  % note`` is.

    LINE-level, and deliberately so: it backs the ``--comments`` universe knob,
    which selects whole lines. For whether a PARTICULAR Γ occurrence is typeset,
    use :func:`is_comment_site` (R33) — a trailing ``%`` comment makes the line
    rendered but the occurrence after it not.
    """
    stripped = line.lstrip()
    return stripped.startswith(COMMENT_PREFIXES.get(suffix, ()))


def is_comment_site(suffix: str, line: str, column: int) -> bool:
    """True when the Γ occurrence at ``column`` (0-based) sits inside a comment.

    R33 repair (`_orchestration/docket-entries/2026-08-07-gamma-tag-spec-correction.md`).
    :func:`is_comment_line` tests only the line's FIRST token, so a TikZ line
    such as ``\\draw (3.6,-0.4) -- (3.6,-1.6); % shorted stub / Gamma=-1 wall``
    was reported ``rendered`` even though its Γ is inside the comment. Spec §1
    condition 2 is about whether the ASSERTION is typeset, so the test has to be
    per-occurrence.

    Only the ``%``-comment languages are handled positionally; for any other
    suffix this falls back to the line-level answer.
    """
    if is_comment_line(suffix, line):
        return True
    if "%" not in COMMENT_PREFIXES.get(suffix, ()):
        return False
    i = 0
    while i < min(column, len(line)):
        if line[i] == "\\":  # \% is an escaped percent, not a comment opener
            i += 2
            continue
        if line[i] == "%":
            return True
        i += 1
    return False


# --------------------------------------------------------------------------
# Classification
# --------------------------------------------------------------------------

#: Subscript span immediately following the Γ token, in either brace or bare
#: form, optionally wrapped in a LaTeX font macro (``\mathrm{}``, ``\text{}``,
#: ``{\rm …}``). The trailing ``\\?`` lets a bare macro subscript such as
#: ``\Gamma_{\min}`` classify as ``other:min`` rather than ``unspecified``.
_SUBSCRIPT_RE = re.compile(
    r"_\{?\s*(?:\\(?:text|mathrm|rm|mathit|mbox|operatorname)\s*\{?\s*)?\\?([A-Za-z0-9,\-]{1,24})"
)

#: The asserted value, read from the first relation operator after the Γ token.
_VALUE_RE = re.compile(
    r"(?:=|\\to|\\rightarrow|→|->|\\equiv|\\approx|\\simeq)[ \t$\\!~]*([-−+]?)[ \t]*([0-9]+(?:\.[0-9]+)?)"
)

# --------------------------------------------------------------------------
# R33 — ADJACENCY REPAIR
# Ruled at `_orchestration/docket-entries/2026-08-07-rulings-r31-r33.md` (R33),
# Grant verbatim *"Agree."*: "The spec's §1 adjacency definition stands; the
# instrument diverges". Documented at
# `_orchestration/docket-entries/2026-08-07-gamma-tag-spec-correction.md`.
#
# THE THREE MEASURED DEFECTS, and what each repair does:
#
#   1. NON-ADJACENT VALUE. `_VALUE_RE.search` scans the WHOLE remainder of the
#      line, so a Γ that asserts nothing inherits the value of a later Γ. On the
#      #923 corpus one site read its "adjacent" value from 410 characters away
#      (`vol_2_subatomic/chapters/01_topological_matter.tex`:167). REPAIR: the
#      relation must be reachable from the Γ token across the BRIDGE only
#      (magnitude bars, `^2`, a subscript, and the universe's own gap
#      characters), and the whole reading is confined to the enclosing
#      inline-math span.
#   2. TRUNCATED VALUE. The numeral was accepted with no check on what follows,
#      so `= 1 - \alpha`, `= 1/3` and `= 1/9` all classified `+1`. REPAIR: a
#      value that is continued by an arithmetic operator is `other`, not ±1 —
#      visible in the census, never silently dropped.
#   3. NOT THE LEFT OPERAND. `T^2 = 1 - \Gamma^2 \to 1` gave Γ the limit that
#      belongs to T² — on lines that go on to say "at $\Gamma = 0$". REPAIR: the
#      Γ (optionally inside magnitude bars) must be the relation's LEFT operand.
#
# `ADJACENCY_FIX` exists so a mutation receipt can force the repair OFF and show
# the receipt firing; nothing but a receipt may flip it.
# --------------------------------------------------------------------------

#: Master switch for the R33 repair. Off = the pre-R33 behaviour, kept ONLY so
#: `research/drivers/gamma_census_adjacency_number_check.py --mutation-receipt`
#: can prove its check is not a tautology.
ADJACENCY_FIX = True

#: What may sit between the Γ token and its relation and still count as
#: adjacent: a closing magnitude bar, a `^2`, a subscript, and the gap
#: characters `GAPS["adjacent-nested"]` already admits.
_BRIDGE_RE = re.compile(
    r"^(\|)?(_\{[^=]{0,40}\}|_[A-Za-z0-9]{1,12})?(\^\{?2\}?)?(\|)?[ \t$}|]*"
)
_RELATION_RE = re.compile(r"^(=|\\to|\\rightarrow|→|->|\\equiv|\\approx|\\simeq)")
_NUMERAL_RE = re.compile(r"^[ \t$\\!~]*([-−+]?)[ \t]*([0-9]+(?:\.[0-9]+)?)")

#: A value followed by one of these is part of a LARGER expression (`1-\alpha`,
#: `1/3`, `1 - 2\times0.250`), so the asserted quantity is not the bare numeral.
_CONTINUES_VALUE = set("-−+/*^·×÷")
_CONTINUES_MACROS = (r"\times", r"\cdot", r"\over", r"\div", r"\pm", r"\mp", r"\frac")

#: Tokens a Γ may legitimately sit immediately after and still be the relation's
#: left operand. Anything else (a digit, an operator, a closing group) means the
#: Γ is embedded in a larger expression.
_OPENERS = set("$([{,;&")
_IMPLIES = (r"\Rightarrow", r"\Longrightarrow", r"\implies", r"\Leftrightarrow",
            r"\iff", r"\therefore", r"\leadsto")
_SPACERS = (r"\left", r"\bigl", r"\Bigl", r"\quad", r"\qquad", r"\!", r"\,", r"\;", r"\:")


def _strip_spacers(text: str) -> str:
    """Drop trailing whitespace and LaTeX spacing macros, repeatedly."""
    while True:
        stripped = text.rstrip()
        hit = next((s for s in _SPACERS if stripped.endswith(s)), None)
        if hit is None:
            return stripped
        text = stripped[: -len(hit)]


def is_left_operand(text_before_gamma: str, _bar_stripped: bool = False) -> bool:
    """True when the Γ is the LEFT operand of the relation that follows it.

    Defect 3 above. `|\\Gamma|` is still the left operand (the bar is a
    delimiter, not an operator), so ONE magnitude bar is stripped and the test
    re-applied — which is what separates `($|\\Gamma| = 1$)` (left operand)
    from `$1 - 2|\\Gamma|^2$` (not).
    """
    seg = _strip_spacers(text_before_gamma)
    if not seg:
        return True
    if seg.endswith("\\["):
        return True
    if any(seg.endswith(tok) for tok in _IMPLIES):
        return True
    if seg[-1] == "|" and not _bar_stripped:
        return is_left_operand(seg[:-1], _bar_stripped=True)
    return seg[-1] in _OPENERS


def _value_is_terminated(tail: str) -> bool:
    """True when nothing after the numeral continues the asserted quantity."""
    rest = tail.lstrip(" \t")
    if not rest:
        return True
    if rest[0] in _CONTINUES_VALUE:
        return False
    return not any(rest.startswith(mac) for mac in _CONTINUES_MACROS)


def _skip_balanced(text: str) -> int:
    """Index just past one brace-balanced expression at the head of ``text``."""
    i, depth = 0, 0
    while i < len(text):
        ch = text[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        elif depth == 0 and _RELATION_RE.match(text[i:]):
            return i
        i += 1
    return len(text)


def read_adjacent_value(segment: str) -> tuple[str, str] | None:
    """``(sign, magnitude)`` asserted for the Γ that ``segment`` starts after.

    Walks the bridge, then the relation, then the value. A relation whose
    right-hand side is an EXPRESSION rather than a numeral (`\\Gamma =
    \\frac{Z-Z_0}{Z+Z_0} = -1`) is followed one hop at a time, because that
    chain does assert a value FOR Γ; a relation whose numeral is continued
    (`= 1 - \\alpha`) stops the walk, because that value is not the numeral.
    """
    bridge = _BRIDGE_RE.match(segment)
    pos = bridge.end() if bridge else 0
    for _ in range(4):  # bounded: no corpus chain is longer, and no unbounded scan
        rel = _RELATION_RE.match(segment[pos:])
        if not rel:
            return None
        pos += rel.end()
        num = _NUMERAL_RE.match(segment[pos:])
        if num:
            if not _value_is_terminated(segment[pos + num.end() :]):
                return ("", "other")
            return (num.group(1), num.group(2))
        pos += _skip_balanced(segment[pos:])
    return None


def math_segment(text_after_gamma: str, inside_math: bool) -> str:
    """The reading window: the rest of the enclosing inline-math span, or line."""
    if not inside_math:
        return text_after_gamma
    i = 0
    while i < len(text_after_gamma):
        if text_after_gamma[i] == "\\":
            i += 2
            continue
        if text_after_gamma[i] == "$":
            return text_after_gamma[:i]
        i += 1
    return text_after_gamma


def in_inline_math(text_before_gamma: str) -> bool:
    """True when an odd number of unescaped ``$`` precede the Γ on this line."""
    i, n = 0, 0
    while i < len(text_before_gamma):
        if text_before_gamma[i] == "\\":
            i += 2
            continue
        if text_before_gamma[i] == "$":
            if i + 1 < len(text_before_gamma) and text_before_gamma[i + 1] == "$":
                i += 2
                continue
            n += 1
        i += 1
    return n % 2 == 1


def _window(line: str, start: int, end: int, pad: int = 70) -> str:
    """A context window centred on the match, with explicit elision markers."""
    left, right = max(0, start - pad), min(len(line), end + pad)
    body = line[left:right].strip()
    return ("…" if left > 0 else "") + body + ("…" if right < len(line) else "")


def strip_gamma_token(text_from_match: str) -> str:
    """Return the text immediately AFTER the Γ token a match started on.

    Written as an explicit prefix test rather than ``str.find("Gamma")``: on a
    line like ``Γ_{bulk} — see the Gamma appendix`` a ``find`` would skip past
    the subscript to the unrelated prose occurrence and misclassify the
    channel as ``unspecified``.
    """
    for prefix, width in ((r"\Gamma", 6), ("Gamma", 5), ("Γ", 1)):
        if text_from_match.startswith(prefix):
            return text_from_match[width:]
    return text_from_match[1:]


def classify_channel(text_after_gamma: str) -> str:
    """Map the subscript immediately after Γ onto the channel vocabulary.

    Returns ``unspecified`` when Γ carries no subscript, a canonical channel
    name when the subscript is a known alias, and ``other:<token>`` otherwise
    so the long tail (``pack``, ``sagnac``, ``ij``, ``cryst``, …) stays visible
    instead of collapsing into an opaque bucket.
    """
    match = _SUBSCRIPT_RE.match(text_after_gamma)
    if not match:
        return "unspecified"
    token = match.group(1).strip().lower().rstrip("}")
    for channel, aliases in CHANNEL_ALIASES.items():
        if token in aliases:
            return channel
    return f"other:{token}"


def classify_sign(text_after_gamma: str, text_before_gamma: str = "") -> str:
    """Read the asserted value off the relation ADJACENT to this Γ.

    The trailing-digit discrimination lives HERE rather than in the detection
    regex, because a negative lookahead is not expressible in POSIX ERE and the
    detection regex must stay byte-identical across both scan methods. So a
    line reading ``\\Gamma = -1.0`` is DETECTED (both methods agree on it) and
    then classified ``other`` — visible in the census, not silently dropped.

    R33: with :data:`ADJACENCY_FIX` on (the default), the value must be
    ADJACENT — reachable across the bridge, inside the same math span, with Γ
    as the relation's left operand, and not continued past the numeral. With it
    off this falls back to the pre-R33 whole-line ``search``, which exists only
    so the mutation receipt can demonstrate the difference.
    """
    if not ADJACENCY_FIX:
        match = _VALUE_RE.search(text_after_gamma)
        if not match:
            return "none"
        sign, magnitude = match.group(1), match.group(2)
    else:
        if not is_left_operand(text_before_gamma):
            return "none"
        segment = math_segment(text_after_gamma, in_inline_math(text_before_gamma))
        read = read_adjacent_value(segment)
        if read is None:
            return "none"
        sign, magnitude = read
        if magnitude == "other":
            return "other"
    negative = sign in ("-", "−")
    if magnitude == "1":
        return "-1" if negative else "+1"
    if magnitude == "0":
        return "0"
    return "other"


def classify_file(rel_path: str) -> str:
    """Bucket a repo-relative path into the file classes the forks slice on."""
    if rel_path.startswith("manuscript/ave-kb/"):
        return "kb_md" if rel_path.endswith(".md") else "kb_other"
    if rel_path.startswith("manuscript/"):
        return "print_tex" if rel_path.endswith(".tex") else "manuscript_other"
    if rel_path.startswith("research/"):
        return "research"
    if rel_path.startswith("src/"):
        return "src"
    return "other"


def scan_python(repo: Path, universe: Universe) -> tuple[list[Site], set[tuple[str, int]]]:
    """Method A: ``rglob`` walk + Python ``re``.

    Returns the classified/filtered sites AND the raw ``(path, lineno)``
    detection set. The raw set is what the two-method self-check compares —
    filtering happens after, so a filter can never hide a scan disagreement.
    """
    regex = re.compile(universe.detection_regex())
    sites: list[Site] = []
    raw: set[tuple[str, int]] = set()

    for path in discover(repo, universe):
        rel = str(path.relative_to(repo))
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for lineno, line in enumerate(lines, start=1):
            matches = list(regex.finditer(line))
            if not matches:
                continue
            raw.add((rel, lineno))

            comment = is_comment_line(path.suffix, line)
            if universe.comments == "exclude" and comment:
                continue
            if universe.comments == "only" and not comment:
                continue

            for match in matches:
                after_gamma = strip_gamma_token(line[match.start() :])
                channel = classify_channel(after_gamma)
                if universe.require_channel and channel == "unspecified":
                    continue
                if universe.channels and channel not in universe.channels:
                    continue
                before_gamma = line[: match.start()]
                sign = classify_sign(after_gamma, before_gamma)
                if universe.sign_filter and sign not in universe.sign_filter:
                    continue
                # R33: `rendered` is a property of the OCCURRENCE, not the line —
                # a trailing `%` comment leaves the line rendered and the Γ after
                # it not. `comment` (line-level) still drives the --comments knob.
                site_comment = (
                    is_comment_site(path.suffix, line, match.start())
                    if ADJACENCY_FIX
                    else comment
                )
                sites.append(
                    Site(
                        path=rel,
                        lineno=lineno,
                        column=match.start() + 1,
                        channel=channel,
                        sign=sign,
                        rendered=not site_comment,
                        file_class=classify_file(rel),
                        matched=match.group(0),
                        excerpt=_window(line, match.start(), match.end()),
                    )
                )
    return sorted(sites, key=Site.sort_key), raw


# --------------------------------------------------------------------------
# Method B — an independent scan engine
# --------------------------------------------------------------------------


def _tracked_paths(repo: Path) -> set[str] | None:
    proc = subprocess.run(
        ["git", "ls-files"], cwd=repo, capture_output=True, text=True, check=False
    )
    if proc.returncode != 0:
        return None
    return {line for line in proc.stdout.splitlines() if line}


def scan_subprocess(repo: Path, universe: Universe, engine: str) -> set[tuple[str, int]]:
    """Method B: shell out to ``grep -rInE`` or ``git grep -InE``.

    Two documented false-negative modes of this repo are guarded structurally:

    * ``--include`` globs are passed as ARGV elements, never through a shell,
      so ``*.tex`` cannot be glob-eaten (the unquoted-``--include`` zero);
    * ``git grep`` is given plain directory operands after ``--``, never a
      ``dir/**`` pathspec (the ``**``-pathspec zero); extension filtering is
      done in Python on the results instead.
    """
    pattern = universe.detection_regex()
    if not pattern:
        raise ValueError("empty detection pattern; refusing to scan")

    if engine == "git-grep":
        cmd = ["git", "grep", "-I", "-n", "-E", pattern, "--", *universe.roots]
    else:
        cmd = ["grep", "-r", "-I", "-n", "-E", pattern]
        for ext in universe.exts:
            cmd.append(f"--include=*{ext}")
        for excluded in ALWAYS_EXCLUDED_DIRS:
            cmd.append(f"--exclude-dir={excluded}")
        cmd.extend(universe.roots)

    proc = subprocess.run(cmd, cwd=repo, capture_output=True, text=True, check=False)
    # grep exit 1 == "no matches", which is a legitimate empty census.
    if proc.returncode not in (0, 1):
        raise RuntimeError(f"method-B scan failed ({' '.join(cmd[:4])}): {proc.stderr.strip()}")

    hits: set[tuple[str, int]] = set()
    for line in proc.stdout.splitlines():
        head, _, rest = line.partition(":")
        number, _, _ = rest.partition(":")
        if not number.isdigit():
            continue
        rel = head
        if universe.exts and not rel.endswith(tuple(universe.exts)):
            continue
        if any(part in ALWAYS_EXCLUDED_DIRS for part in Path(rel).parts):
            continue
        if any(Path(rel).match(glob) for glob in universe.exclude_globs):
            continue
        hits.add((rel, int(number)))
    return hits


@dataclass
class CrossCheck:
    engine: str
    method_a: int
    method_b: int
    only_a: list[str] = field(default_factory=list)
    only_b: list[str] = field(default_factory=list)

    @property
    def agree(self) -> bool:
        return not self.only_a and not self.only_b


def cross_check(
    repo: Path, universe: Universe, raw_a: set[tuple[str, int]], engine: str
) -> CrossCheck:
    """Compare the two engines' RAW ``(path, lineno)`` detection sets.

    Compared before classification and before comment/channel/sign filtering:
    those are Python-side decisions method B never makes, so folding them in
    would manufacture a disagreement that says nothing about scan correctness —
    and, worse, could mask a real one.
    """
    raw_b = scan_subprocess(repo, universe, engine)
    if engine == "git-grep":
        tracked = _tracked_paths(repo)
        if tracked is not None:
            raw_a = {hit for hit in raw_a if hit[0] in tracked}
    only_a = sorted(f"{p}:{n}" for p, n in raw_a - raw_b)
    only_b = sorted(f"{p}:{n}" for p, n in raw_b - raw_a)
    return CrossCheck(engine, len(raw_a), len(raw_b), only_a, only_b)


# --------------------------------------------------------------------------
# Presets — the three disputed sweeps, frozen as knob settings
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Preset:
    name: str
    universe: Universe
    reported: str
    note: str


PRESETS: dict[str, Preset] = {
    "bulk-print-register": Preset(
        name="bulk-print-register",
        universe=Universe(
            roots=("manuscript",),
            exts=(".tex",),
            gamma_form="all",
            relation="any",
            gap="adjacent-nested",
            signs="any",
            comments="include",
            require_channel=True,
            channels=("bulk",),
        ),
        reported="31 lines / 16 files",
        note=(
            "The narrow print register both prior sweeps agreed on. Note the "
            "question shape: it asserts NO value -- it counts where a bulk-"
            "subscripted Gamma is written in the printed manuscript, not where "
            "it is set to -1. That is why the two sweeps could agree on it "
            "while differing 4x on the signed question."
        ),
    ),
    "audit-2026-08-05": Preset(
        name="audit-2026-08-05",
        universe=Universe(
            roots=("manuscript",),
            exts=(".tex",),
            gamma_form="math",
            relation="eqto",
            gap="adjacent",
            signs="minus",
            comments="include",
        ),
        reported="173 lines / 56 files",
        note=(
            "Print-only, LaTeX/unicode Gamma only, subscript-adjacent relation, "
            "-1 only. The NARROW `adjacent` gap is load-bearing: it cannot "
            "cross the inner brace of a font macro, so a "
            "\\Gamma_{\\mathrm{bulk}} = -1 line is INVISIBLE to this universe. "
            "Widening only that one knob to `adjacent-nested` is the single "
            "largest correction available to this preset."
        ),
    ),
    "wave-broad": Preset(
        name="wave-broad",
        universe=Universe(
            roots=("manuscript",),
            exts=(".tex", ".md"),
            gamma_form="tex",
            relation="eqto",
            gap="near",
            signs="minus",
            minus_forms="unicode",
            glue="tight",
            comments="exclude",
        ),
        reported="746 lines / 197 files",
        note=(
            "The KB (manuscript/ave-kb/**/*.md) enters the universe here, which "
            "is where most of the 4x lives: the same claim is restated many "
            "times across KB leaves, so a per-line count over tex+md is not "
            "comparable with a per-line count over tex alone."
        ),
    ),
    "wave-loose": Preset(
        name="wave-loose",
        universe=Universe(
            roots=("manuscript",),
            exts=(".tex", ".md"),
            gamma_form="all",
            relation="wide",
            gap="any",
            signs="pm",
            minus_forms="ascii",
            glue="tight",
            comments="include",
        ),
        reported="810 lines / 203 files",
        note=(
            "Every knob at its loosest EXCEPT the minus spelling: bare ASCII "
            "`Gamma` identifiers count, any relation counts, +1 counts as "
            "signed, and the gap spans the whole line -- so a line mentioning "
            "Gamma anywhere and `= -1` anywhere is a hit, related or not. "
            "minus_forms is pinned to `ascii` because that is what reproduces "
            "the reported figure; flipping that ONE knob to `unicode` adds 105 "
            "lines across 14 further files, which is the largest single "
            "false-negative in any of the prior sweeps. The reported 810 sits "
            "inside this universe's 807-811 comment-policy band (807 with "
            "comments excluded, 811 included, files 203 either way); 810 "
            "itself is reachable only by excluding markdown HTML comments "
            "while keeping LaTeX %-comments, which is not a coherent policy."
        ),
    ),
}


# --------------------------------------------------------------------------
# Census assembly + reporting
# --------------------------------------------------------------------------


def _bucket(sites: list[Site], key) -> dict[str, dict[str, int]]:
    out: dict[str, dict] = {}
    for site in sites:
        name = str(key(site))
        slot = out.setdefault(name, {"sites": 0, "_lines": set(), "_files": set()})
        slot["sites"] += 1
        slot["_lines"].add((site.path, site.lineno))
        slot["_files"].add(site.path)
    return {
        name: {
            "sites": slot["sites"],
            "lines": len(slot["_lines"]),
            "files": len(slot["_files"]),
        }
        for name, slot in sorted(out.items())
    }


def build_census(
    repo: Path,
    universe: Universe,
    *,
    preset: str | None = None,
    check: str = "grep",
    include_sites: bool = False,
) -> tuple[dict, CrossCheck | None]:
    sites, raw_a = scan_python(repo, universe)
    checked = cross_check(repo, universe, raw_a, check) if check != "off" else None

    payload: dict = {
        "schema": "signed-gamma-census/1",
        "preset": preset,
        "universe": {
            k: list(v) if isinstance(v, tuple) else v for k, v in asdict(universe).items()
        },
        "detection_regex": universe.detection_regex(),
        "totals": {
            "sites": len(sites),
            "lines": len({(s.path, s.lineno) for s in sites}),
            "files": len({s.path for s in sites}),
        },
        "by_channel": _bucket(sites, lambda s: s.channel),
        "by_sign": _bucket(sites, lambda s: s.sign),
        "by_file_class": _bucket(sites, lambda s: s.file_class),
        "by_rendered": _bucket(sites, lambda s: "rendered" if s.rendered else "comment"),
    }
    if checked is not None:
        payload["cross_check"] = {
            "engine": checked.engine,
            "method_a_lines": checked.method_a,
            "method_b_lines": checked.method_b,
            "status": "agree" if checked.agree else "DISAGREE",
            "only_method_a": checked.only_a,
            "only_method_b": checked.only_b,
        }
    if include_sites:
        payload["sites"] = [asdict(s) for s in sites]
    return payload, checked


def render_summary(payload: dict) -> str:
    lines: list[str] = []
    label = payload.get("preset") or "custom universe"
    totals = payload["totals"]
    universe = payload["universe"]
    lines.append(f"SIGNED-GAMMA CENSUS - {label}")
    lines.append(f"  regex   : {payload['detection_regex']}")
    lines.append(
        "  universe: roots={roots} exts={exts} gamma={gamma_form} rel={relation} "
        "gap={gap} signs={signs} minus={minus_forms} glue={glue} "
        "comments={comments} magnitude_guard={magnitude_guard}".format(**universe)
    )
    if universe["channels"]:
        lines.append(f"            channels={universe['channels']}")
    lines.append(
        f"  TOTALS  : {totals['sites']} sites / {totals['lines']} lines / "
        f"{totals['files']} files"
    )
    for title, key in (
        ("by channel", "by_channel"),
        ("by sign", "by_sign"),
        ("by file class", "by_file_class"),
        ("rendered vs comment", "by_rendered"),
    ):
        lines.append(f"  {title}:")
        for name, counts in payload[key].items():
            lines.append(
                f"    {name:<28} {counts['sites']:>6} sites  {counts['lines']:>6} lines  "
                f"{counts['files']:>5} files"
            )
    if "cross_check" in payload:
        check = payload["cross_check"]
        lines.append(
            f"  two-method self-check ({check['engine']}): {check['status']} "
            f"(A={check['method_a_lines']} lines, B={check['method_b_lines']} lines)"
        )
        for side in ("only_method_a", "only_method_b"):
            for item in check[side][:20]:
                lines.append(f"    {side}: {item}")
    return "\n".join(lines)


def _parse_reported(text: str) -> tuple[int, int]:
    found = re.findall(r"(\d+)", text)
    return int(found[0]), int(found[1])


def render_reconciliation(repo: Path, check: str) -> tuple[str, list[dict]]:
    rows: list[dict] = []
    out: list[str] = [
        "RECONCILIATION - the prior sweeps, re-run as explicit universes",
        "",
        f"{'preset':<22} {'reported':<24} {'observed':<26} verdict",
        "-" * 96,
    ]
    for preset in PRESETS.values():
        payload, checked = build_census(repo, preset.universe, preset=preset.name, check=check)
        totals = payload["totals"]
        observed = f"{totals['lines']} lines / {totals['files']} files"
        rep_lines, rep_files = _parse_reported(preset.reported)
        if (totals["lines"], totals["files"]) == (rep_lines, rep_files):
            verdict = "EXACT"
        elif totals["files"] == rep_files:
            verdict = f"files EXACT, lines {totals['lines'] - rep_lines:+d}"
        else:
            verdict = (
                f"lines {totals['lines'] - rep_lines:+d}, "
                f"files {totals['files'] - rep_files:+d}"
            )
        if checked is not None and not checked.agree:
            verdict += "  [SELF-CHECK DISAGREE]"
        out.append(f"{preset.name:<22} {preset.reported:<24} {observed:<26} {verdict}")
        rows.append(
            {
                "preset": preset.name,
                "reported": preset.reported,
                "observed_lines": totals["lines"],
                "observed_files": totals["files"],
                "verdict": verdict,
                "note": preset.note,
                "cross_check": payload.get("cross_check", {}).get("status"),
            }
        )
    out.append("")
    out.append("Notes")
    out.append("-----")
    for row in rows:
        out.append(f"  {row['preset']}: {row['note']}")
    return "\n".join(out), rows


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Signed-Gamma corpus census - survey instrument, NOT a gate.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--repo", default=None, help="repo root (default: infer from this file)")
    parser.add_argument("--preset", choices=sorted(PRESETS), help="start from a frozen universe")
    parser.add_argument("--roots", help="comma-separated roots, e.g. manuscript,research,src")
    parser.add_argument("--ext", help="comma-separated extensions, e.g. .tex,.md")
    parser.add_argument("--gamma-form", choices=sorted(GAMMA_FORMS))
    parser.add_argument("--relation", choices=sorted(RELATIONS))
    parser.add_argument("--gap", choices=sorted(GAPS))
    parser.add_argument("--signs", choices=sorted(SIGN_SETS))
    parser.add_argument("--minus-forms", choices=sorted(MINUS_FORMS))
    parser.add_argument("--glue", choices=sorted(GLUE))
    parser.add_argument(
        "--no-magnitude-guard",
        action="store_true",
        help="let `= -1` also match `= -1.5` / `= -100` (naive-grep behaviour)",
    )
    parser.add_argument("--comments", choices=("include", "exclude", "only"))
    parser.add_argument("--exclude-glob", action="append", default=[])
    parser.add_argument("--channel", action="append", default=[], help="keep only these channels")
    parser.add_argument("--sign", action="append", default=[], help="keep only these signs")
    parser.add_argument("--require-channel", action="store_true")
    parser.add_argument(
        "--check",
        choices=("grep", "git-grep", "off"),
        default="grep",
        help="method-B engine for the two-method self-check (default: grep)",
    )
    parser.add_argument("--json", dest="json_path", help="write the machine-readable census here")
    parser.add_argument("--sites", action="store_true", help="include every site in the output")
    parser.add_argument("--reconcile", action="store_true", help="run all presets and compare")
    return parser


def universe_from_args(args: argparse.Namespace) -> tuple[Universe, str | None]:
    base = PRESETS[args.preset].universe if args.preset else Universe()
    overrides: dict = {}
    if args.roots:
        overrides["roots"] = tuple(r.strip() for r in args.roots.split(",") if r.strip())
    if args.ext:
        overrides["exts"] = tuple(e.strip() for e in args.ext.split(",") if e.strip())
    for flag in ("gamma_form", "relation", "gap", "signs", "minus_forms", "glue", "comments"):
        value = getattr(args, flag)
        if value:
            overrides[flag] = value
    if args.no_magnitude_guard:
        overrides["magnitude_guard"] = False
    if args.exclude_glob:
        overrides["exclude_globs"] = tuple(args.exclude_glob)
    if args.channel:
        overrides["channels"] = tuple(args.channel)
    if args.sign:
        overrides["sign_filter"] = tuple(args.sign)
    if args.require_channel:
        overrides["require_channel"] = True
    return replace(base, **overrides), args.preset


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    repo = Path(args.repo).resolve() if args.repo else Path(__file__).resolve().parents[2]

    if args.reconcile:
        text, rows = render_reconciliation(repo, args.check)
        print(text)
        if args.json_path:
            Path(args.json_path).write_text(
                json.dumps(
                    {"schema": "signed-gamma-reconciliation/1", "rows": rows},
                    indent=2,
                    sort_keys=True,
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )
        disagreed = [r for r in rows if r["cross_check"] == "DISAGREE"]
        if disagreed:
            print(
                "\nSELF-CHECK FAILED - the two scan methods disagree. This is an\n"
                "instrument bug, not a corpus finding. Presets: "
                + ", ".join(r["preset"] for r in disagreed),
                file=sys.stderr,
            )
            return 3
        return 0

    universe, preset = universe_from_args(args)
    payload, checked = build_census(
        repo, universe, preset=preset, check=args.check, include_sites=args.sites
    )
    print(render_summary(payload))
    if args.json_path:
        Path(args.json_path).write_text(
            json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    if checked is not None and not checked.agree:
        print(
            "\nSELF-CHECK FAILED - method A and method B disagree on the raw\n"
            "detection set. A census whose two methods disagree is not a census;\n"
            "this is an instrument bug, not a statement about the corpus.",
            file=sys.stderr,
        )
        return 3
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
