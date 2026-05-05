[↑ Ch.8 Applied Fusion](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: qagkgy -->

## Critical Metric Compression Threshold

Setting $V_{topo}(n^*) = V_{yield}$ yields the critical compression threshold:

> **[Resultbox]** *Critical Metric Compression Threshold*
>
> $$
> n^* = \left(\frac{V_{topo,0}}{V_{yield}}\right)^{1/3} = \left(\frac{60{,}340}{43{,}650}\right)^{1/3} \approx \mathbf{1.114}
> $$

A lattice density enhancement of merely $11\%$ is sufficient to suppress the D-T collision strain below the vacuum yield limit. At $n^* = 1.114$:

- The effective Bohr radius compresses from $0.529$ A to $0.475$ A ($90\%$ of free-space).
- The required ignition temperature drops from $15$ keV to $12.1$ keV ($81\%$ of free-space).
- The saturation factor remains $S > 0$, and the Strong Nuclear Force stays active throughout the collision.

### Why Fusion Works in the Sun but Not on Earth

The Sun's core fuses protons via the pp-chain at only $\sim 1.35$ keV---an order of magnitude below the $15$ keV D-T requirement of terrestrial Tokamaks. Yet a $1.35$ keV proton-proton collision generates only $V_{topo} \approx 0.5$ kV in free-space, far below $V_{yield}$.

The answer lies in *density*, not temperature. The solar core operates at $n_e \approx 1.5 \times 10^{32}$ m$^{-3}$---twelve orders of magnitude denser than a Tokamak ($n_e \approx 10^{20}$ m$^{-3}$). At this density, the Debye screening length collapses to:

$$
\lambda_D = \sqrt{\frac{\varepsilon_0 k_B T}{n_e e^2}} \approx 22~\text{pm}
$$

This confines the Coulomb repulsion to a volume smaller than the classical turning distance, dramatically lowering the effective collision strain.

| **Parameter** | **Solar Core** | **Tokamak (ITER)** | **AVE Reactor** |
|---|---|---|---|
| Density $n_e$ (m$^{-3}$) | $1.5 \times 10^{32}$ | $1.0 \times 10^{20}$ | engineered |
| Temperature (keV) | 1.35 | 15.0 | 3.75 |
| Debye length $\lambda_D$ | 22 pm | 91 $\mu$m | N/A |
| $V_{topo}$ (kV) | 10.3 | 60.3 | 7.5 |
| $V_{yield}$ (kV) | 43.65 | 43.65 | 43.65 |
| Strong Force | **ACTIVE** | **DISABLED** | **ACTIVE** |
| Fusion outcome | *Sustained* | *Leaks* | *Sustained* |

---
