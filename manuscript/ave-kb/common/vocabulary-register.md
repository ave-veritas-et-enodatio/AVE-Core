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

## envelope
<!-- id: def-envl0p -->

- **term:** envelope
- **adjudicated-meaning:** *(TWO genuine registers under one token — real-space shell vs phasor-gain condition; the A46 phase-space-vs-real-space clarity risk).* **Sense A — real-space SHELL** [spatial-Brillouin]: the physical 3D saturation-boundary shell of a soliton, size set by $\ell_{node}$ (the "boundary envelope" / "body envelope"; = the r_env length, def-088f0d). **Sense B — phasor-GAIN condition** [phase-carrier]: an amplitude/phase condition, NOT a spatial region — the modulation envelope of a `carrier × envelope` decomposition, and the reversible sub-yield $\sqrt{1-A^2}$ saturation-gain envelope. A gain/modulation envelope (Sense B) is a locus in amplitude/phase space; do NOT read it as a real-space shell (Sense A).
- **axis:** other (spans spatial-Brillouin [A] and phase-carrier [B])
- **dimension/type:** length (L) [Sense A] vs dimensionless amplitude-gain / envelope function [Sense B]
- **status:** ambiguous
- **canonical-home:** Sense A — [`trampoline-framework.md`](trampoline-framework.md):685 ("boundary envelope … size set by $\ell_{node}$") + r_env (def-088f0d); Sense B — [`substrate-hysteresis-index.md`](substrate-hysteresis-index.md):24,136 (reversible sub-yield $\sqrt{1-A^2}$ envelope).
- **clm-cross-links:** *(none verified-specific yet; cross-node: def-088f0d (r_env, Sense-A length), def-a9eef5 (carrier — the "carrier × envelope" partner), def-69f472 (phase-space))*
- **open-ambiguity-flag:** YES — the two registers above. **Conflicting sites (conflation-map):** *Sense A (real-space shell)* — `trampoline-framework.md:685` (boundary envelope, $\ell_{node}$-set); `manuscript/vol_2_quantum/chapters/02_baryon_sector.tex:40` ("multi-node body envelope"); `src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py:77` ("real-space envelope"). *Sense B (phasor-gain)* — `vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md:56,59` ("Gaussian envelope × sinusoidal carrier"); `substrate-hysteresis-index.md:24,27,136` ("reversible reactive envelope", "the smooth $\sqrt{1-A^2}$ envelope"). The board B4 tension (`trampoline:685` "envelope size set by $\ell_{node}$" vs the nucleus 1 fm = 386× below $\ell_{node}$) is a **Sense-A** reading; it does not touch Sense B.
- **verification:** VERIFIED 2026-07-14 — both senses live in the corpus at the cited sites (two-method grep). Register-hygiene def-node; adds/retires no `clm-`. Cross-links to the six-scale boundary-register tag (`boundary-observables-m-q-j.md` §"Same mechanism at all scales", where the electron "boundary envelope" is the amplitude-level-set shell).

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
  - **CEILING REAFFIRMED by a computed null (2026-07-02, KEEP-BOTH note).** The Cleave-01 displacement coupling $Q = \xi_{topo}\,x$ — the dictionary's displacement row read as a *mechanism* — was tested for a derived-pump instance: both the 2-band and faithful N-band srs occupied-manifold Chern over the $(k_z,\theta)$ registry torus return $C = 0$ (both readings, both enantiomorphs; `clm-clvchn`, `research/2026-07-02_cleave-registry-pump-chern-nband_result.md`). **No derived-mechanism instance emerged — the 'identity-by-translation, NOT a derivation' ceiling holds** (a nonzero $C$ would have been the first derived-mechanism instance and an upgrade path; the null reaffirms the ceiling).
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

## quiescent point *(proposed)*
<!-- id: def-q1escn -->

- **term:** quiescent point / Q-point
- **adjudicated-meaning:** *(PROPOSED, gated)* the EE name for the substrate cell's **saturation-state $A$** read as a **DC operating point** — "the dynamical state of the LC tank, analogous to DC bias on a semiconductor varactor" ([`CLAUDE.md`](../CLAUDE.md):75). The electron's Q-point is **self-set** (Axiom-4 self-saturation *is* the bias mechanism, no external bias network) and **self-stable** (the $R\cdot r=\tfrac14$ equilibrium; rest-mass = the DC energy stored at the Q-point). The VCA / graded-impedance trio is the **small-signal** response linearized *around* this Q-point. It is the previously-unnamed DC-bias step of the EE workflow (DC-bias → linearize → AC), NOT a new object.
- **axis:** other (operating-point state along the Axiom-4 kernel; distinct from the kinematic DOFs)
- **dimension/type:** dimensionless (the per-port normalized bias $A=|V|/V_{yield}$); per-port biases sit on the $V_{yield}/V_{snap}$ ladder [voltage scales]
- **status:** proposed
- **canonical-home:** [`node-up-small-large-signal.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md):§4b (the bias-then-small-signal re-expression); the electron load-line at [`cvr-dc-operating-point.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-dc-operating-point.md):43-45; the "DC bias on a varactor" operating-point state at [`CLAUDE.md`](../CLAUDE.md):75
- **clm-cross-links:** clm-vca7r1 (node-up small/large-signal), clm-fd1e7a (the electron R/X/Q/L/C bundle = the small-signal read), clm-kezk9z (the $\Gamma=-1$ cage at the saturated bias)
- **canon-noun map:** "quiescent point / Q-point / DC bias" ↔ the **saturation-state $A$** (self-set, Axiom-4). Non-canon EE name; maps to the canon operating-point-state noun, no noun-swap. CONSISTENCY-class re-expression — coins no new physics.
- **open-ambiguity-flag:** no (fresh coinage; VERIFIED 0 prior KB hits for "quiescent" as a substrate-operating-point term — the single corpus hit `vol5/.../creatine-neural-capacitor.md` is an unrelated biological usage).
- **verification:** VERIFIED the varactor-bias operating-point reading verbatim at [`CLAUDE.md`](../CLAUDE.md):75 and the electron load-line ($V_{snap}\approx511$ kV, $V_{yield}=\sqrt\alpha V_{snap}\approx43.65$ kV) at `cvr-dc-operating-point.md`:43-45. The $R\cdot r=\tfrac14$-sets-the-Q-point **α-free** (the α-flip) is **PENDING/open**, not asserted. **GATED on auditor + Grant review — NOT adopted, NOT SOLID.** *(α-flip STATUS, FORK-A 2026-06-24 — PENDING STANDS: the self-biased **pressure-equilibrium** route returns closed-NEGATIVE → ECHO — fixes a scale not the product $R\cdot r$, α re-enters via the √α ladder + $Z_0\propto\alpha$ area-bridge, relabel of the conservative $H_{couple}$ slosh; [`research/2026-06-24_forka-alpha-flip.md`](../../../research/2026-06-24_forka-alpha-flip.md). SCOPE = that named route ONLY, **NOT** route-exhaustion; the α-flip stays PENDING.)*

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
- **verification:** VERIFIED the 6-DOF + $A$-state content at [`CLAUDE.md`](../CLAUDE.md):73,:75 and $A1\perp T2$ at `master-equation.md`:20. The MASS/CHARGE/$\varepsilon$/$\mu$ role attribution re-expresses the three-channel ROLES (`resonant-lc-solitons.md`:118-125, themselves Grant-gated where the $V_{yield}$ fork applies). **DOMAIN-HYGIENE re-materialization (2026-06-24):** the prior "CHARGE = the Cosserat micro-rotation port (the $\mu$/inductive sector) → $Z_{\mathrm{shear}}$" string direct-wired the EM $\mu_{eff}$ onto the mechanical $Z_{\mathrm{shear}}$ — FORBIDDEN by `resonant-lc-solitons.md`:120,:124,:129 (CHARGE = mechanical static-reactive boundary, $\mu$ = EM param of $Z_{\mathrm{EM}}$, bridged by the def-tk1xfm transducer, not a direct wire). Separated above. **GATED on auditor + Grant review — NOT adopted, NOT SOLID.**

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
  - (d) the isotropic-solid **longitudinal P-wave** $c_L = \sqrt{(K+\tfrac{4}{3}G)/\rho} = \sqrt{10/3}\,c \approx 1.83c$ at $K=2G$ ($\nu=2/7$). This is DISTINCT from the $\sqrt{2}\,c$ bulk-modulus dilatational speed (which drops the $4G/3$ shear term) — the 2026-06-08 c_L reconciliation (Rule 12). Home: `vol1/dynamics/index.md:28`; `vol1/dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md:38`.
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
  - (a) the **bulk-volumetric / V-sector scalar** longitudinal grade — the Heaviside-excised compression scalar, the **A1 dilatation-mass "3"** (`master-equation.md:18,20`). This is the real, physical, Gauss-undeleted grade. **Physical realization:** the **K4 breathing mode** (symmetric radial dilation of all 4 nodes, `vol6/appendix/geometric-inevitability/lambda-higgs-derivation.md`), onto which the **SM Higgs** is a FORM-identification ($m_H = v/\sqrt{N_{K4}} = v/2$) — **NOT** a VALUE-derivation: the route imports $v$ and asserts $N_{K4}=4$, and the quaternion-scalar↔Higgs chord is closed-negative / G3-FAIL (see `def-9b3d05` + `research/2026-06-06_biquaternion-node-algebra-result.md`). [scalar V grade]
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
- **verification:** VERIFIED the three channel impedances + $\Gamma$ values verbatim at `three-channel-impedances.md:20-22` ($Z_{EM}\equiv Z_0$, $\Gamma_{EM}=0$; $Z_{shear}=\rho c_{shear}$, $\Gamma_{shear}\to-1$; $Z_{bulk}=\sqrt2\,\rho c_0$ at $K=2G$, $\Gamma_{bulk}\to-1$). VERIFIED the two coincident-but-distinct $\Gamma=-1$ walls at `resonant-lc-solitons.md:89-94` + `master-equation.md:20`. PROPOSED — consistency re-expression, not new physics.

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

## T₂ (photon-family disambiguation)
<!-- id: def-t2ph01 -->

- **term:** T₂ (the tetrahedral-group triplet label — TWO physically-distinct objects share it, separated by the massless-vs-gapped mass status)
- **adjudicated-meaning:** the **default canonical "T₂ = the photon" sense is the massless transverse-TRANSLATIONAL mode pair (u-family)** — the two massless transverse-shear branches at $c = \sqrt{G/\rho}$ whose eigenvectors are u-dominated (translational). The glyph T₂ is overloaded in the corpus by a *second* object — the **Cosserat microrotational (ω) family** (gapped, mechanical, the static (2,3) winding's home) — historically ALSO called "the photon." Per the G2 ruling (Grant 2026-07-03) the photon is sense (1); the node ω is sense (2), NOT the photon. This node is the canonical disambiguation + mis-use watch-list.
- **axis:** spatial-Brillouin (band-family label on the K4 two-sublattice dispersion)
- **dimension/type:** DOF-family label (n/a — classifies which Cosserat sector a mode lives in); the modes themselves are frequency ($T^{-1}$)
- **status:** SOLID (for the locked "photon = transverse-translational u-family" sense; the disambiguation is Grant-adjudicated 2026-07-03, so the canonical sense seeds SOLID — status and open-ambiguity are orthogonal per the `node`/`ξ` precedent)
- **canonical-home:** sense (1) the photon = transverse-translational u-family: `research/2026-07-03_g2-photon-relabel_note.md` (ruling) + `photon-identification.md:11` (with the G2 relabel note); the decisive eigenvector read at `src/scripts/vol_1_foundations/g2_photon_eigvec_composition.py` / `_output/g2_photon_eigvec_composition.json`. sense (2) the gapped mechanical ω: `cosserat-mass-gap.md` §4 ($m^2 = 4G_c/I_\omega$); `clm-wcoul2` (Yukawa-screened winding pair).
- **clm-cross-links:** clm-g0mkne (Cosserat rotational mass mechanism — carries the G2-RESOLVED photon-family note), clm-j550uh + clm-9kd2t3 (k4-port irrep decomposition), clm-wcoul2 (gapped-ω winding-pair Coulomb), clm-kmliqx (c_R = √2 rotational curvature speed)
- **open-ambiguity-flag:** YES — the surface label T₂ names TWO distinct objects:
  - (1) **the transverse-TRANSLATIONAL mode pair (THE PHOTON's family, MASSLESS)** — the two massless transverse-shear branches, u-dominated (ω-fraction → 0 at k→0: Step-1 rider reads $2.5\times10^{-7}$; u-fraction $= 1.000000$), propagating at $c = \sqrt{G/\rho}$. Its magnetic content = the **EM-inductive circulation of the u-wave** (bond-level curl $\nabla\times u$, the Axiom-1 μ₀-family B), NOT a node micro-rotation.
  - (2) **the Cosserat MICROROTATIONAL (ω) family (GAPPED, mechanical, the winding's home)** — ω-dominated (ω-fraction $= 1.000000$), gapped at $m^2 = 4G_c/I_\omega$ (the mechanical Cosserat mass; Yukawa-screened, short-range, `clm-wcoul2`); the home of the *static* (2,3) winding topology. This is NOT the photon.
  - **The watch-list qualifier rule:** **never write bare "T₂" or "T₂ microrotational ω" for the photon** — the photon is the transverse-*translational* u-family. When a leaf says "T₂ … the photon" it means sense (1) (translational-u); when it says "T₂ … carries the mass-gap / the winding" it means sense (2) (gapped microrotational ω). The two are separated by the massless-vs-gapped mass status, which is the load-bearing distinction (not the free-vs-locked one).
  - **CONFLICTING SITES (verified 2026-07-03, now carrying G2 KEEP-BOTH relabel notes):** `photon-identification.md:11` ("Cosserat shear wave with $u=0$, $\omega\neq0$" — sense-2 label on the photon, CORRECTED to sense 1); `k4-port-irrep-decomposition.md:26` ("Microrotational ω … THIS IS THE PHOTON" — sense-2 label, CORRECTED); `cosserat-mass-gap.md:145` + `vol1/claim-quality.md:1131` (had the RIGHT family — sense 1 translational — with the gapped ω correctly as sense 2; G2-RESOLVED notes added).
- **verification:** VERIFIED — the massless-branch u-dominance ($\omega$-fraction $2.5\times10^{-7}$, u-fraction $1.000000$) and gapped-branch ω-dominance ($1.000000$) computed on the genuine two-sublattice A→B bond operator (`g2_photon_eigvec_composition.json`, k=1e-3, 4 directions); the operator is the same that recovers the gap $m^2 = 4$ bit-exact (V3, `research/2026-06-23_cosserat-band-structure-two-sublattice_prereg-result.md`). Ruling Grant 2026-07-03 (`research/2026-07-03_g2-photon-relabel_note.md`). Status SOLID for the locked "photon = transverse-translational u" sense; open-ambiguity records the T₂ overload (orthogonal per the SCHEMA Definition-record rule). NOTE (flag-don't-fix): the original GAP-G2 orchestration diagnosis (`_orchestration/2026-06-07_electron-synthesis-epic.md:319`) pinned "photon = microrotational ω" as canonical — the eigenvector read contradicts it, resolved AGAINST that side per the ruling.

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

