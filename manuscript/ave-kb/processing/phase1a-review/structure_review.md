# Phase 1a — Structure Feasibility Review

**Reviewer:** kb-structure-reviewer
**Date:** 2026-04-02
**Input:** canonical_taxonomy.md + vol{1-8}_taxonomy.md

---

## Summary

**3 Critical / 6 Warning / 5 Info**

The most critical structural failure is a **common/ tree mismatch**: the vol1 taxonomy proposes a substantially larger and differently-named `common/` tree than the canonical synthesis, creating orphaned file positions and broken down-links before a single leaf is written. Two additional Critical findings: the Vol 6 `geometric-inevitability` dangling refs to Vol 1 (`eq:H_infinity`, `sec:galactic_saturation`) have no confirmed target paths in the canonical skeleton — the PATH-STABLE table is explicitly incomplete and will produce broken `> → Primary:` links at distillation time; and the two `vol5/common/` leaves have no parent index that explicitly links to them in the canonical skeleton, making them orphan candidates under AC-NAV-4.

---

## Critical Findings

### C1: common/ tree definition conflict between vol1_taxonomy and canonical skeleton

**Location:** `vol1_taxonomy.md` §3 skeleton vs. `canonical_taxonomy.md` §3.1

**Problem:** The vol1 taxonomy proposes 14 leaf files under `common/`, including files absent from the canonical skeleton:
- `common/full-derivation-chain.md` (vol1 proposes; canonical omits)
- `common/geometric-inevitability.md` (vol1 proposes; canonical omits — Vol 6 owns this content at `vol6/appendix/geometric-inevitability/`)
- `common/mathematical-closure.md` (vol1 proposes; canonical omits)
- `common/solver-toolchain.md` (vol1 proposes; canonical omits)
- `common/appendices-overview.md` (vol1 proposes; canonical omits)
- Filename conflict: `common/experiments-appendix.md` (vol1 slug) vs. `common/appendix-experiments.md` (canonical slug) — same content, different filenames; vol1's acceptance criteria reference `experiments-appendix.md` which will not exist
- Translation table domain mismatch: vol1 proposes `translation-em.md`, `translation-nuclear.md`, `translation-thermo.md`, `translation-bcs.md`, `translation-galactic.md`, `translation-grav-waves.md`; canonical proposes `translation-circuit.md`, `translation-qm.md`, `translation-particle-physics.md`, `translation-gravity.md`, `translation-cosmology.md`, `translation-condensed-matter.md` — different domain names, different file slugs

Additionally, the vol1 taxonomy places Ch.0 at `vol1/ch0-intro.md` (direct child of `vol1/`, up-link to `vol1/index.md`), while the canonical skeleton places it at `vol1/axioms-and-lattice/ch0-preface-foundations.md` (child of the domain, up-link to `axioms-and-lattice/index.md`). These are different paths.

**Impact:** The vol1 taxonomy's `common/index.md` Contents section will link to files that do not exist in the canonical tree. Every vol1 chapter leaf that points to a `common/` translation table will use a broken path. Because `common/` is cross-volume, this structural mismatch is not isolated to vol1 — it is a dependency failure for the entire KB.

**Required fix:** The canonical skeleton must be designated authoritative for all `common/` content and every per-volume taxonomy's `common/` references must be superseded by the canonical list. A definitive file list (slugs, not just domain names) must be issued to all distillers before Phase 4 begins. The vol1 ch0 placement must be resolved to a single canonical path (`vol1/ch0-intro.md` per vol1 taxonomy architect's explicit design intent).

---

### C2: Vol 6 geometric-inevitability cross-references have no confirmed Vol 1 target paths

**Location:** `canonical_taxonomy.md` §4, row "Vol 6 → Vol 1" (`eq:H_infinity`, `sec:galactic_saturation`); `vol6_taxonomy.md` §4 Navigation Spec

**Problem:** The canonical §4 PATH-STABLE table explicitly states: `ave-kb/vol1/ (exact path: vol1 taxonomy architect to confirm)`. This is an unresolved placeholder. A placeholder is not a stable path.

Reading `vol1_taxonomy.md` §3 skeleton directly, the confirmed source of both references is:
- `mond-hoop-stress.md` in `vol1/dynamics/ch4-continuum-electrodynamics/`
- Source: `ch.4 §"Deriving MOND from Unruh-Hawking Hoop Stress" (label: sec:galactic_saturation); $a_{genesis}=cH_\infty/2\pi$; eq:H_infinity`

Confirmed stable paths:
- `eq:H_infinity` → `ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md`
- `sec:galactic_saturation` → `ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md`

Note: the canonical taxonomy §3.2 uses the slug `ch4-field-regimes/` — but the actual vol1 taxonomy uses `ch4-continuum-electrodynamics/`. This chapter slug inconsistency must also be fixed.

**Impact:** The `geometric-inevitability/index.md` will be written with a broken `> → Primary:` link. An agent following this link from Vol 6 arrives at a path that does not exist.

**Required fix:** Before Phase 1b sign-off, the canonical §4 table must be completed with the confirmed paths above. The `ch4-field-regimes` slug must be corrected to `ch4-continuum-electrodynamics` throughout the canonical skeleton. These paths must carry `<!-- path-stable: referenced from vol6 as eq:H_infinity / sec:galactic_saturation -->` comments, and acceptance criteria AC-ANCHOR-7 and AC-ANCHOR-8 must be added.

---

### C3: Vol 5 common/ leaves have no confirmed parent down-link

**Location:** `canonical_taxonomy.md` §3.6 (Vol 5 skeleton shows `vol5/common/` with two leaves); `vol5_taxonomy.md` §3; `canonical_taxonomy.md` §5.1 (up-link table specifies `vol5/common/{leaf}.md` → `vol5/index.md`)

**Problem:** The canonical skeleton shows `vol5/common/translation-protein.md` and `vol5/common/translation-protein-solver.md` as leaves with up-links to `vol5/index.md`. However, no specification states that `vol5/index.md` must include a Contents entry linking down to these files, and no `vol5/common/index.md` exists in the skeleton. AC-NAV-4 requires every file to be linked from exactly one parent. These two leaves have up-links (valid), but without a confirmed down-link from any parent index, they will be orphaned — reachable by traversal but not discoverable by forward navigation.

**Impact:** An agent reading `vol5/index.md` and following all Contents links will never be directed to the protein translation tables.

**Required fix:** Either (a) `vol5/index.md` must include explicit Contents entries for both files, or (b) a `vol5/common/index.md` must be created with an up-link to `vol5/index.md`, and `vol5/index.md` must link to `vol5/common/index.md`. The latter is structurally cleaner and consistent with how `common/translation-tables/` is handled at the root level.

---

## Warning Findings

### W1: INVARIANT-N5 (Vol 8 raw notation) is volume-specific and misclassified in CLAUDE.md

**Location:** `canonical_taxonomy.md` §1.1, INVARIANT-N5

**Problem:** INVARIANT-N5 is placed in §1 (CLAUDE.md invariants section) while simultaneously noting "Vol-8-local." This is self-contradictory. The vol8 taxonomy correctly identifies this as a `vol8/NOTES.md` item.

**Required fix:** Remove INVARIANT-N5 from CLAUDE.md invariants. Place it in `vol8/NOTES.md` only. Add a cross-navigation note in `vol8/index.md` directing readers to NOTES.md for notation policy.

---

### W2: Vol 1 Ch.0 placement is unresolved between vol1 taxonomy and canonical skeleton

**Location:** Vol1 taxonomy says `vol1/ch0-intro.md` (root level). Canonical says `vol1/axioms-and-lattice/ch0-preface-foundations.md`.

**Required fix:** Use `vol1/ch0-intro.md` — the vol1 taxonomy architect explicitly designed Ch.0 as a root-level standalone leaf. `vol1/index.md` Contents must list it explicitly.

---

### W3: Vol 3 translation table design conflicts with canonical skeleton

**Location:** `vol3_taxonomy.md` §3 and AC9 assume a single `common/translation-tables.md`. Canonical uses a subdirectory with 6 separate leaf files.

**Required fix:** Vol3 distiller dispatch must specify canonical per-domain translation leaf paths. Vol3 AC9 must be replaced with one matching the canonical structure.

---

### W4: Vol 8 NOTES.md lacks a defined structural type and parent down-link specification

**Location:** `canonical_taxonomy.md` §3.9 type: `[vol8-local]`; no content specification

**Required fix:** Define `[vol8-local]` type with content marker `<!-- notes: vol8-local -->`, and require `vol8/index.md` Contents section to include an explicit entry for NOTES.md.

---

### W5: Key Results population strategy undefined for Vol 8 (no resultboxes)

**Location:** `canonical_taxonomy.md` §5.3 requires verbatim Key Results; vol8 has zero resultboxes

**Required fix:** Define a Key Results strategy for Vol 8: use verbatim section-header claims and the two labelled equations as Key Results anchors. Formal exemption from the resultbox-sourced Key Results requirement, with an explicit substitution rule, must be stated in the vol8 distiller dispatch.

---

### W6: Entry-point word budget has zero margin

**Location:** `canonical_taxonomy.md` §2.3 (≤2200 words for entry-point)

**Required fix:** Specify per-volume paragraph limit (200 words maximum per volume) with 400 words of structural headroom (navigation text, common/ entry, header). Total: 8×200 + 400 = 2000 ≤ 2200. Alternatively raise ceiling to 3000 words (matching vol1 taxonomy original spec) with per-volume limit of 300 words.

---

## Info Findings

### I1: Vol 2 quantum-orbitals index doubles as domain and chapter index — word-count risk

Domain/chapter combined index must surface Key Results from 14 subsections. Risk of exceeding 2200-word budget. Vol2 distiller dispatch must include an explicit word-count constraint for this index.

---

### I2: Vol 5 fifth-level depth confirmed compliant

Traced leaf `vol5/protein-folding-engine/network-solver/alzheimers-impedance.md`: 4 up-link hops to entry-point. Exception is self-consistent. No action required.

---

### I3: Vol 6 framework/computational-mass-defect depth confirmed compliant

Path depth = 4 levels below `ave-kb/`. `awk -F/ 'NF>7'` check passes. No action required.

---

### I4: Vol 1 proposed invariants not in canonical synthesis need distiller guidance

Several vol1-proposed invariants (`eq:master_wave`, "Four Universal Regimes", Topo-Kinematic Isomorphism table) were not accepted into CLAUDE.md. The vol1 distiller needs explicit guidance that these belong in `vol1/dynamics/` and `vol1/operators-and-regimes/` domain indexes, not CLAUDE.md.

---

### I5: Vol 8 appendix pointer leaf uses non-standard marker `<!-- leaf: cross-ref -->`

Content minimum must be defined: up-link on line 1, marker on line 2, one `> → Primary:` pointer. No other content. This must be stated in vol8 distiller dispatch.

---

## Sign-off

**Needs revision — return to taxonomy architect.**

Three blocking issues must be resolved before Phase 1b: (1) common/ tree unified with authoritative file list; (2) Vol 6 → Vol 1 cross-reference paths confirmed and added to PATH-STABLE table; (3) vol5/common/ orphan risk resolved via vol5/common/index.md. Six Warning findings addressed as distiller-dispatch guidance items. Revision cycle 1 of 2.
