# Baseline Adversarial Review — α and Gravity

**Reviewer:** mad-participant-1 (baseline; pre-boundaries-mechanism)
**Date:** 2026-05-02
**Topic:** Does AVE correctly handle α invariance under gravity, or are there issues?

## Methodology Note

This baseline review proceeds in two passes per finding. Pass 1: form the finding from summary text only (entry-point.md, CLAUDE.md, vol1/index.md, vol3/index.md, vol3/gravity/index.md, vol3/gravity/ch01-gravity-yield/index.md, vol3/gravity/ch02-general-relativity/index.md, vol3/gravity/ch03-macroscopic-relativity/index.md). Pass 2: consult the most relevant leaf and record whether the finding would be retracted, revised, or stand. The "stand / revise / retract" verdict is the load-bearing measurement.

The reviewer adopts an adversarial physics-literate stance: the kind of reader most likely to file a critical objection. Recurring background knowledge assumed: (a) cosmological quasar-absorption studies (Webb, King, Murphy, etc.) constrain Δα/α at ≲10⁻⁵; (b) atomic-clock comparisons across gravitational potentials (Sr/Yb/Hg, Cs fountains) constrain dα/dΦ at ~10⁻⁷ per unit dimensionless potential or better; (c) Equivalence Principle violation tests (MICROSCOPE, Eot-Wash) place stringent limits on species-dependent gravitational coupling, which would arise from differential α-variation across atomic species.

---

## Findings

### Finding 1 — Summary text never states α's stance under gravity

- **Severity:** high
- **Source of finding:** summary text only
- **Claim being challenged:** The summary text in entry-point.md, vol1/index.md, vol3/index.md, vol3/gravity/index.md, and the ch01/ch02/ch03 indexes nowhere asserts (or denies) that α is invariant under gravitational potential.
- **Issue:** The framework presents α with two correction regimes — a "cold-lattice" geometric value α⁻¹_ideal = 4π³ + π² + π and a "thermal scalar δ_strain at T_CMB" — explicitly tying α to lattice strain. It also describes gravity as inducing radial strain ε₁₁(r) = 7GM/(c²r) and as locally altering ε_eff and μ_eff. By the framework's own logic, gravitational strain should produce a δ_strain analogous to the thermal one, predicting Δα/α ≠ 0 in gravity wells. The summary text never addresses this implication. An adversarial reviewer would file: *the framework either tacitly predicts a gravitational α-variation in conflict with quasar-absorption and atomic-clock bounds, or it owes an explicit mechanism for why gravitational strain is special.*
- **Files consulted to form this finding:** entry-point.md; vol1/index.md; vol3/index.md; vol3/gravity/index.md; vol3/gravity/ch01-gravity-yield/index.md; vol3/gravity/ch03-macroscopic-relativity/index.md
- **Pass-2 leaf consultation:** transverse-refractive-index.md and optical-refraction-gravity.md confirm the framework derives radial strain ε₁₁(r) = 7GM/(c²r) and uses ν_vac = 2/7 to produce a transverse refractive index, but neither leaf explicitly resolves whether the lattice strain that bridges cold-α to CODATA-α also operates in gravity wells. **Verdict: STANDS.** The leaves do not address the question; the finding is not retracted.

### Finding 2 — Achromatic Impedance Matching summary asserts Z₀ invariance but leaves α implicit

- **Severity:** high
- **Source of finding:** summary text only
- **Claim being challenged:** vol3/gravity/index.md and vol3/gravity/ch03-macroscopic-relativity/index.md list "Achromatic Impedance Matching: Z₀' = Z₀ ≈ 376.73 Ω" as a key result, paired with "Refractive Index of Gravity: n(r) = 1 + 2GM/(c²r)".
- **Issue:** Z₀ = √(μ_eff/ε_eff). For Z₀ to remain invariant while n = √(μ_eff·ε_eff)/√(μ₀ε₀) varies with r, both μ_eff and ε_eff must scale by the same factor n. But α = e²/(4πε₀ℏc) — if ε_local = n·ε₀ and c_local = c/n, then α_local = e²/(4π·nε₀·ℏ·(c/n)) = α only if e and ℏ are themselves treated as gravity-invariant. The summary text never says any of this. A reviewer who notices the Z₀ invariance claim has done half the algebra; one who hasn't been led through the cancellation will reasonably suspect α drifts with n(r).
- **Files consulted to form this finding:** vol3/gravity/index.md; vol3/gravity/ch03-macroscopic-relativity/index.md
- **Pass-2 leaf consultation:** achromatic-impedance-matching.md states explicitly μ' = n(r)μ₀ and ε' = n(r)ε₀ and derives Z₀' = Z₀. It does **not** carry the algebra forward to α. The leaf strengthens (does not weaken) the finding's premise but still does not state the α-invariance conclusion. **Verdict: REVISED but STANDS.** A revised version of the finding would say: "the leaves show that the framework's own constitutive scaling makes α algebraically invariant in lossless transverse propagation, but neither summary nor leaf says so explicitly, and the result is not displayed as a Key Result."

### Finding 3 — Multi-species Δα/α not addressed anywhere in summary text

- **Severity:** high
- **Source of finding:** summary text only
- **Claim being challenged:** The known empirical landscape includes multi-species Δα/α measurements (atomic-clock comparisons across gravitational potentials between two transitions of different sensitivity coefficients; quasar absorption-line many-multiplet studies). A framework that derives α from geometry should be able to state whether it predicts species-dependent fractional shifts.
- **Issue:** No summary in scope mentions multi-species comparisons, sensitivity coefficients, or species-independent universality. A reader looking for AVE's stance on this empirically-active topic finds no entry point, even in vol3/gravity, where one would expect it to live.
- **Files consulted to form this finding:** all summary files in scope
- **Pass-2 leaf consultation:** Not consulted (the topic asks specifically about summary-text-formed findings). However, given that none of the consulted leaves (transverse-refractive-index.md, refractive-index-of-gravity.md, achromatic-impedance-matching.md, optical-refraction-gravity.md) mentions species-dependent α at all, the finding likely stands even after leaf consultation. **Verdict: STANDS (provisional, leaf not consulted).** Note: this is the kind of finding that a sidecar/boundary mechanism could resolve trivially by stating "AVE predicts α invariant across species in lossless transverse-wave regimes" — its persistence in baseline reflects exactly the absence of such a claim-boundary.

### Finding 4 — "Cold-lattice α with thermal correction" framing invites unbounded extension to gravitational strain

- **Severity:** high
- **Source of finding:** summary text only
- **Claim being challenged:** entry-point.md asserts α⁻¹_ideal = 4π³ + π² + π (cold) with δ_strain at T_CMB bridging to CODATA. vol1/index.md duplicates this ("CMB-Strain α Correction").
- **Issue:** The summary explicitly establishes the *type* of correction — lattice strain — and applies it once (thermal at T_CMB). It does not establish that thermal strain is the *only* admissible contributor to δ_strain. By construction, a reader applying the framework's stated mechanism should expect any other source of lattice strain (gravitational, mechanical, electromagnetic vacuum-polarization in dense field regions) to contribute additional δ-terms. The framework summary opens this door without closing it.
- **Files consulted to form this finding:** entry-point.md; vol1/index.md
- **Pass-2 leaf consultation:** Not consulted at the cold-lattice-α leaves (vol1 ch.8) since out of stated optional scope. **Verdict: STANDS (provisional).** Resolution would require the framework to commit to a closed enumeration of δ_strain contributors.

### Finding 5 — vol3/gravity has no sub-domain index for "constants invariance" or "α under gravity"

- **Severity:** medium
- **Source of finding:** summary text only
- **Claim being challenged:** vol3/gravity/index.md lists subdomains ch01 (gravity-yield), ch02 (GR), ch03 (optical metric), ch08 (GW). None is dedicated to fundamental-constant variation under gravity.
- **Issue:** Given the framework's first-principles geometric derivation of α and its ambition to address "all physical observables", the absence of a dedicated chapter, subsection, or even a Key Result line addressing constant invariance under gravity is itself a structural gap. An adversarial reviewer would log: "either the framework treats this as so trivial it needs no entry, or it has not been worked through."
- **Files consulted to form this finding:** vol3/gravity/index.md
- **Pass-2 leaf consultation:** N/A (this finding is about structural absence, not a content claim). **Verdict: STANDS.**

### Finding 6 — "c_local = c/n" claim in summary chain creates direct conflict surface with α

- **Severity:** high
- **Source of finding:** summary text only (with confirmation from one consulted leaf)
- **Claim being challenged:** vol3/gravity/index.md and vol3/gravity/ch03-macroscopic-relativity/index.md present "Refractive Index of Gravity: n(r) = 1 + 2GM/(c²r)" as a Key Result. By optical-refraction interpretation, this implies c_local = c/n.
- **Issue:** If c_local varies, then α = e²/(4πε₀ℏc) — which uses c — must either (a) use c_local (in which case α varies), (b) use c_∞ (a global constant — but then which c appears in atomic-physics local measurements?), or (c) be defined as a dimensionless invariant by a separate algebraic mechanism. The summary text does not select among (a)/(b)/(c). A reader is left to infer.
- **Files consulted to form this finding:** vol3/gravity/index.md; vol3/gravity/ch03-macroscopic-relativity/index.md (summary); refractive-index-of-gravity.md (leaf — consulted)
- **Pass-2 leaf consultation:** refractive-index-of-gravity.md explicitly states "c_local = c₀/n" and discusses c_max in intergalactic voids. The leaf takes a position (c is not constant across gravity wells, and this is described as a falsifiable prediction with magnitude ~3,600 m/s of gradient between Earth and intergalactic voids). The leaf does not address whether α tracks c_local or stays geometrically locked. **Verdict: REVISED and STANDS, possibly STRENGTHENED.** The leaf actually commits the framework to a varying c, which sharpens (not softens) the question of whether α varies — the adversarial finding becomes more pointed, not less.

### Finding 7 — CLAUDE.md INVARIANT-S2 fixes α via Axiom 2 but does not state gravitational behavior

- **Severity:** medium
- **Source of finding:** summary text only
- **Claim being challenged:** CLAUDE.md INVARIANT-S2 lists "Axiom 2: Fine Structure — α = e²/(4πε₀ℏc); V_yield = √α · m_e c²/e ≈ 43.65 kV" as the canonical axiom for α.
- **Issue:** This is the only place in the cross-cutting invariants document where α appears as a definitional axiom. It is presented as a constant. There is no qualification that V_yield (which depends on √α) should be treated as gravity-invariant or as varying with local n(r). For a cross-cutting invariants file, this is exactly where a single-line statement like "α is geometrically locked; gravitational strain does not modify α" would belong. Its absence is structurally significant.
- **Files consulted to form this finding:** CLAUDE.md
- **Pass-2 leaf consultation:** N/A — CLAUDE.md is itself the cross-cutting reference; there is no underlying leaf for it. **Verdict: STANDS.**

### Finding 8 — Pitfall #5 in LIVING_REFERENCE.md is referenced by the topic but no in-scope summary surfaces this guidance

- **Severity:** medium (about the KB's surfacing of its own caveats, not about the physics)
- **Source of finding:** summary text only
- **Claim being challenged:** The topic brief states "LIVING_REFERENCE.md 'Common Pitfalls' #5 documents that summary text in this area has caused recurring reader confusion." None of the in-scope summary files (entry-point, CLAUDE.md, vol1/index.md, vol3/index.md, vol3/gravity/index.md, ch01/ch02/ch03 indexes) link to or surface this pitfall.
- **Issue:** A self-aware KB that knows a particular summary region causes recurring reader confusion should either (a) surface the warning at the index level, (b) annotate the load-bearing summary lines, or (c) provide a sidecar disclaimer. Baseline state: it does none of these in scope.
- **Files consulted to form this finding:** all summary files in scope
- **Pass-2 leaf consultation:** N/A. **Verdict: STANDS.** This is the kind of meta-finding the boundaries mechanism is designed to address.

### Finding 9 — vol1 Key Results table presents H_∞ formula assuming α-invariance globally without saying so

- **Severity:** medium
- **Source of finding:** summary text only
- **Claim being challenged:** vol1/index.md lists "H_∞ = 28π m_e³ c G / (ℏ² α²) ≈ 69.32 km/s/Mpc" as a Key Result. This is a numerical prediction that requires α to be a single global constant in the formula.
- **Issue:** The formula uses α² as a multiplicative scalar in the cosmic-horizon consistency relation. If α varies across the universe by gravitational potential (a possibility the framework's own thermal-correction logic does not exclude), then which α appears here? A cold-lattice α? A volume-averaged CODATA α? The framework summary uses the CODATA value (137.036) implicitly. The summary does not call out which α-value is the correct one to use in cosmological predictions, and does not tie the choice to a derivation of why other values would be wrong.
- **Files consulted to form this finding:** entry-point.md; vol1/index.md; vol3/gravity/ch01-gravity-yield/index.md
- **Pass-2 leaf consultation:** optical-refraction-gravity.md uses CODATA α ≈ 1/137.036 in the dimensionless-scale-of-universe calculation. The leaf does not justify this choice over the cold-lattice value. **Verdict: REVISED and STANDS.** The finding sharpens to: "the framework uses CODATA α in its cosmological predictions, but the summary does not state whether the correct value is the cold-lattice asymptote, the CMB-corrected CODATA value, or some r-averaged value, and the consequences of the choice for the H_∞ prediction are not estimated."

---

## Summary Counts

- **Total findings:** 9
- **Findings formed from summary text only:** 9 (all)
- **Findings that would be retracted after consulting the cited leaf:** 0
- **Findings that would be revised after consulting the cited leaf:** 3 (Findings 2, 6, 9 — sharpened or qualified, but not retracted)
- **Findings that stand unchanged after consulting the cited leaf:** 4 (Findings 1, 5, 7, 8)
- **Findings where leaf was not consulted (provisional stand):** 2 (Findings 3, 4)

**Headline:** K = 0 retractions out of 9 summary-only findings. Three revisions are *sharpenings*, not weakenings — i.e., the leaves either confirm the premise or commit the framework more strongly to a position the adversarial reviewer was challenging. None of the leaves consulted explicitly assert α invariance under gravitational potential, and none addresses the species-independence question. The baseline measurement is therefore: an adversarial physics-literate reviewer can file ~9 findings against the α-and-gravity surface area of the AVE KB from summary text alone, and consulting the cited leaves does not retract any of them.
