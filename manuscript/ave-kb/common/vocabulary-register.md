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
- **ontology-grade** *(Grant-ratified convention 2026-07-21; see the convention block below)* — for a **substrate-noun** `def-` node, the noun's ontological status under phase-only epistemology, one of the four values **IDENTITY** / **MODEL-OF** / **ANALOGY** / **IMPORT**. Optional and absent on the legacy clarity-risk / notation entries; present on every substrate-noun ontology node minted 2026-07-21 onward. This field is **not** parsed or materialized (INVARIANT-S12's five required fields are `term` / `adjudicated-meaning` / `axis` / `dimension/type` / `status`; the emitter ignores any additional bullet), so it is a human-facing register commitment, not a drift-gated one.

---

### The ontology-grade convention (`def-` substrate nouns) — Grant-ratified 2026-07-21

**Adjudication basis** (Grant, verbatim `[sic]`): *"i oike the plan lets fire that lane, 1) agree its an identity not literal, 2) lets walk, 3) yup makes sense"*. Under the framework's **phase-only epistemology** (no direct observable of the substrate; the bulk self-cancels — `form-deriving-value-importing.md`:255,:265, `identity-break-test-design.md`:110-111), a substrate **noun** is a **structure commitment**, and "is" only cashes out at the *structure* level — there is no accessible substance the structure is "made of", and asking for one regresses. The `ontology-grade` field records **which** level of commitment a substrate noun carries, on a four-value scale:

- **IDENTITY** *(structure-commitment — the only level where "is" means anything under phase-only epistemology; NOT a substance/material claim)* — the noun commits **exactly** the structural / constitutive relations (connectivity, DOF grades, constitutive couplings) and nothing about a material the structure is made of. An IDENTITY grade does **not** blanket-license imports keyed on the surface word: each import (e.g. a materials-science property borrowed because the substrate is "a crystal") runs the per-import means-test individually (`substrate-native-terminology.md` §"the leak-check"; the law-vs-texture program's operating assumption).
- **MODEL-OF** *(exact isomorphic description, carrying the isomorphism's own status + regime scope)* — the noun names a description that is an **exact isomorphic image** of the structure within a stated regime (e.g. the long-wave / `ωτ≪1` limit), carrying the isomorphism's own adjudication status and its regime of validity. Outside that regime the model and the structure book their content differently and are no longer co-equal.
- **ANALOGY** *(means-tested correspondence, regime-scoped, per the hub-and-spoke discipline)* — a correspondence that is means-tested and regime-scoped (the `ave-cross-discipline-mapping` hub-and-spoke rule: map disciplines to the substrate hub, never discipline-to-discipline), NOT an identity; it is licensed only where its defining property survives the leak-check.
- **IMPORT** *(external value/structure, tagged)* — an externally-sourced value or structure carried into the framework with its provenance tagged (the `echo` / `mixed` value-provenance axis, `def-ech0v1` / `def-fmv001`).

The grade is **orthogonal to `status`**: `status` answers "is the adjudicated sense locked?"; `ontology-grade` answers "at what ontological level does this noun commit?". A noun may be `status: SOLID` **and** carry any of the four grades.

---

> **Note — the word "register" is itself overloaded (collapse-batch T16, hygiene).** This file is a **tracked-index register** (sense 1: the `def-` ledger — one of the vocabulary- / axiom- / interlock- / model- / claim-quality registers, the spine node-types). That is **distinct** from three other corpus senses: (2) the **verb** "to register / pre-register / a meter registers a signal"; (3) an **impedance / content-domain bin** — "graph register", "off-line register", "which register a mode lives in" (`research/2026-07-10_impedance-register-walks_framing.md:13,20`), an *object classification*, NOT a ledger; (4) the **linguistic / communication register** (the "ee register" vs "qft register" framing). Senses 1 and 3 co-occur in the impedance-register-walks framing note (it is a sense-3 "register walk" that cites this sense-1 `vocabulary-register` throughout). A ledger-index and an impedance-content-bin are unrelated objects sharing a word: read `X-register` compounds by context, and never parse an "off-line register" (sense 3) as a tracked index (sense 1). (Pure terminology — no fireable kill-test.)

## substrate (vacuum medium noun)
<!-- id: def-91c4e8 -->

- **term:** substrate / vacuum medium (prose noun)
- **adjudicated-meaning:** the vacuum has **no dedicated object symbol**. Retired 2026-06-18: `$\mathcal{M}_A$` (collided with boundary-observable `$\mathcal{M}$`, implied "manifold", carried stale "amorphous" subscript). Use context prose: **chiral Laves K4 Cosserat crystal** (axiom/formal), **chiral LC network** (EE/circuit), **the substrate** or **the lattice** (general/discrete).
- **axis:** notation
- **dimension/type:** n/a (noun — not a field or observable)
- **status:** SOLID (Grant adjudication 2026-06-18)
- **canonical-home:** [`CLAUDE.md`](../CLAUDE.md) INVARIANT-N1; [`eq_axiom_1.tex`](../../../manuscript/common_equations/eq_axiom_1.tex)
- **clm-cross-links:** (cross-cutting — all axiom-1 claims)
- **open-ambiguity-flag:** no
- **verification:** grep-confirmed retirement pass on canonical manuscript + KB (`analysis/substrate-noun-retirement`, 2026-06-18)

---

## condensate (substrate noun — RETIRED)
<!-- id: def-c0nd3ns -->

- **term:** condensate (as vacuum/substrate noun)
- **adjudicated-meaning:** **RETIRED 2026-06-18** for substrate ontology. Implies BEC/QFT field condensation or Volovik superfluid — contradicts Axiom 1 **chiral Laves K4 Cosserat crystal** + **LC network**. Use INVARIANT-N1 prose nouns instead.
- **axis:** notation / vocabulary
- **dimension/type:** n/a
- **status:** RETIRED (substrate sense); **KEEP** for BCS/BEC/pair-condensate (standard CM) and Meissner-*class* (bounded engine lens)
- **canonical-home:** [`CLAUDE.md`](../CLAUDE.md) INVARIANT-N1
- **clm-cross-links:** (cross-cutting)
- **open-ambiguity-flag:** no
- **verification:** grep pass 2026-06-18; ~102 substrate-noun replacements canonical manuscript + KB + selected `src/` labels

---

## node
<!-- id: def-cc2196 -->

- **term:** node
- **adjudicated-meaning:** the spatial-Nyquist sampling boundary of the substrate lattice — one Brillouin cell at the fundamental pitch $\ell_{node}$, supporting a maximum spatial frequency $k_{max} = \pi/\ell_{node}$ (the Brillouin zone edge).
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
  - **PROPOSED SHARPEN (carrier-vs-charge, epic-reroute 2026-06-24 — awaiting Grant ratification; NOT yet canonical; Rule-12: appended, nothing above edited):** the phase-space coupling-winding test (#417) surfaces a load-bearing distinction the node does not yet record — the **dynamical orbit-winding** of the coupled A1↔ω system reads the **LC oscillator carrier ratio** ($\omega_b:\omega_s$, proven by carrier-ratio detuning: $1{:}1\to0.93$, $2{:}3\to0.65$, $3{:}2\to1.54$; CI-gated at `src/tests/test_phase_space_winding.py:147-161`, $|\text{ratio}-0.667|<0.15$), which is **DISTINCT from the static topological charge-winding** ($\mathrm{Link}(\partial\Omega,F)$, def-3638f2). A topology-protected charge could not track the carrier ratio under detuning. So "carrier" (the dynamical oscillator-ratio Lissajous reading) must be kept separate from "charge" (the static deformation-invariant winding integer). Cross-link: def-3638f2 (winding STATIC/=Link/reactive), def-5d2b8a (the-3). CONSISTENCY-class. See `research/2026-06-24_engine-phase-space-winding_result.md` + `research/2026-06-24_engine-reroute-epic-summary.md`.

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
  - conflicting sites: substrate pitch $\ell_{node}$; charge radius $D_p$ `src/ave/core/constants.py:971`; tube radius $\ell_{node}/(2\pi)$; real-space envelope `src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py:77`; the dimensionless r_opt ratio `vol2/particle-physics/ch01-topological-matter/torus-knot-ladder.md:21`.
- **verification:** GAP VERIFIED — 0 hits for any canonical "soliton size" definition (3 greps empty, §45). The §45 RECOMMENDATION (canonical size = the saturation boundary $r_{body}(m)$) is a PROPOSAL gated on the unresolved §45 A-vs-B fork, NOT adopted — so "size" stays ambiguous, not SOLID. **🔴 STRUCK (fabricated citation — 2026-07-14, Wave-0 KB batch):** the former sixth conflicting site *"multi-node body envelope `manuscript/vol_2_quantum/chapters/02_baryon_sector.tex:40`"* was removed — that directory does NOT exist (real tree: `vol_2_subatomic/`) and the phrase *"multi-node body envelope"* appears nowhere in the corpus (two-method: `grep -F` + `git grep`). **Dropped, NOT repointed** (repointing to the real `vol_2_subatomic/chapters/02_baryon_sector.tex:41` "spans multiple fundamental nodes" would re-assert the supra-node body reading the §45 A-vs-B fork holds open — same rationale as the def-envl0p strike). This resolves the pre-existing `:173` site the def-envl0p verification flagged for auditor.

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
  - conflicting sites: tube radius `electron-identification.md:77` (row 2, "tube radius $\ell_{node}/(2\pi)$"); major/minor + dimensionless ratio `vol2/particle-physics/ch01-topological-matter/torus-knot-ladder.md:21`; radius-vs-cross-section dimension collision `manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex:41`.
- **verification:** VERIFIED the glyph-overloading at the three cites; the cross-section/radius dimension collision VERIFIED at `vol_2_subatomic/chapters/02_baryon_sector.tex:41` ("RMS … effective scattering cross-section" called the 0.84 fm "radius"). **🔴 PATH REPOINTED (2026-07-14, Wave-0 KB batch):** this cite formerly read `manuscript/vol_2_quantum/chapters/02_baryon_sector.tex:40` — the same fabricated `vol_2_quantum/` directory as the struck `size`-node site, but here the CONTENT is real, so REPOINTED (not struck) to the actual file `vol_2_subatomic/chapters/02_baryon_sector.tex:41` (two-method verified: the real line 41 states "The 0.84 fm radius corresponds to the Root-Mean-Square (RMS) effective scattering cross-section").

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
  - **PROPOSED SHARPEN (epic-reroute, 2026-06-24 — awaiting Grant ratification; NOT yet canonical; Rule-12: appended, nothing above edited; additive — does NOT resolve the node's pre-existing ambiguities):** the engine-reroute epic establishes the $(2,3)$ phase-space winding is **STATIC** (a deformation-invariant texture, NOT a dynamical/energetic time-orbit) and is the boundary linking integer $\mathrm{Link}(\partial\Omega, F) \in \mathbb{Z}$ (`charge_quantization.py:258`, `boundary-observables-m-q-j.md:20`). Both internal **dynamical** loci tested NEGATIVE — real-space coupled eigensolve gate-d FAIL (#415) + phase-space coupling-winding BREAK (#417): the dynamical orbit carries the **LC carrier ratio**, not the topological $(2,3)$ (carrier-ratio detuning discriminator). The winding sector is **REACTIVE / LOSSLESS** (Axiom-3: $\mathrm{Im}(\omega)=0$, $\Gamma\to-1$ confined mode, intrinsic $Q\to\infty$ — `resonant-lc-solitons.md:100`). SUBSTRATE-NATIVE WORDING GUARD: use **reactive/lossless**; the framing "charge does no work" is a CONSISTENCY-class *consequence* (work $= \oint$ across a dissipative port $= 0$ because the sector is purely reactive, $\mathrm{Im}(\omega)=0$) — do NOT canonize the bare phrase "no work" (zero corpus hits) without that $\oint$-port definition attached. CONSISTENCY-class, NOT a chord. See `research/2026-06-24_engine-reroute-epic-summary.md`.

---

## quantization / "quantized" (integer eigenvalue-label — a TRIAD)
<!-- id: def-quant3 -->

- **term:** quantization / "quantized" / an integer "quantum number" $n$ (the corpus's self-named biggest historical confusion source)
- **adjudicated-meaning:** *(no single locked sense — the overload IS the content: the word "quantized"/"$n$" carries a **TRIAD** of three physically-distinct integer eigenvalue-labels **of the same bound electron**, read by three different machineries. The operational discriminator is that each has a **distinct invariance group / failure mode** — the corpus's own "different failure modes ⇒ different objects" criterion, not a resemblance.)*
- **axis:** notation (cross-file word overload — three integer-eigenvalue senses on three distinct substrate axes)
- **dimension/type:** integer / dimensionless (all three); three distinct invariance groups
- **status:** ambiguous
- **canonical-home:** *(no single home — three senses canonical in three leaves; see open-ambiguity-flag)*
- **clm-cross-links:** clm-oltvwy (mode-count / de Broglie standing wave), clm-hvb7q3 (winding / hollow-vortex binding), clm-0ktpcn (Nyquist floor / Golden-Torus α keystone)
- **open-ambiguity-flag:** YES — three distinct integer-label senses:
  - (1) **Mode-count integers** — the cavity-deformable **embedding** register (the atomic $n, l, m$; a phase-closure / standing-wave count). Home: `vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md` (clm-oltvwy). **Failure mode: ionization destroys them** ("ionization kills the mode, not the knot"). ★ **Smoking-gun overload:** this leaf writes the mode-counts *as* "winding" — `de-broglie-standing-wave.md:223` is a table whose 3rd column header is literally "**Winding #**" filled with the QM mode numbers $l, n_r$ (:224-226), and `:236` calls the electron a "current ring soliton … with **winding number** $n$" where $n = n_r + l + 1$ (:231) is a **mode count**, not a topological winding. [embedding / mode-count axis]
  - (2) **Winding integers** — the topologically-protected **graph** register (charge, the $(2,3)$, $\mathrm{Link}(\partial\Omega,F)\in\mathbb{Z}$; def-3638f2). Home: `vol2/particle-physics/ch01-topological-matter/hollow-vortex-binding.md:96` ("the winding integer $n$ (the $(2,3)$: $w_{\text{tor}}=2$, $|\text{Link}|=1$)"; clm-hvb7q3). **Failure mode: invariant under any smooth deformation** (survives ionization). [phase-carrier / winding axis]
  - (3) **Nyquist / lattice-sampling quantization** — the substrate resolution floor keyed on $\ell_{node}$ ($=c/\omega_0$). Home: `vol1/ch8-alpha-golden-torus.md:94` ("Ax 1 Nyquist quantizes the minimum substrate-lattice-resolvable tube diameter at $d = 1\,\ell_{node}$"); **load-bearing in the α keystone** as the forced $\Lambda_{\text{line}} = \pi\cdot d = \pi$ step (`op21-multi-mode-mode-counting.md:130`; clm-0ktpcn). **Failure mode: moves iff $\ell_{node}$ changes** — invariant under BOTH cavity-wall deformation and smooth deformation, a **third** distinct invariance group. [lattice-sampling axis]
  - **The clarity risk:** sense (1) is cavity-deformable, sense (2) is topology-protected, sense (3) is a Class-B sampling floor. Reading "current ring soliton with winding number $n$" (:236) as topologically protected (it is (1), cavity-deformable), or reading the α-keystone's Nyquist-quantized $d=1$ as a protected FORM (it is (3), a sampling floor), mis-rates the object — the second would mis-rate the keystone's solidity. Cross-link: def-3638f2 (winding STATIC/=Link/reactive), def-kn0t01 (phase-space winding portrait ≠ real-space knot).
- **verification:** VERIFIED at HEAD — the mode-count-labelled-"winding" overload at `de-broglie-standing-wave.md:223` (literal "Winding #" column header over QM mode numbers) + `:181` ("mode number $n$") + `:236` ("current ring soliton … winding number $n$"); the topological winding at `hollow-vortex-binding.md:96`; the Nyquist floor at `ch8-alpha-golden-torus.md:94` + `op21-multi-mode-mode-counting.md:130`. The three invariance groups (ionization / smooth-deformation / $\ell_{node}$-change) are the discriminator. The mode↔winding boundary is independently killed-and-banked (#417 carrier-ratio detuning + #626 tethered-pivot: the dynamical mode tracks the knob, the $(2,3)$ winding does not). Status ambiguous — three integer senses of one bound electron, no single locked sense.

---

## electron/proton knot disambiguation
<!-- id: def-kn0t01 -->

- **term:** trefoil / cinquefoil / torus knot (particle-body usage)
- **adjudicated-meaning:** Rolfsen knot names and $(2,q)$ torus-knot labels are **phase-space winding portraits** on the bond-pair LC tank (Clifford torus $\mathbb{T}^2$), **not** real-space body topologies. **Electron real-space body:** $0_1$ unknot. **Proton real-space body:** $6^3_2$ Borromean linkage. Valence electrons in orbital-topology leaves are $0_1$ unknot solitons on harmonic tracks — never real-space trefoils.
- **axis:** phase-carrier (winding portrait) vs real-space topology (body knot/link)
- **dimension/type:** topological integers / winding pairs (dimensionless)
- **status:** SOLID — canonical since 2026-05-17 body-topology resolution (`clm-unk0bd`); extended 2026-06-18 knot/fluid audit on PR #291.
- **canonical-home:** `vol1/ch8-alpha-golden-torus.md:29`; `electron-identification.md`; `eq_axiom_2.tex:27`
- **clm-cross-links:** clm-unk0bd, clm-0ktpcn, clm-8c3yhs
- **open-ambiguity-flag:** no — qualifier rule is locked: *phase-space* before any trefoil/cinquefoil/$(2,q)$ label when attached to a particle name; real-space crossings belong only to Borromean/linkage prose for baryons.
- **verification:** VERIFIED disambiguation at `ch8-alpha-golden-torus.md:29` ("trefoil lives in phase space; soliton lives in real space") and `eq_axiom_2.tex:27` (2026-06-18 knot pass).

---

## δ (delta glyph)
<!-- id: def-de17a0 -->

- **term:** δ (the "delta" glyph — three distinct overloaded senses)
- **adjudicated-meaning:** *(no single locked sense — the overload IS the content: three physically-distinct dimensionless quantities share the glyph δ across the corpus, separated by ~3 OOM in magnitude)*.
- **axis:** notation (cross-file glyph overload)
- **dimension/type:** dimensionless (all three); distinct quantities
- **status:** ambiguous
- **canonical-home:** *(no single home — three senses canonical in three leaves; see open-ambiguity-flag)*
- **clm-cross-links:** clm-009nkt (δ_strain), clm-f0jwtk (δ_AVE), clm-rd9cjm (ε₁₁ radial-strain / amplitude-A sibling — T14 word-"strain" collision)
- **open-ambiguity-flag:** YES — three distinct senses:
  - (a) **δ_strain** — the vacuum strain coefficient / cosmic-scale TCC, ≈ 2.22×10⁻⁶ = 1 − CODATA/α_cold (a *definitional residual*; FT-1 magnitude-closed, sign-only). Home: `vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md` (clm-hp7nlm); observable at `vol1/claim-quality.md:105` (clm-009nkt). [TCC / thermal axis]
  - (b) **δ_AVE** — the substrate temporal loss tangent ≡ t_sat/t_period ∈ [0,1] (Class-1 definitional). Home: `temporal-saturation-regime-classifier.md` (clm-f0jwtk). [loss-tangent / saturation-duty axis]
  - (c) **δ = arctan α ≈ 0.418°** — the EE slip angle, where tan δ = α = 1/Q (a Class-A EE identity, NOT an independent prediction). Home: `translation-tables/translation-circuit.md` §10.3:626. [loss-angle axis]
  - **The cross-file clarity risk is (a) vs (b)/(c):** δ_strain (≈ 2.2×10⁻⁶) is **~3280× SMALLER** than the loss-tangent family tan δ = α (≈ 7.3×10⁻³) — they are NOT in the same numerical range and must never be equated (there is no "δ_strain in the tan-δ range" coincidence). Within §10.3, (b) and (c) are the **SAME object** (δ_AVE = δ = arctan α, the α = 1/Q = tan δ identity) — an intentional identity, NOT a clash; do not split it.
  - **Adjacent WORD-"strain" collision (T14, collapse-batch — a DIFFERENT axis from the δ-glyph overload above):** the word "strain" itself is overloaded. Sense (a) **δ_strain** (the ε-sector α-echo residual, ≈ 2.2×10⁻⁶, dimensionless) collides *on the word "strain"* with **$\varepsilon_{11} = 7GM/(c^2 r)$** — the A1-dilatation **radial "strain"** that IS the Axiom-4 saturation **amplitude $A$** (`vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md:14`; `vol3/claim-quality.md:59`; clm-rd9cjm). Both are **dimensionless**, and — unlike the tan-δ family — $\varepsilon_{11}$ CAN reach $\sim10^{-6}$ at large $r$, so the two "strains" CAN sit in the same numerical range. This node guards δ_strain against the loss-angle family (b)/(c) but did **not** previously guard it against the amplitude-$A$/$\varepsilon_{11}$ family (the one genuinely un-guarded dimensionless collision). `q-g22-strain-convention.md` resolves the amplitude-$A$ sense into $A_{\text{geom}}$/$A_{\text{field}}$ but is silent on δ_strain. [word-"strain" axis: ε-sector α-echo residual ⊥ A1 gravitational saturation amplitude]
- **verification:** VERIFIED — δ_strain value/home at `delta-strain-cosmic-tcc.md:13` + `vol1/claim-quality.md:108`; δ_AVE ≡ t_sat/t_period at `common/claim-quality.md:1154`; δ = arctan α ≈ 0.418° at `translation-circuit.md:626`. The ~3280× gap computed from CODATA α (2.22×10⁻⁶ vs 7.297×10⁻³). Status ambiguous — cross-file glyph reuse; the §10.3 (b)=(c) is an intentional identity, not an overload.

---

## ξ (xi glyph)
<!-- id: def-095760 -->

- **term:** ξ (the "xi" glyph — one locked primary sense $\xi_{topo}$ plus a cross-file watch-list of distinct ξ-objects, separated by ~50 OOM in magnitude)
- **adjudicated-meaning:** the **default canonical sense is $\xi_{topo} \equiv e/\ell_{node} \approx 4.149\times10^{-7}$ C/m** (Axiom 2 topological transduction constant; CLAUDE.md INVARIANT-C2). The glyph ξ is overloaded across the corpus by several physically-distinct objects; this node is the canonical mis-use watch-list.
- **axis:** notation (cross-file glyph overload) — primary sense `dimensionless`-bridge has physical dimension C/m
- **dimension/type:** $\xi_{topo}$: charge-per-length (C/m); $\xi_M$, $R_H/\ell_{node}$, $\sqrt\alpha$, $\xi_{K1}$, $\xi_{K2}$: dimensionless
- **status:** SOLID (for the locked $\xi_{topo}$ sense; status and open-ambiguity are orthogonal per the §47/`node` precedent)
- **canonical-home:** $\xi_{topo}$: `vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md` (Axiom 2); `src/ave/core/constants.py:324` (`XI_TOPO`); traceability map at `common/xi-topo-traceability.md`.
- **clm-cross-links:** clm-hmiytz (ξ_topo traceability), clm-sxn6eo (zero-free-parameter chain), clm-dsb560 (G via ξ_M / Machian), ilk-gravmb (Machian-boundary-impedance interlock)
- **open-ambiguity-flag:** YES — the surface glyph ξ is overloaded by distinct objects:
  - (1) **$\xi_{topo}$** (`XI_TOPO`) — Axiom-2 transduction constant, $e/\ell_{node} \approx 4.149\times10^{-7}$ C/m. **This is the locked primary sense.** Home `constants.py:324`. Derived alias: **`XI_TOPO_SQ`** (= $\xi_{topo}^2 \approx 1.721\times10^{-13}$ C²/m², `src/scripts/vol_5_biology/spice_organic_mapper.py:57`) — the inductance/capacitance² scaling power, NOT a distinct ξ.
  - (2) **$\xi_M$** (`XI_MACHIAN`; written bare ξ at legacy sites — non-canonical, pending the deferred subscript sweep) — dimensionless Machian-hierarchy coupling $\approx 8.15\times10^{43}$, $\xi_M = 4\pi(R_H/\ell_{node})\alpha^{-2}$; sets $G = c^4/(7\xi_M T_{EM}) = \hbar c/(7\xi_M m_e^2)$. Home `constants.py:589`; canonical at `vol_3_macroscopic/chapters/01_gravity_and_yield.tex:101`.
  - (3) **$R_H/\ell_{node}$ — NOT a ξ, a factor *inside* $\xi_M$.** Cosmic cell-count $\approx 3.46\times10^{38}$. The $4\pi\alpha^{-2}\approx2.36\times10^{5}$ porous-solid-angle lift carries it up to $\xi_M$. **Never equate $R_H/\ell_{node}$ with ξ** — this is the 5.4-OOM mis-pairing the xi-symbol-cleanup PR corrected.
  - (4) **$\sqrt{\alpha} \approx 0.0854$ (`E_NATIVE_SQRT_ALPHA`, `src/ave/core/genesis_lane_a_provenance.py:35`)** — the native numeric value of the elementary charge $e$ ($e = \xi_{topo}\,\ell_{node} = \sqrt\alpha$ in natural units, canonical at `vol_9_vacuum_datasheet/chapters/11_topological_characteristics.tex:51`). **Attribute $\sqrt\alpha$ to $e$, NOT to $\xi_{topo}$** (which is C/m, not dimensionless). *(RESOLVED — xi-symbol-cleanup PR, middle path: the `genesis_lane_a_provenance.py` source now attributes $\sqrt\alpha$ to $e$ at every site — docstring, comment, const renamed `R_XI_TOPO_NATIVE`→`E_NATIVE_SQRT_ALPHA`, JSON key `xi_topo_sqrt_alpha`→`e_native_sqrt_alpha`. The 15-site corpus shorthand sweep [`_orchestration/` briefs, `claim-quality.md:644,672`, cleave-01 leaves, `divergence-test-substrate-map.md:303`] is deferred to a tracked follow-up.)*
  - (5) **$\xi_{K1} = 8/3$, $\xi_{K2} = 32$** — substrate-scale Cosserat micropolar moduli prefactors, O(1) dimensionless, $\xi_{K2}/\xi_{K1}=12$ K4-symmetry-forced. Home `common/q-g47-substrate-scale-cosserat-closure.md:58`.
  - (6) **Standard-physics ξ homonyms** (NOT AVE objects — read by external context): the correlation length ξ (statistical mechanics), the Riemann ξ-function $\xi(s)$ (analytic number theory), the Ginzburg–Landau coherence length $\xi_0$ (superconductivity). These never appear as AVE quantities; flag if one is mis-read as $\xi_{topo}$ or $\xi_M$.
  - **The dominant numerical clarity risk is (2) vs (3):** $\xi_M\approx8.15\times10^{43}$ vs the factor $R_H/\ell_{node}\approx3.46\times10^{38}$ — a ~5.4 OOM gap. The two were mis-paired (the FORMULA of $\xi_M$ printed with the MAGNITUDE of the factor) at `xi-topo-traceability.md:23` and across the cheatsheet / divergence-map / q-g47 / claim-quality leaves; corrected in the xi-symbol-cleanup PR.
- **verification:** VERIFIED — $\xi_{topo}=4.149\times10^{-7}$ C/m and $\xi_M=8.154833696927648\times10^{43}$ computed from `src/ave/core/constants.py` (`XI_TOPO`:324, `XI_MACHIAN`:589); $R_H/\ell_{node}=3.4557\times10^{38}$ from `R_HUBBLE`:694 / `L_NODE`; $4\pi\alpha^{-2}\times(R_H/\ell_{node}) = \xi_M$ to machine precision; $\sqrt\alpha=0.08542$ at `genesis_lane_a_provenance.py:35`; $\xi_{K1}=8/3$, $\xi_{K2}=32$ at `q-g47-substrate-scale-cosserat-closure.md:58`. Status SOLID for the locked $\xi_{topo}$ sense; open-ambiguity-flag records the glyph overloading (orthogonal per the SCHEMA Definition-record rule). *(Notation convention RESOLVED per Grant — xi-symbol-cleanup PR, FIX-12: **always-subscript is canonical** — write $\xi_{topo}$ / $\xi_M$, never bare ξ for an AVE quantity. The corpus-wide bare-ξ→subscript sweep is deferred to the same tracked follow-up as FIX-9.)*

---

## u₀* (frozen-formation operating-point symbol)
<!-- id: def-u0star -->

- **term:** $u_0^*$ (the substrate frozen-formation operating-point symbol; also written $u_0^\ast$)
- **adjudicated-meaning:** *(no single locked sense — the glyph carries TWO senses that sit on opposite sides of the SYM/ASYM fence, plus a rider homonym FLAG. This def-node is the **deflation** of the §b "triple-convergence": it stops the parity-meter / matched-vertex / nucleation threads cross-authenticating merely because they wear the same symbol.)*
- **axis:** notation (glyph overload — two SYM/ASYM senses + a T-even/T-odd homonym flag)
- **dimension/type:** dimensionless (operating-point ratio, $\approx 0.187$)
- **status:** ambiguous
- **canonical-home:** *(no single home — Sense A at `vol1/ch8-alpha-golden-torus.md:206`; Sense B at `common/universal-saturation-kernel-catalog.md:216` + `common/claim-quality.md:888`)*
- **clm-cross-links:** clm-48g5qf (op14 over-bracing $u_0^*$ = static-E component), clm-invmtr (parity-meter frozen-bias / transverse-channel question)
- **open-ambiguity-flag:** YES — two senses on opposite sides of the SYM/ASYM fence:
  - **Sense A — the substrate magic-angle SYM operating point** $u_0^*\approx0.187$, the point where $K(u_0^*)=2G(u_0^*)$ and $\nu=2/7$ (SYM-class per `research/2026-07-09_fast-sector-settling-boundary-conditions_walked-framing.md:155`). Its value is **asserted / back-fit** to CODATA α and G (2026-06-14 walk-back), not forward-derived; the lock $K=2G$, $\nu=2/7$ is firm but GR-imported. Home: `vol1/ch8-alpha-golden-torus.md:206` (there written "operating point"; the SYM-class label is the cross-corpus sourcing). [SYM operating-point sense]
  - **Sense B — the frozen even-order DC bias the parity meter reads** (`universal-saturation-kernel-catalog.md:216`; the leaf phrases it as an inversion-symmetry / even-order bias — "T-breaking" in the framing prose). **PENDING-GRANT:** whether this frozen bias $u_0^*$ enters the transverse channel is an open D-II calibration-bridge question (`common/claim-quality.md:888`, "whether the frozen bias $u_0^*$ enters the transverse channel … PENDING-GRANT", clm-invmtr). [T-breaking / parity-meter sense]
  - **In-corpus tension:** `vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md:91` calls the over-bracing $u_0^*$ at the K4 magic-angle "the static-E-field component," while `manuscript/ave-kb/CLAUDE.md:75` classes a static-E-only drive **ASYMMETRIC** — so the same $u_0^*$ is read SYM-class (Sense A) *and* identified with a static-E over-brace that CLAUDE.md classes ASYM-N(ε). Whether A and B are one physical object is exactly the A1↔T2 D-II calibration bridge (PENDING-GRANT); until it runs, treat as two. $u_0^*$ is otherwise UN-registered (`rg 'u₀|u_0\*|u_0\^' vocabulary-register.md` → 0 relevant; the only prior `u_0`-substring hits are `\mu_0`).
  - ★ **RIDER — the X40 HOMONYM FLAG (P6-class; a FLAG, NOT a split — Grant ruling 2026-07-11).** Beyond the SYM-vs-bias axis above, $u_0^*$ may cover **two orthogonal fossils** on an *independent* axis — the graph-theoretic Helmholtz split (cut-space ⊥ cycle-space, T-even ⊥ T-odd; orthogonal complements, cannot mix — `research/2026-07-10_rb-fossil-walk_framing.md` §3): a **strain-$u_0^*$** (cut-space, **T-even**, read by the statics windows α / G / Lamb) vs a **flux-$u_0^*$** (cycle-space, **T-odd**, readable ONLY by non-reciprocal observables). X40 returned **BOTH** components nonzero **WITHIN the ratified matched-bath model** (trapped cycle-fraction 1/10 = T-odd loop current; radiated 9/10 = T-even bond strain; the cut-space fate is itself model-dependent — KEEP-BOTH — `research/2026-07-10_x40-ring-closure-transient_result.md:328-354`). Because both projections are nonzero **only within the model** (the split is owed only if the finite cycle-fraction is model-independent), **Grant DEFERRED the register split** (rulings-docket 2026-07-11 item 8: WAIT). So this is recorded as a **FLAG on this def-node, NOT a split**: do **not** mint two $u_0^*$ def-nodes; the strain/flux distinction rides here until the model-conditionality is settled.
- **verification:** VERIFIED at HEAD — Sense A magic-angle operating point at `ch8-alpha-golden-torus.md:206` (value back-fit per the 2026-06-14 walk-back), SYM-class label at `fast-sector-settling-boundary-conditions_walked-framing.md:155`; Sense B frozen-bias at `universal-saturation-kernel-catalog.md:216` + the transverse-channel PENDING-GRANT at `common/claim-quality.md:888`; the SYM-vs-ASYM tension at `op14-cosmic-horizon-profile.md:91` vs `CLAUDE.md:75`; the X40 both-components-nonzero-within-model at `x40-ring-closure-transient_result.md:328-354`; the rb-fossil homonym flag at `rb-fossil-walk_framing.md` §3. Status ambiguous — two SYM/ASYM senses + the deferred cut/cycle homonym flag; deflates (does NOT upgrade) the §b triple-convergence.

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
- **adjudicated-meaning:** *(PROPOSED, gated)* the soliton real-space **ENVELOPE length** (HWHM / tube-radius / saturation-boundary) — the separate name for r_opt **Meaning B**, so the length sense never reuses the dimensionless-ratio glyph. **Within the three-surface anatomy (def-anat3s, [`envelope-anatomy.md`](envelope-anatomy.md)): r_env is the WALL / ropelength-floor length — surface (i), the §45 Resolution-A sub-node locus ($\ell_{node}/2\pi$ for the ground state).** (The length VALUE stays gate-measured; this node's proposed→SOLID promotion stays Grant-gated, GATE note above.)
- **axis:** spatial-Brillouin
- **dimension/type:** length (L)
- **status:** proposed
- **canonical-home:** *(none — coinage; the existing fit-param is currently named r_opt / `HORN_R`; FORM home for the surface it names = [`envelope-anatomy.md`](envelope-anatomy.md), clm-3surfa)*
- **clm-cross-links:** clm-3surfa
- **open-ambiguity-flag:** no
- **verification:** VERIFIED **0 prior exact-token `r_env` hits** (the broad pattern catches the unrelated `HORN_R` constant, but the exact token `r_env` is unused). **GATED on Grant review — NOT SOLID.**

---

## node-Nyquist-size-boundary *(proposed)*
<!-- id: def-e0cd83 -->

- **term:** node-Nyquist-size-boundary
- **adjudicated-meaning:** *(PROPOSED, gated)* the single spatial scale at which a soliton's real-space body crosses the node Nyquist boundary — distinguishing a **supra-node body envelope** from a **sub-node charge-core feature** (the §45 A-vs-B fork). **Within the three-surface anatomy (def-anat3s): this Nyquist boundary is the $\ell_{node}$ scale that SEPARATES the §45 Resolution-A sub-node wall/floor ($\ell_{node}/2\pi$) from the §45 Resolution-B supra-node surfaces (the balance shell $\approx 1.6\,\ell_{node}$, the knee) — the FORM mint names both sides as surfaces (the **knee** is a genuinely distinct supra-node surface; the **balance shell**'s distinctness-from-the-wall is **gate-(b)**, Grant Ruling 6: CONJECTURED $\equiv$ wall), so the Nyquist crossing is the FORM-level dividing line, not an either/or fork.** (The value-side §45 resolution stays gate-(b).)
- **axis:** spatial-Brillouin
- **dimension/type:** length (L) $= \ell_{node}$
- **status:** proposed
- **canonical-home:** *(none — coinage; §46 node-Nyquist size resolution; FORM context = [`envelope-anatomy.md`](envelope-anatomy.md), clm-3surfa)*
- **clm-cross-links:** clm-yc7fgm (the node = spatial-Nyquist boundary claim it builds on); clm-3surfa (the anatomy whose Resolution-A/B surfaces this boundary separates)
- **open-ambiguity-flag:** no
- **verification:** VERIFIED **0 prior corpus hits**. **GATED on Grant review AND on the unresolved §45 A-vs-B canonical FORK** (sub-node charge-core vs supra-node body envelope) — NOT SOLID.

---

## envelope (three-surface anatomy)
<!-- id: def-anat3s -->

- **term:** envelope (three-surface anatomy: wall / balance shell / knee)
- **adjudicated-meaning:** *(FORM minted per Grant Ruling 8 option C, 2026-07-14 — the FORM is ruled; every numerical value is gate-measured, NOT SOLID)* a bound soliton's boundary region is **THREE physically-distinct radial surfaces** on $S(A(r))$: **(i) the wall** (fully-yielded $S\to0$, $\lvert\Gamma\rvert=1$ mirror; carries $\mathcal{M},\mathcal{Q},\mathcal{J}$; ground-state floor $\ell_{node}/2\pi$; sign = the ruled-degenerate selector #260); **(ii) the balance shell** (the $\sigma$-opposite-equal crossing, $\approx 1.6\,\ell_{node}$; CONJECTURED $\equiv$ wall per Ruling 6); **(iii) the knee / dress edge** (the $\Delta S=\alpha$ proportional limit, $A^2=2\alpha$). **CONFIRMED primary sense of "envelope" = the wall** (Grant confirmed in-chat 2026-07-15; the **balance shell** and **knee / dress edge** keep their own names). Ruling record: the post-merge auditor PR + the 2026-07-15 docket continuation (`_orchestration/2026-07-10_rulings-docket.md`). *(The VALUE-side mint — r_env / node-Nyquist proposed → SOLID — stays Grant-gated; see GATE note.)*
- **axis:** spatial-Brillouin
- **dimension/type:** length (L) — three distinct radial loci (values gate-measured)
- **status:** proposed *(FORM ruled — Ruling 8; the numerical values + the length-canonical mint stay Grant-gated, see the GATE note below)*
- **canonical-home:** [`envelope-anatomy.md`](envelope-anatomy.md) (clm-3surfa)
- **clm-cross-links:** clm-3surfa
- **open-ambiguity-flag:** no *(the mint DISSOLVES the §45 A-vs-B fork into named surfaces at the FORM level: Resolution A ↔ wall/floor, Resolution B ↔ balance-or-knee; the value-side stays gate-(b))*
- **verification:** VERIFIED **0 prior `def-anat3s` / "three-surface anatomy" hits** (two-method). The three surfaces re-grepped THIS session against their anchors: wall/floor `trampoline-framework.md:687` + [`boundary-observables-m-q-j.md`](boundary-observables-m-q-j.md); balance `../vol2/particle-physics/ch01-topological-matter/hollow-vortex-binding.md:49,:133` (clm-hvb7q3); knee `src/ave/core/chiral_lattice_v10.py:29-30,:56` ($A^2_{yield}=2\alpha$, $s=\sqrt{1-A^2}$). FORM minted per Grant Ruling 8 (option C, in-chat 2026-07-14; record PR #695 docket continuation). **Values NOT SOLID.**

---

<!-- GATE (docket `_orchestration/2026-07-10_rulings-docket.md`:724,:782 — #686 branch): **FORM-LEVEL MINT AUTHORIZED (Grant Ruling 8, option C, 2026-07-14; record PR #695 docket continuation).** The three-surface ANATOMY (wall / balance shell / knee) is now minted as FORM — the anatomy def-node `def-anat3s` + `envelope-anatomy.md` (clm-3surfa) — DISSOLVING the §45 A-vs-B fork into named surfaces (Resolution A ↔ wall/floor sub-node, Resolution B ↔ balance-or-knee supra-node) at the FORM level. STILL GATED (value-side): (a) the envelope-LENGTH canonical mint — promoting r_env (def-088f0d) + node-Nyquist-size-boundary (def-e0cd83) proposed→SOLID — stays QUEUED / GRANT-GATED; (b) the VALUE-side §45 resolution (which radius each surface sits at; whether the balance shell is a distinct surface or coincides with the wall — Ruling 6's conjecture) is **gate-(b)**; (c) "envelope = the wall" as the primary sense is **CONFIRMED (Grant in-chat 2026-07-15; record: the post-merge auditor PR + the 2026-07-15 docket continuation)** — the other two surfaces (balance shell, knee) keep their own names; this word-level FORM ruling flips NO value node and leaves (a)/(b) gated. This `def-envl0p` node stays the NON-LOCKING register-hygiene ambiguity record for the envelope TOKEN's Sense-A/B (real-space-shell vs phasor-gain) overload — a DIFFERENT axis from the §45 Resolution-A/B fork; it mints NO length and flips NO proposed node to SOLID. -->

## envelope
<!-- id: def-envl0p -->

- **term:** envelope
- **adjudicated-meaning:** *(TWO genuine registers under one token — real-space shell vs phasor-gain condition; the A46 phase-space-vs-real-space clarity risk).* **Sense A — real-space SHELL** [spatial-Brillouin]: the physical 3D saturation-boundary shell of a soliton — the "boundary envelope" of [`trampoline-framework.md`](trampoline-framework.md):685, the finite-thickness region where $A$ approaches the saturation surface. Its canonical LENGTH is the PROPOSED, Grant-gated **r_env** coinage (def-088f0d, *status:proposed — GATED / NOT SOLID*); this node references r_env **as proposed, not by identity**. **In the three-surface anatomy (def-anat3s, [`envelope-anatomy.md`](envelope-anatomy.md), FORM-minted per Grant Ruling 8): this Sense-A real-space shell is the WALL / floor surface (i)** — the §45 Resolution-A sub-node locus. (The §45 Resolution-A/B fork is a DIFFERENT axis from this node's Sense-A/B shell-vs-phasor overload; the anatomy dissolves the former at FORM level only, values gate-(b).) **§45 A-vs-B fork — OPEN (this node takes NO position):** whether this real-space feature is a *supra-node body envelope* (Resolution B) or a *sub-node charge-core feature* (Resolution A) is an unresolved Grant-gated canonical fork (def-e0cd83); this node does NOT equate the boundary-envelope shell with the supra-node "body envelope". **Sense B — phasor-GAIN condition** [phase-carrier]: an amplitude/phase condition, NOT a spatial region — the modulation envelope of a `carrier × envelope` decomposition, and the reversible sub-yield $\sqrt{1-A^2}$ saturation-gain envelope. A gain/modulation envelope (Sense B) is a locus in amplitude/phase space; do NOT read it as a real-space shell (Sense A).
- **axis:** other (spans spatial-Brillouin [A] and phase-carrier [B])
- **dimension/type:** length (L) [Sense A] vs dimensionless amplitude-gain / envelope function [Sense B]
- **status:** ambiguous *(non-locking register-hygiene record — the envelope-LENGTH canonical mint + the §45 A-vs-B resolution stay Grant-GATED; see the GATE note above the heading)*
- **canonical-home:** Sense A — [`trampoline-framework.md`](trampoline-framework.md):685 ("boundary envelope … size set by $\ell_{node}$") + the PROPOSED/gated r_env (def-088f0d, NOT SOLID); Sense B — [`substrate-hysteresis-index.md`](substrate-hysteresis-index.md):24,136 (reversible sub-yield $\sqrt{1-A^2}$ envelope).
- **clm-cross-links:** *(none verified-specific yet; cross-node: def-088f0d (r_env, Sense-A length), def-a9eef5 (carrier — the "carrier × envelope" partner), def-69f472 (phase-space))*
- **open-ambiguity-flag:** YES — the two registers above. **Conflicting sites (conflation-map):** *Sense A (real-space shell)* — `trampoline-framework.md:685` (boundary envelope, $\ell_{node}$-set); `src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py:26` ("the actual real-space envelope is a power-law hedgehog SHELL"). *Sense B (phasor-gain)* — `vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md:58,61` ("carrier × envelope" / "Gaussian envelope × sinusoidal carrier"); `substrate-hysteresis-index.md:24,27,136` ("reversible reactive envelope", "the smooth $\sqrt{1-A^2}$ envelope"). *(The inherited Sense-A site `vol_2_quantum/…/02_baryon_sector.tex:40` "multi-node body envelope" was STRUCK 2026-07-14 — fabricated path + quote, review finding 2; see verification.)* The board B4 tension (`trampoline:685` "envelope size set by $\ell_{node}$" vs the nucleus 1 fm = 386× below $\ell_{node}$) is a **Sense-A** reading; it does not touch Sense B. **2026-08-24 extension (proposed, `def-prstor` package):** two further "envelope" senses are recorded outside this node and must not be folded into Sense A or Sense B — the **`def-envcar` slow envelope $A(r,t)$** (the A1 breather's real-space bias texture, SOLID for the decomposition) and the **phase-space tube-phase-family torus**, which loses the word entirely to **presentation torus** (`def-prstor`). Full four-sense inventory + receipts at `def-prstor`'s disambiguation block.
- **verification:** VERIFIED 2026-07-14 (repaired per PR #690 review, 2026-07-14) — both senses re-grepped two-method (`grep -F` + `git grep`) THIS session at the cited sites: Sense A `trampoline-framework.md:685` "boundary envelope … size set by $\ell_{node}$" (present), `tlm_electron_soliton_eigenmode.py:26` "the actual real-space envelope is a power-law hedgehog SHELL" (present); Sense B `photon-ee-mapping.md:58,61` "carrier × envelope" / "Gaussian envelope × sinusoidal carrier" (present), `substrate-hysteresis-index.md:24,27,136` reversible sub-yield $\sqrt{1-A^2}$ envelope (present). **STRUCK (fabricated citation — review finding 2):** the inherited Sense-A site `manuscript/vol_2_quantum/chapters/02_baryon_sector.tex:40` ("multi-node body envelope") — that directory does NOT exist (real tree: `vol_2_subatomic/`), the real file has ZERO "envelope" hits, and the phrase appears nowhere in the corpus outside this register (also pre-existing at `:173` in the **`size` def-node** (def-249370) — **RESOLVED 2026-07-14, Wave-0 KB batch**: struck there too, same rationale; previously this parenthetical mislabeled that node as "the r_opt node" — it is `size`). Dropped, NOT repointed (repointing to the real `:41` "spans multiple fundamental nodes" would re-assert the supra-node body reading the §45 gate holds open). Register-hygiene def-node; adds/retires no `clm-`; mints no length, resolves no fork (see GATE note). Cross-links to the six-scale boundary-register tag (`boundary-observables-m-q-j.md`).

---

<!-- BUILD-SCAFFOLD REMOVED 2026-08-05. An insertion-instruction comment sat here ("PROPOSED CANDIDATE — awaiting Grant ratification; NOT yet canonical … Insert this block ABOVE the `## SubstrateExcitation *(proposed)*` heading (the anchor line). status:proposed, GATED on auditor + Grant …") — PR #265 build scaffolding that was never removed when the block landed, and which CONTRADICTED the block immediately below it: `def-tk1xfm` is **SOLID — ★GRANT-RATIFIED 2026-07-21** (verbatim `[sic]`: "ratify def-tk1xfm"; adjudicated-meaning :438, status :441, verification :452). Removed as a stale BUILD ARTIFACT, not struck as a claim — the comment carried an insertion instruction and a gate that no longer exists, asserted no physics, and its two substantive provenance facts survive IN-BLOCK: the 0-prior-hits coinage check (verification field) and the 'transformer'-overload guard against the translation-circuit.md §9.2 SOLITON-STRUCTURE object (open-ambiguity-flag (b)). The removed text lives in git. Replacement is deliberately ONE line: `:435` / `:441` are cited by external leaves. -->

## TKI-transformer
<!-- id: def-tk1xfm -->

- **term:** TKI-transformer (topo-kinematic transduction; the Axiom-2 dictionary read as an ideal transformer)
- **adjudicated-meaning:** *(RATIFIED SOLID — Grant 2026-07-21, `[sic]`: "ratify def-tk1xfm"; see status. Prior "PROPOSED, gated" preserved per Rule 12.)* Axiom 2 (Topo-Kinematic Isomorphism, `eq_axiom_2.tex:12`) read as the **ideal, lossless, gain-1, pole-less, INVERTIBLE electromechanical dictionary** between the substrate's mechanical port ($u$/strain $\leftrightarrow$ E, $\omega$/curl $\leftrightarrow$ B) and its electrical port — a **structure-preserving change-of-reference**, the units-checked $\xi_{topo}$ six-row identity table ($Q=\xi x,\ I=\xi v,\ V=\xi^{-1}F,\ L=\xi^{-2}m,\ C=\xi^{2}\kappa,\ R=\xi^{-2}\eta$; `translation-circuit.md:17-26`, clm-fy05jc), which are *"identity statements ... not approximations, not analogies"* (`translation-circuit.md:41`). It transduces **losslessly** — same joule, two gauges — and does **NOT** trap, convert-with-gain, or carry a pole. **It is NOT the resonator's transfer function:** the DYNAMICS (poles = masses, $Q = 1/\alpha$ = the per-cycle radiative leak, saturation = the trap) live in the **four-axiom resonator $H(s)$** (`cvr-transfer-function.md:23-47`), NOT in Axiom-2. The dictionary and the transfer-function are different objects; conflating them inflates a units-bridge into a derived mechanism.
- **axis:** notation / other (a re-reading of an axiom as an EE structure; emits no quantity of its own)
- **dimension/type:** class/structure (n/a — a transduction map; the $\xi_{topo}$ it carries is C/m, INVARIANT-C2)
- **status:** SOLID — ★GRANT-RATIFIED 2026-07-21 (verbatim `[sic]`: *"ratify def-tk1xfm"*), on the framed one-sentence ratification package (pending-rulings §1 item 7): *"Ratify `def-tk1xfm` proposed→SOLID: the Topo-Kinematic Isomorphism (Axiom 2) is an EXACT, lossless, gain-1, pole-less, invertible **co-equality of the mechanical and electrical descriptions BELOW the band edge** ($\omega\tau\ll1$ / long-wave regime), with **per-sector carriers at lattice scale**; the co-equality is REGIME-SCOPED — at band-edge scales the distributed-in-bond (arccos TL) and lumped mass-spring descriptions book the delay differently and are no longer co-equal (per the ratified bond scope, `def-b0nd01` / `clm-bnd5rq`)."* The strength ceiling STANDS: *"identity-by-translation, NOT emerges-from / NOT a derivation"* (reaffirmed by the Cleave-01 Chern null, `clm-clvchn`) — SOLID means the node is ratified/canonical, NOT that it derives a mechanism. *(Prior status, preserved per Rule 12: **proposed** since PR #265 — GATED on auditor + Grant, NOT canon.)* ★**One clause adjusted post-inversion-catch — ✅ GRANT-CONFIRMED 2026-07-21 (verbatim `[sic]`: *"confirm"*, item 3 of the 2026-07-21 adjudication queue; pending-rulings §1 item 8 discharged):** the framed sentence's *"per-sector carriers at lattice scale"* rode the inverted orchestrator walk and is corrected to — *the distributed/TL description is the adjudicated band-edge carrier in BOTH sectors (`clm-bnd5rq`); the lumped mass-spring is the long-wave approximation; the co-equality statement is between the mechanical and electrical descriptions (the TKI proper), exact below the band edge where lumped↔distributed also coincide*. The ratified sentence's CORE (proposed→SOLID, exact co-equality below the band edge) STANDS; the corrected carrier wording is CONFIRMED.
- **canonical-home:** *(none — coinage; the underlying isomorphism is `eq_axiom_2.tex:12`, the dictionary table `translation-circuit.md:17-26` clm-fy05jc, the contrast object `cvr-transfer-function.md:23-47`)*
- **clm-cross-links:** clm-fy05jc (the $\xi_{topo}$ dictionary), clm-eemap1 (EE-as-substrate-native at minimal-DOF)
- **canon-noun map:** the non-canon engineering name 'TKI-transformer' maps to the canon noun **Topo-Kinematic Isomorphism (Axiom 2)**; it MUST NOT drift into a noun-swap and MUST inherit the strength ceiling *'identity-by-translation, NOT emerges-from / NOT a derivation'* (the `translation-circuit.md:660` piezo over-claim guard precedent).
  - **CEILING REAFFIRMED by a computed null (2026-07-02, KEEP-BOTH note).** The Cleave-01 displacement coupling $Q = \xi_{topo}\,x$ — the dictionary's displacement row read as a *mechanism* — was tested for a derived-pump instance: both the 2-band and faithful N-band srs occupied-manifold Chern over the $(k_z,\theta)$ registry torus return $C = 0$ (both readings, both enantiomorphs; `clm-clvchn`, `research/2026-07-02_cleave-registry-pump-chern-nband_result.md`). **No derived-mechanism instance emerged — the 'identity-by-translation, NOT a derivation' ceiling holds** (a nonzero $C$ would have been the first derived-mechanism instance and an upgrade path; the null reaffirms the ceiling).
- **open-ambiguity-flag:** YES — the surface form 'transformer' is overloaded against an existing live object, and one clause is split out to an open seam:
  - (a) **TKI-transformer (THIS node, proposed):** the $\xi_{topo}$ DICTIONARY / change-of-reference — gain-1, pole-less, invertible, lossless. [transduction map]
  - (b) the **soliton-structure 'transformer'** (already in corpus): the (p,q) winding read as toroidal transformer winding-numbers, with leakage-inductance $\to$ weak-force range — `translation-circuit.md:544-554` (the '#### Ideal transformer' sub-block WITHIN §9.2, clm-grounded :551). This is the SOLITON's STRUCTURE, a DIFFERENT object; do NOT let (a) and (b) collapse. [soliton structure]
  - (c) the **resonator $H(s)$** (already canonical): the DYNAMICS — the 2nd-order pole pair $s_\pm=-\alpha\omega_0/2\pm j\omega_d$, $Q=1/\alpha$ leak, $S(A_0)$ Axiom-4 detune (`cvr-transfer-function.md:30-41`). This is exactly what (a) is NOT. [transfer function]
  - **OPEN-SEAM (do NOT canonize — split out of C1):** the clause *'chirality = the handed turns-ratio SIGN $\to$ spin sign'* has **no corpus anchor** tying a transformer turns-ratio sign to spin sign. `eq_axiom_2.tex:21` grounds only **charge SIGN = dislocation handedness** (particle/antiparticle Burgers vectors), NOT spin. The chirality def-node (`def-7c3f9e`) is `status:ambiguous` with the production-vs-instrument split *explicitly unadjudicated* (`the-abandoned-interior.md:183`, 'do NOT pick a side'). The wall-fork H3 is now **MERGED (PR #260, verdict B3 DEGENERATE)** — magnetic-vs-capacitive is a degenerate chirality-set sign/spin selector, NOT a sector branch; the earlier 'magnetic PRIMARY asserted-not-derived' is **superseded by the degeneracy ruling**. The B3-degenerate verdict makes chirality→spin-sign MORE open (the magnetic-primary prop that might have grounded it collapsed), so keep it as an open-seam POINTER to def-7c3f9e / PR#260, not a definitional identity here.
    - conflicting sites: TKI dictionary `translation-circuit.md:17-26,41` (clm-fy05jc); soliton-structure transformer `translation-circuit.md:544-554` (§9.2 'Ideal transformer' sub-block); resonator $H(s)$ `cvr-transfer-function.md:23-47`; chiral-piezo Class-B reframe `translation-circuit.md:643-660` §11; chirality→spin open seam `def-7c3f9e` + PR#260 (MERGED, B3 DEGENERATE).
- **verification:** *(completed at ratify-time — ★Grant-ratified 2026-07-21, `[sic]`: "ratify def-tk1xfm")* the dictionary reading is grounded (`translation-circuit.md:41` 'identity statements, not approximations, not analogies'; `vol5/claim-quality.md:19` the $L/C$ bridges are 'definitional dimensional bridges, convert units not predictions'); the contrast object ($H(s)$ = the dynamics) is canonical (`cvr-transfer-function.md:23-47`). The 'lossless/gain-1/pole-less transformer' framing was a NEW coinage (0 prior hits at PR #265); it is now **SOLID** (Grant-ratified 2026-07-21) **with the Class-B 'NOT a derivation' ceiling PRESERVED** (`translation-circuit.md:646,660`) — the SOLID flip ratifies the node as canonical (exact co-equality below the band edge), it does **NOT** lift the identity-by-translation / not-a-derivation strength ceiling (the Cleave-01 $C=0$ Chern null reaffirms it, `clm-clvchn`). *(Prior verification note, preserved per Rule 12: "to be completed by auditor/Grant at ratify-time … must NOT seed SOLID" — that ratify-time is now.)*

---

## SubstrateExcitation *(proposed)*
<!-- id: def-7a3f1c -->

- **term:** SubstrateExcitation
- **adjudicated-meaning:** *(PROPOSED, gated)* the **class** (base of a class-tree) of any localized excitation of the substrate — the class-invariant FORMS (the resonator pole shape $s_\pm=-\omega_0/(2Q)\pm j\omega_d$, the root-locus, the Axiom-4 kernel $S(A)$, the $\Gamma_{spinor}=-1$ wall) that carry NO instance operating point. Concrete instances supply their own geometry / $(p,q)$ / mass / $L/C$ / $\omega_0$ / $Q$.
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

## DC operating point / quiescent point (Q-point)
<!-- id: def-q1escn -->

- **term:** DC operating point / quiescent point (Q-point)
- **adjudicated-meaning:** *(RATIFIED 2026-08-10 under R43 — see the VOCABULARY RULING below)* the canonical name for the substrate cell's **saturation-state $A$** read as a **DC operating point** — "the dynamical state of the LC tank, analogous to DC bias on a semiconductor varactor" ([`CLAUDE.md`](../CLAUDE.md):75). The electron's Q-point is **self-set** (Axiom-4 self-saturation *is* the bias mechanism, no external bias network) and **self-stable** (the $R\cdot r=\tfrac14$ equilibrium; rest-mass = the DC energy stored at the Q-point). The VCA / graded-impedance trio is the **small-signal** response linearized *around* this Q-point. It is the previously-unnamed DC-bias step of the EE workflow (DC-bias → linearize → AC), NOT a new object.
- **axis:** other (operating-point state along the Axiom-4 kernel; distinct from the kinematic DOFs)
- **dimension/type:** dimensionless (the per-port normalized bias $A=|V|/V_{yield}$); per-port biases sit on the $V_{yield}/V_{snap}$ ladder [voltage scales]
- **status:** SOLID *(PROMOTED from `proposed` 2026-08-10 under R43 — meaning locked AND cites confirm; the promotion rides the BC-SRC ratification, whose clause **Q** IS this object at substrate scope)*
- **canonical-home:** [`node-up-small-large-signal.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md):§4b (the bias-then-small-signal re-expression); the electron load-line at [`cvr-dc-operating-point.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-dc-operating-point.md):43-45; the "DC bias on a varactor" operating-point state at [`CLAUDE.md`](../CLAUDE.md):75. **Substrate-scope home added 2026-08-10 (R43):** [`eq_axiom_5.tex`](../../common_equations/eq_axiom_5.tex) clause **Q** (`eq:bcsrc_quiescence`) + the BC-SRC entry in [`axiom-register.md`](axiom-register.md) — the SAME object at substrate scope: clause Q is the sourceless substrate's DC operating point ($\nabla\cdot\pi = 0$, $\theta = 0$, $\varepsilon_{11} = 0$ away from defects), the quiescent reference that makes the potentials defined and clause G's elliptic solve well-posed. Per-cell Q-point (the $A$-state) and substrate Q-point (clause Q) are the SAME noun at two scopes, not two terms
- **clm-cross-links:** clm-vca7r1 (node-up small/large-signal), clm-fd1e7a (the electron R/X/Q/L/C bundle = the small-signal read), clm-kezk9z (the $\Gamma=-1$ cage at the saturated bias)
- **canon-noun map / ★ VOCABULARY RULING (R43, 2026-08-10 — BINDING on every consumer; the FINAL-scope record per R44):** the **canonical term is "DC operating point / quiescent point (Q-point)"**. **"Ground (reference)" is the EE-ANALOGY GLOSS, NEVER the canonical noun** — it may appear only as an explicitly-labelled analogy. Ruling verbatim, the full wrapped sentence at [`2026-08-10-ruling-r43-ratification.md`](../../../_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md):23-24 — *"the canonical term is **DC operating point / quiescent point (Q-point)**; "ground (reference)" is the EE-analogy gloss, never the"* (…canonical noun). Grant's ratification verbatim, same record `:7-8` — *"we can map it to ground but call it DC operating point? approved."* Grant's physical framing of record — *"BC-SRC is the GROUND REFERENCE of the floating network the bare axioms built"* — originates at [`2026-08-10-ruling-r43-sg-ratified.md`](../../../_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md):23-24 (*"**The physical framing of record (Grant's):** BC-SRC is the GROUND REFERENCE of the"*), a record R44 marks **SUPERSEDED in scope** — it is cited here ONLY as the record of origin for that Grant quote, never as authority. The term still maps onto the **saturation-state $A$** (self-set, Axiom-4) with no noun-swap; at substrate scope it is **Axiom 5 clause Q**. Authors: do not write "the vacuum's ground" as a canonical noun.
- **open-ambiguity-flag:** no (VERIFIED 0 prior KB hits for "quiescent" as a substrate-operating-point term at coinage — the single corpus hit `vol5/.../creatine-neural-capacitor.md` is an unrelated biological usage). *(Two DISTINCT usage cautions that are NOT open-ambiguities of this term's surface form, recorded so the flag stays honest rather than inflated: (i) the letter **Q** alone is heavily overloaded in this corpus as the **quality factor** — write "Q-point", never a bare "Q", when the operating point is meant; (ii) **"ground"** is a live mis-use hazard created by the ruling itself, since the EE analogy is the natural thing to reach for — it is the gloss, not the noun. Neither is a second MEANING of "DC operating point / quiescent point", so `open_ambiguity` stays false per the S12 orthogonal-axes rule.)*
- **verification:** VERIFIED the varactor-bias operating-point reading verbatim at [`CLAUDE.md`](../CLAUDE.md):75 and the electron load-line ($V_{snap}\approx511$ kV, $V_{yield}=\sqrt\alpha V_{snap}\approx43.65$ kV) at `cvr-dc-operating-point.md`:43-45. The $R\cdot r=\tfrac14$-sets-the-Q-point **α-free** (the α-flip) is **PENDING/open**, not asserted. **★ GATE DISCHARGED 2026-08-10 (R43): ADOPTED and SOLID** — *"The proposed `quiescent point` def-node PROMOTES to ratified under this naming"*; the prior "GATED on auditor + Grant review — NOT adopted, NOT SOLID" line is superseded and lives in git. **Scope of the promotion:** the NAME and the operating-point reading only. The α-flip stays PENDING/open exactly as below — ratifying the vocabulary does not ratify the α-free claim. *(α-flip STATUS, FORK-A 2026-06-24 — PENDING STANDS: the self-biased **pressure-equilibrium** route returns closed-NEGATIVE → ECHO — fixes a scale not the product $R\cdot r$, α re-enters via the √α ladder + $Z_0\propto\alpha$ area-bridge, relabel of the conservative $H_{couple}$ slosh; [`research/2026-06-24_forka-alpha-flip.md`](../../../research/2026-06-24_forka-alpha-flip.md). SCOPE = that named route ONLY, **NOT** route-exhaustion; the α-flip stays PENDING.)* **★ GRAVITY-SCOPE RIDER (2026-08-28, Grant-signed picture, PR #1033):** gravitational $\varepsilon_{11}$ is this **same noun** at gravity scope — the DC Q-point of the A1 tank (allowed AC swing / varactor bias), **not** a slide of the graph vertex. Clause Q already names the substrate-scope $\varepsilon_{11}=0$ away from defects; a mass is a defect that holds a local $\varepsilon_{11}$ as the cell's Q-point. Does **not** coin "Q-point gravity." Does **not** change the locked meaning or the SOLID status. Home of the constitutive inventory: [`hop-lc-constitutive-grading.md`](../vol3/gravity/ch03-macroscopic-relativity/hop-lc-constitutive-grading.md).

---

## port ↔ DOF ↔ sector map *(proposed)*
<!-- id: def-portmp -->

- **term:** port ↔ DOF ↔ sector map (the node's multi-port grouping)
- **adjudicated-meaning:** *(PROPOSED, gated)* the lock that groups the node's **6 Axiom-1 spatial DOFs + the saturation-state $A$** into sectors/ports across **two domains** (mechanical vs EM), so the same node can be read in EE port language without sector drift OR domain drift: **MASS** = the **MECHANICAL** A1/dilatation (trace-of-translation) port → $Z_{\mathrm{bulk}}$ ($\rho\times$speed, Pa·s/m); **CHARGE** = the **MECHANICAL** Cosserat **micro-rotation** $(2,3)$-winding port → $Z_{\mathrm{shear}}$ ($\rho\,c_{shear}$, Pa·s/m) — the **static reactive charge boundary** ($\mathrm{Link}(\partial\Omega,F)\in\mathbb{Z}$, lossless, no real power; its saturation modulation is the deviatoric-$G$ shear $c_{shear}=c_0\sqrt{S}$, **NOT** $\mu_{eff}$); **$\varepsilon$** = the **EM** capacitive/electric (displacement/Coulomb) param of $Z_{\mathrm{EM}}$; **$\mu$** = the **EM** magnetic constitutive param of $Z_{\mathrm{EM}}=\sqrt{\mu_{eff}/\varepsilon_{eff}}$ — **Meissner lives here** ($\mu_{eff}\to0\Rightarrow\Gamma=-1$). Effective params modulate with $S(A)$: $\varepsilon_{eff}=\varepsilon_0 S$, $\mu_{eff}=\mu_0 S$, $C_{eff}=C_0/S$ ([`CLAUDE.md`](../CLAUDE.md):73,:75). **DOMAIN guard (`resonant-lc-solitons.md`:129):** do NOT direct-wire the EM $\mu_{eff}$ onto the mechanical $Z_{\mathrm{shear}}$ — the bridge is the Axiom-1 **micro-rotation$\leftrightarrow\mathbf B$** coupling (`CLAUDE.md`:71) read through the **TKI-transducer** (def-tk1xfm, Axiom-2 dictionary, `status:proposed`, *"identity-by-translation, NOT a derivation"* ceiling) — **FLAGGED, not asserted**. **MASS (A1) $\perp$ CHARGE (T2)** ([`master-equation.md`](../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20) — the two homonymous "3"s are orthogonal ports, never one phasor.
- **axis:** other (sector/port taxonomy)
- **dimension/type:** class/structure (n/a — a grouping of DOFs into ports)
- **status:** proposed
- **canonical-home:** [`node-up-small-large-signal.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md):§0 (the multi-port table); Axiom-1 6-DOF + $A$-state at [`CLAUDE.md`](../CLAUDE.md):73,:75; the three-channel role map at [`resonant-lc-solitons.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):118-125
- **clm-cross-links:** clm-vca7r1, clm-kezk9z, clm-p5cf3t (the $\mu$/relativistic-inductor port)
- **canon-noun map:** the EE "ports/sectors" ↔ the Axiom-1 grades (A1 dilatation, Cosserat micro-rotation, $\varepsilon$/$\mu$); maps to canon grade nouns, no noun-swap. CONSISTENCY-class — re-expresses Axiom 1, coins no new DOF or number.
- **open-ambiguity-flag:** YES — "port" is overloaded (cf. def-cc2196 node open-ambiguity; the Vol-9 ch3 K4 **bond-port** vs **$\Gamma$-port** disambiguation): THIS map's "port" means a **sector/grade channel**, NOT the four K4 bond-ports nor a single-$\Gamma$ impedance boundary. Do not collapse the per-sector axis into the per-DOF-translation tensor axis of [`per-dof-vacuum-node-circuit.md`](../vol9/ch3-pin-port-configuration/per-dof-vacuum-node-circuit.md) (that refines only the 3 translation DOFs; this groups all 6 + $A$ by sector).
- **verification:** VERIFIED the 6-DOF + $A$-state content at [`CLAUDE.md`](../CLAUDE.md):73,:75 and $A1\perp T2$ at `master-equation.md`:20. The MASS/CHARGE/$\varepsilon$/$\mu$ role attribution re-expresses the three-channel ROLES (`resonant-lc-solitons.md`:118-125, themselves Grant-gated where the $V_{yield}$ fork applies). **DOMAIN-HYGIENE re-materialization (2026-06-24):** the prior "CHARGE = the Cosserat micro-rotation port (the $\mu$/inductive sector) → $Z_{\mathrm{shear}}$" string direct-wired the EM $\mu_{eff}$ onto the mechanical $Z_{\mathrm{shear}}$ — FORBIDDEN by `resonant-lc-solitons.md`:120,:124,:129 (CHARGE = mechanical static-reactive boundary, $\mu$ = EM param of $Z_{\mathrm{EM}}$, bridged by the def-tk1xfm transducer, not a direct wire). Separated above. **GATED on auditor + Grant review — NOT adopted, NOT SOLID.** **★Note (2026-07-21, #781 repair):** the `def-tk1xfm` transducer this map references (the $\mu_{eff}\leftrightarrow Z_{\mathrm{shear}}$ domain bridge) is now **SOLID** (Grant-ratified 2026-07-21, `[sic]`: "ratify def-tk1xfm"); `def-portmp` nonetheless **STAYS proposed** — its status-limiter was never the tk1xfm ceiling but its OWN gates: auditor+Grant review + the $V_{yield}$-fork-dependent three-channel role attribution (`resonant-lc-solitons.md:118-125`, Grant-gated where the fork applies) + the domain-hygiene re-materialization. Upgrade only when those clear (cf. `def-uatk1s`, whose SOLE limiter WAS the tk1xfm inheritance and which did upgrade).

---

## K4
<!-- id: def-4b1a2c -->

- **term:** K4 (the "K4" name — three distinct overloaded referents)
- **adjudicated-meaning:** the **production carrier** named "K4" is the **chiral srs z=3 net** (the true Sunada-K4 / Laves / srs net: degree-3, chiral, $I4_1 32$ — the object Axiom 1 names; referent (a) below) — RATIFIED as the engine's production carrier by Grant 2026-07-03 (D1). *(The surface form "K4" remains overloaded across three referents in historical prose — the overload documentation is retained, KEEP-BOTH; status and open-ambiguity are orthogonal per the SCHEMA Definition-record rule, cf. def-cc2196 `node`. The ratification locks WHICH sense is production, not the fact that the name was overloaded.)*
- **axis:** other (cross-file name overload spanning a real-space crystal name and a group label)
- **dimension/type:** n/a (a name) — its referents are: a graph/lattice (length-scale $\ell_{node}$), and a finite group (dimensionless)
- **status:** SOLID (production-carrier sense, Grant 2026-07-03 D1 RATIFICATION; name-overload documentation retained via open-ambiguity-flag — orthogonal per SCHEMA)
- **canonical-home:** *(no single home — the production-carrier sense is RATIFIED by Grant 2026-07-03 (D1), recorded in the D1-memo addendum `research/2026-06-12_lattice-d1-adjudication-memo.md` and the migration charter `_orchestration/2026-07-03_srs-migration-policy.md`; restated in-axiom at `manuscript/common_equations/eq_axiom_1.tex:11` (D1 PROVENANCE comment) + `:43` (the D1 in-body block). The broader crystalline-vs-amorphous seam — distinct from the carrier question — stays flagged at `the-abandoned-interior.md:183`.)*
- **clm-cross-links:** *(none verified-specific yet)*
- **open-ambiguity-flag:** YES — three distinct referents share the name "K4":
  - (a) the **axiom NAME "chiral Laves K4"** — the degree-3 srs / Sunada-K4 net, $I4_1 32$ chiral space group (the historical object Sunada called K4). Home: `manuscript/common_equations/eq_axiom_1.tex:37` (the "chiral Laves K4 Cosserat crystal" identity, now stating "3-fold ($z=3$) chiral srs (Sunada-K4 / Laves)" connectivity after the 2026-07-03 DOF-sentence restoration) + `:43` (D1 in-body block tying the name to srs); the srs builder at `src/ave/core/chiral_lattice.py:11-13,199-217`. [structural-chirality instrument]
  - (b) the **engine "K4"** — the degree-4 (z=4) bipartite-FCC **DIAMOND** lattice (achiral $Fd\bar{3}m$), on which the historical $\alpha$ / Lorentz / photon drivers compute (re-tagged a non-canonical instrument by the 2026-07-03 D1 ratification; migration chartered). Home: `src/ave/core/k4_tlm.py:101-119` (`K4Lattice3D`, the `# K4 (DIAMOND) LATTICE` banner at `:97`); the in-axiom re-tag at `eq_axiom_1.tex:43` (the D1 block: "the achiral z=4 diamond is re-tagged a non-canonical instrument"). *(The former `eq_axiom_1.tex:35`/`:37` cite — "The production computational net is z=4 diamond" — was DELETED by the LEAN commit `63fea0ae` and SUPERSEDED by the D1 ratification; re-pinned to `k4_tlm.py` + the D1 re-tag.)* [historical engine substrate, now non-canonical instrument]
  - (c) the **rotation GROUP $K4 \to A_4$** — the tetrahedral-group chain used in the spin-1/2 derivation. Home: `finkelstein-misner-spin-half-derivation.md:52,56` (the $K_4 \to A_4 \to 2T \subset SU(2)$ chain); `vol2/.../ch01-topological-matter/electron-identification.md:52`. [finite group, dimensionless]
  - **The load-bearing tension — ADJUDICATED (Grant 2026-07-03 D1 RATIFICATION):** the structural-vs-named mismatch (axiom NAME (a) = chiral srs net, but the historical PRODUCTION engine ran the achiral diamond (b)) is **RESOLVED**: **srs z=3 is RATIFIED as the production carrier** — the axiom object and the production object are now the SAME. The D1 memo's provisional framing default (B) (srs = instrument, diamond = engine, `research/2026-06-12_lattice-d1-adjudication-memo.md:44,:61`) is **SUPERSEDED** by the ratification (dated addendum appended to that memo). Evidence basis (cite, not re-derived): (1) diamond statics ill-posed — bipartite-checkerboard nullspace (`research/2026-07-03_localization-readjudication_result.md:196-197`); (2) the five-axis instrument comparison — statics, nullspace 1-vs-16, live fraction 89.5%-vs-6.5%, positive-control constructibility, chirality (diamond cannot host the (2,3) winding) (`research/2026-07-03_localization-readjudication_result.md:194-208`, §5); (3) the DEC 2-complex + exact operator calculus on srs (`research/2026-07-03_srs-dec-operators_result.md` — $\partial_1\partial_2=0$ exact, $\mathrm{div}=-\mathrm{grad}^\top$ exact, $b_1=3$ correct 3-torus); (4) Axiom-1 canon itself (z=3 chiral, `eq_axiom_1.tex:23-24`). This is an **ENGINEERING-FIDELITY** ruling — the engine implements the lattice the axiom names; NO new ontological claim beyond Axiom 1. Consequently the **(A) substrate-challenge axis CLOSES** (the axiom object and the production object coincide). The **P0 name walk-back moves from queued to EXECUTABLE** (this arc CHARTERS it; the future migration arcs EXECUTE it — `_orchestration/2026-07-03_srs-migration-policy.md`); the retained name "Laves K4" and the k4_tlm.py "bipartite Diamond" symbols are the walk-back targets. The **broader crystalline-vs-amorphous structural tension stays OPEN** (a distinct seam, NOT the carrier question) at `the-abandoned-interior.md:183` (auditor lane + Grant adjudicate).
    - conflicting sites (now with the resolved carrier tagged): axiom name / srs `eq_axiom_1.tex:37` (identity, z=3 chiral srs after the 2026-07-03 DOF-sentence restoration) + `:43` (D1 in-body block); historical engine diamond `src/ave/core/k4_tlm.py:97-119` (RE-TAGGED non-canonical instrument); group $K4\to A_4$ `finkelstein-misner-spin-half-derivation.md:52,56`; broader crystalline-vs-amorphous open seam `the-abandoned-interior.md:183` (distinct from D1, stays open); P0 walk-back EXECUTABLE (charter `_orchestration/2026-07-03_srs-migration-policy.md`).
- **verification:** VERIFIED the three referents at their cited sites (axiom name + srs builder, diamond `K4Lattice3D`, the $K4\to A_4$ chain). Status **adjudicated** (production-carrier sense) — the D1 RATIFICATION (Grant 2026-07-03) fixes the production carrier as the chiral srs z=3 net (referent (a)); the historical diamond (b) is re-tagged a non-canonical instrument. The name-overload DOCUMENTATION is retained (three senses stay — KEEP-BOTH; the overload history is real) — do not pick a referent for an un-qualified "K4" in *historical* prose, but NEW engine work uses referent (a). Evidence cites re-verified at this arc's HEAD (verify-before-cite); no counter-evidence to the ratification surfaced.

---

## chirality
<!-- id: def-7c3f9e -->

- **term:** chirality (chiral / handedness)
- **adjudicated-meaning:** *(no single locked sense — two distinct realizations the corpus is emphatic NOT to conflate; whether the production realization is GENUINELY a chiral space group is OPEN)*.
- **axis:** other — split across a dimensionless dynamical order-parameter and a real-space crystallographic motif
- **dimension/type:** dimensionless (the $\kappa_{chiral}$ scalar) for the dynamical reading; n/a / space-group label ($I4_1 32$ vs $I4_3 32$) for the geometric reading
- **status:** ambiguous
- **canonical-home:** *(no single home — the production-carrier / instrument split is stated in the D1 in-body block at `manuscript/common_equations/eq_axiom_1.tex:43` (the former `:35` "Cold-lattice handedness" cite was deleted by `63fea0ae`); the broader realization question is flagged OPEN at `the-abandoned-interior.md:183`)*
- **clm-cross-links:** *(none verified-specific yet)*
- **open-ambiguity-flag:** YES — two distinct chirality realizations:
  - (a) **DYNAMICAL chirality**: an excited $k_\chi$ Cosserat order-parameter realized as the scalar $\kappa_{chiral} = \alpha\,\tilde{\kappa}(p,q)$ on the **ACHIRAL $Fd\bar{3}m$ diamond** (the historical engine, now a non-canonical instrument per the 2026-07-03 D1 ratification), asymmetrically loading $\mu$-up / $\varepsilon$-down by local helicity. Home: `src/ave/topological/cosserat_field_3d.py:115-124` ($\kappa_{chiral}=\alpha\cdot\tilde\kappa$), `:522-523` (asymmetric loading); the diamond port-handedness at `src/ave/core/k4_tlm.py:535-548` (`get_helicity_density`). *(The former `eq_axiom_1.tex:35` cite — "Cold-lattice handedness on diamond is an excited $k_\chi$ Cosserat order-parameter" — was DELETED from the axiom file by the LEAN commit `63fea0ae` (2026-07-03); the code home above is the surviving canonical source.)* The strength inherits the $\alpha$ calibration. [dynamical order-parameter, dimensionless]
  - (b) **GEOMETRIC / STRUCTURAL chirality**: the literal $I4_1 32$ Wyckoff-8a srs atomic motif (right-handed = $I4_1 32$, left-mirror = $I4_3 32$) — the **INSTRUMENT** path, not the substrate. Home: `src/ave/core/chiral_lattice.py:45-46,215`. [crystallographic space-group motif]
  - **The OPEN question (do NOT pick a side):** whether the port-handed bipartite **achiral diamond** (a) genuinely **realizes Axiom-1's CHIRAL $I4_1 32$ space group**, or is an achiral diamond carrying a dynamical port-handedness, is **NOT settled in any code read**. The corpus closes the NARROWER chiral-vs-centrosymmetric space-group question as a FALSE POSITIVE ($Fd\bar{3}m$ is the supergroup of $I4_1 32$; $k_\chi=0 \Rightarrow Fd\bar{3}m$, $k_\chi>0 \Rightarrow I4_1 32$ — `claim-quality-closure-roadmap.md:191`, Foundation Item 10; corroborated `manuscript/ave-kb/common/translation-tables/translation-circuit.md:652`), but the BROADER crystalline-vs-amorphous structural model doing the isotropy work is "**not unified**" and named a "**real open seam**" at `the-abandoned-interior.md:183` (auditor lane + Grant adjudicate).
    - conflicting sites: dynamical $\kappa_{chiral}$ on achiral diamond `src/ave/topological/cosserat_field_3d.py:115-124,522-523` (the former `eq_axiom_1.tex:35` cite was deleted by `63fea0ae`, re-pinned to the code home); geometric $I4_1 32$ srs motif `src/ave/core/chiral_lattice.py:45-46,215`; supergroup FALSE-POSITIVE close `claim-quality-closure-roadmap.md:191` (corroborated `manuscript/ave-kb/common/translation-tables/translation-circuit.md:652`); broader open seam `the-abandoned-interior.md:183`.
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
  - (d) the isotropic-solid **longitudinal P-wave** $c_L = \sqrt{(K+\tfrac{4}{3}G)/\rho} = \sqrt{10/3}\,c \approx 1.83c$ at $K=2G$ ($\nu=2/7$). This is DISTINCT from the $\sqrt{2}\,c$ bulk-modulus dilatational speed (which drops the $4G/3$ shear term) — the 2026-06-08 c_L reconciliation (Rule 12). Home: `vol1/dynamics/index.md:28`; `vol1/dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md:38`. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** *(cite excerpts, byte-exact at the cited lines — appended because the R40-B2a stamp modified this line and `verify-new-cite-excerpts` re-classifies its pre-existing cites as added: `Longitudinal (P) Wave | $c_L = \sqrt{(K_{vac}+\tfrac{4}{3}G_{vac})/\rh` · `$A_1 \propto (1, 1, 1, 1)$ | Scalar / longitudinal (lattice port-mode)`)*
  - **CALIBRATION IDENTITY:** the cold-lattice $c$ enters as $G_{vac} \equiv \rho_{bulk}\,c^2$ (from $v_{transverse}=\sqrt{G/\rho}=c$), a definitional identity NOT independently grid-derived. Home: `src/ave/core/constants.py:670-672` ($G\_VAC = RHO\_BULK \cdot C\_0^2$).
  - **FLAG — OPEN (do NOT pre-judge):** the **continuum-vs-discrete photon ontology (DEC-01 / #248)** is **unadjudicated** — whether light is a continuous transverse-energy mode (Branch C) that the discrete substrate merely *samples* (imprinting the $\sqrt{2}$ as an observation fingerprint) vs literal discrete transport is an OPEN ruling. The $\sqrt{2}c$ front's mode-identity (bulk-precursor vs T₂-photon group velocity) is empirically unisolated. Tracked home: the $T_2$-only-vs-A1+T₂ photon-ontology tension is the field-symbol-registry R1 row `research/2026-06-10_field-symbol-registry.md:341` (`photon-identification.md:11` vs `master-equation.md:20`); the $\sqrt{2}c$ mode-front is `vol1/dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md:38`. (The earlier `_orchestration/...handoff.md` cite was an UNTRACKED scratch file — dropped per the citation-rot re-pin; no def-node cites an untracked path.)
    - conflicting sites: $c_{EM}$ vs $c_{shear}$ clm-8nkvwy:111,113 + `manuscript/ave-kb/CLAUDE.md` (Pitfall #5); $\sqrt{2}c$ bulk mode + lattice-projection `photon-propagation-baseline.md:38` + `src/ave/core/k4_tlm.py:181-189`; $\sqrt{10/3}c$ P-wave `vol1/dynamics/index.md:28`; calibration identity `src/ave/core/constants.py:670-672`; DEC-01 ontology tension (tracked) `research/2026-06-10_field-symbol-registry.md:341`.
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
- **clm-cross-links:** clm-efo113 (Master Equation EFT validity — the longitudinal/7th-mode dispersion regime), clm-lv3uw1 (Magnetic-Branch Confinement — the A1 longitudinal grade re-engaging at the $\Gamma=-1$ wall), clm-uu1qbo ($A_1$/$T_2$ propagation-speed split, $c\sqrt{2}$ vs $c$ — the A1 longitudinal port-mode that grounds sense (d))
- **open-ambiguity-flag:** YES — "longitudinal" is overloaded (the field-symbol registry locks four readings); the load-bearing distinction is:
  - (a) the **bulk-volumetric / V-sector scalar** longitudinal grade — the Heaviside-excised compression scalar, the **A1 dilatation-mass "3"** (`master-equation.md:18,20`). This is the real, physical, Gauss-undeleted grade. **Physical realization:** the **K4 breathing mode** (symmetric radial dilation of all 4 nodes, `vol6/appendix/geometric-inevitability/lambda-higgs-derivation.md`), onto which the **SM Higgs** is a FORM-identification ($m_H = v/\sqrt{N_{K4}} = v/2$) — **NOT** a VALUE-derivation: the route imports $v$ and asserts $N_{K4}=4$, and the quaternion-scalar↔Higgs chord is closed-negative / G3-FAIL (see `def-9b3d05` + `research/2026-06-06_biquaternion-node-algebra-result.md`). [scalar V grade] **★SHARPENED 2026-08-07 — REFINE, not retract (everything above in (a) is byte-untouched; this is additive).** The **mechanical content** of this grade, adopted **verbatim** from #761 §1.1 (`research/2026-07-20_mechanical-commonmode-derivation_result.md`:46): the A1-dilatation $\theta=\nabla\!\cdot\!\mathbf u$ is the *"longitudinal polarization of the vector displacement field"* — *"NOT a separate scalar DOF; it is a projection of the same 3-vector"* $\mathbf u$ that the vector band survey solves (nonzero exactly on the P-branch, zero on the S-branches). **Why this is load-bearing and not a gloss:** it forecloses the QED gauge misreading *structurally* rather than by prohibition. A **separate** scalar DOF could be argued constrained/non-dynamical the way EM's $\nabla\!\cdot\!\mathbf A$ genuinely is (curl-only Lagrangian ⇒ no restoring force); a **polarization of a physical displacement field that carries a bulk restoring force** $K\neq0$ cannot be — it is a propagating P-branch wave, and carrying the EM Gauss-kill across is *"structurally incompatible with the rest of the corpus"* (same doc `:71`). The standing "never frame in QED-vector terms" guard is thereby given a *mechanism*, not just an instruction. **Disposition:** this lands, **at the def-node**, the repair #761 §1.3 routed at `:73` as a *"sector-ownership WORDING"* tightening. ★**The `master-equation.md:20` canon line itself is NOT edited** — it is the Grant-ratified 🔴 TWO-"3"s banner (PR#260), and #761 §6.2 item 2 (`research/2026-07-20_mechanical-commonmode-derivation_result.md`:181) books that half as a *"Grant/auditor sector-ownership WORDING ruling"* that is *"wording-only"* with *"the physics identification stands"*. **Def-node half discharged; canon-line half remains Grant's call.**
  - (b) **shear-in-the-longitudinal-direction** — the Cosserat longitudinal-shear sense (the substrate-mechanical $\tau_{zx}$ family used in the dark-wake / thrust arc), a genuine Maxwell/Cauchy shear stress. [stress, $N\,m^{-2}$]
  - (c) the **EM-forbidden** longitudinal photon (transverse-only EM mode) — the sense in which the photon has no longitudinal component.
  - (d) the **port / lattice** $A_1$ longitudinal port-mode ($\sqrt{2}c$ bulk-modulus dilatation; see `def-2e8d61` c).
  - **Load-bearing guard:** the A1 longitudinal scalar (a) is the **dilatation-mass "3"** and is ORTHOGONAL to the Cosserat $(2,3)$ micro-rotation winding (charge); never frame (a) in QED-vector terms, and never wire the winding into the breather's $(V_{inc},V_{ref})$ phasor (`master-equation.md:20`; see `def-1f6e34` the-3).
    - conflicting sites: Heaviside-excised scalar grade `master-equation.md:18,20`; the four-way registry lock `research/2026-06-10_field-symbol-registry.md` (Rule 3, not-canon draft); the K4 A1 longitudinal port-mode ($\sqrt{2}c$) `src/ave/core/k4_tlm.py:181-189` (sense (d); cross-ref `def-2e8d61` c); the EM-forbidden longitudinal photon `vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md:11` (sense (c)); longitudinal-shear $\tau_{zx}$ `common/dark-back-reaction-taxonomy.md:25` (sense (b)). (The earlier four-way-registry cite reached into an UNTRACKED `_orchestration` scratch handoff — dropped per the citation-rot re-pin and re-pointed onto the tracked twins above; no def-node cites an untracked path.)
- **verification:** VERIFIED the V-sector / Heaviside-excised scalar reading at `master-equation.md:18,20` (the scalar/longitudinal grade demoted by Heaviside–Gibbs, physical, re-engages at saturation). The four-way overload is documented in the not-canon field-symbol registry (no prior def-node) at `research/2026-06-10_field-symbol-registry.md` (tracked). Status **ambiguous** — multiple readings under one word; the V-sector scalar sense is the canonical primary but the surface form is overloaded and was unregistered until now.

---

## scalar-grade-0
<!-- id: def-9b3d05 -->

- **term:** scalar-grade-0 (the algebraic Cl(3) / quaternion grade-0 scalar SLOT)
- **adjudicated-meaning:** the **grade-0 scalar SLOT** of the node-algebra — the part `−(a·b)` that the product of two pure-vector biquaternions necessarily produces (`(a·𝐢)(b·𝐢) = −(a·b) + (a×b)·𝐢`), so the transverse (E,B) vector sector **cannot close without it** (`research/2026-06-06_biquaternion-node-algebra-result.md` §4.1, verified C4). This is an **algebraic structure** (a slot in `Cl(3)` / `ℍ⊗ℂ`), distinct from any of the physical FIELD-MODE senses of "longitudinal" (`def-9a4f07`): the slot is the common algebraic **home** of both Maxwell's gauge scalar and AVE's physical acoustic mode — it **identifies, it does not derive** (§4.3).
- **axis:** other — an algebra-level slot (grade-0 of the Clifford/biquaternion node-algebra), not a glyph on a physical substrate axis
- **dimension/type:** class/structure (n/a — an algebraic grade slot; the physical quantity that fills it is the scalar potential grade $V$, the home of `def-9a4f07` sense (a))
- **status:** SOLID — for the **algebra-sense only**: the grade-0 necessity is a verified algebraic fact (`§4.1`, C4 `= −(a·b)`), locked and cite-confirmed. (The SOLID lock and the open-ambiguity flag are orthogonal per the SCHEMA Definition-record rule; the surface form "scalar grade" / "longitudinal" remains overloaded — hence open_ambiguity YES below.)
- **canonical-home:** `research/2026-06-06_biquaternion-node-algebra-result.md` §4.1 (the algebra forces the scalar slot — structural necessity, algebra-level; the §4.3 myth-guard immediately follows)
- **clm-cross-links:** clm-efo113 (Master Equation EFT validity — the longitudinal/7th-mode dispersion the slot is the home of), clm-lv3uw1 (Magnetic-Branch Confinement — the A1 longitudinal grade re-engaging at the $\Gamma=-1$ wall)
- **canon-noun map:** the algebraic grade-0 slot abstracts the physical **A1 dilatation / longitudinal V-scalar grade** (`def-9a4f07` sense (a)); the non-canon algebra name "scalar-grade-0" MUST map to that canon noun and MUST NOT drift into a noun-swap (the slot is the algebra's *home for* the mode, not a new mode).
- **open-ambiguity-flag:** YES — the surface form "scalar grade" / "longitudinal" must be disambiguated against ALL FIVE senses; THIS node is sense (e), the algebra slot, and is NOT any of the four physical FIELD-MODE senses of `def-9a4f07`:
  - (a) the **bulk-volumetric / V-sector scalar** longitudinal grade — the Heaviside-excised compression scalar, the A1 dilatation-mass "3" (`master-equation.md:18,20`; `def-9a4f07` sense (a)). [physical scalar V grade]
  - (b) the **Cosserat longitudinal-shear** $\tau_{zx}$ — shear-in-the-longitudinal-direction, a genuine Maxwell/Cauchy shear stress (`common/dark-back-reaction-taxonomy.md:25`; `def-9a4f07` sense (b)). [physical stress, $N\,m^{-2}$]
  - (c) the **EM-forbidden longitudinal photon** — the transverse-only EM mode; Gauss's law $\nabla\cdot\mathbf{E}=0$ forbids longitudinal EM in vacuum (`vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md:11`; `def-9a4f07` sense (c)). [physical EM mode]
  - (d) the **K4 A1 port-mode** $\sqrt{2}c$ bulk-modulus dilatation (`src/ave/core/k4_tlm.py:181-189`; `def-9a4f07` sense (d), `def-2e8d61` (c)). [physical port mode]
  - (e) **THIS algebraic grade-0 SLOT** (`research/2026-06-06_biquaternion-node-algebra-result.md` §4.1) — a slot in the node-algebra, NOT a physical mode. [algebra structure]
  - **Load-bearing ACCEPTANCE guard (the §4.3 myth-guard, verbatim-scoped):** the algebra **re-opens the slot; the PHYSICS comes from Axiom 1 + Axiom 4 (a real compressible medium), NOT from Cl(3)**. The biquaternion scalar slot is the common algebraic home for both Maxwell's gauge scalar and AVE's physical acoustic mode — **it identifies, it does not derive**. In *standard* Maxwell the scalar modes are gauge (constrained away by current conservation), so "Heaviside deleted a physical mode" is **FALSE for standard EM**; AVE's medium *adds* a real longitudinal DOF where the transverse Maxwell vacuum has only the gauge slot. Never inflate this algebra-level necessity into a derivation of the mode (§4.4: "it does not *derive* the mode, and yields no new number, dispersion relation, or coupling").
    - conflicting sites: the algebra slot `research/2026-06-06_biquaternion-node-algebra-result.md` §4.1 (`= −(a·b)`, C4) + the §4.3 myth-guard; physical V-scalar grade (a) `master-equation.md:18,20` (`def-9a4f07`); Cosserat longitudinal-shear (b) `common/dark-back-reaction-taxonomy.md:25`; EM-forbidden longitudinal photon (c) `vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md:11`; K4 A1 port-mode (d) `src/ave/core/k4_tlm.py:181-189`.
- **verification:** VERIFIED the grade-0 algebraic necessity at `research/2026-06-06_biquaternion-node-algebra-result.md` §4.1 (`(a·𝐢)(b·𝐢) = −(a·b) + (a×b)·𝐢`; scalar part `= −(a·b)`, C4; "you cannot close the vector (E,B) sector without the scalar slot"); VERIFIED the §4.3 identify-not-derive myth-guard verbatim ("the algebra re-opens the slot; the physics ... comes from Axiom 1's medium + Axiom 4 (the Master Equation), not from Cl(3)"). SOLID for the algebra-sense (a verified algebraic fact); open-ambiguity YES records the five-way surface-form overload — THIS slot is sense (e), the physical mode it is the home of is `def-9a4f07` sense (a). The clm-cross-links (clm-efo113, clm-lv3uw1) are the canonical longitudinal/7th-mode claims the slot is the algebraic home of (per the biquaternion §1 cross-link table), NOT claims the algebra derives (§4.4: no new number/dispersion/coupling).

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
  - (a) the **A1 dilatation-MASS "3"** — the Heaviside-excised longitudinal compression scalar $V$ (the A1 breather; $m_e c^2$ = trapped acoustic compression energy). The longitudinal grade of `def-9a4f07`. The **SM Higgs** maps onto this same A1 scalar (= the K4 breathing mode, `lambda-higgs-derivation.md`) as a FORM-identification only — see `def-9a4f07` sense (a). [scalar V grade]
  - (b) the **Cosserat micro-rotation $(2,3)$ WINDING "3"** — the T2 couple-stress, Axiom-1 intrinsic-spin DOF; charge = Beltrami helicity $H_{bel}=\int\omega\cdot(\nabla\times\omega)$. [phase-carrier winding / dimensionless helicity]
  - **Load-bearing FORBIDDEN-wiring guard (Rule 12, Grant-ratified):** the two are ORTHOGONAL (A1 $\perp$ T2); **never wire the winding (b) into the breather's own phasor $(V_{inc},V_{ref})$** — $V_{ref}$ is a read-only projection of the same scalar $V$, not an independent DOF; doing so self-inflicts the genesis-24 / crystal $w_{pol}=0$ double-count. The TWO-objects disambiguation is canon (the `master-equation.md:20` Rule-12 box) but carried **no def-node** until now. (The `status: ambiguous` tag refers to the surface numeral "3" itself, which remains overloaded across two objects — NOT to the disambiguation, which is settled.)
    - conflicting sites: the canonical disambiguation box `master-equation.md:20` (A1 dilatation-mass scalar vs Cosserat $(2,3)$ winding, "never wire the winding into the breather's own phasor"); A1 scalar $V$ engine `src/ave/core/master_equation_fdtd.py:42-47`; Cosserat winding / helicity readout `src/ave/topological/cosserat_field_3d.py:2122` + `src/ave/topological/helicity_observer.py:39-59`.
- **verification:** VERIFIED the two-orthogonal-objects content and the forbidden-wiring guard verbatim at `master-equation.md:20` (Rule 12, Grant-ratified). Status **ambiguous** — the disambiguation is settled in canon, but the surface numeral "3" remains overloaded across two objects (it is the *overload*, not the *meaning*, that the ambiguous tag flags) and the wiring-guard must be qualified at every cite; recorded so the verifier-gated watch-list can catch its mis-use. Do not collapse the A1 "3" and the Cosserat "3" into one object.
  - **PROPOSED SHARPEN (two-natured nature-axis, epic-reroute 2026-06-24 — awaiting Grant ratification; NOT yet canonical; Rule-12: appended, nothing above edited; additive — the orthogonality (a)$\perp$(b) above is UNCHANGED, this adds the NATURE assignment):** the engine-reroute epic adds the **dynamical-vs-static nature axis** to the two "3"s — the **A1 dilatation-mass "3" is DYNAMICAL** (the breather; it seeds, evolves, slosh-exchanges; the time-orbit and the energy store live here; binds at $V_{\text{snap}}$, fork-b A1 mass cavity EXISTS), while the **Cosserat $(2,3)$ winding "3" is STATIC charge** (a deformation-invariant $\mathrm{Link}(\partial\Omega,F)\in\mathbb{Z}$ boundary integer; reactive/lossless, Axiom-3; does no real power across a dissipative port). "two-natured electron" = these two natures (dynamical mass + static charge), the two substrate sectors — NOT two particles glued. The nature assignment is grounded by BOTH internal dynamical loci reading NEGATIVE (#415 + #417): no single bound mode hosts both mass and charge-winding dynamically, so charge must be the static sector. Cross-link: def-3638f2 (winding STATIC/=Link/reactive-no-work guard), def-a9eef5 (carrier-vs-charge). CONSISTENCY-class, NOT a chord; charge=Link STANDS un-walked-back; mass=A1 (#260) untouched. See `research/2026-06-24_engine-reroute-epic-summary.md`.

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
  - **Cross-repo status (peripheral to AVE-Core canon):** the dark-wake thrust species (a) is the subject of an exploratory **AVE-Propulsion** arc (chiral plasma antenna radiating longitudinal Cosserat shear), where the corpus self-flagged a separate "dark-wave" coordinate-sense mis-definition (one of the handoff's catalogued vocabulary errors). Within AVE-Core the term is a settled definitional taxonomy (a no-claim leaf), though the surface form "dark wake" remains overloaded (see status note); the singular "dark wave" has **0 corpus hits**. Cross-repo: `AVE-Propulsion/manuscript/vol_propulsion/chapters/01_ave_resolutions.tex`. The vocabulary-debt classification of "dark wake" is the settled genus/species taxonomy at the tracked home `common/dark-back-reaction-taxonomy.md:11,21-39` (the prior `_orchestration/...handoff.md:94` cite was an UNTRACKED scratch file — dropped per the citation-rot re-pin; no def-node cites an untracked path).
    - conflicting sites: thrust species $\tau^{far}_{zx}$ `dark-back-reaction-taxonomy.md:21-27`; dark-resonance species $\Sigma_{near}$ `dark-back-reaction-taxonomy.md:29-37`; AMO overlap `dark-back-reaction-taxonomy.md:39`; cross-repo arc `AVE-Propulsion/manuscript/vol_propulsion/chapters/01_ave_resolutions.tex`.
- **verification:** VERIFIED the genus/species split, both symbols, both canonical-home leaves, and the AMO-overlap guard at `common/dark-back-reaction-taxonomy.md:11,21-39`; VERIFIED the cross-repo AVE-Propulsion footprint by grep. Status **ambiguous** — the taxonomy split is settled in canon, but the surface form "dark wake" historically collided two objects and the AMO "dark resonance" sense further overloads the renamed species (it is the *surface overload* the ambiguous tag flags, not the taxonomy); recorded so the watch-list catches the mis-use. The split is the content, not resolved here.

---

## optical-activity
<!-- id: def-0pt1ac -->

- **term:** optical-activity (alias **gyrotropy**)
- **adjudicated-meaning:** a **transverse-field SO(2) polarization-plane rotation** observable — the handed lattice rotates the plane of polarization of a transmitted transverse wave by an angle per unit path, sourced by the reflection-odd ring-writhe pseudoscalar (a reciprocal-Faraday **gyrator**, lossless per Axiom-3). The chiral srs-grid magnitude $\pm75.46°$/unit ([#195]) is an **engineering decree** (`ETA_ROT_PER_WRITHE=1.0`), NOT the derived transport — see **status**.
- **axis:** phase-carrier (a transverse 2-DOF polarization-plane angle) — explicitly NOT spatial-Brillouin and NOT a Cosserat rotational grade.
- **dimension/type:** angle (dimensionless, rad or °) per unit propagation; rate $d\theta/\text{step}$
- **status:** SOLID for the QUALITATIVE optical-activity facts (signed / enantiomorph-odd / diamond-null / writhe-sourced / lossless reciprocal gyrator — confirmed by the writhe-aware-transport GATE-1, PR #374). **MAGNITUDE DEMOTED:** the $\pm75.46°$/unit figure (#195) is an **`ETA_ROT_PER_WRITHE=1.0` engineering decree** (`chiral_lattice_vector.py:27,93` — injected per-node SO(2) twist $\eta\times\text{writhe}$), **NOT** substrate-derived transport. The substrate-DERIVED bulk g₀ (writhe-aware vector-TLM, PR #374) **converges to the 4₁ screw pitch** ($\mp2.21589$ rad / lattice-z-unit; signed, L-independent to machine precision, diamond-null); the **k→0 continuum / physical-rad-m mapping is PENDING** (literal lattice-scale value ~40 OOM over the cosmic bound). The engine token is definition-fenced (`measure_optical_activity` / `_optical_activity_per_node` / the `optical_activity` kwarg in `chiral_lattice_vector.vector_tlm_step`).
- **canonical-home:** `common/engine-capability-map.md:44` (the only engine with the chiral grid, srs $I4_1 32$; the $\pm75.46°$/unit figure there is the ETA-decree engineering scale, demoted per PR #374 — derived bulk g₀ = the 4₁ screw pitch)
- **magnitude-flag (NOT bankable):** the $\pm75.46°$/unit figure is an `ETA_ROT_PER_WRITHE` engineering DECREE × an unpinned chirality-fraction — NOT substrate-derived, NOT bankable; the substrate-DERIVED bulk g₀ (Phase-1 EXECUTED PR #374, OUTCOME A = 4₁ screw pitch) is $\sim$40 OOM OVER the cosmic bound, k→0 continuum extraction OPEN. The FORM (signed / enantiomorph-odd / diamond-null / writhe-sourced / lossless reciprocal gyrator) stays SOLID; only the MAGNITUDE is not a prediction. FORM-class node: `clm-fofwr1`.
- **clm-cross-links:** `clm-fofwr1` (the FORM-class field-free-optical-activity node — parity zero-vs-nonzero; magnitude-pending). *(#195 is an engine-result tag, not a clm node.)*
- **open-ambiguity-flag:** YES — the surface word **"rotation"** is the definition-fenced collision. Optical activity is a **transverse polarization-plane twist of the SAME 2-DOF field** (A1b / T1.5), and is **EXPLICITLY ORTHOGONAL to the Cosserat micro-rotation = the (2,3) WINDING = charge** (A1 ⊥ T2, `master-equation.md:20`, `def-5d2b8a`). Despite the shared word, optical-activity is NOT a micro-rotation DOF: it has no independent ω field, no separate scatter/connect, and no gapped dispersion branch (`engine_acceptance/test_l1_multiwave.py` DOF-capability finding). The pre-rename engine token `rot_per_node` / `_rotation_per_node` / `measure_dynamical_rotation` made this collision grep-visible; renamed 2026-06-17 to remove it.
  - conflicting sites: the orthogonal Cosserat micro-rotation winding `master-equation.md:20` (`def-5d2b8a` the two-"3"s); the optical-activity result `common/engine-capability-map.md:44`; the definition-fenced engine path `src/ave/core/chiral_lattice_vector.py:36,79,136`.
- **verification:** VERIFIED the $\pm75.46°$/unit #195 result verbatim at `engine-capability-map.md:44`; VERIFIED (PR #374) that magnitude is the **ETA decree** `ETA_ROT_PER_WRITHE=1.0` at `chiral_lattice_vector.py:27`, applied $\eta\times\text{writhe}$ at `:93` (injected, not derived); VERIFIED the substrate-DERIVED bulk g₀ = the 4₁ screw pitch ($\mp2.21589$ rad / lattice-z-unit, converged + signed) via the writhe-aware vector-TLM (`chiral_vector_tlm_phase1.py` GATE-1/2/3 PASS), with the k→0 continuum mapping pending; VERIFIED the engine mechanism is a 2×2 rotation of the two transverse components $V_{ref}[\dots,0]/[\dots,1]$ with angle sourced from `net_ring_writhe` (`chiral_lattice_vector.py`), i.e. a polarization-plane twist, NOT a micro-rotation DOF; VERIFIED the A1 ⊥ T2 orthogonality anchor at `master-equation.md:20`. SOLID for the locked optical-activity SENSE + qualitative facts; MAGNITUDE demoted from "validated/derived" to "ETA-decree engineering scale" (PR #374). The open-ambiguity-flag records the "rotation" surface-form collision the rename + this def-node fence.

---

## writhe
<!-- id: def-wr1th3 -->

- **term:** writhe (ring-writhe / mean ring-writhe pseudoscalar)
- **adjudicated-meaning:** the **reflection-odd geometric SOURCE pseudoscalar** of the lattice's closed circuits — the mean signed self-crossing measure over the net's distinct shortest rings. It is the κ=0 *geometry-only* channel (no κ_chiral injection) that sources the optical-activity rotation; nonzero + sign-flipped between enantiomorphs, identically zero on the achiral diamond control.
- **axis:** other — a signed geometric (topological-geometric) pseudoscalar of the lattice circuits; box-independent.
- **dimension/type:** dimensionless (signed pseudoscalar; reverses sign under mirror)
- **status:** SOLID — the reflection-odd ring-writhe is the load-bearing **signed discriminator** of the Phase-0 chirality smoke (clean sign-flip on the mirror operation; zero on the achiral control).
- **canonical-home:** `src/ave/core/chiral_lattice.py:387` (`net_ring_writhe` — "nonzero + sign-flipped between enantiomorphs; identically zero on the achiral control"); described at `src/ave/core/chiral_lattice_dynamics.py:18`.
- **clm-cross-links:** `clm-fofwr1` (the FORM-class field-free-optical-activity node this pseudoscalar SOURCES — parity zero-vs-nonzero).
- **open-ambiguity-flag:** no — "writhe" carries the single locked reflection-odd-pseudoscalar sense throughout the chiral-lattice engine. (It is the SOURCE; the optical-activity rotation `def-0pt1ac` is the field RESPONSE it drives. Distinct from **helicity** `def-h3l1c7`: writhe is a property of the lattice *geometry/circuits*; helicity is a property of the *wave* it carries.)
- **verification:** VERIFIED the reflection-odd pseudoscalar definition + the sign-flip / achiral-null discriminator semantics at `chiral_lattice.py:387-412` (`net_ring_writhe` docstring) and `chiral_lattice_dynamics.py:18` ("the SIGNED, converged Phase-0 channel is the reflection-odd ring-writhe pseudoscalar"). SOLID — single locked sense.

---

## helicity
<!-- id: def-h3l1c7 -->

- **term:** helicity (wave helicity / kinetic helicity sign)
- **adjudicated-meaning:** the **handedness SIGN of the WAVE** — the sign of a wave's circulation alignment (the kinetic-helicity reading $\int \mathbf{A}\cdot\mathbf{B}\,dV$ for an EM emitter; the wave's handedness for a transverse mode). This is a property of the **propagating excitation**, distinct from **chirality** (`def-7c3f9e`), which is the handedness of the **lattice** (the substrate / srs / K4 vacuum, set by parent-BH spin).
- **axis:** phase-carrier (a sign on the wave's circulation/polarization handedness)
- **dimension/type:** sign / dimensionless for the wave-handedness reading; $\int\mathbf{A}\cdot\mathbf{B}\,dV$ has dimension of (vector-potential·flux) for the kinetic-helicity reading.
- **status:** SOLID for the locked sense (wave handedness ≠ lattice chirality); the kinetic-helicity matching condition (Hopf/torus-knot $\mathbf{A}\parallel\mathbf{B}$) is a corpus-supported coupling sketch.
- **canonical-home:** `vol4/claim-quality.md:922` (kinetic helicity $\int\mathbf{A}\cdot\mathbf{B}\,dV\neq0$ as the wave-side matching condition to the chiral vacuum); the lattice-side **chirality** counterpart is `def-7c3f9e`.
- **clm-cross-links:** *(none verified-specific yet)*
- **open-ambiguity-flag:** YES — the surface form is overloaded against the LATTICE handedness term **chirality** (`def-7c3f9e`): (a) **helicity** = the WAVE's handedness sign (this node); (b) **chirality** = the LATTICE's handedness (`def-7c3f9e`). The corpus also uses "kinetic helicity" $\int\mathbf{A}\cdot\mathbf{B}$ specifically for the emitter-coupling matching condition (Hopf coil). Do NOT conflate the wave's helicity with the lattice's chirality, nor either with the writhe pseudoscalar (`def-wr1th3`, a lattice-circuit geometry source). Also note an **AMO/optics overlap**: "helicity" elsewhere is the spin-projection-on-momentum of a photon — the same physical handedness sign, but qualify when precision is needed.
  - conflicting sites: wave/kinetic helicity `vol4/claim-quality.md:922,926`; the LATTICE-chirality counterpart `def-7c3f9e` (and `computational-solver-selection.md:19` "handedness of the vacuum"); the geometry-source writhe `def-wr1th3`.
- **verification:** VERIFIED the kinetic-helicity matching condition $\int\mathbf{A}\cdot\mathbf{B}\,dV\neq0$ at `vol4/claim-quality.md:922,926`; VERIFIED that "chirality / handedness of the vacuum" is the LATTICE-side term (`computational-solver-selection.md:19`, `def-7c3f9e`), distinct from the wave's helicity. SOLID for the wave-vs-lattice distinction; open-ambiguity-flag records the chirality overload + the AMO photon-helicity overlap.

---

## graded vacuum impedance network
<!-- id: def-gv1net -->

- **term:** graded vacuum impedance network
- **adjudicated-meaning:** the vacuum equivalent-**circuit MODEL** drawn as **three WIRED reactance channels**, one per substrate grade — $Z_{EM}$ (T2 transverse field, the matched radiative port), $Z_{shear}$ (deviatoric $G$), $Z_{bulk}$ (dilatation $K$) — wired together through a chiral circulator (`def-ch1crc`) and terminated at confinement surfaces (`def-cf1srf`). It AMENDS the Grant-ratified **three-impedance law** (`vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md`, registry §3.11) by ADDING a two-"3"s tag to two of the channels (bulk = MASS-"3" A1 dilatation; shear = CHARGE-"3" Cosserat winding); it does NOT rename the channels. "graded" = the Heaviside-restored longitudinal scalar grade (`master-equation.md:18,20`).
- **axis:** other — an EE equivalent-circuit re-expression class (a CONSISTENCY object), not a substrate-object noun.
- **dimension/type:** circuit-model schematic (per-channel $Z$ in $\Omega$; $\Gamma$ dimensionless). The MODEL has no dimensionful output the channel impedances do not already carry.
- **status:** proposed — consistency-class re-expression. NOT a new physics result and NOT a new substrate primitive.
- **canonical-home:** `vol9/ch3-pin-port-configuration/device-circuit-models.md` §6 (the wired-network leaf); the channel impedances themselves are canonical at `three-channel-impedances.md` (registry §3.11).
- **clm-cross-links:** *(none — no-claim consolidation; references clm-kezk9z/clm-lv3uw1/clm-rtdmsn by cross-link)*
- **open-ambiguity-flag:** YES — **INVARIANT-N1 substrate-noun guard.** "graded vacuum impedance network" is the equivalent-circuit MODEL of the medium, **NOT** a new substrate-object noun (the substrate-noun slot stays prose-only: *substrate / chiral LC network / chiral Laves K4 Cosserat crystal*). Do NOT promote the network to an ontological object. Keep DISTINCT from the coarser **Electric / Magnetic / Either** `AVE_VACUUM_CELL` sector vocabulary (`device-circuit-models.md` §1) — that is a per-element constitutive sector tag, not the three-grade wave-channel set. Keep $Z_{EM}$ named $Z_{EM}$ (do NOT rename to $Z_{transverse}$ — both EM and shear are transverse waves, so "transverse" is ambiguous; EM is the native label since $Z_0$ is a vacuum constant).
  - conflicting sites: the channel-impedance law `three-channel-impedances.md:20-22` (registry §3.11); the coarser per-element sector tag `device-circuit-models.md:26-31` (`AVE_VACUUM_CELL` Electric/Magnetic/Either); the two-"3"s grade tag `master-equation.md:20`.
- **verification:** VERIFIED the three channel impedances + $\Gamma$ values verbatim at `three-channel-impedances.md:20-22` ($Z_{EM}\equiv Z_0$, $\Gamma_{EM}=0$; $Z_{shear}=\rho c_{shear}$, $\Gamma_{shear}\to-1$; $Z_{bulk}=\sqrt2\,\rho c_0$ at $K=2G$, $\Gamma_{bulk}\to-1$). VERIFIED the two coincident-but-distinct $\Gamma=-1$ walls at `resonant-lc-solitons.md:89-94` + `master-equation.md:20`. PROPOSED — consistency re-expression, not new physics. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** *(cite excerpts, byte-exact at the cited lines — appended because the R40-B2a stamp modified this line and `verify-new-cite-excerpts` re-classifies its pre-existing cites as added: `EM-transverse | $Z_{\mathrm{EM}} \equiv Z_0$ | $\approx 376.73\,\Omega` · `**Class-invariant FORMS (carry no electron value):** the pol` · `**🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVE`)*

---

## confinement surface
<!-- id: def-cf1srf -->

- **term:** confinement surface
- **adjudicated-meaning:** the $\Gamma=-1$ cage-wall $\partial\Omega$ that terminates the bulk channel of a `BoundResonator`, whose **SHAPE is FORCED by topology** — the real-space body + the phase-space winding + the node-span — and is therefore **DERIVED, never posited-spherical** (Grant D4). The electron ($0_1$ unknot) and the proton ($6^3_2$ Borromean, multi-node) get DIFFERENT derived shapes.
- **axis:** real-space (a closed 2-surface in the substrate); its shape is set jointly with the phase-space winding label.
- **dimension/type:** a closed orientable 2-surface (geometry); the impedance condition on it is $Z_{core}\to0\Rightarrow\Gamma_{bulk}=-1$ (dimensionless reflection coefficient).
- **status:** proposed — status OPEN: the shape-forcing CHAIN is not derived (no solved boundary-value problem produces the electron's surface from its topology; the proton single-vs-multi-node confinement is UNADJUDICATED). The $\Gamma=-1$ TIR condition itself is canonical (clm-kezk9z, T3.3 `sup-1ecv2m`); the SHAPE is the open object.
- **canonical-home:** `vol9/ch3-pin-port-configuration/device-circuit-models.md` §6.2; the underlying $\Gamma=-1$ TIR wall is canonical at `resonant-lc-solitons.md:25-52`.
- **clm-cross-links:** *(none — gate-register reference; the wall claim is clm-kezk9z)*
- **open-ambiguity-flag:** YES — **two coincident $\Gamma=-1$ walls guard.** The confinement surface is the **A1 MASS wall** ($Z_{bulk}\to0$, the impedance-short $\Gamma=-1$). It must NOT be re-collided with the **$\Gamma_{spinor}=-1$** topological $2\pi\to4\pi$ stability wall of the T2 micro-rotation sector — these are numerically coincident at $-1$ but **distinct objects** ($A1\perp T2$, `master-equation.md:20`, `resonant-lc-solitons.md:89-94`). The electron carries BOTH; the confinement surface is the mass one only.
  - conflicting sites: the two-$\Gamma$ Resultbox `resonant-lc-solitons.md:89-94`; the A1$\perp$T2 anchor `master-equation.md:20`; the boundary-observable surface $\partial\Omega$ `common/boundary-observables-m-q-j.md:29`.
- **verification:** VERIFIED the $\Gamma=-1$ TIR confinement at `resonant-lc-solitons.md:38,47-50`; VERIFIED the A1-mass-wall vs T2-spinor-wall distinction (both $-1$, not the same wall) at `resonant-lc-solitons.md:89-94` + `master-equation.md:20`; VERIFIED the electron $0_1$-unknot vs proton-Borromean real-space bodies at `common/boundary-observables-m-q-j.md:43-44`. OPEN — shape-forcing chain not derived.

---

## V_yield / V_snap *(SOLID — adjudicated T2, Grant 2026-06-30)*
<!-- id: def-vyvsn1 -->

- **term:** V_yield / V_snap (the two Axiom-4 saturation thresholds)
- **adjudicated-meaning:** two voltage thresholds on the Axiom-4 saturation kernel, in **two orthogonal sectors** ($A_1 \perp T_2$). **$V_{\text{yield}} = \sqrt{\alpha}\cdot V_{\text{snap}} \approx 43.65$ kV** = the **transverse Cosserat ($T_2$) self-trap wall** (Grant 2026-06-30 ruling): the transverse micro-rotation crosses Axiom-4 onset, $\Gamma\to-1$, and the single-electron confining $\Gamma=-1$ TIR cavity self-creates here. **$V_{\text{snap}} = m_e c^2/e \approx 511$ kV** = the **longitudinal $A_1$ sector fully saturates** ($A^2=1$, $Z_{\text{core}}\to0$, the A1 varactor bond compliance $C_{\text{eff}}=C_0/S$ diverges HERE); this is the mass-completion + Schwinger / pair-nucleation energy. **The A1 mass channel does NOT saturate at $V_{\text{yield}}$** — it saturates at the $1/\sqrt\alpha\approx11.7\times$-higher $V_{\text{snap}}$.
- **axis:** sectoral saturation thresholds (transverse-T2 self-trap onset vs longitudinal-A1 completion)
- **dimension/type:** voltage (both); BOTH are **CALIBRATION, not derived** ($V_{\text{snap}}\equiv m_e c^2/e$ definitional with $m_e$ in voltage units; $V_{\text{yield}}\equiv\sqrt{\alpha}\cdot V_{\text{snap}}$, the $\sqrt{\alpha}$ being the imported $\alpha$-echo). `src/ave/core/constants.py:455` (V_SNAP), `:464` (V_YIELD).
- **status:** SOLID — adjudicated (Grant 2026-06-30). The formerly-BLOCKING grade-attribution fork is RESOLVED = T2: $V_{\text{yield}}$ is the transverse-$T_2$ self-trap wall; the longitudinal-A1 compliance bound is at $V_{\text{snap}}$. Canonized in prose at `pair-production-axiom-derivation.md:93-104` (T2 horn) and reconciled at `nonlinear-vacuum-capacitance.md:16` (A1 horn re-keyed to $V_{\text{snap}}$).
- **canonical-home:** `pair-production-axiom-derivation.md:93-104` (sectoral prose, Grant 2026-06-30 T2 ruling); `nonlinear-vacuum-capacitance.md:16` (A1 varactor keyed on $V_{\text{snap}}$); `src/ave/core/constants.py:455,:464` (calibration); the electron-binding derivation `research/2026-06-30_electron-portmap-derivation_result.md` §5.
- **clm-cross-links:** *(none verified-specific yet)*
- **open-ambiguity-flag:** **PARTIAL — the sector fork (2) is RESOLVED; the α-lock (1) STANDS as an honest caveat.** **(1) ALPHA-LOCK, not two free thresholds (STANDS):** $V_{\text{yield}}/V_{\text{snap}} = \sqrt{\alpha}\approx0.0854$ EXACTLY (`constants.py:464`). They are NOT two independent per-sector thresholds — the transverse-$T_2$ onset sits at $\sqrt{\alpha}$ of the longitudinal-$A_1$ scale. Do NOT import "one free threshold per sector"; the $\sqrt{\alpha}$ relation is itself a VALUE-level $\alpha$-echo. **Consequence of the ruling:** the electron's A1 mass core operates at strain $A=V_{\text{yield}}/V_{\text{snap}}=\sqrt\alpha$ — an $\alpha$-echo operating point (Class-C), sub-saturated ($S(\sqrt\alpha)=\sqrt{1-\alpha}\approx0.996$), which is why the mass channel does not run away. **(2) sector-attribution fork — RESOLVED = T2 (Grant 2026-06-30):** the earlier conflict — KB leaf `nonlinear-vacuum-capacitance.md:16` had the $V_{\text{yield}}$ varactor on the LONGITUDINAL-A1 bond compliance, while `constants.py` + `pair-production-axiom-derivation.md:102` put $V_{\text{yield}}$ on the TRANSVERSE-$T_2$ self-trap — is now settled: **$V_{\text{yield}}$ is the T2 wall**; the A1 varactor's divergence was re-keyed to $V_{\text{snap}}$, removing the conflict. **(3) keep DISTINCT** from the C_eff/ε_eff saturation-reactance sector split at `ave-kb/CLAUDE.md:73` (a different object — the saturation reactances, not the two-event threshold ladder).
- **verification:** VERIFIED the Grant 2026-06-30 T2 ruling landed in prose at `pair-production-axiom-derivation.md:93-104`; VERIFIED the A1-horn reconciliation (varactor re-keyed $V_{\text{yield}}\to V_{\text{snap}}$) at `nonlinear-vacuum-capacitance.md:16`; VERIFIED the calibration definitions at `constants.py:455,:464` and the $V_{\text{yield}}=\sqrt{\alpha}\cdot V_{\text{snap}}$ alpha-lock ($\sqrt\alpha=0.0854$). Status SOLID — fork (2) resolved, α-lock (1) retained as caveat. See `research/2026-06-30_electron-portmap-derivation_result.md` + `research/2026-06-24_engine-reroute-epic-summary.md`.

---

<!-- PROPOSED CANDIDATE — awaiting Grant ratification; NOT yet canonical. status:proposed, GATED on auditor + Grant. Coined 2026-07-03 for the A2 KEEP-BOTH ruling. Verified 0 prior corpus hits for the surface form 'B_dual' / 'B_DUAL' / 'b_dual'. B_yield was NOT used because it is already OVERLOADED in the corpus (Sense A = B_SNAP in the fdtd engine/tests/prose; Sense B = E_yield/c in the facility survey) — see open-ambiguity. -->

## B_dual *(proposed — the E_yield/c duality scale)*
<!-- id: def-bdual1 -->

- **term:** B_dual ($\equiv E_{\text{yield}}/c$)
- **adjudicated-meaning:** *(PROPOSED, gated)* the **duality image of the transverse-$T_2$ electric yield wall** — the magnetic field-scale obtained by applying the $cB \leftrightarrow E$ field-scale duality to $E_{\text{yield}} \approx 1.13\times10^{17}$ V/m, i.e. $B_{\text{dual}} \equiv E_{\text{yield}}/c \approx 3.77\times10^8$ T. It is the **field-amplitude-matched** magnetic scale, answering *"what is the duality image of the T2 yield wall?"* — DISTINCT from **$B_{\text{SNAP}} \approx 1.89\times10^9$ T** (the `constants.py` symbol `B_SNAP`), the **energy-density-matched** scale defined by $B_{\text{SNAP}}^2/(2\mu_0) = m_ec^2/\ell_{node}^3$, which answers *"what B stores the cell's rest energy in field-energy-density form?"*. **KEEP-BOTH (Grant 2026-07-03):** the two are BOTH correct and answer DIFFERENT questions; they are related by the derived, α-free bridge $B_{\text{SNAP}}/(E_{\text{yield}}/c) = c\,B_{\text{SNAP}}/E_{\text{yield}} = \sqrt{8\pi} = 5.013257$ (clm-bdualb, `research/2026-07-03_bsnap-byield-sqrt8pi-dissolution.md`). **Neither** is the Route-C static-B μ-kernel argument (circulation-keyed, $I_{vac}=0$); the R3 verdict $A_I=0 \Rightarrow \delta n_\mu=0$ is untouched by the choice of B-scale.
- **axis:** other (a magnetic field-scale; the duality image of the T2 electric yield wall)
- **dimension/type:** magnetic flux density (T); $B_{\text{dual}} = E_{\text{yield}}/c = \sqrt{\alpha}\,E_S/c$, so it inherits the $\sqrt{\alpha}$ echo of $E_{\text{yield}}$ (`src/ave/core/constants.py:475` `E_YIELD`, `:481` `B_SNAP`).
- **status:** proposed — VERIFIED **0 prior corpus hits** for `B_dual`; a coinage is NEVER seeded SOLID (INVARIANT-S12). GATED on auditor + Grant ratification.
- **canonical-home:** *(none — coinage; the underlying scale is `E_YIELD/c` from `src/ave/core/constants.py:475`; the KEEP-BOTH ruling + √(8π) bridge at `research/2026-07-03_bsnap-byield-sqrt8pi-dissolution.md` and `vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md` §1 flag-resolution block)*
- **clm-cross-links:** clm-bdualb (the √(8π) bridge identity), clm-pvlas1 (the static-B verdict leaf that hosts the ruling)
- **canon-noun map:** `B_dual` is a NON-CANON engineering name for the field-amplitude-matched magnetic scale `E_yield/c`; it MUST NOT be noun-swapped for `B_SNAP` (the energy-density scale) — the two differ by the √(8π) bridge. Cross-link: `def-vyvsn1` (the $V_{\text{yield}}/V_{\text{snap}}$ ladder $B_{\text{dual}}$ is the magnetic duality image of).
- **open-ambiguity-flag:** YES — the RELATED surface form **`B_yield` is overloaded in the corpus in TWO conflicting senses**, which is exactly why `B_dual` (not `B_yield`) was coined for this scale:
  - (a) **`B_yield = B_SNAP`** (the ENERGY-DENSITY scale): the fdtd engine parameter `b_yield` **defaults to `B_SNAP`** (`src/ave/core/fdtd_3d_jax.py:81`, `src/tests/test_vca_r01_static_b_mu_keying.py:26`, `src/tests/test_vca_node_regime_sweep.py:18`); prose "b_yield = B_SNAP" at `vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md:370`; `constants.py:520` comment ("r = V/V_yield (or B/B_yield)"). [energy-density scale] — **kept as-is** (these correctly mean B_SNAP); disambiguation comments pointing at `def-bdual1` added at `fdtd_3d_jax.py:81` docstring + `constants.py:520` comment (2026-07-03) so the Sense-A meaning is explicit at the engine params.
  - (b) **`E_yield/c = 3.77×10⁸ T`** (the DUALITY scale, = THIS node's `B_dual`): **RESOLVED (2026-07-03, PR #476 follow-on hygiene)** — the survey `research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md` (3 raw uses) is now **retagged `B_yield → B_dual`**, values unchanged. The only remaining `B_yield` mentions in that doc are inside its own scale-name tag block, where the overloaded form is quoted deliberately to document the retag. [duality scale]
  - conflicting sites: (a) `src/ave/core/fdtd_3d_jax.py:81`, `src/tests/test_vca_r01_static_b_mu_keying.py:26`, `node-up-small-large-signal.md:370`, `constants.py:520` — **Sense-A, kept** (now carry `def-bdual1` disambiguation comments at the two engine-param sites). (b) ~~`research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md:27,140,162`~~ — **retagged `B_dual`, no longer a conflicting site (2026-07-03).** The follow-on hygiene retag flagged here is now DONE; the sense-(b) conflict is cleared.
- **verification:** VERIFIED **0 prior corpus hits** for `B_dual` / `B_DUAL` / `b_dual` across `manuscript/`, `research/`, `src/` (2026-07-03). VERIFIED the √(8π) bridge numerically against `src/ave/core/constants.py` to rel 3.3e-11 (< 1e-8), α cancels (clm-bdualb, research note §3). VERIFIED the `B_yield` overload: Sense A (=B_SNAP) at the engine/test sites above; Sense B (=E_yield/c) at the facility-survey sites above. **GATED on auditor + Grant — NOT adopted, NOT SOLID.**

---

## chiral circulator
<!-- id: def-ch1crc -->

- **term:** chiral circulator
- **adjudicated-meaning:** the bipartite **A/B-sublattice NON-RECIPROCAL coupling** that carries the $I4_1 32$ lattice chirality between the two sublattice **TANKS** (an INTER-tank coupling, NOT a per-node C-vs-L reactance), drawn in the equivalent-circuit MODEL as a circulator element.
- **axis:** other — a non-reciprocal two-port coupling element in the equivalent-circuit model (sourced by the lattice chirality `def-7c3f9e`).
- **dimension/type:** circuit two-port (non-reciprocal scattering); dimensionless $S$-parameters.
- **status:** proposed — status STATED, pending the chiral-crystal engine. The cubic-FDTD engine averages chirality out; the non-reciprocity MAGNITUDE needs the chiral-crystal engine (`cvr_model.py:243` AUDITOR_STATE note). NOT adjudicated, NOT available.
  - **↗ First geometry-derived magnitude for the MECHANICAL sibling (2026-07-04, PR #508).** The **acoustic** (mechanical) analog of this non-reciprocal inter-tank coupling — the chiral micropolar translation↔rotation coupling $B$ on the srs-z3 net (a girth-10 inter-node effect: consecutive bond-planes rotate along the $4_1$ screw axis, vanishing identically on centrosymmetric diamond) — is now **geometry-fixed with zero new knobs** and has its first computed magnitude: $B_{\text{inv}}\sim10^{-2}$, carried on the $\sigma^A$ lever-arm channel ($B_{\sigma^A}\approx1.05\times10^{-1}$ dominating the couple-stress $\kappa_{rot}$ channel $B_\mu\approx5.4\times10^{-33}$ by $\sim$30 OOM), parity-odd (exact enantiomorph sign-flip). This is the k-space Bloch face of the same non-centrosymmetry that sources the chiral circulator. **KEEP-BOTH:** the **EM** non-reciprocity $S$-parameter magnitude (the circuit two-port this def- names) remains SEPARATELY pending the chiral-crystal EM engine — the mechanical sibling's magnitude does NOT supply it. Provenance: `research/2026-07-04_srs-chiral-micropolar_result.md` §2a, §7; module `src/ave/core/micropolar_bloch.py`.
- **canonical-home:** `vol9/ch3-pin-port-configuration/device-circuit-models.md` §6.3.
- **clm-cross-links:** *(none — STATED frontier; no clm- node may be authored)*
- **open-ambiguity-flag:** YES — **do NOT call it "gyrator."** The reciprocal optical-activity gyrator (`def-0pt1ac`, the lossless reciprocal-Faraday polarization-plane rotator, $\pm75.46°$/unit) is a DIFFERENT element; "circulator" is reserved here for the non-reciprocal inter-tank coupling. Also DISTINCT from the **per-particle** $S_{LR}\ne S_{RL}^*$ winding non-reciprocity (`cvr_model.py:242`), which is a single-instance scattering asymmetry, not the inter-sublattice-tank coupling.
  - conflicting sites: the reciprocal gyrator `def-0pt1ac` (`vocabulary-register.md:522`); the per-particle winding non-reciprocity `cvr_model.py:238-243`; the lattice chirality source `def-7c3f9e`.
- **verification:** VERIFIED the reciprocal-gyrator collision risk — `def-0pt1ac` is explicitly a *reciprocal*-Faraday gyrator (`vocabulary-register.md:526`), so "gyrator" is the wrong word for a non-reciprocal element. VERIFIED the per-particle $S_{LR}\ne S_{RL}^*$ winding non-reciprocity is a DISTINCT (single-instance) object at `cvr_model.py:242` ("the L<->R conversion NON-RECIPROCAL (S_LR != S_RL*)"), engine-pending at `cvr_model.py:243`. STATED — pending chiral-crystal engine.

---

## chord (FORM-deriving)
<!-- id: def-ch0rd1 -->

- **term:** chord
- **adjudicated-meaning:** a **forced dimensionless FORM** — a structural / topological feature the substrate **independently forces** from its geometry (removing a degree of freedom), so its truth does not rest on any imported numerical value. The "FORM-deriving" half of the FORM-vs-VALUE organizing principle. Machine-encoded as the interlock register's `real_or_fitted = real-geometric-constraint` tag (INVARIANT-S13).
- **axis:** dimensionless
- **dimension/type:** dimensionless (a structural/topological form, not a magnitude)
- **status:** SOLID (organizing-principle adjudication 2026-06-14 → 2026-06-18, Grant-ratified)
- **canonical-home:** [`form-deriving-value-importing.md`](form-deriving-value-importing.md) "The principle"; CI-gated counterpart [`interlock-register.md`](interlock-register.md) (`real-geometric-constraint`)
- **clm-cross-links:** *(cross-cutting organizing principle — no single load-bearing clm-; the per-mechanism chord/echo tags live on `ilk-` nodes, not `clm-`)*
- **open-ambiguity-flag:** YES — "chord" is also used in the literal music/harmony metaphor ("real chord or echo?") of the `determinism → emergent` north-star, and as the geometric chord of a circle. The adjudicated sense here is the **forced-FORM** classification; qualify as "chord (FORM)" at first cite in a value-provenance context.
  - conflicting sites: the harmony-metaphor north-star usage `common/genesis-chord-falsification-ledger.md` (chord/echo falsification framing); the geometric-chord usage in golden-torus geometry `vol1/ch8-alpha-golden-torus.md` (ropelength/Clifford-torus context).
- **verification:** VERIFIED against the interlock register's `real_or_fitted` axis (`interlock-register.md:21,51-64`, INVARIANT-S13) — `real-geometric-constraint` = "the substrate independently forces the relation, so it removes one DOF" = the chord side. This `def-` locks the prose label to that CI-gated tag.

---

## echo (VALUE-importing)
<!-- id: def-ech0v1 -->

- **term:** echo
- **adjudicated-meaning:** an **imported / calibrated dimensionful VALUE** — a named identification or back-solved magnitude the substrate does **NOT** independently select (it buys no parameter reduction; it is a consistency match, not an emergence). The "VALUE-importing" half of the FORM-vs-VALUE organizing principle. Machine-encoded as the interlock register's `real_or_fitted = fitted-identification` tag (INVARIANT-S13). Canonical instance: the α *value* (closed-negative on all three named lift-routes; flip-condition live, route-space not provably exhausted).
- **axis:** dimensionless
- **dimension/type:** classifies a dimensionful magnitude's provenance (the tag is dimensionless; the classified value carries its own dimension)
- **status:** SOLID (organizing-principle adjudication 2026-06-14 → 2026-06-18, Grant-ratified)
- **canonical-home:** [`form-deriving-value-importing.md`](form-deriving-value-importing.md) "Per-constant accounting"; CI-gated counterpart [`interlock-register.md`](interlock-register.md) (`fitted-identification`)
- **clm-cross-links:** *(cross-cutting organizing principle — the per-mechanism echo tags live on `ilk-` nodes, e.g. `ilk-rr14gt` for α, not on a `clm-`)*
- **open-ambiguity-flag:** YES — "echo" is also the literal acoustic/RF echo (a reflected wave) and the north-star harmony metaphor ("real chord or echo?"). The adjudicated sense here is the **imported-VALUE** classification; qualify as "echo (VALUE)" at first cite in a value-provenance context.
  - conflicting sites: the harmony-metaphor north-star usage `common/genesis-chord-falsification-ledger.md`; reflected-wave usages throughout the EE/impedance corpus (e.g. `Γ` reflection contexts).
- **verification:** VERIFIED against the interlock register's `real_or_fitted` axis (`interlock-register.md:51-64`, INVARIANT-S13) — `fitted-identification` = "a named identification the substrate does NOT independently select — a consistency match that buys NO parameter reduction" = the echo side. α's `ilk-rr14gt` carries this tag (`interlock-register.md:90`); the α-value + downstream predictions are UNCHANGED by the echo close (`vol1/ch8-alpha-golden-torus.md:13`).

---

## mixed (form-derived / value-fitted)
<!-- id: def-fmv001 -->

- **term:** mixed
- **adjudicated-meaning:** a **form-derived FORM combined with a value-fitted VALUE** — the substrate derives the *form* of a mechanism but takes the *value* of its calibration termination as an input. **The canonical instance is G** (the Achromatic-Lens `/7` PPN form is derived; the ξ termination is back-solved from CODATA G). **`mixed` is NOT a pure echo** — its derived-form half is real and must be preserved; a mixed mechanism's value-fitted half counts as an echo for the parameter count only until its flip-test closes form-first. E_yield is a second `mixed` instance (saturation-field EXISTENCE = chord; the √α value = α-echo since `e = √α` in natural units).
- **axis:** dimensionless
- **dimension/type:** classifies a mechanism's provenance (form half + value half)
- **status:** SOLID (G-ruling 2026-06-14, Grant-ratified; E_yield adjudication `wlmbl6d5f` 2026-06-20)
- **canonical-home:** [`form-deriving-value-importing.md`](form-deriving-value-importing.md) "Per-constant accounting"; CI-gated counterpart [`interlock-register.md`](interlock-register.md) (`mixed`, `ilk-gravmb`)
- **clm-cross-links:** *(cross-cutting; the G `mixed` tag lives on `ilk-gravmb`, not on a `clm-`)*
- **open-ambiguity-flag:** no — "mixed" is used only in this form-derived/value-fitted sense across the value-provenance corpus.
- **verification:** VERIFIED against the interlock register's `real_or_fitted` axis (`interlock-register.md:57-64`, INVARIANT-S13) — `mixed` = "form-derived / value-fitted (G): the FORM is derived … but the VALUE is a calibration input." COUNT SEMANTICS confirmed: `mixed` and `fitted-identification` BOTH do not reduce the count; only `real-geometric-constraint` reduces (`interlock-register.md:61-63`). G's `ilk-gravmb` carries `mixed` (`interlock-register.md:129`). **NEVER call G a pure echo** — the per-constant table at `form-deriving-value-importing.md` and the G-ruling both require the `mixed` verdict.

---

## open-loop (calibration-role)
<!-- id: def-0penlp -->

- **term:** open-loop (role) — the seventh `calibration_role` value
- **adjudicated-meaning:** a **form-forced FORM whose VALUE is computed from a declared calibration input measured in a *different* experiment, with the output never fit to the observable being predicted**. The discriminator is the feedback question — *"was the observable being predicted used to set any input?"* — NOT *"does α appear?"*: an α-riding value can be open-loop when α was measured elsewhere and nothing about the target observable tuned the computation. EE-native: the standing control-topology word for exactly this no-feedback shape.
- **axis:** value-provenance (peer of `chord`/`echo`/`mixed`/`fitted`/`consistency`/`forward-prediction` on the `calibration_role` axis; orthogonal to `type` per the 2026-08-05 ruling)
- **dimension/type:** classifies a manifest row's value-provenance topology
- **status:** proposed (the ruling's word was OPEN, which the register enum lacks; `proposed` is its conservative mapping per the register's own :41 convention — blind-read F6. Grant's one word upgrades to SOLID. Name + mint Grant-ratified, Wave-2 sitting 2026-08-18, D11; docket `2026-08-18-wave2-adjudication-sitting.md`); **role starts EMPTY** — no row carries it at mint. Per-row reclassification is a later deliberate pass with the reconciler census re-measured before landing (the #966 lesson: never change a gating vocabulary and its population in one motion).
- **canonical-home:** the `calibration_role` schema comment in both manifests (`manuscript/predictions.yaml`, `manuscript/consistency-manifest.yaml`) + `ALLOWED_CALIBRATION_ROLES` in `src/scripts/predictions_manifest_validator.py`
- **clm-cross-links:** *(none at mint — the role is empty by ruling)*
- **open-ambiguity-flag:** YES — "open-loop" has standing corpus use in the (compatible) control-theory sense (50 lines / 25 files at 2026-08-19, `git grep -Ic -i`). Qualifier rule: write **"open-loop (role)"** at first cite in any doc where the control-topology sense could be read.
  - **CONFLICTING SITES (verified 2026-08-19):** `vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-stability-eigenmode.md:10` ("a Nyquist locus of the **open-loop resonator**" — loop-gain sense) and `:34` ("§3 — Nyquist: the open-loop resonator locus"); `common/translation-tables/translation-circuit.md:702` ("Finite open-loop gain $A_{OL}$"). All control-topology sense; none collides with the role sense when the qualifier rule is followed.
- **verification:** the reconciler deliberately does NOT auto-suggest this role (`suggest_role` never returns it) and NO provenance marker forbids it — in particular `VALUE_ECHOED` is COMPATIBLE: an echo-at-value-level computed from an independently-measured calibration input *is* the open-loop shape. Deliberate decision recorded at mint, Wave-2 D11.

---

## T₂ (photon-family disambiguation)
<!-- id: def-t2ph01 -->

- **term:** T₂ (the tetrahedral-group triplet label — TWO physically-distinct objects share it, separated by the massless-vs-gapped mass status)
- **adjudicated-meaning:** the **default canonical "T₂ = the photon" sense is the massless transverse-TRANSLATIONAL mode pair (u-family)** — the two massless transverse-shear branches at $c = \sqrt{G/\rho}$ whose eigenvectors are u-dominated (translational). The glyph T₂ is overloaded in the corpus by a *second* object — the **Cosserat microrotational (ω) family** (gapped, mechanical, the static (2,3) winding's home) — historically ALSO called "the photon." Per the G2 ruling (Grant 2026-07-03) the photon is sense (1); the node ω is sense (2), NOT the photon. This node is the canonical disambiguation + mis-use watch-list.
- **axis:** spatial-Brillouin (band-family label on the K4 two-sublattice dispersion)
- **dimension/type:** DOF-family label (n/a — classifies which Cosserat sector a mode lives in); the modes themselves are frequency ($T^{-1}$)
- **status:** SOLID (for the locked "photon = transverse-translational u-family" sense; the disambiguation is Grant-adjudicated 2026-07-03, so the canonical sense seeds SOLID — status and open-ambiguity are orthogonal per the `node`/`ξ` precedent)
- **canonical-home:** sense (1) the photon = transverse-translational u-family: `research/2026-07-03_g2-photon-relabel_note.md` (ruling) + `photon-identification.md:11` (with the G2 relabel note); the decisive eigenvector read at `src/scripts/vol_1_foundations/g2_photon_eigvec_composition.py` / `manuscript/vol_1_foundations/results/g2_photon_eigvec_composition.json`. sense (2) the gapped mechanical ω: `cosserat-mass-gap.md` §4 ($m^2 = 4G_c/I_\omega$); `clm-wcoul2` (Yukawa-screened winding pair).
- **clm-cross-links:** clm-g0mkne (Cosserat rotational mass mechanism — carries the G2-RESOLVED photon-family note), clm-j550uh + clm-9kd2t3 (k4-port irrep decomposition), clm-wcoul2 (gapped-ω winding-pair Coulomb), clm-kmliqx (c_R = √2 rotational curvature speed)
- **open-ambiguity-flag:** YES — the surface label T₂ names TWO distinct objects:
  - (1) **the transverse-TRANSLATIONAL mode pair (THE PHOTON's family, MASSLESS)** — the two massless transverse-shear branches, u-dominated (ω-fraction → 0 at k→0: Step-1 rider reads $2.5\times10^{-7}$; u-fraction $= 1.000000$), propagating at $c = \sqrt{G/\rho}$. Its magnetic content = the **EM-inductive circulation of the u-wave** (bond-level curl $\nabla\times u$, the Axiom-1 μ₀-family B), NOT a node micro-rotation.
  - (2) **the Cosserat MICROROTATIONAL (ω) family (GAPPED, mechanical, the winding's home)** — ω-dominated (ω-fraction $= 1.000000$), gapped at $m^2 = 4G_c/I_\omega$ (the mechanical Cosserat mass; Yukawa-screened, short-range, `clm-wcoul2`); the home of the *static* (2,3) winding topology. This is NOT the photon.
  - **The watch-list qualifier rule:** **never write bare "T₂" or "T₂ microrotational ω" for the photon** — the photon is the transverse-*translational* u-family. When a leaf says "T₂ … the photon" it means sense (1) (translational-u); when it says "T₂ … carries the mass-gap / the winding" it means sense (2) (gapped microrotational ω). The two are separated by the massless-vs-gapped mass status, which is the load-bearing distinction (not the free-vs-locked one).
  - **CONFLICTING SITES (verified 2026-07-03, now carrying G2 KEEP-BOTH relabel notes):** `photon-identification.md:11` ("Cosserat shear wave with $u=0$, $\omega\neq0$" — sense-2 label on the photon, CORRECTED to sense 1); `k4-port-irrep-decomposition.md:26` ("Microrotational ω … THIS IS THE PHOTON" — sense-2 label, CORRECTED); `cosserat-mass-gap.md:145` + `vol1/claim-quality.md:1131` (had the RIGHT family — sense 1 translational — with the gapped ω correctly as sense 2; G2-RESOLVED notes added).
- **verification:** VERIFIED — the massless-branch u-dominance ($\omega$-fraction $2.5\times10^{-7}$, u-fraction $1.000000$) and gapped-branch ω-dominance ($1.000000$) computed on the genuine two-sublattice A→B bond operator (`g2_photon_eigvec_composition.json`, k=1e-3, 4 directions); the operator is the same that recovers the gap $m^2 = 4$ bit-exact (V3, `research/2026-06-23_cosserat-band-structure-two-sublattice_prereg-result.md`). Ruling Grant 2026-07-03 (`research/2026-07-03_g2-photon-relabel_note.md`). Status SOLID for the locked "photon = transverse-translational u" sense; open-ambiguity records the T₂ overload (orthogonal per the SCHEMA Definition-record rule). NOTE (flag-don't-fix): the original GAP-G2 orchestration diagnosis (`_orchestration/2026-06-07_electron-synthesis-epic.md:319`) pinned "photon = microrotational ω" as canonical — the eigenvector read contradicts it, resolved AGAINST that side per the ruling.

---

## longitudinal split (∇·u dynamical vs ∇·A gauge)
<!-- id: def-l0ngdu -->

- **term:** the longitudinal-sector split — mechanical dilatation $\theta = \nabla\cdot\mathbf{u}$ (DYNAMICAL) vs the EM longitudinal $\nabla\cdot\mathbf{A}$ (GAUGE)
- **adjudicated-meaning:** *(ADJUDICATED distinction — **cold-linear sector-dynamics**; the SAME Helmholtz/Lamé longitudinal split applies to BOTH fields, so the difference is **constitutive**, not kinematic).* The **mechanical dilatation** $\theta = \nabla\cdot\mathbf{u}$ (with $\mathbf{u}$ = the node displacement field; $\theta$ = its volumetric/compression projection — the standard Helmholtz/Lamé split, the same split that gives seismology its P and S waves) is **DYNAMICAL**: it carries a genuine bulk restoring force $\tfrac12 K(\nabla\cdot\mathbf{u})^2$ ($K = 2G$) and rides the **gapless lattice-computed P-branch**. The **EM longitudinal** $\nabla\cdot\mathbf{A}$ is **GAUGE**: the curl-only EM Lagrangian gives it no restoring force. **One word each way — $\nabla\cdot\mathbf{u}$ propagates; $\nabla\cdot\mathbf{A}$ is gauge.** "Heaviside-excised" (the vector-calculus reformulation dropped $\nabla\cdot\mathbf{A}$) is a **historical/notational** statement about the *transverse EM* sector — NOT a dynamical gauge-kill of the A1 compression scalar. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**
- **axis:** other — sector-dynamics (the longitudinal channel of two distinct vector fields), cold-linear regime
- **dimension/type:** $\theta = \nabla\cdot\mathbf{u}$ is dimensionless volumetric strain (L/L); the adjudicated distinction is dynamical-vs-gauge, not a dimensional split
- **status:** SOLID (Grant-ratified 2026-07-20; #761 review-hardened, merged)
- **canonical-home:** [`master-equation.md`](../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):26 (the 2026-07-20 sector-dynamics tag; elaborates the A1 $\perp$ T2 anchor at [`:20`](../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md)) + `research/2026-07-20_mechanical-commonmode-derivation_result.md` §1.3/§5 (merged, review-hardened)
- **clm-cross-links:** *(none minted — #761 mints no `clm-`, propagates to no leaf, READ-ONLY on KB; cross-node: def-9a4f07 (longitudinal V-sector scalar), def-5d2b8a (the two "3"s), def-tk1xfm (TKI transducer))*
- **open-ambiguity-flag:** no — this node **adjudicates** the longitudinal split (it is not itself an overload record). ★ROUTED-OPEN on a SEPARATE axis: the u/A **transverse** identity-collapse candidate is OPEN (def-uatk1s; frontier queue, GW170817 two-distinct-signals gate); this node adjudicates the **LONGITUDINAL** split ONLY.
- **verification:** VERIFIED two-method (`grep -F` + direct read) at HEAD — the sector-dynamics tag verbatim at `master-equation.md:26` ("One word each way: **∇·u propagates; ∇·A is gauge.**"; "θ carries a genuine bulk restoring force (½K(∇·u)², K = 2G) on the gapless lattice-computed P-branch"); the #761 receipts at `research/2026-07-20_mechanical-commonmode-derivation_result.md` §1.3 (the Lagrangian-structure argument — the EM Gauss-kill is STRUCTURALLY BLOCKED from ∇·u) + §5 (the mass IS mechanical acoustic compression ∇·u — the fork-foreclosing fact). Status **SOLID** for the adjudicated longitudinal split.

---

## u vs A (counterpart sector variables, TKI)
<!-- id: def-uatk1s -->

- **term:** $\mathbf{u}$ vs $\mathbf{A}$ — the mechanical node-displacement field vs the EM vector potential, read as **counterpart sector variables** under the Topo-Kinematic Isomorphism
- **adjudicated-meaning:** *(SOLID 2026-07-21 — the def-tk1xfm ceiling it inherited is now lifted (Grant-ratified); the transverse identity-collapse stays ROUTED-OPEN on its own axis, see open-ambiguity. Prior "PROPOSED, gated" preserved per Rule 12 in status.)* Under the Topo-Kinematic Isomorphism (Axiom 2), $\mathbf{u}$ (the mechanical node displacement field) and $\mathbf{A}$ (the EM vector potential) are **COUNTERPART SECTOR VARIABLES** — isomorphic structure (kinetic / curl-potential twins; speed-degenerate transverse channels) — **NOT one field**. They differ in **constitutive stencil**: the longitudinal $\mathbf{u}_\parallel$ carries the K-spring ($\tfrac12 K(\nabla\cdot\mathbf{u})^2$, $K = 2G$, propagating P-branch — def-l0ngdu); the longitudinal $\mathbf{A}_\parallel$ has **no** restoring force (gauge). The isomorphism is **structure-preserving**, not a real-space identity of the two fields.
- **axis:** notation / other — cross-domain sector-variable mapping (mechanical vs EM), the Axiom-2 TKI dictionary
- **dimension/type:** $\mathbf{u}$ = length (L, displacement); $\mathbf{A}$ = EM vector potential (V·s·m⁻¹); the isomorphism is structure-preserving (units bridged by $\xi_{topo}$), not a dimensional identity
- **status:** SOLID (dated 2026-07-21) — the def-tk1xfm ceiling it inherited is **LIFTED** (`def-tk1xfm` proposed→SOLID, Grant-ratified 2026-07-21, `[sic]`: *"ratify def-tk1xfm"*); this node carries the same **below-band-edge co-equality scope**. The TKI transducer's *"identity-by-translation, NOT emerges-from / NOT a derivation"* strength ceiling **STILL STANDS** (`def-tk1xfm` :430 fuller form; exact short-form at `def-portmp` :496) — SOLID ratifies the mapping as canonical, it does not make it a derivation. **NOTE:** the SOLID upgrade is for the **LONGITUDINAL** counterpart-sector-variable content only; the **transverse identity-collapse** (open-ambiguity) is a SEPARATE axis, still **ROUTED-OPEN** (frontier queue, GW170817 gate). *(Prior status, preserved per Rule 12: **proposed** — inherited def-tk1xfm's proposed/PR#265 ceiling; verbatim then at `substrate-native-terminology.md:17` "the `def-tk1xfm` node is **proposed**, PR #265", now SOLID at that site. **NOT canon** — while tk1xfm was proposed.)*
- **canonical-home:** *(none — coinage; the underlying isomorphism is `eq_axiom_2.tex:12` + the dictionary table `translation-circuit.md:17-26` (clm-fy05jc); the TKI def node `def-tk1xfm` is SOLID, Grant-ratified 2026-07-21, was proposed since PR #265)*
- **clm-cross-links:** *(none verified-specific — the counterpart-sector mapping; cross-node: def-tk1xfm (TKI transducer, SOLID 2026-07-21), def-l0ngdu (the longitudinal split), def-5d2b8a (the two "3"s))*
- **open-ambiguity-flag:** ★ROUTED-OPEN — the u/A **transverse** identity-collapse candidate (are the EM and mechanical-transverse sectors two meters on ONE bench object, or two distinct fields?) is a **frontier-queue open question**, gated on the **GW170817 two-distinct-signals** observational test (bulk radiates at $\sqrt{10/3}\cdot c \approx 1.83c$ vs the $|\Delta v|/c \lesssim 10^{-15}$ coincidence bound — `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md` §2 item 1b). This register entry adjudicates the **LONGITUDINAL split ONLY** (def-l0ngdu); it takes **NO position** on the transverse collapse. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**
- **verification:** VERIFIED two-method (`grep -F` + direct read) at HEAD — `def-tk1xfm` is now **SOLID** (Grant-ratified 2026-07-21, `[sic]`: "ratify def-tk1xfm"; the `substrate-native-terminology.md:17` + `:83` status flipped proposed→SOLID in this same #781 repair pass); the *"identity-by-translation, NOT a derivation"* ceiling + the $\mathbf{u}\leftrightarrow$E / $\omega\leftrightarrow$B mechanical-port mapping in the def-tk1xfm register entry; the routed transverse-collapse gate at the frontier-queue doc §2 item 1b. Status **SOLID** for the **LONGITUDINAL** counterpart-sector-variable content (the tk1xfm ceiling lifted); the **transverse identity-collapse** is adjudicated NOWHERE yet, still routed to the frontier queue (a separate axis). *(Prior verification, preserved per Rule 12: cited the def-tk1xfm PROPOSED / PR #265 status wording verbatim at :17 + :83; status was proposed / NOT-canon while tk1xfm was proposed.)*

---

<!-- ============================================================
SUBSTRATE-NOUN ONTOLOGY BLOCK — Grant-ratified 2026-07-21
(verbatim [sic]: "i oike the plan lets fire that lane, 1) agree its an
identity not literal, 2) lets walk, 3) yup makes sense"; the bond grade
ratified mid-flight, verbatim [sic]: "yes rhat grade matches my perspective").
Eight core-noun def- nodes, each carrying the ontology-grade field (the
convention block at the top of this register). Grade legend: IDENTITY /
MODEL-OF / ANALOGY / IMPORT.
============================================================ -->

## crystal
<!-- id: def-cryst1 -->

- **term:** crystal / "the vacuum is a chiral Laves K4 Cosserat crystal"
- **adjudicated-meaning:** the Axiom-1 substrate noun **"crystal"** is a **structure commitment**, NOT a literal-material claim. It commits the K4/srs connectivity (chiral z=3 srs / Sunada-K4 / Laves net, $I4_1 32$ chiral space group), the six per-node Cosserat DOF grades (3 translational→E, 3 microrotational→B), the intrinsic per-node LC oscillator, and the constitutive relations that follow — and **nothing about a material the crystal is "made of"** (there is no substance under the structure; asking "what is the crystal made of?" regresses, and under phase-only epistemology the bulk self-cancels so only the structure is observable). ★**Consequence banked here (load-bearing):** because "crystal" commits STRUCTURE not SUBSTANCE, imports from materials science are **NOT blanket-licensed** by the word — each candidate import (yield, viscosity, plasticity, amorphousness, …) runs the per-import means-test **individually** (the leak-check + the law-vs-texture programs' operating assumption, now anchored here).
- **axis:** other — substrate-noun ontology (a structure commitment, not a glyph on a physical axis)
- **dimension/type:** n/a (a noun — the substrate structure, not a field or observable)
- **status:** SOLID (Grant-ratified 2026-07-21, verbatim `[sic]`: *"1) agree its an identity not literal"*)
- **ontology-grade:** **IDENTITY-AT-STRUCTURE-LEVEL** — the noun commits exactly the structural/constitutive relations; the only level at which "is" means anything under phase-only epistemology, and explicitly NOT a substance/material claim.
- **canonical-home:** `manuscript/common_equations/eq_axiom_1.tex:36-37` (the "chiral Laves K4 Cosserat crystal" identity, z=3 srs connectivity + 6-DOF Cosserat structure); the phase-only epistemology basis at [`form-deriving-value-importing.md`](form-deriving-value-importing.md):255,:265 + [`identity-break-test-design.md`](identity-break-test-design.md):110-111 (the bulk self-cancels — no direct observable).
- **clm-cross-links:** clm-q39qct (z=3 Scheme-A connectivity), clm-9s9apq (z=3 justification)
- **open-ambiguity-flag:** no — the structure-commitment sense is the single adjudicated sense. *(The surface form "K4" — distinct from "crystal" — carries its own three-referent overload at `def-4b1a2c`; the broader crystalline-vs-amorphous STRUCTURAL seam, also distinct from this ontology-grade ruling, stays open at `the-abandoned-interior.md:183`. Neither is an ambiguity of the crystal-as-structure-commitment ruling.)*
- **verification:** VERIFIED two-method (`grep -F` + direct read) at HEAD — the "chiral Laves K4 Cosserat crystal" identity + z=3 srs + 6-DOF Cosserat structure verbatim at `eq_axiom_1.tex:36-37`; the phase-only "bulk self-cancels / no direct observable" basis at `form-deriving-value-importing.md:255,:265` and `identity-break-test-design.md:110-111`. Grade IDENTITY-AT-STRUCTURE-LEVEL ★GRANT-RATIFIED 2026-07-21 (verbatim `[sic]` "agree its an identity not literal"). The per-import means-test consequence is the operating assumption of `substrate-native-terminology.md` §"the leak-check" — now anchored here.

---

## the impedance analogy (mechanical ↔ electrical convention)
<!-- id: def-1mpanl -->

- **term:** the impedance analogy — the corpus's mechanical↔electrical correspondence convention (stress ↔ voltage, velocity ↔ current)
- **adjudicated-meaning:** the corpus's mechanical-electrical analogy is **PINNED** globally as the **IMPEDANCE ANALOGY**: **stress ↔ voltage** ($V=\xi^{-1}F$), **velocity ↔ current** ($I=\xi v$) — the force-analogy (impedance) branch of the two dual analogies, matching the TKI dictionary rows (`translation-circuit.md:17-26`, clm-fy05jc). Under it, mechanical impedance $Z=\text{stress}/\text{velocity}$, so: **$Z\to0$ = short = pressure-release / free boundary = $\Gamma=-1$**, and **$Z\to\infty$ = open = rigid / clamped boundary = $\Gamma=+1$** (`translation-circuit.md:119` — "Short-circuit ($Z\to0$) … $\Gamma=-1$" vs the electric-branch "open-circuit ($Z\to\infty$) … $\Gamma\to+1$"). This is a **register commitment**: use this pairing everywhere; do not silently switch to the dual mobility analogy (force↔current) mid-derivation.
- **axis:** notation / other — a global sign/variable-pairing convention for the mechanical↔electrical correspondence
- **dimension/type:** n/a (a convention pinning; the paired quantities carry their own dimensions — stress Pa, voltage V, velocity m/s, current A)
- **status:** SOLID (Grant-ratified 2026-07-21, verbatim `[sic]`: *"3) yup makes sense"*)
- **ontology-grade:** **ANALOGY** — a means-tested, regime-scoped correspondence (the hub-and-spoke EE-spoke discipline). The pairing's *row-mapping* is underwritten by the TKI dictionary, which is IDENTITY-by-translation below the band edge (`def-tk1xfm`); the **choice of WHICH dual analogy** (impedance vs mobility) is the convention this node pins.
- **canonical-home:** `translation-circuit.md:17-26` (the $\xi_{topo}$ dictionary rows $V=\xi^{-1}F$, $I=\xi v$; clm-fy05jc); `translation-circuit.md:119` (the $Z\to0$ short / $\Gamma=-1$ vs $Z\to\infty$ open / $\Gamma=+1$ reading; clm-lv3uw1)
- **clm-cross-links:** clm-fy05jc (the $\xi_{topo}$ dictionary), clm-lv3uw1 (the $\Gamma=-1$ short / $\Gamma=+1$ open branches)
- **open-ambiguity-flag:** no — the convention is pinned to one sense. **Five-instance sign-trap history this retires (recorded as the motivation for pinning, KEEP-BOTH — not open ambiguities):** (1) clamped-vs-free boundary sign; (2) the skill-row fix; (3) the impedance reading; (4) the comb phase; (5) the RVE vessel state — each a recurrence of the same short/open ↔ free/rigid ambiguity the pinned convention forecloses.
- **verification:** VERIFIED two-method at HEAD — the dictionary rows $V=\xi^{-1}F$ (voltage↔force/stress), $I=\xi v$ (current↔velocity) at `translation-circuit.md:17-26` (clm-fy05jc; "identity statements … not analogies" at :41); the $Z\to0$ short/$\Gamma=-1$ and $Z\to\infty$ open/$\Gamma=+1$ mapping at `translation-circuit.md:119` (clm-lv3uw1). ★GRANT-RATIFIED 2026-07-21 (verbatim `[sic]` "yup makes sense"). Grade ANALOGY (the impedance-vs-mobility choice is a convention; the row-mapping itself is TKI-identity below the band edge, `def-tk1xfm`).

---

## bond
<!-- id: def-b0nd01 -->

- **term:** bond ("bond = transmission-line segment")
- **adjudicated-meaning:** the substrate **BOND** noun (a K4/srs lattice edge) is an **IDENTITY-at-structure-level** commitment: **three propagating coupling channels + one gapped Cosserat couple-stress $\gamma$-grade** (`port-register.md:47-50`; parameterized constitutively by the stretch/bend/twist stiffness triple — axial $k_a$ / shear $k_s$ / couple-stress $\gamma_c$: `axiom-register.md:189` [$\rho=k_a/k_s$ stretch/bend], `vol9/ch9-mechanical-characteristics/index.md:11` [$\gamma_c$] — the $k_a/k_s/\gamma_c$ stiffness triple and the 3+1 port rows are two projections of the same edge), a **unitary node scatter** (power-conserving vertex, $|\Gamma|^2+|T|^2=1$), and a **finite per-cell delay** ($\tau=\sqrt{L_{cell}C_{cell}}=\ell_{node}/c_0$). The phrase **"transmission-line segment"** is grade **MODEL-OF, REGIME-SCOPED**: a *per-channel* projection (a TL is one-mode; the bond is three-channel), **exact in the propagating long-wave regime** ($\omega\tau\ll1$) and native to the EM-sector engines — each K4/srs bond **is** a lossless transmission-line span (`z0-derivation.md:98,:115`, clm-mfb2ax; the lumped node is the $\omega\tau\ll1$ limit of the distributed bond; distributed-vs-lumped ABCD first diverge at $O(\theta^2)$). ★**At band-edge scales the corpus-adjudicated arccos band top $\omega=\omega_{\text{link}}\arccos(\mu/3)$ (`srs-band-structure.md` §2, clm-bnd5rq, gates #604/#607) IS the DISTRIBUTED / transmission-line (TLM) bond description, which stays EXACT through the band edge; the LUMPED mass-spring description ($\omega=\sqrt\lambda$, band top $\sqrt{12}$) is the long-wave approximation that BREAKS DOWN there** (it fails the frozen $1/\sqrt3$ velocity gate). The two descriptions **book the delay differently** (distributed-in-bond vs emergent-from-chain) and are **co-equal only BELOW the band edge** (where lumped↔distributed coincide). `def-tk1xfm`'s TKI co-equality carries exactly this band-edge scope (ratified 2026-07-21). **★Correction (2026-07-21, #781 review):** the original inverted label — the arccos band top paired with the *lumped* mass-spring description — came from the orchestrator walk and was caught by this review; the ratified GRADE (IDENTITY-at-structure-level + MODEL-OF regime-scoped) is unaffected (the reviewer's carve).
- **axis:** other — substrate-noun ontology (a lattice edge / coupling element; its channels carry speeds $L\,T^{-1}$)
- **dimension/type:** n/a as a noun; the channels carry stiffnesses/impedances ($k_a,k_s$, couple-stress $\gamma_c$) and a one-span delay $\tau=\ell_{node}/c_0$ [T]
- **status:** SOLID — bond grade ★GRANT-RATIFIED 2026-07-21 (verbatim `[sic]`: *"yes rhat grade matches my perspective"*; the walk was delivered 2026-07-21 and Grant read + ratified it same day, superseding the DRAFTED-PENDING-GRANT status).
- **ontology-grade:** **IDENTITY-at-structure-level** (the bond noun: three propagating channels + one gapped $\gamma_c$-grade, unitary node scatter, finite per-cell delay) **/ MODEL-OF, REGIME-SCOPED** (the "transmission-line segment" projection: per-channel, exact in the propagating long-wave regime, EM-native; at the band edge the LUMPED mass-spring approximation breaks down and only the DISTRIBUTED arccos-TL description stays exact — the two book the delay differently, co-equal only below the band edge).
- **canonical-home:** `z0-derivation.md:98,:115` (the bond as a distributed transmission line; ABCD identity; lumped = $\omega\tau\ll1$ limit; clm-mfb2ax); `port-register.md:47-50` (the three orientation-resolved channels); `srs-band-structure.md` §1-§2 (the arccos band top + the distributed-arccos-vs-lumped model adjudication; clm-bnd5rq); `axiom-register.md:189` ($\rho=k_a/k_s$).
- **clm-cross-links:** clm-mfb2ax (bond = distributed TL / ABCD identity), clm-bnd5rq (srs band-structure arccos top / model adjudication), clm-fy05jc (the TKI dictionary the per-channel projection rides), clm-uu1qbo (the A1/T2 propagation-speed split across the bond's channels)
- **open-ambiguity-flag:** no — the bond noun's structural sense is single; the "TL segment" scope is captured by the MODEL-OF/REGIME-SCOPED grade above, not an ambiguity.
- **verification:** VERIFIED two-method at HEAD — "each K4/srs bond **is** a lossless transmission-line" span + "the lumped node is the $\omega\tau\ll1$ limit of the distributed bond" + distributed-vs-lumped ABCD first divergence $O(\theta^2)$ at `z0-derivation.md:98,:115` (clm-mfb2ax); the three channels (EM-transverse $T_2$, mechanical-shear $T_2$, bulk-longitudinal $A_1$, gapped Cosserat micro-rotation $\gamma$-grade) at `port-register.md:47-50`; the arccos band top $\omega=\omega_{\text{link}}\arccos(\mu/3)$ + "the arccos TL map, not $\omega=\sqrt\lambda$, is the substrate-native band model" (lumped would give $\sqrt{12}$) at `srs-band-structure.md` §1-§2 (clm-bnd5rq, gates #604/#607). ★Bond grade GRANT-RATIFIED 2026-07-21 (verbatim `[sic]` "yes rhat grade matches my perspective"); the `def-tk1xfm` co-equality-below-band-edge scope is surfaced for its own ratification package (Task-3b).

---

## node (lattice site — the intrinsic LC tank)
<!-- id: def-n0det1 -->

- **term:** node (the K4/srs lattice site read as the intrinsic LC tank — the DOF-grade bundle at a lattice site)
- **adjudicated-meaning:** the substrate **NODE** noun, in its **lattice-site / active-site** sense, is an **IDENTITY-at-structure-level** commitment: the DOF-grade bundle at one K4/srs lattice site — the six Cosserat DOF (3 translational→E, 3 microrotational→B) plus the intrinsic per-node LC oscillator and the $A_1$ dilatation grade (Axiom 1). The description **"LC tank / oscillator"** is grade **MODEL-OF** of that same per-site structure — the EE reading of the translational/E grade (capacitive) coupled to the microrotational/B grade (inductive), co-equal with the mechanical reading per the TKI-as-scoped isomorphism (`def-tk1xfm`). **This is a DISTINCT sense of "node" from `def-cc2196`**, which locks "node" = the *spatial-Nyquist / Brillouin cell* (the sampling boundary at pitch $\ell_{node}$); THIS node is the *lattice-site / 4-port active site* sense that `def-cc2196`'s open-ambiguity flag (b) records. KEEP-BOTH: the two senses coexist (sampling-boundary vs active-site) and are read by context.
- **axis:** other — substrate-noun ontology (a lattice site / DOF-grade bundle)
- **dimension/type:** n/a as a noun; the site carries 6 Cosserat DOF + the $A_1$ grade + the LC tank ($L_{cell}=\mu_0\ell_{node}$, $C_{cell}=\varepsilon_0\ell_{node}$)
- **status:** SOLID (the lattice-site/LC-tank structural sense is Axiom-1 canonical; ontology-grade node minted 2026-07-21)
- **ontology-grade:** **IDENTITY-at-structure-level** (the DOF-grade bundle at a lattice site, per Ax 1) **/ MODEL-OF** (the "LC tank / oscillator" EE reading of the same per-sector structure, co-equal with the mechanical reading below the band edge).
- **canonical-home:** `manuscript/common_equations/eq_axiom_1.tex:36-37` (the 6-DOF micropolar node + intrinsic LC oscillator); [`port-register.md`](port-register.md):37,:47-50 ($V_{4\text{-port}}=A_1\oplus T_2$; the per-site grade content); `z0-derivation.md:115` ($L_{cell}=\mu_0\ell_{node}$, $C_{cell}=\varepsilon_0\ell_{node}$ — the node LC tank).
- **clm-cross-links:** clm-j550uh (K4-port irrep decomposition), clm-9kd2t3 (K4-port irrep), clm-uu1qbo (the A1/T2 grade-speed split)
- **open-ambiguity-flag:** YES — "node" is overloaded. **(a)** the **spatial-Nyquist / Brillouin cell** sampling boundary (`def-cc2196`, SOLID; `paley-wiener-hilbert.md:10`); **(b) THIS node** — the **lattice-site / 4-port active site / intrinsic LC tank** (`docs/glossary.md:32` "K4 4-port tetrahedral active site"); **(c)** a **field/wave null** (a zero of amplitude). Read by context; "sub-node" always means "below $\ell_{node}$", never a graph vertex (per `def-cc2196`).
  - conflicting sites: spatial-Nyquist cell `manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/paley-wiener-hilbert.md:10` (locked by `def-cc2196`); lattice-site / 4-port active site `docs/glossary.md:32`.
- **verification:** VERIFIED two-method at HEAD — the 6-DOF micropolar node + intrinsic LC oscillator at `eq_axiom_1.tex:36-37`; the spatial-Nyquist sense at `paley-wiener-hilbert.md:10` (locked by `def-cc2196`); the 4-port active-site sense at `docs/glossary.md:32` ("K4 4-port tetrahedral active site"). The lattice-site sense is Axiom-1 canonical; this node (minted 2026-07-21) gives it the ontology-grade and cross-refs `def-cc2196` (the Brillouin-cell sense) — KEEP-BOTH, the two senses are distinct.

---

## lattice (the connectivity + ordering commitment)
<!-- id: def-latt1c -->

- **term:** lattice (the substrate connectivity + ordering commitment)
- **adjudicated-meaning:** the substrate **LATTICE** noun is an **IDENTITY-at-structure-level** commitment: the **connectivity + ordering** of the substrate — the chiral z=3 srs / Sunada-K4 / Laves net, $I4_1 32$ chiral space group. The **srs/K4 chirality is STRUCTURAL** (a real-space handedness of the ordering, right-handed $I4_1 32$ vs its $I4_3 32$ mirror), not a dynamical order-parameter. This is the connectivity face of the "crystal" identity (`def-cryst1`): "crystal" commits the full Cosserat-crystal structure; "lattice" is the discrete / Nyquist / graph sub-commitment (the connectivity + ordering), the preferred noun in discrete/graph contexts (INVARIANT-N1).
- **axis:** other — substrate-noun ontology (the connectivity/ordering commitment; length scale $\ell_{node}$)
- **dimension/type:** n/a as a noun; carries the pitch $\ell_{node}$ [L] and the graph connectivity ($z=3$)
- **status:** SOLID (the z=3 srs connectivity + $I4_1 32$ chirality are Axiom-1 canonical, doubly-ratified Grant 2026-06-25 + 2026-07-03 D1; ontology-grade node minted 2026-07-21)
- **ontology-grade:** **IDENTITY-at-structure-level** (the connectivity + ordering commitment; srs/K4 chirality is structural).
- **canonical-home:** `manuscript/common_equations/eq_axiom_1.tex:36-37,:43` (z=3 srs connectivity, $I4_1 32$, D1 ratification); INVARIANT-N1 (`the lattice` as the discrete/graph substrate noun).
- **clm-cross-links:** clm-q39qct (z=3 Scheme-A connectivity), clm-9s9apq (z=3 justification)
- **open-ambiguity-flag:** no — the connectivity/ordering sense is single. *(The "K4" NAME overload — graph/lattice vs group vs engine-diamond — is `def-4b1a2c`; the crystalline-vs-amorphous seam is `the-abandoned-interior.md:183`; neither is an ambiguity of lattice-as-connectivity-commitment.)*
- **verification:** VERIFIED two-method at HEAD — z=3 srs connectivity + $I4_1 32$ chiral space group at `eq_axiom_1.tex:36-37`, D1 ratification at `:43`; the discrete/graph substrate-noun convention at INVARIANT-N1 (`ave-kb/CLAUDE.md`). Grade IDENTITY-at-structure-level; cross-refs `def-cryst1` (the full crystal identity) and `def-cc2196` (the Nyquist-cell sampling reading of the same lattice).

---

## transmission-line segment (the EE model-object)
<!-- id: def-tls3g1 -->

- **term:** transmission-line segment (the EE model-object itself)
- **adjudicated-meaning:** the **transmission-line segment** — as the EE **model-object itself** — is grade **MODEL-OF** (per the bond def `def-b0nd01`): a single-mode lossless TL span with characteristic impedance $Z_0=\sqrt{\mu_0/\varepsilon_0}$ and one-span delay $\tau=\ell_{node}/c_0$, which is the **per-channel projection** of a substrate bond. It is exact in the propagating long-wave regime ($\omega\tau\ll1$) and native to the EM-sector engines; it does NOT carry the bond's three-channel structure (a TL is one-mode). At band-edge scales the LUMPED mass-spring approximation ($\omega=\sqrt\lambda$, band top $\sqrt{12}$) breaks down; the DISTRIBUTED arccos-TL band model ($\omega=\omega_{\text{link}}\arccos(\mu/3)$, top $\pi\sqrt3$) is the one that stays exact through the band edge (see `def-b0nd01`, `srs-band-structure.md` §2, clm-bnd5rq). Cross-ref: `def-b0nd01` (the bond, of which this is the per-channel MODEL-OF).
- **axis:** notation / other — an EE model-object (the per-channel projection of a bond)
- **dimension/type:** circuit/structure — $Z_0$ [Ω], one-span delay $\tau=\ell_{node}/c_0$ [T]
- **status:** SOLID — receipt-primary: the bond = distributed-TL identity is canonical (`clm-mfb2ax`, `z0-derivation.md:98,:115`) and the ABCD-cascade TL-segment usage is canonical (`abcd-transfer-matrix.md:14`); the MODEL-OF grade is carried by those receipts, with the `def-b0nd01` bond-grade ratification (Grant 2026-07-21) as cross-ref (not the primary warrant)
- **ontology-grade:** **MODEL-OF** (the single-mode EE model-object; per-channel projection of the bond; exact in the long-wave regime; see `def-b0nd01`).
- **canonical-home:** `z0-derivation.md:98,:115` (the bond as a distributed TL; $Z_0$, $\tau=\ell_{node}/c_0$; clm-mfb2ax); `vol6/framework/computational-mass-defect/abcd-transfer-matrix.md:14` (each TL segment as a 2×2 ABCD; cascade).
- **clm-cross-links:** clm-mfb2ax (bond = distributed TL / ABCD identity), clm-bnd5rq (band-edge model adjudication)
- **open-ambiguity-flag:** no.
- **verification:** VERIFIED two-method at HEAD — the bond-as-distributed-TL span, $Z_0=\sqrt{\mu_0/\varepsilon_0}$, one-span delay $\tau=\ell_{node}/c_0$ at `z0-derivation.md:98,:115` (clm-mfb2ax); the ABCD-cascade TL-segment usage ("each segment of a transmission line is represented as a $2\times2$ matrix") at `abcd-transfer-matrix.md:14`. Grade MODEL-OF, cross-ref `def-b0nd01`.

---

## Cosserat continuum (long-wave continuum description)
<!-- id: def-c0ss3r -->

- **term:** Cosserat continuum (the long-wave continuum description of the lattice)
- **adjudicated-meaning:** the **Cosserat (micropolar) continuum** — as a description of the substrate — is grade **MODEL-OF, REGIME-SCOPED**: the **long-wave continuum limit** of the discrete K4/srs Cosserat crystal (Axiom 1's continuum clause, the "Trace-Reversed Chiral LC Network"). It is **exact below the band edge by construction of the continuum limit** (the $k\ell_{node}\to0$ face of the lattice), carrying the couple-stress modulus $\gamma_c$, the Cosserat characteristic length $l_c=\sqrt{\gamma_c/G_{vac}}$, and the micropolar 6-DOF. Above the band edge the discrete lattice's dispersion (the arccos band top, `srs-band-structure.md`, clm-bnd5rq) departs from the continuum, and the continuum description ceases to be co-equal. Distinct from the **crystal** IDENTITY (`def-cryst1`): the crystal is the structure; the Cosserat continuum is its long-wave MODEL-OF.
- **axis:** other — substrate-description ontology (the long-wave continuum limit)
- **dimension/type:** continuum field description — moduli $G_{vac}$, $K_{vac}=2G_{vac}$, couple-stress $\gamma_c$, length $l_c$ [L]
- **status:** SOLID (the continuum-limit description is Axiom-1 canonical; MODEL-OF/regime-scoped grade minted 2026-07-21)
- **ontology-grade:** **MODEL-OF, REGIME-SCOPED** (the long-wave continuum description of the lattice; exact below the band edge by construction of the continuum limit).
- **canonical-home:** `manuscript/common_equations/eq_axiom_1.tex:36-37` (the continuum clause: "In the macroscopic continuum limit … a Trace-Reversed Chiral LC Network"); `vol9/ch9-mechanical-characteristics/index.md:11` (the Cosserat micropolar continuum spec: $G_{vac}$, $K_{vac}=2G_{vac}$, $\gamma_c$, $l_c=\sqrt{\gamma_c/G_{vac}}$).
- **clm-cross-links:** clm-kmliqx (the $c_R=\sqrt2\,c$ rotational curvature speed), clm-uu1qbo (the A1/T2 speed split at the continuum limit)
- **open-ambiguity-flag:** no.
- **verification:** VERIFIED two-method at HEAD — the continuum-limit clause at `eq_axiom_1.tex:36-37` ("In the macroscopic continuum limit, the lattice is a Trace-Reversed Chiral LC Network"); the Cosserat micropolar continuum spec ($G_{vac}$, $K_{vac}=2G_{vac}$, $\gamma_c$, $l_c$) at `vol9/ch9-mechanical-characteristics/index.md:11`. Grade MODEL-OF, regime-scoped; cross-ref `def-cryst1` (the crystal it is the long-wave limit of).

---

## vacuum (substrate ontology-grade)
<!-- id: def-vacm01 -->

- **term:** vacuum (the substrate noun, ontology-grade)
- **adjudicated-meaning:** the **VACUUM** noun is an **IDENTITY-at-structure-level** commitment: the substrate itself = **the crystal at its operating point** (`def-cryst1`; the chiral Laves K4 Cosserat crystal at a given saturation-state $A_0$ / quiescent point). Under phase-only epistemology it is a structure commitment, not a substance — "the physical vacuum IS a … crystal" (Axiom 1) is read at the STRUCTURE level. This node is the **ontology-grade** record for the vacuum/substrate noun; it is DISTINCT from `def-91c4e8` (`substrate`), which is the **notation** adjudication (the vacuum has no dedicated object glyph — use prose nouns per INVARIANT-N1). Cross-ref: `def-cryst1` (crystal = the same structure, formal/axiom register), `def-91c4e8` (the notation/symbol rule).
- **axis:** other — substrate-noun ontology (the substrate = the crystal at operating point)
- **dimension/type:** n/a (the substrate noun)
- **status:** SOLID — receipt-primary: the "vacuum IS a chiral Laves K4 Cosserat crystal" identity is Axiom-1 canonical (`eq_axiom_1.tex:36`); the ontology-grade node was minted 2026-07-21, with the `def-cryst1` crystal ratification (Grant 2026-07-21) as cross-ref (not the primary warrant)
- **ontology-grade:** **IDENTITY-at-structure-level** (the substrate noun; = the crystal at operating point; cross-ref `def-cryst1`).
- **canonical-home:** `manuscript/common_equations/eq_axiom_1.tex:36` ("The physical vacuum IS a chiral Laves K4 Cosserat crystal"); the operating-point (saturation-state $A_0$ / quiescent point) at `ave-kb/CLAUDE.md` INVARIANT-S2 + `def-q1escn`; the notation rule at INVARIANT-N1 / `def-91c4e8`.
- **clm-cross-links:** (cross-cutting — all axiom-1 claims)
- **open-ambiguity-flag:** no — the ontology-grade sense is single. *(The notation/symbol question — no object glyph — is `def-91c4e8`, a different axis, not an ambiguity of the ontology grade.)*
- **verification:** VERIFIED two-method at HEAD — "The physical vacuum IS a chiral Laves K4 Cosserat crystal" at `eq_axiom_1.tex:36`; the operating-point / saturation-state $A_0$ reading at `ave-kb/CLAUDE.md` INVARIANT-S2 (the LC-tank operating point) + `def-q1escn` (quiescent point); the notation rule (no glyph) at INVARIANT-N1 / `def-91c4e8`. Grade IDENTITY-at-structure-level; = the crystal (`def-cryst1`) at operating point.

---

## envelope vs carrier (the two-level decomposition of the A1 breather)
<!-- id: def-envcar -->

- **term:** envelope vs carrier — the two-level (fast-carrier / slow-envelope) decomposition of the A1 breather
- **adjudicated-meaning:** *(the DECOMPOSITION is definitional; it settles NO coupling claim — see status).* Canon's word for the mass object is **breather** ([`master-equation.md`](../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20 `[canon]`: *"the A1 breather; mₑc² = trapped acoustic compression energy"*). Read at two levels: a fast internal **CARRIER** — the $\nabla\cdot\mathbf{u}$ compression oscillating at the node/$\omega_e$-class resonance, time-average $\approx 0$ — under a slow **ENVELOPE** $A(r,t)$ = the energy-density / operating-point **bias pattern** (what gravitates; what translates when the star orbits). This is a **level-of-description** discipline: the orbital band ($2\Omega\sim10^{-4}$ Hz) sits **$\sim$24 decades below** the carrier ($\omega_e$-class), so a slowly-orbiting envelope has **no carrier-band spectral content** at the orbital frequency — its slow-band presence is a moving bias texture (coefficient side), not a carrier-band source. **The "24-decade catch":** reading the envelope's slow energy moment as a DC carrier-band compression source conflates the two levels (RECORD §5 the sharpest-grain conflation candidate). The decomposition names the levels; it does NOT by itself decide whether the envelope couples to the radiative channel.
- **axis:** phase-carrier (the fast $\omega_e$-class carrier band) vs other (the slow envelope $A(r,t)$ bias texture) — the level-of-description split
- **dimension/type:** carrier = frequency (T⁻¹, $\omega_e = m_ec^2/\hbar$-class); envelope $A(r,t)$ = the dimensionless saturation-amplitude / operating-point field (an energy-density texture, $\propto|A|^2$)
- **status:** SOLID for the DECOMPOSITION only (definitional — canon breather at `master-equation.md:20`; the two-level carrier×envelope reduction is the standard slow/fast split the #767 reduction is built on). **The coupling verdict is NOT hardened here:** the #767 envelope-sector reduction that USES this decomposition is banked **BIN-1-CONDITIONAL** (`research/2026-07-20_envelope-sector-reduction_result.md` §3.1/§6.2-1) — grade the decomposition, not the coupling.
- **canonical-home:** [`master-equation.md`](../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20 (breather, canon) + the #767 reduction (`research/2026-07-20_envelope-sector-reduction_result.md`, PR #767 merged @ `5287ef32`) + the walk `research/2026-07-20_envelope-boundary-walk_RECORD.md` §5 (the envelope-vs-carrier payload, walk-level)
- **clm-cross-links:** *(none minted — the envelope lane mints no `clm-`, propagates to no leaf, READ-ONLY on KB; cross-node: def-a9eef5 (`carrier`, the overloaded surface form — its phase-carrier reading IS this carrier), def-l0ngdu (∇·u dynamical vs ∇·A gauge), def-5d2b8a (the two "3"s), def-satshr (the shear/compression split of the same envelope's bias field))*
- **open-ambiguity-flag:** no — this node adjudicates the two-level DECOMPOSITION (a specific compound term). The **bare** surface form "carrier" is independently overloaded and is recorded at def-a9eef5 (its phase-carrier reading is the carrier of this decomposition); read that node for the surface-form overload.
- **verification:** VERIFIED two-method (`grep -F` + `git grep`) at HEAD `3d07ceeb` — the breather + `mₑc² = trapped acoustic compression energy` verbatim at `master-equation.md:20`; PR #767 merged (`gh pr view 767` → `mergeCommit 5287ef32`, base `origin/main` is downstream); the envelope-vs-carrier payload + the 24-decade / envelope-moment-vs-carrier-moment conflation at RECORD §5. Status **SOLID** for the decomposition; the #767 coupling verdict (BIN-1-CONDITIONAL) is cited, NOT graded here.

---

## saturation-shear wave vs saturation-compression wave (trace/traceless split of the bias field)
<!-- id: def-satshr -->

- **term:** saturation-shear wave vs saturation-compression wave — the traceless/trace projection split of the saturation-bias field's radiative moment
- **adjudicated-meaning:** *(a definitional trace/traceless SPLIT of the mass second-moment; the LIVE exclusion status is cited, not this node's own grade — see status).* The radiative moment of the slow envelope's bias field is $Q_{ij}\propto\int x_i x_j|A|^2$ (the mass second-moment). Its **traceless (deviatoric)** projection = the **saturation-SHEAR wave** = the **OBSERVED gravitational wave** — the T2-shear channel, quadrupole rotating at $2\Omega$, radiating at $c$, tensor polarization (`scalar-gw-bulk-channel_derivation.md`:95 *"the traceless part rotates at 2Ω"*; kept on the T2/shear channel at exactly $c$, consistent with GW170817's $|c_{GW}-c_{EM}|/c\lesssim10^{-15}$). Its **trace** projection = the **saturation-COMPRESSION wave** = the A1-bulk / scalar (breathing) channel = the **pulsar-excluded bulk radiative port** (Q1 Reading-A, now LIVE against the framework). The observed-GW-=-shear identification is **Reading-independent** (survives the Q1 revert); the compression channel's live exclusion **rides** port-register Q1 Reading-A LIVE and is a cited consequence, not this node's grade. 🔴 **[DEMOTED 2026-08-11 — R40-B1; dated demotion note at the end of this file]**
- **axis:** other — sector-projection split of the saturation-bias field (A1-bulk **trace** vs T2-shear **traceless**), a mass-second-moment decomposition
- **dimension/type:** both are radiative wave channels (metric strain, dimensionless); scalar/breathing (trace, A1-bulk) vs tensor (traceless deviatoric, T2-shear) polarization classes
- **status:** SOLID for the trace/traceless DEFINITIONAL SPLIT (the standard mass-second-moment decomposition; the observed GW = the traceless shear projection is Reading-independent). **NOT a hardening of the coupling verdict:** that the compression/trace channel is an independent radiative port and is pulsar-excluded is **Q1 Reading-A LIVE** (a REVERTED ruling, `port-register.md:87`) — cited here, graded there.
- **canonical-home:** the walk `research/2026-07-20_envelope-boundary-walk_RECORD.md` §4–§5 (the corrected boundary/envelope walk) + [`port-register.md`](port-register.md):87 (Q1 Reading-A LIVE — the compression channel) + `research/2026-07-20_scalar-gw-bulk-channel_derivation.md` §5.1 (the trace/traceless partition + the Abbott #768 second-source stamp)
- **clm-cross-links:** *(none minted — READ-ONLY on KB, no `clm-` propagated; cross-node: def-l0ngdu (∇·u vs ∇·A — the longitudinal/compression sector), def-t2ph01 (T2 photon-family disambiguation — the transverse-shear family), def-9a4f07 (longitudinal V-sector scalar), def-envcar (the envelope whose bias field is split here))*
- **open-ambiguity-flag:** no — this node adjudicates the projection split. **Read-guard (not an overload record):** "scalar mode" here is the GW-polarization sense (the LIGO scalar/breathing polarization test = the compression/trace channel); do NOT conflate it with a QM "scalar field". The compression channel is the A1-bulk (mechanical dilatation), NOT a transverse EM mode.
- **verification:** VERIFIED two-method (`grep -F` + `git grep`) at HEAD `3d07ceeb` — the traceless-rotates-at-$2\Omega$ shear quadrupole at `scalar-gw-bulk-channel_derivation.md:95` and the T2/shear-at-$c$ consistency at `:168`/`:150`; Q1 **Reading-A LIVE** two-method at `port-register.md:87` (row), `:93` (register verdict), `:109` (tally), `:5` (frontmatter); the Abbott second-source stamp (`log₁₀ B = +23.09±0.08` tensor-vs-scalar, EM-sky-fixed) at `scalar-gw-bulk-channel_derivation.md:138` (PR #768 merged @ `c12da9f5`). Status **SOLID** for the definitional split; the compression-port live-exclusion is cited to Q1 Reading-A, NOT graded here.

---

## non-captured saturation wave (bound-vs-free division of the bias field)
<!-- id: def-ncsatw -->

- **term:** non-captured (free) saturation wave vs captured (bound) saturation wave — the bound/free division of a saturation disturbance
- **adjudicated-meaning:** *(WALK-RATIFIED DIRECTION, not a locked canon split — carries the honest walk status; see status).* A disturbance of the saturation-bias field is either **CAPTURED (bound)** — a **soliton**: self-maintained, its own amplitude pins a one-node-shell boundary at the yield **rail** ($S(A)=\sqrt{1-A^2}=0$ at $A=A_{yield}$, $\Gamma=-1$ exact), a closed/confined mode where "the mirror is made of the thing it confines" (RECORD §4) — or **NON-CAPTURED (free)** — a **radiated** saturation wave: an **open-contour** disturbance propagating **sub-rail** (below yield, $S>0$, transmission not exponentially dead), not self-confined; the far-field / GW radiation class (the escape-cone / WKB-turning-point regime of the same boundary picture, RECORD §4 `:47–:48`). The division sorts the same saturation field into the bound soliton (the mass) and the free radiation (the wave) by whether the disturbance touches the rail and self-maintains. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**
- **axis:** other — bound-vs-free (captured/non-captured) classification of a saturation disturbance; the emergent-boundary picture
- **dimension/type:** the bound mode = a confined soliton (rail-touching, $S=0$ at its boundary shell); the free mode = a propagating wave (sub-rail, open contour) — a classification, not a single dimensioned quantity
- **status:** proposed — **WALK-RATIFIED DIRECTION** (the emergent saturation-boundary walk, `research/2026-07-20_envelope-boundary-walk_RECORD.md` §4–§5; the RECORD **canonizes nothing** — every physics statement there is a cited canon hook, a Grant-verbatim walk statement, or an orchestrator walk-level candidate). Coinage (0 prior corpus hits, `git grep` — the only prior use is the queue line that scheduled this def). **NOT SOLID, NOT canon;** adjudicated nowhere yet — the envelope-lane / boundary picture is the eventual adjudicator.
- **canonical-home:** *(none — coinage; grounded walk-level in `research/2026-07-20_envelope-boundary-walk_RECORD.md` §4 (`:46–:48` the rail/self-maintaining/escape-cone content) + §5, the emergent saturation-boundary picture)*
- **clm-cross-links:** *(none minted — RECORD canonizes nothing; cross-node: def-envcar (envelope/carrier — the bound soliton is the envelope of the A1 breather), def-satshr (shear/compression — the free radiated channel splits into these), def-l0ngdu (∇·u dynamical), def-envl0p (the struck soliton-size-envelope node — a distinct object; do not conflate the size-envelope with this bound/free division))*
- **open-ambiguity-flag:** no — a coinage with a single walk-direction meaning. Carries its honest walk-level status (proposed, walk-ratified direction); the term is minted from the walk, not from a locked leaf.
- **verification:** VERIFIED at HEAD `3d07ceeb` — the self-maintaining rail-touching bound soliton ("the mirror is made of the thing it confines") at RECORD `:46`; the free/sub-rail escape-cone radiation (transmission exponentially dead only AT the rail; the shallow-tail WKB turning point below it) at RECORD `:47–:48`; walk-level (RECORD §0 canonizes nothing, mints no `clm-`). Coinage 0-prior-hit confirmed (`git grep -Fi "non-captured saturation"` → only the pending-rulings queue line). Status **proposed** (walk-ratified direction; NOT hardened into canon).

---

## ponderomotive envelope coupling (the |A|²-to-carrier-branch source structure)
<!-- id: def-pndenv -->

- **term:** ponderomotive envelope coupling — the $|A|^2$-to-acoustic-branch far-field source structure of the #767 envelope reduction
- **adjudicated-meaning:** *(the SOURCE STRUCTURE is banked per merged #767; the coupling COEFFICIENT is q1-inherited/ASSUMED, NOT derived — the def carries that; see status).* The mechanism by which the slow envelope drives the radiative channel: the **mass-quadrupole ponderomotive back-reaction** of the carrier intensity $|A|^2$ (= the mass-energy density, `master-equation.md:20`) onto the low-frequency acoustic field — source $Q_{ij}\propto\int x_i x_j|A|^2$ radiating at $2\Omega$ into the **gapless** P-branch (#767 result `:12`/`:36`). Fork F1 resolved: whether $|A|^2$ is a *source* (RHS) or a *coefficient* (the moving well the envelope rides), the far-field object is the same mass quadrupole at $2\Omega$; the adiabatic ($\varepsilon=\Omega/\omega_0\sim10^{-24}$) protection covers only the frequency-scale-separated carrier band, never the gapless acoustic channel (#761 gaplessness, clm-bnd5rq 0.8). **The coefficient is NOT derived here:** the far-field structural coupling $\kappa_{env}^2 = A_{ang}(c_S/c_P)^5 = 0.034$ uses $A_{ang}=2/3$ = the **q1-inherited ASSUMED symmetric-coupling** normalization ($\kappa_L/\kappa_T=1$; the #761 prereg's own *"assumed symmetric-coupling grade-assignment"*), NOT computed from the K4/Ax4 Lagrangian (it is not numerically circular — $\kappa^2$ is a flux ratio, the mass-moment normalization cancels). 🔴 **[DEMOTED 2026-08-11 — R40-B1; dated demotion note at the end of this file]**
- **axis:** other — envelope→acoustic-branch source coupling (slow-band ponderomotive drive of the gapless P-branch)
- **dimension/type:** a source-coupling structure ($Q_{ij}\propto\int x_i x_j|A|^2$, source of the $2\Omega$ far field); the coefficient $\kappa_{env}^2$ is dimensionless (a far-field flux ratio $F_{bulk}/F_{shear}$)
- **status:** proposed — the SOURCE STRUCTURE is banked per **#767 merged** (`5287ef32`); the coupling **COEFFICIENT is q1-inherited / ASSUMED** (not derived from the Lagrangian — #767 review R3), and the overall lane verdict is **BIN-1-CONDITIONAL**. Coinage (0 prior corpus hits; the only prior use is the queue line). **NOT SOLID** (the coefficient is assumed, not derived); a re-open with a DERIVED coupling is a separate future ruling.
- **canonical-home:** *(none locked — the source structure is banked at `research/2026-07-20_envelope-sector-reduction_result.md` `:12`/`:36` (the ponderomotive $|A|^2$ mass-quadrupole coupling); the assumed coefficient is flagged at `:11`/`:127`; PR #767 merged @ `5287ef32`)*
- **clm-cross-links:** *(none minted — #767 mints no `clm-`, READ-ONLY on KB; cross-node: def-envcar (the envelope $|A|^2$ that sources this), def-l0ngdu (∇·u — the gapless P-branch this couples into), def-satshr (the compression channel this feeds vs the surviving shear))*
- **open-ambiguity-flag:** no — this node names one specific source structure. It carries the assumed-coefficient caveat explicitly; the term is a coinage, single meaning.
- **verification:** VERIFIED two-method (`grep -F` + `git grep`) at HEAD `3d07ceeb` — the ponderomotive $|A|^2$ mass-quadrupole coupling into the gapless P-branch at `envelope-sector-reduction_result.md:12` and `:36`; the q1-inherited/ASSUMED equal-coupling normalization ($A_{ang}=2/3$) at `:11` (*"the q1-inherited ASSUMED symmetric-coupling normalization"*) and `:127` (*"[assumed] — q1-inherited symmetric-coupling grade-assignment"*); PR #767 merged (`gh pr view 767` → `5287ef32`); clm-bnd5rq resolves. Status **proposed** (source banked, coefficient assumed, verdict BIN-1-CONDITIONAL — not hardened into canon).

---

## the relative-offset principle (position defined only ON the node graph)
<!-- id: def-r0ffst -->

- **term:** the relative-offset principle (Grant's handle "the relative offset"; the Fork-ρ direction-closure principle)
- **adjudicated-meaning:** *(a named foundational PRINCIPLE, not a substrate object — cite-don't-duplicate; the full statement + three corollaries + the anti-advection reductio live at the canonical home.)* In a phase-only substrate there is **no spatial frame beneath the node graph**: position is defined only ON the graph, as a pattern of **relative phase offsets** across nodes. A localized excitation IS such a pattern, so its energy goes where its host nodes go — it **cannot hold station** against the material displacement of its nodes (station-keeping would require anti-advective node-to-node hopping, which presupposes the very sub-graph spatial anchor phase-only denies). Only the **RELATIVE** offset between an excitation and the medium it rides is defined; a **UNIFORM** such offset self-cancels and is unobservable (the excitation-side twin of no-aether-drag). Scope is **DIRECTION-not-MAGNITUDE**: Corollary C splits into **C-kin** (kinematic participation — trapped-energy patterns sway with the carrier's material motion; walk-ratified, UNCONDITIONAL) and **C-load** (the acoustic-loading consequence `ρ_eff/ρ_0 = 1 + β·φ`; CONDITIONAL on the open sector-crossed inertia ledger `clm-m5swh9`).
- **axis:** other — a foundational phase-only frame/position principle (position on the node graph; the excitation-side mechanism of emergent-relativity self-cancellation); NOT a substrate-noun ontology node (hence no `ontology-grade`)
- **dimension/type:** n/a (a principle, not a field or observable — only the RELATIVE offset between excitation and medium is a defined quantity; a uniform offset is unobservable)
- **status:** SOLID for the NAME/term — the handle "the relative offset" was PROPOSED-FOR-RATIFICATION and is **Grant-ratified-at-merge** (PR #787 merged 2026-07-21, verbatim `[sic]`: *"yes the relative offset makes sense, and seemsmlike a major concept for the cannon to adjudicate and define"*), locked to its canonical home leaf. **This locks the TERM, not a physics grade** (a `def-` node carries no solidity): the underlying physics is a pre-adversarial-review consistency/organizing-class reading — the DIRECTION at `clm-hu1jjw` (0.50, walk-ratified, pending review) and the MAGNITUDE OPEN at `clm-m5swh9` (`*pending*`) — graded there, not here.
- **canonical-home:** [`relative-offset-principle.md`](relative-offset-principle.md) §"The principle" + §"The three corollaries" + §"Honest scope" (hosts `clm-hu1jjw` principle+direction, `clm-m5swh9` open magnitude); walk provenance `research/2026-07-21_fork-rho-walk_RECORD.md`
- **clm-cross-links:** clm-hu1jjw (the principle + Fork-ρ direction, 0.50), clm-m5swh9 (the OPEN loaded-inertia magnitude / β / sector-crossed c², `*pending*`)
- **open-ambiguity-flag:** no — the compound term "the relative-offset principle" carries one locked sense; no other register node uses this surface form (register scan for "offset" → 0 competing `def-` nodes). **Read-guards (not overload records), recorded per the sense-collision guard:** (a) the principle's "**node** graph / **node** indices" uses `def-cc2196`'s graph-vertex / lattice-point sense (the K4 4-port active site / material lattice point), **NOT** `def-cc2196`'s SOLID spatial-Brillouin Nyquist-cell sense — do not re-key; (b) the bare word "offset" is also used for the frozen even-order DC **bias/offset** operating point `u₀*` (`def-u0star` Sense B — a saturation operating point), a different object from a graph-position offset.
- **verification:** VERIFIED at HEAD — PR #787 MERGED 2026-07-21 (`gh pr view 787` → mergedAt 2026-07-21; leaf on `origin/main`), ratifying the previously proposed-for-ratification name; the DIRECTION-0.50 / MAGNITUDE-pending grades confirmed at `common/claim-quality.md` (`clm-hu1jjw` rationale "Graded 0.5"; `clm-m5swh9` `*pending*`). Surface-form uniqueness confirmed two-method (register "offset" scan + grep) → 0 competing `def-` nodes. Status SOLID for the Grant-ratified-at-merge name; the physics grade is cited to the two `clm-` nodes, NOT asserted here (consistency/organizing-class — the excitation-side twin of the AC/DC carve `clm-acdc07`).

---

## saturation rim-inversion (the interior→rim phase-space inversion)
<!-- id: def-satrim -->

- **term:** saturation rim-inversion (the interior→rim phase-space character-inversion of the Axiom-4 kernel)
- **adjudicated-meaning:** *(a named organizing / consistency-class READING over already-canonical objects — not a substrate object and not a new derivation; cite-don't-duplicate; the full mapping + two lower-grade rider reads live at the canonical home.)* The Axiom-4 kernel `S(A)=√(1−(A/A_yield)²)` is a **circle constraint** `S²+(A/A_yield)²=1`. Reading a single mode's reactive state in the (amplitude `A`, phase `θ`) **PER-MODE PHASE-SPACE** disk: a **cold node** lives in the disk INTERIOR (amplitude-dynamic, phase-trivial — its amplitude can wander to `A→0`, so any winding can unwind); a **saturated core** is pinned ON the RIM `A=A_yield` (`S→0`, local clock frozen `c_eff=c√S→0`; amplitude-frozen, phase-topological, `π₁(S¹)=ℤ`). The dynamics and topology **swap roles**; the core's state space is the **BOUNDARY** of the baseline's. The rim is where an imposed static `(2,3)` **Link** winding is **MAXIMALLY PROTECTED** (the amplitude freeze-out removes the `A→0` unwinding channel) — a **locus-of-PROTECTION consistency reading, NOT a quantization mechanism**: charge = the STATIC imposed Link per the #416 two-natured ruling, and the nearest DYNAMICAL charge-winding tests read NEGATIVE (#415 real-space eigensolve, #59 phase-space carrier-lock).
- **axis:** phase-carrier — the per-mode reactive amplitude/phase plane (A46 COORDINATE DISCIPLINE: a **PHASE-SPACE** state-space reading, **NOT** a real-space radial profile — must not be conflated with the envelope wall/knee real-space loci); NOT a substrate-noun ontology node (hence no `ontology-grade`)
- **dimension/type:** n/a (an organizing phase-space reading, not a dimensioned quantity — the state coordinate is `A/A_yield ∈ [0,1]` on the unit-circle constraint; the rim is `A=A_yield`, `S=0`)
- **status:** SOLID for the NAME/term — `saturation-rim-inversion` was PROPOSED-FOR-RATIFICATION and is **Grant-ratified-at-merge** (PR #790 merged 2026-07-21, verbatim `[sic]`: *"i saw the phasor changing, but i think this mapping you provided makes more sense than what i was thinking, shoild we scope cannonizing it?"* — the MAPPING ratified over his prior sign-flip reading), locked to its canonical home leaf. **This locks the TERM, not a physics grade** (a `def-` node carries no solidity): the physics is a pre-review reading — the inversion MAPPING at `clm-riminv` (0.55, consistency-class), with two explicitly lower-grade riders, the topological-necessity CANDIDATE `clm-satnec` (OPEN, `*pending*`, NOT ratified) and the channel-duality re-reading `clm-zdual1` (0.50) — graded there, not here.
- **canonical-home:** [`saturation-rim-inversion.md`](saturation-rim-inversion.md) §"The inversion statement" (hosts `clm-riminv` mapping, `clm-satnec` necessity candidate, `clm-zdual1` channel-duality); walk provenance `research/2026-07-21_phase-space-inversion-walk_RECORD.md`
- **clm-cross-links:** clm-riminv (the interior→rim mapping, 0.55), clm-satnec (the OPEN topological-necessity candidate = the K=2G eigenmode-existence open item, `*pending*`), clm-zdual1 (the A1-short / T2-open channel-duality re-reading over INVARIANT-S2, 0.50)
- **open-ambiguity-flag:** YES — the surface word "inversion" is overloaded in the register; the locked sense here (a) must be qualified against the others:
  - (a) **THIS node — phase-space CHARACTER-inversion** (interior disk ↔ boundary rim: amplitude-dynamic/phase-trivial ↔ amplitude-frozen/phase-topological) [per-mode phase-space, `clm-riminv`].
  - (b) the **parity-meter "inversion-symmetry" / even-order bias** sense (`def-u0star` Sense B, `clm-invmtr`; `universal-saturation-kernel-catalog.md:179,203` "forbidden by inversion symmetry … inversion-symmetry METER") — a T-parity kernel property, NOT a phase-space state swap.
  - (c) the **TKI "INVERTIBLE dictionary"** sense (`def-tk1xfm`; the ξ_topo change-of-reference is gain-1, pole-less, INVERTIBLE — `translation-circuit.md:17-26`) — map-invertibility, NOT a state-space inversion.
  - (d) Grant's **PARKED sign-flip "phasor changing"** sense — the Cosserat micro-rotation SENSE inverting relative to `Ω_freeze` (same leaf §"The parked sign-flip question", `saturation-rim-inversion.md:72-78`, minted as NO-CLAIM; spin/antiparticle-flavored) — a DISTINCT open question, not adjudicated by `clm-riminv`.
  - **cross-ref, NOT a competing sense (KEEP-BOTH):** the semiconductor-analogy spoke of THIS SAME object is the **MOS inversion-layer** row (`translation-circuit.md:299` §4.6.2 Row B / `:400` row 30, `clm-riminv`) — same walk, same object, a means-tested ANALOGY with a flagged disanalogy (MOS = conductive channel; the saturation wall = `|Γ|=1` reflective mirror); it does not redefine this node's sense.
  - conflicting sites: parity-meter inversion-symmetry `universal-saturation-kernel-catalog.md:203`; TKI-invertible dictionary `translation-circuit.md:17`; parked sign-flip `saturation-rim-inversion.md:74`; MOS-inversion-layer cross-ref `translation-circuit.md:299`.
  - **"rim" read-guard:** "rim" here = the phase-space unit-circle boundary `A=A_yield` (locus of protection), **NOT** a real-space envelope wall/knee radial locus (those are `S(A(r))` real-space loci — `envelope-anatomy.md:13` "NOT phase-space contours"; A46). No competing `def-` node carries "rim".
- **verification:** VERIFIED at HEAD — PR #790 MERGED 2026-07-21 (`gh pr view 790` → mergedAt 2026-07-21; leaf on `origin/main`), ratifying the previously proposed-for-ratification name at the MAPPING level; the `clm-riminv` 0.55 / `clm-satnec` `*pending*` / `clm-zdual1` 0.50 grades confirmed at `common/claim-quality.md`. The "inversion" conflicting sites two-method verified: parity-meter at `universal-saturation-kernel-catalog.md:179,203` (+ `def-u0star`); TKI-invertible at `translation-circuit.md:17-26` (+ `def-tk1xfm`); parked sign-flip at `saturation-rim-inversion.md:72-78`; MOS cross-ref at `translation-circuit.md:299,400`. Status SOLID for the Grant-ratified-at-merge name (MAPPING level); the physics grade is cited to the three `clm-` nodes, NOT asserted here (consistency/organizing-class; the necessity candidate is OPEN).

---

## effective mass / m\* (the fitted parameter vs the derived inertia — TWO senses, KEEP-BOTH)
<!-- id: def-mstar1 -->

- **term:** effective mass / $m^*$ (surface form; also $m_{eff}$, $M_{eff}$, "effective density")
- **adjudicated-meaning:** *(the disambiguation IS the content — Grant-ruled 2026-07-26; this node discharges the `translation-circuit.md`:306 open flag, it does not add physics.)* The surface form "effective mass" / $m^*$ names **TWO DISTINCT OBJECTS with OPPOSITE dispositions** in this corpus, separated by Grant's discriminator **derived-not-fitted**: **(A)** the SM thermal-statistical **FITTING PARAMETER** — an empirically fitted transport knob — which the corpus **STRIKES**, and the strike **STANDS**; **(B)** a **DERIVED inertia** read off the substrate's own dispersion / energetics — **a different object, NOT struck**. Grant verbatim `[sic]` (2026-07-26): *"correct, should not be a fitting parameter, a plus c should make sense"* — ratifying option (a)+(c): keep the strike byte-untouched **and** mint this disambiguating node.
- **axis:** other — **Sense A** has no substrate axis (it is a phenomenological transport-model parameter; being axis-less is what the strike removes); **Sense B** is an inertia / inertia-density read, sector-labelled **per instance**. ★**Sector carve (A1⊥T2 cross-wiring watch):** the *loaded branch* — the carrier whose effective density is being read — is the **A1 compression/acoustic** branch in both instances; the *storage sector* (which sector holds the energy that does the loading, and therefore which $c^2$ divides it) is **OPEN and NOT assigned here** — pending-rulings §1 item 13 / charter D1 (`research/2026-07-21_continuum-radial-solver_CHARTER.md`:15,:62; canon's A1 reading is `master-equation.md`:20, the contested T2 reading is `clm-m5swh9`). This node must not pre-empt that ruling. **NOT a substrate-noun ontology node** (hence no `ontology-grade`) — a derived-or-fitted QUANTITY, not a noun naming the medium.
- **dimension/type:** **Sense A** — mass ($M$), fitted. **Sense B — two-armed:** mass ($M$) on the composite-resonator arm ($m_{eff}=m_e\sqrt{1+k}$; the emergent $M_{eff}$); mass-density ($M\,L^{-3}$) on the dressed-branch acoustic arm ($\rho_{eff}/\rho_0$). See the NAME PROPOSAL dimension caveat below.
- **status:** ambiguous — the **DISPOSITION is Grant-ruled 2026-07-26** (A struck / B a distinct object, not struck), but the **surface form $m^*$ remains overloaded across two objects**, so every cite must name which sense. (The `ambiguous` tag flags the *surface overload*, not the *ruling*, exactly as on `def-5d2b8a` and `def-1f6e34`.) This node locks the TERM SPLIT only; it carries no solidity — each Sense-B instance's grade lives on its own `clm-` node.
- **canonical-home:** [`translation-tables/translation-circuit.md`](translation-tables/translation-circuit.md):305-306 (§4.6.3 — the `m^*` tension flag this ruling discharges; the flag's evidence is preserved and a dated RULED block appended, Rule 12)
- **clm-cross-links:** clm-w5ez6i (the emergent $M_{eff}$ from the converged field's own integrated energy — a Sense-B instance, 0.55 input-only), clm-m5swh9 (the OPEN sector-crossed $c^2$ / loaded-inertia magnitude — the D1/I8 object the Sense-B derivation route was proposed to answer, `*pending*`), clm-hu1jjw (the relative-offset direction whose C-load arm is the loading a Sense-B inertia would carry, 0.50)
- **open-ambiguity-flag:** YES — two distinct objects under the one symbol $m^*$, **KEEP-BOTH**:
  - **(a) Sense A — the SM thermal-statistical FITTING PARAMETER. 🔴 STRUCK; the strike STANDS (Grant-ratified 2026-07-26).** An empirically fitted knob in the drift-diffusion / Fermi-Dirac "Weather Forecast" treatment. Strike sites, verbatim: `vol_4_engineering/chapters/19_silicon_design_engine.tex`:45 — *"rendering the entire thermal mobility and effective-mass ($m^*$) parameter set obsolete"*; `vol_4_engineering/chapters/11_experimental_falsification.tex`:463 — *"empirical fitting constants (effective mass $m^*$)"*. **Byte-untouched by this ruling.** [mass ($M$), fitted]
    - **Softer sibling stance (NOT a strike, recorded so the two are not conflated):** `vol6/period-3/silicon/topological-area.md`:17 *peer-frames* the structural reading against the thermal treatment — *"parameterized by effective mass ($m^*$) and mobility ($\mu$)"* … *"peer with standard semiconductor physics"* … *"it does not supersede the thermal treatment"* — rather than striking it. Both stances stay as written (2026-07-21 audit precision note).
  - **(b) Sense B — a DERIVED / substrate-read inertia. A DISTINCT OBJECT; NOT struck.** Read off the substrate's own dispersion or energetics rather than fitted to data. Instances already IN USE in the corpus:
    - **composite-resonator mass** — `vol2/quantum-orbitals/ch07-quantum-mechanics/scale-separation.md`:66, verbatim: *"mode with increased effective mass $m_{\text{eff}} = m_e\sqrt{1+k}$"* (manuscript twin `vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex`:3698, same sentence). [mass ($M$)]
    - **emergent integrated-energy mass** — `vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md`:21, verbatim: *"effective mass **emerges** from the converged field's own integrated energy"* (`clm-w5ez6i`; the value-map still imports $G$ — consistency-class, not a value-chord). [mass ($M$)]
    - **dressed-branch effective density of locally-resonant loading** — the acoustic $\rho_{eff}$ of a cage-loaded composite: `research/2026-07-21_beta-tracking-feasibility_scoping.md`:35 (*"the **acoustic effective density**, which carries two competing terms"* — structural added-mass DOWN vs trapped-energy loading UP, net sign open, `clm-m5swh9`) and the mass-in-mass / locally-resonant anti-resonance topology at `research/2026-07-09_x36-node-bottleneck_result.md`:25,51. Standing external anchor for the same object: `common/physics-lineage-map.md`:488 (*"locally resonant acoustics (effective density negative near anti-resonance; Milton–Willis 2007: effective mass is generically tensorial and nonlocal in time)"*). [mass-density ($M\,L^{-3}$)]
  - **★NAME PROPOSAL for Sense B (PROPOSED-FOR-RATIFICATION — NOT canon; minted so the symbol collision stops).** Proposed name: **dressed effective density**. COINAGE-GREP two-method: **0 prior hits** across `manuscript/` `src/` `research/` `_orchestration/`. *Alternative considered and NOT picked:* **curvature-read inertia** (also 0 hits) — rejected because the literal curvature read is precisely what the 2026-07-26 finding below demotes to decoration; naming the sense after a just-demoted method would re-import the confusion. **⚑ Dimension caveat surfaced, not resolved (flag-don't-fix):** "density" is exact on the acoustic dressed-branch arm ($M\,L^{-3}$) but **wrong-dimension on the composite-resonator arm** ($m_{eff}=m_e\sqrt{1+k}$ is a mass, $M$). If Grant wants ONE name spanning both arms the surface word must generalize (e.g. *"dressed effective inertia"*); if two names are acceptable, "dressed effective density" covers the acoustic arm and the composite-mass arm keeps $m_{eff}$. **Surfaced for Grant; nothing renamed at any site by this entry.**
  - **★2026-07-26 finding — the LITERAL band-bottom curvature read is DECORATION for the D1 question.** Candidate-6 proposed $m^*=\hbar^2/(d^2E/dk^2)$ as the substrate-native derivation route for D1 (`translation-circuit.md`:305). Evaluated at a band bottom it is **sector-blind**: every gapped branch returns $m^*=\hbar\omega_0/v^2$ with $v$ that branch's own curvature coefficient, so $m^*v^2=\hbar\omega_0=E$ **identically** — the gap $\omega_0$ divides out and the read hands back *"this branch's own $c^2$"* for whichever branch is differentiated. It therefore **cannot adjudicate** D1/I8 (which sector's $c^2$ divides $E_{trapped}$: $c_P=0.519$ / $c_S=0.286$ / $c_{EM}$) — it presupposes the answer. **Tracked anchor for the QUESTION:** `research/2026-07-21_continuum-radial-solver_CHARTER.md`:15 (D1) + :62 (I8, *"which sector's `c²` divides `E`"* is *"not automatic"*). **⚑ The FINDING ITSELF has NO tracked home as of this entry** — surfaced in-chat 2026-07-26; no research/scoping doc landed it. Per the citation-rot re-pin discipline (`def-1f6e34`: *no `def-` node cites an untracked path*), only the CHARTER is cited. Cite THIS node for the finding until a scoping doc lands. This does **not** touch D1 itself, which stays OPEN pending the sector-of-storage walk (`_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md` §1 item 13).
    - conflicting sites: Sense-A strikes `19_silicon_design_engine.tex`:45 + `11_experimental_falsification.tex`:463; Sense-A softer peer-frame `vol6/period-3/silicon/topological-area.md`:17; Sense-B composite mass `scale-separation.md`:66 (+ `07_quantum_mechanics_and_orbitals.tex`:3698); Sense-B emergent mass `saturating-modulus-and-backreaction.md`:21; Sense-B dressed density `2026-07-21_beta-tracking-feasibility_scoping.md`:35; the ruled tension flag `translation-circuit.md`:305-306.
- **verification:** All **nine** distinct line-cites in this node verified **two-method** (`sed` line-range + `grep -n` on a distinct substring) at HEAD `c8ceacc3`: the two vol-4 strike lines **VERBATIM-CONFIRMED** at :45 and :463; `m_{\text{eff}} = m_e\sqrt{1+k}` **CONFIRMED** at `scale-separation.md`:66 and its manuscript twin :3698; *"effective mass emerges from the converged field's own integrated energy"* **CONFIRMED** at `saturating-modulus-and-backreaction.md`:21; the softer vol-6 peer-frame **CONFIRMED** at `topological-area.md`:17; the acoustic-effective-density two-term statement **CONFIRMED** at `2026-07-21_beta-tracking-feasibility_scoping.md`:35. **No cite failed.** *(The enumeration above names six; the node's remaining three line-cites — `x36-node-bottleneck_result.md`:25,:51 and `physics-lineage-map.md`:488 — were verified on the same pass and also resolve; count corrected 2026-07-26 per the PR #799 audit.)* Both proposed Sense-B names COINAGE-GREPPED to 0 prior hits. The three `clm_cross_links` resolve in `.index/claims.jsonl`. Status **ambiguous** — the ruling settles the DISPOSITION (A struck / B distinct), not the surface overload; the Sense-B NAME is `proposed`, not ratified, and the decoration finding is recorded here because it has no tracked home yet.

---

## Seed coverage + follow-up

**Seeded (14):** 1 SOLID (`node`), 8 ambiguous (`carrier`, `Nyquist`,
`phase-space`, `size`, `radius`, `r_opt`, `Compton`, `winding`), 5 proposed
(`κ_share`, `r_env`, `node-Nyquist-size-boundary`, `SubstrateExcitation`,
`BoundResonator`).

**Organizing-principle terms (3 SOLID, added 2026-06-20):** `chord`
(`def-ch0rd1`, forced FORM), `echo` (`def-ech0v1`, imported VALUE), `mixed`
(`def-fmv001`, form-derived/value-fitted) — the canonical definitions of the
FORM-vs-VALUE axis, locking the prose labels to the interlock register's
CI-gated `real_or_fitted` tags (INVARIANT-S13). Umbrella leaf:
[`form-deriving-value-importing.md`](form-deriving-value-importing.md).

**Sector disambiguation (1 SOLID, added 2026-07-03):** `T₂` (`def-t2ph01`,
photon-family disambiguation) — locks "T₂ = the photon" to the massless
transverse-TRANSLATIONAL u-family (NOT the gapped Cosserat microrotational ω);
open-ambiguity YES (the two T₂ objects, separated by massless-vs-gapped). G2
ruling Grant 2026-07-03, `research/2026-07-03_g2-photon-relabel_note.md`.

**Substrate-noun ontology (8 nodes, Grant-ratified 2026-07-21):** the
ontology-grade convention (IDENTITY / MODEL-OF / ANALOGY / IMPORT; header block)
plus eight core-noun nodes — `crystal` (`def-cryst1`, IDENTITY), `the impedance
analogy` (`def-1mpanl`, ANALOGY), `bond` (`def-b0nd01`, IDENTITY / MODEL-OF), `node
(lattice site)` (`def-n0det1`, IDENTITY / MODEL-OF), `lattice` (`def-latt1c`,
IDENTITY), `transmission-line segment` (`def-tls3g1`, MODEL-OF), `Cosserat
continuum` (`def-c0ss3r`, MODEL-OF regime-scoped), `vacuum` (`def-vacm01`,
IDENTITY). Grant basis verbatim `[sic]`: *"1) agree its an identity not
literal … 3) yup makes sense"*; the bond grade ratified mid-flight (`[sic]`:
*"yes rhat grade matches my perspective"*). The `def-tk1xfm` co-equality-below-
band-edge scope surfaced for its own ratification package (pending-rulings doc)
— **now RATIFIED proposed→SOLID, Grant 2026-07-21 (`[sic]`: "ratify def-tk1xfm");
executed in the #781 repair pass, with one carrier clause PENDING-GRANT-CONFIRM.**
**Longitudinal sector (2 nodes, added 2026-07-20, `docs/masterq-tag-vocab-defs`):**
`def-l0ngdu` (SOLID — ∇·u dynamical vs ∇·A gauge, Grant-ratified) + `def-uatk1s`
(proposed — u/A counterpart sector variables, inherits `def-tk1xfm`). Category-(a)
of the master-equation sector-dynamics harvest.

**Envelope sector (4 nodes, added 2026-07-21, `docs/envelope-vocab-defs`):**
category-(b) of the envelope-sector harvest (the follow-on after #767 merged) —
`def-envcar` (SOLID for the DECOMPOSITION only — envelope vs carrier, the
two-level split of the A1 breather; coupling verdict BIN-1-CONDITIONAL, not
hardened) + `def-satshr` (SOLID for the definitional SPLIT — saturation-shear
(traceless, observed GW) vs saturation-compression (trace, Q1 Reading-A LIVE
bulk port)) + `def-ncsatw` (proposed, WALK-RATIFIED DIRECTION — non-captured
(free) vs captured (bound) saturation wave; RECORD canonizes nothing) +
`def-pndenv` (proposed — ponderomotive envelope coupling; source structure banked
per #767, coefficient q1-inherited/ASSUMED). Receipts two-method at HEAD
`3d07ceeb`: `master-equation.md:20` (breather), #767 merged `5287ef32`, #768
merged `c12da9f5` (Abbott stamp), `port-register.md:87` (Q1 Reading-A LIVE), the
walk RECORD §4–§5. No walk-level or coupling claim hardened into canon.

**Post-merge canon-leaf principle/reading nodes (2 SOLID-for-the-name, added
2026-07-22, `docs/register-defrow-batch`):** the deferred vocabulary rows for the
two 2026-07-21 walk leaves, minted now that both names ratified **at merge** —
`the relative-offset principle` (`def-r0ffst`, SOLID for the Grant-ratified-at-merge
NAME, PR #787; the physics is DIRECTION-not-MAGNITUDE — `clm-hu1jjw` 0.50 /
`clm-m5swh9` OPEN) + `saturation rim-inversion` (`def-satrim`, SOLID for the
Grant-ratified-at-merge NAME, PR #790; the MAPPING `clm-riminv` 0.55, with the OPEN
necessity candidate `clm-satnec` and the channel-duality `clm-zdual1` 0.50). Both
are named PRINCIPLES / READINGS, **not** substrate nouns — no `ontology-grade`.
`def-satrim` carries **open-ambiguity YES** on the overloaded word "inversion"
(parity-meter `def-u0star` Sense B / TKI-invertible `def-tk1xfm` / Grant's parked
sign-flip / the MOS-inversion-layer cross-ref, KEEP-BOTH); `def-r0ffst` is
single-sense with read-guards vs `def-cc2196` "node" and `def-u0star`
"offset/bias". The `def-` grade locks the TERM only; each reading's solidity lives
on its `clm-` nodes.

**Symbol-collision node (1 ambiguous, added 2026-07-26, `docs/mstar-defnode-tracker`):**
`effective mass / m*` (`def-mstar1`) — the `m^*` disposition ruled by Grant
2026-07-26 (verbatim `[sic]`: *"correct, should not be a fitting parameter, a plus
c should make sense"* = option (a)+(c)). **KEEP-BOTH, two objects, one symbol:**
Sense A = the SM thermal-statistical FITTING PARAMETER, **struck and the strike
STANDS** (`19_silicon_design_engine.tex`:45, `11_experimental_falsification.tex`:463,
byte-untouched); Sense B = a **DERIVED / substrate-read inertia**, a distinct object,
**not struck** ($m_{eff}=m_e\sqrt{1+k}$; the emergent $M_{eff}$; the dressed-branch
acoustic $\rho_{eff}$). Grant's discriminator: **derived-not-fitted**. A distinct
Sense-B name, **dressed effective density**, is minted **proposed-for-ratification**
(0 prior corpus hits) with a surfaced dimension caveat. The node also records the
2026-07-26 finding that the literal $m^*=\hbar^2/(d^2E/dk^2)$ band-bottom curvature
read is **DECORATION** for the D1 sector-crossed-$c^2$ question (sector-blind: the gap
divides out) — the QUESTION's tracked anchor is
`research/2026-07-21_continuum-radial-solver_CHARTER.md`:15,:62; the FINDING has no
tracked home yet and is cited to this node. Discharges the `translation-circuit.md`:306
open flag (marked RULED, evidence preserved).

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


---

## "skin" (gradient skin) — disambiguation vs the EE skin effect
<!-- dated 2026-08-05; Grant-confirmed, core session -->

- **"Gradient skin"** (wall-taxonomy §3) is ANATOMICAL: the thin sub-yield boundary layer hugging a
  wall — a reactive stub. It is **NOT** the EE skin effect.
- The substrate **cannot host a skin effect** under Axiom 3: no conductivity, no eddy dissipation,
  no diffusive screening. Skin effect: $\arg(k) = 45°$, surface impedance with EQUAL real and
  imaginary parts ($Z_s = (1+j)/\sigma\delta$), material-set depth, dissipative. The wall region's
  decay: $\arg(k) = 90°$ (purely imaginary $k$ on the frozen antiphase pattern), ZERO real
  impedance, geometry-set decay constant, purely reactive (evanescent).
- **Discriminator = the real-part test:** any real part in a boundary-layer impedance is a defect
  (it imports dissipation; same class as "drag"/"friction") — except at a declared transfer-cost
  port ([`transfer-cost-theorem.md`](transfer-cost-theorem.md)).
- Preferred register for the wall-approach region going forward: the **semiconductor register**
  ([`translation-tables/translation-circuit.md`](translation-tables/translation-circuit.md),
  semiconductor-register additions): depletion edge / depletion width / junction two-port /
  reach-through.

---

## "infinite" / "divergent" (continuum-limit artifacts) — a math-level cage entry
<!-- dated 2026-08-05; Grant carve 2026-08-04, core session -->

- A divergence produced by a CONTINUUM-LIMIT calculation on the lattice imports the continuum's
  own theorems (true horizons, frozen coordinate time, infinite optical distance, unresolvable
  self-energies) — theorems the discrete substrate cannot host, since a finite node count admits
  no singular point. Before reading any continuum divergence as physics, check what the lattice
  regulator does to it: the regulated quantity is typically FINITE and LOG-ENHANCED, and the
  regulator leaves a computable signature (type case: the RHO-B optical distance — continuum
  log-divergent, lattice-regulated to a finite delay with the Euler–Mascheroni discrete
  correction; PR #876 carve + PR #880).
- This is the vocabulary-cage discipline one level down: not an imported WORD carrying a foreign
  theorem, but an imported LIMIT carrying its own singularity structure.
- Cross-refs: frontier queue row 25 (the discrete near-wall chain as the substrate-native
  instrument class); the `ave-infinity-discipline` skill; the Wilsonian reading in
  `_orchestration/2026-08-04_lorentz-compliance-arc-brief.md` (divergences mark where the
  continuum description is insensitive to the substrate).

---

## the LOCK vocabulary (phase-lock bond / lock range / free-running) — ⚑ PROPOSED, licenses nothing
<!-- dated 2026-08-06; Grant R17 (starting vocabulary, walk-level); NO def- id minted — see the gate note -->

- **status:** **PROPOSED** — adopted as the *starting* vocabulary for the bond's constitutive
  description, walk-level and **UN-AUDITED**. It is **not** canon, it **licenses nothing in
  print**, and no leaf may quote it as the mechanism of anything. Ruled at
  [`2026-08-06-rulings-final-batch.md`](../../../_orchestration/docket-entries/2026-08-06-rulings-final-batch.md):61
  (R17), Grant verbatim at `:63` — *"yes on 5, PLL makes sense or at least is the seemingly
  correct lens to start from, we might adjust vocab later but I like it"*. Source walk:
  [`research/2026-08-06_rotation-substance-ontology_framing-note.md`](../../../research/2026-08-06_rotation-substance-ontology_framing-note.md):101–127
  (§8 dated addendum) — whose own header reads *"still ⚑ UN-AUDITED"*.
- **no `def-` id is minted here, deliberately.** A `def-` node records a *locked* meaning and
  materializes into `claims.jsonl`; this vocabulary is explicitly not locked (R17: *"we might
  adjust vocab later"*). It lands in the dated-entry shape the two entries above use, so a grep
  for the words resolves here and reads the fence first.

**The proposed terms, each phase-scoped (crystal / boundary / de-bonded — a lock word with no
phase attached is a mis-use):**

| term | proposed meaning | phase scope |
|---|---|---|
| **phase-lock bond** | the bond as a phase-lock between adjacent rotors; freezing = the rotor field locking into one globally synchronized network (omega-freeze's common phase = the frozen chirality) | crystal |
| **compliance (lock sense)** | the lock's small-signal stiffness — what presents in the circuit register as capacitance | crystal |
| **lock range** | the drive amplitude a bond holds lock across; breakdown = drive past the lock range | crystal → boundary |
| **free-running** | the de-bonded phase: rotors not locked to neighbours, **dark by construction** (no bond sector ⇒ no EM coupling) | de-bonded |

**⚑ THE ADLER CARVE — load-bearing, and the reason this entry is not just "PLL".** Literal
PLL / injection locking imports a **dissipative attractor**: Adler locking needs a limit cycle,
i.e. gain plus loss. **Axiom 3 forbids that in the cold phase** — two lossless coupled
oscillators beat, they do not Adler-lock. The substrate-native object is **Hamiltonian resonance
capture**: phase-locked islands with KAM / Arnold-tongue structure, which exist with no
dissipation at all.

- **Survives the carve:** the lock range (= island width); the sharp threshold (= separatrix
  crossing); the dark free-running phase.
- **FORBIDDEN LANGUAGE:** *"settling into lock"*. Capture in a lossless system is a
  **boundary-crossing event**, not a relaxation. Any wording that implies decay toward an
  attractor has re-imported the dissipation the carve removed.
- Also retired by R17 in this register: **"melt"** as the C7 wording — melt-vs-breakdown
  dissolves into lock-loss under two control parameters (noise-driven vs drive-driven; canon's
  BH route is drive-driven, the primordial-freeze route is OPEN).

**Standing counter-arm carried WITH the vocabulary (C6, the addendum's own):** resonance-capture
islands in Hamiltonian systems are typically **fragile** — measure-zero-adjacent, with chaotic
separatrix layers. A vacuum-stable *global* lock needs the island to be LARGE and the capture
generic, and that is a **derivation obligation, not a given**. Until it is discharged the lock
lens is a picture, not a mechanism.

**Landing tiers, stated so no one over-reads this entry.** Framing-note addendum: landed. This
register entry: landed, PROPOSED, licenses nothing. The
[`translation-tables/translation-circuit.md`](translation-tables/translation-circuit.md) §4 row:
**QUEUED, not landed** — the mapping table stays canon-only until the residence / phase-register
lanes audit the picture.

---

### 🔴 Dated demotion note — 2026-08-11 (R40 demotion sweep, batch 1)

**Class: DIES-WITH-THE-PHANTOM.** Status change only — the claim text is **preserved
verbatim** (honesty-lag pattern, Rule 12) and stamped in place; it is **no longer live
canon**. Nothing is deleted.

**Demoted in this file:**

- **`:1054`** — *"Its trace projection = the saturation-COMPRESSION wave = the A1-bulk / scalar (breathing) channel = the pulsar-excluded bulk radiative port"*
  Stamped in place at `:1054`.
  **Why it dies (audited row rationale, verbatim):** def-satshr's compression-WAVE half requires the bulk radiative channel; the trace/traceless SPLIT of Q_ij survives as accounting (charge-not-flux, per the #919/#930 residue) and the traceless/shear half (observed GW at c) is untouched; the ridden Q1-Reading-A live-exclusion re-reads as the import's self-exclusion. Covers the :1199 batch-summary restatement.
  **Also covered by this demotion** (named in the audited row; not separately stamped): `:1199`.
- **`:1084`** — *"source $Q_{ij}\propto\int x_i x_j|A|^2$ radiating at $2\Omega$ into the gapless P-branch ... $\kappa_{env}^2 = A_{ang}(c_S/c_P)^5 = 0.034$"*
  Stamped in place at `:1084`.
  **Why it dies (audited row rationale, verbatim):** def-pndenv's far-field coupling: the (c_S/c_P)^5 partition has no referent when c_P is not a propagation speed (prereg verbatim for this family); the ponderomotive mass-quadrupole moment itself survives as source/dress accounting.
  *(R50 reading-note — the audited rationale predates R50 and is quoted byte-exact: where it writes
  "dress", the canonical noun is **the bound response**, mechanism gloss **back-reaction**.)*

**The arc, complete — the framing R40 rules every demotion note carries:**

1. **The kill fired** (#930) — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the #261 K = 2G import** (G-RECON, unchallenged): the compressible
   far-field branch was minted by a GR-imported elastic modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the #935 flat-direction finding: the written
   action conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the RATIFIED bound-sector law — Axiom 5, Substrate DC Bias**
   (BC-SRC clauses **S** / **G** / **Q**), ratified per `_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md`, as reconciled by `_orchestration/docket-entries/2026-08-10-ruling-r44-r43-reconciliation.md` (R44 — the
   full-scope R43 record is FINAL and authoritative; the partial
   `_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md` is SUPERSEDED and is **not**
   the resolution). Under the ratified law the A1 / bulk slot is a **bound response** — mechanism
   gloss **back-reaction** — with no independent propagating branch, no port, and zero longitudinal
   characteristic speed. A bulk *wave speed*, a bulk *radiative port*, a bulk *band-branch* and a
   bulk *transit clock* therefore have **no referent**.

**Standing named-open debt (the honest rider).** The ratified axiom does **not** discharge
everything: **THE BIAS PROPAGATION THEOREM** is Axiom 5's standing named-open entry — clause G's
elliptic law is the *static abstraction* of underived finite-speed bias dynamics (`_orchestration/2026-08-10_bias-propagation-brief.md`). Where a
demoted claim's replacement depends on finite-speed bias dynamics, the resolution is the ratified
axiom **with that debt open**, not a closed replacement.

**Records.** R40 ruling `_orchestration/docket-entries/2026-08-10-rulings-r40-r42.md` · verified worklist `research/drivers/r40_sweep_worklist_verified.json` · scope verification `_orchestration/2026-08-10_r40-sweep-scope-verification.md` ·
batch-1 record `_orchestration/2026-08-11_r40-sweep-batch1.md` · vocabulary R50 `_orchestration/docket-entries/2026-08-10-ruling-r50-vocab.md` (canonical: the displacement pattern u₀ around a
deposit is **the bound response**, mechanism gloss **back-reaction**; ε₁₁ is **the bias**;
"dress", "grade"-as-canonical-noun and "halo"-for-the-physics are retired; and the owed theorem is
renamed **THE BIAS PROPAGATION THEOREM**) · vocabulary **R49(b)** `_orchestration/docket-entries/2026-08-10-rulings-r48-r49.md` (*"retardation"
is RETIRED from this role. The canonical term is **propagation delay / finite propagation speed*** —
the retardation retirement is R49(b)'s, NOT R50's; corrected 2026-08-11 at review).

---

## R40 batch-2a — NEEDS-RE-DERIVATION status note (2026-08-11)

**Class:** status demotion under **R40**. This note mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`,
**moves no solidity number**, adjudicates no channel and opens no fork. Every byte of each demoted
claim is preserved; the stamped line gains a status marker only (honesty-lag pattern, Rule 12).

**The arc, in four clauses (R40's header form; clause 4 points at the LANDED artifact, not at a
ruling record).**

1. **The kill fired** — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the imported `K = 2G` elastic modulus** — the compressible far-field
   branch was minted by a GR-imported modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the flat-direction finding: the written action
   conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the LANDED ratified bound-sector law — Axiom 5, Substrate DC Bias**, clauses
   **S** (deposit), **G** (bias coupling / bridge) and **Q** (quiescence), canonical at
   [`eq_axiom_5.tex`](../../common_equations/eq_axiom_5.tex) with its register entry in
   [`axiom-register.md`](../common/axiom-register.md) (§ *Axiom 5 — Substrate DC Bias*). Under
   clause **G** the A1 / bulk slot is a **bound response** — $\mathbf{u}_0 =
   -\mathcal{A}_g\nabla\varepsilon_{11}$, mechanism gloss **back-reaction** — with **no independent
   propagating branch, no port and zero longitudinal characteristic speed**. A bulk *wave speed*, a
   bulk *radiative port*, a bulk *band-branch* and a bulk *transit clock* therefore have **no
   referent**, and each row below owes its re-derivation on that footing.
   $\mathcal{A}_g$ (the **bias-coupling area**) is an `UNVALUED-RATIFIED-CONSTANT` per **R48**
   ([`interlock-register.md`](../common/interlock-register.md), § *𝒜_g — the bias-coupling
   area*): it is **not valued here or anywhere**, and **the calibration count stays 3**.

**Standing named-open debt — the honesty rider.** The ratified axiom does **not** discharge
everything. **THE BIAS PROPAGATION THEOREM is Axiom 5's standing named-open debt**, stated by the
axiom's own phase-structure paragraph, clause **(c1)**: clause G's elliptic law is the *static
abstraction of underived finite-speed bias dynamics*, and the $(u,\pi)$ no-signalling theorem does
**not** cover the bias read — the bias's finite propagation speed is *owed, not held*. Every row
tagged **⚑ BIAS-DEBT** below re-derives against the ratified axiom **with that debt standing**, never
against a closed replacement.

**Vocabulary.** Canonical nouns authored here: **the bound response** ($\mathbf{u}_0$), **the bias**
($\varepsilon_{11}$), the **DC operating point / quiescent point (Q-point)**; **back-reaction** is
the mechanism gloss. *"dress"*, *"grade"* as $\varepsilon_{11}$'s canonical noun, and *"halo"* for
the physics (the physics noun is the **near-field store / added-mass**) are RETIRED by **R50**;
*"retardation"* is retired by **R49(b)** in favour of **propagation delay / finite propagation
speed**. Corpus text quoted below is reproduced from the banked audit and is
**content-verified at HEAD (markup-reduced, not byte-identical)**; it is never reworded.

**Rows carried in this file.**

- **`:575`** — stamped at `:575`. *(family: c_L P-wave register sense)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  the isotropic-solid longitudinal P-wave $c_L = \sqrt{(K+\tfrac{4}{3}G)/\rho} = \sqrt{10/3}\,c \approx 1.83c$ at $K=2G$ ($\nu=2/7$)
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  def-2e8d61 sense (d) loses its propagation referent (register-row class); sense (c)'s sqrt2*c port/impedance half survives; the :577 DEC-01 flag's bulk-precursor arm of the sqrt2c-front mode-identity fork is void under the carve — fork re-adjudicates toward T2.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

- **`:727`** — stamped at `:727`. *(family: three-channel Z_bulk formula)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  $Z_{EM}\equiv Z_0$, $\Gamma_{EM}=0$; $Z_{shear}=\rho c_{shear}$, $\Gamma_{shear}\to-1$; $Z_{bulk}=\sqrt2\,\rho c_0$ at $K=2G$, $\Gamma_{bulk}\to-1$
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  def-gv1net wires the bulk slot as a reactance CHANNEL with Z_bulk=sqrt2*rho*c0 — formula-level consumption (prereg-explicit); the network's bulk element re-derives as a controlled-source/bound-response element; the Gamma wall receipts survive in |Gamma|=1 form.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

- **`:870`** — stamped at `:870`. *(family: grad-u propagating half)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  One word each way — $\nabla\cdot\mathbf{u}$ propagates; $\nabla\cdot\mathbf{A}$ is gauge.
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Prereg-named propagating half; the real-vs-gauge constitutive distinction (anti-Heaviside, G-SCALAR-REAL) survives, but DYNAMICAL=rides-the-gapless-P-branch is the phantom — the split re-derives as bound-response-vs-gauge; covers :594 def-9a4f07 sharpen ("it is a propagating P-branch wave") and :885 def-uatk1s (u_parallel K-spring, propagating P-branch). SOLID Grant-ratified node — routed re-derivation, not a leaf edit.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

- **`:891`** — stamped at `:891`. *(family: GW170817 two-signals gate)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  gated on the GW170817 two-distinct-signals observational test (bulk radiates at $\sqrt{10/3}\cdot c \approx 1.83c$ vs the $|\Delta v|/c \lesssim 10^{-15}$ coincidence bound
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  The routed-open transverse identity-collapse question survives, but its gate's predicate (a second bulk signal at 1.83c to time against) is unsatisfiable under the carve — a new discriminator is owed for the frontier-queue routing.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

- **`:1069`** — stamped at `:1069`. *(family: free saturation wave; banked `uncertain`)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  NON-CAPTURED (free) — a radiated saturation wave: an open-contour disturbance propagating sub-rail
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  UNCERTAIN — def-ncsatw's bound/captured half (rail-touching soliton, Gamma=-1) survives as boundary class; the free/radiated half survives only if re-scoped to the T2/shear projection of the bias field and dies if read as an A1 compression wave; walk-level proposed node, cheap re-scope.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

## common-mode / differential *(ambiguous — Grant-confirmed 2026-08-24, R57 with the EE-native lead; the four registers of one word; a DISAMBIGUATION VIEW over canon rows, not a coinage)*
<!-- id: def-cmdiff -->

- **term:** common-mode / differential (surface form; four registers — see the ambiguity flag)
- **adjudicated-meaning:** **EE-native first (Grant instruction 2026-08-24, R57: "lead with EE native"):** the substrate is an ideal differential instrument — its common-mode rejection is *infinite by identity*, not engineered (a bench amplifier's CMRR is finite because its matching is built; here the reference co-transforms with the signal exactly, so the rejection is algebraic — canon's EP row states it verbatim: *"coupling-level CMRR infinite by identity"*). *(★ RE-SCOPED AT AUDIT 2026-08-24 — this node is a **DISAMBIGUATION VIEW**, RESTATEMENT-grade. The influence-class carve it was drafted to "coin" **already exists as canon translation rows**; this node points at them and separates them from three other live registers of the same word. It adds no physics.)* The surface form **common-mode / differential** carries **four distinct registers** in this corpus, two of which are near-opposites in physical status, so every use must name which. The register this package needs is the **canon INFLUENCE-CLASS row-pair**: *"Uniform external field | **Common-mode bias** — a uniform DC offset on the whole ladder (shifts every varactor's operating point together)"* / *"External field gradient | **Differential bias** — a bias gradient across the ladder (differential varactor operating points; the load-transfer / gravity-ledger direction)"* ([`translation-tables/translation-circuit.md`](translation-tables/translation-circuit.md):115-116), whose own third column already carries the self-cancellation reading — *"a uniform DC bias is gauge-relative and self-cancels (the common-mode component a differential measurement rejects)"* (`clm-acdc07` (i)). **The gauge/physical reading is therefore CANON, not new.** What the 2026-08-24 walk added is an ASSEMBLY: the same carve showed up on three unrelated legs in one day (chart floor MEASURED, ratio invariance algebra, vertex counting CANON) — recorded, not promoted. **Space declaration (A46):** this is a *classification of influences*, not an object; it applies per-space (the Class-C leg is an impedance-plane statement; the ratio-invariance leg is a phase-carrier statement; the vertex-counting leg is real-space/topological).
- **axis:** other — an influence-classification / surface-form disambiguation spanning axes (impedance-plane, phase-carrier, real-space); NOT a substrate-noun ontology node (hence no `ontology-grade`)
- **dimension/type:** n/a (a classification of influences and a surface-form disambiguation) — each instance carries its own dimension
- **status:** ambiguous — the surface form is overloaded across four registers with no single locked sense; the **influence-class register is already canon** (`translation-circuit.md:115-116` — *"**Common-mode bias** — a uniform DC offset on the whole ladder"*), so this node adjudicates the *overload*, not the physics. **GATED on Grant review.**
- **canonical-home:** [`translation-tables/translation-circuit.md`](translation-tables/translation-circuit.md):115-116 (the canon row-pair; `clm-acdc07` (i) on the :115 row) + [`envelope-anatomy.md`](envelope-anatomy.md):88 (*"uniform external field = common-mode bias; gradient = differential bias"*) and :119, quoted byte-exact to the end of the clause (round-2 m8 fix — the round-1 quote closed mid-phrase after *"operating"*): *"a common-mode / uniform bias shifts every operating point together but reflects nothing, $\nabla A=0$; a gradient is a differential bias → asymmetric Maxwell stress"*. Clause-Q gauge reading: `_orchestration/docket-entries/2026-08-24-ruling-r55-axiom5-source-law.md`:54 — *"**Clause Q is REFERENCE-FIXING.**"* (**not** `def-q1escn`, which is the Q-point *vocabulary* node — cross-node, not the source). Third assembly leg, the vertex-counting fact, quoted **byte-exact with the full path** (the draft trimmed the middle clause with no ellipsis): [`common/translation-tables/translation-circuit.md`](translation-tables/translation-circuit.md):189 — *"the bare junction reflects $\Gamma=(2-z)/z=-1/3$ (a COUNTING fact — one bond feeding two, immune to symmetric transformation)"*. Three-leg assembly recorded at [`research/2026-08-24_frame-invariance-observer-walk_RECORD.md`](../../../research/2026-08-24_frame-invariance-observer-walk_RECORD.md) §1 (**on `origin/main` since #1009**; the §1 table is `:29-32`). ⚑ **Round-2 corpus flag, surfaced not fixed:** that record's own `:32` cell carries the SAME quote **trimmed** — *"a COUNTING fact — immune to symmetric transformation"*, eliding *"one bond feeding two"* — and `research/2026-08-24_smith-annulus_result.md:83` carries a second trim (*"a COUNTING fact"* alone). This entry quotes the canon leaf byte-exact; the two trimmed on-main instances are routed to the auditor lane (packet **§CORPUS-FLAGS F2**), not edited here.
- **clm-cross-links:** clm-acdc07 (the AC/DC carve — the canon home of the gauge-relative/self-cancelling reading), clm-cmtwst (the twist-ledger conditional identity — register (c) below), clm-ppasym (path-participation asymmetry — the differential-bias row's claim)
- **open-ambiguity-flag:** YES — **four registers, KEEP-ALL. This node redefines nothing; it separates:**
  - (a) **EE-literal INSTRUMENT / measurement-channel sense** — amplifier and bench common-mode rejection; a measured channel, not an influence class. Bench receipt: [`cleave-01-requirements-boundary-conditions.md`](../vol4/falsification/ch11-experimental-bench-falsification/cleave-01-requirements-boundary-conditions.md):200 (*"a common-mode $dg/g$ tilts the inferred floor"*). ★ Also the **published-Letter optical instance**, which the draft missed entirely: `papers/2026_birefringence_letter/main.tex`:232,346,560,672,1220,1229 — the *polarimetric differential* vs the *interferometric common-mode index shift* (DeLLight Sagnac route), *"the differential being exactly twice the common-mode shift"*. This is the parent sense.
  - (b) **CANON INFLUENCE-CLASS sense** — the `translation-circuit.md:115-116` row-pair above. **This is the register this package needs, and it is already canon.**
  - (c) **twist-ledger MASS-LEDGER sense** — a generation-independent term cancelling from every mass DIFFERENCE ([`common-mode-twist-ledger.md`](../vol2/particle-physics/ch01-topological-matter/common-mode-twist-ledger.md), `clm-cmtwst`; itself **CONDITIONAL** and re-scoped 2026-08-03 — the leaf's own *"Class tag (read this first). Derived algebraic identity, CONDITIO…"* block at :10 and the :14 re-scope banner). A narrower instance of (a)'s logic at a different object.
  - (d) ★ **A1 SYMMETRIC-IRREP MODE GRADE — the direct cross-wiring hazard, and the reason this flag is YES.** In the port/irrep register, "common-mode" names the **+1 symmetric port-sum eigenspace = the A1 scalar/dilatation grade**, which is **the physical mass sector** — the exact opposite disposition from (b)'s gauge-relative/self-cancelling influence. Receipts: `src/ave/solvers/fork_b_saturation_tank.py`:30 (*"the bound mode lives in the A1 COMMON-MODE / SCALAR grade"*); `src/ave/solvers/node_scattering_multiplicity.py`:95 (*"common-mode (+1) eigenvector = the symmetric port-sum"*), :193, :322, :401, :461; [`port-register.md`](port-register.md):93 (*"the make-or-break mechanical $\nabla\!\cdot\!u$ common-mode derivation"* — landed **NONE-DERIVES**). **Rule: never read a common-mode MODE as a common-mode INFLUENCE.** A1 is a sector (mass); the influence class is a gauge statement. Per the sector-ownership A1⊥T2 watch, crossing these is a defect, not a shorthand.
  - conflicting sites: influence-class canon `translation-circuit.md:115,116` (*"a uniform DC offset on the whole ladder"*); anatomy restatement `envelope-anatomy.md:88,119` (*"uniform external field = common-mode bias; gradient = differential bias"*); instrument sense `cleave-01-requirements-boundary-conditions.md:200` (*"a common-mode $dg/g$ tilts the inferred floor"*); Letter optical sense `main.tex:1229` (*"the differential being exactly twice the common-mode shift"*); mass-ledger sense `common-mode-twist-ledger.md:10` (*"Derived algebraic identity, CONDITIONAL"*); A1 mode-grade `fork_b_saturation_tank.py:30` (*"the bound mode lives in the A1 COMMON-MODE / SCALAR grade"*), `node_scattering_multiplicity.py:95,193` (*"common-mode (+1) eigenvector = the symmetric port-sum"*), `port-register.md:93` (*"common-mode derivation landed **NONE-DERIVES**"*).
- **verification:** **★ THE DRAFT'S "71 prior corpus hits" DID NOT REPRODUCE AND IS WITHDRAWN** (no pattern, no scope stated). Re-measured at `origin/main` @ **`fc154aa6`** (round-2 re-pin; round-1 figures at `37926892` in parentheses), pattern + scope stated, two methods: `git grep -niI 'common-mode' origin/main | wc -l` → **441 lines** (was 429); `git grep -liI 'common-mode' origin/main | wc -l` → **164 files** (was 161); match-count cross-check `git grep -oiI 'common-mode' origin/main | wc -l` → **486** (was 474). By tree (`for d in manuscript src research _orchestration papers results; do git grep -niI 'common-mode' origin/main -- $d/ | wc -l; done`): manuscript **84**, src **78**, research **205**, _orchestration **58**, `papers/` **15**, `results/` **1**; sum **441** ✓ exhaustive. The +12 arrived with PRs #1009/#1010 and is all `research/` + `_orchestration/`. **The draft's implicit claim that all prior hits fall under senses (a)/(b) is likewise withdrawn** — register (d) refutes it, and 441 lines were not read. Receipts re-verified this round at `origin/main` @ `fc154aa6`: `translation-circuit.md:115-116` row-pair **verbatim present** (`git grep -nI 'Common-mode bias' origin/main -- manuscript/ave-kb/common/translation-tables/translation-circuit.md`); `envelope-anatomy.md:88,119` present; `cleave-01-…:200` present; `port-register.md:93` present; `fork_b_saturation_tank.py:30` and `node_scattering_multiplicity.py:95,193` present. `clm-acdc07`, `clm-cmtwst`, `clm-ppasym` each resolve in `claims.jsonl` (count → 1 each). **Grade honesty:** this node is **RESTATEMENT** over one canon row-pair plus a three-instance ASSEMBLY (walk record §1's own grading: MEASURED / elementary algebra (solid) / CANON). The slogan *"only differentials are physical"* is near-definitional under phase-only epistemology — the record's own tautology check says so verbatim (`:121-123`: *"'Only differentials are physical' is near-definitional under phase-only epistemology — the *content* is in the measured instances, not the slogan (tautology check)."*). **NOT SOLID.**

---

## detuned presentation *(SOLID — Grant-ratified 2026-08-24, R57)*
<!-- id: def-dtpres -->

- **term:** detuned presentation
- **adjudicated-meaning:** **Grant-ratified 2026-08-24 (R57, verbatim in the docket entry).** the appearance of a frame-invariant object under a **differentially-detuned reference** — the **presentation-vs-property carve**: a (2,3) winding at fixed frequency ratio paints the same knot forever; a uniform (common-mode) frame change preserves it; only differential detuning (ψ = 3t + α̇t) time-averages the knot into the torus. The torus is the *presentation* of the invariant object in a differentially-detuned reference, **not a property of the object**. **EE-native first — stated inside the register's own lock cage:** the Lissajous figure of a p:q-related oscillator pair on a scope whose two timebases are *differentially* detuned — the figure precesses and fills a band; the ratio relation is the property, the band is the presentation. ⚑ **This entry deliberately does NOT say "a locked pair" in the Adler sense** — see the read-guard in the ambiguity flag. **Space declaration (A46):** the presentation is a **phase-space** object (phasor/Clifford-torus portrait coordinates, `def-69f472`); it is NOT a real-space surface and must never be read against the real-space envelope anatomy (`def-anat3s`).
- **axis:** phase-carrier; NOT a substrate-noun ontology node (hence no `ontology-grade`)
- **dimension/type:** n/a (a presentation/appearance relation between an invariant and a reference)
- **status:** proposed — **0 prior corpus hits at `origin/main` @ `fc154aa6`**, three methods (regex / fixed-string / hyphen-variant), measured **after** the epic branch merged, so the round-1 "and 0 on the epic branch" method is now subsumed; gated on review. **NOT SOLID.**
- **canonical-home:** *(none — coinage)*; origin: [`research/2026-08-24_frame-invariance-observer-walk_RECORD.md`](../../../research/2026-08-24_frame-invariance-observer-walk_RECORD.md) §2 (**on `origin/main` since #1009**, `:41-58`); measured legs it organizes: **#417** (carrier-ratio detuning moves the orbit reading, 2:3 → 0.65) vs **#416** (the static Link does not move) — the dynamical carrier precesses, the topological charge doesn't.
- **clm-cross-links:** *(none minted — the #416/#417 claim ids attach only if the reading is ratified)*; cross-node: def-cmdiff (the detuning classes), def-rtlock (the property side), def-prstor (the presented object), def-69f472 (phase-space), def-satrim (the phase-space rim reading)
- **open-ambiguity-flag:** no — 0-hit coinage, single sense. ⚑ **Read-guard (not an overload record) — the ADLER CARVE travels with this entry.** The register's own standing LOCK-vocabulary entry (`## the LOCK vocabulary (phase-lock bond / lock range / free-running) — ⚑ PROPOSED, licenses nothing`) rules that *"Literal PLL / injection locking imports a **dissipative attractor**: Adler locking needs a limit cycle, i.e. gain plus loss. **Axiom 3 forbids that in the cold phase** — two lossless coupled oscillators beat, they do not Adler-lock."* and that *"a lock word with no phase attached is a mis-use"*, with **FORBIDDEN LANGUAGE:** *"settling into lock"*. This entry's scope needs only a **fixed frequency ratio** (Hamiltonian resonance capture at most), never an attractor: nothing here settles, decays, or acquires a lock range.
- **verification:** VERIFIED **0 prior corpus hits** for `detuned presentation` at `origin/main` @ **`fc154aa6`**, **three methods**: `git grep -niIE 'detuned presentation' origin/main | wc -l` → **0**; `git grep -nIF 'detuned presentation' origin/main | wc -l` → **0**; hyphen-variant `git grep -niIE 'detuned[- ]presentation' origin/main | wc -l` → **0**. ⚑ **Round-2 method change, stated:** at round 1 the two methods were *main* + *the then-unmerged epic branch*. **#1009 has merged**, so the branch content is now IN main and the on-main 0 is the stronger measurement — the branch-side method is retired as redundant, not dropped for convenience. The bare word `presentation` was re-checked for a technical prior sense and has none (no Wirtinger / braid / group-presentation usage; hits are "presentation-layer", "alt presentation"). **Grade honesty: the physics under this word is WALK** — the walk record's §2 is tagged *"[WALK, on canon legs]"* (`:41`) and its header states *"**Status: WALK-GRADE THROUGHOUT. Nothing here is a claim.**"* (`:3`); this def-node names the carve for reference, it does **NOT** upgrade it. **Both lines re-read byte-for-byte on `origin/main` @ `fc154aa6` after the #1009 merge — no drift** (the record's line numbers are identical branch-vs-main). The envelope≈probability-cloud resemblance in the same record's §4 counter-arms (*"Envelope ≈ probability-cloud is pure resemblance at this point — the payload-direction/echo check has NOT been run on it; do not promote."*, `:124-125`) is explicitly **not** part of this entry. **GATED on Grant review — NOT SOLID.**

---

## tube phase *(SOLID — Grant-ratified 2026-08-24, R57 addendum; canonical glyph **ϖ** (varpi); the (2,3) family parameter; ARC-ADOPTION, not a coinage)*
<!-- id: def-tubalf -->

- **term:** tube phase, glyph **ϖ** (varpi; LaTeX `\varpi`) — the (2,3) winding-family parameter. Ruled 2026-08-24 (R57 addendum); the walk/epic documents predate the ruling and write "α" — see the glyph flag.
- **adjudicated-meaning:** *(PROPOSED, gated)* the phase parameter of the (2,3) winding **family**: ψ → ψ + ϖ maps one family member to another. It is **NOT an invariant of the winding** — a uniform frame change / time-origin shift preserves the topological class while moving ϖ; only the class is the winding. Its operational consequence is the **ϖ-agnostic imposition guard** (static-existence epic §5 guard 8; the epic's frozen text predates the glyph ruling and writes the parameter "α" — quoted verbatim, glyph-independent in content): *"Imposing a specific α imposes MORE than the winding and smuggles un-owned structure into the relaxed state. The G1-walked imposition must be α-agnostic (the class, or the family)."* **EE-native first — inside the register's lock cage:** the free absolute phase of an oscillator sitting at a fixed frequency ratio to a reference; specifying that phase specifies the reference, not the ratio. ⚑ **The draft's "a synthesizer locked N:M" framing is WITHDRAWN** — see the read-guard. **Space declaration (A46):** a phase-carrier angle on the phase-space portrait; **not** a real-space angle, and specifically not the real-space **tube radius** — see the glyph/word flag. **⚑ Q2 EVIDENCE (2026-08-24, recorded at ratification review):** on first meeting this entry Grant asked, verbatim, *"this is the geometric justification for using alpha as one of the three calibration inputs?"* — the glyph collision generating a false identification in the adjudicator's own hands within one turn. Answered NO (homonym; the nearest real bridge is the operating-point AMPLITUDE $A=\sqrt{\alpha}$, a different quantity, itself value-imported). This near-miss is the live-fire case for re-deriving a distinct glyph.
- **axis:** phase-carrier; NOT a substrate-noun ontology node (hence no `ontology-grade`)
- **dimension/type:** dimensionless angle (radian)
- **status:** proposed — gated on review. ⚑ **Enum-gloss deviation, disclosed:** the register's legend glosses `proposed` as *"coined, 0 prior corpus hits, gated on review"* (`vocabulary-register.md:57`). **This term is NOT a 0-hit coinage** — it is already in use across this arc (V6 below). It is one sense, so `ambiguous` does not fit either; `proposed` is used for the *gated* half of the gloss, and the deviation is surfaced here rather than papered over. **Grant's call if the enum should be read differently. NOT SOLID.**
- **canonical-home:** [`_orchestration/2026-08-24_static-existence-epic.md`](../../../_orchestration/2026-08-24_static-existence-epic.md) §5 **guard 8 (`:149-155`)** + [`research/2026-08-24_frame-invariance-observer-walk_RECORD.md`](../../../research/2026-08-24_frame-invariance-observer-walk_RECORD.md) §2 (`:41-58`) / §5 (`:136-139`) — **both ON `origin/main` since PR #1009 (`fc154aa6`); the `[branch:static-existence-epic @ f29cb576]` tags are RETIRED.** ⚑ **Line drift measured, not assumed:** guard 8 was at `f29cb576:139-145` and is at **`origin/main:149-155` (+10 lines)** — re-pinned here. The walk-RECORD line numbers did **not** drift and are re-pointed unchanged. **On-main prior use (same sense, same arc):** [`research/2026-08-24_smith-annulus_expectations_FROZEN.md`](../../../research/2026-08-24_smith-annulus_expectations_FROZEN.md):75, plus six more files now on main (V6).
- **clm-cross-links:** *(none — the guard is orchestration process, not a claim)*; cross-node: def-dtpres, def-prstor, def-rtlock, def-69f472
- **open-ambiguity-flag:** YES — **GLYPH COLLISION plus a WORD adjacency; this is the reason the entry exists:**
  - **(1) GLYPH: "α".** The walk and the epic write the family parameter **"α"**, colliding with the **fine-structure constant α** — the corpus's most load-bearing glyph (α-echo, $A^2_{yield}=2\alpha$, $|\Gamma_J(\sqrt\alpha)|$…). Both objects are live *in the same documents' subject matter*: the electron's A1 operating point is $A=\sqrt\alpha$ ([`nonlinear-vacuum-capacitance.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md):36; `def-vyvsn1`) while its family parameter is written "α". **Recommendation (Grant-gated): confine bare "α" to the fine-structure constant; until ruled, every use of the family parameter must carry the words "tube phase".** ⚑ **ROUND-2 CHANGE — THE CANDIDATE-GLYPH MENU IS WITHDRAWN AS DECISION-INPUT.** Round 1 offered Grant two mints, **φ_t** (*"zero corpus collision"*) and **ϑ** (*"currently unclaimed"*). **Both claims were asserted without a stated pattern, scope or SHA, and both fail on re-grep at `origin/main` @ `fc154aa6`** (V11/V11a/V11b): `git grep -nIF '\vartheta' origin/main | wc -l` → **7 lines / 2 files**, six of them `$\vartheta_{\mathrm{coll}}$` = **the collision angle in the published birefringence Letter** (`papers/2026_birefringence_letter/main.tex:594,595,630,635,685,689`) — *the same file this package's `def-cmdiff` register (a) cites*; and `git grep -nIF 'φ_t' origin/main | wc -l` → **5 lines / 4 files**, of which `src/ave/utils/fast_winding_extractor.py:53` (`cos(qψ)·cos(φ_t)`) is a **literal torus phase in the standing-mode formula** — the same phase-space (p,q)-winding machinery this term lives in. **This was exactly the grep-completeness failure mode the whole repair round was about, reintroduced inside a collision-hygiene package.** No replacement menu is offered here: **the glyph question goes back to Grant with the collisions shown** (packet T3), because minting a third candidate from this lane would repeat the error that a candidate is only "free" relative to a stated pattern. **★ RESOLVED 2026-08-24 (R57 addendum) — Grant, verbatim: *"ruled fir varpi"*. Canonical glyph: ϖ.** Derivation: celestial mechanics' longitude of pericenter — the canonical angle-valued family selector ("at which orientation did this family member freeze"), exactly the tube-phase role. Double-swept clean at `fc154aa6`: 0 hits in unicode/LaTeX/code-identifier forms across the pinned tree AND the whole workspace, by two lanes with independently-constructed patterns (the derivation lane + the verify lane's own availability sweep; the round-3 candidate ψ₀ was KILLED at verification — 3 distinct objects incl. the vol_4 published surface, and the subscript-0 misread biases the #416/#417 static-vs-orbit fork). **Bare "α" is now confined to the fine-structure constant BY RULE.** Propagation: the frozen walk/epic/packet documents keep their historical "α" (dated documents, not rewritten); the epic guard-8 wording update rides the next orchestration PR; the channel repo's `smith_sim.py` carries the parameter as `alpha` in code — a cross-repo followups row for their court.
  - **(2) WORD: bare "tube".** Canon's **tube radius** is a **real-space** length — [`electron-identification.md`](../vol2/particle-physics/ch01-topological-matter/electron-identification.md):30, verbatim: *"Tube circumference $\ell_{node}$, tube radius $\ell_{node}/(2\pi)$, loop length $2\pi \cdot \ell_{node}$"* (restated at :122). "Tube **phase**" is a **phase-space** angle. Bare "tube" now sits astride the A46 fence: **never use it alone** — say "tube radius" (real-space) or "tube phase" (phase-space).
  - conflicting sites: real-space tube radius `electron-identification.md:30,122`; fine-structure α operating point `nonlinear-vacuum-capacitance.md:36` and `vocabulary-register.md:757`; the arc's own tube-phase uses `2026-08-24_smith-annulus_expectations_FROZEN.md:75`, `2026-08-24_frame-invariance-observer-walk_RECORD.md:54`, `2026-08-24_g1-ac-steady-state-walk_RECORD.md:103`, `2026-08-24_static-existence-epic.md:151`, `2026-08-24_static-existence-build-brief.md:77`, `2026-08-24_static-existence-g1-walk-packet.md:90`, `2026-08-24_static-existence-p0-capability-report.md:346`; the withdrawn glyph candidates' own collisions `main.tex:594,595,630,635,685,689` (ϑ_coll) and `fast_winding_extractor.py:53` (φ_t).
  - ⚑ **Read-guard — the ADLER CARVE travels.** The draft's EE line (*"a synthesizer locked N:M has a free absolute phase"*) imports PLL/injection-locking language the register's own standing **LOCK vocabulary** entry already fences: *"Literal PLL / injection locking imports a **dissipative attractor**… **Axiom 3 forbids that in the cold phase** — two lossless coupled oscillators beat, they do not Adler-lock. The substrate-native object is **Hamiltonian resonance capture**"*, plus *"a lock word with no phase attached is a mis-use"* and **FORBIDDEN LANGUAGE:** *"settling into lock"*. Restated without the cage violation: this parameter is the free phase of a **fixed-ratio** family; nothing here needs a lock range, an attractor, or gain-plus-loss.
- **verification:** **★ THE DRAFT'S "0 prior corpus hits for `tube phase`" IS FALSE AND IS WITHDRAWN.** **★ ROUND-2 RE-PIN — the branch-side method is retired; everything is now an on-main measurement.** Re-measured at `origin/main` @ **`fc154aa6`**, three methods: `git grep -niIE 'tube[- ]phase' origin/main | wc -l` → **7 lines**; `git grep -liIE 'tube[- ]phase' origin/main | wc -l` → **7 files**; per-file `git grep -ciIE 'tube[- ]phase' origin/main` sums to **7** ✓. The seven files are the build-brief (`:77`), the epic (`:151`), the G1 walk packet (`:90`), the P0 capability report (`:346`), the frame-invariance RECORD (`:54`), the G1 AC-steady-state RECORD (`:103`) and the FROZEN expectations (`:75`) — *the same seven the round-1 count found on the epic branch*, now on main via **#1009**. *(Round-1 figures at `37926892`: **1** on main + **7 files** on the then-unmerged branch.)* **All hits are the same sense from the same arc**, so this is an **ARC-ADOPTION** — a term already in lane use being brought under the gated register — not a coinage. `git grep -nI 'tube radius' origin/main -- '*electron-identification.md'` → **:30, :122**; **the draft's `:77` cite was WRONG** (`:77` is the (2,3) Clifford-torus Rule-12 re-scope row, no tube content) and is corrected to **:30** above. **Guard-8 text re-read verbatim ON MAIN at `:149-155` this round** — it moved **+10 lines** from `f29cb576:139-145` across the merge, and the canonical-home cite above is re-pinned to the current lines (round-1's `:139-145` would now land in §5 guards 5-7). The glyph-candidate collision counts V11/V11a/V11b were measured this round and are the basis for withdrawing the round-1 menu. **Grade honesty:** the non-invariance statement is elementary algebra (the walk record's own §1 grading, *"elementary algebra (solid)"*, `:31`); the guard is epic-ratified **process**, not physics. **GATED on Grant review — NOT SOLID.**

---

## ratio lock *(ambiguous — Grant-confirmed 2026-08-24, R57; a RESTATEMENT + disambiguation pointer, NOT a coinage)*
<!-- id: def-rtlock -->

- **term:** ratio lock (surface form; **two distinct technical objects** in this corpus — see the ambiguity flag)
- **adjudicated-meaning:** *(★ RE-SCOPED AT AUDIT 2026-08-24 — the draft's coinage claim died on re-grep (V1/V2 below, re-pinned to `fc154aa6`: **26 lines / 10 files**, of which **25 lines / 9 files predate this arc**, including literal `ratio lock` tokens). This node is now a **RESTATEMENT of an elementary-algebra fact + a disambiguation pointer** at the pre-existing ORG-1 ratio-locking family. It coins nothing and adds no physics.)* Under a **uniform (common-mode) clock rescale** both frequencies of a p:q-related pair scale together and **the ratio is exactly invariant**; **only differential (mode-asymmetric) detuning changes it** — and then produces the detuned presentation (`def-dtpres`). That invariance is **elementary algebra**, nothing more. **EE-native first — stated inside the register's lock cage:** a frequency **ratio** is dimensionless, so it is blind to any common rescale of the timebase; only relative drift between the two moves it. ⚑ **The draft's *"injection locking / PLL ratio lock is bedrock EE"* line is WITHDRAWN as a cage violation** — see the read-guard. **The candidate reading** — *identity lives in the frame-invariant part; the substrate stores identity topologically because the integer/ratio structure is what survives every common-mode change* — is **WALK** (record `:56-58`, tagged `[WALK.]`), named here without promotion. **Space declaration (A46):** a dimensionless relation between phase-carrier frequencies; not a spatial object.
- **axis:** dimensionless (a ratio between phase-carrier frequencies); NOT a substrate-noun ontology node (hence no `ontology-grade`)
- **dimension/type:** dimensionless (frequency ratio; for the electron case p:q coprime integers)
- **status:** ambiguous — the surface form names **two different technical objects** with no locked sense (see flag). **GATED on Grant review — NOT SOLID.** ⚑ **the keep-vs-decline fork was CLOSED by R57 disposition A5 (2026-08-24): KEEP-as-restatement — this sentence originally offered a live DECLINE and is superseded by that ruling** (packet T4): if the ORG-1 family owns the words, this node should be dropped and the invariance carried as one clause inside `def-dtpres` instead of minting a colliding surface form.
- **canonical-home:** *(no canonical home for the term — see status).* The **invariance** is elementary algebra; the walk record grades it *"elementary algebra (solid)"* at [`research/2026-08-24_frame-invariance-observer-walk_RECORD.md`](../../../research/2026-08-24_frame-invariance-observer-walk_RECORD.md):31 (**on `origin/main` since #1009**; line unchanged across the merge, re-read at `fc154aa6`). ★ **CANON-LABEL CORRECTION (the draft smuggled a label):** the draft wrote *"the (2,3) lock the term names is CANON ([`boundary-observables-m-q-j.md`](boundary-observables-m-q-j.md))"*. **That leaf contains no lock language at all** — `git grep -ncI 'lock' origin/main -- manuscript/ave-kb/common/boundary-observables-m-q-j.md` → **1**, and the one token is **"lockstep"** inside a $k_{\max}$ relabel note at `:106`. What **is** canon there is the **WINDING**: `:54`, verbatim — *"its $(2,3)$/trefoil structure is the phase-space (Clifford-torus) winding label, not the real-space body"*. **So: the (2,3) WINDING is CANON; the frequency-LOCK reading of it is WALK** ([`research/2026-08-24_frame-invariance-observer-walk_RECORD.md`](../../../research/2026-08-24_frame-invariance-observer-walk_RECORD.md) §1 row 2 = `:31`, on `origin/main` since #1009). Canon owns the (2,3) as a **STATIC imposed Link** under the **#416** two-natured ruling, and the nearest **dynamical** lock test reads **NEGATIVE** — `def-satrim` (`vocabulary-register.md:1130`), verbatim: *"charge = the STATIC imposed Link per the #416 two-natured ruling, and the nearest DYNAMICAL charge-winding tests read NEGATIVE (#415 real-space eigensolve, #59 phase-space carrier-lock)"*.
- **clm-cross-links:** *(none minted)*; cross-node: def-cmdiff (the influence classes), def-dtpres (what differential detuning presents), def-kn0t01, def-satrim (the #59 carrier-lock NEGATIVE), def-prstor
- **open-ambiguity-flag:** YES — **two technical objects under one surface form, KEEP-BOTH:**
  - **(a) ORG-1 ringdown ratio-locking (PRIOR, established, named forward-prediction organizer).** *"MODE-RATIO LOCKING"* — the black-hole soft-mode transition's dimensionless elastic ratios freezing while absolute moduli collapse; a full derivation doc, a frozen prereg, a checks script, a manuscript FOREWORD forward-falsifier, and docket rulings. Receipts: `research/2026-07-20_ringdown-systematics_derivation.md:23` (*"## §1 — ORG-1: MODE-RATIO LOCKING (full derivation)"*), :39, :79, :197, and **:200 — a literal `ratio lock` token**: *"**ORG-1 damping/τ-ratio lock** | **DERIVED-AND-TESTABLE at `a*=0` ONLY; spin-behavior UNDETERMINED**"*; `research/2026-07-20_ringdown-systematics_prereg-FROZEN.md:6,24,33,46,78`; `research/2026-07-20_ringdown-systematics_checks.py:7,102,104,130` (:130 *"Damping-ratio locking"*); `manuscript/frontmatter/00_foreword.tex:133` (*"multipole ratio-locking"*); `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/first-principles-predictions.md:22`; `research/2026-07-20_vacuum-metallurgy_kz-relic-and-instruments.md:179,184`; `research/2026-07-30_qlaw-derivation_scoping.md:237`; `_orchestration/2026-07-10_rulings-docket.md:2454,2628,2633,2642,2744`; `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md:259`.
  - **(b) THIS node — the (2,3) p:q frequency-ratio invariance** under common-mode clock rescale. Different object (a winding's carrier ratio, not a BH multipole/damping spectrum), different sector, different grade.
  - **Rule:** a reader meets **two** technical "ratio lock" objects. Never write bare "ratio lock" — write **"ORG-1 mode-ratio locking"** (a) or **"the (2,3) carrier-ratio invariance"** (b).
  - conflicting sites: ORG-1 family `2026-07-20_ringdown-systematics_derivation.md:23,200`, `2026-07-20_ringdown-systematics_prereg-FROZEN.md:33,78`, `2026-07-20_ringdown-systematics_checks.py:130`, `00_foreword.tex:133`, `first-principles-predictions.md:22`, `2026-07-20_vacuum-metallurgy_kz-relic-and-instruments.md:179,184`, `2026-07-30_qlaw-derivation_scoping.md:237`; the winding canon `boundary-observables-m-q-j.md:54`; the #59 NEGATIVE `vocabulary-register.md:1130`.
  - ⚑ **Read-guard — the ADLER CARVE travels, and it is load-bearing here.** The register's standing **LOCK vocabulary** entry rules: *"Literal PLL / injection locking imports a **dissipative attractor**: Adler locking needs a limit cycle, i.e. gain plus loss. **Axiom 3 forbids that in the cold phase** — two lossless coupled oscillators beat, they do not Adler-lock. The substrate-native object is **Hamiltonian resonance capture**: phase-locked islands with KAM / Arnold-tongue structure, which exist with no dissipation at all."* — with *"a lock word with no phase attached is a mis-use"* and **FORBIDDEN LANGUAGE:** *"settling into lock"*. It also carries a **standing counter-arm**: *"resonance-capture islands in Hamiltonian systems are typically **fragile**… A vacuum-stable *global* lock needs the island to be LARGE and the capture generic, and that is a **derivation obligation, not a given**."* **Consequence for this entry:** the *word* "lock" here must be read as a **fixed ratio** (a kinematic statement about an imposed winding), **not** as an Adler/PLL capture. Nothing in this node licenses a lock range, a capture threshold, or a settling process.
- **verification:** **★ THE DRAFT'S "VERIFIED 0 prior corpus hits for `ratio lock`; 1 hyphenated adjacent hit" IS FALSE AND IS WITHDRAWN.** Re-measured at `origin/main` @ **`fc154aa6`** (round-2 re-pin), two methods plus a per-file cross-check: `git grep -niIE 'ratio[- ]lock' origin/main | wc -l` → **26 lines**; `git grep -liIE 'ratio[- ]lock' origin/main | wc -l` → **10 files**; match-count cross-check `git grep -oiIE 'ratio[- ]lock' origin/main | wc -l` → **27**; per-file sum `git grep -ciIE 'ratio[- ]lock' origin/main` → 5+1+1+1+4+5+5+2+1+1 = **26** ✓. *(Round-1 at `37926892`: 25 / 9 / 26. The +1 line / +1 file is the walk RECORD `:31` arriving with #1009 — sense (b), this package's own arc, so the ORG-1 family's count is unchanged at 25.)* The **space-form token itself** is in prior use: `git grep -niIE 'ratio lock' origin/main | wc -l` → **22 lines** (was 21). **Root cause of the false negative:** the draft ran an exact-token grep and read its 0 as a corpus fact — the documented grep-completeness failure mode (a completeness claim from a search is a claim about the pattern). Canon-label check re-run: `git grep -ncI 'lock' origin/main -- manuscript/ave-kb/common/boundary-observables-m-q-j.md` → **1**, token = `lockstep` (`git show origin/main:…/boundary-observables-m-q-j.md | sed -n '106p' | grep -oiE '[a-z-]*lock[a-z-]*'`). Register LOCK entry located and read this round: `git grep -nI 'ADLER' origin/main -- manuscript/ave-kb/common/vocabulary-register.md` → **:1343** (the carve), heading `## the LOCK vocabulary (phase-lock bond / lock range / free-running) — ⚑ PROPOSED, licenses nothing`. `def-satrim`'s #59-NEGATIVE sentence re-read verbatim at `vocabulary-register.md:1130`. **Grade honesty:** the invariance is solid algebra (RESTATEMENT); the identity-storage reading is **WALK**; the (2,3) itself is canon **as a static winding**, and its *dynamical* lock reading has a recorded **NEGATIVE**. **GATED on Grant review — NOT SOLID; DECLINE is a live option.**

---

## response map *(SOLID — Grant-ratified 2026-08-24, R57, WITH the in-lattice caveat; ARC-ADOPTION post-#1007/#1010)*
<!-- id: def-rspmap -->

- **term:** response map (vs orbit)
- **adjudicated-meaning:** **Grant-ratified 2026-08-24 (R57, verbatim in the docket entry).** **Γ(A)**: the medium's reflection-coefficient locus as a function of **hypothetical** amplitude — **a property of the MEDIUM, disjoint from any state's trajectory** (the annulus carve, measured Class-C). The [1/3, 1] annulus is *the image of the response map Γ_J over the hypothetical amplitude range [0, A_y]*; **no canon statement makes any physical amplitude execute that swing** — the standing electron sits FIXED at the operating point $|\Gamma_J(\sqrt\alpha)| = 0.334147$, **0.12% into the annulus**, and does not sweep. **"Orbit" (a state's trajectory) and "response map" (the medium's locus) must never be conflated**; the `vcanon-3` MAJOR repair on the smith-annulus lane is the precedent this term fossilizes. **EE-native first:** a network analyzer's S11-vs-drive curve is a property of the DUT — sweeping the analyzer does not mean the operating circuit sweeps. **Space declaration (A46):** an impedance-plane (Smith-chart) locus; its domain is the DP-1 reactive-amplitude envelope $A$ (dimensionless normalized strain), its codomain Γ (dimensionless); neither is a real-space contour.
- **axis:** other — an impedance-plane map (dimensionless $A \mapsto$ dimensionless Γ); NOT a substrate-noun ontology node (hence no `ontology-grade`)
- **dimension/type:** map, dimensionless → dimensionless
- **status:** proposed — gated on review. ⚑ **Enum-gloss deviation, disclosed** (same shape as `def-tubalf`): the term is no longer 0-hit on main post-#1007/#1010 (V5: **21 lines / 7 files**), but all prior hits are this arc's own, one sense. **NOT SOLID.**
- **canonical-home:** [`research/2026-08-24_smith-annulus_result.md`](../../../research/2026-08-24_smith-annulus_result.md):254-255 — **on `origin/main` since #1007**; the §3.4 H2 re-headline, verbatim across the two lines: *"**H2 — PASS for FORM J only, RE-HEADLINED at repair: the annulus is the medium's response map, not any orbit the electron takes.**"*; the map statement at `:265-267`. ★ **ROUND-2 ADDITION — the canonical home is now a PAIR, not a single doc.** PR **#1010** (`119ef8f2`) landed the **engine Γ(A) means-test**, which measured this same map *on the lattice*: [`research/2026-08-24_engine-gamma-meanstest_prereg_FROZEN.md`](../../../research/2026-08-24_engine-gamma-meanstest_prereg_FROZEN.md) (`:37` — *"This test measures the **MEDIUM'S RESPONSE MAP**"*; `:40` — *"is the response map, not an orbit"*, i.e. this entry's carve is the frozen prereg's own guard) + [`research/2026-08-24_engine-gamma-meanstest_result.md`](../../../research/2026-08-24_engine-gamma-meanstest_result.md) (`:34`, `:444`). **The lumped smith-annulus doc is the map's ANALYTIC home; the means-test pair is its MEASURED home, and the two disagree at the `A=0` endpoint — see rider (a).** Operating-point pin: `vocabulary-register.md:757` (`def-vyvsn1`, the $V_{yield}/V_{snap} = \sqrt\alpha \approx 0.0854$ α-lock) + [`nonlinear-vacuum-capacitance.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md):36 (*"**Note the electron's A1 mass-core operating point** $A=V_{yield}/V_{snap}=\sqrt\alpha\approx0.085$"*).
- **clm-cross-links:** *(none — the smith-annulus lane and the means-test lane both mint **no** `clm-`, so there is nothing to attach)*; cross-node: def-vyvsn1 (the fixed operating point), def-envl0p Sense B / DP-1 (the domain variable $A$), def-satrim (the phase-space rim), def-cmdiff (the differential-bias leg)
- **open-ambiguity-flag:** no — no competing technical sense; the 21 prior hits (V5) are this arc's own documents in this exact sense. **But two mandatory riders travel with the term** (read-guards, not overload records):
  - **(a) the LUMPED-STEP caveat — ★ AMENDED IN ROUND 2 WITH AN IN-LATTICE CAVEAT.** *As drafted:* every intermediate-A value of the measured map is a step-family artifact; **only the endpoints ($|\Gamma| = 1/3$ and $1$) are profile-robust**. Verbatim at `research/2026-08-24_smith-annulus_result.md:271-281`: *"Every intermediate-A number in this draft … is a lumped-step-family artifact; only the endpoints are profile-robust"*, and the same block flags that FORM J as implemented *"grades the ENTIRE semi-infinite far arms uniformly, which no localized winding can do."* ⚑ **IN-LATTICE CAVEAT (forced by PR #1010, merged after the round-1 pin — a lumped-map statement is NOT automatically a lattice statement):** the `1/3` endpoint of that "profile-robust" pair **does not survive as a measured lattice floor**. `research/2026-08-24_engine-gamma-meanstest_result.md:214-215`, verbatim: *"the outcome the prereg's own floor-honesty note foresaw (T4 homogenization: the −1/3 intercept belongs to the isolated vertex, **which does not exist in-lattice**)"*; `:305-306` — *"no floor was measurable at either stepped config; no crossing existed to compare"*; `:447-449` — *"no measurable −1/3 floor — and quantitatively it draws the **core** locus (z = √S plane-interface reflection) to ~1 %"*. **Rule for any use of this term:** the `[1/3, 1]` annulus is a statement about the **lumped analytic map**, whose `A=0` endpoint is an **isolated-vertex idealization**; the lattice measurement of the same map draws the **core** locus with **no floor**. Never cite the `1/3` endpoint as a measured in-lattice value. **Whether the annulus framing survives as written is a live Grant question, put in the adjudication packet — it is surfaced here, not resolved.** *(flag-don't-fix: the lumped map and the lattice run are not formally the same object, but a def-node exists to be cited **without** its context, and this one's whole purpose is preventing map-vs-orbit conflation.)*
  - **(b) the SIDE-ASSIGNMENT FORK (FORM J vs FORM B) is OPEN** — `:250-252`: the prior *"the chart declaration selects FORM J"* argument *"was CIRCULAR … withdrawn. **The side-assignment fork stands fully open as STUCK-POINT #2.**"* **"The response map" without a FORM tag is underspecified off the endpoints.** ★ **Round-2 status: rider (b) SURVIVES the means-test unchanged, and is now doubly sourced.** `research/2026-08-24_engine-gamma-meanstest_result.md:298-300`, verbatim: *"**No §6.4 row fires for the J/B pair; the J/B side-assignment fork is NOT adjudicated by this run and remains open on the B side.**"* (G-B returned INVALID-EXTRACTION, which is neither "draws B-class" nor "NONE"). So the run that amended rider (a) **confirms** rider (b).
- **verification:** Re-measured at `origin/main` @ **`fc154aa6`** (**post-#1007, post-#1009, post-#1010**), two methods: `git grep -niIE 'response[- ]map' origin/main | wc -l` → **21 lines**; `git grep -liIE 'response[- ]map' origin/main | wc -l` → **7 files**; match-count `-oiIE` → **21**. **All seven files enumerated** *(the round-1 field cited a "4 hits / 2 files" count but enumerated only 3 of the 4 lines — the round-2 m7 fix is the full enumeration, not a partial one)*: `research/2026-08-24_smith-annulus_result.md` (`:255,:265,:495`), `research/2026-08-24_engine-gamma-meanstest_prereg_FROZEN.md` (`:29,:31,:37,:40,:50,:96,:99,:302,:308,:309`), `research/2026-08-24_engine-gamma-meanstest_result.md` (`:34,:45,:444`), `_orchestration/2026-08-24_static-existence-build-brief.md` (`:17,:54`), `_orchestration/2026-08-24_static-existence-epic.md` (`:71`), `_orchestration/open-items/2026-08-24-smith-annulus-tube-ratio-pin.md` (`:188`), `_orchestration/open-items/2026-08-24-static-existence-epic-tracker.md` (`:29`). **All 21 are the same sense** (the medium's Γ(A) locus). **The draft's "0 prior corpus hits on main" was TRUE at drafting time and is now STALE by two merges** — not an error; the entry is re-scoped to arc-adoption and the count re-stated at each pin (0 → 4 → 21). **All smith-annulus receipts re-verified at `origin/main` @ `fc154aa6` line numbers this round (they did not shift across either merge):** H2 re-headline `:254-255`; $|\Gamma_J(\sqrt\alpha)| = 0.334147$ / 0.12% `:263`; the image-of-the-map sentence `:265-267`; lumped-step caveat `:271-281`; STUCK-POINT #2 `:252`; `vcanon-3 (MAJOR)` repair row `:495`; symmetric end-bias dev `5.6e-17` `:369,:387`; differential split agreeing to `1e-13` `:383`. Operating-point pins re-read: `vocabulary-register.md:757`, `nonlinear-vacuum-capacitance.md:36` (full path confirmed via `git ls-tree -r --name-only origin/main | grep nonlinear-vacuum-capacitance` → `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/`). Means-test receipts read this round at `fc154aa6`: `:214-215`, `:298-300`, `:305-306`, `:447-449`. **Grade honesty, re-stated after #1010: the LUMPED map is analytic with two profile-robust endpoints; the LATTICE map is MEASURED and shows no floor at `A=0`, drawing the core locus to ~1% instead.** The term is bookkeeping over both; **the two do not agree at the `A=0` endpoint, and this entry surfaces that rather than reconciling it** (flag-don't-fix — Grant adjudicates, per the packet question). The side-assignment stays open on the B side. **GATED on Grant review — NOT SOLID.**

---

## presentation torus *(SOLID — Grant-ratified 2026-08-24, R57; the envelope-collision fix)*
<!-- id: def-prstor -->

- **term:** presentation torus (lead candidate; alternatives in the adjudication packet)
- **adjudicated-meaning:** **Grant-ratified 2026-08-24 (R57, verbatim in the docket entry).** the **phase-space tube-phase-family torus**: the surface swept in the phase-space portrait by the (2,3) family under tube-phase precession — the **detuned presentation (`def-dtpres`) of the winding**. A **phase-space object exclusively** (Clifford-torus portrait coordinates, `def-69f472`; the winding is **not** a real-space knot — [`boundary-observables-m-q-j.md`](boundary-observables-m-q-j.md):54, *"its $(2,3)$/trefoil structure is the phase-space (Clifford-torus) winding label, not the real-space body"*). It is **not** the real-space envelope anatomy (`def-anat3s`; [`envelope-anatomy.md`](envelope-anatomy.md) — radial loci on the real-space saturation profile, *"NOT phase-space contours"*), **not** the reactive-amplitude envelope $A$ (DP-1), and **not** the `def-envcar` slow envelope $A(r,t)$ bias texture. This term exists so the word "envelope" is **never** used for the phase-space torus — see the **four-sense** disambiguation block below (KEEP-BOTH: nothing is redefined; the 2026-07-15 ruled primary sense of "envelope" — the wall — keeps the word). **EE-native first:** the filled band a fixed-ratio Lissajous figure paints on a differentially-detuned scope — a display-space object, not a shell around the circuit.
- **axis:** phase-carrier (a phase-space portrait surface); NOT a substrate-noun ontology node (hence no `ontology-grade`)
- **dimension/type:** phase-space surface (dimensionless phasor coordinates)
- **status:** proposed — **0 prior corpus hits at `origin/main` @ `fc154aa6`**, three methods, measured **after** the epic branch merged (so the round-1 "and 0 on the epic branch" method is subsumed); gated on review. **NOT SOLID; the NAME choice itself is a Grant ruling.**
- **canonical-home:** *(none — coinage)*; the object it names: [`research/2026-08-24_frame-invariance-observer-walk_RECORD.md`](../../../research/2026-08-24_frame-invariance-observer-walk_RECORD.md) §2 (**on `origin/main` since #1009**; the #416/#417 two-acts reading, `:49-54`). The channel repo's `SmithTrefoilEnvelope` animation class is the same object under the colliding name — **their court, flagged not policed**. ⚑ **ROUND-2 CORRECTION (m5): the round-1 claim `git grep -niI 'SmithTrefoil' origin/main | wc -l` → **0**, "the name does not exist inside this corpus", is STALE.** At `origin/main` @ `fc154aa6` the same command returns **1**, with provenance: `research/2026-08-24_frame-invariance-observer-walk_RECORD.md:52` — *"The channel's `SmithTrefoilEnvelope` animation (2026-08-24) is these"* — which arrived on main with **#1009**, i.e. **this arc's own walk record naming the channel class**, not an independent corpus use of it. **The substantive point is unchanged and now stated with the right count:** the *class* still lives in the channel repo (their court); the single in-corpus hit is a mention, so nothing inside this corpus needs renaming.
- **clm-cross-links:** *(none yet)*; cross-node: def-dtpres, def-tubalf, def-69f472, def-anat3s, def-envl0p, def-envcar
- **open-ambiguity-flag:** no — a 0-hit coinage minted precisely to RESOLVE the four-sense "envelope" overload recorded in the block below.
- **verification:** VERIFIED **0 prior corpus hits** for `presentation torus` at `origin/main` @ **`fc154aa6`**, **three methods**: `git grep -niIE 'presentation torus' origin/main | wc -l` → **0**; `git grep -nIF 'presentation torus' origin/main | wc -l` → **0**; hyphen-variant `git grep -niIE 'presentation[- ]torus' origin/main | wc -l` → **0**. ⚑ **Round-2 method change, stated:** the round-1 second method was the then-unmerged epic branch; **#1009 has merged**, so the branch content is IN main and the on-main 0 subsumes it — retired as redundant, not dropped. `SmithTrefoil` → **1** in-corpus, corrected above (was mis-stated as 0). **Grade honesty:** the swept-family object is solid algebra; the *presentation* reading of it is **WALK** (record §2, `[WALK, on canon legs]` at `:41`, re-read on main at `fc154aa6` — no drift). **GATED on Grant review — NOT SOLID; the NAME choice is a Grant ruling** (candidates + naming-convention analysis in the adjudication packet).

---

## static existence *(ambiguous — Grant-confirmed 2026-08-24, R57; two objects with OPPOSITE status polarity)*
<!-- id: def-stexst -->

- **term:** static existence (surface form; **two objects, opposite verdicts** — see the ambiguity flag)
- **adjudicated-meaning:** *(★ RE-SCOPED AT AUDIT 2026-08-24 — the draft's "exactly 1 prior hit / no collision" died on re-grep (V3 below, re-pinned to `fc154aa6`: **12 lines / 6 files**; **10 / 5** at the round-1 pin). The carve below is unchanged; what changed is that the term is now recorded as **overloaded**, with a KEEP-BOTH row separating the settled engine-stage2 object from the OPEN (2,3) railed-core object.)* The third question of the three-question carve on the **railed core** (static-existence epic §1): **formation** (dynamic — can the dynamics BUILD it from free radiation? **LEANS-FALSIFIED / closed-negative**, the energize-LOCK route) / **response** (probe — how does the medium REACT to an imposed grading? MEASURED 2026-08-24, the Class-C means-test) / **existence** (static — **does a railed-core configuration EXIST as a self-consistent stationary state, given the topological constraint?** **OPEN**). "Static" = **fixed-point / eigenmode existence, NOT reachability**: impose the (2,3) winding as a time-independent boundary condition, relax with no drive and no pump, ask whether the relaxed state rails $S \to 0$ at the center. **EE-native first:** the carve between a circuit's start-up transient (formation), its small-signal response (probe), and the **existence of its DC operating point** (static existence) — bias-point existence is a different question from reachability by any start-up path. ⚑ **ROUND-2 HEDGE RESTORATION (m9): the formation cell says LEANS-FALSIFIED *and* closed-negative, because canon's own leaf carries both words.** The epic table (`_orchestration/2026-08-24_static-existence-epic.md:19`) writes it as closed-negative; the canonical KB leaf writes it with the hedge attached — [`saturation-rim-inversion.md`](saturation-rim-inversion.md):57, verbatim: *"**DISTINCT** from the **leans-falsified energize-LOCK formation route** (pumped genesis from a free precursor, closed-negative — the engine pumps `H` at `dt→0`; three escape hatches closed)"*. A def-node's adjudicated-meaning is itself a citable object, so **the hedge travels**: dropping it would let a grep-consumer of this node cite a harder verdict than the leaf carries. *(Same leaf, same line, also carries the mandatory challenge-canonical-negative config-grep obligation for any future prereg of this test — cited, not restated.)* **Space declaration (A46):** the question is about a **real-space lattice configuration** under an imposed **phase-space** winding constraint — and the imposition map carrying phase-space interior structure to real space is itself the epic's **P0(b)** open item; a use of this term **must not presume that map exists**.
- **axis:** other — a question-class carve (the configuration is spatial-Brillouin, the constraint phase-carrier); NOT a substrate-noun ontology node (hence no `ontology-grade`)
- **dimension/type:** n/a (question classification)
- **status:** ambiguous — one phrase, **two objects with opposite recorded verdicts** (see flag); the carve itself is epic-ruled but the surface form is not locked. **GATED on Grant review — NOT SOLID.**
- **canonical-home:** [`saturation-rim-inversion.md`](saturation-rim-inversion.md):55 (**on `origin/main`**) — the named test, quoted with markup preserved: *"**The named test (ROUTED-CANDIDATE, NOT fired) — static existence.** Impose the `(2,3)` winding as a **boundary condition**, relax the lattice, and ask whether the relaxed core **rails `S → 0` at the center**. This **is** the standing eigenmode-existence open item"*; the open-item wording it points at is [`program-arc-map.md`](program-arc-map.md):119 (*"*Closed:* K=2G-as-derived. *Opened:* eigenmode-existence as the only remaining open physics"*). The three-question carve: [`_orchestration/2026-08-24_static-existence-epic.md`](../../../_orchestration/2026-08-24_static-existence-epic.md) §1 — the table at `:19-21`, with Grant's GO verbatim at `:3` (**on `origin/main` since #1009**; the `[branch:static-existence-epic @ f29cb576]` tag is RETIRED). ⚑ **Round-2 note on the Response row (`:20`):** it reads *"MEASURED 2026-08-24 — the Class-C means-test: the canonical core locus, no floor (research pair, **PR pending**)"*. That PR is **#1010, now MERGED** — the parenthetical is stale on the canon leaf; **flagged for the auditor lane, not edited here.**
- **clm-cross-links:** clm-satnec (the topological-necessity route the PROVE branch would evidence; **OPEN**, `*pending*` per `def-satrim`), clm-riminv (the interior→rim mapping the carve sits on)
- **open-ambiguity-flag:** YES — **two objects, opposite polarity, KEEP-BOTH:**
  - **(a) the ENGINE-STAGE2 `c_eff(V)` cage object — SETTLED / "established".** `research/2026-06-23_engine-stage2-native-cage_prereg.md`**:25-26**, verbatim across the two lines *(round-2 m6 fix: the quote WRAPS — round 1 cited the start line only)*: *"The static native c_eff(V) eigenmode existence is **ALREADY ESTABLISHED**"*; **:889-890**, likewise wrapped (*"frames the static existence as open. This is **STALE for the STATIC question**"* — `:889` ends at *"the static existence as"*, `:890` carries the rest); :894, on one line (*"to avoid re-litigating the settled static existence"*); :898, on one line (*"(static existence established)"*). *(Range form matches this file's own smith-annulus convention at `:254-255`, "verbatim across the two lines".)* ⚑ **Note the arc's own later history:** that stage-2 bulk-cage route was subsequently falsified as a localization route — the *settled* verdict attaches to the narrow `c_eff(V)` eigenmode-existence question, **not** to electron localization. A grep-consumer of this node will land on that text; the polarity difference must be visible here or the two collide.
  - **(b) THIS node — the (2,3) railed-core object — OPEN.** `manuscript/ave-kb/common/saturation-rim-inversion.md:55` (canonical home above) and `research/2026-08-14_electron-identity-checkpoint1-walk_RECORD.md:39`, verbatim: *"`clm-satnec` (impose winding, relax, does the core rail?) remains OPEN — static ex…"* (the term used in exactly this sense — supportive prior use, and uncounted by the draft).
  - **(c) two further prior uses, neither in conflict, listed for the record:** `research/2026-06-30_electron-portmap-derivation_result.md:516` (*"NOT resolved in this static existence/stability analysis"* — a scope disclaimer, same sense as (b)); `research/2026-07-17_regime-iv-dissipation-audit_items.json:620,632,1304` (*"a STATIC existence inequality"* — the compactness-limit bound, a **third** object: a kinematic inequality, not an eigenmode question).
  - **Rule:** never write bare "static existence". Write **"the stage-2 `c_eff(V)` static existence"** (a, settled), **"the (2,3) railed-core static existence"** (b, open), or **"the compactness static-existence inequality"** (c).
  - **Guard already in the draft, kept:** "static" here must not be read against the #416 *"charge is the STATIC imposed Link"* sense as if they were different words — the epic §1 cites that ruling as agreeing vocabulary (*"stable because it is static"*); same sense, listed for the record.
  - conflicting sites: settled stage-2 object `2026-06-23_engine-stage2-native-cage_prereg.md:25-26,889-890,894,898`; the OPEN railed-core object `saturation-rim-inversion.md:55`, `2026-08-14_electron-identity-checkpoint1-walk_RECORD.md:39` and `_orchestration/2026-08-24_static-existence-epic.md:1,3` (title + Grant's GO; the three-question carve table is `:19-21`, with the OPEN row at `:21`); scope-disclaimer use `2026-06-30_electron-portmap-derivation_result.md:516`; compactness inequality `2026-07-17_regime-iv-dissipation-audit_items.json:620`.
- **verification:** **★ THE DRAFT'S "VERIFIED: exactly 1 prior main-corpus hit" IS FALSE AND IS WITHDRAWN.** Re-measured at `origin/main` @ **`fc154aa6`** (round-2 re-pin), two methods: `git grep -niI 'static existence' origin/main | wc -l` → **12 lines**; `git grep -liI 'static existence' origin/main | wc -l` → **6 files**; match-count `git grep -oiI 'static existence' origin/main | wc -l` → **13**; per-file `git grep -ciI 'static existence' origin/main` → `2026-08-24_static-existence-epic.md:2`, `saturation-rim-inversion.md:1`, `engine-stage2-native-cage_prereg.md:4`, `electron-portmap-derivation_result.md:1`, `regime-iv-dissipation-audit_items.json:3`, `checkpoint1-walk_RECORD.md:1` = **12** ✓. *(Round-1 at `37926892`: 10 / 5 / 11. The +2 lines / +1 file is the epic itself arriving with #1009 — `:1` title, `:3` Grant's GO — i.e. sense (b), this package's own object; **the collision inventory is unchanged**.)* Every prior-use line above was **read**, not just counted, and the two wrapped prereg quotes are now cited in range form (`:25-26`, `:889-890`) rather than at their start line. Canonical-home quote re-read **verbatim with markup** at `saturation-rim-inversion.md:55`, and the leans-falsified hedge at `:57`; the carve table re-read on main at the epic `:19-21`. ⚑ **Flag-don't-fix — a corpus off-by-one surfaced en route, NOT repaired here:** `saturation-rim-inversion.md:55` cites the open-item wording as `program-arc-map.md:118`, but at `origin/main` line **:118** is *"*Verdict:* **GR-imported** — both gates pass"* and the quoted *"Opened: eigenmode-existence as the only remaining open physics"* is at **:119**. This entry cites **:119** (the correct line) and surfaces the discrepancy for the auditor lane; it does not edit the canon leaf. **Grade honesty:** the carve is an orchestration-epic definitional ruling (Grant's GO recorded verbatim in the epic header); the physics it names is **OPEN** (both branches of the epic's §2 open-goal framing stay live; this entry prefers neither). **GATED on Grant review — NOT SOLID.**

---

## envelope — ★ FOUR-sense disambiguation block *(proposed AMENDMENT to `def-envl0p`; KEEP-BOTH — extends the ambiguity record, redefines NOTHING)*
<!-- amendment: extends def-envl0p's open-ambiguity record. NO interior edit — land this block at end-of-file and append ONE sentence to def-envl0p per §T6-AMENDMENT. Do NOT touch Senses A/B or the 2026-07-15 word-level ruling. -->

**★ REPAIRED AT AUDIT: the row was THREE senses and MISSED a fourth SOLID def-node.**
The draft inventory omitted **`def-envcar`** (`## envelope vs carrier (the two-level
decomposition of the A1 breather)`, `vocabulary-register.md:1051-1062`) — the slow
envelope $A(r,t)$ of the A1 breather, an explicitly **spatial** bias texture,
**SOLID for the decomposition**. It fits none of the three drafted cells: it is not
the wall (sense 1), and the drafted sense-2 cell says *"not a spatial region"* while
`def-envcar`'s envelope is exactly that. **Fourth-sense hunt: POSITIVE.** The
inventory is now four; the object the draft numbered "sense 3" is **sense 4** here —
any prior reference to "sense 3" in lane docs means the phase-space torus and must
be re-pointed.

The token **"envelope"** carries **FOUR def-noded / canon-rowed senses crossing the
A46 fence**. The 2026-07-15 Grant ruling — *"envelope = the wall" as the primary
sense is **CONFIRMED (Grant in-chat 2026-07-15)*** (register GATE comment directly
above the `## envelope` / `<!-- id: def-envl0p -->` heading; currently `:415`) —
governs the word; the three non-wall senses must travel under their own names.

| # | sense | space (A46) | owner / receipts (re-verified at `origin/main` @ **`fc154aa6`**) | rule |
|---|---|---|---|---|
| 1 | **real-space three-surface anatomy / the wall** | **spatial-Brillouin** — real-space radial loci | `def-anat3s` + `def-envl0p` Sense A; [`envelope-anatomy.md`](envelope-anatomy.md):13, verbatim *(round-2 m4 fix: the round-1 quote opened mid-phrase with a dangling `**` and silently dropped "radial loci on the" — this is the same un-ellipsised-truncation class the round-1 repair fixed at A1-6)*: *"the three surfaces below are **radial loci on the real-space saturation profile** $S(A(r))$, NOT phase-space contours (A46 phase-space-vs-real-space discipline: these are `spatial-Brillouin`-axis lengths)"* (`clm-3surfa`); $r_{env}$ = `def-088f0d` (proposed, gated); Grant word-level ruling 2026-07-15 (GATE comment above `def-envl0p`) | **KEEPS the bare word** "envelope" |
| 2 | **reactive-amplitude envelope $A$ (DP-1)** | **phase-carrier** — an amplitude/phase condition, not a spatial region | DP-1, Grant-ratified 2026-07-02: [`substrate-perspective-electron.md`](../vol2/particle-physics/ch01-topological-matter/substrate-perspective-electron.md):62, verbatim: *"reactive-amplitude **envelope** (the cycle time-average / conserved reactive energy of the $(V_{\text{inc}},\Phi_{\text{link}})$-type tank), NOT an instantaneous phase snapshot"*; = `def-envl0p` Sense B family, [`substrate-hysteresis-index.md`](substrate-hysteresis-index.md):**24** *(re-pinned — see the stale-cite flag below)* | say "**reactive-amplitude envelope**" or "the DP-1 envelope $A$" — never bare "envelope" |
| 3 | ★ **the A1 breather's slow envelope $A(r,t)$ — a real-space BIAS TEXTURE** *(the missed sense)* | **spatial** (the register's own axis line calls it *"the slow envelope $A(r,t)$ bias texture"*, level-of-description split vs the fast carrier) | **`def-envcar`**, `vocabulary-register.md:1051-1062`; `:1055` verbatim: *"a slow **ENVELOPE** $A(r,t)$ = the energy-density / operating-point **bias pattern** (what gravitates; what translates when the star orbits)"*; `:1058` status: *"**SOLID for the DECOMPOSITION only**"* (the coupling verdict is **not** hardened there) | say "**the `def-envcar` slow envelope**" / "the A1 breather's envelope" — and respect the **24-decade catch** at `:1055`: reading this envelope's slow energy moment as a carrier-band source conflates the two levels |
| 4 | **phase-space tube-phase-family torus** *(was drafted as "sense 3")* | **phase-carrier** — Clifford-torus portrait coordinates (`def-69f472`) | **the un-owned squatter** — the 2026-08-24 walk record §2 (*"**The torus/envelope appears only under differential detuning**"*, [`RECORD.md`](../../../research/2026-08-24_frame-invariance-observer-walk_RECORD.md):44-45, **on `origin/main` since #1009**) + the channel repo's `SmithTrefoilEnvelope` class name (2026-08-24; **1 in-corpus hit** — `RECORD.md:52`, this arc's own mention of the channel class; the class itself is still their court) | **LOSES the word entirely** → the proposed **presentation torus** (`def-prstor`) |

**Why this is a genuine A46 collision, not a style nit.** Sense 4 vs sense 1 is a
phase-space torus read against a real-space shell — the exact failure the
coordinate-discipline fence exists to catch, in the word the 2026-07-15 ruling
already assigned to the wall. Sense 4 vs sense 2 conflates a *swept family surface*
with a *cycle time-average amplitude*. Sense 3 vs sense 1 is the subtlest: **both
are real-space**, so the A46 fence does not separate them — only the level-of-
description does (`def-envcar`'s carrier/envelope split vs `def-anat3s`'s radial
loci on the saturation profile). The register already carries a standing warning of
this kind at `def-ncsatw` (`vocabulary-register.md:1090`): *"`def-envl0p` (the struck
soliton-size-envelope node — a distinct object; do not conflate the size-envelope
with this bound/free division)"*.

**KEEP-BOTH discipline:** senses 1, 2 and 3 are **untouched** and their receipts
stand; only the un-owned sense 4 gets a new name. Nothing is redefined in place.

**⚑ STALE-CITE FLAG (flag-don't-fix — for the auditor lane, NOT repaired here).**
`def-envl0p`'s own `canonical-home` field cites Sense B as
`substrate-hysteresis-index.md:24,136`. ★ **ROUND-2 WIDENING (F3): the stale
`:136` is in THREE fields, not one** — `vocabulary-register.md:425`
(`canonical-home`, as `:24,136`), `:427` (`open-ambiguity-flag`, as `:24,27,136`)
and `:428` (`verification`, **twice**, as `:24,27,136`). The round-1 flag named
only the first, which under-reports the drift surface for whoever repairs it.
At `origin/main` @ `fc154aa6` **`:24` verifies**
(*"Reversible sub-yield envelope (Level 1, memoryless)"*) but **`:136` no longer
carries any envelope content** — it now holds the `#744 (merged) … THREE-WAY
DEGENERATE` note. Command: `git grep -niI 'envelope' origin/main -- '*substrate-hysteresis-index.md'`
→ envelope lines are **:18, :24, :27, :41, :92, :104, :123, :132, :149** — no `:136`.
This row therefore cites **`:24` only**. Per the vacated-cite pattern the `:136`
half of `def-envl0p`'s cite should be re-pinned or dropped by whoever owns that
node; this package **does not silently edit another node's field**.

**Scope honesty — what this block does NOT claim.** It is a disambiguation of the
**def-noded and canon-rowed** senses, not a classification of the corpus. `git grep
-niIw 'envelope' origin/main -- manuscript/ | wc -l` → **390 lines / 109 files**
at `fc154aa6` (unchanged across both merges; repo-wide **2214 / 536**, up from
2193 / 528 at `37926892` — the delta is all `research/` + `_orchestration/`). Two further live usage families were read and are
**deliberately left unclassified**, listed so nobody mistakes the four-row table for
completeness: (i) the **paraxial/Schrödinger Ψ-envelope** family — `clm-7zuwtm`
*"Schrödinger Equation from Paraxial Envelope (Mechanism, Not Independent
Derivation)"*, [`schrodinger-from-circuit.md`](../vol1/dynamics/ch3-quantum-signal-dynamics/schrodinger-from-circuit.md):20,28;
(ii) the **Peierls–Nabarro co-moving self-matched envelope** —
[`peierls-nabarro-paradox.md`](../vol2/appendices/app-b-paradoxes/peierls-nabarro-paradox.md):12 (*"This paradox assumes the vacuum substrate is a cold, rigid, periodic crystal"*)
(*"the electron is a co-moving self-matched envelope"*, `vol2/appendices/app-b-paradoxes/index.md:19`),
cited from `substrate-hysteresis-index.md:92`. Both plausibly belong to the sense-3
(`def-envcar`) family; **neither is adjudicated here.**

*(Status of this block: proposed — it lands only with `def-prstor`. If Grant picks a
different T6 noun, substitute it in the sense-4 cell.)*

---

## linear (hop $L,C$ vs strain) *(ambiguous — DISAMBIGUATION VIEW, 2026-08-28; three non-interchangeable senses; not a coinage)*
<!-- id: def-ln3str -->

- **term:** linear (hop $L$, $C$ vs strain) — surface form; three registers. Write the sense, never bare "linear $L,C$."
- **adjudicated-meaning:** **DISAMBIGUATION VIEW, RESTATEMENT-grade.** The question *"under what strain do hop $L$ and $C$ scale linearly?"* has **three non-interchangeable answers already in canon**; this node separates them and adds no physics. **(K) Kernel / Ax4.** $S(r)=\sqrt{1-r^2}$ is even; first correction $O(r^2)$. Regime I ($r<\sqrt{2\alpha}$) drops that correction, so the SYM table freezes $\varepsilon_{\mathrm{eff}}=\varepsilon_0$, $\mu_{\mathrm{eff}}=\mu_0$, $C_{\mathrm{eff}}=C_0$. Solar-system gravity is deep Regime I. Hop $L,C$ from Ax4 are **constant to working precision**, not linear in $\varepsilon_{11}$. **(P) Photoelastic / Op19.** $n=1+\nu_{\mathrm{vac}}\varepsilon_{11}$ is linear in strain by construction. Under SYM, hop $L$ and $C$ co-scale with $n$, so the leading gravitational index is $O(\varepsilon_{11})$. Same weak-field band as (K); **different expansion**. Coefficient $\nu_{\mathrm{vac}}=2/7$ is GR-imported. **(Z) SYM co-scale.** $Z=\sqrt{L/C}$ is pinned for all gravity-class loading, so $L\propto C$ at every strain until the loading class leaves SYM. That is linear-in-each-other, not linear-in-strain. **Rule:** never fuse (K) with (P). Photoelasticity $\neq$ the kernel Taylor series.
- **axis:** other — a surface-form disambiguation spanning the Ax4 kernel (amp), Op19 kinematics (strain→index), and Ax3 impedance match; NOT a substrate-noun ontology node (hence no `ontology-grade`)
- **dimension/type:** n/a (a classification of three expansions / constraints). Instance (K) is dimensionless $r=A/A_c$; (P) is dimensionless $\varepsilon_{11}$ and $n$; (Z) is the ratio $L/C$ (impedance-squared)
- **status:** ambiguous — three canon senses, no single locked "linear"; this node adjudicates the *overload*, not a new coupling
- **canonical-home:** [`hop-lc-constitutive-grading.md`](../vol3/gravity/ch03-macroscopic-relativity/hop-lc-constitutive-grading.md) §3 (the three-sense assembly) + [`four-regimes.md`](../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md):110-114 (even Taylor) + [`operators.md`](operators.md):59 (Op19) + [`achromatic-impedance-matching.md`](../vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md):20-28 (SYM co-scale)
- **clm-cross-links:** clm-b2anl4 (Regime I kernel freeze), clm-rd9cjm (Op19 $n=1+\nu\varepsilon_{11}$), clm-07kd5v (SYM $Z=Z_0$), clm-3zz0f6 (SYM $\alpha$ invariance — same co-scale)
- **open-ambiguity-flag:** YES — **three registers, KEEP-ALL. This node redefines nothing; it separates:**
  - **(K) Kernel-even / Regime I freeze.** `four-regimes.md:26` names Regime I "Linear"; `four-regimes.md:110-114` is the even Taylor; `regime-equation-sets.md:19-25` freezes $C_{\mathrm{eff}}=C_0$; `nonlinear-vacuum-capacitance.md:33-34` is the same even expansion on the A1 varactor; `domain-catalog.md:50` places solar $\varepsilon_{11}$ in Regime I.
  - **(P) Op19 / photoelastic linear-in-$\varepsilon_{11}$.** `operators.md:59`; `transverse-refractive-index.md:23`; `achromatic-impedance-matching.md:20-28` ($\mu'=n\mu_0$, $\varepsilon'=n\varepsilon_0$). Sharpened: `2026-07-31_anisotropy-observable_scoping.md:893` (*"photoelasticity is linear in strain while the kernel's index shift is quadratic in amplitude — the two are not the same expansion"*); `2026-08-11_gravity-linearity-audit_result.md:24` (*"The Ax4 kernel appears **nowhere** in that chain"*).
  - **(Z) SYM $L\propto C$.** `achromatic-impedance-matching.md:20-28`; INVARIANT-S2 SYM row `translation-circuit.md:117`. Holds at every gravity-class strain, not only small $r$.
  - conflicting sites: `four-regimes.md:26,110-114`; `regime-equation-sets.md:19-25`; `nonlinear-vacuum-capacitance.md:33-34`; `domain-catalog.md:50`; `operators.md:59`; `transverse-refractive-index.md:23`; `achromatic-impedance-matching.md:20-28`; `2026-07-31_anisotropy-observable_scoping.md:893`; `2026-08-11_gravity-linearity-audit_result.md:24`; `translation-circuit.md:117`.
- **verification:** DISAMBIGUATION VIEW, not a coinage. Coinage-grep of the node title `linear (hop L,C vs strain)` / `def-ln3str` / `hop-lc-constitutive` at write time: **0 prior hits**. Bare "linear" is the overload this node exists to split — not grepped as a coinage. Receipts re-read at write: `four-regimes.md:110-114` even Taylor **verbatim**; `regime-equation-sets.md:19` $C_{\mathrm{eff}}=C_0$ in column I; `operators.md:59` Op19 **verbatim**; `achromatic-impedance-matching.md:20-28` $\mu'=n\mu_0$, $\varepsilon'=n\varepsilon_0$; `nonlinear-vacuum-capacitance.md:33-34` quadratic-leading; `domain-catalog.md:50` solar Regime I; anisotropy `:893` and gravity-linearity-audit `:24` as quoted in the flag. `clm-b2anl4`, `clm-rd9cjm`, `clm-07kd5v`, `clm-3zz0f6` each resolve. **Grade honesty:** WALK assembly of canon legs (Grant asked the question 2026-08-28; PR #1033). Does **not** derive the Op19 coefficient, does **not** plant $(2,1,\tfrac12)$, does **not** slide vertices.

---
