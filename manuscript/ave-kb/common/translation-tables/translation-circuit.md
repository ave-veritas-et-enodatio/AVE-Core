[↑ Translation Tables](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-fy05jc, clm-eemap1, clm-2bkp7v]
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
| **Knee / proportional limit ($A^2 = 2\alpha$)** | **Varactor bias-onset** — the C-vs-V curve departs linear at the yield-knee $A^2_{yield} = 2\alpha$; strain-cost $\Delta S = 1 - \sqrt{1-2\alpha} \approx \alpha$ (onset of dressing / external load-transfer) | [`envelope-anatomy.md`](../envelope-anatomy.md) surface (iii), clm-3surfa; engine `chiral_lattice_v10.py:29-30` |
| **Dress edge (near-field dressing collar)** | **Biased-varactor ladder section** — the endpoint-bound dressing collar between knee and wall; the EM correction is a boundary integral over it (spectator interior, #693) | [`envelope-anatomy.md`](../envelope-anatomy.md) §"radial-ladder", clm-ppasym |
| **Uniform external field** | **Common-mode bias** — a uniform DC offset on the whole ladder (shifts every varactor's operating point together) | [`form-deriving-value-importing.md`](../form-deriving-value-importing.md) §"The AC/DC carve", clm-acdc07 (i) — a uniform DC bias is gauge-relative and self-cancels (the common-mode component a differential measurement rejects) |
| **External field gradient** | **Differential bias** — a bias gradient across the ladder (differential varactor operating points; the load-transfer / gravity-ledger direction) | [`envelope-anatomy.md`](../envelope-anatomy.md) clm-ppasym (path-participation asymmetry) |
| **INVARIANT-S2 SYM scaling** | Concurrent $\varepsilon$ and $\mu$ modulation = isotropic gradient-index (impedance-matched, $\Gamma = 0$) | [`alpha-invariance-symmetric-gravity.md`](../../vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) |
| **INVARIANT-S2 ASYM scaling** | $\varepsilon$ modulation only ($\mu$ fixed) = asymmetric substrate response = $\alpha$-modulating | same |
| **$\Gamma = -1$ saturation TIR boundary** | **Short-circuit ($Z \to 0$) / Total reflection** at the **magnetic-branch** saturation (Cosserat $\mu_{eff} \to 0$ → trapped topological knot → rest mass; clm-lv3uw1). NOT the dielectric-yield boundary: $\tau_{yield}$ is the **electric** branch ($\varepsilon_{eff} \to 0$, $Z \to \infty$, **open-circuit**, $\Gamma \to +1$) — the two Ax-4 branches are mutually exclusive, per [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):78-79 | Op3 anchor in [`operators.md`](../operators.md); [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):78-79 (clm-lv3uw1) |
| **Saturated capacitor — incremental OPEN** (2026-07-15 saturation-anatomy addendum) | polarization exhausted, $C_{diff}\to0$, incremental **open-circuit** ($\Gamma\to+1$; electric branch $\varepsilon_{eff}\to0$, $Z\to\infty$) — clips charge, **voltage-stiff**. Leaves the storage business, joins the boundary business ($\lvert\Gamma\rvert\to1$); ideal saturation **dissipates nothing** (lossless refusal, Ax3) | [`envelope-anatomy.md`](../envelope-anatomy.md) §"saturation anatomy"; the electric branch of the $\Gamma=-1$ row above (clm-lv3uw1) |
| **Saturated inductor — incremental SHORT** (2026-07-15 saturation-anatomy addendum) | magnetization exhausted, $L_{diff}\to L_{air}$, incremental **short-circuit** ($\Gamma\to-1$; magnetic branch $\mu_{eff}\to0$, $Z\to0$ — the choke becomes a wire) — clips flux, **current-soft**. The $\Gamma=-1$ magnetic-branch wall = the trapped topological knot / rest mass | [`envelope-anatomy.md`](../envelope-anatomy.md) §"saturation anatomy"; the magnetic branch of the $\Gamma=-1$ row above (clm-lv3uw1) |
| **Vacuum-node exhaustion** ($A\to1$, $S\to0$) (2026-07-15 saturation-anatomy addendum) | the node **leaves the storage business, joins the boundary business**: its clock **STOPS** ($\omega_0\sqrt{S}\to0$ = the $g_{00}\to0$ signature, Ruling 1 at its limit) AND it becomes a **mirror** ($\lvert\Gamma\rvert\to1$). THE WALL = a closed curve of such cells (TIR = a **ring of reactive refusal**); open-vs-short = the ruled #260 SIGN/spin selector | [`envelope-anatomy.md`](../envelope-anatomy.md) §"saturation anatomy" (clm-3surfa wall / clm-lv3uw1 #260) |
| **Heat (bound-structure register)** (2026-07-15; check fired PR #707) | **clock phase-diffusion** between soliton tanks: mean shift = thermal operating point ($\delta_{strain}$/TCC), variance = heat content (Johnson-Nyquist); under Ax3 **heat = decoherence, NOT dissipation — ✓ CHECK-CORROBORATED** (PR #707: isolated Op14 phase BOUNDED / reversible). Entropy = lost phase information: **still ⚠ PROPOSED**. Temperature = clock-detuning width: **🔴 DEMOTED / RE-GATED on the unbuilt F6 $\varepsilon\to T2$ irreversibility** (PR #707 `ADDITIVE-ARTIFACT` — the diffusion is kernel-independent) | [`thermal-phase-registers.md`](../thermal-phase-registers.md) §2 (post-check status); the $\delta_{strain}$ row (below) + the Johnson-Nyquist thermal-noise-floor row (below) |
| **$\Gamma = 0$ matched-impedance** | **Filter-theory matched-impedance / peak power transfer** | Op17 anchor in [`operators.md`](../operators.md) |
| **Op17 $T^2 = 1 - \Gamma^2$** | EE power-transmission identity | [`operators.md`](../operators.md) Op17 |
| **Op21 $Q = \ell$ at $\Gamma = -1$** | EE Q-factor at boundary mode confinement | [`op21-multi-mode-mode-counting.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md) |
| **Vacuum breakdown at $E_S$** — spontaneous (Schwinger) / seeded (QED cascades) | **Zener interband field-tunneling** (spontaneous) / **Miller avalanche, impact ionization** (seeded) at $V_{BR}$ — split ruled 2026-08-05, see the carrier-sector section | [`four-regimes.md`](../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) Regime III |
| **Miller multiplication $M = 1/S(r)^2$** | Standard semiconductor avalanche-multiplication formula | Op22 anchor in [`operators.md`](../operators.md) |
| **Topological winding $(p, q)$** | **Toroidal transformer winding numbers** (primary $p$, secondary $q$) — integer topological invariants | [`torus-knot-uniqueness.md`](../../vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md) |
| **SU(2)→SO(3) double cover** | **Transformer 2:1 galvanic-isolation winding ratio** (traverse primary twice for one secondary cycle) | [`torus-knot-uniqueness.md`](../../vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md) |
| **$(2, 3)$ Clifford-torus winding (electron)** | **2-primary / 3-secondary toroidal transformer winding pattern** | same |
| **Hopf bundle / Hopf-fibration projection** | **Toroidal transformer flux-linkage topology** (linking number of magnetic flux through hole = topological invariant) | same; cross-link cosmology Hopf |
| **Orthogonal flux-tube crossing ($\cos\theta = 0$; Borromean / quadrature)** | **Quadrature (90°) coupling → cross-term $2A_1A_2\cos\theta \to 0$ → zero-reflection matched ($\Gamma=0$, $T^2=1$, unity coupling)**; parallel ($\cos\theta=1$, Hopf link) = mismatched/repulsive — the geometric realization of Op17 $\Gamma=0$ at a flux-tube crossing | [`thermal-softening.md`](../../vol2/particle-physics/ch02-baryon-sector/thermal-softening.md):71-93 + Op17; baryon per-channel $k=1$ ([R2 result](../../../../research/2026-06-01_baryon-R2-crossing-coupling-result.md)) |
| **Machian $G$** | **Distributed transmission-line input impedance at Hubble-horizon termination** | [`omega-freeze-cosmic-grain-cascade.md`](../omega-freeze-cosmic-grain-cascade.md) |
| **$R_H/\ell_{node} \sim 10^{39}$** (precisely $\approx 3.456\times10^{38}$) | Number of lumped substrate cells along cosmic-scale distributed TL | same |
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
| **Equivalence principle** (gravitational charge $\equiv$ inertial mass) ⚠ regime-tag | **CMRR — COUPLING-level common-mode rejection.** **At the WEP / composition level** CMRR is **infinite BY IDENTITY**: gravitational charge ≡ inertial mass, nothing to mismatch under a uniform (common-mode) drive; the **tide is the DIFFERENTIAL mode**. **At the SEP level CMRR is FINITE / measurable in principle** — the Nordtvedt gravitational-self-energy term is a nonzero mismatch (both surviving T4 branches REQUIRE a finite value; whether it clears the bound = **A7**), so "infinite" is a WEP-scoped statement, not an SEP one. Regime: **A1 gravity, sub-yield.** **DISTINGUISH from the $\varepsilon$-sector gauge rider = READOUT-level CMRR** (same instrument word, DIFFERENT mechanism): a common-mode / uniform-bias $E$ **LOADS the Q-point but reflects nothing** ($\nabla A=0$). Coupling-level (EP) vs readout-level (gauge rider) is the axis. | WEP-CMRR $\sim10^{-15}$ (Eötvös / MICROSCOPE), SEP-CMRR $\sim10^{-4}$ (LLR-Nordtvedt, finite); gauge rider [`claim-quality.md`](../../vol4/claim-quality.md):1856 ("uniform-bias gauge rider does NOT rescue the muon, $\nabla A\ne0$"); originating leaf = EP-CMRR acceptance test [`…_prereg_FROZEN.md`](../../../../research/2026-07-11_ep-cmrr-acceptance-test_prereg_FROZEN.md) + `src/tests/engine_acceptance/test_ep_cmrr.py`. **Consistency / register class; no chord mint.** |
| **A1/T2 far-field radiation partition** (bulk-dilatation P vs shear-transverse S from a rotating mass quadrupole) — ⚠ **cross-discipline** (elastodynamic / seismological analog, NOT EE) | **Seismological P/S quadrupole partition** (isotropic Poisson elastic solid; Aki–Richards moment-tensor radiation): the substrate's DERIVED angular partition $\mathcal{A}_{ang}=I_P/I_S=(8\pi/15)/(4\pi/5)=2/3$ is the inverse of the *identical* P/S angular integrals — seismology is the elastic-medium sibling discipline, the measurement analog of the substrate's elastodynamic sector (alongside the EE rows above). Means-test PASS at value level (§6 #28, $E_S/E_P\approx23.4$) | means-test #28 (§6); [`port-register.md`](../port-register.md) (Q1 row + A1/T2 channels) + [q1-pulsar-hardening](../../../../research/2026-07-20_q1-pulsar-hardening.md) §1,§6 🔴 **[DEMOTED 2026-08-11 — R40-B1; note at EOF]** |

This table is the canonical first-call reference for substrate-primitive → EE-component lookup. Where a row's EE mapping is canonical at a referenced leaf, the leaf carries the derivation; this catalog enumerates the mapping without re-deriving. ★**Tier pointer (2026-08-07):** the **transmission-line MODE tier** — the $A_1$/$T_2$ carve read as common/differential mode, KEEP-BOTH against the seismological row directly above — is landed at **§12** (EOF-appended for line-pin safety, §4.6.2/§4.7.2 row pattern).

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
| 3-port junction / tee scattering (matched-lossless-reciprocal-3-port theorem) | Op3 ($S_{11}$) + Op6 ($\lambda_{min}(S^\dagger S)\to0$) | ✓ | **The srs $z=3$ vertex = an intrinsically MISMATCHED reciprocal 3-port.** A wave down one bond sees the other two in parallel ($Z_0/2$), so the bare junction reflects $\Gamma=(2-z)/z=-1/3$ (a COUNTING fact — one bond feeding two, immune to symmetric transformation), reactively back-scattering / redistributing $|\Gamma|^2=1/9$ of the power (Axiom 3 — **reactive, not loss**). The floor $|S_{11}|\ge1/3$ is the classic **matched-lossless-reciprocal-3-port theorem** (Pozar §7.1 class) — attributed known theory, **confirmed at the vertex** (exact perfect-square identity), so Op6's reflectionless target $\lambda_{min}\to0$ is **UNREACHABLE by any bore of the LOSSLESS reciprocal class**. **The matched alternative is the non-reciprocal circulator** ($S_{11}=0$, unitary, $C_3$; the reciprocal-class evanescent-stub escape is theorem-dead, #620) — needs a **T-breaking** bias (candidate $u_0^{*}/\Omega_{\text{freeze}}$; srs $I4_132$ chirality is only P-breaking) — **PENDING-GRANT**, asserted nowhere. The ✓ is the geometry-independent theorem confirmation (a known identity, canonical leaf); the two-axis Op6 bore verdict (broadband $f^{*}=0$ unique; single-frequency $\{0, f_{\text{touch}}=\sqrt2/\pi\}$ degenerate — half-wave-invisible bore family) is "demonstrated, not adjudicated". Canonical: [`srs-vertex-scattering.md`](../../vol1/operators-and-regimes/ch6-universal-operators/srs-vertex-scattering.md) (`clm-v3port` floor, `clm-bore2x` bore verdict; X38/X37, PR #619/#616/#620). **In-band homogenization (T4 fork close, PR #669, 2026-07-13):** the bare per-vertex $|\Gamma|^2=1/9$ is a real reactive event but is **homogenized away for in-band collective carriers** ($\sigma\approx0.12$ of the incoherent limit) and only **resolves near the band edge** (crosses $1/9$ at $k\cdot\ell\approx1.85$) — CONSISTENCY / peer-with-SM; band edge not independently located (probe reached $k\cdot\ell\le0.83$). Cross-ref only, no new claim: `research/2026-07-13_srs-vertex-ksweep-backscatter_RESULT.md` |
| I/Q quadrature / forward–backward $(V_{inc}, V_{ref})$ phasor decomposition | Op3 + K4-TLM scatter — the **intra-K4 linear $E$↔$B$** | ⚠ | the bond's incident/reflected voltage waves ARE the photon's own quadrature: $E \sim (V_{inc}+V_{ref})$, $B \sim (V_{inc}-V_{ref})/Z$ — a LINEAR $E$↔$B$ internal to the K4 sector (distinct from the *parametric* K4↔Cosserat bridge in the Resonance family). Code-confirmed (`k4_tlm.py`:192-206, 340, 400); **consolidating canonical leaf landed 2026-06-04: [`photon-ee-mapping.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md) §4** (row stays ⚠ not ✓ — consolidation is a description, not an emergence derivation). Gate (a) 2026-06-04 ([`…alpha-quarter-hypothesis.md`](../../../../research/2026-06-04_ee-rf-quadrature-coupling-and-alpha-quarter-hypothesis.md) §8). NB: the $R{\cdot}r=1/4$ phasor-radius question that lives in this sector is a *separate* claim — **gate (b) RESOLVED-NEGATIVE 2026-06-04**: the kinematic phasor↔real-space area bijection does NOT lift it (Class B, α-substituted; bridge forces R·r→4π²α ≠ ¼; [`bijection-result`](../../../../research/2026-06-04_alpha-class2-bijection-result.md)). This row asserts only the linear-quadrature decomposition (gate (a), separate) |
| Transmission line (ABCD, propagation) | Op1 + Op13 ($\Box^2$) + Op16 ($c_{shear}$) | ✓ | $Z_0$-ladder ([`z0-derivation.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md)); K4-TLM cascade; Op13/Op16 in [`operators.md`](../operators.md):53,56 |
| Power transfer / matched-$Z$ | Op17 ($T^2 = 1 - \Gamma^2$) | ✓ | identity ([`operators.md`](../operators.md):57) |
| Smith chart ($Z \leftrightarrow \Gamma$) | Op1 + Op3 | ⚠ | explicit Smith-chart leaf landed 2026-06-13: [`cvr-reflection-smith.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md) — the $\Gamma(A_0)$ matched→short locus, $|\Gamma|^2=1-\alpha$, chiral 2×2 $S$. ⚠ not ✓ (consolidation/description, not emergence) |
| Network theorems (Thévenin / Norton, 2-port) | Op1 / Op3 + §8 ladder networks | ⚠ | partial — ξ_topo ladder + Op5 multiport exist; Thévenin/Norton reduction not consolidated |
| Bias-point + small-signal (**.OP / .AC methodology**; grown-equilibrium then linearize) | Ax4 self-saturation Q-point (the **.OP** analog) + Op14 ($Z_{eff}=Z_0/\sqrt S$) + INVARIANT-S2 small-signal ($\varepsilon_{eff}=\varepsilon_0 S(A_0)$ etc.) (the **.AC** analog) | ⚠ | 2026-07-21 (semiconductor-analysis tier, §4.6). The two-step SPICE method — solve the nonlinear DC operating point, then linearize small-signal about it — maps structurally: the soliton **self-biases** to its Q-point ("grown equilibrium" = .OP; [`resonant-lc-solitons.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md): "Axiom-4 self-saturation IS the bias mechanism"), then small-signal transverse propagation sees the modulated $\varepsilon_{eff}/\mu_{eff}/C_{eff}$ (.AC; CLAUDE.md INVARIANT-S2 operating-point clause; `vol_9…/05_ac_electrical_characteristics.tex` small-signal-at-$A_0$ table). ⚠ not ✓ — a **consolidation** of the already-present small-signal-at-operating-point machinery under one method name, NOT an emergence derivation |
| Homogenization boundary conditions + two-sided variational bounds (**KUBC / SUBC / PBC**; Dirichlet–Thomson) | Op5 (multiport $[Y]$ = the boundary Schur complement of the block Laplacian; [`operators.md`](../operators.md):45) + Op1 (the $r_Z = Z_{bulk,eff}/Z_0$ read; :41) | ⚠ | 2026-07-28 (network-analysis tier, §4.7). **KUBC = drive the ports with voltage sources and read $[Y]$; SUBC = drive with current sources and read $[Z]=[Y]^{+}$** — one multiport, two excitations, and the Hill/Huet ordering IS the Dirichlet/Thomson two-sided bound on effective conductance (same PSD quadratic form, Dirichlet vs Neumann partition; block Laplacian vs scalar Laplacian). The Schur-complement→$[Y]$ reduction is **exact algebra** — but it is **Kron's** exactness (`physics-lineage-map.md` T8: *"an exact isomorphism is ontologically silent"*), so **consistency-class, no chord**. ⚠ **not** ✓ for two stated reasons: (i) no consolidating canonical leaf derives it end-to-end; (ii) the corpus's only running instance (`research/2026-07-28_subc-kubc-bracket_result.md`, **`#802` — MERGED 2026-07-28**; this cell read *"PR #802 OPEN"* until the 2026-08-02 marker sweep, the merge does **not** change the verdict below) is **VOID AS FROZEN** on two criterion-side counts with its bracket **computed-not-banked** (the instrument validation — bit-exact #782/#796 reproduction, G3/G4/G5 — is what passed). ★**Regime fence:** static / DC / single-sign-susceptance ONLY — for a mixed-reactance AC network $B(\omega)$ is not sign-definite and both bounds FAIL. Full carve + the three disanalogies (no rotational sector; no A1/T2 split; dissipated-vs-stored) at §4.7 |

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

Tally across the four families: **19 ✓ solid, 11 ⚠ partial, 2 ✗ gaps** (32 rows; 2026-07-28: +1 ⚠ in the Impedance & transmission family — **homogenization boundary conditions + two-sided variational bounds (KUBC/SUBC/PBC; Dirichlet–Thomson)** ↔ Op5 multiport $[Y]$ + Op1 (network-analysis tier, §4.7). The KUBC↔voltage-clamp / SUBC↔current-feed duality and the Hill/Huet↔Dirichlet/Thomson bound pair are **exact** on the static block-vs-scalar Laplacian — but it is Kron's exactness, hence ontologically silent / consistency-class, the regime fence is static-single-sign only, and the sole running instance (PR #802) is VOID-as-frozen with its bracket computed-not-banked. 2026-07-21: +1 ⚠ in the Impedance & transmission family — the **.OP/.AC bias-point + small-signal methodology** ↔ Ax4 self-saturation Q-point + Op14 + INVARIANT-S2 small-signal (semiconductor-analysis tier, §4.6; a consolidation of the already-present small-signal-at-operating-point machinery, not emergence). 2026-07-10: +1 ✓ in the Impedance & transmission family — the srs **$z=3$ vertex 3-port** ↔ Op3 + Op6, the **matched-lossless-reciprocal-3-port theorem** confirmed at the vertex ($\Gamma=-1/3$ counting fact, $|S_{11}|\ge1/3$ floor = $1/9$-power reactive branch back-scatter; the circulator is the **non-reciprocal matched alternative**, T-breaking PENDING-GRANT; two-axis Op6 bore verdict demonstrated-not-adjudicated; X38/X37, `clm-v3port`/`clm-bore2x`). 2026-07-10: +1 ✓ in the Resonance/nonlinear/wave family — the **difference-tone mixer / inversion-symmetry meter** ↔ Op2 odd-$\chi^3$ parity (PR #610, `clm-invmtr`); the ✓ is the geometry-independent parity identity (difference tone forbidden sub-yield), while the *frequency form factor* stays interface-scoped / bulk-open. 2026-07-09: +2 ✓ in the Resonance/nonlinear/wave family — the srs **band-structure / dispersion survey** ↔ coined-quantum-walk / TLM arccos map (gate-passed #604/#607, clm-bnd5rq) and the **slew-rate / full-power-bandwidth** algebraic identity ($A_I=\dot E/(E_c\omega_0)$; #595 — algebra ✓, physical FPB framing stays unmerged). 2026-06-13 update — the Smith-chart + general-$H(s)$ ⚠ rows gained explicit consolidating CVR leaves, and Nyquist/root-locus flipped ✗→⚠ via the CVR stability-eigenmode leaf's descriptive structure; the 2026-06-04 ⚠ pair was I/Q phasor + degenerate parametric amp). 2026-06-14: the autoresonance gap's *genesis-self-lock application* is now TESTED-NEGATIVE (T2), but the row stays ✗ and the tally stays **2** — the mapping + the PLV/autoresonance detector instrument remain open (phasor-redesign prereg deferred); a tested-negative application is not a resolved mapping. The structurally load-bearing observation is that **the remaining ✗ are both in the control / feedback family** (PLL, autoresonance — stability closed to ⚠) — but they split by anchor: **PLL + stability point at Op14** (Dynamic Impedance / cross-sector feedback), while **autoresonance is a distinct Op21 + Γ=−1 self-lock gap** (per the matrix row). The control-loop axis is the next mapping frontier:

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

## §4.6 — Semiconductor-analysis tier (2026-07-21 vessel-state / rim-inversion walk)
<!-- claim-quality: clm-eemap1 -->

**Attribution (never blended).** Grant proposed the semiconductor-analysis mapping **class** — verbatim `[sic]`: *"and now i think weve entered the realm of semiconductor anakysis and mathematical tools, i think a lot of them will cleanly map to this problem/walks"* — and authorized landing this tier with the sweep-first caveat, verbatim `[sic]`: *"fire but for a) we have likely a lot of this in vol 4/9 already."* The specific row formulations below are orchestrator / lane walk-level (the 2026-07-21 vessel-state + rim-inversion walk). This subsection is under `clm-eemap1` (the META catalog) — a **consolidation** of existing semiconductor content plus a small set of means-tested new rows, NOT a new emergence claim.

### §4.6.1 — Sweep first: the semiconductor content the corpus ALREADY carries (consolidation index)

Per Grant's caveat, a two-method sweep (`grep -rn` + `git grep`) of vol 4 / vol 9 / KB / this leaf was run BEFORE minting. The prediction held — the semiconductor mapping is heavily pre-existing. This index is the single findable map of it (do NOT re-mint these; cross-ref them):

| Existing semiconductor content | Where it lives | What it maps |
|---|---|---|
| **Ideal-diode / Ideal-BJT non-ideality catalog** | §9.2 above (this leaf) | junction capacitance $C_j(V)$ ↔ boundary bond cap **modulated by depletion-region width**; avalanche $V_{BR}$ ↔ Schwinger/Miller; forward drop $V_F$; reverse leakage; reverse recovery $t_{rr}$; $\beta$; $V_{CE(sat)}$; $V_{BE}$; **Early effect ↔ depletion-width modulation**; $f_T$; $I_S$ |
| **T4 finite-boundary axis** | §9.1 above (this leaf) | "junction capacitance, input bias current $I_B$, depletion capacitance, contact resistance, $V_{CE(sat)}$, $V_{BE}$" ↔ $\Gamma\neq0$ at internal impedance boundaries |
| **Native Silicon Design Engine** (full chapter) | `vol_4_engineering/chapters/19_silicon_design_engine.tex` | Semiconductor Translation Matrix (charge carrier e/h ↔ phase-slip / topological void; band gap $E_g$ ↔ $V_{BR}=6\alpha\hbar c/D_{intra}$; Fermi level ↔ LC baseline gradient; $V_{bi}$ ↔ static DC impedance reflection; Shockley $I$-$V$ ↔ $T^2(V)$ modulation), **Doping-as-Geometric-Perturbation** (Boron ↔ removed $sp^3$ port / inductive void; Phosphorus ↔ surplus topological array), **p-n junction ↔ S-parameter boundary** (depletion zone ↔ impedance step $Z_p\to Z_n$), **BJT gain** (cascaded $T^2$, Miller multipliers), native SPICE `.SUBCKT` |
| **Silicon falsification** ($V_{bi}$ / dopant / $m^*$ / amphoteric) | `vol_4_engineering/chapters/11_experimental_falsification.tex`:463 + `vol6/period-3/silicon/topological-area.md` | $V_{bi}\approx1.05$ V structural-lock vs SM's thermal-statistical "Weather Forecast"; $m^*$ + mobility as the SM fitting parameters AVE strikes |
| **C-V small-signal tracking falsifier** | `vol_4_engineering/chapters/12_falsifiable_predictions.tex`:33-45 | LCR small-signal tangent $C_{ss}=C_0(S-A^2/S)$, negative-differential-capacitance stability boundary at $E/E_{yield}=1/\sqrt2$ |
| **Semiconductor I-V phase diagram** | `vol_9_vacuum_datasheet/chapters/14_phase_diagrams.tex` (cross-refs this leaf §9 + §4) | DC bias / switching / avalanche ($M\ge2$) / junction-destruction ↔ Regime I–IV; Zener-knee; APD gain $M_{APD}$ |
| **Small-signal-at-operating-point AC table** | `vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex` §"Small-signal modulation table at operating point $A_0$" + §"DC operating point and the two speeds"; **MOSFET $V_{th}$ analogue** at §"Critical-Voltage Pair" | $\varepsilon_{eff}=\varepsilon_0 S(A_0)$, $\mu_{eff}=\mu_0 S(A_0)$, $C_{eff}=C_0/S(A_0)$ AC characterization at DC bias $A_0$; the vacuum's $(V_{th}:V_{BD,ox})$ pair |
| **Device circuit models + SPICE cell** | `vol_9_vacuum_datasheet/chapters/03a_device_circuit_models.tex` | metric-varactor sector keying; small-signal $C_{ss}=C_0/S^3$; per-regime small-signal-at-bias |
| **VCA symbol catalogue** | [`appendix-vca-symbols.md`](../appendix-vca-symbols.md):36-41 | Geometric Diode ↔ P-N Junction Diode (#1); **Geometric Triode ↔ MOSFET/FET** (#2); Topological Y-Junction ↔ XOR/CMOS (#6) |
| **Regime ↔ device-region map** | [`four-regimes.md`](../../vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) §Semiconductor Device Analogy; [`temporal-saturation-regime-classifier.md`](../temporal-saturation-regime-classifier.md):76-85 (MOSFET cutoff/triode/saturation ↔ Regime I/II/III); [`semiconductor-regime-chemistry.md`](../../vol6/framework/chemistry-translation/semiconductor-regime-chemistry.md) | Regime I small-signal ($g_m$, $r_\pi$, $C_\pi$) / II large-signal / III avalanche / IV breakdown ↔ $S(V)=\sqrt{1-(V/V_{BR})^2}$ |
| **Already-canon §4 rows** (verified present, NOT re-minted) | §4 rows above + §6 #7/#8/#11 | $S(A)$ ↔ varactor C-V near breakdown; operating-point $A_0/A_{yield}$ ↔ DC bias point; Schwinger ↔ Miller avalanche at $V_{BR}$; $M=1/S^2$ ↔ avalanche-multiplication |

### §4.6.2 — Means-tested NEW rows (the vessel-state / rim-inversion walk objects)

Three genuinely-new rows that connect the **vessel-state / rim-inversion walk objects** to semiconductor structures NOT already covered by §4.6.1. Each is means-tested (structural, not decorative); each is **KEEP-BOTH** (it does not redefine any §4.6.1 row). Walk provenance (cite by path; may be unmerged): `saturation-rim-inversion.md` (PR #790, merged 2026-07-21) + `research/2026-07-21_phase-space-inversion-walk_RECORD.md` (PR #790); `research/2026-07-21_rve-aggregation-bench_result.md`; `research/2026-07-21_boundary-strain-amplitude_result.md`.

| # | Substrate primitive (walk object) | Semiconductor analog | Means-test verdict |
|---|---|---|---|
| **A** | **Vessel shell / envelope skirt** — the soliton's self-organized real-space roll-off layer $S(A(r))$ where the rim-dwelling saturated core hands back to interior-dwelling far field; the balance shell's hoop/radial force balance (`saturation-rim-inversion.md` (PR #790, merged 2026-07-21) §"vessel-state skirt"; [`envelope-anatomy.md`](../envelope-anatomy.md)) | **p-n junction depletion region** — self-organized boundary layer of two opposed tendencies (built-in stress ↔ built-in field; radiation-pressure-out vs elastic-restoring-in ↔ diffusion vs drift); squeeze/stretch narrows/widens the shell ↔ forward/reverse bias narrows/widens the depletion width; marginality-at-yield-knee ↔ breakdown knee | **STRUCTURAL PASS** — same governing structure (a self-organized graded boundary layer from two balanced opposed transport/force tendencies, carrying a built-in bias whose width responds to external bias). **Value-level OPEN** (the depletion $\sqrt{V_{bi}-V}$ width scaling vs the skirt strain profile) — owned by the parallel-lane boundary-strain / RVE bench, cross-ref not claimed. **Consistency-class.** **KEEP-BOTH:** distinct from the §9 "junction capacitance $C_j(V)$ ↔ depletion-region-modulated boundary bond cap" *component-non-ideality* row — this row is the *envelope-object ↔ equilibrium-boundary* reading. |
| **B** | **Saturation wall** — the $\Gamma=-1$ / $A\to A_{yield}$ locus, a $\sim$1-node-thick fully-saturated boundary ($S\to0$, $\lvert\Gamma\rvert=1$, roll-off both sides); the rim-inversion walk's **character-swap** (interior disk: amplitude-dynamic/phase-trivial ↔ boundary rim: amplitude-frozen/phase-topological) (`saturation-rim-inversion.md` (PR #790, merged 2026-07-21) `clm-riminv`; §4 saturation-anatomy rows) | **MOS inversion layer** — the thin field-induced channel at the oxide-semiconductor interface that appears at threshold $V_{th}$, where the surface region **inverts character** (p-bulk → n-surface), field-controlled by the gate, screening beyond it | **STRUCTURAL PASS** at the roles level — a thin field-threshold boundary layer + character-inversion + screening. **Disanalogy flagged (the mechanism differs):** MOS inversion produces a **conductive** channel (majority-carrier-type flip); the saturation wall produces a **reflective** ($\lvert\Gamma\rvert=1$, Ax3-lossless-reactive) mirror (phase-space-role flip). Same *role*, different *mechanism*. **Consistency-class.** **KEEP-BOTH:** distinct from the whole-device "Geometric Triode ↔ MOSFET/FET" ([`appendix-vca-symbols.md`](../appendix-vca-symbols.md) #2) — this row is the *wall-sub-structure ↔ inversion-layer* reading. |
| **C** | **Cages at density $\phi$** — the cage packing fraction $\phi$ and its effective-moduli curves $K_{eff}(\phi)$ / $r_Z(\phi)=Z_{bulk,eff}/Z_0$; shell-percolation $\phi_{perc}$ (`research/2026-07-21_rve-aggregation-bench_result.md` §5; #770/#782) | **Doping density** $N$ ($N_a/N_d$) — the effective-medium doping-density curve; heavy/degenerate-doping **percolation** of dopant states; **band-gap narrowing** (the constitutive-crash flavor) | **STRUCTURAL PASS** — density-of-inclusions → effective-medium response → percolation-onset → constitutive collapse. **Value-level LEANS / KUBC-conditional:** the RVE result RETRACTED the "intermediate crash" reading and re-graded to "tracks the coated-inclusion parallel/bypassing bound" ($K_{eff}/K_0\approx0.16$–$0.19$; crash is KUBC-conditional), so "constitutive crash ↔ band-gap-narrowing" is a **candidate**, not established; $\phi_{perc}$ is route-dependent (interior-$\phi$ 0.09/0.13) vs route-independent (coated $f_{incl}=\pi/6\approx0.524$). **Consistency-class.** **KEEP-BOTH / CONSOLIDATE:** vol 4 Ch 19 "Doping as Geometric Perturbation" is the **atom-scale** dopant reading (Boron/Phosphorus ↔ port removal/insertion); this row is the **density/percolation** reading — distinct, both preserved. |

### §4.6.3 — Cross-ref-only (parallel-lane-owned; NOT minted here) + one open flag

- **C-V profiling ↔ $K(\varepsilon_{bias})$ profiling** — reconstruct the vessel-shell profile by sweeping quasi-static strain bias and reading small-signal stiffness. The C-V machinery is pre-existing (§4 varactor row; `12_falsifiable_predictions.tex` $C_{ss}$; §9 diode $C_j(V)$); the $K(\varepsilon_{bias})$ **protocol** is being folded into the vessel-state RVE prereg by a parallel lane (`research/2026-07-21_rve-aggregation-bench_prereg-FROZEN.md`). **Cross-ref only — do NOT duplicate the protocol here.**
- **Effective mass $m^* = \hbar^2/(d^2E/dk^2)$ ↔ dispersion-read inertia** — a candidate derivation route for the D1 sector-crossed $c^2$ question, being scoped by a parallel lane; it would ride the existing band-structure machinery (§4.5(b) "Band-structure / dispersion survey" ✓ row; [`srs-band-structure.md`](../../vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md)). **Cross-ref only.**
  - **⚑ OPEN FLAG (flag-don't-fix — routed to Grant, NOT resolved here).** The corpus is currently in **tension on $m^*$**: it is **struck as SM-garbage-to-obsolete** in `vol_4_engineering/chapters/19_silicon_design_engine.tex`:45 ("rendering the entire thermal mobility and effective-mass ($m^*$) parameter set obsolete"), `11_experimental_falsification.tex`:463 ("empirical fitting constants (effective mass $m^*$)"), and the `doping_engine_map.svg` strikethrough (`vol6/period-3/silicon/topological-area.md`:17 is the SOFTER stance — it peer-frames the structural reading with the thermal-$m^*$ treatment rather than striking it, per the 2026-07-21 audit precision note) — **while** candidate-6 proposes $m^*=\hbar^2/(d^2E/dk^2)$ as a **substrate-native dispersion-read inertia to DERIVE** (and vol 2 Ch 7 + vol 3 already USE an AVE composite/emergent effective mass: $m_{eff}=m_e\sqrt{1+k}$, and "effective mass emerges from the converged field's own integrated energy"). Same symbol, opposite disposition (SM-fitting-param-to-strike vs substrate-native-quantity-to-derive). Surfaced with paths; adjudication is Grant's.
  - **✅ RULED 2026-07-26 — flag DISCHARGED (the evidence above is preserved byte-untouched per Rule 12; this block is additive and dated).** Grant, verbatim `[sic]`: *"correct, should not be a fitting parameter, a plus c should make sense"* — ratifying option **(a)+(c)**: the corpus's strike of $m^*$ **stands byte-untouched**, AND a disambiguating `def-` node is minted. **The tension was a HOMONYM, not a physics conflict:** $m^*$ names **two distinct objects**, separated by Grant's discriminator **derived-not-fitted** — **Sense A** = the SM thermal-statistical **fitting parameter** (an empirically fitted knob), which is what the `:45` / `:463` strike removes and which **stays struck**; **Sense B** = a **derived / substrate-read inertia** (the composite $m_{eff}=m_e\sqrt{1+k}$, the emergent $M_{eff}$, the dressed-branch acoustic $\rho_{eff}$), **a different object and not struck**. Canonical node: [`vocabulary-register.md`](../vocabulary-register.md) **`def-mstar1`** (status `ambiguous` — the surface symbol stays overloaded; the *disposition* is ruled). A distinct **name** for Sense B (**"dressed effective density"**) is minted there **proposed-for-ratification** with a surfaced dimension caveat — nothing is renamed at any site by that entry, so the `:45` / `:463` / `topological-area.md`:17 stances are all unchanged.
  - **★Consequence for the candidate-6 route above (2026-07-26).** The literal band-bottom read $m^*=\hbar^2/(d^2E/dk^2)$ is **DECORATION for the D1 question**, not a derivation of it: it is sector-blind at $k\to0$ (every gapped branch returns $m^*v^2=\hbar\omega_0=E$ identically — the gap divides out and the read hands back *that branch's own* $c^2$), so it **cannot adjudicate** which sector's $c^2$ divides $E_{trapped}$ (`research/2026-07-21_continuum-radial-solver_CHARTER.md`:15 D1, :62 I8). D1 stays **OPEN** on its own axis (the sector-of-storage walk, `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md` §1 item 13). The "cross-ref only" status of the row above is unchanged; what changes is that it is no longer carried as a *candidate derivation route for D1*. The finding has no tracked research doc as of this dated block — it is recorded at `def-mstar1`.

### §4.6.4 — Two-band / k·p near-gap kinematics (2026-08-05 two-band-kinematics lane)
<!-- claim-quality: clm-2bkp7v -->

**END-APPEND to the semiconductor tier; line-pin-safe (nothing above is edited).** Provenance:
`research/2026-08-05_two-band-kinematics_prereg-FROZEN.md` (frozen alone at `f5ddd995`) +
`research/2026-08-05_two-band-kinematics_result.md`; driver
`src/scripts/vol_1_foundations/two_band_kp_kinematics.py`; shipped artifact
`research/drivers/two_band_kp_kinematics_results.json`, gated by
`make verify-two-band-kp-number-check` (with mutation receipt). Operator: the CI-gated
canonical 12×12 Cosserat two-sublattice Bloch matrix (PR #392), reproduced independently
(G1, bit-exact) and re-certified against its own V1–V4 receipts (G2) before any new number
was read.

| # | Substrate primitive | Semiconductor analog | Means-test verdict |
|---|---|---|---|
| **D** | **Near-gap two-band structure of the carrier sector.** $D(0)$ is exactly diagonal: a 6-fold gapless translational ($u$) manifold and a 6-fold micro-rotational ($\omega$) manifold at $m^2 = 4G_c/I_\omega$, coupled at $O(k)$ by the micropolar term. Second-order degenerate PT gives, exactly and isotropically (verified as a characteristic-polynomial identity in 5 directions): carrier $v^2 = 2\gamma/I_\omega$ (×2, $\boldsymbol\omega\parallel\mathbf k$) and $2\gamma/I_\omega + G_c/\rho$ (×4, $\boldsymbol\omega\perp\mathbf k$); translational $v^2 = G/\rho$ (×4, the photon) and $10G/(3\rho)$ (×2, P-wave). | **Two-band k·p / Kane model** — a gapped pair of bands with a linear interband momentum matrix element, whose near-edge dispersion is $E^2 = (E_g/2)^2 + (\hbar v k)^2$ and whose band-edge curvature gives $m^\ast = E_g/(2v^2)$; the standard semiconductor near-gap kinematics. | **STRUCTURAL PASS on the FORM** — the substrate's carrier sector reproduces the two-band k·p structure exactly, with no $O(k)$ term (inversion symmetry) and no $O(k^2)$ anisotropy. **★NUMERICAL DISANALOGY, and it is the load-bearing content:** the carrier does **not** have one limiting velocity, and neither of its two limiting velocities is $c_{EM}=\sqrt{G/\rho}$. The splitting is exactly the gap-opening modulus, $v^2_\perp - v^2_\parallel = G_c/\rho = (I_\omega/4\rho)\,m^2$, so a single carrier limiting velocity requires $G_c=0$ — **no gap**. No positive moduli give a massive carrier one limiting speed. At the engine's placeholder moduli $v/c_{EM} = \sqrt2$ and $\sqrt3$. **Consistency-class on the form (Wilsonian-universal: any gapped two-band lattice yields it, and the Dirac equation postulates it); the DISANALOGY is the reportable finding.** **KEEP-BOTH:** distinct from the §4.6.1 vol-4-Ch-19 "band gap $E_g \leftrightarrow V_{BR}$" *device-scale* row — this row is the *near-gap dispersion kinematics* reading. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |

**★The one branch that IS at $c_{EM}$, and why (a derived cancellation, not a fit).** The direct
micropolar stiffness contributes $(G+G_c)/\rho$ to the transverse-$u$ branch and the k·p level
repulsion from the gapped $\omega$ manifold subtracts **exactly** $G_c/\rho$, leaving
$v^2 = G/\rho \equiv c_{EM}^2$ **identically, for all moduli** — the long-wave micropolar→Cauchy
reduction obtained as an $O(k^2)$ k·p term. The photon's speed is protected; the carrier's is not.

**★Validity fence carried with the row (do NOT read the mismatch as superluminal transport).** On
this lattice the relativistic form's validity window closes *before* its own relativistic regime
opens ($k_{\text{break}}/k_{\text{rel}} = 0.387$ and $0.424$), and the full-BZ carrier group
velocity stays below $c_{EM}$ everywhere (sampled maximum $\approx 0.61\,c_{EM}$ — a random-point
LOWER bound; the supremum is uncertified, audit-measured $\geq 0.613$). The mismatch is in the **low-energy effective theory's
invariant speed**, not in observed energy transport. Root cause recorded: with
$\ell_{node}\equiv\hbar/(m_ec)$ there is no scale separation between the carrier's Compton scale
and the lattice cutoff, so no lattice regularisation of this family has a wide relativistic
window.

**Cross-ref — this row DISCHARGES nothing on the $m^\ast$ axis and confirms the §4.6.3 ruling.**
The 2026-07-26 dated block above rules that the literal band-bottom read $m^\ast=\hbar^2/(d^2E/dk^2)$
is *"sector-blind at $k\to0$ (every gapped branch returns $m^\ast v^2=\hbar\omega_0=E$ identically
— the gap divides out and the read hands back **that branch's own** $c^2$)"*. This lane's
independently pre-registered declaration that $m^\ast = E_g/(2v^2)$ is **tautological** is the same
finding, confirmed with residual `0.0`. What this lane adds is the **per-branch $c^2$ inventory in
closed form** — i.e. *which* $c^2$ each branch hands back. **D1 (sector of storage) stays OPEN**;
nothing here adjudicates it.

#### §4.6.4.1 — ★What is NOT landed here (flag-don't-fix, per the §4.7.4 precedent)

- **The Zitterbewegung correspondence row is REFUSED, not deferred-by-oversight.** The lane's own
  frozen prereg fences it (*"any Zitterbewegung claim — §6 is a documented consequence, mints
  nothing"*), and an unresolved **factor-2 tension** sits directly on the identification: under the
  relativistic reading the branch bottom is the REST frequency ($\hbar\omega_0=E_g/2$) and the
  $\pm\omega$ splitting is $E_g=2\hbar\omega_0$, but the placeholder moduli put the branch bottom at
  $\omega_m = 2\omega_C$, giving $E_g = 4\,m_ec^2$ (placeholder-conditioned; no MeV numeral rendered here per the
  VALUE refusal below) rather than the $2\,m_ec^2$ the Zitterbewegung / pair-threshold
  identification wants. Landing $E_g=2m_ec^2$ needs
  $G_c/I_\omega = 1/4$, not 1. Recorded at `research/2026-08-05_two-band-kinematics_result.md` §7
  FLAG-1; **not adjudicated**.
- **Nothing about the gap's VALUE.** The lane's VALUE-PROVENANCE axis returns **FACTOR DERIVED /
  VALUE IMPORTED**: the factor 4 is derived ([`cosserat-mass-gap.md`](../../vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md):61)
  but $G_c$ and $I_\omega$ are engine placeholders (`cosserat_field_3d.py`:12, :954; no
  `constants.py` symbol exists for either) and the MeV scale is imported from CODATA $m_e$ via
  $\ell_{node}$ (`cosserat-mass-gap.md`:143, :151).
- **Nothing on the ratified z=3 srs carrier.** The canonical Cosserat operator runs on the **z=4
  diamond CONTROL** net (`chiral_lattice.py`:240) rather than the D1-ratified `srs-z3` production
  carrier (`:231`). The srs re-run is **BLOCKED-STRUCTURAL**, measured: every srs site's bond
  tensor $\sum_b\hat d_b\otimes\hat d_b$ has spectrum $\{0,\tfrac32,\tfrac32\}$ (rank 2, trigonal
  planar), so the engine's least-squares gradient functional does not transfer without a new
  bond-based constitutive model. The $O(k^2)$ result above is nonetheless connectivity-INDEPENDENT
  (identical closed forms on z=6 cubic, z=8 bcc and an anisotropic z=4 stencil — the least-squares
  gradient symbol reduces to $i\mathbf k$ exactly for any full-rank centro-symmetric bond set), but
  the $k^4$ coefficients, band tops and zone-edge structure are **diamond-specific** and are not
  landed.
- **LC-1's arc-level kill is NOT fired.** That requires an energy-carrying *inter-event* channel at
  $\neq c$; this lane does not establish the carrier branch is one.

---

## §4.7 — Network-analysis tier: the homogenization ↔ resistor-network boundary duality (2026-07-28 SUBC/KUBC bracket lane)
<!-- claim-quality: clm-eemap1 -->

**Attribution (never blended).** Grant authorized landing this correspondence, verbatim `[sic]`: *"and lets follow up on the constructive note"*. The specific row formulations below are orchestrator / lane walk-level (the 2026-07-28 SUBC/KUBC bracket lane, OWED-1). This subsection sits under `clm-eemap1` (the META catalog) — a **means-tested consolidation** of an exact-but-ontologically-silent algebraic identity, **NOT** a new emergence claim, and it mints **no new claim-id** (the §4.6.2 precedent).

### §4.7.1 — Sweep first: what the corpus ALREADY carries (do NOT re-mint these; this row connects them)

| Existing content | Where it lives | What it already establishes |
|---|---|---|
| **Kron T8 — exact network representability** | [`physics-lineage-map.md`](../physics-lineage-map.md) T8 (§"Gabriel Kron") | *"any linear physical system — rotating machine, **elastic solid**, Maxwell field, Schrödinger wavefunction — is **exactly** representable as an electrical network"*, and numerical analysis later *"reinvented the content anonymously (domain decomposition, **Schur complements**)"*. **This row is an INSTANCE of Kron's theorem, not a new theorem** — and it inherits that entry's own verdict verbatim: *"an exact isomorphism is ontologically silent."* |
| **The scalar weighted-graph-Laplacian Dirichlet energy — already at THEOREM grade** | [`the-sourced-charge-no-go-cascade.md`](../the-sourced-charge-no-go-cascade.md):94 (Lock 3) | `L_w = Bᵀ diag(ε_eff) B` and the Dirichlet energy `φᵀ L_w φ = Σ_edge ε_eff·(Δφ)²`, with the **1-D constant nullspace** on the connected srs graph. That IS the network side of this row's algebra, already canon, already load-bearing |
| **The KUBC-is-an-upper-bound statement** | [`relative-offset-principle.md`](../relative-offset-principle.md):57 | the `#782` `K`-side is *"a **KUBC upper bound** … an upper bound cannot support a floor claim"* — the missing lower side is what the 2026-07-28 lane went after |
| **The sibling method row (.OP/.AC)** | §4.5(b) Impedance & transmission | bias-point-then-linearize; same *methodology-row* class as this one |
| **Op5 multiport $[Y]$; Op1 impedance** | [`operators.md`](../operators.md):45, :41 | $[S] = (I + [Y]/Y_0)^{-1}(I - [Y]/Y_0)$; $Z = \sqrt{\mu/\varepsilon}$ — the two operators this tool reduces onto |

### §4.7.2 — The means-tested rows

| # | Substrate primitive (homogenization object) | Network analog | Means-test verdict |
|---|---|---|---|
| **D** | **KUBC** — kinematic uniform boundary condition: `u = E·x` prescribed on $\partial V$, no traction prescribed anywhere (`research/2026-07-28_subc-kubc-bracket_prereg-FROZEN.md` §1.3) | **Voltage-clamped boundary** — every boundary node held by an ideal voltage source on the affine profile $v = -\mathbf{E}\cdot x$; currents free. In Op5 multiport terms: **drive the ports with voltage sources and read $[Y]$** | **EXACT** (§4.7.3): both are the *Dirichlet partition* of one PSD quadratic form — Kron-class, consistency-class, no chord; static / DC / single-sign-susceptance ONLY; the equilibrium minimizes over kinematically-admissible fields, and clamping the boundary DOFs shrinks the admissible set ⇒ the minimum can only RISE ⇒ **over-stiffens / over-estimates conductance** |
| **E** | **SUBC** — static uniform boundary condition: `t(x) = Σ·n(x)` prescribed on $\partial V$, **no displacement prescribed anywhere** (prereg §1.1) | **Current-fed boundary** — prescribed injected currents on the boundary nodes by ideal current sources; potentials float. In Op5 terms: **drive the ports with current sources and read $[Z] = [Y]^{+}$** | **EXACT**: both are the *Neumann partition* of the same form — Kron-class, consistency-class, no chord; static / DC / single-sign-susceptance ONLY; the equilibrium minimizes complementary energy over statically-admissible flux fields, and prescribing the injection pattern shrinks THAT admissible set ⇒ the minimum rises ⇒ **over-softens / under-estimates conductance** |
| **F** | **The Hill (1963) / Huet (1990) / Hazanov–Huet (1994) two-sided apparent-modulus ordering** `C^SUBC ≤ C* ≤ C^KUBC` (prereg §1.3) | **The Dirichlet / Thomson two-sided bound on effective conductance** $G^{\text{current-fed}} \le G^{*} \le G^{\text{voltage-clamped}}$ — Dirichlet's principle (minimize $\sum_e g_e(\Delta v)^2$ over potentials) bounds above; Thomson's principle (minimize $\sum_e r_e I_e^2$ over KCL-admissible flows) bounds below. Rayleigh's short-cut and cut laws are the two special cases of the same constraint-monotonicity | **EXACT — the SAME theorem, not an analogy — and Kron-class, consistency-class, NO chord; static / DC / single-sign-susceptance ONLY.** Dirichlet's principle *is* minimum potential energy and Thomson's *is* minimum complementary energy, for the scalar field. The prereg states the shared mechanism itself, verbatim: `Both principles are exact statements about the DISCRETE positive-semidefinite quadratic form U(u) = ½ uᵀKu under a Dirichlet vs a Neumann partition; nothing in the argument needs a continuum limit.` Substrate side = block ($3\times3$-per-bond) Laplacian; network side = scalar ($1\times1$) Laplacian. Same algebra, $g_b \to \Phi_b$ |
| **G** | **PBC / periodic homogenization** — the third boundary condition, sitting inside the bracket | **The periodic (Born–von Kármán) network cell** — wrap the cell and read the exact bulk effective conductance of the infinite periodic lattice | **STRUCTURAL PASS, NOT RUN in this lane, and NOT a bound.** Frozen prereg §1.3 verbatim: `A periodic BC would give a third, intermediate estimate — informative but NOT a bound, and therefore not what OWED-1 asks for.` For a genuinely periodic medium the periodic cell returns the exact effective property; for a finite window on a non-periodic composite it is an estimate. **The 2026-07-28 lane ran a finite cluster, not PBC** — so this row has NO validating instance and is landed as structure only |

**The object dictionary** (the substance of the means-test — every load-bearing object maps, not just the headline pair):

| Elasticity / homogenization object | Resistor-network object |
|---|---|
| displacement $u(x)$ (vector field) | node potential $v$ (scalar field) |
| strain $E = \mathrm{sym}\,\nabla u$ | field $-\nabla v$ |
| stress $\Sigma$ | current density $J$ |
| stiffness tensor $C$ (4th-order) | conductance matrix / boundary Schur complement of the Laplacian (**= the Op5 $[Y]$**) |
| strain energy $\tfrac12 E{:}C{:}E$ | the Dirichlet dissipation/storage FUNCTIONAL $\tfrac12 \mathbf{E}\cdot\sigma\cdot\mathbf{E}$ (the Joule rate itself carries no $\tfrac12$ — functional, not power) |
| apparent modulus $C^{app}$ | apparent conductance $G^{app}$ at the driven ports |
| per-bond form $\Phi_b = k_a\hat d\otimes\hat d + k_s(I-\hat d\otimes\hat d)$ | per-edge conductance $g_b$ (the $1\times1$ block) |
| Hill's lemma $\bar\Sigma = \tfrac1V\,\mathrm{sym}\sum_i f_i\otimes(x_i-x_c)$ | the dipole-moment identity $\bar J = \tfrac1V\sum_i I_i (x_i - x_c)$ |
| self-equilibration $\sum_i f_i = 0$ (prereg §1.1; design-time pilot at `L=12`: `\|Σ_i f_i\| = 3.8e-15`) | **Kirchhoff's current law as the solvability condition** — the Fredholm alternative for a singular Laplacian: a floating current-fed network with net-nonzero injection has NO solution |
| null-space projection $Pw = w - \mathrm{mean}(w)$ | **floating-ground gauge fix** — project out the constant potential |
| uncaged reference normalization | the **uniform-conductance** reference network (all $g_b$ equal) |
| uncaged gap $g_0 = K^{unc}_{KUBC}/K^{unc}_{SUBC}$ (measured `1.2419` bulk at `L=16`) | **contact / spreading resistance** of a finitely-probed network — the boundary-layer term that is instrument, not bulk |

### §4.7.3 — ★Where it is EXACT and where it is a DISANALOGY (the KEEP-BOTH disanalogy convention, per the §4.6.2 Row-B MOS precedent)

**EXACT (rows D/E/F):** for the **DC / static, single-sign** problem the two sides are the same object. The substrate operator is a *vector-valued (block) graph Laplacian*; the resistor network is its scalar case. Dirichlet-vs-Neumann partition of one PSD quadratic form; both bounds proved identically ("add a linear constraint to a minimization ⇒ the minimum cannot fall"); the boundary Schur complement is the multiport $[Y]$ (Op5) under voltage drive and $[Y]^{+}$ under current drive. Nothing in either proof needs a continuum limit. **This exactness is Kron's, not AVE's** — and so it is **ontologically silent** (`physics-lineage-map.md` T8, verbatim). **Consistency-class; peer-with-standard-homogenization; NO chord.**

**Three disanalogies, each load-bearing (they are not decoration — every one of them BIT the 2026-07-28 bench):**

1. **★The scalar network has no rotational sector, and that is exactly the mode that had to be disclosed.** The scalar Neumann null space is **1-dimensional** (the constant potential). The vector one is generically **6**-dimensional (3 translations + 3 rigid rotations) — except that on the shipped Born bond model rotations **cost energy**, so the actual null space is the **3 translations only** (prereg §0 walk item 7; result §1 measured `E(rigid rotation, 1e-3) = 1.984e-3 > 0`, `E(uniform translation) = 0.0` exactly). **A network reading would have said "project out the constant and you are done" and would have missed the Born model's absolute-frame rotational stiffness entirely.** The network picture cannot even pose the question.
2. **★The scalar network cannot carry the A1/T2 sector split — and that is precisely where the bench's ordering failed.** A scalar conductivity is rank-2 at worst; there is no analog of a 4th-rank stiffness's decomposition into $K$ / $C'$ / $C_{44}$, no hydrostatic-vs-deviatoric channel split, and therefore no "**which** longitudinal modulus" question. The medium is **CUBIC, not isotropic** (result F2: Zener $A = C_{44}/C' = 1.330402$ SUBC / `1.605316` KUBC), which is why the `M = K + 4G/3` label was **WITHDRAWN** there. Empirically the split is the fault line: the frozen G1 ratio-ordering violations are **`8` of `42` ratio-bearing rows, every one in the `T2` shear companion, `0` of `21` in the `A1` hydrostatic headline sector.** **(2026-07-28 audit repair — an earlier draft inferred "the exact-mapping regime is the A1 bulk channel" from this split; that inference is DELETED as a non-sequitur: the violations are a property of the RATIO construction on a free-surface-floppy uncaged reference — shear `g_0 = 2.1600` vs bulk `1.2419`, an instrument/boundary-layer fact per the #802 result — while the absolute bounds hold 48/48 in BOTH sectors, and the variational argument is mode-agnostic. Whether any sector-scoped statement is warranted is routed to Grant, not asserted here.)** Sector-ownership discipline applies — do NOT cross-wire.
3. **★"Dissipated" vs "stored", and the regime fence that comes with it.** The textbook network statement is about **dissipated** power in resistors; the substrate is Ax3-**lossless-reactive**, so the corresponding form is **stored** reactive energy. That is not a mathematical obstruction *in the static / single-sign case* — a network of one-sign susceptances carries the identical PSD form and identical bounds with $g \to b$. It **IS** an obstruction for a general **AC mixed-reactance (L and C)** network: there $B(\omega)$ is real-symmetric but **not sign-definite** (Foster's-reactance-theorem territory), the quadratic form is indefinite, and the two-sided variational bounds **fail**. **Regime tag, mandatory at every cite of this row: `static / DC / single-sign-susceptance` only. It does NOT carry to the general AC LC network.** Matches the bench's own declared regime (prereg §0: Regime-I cold-linear STATIC, no drive, no time axis).

**Carried exposure (not a disanalogy — evidence the mapping is tight enough to predict the failure mode).** The bounds are on the **ABSOLUTE** apparent modulus / conductance. A **RATIO** of two boundary-conditioned readings is **not** bound-ordered — the bench measured exactly this: `R_KUBC/R_SUBC = g_0^arm / g_0^uncaged`, so the ratio inverts whenever the reference's own boundary-layer gap exceeds the arm's (shear `g_0 = 2.1600` vs bulk `1.2419`), while `absolute_theorem_grade_ordering_holds_everywhere = True` across all `48` walked rows. The network reading inherits this verbatim: *a ratio of two apparent conductances is not itself sandwiched.*

### §4.7.4 — ★What is NOT landed here (flag-don't-fix; the bracket-width corollary is REFUSED)

A "the bracket is WIDE (`0.15081` on `K_eff/K_0`) ⇒ the composite is far from self-averaging at this cell size ⇒ boundary-layer-dominated, the network analog of contact-resistance dominance" corollary was **proposed at walk level and is NOT landed**, because it violates the lane's own frozen anti-seduction fence, verbatim: `a wide bracket is a statement about the INSTRUMENT, not about the medium: the result doc may NOT convert bracket width into physical significance in either direction, and must report the uncaged gap g_0 alongside every width so the reader can see how much of it is finite-size boundary layer`. Converting the width into "the composite is far from self-averaging" is a statement about the **medium** — exactly the move the fence forbids. **What IS landed** is the *instrument* half, which the fence itself asks for: the **uncaged gap `g_0` ↔ contact / spreading resistance** row in the §4.7.2 dictionary, measured on the **uncaged reference** (no cages, hence no medium claim). Routed to Grant / the auditor lane if the width reading is ever wanted; it needs its own bench, not a table row.

**Status of the validating instance, stated plainly (do NOT read the numbers as banked).** The 2026-07-28 lane (`research/2026-07-28_subc-kubc-bracket_prereg-FROZEN.md` + `research/2026-07-28_subc-kubc-bracket_result.md`, **`#802` — MERGED 2026-07-28; both docs are on `main` and cite-able by path**; this parenthetical read *"PR #802, OPEN — cite by path, not yet on `main`"* until the 2026-08-02 marker sweep) reports **BENCH STATUS = VOID AS FROZEN on two criterion-side counts**, with its bracket *computed and shipped in full but NOT BANKED as physics*. What this row rests on is therefore **not** the bracket values but the **instrument validation**, which did pass and is Rule-14-reused corpus: the KUBC re-computation reproduces the merged #782/#796 arms **bit-exactly** (`0.2963682232`, `0.2982369863`, rel `0.00e+00`), G4 convergence, G5 work identity `8.63e-16`, G3 determinism byte-identical. **The exactness claimed in §4.7.3 is algebraic (Kron), not empirical** — it would stand if the bench had never run.

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
| 12 | Cosserat rotation-sector mass-gap $m_\omega \sim 1$ MeV | Transformer cutoff frequency / ferrite Curie threshold | $\checkmark$ structural | [`trampoline-framework.md`](../trampoline-framework.md):192 — `m_\omega^2 = 4 G_c / I_\omega` |
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
| 23 | Dark resonance (near-field reaction) $\Sigma_{\text{near}}$ / $-\dot\Sigma_{\text{near}}$ | Armature-reaction-induced d/q saliency (QED self-energy analogue) → electron $g$-2 anomalous moment | $\checkmark$ **Route B forward $+4.0\%$ parameter-free**; the $g$-2 **50 ppm** closure is **postulate-dependent** (n_q-additivity = 1-point fit, not derivable — FT-b 2026-05-31) | [`q-g19a-petermann-saliency-closure.md`](../../vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md):112 (clm-v2sg8z) + [`dark-back-reaction-taxonomy.md`](../dark-back-reaction-taxonomy.md) |
| 24 | Dark wake (far-field reaction) $\tau^{\text{far}}_{zx}$ | Far-field radiated Maxwell/Cauchy shear stress; $\int \tau\, dA = F$ reaction-momentum trail | $\checkmark$ structural ($\int \tau\, dA = F$ is an EE/Maxwell-stress identity) | [`chiral-thrust-derivation.md`](../../vol4/circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md) (clm-7tynm2) |
| 25 | Proton mass eigenvalue $m_p/m_e$ via $\mathcal{V} = 2$ dual-reactance count | Regenerative LC loop (Black's closed-loop gain $A/(1-\beta A)$); $\mathcal{V} = 2$ = count of node reactance sectors ($X_L + X_C$); mass uniquely selects additive-2 | ⚠ **mass-discriminator PASS** ($\mathcal{V}=2 \to 1836.117\,m_e$ vs $\mathcal{V}=1 \to 1423.96$, $\mathcal{V}=p_c \to 1203.43$; CODATA 1836.153) — count-2 **closed**; per-channel coupling **$k=1$ closed** via Op17 matched-impedance ($\Gamma=0$ at orthogonal Borromean crossing, Axiom-3 manifestation, R2 2026-06-01); residual narrows to the $p_c=8\pi\alpha$-feedback-fraction identification (1-residual Skyrme, NOT zero-parameter) | [`dual-reactance-storage-taxonomy.md`](../dual-reactance-storage-taxonomy.md) + [`2026-06-01_baryon-V2-dual-reactance-closure.md`](../../../../research/2026-06-01_baryon-V2-dual-reactance-closure.md) §2 + [`2026-06-01_baryon-R2-crossing-coupling-result.md`](../../../../research/2026-06-01_baryon-R2-crossing-coupling-result.md) §6 |
| 26 | Casimir force $-\pi^2\hbar c/240d^4$ (parallel plates) | Waveguide/cavity below cutoff ($f_c=c/2d$) = *mechanical high-pass filter*; mode-energy-density differential = inward Maxwell stress $\int\tau\,dA=F$; finite sum to band-edge $f_{\max}=c/(\pi\ell_{node})$ | $\checkmark$ structural (reproduces standard Casimir magnitude + $d^4$ scaling) — but **consistency-class, NOT a discriminator vs QED**: relabeled mechanism, no new observable (2026-06-03 walk-back [`c989f970`](https://github.com/ave-veritas-et-enodatio/AVE-Core/commit/c989f970)) | [`casimir-effective-temperature.md`](../../vol3/condensed-matter/ch11-thermodynamics/casimir-effective-temperature.md) + AVE-Metamaterials Ch.6/8 |
| 27 | srs vacuum-net band structure (scalar top $\pi\sqrt3\,\omega_C=2.781$ MeV at $H$; NO internal gap either channel) | Coined-quantum-walk / TLM **arccos** spectral map $\omega=\omega_{link}\arccos(\mu/3)$ (Op5 scatter+connect + Op6 eigenmode) | $\checkmark$ gate-passed (#604/#607): velocity factor $1/\sqrt3$ to $3\times10^{-9}$; $\lambda_{max}=6.000$ vs direct `build_srs_net`; scalar reduction $2.7\times10^{-15}$; both enantiomorphs identical — all COMPUTED vs independently-derived canonical numbers, and the graph-Laplacian $\omega=\sqrt\lambda$ REJECTED for failing the $1/\sqrt3$ gate (model-selection, not assertion) | [`srs-band-structure.md`](../../vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md) (clm-bnd5rq) |
| 28 | **A1/T2 far-field radiation partition** (bulk-P vs shear-S from a rotating mass quadrupole) | **Seismological P/S energy partition** for an isotropic (Poisson) elastic solid — Aki–Richards moment-tensor radiation: $E_S/E_P=(I_S/I_P)(V_p/V_s)^5=(3/2)(\sqrt3)^5\approx23.4$; the AVE angular factor $\mathcal{A}_{ang}=I_P/I_S=2/3$ is the inverse of the identical integrals | $\checkmark$ **means-test PASS at value level** (exact textbook agreement, external non-AVE anchor — not order-of-magnitude); ★**reads for Q1 Reading A** since the 2026-07-20 revert — [`port-register.md`](../port-register.md):93 verbatim: *"now reads for Reading A: a generic isotropic elastic solid"* **does** radiate its P/bulk channel, exactly the structure #761 found AVE's vacuum has ($K\neq0$ ⇒ radiating P-wave), so no generic-elasticity suppression rescues the framework and *"the pulsar exclusion is LIVE against the framework"*. *(Stale label corrected 2026-08-07; was "sharpens Q1 Reading B … the vacuum's bulk-port suppression cannot come from generic elasticity" — written while Reading B was the RULED-CONDITIONAL standing physics.)* | [q1-pulsar-hardening](../../../../research/2026-07-20_q1-pulsar-hardening.md) §6 (+ §1 the $8\pi/15$ / $4\pi/5$ integrals); [`port-register.md`](../port-register.md) Q1 |
| 29 | **Vessel shell / envelope skirt** (soliton self-organized roll-off layer $S(A(r))$) — 2026-07-21 vessel-state walk | **p-n junction depletion region** (self-organized boundary of opposed tendencies: built-in stress ↔ built-in field, radiation-pressure vs elastic-restoring ↔ diffusion vs drift; squeeze/stretch ↔ forward/reverse bias; yield-knee ↔ breakdown-knee) | **structural PASS** at roles/governing-structure level; value-level (width $\sqrt{V_{bi}-V}$ scaling) OPEN, owned by the parallel-lane boundary-strain/RVE bench — cross-ref, not claimed; consistency-class. KEEP-BOTH vs the §9 $C_j(V)$ component-non-ideality row | §4.6.2 Row A; `saturation-rim-inversion.md` (PR #790, merged 2026-07-21) §"vessel-state skirt" + [`envelope-anatomy.md`](../envelope-anatomy.md); `research/2026-07-21_boundary-strain-amplitude_result.md` |
| 30 | **Saturation wall** ($\Gamma=-1$ / $A\to A_{yield}$, $\sim$1-node; the rim-inversion character-swap) — 2026-07-21 rim-inversion walk (`clm-riminv`, PR #790) | **MOS inversion layer** (thin field-threshold channel where the surface inverts character; field-controlled; screening) | **structural PASS** at roles level (thin field-threshold boundary + character-inversion + screening); **disanalogy flagged** — MOS inversion = conductive channel (carrier-type flip) vs saturation wall = $\lvert\Gamma\rvert=1$ reflective mirror (phase-space-role flip); consistency-class. KEEP-BOTH vs the whole-device Geometric-Triode↔MOSFET row | §4.6.2 Row B; `saturation-rim-inversion.md` (PR #790, merged 2026-07-21); [`appendix-vca-symbols.md`](../appendix-vca-symbols.md) #2 |
| 31 | **Cages at packing fraction $\phi$** ($K_{eff}(\phi)$ / $r_Z(\phi)$; shell-percolation $\phi_{perc}$) — 2026-07-21 RVE aggregation lane (#770/#782) | **Doping density** $N$ (effective-medium doping-density curve; heavy-doping percolation; band-gap narrowing) | **structural PASS** (density→effective-medium→percolation→constitutive-collapse); **value-level LEANS / KUBC-conditional** — RVE retracted "intermediate crash" to "tracks the coated-inclusion parallel bound" ($K_{eff}/K_0\approx0.16$–$0.19$), so "crash ↔ band-gap-narrowing" is a candidate; consistency-class. CONSOLIDATE vol 4 Ch 19 atom-dopant (KEEP-BOTH, distinct density-vs-atom reading) | §4.6.2 Row C; `19_silicon_design_engine.tex` §"Doping as Geometric Perturbation"; `research/2026-07-21_rve-aggregation-bench_result.md` §5 |

| 32 | **Homogenization boundary-condition duality + the two-sided apparent-modulus bracket** — KUBC (`u = E·x` prescribed on $\partial V$) / SUBC (`t = Σ·n` prescribed, no displacement anywhere) / PBC, and the Hill (1963) / Huet (1990) / Hazanov–Huet (1994) ordering `C^SUBC ≤ C* ≤ C^KUBC` — 2026-07-28 SUBC/KUBC bracket lane (OWED-1) | **Resistor-network boundary duality** — KUBC ↔ **voltage-clamped** boundary (ideal voltage sources on an affine profile; read the Op5 multiport $[Y]$); SUBC ↔ **current-fed** boundary (ideal current sources, potentials float; read $[Z]=[Y]^{+}$); the Hill/Huet pair ↔ the **Dirichlet / Thomson** two-sided bound on effective conductance $G^{\text{current-fed}} \le G^{*} \le G^{\text{voltage-clamped}}$ (Rayleigh short-cut / cut = the special cases); PBC ↔ the periodic Born–von Kármán network cell | **EXACT — the SAME theorem, not an analogy** (rows D/E/F): Dirichlet's principle *is* minimum potential energy and Thomson's *is* minimum complementary energy, both being the Dirichlet-vs-Neumann partition of one PSD quadratic form on a graph — substrate = block ($\Phi_b$) Laplacian, network = scalar ($g_b$) Laplacian, `nothing in the argument needs a continuum limit`. Every load-bearing object maps (Hill's lemma ↔ the current-dipole identity; self-equilibration ↔ **KCL as the Fredholm solvability condition**; translation projection ↔ floating-ground gauge fix; uncaged gap $g_0$ ↔ contact/spreading resistance). **But the exactness is KRON's, hence ontologically silent ⇒ CONSISTENCY-CLASS, peer-with-standard-homogenization, NO chord.** ★**Three disanalogies, each of which BIT the bench:** (i) the scalar network has **no rotational sector** — it cannot even pose the Born-model absolute-frame rotational-stiffness question the lane had to disclose (`E(rigid rotation) = 1.984e-3 > 0`); (ii) it **cannot carry the A1/T2 split** (the medium is CUBIC, Zener $A = 1.330402$/`1.605316`; the frozen G1 ratio-ordering violations are `8` of `42`, **all** T2 shear, `0` of `21` A1 hydro) — *(the earlier "exact regime = A1 bulk channel" inference deleted per the 2026-07-28 audit: ratio-construction artifact, not a mapping-scope fact; absolutes hold 48/48 both sectors)*; (iii) dissipated-vs-stored forces a **regime fence: static / DC / single-sign-susceptance ONLY** (a mixed-reactance AC $B(\omega)$ is not sign-definite and both bounds FAIL). ★**Validating instance is NOT banked:** `#802` (**MERGED 2026-07-28**; read *"OPEN"* until the 2026-08-02 marker sweep — merging banks nothing) is **VOID AS FROZEN** on two criterion-side counts; what passed is the instrument validation (bit-exact #782/#796 reproduction, G3/G4/G5). ★**REFUSED (flag-don't-fix):** the "wide bracket ⇒ composite far from self-averaging" corollary — it converts width into a *medium* claim against the lane's own frozen anti-seduction fence | §4.7 (+ §4.5(b) tool row); `research/2026-07-28_subc-kubc-bracket_prereg-FROZEN.md` §0–§5.6 (regime + walk item 7 through the anti-seduction fence) + `research/2026-07-28_subc-kubc-bracket_result.md` (**`#802` — MERGED 2026-07-28**; cite by path); [`physics-lineage-map.md`](../physics-lineage-map.md) T8 (Kron); [`the-sourced-charge-no-go-cascade.md`](../the-sourced-charge-no-go-cascade.md):94 (the scalar $L_w$ Dirichlet energy, already canon); [`relative-offset-principle.md`](../relative-offset-principle.md):57 |

**Validation threshold.** 20+ validated cross-checks across atomic / circuit / cosmology / gauge-boson / topology / saturation / cosmic / detector / elastodynamics / network-homogenization domains — sufficient to establish the META framework as **Class B substrate-mechanism manifestation** (per `consistency-vs-emergence` v1.3 classification rubric Step 8c canonical-source-ceiling-stays-Class-B: the META framework consolidates already-canonical sub-claims into a coherent framing; it does NOT add new substrate-mechanism content beyond canonical axioms; classification stays at Class B and is NOT promoted to Class 2 emergence).

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
- [`trampoline-framework.md`](../trampoline-framework.md) — Cosserat rotation-sector mass-gap (line 192; $\omega_m \sim 1$ MeV)
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
| Temperature coefficient TC$L$ / TC$\mu$ (small for air-core; large near Curie for ferrite) | **Cosserat rotation-sector mass-gap** — below substrate-native Curie temperature, B-modes frozen → TC$\mu \approx 0$; near substrate Curie temperature ($\sim 1$ MeV), B-modes thermally populate → TC$\mu$ grows; ferrite-Curie is the material-specific analog of substrate-Curie at engineering temperatures | [`trampoline-framework.md`](../trampoline-framework.md):192 — `m_\omega^2 = 4 G_c / I_\omega` + §9.3 below + [`delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) |
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
| **Curie temperature ferrite ($T_C$)** | **Cosserat rotation-sector mass-gap $\omega_m \sim 1$ MeV** — substrate-native magnetic-mode thermal-freeze threshold; ferrite-$T_C$ is the material-specific manifestation at lab temperatures | [`trampoline-framework.md`](../trampoline-framework.md):192 — `m_\omega^2 = 4 G_c / I_\omega` + §9.3 below |
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

1. **Every EE datasheet specification is a means-test case for `ave-ee-first-mapping` v1.0.** The means-test corpus at §6 carries the validated cross-checks (20+ and growing — see the §6 tally; including the two dark-back-reaction field-zone rows — dark resonance $\Sigma_{\text{near}}$ and dark wake $\tau^{\text{far}}_{zx}$ — and the proton-mass $\mathcal{V}=2$ dual-reactance-count discriminator); the engineering-non-ideality catalog above adds tens of additional rows (one per datasheet row per component type per substrate axis), each of which is a candidate substrate-physics derivation cross-check. Radical expansion of the means-test surface area.

2. **δ_strain at $T_{CMB}$ is the cosmological instance of substrate TCC.** The same Cosserat-Curie mechanism that produces measurable TCC on a ceramic capacitor in a circuit lab produces the $2.22 \times 10^{-6}$ thermal-running of α at the substrate's cosmic-temperature operating point. One mechanism, many scales.

3. **Engineering datasheet specifications ARE substrate-physics empirical data.** Tens of millions of components characterized over decades by the EE industry constitute a vast empirical dataset of substrate behavior under measurable operating conditions. AVE's substrate-physics derivation is the unified-field-theory backbone that explains the catalog of EE corrections from a fixed set of substrate axioms.

4. **The substrate is one substance characterized across scales.** From cold-lattice ideal ($T \to 0$, $A_0 \to 0$, $\Gamma \to 0$) up through engineering operating regimes (room temperature, finite signal, finite parasitics, imperfect boundary), engineering and substrate-physics describe the same natural substrate. The deviations from cold-lattice that engineering codifies as "corrections" are the substrate as it actually exists in nature, not engineered alterations of it.

### §9.5 — Cross-references

- **δ_strain canonical mechanism leaf:** [`delta-strain-cosmic-tcc.md`](../../vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md) (clm-hp7nlm) — Cosserat-rotation-sector-mass-gap thermal-mode-population ASYM; substrate-mechanism path for the TCC rows above
- **Cosserat couple-stress canonical:** [`gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md):39 ($l_c = \sqrt{\gamma_c/G_{vac}}$) — same primitive that sets transformer leakage-inductance characteristic length AND weak force range
- **Cosserat rotation-sector mass-gap canonical:** [`trampoline-framework.md`](../trampoline-framework.md):192 — `m_\omega^2 = 4 G_c / I_\omega` ($\omega_m = 2$ in natural units, $\sim 1$ MeV) — substrate-native Curie analog
- **SYM α-invariance canonical:** [`alpha-invariance-symmetric-gravity.md`](../../vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) (clm-3zz0f6) — load-bearing for ASYM-induced α-drift mechanism (SYM gives α invariance; the substrate-thermal ASYM is what produces δ_strain)
- **SYM vs ASYM canonical:** [`einstein-field-equation.md`](../../vol3/gravity/ch02-general-relativity/einstein-field-equation.md) (clm-8nkvwy) — the c_EM vs c_shear distinction load-bearing for δ_strain derivation
- **Companion agent-discipline skill:** `~/.claude/skills/ave-ee-first-mapping/SKILL.md` v1.0 — EE-first-mapping discipline that uses this catalog at fire-time
- **Means-test corpus extension target:** §6 above carries the canonical validated cross-check corpus (20+ and growing — see the §6 tally); the §9 component-non-ideality catalog is the candidate expansion surface

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

Field-Oriented Control (Park d/q) is the canonical co-rotating-frame decomposition ([`05_universal_solver_toolchain.tex`](../../../backmatter/05_universal_solver_toolchain.tex):179-195; d-axis = reactive/non-radiating, q-axis = real/radiating). Applied to the electron rotor:

- The **"½ phase-pair commutation" is the SPINOR DOUBLE-COVER** — the Finkelstein-Misner kink / Dirac belt trick (SU(2)→SO(3), 2:1), **NOT** a half-pole-pair machine. Canonical: [`spin-half-paradox.md`](../../vol2/appendices/app-b-paradoxes/spin-half-paradox.md):12-14 (Cosserat microrotation DOF IS the substrate-native spin origin); §4 "SU(2)→SO(3) double cover" + "$(2,3)$ Clifford-torus winding" rows.
- The **pole-pairs are the $(2,3)$ WINDING numbers** — already canonical (toolchain :437 pole-pairs ↔ mode-$\ell$ row; §4 $(2,3)$ Clifford-torus winding row).
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

---

## Semiconductor-register additions — the depleted wall region (2026-08-05, Grant-ratified)

**End-appended for line-pin safety; fold into the §4 table at the next consolidated pass. Skill-body
mirror (`ave-ee-first-mapping` Step-2 table) and the vol2/vol4 secondary-instance mirror-check are
OWED — tracked in the 2026-08-05 docket.** Origin: the echo-delay lane's §0.2 question, walked in
the core session 2026-08-05; Grant corrected the register to SEMICONDUCTOR and ratified.

| Substrate primitive | EE (semiconductor) mapping |
|---|---|
| The per-frequency turning point where the local band edge falls to the drive ($\omega_{max}(S(r)) = \omega$) | **Depletion edge** — the DC-bias-set surface where the medium stops supporting the signal band; bias-created, signal-discovered |
| The choked section between the depletion edge and the physical end (the wall / last cell) | **Depletion region, width $W(\omega)$** — cells whose signal-band support the DC operating point has depleted |
| The reactive coupling across the depleted cells (exact per-cell ABCD product; no propagating transfer, displacement-analog transfer persists) | **Junction capacitance / the junction two-port** |
| The thin-$W$ limit where the far terminal sets the composite reflection (hard, achromatic) | **Reach-through / punch-through** (cf. reach-through APDs); the thin-junction direct-coupling geometry is the Zener/Esaki class; the large-signal fate of the same region is the existing Miller-avalanche row (Schwinger) |

**Mandatory carves when applying these rows:**
1. What is depleted is **signal-band support** (the cells' propagating capacity), NOT charge carriers.
2. The depletion edge is **drive-frequency-indexed**: each $\omega$ has its own $W(\omega)$; at fixed $\omega$ it is a pure DC level set (wall-taxonomy axis discipline).
3. **No space-charge / built-in-field electrostatics ride along** — the mapping is small-signal network topology only.

### Carrier-sector rows (Grant "bank it" 2026-08-05; tags per row)

| Substrate object | EE (semiconductor) mapping | tag |
|---|---|---|
| The matter-free cold vacuum | **Intrinsic (undoped) crystal** | walk-ratified |
| The pair-creation threshold $2m_ec^2 = 1.022$ MeV | **The bandgap $E_g$** | correspondence [T]; the VALUE is imported via $m_e$ (definitional) — the register derives no mass value |
| Pair production | **Generation** (pumping a carrier pair across the gap) | [T] |
| Annihilation $e^+e^-\to2\gamma$ | **Radiative recombination** (carrier falls into the hole; gap energy leaves as photons) | [T] — and historically exact: Dirac's 1930 hole theory IS this picture; the oldest QED ontology was semiconductor physics before semiconductors existed |
| The positron | **The hole** | [T] (Dirac correspondence) |
| The electron soliton (self-localized, lattice-deforming, carries its deformation) | **Self-trapped carrier, polaron class** | WALK-LEVEL, un-audited |
| Why the cold vacuum is empty of pairs | $n_i \propto e^{-E_g/2kT}$ at $T_{CMB}$: $E_g/2kT \sim 10^9$ — doubly-exponentially nil | consistency-class |

> **⚑ FLAG-BREAKDOWN-CLASS — RULED 2026-08-05 (sheet item 7): the split is canonical and the §4 row is updated in place.** The formerly-single row compressed
> Miller-avalanche ↔ Schwinger row compresses TWO device breakdown modes. Spontaneous
> field-induced pair production ($\Gamma \propto e^{-\pi E_S/E}$, no seed carriers) is the
> **ZENER class** (interband field-tunneling); **avalanche** (impact ionization, seed-carrier
> multiplication) maps to **seeded QED cascades** in strong fields. Both rows are real; the
> current single row mis-files the spontaneous mechanism. KEEP-BOTH until ruled.

**Register-span note (consistency obligation, not decoration):** the semiconductor register now
carries FIVE sectors — the Ax4 varactor kernel, the gravitational wall region, vacuum
breakdown (the Miller/Zener rows, see the flag above), the Vol-6 nuclear semiconductor-circuit
chapters, and the CARRIER sector (the rows above). The same words must bind the same circuit
objects in all five. Proof-of-concept derivation candidate routed 2026-08-05: two-band bipartite
k·p dispersion of the gapped lattice → the relativistic massive-carrier form (see the docket).

### The datasheet map (orientation; Grant-ratified frame 2026-08-05)

The five-sector register is operationalized by reading the program's analyses as sections of a
single device datasheet — the characterization of an ideal, intrinsic, parasitic-free crystal
(the parasitic-free clause IS Axiom 3 + crystalline perfection; the model has ideal intended
terminals — the transfer-cost ports — and one noise temperature, the CMB Johnson floor, which are
datasheet items, not parasitics):

| Datasheet section | Corpus object |
|---|---|
| DC operating point / bias network | The gravitational grading (the DC level-set fields of wall-taxonomy) |
| Small-signal analysis | Maxwell / linear-GR wave physics; the certified ringdown circuits |
| Large-signal analysis | Op14 saturation; the walls |
| C–V characteristic | The Ax4 varactor kernel |
| Band structure | The adjudicated dispersion (`srs-band-structure.md`) + sector gaps |
| Depletion / reach-through | The wall-approach region (the semiconductor rows above) |
| Transit-time analysis | The echo-delay laws (`research/2026-08-04_echo-delay-regulated-sum_result.md`) |
| Breakdown modes | Zener class (spontaneous Schwinger) / avalanche class (seeded cascades) — see FLAG-BREAKDOWN-CLASS |
| Absolute maximum ratings | V_snap, V_yield, the two I_max tiers (swing + slew) |
| Generation–recombination | Pair production / annihilation (carrier-sector rows) |

---

## §12 — Transmission-line MODE tier: the shear/bulk carve read as differential/common mode (2026-08-07 GW-formation walk + correspondence audit)
<!-- claim-quality: clm-eemap1 -->

**EOF-APPEND, and the placement is deliberate.** This tier belongs to the §4 stack by *content* (it is a §4.6.2/§4.7.2-pattern means-tested-row tier) but is landed at EOF by *position*, following this leaf's own growth pattern (§9 and §10 were likewise appended after §8). **Reason: a mid-file insert here would shift 59 inbound `translation-circuit.md:NN` cites.** Zero are rotted this way. The §4 table carries a one-token pointer to this tier, added line-count-neutral.

**Attribution (never blended).** Grant agreed the **carve** at walk level, verbatim `[sic]`: *"shear vs. bulk as diff vs common makes perfect sense to me"*, and fired the review, verbatim `[sic]`: *"let's run the audit lane."* The specific row formulations below are **orchestrator / lane walk-level** (the 2026-08-07 GW-formation walk), landed only after the correspondence audit returned per-row verdicts — recorded at `_orchestration/docket-entries/2026-08-07-rulings-r28-r30.md` §AUDIT OUTCOME (merged #921). This subsection sits under `clm-eemap1` (the META catalog) and mints **no new claim-id** (the §4.6.2 / §4.7.2 precedent). **Every row is an EE re-expression of an already-canonical decomposition, channel-subscripted; none is a new mint.**

### §12.1 — Sweep first: the carve is PRIOR ART (do NOT re-mint; these rows re-express it)

| Existing content | Where it lives | What it already establishes |
|---|---|---|
| **The K4 4-port irrep decomposition** — the carve itself | [`port-register.md`](../port-register.md):37 (`[canon]`, `clm-j550uh`/`clm-9kd2t3`) | $V_{\text{4-port}} = A_1 \oplus T_2$ under $T_d$, with $A_1$ = *"common-mode scalar/longitudinal (dilatation, mass)"* and $T_2$ = *"traceless triplet (shear, the photon/GW)"*. **The differential/common-mode language is ALREADY THERE.** The rows below add the transmission-line reading of it, nothing more |
| **The four channels, speeds, gaps** | [`port-register.md`](../port-register.md):48 (ch-2 shear/GW, *"GW are transverse shear modes"*), :49 (ch-3 bulk-longitudinal/dilatation; the FLAG-A *"two distinct physical longitudinal modes, both retained"* split) | which line is which, with its impedance, band edge and radiative-vs-port speed |
| **The seismological P/S sibling row** | §4 row at `:157` + §6 means-test #28 (this leaf) | the SAME $A_1$/$T_2$ carve mapped to the **elastodynamic/seismological** measurement sibling ($E_S/E_P\approx23.4$), means-tested at value level |
| **The Q1 bulk-radiative-port state** | [`port-register.md`](../port-register.md):93 (*"the pulsar exclusion is LIVE against the framework"*) | the standing physics on whether the common-mode line carries a far-field radiative port — **Reading-A-live since 2026-07-20** |

> **★KEEP-BOTH, stated explicitly (per the §4.6.2 Row-B / §4.7.3 disanalogy convention).** This subsection **does not redefine, supersede, or absorb** the seismological row at `:157` / §6 #28. That row maps the $A_1$/$T_2$ carve to the **elastic-medium sibling discipline** and is a **value-level** means-test (the Aki–Richards P/S energy partition, external non-AVE anchor). These rows map the same carve to the **two-conductor transmission-line mode basis** and are **structural/role-level**. Two lenses on one canonical decomposition; both preserved, neither is the other's correction. Where they touch (the far-field partition) the seismological row remains the value-level authority.

### §12.2 — The means-tested rows (G1–G6; every row channel-subscripted)

**Regime / sector header, mandatory at every cite of these rows:** deeply-linear far field (Regime I, $V_{GW}/V_{snap}\sim10^{-28}$), **cold-reactive** phase-state (Ax3-lossless-reactive; far-field radiation is the Ax3-legal port, not a bulk resistor). Channel subscripts per the three-impedance law — **ch-1** EM-transverse ($T_2$, $Z_{EM}\equiv Z_0$), **ch-2** mechanical shear/GW ($T_2$, $Z_{shear}=\rho c_{shear}$), **ch-3** bulk-longitudinal/dilatation ($A_1$, $Z_{bulk}$), **ch-4** Cosserat micro-rotation (couple-stress, gapped).

| # | Substrate primitive (channel-subscripted) | EE transmission-line analog | Means-test verdict + class | Receipts (two-method) |
|---|---|---|---|---|
| **G1** | **The source: a compact binary as a two-line driver.** The rotating two-lump mass distribution drives **ch-2 AND ch-3 simultaneously** at quadrupole order; the source moment is the rotating mass second moment, whose traceless part rotates at $2\Omega$ | **A mechanically-commutated polyphase source** — the rotor *position* is the commutator, so the electrical drive frequency is $2\times$ the mechanical rate, and **one machine feeds two lines at once** (a differential line and a common-mode line), not one line with a fixed split | **STRUCTURAL PASS at the source-side role level. Consistency-class; walk-wording; mints nothing.** The load-bearing content is the **two-couplings** reading: the source has an independent coupling into each line, NOT one geometry-locked ratio. **The $2\Omega$ kinematics is standard rotating-quadrupole content `[import]`, not AVE-derived.** ★**NOUN COLLISION, distinguished exactly as G4 distinguishes "balanced bridge" — and it is IN THIS LEAF.** §10.4 already spends "commutation" on a different object: *"the electron is a self-commutating 3-phase machine"* (`:832`), where *"the rotor supplies its own commutation; no external commutator"* (`:838`). **G1's binary is the OPPOSITE case: an EXTERNALLY commutated source** — the orbital geometry is the commutator, and there is no self-drive. Same word, inverted mechanism, different sector. **Do not read G1 as an instance of §10.4 or vice versa.** ★**Drive-scope rider: §12.3** — this row asserts *simultaneous* ch-2/ch-3 drive, and the rider that scopes what "drive" may be claimed rides one hop away, exactly as it does from G3. | `master-equation.md`:20 `[canon]` — mass = the $A_1$ dilatation, *"trapped acoustic compression energy"*; `research/2026-07-20_mechanical-commonmode-derivation_result.md`:52 — the source drives the dilatation channel at quadrupole order *"with no conservation law left to kill it"*; same doc `:79` — the traceless part *"rotates at"* $2\Omega$; the sector fence this row must not cross, same doc `:28`: *"A1 owns compression/mass/dilatation; T2 owns shear/GW/char"*ge-winding; the trace/traceless projection split itself is already a def-node — [`vocabulary-register.md`](../vocabulary-register.md):1054 `def-satshr` (*"a definitional trace/traceless SPLIT of the mass second-moment"*), so G1 mints no split of its own 🔴 **[DEMOTED 2026-08-11 — R40-B1; note at EOF]** |
| **G2** | **ch-2 (the $T_2$ mechanical shear line) carries the observed GW.** Gapless acoustic, $c_{shear}=c$, $Z_{shear}=\rho\,c_{shear}$ | **The DIFFERENTIAL mode** of a two-conductor line — the odd/traceless part; the mode a balanced line is built to carry and a common-mode choke rejects | **PRIOR ART, canon-consistent — NOT a mint.** [`port-register.md`](../port-register.md):37 already names $T_2$ the *"traceless triplet (shear, the photon/GW)"*; this row supplies the transmission-line word for it. **Consistency-class.** **KEEP-BOTH** vs the `:157` / §6 #28 seismological-S row (elastic-sibling, value-level) — see the §12.1 box **(a) analytic irrep derivation** — [`k4-port-irrep-decomposition.md`](../../vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md):11: *"The K4 4-port amplitude space decomposes under the tetrahedral group"* $T_d$ as $V_{\text{4-port}} = A_1 \oplus T_2$. **(b) INDEPENDENT engine eigen-decomposition** — `src/ave/solvers/node_scattering_multiplicity.py`:83, the orthogonal complement is *"the -1 eigenspace of dimension n-1 (the DIFFERENTIAL modes)"*. Channel row: [`port-register.md`](../port-register.md):48 (*"GW are transverse shear modes"*, *"gapless acoustic; edge"*). **★Two-method is (a) vs (b) — a group-theory derivation and a separately-run numerical eigen-decomposition, different files and different kinds of evidence.** *(Correction 2026-08-07: an earlier draft labelled `port-register.md`:37 + `:48` "two-method". Those are two lines of ONE file — one source read twice, not two methods. Withdrawn; it must not enter this catalog as a receipt precedent.)* |
| **G3** | **ch-3 (the $A_1$ bulk-longitudinal / dilatation line) is the compression line.** Gapless; FLAG-A two-speed split — PORT/impedance $\sqrt2\,c$ vs RADIATIVE far-field $\sqrt{10/3}\,c$ | **The COMMON mode** of the same two-conductor line — the even/scalar part referenced to ground; the mode a common-mode choke *does* see. ★**MODE IDENTITY ONLY — this row asserts nothing about what drives it** | **PRIOR ART, canon-consistent — NOT a mint.** [`port-register.md`](../port-register.md):37 already names $A_1$ the *"common-mode scalar/longitudinal (dilatation, mass)"*. **Consistency-class.** ★**The walk's "radial-AC-driven" drive restriction is STRUCK; the drive question is OPEN and adversarial to a standing negative — do NOT cite this row as licensing a drive claim in either direction. ★**TWO riders ride this row, both in §12.3** — the second is **FLAG-W, the line's unresolved TERMINATION:** `research/2026-08-03_coldq-polar-family_result.md`:170 asks *"At the saturation radius, does the vacuum's compression line vent, or does it dead-end?"* and records *"Three canonical leaves, two opposite answers, no repair made"*, **ROUTED TO GRANT, UNRESOLVED**. A named line with an open termination carries its flag** **(a) analytic irrep derivation** — [`k4-port-irrep-decomposition.md`](../../vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md):11 (*"The K4 4-port amplitude space decomposes under the tetrahedral group"*). **(b) INDEPENDENT engine eigen-decomposition** — `src/ave/solvers/node_scattering_multiplicity.py`:81, the all-ones port-sum vector is the single *"+1 eigenvector (the COMMON MODE = symmetric breathing channel"*; corroborated at `research/2026-06-20_node-2domain-nport.md`:61 (shear on a *"separate, differential/deviatoric axis"*) and `:63` (*"from the common-mode dilatation"*). Channel row: [`port-register.md`](../port-register.md):49 (*"two distinct physical longitudinal modes, both retained"*). **★Two-method is (a) vs (b)** — derivation vs separately-run numerics. *(Same 2026-08-07 correction as G2: the old "`:37` + `:49`" pairing was one file read twice and is withdrawn.)* ★**Drive-side state, both riders: §12.3.** 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |
| **G4** | **LIGO reads ch-2.** The canon object is an **impedance antenna**: the Fabry–Perot arms accumulate the GW-induced *impedance* modulation, channel-scoped to $\delta Z_{shear}=Z_{shear}\cdot h$ | **A DIFFERENTIAL PICKUP on the ch-2 line** (the added EE lens). It senses the channel-2 differential mechanical mode and reads out on the **ch-1 EM port** | **STRUCTURAL PASS at the pickup-role level; KEEP-BOTH — the canon noun "impedance antenna" is RETAINED, "differential pickup" is an added lens, not a replacement. Consistency-class.** ★**OPEN, must NOT be asserted derived: the mechanical(ch-2) → EM(ch-1) TRANSDUCER LEG.** Canon states the readout, not the transduction. ★**"Balanced bridge" is deliberately NOT used** — it collides with the canonical Mg **6-phase balanced Wheatstone bridge** | [`gw-detection-antenna.md`](../../vol3/gravity/ch08-gravitational-waves/gw-detection-antenna.md):13 (*"A gravitational wave detector is an impedance antenna"*) + [`gw-impedance-perturbation.md`](../../vol3/gravity/ch08-gravitational-waves/gw-impedance-perturbation.md):18 (the 2026-06-11 channel correction; *"The LIGO free-space perturbation is unaffected"*). Collision site: [`ee-equivalent.md`](../../vol6/period-3/magnesium/ee-equivalent.md):10 (*"6-phase balanced Wheatstone bridge"*). ★**The row's OWN FENCE, cited not assumed:** the ch-2→ch-1 hop crosses impedance DOMAINS, and [`device-circuit-models.md`](../../vol9/ch3-pin-port-configuration/device-circuit-models.md):145 forbids collapsing them — *"Mixed impedance DOMAINS (units discipline — do NOT collapse to one unit)"*. The corpus's transducer for that crossing is an **ideal transformer**, `research/2026-06-20_node-2domain-nport.md`:200 (*"the transducer is an"* **ideal TRANSFORMER**) — explicitly *"NOT a gyrator"* (`:201`), and it carries an α-leak (`:204`, *"two factors, kept SEPARATE so the α-leak is VISIBLE"*). **That a transducer object exists in canon does NOT make G4's transduction leg derived** — it names what would have to be derived. Readout receipts: [`gw-detection-antenna.md`](../../vol3/gravity/ch08-gravitational-waves/gw-detection-antenna.md):31 (*"resolved via homodyne readout"*) + [`fabry-perot-phase-shift.md`](../../vol3/gravity/ch08-gravitational-waves/fabry-perot-phase-shift.md):15 (the accumulated-phase form) |
| **G5** | **Pulsar timing ($\dot P_b$) is a TRANSMITTER-side, channel-agnostic total-power audit.** It measures the energy-loss rate *at the binary*, summed over every channel the source radiates into | **A WATTMETER in series at the transmitter output** — as opposed to a receiver at the far end. It reads TOTAL delivered power and **cannot resolve which line carried it**; downstream mode conversion never reaches its reading | **STRUCTURAL PASS — this is exactly the argument the derivation makes. Consistency-class.** ★**CORRECTION carried (do not restate the walk's parenthetical):** *"no bulk-channel receiver exists"* is **CONTRADICTED**. The LIGO/Virgo network **polarization decomposition IS a receiver-side scalar-channel measurement** — pure-scalar excluded at $\log_{10}B=+23.09\pm0.08$ (EM-sky-fixed), with the *mixed admixture* only weakly bounded. What does not yet exist is a **DEDICATED** bulk-channel antenna. ★★**WHY THE WATTMETER LENS MATTERS — a LIVE contradiction, not a settled reading.** [`port-register.md`](../port-register.md):127 records that *"the Hulse-Taylor $\dot P_b$ step-3 attributes the radiated power to the"* **bulk/longitudinal** channel *"while the KB canon assigns GW to the"* **transverse shear** channel — *"a bulk+shear double-count pulsar timing forbids"*, **NOT FIXED, resolving only with the Q1 ruling.** A total-power meter cannot separate the two, which is exactly why the channel attribution is still open. **Do NOT read G5 as closure over that flag** | `research/2026-07-20_mechanical-commonmode-derivation_result.md`:89 — *"it counts every channel the source radiates into, regardless of downstream conversion"*; the LIVE contradiction: [`port-register.md`](../port-register.md):127 (*"a bulk+shear double-count pulsar timing forbids"*) + [`port-register.md`](../port-register.md):87 (the Q1 row, *"the pulsar exclusion is LIVE against the framework"*) + [`port-register.md`](../port-register.md):35 (*"pulsar timing already polices any bulk"* radiative port); receiver-side: `research/2026-07-20_scalar-gw-bulk-channel_derivation.md`:132 (*"we find overwhelming evidence in favor of pure tensor polarization modes"*) + `:141` (*"admixture is in tension but not decisively resolved by GW170817's network"*); polarization-sense read-guard: [`vocabulary-register.md`](../vocabulary-register.md):1060 (*"the LIGO scalar/breathing polarization test = the compression/trace channel"*) |
| **G6** | **The two-picture reconciliation — one wave, two descriptions.** Picture 1 (elastodynamic): the GW **IS** a ch-2 transverse shear **displacement** wave — the first-order carrier. Picture 2 (trampoline / gradient-index): what the instrument port reads is an **impedance modulation** $\delta Z_{shear}=Z_{shear}\cdot h$ | **Carrier vs readout on one line** — the displacement is the signal on the ch-2 line; the impedance modulation is the **detector's transfer function applied to it**, not a second wave. Walk-wording, verbatim: *"echo-sector shear displacement = the first-order carrier"* / trampoline-sector *"impedance modulation = what the EM port reads of it"* | ★**RE-GRADED 2026-08-07: PRIOR-ART-EXISTS, not a new de-confliction.** Canon already writes the carrier and the readout **in one leaf**: [`gw-impedance-perturbation.md`](../../vol3/gravity/ch08-gravitational-waves/gw-impedance-perturbation.md):10 states the antenna reads *"the GW-induced impedance modulation"* and `:18` states *"A gravitational wave is a"* **transverse shear wave**. The two-picture reconciliation is therefore **already canon-resident**; this row supplies the transmission-line word for it and nothing more. *(Was: "STRUCTURAL PASS as a de-confliction" — an over-grade, corrected; the de-confliction value stands, the novelty does not.)* **Consistency-class.** ★**The leg BETWEEN the two pictures — the ch-2 mechanical → ch-1 EM transduction — is OPEN in canon and is NOT asserted derived here.** This row licenses only *"do not count them twice"*; it licenses no transduction magnitude | [`port-register.md`](../port-register.md):48 (the ch-2 carrier, *"gapless acoustic; edge"*) + [`gw-impedance-perturbation.md`](../../vol3/gravity/ch08-gravitational-waves/gw-impedance-perturbation.md):18 (the readout, channel-corrected: *"The LIGO free-space perturbation is unaffected"*); **one site per text family, so the row is not read off a single leaf** — displacement/carrier family: [`einstein-field-equation.md`](../../vol3/gravity/ch02-general-relativity/einstein-field-equation.md):82 (orbiting masses *"act as macroscopic impellers driving transverse shear waves through the electro-mechanical substrate"*) + `:84` (*"gravitational waves are low-frequency macroscopic inductive strain-waves propagating through the structured LC network"*); gradient-index/readout family: same leaf `:76` (*"This creates an inductive deficit in the adjacent vacuum"*) + §6 row 19 (GR metric ↔ gradient-index line impedance). Walk source: `_orchestration/docket-entries/2026-08-07-rulings-r28-r30.md`:19 (*"echo-sector shear displacement = the first-order carrier"*) |

### §12.3 — ★The G3 DRIVE-SIDE RIDER (rides with every cite of G3; the drive question is OPEN and ADVERSARIAL to a standing negative)

**The walk's "the bulk channel is the COMMON-MODE compression line (radial-AC-driven — the lumps' separation oscillating)" carried a DRIVE RESTRICTION. That restriction is STRUCK** (audit verdict 2, `_orchestration/docket-entries/2026-08-07-rulings-r28-r30.md`:55 — *"drive restriction is STRUCK from the walk output"*): restricting the common-mode drive to radial-AC would **reconstruct a closed path**. The corpus already names that exact inference and rules it FALSE.

**The incumbent, quoted verbatim and not paraphrased** — #761 §2, `research/2026-07-20_mechanical-commonmode-derivation_result.md`:79:

> Kept for completeness (the last source-side escape). The A1 channel is the
> scalar/breathing sector; the mass second moment `M_ij` has a trace `Σ M_a r_a²`
> that, **for a circular binary, is constant.** Tempting: "the A1 sees only the
> constant trace ⇒ no radiation." **FALSE.** A scalar/longitudinal field radiates at
> quadrupole order via the **traceless** second moment of the source (standard
> acoustic multipole radiation — the same structure that gives every earthquake its
> P-arrival). With `mass = A1-dilatation`, the scalar source's second moment IS
> `M_ij`, whose traceless part **rotates at `2Ω`** — nonzero. … **The
> tracelessness rescue is dead**

**What survives from the walk, and what does NOT.** What survives is the **anchor dissolution**: the geometry-locked flux RATIO premise dissolves at mechanism level, because the source has **two independent couplings** (G1), not one ratio fixed by geometry — and the corpus supports one-field-two-modes independently (`research/2026-07-20_mechanical-commonmode-derivation_result.md`:46 — the dilatation is the *"longitudinal polarization of the vector displacement field"* and *"NOT a separate scalar DOF; it is a projection of the same 3-vector"* $u$, with `:52` computing the coupling separately). **What does NOT survive is any inference from that dissolution to bulk silence.** Dissolving the anchor changes nothing about whether the common-mode line radiates: the §1.2 / §2 findings **stand** until they are re-derived lattice-natively.

**Why the question is nevertheless OPEN (and this row is adversarial to the standing negative).** The load-bearing step of the incumbent is an **IMPORTED continuum result** — its own words, *"standard acoustic multipole radiation"*. The legitimate challenge is therefore a **lattice-native re-derivation**, which is exactly what the running overlap-integral lane is chartered to do (`_orchestration/2026-08-07_overlap-integral-brief.md`, which carries this same verbatim block as the incumbent it must engage rather than route around). **Both outcomes are live and pre-declared:** agreement with the continuum ⇒ the exclusion stands *on the lattice's own authority*; disagreement ⇒ the negative was an import artifact and the lane must name the exact divergence step. **Until that lane returns, cite G3 for the MODE IDENTITY only.** The standing physics on the drive/port side remains [`port-register.md`](../port-register.md):93 — Q1 Reading-A-live, *"the pulsar exclusion is LIVE against the framework"*.

### §12.3(b) — ★FLAG-W: the compression line's TERMINATION is unresolved in canon (a SECOND rider on G3, independent of the drive question)

**A named transmission line carries its termination flag.** G3 names ch-3 "the compression line". Canon does not currently agree on what that line is terminated INTO at the saturation radius. The question, verbatim from `research/2026-08-03_coldq-polar-family_result.md`:170:

> **★ `FLAG-W` — routed to Grant.** *At the saturation radius, does the vacuum's compression line vent, or does it dead-end?* Three canonical leaves, two opposite answers, no repair made. **This is the highest-value item this lane produced and it needs a physical ruling, not a documentation edit.**

The same lane records the split concretely (`:19`): canon carries *"two opposite bulk-modulus signs at the same"* `r_sat` wall — one leaf has the bulk line **vent** ($c_{bulk}\to0$, $\Gamma_{bulk}=-1$), another has it **jam** (*"the modulus goes rigid"*), and a third flags conflating them as a **firewall violation**. *"Neither leaf is repaired."* **UNRESOLVED, ROUTED TO GRANT — not adjudicated here and not adjudicable by a correspondence row.**

**Consequence for citing G3 (independent of the §12.3 drive rider — these are two different open questions and neither implies the other).** The mode-identity content of G3 (ch-3 = the common mode) is **termination-independent** and stands. Anything **termination-dependent** — reflection at the wall, standing-wave/cavity structure on the compression line, whether the line drains or stores at $r_{sat}$, $Q$ of that line — is **NOT licensed by G3** while FLAG-W is open.

**★This is also live for the R30 bench candidate.** A "compression-line antenna" is a **receiver**, and a receiver's coupling is the reciprocal of the source pickup — so its design depends on the very termination FLAG-W leaves open. **The bench candidate inherits this flag; it cannot be specified past it.** Recorded here so the R30 requirements pass does not have to rediscover it.

### §12.4 — ★What is NOT landed here (flag-don't-fix, per the §4.6.4.1 / §4.7.4 precedent)

- **The "dark wake" row is DROPPED — it was a CONFLICT, not an omission.** The walk called the dark wake *"the reactive near-field trail of a moving biased patch"*; canon says the opposite. [`dark-back-reaction-taxonomy.md`](../dark-back-reaction-taxonomy.md):23 makes the dark wake the **FAR-field radiated shear stress** — *"the real-space longitudinal-shear trail behind a"* moving soliton — while the **near-field reactive** species is the dark **RESONANCE** ([`dark-back-reaction-taxonomy.md`](../dark-back-reaction-taxonomy.md):29, *"Species 2 — dark resonance"*, whose body at `:31` reads *"near-field reactive self-energy"*). The walk inverted the field-zone tag that the taxonomy exists to fix. Separately, the object is **EM-gradient-sourced** and therefore **out-of-set** for GW formation. Audit verdict 3, `_orchestration/docket-entries/2026-08-07-rulings-r28-r30.md`:68 (*"Row 4 (dark wake) is DROPPED"*). **Not deferred — refused.**
- **"Balanced bridge" as a LIGO descriptor is REFUSED** (audit verdict 5): the corpus already spends "balanced bridge" on the Mg octahedral topology, and a second, unrelated referent for the same EE noun in the same catalog is a collision, not a mapping.
- **No transduction claim.** Neither G4 nor G6 asserts a derived mechanical→EM transducer leg; the audit is explicit that the leg *"is OPEN in canon and must not be asserted derived"* (`…2026-08-07-rulings-r28-r30.md`:80).
- **No drive claim on the common-mode line, in either direction** — §12.3. This subsection does not soften, and does not re-open, the Q1 revert.
- **No §6 catalog row minted for this tier.** The §4.6.2 / §4.7.2 precedent mirrors its rows into the §6 means-test catalog once a *validating instance* exists. These rows are role-level re-expressions of an existing decomposition with no new numeric receipt of their own, and the one lane that could supply one (the overlap integral) has not returned. **Routed, not asserted.**
- **The R30 bench candidate is NOT landed as a row.** A dedicated bulk-channel receiver is a registered *bench candidate*, not a correspondence; it belongs to the bench-documentation pattern, not this catalog. 🔴 **[DEMOTED 2026-08-11 — R40-B1; dated demotion note at the end of this file]**

---

### 🔴 Dated demotion note — 2026-08-11 (R40 demotion sweep, batch 1)

**Class: DIES-WITH-THE-PHANTOM.** Status change only — the claim text is **preserved
verbatim** (honesty-lag pattern, Rule 12) and stamped in place; it is **no longer live
canon**. Nothing is deleted.

**Demoted in this file:**

- **`:157`** — *"A1/T2 far-field radiation partition (bulk-dilatation P vs shear-transverse S from a rotating mass quadrupole) — ⚠ cross-discipline"*
  Stamped in place at `:157`.
  **Why it dies (audited row rationale, verbatim):** Prereg-named seismological-partition row: no native P/S partition exists under the carve (provenance case (d) — it had to be imported from rock physics); the Aki–Richards value stays true of rock, the substrate mapping is void. Covers the duplicate §6 means-test #28 at :534 (E_S/E_P≈23.4, "reads for Q1 Reading A") and the §12.1 pointer :947.
  **Also covered by this demotion** (named in the audited row; not separately stamped): `:534`, `:947`.
- **`:958`** — *"The rotating two-lump mass distribution drives ch-2 AND ch-3 simultaneously at quadrupole order"*
  Stamped in place at `:958`.
  **Why it dies (audited row rationale, verbatim):** G1's ch-3 half requires a drivable propagating compression line; under the carve the trace moment exists (accounting) but there is no line to deliver into — the ch-2 (shear) half and the polyphase-source lens survive.
- **`:974`** — *"A scalar/longitudinal field radiates at quadrupole order via the traceless second moment of the source (standard acoustic multipole radiation — the same structure that gives every earthquake its P-arrival)"*
  **NOT stamped in body — R39 BYTE-FENCE ROUTED:** the site is inside the verbatim #761 block-quotation at :971-979 ("The incumbent, quoted verbatim and not paraphrased", :969) — quotation class, R39.
  Preserved-span bytes are untouched; this ledger entry is the note.
  **Why it dies (audited row rationale, verbatim):** The §12.3 incumbent is an imported P-Green-function radiation claim — void when there is no P branch; its voiding is carve content. The rider's routed lattice-native re-derivation lane (:983) survives as routing: the carve is the pre-declared "negative was an import artifact" arm.
  **Scope carve (review fix 2026-08-11).** `:983` is **NOT** demoted. The audited rationale carves it
  verbatim: *"The rider's routed lattice-native re-derivation lane (:983) survives as routing: the carve
  is the pre-declared 'negative was an import artifact' arm."*
- **`:1004`** — *"A dedicated bulk-channel receiver is a registered bench candidate, not a correspondence"*
  Stamped in place at `:1004`.
  **Why it dies (audited row rationale, verbatim):** A compression-line antenna (also :995) is a receiver for a far-field bulk wave — nothing to receive under the carve; the candidate's design premise is the phantom (its FLAG-W inheritance dissolves with it).
  **Also covered by this demotion** (named in the audited row; not separately stamped): `:995`.

**The arc, complete — the framing R40 rules every demotion note carries:**

1. **The kill fired** (#930) — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the #261 K = 2G import** (G-RECON, unchallenged): the compressible
   far-field branch was minted by a GR-imported elastic modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the #935 flat-direction finding: the written
   action conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the RATIFIED bound-sector law — Axiom 5, Substrate DC Bias**
   (BC-SRC clauses **S** / **G** / **Q**), ratified per `_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md`, as reconciled by `_orchestration/docket-entries/2026-08-10-ruling-r44-r43-reconciliation.md` (R44 — the
   full-scope R43 record is FINAL and authoritative; the partial
   `_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md` is SUPERSEDED and is **not**
   the resolution). Under the ratified law the A1 / bulk slot is a **bound response** — mechanism
   gloss **back-reaction** — with no independent propagating branch, no port, and zero longitudinal
   characteristic speed. A bulk *wave speed*, a bulk *radiative port*, a bulk *band-branch* and a
   bulk *transit clock* therefore have **no referent**.

**Standing named-open debt (the honest rider).** The ratified axiom does **not** discharge
everything: **THE BIAS PROPAGATION THEOREM** is Axiom 5's standing named-open entry — clause G's
elliptic law is the *static abstraction* of underived finite-speed bias dynamics (`_orchestration/2026-08-10_bias-propagation-brief.md`). Where a
demoted claim's replacement depends on finite-speed bias dynamics, the resolution is the ratified
axiom **with that debt open**, not a closed replacement.

**Records.** R40 ruling `_orchestration/docket-entries/2026-08-10-rulings-r40-r42.md` · verified worklist `research/drivers/r40_sweep_worklist_verified.json` · scope verification `_orchestration/2026-08-10_r40-sweep-scope-verification.md` ·
batch-1 record `_orchestration/2026-08-11_r40-sweep-batch1.md` · vocabulary R50 `_orchestration/docket-entries/2026-08-10-ruling-r50-vocab.md` (canonical: the displacement pattern u₀ around a
deposit is **the bound response**, mechanism gloss **back-reaction**; ε₁₁ is **the bias**;
"dress", "grade"-as-canonical-noun and "halo"-for-the-physics are retired; and the owed theorem is
renamed **THE BIAS PROPAGATION THEOREM**) · vocabulary **R49(b)** `_orchestration/docket-entries/2026-08-10-rulings-r48-r49.md` (*"retardation"
is RETIRED from this role. The canonical term is **propagation delay / finite propagation speed*** —
the retardation retirement is R49(b)'s, NOT R50's; corrected 2026-08-11 at review).

---

## R40 batch-2a — NEEDS-RE-DERIVATION status note (2026-08-11)

**Class:** status demotion under **R40**. This note mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`,
**moves no solidity number**, adjudicates no channel and opens no fork. Every byte of each demoted
claim is preserved; the stamped line gains a status marker only (honesty-lag pattern, Rule 12).

**The arc, in four clauses (R40's header form; clause 4 points at the LANDED artifact, not at a
ruling record).**

1. **The kill fired** — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the imported `K = 2G` elastic modulus** — the compressible far-field
   branch was minted by a GR-imported modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the flat-direction finding: the written action
   conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the LANDED ratified bound-sector law — Axiom 5, Substrate DC Bias**, clauses
   **S** (deposit), **G** (bias coupling / bridge) and **Q** (quiescence), canonical at
   [`eq_axiom_5.tex`](../../../common_equations/eq_axiom_5.tex) with its register entry in
   [`axiom-register.md`](../../common/axiom-register.md) (§ *Axiom 5 — Substrate DC Bias*). Under
   clause **G** the A1 / bulk slot is a **bound response** — $\mathbf{u}_0 =
   -\mathcal{A}_g\nabla\varepsilon_{11}$, mechanism gloss **back-reaction** — with **no independent
   propagating branch, no port and zero longitudinal characteristic speed**. A bulk *wave speed*, a
   bulk *radiative port*, a bulk *band-branch* and a bulk *transit clock* therefore have **no
   referent**, and each row below owes its re-derivation on that footing.
   $\mathcal{A}_g$ (the **bias-coupling area**) is an `UNVALUED-RATIFIED-CONSTANT` per **R48**
   ([`interlock-register.md`](../../common/interlock-register.md), § *𝒜_g — the bias-coupling
   area*): it is **not valued here or anywhere**, and **the calibration count stays 3**.

**Standing named-open debt — the honesty rider.** The ratified axiom does **not** discharge
everything. **THE BIAS PROPAGATION THEOREM is Axiom 5's standing named-open debt**, stated by the
axiom's own phase-structure paragraph, clause **(c1)**: clause G's elliptic law is the *static
abstraction of underived finite-speed bias dynamics*, and the $(u,\pi)$ no-signalling theorem does
**not** cover the bias read — the bias's finite propagation speed is *owed, not held*. Every row
tagged **⚑ BIAS-DEBT** below re-derives against the ratified axiom **with that debt standing**, never
against a closed replacement.

**Vocabulary.** Canonical nouns authored here: **the bound response** ($\mathbf{u}_0$), **the bias**
($\varepsilon_{11}$), the **DC operating point / quiescent point (Q-point)**; **back-reaction** is
the mechanism gloss. *"dress"*, *"grade"* as $\varepsilon_{11}$'s canonical noun, and *"halo"* for
the physics (the physics noun is the **near-field store / added-mass**) are RETIRED by **R50**;
*"retardation"* is retired by **R49(b)** in favour of **propagation delay / finite propagation
speed**. Corpus text quoted below is reproduced from the banked audit and is
**content-verified at HEAD (markup-reduced, not byte-identical)**; it is never reworded.

**Rows carried in this file.**

- **`:326`** — stamped at `:326`. *(family: band-survey P-branch eigenvalue)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  translational $v^2 = G/\rho$ (×4, the photon) and $10G/(3\rho)$ (×2, P-wave)
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Row D's translational eigenstructure lists the ×2 P-branch — the K-import's spectrum; the band survey re-derives under the constraint (branch removed, not slowed); the carrier-sector (ch-4) k·p content and the reported disanalogy are untouched.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

- **`:960`** — stamped at `:960`. *(family: ch-3 compression line)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  ch-3 (the $A_1$ bulk-longitudinal / dilatation line) is the compression line. Gapless; FLAG-A two-speed split — PORT/impedance $\sqrt2\,c$ vs RADIATIVE far-field $\sqrt{10/3}\,c$
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  G3's MODE IDENTITY (A1 = common-mode projection, irrep algebra) survives as a projection of the bound response; "line/gapless" + the radiative speed consume the phantom. Covers :948 (Q1 Reading-A-live pointer — ledger of the imported reading), :954 header, and the §12.3(b) FLAG-W rider :987-:991 (vent-vs-dead-end dissolves: no propagating line to terminate; wall receipts survive relativized, provenance case (c)).
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

