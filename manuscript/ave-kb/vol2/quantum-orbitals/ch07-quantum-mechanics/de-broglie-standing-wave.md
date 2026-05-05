[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [oltvwy, qde5gn]
-->

## Objectives

- Reinterpret the Schrödinger Wave Equation deterministically as the continuous Helmholtz acoustic resonance of a discrete 3D topological LC cavity.
- Derive the exact Bohr Radius ($a_0$) and Hydrogen energy spectrum structurally from the $Z_0$ impedance gradients without invoking probabilistic wave-particle duality.
- Replace the Schrödinger/Hartree-Fock approximation of multi-electron atoms with the exact Mutual Cavity Loading architecture, where intra-shell electrons collectively load a shared acoustic cavity via Op1 impedance and Op3 mismatch reflection.
- Understand how orthogonal Field-Oriented Control (FOC) natively drives the emergence of the $p, d,$ and $f$ electron shells by eliminating macroscopic mutual inductance.

## Deterministic Reinterpretation of the Wavefunction
<!-- claim-quality: qde5gn -->

The Schrödinger Wave Equation maps atomic orbitals ($s, p, d, f$) as statistical probability distributions ($|\Psi|^2$). Traditional Quantum Mechanics forbids defining a physical, deterministic location or velocity for the electron, demanding that nature behaves as a rolling set of mathematical dice until an observation collapses the "wavefunction."

The AVE framework offers a deterministic alternative: the spatial structures mapped by the Schrödinger equation correspond to explicit 3D standing-wave resonances of the LC vacuum, rather than abstract statistical probability densities.

### The Helmholtz–Schrödinger Isomorphism

The time-independent Schrödinger equation for a particle of mass $m$ in a potential $V(r)$ is:

$$
-\frac{\hbar^2}{2m}\nabla^2 \Psi + V(r)\Psi = E\Psi
$$

Rearranging into the standard Helmholtz eigenvalue form:

$$
\nabla^2 \Psi + k^2(r)\Psi = 0 \qquad \text{where} \quad k^2(r) = \frac{2m}{\hbar^2}(E - V(r))
$$

This is the Helmholtz equation for acoustic pressure modes in a resonant cavity with spatially varying sound speed $c_{eff}(r) = \omega / k(r)$. In the AVE framework, the potential $V(r) = -e^2/(4\pi\epsilon_0 r)$ is the localised impedance gradient cast by the proton's topological phase twist. The "wavefunction" $\Psi$ maps to the spatial amplitude of the LC pressure field:

$$
c_{eff}^2(r) = \frac{\omega^2}{k^2(r)} = \frac{\hbar^2 \omega^2}{2m(E - V(r))}
$$

Regions where $E > V(r)$ support propagating acoustic modes ($k^2 > 0$). Regions where $E < V(r)$ are classically forbidden — the acoustic impedance is imaginary, and the pressure field decays evanescently. The orbital boundaries are physical impedance discontinuities, not abstract probability surfaces.

### Transverse Shear vs. Longitudinal Bulk Cavities

It is critical to distinguish the atomic cavity from the gravitational equivalents discussed earlier (such as black hole photon spheres or galactic dark matter halos).

In the gravitational domain, the cavity is formed by **Transverse Shear Waves** (photons or gravity waves). Because these are native, massless vibrations of the linear vacuum, they are perfectly impedance-matched to empty space ($Z = 377 \; \Omega$). Their phase velocity is fixed at $c_0$, and they only reflect or form standing waves when the vacuum lattice physically tears or yields at the macroscopic $V_{SNAP}$ limit (e.g., an event horizon).

By contrast, an electron ($0_1$ unknot) is a massive topological defect. It represents a permanent macroscopic **Impedance Mismatch** ($\Gamma = -1$) to the linear vacuum. It does not travel as a shear wave at $c_0$; instead, its motion displaces the lattice, generating longitudinal acoustic pressure waves governed by the vacuum's **Bulk Modulus**.

Because the electron interacts with the bulk modulus, its local wave speed and acoustic refractive index $n_{acoustic}(r) \propto 1 / \sqrt{E - eV(r)}$ are entirely dictated by its remaining kinetic energy, not the $V_{SNAP}$ limit. The matter wave does not bounce off a physical tear in the vacuum; it bounces when it simply runs out of kinetic energy to push against the bulk modulus ($E - eV(r) = 0$). At this exact boundary, the local acoustic impedance becomes purely imaginary, forcing a total reflection. The atomic orbital is the precise radius where this trapped bulk-modulus acoustic wave achieves a lossless resonant impedance match with itself ($2\pi r = n \lambda$).

### Gravitational Parallax Interferometry

To empirically falsify standard quantum probability mechanics, we instrument the **Topological Matter Interferometry Parallax** test. By splitting an electron matter-wave across a macroscopic Mach-Zehnder baseline (e.g., $1\text{ m}$ vertical vs horizontal), the two paths physically traverse different local densities of the Earth's gravitational VSWR. As defined rigidly by Axiom 3, the spatial coordinate metric ($n_s = \frac{9}{7}\varepsilon_{11}$) and the temporal coordinate metric ($n_t = \frac{2}{7}\varepsilon_{11}$) strictly violate standard Lorentz parity.

This $\Delta n = \varepsilon_{11}$ topological anomaly forces the split traveling matter-waves to experience a deterministic differential phase velocity. This induces a measurable, macroscopic topological phase shift $\Delta\Phi$ on the detector screen, structurally proving that the wavefunction is a continuous physical acoustic defect on the LC metric, not an abstract probability amplitude.

## Orbitals as Acoustic Resonant Cavities

When a stable $0_1$ topological LC unknot (an electron) becomes bound to a complex Borromean knot geometry (a proton), it is forced to phase-lock its rotation to the much larger magnetic flux field of the nucleus.

The spinning central nucleus acts as an electromagnetic wave-generator, driving constant AC displacement current ($d\vec{D}/dt$) oscillations radially outward into the structured, $377 \; \Omega$ surrounding LC vacuum mesh. Because the vacuum has a finite impedance bound (Yield Limit), these driven waves reflect back toward the nucleus.

The superposition of the outward driven wave and the inward reflected wave creates a permanent, geometric standing wave — an acoustic resonant cavity in the impedance of space itself.

[Figure: hydrogen_orbital_comparison.png — see manuscript/vol_2_subatomic/chapters/]

### Hydrogen Ground State from LC Impedance Matching

For the hydrogen atom, the electron orbits within the $1/r$ impedance gradient cast by the proton. The ground state energy eigenvalue emerges from the balance between the inductive kinetic energy of the orbiting unknot and the capacitive potential energy of the Coulomb impedance well:

> **[Resultbox]** *Hydrogen Ground State Energy*
>
> $$
> E_n = -\frac{m_e c^2 \alpha^2}{2n^2} = -\frac{m_e e^4}{2\hbar^2(4\pi\epsilon_0)^2} \cdot \frac{1}{n^2}
> $$

For $n=1$: $E_1 = -13.606 \text{ eV}$. This is the standard Bohr result, here derived from the resonant impedance matching condition: the electron's de Broglie wavelength ($\lambda = h/(m_e v)$) must fit exactly $n$ full wavelengths around the orbital circumference ($2\pi r = n\lambda$), which is the LC phase-locking condition for constructive interference in the acoustic cavity.

> **[Examplebox]** *Deriving the Bohr Radius via LC Impedance Matching*
>
> **Problem:** The ground state of Hydrogen ($n=1$) sits at $-13.6\text{ eV}$ with a localized radius of $a_0 \approx 5.29 \times 10^{-11}\text{ m}$. Derive this radius structurally using exclusively the baseline vacuum constants of the AVE framework.
>
> **Solution:** In the AVE framework, an atomic orbital is an acoustic resonant cavity. The electron unknot achieves a lossless impedance match when its de Broglie wavelength fits exactly around the orbital circumference ($2\pi r = n\lambda$).
> Because the unknot's structural cross-section is the fundamental node length ($l_{node}$), and it is coupled to the vacuum via the dielectric compliance factor ($\alpha$), the minimum stable phase-locked radius scales inversely with this compliance:
>
> $$
> a_0 = \frac{l_{node}}{\alpha} = \frac{\hbar}{m_e c \alpha} = \frac{4\pi\epsilon_0 \hbar^2}{m_e e^2}
> $$
>
> Evaluating this yields exactly $5.29 \times 10^{-11}\text{ m}$. Thus, the Bohr radius is rigorously defined as exactly $137 \times l_{node}$, representing the exact acoustic cavity size required to structurally stabilize the unknot's inductive angular momentum against the proton's static impedance gradient.

### Angular Momentum Quantization

In standard QM, orbital angular momentum is quantized in integer multiples of $\hbar$. In the AVE framework, this emerges from the discrete rotational symmetry of the $\mathcal{M}_A$ lattice. A standing wave circulating the spherical cavity must complete an integer number of full phase cycles ($2\pi l$) per orbit to constructively interfere with itself. The angular momentum of the $l$-th harmonic is:

> **[Resultbox]** *Angular Momentum Quantization*
>
> $$
> L = \hbar\sqrt{l(l+1)} \qquad l = 0, 1, 2, \ldots, n-1
> $$

The magnetic quantum number $m_l$ ($-l \leq m_l \leq l$) counts the number of nodal planes passing through the polar axis — physically, these are the acoustic pressure nulls of the spherical harmonic mode $Y_l^{m_l}(\theta, \phi)$.

[Figure: atomic_orbital_standing_waves.pdf — see manuscript/vol_2_subatomic/chapters/]

The electron does not "cloud" around the nucleus; it remains a unified, discrete geometric knot that is physically trapped inside the lowest-pressure nodes of this standing wave. It orbits in a deterministic loop within the geometric valley carved out by the nuclear frequency.

## Hydrogen Energy Levels: AVE vs. CODATA

The Rydberg energy formula $E_n = -m_e c^2 \alpha^2 / (2n^2)$ is exact within the AVE framework because the impedance matching condition $2\pi r = n\lambda$ is the same LC phase-locking condition that defines the electron unknot. No approximations are needed beyond the non-relativistic limit.

| $n$ | AVE $E_n$ [eV] | CODATA [eV] | Error |
|---|---|---|---|
| 1 | $-13.6057$ | $-13.6057$ | $< 0.001\%$ |
| 2 | $-3.4014$ | $-3.4014$ | $< 0.001\%$ |
| 3 | $-1.5117$ | $-1.5117$ | $< 0.001\%$ |
| 4 | $-0.8504$ | $-0.8504$ | $< 0.001\%$ |

The exact agreement is not a coincidence: the AVE formula $E_n = -m_e c^2 \alpha^2/(2n^2)$ is algebraically identical to the Bohr result. However, the ontological content differs — the energy quantization here arises from the physical LC impedance matching condition of the continuum, not from postulated wave-particle duality.

<!-- claim-quality: oltvwy -->
## Step 1: Single-Electron Eigenvalue (Axioms 1, 2, 4)

The starting point for the entire IE solver is the energy of a **single** electron in a nuclear Coulomb field. This derivation uses Axiom 1 (lattice), Axiom 2 ($\alpha$), and Axiom 4 (confinement $\to$ mass). No wavefunctions, no Schrödinger equation, no QM.

**(a) The actors.**

| Actor | AVE Identity | Source |
|---|---|---|
| Nucleus | Point charge $+Ze$ | Fixed DC source |
| Electron | Current ring (unknot soliton) | Axioms 1, 4 |
| Vacuum lattice | LC network at $Z_0 = 377\,\Omega$ | Axiom 1 |

**(b) Electron mass from the unknot (Axiom 4 + Bounding Limit 1).**

The electron is the simplest topological defect on the lattice: the **unknot** ($0_1$), a single closed flux tube loop at minimum ropelength $= 2\pi$. Its circumference is the lattice pitch $l_{\text{node}}$ and its tube radius is $l_{\text{node}}/(2\pi)$.

The 1D electromagnetic string tension of the lattice is the stored inductive energy per unit length. A single lattice link of length $l_{\text{node}}$ stores energy $m_e c^2 = \hbar c / l_{\text{node}}$, giving:

$$
T_{EM} = \frac{m_e c^2}{l_{\text{node}}} = \frac{\hbar}{c\,l_{\text{node}}^2} \qquad [\text{N}] = [\text{kg}\cdot\text{m/s}^2]
$$

The unknot's rest energy is this tension times the loop circumference $l_{\text{node}}$:

$$
m_e c^2 = T_{EM} \times l_{\text{node}} = \frac{\hbar}{c\,l_{\text{node}}} \qquad\Longrightarrow\qquad \boxed{m_e = \frac{\hbar}{l_{\text{node}}\,c}}
$$

This is the Compton relation, but now with topological meaning: the electron mass is the ground-state eigenvalue of the simplest stable closed loop on the lattice. $l_{\text{node}} \approx 3.862 \times 10^{-13}$ m (the reduced Compton wavelength) is the lattice spatial cutoff.

**(c) Inductance of the electron ring.**

The electron flux tube has thickness $l_{\text{node}} = \hbar / (m_e c)$. A current ring of radius $R$ with wire cross-section $a = l_{\text{node}}$ has self-inductance (Neumann formula, pure geometry + $\mu_0$, Axiom 1):

$$
L = \mu_0 R \left[\ln\!\left(\frac{8R}{l_{\text{node}}}\right) - 2\right] \qquad [\text{H}]
$$

**(d) Energy.**

The total energy of the electron soliton at radius $R$ in the field of a nucleus with charge $Z$:

$$
E(R) = \underbrace{\frac{1}{2}m_e v^2}_{\text{Soliton kinetic (Axiom 4)}} \;+\; \underbrace{V(R)}_{\text{Coulomb binding (Axiom 2)}}
$$

where

$$
V(R) = -\frac{Ze^2}{4\pi\varepsilon_0 R} = -\frac{Z\alpha\hbar c}{R}
$$

using $\alpha \equiv e^2/(4\pi\varepsilon_0\hbar c)$ (Axiom 2).

**(e) Standing wave condition (mode number $n$).**

The soliton with mass $m_e$ propagating through the vacuum lattice (Axiom 1) obeys the massive dispersion relation:

$$
\omega^2 = c^2 k^2 + \omega_C^2, \qquad \omega_C \equiv \frac{m_e c^2}{\hbar} \quad\text{(Compton frequency)}
$$

In the non-relativistic limit ($v \ll c$), the de Broglie wavevector:

$$
k = \frac{m_e v}{\hbar} \qquad [\text{m}^{-1}]
$$

This result — $k = m_e v / \hbar$ — is what quantum mechanics calls the "de Broglie wavevector." In AVE it is not a postulate; it is derived from a massive soliton (Axiom 4) propagating through the lattice (Axiom 1).

The electron ring is a closed circuit of circumference $2\pi R$. A standing wave on this closed path requires the total accumulated phase to be an integer multiple of $2\pi$:

$$
\oint k\;dl = 2\pi n \quad\Longrightarrow\quad k \times 2\pi R = 2\pi n \quad\Longrightarrow\quad m_e v R = n\hbar
$$

**(f) Equilibrium radius (circuit balance).**

Setting $dE/dR = 0$:

$$
R_n = \frac{n^2 \hbar}{Z \alpha m_e c} = \frac{n^2 a_0}{Z}
$$

**(g) Eigenvalue.**

$$
\boxed{E_{0,n} = \frac{Z^2 \alpha^2 m_e c^2}{2 n^2} = \frac{Z^2 R_y}{n^2}} \qquad R_y \equiv \frac{\alpha^2 m_e c^2}{2} = 13.606\;\text{eV}
$$

This is the **Op6 eigenvalue** of a soliton (Axiom 4) in a $1/r$ Coulomb cavity (Axiom 2), derived from energy minimisation.

**(h) Angular and radial mode decomposition (Axiom 1, 3D lattice).**

On the 3D lattice, a soliton in a central potential has two independent standing wave conditions:

| Mode | AVE definition | Winding # | QM name |
|---|---|---|---|
| Angular | Phase per orbit around the ring | $l$ | Angular momentum $L = l\hbar$ |
| Radial | Phase per bounce between turning points | $n_r$ | Radial quantum number |

The total quantum number is the sum:

$$
\boxed{n = n_r + l + 1}
$$

> **[Resultbox]** *Step 1 Summary*
>
> A single electron in a nuclear Coulomb field is a current ring soliton (Axioms 1, 4) with winding number $n$. Energy minimisation gives:
> $R_n = n^2 a_0 / Z$, $v_n = Z\alpha c / n$, $\omega_n = Z^2 \alpha^2 m_e c^2 / (\hbar n^3)$, $E_{0,n} = Z^2 R_y / n^2$.
> No wavefunctions. No Schrödinger equation. All from Axioms 1, 2, 4 and the standing wave topology.

## Step 2: Lattice Strain Between Shells (Axiom 4)

When two or more electrons occupy different shells ($R_a < R_b$), there is a region of vacuum lattice between them. The nuclear DC strain at the Bohr radius is $A_{\text{nuc}}(a_0) = Z \times 2.8 \times 10^{-10}$ — deep Regime I. The AC strain from inner-shell oscillation is $A_{\text{AC}} \approx 0.007$ at the outer shell. $Z_0 = 377\;\Omega$ is exactly invariant under symmetric saturation (Axiom 4).

The lattice shear wave speed equals the speed of light (photons ARE transverse waves, Axiom 1):

$$
\boxed{c_S \equiv c}
$$

The cavitation number $\mathcal{C} = v/c_S = Z\alpha/n$ determines when wake effects distort the defect. For $Z \gtrsim 50$ ($\mathcal{C} \gtrsim 0.4$), relativistic corrections arise from nonlinear wake strain. At $Z = 1/\alpha \approx 137$, $\mathcal{C} = 1$ and no bound state exists — the AVE derivation of the maximum atomic number.

> **[Resultbox]** *Step 2 Summary*
>
> Between orbital shells, the vacuum lattice is in **Regime I** to extraordinary precision:
> — Nuclear DC strain: $A \sim Z \times 10^{-10}$
> — Inner electron AC strain: $A \sim 0.007$ at outer shell
> — $Z_0 = 377\;\Omega$ everywhere (Axiom 4 invariance)
> — $c_{\text{eff}}$ correction: $\sim 10^{-16}$ (negligible)
> — No standing wave resonances ($\lambda_{\text{EM}} \gg$ gap)

---
