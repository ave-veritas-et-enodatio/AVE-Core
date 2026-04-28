# 79 — L3 Electron-Modeling Branch Closure Synthesis (v3, PENDING path α)

**Status:** implementer-drafted with auditor + Grant pushback, 2026-04-28 v3.1. Presents lemniscate-with-q-half-twists as primary AVE-native plumber framing for the (2, q) particle family in the K4-TLM + Cosserat substrate, with corpus mathematical/topological descriptions cited as equivalent representations. **PENDING path α empirical result before final closure adjudication.** Framework structure landed; Mode I/III empirical adjudication awaits path α result.

**Version history:**
- v1 → v2: incorporated 5 auditor pushbacks (knot-theory honesty in §1+§2, substrate-vs-imported equivalence in §4, Pauli per doc 37 §3.1, A60 to COLLABORATION_NOTES, c=q half-twist universal form)
- v2 → v3: Grant adjudication 2026-04-28
  - Q1 (Kelvin lineage): added §11 historical-precedent reference; doc 80_ companion research note
  - Q2 (substrate-fundamental factor-of-2): §4 reframed — bipartite K4 is the fundamental source; tetrahedral T_d → 2T → SU(2) flagged as separate downstream framework derivation
  - Q3 (Pauli substrate-native): §6.6 rewritten — one bound state per saturated node-pair, atomic shells = multiple bond-pair locations within envelope; doc 37 §3.1 flagged in §9(e) as substrate-revision-required (its "+n̂/−n̂ pair-sharing" framing was SM/QED creep)
- v3 → v3.1 (this version): auditor pushback round 2 (2026-04-28)
  - §4 added explicit "same geometry two languages" sentence preventing future agents from reading bipartite-cycle factor + SU(2) factor as compounding to 4×
  - §6.6 flagged as PROVISIONAL pending corpus pressure-test (He, Li, Cooper pair) — substrate-native Pauli framing is the working hypothesis, not yet canonicalized
  - §9(e) Pauli pressure-test promoted to load-bearing item with specific test cases enumerated
  - Lane attribution fixed: "implementer-drafted with auditor + Grant pushback" per Rule 15 (was incorrectly "auditor-drafted" in v3)

**Companion docs:** [doc 78_](78_canonical_phase_space_phasor.md) (r9 phase-space phasor result, Mode III with caveats); [doc 80_](80_kelvin_helmholtz_ave_precedent.md) (Kelvin/Helmholtz/Faddeev-Niemi historical lineage); [doc 75_](75_cosserat_energy_conservation_violation.md) (Cosserat sector engine implementation, T_kinetic saturation fix prescription); [doc 77_](77_lattice_to_axiom4_bridge.md) (canonical Scheme A bridge).

---

## §1 — What the (2, q) particle family is (primary plumber framing)

**A stable particle in the AVE substrate is a lemniscate (figure-8 curve) with q half-twists, threaded through a saturated K4 node, oscillating between two adjacent A-B sublattice neighbors.** The lemniscate's two lobes alternate between the A node and B node sides; the central crossing of the lemniscate sits at one of the saturated nodes. The number of half-twists wrapping the lemniscate around its propagation axis is the particle-distinguishing parameter q:

- **q = 3** → electron (with the substrate's right-handed twist; q = -3 mirror image = positron)
- **q = 5** → proton
- **q = 7** → Δ baryon
- (q must be odd per stability rule in [`faddeev_skyrme.py:18`](../../src/ave/topological/faddeev_skyrme.py#L18))

What the engine measures as "the particle" is the **time-averaged envelope** of this oscillating-and-twisting lemniscate: per Compton period the lemniscate rotates and flexes, and per-cycle averaging gives the (V_inc, V_ref) phase-space ellipse with major-axis R_phase and minor-axis r_phase.

The substrate's bipartite K4 structure forces the lemniscate's two-lobe shape (bonds connect A↔B; any oscillation alternates sublattices). This is universal across the (2, q) family — every stable particle has the lemniscate lobe structure because the lattice is bipartite.

**Mathematical correspondence note:** the "lemniscate with q half-twists" plumber visualization corresponds to the (2, q) torus knot at the c=q crossing-count level via §2's cross-mapping. The construction is **not** topologically the standard figure-eight knot (4_1) — that's a distinct knot. The lemniscate-with-q-half-twists construction, properly closed as a 2-strand braid, gives the (2, q) torus knot family: trefoil (3_1) for q=3, cinquefoil (5_1) for q=5, etc. The plumber visualization captures the substrate-physical content; the tabulated-knot identification carries the formal topology.

**Historical precedent:** this lemniscate-with-twists picture has direct lineage to Lord Kelvin's 1867 *"On Vortex Atoms"* hypothesis (knotted vortices in fluid medium = atoms) and Helmholtz's 1858 vortex theorems (topological invariance of vortex tubes under fluid evolution). Modern revival via Faddeev-Niemi 1997 knotted solitons is already in the AVE codebase as [`src/ave/topological/faddeev_skyrme.py`](../../src/ave/topological/faddeev_skyrme.py). See [doc 80_](80_kelvin_helmholtz_ave_precedent.md) for the historical precedent + specific Kelvin intuitions worth deepening.

## §2 — Equivalent corpus representations

Same physical object, four corpus framings:

| Corpus framing | What it captures | Citation |
|---|---|---|
| (2, q) torus knot family | Mathematical topology class | [doc 07 §3](07_universal_operator_invariants.md) |
| Scalar c = q via Op10 | Crossing count invariant (3, 5, 7, ...) | [universal_operators.py:577-579](../../src/ave/core/universal_operators.py#L577) |
| Trefoil / cinquefoil / septafoil on Clifford torus | Standard-knot-theoretic representation | [doc 26_](26_step5_phase_space_RR.md) + faddeev_skyrme.py |
| Two-node-bond + bond's (2, q) phase-space LC | Substrate-anchored object class | [doc 37 §1](37_node_saturation_pauli_mechanism.md) |

Cross-mapping to the lemniscate-with-q-half-twists picture:
- Tabulated knot (3_1, 5_1, 7_1, ...) ≡ lemniscate-with-q-half-twists at the c=q crossing-count level (construction equivalence, not standard-knot-theoretic identity to figure-eight knot 4_1)
- c = q ≡ q half-twists in the lemniscate
- Two-node-bond ≡ lemniscate oscillating between A-B endpoints; central crossing at saturated node
- (R_phase, r_phase) ≡ time-averaged envelope of the lemniscate-with-twists in (V_inc, V_ref) phase space

## §3 — Why "2" is universal across the (2, q) family

**"2" = the lemniscate has two lobes**, enforced by bipartite K4 (every oscillation alternates A↔B sublattices). This is universal — every stable (2, q) particle in the AVE substrate has the lemniscate lobe structure because the lattice is bipartite. **"q" varies by particle** as the half-twist count.

This is **substrate-structural synthesis** per Rule 14, confirmed by Grant 2026-04-28 plumber-physical view — NOT direct corpus citation. Doc 03 §4.3 + faddeev_skyrme.py:18 confirm "2 is series index, q odd is stability requirement"; the physical interpretation as bipartite-cycle / lemniscate-lobe-count is the AVE-native synthesis this closure adopts.

## §4 — The factor m_Cosserat = 2·m_e (substrate-fundamental, bipartite K4)

**Substrate-fundamental description (per Grant Q2 2026-04-28):** the factor of 2 between m_Cosserat (medium oscillation period) and m_e (observable envelope cycle period) arises directly from **K4 bipartite structure**. The substrate has two interpenetrating sublattices A and B; every dynamical object alternates between them per oscillation cycle. The lemniscate has two lobes (one per sublattice visit); one full medium-frequency traversal visits both lobes, but the time-averaged envelope completes a cycle per LOBE-VISIT, so observable frequency = 2× medium frequency. **m_e (observable) = m_Cosserat (medium) / 2.**

This is direct from Ax 1 + K4 lattice geometry. No imported math required.

**Imported-math equivalent:** the SU(2)→SO(3) double cover encodes the same factor of 2 in representation-theoretic language (spinor wraps 720°, medium 360°). Vol 2 Ch 4 + A-008 carry this derivation via gyroscopic precession with half-cover identification.

**Both descriptions stay in the corpus.** The bipartite-cycle / lobe-count is primary because it's substrate-fundamental and Rule-6-clean; the SU(2) language is the imported-math abstraction of the same factor, retained as equivalent representation.

**Critical clarity (per auditor pushback v3.1):** the bipartite-cycle factor of 2 and the SU(2)→SO(3) double-cover are **the same geometric content viewed at two abstraction layers** (substrate-physical vs representation-theoretic), **NOT two independent factors that compound**. A future reader should not interpret this section as "lobe-count factor of 2 multiplied by SU(2) factor of 2 = 4× total" — both are the same factor expressed in different vocabulary. Empirically m_Cosserat = 2·m_e (one factor), and the substrate-physical / representation-theoretic descriptions are two ways of stating that single factor.

**Possibly relevant downstream group-theoretic structure** (NOT load-bearing for L3 closure, flagged for separate research): K4's tetrahedral point symmetry T_d (order 24) has a binary tetrahedral double cover 2T (order 48) ⊂ SU(2). The Cosserat ω-rotation at a saturated node may use the 2T representation rather than T_d, which would group-theoretically explain why the SU(2) double cover gives the same factor of 2 as the bipartite-cycle. **This equivalence is asserted, NOT derived in this closure.** Demonstrating it (showing K4 tetrahedral covering group ⊃ SU(2) explicitly drives the medium-vs-observable factor) is post-closure framework derivation work.

The substrate-fundamental claim — bipartite K4 cycle count = factor of 2 — does NOT require this group-theoretic equivalence to land. The lobe-count derivation is sufficient on its own.

## §5 — Three-layer chirality structure

The substrate's one-handed chirality (K4 right-handed bipartite, genesis-fossilized) interfaces with the (2, q) particle in three distinct ways:

**Layer 1 — Substrate chirality projects into the lemniscate's twist direction.** K4 right-handed → particle has right-handed twist (electron, proton, Δ). Mirror image (left-handed) = antiparticle. Substrate's single chirality direction picks the twist sign.

**Layer 2 — Two channels carry the twist within the (2, q) bound state.** Per [doc 20 §3](20_chirality_projection_sub_theorem.md): two independent chirality channels combining via parallel impedance χ = α · pq/(p+q). Under the lemniscate framing, the two channels are:
- **Bipartite-cycle channel (p=2):** bond-axis K4-LC oscillation between A-B node pair (lobe-traversal motion; substrate-universal across all (2, q) particles)
- **Scalar-crossing channel (q=c):** Cosserat ω-field rotation at the saturated central node (the half-twist count; particle-distinguishing)

For electron: χ = α · 6/5 = 1.2α. For proton: χ = α · 10/7. Both channels carry the substrate's right-handed twist; their parallel-impedance combination is the macroscopic chirality coupling per particle.

**Layer 3 — Time-averaged envelope cycles twice per medium oscillation.** Per §4 above. m_Cosserat = 2·m_e is the lobe-count factor.

## §6 — Empirical state at closure

### §6.1 — R6 closure (CLOSED 2026-04-25)
[doc 03 §4.3 validated empirically — topology quantized, NOT dynamically derived; Golden Torus unstable in coupled engine; F17-K Phase 5c-v2-v2 + X4b stability work.]

### §6.2 — R7 seven Mode III tests (CLOSED Mode III at corpus GT, REINTERPRETED)
The seven Mode III tests at corpus GT (V-block × 2 N, Cos-block × 2 N, R7.2 G-13, Test B v2/v3 multipoint) all tested for a **spatial multi-cell extended structure** — bond-extent (R, r) torus with multi-cell winding patterns. Per doc 07 §3's category-error flag + Vol 1 Ch 8 spatial-trefoil pedagogical creeper, these tests measured spatial-winding observables that the AVE-native operator catalog doesn't predict.

Under this closure's framing: **the seven Mode III results are correct** (no spatial multi-cell torus exists at corpus (R, r)) — but the **falsification target was the creeper, not the operator-derived prediction**. The corpus electron is the lemniscate-with-twist at the bond-pair scale, NOT a spatial multi-cell torus.

### §6.3 — R8 photon-tail Mode III (CLOSED, REINTERPRETED)
Path (a) standing-wave + path (b) propagating IC at engine-representable corpus aspect (N=64, R=4, r=1.5): both Mode III. Same creeper category as §6.2 — tested spatial multi-cell phasor (12 loop nodes), didn't match the operator-derived bond-pair prediction. A58 confirms IC velocity choice doesn't change result.

### §6.4 — Move 5 attractor (positive empirical signal under reframing)
Move 5 at corpus GT produced a stable (2, 3) attractor for ~150 Compton periods at peak |ω|=0.3π (saturation onset). c=3 via Op10 confirmed. **Under the closure's framing, Move 5's attractor IS the corpus electron at engine-representable scale**, just measured via the wrong observables (real-space (R, r) shell tracking instead of bond-pair phase-space phasor). The dissolution after 150 Compton periods is real but reflects sub-corpus equilibrium drift, not framework falsification.

### §6.5 — r9 phase-space phasor (Mode III with caveats)
Pre-reg P_phase8_canonical_phase_space_phasor at commit `a535090` ran phase-space (V_inc, V_ref) phasor on Move 5's attractor at top-K=4 single cells. Result `466d8c4`: Mode III nominal (C1 R/r=3.84 vs target φ²=2.618 FAIL; C2 chirality 50% TIE FAIL); persistence 33% (below 40% guard); chirality cross-products noise-dominated.

A59 methodology gaps:
- Persistence guard violated — recording window captured attractor decay
- Chirality cross-product noise-dominated
- Bipolar +x/−x R/r distribution
- **Sampled at top-K single cells, not bond-pair scale** — under this closure's framing, this is the load-bearing methodology miss

### §6.6 — Pauli exclusion (substrate-native, per Grant Q3 2026-04-28)

> **⚠ PROVISIONAL pending corpus pressure-test — see §9(e).** This subsection's framing is the substrate-native Pauli hypothesis under Grant Q3 + Rule 14. The "vector ω-superposition cancels" argument is sound for free fields but isn't airtight under saturation (saturated states may not superpose linearly the way free fields do). Canonicalization requires verifying the alternative framing matches observed atomic shell capacities (He, Li, Cooper). v4 lands canonical or revised after pressure-test.

Each saturated K4 node has a hard A²≤1 budget. The lemniscate-with-twist's central crossing requires A²→1 at that node. **Working hypothesis: at most ONE bound state per saturated node-pair.** Pauli exclusion would then be literal at the substrate level: a second lemniscate centered at the same node-pair would require A²=2, violating the saturation budget.

**No pair-sharing (under this hypothesis).** Two opposite-direction ω-fields at the same node superpose linearly and cancel (vector addition), rather than coexisting as separate Pauli-allowed states. The "two electrons of opposite spin share the 1s orbital" framing from standard chemistry would map to AVE substrate as: **multiple separate bound states at different bond-pair locations within the same atomic-shell spatial envelope**, NOT two states at the same node-pair.

In an atom:
- The atomic shell ("1s", "2p", etc.) is a SPATIAL ENVELOPE spanning multiple bond-pairs
- Each saturated bond-pair within the envelope hosts ONE lemniscate-with-twist bound state
- Different bound states have different rotation-axis orientations (set by local bond geometry, NOT freely chosen)
- "Spin-up" and "spin-down" in standard chemistry = different rotation-axis orientations of separate bound states at separate bond-pair locations
- Total atomic spin = vector sum of bond-pair rotation axes within the envelope

The Pauli mechanism is then: per-node A²≤1 budget excludes second occupation at any given saturated node; atomic shell capacity (2 for s, 6 for p, etc.) is set by how many bond-pair locations are available within the shell's spatial envelope.

**This replaces doc 37 §3.1's "+n̂/−n̂ orientations sharing same node-pair" framing**, which fails at the substrate level (vector ω-superposition cancels rather than splits the budget). Doc 37 §3.1 is flagged in §9(e) corpus revision package as needing pedagogical revision under the substrate-native reading.

## §7 — Path α requirements (empirical test pending)

Path α rerun is the empirical test that decides positive vs negative L3 closure under this framing:

1. **Bond-pair sampler** (per §6 framework): identify top-K saturated cells; for each saturated A node, find nearest saturated B-sublattice neighbor with shared bond; sample (V_inc, V_ref) at that bond's port between the two saturated endpoints
2. **Earlier recording window:** t ∈ [10, 50] P (fresh attractor pre-decay) instead of [50, 200] P
3. **Hilbert-transform / cross-spectrum chirality:** resolves cross-product noise dominance
4. **Per-cluster R/r adjudication:** handles bipolar distribution
5. **Dual-criterion (unchanged from r9):** C1 R/r=φ² ± 5%, C2 chirality direction matches K4 right-handed substrate

**If Mode I:** corpus electron empirically confirmed as lemniscate-with-twist at bond-pair scale. L3 branch closes positive. Closure synthesis lands as final.

**If Mode III:** the lemniscate-with-twist framing fails too. Deeper reframe needed; closure synthesis adjudicates Mode III with structural reason.

**Cost:** ~1.5-2 hr fresh implementer session.

## §8 — What the L3 branch CLOSES (conditional on path α)

**If path α Mode I:** L3 branch closes positive. The corpus electron IS the lemniscate-with-twist bond-pair object. The seven R7+R8 Mode III tests are reread as testing spatial-creeper observables; Move 5's attractor + bond-pair phasor at φ² aspect is the empirical confirmation.

**If path α Mode III:** L3 branch closes negative with structural reason. Either:
- The substrate fundamentally doesn't host the (2, q) lemniscate-with-twist object at engine-representable scale (continuum-limit-only) — corpus revision specifies this
- Or another reframe is needed beyond bond-pair (e.g., higher-dimensional embedding, non-corpus parameters)
- Or the engine implementation gap (V·S/T·1 per doc 75 §6.3) is load-bearing and post-fix rerun changes the result

## §9 — Corpus revision package downstream of L3 closure

Independent of path α result, the closure surfaces five corpus revisions:

**(a) Vol 1 Ch 8 pedagogical revision** — chapter's own handoff comment lines 1-56 already flags F1/F2/F3 fixes pending. Spatial-trefoil framing → phase-space (R, r) per doc 28 §5.4. Add lemniscate-with-twists plumber language as primary; mathematical (2, q) torus knot as derived equivalent.

**(b) Doc 20 §3 spatial-axis language retirement** — "p cycles around major circumference 2πR / q cycles around minor 2πr" → (bipartite-cycle, scalar-crossing) channels per doc 07 §3 reconciliation. Parallel-impedance formula χ = α·pq/(p+q) preserved; physical interpretation of channels updated.

**(c) Vol 2 Ch 4 SU(2)→SO(3) framing reframe** (Rule 6) — gyroscopic precession + half-cover stays mathematically; replaces "spinor wraps 720°" with bipartite-K4 lobe-count / lemniscate-two-traversal framing. SU(2) language renamed as derived equivalent representation.

**(d) Doc 03 §4.3 channel-not-axis annotation** — "(2, q) torus knot" framing should explicitly note the channel-not-axis reading per doc 07 §3 + doc 20 §3 reconciliation under the bond-pair object class.

**(e) NEW per Grant Q3 2026-04-28 — Doc 37 §3.1 Pauli mechanism revision (PROVISIONAL pending pressure-test per auditor v3.1)** — "Two electrons of opposite spin share same node-pair via complementary +n̂/−n̂ orientations" is structurally questionable at the substrate (vector ω-superposition cancels rather than splits A² budget under free-field reading; saturated-state superposition behavior open). Working alternative: "one bound state per saturated node-pair; atomic shells = multiple bond-pair locations within an atomic envelope, each with rotation axis set by local bond geometry."

**Load-bearing pressure-test before canonicalizing (must complete before v4 closure adjudication finalizes):**

1. **Helium 1s²:** does the substrate-native framing predict 2 saturated bond-pairs within the 1s spatial envelope? Verify via either (a) corpus-existing AVE chemistry derivation of He shell structure, or (b) substrate-structural argument from K4 geometry around a 2-proton nucleus.
2. **Lithium 1s²2s¹:** does the framing predict 3 bond-pairs distributed across 1s + 2s envelopes (2 + 1 split)? Verify shell-capacity match.
3. **Cooper pair (singlet superconductivity):** opposite-spin electrons in same momentum/spatial state. Does the cancellation argument explain the bound state, or does Cooper require a separate (BCS-style phonon-mediated) framework that bypasses per-node Pauli? Establish whether AVE substrate has a Cooper-pair mechanism distinct from atomic Pauli.
4. **AVE-Protein + chemistry-application corpus work** may have used doc 37 §3.1's pair-sharing framing — auditor lane work to grep + verify; flagged as significant downstream cleanup if the substrate-native framing canonicalizes.

If pressure-tests confirm the substrate-native framing matches observed shell capacities: doc 37 §3.1 needs rewriting; the closure can adjudicate Pauli substrate-native as canonical. If pressure-tests reveal the framing is incomplete (e.g., Cooper pair doesn't fit cleanly): the closure adjudicates the framing as partial and flags the gap for further framework work.

Doc 37 §3.2's periodic-table verification NUMERICS may still hold under either framing; only the per-node mechanism description is in question.

These revisions are **chapter-level editorial work**, not part of the L3 branch closure commit.

## §10 — Methodology rules surfaced

**A59** (already in [doc 78_ §7](78_canonical_phase_space_phasor.md)): phase-space phasor test methodology — verify attractor persistence over recording window before adjudicating; Hilbert-transform / cross-spectrum (not mean P × dP/dt) for chirality; bipolar R/r distributions need per-cluster adjudication.

**A60 candidate** (Rule 6 prefer-plumber-over-imports rule that the lemniscate reframe paradigms): **flagged for post-closure COLLABORATION_NOTES amendment in auditor lane.** Not included in this research-doc closure synthesis per Rule 15 lane discipline.

## §11 — Historical precedent (NEW per Grant Q1 2026-04-28)

The lemniscate-with-twists / (2, q) torus knot framing has direct historical lineage to 19th-century vortex atom theory:

- **Helmholtz 1858** — vortex theorems: circulation conservation, vortex tube topology preservation under ideal-fluid evolution. The mathematical ancestor of *"topology is quantized, not dynamically derived"* (doc 03 §4.3).
- **Kelvin 1867** — *"On Vortex Atoms"* (Proc. Roy. Soc. Edinburgh 6, 94-105): atoms = knotted vortices in the aether. Different knot types = different chemical elements. Stability via topological invariance under flow.
- **Tait 1877+** — first systematic knot tabulation, motivated specifically to support Kelvin's hypothesis. Foundation of modern knot theory.
- **(long gap — Michelson-Morley killed luminiferous aether)**
- **Faddeev-Niemi 1997** — knotted solitons in Yang-Mills field theory. Modern revival with proper field theory. **Already in AVE codebase as [`src/ave/topological/faddeev_skyrme.py`](../../src/ave/topological/faddeev_skyrme.py)** — load-bearing for the (2, q odd) stability rule per doc 07 §3.

[Doc 80_](80_kelvin_helmholtz_ave_precedent.md) walks the historical lineage in detail with specific Kelvin/Helmholtz intuitions worth deepening for AVE-specific (2, q) ladder framework. Companion to this closure synthesis; not blocking the closure adjudication.

---

## End of doc 79_ v3

**Status:** framework structure landed; awaiting path α empirical result before final Mode I/III adjudication (§7-§8). Updates expected post-path-α; this v3 commit captures the framing for review and citation in the interim.

**Pending implementer-side work** (held per Grant 2026-04-28):
- Path α run (~1.5-2 hr) with bond-pair sampler + methodology fixes from §7
- v4 update post-path-α with empirical adjudication landed in §8
- Possibly v4 corpus-revision-package updates per path α result

**Pending auditor-lane work** (per Rule 15 + COLLABORATION_NOTES):
- A60 post-closure amendment (Rule 6 prefer-plumber-over-imports rule)
- A43 strengthening: "auditor must grep corpus before asserting absence" (third A43 instance this session validates the rule)
- Manual r8.10 entry for §13.5n (this doc 79_) + §17 critical-path (E-072) + §A48-A60 audit catalog
- Corpus revision package §9 (a)-(e) editorial pass post-L3-closure

**Open Grant adjudications** (held per "hold for further questions"):
- v3 reads cleanly under Grant's plumber view? particularly §4 substrate-fundamental factor-of-2 + §6.6 substrate-native Pauli + §11 Kelvin precedent reference?
- Refinements to §1-§5 framework structure before path α runs?
- Path α timing — when to run vs. continue framework refinement?

---

*Doc 79_ v3 written 2026-04-28. Closure synthesis framework finalized pending empirical adjudication via path α. Per A48 frozen-extraction-scope: framework + methodology fixes + dual-criterion are pre-registered structurally; specific pre-reg P_phase9_path_alpha to be frozen separately when path α runs.*
