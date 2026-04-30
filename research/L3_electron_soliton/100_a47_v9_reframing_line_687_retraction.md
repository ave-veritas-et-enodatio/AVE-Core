# L3 Doc 100 — A47 v9 Reframing + Line-687 Retraction (Methodology Artifact)

**Status:** Retraction artifact + methodology lesson. Per Rule 12 (retraction-preserves-body), this doc carries the corrective findings; the originating handoff body is preserved in place with footnote markers pointing here.

**Date:** 2026-04-30
**Lane:** Implementer-drafted, Grant-adjudicated, auditor-concurred.
**Originating artifact:** [`.agents/handoffs/SESSION_HANDOFF_2026-04-30_TRACK_B_ACTIVATION.md`](../../.agents/handoffs/SESSION_HANDOFF_2026-04-30_TRACK_B_ACTIVATION.md) (gitignored per Rule 15 lane discipline; .gitignore:71)
**Pattern precedent:** [doc 81 §2.2 line 36](81_l3_followup_questions.md#L36) — Op20+Op22 synthesis-as-corpus correction footnote (commit `35cc818`).

---

## §1 — What was claimed (verbatim from originating handoff)

The handoff at `.agents/handoffs/SESSION_HANDOFF_2026-04-30_TRACK_B_ACTIVATION.md` (commit `f120ad0`) made four cross-referenced claims about an unimplemented refinement marker in [`src/ave/solvers/radial_eigenvalue.py`](../../src/ave/solvers/radial_eigenvalue.py):

- **§0 line 30 (TL;DR top forward action):** *"Investigate `radial_eigenvalue.py:687` 'not yet implemented' refinement for A47 v9 Li discrepancy resolution (~30 min trace)"*
- **§2.2 line 131 (engine code table):** *"**'not yet implemented' at 687 — A47 v9 root-cause candidate**"*
- **§4.2 line 246 (A47 catalog v9 entry — load-bearing site):** *"root-cause is 'not yet implemented' refinement at radial_eigenvalue.py:687 per Op2 crossing or MCL refinement"*
- **§5.1 line 272 (first immediate action):** *"Investigate `radial_eigenvalue.py:687` 'not yet implemented' comment — what specific refinement (Op2 crossing? MCL?) is missing?"*

The fabrication was load-bearing: §0 listed it as the #1 priority forward action; §5.1 listed it as the first immediate action with `~20 min trace` cost estimate.

---

## §2 — Direct verification (Rule 9 v2: right kind of question?)

**Empirical check 1 — file content at line 687.** Read [`src/ave/solvers/radial_eigenvalue.py`](../../src/ave/solvers/radial_eigenvalue.py) lines 680-695:

```
686    return sol.t, sol.y[0], sol.y[1]
687    [BLANK]
688    [BLANK]
689    # ---------------------------------------------------------------------------
690    # Step 4: ABCD transfer matrix per section (Eq. abcd_section)
691    # ---------------------------------------------------------------------------
```

Line 687 is blank. It is the boundary between `_radial_ode_integrate` and `_abcd_section`.

**Empirical check 2 — full-file grep.** `grep -ni "not.*implement\|TODO\|FIXME\|placeholder\|future work" src/ave/solvers/radial_eigenvalue.py` returns **zero matches across all 1914 lines**.

There is no "not yet implemented" comment anywhere in the file. The four references in the handoff are pinned to a fabricated artifact.

---

## §3 — Empirical re-derivation of A47 v9

Per auditor direction (Rule 9 v2: walk the symptom, not the marker), running the actual computation:

```python
>>> from ave.solvers.radial_eigenvalue import ionization_energy_e2k
>>> ionization_energy_e2k(3)
5.687332  # eV
```

Reference values:

| Source | Li IE (eV) | Error vs CODATA |
|---|:---:|:---:|
| CODATA | 5.392 | — |
| Manuscript table ([ionization-energy-validation.md:18](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md#L18)) | 5.525 | +2.46% |
| Current code (`ionization_energy_e2k(3)` this turn) | 5.687 | **+5.48%** |

**Code-vs-manuscript gap: +2.94%.**

Test harness at [`src/tests/test_radial_eigenvalue.py:35-47`](../../src/tests/test_radial_eigenvalue.py#L35-L47) covers H, He, C, Ge — Li is **omitted from coverage**. The omission is consistent with the code output not reproducing the manuscript value at the test-harness 5% tolerance.

---

## §4 — Reframing of A47 v9

**Original handoff framing (binary):** *"is the refinement implemented?"* — anchored to a non-existent marker.

**Corrected framing (provenance):** *"the manuscript table at ionization-energy-validation.md:18 reports 5.525 eV at +2.46%; the current solver at HEAD outputs 5.687 eV at +5.48%. Where does the +2.94% gap come from?"*

Three candidate provenances for next-session investigation:

1. **Manuscript-vs-code drift** — manuscript values were generated against a prior version of `radial_eigenvalue.py`; solver has changed since manuscript snapshot.
2. **Hand-computed manuscript values** — the table was produced outside the solver (analytical estimate, alternate code) and never matched it.
3. **Parameter-default drift** — current solver uses different default parameters (shell counts, screening model, `kappa_hopf`, integration grid) than what the manuscript run used.

Investigation path: `git log --oneline -- src/ave/solvers/radial_eigenvalue.py` + diff against manuscript-snapshot SHA + parameter-sweep on `ionization_energy_e2k(3, ...)` to locate the parameter delta. ~30-60 min targeted investigation, NOT the ~20 min "find the marker" the handoff implied.

This is a **manuscript-vs-code provenance question**, not a missing-implementation question. Different failure mode, different investigation, different fix surface.

---

## §5 — A47 v11 candidate (auditor-lane, flagged for COLLABORATION_NOTES)

**A47 v11 candidate:** engine-code line-number claims need direct verification, parallel to A43 v2's manuscript-verbatim discipline.

The session catalogued [A47 v10](../../.agents/handoffs/SESSION_HANDOFF_2026-04-30_TRACK_B_ACTIVATION.md) — *"cross-repo Explore-agent claims need direct verification"* — after `diff -q` falsified a hallucinated parent-repo claim. The very next catalog entry (A47 v9) made the same kind of unverified file-content claim about a file *inside* AVE-Core, and elevated the fabrication to the top forward action for next session.

The discipline rule was written but not applied to its neighbor. A47 v11 closes the gap: the same direct-verification rule applies to internal-repo claims, not just cross-repo claims. Specifically:

> Any claim of the form *"file X at line N contains comment/marker/code Y"* must be directly verified by reading or grepping the file before the claim is elevated to a forward action. The cost of `grep` is seconds; the cost of a downstream session burning ~20-30 min on a fabricated marker is real.

This pairs with the existing A43 v2 manuscript-verbatim discipline (auditor-lane, COLLABORATION_NOTES) — both are direct-verification rules at the citation level, applied to different artifact classes (manuscript text vs engine code).

**Lane:** auditor-edit per Rule 15. This doc flags the candidate; auditor sweeps and adds to COLLABORATION_NOTES on next status check.

---

## §6 — Retraction footprint (handoff edits applied)

Per Rule 12 (retraction-preserves-body), the four originating-handoff references receive the doc-81 §2.2 footnote pattern:

- **Load-bearing site** (handoff §4.2 A47 v9 entry, line 246): 🔴 prepended footnote pointing to this doc; original body preserved verbatim.
- **Three derivative references** (handoff §0 line 30, §2.2 line 131, §5.1 line 272): inline backref `[🔴 retracted — see §4.2 footnote + doc 100]`; original body preserved.

The handoff is gitignored (.gitignore:71), so handoff edits don't carry a git diff trail; the audit trail comes from this doc (doc 100, tracked) which describes what was retracted, when, and why.

---

## §7 — Methodology lesson

The line-687 fabrication survived from session-end through handoff-write because:

1. **Internal consistency.** The claim was internally plausible — file path + line number + plausible refinement candidate names ("Op2 crossing" / "MCL refinement"). Nothing about the surface text triggered skepticism.
2. **Cross-reference reinforcement.** Four locations within the handoff each pinned the others; reading any one of them confirmed the others without prompting independent verification.
3. **Lane-restricted artifact.** The handoff was gitignored — no PR review, no diff scrutiny, no reviewer-side `grep` of cited line numbers.
4. **Verification omission.** The directly-verifiable claim (file content at a specific line in a specific file in this repo) wasn't directly verified before being elevated to top forward action.

The catch came from a fresh agent with no prior conversational momentum running `grep` against the actual file at session pickup.

**Generalization:** load-bearing pinned-to-file-content claims — especially in lane-restricted artifacts where there's no diff review — should be the highest-priority targets for verify-on-pickup. This is what A47 v11 (§5) formalizes.

---

## §8 — Tracker propagation (auditor-lane handoff)

For auditor sweep on next "what's the status" check:

- **Clash registry entry:** line-687 hallucinated marker (handoff §0/§2.2/§4.2/§5.1 of `f120ad0` companion artifact) vs direct-grep verification + this doc.
- **Retraction log entry:** A47 v9 reframed under doc-81 §2.2 footnote pattern; load-bearing site (handoff §4.2 line 246) retracted; body preserved verbatim.
- **A-NNN entry candidate:** manuscript-vs-code provenance question — `ionization_energy_e2k(3)` returns 5.687 eV vs manuscript table 5.525 eV (+2.94% gap); test harness at [`src/tests/test_radial_eigenvalue.py:35-47`](../../src/tests/test_radial_eigenvalue.py#L35-L47) omits Li from coverage.
- **A47 v11 candidate:** engine-code line-number claims need direct verification (§5 of this doc).

No tracker edits attempted from implementer lane. Auditor adjudicates final A-NNN numbering, COLLABORATION_NOTES wording, and clash-registry/retraction-log entry shape.

---

— implementer-drafted, 2026-04-30, post-Grant adjudication on (1) doc 81 §2.2 footnote pattern + (2) promotion of catch to tracked numbered doc; auditor concurrence on both lanes.
