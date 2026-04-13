# KB Structure Review — Phase 4 Iteration 1

**Date:** 2026-04-03
**Scope:** `ave-kb/` — 813 files across 8 volumes plus common/

---

## Structure Review Summary

The most critical finding is a dead-end navigation path in `vol2/appendices/app-a-translation-matrix/` for the two protein translation pointer leaves: both claim their canonical content lives in `ave-kb/common/`, but no protein files exist there — the actual canonical content is in `ave-kb/vol5/common/`. An agent following these pointers arrives at a dead end. The second-most-critical finding is that `vol4/index.md` is the only volume-level index missing a Key Results section, violating the index invariant and preventing orientation for agents arriving at vol4 from any path other than the entry-point. Beyond these two, uplink chains are intact throughout, down-link completeness is high across all sampled indexes, all seven known PATH-STABLE documents carry annotations (though three are missing the source volume specification), and GAP stubs are informative and accurate. The vol8 NOTES.md uses a custom `<!-- notes: vol8-local -->` marker not defined in CLAUDE.md, creating an undocumented document type that also escapes the Derivations/Detail table.

---

## Findings

---

### CRITICAL-1: Protein translation pointer leaves route agents to nonexistent content

**Issue:** `vol2/appendices/app-a-translation-matrix/translation-protein.md` and `translation-protein-solver.md` both contain the prose statement "The canonical KB location for the rendered table will be in `ave-kb/common/`." No protein translation files exist in `ave-kb/common/` — they are in `ave-kb/vol5/common/translation-protein.md` and `ave-kb/vol5/common/translation-protein-solver.md`. The `vol2/appendices/app-a-translation-matrix/index.md` repeats this incorrect canonical location in its table under the "Canonical Location" column.

**Location:**
- `vol2/appendices/app-a-translation-matrix/translation-protein.md` body prose
- `vol2/appendices/app-a-translation-matrix/translation-protein-solver.md` body prose
- `vol2/appendices/app-a-translation-matrix/index.md` table column "Canonical Location: `ave-kb/common/`"

**Navigation impact:** An agent navigating the vol2 App A index to find protein translation content will read the pointer leaf, follow the stated canonical location to `ave-kb/common/`, find six physics translation files but no protein files, and have no further navigation signal. The actual content is at `ave-kb/vol5/common/`, which is not linked from any document in `vol2/appendices/app-a-translation-matrix/`.

**Avoidance requirement:** Every pointer leaf that states a canonical location must state the location where that content actually exists in the distilled KB. The canonical location claim in both protein pointer leaves must match the actual path `ave-kb/vol5/common/` where those files reside.

---

### CRITICAL-2: vol4/index.md has no Key Results section

**Issue:** `vol4/index.md` is the only volume-level index in the KB without a `## Key Results` section. All other seven volume indexes carry this section. The vol4 index goes directly from the volume description to the `## Domains` table.

**Location:** `vol4/index.md` — no `## Key Results` section.

**Navigation impact:** An agent arriving at `vol4/index.md` from any path other than the entry-point (which does include vol4 key results inline) receives no summary of what vol4 concludes before having to choose a domain. Every other volume provides this orientation at the volume-index level. An agent trying to answer a question about vol4's main results must descend into a domain before encountering any results.

**Avoidance requirement:** Every volume-level index must contain a `## Key Results` table populated with at least one entry per domain, so that an agent arriving at that index without prior context can route to the correct subdomain without reading all domain descriptions.

---

### CRITICAL-3: vol2/appendices/app-c-derivations/index.md is a leaf without a leaf marker

**Issue:** `vol2/appendices/app-c-derivations/` contains only `index.md` — no child files. The document contains verbatim leaf content (hardware substrate parameters, signal dynamics formulas, cosmological dynamics constants) but carries neither `<!-- leaf: verbatim -->` on line 2 (required by INVARIANT-S5) nor a `## Derivations and Detail` table. Line 2 is `<!-- Anomaly A10: App C has no \label in source... -->`, an internal distiller note, not a structural marker.

**Location:** `vol2/appendices/app-c-derivations/index.md` lines 1–2.

**Navigation impact:** A machine check for the leaf marker will miss this document. An agent or maintenance pass checking "index files without a Derivations/Detail table" will flag this as a broken index (one that has lost its children) rather than an intentional terminal leaf. The Anomaly A10 comment provides no machine-checkable signal about document type.

**Avoidance requirement:** Any document that contains verbatim leaf content and has no children must carry `<!-- leaf: verbatim -->` on line 2, regardless of whether the file is named `index.md`. When an appendix section's entire content fits in a single file, that file is a leaf and must be marked accordingly.

---

### WARNING-1: Three PATH-STABLE annotations on vol4 falsification leaves are missing the source volume

**Issue:** The three PATH-STABLE falsification leaves carry annotations in the form `<!-- path-stable: referenced as sec:X -->` without specifying the referencing volume. The canonical format (as used by vol1, vol4/k4-tlm, and vol5 PATH-STABLE documents) is `referenced from {vol} as {label}`.

**Location:**
- `vol4/falsification/ch11-experimental-bench-falsification/achromatic-lens-test.md` line 3: `<!-- path-stable: referenced as sec:achromatic_lens -->`
- `vol4/falsification/ch11-experimental-bench-falsification/boundary-trapping-test.md` line 3: `<!-- path-stable: referenced as sec:boundary_trapping -->`
- `vol4/falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md` line 3: `<!-- path-stable: referenced as sec:induced_vacuum_impedance_mirror -->`

**Navigation impact:** An agent cannot determine which volume holds the cross-reference without a separate search. The correct referencing volume is vol3.

**Avoidance requirement:** Every PATH-STABLE annotation must specify the referencing volume in the form `referenced from {vol} as {label}`.

---

### WARNING-2: vol8/NOTES.md uses an undocumented document-type marker and escapes the Derivations/Detail table

**Issue:** `vol8/NOTES.md` carries `<!-- notes: vol8-local -->` on line 2. This marker is not defined in CLAUDE.md and is not one of the two recognised line-2 patterns (absent for indexes, `<!-- leaf: verbatim -->` for leaves). Additionally, NOTES.md is listed in the `vol8/index.md` Contents bullet list but NOT in the `## Derivations and Detail` table.

**Location:** `vol8/NOTES.md` line 2; `vol8/index.md` lines 29–36 (Contents bullet only).

**Navigation impact:** An agent traversing vol8 via Derivations/Detail tables — the standard descent path — will never reach NOTES.md. The document contains cross-cutting operational information for vol8 (raw-form notation policy, pending-autotune markers for three specific leaves, Z-proportionality inversion scope) that affects correct interpretation of vol8 leaf content.

**Avoidance requirement:** Every document in the KB tree must use one of the two recognised line-2 markers. Every child document must appear in its parent index's Derivations and Detail table.

---

### WARNING-3: vol8/appendix is excluded from the Derivations and Detail table

**Issue:** `vol8/appendix/index.md` and its child `unified-experiments-ref.md` are reachable only via a Contents bullet list in `vol8/index.md`, not via the `## Derivations and Detail` table.

**Location:** `vol8/index.md` line 35 (bullet only): `- [Appendix](appendix/index.md)`.

**Navigation impact:** Table-driven traversal from `vol8/index.md` misses the appendix subtree entirely.

**Avoidance requirement:** Every child directory or document must appear in the parent index's Derivations and Detail table. Contents bullet lists are supplemental and not a substitute for table-driven down-links.

---

### WARNING-4: Several cross-volume "See also" references use unresolved source labels without hyperlinks

**Issue:** Multiple leaves in `vol3/condensed-matter/ch11-thermodynamics/` and `vol3/applied-physics/ch07-stellar-interiors/` carry `> ↗ See also:` annotations using bare LaTeX labels (e.g., `` `ch:quantum_computing` ``, `` `ch:regime_map` ``, `` `ch:fundamental_axioms` ``, `` `ch:baryons` ``) without a resolved relative-path hyperlink.

**Location (sample):**
- `vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md`
- `vol3/condensed-matter/ch11-thermodynamics/baryon-asymmetry-derivation.md`
- `vol3/applied-physics/ch07-stellar-interiors/stellar-regime-classification.md`
- `vol3/condensed-matter/ch11-thermodynamics/index.md`

**Navigation impact:** An agent reading these cross-references cannot navigate to the referenced content. The label provides a naming hint but not a traversable link.

**Avoidance requirement:** Every `> ↗ See also:` annotation must contain a functional relative path to the referenced document. Bare LaTeX source labels must either be resolved to actual KB paths or removed.

---

### WARNING-5: vol2/appendices/app-a-translation-matrix/index.md has no Key Results section

**Issue:** The App A translation matrix index has a "Translation Tables" contents table and a "Parameter Accounting" section, but no `## Key Results` section. This is a subtopic-level index and the structural invariant requires a Key Results section.

**Location:** `vol2/appendices/app-a-translation-matrix/index.md` — no `## Key Results` heading.

**Navigation impact:** An agent arriving at App A expecting the standard index format will not find a Key Results section and must parse the Parameter Accounting prose section to understand what this appendix concludes.

**Avoidance requirement:** Every subtopic index must carry a `## Key Results` section.

---

### NOTE-1: vol8/appendix/unified-experiments-ref.md uses a non-standard leaf marker

**Issue:** This leaf carries `<!-- leaf: cross-ref -->` on line 2 instead of `<!-- leaf: verbatim -->`.

**Location:** `vol8/appendix/unified-experiments-ref.md` line 2.

**Avoidance requirement:** All leaf documents must use `<!-- leaf: verbatim -->` on line 2.

---

### NOTE-2: common/ PATH-STABLE annotations use a different format than vol-level PATH-STABLE documents

**Issue:** The five PATH-STABLE files in `common/` carry annotations in the form `<!-- path-stable: label app:X -->` rather than `referenced from {vol} as {label}`. These do not name a referencing volume.

**Location:** `common/appendix-experiments.md`, `common/full-derivation-chain.md`, `common/mathematical-closure.md`, `common/solver-toolchain.md`, `common/appendices-overview.md` — all on line 3.

**Avoidance requirement:** PATH-STABLE annotations should use consistent format across all files.

---

### NOTE-3: PATH-STABLE placement for non-leaf indexes is undocumented in CLAUDE.md

**Issue:** For a chapter index (non-leaf), the PATH-STABLE annotation lands on line 2 (uplink on line 1, path-stable on line 2), because there is no leaf marker occupying line 2. CLAUDE.md describes PATH-STABLE as "line 3" in the context of leaf documents. The index case (line 2) is structurally correct but the two-case rule is not stated.

**Location:** `vol2/quantum-orbitals/ch07-quantum-mechanics/index.md` lines 1–2.

**Avoidance requirement:** CLAUDE.md should explicitly distinguish PATH-STABLE placement for leaf (line 3) vs. index (line 2) documents.

---

## Confirmed Clean

- All uplink chains sampled resolve to entry-point without breaks: vol1, vol6 (fluorine), vol8, vol5 protein-folding-engine, common/ tree.
- Down-link completeness verified exhaustively for: vol2/ch07 (20/20), vol5/deterministic-folding (15/15), vol5/network-solver (28/28), vol4/ch11 (23/23), vol4/ch13 (5/5), vol5/biological-applications (6/6), vol6/period-3/sodium (7/7).
- GAP stubs (fluorine, neon, silicon orbital-knot/semiconductor-regime): all carry informative comments.
- Vol6 anomaly handling: Fluorine, Neon, Silicon indexes correctly list non-standard and GAP stub leaves.
- Na/Mg/Al extra §3 leaves: all listed in respective element indexes.
- Entry-point: links to all 8 volume indexes and common/index.md; under 3000 tokens.
- Cross-volume links resolved: vol3/gravity/ch02 → common/translation-gravity (verified), vol3/gravity/ch02 → vol4/k4-tlm-simulator (verified).
- vol5/common/index.md, vol8/appendix/index.md, common/index.md: no Key Results appropriate (navigation-only indexes).

---

## Out of Scope

- Content accuracy — structure and navigation only.
- Exhaustive down-link enumeration across all 813 files.
- DANGLING REFS comments in leaf documents — distiller notes about unresolved LaTeX cross-references within source.
