[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.14 Phase Diagrams

> **🔴 G-ruling reconciliation (2026-06-15, Rule 12; KB-is-truth).** Per Grant's 2026-06-14 G-ruling ([`common/interlock-register.md`](../../common/interlock-register.md) `ilk-gravmb`), Newton's $G$ is **mixed**, not first-principles "derived": the Achromatic-Lens **FORM** is substrate-derived but the Machian-coupling **VALUE** is a calibration input ($\xi$ back-solved from CODATA $G$; flip-test mixed→real = Chain B$'$, 0 closed-form candidates). The "Machian G is DERIVED" framings below are reframed to **mixed** in place — **NOT** "echo" (the derived-form half stands). Prior wording preserved per Rule 12.

Chapter 14 of the Vol 9 datasheet documents the substrate's two principal phase-organization axes: (1) the **operating-point axis** — the Axiom 4 universal saturation kernel $S(r) = \sqrt{1 - r^2}$ partitioned into Regime I (linear) / II (nonlinear / saturating) / III (yield / avalanche) / IV (ruptured) per the canonical four-regime map; (2) the **cosmic axis** — substrate cosmological phase organized into standard cosmic phase (bulk substrate at $r \ll 1$ at $T_{CMB}$ with $\delta_{strain}$ thermal asymmetry), ruptured-plasma phase (BH interior locally in Regime IV, **single-medium substrate, NOT a separate sublattice**), and cosmic-genesis phase (post-$\hat{\Omega}_{freeze}$ single-seed lattice-genesis crystallization state). The chapter consolidates the canonical $r_1 = \sqrt{2\alpha}$ / $r_2 = \sqrt{3}/2$ (spin-2 sector) / $r_3 = 1$ regime boundaries, the canonical 8-substrate-domain phase mapping (electromagnetic / gravitational / BCS / magnetic / nuclear / GW / galactic-rotation), and the EE phase-diagram translation (semiconductor I-V / varactor C-vs-V / Stribeck-curve tribology / cavity-QED coupling regimes) into datasheet phase-diagram format.

The chapter content is **Class B/C synthesis** per `consistency-vs-emergence` v1.3 — no new substrate-physics primitives are introduced; the content consolidates the canonical Vol 1 Ch 7 four-regime map + Vol 3 cosmology canonical leaves into datasheet Phase-Diagram format. Vol 9 visual representation note: datasheet phase diagrams are figures. Ch 14 generates the canonical **true thermodynamic phase diagram** figure (`true_phase_diagram.pdf`, the $(T \times \bar\rho)$ plane bounded by the melt line $T_{melt}$ and the candidate cavitation line $\bar\rho_{cav}$; manuscript `chapters/14_phase_diagrams.tex` §True Phase Diagram, regenerated from canonical constants by `figures/gen_true_phase_diagram.py` with no hardcoded observable target), alongside phase-state tables; other Vol 9 chapters wire driver-emitted figures (e.g. the Ch 5 CVR six-view sweep, the Ch 7 Axiom-4 quarter-arc kernel plot). Figures are in scope wherever a driver emits a re-runnable plot.

## Framing constraints preserved verbatim

The chapter preserves the framework's canonical phase-organization framing without modification:

- **Operating-point regime partition is substrate-natural** — the substrate's natural response to operating point along the Axiom 4 kernel; engineering observes regime transitions empirically (varactor C-V, semiconductor I-V, avalanche photodiode gain); AVE derives Regime I-IV from Ax 4 alone. **NO "engineered phase diagram."**
- **Lattice-genesis single-seed cosmology** — the observable universe emerged from a single chiral seed crystallizing under $\hat{\Omega}_{freeze}$. **NO multiverse; NO multiple universes; NO baby-universe black holes with daughter cosmologies.**
- **BH interior = ruptured-plasma phase** — substrate locally in Regime IV at cosmological strain; shear modulus phase-transitions $G_{shear} \to 0$. **SUBSTRATE SINGLE-MEDIUM THROUGHOUT — RUPTURED-PLASMA, NOT a separate B-sublattice; NOT a daughter cosmology; NOT an inner cosmic genesis.**
- **Machian G is MIXED** (G-ruling 2026-06-14, `ilk-gravmb`) — gravity's **FORM** is the derived Machian boundary impedance (Ax 1 + Ax 4 SYM scaling), NOT a primitive axiom; but $G$'s **VALUE** is calibration-fitted ($\xi$ back-solved from CODATA $G$; Chain B$'$ open). NOT "echo" — the derived-form half stands. (Used in cosmic-phase framing throughout; canonical at Vol 9 Ch 12.)
- **Substrate is single-medium** — the eight-row substrate-domain phase mapping is the same Ax 4 kernel projected onto distinct domain-specific control parameters; engineering observes domain-specific transitions; AVE derives every $A_c$ from the four axioms.

## Primary canonical sources

| Source | Content |
|---|---|
| [`vol1/operators-and-regimes/ch7-regime-map/four-regimes.md`](../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) (`clm-2dwzib`, `clm-b2anl4`) | Canonical four-regime $r = A/A_c$ partition; first-principles derivation of $r_1 = \sqrt{2\alpha}$ (sub-$\alpha$ resolvability), $r_2 = \sqrt{3}/2$ (spin-2 avalanche-onset), $r_3 = 1$ (Ax 4 rupture); sector-dependence treatment (scalar / vector / spin-2); semiconductor analog mapping; Miller multiplication $M = 1/S^2$ identity |
| [`vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md`](../../vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md) (`clm-82dxbj`) | Canonical 8-substrate-domain control-parameter catalog: electromagnetic (dielectric + field strength) / gravitational / BCS / magnetic / nuclear / GW / galactic rotation; representative operating-point locations in Regime I-IV per domain; galactic-rotation = Regime III→IV transition (substrate-mechanism of MOND scaling) |
| [`common/omega-freeze-cosmic-grain-cascade.md`](../../common/omega-freeze-cosmic-grain-cascade.md) (`clm-dsb560`, `clm-a7cbqq`) | Cosmic-genesis $\hat{\Omega}_{freeze}$ mechanism; phase-transition-while-spinning single-seed lattice-genesis crystallization; bond over-bracing $u_0 = u_0^*$ frozen-in; right-handed $I4_1 32$ chirality selection at genesis; CMB axis-of-evil empirical pin |
| [`vol3/gravity/ch03-macroscopic-relativity/dielectric-rupture-event-horizon.md`](../../vol3/gravity/ch03-macroscopic-relativity/dielectric-rupture-event-horizon.md) (`clm-ir8h78`) | Cosmological-scale substrate rupture canonical leaf: Schwarzschild radius = dielectric-saturation boundary; BH interior locally in Regime IV; $G_{shear} \to 0$ phase transition |
| [`vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (`clm-hp7nlm`) | Standard cosmic phase canonical $\delta_{strain}$ at $T_{CMB}$; Cosserat-rotation-sector mass-gap thermal-mode-population ASYM mechanism |
| [`vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md`](../../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) (`clm-s4n33u`) | Asymptotic de Sitter equilibrium $\rho_\Lambda$ closure (next cosmological phase transition predicted by framework) |
| [`common/universal-saturation-kernel-catalog.md`](../../common/universal-saturation-kernel-catalog.md) (`clm-gz7ryg`, `clm-dxdsvt`, etc.) | A-034 universal saturation-kernel catalog: same Ax 4 kernel governs all 26 cross-scale topological-reorganization events including cosmic-scale lattice-genesis crystallization phase transition |
| [`common/translation-tables/translation-circuit.md`](../../common/translation-tables/translation-circuit.md) (`clm-eemap1`); line 133 | EE-substrate-native META framework; canonical entry "Black-hole-interior ruptured plasma → Plasma physics" (substrate single-medium throughout; ruptured-plasma framing canonical at line 133) |
| [`common/temporal-saturation-regime-classifier.md`](../../common/temporal-saturation-regime-classifier.md) | Orthogonal temporal axis (lossless / cyclic / lossy) layered on top of Regime I-IV operating-point partition; how the substrate evolves THROUGH regimes per observation window |
| [`vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md`](../../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) (`clm-ezai5b`) | Regime III→IV transition substrate-mechanism: Schwinger pair production as saturated flux-tube rupture (4-piece synthesis used in cross-phase-transition section) |
| CLAUDE.md INVARIANT-S2 | Axiom 4 universal saturation kernel verbatim; operating-point gauge-relativity statement; two effective wave speeds discipline ($c_{EM}$ vs $c_{shear}$); SYM-class α-invariance; cosmic-genesis canonical framing |

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/14_phase_diagrams.tex` (canonical Vol 9 chapter file; populated in this PR).

## Cross-chapter dependencies within Vol 9

- **Ch 2 (Absolute Maximum Ratings)** catalogs $V_{snap}$ as the substrate-rupture absolute rating (the $r_3 = 1$ phase boundary numerical limit at the dielectric-sector projection); Ch 14 catalogs the cross-phase-transition boundaries themselves.
- **Ch 6 (Temperature Characteristics)** carries the standard-cosmic-phase $\delta_{strain}$ at $T_{CMB}$ canonical content; Ch 14 catalogs the standard cosmic phase as one of three cosmic phases.
- **Ch 7 (Saturation Characteristics)** carries the full Regime I + II characteristic-curves treatment + the Axiom 4 kernel statement; Ch 14 consolidates the regime partition into phase-diagram format with pointer to Ch 7 for the full treatment.
- **Ch 8 (Breakdown Characteristics)** carries the Regime III Miller-multiplication identity + Regime IV Schwinger substrate-mechanism + cosmological breakdown reference; Ch 14 catalogs the Regime III→IV cross-phase transition with pointer to Ch 8 for the substrate-mechanism.
- **Ch 12 (Cosmological Characteristics)** carries the cosmic-genesis $\hat{\Omega}_{freeze}$ mechanism + lattice-genesis single-seed framing + BH-interior ruptured-plasma framing + Machian-G form-derivation (value mixed/calibration-fitted; `ilk-gravmb` — see Ch 12); Ch 14 catalogs the cosmic phase diagram with pointers to Ch 12 for the substrate-physics.

## Cross-volume canonical-derivation pointers

- Vol 1 Ch.~7 — four-regime map + 8-domain catalog (canonical regime partition + domain-to-regime mapping).
- Vol 1 Ch.~1 Axiom 1 — K4 $I4_1 32$ chiral space group canonical statement; substrate single-medium identity.
- Vol 1 Ch.~8 `ch8-alpha-golden-torus.md` (`clm-0ktpcn`) — magic-angle operating point $u_0^*$ at which the cosmic-genesis phase locked the substrate's Golden Torus geometry.
- Vol 2 Ch.~1 topological matter — Regime IV Schwinger pair-production substrate-mechanism (Regime III→IV transition).
- Vol 3 Ch.~1 gravity and yield — SYM-class α-invariance canonical proof (`clm-3zz0f6`).
- Vol 3 Ch.~3 macroscopic relativity — Schwarzschild $r_s$ as substrate dielectric-rupture boundary (cosmological-scale Regime IV instance).
- Vol 3 Ch.~4 generative cosmology — $\hat{\Omega}_{freeze}$ + $H_\infty$ + lattice-genesis framework (cosmic-genesis phase canonical leaf).
- Vol 3 Ch.~5 dark sector — $\delta_{strain}$ at $T_{CMB}$ + $\rho_\Lambda$ closure (standard cosmic phase + asymptotic equilibrium).
- Vol 3 Ch.~15 black-hole orbitals — BH-interior phase-transition canonical entries; QNM spectrum at $\omega_R M_g = 18/49$.

---
