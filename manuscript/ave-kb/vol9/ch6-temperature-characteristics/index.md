[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.6 Temperature Characteristics

Chapter 6 of the Vol 9 datasheet documents the substrate's natural thermal behavior under the **Cosserat-rotation-sector mass-gap thermal-mode-population ASYM** mechanism (canonical at `clm-hp7nlm`). The substrate's bipartite K4-node DOF structure (3 translational E-DOFs + 3 microrotational B-DOFs per Ax 1) produces an asymmetric thermal-mode population at finite $T$: E-modes thermally populated at any $T > 0$; B-modes mass-gap-frozen below the substrate Cosserat-Curie temperature $T_{B-gap} = \hbar\omega_m/k_B \sim 10^{10}$ K. This substrate-mechanism asymmetry drives a finite $\delta_{strain}$ even in the canonical SYM-class limit, producing both the cosmic-scale CMB-thermal-running of $\alpha^{-1}$ AND the engineering-scale TCC / TCR / TC$\mu$ catalog characterized on every component datasheet across decades.

The chapter consolidates: the Cosserat-Curie thermal-asymmetry mechanism (cosmic-scale $\delta_{strain} \approx 2.225 \times 10^{-6}$, $\eta_\varepsilon \approx 4.45 \times 10^{-6}$); the per-parameter temperature-coefficient spec table at $T_{CMB}$; the Johnson-Nyquist thermal-noise floor as substrate-native EE observable of the same thermal-mode population; the operating-temperature-range boundaries ($T_{B-gap}$ above; cold-lattice $T \to 0$ below; $T_{melt}$ Regime IV pair-production threshold); and the EE-translation catalog mapping TCC / TCR / TC$\mu$ / Curie-temperature / Johnson-Nyquist vocabulary back to the single Cosserat-Curie substrate primitive.

## Primary canonical sources

- [`ave-kb/vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (`clm-hp7nlm`) — Cosserat-rotation-sector mass-gap thermal-mode-population ASYM canonical leaf; substrate-mechanism derivation of $\delta_{strain}$ at $T_{CMB}$; landed via PR #54 on 2026-05-28. **Class B substrate-mechanism manifestation at solidity 0.55 PARTIAL band — NOT promoted in this chapter**; the candidate quantitative substrate-statistical-mechanics derivation of $\eta_\varepsilon$ (Q-DELTA-MAP-1-quant) was **CLOSED NEGATIVE** (FT-1, 2026-05-31: ~31 OOM undershoot, generic-thermal not AVE-distinct), so the δ_strain magnitude is a **definitional residual** — only the SIGN is substrate-set.
- [`ave-kb/common/translation-tables/translation-circuit.md`](../../common/translation-tables/translation-circuit.md) §9 (Ideal Lattice ↔ Engineering Corrections) — engineering-correction catalog mapping the Cosserat-Curie mechanism to EE-vocabulary observables (TCC of ceramic capacitors; TC$\mu$ of inductor cores; TCR; TC$V_F$; Curie temperature of ferrites; Johnson-Nyquist noise floor; etc.).
- **CLAUDE.md INVARIANT-S2** — Ax 1 six-DOF bipartite-mode structure + two-effective-wave-speeds discipline ($c_{EM}$ vs $c_{shear}$); the ASYM-class Cosserat-Curie mechanism is the third substrate-mechanism class beyond canonical SYM / large-amplitude ASYM.

## Upstream substrate primitives referenced

- **Cosserat rotation-sector mass-gap** ($\omega_m = 2$ in natural units, $\sim 1$ MeV): [`trampoline-framework.md`](../../common/trampoline-framework.md) line 188 — substrate-native magnetic-mode thermal-freeze threshold; substrate-Curie analog.
- **Cosserat couple-stress $\gamma_c$** + characteristic length $l_c = \sqrt{\gamma_c/G_{vac}}$: [`gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md) line 39 — load-bearing joint-constraint with the weak-force range.
- **SYM α-invariance proof** (`clm-3zz0f6`): [`alpha-invariance-symmetric-gravity.md`](../../vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) — load-bearing; SYM scaling preserves α, the Cosserat-Curie ASYM is the substrate-mechanism class that breaks SYM and produces α-drift.
- **Two-effective-wave-speeds canonical** (`clm-8nkvwy:111` / `:113`): [`einstein-field-equation.md`](../../vol3/gravity/ch02-general-relativity/einstein-field-equation.md) — $c_{EM}$ (Maxwell phase velocity, enters α) vs $c_{shear}$ (mechanical / group / rest-mass velocity, Schwarzschild). Pitfall #5 framework-leakage warning preserved.
- **Cold-lattice α asymptote** (`clm-0ktpcn`, $\alpha^{-1}_{ideal} = 4\pi^3 + \pi^2 + \pi$): Vol 1 Ch 8 alpha-golden-torus leaf — reference frame against which $\delta_{strain}$ is measured.
- **Substrate vacuum strain coefficient** (`clm-009nkt`): Vol 1 claim-quality entry — $\delta_{strain}$ back-subtracted from CODATA; this chapter is its cosmic-scale TCC instance leaf.

## Cross-volume Vol 9 cross-refs

- **Ch.4 DC Electrical Characteristics** ([`chapters/04_dc_electrical_characteristics.tex`](../../../vol_9_vacuum_datasheet/chapters/04_dc_electrical_characteristics.tex)) — cold-lattice reference frame ($S(0) = 1$, $T \to 0$) against which TCs are quoted.
- **Ch.5 AC Electrical Characteristics** ([`chapters/05_ac_electrical_characteristics.tex`](../../../vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex)) — frequency-domain operating-point modulation; $c_{EM}$ vs $c_{shear}$ disambiguation invoked here for thermal modulation.
- **Ch.2 Absolute Maximum Ratings** ([`chapters/02_absolute_maximum_ratings.tex`](../../../vol_9_vacuum_datasheet/chapters/02_absolute_maximum_ratings.tex)) — $T_{melt} \sim m_e c^2/k_B \approx 5.93 \times 10^9$ K Regime IV pair-production threshold (canonical `clm-uu6dl5`); Cosserat-Curie linear approximation breaks down well before $T_{melt}$.
- **Ch.10 Magnetic / Microrotational Characteristics** (Wave 2 sibling) — Cosserat rotation-sector mass-gap $\omega_m \sim 1$ MeV; same substrate primitive that drives Ch.6 Cosserat-Curie.
- **Ch.15 Falsification Tests** — joint-falsification with right-handed neutrino kill-switch (`clm-gw2wgc`); independent measurement of either weak-force range OR substrate α-drift constrains both.

## Closed research workstream (negative result)

**Q-DELTA-MAP-1-quant — CLOSED NEGATIVE (FT-1, 2026-05-31).** The candidate quantitative substrate-statistical-mechanics derivation of $\eta_\varepsilon \approx 4.45 \times 10^{-6}$ at $T_{CMB}$ from substrate primitives ($\ell_{node}$, $G_{vac}$, $\rho_{bulk}$, E-mode dispersion) was run forward (no target fed in) and **undershoots by ~31 OOM** ($\Theta_\text{Debye} \approx 2.3 \times 10^{10}$ K $\gg T_{CMB}$ forces the Debye-$T^4$ regime, below equipartition; BE occupation cannot amplify), AND is **generic-thermal, not AVE-distinct** (SM-counterfactual). The Class 2 lift via this route does **NOT** occur — `clm-hp7nlm` STAYS solidity 0.55 and `clm-009nkt` STAYS 0.55. δ_strain's magnitude is a **definitional residual**; only the SIGN is substrate-set. The mechanism-class identification + its weak-force $\gamma_c$ joint-constraint SURVIVE. Anchor: [`research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md`](../../../../research/2026-05-31_FT-1_delta-strain-eta-epsilon_result.md). The negative result is bounded in chapter §\ref{sec:vol9_temperature_open}.

## Manuscript counterpart

[`manuscript/vol_9_vacuum_datasheet/chapters/06_temperature_characteristics.tex`](../../../vol_9_vacuum_datasheet/chapters/06_temperature_characteristics.tex)

---
