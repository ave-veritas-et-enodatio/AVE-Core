[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Canonical AXIOM register — a status / provenance / residual-content VIEW over the FOUR existing `axiom-N` framework nodes (node_type: \"axiom\", ids axiom-1..axiom-4; the former axiom-5 = Substrate DC Bias was restructured axiom->source law per R55 2026-08-24, its node RETIRED, and its register entry at the end of this file is now the SOURCE-LAW entry), which are ALREADY materialized into claims.jsonl by refresh-kb-metadata from the `- Axiom N: **…**` bullets in CLAUDE.md INVARIANT-S2 (the KB's axiom-numbering authority). This leaf originates NO new node-body via frontmatter and mints NO new axiom id: axioms are terminal UNSCORED framework nodes (SCHEMA.md 'Framework record' — 5 fields, no confidence/solidity/quality, emit no edges), so a register that re-declared them would be a parallel scheme, forbidden by INVARIANT-S11 (extend, don't reinvent). It is the axiom analog of the interlock-register's per-CONSTANT Calibration-Constant Criteria Register: a bolded-field VIEW that POINTS AT the existing framework nodes (via the `axiom-N` id) and, where an axiom's content is partly derived, at the theorem `clm-`/result that carries the proof — NOT a source of new claims. Hence no-claim."
path-stable: "the canonical axiom-register leaf; makes the AVE axioms' status / provenance / residual-content first-class as a view over the axiom-N framework nodes"
-->

<!-- axiom-meta
axiom-nodes: axiom-1 axiom-2 axiom-3 axiom-4
expected-independent-axiom-count: 4
-->

# Axiom Register — the Four AVE Axioms (status / provenance / residual-content view)

The **source-of-truth index** for the AVE **axioms** — the four canonical
structural primitives the entire framework rests on. This register makes each
axiom's **adjudication status**, **provenance**, and **residual axiomatic
content** first-class, the way
[`interlock-register.md`](interlock-register.md) makes the calibration-parameter
interlock first-class. The axioms were previously tracked as terminal framework
nodes (materialized, but with no status view) plus scattered eq-labels and prose
"remains postulated" notes; this register consolidates the status view without
minting a parallel id scheme.

> **This is a VIEW, not a new node scheme (INVARIANT-S11 — extend, don't
> reinvent).** The four axioms are **ALREADY first-class metadata nodes**:
> `refresh-kb-metadata` parses the `- Axiom N: **<title>** — …` bullets in the
> [`INVARIANT-S2`](../CLAUDE.md) section of `CLAUDE.md` and emits one
> `node_type: "axiom"` record per axiom into
> [`.index/claims.jsonl`](../.index/claims.jsonl) — `axiom-1` … `axiom-4`, the
> [`.index/SCHEMA.md`](../.index/SCHEMA.md) "Framework record" (5 fields:
> `node_type` / `id` / `title` / `canonical_path` / `canonical_anchor`). Per
> SCHEMA.md a framework node carries **NO scoring fields** (no `confidence` /
> `solidity` / `quality` — it is **solidity-1.0 by definition, framework
> bedrock**) and **originates no `depends` / `strengthens` / `supports`
> edges**. This register does **not** re-declare those nodes and mints **no**
> new axiom id — that would be the shadow-scheme rot INVARIANT-S11 exists to
> stop. It is a bolded-field register that **POINTS AT** the existing
> `axiom-N` framework nodes (by id) and, where an axiom's content is partly
> derived, at the theorem `clm-` / result doc that carries the proof + its
> solidity. It is the direct axiom analog of the interlock-register's second
> half — the per-CONSTANT
> [Calibration-Constant Criteria Register](interlock-register.md), a VIEW over
> the `ilk-` nodes that mints no `ilk-` id and touches no count machinery.

> **Node-type discipline (why status is a view field, not a scored claim).**
> Per [`CLAUDE.md` INVARIANT-S2 / SCHEMA.md](../.index/SCHEMA.md), an axiom is
> a **terminal, UNSCORED framework node**. So an axiom's `status` here is a
> **human-facing view field**, NOT a `confidence`/`solidity` on the node. When
> an axiom's content is **derived** (fully or in part), the *derivation's*
> confidence/solidity lives on the **theorem `clm-` node** that carries the
> proof — the axiom node stays UNSCORED and this register's `derived_by` field
> points at that theorem. This keeps two things separate that must not merge:
> *"is this a bedrock primitive?"* (framework-node identity — always
> solidity-1.0-by-definition) vs *"how much of its content is now a theorem of
> something weaker?"* (the `status` + `residual_content` view). A SHAPE-DERIVED
> axiom is **not** a demoted axiom — its residual content is still bedrock; what
> shrank is *how much* is axiomatic, not *whether* the residual is.

## Status axis (the four values)

Each axiom carries a **status** ∈ the following four-value axis (the axiom
analog of the interlock-register's `real_or_fitted` chord/echo axis, but a
*derivational-maturity* axis rather than a chord/echo one):

- **POSTULATED** — the axiom is taken as a primitive; no derivation of its
  content from anything weaker exists. (The default / bedrock state.)
- **SHAPE-DERIVED** — the axiom's *specific form* (a curve, an equation, a
  functional shape) is a **theorem** of a *named residual primitive* that is
  itself weaker / smaller than the original axiom. The axiom does **not**
  vanish; its **content shrinks and relocates** to the residual. May carry a
  `(conditional)` qualifier when the residual identifications are named-but-not-
  themselves-forced (a full reduction would force those too). This is a
  **content reduction, not a count reduction** — the axiom count does not drop.
- **CHALLENGED** — an open, live challenge to the axiom's necessity or content
  exists (a candidate reduction under active adjudication), not yet resolved to
  SHAPE-DERIVED or back to POSTULATED.
- **DERIVED-TO-THEOREM** — the axiom's *entire* content is a theorem of the
  other axioms + a bare, already-present identification (no independent residual
  primitive). Only at this status does the **independent-axiom count drop** (the
  axiom is no longer independent). **No axiom is at this status.** **⊕ RATIFIED-ADDITION** *(the UPWARD bin, added 2026-08-10 per R47 item 1)* — a NEW axiom is ratified into the set; the only bin that moves the count UP. It demotes nothing: existing axioms keep their numbering, names and status. **Axiom 5 (Substrate DC Bias) is the first and so far only entry.** The bin exists because the four values above could only describe an axiom SHRINKING (POSTULATED → SHAPE-DERIVED → DERIVED-TO-THEOREM); the axis had no way to record the set GROWING, so a ratified addition had nowhere honest to sit.

> **Status ≠ solidity.** A framework node has no solidity to lower. The
> `status` field records the *derivational maturity of the axiom's content*, a
> separate axis from the node's framework-bedrock identity. Only
> DERIVED-TO-THEOREM changes the **independent-axiom count**; SHAPE-DERIVED and
> CHALLENGED and POSTULATED all leave the count at 4.

## The LIVE independent-axiom count

> **`expected-independent-axiom-count: 4`** (the `axiom-meta` block above; the
> axiom analog of the interlock-register's `expected-independent-count: 3`
> parameter count). It is `(# axiom-N framework nodes) − (# axioms at
> DERIVED-TO-THEOREM)`. There are **four** `axiom-N` framework nodes and
> **zero** at DERIVED-TO-THEOREM, so the count is **4**. A status flip to
> DERIVED-TO-THEOREM (an axiom's *whole* content becoming a theorem of the
> others) would drop it `4 → 3`. **A SHAPE-DERIVED flip does NOT move the
> count** — Axiom 4 is SHAPE-DERIVED (conditional) and the count stays 4,
> because its residual (the L2-norm / fixed-radius constraint) is itself the
> relocated axiomatic content, not a pre-existing primitive.
>
> **Not yet CI-asserted (schema note, §Schema/gate note below).** Unlike the
> interlock register's `expected-independent-count`, this
> `expected-independent-axiom-count` is **not** currently recomputed or gated by
> `verify-kb-metadata` — there is no `axiom-meta` parser and no status field on
> the framework-node record. Wiring that gate is a `verify-kb-metadata`
> extension flagged (but deliberately NOT built) in this pass — get the leaf
> right first. Until then the count is a hand-maintained assertion, loud only to
> a human reader.

## Per-axiom field legend

Each `## Axiom N — <title>` heading below carries a bolded field block (parallel
to an `ilk-` entry / a per-constant criteria entry) with these fields:

- **axiom-node** — the existing `axiom-N` framework-node id this entry is a view
  over (the grep anchor: `grep -r "axiom-N"` reaches the CLAUDE.md bullet, the
  claims.jsonl record, and this entry). Never a new id.
- **canonical-statement** — the axiom's canonical name + a one-line statement,
  citing `axiom-definitions.md` (the in-chapter KB restatement) and
  `eq_axiom_N.tex` (the single-source-of-truth `\input`).
- **status** — one of {POSTULATED, SHAPE-DERIVED, CHALLENGED,
  DERIVED-TO-THEOREM} per the axis above.
- **provenance** — where the axiom's status comes from (the derivation branch /
  result doc if SHAPE-DERIVED or CHALLENGED; the honest "postulated" corpus
  self-statements if POSTULATED).
- **residual_content** — what stays AXIOMATIC if part of the axiom is derived.
  For a POSTULATED axiom this is the whole axiom. For a SHAPE-DERIVED axiom it
  is the *smaller* relocated primitive (e.g. Axiom 4's L2-norm / fixed-radius
  constraint) — the axiom's residual after the derivable part is factored out.
- **derived_by** — the theorem `clm-` / result doc that carries the proof + its
  solidity, when the axiom is SHAPE-DERIVED / CHALLENGED. `(none — postulated)`
  when POSTULATED. (The axiom node stays UNSCORED; the solidity lives here on
  the theorem, per the node-type discipline blockquote above.)
- **count-effect** — whether this axiom's status removes it from the
  independent-axiom count. Only DERIVED-TO-THEOREM removes; all others keep it.

---

## Axiom 1 — Substrate Topology (Chiral Laves K4 Cosserat Crystal)
<!-- view of framework node: axiom-1 -->

- **axiom-node:** `axiom-1` (framework node, `node_type: "axiom"`; parsed from the CLAUDE.md INVARIANT-S2 `- Axiom 1: **Substrate Topology**` bullet; UNSCORED).
- **canonical-statement:** The physical vacuum IS a chiral Laves K4 Cosserat crystal — a 3D crystallized substrate of micropolar (Cosserat) nodes at pitch $\ell_{node}$, right-handed $I4_1 32$ chiral space group, 3-fold ($z=3$) chiral srs (Sunada-K4 / Laves) nearest-neighbour connectivity, six intrinsic DOF per node (3 translational → $\varepsilon_0$/E, 3 microrotational → $\mu_0$/B; the Cosserat rotational DOF IS the substrate-native origin of intrinsic spin). Canonical: [`axiom-definitions.md:16`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) + `eq_axiom_1.tex` (single source of truth). *(2026-07-03 DOF-sentence restoration: connectivity corrected from the contaminated "z=4 diamond … in the production engine" wording to the axiom's z=3 physical claim — an implementation-contamination fix per INVARIANT-S2, NOT a meaning change; the z=4-diamond is the engine's non-canonical instrument, migration chartered. See `research/2026-07-03_axiom1-dof-restoration_note.md`.)*
- **status:** **POSTULATED.** No derivation of the K4 / Cosserat substrate topology from anything weaker exists; it is the bedrock structural primitive.
- **provenance:** Postulated primitive. The lattice IDENTITY (D1) is **RATIFIED (Grant 2026-07-03, PR #486): the chiral z=3 srs net is the production carrier**; the achiral z=4 diamond is re-tagged a non-canonical engine instrument (statics-pathological). The prior 2026-06-12 "z=4 diamond production engine vs bare z=3 srs instrument" reading is **SUPERSEDED**. This is an engineering-fidelity ruling that fixes the coordination-number reading of the axiom to z=3 (already the Scheme-A canonical restatement at `axiom-definitions.md:16` / `01_fundamental_axioms.tex:54`, `clm-q39qct`; z=3 justification `clm-9s9apq`), NOT a derivation of the axiom. Records: `research/2026-06-12_lattice-d1-adjudication-memo.md` (2026-07-03 addendum); `_orchestration/2026-07-03_srs-migration-policy.md`; `def-4b1a2c`.
- **residual_content:** **the whole axiom** — the K4 Cosserat crystal substrate topology (space group, connectivity, per-node 6-DOF micropolar structure) is entirely axiomatic.
- **derived_by:** `(none — postulated)`.
- **count-effect:** counts as 1 independent axiom.
- **finding — Axiom 1 has NO dedicated axiom-content `clm-` node (only the framework `axiom-1` node).** The brief asked to reconcile Axiom 1's supposed `clm-3kzmt9`. **`clm-3kzmt9` is NOT an Axiom-1 node.** Verified: its canonical entry is at [`vol1/claim-quality.md:187`](../vol1/claim-quality.md) titled around the **ξ vs ξ_topo homonym distinction** (its body: "$\xi \approx 8.15\times10^{43}$ … vs $\xi_{topo} = e/\ell_{node}$ … different quantities sharing a Greek letter"; specific claim = the $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ cosmological-horizon dilution) plus the α-is-Class-B relabel — confidence 0.90, solidity 0.63, depends-on clm-0ktpcn + clm-5xon03. In [`axiom-definitions.md:33`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) its Tier-2 marker `<!-- claim-quality: clm-3kzmt9 -->` sits on the **notation-warning block UNDER Axiom 2**, not on Axiom 1. So it was never Axiom 1's node. Axiom 1's ONLY first-class node is the terminal framework node `axiom-1`; there is no scored `clm-` that states Axiom 1's content (nor should there be — an axiom is UNSCORED bedrock, so a scored Axiom-1 `clm-` would be a category error, per the node-type discipline). This register's `axiom-1` view IS the intended first-class status home; no `clm-` wiring is needed or correct. **⚑ DOMAIN OF VALIDITY (PHASE-SCOPED) — ADDED 2026-08-06, Grant ruling R7. An ADDITION: nothing above is rewritten, and this axiom's `status`, `provenance`, `residual_content`, `derived_by` and `count-effect` are unchanged by it.** Ruled at [`2026-08-06-rulings-decision-batch.md`](../../../_orchestration/docket-entries/2026-08-06-rulings-decision-batch.md):100–113 (R7), Grant verbatim at `:102` — *"all right, let's do it but intrinsic LC would be the crystallized form of the vacuum so really that ax needs to understand each phase of the vacuum material right?"*. Ruled at concept level: Axiom 1's intrinsic-LC description is the constitutive law of the vacuum material's **crystalline phase**, not of the material as such; **phases are states of one substance, not new axioms** — which is why this lands as a scope header ON Axiom 1 and explicitly NOT as a fifth axiom. **RULED HEADER TEXT, quoted word-for-word from the record `:109`–`:113` (the wording merge-ratified with it):** ⟪ **Domain of validity (phase-scoped, 2026-08-06).** This axiom states the constitutive law of the vacuum material's crystalline phase (cold, sub-yield, lossless-reactive). It does not assert the substance-level law across the material's other phase-states (saturation boundary; ruptured/plasma above V_snap; pre-freeze). Any use across a phase boundary is an extrapolation and must be declared as one. ⟫ *(Rendering note: the ruled text is set inline between ⟪ ⟫ rather than as an indented blockquote because this register's `:189`, `:190`, `:193`, `:194`, `:229`–`:232` are cited by line across the corpus — including inside MERGED ruled text — so this entry is written line-count-neutral. The words are the record's; only the wrapper differs.)* **⚑ VOCABULARY RIDER — SURFACED, NOT FIXED (doc lane).** R7's own vocabulary fence (`:115` — *"Vocabulary fence: the phase inventory must be substrate-named"*) bars borrowed condensed-matter phase words, and the SAME batch's R8 (`:130`–`:131`) classes **"plasma"** as *"a vocabulary leak of the same class as the retired 'amorphous'"* — a lean since upgraded to a GO for the **pre-bond** rename ([`2026-08-06-rulings-go-prebond-hawking.md`](../../../_orchestration/docket-entries/2026-08-06-rulings-go-prebond-hawking.md):7–17, R9). The ruled header above nevertheless contains the token `ruptured/plasma`. **It is quoted word-for-word and NOT silently repaired here** — ruled text propagates verbatim, and R9's rename is scoped to the phrase *"pre-geodesic plasma"*, which this is not. Whether the header's `plasma` token is inside or outside the rename's scope is the ruling author's call. Flagged, not resolved. **⚑⚑ R7 IS OVERRULED — R45, 2026-08-10. Dated supersession; the ruled header text above is PRESERVED byte-for-byte and is NOT rewritten.** Grant, verbatim: *"I didn't want axiom 1 to be solid/crystal phase only, I wanted it to be comprehensive and open to other phases and show the boundaries and nuances between them, same goes for each axiom, so yes I want to overrule the last ruling."* **What changes:** R7 read each axiom as valid-in-the-crystalline-phase-ONLY, with any cross-phase use a declared extrapolation. R45 replaces that with the COMPREHENSIVE-MAP doctrine — **each axiom is a law of the MATERIAL and carries its phase structure explicitly INSIDE**: (a) the crystalline-phase form (today's content), (b) the behavior at each phase boundary where derived, and (c) NAMED-OPEN holes where the phase's law is not yet written, as first-class entries rather than silences. So the header above is no longer a *scope limitation* on Axiom 1; it is row (a) of Axiom 1's phase map, and rows (b)/(c) are supplied in the **Per-axiom PHASE-STRUCTURE map** at the end of this register (R47 item 5). **Honesty requirement carried from the ruling:** comprehensiveness is the FRAME; the text never claims content it lacks. The `ruptured/plasma` vocabulary rider above is unaffected and still routed.

---

## Axiom 2 — Topo-Kinematic Isomorphism
<!-- view of framework node: axiom-2 -->

- **axiom-node:** `axiom-2` (framework node, `node_type: "axiom"`; parsed from the CLAUDE.md INVARIANT-S2 `- Axiom 2: **Topo-Kinematic Isomorphism**` bullet; UNSCORED).
- **canonical-statement:** Charge $q$ is a discrete geometric dislocation (localized phase twist) in the substrate; the Burgers vector is $\ell_{node}$, so $[Q] \equiv [L]$, with macroscopic scaling the Topological Conversion Constant $\xi_{topo} \equiv e/\ell_{node}$ [C/m]. Canonical: [`axiom-definitions.md:18-31`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) + `eq_axiom_2.tex` (`eq:axiom2_xi_topo`).
- **status:** **POSTULATED.** The charge-as-dislocation, $[Q]\equiv[L]$ isomorphism is a primitive; no derivation from weaker structure exists. (Charge quantization, sign, and $\mathbb{Z}_3$ fractional charges FOLLOW from it conjoined with Axiom 1 — but those are consequences OF the axiom, not derivations of it.)
- **provenance:** Postulated primitive. `eq_axiom_2.tex` states the canonical primitive from Vol 1 Ch 1; the calibration constants α and V_yield that once lived in an "Axiom 2 — Fine Structure" title were moved OUT to `eq_calibration_constants.tex` per the 2026-04-27 axiom homologation (they are derived, not axiomatic).
- **residual_content:** **the whole axiom** — the topo-kinematic isomorphism ($[Q]\equiv[L]$, charge = Burgers-vector dislocation, $\xi_{topo}$ scaling) is entirely axiomatic.
- **derived_by:** `(none — postulated)`.
- **count-effect:** counts as 1 independent axiom.
- **Axiom-2 tracking-state confirmation (brief §4).** Axiom 2's first-class node is the framework node `axiom-2` (materialized in claims.jsonl). Its content is additionally referenced by the scored claim **`clm-dfaiwj`** ([`vol1/claim-quality.md:690`](../vol1/claim-quality.md), "$\xi_{topo}\equiv e/\ell_{node}$ [C/m]; the SI-dimensional table follows"; confidence 0.80, solidity 0.80, `depends-on: Axiom 2` as a framework target) — but `clm-dfaiwj` is a **consequence claim that DEPENDS ON Axiom 2** (the SI-dimensional isomorphism table it unlocks), NOT the axiom itself. In [`axiom-definitions.md:20`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) the Tier-2 marker `<!-- claim-quality: clm-dfaiwj -->` sits on the Axiom-2 charge-dislocation paragraph. So Axiom 2 IS tracked: framework node `axiom-2` (the axiom) + `clm-dfaiwj` (a downstream consequence that cites it). The brief's "Axiom 2 unconfirmed" is resolved: it was never un-tracked as a node — it lacked only this status-register VIEW entry, now supplied. (The `clm-3kzmt9` notation-warning marker also physically sits in the Axiom-2 subsection of `axiom-definitions.md`, but it is the ξ-homonym / α-Class-B claim, not an Axiom-2 content node.)

---

## Axiom 3 — Minimum Reflection Principle
<!-- view of framework node: axiom-3 -->

- **axiom-node:** `axiom-3` (framework node, `node_type: "axiom"`; parsed from the CLAUDE.md INVARIANT-S2 `- Axiom 3: **Minimum Reflection Principle**` bullet; UNSCORED).
- **canonical-statement:** The substrate extremizes the macroscopic action $S_{AVE}$; two co-canonical forms — the **variational** form ($\mathcal{L}_{node} = \tfrac12\varepsilon_0|\partial_t\mathbf{A}_n|^2 - \tfrac{1}{2\mu_0}|\nabla\times\mathbf{A}_n|^2$) and the substrate-native **boundary** form (minimize the reflection $|\Gamma|^2$ at every internal impedance boundary). The two are equivalent (E-L equations enforce E/B continuity = the $|\Gamma|^2$-minimum condition). Canonical: [`axiom-definitions.md:36-46`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) + `eq_axiom_3.tex` (`eq:axiom3_lagrangian`, `eq:axiom3_boundary`; architectural label `eq:axiom3_action`).
- **status:** **POSTULATED.** No derivation of the extremal principle from weaker structure exists. (The variational ⇄ boundary EQUIVALENCE is **ASSERTED — a flagged underived dynamics leg** — and it relates two co-canonical FORMS of the one postulated axiom, so it would not derive the axiom itself even if it were tight.) **⚑ R43 (2026-08-10) — self-contradiction repaired (drift finding D2).** This field previously read *"the variational ⇄ boundary EQUIVALENCE is a proven internal theorem"*, which contradicted this same register's own DERIVED-LEGS row at `:231` (*"**ASSERTED-not-derived:** the **variational ↔ min-$|\Gamma|^2$ equivalence**"*, *"an **underived dynamics leg**"*). Adjudicated in favour of ASSERTED, because the canonical source of truth already says so and had already surfaced the divergence rather than overwriting it: [`eq_axiom_3.tex`](../../common_equations/eq_axiom_3.tex):37 — *"Equivalence (ASSERTED --- an underived dynamics leg)"*, *"a \textbf{flagged underived dynamics leg}"*, and, naming this very field, *"the register presently records this equivalence as a proven internal theorem; the field-continuity gap above is surfaced for adjudication rather than silently overwriting either statement."* Two concordant statements (`:231` + the canonical `.tex`) against one; the substantive gap is that field continuity holds at *reflecting* boundaries too, so EL-continuity is necessary but not sufficient for the $|\Gamma|^2$-extremum. Prior wording lives in git per the audit-trail-in-git-only convention. Ruling: [`2026-08-10-ruling-r43-ratification.md`](../../../_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md) — *"the register `:174`/`:231` self-contradiction repair ride the same execution."*
- **provenance:** Postulated primitive. Legacy name "Effective Action Principle" (the variational dialect). The substrate-native name follows the externally-observable quantity ($|\Gamma|^2$) per the substrate-observability rule.
- **residual_content:** **the whole axiom** — the minimum-reflection / least-reflected-action extremal principle is entirely axiomatic. (Note: Axiom 3's lossless-reactive extremal content is the primitive that MAKES the bond-LC L2 energy invariant exact — the invariant Axiom 4's SHAPE-DERIVED status leans on; see the Axiom-4 provenance below. Axiom 3 supplies the "lossless" half of that residual.)
- **derived_by:** `(none — postulated)`.
- **count-effect:** counts as 1 independent axiom.

---

## Axiom 4 — Universal Saturation Kernel
<!-- view of framework node: axiom-4 -->

- **axiom-node:** `axiom-4` (framework node, `node_type: "axiom"`; parsed from the CLAUDE.md INVARIANT-S2 `- Axiom 4: **Universal Saturation Kernel**` bullet; UNSCORED).
- **canonical-statement:** The substrate's bulk response to local strain $A$ (normalized to the bandwidth limit $A_{yield}$) is the universal quarter-arc kernel $S(A) = \sqrt{1 - (A/A_{yield})^2}$, $A \in [0, A_{yield}]$ — Maxwell recovered at $A=0$ ($S=1$), vertical-tangent impulsive saturation at $A \to A_{yield}$ ($S \to 0$). Governs all cross-scale saturation events (A-034 catalog). Canonical: [`axiom-definitions.md:48-58`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) + `eq_axiom_4.tex` (`eq:axiom4_saturation`).
- **status:** **SHAPE-DERIVED (conditional).** The *specific shape* $S(A)=\sqrt{1-A^2}$ is a **theorem** given a named residual primitive; it is NOT forced by generic saturation properties alone. Seeded at this honest current state — a reduction, NOT canonized (Grant: hold the full reduction for the orchestration epic). See the derivation, provenance, and open-epic notes below.
- **provenance:** Per the just-completed derivation on branch `analysis/axiom4-saturation-forced` @ `7170f40e` (`research/2026-07-02_axiom4-forced_result.md`, verdict "CONDITIONALLY-FORCED"): the shape is **uniquely forced by an L2-norm / fixed-radius constraint** ($A^2 + S^2 = A_{yield}^2$, i.e. $(A,S)$ is a fixed-length 2-vector), and **by nothing weaker** — the endpoints + Maxwell small-$A$ limit + vertical tangent are ALL satisfied by a whole family $(1-A^2)^p$ ($0<p<1$); only the **L2 (quadratic) norm** picks $p=\tfrac12$ (the kernel ↔ norm map is 1-1: an $L^p$ invariant forces $S=(1-A^p)^{1/p}$, a different curve for every $p\neq2$). The **Born-Infeld $n=2$ form is the same posit variationally** (Path B re-expresses the L2/quadratic content in a Lagrangian dialect; it adds no independent forcing). The forced part rests on a substrate-REAL invariant: the lossless bond-LC tank (Axiom 1 + Axiom 3) conserves $E=\tfrac12CV^2+\tfrac12\Phi^2/L$ exactly, so the *dynamical* phase-plane vector $(V/V_{max}, \Phi/\Phi_{max})$ traces a machine-precision circle — the L2 invariant is FORCED for the dynamical $(V_{inc},\Phi_{link})$ pair.
- **residual_content:** *(re-pinned 2026-07-02 — final wording; supersedes the earlier "L2-norm / fixed-radius" and the interim "combine-rule" wordings. The full Axiom-4 arc — reduction epic → DP-3 → buckling → moduli — resolved it.)* **The √ FORM is FORCED geometry, α-free; the residual is the yield ANCHOR, a GR-imported value.** The buckling derivation shows $S(A)=\sqrt{1-A^2}$ is the axial projection of a **fixed-arc-length K4 bond bowing** (Euler-strut geometry, α-free — the "L2 fixed radius" is the bond length, not an abstract posit); the moduli result sharpens this: for **any** finite stretch/bend ratio $\rho=k_a/k_s$ the bond settles at a self-consistent operating arc-length $arc^*$, so $S(A)=\sqrt{1-(A/arc^*)^2}$ is an **exact geometric √ — the *form* is forced, robust across $\rho$, not a chosen curve.** The "combine" question **dissolves**: the kernel is a **load-response bifurcation** (axial A1 dilatation load → transverse T2 bow response; $A^2+S^2=arc^{*2}$ is a *single fixed-length constraint*, not a norm over co-equal grades — the DP-3 L∞-vs-normalized-L2 fork was the wrong question, normalized-L2 being identically 1). **The genuine residual axiomatic content is the yield ANCHOR $arc^*$** — the effective yield strain, a few-% below the bare bond length $\ell_{node}$ ($arc^*\approx0.89$–$0.96\,\ell_{node}$ in the tent model, $\sim$0.79× that under the continuum elastica [band $\sim$4–13%], PR #462; an $O(1/\rho)$ deficit — the **structure** is model-robust, the exact prefactor model-dependent, and the exact $A$-independence is tent-specific, arc\* being the near-yield operating-point value) — and $arc^*$ **inherits from the GR-imported K=2G** ($\rho$ is K=2G-set: $\rho=2\Leftrightarrow$ K=2G; the sub-isostatic $z=4$ fixes only the FORM $K/G=f(\rho)$, not the value). Inextensibility ($k_{stretch}\gg k_{bend}$) does **NOT** hold — $\rho=$ slenderness$^2\in[2,5.3]$ (a stubby strut, not a thin elastica), and the elastica regime $\rho\gg1$ is affirmatively forbidden by K=2G. **FORM-derived / VALUE-imported (the framework's signature, cf. G and α): the √ form is forced geometry; the yield anchor $arc^*$ is an imported K=2G value. Content reduction (the form is no longer a free curve), NOT count reduction: axiom count stays 4.**
- **derived_by:** three structural/derivational research results (no scored `clm-` minted; not-yet-canonized research docs per Grant's hold): (1) `research/2026-07-02_axiom4-forced_result.md` (branch `analysis/axiom4-saturation-forced` @ `7170f40e`) — the within-tank L2 forcing + the L^p 1-to-1 map; (2) `research/2026-07-02_axiom4-reduction-epic_result.md` (merged PR #455) — FULL reduction **REFUTED**, the within-tank L2 promoted to airtight, the residual relocated to the cross-sector combine rule; (3) `research/2026-07-02_axiom4-combine-rule_result.md` (PR #457) — the combine is per-yield-normalized (single-radius-L2 falsified), cross-grade aggregation underdetermined at $O(\alpha)$; (4) `research/2026-07-02_axiom4-buckling-kernel_result.md` (PR #459) — the √ shape is the α-free inextensible-rod projection ($A_{yield}=\ell_{node}$) GIVEN inextensibility; the "combine" is a load-response bifurcation; residual sharpened to $k_{stretch}\gg k_{bend}$; (5) `research/2026-07-02_axiom4-moduli-hierarchy_result.md` (PR #460) — inextensibility FAILS ($\rho=$ slenderness$^2\in[2,5.3]$, K=2G-forbidden from being an elastica); the √ *form* is robust for any $\rho$ (exact in $u=A/arc^*$), but the yield anchor $arc^*$ inherits from GR-imported K=2G. Prior art: the **Q-G47** gate (`common/q-g47-substrate-scale-cosserat-closure.md`) closed only the OPERATING POINT $u_0^*$ where $S(A^*)=0$ — it took $S(A)$ and the $A^*=1$ boundary as INPUT, it did NOT derive the shape, and it never emits $S(A)$.
- **count-effect:** counts as 1 independent axiom (SHAPE-DERIVED does NOT move the count; the residual L2 primitive is the relocated axiomatic content, not a pre-existing one).
- **ρ-CONVENTION DISAMBIGUATION (cross-carrier — additive clarification, 2026-07-05; #527/#523 lineage).** The "$\rho=2\Leftrightarrow$ K=2G" clause above is the **moduli-model ρ** — the $k_a/k_s$ stretch/bend stiffness ratio of the buckling/Euler-strut derivation (the $z=4$/Keating convention that puts K=2G at $\rho=2$). This is a DIFFERENT ρ from the **srs swapped-spring ρ** used by the ratified chiral srs-z3 elastic tensor, where **K=0 at $\rho=2$ and K=2G at $\rho\approx9.7734$** (verified on the srs cold family, #527; e.g. [`../vol4/circuit-theory/ch1-vacuum-circuit-analysis/parent-condition-match-forces-balance.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/parent-condition-match-forces-balance.md) §3, and #518/#521 which operate at $\rho^\ast\approx9.77$). The two ρ's SHARE the symbol across carriers (moduli-model buckling ρ vs srs swapped-spring ρ); they are not the same coordinate. Read every "$\rho$" in this register field as the **moduli-model** ρ; a bare "$\rho=2\Leftrightarrow$K=2G" without the carrier qualifier is ambiguous when set beside the srs numbers. (Surfaced by #527 §3b/§8.3; landed additively, the residual_content wording above is not rewritten.)
- **LOAD-RESPONSE SIGN RULE (the load-response-bifurcation phrasing IS a force-sign rule; #527 [SIGN-RULE-DERIVED], additive cross-link 2026-07-05).** The "$A^2+S^2=arc^{*2}$ load-response bifurcation (axial A1 dilatation load → transverse T2 bow response)" grammar above, read strictly as *which coordinate is clamped vs driven*, resolves the #526 pre-stress T-slot **sign** fork into a **channel-keyed rule** (derived from scratch from this fixed-arc-length microfoundation, not the pair-potential analogy): a **transverse pluck** lengthens the arc via the bow ⟹ **TENSION** ($T>0$) ⟹ the #526 remap's $k_{shear\,eff}=k_s+T/\ell$ **GROWS ⟹ CAPPED** track; an **axial end-load** buckles the strut ⟹ **COMPRESSION** ($T<0$, sharing #526's $|\Phi'(A)|$ magnitude bit-exact, opposite sign) ⟹ $k_{shear\,eff}$ **SHRINKS ⟹ UNCAPPED** track. The verdict depends on $\text{sign}(T)$ ALONE (magnitude is a band); this is Grant's ratified "it does both depending on interaction." **T2 HOMONYM GUARD (binding — rides this note):** the "T2 bow" here is the **mechanical bow COORDINATE** of the strut (the transverse displacement in $A^2+S^2=arc^{*2}$), NOT the **Cosserat (2,3) micro-rotation charge winding** (a static reactive charge boundary carrying no real power, $A1\perp T2$ per `master-equation.md`; both internal dynamical loci #415/#417 NEGATIVE). mass=A1; charge=Cosserat-winding; bow=T2-mechanical-response — do NOT cross-wire. **Class:** CONSISTENCY (resolves a #526 sign axis; no new VALUE — 2/7, 9.7734, /7 stay GR-imported). Provenance: `research/2026-07-04_bond-force-sign-rule_result.md` (§4 grounding, §9 cross-link candidate). Open (flag for Grant, NOT landed): if the electron self-trap wall is the STATIC T2 winding (no real power), what physically PLUCKS the bond in matter to deliver arm-(a)'s transverse bias? — a substrate-ontology question surfaced, not resolved (#527 §4).
- **ARC COMPLETE (2026-07-02) → FULL reduction REFUTED; the residual is fully characterized.** Five derivations (reduction epic → DP-3 → buckling → moduli, PRs #455/457/459/460) drove Axiom-4's residual from an abstract "L2-norm posit" to a fully-understood object: the kernel **√ FORM is a robust α-free geometric theorem** (the fixed-arc-length compressible-strut projection, exact in $u=A/arc^*$ for any $\rho$), and what stays axiomatic is the **yield anchor $arc^*$, inherited from the GR-imported K=2G** — the framework's **FORM-derived / VALUE-imported** signature (cf. G, α). Axiom 4 stays SHAPE-DERIVED **(conditional)**, count 4. **The only remaining reduction** would be forward-deriving K=2G from Axiom 1 (currently GR-imported; the standing `Chain B′` problem in [`interlock-register.md`](interlock-register.md)) — a separate arc. **Do NOT restate Axiom 4 as a theorem in `axiom-definitions.md` / `eq_axiom_4.tex`** — the √ form is forced but its anchor is imported, so the axiom does not collapse to a theorem. Forward prediction surfaced (PR #460, scoped PR #462): the effective yield strain is $arc^*<\ell_{node}$ by an $O(1/\rho)$ deficit (~4.5–11% tent / ~4–13% continuum-elastica; $O(1/\rho)$ structure model-robust, exact % model-dependent). **PR #462 verdict: this is an INTERNAL REFINEMENT, not a bench falsifier** — the measurable yield is α-anchored ($V_{yield}=\sqrt\alpha\,V_{snap}$), so the geometric arc\* deficit is absorbed by the α-anchor and moves no bench observable; the AVE-distinct content is the saturation curve's *existence*, not the knee position. The corpus's standing self-statements remain correct and are now *explained*: [`trampoline-analogy-primer.md:192`](trampoline-analogy-primer.md) "**Axiom 4 remains postulated**"; [`common/claim-quality.md:805`](claim-quality.md) "the kernel is the **postulated** Axiom 4 form."

---

## Summary — status roll-up + count

| Axiom | node | status | residual_content | count-effect |
|---|---|---|---|---|
| **1** Substrate Topology | `axiom-1` | POSTULATED | whole axiom (K4 Cosserat crystal topology) | counts (1) |
| **2** Topo-Kinematic Isomorphism | `axiom-2` | POSTULATED | whole axiom ($[Q]\equiv[L]$ dislocation isomorphism) | counts (1) |
| **3** Minimum Reflection Principle | `axiom-3` | POSTULATED | whole axiom (least-reflected-action extremal principle) | counts (1) |
| **4** Universal Saturation Kernel | `axiom-4` | SHAPE-DERIVED (conditional) | the L2-norm / fixed-radius energy constraint | counts (1) |

**LIVE independent-axiom count = 4** (`expected-independent-axiom-count: 4` in
the `axiom-meta` block). Four `axiom-N` framework nodes; **zero** at
DERIVED-TO-THEOREM. Axiom 4's SHAPE-DERIVED status is a content reduction, not a
count reduction — the residual L2-norm primitive is the relocated axiomatic
content. The count drops `4 → 3` only if an axiom's *whole* content becomes a
theorem of the others + a bare pre-existing identification (DERIVED-TO-THEOREM),
which the Axiom-4 full-reduction epic would test but has not established. **⚑ R43/R44 (2026-08-10) — this roll-up is INCOMPLETE and is NOT silently rewritten (line-shift discipline: the rows above carry inbound `:NN` cites).** A FIFTH axiom, **BC-SRC**, was ratified on 2026-08-10 — *"This is the first new axiom ratified since the founding set"* — and its full register entry, its summary-table delta, and the enumerated machine-side blocker on its `axiom-N` framework node are appended at the END of this file under **"Axiom 5 — BC-SRC"**. Read that section together with this line. **UPDATE (same day): the gap is CLOSED** — the `axiom-5` framework node now EXISTS (the `[1-4]`->`[1-5]` parser widening landed under R47 item 1), so the framework-node count and the ratified-axiom count now AGREE at **five**, and `expected-independent-axiom-count` in the `axiom-meta` block above reads 5. **UPDATE (R55, 2026-08-24): SUPERSEDED** — the Substrate DC Bias was restructured **axiom → SOURCE LAW** (`2026-08-24-ruling-r55-axiom5-source-law.md`); the `axiom-5` node is RETIRED (zero inbound depends edges at retirement), the count returns to **four**, and the end-of-file entry is now the SOURCE-LAW entry. The four-axiom roll-up above is again complete as written.

## Per-axiom DERIVED-LEGS (dictionary-vs-dynamics decomposition)

A finer view than the `status` axis: each axiom is decomposed into (1) what it
**DEFINES** (its *dictionary* content — a naming/identification, not a dynamical
claim), (2) what **dynamics** it **ASSERTS**, and (3) which of those assertions
the **engine has DERIVED** (with `clm-` / result cite) vs which remain
**ASSERTED / OPEN**. This is the P1 audit template made canonical: **the
underived legs ARE the next-arc map** — each ASSERTED/OPEN cell is a live
derivation target. A DERIVED leg does **not** change the axiom's `status` (an
axiom's dynamics being partly engine-confirmed is a *content* fact; only whole
content becoming a theorem-of-the-others moves the count — see the status axis).

| Axiom | DEFINES (dictionary) | ASSERTS (dynamics) | DERIVED (engine, cited) | ASSERTED / OPEN |
|---|---|---|---|---|
| **1** | the substrate: K4 Cosserat crystal lattice + per-node 6-DOF (3 transl→$\varepsilon_0$, 3 microrot→$\mu_0$) | the lattice *responds* — impedance, screw kinematics, buckling | **three-impedance law** ($Z_{EM}/Z_{shear}/Z_{bulk}$, graded-network); the **$4_1$ screw operator** (chiral holonomy); the **buckling-kernel SHAPE chain** (fixed-arc-length strut projection → Axiom-4 √ form, PRs #459/#460) | **[re-scoped 2026-07-11 → migration-legs-only]** the **D1 $z{=}3$ identity itself is SETTLED** — D1 RATIFIED (Grant 2026-07-03: srs-z3 is the production carrier, `_orchestration/index.md` §2026-07-03; the diamond $z{=}4$ engine re-tagged a non-canonical instrument). What remains OPEN is **only the register MIGRATION legs**: the **continuum-limit legs** (rigorous lattice→continuum) + the module-inventory migration (`_orchestration/2026-07-03_srs-migration-policy.md`). *KEEP-BOTH — original wording preserved: "the **D1 $z{=}3$-vs-$z{=}4$ production identity** (unified-srs arc tension — bare srs instrument $z{=}3$ vs diamond production engine $z{=}4$); the **continuum-limit legs** (rigorous lattice→continuum)".* |
| **2** | $[Q]\equiv[L]/\xi_{topo}$ — charge = Burgers-vector dislocation ($\xi_{topo}\equiv e/\ell_{node}$) | HOW windings interact (coupling class); charge sign; formation; $\mathbb{Z}_3$ splitting; **the EM-READOUT leg** — does the winding's charge label emerge as a *sourced* static exterior field? | the **INTERACTION leg** — `clm-wcoul2` (2026-07-03, **lands with PR #466**): like windings **repel** / unlike **attract**, signed-Coulomb sign structure under the winding=charge mapping, gapped-ω-mediated (electric-not-magnetic) — the **first engine-derived winding-pair interaction** (CONSISTENCY-class; sign-only, magnitude BLOCKED) | **computed-NULL:** the **displacement-PUMP leg** — `clm-clvchn` (**NULL-CONFIRMED-FINAL**, $C{=}0$ registry-pump Chern over the $4_1$ texture). **EM-READOUT leg = FOUR-LOCK CASCADE** (`clm-nogo4l`, 2026-07-03): the *sourced-static-monopole* route is closed by four locks — (1) blind-readout retraction (instrument, PR #477); (2) sourced-solve tautology (instrument, Stage-1b $\nabla{\cdot}E=+(\text{source}-\text{mean})$); (3) [NO-FLUX-STRUCTURAL] maximum principle (theorem, $\varepsilon{>}0$); (4) $\partial\partial{=}0$ continuity (**DERIVATION GRADE** as of 2026-07-03 β-arc PR #488, upgraded from theorem-grade lean: the coupling zoo was swept + $\nabla{\cdot}J$ computed per branch → [NO-AXIOM-NATIVE-TERM]; the one J-mixed candidate (A44 converter) sources a globally-**neutral** polarization texture, $\text{sum}(\nabla{\cdot}J){=}0$ exact, chirality closed-negative). **The dynamical (lane Y) route to a sourced net monopole is CLOSED at derivation grade.** **SURVIVOR MAP:** lane Z (harmonic sector $\ker\partial_1\cap\ker\partial_2^\top$, $b_1{=}3$) — **step-0 result** (`research/2026-07-03_lanez-fluxoid-step0_note.md`, PR #489): the $\Delta b_1{=}{+}1$ core-linking meridian DOF is **confirmed on $H_1$** for the (2,3) torus core (disc-fill-certified; a ball core opens none), but its charge VALUE is **[DOORWAY-NO-PINNING]** — the three axiom-native pinning candidates (LC-phasor single-valuedness, the $\xi_{topo}\equiv e/\ell_{node}$ dictionary, the $S{\to}0$/$\Gamma{=}{-}1$ wall BC; §4 pinning ledger) pin only the *integer* holonomy, reduce to the $\xi_{topo}$ ECHO, or fail to fix flux. Lane W (pairs, `clm-wcoul2`) — **step-0 CLOSED at FORM grade** (`research/2026-07-03_lanew-pair-field-form_prereg.md` §3.7, PR #492): the massless-channel winding-pair field (A44 neutral-texture-mediated) is **[MULTIPOLE-FORM]** ($p{=}{-}3.0$ dipole-dipole or steeper, NOT $p{=}{-}1$ Coulomb; monopole forced zero) — the honest charge-FORM negative, so the pair channel derives no Coulomb monopole either. The J-mixed term is NOT a survivor route to net charge (it names a future *bound-charge form-factor* study, not a sourced escape); one residual **framing fork** (net-monopole vs holonomy-far-field) surfaced to Grant. **EM-READOUT LEG — FINAL STATE: CLOSED, BRANCH 3 (Grant-ratified 2026-07-03).** Every live lane has reported; the epic closes on the charter's §2 branch 3 — *"UNDERIVABLE (stuck at grade) — a permanent FORM-level ceiling on charge-as-winding unless/until new machinery: the honest 'posited forever' state, named."* **The ceiling is LOCATED** at the London-analog integer→flux-VALUE conversion ($\xi_{topo}\equiv e/\ell_{node}$, the α-echo): the FORM is derived (Link integer + holonomy + linking-DOF + neutrality forced), the VALUE imported (see [`common/form-deriving-value-importing.md`](form-deriving-value-importing.md) §"Charge-flux" + the cold-eyes charter-vs-grade adjudication `research/2026-07-03_cold-eyes-program-audit_result.md` §4). Peer-with-SM is context only (both import the charge quantum; SM anomaly-cancellation constrains charge ratios — the "SM doesn't derive quantization" line retired; the genuine surplus = integer FORM + forced neutrality + no-sourcing + ball-vs-torus $\Delta b_1$). *Scope: charge is UNSOURCED, not failed; topology/pairs live; the $\varepsilon{\to}0$ puncture is lane Z's doorway.* See [`the-sourced-charge-no-go-cascade.md`](the-sourced-charge-no-go-cascade.md) §"The epic closure — BRANCH 3". **ASSERTED/OPEN:** winding-**formation**/genesis (leans-falsified *as a route*, not as existence); **fractional-charge $\mathbb{Z}_3$** splitting |
| **3** | lossless-reactive extremal principle, in two co-canonical FORMS: **variational** ($\mathcal{L}_{node}$) and **boundary** (min $|\Gamma|^2$) | the substrate *evolves toward* the extremum (and the two forms agree) | **Noether consequences** in the continuum limit (conservation laws — *with the emergent-Lorentz qualifier*) | **ASSERTED-not-derived:** the **variational ↔ min-$|\Gamma|^2$ equivalence** — the EL-continuity argument is **loose** (field continuity holds at *reflecting* boundaries too, so "EL ⟹ $|\Gamma|^2$-minimum" is not tight); an **underived dynamics leg** awaiting its own engine adjudication: *"does the engine evolve toward reflection minima?"* |
| **4** | $S(A)=\sqrt{1-(A/A_{yield})^2}$ — the universal saturation kernel | the response *has this specific √ shape*, with a yield anchor, combined across grades | the kernel **SHAPE** (the √ form is a robust α-free geometric theorem — fixed-arc-length strut projection, exact in $u=A/arc^*$ for any $\rho$; buckling-kernel arc, **conditional on the $arc^*$/K=2G anchor** — see this register's Axiom-4 `residual_content` + `derived_by`, PRs #459/#460) | **cross-grade combine rule** underdetermined at $O(\alpha)$ (**PR #457**); the ceiling's **HARDNESS** (yield *exists* — derived — vs yield is *hard/impulsive* — open); the **yield-anchor $arc^*$ = K=2G import** (GR-imported value, standing `Chain B′` in [`interlock-register.md`](interlock-register.md)) |

> **Non-conflation guard (Axiom 2, load-bearing).** `clm-wcoul2` (the DERIVED
> interaction leg) and `clm-clvchn` (the NULL pump leg) are **different
> observables** — the pair-interaction SIGN over the mid-plane ω-field
> normal-stress vs the single-plate displacement→charge registry-pump Chern. **The
> derived pair-interaction does NOT reopen the pump / Cleave-01.** A REOPEN of
> `clm-clvchn` needs a nonzero gap-independent displacement-charge floor, which
> `clm-wcoul2` neither measures nor implies.
>
> **Consistency legs are enabling infrastructure.** `clm-wcoul2` is CONSISTENCY-
> class (signed-Coulomb is SM-shared) — booked here **not** as a chord but because
> it **derives an axiom's dynamics leg**. Each such leg is recorded with *"what
> hunt does this newly enable?"*: the Ax2 interaction leg is the substrate any
> future winding-pair *magnitude* chord must stand on (once $\omega_{gap}$ is
> mapped to $\Omega_C$ and a plane-conservative force integral is found —
> `clm-wcoul2` strengthen-by).
>
> **Merge-order note.** `clm-wcoul2` is minted on
> `analysis/writhe-campaign-linear-channel` (PR #466); if that has not merged when
> this register lands, the Axiom-2 DERIVED cell **stacks on PR #466** (verified
> present in this branch's tree, absent from `origin/main` at authoring time).

## Schema / gate note (flagged for the auditor + Grant — NOT built this pass)

This register is a **VIEW leaf** and needs no new node-type to be correct today:
it originates no node-body (frontmatter `no-claim`), and the four `axiom-N`
framework nodes it views are already materialized + gated. But two extensions
would make the register's derived quantities **machine-enforced**, mirroring the
interlock register's CI-gated `expected-independent-count`. Both are **flagged,
deliberately NOT built** in this pass (get the leaf right first; a schema change
is Grant-ratify-gated canonical infrastructure):

1. **A `status` field on the framework-node record + an `axiom-meta` parser.**
   The `axiom-N` framework record is currently 5 fields with no status. To make
   `status` machine-tracked (and the `expected-independent-axiom-count`
   CI-asserted the way the interlock count is), `verify-kb-metadata` would need
   to (a) parse the `axiom-meta` block + the per-axiom `status:` fields here,
   (b) recompute the count = `(# axiom-N nodes) − (# DERIVED-TO-THEOREM)`, and
   (c) fail loudly on drift. **Design question for Grant:** should the axiom
   `status` live as a 6th field ON the framework-node record (parsed from THIS
   register, the way `ilk-` tags drive the interlock count), keeping the axiom's
   status in one machine-read place — OR stay a hand-maintained view field
   (loud only to a human reader) until an axiom actually approaches
   DERIVED-TO-THEOREM? The interlock precedent argues for wiring it; the
   conservative read is that with zero axioms near a count-change, the gate
   earns its complexity only when the epic lands.

2. **Nothing else.** No new id prefix, no new edge class, no new node-type — the
   axioms are already nodes (INVARIANT-S11 satisfied by reusing `axiom-N`).

**Design decisions made in this pass that Grant should ratify** (surfaced, not
silently committed — this is canonical infrastructure):

- **(D-A) Register-as-VIEW, not new-id-scheme.** The axioms are already
  `node_type: "axiom"` framework nodes, so this register mints NO new axiom id
  and re-declares nothing — it is a status/provenance/residual VIEW over
  `axiom-1..4` (the exact pattern of the interlock register's per-constant
  criteria section). *Alternative rejected:* minting fresh `axm-`-style ids
  would be a parallel scheme forbidden by INVARIANT-S11.
- **(D-B) `status` is a view field, not a node scoring field.** Axioms are
  UNSCORED framework bedrock; `status` records derivational maturity of
  *content*, and a derived axiom's solidity lives on the theorem `clm-`/result
  it points at via `derived_by`, never on the axiom node.
- **(D-C) The four-value status axis** {POSTULATED, SHAPE-DERIVED, CHALLENGED,
  DERIVED-TO-THEOREM} with only DERIVED-TO-THEOREM moving the count — chosen to
  make "content reduction (Axiom 4) vs count reduction" machine-legible and to
  keep the count honest (SHAPE-DERIVED does not fabricate a parameter drop).
- **(D-D) `expected-independent-axiom-count: 4` hand-asserted, gate deferred.**
  Per item 1 above — flagged for Grant's ratify on whether to wire the CI gate
  now or when the epic lands.

---

## The Substrate DC Bias SOURCE LAW (deposit · grade · quiescence) — formerly Axiom 5

> **★ THE FIRST NEW AXIOM RATIFIED SINCE THE FOUNDING SET.** Ratified
> 2026-08-10 under R43. Source of record:
> [`2026-08-10-ruling-r43-ratification.md`](../../../_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md):22
> — *"This is the first new axiom ratified since the founding set."* Clauses S
> and G were first recorded in the companion partial record (**SUPERSEDED IN SCOPE per
> R44**; body preserved, cite the full record)
> [`2026-08-10-ruling-r43-sg-ratified.md`](../../../_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md);
> clause Q and the vocabulary ruling ride the R43 ratification record on top.
> **This section is appended at the END of the register rather than slotted after
> Axiom 4 deliberately**: the Axiom-1..4 sections and the roll-up table carry a
> dense inbound `:NN` cite surface (max inbound `:232` at authoring) and an
> in-place insertion would silently shift every one of them.

> **★ R55 (2026-08-24): RESTRUCTURED — AXIOM → SOURCE LAW.** Ruling:
> [`2026-08-24-ruling-r55-axiom5-source-law.md`](../../../_orchestration/docket-entries/2026-08-24-ruling-r55-axiom5-source-law.md)
> — *"four axioms + a source law."* The container is re-graded; every ratified
> clause (S data / G law / Q reference), value, named-open, and the falsifier
> stand untouched. The `axiom-5` framework node is RETIRED (zero inbound
> `depends` edges at retirement — measured receipt in the ruling). The banner
> above is HISTORICAL — true of its date, superseded in grade. The pre-R55
> wording below is preserved; read "axiom" in this section's historical text as
> the source law.

- **axiom-node:** **RETIRED per R55 (2026-08-24).** Arc, kept whole: NOT YET
  MINTED at authoring (the disclosed gap, routed) → minted same-day under R47
  item 1 (the `[1-4]`->`[1-5]` parser widening) → **retired at the R55
  restructure** (parser reverted to `[1-4]`; zero inbound `depends` edges at
  retirement, so nothing dangled). The source law deliberately carries NO
  framework node until a consumer needs one — a machine node with zero
  consumers is machinery without a load (INVARIANT-S11 extension deferred).
- **canonical-statement:** The four founding axioms write a *floating* network —
  topology (Ax 1), charge dictionary (Ax 2), lossless extremal dynamics (Ax 3),
  saturation kernel (Ax 4) — but never write the source coupling that pins the
  bound (A1 dilatation) sector's absolute state. **BC-SRC is that missing
  specification: the substrate's DC operating point.** Canonical:
  [`eq_axiom_5.tex`](../../common_equations/eq_axiom_5.tex)
  (`eq:bcsrc_deposit`, `eq:bcsrc_bridge`, `eq:bcsrc_quiescence`,
  `eq:bcsrc_falsifier`). **Three clauses, ratified together** — clause text
  landed AS RATIFIED from
  [`2026-08-10_bound-constitutive_result.md`](../../../research/2026-08-10_bound-constitutive_result.md)
  §2.6, with the R43 / R43-S+G ratification records' expansions folded in where
  they add content:

  - **S (deposit).** *"A matter defect deposits a nonzero net A1 dilatation flux:
    `∮_S u·n̂ = 4πB(M)` over any enclosing exterior surface, with `B(M)` = the
    defect's A1 mass accounting (dimensional VALUE via the imported G/ξ chain)."*
    Ratified expansion (S+G partial record, SUPERSEDED IN SCOPE per R44 — record-of-origin only): every defect deposits this flux **at genesis** —
    particles are factory-charged; **mass is an enclosed compression charge BY
    LAW**. The write event is a genuine new law (the four-lock no-go bars the
    receipted dynamics from creating it); KCL / the derived conservation leg
    preserves it thereafter.
  - **G (bias coupling / bridge).** *"The operating-point grade is the bound
    sector's potential: `u₀ = −λ∇ε₁₁`, with the grade pinned by the elliptic law
    `−∇·[κD(A)∇ε₁₁] = T₀₀`, `κ = c⁴/7G` (VALUE imported). Equivalently: the canon
    backreaction solve becomes BC-LAW in potential form."* Ratified expansion
    (recorded in the S+G partial record, **SUPERSEDED IN SCOPE per R44** — cited as
    record-of-origin only; the authoritative record is the full-scope R43 ratification): read as a circuit this is the **DC-bias-network law** — mass-energy
    injects current, the saturation-graded conductance distributes the potential
    ε₁₁ (THE BIAS), the BOUND RESPONSE is its field, κ is the bias sector's
    permittivity.
    `backreaction.py`'s elliptic statics becomes **axiom-licensed**. **One new
    coupling constant, $\mathcal{A}_g$** (the BIAS-COUPLING AREA, [m²]; R50's re-read of R46's "grade-coupling area"), enters the framework
    here and nowhere else. **⚑ SYMBOL RETIREMENT (R46, 2026-08-10):** the verbatim
    clause text above still reads `λ` because it is quoted verbatim from the source
    lane and verbatim text is not rewritten. **`λ` is RETIRED for this role** —
    wavelength and Lagrange-multiplier collisions — and the ratified symbol is
    **𝒜_g**. Collision receipt (R46, re-verified here two-method): the ξ family is
    crowded (seven members, ξ_topo alone ×790) so ξ_g was REJECTED, while
    `\mathcal{A}` carries exactly one other subscripted member corpus-wide — 𝒜_g is
    clean. Read every `λ` inside the quoted clause as 𝒜_g. **The same applies to `grade` and
    `dress` in that quote:** R50 demoted "grade" from ε₁₁'s canonical name to informal
    use (canonical noun: **THE BIAS**) and retired "dress" (canonical: **the bound
    response**). The quoted clause is likewise left verbatim — read every `grade`
    inside it as **bias**, and `dress` as **bound response**.
  - **Q (quiescence — the DC operating point).** *"The sourceless substrate sits
    at the cold operating point: `∇·π = 0`, `θ = 0`, `ε₁₁ = 0` away from
    defects."* Ratified role (R43): this is **the DC OPERATING POINT — the
    quiescent reference that makes potentials defined and G's solve well-posed**.
    **⚑ Reconciliation finding (surfaced, not silently resolved):** the §2.6
    source text closes clause Q with the hedge *"(Possibly already canon — the
    cold-quiescent operating-point definition; bundled for completeness and
    flagged as such.)"* R43 ratified Q as a full load-bearing clause with a named
    role, so that hedge is **superseded by the ratification** and is recorded here
    rather than carried forward as live text.

- **VOCABULARY RULING (R43, binding on every consumer).** The canonical term is
  **"DC operating point / quiescent point (Q-point)"**. **"Ground (reference)" is
  the EE-analogy gloss, NEVER the canonical noun.** Grant's physical framing of
  record — *"BC-SRC is the GROUND REFERENCE of the floating network the bare
  axioms built"* — is quoted as the analogy, and the canonical noun is used in
  every surrounding statement. The proposed `quiescent point` vocabulary node
  ([`def-q1escn`](vocabulary-register.md)) **promotes to ratified under this
  naming**.
- **status:** **POSTULATED.** BC-SRC is a new axiomatic primitive, not a theorem
  of Axioms 1–4. *(R55, 2026-08-24: read "axiomatic primitive" as "postulated
  source-law primitive" — container re-graded, derivation status unchanged.)* **Minimality is established by ablation, not asserted:** without
  **S** the derived conservation legs leave the bound-response value unpinned; without
  **G** there is no receipted home for the finite static stiffness, no
  bias-reading causality, no energy functional, and no derived connection to the
  static /7 chain; without **Q** the conserved data is unpinned far from sources.
  No clause is derivable from the receipted action — S has no energy→flux map, G's
  κ has no axiom preimage, Q is definitional-or-canon.
- **provenance:** Postulated primitive, ratified 2026-08-10 (R43 + the R43-S+G
  companion). Produced as the minimal new-axiom candidate of the bound-sector
  constitutive lane, which ran its own Tier-2 (44 agents, 5 lenses) BEFORE
  presentation and re-binned all four of its deliverables
  `DERIVED-VIA-NEW-AXIOM(BC-SRC)` rather than `DERIVED`.
- **residual_content:** **all three clauses.** S (the nonzero, M-proportional
  deposit), G (the bias↔bound-response bridge + the κ-stiffened elliptic bias law), and
  Q (the quiescent DC operating point) are the axiom's own content. **FORM-derived
  / VALUE-imported** per the framework's standing signature: κ = c⁴/7G and
  ν = 2/7 stay GR-imported (#261 untouched) and B(M)'s dimensional normalization
  rides the imported G/ξ chain; **𝒜_g is a genuinely new constant.**
- **derived_by:** `(none — postulated)`. What the lane DID derive, and what
  therefore does **not** belong to this axiom's residual: the conservation leg
  `∂_t(∇·π) = −∇·j_m`; the kinematic freeze; the exterior uniqueness of the bound response `u₀ = B r̂/r²`;
  zero longitudinal characteristic speed; the (u,π)-sector domain-of-dependence
  theorem; the exact Kirchhoff-transformed energy functional; the pole-absence
  half. Those are theorems of the receipted dynamics, cited at
  [`2026-08-10_bound-constitutive_result.md`](../../../research/2026-08-10_bound-constitutive_result.md).
- **count-effect:** counts as **1 independent axiom**. The **ratified-axiom count
  is 5**; the **framework-node count remains 4** until the node lands (below).
  Both numbers are stated because they currently differ — neither is quietly
  adjusted to match the other. *(R55, 2026-08-24: SUPERSEDED — counts as the ONE
  source law, zero axioms; both counts read 4 and AGREE; see the LIVE count line
  below.)*
- **internal falsifier (ships with the axiom):** clauses S + G jointly force
  `B = 7·𝒜_g·GM/c²`. **One 𝒜_g across every consumer** — measuring 𝒜_g from two
  independent consumers over-determines it, and the over-determination is the
  axiom's own test port. This is the first axiom in the register to arrive with a
  built-in falsifier rather than an appended one; the 𝒜_g over-determination lane is
  the ratification's first follow-on derivation.

### Machine-side status — the `axiom-5` framework node is MINTED (blocker discharged 2026-08-10)

> **R55 (2026-08-24): the node is now RETIRED** — see the **axiom-node** bullet at
> the top of this section for the full arc. This subsection below is the frozen
> 2026-08-10 minting record; its "MINTED" header names its own date's state.

> **⚑ SUPERSEDES the "BLOCKED (enumerated, routed)" section that stood here.** That
> section correctly enumerated two blockers and routed them rather than forcing them.
> **R47 item 1 ruled GO**, and both are now discharged in-branch:

1. **The tooling blocker — DISCHARGED by a minimal parser widening.** The bullet
   parser was hard-capped at axioms one through four, so an `- Axiom 5:` bullet would
   have **silently** produced no node and no error. Widened at
   `manuscript/ave-kb/tools/kb_index_lib.py`:180 to
   `` `_AXIOM_BULLET_RE = re.compile(r"^- Axiom ([1-5]): \*\*(.+?)\*\*")` `` and the
   in-bullet token regex at `:183` to `` `\bAxiom ([1-5])\b` ``. **Minimal by
   construction:** bumped to the live count, NOT opened to `\d+`, so a typo'd
   "Axiom 9" still fails loudly instead of quietly minting a node.
   **★ AND THE SILENT-DROP MODE ITSELF IS DEAD, not merely narrowed** (Grant: *"kill
   the mode, not just the range"*). The parse is now **broad-RECOGNIZE then strictly
   PARSE**, with **three outcomes and no fourth**: *parsed* / *not-a-bullet* (silent,
   correct — absence is not malformation) / **MALFORMED → RAISES
   `FrameworkNodeParseError`** naming the file:line. The recognizer is
   `` `^\s*-\s*Axiom\b` `` — **leading indentation included**, which matters because
   indentation is *the* canonical malformation: the parse-error docstring names it
   first and this repo's own regression fixture mangles by indenting. An earlier cut
   of this batch wrote `` `^- *Axiom\b` `` (the star AFTER the dash), which **cannot
   match an indented bullet at all** — so the hole survived the widening and was found
   by review, not by me. Closed with two regression tests, one the **Axiom-5-specific**
   case: `axiom-5` has **zero** inbound `depends-on` edges (axiom-1: 99, axiom-2: 38,
   axiom-3: 30, axiom-4: 101, **axiom-5: 0**), so dropping it dangles nothing and the
   downstream `_assert_framework_node_coverage` backstop **cannot** see it — the
   parse-time recognizer is the only thing that can.
   **AUTHORING CONSTRAINT, documented because it is a real fence:** a prose bullet that
   merely opens with `- Axiom N` (e.g. `- Axiom 3 forbids dissipation.`) now
   **hard-fails the indexer**. Blast radius is one file and it fails loud, so the
   direction is right — but write such prose without the leading-bullet form.
   **Before/after receipt** (`make refresh-kb-metadata`, same tree, one variable
   changed): BEFORE → `['axiom-1','axiom-2','axiom-3','axiom-4']`; AFTER →
   `['axiom-1','axiom-2','axiom-3','axiom-4','axiom-5']`, the new record titled
   *Substrate DC Bias* with `canonical_anchor: invariant-s2-ave-axiom-numbering`.
2. **The blast-radius blocker — DISCHARGED without moving a single cite.** The
   INVARIANT-S2 bullet did NOT go inline (that would have shifted the 23 distinct
   inbound `:NN` cite lines in KB `CLAUDE.md`, including the heavily-cited
   `:73`/`:75` operating-point pair and cites as deep as `:318`). It went at the END
   of `CLAUDE.md` under an explicit **"INVARIANT-S2 continuation"** heading, with the
   S2 lead-in edited same-line to point at it. The parser scans the whole file, so
   the materialized node is identical either way — verified by the anchor above.
   **All 23 cite anchors re-verified unshifted post-edit.** The `##` heading is
   deliberate: an `### INVARIANT-…` heading would have minted a spurious invariant.

> **⚑ UNAVOIDABLE SIDE-EFFECT, DISCLOSED: minting a node shifts `.index/claims.jsonl`
> line cites by +1.** `claims.jsonl` is GENERATED and stable-sorted, so inserting the
> `axiom-5` record pushes every later record down one line. Three tracked line-cites
> into it are affected, and the re-resolution map is given here because one of the
> citing documents is a FROZEN prereg and cannot be re-pointed:
>
> **Complete map — all SIX affected cites** (re-derived range-aware at the final tip;
> an earlier cut of this note listed only three, which was an undercount):
>
> | Cite | Record it meant | Now at | Citing site(s) |
> |---|---|---|---|
> | `claims.jsonl:17` | `clm-2e9j97` | `:18` | `research/2026-07-20_ringdown-systematics_derivation.md`:19 |
> | `claims.jsonl:122` | `clm-f5ucdo` | `:123` | `research/2026-06-15_grid-definition-cartography.md`:187 |
> | `claims.jsonl:203` | `clm-mroghg` | `:204` | `_orchestration/2026-08-02_manuscript-reconciliation-board.md`:172 |
> | `claims.jsonl:239` | `clm-q8un7j` | `:240` | `…k4-zone-edge-nyquist-settle_prereg_FROZEN.md`:39 (**FROZEN**) + its result `:87` |
> | `claims.jsonl:252` | `clm-refjr6` | `:253` | `research/2026-06-24_engine-reroute-epic-summary.md`:93 + two docket entries |
> | `claims.jsonl:357` | `def-b0nd01` | `:358` | `research/2026-08-06_iomega-law_result.md`:686 |
>
> **R55 STALENESS NOTE (2026-08-24): five of the six "Now at" values above are
> stale** — retiring the `axiom-5` record re-shifts `claims.jsonl` back by −1,
> so those five rows resolve at their ORIGINAL "Cite" values again. The
> `def-b0nd01` row is the exception: its "Now at" `:358` had already drifted
> pre-R55 (measured pre-R55 position `:359`), and the retirement shift lands it
> back on `:358` — the one stale column value that still resolves, by
> cancellation, not correctness. Measured at the R55 tip: `clm-2e9j97` at `:17`; `clm-f5ucdo` at `:122`; `clm-mroghg` at `:203`; `clm-q8un7j` at `:239`; `clm-refjr6` at `:252`; `def-b0nd01` at `:358`.
> Resolve by the durable node id, never by either line column.
>
> **Root cause, stated so it is not re-learned:** a `:NN` cite into a generated,
> stable-sorted index is inherently volatile — ANY new `clm-`/`def-`/`sup-`/axiom
> node moves it. The durable citation form is the **node id** (`clm-q8un7j`), which
> is greppable and shift-proof by construction. Not repaired here (frozen prereg;
> and the practice, not this landing, is the defect); routed.

**Consequently `expected-independent-axiom-count` is now 5 and the two counts AGREE.** *(R55, 2026-08-24: superseded — restructured to source law; the node is retired and the count is back to 4. This paragraph is the frozen 2026-08-10 arc record.)*

> **⚑ THE ARC IN MINIATURE.** The axiom was ratified, registered, indexed and gated —
> and still did not exist in the book anyone would read, because no document `\input`
> the file. Wiring it into the foreword is the whole fix; noticing that the machine
> state and the readable state had silently diverged is the point worth keeping.
The earlier state — ratified-axiom 5, framework-node 4 — is closed, not papered over.

> **⚑ HOMONYM GUARD — "Axiom 5" is an overloaded token as of this landing.** Three
> live engine files use `Axiom 5` for an unrelated coupled-resonator normal-mode
> operator: `src/ave/solvers/coupled_resonator.py`, `src/ave/condensed/silicon_crystal.py`,
> `src/ave/condensed/silicon_doping.py`. They pre-date this axiom and are **NOT**
> renamed here — engine code is outside this lane's fence. Note the direction of the
> problem: before this landing that label pointed at *nothing*; it now silently
> re-targets onto a real axiom, so a bare `grep "Axiom 5"` returns two unrelated
> objects. **Canonically, "Axiom 5" means Substrate DC Bias and nothing else.** The
> engine token is the stale one; rename/disambiguation is routed, not done here.

### Per-axiom PHASE-STRUCTURE map (R45 comprehensive doctrine; R47 item 5)

**This is a phase-structure column, NOT a scope-limitation column.** Each axiom is a
law of the MATERIAL; the map states (a) its crystalline-phase form, (b) its behavior
at each phase boundary *where derived*, and (c) its NAMED-OPEN holes as first-class
entries. **Honesty requirement (R45): comprehensiveness is the FRAME; the text never
claims content it lacks.** An "unwritten" cell below is a real hole, deliberately
named — not a hedge and not a promise.

| Axiom | (a) Crystalline-phase form | (b) At a derived phase boundary | (c) NAMED-OPEN holes |
|---|---|---|---|
| **1** Substrate Topology | K4 Cosserat crystal, 6-DOF micropolar nodes, intrinsic LC per node — the R7 header text at `:151`, now read as row (a) rather than as a scope fence | the saturation boundary via Ax 4's kernel; the buckling/strut projection at near-yield | **de-bonded** phase topology (unwritten); **genesis** (pre-lattice) (unwritten); **pre-freeze** (unwritten) |
| **2** Topo-Kinematic Isomorphism | $[Q]\equiv[L]$, charge = Burgers-vector dislocation; integers survive coarse-graining | integer protection is topological, so it does NOT lapse at the yield boundary — the one cell where the crystalline law provably carries across | **genesis/formation** of a winding (leans-falsified as a ROUTE, not as existence); $\mathbb{Z}_3$ fractional splitting; the de-bonded phase's dictionary (unwritten) |
| **3** Minimum Reflection Principle | lossless-reactive extremal principle in two co-canonical forms; temporal-gauge (Weyl) written action | Ax3-lossless is what makes the bond-LC L2 invariant exact, so it is load-bearing AT the yield boundary | the variational ⇄ min-$\|\Gamma\|^2$ **equivalence** (ASSERTED, underived — see `:174`); **ruptured-phase** form (unwritten); whether losslessness itself survives past-wall (unwritten) |
| **4** Universal Saturation Kernel | $S(A)=\sqrt{1-(A/A_{yield})^2}$ — the kernel IS the boundary law, so this axiom is the one that spans (a)→(b) by construction | the yield boundary is its own subject; vertical tangent at $A\to A_{yield}$ | the ceiling's **HARDNESS** (yield *exists* = derived; yield is *hard/impulsive* = open); cross-grade combine rule underdetermined at $O(\alpha)$; **past-wall** behavior (unwritten) |
| **5** Substrate DC Bias | clauses **Q** and **G** are the crystalline-phase law. Clause **S** is *genesis-deposited boundary DATA on this phase* — present and conserved, **mechanism-agnostic** | $D(A)$ carries clause G's response into the graded regime; the $D(A)\to\infty$ wall is past-wall-adjacent and **not written** | **★ THE BIAS PROPAGATION THEOREM — this axiom's STANDING DEBT.** Clause G's elliptic law is the **static abstraction of underived finite-speed bias dynamics** (an elliptic solve is instantaneous by construction, and the axiom does not write what replaces it when the source moves). **The $(u,\pi)$ no-signalling theorem does NOT cover the bias read** — it is proven on the $(u,\pi)$ sector and the bias is a declared distinct object, so the bias's finite propagation speed is **owed, not held**. Also: **the genesis-phase law that writes clause S's flux** (the deposit is data, not a derivation); **de-bonded** form of all three clauses (unwritten); **pre-freeze** (unwritten) |

*Ax5's row is R45's own worked example, carried in substance from the ruling: "Q and
G are crystalline-phase law; S is genesis-deposited boundary data on the crystalline
phase, mechanism-agnostic — the mechanism is a named-open entry of the genesis phase."*

### Summary roll-up delta (the table above is NOT rewritten in place)

| Axiom | node | status | residual_content | count-effect |
|---|---|---|---|---|
| **SL** Substrate DC Bias source law (deposit · grade · quiescence) | `axiom-5` **RETIRED (R55, 2026-08-24)** | POSTULATED *(bin: SOURCE-LAW per R55; was RATIFIED-ADDITION)* | whole source law (clauses S + G + Q; one coupling constant 𝒜_g — DERIVE-FIRST, in no register) | counts (0 axioms; 1 source law) |

**LIVE independent-axiom count = 4 + ONE SOURCE LAW (R55, 2026-08-24)** —
ratified-axiom count and framework-node count AGREE again at four
(`expected-independent-axiom-count: 4` in the `axiom-meta` block). Zero axioms at
DERIVED-TO-THEOREM; the Substrate DC Bias carries bin SOURCE-LAW.

### 𝒜_g and the independent-PARAMETER count — RULED, not left to a blind gate

**⚑ SUPERSEDES this section's earlier "𝒜_g enters NO register (R46 derive-first)"
statement.** The derive-first gate has been discharged — the lane reported, the frozen
hypothesis $\mathcal{A}_g = c\,\ell_{node}^2$ is NOT SUPPORTED — and **R48 rules that
𝒜_g DOES enter the register now**, under a new class.

- **𝒜_g's home:** [`interlock-register.md`](interlock-register.md), per-constant
  criteria register, class **`UNVALUED-RATIFIED-CONSTANT`** (minted by R48). Ratified
  as real, **COHERENT across consumers at $f = 7$** under the declared $4\pi$
  convention, and **UNVALUED** — no sound consumer values it.
- **The calibration count STAYS 3, BY RULING.** It moves 3 → 4 exactly when a
  **sound** consumer produces a value. This is the disposition of the standing
  parameter-economy question, and it must be read correctly: the count is unmoved
  **because R48 ruled that an unvalued constant buys no parameter and costs none** —
  **NOT** because the INVARIANT-S13 gate structurally cannot see 𝒜_g. Both facts are
  true and only one is the reason. Mechanically: 𝒜_g mints no `ilk-` node and is
  deliberately absent from `calibration-params:`, and the register's own integration
  note states the count is computed *"ONLY from the `ilk-` `real_or_fitted` tags …
  NOT from this section"*. So a green `verify-kb-metadata` here reports the **ruled**
  state.
- **The one VALUED route is an EXHIBIT of its own inconsistency, not a value.** The
  near-field-store (added-mass) row inverts to
  $\mathcal{A}_g \approx 3.7\times10^{32}$–$1.2\times10^{33}\,\mathrm{m}^2$, but at
  that value the bound-response strain is $\sim2.3\times10^{10}$ at a solar surface —
  **ten orders past yield**, while the row declares itself cold-linear. Self-refuting
  on its own regime declaration. **The row's repair is ROUTED and is deliberately not
  performed here.**
- **𝒜_g is not a falloff.** The $1/r$ bias profile and $1/r^2$ bound response are free
  geometry from the elliptic solve; 𝒜_g is the **scale converter** (metres of
  displacement per unit bias slope). *(R48 walk note of record.)*
- **Non-circularity observation, ROUTED (recorded, not adjudicated):** clause G is
  non-circular only if the bias $\varepsilon_{11}$ is a **distinct object** from
  mechanical strain $\nabla u$; the $\ell_{node}^2$ hypothesis's 57-order miss is
  **evidence FOR that distinctness**. Routed to the residence-lane family.

### R49(a) — the clause-G source convention: repaired here, routed there

**The correction (TYPO-CLASS, dated fragment, NOT a re-ratification).** The ratified
clause-G text writes the elliptic law with a bare `= T₀₀`; the canonical declared
convention carries the $4\pi$ — [`gordon-optical-metric.md`](../vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md):25
(clm-rd9cjm), verbatim: *"-\left(\frac{c^{4}}{7G}\right)\nabla^{2}\epsilon_{11}(r) = 4\pi Mc^{2}\delta^{3}(r)"*.
R49(a) corrects it typo-class **because the ratification never exhibited the
convention question** — there was nothing to re-ratify. No VALUE moves; the $f = 7$
chain is unchanged.

**⚑ SITE COUNT RE-DERIVED AT HEAD, NOT INHERITED — and CORRECTED TWICE.** The
upstream inventory says *"five-plus sites"*. My derivations, in order, with the reason
each moved: **19** (first strict pass — WRONG, false-negatived on the Unicode `∇²`
superscript) → **25** (widened) → **27** (widened again: `.json`/`.jsonl` were outside
the scanned extensions, and the *inside-bracket* variational form
`(−∇·[κD∇ε₁₁] − T₀₀)` never has `= T₀₀` on the right-hand side so the `=`-anchored
pattern could not see it). **27 is the current figure: 3 repaired here + 24 still
carrying the bare source.** Every intermediate number is shown because a count that
moved three times under my own method is exactly the thing not to present as final.

| Class | n | Sites | Disposition |
|---|---|---|---|
| KB / manuscript prose | 3 | `saturating-modulus-and-backreaction.md`:42, :50; `vol3/claim-quality.md`:1254 | **REPAIRED HERE**, each same-line with a dated typo-class note. Also repaired: that leaf's `:43-44` cite, which named `gravitational-refractive-index-gradient.md` — a file carrying **neither** formula — now re-pointed to the gordon leaf + clm-rd9cjm. |
| Verbatim-quoted ratified text | 4 | `axiom-register.md`:350 (inside the quoted clause-G block); `2026-08-10_inventory-review.md`:211, :450, :455 | **NOT rewritten.** Ratified text quoted verbatim is never edited; the dated fragment in [`eq_axiom_5.tex`](../../common_equations/eq_axiom_5.tex) carries the correction for all four. |
| Dated / FROZEN research | 12 | `2026-06-29_grqed-stage1-gr-extension_result.md`:14, :16, :38, :39, :73, :164; `2026-08-10_bound-constitutive_result.md`:37, :120, **:173**; `…_prereg-FROZEN.md`:16; `2026-08-07_a1-port-sourcing_result.md`:123; `2026-08-09_bound-response_result.md`:61 | **SURFACE-NOTE CLASS, not repaired.** ★ **`:173` is the substantive one and was missed by my first two passes**: it is not a prose restatement but the corrected energy functional's **Euler–Lagrange pair**, `D(ε₁₁)·(−∇·[κD∇ε₁₁] − T₀₀) = 0`. Under the declared 4π convention the variational source must carry the 4π too, or the *"R9 machine-verified"* stationarity statement no longer matches the canon law. **A convention-dependent DERIVATION, not a label** — flagged as such and routed, since the doc is frozen. |
| Driver artifact | 1 | `research/drivers/bound_response_consumer_audit.json`:3120 | **SURFACE-NOTE CLASS, not repaired** — a frozen classifier artifact whose `rationale` string restates clause G with a bare `T₀₀`. Missed by my earlier passes because `.json` was outside the scanned extensions. |
| Engine `src/ave/` | 7 | `gw_propagation.py`:364, :368, :412, :456, :482, :599; `backreaction.py`:12 | **ROUTED, out of the doc lane's fence.** The upstream inventory named three of these; there are seven. |

**Also routed, unrepaired (from the same upstream inventory, re-verified as real):** the
engine units-bridge gap (`backreaction.py` runs dimensionless-lattice and carries no
$4\pi$ in its source normalization — nothing bridges its lattice `T₀₀` to the canon
$4\pi$-carrying SI source), and the $\kappa$ dimensional-label question ($c^4/7G$
carries FORCE units as the equation requires, yet is labelled `[Pa]` in code).

### Routed follow-on — the parsimony-class count sites (flag-don't-fix, NOT repaired here)

Two deltas landed today (a fifth axiom; a new coupling constant 𝒜_g whose status is
open). The **naming** class of "four axioms" sites is NOT stale — "the four founding
axioms" remains correct, and `eq_axiom_5.tex` says so explicitly — but the
**derivation-base / parsimony** class understates the base and is routed:

| Site | What is stale |
|---|---|
| `README.md`:41, :51, :74 | "47 predictions … from exactly **4 axioms**"; "3 dimensionful constants `{m_e, α, G}` plus the 4 axioms" |
| `LIVING_REFERENCE.md`:13 | "1 cosmological IC (Ω_freeze) + 1 scale (ℓ_node) + 4 axioms" |
| `manuscript/backmatter/02_full_derivation_chain.tex`:1053, :1057, :1137 | "+ four axioms"; "reduces 26 SM parameters to a 3-element bounding set + four axioms" |

Excluded on purpose (per `eq_axiom_5.tex`: *"It is NOT one of the four founding
axioms and does not renumber them"*): every site that NAMES the founding set —
`README.md`:63 "The 4 Axioms", `LIVING_REFERENCE.md`:447 "Never modify the 4 axioms",
`01_fundamental_axioms.tex`:2's chapter title, and the "Vol 1 Ch 1 (Four Fundamental
Axioms)" cross-refs. Those are names, not counts, and are correct as written.
