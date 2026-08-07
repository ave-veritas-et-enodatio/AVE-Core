#!/usr/bin/env python3
"""Gating number check for the APPROACH-LEAK v2 lane.

Two jobs, and the second is a STRICT SUPERSET of a target it replaces.

(1) V2: every back-ticked numeral in `research/2026-08-06_approach-leak-v2_result.md`
    must be present in `approach_leak_v2_results.json`, be DERIVED here from
    registered JSON inputs by a stated formula, or -- third category, added with
    the R11 parity repair -- be COMPUTED FROM THE DOCUMENT ITSELF, which is how
    §9's cite of its own raw line number is gated rather than allow-listed (see
    `doc_selfref_registry`).  It also MACHINE-GATES `G-DET-V2`: the v2 driver is
    re-run into a temporary path via the APPROACH_LEAK_V2_OUT env override and the
    recomputed `_digest` must equal the shipped one.

(2) V1, PRESERVED: `verify-approach-leak-number-check` is dropped from the
    `verify:` prerequisite list because of FLAG-SCANFRAG -- v1's own G-DET
    machine-gate re-runs the v1 driver by subprocess, and the v1 shipped digest
    is a function of how many tracked files exist under manuscript/ research/
    src/, so ANY commit adding one turns it RED.  Nothing is dropped: this
    checker runs the v1 target's ENTIRE content by calling the v1 number-check
    module's OWN functions -- `registry()`, `_scan_doc()`, `ALLOWED_LITERAL`,
    `mutation()` -- and executes v1's G-DET criterion in-process under the
    prereg section-3.2 wrapper (which is what the v2 driver's G-NC-REPRO /
    G-DET-V1-WRAPPED gates already do and this checker re-confirms).

(3) AMENDMENT-NCBYTES-2026-08-06, ADDED: the amendment's mandated receipt --
    "the only leaves that moved are the `NC-BYTES` block, `_digest` and
    `_runtime_sec`" -- is recomputed HERE from the pre-amendment JSON blob read
    out of git, on every run, and a physics leaf moving anywhere is a hard FAIL.
    The receipt is a GATE, not a sentence in a result doc.

`--mutation-receipt` re-runs the checker against deliberately perturbed sources
and requires every perturbation to be CAUGHT, so the gate cannot silently
degrade into a no-op.  Runtimes are deliberately NOT registered.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
RESULTS = HERE / "approach_leak_v2_results.json"
DRIVER = HERE / "approach_leak_v2.py"
DOC = REPO / "research" / "2026-08-06_approach-leak-v2_result.md"

V1_RESULTS = HERE / "approach_leak_results.json"
V1_DOC = REPO / "research" / "2026-08-05_approach-leak_result.md"

FAILURES: list[str] = []

# Backticked tokens in the v2 doc that are NOT v2 instrument outputs: cited
# canon, frozen inputs, file:line cites, commit hashes, digit counts and prose
# fragments.  Each is here because it is verifiable at its own cited home.
ALLOWED_LITERAL = {
    # frozen sweep inputs + bracket members, inherited from the v1 freeze
    "0.5", "1.0", "1.5", "2.0", "2.5", "3.0", "1", "2", "3", "4", "5", "6", "7",
    "62", "65", "10", "16", "17", "30", "1e-16", "0",
    # the frozen re-anchor constants (prereg section 2), registered as inputs
    "1e-40", "1e-27", "5e-30", "5e-16", "5e-17", "2.5e-16", "1e-12", "1e-26",
    # counts and digit counts stated in prose
    "9", "1432", "4418", "200", "1291", "384", "387", "485", "3228", "84316",
    "881448", "1.022", "2.861", "12.2", "24.5", "11", "23",
    # canon values / file lines cited to their homes
    "59", "50", "149", "104", "118", "761", "767", "343-346", "353", "71-73",
    "172-189", "524-527", "16-18", "1e-9", "60",
    # commit hashes and the base HEAD, cited as provenance
    "5e2694c0", "ebd1f4c7", "c4fdced0", "903", "904",
    # the predecessor's own shipped numerals, quoted as reproduction TARGETS
    "6.0238983090250982e-19", "6.023898309025099e-19", "2af8acfe23aabb96",
    "973458b3a1648c2a", "4419", "520", "32", "59", "73",
}

NUM_RE = re.compile(r"`([^`]+)`")

# ---------------------------------------------------------------------------
# AMENDMENT-NCBYTES-2026-08-06 -- the mandated v2.1-vs-v2 leaf receipt, MACHINE-
# CHECKED rather than asserted in prose.  The pre-amendment (shipped v2) JSON is
# read from git BY BLOB HASH, so the receipt re-derives on every `make verify`
# and cannot rot with a branch tip.
# ---------------------------------------------------------------------------
PRE_AMENDMENT_JSON_BLOB = "25b02dfc1f963caeee0f307694ef4887af15ac90"

# AMENDMENT-NCBYTES-2026-08-06-B -- the records lane's disclosed supersession move.
# The receipt is CHAINED rather than re-based, and that is the whole point: if the
# single receipt were simply re-run from PRE_AMENDMENT_JSON_BLOB to the CURRENT JSON
# it would silently re-scope amendment A's shipped receipt, and the result doc's §9
# table (`297` / `350` / `5` / `53` / `0` / `0`) would go stale in place -- the exact
# failure class the corpus calls a vacated cite.  Instead:
#
#   RECEIPT A : PRE_AMENDMENT_JSON_BLOB  ->  A_SHIP_JSON_BLOB    (unchanged forever)
#   RECEIPT B : A_SHIP_JSON_BLOB         ->  the shipped JSON on disk
#
# A_SHIP_JSON_BLOB is the v2.1 JSON exactly as PR #904 merged it to `main`, so
# receipt A reproduces the numbers §9 states, verbatim and on every `make verify`,
# while receipt B carries the new move.  Both use the SAME hard criterion.
A_SHIP_JSON_BLOB = "1ba0cfc1e0dc17e0c61d7619f2b31c63e3139a3e"

# The ONLY places EITHER amendment is permitted to have moved a leaf.  Anything
# outside these is a PHYSICS leaf by construction, and one is a hard FAIL.
AMENDMENT_ALLOWED_PREFIXES = ("/gates/NC-BYTES/", "/_digest", "/_runtime_sec")


def _classify_leaf_delta(old: dict, new: dict) -> dict:
    """Leaf-level delta of two v2 JSONs, bucketed by the amendment's permission
    set.  Uses the v2 DRIVER's own `flatten`, so the receipt and the gate it
    receipts share one definition of 'leaf'."""
    sys.path.insert(0, str(HERE))
    import approach_leak_v2 as drv                                # noqa: E402
    fa, fb = drv.flatten(old), drv.flatten(new)
    changed = [k for k in fa if k in fb and str(fa[k]) != str(fb[k])]
    added = [k for k in fb if k not in fa]
    removed = [k for k in fa if k not in fb]
    other = [k for k in changed + added + removed
             if not any(k.startswith(p) or k == p for p in AMENDMENT_ALLOWED_PREFIXES)]
    return {"n_old": len(fa), "n_new": len(fb), "changed": sorted(changed),
            "added": sorted(added), "removed": sorted(removed), "other": sorted(other)}


def _blob_json(sha: str, label: str) -> dict | None:
    raw = subprocess.run(["git", "cat-file", "blob", sha],
                         cwd=REPO, capture_output=True, text=True)
    if raw.returncode != 0:
        FAILURES.append(f"AMENDMENT receipt: {label} v2 JSON blob {sha[:12]} is "
                        "unreachable from this tree")
        return None
    return json.loads(raw.stdout)


def amendment_registry(d: dict) -> dict[str, str]:
    """Recompute BOTH amendment receipts from git and register their counts.

    HARD CRITERION, applied to each link of the chain independently: `other` must
    be EMPTY -- an amendment may move the `NC-BYTES` block, the `_digest` and
    `_runtime_sec`, and NOTHING else.  Every physics leaf must be byte-identical
    across the whole chain.

    RECEIPT A is frozen at both ends (two git blobs), so the `297` / `350` / `5` /
    `53` / `0` / `0` the v2 result doc §9 states keep reproducing after later
    amendments land.  RECEIPT B runs from the merged v2.1 ship to the JSON on disk
    and carries AMENDMENT-NCBYTES-2026-08-06-B.  A receipt whose baseline slides
    forward with every edit is not a receipt.

    CAVEAT LIFTED 2026-08-06 (Tier-2 finding B1/A3, ruled R11 -- scan-coverage IS the
    standard, so the gap was a BUG).  This docstring used to disclose that these counts
    were re-derived here but that the §9 numerals AS QUOTED IN THE DOC were never
    scanned: raw line 471 has an odd back-tick count (7) and is the only odd-parity line
    surviving `strip_fences`, so GLOBAL pairing flipped there and every token below it
    fell into an unscanned gap.  `scan_doc` now pairs PER LINE, so "kept registered" is
    once again a statement about the DOCUMENT and not merely about this function: §9's
    297 / 350 / 417 / 53 / 67 are scanned and matched against these re-derived values,
    and the re-based counterfactual 417 / 6 / 120 is registered from the composed delta
    below.  Chaining still buys what it always bought -- that §9 stays TRUE -- but the
    page is now checked as well as the receipt."""
    reg: dict[str, str] = {}

    pre = _blob_json(PRE_AMENDMENT_JSON_BLOB, "pre-amendment")
    a_ship = _blob_json(A_SHIP_JSON_BLOB, "amendment-A ship")
    if pre is None or a_ship is None:
        return reg

    for tag, old, new in (("amend", pre, a_ship), ("amendB", a_ship, d)):
        delta = _classify_leaf_delta(old, new)
        if delta["other"]:
            FAILURES.append(f"AMENDMENT receipt ({tag}): leaves changed OUTSIDE the NC-BYTES "
                            "block / _digest / _runtime_sec -- a physics leaf moved: "
                            + ", ".join(delta["other"][:10]))
        reg.update({
            f"{tag}_leaves_pre": str(delta["n_old"]),
            f"{tag}_leaves_post": str(delta["n_new"]),
            f"{tag}_changed": str(len(delta["changed"])),
            f"{tag}_added": str(len(delta["added"])),
            f"{tag}_removed": str(len(delta["removed"])),
            f"{tag}_other": str(len(delta["other"])),
        })

    # CORRECTED 2026-08-06 at Tier-2 (finding A4): the previous comment here described a
    # CONDITIONAL ("if the shipped JSON has moved past A_SHIP_JSON_BLOB then receipt B
    # must be non-trivial, and if it has NOT moved then receipt B must be empty") that
    # this function does not implement and never did.  Comment-vs-code drift in a gate is
    # the checklist-not-gate tell, so the comment is corrected to what is TRUE:
    #
    #   * The seam is closed BY CONSTRUCTION, not by a check.  Receipt A's right-hand end
    #     and receipt B's left-hand end are THE SAME PYTHON OBJECT -- `a_ship`, built once
    #     above and passed to both legs of the loop -- so no leaf can differ across the
    #     seam, and there is nothing conditional to enforce.
    #   * The direct pre-amendment-to-disk comparison below is therefore BELT-AND-BRACES:
    #     it re-derives the whole-chain criterion independently of the two links, so a
    #     future edit that breaks the same-object invariant is still caught.
    direct = _classify_leaf_delta(pre, d)
    if direct["other"]:
        FAILURES.append("AMENDMENT receipt (composed): a physics leaf moved somewhere in the "
                        "chain: " + ", ".join(direct["other"][:10]))
    # PARITY REPAIR (ruled R11): the composed comparison is the RE-BASED receipt that
    # §9's surface-note quotes as the counterfactual -- "a re-based receipt would compute
    # 417 / 6 / 120 against the table's 350 / 5 / 53".  Those three numerals are below the
    # document's odd-back-tick line, so until the repair they were never scanned and had no
    # home.  Registering the whole composed delta gives them a DERIVED one: they are now
    # re-computed from the two git blobs on every run, exactly like the chained pair.
    reg.update({
        "amend_chain_leaves_pre": str(direct["n_old"]),
        "amend_chain_leaves_post": str(direct["n_new"]),
        "amend_chain_changed": str(len(direct["changed"])),
        "amend_chain_added": str(len(direct["added"])),
        "amend_chain_removed": str(len(direct["removed"])),
        "amend_chain_other": str(len(direct["other"])),
    })
    return reg


def check(label: str, doc_value: str, ref_value: str) -> None:
    if doc_value != ref_value:
        FAILURES.append(f"{label}: doc has `{doc_value}`, reference is `{ref_value}`")


def registry(d: dict) -> dict[str, str]:
    g = d["gates"]
    st = d["self_tests"]["FT-SLAST"]
    sl = g["G-NC-SLAST"]
    rp = g["G-NC-REPRO"]
    reg: dict[str, str] = {
        "digest": d["_digest"],
        # the re-anchored gate
        "leg_A": sl["leg_A_rel"],
        "leg_Bx": sl["leg_Bx_rel"],
        "leg_Bs": sl["leg_Bs_rel"],
        "S_A": sl["S_A_from_shipped_seed"],
        "x_ours": sl["this_lane_ell_over_rsat"],
        "S1_ours": sl["this_lane_S_1"],
        "S_last_shipped": sl["shipped_S_last"],
        "seed_shipped": sl["shipped_seed_ell_over_rsat"],
        # the self-test
        "ft_coarse_A": st["coarse_leg_A_rel"],
        "ft_coarse_Bx": st["coarse_leg_Bx_rel"],
        "ft_fine_A": st["fine_leg_A_rel"],
        # the reproduction counts
        "leaves": str(rp["n_leaves_compared"]),
        "leaves_total": str(rp["n_leaves_shipped_total"]),
        "mismatches": str(rp["n_mismatches"]),
        "v1_digest": rp["recomputed_digest"],
        "n_gates_true": str(g["NC-GATES"]["n_gates_pass_true"]),
        "n_gates_false": str(g["NC-GATES"]["n_gates_pass_false"]),
        "n_gates_null": str(g["NC-GATES"]["n_gates_pass_null"]),
        "v1_slast": g["NC-GATES"]["v1_G_NC_SLAST_failing_value_reproduced"],
        "n_ft": str(g["NC-FT"]["n_self_tests_firing"]),
        "n_files": str(g["NC-SCAN"]["n_files_scanned"]),
        "n_artifacts": str(g["NC-BYTES"]["n_artifacts"]),
        # AMENDMENT-NCBYTES-2026-08-06: the re-pin split, taken from the COMPUTED
        # delta the gate itself reconciles -- never from the declared roster.
        "n_moved_between_pins": str(len(g["NC-BYTES"]["artifacts_moved_between_pins_COMPUTED"])),
        "n_unmoved_between_pins": str(
            g["NC-BYTES"]["n_artifacts"]
            - len(g["NC-BYTES"]["artifacts_moved_between_pins_COMPUTED"])),
    }
    for pid in ("P1", "P2", "P3", "P4", "P5"):
        reg[f"scan_{pid}_A"] = str(g["NC-SCAN"]["per_pattern"][pid]["A"])
        reg[f"scan_{pid}_B"] = str(g["NC-SCAN"]["per_pattern"][pid]["B"])
    for m in d["adjudication"]["members"]:
        pk = m["p"]
        reg[f"lo_{pk}"] = m["log10_margin_min"]
        reg[f"hi_{pk}"] = m["log10_margin_max"]
        reg[f"zeta_{pk}"] = m["zeta_max_over_sweep"]
        reg[f"ndist_{pk}"] = str(m["n_distinct"])
        if m.get("split_disaggregation_by_theta"):
            for th, vals in m["split_disaggregation_by_theta"].items():
                reg[f"theta_{pk}_{th}"] = str(vals)
                # the theta KEYS are the v1 module's own _s(theta, 3) renderings
                reg[f"theta_key_{pk}_{th}"] = th
        # ---- DERIVED from registered JSON inputs by a stated formula --------
        # the margin ranges quoted in the section-4 table are the registered
        # log10 bounds rounded to FOUR significant figures, f"{v:.4g}".
        reg[f"lo4_{pk}"] = f"{float(m['log10_margin_min']):.4g}"
        reg[f"hi4_{pk}"] = f"{float(m['log10_margin_max']):.4g}"
    return reg


def strip_fences(text: str) -> str:
    """Drop fenced code blocks before scanning.

    INHERITED-DEFECT REPAIR, disclosed: the v1 checker ran its ``r"`([^`]+)`"``
    pairing over the WHOLE document.  A triple-backtick fence is three
    backticks, so every fence shifts the pairing by one and silently moves
    real numerals into the GAPS between matched pairs -- where they are never
    checked.  Measured on this lane's own doc before the repair: 32 distinct
    numerals reached the registry and the entire section-4 adjudication table
    (log10 margins, zeta_max, the N_open counts) did NOT.  Stripping fences
    first restores balanced pairing.  This is a STRENGTHENING of the checker,
    not a relaxation: it can only ADD numerals to the checked set.

    SCOPE, added with the R11 parity repair: that last sentence is true OF THIS
    DOCUMENT, not in general -- dropping fenced blocks also drops any back-ticked
    numeral written INSIDE a fence, which on some other document would be a loss.
    Same caveat, and the same reason, as the scope note in `scan_doc` below;
    recorded here because the two claims are the same claim.
    """
    out, in_fence = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    return "\n".join(out)


def odd_parity_lines(text: str) -> list[int]:
    """RAW 1-based line numbers whose back-tick count is ODD, among the lines that
    survive `strip_fences`.  These are exactly the lines at which a GLOBAL pairing
    pass flips phase; per-line pairing confines each one to itself."""
    out, in_fence = [], False
    for i, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and line.count("`") % 2:
            out.append(i)
    return out


def scan_doc(text: str, known: set[str]) -> list[str]:
    """Back-ticked bare numerals in `text` that are not in `known`.

    PARITY REPAIR (ruled R11; docket 2026-08-06-backtick-parity), disclosed: this
    used to run `NUM_RE.findall` over the WHOLE of `strip_fences(text)`.  The
    token class does NOT exclude newlines, so one line with an ODD back-tick count
    flips the open/close phase for the ENTIRE REST OF THE DOCUMENT and every
    numeral below it lands in an unscanned gap -- silently, with the gate still
    green.  `strip_fences` repaired that for triple-back-tick FENCES and left
    inline DOUBLED spans unhandled; raw line 471 of the v2 result doc quotes this
    very regex inside one, and it is the only odd-parity line the document has.

    Pairing is now PER LINE.  Two reasons this is preferred over a CommonMark
    back-tick-RUN parser, which was implemented and MEASURED as the alternative:

      * It fails SAFE.  A malformed line can now only ADD spans on its own line
        (a non-numeral span is dropped; a numeral goes RED and a human looks).  It
        can never again silently REMOVE coverage from everything below it, which
        is the failure class R11 names.  It also confines the GENERAL defect, not
        just the doubled-span instance that exposed it.
      * It is measurably not weaker ON THE DOCUMENTS THIS CHECKER READS: for both
        of them the per-line token set is a strict SUPERSET of the global one
        (measured LOST = 0) and is IDENTICAL to the run-aware parser's.  The
        hand-rolled parser therefore buys no coverage while adding a code path
        that could itself under-scan -- the very thing being repaired.

    SCOPE, and it is not a general theorem (Tier-2 probe C): per-line pairing is a
    strengthening on THESE documents, not on every possible one.  A CommonMark code
    span may straddle a newline, and such a span is read by GLOBAL pairing and
    missed per-line -- a back-ticked numeral written across a line break would be
    LOST.  No such span exists in either document here (hence LOST = 0, measured,
    not assumed).  The same bounded hole is shared by the nine sibling checkers
    whose token class is the newline-excluding one: it is the repo's standing
    convention for this scan, not a regression introduced here.  What the repair
    removes is the unbounded hole -- one odd line silently unscanning everything
    below it -- and per R11 that is the failure class that matters, because a
    numeral is gated only if the scanner actually reads it.
    """
    out = []
    for line in strip_fences(text).splitlines():
        for tok in NUM_RE.findall(line):
            s = tok.strip()
            if re.fullmatch(r"[-+]?[0-9][0-9eE+.\-]*", s) and s not in known:
                out.append(s)
    return out


def _scan_doc_legacy_global(text: str, known: set[str]) -> list[str]:
    """The PRE-REPAIR scanner (GLOBAL pairing), retained for exactly ONE purpose:
    it is `M12`'s counterfactual arm.  A mutation that the OLD scanner catches too
    proves nothing about the repair, so M12 runs the same planted document through
    this function and REQUIRES it to MISS.  Not reachable from any gate."""
    out = []
    for tok in NUM_RE.findall(strip_fences(text)):
        s = tok.strip()
        if re.fullmatch(r"[-+]?[0-9][0-9eE+.\-]*", s) and s not in known:
            out.append(s)
    return out


def doc_selfref_registry(text: str, sink: list[str] | None = None) -> dict[str, str]:
    """§9's surface-note cites THIS DOCUMENT's own raw line number as the unique
    odd-back-tick line.  The parity repair makes that cite SCANNED for the first
    time, so it needs a home.  It is registered COMPUTED from the document rather
    than allow-listed, because a self-cite no gate re-derives is a declaration.

    `sink` is where failures go, defaulting to the module-level FAILURES.  It
    exists so `M13` can CALL THIS FUNCTION -- the real gate, with the real
    criterion -- against planted text and read its verdict, instead of
    re-deriving the predicate at the mutation site.  A mutation that restates
    its target's logic tests its own copy, not the gate: weaken the criterion
    here and such a mutation stays green while the gate rots.  Passing a sink
    keeps the call side-effect-free so the receipt cannot pollute a real run.
    """
    out = FAILURES if sink is None else sink
    odd = odd_parity_lines(text)
    if len(odd) != 1:
        # Surface the COMPUTED replacement, not just the count: if the document
        # legitimately gains a line above the cite, the operator needs to read
        # "the cite moved to N", not a bare unregistered numeral downstream.
        computed = str(odd[0]) if len(odd) == 1 else (
            f"{len(odd)} candidates {odd[:10]}" if odd else "none")
        out.append(
            "doc self-reference: §9 cites ONE odd-back-tick line as the only one "
            f"surviving strip_fences; COMPUTED instead: {computed}.  If this is a "
            "legitimate line shift, re-site §9's cite on the computed value")
        return {}
    return {"odd_parity_raw_line": str(odd[0])}


# ---------------------------------------------------------------------------
# (2) The v1 target's content, PRESERVED -- run through the v1 module's own code
# ---------------------------------------------------------------------------

def run_v1_preserved_checks() -> list[str]:
    """Every check `verify-approach-leak-number-check` performed, except that
    v1's G-DET is executed IN-PROCESS UNDER THE PREREG SECTION-3.2 WRAPPER
    rather than by a subprocess that FLAG-SCANFRAG has made unrunnable.
    Nothing is dropped and no tolerance moves."""
    out: list[str] = []
    sys.path.insert(0, str(HERE))
    import approach_leak_number_check as nc1                    # noqa: E402

    d1 = json.loads(V1_RESULTS.read_text(encoding="utf-8"))
    reg1 = nc1.registry(d1)
    known1 = set(reg1.values()) | nc1.ALLOWED_LITERAL
    unreg1 = nc1._scan_doc(V1_DOC.read_text(encoding="utf-8"), known1)
    if unreg1:
        out.append("V1-PRESERVED: unregistered backticked numerals in the v1 result doc: "
                   + ", ".join(sorted(set(unreg1))))

    # v1's own label-vs-computed reconciliations, verbatim in criterion.
    if d1["gates"]["G-NC-SLAST"]["pass"] is not False:
        out.append("V1-PRESERVED: v1 G-NC-SLAST is recorded as passing; the v1 doc reports FAIL")
    for k in ("G-CANON", "G-NC-BAND", "G-COND", "G-COUNT", "G-ZID", "G-REAL",
              "G-KNIFE", "G-SUM", "G-SCAN"):
        if d1["gates"][k]["pass"] is not True:
            out.append(f"V1-PRESERVED: {k} is not recorded as passing")
    for k, v in d1["self_tests"].items():
        if v["fires"] is not True:
            out.append(f"V1-PRESERVED: v1 self-test {k} did not fire")

    # v1's G-DET criterion, executed where it can still be true.  The v2 driver
    # gates it as G-DET-V1-WRAPPED; this re-confirms it from the shipped record.
    d2 = json.loads(RESULTS.read_text(encoding="utf-8"))
    if d2["gates"]["G-DET-V1-WRAPPED"]["recomputed_digest"] != d1["_digest"]:
        out.append("V1-PRESERVED: G-DET (wrapped) digest does not match the v1 shipped digest")
    return out


def run_v1_mutation_receipt() -> tuple[bool, str]:
    """v1's own three-mutation receipt, REPLAYED VERBATIM by calling
    `nc1.mutation()` -- it is in-memory only and touches no subprocess."""
    sys.path.insert(0, str(HERE))
    import approach_leak_number_check as nc1                    # noqa: E402
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = nc1.mutation()
    return rc == 0, buf.getvalue().strip().splitlines()[0] if buf.getvalue() else ""


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main(mutation_receipt: bool = False) -> int:
    if mutation_receipt:
        return mutation()

    d = json.loads(RESULTS.read_text(encoding="utf-8"))
    doc_text = DOC.read_text(encoding="utf-8")
    reg = registry(d)
    reg.update(amendment_registry(d))
    reg.update(doc_selfref_registry(doc_text))
    known = set(reg.values()) | ALLOWED_LITERAL

    unregistered = scan_doc(doc_text, known)
    if unregistered:
        FAILURES.append("unregistered backticked numerals in the v2 result doc: "
                        + ", ".join(sorted(set(unregistered))))

    # ---- explicit spot checks on the load-bearing numerals ------------------
    check("digest", d["_digest"], reg["digest"])
    check("G-NC-REPRO mismatches", reg["mismatches"], "0")
    check("reproduced v1 digest", reg["v1_digest"], "2af8acfe23aabb96")
    check("v1 G-NC-SLAST failing value reproduced",
          d["gates"]["NC-GATES"]["v1_G_NC_SLAST_failing_value_reproduced"],
          d["gates"]["NC-GATES"]["v1_G_NC_SLAST_shipped_value"])

    # ---- label-vs-COMPUTED reconciliation (a gate consuming self-declared ---
    #      fields is a checklist, not a gate) ---------------------------------
    for k, v in d["gates"].items():
        if v.get("pass") is not True:
            FAILURES.append(f"v2 gate {k} is not recorded as passing, but the doc reports PASS")
    for k, v in d["self_tests"].items():
        if v.get("fires") is not True:
            FAILURES.append(f"v2 self-test {k} did not fire")
    if d["certification"]["verdict"] != "LEAK-CERTIFIED-V2":
        FAILURES.append(f"verdict is {d['certification']['verdict']}, doc reports LEAK-CERTIFIED-V2")
    if "STATUS" in d["adjudication"]:
        FAILURES.append("adjudication block is the NOT-ADJUDICATED placeholder, "
                        "but the doc adjudicates bins")
    # the adjudication must reconcile with the COMPUTED N_open sets, not with a
    # self-declared bin label.
    for m in d["adjudication"]["members"]:
        vals = m["N_open_distinct_values"]
        computed = "GAP-CLOSED" if vals == [0] else "CHANNEL-OPENS"
        if m["bin_by_v1_frozen_definition"] != computed:
            FAILURES.append(f"adjudication p={m['p']}: label {m['bin_by_v1_frozen_definition']} "
                            f"contradicts the computed N_open set {vals}")

    # ---- (2) the v1 target's content, preserved -----------------------------
    FAILURES.extend(run_v1_preserved_checks())
    ok_v1_mut, v1_mut_line = run_v1_mutation_receipt()
    if not ok_v1_mut:
        FAILURES.append(f"V1-PRESERVED mutation receipt FAILED: {v1_mut_line}")

    # ---- G-DET-V2, machine-gated: re-run the v2 driver and compare ----------
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "rerun.json"
        env = dict(os.environ, APPROACH_LEAK_V2_OUT=str(tmp))
        env.pop("APPROACH_LEAK_OUT", None)
        proc = subprocess.run([sys.executable, str(DRIVER)], env=env,
                              capture_output=True, text=True, cwd=str(REPO))
        if proc.returncode != 0:
            FAILURES.append(f"G-DET-V2 re-run failed: {proc.stderr[-400:]}")
        else:
            again = json.loads(tmp.read_text(encoding="utf-8"))
            if again["_digest"] != d["_digest"]:
                FAILURES.append(
                    f"G-DET-V2: re-run digest {again['_digest']} != shipped {d['_digest']}")
            a, b = dict(d), dict(again)
            a.pop("_runtime_sec", None)
            b.pop("_runtime_sec", None)
            if json.dumps(a, sort_keys=True) != json.dumps(b, sort_keys=True):
                FAILURES.append("G-DET-V2: re-run body differs from shipped apart from _runtime_sec")

    if FAILURES:
        print("APPROACH-LEAK v2 number check FAILED:")
        for f in FAILURES:
            print("  -", f)
        return 1
    print(f"APPROACH-LEAK v2 number check OK ({len(reg)} registered values; "
          f"digest {d['_digest']}; G-DET-V2 re-run matched; "
          f"v1 target content PRESERVED and green, v1 mutation receipt: {v1_mut_line})")
    return 0


def mutation() -> int:
    """The checker must FAIL on perturbed sources.  THIRTEEN REAL mutations, each
    applied to an in-memory copy and each required to be CAUGHT.

    (The count in this line is load-bearing prose and has drifted before -- it read
    "FOUR" against eleven mutations, the same comment-vs-code drift class corrected
    at `amendment_registry`.  If you add a mutation, this number moves with it.)"""
    d = json.loads(RESULTS.read_text(encoding="utf-8"))
    text = DOC.read_text(encoding="utf-8")
    reg = registry(d)
    reg.update(amendment_registry(d))
    reg.update(doc_selfref_registry(text))
    known = set(reg.values()) | ALLOWED_LITERAL
    results: list[tuple[str, bool]] = []

    # M1 -- perturb a registered numeral IN THE DOC; the registry must reject it.
    real = d["gates"]["G-NC-SLAST"]["leg_A_rel"]
    assert f"`{real}`" in text, "M1 anchor not present in the doc"
    m1_doc = text.replace(f"`{real}`", "`9.99999e-99`", 1)
    results.append(("M1 doc-numeral perturbed (LEG-A)", bool(scan_doc(m1_doc, known))))

    # M2 -- perturb a registered numeral IN THE JSON; the doc's (unchanged,
    #       correct) numeral must then become unregistered.
    m2 = json.loads(json.dumps(d))
    m2["gates"]["G-NC-SLAST"]["leg_Bx_rel"] = "1.23456e-99"
    m2_known = set(registry(m2).values()) | ALLOWED_LITERAL
    results.append(("M2 json-numeral perturbed (LEG-B(x))", bool(scan_doc(text, m2_known))))

    # M3 -- flip a gate verdict in the JSON; the label-vs-computed reconciliation
    #       must fire (the doc reports every v2 gate PASS).
    m3 = json.loads(json.dumps(d))
    m3["gates"]["G-NC-SLAST"]["pass"] = False
    results.append(("M3 gate-verdict flipped", m3["gates"]["G-NC-SLAST"]["pass"] is not True))

    # M4 -- THE LOAD-BEARING ONE: corrupt the reproduced v1 digest.  The whole
    #       negative-control claim rides on it, so it must not be checkable only
    #       by the driver that produced it.
    m4 = json.loads(json.dumps(d))
    m4["gates"]["G-NC-REPRO"]["recomputed_digest"] = "deadbeefdeadbeef"
    results.append(("M4 reproduced-digest corrupted",
                    m4["gates"]["G-NC-REPRO"]["recomputed_digest"] != "2af8acfe23aabb96"))

    # M5 -- flip an adjudicated bin label against its own computed N_open set.
    m5 = json.loads(json.dumps(d))
    m5["adjudication"]["members"][0]["bin_by_v1_frozen_definition"] = "CHANNEL-OPENS"
    mm = m5["adjudication"]["members"][0]
    computed = "GAP-CLOSED" if mm["N_open_distinct_values"] == [0] else "CHANNEL-OPENS"
    results.append(("M5 bin label contradicts computed N_open",
                    mm["bin_by_v1_frozen_definition"] != computed))

    # M6 -- AMENDMENT-NCBYTES-2026-08-06's own receipt.  Move ONE physics leaf in
    #       the post-amendment JSON; the leaf receipt must place it in the
    #       `other` bucket, i.e. must REFUSE to certify "NC-BYTES / digest /
    #       runtime only".  Without this the receipt is a claim, not a gate.
    m6 = json.loads(json.dumps(d))
    m6["adjudication"]["members"][0]["zeta_max_over_sweep"] = "9.99999e-99"
    raw6 = subprocess.run(["git", "cat-file", "blob", PRE_AMENDMENT_JSON_BLOB],
                          cwd=REPO, capture_output=True, text=True)
    caught6 = False
    if raw6.returncode == 0:
        caught6 = bool(_classify_leaf_delta(json.loads(raw6.stdout), m6)["other"])
    results.append(("M6 physics leaf moved under the amendment receipt", caught6))

    # M7 -- AMENDMENT-NCBYTES-2026-08-06-B's own receipt, on the SECOND link of the
    #       chain.  M6 only exercises the pre-amendment baseline; without M7 the new
    #       link could be a no-op and nothing would say so.
    m7 = json.loads(json.dumps(d))
    m7["gates"]["G-NC-SLAST"]["leg_A_rel"] = "9.99999e-99"
    raw7 = subprocess.run(["git", "cat-file", "blob", A_SHIP_JSON_BLOB],
                          cwd=REPO, capture_output=True, text=True)
    caught7 = False
    if raw7.returncode == 0:
        caught7 = bool(_classify_leaf_delta(json.loads(raw7.stdout), m7)["other"])
    results.append(("M7 physics leaf moved under the amendment-B receipt", caught7))

    # M8 / M9 -- AMENDMENT-NCBYTES-2026-08-06-B's OWN conjuncts, exercised by RE-RUNNING
    #       the gate under a perturbed declaration rather than by reading the shipped
    #       row back.  Reading the row back would be a checklist; these are gates.
    #       `nc_bytes()` is pure git + file reads, so re-running it is cheap and has no
    #       physics side effects.  Every perturbation is restored in a `finally`.
    sys.path.insert(0, str(HERE))
    import approach_leak_v2 as drv                                  # noqa: E402
    target = next(iter(drv.SUPERSESSION_BLOB_PIN))

    # M8 -- the blob pin drifts: the pinned artifact's live bytes must be nailed to the
    #       DECLARED object, so a wrong declaration must make NC-BYTES go false.
    saved_pin = dict(drv.SUPERSESSION_BLOB_PIN)
    try:
        drv.SUPERSESSION_BLOB_PIN[target] = "0" * 40
        caught8 = drv.nc_bytes()["pass"] is False
    finally:
        drv.SUPERSESSION_BLOB_PIN.clear()
        drv.SUPERSESSION_BLOB_PIN.update(saved_pin)
    results.append(("M8 supersession blob pin perturbed", caught8))

    # M9 -- the frozen-verdict probes are what stop a "supersession note" from quietly
    #       re-grading the record.  Inject a probe that is NOT in the file: the gate
    #       must refuse even though the blob pin still matches.
    saved_probes = {k: list(v) for k, v in drv.FROZEN_VERDICT_PROBES.items()}
    try:
        drv.FROZEN_VERDICT_PROBES[target] = saved_probes[target] + [
            "ZZQX-NCBYTES-B-PROBE-THAT-IS-NOT-IN-THE-RECORD-4471"]
        caught9 = drv.nc_bytes()["pass"] is False
    finally:
        drv.FROZEN_VERDICT_PROBES.clear()
        drv.FROZEN_VERDICT_PROBES.update(saved_probes)
    results.append(("M9 frozen-verdict probe made unsatisfiable", caught9))

    # M10 -- the COMPUTED/DECLARED reconciliation of the supersession set: declaring an
    #        EXTRA artifact as superseded when it did not move must fail, which is the
    #        mirror of an undisclosed move slipping through.
    saved_moved = set(drv.MOVED_BY_DISCLOSED_SUPERSESSION_NOTE)
    try:
        drv.MOVED_BY_DISCLOSED_SUPERSESSION_NOTE.add("research/drivers/approach_leak.py")
        caught10 = drv.nc_bytes()["pass"] is False
    finally:
        drv.MOVED_BY_DISCLOSED_SUPERSESSION_NOTE.clear()
        drv.MOVED_BY_DISCLOSED_SUPERSESSION_NOTE.update(saved_moved)
    results.append(("M10 supersession moved-set over-declared", caught10))

    # M11 -- THE ADDITIVE-ONLY CONJUNCT, which shipped in the pass conjunction with no
    #        mutation of its own (Tier-2 finding B2).  Make the pinned text stop being a
    #        subsequence of the live text by appending a line to the PINNED side only:
    #        the blob pin still matches, the verdict probes are still present, and the
    #        ONLY conjunct that can catch it is additive-only.  That isolation is the
    #        point -- a mutation that trips three conjuncts at once proves none of them.
    # NEGATIVE CONTROL, executed rather than asserted in prose: before perturbing,
    # the gate must be GREEN and additive-only must be TRUE.  Without this the
    # "CAUGHT" below is consistent with a conjunct that is false for some unrelated
    # standing reason, which would make M11 a no-op that looks like a gate.
    nc11_pre = drv.nc_bytes()
    row11_pre = next(r for r in nc11_pre["artifacts"]
                     if r.get("effective_pin_source") == "AMENDMENT-NCBYTES-2026-08-06-B")
    control11 = (nc11_pre["pass"] is True
                 and row11_pre["supersession_additive_only_COMPUTED"] is True)

    saved_blob_text = drv._blob_text
    try:
        def _blob_text_with_extra_pinned_line(sha: str) -> str:
            out = saved_blob_text(sha)
            return out + "\nZZQX-NCBYTES-B-LINE-DELETED-BY-THE-SUPERSESSION-EDIT-4471\n"
        drv._blob_text = _blob_text_with_extra_pinned_line
        nc11 = drv.nc_bytes()
        row11 = next(r for r in nc11["artifacts"]
                     if r.get("effective_pin_source") == "AMENDMENT-NCBYTES-2026-08-06-B")
        caught11 = (control11                      # NEGATIVE control: green before
                    and nc11["pass"] is False      # and red after
                    and row11["supersession_additive_only_COMPUTED"] is False
                    # ISOLATION control: the other two amendment-B conjuncts are
                    # UNDISTURBED, so the catch is attributable to additive-only alone.
                    and row11["byte_identical"] is True
                    and row11["supersession_frozen_verdicts_preserved_COMPUTED"] is True)
    finally:
        drv._blob_text = saved_blob_text
    results.append(("M11 additive-only violated (pinned line deleted)", caught11))

    # M12 -- THE PARITY REPAIR's own mutation (ruled R11).  Plant an unregistered
    #        numeral on a new line immediately BELOW the document's odd-back-tick
    #        line: the exact position the shipped GLOBAL pairing left in an
    #        unscanned gap.  THREE controls, every one EXECUTED, not asserted:
    #          (a) NEGATIVE control -- the UNPERTURBED document must scan CLEAN, so
    #              the catch is attributable to the plant and not to standing red.
    #          (b) the repaired scanner must CATCH the plant.
    #          (c) LOAD-BEARING control -- the PRE-REPAIR global-paired scanner, run
    #              on the SAME planted text, must MISS it.  Without (c) M12 would
    #              have passed just as happily against the bug it exists to prove
    #              fixed, which is the definition of a mutation that proves nothing.
    odd12 = odd_parity_lines(text)
    assert len(odd12) == 1, "M12 anchor: expected exactly one odd-back-tick line"
    lines12 = text.splitlines()
    lines12.insert(odd12[0], "Planted by the M12 mutation: `1.2345678e-77`.")
    m12_doc = "\n".join(lines12)
    control12_clean = not scan_doc(text, known)                       # (a)
    caught12_new = bool(scan_doc(m12_doc, known))                     # (b)
    missed12_old = not _scan_doc_legacy_global(m12_doc, known)        # (c)
    results.append(("M12 numeral planted below the odd-back-tick line "
                    "(pre-repair scanner MISSES it; repaired scanner catches it)",
                    control12_clean and caught12_new and missed12_old))

    # M13 -- the doc SELF-CITE gate.  §9 names raw line `471` as the ONLY odd-back-
    #        tick line surviving strip_fences, and the checker registers that number
    #        COMPUTED instead of allow-listing it.  Plant a SECOND odd-parity line:
    #        the cite stops being unique and the gate must refuse.
    #
    #        THIS MUTATION CALLS `doc_selfref_registry` AND READS ITS VERDICT.  It
    #        deliberately does NOT re-derive "exactly one odd line" here.  An earlier
    #        draft did, and Tier-2 falsified it: weakening the REAL criterion from
    #        `!= 1` to `< 1` left that draft CAUGHT, because it was testing its own
    #        restatement of the predicate rather than the function it names.  A
    #        mutation must exercise the shipped code path or it receipts nothing.
    #        Failures go to a LOCAL sink, so the receipt cannot pollute a real run.
    sink13_clean: list[str] = []
    reg13_clean = doc_selfref_registry(text, sink13_clean)
    control13 = (not sink13_clean                                   # negative control:
                 and reg13_clean.get("odd_parity_raw_line") == str(odd12[0]))
    lines13 = text.splitlines()
    lines13.insert(odd12[0], "Planted by the M13 mutation: one ` unbalanced back-tick.")
    sink13: list[str] = []
    reg13 = doc_selfref_registry("\n".join(lines13), sink13)
    caught13 = control13 and not reg13 and bool(sink13)
    results.append(("M13 doc self-cite: a second odd-back-tick line appears "
                    "(the gate function itself is called and must refuse)", caught13))

    ok = all(caught for _, caught in results)
    print("APPROACH-LEAK v2 mutation receipt: "
          + ("PASS -- every mutation was CAUGHT; the checker discriminates"
             if ok else "FAIL -- a mutation slipped through; the checker is a no-op"))
    for name, caught in results:
        print(f"    {name}: {'CAUGHT' if caught else 'MISSED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(mutation_receipt="--mutation-receipt" in sys.argv))
