[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Canonical AXIOM register — a status / provenance / residual-content VIEW over the FOUR existing `axiom-N` framework nodes (node_type: \"axiom\", ids axiom-1..axiom-4), which are ALREADY materialized into claims.jsonl by refresh-kb-metadata from the `- Axiom N: **…**` bullets in CLAUDE.md INVARIANT-S2 (the KB's axiom-numbering authority). This leaf originates NO new node-body via frontmatter and mints NO new axiom id: axioms are terminal UNSCORED framework nodes (SCHEMA.md 'Framework record' — 5 fields, no confidence/solidity/quality, emit no edges), so a register that re-declared them would be a parallel scheme, forbidden by INVARIANT-S11 (extend, don't reinvent). It is the axiom analog of the interlock-register's per-CONSTANT Calibration-Constant Criteria Register: a bolded-field VIEW that POINTS AT the existing framework nodes (via the `axiom-N` id) and, where an axiom's content is partly derived, at the theorem `clm-`/result that carries the proof — NOT a source of new claims. Hence no-claim."
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
  axiom is no longer independent). **No axiom is at this status.**

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
- **finding — Axiom 1 has NO dedicated axiom-content `clm-` node (only the framework `axiom-1` node).** The brief asked to reconcile Axiom 1's supposed `clm-3kzmt9`. **`clm-3kzmt9` is NOT an Axiom-1 node.** Verified: its canonical entry is at [`vol1/claim-quality.md:187`](../vol1/claim-quality.md) titled around the **ξ vs ξ_topo homonym distinction** (its body: "$\xi \approx 8.15\times10^{43}$ … vs $\xi_{topo} = e/\ell_{node}$ … different quantities sharing a Greek letter"; specific claim = the $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ cosmological-horizon dilution) plus the α-is-Class-B relabel — confidence 0.90, solidity 0.63, depends-on clm-0ktpcn + clm-5xon03. In [`axiom-definitions.md:33`](../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) its Tier-2 marker `<!-- claim-quality: clm-3kzmt9 -->` sits on the **notation-warning block UNDER Axiom 2**, not on Axiom 1. So it was never Axiom 1's node. Axiom 1's ONLY first-class node is the terminal framework node `axiom-1`; there is no scored `clm-` that states Axiom 1's content (nor should there be — an axiom is UNSCORED bedrock, so a scored Axiom-1 `clm-` would be a category error, per the node-type discipline). This register's `axiom-1` view IS the intended first-class status home; no `clm-` wiring is needed or correct.

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
- **status:** **POSTULATED.** No derivation of the extremal principle from weaker structure exists. (The variational ⇄ boundary EQUIVALENCE is a proven internal theorem, but it relates two co-canonical FORMS of the one postulated axiom — it does not derive the axiom itself.)
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
which the Axiom-4 full-reduction epic would test but has not established.

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
| **1** | the substrate: K4 Cosserat crystal lattice + per-node 6-DOF (3 transl→$\varepsilon_0$, 3 microrot→$\mu_0$) | the lattice *responds* — impedance, screw kinematics, buckling | **three-impedance law** ($Z_{EM}/Z_{shear}/Z_{bulk}$, graded-network); the **$4_1$ screw operator** (chiral holonomy); the **buckling-kernel SHAPE chain** (fixed-arc-length strut projection → Axiom-4 √ form, PRs #459/#460) | the **D1 $z{=}3$-vs-$z{=}4$ production identity** (unified-srs arc tension — bare srs instrument $z{=}3$ vs diamond production engine $z{=}4$); the **continuum-limit legs** (rigorous lattice→continuum) |
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
