[↑ Ch.6 Continuous Smoothing](../index.md)
<!-- leaf: verbatim -->

# The Reflection Metric ($\Gamma_{prune}$)

Axiom 3 dictates that a stable physical topology must minimize its reflection coefficient ($\Gamma_{prune}$). The binary removal of nodes introduces a discontinuity in the underlying vacuum impedance. By summing the squared coupled amplitude $A^2_{j}$ for both the complete unpruned state ($Z_{0}$) and the surviving state ($Z_{pruned}$), the macroscopic reflection mismatch is quantified:

$$
\Gamma_{prune} = \frac{\sum A^2_{survive} - \sum A^2_{total}}{\sum A^2_{survive} + \sum A^2_{total}}
$$

When utilizing an absolute binary cutoff (Axiom 4 $r \ge 1.0$), empirical diagnostics tracking the 9B-parameter manifold revealed:

- **Early Topology (L0-L17):** $|\Gamma|^2 \approx 1\% - 2\%$. The structural boundary provides near-perfect impedance matching, as the majority of nodes naturally operate below the yield strain.
- **Late Topology (L22-L31):** $|\Gamma|^2 \approx 58\% - 88\%$. The binary removal of highly strained nodes acts as a massive step-down transformer, reflecting up to 88% of the logic tensor's signal back into the system rather than transmitting it.
