# AVE Knowledge Base — Cross-Cutting Invariants

The following invariants are confirmed genuinely cross-cutting: each appears in two or more volumes and requires no qualification when applied to any single volume. These belong here and must NOT be duplicated in domain documents.

---

## Notation and Rendering

### INVARIANT-N1: Vacuum medium notation

$\mathcal{M}_A$ denotes the vacuum medium. Written directly in body text; do NOT use `\vacuum` macro (macro exists but is not used in chapter bodies across any volume). KB distillers must render as `$\mathcal{M}_A$` throughout.

*Confirmed by: vol1, vol2, vol3, vol4, vol5, vol6, vol7, vol8 (unanimous)*

### INVARIANT-N2: Lattice node spacing notation (vol-split)

Volumes 1–5 write `$\ell_{node}$` (script ell) as the primary form. Volumes 6–7 write `$l_{node}$` (roman ell) as the primary form. Vol 8 does not use this symbol. Vols 2 and 4 contain isolated roman-ell instances in their source; those specific instances must be preserved as roman (do not normalize to script). Distillers must preserve the source notation within each volume; do not normalize across volumes.

*Confirmed by: source grep — vol1 (52 script, 2 roman); vol2 (56 script, 4 roman); vol3 (19 script, 1 roman); vol4 (22 script, 4 roman); vol5 (29 script, 0 roman); vol6 (1 script, 3 roman); vol7 (1 script, 4 roman); vol8 (0)*

### INVARIANT-N3: AVE Operator numbering convention

Topological operators are named OpN where N is the operator number. Known operators: Op2 (knot crossing correction), Op3 (small-signal impedance correction), Op4 (potential well / H-bond), Op8 (large-signal confirmation), Op9 (charge correction), Op14 (long-range coupling). The naming convention is cross-volume; individual operator formulae live in domain documents.

*Confirmed by: vol2, vol3, vol4, vol5 (explicit); vol7 (Op3, Op8 in Ch.4)*

### INVARIANT-N4: $S_{11}$ dual-use notation

$S_{11}$ is used as the standard EE reflection coefficient in Vol 4 and Vol 7, AND as a folding free-energy functional / objective function in Vol 5. An agent navigating from Vol 4 to Vol 5 must not assume the same physical meaning. Both uses are intentional and AVE-specific.

*Confirmed by: vol4 (EE context), vol5 (biology context)*

---

## Structural Conventions

### INVARIANT-S1: tcolorbox environments

All volumes share these named environments: `resultbox`, `axiombox`, `simbox`, `examplebox`, `summarybox`, `exercisebox`, `circuitbox`, `codebox`, `objectivebox`. In KB markdown, each renders as a named blockquote with a bold environment-type prefix:

```markdown
> **[Resultbox]** *Title of the Result*
>
> Body content...
```

Individual volumes may use only a subset; resultbox is the most common. Vol 5 uses only resultbox. Vol 8 uses none.

*Confirmed by: vol1, vol2, vol3, vol4, vol5, vol6, vol7 (confirmed in surveys); vol8 (zero instances)*

### INVARIANT-S2: AVE Axiom numbering

The four AVE axioms carry stable meanings across all volumes. Canonical source of truth: `AVE-Core/manuscript/common_equations/eq_axiom_[1-4].tex`. KB documents must use these labels; volume-specific re-instantiations may add a parenthetical domain alias but the canonical name is primary.

- Axiom 1: **Impedance** — Z₀ = √(μ₀/ε₀); ℓ_node = ℏ/(m_e·c). (Vol 8 alias: ABCD cascade / coupled amplitude.)
- Axiom 2: **Fine Structure** — α = e²/(4πε₀ℏc); V_yield = √α · m_e c²/e ≈ 43.65 kV. Includes the topo-kinematic isomorphism `[Q] ≡ [L]` as its underlying mechanism. (Vol 8 alias: topological phase dislocation.)
- Axiom 3: **Gravity** — G = ℏc/(7ξ·m_e²) with ξ ≈ 8.15×10⁴³ the dimensionless Machian hierarchy coupling (NOT ξ_topo). (Vol 8 alias: least reflected action.)
- Axiom 4: **Universal Saturation Kernel** — S(A) = √(1 − (A/A_yield)²). (Vol 8 alias: SiLU / saturation gate.)

*Confirmed by: vol1 canonical .tex (eq_axiom_[1-4].tex); vol8 (re-instantiated in virtual media domain).*

### INVARIANT-S3: Shared experimental appendix

`common/appendix_experiments.tex` (Unified Index of Experimental Falsifications) is not owned by any volume. Its canonical KB location is `ave-kb/common/appendix-experiments.md`. Each volume that includes this file points to the canonical location; it is never duplicated in a volume tree.

*Confirmed by: vol7, vol8 (explicit); implied by vol1, vol3, vol4 context*

### INVARIANT-S4: Up-link format

Every KB document except `ave-kb/entry-point.md` begins with exactly one up-link on line 1:

```markdown
[↑ Parent Name](../index.md)
```

The `↑` character (U+2191) is the machine-checkable marker. Pattern: `^\[↑ `.

*Confirmed by: all 8 volumes (unanimous)*

### INVARIANT-S5: KB frontmatter (unified metadata block)

Every KB content file (`.md` under `manuscript/ave-kb/`, excluding `claim-quality.md`, `CLAUDE.md`, `CONVENTIONS.md`, `README.md`, and the `session/` working directory) carries a YAML-in-HTML-comment frontmatter block immediately after the up-link line. This block consolidates what was previously a stack of separate comment-line conventions (leaf marker, path-stable, claim-quality, no-claim, subtree-IDs).

**Format:**

```markdown
[↑ Parent Title](relative/path)

<!-- kb-frontmatter
kind: leaf
claims: [clm-h9aqmt]
path-stable: "referenced from vol2 as eq:dynamic_capacitance_yield"
-->

# Title
... body ...
```

**Required field on every file:**
- `kind` — one of `leaf`, `leaf-as-index`, `index`, `entry-point`.

**For `kind: leaf` and `kind: leaf-as-index`:**
- Either `claims: [id1, id2, ...]` OR `no-claim: <reason>`. Mutually exclusive; verifier enforces.
- Optional `path-stable: <provenance string>` — preserves the prior INVARIANT-S6 cross-volume label provenance.

**For `kind: index`:**
- `subtree-claims: [id1, id2, ...]` — **derived field**, regenerated by `make refresh-kb-metadata`. Do not hand-edit.
- Optional `bootstrap: true` — set on volume roots and `entry-point`; the bootstrap blockquote directive in the body is hand-maintained for now.

**For `kind: entry-point`:**
- `subtree-claims: [id1, id2, ...]` — derived (union of all leaf claims in the KB).
- `bootstrap: true`.

**Exceptions** (formerly noted under INVARIANT-S5/S6/S8):
- *Leaf-as-index*: when a directory contains only `index.md`, that file may declare `kind: leaf-as-index` and carry `claims:` directly. Its frontmatter subsumes any subtree summary — no separate `subtree-claims` line is needed because the leaf IS the subtree.
- *Empty subtree*: an index whose children are all `no-claim` carries `subtree-claims: []`. The empty list is intentional, not forgotten.
- *Navigation-pointer index*: an index that delegates results to children may use a `> **Navigation note:**` blockquote in lieu of `## Key Results`. Treat absence of `## Key Results` as a signal to check for a Navigation note, not automatically a defect.

**Maintenance pipeline:**
- `make refresh-kb-metadata` regenerates derived fields (currently `subtree-claims`). Idempotent. Run after any change to leaf claims.
- `make verify-claim-quality` is read-only — never modifies. Failures tagged refresh-fixable suggest running refresh first; manual-fix failures must be repaired by hand.

*Confirmed by: convention spec at `mad-review/kb-metadata-spine-spec.md`; migration script and standing refresh+verify scripts at `manuscript/ave-kb/tools/`.*

### INVARIANT-S6: (subsumed into S5 frontmatter)

Path-stable provenance is now the `path-stable` field of the kb-frontmatter block. The legacy `<!-- path-stable: ... -->` line form is no longer used. Cross-volume references that need stable labels declare them in their leaf's frontmatter.

### INVARIANT-S7: Canonicality of leaves

Leaves are canonical. Intermediate, index, and entry-point nodes are *derived* via summarization; even faithfully executed, a summary may suggest implications not present in or supported by the leaves. Summary content is a routing aid, not a source of claims.

Cross-cutting claim-quality content lives in [`claim-quality.md`](claim-quality.md) (KB root). Per-volume claim-quality content lives in `volN/claim-quality.md` — one each for [vol1](vol1/claim-quality.md), [vol2](vol2/claim-quality.md), [vol3](vol3/claim-quality.md), [vol4](vol4/claim-quality.md), [vol5](vol5/claim-quality.md), [vol6](vol6/claim-quality.md), and [common](common/claim-quality.md). Every consumer (agent or human) forming a claim about an AVE result must consult the cited leaf — and, where a relevant `claim-quality.md` entry exists, that claim-quality entry — before treating a summary statement as a claim source.

The volume `index.md` files and `entry-point.md` carry blockquoted bootstrap directives instructing consumers to load the relevant claim-quality documents on entry; these directives are binding on agents that visit those files.

*Confirmed by: convention spec at `AVE-Core/kb-claims-boundaries-convention.md` (gestation; promoted to `CONVENTIONS.md` in Dispatch 8); plan at `mad-review/kb-claims-boundaries-plan.md` (umbrella).*

### INVARIANT-S8: Claim-quality ID propagation

Each entry in a `claim-quality.md` file carries a stable ID of the form `clm-` plus 6 lowercase-alphanumeric characters (`<!-- id: clm-xxxxxx -->`). These IDs propagate downward through the KB via the kb-frontmatter (INVARIANT-S5) so any consumer can grep an ID and reach every location that participates in the claim.

**Frontmatter `claims` field (mandatory on every leaf and leaf-as-index, unless no-claim).** Lists every claim-quality ID that cites the leaf in its "Leaf references" footer. A leaf either carries `claims: [...]` or `no-claim: <reason>`; the verifier enforces mutual exclusivity. The list is the complete index of which claim-quality entries depend on this leaf.

**Tier 2 — inline markers (mandatory for multi-claim leaves).** When a leaf's `claims` list has 2+ IDs, every ID must have a proximal `<!-- claim-quality: clm-<id> -->` marker adjacent to the specific equation, named principle, section, or block that maps to that ID. The frontmatter `claims` list says "these IDs apply to this leaf"; Tier 2 markers say "this specific equation IS that claim." For single-claim leaves, Tier 2 is not required — the frontmatter is unambiguous.

**Frontmatter `subtree-claims` field (derived).** Each `kind: index` and `kind: entry-point` file carries `subtree-claims: [...]` listing the union of leaf claims under its scope. This field is regenerated by `make refresh-kb-metadata` from the leaf frontmatter — never hand-edited. Drift between declared and computed is a hard verifier failure (refresh-fixable category).

**Bidirectional coverage (verifier-enforced).** Every canonical entry in any `claim-quality.md` file must be cited by at least one leaf's `claims` field. An entry with no leaf citation is a hard failure: either back-link from the relevant leaves, or remove the entry. Meta-claims and reading-hazards belong in `CLAUDE.md`, `CONVENTIONS.md`, or `LIVING_REFERENCE.md`, not in `claim-quality.md`.

**Grep guarantee.** `grep -r "clm-<id>"` across the KB returns: the canonical entry in `claim-quality.md`, every leaf whose frontmatter cites the ID, every Tier 2 inline marker, and every intermediate-index `subtree-claims` summary that scopes the entry. The `clm-` prefix makes IDs unambiguously greppable — `\bclm-[a-z0-9]{6}\b` matches IDs and nothing else, never an English or physics word. Walking from a claim-quality entry to its supporting derivations (and back) is mechanical and bidirectional.

*Confirmed by: spec at `mad-review/kb-metadata-spine-spec.md`; live pipeline tools at `manuscript/ave-kb/tools/{refresh-kb-metadata,check-claim-quality}.py` (one-shot migration tools retired to `tools/archival/`); CI gate via `make verify-claim-quality`.*

---

## Cross-Volume Physical Constants

### INVARIANT-C1: Dielectric yield limit

$V_{\text{yield}} \approx 43.65\,\text{kV}$ is defined in Vol 4 Ch.1. When this value appears in any KB document outside Vol 4, it must carry a cross-reference primary pointer to its Vol 4 definition.

*Confirmed by: vol4 (definition), vol3, vol6, vol7 (references without qualification)*

### INVARIANT-C2: Electromechanical transduction constant

$\xi_{topo} = e / l_{node}$ (units: C/m). The bridge between AVE lattice parameters and mechanical/biological quantities. Used in Vol 2 (atomic orbital mappings), Vol 4 (circuit engineering derivations), and Vol 5 (mass-to-inductance, bond stiffness-to-capacitance translations). Canonical definition: Vol 5 `organic-circuitry/electromechanical-transduction-constant.md`.

*Confirmed by: vol5 (proposes as CLAUDE.md invariant, three or more volumes)*

### INVARIANT-C3: H-bond canonical values

$d_{HB} = 1.754\,\text{\AA}$ and $E_{HB} = 4.98\,\text{kcal/mol}$ are the canonical AVE predictions for the hydrogen bond equilibrium distance and energy, derived from Op4 potential minimum in Vol 5. Referenced from Vol 3. The result values belong here; the derivation lives in `vol5/molecular-foundations/organic-circuitry/hbond-op4-equilibrium.md`.

*Confirmed by: vol5 (derivation), vol3 (cross-volume reference)*

### INVARIANT-C4: Z-proportionality regimes

Two distinct impedance scaling regimes in the AVE framework:

- Physical/biological media: $Z \propto 1/A$
- Virtual media (LLM / information topology): $Z \propto A$

This inversion defines the hardware/software isomorphism. Cross-referenced from Vols 1, 2, 5, and 8.

*Confirmed by: vol8 (explicit); vol1 (foundation); vol2, vol5 (biological context)*

---

## Cross-Reference Formats

### INVARIANT-F1: Primary cross-volume dependency

When a KB document requires the reader to navigate to another location to get a definition, use:

```markdown
> → Primary: [Document Name](relative/path/to/target.md) — brief rationale (source label if known)
```

### INVARIANT-F2: Optional cross-volume suggestion

When a KB document suggests (but does not require) navigation to a related location:

```markdown
> ↗ See also: [Document Name](relative/path/to/target.md) — brief rationale
```

Cross-volume references appear in index documents and in leaf documents where the source text explicitly references another section. They must never paraphrase or summarize the target content.
