[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-sysqaf, clm-6mvtsf, clm-gdd70j]
path-stable: "universal-operator catalog of record (Vol 1 Ch 6)"
-->

# Universal Scale-Invariant Operators (Op1-Op22)

**Status:** consolidation source-of-truth for the 22 universal scale-invariant operators per [Vol 1 Ch 6](../../vol_1_foundations/chapters/06_universal_operators.tex). Canonical names + formulas (where given in Vol 1 Ch 6 or grep-verified at ≥3 distributed citations) plus synthesis labels for operators where the formula is implementer/auditor synthesis without canonical anchor.

**Canonical anchor:** [`manuscript/vol_1_foundations/chapters/06_universal_operators.tex`](../../vol_1_foundations/chapters/06_universal_operators.tex) line 9 verbatim: *"Define the 22 Universal Operators used identically across all spatial scales of the physics engine."*

This single-source-of-truth file anchors multi-operator signature observer work and substrate-$(n,l,m_l)$ → K4 mapping work. Per cross-tree citation promotion discipline: this catalog accumulates ≥3 cross-citations across tracked files (Vol 1 Ch 6, doc 81 §2.2, the Round 10+ plan, collaboration notes, multiple Vol 2-5 derivations); promotion to `manuscript/ave-kb/common/` per the ≥3-citation threshold.

**Per anyone-must-grep, lane-symmetric discipline:** every entry below is marked CANONICAL (grep-verified verbatim at ≥3 cross-citations to corpus sources) or SYNTHESIS (formula is implementer/auditor synthesis without canonical anchor — useful for orientation but should be promoted to canonical only after derivation lands in Vol 1-5 manuscript or KB leaves).

---

## §1 — Naming-namespace collision flag (auditor-lane)

[`manuscript/ave-kb/CLAUDE.md` INVARIANT-N3](../CLAUDE.md) lists "Known operators: Op2 (knot crossing correction), Op3 (small-signal impedance correction), Op4 (potential well / H-bond), Op8 (large-signal confirmation), Op9 (charge correction), Op14 (long-range coupling)" — six operators with chemistry/molecular descriptions. **These are NOT the same operators as Vol 1 Ch 6's Op2 (Saturation), Op3 (Reflection), Op4 (Pairwise Potential), Op8 (Packing Reflection), Op9 (Steric), Op14 (Dynamic Impedance).**

This is a naming-namespace collision: two different operator sets sharing the "Op#" namespace. The Vol 1 Ch 6 set is the primary AVE physics/circuit-theory operator basis. The INVARIANT-N3 set may be a vol-5-domain-specific molecular-chemistry overload, or it may be stale (predating Vol 1 Ch 6 expansion to 22). Resolution requires auditor-lane review of both sources + cross-volume usage to determine which is canonical and whether INVARIANT-N3 should be revised or flagged as a separate vol-5-specific scheme.

This catalog uses **Vol 1 Ch 6 as the canonical primary**; INVARIANT-N3 collision flagged for auditor-lane.

---

## §2 — Canonical 22-operator catalog (Vol 1 Ch 6 anchor)
<!-- claim-quality: clm-sysqaf -->

The 22 universal scale-invariant operators (Op1–Op22) are the AVE engine's named operator basis — the catalog of record per Vol 1 Ch 6. Individual operator formulae are owned by their respective Vol 1 Ch 6 leaves; entries below restating an operator formula cite those Ch 6 leaves.

The Op1 Universal Impedance formula $Z = \sqrt{\mu/\varepsilon}$ restated below is owned by the [Vol 1 Ch 6 §6.1 Universal Impedance Operator](../vol1/operators-and-regimes/ch6-universal-operators/impedance-operator.md) leaf — this catalog cites it.
<!-- claim-quality: clm-gdd70j -->

| # | Name | Formula | Vol 1 Ch 6 line | Status |
|---|---|---|---|---|
| Op1 | Universal Impedance Operator | $Z = \sqrt{\mu/\varepsilon}$ | 30 | CANONICAL — explicit equation in Vol 1 Ch 6 §1.1 + cross-scale table at lines 47-92 (8 scale instances: vacuum lattice, plasma, seismic, gravitational, protein, fluid, galactic, chiral antenna) |
| Op2 | Universal Saturation Operator | $S(A, A_c) = \sqrt{1 - (A/A_c)^2}$ | 101 | CANONICAL — explicit equation Vol 1 Ch 6 §1.2. **A-034 EXPANDED CATALOG (canonical 2026-05-15 evening)**: 4 original scale instances (dielectric saturation, BCS $B_c(T)$ at 0.00% error, galactic rotation, relativistic mass) → **21 canonical instances spanning 21 orders of magnitude** per **[KB canonical: Universal Saturation-Kernel Catalog](universal-saturation-kernel-catalog.md)** + [Backmatter Ch 7](../../backmatter/07_universal_saturation_kernel.tex) + [Vol 3 Ch 4 §TKI Strain-Snap](../../vol_3_macroscopic/chapters/04_generative_cosmology.tex). 3-way symmetry classification: 18 SYM (vacuum $K=2G$), 2 ASYM-N (BCS $\mu$-only, plasma $\varepsilon$-only), 1 ASYM-E (engineered metamaterials $K/G \neq 2$). Per Grant 2026-05-15: *"the bulk response of the lattice to strain is universal."* Empirical anchors: BCS 0.00%, BH ring-down 1.7% from GR, NOAA-validated solar flares (40-yr), Schwarzschild exact. |
| Op3 | Universal Reflection Coefficient | $\Gamma = (Z_2 - Z_1)/(Z_2 + Z_1)$ | 127 | CANONICAL — explicit equation Vol 1 Ch 6 §1.3 + scale table at lines 133-144 (sub-nuclear Pauli, lab antenna $S_{11}$, Moho discontinuity) |
| Op4 | Universal Pairwise Potential | $U(r) = -K/r\cdot(T^2 - \Gamma^2)$; $Z(r) = Z_0/(1-(d_{sat}/r)^2)^{1/4}$ | 190 | CANONICAL — explicit equation Vol 1 Ch 6 §1.4 + 3-regime table (Coulomb / nuclear-H-bond / Pauli) |
| Op5 | Multiport Y-to-S Conversion | $[S] = (I + [Y]/Y_0)^{-1}\cdot(I - [Y]/Y_0)$ | 225 | CANONICAL — explicit equation Vol 1 Ch 6 §1.5; applied at nuclear $K_{MUTUAL}$ eigenvalues, protein fold eigenstate, antenna S-parameters |
| Op6 | Universal Eigenvalue Target | $\lambda_{min}(S^\dagger S) \to 0$ | 242 | CANONICAL — explicit equation Vol 1 Ch 6 §1.6; ground-state condition (one mode perfectly absorbed) |
| Op7 | Universal Spectral Analyser | Spatial Fourier transform; $\alpha$-helix $k=N/3.6$, $\beta$-sheet $k=N/2$ | 252-264 | CANONICAL by description (no explicit formula in Vol 1 Ch 6 — DSP complement to time-domain SPICE; protein periodicity examples canonical at lines 257-260) |
| Op8 | Packing Reflection Coefficient | $\Gamma_{pack} = (R_g - R_{g,target})/(R_g + R_{g,target})$; $R_{g,target} = \sqrt{3/5}\cdot(3\cdot N\cdot V_{res}/(4\pi\cdot\eta_{target}))^{1/3}$; $\eta_{target} = P_C\cdot(1 - 1/N)$ | 282 | CANONICAL — explicit equation Vol 1 Ch 6 §1.8 (eq:rg_target + eq:gamma_pack); domain-agnostic application to protein globules + nuclear matter + fluid cavities |
| Op9 | Universal Steric Reflection | $\Gamma_{steric} \to -1$ (Pauli-level overlap → impedance divergence) | 299 | CANONICAL by description — Vol 1 Ch 6 §1.9 lists as "Pauli-level repulsion mapping overlap to an impedance divergence $\Gamma \to -1$"; explicit functional form distributed across vol_2 + vol_5 leaves |
| Op10 | Junction Projection Loss | $Y_{loss} \approx \sin^2(\theta)/\pi^2$ | 300 | CANONICAL — explicit equation Vol 1 Ch 6 §1.10; predicts $c=3$ invariant for $(2,3)$ torus knot per **[KB canonical: (2,3) Torus-Knot Uniqueness](../vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md)** + `extract_crossing_count` implementation in [`src/ave/topological/cosserat_field_3d.py:1468-1550`](../../../src/ave/topological/cosserat_field_3d.py) |
| Op11 | Topological Curl | $\nabla\times V$ (discrete Yee-lattice form) | 309 | CANONICAL by description — Vol 1 Ch 6 §1.11 names; "translates discrete network adjacency to continuous calculus"; computational |
| Op12 | Topological Divergence | $\nabla\cdot V$ (discrete Yee-lattice form) | 309 | CANONICAL by description — Vol 1 Ch 6 §1.11 names; computational |
| Op13 | D'Alembertian | $\Box^2$ (fully generalized wave equation operator) | 310 | CANONICAL by description — Vol 1 Ch 6 §1.12; uses local saturated $c_{eff}$ (not constant $c$) per Op16 |
| Op14 | Dynamic Impedance | $Z_{eff} = Z_0/\sqrt{S}$ | 311 | CANONICAL — explicit equation Vol 1 Ch 6 §1.13. **KB canonical references** (post-2026-05-16 promotion): [Lattice Impedance Decomposition](../vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md), [Op14 Local Clock Modulation](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md), [Op14 Cross-Sector Trading](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md) (empirical: $\rho(H_{cos}, \Sigma|\Phi_{link}|^2) = -0.990$ at Move 11b). Additional cross-citations: [vol_4 ch 13:338](../../vol_4_engineering/chapters/13_future_geometries.tex), [vol4 KB caustic-resolution lines 15+32](../vol4/advanced-applications/ch20-optical-caustic-resolution/index.md). Asymmetric Meissner case: $Z_{eff} = Z_0\cdot\sqrt{S_\mu/S_\varepsilon}$ distilled in [pair-production-axiom-derivation §6](../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) — different observable when $S_\mu \neq S_\varepsilon$ (Meissner-asymmetric magnetic-moment mechanism, also covered in [L3 closure synthesis §6](../vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md)). |
| Op15 | Virtual Strain Radius | $r_{virtual} = \sqrt{1 - \sigma(x)^2}$ | 312 | CANONICAL by description — Vol 1 Ch 6 §1.13 names; "links topological node count to spatial metric volumes"; explicit formula in doc 81 §2.2 — but only single citation. **SYNTHESIS-LABELED until ≥3 cross-citations land.** |
| Op16 | Universal Wave Speed | $c_{shear} = c_0\cdot\sqrt{S}$ | 317 | CANONICAL — Vol 1 Ch 6 §1.14 narrative ("Freezes wave propagation dynamically as $S \to 0$") + grep-verified explicit formula at ≥3 cross-citations: [vol_2 ch 7 line 1032 + lines 985-993](../../vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex) (label `eq:c_shear`), [axiom-homologation.md §208](axiom-homologation.md) (Ax 4 derived effects table: $c_{eff} = c_0\cdot S^{1/2}$), **[KB canonical: Op14 Local Clock Modulation](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md)** (substrate-native time-dilation via $\omega_{local} = \omega_{global}\sqrt{1-A^2}$; cross-volume parallel to gravitational $\tau_{local} = n(r)\tau_{unstrained}$). Gravitational analog: $c \cdot \sqrt{1-A^2} \equiv$ Schwarzschild $c \cdot \sqrt{1-r_s/r}$ in $r_s/r \ll 1$ limit. |
| Op17 | Power Transmission | $T^2 = 1 - \Gamma^2$ | 318 | CANONICAL — explicit equation Vol 1 Ch 6 §1.16; active energy transfer coefficient |
| Op18 | Coupled Frequency | $\omega_c = \omega_0/\sqrt{1 - \lambda k}$ | 319 | CANONICAL by description — Vol 1 Ch 6 §1.18 names; explicit formula in doc 81 §2.2 but SYNTHESIS-LABELED until ≥3 cross-citations |
| Op19 | Refractive Index | $n(r) = 1 + \nu_{vac}\cdot\varepsilon_{11}$ | 319 | CANONICAL — explicit equation Vol 1 Ch 6 §1.18 + cross-citations: [`eq_gravity_derived.tex`](../../common_equations/eq_gravity_derived.tex) (canonical Symmetric Gravity $n(r) = 1 + 2GM/(rc^2)$ form post-axiom-homologation), [Vol 3 Ch 3](../../vol_3_macroscopic/chapters/03_macroscopic_relativity.tex). $\nu_{vac} = 2/7$ (Poisson ratio: 2 compliance / 7 total modes) |
| Op20 | Regime Eigenvalue | (no canonical formula in Vol 1 Ch 6 — only "5-step regime-crossing scalar target") | 320 | **SYNTHESIS** — Vol 1 Ch 6 narrative only ("Defines the 5-step regime-crossing scalar target"). Formula $\omega_{regime} = \ell\cdot c_{wave}/r_{eff}$ appears ONLY in doc 81 §2.2 + the Round 10+ plan §3.4 — implementer-synthesis without canonical manuscript anchor. **A43 v10 instance flagged for auditor-lane post-closure bundle:** the synthesis-as-corpus framing of the Op20 formula in doc 81 + propagation into the Round 10+ plan needs verification or explicit synthesis-labeling at the source. Round 10+ Phase 1 Direction 3.4 observer pre-reg should label the formula as "synthesis from doc 81 + plan; canonical Vol 1 Ch 6 narrative does not specify" |
| Op21 | Quality Factor Phase Transition | $Q \sim 1/\ln(Z_1/Z_0)$ (Bardeen BCS mapping) | 321 | CANONICAL — Vol 1 Ch 6 §1.21 explicit formula; superconductivity threshold mechanism. Note: separately, $Q = \ell$ (lattice pitch in natural units) per doc 81 §2.2 — that's a different identification (Q-as-lattice-pitch) and may be the bootstrap / $\alpha = 1/137.036$ derivation, NOT the Bardeen mapping. Cross-reference needs auditor-lane confirmation |
| Op22 | Avalanche Factor | $M = 1/S^2 = 1/(1 - r^2)$ | 322 | CANONICAL — explicit formula at [`backmatter/appendix_c_derived_numerology.tex:78`](../../backmatter/appendix_c_derived_numerology.tex) + [`ave-kb/common/appendix-derived-numerology.md:50`](appendix-derived-numerology.md): "universal avalanche factor $M = 1/S^2 = 1/(1 - r^2)$ directly derives from Axiom 4 power conservation (effective pure 1D exponent of n=2)". Vol 1 Ch 6 §1.22 narrative confirms ("Captures nonlinear cascading metric yield"). **A43 v11 correction flagged:** doc 81 §2.2 gave $M = 1/(1 - S(V))$ which is a DIFFERENT formula ($1/(1-S)$ vs $1/S^2$); as $S \to 0$ these diverge differently (corpus → ∞, doc 81 → 1). Round 10+ Phase 1 Direction 3.5 observer pre-reg should use the canonical $M = 1/S^2$ formula, NOT doc 81's synthesis. Auditor-lane post-closure bundle should add as A43 v11 worked example |

---

## §3 — Implementation pointers

| Op | Implementation pointer (where engine code or test driver exists) |
|---|---|
| Op1 (Z) | [`src/ave/core/k4_tlm.py`](../../../src/ave/core/k4_tlm.py) `build_scattering_matrix(z_local)` at line 36 |
| Op2 (S) | Distributed across [`cosserat_field_3d.py:459`](../../../src/ave/topological/cosserat_field_3d.py) `_update_saturation_kernels` + [`k4_tlm.py:248-322`](../../../src/ave/core/k4_tlm.py) S_field state |
| Op3 (Γ) | Implicit in scatter+connect K4 dynamics; explicit Γ-curves in `_reflection_density` at [`cosserat_field_3d.py:266`](../../../src/ave/topological/cosserat_field_3d.py) |
| Op6 (λ_min) | Eigsolve drivers throughout `src/scripts/vol_1_foundations/r7_*` (V-block + Cos-block eigsolves at corpus GT) |
| Op10 (Y_loss / c=3) | `extract_crossing_count` at [`cosserat_field_3d.py:1468-1550`](../../../src/ave/topological/cosserat_field_3d.py) (Cosserat ω-field) + [`tlm_electron_soliton_eigenmode.py:567-640`](../../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py) (K4 V-field) |
| Op14 (Z_eff) | [`cosserat_field_3d.py:459`](../../../src/ave/topological/cosserat_field_3d.py) `_update_saturation_kernels` modulates per-cell impedance via $S(A)$ per Axiom 4 |
| Op16 (c_shear) | NOT YET implemented as observer; Round 10+ Phase 1 Direction 3.3 candidate |
| Op20 (ω_regime) | NOT YET implemented; Round 10+ Phase 1 Direction 3.4 candidate (formula synthesis-flagged per §2 above) |
| Op22 (M) | NOT YET implemented; Round 10+ Phase 1 Direction 3.5 candidate (use canonical $M = 1/S^2$ per §2 above) |

---

## §4 — Scale-invariance argument (summary)
<!-- claim-quality: clm-6mvtsf -->

Per Vol 1 Ch 6 §1.1 verbatim claim line 29-35: *"The characteristic impedance $Z = \sqrt{\mu/\varepsilon}$ is the single structural invariant of the AVE framework. No scale-specific modifications, fitting parameters, or domain-dependent redefinitions are required. Every physical phenomenon in the derivation chain reduces to boundary conditions on this single operator."*

The 22 operators inherit scale-invariance from Op1 ($Z$) by construction:
- Op2 ($S$) is a dimensionless ratio ($A/A_c$) — automatically scale-invariant
- Op3 ($\Gamma$) is a dimensionless ratio of impedances — Op1-derived, automatically scale-invariant
- Op4-22 compose Op1+Op2+Op3 with dimensionless coefficients — all inherit invariance

**Scale-invariance is the framework's distinguishing claim.** The same operator code path is called at vacuum lattice ($10^{-13}$ m), atomic ($10^{-10}$ m), molecular ($10^{-8}$ m), seismic ($10^6$ m), gravitational ($10^{26}$ m) — 14 orders of magnitude per Vol 1 Ch 6 line 15. The cross-scale table at lines 47-92 (Op1) + four-domain demonstration at lines 107-115 (Op2) + scale table at lines 133-144 (Op3) collectively anchor the claim. The Op1 Universal Impedance formula $Z = \sqrt{\mu/\varepsilon}$ itself is owned by [Vol 1 Ch 6 §6.1 Universal Impedance Operator](../vol1/operators-and-regimes/ch6-universal-operators/impedance-operator.md).

---

## §5 — A43 v10/v11 worked-example flags (auditor-lane post-closure bundle)

Two implementer-side A43 instances surfaced during Phase 0.2 grep-verification of operator formulas in this catalog. Numbering note: A43 v9 was the auditor-side atomic-orbital ladder wrong-directory grep instance landed earlier this session in the post-closure queue; v10 and v11 below are these two new implementer-side instances.

**A43 v10 — Op20 ω_regime formula synthesis-as-corpus:** doc 81 §2.2 + the Round 10+ plan §3.4 + this catalog §2 use $\omega_{regime} = \ell\cdot c_{wave}/r_{eff}$ as if canonical. Vol 1 Ch 6 §1.20 line 320 only specifies "Defines the 5-step regime-crossing scalar target" — no formula. The $\omega_{regime} = \ell\cdot c_{wave}/r_{eff}$ framing originated in doc 81 §2.2 implementer-synthesis from "regime eigenvalue" naming + ω-form analogy, NOT verbatim corpus. Synthesis-as-corpus per the lane-symmetric discipline. Correction: label as synthesis in operators.md §2 (DONE in this commit); flag in the Round 10+ plan §3.4 in-flight amendment; doc 81 §2.2 addendum; auditor-lane A43 v10 worked example.

**A43 v11 — Op22 formula different from canonical:** doc 81 §2.2 + the Round 10+ plan §3.5 + this catalog draft used $M = 1/(1 - S(V))$; canonical [`backmatter/appendix_c_derived_numerology.tex:78`](../../backmatter/appendix_c_derived_numerology.tex) gives $M = 1/S^2 = 1/(1 - r^2)$. As $S \to 0$, the formulas diverge differently: corpus → ∞ (avalanche actually cascades to infinity at saturation onset), doc 81 → 1 (no cascade). doc 81 synthesis was the wrong formula; corpus correct. Correction: use the canonical formula in operators.md §2 (DONE in this commit); fix in the Round 10+ plan §3.5 in-flight amendment; doc 81 §2.2 addendum; auditor-lane A43 v11 worked example.

Both worked examples extend the lane-symmetric pattern from 8 to 11 instances total cumulatively (six auditor-side + two implementer-side originally + three post-A43-v2 in queue: v9 auditor atomic-orbital + v10 implementer Op20 + v11 implementer Op22). Pattern continues empirically symmetric.

---

## §6 — Catalog provenance

This catalog is the canonical Phase 0.2 deliverable per the Round 10+ plan. The catalog enables:

- **Multi-operator signature observer work** (Phase 1) — Op14/16/20/22 formula citations canonical (Op14, Op16) or synthesis-flagged (Op20, Op22 doc-81-correction-applied)
- **Substrate-$(n,l,m_l)$ → K4 mapping work** (Phase 1) — Op6 (eigenvalue target → radial nodes $n_r$), Op10 ($c=3$ invariant → angular nodes $l$) canonical citations available
- **Per-pre-reg verification gate** — operators.md is the single-source-of-truth for cross-ref grep-verification at pre-reg freeze time

---

## §7 — References

- [`manuscript/vol_1_foundations/chapters/06_universal_operators.tex`](../../vol_1_foundations/chapters/06_universal_operators.tex) — canonical 22-operator catalog (primary anchor)
- [`manuscript/ave-kb/CLAUDE.md` INVARIANT-N3](../CLAUDE.md) — KB cross-cutting invariant naming (collision flagged in §1)
- [`manuscript/backmatter/appendix_c_derived_numerology.tex`](../../backmatter/appendix_c_derived_numerology.tex) — Op22 canonical formula
- [`manuscript/ave-kb/common/appendix-derived-numerology.md`](appendix-derived-numerology.md) — KB Op22 canonical formula
- [`manuscript/ave-kb/common/axiom-homologation.md`](axiom-homologation.md) — Ax 4 derived-effects table includes $c_{eff} = c_0\cdot S^{1/2}$ (Op16)
- [Vol 1 Ch 6 §6.1 Universal Impedance Operator](../vol1/operators-and-regimes/ch6-universal-operators/impedance-operator.md) — owns the Op1 $Z = \sqrt{\mu/\varepsilon}$ formula
- [Universal Saturation-Kernel Catalog](universal-saturation-kernel-catalog.md) — A-034 21-instance expansion of Op2
