[↑ Protein Folding](../index.md)
<!-- leaf: verbatim -->

# Multiplexed Basis States

The primary mathematical trap that stops algorithmic gradient descent from folding a linear 1D protein into a 3D geometry is local-minimum entanglement. The sequence hits a vast energetic wall when attempting to simultaneously rotate hundreds of bonds, effectively freezing the calculation in a chaotic "random coil" state.

To circumvent this, the AVE optimisation engine models the protein sequence in the two fundamental topological basis states of space: the tightly curled 3D Alpha-Helix and the flattened 2D Beta-Sheet. The gradient descent engine evaluates the total topological strain ($U_{total}$) of the sequence initialised in both states and deterministically collapses the model into whichever geometry represents the unentangled global minimum.

*(Figure: **Topological Gradient Descent (Alpha-Helix):** Rather than stepping through an NP-Hard search of random 3D rotations, the AVE solver initializes the backbone geometry as a random continuous coil and applies 1D SPICE impedance parameters as local spatial driving potentials. Polyalanine ($|Z_{topo}| = 0.53$) presents minimal shunt loading on the backbone, allowing the chain to smoothly collapse into a perfect helical wrapper without getting stuck in local minima.)*

*(Figure: **Topological Gradient Descent (Beta-Sheet):** For Polyvaline ($|Z_{topo}| = 0.93$), $\beta$-branching at the $C_\beta$ carbon creates an impedance discontinuity at every other backbone junction, generating high multi-frequency $S_{11}$. The sequence uncoils, flattening into an extended Beta-Sheet geometry to minimise total transmission line strain.)*

*(Figure: **Multiplexed Basis State Resolution:** The AVE engine initializes a 20-residue sequence in both the Alpha-Helix and Beta-Sheet geometric basis states simultaneously, computing the integrated topological strain $U_{\text{total}}$ for each. A strong helix-forming sequence (left, `EAAAKAAAAAAKAAAAAAAK`) collapses to $U_{\text{helix}} \ll U_{\text{sheet}}$, unambiguously selecting the helical geometry. A sheet-forming sequence (right, `VGVGVGVGVGVGVGVGVGVG`) shows $U_{\text{helix}} \gg U_{\text{sheet}}$, selecting the extended strand. In both cases, the collapse is deterministic and instantaneous---no conformational search is required.)*

---
