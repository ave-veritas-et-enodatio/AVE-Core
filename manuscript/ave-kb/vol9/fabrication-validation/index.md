[↑ Vol 9: Axiomatic Hardware](../index.md)

# Fabrication & Validation

Physical realization, declarative compilation, compiler results, performance benchmarking, and the APU capstone specification. Covers substrate selection (PTFE/SOI/SiN), the atopile declarative hardware compiler, the 21-stage compilation audit, the 10-metric AVE Performance Lexicon, and the formal engineering specification with falsification predictions.

## Key Results

| Result | Statement |
|---|---|
| Substrate Selection | SOI Photonics ($\tan\delta = 0.0001$) is the only viable substrate at $f_{CC} = 1.832\,\text{THz}$; FR-4 melts at 4.4 kW [Ch.23](./ch23-physical-fabrication/substrate-selection.md) |
| Declarative Compilation | atopile projects nonlinear continuum mathematics directly onto parametrized industrial components [Ch.24](./ch24-declarative-compilation/atopile-integration.md) |
| 21 Compiler Stages Pass | All 21 compilation stages validated; real JLCPCB components sourced [Ch.25](./ch25-compilation-results/compiler-stage-audit.md) |
| IEEE 287 Passivity Paradox | S-matrix singular value > 1.0 is the definitive signature of topodynamic computation, not a model error [Ch.25](./ch25-compilation-results/ieee-287-passivity-note.md) |
| $f_{CC} = 1.832\,\text{THz}$ | Carrier Coherence Frequency = cavity eigenvalue $c_0/(2L\sqrt{\kappa})$ at SOI 3nm node [Ch.26](./ch26-performance-benchmarking/carrier-coherence-frequency.md) |
| $P_{drag} = 19.8\,\text{W}$ | Viscous Drag Loss $\propto \omega\mu\kappa\tan\delta$ — within 250 W socket budget at SOI [Ch.26](./ch26-performance-benchmarking/viscous-drag-loss.md) |
| $M_{GISA} = 14$ | Spatial Opcode Multiplicity = 14 concurrent harmonic channels at 1.2 mm pitch [Ch.26](./ch26-performance-benchmarking/spatial-opcode-multiplicity.md) |
| APU Spec Sheet | 10-metric formal specification derived exclusively from Axioms 1–4 [Ch.27](./ch27-capstone/apu-spec-sheet.md) |
| 3 Falsification Predictions | Phase coherence threshold, focal isolation, viscous drag linearity [Ch.27](./ch27-capstone/falsification-predictions.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Ch.23: Physical Fabrication](./ch23-physical-fabrication/index.md) | Substrate options (PTFE/SOI/SiN), phase dispersion characterization |
| [Ch.24: Declarative Compilation](./ch24-declarative-compilation/index.md) | atopile integration, physics→BOM pipeline |
| [Ch.25: Compilation Results](./ch25-compilation-results/index.md) | 21-stage compiler audit, IEEE 287 passivity paradox |
| [Ch.26: Performance Benchmarking](./ch26-performance-benchmarking/index.md) | 10-metric AVE Performance Lexicon, SOI/FR-4 comparison |
| [Ch.27: Capstone](./ch27-capstone/index.md) | APU specification sheet, falsification predictions, forward engineering path |
