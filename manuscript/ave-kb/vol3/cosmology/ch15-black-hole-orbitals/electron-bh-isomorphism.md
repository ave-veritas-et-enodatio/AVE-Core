[↑ Ch.15 Black Hole Orbitals](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-ir8h78]
-->

## The Electron--Black Hole Isomorphism

In the AVE framework, the electron is a self-trapped photon---a topological $0_1$ unknot confined at the lattice node scale ($\ell_{node}$) by a $\Gamma = -1$ total internal reflection boundary. The event horizon of a Schwarzschild black hole is governed by isomorphic confinement physics operating at cosmological scale---not via impedance mismatch, but via a **lattice phase transition**.

### Symmetric Gravity and Saturation

As established in Chapter ch:relativity, gravity is a refractive gradient: the local refractive index increases with proximity to a mass source. The principal radial strain from Axiom 4 is:

> **[Resultbox]** *Principal Radial Strain*
>
> $$
> \varepsilon_{11}(r) = \frac{7\,G\,M}{c^2\,r}
> $$

where the factor 7 emerges from the Machian stress boundary $T_{max} = c^4/(7G)$.

Critically, gravity is **Symmetric** in the **EM-transverse channel**: the characteristic impedance $Z_{EM}(r) = \sqrt{\mu'(r)/\varepsilon'(r)} = Z_0$ is *invariant* at all radii, because both $\mu'$ and $\varepsilon'$ scale identically with $n(r)$. There is **no EM impedance mismatch** and **no EM reflection coefficient** ($\Gamma_{EM} = 0$ everywhere under SYM scaling). Per the three-impedance law (field-symbol registry §3.11), $Z_0 \equiv Z_{EM}$ only; shear and bulk channels carry separate impedances $Z_{shear}$ and $Z_{bulk}$.

The electron's confinement is **bulk-channel** TIR ($Z_{bulk} \to 0 \Rightarrow \Gamma_{bulk} = -1$ at the knot core). The black hole's confinement at $r_{\text{sat}}$ is **shear- and bulk-channel** phase transition ($G_{shear} \to 0$, $c_{bulk} \to 0$) while the EM channel remains matched ($\Gamma_{EM} = 0$). See [`bulk-impedance-at-saturation-boundary.md`](bulk-impedance-at-saturation-boundary.md) for the astrophysical $Z_{bulk}$ assignment.

### The Saturation Boundary as a Phase Transition

When $\varepsilon_{11}(r) = 1$ (at $r_{sat} = 7\,M_g = 3.5\,r_s$), the lattice reaches its **elastic limit**. Beyond this radius, the lattice undergoes a phase transition:

- The shear modulus $G_{shear} \to 0$ (topology melts)
- The group velocity $c_g = c(1-\varepsilon^2)^{1/4} \to 0$ (energy freezes)
- Gravitational waves, being *transverse shear waves*, **cannot propagate** in the ruptured interior

The saturated interior therefore acts as a **perfect reflector for shear waves**. The phase transition eliminates the shear restoring force ($G_{shear} \to 0$, $c_{shear} \to 0$), which **is** a shear-channel impedance collapse: $Z_{shear} = \rho\,c_{shear} \to 0 \Rightarrow \Gamma_{shear} = -1$ (Op3). The earlier "not through impedance mismatch" wording predated the three-impedance-law channel subscripts (vocab audit §4b #3); the solid--liquid-boundary analogy is exactly $Z_{shear} \to 0$ at the interface.

| **Property** | **Electron** | **Black Hole** |
|---|---|---|
| Confinement Boundary | $\ell_{node} \approx 3.86 \times 10^{-13}$ m | $r_{sat} = 7\,GM/c^2 = 3.5\,r_s$ |
| Confinement Mechanism | Bulk TIR ($\Gamma_{bulk} = -1$, $Z_{bulk} \to 0$) | Shear + bulk phase transition ($\Gamma_{shear} = \Gamma_{bulk} = -1$; $\Gamma_{EM} = 0$) |
| "Ground-State" Orbital | Bohr radius $a_0 = \ell_{node}/\alpha$ | Saturation cavity $r_{eff} = 49M_g/9$ |
| Shell Gaps | Spectral emission lines | Accretion disk QPOs |
| Interior Physics | Constructive (topology preserved) | Destructive (topology melts) |
| Impedance (per channel) | $Z_{bulk} \to 0$ at knot core | $Z_{EM} = Z_0$ (SYM); $Z_{shear}, Z_{bulk} \to 0$ at $r_{\text{sat}}$ |

---
