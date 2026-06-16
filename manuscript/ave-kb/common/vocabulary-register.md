[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Canonical vocabulary register — hosts def- (adjudicated-term) nodes, the third tracked index after the claim graph (clm/exp/sup) and the code-provenance index. def- is a spine node-type specified in .index/SCHEMA.md and canonized in INVARIANT-S12 (extend-don't-reinvent); the Stage-2 emitter materializes each def- entry into claims.jsonl as a node_type: definition record (LIVE 2026-06-08). This leaf originates no clm-/exp-/sup- node-body via frontmatter — the def- entries are body-hosted register entries (the def- analog of clm-/sup- entries hosted in a claim-quality.md register, which is itself no-claim) — so it carries no-claim."
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
> `def-` spec) **and** Stage 2 are both **landed** (2026-06-08). Stage 2 wired
> `refresh-kb-metadata` to materialize each `def-` node into `claims.jsonl`
> (`node_type: "definition"`, sorted between `claim` and `experiment`) and
> `verify-kb-metadata` to drift-gate them under the same referential-integrity
> pass as `clm`/`exp`/`sup` (every `clm_cross_links` id resolves to a claim /
> experiment / support node; orphan = hard failure). The `def-` namespace is
> now part of the pipeline id grammar (`ANY_NODE_ID_RE` + `verify-md-links`),
> so a perturbed entry **fails `make verify-kb-metadata`** (INVARIANT-S12).

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

## carrier
<!-- id: def-a9eef5 -->

- **term:** carrier
- **adjudicated-meaning:** *(no single locked sense — ambiguous; canon gated on review)*. Primary contested reading: the fast internal phase oscillation $\omega = mc^2/\hbar$ — the "carrier" in a carrier × envelope decomposition.
- **axis:** phase-carrier (the contested primary axis)
- **dimension/type:** frequency (T⁻¹) for the carrier-frequency reading; n/a for the charge-carrier reading
- **status:** ambiguous
- **canonical-home:** *(none locked — gated on review)*
- **clm-cross-links:** *(none verified-specific yet)*
- **open-ambiguity-flag:** YES — (a) **carrier frequency**: the internal phase oscillation $\omega = mc^2/\hbar$, the "carrier × envelope" decomposition [phase-carrier]; (b) **charge carrier**: semiconductor majority/minority carrier [material / real-space]. §47 AMB-4 also lists (c) a "real-space lattice host" [spatial-Brillouin] reading.
  - conflicting sites: carrier × envelope `vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md:56,59` ("Gaussian envelope × sinusoidal carrier frequency"); internal-carrier $\omega$ `research/2026-06-08_highE-winding-aliasing-prereg.md:36` ("a carrier frequency $\omega > \omega_{fold}$ Nyquist-folds").
- **verification:** VERIFIED the carrier-frequency (phase-carrier) reading at the two cites. The §47 "real-space lattice host" [SB] sub-reading is NOT located at a specific corpus site → that sub-reading is flagged **OPEN**, not asserted. Status ambiguous (no locked sense; canon gated on Grant review per §47).

---

## Nyquist / aliasing
<!-- id: def-dcbdf2 -->

- **term:** Nyquist (and "aliasing")
- **adjudicated-meaning:** *(no single locked sense — the ambiguity IS the content: two physically-distinct axes that coincide numerically at $c/\ell_{node}$)*.
- **axis:** spatial-Brillouin vs phase-carrier (the clarity risk is the fusion of these two axes — A46)
- **dimension/type:** spatial frequency (L⁻¹) vs temporal frequency (T⁻¹)
- **status:** ambiguous
- **canonical-home:** *(no single home — disambiguation at `research/2026-06-08_highE-winding-aliasing-prereg.md:68`)*
- **clm-cross-links:** clm-yc7fgm
- **open-ambiguity-flag:** YES — (a) **SPATIAL-Brillouin / wavenumber** axis: aliasing of spatial frequency $q > \pi/\ell_{node}$ (canonical; the corpus RESTRICTS "aliasing" to this axis); (b) **PHASE-CARRIER** axis: Nyquist-folding of the internal carrier $\omega = mc^2/\hbar$ (the A46 extension the corpus forbids fusing). "They coincide numerically at $c/\ell_{node}$ but are physically distinct geometries."
  - conflicting sites: two-axis distinction verbatim `research/2026-06-08_highE-winding-aliasing-prereg.md:68`; spatial-Brillouin canonical `vol1/dynamics/ch3-quantum-signal-dynamics/paley-wiener-hilbert.md:10`.
- **verification:** VERIFIED at prereg:68 (the two axes "coincide numerically at c/ℓ_node but are physically distinct geometries"). Status ambiguous — the A46 axis-fusion is the live clarity risk.

---

## phase-space
<!-- id: def-69f472 -->

- **term:** phase-space
- **adjudicated-meaning:** the $(V_{inc}, V_{ref})$ / Clifford-torus **phasor coordinate space** — a distinct coordinate space from real space ("the trefoil lives in phase space; the soliton lives in real space"). Held ambiguous because the surface form is actively conflated with a SIZE.
- **axis:** phase-carrier (coordinate-space) — contested against a spatial size-reading
- **dimension/type:** phasor coordinate (dimensionless plane) vs (mis-applied) length
- **status:** ambiguous
- **canonical-home:** `vol1/ch8-alpha-golden-torus.md:29` (the coordinate-space meaning)
- **clm-cross-links:** clm-0ktpcn, clm-3zz0f6
- **open-ambiguity-flag:** YES — (a) a distinct **COORDINATE space**: "the trefoil lives in phase space; the soliton lives in real space" (canonical, well-cited); (b) conflated with a **SIZE / "sub-node" spatial scale** (the A46 leak; forbidden). Real-space ≠ phase-space is canonical as COORDINATES, NOT a size-claim.
  - conflicting sites: coordinate meaning `vol1/ch8-alpha-golden-torus.md:29`; the size-conflation flagged in §46/§47.
- **verification:** VERIFIED the coordinate-space meaning at ch8:29. Held **ambiguous** (per the §47 clarity-risk list), NOT SOLID, precisely because the surface form is actively conflated with a length (the A46 size-leak) — SOLID is reserved for the spine-blessed `node` per §46.

---

## size
<!-- id: def-249370 -->

- **term:** size (soliton size)
- **adjudicated-meaning:** *(NO canonical soliton-size definition exists — confirmed GAP, §45)*. The corpus uses ≥6 length scales + 1 dimensionless ratio for "size" and never picks one.
- **axis:** spatial-Brillouin (the contested length axis) / mixed
- **dimension/type:** length (L) — but unspecified WHICH length
- **status:** ambiguous
- **canonical-home:** *(none — confirmed GAP)*
- **clm-cross-links:** *(none — no canonical definition to cross-link)*
- **open-ambiguity-flag:** YES — the conflation is **CANONICAL** (not session-introduced) and is the root cause of the §43 / sub-node tension: ≥6 length scales + 1 ratio share the word "size".
  - conflicting sites: substrate pitch $\ell_{node}$; charge radius $D_p$ `src/ave/core/constants.py:971`; tube radius $\ell_{node}/(2\pi)$; real-space envelope `src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py:77`; the dimensionless r_opt ratio `vol2/particle-physics/ch01-topological-matter/torus-knot-ladder.md:21`; multi-node body envelope `manuscript/vol_2_quantum/chapters/02_baryon_sector.tex:40`.
- **verification:** GAP VERIFIED — 0 hits for any canonical "soliton size" definition (3 greps empty, §45). The §45 RECOMMENDATION (canonical size = the saturation boundary $r_{body}(m)$) is a PROPOSAL gated on the unresolved §45 A-vs-B fork, NOT adopted — so "size" stays ambiguous, not SOLID.

---

## radius
<!-- id: def-7e029c -->

- **term:** radius (R / r / r_opt glyph cluster)
- **adjudicated-meaning:** *(≥3 distinct objects under overlapping glyphs — ambiguous)*: major torus radius $R$, tube/minor radius $r = \ell_{node}/(2\pi)$, and the dimensionless r_opt "radius" ratio.
- **axis:** spatial-Brillouin / dimensionless (mixed)
- **dimension/type:** length (L) for $R$ and $r$; dimensionless for r_opt
- **status:** ambiguous
- **canonical-home:** *(none single)*
- **clm-cross-links:** clm-uatcql, clm-k6olj8
- **open-ambiguity-flag:** YES — three objects under one glyph: (a) **major (torus) radius** $R$ [L]; (b) **tube/minor radius** $r = \ell_{node}/(2\pi)$ [L]; (c) the **dimensionless r_opt** "radius" ratio. PLUS a **dimension collision**: a "RMS scattering cross-section = 0.84 fm" equates an AREA (L²) to a LENGTH — the 0.84 fm is the charge RADIUS (L), not a cross-section (L²).
  - conflicting sites: tube radius `electron-identification.md:77` (row 2, "tube radius $\ell_{node}/(2\pi)$"); major/minor + dimensionless ratio `vol2/particle-physics/ch01-topological-matter/torus-knot-ladder.md:21`; radius-vs-cross-section dimension collision `manuscript/vol_2_quantum/chapters/02_baryon_sector.tex:40`.
- **verification:** VERIFIED the glyph-overloading at the three cites; the cross-section/radius dimension collision VERIFIED at `02_baryon_sector.tex:40` ("RMS … effective scattering cross-section" called the 0.84 fm "radius").

---

## r_opt
<!-- id: def-0e457a -->

- **term:** r_opt
- **adjudicated-meaning:** *(THE CLARITY-KILLER, §47 AMB-2 — TWO genuine meanings under one token)*. **Meaning A** = dimensionless coupling-budget ratio $\kappa_{FS}/q$ ("NOT a length"; the §43 target; a third token `r_conf` also denotes this). **Meaning B** = a GENUINE envelope-length (soliton HWHM / tube-radius, a live fit-param = `HORN_R`).
- **axis:** dimensionless (Meaning A) vs spatial-Brillouin (Meaning B)
- **dimension/type:** dimensionless (A) vs length L (B)
- **status:** ambiguous
- **canonical-home:** Meaning A `vol2/particle-physics/ch01-topological-matter/torus-knot-ladder.md:21`; Meaning B `src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py:77`
- **clm-cross-links:** clm-k6olj8
- **open-ambiguity-flag:** YES — "r_opt is dimensionless" was HALF the story; Meaning B is a genuine length.
  - conflicting sites: Meaning A `vol2/particle-physics/ch01-topological-matter/torus-knot-ladder.md:21` ("the dimensionless coupling-budget ratio, NOT a length"); Meaning B `src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py:77-78` (`r_opt = max(r, 1.0); envelope = amplitude*π/(1+(rho_tube/r_opt)²)`) and `src/scripts/vol_1_foundations/r10_path_alpha_v14e_seven_mode_seed.py:132-133` (`r_opt = HORN_R`).
  - resolution-proposal (gated): split — `κ_share` (def-24e6e6) for Meaning A; `r_env` (def-088f0d) for Meaning B.
- **verification:** BOTH meanings VERIFIED at their cites. Status ambiguous; the resolution is the proposed split (not yet adopted — gated on Grant review).

---

## Compton
<!-- id: def-90f843 -->

- **term:** Compton
- **adjudicated-meaning:** *(ambiguous — the SUFFIX is the sole disambiguator)*: "Compton **wavelength**" $\lambda_C = \hbar/m_e c = \ell_{node}$ [length] vs "Compton **frequency** / Compton **clock**" $\omega = mc^2/\hbar$ [frequency].
- **axis:** spatial-Brillouin (wavelength) vs phase-carrier (frequency)
- **dimension/type:** length (L) vs frequency (T⁻¹)
- **status:** ambiguous
- **canonical-home:** wavelength `vol1/ch0-intro.md:48`; frequency `vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md`
- **clm-cross-links:** clm-oltvwy, clm-qde5gn
- **open-ambiguity-flag:** YES — (a) "Compton **wavelength**": length $\lambda_C = \hbar/m_e c = \ell_{node}$ [spatial-Brillouin, L]; (b) "Compton **frequency** / Compton **clock**": $\omega = mc^2/\hbar$ [phase-carrier, T⁻¹]. The suffix (wavelength vs frequency/clock) is the ONLY disambiguator.
  - conflicting sites: wavelength `vol1/ch0-intro.md:21,48` ("electron's Compton wavelength", "reduced Compton wavelength of the electron"); frequency/clock `vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md`.
- **verification:** VERIFIED both readings via grep — "Compton wavelength" at `ch0-intro.md:21,48`; "Compton clock/frequency" leaves enumerated.

---

## winding
<!-- id: def-3638f2 -->

- **term:** winding
- **adjudicated-meaning:** *(ambiguous — two distinct axes)*: real-space knot CROSSING number (the electron is the $0_1$ UNKNOT, NO real-space crossings) vs the phase-space $(2,3)$ Clifford-torus WINDING pattern (2 on the d-axis, 3 on the q-axis).
- **axis:** real-space topology (other) vs phase-carrier
- **dimension/type:** integer crossing count vs integer winding pair (both topological / dimensionless)
- **status:** ambiguous
- **canonical-home:** `vol1/ch8-alpha-golden-torus.md:29`; `electron-identification.md:77` (row 3)
- **clm-cross-links:** clm-0ktpcn, clm-uatcql
- **open-ambiguity-flag:** YES — (a) real-space knot **CROSSING** number: the electron is the $0_1$ UNKNOT, NO real-space crossings [real-space topology]; (b) the phase-space $(2,3)$ Clifford-torus **WINDING** pattern [phase-carrier]. The $(2,3)$ "trefoil" lives in phase space, NOT a real-space knot.
  - conflicting sites: real-space-$0_1$-vs-phase-space-$(2,3)$ `vol1/ch8-alpha-golden-torus.md:29`; the disambiguation row `electron-identification.md:77` (row 3).
  - **OPEN sub-flag (over-read guard):** §47 asserted "winding/$(2,3)$ LEAKS to size (`torus-knot-ladder.md:21` 'higher q→smaller solitons')". This did **NOT verify**: `torus-knot-ladder.md:21` states r_opt is "the **dimensionless coupling-budget ratio, NOT a length**" and "Higher $q$ gives a **smaller dimensionless budget ratio**" (NOT "smaller solitons"). The cited line is the careful disambiguated form; the size-leak claim is unsupported at that cite → recorded **OPEN**, not seeded as fact (flag-don't-fix).
- **verification:** the real-space-vs-phase-space axis-ambiguity VERIFIED (ch8:29, electron-id:77 row 3). The §47 "winding-leaks-to-size" sub-claim FAILED verification at its cited site (`torus-knot-ladder.md:21` says the opposite) → recorded OPEN.
  - **PROPOSED SHARPEN (C4, 2026-06-15 — awaiting Grant ratification; NOT yet canonical; Rule-12: appended AFTER the def-3638f2 verification line, nothing above edited; this does NOT resolve the node's pre-existing real-space-crossing-vs-phase-winding ambiguity — it adds an orthogonal [Q]≡[L]-vs-integer dimension axis):** the multi-lane synthesis phrased charge as *"a conserved integer, NOT a length or magnitude."* That is correct for the **winding NUMBER** but would over-read if taken to deny Axiom-2's canonical charge dimension. SHARPEN: **the winding NUMBER is the conserved, dimensionless INTEGER** ($N\in\mathbb{Z}$; *"charge is defined as an integer topological winding number ... True fractional twists are mechanically forbidden"* — `topological-fractionalization.md:12`, clm-mnb3lt/clm-67jn9o); **the dislocation that number LABELS carries** $[Q]\equiv[L]$ (Burgers vector $=\ell_{node}$, $\xi_{topo}=e/\ell_{node}$ C/m — `eq_axiom_2.tex:13`). Do NOT assert charge is dimensionless tout court — that contradicts Axiom 2. (Cross-link: charge=$T_2$ (2,3) winding is ORTHOGONAL to the $A_1$/V-scalar mass — `master-equation.md:20`, def-5d2b8a; this is the C4 charge=winding statement, which folds as a cross-link into the PROPOSED `BoundResonator` node def-b42e9d, leaving the electron's eigenmode-EXISTENCE instantiation FLAGGED open.)

---

## δ (delta glyph)
<!-- id: def-de17a0 -->

- **term:** δ (the "delta" glyph — three distinct overloaded senses)
- **adjudicated-meaning:** *(no single locked sense — the overload IS the content: three physically-distinct dimensionless quantities share the glyph δ across the corpus, separated by ~3 OOM in magnitude)*.
- **axis:** notation (cross-file glyph overload)
- **dimension/type:** dimensionless (all three); distinct quantities
- **status:** ambiguous
- **canonical-home:** *(no single home — three senses canonical in three leaves; see open-ambiguity-flag)*
- **clm-cross-links:** clm-009nkt (δ_strain), clm-f0jwtk (δ_AVE)
- **open-ambiguity-flag:** YES — three distinct senses:
  - (a) **δ_strain** — the vacuum strain coefficient / cosmic-scale TCC, ≈ 2.225×10⁻⁶ = 1 − CODATA/α_cold (a *definitional residual*; FT-1 magnitude-closed, sign-only). Home: `vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md` (clm-hp7nlm); observable at `vol1/claim-quality.md:105` (clm-009nkt). [TCC / thermal axis]
  - (b) **δ_AVE** — the substrate temporal loss tangent ≡ t_sat/t_period ∈ [0,1] (Class-1 definitional). Home: `temporal-saturation-regime-classifier.md` (clm-f0jwtk). [loss-tangent / saturation-duty axis]
  - (c) **δ = arctan α ≈ 0.418°** — the EE slip angle, where tan δ = α = 1/Q (a Class-A EE identity, NOT an independent prediction). Home: `translation-tables/translation-circuit.md` §10.3:626. [loss-angle axis]
  - **The cross-file clarity risk is (a) vs (b)/(c):** δ_strain (≈ 2.2×10⁻⁶) is **~3280× SMALLER** than the loss-tangent family tan δ = α (≈ 7.3×10⁻³) — they are NOT in the same numerical range and must never be equated (there is no "δ_strain in the tan-δ range" coincidence). Within §10.3, (b) and (c) are the **SAME object** (δ_AVE = δ = arctan α, the α = 1/Q = tan δ identity) — an intentional identity, NOT a clash; do not split it.
- **verification:** VERIFIED — δ_strain value/home at `delta-strain-cosmic-tcc.md:13` + `vol1/claim-quality.md:108`; δ_AVE ≡ t_sat/t_period at `common/claim-quality.md:1154`; δ = arctan α ≈ 0.418° at `translation-circuit.md:626`. The ~3280× gap computed from CODATA α (2.225×10⁻⁶ vs 7.297×10⁻³). Status ambiguous — cross-file glyph reuse; the §10.3 (b)=(c) is an intentional identity, not an overload.

---

## κ_share *(proposed)*
<!-- id: def-24e6e6 -->

- **term:** κ_share (kappa_share)
- **adjudicated-meaning:** *(PROPOSED, gated)* the dimensionless coupling-budget ratio $\kappa_{FS}/q$ — the §43/§46 rename target for r_opt **Meaning A**. A pure number; the dimensional-provenance LINT rule is **NEVER $\times\,\ell_{node}$**.
- **axis:** dimensionless
- **dimension/type:** dimensionless
- **status:** proposed
- **canonical-home:** *(none — coinage; origin §43/§46/§47 epic adjudication)*
- **clm-cross-links:** clm-k6olj8 (the r_opt-as-ratio claim it would rename)
- **open-ambiguity-flag:** no (a fresh coinage carries no prior overloading)
- **verification:** VERIFIED **0 prior corpus hits** for `κ_share`/`kappa_share` (safe to coin). **GATED on Grant review — NOT adopted, NOT SOLID.** Seeding a coinage SOLID would violate the proposed-gate (a coinage with prior hits would be a collision, not a coinage).

---

## r_env *(proposed)*
<!-- id: def-088f0d -->

- **term:** r_env
- **adjudicated-meaning:** *(PROPOSED, gated)* the soliton real-space **ENVELOPE length** (HWHM / tube-radius / saturation-boundary) — the separate name for r_opt **Meaning B**, so the length sense never reuses the dimensionless-ratio glyph.
- **axis:** spatial-Brillouin
- **dimension/type:** length (L)
- **status:** proposed
- **canonical-home:** *(none — coinage; the existing fit-param is currently named r_opt / `HORN_R`)*
- **clm-cross-links:** *(none verified-specific yet)*
- **open-ambiguity-flag:** no
- **verification:** VERIFIED **0 prior exact-token `r_env` hits** (the broad pattern catches the unrelated `HORN_R` constant, but the exact token `r_env` is unused). **GATED on Grant review — NOT SOLID.**

---

## node-Nyquist-size-boundary *(proposed)*
<!-- id: def-e0cd83 -->

- **term:** node-Nyquist-size-boundary
- **adjudicated-meaning:** *(PROPOSED, gated)* the single spatial scale at which a soliton's real-space body crosses the node Nyquist boundary — distinguishing a **supra-node body envelope** from a **sub-node charge-core feature** (the §45 A-vs-B fork).
- **axis:** spatial-Brillouin
- **dimension/type:** length (L) $= \ell_{node}$
- **status:** proposed
- **canonical-home:** *(none — coinage; §46 node-Nyquist size resolution)*
- **clm-cross-links:** clm-yc7fgm (the node = spatial-Nyquist boundary claim it builds on)
- **open-ambiguity-flag:** no
- **verification:** VERIFIED **0 prior corpus hits**. **GATED on Grant review AND on the unresolved §45 A-vs-B canonical FORK** (sub-node charge-core vs supra-node body envelope) — NOT SOLID.

---

<!-- PROPOSED CANDIDATE — awaiting Grant ratification; NOT yet canonical. Insert this block ABOVE the `## SubstrateExcitation *(proposed)*` heading (the anchor line). status:proposed, GATED on auditor + Grant. Verified 0 prior corpus hits for the surface form 'TKI-transformer' (the only existing 'transformer' object is the SOLITON STRUCTURE of translation-circuit.md §9.2 — see open-ambiguity, do NOT overload). -->

## TKI-transformer *(proposed)*
<!-- id: def-tk1xfm -->

- **term:** TKI-transformer (topo-kinematic transduction; the Axiom-2 dictionary read as an ideal transformer)
- **adjudicated-meaning:** *(PROPOSED, gated)* Axiom 2 (Topo-Kinematic Isomorphism, `eq_axiom_2.tex:12`) read as the **ideal, lossless, gain-1, pole-less, INVERTIBLE electromechanical dictionary** between the substrate's mechanical port ($u$/strain $\leftrightarrow$ E, $\omega$/curl $\leftrightarrow$ B) and its electrical port — a **structure-preserving change-of-reference**, the units-checked $\xi_{topo}$ six-row identity table ($Q=\xi x,\ I=\xi v,\ V=\xi^{-1}F,\ L=\xi^{-2}m,\ C=\xi^{2}\kappa,\ R=\xi^{-2}\eta$; `translation-circuit.md:17-26`, clm-fy05jc), which are *"identity statements ... not approximations, not analogies"* (`translation-circuit.md:41`). It transduces **losslessly** — same joule, two gauges — and does **NOT** trap, convert-with-gain, or carry a pole. **It is NOT the resonator's transfer function:** the DYNAMICS (poles = masses, $Q = 1/\alpha$ = the per-cycle radiative leak, saturation = the trap) live in the **four-axiom resonator $H(s)$** (`cvr-transfer-function.md:23-47`), NOT in Axiom-2. The dictionary and the transfer-function are different objects; conflating them inflates a units-bridge into a derived mechanism.
- **axis:** notation / other (a re-reading of an axiom as an EE structure; emits no quantity of its own)
- **dimension/type:** class/structure (n/a — a transduction map; the $\xi_{topo}$ it carries is C/m, INVARIANT-C2)
- **status:** proposed
- **canonical-home:** *(none — coinage; the underlying isomorphism is `eq_axiom_2.tex:12`, the dictionary table `translation-circuit.md:17-26` clm-fy05jc, the contrast object `cvr-transfer-function.md:23-47`)*
- **clm-cross-links:** clm-fy05jc (the $\xi_{topo}$ dictionary), clm-eemap1 (EE-as-substrate-native at minimal-DOF)
- **canon-noun map:** the non-canon engineering name 'TKI-transformer' maps to the canon noun **Topo-Kinematic Isomorphism (Axiom 2)**; it MUST NOT drift into a noun-swap and MUST inherit the strength ceiling *'identity-by-translation, NOT emerges-from / NOT a derivation'* (the `translation-circuit.md:660` piezo over-claim guard precedent).
- **open-ambiguity-flag:** YES — the surface form 'transformer' is overloaded against an existing live object, and one clause is split out to an open seam:
  - (a) **TKI-transformer (THIS node, proposed):** the $\xi_{topo}$ DICTIONARY / change-of-reference — gain-1, pole-less, invertible, lossless. [transduction map]
  - (b) the **soliton-structure 'transformer'** (already in corpus): the (p,q) winding read as toroidal transformer winding-numbers, with leakage-inductance $\to$ weak-force range — `translation-circuit.md:544-554` (the '#### Ideal transformer' sub-block WITHIN §9.2, clm-grounded :551). This is the SOLITON's STRUCTURE, a DIFFERENT object; do NOT let (a) and (b) collapse. [soliton structure]
  - (c) the **resonator $H(s)$** (already canonical): the DYNAMICS — the 2nd-order pole pair $s_\pm=-\alpha\omega_0/2\pm j\omega_d$, $Q=1/\alpha$ leak, $S(A_0)$ Axiom-4 detune (`cvr-transfer-function.md:30-41`). This is exactly what (a) is NOT. [transfer function]
  - **OPEN-SEAM (do NOT canonize — split out of C1):** the clause *'chirality = the handed turns-ratio SIGN $\to$ spin sign'* has **no corpus anchor** tying a transformer turns-ratio sign to spin sign. `eq_axiom_2.tex:21` grounds only **charge SIGN = dislocation handedness** (particle/antiparticle Burgers vectors), NOT spin. The chirality def-node (`def-7c3f9e`) is `status:ambiguous` with the production-vs-instrument split *explicitly unadjudicated* (`the-abandoned-interior.md:183`, 'do NOT pick a side'). The wall-fork H3 is now **MERGED (PR #260, verdict B3 DEGENERATE)** — magnetic-vs-capacitive is a degenerate chirality-set sign/spin selector, NOT a sector branch; the earlier 'magnetic PRIMARY asserted-not-derived' is **superseded by the degeneracy ruling**. The B3-degenerate verdict makes chirality→spin-sign MORE open (the magnetic-primary prop that might have grounded it collapsed), so keep it as an open-seam POINTER to def-7c3f9e / PR#260, not a definitional identity here.
    - conflicting sites: TKI dictionary `translation-circuit.md:17-26,41` (clm-fy05jc); soliton-structure transformer `translation-circuit.md:544-554` (§9.2 'Ideal transformer' sub-block); resonator $H(s)$ `cvr-transfer-function.md:23-47`; chiral-piezo Class-B reframe `translation-circuit.md:643-660` §11; chirality→spin open seam `def-7c3f9e` + PR#260 (MERGED, B3 DEGENERATE).
- **verification:** *(to be completed by auditor/Grant at ratify-time)* the dictionary reading is grounded (`translation-circuit.md:41` 'identity statements, not approximations, not analogies'; `vol5/claim-quality.md:19` the $L/C$ bridges are 'definitional dimensional bridges, convert units not predictions'); the contrast object ($H(s)$ = the dynamics) is canonical (`cvr-transfer-function.md:23-47`). The 'lossless/gain-1/pole-less transformer' framing is a NEW coinage (0 prior hits) — must NOT seed SOLID; the chiral-piezo transducer half inherits the Class-B 'NOT a derivation' ceiling (`translation-circuit.md:646,660`).

---

## SubstrateExcitation *(proposed)*
<!-- id: def-7a3f1c -->

- **term:** SubstrateExcitation
- **adjudicated-meaning:** *(PROPOSED, gated)* the **class** (base of a class-tree) of any localized excitation of the $\mathcal{M}_A$ substrate — the class-invariant FORMS (the resonator pole shape $s_\pm=-\omega_0/(2Q)\pm j\omega_d$, the root-locus, the Axiom-4 kernel $S(A)$, the $\Gamma_{spinor}=-1$ wall) that carry NO instance operating point. Concrete instances supply their own geometry / $(p,q)$ / mass / $L/C$ / $\omega_0$ / $Q$.
- **axis:** other (class label / type, not a glyph on a physical axis)
- **dimension/type:** class (n/a — a type, not a quantity)
- **status:** proposed
- **canonical-home:** *(none — coinage; field-def electron pilot 2026-06-14, engine class in `src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`)*
- **clm-cross-links:** clm-fd1e7a (the electron field-bundle instance-1 it abstracts)
- **canon-noun map:** abstracts the family whose electron member is the **unknot dilatation-mass / Mass-Dilatation Resonator / Resonant LC Tank / $0_1$ unknot + $(2,3)$ winding**. The label is a non-canon ENGINEERING class name; it MUST map to those canon nouns and must NOT drift into a noun-swap. ("vortex ring" / "lossless pivot" stay research-only.)
- **open-ambiguity-flag:** no (a fresh coinage carries no prior overloading)
- **verification:** VERIFIED **0 prior corpus hits** for `SubstrateExcitation` (clean to coin; only this pilot's new engine code uses it). **GATED on auditor + Grant review — NOT adopted, NOT SOLID.**

---

## BoundResonator *(proposed)*
<!-- id: def-b42e9d -->

- **term:** BoundResonator
- **adjudicated-meaning:** *(PROPOSED, gated)* the **bound sub-class** of `SubstrateExcitation` (def-7a3f1c) — a closed, high-$Q$, TIR-confined LC cavity whose poles ride toward (never cross) the $j\omega$ axis as $Q\to1/\alpha$. The **electron is instance-1**. Distinguished by the cavity-class discriminator (ave-cavity-class-identification) from an *OpenCosseratScrew* (a radiating longitudinal Cosserat shear mode, $\oint\neq0$), which the electron is NOT.
- **axis:** other (class label / type)
- **dimension/type:** class (n/a — a type); its instance carries $Q$ [dimensionless], $L$ [H], $C$ [F], $\omega_0$ [T⁻¹]
- **status:** proposed
- **canonical-home:** *(none — coinage; field-def electron pilot 2026-06-14, engine class in `src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`)*
- **clm-cross-links:** clm-fd1e7a (the electron R/X/Q/L/C bundle = instance-1), clm-rtdmsn ($Q_e=1/\alpha$), clm-kezk9z (the LC-tank / $\Gamma=-1$ wall)
- **canon-noun map:** the electron instance = **unknot dilatation-mass / Mass-Dilatation Resonator / Resonant LC Tank / $0_1$ unknot + $(2,3)$ winding**. Non-canon engineering class name; maps to those canon nouns, no noun-swap.
- **open-ambiguity-flag:** no (a fresh coinage carries no prior overloading). *(Distinct caveat — NOT an open-ambiguity of THIS term:* the two $\Gamma$'s the electron carries, $\Gamma_{spinor}=-1$ [class-invariant wall, ALL fermions] vs $|\Gamma_{EM}|^2=1-\alpha$ [electron-scoped EM leak], are a separate homonym surfaced for adjudication at clm-fd1e7a / [cvr-reflection-smith.md](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md):36 — do not conflate them.)
- **verification:** VERIFIED **0 prior corpus hits** for `BoundResonator` (clean to coin; only this pilot's new engine code uses it). **GATED on auditor + Grant review — NOT adopted, NOT SOLID.**



---

## K4
<!-- id: def-4b1a2c -->

- **term:** K4 (the "K4" name — three distinct overloaded referents)
- **adjudicated-meaning:** *(no single locked sense — the overload IS the content: one name spans three distinct objects across the corpus, and the production engine does NOT use the object the Axiom-1 name denotes)*. The unadjudicated name-overload is itself the open item; the P0 walk-back of the "Laves K4" name is queued.
- **axis:** other (cross-file name overload spanning a real-space crystal name and a group label)
- **dimension/type:** n/a (a name) — its referents are: a graph/lattice (length-scale $\ell_{node}$), and a finite group (dimensionless)
- **status:** ambiguous
- **canonical-home:** *(no single home — the name-identity is adjudicated by the D1 memo and restated in-axiom at `manuscript/common_equations/eq_axiom_1.tex:35`; the name-overload is flagged unresolved at `the-abandoned-interior.md:183`)*
- **clm-cross-links:** *(none verified-specific yet)*
- **open-ambiguity-flag:** YES — three distinct referents share the name "K4":
  - (a) the **axiom NAME "chiral Laves K4"** — the degree-3 srs / Sunada-K4 net, $I4_1 32$ chiral space group (the historical object Sunada called K4). Home: `manuscript/common_equations/eq_axiom_1.tex:23-24` (the "chiral Laves K4 Cosserat crystal" identity) + `:18-21` (D1 adjudication tying the name to srs); the srs builder at `src/ave/core/chiral_lattice.py:11-13,199-217`. [structural-chirality instrument]
  - (b) the **engine "K4"** — the degree-4 (z=4) bipartite-FCC **DIAMOND** lattice (achiral $Fd\bar{3}m$), on which the production $\alpha$ / Lorentz / photon drivers compute. Home: `src/ave/core/k4_tlm.py:101-119` (`K4Lattice3D`, the `# K4 (DIAMOND) LATTICE` banner at `:97`); the in-axiom split at `eq_axiom_1.tex:35` ("The production computational net is z=4 diamond"). [production engine substrate]
  - (c) the **rotation GROUP $K4 \to A_4$** — the tetrahedral-group chain used in the spin-1/2 derivation. Home: `finkelstein-misner-spin-half-derivation.md:52,56` (the $K_4 \to A_4 \to 2T \subset SU(2)$ chain); `vol2/.../ch01-topological-matter/electron-identification.md:52`. [finite group, dimensionless]
  - **The load-bearing tension:** the **axiom NAME (a) denotes the chiral srs net, but the PRODUCTION engine runs the achiral diamond (b)** — a structural-vs-named mismatch. Per the D1 memo (2026-06-12, `research/2026-06-12_lattice-d1-adjudication-memo.md:44`) the engine + axiom AGREE on diamond for production; the residual mismatch is the retained name "Laves K4" itself. The **P0 walk-back of the name is queued** (provenance comment `manuscript/common_equations/eq_axiom_1.tex:20`, D1-adjudication block), and the broader crystalline-vs-amorphous structural tension is flagged a "real open seam" at `the-abandoned-interior.md:183` (auditor lane + Grant adjudicate). The D1 memo's framing default (B) (srs = instrument, diamond = engine) is PROVISIONAL; the (A) substrate-challenge axis remains live.
    - conflicting sites: axiom name / srs `eq_axiom_1.tex:23-24,18-21`; engine diamond `src/ave/core/k4_tlm.py:97-119`; group $K4\to A_4$ `finkelstein-misner-spin-half-derivation.md:52,56`; name-overload open seam `the-abandoned-interior.md:183`; P0 walk-back queued `eq_axiom_1.tex:20`.
- **verification:** VERIFIED the three referents at their cited sites (axiom name + srs builder, diamond `K4Lattice3D`, the $K4\to A_4$ chain). Status **ambiguous** — the name-overload is unadjudicated (P0 walk-back queued, not yet applied); the production engine demonstrably runs object (b) while the Axiom-1 name denotes object (a). Recorded as a seam, not resolved — do not pick a referent for an un-qualified "K4".

---

## chirality
<!-- id: def-7c3f9e -->

- **term:** chirality (chiral / handedness)
- **adjudicated-meaning:** *(no single locked sense — two distinct realizations the corpus is emphatic NOT to conflate; whether the production realization is GENUINELY a chiral space group is OPEN)*.
- **axis:** other — split across a dimensionless dynamical order-parameter and a real-space crystallographic motif
- **dimension/type:** dimensionless (the $\kappa_{chiral}$ scalar) for the dynamical reading; n/a / space-group label ($I4_1 32$ vs $I4_3 32$) for the geometric reading
- **status:** ambiguous
- **canonical-home:** *(no single home — the production-vs-instrument split is stated at `manuscript/common_equations/eq_axiom_1.tex:35`; the broader realization question is flagged OPEN at `the-abandoned-interior.md:183`)*
- **clm-cross-links:** *(none verified-specific yet)*
- **open-ambiguity-flag:** YES — two distinct chirality realizations:
  - (a) **DYNAMICAL chirality**: an excited $k_\chi$ Cosserat order-parameter realized as the scalar $\kappa_{chiral} = \alpha\,\tilde{\kappa}(p,q)$ on the **ACHIRAL $Fd\bar{3}m$ diamond** (the production engine), asymmetrically loading $\mu$-up / $\varepsilon$-down by local helicity. Home: `eq_axiom_1.tex:35` ("Cold-lattice handedness on diamond is an excited $k_\chi$ Cosserat order-parameter"); `src/ave/topological/cosserat_field_3d.py:115-124` ($\kappa_{chiral}=\alpha\cdot\tilde\kappa$), `:522-523` (asymmetric loading); the diamond port-handedness at `src/ave/core/k4_tlm.py:535-548` (`get_helicity_density`). The strength inherits the $\alpha$ calibration. [dynamical order-parameter, dimensionless]
  - (b) **GEOMETRIC / STRUCTURAL chirality**: the literal $I4_1 32$ Wyckoff-8a srs atomic motif (right-handed = $I4_1 32$, left-mirror = $I4_3 32$) — the **INSTRUMENT** path, not the substrate. Home: `src/ave/core/chiral_lattice.py:45-46,215`. [crystallographic space-group motif]
  - **The OPEN question (do NOT pick a side):** whether the port-handed bipartite **achiral diamond** (a) genuinely **realizes Axiom-1's CHIRAL $I4_1 32$ space group**, or is an achiral diamond carrying a dynamical port-handedness, is **NOT settled in any code read**. The corpus closes the NARROWER chiral-vs-centrosymmetric space-group question as a FALSE POSITIVE ($Fd\bar{3}m$ is the supergroup of $I4_1 32$; $k_\chi=0 \Rightarrow Fd\bar{3}m$, $k_\chi>0 \Rightarrow I4_1 32$ — `claim-quality-closure-roadmap.md:191`, Foundation Item 10; corroborated `manuscript/ave-kb/common/translation-tables/translation-circuit.md:652`), but the BROADER crystalline-vs-amorphous structural model doing the isotropy work is "**not unified**" and named a "**real open seam**" at `the-abandoned-interior.md:183` (auditor lane + Grant adjudicate).
    - conflicting sites: dynamical $\kappa_{chiral}$ on achiral diamond `eq_axiom_1.tex:35` + `src/ave/topological/cosserat_field_3d.py:115-124,522-523`; geometric $I4_1 32$ srs motif `src/ave/core/chiral_lattice.py:45-46,215`; supergroup FALSE-POSITIVE close `claim-quality-closure-roadmap.md:191` (corroborated `manuscript/ave-kb/common/translation-tables/translation-circuit.md:652`); broader open seam `the-abandoned-interior.md:183`.
- **verification:** VERIFIED both realizations verbatim at their cited sites; VERIFIED that "chirality / chiral / handedness / enantiomorph" carried **ZERO prior def-node** (the load-bearing vocabulary gap, confirmed by grep of this register). Status **ambiguous** — the production-vs-instrument split is real and corpus-documented, but whether the achiral diamond genuinely realizes a chiral space group is unadjudicated. Recorded as a seam, not resolved.

---

## c
<!-- id: def-2e8d61 -->

- **term:** c (the substrate wave speed(s))
- **adjudicated-meaning:** *(no single number — distinct substrate-native speeds share the symbol $c$, and the cold-lattice value enters as a CALIBRATION IDENTITY ($G_{vac} \equiv \rho_{bulk}\,c^2$), NOT a grid-derived output)*. Conflating the speeds is the canonical Pitfall #5 framework-leakage error.
- **axis:** other — distinct effective speeds (all $L\,T^{-1}$), separated by operating-point dependence and by mode
- **dimension/type:** velocity ($L\,T^{-1}$); the listed forms are distinct quantities, not interchangeable
- **status:** ambiguous
- **canonical-home:** *(no single home — Pitfall #5 / two-effective-speeds discipline at `manuscript/ave-kb/CLAUDE.md`; mode speeds at `vol1/dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md:38`)*
- **clm-cross-links:** clm-8nkvwy
- **open-ambiguity-flag:** YES — the symbol $c$ spans multiple distinct substrate speeds, and the photon's propagation ontology is itself OPEN:
  - (a) $c_{EM}(A_0) = c_0/S(A_0)$ — the **Maxwell phase velocity** that enters $\alpha = e^2/(4\pi\varepsilon_0\hbar c)$ (canonical clm-8nkvwy:111).
  - (b) $c_{shear}(A_0) = c_0\sqrt{S(A_0)}$ — the **substrate mechanical / group / rest-mass speed** that tracks the Schwarzschild reduction (canonical clm-8nkvwy:113). Substituting $c_{shear}$ into the $\alpha$ formula is the documented Phase 3-A3 walk-back error — use $c_{EM}$ in $\alpha$, $c_{shear}$ in time-dilation.
  - (c) the K4 **$A_1$ bulk-modulus port-mode** $\sqrt{K_{bulk}/\rho} = \sqrt{2}\,c$ (pure-dilatation; measured cardinal-axis $v/c \approx 1.45$). The $\sqrt{2}$ mode-ratio $v_{A_1}/v_{T_2} = \sqrt{K/G} = \sqrt{2}$ holds at $K=2G$; the cardinal-axis $\sqrt{2}$ is **also** a port-step-vs-Euclidean lattice-projection convention ($dt=dx/(c\sqrt{2})$), distinct from a physical anisotropy. Home: `vol1/dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md:38`; `src/ave/core/k4_tlm.py:181-189`.
  - (d) the isotropic-solid **longitudinal P-wave** $c_L = \sqrt{(K+\tfrac{4}{3}G)/\rho} = \sqrt{10/3}\,c \approx 1.83c$ at $K=2G$ ($\nu=2/7$). This is DISTINCT from the $\sqrt{2}\,c$ bulk-modulus dilatational speed (which drops the $4G/3$ shear term) — the 2026-06-08 c_L reconciliation (Rule 12). Home: `vol1/dynamics/index.md:28`; `vol1/dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md:38`.
  - **CALIBRATION IDENTITY:** the cold-lattice $c$ enters as $G_{vac} \equiv \rho_{bulk}\,c^2$ (from $v_{transverse}=\sqrt{G/\rho}=c$), a definitional identity NOT independently grid-derived. Home: `src/ave/core/constants.py:670-672` ($G\_VAC = RHO\_BULK \cdot C\_0^2$).
  - **FLAG — OPEN (do NOT pre-judge):** the **continuum-vs-discrete photon ontology (DEC-01 / #248)** is **unadjudicated** — whether light is a continuous transverse-energy mode (Branch C) that the discrete substrate merely *samples* (imprinting the $\sqrt{2}$ as an observation fingerprint) vs literal discrete transport is an OPEN ruling. The $\sqrt{2}c$ front's mode-identity (bulk-precursor vs T₂-photon group velocity) is empirically unisolated. Home: `_orchestration/2026-06-14_photon-ontology-vocabulary-adjudication-handoff.md:41,50` ("needs your ruling" / "OPEN").
    - conflicting sites: $c_{EM}$ vs $c_{shear}$ clm-8nkvwy:111,113 + `manuscript/ave-kb/CLAUDE.md` (Pitfall #5); $\sqrt{2}c$ bulk mode + lattice-projection `photon-propagation-baseline.md:38` + `src/ave/core/k4_tlm.py:181-189`; $\sqrt{10/3}c$ P-wave `vol1/dynamics/index.md:28`; calibration identity `src/ave/core/constants.py:670-672`; DEC-01 OPEN `_orchestration/2026-06-14_photon-ontology-vocabulary-adjudication-handoff.md:41,50`.
- **verification:** VERIFIED the speed-set and the $G_{vac}=\rho c^2$ calibration identity at their cited sites; VERIFIED the $\sqrt{10/3}c$-vs-$\sqrt{2}c$ distinction (2026-06-08 c_L reconciliation, Rule 12) at `vol1/dynamics/index.md:28`. Status **ambiguous** — multiple distinct speeds under one symbol, cold-value is a calibration identity, and the photon ontology (DEC-01) is OPEN and explicitly NOT pre-judged here.

---

## longitudinal
<!-- id: def-9a4f07 -->

- **term:** longitudinal (the V-sector scalar grade)
- **adjudicated-meaning:** the **real V-sector scalar grade** — the Heaviside/Gibbs-excised longitudinal compression scalar that is **physical, NOT Gauss-deleted**. It is "the 3" in its A1 dilatation-MASS sense (the Heaviside-demoted scalar/longitudinal grade that re-engages at saturation = the electron). It must **never** be framed in QED-vector terms.
- **axis:** other — the longitudinal scalar V grade (a substrate field grade, not a transverse-vector component)
- **dimension/type:** scalar potential grade $V$ (the A1 dilatation channel); dimensionless winding for the orthogonal Cosserat sense (see open-ambiguity)
- **status:** ambiguous
- **canonical-home:** `vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:18` (the Maxwell–Heaviside note: the scalar/longitudinal grade demoted by Heaviside–Gibbs, "re-engages at saturation = the electron")
- **clm-cross-links:** *(none verified-specific yet)*
- **open-ambiguity-flag:** YES — "longitudinal" is overloaded (the field-symbol registry locks four readings); the load-bearing distinction is:
  - (a) the **bulk-volumetric / V-sector scalar** longitudinal grade — the Heaviside-excised compression scalar, the **A1 dilatation-mass "3"** (`master-equation.md:18,20`). This is the real, physical, Gauss-undeleted grade. [scalar V grade]
  - (b) **shear-in-the-longitudinal-direction** — the Cosserat longitudinal-shear sense (the substrate-mechanical $\tau_{zx}$ family used in the dark-wake / thrust arc), a genuine Maxwell/Cauchy shear stress. [stress, $N\,m^{-2}$]
  - (c) the **EM-forbidden** longitudinal photon (transverse-only EM mode) — the sense in which the photon has no longitudinal component.
  - (d) the **port / lattice** $A_1$ longitudinal port-mode ($\sqrt{2}c$ bulk-modulus dilatation; see `def-2e8d61` c).
  - **Load-bearing guard:** the A1 longitudinal scalar (a) is the **dilatation-mass "3"** and is ORTHOGONAL to the Cosserat $(2,3)$ micro-rotation winding (charge); never frame (a) in QED-vector terms, and never wire the winding into the breather's $(V_{inc},V_{ref})$ phasor (`master-equation.md:20`; see `def-1f6e34` the-3).
    - conflicting sites: Heaviside-excised scalar grade `master-equation.md:18,20`; the four-way registry lock `research/2026-06-10_field-symbol-registry.md` (Rule 3, not-canon draft) + `_orchestration/2026-06-14_photon-ontology-vocabulary-adjudication-handoff.md:92`; longitudinal-shear $\tau_{zx}$ `common/dark-back-reaction-taxonomy.md:25`.
- **verification:** VERIFIED the V-sector / Heaviside-excised scalar reading at `master-equation.md:18,20` (the scalar/longitudinal grade demoted by Heaviside–Gibbs, physical, re-engages at saturation). The four-way overload is documented in the not-canon field-symbol registry (no prior def-node) per the handoff table `:92`. Status **ambiguous** — multiple readings under one word; the V-sector scalar sense is the canonical primary but the surface form is overloaded and was unregistered until now.

---

## the-3
<!-- id: def-5d2b8a -->

- **term:** the-3 (the two homonymous "3"s)
- **adjudicated-meaning:** *(the disambiguation IS the content — Rule-12 ratified at `master-equation.md:20`)*: the "3" names **TWO DISTINCT, ORTHOGONAL objects (A1 $\perp$ T2)**: the **A1 dilatation MASS** (the Heaviside-excised longitudinal compression scalar $V$; $m_e c^2$ = trapped acoustic compression energy) vs the **Cosserat micro-rotation $(2,3)$ WINDING** (the Axiom-1 intrinsic-spin DOF; charge = Beltrami helicity $H_{bel}=\int\omega\cdot(\nabla\times\omega)$). The electron is the unknot dilatation-mass **carrying** the $(2,3)$ winding — two objects, not one.
- **axis:** other — A1 scalar V grade (mass) vs phase-carrier $(2,3)$ Cosserat winding (charge), declared orthogonal
- **dimension/type:** scalar V grade / energy ($m_e c^2$) for the A1 mass "3"; integer winding pair $(2,3)$ / dimensionless helicity for the Cosserat charge "3"
- **status:** ambiguous
- **canonical-home:** `vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20` (the Rule-12, Grant-ratified TWO-"3"s disambiguation box — the canonical anchor)
- **clm-cross-links:** *(none verified-specific yet)*
- **open-ambiguity-flag:** YES — two distinct objects under the one numeral "3":
  - (a) the **A1 dilatation-MASS "3"** — the Heaviside-excised longitudinal compression scalar $V$ (the A1 breather; $m_e c^2$ = trapped acoustic compression energy). The longitudinal grade of `def-9a4f07`. [scalar V grade]
  - (b) the **Cosserat micro-rotation $(2,3)$ WINDING "3"** — the T2 couple-stress, Axiom-1 intrinsic-spin DOF; charge = Beltrami helicity $H_{bel}=\int\omega\cdot(\nabla\times\omega)$. [phase-carrier winding / dimensionless helicity]
  - **Load-bearing FORBIDDEN-wiring guard (Rule 12, Grant-ratified):** the two are ORTHOGONAL (A1 $\perp$ T2); **never wire the winding (b) into the breather's own phasor $(V_{inc},V_{ref})$** — $V_{ref}$ is a read-only projection of the same scalar $V$, not an independent DOF; doing so self-inflicts the genesis-24 / crystal $w_{pol}=0$ double-count. The TWO-objects disambiguation is canon (the `master-equation.md:20` Rule-12 box) but carried **no def-node** until now. (The `status: ambiguous` tag refers to the surface numeral "3" itself, which remains overloaded across two objects — NOT to the disambiguation, which is settled.)
    - conflicting sites: the canonical disambiguation box `master-equation.md:20` (A1 dilatation-mass scalar vs Cosserat $(2,3)$ winding, "never wire the winding into the breather's own phasor"); A1 scalar $V$ engine `src/ave/core/master_equation_fdtd.py:42-47`; Cosserat winding / helicity readout `src/ave/topological/cosserat_field_3d.py:2122` + `src/ave/topological/helicity_observer.py:39-59`.
- **verification:** VERIFIED the two-orthogonal-objects content and the forbidden-wiring guard verbatim at `master-equation.md:20` (Rule 12, Grant-ratified). Status **ambiguous** — the disambiguation is settled in canon, but the surface numeral "3" remains overloaded across two objects (it is the *overload*, not the *meaning*, that the ambiguous tag flags) and the wiring-guard must be qualified at every cite; recorded so the verifier-gated watch-list can catch its mis-use. Do not collapse the A1 "3" and the Cosserat "3" into one object.

---

## dark-wake
<!-- id: def-1f6e34 -->

- **term:** dark-wake (dark wake)
- **adjudicated-meaning:** *(a vocabulary collision the corpus has split under a shared genus — `common/dark-back-reaction-taxonomy.md`)*: the name "dark wake" historically named TWO physically distinct substrate back-reaction phenomena (written with one shared $\tau_{zx}$ symbol on a longitudinal-shear signature resemblance); the canonical taxonomy now reserves "dark wake" for the **thrust species only** and renames the other.
- **axis:** other — a far-field radiated shear-stress phenomenon vs a near-field reactive self-energy rate
- **dimension/type:** shear stress ($N\,m^{-2}$) for the thrust species ($\tau^{far}_{zx}$); reactive power per time ($V^2/\text{time}$) for the dark-resonance species ($-\dot\Sigma_{near}$)
- **status:** ambiguous
- **canonical-home:** `common/dark-back-reaction-taxonomy.md:21` (Species 1 — dark wake / thrust / $\tau^{far}_{zx}$)
- **clm-cross-links:** clm-7tynm2, clm-v2sg8z
- **open-ambiguity-flag:** YES — the name historically spanned two distinct objects (a symbol-level category error, forced by the 2026-05-31 FT-Dark-Wake-Cross-Scale Outcome C):
  - (a) **dark wake (thrust) → $\tau^{far}_{zx}$** — the **far-field radiated longitudinal-shear stress**, the real-space motion-trail behind a *moving* soliton (no motion, no wake), carrying the Newton-3rd reaction momentum ($P_{wake}=F\cdot c_0$). A genuine Maxwell/Cauchy shear stress. Home: `common/dark-back-reaction-taxonomy.md:21-27`; canonical leaf `vol4/circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md` (clm-7tynm2). [stress, $N\,m^{-2}$]
  - (b) **dark resonance (g-2) → $\Sigma_{near}$ / $-\dot\Sigma_{near}$** — the electron's **near-field reactive self-energy** (at rest, in the Cosserat $(2,3)$ phase space), the QED self-energy analogue feeding $A_2$. Previously mislabeled "dark wake" with $\tau_{zx}$. Home: `common/dark-back-reaction-taxonomy.md:29-37`; canonical leaf `vol2/.../ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md` (clm-v2sg8z). [reactive power rate, $V^2/\text{time}$]
  - **AMO-overlap guard:** "dark resonance" (b) is ALSO an established atomic-physics term (CPT / EIT dark state) — a DIFFERENT phenomenon; qualify as "AVE dark resonance (substrate self-$\Gamma$)" when precision is needed (`dark-back-reaction-taxonomy.md:39`).
  - **Cross-repo status (peripheral to AVE-Core canon):** the dark-wake thrust species (a) is the subject of an exploratory **AVE-Propulsion** arc (chiral plasma antenna radiating longitudinal Cosserat shear), where the corpus self-flagged a separate "dark-wave" coordinate-sense mis-definition (one of the handoff's catalogued vocabulary errors). Within AVE-Core the term is a settled definitional taxonomy (a no-claim leaf), though the surface form "dark wake" remains overloaded (see status note); the singular "dark wave" has **0 corpus hits**. Cross-repo: `AVE-Propulsion/manuscript/vol_propulsion/chapters/01_ave_resolutions.tex`. The vocabulary-debt classification of "dark wake" is surface-level + producer-mis-premise per `_orchestration/2026-06-14_photon-ontology-vocabulary-adjudication-handoff.md:94`.
    - conflicting sites: thrust species $\tau^{far}_{zx}$ `dark-back-reaction-taxonomy.md:21-27`; dark-resonance species $\Sigma_{near}$ `dark-back-reaction-taxonomy.md:29-37`; AMO overlap `dark-back-reaction-taxonomy.md:39`; cross-repo arc `AVE-Propulsion/manuscript/vol_propulsion/chapters/01_ave_resolutions.tex`.
- **verification:** VERIFIED the genus/species split, both symbols, both canonical-home leaves, and the AMO-overlap guard at `common/dark-back-reaction-taxonomy.md:11,21-39`; VERIFIED the cross-repo AVE-Propulsion footprint by grep. Status **ambiguous** — the taxonomy split is settled in canon, but the surface form "dark wake" historically collided two objects and the AMO "dark resonance" sense further overloads the renamed species (it is the *surface overload* the ambiguous tag flags, not the taxonomy); recorded so the watch-list catches the mis-use. The split is the content, not resolved here.

---

## Seed coverage + follow-up

**Seeded (14):** 1 SOLID (`node`), 8 ambiguous (`carrier`, `Nyquist`,
`phase-space`, `size`, `radius`, `r_opt`, `Compton`, `winding`), 5 proposed
(`κ_share`, `r_env`, `node-Nyquist-size-boundary`, `SubstrateExcitation`,
`BoundResonator`).

**Over-read guards applied (verify-before-cite):** two §47 paraphrases did NOT
survive re-grep and are recorded as corrections rather than seeded as fact —
(1) the `winding`-leaks-to-size claim cited to `torus-knot-ladder.md:21` (that
line states the opposite: r_opt is "dimensionless … NOT a length"); (2) the
§46/§47 line-number for the proton 0.84 fm "RMS vibration" cite (the live site is
`src/ave/core/constants.py:967-971`, not :957-960). Surfaced flag-don't-fix.

**Follow-up (tracked):** (a) Stage 2 — **LANDED 2026-06-08**: `refresh-kb-metadata`
materializes `node_type: "definition"` records into `claims.jsonl` and
`verify-kb-metadata` drift-gates `clm_cross_links` referential integrity (per the
[`.index/SCHEMA.md`](../.index/SCHEMA.md) "Stage-2 materialization rule" +
INVARIANT-S12). (b) Add the remaining §47 clarity-risk terms beyond this core
set as each is individually verified. (c) Grant adjudication of the 3 `proposed`
coinages and the §45 A-vs-B canonical fork before any `proposed` → `SOLID`
promotion.

