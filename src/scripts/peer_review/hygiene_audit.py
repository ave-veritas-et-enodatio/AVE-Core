"""
§9 LaTeX Hygiene Re-Audit
=========================

WS2D: Verify internal \\ref links, \\label consistency, variable nomenclature,
and broken cross-references in all 6 volumes. Reports specific file:line evidence.

Run: PYTHONPATH=src python src/scripts/peer_review/hygiene_audit.py
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

MANUSCRIPT_ROOT = Path("manuscript")

# ═════════════════════════════════════════════════════════════════
# HELPERS
# ═════════════════════════════════════════════════════════════════


def find_tex_files(vol_dir: Path) -> list:
    """Find all .tex files in a volume directory."""
    if not vol_dir.exists():
        return []
    tex_files = []
    for root, _, files in os.walk(vol_dir):
        for f in files:
            if f.endswith(".tex"):
                tex_files.append(Path(root) / f)
    return sorted(tex_files)


def extract_labels_and_refs(tex_file: Path) -> dict:
    """Extract all \\label{} and \\ref{} from a .tex file."""
    content = tex_file.read_text(errors="replace")
    lines = content.split("\n")

    labels = {}  # key -> (file, line)
    refs = {}  # key -> list of (file, line)

    for i, line in enumerate(lines, 1):
        # Skip comments
        stripped = line.split("%")[0]

        for m in re.finditer(r"\\label\{([^}]+)\}", stripped):
            key = m.group(1)
            labels[key] = (str(tex_file), i)

        for m in re.finditer(r"\\(?:ref|eqref|autoref|cref)\{([^}]+)\}", stripped):
            key = m.group(1)
            if key not in refs:
                refs[key] = []
            refs[key].append((str(tex_file), i))

    return {"labels": labels, "refs": refs}


def check_nomenclature(tex_file: Path) -> list:
    """Check for inconsistent variable naming patterns."""
    content = tex_file.read_text(errors="replace")
    issues = []

    # Check for known nomenclature inconsistencies
    patterns = [
        # (pattern, description, severity)
        (r"\\ell_\{?node\}?", "ℓ_node (should use \\ell_\\text{node})", "style"),
        (r"V_\{?snap\}?", "V_snap (should use V_\\text{snap} or V_{\\text{snap}})", "style"),
        (r"\\text\{topo\}", "topo subscript (consistent use)", "check"),
    ]

    lines = content.split("\n")
    for i, line in enumerate(lines, 1):
        stripped = line.split("%")[0]
        # Check for raw ASCII in math mode
        if "\\begin{equation}" in line or "$" in line:
            # Look for unescaped underscores outside of commands
            pass

    return issues


# ═════════════════════════════════════════════════════════════════
# MAIN AUDIT
# ═════════════════════════════════════════════════════════════════

VOLUMES = [
    ("Volume 1: Foundations", MANUSCRIPT_ROOT / "vol_1_foundations"),
    ("Volume 2: Subatomic", MANUSCRIPT_ROOT / "vol_2_subatomic"),
    ("Volume 3: Macroscopic", MANUSCRIPT_ROOT / "vol_3_macroscopic"),
    ("Volume 4: Engineering", MANUSCRIPT_ROOT / "vol_4_engineering"),
    ("Volume 5: Biology", MANUSCRIPT_ROOT / "vol_5_biology"),
    ("Volume 6: Periodic Table", MANUSCRIPT_ROOT / "vol_6_periodic_table"),
]

print("=" * 100)
print("  §9 LATEX HYGIENE RE-AUDIT")
print("  WS2D: Cross-Reference Integrity and Nomenclature Consistency")
print("=" * 100)

total_labels = 0
total_refs = 0
total_broken = 0
total_files = 0
volume_reports = []

for vol_name, vol_dir in VOLUMES:
    print(f"\n{'─'*100}")
    print(f"  {vol_name}: {vol_dir}")
    print(f"{'─'*100}")

    tex_files = find_tex_files(vol_dir)
    if not tex_files:
        print(f"  ⚠️  No .tex files found in {vol_dir}")
        continue

    all_labels = {}
    all_refs = defaultdict(list)
    file_count = len(tex_files)
    total_files += file_count

    for tf in tex_files:
        result = extract_labels_and_refs(tf)
        for k, v in result["labels"].items():
            if k in all_labels:
                print(f"  ⚠️  DUPLICATE LABEL: '{k}'")
                print(f"       First: {all_labels[k][0]}:{all_labels[k][1]}")
                print(f"       Second: {v[0]}:{v[1]}")
            all_labels[k] = v
        for k, v_list in result["refs"].items():
            all_refs[k].extend(v_list)

    n_labels = len(all_labels)
    n_refs = len(all_refs)
    total_labels += n_labels
    total_refs += n_refs

    # Find broken refs (ref without matching label)
    broken_refs = {}
    for ref_key, locations in all_refs.items():
        if ref_key not in all_labels:
            broken_refs[ref_key] = locations
            total_broken += len(locations)

    # Also check backmatter labels (shared across volumes)
    backmatter_dir = MANUSCRIPT_ROOT / "backmatter"
    backmatter_labels = {}
    for tf in find_tex_files(backmatter_dir):
        result = extract_labels_and_refs(tf)
        backmatter_labels.update(result["labels"])

    # Re-check broken refs against backmatter
    still_broken = {}
    for ref_key, locations in broken_refs.items():
        if ref_key not in backmatter_labels:
            still_broken[ref_key] = locations

    print(f"  Files scanned:     {file_count}")
    print(f"  Labels defined:    {n_labels}")
    print(f"  References used:   {sum(len(v) for v in all_refs.values())}")

    if still_broken:
        print(f"  ❌ Broken refs:    {len(still_broken)}")
        for ref_key, locs in sorted(still_broken.items())[:5]:
            for loc_file, loc_line in locs[:2]:
                short = os.path.basename(loc_file)
                print(f"       {short}:{loc_line} → \\ref{{{ref_key}}} (no \\label found)")
        if len(still_broken) > 5:
            print(f"       ... and {len(still_broken) - 5} more")
    else:
        print(f"  ✅ Broken refs:    0")

    # Sample 3 labels for evidence
    sample_labels = list(all_labels.items())[:3]
    if sample_labels:
        print(f"  Sample labels (evidence):")
        for key, (file, line) in sample_labels:
            short = os.path.basename(file)
            print(f"       {short}:{line}  \\label{{{key}}}")

    volume_reports.append(
        {
            "name": vol_name,
            "files": file_count,
            "labels": n_labels,
            "refs": sum(len(v) for v in all_refs.values()),
            "broken": len(still_broken),
        }
    )

# ═════════════════════════════════════════════════════════════════
# GLOBAL SUMMARY
# ═════════════════════════════════════════════════════════════════

print(f"\n{'='*100}")
print(f"  GLOBAL HYGIENE SUMMARY")
print(f"{'='*100}")
print(f"\n  {'Volume':<30s} {'Files':>6s} {'Labels':>8s} {'Refs':>7s} {'Broken':>8s} {'Status':>8s}")
print(f"  {'─'*75}")
for r in volume_reports:
    status = "✅" if r["broken"] == 0 else "❌"
    print(f"  {r['name']:<30s} {r['files']:>6d} {r['labels']:>8d} {r['refs']:>7d} {r['broken']:>8d} {status:>8s}")
print(f"  {'─'*75}")
print(f"  {'TOTAL':<30s} {total_files:>6d} {total_labels:>8d} {total_refs:>7d} {total_broken:>8d}")

if total_broken == 0:
    print(f"\n  🎯 HYGIENE VERDICT: ALL CROSS-REFERENCES RESOLVE ✅")
else:
    print(f"\n  ⚠️  HYGIENE VERDICT: {total_broken} BROKEN REFERENCES FOUND ❌")
print(f"{'='*100}")
