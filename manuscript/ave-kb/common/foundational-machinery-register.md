[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Canonical FOUNDATIONAL-MACHINERY register — a status / provenance / usage VIEW over the EXISTING `clm-` claim nodes that carry AVE's derived MACHINERY tier (named theorems + universal operators + kernels), the THIRD rung of the provenance ladder (axioms → machinery → calibration-inputs → applications). This leaf originates NO new node-body via frontmatter and mints NO new id: every member is an ALREADY-materialized `node_type: \"claim\"` node in claims.jsonl (a `<!-- id: clm-xxxxxx -->` entry in a `claim-quality.md` register), so a register that re-declared them would be a parallel scheme, forbidden by INVARIANT-S11 (extend, don't reinvent). It is the machinery-tier analog of the axiom-register (a VIEW over the four `axiom-N` framework nodes) and the interlock-register's per-constant Calibration-Constant Criteria Register (a VIEW over the `ilk-` nodes): a bolded-field VIEW that POINTS AT existing nodes (via their `clm-` id) and READS their recorded status/solidity/provenance/citation_count — NOT a source of new claims and NOT a rescoring. Hence no-claim."
path-stable: "the canonical foundational-machinery register leaf; makes AVE's derived-machinery tier (theorems + operators + kernels) first-class as a status/provenance/usage view over the member clm- claim nodes"
-->

<!-- foundational-machinery-meta
foundational-machinery: clm-gdd70j clm-sysqaf clm-6mvtsf clm-1eg13f clm-rtdmsn clm-6t3p6x clm-ka5zdx clm-law1ho clm-ofys5v clm-gz7ryg
expected-machinery-count: 10
expected-derived-count: 8
expected-definitional-count: 2
-->

# Foundational-Machinery Register — Derived Theorems / Operators / Kernels (status / provenance / usage view)

The **source-of-truth index** for AVE's **derived MACHINERY** — the named
theorems, universal operators, and kernels that vol1 / vol2 / vol3 (and the
engine) build on. This is the **third rung of the provenance ladder**:

> **axioms** (`axiom-register.md`) → **machinery** (THIS register) →
> **calibration-inputs** {m_e, α, G} (`interlock-register.md`) →
> **applications** (the scale-instance `clm-`s).

Rungs 1, 2, and 4-inputs already have first-class tracking; the derived-machinery
tier was tracked only as scattered `clm-` claims, informally "near-foundational
machinery" ([`session/kb-improvements.md`](../session/kb-improvements.md): "the
universal operators (Op14 `clm-1eg13f`), Theorem 3.1′ (`clm-rtdmsn`), and the
parametric-coupling kernel (`clm-6t3p6x`) are near-foundational machinery that
vol1/vol2/vol3 build on"). This register consolidates the status view.

## Sections

- **§0 — Register discipline (VIEW, not new-id-scheme).**
- **§1 — Membership set (the load-bearing call — surface for Grant).**
- **§2 — Per-entry view fields (READ from existing claim records).**
- **§3 — Operators (the universal-operator machinery).**
- **§4 — Theorems (the named-theorem machinery).**
- **§5 — Kernels (the kernel machinery).**
- **§6 — Summary roll-up + the DERIVED-vs-DEFINITIONAL audit count.**
- **§7 — Companion registers + the vol3→vol4 mis-volume artifact this homes.**
- **§8 — Schema / gate note (flagged, NOT built this pass) + design decisions to ratify.**

## §0 — Register discipline (VIEW, not new-id-scheme)

> **This is a VIEW, not a new node scheme (INVARIANT-S11 — extend, don't
> reinvent).** Every member of this register is an **ALREADY first-class claim
> node**: `refresh-kb-metadata` materializes one `node_type: "claim"` record per
> `<!-- id: clm-xxxxxx -->` entry across the `claim-quality.md` registers into
> [`.index/claims.jsonl`](../.index/claims.jsonl). This register does **not**
> re-declare those nodes and mints **no** new id — that would be the
> shadow-scheme rot INVARIANT-S11 exists to stop. It is a bolded-field register
> that **POINTS AT** the existing machinery `clm-` nodes (by id) and **READS**
> their recorded fields (title / solidity / build_band / depends-on /
> citation_count) — it never recomputes or rescores anything. It is the direct
> machinery-tier analog of the `axiom-register.md` (a VIEW over the four
> `axiom-N` framework nodes — the forthcoming companion register on branch
> `analysis/axiom-register`; cross-linked as a live link when it merges, kept as
> a backtick reference here so this leaf's link-integrity gate does not depend on
> an unmerged sibling) and the interlock-register's
> [Calibration-Constant Criteria Register](interlock-register.md) (a VIEW over
> the `ilk-` nodes that mints no `ilk-` id and touches no count machinery).

> **Node-count invariance (zero new IDs).** Because every member is an existing
> `clm-` node and this leaf carries `no-claim` (no `claims:` / `exp-id:` /
> `sup-id:` frontmatter), materializing this leaf adds **zero** nodes to
> `claims.jsonl`. The `foundational-machinery:` meta line is a machine-readable
> list of member ids (the analog of the interlock-register's
> `calibration-params:` line), NOT a node declaration — parsing it emits no
> record and no edge. `make verify-kb-metadata` node count is **UNCHANGED** by
> this leaf (see §8 for the gate note; the count-invariance is confirmed in the
> validation footer).

> **What "machinery" means here (the tier boundary).** A member is
> **derived MACHINERY** iff it is a reusable theorem / operator / kernel that the
> per-domain application leaves *build on* (it is a `depends-on` target of
> downstream claims and/or the engine's shared code path), as distinct from an
> **application** — a scale-instance that USES the machinery at one domain
> (galactic rotation, protein fold, BCS, a specific bench). The boundary is not
> always sharp; §1 flags every borderline machinery-vs-application inclusion for
> Grant rather than silently deciding it.

## §1 — Membership set (the load-bearing call — surface for Grant)

<!-- filled in a later commit -->

## §2 — Per-entry view fields (READ from existing claim records)

<!-- filled in a later commit -->

## §3 — Operators (the universal-operator machinery)

<!-- filled in a later commit -->

## §4 — Theorems (the named-theorem machinery)

<!-- filled in a later commit -->

## §5 — Kernels (the kernel machinery)

<!-- filled in a later commit -->

## §6 — Summary roll-up + the DERIVED-vs-DEFINITIONAL audit count

<!-- filled in a later commit -->

## §7 — Companion registers + the vol3→vol4 mis-volume artifact

<!-- filled in a later commit -->

## §8 — Schema / gate note (flagged, NOT built this pass) + design decisions to ratify

<!-- filled in a later commit -->
