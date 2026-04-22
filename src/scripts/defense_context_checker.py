#!/usr/bin/env python3
"""
Defense-Context Checker — scans the AVE corpus for known "uncontextualized AI
reviewer" anti-patterns. Each rule corresponds to a named section in
docs/framing_and_presentation.md.

The anti-patterns are framings that a skeptical physicist (or LLM reviewer)
will misread in predictable ways. Example: an unqualified "α is the input
parameter" sentence reads as "AVE still has a free parameter" unless the
Golden-Torus derivation is cross-referenced within a few sentences. The
checker detects the anti-pattern PRESENCE and, if the corresponding inline
mitigator is absent within a context window, emits a warning pointing at
the right framing-doc section.

v1 is warning-only — wired into `make verify` with `|| true` so findings do
not fail the build. Findings should drive manuscript edits, not block CI.

Usage:
    python src/scripts/defense_context_checker.py                # human-readable
    python src/scripts/defense_context_checker.py --severity warn  # filter
    python src/scripts/defense_context_checker.py --json           # machine-readable
    python src/scripts/defense_context_checker.py --files a.tex b.md  # specific files

Exit codes:
    0 — scan complete (always, in warning-only mode)
    1 — scan error (I/O, regex compile failure)

Reference: docs/framing_and_presentation.md, .agents/workflows/audit-math.md,
           .agents/workflows/audit-latex.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ───────────────────────────────────────────────────────────────────────────
# Rule definitions
# ───────────────────────────────────────────────────────────────────────────
@dataclass
class Rule:
    """
    A single anti-pattern check.

    Matching is greedy over each source file: every occurrence of `pattern`
    is a candidate finding. A candidate is SUPPRESSED if `mitigator` matches
    within `context_chars` (symmetric window around the match).

    Rules with `mitigator=None` always fire (known-stale values etc.).
    """

    id: str
    pattern: str
    mitigator: Optional[str] = None
    severity: str = "warn"  # "critical" | "warn" | "info"
    message: str = ""
    fix: str = ""
    see: str = ""
    context_chars: int = 600
    # File-type scope: if non-empty, rule only applies to files whose suffix
    # is in this set (e.g. {".tex"} for LaTeX-only rules).
    extensions: frozenset[str] = field(default_factory=frozenset)


RULES: list[Rule] = [
    # ─── CRITICAL: known-stale arithmetic ──────────────────────────────────
    Rule(
        id="CRIT-1",
        pattern=r"139\s*/\s*450|\\frac\{139\}\{450\}",
        mitigator=None,
        severity="critical",
        message=(
            "Stale PMNS reduction: 2/7 + 1/45 = 97/315, not 139/450. "
            "Claimed decimal 0.30794 matches 97/315; 139/450 = 0.30889."
        ),
        fix="Replace 139/450 with 97/315.",
        see="audit-math.md §1 (Known Stale Values) and docs/framing_and_presentation.md",
    ),
    # ─── B1: α as free/input parameter without derivation cross-ref ────────
    Rule(
        id="B1",
        # Sentences framing α as an input, free, fundamental, or fit parameter.
        # Must be an assertive "α IS a parameter" phrasing — proximity alone
        # is too aggressive (matches "zero free parameters" = correct framing).
        pattern=(
            # (a) α + copula + (free|input|empirical|axiomatic) parameter
            r"(?:\\alpha|α|\balpha\b)\b[^.\n]{0,40}"
            r"\b(?:is|serves\s+as|acts\s+as|treated\s+as|remains)\b[^.\n]{0,30}"
            r"\b(?:free|input|empirical|fit|axiomatic)\s+(?:parameter|input|constant|anchor)"
            # (b) VERB α as (a|an|the) (free|input|...) parameter
            r"|(?:takes|treats|treating|uses|using|accepting)\s+"
            r"(?:\\alpha|α|\balpha\b)\s+as\s+(?:a\s+|an\s+|the\s+)?"
            r"(?:free|input|empirical|fit|axiomatic)\s+(?:parameter|input|constant|anchor)"
            # (c) α is (still )?the (one|single|sole|only) (empirical|free) ANCHOR
            r"|(?:\\alpha|α|\balpha\b)\s+is\s+(?:still\s+)?the\s+"
            r"(?:one|single|sole|only)\s+(?:empirical|free)"
            # (d) α is CODATA-sourced / taken from CODATA
            r"|(?:\\alpha|α|\balpha\b)[^.\n]{0,40}"
            r"\b(?:is\s+CODATA[-\s]sourced|taken\s+from\s+CODATA)"
        ),
        # Mitigators: Ch 8 label, Golden Torus prose, derivation language.
        mitigator=(
            r"ch:alpha_golden_torus|Golden\s+Torus|4\\pi\^3\s*\+\s*\\pi\^2\s*\+\s*\\pi"
            r"|137\.036304|ALPHA_COLD_INV|derived\s+from\s+first\s+principles"
            r"|S[_\^]?\{?11\}?-min(?:imum|imization)?"
        ),
        severity="warn",
        message=(
            "α described as a free/input/CODATA-sourced parameter without an "
            "inline pointer to the Golden-Torus derivation. A reviewer will "
            "conclude the framework still has one free parameter."
        ),
        fix=(
            "Cite Ch.~\\ref{ch:alpha_golden_torus} or mention the Golden "
            "Torus S_11-minimum derivation within the same paragraph."
        ),
        see="docs/framing_and_presentation.md §B1",
        context_chars=600,
    ),
    # ─── B2: Millennium proofs framed as rigorous without caveat ───────────
    Rule(
        id="B2",
        pattern=(
            # "Yang-Mills / Navier-Stokes / Strong CP" + "proof" / "solve" /
            # "exact" language that reads as a Clay-rigorous claim.
            r"(?:Yang[-\s]?Mills|Navier[-\s]?Stokes|Strong\s+CP|Riemann|Hodge"
            r"|Birch[-\s]and[-\s]Swinnerton[-\s]Dyer|Poincar[ée]|P\s+vs\.?\s+NP)"
            r"[^.\n]{0,120}"
            r"(?:proved|proof\b|solved|rigorously|Clay[-\s]rigorous|exact(?:ly)?\s+proved"
            r"|✅\s+Proofs?)"
        ),
        mitigator=(
            r"framework[-\s]conditional|framework[-\s]derived|framework[-\s]level"
            r"|engineering[-\s]physics|lattice[-\s]conditional|ideal[-\s]diode"
            r"|ch:millennium_prizes|not\s+Clay[-\s]rigorous"
            r"|caveat|Vacuum[-\s]Impedance\s+Derivations?"
        ),
        severity="warn",
        message=(
            "Millennium-problem claim framed as a proof/rigorous result without "
            "an inline engineering-physics / framework-conditional caveat. A "
            "reviewer will apply Clay standards and declare the result "
            "insufficient."
        ),
        fix=(
            'Add inline caveat: "framework-conditional lattice-level resolution; '
            'Clay-grade formalization remains future work". Or cite '
            "Ch.~\\ref{ch:millennium_prizes}."
        ),
        see="docs/framing_and_presentation.md §B2",
        context_chars=500,
    ),
    # ─── A3: non-integer coordination without amorphous framing ────────────
    Rule(
        id="A3",
        # z_0 ≈ 51.25 (or similar non-integer), OR generic "non-integer coord"
        # claim without the amorphous-is-natural context.
        pattern=(
            r"z_?0\s*[≈~]\s*51\.25"
            r"|z_?0\s*\\approx\s*51\.25"
            r"|51\.25[^.\n]{0,40}(?:coordination|coordin|neighbou?rs?)"
        ),
        mitigator=r"amorphous|glass|disordered|non[-\s]?crystalline|jamming|Phillips[-\s]Thorpe",
        severity="warn",
        message=(
            "z_0 ≈ 51.25 presented without the amorphous-lattice framing. A "
            "reviewer trained on crystalline lattices (FCC z=12, SRS z=3, etc.) "
            "will flag non-integer coordination as suspicious."
        ),
        fix=(
            'Add one-line prelude: "As the vacuum is a disordered amorphous '
            "chiral manifold (not a crystal), effective coordination numbers "
            'are generically non-integer statistical means."'
        ),
        see="docs/framing_and_presentation.md §A3",
        context_chars=500,
    ),
    # ─── A1: 0.00% prediction without identity classification ──────────────
    Rule(
        id="A1",
        # Table rows or prose claiming "0.00%" / "exact" agreement on a
        # prediction — potentially-tautological unless classified.
        pattern=(r"(?:\|\s*0\.00\s*\\?%|\|\s*Exact\s*\|" r"|0\.00\s*\\?%\s*(?:agreement|error|match))"),
        mitigator=(
            r"identity|manifestation|definitional|by\s+construction"
            r"|tautolog(?:y|ical)|not\s+a\s+fit|consistency\s+check"
            r"|Axiom\s+[0-9]\s+manifestation"
            # Classification-preamble keywords: if a table is preceded by
            # a preamble explaining the identity/manifestation/prediction
            # split, individual rows are covered by that preamble.
            r"|Classification\s+note|classification\s+tag"
            r"|mix\s+four\s+kinds\s+of\s+claim"
        ),
        severity="info",
        message=(
            "0.00% / Exact prediction row without a classification tag. A "
            "reviewer cannot distinguish definitional identity, axiom "
            "manifestation, and numerical coincidence from the ✅ column alone."
        ),
        fix=(
            "Tag the row or nearby prose as (Identity), (Axiom N Manifestation), "
            "or (Prediction) so the reader knows which kind of 0% this is. "
            "Alternatively, add a Classification preamble above the master "
            "table explaining the identity/manifestation/prediction split."
        ),
        see="docs/framing_and_presentation.md §A1",
        # Wide context window: master prediction tables can be ~5000 chars
        # end-to-end (LIVING_REFERENCE has 47 rows spanning ~50 lines). A
        # classification preamble at the top of the table needs to be
        # visible from rows near the bottom.
        context_chars=5000,
    ),
    # ─── C2: anti-cheat badge overclaim ─────────────────────────────────────
    Rule(
        id="C2",
        pattern=(
            # "zero smuggled parameters" — verification-specific phrase,
            # unambiguous on its own
            r"zero\s+smuggled\s+parameters"
            # "mathematically pure" ONLY when co-occurring with verification
            # context. The phrase is used in non-verification senses too
            # (geometric symmetry, idealized substrate); firing on the raw
            # phrase caused 4 false positives in the R-3 triage.
            r"|\b(?:verify_universe|anti[-\s]cheat|scan|verified|verification)[^\n]{0,200}mathematically\s+pure"
            r"|mathematically\s+pure[^\n]{0,200}\b(?:verify_universe|anti[-\s]cheat|scan|verified|verification)\b"
            # "PURE" badge in verification context (e.g. "373/373 PURE")
            r"|\bPURE\b(?:\s+anti[-\s]cheat|\s+verified|\s+\d+\s*/\s*\d+)"
        ),
        mitigator=(
            r"(?:SI|CODATA).{0,60}(?:import|literal)"
            r"|narrow\s+scope|specific\s+scope|scoped\s+to|scope[:\s]"
            r"|AST\s+scan|syntactic|not\s+semantic"
        ),
        severity="info",
        message=(
            "verify_universe.py claim framed as if it verifies the full "
            '"no smuggled data" rule, but the scan is a narrow AST-level '
            "check for banned imports and a handful of literal magic numbers."
        ),
        fix=(
            'Add inline scope: "the scan prohibits scipy.constants imports '
            "and specific CODATA-value literals; it does not AST-walk data "
            'arrays or fit-target arguments."'
        ),
        see="docs/framing_and_presentation.md §C2",
        context_chars=400,
    ),
]


# ───────────────────────────────────────────────────────────────────────────
# Scanner
# ───────────────────────────────────────────────────────────────────────────
@dataclass
class Finding:
    rule_id: str
    severity: str
    path: str
    line: int
    matched_text: str
    message: str
    fix: str
    see: str


def line_of_offset(text: str, offset: int) -> int:
    """Return the 1-based line number containing `offset`."""
    return text.count("\n", 0, offset) + 1


def scan_file(path: Path, rules: list[Rule]) -> list[Finding]:
    try:
        source = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        print(f"[defense-checker] ERROR reading {path}: {e}", file=sys.stderr)
        return []

    findings: list[Finding] = []
    suffix = path.suffix.lower()

    for rule in rules:
        if rule.extensions and suffix not in rule.extensions:
            continue

        pat = re.compile(rule.pattern, re.IGNORECASE | re.MULTILINE)
        mit = re.compile(rule.mitigator, re.IGNORECASE | re.MULTILINE) if rule.mitigator is not None else None

        for m in pat.finditer(source):
            start, end = m.span()
            matched = m.group(0).strip()

            if mit is not None:
                # Suppress finding if a mitigator appears within the symmetric
                # context window.
                window_start = max(0, start - rule.context_chars)
                window_end = min(len(source), end + rule.context_chars)
                window = source[window_start:window_end]
                if mit.search(window):
                    continue

            findings.append(
                Finding(
                    rule_id=rule.id,
                    severity=rule.severity,
                    path=str(path),
                    line=line_of_offset(source, start),
                    matched_text=(matched if len(matched) <= 180 else matched[:177] + "…"),
                    message=rule.message,
                    fix=rule.fix,
                    see=rule.see,
                )
            )

    return findings


def discover_targets(root: Path) -> list[Path]:
    """
    Default scan surface: manuscript LaTeX + KB markdown + top-level
    public-facing docs. Excludes:
      - .agents/ (internal audit scratch that legitimately discusses
        anti-patterns; scanning it would generate noise)
      - docs/framing_and_presentation.md itself (it enumerates the rules)
      - build/ (artifacts)
      - any *.aux, *.log, *.pdf
    """
    targets: list[Path] = []

    # LaTeX sources
    for p in (root / "manuscript").rglob("*.tex"):
        if "build/" in str(p) or "/aux/" in str(p):
            continue
        targets.append(p)

    # KB markdown
    for p in (root / "manuscript" / "ave-kb").rglob("*.md"):
        if p.name == "CLAUDE.md":
            # meta-doc about cross-cutting invariants; not claim-bearing
            continue
        targets.append(p)

    # Top-level public docs
    for name in ("README.md", "LIVING_REFERENCE.md"):
        candidate = root / name
        if candidate.exists():
            targets.append(candidate)

    return sorted(set(targets))


def format_text_report(findings: list[Finding], total_files: int) -> str:
    if not findings:
        return f"[defense-checker] Scanned {total_files} files. " "No anti-patterns detected."

    # Count by severity
    by_sev: dict[str, int] = {}
    for f in findings:
        by_sev[f.severity] = by_sev.get(f.severity, 0) + 1

    order = ["critical", "warn", "info"]
    header = [f"[defense-checker] Scanned {total_files} files; " f"{len(findings)} findings."]
    for sev in order:
        if sev in by_sev:
            header.append(f"  {sev.upper():<8} {by_sev[sev]}")

    out = ["\n".join(header), ""]

    for sev in order:
        sev_findings = [f for f in findings if f.severity == sev]
        if not sev_findings:
            continue
        out.append(f"─── {sev.upper()} ({len(sev_findings)}) " + "─" * 50)
        # Group by path for readability
        by_path: dict[str, list[Finding]] = {}
        for f in sev_findings:
            by_path.setdefault(f.path, []).append(f)
        for path in sorted(by_path):
            for f in sorted(by_path[path], key=lambda x: x.line):
                out.append(f"{f.path}:{f.line}  [{f.rule_id}]")
                out.append(f"    matched: {f.matched_text}")
                out.append(f"    {f.message}")
                out.append(f"    fix: {f.fix}")
                out.append(f"    see: {f.see}")
                out.append("")

    return "\n".join(out)


def format_json_report(findings: list[Finding], total_files: int) -> str:
    return json.dumps(
        {
            "scanned_files": total_files,
            "findings": [
                {
                    "rule_id": f.rule_id,
                    "severity": f.severity,
                    "path": f.path,
                    "line": f.line,
                    "matched_text": f.matched_text,
                    "message": f.message,
                    "fix": f.fix,
                    "see": f.see,
                }
                for f in findings
            ],
        },
        indent=2,
    )


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Scan AVE corpus for defense-context anti-patterns " "(docs/framing_and_presentation.md rules).",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Repo root (default: auto-detected from script location)",
    )
    parser.add_argument(
        "--files",
        nargs="*",
        type=Path,
        help="Specific files to scan (default: manuscript/ + KB + top-level docs)",
    )
    parser.add_argument(
        "--severity",
        choices=["critical", "warn", "info", "all"],
        default="all",
        help="Filter output to this severity and above (default: all)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output machine-readable JSON instead of human-readable report",
    )
    parser.add_argument(
        "--rule",
        help="Run only the rule with this ID (useful for testing)",
    )
    args = parser.parse_args(argv)

    # Rule filter
    rules = RULES
    if args.rule:
        rules = [r for r in RULES if r.id == args.rule]
        if not rules:
            print(f"[defense-checker] Unknown rule id: {args.rule}", file=sys.stderr)
            return 1

    # Target files
    if args.files:
        targets = [p for p in args.files if p.exists()]
    else:
        targets = discover_targets(args.root)

    # Scan
    all_findings: list[Finding] = []
    for path in targets:
        all_findings.extend(scan_file(path, rules))

    # Severity filter
    if args.severity != "all":
        sev_order = {"critical": 0, "warn": 1, "info": 2}
        cutoff = sev_order[args.severity]
        all_findings = [f for f in all_findings if sev_order[f.severity] <= cutoff]

    # Output
    if args.json:
        print(format_json_report(all_findings, len(targets)))
    else:
        print(format_text_report(all_findings, len(targets)))

    # Warning-only: always exit 0 in human mode so make verify doesn't fail.
    # (JSON callers can inspect the count themselves.)
    return 0


if __name__ == "__main__":
    sys.exit(main())
