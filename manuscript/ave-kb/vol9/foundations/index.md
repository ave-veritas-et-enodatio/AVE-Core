[↑ Vol 9: Axiomatic Hardware](../index.md)

# Foundations

Motivates the departure from Von Neumann particle-drift computing by formalizing the three axiomatic physical ceilings (drift velocity saturation, quantum tunneling, Landauer thermodynamic bound). Establishes the Topo-Kinematic translation matrix that maps every classical EE component to an equivalent passive VCA waveguide topology. Addresses information erasure thermodynamics within the APU substrate.

## Key Results

| Result | Statement |
|---|---|
| Von Neumann Wall | Standard particle-drift computation bounded permanently by $v_{sat} \approx 10^7$ cm/s, quantum tunneling at $\sim 20$ atoms, and Landauer's $\Delta Q \geq k_B T \ln 2 \approx 0.017$ eV at 300 K [Ch.1](./ch01-von-neumann-wall/von-neumann-limits.md) |
| Topo-Kinematic Translation | 8-row Rosetta Stone mapping logic, amplification, valving, delay, clocks, memory, routing, and storage from classical EE to VCA waveguide geometry [Ch.2](./ch02-vca-translation/unified-translation-directory.md) |
| Topological Entropic Radiation | Bit deletion in APU converts compressed topology into kinetic lattice phonons at speed $c$; stable soliton kinks resist scattered entropy [Ch.3](./ch03-vacuum-thermodynamics/landauer-topological-erasure.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Ch.1: Von Neumann Wall](./ch01-von-neumann-wall/index.md) | Drift-velocity ceiling, quantum tunneling limit, Landauer thermodynamic bound, axiomatic path forward |
| [Ch.2: VCA Translation Matrix](./ch02-vca-translation/index.md) | Logic gates → Y-junctions, transistors → geometric triodes, diodes → funnels, RC delay → corrugation, flash → soliton kinks, traces → Klopfenstein tapers, capacitors → strain reservoirs, crystals → ring oscillators |
| [Ch.3: Vacuum Thermodynamics](./ch03-vacuum-thermodynamics/index.md) | Landauer erasure in VCA, phonon-skyrmion scattering dynamics, thermal avalanche breakdown, geometric baffles |
