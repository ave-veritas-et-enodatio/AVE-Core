[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Canonical vocabulary register — hosts def- (adjudicated-term) nodes, the third tracked index after the claim graph (clm/exp/sup) and the code-provenance index. def- is a spine node-type SPECIFIED in .index/SCHEMA.md (INVARIANT-S11 extend-don't-reinvent); pipeline materialization into claims.jsonl is Stage 2 (PENDING). This leaf originates no clm-/exp-/sup- node, so it carries no-claim until the def- emitter is wired (Stage 2), at which point hosting def- nodes will satisfy Tier-1 coverage on its own."
path-stable: "the canonical vocabulary-register leaf; docs/glossary.md is its rendered view"
-->

# Vocabulary Register — Adjudicated AVE Terms (`def-` spine index)

The **source-of-truth index** for adjudicated AVE vocabulary. Each entry is a
`def-` node (`\bdef-[a-z0-9]{6}\b`) recording the *locked meaning* of a
load-bearing term, the substrate **axis** it lives on, its **dimension/type**, an
adjudication **status**, the `clm`/`exp`/`sup` ids it is load-bearing for, and —
for an overloaded term — an **open-ambiguity flag** plus the verified file:line
**conflicting sites**. This is the third tracked metadata index after
[`claims.jsonl`](../.index/claims.jsonl) (the `clm`/`exp`/`sup` claim graph) and
the code-provenance index. The node-type is specified in
[`.index/SCHEMA.md`](../.index/SCHEMA.md) ("Definition record") and is a
deliberate spine extension per [`INVARIANT-S11`](../CLAUDE.md) (extend, don't
reinvent — the unified id system is verifier-gated, never a parallel local
scheme).

> **Rendered view.** [`docs/glossary.md`](../../../docs/glossary.md) is the
> human-facing **rendered view** of this register; **this register is the
> source of truth**. When the two disagree, this spine register wins (and the
> glossary is re-synced from it).

> **Stage status.** Stage 1 (this file + the [`.index/SCHEMA.md`](../.index/SCHEMA.md)
> `def-` spec) is **landed**. Stage 2 — wiring `refresh-kb-metadata` to
> materialize each `def-` node into `claims.jsonl` (`node_type: "definition"`)
> and `verify-kb-metadata` to drift-gate them under the same referential-integrity
> pass as `clm`/`exp`/`sup` — is **PENDING** (tracked follow-up). Until Stage 2
> lands, the `def-` namespace is invisible to the pipeline id regexes
> (`clm|exp|sup`), so this register does not perturb the existing build or verify.

> **Seed scope.** This is a **verified SEED**, not the full table. Each term was
> re-derived and re-grepped against the live corpus (verify-before-cite); a term
> whose meaning/cite did not verify is tagged **OPEN**, never **SOLID**. The seed
> is recovered from the §46/§47 soliton-size vocabulary disambiguation
> (`_orchestration/2026-06-07_electron-synthesis-epic.md` §46–§47) — persisting
> that at-risk adjudication into the tracked spine. Remaining §47 clarity-risk
> terms are added as each is individually verified.

## Per-node field legend

Each `## <term>` heading carries a `<!-- id: def-xxxxxx -->` marker and a
field block (parallel to a `claim-quality.md` `### Quality` block, so Stage 2 can
parse it):

- **term** — the surface form.
- **adjudicated-meaning** — the locked meaning (single sentence).
- **axis** — `spatial-Brillouin` | `phase-carrier` | `dimensionless` | `notation` | `other`.
- **dimension/type** — physical dimension or type (e.g. `length (L)`, `frequency (T⁻¹)`, `dimensionless`, `n/a (notation)`).
- **status** — `SOLID` (locked + cite confirms) | `ambiguous` (≥2 corpus meanings, no locked sense, canon gated) | `proposed` (coined, 0 prior corpus hits, gated on review) | `retired` (superseded, preserved per Rule 12).
- **canonical-home** — the leaf:line that grounds the adjudicated meaning (or `(none — coinage)` for a proposed term).
- **clm-cross-links** — verified `clm`/`exp`/`sup` ids the term is load-bearing for (reverse bookkeeping; may be empty).
- **open-ambiguity-flag** — `YES` + conflicting meanings/sites when the surface form is overloaded; `no` otherwise.
- **verification** — the verify-before-cite result for this entry.

---

## node
<!-- id: def-cc2196 -->

- **term:** node
- **adjudicated-meaning:** the spatial-Nyquist sampling boundary of the $\mathcal{M}_A$ lattice — one Brillouin cell at the fundamental pitch $\ell_{node}$, supporting a maximum spatial frequency $k_{max} = \pi/\ell_{node}$ (the Brillouin zone edge).
- **axis:** spatial-Brillouin
- **dimension/type:** length (L); one cell $\ell_{node} \approx 386$ fm
- **status:** SOLID
- **canonical-home:** `vol1/dynamics/ch3-quantum-signal-dynamics/paley-wiener-hilbert.md:10` (corroborated at `vol1/claim-quality.md:801`)
- **clm-cross-links:** clm-yc7fgm
- **open-ambiguity-flag:** YES — the canonical sense above is locked (SOLID), but the surface form "node" is overloaded elsewhere: (a) a **field/wave null** (a zero of the field amplitude) [dimensionless]; (b) a **K4 graph vertex** (the 4-port tetrahedral active site) [notation/graph]. The qualifier **"sub-node" MUST be read as "below $\ell_{node}$ (the cell scale)"**, never as a graph-vertex or null.
  - conflicting sites: graph-vertex / circuit-node usage `docs/glossary.md:20` ("Node | (circuit node) | (lattice point) | … K4 4-port tetrahedral active site"); single-node containment `src/ave/core/semiconductor_binding_engine.py:68` ("the entire nucleus exists inside a single saturated lattice node").
- **verification:** VERIFIED — `paley-wiener-hilbert.md:10` confirms the spatial-Nyquist / Brillouin-cell meaning verbatim; §46 marks "node = spatial Nyquist boundary" spine-supported / canonical. Status SOLID for the locked sense; open-ambiguity-flag records the surface-form overloading (status and open-ambiguity are orthogonal per the SCHEMA Definition-record rule).

---
