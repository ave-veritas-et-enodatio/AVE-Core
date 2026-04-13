[↑ Fabrication & Validation](../index.md)

# Axiomatic Performance Lexicon

Every classical semiconductor performance metric is a degenerate special case of a deeper topological invariant. This chapter derives the 10 canonical AVE performance metrics from first principles and provides their explicit correspondence to classical equivalents.

## Key Results

| Result | Statement |
|---|---|
| Carrier Coherence Frequency | $f_{CC} = c_0/(2L\sqrt{\kappa_{topo}}) = 1.832$ THz (SOI, 3nm) |
| Viscous Drag Loss | $P_{drag} = \omega\mu\kappa\tan\delta\int|S|^2 dV = 19.8$ W (SOI at $f_{CC}$) |
| Spatial Opcode Multiplicity | $M_{GISA} = 14$ concurrent harmonic channels (1.2 mm pitch) |
| Focal Lock Time | $\tau_{lock} = 0.07$ ps ($711{,}590\times$ faster than DRAM) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Carrier Coherence Frequency](carrier-coherence-frequency.md) | $f_{CC}$ replaces clock speed |
| [Viscous Drag Loss](viscous-drag-loss.md) | $P_{drag}$ replaces $I^2R$ power dissipation |
| [Spatial Opcode Multiplicity](spatial-opcode-multiplicity.md) | $M_{GISA}$ replaces IPC |
| [Performance Lexicon Summary](performance-lexicon-summary.md) | All 10 metrics in unified table |
