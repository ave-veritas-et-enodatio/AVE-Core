#!/usr/bin/env python3
"""Provenance-stamp gate for AVE-Core research docs.

The machine version of the house rule "a validation stamp must have a matching
artifact." Four times in one session, research docs carried
`driver-confirmed` / `test-locked` / `sympy-verified` stamps for checks that did
not exist in the shipped artifacts (the print-vs-compute class). An instruction
that fails repeatedly becomes a tool; this is that tool.

WHAT IT CHECKS
--------------
In `research/**/*.md`, every occurrence of a *provenance stamp token* — an
assertion that a computation / test in a SHIPPED ARTIFACT confirmed a result —
must carry an artifact reference on the same line or in the immediately-adjacent
parenthetical. The reference is one of:

  * an in-tree file path                         `pump_probe_predictions.py`
  * a file path with a :line suffix              `scale_invariant.py:107-156`
  * a pytest node id / named symbol on a path    `path/test_x.py::test_name`
                                                 `tensors.py::compute_toroidal_halo_volume`

The gate RESOLVES each reference: the file must exist in-tree (basename or
path-suffix match, mirroring verify-md-links' \\kbleaf resolver); when
`::symbol` (or `:line`) is given the file must exist AND, for `::symbol`, the
symbol name must appear in that file. An unresolvable stamp is a FAIL with a
precise message (doc:line, the stamp token, and what was tried).

Symbol resolution is a bare-word grep, NOT an AST parse: `::verify_reciprocity`
is satisfied iff the token `verify_reciprocity` appears anywhere in the resolved
file (as a def, a call, or even a docstring mention). This is deliberately the
same coarse "the file mentions this symbol" check verify-md-links uses for its
`path::member` \\kbleaf cites — it catches the print-vs-compute failure (the
NAMED function/test simply is not in the artifact) without coupling the gate to
Python's grammar or to non-Python artifacts (a pytest node id, a Mathematica
symbol, a JSON key).

THE STAMP-TOKEN SET (surveyed from the live corpus, 2026-07-06)
---------------------------------------------------------------
The tokens below are the "print-vs-compute" class: each asserts that a
computation / test / symbolic-algebra run / engine run / finite-element run in a
shipped artifact was performed. These are exactly the stamps where a claim
without a matching artifact is the documented failure mode.

    driver-confirmed   test-locked      sympy-verified   sympy-confirmed
    engine-confirmed   engine-verified  FEM-verified

Matched case-insensitively, on a word boundary, OUTSIDE fenced / inline code
(a token inside a ``` fence or a `code span` is example text, not an assertion).

DELIBERATELY EXCLUDED (documented, not force-fitted):
  * `grep-confirmed` / `grep-verified` — a CORPUS-GREP action-class ("canon is
    silent on X", "grep-confirmed absent"), not a shipped-computational-artifact
    check. Its artifact is the corpus itself, not a single `path::symbol`;
    demanding a file+symbol for an absence-of-source finding is a semantic
    mismatch. (The motivation listed it with a trailing `?`; this is the
    adjudication.)
  * physics-vocabulary `-locked` / `-confirmed` forms (`phase-locked`,
    `vapor-locked`, `SNAP-LOCKED`, `HEAL-CONFIRMED`, `MOTION-LOCKED`,
    `NULL-CONFIRMED`, ...) — substrate-state descriptors, not provenance
    stamps.
  * process stamps (`Grant-confirmed`, `re-verified`, `corpus-confirmed`,
    `commit-verified`, `WebFetch-verified`) — human/agent-action provenance,
    not a shipped computational artifact.

LEGACY BASELINE (new/changed enforcement only)
----------------------------------------------
The gate is run over the existing corpus once; every current failure is
grandfathered into a checked-in baseline (`provenance-stamp-baseline.json`),
keyed by a STABLE content hash of the stamped line (path + normalized line
text, NOT the line number — line numbers drift on any insertion above). A
baselined failure passes UNTIL its line content changes; then the key no longer
matches and enforcement re-triggers for that stamp. The baseline may shrink
(fewer legacy failures is always allowed); a NEW/CHANGED unresolvable stamp
whose key is not in the baseline FAILS. Growing the baseline (adding a key the
gate did not itself emit) is not done by the gate — `--update-baseline`
regenerates it from the live scan, so a hand-added phantom key is overwritten.

The gate's own runtime is trivial: pure grep + path-resolve, no builds, no
imports beyond the standard library. See `verify-provenance-stamps` in the
Makefile and the "Provenance-stamp grammar" section of the repo README.
"""

import argparse
import hashlib
import json
import logging
import re
import sys
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger("verify-provenance-stamps")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# The provenance-stamp token set (see module docstring for the survey +
# exclusion rationale). Matched case-insensitively on a word boundary.
STAMP_TOKENS: tuple[str, ...] = (
    "driver-confirmed",
    "test-locked",
    "sympy-verified",
    "sympy-confirmed",
    "engine-confirmed",
    "engine-verified",
    "FEM-verified",
)

# One alternation, case-insensitive, hyphen-boundaried. `(?<![\w-])` / `(?![\w-])`
# so `re-sympy-verified` or `sympy-verifiedish` never matches, but ordinary
# punctuation ("(sympy-verified)", "sympy-verified.") does.
_STAMP_RE = re.compile(
    r"(?<![\w-])(" + "|".join(re.escape(t) for t in STAMP_TOKENS) + r")(?![\w-])",
    re.IGNORECASE,
)

# Only research/ docs are gated (the print-vs-compute failures were all there).
SCAN_ROOT_REL = "research"

# Never crawled (matched as a single path segment at any depth). `_archive`
# is a frozen archive — intentionally stale, must not gate.
SKIP_DIRS = {".venv", "venv", ".git", "build", "node_modules", ".index", ".agents", "_archive"}

# Baseline lives beside this tool, checked in, so its diff is reviewable.
BASELINE_FILENAME = "provenance-stamp-baseline.json"

# File extensions an artifact reference may legitimately name. A stamp's
# artifact is a shipped computational artifact — code, a driver, a test,
# a data/manifest file it emitted, or a KB/manuscript leaf that hosts the
# computed value.
_ARTIFACT_EXTS = {
    ".py", ".md", ".tex", ".json", ".jsonl", ".csv", ".txt",
    ".npy", ".npz", ".yaml", ".yml", ".stl", ".ipynb",
}

# Ephemeral / generated dirs excluded from the artifact target index (mirrors
# verify-md-links' _TARGET_INDEX_SKIP). `_archive` / `.index` ARE valid targets
# (tracked, present on a fresh checkout).
_TARGET_INDEX_SKIP = {".venv", "venv", ".git", "build", "node_modules", ".agents", "__pycache__"}


# ---------------------------------------------------------------------------
# Repo discovery + crawl (mirrors verify-md-links)
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


def iter_research_markdown(repo_root: Path):
    """Yield every `.md` under research/, skipping SKIP_DIRS at any depth."""
    scan_root = repo_root / SCAN_ROOT_REL
    if not scan_root.is_dir():
        return
    for path in sorted(scan_root.rglob("*.md")):
        parts = path.relative_to(repo_root).parts
        if any(part in SKIP_DIRS for part in parts):
            continue
        yield path


def strip_code(text: str) -> str:
    """Blank fenced code blocks + inline code spans, preserving line count.

    Identical semantics to verify-md-links.strip_code: a stamp token inside a
    ``` fence or a `code span` is example text, not an assertion, so it is not
    matched. Newlines preserved so reported line numbers stay accurate.
    """
    out_lines: list[str] = []
    fence: str | None = None
    for raw in text.splitlines():
        stripped = raw.lstrip()
        if fence is None:
            if stripped.startswith("```") or stripped.startswith("~~~"):
                fence = stripped[:3]
                out_lines.append("")
                continue
            out_lines.append(re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), raw))
        else:
            out_lines.append("")
            if stripped.startswith(fence):
                fence = None
    return "\n".join(out_lines)


# ---------------------------------------------------------------------------
# Artifact-reference grammar
# ---------------------------------------------------------------------------
#
# A reference is a file path that MAY carry a :line / :line-range suffix or a
# ::symbol (or :symbol) member suffix. It is matched from the RAW line (not the
# code-stripped one), because in the corpus these references live inside inline
# `code spans` (`scale_invariant.py:107-156`, `path/test_x.py::test_name`) — the
# very spans strip_code blanks. Requiring a recognized file extension keeps the
# match tight (prose words are not paths).
#
#   group(path)    the path up to the first suffix
#   group(line)    optional  :NNN  or  :NNN-MMM  or  :NNN--MMM
#   group(symbol)  optional  ::name  or  :name  (member / pytest node)
_EXT_ALT = "|".join(re.escape(e[1:]) for e in _ARTIFACT_EXTS)  # py|md|tex|...
_ARTIFACT_REF_RE = re.compile(
    r"(?P<path>[A-Za-z0-9_./\-]+\.(?:" + _EXT_ALT + r"))"
    r"(?P<line>:\d+(?:-{1,2}\d+)?)?"
    r"(?P<symbol>::[A-Za-z_][\w.]*(?:\(\))?|:[A-Za-z_][\w.]*(?:\(\))?)?",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ArtifactRef:
    raw: str          # verbatim match, e.g. "tensors.py::compute_x"
    path: str         # "tensors.py"
    symbol: str | None  # "compute_x" or None (a bare :line carries no symbol)


def extract_artifact_refs(raw_line: str) -> list[ArtifactRef]:
    """Pull every file-path artifact reference from a raw markdown line."""
    refs: list[ArtifactRef] = []
    for m in _ARTIFACT_REF_RE.finditer(raw_line):
        sym = m.group("symbol")
        symbol = None
        if sym:
            symbol = sym.lstrip(":").rstrip("()") or None
        refs.append(ArtifactRef(raw=m.group(0), path=m.group("path"), symbol=symbol))
    return refs


# ---------------------------------------------------------------------------
# Target index + resolution (path-suffix, mirrors verify-md-links' \kbleaf)
# ---------------------------------------------------------------------------

def build_target_index(repo_root: Path) -> dict[str, list[tuple[str, ...]]]:
    """Index repo files by basename -> [relative path-parts].

    Backs both bare-name (`foo.py`) and path-suffix (`a/b/foo.py`) resolution.
    Excludes gitignored / generated trees and nested worktrees; INCLUDES
    `_archive` and `.index` (tracked, legitimately citable).
    """
    files: dict[str, list[tuple[str, ...]]] = {}
    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        parts = path.relative_to(repo_root).parts
        if any(part in _TARGET_INDEX_SKIP for part in parts):
            continue
        files.setdefault(parts[-1], []).append(parts)
    return files


def _suffix_candidates(
    path: str, index: dict[str, list[tuple[str, ...]]]
) -> list[tuple[str, ...]]:
    """Real repo paths that END WITH the reference path (segment-wise)."""
    parts = tuple(p for p in path.split("/") if p and p != ".")
    if not parts:
        return []
    return [c for c in index.get(parts[-1], ()) if c[-len(parts):] == parts]


def _symbol_in_file(repo_root: Path, rel_parts: tuple[str, ...], symbol: str) -> bool:
    """True if `symbol` appears as a bare word in the file at rel_parts."""
    target = repo_root.joinpath(*rel_parts)
    try:
        text = target.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    return re.search(r"(?<![\w])" + re.escape(symbol) + r"(?![\w])", text) is not None


def resolve_ref(
    ref: ArtifactRef, repo_root: Path, index: dict[str, list[tuple[str, ...]]]
) -> str | None:
    """Resolve one artifact reference. Returns None on success, else a reason.

    * file must exist (basename or path-suffix match);
    * when `::symbol` is given, the symbol must appear in the resolved file.
    A `:line` suffix carries no symbol and is satisfied by file existence.
    """
    candidates = _suffix_candidates(ref.path, index)
    if not candidates:
        return f"file not found in-tree: {ref.path!r}"
    if ref.symbol is None:
        return None  # bare path / :line — file exists, satisfied
    # ::symbol — require the name in AT LEAST ONE resolved candidate file.
    if any(_symbol_in_file(repo_root, cand, ref.symbol) for cand in candidates):
        return None
    where = ref.path if len(candidates) == 1 else f"{ref.path} ({len(candidates)} matches)"
    return f"symbol {ref.symbol!r} not found in {where}"


# ---------------------------------------------------------------------------
# Findings + stable baseline key
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Finding:
    file: Path      # absolute path of the research .md
    line: int       # 1-based line number (for the human message; NOT the key)
    stamp: str      # the matched stamp token (lower-cased)
    reason: str     # why it failed (precise: what was tried)
    key: str        # stable content-hash baseline key (see baseline_key)


def _normalize_line(line: str) -> str:
    """Collapse whitespace so a re-wrap / re-indent that does not touch the
    stamp's textual content keeps the SAME baseline key. Any real content
    change (adding/removing a word, editing the stamp) changes the key and
    re-triggers enforcement — the design requirement."""
    return re.sub(r"\s+", " ", line).strip()


def baseline_key(repo_root: Path, md_file: Path, stamp: str, raw_line: str) -> str:
    """Stable key = hash(repo-relative-path + stamp + normalized line text).

    Deliberately NOT the line number: an insertion above a stamped line must not
    re-trigger every stamp below it. The path is included so an identical
    stamped sentence in two docs keys independently. Editing the stamped line's
    content changes the hash → the grandfather lapses and enforcement resumes.
    """
    try:
        rel = md_file.resolve().relative_to(repo_root).as_posix()
    except ValueError:
        rel = md_file.name
    payload = f"{rel}\x1f{stamp.lower()}\x1f{_normalize_line(raw_line)}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Scan
# ---------------------------------------------------------------------------

def scan_doc(
    md_file: Path, repo_root: Path, index: dict[str, list[tuple[str, ...]]]
) -> list[Finding]:
    """Return one Finding per UNRESOLVABLE stamp occurrence in `md_file`.

    A stamp on a line PASSES (no Finding) iff the raw line carries at least one
    artifact reference that resolves (`resolve_ref` returns None). Stamps inside
    fenced/inline code are not matched (scanned on the code-stripped body). The
    per-occurrence `reason` is the resolution failure that is closest to
    succeeding (a file-not-found is reported over a generic no-reference when a
    reference was present but wrong).
    """
    try:
        text = md_file.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        logger.warning("could not read %s: %s", md_file, exc)
        return []
    raw_lines = text.splitlines()
    stripped_lines = strip_code(text).splitlines()

    findings: list[Finding] = []
    for idx, stripped in enumerate(stripped_lines):
        if not _STAMP_RE.search(stripped):
            continue
        raw = raw_lines[idx] if idx < len(raw_lines) else stripped
        refs = extract_artifact_refs(raw)
        # Resolve every reference once; the line is satisfied if ANY resolves.
        reasons = [resolve_ref(r, repo_root, index) for r in refs]
        satisfied = any(reason is None for reason in reasons)
        if satisfied:
            continue
        # Not satisfied: report the most-informative reason. If a reference was
        # present but unresolvable, surface that; else "no artifact reference".
        wrong = [reason for reason in reasons if reason is not None]
        detail = wrong[0] if wrong else "no artifact reference on line (need path, path:line, or path::symbol)"
        # One Finding per stamp TOKEN occurrence on the line (a line may carry
        # more than one distinct stamp, e.g. two different tokens).
        for m in _STAMP_RE.finditer(stripped):
            stamp = m.group(1).lower()
            findings.append(
                Finding(
                    file=md_file,
                    line=idx + 1,
                    stamp=stamp,
                    reason=detail,
                    key=baseline_key(repo_root, md_file, stamp, raw),
                )
            )
    return findings


def scan(repo_root: Path, index: dict[str, list[tuple[str, ...]]]) -> list[Finding]:
    findings: list[Finding] = []
    for md_file in iter_research_markdown(repo_root):
        findings.extend(scan_doc(md_file, repo_root, index))
    return findings


# ---------------------------------------------------------------------------
# Baseline I/O
# ---------------------------------------------------------------------------

def baseline_path(repo_root: Path) -> Path:
    return repo_root / "manuscript" / "ave-kb" / "tools" / BASELINE_FILENAME


def load_baseline(repo_root: Path) -> dict[str, str]:
    """Return {key: doc:line-ish provenance note}. Empty if absent."""
    path = baseline_path(repo_root)
    if not path.is_file():
        logger.info("no baseline at %s (all stamps enforced)", path)
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        logger.warning("could not read baseline %s: %s (treating as empty)", path, exc)
        return {}
    return dict(data.get("grandfathered", {}))


def write_baseline(repo_root: Path, findings: list[Finding]) -> int:
    """Regenerate the baseline from the current live findings. Returns count.

    The value stored per key is a human-readable `doc:line  stamp  reason`
    provenance note (so a reviewer of the baseline diff sees WHAT was
    grandfathered), but only the KEY is load-bearing for the gate.
    """
    grandfathered: dict[str, str] = {}
    for f in sorted(findings, key=lambda x: (str(x.file), x.line)):
        try:
            rel = f.file.resolve().relative_to(repo_root).as_posix()
        except ValueError:
            rel = f.file.name
        grandfathered[f.key] = f"{rel}:{f.line}  [{f.stamp}]  {f.reason}"
    payload = {
        "_comment": (
            "Grandfathered provenance-stamp failures — generated by "
            "verify-provenance-stamps.py --update-baseline. Keys are stable "
            "content hashes (path+stamp+normalized-line); editing a stamped "
            "line changes its key and re-enables enforcement. This file may "
            "SHRINK freely; a new/changed unresolvable stamp fails the gate."
        ),
        "grandfathered": grandfathered,
    }
    path = baseline_path(repo_root)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return len(grandfathered)


# ---------------------------------------------------------------------------
# Report + CLI
# ---------------------------------------------------------------------------

def report(gating: list[Finding], grandfathered: list[Finding], repo_root: Path) -> None:
    def rel(f: Finding) -> str:
        try:
            return f.file.resolve().relative_to(repo_root).as_posix()
        except ValueError:
            return str(f.file)

    for f in sorted(grandfathered, key=lambda x: (str(x.file), x.line)):
        print(f"{rel(f)}:{f.line}  [{f.stamp} · grandfathered]  {f.reason}")
    for f in sorted(gating, key=lambda x: (str(x.file), x.line)):
        print(f"{rel(f)}:{f.line}  [{f.stamp}]  FAIL: {f.reason}")


def run(repo_root: Path) -> tuple[list[Finding], list[Finding]]:
    """Scan + split into (gating, grandfathered). Shared by main() and tests."""
    index = build_target_index(repo_root)
    baseline = load_baseline(repo_root)
    findings = scan(repo_root, index)
    gating = [f for f in findings if f.key not in baseline]
    grandfathered = [f for f in findings if f.key in baseline]
    return gating, grandfathered


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--root", type=Path, default=None,
        help="repo root to scan (default: auto-detected from this script's location)",
    )
    parser.add_argument(
        "--update-baseline", action="store_true",
        help="regenerate the grandfather baseline from the live scan (allowed to "
             "shrink; overwrites any hand-added phantom keys) and exit 0",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="info-level logging")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )

    repo_root = (args.root or find_repo_root(Path(__file__).resolve())).resolve()
    logger.info("scanning research root: %s", repo_root / SCAN_ROOT_REL)

    if args.update_baseline:
        index = build_target_index(repo_root)
        findings = scan(repo_root, index)
        n = write_baseline(repo_root, findings)
        print(f"[verify-provenance-stamps] baseline regenerated: {n} grandfathered "
              f"failures -> {baseline_path(repo_root).relative_to(repo_root)}", file=sys.stderr)
        return 0

    gating, grandfathered = run(repo_root)
    report(gating, grandfathered, repo_root)

    print(
        f"\n[verify-provenance-stamps] tokens: {', '.join(STAMP_TOKENS)}\n"
        f"[verify-provenance-stamps] gating failures: {len(gating)}  "
        f"grandfathered (legacy baseline): {len(grandfathered)}",
        file=sys.stderr,
    )
    if gating:
        print(
            "[verify-provenance-stamps] A provenance stamp must carry an artifact "
            "reference on the same line: an in-tree file path, path:line, or "
            "path::symbol. Add the reference, or (for a legacy line) run "
            "`make refresh-provenance-baseline`. See the README "
            "'Provenance-stamp grammar' section.",
            file=sys.stderr,
        )
    return 1 if gating else 0


if __name__ == "__main__":
    raise SystemExit(main())
