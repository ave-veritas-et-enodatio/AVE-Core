# AVE KB Burndown — Actionable Items Only

> Distilled from `kb-burndown-unified.md`. Excludes 🟢 RESOLVED items (B6.2, B11, B13, B15, N3) and ⚪ VERIFIED items (N5, N6, N7) and the 3 already-fixed kb-followups (KB-14, KB-15, KB-16). Everything below is open work.
>
> **Severity post-bounding rule:** items that the claims-boundaries mechanism (`kb/claims-boundaries.md` and `kb/volN/claims-boundaries.md`) makes downstream-safe have their priority adjusted to reflect that consumers traversing the directives are protected; the underlying source-text fix is still needed but no longer urgent for downstream correctness.
>
> **Total actionable: 35 items** (2 CRITICAL, 13 MAJOR, 11 MINOR, 9 TRIVIAL).

---

## CRITICAL — Fix immediately (boundaries don't protect consumers)

| ID | Finding | Files | Owner |
|---|---|---|---|
| **B4** | `translation-particle-physics.md` Higgs VEV formula wrong by ~3500×: "v = m_ec²/α = 246 GeV" (actual: 70.0 MeV). Correct AVE formula: v = 1/√(√2·G_F) = 248.8 GeV (already in `full-derivation-chain.md`). | `common/translation-tables/translation-particle-physics.md` | kb-content-distiller |
| **B8** | G_vac = m_ec²/ℓ_node² has wrong units (J/m² = N/m, not Pa) and value off by 10¹³ (5.49×10¹¹ N/m vs claimed 5.48×10²⁴ Pa). Correct shear-modulus formula: m_ec²/ℓ_node³. Downstream: v_longitudinal computation gives 3.93c, not the claimed √2·c. | `vol1/dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md`, `mond-hoop-stress.md` | vol1 domain author |

---

## MAJOR — Address before manuscript submission

### Bounded but source-text fix still required

| ID | Finding | Files | Owner |
|---|---|---|---|
| **B3** | `master-equation.md` direction error: "ε_eff → 0 forces Z → 0" — wrong. Z = √(μ/ε) gives Z → ∞ for ε → 0 with μ finite. `regime-equation-sets.md` table is internally inconsistent with its own caption. | `master-equation.md`, `regime-equation-sets.md` | vol1 domain author |
| **B5** | Ch.8 Golden Torus α derivation rests on three asserted (not derived from axioms) identifications: (a) sum decomposition α⁻¹ = Λ_vol+Λ_surf+Λ_line; (b) 4π spin-1/2 cover factor; (c) Λ_line = π·d. Spectacular numerical agreement follows from assertions, not proofs. | `vol1/ch8-alpha-golden-torus.md` | vol1 / theoretical author |
| **B10** | Neon-20 <0.001% prediction requires R_bipyramid = 72.081d — an optimizer-tuned parameter against the known mass. Violates LIVING_REFERENCE rule #12 (no smuggled data). vol1 sidecar discloses but headline still misleads. | `vol1/operators-and-regimes/ch5-universal-spatial-tension/scale-invariance.md` | vol1 domain author |
| **B12** | LIVING_REFERENCE Axiom 3 G formula G = ℏc/(7ξ·m_e²) — units issue: artifact `lc-condensate-vacuum.md` uses G_true = ℏc/m_e² (correct units, different formula, no 7ξ factor). Reconcile which is canonical. | `LIVING_REFERENCE.md` vs `vol1/axioms-and-lattice/ch1-fundamental-axioms/lc-condensate-vacuum.md` | vol1 domain author |
| **B14** | `mathematical-closure.md` asserts mathematical closure narratively without formal DAG construction or acyclicity check. G appears as both empirical input (line 20) and claimed derived quantity in same document. Setting ℓ_node = 1 is a units reframing, not a derivation. | `common/mathematical-closure.md` | kb-taxonomy-architect + theoretical author |

### Substantive authoring fixes (no bounding coverage)

| ID | Finding | Files | Owner |
|---|---|---|---|
| **B9** | Torus-knot mass ladder inconsistent across files: (2,5) proton = 938 MeV vs 945 MeV; (2,7) Δ(1232) = 1261 MeV vs 1270 MeV. Identify canonical solver output. | `common/full-derivation-chain.md`, `common/solver-toolchain.md` | kb-content-distiller |
| **B6.1** | `translation-gravity.md` row 9 G formula evaluates to ~6.9×10³⁶ m³/(kg·s²) — ~10⁴⁷× the measured G. | `common/translation-tables/translation-gravity.md` | kb-content-distiller |
| **B6.3** | `translation-gravity.md` row 9 attributes G to Axiom 2 (Topo-Kinematic); LIVING_REFERENCE places G under Axiom 3 (Gravity). Reattribute. | `common/translation-tables/translation-gravity.md` | kb-content-distiller |
| **B7** | Ch.2 "α derivation" mislabels two failures: (i) uses Schwinger critical field (QED result) as input; (ii) algebraic chain p_c = 2e²/(ε₀ℏc) ≡ 8πα is rearrangement of α's definition. Reframe as constraint/consistency check, not derivation. | `vol1/axioms-and-lattice/ch2-macroscopic-moduli/dielectric-rupture.md`, `common/full-derivation-chain.md` Layer 2 | vol1 / theoretical author |
| **B2** | C_eff = C_0/S (Axiom 4) and ε_eff = ε_0·S (master/telegrapher) need explicit convention disambiguation in the leaves: differential vs constitutive capacitance, Born-Infeld vs Maxwell. Boundaries entry shows them as compatible but the convention is not named. | `axiom-definitions.md`, `master-equation.md`, `nonlinear-telegrapher.md`, `operating-regimes-table.md` | vol1 domain author |

### Newly surfaced (from kb-claims-boundaries dispatches)

| ID | Finding | Files | Owner |
|---|---|---|---|
| **KB-7** | vol4 index Key Results / Domains tables cite "PONDER-05 469 µN predicted thrust" with link to `vol4/hardware-programs/index.md` — directory doesn't exist; PONDER-05 / 469 µN appear nowhere in vol4 leaves. Actual leaves give PONDER-01 with 40.1 µN. Either author missing leaves or normalize index numbering. | `vol4/index.md` (lines 12, 23) | kb-taxonomy-architect + kb-content-distiller |
| **KB-12** | `radioactive-decay-impedance.md` reports tritium decay as ~11.3 MeV; empirical β-endpoint is 18.6 keV (~600× smaller). Either framework figure means something different from measured Q_β (and should say so) or substantive numerical error. | `vol6/framework/computational-mass-defect/radioactive-decay-impedance.md` | vol6 framework author or nuclear-domain reviewer |

---

## MINOR — Address before public release

| ID | Finding | Files | Owner |
|---|---|---|---|
| **B16** | `xi-topo-traceability.md` dependency arrows wrong. Chain shows ℓ_node → (Axiom 1) → α → (Axiom 2) → ξ_topo. α is derived in Ch.8 from Golden Torus topology (all four axioms + geometric constraints), not from Axiom 1 alone. | `common/xi-topo-traceability.md` | kb-content-distiller |
| **B17** | V_cb deviation in LIVING_REFERENCE Master Prediction Table #27 claims 4.1%; arithmetic with PDG averages gives 5.7–6.3%. | `LIVING_REFERENCE.md` row #27 | LIVING_REFERENCE author |
| **B18** | Neutrino crossing numbers (c₁=5, c₂=7, c₃=9) and Cosserat lepton coupling factors (α√(3/7) muon, 8π/α tau) asserted by pattern, not derived from the four axioms. | `common/full-derivation-chain.md`, `vol1/operators-and-regimes/ch5-universal-spatial-tension/scale-invariance.md` | theoretical author |
| **B19** | GUP derivation asserts root-sum-square combination ("orthogonal hardware constraints") without applying Robertson-Schrödinger inequality to the cosine commutator. | `vol1/dynamics/ch3-quantum-signal-dynamics/gup-derivation.md` | vol1 / theoretical author |
| **B20** | Schrödinger-from-circuit derivation recovers only free-particle equation; no V(r)·Ψ term derived for bound-state physics. Would arise from spatial modulation of ε_eff or μ_eff. | `vol1/dynamics/ch3-quantum-signal-dynamics/schrodinger-from-circuit.md` | vol1 / theoretical author |
| **B21** | `phase-locked-topological-thread.md` contains raw LaTeX (`\begin{itemize}`, `\begin{tabular}`, malformed `$T \ll T_{pair**$`). Won't render in any Markdown viewer. | `vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md` | kb-content-distiller |
| **N1** | r₂ = √3/2 boundary derived from ℓ_min = 2 is spin-2 (GW) specific. For scalars ℓ_min = 0, photons ℓ_min = 1. "Universal regimes" framing requires additional justification or scope-restriction. | regime-map leaves | vol1 / theoretical author |
| **N2** | Cosserat "three sectors = three generations" is structural matching, not axiom-derived. Should be labeled as identified/matched rather than derived. | `scale-invariance.md`, `full-derivation-chain.md` | vol1 / theoretical author |
| **N4** | `dielectric-lagrangian.md` minor intermediate unit-tracking inconsistency (kg/s vs kg/s² in one step) that cancels in the final result. Documentation fix only. | `vol1/dynamics/ch3-quantum-signal-dynamics/dielectric-lagrangian.md` | vol1 author |
| **KB-1** | Z=Z₀ vs Z→0 horizon impedance interpretive tension between leaves: `einstein-field-equation.md` says Z → 0 at r_s; `invariant-gravitational-impedance.md` and `gw-propagation-lossless.md` say Z = Z₀ invariant under symmetric gravity. Both reconcilable but no in-leaf reconciling note. | `vol3/gravity/ch02-general-relativity/einstein-field-equation.md` (~line 42), `vol3/gravity/ch08-gravitational-waves/invariant-gravitational-impedance.md`, `gw-propagation-lossless.md` | kb-content-distiller or vol3-gravity domain expert |
| **KB-5** | vol5 index references `vol5/protein-folding-engine/` subtree (Chs. 3–5: Z_topo, 8-tier architecture, 2D TL solver, 20-protein PDB validation, S₁₁ objective, Kramers folding time). Directory unauthored in this repo (engine lives in private `AVE-Protein` repo). Multiple broken Key Results links; confirmed broken cross-link in `consciousness-cavity-eigenmode.md` line 53. | `vol5/index.md`, `vol5/biological-applications/consciousness-cavity-eigenmode.md` | kb-taxonomy-architect (replicate vs amend decision) + kb-content-distiller |
| **KB-9** | vol4 leaves switch between V_yield (43.65 kV) and "60 kV" without flagging. The 60 kV figure is the D-T tokamak ion-collision strain (V_topo ≈ 60.3 kV), not a third axiomatic yield threshold. Used as if equivalent in YBCO-array and autoresonant-PLL leaves. | `vol4/simulation/ch15-autoresonant-breakdown/theory.md`, `vol4/falsification/ch11-experimental-bench-falsification/ybco-phased-array.md`, `metric-levitation-limit.md` | kb-content-distiller or vol4-engineering domain expert |

---

## TRIVIAL — Polish; address opportunistically

| ID | Finding | Files | Owner |
|---|---|---|---|
| **KB-2** | Hubble Key Results row in `vol3/index.md` shows H_∞ ≈ 69.32 km/s/Mpc with no qualifier. Boundaries cover; index headline still misleads direct readers. Add asterisk/footnote referencing `lattice-genesis-hubble-tension.md`'s consistency-proof framing. | `vol3/index.md` line 14 | kb-content-distiller |
| **KB-3** | Hubble value 69.32 (LIVING_REFERENCE, entry-point.md) vs 69.33 (`lattice-genesis-hubble-tension.md` table) — last-digit inconsistency. Pick one; reconcile. | `LIVING_REFERENCE.md` row #23, `entry-point.md`, `lattice-genesis-hubble-tension.md` | kb-content-distiller |
| **KB-4** | `common/index.md` Key Results: "8 derivation layers → genuinely zero free parameters" lacks the conditional qualifier (one currently-fitted δ_strain scalar). Boundaries cover; index headline still over-broad. | `common/index.md` | kb-content-distiller |
| **KB-6** | vol5 η_eq packing-fraction formula and S₁₁ folding-functional definition have no derivation leaf in this repo (functional-definition leaves are in private `AVE-Protein`). Same content-gap pattern as the original α-invariance gap (now closed). Either replicate sanitized leaves or accept honest invariant-doc provenance. | vol5 sidecar references | kb-content-distiller |
| **KB-8** | `optical-caustic-resolution/index.md` Key Results: "E_max = E_YIELD = √α·m_ec²/e ≈ 43.65 kV/m" — formula evaluates to 43.65 **kV** (voltage), not kV/m (field). Macroscopic field equivalent: ~1.13×10¹⁷ V/m. Units glitch only; substantive bound is correct. | `vol4/advanced-applications/ch20-optical-caustic-resolution/index.md` (~line 14) | kb-content-distiller |
| **KB-10** | vol6 `mass-defect-summary.md` and index Key Results show 0.00001%–0.02739% errors without the fit-vs-prediction qualifier present in `semiconductor-nuclear-analysis.md` (per-nucleus geometric fit). Boundaries cover; summary still misleads. | `vol6/framework/mass-defect-summary.md`, `vol6/index.md` | kb-content-distiller |
| **KB-11** | vol6 heavy-element catalog "<0.5% across 105 elements" headline — typical-case figure. `full-element-table.md` shows worst case Cl-35 at 1.465%, several others above 0.5%. Boundaries tier the accuracy; headline still clean. | `vol6/appendix/heavy-element-catalog/index.md`, `vol6/index.md` | kb-content-distiller |
| **KB-13** | vol6 ABCD transfer-matrix open-problem caveat (gates Z ≥ 15 catalog results) not surfaced from `full-element-table.md` or `appendix/heavy-element-catalog/index.md`. Add cross-link from heavy-element catalog to `abcd-transfer-matrix.md`. | `vol6/appendix/heavy-element-catalog/index.md`, `full-element-table.md` | kb-content-distiller |
| **KB-17** | vol2 sidecar lacks Hubble entry; cross-cutting Hubble references corrected to vol1+vol3 only (commit `e7f4566`). Add brief vol2 entry deferring to vol3's canonical treatment. | `vol2/claims-boundaries.md` | kb-content-distiller |

---

## Out of this scope (tracked elsewhere)

These are part of the broader plan but outside the AVE-Core repo (the kb-claims-boundaries work ran AVE-Core-only per scope cut):

- All `.claude/agents/*.md` edits (KB-touching agents + MAD-side agents) — separate repo
- Boundaries Mode codification in `kb-content-distiller.md` (Dispatch 13 in plan) — separate repo
- Plan-doc updates in `mad-review/` — separate repo

These should be picked up in a separate dispatch sized to the agents/MAD repos.

---

## Counts

| Tier | Count |
|---|---:|
| CRITICAL | 2 |
| MAJOR | 13 |
| MINOR | 11 |
| TRIVIAL | 9 |
| **Total actionable** | **35** |

> **Closed in earlier passes (not in this list):** B1 (axiom numbering drift) was resolved by the "phase 1 — axiom numbering consistency" commit `8538e5f` plus follow-ups `f41d612`, `aa172ef`. `axiom-definitions.md`, `mathematical-closure.md`, CLAUDE.md INVARIANT-S2, and LIVING_REFERENCE.md now all use the canonical Axiom 1=Impedance / 2=Fine Structure / 3=Gravity / 4=Saturation Kernel ordering.

Source: `kb-burndown-unified.md` (commit `bccfa1e`); branch `kb-claims-boundaries`.
