# Vol 9 Survey — Axiomatic Hardware (APU)

**Generated:** 2026-04-12
**Source:** `manuscript/vol_9_axiomatic_hardware/chapters/` (27 chapters + manifest)

## Overview

Vol 9 documents the complete Axiomatic Processing Unit (APU) — a photonic interference lattice computer derived from the four AVE axioms. It progresses from motivating the departure from Von Neumann architecture, through individual primitive VCA hardware elements, to system-level integration, fabrication, and benchmarking.

**Total source lines:** ~3,035
**Chapters:** 27 (Ch 1–27)
**Resultboxes:** 27 (exactly 1 per chapter — chapter summaries)
**Axiomboxes / Simboxes:** 0
**Objectiveboxes:** 0 (objectives use `\section*{Chapter Objectives}` + `\begin{itemize}`)
**\section{}:** 0 numbered sections (all use `\section*` or `\section` without numbering)
**\label{}:** Concentrated in Ch 5–9, 23, 25–27 (technical chapters with equations)
**Figures:** TikZ diagrams (Ch 1–2, 4) + external sim images (Ch 3, 4, 5, 6, 7, 8, 9, 23, 25, 26)

## Cross-References

### Internal (within Vol 9)
- Ch 10 → Ch 14 (topological clocks), Ch 9 (transducers), Ch 17 (topological logic)
- Ch 13 → Ch 8 (soliton kinks), Ch 21 (boundary interfaces)
- Ch 18 → Ch 19 (tensor plates ALU)
- Ch 26 → Ch 18 (GISA), Ch 13 (geometric MUX), Ch 15 (phase degeneracy), Ch 8 (soliton kinks)
- Ch 27 → Ch 1, 10, 13, 15, 18, 9, 8 (comprehensive capstone references)
- Ch 9 → Ch 2 (VCA translation)

### External (to other volumes)
- Ch 2 → Appendix D (VCA symbols) via `\ref{app:vca_symbols}`
- Ch 3 → Ch 16 via `\ref{ch:fluidic_substrate_logic}` (internal, but conceptually links to Vol 3 dark matter)
- **No other volumes reference INTO Vol 9** (confirmed by grep)

## Per-Chapter Inventory

| Ch | Lines | Title | Key Content | Est. Leaves |
|:---:|:---:|-------|-------------|:---:|
| 1 | 72 | Von Neumann Wall | Drift velocity, tunneling, Landauer bound, TikZ figure | 1 |
| 2 | 426 | Topo-Kinematic Rosetta Stone | 8 TikZ comparison figures + full translation longtable (8 rows) | 3–4 |
| 3 | 56 | Vacuum Thermodynamics | Landauer in VCA, phonon scattering, thermal avalanche, geometric baffles | 1 |
| 4 | 54 | Geometric Diodes | S(V)→0 proof, Γ→−1 reflection, sim figure | 1 |
| 5 | 203 | Geometric Triodes | 5 subsections, quadrature strain, transconductance gain, JAX validation | 3 |
| 6 | 224 | Dielectric Delay Lines | 6 subsections, slow-wave derivation, group velocity, JAX figure | 3 |
| 7 | 231 | Strain Reservoirs | 5 subsections, Klopfenstein taper, energy density, JAX figure | 3 |
| 8 | 229 | Static Soliton Kinks | 5 subsections, sine-Gordon derivation, write/read protocol, JAX figure | 3 |
| 9 | 174 | Axiomatic Transducers | 3 subsections, Klopfenstein profile, 50Ω→377Ω matching, JAX figure | 2 |
| 10 | 47 | Topological Pumps | Continuous wave pump vs DC supply, distribution cascades | 1 |
| 11 | 46 | Phase-Locked Routing | Curved waveguide routing, impedance matching | 1 |
| 12 | 47 | RF Topological Routing | Legacy digital interfacing, harmonic synthesis | 1 |
| 13 | 52 | Geometric Multiplexing | O(1) RAM via beam interference focal addressing | 1 |
| 14 | 40 | Topological Clocks | Native closed-loop timing, no external crystal | 1 |
| 15 | 54 | Phase Degeneracy Restoration | Passive error correction via Adler injection locking | 1 |
| 16 | 50 | Fluidic Substrate Logic | Tesla valve analogy, macroscopic fluid scaling | 1 |
| 17 | 36 | Topological Logic | XOR/NOT gate realizations via waveguide interference | 1 |
| 18 | 51 | Geometric Instruction Set | GISA — sub-harmonic opcode encoding, diffraction ISA | 1 |
| 19 | 48 | Tensor Plates ALU | Passive refractive matrix multiplication | 1 |
| 20 | 46 | APU Core Topology | Monolithic computation plane, no Von Neumann bus | 1 |
| 21 | 94 | APU Boundary Interfaces | λ-matching stages, 50Ω coupling, SerDes | 2 |
| 22 | 70 | APU Design Methodology | Wave-mechanics development workflow, FDTD→ato | 1 |
| 23 | 111 | Physical Fabrication | Substrate options (PTFE/SOI/SiN), phase dispersion | 2 |
| 24 | 33 | Declarative Compilation | atopile integration, physics→BOM pipeline | 1 |
| 25 | 106 | Compilation Results | 21 compiler stages pass, real BOM, IEEE 287 note | 2 |
| 26 | 215 | Performance Benchmarking | 10 AVE Performance Lexicon metrics, SOI/FR-4 comparison | 4 |
| 27 | 122 | Capstone | Spec sheet, 6 validation suites recap, falsification predictions | 2 |

**Estimated total leaves:** ~43 (+ 6 index files = ~49 files)

## Structural Notes

1. Most chapters (10–17, 18–20, 24) are short (36–52 lines) with a single resultbox → 1 leaf each
2. Ch 2 (VCA Translation) is by far the longest (426 lines) with 8 TikZ figures → split into 3–4 leaves
3. The technical core (Ch 5–9) averages ~210 lines with multiple subsections → 2–3 leaves each
4. Ch 26 (Performance Benchmarking) has 11 subsections, 20 `\subsection` entries → 3–4 leaves
5. No `\axiombox`, `\simbox`, or `\objectivebox` environments used (objectives in plain `\section*`)
6. Cross-references are exclusively internal to Vol 9
