# AVE KB — Format Conventions

Spec document for anyone adding, editing, or auditing KB content. Authoritative source for structural decisions: `CLAUDE.md` (cross-cutting invariants). This document covers format and process; `CLAUDE.md` covers physical notation and cross-volume constants.

---

## Document Types

### Leaf

A verbatim LaTeX→Markdown translation of one source section. Structure:

```
Line 1: [↑ Parent Name](../index.md)
Line 2: <!-- leaf: verbatim -->
Line 3: <!-- path-stable: referenced from {vol} as {label} -->  (if PATH-STABLE)
Line 4: (blank)
         ... content ...
```

Content must not introduce editorial interpretation. Equations, table values, and phrasing are taken directly from the source.

**Exception:** When a directory contains only `index.md` with no sibling leaves, `index.md` may carry `<!-- leaf: verbatim -->` on line 2, serving simultaneously as navigation node and sole leaf. One confirmed instance: `vol2/appendices/app-c-derivations/index.md`.

### Index (chapter / domain / volume / entry-point)

A navigation node. Structure:

```
Line 1: [↑ Parent Name](../index.md)   (omitted for entry-point.md only)
Line 2: <!-- path-stable: ... -->      (if PATH-STABLE; no blank line before it)

# Chapter/Domain/Volume Title

Brief description paragraph (optional).

## Key Results

| Concept | Result |
|---|---|
| ... | ... |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Title](path.md) | One-line description |
```

Key Results content is verbatim from the source. Derivations and Detail links must stay in sync when children are added or removed.

**Navigation-pointer index exception:** An index that contains no original results — only pointers to child leaves — may replace `## Key Results` with a `> **Navigation note:**` blockquote stating explicitly that results reside in the destination leaves. Two confirmed instances: `common/translation-tables/index.md`, `vol5/common/index.md`. Absence of `## Key Results` is not a defect if a Navigation note is present.

---

## Structural Annotations

### Up-link (INVARIANT-S4)

Every document except `entry-point.md` begins on line 1 with exactly one up-link:

```markdown
[↑ Parent Name](../index.md)
```

The `↑` character is U+2191. The link validator checks for `^\[↑ ` pattern. Multiple up-links or a missing up-link are defects.

### Leaf marker (INVARIANT-S5)

Line 2 of every leaf document:

```markdown
<!-- leaf: verbatim -->
```

### PATH-STABLE annotation (INVARIANT-S6)

Documents that are cross-volume reference targets carry:

```markdown
<!-- path-stable: referenced from {vol} as {label} -->
```

Placement is immediately after the last structural annotation, with no blank line between annotations:

- Leaf: line 3 (after `<!-- leaf: verbatim -->`)
- Index: line 2 (after the up-link)

---

## tcolorbox Rendering (INVARIANT-S1)

All tcolorbox environments render as named blockquotes with a bold environment-type prefix. General pattern:

```markdown
> **[Resultbox]** *Title of the Result*
>
> Body content...
```

The blank `>` line between the title line and the body is required — omitting it collapses title and body into a single paragraph in most Markdown renderers.

| LaTeX environment | Markdown prefix |
|---|---|
| `resultbox` | `**[Resultbox]**` |
| `axiombox` | `**[Axiombox]**` |
| `summarybox` | `**[Summarybox]**` |
| `exercisebox` | `**[Exercisebox]**` |
| `simbox` | `**[Simbox]**` |
| `examplebox` | `**[Examplebox]**` |
| `circuitbox` | `**[Circuitbox]**` |
| `codebox` | `**[Codebox]**` |
| `objectivebox` | `**[Objectivebox]**` |

Resultbox is the most common environment. Vol 5 uses only resultbox. Vol 8 uses none. Individual volumes may use only a subset; render whatever is present in the source using this pattern.

**Summarybox and exercisebox omission:** Some chapter indexes carry this note: `NOTE: summarybox and exercisebox environments are not extracted as leaves.` This is standard practice for those environment types where the source material is summary or practice content rather than primary results.

---

## Math Rendering

- Display math: `$$...$$`
- Inline math: `$...$`
- Do not carry LaTeX macros into KB output. Always expand to explicit notation (e.g., `$\mathcal{M}_A$` not `$\vacuum$`).
- Preserve source notation within each volume — do not normalize across volumes. In particular, lattice node spacing uses `$\ell_{node}$` (script ell) in vols 1–5 and `$l_{node}$` (roman ell) in vols 6–7. Isolated roman-ell instances in vols 2 and 4 must be preserved as roman. See INVARIANT-N2 in `CLAUDE.md`.

---

## Cross-Volume Reference Format

References appear at the bottom of index and leaf documents where the source text explicitly references another section.

Required dependency:

```markdown
> → Primary: [Document Name](relative/path/to/target.md) — brief rationale (source label if known)
```

Optional suggestion:

```markdown
> ↗ See also: [Document Name](relative/path/to/target.md) — brief rationale
```

Cross-volume references must not paraphrase or summarize the target content.

---

## Adding New Content

1. One file per source section (resultbox boundary or natural section break in the source).
2. Line 1: up-link to parent index.
3. Line 2: `<!-- leaf: verbatim -->` (for leaves).
4. Add a row to the parent's `## Derivations and Detail` table.
5. If the new content introduces a Key Result not already in the parent's `## Key Results` table, propagate it upward through the index hierarchy.
6. If the document is a cross-volume reference target, add the PATH-STABLE annotation on line 3 (leaf) or line 2 (index).

**Navigation-pointer index exception:** If a new index contains no original results — it exists solely to point to child leaves that carry results — use the navigation-pointer exception pattern: replace `## Key Results` with a `> **Navigation note:**` blockquote that explicitly states results reside in the destination leaves. Do not add a `## Key Results` table that would be empty or misleading.

---

## Auditing

### Link validator

`/tmp/check_links.py` — checks for broken links, missing up-links, and multiple up-links. Run before committing structural changes.

Known false positives: three broken-link reports in `CLAUDE.md` are template syntax examples (`{vol}`, `{label}` placeholders), not actual links. Do not fix them.

### Content checks

```
grep -r '## Resultbox:' ave-kb/
```
Must return zero hits. All resultbox environments must use the blockquote format (`> **[Resultbox]**`), not a heading.

```
grep -r 'leaf: placeholder' ave-kb/
```
Must return zero hits. Placeholder leaves must be replaced with verbatim content before a document is considered complete.

---

## Notation Invariants Summary

See `CLAUDE.md` for full definitions. Quick reference:

| Invariant | Rule |
|---|---|
| N1 | Vacuum medium is `$\mathcal{M}_A$` — never use `\vacuum` macro |
| N2 | Lattice spacing: script `$\ell_{node}$` in vols 1–5, roman `$l_{node}$` in vols 6–7 |
| N3 | Topological operators are named OpN (Op2, Op3, Op4, Op8, Op9, Op14) |
| N4 | `$S_{11}$` means reflection coefficient in vol 4/vol 7; folding objective function in vol 5 |
| S1 | tcolorbox environments render as `> **[Type]** *Title*` blockquotes with a blank `>` line between title and body; see INVARIANT-S1 in `CLAUDE.md` |
| S2 | Four AVE axioms carry stable cross-volume meanings — do not redefine |
