"""Self-test for manuscript/ave-kb/tools/verify-frozen-provenance.py.

The gate must catch the two motivating incidents and not fire on their
controls. Four self-contained mini-repos under
tools/tests/fixtures/frozen-provenance/ (each a `research/` dir with a
result doc + prereg), the tool pointed at each via `--root`:

  * case_770_fabricated — a Frozen-labeled fabricated robustness string absent
    from the prereg (the PR#770 class) -> gating FAIL.
  * case_782_swapped   — a Frozen-labeled ABSOLUTE Lamé criterion swapped for
    the prereg's relative one (the PR#782 class) -> gating FAIL, NOT fooled by
    the different-but-present frozen criterion.
  * case_pass          — every Frozen criterion byte-present in the prereg ->
    ZERO gating findings (the negative control).
  * case_no_prereg     — a Frozen label with no resolvable prereg -> gating FAIL
    (the missing-pointer rule).

All fixtures are dated 2026-07-30 (>= the default gating cutoff) so the gate
fires with teeth. Pure text scan + substring resolve — no builds.

Run directly (`python tools/tests/test_verify_frozen_provenance.py`) or via
pytest.
"""

import importlib.util
import sys
from pathlib import Path

_TOOL = Path(__file__).resolve().parent.parent / "verify-frozen-provenance.py"
_FIXTURES = Path(__file__).resolve().parent / "fixtures" / "frozen-provenance"


def _load_module():
    spec = importlib.util.spec_from_file_location("verify_frozen_provenance", _TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _run(case: str):
    """(gating, warn, incidents) for a fixture case root."""
    vfp = _load_module()
    return vfp.run(_FIXTURES / case)


# --------------------------------------------------------------------------
# The two motivating incidents FIRE (with teeth) on their reconstructed patterns
# --------------------------------------------------------------------------

def test_pr770_fabricated_string_is_caught() -> None:
    gating, _warn, _inc = _run("case_770_fabricated")
    assert gating, "the PR#770 fabricated frozen string must produce a gating FAIL"
    f = gating[0]
    assert f.kind == "mismatch"
    assert "ROBUST across rail depth" in f.detail
    assert "NOT byte-present" in f.detail


def test_pr782_swapped_criterion_is_caught() -> None:
    gating, _warn, _inc = _run("case_782_swapped")
    # The swapped absolute criterion FAILS; it must NOT be excused by the
    # DIFFERENT relative criterion that IS present (reconcile against prereg,
    # not a self-declared echo).
    mism = [f for f in gating if f.kind == "mismatch"]
    assert mism, "the PR#782 swapped Lamé criterion must produce a gating FAIL"
    assert any("ext1" in f.detail for f in mism)


def test_no_prereg_hard_fails() -> None:
    gating, _warn, _inc = _run("case_no_prereg")
    assert any(f.kind == "no-prereg" for f in gating), (
        "a gating doc with Frozen labels but no resolvable prereg must hard-fail"
    )


# --------------------------------------------------------------------------
# The negative control does NOT fire (not a false-positive machine)
# --------------------------------------------------------------------------

def test_pass_control_is_clean() -> None:
    gating, warn, _inc = _run("case_pass")
    assert not gating, f"byte-identical frozen criteria must not gate: {gating}"
    assert not warn, f"byte-identical frozen criteria must not warn: {warn}"


# --------------------------------------------------------------------------
# Label grammar: a quoted MENTION of "Frozen:" is not a label (the disclosure
# lines in the corrected docs must not trip the gate).
# --------------------------------------------------------------------------

def test_quoted_mention_is_not_a_label() -> None:
    vfp = _load_module()
    # A disclosure sentence quoting the token, as the corrected #782 doc does.
    text = 'The driver **mislabeled "Frozen:"** the absolute criterion `x <= 1`.'
    assert vfp.extract_frozen_labels(text) == [], (
        "a quoted mention of \"Frozen:\" must not be read as a live label"
    )
    # A real bold label IS read, with its quoted criterion.
    labels = vfp.extract_frozen_labels("> **Frozen:** `rho -> 1`")
    assert len(labels) == 1
    assert labels[0].criterion == "rho -> 1"


# --------------------------------------------------------------------------
# Gating is by date: a pre-cutoff doc warns, never gates.
# --------------------------------------------------------------------------

def test_pre_gate_date_is_warn_only() -> None:
    vfp = _load_module()
    from datetime import date
    # A mismatch on a pre-cutoff-dated doc is a warn (not gating).
    findings = vfp.scan_doc(
        _FIXTURES / "case_770_fabricated" / "research"
        / "2026-07-30_constituent-cage-fixture_result.md",
        _FIXTURES / "case_770_fabricated",
        date(2027, 1, 1),   # cutoff in the future -> the 2026-07-30 doc is pre-gate
        set(),
    )
    assert findings, "the mismatch must still be reported"
    assert all(not f.gating for f in findings), "pre-gate findings must be warn-only"


# --------------------------------------------------------------------------
# REPAIR 1 (audit 3a) — backdated-filename evasion. Severity keys on
# max(filename date, first-add date); an UNTRACKED doc is new by definition and
# GATES even with a pre-cutoff filename prefix. (Fixtures are not in git history
# as research/ docs, so the logic is exercised via the untracked-doc path.)
# --------------------------------------------------------------------------

def _write_backdated_mismatch(tmp: Path) -> Path:
    """A pre-cutoff-NAMED result doc carrying a Frozen criterion absent from its
    (sibling) prereg. The backdated prefix is the evasion; the doc is new."""
    research = tmp / "research"
    research.mkdir(parents=True)
    (research / "2026-07-01_backdated-fixture_prereg-FROZEN.md").write_text(
        "# Backdated prereg\n\nFrozen bins: `real criterion <= 0.25`\n",
        encoding="utf-8",
    )
    doc = research / "2026-07-01_backdated-fixture_result.md"
    doc.write_text(
        "# Backdated result\n\n"
        "Prereg-file: research/2026-07-01_backdated-fixture_prereg-FROZEN.md\n\n"
        "> **Gate — Frozen:** `fabricated criterion <= 0.10`\n",
        encoding="utf-8",
    )
    return doc


def test_backdated_untracked_doc_gates() -> None:
    vfp = _load_module()
    from datetime import date
    import tempfile
    cutoff = date(2026, 7, 22)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        doc = _write_backdated_mismatch(tmp)
        # add_dates provided but the doc is ABSENT (untracked) -> gating.
        gating = [
            f for f in vfp.scan_doc(doc, tmp, cutoff, set(), add_dates={})
            if f.gating
        ]
        assert any(f.kind == "mismatch" for f in gating), (
            "a backdated-filename, untracked result doc with a Frozen mismatch "
            "must GATE, not warn (max(filename, add-date) + untracked=new rule)"
        )
        # Contrast: the LEGACY filename-only path (add_dates=None) would WARN —
        # this is exactly the evasion REPAIR 1 closes.
        legacy = vfp.scan_doc(doc, tmp, cutoff, set(), add_dates=None)
        assert legacy and all(not f.gating for f in legacy), (
            "filename-only (legacy) severity lets the backdated prefix warn — "
            "the hole REPAIR 1 closes"
        )


# --------------------------------------------------------------------------
# Trivial-runtime / stdlib-only sanity.
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# REPAIR 2 (audit 3b) — quoted-label smuggle is surfaced (advisory), while the
# corrected #770/#782 disclosure lines stay 0-findings (proximity discriminator).
# --------------------------------------------------------------------------

# Verbatim fragments from the merged, corrected #782 disclosure lines (sec 7.6):
# a backtick criterion, then prose, then `mislabeled "Frozen:"`, then MORE prose.
# The quoted `"Frozen:"` is NOT immediately followed by a quoted token -> no hit.
_DISCLOSURE_770_782 = [
    'agreement `|ext1−ext2| ≤ 0.10` that it **mislabeled "Frozen:"** '
    '(a criterion invented post-freeze) and normalized the ratio.',
    'the frozen relative shell-agreement (ii) `|Δ|/mean ≤ 0.25`, '
    '**mislabeled it "Frozen:"** in the code comment (a criterion invented).',
    'The driver **mislabeled "Frozen:"** the absolute criterion `x <= 1`.',
]

# The smuggle shape: a QUOTED "Frozen:" IMMEDIATELY followed by a quoted token.
_SMUGGLES = [
    '> **"Frozen:"** `fabricated criterion <= 0.10`',
    'note: "Frozen:" "|ext1-ext2| <= 0.10" (banked)',
    '`Frozen:` `some criterion` — backtick-wrapped label dodge',
]


def test_quoted_label_smuggle_is_surfaced_advisory() -> None:
    vfp = _load_module()
    for line in _SMUGGLES:
        assert vfp.find_quoted_label_smuggles(line), (
            f"the quoted-label smuggle shape must be surfaced: {line!r}"
        )
    # And the smuggle produces a NON-gating advisory finding through scan_doc,
    # even when the doc carries no REAL Frozen label (the whole dodge).
    import tempfile
    from datetime import date
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        research = tmp / "research"
        research.mkdir(parents=True)
        doc = research / "2026-07-30_smuggle-fixture_result.md"
        doc.write_text("# Smuggle\n\n" + _SMUGGLES[0] + "\n", encoding="utf-8")
        findings = vfp.scan_doc(doc, tmp, date(2026, 7, 22), set(), add_dates={})
        smug = [f for f in findings if f.kind == "smuggle"]
        assert smug, "a smuggle-only doc must still surface the advisory"
        assert all(not f.gating for f in smug), "the smuggle advisory must not gate"


def test_disclosure_lines_are_not_smuggles() -> None:
    vfp = _load_module()
    for line in _DISCLOSURE_770_782:
        assert vfp.find_quoted_label_smuggles(line) == [], (
            f"a real disclosure mention must NOT be read as a smuggle: {line!r}"
        )
        # ...and it must not be a live label either (regression on the base gate).
        assert vfp.extract_frozen_labels(line) == []


# --------------------------------------------------------------------------
# REPAIR 3 (audit 3c) — the header heuristic must not preempt the correctly-named
# sibling, and a gating-dated doc that resolves ONLY via a cross-lane header
# mention hard-fails (the explicit pointer is the documented escape).
# --------------------------------------------------------------------------

def test_naming_sibling_beats_header_heuristic() -> None:
    vfp = _load_module()
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        research = tmp / "research"
        research.mkdir(parents=True)
        # Decoy: another lane's prereg, mentioned in the header.
        (research / "2026-07-20_otherlane_prereg-FROZEN.md").write_text(
            "# Other lane\n\nFrozen: `decoy criterion`\n", encoding="utf-8")
        # The correctly-named sibling for THIS doc.
        (research / "2026-07-30_mylane_prereg-FROZEN.md").write_text(
            "# My lane\n\nFrozen: `real criterion <= 0.25`\n", encoding="utf-8")
        doc = research / "2026-07-30_mylane_result.md"
        text = ("# My lane result\n\n"
                "Resolves the frozen bins of "
                "`research/2026-07-20_otherlane_prereg-FROZEN.md`.\n\n"
                "> **Gate — Frozen:** `real criterion <= 0.25`\n")
        doc.write_text(text, encoding="utf-8")
        ref = vfp.resolve_prereg(doc, text, tmp)
        assert ref.method == "naming", (
            f"a correctly-named sibling must win over a header mention, got {ref.method}"
        )
        assert ref.path.name == "2026-07-30_mylane_prereg-FROZEN.md"


def test_gating_doc_cross_lane_header_gates() -> None:
    vfp = _load_module()
    from datetime import date
    import tempfile
    cutoff = date(2026, 7, 22)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        research = tmp / "research"
        research.mkdir(parents=True)
        crit = "cross-lane criterion <= 0.10"
        # Another lane's prereg that HAPPENS to contain the criterion string
        # (so the byte-check would false-PASS against the wrong file).
        (research / "2026-07-20_otherlane_prereg-FROZEN.md").write_text(
            f"# Other lane\n\nFrozen: `{crit}`\n", encoding="utf-8")
        # Gating-dated doc: no explicit pointer, NO naming sibling, header mention
        # of the OTHER lane's prereg (different date-stem).
        doc = research / "2026-07-30_mylane_result.md"
        text = ("# My lane result\n\n"
                "Resolves the frozen bins of "
                "`research/2026-07-20_otherlane_prereg-FROZEN.md`.\n\n"
                f"> **Gate — Frozen:** `{crit}`\n")
        doc.write_text(text, encoding="utf-8")
        findings = vfp.scan_doc(doc, tmp, cutoff, set(), add_dates=None)
        # The criterion byte-passes against the (wrong) prereg -> no mismatch...
        assert not any(f.kind == "mismatch" for f in findings), (
            "the wrong-prereg criterion byte-passes; the mismatch check cannot catch it"
        )
        # ...but the cross-lane header-only resolution GATES.
        gating = [f for f in findings if f.gating]
        assert any(f.kind == "no-explicit-pointer" for f in gating), (
            "a gating doc resolving ONLY via a cross-lane header mention must hard-fail"
        )


def test_gating_doc_same_stem_header_stays_advisory() -> None:
    vfp = _load_module()
    from datetime import date
    import tempfile
    cutoff = date(2026, 7, 22)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        research = tmp / "research"
        research.mkdir(parents=True)
        crit = "same-lane criterion <= 0.10"
        # SAME date-stem prereg (same lane/day, differently named) -> advisory only.
        (research / "2026-07-30_mylane-variant_prereg-FROZEN.md").write_text(
            f"# Same day\n\nFrozen: `{crit}`\n", encoding="utf-8")
        doc = research / "2026-07-30_mylane_result.md"
        text = ("# My lane result\n\n"
                "Resolves the frozen bins of "
                "`research/2026-07-30_mylane-variant_prereg-FROZEN.md`.\n\n"
                f"> **Gate — Frozen:** `{crit}`\n")
        doc.write_text(text, encoding="utf-8")
        findings = vfp.scan_doc(doc, tmp, cutoff, set(), add_dates=None)
        nep = [f for f in findings if f.kind == "no-explicit-pointer"]
        assert nep, "a header-heuristic gating doc should still advise the pointer"
        assert all(not f.gating for f in nep), (
            "a SAME-date-stem header resolution must stay advisory, not gate"
        )


def test_pure_stdlib_no_third_party_imports() -> None:
    src = _TOOL.read_text(encoding="utf-8")
    for banned in ("import numpy", "import sympy", "from ave", "import ave", "import scipy"):
        assert banned not in src, f"gate must not import {banned!r}"


if __name__ == "__main__":
    for case in ("case_770_fabricated", "case_782_swapped", "case_pass", "case_no_prereg"):
        g, w, _ = _run(case)
        print(f"{case}: {len(g)} gating, {len(w)} warn")
        for f in g:
            print(f"    FAIL [{f.kind}] {f.detail}")
    test_pr770_fabricated_string_is_caught()
    test_pr782_swapped_criterion_is_caught()
    test_no_prereg_hard_fails()
    test_pass_control_is_clean()
    test_quoted_mention_is_not_a_label()
    test_pre_gate_date_is_warn_only()
    test_backdated_untracked_doc_gates()
    test_quoted_label_smuggle_is_surfaced_advisory()
    test_disclosure_lines_are_not_smuggles()
    test_naming_sibling_beats_header_heuristic()
    test_gating_doc_cross_lane_header_gates()
    test_gating_doc_same_stem_header_stays_advisory()
    test_pure_stdlib_no_third_party_imports()
    print("ALL PASS")
