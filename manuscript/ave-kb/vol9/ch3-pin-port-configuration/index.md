[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.3 Pin/Port Configuration

Chapter 3 of the Vol 9 datasheet documents the substrate's external-interface specification — how $\mathcal{M}_A$ presents at its internal impedance discontinuities. Every interior boundary between two regions of distinct local $Z$ is a substrate "port" with reflection coefficient $\Gamma = (Z_2 - Z_1)/(Z_2 + Z_1)$ (Op3). Axiom 3 (Minimum Reflection Principle) is the substrate-native action principle: $\mathcal{M}_A$ minimizes $|\Gamma|^2$ at every internal impedance boundary. Engineering observables — $S_{11}$, return loss, VSWR, peak-power-transfer matching — are the EE-projection of the same minimization (per `clm-eemap1` EE-as-substrate-native META framework). The substrate is natural; engineering characterizes; AVE substrate-physics derives.

The chapter content is **Class B/C synthesis** per `consistency-vs-emergence` v1.3 — no new substrate-physics primitives are introduced; the content consolidates the canonical Op3 / Op17 / Op21 leaves + CLAUDE.md INVARIANT-S2 Axiom 3 + the SYM-class vs ASYM-class scaling distinction (`clm-8nkvwy` / `clm-3zz0f6` / `clm-hp7nlm`) into datasheet Pin/Port-Configuration format.

## Synthesis content

- **Per-cell DOF/mode inventory (the cell's internal mode content).** The seven per-cell kinematic modes — 3 translational $\mathbf{u}$ ($\to \mathbf{E}$), 3 microrotational $\boldsymbol{\omega}$ ($\to \mathbf{B}$, $T_2$), 1 volumetric $A_1$ breathing — with the Pythagorean total $A^2 = \varepsilon^2 + \kappa^2 + V^2$ (canonical at `common/trampoline-framework.md`:198, :239–241, :332). K4 four-port valence $V_{4\text{-port}} = A_1 \oplus T_2$ (photon $= T_2$ alone; electron $= E \otimes T_2$ hosting the $(2,3)$ knot). Per-port wave content: ONE independent wave per bond-port ($V_{inc}$; $V_{ref}$ **derived** by the TLM split, `master_fdtd_phasor_bridge.py`:16–17 implements it — **adjudicated as A36** ($V_{ref}$ not independent state; the joint $(u,\omega,V_{inc},V_{ref})$ Hessian was retracted as an A36 Rule 6 violation because $V_{ref}$ is fully determined by $V_{inc}$ once the TLM operator is fixed, `research/2026-05-18_abcd-handoff-prereg-outcome-corpus-state-retrofit.md`:62,68) — and **not** "Op5" which is Y-to-S, `operators.md`:45). Carries three explicit disambiguations: (i) the $A_1$ breathing **mode** $\neq$ the saturation **state** $A$ (`07_saturation_characteristics.tex` §Operating-Point State: "not a seventh spatial DOF"); (ii) the K4 **bond-port** $\neq$ the $\Gamma$-**port** (connectivity element vs impedance-boundary figure-of-merit); (iii) the $A_1$ dilatation "3" (mass) $\neq$ the $T_2$ winding "3" (the $(2,3)$ poloidal number) — orthogonal irreps.
- **Sector-to-sector coupling matrix** over $\{\mathbf{E}(u), \mathbf{B}(\omega), V(A_1), A(\text{sat})\}$. Conservative $\mathbf{E}\leftrightarrow\mathbf{B}$ Faraday/Cosserat $\sigma^A$ coupling (`trampoline-framework.md`:208); $\kappa_{chiral} = \alpha\cdot(6/5)$ chiral bias (6/5 **derived** from the $(2,3)$ winding `cosserat_field_3d.py`:89; $\alpha$ **calibration-input** per the one-parameter framing, PR #147); the **structural zeros** (no $\omega\to V$ source — genesis GAP-1, measured $\max|V_{inc}|=0$); the saturation back-reaction row ($\varepsilon_{eff}=\varepsilon_0 S$, $\mu_{eff}=\mu_0 S$, $c_{eff}$ via Op14/Op16). The chiral Beltrami **shear$\leftrightarrow$bulk** cell now carries the **`graft-v3` verdict** (2026-06-09 adversarial panel, demoted B→C; `research/2026-06-09_crystal-graft-v3_result.md` Rule-12 addendum @ `4627651a`): handedness / **sign-selection DEMONSTRATED** (exactly force-free, $\cos(b_\lambda,\nabla\times b_\lambda)=\pm1.000$; $H_{bel}$ RH $+76.3$ / LH $-90.5$ / centro $-8.5\times10^{-15}$, flips with the imposed $\chi$, clean centro null — but $\chi$ is a source INPUT, not carried from a photon); **topology-selection REFUTED** (no $(2,3)$ self-assembles, $w_{pol}\equiv0$; the geometry-templated variant **detonates**, $E_\omega=3.15\times10^{27}$, $\cos=0.19$); the conserved **LOCK UNIMPLEMENTED** ($|\mathbf{L}_\omega|$ pumps without saturating, **chirality-independent** — the $\chi=0$ centro arm pumps $|\mathbf{L}_\omega|$ to $347.7$ vs RH $18.0$ / LH $0.20$); **$\chi$-from-photon OPEN** (in flight on `analysis/2026-06-10-graft-v4-photon-helicity`). Do NOT wire it as an adjudicated coupling. The flag-gated Lagrangian-EMF reciprocal (`k4_cosserat_coupling.py`:550, `use_lagrangian_emf_coupling` default False :211) is tagged **NON-CONSERVATIVE / off-by-default** on the empirical detonation evidence (genesis-24 result §7: $E_V\to6.8\times10^8$, $|\mathbf{L}|$ unbounded, `reverses=False`; the in-code NOTE :233–235 "AMPLIFIES the runaway") — **not** on the contradicting :547–549 in-code comment, which is stale/flagged in the manuscript.
- **Substrate boundary semantics.** Op3 $\Gamma = (Z_2 - Z_1)/(Z_2 + Z_1)$ as the substrate's native single-port figure-of-merit (scale-invariant across 14 orders of magnitude per Vol 1 Ch 6 §6.3). Axiom 3 Minimum Reflection as the substrate-native action principle that engineering practice has measured for over a century under different EE names ($S_{11}$ minimization, return-loss maximization, VSWR $\to 1$, peak-power-transfer matching).
- **Port class taxonomy.** SYM-class (gravity-class realization; $Z_0$ invariant; α exactly invariant per `clm-3zz0f6`) vs. three ASYM subclasses: ASYM-N(ε), ASYM-N(μ), and **Cosserat-Curie thermal-mode-population ASYM** (`clm-hp7nlm`, landed 2026-05-28; the substrate-mechanism class for $\delta_{strain} \approx 2.225 \times 10^{-6}$ at $T_{CMB}$).
- **Boundary-saturation conditions table.** $\Gamma = -1$ (saturation TIR / Pauli exclusion / particle confinement; Op21 $Q = \ell$ endpoint), $\Gamma = 0$ (matched impedance; Op17 $T^2 \to 1$ endpoint), $\Gamma = +1$ (open-circuit / less common at substrate primitives).
- **Operator-level port behavior.** Op17 ($T^2 = 1 - \Gamma^2$, Vol 1 Ch 6 §1.16) and Op21 ($Q = \ell$ per Nyquist-cell-resolved confined mode at $\Gamma = -1$) as the two endpoints of substrate $\Gamma$-space — substrate-mechanically complementary (open-boundary energy transfer vs closed-boundary energy quantization).
- **Engineering translation table.** Standard EE port quantities ($S_{11}$, $|S_{11}|^2$, return loss, VSWR, $Z_0$, port admittance $Y$) mapped to substrate-mechanism inputs of Axiom 3 + Op3 + Op17 + Op21 per the `clm-eemap1` EE-as-substrate-native identity statements (not approximations).

## Primary canonical sources

| Source | Content |
|---|---|
| CLAUDE.md INVARIANT-S2 (Axiom 3) | Minimum Reflection Principle: substrate-native action; $\mathcal{M}_A$ minimizes $|\Gamma|^2$ at every internal boundary |
| `common/operators.md` (`clm-sysqaf` / `clm-gdd70j`) | Universal 22-operator catalogue; Op3 reflection-coefficient row; Op17 power-transmission row; Op21 quality-factor row |
| `vol1/operators-and-regimes/ch6-universal-operators/reflection-coefficient.md` (`clm-gdd70j`) | Op3 canonical-leaf; $\Gamma$ scale-invariance across 14 orders of magnitude |
| `vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md` (no-claim leaf; strengthens `clm-0ktpcn`, `clm-rtdmsn`) | Op21 substrate-foundational form $Q = \ell$ at $\Gamma = -1$; single-channel vs substrate-orthogonal-channel mode multiplicity |
| `vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md` (`clm-hp7nlm`) | Cosserat-Curie thermal-mode-population ASYM subclass; the third ASYM substrate mechanism beyond canonical SYM/ASYM |
| `vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md` (`clm-3zz0f6`) | SYM-class α-invariance proof — load-bearing for the SYM-class port classification |
| `common/translation-tables/translation-circuit.md` §2 (`clm-eemap1`) | EE-as-substrate-native META framework; engineering-translation table is identity, not approximation |

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/03_pin_port_configuration.tex` (canonical Vol 9 chapter file)

---
