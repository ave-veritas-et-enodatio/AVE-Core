#!/usr/bin/env python3
"""Fail-loud text-anchor check for engine_capability_matrix.yaml.

WHY
---
YAML cell `anchor:` fields that cite a KB leaf as `file.md:NN` rot when a
banner is inserted above the cited line. That happened three times in the
electron-identity epic (the last: Phase C banners shifted the eight
loop-gap-doctrine pins). Line retargets fix the instance. This checker
kills the class for that doctrine file.

CONTRACT (same matching rule as `_orchestration/tools/generate_board.py`
`validate_anchor`, copied here so the KB tree does not import orchestration):

  * A doctrine cite MUST be `loop-gap-electron-resonator-closure-doctrine.md :: <needle>`
    — verbatim text, not a line number.
  * The needle occurs EXACTLY ONCE in the source after whitespace-normalization
    per paragraph (blank-line split). Floor 12 chars.
  * Matching does NOT strip markdown (`**`, `_`). That is the C6 receipt:
    `normalize()` in verify-anchor-content.py collapses whitespace only, so an
    excerpt that drops `**` is not a substring of `**anhysteretic**`.
  * Any remaining `loop-gap-electron-resonator-closure-doctrine.md:NN` line pin
    is a hard fail.
  * Other anchor forms (Python `file:line`, `PR#N`, parentheticals) are
    unchanged by this checker.

Usage:
    python3 manuscript/ave-kb/tools/verify-engine-capability-anchors.py
    python3 manuscript/ave-kb/tools/verify-engine-capability-anchors.py --yaml PATH
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DEFAULT_YAML = HERE.parent / "common" / "figures" / "engine_capability_matrix.yaml"
DOCTRINE = "loop-gap-electron-resonator-closure-doctrine.md"
TEXT_SEP = " :: "
MIN_NEEDLE = 12
LINE_PIN_RE = re.compile(
    rf"(?:^|[;\s]){re.escape(DOCTRINE)}:(\d+)(?:-\d+)?(?:$|[;\s,])"
)


def die(msg: str, code: int = 1) -> None:
    print(f"verify-engine-capability-anchors: {msg}", file=sys.stderr)
    raise SystemExit(code)


def normalize(text: str) -> str:
    return " ".join(text.split())


def hit_count(body: str, needle: str) -> int:
    """Exact-once matching, per paragraph. Same limits as generate_board.py:

    A needle may wrap plain lines inside one block. It may not span a blank
    line. `> ` / `- ` prefixes are NOT stripped.
    """
    blocks = [normalize(b) for b in re.split(r"\n\s*\n", body)]
    n = normalize(needle)
    return sum(b.count(n) for b in blocks)


def resolve_source(yaml_path: Path, source: str) -> Path:
    name = Path(source).name
    candidates = [
        yaml_path.parent / source,
        yaml_path.parent.parent / name,
        yaml_path.parent.parent / source,
    ]
    for c in candidates:
        if c.is_file():
            return c.resolve()
    die(f"source {source!r} not found relative to {yaml_path}")


def validate_text_anchor(who: str, yaml_path: Path, source: str, needle: str) -> None:
    n = normalize(needle)
    if len(n) < MIN_NEEDLE:
        die(
            f"{who}: needle {needle!r} normalizes to {n!r} "
            f"({len(n)} chars) — too short (min {MIN_NEEDLE}). Quote more of the line."
        )
    src = resolve_source(yaml_path, source)
    body = src.read_text(encoding="utf-8", errors="replace")
    hits = hit_count(body, needle)
    rel = src.name
    if hits == 0:
        die(
            f"{who}: needle not found in {rel}.\n"
            f"         needle: {needle!r}\n"
            f"         Repoint the text; do NOT convert it back to a line number."
        )
    if hits > 1:
        die(
            f"{who}: needle occurs {hits} times in {rel} — lengthen it.\n"
            f"         needle: {needle!r}"
        )


def iter_cell_anchors(data: dict):
    for eng in data.get("engines", []):
        eng_key = eng.get("key") or eng.get("name") or "?"
        for dof, cell in (eng.get("cells") or {}).items():
            if not isinstance(cell, dict):
                continue
            anchor = cell.get("anchor")
            if not isinstance(anchor, str) or not anchor.strip():
                continue
            yield f"{eng_key}.{dof}", anchor


def validate_matrix(yaml_path: Path) -> int:
    if not yaml_path.is_file():
        die(f"yaml not found: {yaml_path}")
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        die(f"{yaml_path}: not a mapping")

    n_text = 0
    for who, anchor in iter_cell_anchors(data):
        if LINE_PIN_RE.search(anchor):
            die(
                f"{who}: {DOCTRINE} is cited as a line pin ({anchor!r}). "
                f"Use `{DOCTRINE}{TEXT_SEP}<verbatim needle>`."
            )
        if TEXT_SEP not in anchor:
            continue
        source, needle = anchor.split(TEXT_SEP, 1)
        source, needle = source.strip(), needle.strip()
        if not source.endswith(".md"):
            die(f"{who}: text-anchor source {source!r} is not a .md file")
        if Path(source).name != DOCTRINE and DOCTRINE not in source:
            # Text-anchor form is legal for any .md; still validate exact-once.
            pass
        validate_text_anchor(who, yaml_path, source, needle)
        n_text += 1

    if n_text < 8:
        die(
            f"expected at least 8 {DOCTRINE} text-anchors "
            f"(six loop: cells + srs_v9.a1_cage + srs_v9.three_channel); found {n_text}."
        )
    print(f"verify-engine-capability-anchors: OK ({n_text} text-anchors)")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("WHY", 1)[0])
    p.add_argument(
        "--yaml",
        type=Path,
        default=DEFAULT_YAML,
        help="path to engine_capability_matrix.yaml",
    )
    args = p.parse_args(argv)
    return validate_matrix(args.yaml)


if __name__ == "__main__":
    sys.exit(main())
