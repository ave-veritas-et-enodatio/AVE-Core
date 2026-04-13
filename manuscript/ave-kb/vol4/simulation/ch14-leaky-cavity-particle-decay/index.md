[↑ Vol 4: Simulation](../index.md)

# Ch.14: The Leaky Cavity — Simulating Particle Decay

Particle decay reframed as a deterministic analog engineering problem: a topological knot (fermion) modeled as an LC tank circuit whose peak voltage exceeds the $\mathcal{M}_A$ structural yield limit $V_{yield} = 43.65\,\text{kV}$, triggering impedance rupture and exponential RC-discharge.

## Key Results

| Result | Expression | Source |
|---|---|---|
| Stable fermion criterion | Internal topological voltage $< V_{yield}$; LC tank rings indefinitely ($R_{eff} = 1\,\text{G}\Omega$) | theory |
| Unstable fermion (Muon) | $206\times$ electron mass-energy forces standing-wave voltage past $V_{yield}$; switch closes ($R_{eff} = 50\,\Omega$), exponential decay envelope | theory |
| Dielectric environment invariance | Bulk dielectric ($\varepsilon_r$) of surrounding medium cannot alter sub-femtometer $\mathcal{M}_A$ yield limit; decay rate invariant to external medium | theory |
| SPICE netlist | `leaky_cavity.cir` — voltage-controlled switch model with $C = 1\,\text{nF}$, $L = 1\,\text{mH}$, IC $= 150\,\text{kV}$ | netlist |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Theory](theory.md) | Vacuum breakdown voltage; fermions as resonant topologies; RLC avalanche mechanism; environmental modifier analysis |
| [SPICE Netlist](spice-netlist.md) | Verbatim `leaky_cavity.cir` netlist with voltage-controlled switches |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---
