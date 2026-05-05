[↑ Silicon Design Engine](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [0hwopi]
-->

# Topological Transistor Mechanics (BJT Gain)

Standard physics relies on statistical particle thermal diffusion models (often involving Boltzmann distributions and hole lifetimes $L_n$, $D_n$) to approximate Bipolar Junction Transistor (BJT) Current Gain ($\beta$). Under the AVE paradigm, transiting currents do not "diffuse"---they strictly propagate as waves across dual coupled macroscopic cavities.

A BJT (e.g., an N-P-N layout) represents dual cascaded boundaries: the Emitter-Base interface ($T^2_{EB}$) and the Base-Collector interface ($T^2_{BC}$). Because modern Emitters are geometrically forced into highly degenerate topological configurations relative to lightly doped Bases, their structural Miller Avalanche multipliers mismatch ($M_E \neq M_B$). The resulting localized grid impedance mismatch ($Z_E \neq Z_B$) selectively chokes the perfect $S_{11}$ transmission baseline.

Instead of computing arbitrary thermal probabilities, the Common-Base gain ($\alpha$) calculates strictly as the cascaded geometric Forward survivability against orthogonal cavity Ground leakage per matrix gap length ($N_{gap}$):

$$\alpha = \left( T^2_{EB} \right)^{N_{gap}}$$

yielding the final pure geometric common-emitter Current Gain ($\beta$):

$$\beta = \frac{\alpha}{1 - \alpha} = \frac{(T^2_{EB})^{N_{gap}}}{1 - (T^2_{EB})^{N_{gap}}}$$

When experimentally validated using asymmetric Miller multiplier limits ($Z_E = 0.35, Z_B = 0.66$), this topological scaling rigorously bounds $\beta$ naturally into the physically observed limits of empirical power electronics ($\beta \approx 10 \to 300$), executed natively from structure with zero thermal statistical assumptions.
