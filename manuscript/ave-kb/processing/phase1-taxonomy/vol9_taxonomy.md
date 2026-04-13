# Vol 9 Taxonomy — Axiomatic Hardware (APU)

**Generated:** 2026-04-12
**Based on:** `processing/phase0-surveys/vol9_survey.md`

## Hierarchy Design

```
vol9/
├── index.md                                    (volume index)
├── foundations/                                 (Ch 1–3: motivation + framework)
│   ├── index.md                                (domain index)
│   ├── ch01-von-neumann-wall/
│   │   ├── index.md                            (chapter index)
│   │   └── von-neumann-limits.md               (leaf: drift, tunneling, Landauer)
│   ├── ch02-vca-translation/
│   │   ├── index.md                            (chapter index)
│   │   ├── logic-translation.md                (leaf: XOR gates → Y-junctions)
│   │   ├── amplification-translation.md        (leaf: transistor → geometric triode)
│   │   ├── component-translation.md            (leaf: diode, delay, memory, routing, storage)
│   │   └── unified-translation-directory.md    (leaf: full longtable)
│   └── ch03-vacuum-thermodynamics/
│       ├── index.md                            (chapter index)
│       └── landauer-topological-erasure.md     (leaf: phonon decay, avalanche, baffles)
│
├── primitive-elements/                          (Ch 4–10: individual VCA components)
│   ├── index.md                                (domain index)
│   ├── ch04-geometric-diodes/
│   │   ├── index.md
│   │   └── dielectric-rupture-gating.md        (leaf: S(V)→0, Γ→−1 proof)
│   ├── ch05-geometric-triodes/
│   │   ├── index.md
│   │   ├── quadrature-strain-superposition.md  (leaf: V_total derivation)
│   │   ├── transconductance-gain.md            (leaf: gain formula + linearity)
│   │   └── triode-jax-validation.md            (leaf: simulation results)
│   ├── ch06-dielectric-delay-lines/
│   │   ├── index.md
│   │   ├── slow-wave-derivation.md             (leaf: Telegraphist eqs → v_ph)
│   │   ├── group-velocity-preservation.md      (leaf: dispersion analysis)
│   │   └── delay-line-jax-validation.md        (leaf: simulation results)
│   ├── ch07-strain-reservoirs/
│   │   ├── index.md
│   │   ├── klopfenstein-reservoir-profile.md   (leaf: taper design)
│   │   ├── energy-density-derivation.md        (leaf: stored strain energy)
│   │   └── reservoir-jax-validation.md         (leaf: simulation results)
│   ├── ch08-static-soliton-kinks/
│   │   ├── index.md
│   │   ├── sine-gordon-derivation.md           (leaf: Axiom 4 → sine-Gordon)
│   │   ├── write-read-protocol.md              (leaf: kink creation/readout)
│   │   └── soliton-jax-validation.md           (leaf: simulation results)
│   ├── ch09-axiomatic-transducers/
│   │   ├── index.md
│   │   ├── impedance-matching-proof.md         (leaf: 50Ω → 377Ω, Γ_step)
│   │   └── transducer-jax-validation.md        (leaf: Klopfenstein sim)
│   └── ch10-topological-pumps/
│       ├── index.md
│       └── continuous-wave-injection.md        (leaf: pump architecture)
│
├── system-architecture/                         (Ch 11–17: system-level integration)
│   ├── index.md                                (domain index)
│   ├── ch11-phase-locked-routing/
│   │   ├── index.md
│   │   └── curved-waveguide-routing.md         (leaf)
│   ├── ch12-rf-topological-routing/
│   │   ├── index.md
│   │   └── legacy-digital-interfacing.md       (leaf)
│   ├── ch13-geometric-multiplexing/
│   │   ├── index.md
│   │   └── focal-beam-addressing.md            (leaf: O(1) RAM)
│   ├── ch14-topological-clocks/
│   │   ├── index.md
│   │   └── native-ring-oscillator.md           (leaf)
│   ├── ch15-phase-degeneracy-restoration/
│   │   ├── index.md
│   │   └── adler-injection-locking.md          (leaf: passive ECC)
│   ├── ch16-fluidic-substrate-logic/
│   │   ├── index.md
│   │   └── tesla-valve-analogues.md            (leaf)
│   └── ch17-topological-logic/
│       ├── index.md
│       └── xor-not-waveguide-gates.md          (leaf)
│
├── computation/                                 (Ch 18–22: instruction + ALU + core)
│   ├── index.md                                (domain index)
│   ├── ch18-geometric-instruction-set/
│   │   ├── index.md
│   │   └── gisa-subharmonic-opcodes.md         (leaf: diffraction ISA)
│   ├── ch19-tensor-plates-alu/
│   │   ├── index.md
│   │   └── passive-matrix-multiplication.md    (leaf)
│   ├── ch20-apu-core-topology/
│   │   ├── index.md
│   │   └── monolithic-computation-plane.md     (leaf)
│   ├── ch21-apu-boundary-interfaces/
│   │   ├── index.md
│   │   ├── lambda-matching-stages.md           (leaf: impedance coupling)
│   │   └── serdes-geometry-converter.md        (leaf: digital↔geometric)
│   └── ch22-apu-design-methodology/
│       ├── index.md
│       └── fdtd-to-ato-workflow.md             (leaf: design pipeline)
│
└── fabrication-validation/                      (Ch 23–27: physical realization + benchmarks)
    ├── index.md                                (domain index)
    ├── ch23-physical-fabrication/
    │   ├── index.md
    │   ├── substrate-selection.md              (leaf: PTFE/SOI/SiN comparison)
    │   └── phase-dispersion-characterization.md (leaf: fabrication tolerances)
    ├── ch24-declarative-compilation/
    │   ├── index.md
    │   └── atopile-integration.md              (leaf: physics→BOM)
    ├── ch25-compilation-results/
    │   ├── index.md
    │   ├── compiler-stage-audit.md             (leaf: 21 stages pass)
    │   └── ieee-287-passivity-note.md          (leaf: passivity paradox)
    ├── ch26-performance-benchmarking/
    │   ├── index.md
    │   ├── carrier-coherence-frequency.md      (leaf: f_CC = c/(2L√κ))
    │   ├── viscous-drag-loss.md                (leaf: P_drag ∝ ω)
    │   ├── spatial-opcode-multiplicity.md      (leaf: M_GISA)
    │   └── performance-lexicon-summary.md      (leaf: all 10 metrics table)
    └── ch27-capstone/
        ├── index.md
        ├── apu-spec-sheet.md                   (leaf: formal spec table)
        └── falsification-predictions.md        (leaf: 6 experimental tests)
```

## File Counts

| Domain | Indexes | Leaves | Total |
|--------|:---:|:---:|:---:|
| `vol9/index.md` | 1 | 0 | 1 |
| `foundations/` | 4 | 7 | 11 |
| `primitive-elements/` | 8 | 17 | 25 |
| `system-architecture/` | 8 | 7 | 15 |
| `computation/` | 6 | 7 | 13 |
| `fabrication-validation/` | 6 | 11 | 17 |
| **TOTAL** | **33** | **49** | **82** |

## Ell Convention

Vol 9 source contains **zero** instances of either `$\ell_{node}$` or `$l_{node}$`. Per Phase 1 decision, all new KB content will use **script ell** `$\ell_{node}$` (dominant convention).

## PATH-STABLE Candidates

No other volumes currently reference Vol 9 content. No PATH-STABLE annotations are required at this time. Future Vol 4 cross-refs to the VCA Translation Matrix or Performance Lexicon would warrant PATH-STABLE on:
- `vol9/foundations/ch02-vca-translation/unified-translation-directory.md`
- `vol9/fabrication-validation/ch26-performance-benchmarking/performance-lexicon-summary.md`

## CLAUDE.md Invariant Candidates

Potential new cross-cutting invariants from Vol 9:
1. **VCA schematic symbols** — double-line waveguide notation, filled-dot saturation markers (used throughout Vol 9 TikZ figures). Could become INVARIANT-S7 if adopted in other volumes.
2. **APU Performance Lexicon** — 10 metrics (f_CC, P_drag, M_GISA, etc.) with formal AVE names vs classical names. Could become INVARIANT-C5 if referenced outside Vol 9.

**Decision:** Both deferred to Phase 6 cross-reference audit. No CLAUDE.md changes now.

## Naming Conventions

- Volume directory: `vol9/` (consistent with vol1–vol8)
- Domain slugs: lowercase, hyphenated (consistent with existing KB)
- Chapter directories: `ch{NN}-{slug}/` with zero-padded number (consistent with Vol 3, Vol 4)
- Leaf slugs: descriptive, lowercase, hyphenated (consistent)
- No naming collisions with existing vol1–vol8 hierarchy
