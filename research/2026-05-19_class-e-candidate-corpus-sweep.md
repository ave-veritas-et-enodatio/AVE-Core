# Class E Candidate Corpus Sweep — Inventory of Operating-Point-Projection Candidates

**Date**: 2026-05-19 EOD
**Branch**: `analysis/h-infinity-downstream-cascade`
**Epic**: Phase 3 of [`_orchestration/_archive/h-infinity-downstream-cascade.md`](../_orchestration/_archive/h-infinity-downstream-cascade.md)
**Originating skill canonization**: `consistency-vs-emergence` v1.1 at skills repo commit `470f1ec` (Class E added — operating-point projection / topological equilibrium observable; Grant canonized 2026-05-19 EOD)
**Lane**: implementer (inventory only; NO reclassification of these candidates in this epic — that's a separate queued epic post-Grant adjudication per brief constraint)
**Skills applied**: `consistency-vs-emergence` v1.1, `verify-before-cite` v1.3, `ave-canonical-leaf-pull`, `ave-prereg`

---

## §0 Purpose + scope constraint

Per the h-infinity-downstream-cascade epic Phase 3 brief: the skill v1.1 body's "When Class C vs Class E?" discriminator + Class E asymmetry note flags that the corpus likely has multiple Class E candidates currently classified elsewhere (Class C / B / A / D / engineering_limit). This phase is an **inventory-only sweep**:

- Enumerate each candidate's current classification (per `predictions.yaml` type or implicit corpus framing).
- Apply the Class E discriminator (*"does the prediction sit on a chain that requires a substrate operating-point such that removing the operating-point destroys N predictions simultaneously?"*) to flag candidacy.
- Document the cascade-implication scope per candidate (how many corpus files would touch if Class E refinement were applied later).
- **Do NOT reclassify any of these candidates in this session.** Reclassification of each candidate is queued for a separate future epic per Grant adjudication.

**Scope-correction note**: The H_∞ + {G, Ω_freeze, α} family (Phase 2 of this epic) is ALREADY reclassified to Class E in this branch — that's not part of the candidate sweep because it's the source case that drove the v1.1 canonization. This sweep is for OTHER candidates.

---

## §1 Discriminator (per skill v1.1)

Per [`~/.claude/skills/consistency-vs-emergence/SKILL.md`](skill, external to repo) §"When Class C vs Class E?":

> **Class C** is "we have ONE target, and our derivation routes through a CODATA-derived intermediate via SI substitution. Removing the SI substitution destroys the derivation. Novelty is in mechanism." (canonical: solar deflection through lattice refraction.)
>
> **Class E** is "we have N targets, and they're constrained by a single substrate operating-point. We can't predict ANY of the N from substrate primitives alone, but we have ONE free parameter (the operating-point) that ties all N together. Removing the assumption of equilibrium destroys the whole set, not just one entry. Novelty is in the cross-scale topological bridge, not the individual values." (canonical: $H_\infty$, $G$, $\hat{\Omega}_{\text{freeze}}$, $\alpha$ all derive from $u_0^* \approx 0.187$.)
>
> **Discriminator question**: does the prediction sit on a chain that requires a CODATA-derived intermediate (Class C), or does it sit on a chain that requires a substrate operating-point (Class E)? If removing one intermediate destroys ONE prediction, it's Class C. If removing one operating-point parameter destroys N predictions simultaneously, it's Class E.

Additional inverse-failure-mode flag: *"a Class C observable miscategorized as Class E looks like 'we have a joint-constraint set' when the observable actually only depends on one CODATA-derived intermediate. The discriminator is: are there OTHER substrate observables constrained by the SAME parameter? If yes, Class E. If no, it's still Class C even if the language sounds joint."*

---

## §2 Candidate inventory

### Candidate 1 — $M / Q / J$ at $\Gamma = -1$ boundary observables

**Canonical source**: [`manuscript/ave-kb/common/boundary-observables-m-q-j.md`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md) — the three integrated boundary observables ($\mathcal{M}$, $\mathcal{Q}$, $\mathcal{J}$) at every $\Gamma = -1$ saturation surface.

**Current classification**: implicit Class C per scale-instance (no `predictions.yaml` entry directly named "M/Q/J set" — appears scale-distributed across P02 / P07 / P08 / multiple particle-mass entries).

**Class E discriminator application**: STRONG candidate. Per skill v1.1 §"In-session validation":
> *"Boundary-observable analog: per `boundary-observables-m-q-j.md`, the $M / Q / J$ observables at $\Gamma = -1$ boundaries are also joint-constrained. Class E applies."*

The three observables at any $\Gamma = -1$ surface are tied at the substrate operating point (the surface's saturation kernel state); failure of any one (e.g., observed $M$, $Q$, $J$ at a given scale not satisfying the three-invariant boundary integrals) falsifies the universal substrate-observability rule at that scale.

**Sub-case structure**: per `boundary-observables-m-q-j.md` §"Same mechanism at all scales", M/Q/J observables manifest at 6 scales:
- Electron ($\ell \sim 10^{-13}$ m) — $m_e c^2$, $e$, $\hbar/2$
- Nucleus ($\ell \sim 10^{-15}$ m) — nucleon mass, electric charge, nuclear spin
- Atom ($\ell \sim 10^{-10}$ m) — atomic mass, ionization, total angular momentum
- Planetary magnetopause — planet mass, dipole moment, rotation
- Black-hole event horizon — $M$, $Q$, $J$ (Kerr-Newman)
- Cosmic horizon ($R_H \sim 10^{26}$ m) — $\mathcal{M}_\text{cosmic}$, $\mathcal{Q}_\text{cosmic}$, $\mathcal{J}_\text{cosmic}$

**Sub-discriminator**: within EACH scale instance, the three observables are NOT independent — they share the same boundary surface and same substrate-internal solitons. The triplet at each scale is one Class E candidate; the cross-scale "same mechanism" structure is a meta-Class E candidate.

**Cascade-implication scope (if Class E refinement applied later)**:
- `boundary-observables-m-q-j.md` (primary leaf) — add Class E framing block; estimated +30 lines
- `manuscript/frontmatter/00_foreword.tex` — `Same mechanism at all scales` paragraph reframed as Class E projection; estimated +10 lines
- `manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex` §sec:substrate_vocab_box_ch1 — vocabulary box update; estimated +5 lines
- Per-scale instance leaves at vol2 / vol3 / vol4 / vol7 carrying M/Q/J observable claims — estimated 6-12 leaves touched
- `manuscript/predictions.yaml` — multi-entry type review pass (P02 / P07 / P08 / proton charge / etc.) — estimated 8-15 type fields changed

**Recommended Grant adjudication priority**: HIGH — most empirically load-bearing of the candidates listed here; touches every scale of the substrate.

**Open question for Grant adjudication**:
- Per skill v1.1 §"Next probe due (2026-08-17)": *"Probe whether Class E discriminator covers all operating-point-projection variants, OR if there are further sub-classes hiding within (boundary-observable cascade vs cosmic-genesis operating-point vs saturation-kernel scale-instance — three Class-E sub-types?)"*. M/Q/J is a candidate for "boundary-observable cascade" sub-type; H_∞-family is "cosmic-genesis operating-point" sub-type. Discriminator-refinement-vs-single-Class-E is an open methodological question.

---

### Candidate 2 — 8 testable observables of Ω_freeze

**Canonical source**: [`manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:46-58`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) §3 "Eight testable observables (Tier-2 framework synthesis)".

**Current classification**: Tier-2 framework synthesis (not a single `predictions.yaml` type — distributed across multiple entries and A-034 prereg).

The 8 observables:
1. CMB axis-of-evil (Planck PR3 low-$\ell$ multipoles)
2. Hubble flow anisotropy (Pantheon+ supernova compilation)
3. LSS spin direction (SDSS galaxy spin axes — A-031 pending; SDSS DR17 epic in-flight on `analysis/c5-sdss-dr17-spin-orientation`)
4. Matter asymmetry direction (CMB temperature + matter density correlation)
5. E/B polarization decoupling (Planck PR3 + BICEP/Keck + LiteBIRD)
6. Orbital-plane alignment (Solar system ecliptic + Gaia DR3 binaries + SDSS galactic disks + LIGO/Virgo)
7. G anisotropy via tensor extension ($\Delta G/G \sim \alpha^N$ along $P_2(\cos\theta)$, conjectural)
8. CMB QNM matching (Hawking/ring-down via cosmic-horizon QNM at $\omega_R M_g = 18/49$)

**Class E discriminator application**: STRONG candidate. All 8 observables share the single $\hat{\Omega}_\text{freeze}$ axis at $(l=60.28°, b=50.48°)$ (Planck PR3 SMICA empirical pin 2026-05-19 per `research/2026-05-19_c5-cmb-axis-executable-observer-result.md:17`); failure of any one to align with the axis at significant significance falsifies the cosmic-grain-cascade framework.

**Sub-discriminator note (skill v1.1 inverse failure mode)**: each observable's individual measurement is NOT a Class C consistency check (none route through CODATA SI substitution); each is a directional-alignment measurement against a substrate-native preferred axis. The Class E joint-constraint is "all 8 observables must agree on the SAME axis at relevant significance, OR the framework is falsified" — which is genuinely a joint constraint.

**Cascade-implication scope (if Class E refinement applied later)**:
- `omega-freeze-cosmic-grain-cascade.md` (primary) — §3 table get Class E framing block per row; estimated +30 lines (one Class E row classification per observable)
- A-034 prereg + result documents — per-observable type extension; estimated 4-6 research docs touched
- `manuscript/frontmatter/00_foreword.tex` "three-route framework commitment" passage — extend with Class E framing; estimated +5 lines
- `manuscript/predictions.yaml` — multi-entry type review (per-observable entries if/when promoted to manuscript predictions); estimated 6-8 entries (mostly pre-registered) get Class E type

**Recommended Grant adjudication priority**: HIGH — the framework's sharpest empirical commitment per `omega-freeze-cosmic-grain-cascade.md:5` ("**the framework's sharpest empirical commitment**"). Active in-flight: SDSS DR17 epic on `analysis/c5-sdss-dr17-spin-orientation` tests Observable 3 (LSS spin direction); orbital-plane alignment (Observable 6) tested in A-034.

**Sub-question for Grant adjudication**: Observable 7 (G anisotropy) is conjectural at amplitude (N=2 vs higher α-powers); see L3 doc 119 honest adjudication. Sub-question is whether conjectural-amplitude Class E candidates get inventoried as full Class E or as Class E-pending until amplitude is derived.

---

### Candidate 3 — Hoop-stress 2π cross-scale motif

**Canonical source**: [`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md) §"Cross-volume substrate motif: Hoop Stress 2π projection at multiple scales (NEW 2026-05-17)".

**Current classification**: implicit Class B (axiom manifestation) per axiom-4-saturation framing at each scale instance; no unified `predictions.yaml` entry for the motif.

The motif: substrate bulk drift $c \times \epsilon$ projected through the $2\pi$ Hoop Stress geometric factor onto closed topological loops gives the observable equilibrium scale, at:
- **Cosmic scale** (MOND): $a_0 = c \cdot H_\infty / (2\pi) \approx 1.07 \times 10^{-10}$ m/s² (cosmic horizon loop, $\epsilon = H_\infty$)
- **Substrate scale** (electron α-slew): $v_\text{substrate} = c \cdot \alpha / (2\pi) \approx 348.2$ km/s (electron unknot loop, $\epsilon = \alpha$); LSR-class scope only per `research/2026-05-17_substrate_equilibrium_velocity_GLOBULAR_CLUSTER_result.md` Outcome III

**Class E discriminator application**: WEAK-MODERATE candidate. The motif is genuinely cross-scale (substrate $2\pi$ Ideal Ropelength for the unknot per `vol3/gravity/ch01-gravity-yield/leaky-cavity-decay.md:12` + `kinetic-yield-threshold.md:22` is rigorous; cosmic $2\pi$ via Unruh-Hawking is asserted-not-derived per `mond-hoop-stress.md:83`).

The Class E question: are the cosmic-scale $a_0$ and substrate-scale $v_\text{substrate}$ joint-constrained by a single substrate operating-point, or are they two SEPARATE instances of the same axiomatic mechanism?

**Per skill v1.1 inverse failure mode**: this looks MORE like a Class B axiom-manifestation pattern (same Hoop-stress $2\pi$ projection mechanism at multiple scales, with different scale-instance small-parameters $\epsilon \in \{H_\infty, \alpha\}$) than a Class E joint-constraint (where N observables share ONE operating-point). The substrate operating-point that ties both scales would have to be $u_0^* \approx 0.187$ acting through (a) Hoop-stress at cosmic scale via $H_\infty$ projection (Class E via H_∞ joint-constraint structure), AND (b) Hoop-stress at substrate scale via $\alpha$ projection (Class E via α joint-constraint structure). The motif is the SHARED MECHANISM, not the SHARED PARAMETER.

**Subtle Class E sub-candidate**: if $\alpha$ AND $H_\infty$ are BOTH Class E projections of $u_0^*$ (which they are per Phase 2 + skill v1.1 H_∞ origin case), then the Hoop-stress motif's BOTH instances inherit Class E status FROM THE OPERATING POINT, not from the motif itself. Class E applies to the operating-point structure; Class B applies to the cross-scale mechanism.

**Cascade-implication scope (if Class E framing applied later)**:
- `mond-hoop-stress.md` §4.5 — Class E framing on the cross-scale table; estimated +10 lines
- `vol_1_foundations/chapters/04_continuum_electrodynamics.tex` (LaTeX mirror) — same; estimated +10 lines
- DAMA derivative observable note (skill discipline: DAMA $E_{slew} = \alpha m_e c^2$ has the 2π CANCEL per honest-scope walk-back; NOT an independent instance of the motif) — verify Class E doesn't accidentally re-promote DAMA to motif-instance status
- `research/2026-05-17_hoop-stress-2pi-step-4-result.md` — postscript on Class E status vs Class B
- `manuscript/predictions.yaml` — possibly new entry for cross-scale motif (currently no entry); estimated +1 new entry

**Recommended Grant adjudication priority**: MEDIUM — the motif itself is more Class B than Class E; the cross-scale shared-parameter inheritance via $u_0^*$ is interesting but secondary to the operating-point structure directly. Phase 2 already captured the Hoop-stress-projection-inheritance for MOND $a_0$ Anomaly 2/3.

---

### Candidate 4 — Three-route framework synthesis (Tier-1)

**Canonical source**: [`manuscript/frontmatter/00_foreword.tex:146-154`](../manuscript/frontmatter/00_foreword.tex) "The three-route framework commitment" + [`manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:13-17`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) §1.

**Current classification**: Phase 2 of this epic ALREADY refined this to Class E via the `omega-freeze-cosmic-grain-cascade.md:7` walk-back. NOT a new candidate — already-reclassified in Phase 2.

Listed here for completeness because the brief's Phase 3 spec mentions "the three-route framework $\alpha + G + \mathcal{J}_{\text{cosmic}}$" as a candidate. Resolution: this IS the H_∞ family + Ω_freeze (Phase 2 scope); not a separate candidate.

**Recommended Grant adjudication priority**: N/A — already-done in Phase 2.

---

### Candidate 5 — ν_vac = 2/7 cascade (10+ observable projections of a single substrate Poisson ratio)

**Canonical source**: per `closure-roadmap.md:162` (2026-05-17 night Foundation Item 13 entry — Vol 2 Ch 3 neutrino sector audit), ν_vac = 2/7 has confirmed ~14 distinct uses across Vols 2/3/5/6. Canonical leaves include:
- [`manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md) (canonical definition)
- `trace-reversal-mechanism.md` (independent Feng-Thorpe-Garboczi EMT derivation)
- `mode-counting-heat-capacity.md` (independent compliance-mode-counting derivation: d=2 transverse / n=7 compliance modes)
- `one-seventh-impedance-projection.md`
- `kolmogorov-spectral-cutoff.md` (38/21 avalanche exponent)
- `ave-compactness-limit.md` (Buchdahl 2GM/c²R < 2/7)
- `higgs-mechanism.md` (M_W/M_Z = √(7/9) → sin²θ_W = 2/9)
- `spontaneous-symmetry-breaking.md` (M_W = m_e/(8πα³√(3/7)))
- `pmns-eigenvalues.md` (neutrino sector PMNS predictions, 4-of-5 Class D verified per FI-13)
- `g-star-derivation.md` (g* = 7³/4 = 85.75)
- `scale-invariance-table.md` (α_s = α^(3/7))
- `membrane-phase-buffering.md` (water n_coop=9)
- `conclusion-death-of-numerology.md` (β_fold = ln(3)·3/7)
- `appendices/index.md` (protein backbone f=21.7 THz)

**Class E discriminator application**: SUBTLE — does NOT meet the strict Class E discriminator. ν_vac = 2/7 is a derived constant (from K4 amorphous-network EMT + compliance-mode-counting, TWO INDEPENDENT substrate-internal derivations); it's not an operating-point that can be tuned externally. Removing ν_vac would destroy the K4 substrate (the substrate IS the K4 graph at Poisson ratio 2/7 by construction), not destroy "N independent observables tied to one external parameter."

**Per skill v1.1 inverse failure mode**: this is closer to Class A identity (ν_vac IS the substrate definition) or Class B (axiom manifestation — each observable is one instance of "AVE recovers known result via 2/7 Poisson-ratio mechanism"). Each individual derivation routes through ν_vac as an INTERNAL substrate property, not through ν_vac as an EXTERNAL operating-point.

**Class E candidate-with-qualification**: ν_vac = 2/7 functions Class-E-LIKE in the sense that ~14 observables share the same internal substrate parameter, and falsifying any one (e.g., a strong measurement of vacuum Poisson ratio ≠ 2/7 from a future direct test) would falsify the entire cascade. But the joint-constraint structure is different — there's no "operating-point" choice; it's a derived ratio from K4 topology.

**Cascade-implication scope (if Class E refinement applied later)**:
- Would require explicit Grant adjudication on whether "derived substrate parameter shared across N observables" qualifies as Class E or is a separate class (Class F? Class B-cluster?)
- Per skill v1.1 §"Next probe due (2026-08-17)": this is the strongest candidate for "sub-class within Class E or new class altogether" — distinct from cosmic-genesis operating-point (Class E proper) and boundary-observable cascade (Class E sub-type).

**Recommended Grant adjudication priority**: HIGH but BLOCKING on skill methodology question. Should not be inventoried as a Class E candidate without methodological-class adjudication first.

---

### Candidate 6 — Universal saturation-kernel A-034 catalog (19-instance / 21-OOM)

**Canonical source**: [`manuscript/ave-kb/common/mathematical-closure.md:94-112`](../manuscript/ave-kb/common/mathematical-closure.md) §"A-034: Universal Saturation-Kernel Empirical Anchors" + [`manuscript/backmatter/07_universal_saturation_kernel.tex`](../manuscript/backmatter/07_universal_saturation_kernel.tex) (full 21-instance catalog).

**Current classification**: Class B axiom_manifestation (per `predictions.yaml` entries P43, P_A034_solar_flare, P_A034_bh_ringdown, P_A034_schwarzschild — all type `axiom_manifestation` except P_A034_bh_ringdown which is `derived_prediction` and P_A034_schwarzschild which is `identity`).

The kernel $S(A) = \sqrt{1 - A^2}$ governs:
- Condensed-matter: BCS B_c(T) — 0.00% (Vol 3 Ch 9)
- Solar/Geophysical: solar flare LED-avalanche — within data scatter
- Gravitational: BH ring-down QNM ω_R M_g = 18/49 — 1.7% (Vol 3 Ch 15)
- Cosmological: Schwarzschild radius — exact (Vol 3 Ch 15/20)
+ 17 more instances per full catalog

**Class E discriminator application**: SUBTLE — the kernel is Class B (one axiom expressed at many scales) by canonical definition; the joint-constraint structure is "all instances must use the SAME $\sqrt{1-A^2}$ functional form without per-scale parameter retuning" rather than "all instances tied to ONE numerical operating-point."

**Class E sub-candidate consideration**: per skill v1.1 §"Next probe due — saturation-kernel scale-instance" possibility. The kernel-invariance constraint is structurally similar to the operating-point constraint (failure of any one scale-instance to match the kernel would falsify Axiom 4 universally); but the constraint is on FUNCTIONAL FORM not NUMERICAL VALUE.

**Per skill v1.1 inverse failure mode**: each kernel application's match to data is Class C (alternative-mechanism-recovers-standard-result) or Class B (axiom manifestation) depending on whether the comparison is to a CODATA-derived target or to a measured observable directly. The 21-OOM cross-scale "same kernel" claim is a meta-statement about Axiom 4, not a Class E joint-constraint on N observables.

**Cascade-implication scope (if Class E refinement applied later)**: LOW — would primarily affect framing of the cross-scale-kernel-invariance language as "Class E-class joint-constraint on functional-form across N scale-instances" rather than substantive observable reclassification. Estimated 2-3 leaves touched.

**Recommended Grant adjudication priority**: LOW — Class B is the more natural fit; Class E framing would require methodology extension to cover "shared functional-form-across-scales" as a distinct joint-constraint type.

---

### Candidate 7 — α + δ_strain CMB thermal-running cascade

**Canonical source**: [`manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md:24`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md) — δ_strain ≈ 2.225 × 10⁻⁶ bridges cold-α prediction to CODATA + [`manuscript/predictions.yaml` P47](../manuscript/predictions.yaml).

**Current classification**: P47 type `derived_prediction` (definitional once δ_strain is named the residual between ALPHA_COLD_INV and CODATA ALPHA).

**Class E discriminator application**: WEAK candidate. δ_strain is a single residual constant, not N observables tied to one operating-point. Per `predictions.yaml` P47 notes:
> *"δ_strain is defined by the relation, so predicted == observed by construction — the substantive claim is that the *residual between Ch 8's cold α prediction and CODATA* has this magnitude, not that the formula fits."*

This is closer to Class A (identity-by-definition) than Class E.

**Cross-cascade question**: per `cosmological-constant-closure.md:7`, δ_strain "is currently empirically calibrated at $T_{\text{CMB}}$ pending first-principles derivation, inherited via $\alpha$ closure" — i.e., δ_strain has a pending first-principles derivation route. If that route lands and δ_strain becomes a derived prediction (Class D), it could THEN be considered for Class E if it shares an operating-point with other observables. Currently: NOT a Class E candidate.

**Recommended Grant adjudication priority**: VERY LOW — not a Class E candidate in current corpus state. Re-evaluate post-δ_strain first-principles derivation.

---

### Candidate 8 — PMNS matrix neutrino sector (4-of-5 Class D verified, 1-of-5 conditional)

**Canonical source**: per `closure-roadmap.md:162` Foundation Item 13 — Vol 2 Ch 3 neutrino sector + `manuscript/predictions.yaml` P29_32.

**Current classification**: P29_32 type `derived_prediction` (Class D per consistency-vs-emergence v1.0 audit per FI-13 2026-05-17 night, with 4-of-5 PMNS predictions verified Class D EMERGENCE and sin²θ_13 Class D CONDITIONAL on c_1=5 derivation gap).

**Class E discriminator application**: WEAK-MODERATE candidate. The 5 PMNS predictions (sin²θ_12, sin²θ_23, sin²θ_13, δ_CP/π, m_i ∝ 1/c_i²) DO share substrate parameters (ν_vac = 2/7 + mode-space c-ladder {5,7,9}) — meeting the "N observables share substrate parameter" Class E pattern.

But: the substrate parameters here are derived properties (ν_vac per K4 EMT; c-ladder per torus knot mode-space), not "an operating point" in the H_∞ family sense (where $u_0^* \approx 0.187$ has a specific empirical pin at $\alpha$ via Golden Torus closure). The PMNS predictions don't ride on a single tunable parameter — they ride on TWO derived constants.

**Per skill v1.1 inverse failure mode**: similar to ν_vac = 2/7 cascade (Candidate 5) — derived-substrate-parameter cascade rather than operating-point projection.

**Cascade-implication scope**: if reclassified to Class E, would join Candidate 5 (ν_vac cascade) as a methodologically-open question class.

**Recommended Grant adjudication priority**: MEDIUM — should be adjudicated alongside Candidate 5 (ν_vac cascade) for the methodology question.

---

### Candidate 9 — BH boundary observables (M, Q, J in Kerr-Newman framing)

**Canonical source**: [`manuscript/ave-kb/common/boundary-observables-m-q-j.md`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md) row "Black-hole event horizon" + `manuscript/predictions.yaml` P_A034_bh_ringdown + P_A034_schwarzschild.

**Current classification**: split — Schwarzschild radius is `identity` (Class A); BH ring-down QNM is `derived_prediction` (Class D); the full M/Q/J Kerr-Newman set has no unified predictions.yaml entry.

**Class E discriminator application**: STRONG sub-instance of Candidate 1 (the M/Q/J cross-scale boundary-observable structure). The BH scale-instance is one of the 6 scales listed in `boundary-observables-m-q-j.md` §"Same mechanism at all scales".

**Recommended Grant adjudication priority**: should be subsumed under Candidate 1 adjudication.

---

### Candidate 10 — Spin-statistics + chirality + matter asymmetry (lattice-genesis joint)

**Canonical source**: implicit across Vol 3 Ch 4 generative cosmology + Vol 2 Ch 10 baryon asymmetry derivation.

**Current classification**: P22 (Baryon asymmetry) `derived_prediction`; matter asymmetry direction (Observable 4 in omega-freeze) implicit Class E sub-component per Candidate 2.

**Class E discriminator application**: subsumed under Candidate 2 (Ω_freeze 8-observable cascade) — matter asymmetry IS Observable 4 of that cascade.

**Recommended Grant adjudication priority**: subsume under Candidate 2.

---

## §3 Summary table

| # | Candidate | Current class | Strict Class E candidate? | Cascade scope | Adjudication priority |
|---|---|---|---|---|---|
| 1 | M/Q/J at Γ=-1 boundaries (6-scale) | implicit Class C distributed | **YES (skill v1.1 explicitly names)** | 6-15 leaves + 8-15 yaml entries | **HIGH** |
| 2 | Ω_freeze 8 observables (Tier-2 framework) | A-034 prereg + distributed | **YES (joint axis constraint)** | 4-6 docs + 6-8 yaml + foreword | **HIGH** |
| 3 | Hoop-stress 2π cross-scale motif | implicit Class B | WEAK-MODERATE (more Class B than E) | 2-3 leaves | MEDIUM |
| 4 | Three-route framework α+G+𝒥 | ALREADY Class E (Phase 2) | N/A | N/A | done |
| 5 | ν_vac = 2/7 cascade (~14 observables) | distributed Class B/D | SUBTLE — derived-parameter cascade, not operating-point | 14+ leaves | **HIGH** but blocking on methodology question |
| 6 | A-034 saturation-kernel 21-OOM | Class B (axiom_manifestation) | WEAK (functional-form invariance, not numerical operating-point) | 2-3 leaves | LOW |
| 7 | α + δ_strain CMB thermal-running | derived_prediction (Class A-like) | WEAK (single observable, not N) | 0-1 leaves | VERY LOW |
| 8 | PMNS matrix (Vol 2 Ch 3) | derived_prediction (Class D) | WEAK-MODERATE — ν_vac+c-ladder derived parameters | bundle with #5 | MEDIUM |
| 9 | BH M/Q/J Kerr-Newman | split (identity + derived) | subsumed under #1 | bundle with #1 | (subsume) |
| 10 | Matter asymmetry + chirality + spin-statistics | derived + Observable-4 | subsumed under #2 | bundle with #2 | (subsume) |

**Distinct candidates count after subsumption**: 7 (Candidates 1, 2, 3, 5, 6, 7, 8).

**Strict Class E (per skill v1.1 discriminator)**: 2 (Candidates 1, 2).

**Methodology-question candidates** (Class E-LIKE but blocking on Grant adjudication of methodology extension): 2 (Candidates 5, 8).

**Class B (more natural fit)**: 2 (Candidates 3, 6).

**Not-Class-E**: 1 (Candidate 7).

---

## §4 Methodology questions surfaced for future Grant adjudication

Per the brief constraint (inventory-only, no reclassification), this section surfaces questions whose resolution would gate the per-candidate epics:

### Q1: Sub-class structure within Class E

Per skill v1.1 §"Next probe due (2026-08-17)": *"Probe whether Class E discriminator covers all operating-point-projection variants, OR if there are further sub-classes hiding within (boundary-observable cascade vs cosmic-genesis operating-point vs saturation-kernel scale-instance — three Class-E sub-types?)"*

This sweep surfaces THREE distinct flavors of "N observables share something":
- (a) Operating-point projection in the cosmic-genesis sense — N observables share ONE tunable substrate parameter ($u_0^*$ at cosmic genesis). **Canonical Class E.** Examples: H_∞ family (Phase 2 done), Ω_freeze 8-observable cascade (Candidate 2).
- (b) Boundary-observable cascade — N observables (M, Q, J) at every Γ=-1 saturation surface share the same boundary-integral structure across all 6 scales. **Class E "boundary-observable cascade" sub-type per skill v1.1 hint.** Example: Candidate 1.
- (c) Derived-substrate-parameter cascade — N observables share an internal substrate-derived constant (ν_vac = 2/7 from K4 EMT; c-ladder from torus-knot mode space). The constraint is "all N observables consistent with the same derived constant," NOT "all N observables tied to a single tunable parameter." **Methodology-question candidate; may be Class E sub-type or new class.** Examples: Candidate 5 (ν_vac), Candidate 8 (PMNS).

Question for Grant: are these three sub-types of Class E, or do (b)/(c) deserve distinct class labels (Class F / Class G)?

### Q2: Functional-form-invariance vs numerical-value-projection

Candidate 6 (A-034 saturation-kernel 21-OOM) is "same functional form $\sqrt{1-A^2}$ at every scale without parameter retuning" — a constraint on functional form. Is this Class E or Class B?

Question for Grant: does Class E cover only numerical-value joint-constraints, or does it cover functional-form invariance as well?

### Q3: Skill v1.1 inverse-failure-mode applicability

Per skill v1.1: *"a Class C observable miscategorized as Class E looks like 'we have a joint-constraint set' when the observable actually only depends on one CODATA-derived intermediate. The discriminator is: are there OTHER substrate observables constrained by the SAME parameter? If yes, Class E. If no, it's still Class C even if the language sounds joint."*

Application: most cascade-style observables in this corpus DO share substrate parameters with multiple other observables (the substrate is highly cross-cutting). Strict application of the inverse-failure-mode test would promote many corpus-wide "shared substrate parameter" claims to Class E.

Question for Grant: what's the threshold for "enough cross-observable sharing" to elevate to Class E? Is it (a) ≥ 2 observables, (b) ≥ 5, (c) ≥ N where N is determined by an empirical-discrimination cost-benefit?

---

## §5 Verdict summary (1 paragraph per brief return-spec)

Phase 3 inventory surfaces **7 distinct Class E candidate-classes after subsumption**, of which 2 (M/Q/J boundary observables across 6 scales; Ω_freeze 8-observable Tier-2 framework synthesis) are strict Class E candidates per the skill v1.1 discriminator and HIGH priority for future Grant-adjudicated reclassification epics. 2 candidates (ν_vac = 2/7 cascade, PMNS matrix) are Class-E-LIKE but block on a methodology-extension question (whether derived-substrate-parameter cascades count as Class E or warrant a distinct sub-class). 2 candidates (Hoop-stress 2π motif, A-034 saturation-kernel) fit Class B (axiom-manifestation) more naturally than Class E. 1 candidate (δ_strain CMB thermal-running) is NOT a Class E candidate in current corpus state. Per brief constraint, NO reclassification of any candidate is applied in this session; the inventory is the deliverable. Three methodology questions (Q1–Q3 in §4) are surfaced for future Grant adjudication and would gate the per-candidate epic sequencing. The skill v1.1 explicitly hints at sub-class structure within Class E (cosmic-genesis vs boundary-observable cascade vs saturation-kernel scale-instance) — this inventory's distinct candidate-class enumeration is structurally consistent with that three-sub-type hypothesis and provides corpus-grounded examples for each.

---

## §6 Citation verification (`verify-before-cite` v1.3)

Every file:line citation in this doc verified at `analysis/h-infinity-downstream-cascade` tip post-Phase-2 (commit f6eec27):

- `manuscript/ave-kb/common/boundary-observables-m-q-j.md` (§"Same mechanism at all scales" lines 31-40) — verified verbatim
- `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:46-58` (§3 Eight testable observables) — verified verbatim post-Phase-1 edit
- `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md` §"Cross-volume substrate motif" (lines 43-71) — verified verbatim post-Phase-2 edit
- `manuscript/ave-kb/common/closure-roadmap.md:162` (Foundation Item 13 ν_vac cascade entry) — verified verbatim
- `manuscript/ave-kb/common/mathematical-closure.md:94-112` (§A-034 saturation-kernel anchors) — verified verbatim
- `manuscript/predictions.yaml` P02/P03/P04/P05/P06/P07/P23/P29_32/P43/P47 + P_A034_* entries — verified verbatim
- skills repo commit `470f1ec` (consistency-vs-emergence v1.1 canonization) — verified via `git -C ~/.claude/skills log -1 -- consistency-vs-emergence/SKILL.md`

Inventory complete. Branch ready for Phase 4 audit.
