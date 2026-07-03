[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-nogo4l]
path-stable: "the canonical home for the four-lock sourced-charge no-go cascade + the survivor map (lane Z harmonic sector, lane W pairs, the J-mixed entry condition)"
-->

# The Sourced-Charge No-Go Cascade — Four Locks, One Route

> **What this leaf is.** A **consolidation home**, not a derivation. Across
> 2026-07-03 the EM-readout derivation epic (Axiom 2's last underived leg — does
> the winding's charge label emerge as a *sourced* static exterior field?) closed
> the SOURCED-static-monopole route through **four independent locks**, each
> discovered by a different instrument and each with its own proof class. This
> leaf gathers all four in one place, states the survivor map, and points at the
> canonical per-lock homes. The synthesis claim is `clm-nogo4l`
> ([`common/claim-quality.md`](claim-quality.md)); this leaf is the prose umbrella.

<!-- claim-quality: clm-nogo4l — the four-lock sourced-charge no-go cascade synthesis -->

## The scope guard (read first — verbatim, load-bearing)

> **No claim that charge fails.** The claim is that charge is **UNSOURCED** — that
> no *sourced static exterior monopole* emerges from the winding's constitutive
> texture or from a curl-coupled dynamics. **Topology and pairs remain live.** The
> winding's `Q = Link(∂Ω, F) ∈ ℤ` label (`clm-ze4clw`) is not touched; it lives in
> the **harmonic** sector (lane Z), which every lock explicitly leaves open. The
> inter-winding pair force (`clm-wcoul2`, lane W) is not touched. And the
> **`ε → 0` puncture caveat** — the one place the maximum-principle hypothesis
> fails (a bond exactly at the yield/rupture point, `S = 0`) — is lane Z's
> doorway, not a closed door. **mass = A1 (PR #260) is untouched** throughout; only
> the sourced-monopole *route to the charge readout* is closed.

## The four locks

Each lock closes the route from a different direction. Two are **instrument-class**
(an apparatus could not have read the alternative); two are **theorem-class** (the
route is structurally forbidden). Ordered by discovery.

### Lock 1 — blind-readout retraction (instrument class; PR #477)

The Stage-1 blind-readout panel (2026-07-03, PR #477) caught a **merged null read
on a structurally-degenerate observable without a same-pipeline positive control**
— the CLASS-2 blind-readout pathology. The retraction motivated the full
verdict-exposure sweep
([`research/2026-07-03_engine-verdict-exposure-sweep_result.md`](../../../research/2026-07-03_engine-verdict-exposure-sweep_result.md)),
which graded 31 merged engine verdicts against two apparatus-pathology classes
(CLASS-1 stencil pathology, CLASS-2 blind readout). **Proof class:
INSTRUMENT-AUDIT** — it makes no chord/echo/emergence claim about the vacuum; it
grades the *evidentiary standing* of a readout. The lesson it hard-wired into the
epic: a null on an observable the apparatus was never shown able to read the
*opposite* of is not physics. Every subsequent Stage required a same-pipeline
liveness positive control before any winding-null could count.

### Lock 2 — sourced-solve tautology (instrument class; Stage-1b identity)

The Stage-1b static-linear result
([`research/2026-07-03_em-readout-vsector-stage1b_result.md`](../../../research/2026-07-03_em-readout-vsector-stage1b_result.md),
§3; the retracted Stage-2 prereg §1 records it verbatim-faithful) showed that a
**linear static solve `L φ = b` with a hand-assembled `b` is INFORMATIONALLY
TRANSPARENT**: `∇·E = +(source − mean)` *by construction of the solve* — the
enclosed-charge observable `Q_enc = Σ_Ω(∇·E) = Σ_Ω(b − mean)` returns the source
you built. It is a **MIRROR, not an instrument** — the solve gives back its own
RHS. The Stage-2 redesign inherited this as the un-riggability core (there must be
NO right-hand-side source term, EVER); the winding may enter ONLY the constitutive
state. **Proof class: INSTRUMENT / identity** — a tautology of the discrete Gauss
theorem, not a physics negative. It closes the *sourced* branch: any monopole a
sourced solve reports was assembled by hand.

### Lock 3 — [NO-FLUX-STRUCTURAL] maximum principle (theorem class; ε > 0)

With the sourced branch closed, the Stage-2a redesign built the source-free
alternative: a variable-coefficient homogeneous PDE `L_w φ = 0`,
`L_w = Bᵀ diag(ε_eff) B`, where the winding textures `ε_eff = S(A(r)) > 0` but
never appears as a source. The result was **[NO-FLUX-STRUCTURAL] at theorem grade**
(Stage-2a retirement addendum,
[`research/2026-07-03_em-readout-stage2-redesign_prereg.md`](../../../research/2026-07-03_em-readout-stage2-redesign_prereg.md)
§R1): the Dirichlet energy `φᵀ L_w φ = Σ_edge ε_eff·(Δφ)²` vanishes iff every term
vanishes (each is non-negative), forcing `Δφ ≡ 0` on the connected srs graph,
hence `φ = const` — **zero field, zero flux, for ANY strictly-positive edge
weights, ANY texture, ANY composition rule (Q/M/X), ANY regime.** **Proof class:
THEOREM** (discrete maximum principle / Dirichlet-energy argument), established
three independent ways (maximum-principle analytic + panel ablation
`max|φ| = 0.000e+00` exact + nullspace check: `L_w` has a 1-D nullspace = the
constant). **The one honest caveat, NOT silently dropped:** the hypothesis is
`ε_eff = S(A) > 0` *strictly*. At `S = 0` exactly (full saturation, `A = 1`, a bond
at the rupture point) the positivity fails and the connectedness argument no longer
forces `φ = const`. This `ε → 0` puncture is out-of-scope for the sub-yield
instrument — and it is **lane Z's doorway** (see survivor map).

### Lock 4 — ∂∂=0 continuity (theorem-grade lean; step-0 note)

The Stage-2b Step-0 continuity note
([`research/2026-07-03_em-readout-stage2b-step0-continuity_note.md`](../../../research/2026-07-03_em-readout-stage2b-step0-continuity_note.md))
asked whether the *dynamical* route escapes the statics death. Taking the discrete
divergence of the chartered Ampère update and using the DEC identity `∇·∇× ≡ 0`
(the exact `∂₁∂₂ = 0` boundary-of-boundary identity on the srs 2-complex):
`∂_t(∇·(ε_eff E)) = −∇·J_coupling`. For the **default axiom-native LC coupling —
an Ampère-form curl drive `J_coupling = ∇×(g(A) ω) = curl_adj(·)`** — the
divergence is identically zero, so `∂_t(∇·E) ≡ 0`: **the enclosed charge is a
conserved constant of motion**, set by initial data, not emergent. The DC monopole
content of any settled state is whatever was seeded — the statics tautology in
dynamical clothing. **Proof class: THEOREM-GRADE LEAN** (an algebraic identity on
the chartered update equations, needing no integrator; the `∂₁∂₂ = 0` core is
theorem-grade and test-asserted, PR #483). The lean qualifier: it holds *unless* a
specific **J-mixed** coupling term exists — one with `∇·J_coupling ≠ 0` that is
(a) ω-field-derived (no integer), (b) not a static texture (evades Lock 3),
(c) not a forbidden propagating longitudinal mode — a term **canon does not
currently supply**, surfaced flag-don't-fix to the orchestrator review gate.

## The unifying observation (why statics AND curl-coupled dynamics die by the same theorem)

Locks 3 and 4 are not two coincidences — they are **one theorem operating twice**.
The DEC result names its own operator
([`research/2026-07-03_srs-dec-operators_result.md`](../../../research/2026-07-03_srs-dec-operators_result.md),
`src/ave/topological/srs_dec.py:242`): *"div∘curl_adj = −∂₁∂₂ = 0 ← THE THEOREM's
operator: any F=curl_adj(anything) has div F ≡ 0, hence zero enclosed charge."*

- **Statics died** because the winding's substrate flux `F = ∇×ω = curl_adj(ω)`
  is exactly such an F (a curl), so `∇·F ≡ 0` — no monopole. (Lock 3's
  maximum-principle theorem is the complementary statement: a *texture* is not a
  curl-source either, so it cannot source `∇·E` from the source-free side.)
- **Curl-coupled dynamics dies** for the identical reason: `J_coupling = ∇×(g ω)`
  is again `curl_adj(·)`, so `∇·J_coupling ≡ 0`, so `∂_t(∇·E) ≡ 0`.

The **same `∂₁∂₂ = 0` theorem closes both routes.** The only escape — statically
or dynamically — is a mechanism whose source is NOT a pure curl of the ω field
(Lock 4's J-mixed, canon-unsupplied) OR a field that lives where `∂₁∂₂ = 0` does
NOT reach: the **harmonic sector**.

## The survivor map

The cascade closes the sourced *co-exact* (gradient) route. It leaves three live
paths, structurally distinct from the closed one:

### Lane Z — the harmonic sector (the structural complement)

By the Hodge decomposition of srs 1-cochains, the space `div` does NOT annihilate
splits into the **co-exact** part (`im grad = im ∂₁ᵀ` — the gradient/Coulomb
potential sector, `clm-4r4jiy`, the part the cascade closes) and the **harmonic**
part `H₁ = ker∂₁ ∩ ker∂₂ᵀ` (the DEC theorem,
[`research/2026-07-03_srs-dec-operators_result.md`](../../../research/2026-07-03_srs-dec-operators_result.md)
§4). Harmonic 1-cochains are **neither exact nor co-exact**, so `∇·∇× ≡ 0` does
not apply to them — this is the structural complement of the closed sector. Its
dimension is the measured topological invariant **`b₁ = 3`** (the three
non-contractible wraps of the periodic 3-torus; L-independent at L=3 and L=4). Any
Link-counting charge emergence (`Q = Link(∂Ω, F) ∈ ℤ`, `clm-ze4clw`) would land
here, not in the closed co-exact sector — but it requires a genuinely different
instrument: an **edge-field E representation** (the 1-cochain, not the node
potential φ) read through the DEC harmonic projector, invisible to every
scalar-φ instrument the cascade retired. The `ε → 0` puncture (Lock 3's honest
caveat) is lane Z's doorway.

### Lane W — winding pairs

The field *between* two windings (the clm-wcoul2 inter-winding force). The
pair-interaction may carry Coulomb sign structure even if the single-winding
exterior does not — the Stage-0 option-C hypothesis. `clm-wcoul2` (the engine-
derived Axiom-2 interaction leg: like windings repel, unlike attract, gapped-ω-
mediated, electric-not-magnetic) is the first landing in this lane. It is
CONSISTENCY-class (signed-Coulomb is SM-shared), booked as enabling infrastructure
for a future winding-pair *magnitude* chord.

### The J-mixed entry condition (β arc, in flight)

The one escape Lock 4 leaves open: a coupling current `J_coupling` with
`∇·J_coupling ≠ 0` that is ω-field-derived, not a static texture, and not a
forbidden longitudinal mode. **Pending** — surfaced to the orchestrator review gate
as the make-or-break entry condition for any Stage-2b build; the divergence of the
coupling must be established analytically BEFORE any integrator run (the discipline
the Stage-2a anchor-source violated). Cited here as **pending**, not resolved.

## Where the pieces live (consolidation map)

This leaf is the prose umbrella; the load-bearing machinery lives elsewhere:

- **Lock 1** — [`research/2026-07-03_engine-verdict-exposure-sweep_result.md`](../../../research/2026-07-03_engine-verdict-exposure-sweep_result.md)
  (the CLASS-2 blind-readout definition + the 31-row triage); PR #477 (the
  triggering Stage-1 panel catch).
- **Lock 2** — the Stage-1b tautology, recorded verbatim-faithful at
  [`research/2026-07-03_em-readout-stage2-redesign_prereg.md`](../../../research/2026-07-03_em-readout-stage2-redesign_prereg.md)
  §1 (from `research/2026-07-03_em-readout-vsector-stage1b_result.md` §3).
- **Lock 3** — the [NO-FLUX-STRUCTURAL] theorem, Stage-2a retirement addendum
  [`research/2026-07-03_em-readout-stage2-redesign_prereg.md`](../../../research/2026-07-03_em-readout-stage2-redesign_prereg.md)
  §R1 (the proof triple + the `ε → 0` caveat).
- **Lock 4** — the ∂∂=0 continuity note
  [`research/2026-07-03_em-readout-stage2b-step0-continuity_note.md`](../../../research/2026-07-03_em-readout-stage2b-step0-continuity_note.md)
  §2/§4 (the divergence-of-the-coupling reduction + J-mixed escape).
- **The class-level upgrade** — the srs DEC ∂₁∂₂=0 theorem,
  [`research/2026-07-03_srs-dec-operators_result.md`](../../../research/2026-07-03_srs-dec-operators_result.md)
  §3 (the theorem) + §4 (the harmonic `b₁=3` survivor sector); module
  [`src/ave/topological/srs_dec.py`](../../../src/ave/topological/srs_dec.py).
- **The charge dictionary** — `clm-ze4clw` (`Q = Link(∂Ω, F) ∈ ℤ`,
  [`common/boundary-observables-m-q-j.md`](boundary-observables-m-q-j.md)); the
  Coulomb potential (co-exact) sector `clm-4r4jiy`
  ([`vol4/claim-quality.md`](../vol4/claim-quality.md)).
- **The Axiom-2 interaction leg** (lane W) — `clm-wcoul2`
  ([`vol4/claim-quality.md`](../vol4/claim-quality.md)); the Ax2 leg-map is in
  [`common/axiom-register.md`](axiom-register.md) §"Axiom 2".
- **The charter** — the EM-readout derivation charter §5 cross-references
  (`_orchestration/2026-07-03_em-readout-derivation-charter.md`).

> ↗ See also: [FORM-Deriving / VALUE-Importing](form-deriving-value-importing.md)
> §"The AC/DC carve" — the epistemological frame under which this cascade is the
> DC-sector empirical validation (the sourced-monopole DC readout is closed
> co-exact-side; the survivors are DC→AC-coupling and topological/harmonic).
