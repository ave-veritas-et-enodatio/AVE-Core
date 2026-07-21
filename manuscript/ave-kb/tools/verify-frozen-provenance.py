#!/usr/bin/env python3
"""Frozen-label provenance gate for AVE-Core research result docs.

The machine version of the house rule "a criterion labeled *Frozen* in a result
doc must actually be frozen — i.e. present, byte-identically, in the lane's
committed prereg." Twice in the 2026-07-20/21 window a result doc shipped a
`Frozen:`-labeled string that did NOT match the lane's prereg, each caught only
by adversarial review:

  * **PR #770** — the driver JSON carried a HARD-CODED note
    ``"ROBUST across rail depth (S_RAIL 0.03->0.003 all RISING, pressure-tested)"``
    surfaced as a frozen/pressure-tested result. It was never in the prereg and
    never computed (only ``S_RAIL=0.03`` was run). A fabricated string labeled
    as frozen. (`research/2026-07-20_constituent-cage-ensemble_result.md` sec 7.5.)
  * **PR #782** — the Lamé gate was banked on an ABSOLUTE two-shell agreement
    ``|ext1-ext2| <= 0.10`` mislabeled ``"Frozen:"``, swapped for the actual
    frozen criterion ``|Delta|/mean <= 0.25`` (prereg sec 4 Leg 2). A swapped
    criterion vs its prereg. (`research/2026-07-21_rve-aggregation-bench_result.md`
    sec 7.6.)

An instruction that fails twice becomes a tool; this is that tool.

WHAT IT CHECKS
--------------
In each ``research/**/*result.md`` (result docs; ``_result.md`` / ``-result.md``
/ ``_RESULT.md``), every line carrying a *Frozen label* — the token
``Frozen:`` (optionally hyphen-qualified ``Frozen-wall:`` or parenthesised
``Frozen (Leg 5):``), case-insensitive, at a real label position (NOT a quoted
mention like ``"Frozen:"`` in a disclosure sentence) — is inspected for the
*frozen criterion* it labels: the first inline-code span `` `...` `` or
double-quoted ``"..."`` string that FOLLOWS the label on that line.

That quoted criterion must appear **byte-identically** as a substring of the
lane's **prereg file content** (the working tree; or the pinned commit's blob
when the doc carries a ``Prereg-commit:`` line and ``git show`` resolves it
cheaply). Reconcile-don't-declare: the comparison target is ALWAYS the prereg
file's bytes — never a self-declared echo elsewhere in the result doc. A
labeled criterion absent from the prereg is a FAIL with a precise message
(doc:line, the label, the criterion, the prereg path, and what was tried).

PREREG RESOLUTION (machine-readable pointer convention)
-------------------------------------------------------
The lane's prereg is resolved, in priority order:

  1. **Explicit pointer (the convention new docs MUST carry).** A line
     ``Prereg-file: <path>`` near the top (bold / blockquote / link-wrapped
     forms accepted). An optional companion ``Prereg-commit: <sha>`` pins the
     blob to compare against (else the working tree is used).
  2. **Header heuristic (legacy).** The first ``research/...prereg....md`` path
     referenced in the doc's header region (the corpus habit
     "Resolves the frozen bins of `research/..._prereg-FROZEN.md`").
  3. **Naming convention (legacy).** ``<stem>_prereg-FROZEN.md`` /
     ``<stem>_prereg.md`` / ``<stem>-prereg.md`` / ``<stem>_prereg_and_derivation.md``
     beside the result doc, where ``<stem>`` is the filename minus ``[-_]result.md``.

A GATING doc (see below) that carries Frozen labels but resolves NO prereg by
ANY method is a HARD FAIL — "add a machine-readable ``Prereg-file: <path>``
line." A gating doc that resolves only via heuristic/naming (no explicit line)
PASSES the resolution but emits an ADVISORY recommending the explicit pointer
(recommend-but-don't-enforce, surfaced — never silent).

GATING DESIGN (date cutoff + explicit grandfather list)
-------------------------------------------------------
Gating is by the result doc's *effective date* — ``max(filename date, first-add
date)`` — against ``gating_date`` in the checked-in grandfather list
(``frozen-provenance-grandfather.json``, default 2026-07-22). The filename date
is the ``YYYY-MM-DD`` prefix; the first-add date is the doc's earliest commit
under ``research/``, read in ONE ``git log --diff-filter=A`` pass (never a
per-file subprocess). Keying on the MAX closes the **backdated-filename
evasion**: a brand-new bad doc named ``2026-07-01_*.md`` cannot buy the warn
path with a stale prefix — its add date gates it.

  * effective date **>= gating_date** -> a Frozen-mismatch or a missing-prereg
    is a HARD FAIL (exit 1).
  * effective date **< gating_date** -> WARN-ONLY (grandfathered by the pre-gate
    date); printed, never gating. The two known incidents are annotated in the
    grandfather list as caught-and-corrected.
  * an **untracked / uncommitted** result doc has no add date and is treated as
    gating-dated (it is new by definition — a stale filename cannot exempt it).
  * if **git is unavailable** the filename date is used and a single advisory
    records that the add-date cross-check was skipped (fail-open on the
    cross-check, never on the byte-check).
  * ``grandfathered_result_docs`` in the list is an explicit escape hatch: a
    named doc is warn-only even if dated on/after the cutoff (normally empty;
    the diff is reviewable).

SCOPE HONESTY — what this gate CANNOT catch (documented, not force-fitted)
-------------------------------------------------------------------------
  * **A criterion frozen WRONG in the prereg itself.** Garbage-in: if the
    prereg already carries the wrong criterion, the result-vs-prereg byte-match
    passes. This gate checks result<->prereg consistency, not prereg
    correctness — that is an adversarial-review / physics job.
  * **Prose paraphrases that avoid the ``Frozen:`` label.** A frozen claim
    written without the label, or the criterion stated in running prose, is not
    inspected. Only labeled, QUOTED criteria are byte-verified.
  * **Label-avoidance (PARTIALLY surfaced).** Dropping the label entirely, or
    wording the criterion unquoted so no code-span / double-quote token is
    extractable, dodges the byte-check (an unquoted labeled line is reported as
    an ADVISORY "Frozen label with no quoted criterion — verify manually", never
    gated). ONE specific dodge IS surfaced (advisory): the **quoted-label
    smuggle** ``"Frozen:" `<criterion>` `` — a QUOTED ``"Frozen:"`` token (which
    the label lookbehind renders invisible, so a disclosure mention doesn't
    self-trip) immediately followed by a quoted criterion. That proximity shape
    is flagged; a *paraphrase with no label at all* is still not caught. Do NOT
    read this as "all label-avoidance is caught" — only the adjacent-quoted-token
    smuggle is.
  * **Semantic equivalence.** A criterion that MEANS the same but differs by a
    byte (``<= 0.10`` vs ``<=0.10``; ``≤`` vs ``<=``; reordered terms) fails the
    byte-match. This is a deliberate false-positive-toward-safety: the fix is to
    quote the criterion in the result doc identically to the prereg — which is
    the whole point of a *frozen* criterion.
  * **Backdated filename (GUARDED).** A stale ``YYYY-MM-DD`` prefix on an
    otherwise-new doc used to buy the warn path (severity keyed on the filename
    alone). GUARD: severity now keys on ``max(filename date, first-add date)``
    and treats untracked docs as gating-dated, so a backdated new doc gates.
    RESIDUAL: only when git is unavailable does the check fall back to the
    filename date (an explicit advisory says so) — that fallback window is the
    remaining, surfaced, exposure.

The gate's runtime is trivial: pure text scan + substring resolve, stdlib only
(one optional ``git show`` per pinned-commit doc). See ``verify-frozen-provenance``
in the Makefile.
"""

import argparse
import json
import logging
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

logger = logging.getLogger("verify-frozen-provenance")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCAN_ROOT_REL = "research"

# Result-doc filename suffix (case-insensitive): `_result.md`, `-result.md`,
# `_RESULT.md`. A leading YYYY-MM-DD prefix carries the gating date.
_RESULT_NAME_RE = re.compile(r"[-_]result\.md$", re.IGNORECASE)
_DATE_PREFIX_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")

# Never crawled (single path segment at any depth). `_archive` is a frozen
# archive — intentionally stale, must not gate.
SKIP_DIRS = {".venv", "venv", ".git", "build", "node_modules", ".index",
             ".agents", "_archive", "__pycache__"}

# Default gate cutoff — overridden by the grandfather list's `gating_date`.
DEFAULT_GATING_DATE = date(2026, 7, 22)

GRANDFATHER_FILENAME = "frozen-provenance-grandfather.json"

# ---------------------------------------------------------------------------
# Grammar
# ---------------------------------------------------------------------------
#
# A Frozen LABEL: the word Frozen (optionally `-qualified` or `(parenthesised)`)
# immediately followed by a colon, at a real label position. The negative
# lookbehind excludes a preceding word char / hyphen / quote char so a MENTION
# — e.g. `mislabeled "Frozen:"` in a disclosure sentence — is NOT read as a
# label (those are the corrective texts; they must not trip the gate).
_FROZEN_LABEL_RE = re.compile(
    r"""(?<![\w"'`\-])[Ff]rozen(?:-[A-Za-z]+)?(?:\s*\([^)\n]*\))?:"""
)

# The frozen CRITERION is the first inline-code span OR double-quoted string
# that follows the label. Inline code is preserved (the criterion usually lives
# in backticks); only FENCED blocks are blanked (a fenced example is not a live
# label). Both patterns capture the verbatim inner text.
_CODE_SPAN_RE = re.compile(r"`([^`]+)`")
_DQUOTE_RE = re.compile(r'"([^"]+)"')

# REPAIR 2 (audit 3b): quoted-label SMUGGLE shape. The label lookbehind above
# deliberately makes a QUOTED `"Frozen:"` invisible (so a disclosure MENTION
# doesn't self-trip) — but that same exclusion lets someone smuggle a frozen
# criterion past the byte-check by quoting the label: `"Frozen:" <criterion>`.
# We surface (advisory, never gating) the specific smuggle shape: a QUOTED
# Frozen-label token IMMEDIATELY followed (only markdown emphasis / whitespace
# between) by a backticked/quoted criterion-like token. The proximity constraint
# is what keeps it off the real disclosure lines (`mislabeled "Frozen:"` then
# PROSE, criterion far away) — regression-checked against the corrected
# #770/#782 docs (both stay 0-findings).
_QUOTED_FROZEN_SMUGGLE_RE = re.compile(
    r"""["'`][Ff]rozen(?:-[A-Za-z]+)?(?:\s*\([^)\n]*\))?:["'`]"""  # a QUOTED Frozen: token
    r"""[ \t*_]*"""                                                # only md-emphasis / space
    r"""(?=`[^`\n]+`|"[^"\n]+")"""                                 # then, immediately, a quoted criterion
)

# Explicit machine-readable pointer: `Prereg-file: <path>` (bold / blockquote /
# link-wrapped forms accepted). `Prereg-commit: <sha>` optionally pins the blob.
_PREREG_FILE_RE = re.compile(
    r"^[ \t]*>?[ \t]*[*_]{0,3}Prereg-file[*_]{0,3}[ \t]*:[ \t]*"
    r"(?:[*_`]{1,3})?(?:\[[^\]]*\]\()?"
    r"([A-Za-z0-9_./\-]+\.md)",
    re.IGNORECASE | re.MULTILINE,
)
_PREREG_COMMIT_RE = re.compile(
    r"^[ \t]*>?[ \t]*[*_]{0,3}Prereg-commit[*_]{0,3}[ \t]*:[ \t]*"
    r"(?:[*_`]{1,3})?([0-9a-f]{7,40})\b",
    re.IGNORECASE | re.MULTILINE,
)
# Header-heuristic (legacy): first `research/...prereg....md` path reference.
_PREREG_PATH_RE = re.compile(
    r"(research/[A-Za-z0-9_./\-]*prereg[A-Za-z0-9_./\-]*\.md)", re.IGNORECASE
)
_HEADER_LINES = 40  # header region scanned for the heuristic reference


# ---------------------------------------------------------------------------
# Discovery + crawl (mirrors verify-provenance-stamps)
# ---------------------------------------------------------------------------

def find_repo_root(start: Path) -> Path:
    """Walk up from `start` to the AVE-Core repo root (Makefile + manuscript/)."""
    for parent in (start, *start.parents):
        if (parent / "Makefile").is_file() and (parent / "manuscript").is_dir():
            return parent
    for parent in (start, *start.parents):
        if (parent / ".git").exists():
            return parent
    return start


def iter_result_markdown(repo_root: Path):
    """Yield every result doc under research/, skipping SKIP_DIRS at any depth."""
    scan_root = repo_root / SCAN_ROOT_REL
    if not scan_root.is_dir():
        return
    for path in sorted(scan_root.rglob("*.md")):
        if not _RESULT_NAME_RE.search(path.name):
            continue
        parts = path.relative_to(repo_root).parts
        if any(part in SKIP_DIRS for part in parts):
            continue
        yield path


def strip_fenced_code(text: str) -> str:
    """Blank ``` / ~~~ fenced blocks, preserving line count and INLINE code.

    A Frozen label inside a fenced example is documentation, not a live label,
    so fenced blocks are blanked. Inline code spans are PRESERVED — the frozen
    criterion usually lives in a `code span`, and blanking it would erase the
    very token this gate must byte-check.
    """
    out: list[str] = []
    fence: str | None = None
    for raw in text.splitlines():
        stripped = raw.lstrip()
        if fence is None:
            if stripped.startswith("```") or stripped.startswith("~~~"):
                fence = stripped[:3]
                out.append("")
                continue
            out.append(raw)
        else:
            out.append("")
            if stripped.startswith(fence):
                fence = None
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Frozen-label + criterion extraction
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FrozenLabel:
    line: int             # 1-based line number
    label: str            # the matched label text, e.g. "Frozen:" / "Frozen-wall:"
    criterion: str | None  # the quoted criterion inner text, or None if unquoted


def _first_quoted_token(suffix: str) -> str | None:
    """First inline-code span OR double-quoted string in `suffix` (inner text)."""
    code = _CODE_SPAN_RE.search(suffix)
    dq = _DQUOTE_RE.search(suffix)
    if code and dq:
        return (code if code.start() <= dq.start() else dq).group(1)
    if code:
        return code.group(1)
    if dq:
        return dq.group(1)
    return None


def extract_frozen_labels(text: str) -> list[FrozenLabel]:
    """Every Frozen label + the criterion it labels, across a doc's fence-stripped body."""
    labels: list[FrozenLabel] = []
    lines = strip_fenced_code(text).splitlines()
    for idx, line in enumerate(lines, start=1):
        matches = list(_FROZEN_LABEL_RE.finditer(line))
        for i, m in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(line)
            suffix = line[m.end():end]
            labels.append(
                FrozenLabel(line=idx, label=m.group(0),
                            criterion=_first_quoted_token(suffix))
            )
    return labels


def find_quoted_label_smuggles(text: str) -> list[int]:
    """1-based line numbers of the quoted-label SMUGGLE shape (REPAIR 2).

    A QUOTED `"Frozen:"` token immediately followed by a backticked/quoted
    criterion-like token — the shape that presents a frozen criterion while
    dodging the byte-check via the label lookbehind. The proximity constraint
    keeps this OFF real disclosure lines (`mislabeled "Frozen:"` + prose)."""
    hits: list[int] = []
    for idx, line in enumerate(strip_fenced_code(text).splitlines(), start=1):
        if _QUOTED_FROZEN_SMUGGLE_RE.search(line):
            hits.append(idx)
    return hits


# ---------------------------------------------------------------------------
# Date parsing
# ---------------------------------------------------------------------------

def parse_doc_date(filename: str) -> date | None:
    m = _DATE_PREFIX_RE.match(filename)
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


# NUL-adjacent unit-separator sentinel so a commit-header line is never confused
# with a `research/...` path line in the single `git log` pass.
_GITLOG_SENTINEL = "\x1f"


def build_add_date_map(repo_root: Path) -> tuple[dict[str, date] | None, str | None]:
    """First-commit (add) date per ``research/`` path, in ONE ``git log`` pass.

    Returns ``(map, error)``. ``map`` is repo-root-relative posix path ->
    earliest add date (``--reverse`` => oldest first => ``setdefault`` keeps the
    first add). On ANY git failure returns ``(None, reason)`` so the caller
    falls back to filename dates and emits a single 'cross-check skipped'
    advisory (fail-open on the cross-check, never on the byte-check). Exactly one
    subprocess — never a per-file call.
    """
    try:
        out = subprocess.run(
            ["git", "-C", str(repo_root), "log", "--reverse",
             "--diff-filter=A", f"--format={_GITLOG_SENTINEL}%ad",
             "--date=short", "--name-only", "--", SCAN_ROOT_REL],
            capture_output=True, text=True, timeout=60,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return None, f"git unavailable ({exc})"
    if out.returncode != 0:
        return None, f"git log failed (rc={out.returncode}: {out.stderr.strip()[:120]})"

    add_dates: dict[str, date] = {}
    cur: date | None = None
    for line in out.stdout.splitlines():
        if line.startswith(_GITLOG_SENTINEL):
            raw = line[len(_GITLOG_SENTINEL):].strip()
            try:
                y, mo, d = (int(x) for x in raw.split("-"))
                cur = date(y, mo, d)
            except (ValueError, AttributeError):
                cur = None
            continue
        path = line.strip()
        if path and cur is not None:
            add_dates.setdefault(path, cur)  # oldest add wins
    return add_dates, None


# ---------------------------------------------------------------------------
# Prereg resolution + content read
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PreregRef:
    path: Path | None     # resolved prereg absolute path (None if unresolved)
    method: str           # "explicit" | "header-heuristic" | "naming" | "none"
    commit: str | None    # pinned commit sha, or None (working tree)


def _resolve_candidate(repo_root: Path, doc_dir: Path, raw: str) -> Path | None:
    """Resolve a path token against repo root, research/, and the doc's dir."""
    raw = raw.strip().strip("`*[]()").strip()
    if not raw:
        return None
    for base in (repo_root, repo_root / SCAN_ROOT_REL, doc_dir):
        cand = (base / raw).resolve()
        if cand.is_file():
            return cand
    return None


def resolve_prereg(doc_path: Path, text: str, repo_root: Path) -> PreregRef:
    """Resolve the lane's prereg by explicit pointer, header heuristic, then naming."""
    doc_dir = doc_path.parent
    commit_m = _PREREG_COMMIT_RE.search(text)
    commit = commit_m.group(1) if commit_m else None

    # 1. Explicit machine-readable pointer.
    m = _PREREG_FILE_RE.search(text)
    if m:
        cand = _resolve_candidate(repo_root, doc_dir, m.group(1))
        return PreregRef(path=cand, method="explicit", commit=commit)

    # 2. Header heuristic — first research/...prereg....md reference near the top.
    header = "\n".join(text.splitlines()[:_HEADER_LINES])
    hm = _PREREG_PATH_RE.search(header)
    if hm:
        cand = _resolve_candidate(repo_root, doc_dir, hm.group(1))
        if cand:
            return PreregRef(path=cand, method="header-heuristic", commit=commit)

    # 3. Naming convention beside the result doc.
    stem = _RESULT_NAME_RE.sub("", doc_path.name)
    for suffix in ("_prereg-FROZEN.md", "_prereg.md", "-prereg-FROZEN.md",
                   "-prereg.md", "_prereg_and_derivation.md"):
        cand = doc_dir / f"{stem}{suffix}"
        if cand.is_file():
            return PreregRef(path=cand.resolve(), method="naming", commit=commit)

    return PreregRef(path=None, method="none", commit=commit)


def read_prereg_content(ref: PreregRef, repo_root: Path) -> tuple[str | None, str]:
    """Read the prereg bytes to compare against. Returns (content, source-note).

    Working tree by default (reconcile-don't-declare: the live prereg content).
    If the doc pins a commit AND `git show` resolves it cheaply, that blob is
    used (the doc's declared freeze point) with a note; else the working tree.
    """
    if ref.path is None:
        return None, "unresolved"
    if ref.commit:
        try:
            rel = ref.path.resolve().relative_to(repo_root).as_posix()
            out = subprocess.run(
                ["git", "-C", str(repo_root), "show", f"{ref.commit}:{rel}"],
                capture_output=True, text=True, timeout=10,
            )
            if out.returncode == 0:
                return out.stdout, f"git show {ref.commit[:8]}:{rel}"
        except (OSError, subprocess.SubprocessError):
            pass
        logger.info("pinned commit %s unresolved for %s — using working tree",
                    ref.commit, ref.path)
    try:
        return ref.path.read_text(encoding="utf-8"), "working tree"
    except (OSError, UnicodeDecodeError) as exc:
        logger.warning("could not read prereg %s: %s", ref.path, exc)
        return None, f"read-error: {exc}"


# ---------------------------------------------------------------------------
# Findings
# ---------------------------------------------------------------------------

# kind values, in decreasing severity:
#   "no-prereg"  — Frozen labels present, no prereg resolvable (gating-eligible)
#   "mismatch"   — quoted criterion NOT byte-present in the prereg (gating-eligible)
#   "unquoted"   — Frozen label, no quoted criterion (ADVISORY, never gating)
#   "no-explicit-pointer" — resolved via fallback, lacks Prereg-file line
#                  (ADVISORY; ESCALATES to gating on a cross-lane header-heuristic
#                  resolution of a gating-dated doc — see resolve_prereg / REPAIR 3)
#   "git-skipped" — add-date cross-check skipped, git unavailable (ADVISORY, once)
#   "smuggle"    — quoted `"Frozen:"` + adjacent criterion (label-dodge; ADVISORY)
_ADVISORY_KINDS = {"unquoted", "no-explicit-pointer", "git-skipped", "smuggle"}


@dataclass(frozen=True)
class Finding:
    file: Path
    line: int          # 1-based; 0 for whole-doc findings (no-prereg)
    kind: str
    detail: str
    doc_date: date | None
    gating: bool       # True => contributes to exit 1


# ---------------------------------------------------------------------------
# Scan
# ---------------------------------------------------------------------------

def scan_doc(
    doc_path: Path,
    repo_root: Path,
    gating_date: date,
    grandfathered_docs: set[str],
    add_dates: dict[str, date] | None = None,
) -> list[Finding]:
    """Return findings for one result doc (empty if clean or no Frozen labels).

    ``add_dates`` (REPAIR 1): repo-relative-posix -> first-commit date, from the
    single ``build_add_date_map`` pass. When provided, severity keys on
    ``max(filename date, add date)`` and an untracked doc (absent from the map)
    is treated as gating-dated. When ``None`` (git unavailable, or a direct
    caller opting out) the legacy filename-date-only rule applies.
    """
    try:
        text = doc_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        logger.warning("could not read %s: %s", doc_path, exc)
        return []

    labels = extract_frozen_labels(text)
    # REPAIR 2: quoted-label smuggles are detected even when the doc has NO real
    # label (that is the whole dodge), so this must run before the early return.
    smuggles = find_quoted_label_smuggles(text)
    if not labels and not smuggles:
        return []

    doc_date = parse_doc_date(doc_path.name)
    try:
        rel = doc_path.resolve().relative_to(repo_root).as_posix()
    except ValueError:
        rel = doc_path.name

    def is_gating(default: bool = True) -> bool:
        """A finding gates iff the doc's EFFECTIVE date is on/after the cutoff,
        it is not an explicit grandfather-list exemption, and the kind is
        enforceable. Effective date = max(filename date, first-add date); an
        untracked doc gates (new by definition); no map -> filename date only."""
        if not default:
            return False
        if rel in grandfathered_docs:
            return False
        if add_dates is None:
            # Fallback (git unavailable / direct opt-out): filename date only.
            if doc_date is None:
                return False  # undated -> cannot gate (warn-only)
            return doc_date >= gating_date
        add_date = add_dates.get(rel)
        if add_date is None:
            return True  # untracked / uncommitted -> new by definition -> gating
        candidates = [d for d in (doc_date, add_date) if d is not None]
        return bool(candidates) and max(candidates) >= gating_date

    findings: list[Finding] = []

    # REPAIR 2: surface (advisory) each quoted-label smuggle shape.
    for ln in smuggles:
        findings.append(Finding(
            file=doc_path, line=ln, kind="smuggle",
            detail=("a QUOTED `\"Frozen:\"` token is immediately followed by a "
                    "backticked/quoted criterion — this shape dodges the "
                    "Frozen-label byte-check; use a REAL (unquoted) Frozen label "
                    "so the criterion is verified against the prereg"),
            doc_date=doc_date, gating=False,
        ))

    if not labels:
        return findings  # smuggle-only doc: nothing to byte-check

    ref = resolve_prereg(doc_path, text, repo_root)

    # No prereg resolvable at all -> hard-fail (gating docs) / warn (pre-gate).
    if ref.path is None:
        findings.append(Finding(
            file=doc_path, line=0, kind="no-prereg",
            detail=("carries Frozen label(s) but no prereg resolves — add a "
                    "machine-readable `Prereg-file: <path>` line near the top"),
            doc_date=doc_date, gating=is_gating(),
        ))
        # Cannot byte-check any criterion without a prereg; stop here.
        return findings

    prereg_text, source = read_prereg_content(ref, repo_root)
    prereg_rel = _rel(ref.path, repo_root)

    # Resolved only via fallback on a gating doc -> advisory to add the pointer.
    if ref.method != "explicit" and is_gating():
        findings.append(Finding(
            file=doc_path, line=0, kind="no-explicit-pointer",
            detail=(f"prereg resolved via {ref.method} ({prereg_rel}); add an "
                    f"explicit `Prereg-file: {prereg_rel}` line (convention)"),
            doc_date=doc_date, gating=False,
        ))

    if prereg_text is None:
        findings.append(Finding(
            file=doc_path, line=0, kind="no-prereg",
            detail=f"prereg {prereg_rel} could not be read ({source})",
            doc_date=doc_date, gating=is_gating(),
        ))
        return findings

    for lab in labels:
        if lab.criterion is None:
            findings.append(Finding(
                file=doc_path, line=lab.line, kind="unquoted",
                detail=(f"{lab.label!r} labels no quoted criterion — quote the "
                        f"frozen criterion in `backticks` or \"quotes\" so it "
                        f"can be byte-checked against {prereg_rel}"),
                doc_date=doc_date, gating=False,
            ))
            continue
        if lab.criterion not in prereg_text:
            findings.append(Finding(
                file=doc_path, line=lab.line, kind="mismatch",
                detail=(f"{lab.label!r} criterion {lab.criterion!r} is NOT "
                        f"byte-present in the prereg {prereg_rel} ({source})"),
                doc_date=doc_date, gating=is_gating(),
            ))
    return findings


def _rel(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root).as_posix()
    except ValueError:
        return str(path)


def scan(repo_root: Path, gating_date: date, grandfathered_docs: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    # REPAIR 1: one git pass builds the file->first-add-date map for the
    # backdated-filename cross-check. On git failure -> fallback + one advisory.
    add_dates, git_err = build_add_date_map(repo_root)
    if git_err is not None:
        findings.append(Finding(
            file=repo_root, line=0, kind="git-skipped",
            detail=(f"add-date cross-check skipped ({git_err}); gating keyed on "
                    f"filename date only — a backdated-filename evasion is NOT "
                    f"cross-checked in this run"),
            doc_date=None, gating=False,
        ))
    for doc in iter_result_markdown(repo_root):
        findings.extend(scan_doc(doc, repo_root, gating_date, grandfathered_docs, add_dates))
    return findings


# ---------------------------------------------------------------------------
# Grandfather list I/O
# ---------------------------------------------------------------------------

def grandfather_path(repo_root: Path) -> Path:
    return repo_root / "manuscript" / "ave-kb" / "tools" / GRANDFATHER_FILENAME


def load_config(repo_root: Path) -> tuple[date, set[str], list[dict]]:
    """Return (gating_date, grandfathered_result_docs, incidents)."""
    path = grandfather_path(repo_root)
    if not path.is_file():
        logger.info("no grandfather list at %s (default gating date)", path)
        return DEFAULT_GATING_DATE, set(), []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        logger.warning("could not read %s: %s (defaults)", path, exc)
        return DEFAULT_GATING_DATE, set(), []
    gd = DEFAULT_GATING_DATE
    raw_gd = data.get("gating_date")
    if raw_gd:
        try:
            y, m, d = (int(x) for x in raw_gd.split("-"))
            gd = date(y, m, d)
        except (ValueError, AttributeError):
            logger.warning("bad gating_date %r — using default", raw_gd)
    docs = set(data.get("grandfathered_result_docs", []))
    incidents = list(data.get("incidents", []))
    return gd, docs, incidents


# ---------------------------------------------------------------------------
# Report + CLI
# ---------------------------------------------------------------------------

def report(findings: list[Finding], incidents: list[dict], repo_root: Path) -> None:
    gating = [f for f in findings if f.gating]
    warn = [f for f in findings if not f.gating]

    def loc(f: Finding) -> str:
        r = _rel(f.file, repo_root)
        return f"{r}:{f.line}" if f.line else r

    if incidents:
        print("[verify-frozen-provenance] known incidents (annotated, caught-and-corrected):")
        for inc in incidents:
            print(f"  - #{inc.get('pr','?')} {inc.get('class','')}: "
                  f"{inc.get('doc','?')} — {inc.get('status','')}")
    for f in sorted(warn, key=lambda x: (str(x.file), x.line)):
        tag = "advisory" if f.kind in _ADVISORY_KINDS else "warn/pre-gate"
        print(f"{loc(f)}  [{f.kind} · {tag}]  {f.detail}")
    for f in sorted(gating, key=lambda x: (str(x.file), x.line)):
        print(f"{loc(f)}  [{f.kind}]  FAIL: {f.detail}")


def run(repo_root: Path) -> tuple[list[Finding], list[Finding], list[dict]]:
    """Scan + split into (gating, warn, incidents). Shared by main() and tests."""
    gating_date, gf_docs, incidents = load_config(repo_root)
    findings = scan(repo_root, gating_date, gf_docs)
    gating = [f for f in findings if f.gating]
    warn = [f for f in findings if not f.gating]
    return gating, warn, incidents


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--root", type=Path, default=None,
                        help="repo root to scan (default: auto-detected)")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="info-level logging")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )

    repo_root = (args.root or find_repo_root(Path(__file__).resolve())).resolve()
    gating_date, gf_docs, incidents = load_config(repo_root)
    logger.info("scanning result docs under %s (gating date %s)",
                repo_root / SCAN_ROOT_REL, gating_date.isoformat())

    findings = scan(repo_root, gating_date, gf_docs)
    report(findings, incidents, repo_root)

    n_docs = sum(1 for _ in iter_result_markdown(repo_root))
    gating = [f for f in findings if f.gating]
    warn = [f for f in findings if not f.gating]
    print(
        f"\n[verify-frozen-provenance] result docs scanned: {n_docs}  |  "
        f"findings: {len(findings)} ({len(gating)} gating, {len(warn)} warn/advisory)  |  "
        f"gating date: {gating_date.isoformat()}",
        file=sys.stderr,
    )
    if gating:
        print(
            "[verify-frozen-provenance] A criterion labeled `Frozen:` in a result "
            "doc must appear byte-identically in the lane's prereg. Fix the "
            "labeled criterion (quote it as the prereg does), add a resolvable "
            "`Prereg-file: <path>` line, or — for a legacy pre-gate doc — the "
            "date cutoff already exempts it. See the module docstring.",
            file=sys.stderr,
        )
    return 1 if gating else 0


if __name__ == "__main__":
    raise SystemExit(main())
