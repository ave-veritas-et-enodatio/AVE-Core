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

### Claim Quality Sidecar (INVARIANT-S7)

A derived artifact that records the per-claim status of the framework's load-bearing claims for a volume (or for the whole KB at the cross-cutting level): what is claimed, what is NOT claimed, how confident we are in each claim locally, how solidly each claim can be built on (given its dependencies), and what work would strengthen it. Sidecars exist because index and entry-point documents are *summaries* of leaves, and a summary may suggest implications not actually supported by the leaves OR may obscure how solid those implications are. The sidecar identifies, per principle/equation/result, both the boundaries (claims and non-claims) and the quality (confidence, solidity, dependency chain, strengthen-by) of each.

Locations:
- Cross-cutting (project-wide tripwires that appear in two or more volumes): `claim-quality.md` (KB root)
- Per volume: `volN/claim-quality.md` and `common/claim-quality.md`

Structure:

```
Line 1: # [Scope] — Claim Quality
Line 2: (blank)
Line 3: <!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from {scope}/index.md bootstrap directive -->
Line 4: (blank)
Line 5: > **Canonicality:** (preamble — see canonicality preamble below)
Line 6: (blank)
        ... entries ...
```

Note: this differs from INVARIANT-S6's index-document line-2 placement for PATH-STABLE. Sidecars carry no up-link, so the annotation sits below the H1 with a blank-line separator for readability. Convention spec §3 is the authoritative source for this placement.

Sidecar files **do not** carry an up-link. They are not navigation nodes in the leaf/index tree; they are referenced only via bootstrap directives in `entry-point.md` and `volN/index.md`.

Entry format (principle-keyed):

```markdown
## [Principle / Equation / Constant Name]
<!-- id: <6-char-alphanumeric> -->

- [formula/equation/constant — if necessary]
- _Specific Claims_
  - [Claim 1]
  - ...
- _Specific Non-Claims and Caveats_
  - [Non-claim or caveat 1]
  - ...

> **Leaf references:** [honest provenance — leaves where the claim is established, OR CLAUDE.md / LIVING_REFERENCE.md when the bound lives at invariant level rather than in any leaf]

## Quality
- confidence: 0.X
- depends-on:
  - <other-id> — Other Entry Title (solidity 0.X)
  - [...]
- solidity: 0.X (build-status phrase)
- rationale: one-sentence statement of why
- strengthen-by:
  - [specific work that would raise confidence or close a dependency]
  - [...]
```

The Quality Convention preamble at the top of the cross-cutting `claim-quality.md` is the canonical spec for the confidence rubric, the solidity computation rule (`solidity = confidence × min(dependency solidity)` for entries with dependencies; `solidity = confidence` otherwise), the build-status legend, and the 6-character stable-ID format. Read that preamble before editing or scoring entries; this section gives the format only.

Canonicality preamble (cross-cutting sidecar — verbatim):

```markdown
> **Canonicality preamble.** Leaves are canonical. Intermediate, index, and entry-point nodes are derived summaries and may suggest implications not supported by the leaves. Each entry below identifies a principle the AVE framework asserts and bounds it precisely: what is claimed, and what is NOT claimed even though a summary or external reading might suggest it.
```

Canonicality preamble (volume sidecar — short reference):

```markdown
> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting claim-quality register](../claim-quality.md) for the full preamble and the canonical list of project-wide tripwires (the cross-cutting sidecar is the source of truth; do not infer the list from this preamble). Entries below are scoped to Vol N; cross-cutting tripwires with vol N-specific manifestations are noted but not duplicated.
```

Sourcing rule (priority order):
1. Leaves under the sidecar's scope (canonical primary source).
2. CLAUDE.md invariants — when a bound is asserted at structural-invariant level but not explicitly stated in any leaf.
3. LIVING_REFERENCE.md "Common Pitfalls" / "Critical Distinctions" — explicit project-wide tripwires.
4. Master Prediction Table classification note — for the meta-tripwire about reading prediction-table cells.

Indexes are NEVER a source for claim entries (circular: indexes are what's being bounded).

Provenance honesty: every entry's "Leaf references" footer must honestly identify the source. Inventing leaf citations for content that does not appear in the cited leaf is a Critical error.

Routing rule (cross-cutting vs volume-specific): a claim-quality entry goes in the cross-cutting sidecar if the claim appears in two or more volumes' leaves as a tripwire; otherwise volume-specific.

Sidecar-vs-leaf contradiction resolution: leaves win; the sidecar gets fixed.

#### Bootstrap directive (required on `entry-point.md` and every `volN/index.md` and `common/index.md`)

Sidecars are discovered through bootstrap directives placed at the top of `entry-point.md` and every volume `index.md`. Without the directive, a consumer reading the index will not know to load the sidecar. Placement is **line 3** of a volume `index.md` (after the line-1 up-link and a line-2 blank), or near-top of `entry-point.md` (after the H1).

For `volN/index.md` and `common/index.md`:

```markdown
[↑ AVE Knowledge Base](../entry-point.md)

> ⛔ **Bootstrap.** Leaves are canonical; this index and the entry-point are *derived* summaries and may suggest implications not supported by the leaves. Before forming any claim about results in this volume, load [`./claim-quality.md`](./claim-quality.md) and [`../claim-quality.md`](../claim-quality.md). Treat the summary text and Key Results entries below as routing only — qualifications and conditions live in the cited leaves and the claim-quality documents.
```

For subtopic-level `index.md` (one level below volume), relative paths shift by one:

```markdown
> ⛔ **Bootstrap.** ... load [`../claim-quality.md`](../claim-quality.md) (volume scope) and [`../../claim-quality.md`](../../claim-quality.md) (cross-cutting). ...
```

For `entry-point.md` (no up-link):

```markdown
# Applied Vacuum Engineering — Knowledge Base

> ⛔ **Bootstrap.** Leaves are canonical; the volume indexes and this entry-point are *derived* summaries and may suggest implications not supported by the leaves. Before forming any claim about AVE results, load [`./claim-quality.md`](./claim-quality.md) (cross-cutting) and the relevant per-volume sidecar: [vol1](./vol1/claim-quality.md), [vol2](./vol2/claim-quality.md), ... [common](./common/claim-quality.md). Treat the summary text below as routing only — qualifications and conditions live in the cited leaves and the claim-quality documents.
```

Marker character: `⛔` (U+26D4). Form is blockquoted, imperative, single-paragraph. The marker is the machine-checkable signal that a directive is present (`grep -l "⛔ \*\*Bootstrap"`).

#### Maintenance cadence

Sidecars are derived artifacts. Refresh when:
- A leaf under the sidecar's scope is added, edited, or removed.
- `LIVING_REFERENCE.md` "Common Pitfalls" or "Critical Distinctions" is added or revised.
- A MAD review surfaces a new tripwire.

Refresh is the same cadence as summary-mode distillation. Until `kb-content-distiller` carries an explicit Claim-Quality Mode (see `CLAUDE.md` INVARIANT-S7 followups), refresh requires a one-off `generalist-coder` dispatch with a custom brief that points at the convention spec sections above.

#### Compactness budget

Per-volume sidecars target **under ~500 lines**. This is a validation criterion, not a hard cap. If a volume sidecar materially exceeds the budget, the sidecar architecture should be reconsidered (the per-subtopic embedded-section approach was the rejected alternative; reopening it is appropriate if the sidecar form scales poorly).

Worked-example entries demonstrating the format on real principles live in `claim-quality.md` (cross-cutting sidecar) — the four original entries (Master Prediction Table reading conventions, Symmetric vs Asymmetric Saturation, α Invariance under Symmetric Gravity, BCS $B_c(T)$ axiom manifestation) are the canonical references for entry style.

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
| S7 | Leaves are canonical; index/entry-point are derived. Cross-cutting bounds in `claim-quality.md` (KB root); per-volume bounds in `volN/claim-quality.md`. Bootstrap directives in entry-point and volume indexes are binding |
