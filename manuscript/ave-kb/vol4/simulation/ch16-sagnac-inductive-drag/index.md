[↑ Vol 4: Simulation](../index.md)
<!-- claim-quality (subtree): cbwd77 -->

# Ch.16: Sagnac Macroscopic Inductive Drag

The Sagnac Effect reframed as Lenz's law operating on the dense $\mathcal{M}_A$ mutual inductance core ($\rho \approx 7.9 \times 10^6\,\text{kg/m}^3$). A rotating mass phase-drags the local inductive capacity $\mu$ of the vacuum LC network, altering the co- and counter-rotating propagation speeds. Simulated as a 50-node discrete LC ring with directional behavioral inductors.

## Key Results

| Result | Expression | Source |
|---|---|---|
| Rotating LC frame | Co-rotating wave: reduced $\mu_{eff}$, faster than $c_0$; counter-rotating wave: increased $\mu_{eff}$, slower than $c_0$ | theory |
| Directional inductor | $L_{eff} = L_0(1 - S_{DRAG})$ if $I > 0$; $L_{eff} = L_0(1 + S_{DRAG})$ if $I < 0$ | netlist |
| SPICE netlist | `sagnac_ring.cir` — 50-node ring, behavioral current source implementing directional inductance | netlist |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Theory](theory.md) | Rotating LC frame mechanism; differential LC ring topology |
| [SPICE Netlist](spice-netlist.md) | Verbatim `sagnac_ring.cir` netlist (single node segment) with behavioral directional inductor |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---
