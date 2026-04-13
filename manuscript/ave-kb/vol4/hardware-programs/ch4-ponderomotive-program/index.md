[↑ Hardware Programs](../index.md)

# Ch.4 The Ponderomotive Program: From PCBA to Quartz

This chapter chronicles the engineering evolution from the original PONDER-01 asymmetric PCBA concept to the thermally viable PONDER-05 DC-biased quartz configuration. The PONDER-01 architecture suffers a fatal thermal limitation ($P_{diss} \approx 250$ W/mm$^3$ at VHF), which forces a design pivot to DC bias near $V_{yield}$ with modest AC perturbation.

## Key Results

| Result | Statement |
|---|---|
| PONDER-01 thrust prediction | $F_{thrust} = k_{topo} \cdot A_{electrode} \cdot \varepsilon_0 \nabla |\mathbf{E}|^2 \approx 45\;\mu$N |
| Dielectric dissipation | $P_{diss} = \omega C V_{rms}^2 \tan\delta$ |
| BaTiO$_3$ thermal load | $\approx 250$ W/mm$^3$ at 100 MHz (CW impossible) |
| Quartz thermal load | $\approx 0.001$ mW at 50 kHz (CW indefinite) |
| PONDER-05 predicted thrust | $469\;\mu$N at 30 kV DC + 500 V AC |

## Derivations and Detail

| Document | Contents |
|---|---|
| [PCBA to Quartz Evolution](pcba-to-quartz-evolution.md) | PONDER-01 concept; thermal catastrophe; PONDER-05 pivot; regime comparison |
| [VHF Drive Topology](vhf-drive-topology.md) | Bistatic parallax offset mode |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---
