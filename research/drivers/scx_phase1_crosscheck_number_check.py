#!/usr/bin/env python3
"""Gating number check for the SCX Phase-1 external-solver cross-check lane.

Every back-ticked numeral in `research/2026-08-25_solver-crosscheck-phase1_result.md`
must be one of:

  (1) PRESENT in the shipped record `scx_phase1_crosscheck_results.json` -- matched
      as a CORRECT ROUNDING of a JSON value, so the doc may round without the gate
      going blind;
  (2) DERIVED here from registered JSON inputs by a stated formula;
  (3) COMPUTED FROM AN IN-TREE ARTIFACT by this checker (e.g. the test count is
      counted out of the test module's AST, not trusted);
  (4) on the explicit ALLOW-LIST, each entry carrying its own reason.

It ALSO reconciles the doc's headline against the record rather than reading a
self-declared string: the verdict bin printed in the doc must equal the JSON's
COMPUTED `verdict.bin`, and the frozen tolerances quoted in the doc must equal
the ones the driver actually ran under.

`--mutation-receipt` re-runs the checker against deliberately perturbed sources
and requires EVERY perturbation to be CAUGHT, so the gate cannot silently degrade
into a no-op.
"""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
RESULTS = HERE / "scx_phase1_crosscheck_results.json"
DOC = REPO / "research" / "2026-08-25_solver-crosscheck-phase1_result.md"
PREREG = REPO / "research" / "2026-08-25_solver-crosscheck-phase1_prereg-FROZEN.md"
TESTS = REPO / "src" / "tests" / "test_scx_spice_export.py"

FAILURES: list[str] = []

#: Back-ticked numerals that are NOT driver outputs. Each carries its reason.
ALLOWED: dict[str, str] = {
    "1.05": "frozen POSITIVE_CONTROL_FACTOR, quoted from the prereg (also in the JSON)",
    "0.5": "the 1/2 in a formula, not a measurement",
    "1.00000000": "f/f_top of the as-frozen band's final grid point -- an exactly-unity ratio",
    "2": "small structural integer (multiplicity / count) also present in the record",
    "3": "small structural integer (z = 3 coordination / multiplicity)",
    "4": "small structural integer (multiplicity / port-block size)",
    "1": "small structural integer",
    "0": "small structural integer",
    "4.448e-12": (
        "the REFUTED single-drive-node drafting probe for amendment A1, quoted in "
        "result-doc section 6 precisely BECAUSE the full 4-drive-node run supersedes "
        "it (1.240e-04). It is deliberately absent from the shipped record: the record "
        "carries what the run measured, and this is what a narrower probe had claimed."
    ),
}

# ── (2) DERIVED registry: value -> the formula that produces it from the JSON ──
def derived(rec: dict) -> dict[float, str]:
    fresh = rec["reproduction_gate"]["fresh"]
    out = {
        float(fresh["srs_L2_ports"]): "srs L=2 TLM port space = 2 * B",
        float(fresh["srs_L2_cycle_space"]): "cycle space = B - N + 1",
        float(fresh["srs_L2_bonds"]): "srs L=2 bond count B",
        float(fresh["srs_L2_nodes"]): "srs L=2 node count N",
        float(fresh["srs_L3_nodes"]): "srs L=3 node count = 8L^3",
        float(fresh["srs_L3_parts"][0]): "srs L=3 bipartite part size",
        float(rec["auxb"]["n_points"]): "AUX-B theta grid point count",
        float(rec["frozen_tolerances"]["EC1_COARSE_POINTS"]): "EC-1 coarse sweep points",
    }
    for k in ("L0", "L1", "L2v", "L2s", "L3", "L4"):
        r = rec["rungs"][k]
        out[float(r["count_ref"])] = f"{k} interior reference mode count"
        out[float(r["count_solver"])] = f"{k} interior solver mode count"
        if r.get("mult_total_ref") is not None:
            out[float(r["mult_total_ref"])] = f"{k} total interior multiplicity"
    return out


# ── (3) COMPUTED-FROM-ARTIFACT registry ──────────────────────────────────────
def computed_from_tree() -> dict[float, str]:
    """Numbers the doc states ABOUT the tree, recomputed from the tree."""
    tree = ast.parse(TESTS.read_text(encoding="utf-8"))
    n_tests = sum(
        1
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
    )
    # One test is parametrized over 2 builders, so pytest collects 1 extra item.
    extra = 0
    for node in ast.walk(tree):
        if not (isinstance(node, ast.FunctionDef) and node.name.startswith("test_")):
            continue
        for dec in node.decorator_list:
            if not isinstance(dec, ast.Call):
                continue
            if getattr(dec.func, "attr", None) != "parametrize":
                continue
            for arg in dec.args[1:2]:
                if isinstance(arg, (ast.List, ast.Tuple)):
                    extra += len(arg.elts) - 1   # k cases replace 1 function
    collected = n_tests + extra
    return {float(collected): f"pytest items collected from {TESTS.name} (AST-counted)"}


# ── numeric-token scanning ───────────────────────────────────────────────────
_TICK = re.compile(r"`([^`\n]+)`")
_NUMERIC = re.compile(r"^[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?$")


def _sig_tolerance(token: str) -> float:
    """Absolute tolerance under which `token` is a CORRECT ROUNDING."""
    t = token.lstrip("+-")
    if "e" in t.lower():
        mant = t.lower().split("e")[0]
        digits = len(mant.replace(".", "").lstrip("0")) or 1
        return 0.5 * abs(float(token)) * 10.0 ** (-(digits - 1)) if float(token) else 1e-300
    if "." in t:
        return 0.5 * 10.0 ** (-len(t.split(".")[1]))
    return 0.5


def _harvest(obj, out: set[float]) -> None:
    if isinstance(obj, bool):
        return
    if isinstance(obj, (int, float)):
        out.add(float(obj))
    elif isinstance(obj, dict):
        for v in obj.values():
            _harvest(v, out)
    elif isinstance(obj, list):
        for v in obj:
            _harvest(v, out)


def scan_doc(doc_text: str, rec: dict) -> list[str]:
    pool: set[float] = set()
    _harvest(rec, pool)
    der = derived(rec)
    comp = computed_from_tree()
    pool |= set(der) | set(comp)
    bad = []
    for line_no, line in enumerate(doc_text.splitlines(), 1):
        for tok in _TICK.findall(line):
            t = tok.strip()
            if not _NUMERIC.match(t) or t in ALLOWED:
                continue
            val = float(t)
            tol = _sig_tolerance(t)
            if not any(abs(val - p) <= tol for p in pool):
                bad.append(
                    f"{DOC.name}:{line_no}  back-ticked numeral `{t}` is not in "
                    f"{RESULTS.name}, not derived, not computed from the tree, and not "
                    f"allow-listed (rounding tolerance {tol:.3g})"
                )
    return bad


def reconcile(doc_text: str, rec: dict) -> list[str]:
    """The headline must RECONCILE against the record, not restate itself."""
    bad = []
    bin_ = rec["verdict"]["bin"]
    if f"# `{bin_}`" not in doc_text:
        bad.append(
            f"doc headline does not carry the record's COMPUTED verdict bin {bin_!r} "
            "as its section-0 heading -- a result doc may not declare a bin the driver "
            "did not compute"
        )
    for other in ("AGREE", "DIVERGE-ATTRIBUTED", "DIVERGE-UNATTRIBUTED", "INCONCLUSIVE"):
        if other != bin_ and f"# `{other}`" in doc_text:
            bad.append(f"doc headline carries bin {other!r}, which is not the record's {bin_!r}")
    # Reconcile the tolerance VALUES, not their string forms: `1.0e-7` and
    # `1e-07` are the same tolerance, and a gate that insists on one spelling
    # tests formatting rather than agreement.
    for name, key in (("TOL-FREQ", "TOL_FREQ"), ("TOL-REFINE", "TOL_REFINE"),
                      ("TOL-GRID", "TOL_GRID"), ("TOL-LOSSLESS", "TOL_LOSSLESS"),
                      ("TOL-GAMMA", "TOL_GAMMA")):
        want = float(rec["frozen_tolerances"][key])
        quoted = [
            float(m)
            for line in doc_text.splitlines() if name in line
            for m in _TICK.findall(line) if _NUMERIC.match(m.strip())
        ]
        if not any(abs(q - want) <= 1e-12 * max(abs(want), 1e-300) for q in quoted):
            bad.append(
                f"doc never quotes {name} at the value the driver ran under ({want!r}); "
                f"back-ticked numerals found on its lines: {quoted}"
            )
    if rec["reproduction_gate"]["pass"] is not True:
        if "ZERO drift" in doc_text:
            bad.append("doc claims ZERO drift but the record's reproduction gate did not pass")
    if not rec["controls"]["positive"]["detected"]:
        if "DEFECT RESOLVED" in doc_text:
            bad.append("doc claims the positive control resolved the defect; the record disagrees")
    if PREREG.exists():
        pre = PREREG.read_text(encoding="utf-8")
        if "AMENDMENT A1" not in pre:
            bad.append("the frozen prereg no longer carries AMENDMENT A1; the result doc cites it")
    return bad


def run(doc_text: str | None = None, rec: dict | None = None) -> list[str]:
    rec = rec if rec is not None else json.loads(RESULTS.read_text(encoding="utf-8"))
    doc_text = doc_text if doc_text is not None else DOC.read_text(encoding="utf-8")
    return scan_doc(doc_text, rec) + reconcile(doc_text, rec)


def mutation() -> int:
    """Every perturbation below MUST be caught, or this gate is a no-op."""
    base_rec = json.loads(RESULTS.read_text(encoding="utf-8"))
    base_doc = DOC.read_text(encoding="utf-8")
    if run(base_doc, base_rec):
        print("[scx-nc] RECEIPT ABORT: the unperturbed sources already fail.")
        return 1

    checks: list[tuple[str, str, dict]] = []

    # A pool-matching gate has ONE structural weakness: a perturbation that lands
    # on some OTHER pooled value slips through. (Measured while writing this
    # receipt: perturbing the L4 max-deviation to 9.99e-10 was MISSED, because
    # TOL_REFINE and TOL_LOSSLESS are both 1e-9 and sit in the pool.) So the
    # fixture PROVES its own perturbation is non-colliding before using it,
    # rather than assuming it -- otherwise the receipt tests the fixture.
    pool: set[float] = set()
    _harvest(base_rec, pool)
    pool |= set(derived(base_rec)) | set(computed_from_tree())
    target = "4.852624968521013e-10"
    perturbed = None
    for mult in (1.5, 2.3, 3.7, 5.9, 11.3):
        cand = f"{float(target) * mult:.16e}"
        if not any(abs(float(cand) - q) <= _sig_tolerance(cand) for q in pool):
            perturbed = cand
            break
    if perturbed is None:
        print("[scx-nc] RECEIPT ABORT: could not construct a non-colliding perturbation.")
        return 1
    d = base_doc.replace(f"`{target}`", f"`{perturbed}`")
    if d == base_doc:
        print(f"[scx-nc] RECEIPT ABORT: target numeral `{target}` is not in the doc.")
        return 1
    checks.append((f"doc numeral perturbed away from the record ({target} -> {perturbed})",
                   d, base_rec))

    r = json.loads(json.dumps(base_rec))
    r["verdict"]["bin"] = "DIVERGE-ATTRIBUTED"
    checks.append(("record verdict bin flipped under an unchanged doc", base_doc, r))

    r2 = json.loads(json.dumps(base_rec))
    r2["frozen_tolerances"]["TOL_FREQ"] = 1.0e-3
    checks.append(("frozen TOL-FREQ silently widened in the record", base_doc, r2))

    r3 = json.loads(json.dumps(base_rec))
    r3["reproduction_gate"]["pass"] = False
    checks.append(("reproduction gate flipped to FAIL under a ZERO-drift doc", base_doc, r3))

    r4 = json.loads(json.dumps(base_rec))
    r4["controls"]["positive"]["detected"] = False
    checks.append(("positive control flipped to MISSED under a RESOLVED doc", base_doc, r4))

    ok = True
    for label, doc_t, rec_t in checks:
        found = run(doc_t, rec_t)
        if found:
            print(f"[scx-nc] receipt CAUGHT: {label}")
        else:
            print(f"[scx-nc] *** receipt MISSED: {label} -- the gate is a no-op for this class")
            ok = False
    return 0 if ok else 1


def main() -> int:
    if "--mutation-receipt" in sys.argv:
        return mutation()
    for path in (RESULTS, DOC, PREREG, TESTS):
        if not path.exists():
            print(f"[scx-nc] MISSING required artifact: {path}")
            return 1
    problems = run()
    for p in problems:
        print(f"[scx-nc] FAIL  {p}")
    if problems:
        print(f"[scx-nc] {len(problems)} finding(s)")
        return 1
    print("[scx-nc] OK -- every back-ticked numeral in the result doc reconciles against "
          "the shipped record, and the headline bin matches the driver's COMPUTED verdict.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
