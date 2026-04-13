# Phase 4 Burn-Down List — Iteration 3

**Date:** 2026-04-03
**Files affected:** 9 (2 leaves, 5 index files, 1 CLAUDE.md, 1 vol8/appendix)

---

## Critical Fixes

### C-1: vol2/ch02 `thermal-softening.md` — three `$l_{node}$` → `$\ell_{node}$`

**File:** `ave-kb/vol2/particle-physics/ch02-baryon-sector/thermal-softening.md`

**Source authority:** `vol_2_subatomic/chapters/02_baryon_sector.tex` line 121

**Fix:** In the prose paragraph beginning "Each flux tube is a Gaussian LC resonant loop...", change all three roman-ell occurrences that correspond to source line 121:

| Current (roman) | Correct (script) |
|---|---|
| `FWHM $= l_{node}$` | `FWHM $= \ell_{node}$` |
| `$\sigma = l_{node}/(2\sqrt{2\ln 2})$` | `$\sigma = \ell_{node}/(2\sqrt{2\ln 2})$` |
| `$d = l_{node}/2$` | `$d = \ell_{node}/2$` |

Then in the Topological Inductive Density Threshold resultbox equation (source line 131):

| Current (roman) | Correct (script) |
|---|---|
| `1 + \frac{l_{node}}{8\sqrt{2\ln 2}}` | `1 + \frac{\ell_{node}}{8\sqrt{2\ln 2}}` |

**Do not change** the roman `$l_{node}$` on source line 103 ("By Axiom 1, the Full-Width at Half-Maximum (FWHM) of a fundamental flux tube is $1.0 l_{node}$") — that occurrence is roman in the source and must remain roman.

---

### C-2: vol2/ch02 `self-consistent-mass-oscillator.md` — one `$l_{node}$` → `$\ell_{node}$`

**File:** `ave-kb/vol2/particle-physics/ch02-baryon-sector/self-consistent-mass-oscillator.md`

**Source authority:** `vol_2_subatomic/chapters/02_baryon_sector.tex` line 160

**Fix:** In the Cinquefoil Confinement Bound resultbox equation, change:

| Current (roman) | Correct (script) |
|---|---|
| `\approx 4.97 \; l_{node}` | `\approx 4.97 \; \ell_{node}` |

The surrounding prose on that page does not use `l_{node}` and requires no change.

---

### C-3: vol4/ch3 `n-ave-derivation.md` — append three missing sentences to "Predicted Shifts" paragraph

**File:** `ave-kb/vol4/hardware-programs/ch3-hopf-01-chiral-verification/n-ave-derivation.md`

**Source authority:** `vol_4_engineering/chapters/03_hopf_01_chiral_verification.tex` line 75

**Fix:** After the Predicted Shifts table and the current final sentence ("All shifts exceed 8.5 MHz---easily resolvable with a VNA. All resonant frequencies fall below 1.1 GHz (well within NanoVNA-H4 range)."), append:

```
The $(3,5)$ knot provides an intermediate data point (five knots plus the zero-topology control give six independent measurements). When submerged in mineral oil ($\varepsilon_{eff} \approx 2.265$), frequencies drop to 0.40--0.83 GHz. The ppm values are computed from the exact relation $\Delta f/f = \alpha\,pq/(p+q)\,/\,(1 + \alpha\,pq/(p+q))$.
```

The `---` horizontal rule separating this leaf from the next section must remain after these sentences, not before them.

---

## Warning Fixes

### W-1: CLAUDE.md INVARIANT-N2 — correct per-volume ell convention

**File:** `ave-kb/CLAUDE.md`

**Issue:** INVARIANT-N2 states "All volumes except Vol 1 write `$l_{node}$` (roman ell)." Source grep shows this is wrong for multiple volumes. Confirmed per-volume conventions from source:

| Volume | Dominant notation | Basis |
|---|---|---|
| Vol 1 | script `\ell_{node}` | 52 vs 2 occurrences |
| Vol 2 | script `\ell_{node}` (mixed — some roman per source) | 56 vs 4 occurrences |
| Vol 3 | script `\ell_{node}` (one isolated roman) | 19 vs 1 occurrence |
| Vol 4 | script `\ell_{node}` (some roman per source) | 22 vs 4 occurrences |
| Vol 5 | script `\ell_{node}` | 29 occurrences, 0 roman |
| Vol 6 | roman `l_{node}` (one isolated script) | 1 vs 3 occurrences |
| Vol 7 | roman `l_{node}` (one isolated script) | 1 vs 4 occurrences |
| Vol 8 | not used | 0 occurrences |

**Fix:** Replace the current INVARIANT-N2 body with:

```
### INVARIANT-N2: Lattice node spacing notation (vol-split)

Volumes 1–5 write `$\ell_{node}$` (script ell) as the primary form. Volumes 6–7 write
`$l_{node}$` (roman ell) as the primary form. Vol 8 does not use this symbol. Both vols 2
and 4 contain isolated roman-ell instances in their source; those specific instances must be
preserved as roman (do not normalize to script). Distillers must preserve the source notation
within each volume; do not normalize across volumes.

*Confirmed by: source grep — vol1 (52 script, 2 roman); vol2 (56 script, 4 roman);
vol3 (19 script, 1 roman); vol4 (22 script, 4 roman); vol5 (29 script, 0 roman);
vol6 (1 script, 3 roman); vol7 (1 script, 4 roman); vol8 (0)*
```

---

### W-2: Vol3 domain indexes — convert `## Contents` bullet list to `## Derivations and Detail` table

**Files (all four):**
- `ave-kb/vol3/gravity/index.md`
- `ave-kb/vol3/condensed-matter/index.md`
- `ave-kb/vol3/cosmology/index.md`
- `ave-kb/vol3/applied-physics/index.md`

**Fix:** In each file, replace the `## Contents` heading and its bulleted list with a `## Derivations and Detail` section using a two-column table with `Document | Contents` headers. The existing bullet text maps directly: the link becomes the Document column value; the description after ` — ` becomes the Contents column value.

**Example transformation** (from `condensed-matter/index.md`):

Before:
```markdown
## Contents

- [Ch.9: Condensed Matter and Superconductivity](./ch09-condensed-matter-superconductivity/index.md) — Kuramoto phase-locking, Meissner gear train, $\varepsilon$--$\mu$ duality, type I/II classification, critical field validation
```

After:
```markdown
## Derivations and Detail

| Document | Contents |
|---|---|
| [Ch.9: Condensed Matter and Superconductivity](./ch09-condensed-matter-superconductivity/index.md) | Kuramoto phase-locking, Meissner gear train, $\varepsilon$--$\mu$ duality, type I/II classification, critical field validation |
```

Apply this transformation to all chapter entries in all four files. Key Results sections are already correct — do not modify them.

---

### W-3a: `common/index.md` — add `## Key Results` section

**File:** `ave-kb/common/index.md`

**Ruling:** This index has original navigational function (six children, each containing system-level results). The Key Results section should surface the highest-level system results accessible through this index — specifically results from `full-derivation-chain.md` and `mathematical-closure.md` which contain the system's most significant meta-results.

**Fix:** Insert the following `## Key Results` section between the introductory paragraph and the `## Contents` section:

```markdown
## Key Results

| Result | Location |
|---|---|
| Complete derivation chain: 3 bounding limits + 4 axioms → 8 derivation layers → zero free parameters | [Full Derivation Chain](full-derivation-chain.md) |
| Automated diagnostic confirms strict geometric closure (DAG proof, no free parameters) | [Mathematical Closure](mathematical-closure.md) |
| Universal regime-boundary eigenvalue method applies across BH QNM, nuclear, protein, and semiconductor domains | [Solver Toolchain](solver-toolchain.md) |
| Unified experimental index: hardware benchmarks, astronomical tests, biophysical proposals (all volumes) | [Unified Experiments Appendix](appendix-experiments.md) |
```

---

### W-3b: `common/translation-tables/index.md` — add `## Key Results` section

**File:** `ave-kb/common/translation-tables/index.md`

**Ruling:** This is a pure navigation index for six translation tables. There are no physical results of its own — each table's mappings are results belonging to their respective domain volume. A Key Results section here would either duplicate domain results or be vacuous. **Exempt from Key Results requirement.** Add a structural note instead.

**Fix:** Insert the following between the introductory paragraph and `## Contents`:

```markdown
> **Navigation note:** This index is a navigation pointer to six domain-specific translation tables. Key results are in the destination leaves; this node carries no original results.
```

---

### W-3c: `vol5/common/index.md` — add `## Key Results` section

**File:** `ave-kb/vol5/common/index.md`

**Ruling:** Same as `common/translation-tables/index.md` — this is a navigation index for two vol5-specific translation tables. The tables' rows are the results; this index contributes no independent content. Exempt from Key Results requirement; structural note suffices.

**Fix:** Insert the following between the introductory paragraph and `## Contents`:

```markdown
> **Navigation note:** This index is a navigation pointer to two Vol 5 biology-specific translation tables. Key results are in the destination leaves; this node carries no original results.
```

---

### W-3d: `vol8/appendix/index.md` — add `## Key Results` section and fix uplink

**File:** `ave-kb/vol8/appendix/index.md`

**Fix part 1 — Key Results:** Insert the following between the introductory sentence and `## Contents`:

```markdown
## Key Results

| Result | Statement |
|---|---|
| Vol 8 experimental programme | Vol 8 contributes no original experimental content — see [Unified Experiments Appendix](../../common/appendix-experiments.md) |
```

**Fix part 2 — uplink text (merges N-2):** Line 1 currently reads `[↑ Vol 8: Virtual Media](../index.md)`. Change to:

```markdown
[↑ Vol 8: Virtual Media and Informational Topology](../index.md)
```

---

## Note Fixes

### N-1: CLAUDE.md — add leaf-in-index-file clarification to INVARIANT-S5

**File:** `ave-kb/CLAUDE.md`

**Affected case:** `vol2/appendices/app-c-derivations/index.md` carries `<!-- leaf: verbatim -->` on line 2. This is the only single-file directory in the KB where the index IS the leaf.

**Fix:** Append one sentence to INVARIANT-S5:

```
Exception: when a directory contains only `index.md` (no other files), `index.md` may carry
`<!-- leaf: verbatim -->` on line 2, functioning simultaneously as the directory's navigation
node and its sole leaf. One confirmed instance: `vol2/appendices/app-c-derivations/index.md`.
```

---

## Fix Wave Plan

All fixes are independent — no ordering dependencies.

**Batch 1 (parallel):** C-1, C-2, C-3, W-1, W-2, W-3a, W-3b, W-3c, W-3d, N-1

Note: W-3d subsumes N-2 (the uplink text fix is included within W-3d Fix part 2). N-2 as a standalone item is closed.

---

## Structural Classification

All findings are **Addendum** class (accuracy or formatting fixes; no structural changes required). The INVARIANT-N2 correction (W-1) is Modification class — it corrects a documented convention but does not change any hierarchy topology.

No Backtrack or Hierarchy Redesign items.
