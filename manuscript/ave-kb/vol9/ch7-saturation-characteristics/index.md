[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.7 Saturation Characteristics

Chapter 7 of the Vol 9 datasheet documents the Axiom 4 universal saturation kernel $S(A_0) = \sqrt{1 - (A_0/A_{yield})^2}$ as the substrate primitive governing every cross-scale saturation event in the natural vacuum. The chapter consolidates: (1) the verbatim Axiom 4 statement from `manuscript/common_equations/eq_axiom_4.tex` (single source of truth); (2) the dielectric specialization at atomic and bench scale — $\varepsilon_{eff} = \varepsilon_0 S$, $\mu_{eff} = \mu_0 S$, $C_{eff} = C_0/S$ — with the two effective wave speeds $c_{EM}(A_0) = c_0/S$ and $c_{shear}(A_0) = c_0\sqrt{S}$ called out explicitly per INVARIANT-S2 Pitfall #5 discipline; (3) the operating-point characteristic-curve table at canonical $r$ values from $r = 0$ through rupture; (4) the four-regime map (Small-Signal / Large-Signal / Avalanche / Breakdown) with semiconductor analog; (5) the PONDER-05 bench observation (27.4% quartz $\varepsilon_{eff}$ collapse at ~30 kV) as a **material-scale consistency analog of the kernel SHAPE** — NOT a vacuum-kernel falsifier; "$V_{DC}/V_{yield} = 0.687$ at 30 kV" reads the apparatus voltage as the **per-node** ratio (vacuum per-node $A_0 = 10^{-7}$–$10^{-10}$ at 30 kV; `vol4/claim-quality.md:51`; vacuum falsifier is facility-class $\sim 8\times10^{16}$ V/m); (6) cross-reference to the A-034 universal saturation-kernel catalog at 26 instances spanning 21 orders of magnitude; (7) the EE saturation translation table (varactor / Miller multiplication / op-amp slew rate / core saturation / non-linear telegrapher) → Axiom 4 substrate primitive.

The chapter is a **synthesis chapter** per Vol 9 charter — no substrate primitive is re-derived. All derivations live in the cited canonical leaves; the chapter consolidates them into datasheet format.

## Primary canonical sources

- **Axiom 4 canonical statement (verbatim source of truth):** [`manuscript/common_equations/eq_axiom_4.tex`](../../../common_equations/eq_axiom_4.tex); INVARIANT-S2 mirror at [`manuscript/ave-kb/CLAUDE.md`](../../CLAUDE.md).
- **Universal saturation-kernel catalog (A-034, 26 instances / 21 orders of magnitude):** [`common/universal-saturation-kernel-catalog.md`](../../common/universal-saturation-kernel-catalog.md) (`clm-gz7ryg`, `clm-dxdsvt`, `clm-hvvvop`, `clm-5fu303`, `clm-l4o7hv`).
- **Four-regime map (regime boundaries from first principles):** [`vol1/operators-and-regimes/ch7-regime-map/four-regimes.md`](../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) (`clm-2dwzib`, `clm-b2anl4`).
- **Axiom-definitions in-chapter restatement:** [`vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`](../../vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) (`clm-3kzmt9`, `clm-dfaiwj`).
- **$\alpha$-invariance under SYM-class scaling (canonical proof):** [`vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md`](../../vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) (`clm-3zz0f6`).
- **PONDER-05 substrate-physics anchor ($P(\delta V)$ shape function, Phase 0c + Phase 2-NA):** [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md).
- **PONDER-05 operating-point statement (quartz 27.4% at ~30 kV — consistency-class material analog, NOT a vacuum-kernel reading; "$V_{DC}/V_{yield} = 0.687$" is a per-node ratio):** [`vol4/falsification/ch11-experimental-bench/measurement-hierarchy-snr.md`](../../vol4/falsification/ch11-experimental-bench/measurement-hierarchy-snr.md):66.
- **PONDER-05 divergence-test matrix row (B7-PONDER-05):** [`common/divergence-test-substrate-map.md`](../../common/divergence-test-substrate-map.md).
- **EE saturation translation (ideal-lattice ↔ engineering-corrections):** [`common/translation-tables/translation-circuit.md`](../../common/translation-tables/translation-circuit.md) §9 (`clm-eemap1`).
- **ASYM-class substrate-distinct $\alpha$-modulation mechanism:** [`vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (`clm-hp7nlm`).

## Catalog-cardinality note (canonical)

The Axiom 4 kernel governs **26 canonical cross-scale instances** per the canonical catalog at [`universal-saturation-kernel-catalog.md`](../../common/universal-saturation-kernel-catalog.md): 17 physical-substrate canonical + 2 biological-substrate + 5 engineered-substrate + 2 physical-substrate companion rows scoped for Sessions 4/5. The Vol 0 backmatter chapter and [`eq_axiom_4.tex`](../../../common_equations/eq_axiom_4.tex) cite the physical-substrate-only subset as **19 cross-scale topological-reorganization events** (17 canonical + 2 scoped). Both counts are correct at their respective scopes; cross-scale span is **21 orders of magnitude** uniformly (atomic ∼ $10^{-15}$ m to cosmic ∼ $10^{26}$ m).

## Miller avalanche exponent — 1D vs 3D-corrected (canonical)

The substrate Miller multiplication identity $M(r) = 1/S(r)^2 = 1/(1-r^2)$ is the **1D Miller
form** (semiconductor avalanche-multiplication law $M = 1/(1-(V_R/V_{BR})^n)$ at exponent $n=2$).
The **3D-corrected macroscopic exponent** is `AVALANCHE_N_3D = 2(1 − ν_vac/3) = 38/21 ≈ 1.8095`
(`src/ave/core/constants.py:336`), where $ν_{vac}=2/7$ is the vacuum Poisson ratio: the 3D
solid-angle correction to the carrier-multiplication geometry softens the 1D $n=2$ to $n≈1.81$.
Both forms are canonical at their respective scopes — the $n=2$ 1D form for the bond-line
(per-channel) avalanche, the $n=38/21$ 3D-corrected form for the bulk macroscopic avalanche.

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/07_saturation_characteristics.tex` (populated Vol 9 PR-E sub-PR — Ch 7 buildout).

## Engine-acceptance suite coverage (Axiom-4 kernel gate, GREEN 2026-06-16/17)

The saturation kernel S(A)=√(1−(A/A_yield)²) this chapter specifies is verified
directly as an L0 constitutive gate by the engine-acceptance suite's **A4** test
(`src/tests/engine_acceptance/test_l0_axioms.py:555`, `sup-2qja9z` → `clm-gz7ryg`,
`clm-8nkvwy`, wired in [`../ch17-engine-requirements/engine-acceptance-suite.md`](../ch17-engine-requirements/engine-acceptance-suite.md)):
the quarter-arc identity, the EM projection (ε_eff=ε₀S, μ_eff=μ₀S, c_EM=c₀/S, Z_EM=Z₀),
and the canonical longitudinal c_eff²=c₀²/S all to <1e-12, with cold limit S(0)=1 and the
stiffening wall as A→A_yield. The L2 operating-point manifestations (T2.1 c_EM, T2.3 ASYM
mirror) ride the SAME kernel.

**S^(1/4)-vs-S^(1/2) exponent flag — RESOLVED 2026-06-17.** The refractive-index exponent
defect (legacy `S**0.25`) is resolved in favor of the **physical `S**0.5`**: the engine now
returns `n_EM = c₀/c_eff = S(A)^(+1/2)` (`master_equation_fdtd.py:167-170`, `return S**0.5`)
and `n_shear = S(A)^(−1/2)` (`:173-178`), consistent with the kernel anchor `c_eff²=c₀²/S`
(`:148-151`) — the in-code comment at `:160-161` records the legacy `S^{1/4}` as a now-corrected
exponent defect. The canonical wave-speed form is **c_shear = c₀√S** (= S^(1/2); matter/group/
rest-mass speed), and `c_EM = c₀/S`. The flag is closed (no longer a physics-review item).

## Volume-scope classification

Per Vol 9 charter (synthesis volume; no primary derivations), this chapter's content is Class B (synthesis consolidation of canonical content) per `consistency-vs-emergence` v1.3. No emergence-class claims; no new substrate primitives proposed. All numerical entries in the chapter's characteristic-curve table derive directly from $S(r) = \sqrt{1 - r^2}$ at cold-lattice limit with no corrections; the table is a definitional identity of the kernel, not a measurement or emergence test.

---
