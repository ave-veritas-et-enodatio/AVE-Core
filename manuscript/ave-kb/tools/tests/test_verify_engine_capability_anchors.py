"""Fail-loud contract for engine_capability_matrix.yaml text-anchors.

Guards the 2026-08-17 Audit 1 correction: doctrine cites are verbatim-text
needles, not `:NN` pins. A line pin, a missing needle, a duplicate needle,
and a too-short needle must each exit non-zero. A well-formed eight-cell
matrix exits 0.
"""
from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path

import pytest
import yaml

_TOOL = Path(__file__).resolve().parent.parent / "verify-engine-capability-anchors.py"
_DOCTRINE = "loop-gap-electron-resonator-closure-doctrine.md"
_NEEDLE_LOOP = "is **anhysteretic** — zero enclosed loop area"
_NEEDLE_HEAL = "srs transverse-only Lane A still HEAL-CONFIRMED"
_NEEDLE_ABSENT = "**Absent** in discrete srs v9/v10"


def _load():
    spec = importlib.util.spec_from_file_location(
        "verify_engine_capability_anchors", _TOOL
    )
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _doctrine_body() -> str:
    return "\n".join(
        [
            "# LOOP GAP",
            "",
            f"Canon kernel {_NEEDLE_LOOP} — so reactive storage is not mass.",
            "",
            f"| 1 | OP-2 | {_NEEDLE_HEAL}. |",
            "",
            f"| Bulk | {_NEEDLE_ABSENT} |",
            "",
        ]
    )


def _eight_cell_matrix(**overrides: str) -> dict:
    """Minimal engines×cells with the eight doctrine cites plus a PR pin."""
    loop = overrides.get("loop", f"{_DOCTRINE} :: {_NEEDLE_LOOP}")
    heal = overrides.get("a1_cage", f"{_DOCTRINE} :: {_NEEDLE_HEAL}")
    absent = overrides.get("three_channel", f"{_DOCTRINE} :: {_NEEDLE_ABSENT}")
    engines = []
    keys = [
        "master_eq",
        "crystal",
        "k4_tlm",
        "vacuum_engine",
        "cavitation",
        "srs_v9",
    ]
    for k in keys:
        cells = {
            "loop": {"status": "absent", "anchor": loop},
            "boost": {"status": "absent", "anchor": "PR#186; PR#189"},
        }
        if k == "srs_v9":
            cells["a1_cage"] = {"status": "absent", "anchor": heal}
            cells["three_channel"] = {"status": "absent", "anchor": absent}
        engines.append({"key": k, "name": k, "cells": cells})
    return {"engines": engines}


def _write_tree(root: Path, matrix: dict, doctrine: str | None = None) -> Path:
    common = root / "common"
    figures = common / "figures"
    figures.mkdir(parents=True)
    (common / _DOCTRINE).write_text(doctrine if doctrine is not None else _doctrine_body())
    yaml_path = figures / "engine_capability_matrix.yaml"
    yaml_path.write_text(yaml.safe_dump(matrix, sort_keys=False))
    return yaml_path


def test_well_formed_eight_pass() -> None:
    mod = _load()
    with tempfile.TemporaryDirectory() as td:
        yaml_path = _write_tree(Path(td), _eight_cell_matrix())
        assert mod.validate_matrix(yaml_path) == 0


def test_line_pin_fails() -> None:
    mod = _load()
    matrix = _eight_cell_matrix(loop=f"{_DOCTRINE}:18")
    with tempfile.TemporaryDirectory() as td:
        yaml_path = _write_tree(Path(td), matrix)
        with pytest.raises(SystemExit) as ei:
            mod.validate_matrix(yaml_path)
        assert ei.value.code == 1


def test_missing_needle_fails() -> None:
    mod = _load()
    matrix = _eight_cell_matrix(loop=f"{_DOCTRINE} :: this needle is absent from doctrine")
    with tempfile.TemporaryDirectory() as td:
        yaml_path = _write_tree(Path(td), matrix)
        with pytest.raises(SystemExit) as ei:
            mod.validate_matrix(yaml_path)
        assert ei.value.code == 1


def test_duplicate_needle_fails() -> None:
    mod = _load()
    dup = _doctrine_body() + "\n\n" + _NEEDLE_LOOP + "\n"
    with tempfile.TemporaryDirectory() as td:
        yaml_path = _write_tree(Path(td), _eight_cell_matrix(), doctrine=dup)
        with pytest.raises(SystemExit) as ei:
            mod.validate_matrix(yaml_path)
        assert ei.value.code == 1


def test_short_needle_fails() -> None:
    mod = _load()
    # Unique in the doctrine body after we plant it, but shorter than the floor.
    short_body = _doctrine_body() + "\n\nshorty12xx\n"
    matrix = _eight_cell_matrix(a1_cage=f"{_DOCTRINE} :: shorty12xx")
    with tempfile.TemporaryDirectory() as td:
        yaml_path = _write_tree(Path(td), matrix, doctrine=short_body)
        with pytest.raises(SystemExit) as ei:
            mod.validate_matrix(yaml_path)
        assert ei.value.code == 1


def test_starstar_not_stripped() -> None:
    """C6 receipt: dropping ** must not match **anhysteretic**."""
    mod = _load()
    matrix = _eight_cell_matrix(
        loop=f"{_DOCTRINE} :: is anhysteretic — zero enclosed loop area"
    )
    with tempfile.TemporaryDirectory() as td:
        yaml_path = _write_tree(Path(td), matrix)
        with pytest.raises(SystemExit) as ei:
            mod.validate_matrix(yaml_path)
        assert ei.value.code == 1
