[↑ Common Resources](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from research/_archive/L3_electron_soliton as universal-operator catalog -->

# Universal Scale-Invariant Operators (Op1-Op22)

**Status:** consolidation source-of-truth for the 22 universal scale-invariant operators per [Vol 1 Ch 6](../../vol_1_foundations/chapters/06_universal_operators.tex). Canonical names + formulas (where given in Vol 1 Ch 6 or grep-verified at ≥3 distributed citations) plus synthesis labels for operators where the formula is implementer/auditor synthesis without canonical anchor.

**Canonical anchor:** [`manuscript/vol_1_foundations/chapters/06_universal_operators.tex`](../../vol_1_foundations/chapters/06_universal_operators.tex) line 9 verbatim: *"Define the 22 Universal Operators used identically across all spatial scales of the physics engine."*

**Phase 0.2 of [Round 10+ plan](../../../research/_archive/L3_electron_soliton/round_10_plan.md) commits this single-source-of-truth file** to anchor Direction 3 (multi-operator signature observer) + Direction 3' (substrate-(n,l,m_l) → K4 mapping) + future operator-implementation work. Per Rule 12 v2 cross-tree citation promotion: this catalog accumulates ≥3 cross-citations across tracked files (Vol 1 Ch 6, doc 81 §2.2, round_10_plan.md, COLLABORATION_NOTES Rule 8 A43 v2, multiple Vol 2-5 derivations); promotion to `manuscript/ave-kb/common/` per Rule 12 v2 threshold.

**Per A43 v2 (anyone-must-grep, lane-symmetric) discipline:** every entry below is marked CANONICAL (grep-verified verbatim at ≥3 cross-citations to corpus sources) or SYNTHESIS (formula is implementer/auditor synthesis without canonical anchor — useful for orientation but should be promoted to canonical only after derivation lands in Vol 1-5 manuscript or KB leaves).

---

## §1 — Naming-namespace collision flag (auditor-lane)

[`manuscript/ave-kb/CLAUDE.md` INVARIANT-N3](../CLAUDE.md) lists "Known operators: Op2 (knot crossing correction), Op3 (small-signal impedance correction), Op4 (potential well / H-bond), Op8 (large-signal confirmation), Op9 (charge correction), Op14 (long-range coupling)" — six operators with chemistry/molecular descriptions. **These are NOT the same operators as Vol 1 Ch 6's Op2 (Saturation), Op3 (Reflection), Op4 (Pairwise Potential), Op8 (Packing Reflection), Op9 (Steric), Op14 (Dynamic Impedance).**

This is a naming-namespace collision: two different operator sets sharing the "Op#" namespace. The Vol 1 Ch 6 set is the primary AVE physics/circuit-theory operator basis. The INVARIANT-N3 set may be a vol-5-domain-specific molecular-chemistry overload, or it may be stale (predating Vol 1 Ch 6 expansion to 22). Resolution requires auditor-lane review of both sources + cross-volume usage to determine which is canonical and whether INVARIANT-N3 should be revised or flagged as a separate vol-5-specific scheme.

This catalog uses **Vol 1 Ch 6 as the canonical primary**; INVARIANT-N3 collision flagged for auditor-lane.

---

## §2 — Canonical 22-operator catalog (Vol 1 Ch 6 anchor)

| # | Name | Formula | Vol 1 Ch 6 line | Status |
|---|---|---|---|---|
| Op1 | Universal Impedance Operator | Z = √(μ/ε) | 30 | CANONICAL — explicit equation in Vol 1 Ch 6 §1.1 + cross-scale table at lines 47-92 (8 scale instances: vacuum lattice, plasma, seismic, gravitational, protein, fluid, galactic, chiral antenna) |
| Op2 | Universal Saturation Operator | S(A, A_c) = √(1 - (A/A_c)²) | 101 | CANONICAL — explicit equation Vol 1 Ch 6 §1.2. **A-034 EXPANDED CATALOG (canonical 2026-05-15 evening)**: 4 original scale instances (dielectric saturation, BCS B_c(T) at 0.00% error, galactic rotation, relativistic mass) → **21 canonical instances spanning 21 orders of magnitude** per **[KB canonical: Universal Saturation-Kernel Catalog](universal-saturation-kernel-catalog.md)** + [Backmatter Ch 7](../../backmatter/07_universal_saturation_kernel.tex) + [Vol 3 Ch 4 §TKI Strain-Snap](../../vol_3_macroscopic/chapters/04_generative_cosmology.tex) (workflow tracker at `research/_archive/L5/axiom_derivation_status.md`). 3-way symmetry classification: 18 SYM (vacuum K=2G), 2 ASYM-N (BCS μ-only, plasma ε-only), 1 ASYM-E (engineered metamaterials K/G ≠ 2). Per Grant 2026-05-15: *"the bulk response of the lattice to strain is universal."* Empirical anchors: BCS 0.00%, BH ring-down 1.7% from GR, NOAA-validated solar flares (40-yr), Schwarzschild exact. |
| Op3 | Universal Reflection Coefficient | Γ = (Z₂ - Z₁)/(Z₂ + Z₁) | 127 | CANONICAL — explicit equation Vol 1 Ch 6 §1.3 + scale table at lines 133-144 (sub-nuclear Pauli, lab antenna S₁₁, Moho discontinuity) |
| Op4 | Universal Pairwise Potential | U(r) = -K/r·(T² - Γ²); Z(r) = Z₀/(1-(d_sat/r)²)^(1/4) | 190 | CANONICAL — explicit equation Vol 1 Ch 6 §1.4 + 3-regime table (Coulomb / nuclear-H-bond / Pauli) |
| Op5 | Multiport Y-to-S Conversion | [S] = (I + [Y]/Y₀)⁻¹·(I - [Y]/Y₀) | 225 | CANONICAL — explicit equation Vol 1 Ch 6 §1.5; applied at nuclear K_MUTUAL eigenvalues, protein fold eigenstate, antenna S-parameters |
| Op6 | Universal Eigenvalue Target | λ_min(S†S) → 0 | 242 | CANONICAL — explicit equation Vol 1 Ch 6 §1.6; ground-state condition (one mode perfectly absorbed) |
| Op7 | Universal Spectral Analyser | Spatial Fourier transform; α-helix k=N/3.6, β-sheet k=N/2 | 252-264 | CANONICAL by description (no explicit formula in Vol 1 Ch 6 — DSP complement to time-domain SPICE; protein periodicity examples canonical at lines 257-260) |
| Op8 | Packing Reflection Coefficient | Γ_pack = (R_g - R_g_target)/(R_g + R_g_target); R_g_target = √(3/5)·(3·N·V_res/(4π·η_target))^(1/3); η_target = P_C·(1 - 1/N) | 282 | CANONICAL — explicit equation Vol 1 Ch 6 §1.8 (eq:rg_target + eq:gamma_pack); domain-agnostic application to protein globules + nuclear matter + fluid cavities |
| Op9 | Universal Steric Reflection | Γ_steric → -1 (Pauli-level overlap → impedance divergence) | 299 | CANONICAL by description — Vol 1 Ch 6 §1.9 lists as "Pauli-level repulsion mapping overlap to an impedance divergence Γ → -1"; explicit functional form distributed across vol_2 + vol_5 leaves |
| Op10 | Junction Projection Loss | Y_loss ≈ sin²(θ)/π² | 300 | CANONICAL — explicit equation Vol 1 Ch 6 §1.10; predicts c=3 invariant for (2,3) torus knot per **[KB canonical: (2,3) Torus-Knot Uniqueness](../vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md)** + extract_crossing_count implementation in [`src/ave/topological/cosserat_field_3d.py:1468-1550`](../../../src/ave/topological/cosserat_field_3d.py) |
| Op11 | Topological Curl | ∇×V (discrete Yee-lattice form) | 309 | CANONICAL by description — Vol 1 Ch 6 §1.11 names; "translates discrete network adjacency to continuous calculus"; computational |
| Op12 | Topological Divergence | ∇·V (discrete Yee-lattice form) | 309 | CANONICAL by description — Vol 1 Ch 6 §1.11 names; computational |
| Op13 | D'Alembertian | □² (fully generalized wave equation operator) | 310 | CANONICAL by description — Vol 1 Ch 6 §1.12; uses local saturated c_eff (not constant c) per Op16 |
| Op14 | Dynamic Impedance | Z_eff = Z₀/√S | 311 | CANONICAL — explicit equation Vol 1 Ch 6 §1.13. **KB canonical references** (post-2026-05-16 promotion): [Lattice Impedance Decomposition](../vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md), [Op14 Local Clock Modulation](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md), [Op14 Cross-Sector Trading](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md) (empirical: ρ(H_cos, Σ\|Φ_link\|²) = -0.990 at Move 11b). Additional cross-citations: [vol_4 ch 13:338](../../vol_4_engineering/chapters/13_future_geometries.tex), [vol4 KB caustic-resolution lines 15+32](../vol4/advanced-applications/ch20-optical-caustic-resolution/index.md). Asymmetric Meissner case: `Z_eff = Z₀·√(S_μ/S_ε)` distilled in [pair-production-axiom-derivation §6](../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) — different observable when S_μ ≠ S_ε (Meissner-asymmetric magnetic-moment mechanism, also covered in [L3 closure synthesis §6](../vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md)). |
| Op15 | Virtual Strain Radius | r_virtual = √(1 - σ(x)²) | 312 | CANONICAL by description — Vol 1 Ch 6 §1.13 names; "links topological node count to spatial metric volumes"; explicit formula in [doc 81 §2.2](../../../research/_archive/L3_electron_soliton/81_l3_followup_questions.md) — but only single citation. **SYNTHESIS-LABELED until ≥3 cross-citations land.** |
| Op16 | Universal Wave Speed | c_shear = c₀·√S | 317 | CANONICAL — Vol 1 Ch 6 §1.14 narrative ("Freezes wave propagation dynamically as S → 0") + grep-verified explicit formula at ≥3 cross-citations: [vol_2 ch 7 line 1032 + lines 985-993](../../vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex) (label `eq:c_shear`), [axiom-homologation.md §208](axiom-homologation.md) (Ax 4 derived effects table: c_eff = c₀·S^(1/2)), **[KB canonical: Op14 Local Clock Modulation](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md)** (substrate-native time-dilation via $\omega_{local} = \omega_{global}\sqrt{1-A^2}$; cross-volume parallel to gravitational $\tau_{local} = n(r)\tau_{unstrained}$). Gravitational analog: $c \cdot \sqrt{1-A^2} \equiv$ Schwarzschild $c \cdot \sqrt{1-r_s/r}$ in $r_s/r \ll 1$ limit. |
| Op17 | Power Transmission | T² = 1 - Γ² | 318 | CANONICAL — explicit equation Vol 1 Ch 6 §1.16; active energy transfer coefficient |
| Op18 | Coupled Frequency | ω_c = ω₀/√(1 - λk) | 319 | CANONICAL by description — Vol 1 Ch 6 §1.18 names; explicit formula in [doc 81 §2.2](../../../research/_archive/L3_electron_soliton/81_l3_followup_questions.md) but SYNTHESIS-LABELED until ≥3 cross-citations |
| Op19 | Refractive Index | n(r) = 1 + ν_vac·ε₁₁ | 319 | CANONICAL — explicit equation Vol 1 Ch 6 §1.18 + cross-citations: [`eq_gravity_derived.tex`](../../common_equations/eq_gravity_derived.tex) (canonical Symmetric Gravity n(r) = 1 + 2GM/(rc²) form post-axiom-homologation), [Vol 3 Ch 3](../../vol_3_macroscopic/chapters/03_macroscopic_relativity.tex). ν_vac = 2/7 (Poisson ratio: 2 compliance / 7 total modes) |
| Op20 | Regime Eigenvalue | (no canonical formula in Vol 1 Ch 6 — only "5-step regime-crossing scalar target") | 320 | **SYNTHESIS** — Vol 1 Ch 6 narrative only ("Defines the 5-step regime-crossing scalar target"). Formula `ω_regime = ℓ·c_wave/r_eff` appears ONLY in [doc 81 §2.2](../../../research/_archive/L3_electron_soliton/81_l3_followup_questions.md) + [round_10_plan.md §3.4](../../../research/_archive/L3_electron_soliton/round_10_plan.md) — implementer-synthesis without canonical manuscript anchor. **A43 v10 instance flagged for auditor-lane post-closure bundle:** the synthesis-as-corpus framing of Op20 formula in doc 81 + propagation into round_10_plan.md needs verification or explicit synthesis-labeling at the source. Round 10+ Phase 1 Direction 3.4 observer pre-reg should label the formula as "synthesis from doc 81 + plan; canonical Vol 1 Ch 6 narrative does not specify" |
| Op21 | Quality Factor Phase Transition | Q ~ 1/ln(Z₁/Z₀) (Bardeen BCS mapping) | 321 | CANONICAL — Vol 1 Ch 6 §1.21 explicit formula; superconductivity threshold mechanism. Note: separately, `Q = ℓ` (lattice pitch in natural units) per [doc 81 §2.2](../../../research/_archive/L3_electron_soliton/81_l3_followup_questions.md) — that's a different identification (Q-as-lattice-pitch) and may be the bootstrap / α = 1/137.036 derivation, NOT the Bardeen mapping. Cross-reference needs auditor-lane confirmation |
| Op22 | Avalanche Factor | M = 1/S² = 1/(1 - r²) | 322 | CANONICAL — explicit formula at [`backmatter/appendix_c_derived_numerology.tex:78`](../../backmatter/appendix_c_derived_numerology.tex) + [`ave-kb/common/appendix-derived-numerology.md:50`](appendix-derived-numerology.md): "universal avalanche factor M = 1/S² = 1/(1 - r²) directly derives from Axiom 4 power conservation (effective pure 1D exponent of n=2)". Vol 1 Ch 6 §1.22 narrative confirms ("Captures nonlinear cascading metric yield"). **A43 v11 correction flagged:** [doc 81 §2.2](../../../research/_archive/L3_electron_soliton/81_l3_followup_questions.md) gave `M = 1/(1 - S(V))` which is a DIFFERENT formula (1/(1-S) vs 1/S²); as S → 0 these diverge differently (corpus → ∞, doc 81 → 1). Round 10+ Phase 1 Direction 3.5 observer pre-reg should use canonical `M = 1/S²` formula, NOT doc 81's synthesis. Auditor-lane post-closure bundle should add as A43 v11 worked example |

---

## §3 — Implementation pointers

| Op | Implementation pointer (where engine code or test driver exists) |
|---|---|
| Op1 (Z) | [`src/ave/core/k4_tlm.py`](../../../src/ave/core/k4_tlm.py) build_scattering_matrix(z_local) at line 36 |
| Op2 (S) | Distributed across [`cosserat_field_3d.py:459`](../../../src/ave/topological/cosserat_field_3d.py) `_update_saturation_kernels` + [`k4_tlm.py:248-322`](../../../src/ave/core/k4_tlm.py) S_field state |
| Op3 (Γ) | Implicit in scatter+connect K4 dynamics; explicit Γ-curves in `_reflection_density` at [`cosserat_field_3d.py:266`](../../../src/ave/topological/cosserat_field_3d.py) |
| Op6 (λ_min) | Eigsolve drivers throughout `src/scripts/vol_1_foundations/r7_*` (V-block + Cos-block eigsolves at corpus GT) |
| Op10 (Y_loss / c=3) | `extract_crossing_count` at [`cosserat_field_3d.py:1468-1550`](../../../src/ave/topological/cosserat_field_3d.py) (Cosserat ω-field) + [`tlm_electron_soliton_eigenmode.py:567-640`](../../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py) (K4 V-field) |
| Op14 (Z_eff) | [`cosserat_field_3d.py:459`](../../../src/ave/topological/cosserat_field_3d.py) `_update_saturation_kernels` modulates per-cell impedance via S(A) per axiom 4 |
| Op16 (c_shear) | NOT YET implemented as observer; Round 10+ Phase 1 Direction 3.3 candidate |
| Op20 (ω_regime) | NOT YET implemented; Round 10+ Phase 1 Direction 3.4 candidate (formula synthesis-flagged per §2 above) |
| Op22 (M) | NOT YET implemented; Round 10+ Phase 1 Direction 3.5 candidate (use canonical `M = 1/S²` per §2 above) |

---

## §4 — Scale-invariance argument (summary)

Per Vol 1 Ch 6 §1.1 verbatim claim line 29-35: *"The characteristic impedance Z = √(μ/ε) is the single structural invariant of the AVE framework. No scale-specific modifications, fitting parameters, or domain-dependent redefinitions are required. Every physical phenomenon in the derivation chain reduces to boundary conditions on this single operator."*

The 22 operators inherit scale-invariance from Op1 (Z) by construction:
- Op2 (S) is dimensionless ratio (A/A_c) — automatically scale-invariant
- Op3 (Γ) is dimensionless ratio of impedances — Op1-derived, automatically scale-invariant
- Op4-22 compose Op1+Op2+Op3 with dimensionless coefficients — all inherit invariance

**Scale-invariance is the framework's distinguishing claim.** The same operator code path is called at vacuum lattice (10⁻¹³ m), atomic (10⁻¹⁰ m), molecular (10⁻⁸ m), seismic (10⁶ m), gravitational (10²⁶ m) — 14 orders of magnitude per Vol 1 Ch 6 line 15. The cross-scale table at lines 47-92 (Op1) + four-domain demonstration at lines 107-115 (Op2) + scale table at lines 133-144 (Op3) collectively anchor the claim.

---

## §5 — A43 v10/v11 worked-example flags (auditor-lane post-closure bundle)

Two implementer-side A43 instances surfaced during Phase 0.2 grep-verification of operator formulas in this catalog. Numbering note: A43 v9 was the auditor-side atomic-orbital ladder wrong-directory grep instance landed earlier this session in the post-closure queue; v10 and v11 below are these two new implementer-side instances.

**A43 v10 — Op20 ω_regime formula synthesis-as-corpus:** doc 81 §2.2 + round_10_plan.md §3.4 + this catalog §2 use `ω_regime = ℓ·c_wave/r_eff` as if canonical. Vol 1 Ch 6 §1.20 line 320 only specifies "Defines the 5-step regime-crossing scalar target" — no formula. The `ω_regime = ℓ·c_wave/r_eff` framing originated in [doc 81 §2.2](../../../research/_archive/L3_electron_soliton/81_l3_followup_questions.md) implementer-synthesis from "regime eigenvalue" naming + ω-form analogy, NOT verbatim corpus. Synthesis-as-corpus per A43 v2 lane-symmetric discipline. Correction: label as synthesis in operators.md §2 (DONE in this commit); flag in round_10_plan.md §3.4 in-flight amendment; doc 81 §2.2 Rule-12-style addendum; auditor-lane A43 v10 worked example.

**A43 v11 — Op22 formula different from canonical:** doc 81 §2.2 + round_10_plan.md §3.5 + this catalog draft used `M = 1/(1 - S(V))`; canonical [`backmatter/appendix_c_derived_numerology.tex:78`](../../backmatter/appendix_c_derived_numerology.tex) gives `M = 1/S² = 1/(1 - r²)`. As S → 0, the formulas diverge differently: corpus → ∞ (avalanche actually cascades to infinity at saturation onset), doc 81 → 1 (no cascade). doc 81 synthesis was wrong formula; corpus correct. Correction: use canonical formula in operators.md §2 (DONE in this commit); fix in round_10_plan.md §3.5 in-flight amendment; doc 81 §2.2 Rule-12-style addendum; auditor-lane A43 v11 worked example.

Both worked examples extend the [A43 v2 lane-symmetric pattern](../../../.agents/handoffs/COLLABORATION_NOTES.md) from 8 to 11 instances total cumulatively (six auditor-side originally in A43 v2 body + two implementer-side originally in A43 v2 body + three post-A43-v2 in queue: v9 auditor atomic-orbital + v10 implementer Op20 + v11 implementer Op22). Pattern continues empirically symmetric.

---

## §5.5 — Cross-volume substrate motifs (recurring patterns, NOT numbered Ops)

Named recurring substrate-physics patterns that operate across multiple AVE volumes but are NOT numbered operators from the Vol 1 Ch 6 catalog. These are structural-synthesis observations rather than primitive physics operators.

### Hoop Stress 2π projection (NEW 2026-05-17, honest-scoped 2026-05-17 late evening seventh audit cycle per external reviewer catch)

**Recurring pattern**: substrate bulk drift $c \times \epsilon$ (where $\epsilon$ is a small dimensionless parameter set by scale) projected through the Hoop Stress geometric factor $2\pi$ onto closed topological loops gives the observable equilibrium scale at that scale.

**Independent scale-instances** (2 truly independent applications across distinct scales with distinct small-parameters):

| Scale | Formula | Small parameter $\epsilon$ | Output | Canonical source |
|---|---|---|---|---|
| **Cosmic** (MOND) | $a_0 = c \cdot \epsilon / (2\pi)$ | $\epsilon = H_\infty$ (cosmological expansion rate) | Acceleration $\sim 10^{-10}$ m/s² | [`../vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md` §1](../vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md) |
| **Substrate** (electron α-slew) | $v_{substrate} = c \cdot \epsilon / (2\pi)$ | $\epsilon = \alpha$ (fine structure constant) | Velocity $\sim 348$ km/s | [`../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md` §5](../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md) |

**Derivative observables at the substrate operating point** (algebraically derived from the α-slew instance via h × ν_slew conversions; NOT independent Hoop Stress applications):

| Derivative | Algebraic chain | Output | Canonical source |
|---|---|---|---|
| DAMA energy quantum | $E_{substrate} = h \cdot \nu_{slew} = h \cdot \alpha c / (2\pi \ell_{node})$; with $\ell_{node} = \hbar/(m_e c)$, the $2\pi$ and $\hbar$ factors collapse and yield $E = \alpha m_e c^2$ | $\sim 3.728$ keV | [`../vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md`](../vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md) |

**Honest-scope note (2026-05-17 late evening, external reviewer catch on prior version of this section)**: an earlier version of this table listed DAMA quantum as instance #3 of the Hoop Stress motif. External reviewer caught that DAMA quantum is algebraically DERIVED from the α-slew velocity instance (the 2π cancels in the derivation chain), not an independent third scale-instance. Corpus-grep across all 10 AVE repos (2026-05-17 late evening) confirmed NO genuine third independent scale-instance of `c × ε / (2π)` Hoop Stress projection exists. Honest framing is **2 independent scale-instances + 1 derivative observable**; the motif is structurally recurring across 2 scales (cosmic + substrate), not 3.

**Physical interpretation**: Hoop Stress is the canonical continuum-mechanics projection — when an isotropic outward radial force is applied to a closed circular loop, the resulting longitudinal tension on the loop is `T = F_r / 2π`. The same projection applies to substrate drift acting on topological-loop solitons at any scale (cosmic horizon, electron unknot). The small-parameter $\epsilon$ is set by the dominant physics at each scale: cosmological expansion ($H_\infty$) at cosmic scale; electromagnetic coupling ($\alpha$) at substrate scale. A future genuine third instance at intermediate scale (atomic, nuclear, stellar, molecular) would substantiate the motif more strongly; current corpus-grep confirms no such third instance currently exists.

**Empirical anchors (as of 2026-05-17 late evening)**:
- Cosmic instance: $a_0$ matches Milgrom to 10.7%; SPARC 135-galaxy benchmark 11.5% Q=1 mean residual (FOREWORD-PROMOTED as first positive load-bearing empirical anchor).
- Substrate instance: $v_{substrate}$ within 9% of LSR-class bulk velocity (375 km/s observed); cluster tightness $\sigma=11$ km/s inconsistent with random galactic kinematics (active research consistency result; demoted from foreword promotion per ave-discrimination-check audit because directional alignment is consistency check with K4=CMB identification, not independent AVE evidence).
- DAMA derivative observable: $E_{substrate} = 3.728$ keV in DAMA's 2-6 keV detection window (zero-parameter foreword-bullet AVE-distinct prediction).

**Other 2π denominators in the corpus that are NOT Hoop Stress 2π projections** (added 2026-05-17 late evening per corpus-grep finding): the corpus contains multiple distinct physical origins of 2π factors. Examples of NEAR-MISSES that share form but differ in physical origin:
- **Q-G22 atomic-strain ratio** at [`../vol4/circuit-theory/ch1-vacuum-circuit-analysis/q-g22-strain-convention.md:39-41`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/q-g22-strain-convention.md): `A = α/(2π)` at $r = 2\pi a_0$ — the 2π is the orbital-circumference geometric factor, NOT a Hoop Stress projection of substrate drift.
- **Q-G27 muon Cosserat saliency** at [`../vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md:38`](../vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md): $\delta_{Cosserat} = -\alpha\sqrt{3/7}/(2\pi)$ — the 2π is explicitly named "Compton-traverse form-factor" (Schwinger-cousin), NOT Hoop Stress.
- **Atomic orbital current** $I = e\omega_1/(2\pi)$ at [`../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md:50`](../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md): 2π is orbital-period normalization, NOT Hoop Stress.

These are structurally different physics; the matching form does NOT indicate the same recurring motif. Discipline note: when claiming a "recurring 2π motif," verify the geometric ORIGIN of the 2π factor, not just its presence in a denominator.

**Canonical-status note**: this motif was NAMED for the first time in the corpus 2026-05-17. The two-instance scope (cosmic + substrate) is the current corpus state. Future work that finds a genuine third independent instance at a different scale with a different small-parameter would strengthen the motif claim; corpus-grep 2026-05-17 late evening confirmed absence.

## §6 — Phase 0.2 status

This catalog is the canonical Phase 0.2 deliverable per [Round 10+ plan](../../../research/_archive/L3_electron_soliton/round_10_plan.md) commit `48ee43d` + amendment `d8ca5b9`. Catalog enables:

- **Direction 3 multi-operator signature observer** (Phase 1) — Op14/16/20/22 formula citations canonical (Op14, Op16) or synthesis-flagged (Op20, Op22 doc-81-correction-applied)
- **Direction 3' substrate-(n,l,m_l) → K4 mapping** (Phase 1) — Op6 (eigenvalue target → radial nodes n_r), Op10 (c=3 invariant → angular nodes l) canonical citations available
- **Per-pre-reg A43 v2 verification gate** (round_10_plan.md verification table) — operators.md is the single-source-of-truth for cross-ref grep-verification at pre-reg freeze time

---

## §7 — References

- [`manuscript/vol_1_foundations/chapters/06_universal_operators.tex`](../../vol_1_foundations/chapters/06_universal_operators.tex) — canonical 22-operator catalog (primary anchor)
- [`manuscript/ave-kb/CLAUDE.md` INVARIANT-N3](../CLAUDE.md) — KB cross-cutting invariant naming (collision flagged in §1)
- [`manuscript/backmatter/appendix_c_derived_numerology.tex`](../../backmatter/appendix_c_derived_numerology.tex) — Op22 canonical formula
- [`manuscript/ave-kb/common/appendix-derived-numerology.md`](appendix-derived-numerology.md) — KB Op22 canonical formula
- [`manuscript/ave-kb/common/axiom-homologation.md`](axiom-homologation.md) — Ax 4 derived-effects table includes c_eff = c₀·S^(1/2) (Op16)
- [`research/_archive/L3_electron_soliton/81_l3_followup_questions.md` §2.2](../../../research/_archive/L3_electron_soliton/81_l3_followup_questions.md) — doc 81 synthesis catalog (with A43 v10/v11 corrections noted in §5; doc 81 also has Rule-12-style addendum referencing this catalog as canonical)
- [`research/_archive/L3_electron_soliton/round_10_plan.md`](../../../research/_archive/L3_electron_soliton/round_10_plan.md) — Round 10+ plan (Phase 1 Direction 3 cites operators directly)
- [`.agents/handoffs/COLLABORATION_NOTES.md`](../../../.agents/handoffs/COLLABORATION_NOTES.md) — Rule 8 A43 v2 lane-symmetric (anyone-must-grep) discipline; ≥3-citation promotion threshold (Rule 12 v2)
