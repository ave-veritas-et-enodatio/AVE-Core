# Vol 6 Taxonomy Design — Periodic Table of Topological Knots (Z=1–14)

**Architect:** kb-taxonomy-architect
**Source survey:** `/.claude/phase0-surveys/vol6_survey.md`
**Target root:** `manuscript/ave-kb/vol6/`

---

## 1. Invariants

INVARIANT items confirmed as genuinely cross-cutting (appearing in Vol 6 AND at least one other volume).

1. **INVARIANT: mathcal-M-notation** — $\mathcal{M}_A$ denotes the vacuum medium; written inline, NOT via `\vacuum` macro. (source: survey §3, confirmed cross-volume in prompt context)

2. **INVARIANT: l-node-spelling** — All volumes except Vol 1 write `$l_{node}$` (roman ell, not script). Vol 1 writes `$\ell_{node}$`. Distillers must preserve this distinction at the leaf level. (source: cross-volume context)

3. **INVARIANT: V-yield-definition** — $V_{yield} \approx 43.65$ kV (dielectric yield limit) defined in Vol 4 Ch.1; referenced by other volumes. NOT defined in Vol 6. (source: cross-volume context)

4. **INVARIANT: tcolorbox-environments** — Shared environment names: `resultbox`, `axiombox`, `simbox`, `examplebox`, `summarybox`, `exercisebox`, `circuitbox`, `codebox`, `objectivebox`. Present in manuscript infrastructure; Vol 6 uses only `resultbox` (once, in `01_computational.tex`). (source: survey §2)

5. **INVARIANT: shared-backmatter-03** — `../backmatter/03_geometric_inevitability.tex` is the Vol 6 backmatter (NOT `01_appendices.tex`). Contains dangling refs to Vol 1 and Vol 5 labels — these render as `??` in Vol 6 PDF. (source: survey §1, §7 anomaly 11)

**Not invariants (Vol 6-specific, not cross-cutting):**
- The 6-section element template (unique to Vol 6's catalog structure)
- Semiconductor-nuclear parameter mapping (Vol 6 `01_computational.tex`)
- Miller avalanche multiplication formula (Vol 6 only)
- Element EE analogues (Vol 6 only)
- Named colors `darkbg`, `neonblue`, etc. (local to standalone circuit figure files; not used in chapter text)

---

## 2. Volume Hierarchy Design

### Grouping decision: Periodic-row grouping with a shared framework section

**Rationale:**

Vol 6 has two distinct structural types:
- **Framework chapters** (3 chapters + 1 unnumbered): Cross-cutting theory that applies to all elements — the computational model, chemistry translation guide, mass defect summary. These are NOT part of the element catalog.
- **Element catalog** (14 chapters, Z=1–14): Highly parallel, one chapter per element, following a standard 6-section template.
- **Appendices** (2): Heavy element catalog (Z=15–119) and shared geometric inevitability backmatter.

For the element catalog, grouping by **periodic row (period)** is correct for agent navigation because:
1. It mirrors natural chemical/physical groupings an agent query will use ("Period 2 elements", "noble gases").
2. It limits any period-index to at most 8 elements, keeping index token counts manageable.
3. It avoids a flat 14-element list at the vol6 index level, which would force the agent to read 14 one-liners when looking for a single element.
4. Per memory note: periodic-table groupings with >50 leaves should use period grouping.

**Period assignments for Z=1–14:**
- Period 1: H (Z=1), He (Z=2) — 2 elements
- Period 2: Li (Z=3), Be (Z=4), B (Z=5), C (Z=6), N (Z=7), O (Z=8), F (Z=9), Ne (Z=10) — 8 elements
- Period 3 (partial, Z=11–14): Na (Z=11), Mg (Z=12), Al (Z=13), Si (Z=14) — 4 elements

**Framework and appendix placement:**
- Framework chapters live under `vol6/framework/` (not in any period group).
- The heavy element appendix lives under `vol6/appendix/`.
- The shared geometric inevitability backmatter lives under `vol6/appendix/geometric-inevitability/` with a cross-volume primary pointer to its dangling refs.

### Proposed directory structure

```
ave-kb/vol6/
  index.md
  framework/
    index.md
    mass-defect-summary.md               [leaf]
    executive-abstract.md                [leaf]
    computational-mass-defect/
      index.md
      mass-as-reactive-load.md           [leaf]
      topological-circuit-conventions.md [leaf]
      python-simulator.md                [leaf]
      network-analytics.md               [leaf]
      nucleon-spacing-derivation.md      [leaf]
      mutual-coupling-constant.md        [leaf]
      pn-junction-coupling.md            [leaf]
      abcd-transfer-matrix.md            [leaf]
      operating-regimes.md               [leaf]
      semiconductor-nuclear-analysis.md  [leaf]
      radioactive-decay-impedance.md     [leaf]
    chemistry-translation/
      index.md
      quantum-vs-topological-shells.md   [leaf]
      lewis-dots-vsepr.md                [leaf]
      semiconductor-regime-chemistry.md  [leaf]
  period-1/
    index.md
    hydrogen/
      index.md
      structure-isotope-stability.md     [leaf]
      vacuum-density-flux.md             [leaf]
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      orbital-knot-topology.md           [leaf]
      semiconductor-regime.md            [leaf]
    helium/
      index.md
      structure-isotope-stability.md     [leaf]
      vacuum-density-flux.md             [leaf]
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      orbital-knot-topology.md           [leaf]
      semiconductor-regime.md            [leaf]
  period-2/
    index.md
    lithium/
      index.md
      structure-isotope-stability.md     [leaf]
      vacuum-density-flux.md             [leaf]
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      orbital-knot-topology.md           [leaf]
      semiconductor-regime.md            [leaf]
    beryllium/
      index.md
      structure-isotope-stability.md     [leaf]
      vacuum-density-flux.md             [leaf]
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      orbital-knot-topology.md           [leaf]
      semiconductor-regime.md            [leaf]
    boron/
      index.md
      structure-isotope-stability.md     [leaf]
      vacuum-density-flux.md             [leaf]
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      orbital-knot-topology.md           [leaf]
      semiconductor-regime.md            [leaf]
    carbon/
      index.md
      structure-isotope-stability.md     [leaf]
      vacuum-density-flux.md             [leaf]
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      orbital-knot-topology.md           [leaf]
      semiconductor-regime.md            [leaf]
    nitrogen/
      index.md
      structure-isotope-stability.md     [leaf]
      vacuum-density-flux.md             [leaf]
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      orbital-knot-topology.md           [leaf]
      semiconductor-regime.md            [leaf]
    oxygen/
      index.md
      structure-isotope-stability.md     [leaf]
      vacuum-density-flux.md             [leaf]
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      orbital-knot-topology.md           [leaf]   ← NOTE: no named subsection in source; leaf is shorter
      semiconductor-regime.md            [leaf]
    fluorine/
      index.md
      structure-isotope-stability.md     [leaf]   ← NOTE: titled "The Macroscopic Halo Offset" in source
      vacuum-density-flux.md             [leaf]
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      orbital-knot-topology.md           [leaf]
      semiconductor-regime.md            [leaf]
    neon/
      index.md
      structure-isotope-stability.md     [leaf]
      vacuum-density-flux.md             [leaf]
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      orbital-knot-topology.md           [leaf]
      curve-fitting-fallacy.md           [leaf]   ← EXTRA section unique to neon
      semiconductor-regime.md            [leaf]
  period-3/
    index.md
    sodium/
      index.md
      structure-isotope-stability.md     [leaf]
      vacuum-density-flux.md             [leaf]
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      core-proximity-effect.md           [leaf]   ← EXTRA section unique to sodium
      orbital-knot-topology.md           [leaf]
      semiconductor-regime.md            [leaf]
    magnesium/
      index.md
      structure-isotope-stability.md     [leaf]
      vacuum-density-flux.md             [leaf]
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      symmetric-shell-collapse.md        [leaf]   ← EXTRA section unique to magnesium
      orbital-knot-topology.md           [leaf]
      semiconductor-regime.md            [leaf]
    aluminum/
      index.md
      structure-isotope-stability.md     [leaf]
      vacuum-density-flux.md             [leaf]
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      gradual-halo-separation.md         [leaf]   ← EXTRA section unique to aluminum
      orbital-knot-topology.md           [leaf]
      semiconductor-regime.md            [leaf]
    silicon/
      index.md
      structure-isotope-stability.md     [leaf]
      vacuum-density-flux.md             [leaf]   ← NOTE: titled "Symmetric Core Collapse" in source
      ee-equivalent.md                   [leaf]
      topological-area.md                [leaf]
      orbital-knot-topology.md           [leaf]
      semiconductor-regime.md            [leaf]
  appendix/
    index.md
    heavy-element-catalog/
      index.md
      mass-prediction-accuracy.md        [leaf]
      full-element-table.md              [leaf]   ← verbatim longtable Z=15–119
      selected-heavy-orbital-topology.md [leaf]
      selected-heavy-strain-fields.md    [leaf]
      selected-heavy-circuit-models.md   [leaf]
    geometric-inevitability/
      index.md
      golden-ratio-min-impedance.md      [leaf]
      fibonacci-packing-proxy.md         [leaf]
      pi-topological-horizon.md          [leaf]
      magic-numbers-shell-closure.md     [leaf]
      platonic-progression.md            [leaf]
      derived-numerical-constants.md     [leaf]
      g-star-derivation.md               [leaf]
      alpha-s-derivation.md              [leaf]
      lambda-higgs-derivation.md         [leaf]
      conclusion-death-of-numerology.md  [leaf]
```

---

## 3. Document Skeleton

All files listed with one-line content scope. `[leaf — verbatim]` marks terminal documents. `[index]` marks navigation nodes.

### Volume index

`ave-kb/vol6/index.md` — [index] One-paragraph summary of Vol 6; links to framework/, period-1/, period-2/, period-3/, appendix/; surfaces key results: binding energy ceiling formula, semiconductor-nuclear parameter map, Z=1–14 EE analogue table

### Framework section

`ave-kb/vol6/framework/index.md` — [index] Framework chapter summaries; links to mass-defect-summary, executive-abstract, computational-mass-defect/, chemistry-translation/; surfaces: $E_{\text{binding(max)}} = \alpha \cdot M_{\text{proton}} c^2$, key constants $d$, $K$, $V_{BR}$

`ave-kb/vol6/framework/mass-defect-summary.md` — [leaf — verbatim] Source: `00_summary_table.tex`; unnumbered chapter; empirical vs. topological mass table for H through Si (`tab:mass_summary`)

`ave-kb/vol6/framework/executive-abstract.md` — [leaf — verbatim] Source: `00_introduction.tex`; continuous mathematical closure Z=1–28, alpha-series, golden ratio emergence, deterministic simulation

`ave-kb/vol6/framework/computational-mass-defect/index.md` — [index] Subtopic summary of `01_computational.tex`; surfaces all 8 labelled equations; links to 11 leaf files

`ave-kb/vol6/framework/computational-mass-defect/mass-as-reactive-load.md` — [leaf — verbatim] Source: `01_computational.tex` §"Mass as a Localized Reactive Load"; conceptual foundation: mass as localized reactive LC load

`ave-kb/vol6/framework/computational-mass-defect/topological-circuit-conventions.md` — [leaf — verbatim] Source: `01_computational.tex` §"Topological Circuit Conventions"; sign conventions, port definitions, circuit topology rules

`ave-kb/vol6/framework/computational-mass-defect/python-simulator.md` — [leaf — verbatim] Source: `01_computational.tex` §"The Python Simulator: EE-Based Thermodynamic Integration"; verbatim Python code from `\verbatim` blocks; NOTE: source uses `\verbatim` not `codebox`

`ave-kb/vol6/framework/computational-mass-defect/network-analytics.md` — [leaf — verbatim] Source: `01_computational.tex` §"Network Analytics: Q-Factor and S-Parameters" + subsections; topological Q-factor, $S_{11}$; figures `fig:ee_network_analytics`

`ave-kb/vol6/framework/computational-mass-defect/nucleon-spacing-derivation.md` — [leaf — verbatim] Source: `01_computational.tex` §`sec:d_derivation`; derivation of $d = 4\hbar/(m_pc) \approx 0.841$ fm (`eq:d_proton`); $D_{\text{intra}} = d\sqrt{8}$ (`eq:d_intra`)

`ave-kb/vol6/framework/computational-mass-defect/mutual-coupling-constant.md` — [leaf — verbatim] Source: `01_computational.tex` §`sec:K_derivation`; full derivation of $K \approx 11.337$ MeV·fm (`eq:k_mutual`, `eq:k_mutual_expanded`)

`ave-kb/vol6/framework/computational-mass-defect/pn-junction-coupling.md` — [leaf — verbatim] Source: `01_computational.tex` §`sec:pn_junction`; nuclear diode analogy, Coulomb correction (`eq:coulomb_correction`), absolute mass defect topologic limit; resultbox "Topologic Yield Mass Defect (Binding Energy Ceiling)"

`ave-kb/vol6/framework/computational-mass-defect/abcd-transfer-matrix.md` — [leaf — verbatim] Source: `01_computational.tex` §`sec:abcd_cascade`; ABCD framework, nucleon ports, network topology for Z≥15

`ave-kb/vol6/framework/computational-mass-defect/operating-regimes.md` — [leaf — verbatim] Source: `01_computational.tex` §`sec:operating_regimes`; linear vs. non-linear regimes, Sulfur-32 breakdown, Small/Large Signal ratio $V_R/V_{BR}$

`ave-kb/vol6/framework/computational-mass-defect/semiconductor-nuclear-analysis.md` — [leaf — verbatim] Source: `01_computational.tex` §`sec:semiconductor_nuclear`; two binding models (`sec:two_models`), parameter derivation table (`tab:semi_nuclear_map`), breakdown voltage (`eq:V_BR`), Miller avalanche (`eq:miller`, `eq:V_R`), complete binding energy formula (`eq:semiconductor_mass`), `tab:model_comparison`, `tab:engine_traceability`, `tab:avalanche_results`

`ave-kb/vol6/framework/computational-mass-defect/radioactive-decay-impedance.md` — [leaf — verbatim] Source: `01_computational.tex` §"Radioactive Decay as Impedance Mismatch"; Tritium beta decay, Beryllium-8 alpha fission; figure `fig:isotope_decay`

`ave-kb/vol6/framework/chemistry-translation/index.md` — [index] Summary of `02_chemistry.tex`; maps conventional chemistry vocabulary to AVE topological equivalents; NOTE: source chapter has no `\label`

`ave-kb/vol6/framework/chemistry-translation/quantum-vs-topological-shells.md` — [leaf — verbatim] Source: `02_chemistry.tex` §"Quantum Orbitals vs. Topological Shells"; orbital shell mapping

`ave-kb/vol6/framework/chemistry-translation/lewis-dots-vsepr.md` — [leaf — verbatim] Source: `02_chemistry.tex` §§"Lewis Dots and Unbound Valency" + "VSEPR Theory and Inductive Minimization"; electronegativity as asymmetric inductance

`ave-kb/vol6/framework/chemistry-translation/semiconductor-regime-chemistry.md` — [leaf — verbatim] Source: `02_chemistry.tex` §"Semiconductor Regime Classification and Chemical Behavior"; links chemical behavior to operating regime

### Period 1

`ave-kb/vol6/period-1/index.md` — [index] Period 1 summary (H, He); EE analogues (Isolated LC Tank, Polyphase Resonant Transformer); links to hydrogen/, helium/

`ave-kb/vol6/period-1/hydrogen/index.md` — [index] Z=1 Hydrogen summary; EE analogue: Isolated LC Tank; knot type: trefoil $3_1$; source: `03_hydrogen.tex`; links to 6 leaves

`ave-kb/vol6/period-1/hydrogen/structure-isotope-stability.md` — [leaf — verbatim] Source: `03_hydrogen.tex` §1; topological structure, isotope stability analysis for H-1/H-2/H-3

`ave-kb/vol6/period-1/hydrogen/vacuum-density-flux.md` — [leaf — verbatim] Source: `03_hydrogen.tex` §2; continuous vacuum density flux; figure `fig:h1_density`

`ave-kb/vol6/period-1/hydrogen/ee-equivalent.md` — [leaf — verbatim] Source: `03_hydrogen.tex` §3; electrical engineering equivalent circuit; figure `fig:circuit_h1`

`ave-kb/vol6/period-1/hydrogen/topological-area.md` — [leaf — verbatim] Source: `03_hydrogen.tex` §4; topological area of interest

`ave-kb/vol6/period-1/hydrogen/orbital-knot-topology.md` — [leaf — verbatim] Source: `03_hydrogen.tex` §5 + subsections (Bohr radius, Rydberg, de Broglie — 3 subsubsections, deviation from standard template); figure `fig:hydrogen_1_topo`

`ave-kb/vol6/period-1/hydrogen/semiconductor-regime.md` — [leaf — verbatim] Source: `03_hydrogen.tex` §6; semiconductor regime classification

`ave-kb/vol6/period-1/helium/index.md` — [index] Z=2 Helium summary; EE analogue: Polyphase Resonant Transformer; source: `04_helium.tex`; links to 6 leaves

`ave-kb/vol6/period-1/helium/structure-isotope-stability.md` — [leaf — verbatim] Source: `04_helium.tex` §1

`ave-kb/vol6/period-1/helium/vacuum-density-flux.md` — [leaf — verbatim] Source: `04_helium.tex` §2

`ave-kb/vol6/period-1/helium/ee-equivalent.md` — [leaf — verbatim] Source: `04_helium.tex` §3

`ave-kb/vol6/period-1/helium/topological-area.md` — [leaf — verbatim] Source: `04_helium.tex` §4

`ave-kb/vol6/period-1/helium/orbital-knot-topology.md` — [leaf — verbatim] Source: `04_helium.tex` §5

`ave-kb/vol6/period-1/helium/semiconductor-regime.md` — [leaf — verbatim] Source: `04_helium.tex` §6

### Period 2

`ave-kb/vol6/period-2/index.md` — [index] Period 2 summary (Li–Ne); lists all 8 elements with EE analogues; links to 8 element subdirectories

`ave-kb/vol6/period-2/lithium/index.md` — [index] Z=3 Lithium; EE analogue: Air-Core Transformer; ANOMALY NOTE: `fig:li7_density_equator` defined twice — distiller uses second definition (equatorial slice); source: `05_lithium.tex`

`ave-kb/vol6/period-2/lithium/structure-isotope-stability.md` — [leaf — verbatim] Source: `05_lithium.tex` §1

`ave-kb/vol6/period-2/lithium/vacuum-density-flux.md` — [leaf — verbatim] Source: `05_lithium.tex` §2; ANOMALY: duplicate label `fig:li7_density_equator` — use second definition

`ave-kb/vol6/period-2/lithium/ee-equivalent.md` — [leaf — verbatim] Source: `05_lithium.tex` §3

`ave-kb/vol6/period-2/lithium/topological-area.md` — [leaf — verbatim] Source: `05_lithium.tex` §4

`ave-kb/vol6/period-2/lithium/orbital-knot-topology.md` — [leaf — verbatim] Source: `05_lithium.tex` §5

`ave-kb/vol6/period-2/lithium/semiconductor-regime.md` — [leaf — verbatim] Source: `05_lithium.tex` §6

`ave-kb/vol6/period-2/beryllium/index.md` — [index] Z=4 Beryllium; EE analogue: AC Wheatstone Bridge; source: `06_beryllium.tex`

`ave-kb/vol6/period-2/beryllium/structure-isotope-stability.md` — [leaf — verbatim] Source: `06_beryllium.tex` §1

`ave-kb/vol6/period-2/beryllium/vacuum-density-flux.md` — [leaf — verbatim] Source: `06_beryllium.tex` §2

`ave-kb/vol6/period-2/beryllium/ee-equivalent.md` — [leaf — verbatim] Source: `06_beryllium.tex` §3

`ave-kb/vol6/period-2/beryllium/topological-area.md` — [leaf — verbatim] Source: `06_beryllium.tex` §4

`ave-kb/vol6/period-2/beryllium/orbital-knot-topology.md` — [leaf — verbatim] Source: `06_beryllium.tex` §5

`ave-kb/vol6/period-2/beryllium/semiconductor-regime.md` — [leaf — verbatim] Source: `06_beryllium.tex` §6

`ave-kb/vol6/period-2/boron/index.md` — [index] Z=5 Boron ("Saturated Topological Horizon"); EE analogue: Massive Parasitic Array; ANOMALY NOTE: source chapter `07_boron.tex` has no `\label{ch:boron}`

`ave-kb/vol6/period-2/boron/structure-isotope-stability.md` — [leaf — verbatim] Source: `07_boron.tex` §1

`ave-kb/vol6/period-2/boron/vacuum-density-flux.md` — [leaf — verbatim] Source: `07_boron.tex` §2

`ave-kb/vol6/period-2/boron/ee-equivalent.md` — [leaf — verbatim] Source: `07_boron.tex` §3

`ave-kb/vol6/period-2/boron/topological-area.md` — [leaf — verbatim] Source: `07_boron.tex` §4

`ave-kb/vol6/period-2/boron/orbital-knot-topology.md` — [leaf — verbatim] Source: `07_boron.tex` §5

`ave-kb/vol6/period-2/boron/semiconductor-regime.md` — [leaf — verbatim] Source: `07_boron.tex` §6

`ave-kb/vol6/period-2/carbon/index.md` — [index] Z=6 Carbon ("Subcritical 3-Alpha Ring"); EE analogue: 3-Phase Delta-Wye Map; Platonic geometry: Triangle; ANOMALY NOTE: source `08_carbon.tex` has no `\label{ch:carbon}`

`ave-kb/vol6/period-2/carbon/structure-isotope-stability.md` — [leaf — verbatim] Source: `08_carbon.tex` §1

`ave-kb/vol6/period-2/carbon/vacuum-density-flux.md` — [leaf — verbatim] Source: `08_carbon.tex` §2

`ave-kb/vol6/period-2/carbon/ee-equivalent.md` — [leaf — verbatim] Source: `08_carbon.tex` §3

`ave-kb/vol6/period-2/carbon/topological-area.md` — [leaf — verbatim] Source: `08_carbon.tex` §4

`ave-kb/vol6/period-2/carbon/orbital-knot-topology.md` — [leaf — verbatim] Source: `08_carbon.tex` §5

`ave-kb/vol6/period-2/carbon/semiconductor-regime.md` — [leaf — verbatim] Source: `08_carbon.tex` §6

`ave-kb/vol6/period-2/nitrogen/index.md` — [index] Z=7 Nitrogen ("Algorithmic Topologies"); EE analogue: Irregular Scattering Matrix; ANOMALY NOTE: source `09_nitrogen.tex` has no `\label{ch:nitrogen}`

`ave-kb/vol6/period-2/nitrogen/structure-isotope-stability.md` — [leaf — verbatim] Source: `09_nitrogen.tex` §1

`ave-kb/vol6/period-2/nitrogen/vacuum-density-flux.md` — [leaf — verbatim] Source: `09_nitrogen.tex` §2

`ave-kb/vol6/period-2/nitrogen/ee-equivalent.md` — [leaf — verbatim] Source: `09_nitrogen.tex` §3

`ave-kb/vol6/period-2/nitrogen/topological-area.md` — [leaf — verbatim] Source: `09_nitrogen.tex` §4

`ave-kb/vol6/period-2/nitrogen/orbital-knot-topology.md` — [leaf — verbatim] Source: `09_nitrogen.tex` §5

`ave-kb/vol6/period-2/nitrogen/semiconductor-regime.md` — [leaf — verbatim] Source: `09_nitrogen.tex` §6

`ave-kb/vol6/period-2/oxygen/index.md` — [index] Z=8 Oxygen; EE analogue: Tetraphase Network; Platonic geometry: Tetrahedron; ANOMALY NOTE: orbital section has no named subsection in source

`ave-kb/vol6/period-2/oxygen/structure-isotope-stability.md` — [leaf — verbatim] Source: `10_oxygen.tex` §1

`ave-kb/vol6/period-2/oxygen/vacuum-density-flux.md` — [leaf — verbatim] Source: `10_oxygen.tex` §2

`ave-kb/vol6/period-2/oxygen/ee-equivalent.md` — [leaf — verbatim] Source: `10_oxygen.tex` §3

`ave-kb/vol6/period-2/oxygen/topological-area.md` — [leaf — verbatim] Source: `10_oxygen.tex` §4

`ave-kb/vol6/period-2/oxygen/orbital-knot-topology.md` — [leaf — verbatim] Source: `10_oxygen.tex` §5; no named subsection in source (deviation)

`ave-kb/vol6/period-2/oxygen/semiconductor-regime.md` — [leaf — verbatim] Source: `10_oxygen.tex` §6

`ave-kb/vol6/period-2/fluorine/index.md` — [index] Z=9 Fluorine ("Halogen Halo"); EE analogue: Halogen Halo / Asymmetric Inductance; NOTE: §2 titled "The Macroscopic Halo Offset" in source

`ave-kb/vol6/period-2/fluorine/structure-isotope-stability.md` — [leaf — verbatim] Source: `11_fluorine.tex` §1

`ave-kb/vol6/period-2/fluorine/vacuum-density-flux.md` — [leaf — verbatim] Source: `11_fluorine.tex` §2 (titled "The Macroscopic Halo Offset" in source — preserve title in leaf)

`ave-kb/vol6/period-2/fluorine/ee-equivalent.md` — [leaf — verbatim] Source: `11_fluorine.tex` §3

`ave-kb/vol6/period-2/fluorine/topological-area.md` — [leaf — verbatim] Source: `11_fluorine.tex` §4

`ave-kb/vol6/period-2/fluorine/orbital-knot-topology.md` — [leaf — verbatim] Source: `11_fluorine.tex` §5

`ave-kb/vol6/period-2/fluorine/semiconductor-regime.md` — [leaf — verbatim] Source: `11_fluorine.tex` §6

`ave-kb/vol6/period-2/neon/index.md` — [index] Z=10 Neon ("Bipyramidal Noble Gas"); EE analogue: 5-Phase Ring Oscillator; Platonic geometry: Triangular Bipyramid; NOTE: extra section "Addressing the Curve-Fitting Fallacy" — 7 leaves total

`ave-kb/vol6/period-2/neon/structure-isotope-stability.md` — [leaf — verbatim] Source: `12_neon.tex` §1

`ave-kb/vol6/period-2/neon/vacuum-density-flux.md` — [leaf — verbatim] Source: `12_neon.tex` §2

`ave-kb/vol6/period-2/neon/ee-equivalent.md` — [leaf — verbatim] Source: `12_neon.tex` §3

`ave-kb/vol6/period-2/neon/topological-area.md` — [leaf — verbatim] Source: `12_neon.tex` §4

`ave-kb/vol6/period-2/neon/orbital-knot-topology.md` — [leaf — verbatim] Source: `12_neon.tex` §5

`ave-kb/vol6/period-2/neon/curve-fitting-fallacy.md` — [leaf — verbatim] Source: `12_neon.tex` §"Addressing the Curve-Fitting Fallacy" (extra section, unique to neon)

`ave-kb/vol6/period-2/neon/semiconductor-regime.md` — [leaf — verbatim] Source: `12_neon.tex` §6

### Period 3

`ave-kb/vol6/period-3/index.md` — [index] Period 3 partial summary (Na–Si, Z=11–14); lists 4 elements with EE analogues; links to 4 element subdirectories

`ave-kb/vol6/period-3/sodium/index.md` — [index] Z=11 Sodium ("Alkali Halogen Paradox"); EE analogue: Dual-Band Coupled Filter; NOTE: extra unique section "The Core Proximity Effect" — 7 leaves total

`ave-kb/vol6/period-3/sodium/structure-isotope-stability.md` — [leaf — verbatim] Source: `13_sodium.tex` §1

`ave-kb/vol6/period-3/sodium/vacuum-density-flux.md` — [leaf — verbatim] Source: `13_sodium.tex` §2

`ave-kb/vol6/period-3/sodium/ee-equivalent.md` — [leaf — verbatim] Source: `13_sodium.tex` §3

`ave-kb/vol6/period-3/sodium/topological-area.md` — [leaf — verbatim] Source: `13_sodium.tex` §4

`ave-kb/vol6/period-3/sodium/core-proximity-effect.md` — [leaf — verbatim] Source: `13_sodium.tex` §"The Core Proximity Effect" (unique extra section)

`ave-kb/vol6/period-3/sodium/orbital-knot-topology.md` — [leaf — verbatim] Source: `13_sodium.tex` §5

`ave-kb/vol6/period-3/sodium/semiconductor-regime.md` — [leaf — verbatim] Source: `13_sodium.tex` §6

`ave-kb/vol6/period-3/magnesium/index.md` — [index] Z=12 Magnesium ("Six-Alpha Octahedron"); EE analogue: 6-Phase Balanced Bridge; Platonic geometry: Octahedron; NOTE: extra unique section "The Symmetric Shell Collapse" — 7 leaves total

`ave-kb/vol6/period-3/magnesium/structure-isotope-stability.md` — [leaf — verbatim] Source: `14_magnesium.tex` §1

`ave-kb/vol6/period-3/magnesium/vacuum-density-flux.md` — [leaf — verbatim] Source: `14_magnesium.tex` §2

`ave-kb/vol6/period-3/magnesium/ee-equivalent.md` — [leaf — verbatim] Source: `14_magnesium.tex` §3

`ave-kb/vol6/period-3/magnesium/topological-area.md` — [leaf — verbatim] Source: `13_magnesium.tex` §4

`ave-kb/vol6/period-3/magnesium/symmetric-shell-collapse.md` — [leaf — verbatim] Source: `14_magnesium.tex` §"The Symmetric Shell Collapse" (unique extra section)

`ave-kb/vol6/period-3/magnesium/orbital-knot-topology.md` — [leaf — verbatim] Source: `14_magnesium.tex` §5

`ave-kb/vol6/period-3/magnesium/semiconductor-regime.md` — [leaf — verbatim] Source: `14_magnesium.tex` §6

`ave-kb/vol6/period-3/aluminum/index.md` — [index] Z=13 Aluminum ("Octahedral Halo"); EE analogue: Asymmetrically Loaded Octahedral Network; NOTE: extra unique section "The Gradual Halo Separation Effect" — 7 leaves total

`ave-kb/vol6/period-3/aluminum/structure-isotope-stability.md` — [leaf — verbatim] Source: `15_aluminum.tex` §1

`ave-kb/vol6/period-3/aluminum/vacuum-density-flux.md` — [leaf — verbatim] Source: `15_aluminum.tex` §2

`ave-kb/vol6/period-3/aluminum/ee-equivalent.md` — [leaf — verbatim] Source: `15_aluminum.tex` §3

`ave-kb/vol6/period-3/aluminum/topological-area.md` — [leaf — verbatim] Source: `15_aluminum.tex` §4

`ave-kb/vol6/period-3/aluminum/gradual-halo-separation.md` — [leaf — verbatim] Source: `15_aluminum.tex` §"The Gradual Halo Separation Effect" (unique extra section)

`ave-kb/vol6/period-3/aluminum/orbital-knot-topology.md` — [leaf — verbatim] Source: `15_aluminum.tex` §5

`ave-kb/vol6/period-3/aluminum/semiconductor-regime.md` — [leaf — verbatim] Source: `15_aluminum.tex` §6

`ave-kb/vol6/period-3/silicon/index.md` — [index] Z=14 Silicon ("Seven-Alpha Bipyramid"); EE analogue: 7-Phase Pentagonal Bipyramid Network; Platonic geometry: Pentagonal Bipyramid; NOTE: §2 titled "Symmetric Core Collapse" in source

`ave-kb/vol6/period-3/silicon/structure-isotope-stability.md` — [leaf — verbatim] Source: `16_silicon.tex` §1

`ave-kb/vol6/period-3/silicon/vacuum-density-flux.md` — [leaf — verbatim] Source: `16_silicon.tex` §2 (titled "Symmetric Core Collapse" in source — preserve title in leaf)

`ave-kb/vol6/period-3/silicon/ee-equivalent.md` — [leaf — verbatim] Source: `16_silicon.tex` §3

`ave-kb/vol6/period-3/silicon/topological-area.md` — [leaf — verbatim] Source: `16_silicon.tex` §4

`ave-kb/vol6/period-3/silicon/orbital-knot-topology.md` — [leaf — verbatim] Source: `16_silicon.tex` §5

`ave-kb/vol6/period-3/silicon/semiconductor-regime.md` — [leaf — verbatim] Source: `16_silicon.tex` §6

### Appendix section

`ave-kb/vol6/appendix/index.md` — [index] Appendix summary; links to heavy-element-catalog/ and geometric-inevitability/

`ave-kb/vol6/appendix/heavy-element-catalog/index.md` — [index] Summary of `A_heavy_element_catalog.tex`; surfaces: Z=15–119 mass prediction accuracy, selected heavy element geometries (S-32 through Fe-56); links to 5 leaves

`ave-kb/vol6/appendix/heavy-element-catalog/mass-prediction-accuracy.md` — [leaf — verbatim] Source: `A_heavy_element_catalog.tex` §"Mass Prediction Accuracy"; figure `fig:mass_error_vs_Z`

`ave-kb/vol6/appendix/heavy-element-catalog/full-element-table.md` — [leaf — verbatim] Source: `A_heavy_element_catalog.tex` longtable `tab:heavy_catalog`; Z=15–119 empirical vs. topological mass; NOTE: longtable — distiller translates to Markdown table

`ave-kb/vol6/appendix/heavy-element-catalog/selected-heavy-orbital-topology.md` — [leaf — verbatim] Source: `A_heavy_element_catalog.tex` §"Orbital Topology of Selected Heavy Elements"; S-32 through Fe-56; figures `fig:sulfur_topology` through heavy element topology figures

`ave-kb/vol6/appendix/heavy-element-catalog/selected-heavy-strain-fields.md` — [leaf — verbatim] Source: `A_heavy_element_catalog.tex` §"Nuclear Strain Fields of Selected Heavy Elements"

`ave-kb/vol6/appendix/heavy-element-catalog/selected-heavy-circuit-models.md` — [leaf — verbatim] Source: `A_heavy_element_catalog.tex` §"Equivalent Circuit Models of Selected Heavy Elements"; figure `fig:circuit_fe56` and others

`ave-kb/vol6/appendix/geometric-inevitability/index.md` — [index] Summary of `../backmatter/03_geometric_inevitability.tex` (~487 lines); surfaces derived constants $g_*$, $\alpha_s$, $\lambda_H$; CROSS-VOLUME NOTE: 3 dangling refs (`eq:H_infinity`, `sec:galactic_saturation`, `sec:membrane_phase_buffering`) — these resolve in Vol 1/Vol 5 but not in Vol 6 PDF; links to 9 leaves

`ave-kb/vol6/appendix/geometric-inevitability/golden-ratio-min-impedance.md` — [leaf — verbatim] Source: `03_geometric_inevitability.tex` §`sec:golden_ratio_emergence`; golden ratio as minimum impedance at 12 nodes, icosahedral packing

`ave-kb/vol6/appendix/geometric-inevitability/fibonacci-packing-proxy.md` — [leaf — verbatim] Source: `03_geometric_inevitability.tex` §`sec:fibonacci_packing`; Fibonacci sequence as convergent ratio packing proxy

`ave-kb/vol6/appendix/geometric-inevitability/pi-topological-horizon.md` — [leaf — verbatim] Source: `03_geometric_inevitability.tex` §`sec:pi_horizon`; Pi and the topological horizon

`ave-kb/vol6/appendix/geometric-inevitability/magic-numbers-shell-closure.md` — [leaf — verbatim] Source: `03_geometric_inevitability.tex` §`sec:magic_numbers`; nuclear magic numbers as impedance matching shell closure

`ave-kb/vol6/appendix/geometric-inevitability/platonic-progression.md` — [leaf — verbatim] Source: `03_geometric_inevitability.tex` §"The Platonic Progression"; geometry sequence from triangle to FCC-14

`ave-kb/vol6/appendix/geometric-inevitability/derived-numerical-constants.md` — [leaf — verbatim] Source: `03_geometric_inevitability.tex` §`sec:derived_numerology`; 9+ constants; $n_{\text{coop}} = 9$, $\beta_{\text{fold}}$, $T_m$ water melting eigenmode

`ave-kb/vol6/appendix/geometric-inevitability/g-star-derivation.md` — [leaf — verbatim] Source: `03_geometric_inevitability.tex` §`sec:g_star_derivation`; $g_* = 7^3/4 = 85.75$ lattice mode count

`ave-kb/vol6/appendix/geometric-inevitability/alpha-s-derivation.md` — [leaf — verbatim] Source: `03_geometric_inevitability.tex` §`sec:alpha_s_derivation`; $\alpha_s = \alpha^{3/7}$ strong coupling constant

`ave-kb/vol6/appendix/geometric-inevitability/lambda-higgs-derivation.md` — [leaf — verbatim] Source: `03_geometric_inevitability.tex` §`sec:lambda_higgs_derivation`; $\lambda_H = 1/8$ Higgs quartic coupling; NOTE: `\cite{pdg2022}` reference present — requires shared `../bibliography`

`ave-kb/vol6/appendix/geometric-inevitability/conclusion-death-of-numerology.md` — [leaf — verbatim] Source: `03_geometric_inevitability.tex` §"Conclusion: The Death of Numerology"

---

## 4. Navigation Spec

### Up-link format

Every non-root document line 1:

```
[↑ Vol 6: Periodic Table of Knots](../../index.md)          ← from element index
[↑ Period 1](../index.md)                                    ← from element index
[↑ Hydrogen](../index.md)                                    ← from leaf (element level)
[↑ Computational Mass Defect](../index.md)                   ← from leaf (subtopic level)
[↑ Framework](../../index.md)                                ← from subtopic index
[↑ Vol 6: Periodic Table of Knots](../index.md)              ← from period/section index
```

Exact template by level:

- **Leaf under element** (depth 4): `[↑ {Element Name}](../index.md)`
- **Element index** (depth 3): `[↑ {Period N}](../index.md)`
- **Subtopic index under framework** (depth 3): `[↑ Framework](../index.md)`
- **Leaf under framework subtopic** (depth 4): `[↑ {Subtopic Name}](../index.md)`
- **Period/section index** (depth 2): `[↑ Vol 6: Periodic Table of Knots](../index.md)`
- **Vol 6 index** (depth 1): `[↑ Entry Point](../entry-point.md)`

### Down-link format

At bottom of every index file, a `## Contents` section:

```markdown
## Contents

- [Mass Defect Summary](mass-defect-summary.md) — unnumbered chapter; empirical vs. topological mass table H–Si
- [Executive Abstract](executive-abstract.md) — continuous mathematical closure, alpha-series, golden ratio
- [Computational Mass Defect](computational-mass-defect/index.md) — 11 leaves; all labelled equations
- [Chemistry Translation](chemistry-translation/index.md) — 3 leaves; vocabulary mapping
```

### Cross-volume reference format

Primary dependency (agent must follow to resolve the referenced concept):
```
> → Primary: [H_infinity equation](../../vol1/ch4/field-saturation.md) — `eq:H_infinity` defined here; dangling in Vol 6 PDF
```

Optional suggestion (agent may follow):
```
> ↗ See also: [Vol 4 Ch.1 — Dielectric Yield Limit](../../vol4/ch01/dielectric-yield.md) — $V_{yield}$ definition referenced by Vol 4 prose about Vol 6
```

Cross-volume refs in `geometric-inevitability/index.md` specifically:
```
> → Primary: [Vol 1 Ch.4](../../vol1/ch4/index.md) — `eq:H_infinity` and `sec:galactic_saturation` resolve here
> → Primary: [Vol 5 Ch.2](../../vol5/ch2/index.md) — `sec:membrane_phase_buffering` resolves here
```

---

## 5. Shared Content Decision

**Recommendation: (a) Dedicated pages at `ave-kb/common/`**

The `common/translation_*.tex` tables are used by multiple volumes (confirmed: NOT included by Vol 6, but used by at least Vol 1 and others per cross-volume context). Vol 6 explicitly does NOT include these files (`../common/translation_*.tex` noted as "NOT included by vol_6").

Therefore for Vol 6 specifically: no translation table pages needed in `ave-kb/vol6/`. The `ave-kb/common/` location is the correct home for these files when they are created for volumes that do include them.

The geometric inevitability backmatter (`03_geometric_inevitability.tex`) is the converse case: it IS unique to Vol 6's compilation and lives under `ave-kb/vol6/appendix/geometric-inevitability/` rather than `ave-kb/common/`. If another volume also includes it, the distiller should create a symlink or cross-reference at that point — do not pre-emptively move it.

**Rationale for (a) over (b):**
- Duplication of large translation tables (longtables with dozens of rows) creates drift risk: if one copy is corrected, the other becomes stale.
- An agent navigating to a translation table should land at a single authoritative location.
- Volumes that do not include the translation tables do not need the content in their section at all; a `> → Primary:` pointer to `ave-kb/common/` is sufficient.

---

## 6. Anomalies Affecting Taxonomy Design

The following survey anomalies have structural impact and are recorded here for the distiller:

| # | Anomaly | Taxonomy impact |
|---|---|---|
| 1 | Duplicate `fig:li7_density_equator` in `05_lithium.tex` (two `\label` at lines 23 and 29) | `lithium/vacuum-density-flux.md` leaf note: use second figure definition (equatorial slice) |
| 2 | Boron, Carbon, Nitrogen chapters missing `\label{ch:...}` | Noted in element index files; no structural impact — KB uses slug-based paths not LaTeX labels |
| 3 | Chemistry chapter missing `\label` | Noted in `chemistry-translation/index.md`; no structural impact |
| 4 | No `_manifest.tex`; chapter list hardcoded in `main.tex` | No impact — chapter list fully captured in survey |
| 5 | `circuits/` directory NOT linked from any chapter (7 files, H–N only) | Excluded from KB per brief; these are earlier working copies |
| 6 | `simulations/` directory: 13 orphaned PNGs + 100+ SPICE netlists, not referenced from any `.tex` | Excluded from KB; Python simulator prose in `01_computational.tex` is the authoritative representation |
| 7 | `elements.json` in volume root | Excluded; Python-engine-only artifact |
| 8 | `assets/` directory missing (in `\graphicspath`) | No impact; figures compile from `figures/`; distiller notes any missing figure at extraction time |
| 9 | Oxygen orbital section: no named `\subsection` | `oxygen/orbital-knot-topology.md` leaf shorter than standard; noted in oxygen element index |
| 10 | Python code in `\verbatim` not `codebox` | `python-simulator.md` leaf: translate verbatim block to fenced Markdown code block |
| 11 | 3 dangling `\ref{}` in `03_geometric_inevitability.tex` | `geometric-inevitability/index.md` carries `> → Primary:` cross-volume pointers to Vol 1 and Vol 5 for these 3 refs |
| 12 | `\chapter*` for `00_summary_table.tex` produces blank `\ref` output | No impact on KB — `mass-defect-summary.md` leaf cited by slug path, not `\ref` |
| 13 | Local `bibliography.bib` alongside shared `../bibliography` | `lambda-higgs-derivation.md` leaf notes `\cite{pdg2022}` requires shared bibliography |

---

## 7. Acceptance Criteria

1. **Up-link completeness**: every file under `ave-kb/vol6/` except `ave-kb/vol6/index.md` contains a line matching `^\[↑ ` (grep-checkable). No dead ends in upward navigation.

2. **Depth constraint**: no file path under `ave-kb/vol6/` exceeds 4 slash-separated components below `ave-kb/`. Verifiable: `find ave-kb/vol6 -name "*.md" | awk -F/ 'NF>7 {print}'` produces empty output (path = `ave-kb/vol6/{section}/{element}/{leaf}` = 5 components = 4 levels below root).

3. **Entry-point token budget**: `wc -w ave-kb/entry-point.md` reports under 2200 words. Vol 6 contributes one paragraph to entry-point; adding that paragraph must not push entry-point over budget.

4. **Leaf identification**: every leaf file contains `<!-- leaf: verbatim -->` on line 2 (after up-link on line 1). Verifiable: `grep -rL "<!-- leaf:" ave-kb/vol6/` returns only index files (those containing `## Contents`).

5. **Element coverage**: exactly 14 element subdirectories exist under period-1/, period-2/, period-3/ (2 + 8 + 4 = 14). Verifiable: `find ave-kb/vol6/period-*/  -maxdepth 1 -type d | wc -l` = 14 (excluding the period directories themselves).

6. **Standard template coverage**: every element directory except neon, sodium, magnesium, aluminum contains exactly 6 leaf files. Neon, sodium, magnesium, aluminum contain exactly 7 leaf files (5 standard + 1 extra element-specific section + 1 semiconductor). Verifiable by file count per element directory.

7. **Framework equation coverage**: `ave-kb/vol6/framework/computational-mass-defect/index.md` surfaces all 8 labelled equations (`eq:d_proton`, `eq:d_intra`, `eq:k_mutual_expanded`, `eq:k_mutual`, `eq:coulomb_correction`, `eq:V_BR`, `eq:miller`, `eq:V_R`, `eq:semiconductor_mass`) and the resultbox title "Topologic Yield Mass Defect (Binding Energy Ceiling)". Verifiable by content inspection.

8. **Anomaly notes present**: the 5 anomalies with direct leaf impact (duplicate label, 3 missing chapter labels, oxygen orbital deviation, Python verbatim source, Fluorine/Silicon section title deviations) are each noted in the relevant index or leaf file. Not verifiable mechanically — review checklist item.

9. **Cross-volume refs are blockquoted**: all cross-volume references in `geometric-inevitability/index.md` use the `> → Primary:` blockquote format. Verifiable: `grep -n "Primary:" ave-kb/vol6/appendix/geometric-inevitability/index.md` returns 2 lines (Vol 1 and Vol 5).

10. **No CLAUDE.md domain-specific content**: applying the boundary test — every statement in `ave-kb/CLAUDE.md` must apply to ALL volumes without qualification. The 5 invariants identified in §1 of this design must each be verified against all other volume surveys before being written into `ave-kb/CLAUDE.md`. Invariants 1–4 are confirmed cross-volume; Invariant 5 (backmatter file name) is Vol 6-specific and must NOT be written into `ave-kb/CLAUDE.md`.

---

## File Count Summary

| Category | Index files | Leaf files |
|---|---|---|
| vol6/index.md | 1 | — |
| framework/ | 3 | 14 |
| period-1/ | 3 | 12 |
| period-2/ | 9 | 55 |
| period-3/ | 5 | 28 |
| appendix/ | 3 | 15 |
| **Total** | **24** | **124** |

Wait — recount from skeleton:

**Index files (navigation nodes):**
- vol6/index.md: 1
- framework/index.md: 1
- framework/computational-mass-defect/index.md: 1
- framework/chemistry-translation/index.md: 1
- period-1/index.md: 1
- period-1/hydrogen/index.md: 1
- period-1/helium/index.md: 1
- period-2/index.md: 1
- period-2/{8 elements}/index.md: 8
- period-3/index.md: 1
- period-3/{4 elements}/index.md: 4
- appendix/index.md: 1
- appendix/heavy-element-catalog/index.md: 1
- appendix/geometric-inevitability/index.md: 1
**Index total: 24**

**Leaf files (verbatim):**
- framework: mass-defect-summary (1) + executive-abstract (1) + 11 computational leaves + 3 chemistry leaves = 16
- period-1: 6 H + 6 He = 12
- period-2: 6 Li + 6 Be + 6 B + 6 C + 6 N + 6 O + 6 F + 7 Ne = 49
- period-3: 7 Na + 7 Mg + 7 Al + 6 Si = 27
- appendix: 5 heavy-catalog + 10 geometric-inevitability = 15
**Leaf total: 119**

**Grand total: 143 files**

---

*Correction note: `topological-area.md` for magnesium references `13_magnesium.tex` in the skeleton — this is a typo; the correct source is `14_magnesium.tex`. Distiller: use `14_magnesium.tex` for all 7 magnesium leaves.*
