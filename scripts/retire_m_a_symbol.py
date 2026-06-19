#!/usr/bin/env python3
"""Retire $\\mathcal{M}_A$ substrate object symbol → prose-only substrate nouns."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CANONICAL_ROOTS = [
    ROOT / "manuscript",
    ROOT / "docs",
    ROOT / "LIVING_REFERENCE.md",
    ROOT / "_orchestration",
]

SKIP_PARTS = {
    "_archive",
    "research",
    "build",
    ".git",
    ".venv",
}

# Most specific first.
REPLACEMENTS: list[tuple[str, str]] = [
    (r"\\Omega\s*\\subset\s*\\mathcal\{M\}_A", r"a localized region $\\Omega$ in the substrate"),
    (r"\\int_\{\\mathcal\{M\}_A\}", r"\\int"),
    (r"discrete amorphous LC resonant condensate \(\$\\mathcal\{M\}_A\$\)", "discrete chiral LC resonant network"),
    (r"amorphous LC resonant condensate \(\$\\mathcal\{M\}_A\$\)", "chiral LC resonant network"),
    (r"The Vacuum as an LC Resonant Condensate \(\$\\mathcal\{M\}_A\$\)", "The Vacuum as an LC Resonant Network"),
    (r"LC Resonant Condensate \(\$\\mathcal\{M\}_A\$\)", "LC resonant network"),
    (r"Electromagnetic LC Resonant Network \(\$\\mathcal\{M\}_A\$\)", "electromagnetic LC resonant network"),
    (r"Trace-Reversed Chiral LC Network \(\$\\mathcal\{M\}_A\$\)", "Trace-Reversed Chiral LC Network"),
    (r"chiral Laves K4 Cosserat crystal \$\\mathcal\{M\}_A\$", "chiral Laves K4 Cosserat crystal"),
    (r"chiral Laves K4 Cosserat crystal \\$\\mathcal\{M\}_A\\$", "chiral Laves K4 Cosserat crystal"),
    (r"discrete topological \$\\mathcal\{M\}_A\$ lattice", "discrete topological substrate lattice"),
    (r"structural limit of the \$\\mathcal\{M\}_A\$ lattice", "structural limit of the substrate lattice"),
    (r"the \$\\mathcal\{M\}_A\$ lattice", "the substrate lattice"),
    (r"The \$\\mathcal\{M\}_A\$ lattice", "The substrate lattice"),
    (r"\$\\mathcal\{M\}_A\$ lattice", "substrate lattice"),
    (r"the \$\\mathcal\{M\}_A\$ LC network", "the substrate LC network"),
    (r"The \$\\mathcal\{M\}_A\$ LC network", "The substrate LC network"),
    (r"\$\\mathcal\{M\}_A\$ LC network", "substrate LC network"),
    (r"\$\\mathcal\{M\}_A\$ LC Network", "substrate LC network"),
    (r"\$\\mathcal\{M\}_A\$ condensate", "substrate"),
    (r"\$\\mathcal\{M\}_A\$ elastodynamic fluid", "substrate elastodynamic medium"),
    (r"\$\\mathcal\{M\}_A\$ manifold", "substrate"),
    (r"\$\\mathcal\{M\}_A\$ fluid", "substrate medium"),
    (r"\$\\mathcal\{M\}_A\$ graph", "substrate graph"),
    (r"\$\\mathcal\{M\}_A\$ LC", "substrate LC"),
    (r"of the \$\\mathcal\{M\}_A\$", "of the substrate"),
    (r"in the \$\\mathcal\{M\}_A\$", "in the substrate"),
    (r"in \$\\mathcal\{M\}_A\$", "in the substrate"),
    (r"on the \$\\mathcal\{M\}_A\$", "on the substrate"),
    (r"on \$\\mathcal\{M\}_A\$", "on the substrate"),
    (r"through \$\\mathcal\{M\}_A\$", "through the substrate"),
    (r"through the \$\\mathcal\{M\}_A\$", "through the substrate"),
    (r"surrounding \$\\mathcal\{M\}_A\$", "surrounding substrate"),
    (r"bulk \$\\mathcal\{M\}_A\$", "bulk substrate"),
    (r"continuous \$\\mathcal\{M\}_A\$", "continuous substrate"),
    (r"localized \$\\mathcal\{M\}_A\$", "localized substrate"),
    (r"nonlinear \$\\mathcal\{M\}_A\$", "nonlinear substrate"),
    (r"the \$\\mathcal\{M\}_A\$ substrate", "the substrate"),
    (r"\$\\mathcal\{M\}_A\$ substrate", "substrate"),
    (r"the \$\\mathcal\{M\}_A\$ vacuum", "the vacuum substrate"),
    (r"\$\\mathcal\{M\}_A\$ vacuum", "vacuum substrate"),
    (r"\$\\mathcal\{M\}_A\$/", "substrate/"),
    (r"\$\\mathcal\{M\}_A\$", "the substrate"),
    # bare (no math delimiters) fallbacks for markdown
    (r"\\mathcal\{M\}_A lattice", "substrate lattice"),
    (r"\\mathcal\{M\}_A LC network", "substrate LC network"),
    (r"\\mathcal\{M\}_A graph", "substrate graph"),
    (r"\\mathcal\{M\}_A", "the substrate"),
]

AMORPHOUS_REPLACEMENTS: list[tuple[str, str]] = [
    (r"discrete amorphous LC resonant condensate", "discrete chiral LC resonant network"),
    (r"amorphous LC resonant condensate", "chiral LC resonant network"),
    (r"Amorphous Condensate", "Chiral LC Network"),
    (r"amorphous condensate", "chiral LC network"),
    (r"Amorphous condensate", "Chiral LC network"),
]

CLEANUPS: list[tuple[str, str]] = [
    (r"\bthe the substrate\b", "the substrate"),
    (r"\bThe the substrate\b", "The substrate"),
    (r"\bsubstrate substrate\b", "substrate"),
    (r"\bthe substrate substrate\b", "the substrate"),
    (r"\bthe substrate lattice lattice\b", "the substrate lattice"),
    (r"\bthe substrate LC network network\b", "the substrate LC network"),
    (r"\bthe substrate medium medium\b", "the substrate medium"),
]


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & SKIP_PARTS:
        return True
    if path.suffix not in {".tex", ".md", ".py"} and path.name != "LIVING_REFERENCE.md":
        return False
    return False


def iter_files() -> list[Path]:
    out: list[Path] = []
    for root in CANONICAL_ROOTS:
        if root.is_file():
            if not should_skip(root):
                out.append(root)
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if should_skip(path):
                continue
            if path.suffix not in {".tex", ".md"}:
                continue
            out.append(path)
    return sorted(set(out))


def transform(text: str) -> tuple[str, int]:
    n = 0
    for pat, repl in REPLACEMENTS:
        text, c = re.subn(pat, repl, text)
        n += c
    for pat, repl in AMORPHOUS_REPLACEMENTS:
        text, c = re.subn(pat, repl, text)
        n += c
    for pat, repl in CLEANUPS:
        text, c = re.subn(pat, repl, text)
        n += c
    return text, n


def main() -> int:
    total_files = 0
    total_repls = 0
    remaining: list[str] = []

    for path in iter_files():
        original = path.read_text(encoding="utf-8")
        if "\\mathcal{M}_A" not in original and "amorphous condensate" not in original.lower():
            continue
        updated, count = transform(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            total_files += 1
            total_repls += count
        if "\\mathcal{M}_A" in updated:
            remaining.append(str(path.relative_to(ROOT)))

    print(f"Updated {total_files} files ({total_repls} pattern applications)")
    if remaining:
        print(f"WARNING: {len(remaining)} files still contain \\mathcal{{M}}_A:")
        for p in remaining[:30]:
            print(f"  {p}")
        if len(remaining) > 30:
            print(f"  ... and {len(remaining) - 30} more")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
