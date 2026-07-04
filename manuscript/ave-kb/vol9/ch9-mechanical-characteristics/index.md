[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.9 Mechanical Characteristics

Chapter 9 of the Vol 9 datasheet documents the natural vacuum substrate as a Cosserat micropolar continuum (Axiom 1: 6 DOF per K4 node = 3 translational $\to$ $\mathbf{E}$ + 3 microrotational $\to$ $\mathbf{B}$; intrinsic spin originates from the Cosserat microrotational DOF). Spec entries: shear modulus $G_{vac}$, bulk modulus $K_{vac} = 2 G_{vac}$, vacuum Poisson ratio $\nu_{vac} = 2/7$ (Axiom 1 LC + Axiom 2 $\alpha$ interlink), Cosserat couple-stress modulus $\gamma_c$, bulk mass density $\rho_{bulk} = \xi_{topo}^2 \mu_0 / (P_C \ell_{node}^2)$, transverse mechanical wave speed $v_T = c_0$ at the cold-lattice limit (modulated to $v_T(A_0) = c_{shear}(A_0) = c_0\sqrt{S(A_0)}$ under saturation), two distinct longitudinal speeds (KEEP-BOTH, 2026-06-08 $c_L$ reconciliation, Rule 12) — the **bulk-modulus dilatational / A1-scalar port-mode** $v_{bulk} = \sqrt{2}\, c_0 = \sqrt{K/\rho}$ (drops the $4G/3$ shear term) **distinct from** the **solid longitudinal P-wave** $c_L = \sqrt{(K + 4G/3)/\rho} = \sqrt{10/3}\, c_0 \approx 1.83\, c_0$ at $\nu_{vac} = 2/7$ — and Cosserat characteristic length $l_c = \sqrt{\gamma_c / G_{vac}}$ identified with the weak-force range $r_W$.

## Node-model channel tags (session add — bulk = MASS-"3"/A1, shear = CHARGE-"3"/Cosserat)

Per the corrected graded-vacuum-impedance-network device model ([`device-circuit-models.md`](../ch3-pin-port-configuration/device-circuit-models.md):143-149, on main), the mechanical primitives map onto the two CONFINED channels of the 2-domain N-port: the **bulk channel** carries the **MASS-"3"** (A1 dilatation, $Z_{bulk} = \rho_{bulk}\, c_{bulk} = \sqrt{2}\,\rho_{bulk}\, c_0$ at $K = 2G$, $\Gamma_{bulk} \to -1$ CONFINED — a *mechanical/acoustic* impedance $\rho \times$ speed, NOT in $Z_0$ units), and the **shear channel** carries the **CHARGE-"3"** (Cosserat micro-rotation winding, $Z_{shear} = \rho_{bulk}\, c_{shear}$, $\Gamma_{shear} \to -1$ CONFINED). The EM channel ($Z_{EM} \equiv Z_0 = \sqrt{\mu_0/\varepsilon_0} \approx 376.73\,\Omega$, $\Gamma_{EM} = 0$) is the sole external MATCHED radiative PORT — not a mechanical primitive (it lives in $\Omega$, an electrical-impedance DOMAIN distinct from the $\rho c$ mechanical impedances). $A1 \perp T2$: the mass (A1 dilatation) and charge/spin (Cosserat $(2,3)$ micro-rotation) grades are orthogonal, never wired into one shared phasor (the two-"3"s fence, [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20).

The chapter content is **Class B/C synthesis** per `consistency-vs-emergence` v1.3 --- no new substrate-physics primitives are introduced; the content consolidates canonical mechanical-sector derivations (CLAUDE.md INVARIANT-S2 Axiom 1; $\nu_{vac} = 2/7$ at `vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md`; $K_{vac} = 2 G_{vac}$ at the EMT $p^* = 8\pi\alpha$ packing fraction; weak-force range $l_c$ at `vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md` line 39; $c_{EM}$-vs-$c_{shear}$ semantic distinction at `clm-8nkvwy`) into datasheet Mechanical-Characteristics format, with the EE-substrate-native projection per `common/translation-tables/translation-circuit.md` $\S4$ added as the EE mechanical translation table.

## Primary canonical sources

| Source | Content |
|---|---|
| CLAUDE.md INVARIANT-S2 (Axiom 1) | Cosserat micropolar 6 DOF per node; intrinsic spin from microrotational DOF; $c_{EM}$ vs $c_{shear}$ distinction; SYM-class $\alpha$ invariance |
| Vol 1 Ch 1 (`vol_1_foundations/chapters/01_fundamental_axioms.tex`) | Canonical chapter-form derivation of Axiom 1 |
| Vol 1 Ch 4 §`sec:cosserat_primer` | Cosserat primer (manuscript) |
| [`vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md`](../../vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md) (`clm-x19btt`) | $\nu_{vac} = 2/7$ derivation from $K_{vac} = 2 G_{vac}$ + standard isotropic identity |
| [`vol3/gravity/ch01-gravity-yield/topological-packing-fraction.md`](../../vol3/gravity/ch01-gravity-yield/topological-packing-fraction.md) | EMT $p^* = 8\pi\alpha$ packing fraction (input to $K/G = 2$) |
| [`vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md`](../../vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md) | 1D $\to$ 3D volumetric bulk projection = 1/7 |
| [`vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md) (`clm-5zuo7g`, `clm-q8un7j`) | $l_c = \sqrt{\gamma_c / G_{vac}}$ weak-force range; $W/Z$ evanescent cutoff masses; $m_W/m_Z = \sqrt{7}/3$ |
| [`common/appendix-derived-numerology.md`](../../common/appendix-derived-numerology.md) (`clm-zi6t1e`) | Derived hardware numerology incl. $\nu_{vac} = 2/7$, $K = 2G$ at $p^* = 8\pi\alpha$, $n_{3D} = 38/21$ |
| [`common/translation-tables/translation-circuit.md`](../../common/translation-tables/translation-circuit.md) (`clm-eemap1`) | EE-substrate-native META framework + comprehensive substrate-primitive-to-EE-component mapping table |
| [`common/trampoline-framework.md`](../../common/trampoline-framework.md) line 188 | Cosserat rotation-sector mass-gap $m_\omega \sim 1$ MeV (consequence for Ch.10) |
| [`vol9/ch3-pin-port-configuration/device-circuit-models.md`](../ch3-pin-port-configuration/device-circuit-models.md):143-149 | Node-model channel tags: bulk = MASS-"3"/A1 dilatation ($Z_{bulk}$), shear = CHARGE-"3"/Cosserat micro-rotation ($Z_{shear}$), EM = matched radiative PORT ($Z_0$, $\Gamma_{EM} = 0$); $A1 \perp T2$ orthogonality fence |
| `src/ave/core/constants.py` | symbols `NU_VAC`, `RHO_BULK`, `G_VAC`, `V_LONG`, `XI_TOPO`, `P_C`, `L_NODE` (symbol-name cites; line numbers unstable across renumbers) |

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/09_mechanical_characteristics.tex` (canonical Vol 9 chapter file; populated in this PR)

## Cross-chapter dependencies within Vol 9

- **Ch 1 (General Description and Features)** establishes the substrate identity + 6-DOF Cosserat micropolar framing; Ch 9 spec'es the resulting bulk mechanical primitives.
- **Ch 6 (Temperature Characteristics)** documents the Cosserat-Curie thermal-asymmetry $\delta_{strain}$ at $T_{CMB}$ as a consequence of the rotation-sector mass-gap thermally freezing $\mu$ while $\varepsilon$ remains thermally populated --- the same Cosserat couple-stress $\gamma_c$ that sets the weak-force range in this chapter.
- **Ch 7 (Saturation Characteristics)** sets the Axiom 4 kernel $S(A_0) = \sqrt{1 - (A_0/A_{yield})^2}$ that modulates $v_T(A_0) = c_{shear}(A_0) = c_0\sqrt{S(A_0)}$ at finite operating point.
- **Ch 10 (Magnetic / Microrotational Characteristics)** develops the magnetic-sector consequences of the Cosserat couple-stress $\gamma_c$ spec'd here: flywheel inductance, rotation-sector mass-gap, weak-force range as a magnetic-sector spec entry.

## Cross-volume canonical-derivation pointers

- Vol 3 Ch.~`ch:gravity_and_yield` (manuscript) --- canonical derivation of $\nu_{vac} = 2/7$ + the gravitational-time-dilation $c_{shear} = c_0\sqrt{S}$ Schwarzschild reduction in the SYM-class gravity-class limit.
- Vol 2 Ch.~`ch:electroweak` (manuscript) --- canonical $l_c$ + Yukawa-cutoff derivation; $W/Z$ mass ratio from $\nu_{vac}$.
- Vol 1 Ch.~`ch:regime_map` --- four-regime kernel context for $S(A_0)$ saturation modulation.

---
