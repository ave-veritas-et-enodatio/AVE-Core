# KB Structure Review — Phase 4b Confirmation (Adversarial)

**Date:** 2026-04-03
**Scope:** `ave-kb/` — 814 files
**Framing:** "The previous review passes found no issues. Assume something was missed. What is it?"

---

## Structure Review Summary

Three review iterations were confirmed, and one structural failure cluster was still present. Two orphaned placeholder files in `vol3/condensed-matter/` survive all three prior iterations undetected. Both are absent from their chapter's Derivations and Detail table (so no down-link path reaches them from the entry-point), carry an undocumented leaf marker variant (`<!-- leaf: placeholder -->`), and have uplinks that resolve to the wrong hierarchy level — the domain index rather than the chapter index directly above them. All other probe targets are clean: vol1 operators-and-regimes navigation and description accuracy, vol6 period-2 and period-3 element indexes, vol5 protein-folding-engine depth, common/index.md Key Results, CLAUDE.md link integrity, and vol8/appendix cross-reference.

---

## Findings

### 4B-STR-C1 (CRITICAL): Orphaned placeholder files with broken uplinks

**Files:**
1. `vol3/condensed-matter/ch09-condensed-matter-superconductivity/remaining-ch09-results.md`
   - Not listed in `ch09-condensed-matter-superconductivity/index.md` (that index has 9 entries; this file is absent)
   - Uplink: `[↑ Ch.9: Condensed Matter and Superconductivity](../index.md)` — but `../index.md` from this file's location resolves to `vol3/condensed-matter/index.md` (the domain index), not the chapter index.

2. `vol3/condensed-matter/ch11-thermodynamics/ch11-remaining-resultboxes.md`
   - Not listed in `ch11-thermodynamics/index.md` (that index has 15 entries; this file is absent)
   - Uplink: `[↑ Ch.11: Thermodynamics and The Arrow of Time](../index.md)` resolves to `vol3/condensed-matter/index.md` (domain index)

**Navigation impact:** An agent navigating down from the entry-point cannot reach either file. If an agent somehow arrives (via directory enumeration), following the uplink delivers them to the domain index while believing they navigated to the chapter — a false hierarchy position that would corrupt accumulated context about where they are in the tree.

**Fix:**
- Add each file to its chapter's Derivations and Detail table
- Fix each file's uplink from `(../index.md)` to `(index.md)` (no path prefix) so it resolves to the chapter index
- Change `<!-- leaf: placeholder -->` to `<!-- leaf: verbatim -->` on line 2 of each file (INVARIANT-S5 compliance)

---

### 4B-STR-W1 (WARNING): Non-standard line-2 annotation in one index file

**File:** `vol5/protein-folding-engine/network-solver/index.md`, line 2

**Issue:** Has `<!-- vol5-internal: ch:network_solver -->` on line 2. INVARIANT-S6 specifies line 2 of an index document must be either blank or a `<!-- path-stable: -->` comment. This is the only index file in the KB with a non-INVARIANT line-2 comment.

**Navigation impact:** Does not break navigation (document has correct uplink, populated Key Results, and populated Derivations table). However, a machine-checkable audit of INVARIANT-S6 compliance would flag this as an anomaly.

**Fix:** Remove the `<!-- vol5-internal: ch:network_solver -->` comment from line 2 (or replace with a blank line).

---

### 4B-STR-W2 (WARNING): Two navigation-pointer indexes missing Key Results with no machine-readable exception

**Files:**
- `common/translation-tables/index.md` — omits `## Key Results`, uses prose "Navigation note"
- `vol5/common/index.md` — omits `## Key Results`, uses prose "Navigation note"

**Issue:** Neither INVARIANT-S5, INVARIANT-S6, nor the entry-point navigation description defines a machine-readable exception for "pure navigation pointer" index files. An agent relying on "index documents carry a Key Results table" will find a structural mismatch.

**Note:** The navigation itself works; the failure is structural legibility/machine-readability only.

**Fix:** Either add `<!-- index-type: navigation-pointer -->` as a machine-readable exception marker to CLAUDE.md and these two files, or add minimal Key Results rows summarizing what the pointer targets contain.

---

### 4B-STR-N1 (NOTE): `<!-- leaf: placeholder -->` is an undocumented leaf marker variant

**Files:** Both orphaned files in `vol3/condensed-matter/` (addressed by 4B-STR-C1 fix above)

**Issue:** INVARIANT-S5 defines only `<!-- leaf: verbatim -->`. The `<!-- leaf: placeholder -->` variant is not defined.

**Fix:** Addressed by 4B-STR-C1 fix (change to `<!-- leaf: verbatim -->`).

---

## Confirmed Clean

1. **vol1/operators-and-regimes/ bidirectional navigation** — All paths resolve, uplink chains unbroken ✓
2. **vol1/operators-and-regimes/ description accuracy** — Domain index summary matches chapter index content ✓
3. **vol6/period-2/ and vol6/period-3/ element indexes** — All 12 element subdirectories match their indexes ✓
4. **vol5/protein-folding-engine/ depth** — Four levels deep (not five), all indexes correct ✓
5. **common/index.md Key Results** — All four entries link to existing files ✓
6. **CLAUDE.md links** — Three apparent broken links are fenced code examples only; zero real broken paths ✓
7. **vol8/appendix cross-reference** — `../../common/appendix-experiments.md` resolves correctly ✓
8. **Link integrity (comprehensive)** — Zero broken `.md` links outside CLAUDE.md code examples ✓
9. **Entry-point size** — ~1,230 words (~1,640 tokens), well under 3,000-token limit ✓
10. **Up-link conformance** — All 813 non-CLAUDE.md files begin with `[↑ ` on line 1 ✓
