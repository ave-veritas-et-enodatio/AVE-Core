# Vol 2 Taxonomy Design — The Subatomic Scale

**Source survey:** `.claude/phase0-surveys/vol2_survey.md`
**KB output target:** `manuscript/ave-kb/vol2/`
**Design date:** 2026-04-02

---

## 1. Invariants

Content from Vol 2 that is genuinely cross-cutting and belongs in `manuscript/ave-kb/CLAUDE.md` rather than in volume-specific KB pages. Each entry must be in use across at least two distinct volume trees.

```
INVARIANT: macro-Lvac — \Lvac expands to L_{node} (lattice inductance) (source: vol2 §3 notation table)
INVARIANT: macro-Cvac — \Cvac expands to C_{node} (lattice capacitance) (source: vol2 §3 notation table)
INVARIANT: macro-Zvac — \Zvac expands to Z_0 (characteristic impedance) (source: vol2 §3 notation table)
INVARIANT: macro-Wcut — \Wcut expands to \omega_{sat} (saturation / cut-off frequency) (source: vol2 §3 notation table)
INVARIANT: macro-lp — \lp expands to l_{node} (lattice pitch, all vols except Vol 1 which uses \ell_{node}) (source: vol2 §3 notation table)
INVARIANT: macro-vacuum — \vacuum expands to M_A (aether mass matrix / vacuum); chapters write $\mathcal{M}_A$ directly, NOT via this macro (source: vol2 §3 notation table; confirmed cross-volume)
INVARIANT: macro-slew — \slew expands to c (speed of light) (source: vol2 §3 notation table)
INVARIANT: macro-planck — \planck expands to \hbar (reduced Planck constant) (source: vol2 §3 notation table)
INVARIANT: macro-permeability — \permeability expands to \mu_0 (source: vol2 §3 notation table)
INVARIANT: macro-permittivity — \permittivity expands to \epsilon_0 (source: vol2 §3 notation table)
INVARIANT: macro-impedance — \impedance expands to Z_0 (impedance of free space) (source: vol2 §3 notation table)
INVARIANT: resultbox-no-label — resultbox{} environment does not support \label; key results are identified by title string + source line range, not by LaTeX label (source: vol2 anomaly A10; applies to all volumes)
INVARIANT: script-ell-exception — Vol 1 writes \ell_{node} (script ell); all other volumes write l_{node} via \lp macro (source: cross-volume confirmed)
INVARIANT: citestart-citeend — \citestart{} and \citeend{} are no-op placeholders; distillers ignore them (source: vol2 §3 notation table)
INVARIANT: tcolorbox-environments — shared custom environments: resultbox, axiombox, simbox, examplebox, summarybox, exercisebox, circuitbox, codebox, objectivebox (source: confirmed all 8 volumes)
INVARIANT: chapter-per-volume-objectivebox — each chapter opens with objectivebox and closes with summarybox + exercisebox (confirmed vol2 and all surveyed volumes that include body chapters)
```

**CLAUDE.md boundary note:** Vol 2 specific content — knot topology particle assignments, PMNS mixing angles, orbital screening rules, etc. — does NOT belong in CLAUDE.md. Only the 16 invariants above pass the binary filter: "does this need qualification when applied to any single volume?"

---

## 2. Domain Groupings and Rationale

Vol 2 spans 12 chapters and appendices. The chapters divide cleanly into five subject clusters:

| Domain slug | Chapters | Rationale |
|---|---|---|
| `particle-physics` | Ch 1–6 | Torus knot particle taxonomy, baryons, neutrinos, spin, electroweak, Higgs — all knot-topology-based particle content. These six chapters form a contiguous derivation chain with strong internal cross-reference density. |
| `quantum-orbitals` | Ch 7 alone | Anomalously large (~3600 lines, 10× average). Warrants its own domain. Orbital mechanics, analog filter atom model, and wavefunction reinterpretation form a coherent sub-theory with different mathematical machinery from chs 1–6. Also provides `ch:quantum_orbitals` — the label referenced by Vol 5. |
| `foundations-validation` | Ch 8–9 | Planck-scale / string-theory reinterpretation (ch.8) and computational proof / anomaly catalog (ch.9). Short chapters (~103 and ~243 lines) that serve as theory grounding and empirical validation — naturally grouped. |
| `open-problems` | Ch 10–12 | Open problems (ch.10), SM overdrive (ch.11), and millennium prizes (ch.12). All three chapters address the reach of the AVE framework beyond canonical subatomic physics. Ch.12 is large (~679 lines) but structurally regular across 8 prize problems. |
| `backmatter` | App A–F | Translation tables, paradox resolutions, DCVE, universal solver. Grouped separately from body chapters because they are reference material, not narrative derivation. App A translation tables may be replaced by cross-references to `ave-kb/common/` (see §5). |

**Depth analysis:** The structure is entry-point → vol2/index → domain/index → chapter/index → leaf = 4 levels. Ch.7 within `quantum-orbitals` could add a 5th level (subtopic group), but because ch.7 is the only chapter in its domain, the domain/index and chapter/index collapse: `vol2/quantum-orbitals/index.md` serves as both. The 13 subsections of ch.7 become the "subtopic" nodes (level 3), and their leaf files are level 4. Depth stays at 4. This is the correct flattening — confirmed by memory note: "trigger for 4-level: >20 chapters or >50 leaves."

---

## 3. Document Skeleton

Notation:
- `[index]` — navigation node; contains domain/chapter summary and Contents table
- `[leaf — verbatim]` — terminal document; contains verbatim translated source content
- `[leaf — placeholder]` — terminal document position defined; source content not yet fully surveyed at leaf granularity
- `[FLAG]` — anomaly note for distiller

### Top-level vol2 nodes

```
ave-kb/
  CLAUDE.md                              — [invariant scope: macros, environment names, ell-exception, resultbox-no-label rule, citestart/citeend; cross-cutting across all 8 volumes]
  entry-point.md                         — [top-level index: one-paragraph summary per volume + link to vol index; target <3000 tokens]
  common/
    index.md                             — [navigation index for shared translation tables and cross-volume reference content]
    translation-particle-physics.md      — [leaf — verbatim] source: ../common/translation_particle_physics.tex
    translation-qm.md                    — [leaf — verbatim] source: ../common/translation_qm.tex
    translation-circuit.md               — [leaf — verbatim] source: ../common/translation_circuit.tex
    translation-gravity.md               — [leaf — verbatim] source: ../common/translation_gravity.tex
    translation-cosmology.md             — [leaf — verbatim] source: ../common/translation_cosmology.tex
    translation-condensed-matter.md      — [leaf — verbatim] source: ../common/translation_condensed_matter.tex
    translation-protein.md               — [leaf — verbatim] source: ../common/translation_protein.tex
    translation-protein-solver.md        — [leaf — verbatim] source: ../common/translation_protein_solver.tex
    appendix-experiments.md              — [leaf — verbatim] source: ../common/appendix_experiments.tex (shared cross-volume)

  vol2/
    index.md                             — [vol2 domain index: one-paragraph per domain, key results surface, links to 5 domain indices]
```

### Domain: particle-physics (Ch 1–6)

```
    vol2/particle-physics/
      index.md                           — [domain index: covers ch.1–6 torus knot taxonomy through Higgs; surfaces major results per chapter; links to 6 chapter indices]

      ch01-topological-matter/
        index.md                         — [chapter index: mathematical topology of mass, torus knot ladder, chirality; links to 6 leaves]
        mathematical-topology-of-mass.md — [leaf — verbatim] source: ch.1 §1.1 — topology-as-mass framework
        lenz-inertia.md                  — [leaf — verbatim] source: ch.1 §1.2 — Newtonian inertia as macroscopic Lenz's Law; resultbox content
        electron-unknot.md               — [leaf — verbatim] source: ch.1 §1.3 — electron as fundamental unknot (0_1); resultbox: eq:dynamic_capacitance_yield
        regime-classification.md         — [leaf — verbatim] source: ch.1 §1.4 — topological matter regime classification table
        torus-knot-ladder.md             — [leaf — verbatim] source: ch.1 §1.5 — torus knot phase winding ladder (fermion generations)
        chirality-antimatter.md          — [leaf — verbatim] source: ch.1 §1.6 — chirality and antimatter disintegration

      ch02-baryon-sector/
        index.md                         — [chapter index: Borromean confinement, proton mass, baryon spectrum, neutron decay, He-4; links to 10 leaves]
        borromean-confinement.md         — [leaf — verbatim] source: ch.2 §2.1 — Borromean ring topology of baryon confinement
        proton-mass.md                   — [leaf — verbatim] source: ch.2 §2.2 — proton mass as dynamic tensor deficit; eq:torus_knot_ladder
        quark-flavors.md                 — [leaf — verbatim] source: ch.2 §2.2.1 — topological origin of quark flavors
        mass-oscillator.md               — [leaf — verbatim] source: ch.2 §2.3.1 (FIRST instance) — self-consistent mass oscillator (structural eigenvalue) [FLAG: duplicate subsection title; this leaf covers first instance ~line 114; see anomaly A2]
        mass-oscillator-second.md        — [leaf — verbatim] source: ch.2 §2.3.1 (SECOND instance ~line 166) — distinct content; flag for author review re: merge vs. rename [FLAG: anomaly A2]
        thermal-softening.md             — [leaf — verbatim] source: ch.2 §2.3.2 (sec:thermal_softening) — thermal softening and deconfinement transition
        hadronic-spectrum.md             — [leaf — verbatim] source: ch.2 §2.3.3 + §2.3 baryon resonance — hadronic spectrum table and resonance results
        topological-fractionalization.md — [leaf — verbatim] source: ch.2 §2.4 — topological fractionalization; fractional quark charges
        neutron-decay.md                 — [leaf — verbatim] source: ch.2 §2.5 — neutron decay mechanism
        helium4-nucleus.md               — [leaf — verbatim] source: ch.2 §2.6 + §2.7 — Helium-4 nucleus; hierarchy bridge

      ch03-neutrino-sector/
        index.md                         — [chapter index: chiral unknots, mass eigenvalue, oscillation, PMNS angles, hierarchy; links to 8 leaves]
        mass-without-charge.md           — [leaf — verbatim] source: ch.3 §3.1 — mass without charge (neutrino topology overview)
        chiral-exclusion.md              — [leaf — verbatim] source: ch.3 §3.2 (sec:chiral_screening) — chiral exclusion principle; eq:chiral_threshold
        neutrino-mass-eigenvalue.md      — [leaf — verbatim] source: ch.3 §3.3 — neutrino mass eigenvalue derivation
        neutrino-oscillation.md          — [leaf — verbatim] source: ch.3 §3.4 — neutrino oscillation mechanism
        pmns-mixing-angles.md            — [leaf — verbatim] source: ch.3 §3.5 (sec:pmns_eigenvalues, sec:pmns_junction) — PMNS mixing angles; eq:theta12_leading, eq:theta23_leading, eq:theta13, eq:pmns_13/12/23
        cp-violation.md                  — [leaf — verbatim] source: ch.3 §3.5–3.6 (sec:delta_cp) — CP-violation phase; eq:delta_cp_pmns
        neutrino-mass-hierarchy.md       — [leaf — verbatim] source: ch.3 §3.6 — neutrino mass hierarchy ordering
        dangling-full-derivation.md      — [leaf — placeholder] source: app:full_derivation_chain — referenced from ch.3 but not included in vol_2 main.tex [FLAG: anomaly A5; author must confirm whether backmatter/02_full_derivation_chain.tex should be \input-ted]

      ch04-quantum-spin/
        index.md                         — [chapter index: spin as gyroscopic precession, Larmor derivation; links to 3 leaves]
        spin-as-precession.md            — [leaf — verbatim] source: ch.4 §4.1–4.2 — introduction and framework for spin as classical gyroscopic precession
        larmor-derivation.md             — [leaf — verbatim] source: ch.4 §4.2.1 — Larmor derivation via topological gyroscopes
        visual-equivalence.md            — [leaf — verbatim] source: ch.4 §4.2.2 — visual equivalence: spinor transition continuous mechanics

      ch05-electroweak-mechanics/
        index.md                         — [chapter index: electrodynamics as phase gradient, weak interaction, gauge symmetry; links to 5 leaves]
        electrodynamics-phase-gradient.md — [leaf — verbatim] source: ch.5 §5.1 — electrodynamics as gradient of topological phase
        weak-interaction.md              — [leaf — verbatim] source: ch.5 §5.2 — weak interaction mechanism
        gauge-layer.md                   — [leaf — verbatim] source: ch.5 §5.3 — gauge symmetry as topological structure
        electroweak-summary.md           — [leaf — verbatim] source: ch.5 summarybox — chapter summary
        electroweak-objectives.md        — [leaf — verbatim] source: ch.5 objectivebox — chapter objectives [may merge with summary if trivially short]

      ch06-electroweak-higgs/
        index.md                         — [chapter index: Higgs reinterpretation, W/Z masses, lepton spectrum, anomalous moment, SM-AVE table; links to 9 leaves]
        higgs-reinterpretation.md        — [leaf — verbatim] source: ch.6 §6.1 — Higgs mechanism as topological vacuum condensate
        weak-mixing-angle.md             — [leaf — verbatim] source: ch.6 §6.2 — weak mixing angle derivation
        w-z-boson-masses.md              — [leaf — verbatim] source: ch.6 §6.3 — W and Z boson mass derivation
        wz-plasma-arcs.md                — [leaf — verbatim] source: ch.6 §6.4 — W and Z bosons as dielectric plasma arcs
        lepton-spectrum.md               — [leaf — verbatim] source: ch.6 §6.5 — three-generation lepton spectrum; eq:muon_twist_angle
        neutrino-mass-spectrum.md        — [leaf — verbatim] source: ch.6 §6.6 — neutrino mass spectrum (from Higgs perspective)
        anomalous-magnetic-moment.md     — [leaf — verbatim] source: ch.6 §6.7 — Schwinger anomalous magnetic moment
        sm-ave-translation.md            — [leaf — verbatim] source: ch.6 §6.8 (sec:sm_ave_translation) + ../common/translation_particle_physics.tex [NOTE: cross-reference to ave-kb/common/translation-particle-physics.md; distiller uses common/ leaf, does not duplicate]
```

### Domain: quantum-orbitals (Ch 7)

Ch.7 is ~3600 lines, its own domain. The domain/index serves as both domain and chapter index. 13 subsections become subtopic groups; leaves within each group correspond to section content or named resultboxes.

```
    vol2/quantum-orbitals/
      index.md                           — [domain + chapter index: ch.7 only; surfaces all key results: wavefunction reinterpretation, orbital resonance, hydrogen levels, helium coupling, analog filter model, geometry pipeline; links to 13 subsection leaves or groups; also provides cross-volume anchor for ch:quantum_orbitals label referenced by Vol 5]

      wavefunction-reinterpretation.md   — [leaf — verbatim] source: ch.7 §7.1 — deterministic reinterpretation of quantum wavefunction; AVE interpretation
      orbitals-as-cavities.md            — [leaf — verbatim] source: ch.7 §7.2 — orbitals as acoustic resonant cavities; conceptual framework
      hydrogen-energy-levels.md          — [leaf — verbatim] source: ch.7 §7.3 — hydrogen energy levels derivation; eq:de_broglie_n
      ode-orbital-verification.md        — [leaf — verbatim] source: ch.7 §7.3.1 (sec:ode_orbital_verification) — ODE-based orbital numerical verification; simbox results
      helium-symmetric-cavity.md         — [leaf — verbatim] source: ch.7 §7.4 (sec:helium_symmetric_cavity) — helium symmetric cavity approach
      qm-ave-translation.md              — [leaf — verbatim] source: ch.7 §7.5 (sec:qm_ave_translation) + ../common/translation_qm.tex [NOTE: cross-reference to ave-kb/common/translation-qm.md; distiller uses common/ leaf]
      analog-ladder-filter.md            — [leaf — verbatim] source: ch.7 §7.6 (sec:analog_ladder_filter) — atom as analog ladder filter; circuit model
      radial-tl-eigenvalue.md            — [leaf — verbatim] source: ch.7 §7.7 (sec:radial_tl_eigenvalue) — radial transmission-line eigenvalue; eq:screening_rule
      macro-cavity-saturation.md         — [leaf — verbatim] source: ch.7 §7.8 (sec:macro_cavity_saturation) — macro-cavity saturation model
      p-shell-isomorphism.md             — [leaf — verbatim] source: ch.7 §7.9 — p-shell isomorphism
      scale-separation.md                — [leaf — verbatim] source: ch.7 §7.10 (sec:scale_separation) — scale separation: knot topology vs orbital geometry; tab:knot_vs_orbital (first instance) [FLAG: anomaly A4 — tab:knot_vs_orbital duplicated in ch.12; these are distinct tables]
      subshell-junction-scattering.md    — [leaf — verbatim] source: ch.7 §7.11 (sec:lattice_js2) — sub-shell junction scattering (Phase 5)
      helium-coupling.md                 — [leaf — verbatim] source: ch.7 §7.12 — helium coupling from first principles; eq:bonding_mode, eq:omega_bond_derived
      geometry-pipeline.md              — [leaf — verbatim] source: ch.7 §7.13 (sec:geometry_pipeline) — geometry pipeline for orbital construction
      knot-vs-orbital-table.md           — [leaf — verbatim] source: ch.7 tab:knot_vs_orbital and tab:operator_domain — knot-to-orbital mapping table and QM/AVE operator domain table [FLAG: tab:knot_vs_orbital label also used in ch.12 for a different table; anomaly A4]
```

### Domain: foundations-validation (Ch 8–9)

```
    vol2/foundations-validation/
      index.md                           — [domain index: Planck-scale theory and computational verification; links to 2 chapter indices]

      ch08-planck-scale/
        index.md                         — [chapter index: string tension, extra dimensions, topological resonance; links to 4 leaves]
        dimensionality-crisis.md         — [leaf — verbatim] source: ch.8 §8.1 — the dimensionality crisis in string theory
        string-tension-inductance.md     — [leaf — verbatim] source: ch.8 §8.2 — string tension as mutual inductance
        no-extra-dimensions.md           — [leaf — verbatim] source: ch.8 §8.3 — why extra dimensions are unnecessary in AVE
        topological-resonance.md         — [leaf — verbatim] source: ch.8 §8.4 — topological resonance vs closed strings

      ch09-computational-proof/
        index.md                         — [chapter index: scale invariance proof, anomaly catalog, precision policy; links to 6 leaves]
        scale-invariance-proof.md        — [leaf — verbatim] source: ch.9 §9.1 — computational proof of scale invariance
        verification-summary.md          — [leaf — verbatim] source: ch.9 §9.2 — verification summary table across scales
        anomaly-catalog.md               — [leaf — verbatim] source: ch.9 §9.3 (sec:anomaly_catalog) — anomaly catalog Tiers 2–4 (§9.3.1–9.3.3)
        precision-policy.md              — [leaf — verbatim] source: ch.9 §9.4 (sec:precision_policy) — numerical precision policy
        methodological-contamination.md  — [leaf — verbatim] source: ch.9 §9.5 (sec:methodological_contamination) — avoidance of methodological contamination
        internal-label-note.md           — [leaf — placeholder] source: ch.9 internal ref ch:quantum_mechanics_and_orbitals [FLAG: anomaly A7 — internal typo; actual label is ch:quantum_orbitals; no content change needed but distiller should annotate the cross-reference in scale-invariance-proof.md]
```

**Note on ch09 internal label:** anomaly A7 does not require a separate file. The flag should be recorded as an annotation within `scale-invariance-proof.md` or `verification-summary.md`, not a standalone leaf. Remove `internal-label-note.md` from the final build — absorbed into the annotation convention.

### Domain: open-problems (Ch 10–12)

```
    vol2/open-problems/
      index.md                           — [domain index: cosmological open problems, SM reach, millennium prizes; links to 3 chapter indices]

      ch10-open-problems/
        index.md                         — [chapter index: strong CP, baryon asymmetry, Hubble tension, g*=85.75 prediction, scale invariance; links to 8 leaves]
        strong-cp.md                     — [leaf — verbatim] source: ch.10 §10.1 (sec:strong_cp) — strong CP problem and AVE resolution
        baryon-asymmetry.md              — [leaf — verbatim] source: ch.10 §10.2 (sec:baryon_asymmetry) — baryon asymmetry resolution; eq:eta_baryon
        hubble-tension.md                — [leaf — verbatim] source: ch.10 §10.3 (sec:hubble_tension) — Hubble tension resolution
        g-star-prediction.md             — [leaf — verbatim] source: ch.10 §10.4 (sec:g_star_prediction) — testable prediction g*=85.75; eq:g_star_ave
        scale-invariance-principle.md    — [leaf — verbatim] source: ch.10 §10.5 (sec:scale_invariance) — scale invariance principle; tab:scale_invariance
        open-problems-resolutions.md     — [leaf — verbatim] source: ch.10 §10.6 (sec:open_problems_resolutions) — quantitative resolutions summary
        dangling-ch-mass-gap.md          — [leaf — placeholder] [FLAG: anomaly A6 — ch:mass_gap referenced here but not defined in vol_2; content is in ch.12 §12.2 under sec:ym_millennium; distiller should replace this reference with a cross-reference to vol2/open-problems/ch12-millennium/yang-mills-mass-gap.md]
        dangling-ch-navier-stokes.md     — [leaf — placeholder] [FLAG: anomaly A6 — ch:navier_stokes referenced here but content is in ch.12 §12.1 under sec:ns_millennium; distiller should replace with cross-reference to vol2/open-problems/ch12-millennium/navier-stokes.md]

      ch11-sm-overdrive/
        index.md                         — [chapter index: universal energy functional, lattice QCD, AlphaFold overdrive, scaling table; links to 5 leaves]
        universal-energy-functional.md   — [leaf — verbatim] source: ch.11 §11.1 — universal Faddeev-Skyrme energy functional; eq:universal_energy
        overdrive-nuclear.md             — [leaf — verbatim] source: ch.11 §11.2 (sec:overdrive_nuclear) — overdriving lattice QCD
        overdrive-protein.md             — [leaf — verbatim] source: ch.11 §11.3 (sec:overdrive_protein) — overdriving AlphaFold protein folding [NOTE: cross-volume — Vol 5 biology content; > → Primary: vol5/quantum-biology/ch02-protein-folding/index.md (when constructed)]
        overdrive-comparison-table.md    — [leaf — verbatim] source: ch.11 §11.4 + tab:overdrive_comparison — computational scaling comparison table
        axiom-survey.md                  — [leaf — verbatim] source: ch.11 axiombox instances — axioms enumerated in ch.11 (SM overdrive domain)

      ch12-millennium/
        index.md                         — [chapter index: 7 millennium prize problems + synthesis; links to 14 leaves]
        navier-stokes.md                 — [leaf — verbatim] source: ch.12 §12.1 (sec:ns_millennium) — Navier-Stokes: lattice enstrophy bound; eq:lattice_ns, eq:laplacian_norm, eq:enstrophy_bound
        yang-mills-mass-gap.md           — [leaf — verbatim] source: ch.12 §12.2 (sec:ym_millennium) — Yang-Mills mass gap; eq:bogomolnyi_bound (FIRST occurrence) [FLAG: anomaly A3 — eq:bogomolnyi_bound appears twice in this chapter; distiller must disambiguate by line range]
        bogomolnyi-second.md             — [leaf — verbatim] source: ch.12 §12.2 later derivation — second occurrence of eq:bogomolnyi_bound [FLAG: anomaly A3; eq:gauge_rank, eq:confinement_radius, eq:confinement_gamma likely in this section; verify source lines]
        riemann-hypothesis.md            — [leaf — verbatim] source: ch.12 §12.3 (sec:rh_millennium) — Riemann hypothesis: zeta zeros as lattice dispersion poles; eq:lattice_dispersion
        hodge-conjecture.md              — [leaf — verbatim] source: ch.12 §12.4 (sec:hc_millennium) — Hodge conjecture and topological cycles
        bsd-conjecture.md                — [leaf — verbatim] source: ch.12 §12.5 (sec:bsd_millennium) — Birch and Swinnerton-Dyer conjecture
        p-vs-np.md                       — [leaf — verbatim] source: ch.12 §12.6 (sec:pnp_millennium) — P vs NP and topological complexity
        poincare-conjecture.md           — [leaf — verbatim] source: ch.12 §12.7 (sec:poincare_millennium) — Poincaré conjecture and 3-manifold topology
        millennium-synthesis.md          — [leaf — verbatim] source: ch.12 §12.8 (sec:millennium_synthesis) — synthesis: common lattice structure across Millennium problems
        knot-vs-orbital-table-ch12.md    — [leaf — verbatim] source: ch.12 tab:knot_vs_orbital — the SECOND knot-vs-orbital table (distinct from ch.7 version) [FLAG: anomaly A4 — same label, different content; distiller must not merge these]
```

**Note on ch10 dangling-ref placeholders:** `dangling-ch-mass-gap.md` and `dangling-ch-navier-stokes.md` are structural placeholders only — they mark the locations where content is expected but content lives in ch.12. They should contain a single redirect note (not verbatim source) pointing to the correct leaf. They are the only leaves in this skeleton that are not verbatim — they are navigation redirects. Mark them `<!-- leaf: redirect -->`.

### Domain: backmatter (Appendices A–F)

```
    vol2/backmatter/
      index.md                           — [backmatter index: translation matrix, paradox resolutions, computational graph, DCVE, universal solver; links to 5 appendix indices]

      app-a-translation-matrix/
        index.md                         — [appendix index: 8 translation tables — all cross-reference to ave-kb/common/; no verbatim duplication here]
        [NOTE: All 8 translation tables are in ave-kb/common/. App A's index.md contains only the section header and links to common/ leaves. No leaf files are created here — content lives at ave-kb/common/translation-*.md]

      app-b-paradox-resolutions/
        index.md                         — [appendix index: spin-1/2 paradox, holographic information paradox, Peierls-Nabarro friction paradox]
        spin-half-paradox.md             — [leaf — verbatim] source: app B — resolving spin-1/2 rotation paradox
        holographic-paradox.md           — [leaf — verbatim] source: app B — holographic information paradox resolution
        peierls-nabarro-paradox.md       — [leaf — verbatim] source: app B — Peierls-Nabarro friction paradox resolution

      app-d-computational-graph/
        index.md                         — [appendix index: computational graph architecture for AVE]
        graph-architecture.md            — [leaf — verbatim] source: app D (app:computational_graph) — computational graph architecture overview
        cross-scale-isomorphism.md       — [leaf — verbatim] source: app D — cross-scale isomorphism (BH QNM, electron, nuclear, protein, antenna, tokamak, BLDC motor)

      app-e-dcve/
        index.md                         — [appendix index: discrete chiral LC vacuum electrodynamics]
        dcve-foundations.md              — [leaf — verbatim] source: app E (app:dcve) — DCVE theoretical foundations
        dcve-equations.md                — [leaf — verbatim] source: app E — DCVE core equations and circuit model
        dcve-results.md                  — [leaf — verbatim] source: app E — DCVE key results and verification

      app-f-universal-solver/
        index.md                         — [appendix index: universal solver toolchain description]
        solver-overview.md               — [leaf — verbatim] source: app F (app:solver_toolchain) — universal solver toolchain overview
        solver-modules.md                — [leaf — verbatim] source: app F — solver module descriptions
        solver-verification.md           — [leaf — verbatim] source: app F — solver verification results
        solver-usage.md                  — [leaf — verbatim] source: app F — solver usage guide
        solver-code.md                   — [leaf — verbatim] source: app F codebox instances — SPICE netlists / code blocks

      app-c-derivations/
        index.md                         — [appendix index: summary of exact analytical derivations]
        exact-derivations-summary.md     — [leaf — verbatim] source: app C — summary table of exact analytical derivations (no label defined in survey)
```

**Note on App C:** Survey lists App C as "Summary of Exact Analytical Derivations — no label." Single index + one leaf is the correct treatment.

---

## 4. Navigation Spec

### Up-link format

Every document except `ave-kb/entry-point.md` carries exactly one up-link on line 1. Format:

```markdown
[↑ Vol 2: The Subatomic Scale](../index.md)
```

Specific level examples:

| Level | Up-link line |
|---|---|
| Leaf in chapter | `[↑ Ch.1: Topological Matter](../index.md)` |
| Chapter index | `[↑ Particle Physics](../index.md)` |
| Domain index | `[↑ Vol 2: The Subatomic Scale](../index.md)` |
| Vol 2 index | `[↑ Entry Point](../../entry-point.md)` |

Machine-check pattern: `^\[↑ ` (Unicode ↑ U+2191 at start of line 1).

### Down-link format

Index documents carry a `## Contents` section at the bottom:

```markdown
## Contents

- [Ch.1: Topological Matter](ch01-topological-matter/index.md) — torus knot fermion generation ladder, electron as 0_1 unknot, chirality
- [Ch.2: Baryon Sector](ch02-baryon-sector/index.md) — Borromean confinement, proton mass, baryon resonance spectrum
...
```

### Leaf marker

Line 2 of every leaf document (after up-link):

```markdown
<!-- leaf: verbatim -->
```

Redirect leaves use:
```markdown
<!-- leaf: redirect -->
```

Placeholder leaves use:
```markdown
<!-- leaf: placeholder — [reason] -->
```

### Cross-volume reference format

Two blockquote types, both on their own line:

```markdown
> → Primary: [Ch.7: Quantum Mechanics and Orbitals](../../vol2/quantum-orbitals/index.md) — definition of ch:quantum_orbitals
> ↗ See also: [Protein Folding](../../vol5/quantum-biology/ch02-protein-folding/index.md) — applies orbital cavity model to protein beta-sheets
```

`→ Primary:` = structural dependency (follow if definition is needed)
`↗ See also:` = optional suggestion (follow if additional context is useful)

### Vol 5 → Vol 2 cross-reference (specific)

Vol 5 ch.3 references `ch:quantum_mechanics` (4 occurrences). The canonical KB location is:

```
ave-kb/vol2/quantum-orbitals/index.md
```

In Vol 5 ch.3 leaves, the cross-reference reads:

```markdown
> → Primary: [Quantum Mechanics and Atomic Orbitals (Vol 2, Ch.7)](../../vol2/quantum-orbitals/index.md) — ch:quantum_orbitals; deterministic wavefunction, orbital resonance cavities
```

Note: The LaTeX label `ch:quantum_mechanics` used in Vol 5 is a DIFFERENT label name from the actual Vol 2 label `ch:quantum_orbitals`. This is NOT an anomaly in Vol 2 — it is a Vol 5 prose reference that uses an informal label. The KB cross-reference above resolves it correctly regardless of the label name used in the source.

### Entry-point format (vol2 section)

In `ave-kb/entry-point.md`, the Vol 2 entry reads:

```markdown
## Vol 2: The Subatomic Scale

Derives particle physics from torus knot topology: fermion generations as knot ladders, baryon confinement via Borromean rings, neutrino masses via chiral unknots, W/Z boson masses as dielectric plasma arcs. Chapter 7 (~3600 lines) reinterprets quantum mechanics as acoustic resonant cavity theory. Chapters 10–12 resolve cosmological open problems and address all seven Millennium Prize Problems from lattice topology. Key cross-volume dependency: `ch:quantum_orbitals` is referenced by Vol 5.

[Vol 2 Index](vol2/index.md)
```

---

## 5. Shared Content Decision (Translation Tables)

**Recommendation: dedicate `ave-kb/common/` pages, referenced from each volume.**

Reasoning:

1. **Duplication multiplier is high.** The 8 `../common/translation_*.tex` files appear across multiple volumes. Vol 2 alone references 8 of them; the full matrix across all 8 volumes would yield ~20–30 duplicate leaf instances if each volume maintained its own copy.

2. **Agent navigation cost is low.** A cross-volume pointer `> → Primary: [Translation: Particle Physics](../common/translation-particle-physics.md)` is one hop. An agent navigating from a leaf in vol2/particle-physics/ to the SM-AVE translation table traverses: leaf → ch06 index → common/ (3 hops total, all documented). This is acceptable.

3. **Maintenance coherence.** If the source `translation_*.tex` file is updated, there is one KB leaf to update, not N.

4. **Exception:** `sec:sm_ave_translation` in ch.6 §6.8 and `sec:qm_ave_translation` in ch.7 §7.5 are in-chapter sections that introduce/frame the translation tables — these section headings and introductory prose belong in the chapter leaf (`sm-ave-translation.md` and `qm-ave-translation.md`), which then contains a `→ Primary:` pointer to `ave-kb/common/translation-*.md` for the verbatim table content. The chapter leaf is NOT a duplicate — it contains the section introduction; the common leaf contains the verbatim table.

**Distiller instruction:** When converting ch.6 §6.8, place the section header and introductory paragraphs in `vol2/particle-physics/ch06-electroweak-higgs/sm-ave-translation.md`, with `> → Primary: [SM/AVE Translation Table](../../../common/translation-particle-physics.md)` for the table itself.

---

## 6. Anomaly Registry (for distiller handoff)

| ID | Location | Type | Distiller action |
|---|---|---|---|
| A1 | Ch.7 entire (~3600 lines) | Size anomaly | Ch.7 gets own domain `quantum-orbitals/`; 14 leaves mapped to subsection granularity |
| A2 | ch02 §2.3.1 | Duplicate subsection title (~lines 114 and 166) | Two separate leaves: `mass-oscillator.md` (first instance) and `mass-oscillator-second.md` (second instance); flag both for author review |
| A3 | ch12 §12.2 | Duplicate eq:bogomolnyi_bound label | Two leaves: `yang-mills-mass-gap.md` (first occurrence) and `bogomolnyi-second.md` (second); identify by line range in source; do not merge |
| A4 | ch07 and ch12 | Duplicate tab:knot_vs_orbital label | Two distinct tables; `scale-separation.md` (ch.7) and `knot-vs-orbital-table-ch12.md` (ch.12); do not merge or treat as same content |
| A5 | ch03, backmatter | Dangling ref app:full_derivation_chain | Placeholder `dangling-full-derivation.md` in ch03; author must confirm if backmatter/02_full_derivation_chain.tex should be input-ted |
| A6 | ch10 | Dangling refs ch:mass_gap, ch:navier_stokes | Redirect placeholders in ch10; content is in ch12 §12.2 and §12.1 respectively |
| A7 | ch09 | Internal label typo (ch:quantum_mechanics_and_orbitals) | Annotate in scale-invariance-proof.md; no structural change; correct target is vol2/quantum-orbitals/index.md |
| A8 | All chapters | amsthm envs defined but unused | No action; no theorem/lemma/definition leaves needed |
| A9 | ch01, ch03 file comments | Stale internal file-number comments | No action; _manifest.tex ordering is authoritative |
| A10 | All chapters | resultbox has no \label | Identify results by title string + source line range; record both in leaf file header comment |

---

## 7. Acceptance Criteria

1. **Up-link completeness:** every file in `ave-kb/vol2/` (and `ave-kb/common/`) except `ave-kb/entry-point.md` contains `^\[↑ ` on line 1.
   Shell check: `find /path/to/ave-kb/vol2 -name "*.md" | xargs grep -rL "^\[↑ "` returns empty.

2. **Entry-point token budget:** `ave-kb/entry-point.md` is under 3000 tokens.
   Shell proxy: `wc -w ave-kb/entry-point.md` returns ≤ 2200 words.

3. **Depth constraint:** no file in `ave-kb/vol2/` is more than 4 path segments below `ave-kb/`.
   Shell check: `find ave-kb/vol2 -name "*.md" | awk -F/ 'NF>7 {print}'` returns empty (7 = ave-kb/vol2/domain/chapter/leaf).

4. **Leaf marker presence:** every terminal (leaf) document contains `<!-- leaf: verbatim -->`, `<!-- leaf: redirect -->`, or `<!-- leaf: placeholder` on line 2.
   Shell check: `find ave-kb/vol2 -name "*.md" | xargs grep -L "<!-- leaf:"` returns only index files.

5. **Anomaly A3 — no label merge:** `ave-kb/vol2/open-problems/ch12-millennium/yang-mills-mass-gap.md` and `bogomolnyi-second.md` both exist as distinct files and both reference `eq:bogomolnyi_bound` with different source line ranges in their header comments.

6. **Anomaly A4 — no table merge:** `ave-kb/vol2/quantum-orbitals/scale-separation.md` and `ave-kb/vol2/open-problems/ch12-millennium/knot-vs-orbital-table-ch12.md` both exist and neither contains a `<!-- leaf: verbatim -->` marker on the same content.

7. **ch:quantum_orbitals cross-volume reachability:** `ave-kb/vol2/quantum-orbitals/index.md` exists and contains a prose anchor explicitly identifying it as the target for Vol 5's `ch:quantum_mechanics` cross-reference. Navigating from `ave-kb/vol5/` to this node requires at most 2 hops following `→ Primary:` pointers.

8. **Translation tables not duplicated:** `ave-kb/common/translation-particle-physics.md` exists; `ave-kb/vol2/particle-physics/ch06-electroweak-higgs/sm-ave-translation.md` does NOT contain the full verbatim table — it contains only the section introduction and a `→ Primary:` pointer. Check: the common file is larger than the chapter leaf.

9. **CLAUDE.md invariant usage:** each constant or macro listed in `ave-kb/CLAUDE.md` is referenced in at least 2 distinct volume subdirectory trees. Check by searching for macro name strings (e.g., `\lp`, `\Zvac`) across `ave-kb/vol*/`.

10. **Dangling-ref placeholders visible in parent Contents:** `ave-kb/vol2/open-problems/ch10-open-problems/index.md` Contents table includes entries for `dangling-ch-mass-gap.md` and `dangling-ch-navier-stokes.md` with `[FLAG]` annotations; `ave-kb/vol2/ch03-neutrino-sector/index.md` includes entry for `dangling-full-derivation.md`.

---

## 8. File Count Summary

### Index files (navigation nodes)
| Level | Count |
|---|---|
| Vol 2 index (1) + domain indices (5) | 6 |
| Chapter/appendix indices (12 chapters + 6 appendix sub-indices) | 18 |
| common/ index (1) | 1 |
| **Index subtotal** | **25** |

### Leaf files
| Domain | Leaf count |
|---|---|
| common/ translation + experiments | 9 |
| particle-physics (ch.1–6) | 6 + 10 + 8 + 3 + 5 + 9 = 41 |
| quantum-orbitals (ch.7) | 14 |
| foundations-validation (ch.8–9) | 4 + 5 = 9 |
| open-problems (ch.10–12) | 8 + 5 + 10 = 23 |
| backmatter (app A–F) | 0 + 3 + 2 + 3 + 5 + 1 = 14 |
| **Leaf subtotal** | **~110** |

**Total files:** ~25 index + ~110 leaf = **~135 files**

Note: App A has 0 leaf files because all 8 translation tables live in `ave-kb/common/`. The 135 total is within the survey estimate of 125–135 KB leaves, with the small discrepancy explained by the anomaly-resolution placeholders (4 files) and the App A→common redirect structure.

---

## 9. Key Design Decisions (summary)

1. **Ch.7 as its own domain** (`quantum-orbitals/`): justified by 10× size anomaly and distinct mathematical subject matter. Domain/index and chapter/index collapse into single node. 14 subsection-level leaves fit within 4-level depth constraint.

2. **`ave-kb/common/` for translation tables**: all 8 `../common/translation_*.tex` files and `appendix_experiments.tex` go to a shared `ave-kb/common/` directory. Chapter-level leaves in particle-physics and quantum-orbitals contain only the section introduction + `→ Primary:` pointer, not the verbatim table. This eliminates cross-volume duplication for content that will appear in multiple volume KBs.

3. **Anomaly A2 (duplicate subsection)**: materialized as two distinct leaf files rather than merged. Author review flag embedded in both files. This preserves fidelity to source.

4. **Anomaly A3/A4 (duplicate labels)**: each occurrence gets its own leaf with line-range disambiguation in the header comment. The LaTeX label collision does not affect the KB because KB navigation uses file paths, not LaTeX labels.

5. **Dangling references (A5, A6) as redirect placeholders**: rather than silently dropping the references, they become `<!-- leaf: redirect -->` files that name the correct destination. This prevents silent navigation dead-ends.

6. **Vol 5 → `ch:quantum_orbitals` linkage**: the `quantum-orbitals/index.md` explicitly declares its cross-volume anchor role. The label mismatch (`ch:quantum_mechanics` in Vol 5 prose vs `ch:quantum_orbitals` in Vol 2) is resolved by prose annotation in both the Vol 2 domain index and in the Vol 5 leaves (when constructed).

7. **objectivebox/summarybox/exercisebox leaves**: Vol 2 has these per-chapter, unlike some other volumes. They are absorbed into chapter-level leaf content (objectives into the first leaf or chapter index; summaries/exercises into the last leaf). They are not given separate leaf files unless their content is independently significant — this avoids leaf proliferation for boilerplate structural elements.
