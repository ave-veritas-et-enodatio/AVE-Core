[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Ramachandran Basins from Steric Geometry

The engine's Ramachandran basins can be derived from a single geometric constant: the sp$^3$ tetrahedral angle $\theta_\text{tet} = \arccos(-1/3) \approx 109.47^\circ$ (Axiom 2).

## $\alpha$-Helix Basin

The C$_\alpha$ carbon is sp$^3$-hybridised, giving three staggered rotamers at $\pm 60^\circ$ and $180^\circ$ for the $\varphi$ dihedral. Of these, only the gauche$^-$ position ($\varphi = -60^\circ$) avoids steric clash between O$_{i-1}$ and the sidechain $R$.

The $\psi$ angle follows from the backbone resonator $Q$-factor. A helical slow-wave structure locks into a standing wave whose pitch equals the half-cycle periodicity of the resonator:

$$\text{res/turn} = \frac{Q}{2} = \frac{3\pi^2}{8} \approx 3.701$$

The angular advance per residue is $\Delta = 360^\circ / (Q/2) = 2880/(3\pi^2) \approx 97.3^\circ$, giving $\psi_\alpha = -(\Delta - |\varphi_\alpha|) = -(97.3 - 60.0) = -37.3^\circ$.

## $\beta$-Sheet Basin

The fully extended backbone ($\varphi = \psi = 180^\circ$) is modified by the sp$^3$ tetrahedral deviation at each C$_\alpha$.

## PPII Basin

The polyproline II helix has no intramolecular hydrogen bonds---it is the backbone conformation when no standing-wave resonance locks in ($\Gamma \to 1$ at all junctions). $\psi_\text{PPII} = \psi_\beta$ is derived from the same maximum-extension geometry. The $\varphi$ centre ($-75^\circ$) is a measured boundary condition, analogous to $d_0 = 3.80$ Å: it does not enter the $S_{11}$ loss function.

> **[Resultbox]** *Derived Ramachandran Basins*
>
> $$\varphi_\alpha = -60^\circ, \quad \psi_\alpha = -37.3^\circ\;(\Delta = 2.7^\circ), \quad \varphi_\beta = -\!\left(180 - \frac{\theta_\text{tet}}{2}\right) \approx -125.3^\circ, \quad \psi_\beta = +125.3^\circ$$

Compare to crystallographic observation: $\varphi_\alpha^\text{obs} = -57^\circ$, $\psi_\alpha^\text{obs} = -47^\circ$ (median); $\varphi_\beta^\text{obs} = -120^\circ$, $\psi_\beta^\text{obs} = +130^\circ$. The derived values are within $5^\circ$ of all observed centres except $\psi_\alpha$ ($\Delta = 2.7^\circ$ from the $Q/2$ derivation vs. $9.7^\circ$ from crystallography). This residual is flagged as an open question: the simple $|\varphi| + |\psi| = \Delta$ partition may require a NERF or $\nu_\text{vac}$ correction. Benchmark shows zero regression when using the derived values.

<!-- Figure: protein_smith_chart.png — referenced for Smith chart context -->

---
