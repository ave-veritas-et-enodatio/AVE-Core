[↑ Translation Tables](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "translation reference table; no claim originated here. Substrate-native vocabulary mappings for standard-physics detector-architecture terminology (SQUID, transmon, Josephson junction, transition-edge sensor, superconducting nanowire single-photon detector, avalanche photodiode, photomultiplier, etc.). Most rows are NEW MAPPING because substrate-architecture descriptions of these devices are not yet canonical in AVE-Core. Created 2026-05-26 per ave-discipline-translate v1.1 trigger 6 substrate-native vocabulary discipline."
-->

# Detector Instrumentation ↔ AVE Substrate-Architecture Translation

<!-- label: tab:trans_instrumentation -->

Standard-physics detector vocabulary (SQUID, transmon, Josephson junction, transition-edge sensor, superconducting nanowire single-photon detector, avalanche photodiode, photomultiplier, etc.) names device CONSTRUCTIONS — what materials are used, what circuit topologies are built. AVE-substrate-mechanically, each device is a specific boundary-Joule extraction architecture: a particular geometry of substrate boundary aperture, a particular impedance-matching scheme, a particular threshold-triggered amplification chain. This table maps device-construction names to their substrate-architecture descriptions.

**Discipline note (v1.1 trigger 6 origin)**: this table exists because the 2026-05-26 Q-NCLT-1 → Q-AX4-NA-2 adjudication surfaced that the substrate-architecturally-relevant property of a detector (wide-aperture vs narrow-aperture; continuous-flux vs single-event-threshold-triggered; bulk-averaging vs histogram-statistics) was hidden behind the device-construction names. The standard-physics-community lists "single-photon avalanche detectors", "transmons", "TES", "SNSPD" — but the substrate-distinct prediction (Ax 4 saturation amplitude-shape signature at narrow apertures) requires identifying which of these are narrow-aperture-single-event-threshold-triggered architectures. The substrate-architecture column makes the discriminating property explicit.

**Status taxonomy per row**: nearly all rows are **NEW MAPPING** because canonical-leaf integration of substrate-architecture descriptions of standard-physics detectors is sparse in AVE-Core. The closest existing anchors are:

- [`vol3/condensed-matter/ch09-condensed-matter-superconductivity/`](../../vol3/condensed-matter/ch09-condensed-matter-superconductivity/) — superconductivity primitives (Cooper pairs, Meissner, BCS) that underlie most cryogenic detector architectures
- [`vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md`](../../vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md) — transmon qubit Ohmic-damping formalism
- [`vol4/circuit-theory/`](../../vol4/circuit-theory/) — substrate-circuit-analysis chapters (boundary impedance, transmission-line, matched extraction)

## Wide-aperture continuous-flux extractors (Category I)

These average substrate amplitude across a wide boundary aperture and extract energy continuously rather than as discrete threshold-triggered events. Substrate-architecturally they measure bulk averages and are insensitive to per-site substrate amplitude-shape (the central-aggregation across many independent lattice sites washes per-site shape into the quadratic-Lagrangian aggregate — see [`translation-stochastics.md`](translation-stochastics.md) CLT row). The Ax 4 saturation-induced narrow-aperture amplitude-shape prediction is NOT observable in this category.

| **Standard-physics name** | **AVE substrate-architecture** | **Status / Anchor** |
|---|---|---|
| Photodiode (continuous-flux) | Wide-aperture continuous boundary-Joule extractor — substrate amplitude averaged across a large area of boundary lattice sites with Joule extraction at each; the aggregate energy flow is the measured photocurrent | NEW MAPPING |
| Photomultiplier tube (PMT) | Wide-aperture continuous extractor with cascaded threshold-triggered amplification stages — primary extraction at a wide photocathode aperture; downstream dynode stages each apply threshold-triggered amplification to the cascading substrate-amplitude pulse | NEW MAPPING |
| CCD / CMOS imager | Wide-aperture continuous extractor with spatial pixelization — each pixel is a moderately-wide aperture (still large N substrate sites) accumulating boundary-Joule energy over the integration time | NEW MAPPING |
| Bolometer (resistive thermometer) | Wide-aperture continuous extractor measuring substrate-thermal energy aggregate — the resistive element thermalizes incident substrate-mode energy and reads out via temperature shift | NEW MAPPING |

## Narrow-aperture single-event threshold-triggered extractors (Category II)

These extract energy via threshold-triggered single events at narrow boundary apertures — each event is a discrete threshold-crossing where the substrate amplitude exceeds a sharp threshold and triggers a downstream amplification chain. Substrate-architecturally, this category is where per-site amplitude-shape survives to the aperture-aggregate (when the aperture spans few independent substrate lattice sites). The Ax 4 saturation-induced narrow-aperture amplitude-shape prediction is potentially observable HERE if substrate operating conditions also reach the saturation regime (high $V/A_c$).

| **Standard-physics name** | **AVE substrate-architecture** | **Status / Anchor** |
|---|---|---|
| Avalanche photodiode (APD) | Narrow-aperture threshold-triggered extractor with substrate-saturation-driven cascading amplification — primary extraction at a narrow boundary aperture (small N substrate sites); the substrate amplitude at the aperture triggers an avalanche when it crosses the threshold near substrate saturation onset $A_c$ | NEW MAPPING — Ax 4 saturation kernel directly relevant to the avalanche cascade mechanism |
| Single-photon avalanche diode (SPAD) | Same substrate-architecture as APD but operated in Geiger mode: substrate amplitude at narrow boundary aperture biased near saturation onset; each threshold-crossing event is a single-photon-energy quantum extraction | NEW MAPPING — substrate-saturation × narrow-aperture confluence; primary candidate for Ax 4 amplitude-shape prediction observability |
| Transition-edge sensor (TES) | Narrow-aperture threshold-triggered extractor at superconducting-to-normal transition — the substrate at the sensor aperture sits at the impedance transition (matched-to-normal), and incident substrate-mode energy pushes it across the transition; the substrate-architecture is narrow-aperture per design (small absorber volume) | NEW MAPPING — Ax 4 saturation kernel at substrate boundary impedance transition |
| Superconducting nanowire single-photon detector (SNSPD) | Narrow-aperture threshold-triggered extractor at superconducting hotspot formation — incident substrate-mode amplitude at narrow nanowire aperture (literally narrow in lattice-site units; nanowire width ~ 100 nm ~ 250-2500 substrate lattice sites depending on substrate-correlation length per Q-AX4-NA-3) triggers a hotspot that breaks superconductivity and produces a voltage pulse | NEW MAPPING — substrate-architecturally the closest to the substrate-saturation × narrow-aperture confluence; primary candidate for Ax 4 amplitude-shape prediction observability |
| Microwave kinetic inductance detector (MKID) | Narrow-aperture continuous-monitoring extractor (hybrid category) — substrate-mode amplitude monitored continuously via inductance shift in a narrow superconducting strip; events that push the substrate into saturation regime briefly produce detectable inductance excursions | NEW MAPPING |

## Quantum-information-substrate extractors (Category III)

These devices use substrate-mode coupling to coherent extraction-architecture (the standard community calls these "qubits"); substrate-architecturally they are matched-impedance bidirectional substrate-mode coupling structures, not one-way extraction architectures like Categories I-II. The Ax 4 saturation-induced amplitude-shape prediction does NOT directly apply (these are not one-way Joule extractors) but they have their own substrate-architecture observables.

| **Standard-physics name** | **AVE substrate-architecture** | **Status / Anchor** |
|---|---|---|
| Superconducting qubit (generic) | Matched-impedance bidirectional substrate-mode coupling structure — a substrate region with engineered impedance discontinuity that hosts a localized substrate-mode resonance (the "qubit" state); coupling to substrate boundary-mode is via impedance-matched transmission line | NEW MAPPING |
| Transmon qubit | Specific superconducting qubit topology with Josephson-junction-mediated impedance discontinuity; the substrate-mode resonance lives in the Josephson-junction nonlinear inductance against shunt capacitance | **PARTIAL CANONICAL**: [`vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md`](../../vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md) covers transmon Ohmic-damping (T1/T2 decoherence) substrate-mechanics; full substrate-architecture description pending |
| Josephson junction (JJ) | Substrate-impedance discontinuity at the boundary between two phase-locked-substrate regions (the standard community calls these "superconductors") separated by a thin barrier; substrate-architecturally the JJ is the canonical small-area substrate-impedance-mismatch element | NEW MAPPING — Vol 3 Ch 9 superconductivity primitives apply directly |
| SQUID (superconducting quantum interference device) | Two parallel Josephson-junction substrate-impedance-discontinuities forming a flux-sensing loop — substrate magnetic-flux through the loop modulates the impedance of the parallel JJ pair via substrate-mode phase relations | NEW MAPPING |
| RF-SQUID amplifier | SQUID configured as boundary-amplification element — the SQUID's flux-dependent impedance is read out via RF substrate-mode coupling; substrate-architecturally a narrow-aperture sensitive impedance monitor | NEW MAPPING |

## Cryogenic substrate-mode microscopes (Category IV)

These are not "detectors" in the click-rate sense but are substrate-architecture measurement tools that map substrate properties across position or operating condition.

| **Standard-physics name** | **AVE substrate-architecture** | **Status / Anchor** |
|---|---|---|
| Scanning tunneling microscope (STM) | Atomic-scale substrate-boundary tunneling-impedance probe — the STM tip forms an extremely narrow (single-atom or few-atom) substrate-boundary impedance with the sample; tunneling current is substrate-mode amplitude leaking across the boundary | NEW MAPPING — substrate-architecturally CRITICAL for narrow-aperture geometric accessibility per Q-AX4-NA-2 |
| Atomic force microscope (AFM) | Mechanical substrate-displacement probe with Cosserat-coupling readout — the AFM cantilever measures substrate's mechanical (K4 + Cosserat) response at the tip-sample boundary | NEW MAPPING — Cosserat-substrate canonical applies; Vol 1 substrate primitives |
| Electron microscope (TEM/SEM) | Substrate-mode (electron-as-unknot) imaging via wide-aperture substrate-mode propagation through sample — uses the substrate's matter-wave (substrate-mode) properties to image | NEW MAPPING |

## Discipline implications

This table grounds the substrate-architecture column that the Q-AX4-NA-2 adjudication needs. The substrate-distinct vs substrate-agnostic distinction surfaced in `_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md` becomes operationalizable through this table: identify which Category II detectors operate at high $V/A_c$ (saturation regime; APD, SPAD, TES, SNSPD all candidates) AND span few enough independent substrate lattice sites for per-site amplitude-shape to survive aggregation.

**Example (OK pattern, applies trigger 6)**:
"Single-photon avalanche detectors are narrow-aperture threshold-triggered extractors with substrate-saturation-driven cascading amplification (the standard community names this architecture 'SPAD'). The substrate amplitude at the aperture is biased near the substrate saturation onset $A_c$..."

**Example (NOT OK pattern)**:
"SPADs are single-photon detectors in Geiger mode operating near breakdown with high gain." (Standard-physics vocabulary used as primary description; substrate-architecture hidden behind device-construction labels.)

## Canonical home gaps surfaced by this table

Most rows are NEW MAPPING. Candidate Phase 2-A.5-style follow-on workstreams that could establish canonical homes:

- **Category I + II substrate-architecture taxonomy** — single canonical leaf in vol3 or vol4 mapping standard detector technologies to substrate-architecture descriptions; would close Section I-II rows
- **Transmon / qubit substrate-architecture** — extend [`transmon-decoherence.md`](../../vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md) with the substrate-architecture framing for qubit-as-substrate-mode-resonance
- **STM substrate-boundary tunneling-impedance** — substrate-mechanical canonical leaf would close this row and provide the substrate-architecture for narrow-aperture experimental geometry (relevant to Q-AX4-NA-2)

These follow-ons are not in scope for this translation table but flagged here for future epic seeding.

## Cross-references

- **Companion translation tables**: [`translation-stochastics.md`](translation-stochastics.md) for stochastics vocabulary that underlies measurement-process at detectors; [`translation-qm.md`](translation-qm.md) Section B for measurement-process QM vocabulary that maps to these device architectures; [`translation-circuit.md`](translation-circuit.md) for boundary-impedance vocabulary that underlies all extractor architectures; [`translation-condensed-matter.md`](translation-condensed-matter.md) for superconductivity primitives underlying cryogenic detector categories
- **Substrate-architecture canonical anchors**: [`vol3/condensed-matter/ch09-condensed-matter-superconductivity/`](../../vol3/condensed-matter/ch09-condensed-matter-superconductivity/) (Cooper pairs, Meissner, BCS); [`vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md`](../../vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md) (transmon Ohmic-damping); [`vol4/circuit-theory/`](../../vol4/circuit-theory/) (boundary-impedance + transmission-line + matched-extraction primitives)
- **Sibling epic surfaced by this discipline**: [`_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md`](../../../../_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md) — Q-AX4-NA-2 (boundary-extraction architecture × substrate-correlation-length adjudication) directly consumes this table to identify candidate observable-regime devices
- **Discipline anchor**: `ave-discipline-translate` v1.1 trigger 6 — this table IS the lookup infrastructure for detector-architecture vocabulary substitution during prose composition
