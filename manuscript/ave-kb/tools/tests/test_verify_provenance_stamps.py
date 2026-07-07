"""Self-test for manuscript/ave-kb/tools/verify-provenance-stamps.py.

The gate must satisfy its own discipline: a fixture doc with a VALID stamp
(path / path:line / path::symbol) passes; a BOGUS stamp (no reference, wrong
file, or wrong symbol) fails, with the can-fire proven and its precise message
recorded; a code-fence / inline stamp is ignored; and a baseline-grandfathered
stamp passes until its line content changes.

Runs against the self-contained mini-repo under
tools/tests/fixtures/provenance/ (a `research/` doc + a `src/` artifact), the
tool pointed at that root via `--root`. Pure grep + resolve — no builds.

Run directly (`python tools/tests/test_verify_provenance_stamps.py`) or via
pytest.
"""

import importlib.util
import sys
from pathlib import Path

_TOOL = Path(__file__).resolve().parent.parent / "verify-provenance-stamps.py"
_FIXTURE_ROOT = Path(__file__).resolve().parent / "fixtures" / "provenance"
_FIXTURE_DOC = _FIXTURE_ROOT / "research" / "sample_stamps.md"


def _load_module():
    spec = importlib.util.spec_from_file_location("verify_provenance_stamps", _TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _scan(vps):
    index = vps.build_target_index(_FIXTURE_ROOT)
    return vps.scan_doc(_FIXTURE_DOC, _FIXTURE_ROOT, index), index


# --------------------------------------------------------------------------
# Can-fire + precise messages (bogus stamps FAIL)
# --------------------------------------------------------------------------

def test_bogus_stamps_fire_with_precise_reasons() -> None:
    vps = _load_module()
    findings, _ = _scan(vps)

    # (a) no artifact reference at all.
    no_ref = [f for f in findings if "no artifact reference" in f.reason]
    assert no_ref, "a stamp with no artifact reference must fail"
    assert any(f.stamp == "sympy-verified" for f in no_ref)

    # (b) file named but not in-tree.
    notfound = [f for f in findings if "file not found in-tree" in f.reason]
    assert notfound, "a stamp naming a nonexistent file must fail"
    assert any("no_such_driver.py" in f.reason for f in notfound)
    assert any(f.stamp == "test-locked" for f in notfound)

    # (c) real file but the ::symbol is absent.
    nosym = [f for f in findings if "symbol" in f.reason and "not found" in f.reason]
    assert nosym, "a stamp whose ::symbol is absent must fail"
    assert any("function_that_is_absent" in f.reason for f in nosym)
    assert any(f.stamp == "engine-confirmed" for f in nosym)


# --------------------------------------------------------------------------
# Valid stamps PASS
# --------------------------------------------------------------------------

def test_valid_stamps_do_not_fire() -> None:
    vps = _load_module()
    findings, _ = _scan(vps)
    failing_reasons = {f.reason for f in findings}

    # None of the three valid-stamp lines (bare path, path::symbol, path:line)
    # may produce a finding. They all reference driver_ok.py, which exists, and
    # driver_ok.py::verify_reciprocity, whose symbol IS present.
    # Assert positively: the resolver returns None for each valid reference.
    index = vps.build_target_index(_FIXTURE_ROOT)
    for raw, ok in (
        ("(sympy-verified, `driver_ok.py`).", True),
        ("(driver-confirmed, `driver_ok.py::verify_reciprocity`).", True),
        ("(sympy-verified, `driver_ok.py:3`).", True),
        ("(engine-confirmed, `driver_ok.py::function_that_is_absent`).", False),
        ("(test-locked, `no_such_driver.py`).", False),
    ):
        refs = vps.extract_artifact_refs(raw)
        assert refs, f"expected an artifact ref in {raw!r}"
        resolved_any = any(vps.resolve_ref(r, _FIXTURE_ROOT, index) is None for r in refs)
        assert resolved_any is ok, (raw, [vps.resolve_ref(r, _FIXTURE_ROOT, index) for r in refs])

    # And the failing_reasons never include a valid-line file.
    assert not any("driver_ok.py'" in r and "not found" in r for r in failing_reasons)


# --------------------------------------------------------------------------
# Code fences / inline code are ignored (example text, not assertions)
# --------------------------------------------------------------------------

def test_code_spans_ignored() -> None:
    vps = _load_module()
    findings, _ = _scan(vps)
    # The fenced "this is sympy-verified with no artifact" line and the inline
    # `inline sympy-verified code span` must produce NO finding. If code were
    # scanned, they would add reference-less failures. Confirm no finding falls
    # on a line whose stripped body is blank (fence) or whose raw contains the
    # inline-code marker phrase.
    raw_lines = _FIXTURE_DOC.read_text(encoding="utf-8").splitlines()
    for f in findings:
        raw = raw_lines[f.line - 1]
        assert "must not be flagged" not in raw, f"fenced stamp leaked: {raw!r}"
        assert "inline sympy-verified code span" not in raw, f"inline stamp leaked: {raw!r}"


# --------------------------------------------------------------------------
# Baseline grandfathering + re-trigger on line-content change
# --------------------------------------------------------------------------

def test_baseline_grandfathers_then_re_triggers_on_edit() -> None:
    vps = _load_module()
    findings, _ = _scan(vps)

    # Pick a real bogus finding (the reference-less sympy-verified line).
    victim = next(f for f in findings if "no artifact reference" in f.reason)

    # A baseline containing its key grandfathers it: gating drops it, the
    # grandfathered set keeps it.
    baseline = {victim.key: "legacy"}
    gating = [f for f in findings if f.key not in baseline]
    grandfathered = [f for f in findings if f.key in baseline]
    assert victim.key not in {f.key for f in gating}
    assert victim.key in {f.key for f in grandfathered}

    # Editing the stamped line's CONTENT changes the key — enforcement resumes.
    edited_key = vps.baseline_key(
        _FIXTURE_ROOT, victim.file, victim.stamp,
        "The per-channel loading is consistent at THIRD order (sympy-verified).",
    )
    assert edited_key != victim.key, "a content edit must change the baseline key"
    assert edited_key not in baseline, "the edited stamp is no longer grandfathered"

    # A pure whitespace re-wrap (same tokens) keeps the SAME key (no spurious
    # re-trigger on reflow).
    original_raw = _FIXTURE_DOC.read_text(encoding="utf-8").splitlines()[victim.line - 1]
    rewrapped = "   " + "  ".join(original_raw.split()) + "  "
    rewrap_key = vps.baseline_key(_FIXTURE_ROOT, victim.file, victim.stamp, rewrapped)
    assert rewrap_key == victim.key, "whitespace-only reflow must NOT change the key"


# --------------------------------------------------------------------------
# Trivial-runtime / stdlib-only sanity (the gate must satisfy its own runtime
# discipline: pure grep + resolve, no builds).
# --------------------------------------------------------------------------

def test_pure_stdlib_no_third_party_imports() -> None:
    src = _TOOL.read_text(encoding="utf-8")
    # No numpy / sympy / ave engine imports — the gate is grep + path-resolve.
    for banned in ("import numpy", "import sympy", "from ave", "import ave", "import scipy"):
        assert banned not in src, f"gate must not import {banned!r}"


if __name__ == "__main__":
    vps = _load_module()
    findings, _ = _scan(vps)
    print(f"fixture findings: {len(findings)}")
    for f in sorted(findings, key=lambda x: x.line):
        print(f"  L{f.line}  [{f.stamp}]  {f.reason}")
    # Run the pytest functions directly.
    test_bogus_stamps_fire_with_precise_reasons()
    test_valid_stamps_do_not_fire()
    test_code_spans_ignored()
    test_baseline_grandfathers_then_re_triggers_on_edit()
    test_pure_stdlib_no_third_party_imports()
    print("ALL PASS")
