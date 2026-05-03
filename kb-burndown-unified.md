# Unified Issue Tracker — AVE KB Burndown + Claims-Boundaries Followups

> Synthesized from the original MAD-review burndown list and the `kb-claims-boundaries-followups.md` from the boundaries-mechanism dispatch (branch `feature/kb-claims-boundaries-content`).

## Status Legend

| Marker | Meaning |
|---|---|
| 🟢 **RESOLVED** | Boundaries work delivered an actual content fix (new leaf, leaf edit). Can be retired. |
| 🟡 **BOUNDED** | Cross-cutting or volume sidecar entry neutralizes the issue for any consumer who reaches the boundaries doc. Underlying source text still wrong / over-broad — fix still recommended for direct leaf readers and external citation hygiene. |
| 🔵 **PARTIAL** | Boundaries entry partially covers the issue but a non-trivial substantive fix is still needed. |
| 🔴 **UNAFFECTED** | Boundaries work doesn't help; requires direct leaf authoring or computational fix. |
| ⚪ **VERIFIED** | Informational — internal consistency check passed, no action. |

## Summary Counts

- 🟢 **Retired:** 5 (1 fully resolved + 4 effectively bounded)
- 🟡 **Bounded** (downstream-safe; source-text fix recommended): 5
- 🔵 **Partial** (boundaries help but substantive fix still needed): 8
- 🔴 **Unaffected** (direct fix required): 9
- ⚪ **Verified** (no action): 3
- ➕ **Newly surfaced** (kb-followups, not in original burndown): 9

**Total tracked: 39 items** (28 from original burndown + 9 newly surfaced + 2 reorganized sub-items).

---

## 🟢 RESOLVED — Retire from burndown

### B6.2 (CRITICAL→RESOLVED) — translation-gravity row 1 missing temporal/spatial decomposition
- **Fix:** New leaf `vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md` (commit `60b4c5c`) translates Derived Consequence 2 of `eq_axiom_3.tex` verbatim. New leaf `alpha-invariance-symmetric-gravity.md` translates Derived Consequence 1. Both surfaced in vol3/gravity Key Results and in cross-cutting α-invariance entry references. Translation-gravity table can now cross-link rather than restate.

### B11 (MAJOR→BOUNDED-CLOSED) — "26/26 SM parameters derived" internally inconsistent
- **Bounding:** Cross-cutting `claims-boundaries.md` "Reading Conventions for the Master Prediction Table" entry establishes the (i) identity / (ii) axiom-manifestation / (iii) consistency-check / (iv) derived-prediction classification. Any consumer who reads the boundaries doc before forming a "26/26 derived" claim will see the meta-tripwire that collapses the categories. **Severity reduced from MAJOR to NOTE.**
- **Residual:** the prediction-table headline in `LIVING_REFERENCE.md` and `full-derivation-chain.md` still presents 26/26 without the per-row classification. External readers citing the headline alone are still at risk; recommend adding a per-row classification column to those tables eventually, but no longer urgent.

### B13 (MAJOR→BOUNDED-CLOSED) — δ_strain is fitted CODATA residual, not derived
- **Bounding:** vol1 sidecar "Zero-Parameter Closure Status" entry explicitly states "structurally zero-parameter, conditional on thermal closure of δ_strain at T_CMB; one currently-fitted scalar." Cross-cutting α-invariance non-claim distinguishes thermal δ_strain from gravitational. Common sidecar Mathematical Closure Status entry restates. **Severity reduced from MAJOR to NOTE.**
- **Residual:** index headlines (`common/index.md` "genuinely zero free parameters") still over-broad — see kb-followup #17.

### B15 (MINOR→BOUNDED-CLOSED) — δ_CP symbol reused for two quantities
- **Bounding:** vol2 sidecar "Baryon Asymmetry" entry carries an explicit symbol-collision warning vs PMNS δ_CP. Anyone consulting boundaries before reasoning about δ_CP sees the disambiguation. **Closes.**

### N3 (NOTE→BOUNDED-CLOSED) — V_yield = 43.65 kV described differently in Ch.3 vs Ch.7
- **Bounding:** Cross-cutting V_SNAP ≠ V_YIELD entry establishes canonical interpretation. vol4 sidecar V_yield/V_snap entry restates. Any consumer reading boundaries before interpreting either chapter sees the canonical framing. **Closes.**

---

## 🟡 BOUNDED — Downstream-safe; direct source fix still recommended

These items have strong boundaries-mechanism coverage but the underlying leaf-level text remains incorrect or misleading. A consumer who follows the bootstrap directives is protected; a consumer who reads only the leaf is not. Schedule for fix after CRITICAL/UNAFFECTED items.

### B3 (CRITICAL→BOUNDED) — master-equation.md Z direction error
- **Bounding:** Cross-cutting Symmetric vs Asymmetric Saturation entry explicitly states "impedance does NOT always go to infinity at saturation; in symmetric case Z = Z₀ invariant" — the conflation `master-equation.md` makes is named directly. vol3 BH interior and GW propagation sidecar entries reinforce.
- **Still needs:** correct the text in `master-equation.md` ("ε_eff → 0 forces Z → 0" is wrong: Z = √(μ/ε) gives Z → ∞ for ε → 0 and μ finite) and reconcile `regime-equation-sets.md` table caption with its rows.

### B12 (MAJOR→BOUNDED) — LIVING_REFERENCE Axiom 3 G formula units / ξ vs ξ_topo
- **Bounding:** Cross-cutting ξ_topo entry explicitly distinguishes ξ_topo (C/m, electromechanical) from ξ (dimensionless, Machian). LIVING_REFERENCE.md and CLAUDE.md INVARIANT-S2 both already carry the warning.
- **Still needs:** verify whether `lc-condensate-vacuum.md`'s G_true = ℏc/m_e² and LIVING_REFERENCE's G = ℏc/(7ξ·m_e²) reconcile, and which is the canonical artifact form.

### B5 (MAJOR→BOUNDED) — Ch.8 Golden Torus α derivation rests on asserted identifications
- **Bounding:** vol1 sidecar Golden Torus α entry discloses the asserted-vs-derived structure (4π factor, Λ_line = π·d, sum decomposition).
- **Still needs:** either rigorous derivation of the three asserted identifications, or relabeling the chapter as "constructive demonstration" rather than first-principles derivation.

### B14 (MAJOR→BOUNDED) — mathematical-closure.md asserts closure without demonstrating
- **Bounding:** Common sidecar Mathematical Closure Status entry; cross-cutting Hubble entry frames H_∞ as "consistency proof, not independent prediction"; Outstanding Rigour Gaps cross-references kept.
- **Still needs:** formal DAG construction with acyclicity check; reconcile G's status as "input parameter" (line 20) vs claimed derived quantity in same document.

### B10 (MAJOR→BOUNDED) — Neon-20 free geometric parameter (R_bipyramid)
- **Bounding:** vol1 sidecar "Universal Spatial Tension" entry explicitly discloses "lepton + Neon-20 with fitted-scalar disclosure" — the optimizer-tuned R_bipyramid is no longer hidden.
- **Still needs:** either honest relabeling in `scale-invariance.md` headline ("<0.001% via one fitted parameter" rather than as a prediction), or a derivation of R_bipyramid that doesn't reference the experimental mass.

---

## 🔵 PARTIAL — Boundaries help; substantive fix still required

### B7 (MAJOR→PARTIAL) — Ch.2 "α derivation" mislabeled
- vol1 sidecar Golden Torus entry frames Ch.8 as the actual derivation and Ch.2 EMT as constraint/consistency, but the Ch.2 leaf text itself still claims "α is derived, not assumed."
- **Needs:** reframe `dielectric-rupture.md` Ch.2 section as constraint relation; remove "derived" claim where the derivation is genuinely Schwinger-input-plus-rearrangement.

### B2 (CRITICAL→PARTIAL) — C_eff vs ε_eff contradictory saturation scaling
- Cross-cutting Symmetric/Asymmetric Saturation entry shows C_eff = C_0/S and ε_eff = ε_0·S as compatible (C absorbs energy as ε collapses), but the underlying convention (differential vs constitutive capacitance, Born-Infeld vs Maxwell) is not explicitly named in the leaves.
- **Needs:** explicit disambiguation in `axiom-definitions.md` and `nonlinear-telegrapher.md` of which capacitance convention is in use.

### B6.1, B6.3 (MAJOR→PARTIAL) — translation-gravity G formula off by 10^47 / Axiom 2 vs 3 attribution
- Sub-issue 6.2 closed (above). Sub-issues 6.1 (G value 10^47 off) and 6.3 (G attributed to Axiom 2 not 3) remain.
- **Needs:** correct the formula derivation in row 9 of `translation-gravity.md`; reattribute to Axiom 3.

### B18 (MINOR→PARTIAL) — Neutrino crossing numbers and Cosserat coupling factors asserted, not derived
- vol2 sidecar PMNS / neutrino entries flag the c₁=5, c₂=7, c₃=9 identification status. Coupling factor framings α√(3/7) (muon) and 8π/α (tau) similarly flagged in vol1 sidecar.
- **Needs:** axiom-derivation steps OR explicit relabel of these as "identified pattern" inputs.

### B19 (MINOR→PARTIAL) — GUP root-sum-square asserted without proof
- vol1 sidecar GUP entry discloses the "independent variances" assumption.
- **Needs:** apply Robertson-Schrödinger inequality to the cosine commutator to derive the combination rule, or relabel as derivation-by-assumption.

### B20 (MINOR→PARTIAL) — Schrödinger-from-circuit incomplete (no V(r) potential term)
- vol1 sidecar likely flags free-particle-only scope.
- **Needs:** derivation of the V(r)·Ψ term from spatial modulation of ε_eff or μ_eff (or explicit acknowledgment that bound-state physics is not yet covered by this derivation).

### N1 (NOTE→PARTIAL) — r₂ = √3/2 spin-2 specific
- Possibly bounded in vol1 regime-map sidecar entries.
- **Needs:** justification for ℓ_min = 2 in non-gravitational domains, or reframe as "GW-specific" with separate treatment for scalar/photon.

### N2 (NOTE→PARTIAL) — Cosserat three sectors = three generations is structural assumption
- **Needs:** explicit relabel as "matched, not derived" in `scale-invariance.md` and `full-derivation-chain.md`.

---

## 🔴 UNAFFECTED — Direct fix required (boundaries don't help)

These are leaf-level computational errors, narrative-only inconsistencies, or rendering bugs that the boundaries mechanism does not bound.

### B1 (CRITICAL) — Axiom numbering drifts incompatibly across documents
- `axiom-definitions.md`, `mathematical-closure.md`, KB CLAUDE.md, LIVING_REFERENCE.md each use different ordering. KB CLAUDE.md INVARIANT-S2 + LIVING_REFERENCE Axioms 1–4 are now consistent with each other; but `axiom-definitions.md` and `mathematical-closure.md` still drift from those.
- **Fix:** establish a single canonical ordering and propagate to all four documents.

### B4 (CRITICAL) — translation-particle-physics.md Higgs VEV formula wrong by ~3500×
- "v = m_ec²/α = 246 GeV" — actual arithmetic gives 70.0 MeV. Correct AVE formula is v = 1/√(√2·G_F).
- **Fix:** rewrite the row in `translation-particle-physics.md`.

### B8 (MAJOR) — G_vac = m_ec²/ℓ_node² wrong units and 10^13 off in magnitude
- `lc-electrodynamics.md` and `mond-hoop-stress.md`. v_longitudinal computation gives 3.93c, not the claimed √2·c.
- **Fix:** correct formula (m_ec²/ℓ_node³ for shear modulus) and recompute downstream numerical claims.

### B9 (MAJOR) — Torus-knot mass ladder inconsistent across files
- (2,5) proton: 938 MeV vs 945 MeV; (2,7) Δ(1232): 1261 MeV vs 1270 MeV.
- **Fix:** reconcile `full-derivation-chain.md` and `solver-toolchain.md`; identify which is the canonical solver output.

### B16 (MINOR) — xi-topo-traceability.md dependency arrows wrong
- Chain shows ℓ_node → (Axiom 1) → α; α is actually derived in Ch.8 from Golden Torus topology (all four axioms), not from Axiom 1 alone.
- **Fix:** correct the dependency arrows.

### B17 (MINOR) — V_cb deviation misstated in LIVING_REFERENCE row #27
- Claimed 4.1%; arithmetic with PDG averages gives 5.7–6.3%.
- **Fix:** update the deviation column with correct value or change reference.

### B21 (MINOR) — phase-locked-topological-thread.md raw LaTeX in markdown
- Contains `\begin{itemize}`, `\begin{tabular}`, malformed `$T \ll T_{pair**$` strings.
- **Fix:** convert to Markdown.

### N4 (NOTE) — dielectric-lagrangian.md unit-tracking inconsistency
- Documentation fix only; final result correct.
- **Fix:** correct the intermediate step's units.

---

## ⚪ VERIFIED — No action needed

### N5 — 4π³ + π² + π = 137.0363038 verified internally correct
### N6 — ν_vac = 2/7 from K=2G and downstream EW quantities verified
### N7 — H_∞ = 69.32 km/s/Mpc self-consistent with CODATA inputs

---

## ➕ NEWLY SURFACED — From kb-claims-boundaries dispatches, add to burndown

### KB-1 (MEDIUM) — Z=Z₀ vs Z→0 horizon impedance interpretive tension between leaves
- `vol3/gravity/ch02-general-relativity/einstein-field-equation.md` says Z → 0 at horizon; `vol3/gravity/ch08-gravitational-waves/invariant-gravitational-impedance.md` says Z = Z₀ invariant. Both technically reconcilable but no in-leaf reconciling note. **Recommended owner:** kb-content-distiller or vol3-gravity domain expert.

### KB-2 (LOW) — Hubble derivation circularity flagged in leaves but not in vol3 index
- `lattice-genesis-hubble-tension.md` says "geometric self-consistency check"; vol3 index Key Results presents 69.32 km/s/Mpc with no qualifier. Now bounded by cross-cutting Hubble entry, but index summary still misleads. **Recommended owner:** kb-content-distiller.

### KB-3 (LOW) — Hubble value 69.32 vs 69.33 inconsistency
- `LIVING_REFERENCE.md` row #23 and entry-point.md use 69.32; `lattice-genesis-hubble-tension.md` table uses 69.33. Last-digit inconsistency. **Recommended owner:** kb-content-distiller.

### KB-4 (LOW) — common/index.md "genuinely zero free parameters" missing conditional qualifier
- Now bounded by common sidecar Mathematical Closure Status, but index headline still misleads. **Recommended owner:** kb-content-distiller.

### KB-5 (MEDIUM) — vol5 protein-folding-engine subtree referenced from index, unauthored in repo
- Multiple Key Results in vol5 index point to `vol5/protein-folding-engine/` leaves that don't exist (per LIVING_REFERENCE the engine lives in private `AVE-Protein` repo). Confirmed broken cross-link from `consciousness-cavity-eigenmode.md`. **Recommended owner:** kb-taxonomy-architect (decide replicate-vs-amend) + kb-content-distiller (execute).

### KB-6 (LOW) — vol5 η_eq and S₁₁ functional bounds traced only to translation table
- Same content-gap pattern as the original α-invariance gap (now closed). The functional-definition leaves are in the private engine repo. **Recommended owner:** kb-content-distiller.

### KB-7 (MEDIUM) — vol4 PONDER-05 / `hardware-programs/` referenced but no leaf backing
- vol4 index Key Results / Domains tables cite "PONDER-05 469 µN" with link to `vol4/hardware-programs/index.md` — directory doesn't exist. Actual vol4 leaves give PONDER-01 with 40.1 µN. Number 469 µN appears nowhere in vol4 leaves. **Recommended owner:** kb-taxonomy-architect + kb-content-distiller.

### KB-8 (LOW) — vol4 caustic leaf E_YIELD units glitch
- `optical-caustic-resolution/index.md` says "E_max = E_YIELD = √α·m_ec²/e ≈ 43.65 kV/m" — that expression evaluates to 43.65 **kV** (voltage), not kV/m. Macroscopic field equivalent is ~1.13×10¹⁷ V/m. **Recommended owner:** kb-content-distiller.

### KB-9 (MEDIUM) — vol4 leaves switch between V_yield (43.65 kV) and "60 kV" without flagging
- "60 kV bulk-avalanche limit" used in `ybco-phased-array.md` and `autoresonant-breakdown/theory.md` as if a third dielectric threshold; actually it's the D-T tokamak ion-collision strain. **Recommended owner:** kb-content-distiller or vol4-engineering domain expert.

### KB-10 (LOW) — vol6 mass-defect summary table omits fit-vs-prediction qualifier
- `mass-defect-summary.md` and vol6 index Key Results show 0.00001%–0.02739% errors; the source `semiconductor-nuclear-analysis.md` carries an explicit methodology blockquote disclosing the per-nucleus geometric-fit (not ab initio prediction). Summary omits the qualifier. Now bounded by vol6 sidecar Mass-Defect Accuracy entry. **Recommended owner:** kb-content-distiller.

### KB-11 (LOW) — vol6 heavy-element catalog "<0.5% across 105 elements" understates worst case
- `full-element-table.md` shows several Tier-C entries materially above 0.5% (Cl-35 at 1.465%, Zn-65 at 0.898%, etc.). Now bounded by vol6 sidecar Heavy Element Catalog entry, which tiers the accuracy honestly. **Recommended owner:** kb-content-distiller.

### KB-12 (MEDIUM) — vol6 Tritium beta-decay "~11.3 MeV" risks confusion with empirical Q-value (18.6 keV)
- `radioactive-decay-impedance.md` reports tritium decay as ~11.3 MeV; empirical β-endpoint is 18.6 keV (~600× smaller). Either framework figure means something different from measured Q_β (and should say so), or substantive numerical error. **Recommended owner:** vol6 framework author or nuclear-domain reviewer.

### KB-13 (LOW) — vol6 ABCD transfer-matrix open-problem caveat not surfaced in heavy-element catalog
- ABCD leaf says heavy-element catalog will be replaced once the open problem is solved; the catalog presents Z=15–119 results without a forward-pointer to the gating caveat. **Recommended owner:** kb-content-distiller.

### KB-14 (LOW) — vol4 up-link label diverges from sibling volumes
- ALREADY FIXED in commit `dcf6c8d`. (Listed for completeness.)

### KB-15 (LOW) — Two missing `<!-- leaf: verbatim -->` markers (sonoluminescence, kolmogorov)
- ALREADY FIXED in commit `dcf6c8d`. (Listed for completeness.)

### KB-16 (LOW) — Subtopic-index bootstrap directive coverage
- ALREADY FIXED in commit `dcf6c8d` (subtopic level). Chapter level (depth 3+) explicitly deferred — no current evidence of need.

### KB-17 (LOW) — vol2 sidecar lacks Hubble entry
- Vol2 leaves touch H_∞ but vol2 sidecar has no entry. Cross-cutting Hubble references corrected to vol1+vol3 only. Adding a brief vol2 entry deferring to vol3 would close. **Recommended owner:** kb-content-distiller.

---

## Recommended GitHub-issue updates

1. **Close as resolved (5 items):** B6.2 (fully fixed), B11, B13, B15, N3 (effectively retired via boundaries).
2. **Mark severity-reduced (5 items):** B3, B5, B10, B12, B14 — change tag from CRITICAL/MAJOR to "BOUNDED-NEEDS-FIX" or similar; downstream-safe but source-text fix still wanted.
3. **Keep as PARTIAL (8 items):** B2, B6.1, B6.3, B7, B18, B19, B20, N1, N2.
4. **Keep as UNAFFECTED, prioritize (9 items):** B1, B4, B8, B9, B16, B17, B21, N4 (these are now the highest-leverage cleanup targets; boundaries can't help).
5. **Add 9 newly-surfaced items** (KB-1 through KB-12, minus the 3 already-fixed: KB-14, 15, 16 listed for completeness only).
6. **Note KB-17** (vol2 Hubble entry) as a small follow-up to the boundaries work itself.

## Branch reference

All boundaries-mechanism work is on `feature/kb-claims-boundaries-content` (5 commits, off the existing `kb-claims-boundaries` branch state). PR not yet opened; user intends single review pass before merge.
