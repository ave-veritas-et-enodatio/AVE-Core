# PREREG — θ route 1: the n-component Brunnian embedding obstruction in the z=3 srs carrier

> **Class:** research-tier pre-registration. **No canon edit.** Nothing is minted; no `clm-`/`def-`/
> `exp-`/`sup-`/`ilk-` node is authored; no solidity moves. This document freezes the question, the
> outcome bins and the adjudication criteria BEFORE the first-order pass, per `ave-prereg`.
>
> **Frozen:** 2026-08-23, before any enumeration. The companion result doc is
> [`2026-08-23_theta-route1-embedding-obstruction_result.md`](2026-08-23_theta-route1-embedding-obstruction_result.md).

---

## §0 — SECTOR DECLARATION (mandatory header, stated before any standard-physics word)

| Axis | Declaration |
|---|---|
| **MODE** | **Axiom-1 carrier geometry** — the static graph + metric structure of the ratified chiral z=3 srs net — conjoined with the **real-space body topology** of flux-tube loops. This is NOT a V-sector (K4-TLM scatter/connect) dynamics question, NOT a Cosserat (u, ω) LC-tank eigenproblem, and NOT an energy-minimisation problem. |
| **REGIME** | **Split, and the split is declared as a scope caveat.** The *carrier* is characterised **cold / Regime I** (unsaturated, lossless-reactive, no drive). The *object* the question asks about — the proton's Borromean core — is canonically **Regime IV / Ax4-saturated** (`proton-identification.md`:24, property 4: *"the cinquefoil core operates in the saturated regime ($S \to 0$, $G_{shear} = 0$)"*). Whether the cold net's port geometry survives into the saturated core is **not established by this lane** and is carried as a declared scope caveat, not assumed away. |
| **PHASE-STATE** | **Crystalline** (cold, sub-yield) for the carrier — Axiom 1's phase-map row (a) per R45. The baryon core sits at/beyond the saturation boundary; per the R45 COMPREHENSIVE-MAP doctrine that is a **named-open hole**, not a silence. |
| **CHANNEL** | **REAL-SPACE** body topology. Per `manuscript/ave-kb/CLAUDE.md` INVARIANT-N1: *"the electron's **real-space body** is the $0_1$ **unknot**; the proton's is the $6^3_2$ **Borromean** linkage. Rolfsen names … refer to **phase-space winding portraits** on the bond-pair LC tank (Clifford torus), **not** real-space body knots."* The $(2,5)$ cinquefoil is therefore **out of channel** for this question and is never used as evidence in it. |

**Why the channel declaration is load-bearing (A46 / `phase-space-coordinate-check`).** The corpus
claim under test — "three mutually entangled flux loops" forming a $6^3_2$ Borromean linkage — is
declared by INVARIANT-N1 to be a **real-space** claim. A Brunnian-embedding test is therefore
correctly posed in real-space lattice coordinates, and the usual A46 hazard runs the other way here:
the risk is importing the *phase-space* $(2,5)$ winding as though it constrained the real-space
embedding. It does not, and this prereg forbids that move.

---

## §1 — SUBSTRATE-NATIVE WALK (`substrate-native-check`, trigger 6 — prose-derivation construction)

Fired before any code or argument. Ten checkpoints, walked in order.

| CP | Checkpoint | Walk result for this lane |
|---|---|---|
| 1 | What is the substrate's dynamics for this problem? | **Neither wave-propagation nor minimisation — the question is not dynamical.** It asks whether a *link type* is realisable by disjoint closed curves subject to a lattice constraint. That is a topology/combinatorics question about the carrier, answered by graph structure + link invariants. **The SM/continuum default this closes: "n=4 is energetically disfavoured."** An energy answer is NOT an embedding obstruction and does not satisfy the frozen route. |
| 2 | Which sector? | Carrier geometry (Axiom 1). Not V-sector, not Cos-sector, not Op14 cross-coupled. |
| 3 | AVE-native objective? | A **topological realisability count**, not an energy functional, not an $S_{11}$ minimum, not a Hessian spectrum. Stated so that the answer form is constrained in advance. |
| 4 | Phase-space vs real-space | **Real-space** — see §0 CHANNEL. Locked. |
| 5 | Saturation-modulated local clock | **N/A to the characterisation** (no eigensolve, no drive, no Op14). Carried instead as the REGIME scope caveat in §0. |
| 6 | Reactance pair (C-state AND L-state) | **N/A** — no time-domain run in this lane. |
| 7 | Sampling discipline (PML exclusion, density-peak vs centroid) | **N/A** — no field extraction. The driver reads graph adjacency + positions only; there is no PML and no `argpartition`. |
| 8 | Generative precursor vs planted end-state | **Named, and it is the reason this lane cannot bank a positive.** A genuine "does the lattice force exactly 3 loops?" test is a **hosting test**: seed the generative precursor and let the dynamics build the cage. This lane instead reasons about a **planted** finished Borromean object. That is the ambiguous-failure mode CP8 warns about, so this lane's verdict space is deliberately restricted to *obstruction-or-not*, and a "n=3 fits" reading can **never** be banked from it. |
| 9 | Heuristic-vs-dynamical observable | The measured quantities (degree, bond angles, girth, bond length, scale ratios) are **computed** from the certified constructor and the canonical constants module. The n=3-vs-n=4 verdict itself would be an **analytic** argument, not an engine-evolved observable ⇒ **WALL-engine**: no engine in the tree evolves a baryon-scale three-loop configuration, so the dynamical form of this question is currently untestable. Stated as a capability finding, not a physics floor. |
| 10 | Boundary condition, not bulk force | **N/A** — nothing is confined or reflected here. Flagged only so the walk is complete. |

**Exit:** all ten checkpoints answered; two (CP8, CP9) return *constraints on what this lane may
conclude*, and those constraints are written into the outcome bins in §4.

---

## §2 — VOCABULARY LEAK-CHECK (every borrowed word, before it is used)

| Word | Origin | Corpus status | Ruling for this doc |
|---|---|---|---|
| **Brunnian** | knot theory | **ZERO corpus hits.** Searched `manuscript/`, `research/`, `src/`, `_orchestration/` with `grep -rn "Brunnian"` — no matches. | **Imported term, tagged as such.** The *property* IS corpus-present, in prose: `vol_2_subatomic/chapters/02_baryon_sector.tex`:31 — *"three LC standing waves interlinked such that no two individual loops are linked directly, but the three together form an inseparable resonant triad."* That sentence IS the Brunnian condition. Used here only as shorthand for that quoted property. |
| **Milnor (invariant)** | knot theory | **ZERO corpus hits** (same search). | Imported; used only where the frozen route text uses it, tagged. |
| **Borromean**, **$6^3_2$** | corpus-native | Canonical (`proton-identification.md`:22, INVARIANT-N1). | Native. Use freely. |
| **port** | corpus-native (EE) | **CONTESTED COUNT — see §3.3.** The canonical port-irrep leaf is a **4-port** node; the ratified carrier is **z=3**. | Used only with an explicit port-count qualifier at every occurrence. |
| **flux loop / flux tube** | corpus-native | Canonical (`electron-unknot.md`:11, Axiom-1 $d \equiv 1\,\ell_{node}$). | Native. |
| **lattice cycle** | graph theory | Not a corpus term. | Imported; defined in §3.1 as *a closed walk in the srs bond graph*. |
| **over-subscription** | the frozen route's own wording | Not a corpus term. | Defined operationally in §4.2 rather than left to intuition. |
| **energetically disfavoured** | continuum/SM default | — | **BARRED as a verdict** by CP3. May appear only as a named non-answer. |

---

## §3 — THE FORMALIZATION FORK, STATED PRECISELY (resolved BEFORE bins are exercised)

The frozen route requires the fork be resolved first. This section states the two candidate
formalizations in a way that makes each **falsifiable against the corpus**, and states what evidence
would settle each. The verdict itself is in the result doc; only the *criteria* are frozen here.

### §3.1 — Formalization C (extended lattice cycle)

*A baryon flux loop is a closed walk in the srs bond graph — the tube runs from node to node along
bonds.* Consequences that must hold if C is right:

- The loop's real-space perimeter is an integer multiple of the bond length $\ell_{node}$, bounded
  below by the net's **girth**.
- The proton body therefore has a hard minimum real-space size set by the girth, and cannot be
  smaller.
- Three loops meeting at one node engage that node's ports in a way that is arithmetically
  constrained by the coordination number.

### §3.2 — Formalization N (sub-cell tube anchored at a node's bond directions)

*A baryon flux loop is a sub-bond object anchored at one node, associated with one of that node's
incident bond directions.* Consequences that must hold if N is right:

- The loop's real-space size is **less than** one bond length.
- A loop must be able to *distinguish* the three bond directions at the node it is anchored to —
  i.e. the object's spatial extent must be comparable to the bond length, or the node must possess
  sub-bond internal structure that carries the 3-fold port information.
- The one-per-port assignment must be a **derived** rule, not a stipulation, or the resulting
  "n ≤ 3" is the numeral rhyme the docket bars.

### §3.3 — The port-count precondition (checked before either branch is exercised)

Both formalizations presuppose that "the node's ports" is a single well-defined object. This prereg
records in advance that the corpus carries **two** port counts, and that the result doc must
reconcile or flag them rather than silently pick one:

- **z = 3** — `axiom-register.md`:147, the D1 ratification: *"the chiral z=3 srs net is the
  production carrier"*.
- **4-port** — `k4-port-irrep-decomposition.md`:11 (clm-j550uh): *"The K4 4-port amplitude space
  decomposes under the tetrahedral group $T_d$ as $V_{\text{4-port}} = A_1 \oplus T_2$"*, described
  in that same leaf as *"**the canonical group-theoretic foundation**"*.

**Frozen instruction:** if the two counts cannot be reconciled by scope, the lane **flags, does not
fix** (Grant's standing directive), and the flag is a first-class result, not a footnote.

---

## §4 — THE FROZEN QUESTION, THE BINS, AND WHAT COUNTS AS OVER-SUBSCRIPTION

### §4.1 — The question (frozen wording, from open-item `theta-dressing-open-questions`, route 1)

> *"In the ratified z=3 srs carrier: can n mutually-Brunnian flux structures meet a node at
> one-per-port, and does n=4 force over-subscription while n=3 fits?"*

**Kill condition (verbatim from the same open item, quoted not paraphrased):**

> *"Kill condition: if n=4 embeds as cleanly as n=3 under the corpus-supported formalization,
> routes 2-3 lose their lattice anchor and the thirds stay honestly imported."*

**Standing weld hazard (verbatim from docket `2026-08-23-theta-fork-ruling` and the open item):**

> *"'N=3 because z=3' counts only as a derived embedding obstruction, never as the numeral rhyme"*

### §4.2 — What counts as OVER-SUBSCRIPTION (defined in advance)

`n` structures **over-subscribe** a node iff, under the corpus-supported formalization, the
one-per-port assignment for `n` structures is **not injective** — i.e. two distinct structures are
forced onto the same port, or one structure is forced to occupy zero ports — **and** no relabelling
of the assignment removes the collision. Over-subscription is a statement about the *assignment map*,
not about energy, not about crowding, and not about numerical convergence.

### §4.3 — Outcome bins (frozen; exactly one is the primary verdict)

| Bin | Fires when | Consequence |
|---|---|---|
| **B1 — n=3-FORCED** | Under the corpus-supported formalization, `n=3` admits an injective one-per-port assignment carrying a Brunnian link, `n=4` provably does not, AND the one-per-port rule is itself derived rather than stipulated. | Routes 2–3 keep their lattice anchor; the `3` gains a derived embedding obstruction. **Cannot be reached from a planted end-state alone** (CP8) — a B1 reading must be flagged as obstruction-only and routed to a hosting test. |
| **B2 — n=4-EQUALLY-CLEAN (KILL)** | `n=4` embeds as cleanly as `n=3` under the corpus-supported formalization. | The verbatim kill fires: *"routes 2-3 lose their lattice anchor and the thirds stay honestly imported."* |
| **B3 — FORMALIZATION-UNDETERMINED** | The corpus does not determine whether C or N holds — including the case where both are canonically asserted and the conflict is already flagged unresolved. | **STOP-AND-ASK.** State both branches' consequences; do not pick. This is a walk-candidate for Grant, not a lane decision. |
| **B4 — QUESTION-ILL-POSED-AS-FROZEN** | The frozen question contains a defect that makes it unanswerable as written (a premise with no referent under either formalization, or an arithmetic inconsistency in the premise). | **STOP-AND-ASK with the specific defect named.** Do not repair the question unilaterally — a repaired question is a new question and needs its own freeze. |

**Multi-bin discipline (frozen).** If more than one bin's condition is met, the **primary verdict** is
the earliest of B4 → B3 → B2 → B1 in that precedence order (a defect in the question dominates an
undetermined formalization, which dominates any conditional physics reading). Any further bins are
reported as **CONDITIONAL** readings, explicitly not banked.

### §4.4 — Adjudication criteria that may NOT be dropped post-hoc

1. A "derived embedding obstruction" requires the one-per-port rule to be **derived from canon**, not
   assumed. Absent that derivation, `n ≤ z = 3` is the numeral rhyme and does **not** satisfy B1.
2. A B1 verdict additionally requires demonstrating that the `n=3` assignment actually carries a
   **Brunnian** link (pairwise-unlinked, collectively non-splittable), not merely that three
   structures fit.
3. "Energetically disfavoured" never satisfies B1 or B2 (CP3).
4. Any numeric compared against a corpus statement must be **computed** from
   `ave.core.constants` / the certified constructor, never restated from prose.

---

## §5 — CONSISTENCY-VS-EMERGENCE CLASSIFICATION (frozen in advance)

`consistency-vs-emergence` fired at design time. Pre-classification of each bin:

- **B1** would be an **EMERGENCE-class** result *about the value 3* — the lattice would be forcing a
  number the corpus currently feeds in (`topological-fractionalization.md`:59: *"The denominator
  VALUE $3$ is FED IN … There is NO 3-loop stability theorem."*). Because it is emergence-class, it
  carries the highest evidentiary bar, which is why §4.4 criteria 1–2 are non-negotiable.
- **B2** is a clean **NEGATIVE** and requires no class tag beyond the kill.
- **B3 / B4** are **PROCESS** verdicts about the corpus state, not physics claims, and are classed
  accordingly — they mint nothing.
- The characterisation numbers in the driver are **IDENTITY / MANIFESTATION** class: `L_NODE`,
  `PROTON_ELECTRON_RATIO`, `D_PROTON` are canonical-module reads; degree / angle / girth are
  measurements of the certified constructor. **No CODATA is re-entered on any verdict path**
  (`PROTON_ELECTRON_RATIO` is the AVE-derived `_X_CORE + 1.0` at `constants.py`:987, not
  `M_PROTON`).

---

## §6 — METHOD

1. **Corpus pass (verify-before-cite on every quote).** Read, in full: `electron-unknot.md`,
   `proton-identification.md`, `topological-fractionalization.md`, `neutron-identification.md`,
   `srs-band-structure.md`, `axiom-register.md` (Axiom 1), `k4-port-irrep-decomposition.md`, and
   `vol_2_subatomic/chapters/02_baryon_sector.tex` §Borromean-Confinement. Quote the deciding texts
   verbatim with file:line.
2. **Carrier characterisation (read-only).**
   [`drivers/theta_route1_srs_scale_ladder.py`](drivers/theta_route1_srs_scale_ladder.py) —
   degree census, pairwise bond-angle set, bond-star closure (coplanarity), girth, and the
   nearest-neighbour bond length in pitch units, on `ave.core.chiral_lattice.build_srs_net`, **both
   enantiomorphs**; plus the scale ladder in $\ell_{node}$ units from `ave.core.constants`.
3. **Fork resolution.** Adjudicate C vs N against the quoted texts. If both are canonically asserted
   and the conflict is already flagged, that is B3 and the lane stops.
4. **First-order pass.** Under whichever branches survive, state the combinatorial/geometric
   argument. Enumerate only if the fork resolved to a single formalization — per truth-per-token,
   an enumeration under a void reading is waste.
5. **Bin, and report the stuck-point.** 2-attempt cap; STUCK-POINT report on stop-and-ask.

**Pre-registered null-liveness check (`pre-test-physics-check` trigger 10).** The decision observable
here can return "no obstruction", so: the positive control is **the girth measurement itself** — a
quantity that is *known* to be non-trivial (10, not 3 or 4) and that would immediately expose a
constructor or graph-traversal bug; and the structural-degeneracy check is that the bond-angle and
bond-star measurements are run on **both enantiomorphs** independently, so a symmetry-forced artifact
would show as an implausible exact agreement on a quantity that has no reason to agree. (It does
agree, exactly, on degree/angle/girth — which is the *expected* enantiomorph invariance, and is
recorded as such rather than read as a signal.)

---

## §7 — WHAT THIS PREREG DOES NOT DO

- It does not resolve the `strong-cp.md` ↔ `topological-fractionalization.md` θ-symbol collision
  (docket `2026-08-23-theta-fork-ruling` executed that separately; the docket + open item live on
  branch `kb/2026-08-23-theta-carve` / PR #998 and are **not on `main`** at this branch's base).
- It does not touch the CP-parity debt (route 4).
- It does not define `Wind(∂Ω)` (the definitional gap the open item names as prerequisite-adjacent).
- It does not edit, demote, or repair any canonical leaf. Every corpus tension it finds is
  **flagged with both sides quoted**, per flag-don't-fix.
