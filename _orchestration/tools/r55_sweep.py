#!/usr/bin/env python3
"""R55 Phase-2 wording-sweep inventory and classifier.

Enumerates every hit of the sweep regex in manuscript/, src/ and README.md at a
revision, sorts each hit into one context class, and writes the per-line record
to r55_sweep_inventory.tsv beside this file. It edits nothing: the edits are
hand-applied, same-line, one commit per class.

    python3 _orchestration/tools/r55_sweep.py --base <BASE> --tip HEAD --write
    python3 _orchestration/tools/r55_sweep.py --base <BASE> --tip HEAD --check

--check re-runs the measurement on the tip and fails unless every tip hit is a
line the TSV records as a residual, or an edited line whose remaining hit is an
identifier. A second, independent method (a Python regex walk of the tracked
files) must return the same hit set as git grep, or the run fails.
"""
from __future__ import annotations

import argparse
import collections
import importlib.util
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "r55_sweep_inventory.tsv")

SCOPE = ["manuscript/", "src/", "README.md"]
HIT = r"axiom[ ~_-]?5|five axioms|[^0-9]5 axioms|fifth axiom|axiom count|ratified-axiom"
HIT_RE = re.compile(HIT, re.I)

# The item's own measurement, kept beside the wider inventory regex.
ITEM_RE = re.compile(r"axiom.{0,1}5", re.I)

# Built at runtime: the literal header on one line, or wrapped, would make the
# R40 quote checker count this script as a note-bearing file.
NOTE_B2A = re.compile("R40 batch" + "-2a (—|---) NEEDS" + "-RE-DERIVATION status note")
NOTE_B1 = re.compile(
    r"Dated demotion note (—|---) 2026-08-11 \(R40 demotion sweep, batch"
    r"|DATED DEMOTION NOTE — 2026-08-11 \(R40 demotion sweep, batch",
)
NOTE_B1_DETAIL = re.compile("R40 batch" + "-1 demotion note --- per-line detail")
NOTE_B1_END = re.compile(r"\\textbf\{Records\.\}|\*\*Records\.\*\*")

IDENTIFIERS = re.compile(
    r"eq[\\]?_axiom[\\]?_5(\.tex)?"
    r"|eq:axiom5_\w+"
    r"|`axiom-5`|axiom-5\b(?=[\s:*,'\"\]\)]|$)"
    r"|r55-axiom5-source-law"
    r"|test_axiom5_\w+"
    r"|axiom5_\w*"
    r"|expected-independent-axiom-count"
    r"|axiom-count"
)

PHASE_1 = {
    "manuscript/common_equations/eq_axiom_5.tex",
    "manuscript/common_equations/eq_axiom_3.tex",
    "manuscript/ave-kb/common/axiom-register.md",
    "manuscript/ave-kb/tools/kb_index_lib.py",
    "manuscript/ave-kb/tools/tests/test_kb_index_lib.py",
}

# Lines whose subject is the token itself. The R55 alias and both homonym guards
# rely on the old name appearing here.
TOKEN_AS_SUBJECT = {
    "manuscript/ave-kb/CLAUDE.md": {68, 359, 360, 379, 380, 381, 382, 383, 384, 385, 386, 387},
    "manuscript/ave-kb/common/axiom-register.md": {306, 533, 534, 535, 536, 537, 538, 539, 540, 541},
}

HOMONYMS = {
    "src/ave/solvers/coupled_resonator.py": {656, 689},
    "src/ave/condensed/silicon_crystal.py": {154},
    "src/ave/condensed/silicon_doping.py": {18},
    # Osterwalder-Schrader OS1--OS5, named at :57.
    "manuscript/vol_2_subatomic/chapters/12_appendix_formal_proofs.tex": {64},
}

BARRED_1068 = {
    "src/ave/topological/cosserat_field_3d.py",
    "src/ave/topological/vacuum_engine.py",
    "src/ave/topological/k4_quaternion.py",
    "src/ave/topological/k4_cosserat_coupling.py",
}

# Sites that restate a note outside its header. Residuals, not edits.
NOTE_RESTATEMENT = {"src/ave/solvers/harmonic_balance_srs.py": {1115, 1119}}

# Grade-bearing: the line states the count or the container's grade.
GRADE_BEARING = {
    "manuscript/frontmatter/00_foreword.tex": {1, 59, 61},
    "manuscript/ave-kb/common/form-deriving-value-importing.md": {63},
}

# Label-only sites that also say the source law supplies the Gauss constraint.
GAUSS_PIN = {
    "manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md": {34},
    "manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g20f-vacuum-polarization.md": {132, 136},
    "manuscript/backmatter/02_full_derivation_chain.tex": {153},
    "manuscript/backmatter/12_mathematical_closure.tex": {79},
    "manuscript/vol_2_subatomic/chapters/05_electroweak_gauge_theory.tex": {35},
    "manuscript/ave-kb/session/axiom-homologation.md": {847, 848},
}

PURE_REFERENCE = {
    "manuscript/ave-kb/CLAUDE.md": {389},
    "manuscript/ave-kb/common/interlock-register.md": {383, 464, 465},
    "manuscript/ave-kb/common/relational-cancellation-identity.md": {153},
    "manuscript/ave-kb/common/translation-tables/translation-diagrammatics.md": {99, 113},
    "manuscript/ave-kb/common/vocabulary-register.md": {500},
}

# Same sense as the sweep regex, but not the source law: a pre-R44 negation, or a
# count statement that holds at four.
OTHER_SENSE = {
    "README.md": {72},
    "manuscript/common_equations/eq_axiom_4.tex": {50},
    "manuscript/ave-kb/common/index.md": {77},
    "manuscript/ave-kb/common/historical-precedents.md": {43},
    "manuscript/ave-kb/vol2/claim-quality.md": {1244},
    "manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/mass-closure-theorem.md": {10},
    "manuscript/ave-kb/vol3/claim-quality.md": {80, 94},
}

EDIT_CLASSES = ("GRADE-BEARING", "GAUSS-PIN", "PURE-REFERENCE")

REASONS = {
    "GENERATED": "generated index; its source line is a fifth-axiom negation",
    "R40-NOTE": "dated R40 note, left as it stands; read through the R55 alias",
    "BARRED-1068": "engine file fenced while #1068 is open",
    "HOMONYM-EXCLUDED": "a different object from the source law",
    "PHASE-1": "R55 Phase-1 site, not long tail",
    "TOKEN-AS-SUBJECT": "the line's subject is the old name; the alias and guards rely on it",
    "NOTE-RESTATEMENT": "restates a dated R40 note outside its header",
    "IDENTIFIER": "file name, label, node id, test name or path",
    "OTHER-SENSE": "negation or a count that holds at four; not the source law",
    "GRADE-BEARING": "states the count or grade",
    "GAUSS-PIN": "label only; the conflict with R55 rider 1 is logged",
    "PURE-REFERENCE": "names the object",
    "UNCLASSIFIED": "no class fits: stuck-point",
}


def git(*args):
    return subprocess.run(["git", "-C", REPO, *args], capture_output=True, text=True, check=True).stdout


def file_lines(rev, path, cache={}):
    key = (rev, path)
    if key not in cache:
        cache[key] = git("show", f"{rev}:{path}").split("\n")
    return cache[key]


def hits_git_grep(rev):
    out = subprocess.run(
        ["git", "-C", REPO, "grep", "-n", "-i", "-E", HIT, rev, "--", *SCOPE],
        capture_output=True,
        text=True,
    ).stdout
    found = set()
    for row in out.splitlines():
        _, path, line, _ = row.split(":", 3)
        found.add((path, int(line)))
    return found


def hits_python_walk(rev):
    found = set()
    for path in git("ls-tree", "-r", "--name-only", rev, "--", *SCOPE).splitlines():
        try:
            blob = subprocess.run(["git", "-C", REPO, "show", f"{rev}:{path}"], capture_output=True, check=True).stdout
            text = blob.decode("utf-8")
        except UnicodeDecodeError:
            continue
        for n, line in enumerate(text.split("\n"), 1):
            if HIT_RE.search(line):
                found.add((path, n))
    return found


def note_spans(path, lines):
    """Line spans of the dated R40 notes in a file, 1-indexed and inclusive."""
    spans = []
    for i, line in enumerate(lines, 1):
        if not (NOTE_B2A.search(line) or NOTE_B1.search(line) or NOTE_B1_DETAIL.search(line)):
            continue
        heading = re.match(r"^(#{1,6}) ", line) if path.endswith(".md") else None
        if heading:
            depth, end = len(heading.group(1)), len(lines)
            for j in range(i + 1, len(lines) + 1):
                next_heading = re.match(r"^(#{1,6}) ", lines[j - 1])
                if next_heading and len(next_heading.group(1)) <= depth:
                    end = j - 1
                    break
            spans.append((i, end))
        elif path.endswith(".md") or (path.endswith(".tex") and not line.lstrip().startswith("%")):
            end = i
            for j in range(i, len(lines) + 1):
                if NOTE_B1_END.search(lines[j - 1]):
                    end = j
                    break
            spans.append((i, end))
        else:
            mark = "%" if path.endswith(".tex") else "#"
            end = i
            while end < len(lines) and lines[end].lstrip().startswith(mark):
                end += 1
            spans.append((i, end))
    return spans


def in_map(table, path, line):
    return line in table.get(path, ())


def is_identifier_only(text):
    return not HIT_RE.search(IDENTIFIERS.sub(" ", text))


def classify(path, line, text, spans):
    in_note = any(a <= line <= b for a, b in spans)
    if path.startswith("manuscript/ave-kb/.index/"):
        return "GENERATED"
    if path in BARRED_1068:
        return "BARRED-1068"
    if in_note:
        return "R40-NOTE"
    if in_map(HOMONYMS, path, line):
        return "HOMONYM-EXCLUDED"
    if in_map(TOKEN_AS_SUBJECT, path, line):
        return "TOKEN-AS-SUBJECT"
    if path in PHASE_1:
        return "PHASE-1"
    if in_map(NOTE_RESTATEMENT, path, line):
        return "NOTE-RESTATEMENT"
    for table, name in ((GRADE_BEARING, "GRADE-BEARING"), (GAUSS_PIN, "GAUSS-PIN"), (PURE_REFERENCE, "PURE-REFERENCE")):
        if in_map(table, path, line):
            return name
    if in_map(OTHER_SENSE, path, line):
        return "OTHER-SENSE"
    if is_identifier_only(text):
        return "IDENTIFIER"
    return "UNCLASSIFIED"


def load_detector():
    path = os.path.join(REPO, "research/drivers/r40_preserved_span_number_check.py")
    spec = importlib.util.spec_from_file_location("r40_span", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def preserve_flag(detector, path, lines, line, spans):
    """NONE, R40 (only the notes' own preamble declares it), or OTHER:<declaration lines>."""
    flags = detector.flags_for(path, lines, line)
    if not flags:
        return "NONE"
    other = sorted({i for _, _, _, i in flags if not any(a <= i <= b for a, b in spans)})
    return "OTHER:" + ",".join(str(i) for i in other) if other else "R40"


def rows_for(base, tip):
    method_a, method_b = hits_git_grep(base), hits_python_walk(base)
    if method_a != method_b:
        sys.exit(f"second method disagrees at {base}: {sorted(method_a ^ method_b)[:10]}")
    detector = load_detector()
    rows = []
    for path, line in sorted(method_a):
        lines = file_lines(base, path)
        text = lines[line - 1]
        spans = note_spans(path, lines)
        name = classify(path, line, text, spans)
        tip_lines = file_lines(tip, path)
        same = len(tip_lines) >= line and tip_lines[line - 1] == text
        rows.append(
            {
                "path": path,
                "line": line,
                "class": name,
                "state": "RESIDUAL" if same else "EDITED",
                "preserve": preserve_flag(detector, path, lines, line, spans),
                "reason": REASONS[name],
                "text": text,
            }
        )
    return rows


def write_tsv(rows):
    with open(TSV, "w", encoding="utf-8") as out:
        out.write("path\tline\tclass\tstate\tpreserve_flag\treason\tverbatim_at_base\n")
        for r in rows:
            text = r["text"]
            if r["class"] == "GENERATED":
                m = HIT_RE.search(text)
                text = "..." + text[max(0, m.start() - 100) : m.end() + 100] + "..."
            text = text.replace("\t", " ")
            out.write(f"{r['path']}\t{r['line']}\t{r['class']}\t{r['state']}\t{r['preserve']}\t{r['reason']}\t{text}\n")


def report(rows, base, tip):
    base_item = sum(1 for p in {r["path"] for r in rows} if any(ITEM_RE.search(x) for x in file_lines(base, p)))
    counts = collections.Counter(r["class"] for r in rows)
    edited = collections.Counter(r["class"] for r in rows if r["state"] == "EDITED")
    print(f"hit lines at base: {len(rows)} in {len({r['path'] for r in rows})} files")
    print(f"files matching the item's measurement among them: {base_item}")
    print(f"{'class':<20}{'at base':>8}{'edited':>8}{'residual':>10}")
    for name in sorted(counts):
        print(f"{name:<20}{counts[name]:>8}{edited[name]:>8}{counts[name] - edited[name]:>10}")
    flags = collections.Counter(r["preserve"].split(":")[0] for r in rows)
    print(f"preserved-span flags, all sites: {dict(flags)}")
    sites = [r for r in rows if r["class"] in EDIT_CLASSES]
    print(f"edit sites: {len(sites)} lines in {len({r['path'] for r in sites})} files")
    for r in sites:
        print(f"  {r['path']}:{r['line']} [{r['class']}] {r['state']} flag={r['preserve']}")
    print(f"tip: {tip}, base: {base}")


def check(rows, tip):
    problems = []
    if any(r["class"] == "UNCLASSIFIED" for r in rows):
        problems.append("UNCLASSIFIED rows remain")
    for r in rows:
        if r["class"] in EDIT_CLASSES and r["state"] != "EDITED":
            problems.append(f"edit site not edited: {r['path']}:{r['line']}")
        if r["class"] not in EDIT_CLASSES and r["state"] != "RESIDUAL":
            problems.append(f"out-of-class line changed: {r['path']}:{r['line']}")
    tip_a, tip_b = hits_git_grep(tip), hits_python_walk(tip)
    if tip_a != tip_b:
        problems.append(f"second method disagrees at tip: {sorted(tip_a ^ tip_b)[:10]}")
    recorded = {(r["path"], r["line"]): r for r in rows}
    for path, line in sorted(tip_a):
        row = recorded.get((path, line))
        text = file_lines(tip, path)[line - 1]
        if row is None:
            if path != "_orchestration/tools/r55_sweep.py":
                problems.append(f"new hit at tip: {path}:{line}")
        elif row["state"] == "EDITED" and not is_identifier_only(text):
            problems.append(f"edited line still carries a live token: {path}:{line}: {text[:120]}")
    print(f"tip hit lines: {len(tip_a)}; second method agrees: {tip_a == tip_b}")
    for p in problems:
        print("PROBLEM:", p)
    return not problems


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--base", required=True)
    parser.add_argument("--tip", default="HEAD")
    parser.add_argument("--write", action="store_true", help="write the TSV")
    parser.add_argument("--check", action="store_true", help="re-run on the tip and fail on any problem")
    parser.add_argument("--flag-probe", help="path:line to report detector flags for")
    args = parser.parse_args()
    if args.flag_probe:
        path, line = args.flag_probe.rsplit(":", 1)
        print(load_detector().flags_for(path, file_lines(args.base, path), int(line)))
        return 0
    rows = rows_for(args.base, args.tip)
    if args.write:
        write_tsv(rows)
    report(rows, args.base, args.tip)
    if args.check and not check(rows, args.tip):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
