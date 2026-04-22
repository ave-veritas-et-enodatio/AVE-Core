"""
Unit tests for the defense-context checker.

Each rule gets two fixtures:
  - a "bad" source that contains the anti-pattern WITHOUT the mitigator,
    which must fire the rule
  - a "good" source that contains the anti-pattern AND the mitigator nearby,
    which must NOT fire the rule

Reference: src/scripts/defense_context_checker.py
"""

from pathlib import Path

from scripts.defense_context_checker import RULES, Rule, discover_targets, scan_file

def _write(tmp_path: Path, name: str, content: str) -> Path:
    """Write a fixture file and return its Path."""
    p = tmp_path / name
    p.write_text(content, encoding="utf-8")
    return p

def _rules_for(rule_id: str) -> list[Rule]:
    """Return the single rule matching this id (scan_file takes a list)."""
    return [r for r in RULES if r.id == rule_id]

# ───────────────────────────────────────────────────────────────────────────
# CRIT-1: known-stale 139/450 arithmetic
# ───────────────────────────────────────────────────────────────────────────
class TestKnownStaleArithmetic:
    def test_bare_fraction_fires(self, tmp_path: Path) -> None:
        p = _write(tmp_path, "bad.md", "sin²θ₁₂ = 2/7 + 1/45 = 139/450.")
        findings = scan_file(p, _rules_for("CRIT-1"))
        assert len(findings) == 1
        assert findings[0].severity == "critical"

    def test_latex_frac_fires(self, tmp_path: Path) -> None:
        p = _write(tmp_path, "bad.tex", r"\frac{2}{7} + \frac{1}{45} = \frac{139}{450}")
        findings = scan_file(p, _rules_for("CRIT-1"))
        assert len(findings) == 1

    def test_correct_97_315_no_fire(self, tmp_path: Path) -> None:
        p = _write(tmp_path, "good.md", "sin²θ₁₂ = 2/7 + 1/45 = 97/315.")
        findings = scan_file(p, _rules_for("CRIT-1"))
        assert findings == []

# ───────────────────────────────────────────────────────────────────────────
# B1: α as free/input parameter without Golden-Torus derivation cross-ref
# ───────────────────────────────────────────────────────────────────────────
class TestAlphaAsInput:
    def test_alpha_free_parameter_no_mitigator_fires(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "bad.tex",
            "The framework takes α as the input parameter from CODATA and "
            "derives all downstream quantities from it. This is the single "
            "empirical anchor of the theory.",
        )
        findings = scan_file(p, _rules_for("B1"))
        assert len(findings) >= 1
        assert findings[0].severity == "warn"

    def test_alpha_with_ch8_ref_no_fire(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "good.tex",
            r"Historically α was treated as the one free parameter. "
            r"The zero-parameter closure is now complete: α is derived from "
            r"the Golden Torus S$_{11}$-minimum geometry in "
            r"Ch.~\ref{ch:alpha_golden_torus}.",
        )
        findings = scan_file(p, _rules_for("B1"))
        assert findings == []

    def test_alpha_with_prose_mitigator_no_fire(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "good.md",
            "In earlier work α was treated as the input parameter. "
            "With the Golden Torus derivation this is superseded: "
            "α⁻¹ = 4π³ + π² + π ≈ 137.036304 from first principles.",
        )
        findings = scan_file(p, _rules_for("B1"))
        assert findings == []

# ───────────────────────────────────────────────────────────────────────────
# B2: Millennium-problem proof claim without engineering-physics caveat
# ───────────────────────────────────────────────────────────────────────────
class TestMillenniumProofs:
    def test_yang_mills_proof_no_caveat_fires(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "bad.md",
            "The Yang-Mills mass gap is proved via the Axiom 4 saturation " "kernel applied to the Wilson action.",
        )
        findings = scan_file(p, _rules_for("B2"))
        assert len(findings) >= 1

    def test_navier_stokes_solved_no_caveat_fires(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "bad.md",
            "The Navier-Stokes smoothness problem is solved by the discrete " "lattice floor at ℓ_node.",
        )
        findings = scan_file(p, _rules_for("B2"))
        assert len(findings) >= 1

    def test_strong_cp_with_caveat_no_fire(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "good.md",
            "Strong CP is framework-conditional on the lattice axioms; "
            "the engineering-physics derivation uses the saturation gate. "
            "A Clay-rigorous formalization remains open future work.",
        )
        findings = scan_file(p, _rules_for("B2"))
        assert findings == []

    def test_millennium_with_ch12_ref_no_fire(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "good.tex",
            r"The Millennium problems are solved at the engineering-physics "
            r"level in Ch.~\ref{ch:millennium_prizes}; see caveats there.",
        )
        findings = scan_file(p, _rules_for("B2"))
        assert findings == []

# ───────────────────────────────────────────────────────────────────────────
# A3: non-integer coordination z_0 ≈ 51.25 without amorphous framing
# ───────────────────────────────────────────────────────────────────────────
class TestNonIntegerCoordination:
    def test_z0_51_25_no_amorphous_fires(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "bad.tex",
            r"Solving the EMT quadratic at $p^* = 8\pi\alpha$ gives "
            r"$z_0 \approx 51.25$, the effective coordination number of "
            r"the vacuum lattice.",
        )
        findings = scan_file(p, _rules_for("A3"))
        assert len(findings) >= 1

    def test_z0_with_amorphous_prelude_no_fire(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "good.tex",
            r"Because the vacuum is an amorphous disordered manifold (not a "
            r"crystal), non-integer effective coordination is generic. "
            r"The EMT quadratic gives $z_0 \approx 51.25$.",
        )
        findings = scan_file(p, _rules_for("A3"))
        assert findings == []

    def test_z0_with_phillips_thorpe_no_fire(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "good.tex",
            r"In the Phillips-Thorpe rigidity framework, $z_0 \approx 51.25$ " r"is the glass-transition coordination.",
        )
        findings = scan_file(p, _rules_for("A3"))
        assert findings == []

# ───────────────────────────────────────────────────────────────────────────
# A1: 0.00% / Exact in prediction tables without identity classification
# ───────────────────────────────────────────────────────────────────────────
class TestExactPredictionClassification:
    def test_exact_table_row_no_identity_fires(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "bad.md",
            "| 2 | Z₀ from Axiom 1 | 0.00% | ✅ |\n" "| 42 | α invariance under gravity | Exact | ✅ |",
        )
        findings = scan_file(p, _rules_for("A1"))
        assert len(findings) >= 1
        assert findings[0].severity == "info"

    def test_exact_with_identity_tag_no_fire(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "good.md",
            "| 2 | Z₀ = √(μ₀/ε₀) — definitional identity | 0.00% | ✅ |",
        )
        findings = scan_file(p, _rules_for("A1"))
        assert findings == []

    def test_exact_with_axiom_manifestation_no_fire(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "good.md",
            "| 43 | BCS B_c(T) — Axiom 4 manifestation at thermal scaling | 0.00% | ✅ |",
        )
        findings = scan_file(p, _rules_for("A1"))
        assert findings == []

# ───────────────────────────────────────────────────────────────────────────
# C2: anti-cheat badge overclaim
# ───────────────────────────────────────────────────────────────────────────
class TestAntiCheatBadgeScope:
    def test_zero_smuggled_no_scope_fires(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "bad.md",
            "The verify_universe.py scan confirms zero smuggled parameters " "across the entire codebase.",
        )
        findings = scan_file(p, _rules_for("C2"))
        assert len(findings) >= 1
        assert findings[0].severity == "info"

    def test_zero_smuggled_with_scope_no_fire(self, tmp_path: Path) -> None:
        p = _write(
            tmp_path,
            "good.md",
            "The verify_universe.py scan prohibits scipy.constants imports "
            "and CODATA-value literal magic numbers — a narrow AST scan. "
            "This guarantees zero smuggled parameters in the specific scope "
            "of module-level literals.",
        )
        findings = scan_file(p, _rules_for("C2"))
        assert findings == []

# ───────────────────────────────────────────────────────────────────────────
# Meta: discovery and end-to-end
# ───────────────────────────────────────────────────────────────────────────
class TestDiscovery:
    def test_discover_targets_includes_readme(self, tmp_path: Path) -> None:
        # Simulate minimal repo layout
        (tmp_path / "manuscript").mkdir()
        (tmp_path / "manuscript" / "ave-kb").mkdir()
        (tmp_path / "README.md").write_text("# test", encoding="utf-8")
        (tmp_path / "LIVING_REFERENCE.md").write_text("# ref", encoding="utf-8")
        _write(tmp_path / "manuscript", "test.tex", "content")
        _write(tmp_path / "manuscript" / "ave-kb", "test.md", "content")

        targets = discover_targets(tmp_path)
        names = {p.name for p in targets}
        assert "README.md" in names
        assert "LIVING_REFERENCE.md" in names
        assert "test.tex" in names
        assert "test.md" in names

    def test_discover_excludes_claude_md(self, tmp_path: Path) -> None:
        (tmp_path / "manuscript" / "ave-kb").mkdir(parents=True)
        _write(tmp_path / "manuscript" / "ave-kb", "CLAUDE.md", "invariants")
        _write(tmp_path / "manuscript" / "ave-kb", "regular.md", "content")

        targets = discover_targets(tmp_path)
        names = {p.name for p in targets}
        assert "CLAUDE.md" not in names
        assert "regular.md" in names

class TestEndToEnd:
    def test_all_rules_compile(self) -> None:
        """Every rule's pattern and mitigator must be valid regex."""
        import re

        for rule in RULES:
            re.compile(rule.pattern)
            if rule.mitigator is not None:
                re.compile(rule.mitigator)

    def test_rule_ids_unique(self) -> None:
        ids = [r.id for r in RULES]
        assert len(ids) == len(set(ids))

    def test_rule_severities_valid(self) -> None:
        for rule in RULES:
            assert rule.severity in {"critical", "warn", "info"}

    def test_all_rules_have_see_pointer(self) -> None:
        """Every rule must point at either the framing doc or an audit playbook."""
        for rule in RULES:
            assert rule.see, f"Rule {rule.id} missing 'see' pointer"
