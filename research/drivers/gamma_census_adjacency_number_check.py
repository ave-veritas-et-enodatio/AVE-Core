#!/usr/bin/env python3
"""gamma_census_adjacency_number_check.py — standing gate for the R33 census repair.

Ruled at `_orchestration/docket-entries/2026-08-07-rulings-r31-r33.md` (R33), Grant
verbatim *"Agree."*; documented at
`_orchestration/docket-entries/2026-08-07-gamma-tag-spec-correction.md`.

Checks, on every `make verify` (all gating; nonzero exit on any failure):

  1. IDENTITY  — the post-R33 actionable set on the CURRENT tree reconciles exactly
                 against the merged `\\gammaundeclared{}` tag population:
                     post-R33 actionable = tagged + the one §4.4 do-not-touch site.
                 A recomputed multiset, not a declared number.
  2. FINDINGS  — every line that hosted one of the 33 #923 findings contributes
                 exactly `pre_fix - eliminated` actionable sites after the repair.
                 32 of the 33 are eliminated BY THE CLASSIFIER; the 33rd
                 (QUOTED-RULED-TEXT) is a spec §4.4 SITE-SELECTION exclusion, not a
                 classification property, and is asserted to REMAIN actionable —
                 stated rather than hidden, because encoding a site-selection rule
                 into the census would be building the instrument to hit a number.
  3. PLANTED   — synthetic lines exercising each repaired defect classify as the
                 repair requires; in particular a far-value line (the only ±1 value
                 sits well past the Γ, behind unrelated text) must NOT read as
                 adjacent, a value outside the Γ's math span must not be reached,
                 and a Γ inside a TRAILING comment must not count as typeset.
                 Nothing in these lines reads the corpus, so a corpus edit can
                 never quietly turn one green.
  4. MUTATION  — `--mutation-receipt` forces `ADJACENCY_FIX` OFF and re-runs the SAME
                 check code. Each named control must FIRE. A control that does not
                 fire prints MISSED and the run fails, so no check here is a
                 tautology over an unperturbed instrument.

WHAT EACH CHECK CONSUMES (scoped honestly, because "recomputed" is not uniform):
  * IDENTITY and the PLANTED families consume NO declared number — both sides are
    recomputed from the tree / from the classifier on this run.
  * FINDINGS consumes 29 frozen `expected_post_fix` baselines. That is a legitimate
    REGRESSION BASELINE, not a self-declared field: each was measured at the #923
    execution SHA `2520e467` and re-measured at `644a4546`, reproducing at both. It
    is called out here so nobody reads the whole gate as baseline-free.

Standalone: `python3 research/drivers/gamma_census_adjacency_number_check.py`
            `python3 research/drivers/gamma_census_adjacency_number_check.py --mutation-receipt`
Auto-discovered by `make verify` via `verify-lane-number-checks` (the
`research/drivers/*_number_check.py` glob); the receipt is auto-run because this
source declares the literal `--mutation-receipt`.
"""

from __future__ import annotations

import collections
import importlib.util
import re
import sys
from pathlib import Path

DRIVERS = Path(__file__).resolve().parent
REPO = DRIVERS.parents[1]
CENSUS = REPO / "src/scripts/signed_gamma_census.py"

TAG_RE = re.compile(r"\\gammaundeclared\{\}")

#: The one #923 finding the CLASSIFIER cannot and must not eliminate: the Γ sits
#: inside a verbatim ``…'' quotation of a canonical KB leaf, which spec §4 item 4
#: excludes as a SITE-SELECTION rule ("any line inside quoted ruled text"). Spec §1
#: has four conditions — file class, rendered, channel, sign — and quotation is not
#: one of them, so this site is correctly ACTIONABLE and correctly UNTAGGED.
QUOTED_EXCLUSION = ("manuscript/vol_9_vacuum_datasheet/chapters/12_cosmological_characteristics.tex", 190)

#: (path, lineno, pre_fix_actionable, findings_hosted, expected_post_fix, classes)
#: measured at the #923 execution SHA 2520e467 and re-derived at 644a4546.
#:
#: `classes` is the #923 TRIAGE label — the reason the site was withheld from
#: tagging. It is NOT always the guard that eliminates the site today, because
#: `classify_sign` short-circuits on the left-operand test before it reads a
#: value, so a site can be caught by two repairs at once. Where the audit
#: measured a divergence the label is DUAL, naming the triage class first and
#: the eliminating guard second — an honest attribution beats a tidy one.
FINDING_LINES: tuple[tuple[str, int, int, int, int, str], ...] = (
    ("manuscript/backmatter/01_appendices.tex", 80, 2, 1, 1, "NOT-THE-LEFT-OPERAND"),
    ("manuscript/common_equations/eq_axiom_3.tex", 37, 2, 1, 1, "MIS-ASSOCIATION"),
    ("manuscript/vol_0_engineering_compendium/chapters/01_theoretical_stress_tests.tex", 86, 2, 1, 1, "NOT-THE-LEFT-OPERAND"),
    ("manuscript/vol_1_foundations/chapters/07_regime_map.tex", 225, 2, 1, 1, "MIS-ASSOCIATION"),
    ("manuscript/vol_2_subatomic/chapters/01_topological_matter.tex", 167, 2, 1, 1, "MIS-ASSOCIATION"),
    ("manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex", 4053, 1, 1, 0, "MIS-ASSOCIATION"),
    ("manuscript/vol_3_macroscopic/chapters/19_phase_transition_melting.tex", 400, 1, 1, 0, "MIS-ASSOCIATION"),
    ("manuscript/vol_3_macroscopic/chapters/19_phase_transition_melting.tex", 452, 1, 1, 0, "TRUNCATED-VALUE"),
    ("manuscript/vol_5_biology/chapters/02_organic_circuitry.tex", 522, 1, 1, 0, "TRUNCATED-VALUE"),
    ("manuscript/vol_5_biology/chapters/02_organic_circuitry.tex", 772, 1, 1, 0, "TRUNCATED-VALUE"),
    ("manuscript/vol_6_periodic_table/chapters/16_silicon.tex", 89, 1, 1, 0, "TRUNCATED-VALUE (eliminated by NOT-THE-LEFT-OPERAND; both fire)"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex", 11, 2, 1, 1, "MIS-ASSOCIATION"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex", 214, 1, 1, 0, "NOT-THE-LEFT-OPERAND"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex", 225, 2, 1, 1, "MIS-ASSOCIATION"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex", 266, 3, 3, 0, "MIS-ASSOCIATION"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex", 269, 1, 1, 0, "NOT-THE-LEFT-OPERAND"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/03a_device_circuit_models.tex", 232, 1, 1, 0, "MIS-ASSOCIATION"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex", 164, 1, 1, 0, "TRUNCATED-VALUE"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex", 165, 1, 1, 0, "TRUNCATED-VALUE"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex", 170, 1, 1, 0, "TRUNCATED-VALUE"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex", 172, 4, 2, 2, "MIS-ASSOCIATION"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex", 185, 2, 2, 0, "MIS-ASSOCIATION/TRUNCATED-VALUE"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex", 201, 1, 1, 0, "TRUNCATED-VALUE"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex", 241, 3, 1, 2, "TRUNCATED-VALUE"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/12_cosmological_characteristics.tex", 190, 2, 1, 2, "QUOTED-RULED-TEXT"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/13_application_examples.tex", 35, 2, 1, 1, "MIS-ASSOCIATION"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/13_application_examples.tex", 267, 1, 1, 0, "MIS-ASSOCIATION"),
    ("manuscript/vol_9_vacuum_datasheet/chapters/15_falsification_tests.tex", 29, 2, 1, 1, "MIS-ASSOCIATION"),
    ("manuscript/vol_9_vacuum_datasheet/figures/electron_selfbiased_multiport.tex", 46, 1, 1, 0, "TRAILING-COMMENT (rendered=False) + NOT-THE-LEFT-OPERAND (sign=none); both fire independently"),
)

#: (label, line, expected sign, why). Synthetic — nothing here reads the corpus, so a
#: corpus edit can never quietly turn one of these green.
PLANTED: tuple[tuple[str, str, str, str], ...] = (
    (
        "FAR-VALUE",
        r"the substrate minimizes $|\Gamma|^2$ at every internal boundary and, much "
        r"later in the same sentence after a great deal of unrelated prose about "
        r"impedance, the wall closes at $\Gamma = -1$ exactly.",
        "none",
        "the only +-1 value sits far away behind unrelated text and a math-mode exit",
    ),
    (
        "ADJACENT",
        r"total reflection at the wall ($\Gamma = -1$) closes the cavity.",
        "-1",
        "the value is adjacent to its own Gamma; the census must still see it",
    ),
    (
        "TRUNCATED",
        r"the corollary $|\Gamma|^2 = 1 - \alpha$ inherits the tank quality factor.",
        "other",
        "the asserted value is 1 - alpha, not 1",
    ),
    (
        "NOT-LEFT-OPERAND",
        r"by Op17 ($T^2 = 1 - \Gamma^2 \to 1$ at $\Gamma = 0$) the coupling is matched.",
        "none",
        "the limit belongs to T^2; the same line says Gamma = 0",
    ),
    (
        "MAGNITUDE",
        r"Axiom~3 forces only $|\Gamma| = 1$; the sign needs a reference plane.",
        "+1",
        "an unsigned magnitude assertion is still a value the census reports",
    ),
    (
        "CHAIN",
        r"\[ \Gamma = \frac{Z_{knot} - Z_0}{Z_{knot} + Z_0} = \frac{0 - 377}{0 + 377} = -1 \]",
        "-1",
        "a relation CHAIN does assert its final value for Gamma",
    ),
    (
        # ISOLATES `math_segment`. Constructed so no other guard can mask it: the
        # text before the Gamma ends in an opener (left-operand passes), the value
        # is a clean `-1` (the termination guard passes), and `$` is a BRIDGE
        # character — so the anchored bridge would walk straight out of the math
        # span and read a value that is not in the same expression. Only the
        # span confinement stops it.
        "MATH-SPAN",
        r"total reflection ($\Gamma$ = -1) at the wall.",
        "none",
        "the value sits OUTSIDE the Gamma's math span; the bridge alone would reach it",
    ),
)

#: (label, line, expected `rendered`, why). The comment repair is a `rendered`
#: property, not a sign, so it needs its own control — and it needs one BADLY:
#: on the corpus `is_comment_site` differs from `is_comment_line` at exactly ONE
#: site, and at that site the left-operand guard fires first, so the comment
#: repair is behaviourally masked and nothing else here would exercise it. This
#: line is built so ONLY the comment repair can catch it: the text before the Γ
#: ends in an opener, and the value is adjacent and clean.
PLANTED_RENDERED: tuple[tuple[str, str, bool, str], ...] = (
    (
        "TRAILING-COMMENT",
        r"\draw (0,0) -- (1,1); % shorted stub ($\Gamma = -1$) wall",
        False,
        "the Gamma is inside a TRAILING comment; the line's first token is not one",
    ),
    (
        "RENDERED-CONTROL",
        r"total reflection ($\Gamma = -1$) at the wall.",
        True,
        "no comment anywhere; the repair must not start suppressing typeset sites",
    ),
)


def load_census():
    spec = importlib.util.spec_from_file_location("signed_gamma_census", CENSUS)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["signed_gamma_census"] = mod  # dataclasses needs the module registered
    spec.loader.exec_module(mod)
    return mod


def actionable_sites(cen) -> collections.Counter:
    """The spec §1 set on the CURRENT tree, recomputed through the live classifier."""
    universe = cen.Universe(
        roots=("manuscript",),
        exts=(".tex", ".md"),
        gamma_form="all",
        relation="any",
        gap="adjacent-nested",
        signs="any",
        minus_forms="unicode",
        glue="math",
        comments="include",
    )
    sites, _raw = cen.scan_python(REPO, universe)
    return collections.Counter(
        (s.path, s.lineno)
        for s in sites
        if s.file_class == "print_tex"
        and s.rendered
        and s.channel == "unspecified"
        and s.sign in ("-1", "+1")
    )


def tagged_sites() -> collections.Counter:
    """Every merged `\\gammaundeclared{}` marker, by (path, line), excl. the definition."""
    out: collections.Counter = collections.Counter()
    for path in sorted((REPO / "manuscript").rglob("*.tex")):
        rel = path.relative_to(REPO).as_posix()
        if rel.endswith("structure/commands.tex"):
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            n = len(TAG_RE.findall(line))
            if n:
                out[(rel, lineno)] += n
    return out


def classify_line(cen, line: str, suffix: str = ".tex") -> str:
    """Sign the census would assign to the FIRST Γ occurrence on a synthetic line."""
    regex = re.compile(
        cen.Universe(gamma_form="all", relation="any", signs="any").detection_regex()
    )
    match = regex.search(line)
    if match is None:
        return "no-match"
    after = cen.strip_gamma_token(line[match.start():])
    return cen.classify_sign(after, line[: match.start()])


def rendered_of_first_gamma(cen, line: str, suffix: str = ".tex") -> bool:
    """`rendered` the census would assign to the FIRST Γ occurrence on a line.

    Mirrors `scan_python`'s own branch exactly — per-OCCURRENCE with the repair
    on, per-LINE with it off — so this control actually exercises the toggle
    rather than restating one side of it.
    """
    regex = re.compile(
        cen.Universe(gamma_form="all", relation="any", signs="any").detection_regex()
    )
    match = regex.search(line)
    if match is None:
        return True
    if cen.ADJACENCY_FIX:
        return not cen.is_comment_site(suffix, line, match.start())
    return not cen.is_comment_line(suffix, line)


def run_checks(cen) -> list[str]:
    """Every control, as a list of failure strings. Empty list == all green."""
    fails: list[str] = []

    # 1. IDENTITY ---------------------------------------------------------------
    act, tags = actionable_sites(cen), tagged_sites()
    expected = collections.Counter(tags)
    expected[QUOTED_EXCLUSION] += 1
    if act != expected:
        fails.append(
            "IDENTITY: post-R33 actionable != tagged + the one §4.4 exclusion  "
            f"(actionable={sum(act.values())}, tagged={sum(tags.values())}; "
            f"actionable-only={sorted((act - expected).elements())}, "
            f"expected-only={sorted((expected - act).elements())})"
        )

    # 2. FINDINGS ---------------------------------------------------------------
    for path, lineno, pre, hosted, want, classes in FINDING_LINES:
        got = act[(path, lineno)]
        if got != want:
            fails.append(
                f"FINDINGS: {path}:{lineno} [{classes}] hosts {hosted} of the 33 "
                f"#923 findings; expected {want} actionable after the repair "
                f"(pre-fix {pre}), measured {got}"
            )

    # 3. PLANTED — sign ---------------------------------------------------------
    for label, line, want, why in PLANTED:
        got = classify_line(cen, line)
        if got != want:
            fails.append(
                f"PLANTED[{label}]: expected sign {want!r} ({why}), measured {got!r}"
            )

    # 4. PLANTED — rendered -----------------------------------------------------
    for label, line, want, why in PLANTED_RENDERED:
        got = rendered_of_first_gamma(cen, line)
        if got != want:
            fails.append(
                f"PLANTED[{label}]: expected rendered={want} ({why}), measured {got}"
            )

    return fails


# =====================================================================================
# MUTATION RECEIPT
# ONE perturbation — `ADJACENCY_FIX = False`, i.e. the pre-R33 instrument — fed back
# through the SAME check code above. Each control named below must FIRE. A control that
# does not fire prints MISSED and the run fails, so none of the checks is a tautology
# over an unperturbed instrument. This is the forced-failure proof the R33 ruling asks
# for: "force the fix off -> the receipt goes MISSED".
# =====================================================================================
CONTROLS: tuple[tuple[str, str], ...] = (
    ("IDENTITY", "the actionable set no longer reconciles against the tag population"),
    ("FINDINGS", "the #923 finding lines come back as actionable"),
    ("PLANTED[FAR-VALUE]", "a value far down the line is read as adjacent again"),
    ("PLANTED[TRUNCATED]", "`= 1 - \\alpha` is read as `+1` again"),
    ("PLANTED[NOT-LEFT-OPERAND]", "T^2's limit is attributed to Gamma again"),
    ("PLANTED[MATH-SPAN]", "the bridge walks out of the math span and reads a foreign value"),
    ("PLANTED[TRAILING-COMMENT]", "a Gamma inside a trailing comment counts as typeset again"),
)


def mutation_receipt(cen) -> int:
    print("[gamma-adjacency] MUTATION RECEIPT — forcing ADJACENCY_FIX = False")
    print("[gamma-adjacency]   (the pre-R33 instrument; the corpus is NOT touched)")
    cen.ADJACENCY_FIX = False
    try:
        fails = run_checks(cen)
    finally:
        cen.ADJACENCY_FIX = True
    missed = []
    for name, why in CONTROLS:
        fired = any(f.startswith(name) for f in fails)
        print(f"  {'FIRED ' if fired else 'MISSED'}  {name:26s} — {why}")
        if not fired:
            missed.append(name)
    print(f"[gamma-adjacency]   perturbed run produced {len(fails)} failure(s)")
    if missed:
        print("[gamma-adjacency] *** RECEIPT FAILED — control(s) did not fire: "
              + ", ".join(missed))
        print("[gamma-adjacency]     A control that cannot fire is not a control.")
        return 1
    print("[gamma-adjacency] RECEIPT OK — every declared control fired under the "
          "forced-off instrument.")
    return 0


def main(argv: list[str]) -> int:
    cen = load_census()
    if "--mutation-receipt" in argv:
        return mutation_receipt(cen)

    print("[gamma-adjacency] R33 census-repair gate (signed_gamma_census.classify_sign)")
    act, tags = actionable_sites(cen), tagged_sites()
    print(f"[gamma-adjacency]   post-R33 actionable : {sum(act.values())} sites / "
          f"{len(act)} lines / {len({p for p, _ in act})} files")
    print(f"[gamma-adjacency]   merged tags         : {sum(tags.values())} markers / "
          f"{len(tags)} lines")
    print(f"[gamma-adjacency]   §4.4 do-not-touch   : 1 "
          f"({QUOTED_EXCLUSION[0]}:{QUOTED_EXCLUSION[1]}, quoted ruled text)")
    print(f"[gamma-adjacency]   identity            : "
          f"{sum(act.values())} = {sum(tags.values())} tagged + 1 site-selection exclusion")

    fails = run_checks(cen)
    for f in fails:
        print(f"  *** {f}")
    if fails:
        print(f"[gamma-adjacency] *** FAILED — {len(fails)} check(s)")
        return 1
    print(f"[gamma-adjacency] OK — identity reconciled, {len(FINDING_LINES)} finding "
          f"line(s) re-checked, {len(PLANTED) + len(PLANTED_RENDERED)} planted case(s) correct.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
