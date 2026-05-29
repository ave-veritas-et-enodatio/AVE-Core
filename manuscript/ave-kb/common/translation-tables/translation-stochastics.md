[↑ Translation Tables](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "translation reference table; no claim originated here. Substrate-native vocabulary mappings for standard-physics stochastics terminology that appears in canonical FDT / Nyquist-noise leaves (vol3/ch11) and in Phase 2-A clm-ldmvwi result chain. Created 2026-05-26 per ave-discipline-translate v1.1 trigger 6 substrate-native vocabulary discipline."
-->

# Stochastics ↔ AVE Substrate-Native Translation

<!-- label: tab:trans_stochastics -->

Standard-physics stochastics vocabulary (Fluctuation-Dissipation Theorem, Central Limit Theorem, Wick's theorem, Gaussian noise, Markovian process, Langevin equation, cumulant expansion, etc.) appears densely in any AVE derivation that touches substrate amplitude statistics — most notably the Phase 2-A clm-ldmvwi master-equation-derivation-path of quadratic-in-amplitude boundary-Joule extraction-rate scaling. This table maps each standard-physics term to its AVE substrate-native equivalent.

**Discipline note (v1.1 trigger 6 origin)**: this table exists because the 2026-05-26 Q-NCLT-1 adjudication session surfaced that the agent was using stochastics vocabulary as primary prose vocabulary describing substrate physics rather than as parenthetical translation reference. The resulting wholesale-vocabulary-substitution failure mode (FM-5 in `ave-discipline-translate` v1.1) had occluded the load-bearing structural distinction between substrate-mechanism emergence and substrate-agnostic statistics. This table grounds the substrate-native vocabulary that v1.1 trigger 6 enforces.

**Status taxonomy per row**:

- **CANONICAL**: substrate-native name appears in a canonical KB leaf with verifiable file:line attribution.
- **NEW MAPPING**: substrate-native name proposed here; canonical home pending downstream KB-integration work (likely follow-on from Phase 2-A.5 or future result-doc sweep). Phase 2-A research-tier result docs use the proposed substrate-native name but research/ is not canonical-tier.

| **Standard physics name** | **AVE substrate-native equivalent** | **Status / Canonical home** |
|---|---|---|
| Fluctuation-Dissipation Theorem (FDT) | Boundary-impedance thermalization — the Nyquist relation $\langle V^2(f)\rangle = 4 k_B T R \Delta f$ applies literally (not analogically) to every $\mathcal{M}_A$ lattice impedance boundary; each boundary is a substrate-thermal noise source proportional to its local impedance | **CANONICAL**: [`vol3/condensed-matter/ch11-thermodynamics/nyquist-noise-fdt.md`](../../vol3/condensed-matter/ch11-thermodynamics/nyquist-noise-fdt.md) (clm-eaiqj1) |
| Nyquist thermal voltage noise | Vacuum Nyquist baseline — $\langle V^2_{vac}(f)\rangle = 4 k_B T Z_0 \Delta f$ at the substrate's characteristic impedance $Z_0 = \sqrt{\mu_0/\varepsilon_0} \approx 376.73$ Ω; each lattice node radiates thermal noise proportional to local impedance | **CANONICAL**: same leaf |
| Thermal noise (generic, any conductor) | $\mathcal{M}_A$ lattice thermal amplitude radiation per local impedance; substrate-thermal excitation at K4-TLM lattice nodes governed by Nyquist relation; "temperature is RMS electromagnetic noise" framing (vol3 ch11 thermodynamics) | **CANONICAL**: same leaf |
| Equilibrium thermal bath | $\mathcal{M}_A$ substrate at uniform temperature with substrate-thermal amplitude statistics governed by the vacuum Nyquist baseline; substrate-mechanical (not phenomenological bath model) | **CANONICAL** (anchor): same leaf |
| Gaussian noise (per-site amplitude statistics) | Quadratic-Lagrangian-shape amplitude statistics — in the linear substrate regime (Ax 1 baseline; substrate Lagrangian $\mathcal{L}_{node} = \tfrac{1}{2}\varepsilon_0\|\partial_t\mathbf{A}_n\|^2 - \tfrac{1}{2\mu_0}\|\nabla\times\mathbf{A}_n\|^2$ quadratic in amplitude), per-site amplitude moments factorize into products of 2-point correlators; no irreducible higher-order content | **NEW MAPPING**: Phase 2-A.2 + A.4 result docs ([`research/2026-05-26_clm-ldmvwi-phase-2a-4-uniqueness-result.md`](../../../../research/2026-05-26_clm-ldmvwi-phase-2a-4-uniqueness-result.md) §3.1) invoke; canonical home pending |
| Wick's theorem / Isserlis' theorem | Quadratic-Lagrangian moment factorization — the substrate-mechanical name for the fact that a quadratic-Lagrangian system has all higher-order amplitude correlators reducible to 2-point correlator products ($\langle V^{2n}\rangle = (2n-1)!! \cdot \sigma^{2n}$ for Gaussian-shape per-site amplitude) | **NEW MAPPING**: Phase 2-A.4 §3.1 invokes; canonical home pending |
| Central Limit Theorem (CLT) | Central-aggregation across N independent substrate lattice sites — the **substrate-agnostic** statistics theorem stating that the sum of N independent equal-variance per-site amplitudes converges to quadratic-Lagrangian-shape as N → ∞. Note: this aggregation is **NOT** AVE-distinct — it applies to any framework with N independent contributions of equal variance; the substrate-distinct content (when present) lives in the per-site amplitude-shape, NOT in the aggregation step | **NEW MAPPING**: Phase 2-A.4 §3.1 invokes; epic `ax4-saturation-narrow-aperture-amplitude-shape.md` makes the substrate-distinct/substrate-agnostic distinction explicit |
| Markovian process | History-independent substrate amplitude dynamics — substrate amplitude evolution at a lattice site depends only on current state, not on history; substrate-mechanically: the K4-TLM bond-LC dynamics has no memory term in the linear regime | **NEW MAPPING**: Phase 2-A.2 invokes; canonical home pending |
| White noise (delta-correlated) | Markovian substrate amplitude fluctuations with $\langle f(t)f(t')\rangle \propto \delta(t-t')$; the substrate-thermal noise injection at each boundary site is delta-correlated by FDT in the equilibrium linear regime | **NEW MAPPING**: Phase 2-A.2 result doc derives the canonical FDT-derived form |
| Langevin equation | Stochastic substrate-amplitude evolution equation — single-site SDE for substrate amplitude under FDT-derived thermal noise injection; canonical form: $\Box V + 2\gamma_n \delta^3(\mathbf{x}-\mathbf{x}_n) \partial_t V = f_n(t) \delta^3(\mathbf{x}-\mathbf{x}_n)$ at a boundary lattice site with Joule extraction coefficient $\gamma_n = Z_{det}^{-1}$ and thermal noise $\langle f_n(t)f_n(t')\rangle = 2 k_B T Z_{det} \delta(t-t')$ | **NEW MAPPING**: Phase 2-A.2 result doc derives ([`research/2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md`](../../../../research/2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md)); canonical home pending |
| Stochastic differential equation (SDE) | Stochastic substrate-amplitude evolution at lattice site; same physics as Langevin row | **NEW MAPPING**: same anchor |
| Cumulant expansion ($\kappa_n$) | Substrate amplitude correlator decomposition — irreducible n-point amplitude correlator content beyond the 2-point baseline; $\kappa_n = 0$ for $n \geq 3$ in the linear substrate regime (quadratic-Lagrangian-shape), $\kappa_n \neq 0$ from Ax 4 saturation kernel | **NEW MAPPING**: Phase 2-A.4 §3.1 invokes; canonical home pending |
| Edgeworth expansion / cumulant pre-asymptote | Pre-asymptotic substrate amplitude-shape across N-site aggregation — leading irreducible higher-order content scales as $\kappa_3/\sigma^3 \sim 1/\sqrt{N}$, $\kappa_4/\sigma^4 \sim 1/N$ for the aperture-aggregate when per-site has substrate-pinned higher-order content | **NEW MAPPING**: invoked in epic `ax4-saturation-narrow-aperture-amplitude-shape.md`; canonical home pending |
| First-passage time / threshold-crossing | Boundary-Joule extraction event onset — the substrate amplitude at a boundary site first crosses the Joule extraction threshold; canonical AVE form: Rice's-formula-derived threshold-crossing rate at substrate boundary | **NEW MAPPING**: Phase 2-A.3 result doc derives ([`research/2026-05-26_clm-ldmvwi-phase-2a-3-threshold-crossing-result.md`](../../../../research/2026-05-26_clm-ldmvwi-phase-2a-3-threshold-crossing-result.md)); canonical home pending |
| Rice's formula (voltage-threshold crossing rate) | Substrate boundary-amplitude threshold-crossing rate — substrate-mechanical form: count of substrate amplitude crossings of the Joule extraction threshold per unit time; applies to substrate amplitude at boundary site | **NEW MAPPING**: Phase 2-A.3 derives |
| Wald mean-rate (energy-bucket first passage) | Cumulative-Joule energy-bucket first-passage rate at substrate boundary — substrate-mechanical name for the same threshold-crossing rate viewed through energy-accumulation rather than instantaneous-amplitude lens | **NEW MAPPING**: Phase 2-A.3 derives both Rice + Wald approaches |
| Brownian motion / diffusive process | Diffusive substrate amplitude evolution under FDT-derived noise; substrate-mechanical: per-site amplitude diffuses in amplitude-space when no signal is present | **NEW MAPPING**: not yet canonical-named |

## Discipline implications

This table grounds the substrate-native vocabulary mandated by `ave-discipline-translate` v1.1 trigger 6 during prose composition. When an agent is about to compose user-facing prose describing substrate physics that touches stochastics, the substrate-native column above is the PRIMARY description language; the standard-physics column appears only as parenthetical translation reference.

**Example (OK pattern)**:
"At each boundary lattice site, the substrate amplitude evolves under boundary-impedance thermalization (the standard community calls the underlying relation 'FDT'); in the linear substrate regime, the per-site amplitude statistics have quadratic-Lagrangian-shape (the standard community calls this 'Gaussian')."

**Example (NOT OK pattern)**:
"At each detector boundary, thermal noise follows FDT; in equilibrium, the noise is Gaussian." (Standard-physics vocabulary cluster used as primary description; substrate physics hidden behind labels.)

## Canonical home gaps surfaced by this table

Most rows are **NEW MAPPING** rather than CANONICAL, indicating that the Phase 2-A research-tier work needs follow-on canonical-leaf integration to land these substrate-native names in canonical KB leaves. Candidate Phase 2-A.5-style follow-on workstreams:

- **Quadratic-Lagrangian moment factorization** + **substrate amplitude correlator decomposition** — single new canonical leaf in vol3/ch11 (companion to nyquist-noise-fdt.md) would close several rows
- **Stochastic substrate-amplitude evolution equation** — Phase 2-A.2 form (master vacuum equation + FDT-derived noise injection at boundary lattice sites) → promote to canonical leaf
- **Substrate boundary-amplitude threshold-crossing rate** — Phase 2-A.3 form → promote to canonical leaf

These follow-ons are not in scope for this translation table but flagged here for future epic seeding.

## Cross-references

- **Companion translation tables**: [`translation-qm.md`](translation-qm.md) for QM measurement-process vocabulary (Born rule, $|\psi|^2$, click rate — pending v1.1 extension); [`translation-circuit.md`](translation-circuit.md) for electrical-impedance vocabulary; [`translation-condensed-matter.md`](translation-condensed-matter.md) for superconductivity vocabulary
- **Substrate-thermal-amplitude canonical home**: [`vol3/condensed-matter/ch11-thermodynamics/nyquist-noise-fdt.md`](../../vol3/condensed-matter/ch11-thermodynamics/nyquist-noise-fdt.md) (clm-eaiqj1) — anchor for FDT + Nyquist + boundary-impedance thermalization
- **Phase 2-A clm-ldmvwi result chain** (research-tier; not canonical leaves): A.1 prereg + [A.2 stochastic master eq](../../../../research/2026-05-26_clm-ldmvwi-phase-2a-2-stochastic-master-eq-result.md) + [A.3 threshold-crossing](../../../../research/2026-05-26_clm-ldmvwi-phase-2a-3-threshold-crossing-result.md) + [A.4 uniqueness](../../../../research/2026-05-26_clm-ldmvwi-phase-2a-4-uniqueness-result.md) + A.5 KB integration — most NEW MAPPING rows reference this chain as derivation anchor
- **Discipline anchor**: `ave-discipline-translate` v1.1 trigger 6 (substrate-native prose-vocabulary discipline); this table IS the lookup infrastructure that trigger 6 walks during prose composition
- **Sibling epic surfaced by this discipline**: [`_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md`](../../../../_orchestration/ax4-saturation-narrow-aperture-amplitude-shape.md) — the substrate-distinct vs substrate-agnostic distinction (Ax 4 saturation vs central-aggregation pre-asymptote) that this table makes explicit
