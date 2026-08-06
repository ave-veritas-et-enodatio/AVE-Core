"""Regression tests for ``src/scripts/signed_gamma_census.py``.

The corpus fixtures are built into ``tmp_path`` rather than committed as files
under ``manuscript/`` or ``src/tests/fixtures/``. That is deliberate: a
committed ``.tex`` fixture containing ``\\Gamma_{bulk} = -1`` would be counted
by any live census run whose universe includes its root, so the instrument
would be measuring its own test data. A synthetic corpus keeps the assertions
exact and keeps the live census clean.

Nothing here asserts a LIVE corpus count. Those numbers are documented in the
preset table and printed by ``make gamma-census``; pinning them in a test would
turn a survey into a gate, and would break on the next manuscript edit.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from dataclasses import replace
from pathlib import Path

import pytest

_MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "signed_gamma_census.py"


def _load():
    spec = importlib.util.spec_from_file_location("signed_gamma_census", _MODULE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    # Registered before exec so @dataclass can resolve cls.__module__ during
    # class creation; without this the frozen dataclasses raise AttributeError.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


census = _load()


# --------------------------------------------------------------------------
# Synthetic corpus — one line per (channel, sign, rendered) case of interest
# --------------------------------------------------------------------------

TEX_LINES = [
    r"Bulk wall: $\Gamma_{bulk} = -1$ at the cage.",  # 1  bulk / -1
    r"Font-wrapped: $\Gamma_{\mathrm{bulk}} \to -1$ here.",  # 2  bulk / -1
    r"Shear: $\Gamma_{shear} = +1$ open circuit.",  # 3  shear / +1
    r"EM port: $\Gamma_{EM} = 0$ matched.",  # 4  EM / 0
    r"Steric: $\Gamma_{pack} \to -1$ repulsion.",  # 5  other:pack / -1
    r"Bare: $\Gamma = -1$ with no channel.",  # 6  unspecified / -1
    r"% commented: $\Gamma_{bulk} = -1$ draft line.",  # 7  bulk / -1 / COMMENT
    r"Decimal: $\Gamma_{bulk} = -1.5$ not a unit reflection.",  # 8  guarded out
    r"Unicode minus: $\Gamma_{shear} = −1$ spelled U+2212.",  # 9  shear / -1
    r"No relation here, just $\Gamma_{bulk}$ mentioned.",  # 10 no sign
]

MD_LINES = [
    r"KB leaf: $\Gamma_{bulk} \to -1$ confinement.",  # 1  bulk / -1
    r"<!-- $\Gamma_{EM} = -1$ held in an HTML comment -->",  # 2  EM / -1 / COMMENT
    r"Code identifier: `Gamma_bulk = -1` in the driver.",  # 3  ASCII form
]


@pytest.fixture()
def corpus(tmp_path: Path) -> Path:
    (tmp_path / "manuscript" / "vol_1").mkdir(parents=True)
    (tmp_path / "manuscript" / "ave-kb").mkdir(parents=True)
    (tmp_path / "manuscript" / "vol_1" / "ch01.tex").write_text(
        "\n".join(TEX_LINES) + "\n", encoding="utf-8"
    )
    (tmp_path / "manuscript" / "ave-kb" / "leaf.md").write_text(
        "\n".join(MD_LINES) + "\n", encoding="utf-8"
    )
    return tmp_path


def sites_for(repo: Path, **kwargs) -> list:
    universe = replace(census.Universe(**kwargs))
    found, _ = census.scan_python(repo, universe)
    return found


# --------------------------------------------------------------------------
# Channel classification — one case per channel, including the long tail
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        (r"_{bulk} = -1", "bulk"),
        (r"_{\mathrm{bulk}} = -1", "bulk"),
        (r"_{\text{bulk}} = -1", "bulk"),
        (r"_{\rm bulk} = -1", "bulk"),
        (r"_bulk = -1", "bulk"),
        (r"_{BULK} = -1", "bulk"),
        (r"_{shear} = -1", "shear"),
        (r"_{\mathrm{shear}} = -1", "shear"),
        (r"_{EM} = -1", "EM"),
        (r"_{\mathrm{EM}} = 0", "EM"),
        (r"_{pack} \to -1", "other:pack"),
        (r"_{ij} = 0", "other:ij"),
        (r"_{\min} = -1", "other:min"),
        (r" = -1", "unspecified"),
        (r" \to -1", "unspecified"),
    ],
)
def test_channel_classification(text: str, expected: str) -> None:
    assert census.classify_channel(text) == expected


def test_channel_aliases_are_literal_only() -> None:
    """`long`/`dilatation`/`cosserat` must NOT silently fold into a channel.

    Equating them is a physics judgement about which named channel a subscript
    denotes. The enumerator reports what is written and leaves the folding to
    whoever adjudicates the vocabulary.
    """
    assert census.classify_channel(r"_{long} = -1") == "other:long"
    assert census.classify_channel(r"_{dilatation} = -1") == "other:dilatation"
    assert census.classify_channel(r"_{cosserat} = -1") == "other:cosserat"


# --------------------------------------------------------------------------
# Sign classification — one case per sign value
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        (r"_{bulk} = -1", "-1"),
        (r"_{bulk} \to -1", "-1"),
        (r"_{bulk} = −1", "-1"),  # U+2212
        (r"_{bulk} = +1", "+1"),
        (r"_{bulk} = 1", "+1"),
        (r"_{EM} = 0", "0"),
        (r"_{bulk} = -1.5", "other"),
        (r"_{bulk} = -100", "other"),
        (r"_{bulk}", "none"),
        (r"_{bulk} is discussed", "none"),
    ],
)
def test_sign_classification(text: str, expected: str) -> None:
    assert census.classify_sign(text) == expected


def test_strip_gamma_token_does_not_skip_to_a_later_prose_gamma() -> None:
    """`str.find("Gamma")` would jump past the subscript on this line."""
    line = r"Γ_{bulk} = -1 — see the Gamma appendix"
    assert census.classify_channel(census.strip_gamma_token(line)) == "bulk"


# --------------------------------------------------------------------------
# Comment vs rendered
# --------------------------------------------------------------------------


def test_comment_detection_is_first_token_only() -> None:
    assert census.is_comment_line(".tex", r"  % \Gamma_{bulk} = -1")
    assert not census.is_comment_line(".tex", r"$\Gamma=-1$  % trailing note")
    assert census.is_comment_line(".md", r"<!-- $\Gamma_{EM} = -1$ -->")
    assert not census.is_comment_line(".md", r"text <!-- $\Gamma_{EM} = -1$ -->")


def test_comment_policy_partitions_the_corpus(corpus: Path) -> None:
    common = dict(roots=("manuscript",), exts=(".tex",), gap="adjacent-nested")
    included = sites_for(corpus, comments="include", **common)
    excluded = sites_for(corpus, comments="exclude", **common)
    only = sites_for(corpus, comments="only", **common)

    assert len(included) == len(excluded) + len(only)
    assert {s.rendered for s in excluded} == {True}
    assert {s.rendered for s in only} == {False}
    assert [s.lineno for s in only] == [7]


# --------------------------------------------------------------------------
# File classification
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("manuscript/vol_1_foundations/chapters/04.tex", "print_tex"),
        ("manuscript/ave-kb/common/master-equation.md", "kb_md"),
        ("manuscript/ave-kb/tools/x.py", "kb_other"),
        ("manuscript/predictions.yaml", "manuscript_other"),
        ("research/2026-08-05_lane_prereg.md", "research"),
        ("src/ave/core/constants.py", "src"),
        ("docs/framing_and_presentation.md", "other"),
    ],
)
def test_file_classification(path: str, expected: str) -> None:
    assert census.classify_file(path) == expected


def test_file_class_split_across_tex_and_md(corpus: Path) -> None:
    found = sites_for(
        corpus, roots=("manuscript",), exts=(".tex", ".md"), gap="adjacent-nested"
    )
    classes = {s.file_class for s in found}
    assert classes == {"print_tex", "kb_md"}


# --------------------------------------------------------------------------
# The knobs that carry the quantified blind spots
# --------------------------------------------------------------------------


def test_magnitude_guard_separates_unit_from_decimal(corpus: Path) -> None:
    common = dict(roots=("manuscript",), exts=(".tex",), gap="adjacent-nested")
    guarded = sites_for(corpus, magnitude_guard=True, **common)
    naive = sites_for(corpus, magnitude_guard=False, **common)
    assert 8 not in [s.lineno for s in guarded]  # `= -1.5`
    assert 8 in [s.lineno for s in naive]


def test_ascii_only_minus_is_blind_to_u2212(corpus: Path) -> None:
    """The largest single false-negative found in the prior sweeps."""
    common = dict(roots=("manuscript",), exts=(".tex",), gap="adjacent-nested")
    unicode_lines = {s.lineno for s in sites_for(corpus, minus_forms="unicode", **common)}
    ascii_lines = {s.lineno for s in sites_for(corpus, minus_forms="ascii", **common)}
    assert 9 in unicode_lines  # `\Gamma_{shear} = −1`
    assert 9 not in ascii_lines


def test_adjacent_gap_cannot_cross_a_font_macro_brace(corpus: Path) -> None:
    """`adjacent` is narrow ON PURPOSE — it is what reproduces the audit sweep.

    Line 2 is ``\\Gamma_{\\mathrm{bulk}} \\to -1``. The narrow brace span stops
    at the inner ``}`` of ``\\mathrm{bulk}``, so the site is invisible; the
    repaired ``adjacent-nested`` sees it. Preserving both is what makes the
    under-count legible as a preset difference rather than an unexplained gap.
    """
    common = dict(roots=("manuscript",), exts=(".tex",))
    narrow = {s.lineno for s in sites_for(corpus, gap="adjacent", **common)}
    nested = {s.lineno for s in sites_for(corpus, gap="adjacent-nested", **common)}
    assert 2 not in narrow
    assert 2 in nested
    assert narrow < nested


def test_gamma_form_all_admits_bare_ascii_identifiers(corpus: Path) -> None:
    common = dict(roots=("manuscript",), exts=(".md",), gap="adjacent-nested")
    tex_only = {s.lineno for s in sites_for(corpus, gamma_form="tex", **common)}
    every = {s.lineno for s in sites_for(corpus, gamma_form="all", **common)}
    assert 3 not in tex_only  # `Gamma_bulk = -1` in a code span
    assert 3 in every


def test_channel_and_sign_filters(corpus: Path) -> None:
    common = dict(roots=("manuscript",), exts=(".tex",), gap="adjacent-nested")
    bulk_only = sites_for(corpus, channels=("bulk",), **common)
    assert {s.channel for s in bulk_only} == {"bulk"}
    minus_only = sites_for(corpus, sign_filter=("-1",), **common)
    assert {s.sign for s in minus_only} == {"-1"}


# --------------------------------------------------------------------------
# The two-method self-check — including a deliberate disagreement
# --------------------------------------------------------------------------


def _grep_available() -> bool:
    try:
        subprocess.run(["grep", "--version"], capture_output=True, check=False)
    except FileNotFoundError:
        return False
    return True


requires_grep = pytest.mark.skipif(not _grep_available(), reason="no grep on PATH")


@requires_grep
@pytest.mark.parametrize("preset", sorted(census.PRESETS))
def test_two_methods_agree_on_every_preset_over_the_fixture(corpus: Path, preset: str) -> None:
    universe = census.PRESETS[preset].universe
    _, raw = census.scan_python(corpus, universe)
    result = census.cross_check(corpus, universe, raw, "grep")
    # Non-vacuity: two engines that both find nothing agree trivially, which
    # would make this assertion decoration.
    assert raw, f"{preset}: fixture produced no detections at all"
    assert result.agree, f"{preset}: only_a={result.only_a} only_b={result.only_b}"


@requires_grep
def test_self_check_actually_detects_a_two_method_disagreement(
    corpus: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A self-check that can never fail is decoration, not a check.

    This reintroduces the exact defect the live run caught: ``[^\\n]`` inside a
    POSIX bracket expression is "neither a backslash nor the letter n", so grep
    silently cannot cross ``\\mathrm{`` while Python reads it as "any char but
    newline". Both engines accept the pattern; only the results diverge. The
    self-check must catch it.
    """
    unsafe = dict(census.GAPS)
    unsafe["near"] = r"[^\n]{0,25}"
    monkeypatch.setattr(census, "GAPS", unsafe)

    universe = census.Universe(
        roots=("manuscript",), exts=(".tex",), gamma_form="tex", gap="near", relation="eqto"
    )
    _, raw = census.scan_python(corpus, universe)
    result = census.cross_check(corpus, universe, raw, "grep")

    assert not result.agree
    # Python sees the font-wrapped line; grep cannot cross the backslash.
    assert any(item.endswith("ch01.tex:2") for item in result.only_a)
    assert result.only_b == []


@requires_grep
def test_disagreement_exits_3_not_0(corpus: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    unsafe = dict(census.GAPS)
    unsafe["near"] = r"[^\n]{0,25}"
    monkeypatch.setattr(census, "GAPS", unsafe)
    code = census.main(
        [
            "--repo",
            str(corpus),
            "--roots",
            "manuscript",
            "--ext",
            ".tex",
            "--gamma-form",
            "tex",
            "--gap",
            "near",
        ]
    )
    assert code == 3


# --------------------------------------------------------------------------
# Determinism + machine-readable output
# --------------------------------------------------------------------------


def test_json_artifact_is_deterministic_and_timestamp_free(corpus: Path, tmp_path: Path) -> None:
    universe = census.Universe(roots=("manuscript",), exts=(".tex",), gap="adjacent-nested")
    first, _ = census.build_census(corpus, universe, check="off", include_sites=True)
    second, _ = census.build_census(corpus, universe, check="off", include_sites=True)
    blob_a = json.dumps(first, indent=2, sort_keys=True, ensure_ascii=False)
    blob_b = json.dumps(second, indent=2, sort_keys=True, ensure_ascii=False)
    assert blob_a == blob_b
    for banned in ("timestamp", "generated", "date", "mtime"):
        assert banned not in blob_a.lower()


def test_sites_are_sorted(corpus: Path) -> None:
    found = sites_for(
        corpus, roots=("manuscript",), exts=(".tex", ".md"), gap="adjacent-nested"
    )
    assert found == sorted(found, key=census.Site.sort_key)


def test_bucket_counts_are_consistent_with_totals(corpus: Path) -> None:
    universe = census.Universe(roots=("manuscript",), exts=(".tex", ".md"), gap="adjacent-nested")
    payload, _ = census.build_census(corpus, universe, check="off")
    for key in ("by_channel", "by_sign", "by_file_class", "by_rendered"):
        assert sum(v["sites"] for v in payload[key].values()) == payload["totals"]["sites"]


def test_preset_overrides_are_honoured() -> None:
    parser = census.build_parser()
    args = parser.parse_args(["--preset", "audit-2026-08-05", "--ext", ".tex,.md"])
    universe, name = census.universe_from_args(args)
    assert name == "audit-2026-08-05"
    assert universe.exts == (".tex", ".md")
    # untouched knobs still come from the preset
    assert universe.gap == "adjacent"
    assert universe.gamma_form == "math"


def test_every_preset_regex_is_ere_bracket_safe() -> None:
    """No ``\\n`` or ``\\t`` inside a bracket expression, in any preset.

    Both are silently mis-read by POSIX ERE and neither raises. This is a
    structural guard so the class of bug cannot be reintroduced by editing the
    knob tables.
    """
    for preset in census.PRESETS.values():
        pattern = preset.universe.detection_regex()
        for depth_slice in _bracket_spans(pattern):
            assert "\\n" not in depth_slice, (preset.name, depth_slice)
            assert "\\t" not in depth_slice, (preset.name, depth_slice)


def _bracket_spans(pattern: str) -> list[str]:
    spans, index = [], 0
    while index < len(pattern):
        if pattern[index] == "[" and (index == 0 or pattern[index - 1] != "\\"):
            close = pattern.find("]", index + 2)
            if close != -1:
                spans.append(pattern[index : close + 1])
                index = close + 1
                continue
        index += 1
    return spans


def test_module_is_not_wired_into_make_verify() -> None:
    """Gating on an unadjudicated census is the checklist-not-a-gate defect."""
    makefile = (_MODULE_PATH.parents[2] / "Makefile").read_text(encoding="utf-8")
    verify_line = next(
        line for line in makefile.splitlines() if line.startswith("verify:")
    )
    assert "gamma-census" not in verify_line
    assert "gamma-census:" in makefile  # the runner target does exist
