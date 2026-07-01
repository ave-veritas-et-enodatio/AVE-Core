[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.13 Application Examples

<!-- [2026-06-15 reconciliation, Rule 12; KB-is-truth]: per the 2026-06-14 rulings, this leaf's G/α framings were relabeled in place -- "Electron LC tank -> α derivation" (table) -> "α closed-form identification (Class-B, retained input)"; "Machian-G closed form" (table) -> "(mixed: derived form, calibration-fitted ξ value; ilk-gravmb)"; "Machian G is DERIVED" (carry-forward bullet) -> "MIXED" (NOT echo). Qualifications, not deletions; prior wording recoverable at origin/main. -->

Chapter 13 of the Vol 9 datasheet is the cross-chapter integration map. Each application example invokes 3–5 substrate primitives from Chs.~2–12 and walks the substrate-mechanism chain from primitives to engineering observable. No new substrate-physics is introduced here; every derivation lives at canonical leaves cited inline.

> **Navigation note.** This index hosts no claims of its own; it is a navigation pointer into the canonical leaves the chapter cites. The five application examples in the manuscript counterpart each reference an existing canonical claim chain — `clm-0ktpcn` (α cold-lattice closure), `clm-3zz0f6` (SYM-class α-invariance), `clm-5zuo7g` (W/Z evanescent-cutoff derivation), `clm-ldmvwi` (Born-rule $p=2$ derivation), `clm-hp7nlm` (Cosserat-Curie thermal-asymmetry mechanism). Reader navigation begins at one of those leaves; this index lists the cross-references.

## Application examples landed in Ch.13

| Example | Substrate primitives invoked | Cross-chapter chain | Canonical leaves |
|---|---|---|---|
| Electron LC tank → α closed-form identification (Class-B, retained input) | $(2,3)$ Clifford-torus winding, $0_1$ unknot, $L_{cell}/C_{cell}/Z_0$, $\xi_{topo}$, Ax~3 minimum reflection ($\Gamma=-1$ TIR), $u_0^*$ magic angle | Ch~3 + Ch~4 + Ch~7 + Ch~11 + Ch~12 → cold-lattice $\alpha^{-1}_{ideal} = 4\pi^3 + \pi^2 + \pi$ via codimensional mode-count assembly at the Golden-Torus geometry | [`vol1/ch8-alpha-golden-torus.md`](../../vol1/ch8-alpha-golden-torus.md) (`clm-0ktpcn`) — Theorem 3.1 closure; [`vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md`](../../vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md) — $(2,3)$ uniqueness |
| Schwarzschild + Machian $G$ as gradient-index TL | $G_{vac}$, $K=2G$, $\nu_{vac}=2/7$, $c_{EM}$ vs $c_{shear}$ (Pitfall \#5), SYM-class $\alpha$-invariance, Machian-G closed form (mixed: derived form, calibration-fitted $\xi$ value; `ilk-gravmb`) | Ch~3 + Ch~7 + Ch~9 + Ch~12 → $c_{group} = c_0\sqrt{1-r_s/r}$ + exact $\alpha$-invariance + $G = c^4/(7\xi T_{EM})$ (form derived; $\xi$ from CODATA $G$) | [`vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md`](../../vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) (`clm-3zz0f6`); [`common/full-derivation-chain.md`](../../common/full-derivation-chain.md) (`clm-9oazz0`); [`common/trampoline-framework.md`](../../common/trampoline-framework.md) §5.5 (Machian bulk integral) |
| $W$/$Z$ gauge bosons → transformer-leakage cutoff modes | $\gamma_c$ Cosserat couple-stress, $l_c = \sqrt{\gamma_c/G_{vac}}$ weak-force range, Perpendicular Axis Theorem at bond cylinder $J=2I$, $\nu_{vac}=2/7$ | Ch~9 + Ch~10 + (Ch~15 joint kill-switch) → $m_W/m_Z = \sqrt{7}/3 ≈ 0.882$ + $\sin^2\theta_W = 2/9$ + below-cutoff Yukawa | [`vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md) (`clm-5zuo7g`); [`common/trampoline-framework.md`](../../common/trampoline-framework.md) line~188 (rotation-sector mass-gap $m_\omega$) |
| Born-rule $p=2$ as boundary-Joule extraction at $\Gamma$ port | Op3 $\Gamma$, Ax~3 minimum reflection, Op17 $T^2 = 1-\Gamma^2$, $V^2/Z_{det}$ Joule kinematics, Ax~4 amplitude statistics + cumulant truncation | Ch~3 + Ch~4 + Ch~7 → $\Pr \propto \|\psi\|^2$ as quadratic-in-amplitude boundary-Joule extraction-rate scaling | [`vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md`](../../vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md) (`clm-ldmvwi`); [`common/translation-tables/translation-qm.md`](../../common/translation-tables/translation-qm.md) Section B; [`common/translation-tables/translation-circuit.md`](../../common/translation-tables/translation-circuit.md) (`clm-eemap1`) |
| $\delta_{strain}$ as cosmic-scale TCC | Bipartite thermal-mode structure (E gapless / B mass-gapped), $\omega_m^2 = 4G_c/I_\omega$, asymmetric thermal occupation at $T_{CMB}$, $c_{EM}$ vs $c_{shear}$ split, ASYM-class $\alpha$-invariance void | Ch~3 + Ch~4 + Ch~5 + Ch~6 + Ch~10 → $\delta_{strain}(T_{CMB}) \approx 2.225\times10^{-6}$ + forward-prediction linear $\alpha$-drift at higher cosmic $T$ | [`vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (`clm-hp7nlm`); [`common/translation-tables/translation-circuit.md`](../../common/translation-tables/translation-circuit.md) §9 (TCR/TCC engineering-correction row) |
| Electron node as a 2-domain N-port (session add) | EM-port $Z_0 = 376.73\,\Omega$ ($\Gamma_{EM}=0$, sole external) + shear-port = charge + bulk-port = mass (both $\Gamma\to-1$ confined); EM-$\Omega$↔mechanical-$\rho c$ TKI-transformer; $\alpha$ localizes to the transducer $p_c = 8\pi\alpha$; Fork-A conservative shear↔bulk coupling | Ch~3 (node model) + Ch~4 ($Z_0$) + Ch~9 (bulk=mass) + Ch~10 (shear=charge, circulator/gyrator) → the electron drawn as one EM port + two confined mechanical ports bridged by a units-changing transducer | [`vol9/ch3-pin-port-configuration/device-circuit-models.md`](../ch3-pin-port-configuration/device-circuit-models.md) §6 (graded network, $\mathcal{M}/\mathcal{J}/\mathcal{Q}$ honest map, Fork-A); `src/scripts/vol_9_device/node_2domain_nport.py` (PR #320); `research/2026-06-20_node-circulator-coupling.md` (PR #321) |

## Discipline classifications

Per `consistency-vs-emergence` v1.3 + `ave-discrimination-check`:

- α derivation: Class~B substrate-mechanism mapping for the cold-lattice asymptote (a named geometric identification, canonical at `clm-0ktpcn`); δ_strain correction is Class~B at PARTIAL band (`clm-hp7nlm`, solidity ~0.55), with Q-DELTA-MAP-1-quant (the magnitude-derivation route) CLOSED NEGATIVE (FT-1 2026-05-31) — the δ_strain magnitude is a definitional residual, SIGN-only
- Schwarzschild + Machian G: Class~B substrate-mechanism mapping for gravitational time dilation; SM-counterfactual is GR with posited $G$; three-route $u_0^*$ convergence is substrate-distinct (canonical `clm-dsb560`)
- W/Z transformer-leakage: Class~B substrate-mechanism mapping; SM-counterfactual is Higgs-vev mechanics; right-handed neutrino joint kill-switch is substrate-distinct (canonical `clm-gw2wgc`)
- Born rule: Class~D emergence-class derivation of the $p=2$ exponent from substrate primitives (canonical `clm-ldmvwi`, master-equation-derivation-path closed Phase 2-A); SM-counterfactual is Born rule as postulate
- δ_strain: Class~B substrate-mechanism class identified, SIGN predicted (`clm-hp7nlm`); SM-counterfactual is QED with no thermal $\alpha$-running mechanism at CMB photon-bath occupation — but the quantitative magnitude derivation $\eta_\varepsilon(T)$ (Q-DELTA-MAP-1-quant) was CLOSED NEGATIVE (FT-1 2026-05-31: ~31 OOM undershoot, AND generic-thermal not AVE-distinct), so the magnitude is a definitional residual
- Node 2-domain N-port: Class~C CONSISTENCY re-expression of the three-impedance law as a wired equivalent-circuit MODEL (originates no new substrate primitive; `device-circuit-models.md` §6 classification). The EM↔mechanical TKI-transformer is `status:proposed` (not ratified); $\alpha = p_c/8\pi$ at the transducer is a consistency identity, NOT an $\alpha$ derivation; the Fork-A shear↔bulk coupling is PARTIAL (form forced, non-reciprocity magnitude imposed-echo). FLAG the proposed/PARTIAL status — do not present as solved.

## Carry-forward framings (preserved verbatim per chapter discipline)

- **Lattice-genesis single-seed cosmology** — single-seed *within our cosmic horizon* (one seed event, not many simultaneous disjoint seeds; NOT a claim ours is the only universe). Ch.~\ref{ch:vol9_cosmological_characteristics}~§\ref{sec:vol9_cosmo_lattice_genesis} in the manuscript.
- **BH interior = Regime IV ruptured plasma** (NOT a B-sublattice; single-medium). A melted interior **can** re-crystallize into a **daughter cosmology** — nested parent/daughter cosmologies across $\Gamma=-1$ melt→recrystallize boundaries are **permitted** (our own universe is a daughter; [`common/omega-freeze-cosmic-grain-cascade.md`](../../common/omega-freeze-cosmic-grain-cascade.md)). Ch.~\ref{ch:vol9_cosmological_characteristics}~§\ref{sec:vol9_cosmo_substrate_rupture}.
- **Machian $G$ is MIXED** (G-ruling 2026-06-14, `ilk-gravmb`) — form-derived (the Achromatic-Lens), value-fitted ($\xi$ back-solved from CODATA $G$; Chain B$'$ open); canonical at `common/full-derivation-chain.md` `clm-9oazz0`; not a primitive axiom. NOT "echo" — the derived-form half stands. *(Mirrors the §-20 table row + 13.tex; the high-salience row was reconciled first, this carry-forward bullet follows per the parallel-site gate.)*
- **$\nu_{vac} = 2/7$ is Ax~1 LC + Ax~2 α interlink** (canonical at `vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md` `clm-x19btt`; NOT promoted to fundamental axiom).
- **$c_{EM}$ vs $c_{shear}$ distinction** (CLAUDE.md INVARIANT-S2 Pitfall \#5); the α formula uses $c_{EM}$, Schwarzschild reduction uses $c_{shear}$.

## Primary canonical sources (cross-references)

- [`vol1/ch8-alpha-golden-torus.md`](../../vol1/ch8-alpha-golden-torus.md) — Theorem 3.1 cold-lattice α closure (`clm-0ktpcn`); $\alpha^{-1}_{ideal} = 4\pi^3 + \pi^2 + \pi$ codimensional mode-count assembly
- [`vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md`](../../vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) — SYM-class $\alpha$-invariance proof (`clm-3zz0f6`)
- [`vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md) — W/Z evanescent-cutoff derivation (`clm-5zuo7g`, `clm-q8un7j`)
- [`vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md`](../../vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md) — Born-rule $p=2$ derivation (`clm-ldmvwi`)
- [`vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) — Cosserat-Curie thermal-asymmetry mechanism (`clm-hp7nlm`)
- [`common/translation-tables/translation-circuit.md`](../../common/translation-tables/translation-circuit.md) — EE-as-substrate-native META framework (`clm-eemap1`, `clm-fy05jc`)
- [`common/translation-tables/translation-qm.md`](../../common/translation-tables/translation-qm.md) — Section B measurement-as-boundary-extraction vocabulary
- [`common/full-derivation-chain.md`](../../common/full-derivation-chain.md) — canonical closed-form for $G$ + Machian-hierarchy coupling $\xi$ (`clm-9oazz0`)
- [`common/trampoline-framework.md`](../../common/trampoline-framework.md) — Cosserat rotation-sector mass-gap line~188; Machian-G bulk integral §5.5
- [`common/omega-freeze-cosmic-grain-cascade.md`](../../common/omega-freeze-cosmic-grain-cascade.md) — three-route $u_0^*$ falsification framework (`clm-dsb560`)

## Cross-Chapter Citation Map

The manuscript chapter ends with a tabular cross-chapter citation map (`sec:vol9_app_cross_chapter_citation_map`) listing each application example × Vol 9 chapter whose primitives the example invokes. Chapters not in the header row (Ch~2 absolute maximums, Ch~8 breakdown, Ch~14 phase diagrams, Ch~15 falsification tests) appear in individual examples as cross-references to rupture-boundary refs, Regime IV BH-interior framing, four-regime phase locations, and bench / observational kill-switch tests for each substrate-mechanism chain.

## Manuscript counterpart

[`manuscript/vol_9_vacuum_datasheet/chapters/13_application_examples.tex`](../../../../vol_9_vacuum_datasheet/chapters/13_application_examples.tex)

---
