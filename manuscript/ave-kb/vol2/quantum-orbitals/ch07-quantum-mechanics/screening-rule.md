[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: w6kk5y -->

## The Screening Rule: Two Distinct Physics

Electron–electron interactions enter the TL solver through $Z_{\text{eff}}(r)$ — a piecewise-constant function with steps at each inner shell boundary. Critically, the screening $\sigma$ that determines each step has **two distinct origins**:

1. **Cross-shell screening** (Gauss's law, Axiom 2): Inner electrons fully enclosed by the outer orbit screen their charge:

$$
\sigma_{\text{cross}} = N_{\text{inner}}
$$

Pure electrostatics: enclosed dislocations subtract from $Z$.

2. **Same-shell repulsion** (lattice coupling, Axiom 4): Electrons on the *same* orbit (same-radius figure-8) are at equal footing — neither is inner to the other. Their mutual Coulomb repulsion is modulated by the lattice phase-jitter coupling $J$:

$$
\sigma_{\text{same}} = (N_{\text{same}} - 1) \times J_{\text{shell}}
$$

$J_{1s^2} = \tfrac{1}{2}(1 + p_c) = 0.5917$ from Axiom 4 (§`sec:lattice_js2`).

The combined rule:

> **[Resultbox]** *AVE Screening Rule*
>
> $$
> \sigma_{\text{total}} = \underbrace{N_{\text{inner}}}_{\text{Gauss (Axiom 2)}} + \underbrace{(N_{\text{same}} - 1) \times J_{\text{shell}}}_{\text{Lattice (Axiom 4)}}
> $$

In the TL solver, $\sigma$ creates a **step in $Z_{\text{eff}}(r)$** at the inner shell radius. This step is an Op3 impedance mismatch that modifies the eigenvalue away from the pure Coulomb value $Z_{\text{eff}}^2 R_y$. The departure is a genuinely new physical effect: the potential is *not* $1/r$ (it has a discontinuity), so the eigenvalue cannot be expressed analytically and must be found by the ABCD cascade.

---
