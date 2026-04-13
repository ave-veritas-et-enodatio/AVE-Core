# Phase 1a — Structure Feasibility Review (Cycle 2)

**Reviewer:** kb-structure-reviewer
**Date:** 2026-04-02
**Cycle:** 2 of 2

---

## Verification of Cycle 1 Resolutions

### C1 — common/ tree: RESOLVED
All sub-items confirmed: 4 backmatter files added; canonical authority note present; vol1 Ch.0 at vol1/ch0-intro.md; ch4 slug ch4-continuum-electrodynamics. Introduces N1 (see below).

### C2 — Vol 6 → Vol 1 paths: RESOLVED
Both confirmed in §4 table; AC-ANCHOR-7 and AC-ANCHOR-8 added. §9 note 7 not updated (see N2).

### C3 — vol5/common/ orphan: RESOLVED
vol5/common/index.md added; §8g specifies required Contents entry. §5.1 not updated (see N1).

### W1 — INVARIANT-N5 retraction: RESOLVED
Retraction notice in §1; pointer to vol8/NOTES.md.

### W4 — Vol 8 NOTES.md type: RESOLVED
§8b defines [vol8-local] type with content marker, up-link, and Contents requirement.

### W5 — Vol 8 Key Results: RESOLVED
§8a defines strategy using eq:gamma_scaling and eq:unit_circle as anchors; fallback rule specified.

### W6 — Entry-point budget: RESOLVED
§8c: 200 words/vol × 8 + 400 structural = 2000 target, 2200 ceiling.

---

## New Findings from Revision

### Critical N1: §5.1 up-link table contradicts §3.6 skeleton for vol5/common/ leaves
§5.1 still routes vol5/common/{leaf}.md → vol5/index.md, but §3.6 skeleton specifies up-link to vol5/common/index.md. These are mutually exclusive. vol5/common/index.md becomes a navigational sink — parent by down-link, not acknowledged as parent by any up-link.

**Required fix:** Update §5.1 table row for vol5/common/{leaf}.md to specify vol5/common/index.md as target.

### Critical N2: §9 coordinator notes 5 and 7 are stale (still say "TBD" and "not yet resolved")
Note 5 still references vol1/axioms-and-lattice/ch0-preface-foundations.md; note 7 still calls Vol1 paths "not yet resolved." Both were resolved in the revision. Distillers reading these notes will follow the obsolete guidance.

**Required fix:** Update §9 notes 5 and 7 to mark as RESOLVED with pointers to §3.2, §4, and AC-ANCHOR-7/8.

### Warning N3: common/ root leaf up-link parent is ambiguous
§5.1 routes common/{leaf}.md → entry-point, but common/index.md is the structural down-link parent for these leaves. AC-NAV-4 link-graph check will flag false failure.

**Required fix:** Make explicit design decision: common/ root leaves up-link to common/index.md (option A) or entry-point directly (option B). Update §5.1 and §3.1 accordingly.

### Warning N4: Vol 1 file count inconsistent between §3.2 (says 59) and §6 (says 60), both differ from explicit skeleton count (56)
Explicit skeleton count: 11 index + 45 leaves = 56 files. Vol1 taxonomy claims ~58 leaves. The canonical §3.2 is a partial enumeration; full leaves deferred to vol1_taxonomy.md §3.

**Required fix:** §3.2 must not state its own count. §6 must show vol1 count consistent with vol1_taxonomy.md (~11 index + ~58 leaves ≈ 69 files).

### Warning N5: vol5/molecular-foundations/index.md not explicitly declared in §3.6
The domain-level index for molecular-foundations/ is missing from the §3.6 skeleton block. Without it, biophysics-intro/ and organic-circuitry/ have no conformant up-link target.

**Required fix:** Explicitly declare vol5/molecular-foundations/index.md in §3.6 with up-link, Contents, and Key Results requirements.

---

## Summary

**2 Critical / 3 Warning** (all from revision, not original issues)

---

## Sign-off

**Needs revision — escalate to human.**
This is cycle 2 of 2. Two blocking Criticals remain. Both are single-line fixes (§5.1 table row update; §9 note annotations). Scope is minimal — no structural redesign needed. Recommend coordinator authorize a cycle 3 fix pass followed by final feasibility review, or accept the revision directly given that all issues are precisely bounded with known fixes.
