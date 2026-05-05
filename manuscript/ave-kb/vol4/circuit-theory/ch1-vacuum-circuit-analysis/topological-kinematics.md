[↑ Ch.1 Vacuum Circuit Analysis](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: i9l284 -->

## The Topo-Kinematic Circuit Identity

The Vacuum Circuit Analysis (VCA) framework rests upon a single, exact dimensional isomorphism between continuum spatial mechanics and electrical network theory. This section derives the mapping rigorously, verifies it through independent thermodynamic consistency checks, and tabulates the complete translation dictionary.

### Defining the Topological Conversion Constant

The fundamental bridge between electrical and mechanical domains is the **Topological Conversion Constant** $\xi_{topo}$, defined as the ratio of the elementary charge to the spatial lattice pitch:

> **[Resultbox]** *Topological Conversion Constant*
>
> $$
> \xi_{topo} \equiv \frac{e}{\ell_{node}} = \frac{1.602 \times 10^{-19} \text{ C}}{3.862 \times 10^{-13} \text{ m}} \approx 4.149 \times 10^{-7} \text{ C/m}
> $$

This constant carries dimensions of $[\text{C/m}]$ and encodes the physical fact that, in a discrete lattice with pitch $\ell_{node}$, one quantum of electrical charge corresponds to one quantum of spatial displacement. Neither $e$ nor $\ell_{node}$ is adjustable; both are fixed by the lattice axioms (Axioms 1--2).

### Deriving the Six-Row Translation Table

Each row of the Topo-Kinematic identity is derived by substituting $\xi_{topo}$ into the standard SI definition of the electrical quantity and isolating the resulting mechanical observable.

**Row 1: Charge $\leftrightarrow$ Displacement.** Electrical charge is the time integral of current. Substituting the kinematic mapping for current ($I \equiv \xi_{topo}\, v$):

> **[Resultbox]** *Charge--Displacement Identity*
>
> $$
> Q = \int I \, dt = \xi_{topo} \int v \, dt = \xi_{topo}\, x
> $$

Dimensional check: $[\text{C/m}] \times [\text{m}] = [\text{C}]$. $\checkmark$

**Row 2: Current $\leftrightarrow$ Velocity.** Differentiating the charge identity with respect to time:

> **[Resultbox]** *Current--Velocity Identity*
>
> $$
> I = \frac{dQ}{dt} = \xi_{topo}\, \frac{dx}{dt} = \xi_{topo}\, v
> $$

The hardware velocity limit $v_{max} = c$ maps to a maximum circuit current:

$$
I_{max} = \xi_{topo}\, c = 4.149 \times 10^{-7} \times 2.998 \times 10^{8} \approx 124.4 \text{ A}
$$

This is the absolute slew-rate limit of the discrete lattice. No topological current can exceed $124.4$ A because no spatial velocity can exceed $c$.

**Row 3: Voltage $\leftrightarrow$ Force.** Voltage is the energy per unit charge ($V = W/Q$). Substituting $Q = \xi_{topo}\, x$ and $W = \int F\, dx$:

> **[Resultbox]** *Voltage--Force Identity*
>
> $$
> V = \frac{W}{Q} = \frac{\int F\, dx}{\xi_{topo}\, x} \quad \Longrightarrow \quad V = \xi_{topo}^{-1}\, F
> $$

The maximum lattice force is the electromagnetic string tension $T_{EM} = m_e c^2 / \ell_{node} \approx 0.212$ N. The corresponding voltage is:

$$
V_{snap} = \xi_{topo}^{-1}\, T_{EM} = \frac{0.212}{4.149 \times 10^{-7}} \approx 511{,}000 \text{ V} = 511 \text{ kV}
$$

This recovers $V_{snap} = m_e c^2 / e$ exactly, confirming the identity.

**Row 4: Inductance $\leftrightarrow$ Mass.** Inductance opposes changes in current ($V = L\, dI/dt$). Substituting the voltage and current identities:

> **[Resultbox]** *Inductance--Mass Identity*
>
> $$
> V = L \frac{dI}{dt} \quad \Longrightarrow \quad \xi_{topo}^{-1} F = L\, \xi_{topo} \frac{dv}{dt} = L\, \xi_{topo}\, a
> \quad \Longrightarrow \quad L = \xi_{topo}^{-2}\, m
> $$

For the electron: $L_e = \xi_{topo}^{-2}\, m_e = m_e / \xi_{topo}^{2} \approx 5.292 \times 10^{-18}$ H ($\approx 5.3$ aH). This is the equivalent lumped inductance of a single electron's rest mass.

**Row 5: Capacitance $\leftrightarrow$ Compliance.** Capacitance stores charge per unit voltage ($C = Q/V$). Substituting:

> **[Resultbox]** *Capacitance--Compliance Identity*
>
> $$
> C = \frac{Q}{V} = \frac{\xi_{topo}\, x}{\xi_{topo}^{-1}\, F} = \xi_{topo}^{2} \frac{x}{F} = \xi_{topo}^{2}\, \kappa
> $$

where $\kappa = x/F = 1/k$ is the mechanical compliance (inverse spring constant). Dielectric breakdown occurs when the lattice displacement exceeds its absolute yield limit ($x > \ell_{node}$), which is structurally isomorphic to capacitor voltage exceeding the breakdown threshold.

**Row 6: Resistance $\leftrightarrow$ Viscosity.** Resistance dissipates power as $P = I^2 R$. Substituting:

> **[Resultbox]** *Resistance--Viscosity Identity*
>
> $$
> R = \frac{V}{I} = \frac{\xi_{topo}^{-1} F}{\xi_{topo}\, v} = \xi_{topo}^{-2} \frac{F}{v} = \xi_{topo}^{-2}\, \eta
> $$

where $\eta = F/v$ is the mechanical drag coefficient (units: kg/s). When the dielectric saturates and the vacuum enters the zero-impedance slipstream ($\eta \to 0$), the equivalent circuit resistance drops to zero---the hallmark of a superconductor.

### Complete Translation Dictionary

Table consolidates the six identities into a single reference dictionary.

See [Translation Table: Circuit/EE ↔ AVE](../../../common/translation-tables/translation-circuit.md) — this corresponds to `\input{../common/translation_circuit.tex}` in source.

### Self-Consistency Verification

**Work--Energy Theorem.** The physical work done to charge a capacitor is $W = \int V\, dQ$. Substituting the Topo-Kinematic identities:

$$
W = \int (\xi_{topo}^{-1}\, F)(\xi_{topo}\, dx) = \int F\, dx
$$

The $\xi_{topo}$ factors cancel identically, recovering the mechanical work integral with no residual scaling. This proves the mapping is dimensionally exact and energy-conserving.

**Impedance Cross-Check.** The characteristic impedance of free space maps as:

$$
Z_{mech} = \xi_{topo}^{2}\, Z_0 = (4.149 \times 10^{-7})^2 \times 376.73 \approx 6.485 \times 10^{-11} \text{ kg/s}
$$

This is independently verifiable as the acoustic impedance of a single lattice node: $Z_{acoustic} = \rho_{bulk}\, c\, \ell_{node}^2 \approx 7.91 \times 10^6 \times 3.0 \times 10^8 \times (3.86 \times 10^{-13})^2 \approx 3.5 \times 10^{-10}$ kg/s. The factor-of-$\sim 5$ difference arises from the porosity correction ($p_c = 8\pi\alpha \approx 0.183$), confirming that the scaling is structurally consistent within the geometric packing fraction of the lattice.

---
