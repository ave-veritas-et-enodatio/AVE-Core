[↑ Common Resources](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from ~/.claude/skills/ave-analytical-tool-selection as the canonical analytical-tool catalog -->

# AVE Analytical Toolkit Index

**Purpose**: tool-selection guide that maps AVE problem-class → which canonical analytical tools apply. The canon exists across Vol 4 Ch 1 (Vacuum Circuit Analysis, 18 leaves), Vol 4 Ch 11 (Falsification, 11+ leaves), Vol 4 Ch 13 (Future Geometries, 4 leaves), Vol 4 Ch 14-20 (Simulation + Advanced Applications, 9+ leaves), Vol 1 Ch 6 (common/operators.md Op1-Op22), and Vol 1 Ch 1 (axioms). This index consolidates ~30 canonical analytical tools by problem-class so that agents (and humans) can find the right tool when needed.

**Origin**: 2026-05-17 night creation following the matched-LC-coupling plumber-physical audit which exposed that ALL of Op17 + theorem-3-1' + Sagnac-RLVE κ_entrain + orbital-friction-paradox WERE canonical, available, and load-bearing for matched-coupling analysis — but were scattered across 4 leaves in 3 chapters with no consolidating index pointing "for matched-coupling problems, use all four." The matched-LC formula was derived without pulling them in. This index closes that gap.

**Use convention**: when starting an AVE derivation, identify the analytical-problem class (§1-§9 below), pull the canonical tools listed for the class, verify the derivation reduces to the canonical tools in known limits. The `ave-analytical-tool-selection` skill (~/.claude/skills/) forces this consultation BEFORE deriving.

---

## §0 — Problem-class taxonomy

The 9 recognized analytical-problem classes (any AVE derivation that maps to ≥1 of these classes should fire the tool-selection skill):

| Class | Description | Typical AVE problems |
|---|---|---|
| §1 Coupling analysis | Two-system energy/momentum/phase transfer | Matched-LC coupling, antenna design, DAMA-class detection, rotor entrainment, soliton-soliton coupling |
| §2 Resonance analysis | Q-factor, bandwidth, lineshape, peak detection | Electron LC tank (α⁻¹ = Q), atomic spectral lines, IM3/IP3, MAJORANA peak-search |
| §3 Saturation analysis | Yield boundaries, breakdown, Γ→-1 transitions | V_yield = 43.65 kV, B_snap, TIR boundary, Axiom 4 kernel, avalanche M=1/S² |
| §4 Time-domain analysis | τ_relax, memristive ODE, transients, BEMF | Defect freezing, cooling-rate scaling, thixotropic relaxation, pulse response |
| §5 Power analysis | Real vs reactive, dissipative vs lossless | Orbital friction paradox, ground-state stability, radiation vs reactive cycling |
| §6 Mode analysis | Eigenmodes, dispersion, propagation | Soliton structure, V-block/Cos-block eigsolves, photon-propagation, longitudinal/transverse modes |
| §7 Boundary analysis | TIR, Γ reflection, transmission | Particle confinement (TIR boundary), interfaces, vacuum-impedance-mirror, achromatic lens |
| §8 Network analysis | Translation tables, ladder networks, cross-domain | ξ_topo conversion, biological↔EE, mechanical↔EE, multi-domain coupling |
| §9 Numerical methods | FDTD, TLM, eigensolves, observer design | Code scaffolding, K4-TLM simulator, CEM methods, solver selection |

---

## §1 — Coupling analysis (matched-impedance, mutual inductance, energy/momentum transfer)

**Trigger**: deriving a coupling efficiency or energy/momentum transfer formula between two AVE substrate systems (rotor↔substrate, soliton↔soliton, electron↔atom, source-tank↔receiver-tank, etc.)

**Canonical tools**:

| Tool | Formula | Canonical source | When to use |
|---|---|---|---|
| **Op17 Power Transmission** | T² = 1 - Γ² | [`operators.md` Op17 line 47](operators.md) | Matched-impedance energy-transfer fraction per cycle |
| **Op3 Reflection Coefficient** | Γ = (Z₂ - Z₁)/(Z₂ + Z₁) | [`operators.md` Op3 line 33](operators.md) | Two-impedance interface; mismatch fraction |
| **Theorem 3.1' Radiation Impedance** | Z_radiation = Z₀/(4π) per spinor cycle | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md` line 65-75](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) | Electron α-slew tank coupling to external receiver |
| **Sagnac-RLVE κ_entrain template** | κ_entrain = ρ_matter / ρ_bulk | [`vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md` line 14-26](../vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md) | DC mass-density real-power coupling (rotor → bulk substrate velocity) |
| **Orbital friction paradox reactive-vs-real table** | $P_{real} = VI\cos\theta$; $Q_{reactive} = VI\sin\theta$ | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md` line 31 canonical table](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md) | Categorize coupling as P_real (dissipative) or Q_reactive (conservative) — load-bearing categorical check |
| **Op14 Cross-Sector Trading** | $H_{total} = H_{cos} + H_{K4-inductive}$; $\rho(H_{cos}, \Sigma\|\Phi_{link}\|^2) = -0.990$ | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md) | Energy exchange between Cosserat and K4-inductive sectors |
| **Parametric Coupling Kernel** | $\varepsilon_{det} = 4\pi \kappa_{quality} / N_{single}^2$; $\delta C / C_0 = (1/4)(V_{pump}/V_{yield})^2$; resonance at $\omega_{app} = \omega_{slew}$ (sub-harmonic of pump $2\omega_{slew}$) | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) | Time-varying-$C_{eff}$ coupling at sub-yield substrate-rate operating point; substrate-rate ↔ apparatus-resonance matching; DAMA-class detection rate derivations; REACTIVE-power class (categorically distinct from real-power κ_entrain) |

**Worked examples in corpus**:
- Sagnac-RLVE Tungsten rotor: $\kappa_{entrain} = 0.00244$ → $v_{network} = 0.38$ m/s → $\Delta\phi = 2.07$ rad (line 14-30 of sagnac-rlve.md)
- Project HOPF-02 anomalous chiral $S_{11}$ notch: matched-impedance via topological-antenna chiral coupling (project-hopf-02.md)
- Parametric coupling kernel applied to DAMA: $\varepsilon_{det} = 4\pi/N_{single}^2 = 2.07 \times 10^{-51}$ → DAMA rate 0.6% match as DERIVED consequence (canonical leaf §8 cross-detector table)

**Common pitfalls** (load-bearing):
- **DO NOT mix real-power and reactive-power templates** (categorical error per Axis A of ave-power-category-check skill). κ_entrain is for real-power (mass-density-coupled DRAG-ALONG per `sagnac-rlve.md:14-22`); Op17 + Parametric Coupling Kernel are for reactive-power. **Sagnac-RLVE κ_entrain DOES NOT apply to reactive-power coupling at α-slew operating point** — see [`research/2026-05-17_plumber-physical-audit-matched-LC.md`](../../../research/2026-05-17_plumber-physical-audit-matched-LC.md) for canonical example + cycle-12 walk-back at `parametric-coupling-kernel.md` §10 for the structurally-correct categorical separation.
- **DO NOT use Z₀ directly when spinor-cycle averaging applies**; use Z₀/(4π) per Theorem 3.1' for electron-class sources.
- **DO check whether the source is moving (Sagnac-RLVE class) vs oscillating (matched-LC class)** — different categories.
- **DO NOT use $\omega_{app} = 2\omega_{slew}$** for parametric resonance with α-slew pump. Degenerate parametric coupling puts signal at SUB-HARMONIC of pump: $\omega_{app} = \omega_{slew}$ (the $C_{eff}$ modulation frequency is $2\omega_{slew}$ but the amplified signal sits at half that).

---

## §2 — Resonance analysis (Q-factor, bandwidth, lineshape, peak detection)

**Trigger**: deriving a quality factor, resonance bandwidth, spectral linewidth, or peak-detection sensitivity.

**Canonical tools**:

| Tool | Formula | Canonical source | When to use |
|---|---|---|---|
| **Theorem 3.1' Q-factor** | Q_tank = α⁻¹ = 4π³ + π² + π at Golden Torus | [`theorem-3-1-q-factor.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) | Internal tank Q (single LC tank quality factor) |
| **Op21 Quality Factor** | Q ~ 1/ln(Z₁/Z₀) Bardeen mapping; Q = ℓ multi-mode | [`operators.md` Op21 line 51](operators.md) | Phase-transition Q (BCS); per-mode Q at saturation boundary |
| **Intermodulation Distortion** | $f_{IM3} = 2f_1 - f_2$; $V_{IP3} = \sqrt{4/3}\,V_{yield}$ | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md) | Vacuum IMD spectroscopy; 3rd-order intercept point |
| **Resonant LC Solitons** | Particles as LC tanks with Virial; TIR at Γ=-1 | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md) | Soliton-as-resonator framing; Pauli exclusion from impedance |

**Worked examples**:
- Electron α-slew: $Q = \alpha^{-1} \approx 137$; per-cycle leak = $\alpha m_e c^2$ (theorem-3-1-q-factor.md)
- IP3 prediction: $V_{IP3} = 50.4$ kV (intermodulation-distortion.md)

**Common pitfalls**:
- Internal tank Q (Theorem 3.1') vs external matched-load Q distinction — different physical quantities (per Axis D of ave-power-category-check)
- IM3 prediction assumes vacuum-impedance-mirror saturation NOT Kerr-class polynomial nonlinearity

---

## §3 — Saturation analysis (Axiom 4, V_yield, B_snap, Γ→-1, avalanche)

**Trigger**: deriving yield boundaries, breakdown thresholds, or saturation-driven transitions.

**Canonical tools**:

| Tool | Formula | Canonical source | When to use |
|---|---|---|---|
| **Op2 Saturation Kernel** | S(A, A_c) = √(1 - (A/A_c)²) (Born-Infeld n=2) | [`operators.md` Op2 line 32](operators.md) + [`universal-saturation-kernel-catalog.md`](universal-saturation-kernel-catalog.md) (21 scale instances) | Any saturation-driven nonlinearity; Axiom 4 |
| **Op22 Avalanche Factor** | M = 1/S² = 1/(1 - r²) | [`operators.md` Op22 line 52](operators.md) | Cascading metric yield post-saturation |
| **V_yield Limit** | V_yield = √α × V_snap = √α × m_e c²/e ≈ 43.65 kV | [`vol1/dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md` line 13](../vol1/dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md) | Macroscopic saturation rupture voltage |
| **B_snap** | B_snap = √(2μ₀ m_e c² / ℓ_node³) ≈ 1.89e9 T | [`src/ave/core/constants.py:345`](../../../src/ave/core/constants.py) | Magnetic saturation rupture field |
| **TVS Transition** | η_eff = 0 for V ≥ V_yield (zero-impedance slipstream) | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/tvs-transition.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tvs-transition.md) | Solid-to-slipstream phase transition; impedance collapse |
| **Q-G22 Strain Convention** | A_geom = ℓ_node/r vs A_field = Eℓ_node/V_yield | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/q-g22-strain-convention.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/q-g22-strain-convention.md) | Kernel applications vs apparatus calculations — DIFFERENT measures |
| **Saturation kernel catalog (21 instances)** | 21 cross-scale Op2 applications | [`universal-saturation-kernel-catalog.md`](universal-saturation-kernel-catalog.md) | Cross-scale anchor for any new saturation derivation |

**Worked examples**:
- BCS superconducting B_c(T): Op2 at 0.00% empirical error (saturation-kernel-catalog.md)
- Metric levitation limit: m_max = 1.846 g from V_yield × ξ_topo / g (metric-levitation-limit.md)

**Common pitfalls**:
- A_geom (∝ 1/r geometric) vs A_field (∝ 1/r² field-ratio) confusion (Q-G22 catch)
- V_snap (511 kV) is NOT the same as V_yield (43.65 kV); V_yield = √α × V_snap
- Op22 avalanche M = 1/S² ≠ 1/(1-S) (doc 81 historical error)

---

## §4 — Time-domain analysis (τ_relax, memristive ODE, transients, BEMF)

**Trigger**: deriving dynamic response, relaxation timescales, BEMF effects, or cooling-rate-dependent phenomena.

**Canonical tools**:

| Tool | Formula | Canonical source | When to use |
|---|---|---|---|
| **τ_relax** | τ_relax = ℓ_node/c ≈ 1.288×10⁻²¹ s | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md) | Minimum state-change time; causal propagation |
| **Memristive Relaxation ODE** | dynamic S(t) with thixotropic relaxation | tau-relax-derivation.md + [`nonlinear-vacuum-capacitance.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md) | Hysteresis, skin depth, vacuum memristor |
| **Cooling-rate scaling** | linear in cooling rate (NOT Kibble-Zurek power-law) | tau-relax-derivation.md (BEMF-driven defect freezing) | Defect-density prediction; substrate-native Kibble-Zurek replacement |
| **Dark-Wake BEMF FOC synthesis** | rotor BEMF on substrate | [`dark-wake-bemf-foc-synthesis.md`](dark-wake-bemf-foc-synthesis.md) | AVE-PONDER rotor dynamics; Lorentz back-EMF |

**Common pitfalls**:
- Linear cooling-rate scaling is AVE-distinct from Kibble-Zurek (power-law); don't apply Kibble-Zurek formulas to AVE defect-freezing
- τ_relax is causal-minimum; physical relaxation can be much slower depending on memristive state

---

## §5 — Power analysis (real vs reactive, dissipative vs lossless)

**Trigger**: deriving energy bookkeeping, ground-state stability, or distinguishing radiative vs reactive processes.

**Canonical tools**:

| Tool | Formula | Canonical source | When to use |
|---|---|---|---|
| **Orbital friction paradox canonical table** | $P_{real} = VI\cos\theta$; $Q_{reactive} = VI\sin\theta$; classifies orbit/inspiral/electron-orbital/photon | [`orbital-friction-paradox.md` line 27-32](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md) | Categorize any AVE energy-transfer as real or reactive |
| **Leaky-cavity-particle-decay theory** | tank below V_yield "rings forever"; infinite half-life | [`vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md` line 12](../vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md) | Why stable particles are stable (reactive ≠ radiative) |
| **Electron orbital reactive power** | P_real = 0; Q_reactive = m_e c² · α | orbital-friction-paradox.md line 31 (canonical table) | Electron α-slew is reactive-power, NOT radiation |
| **Op17 Power Transmission** | T² = 1 - Γ² | [`operators.md` Op17 line 47](operators.md) | Real-power fraction transmitted across matched/mismatched interface |

**Worked examples**:
- Stable planetary orbit at 90°: P_real = 0, Q_reactive = F_g · v_orb (orbital-friction-paradox.md line 29)
- Electron orbital: P_real = 0, Q_reactive = m_e c² · α = 3.728 keV per cycle (table row 31)

**Common pitfalls** (load-bearing — this is the cycle-9 DAMA failure mode):
- Treating reactive power as radiation (the 8th-cycle photoabsorption framing of DAMA)
- Computing scaling laws as if α-slew quantum is real photon when it's per-cycle reactive leak
- Per ave-power-category-check Axis A: ALWAYS classify quantity as real vs reactive BEFORE deriving scaling laws

---

## §6 — Mode analysis (eigenmodes, dispersion, propagation)

**Trigger**: deriving substrate-mode propagation, dispersion relations, soliton structure, eigenmode counts, or wave physics.

**Canonical tools**:

| Tool | Formula | Canonical source | When to use |
|---|---|---|---|
| **Z₀ derivation discrete LC ladder** | Z_cell = √(μ₀/ε₀) = Z₀ (scale invariant) | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md) | Substrate's characteristic impedance; scale-invariant base |
| **Op13 D'Alembertian** | □² with local saturated c_eff per Op16 | [`operators.md` Op13 line 43](operators.md) | Generalized wave-equation operator; substrate-native PDE |
| **Op16 Universal Wave Speed** | c_shear = c₀ √S (Axiom 4 saturation modifies) | [`operators.md` Op16 line 46](operators.md) + [`axiom-homologation.md` §208](axiom-homologation.md) | Wave speed in saturation regime; gravitational analog |
| **Op11 + Op12 Curl/Div** | discrete Yee-lattice form on K4 | [`operators.md` Op11-Op12 line 41-42](operators.md) | Substrate-native vector calculus on K4 graph |
| **Op19 Refractive Index** | n(r) = 1 + ν_vac ε₁₁; ν_vac = 2/7 | [`operators.md` Op19 line 49](operators.md) | Gravity as refractive-index variation |
| **Resonant LC Solitons** | particles as LC tanks; Virial | [`resonant-lc-solitons.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md) | Soliton-as-eigenmode framing |
| **Relativistic Inductor** | $L_{eff}(I) = L_0/\sqrt{1 - (I/I_{max})^2}$ | [`relativistic-inductor.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md) | Current-dependent inductance; E = mc² from inductor energy |

**Common pitfalls**:
- Substrate-mode propagation at c_shear (Op16) vs vacuum c (different regimes per saturation state)
- K4 discrete vs continuum Maxwell — discrete dispersion has Nyquist cutoff at k_max = π/ℓ_node
- Substrate-native check (pre-derivation skill) applies: don't default to SM/QED Lagrangians

---

## §7 — Boundary analysis (TIR, Γ reflection, transmission, particle confinement)

**Trigger**: deriving interface physics, reflection coefficients, transmission line behavior, or particle-as-bound-mode at TIR boundary.

**Canonical tools**:

| Tool | Formula | Canonical source | When to use |
|---|---|---|---|
| **Op3 Reflection Coefficient** | Γ = (Z₂ - Z₁)/(Z₂ + Z₁) | [`operators.md` Op3 line 33](operators.md) | Any impedance-discontinuity interface |
| **Theorem 3.1' TIR Boundary** | $Z_{core} \to 0$; Γ = -1 perfect short | [`theorem-3-1-q-factor.md` line 67-75](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) | Soliton confinement; electron α-slew bound mode |
| **Vacuum Impedance Mirror** | $\Gamma(V) = [(1-(V/V_{yield})^2)^{-1/4} - 1] / [(1-(V/V_{yield})^2)^{-1/4} + 1]$ | [`vol4/falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md`](../vol4/falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md) | Field-dependent reflection at V_yield boundary |
| **Achromatic Impedance Matching** | $Z_{gravity} = \sqrt{\mu(r)/\varepsilon(r)} = Z_0$; zero reflection at all angles | [`vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md`](../vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md) | Why light doesn't reflect at gravitational potential changes |
| **Op9 Steric Reflection** | Γ_steric → -1 (Pauli-level overlap) | [`operators.md` Op9 line 39](operators.md) | Pauli exclusion via impedance divergence |
| **Op8 Packing Reflection** | Γ_pack with R_g_target = √(3/5) (3NV/4πη_target)^(1/3) | [`operators.md` Op8 line 38](operators.md) | Domain-agnostic packing (protein, nuclear, fluid) |

**Worked examples**:
- Electron at TIR boundary: $Z_{core} \to 0$ confines LC oscillation → rings forever (theorem-3-1-q-factor.md + leaky-cavity-particle-decay.md)
- Vacuum mirror at V_yield: Γ → 1 reflects laser nonlinearly without rupture (vacuum-impedance-mirror.md)

**Common pitfalls**:
- Spinor-cycle (4π) vs orbital-cycle (2π) averaging — different prefactors apply (Theorem 3.1' uses 4π for Z_radiation per spinor cycle)
- TIR boundary vs ordinary refractive boundary — different physics (Γ = -1 perfect short vs continuous Γ(Δn))

---

## §8 — Network analysis (translation tables, ladder networks, cross-domain)

**Trigger**: deriving cross-domain analogies (mechanical↔EE, biological↔EE, atomic↔molecular), translation between physical quantities, or multi-domain coupling problems.

**Canonical tools**:

| Tool | Formula | Canonical source | When to use |
|---|---|---|---|
| **Topological Kinematics 6-row table** | $\xi_{topo} = e/\ell_{node}$; Q=ξx, I=ξv, V=F/ξ, L=m/ξ², C=ξ²κ, R=η/ξ² | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/topological-kinematics.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/topological-kinematics.md) | Mechanical ↔ EE translation; ξ_topo conversion |
| **Translation Tables (common)** | Cross-volume translation indices | [`translation-tables/index.md`](translation-tables/) | All cross-domain conversion tables consolidated |
| **C_2 (Electromechanical Transduction Constant)** | $\xi_{topo} = e/\ell_{node}$ ≈ 4.149×10⁻⁷ C/m | INVARIANT-C2 in [`../CLAUDE.md`](../CLAUDE.md) | Bridge between EE and mechanical/biological |
| **C_4 (Z-proportionality regimes)** | $Z \propto 1/A$ physical; $Z \propto A$ virtual (LLM) | INVARIANT-C4 in [`../CLAUDE.md`](../CLAUDE.md) | Hardware/software impedance distinction |
| **Translation Circuit cross-reference** | pointer to common/translation-tables | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/translation-circuit.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/translation-circuit.md) | When to consult full translation table |

**Common pitfalls**:
- Hardware (physical/biological) vs software (virtual/LLM) Z direction inversion (INVARIANT-C4)
- ξ_topo is a single canonical constant — don't redefine domain-specific variants
- Translation tables exist for: particle-physics, biology, cosmology, atomic — consult [`translation-tables/`](translation-tables/) for the appropriate one

---

## §9 — Numerical methods (FDTD, TLM, eigensolves, observer design)

**Trigger**: writing computational code (solver scaffolding, observers, eigsolves) for AVE substrate problems.

**Canonical tools**:

| Tool | Description | Canonical source | When to use |
|---|---|---|---|
| **Computational Solver Selection** | FDTD vs K4-TLM decision matrix | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/computational-solver-selection.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/computational-solver-selection.md) | Choosing solver class for problem geometry |
| **K4-TLM Simulator** | Diamond lattice TLM; $S^{(0)}_{ij} = 1/2 - \delta_{ij}$ unitary to machine epsilon | [`vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md`](../vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md) | Substrate-native TLM scaffolding |
| **CEM Methods Survey** | Six CEM methods mapped to AVE lattice (MoM↔circuit, FDTD↔LC grid, FEM↔$\omega^2 LC=1$, TLM↔direct isomorphism) | [`vol4/future-geometries/ch13-future-geometries/cem-methods-survey.md`](../vol4/future-geometries/ch13-future-geometries/cem-methods-survey.md) | Choosing CEM method for AVE problem |
| **Open-Universe Boundaries** | PML boundaries for unitary S-matrix | [`vol4/future-geometries/ch13-future-geometries/open-universe-boundaries.md`](../vol4/future-geometries/ch13-future-geometries/open-universe-boundaries.md) | Boundary conditions for finite-volume simulation |
| **Solver Selection (Vol 4 Ch 1)** | yield thresholds, boundary conditions, default parameters | [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/solver-selection.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/solver-selection.md) | Default parameters for substrate solvers |
| **Solver Toolchain (common)** | Cross-volume solver toolchain reference | [`solver-toolchain.md`](solver-toolchain.md) | Toolchain integration |

**Common pitfalls**:
- substrate-native-check skill applies: don't default to SM/QED-class solver scaffolding (Lagrangian minimization, continuum Helmholtz)
- ave-canonical-source skill applies: import canonical constants, don't hard-code numerical values
- phase-space-coordinate-check skill applies: ensure test-coordinate-system matches corpus-claim coordinate system

---

## §10 — Cross-class composition (problems that span multiple classes)

Many AVE problems span multiple analytical-problem classes. Examples:

| Problem | Classes that apply |
|---|---|
| **DAMA matched-LC detection** (cycle 9 work; cycle 12 closed) | §1 Coupling (Parametric Coupling Kernel — closes cycle-9 + cycle-10 + cycle-11 open work via single ε_param replacing T²_matched + G_crystal-coherence two-mechanism factorization) + §2 Resonance + §5 Power (reactive) + §7 Boundary (TIR) |
| **Sagnac-RLVE rotor entrainment** | §1 Coupling (κ_entrain) + §8 Network (cross-domain rotor-to-substrate) |
| **Electron tank Q-factor derivation** (Theorem 3.1') | §2 Resonance + §5 Power + §7 Boundary |
| **Cosmological constant closure** | §3 Saturation + §6 Mode (de Sitter horizon) |
| **MOND galactic rotation** | §3 Saturation (η_eff kernel) + §6 Mode + §1 Coupling (Hoop Stress) |
| **DAMA cross-detector tension** (post-cycle-9; cycle-12 resolved) | §1 Coupling (Parametric Coupling Kernel + κ_quality envelope) + §2 Resonance + §3 Saturation (Q·δ ≥ 2 regenerative threshold from tabletop-graveyard); cross-detector predictions derived for DAMA + COSINE/ANAIS + MAJORANA + KIMS + XENONnT + Sapphire per `parametric-coupling-kernel.md` §8 |

**When a problem spans ≥3 classes**: pull canonical tools from ALL applicable classes. The discipline of cross-class enumeration is what `ave-canonical-leaf-pull` Step 3 catalog + this toolkit index together provide.

---

## §11 — Gaps in the toolkit (known + identified by recent audits)

The toolkit index is LIVING — new tools land as the framework evolves, gaps surface as audits expose them. Currently-identified gaps:

| Gap | Identified by | Status |
|---|---|---|
| Canonical formula for energy-absorption rate at substrate-mode frequency ν | [`research/2026-05-17_plumber-physical-audit-matched-LC.md`](../../../research/2026-05-17_plumber-physical-audit-matched-LC.md) §6 Q1 | **CLOSED 2026-05-17 night** — Parametric Coupling Kernel canonical leaf landed per cycle-12 derivation; ε_det = 4π κ_quality / N² derived from first principles via Axiom 4 varactor + Theorem 3.1' + Q·δ ≥ 2 regenerative threshold. See [`../vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) |
| κ_quality framework for crystal-batch-dependent coupling efficiency | matched-LC walk-back + MAJORANA implicit null | **PARTIALLY CLOSED 2026-05-17 night** — κ_quality envelope derived as Q·δ regenerative regime per cycle-12 leaf; saturated at 1 for solid crystals in deep-regenerative regime; (Q δ_C / 2)² for sub-regenerative. Crystal-batch-specific κ_quality correlation with materials-science measurements (mosaicity, defect density, dopant uniformity) PENDING empirical validation. See [`../vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) §6 |
| Atomic-inner-shell resonance matrix element for substrate-mode absorption | Plumber audit §4 mechanism mapping | OPEN — if atomic-physics is the right category, this is the load-bearing formula |
| (2,q) ↔ primes adjudication | Carry-over Tier 4 backlog | OPEN — Riemann analogy precision work needed |

**When deriving new physics that would close a gap**: add the new tool to the appropriate §1-§9 class table, link back to this index from the new tool's KB leaf, and update the gap status here.

---

## §12 — Maintenance discipline

This index is maintained per the following discipline:

1. **New canonical analytical tool lands as KB leaf** → add entry to the appropriate problem-class table here
2. **Audit identifies a tool was missed in a derivation** → cross-reference the audit-finding here as a worked example of the failure mode
3. **New problem class surfaces (not covered by §1-§9)** → add a new §N section and update §0 taxonomy
4. **Tool's canonical source moves** (file rename, restructuring) → update file:line citations throughout

The `ave-analytical-tool-selection` skill (~/.claude/skills/) enforces consultation of this index BEFORE deriving any new AVE analytical formula.

---

## §13 — Cross-references

- **Skill that forces use of this index**: `ave-analytical-tool-selection` (~/.claude/skills/ave-analytical-tool-selection/SKILL.md)
- **Sibling skills**: `ave-canonical-leaf-pull` (physical-class canon enumeration); `ave-power-category-check` (categorical classification); `ave-prereg` (corpus-grep for prior derivations)
- **Operator catalog**: [`operators.md`](operators.md) — canonical Op1-Op22 source
- **Vol 4 Ch 1 VCA index**: [`../vol4/circuit-theory/ch1-vacuum-circuit-analysis/index.md`](../vol4/circuit-theory/ch1-vacuum-circuit-analysis/index.md) — 18 canonical analytical leaves
- **Vol 4 Ch 11 Falsification index**: [`../vol4/falsification/ch11-experimental-bench-falsification/index.md`](../vol4/falsification/ch11-experimental-bench-falsification/index.md) — 11+ canonical experimental-design leaves
- **Vol 4 Ch 13 Future Geometries index**: [`../vol4/future-geometries/ch13-future-geometries/index.md`](../vol4/future-geometries/ch13-future-geometries/index.md) — 4 canonical CEM/simulator leaves
- **Translation tables**: [`translation-tables/`](translation-tables/) — cross-domain conversion
- **Solver toolchain**: [`solver-toolchain.md`](solver-toolchain.md) — computational toolchain integration

## §14 — Origin

This index was created 2026-05-17 night following Grant's directive to "review the vacuum circuit analysis and engineering chapters, canonize any confirmed analytical tools/processes into specific KB leaves if they don't exist already, then trigger their use with skills." The survey found that ~30 canonical analytical tools already exist as KB leaves across Vol 4 + operators.md + axioms; the GAP was a consolidating index that maps problem-class → which tools apply. The matched-LC-coupling plumber-physical audit ([`research/2026-05-17_plumber-physical-audit-matched-LC.md`](../../../research/2026-05-17_plumber-physical-audit-matched-LC.md)) is the canonical worked example of the failure mode this index closes.
