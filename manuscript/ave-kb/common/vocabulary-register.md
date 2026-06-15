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

