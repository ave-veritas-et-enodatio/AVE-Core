#!/usr/bin/env python3
"""Retire substrate-as-'condensate' prose → INVARIANT-N1 nouns (crystal / LC network / substrate).

Preserves standard CM terms (BCS/BEC/pair-condensate) and bounded engine lenses (Meissner-class).
"""

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
    ROOT / "src" / "ave",
    ROOT / "src" / "scripts" / "vol_4_engineering",
]

SKIP_PARTS = {
    "_archive",
    "research",
    "build",
    ".git",
    ".venv",
}

# If any preserve pattern matches the full line, skip substrate-condensate replacements on that line.
PRESERVE_LINE = re.compile(
    r"(?i)"
    r"(BCS\s+(?:pair[- ]?)?condensate|"
    r"Bose[- ]Einstein\s+Condensate|"
    r"pair-condensate\s+yield|"
    r"Cooper[- ]pair\s+condensate|"
    r"Meissner-class\s+condensate|"
    r"Quantum\s+Condensates|"
    r"pairs\s+condense|"
    r"CONDENSED\s+PHASE|"
    r"NOT\s+a\s+Bose|"
    r"condensate['\u2019]s\s+pair-breaking)"
)

REPLACEMENTS: list[tuple[str, str]] = [
    # Remaining M_A + condensate
    (r"\$\\mathcal\{M\}_\{A\}\$ condensate", "substrate"),
    (r"saturating \$\\mathcal\{M\}_\{A\}\$ condensate", "saturating substrate"),
    (r"saturating \\mathcal\{M\}_\{A\} condensate", "saturating substrate"),
    # Section / product titles (specific before generic)
    (r"Electromagnetic Coupling to the Chiral LC Condensate", "Electromagnetic Coupling to the Chiral LC Network"),
    (r"Helicity Injection: Polarization Matching to the Chiral LC Condensate", "Helicity Injection: Polarization Matching to the Chiral LC Network"),
    (r"Continuum Electrodynamics of the LC Condensate", "Continuum Electrodynamics of the LC Network"),
    (r"The Three Operating Regimes of the LC Condensate", "The Three Operating Regimes of the LC Network"),
    (r"The Condensate Transmission Line", "The Substrate Transmission Line"),
    (r"Condensate IMD Spectroscopy", "Substrate IMD Spectroscopy"),
    (r"Condensate Return Loss Profile", "Substrate Return Loss Profile"),
    (r"The Condensate Memristor", "The Substrate Memristor"),
    (r"Analog Condensate Power Dissipation", "Analog Substrate Power Dissipation"),
    (r"Condensate \$I-V\$ Trace", "Substrate $I-V$ Trace"),
    (r"AVE Condensate Match", "AVE Substrate Match"),
    (r"LC Condensate Vacuum", "LC Resonant Network Vacuum"),
    (r"LC condensate vacuum", "LC resonant network vacuum"),
    (r"substrate LC Condensate framework", "substrate LC Network framework"),
    (r"solid-state LC condensate \(the substrate\)", "solid-state LC network (the substrate)"),
    (r"solid-state LC condensate", "solid-state LC network"),
    (r"Chiral LC Condensate", "Chiral LC Network"),
    (r"chiral LC condensate", "chiral LC network"),
    (r"bilateral chiral LC condensate", "bilateral chiral LC network"),
    (r"substrate LC condensate", "substrate LC network"),
    (r"structured LC condensate", "structured LC network"),
    (r"surrounding LC condensate", "surrounding LC network"),
    (r"the LC condensate", "the LC network"),
    (r"of the LC condensate", "of the LC network"),
    (r"within the LC condensate", "within the LC network"),
    (r"impedance structure of the LC condensate", "impedance structure of the LC network"),
    (r"structural relaxation event of the LC condensate", "structural relaxation event of the LC network"),
    (r"transient acoustic relaxation mode` of the LC condensate", "transient acoustic relaxation mode of the LC network"),
    (r"transient acoustic relaxation mode\*\* of the LC condensate", "transient acoustic relaxation mode** of the LC network"),
    (r"transient acoustic relaxation mode of the LC condensate", "transient acoustic relaxation mode of the LC network"),
    (r"INVARIANT-S2 / Axiom 1 \(LC condensate;", "INVARIANT-S2 / Axiom 1 (LC network;"),
    (r'"LC condensate;', '"LC network;'),
    (r"solid-state condensate", "solid-state vacuum medium"),
    (r"post-genesis condensate of a phase transition", "post-genesis crystallized lattice from a phase transition"),
    (r"vacuum condensate", "vacuum medium"),
    (r"local vacuum condensate", "local vacuum medium"),
    (r"discrete vacuum condensate", "discrete vacuum network"),
    (r"discrete condensate grid", "discrete substrate grid"),
    (r"electro-mechanical condensate", "electro-mechanical substrate"),
    (r"effective condensate", "effective substrate medium"),
    (r"dense spatial condensate", "dense spatial substrate"),
    (r"spatial condensate", "spatial substrate"),
    (r"strained condensate", "strained substrate region"),
    (r"invariant optical density of the condensate", "invariant optical density of the substrate"),
    (r"yield threshold of the condensate", "yield threshold of the substrate"),
    (r"yield limit of the effective condensate", "yield limit of the effective substrate medium"),
    (r"threshold of the condensate", "threshold of the substrate"),
    (r"the AVE condensate", "the AVE substrate"),
    (r"physical condensate graph", "physical substrate graph"),
    (r"real condensate, not a computational", "real substrate lattice, not a computational"),
    (r"physical-condensate interpretation", "physical-substrate interpretation"),
    (r"torus knot condensate", "torus knot substrate"),
    (r"inside the LC condensate", "inside the LC network"),
    (r"compresses the condensate volume", "compresses the substrate volume"),
    (r"AVE Structural Condensate", "AVE Structural Substrate"),
    (r"4th-order condensate saturation limit", "4th-order substrate saturation limit"),
    (r"V_\{condensate\}", r"V_{substrate}"),
    (r"I_\{condensate\}", r"I_{substrate}"),
    (r"\\$V_\{condensate\}", r"$V_{substrate}"),
    (r"\\$I_\{condensate\}", r"$I_{substrate}"),
]

CLEANUPS: list[tuple[str, str]] = [
    (r"\bsubstrate substrate\b", "substrate"),
    (r"\bthe the substrate\b", "the substrate"),
    (r"\bLC network network\b", "LC network"),
]


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & SKIP_PARTS:
        return True
    if path.name.startswith("retire_") and path.name.endswith(".py") and path.parent.name == "scripts":
        return path.name in {"retire_substrate_condensate_noun.py", "retire_m_a_symbol.py"}
    if path.suffix not in {".md", ".tex", ".py", ".jsonl", ".yaml", ".yml"}:
        return True
    return False


def iter_files() -> list[Path]:
    out: list[Path] = []
    for root in CANONICAL_ROOTS:
        if root.is_file():
            if not should_skip(root):
                out.append(root)
            continue
        for p in root.rglob("*"):
            if p.is_file() and not should_skip(p):
                out.append(p)
    return sorted(set(out))


def apply_replacements(text: str) -> tuple[str, int]:
    changes = 0
    lines = text.splitlines(keepends=True)
    new_lines: list[str] = []
    for line in lines:
        if PRESERVE_LINE.search(line):
            new_lines.append(line)
            continue
        original = line
        for pattern, repl in REPLACEMENTS:
            line, n = re.subn(pattern, repl, line)
            changes += n
        for pattern, repl in CLEANUPS:
            line, n = re.subn(pattern, repl, line)
            changes += n
        new_lines.append(line)
    return "".join(new_lines), changes


def main() -> int:
    total_files = 0
    total_changes = 0
    for path in iter_files():
        original = path.read_text(encoding="utf-8")
        updated, n = apply_replacements(original)
        if n and updated != original:
            path.write_text(updated, encoding="utf-8")
            total_files += 1
            total_changes += n
            print(f"{path.relative_to(ROOT)}: {n}")
    print(f"\nDone: {total_files} files, {total_changes} replacements")
    return 0


if __name__ == "__main__":
    sys.exit(main())
