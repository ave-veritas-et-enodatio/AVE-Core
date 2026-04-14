# Structure Review — Final Confirmation Pass
*Reviewer: kb-structure-reviewer | Date: 2026-04-03 | Scope: Phase 4b fixes + adversarial investigation*

---

## Structure Review Summary

One Critical finding was uncovered that all prior review passes missed: the entry-point's Vol 3 domain routing table omits the `Applied Physics` domain entirely, routing applied-physics topics (stellar interiors, neutrino oscillation, ideal gas law, geophysics) through the `Condensed Matter` link. An agent starting from the entry-point with a question about stellar interiors or seismic waves will follow `Condensed Matter → index.md → ch09/10/11` and find no path forward; the Applied Physics subtree (ch07, ch12, ch13) is unreachable from entry-point by following links. All Phase 4b structural fixes verified correct. No other Critical or Warning findings.

---

## Findings

### FINDING 1 — Critical

**Issue:** The entry-point's Vol 3 domain routing table lists 3 domains (Gravity, Cosmology, Condensed Matter) but vol3 contains 4 domains. The fourth domain, `Applied Physics`, is absent from the entry-point table. The Condensed Matter row's "Contents" summary has been populated with applied-physics topics ("stellar interiors; geophysics") to compensate, but this creates a false routing: the `Applied Physics` domain index at `vol3/applied-physics/index.md` is not reachable from the entry-point by any sequence of down-links.

**Location:** `/manuscript/ave-kb/entry-point.md`, lines 48–52 (Vol 3 domain table); confirmed against `/manuscript/ave-kb/vol3/index.md` lines 43–50 which correctly lists all 4 domains.

**Navigation impact:** An agent querying about neutrino MSW oscillation, the ideal gas law derivation, or seismic FDTD modelling will route from entry-point to `vol3/condensed-matter/index.md`. That index covers only ch09, ch10, ch11. There is no link from `condensed-matter/index.md` into `applied-physics/`. The agent dead-ends without ever discovering the Applied Physics subtree (ch07-stellar-interiors, ch12-ideal-gas-law, ch13-geophysics — 13 leaves total). Navigation from any Applied Physics leaf back to entry-point works correctly (leaf → chapter index → `applied-physics/index.md` → `vol3/index.md` → entry-point), but the reverse traversal (entry-point → Applied Physics leaf) is broken.

**Avoidance requirement:** Every domain-level index reachable from `vol3/index.md` must also appear as a named row in the `entry-point.md` Vol 3 domain table, with a link that resolves to that domain's index file.

---

## Phase 4b Fix Verification

All six Phase 4b fixes confirmed:

1. **vol3/gravity/ch01-gravity-yield ell changes** — Verified. All 6 files (`gravitational-coupling-constant.md`, `index.md`, `kinetic-yield-threshold.md`, `leaky-cavity-decay.md`, `optical-refraction-gravity.md`, `static-nodal-tension.md`) contain `\ell_{node}`. The protected file `trace-reversal-mechanism.md` retains `l_{node}` (roman ell) as required; grep confirms 1 roman instance, 0 script instances.

2. **vol2/particle-physics/ch02-baryon-sector/thermal-softening.md line 9** — Verified. Line 9 now contains `\ell_{node}` (script ell). Remaining roman-ell instances at lines 55, 73, 86 are preserved as per INVARIANT-N2 (vol2 roman-ell instances are legitimate).

3. **vol3/condensed-matter/ch09-condensed-matter-superconductivity/remaining-ch09-results.md** — Verified. Line 1 uplink: `[↑ Ch.9: Condensed Matter and Superconductivity](index.md)` (correct sibling path, not `../index.md`). Line 2: `<!-- leaf: verbatim -->` (correct, not placeholder variant). Listed in ch09 index at line 32. Resolves correctly.

4. **vol3/condensed-matter/ch11-thermodynamics/ch11-remaining-resultboxes.md** — Verified. Line 1 uplink: `[↑ Ch.11: Thermodynamics and The Arrow of Time](index.md)` (correct). Line 2: `<!-- leaf: verbatim -->`. Listed in ch11 index at line 54. Resolves correctly.

5. **vol5/protein-folding-engine/network-solver/index.md** — Verified. Line 2 is blank (non-standard annotation removed). No line-2 custom comment present.

6. **ave-kb/CLAUDE.md navigation-pointer index exception** — Verified. Exception paragraph is present after INVARIANT-S6 body text.

---

## Adversarial Investigation Results

### vol3/condensed-matter chapters (ch09, ch10, ch11)

**Orphan check:** All leaves in all three chapters are listed in their chapter indexes. The orphan sweep using resolved paths across all 814 files in vol3 returned zero unlisted leaves.

**Cross-volume link integrity:** All cross-volume links in ch11 index resolve correctly:
- `../../../vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md` — exists
- `../../../vol7/condensed-matter/ch4-phase-transitions/s03-melting-eigenmode.md` — exists

**Key Results:** ch09, ch10, ch11 indexes all contain populated Key Results sections representing results from all subtopics in each chapter.

**Uplinks:** All leaves sampled use correct `index.md` (same-directory sibling) uplink, not `../index.md` (which would skip the chapter level). Both patterns are in use across the KB — the critical check is that resolution is correct, not the literal string, and all tested links resolve correctly.

### vol3/applied-physics chapters (ch07, ch12, ch13)

**Orphan check:** Zero unlisted leaves in any of the three chapters.

**Key Results:** All three chapter indexes (ch07-stellar-interiors, ch12-ideal-gas-law, ch13-geophysics) contain populated Key Results sections.

**Applied-physics domain index:** `applied-physics/index.md` has a populated Key Results section drawing from all 3 chapters and a correct Derivations and Detail table linking to all 3 chapter indexes. Uplink to `vol3/index.md` correct.

**Navigation failure:** While the internal structure of applied-physics is sound, this domain is unreachable from the entry-point (see Finding 1).

### vol3/gravity chapters (ch02, ch03, ch08)

**Orphan check:** Zero unlisted leaves. Confirmed via resolved-path sweep.

**Cross-volume link integrity:** ch02-general-relativity index cross-volume links all resolve:
- `../../../vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md` — exists (noted in index as "vol4 not yet distilled")
- `../../../common/translation-tables/translation-gravity.md` — exists
- `../../../common/translation-tables/translation-cosmology.md` — exists

**Key Results:** ch02, ch03, ch08 indexes all contain populated Key Results sections.

**Uplinks:** Sampled leaves in ch03 and ch08 use `index.md` (correct sibling-level uplink). Gravity domain index uses `../index.md` → `vol3/index.md` correctly.

### Link validator false positives

The link checker reports 3 broken links, all in `ave-kb/CLAUDE.md`. Investigation confirms all three are template/example syntax inside fenced code blocks (the INVARIANT-S4 uplink template `[↑ Parent Name](../index.md)` and the INVARIANT-F1/F2 cross-reference templates `[Document Name](relative/path/to/target.md)`). These are not live navigation links. The link checker cannot distinguish code-block examples from live links. No action required.

---

## Exit Criteria Assessment

**Critical findings:** 1 (entry-point Vol 3 domain table omits Applied Physics domain — navigation dead-end for applied-physics subtree)

**Warning findings:** 0

**Note findings:** 0

**Exit criteria not met.** The KB does not pass "no Critical or Warning findings" until the entry-point Vol 3 domain table is corrected to include Applied Physics as a fourth domain row.

---

## Scope Notes

This review examined:
- All Phase 4b fixes (6 of 6 confirmed)
- Full resolved-path orphan sweep across all of vol3 (814 total files)
- All vol3 chapter indexes for Key Results section completeness
- Cross-volume link integrity for vol3/ch11 and vol3/ch02 (all targeted links verified present on disk)
- Entry-point navigability to each vol3 domain

Not reviewed in this pass:
- vol1, vol2, vol4–vol8 chapter-level structures (outside adversarial scope)
- Leaf content fidelity (accuracy, not structure)
- PATH-STABLE annotation completeness on newly-created leaves
- The `common/` directory structure beyond confirming translation-table files exist
