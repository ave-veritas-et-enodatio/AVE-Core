[↑ Ch.7 Regime Map](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol1 as sec:domain_catalog -->

## Section 7.2: Domain Control Parameter Catalog

Each domain has a unique physical interpretation of the amplitude $A$ and the critical threshold $A_c$. In every case, $A_c$ is **derived from the four axioms**---it is never a fitted or empirical parameter.

### Electromagnetic (Dielectric)

| | |
|---|---|
| Amplitude $A$ | Applied voltage $V$ |
| Critical $A_c$ | $V_{yield} = \sqrt{\alpha} \cdot V_{snap} = \sqrt{\alpha} \cdot m_e c^2/e \approx 43.65$ kV |
| Control parameter | $r = V / V_{yield}$ |

**Regime locations:**
- Lab capacitor (1 kV): $r = 0.023$ --- Regime I
- HV Capacitor @ 30 kV: $r = 0.687$ --- Regime II
- HV Capacitor @ 43 kV: $r = 0.985$ --- Regime III
- Schwinger pair production: $r = 1.0$ --- Regime IV boundary

### Electromagnetic (Field Strength)

| | |
|---|---|
| Amplitude $A$ | Local electric field $E$ |
| Critical $A_c$ | $E_{yield} = V_{yield}/\ell_{node} \approx 1.13 \times 10^{17}$ V/m |
| Control parameter | $r = E / E_{yield}$ |

At the lattice scale, even extreme laboratory fields ($10^6$ V/m) correspond to $r \sim 10^{-11}$, deep in Regime I. The Schwinger critical field ($E_S = m_e^2 c^3/(e\hbar) \approx 1.32 \times 10^{18}$ V/m) corresponds to $r = E_S/E_{yield} = V_{snap}/V_{yield} = 1/\sqrt{\alpha} \approx 11.7$, deep in Regime IV.

### Gravitational

| | |
|---|---|
| Amplitude $A$ | Principal radial strain $\varepsilon_{11} = 7GM/(c^2 r)$ |
| Critical $A_c$ | Unitary strain = 1 |
| Control parameter | $r = \varepsilon_{11}$ |

The factor of 7 arises from the 7 compliance modes of the K4/SRS lattice ($\nu_{vac} = 2/7$). **Regime locations:**
- Solar surface: $\varepsilon_{11} = 2.1 \times 10^{-6}$ --- Regime I
- White dwarf: $\varepsilon_{11} \approx 3 \times 10^{-4}$ --- Regime I
- Neutron star (1.4 $M_\odot$, $R = 10$ km): $\varepsilon_{11} \approx 1.46$ --- Regime IV
- Black hole at $r_s = 2GM/c^2$: $\varepsilon_{11} = 7/2 = 3.5$ --- Regime IV

*The neutron star result demands attention.* A 1.4 $M_\odot$ star at $R = 10$ km has $\varepsilon_{11} = 1.46 > 1$, placing it in Regime IV (ruptured topology). This is the AVE analog of the Buchdahl limit: no static configuration can have $r < 9GM/4c^2$ (where $\varepsilon_{11} > 63/36 = 1.75$). In AVE, the saturation boundary defines an absolute limit on gravitational compactness --- the lattice topology cannot support strain beyond unity.

> **[Examplebox]** *Evaluating the Gravitational Regime of a Black Hole*
>
> **Problem:** Calculate the dimensionless control parameter $r$ for the gravitational strain at the Event Horizon ($r_s = 2GM/c^2$) of a black hole, and determine its operating regime.
>
> **Solution:** In the gravitational domain, the amplitude $A$ is the principal radial strain $\varepsilon_{11} = 7GM/(c^2 R_{radial})$, where the factor of 7 arises from the 7 compliance modes of the K4 lattice. The critical capacity of the lattice is unitary strain ($A_c = 1$).
> At the Schwarzschild radius $R_{radial} = r_s = 2GM/c^2$:
>
> $$
> r = \frac{A}{A_c} = \frac{7GM/(c^2 \cdot (2GM/c^2))}{1} = \frac{7}{2} = 3.5
> $$
>
> Because $r = 3.5 \ge 1.0$, the local spatial metric has structurally failed. The LC network at the event horizon is in **Regime IV (Ruptured)**, meaning topological coherence is destroyed and local scalar $c_{eff} = 0$.

### BCS / Superconducting

| | |
|---|---|
| Amplitude $A$ | Temperature $T$ (or magnetic field $B$) |
| Critical $A_c$ | $T_c$ (or $B_{c0}$) |
| Control parameter | $r = T/T_c$ |

The BCS relation $B_c(T) = B_{c0}\sqrt{1 - (T/T_c)^2}$ IS the AVE saturation operator, with $A = T$ and $A_c = T_c$. Below $T_c$: superconducting ($S > 0$, Meissner effect active). At $T_c$: normal state ($S = 0$, topology destroyed).

### Magnetic

| | |
|---|---|
| Amplitude $A$ | Applied magnetic field $B$ |
| Critical $A_c$ | $B_{snap} = m_e^2 c^2/(e\hbar) \approx 1.89 \times 10^9$ T |
| Control parameter | $r = B / B_{snap}$ |

Lab magnets ($\sim$10 T) have $r \sim 10^{-8}$ (Regime I). A magnetar surface field ($\sim 10^{10}$ T) has $r \sim 5$ (Regime IV). At $B_{snap}$, the vacuum permeability $\mu_{eff}$ reaches zero --- the vacuum becomes a perfect diamagnet (the Meissner effect of the vacuum itself).

### Nuclear

| | |
|---|---|
| Amplitude $A$ | $d_{sat}/r_{sep}$ (confinement ratio) |
| Critical $A_c$ | 1 (Pauli wall) |
| Control parameter | $r = d_{sat}/r_{sep}$ |

When $r_{sep} > d_{sat}$: $r < 1$, the interaction potential $U(r) = -(K/r)(1 - 2\Gamma^2)$ is attractive (Regime I--III). When $r_{sep} \leq d_{sat}$: $r \geq 1$, $\Gamma \to 1$, the potential becomes repulsive --- this is Pauli exclusion from first principles.

### Gravitational Waves

| | |
|---|---|
| Amplitude $A$ | GW strain $h$ |
| Critical $A_c$ | $h_{yield} = \sqrt{\alpha} \approx 0.0854$ |
| Control parameter | $r = h / \sqrt{\alpha}$ |

LIGO detections ($h \sim 10^{-21}$) correspond to $r \sim 10^{-20}$ --- the most deeply linear measurement in physics. A neutron star merger at the surface ($h \sim 0.01$) reaches $r = 0.117 < \sqrt{2\alpha} = 0.121$ --- still in Regime I. The correction $\Delta S = 0.007 < \alpha$ is sub-$\alpha$ and unresolvable. A strong merger at $h \sim 0.02$ ($r = 0.23$) enters Regime II.

### Galactic Rotation

| | |
|---|---|
| Amplitude $A$ | Newtonian gravitational acceleration $g_N$ |
| Critical $A_c$ | $a_0 \approx 1.2 \times 10^{-10}$ m/s$^2$ |
| Control parameter | $r = g_N / a_0$ |

*Note:* The galactic domain uses the **same** universal operator as every other domain: $S(r \to 1)$ means medium compliance $\to 0$. What differs is the *observational consequence*: in EM, $\varepsilon \to 0$ produces pair production (dramatic). In gravity, $G_{shear} \to 0$ produces an event horizon (dramatic). In the galactic domain, $\eta \to 0$ means the lattice drag *vanishes*, leaving simple Newtonian gravity (unspectacular).

The "dark matter problem" **IS** the Regime III$\to$IV phase transition. At $r = g_N/a_0 \approx 1$, the lattice mutual inductance undergoes the same phase transition as every other domain. "Dark matter" is the drag that exists on the Regime I--III side of this boundary. Inner-galaxy stars at $g_N \gg a_0$ ($r \gg 1$) are in Regime IV: the lattice is fully saturated, drag is zero, orbits are Keplerian. Outer-galaxy stars at $g_N \ll a_0$ ($r \ll 1$) are in Regime I: the lattice is unsaturated, full drag produces $g_{eff} \to \sqrt{g_N \cdot a_0}$ (flat rotation curves).

---
