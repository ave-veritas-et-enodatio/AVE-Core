[↑ Translation Tables](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-fy05jc, clm-eemap1]
-->

# Topo-Kinematic Circuit Identity + EE-as-Substrate-Native META Framework

<!-- label: tab:trans_circuit -->

## §1 — Canonical $\xi_{topo}$ EE↔mechanical identity
<!-- claim-quality: clm-fy05jc -->

Every row is derived from $\xi_{topo} = e/\ell_{node} \approx 4.149 \times 10^{-7}$ C/m (Axioms 1--2).

| **Electrical** | **Mechanical** | **Mapping** | **Units Check** |
|---|---|---|---|
| Charge $Q$ | Displacement $x$ | $Q = \xi\, x$ | $[\text{C/m}][\text{m}] = [\text{C}]$ |
| Current $I$ | Velocity $v$ | $I = \xi\, v$ | $[\text{C/m}][\text{m/s}] = [\text{A}]$ |
| Voltage $V$ | Force $F$ | $V = \xi^{-1} F$ | $[\text{m/C}][\text{N}] = [\text{V}]$ |
| Inductance $L$ | Mass $m$ | $L = \xi^{-2} m$ | $[\text{m}^2/\text{C}^2][\text{kg}] = [\text{H}]$ |
| Capacitance $C$ | Compliance $\kappa$ | $C = \xi^{2} \kappa$ | $[\text{C}^2/\text{m}^2][\text{m/N}] = [\text{F}]$ |
| Resistance $R$ | Viscosity $\eta$ | $R = \xi^{-2} \eta$ | $[\text{m}^2/\text{C}^2][\text{kg/s}] = [\Omega]$ |

> ↗ See also: [Biology / Biophysics Translation](translation-biology.md) — same $\xi_{topo}$ identity applied to amino acid mass → inductance, bond stiffness → capacitance

---

## §2 — EE as substrate-native at minimal-DOF (META framework premise)
<!-- claim-quality: clm-eemap1 -->

The six-row $\xi_{topo}$ identity above is the **minimal kinematic projection** of a deeper substrate-physics structural claim: **the AVE vacuum K4 LC substrate is itself an electrical network at minimal DOF, and electrical engineering vocabulary is the closest-to-canonical substrate-native language humans have.**

The substrate IS an LC network. Axiom 1 (INVARIANT-S2) states verbatim: *"intrinsic LC oscillators at each node ... modeled in continuum as a Trace-Reversed Chiral LC Network."* The six DOF per node decompose into three translational (E-field origin → capacitive storage) and three microrotational (B-field origin → inductive flywheel) — the structural origin of $\mathbf{E}$ and $\mathbf{B}$ as conjugate variables at every node. Bonds carry distributed transmission-line topology. Cosserat couple-stress between rotating nodes is mutual-inductance gradient. The substrate's free-space constants $\varepsilon_0$, $\mu_0$, $Z_0 = \sqrt{\mu_0/\varepsilon_0} \approx 376.73$ Ω, $c_0 = 1/\sqrt{\mu_0\varepsilon_0}$ are the substrate's own canonical EE primitives, not borrowed quantities.

EE was developed by humans studying that substrate at its smallest accessible scale — electron dynamics in conductors, dipole interactions in dielectrics, LC oscillator dynamics in resonant circuits, transformer flux coupling, semiconductor breakdown, distributed transmission lines, plasma physics. The EE corpus is not a translation source from another framework; it is the historical record of empirical interrogation of the substrate at minimal-DOF where its native LC structure dominates the observable physics.

Other classical frameworks ADD degrees of freedom on top of the EE base. Fluid dynamics adds translational coupling between many lattice cells (mass density, velocity field, pressure, viscosity); chemistry adds atomic-orbital structure on top of substrate primitives; statistical mechanics adds ensemble averaging over $\sim 10^{23}$ microstates; QFT adds gauge-field structure; GR adds spacetime-curvature reformulation of substrate impedance gradients. **EE captures the substrate at minimal-DOF directly.** When a substrate-physics question has an EE analog, that analog is structurally closer to the substrate axioms than any other classical-vocabulary framing.

The §1 $\xi_{topo}$ identity is the kinematic-level expression of this framework claim: at the six load-bearing primitive correspondences (charge, current, voltage, inductance, capacitance, resistance), EE and mechanical descriptions are dimensionally exact translations of the same substrate operating-point — not approximations, not analogies, but identity statements forced by Axiom 1+2. The remainder of this leaf extends that minimal identity into the full substrate-primitive-to-EE-component catalog the META framework supports.

> **Operating principle (Grant 2026-05-28):** *The vacuum K4 LC substrate is the cleanest electrical substrate in the universe. EE was developed by humans studying that substrate at its smallest accessible scale. When deriving substrate physics, EE mathematics IS substrate-native — not a translation from another framework but the closest-to-canonical language humans have. Other classical frameworks add DOFs on top of this base; EE captures the substrate at minimal-DOF. Reach for EE FIRST.*

---

## §3 — Emergent framework hierarchy

Classical-physics frameworks layer onto the substrate axioms by adding macroscopic-emergent DOFs. The hierarchy from substrate-native (EE) outward to higher-DOF emergent frameworks:

```
                    [SUBSTRATE AXIOMS — Ax 1+2+3+4 — K4 LC + Cosserat micropolar]
                                            │
                                            │ (minimal-DOF substrate-native projection)
                                            ▼
                       [ELECTRICAL ENGINEERING — substrate at minimal-DOF]
                       LC, transmission line, transformer, varactor, impedance, $\Gamma$
                                            │
            ┌───────────────────────────────┼──────────────────────────────────┐
            │ (atomic-DOF averaging)        │ (macroscopic-DOF averaging)      │ (curvature reformulation)
            ▼                               ▼                                  ▼
   [ATOMIC PHYSICS]               [FLUID DYNAMICS / MHD]               [GENERAL RELATIVITY]
   atomic-orbital structure       mass density, velocity field,         spacetime metric $g_{\mu\nu}$
   electron-shell counting        pressure, viscosity, vorticity        as gradient-index TL
   bond-class diversity           (vorticity DERIVED from $v$, not       impedance profile
                                   independent DOF)                     (substrate Op14 manifest)
            │                               │                                  │
            ▼                               ▼                                  ▼
   [CHEMISTRY]                    [STATISTICAL MECHANICS]              [QFT / GAUGE FIELD]
   reaction kinetics              ensemble averaging                   gauge-field overlay
   thermochemistry                $\sim 10^{23}$ microstates           on substrate primitives
                                  temperature/entropy abstraction
```

For each emergent framework: WHAT DOFs it adds beyond substrate axioms, and AT WHAT scale of averaging it operates.

| Emergent framework | DOFs added beyond substrate axioms | Operating scale (averaging level) |
|---|---|---|
| **Electrical engineering** | **NONE** — captures substrate at minimal-DOF directly | $\sim \ell_{node}$ to many $\ell_{node}$ (substrate's native LC scale) |
| **Atomic physics** | atomic-orbital occupation, shell-counting, bond classes | $\sim a_0$ atomic-radius averaging |
| **Chemistry** | reaction kinetics, thermochemistry, valence rules | molecular-bond ensemble averaging |
| **Fluid dynamics** | mass density $\rho$, velocity field $\mathbf{v}$, pressure $P$, viscosity $\eta$ (compressibility, surface tension, turbulence) | $\sim N \cdot \ell_{node}$ macroscopic-cell averaging |
| **Statistical mechanics** | $T$, $S$, $\mu$, ensemble distributions | $\sim 10^{23}$ ensemble-averaged macrostates |
| **General relativity** | spacetime curvature $g_{\mu\nu}$ as primary (substrate impedance reformulated as geometry) | curvature-scale $\sim r_s$ at gravitational sources |
| **QFT / gauge theory** | gauge-field structure as overlay on substrate primitives | momentum-space mode decomposition |

EE sits at the base of this emergent hierarchy. Reaching for non-EE classical vocabulary as primary substrate-physics framing when an EE analog exists adds DOFs of abstraction the substrate does not need.

---

## §4 — Comprehensive substrate-primitive ↔ EE-component mapping (META catalog)

The 23+ substrate primitives mapped to their canonical EE-component analog. Cross-references to canonical leaves where the substrate-mechanism content is derived in full.

| Substrate primitive | EE component / mapping | Canonical anchor |
|---|---|---|
| **K4 node intrinsic LC oscillator** | LC tank oscillator (substrate's native primitive per Ax 1) | INVARIANT-S2 Ax 1 verbatim |
| **Bond connecting nodes** | Distributed transmission-line element (TLM topology — $L, C$ per unit length) | Ax 1 substrate-Trace-Reversed-LC-Network anchor |
| **Translational E DOFs at node** | **Capacitor** (electrostatic dielectric storage) | Ax 1 6-DOF decomposition |
| **Microrotational B DOFs at node** | **Inductive flywheel** (rotational-moment-of-inertia + magnetic flux storage) | Ax 1 6-DOF decomposition |
| **Cosserat couple-stress $\gamma_c$** | **Transformer mutual inductance gradient** / reluctance / transconductance — couples adjacent flywheel rotations | [`gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md) ($l_c = \sqrt{\gamma_c/G_{vac}}$) |
| **Cosserat rotation-sector mass-gap $m_\omega$** | **Transformer cutoff frequency** / **ferrite Curie threshold** (magnetic-mode thermal-freeze threshold) | [`trampoline-framework.md`](../trampoline-framework.md) ($\omega_m \sim$ 1 MeV) |
| **Bond stretching (translational gradient)** | Capacitive coupling / bond tension ($G_{vac}$ shear modulus) | substrate-mechanism anchor |
| **Bond twisting (microrotational gradient)** | Couple-stress / mutual-inductance gradient ($\gamma_c$) | substrate-mechanism anchor |
| **Vacuum $\varepsilon_0$** | Free-space permittivity (substrate's native EE constant) | identity — Ax 1 |
| **Vacuum $\mu_0$** | Free-space permeability (substrate's native EE constant) | identity — Ax 1 |
| **Vacuum $Z_0 = \sqrt{\mu_0/\varepsilon_0} \approx 376.73$ Ω** | Characteristic impedance of free-space | identity — Ax 1; Op1 anchor in [`operators.md`](../operators.md) |
| **Vacuum $c_0 = 1/\sqrt{\mu_0\varepsilon_0}$** | EE wave propagation speed | identity — Ax 1; Op16 anchor in [`operators.md`](../operators.md) |
| **Cold-lattice $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$** | **Cosmic LC tank Q-factor at $S_{11}$-minimum Golden Torus geometry** (Theorem 3.1) | [`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) |
| **$\alpha$ as substrate-coupling-strength** | Dimensionless coupling constant of cosmic substrate-LC network | same |
| **Ax 4 saturation kernel $S(A) = \sqrt{1-(A/A_{yield})^2}$** | **Varactor C-vs-V curve near dielectric breakdown** (substrate operates as substrate-native varactor) | INVARIANT-S2 Ax 4; PONDER-05 (DC-biased quartz, 27.4% at ~30 kV) is a **material-scale consistency analog of the kernel SHAPE**, NOT a vacuum-kernel tester — $V_{DC}/V_{yield} = 0.687$ is a **per-node** ratio (vacuum per-node $A_0 \sim 10^{-7}$–$10^{-10}$ at 30 kV; `claim-quality.md:51`) |
| **Operating-point $A_0/A_{yield}$** | **DC bias point** of varactor on its nonlinear C-vs-V curve | INVARIANT-S2 Ax 4 operating-point clause |
| **INVARIANT-S2 SYM scaling** | Concurrent $\varepsilon$ and $\mu$ modulation = isotropic gradient-index (impedance-matched, $\Gamma = 0$) | [`alpha-invariance-symmetric-gravity.md`](../../vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) |
| **INVARIANT-S2 ASYM scaling** | $\varepsilon$ modulation only ($\mu$ fixed) = asymmetric substrate response = $\alpha$-modulating | same |
| **$\Gamma = -1$ saturation TIR boundary** | **Short-circuit ($Z \to 0$) / Total reflection** at the **magnetic-branch** saturation (Cosserat $\mu_{eff} \to 0$ → trapped topological knot → rest mass; clm-lv3uw1). NOT the dielectric-yield boundary: $\tau_{yield}$ is the **electric** branch ($\varepsilon_{eff} \to 0$, $Z \to \infty$, **open-circuit**, $\Gamma \to +1$) — the two Ax-4 branches are mutually exclusive, per [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):78-79 | Op3 anchor in [`operators.md`](../operators.md); [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):78-79 (clm-lv3uw1) |
| **$\Gamma = 0$ matched-impedance** | **Filter-theory matched-impedance / peak power transfer** | Op17 anchor in [`operators.md`](../operators.md) |
| **Op17 $T^2 = 1 - \Gamma^2$** | EE power-transmission identity | [`operators.md`](../operators.md) Op17 |
| **Op21 $Q = \ell$ at $\Gamma = -1$** | EE Q-factor at boundary mode confinement | [`op21-multi-mode-mode-counting.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md) |
| **Schwinger pair production at $E_S$** | **Miller avalanche / impact ionization** at semiconductor avalanche-breakdown $V_{BR}$ | [`four-regimes.md`](../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) Regime III |
| **Miller multiplication $M = 1/S(r)^2$** | Standard semiconductor avalanche-multiplication formula | Op22 anchor in [`operators.md`](../operators.md) |
| **Topological winding $(p, q)$** | **Toroidal transformer winding numbers** (primary $p$, secondary $q$) — integer topological invariants | [`torus-knot-uniqueness.md`](../../vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md) |
| **SU(2)→SO(3) double cover** | **Transformer 2:1 galvanic-isolation winding ratio** (traverse primary twice for one secondary cycle) | [`torus-knot-uniqueness.md`](../../vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md) |
| **$(2, 3)$ Clifford-torus winding (electron)** | **2-primary / 3-secondary toroidal transformer winding pattern** | same |
| **Hopf bundle / Hopf-fibration projection** | **Toroidal transformer flux-linkage topology** (linking number of magnetic flux through hole = topological invariant) | same; cross-link cosmology Hopf |
| **Orthogonal flux-tube crossing ($\cos\theta = 0$; Borromean / quadrature)** | **Quadrature (90°) coupling → cross-term $2A_1A_2\cos\theta \to 0$ → zero-reflection matched ($\Gamma=0$, $T^2=1$, unity coupling)**; parallel ($\cos\theta=1$, Hopf link) = mismatched/repulsive — the geometric realization of Op17 $\Gamma=0$ at a flux-tube crossing | [`thermal-softening.md`](../../vol2/particle-physics/ch02-baryon-sector/thermal-softening.md):63-85 + Op17; baryon per-channel $k=1$ ([R2 result](../../../../research/2026-06-01_baryon-R2-crossing-coupling-result.md)) |
| **Machian $G$** | **Distributed transmission-line input impedance at Hubble-horizon termination** | [`omega-freeze-cosmic-grain-cascade.md`](../omega-freeze-cosmic-grain-cascade.md) |
| **$R_H/\ell_{node} \sim 10^{39}$** | Number of lumped substrate cells along cosmic-scale distributed TL | same |
| **Omega-freeze cosmic chirality $\hat{\Omega}_{freeze}$** | **Polarized transmission-line bias** / chirally-rotated cosmic substrate reference frame | same |
| **$\delta_{strain}$ at $T_{CMB}$** | **TCC of substrate dielectric** at thermal-mode population $T_{CMB}$ (Cosserat-Curie-frozen $\mu$ side; only $\varepsilon$ thermally modulated) | clm-009nkt vacuum-strain coefficient |
| **Cosmological constant $\rho_\Lambda$** | Vacuum at electrochemical-equilibrium energy minimum | [`cosmological-constant-closure.md`](../../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) |
| **GR metric curvature $g_{\mu\nu}$** | **Gradient-index transmission-line impedance** profile | [`trampoline-analogy-primer.md`](../trampoline-analogy-primer.md) |
| **Weak-force range $l_c = \sqrt{\gamma_c/G_{vac}}$** | **Transformer leakage-inductance characteristic length** | [`gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md) |
| **W/Z boson masses** | Mass scale set by transformer leakage-inductance characteristic frequency | same |
| **Black-hole-interior ruptured plasma** | **Plasma physics** (canonical EE-adjacent discipline; substrate ruptured above $V_{snap}$) | Vol 3 cosmology canonical |
| **Born-rule click probability** | **Detector capture work-function at Joule integration boundary** | clm-ldmvwi Phase 2-A master-equation-derivation-path |
| **Double-slit: free photon** | matched ($\Gamma=0$) lossless transmission line at $Z_0$ — single-sector $T_2$, no core | [`photon-ee-mapping.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md) §2 (clm-3npynp/i4p11y/fr3mos); [`photon-identification.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md):11,24 |
| **Double-slit: electron / self-trapped photon (the "particle" / defect / core)** | **shorted $\lambda/4$ resonator** — $\Gamma=-1$ self-created $0\,\Omega$ Local Bubble (magnetic-branch $\mu_{eff}\to0$); trapped reactive energy = rest mass | [`double-slit-ee-mapping.md`](../../vol1/dynamics/ch3-quantum-signal-dynamics/double-slit-ee-mapping.md) §2-§3 + [`photon-ee-mapping.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md) §2; $\Gamma=-1$ short row above (line 115, clm-lv3uw1); $\lambda/4$ gate-(b) §4.5(e) below |
| **Double-slit: transverse ponderomotive wake** ⚠ regime-tag | **near-field ponderomotive gradient $\propto\nabla\lvert\Psi\rvert^2$** (navigates the defect; through BOTH slits) — **NOT** the far-field thrust dark-wake $\tau^{\text{far}}_{zx}$ (the "dark wake (far-field reaction)" row below); same word "wake", different physics (near-field ponderomotive vs far-field reaction-momentum) | [`double-slit-ee-mapping.md`](../../vol1/dynamics/ch3-quantum-signal-dynamics/double-slit-ee-mapping.md) §3,§6 + [`ohmic-decoherence-born.md`](../../vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md):11 |
| **Double-slit: which-path detector / observer** | **resistive load $Z_{det}$** (Joule sink); $W_{extracted}\propto\lvert\partial_t\mathbf{A}\rvert^2/Z_{det}$ thermalizes the phase wave (Ohmic decoherence) | [`double-slit-ee-mapping.md`](../../vol1/dynamics/ch3-quantum-signal-dynamics/double-slit-ee-mapping.md) §4 + [`ohmic-decoherence-born.md`](../../vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md):18,23,34 (clm-ldmvwi) |
| **Double-slit: fringe visibility vs detector impedance** | **continuous decoherence** — $V$ vs $Z_{det}$ continuous (Γ-detune), vs Copenhagen binary collapse (**AVE-distinct falsifiable prediction**) | [`double-slit-ee-mapping.md`](../../vol1/dynamics/ch3-quantum-signal-dynamics/double-slit-ee-mapping.md) §5 |
| **Cosmic-temperature evolution of $\alpha$** | Crystal oscillator frequency vs $T$ (substrate's analog of frequency-temperature curve) | clm-009nkt + related |
| **Aharonov-Bohm phase** | Magnetic-flux-modulation of conduction-electron interference (canonical EE phenomenon) | Vol 2 quantum canonical |
| **Vacuum thermal noise floor** | Johnson-Nyquist thermal noise at vacuum baseline ($k_B T_{CMB}$ per mode per Hz) | [`translation-stochastics.md`](translation-stochastics.md) FDT cross-link |
| **dark wake (far-field reaction)** | far-field radiated shear stress **$\tau^{\text{far}}_{zx}$** (Maxwell/Cauchy stress; $\int \tau\, dA = F$; real-space reaction-momentum trail) | ✓ cross-ref [`chiral-thrust-derivation.md`](../../vol4/circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md) (clm-7tynm2) |
| **dark resonance (near-field reaction)** | near-field reactive self-energy **$\Sigma_{\text{near}}$ / $-\dot\Sigma_{\text{near}}$** (QED self-energy analogue; armature-reaction-induced d/q saliency → electron $g$-2 anomalous moment) | cross-ref [`q-g19a-petermann-saliency-closure.md`](../../vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md) (clm-v2sg8z) + [`dark-back-reaction-taxonomy.md`](../dark-back-reaction-taxonomy.md) |
| **Casimir cavity / lattice-mode cavity dispersion** (parallel-plate boundaries) | **Waveguide/cavity below cutoff** (*mechanical high-pass filter*): long-$\lambda$ modes below $f_c = c/2d$ are excluded/evanescent (Op16; §4.5 below-cutoff row); finite mode sum to lattice band-edge $f_{\max} = c/(\pi\ell_{node})$ ($\omega_{\max}=2c/\ell_{node}$); the mode-energy-density differential vs free field = net inward **Maxwell stress** ($\int\tau\,dA = F$, §6 #24) → $-\pi^2\hbar c/240d^4$ | **consistency-class** (relabeled mechanism, NOT a QED discriminator; 2026-06-03 walk-back [`c989f970`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/c989f970)); [`casimir-effective-temperature.md`](../../vol3/condensed-matter/ch11-thermodynamics/casimir-effective-temperature.md) + AVE-Metamaterials Ch.6/8 |
| **Electron flux confinement / fluxoid** (frozen-flux distributed collimation) | **London / Abrikosov superconducting vortex.** $R=0 \Rightarrow d\Phi/dt = IR = 0$ in every surrounding lossless cell ⇒ each conserves its (zero) flux forever ⇒ collimation is DISTRIBUTED, no wall required. Anatomy (one-to-one): phase-winding axis $=$ Link $\in\mathbb{Z}=$ charge (boundary data); saturated D3 yield-envelope core $\approx$ the SC normal-core ($\xi$) analog; screening circulation to the far field $=$ the mass energy $\tfrac12 L I^2$; **fluxoid quantization $=$ charge quantization**; Ax3 lossless $=$ the $R{=}0$ persistence. **Disanalogy that matters:** SC flux-flow DISSIPATES (resistive normal core); the vacuum core is Ax3-REACTIVE ⇒ lossless motion (free electrons). | ⚠ **WALKED-FRAMING grade (W4, #606** — [`2026-07-09_fast-sector-settling-boundary-conditions_walked-framing.md`](../../../../research/2026-07-09_fast-sector-settling-boundary-conditions_walked-framing.md) W4, **FRAMING, not canon)**. Canonical confinement side (Γ=−1 T2 wall): [`electron-identification.md`](../../vol2/particle-physics/ch01-topological-matter/electron-identification.md). **OPEN (kernel-checkable, NOT canonized):** the type-II / κ surface-energy *sign* of $S(A)=\sqrt{1-A^2}$ — a negative (effective type-II) sign would DERIVE the granularity of charge (one quantum per filament); the 0-for-N hopeful-forms prior applies. |
| **Equivalence principle** (gravitational charge $\equiv$ inertial mass) ⚠ regime-tag | **CMRR — COUPLING-level common-mode rejection.** CMRR **infinite BY IDENTITY**: nothing to mismatch under a uniform (common-mode) drive; the **tide is the DIFFERENTIAL mode**. Regime: **A1 gravity, sub-yield.** **DISTINGUISH from the $\varepsilon$-sector gauge rider = READOUT-level CMRR** (same instrument word, DIFFERENT mechanism): a common-mode / uniform-bias $E$ **LOADS the Q-point but reflects nothing** ($\nabla A=0$). Coupling-level (EP) vs readout-level (gauge rider) is the axis. | WEP-CMRR $\sim10^{-15}$ (Eötvös / MICROSCOPE), SEP-CMRR $\sim10^{-4}$ (LLR-Nordtvedt); gauge rider [`claim-quality.md`](../../vol4/claim-quality.md):1856 ("uniform-bias gauge rider does NOT rescue the muon, $\nabla A\ne0$"); originating leaf = EP-CMRR acceptance test [`…_prereg_FROZEN.md`](../../../../research/2026-07-11_ep-cmrr-acceptance-test_prereg_FROZEN.md) + `src/tests/engine_acceptance/test_ep_cmrr.py`. **Consistency / register class; no chord mint.** |

This table is the canonical first-call reference for substrate-primitive → EE-component lookup. Where a row's EE mapping is canonical at a referenced leaf, the leaf carries the derivation; this catalog enumerates the mapping without re-deriving.

---

## §4.5 — EE Analytical Tool ↔ Operator ↔ Validation Tracker (living)
<!-- claim-quality: clm-eemap1 -->

### (a) Purpose + validation legend

§4 maps substrate-*primitive* → EE-*component* (charge → capacitor, bond → transmission line, Cosserat couple-stress → transformer mutual-L). This section is the **tool-axis complement**: it maps an EE analytical **tool** (impedance analysis, reflection, S-parameters, Q-factor, harmonic balance, modal decomposition, PLL, …) → the AVE **operator(s)** it lands on → whether that mapping is **validated**. Where §4 answers *"what substrate primitive is this component?"*, this tracker answers *"when I reach for this EE analytical method, which Op# am I actually invoking, and is that correspondence solid or just implied?"*

It is **living** and maintained per `ave-ee-first-mapping` v1.2 Step 6b: when an EE analytical tool is *used* or *established* in a substrate-physics derivation, its row + validation mark are added or updated here.

**Validation legend** (the validation column IS the review surface — audited via `ave-sweep-audit`, the same means-test discipline as §6; ✓ is reserved for genuine identity / canonical derivation, never aspiration):

- **✓** — genuine identity or canonical derivation. The EE tool reduces to the named operator(s) by an exact identity (e.g. $Z_0 = \sqrt{\mu_0/\varepsilon_0}$) or a canonical leaf derives the correspondence end-to-end.
- **⚠** — partial / scattered / used-but-not-consolidated. The mapping is real and used in the corpus but is implied rather than explicit, or lives scattered across leaves without a single consolidating derivation.
- **✗** — gap. No operator mapping exists yet, or the only candidate anchor is invalidated. These rows are the work-queue, not claims.

> **Operator-citation provenance.** Every Op# below was grep-verified against [`operators.md`](../operators.md) §2 (the canonical 22-operator catalog) and the §4 catalog above at section-authoring time (`verify-before-cite`). No operator-number corrections were required — all eleven distinct operators referenced (Op1, Op2, Op3, Op5, Op6, Op13, Op14, Op16, Op17, Op21, Op22) match their canonical formulae in `operators.md` §2 (Op5 = Multiport Y-to-S / K4-TLM scatter+connect, added 2026-07-09 with the band-structure row).

### (b) The matrix (grouped by EE family)

#### Impedance & transmission

| EE tool | AVE operator(s) | Validation | Anchor / note |
|---|---|---|---|
| Impedance $Z$ / admittance $Y$ | Op1 ($Z = \sqrt{\mu/\varepsilon}$) + Op14 ($Z_{eff} = Z_0/\sqrt{S}$) | ✓ | Op1 identity ([`operators.md`](../operators.md):41) + Op14 canonical ([`operators.md`](../operators.md):54) |
| Reflection $\Gamma$ | Op3 ($\Gamma = (Z_2 - Z_1)/(Z_2 + Z_1)$) | ✓ | canonical ([`operators.md`](../operators.md):43) |
| S-parameters / $S_{11}$ | Op3 + K4-TLM scatter $S^{(0)}_{ij}$ | ✓ | $S_{11}$ canonical (Op3); K4-TLM scatter unitary to machine epsilon ([`k4-tlm-simulator.md`](../../vol4/future-geometries/ch13-future-geometries/k4-tlm-simulator.md), exact 4-port via Op5) |
| 3-port junction / tee scattering (matched-lossless-reciprocal-3-port theorem) | Op3 ($S_{11}$) + Op6 ($\lambda_{min}(S^\dagger S)\to0$) | ✓ | **The srs $z=3$ vertex = an intrinsically MISMATCHED reciprocal 3-port.** A wave down one bond sees the other two in parallel ($Z_0/2$), so the bare junction reflects $\Gamma=(2-z)/z=-1/3$ (a COUNTING fact — one bond feeding two, immune to symmetric transformation), reactively back-scattering / redistributing $|\Gamma|^2=1/9$ of the power (Axiom 3 — **reactive, not loss**). The floor $|S_{11}|\ge1/3$ is the classic **matched-lossless-reciprocal-3-port theorem** (Pozar §7.1 class) — attributed known theory, **confirmed at the vertex** (exact perfect-square identity), so Op6's reflectionless target $\lambda_{min}\to0$ is **UNREACHABLE by any bore of the LOSSLESS reciprocal class**. **The matched alternative is the non-reciprocal circulator** ($S_{11}=0$, unitary, $C_3$; the reciprocal-class evanescent-stub escape is theorem-dead, #620) — needs a **T-breaking** bias (candidate $u_0^{*}/\Omega_{\text{freeze}}$; srs $I4_132$ chirality is only P-breaking) — **PENDING-GRANT**, asserted nowhere. The ✓ is the geometry-independent theorem confirmation (a known identity, canonical leaf); the two-axis Op6 bore verdict (broadband $f^{*}=0$ unique; single-frequency $\{0, f_{\text{touch}}=\sqrt2/\pi\}$ degenerate — half-wave-invisible bore family) is "demonstrated, not adjudicated". Canonical: [`srs-vertex-scattering.md`](../../vol1/operators-and-regimes/ch6-universal-operators/srs-vertex-scattering.md) (`clm-v3port` floor, `clm-bore2x` bore verdict; X38/X37, PR #619/#616/#620) |
| I/Q quadrature / forward–backward $(V_{inc}, V_{ref})$ phasor decomposition | Op3 + K4-TLM scatter — the **intra-K4 linear $E$↔$B$** | ⚠ | the bond's incident/reflected voltage waves ARE the photon's own quadrature: $E \sim (V_{inc}+V_{ref})$, $B \sim (V_{inc}-V_{ref})/Z$ — a LINEAR $E$↔$B$ internal to the K4 sector (distinct from the *parametric* K4↔Cosserat bridge in the Resonance family). Code-confirmed (`k4_tlm.py`:192-206, 340, 400); **consolidating canonical leaf landed 2026-06-04: [`photon-ee-mapping.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md) §4** (row stays ⚠ not ✓ — consolidation is a description, not an emergence derivation). Gate (a) 2026-06-04 ([`…alpha-quarter-hypothesis.md`](../../../../research/2026-06-04_ee-rf-quadrature-coupling-and-alpha-quarter-hypothesis.md) §8). NB: the $R{\cdot}r=1/4$ phasor-radius question that lives in this sector is a *separate* claim — **gate (b) RESOLVED-NEGATIVE 2026-06-04**: the kinematic phasor↔real-space area bijection does NOT lift it (Class B, α-substituted; bridge forces R·r→4π²α ≠ ¼; [`bijection-result`](../../../../research/2026-06-04_alpha-class2-bijection-result.md)). This row asserts only the linear-quadrature decomposition (gate (a), separate) |
| Transmission line (ABCD, propagation) | Op1 + Op13 ($\Box^2$) + Op16 ($c_{shear}$) | ✓ | $Z_0$-ladder ([`z0-derivation.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md)); K4-TLM cascade; Op13/Op16 in [`operators.md`](../operators.md):53,56 |
| Power transfer / matched-$Z$ | Op17 ($T^2 = 1 - \Gamma^2$) | ✓ | identity ([`operators.md`](../operators.md):57) |
| Smith chart ($Z \leftrightarrow \Gamma$) | Op1 + Op3 | ⚠ | explicit Smith-chart leaf landed 2026-06-13: [`cvr-reflection-smith.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md) — the $\Gamma(A_0)$ matched→short locus, $|\Gamma|^2=1-\alpha$, chiral 2×2 $S$. ⚠ not ✓ (consolidation/description, not emergence) |
| Network theorems (Thévenin / Norton, 2-port) | Op1 / Op3 + §8 ladder networks | ⚠ | partial — ξ_topo ladder + Op5 multiport exist; Thévenin/Norton reduction not consolidated |

#### Resonance / nonlinear / wave

| EE tool | AVE operator(s) | Validation | Anchor / note |
|---|---|---|---|
| Q-factor / resonance | Op21 ($Q = \ell$) + Thm 3.1′ ($Q = \alpha^{-1}$) | ✓ | $\alpha^{-1} = Q_{tank} = 4\pi^3 + \pi^2 + \pi$ exact ([`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md):15); Op21 in [`operators.md`](../operators.md):61 |
| Filter theory / transfer fn $H(s)$ | Op17 + ladder | ⚠ | general $H(s)$ now mapped 2026-06-13: [`cvr-transfer-function.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-transfer-function.md) — the 2×2 chiral $H(s)$, pole pair $-\alpha\omega_0/2\pm j\omega_d$, $Q=1/\alpha$, BW$=\alpha\omega_0$. ⚠ not ✓ (consolidation) |
| Harmonic balance / IMD (IP3) | Op2 ([`operators.md`](../operators.md):42) + intermodulation-distortion leaf | ✓ | $V_{IP3} = \sqrt{4/3}\,V_{yield} \approx 50.4$ kV ([`intermodulation-distortion.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md):50) |
| Mixer / difference-tone conversion (two-tone → beat; inversion-symmetry meter) | Op2 ([`operators.md`](../operators.md):42) — the odd-$\chi^3$ kernel parity | ✓ | **Parity identity (geometry-independent):** the even Ax-4 kernel $\Rightarrow$ odd restoring force $\Rightarrow$ a combination tone at $m\omega_{lo}+n\omega_{hi}$ is allowed iff $m+n$ is odd, so the literal difference tone $\omega_{hi}-\omega_{lo}$ is **FORBIDDEN** sub-yield (by inversion symmetry, *reactive*/lossless — not suppressed). The difference channel is an **inversion-symmetry meter**: the vacuum as a biased-varactor difference-tone mixer, conversion $\propto$ bias — a planted even-$\chi^2$ term lights the forbidden tone $\propto\beta^2$ (exponent 2.000, $R^2 = 0.99999999$). Canonical: [`universal-saturation-kernel-catalog.md` § The parity theorem](../universal-saturation-kernel-catalog.md) (`clm-invmtr`); A⁶ χ³ fingerprint `clm-a6chi3`. **A1↔T2 calibration bridge — PENDING-GRANT:** the bias-calibration route via $C_{ss}=C_0/S^3$ ([`node-up-small-large-signal.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md):106, `clm-vca7r1`) cites an **A1-longitudinal** tangent, but this meter reads a **T2-transverse** observable — whether the frozen bias $u_0^*$ enters the transverse channel through the A1 tangent, a T2-native tangent, or a cross-sector coupling is PENDING-GRANT (first question of the D-II calibration batch; the cross-wire is not licensed without the bridge). **SCOPE:** the ✓ is the parity identity; the *frequency form factor* (χ³ vertex vs ω above band) is **interface-scoped / BULK OPEN** (fork A, PR #610 — at sep$\ge$3 the co-located interface reading was the artifact and the beat collapses $\approx$17.1 orders tracking physical skin suppression), NOT part of this identity |
| Varactor / nonlinear $C(V)$ | Op2 / Op14 ($S(A)$ dielectric specialization) | ✓ | $C_{eff} = C_0/S(A_0)$; PONDER-05 (DC-biased quartz, 27.4% at ~30 kV) is a material-scale consistency analog of the kernel SHAPE, NOT a vacuum-kernel tester — $V_{DC}/V_{yield} = 0.687$ is a per-node ratio (`claim-quality.md:51`) |
| Degenerate parametric amplifier (pump → signal/idler) | Op14 + $W_{refl}$ bridge (K4-$V^2$ → Cosserat-$\omega$) | ⚠ | the K4↔Cosserat coupling $W_{refl}\propto V^2\!\cdot\! f(\omega)$ is **even in $\omega$** ⇒ $\partial_\omega W\big|_{\omega=0}=0$, an exact $\omega{=}0$ fixed point: a parametric pump that CANNOT seed the $\omega$-idler from zero (**Q0**). This IS the canonical **pair-production** coupling (matter spin from a *seeded* $\Gamma\!\to\!-1$ rupture), NOT an additive forcing term — a linear $V$→$\omega$ term would manufacture spin below threshold (wrong physics). A **description of the coupling structure, NOT an emergence claim.** Code-confirmed (`k4_cosserat_coupling.py`:118, `cosserat_field_3d.py`:466); gate (a) 2026-06-04 (research §8), Grant-adjudicated canonical. Generalizes the Varactor row (a pumped varactor IS a parametric amp) |
| Avalanche / breakdown (Miller) | Op22 ($M = 1/S^2$) | ✓ | identity ([`operators.md`](../operators.md):62) |
| Nonlinear inductor $L(I)$ | relativistic-inductor leaf | ✓ | $L_{eff}(I) = L_0/\sqrt{1 - (I/I_{max})^2}$; $E = mc^2$ from inductor energy ([`relativistic-inductor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md)) |
| Modal / eigenmode decomposition | Op6 ($\lambda_{min}$) + Op13 | ✓ | eigsolves at corpus GT; Op6/Op13 in [`operators.md`](../operators.md):46,53 |
| Regenerative / positive-feedback loop (Black's closed-loop gain $A/(1-\beta A)$) | baryon self-consistent mass eigenvalue: dual-reactance loop, $x = \mathcal{I}_{scalar}/(1 - \mathcal{V}\,p_c) + 1$ | ⚠ | the $1/(1-\mathcal{V}\,p_c)$ regenerative form IS Black's closed-loop gain with loop-gain $\beta A = \mathcal{V}\,p_c$ and $\mathcal{V} = 2$ = the count of the node's two reactance sectors ($X_L + X_C$, each one electron-unit); **count-2 closed** (mass-confirmed, $\mathcal{V}=2 \to 1836.117\,m_e$); **per-channel coupling $k=1$ closed** via Op17 matched-impedance (Axiom-3 $\Gamma=0$ at the orthogonal Borromean crossing — *assumption removed*, R2 2026-06-01); residual narrows to the **$p_c=8\pi\alpha$-as-feedback-fraction** identification (separate, pre-existing). Anchor: [`dual-reactance-storage-taxonomy.md`](../dual-reactance-storage-taxonomy.md) + [`2026-06-01_baryon-V2-dual-reactance-closure.md`](../../../../research/2026-06-01_baryon-V2-dual-reactance-closure.md) + [`2026-06-01_baryon-R2-crossing-coupling-result.md`](../../../../research/2026-06-01_baryon-R2-crossing-coupling-result.md); §6 #25 |
| Transformer / mutual-L / leakage | Cosserat $\gamma_c$; $l_c = \sqrt{\gamma_c/G_{vac}}$ | ✓ | leakage-inductance length = weak-force range ([`gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md):39) |
| Memristor / hysteresis | $\tau_{relax}$ + Cosserat-B phase-lock memory | ✓ | memristive relaxation ODE ([`tau-relax-derivation.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/tau-relax-derivation.md) + [`nonlinear-vacuum-capacitance.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md)); B-sector phase-lock memory per §9.2 |
| WKB tunneling / barrier penetration | Op16 ([`operators.md`](../operators.md):56; $c_{shear} = c_0\sqrt{S}$) + ASYM-saturation EM-evanescent ($c_{EM} = c_0/\sqrt{S}$ at $S < 1$, sub-threshold field) | ⚠ | canonical but scattered, not consolidated as one tool→operator row: classically-forbidden ↔ evanescent decay ([`ode-verification.md`](../../vol2/quantum-orbitals/ch07-quantum-mechanics/ode-verification.md):51, [`de-broglie-standing-wave.md`](../../vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md):42); ASYM EM-evanescent ([`claim-quality.md`](../../claim-quality.md):112); plasma below-cutoff ([`temporal-saturation-regime-classifier.md`](../temporal-saturation-regime-classifier.md):100); W/Z as "evanescent cutoff excitations" ([`gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md):52). #2 cold-fusion Gamow coordinate-compression ($n_{scalar} = 1/S$) is the same mapping (surfaced by the 2026-05-31 EE-mapping self-audit). **Casimir** parallel-plate cavity below cutoff $f_c = c/2d$ excludes long-$\lambda$ modes (= *mechanical high-pass filter*; net force via Maxwell stress, §6 #26) — consistency-class, 2026-06-03 walk-back; see §4 Casimir row |
| Band-structure / dispersion survey (Bloch/Ybus + coined-quantum-walk arccos spectral map) | Op5 (K4-TLM scatter+connect [`operators.md`](../operators.md):45) + Op6 ($\lambda_{min}$ eigenmode :46) + Op16 (velocity gate :56) | ✓ | **VALIDATED (gate-passed, #604/#607).** The substrate-native band model is the transmission-line **arccos** (coined-quantum-walk) map $\omega=\omega_{link}\arccos(\mu/3)$, NOT the graph-Laplacian $\omega=\sqrt\lambda$ (which FAILS the $1/\sqrt3$ velocity gate, giving $1/\sqrt2$). Consolidating canonical leaf: [`srs-band-structure.md`](../../vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md) (clm-bnd5rq) — scalar top $\pi\sqrt3=5.441\,\omega_C$ at $H$, vector top BRACKET $[5.441,17.011]\,\omega_C$, NO internal gap either channel |
| Slew rate / full-power bandwidth (large-signal rating) | Op14 ($\mu$-grade, $Z_{eff}=Z_0/\sqrt S$; [`operators.md`](../operators.md):54) | ✓ | **algebraic identity only:** the normalized slew $A_I=\dot E/(E_c\omega_0)=(E/E_c)(\omega/\omega_0)$ is the vacuum's full-power-bandwidth rating at the FPB corner $(\omega_0,E_c)$ — the $\mu$-kernel (slew-rate) rating dual to the $\varepsilon$-kernel $S(A)$ (output-swing) rating (FPB note #595). ✓ is for the **algebra**; the physical "$\mu$-kernel-as-a-second-rating" FRAMING **and** the above-$\omega_0$ hard-cutoff-vs-power-law closure stay **#595-UNMERGED framing, NOT canon** ([`lattice-model-register.md`](../lattice-model-register.md) slew-identity pointer, "do not treat the slew identity as derived") |

#### Control & feedback (the gap cluster)

| EE tool | AVE operator(s) | Validation | Anchor / note |
|---|---|---|---|
| FOC / Park (d/q) transform | (2,3) phase-space d/q → dark resonance ($\Sigma_{near}$) | ⚠ | just disambiguated (dark-resonance d/q saliency, §4 row + §6 #23); not yet a clean tool→operator row — the d/q *transform itself* as an analytical tool is not consolidated |
| PLL / phase-locked loop | Op14 cross-sector trading ($\rho = -0.990$) — candidate | ✗ | GAP — no PLL→operator row. **Note:** the $\rho = -0.990$ result ([`op14-cross-sector-trading.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md):11) is Cosserat↔K4-inductive *energy-trading* anti-correlation, NOT a validated phase-lock; phase-lock content is scattered across Kuramoto ([`kuramoto-phase-locking.md`](../../vol3/condensed-matter/ch09-condensed-matter-superconductivity/kuramoto-phase-locking.md)) + FOC with no consolidating row |
| Autoresonance / self-resonance | soliton self-lock ($\Gamma = -1$ + Op21) — candidate | ✗ | GAP — not mapped. The only autoresonant-PLL leaf ([`ch15-autoresonant-breakdown/theory.md`](../../vol4/simulation/ch15-autoresonant-breakdown/theory.md)) is ⛔ INVALIDATED (computed against wrong $60$ kV threshold, not canonical $V_{yield} = 43.65$ kV); self-lock at the TIR boundary — its **genesis-self-lock-from-a-flowing-photon-precursor application** was **TESTED-NEGATIVE 2026-06-14** (T2 on `crystal_engine`, near-yield-forming; NO-GENESIS at every $A_0 \in \{0.69, 0.78, 0.866, 0.95\}$; [`research/2026-06-14_t2-genesis-selflock_result.md`](../../../../research/2026-06-14_t2-genesis-selflock_result.md), commits `0affe18e`/`09722e2b`). That tests **one application, not the mapping**: the general autoresonance↔substrate mapping stays **unmapped**, and the **PLV/autoresonance detector instrument is defective** (LOCK unreachable by *any* positive — the known self-focusing sech bins UNRESOLVED at PLV ≈ 0.53 ≈ the photon arms), **phasor-redesign prereg deferred**. The eigenmode STRUCTURE is now mapped descriptively in [`cvr-stability-eigenmode.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-stability-eigenmode.md) (2026-06-13), but the self-lock stays underived — row stays ✗ |
| Control / stability (Nyquist, root-locus) | Op14 feedback loop — candidate | ⚠ | Nyquist/root-locus STRUCTURE mapped 2026-06-13: [`cvr-stability-eigenmode.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-stability-eigenmode.md) — descriptive eigenmode geometry (poles → $j\omega$ axis as $Q\to1/\alpha$; Nyquist eigenmode loop). ⚠ not ✓ — the feedback-stability CRITERION is descriptive, not yet derived |

#### Noise / numerical

| EE tool | AVE operator(s) | Validation | Anchor / note |
|---|---|---|---|
| Noise (Johnson-Nyquist, FDT, 1/f) | translation-stochastics (FDT = boundary-$Z$ thermalization) | ✓ | vacuum thermal floor at $k_B T_{CMB}$ per mode per Hz ([`translation-stochastics.md`](translation-stochastics.md); §4 + §6 #22) |
| Numerical CEM (FDTD / TLM / FEM / MoM) | §9 toolkit-index (K4-TLM, CEM-survey) | ✓ | six CEM methods → AVE lattice ([`cem-methods-survey.md`](../../vol4/future-geometries/ch13-future-geometries/cem-methods-survey.md)); K4-TLM direct isomorphism |

### (c) The gap-finding

Tally across the four families: **19 ✓ solid, 9 ⚠ partial, 2 ✗ gaps** (30 rows; 2026-07-10: +1 ✓ in the Impedance & transmission family — the srs **$z=3$ vertex 3-port** ↔ Op3 + Op6, the **matched-lossless-reciprocal-3-port theorem** confirmed at the vertex ($\Gamma=-1/3$ counting fact, $|S_{11}|\ge1/3$ floor = $1/9$-power reactive branch back-scatter; the circulator is the **non-reciprocal matched alternative**, T-breaking PENDING-GRANT; two-axis Op6 bore verdict demonstrated-not-adjudicated; X38/X37, `clm-v3port`/`clm-bore2x`). 2026-07-10: +1 ✓ in the Resonance/nonlinear/wave family — the **difference-tone mixer / inversion-symmetry meter** ↔ Op2 odd-$\chi^3$ parity (PR #610, `clm-invmtr`); the ✓ is the geometry-independent parity identity (difference tone forbidden sub-yield), while the *frequency form factor* stays interface-scoped / bulk-open. 2026-07-09: +2 ✓ in the Resonance/nonlinear/wave family — the srs **band-structure / dispersion survey** ↔ coined-quantum-walk / TLM arccos map (gate-passed #604/#607, clm-bnd5rq) and the **slew-rate / full-power-bandwidth** algebraic identity ($A_I=\dot E/(E_c\omega_0)$; #595 — algebra ✓, physical FPB framing stays unmerged). 2026-06-13 update — the Smith-chart + general-$H(s)$ ⚠ rows gained explicit consolidating CVR leaves, and Nyquist/root-locus flipped ✗→⚠ via the CVR stability-eigenmode leaf's descriptive structure; the 2026-06-04 ⚠ pair was I/Q phasor + degenerate parametric amp). 2026-06-14: the autoresonance gap's *genesis-self-lock application* is now TESTED-NEGATIVE (T2), but the row stays ✗ and the tally stays **2** — the mapping + the PLV/autoresonance detector instrument remain open (phasor-redesign prereg deferred); a tested-negative application is not a resolved mapping. The structurally load-bearing observation is that **the remaining ✗ are both in the control / feedback family** (PLL, autoresonance — stability closed to ⚠) — but they split by anchor: **PLL + stability point at Op14** (Dynamic Impedance / cross-sector feedback), while **autoresonance is a distinct Op21 + Γ=−1 self-lock gap** (per the matrix row). The control-loop axis is the next mapping frontier:

- **PLL** — the $\rho = -0.990$ cross-sector-trading result is energy-exchange evidence, not a phase-lock derivation; phase-lock content is scattered (Kuramoto, FOC) with no consolidating row.
- **Autoresonance** — the one autoresonant-PLL leaf is invalidated (wrong yield threshold); the soliton-self-lock-from-a-photon-precursor *application* is now **TESTED-NEGATIVE** (2026-06-14, T2 on `crystal_engine` near-yield, NO-GENESIS), while the *general mapping* stays unmapped and the autoresonance *detector instrument* is defective (phasor-redesign prereg deferred) — row stays ✗ (a tested-negative application is not a resolved mapping).
- **Stability (Nyquist / root-locus)** — the descriptive eigenmode structure now exists ([`cvr-stability-eigenmode.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-stability-eigenmode.md), 2026-06-13: root-locus + Nyquist loop); ⚠ not ✓ — a *derived* substrate-native feedback-stability criterion is still open.

This is a clean diagnosis: the corpus has strong open-loop coverage (impedance, resonance, saturation, wave, mode) and a coherent *closed-loop control* gap — PLL + stability anchoring on Op14, autoresonance on Op21 + the Γ=−1 boundary. That cluster is the work-queue. (2026-06-14: the autoresonance gap's genesis-self-lock application is tested-negative; the remaining autoresonance work is the PLV-detector phasor-redesign prereg + the general EE↔AVE mapping, not the genesis application.)

### (d) Maintenance note

This tracker stays current per `ave-ee-first-mapping` v1.2 **Step 6b**: when an agent **uses or establishes** an EE-tool↔operator mapping in a substrate-physics derivation, add (or update) its row here with a validation mark, then `verify-before-cite` the operator number against [`operators.md`](../operators.md) §2. The validation column is the review surface — fire `ave-sweep-audit` over the tracker periodically (or when a batch of rows lands) to confirm every ✓ is a genuine identity / canonical derivation and every ⚠ / ✗ is still current (e.g. an ✗ flips to ✓ when its gap closes; a ⚠ flips to ✓ when a consolidating leaf lands).

> Companion axes: [`ave-analytical-toolkit-index.md`](../ave-analytical-toolkit-index.md) is the *problem-class → AVE-tool* side (when starting a derivation, which Op# applies); this §4.5 is the *EE-tool → operator → validation* side (when reaching for a named EE method, which Op# + is it solid). [`operators.md`](../operators.md) is the canonical Op1–Op22 set both reference.

### (e) Canonization candidates — gate (a) RUN 2026-06-04 (split verdict; do NOT promote to ✓ until the α-emergence gates b+c pass)

Surfaced 2026-06-04 via `ave-ee-first-mapping` on the photon→electron engine arc (the Q0 parametric-decoupling finding); full record + the crystal-clear vocab/math map in [`2026-06-04_ee-rf-quadrature-coupling-and-alpha-quarter-hypothesis.md`](../../../../research/2026-06-04_ee-rf-quadrature-coupling-and-alpha-quarter-hypothesis.md) (§8 = gate (a) outcome). **Gate (a) split the set in two:** the *descriptive* mappings (what the engine factually does — read from code) PASSED and are KB-eligible; the *α-emergence* mappings stay ⚠-pending gate (b) and still CONTRADICT the honest-α Class-B verdict (2026-06-02: the substrate does NOT independently select R·r=1/4). Grep-discoverable breadcrumbs:

**The load-bearing disambiguation (gate (a)'s headline clarity).** There are **two distinct "magnetic" DOFs and two distinct E↔B couplings** — do not conflate them:
- **(I) Intra-K4, the photon's own E↔B — LINEAR, PRESENT:** `V_inc/V_ref ↔ Φ_link` via TLM scatter+connect (`k4_tlm.py:340,400`). E ~ (V_inc+V_ref), B ~ (V_inc−V_ref)/Z, locked by the line impedance. *This is where the 1/4 phasor lives.*
- **(II) K4↔Cosserat bridge, photon → matter spin — PARAMETRIC, CANONICAL:** V² modulates the saturation varactor in `W_refl` (`A²_ε ⊃ V²/V_SNAP²`), it does not torque ω; even in ω ⇒ ω=0 is an exact fixed point. This is **pair-production** (matter spin from a seeded Γ→−1 rupture), not a bug. Three engines carry these: K4-TLM (`k4_tlm.py`, the photon, linear), Cosserat (`cosserat_field_3d.py`, ω = matter spin, bridged via W_refl), Maxwell-FDTD (`fdtd_3d.py:285,309`, clean curl E↔H reference, no (2,3) carrier).

**Per-term dispositions:**
- **Degenerate parametric amplifier** ↔ Op14/W_refl bridge (K4-V → Cosserat-ω): the V²-even-in-ω coupling is a parametric pump that cannot seed the ω-idler from zero (Q0; `k4_cosserat_coupling.py:118`). **Gate (a) PASSED as a DESCRIPTION** — but RE-SCOPED: this is the *canonical pair-production* coupling, NOT an engine artifact. KB-eligible. → ✅ **PROMOTED 2026-06-04 to §4.5(b) Resonance/nonlinear/wave family as a ⚠ row** (consolidating canonical leaf landed 2026-06-04: [`photon-ee-mapping.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md) §4.1, the coupling-(II) disambiguation; ⚠ not ✓).
- ~~**Linear LC / transformer E↔B is a MISSING term**~~ — **REFUTED by gate (a).** The linear E↔B exists *intra-K4* (`V↔Φ_link`); the K4↔Cosserat bridge is *correctly* parametric. The original "missing-coupling" diagnosis conflated couplings (I) and (II). Struck.
- **I/Q quadrature** ↔ (V_inc,V_ref) (`k4_tlm.py:192-193`); the photon's E+B both live in the K4 sector. **Gate (a) PASSED.** KB-eligible. → ✅ **PROMOTED 2026-06-04 to §4.5(b) Impedance & transmission family as a ⚠ row** (consolidating canonical leaf landed 2026-06-04: [`photon-ee-mapping.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md) §4; ⚠ not ✓).
- **Half/quarter-wave resonator** ↔ Γ=−1 boundary (antinode pinned at the cell edge) — refines the §4 "open-circuit / total-reflection" row. **Gate (b) RAN 2026-06-04 (adversarial re-challenge): CLOSED.** Retained as the **DESCRIPTION** of the electron's trapped-reactive-energy structure (the most-fundamental EE mapping — a shorted λ/4 resonator = a half-Γ-lap on the Smith chart); it does **not** derive R·r=¼ (next row).
- ~~**R·r = 1/4 = (Nyquist half-cell)²** — candidate EMERGENT origin~~ — **CHALLENGE-CLOSED 2026-06-04 (Class B hardened).** The seeded-crystallization / ideal-vs-noisy reframe was tested against every prior α-¼ attempt and **FALSIFIED** (the 4 α-lift tests were *seeded* not cold → no relaxation to ¼; the dynamical-AC dressed-eigenmode route was already run 2026-06-02 → flat). R·r=¼ stays a **named identification the substrate does not independently select** (Class B, `clm-0ktpcn`). Full record: [`2026-06-04_alpha-quarter-adversarial-rechallenge.md`](../../../../research/2026-06-04_alpha-quarter-adversarial-rechallenge.md).
- **Injection locking** ↔ nucleation rule; **Manley–Rowe** ↔ pump/signal/idler split; **2:3 Lissajous / mode-lock** ↔ the (2,3) winding. **Gate (a) PASSED as descriptions** of the Cos-sector seed/winding; the (2,3)-*emergence* remains a no-seed/pair-production question.

Promotion path: **DONE 2026-06-04** — the two clean code-confirmed descriptive mappings (degenerate parametric-amp↔W_refl bridge; I/Q↔(V_inc,V_ref)) landed as ⚠ rows in §4.5(b) (tally 24→26); the two-sector disambiguation above is the load-bearing context for both. **Held back deliberately** (still candidates, NOT promoted): the **injection-lock↔nucleation** and **2:3-Lissajous↔(2,3)-winding** descriptions — they touch the *open-emergence* (2,3) question, so promoting them would risk an emergence-masquerade; they stay here until the emergence question itself resolves. The **α-emergence mappings (half/quarter-wave, R·r=1/4) clear gate (b)+(c) first.**

---

## §5 — EE vs Fluid Dynamics: substrate-distance comparison

Fluid dynamics is a frequent candidate for substrate-physics framing because the vacuum is often visualized as a "medium." This section makes the substrate-distance comparison explicit: EE captures the substrate at minimal-DOF; fluid dynamics operates at $\sim N$-scales-of-averaging distance from the substrate and adds DOFs the substrate does not carry primitively.

### Substrate-primitive vs Fluid-emergent-DOF comparison

| Quantity / concept | Substrate-native (EE / AVE axioms) | Fluid-dynamics-added DOF |
|---|---|---|
| Carrier of dynamics | LC oscillator at each K4 node (Ax 1) | Mass density $\rho(\mathbf{r}, t)$ — macroscopic-cell averaged |
| Wave propagation | $c_0 = 1/\sqrt{\mu_0 \varepsilon_0}$ (substrate-native) | Sound speed $c_s = \sqrt{\partial P/\partial \rho}$ — emergent from EOS |
| Pressure | Substrate impedance / boundary $\Gamma$ at $\Gamma = -1$ TIR | $P(\rho, T)$ — equation-of-state-derived |
| Viscosity | NOT a substrate primitive — emergent from many-cell coupling | $\eta$ — macroscopic momentum-diffusion |
| Compressibility | $S(A)$ kernel near $A_{yield}$ (substrate-native nonlinearity) | $\kappa = -V^{-1}\partial V/\partial P$ — emergent |
| Multi-species | NOT a substrate concept (vacuum is single substance) | Species-fraction $X_i$ added |
| Surface tension | NOT a substrate primitive — emergent boundary phenomenon | $\sigma$ — molecular-cohesion-derived |
| Turbulence | NOT a substrate-axiom primitive — emergent at high Re | Onset at $\mathrm{Re} \gtrsim O(10^3)$ |
| **Rotational DOF at material point** | **Cosserat microrotation — INDEPENDENT primary DOF (Ax 1)** | **Vorticity $\omega = \nabla \times \mathbf{v}$ — DERIVED from velocity field, NOT independent** |

The bottom row is the load-bearing substrate-mechanism distinction.

### The Cosserat distinction — why fluid dynamics structurally misses the substrate's rotational sector

In **classical Navier-Stokes fluid dynamics**, vorticity $\omega = \nabla \times \mathbf{v}$ is a *derived* quantity — the curl of the velocity field. A fluid material point has no independent rotational DOF; its angular state is whatever the surrounding velocity field gradient determines.

In **Cosserat micropolar mechanics** (Ax 1), microrotation is a *primary* DOF at every material point, independent of translation. Each K4 node carries six DOFs: three translational (E-field origin) AND three microrotational (B-field origin). The microrotational sector is NOT derived from the translational sector; it is independently dynamical. This is the structural substrate-physics reason classical fluid dynamics misses the substrate's full structure: **fluid dynamics has no independent rotational DOFs at material points.**

EE captures both sectors at minimal-DOF: capacitive storage maps to the translational/E sector, inductive flywheel storage maps to the microrotational/B sector, and transformer-flux coupling between them maps to Cosserat couple-stress. Fluid dynamics has no analog of the inductive-flywheel sector at the material-point level; its only rotational content is the derived vorticity field.

### When fluid dynamics IS appropriate for AVE work

Fluid dynamics is the correct emergent framework when the relevant physics operates at **macroscopic-emergent scales** where many-cell substrate averaging is the dominant content:

- **Galactic rotation curves** — galactic-scale substrate-mass-distribution dynamics at $\sim N \gg 10^{60}$ substrate cells
- **Ruptured-plasma black-hole interior** — substrate ruptured above $V_{snap}$; plasma physics (EE-adjacent) applies, and MHD captures bulk flow
- **MHD-like cosmic phenomena** — large-scale magnetized plasma flows
- **Atmospheric / oceanic substrate effects** — atmospheric-pressure-modulated dielectric effects at planetary scale
- **CMB plasma-recombination dynamics** — early-universe plasma-substrate coupling

For substrate-primitive-level work (electron LC tank structure, Q-factor cold-lattice $\alpha^{-1}$ closure, varactor C-vs-V saturation, $(p, q)$ knot-mode topology, transformer leakage-inductance $l_c$ setting weak-force range, Schwinger / Miller avalanche, etc.), EE is the substrate-native primary framing and fluid-dynamics framing is structurally too far from the substrate.

### Means-test: EE vs Fluid for representative substrate-physics phenomena

| Phenomenon | EE framing distance | Fluid-dynamics framing distance | Verdict |
|---|---|---|---|
| Cold-lattice $\alpha^{-1}$ from Q-factor | Substrate-native (cosmic LC Q) | Many-scales-removed (no fluid analog) | **EE** |
| Saturation kernel $S(A)$ | Substrate-native (varactor C-vs-V) | Possibly via shock compressibility, much weaker | **EE** |
| Cosserat rotation-sector mass-gap | Substrate-native (transformer cutoff / Curie) | No fluid analog | **EE** |
| Topological $(p, q)$ winding | Substrate-native (transformer windings) | No fluid analog | **EE** |
| Galactic rotation curves | Substrate-mass-distribution; bulk-flow appropriate | Substrate-native at macroscopic scale | **fluid / MHD** (emergent) |
| BH-interior ruptured plasma | Substrate ruptured; plasma EE applies | MHD bulk flow appropriate | **plasma / MHD** (emergent EE-adjacent) |
| $\delta_{strain}$ at $T_{CMB}$ | Substrate-native (TCC + Cosserat-Curie-frozen $\mu$) | Many-scales-removed | **EE** |
| Born-rule click probability | Substrate-native (detector-capture work-function at Joule boundary) | No fluid analog | **EE** |

---

## §6 — Means-test corpus — validated cross-checks

The canonical cross-checks that establish the EE-as-substrate-native mapping is robust. These cases replicate via EE first-principles AND via independent substrate-primitive derivation. They constitute the empirical validation that supports the META framework as Class B substrate-mechanism manifestation.

| # | Substrate prediction | EE analog | Validation status | Canonical anchor |
|---|---|---|---|---|
| 1 | Cold-lattice $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ | Cosmic LC tank Q-factor at $S_{11}$-min Golden Torus | $\checkmark$ exact (Theorem 3.1) | [`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) |
| 2 | Vacuum $Z_0 \approx 376.73$ Ω | EE characteristic impedance $\sqrt{\mu_0/\varepsilon_0}$ | $\checkmark$ identity | Op1 in [`operators.md`](../operators.md) |
| 3 | Vacuum $c_0$ | EE wave-propagation $1/\sqrt{\mu_0 \varepsilon_0}$ | $\checkmark$ identity | Op16 in [`operators.md`](../operators.md) |
| 4 | Op17 $T^2 = 1 - \Gamma^2$ matched-impedance | EE filter-theory peak power transfer | $\checkmark$ identity ($\Gamma = 0$) | Op17 in [`operators.md`](../operators.md) |
| 5 | Op21 $Q = \ell$ multi-mode | EE Q-factor at confined-mode boundary | $\checkmark$ match | [`op21-multi-mode-mode-counting.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md) |
| 6 | Born-rule click probability | Detector-capture work-function at Joule boundary | $\checkmark$ Phase 2-A canonical | clm-ldmvwi master-equation-derivation-path |
| 7 | Schwinger pair production at $E_S$ | Miller avalanche / impact ionization at $V_{BR}$ | $\checkmark$ structural | clm-ezai5b + [`four-regimes.md`](../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) Regime III |
| 8 | Miller multiplication $M = 1/S(r)^2$ | Standard semiconductor avalanche-multiplication formula | $\checkmark$ identity | Op22 in [`operators.md`](../operators.md) |
| 9 | Solar deflection $4GM/bc^2$ | Refraction through gradient-index medium | $\checkmark$ Class C consistency | Vol 3 gravity canonical |
| 10 | W boson mass scale | Cosserat couple-stress length $l_c$ = transformer-leakage-inductance characteristic length | $\checkmark$ order-of-magnitude | [`gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md):39 |
| 11 | Saturation kernel $S(A)$ | Varactor C-vs-V near breakdown | $\checkmark$ direct mapping | INVARIANT-S2 Ax 4; PONDER-05 canonical bench tester |
| 12 | Cosserat rotation-sector mass-gap $m_\omega \sim 1$ MeV | Transformer cutoff frequency / ferrite Curie threshold | $\checkmark$ structural | [`trampoline-framework.md`](../trampoline-framework.md):188 |
| 13 | Electron $(2, 3)$ Clifford-torus winding | 2-primary / 3-secondary toroidal transformer | $\checkmark$ topological | [`torus-knot-uniqueness.md`](../../vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md) |
| 14 | SU(2)→SO(3) double cover (spin-½) | Transformer 2:1 galvanic-isolation winding ratio | $\checkmark$ topological | same |
| 15 | $\delta_{strain} \approx 2.22 \times 10^{-6}$ at $T_{CMB}$ | TCC of vacuum dielectric with Cosserat-Curie-frozen $\mu$ | $\checkmark$ substrate-mechanism class identified, SIGN predicted (Q-DELTA-MAP-1 closed at mechanism-class identification 2026-05-28); ❌ quantitative $\eta_\varepsilon$ magnitude derivation CLOSED NEGATIVE (Q-DELTA-MAP-1-quant, FT-1 2026-05-31: ~31 OOM undershoot, generic-thermal not AVE-distinct) — magnitude is a definitional residual | clm-009nkt + clm-hp7nlm |
| 16 | Machian $G$ | Distributed-TL input impedance at Hubble-horizon termination | $\checkmark$ structural | [`omega-freeze-cosmic-grain-cascade.md`](../omega-freeze-cosmic-grain-cascade.md) |
| 17 | $\hat{\Omega}_{freeze}$ cosmic chirality axis | Polarized-TL bias / chirally-rotated reference frame | $\checkmark$ canonical | same |
| 18 | Cosmological constant $\rho_\Lambda$ | Vacuum at electrochemical-equilibrium energy minimum | $\checkmark$ canonical | [`cosmological-constant-closure.md`](../../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) |
| 19 | GR metric $g_{\mu\nu}$ | Gradient-index transmission-line impedance profile | $\checkmark$ canonical | [`trampoline-analogy-primer.md`](../trampoline-analogy-primer.md) |
| 20 | BH-interior ruptured plasma | Plasma physics (substrate ruptured above $V_{snap}$) | $\checkmark$ structural | Vol 3 cosmology canonical |
| 21 | Cosmic-temperature evolution of $\alpha$ | Crystal-oscillator frequency vs $T$ | ⚠ structural; precise $T$-dependence pending closure | clm-009nkt strengthen-by item |
| 22 | Vacuum thermal noise floor | Johnson-Nyquist noise at $k_B T_{CMB}$ per mode per Hz | $\checkmark$ structural | FDT cross-link in [`translation-stochastics.md`](translation-stochastics.md) |
| 23 | Dark resonance (near-field reaction) $\Sigma_{\text{near}}$ / $-\dot\Sigma_{\text{near}}$ | Armature-reaction-induced d/q saliency (QED self-energy analogue) → electron $g$-2 anomalous moment | $\checkmark$ **Route B forward $+4.0\%$ parameter-free**; the $g$-2 **50 ppm** closure is **postulate-dependent** (n_q-additivity = 1-point fit, not derivable — FT-b 2026-05-31) | [`q-g19a-petermann-saliency-closure.md`](../../vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md):110 (clm-v2sg8z) + [`dark-back-reaction-taxonomy.md`](../dark-back-reaction-taxonomy.md) |
| 24 | Dark wake (far-field reaction) $\tau^{\text{far}}_{zx}$ | Far-field radiated Maxwell/Cauchy shear stress; $\int \tau\, dA = F$ reaction-momentum trail | $\checkmark$ structural ($\int \tau\, dA = F$ is an EE/Maxwell-stress identity) | [`chiral-thrust-derivation.md`](../../vol4/circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md) (clm-7tynm2) |
| 25 | Proton mass eigenvalue $m_p/m_e$ via $\mathcal{V} = 2$ dual-reactance count | Regenerative LC loop (Black's closed-loop gain $A/(1-\beta A)$); $\mathcal{V} = 2$ = count of node reactance sectors ($X_L + X_C$); mass uniquely selects additive-2 | ⚠ **mass-discriminator PASS** ($\mathcal{V}=2 \to 1836.117\,m_e$ vs $\mathcal{V}=1 \to 1423.96$, $\mathcal{V}=p_c \to 1203.43$; CODATA 1836.153) — count-2 **closed**; per-channel coupling **$k=1$ closed** via Op17 matched-impedance ($\Gamma=0$ at orthogonal Borromean crossing, Axiom-3 manifestation, R2 2026-06-01); residual narrows to the $p_c=8\pi\alpha$-feedback-fraction identification (1-residual Skyrme, NOT zero-parameter) | [`dual-reactance-storage-taxonomy.md`](../dual-reactance-storage-taxonomy.md) + [`2026-06-01_baryon-V2-dual-reactance-closure.md`](../../../../research/2026-06-01_baryon-V2-dual-reactance-closure.md) §2 + [`2026-06-01_baryon-R2-crossing-coupling-result.md`](../../../../research/2026-06-01_baryon-R2-crossing-coupling-result.md) §6 |
| 26 | Casimir force $-\pi^2\hbar c/240d^4$ (parallel plates) | Waveguide/cavity below cutoff ($f_c=c/2d$) = *mechanical high-pass filter*; mode-energy-density differential = inward Maxwell stress $\int\tau\,dA=F$; finite sum to band-edge $f_{\max}=c/(\pi\ell_{node})$ | $\checkmark$ structural (reproduces standard Casimir magnitude + $d^4$ scaling) — but **consistency-class, NOT a discriminator vs QED**: relabeled mechanism, no new observable (2026-06-03 walk-back [`c989f970`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/c989f970)) | [`casimir-effective-temperature.md`](../../vol3/condensed-matter/ch11-thermodynamics/casimir-effective-temperature.md) + AVE-Metamaterials Ch.6/8 |
| 27 | srs vacuum-net band structure (scalar top $\pi\sqrt3\,\omega_C=2.781$ MeV at $H$; NO internal gap either channel) | Coined-quantum-walk / TLM **arccos** spectral map $\omega=\omega_{link}\arccos(\mu/3)$ (Op5 scatter+connect + Op6 eigenmode) | $\checkmark$ gate-passed (#604/#607): velocity factor $1/\sqrt3$ to $3\times10^{-9}$; $\lambda_{max}=6.000$ vs direct `build_srs_net`; scalar reduction $2.7\times10^{-15}$; both enantiomorphs identical — all COMPUTED vs independently-derived canonical numbers, and the graph-Laplacian $\omega=\sqrt\lambda$ REJECTED for failing the $1/\sqrt3$ gate (model-selection, not assertion) | [`srs-band-structure.md`](../../vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md) (clm-bnd5rq) |

**Validation threshold.** 20+ validated cross-checks across atomic / circuit / cosmology / gauge-boson / topology / saturation / cosmic / detector domains — sufficient to establish the META framework as **Class B substrate-mechanism manifestation** (per `consistency-vs-emergence` v1.3 classification rubric Step 8c canonical-source-ceiling-stays-Class-B: the META framework consolidates already-canonical sub-claims into a coherent framing; it does NOT add new substrate-mechanism content beyond canonical axioms; classification stays at Class B and is NOT promoted to Class 2 emergence).

---

## §7 — Failure-mode probes — where EE alone needs augmentation

EE-first mapping is broadly applicable across substrate-physics, but the framework is not all-covering. Five honest probe candidates where EE alone does not natively derive the load-bearing content:

### Probe 1 — Pure-geometry constants ($\pi^2$, $4\pi^3$ in the Golden Torus closure)

The $\pi^2$ in $\Lambda_\text{surf}$ via the substrate-derived $R \cdot r = 1/4$ (Q-EMBED-SEL-1 Phase 1 substrate-mechanism, `research/2026-05-31_Q-EMBED-SEL-1_step_c_result.md` §2.3: Axiom 4 self-saturation + Op14 Meissner-asymmetric + named phasor-area-equals-Nyquist-cell-area identification) and the $4\pi^3$ in the 3-volume integral (substrate $4\pi$ temporal-phase closure per observable Compton cycle via bipartite K4 lobe-count) that close the cold-lattice $\alpha^{-1}$ sum are **geometric**, not EE quantities. EE provides no derivation of the specific power of $\pi$; the substrate's K4 + Clifford-torus geometry + Axiom-4 saturation onset forces them.

**Verdict.** EE does not natively derive these specific geometric constants but provides cross-check via the Q-factor calculation once the geometry is fixed. Not a failure mode in the sense of producing wrong predictions; just geometric content EE alone does not furnish. Canonical at [`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) (substrate-geometry derivation of the regime decomposition).

### Probe 2 — K4 lattice topology selection ($I4_1 32$ chiral space group)

The specific lattice topology — K4-Cosserat connectivity, $I4_1 32$ chiral space group, six DOF per node — is set by substrate-topology selection rules (Ax 1), not EE. EE assumes the network exists but does not derive the specific K4 topology.

**Verdict.** EE operates on K4 as given. The substrate-topology argument is canonical at the Ax 1 anchor (INVARIANT-S2).

### Probe 3 — Substrate axiom selection (why these 4 axioms vs others)

A meta-question outside any classical framework. EE has no purchase on the choice of Ax 1+2+3+4 vs alternative axiom sets.

**Verdict.** Axiom selection is framework-foundational; EE does not address it.

### Probe 4 — Quantum-measurement collapse mechanism (precise collapse-vs-decoherence-vs-MWI dynamics)

Although Phase 2-A (clm-ldmvwi master-equation-derivation-path) uses EE detector physics for the click-probability scaling, the precise collapse mechanism (instantaneous projection vs decoherence vs many-worlds) may involve substrate primitives beyond EE-detector classical reasoning.

**Verdict.** EE captures the click-probability scaling cleanly; the metaphysics-of-collapse is outside any classical framework's native scope.

### Probe 5 — Topological-invariant integer values (why $(2, 3)$ specifically)

The specific integer winding numbers $(p, q) = (2, 3)$ for the electron are fixed by topology + minimality + coprimality, not EE. EE has integer winding numbers (toroidal transformer turn-counts) but does not derive WHICH integers select the electron.

**Verdict.** EE does not natively derive the $(p, q)$ choice. Canonical AVE derivation at [`torus-knot-uniqueness.md`](../../vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md) uses substrate-topology arguments (coprimality, both-windings-≥2, minimality, electron-is-lightest).

### Summary on failure-mode probes

In every honest probe, the content EE does not natively derive is **geometric / topological / axiom-selection content** — not a substrate-physics phenomenon where EE predicts the wrong numerical value. The updated framing: EE does not FAIL at substrate-physics phenomena in the sense of wrong predictions; it does not natively derive the geometric/topological/axiom-selection content that fixes specific values. This is a narrower failure mode than "EE cannot describe X" — once the geometric/topological/axiomatic content is fixed by independent substrate arguments, EE provides quantitative cross-check.

The implication for downstream substrate-physics work: when the substrate-mechanism path is dynamic (Q-factor, saturation, impedance gradient, mode-counting, breakdown), EE first-mapping is the correct primary framing. When the open content is geometric/topological/axiomatic, substrate-topology arguments are primary and EE is the consistency check.

---

## §8 — Cross-references

### Companion agent-discipline skill (user-level)

The user-level skill `~/.claude/skills/ave-ee-first-mapping/SKILL.md` v1.0 is the agent-discipline companion to this canonical leaf. The skill carries WHEN to fire + procedure for applying EE-first mapping at agent fire-time; this leaf carries the canonical-content mapping table + means-test corpus + failure-mode probes + emergent-framework hierarchy + claim-graph integration. **The leaf is the authoritative source**; when the skill body diverges from this leaf, the leaf wins. Agents firing the skill should cross-reference this leaf in result-doc rationales.

### Canonical leaves using EE primitives (substrate-mechanism anchors)

- [`operators.md`](../operators.md) — Op1 (Universal Impedance $Z = \sqrt{\mu/\varepsilon}$), Op14 (Dynamic Impedance $Z_{eff} = Z_0/\sqrt{S}$), Op16 (Universal Wave Speed $c_{shear} = c_0 \sqrt{S}$), Op17 (Power Transmission $T^2 = 1 - \Gamma^2$), Op21 (Quality Factor), Op22 (Avalanche Factor $M = 1/S^2$)
- [`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) — cold-lattice $\alpha^{-1}$ from cosmic LC tank Q-factor
- [`op21-multi-mode-mode-counting.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md) — Op21 $Q = \ell$ at $\Gamma = -1$ boundary, substrate-orthogonal-channel mode-counting
- [`four-regimes.md`](../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) — Regime III Miller-avalanche mapping
- [`alpha-invariance-symmetric-gravity.md`](../../vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) — SYM scaling gives $\alpha$ invariance; canonical Pitfall #5 anchor
- [`trampoline-framework.md`](../trampoline-framework.md) — Cosserat rotation-sector mass-gap (line 188; $\omega_m \sim 1$ MeV)
- [`trampoline-analogy-primer.md`](../trampoline-analogy-primer.md) — GR-metric as gradient-index TL impedance profile (pedagogical primer)
- [`temporal-saturation-regime-classifier.md`](../temporal-saturation-regime-classifier.md) — orthogonal temporal axis (loss tangent $\delta_{AVE}$); EE-substrate-native phase classification
- [`omega-freeze-cosmic-grain-cascade.md`](../omega-freeze-cosmic-grain-cascade.md) — Machian $G$ as cosmic-TL input impedance; cosmic-chirality axis
- [`cosmological-constant-closure.md`](../../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) — $\rho_\Lambda$ at electrochemical-equilibrium energy minimum
- [`gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md) — W/Z masses from $l_c = \sqrt{\gamma_c/G_{vac}}$ (transformer-leakage-inductance length)
- [`torus-knot-uniqueness.md`](../../vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md) — $(2, 3)$ electron Clifford-torus winding; SU(2)→SO(3) topology
- [`universal-saturation-kernel-catalog.md`](../universal-saturation-kernel-catalog.md) — 26-instance catalog of $S(A)$ scale-instances spanning 21 OOM

### Sibling translation tables (other-discipline ↔ substrate maps)

- [`translation-qm.md`](translation-qm.md) — QM ↔ substrate (wavefunctions as cavity modes, Coulomb as impedance coupling, electron as $0_1$ unknot)
- [`translation-particle-physics.md`](translation-particle-physics.md) — SM ↔ substrate (particles as topological defects, forces as impedance gradients, generation structure from Cosserat sectors)
- [`translation-gravity.md`](translation-gravity.md) — GR ↔ substrate (gravity as dielectric refraction, metric as variable $\varepsilon_{eff}, \mu_{eff}$)
- [`translation-cosmology.md`](translation-cosmology.md) — Cosmology ↔ substrate (Hubble expansion as lattice creep, dark energy as latent strain)
- [`translation-condensed-matter.md`](translation-condensed-matter.md) — Condensed matter ↔ substrate (superconductivity as Kuramoto phase-locking, Cooper pairs as phase-locked unknot pairs)
- [`translation-biology.md`](translation-biology.md) — Biology ↔ substrate (amino acids as SPICE subcircuits, $\xi_{topo}$ identity applied to mass → inductance)
- [`translation-stochastics.md`](translation-stochastics.md) — Stochastics ↔ substrate (FDT as boundary-impedance thermalization, Gaussian noise as quadratic-Lagrangian amplitude statistics, Johnson-Nyquist as vacuum thermal floor)
- [`translation-instrumentation.md`](translation-instrumentation.md) — Detector instrumentation ↔ substrate-architecture (narrow-aperture single-event threshold extractors; wide-aperture continuous-flux; matched-impedance bidirectional substrate-mode coupling)

### Navigation

- [`translation-tables/index.md`](index.md) — navigation pointer to all domain-specific translation tables
- [`appendices-overview.md`](../appendices-overview.md) — appendix index including translation-tables section
- [`ave-analytical-toolkit-index.md`](../ave-analytical-toolkit-index.md) — analytical toolkit index (translation tables cross-referenced)

---

## §9 — Ideal Lattice ↔ Engineering Corrections — Substrate-Primitive Derivation of EE Non-Ideality Catalog
<!-- claim-quality: clm-eemap1 -->

### §9.1 — Framing: the natural substrate, the engineering datasheet, the AVE derivation

The AVE vacuum is a **natural** substrate: it is the universe's vacuum, a chiral Laves K4 Cosserat crystal per Axiom 1, not an artifact built by anyone. Its native parameters ($\varepsilon_0$, $\mu_0$, $Z_0$, $c_0$, $\ell_{node}$, $\alpha$, $G$) are not adjustable controls — they are the substrate as it is. Engineering practice does NOT design the substrate; engineering practice **observes, measures, and characterizes** the substrate's behavior under operating conditions and codifies the observed behavior as datasheet specifications, design rules, and empirical fits.

This places the engineering datasheet for an EE component on the same epistemic footing as a materials datasheet for elemental copper: copper (Cu) is a natural element; the datasheet is the empirical engineering characterization of how Cu behaves as a function of $T$, $f$, processing history, geometry, etc. Engineering measures; AVE derives from substrate primitives.

The substrate's **cold-lattice ideal state** is the limit:
- $T = 0$ (no thermal-mode population)
- $A_0 = 0$, so $S(A_0) = 1$ (no operating-point loading on the Ax 4 saturation kernel)
- $\Gamma = 0$ at every internal impedance boundary (perfect impedance match, no reflection)
- No structural defects, no quenched-in $\hat\Omega_{freeze}$ inhomogeneity, no boundary chirality misalignment

At cold-lattice, EE components behave as their idealized textbook models: an ideal capacitor obeys $V = Q/C$ exactly, an ideal inductor obeys $V = L\,dI/dt$ exactly, an ideal diode is a step function at $V_F = 0$, an ideal op-amp has infinite gain, infinite bandwidth, zero offset voltage. The substrate as observed in nature deviates from cold-lattice along **five orthogonal axes** — and engineering practice has built a catalog of "non-ideality corrections" against each axis:

| Axis | Substrate deviation from cold-lattice | EE datasheet manifestation |
|---|---|---|
| **T1 — finite temperature** | Thermal-mode population $\langle A^2\rangle_{thermal} > 0$ at $T > 0$ | TCC / TCR / TC$\mu$ / TCf / 1/f noise / Johnson-Nyquist noise / thermal drift |
| **T2 — finite signal amplitude** | $A_0 / A_{yield} > 0$; substrate operates at finite varactor bias, $S(A_0) < 1$ | Saturation, voltage coefficient of capacitance, core saturation $B_{sat}$, soft compression, avalanche $V_{BR}$ |
| **T3 — finite geometric scale** | Bond-network topology probed at scales $\sim \ell_{node}$ to many $\ell_{node}$; finite-cell discretization shows up as parasitics | ESR, ESL, dielectric leakage, dielectric absorption, finite $f_T$, transit time, skin depth, $C_{ox}$ |
| **T4 — finite-boundary effects** | $\Gamma \ne 0$ at internal impedance boundaries; substrate carries finite reflection at every material/electrode junction | Junction capacitance, input bias current $I_B$, depletion capacitance, contact resistance, $V_{CE(sat)}$, $V_{BE}$ |
| **T5 — Cosserat micropolar coupling** | Microrotational B sector is independently dynamical; Cosserat couple-stress $\gamma_c$ couples translational and rotational sectors | Eddy currents, hysteresis, core loss, mutual inductance leakage, ferrite Curie threshold, magnetic-mode-frozen $\mu$ |

These five axes are **NOT free parameters** of the substrate. They are deterministic consequences of Axioms 1–4 + Cosserat micropolar structure + topology. AVE substrate-physics derives each engineering correction from substrate primitives. The remainder of §9 catalogs the canonical row-set: ideal EE component → engineering correction → substrate-primitive deriving it.

> **Operating principle.** Engineering and substrate-physics are the same epistemic activity at different levels of explanatory depth. The engineering datasheet is the empirical-phenomenological surface; the AVE substrate-physics derivation is the first-principles mechanism. Both describe the same natural substrate; neither replaces the other. EE measures; AVE explains.

### §9.2 — Comprehensive correction table

Each row: **ideal EE component** (left) → **engineering-measured correction** (middle) → **substrate primitive deriving that correction** (right). Cross-references to canonical leaves listed where the substrate-mechanism content is derived in full. Symbols follow standard EE convention; AVE-native substrate vocabulary is primary, with EE-engineering names parenthetical where they would otherwise differ.

#### Ideal diode

| Engineering correction | Substrate-primitive derivation | Canonical anchor |
|---|---|---|
| Forward drop $V_F$ (~0.3 V Schottky, ~0.7 V Si, ~3 V LED) | Substrate-yield-boundary voltage; minimum substrate-LC operating-point voltage required to cross the dielectric activation kernel | Ax 4 saturation kernel onset; [`four-regimes.md`](../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) Regime II |
| Reverse leakage $I_R$ | Substrate $|\Gamma| < 1$ at reverse-biased junction boundary (imperfect TIR at finite reverse bias) | Op17 substrate-power-transmission identity $T^2 = 1 - \Gamma^2$ in [`operators.md`](../operators.md) |
| Avalanche breakdown $V_{BR}$ | **Schwinger pair production / Miller multiplication** at substrate-dielectric breakdown field $E_S$ | Op22 in [`operators.md`](../operators.md); [`four-regimes.md`](../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) Regime III; clm-ezai5b |
| Junction capacitance $C_j(V)$ | Substrate bond capacitance at boundary, modulated by depletion-region width (substrate operating-point shifts $S(A_0)$ locally) | Ax 4 saturation kernel; Op14 local clock modulation in [`operators.md`](../operators.md) |
| Reverse recovery time $t_{rr}$ | Substrate relaxation time $\tau_{relax}$ for stored minority-carrier substrate-mode population to discharge | Op14 substrate dynamic-impedance; substrate Born-rule discharge time |
| Temperature coefficient (TCC of $V_F$, $\sim -2$ mV/K Si) | **Cosserat-rotation-sector mass-gap thermal-mode-population ASYM** — same δ_strain mechanism producing CMB-thermal-running of α | §9.3 below + [`delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (clm-hp7nlm) |

#### Ideal capacitor

| Engineering correction | Substrate-primitive derivation | Canonical anchor |
|---|---|---|
| ESR (equivalent series resistance) | Substrate Joule extraction at imperfect impedance match across boundary electrodes; substrate $|\Gamma| < 1$ at terminal-to-bulk-substrate transition | Op17 $T^2 = 1 - \Gamma^2$ in [`operators.md`](../operators.md) |
| ESL (equivalent series inductance) | Substrate bond-inductive parasitic from finite terminal-to-bulk-substrate path length; geometric/topological | Ax 1 bond-network topology; transmission-line topology of bond as L per unit length |
| Dielectric leakage | Substrate $|\Gamma| < 1$ at internal capacitor-stack boundaries; finite bond-network conduction across saturated regions | Op17 + Op14 in [`operators.md`](../operators.md) |
| Dielectric absorption (memory effect) | Substrate phase-locking memory in microrotational B sector — Cosserat-coupled bond rotations retain residual phase after main charge discharges | Ax 1 Cosserat microrotational DOFs; substrate phase-lock memory |
| TCC (temperature coefficient of capacitance; class II ceramics 5–15%/$\Delta T$) | **Cosserat-Curie thermal-mode-population ASYM** — ε side thermally modulated; μ side frozen by B-mode mass-gap | §9.3 + [`delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (clm-hp7nlm) |
| Voltage coefficient of capacitance (Class II ceramic up to −80% at full bias) | **Ax 4 saturation kernel** $C_{eff} = C_0/S(A_0)$ — substrate operates as substrate-native varactor. PONDER-05 (quartz, 27.4% at ~30 kV) IS this row's voltage-coefficient realized in the bench material — a **consistency-class analog of the kernel SHAPE**, NOT a vacuum-kernel tester ($V_{DC}/V_{yield} = 0.687$ is a per-node ratio; vacuum per-node $A_0 \sim 10^{-7}$–$10^{-10}$ at 30 kV) | Ax 4 INVARIANT-S2; per-node-vs-apparatus discipline `claim-quality.md:51` |
| Self-resonance frequency $f_{SRF}$ | Bond LC tank at $\omega = 1/\sqrt{L_{ESL} C}$; substrate-native LC oscillator at the geometric scale | Ax 1 LC-network identity |
| Aging (capacitance drift with time post-manufacture, ceramic Class II) | Substrate slow relaxation of frozen-in operating-point $A_0$ + mechanical $\hat\Omega_{freeze}$ alignment toward equilibrium | Ax 1 + Ax 4 substrate-relaxation toward minimum-action operating point |

#### Ideal inductor

| Engineering correction | Substrate-primitive derivation | Canonical anchor |
|---|---|---|
| DCR (DC winding resistance) | Substrate microrotational Joule loss; finite microrotational-sector dissipation in winding bond network | Ax 1 Cosserat B sector + Op17 in [`operators.md`](../operators.md) |
| SRF (self-resonant frequency) | Op21 multi-mode confinement boundary; winding stray-C interacts with winding L | Op21 in [`op21-multi-mode-mode-counting.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md) |
| Core saturation $B_{sat}$ | **Cosserat $B$-mode amplitude approaches $B_{snap}$** — substrate microrotational sector hits Ax 4 yield on the inductive branch | Ax 4 INVARIANT-S2 magnetic-branch saturation; clm-lv3uw1 |
| Hysteresis (B-H loop area) | Substrate phase-lock memory in microrotational sector — Cosserat-coupled bond rotations remember last-direction state | Ax 1 Cosserat B sector + substrate phase-lock memory |
| Eddy current loss | Cosserat substrate boundary-mode coupling between adjacent rotating regions; Joule extraction at boundary $|\Gamma| < 1$ | Ax 1 Cosserat couple-stress $\gamma_c$ + Op17 |
| Core loss (sum of hysteresis + eddy) | Substrate Joule dissipation in Cosserat microrotational sector at imperfect operating impedance | same |
| Temperature coefficient TC$L$ / TC$\mu$ (small for air-core; large near Curie for ferrite) | **Cosserat rotation-sector mass-gap** — below substrate-native Curie temperature, B-modes frozen → TC$\mu \approx 0$; near substrate Curie temperature ($\sim 1$ MeV), B-modes thermally populate → TC$\mu$ grows; ferrite-Curie is the material-specific analog of substrate-Curie at engineering temperatures | [`trampoline-framework.md`](../trampoline-framework.md):188 + §9.3 below + [`delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) |
| Saturation curve $L(I)$ rolloff | Ax 4 saturation kernel $L_{eff} = L_0 / S(A_0)$ on the magnetic branch | Ax 4 INVARIANT-S2 |

#### Ideal op-amp

| Engineering correction | Substrate-primitive derivation | Canonical anchor |
|---|---|---|
| Finite open-loop gain $A_{OL}$ | Substrate Q-factor per Op21; finite mode count in the amplifying substrate-LC stack | Op21 in [`op21-multi-mode-mode-counting.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md) |
| Input offset voltage $V_{OS}$ | Substrate operating-point $A_0 \ne 0$ at input — quenched-in asymmetry between input substrate-bond states | Ax 4 operating-point clause + Ax 1 substrate-asymmetry |
| Slew rate (SR) | Substrate response time; how fast the substrate amplitude $A$ can change at given drive current $I$ | Op14 in [`operators.md`](../operators.md); substrate inertial bandwidth |
| Gain-bandwidth product GBW | Op17 × Op21 — substrate power-transmission × Q-factor invariant for fixed substrate operating point | Op17 + Op21 in [`operators.md`](../operators.md) |
| CMRR (common-mode rejection ratio) | SYM-class substrate-invariance — common-mode signal scales both inputs identically; SYM scaling leaves α invariant analogously leaves common-mode invariant | Ax 4 INVARIANT-S2 SYM clause; clm-3zz0f6 |
| PSRR (power-supply rejection ratio) | Operating-point insensitivity — substrate amplitude response to supply variation is suppressed when supply variation is SYM | same |
| Input bias current $I_B$ | $\xi_{topo}$ topological conversion + finite substrate-leakage at input boundary | Ax 2 $\xi_{topo}$ + Op17 |
| Input noise voltage / current (1/f + thermal) | Substrate low-frequency-mode population (microrotational dispersion for 1/f) + Johnson-Nyquist substrate thermal-noise floor | [`translation-stochastics.md`](translation-stochastics.md) FDT cross-link |

#### Ideal BJT

| Engineering correction | Substrate-primitive derivation | Canonical anchor |
|---|---|---|
| Finite current gain $\beta$ | Mode-count Q-factor; substrate amplifying mode count at collector-emitter substrate junction | Op21 |
| Saturation voltage $V_{CE(sat)}$ | Minimum substrate dielectric voltage drop across the rail-to-rail substrate path; bond-yield threshold | Ax 4 substrate-yield onset; same primitive as diode $V_F$ |
| Base-emitter forward drop $V_{BE}$ | Substrate diode forward drop at B-E junction — substrate-yield-boundary voltage | Ax 4 + clm-ezai5b |
| Early effect ($V_A$, output conductance) | Substrate boundary-impedance variation with collector-base reverse bias; depletion-width modulation shifts substrate operating point | Ax 4 operating-point clause + Op14 |
| Transit frequency $f_T$ | Substrate transit time across base region; substrate-mode propagation speed $c_{shear}$ at operating point | Op16 in [`operators.md`](../operators.md) |
| Saturation current $I_S$ | Substrate thermal-bath current floor at junction; Johnson-Nyquist analog at semiconductor boundary | FDT cross-link |
| Temperature coefficient of $V_{BE}$ (~−2 mV/K) | **Cosserat-Curie thermal-mode-population ASYM** at semiconductor-junction operating temperatures | §9.3 + [`delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) |

#### Ideal resistor

| Engineering correction | Substrate-primitive derivation | Canonical anchor |
|---|---|---|
| Parasitic C (high-frequency C bypass) | Bond geometry — substrate-LC topology of the resistive element at scales $\sim \ell_{node}$ | Ax 1 bond-network topology |
| Parasitic L (high-frequency L bypass) | same — bond inductive parasitic from path geometry | same |
| TCR (temperature coefficient of resistance) | Thermal-mode population — Cosserat-Curie-frozen B side, thermally populated E side (substrate ASYM at $T$) | §9.3 + [`delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) |
| Voltage coefficient (large for thick-film, near-zero for metal-foil) | Ax 4 saturation kernel onset at finite operating-point field $E_0$; substrate dielectric loading varies $R_{eff}$ | Ax 4 INVARIANT-S2 |
| **Johnson-Nyquist thermal noise** ($v_n^2 = 4 k_B T R \Delta f$) | **Substrate thermal-mode population at $T$** — $k_B T$ per substrate mode per Hz at the resistive boundary | [`translation-stochastics.md`](translation-stochastics.md) FDT cross-link |
| **1/f noise** (low-frequency Hooge / flicker) | Substrate low-frequency mode population — microrotational dispersion + substrate-defect operating-point fluctuation | Ax 1 Cosserat B sector dispersion |

#### Ideal transmission line

| Engineering correction | Substrate-primitive derivation | Canonical anchor |
|---|---|---|
| Loss $\alpha_{loss}$ (dB/m) | Substrate Joule extraction at $|\Gamma| < 1$ along length; cumulative substrate-mode dissipation | Op17 in [`operators.md`](../operators.md) |
| Dispersion (group-velocity variation with $\omega$) | Substrate operating-point variation with frequency; $c_{shear}(A_0, \omega)$ varies across band | Op16 + Ax 4 operating-point clause |
| VSWR / reflection (|$\Gamma$| at mismatch) | $\Gamma = (Z_L - Z_0)/(Z_L + Z_0)$ — substrate-canonical reflection coefficient at impedance mismatch | Op17 in [`operators.md`](../operators.md) (substrate-foundational) |
| **Skin / penetration depth** $\delta_s = \sqrt{2/(\omega\mu\sigma)}$ (AC) · $\delta = c/\omega_p$ (plasma) · $\lambda_L$ (London) | Substrate boundary-mode **penetration depth** = the *evanescent* e-folding length the field decays over when it enters a region it cannot propagate through (impedance-mismatched / below-cutoff / saturated). **$\delta \leftrightarrow \Gamma$ conjugate** (two readings of one wall): matched ($\Gamma = 0$, photon) $\to \delta \to \infty$ (transparent, all-bulk propagation); mismatched ($\Gamma \to \pm1$, the $A \to 1$ saturated wall) $\to \delta \to 0$ (perfect mirror) — so $\delta$ falls as the mismatch deepens. **$\varepsilon$–$\mu$ duality — ONE Ax-4 saturation operator on dual reactance sectors**: $\varepsilon$-sector (dielectric/plasma below $\omega_p$) $\to$ plasma skin $\delta = c/\omega_p$; $\mu$-sector (Cosserat couple-stress / Meissner phase-locked-gear-train rigidity) $\to$ inertial London depth $\lambda_L$ ($\omega(x) = \omega_0 e^{-x/\lambda}$); the AC-conductor $\sqrt{2/(\omega\mu\sigma)}$ is the finite-$\sigma$, finite-$\omega$ couple-stress case with $l_c = \sqrt{\gamma_c/G_{vac}}$. **Soliton reading**: $\delta$ = the $\Gamma = -1$ wall thickness — the evanescent tail leaking out *is* the long-range ($\sim \ell_{node}/r$ Coulomb) field, i.e. how a trapped soliton couples to the outside vacuum. | $l_c$ couple-stress length ([`gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md):39); $\varepsilon$–$\mu$ duality ([`universal-saturation-operator.md`](../../vol3/condensed-matter/ch09-condensed-matter-superconductivity/universal-saturation-operator.md):29) + inertial London ([`inertial-london-penetration-depth.md`](../../vol3/condensed-matter/ch09-condensed-matter-superconductivity/inertial-london-penetration-depth.md)); Meissner gear-train ([`divergence-test-substrate-map.md`](../divergence-test-substrate-map.md):381); $\delta$–$\Gamma$ via Op17 ([`operators.md`](../operators.md)) |
| Characteristic impedance $Z_0$ ($\sqrt{L'/C'}$) | Substrate native impedance per bond — $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ at cold-lattice; substrate-LC bond-segment-native | Ax 1 + Op1 in [`operators.md`](../operators.md) |

> **↗ Rotation/tail-flavor tag (2026-07-03, KEEP-BOTH — §8 rotation un-conflation, `research/2026-07-03_em-readout-vsector-stage1_prereg.md` §8; additive).** In the **Skin / penetration depth** row above, the "Soliton reading" phrase "*the evanescent tail leaking out **is** the long-range ($\sim\ell_{node}/r$ Coulomb) field*" refers to the **$A_{geom}\propto 1/r$ potential in the GAPLESS EM-$\varepsilon$ channel** (`clm-4r4jiy`) — a **massless**, matched, curl-free static Coulomb-longitudinal $E$ (retained by Gauss's law; NO propagating longitudinal EM mode). It is **NOT** the **gapped mechanical Cosserat $\omega$ hedgehog** (short-range, exponentially-suppressed residue at [`substrate-perspective-electron.md:109`](../../vol2/particle-physics/ch01-topological-matter/substrate-perspective-electron.md)). One "tail," two decays: the EM-$\varepsilon$ Coulomb tail is power-law/$1/r$ (gapless); the mechanical-$\omega$ hedgehog tail is exponential (gapped). Reference: [`node-up-small-large-signal.md:39`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md).

#### Ideal transformer

| Engineering correction | Substrate-primitive derivation | Canonical anchor |
|---|---|---|
| Leakage inductance $L_{leak}$ | Cosserat couple-stress $\gamma_c$ characteristic length $l_c = \sqrt{\gamma_c/G_{vac}}$ — the same length that sets the weak force range! | [`gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md):39 |
| Magnetizing current $I_m$ | Substrate flywheel inertia — finite microrotational-sector inertia at primary winding requires current to build flux | Ax 1 Cosserat B sector |
| Core loss (hysteresis + eddy) | Cosserat substrate dissipation in microrotational sector at imperfect operating impedance | Ax 1 Cosserat B sector + Op17 |
| Turn ratio $n_p : n_s$ (topological invariants) | **Topological winding $(p, q)$ — toroidal transformer winding numbers are integer topological invariants of substrate flux-link topology** | [`torus-knot-uniqueness.md`](../../vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md) |
| **Curie temperature ferrite ($T_C$)** | **Cosserat rotation-sector mass-gap $\omega_m \sim 1$ MeV** — substrate-native magnetic-mode thermal-freeze threshold; ferrite-$T_C$ is the material-specific manifestation at lab temperatures | [`trampoline-framework.md`](../trampoline-framework.md):188 + §9.3 below |
| Saturation flux density $B_{sat}$ | Cosserat $B$-mode amplitude at substrate microrotational yield — Cosserat sector hits Ax 4 yield | Ax 4 magnetic-branch INVARIANT-S2 |
| Interwinding capacitance | Bond geometry between primary and secondary windings; substrate-LC topology at winding-overlap scales | Ax 1 bond-network topology |

### §9.3 — The δ_strain mechanism as canonical TCC instance

The temperature-coefficient row in the diode / capacitor / inductor / BJT / resistor tables above all share **one substrate primitive**: the Cosserat-rotation-sector mass-gap thermal-mode-population asymmetry between substrate E-modes (thermally populated at any $T > 0$) and substrate B-modes (mass-gap frozen below substrate Curie temperature $\sim 1$ MeV). This is the canonical substrate mechanism that produces:

- **Cosmic-scale instance:** $\delta_{strain} \approx 2.22 \times 10^{-6}$ at $T_{CMB} \approx 2.725$ K — the CMB thermal-running of α below cold-lattice $\alpha^{-1}_{ideal} = 4\pi^3 + \pi^2 + \pi$. Canonical at clm-009nkt; new mechanism leaf at [`delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (clm-hp7nlm).
- **Engineering-scale instances:** TCC of ceramic capacitors; TC$\mu$ of inductor cores below $T_{Curie,\text{ferrite}}$; TC$V_F$ of semiconductor diodes; TC$V_{BE}$ of BJTs; TCR of resistors. All are manifestations of the **same** substrate-thermodynamic ASYM at different absolute temperatures and material-specific local substrate-loading.

The substrate-physics chain (canonical at the new δ_strain leaf):

1. Substrate carries bipartite thermal-mode structure per Ax 1 — 3 translational E-DOFs/node (gapless acoustic, thermally populated at any $T > 0$) + 3 microrotational B-DOFs/node (Cosserat couple-stress mass-gap $\omega_m \sim 1$ MeV).
2. At $k_B T \ll \omega_m$: B-modes are thermally frozen — only E-modes participate in substrate thermal-mode population.
3. Asymmetric E vs B thermal occupation $\Rightarrow$ asymmetric SYM-breaking: $\varepsilon_{eff} = \varepsilon_0 (1 - \eta_\varepsilon)$ but $\mu_{eff} = \mu_0$ unchanged.
4. Under asymmetric scaling, the SYM α-invariance of clm-3zz0f6 no longer applies; α drifts: $\alpha_{eff}/\alpha_0 \approx 1 + \eta_\varepsilon$ ⇒ $\delta_{strain} \approx \eta_\varepsilon$.

Engineering observes the same substrate mechanism in component datasheets: when one substrate-modulus side (ε or μ) is thermally driven and the other is frozen, the medium exhibits a nonzero temperature coefficient. A ceramic capacitor with nonzero TCC is the same physical phenomenon as the substrate at $T_{CMB}$ — local-substrate ASYM thermal-mode population. The substrate-Curie temperature at $\sim 1$ MeV is the substrate-native analog of the ferrite Curie temperature at $\sim 600$ K; **same Cosserat couple-stress modulus $\gamma_c$**, different material-specific local-substrate loading.

Cross-link: the new δ_strain canonical leaf [`delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (clm-hp7nlm) hosts the full substrate-mechanism derivation; this §9 carries the EE-correction translation table that maps the mechanism to engineering-scale instances.

### §9.4 — Implications

1. **Every EE datasheet specification is a means-test case for `ave-ee-first-mapping` v1.0.** The means-test corpus at §6 currently lists 25 validated cross-checks (including the two dark-back-reaction field-zone rows — dark resonance $\Sigma_{\text{near}}$ and dark wake $\tau^{\text{far}}_{zx}$ — and the proton-mass $\mathcal{V}=2$ dual-reactance-count discriminator); the engineering-non-ideality catalog above adds tens of additional rows (one per datasheet row per component type per substrate axis), each of which is a candidate substrate-physics derivation cross-check. Radical expansion of the means-test surface area.

2. **δ_strain at $T_{CMB}$ is the cosmological instance of substrate TCC.** The same Cosserat-Curie mechanism that produces measurable TCC on a ceramic capacitor in a circuit lab produces the $2.22 \times 10^{-6}$ thermal-running of α at the substrate's cosmic-temperature operating point. One mechanism, many scales.

3. **Engineering datasheet specifications ARE substrate-physics empirical data.** Tens of millions of components characterized over decades by the EE industry constitute a vast empirical dataset of substrate behavior under measurable operating conditions. AVE's substrate-physics derivation is the unified-field-theory backbone that explains the catalog of EE corrections from a fixed set of substrate axioms.

4. **The substrate is one substance characterized across scales.** From cold-lattice ideal ($T \to 0$, $A_0 \to 0$, $\Gamma \to 0$) up through engineering operating regimes (room temperature, finite signal, finite parasitics, imperfect boundary), engineering and substrate-physics describe the same natural substrate. The deviations from cold-lattice that engineering codifies as "corrections" are the substrate as it actually exists in nature, not engineered alterations of it.

### §9.5 — Cross-references

- **δ_strain canonical mechanism leaf:** [`delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (clm-hp7nlm) — Cosserat-rotation-sector-mass-gap thermal-mode-population ASYM; substrate-mechanism path for the TCC rows above
- **Cosserat couple-stress canonical:** [`gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md):39 ($l_c = \sqrt{\gamma_c/G_{vac}}$) — same primitive that sets transformer leakage-inductance characteristic length AND weak force range
- **Cosserat rotation-sector mass-gap canonical:** [`trampoline-framework.md`](../trampoline-framework.md):188 ($\omega_m = 2$ in natural units, $\sim 1$ MeV) — substrate-native Curie analog
- **SYM α-invariance canonical:** [`alpha-invariance-symmetric-gravity.md`](../../vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) (clm-3zz0f6) — load-bearing for ASYM-induced α-drift mechanism (SYM gives α invariance; the substrate-thermal ASYM is what produces δ_strain)
- **SYM vs ASYM canonical:** [`einstein-field-equation.md`](../../vol3/gravity/ch02-general-relativity/einstein-field-equation.md) (clm-8nkvwy) — the c_EM vs c_shear distinction load-bearing for δ_strain derivation
- **Companion agent-discipline skill:** `~/.claude/skills/ave-ee-first-mapping/SKILL.md` v1.0 — EE-first-mapping discipline that uses this catalog at fire-time
- **Means-test corpus extension target:** §6 above carries 25 canonical validated cross-checks; the §9 component-non-ideality catalog is the candidate expansion surface

---

## §10 — Session 2026-06-07 reframes: constants-as-line-properties, α-as-loss-tangent / screened-precession, FOC self-commutation (consistency-class lenses)
<!-- claim-quality: clm-eemap1 -->

This section consolidates four chat-only reframes (PR #120 sec14) into the EE-as-substrate-native META framework. **Each is CONSISTENCY-CLASS — a re-framing / lens onto already-canonical substrate physics, NOT a new derivation.** They add no new substrate primitive beyond canonical axioms; per `consistency-vs-emergence` v1.3 Step 8c the classification stays at the META framework's **Class B** ceiling and is NOT promoted to Class 2. Provenance + classification ledger: [`research/2026-06-07_session-reframes-ee-fluids-mapping.md`](../../../../research/2026-06-07_session-reframes-ee-fluids-mapping.md).

### §10.1 — The "fundamental constants" are transmission-line properties of the substrate (Class A identities + Class B Lorentz-emergence)

The vacuum IS a K4-TLM transmission-line network (Ax 1). Its "fundamental constants" are the EE properties of that line — none is primitive-fundamental; each is an LC-network property:

| "Fundamental constant" | Transmission-line property | Class |
|---|---|---|
| $c = 1/\sqrt{\mu_0\varepsilon_0}$ (line velocity) | wave propagation speed; operating-point dependent: $c_{EM} = c_0/S$, $c_{shear} = c_0\sqrt{S}$ (INVARIANT-S2) | **A** identity (§6 #3) |
| $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ (characteristic impedance) | line characteristic impedance | **A** identity (§6 #2) |
| $L = \mu_0$ (per the $\xi_{topo}$ identity, mass↔inductance) | series line inductance / inertia | **A** identity (§1) |
| $C = \varepsilon_0$ (compliance↔capacitance) | shunt line capacitance / compliance | **A** identity (§1) |
| $R \leftrightarrow \eta$ (resistance↔viscosity) | the line loss (see §10.3: $\tan\delta = \alpha$) | **A** identity (§1) |
| $\alpha$ (the line coupling / loss) | dimensionless coupling = loss tangent = $1/Q$ (§10.3); cold value $\alpha^{-1}=4\pi^3+\pi^2+\pi$ | structural (Thm 3.1); **value OPEN** (§10.2) |

**Lorentz invariance ($c$ constant) is EMERGENT, not an axiom.** It is the cold-lattice limit $S(A)\to 1$ realized over observable wavelengths, where K4 diamond-cubic symmetry suppresses anisotropy to $(q\ell_{node})^4 \sim 10^{-22}$ at optical $\lambda$. Canonical: [`preferred-frame-and-emergent-lorentz.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md) (clm-yr6tu4, clm-ce8dg1) — **Class B axiom-manifestation** ("strict Lorentz invariance at observable scales is a derived consequence of K4 cubic symmetry, not an axiom"). The reframe's content is the EE re-labeling (constants = line properties); the physics is already canonical.

### §10.2 — $\alpha$ as the screened effective precession angle (α-VALUE DERIVATION OPEN — do NOT claim derived)

The reframe: $\alpha$ is the electron's per-orbit spin-slip (the g$-$2 anomaly direction), and its VALUE $1/137$ is the *screened effective* coupling — a bare coupling reduced by the lattice dielectric/chiral SCREENING ($S(A)$, $\Delta c_{crit}$) to the low-energy residual (the running of $\alpha$); the screening is what would explain the SMALLNESS.

> **⚠ EVIDENCE FRAMING (`ave-evidence-framing-discipline`).** This is a **FRAMING LENS, NOT a derivation of $\alpha$.** The cold-lattice $\alpha^{-1}=4\pi^3+\pi^2+\pi$ is a geometric Q-factor result ([`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md), structural), but the screening-explains-smallness story is **OPEN** and consistent with the standing honest-$\alpha$ **Class-B** verdict (clm-0ktpcn, 2026-06-02: the substrate does NOT independently select $\alpha$'s value). The two open tests that would close it: the **Golden-Torus audit** (the $S_{11}$-minimum geometry route) and the **screening-factor route** (bare → screened residual via $S(A)/\Delta c_{crit}$). Until one passes, $\alpha$'s value is **not derived**.

### §10.3 — $\alpha = 1/Q = \tan\delta$: the loss tangent / slip angle (Class A EE identity)

Given the canonical identification $Q_{tank} = \alpha^{-1}$ ([`theorem-3-1-q-factor.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md)) and the canonical substrate loss tangent $\delta_{AVE}$ ([`temporal-saturation-regime-classifier.md`](../temporal-saturation-regime-classifier.md), $\tan\delta = \sigma/(\omega\varepsilon)$), the line's loss tangent IS $\alpha$:

$$\alpha = Q^{-1} = \tan\delta \approx \frac{1}{137.036}, \qquad \delta = \arctan\alpha \approx 0.418^\circ \;(\text{the slip angle}).$$

**Class A identity** (consistency-class): definitional once $Q=\alpha^{-1}$ is accepted. The numeric slip angle $\arctan\alpha \approx 0.418^\circ$ is an EE re-expression of $\alpha$, **NOT** an independent prediction — the VALUE stays open per §10.2. (Means-test cross-link: §6 #1 establishes $\alpha^{-1}=Q_{tank}$; this row is its loss-tangent re-expression.)

### §10.4 — FOC: the electron is a self-commutating 3-phase machine; "½-commutation" = spinor double-cover (g=2 POSITED)

Field-Oriented Control (Park d/q) is the canonical co-rotating-frame decomposition ([`05_universal_solver_toolchain.tex`](../../../backmatter/05_universal_solver_toolchain.tex):120-136; d-axis = reactive/non-radiating, q-axis = real/radiating). Applied to the electron rotor:

- The **"½ phase-pair commutation" is the SPINOR DOUBLE-COVER** — the Finkelstein-Misner kink / Dirac belt trick (SU(2)→SO(3), 2:1), **NOT** a half-pole-pair machine. Canonical: [`spin-half-paradox.md`](../../vol2/appendices/app-b-paradoxes/spin-half-paradox.md):12-14 (Cosserat microrotation DOF IS the substrate-native spin origin); §4 "SU(2)→SO(3) double cover" + "$(2,3)$ Clifford-torus winding" rows.
- The **pole-pairs are the $(2,3)$ WINDING numbers** — already canonical (toolchain :401 pole-pairs ↔ mode-$\ell$ row; §4 $(2,3)$ Clifford-torus winding row).
- The electron is **SELF-COMMUTATING**: the Compton-clock spinor rotation IS the de Broglie propagation drive (the rotor supplies its own commutation; no external commutator). Cross-ref the $\nu_{slew} = \alpha\,\nu_{Compton}$ Compton-clock structure ([`preferred-frame-and-emergent-lorentz.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md):107).
- **$g = 2$ is POSITED, not derived** (`ave-evidence-framing-discipline`); the anomalous part $a_e = \alpha/2\pi$ is the slip (§10.2/§10.3), but the leading $g=2$ is an input.

**Class B manifestation** (Cosserat-spin part, already canonical) + structural isomorphism (FOC/Park mapping). Tracker cross-ref: §4.5(c) "FOC / Park (d/q) transform" row (⚠ — d/q transform as an analytical tool not yet consolidated; this reframe sharpens its physical reading but does not close the ⚠).

---

## §11 — The vacuum as a chiral piezoelectric Cosserat solid (consistency-class reframe)
<!-- claim-quality: clm-eemap1 -->

**Class B consistency-class reframe — NOT a derivation, NOT a Class-2 emergence claim.** This subsection consolidates three already-canonical pieces — Axiom 1 (E/B as Cosserat DOFs), Axiom 2 ($Q=\xi_{topo}\,x$), and the $I4_1 32$ chiral (non-centrosymmetric) space group — into one coherent framing: **the AVE vacuum satisfies the structural definition of a piezoelectric (+ piezomagnetic) medium, and classical electromagnetism is its piezoelectric response.** It introduces no free parameter, predicts no new number, and relaxes no standard-EM result. It sits at the same Class B ceiling as the EE-as-substrate-native META framework (§6, canonical-source-ceiling rule) — a vocabulary translation over canonical axioms, not new substrate-mechanism content. Full record: [`research/2026-06-08_vacuum-as-chiral-piezoelectric.md`](../../../../research/2026-06-08_vacuum-as-chiral-piezoelectric.md).

The mapping (each right-column entry is already canonical; the reframe adds no new row, only the observation that the right column *is* a chiral piezoelectric medium):

| Piezoelectric / Cosserat phenomenology | AVE substrate identity | Class | Anchor |
|---|---|---|---|
| Medium must be **non-centrosymmetric** to be piezoelectric (centrosymmetric class forbids it) | $I4_1 32$ chiral space group; centrosymmetric $Fd\bar{3}m$ is the $k_\chi=0$ supergroup (piezo-forbidden) | A axiom + B consistency | Ax 1 INVARIANT-S2; [`claim-quality-closure-roadmap.md`](../../claim-quality-closure-roadmap.md):191 |
| **Direct effect:** strain $\to$ bound charge / polarization | $Q = \xi_{topo}\,x$ — displacement $\to$ topological charge (§1 row above) | A identity | Ax 2; §1 $\xi_{topo}$ identity |
| **Inverse effect:** applied field $\to$ strain | **E** = translational DOF; modulating the translational/$\varepsilon$ sector IS a lattice deformation | A identity | Ax 1 6-DOF decomposition |
| **Piezomagnetic / couple-stress:** stress $\to$ magnetization / micro-rotation | **B** = microrotational Cosserat DOF; antisymmetric stress $\sigma^A$ fires couple-stress $\to\omega$; force projects via force-stress (E) AND couple-stress (B) | A axiom + B consistency | [`trampoline-framework.md`](../trampoline-framework.md):183-196 |
| Universal **electromechanical coupling constant** $d$ | $\xi_{topo} = e/\ell_{node}$ — the **dielectric-invariant floor**; material piezo ($d_{ij}$) rides on top | A identity / B live-bench | [`project-cleave-01.md`](../../vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md):42-47 |

**The one falsifiable surface** is pre-existing and unchanged by the reframe: the universal $\xi_{topo}\cdot x$ floor is dielectric-invariant (topology-protected integer linking charge), while material piezoelectricity rides on top — the two-sided **C15-CLEAVE** femto-electrometer discriminator (P1 presence / P2 dielectric-invariance), the live bench at [`project-cleave-01.md`](../../vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md):42-47,65,87. The reframe supplies only the one-line reading: *C15-CLEAVE measures the vacuum's direct piezoelectric coefficient $\xi_{topo}$, separated from any material $d_{ij}$ by the gap-sweep + material-swap.*

> **Over-claim guard (`ave-evidence-framing-discipline`).** Correct strength: EM **is** (in substrate vocabulary) the vacuum's piezoelectric response — an identity-by-translation. NOT "EM emerges from / is derived from piezoelectricity" (causally backwards, too strong). The non-centrosymmetry tie is a Class B consistency observation; it does NOT independently select $I4_1 32$ (that is the substrate-topology argument, §7 Probe 2).
