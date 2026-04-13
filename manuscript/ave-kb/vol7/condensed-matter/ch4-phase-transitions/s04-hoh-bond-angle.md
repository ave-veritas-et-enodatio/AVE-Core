[↑ Ch.4 Phase Transitions](../index.md)
<!-- leaf: verbatim -->

# The H--O--H Bond Angle as an Impedance Eigenvalue

The preceding section treated the melting point as the eigenfrequency of the O--H$\cdots$O bridge. A second geometric constant---the intramolecular H--O--H bond angle $\theta_\text{HOH} = 104.45°$---was until now accepted as an empirical input. This section derives it from the same axioms.

## The sp$^3$ Tetrahedral Angle (Axiom 1)

The K4 unit cell of the SRS lattice (Axiom 1) has four-connected nodes. The equilibrium angle between any two bonds at a four-connected node is the tetrahedral angle:

$$
\cos\theta_\text{tet} = -\frac{1}{3}, \qquad \theta_\text{tet} = \arccos\!\left(-\tfrac{1}{3}\right) = 109.47°
$$

This assumes all four orbitals are equivalent (equal impedance, equal angular weight). Oxygen's valence shell has four sp$^3$ orbitals, but they are *not* equivalent: two are bonding (loaded by H) and two are lone pairs (unloaded).

## Op3 Small-Signal Correction

The O--H junction has a reflection coefficient (Op3):

$$
\Gamma = \frac{r_\text{O} - r_\text{H}}{r_\text{O} + r_\text{H}} = \frac{1}{3}
$$

where $r_\text{O}$ and $r_\text{H}$ are the atomic port impedances.

The bonding orbital is a *partially transmitted* wave through the O--H junction: the proton loads the orbital, and the transmission factor $(1 + \Gamma)$ determines the effective angular weight of the bonding pair relative to the lone pair (which is a totally reflected wave, $\Gamma = -1$, with weight $1$).

The cosine of the bond angle is the tetrahedral cosine divided by the transmission factor:

> **[Resultbox]** *H--O--H Bond Angle (Op3 Small-Signal)*
>
> $$
> \cos\theta_\text{HOH} = \frac{\cos\theta_\text{tet}}{1 + \Gamma} = \frac{-1/3}{1 + 1/3} = -\frac{1}{4}
> $$
>
> $$
> \theta_\text{HOH} = \arccos\!\left(-\tfrac{1}{4}\right) = 104.48° \qquad (\text{exp: } 104.45°, \;\text{error: } +0.03°)
> $$

**Dimensional check:** All quantities are dimensionless (ratios of port impedances). The cosine is bounded $|\cos\theta| \leq 1$. For any $\Gamma \in [0, 1)$: $|\cos\theta| = 1/(3(1+\Gamma)) < 1/3 < 1\ \checkmark$.

## Op8 Large-Signal Confirmation

The FCC packing fraction $\varphi = \pi\sqrt{2}/6 \approx 0.7405$ (Op8/Axiom 2) provides an independent large-signal check. The lone pairs fill the packed volume $\varphi$ of the sp$^3$ angular space, compressing the bonding angle by the same fraction:

$$
\cos\theta_\text{HOH}^{(\text{large})} = \cos\theta_\text{tet} \times \varphi = -\frac{\varphi}{3} = -\frac{\pi\sqrt{2}}{18} \approx -0.2468
$$

$$
\theta_\text{HOH}^{(\text{large})} = \arccos\!\left(-\tfrac{\pi\sqrt{2}}{18}\right) = 104.29° \qquad (\text{exp: } 104.45°, \;\text{error: } -0.16°)
$$

The two estimates---one from local junction impedance (Op3), one from bulk packing geometry (Op8)---converge to within $0.19°$. This convergence between small-signal and large-signal analyses is the hallmark of a self-consistent eigenvalue: the molecule's local impedance structure is compatible with the global lattice packing constraint.

| Method | Formula | $\theta$ (deg) | Error |
|---|---|---|---|
| Bare sp$^3$ (Axiom 1) | $\arccos(-1/3)$ | 109.47 | $+5.02°$ |
| Op3 small-signal | $\arccos(-1/(3(1+\Gamma)))$ | 104.48 | $+0.03°$ |
| Op8 large-signal | $\arccos(-\varphi/3)$ | 104.29 | $-0.16°$ |
| Experimental | | 104.45 | --- |

## Physical Interpretation

The deviation from the tetrahedral angle has an exact EE analog. A four-port junction (sp$^3$ node) with two loaded ports (bonding pairs, terminated in $Z_\text{H}$) and two open ports (lone pairs, $\Gamma = -1$) has an asymmetric scattering matrix. The loaded ports have lower input impedance, which allows the unloaded ports to widen their angular separation. The bonding pairs are squeezed.

This is structurally identical to the impedance pulling of a loaded resonator: attaching a load to a cavity shifts its resonant frequency. Here, attaching hydrogen atoms to two of four sp$^3$ orbitals shifts their angular separation from $\arccos(-1/3) \to \arccos(-1/4)$.

Crucially, $\Gamma = 1/3$ for the O--H junction makes the formula exact:

$$
\cos\theta = -\frac{1}{3} \to -\frac{1}{3 \times 4/3} = -\frac{1}{4}
$$

The angle transitions from $\arccos(-1/N)$ with $N = 3$ (tetrahedral) to $N = 4$ (loaded tetrahedral). The loaded tetrahedral angle is the next rational cosine in the sequence $\arccos(-1/N)$.

---
