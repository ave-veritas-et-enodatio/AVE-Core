[↑ Ch.4 Continuum Electrodynamics](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-efo113, clm-lv3uw1]
-->

> ↗ See also: [Particle Physics (Torus Knot Ladder)](../../../vol2/particle-physics/index.md) — trapped knots yield baryon mass spectrum
> ↗ See also: [Gravity (Metric Refraction)](../../../vol3/gravity/index.md) — refractive gradient produces gravitational acceleration
> ↗ See also: [FDTD Solver](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/index.md) — computational implementation of Master Equation

## Section 4.1: The Unifying Master Equation

If the discrete spatial vacuum is a physical LC network (the substrate) supporting momentum limits and finite wave propagation, its macroscopic low-energy effective field theory (EFT) mathematically maps to continuous network dynamics.

Before discussing the bulk properties of the universe, the transport mechanism is defined. In the continuous limit ($L \gg \ell_{node}$), signal propagation is governed by the classical Maxwell-Heaviside acoustic wave equation:

> ↗ See also: [Historical Precedents](../../../common/historical-precedents.md) — why it is *Maxwell-Heaviside*: Maxwell wrote EM in Hamilton's quaternions; Heaviside-Gibbs reformulated to vector calculus, demoting the scalar/longitudinal (correct for the transverse photon; the longitudinal re-engages at saturation = the electron).

> **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal re-engages at saturation = the electron" names the **A1 dilatation-MASS** "3" only — the Heaviside-excised longitudinal compression scalar (the A1 breather; `mₑc²` = trapped acoustic compression energy). It must **NOT** be conflated with the **second, orthogonal "3"**: the Cosserat **micro-rotation `(2,3)` WINDING** (T2 couple-stress, the Axiom-1 intrinsic-spin DOF; charge = Beltrami helicity `H_bel = ∫ω·(∇×ω)`). The "3" is **TWO DISTINCT objects, orthogonal (A1 ⊥ T2)** — Grant-ratified, recorded verbatim at the crystal-graft-v2 result §0 ("The two distinct '3's", branch `analysis/2026-06-09-crystal-graft-v2`; the n-exponent qualifier addendum at `9fdba6fe`). Load-bearing consequence (same source): **never wire the winding into the breather's own phasor `(V_inc, V_ref)`** — `V_ref` is a read-only projection of the same scalar `V`, not an independent DOF; doing so self-inflicts the genesis-24/crystal `w_pol = 0` double-count. The electron is the unknot dilatation-mass **carrying** the `(2,3)` winding — two objects, not one.

> **↗ Cross-link (2026-06-10, Rule 12, Grant rename-queue R1 — note above preserved):** this two-objects content is the STATE-side companion to the PROVENANCE-vs-STATE ontology at [`photon-identification.md:11`](photon-identification.md) — the (2,3) winding *rides* the condensed phase (the A1 standing-V order parameter); "self-trapped photon" is provenance, not state. Registry §5 R1.

> **↗ MASS = A1 DEPRESSION / FLYWHEEL = T2 ($\omega$) FREQUENCY-REGULATOR — the clean split (2026-06-20, Rule 12 framing-note, consistency-class reframe NOT a new chord; Grant-ratified mass-sector ruling).** The two-"3"s above split into **A1 = mass** and **T2 = spin/charge**; this note names *what each sector physically is* in the mass sector:
> - **A1 (the mass "3") = the rest-mass STORE = the trampoline DEPRESSION** — the standing bulk-reactance wave's **mutual couple to the bulk lattice** ($K$ = inter-node bulk modulus; $Z_{bulk}\to0 \Rightarrow \Gamma_{bulk}=-1$ at the cage; [`lattice-extreme-bh-rationality.md`](../../../vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md):28).
> - **T2 / Cosserat micro-rotation ($\omega$) = the FLYWHEEL = the local FREQUENCY REGULATOR** — the rotor / Park-dq field-oriented-control rotating frame / the electron's spin-clock (Compton/Larmor). The "mass-gap $m^2 = 4 G_c/I_\omega$" on this sector is the flywheel's *clock* gap, **NOT** the rest mass.
> - **A1 ⊥ T2 = the FOC 90° orthogonal decoupling** — the substrate holds mass (A1) and spin/charge (T2) at $90°$ to eliminate mutual inductance (canonical FOC: [`helium-symmetric-cavity.md`](../../../vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md):52-56, [`de-broglie-standing-wave.md`](../../../vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md):13). **This is the MECHANISM behind the no-double-count guard** stated above ("never wire the winding into the breather's own phasor").
> - **Lepton tower:** more Cosserat torsion → faster flywheel → higher regulated frequency → (Compton $f = mc^2/\hbar$) deeper A1 depression → more mass. The flywheel regulates the frequency that *sets* the mass; the mass stays A1.
>
> ⚑ **Open Grant-flag (chord-candidate, surfaced not resolved):** does the FOC mechanism *FORCE* the A1 ⊥ T2 orthogonality (i.e., a *derivation* of the no-double-count guard from mutual-inductance minimization) rather than *assert* it? If forced, that would promote the guard from asserted to derived — a chord-candidate. Not adjudicated here.

> **[Resultbox]** *Maxwell-Heaviside Acoustic Wave Equation*
>
> $$
> \frac{\partial^2 \mathbf{E}}{\partial t^2} - c^2 \nabla^2 \mathbf{E} = 0 \quad , \quad c = \frac{1}{\sqrt{\epsilon_0 \mu_0}}
> $$

Because the ambient vacuum is a discrete lattice, the fundamental mechanical update equations at the node scale are given by the discretised Finite-Difference Time-Domain (FDTD) operator (the Yee Cell update):

> **[Resultbox]** *FDTD Yee Cell Update*
>
> $$
> \mathbf{E}^{n+1} = \mathbf{E}^n + \frac{\Delta t}{\epsilon_0} (\nabla_d \times \mathbf{H}^{n+1/2}) \quad , \quad \mathbf{H}^{n+1/2} = \mathbf{H}^{n-1/2} - \frac{\Delta t}{\mu_0} (\nabla_d \times \mathbf{E}^n)
> $$

Interpreting these equations as the acoustic oscillation of structural string tension ($\epsilon_0$) and inertia ($\mu_0$), the macroscopic kinematics of the expanding universe can be evaluated using these generalised electrodynamic limits.

Synthesizing the continuous macroscopic wave equation with the explicit lattice saturation hardware limit established in Axiom 4 ($\epsilon_{eff}$), yields the single, overarching mathematical framework governing the entire Applied Vacuum Engineering paradigm.

In standard physics, the vacuum parameters ($\epsilon_0, \mu_0$) are strictly linear constants, resulting in the fundamental D'Alembert wave operator $\Box V = 0$:

> **[Resultbox]** *D'Alembert Wave Operator*
>
> $$
> \nabla^2 V - \underbrace{\mu_0 \epsilon_0}_{= 1/c^2} \frac{\partial^2 V}{\partial t^2} = 0
> $$

However, because the substrate lattice undergoes measurable, non-linear dielectric yielding as it approaches the $43.65\text{ kV}$ topological saturation bound, the constitutive permittivity physically collapses under the universal saturation kernel $S$. Axiom 4 (squared limit, $n=2$) defines:

> **[Resultbox]** *Non-Linear Permittivity Collapse*
>
> $$
> \varepsilon_{eff}(V) = \varepsilon_0 \cdot \sqrt{1 - \left(\frac{V}{V_{yield}}\right)^2}
> $$

The substitution is direct: wherever the standard wave equation contains the constant $\varepsilon_0$, it is replaced with the voltage-dependent $\varepsilon_{eff}(V)$. Because $c_{eff}(V) = 1/\sqrt{\mu_0 \varepsilon_{eff}(V)}$, the local wave speed itself becomes a function of the field amplitude:

<!-- claim-quality: clm-efo113 -->
**Domain of validity (EFT statement).** The direct substitution of $\varepsilon_{eff}(V)$ into the linear D'Alembert form is exact only in the leading-order long-wavelength EFT regime, where the field-gradient corrections that arise from $\nabla \cdot \mathbf{D} = \varepsilon_{eff}(V)\,\nabla \cdot \mathbf{E} + (\nabla \varepsilon_{eff})\cdot \mathbf{E} = 0$ are subdominant to the inertial term $\varepsilon_{eff}(V)\,\partial^2 V/\partial t^2$. This holds in the linear limit $V \ll V_{yield}$ (where $d\varepsilon_{eff}/dV \to 0$ and $\nabla \varepsilon_{eff} \to 0$). Particle confinement and standing-wave claims at $V \to V_{yield}$ depend on the dropped first-derivative gradient terms remaining negligible by symmetry at saturation; we use the leading-order form throughout this volume and flag the EFT caveat explicitly where downstream chapters invoke the master equation in the saturated regime. A higher-order correction including the $\nabla \varepsilon_{eff} \cdot \nabla V$ term is not derived here but is required for any quantitative claim that depends on the wave-equation form near $V_{yield}$ rather than on the saturation kernel $S$ alone.

> **[Resultbox]** *Field-Dependent Wave Speed*
>
> $$
> c_{eff}(V) = c_0 \left(1 - \left(\frac{V}{V_{yield}}\right)^2\right)^{-1/4}
> $$

Note: the wave speed *increases* as permittivity drops (thinner dielectric $\to$ faster propagation), while the **longitudinal-A1 bond compliance** $C_{eff} = C_0/S \to \infty$ (the stretch-reactance softening at yield). Per the Q1 = (B) sector split (INVARIANT-S2, Grant-ratified 2026-06-15) this $C_0/S$ is a DISTINCT sector from the transverse permittivity — orthogonal reactances (A1 ⊥ T2, line 20 above), not one object; the LCR-measured *transverse* capacitance $C_{diel}=\varepsilon_{eff}A/d\propto S$ rolls off, it does **not** diverge. The resulting non-linear wave equation is the **Unifying AVE Master Equation**:

> **[Resultbox]** *The Unifying AVE Master Equation*
>
> <!-- eq:master_wave -->
>
> $$
> \nabla^2 V - \mu_0 \, \varepsilon_0 \sqrt{1 - \left(\frac{V}{V_{yield}}\right)^2}
> \;\frac{\partial^2 V}{\partial t^2} = 0
> $$

This single line of non-linear differential topology formally replaces the fragmented domains of the Standard Model and General Relativity:

1. **Classical Electromagnetism ($V \ll 43.65\text{ kV}$):** The square root term evaluates to 1. The equation reduces to the linear Maxwellian wave equation used in standard optics and RF engineering.
2. **Particle Assembly ($V \to 43.65\text{ kV}$):** The non-linear regime divides into two distinct saturation symmetries (per Axiom 4 confinement theorem):
   - *Asymmetric (electric-only) saturation*, where only $\varepsilon_{eff} \to 0$ while $\mu_{eff}$ remains intact, drives $Z = \sqrt{\mu_0/\varepsilon_{eff}} \to \infty$ — the medium becomes electromagnetically opaque (evanescent, no energy transport). This is the dielectric-rupture branch (electric breakdown).
   > **🔴 MAGNETIC-BRANCH = SIGN-SELECTOR, NOT CAGE-MECHANISM (2026-06-18, Rule 12 / PR#260 B3-DEGENERATE — body below PRESERVED unedited; Grant-ratified).** The "magnetic branch" named in the body below is the **chirality/spin SIGN-selector** (μ-first $\Rightarrow \Gamma=-1$ vs ε-first $\Rightarrow \Gamma=+1$ are the spin-conjugate signs) and is **MUTE on the mass sector** — it is NOT the cage *mechanism*. The electron mass-cage is the **A1 longitudinal dilatation** ($Z_{bulk}\to0 \Rightarrow \Gamma_{bulk}=-1$); the magnetic-vs-electric fork is DEGENERATE on the equilibrium observables ($Z=Z_0\sqrt{S}$, $|\Gamma|=1$ both ways) and the asymmetry is chirality-set, not substrate-forced (`vol1/claim-quality.md`:280 scope-note; wall-fork H3 result). Reading the body as "confinement proceeds via the magnetic/charge sector" would wire the cage into the $T_2$ charge-winding and break the two-"3"s orthogonality (A1 ⊥ T2, [`master-equation.md`](master-equation.md):20). Body preserved per Rule-12.
   - <!-- claim-quality: clm-lv3uw1 --> *Particle confinement* proceeds via the magnetic branch instead: at a torus-knot self-intersection the field $\mathbf{B}$ saturates $\mu_{eff}$ first, driving $Z = \sqrt{\mu_{eff}/\varepsilon_0} \to 0$ and $\Gamma \to -1$ (short-circuit). The accelerating wave reflects off its own self-induced impedance boundary, trapping into a stabilised topological knot (a Fermion) and physically generating invariant rest mass without invoking the Higgs Mechanism.

   Both branches are governed by the same kernel $S(A) = \sqrt{1-(A/A_{yield})^2}$; they differ in which constitutive parameter saturates first. See LIVING_REFERENCE Axiom 4 derived consequences for the symmetric vs asymmetric tables.
3. **Gravity:** The trapped topological knot permanently strains the surrounding $\varepsilon_{eff}$ and $\mu_{eff}$ fields symmetrically ($n(r) = 1 + 2GM/rc^2$). This produces a continuous refractive gradient radially outward while preserving $Z_0$. Test photons propagating through this gradient refract toward the knot, executing the macroscopic acceleration attributed to gravity.

---
