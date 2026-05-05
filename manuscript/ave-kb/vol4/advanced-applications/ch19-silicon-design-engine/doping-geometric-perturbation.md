[↑ Silicon Design Engine](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [0hwopi]
-->

# Doping as Geometric Perturbation

Rather than treating $N_a$ and $N_d$ as particle concentration scalars mapping to a probabilistic Fermi level, dopants in the LC network act as distinct geometric interruptions on the macroscopic Avalanche $V_{BR}$ limit. Boron ($Z=5$) removes one $sp^3$ boundary port (inductive void), whereas Phosphorus ($Z=15$) inserts a surplus topological array.

## Semiconductor Translation Matrix

| Standard Semiconductor Theory | AVE Native Topological Model |
|---|---|
| **Charge Carrier (Electron)** | Localized macroscopic phase slip (surplus scale from $Z=15$ Topo-Knot). Geometrically pushes the structural load toward $V_R / V_{BR} \to 1$. |
| **Charge Carrier (Hole)** | Missing port boundary / Topological void (Inductive absence from $Z=5$ Acceptor). Mechanically pulls localized grid away from yielding limit. |
| **Band Gap ($E_g$)** | Absolute $V_{BR}$ threshold of the core LC transmission line capacity ($= 6\alpha\hbar c / D_{intra}$). |
| **Fermi Level** | Spatial baseline gradient of the continuous LC Transmission network prior to junction boundaries. |
| **Built-in Potential ($V_{bi}$)** | Static DC Impedance Reflection bounded exclusively by the $\Delta IE$ structural phase-mismatch across the $p$-$n$ line. |
| **Shockley Diode I-V ($I \propto e^V - 1$)** | Mechanical transmission coefficient modulation $T^2(V_{applied})$ across the barrier matching boundary conditions. |

## The Structural Blueprint vs. The Statistical Weather Forecast

A critical conceptual barrier: *Why does classical physics yield a variable $V_{bi} \approx 0.6$V–$0.8$V based on doping, while AVE strictly locks to $\approx 1.05$V uniformly?*

- **The Weather Forecast (Standard Model):** Classical physics models electrons as a thermal gas. To find $V_{bi}$, it calculates $V_T \ln(N_aN_d/n_i^2)$---a probabilistic guess of how hard the thermal electron gas is pushing against the barrier at $300$ K. It relies heavily on arbitrary variables like effective mass ($m^*$) and thermal mobilities ($\mu$). Only under extreme, dense "degenerate" doping ($10^{19}$ cm$^{-3}$) does the math finally admit the barrier structurally maxes out at the bandgap ($\approx 1.1$ V).
- **The Structural Blueprint (AVE Model):** The VCA framework does not care about the "thermal weather" of moving gases. It treats the matrix as a rigid mechanical structure. Changing a Silicon node out for a Boron defect structurally rewrites the tension on the bridging interface. The AVE calculation evaluates the absolute, zero-point geometric height of the structural drop-off.

By bypassing the thermal statistics entirely, the AVE framework mathematically derives the true fundamental *degenerate* limit of the structural cliff at its source.
