[↑ Translation Tables](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-fy05jc]
-->

# Quantum Mechanics ↔ AVE Translation

<!-- label: tab:trans_qm -->

## Intra-system QM ↔ AVE (Section A: cavity-mode dynamics)

Rows 1--8: same mathematics, different ontology. Row 9: genuinely new AVE prediction.

| **Standard QM** | **AVE Equivalent** | **Relationship** |
|---|---|---|
| Wavefunction $\psi(r)$ | Acoustic cavity mode | Same equation (Helmholtz). AVE: mode of vacuum LC mesh. |
| $|\psi|^2$ probability | Time-averaged trajectory | Density of point-defect sweeping its standing-wave mode. |
| Coulomb potential $e^2/(4\pi\varepsilon_0 r)$ | $\alpha\hbar c / r$ (Axiom 2) | Algebraically identical. $K = \alpha\hbar c$ is the impedance coupling. |
| Bohr radius $a_0$ | $\ell_{node}/\alpha$ | $a_0 = \hbar/(m_e c \alpha)$. The atom is $1/\alpha \approx 137$ lattice pitches. |
| Hartree energy $E_H$ | $m_e(\alpha c)^2$ | Same formula. $E_H = K/a_0$ (coupling per cavity radius). |
| Electron | $0_1$ topological unknot | Irreducible closed flux tube. Internal radius $\sim \lambda_W \ll a_0$. |
| Spin | Unknot chirality | Two orientations of the unknot twist: $\pm 1/2$. |
| Exchange integral $K_{12}$ | Phase-separation geometry | For same orbital: $K_{12} = J_{12}$ (mathematics identical). |
| Correlation energy | LC phase-jitter | **New AVE content.** $J_{s^2} = \tfrac{1}{2}(1+p_c)$ from torus-knot geometry. |

> **Superposition note (consistency-class / SYNTHESIS — NOT canonical-derived).** The $|\psi|^2$ row above admits a *Nyquist/aliasing reading*: superposition is the **local, epistemic** appearance of a deterministic point-defect trajectory time-averaged (under-sampled) relative to its fast carrier oscillation — i.e. $|\psi|^2 = $ trajectory-density, read as temporal aliasing. This is **Grant's Nyquist reframe, tagged synthesis-not-canonical**: the corpus reserves the word *"aliasing"* for **spatial** Brillouin undersampling only ([`paley-wiener-hilbert.md:10`](../../vol1/dynamics/ch3-quantum-signal-dynamics/paley-wiener-hilbert.md)), and the temporal reading carries **no observable distinct** from textbook $|\psi|^2$ (Class-0 reframe, no discriminator). It must **not** be promoted to canonical-derived. In the QM-foundations trio ([`research/2026-06-08_qm-foundations-trio.md`](../../../../research/2026-06-08_qm-foundations-trio.md)) this superposition leg (local / epistemic) is the *aliasing* slot; the **entanglement** leg (nonlocal / ontic) is the *thread* slot ([`phase-locked-topological-thread.md`](../../vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md)). Aliasing is deliberately kept OUT of the entanglement leaf — a local-aliasing account of entanglement would Bell-falsify.

## Measurement-process QM ↔ AVE (Section B: boundary-Joule extraction)

The QM measurement postulate (Born rule + click-rate scaling + detector observables) has its own substrate-native vocabulary distinct from the intra-system cavity-mode framing of Section A. Section A maps WAVEFUNCTION-AS-CAVITY-MODE; Section B maps MEASUREMENT-AS-BOUNDARY-EXTRACTION.

The Phase 2-A clm-ldmvwi workstream (PR #38, merged 2026-05-26) derived end-to-end the substrate-mechanism chain: master vacuum equation → boundary-impedance thermalization (FDT) at extraction lattice site → Joule extraction kinematics ($V^2/Z_{det}$) → cumulant truncation under quadratic-Lagrangian-shape per-site amplitude statistics → quadratic-in-amplitude boundary-Joule extraction-rate scaling. The standard-physics community calls the resulting scaling rule "Born rule p=2"; AVE-substrate-mechanically it is a derived consequence of the substrate's Lagrangian + boundary kinematics, not a postulated measurement rule.

**Discipline anchor (`ave-discipline-translate` v1.1 trigger 6)**: rows below give the substrate-native vocabulary mandated for prose composition. The standard-physics column names appear only as parenthetical translation references.

| **Standard QM measurement-process** | **AVE substrate-native equivalent** | **Anchor / Status** |
|---|---|---|
| Born rule p=2 / $\Pr \propto \|\psi\|^2$ | Quadratic-in-amplitude boundary-Joule extraction-rate scaling — extraction rate at a boundary lattice site is $V^2/Z_{det}$ per Joule kinematics + Axiom 1 Ohmic boundary; the $p=2$ exponent is derived (not postulated) from quadratic-Lagrangian per-site amplitude statistics + cumulant truncation | **DERIVED** end-to-end in Phase 2-A clm-ldmvwi master-equation-derivation-path; canonical claim entry: clm-ldmvwi in [`vol1/claim-quality.md`](../../vol1/claim-quality.md) |
| Quantum-measurement postulate / projective measurement | Boundary-Joule extraction event at substrate aperture — the substrate amplitude at a boundary lattice site crosses the Joule extraction threshold, drawing energy from the substrate via $V^2/Z_{det}$ kinematics | **NEW MAPPING**: Phase 2-A.3 result doc derives the threshold-crossing first-passage form; canonical home pending |
| Click rate (photodetector / SPAD / TES) | Boundary-Joule extraction event rate at threshold-crossing first-passage — Rice's-formula-derived crossing rate of the substrate amplitude across the Joule extraction threshold; or equivalently Wald mean-rate first-passage of the cumulative-Joule energy bucket | **NEW MAPPING**: Phase 2-A.3 derives both Rice + Wald forms |
| Measurement outcome / detector "click" | Substrate energy-extraction event — discrete energy quantum drawn from substrate via boundary-Joule kinematics at a threshold-crossing event; energy is $\hbar \omega$ per event for resonant substrate-mode coupling | **NEW MAPPING**: Phase 2-A.3 + 2-A.5 KB integration; canonical home pending |
| Wave-function collapse / measurement-induced state reduction | Substrate energy depletion at the threshold-crossing event — the substrate mode amplitude depletes (locally and on the propagation path) by the energy drawn through the boundary-Joule extraction. No discontinuous "collapse"; the substrate evolution is continuous through and after the extraction event | **NEW MAPPING**: structural framing in clm-ldmvwi rationale; canonical home pending |
| Detector dark count | Substrate-thermal boundary-amplitude threshold crossing absent signal — at $V_n / V_{threshold}$ near unity from FDT-derived thermal amplitude alone, occasional threshold crossings occur without signal contribution; the rate is set by the vacuum Nyquist baseline + Joule extraction threshold | **NEW MAPPING**: structural; canonical home pending |
| Detector quantum efficiency η | Boundary-Joule extraction efficiency per substrate-amplitude event — fraction of substrate energy in the incoming mode that gets drawn through the boundary impedance into the detector load vs reflected back into the substrate by impedance mismatch; substrate-mechanically: $\eta = 1 - \|\Gamma\|^2$ where $\Gamma$ is the boundary reflection coefficient | **NEW MAPPING**: Axiom 3 minimum-reflection-coefficient infrastructure applies directly; canonical home pending |
| Photon (incident on detector) | Substrate transverse-mode amplitude quantum — chiral impedance-matched substrate transverse-mode packet of energy $\hbar \omega$ arriving at the boundary aperture | **CANONICAL**: per `phase-locked-topological-thread.md` and Vol 2 ch1 topological-matter context — photon is a substrate-mode object, not a measurement-process observable per se |
| Photon flux ⇒ click rate scaling | Substrate-mode amplitude → boundary-Joule extraction-rate at detector — scaling is quadratic in signal amplitude (Section B row 1 above); for coherent substrate-mode amplitude, scaling matches standard "$\|\Psi\|^2$" by direct substrate kinematics | **DERIVED**: Phase 2-A clm-ldmvwi chain |

## Section ordering note

Section A rows are intra-system: they describe the dynamics of a substrate cavity mode (e.g. the electron's atomic orbital structure). Section B rows are measurement-process: they describe what happens when the substrate mode interacts with a boundary-Joule extraction aperture (e.g. a photodetector).

Section A's $\|\psi\|^2$ row (intra-system position probability density) and Section B's Born-rule row (measurement-process click-rate scaling) refer to DIFFERENT physical claims that standard QM happens to express with the same $\|\psi\|^2$ symbol. AVE distinguishes them substrate-mechanically:

- Section A $\|\psi\|^2$ → density of point-defect sweeping its standing-wave mode (intra-system: where the electron is)
- Section B Born rule → quadratic-in-amplitude boundary-Joule extraction-rate scaling (measurement-process: what rate energy is drawn out of a substrate mode at a detector boundary)

These are independent substrate-mechanical claims; conflating them under one $\|\psi\|^2$ label is exactly the standard-physics-vocabulary substitution failure mode that `ave-discipline-translate` v1.1 trigger 6 catches.

## Cross-references

- **Companion translation tables**: [`translation-stochastics.md`](translation-stochastics.md) for Section B's underlying stochastics vocabulary (FDT, Gaussian, CLT, Wick, Langevin, cumulants); [`translation-circuit.md`](translation-circuit.md) for boundary-impedance / Joule-kinematics vocabulary
- **Section B canonical claim**: clm-ldmvwi in [`vol1/claim-quality.md`](../../vol1/claim-quality.md) — Born rule from Ohmic measurement work, master-equation-derivation-path closed via Phase 2-A workstream (5 sub-phases)
- **Section B research chain** (research-tier, not canonical leaves): Phase 2-A.1 prereg + [A.2 stochastic master eq](../../../../research/2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md) + [A.3 threshold-crossing](../../../../research/2026-05-26_clm-ldmvwi-phase-2a-3-threshold-crossing-result.md) + [A.4 uniqueness](../../../../research/2026-05-26_clm-ldmvwi-phase-2a-4-uniqueness-result.md) + A.5 KB integration. Most Section B NEW MAPPING rows reference this chain as derivation anchor; canonical KB-leaf integration of the chain is pending Phase 2-A.5-style follow-on work
- **Sibling epic**: [`_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md`](../../../../_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md) — substrate-distinct Section B prediction surfaced by applying `ave-discipline-translate` v1.1 trigger 6 to the Phase 2-A.4 chain
- **Discipline anchor**: `ave-discipline-translate` v1.1 trigger 6 (substrate-native prose-vocabulary discipline); Section B is the lookup infrastructure for measurement-process vocabulary
