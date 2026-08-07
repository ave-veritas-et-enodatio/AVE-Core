#!/usr/bin/env python3
"""APPROACH-LEAK v2 driver -- ONE negative-control tolerance re-anchored SEED-AWARE.

Frozen pre-registration: research/2026-08-06_approach-leak-v2_prereg-FROZEN.md
(commit ebd1f4c7, pushed with no code and one disclosed build-wiring line).

WHAT THIS DOES, AND WHAT IT DELIBERATELY DOES NOT DO
----------------------------------------------------
It does NOT re-implement one line of the v1 physics.  It imports the v1 driver
module and calls the v1 module's own `main()`; every physics number it reports
is a string REPRODUCED from that run and compared to the shipped v1 JSON by
`==`.  The only thing computed afresh here is the RE-ANCHORED negative control
G-NC-SLAST and its fireability self-test FT-SLAST -- and even those are
evaluated through the v1 module's own `S2_exact`, `r_sat`, `L_NODE`.

THE RE-ANCHOR (prereg section 2), in one sentence: a reproduction gate's
tolerance is bounded by the precision at which the SOURCE SHIPPED its
comparand, not by the precision at which the CONSUMER computes.

  LEG-A  seed-exact   : recompute S_last from the predecessor's OWN shipped
                        rung through the identical cancellation-free form.
                        Bound 5e-30 (half a unit in the 30th significant digit
                        of an mp.nstr(x, 30) rendering).  TOLERANCE 1e-27.
  LEG-B  seed-bounded : this lane's mass-derived ell/r_sat and S_1 vs the
                        shipped strings.  Bound 5e-17 (half a unit in the 17th
                        significant digit of the shipped rung) x a DECLARED 10x
                        safety factor for the unauditable upstream chain.
                        TOLERANCE 5e-16 on both.

THE ONE DECLARED INTERVENTION (prereg section 3.2): `v1._tracked_files` is
wrapped to additionally drop THIS lane's six artifacts, restoring the v1 scan
surface exactly.  It is itself GATED: n_files_scanned must reproduce as 4418.

DISCIPLINE
----------
* Engine `src/ave` byte-untouched and never imported (the v1 module reads
  constants.py by an `ast` literal parse, and that is inherited, not changed).
* mpmath dps = 60, obtained by importing the v1 module's own `mp` configuration.
* No iterated map: closed forms evaluated once, or strings reproduced.
* Every predecessor artifact is READ-ONLY and byte-gated (NC-BYTES).
"""

from __future__ import annotations

import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile
import time
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
OUT = Path(os.environ.get("APPROACH_LEAK_V2_OUT", str(HERE / "approach_leak_v2_results.json")))

V1_JSON = HERE / "approach_leak_results.json"
LASTBOND_JSON = HERE / "last_bond_kernel_collapse_results.json"

# The v1 ship commit, as originally frozen (prereg section 3.3).  RETAINED as the
# audit anchor; since AMENDMENT-NCBYTES-2026-08-06 it is no longer the comparison
# target -- it is recorded per artifact so the delta stays visible.
V1_SHIP_COMMIT = "5e2694c0"

# AMENDMENT-NCBYTES-2026-08-06 (disclosed pre-merge; result doc section 9 and
# _orchestration/docket-entries/2026-08-06-approach-leak-v2-correction.md).
# NC-BYTES now pins ALL TEN read-only artifacts at the REPAIRED v1 tip.  Rationale,
# in one sentence: the gate's PURPOSE is "this lane wrote none of the
# predecessors", and two of the ten were rewritten between the two commits by the
# ORCHESTRATOR's disclosed post-ship SCANFRAG repair -- an event extrinsic to this
# lane, which the un-amended pin cannot express and therefore misreports as a
# lane-authored write.
V1_PIN_COMMIT = "f3607be8"

# The artifacts that moved between V1_SHIP_COMMIT and V1_PIN_COMMIT.  DECLARED
# here and RECONCILED against the computed delta inside nc_bytes(): a gate that
# consumes its own declaration is a checklist, not a gate.
REPAIRED_BY_DISCLOSED_ORCHESTRATOR_REPAIR = {
    "research/2026-08-05_approach-leak_result.md",
    "research/drivers/approach_leak.py",
}

# AMENDMENT-NCBYTES-2026-08-06-B (disclosed pre-merge; docket fragment
# _orchestration/docket-entries/2026-08-06-g-rho2-supersession.md).  A SECOND
# extrinsic, disclosed move of ONE read-only artifact -- and this one is not a
# repair, it is a records edit.
#
# WHAT HAPPENED, in one sentence: the frozen v1 kernel-collapse result document
# records `G-RHO2` as FAIL, the rerun that document's own section 1.3 NAMED has since
# landed ROW-CERTIFIED (PR #902, merge commit b06cbeb1), and the records lane added
# the dated supersession pointer the corpus's freeze discipline requires -- so the
# artifact's live blob no longer equals its blob at V1_PIN_COMMIT.
#
# WHY THE PIN MOVES RATHER THAN THE GATE RELAXING: the gate's purpose is "no
# predecessor artifact drifted un-disclosed".  A per-artifact BLOB pin (not a commit
# pin) expresses exactly that for an artifact whose move is authored HERE: the move is
# nailed to one 40-hex object, so any FURTHER edit -- by this lane or anyone -- fails.
# A commit pin cannot be used because the commit that carries the move does not exist
# until this lane commits, which would make the gate un-runnable pre-commit.
SUPERSESSION_BLOB_PIN = {
    "research/2026-08-05_last-bond-kernel-collapse_result.md":
        "95a7dae4d7fa7794a4bb22c0c03b08af1268bded",
}

# The DECLARED moved-set for amendment B, reconciled below against the COMPUTED one.
MOVED_BY_DISCLOSED_SUPERSESSION_NOTE = set(SUPERSESSION_BLOB_PIN)

# The v1 record's OWN verdict text, which the supersession note may not soften.  These
# are byte-exact substrings of the artifact as pinned; the gate requires every one of
# them to still be present in the LIVE file.  A "supersession note" that quietly
# re-graded the frozen FAIL would fail here even though the blob pin still matched,
# because the blob pin only says WHICH bytes, never WHICH CLAIM.
FROZEN_VERDICT_PROBES = {
    "research/2026-08-05_last-bond-kernel-collapse_result.md": [
        "**TASK 2 is `ROW-NOT-CERTIFIED`.** `G-RHO2` FAILS on an injection point this "
        "lane sized wrong at freeze.",
        "| **G-RHO2** ✗ | 2 | fitted exponent of `\\|dΓ/dZ_beyond\\|` vs `k_0` in "
        "`[1.9, 2.1]` | `0.00370115115631918737071374823881` | **FAIL** |",
        "TASK 2 → `ROW-NOT-CERTIFIED`.",
    ],
}

# ---------------------------------------------------------------------------
# Frozen constants of the re-anchor (prereg section 2).  DERIVED FROM DIGIT
# COUNTS OF THE SHIPPED STRINGS, not from any measured separation.
# ---------------------------------------------------------------------------

SEED_SIG_DIGITS = 17            # the shipped rung's decimal rendering
COMPARAND_SIG_DIGITS = 30       # mp.nstr(x, 30) -- last_bond_kernel_collapse.py:71-73

BOUND_A = "5e-30"               # half a unit in the 30th significant digit
TOL_A = "1e-27"                 # frozen; headroom 200x over BOUND_A
SEED_RENDER_BOUND = "5e-17"     # half a unit in the 17th significant digit
SEED_SAFETY_FACTOR = 10         # declared, for the unauditable upstream chain
BOUND_BX = "5e-16"              # SEED_RENDER_BOUND x SEED_SAFETY_FACTOR
BOUND_BS = "2.5e-16"            # x (dlnS/dlnx = 1/2) on the near-wall floor
TOL_B = "5e-16"                 # frozen; applied to BOTH leg-B residuals

FT_COARSE_PERTURB = "1e-12"     # must fail LEG-A and LEG-B(x)
FT_FINE_PERTURB = "1e-26"       # must fail LEG-A only; LEG-B untouched

# The v1 record this lane must reproduce (prereg section 3.1, section 5).
V1_SHIPPED_DIGEST = "2af8acfe23aabb96"
V1_N_FILES_SCANNED = 4418
V1_N_LEAVES = 1432
V1_N_GATES_PASS_TRUE = 9
V1_N_SELFTESTS_FIRING = 6

# This lane's own artifacts, dropped from the v1 scan surface by the section-3.2
# wrapper so that the reproduction is not destroyed by pure self-reference.
V2_OWN_ARTIFACTS = {
    "research/2026-08-06_approach-leak-v2_prereg-FROZEN.md",
    "research/2026-08-06_approach-leak-v2_result.md",
    "research/drivers/approach_leak_v2.py",
    "research/drivers/approach_leak_v2_number_check.py",
    "research/drivers/approach_leak_v2_results.json",
    "_orchestration/docket-entries/2026-08-06-approach-leak-v2.md",
}

# NC-BYTES roster (prereg section 3.3): every artifact this lane reads and may
# not write.  Byte-gated against the v1 ship commit.
READ_ONLY_ARTIFACTS = [
    "research/2026-08-05_approach-leak_prereg-FROZEN.md",
    "research/2026-08-05_approach-leak_result.md",
    "research/drivers/approach_leak.py",
    "research/drivers/approach_leak_results.json",
    "research/drivers/approach_leak_number_check.py",
    "_orchestration/docket-entries/2026-08-05-approach-leak.md",
    "research/drivers/last_bond_kernel_collapse.py",
    "research/drivers/last_bond_kernel_collapse_results.json",
    "research/drivers/last_bond_kernel_collapse_number_check.py",
    "research/2026-08-05_last-bond-kernel-collapse_result.md",
]


# ---------------------------------------------------------------------------
# Import the v1 module, apply the ONE declared intervention.
# ---------------------------------------------------------------------------

def import_v1(v1_out: Path):
    """Import the v1 driver module with its output redirected, and wrap its
    scan-surface enumerator per prereg section 3.2.

    `APPROACH_LEAK_OUT` is read by the v1 module AT IMPORT TIME, so it must be
    set before the import.  The wrapper drops THIS lane's artifacts and nothing
    else; it is gated by requiring n_files_scanned to reproduce as 4418.
    """
    os.environ["APPROACH_LEAK_OUT"] = str(v1_out)
    sys.path.insert(0, str(HERE))
    import approach_leak as v1                      # noqa: E402  (deliberate late import)

    original = v1._tracked_files

    def wrapped() -> list[str]:
        return [f for f in original() if f not in V2_OWN_ARTIFACTS]

    wrapped.__doc__ = (
        "prereg section 3.2 wrapper: v1's own six artifacts are already excluded by "
        "v1's construction; this drops THIS lane's six as well, restoring the v1 "
        "scan surface exactly.  GATED: n_files_scanned must reproduce as 4418.")
    v1._tracked_files = wrapped
    return v1


# ---------------------------------------------------------------------------
# Leaf-by-leaf string comparison of two JSON trees.
# ---------------------------------------------------------------------------

def flatten(obj, prefix: str = "") -> dict[str, object]:
    out: dict[str, object] = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            out.update(flatten(v, f"{prefix}/{k}"))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out.update(flatten(v, f"{prefix}/{i}"))
    else:
        out[prefix] = obj
    return out


def compare_trees(shipped: dict, recomputed: dict, ignore: set[str]) -> dict:
    fa, fb = flatten(shipped), flatten(recomputed)
    keys = sorted(set(fa) | set(fb))
    compared = 0
    mismatches: list[dict] = []
    for k in keys:
        if k in ignore:
            continue
        compared += 1
        a = fa.get(k, "<ABSENT-IN-SHIPPED>")
        b = fb.get(k, "<ABSENT-IN-RECOMPUTED>")
        # EXACT STRING EQUALITY on the rendered leaf, not a numeric tolerance.
        if str(a) != str(b):
            mismatches.append({"leaf": k, "shipped": str(a)[:160], "recomputed": str(b)[:160]})
    return {"n_leaves_compared": compared, "n_mismatches": len(mismatches),
            "mismatches": mismatches[:25]}


# ---------------------------------------------------------------------------
# NC-BYTES: every read-only artifact still hashes to its v1-ship-commit blob.
# ---------------------------------------------------------------------------

def _blob(commit: str, rel: str) -> str:
    return subprocess.run(["git", "rev-parse", f"{commit}:{rel}"],
                          cwd=REPO, capture_output=True, text=True).stdout.strip()


def _blob_text(sha: str) -> str:
    return subprocess.run(["git", "cat-file", "blob", sha],
                          cwd=REPO, capture_output=True, text=True).stdout


def _is_subsequence(old_lines: list[str], new_lines: list[str]) -> bool:
    """True iff `old_lines` occurs in order inside `new_lines` -- i.e. the edit that
    took old to new DELETED nothing and only INSERTED.

    Greedy earliest-match is exact for subsequence existence, so this is a decision
    procedure and not a heuristic.  It is used instead of `git diff --numstat` on two
    blobs because the LIVE blob is not in the object database until commit time, and a
    gate must not write objects as a side effect of running.
    """
    it = iter(new_lines)
    for ol in old_lines:
        for nl in it:
            if nl == ol:
                break
        else:
            return False
    return True


def nc_bytes() -> dict:
    """AMENDED 2026-08-06 (AMENDMENT-NCBYTES-2026-08-06), pre-merge and disclosed.

    PURPOSE, unchanged and restated verbatim from the freeze: *this lane wrote
    none of the ten read-only predecessor artifacts.*

    WHAT MOVED: the comparison target for all ten, from V1_SHIP_COMMIT
    (5e2694c0, the PRE-repair v1 ship) to V1_PIN_COMMIT (f3607be8, the REPAIRED
    v1 tip carried in by this branch's 2026-08-06 merge).  For EIGHT of the ten
    that is a no-op in value -- the blob object is the same at both commits --
    and that no-op is COMPUTED here, not asserted.  For the TWO the orchestrator's
    disclosed post-ship SCANFRAG repair rewrote, the target moves onto the
    repaired state.

    NOTHING IS DROPPED.  The original conjunct (live == pinned blob, ten of ten)
    is retained; two NEW conjuncts are added, and both of them gate the re-pin
    itself:
      (i)  the COMPUTED set of artifacts that differ between the two commits must
           equal the DECLARED set REPAIRED_BY_DISCLOSED_ORCHESTRATOR_REPAIR --
           so an undisclosed extra rewrite fails the gate;
      (ii) every artifact NOT in that set must be byte-identical at BOTH commits
           -- so the eight-fold no-op is proved, not claimed.

    RE-AMENDED 2026-08-06 (AMENDMENT-NCBYTES-2026-08-06-B), pre-merge and disclosed.
    A SECOND disclosed move, this one authored by the records lane rather than by the
    orchestrator: the frozen v1 kernel-collapse result document now carries a dated
    supersession note pointing at the ROW-CERTIFIED rerun its own section 1.3 named.
    That artifact's target becomes a PER-ARTIFACT BLOB PIN; the other nine keep the
    commit pin.  Three further conjuncts are ADDED (COMPUTED/DECLARED reconciliation
    of the supersession set, ADDITIVE-ONLY on the moved artifact, and byte-exact
    survival of the record's own FAIL verdict strings).  See `amendment_B_frozen`.
    """
    rows = []
    ok = True
    computed_moved: list[str] = []
    computed_superseded: list[str] = []
    unmoved_stable = True
    sup_additive_all = True
    sup_verdicts_all = True
    sup_reconciles_all = True
    for rel in READ_ONLY_ARTIFACTS:
        b_ship = _blob(V1_SHIP_COMMIT, rel)
        b_pin = _blob(V1_PIN_COMMIT, rel)
        l = subprocess.run(["git", "hash-object", rel],
                           cwd=REPO, capture_output=True, text=True).stdout.strip()
        # AMENDMENT-NCBYTES-2026-08-06-B: the EFFECTIVE pin is the v1-pin blob unless
        # this artifact carries a DECLARED per-artifact supersession blob pin.
        b_eff = SUPERSESSION_BLOB_PIN.get(rel, b_pin)
        pin_src = ("AMENDMENT-NCBYTES-2026-08-06-B" if rel in SUPERSESSION_BLOB_PIN
                   else "V1_PIN_COMMIT")
        same = bool(b_eff) and b_eff == l
        ok = ok and same
        moved = bool(b_ship) and bool(b_pin) and b_ship != b_pin
        declared = rel in REPAIRED_BY_DISCLOSED_ORCHESTRATOR_REPAIR
        if moved:
            computed_moved.append(rel)
        else:
            unmoved_stable = unmoved_stable and (b_ship == b_pin)
        # amendment B's own COMPUTED/DECLARED reconciliation, on the SAME shape as A:
        # "did this artifact's live bytes leave the v1 pin?" vs "did we say so?".
        sup_moved = bool(b_pin) and bool(l) and b_pin != l
        sup_declared = rel in MOVED_BY_DISCLOSED_SUPERSESSION_NOTE
        sup_reconciles_all = sup_reconciles_all and (sup_moved == sup_declared)
        if sup_moved:
            computed_superseded.append(rel)
        row = {"path": rel,
               "blob_at_v1_ship": b_ship[:12],
               "blob_at_v1_pin": b_pin[:12],
               "blob_at_effective_pin": b_eff[:12],
               "effective_pin_source": pin_src,
               "blob_live": l[:12],
               "byte_identical": same,
               "moved_by_disclosed_repair_COMPUTED": moved,
               "moved_by_disclosed_repair_DECLARED": declared,
               "declaration_reconciles": moved == declared,
               "moved_by_disclosed_supersession_COMPUTED": sup_moved,
               "moved_by_disclosed_supersession_DECLARED": sup_declared,
               "supersession_declaration_reconciles": sup_moved == sup_declared}
        if sup_declared:
            old_lines = _blob_text(b_pin).splitlines()
            new_lines = Path(REPO / rel).read_text(encoding="utf-8").splitlines()
            additive = _is_subsequence(old_lines, new_lines)
            probes = FROZEN_VERDICT_PROBES.get(rel, [])
            live_text = "\n".join(new_lines)
            missing = [p for p in probes if p not in live_text]
            sup_additive_all = sup_additive_all and additive
            sup_verdicts_all = sup_verdicts_all and not missing
            row.update({
                "supersession_lines_at_v1_pin": len(old_lines),
                "supersession_lines_live": len(new_lines),
                "supersession_lines_added": len(new_lines) - len(old_lines),
                "supersession_additive_only_COMPUTED": additive,
                "supersession_n_frozen_verdict_probes": len(probes),
                "supersession_frozen_verdicts_preserved_COMPUTED": not missing,
                "supersession_frozen_verdict_probes_missing": missing,
            })
        rows.append(row)
    delta_reconciles = sorted(computed_moved) == sorted(REPAIRED_BY_DISCLOSED_ORCHESTRATOR_REPAIR)
    sup_delta_reconciles = (sorted(computed_superseded)
                            == sorted(MOVED_BY_DISCLOSED_SUPERSESSION_NOTE))
    return {"frozen": (f"every read-only predecessor artifact hashes to its blob at the pinned v1 "
                       f"commit -- this lane wrote none of them. AMENDED 2026-08-06: the pin is "
                       f"the REPAIRED v1 tip {V1_PIN_COMMIT}, not the pre-repair ship "
                       f"{V1_SHIP_COMMIT}; two of the ten were rewritten between them by the "
                       f"ORCHESTRATOR's disclosed SCANFRAG repair, an event extrinsic to this "
                       f"lane. Purpose preserved, no conjunct dropped, two conjuncts ADDED that "
                       f"gate the re-pin itself."),
            "amendment": "AMENDMENT-NCBYTES-2026-08-06",
            "amendment_disclosure": ("research/2026-08-06_approach-leak-v2_result.md section 9; "
                                     "_orchestration/docket-entries/"
                                     "2026-08-06-approach-leak-v2-correction.md"),
            "pin_commit": V1_PIN_COMMIT,
            "pin_choice": "ALL TEN re-pinned at the repaired v1 tip (not a split pin)",
            "pin_choice_rationale": ("one pin, one truth-source: f3607be8 is a descendant of "
                                     "5e2694c0 whose diff touches exactly two of the ten, so for "
                                     "the other eight the pin is a COMPUTED no-op (see "
                                     "unmoved_artifacts_identical_at_both_commits); and the "
                                     "repaired tip is the predecessor state that will actually "
                                     "merge to main, so the gate tracks the mergeable predecessor "
                                     "rather than a superseded intermediate. A split pin would "
                                     "carry two commit references for one roster with no gain in "
                                     "strength and a standing drift hazard."),
            "superseded_pin_commit": V1_SHIP_COMMIT,
            "superseded_pin_retained_per_artifact": True,
            "n_artifacts": len(READ_ONLY_ARTIFACTS),
            "artifacts": rows,
            "artifacts_moved_between_pins_COMPUTED": sorted(computed_moved),
            "artifacts_moved_between_pins_DECLARED": sorted(
                REPAIRED_BY_DISCLOSED_ORCHESTRATOR_REPAIR),
            "delta_declaration_reconciles": bool(delta_reconciles),
            "unmoved_artifacts_identical_at_both_commits": bool(unmoved_stable),
            # ---- AMENDMENT-NCBYTES-2026-08-06-B ------------------------------
            "amendment_B": "AMENDMENT-NCBYTES-2026-08-06-B",
            "amendment_B_disclosure": ("_orchestration/docket-entries/"
                                       "2026-08-06-g-rho2-supersession.md"),
            "amendment_B_frozen": (
                "ONE read-only artifact -- the frozen v1 kernel-collapse result document -- "
                "carries a DISCLOSED, records-lane-authored dated supersession note, so its "
                "live blob no longer equals its blob at the v1 pin commit. Its pin moves to "
                "a per-artifact BLOB pin rather than a commit pin, because the commit that "
                "carries the move does not exist until this branch commits. Purpose "
                "preserved (no predecessor drifted un-disclosed); nothing dropped; THREE "
                "conjuncts ADDED, all of which gate the re-pin itself: (i) the COMPUTED "
                "left-the-v1-pin set must equal the DECLARED supersession set, so an "
                "undisclosed edit to any of the other nine fails; (ii) the move must be "
                "ADDITIVE-ONLY -- the pinned text must survive as a line subsequence of the "
                "live text, so the frozen record cannot be rewritten under cover of a "
                "'note'; (iii) the record's OWN verdict strings (the ROW-NOT-CERTIFIED "
                "line, the G-RHO2 FAIL table row, the frozen-consequence line) must still "
                "be present byte-exactly, because a blob pin says WHICH BYTES and never "
                "WHICH CLAIM."),
            "amendment_B_pin_kind": "per-artifact blob pin (not a commit pin)",
            "amendment_B_blob_pin_DECLARED": dict(SUPERSESSION_BLOB_PIN),
            "artifacts_moved_by_supersession_COMPUTED": sorted(computed_superseded),
            "artifacts_moved_by_supersession_DECLARED": sorted(
                MOVED_BY_DISCLOSED_SUPERSESSION_NOTE),
            "supersession_delta_declaration_reconciles": bool(sup_delta_reconciles),
            "supersession_all_moves_additive_only": bool(sup_additive_all),
            "supersession_all_frozen_verdicts_preserved": bool(sup_verdicts_all),
            "supersession_per_artifact_declaration_reconciles": bool(sup_reconciles_all),
            "pass": bool(ok and delta_reconciles and unmoved_stable
                         and sup_delta_reconciles and sup_additive_all
                         and sup_verdicts_all and sup_reconciles_all)}


# ---------------------------------------------------------------------------
# THE RE-ANCHORED GATE (prereg section 2 / section 4.1).
# ---------------------------------------------------------------------------

def slast_legs(v1, seed_str: str, comparand_str: str) -> dict:
    """Evaluate LEG-A, LEG-B(x) and LEG-B(S).

    LEG-A  : S_last recomputed from the SHIPPED SEED through v1's own
             cancellation-free S2_exact with r_sat = 1, which is term-for-term
             the last-bond driver's `s_squared_exact(x) = x(2+x)/(1+x)^2`.
    LEG-B  : this lane's mass-derived ell/r_sat at 62 M_sun and its S_1 at
             theta = 1, against the same two shipped strings.
    """
    mp = v1.mp
    x_r = mp.mpf(seed_str)
    s_shipped = mp.mpf(comparand_str)

    s_a = mp.sqrt(v1.S2_exact(x_r, mp.mpf(1)))
    leg_a = abs(s_a - s_shipped) / s_shipped

    rs_ref = v1.r_sat(v1.M_REF)
    x_ref = v1.L_NODE / rs_ref
    s_1 = mp.sqrt(v1.S2_exact(mp.mpf(1) * v1.L_NODE, rs_ref))
    leg_bx = abs(x_ref - x_r) / x_r
    leg_bs = abs(s_1 - s_shipped) / s_shipped

    return {
        "S_A_from_shipped_seed": v1._s(s_a, 30),
        "S_A_string_identical_to_shipped": (v1._s(s_a, 30) == comparand_str),
        "leg_A_rel": v1._s(leg_a, 6),
        "leg_A_pass": bool(leg_a < mp.mpf(TOL_A)),
        "this_lane_ell_over_rsat": v1._s(x_ref, 30),
        "this_lane_S_1": v1._s(s_1, 30),
        "leg_Bx_rel": v1._s(leg_bx, 6),
        "leg_Bx_pass": bool(leg_bx < mp.mpf(TOL_B)),
        "leg_Bs_rel": v1._s(leg_bs, 6),
        "leg_Bs_pass": bool(leg_bs < mp.mpf(TOL_B)),
    }


def build_slast_gate(v1, seed_str: str, comparand_str: str) -> dict:
    legs = slast_legs(v1, seed_str, comparand_str)
    passed = legs["leg_A_pass"] and legs["leg_Bx_pass"] and legs["leg_Bs_pass"]
    return {
        "frozen": ("SEED-AWARE re-anchor (prereg section 2). LEG-A: S_last recomputed from the "
                   "SHIPPED SEED through the identical cancellation-free form reproduces the "
                   "shipped S_last. LEG-B: this lane's mass-derived ell/r_sat and S_1 reproduce "
                   "the shipped strings. PASS iff ALL THREE legs pass."),
        "shipped_seed_ell_over_rsat": seed_str,
        "shipped_seed_significant_digits": SEED_SIG_DIGITS,
        "shipped_S_last": comparand_str,
        "shipped_comparand_significant_digits": COMPARAND_SIG_DIGITS,
        "tol_leg_A": TOL_A,
        "bound_leg_A": BOUND_A,
        "headroom_leg_A": "200x",
        "tol_leg_B": TOL_B,
        "bound_leg_Bx": BOUND_BX,
        "bound_leg_Bs": BOUND_BS,
        "seed_render_bound": SEED_RENDER_BOUND,
        "seed_safety_factor": SEED_SAFETY_FACTOR,
        "derivation": ("the tolerances derive from the DIGIT COUNTS of the shipped strings and "
                       "from nothing else: half a unit in the 30th significant digit for the "
                       "comparand's mp.nstr(x, 30) rendering, and half a unit in the 17th for "
                       "the seed's, times a declared safety factor for the seed's unauditable "
                       "upstream chain (FLAG-RUNGPROV). v1's measured 2.04408e-17 is NOT an "
                       "input to either derivation."),
        "v1_frozen_tolerance_superseded": "1e-40 rel (single leg, mass-derived)",
        "v1_domain_of_validity_violation": ("1e-40 sat 10 orders below the comparand's own "
                                            "30-digit rendering floor and 23 orders below the "
                                            "seed's 17-digit floor: unsatisfiable by ANY correct "
                                            "instrument, hence ARTIFACT-class"),
        **legs,
        "pass": bool(passed),
    }


def build_ft_slast(v1, seed_str: str, comparand_str: str) -> dict:
    """Two-part fireability. BOTH parts must produce the required failures."""
    mp = v1.mp

    # (i) COARSE: perturb the SEED. LEG-A and LEG-B(x) must both fail.
    seed_pert = v1._s(mp.mpf(seed_str) * (1 + mp.mpf(FT_COARSE_PERTURB)), 40)
    coarse = slast_legs(v1, seed_pert, comparand_str)
    coarse_fires = (not coarse["leg_A_pass"]) and (not coarse["leg_Bx_pass"])

    # (ii) FINE: perturb the COMPARAND by 1e-26, one decade above TOL_A.
    #      LEG-A must fail; LEG-B must be UNTOUCHED and still pass -- which is
    #      what proves TOL_A is non-vacuous at its own scale.
    comp_pert = v1._s(mp.mpf(comparand_str) * (1 + mp.mpf(FT_FINE_PERTURB)), 40)
    fine = slast_legs(v1, seed_str, comp_pert)
    fine_fires = (not fine["leg_A_pass"]) and fine["leg_Bx_pass"] and fine["leg_Bs_pass"]

    return {
        "frozen": ("(i) COARSE: perturbing the shipped seed by 1e-12 must make LEG-A FAIL and "
                   "LEG-B(x) FAIL. (ii) FINE: perturbing the shipped comparand by 1e-26 must "
                   "make LEG-A FAIL while LEG-B is untouched and still passes -- proving the "
                   "1e-27 leg is non-vacuous at its own scale. BOTH parts required."),
        "coarse_perturbation": FT_COARSE_PERTURB,
        "coarse_leg_A_rel": coarse["leg_A_rel"],
        "coarse_leg_A_pass": coarse["leg_A_pass"],
        "coarse_leg_Bx_rel": coarse["leg_Bx_rel"],
        "coarse_leg_Bx_pass": coarse["leg_Bx_pass"],
        "coarse_fires": bool(coarse_fires),
        "fine_perturbation": FT_FINE_PERTURB,
        "fine_leg_A_rel": fine["leg_A_rel"],
        "fine_leg_A_pass": fine["leg_A_pass"],
        "fine_leg_Bx_pass": fine["leg_Bx_pass"],
        "fine_leg_Bs_pass": fine["leg_Bs_pass"],
        "fine_fires": bool(fine_fires),
        "fires": bool(coarse_fires and fine_fires),
    }


# ---------------------------------------------------------------------------
# THE ADJUDICATION (prereg section 6).  v1's frozen bin DEFINITIONS, verbatim.
# ---------------------------------------------------------------------------

def theta_disaggregation(v1, pk: str) -> dict:
    """Disaggregate ONE bracket member's N_open by theta, through v1's own
    N_open_count.  Run only for the member whose aggregate set contains BOTH 0
    and a positive value -- i.e. the only member where the aggregate can hide a
    split.  This is a DISAGGREGATION of the reproduced sweep computed by the v1
    instrument's own function, not a new quantity.
    """
    mp = v1.mp
    p = mp.mpf(pk)
    out: dict[str, list[int]] = {}
    for theta in v1.THETAS:
        vals: set[int] = set()
        for m in v1.MASSES:
            rs = v1.r_sat(m)
            x = v1.L_NODE / rs
            for Om in v1.BAND:
                n, _ = v1.N_open_count(Om, x, p, theta, rs)
                vals.add(n)
        out[v1._s(theta, 3)] = sorted(vals)
    return out


def adjudicate(v1, repro: dict) -> dict:
    """Award the bins using v1's FROZEN section-7 definitions, verbatim.

    GAP-CLOSED     : N_open = 0 at EVERY row of the frozen sweep for the member
    CHANNEL-OPENS  : N_open >= 1 at ANY row
    Reporting overlay (prereg section 6.1(1)): a member whose verdict splits on
    a swept parameter is ALSO annotated SPLIT with the parameter named.  The
    OVERLAY DOES NOT MOVE THE BOUNDARY -- the awarded bin is v1's.
    """
    per_p = repro["sweep"]["per_p"]
    members = []
    for pk in sorted(per_p, key=float):
        v = per_p[pk]
        vals = v["N_open_distinct_values"]
        bin_frozen = "GAP-CLOSED" if set(vals) == {0} else "CHANNEL-OPENS"
        split = (0 in vals) and any(n != 0 for n in vals)
        row = {
            "p": pk,
            "provenance": v["provenance"],
            "N_open_distinct_values": vals if len(vals) <= 6 else [min(vals), "...", max(vals)],
            "n_distinct": len(vals),
            "bin_by_v1_frozen_definition": bin_frozen,
            "side_of_p_crit": v["side_of_p_crit"],
            "log10_margin_min": v["log10_margin_min"],
            "log10_margin_max": v["log10_margin_max"],
            "zeta_max_over_sweep": v["zeta_max_over_sweep"],
            "canon_or_engine_stated": pk in ("0.5", "1.0"),
            "requires_unwritten_I_omega_law": pk in ("2.0", "2.5", "3.0"),
            "split_overlay": split,
        }
        if split:
            row["split_disaggregation_by_theta"] = theta_disaggregation(v1, pk)
            row["split_note"] = ("the aggregate hides a split; disaggregated by theta through "
                                 "v1's own N_open_count. The AWARDED bin remains v1's frozen "
                                 "CHANNEL-OPENS (N_open >= 1 at some row); the split is a "
                                 "REPORTING overlay and moves no boundary.")
        members.append(row)

    gap_closed = [m["p"] for m in members if m["bin_by_v1_frozen_definition"] == "GAP-CLOSED"]
    opens = [m["p"] for m in members if m["bin_by_v1_frozen_definition"] == "CHANNEL-OPENS"]
    stated = [m["p"] for m in members if m["canon_or_engine_stated"]]

    scan = repro["scan"]
    absence = {pid: scan[pid]["ABSENCE_RECEIPT"] for pid in ("P1", "P2", "P3", "P4", "P5")}
    underdetermined = bool(absence["P3"] and absence["P4"])

    return {
        "bin_definitions_source": ("research/2026-08-05_approach-leak_prereg-FROZEN.md section 7 "
                                   "-- used VERBATIM; no boundary moved, no bin added or merged"),
        "bin_arithmetic_source": ("ibid. section 7 frozen bin-arithmetic -- BOTH bins reported, "
                                  "members named, no member preferred, no single headline bin "
                                  "unless every member agrees"),
        "members": members,
        "GAP-CLOSED_members": gap_closed,
        "CHANNEL-OPENS_members": opens,
        "members_canon_or_engine_states": stated,
        "every_stated_member_is_GAP-CLOSED": bool(set(stated) <= set(gap_closed)),
        "UNDERDETERMINED-CANON": {
            "fires": underdetermined,
            "missing_laws_enumerated": [
                "I_omega(A) grading law -- exponent b -- ZERO hits on P3 and P4, both engines",
                "G_c(A) grading law -- exponent a -- no canon leaf states it; the only "
                "substantive P2 hit is the ENGINE line cosserat_field_3d.py:767, unratified",
            ],
            "P3_absence_receipt": absence["P3"],
            "P4_absence_receipt": absence["P4"],
            "n_files_scanned": repro["gates"]["G-SCAN"]["n_files_scanned"],
            "note": ("the absence receipts are RE-VERIFIED on this branch by the reproduction, "
                     "not inherited from the v1 record"),
        },
        "SCALE-UNDERDETERMINED": {
            "fires": True,
            "field": "residual_backaction_QUARANTINED -- the prefactor 2*(G_c/G) and that alone",
            "reason": ("A-008 pins G_c/I_omega, NOT G_c/G; every other number in the lane is "
                       "ratio-only (N_open is an integer, zeta_max a dimensionless amplitude "
                       "ratio, the margin a competition between two powers of ell_node/r_sat)"),
            "not_extended_to": "any other field, per the v1 freeze",
        },
        "rotational_top_bracket_status": (
            "MOOT on every below-knife member -- the drive never reaches the band at all, so "
            "its top is never consulted. Reported as moot, not silently dropped."),
        "analogy_declaration": ("every p >= 2 member rides the RHO-B 1/S^3 grading applied to the "
                                "micro-inertia BY ANALOGY. It is an ANALOGY and NOT CANON, and is "
                                "labelled as such at every site it appears."),
    }


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()

    shipped_v1 = json.loads(V1_JSON.read_text(encoding="utf-8"))
    lb = json.loads(LASTBOND_JSON.read_text(encoding="utf-8"))
    rung = lb["task3_continuum"]["ladder"][0]
    seed_str = rung["ell_over_rsat"]
    comparand_str = rung["S_last_from_exact_S2"]

    with tempfile.TemporaryDirectory() as td:
        v1_out = Path(td) / "v1_reproduction.json"
        v1 = import_v1(v1_out)
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = v1.main()
        if rc != 0:
            print("v1 reproduction run returned non-zero", file=sys.stderr)
            return 1
        repro = json.loads(v1_out.read_text(encoding="utf-8"))

        cmp_result = compare_trees(shipped_v1, repro, ignore={"/_runtime_sec"})

        gates_pass_true = sorted(k for k, v in repro["gates"].items() if v.get("pass") is True)
        gates_pass_false = sorted(k for k, v in repro["gates"].items() if v.get("pass") is False)
        gates_pass_null = sorted(k for k, v in repro["gates"].items() if v.get("pass") is None)
        fts_firing = sorted(k for k, v in repro["self_tests"].items() if v.get("fires") is True)

        nfiles = repro["gates"]["G-SCAN"]["n_files_scanned"]
        digest_ok = repro["_digest"] == V1_SHIPPED_DIGEST

        repro_pass = bool(
            cmp_result["n_mismatches"] == 0
            and cmp_result["n_leaves_compared"] == V1_N_LEAVES - 1   # _runtime_sec ignored
            and digest_ok
            and nfiles == V1_N_FILES_SCANNED
            and len(gates_pass_true) == V1_N_GATES_PASS_TRUE
            and len(fts_firing) == V1_N_SELFTESTS_FIRING
        )

        gates: dict[str, dict] = {}
        gates["G-NC-REPRO"] = {
            "frozen": ("the v1 instrument, re-executed on this branch under the section-3.2 "
                       "wrapper, reproduces the shipped approach_leak_results.json with EXACT "
                       "STRING EQUALITY on every leaf apart from _runtime_sec; 0 mismatches "
                       "required, and the recomputed _digest must equal the shipped one"),
            "n_leaves_compared": cmp_result["n_leaves_compared"],
            "n_leaves_shipped_total": V1_N_LEAVES,
            "n_leaves_ignored": 1,
            "ignored_leaves": ["/_runtime_sec (machine-dependent; not a number-check target)"],
            "n_mismatches": cmp_result["n_mismatches"],
            "mismatches": cmp_result["mismatches"],
            "recomputed_digest": repro["_digest"],
            "shipped_digest": V1_SHIPPED_DIGEST,
            "digest_identical": digest_ok,
            "declared_intervention": (
                "v1._tracked_files is wrapped to additionally drop THIS lane's six artifacts, "
                "restoring the v1 scan surface exactly (prereg section 3.2). Without it the "
                "delta is exactly seven leaves, of which n_files_scanned and scan.P5 are pure "
                "self-reference. The wrapper is ITSELF GATED by requiring n_files_scanned = 4418."),
            "v2_artifacts_dropped_from_scan_surface": sorted(V2_OWN_ARTIFACTS),
            "pass": repro_pass,
        }
        gates["G-DET-V1-WRAPPED"] = {
            "frozen": ("v1's own G-DET criterion, preserved under the section-1.1 build-wiring "
                       "supersession: the v1 driver re-run in-process under the wrapper must "
                       "reproduce the shipped digest. Same criterion, same tolerance (identity)."),
            "recomputed_digest": repro["_digest"],
            "shipped_digest": V1_SHIPPED_DIGEST,
            "pass": digest_ok,
        }
        gates["NC-GATES"] = {
            "frozen": ("every v1 gate block reproduces, including the 9 shipped pass:true, the "
                       "1 shipped pass:false (v1's G-NC-SLAST at its OWN 1e-40 siting -- "
                       "reproducing v1's FAILING value byte-exact is the strongest available "
                       "proof that only the ANCHOR moved and not the instrument), and the 2 "
                       "shipped pass:null"),
            "n_gates_pass_true": len(gates_pass_true),
            "gates_pass_true": gates_pass_true,
            "n_gates_pass_false": len(gates_pass_false),
            "gates_pass_false": gates_pass_false,
            "n_gates_pass_null": len(gates_pass_null),
            "gates_pass_null": gates_pass_null,
            "v1_G_NC_SLAST_failing_value_reproduced": repro["gates"]["G-NC-SLAST"]["measured_rel_sep"],
            "v1_G_NC_SLAST_shipped_value": shipped_v1["gates"]["G-NC-SLAST"]["measured_rel_sep"],
            "pass": bool(len(gates_pass_true) == V1_N_GATES_PASS_TRUE
                         and repro["gates"]["G-NC-SLAST"]["measured_rel_sep"]
                         == shipped_v1["gates"]["G-NC-SLAST"]["measured_rel_sep"]),
        }
        gates["NC-FT"] = {
            "frozen": "all 6 v1 self-test blocks reproduce, every field, every fires flag true",
            "n_self_tests_firing": len(fts_firing),
            "self_tests_firing": fts_firing,
            "pass": bool(len(fts_firing) == V1_N_SELFTESTS_FIRING),
        }
        gates["NC-SCAN"] = {
            "frozen": ("n_files_scanned reproduces as 4418 and every P1-P5 hit count, agreement "
                       "flag and union-hit list reproduces -- so the I_omega(A) absence receipt "
                       "UNDERDETERMINED-CANON rests on is RE-VERIFIED, not inherited"),
            "n_files_scanned": nfiles,
            "n_files_scanned_expected": V1_N_FILES_SCANNED,
            "per_pattern": {pid: {"A": repro["scan"][pid]["method_A_git_grep_P_hits"],
                                  "B": repro["scan"][pid]["method_B_python_re_hits"],
                                  "agree": repro["scan"][pid]["agree"],
                                  "absence_receipt": repro["scan"][pid]["ABSENCE_RECEIPT"]}
                            for pid in ("P1", "P2", "P3", "P4", "P5")},
            "pass": bool(nfiles == V1_N_FILES_SCANNED
                         and all(repro["scan"][pid]["agree"] for pid in
                                 ("P1", "P2", "P3", "P4", "P5"))),
        }
        gates["NC-BYTES"] = nc_bytes()
        gates["G-NC-SLAST"] = build_slast_gate(v1, seed_str, comparand_str)

        self_tests = {"FT-SLAST": build_ft_slast(v1, seed_str, comparand_str)}

        adjud = adjudicate(v1, repro)

    all_gate_pass = all(v.get("pass") is True for v in gates.values())
    all_ft_fire = all(v.get("fires") is True for v in self_tests.values())
    certified = bool(all_gate_pass and all_ft_fire)

    payload = {
        "_prereg": ("research/2026-08-06_approach-leak-v2_prereg-FROZEN.md "
                    "(commit ebd1f4c7, pushed with no code)"),
        "_predecessor": ("research/2026-08-05_approach-leak_prereg-FROZEN.md + _result.md "
                         "(branch research/approach-leak, PR #903, CLEARED, UNMERGED)"),
        "_non_claim": ("DERIVATION result. Mints no clm-/def-/exp-/sup-/ilk-; propagates to no KB "
                       "or manuscript leaf; moves no solidity. Engine src/ave byte-untouched and "
                       "never imported. Every predecessor artifact byte-untouched (NC-BYTES)."),
        "_method": {
            "no_v1_physics_reimplemented": True,
            "v1_module_imported_and_its_main_called": True,
            "dps": 60,
            "error_model": "round-off only; no iterated map; closed forms evaluated once",
        },
        "_frozen_reanchor_constants": {
            "seed_significant_digits": SEED_SIG_DIGITS,
            "comparand_significant_digits": COMPARAND_SIG_DIGITS,
            "bound_leg_A": BOUND_A, "tol_leg_A": TOL_A,
            "seed_render_bound": SEED_RENDER_BOUND,
            "seed_safety_factor": SEED_SAFETY_FACTOR,
            "bound_leg_Bx": BOUND_BX, "bound_leg_Bs": BOUND_BS, "tol_leg_B": TOL_B,
            "ft_coarse_perturbation": FT_COARSE_PERTURB,
            "ft_fine_perturbation": FT_FINE_PERTURB,
        },
        "gates": gates,
        "self_tests": self_tests,
        "certification": {
            "verdict": "LEAK-CERTIFIED-V2" if certified else "LEAK-NOT-CERTIFIED-V2",
            "all_gates_pass": all_gate_pass,
            "all_self_tests_fire": all_ft_fire,
            "consequence_clause": ("v2 RETAINS the GLOBAL form of v1's consequence, unweakened "
                                   "(prereg section 5.1) -- a v2 choice recorded before any v2 "
                                   "number existed, and the stricter of the two options"),
        },
        "adjudication": adjud if certified else {
            "STATUS": "NOT ADJUDICATED -- certification failed; the global consequence is honoured"},
        "flags_carried_by_pointer": {
            "FLAG-EXP": "research/2026-08-05_approach-leak_result.md section 7 -- not restated, not repaired",
            "FLAG-IOMEGA": "research/2026-08-05_approach-leak_result.md section 7 -- not restated, not repaired",
            "FLAG-MECH": "research/2026-08-05_approach-leak_result.md section 7 -- not restated, not repaired",
            "FLAG-ROTTOP": "research/2026-08-05_approach-leak_result.md section 7 -- not restated, not repaired",
            "FLAG-FREEZE": "DISCHARGED by this lane; the v1 body stays byte-untouched (Rule 12)",
            "FLAG-RUNGPROV": "NEW, minted at freeze (prereg section 2.1). Surfaced, NOT repaired.",
            "FLAG-SCANFRAG": "NEW, minted at freeze (prereg section 1.1). Surfaced, NOT repaired.",
        },
        "gates_DET": {
            "G-DET-V2": {
                "frozen": "two full v2 runs, identical digest, byte-identical apart from _runtime_sec",
                "method": ("MACHINE-GATED on every make verify: approach_leak_v2_number_check.py "
                           "re-runs this driver into a temporary path via APPROACH_LEAK_V2_OUT "
                           "and requires the recomputed _digest to equal the shipped one"),
                "status": "GATED BY THE NUMBER-CHECK",
                "pass": None,
            }
        },
    }

    body = json.dumps(payload, indent=1, sort_keys=True, ensure_ascii=False)
    payload["_digest"] = hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]
    payload["_runtime_sec"] = round(time.time() - t0, 2)
    OUT.write_text(json.dumps(payload, indent=1, sort_keys=True, ensure_ascii=False) + "\n",
                   encoding="utf-8")

    failed = [k for k, v in gates.items() if v.get("pass") is not True]
    nofire = [k for k, v in self_tests.items() if v.get("fires") is not True]
    print(f"digest={payload['_digest']}  verdict={payload['certification']['verdict']}")
    print(f"  gates_failed={failed}  self_tests_not_fired={nofire}")
    print(f"  G-NC-REPRO: {cmp_result['n_leaves_compared']} leaves, "
          f"{cmp_result['n_mismatches']} mismatches, digest {repro['_digest']}")
    g = gates["G-NC-SLAST"]
    print(f"  G-NC-SLAST v2: LEG-A={g['leg_A_rel']} (tol {TOL_A})  "
          f"LEG-B(x)={g['leg_Bx_rel']}  LEG-B(S)={g['leg_Bs_rel']} (tol {TOL_B})")
    if certified:
        print(f"  GAP-CLOSED: {adjud['GAP-CLOSED_members']}   "
              f"CHANNEL-OPENS: {adjud['CHANNEL-OPENS_members']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
