[↑ Translation Tables](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Architecture / organizing-discipline doc for the cross-discipline translation infrastructure (the hub-and-spoke rule + per-row requirements + spoke inventory). References the existing translation tables, the vocabulary spine, and the axioms; originates no new physical claim (consistency-class organizing methodology only)."
path-stable: "the hub-and-spoke architecture spec for the translation-tables subtree; companion to index.md (navigation) and substrate-native-terminology.md (the vocabulary spine)"
-->

# Translation-Tables Architecture — the Hub-and-Spoke Rule

This is a **no-claim organizing-discipline leaf.** It records the *architecture* of the cross-disciplinary translation infrastructure — how the per-discipline tables relate to the substrate and to each other — so that new disciplines get mapped consistently and cross-discipline correspondences do not accrete as ad-hoc rows in the wrong table. It mints no physics; it organizes existing consistency-class content. Ratified design (Grant 2026-07-20, itemized go #2): **hub-and-spoke**.

Companion nodes: [index.md](index.md) (navigation pointer to the spokes) · [substrate-native-terminology.md](../substrate-native-terminology.md) (the vocabulary spine) · [translation-circuit.md](translation-circuit.md) (the privileged operational spoke) · the agent-discipline side is the `ave-cross-discipline-mapping` skill (meta) + `ave-ee-first-mapping` skill (the EE spoke).

## 1 — The hub

**The hub is the substrate-native representation — the axioms (Ax 1–4) expressed in the least-leaky language, with the [vocabulary spine](../substrate-native-terminology.md) as its lexicon.** Every discipline maps to this one representation; disciplines do **not** map to each other.

- The hub's **noun-and-primitive lexicon** is [`substrate-native-terminology.md`](../substrate-native-terminology.md) (the EE-native leak-check + regime-scoped term register) plus the adjudicated-term index [`vocabulary-register.md`](../vocabulary-register.md) (`def-` nodes). A spoke row's substrate-side cell must use spine vocabulary — reach for the EE-native primitive first, and scope any borrowed materials/fluid word to the regime where its defining property literally holds.
- The hub is a *representation*, not a table. It is realized in the corpus as the axioms + the canonical leaves; the translation tables are the **projections of disciplines onto it**.

## 2 — The spokes

**A spoke is one discipline's translation table: `translation-<discipline>.md`.** Each row maps a discipline concept to its substrate-native (hub) equivalent. The spokes are the files enumerated in [index.md](index.md).

- **The privileged operational spoke is circuit/EE** ([`translation-circuit.md`](translation-circuit.md)). Per canon (`substrate-native-terminology.md`, `ave-ee-first-mapping`), EE is the *least-leaky* language because its bedrock constants ($\varepsilon_0,\mu_0,Z_0,c$) were measured off empty space — EE is "already a vacuum theory." EE stays the primary operational spoke; the hub-and-spoke rule and the `ave-cross-discipline-mapping` meta-skill govern the *family* of spokes, of which EE is the first-among-equals.
- **A spoke is regime-conditional.** EE is primary for *dynamics*; for *geometric/topological/axiomatic* content substrate-topology is primary and the discipline is the consistency check (per the vocabulary spine's "division of labor").

## 3 — The rule: spokes map to the hub, never to each other

> **HUB-AND-SPOKE RULE.** A discipline maps **only** to the substrate-native representation (the hub). A cross-discipline correspondence (discipline-X concept ↔ discipline-Y concept) is expressed as **two spoke rows that share a hub cell**, never as a direct X↔Y row. The shared hub cell is the join.

Rationale: a direct discipline-to-discipline row (e.g. "seismological P-wave ↔ superconducting vortex") smuggles in an unstated substrate identification and is unauditable — there is no means-test against the substrate, only against a sibling discipline that itself may be leaky. Routing through the hub forces every correspondence to state its substrate primitive, which is the thing that can be means-tested and Ax3-checked.

**Carve-out — one deliberate OUTSIDE-SCOPE sibling (Grant ruling D2, 2026-08-01; verbatim [sic]: *"D2: follow rec"*).** [`../theorem-thesaurus.md`](../theorem-thesaurus.md) sits in `common/` and **not** in this subtree, by ruling and not by oversight: its rows join theorem **names** across disciplines through a **proof** (a mathematical identity), never through a substrate identification — so the rule's own rationale above (the unstated-substrate-identification / unauditable-X↔Y hazard, this section's rationale line) **does not reach it**, and its audit is the proof rather than a means-test. That leaf states the same boundary in its own §0 contract (*"a statement about the **algebra**, not about the world"*, with the mandatory Kron ontological-silence ceiling on every EXACT row). Nothing here relaxes the hub-and-spoke rule for any actual spoke: a genuine discipline-X↔discipline-Y **substrate** correspondence still routes through the hub.

**Corollary — cross-discipline rows do not live in a sibling's spoke.** When a row's *discipline* side is not the spoke's discipline, it is a leak into the wrong spoke and should be relocated to (or pointered from) the correct discipline's spoke. *(Live instance, flag-don't-fix: the A1/T2 ↔ seismological P/S partition row currently sits in the EE spoke [`translation-circuit.md`](translation-circuit.md) §4 (line 157, ⚠-tagged "cross-discipline / NOT EE") and §6 means-test #28. Its discipline home is [`translation-elastodynamics.md`](translation-elastodynamics.md); the circuit-spoke ⚠ entry should be relocated or reduced to a pointer — an auditor-lane cleanup, not done here. Both copies cite the same merged source (#753), so this is consistency-class duplication, not a contradiction.)*

## 4 — Per-row requirements

Every spoke row carries three fields beyond the concept↔substrate pair:

1. **Means-test receipt** — the cross-check that the substrate prediction and the discipline's own result agree (numerical + scaling, or an explicit "structural / order-of-magnitude / not-yet-tested" grade). A row with no receipt is a *candidate/watch* row, tagged as such — it is not a validated mapping.
2. **Ax3-compatibility tag** — does the correspondence import a property the substrate lacks in the row's regime? The sharpest test is internal-friction dissipation: the sub-yield interior is lossless-reactive (Ax 3), so a discipline word that smuggles in viscous heating leaks. Tag **CLEAN** (Ax3-native / reactive / radiative-port-legal), **GATED** (rides an open lossless-vs-dissipative fork), or **FAIL** (imports dissipation the regime forbids).
3. **Provenance class** (`consistency-vs-emergence`) — **identity / manifestation / consistency / emergence / import**. Cross-discipline rows are consistency-class or import-class by construction (a discipline sibling is an external anchor, not an AVE-distinct chord); an emergence-class headline on a cross-discipline row is a category error.

## 5 — Spoke inventory (graded)

| Spoke | Status | Note |
|---|---|---|
| [circuit / EE](translation-circuit.md) | **EXISTS (privileged operational spoke)** | 30+ primitive rows + tool tracker + means-test corpus; the canonical first-call |
| [elastodynamics / seismology](translation-elastodynamics.md) | **NEW (this batch)** | seeded from merged #753 (§6 Aki–Richards P/S receipt); the elastic-medium sibling |
| [materials / metallurgy](translation-materials.md) | **NEW (this batch)** | source derivation PR #762 (`research/vacuum-metallurgy`) **merged 2026-07-20**; rows canonical (see the leaf banner) |
| [Feynman diagrammatics](translation-diagrammatics.md) | **NEW (2026-08-23)** | NO-CLAIM formalism register — every row a POINTER at its canonical home (no validated new mappings); per-row means-test/Ax3/provenance fields: **EXEMPT (Grant ruling 2026-08-23)** — no row is a validated mapping, every row is a pointer at a canonical home carrying its own status; a future row that MINTS a mapping loses the exemption and retrofits |
| [quantum mechanics](translation-qm.md) | sibling — retrofit-graded, routed | pre-existing §8 sibling; per-row hub-and-spoke retrofit is an auditor-lane follow-on |
| [particle physics](translation-particle-physics.md) | sibling — retrofit-graded, routed | " |
| [gravity](translation-gravity.md) | sibling — retrofit-graded, routed | " |
| [cosmology](translation-cosmology.md) | sibling — retrofit-graded, routed | " |
| [condensed matter](translation-condensed-matter.md) | sibling — retrofit-graded, routed | " |
| [biology / biophysics](translation-biology.md) | sibling — retrofit-graded, routed | " |
| [stochastics](translation-stochastics.md) | sibling — retrofit-graded, routed | " |
| [detector instrumentation](translation-instrumentation.md) | sibling — retrofit-graded, routed | " |

The eight §8 siblings predate this architecture; they are **graded for retrofit** (add the per-row means-test / Ax3 / provenance fields where missing) as an auditor-lane campaign, **routed, not done here** — this batch lands the rule + the two new spokes only.

## 6 — Relationship to the skills

- **`ave-cross-discipline-mapping`** (meta-skill) is the agent-discipline side of this leaf: it fires when doing an X-discipline analysis or discovering a substrate↔discipline correspondence, and enforces "consult `translation-X` first; land validated correspondences as rows with receipts; never map discipline-to-discipline directly."
- **`ave-ee-first-mapping`** is the EE spoke's discipline (EE stays the privileged operational spoke). The meta-skill generalizes its Step-6 landing discipline to the whole spoke family; EE-first-mapping remains the authority for the circuit spoke specifically.

> **Cross-references:** the navigation pointer → [index.md](index.md); the vocabulary spine → [substrate-native-terminology.md](../substrate-native-terminology.md); the adjudicated-term index → [vocabulary-register.md](../vocabulary-register.md); the classification discipline → [claim-quality.md](../claim-quality.md) (`consistency-vs-emergence`).
