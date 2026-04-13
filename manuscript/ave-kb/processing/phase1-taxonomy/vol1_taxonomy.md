# Phase 1 Taxonomy Design — Vol 1: Foundations and Universal Operators

**Produced by:** kb-taxonomy-architect
**Source survey:** `.claude/phase0-surveys/vol1_survey.md`
**Date:** 2026-04-02

---

## 1. CLAUDE.md Invariants (from Vol 1)

These concepts are defined in Vol 1 and used uniformly across ALL volumes. They belong in
`manuscript/ave-kb/CLAUDE.md`, not in any volume-specific document.

INVARIANT: Four-Axiom Set — The four AVE fundamental axioms (LC substrate, Topo-Kinematic
Isomorphism, Effective Action, Dielectric Saturation); these are the axiomatic root of every
volume (source: `ch:fundamental_axioms`, `eq:axiom1_impedance`–`eq:axiom4_saturation`)

INVARIANT: Vacuum Impedance — $Z_0$ (also written via `\Zvac`); the characteristic impedance
of the LC vacuum condensate; appears as a divisor or normalizer in all volumes
(source: ch.1, `eq:axiom1_impedance`)

INVARIANT: Node Length — $\ell_{node}$ (script ell, Vol 1 convention); the fundamental lattice
pitch; used as length scale across all volumes; NOTE: Vol 1 writes `\ell_{node}` (script ell),
all other volumes write `l_{node}` (roman l) — both mean the same quantity
(source: ch.1, `eq:axiom1_pitch`)

INVARIANT: Vacuum Porosity Ratio — $\alpha$ as packing fraction of the chiral SRS lattice;
defined from geometry alone; appears in quantum and atomic volumes as fine-structure
analogue (source: ch.1, `eq:axiom2_alpha`)

INVARIANT: Dielectric Yield Voltage — $V_{yield} \approx 43.65$ kV (defined formally in Vol 4
Ch.1 as `eq:axiom2_v_yield`); referenced here in ch.3 as "43.65 keV yield limit"; cross-volume
notation anchor (source: ch.3 §3.4.2; formal definition in Vol 4)

INVARIANT: Vacuum Manifold Symbol — $\mathcal{M}_A$ (NOT via `\vacuum` macro); all chapters
across all volumes write `$\mathcal{M}_A$` directly; macro `\vacuum` is defined but unused
(source: structure/commands.tex; confirmed ch.1–ch.7)

INVARIANT: Unifying AVE Master Equation — `eq:master_wave`; the single equation from which
all regime-specific behaviour is derived; cited across Vols 2–7 as the governing equation
(source: ch.4, `eq:master_wave`)

INVARIANT: Asymptotic Hubble Constant — $H_\infty = 69.32$ km/s/Mpc; derived from hardware
constants; referenced in cosmology, galactic, and engineering volumes
(source: ch.4, `eq:H_infinity`)

INVARIANT: Four Universal Regimes — the regime map $r = A/A_c$ partitioning I–IV; the
navigational backbone for all domain-specific derivations across all volumes; cross-referenced
as `ch:regime_map` (source: ch.7)

INVARIANT: Topo-Kinematic Dimensional Isomorphism — the table establishing that mechanical
and EM degrees of freedom are dimensionally exchangeable; this isomorphism is the basis of
Vol 5 biology and Vol 2 quantum derivations (source: ch.2 §2.3 table)

INVARIANT: Universal Operators Symbol Convention — Z (impedance), S (saturation), Γ (reflection
coefficient); the operator trio appears in all volumes; labels `sec:universal_impedance`,
`sec:universal_saturation`, `sec:universal_gamma` (source: ch.6)

**Total invariants identified: 11**

**CLAUDE.md boundary rationale:** All 11 pass the binary filter — none requires qualification
when applied to any single volume. Constants like $V_{snap} = 511.0$ kV and
$a_{genesis} = cH_\infty/2\pi$ are Vol 1 results but are only heavily used in Vols 3–4;
they belong in the vol1 domain document, not CLAUDE.md, unless the coordinator confirms
cross-volume use reaches the 2-volume minimum.

---

## 2. Volume Hierarchy Design

### Domain grouping rationale

Three content domains emerge naturally from the chapter structure:

**Domain A — `axioms-and-lattice` (Ch.1 + Ch.2)**
Ch.1 establishes the four axioms and the chiral SRS network architecture. Ch.2 derives
the macroscopic moduli (bulk modulus, shear modulus, dielectric snap limit) directly from
the Ch.1 lattice. These are inseparable as "what the vacuum IS" — the substrate definition.
Grouping them avoids scattering the constitutive relations across two sibling domains.

**Domain B — `dynamics` (Ch.3 + Ch.4)**
Ch.3 derives quantum mechanics, signal bandwidth, and wave-particle duality from the Ch.1–2
substrate. Ch.4 derives continuum electrodynamics, the Master Equation, dark sector, and
MOND from the same substrate. Both are "what the vacuum DOES" — dynamic behaviour. The
inverted logical dependency (Ch.3 uses $\rho_{bulk}$ from Ch.4) is a content-ordering
note for the distiller, not a structural problem; the chapters belong together by theme.

**Domain C — `operators-and-regimes` (Ch.5 + Ch.6 + Ch.7)**
Ch.5 establishes the universal spatial tension ($M \propto 1/r$) and scale invariance.
Ch.6 defines the 8 universal operators (Z, S, Γ, etc.). Ch.7 assembles these into the
full regime map and domain control catalog. Together they form "the universal toolkit"
— agents navigating to a specific operator or regime land here. This domain is the
primary navigation target from other volumes.

**Ch.0 — Introduction**: no resultboxes, no labels, ~55 lines. Treated as a single
standalone leaf attached directly to the volume index, not assigned to any domain.

**Backmatter**: shared appendices (`full_derivation_chain`, `geometric_inevitability`,
`solver_toolchain`, `translation_*.tex`) appear in multiple volumes. They live at
`ave-kb/common/` with a single authoritative position per appendix. Vol 1 domain
documents cross-reference them but do not own them. See §5 (Shared Content Decision).

### Depth assessment

With 55–70 leaves across 7 chapters grouped into 3 domains, the 4-level maximum
(vol1/index → domain/index → chapter/index → leaf) is fully adequate. No 5th level
is warranted: even the densest chapter (Ch.3, ~17 resultboxes → ~17 leaves) fits
comfortably as siblings under a single chapter index.

---

## 3. Document Skeleton

### Conventions used in this skeleton
- `[index]` = navigation node, never verbatim content
- `[leaf — verbatim]` = terminal document, source content translated not summarized
- `[leaf — placeholder]` = structural position present but source not yet leaf-level confirmed
- All paths relative to `manuscript/ave-kb/`

```
ave-kb/
  CLAUDE.md                          [invariant] cross-cutting notation, 11 invariants from Vol 1 + additions from Vols 2–8
  entry-point.md                     [index] top-level KB anchor; one paragraph per volume, link to each vol index; target <3000 tokens

  common/
    index.md                         [index] shared backmatter and translation resources; links to appendix leaves
    full-derivation-chain.md         [leaf — verbatim] source: backmatter/02_full_derivation_chain.tex; complete AVE derivation chain (label: app:full_derivation_chain)
    geometric-inevitability.md       [leaf — verbatim] source: backmatter/03_geometric_inevitability.tex; proof that K4/SRS geometry is topologically forced
    mathematical-closure.md          [leaf — verbatim] source: backmatter/12_mathematical_closure.tex; system verification trace (label: app:verification)
    solver-toolchain.md              [leaf — verbatim] source: backmatter/05_universal_solver_toolchain.tex; universal solver toolchain (label: app:solver_toolchain); contains eq:ave_qnm_eigenvalue
    appendices-overview.md           [leaf — verbatim] source: backmatter/01_appendices.tex preamble; App A–E overview and translation matrix index (label: app:translation_matrix)
    translation-em.md                [leaf — verbatim] source: common/translation_em.tex (or equivalent); EM domain translation table
    translation-gravity.md           [leaf — verbatim] source: common/translation_gravity.tex; gravity domain translation table
    translation-nuclear.md           [leaf — verbatim] source: common/translation_nuclear.tex; nuclear domain translation table
    translation-quantum.md           [leaf — verbatim] source: common/translation_quantum.tex; quantum domain translation table
    translation-thermo.md            [leaf — verbatim] source: common/translation_thermo.tex; thermodynamic domain translation table
    translation-bcs.md               [leaf — verbatim] source: common/translation_bcs.tex; BCS/superconducting domain translation table
    translation-galactic.md          [leaf — verbatim] source: common/translation_galactic.tex; galactic rotation domain translation table
    translation-grav-waves.md        [leaf — verbatim] source: common/translation_grav_waves.tex (or equivalent); gravitational wave domain translation table
    experiments-appendix.md          [leaf — verbatim] source: common/appendix_experiments.tex; unified experimental falsification index (label: app:unified_experiments)

  vol1/
    index.md                         [index] Vol 1 summary; one paragraph per domain + Ch.0; links to domain indices and ch0-intro leaf; key results: 4 axioms, Master Equation, Regime Map
    ch0-intro.md                     [leaf — verbatim] source: 00_intro.tex; contextualizing AVE in topological physics; unnumbered chapter, no labels

    axioms-and-lattice/
      index.md                       [index] Domain A summary; axiom definitions, lattice constants, moduli derivation; key results from Ch.1 and Ch.2; links to ch1 and ch2 indices

      ch1-fundamental-axioms/
        index.md                     [index] Ch.1 summary; cutoff scales, 4 axioms, LC condensate, porosity ratio, derivation pipeline; links to all ch1 leaves
        axiom-definitions.md         [leaf — verbatim] source: ch.1 §"The Four Fundamental Axioms"; verbatim axiom statements with labels eq:axiom1_impedance, eq:axiom1_pitch, eq:axiom2_alpha, eq:axiom2_v_yield, eq:axiom3_gravity, eq:axiom3_refraction, eq:axiom4_saturation
        calibration-cutoff-scales.md [leaf — verbatim] source: ch.1 §"The Calibration of the Effective Cutoff Scales"; three cutoff scales ($\ell_{node}$, $\alpha$, $G$); resultboxes for each
        lc-condensate-vacuum.md      [leaf — verbatim] source: ch.1 §"The Vacuum as an LC Resonant Condensate"; planck artifact vs. topological coherence; porosity ratio $\alpha$; resultboxes
        zero-parameter-universe.md   [leaf — verbatim] source: ch.1 §"The Pathway to a Zero-Parameter Universe"; resultbox for zero-parameter claim
        kirchhoff-network-method.md  [leaf — verbatim] source: ch.1 §"Methodology: Explicit Discrete Kirchhoff Execution"; network mapping, Laplacian integration, master constants pipeline table (fig:calibration_flowchart)
        lattice-structure.md         [leaf — verbatim] source: ch.1 §"The Network Mapping" subsections + fig:lattice_3d, fig:rigidity_alpha, fig:equilibrium_G; chiral SRS net geometry; topological conversion constant $\xi_{topo}=e/\ell_{node}$

      ch2-macroscopic-moduli/
        index.md                     [index] Ch.2 summary; implosion paradox, constitutive moduli, dielectric snap limit; key results: $V_{snap}=511.0$ kV, $\mathcal{R}_{OB}\approx1.673$; links to ch2 leaves
        implosion-paradox.md         [leaf — verbatim] source: ch.2 §"The Implosion Paradox: Why The Vacuum Must Be Micropolar"; resultboxes establishing micro-polar necessity
        constitutive-moduli.md       [leaf — verbatim] source: ch.2 §"The Constitutive Moduli of the Void"; bulk modulus K, shear modulus G, discrete Voronoi cell, packing fraction $p_c=8\pi\alpha$; resultboxes; fig:emt_landscape
        topo-kinematic-isomorphism.md [leaf — verbatim] source: ch.2 §2.3 table "Topo-Kinematic Dimensional Isomorphism"; verbatim table mapping mechanical ↔ EM degrees of freedom
        dielectric-rupture.md        [leaf — verbatim] source: ch.2 §"Dielectric Rupture and The Volumetric Energy Collapse"; resultboxes for over-bracing factor and volumetric collapse
        dielectric-snap-limit.md     [leaf — verbatim] source: ch.2 §"The Dielectric Snap Limit ($V_{snap}=511.0$ kV)"; resultbox for $V_{snap}$; computational proof of over-bracing

    dynamics/
      index.md                       [index] Domain B summary; quantum formalism, signal dynamics, master equation, dark sector, MOND; key results: eq:master_wave, eq:H_infinity, GUP, Born Rule, entanglement mechanism; links to ch3 and ch4 indices

      ch3-quantum-signal-dynamics/
        index.md                     [index] Ch.3 summary; dielectric Lagrangian, GUP, Schrödinger derivation, wave-particle duality, entanglement; 17 resultboxes; links to ch3 leaves; note on forward reference to $\rho_{bulk}$ (ch.4)
        dielectric-lagrangian.md     [leaf — verbatim] source: ch.3 §"The Dielectric Lagrangian: Hardware Mechanics"; vector potential as mass flow rate; resultboxes; dimensional proof
        paley-wiener-hilbert.md      [leaf — verbatim] source: ch.3 §"The Paley-Wiener Hilbert Space"; bandwidth → quantum; resultboxes establishing Hilbert space construction
        gup-derivation.md            [leaf — verbatim] source: ch.3 §"The Generalized Uncertainty Principle (GUP)"; GUP from discrete commutator; resultboxes; fig:gup_resolution
        schrodinger-from-circuit.md  [leaf — verbatim] source: ch.3 §"Deriving the Schrödinger Equation from Circuit Resonance"; Klein-Gordon as resonance; paraxial reduction; resultboxes
        zero-impedance-boundary.md   [leaf — verbatim] source: ch.3 §"Wave-Particle Duality and The Zero-Impedance Boundary"; $0\,\Omega$ boundary condition; internal confinement; Pauli exclusion as $\Gamma=-1$; fig:double_slit_comparison
        quantum-foam-virtual.md      [leaf — verbatim] source: ch.3 §"The Physical Origin of Quantum Foam and Virtual Particles"; RMS thermal noise interpretation; failed topologies; resultboxes
        ohmic-decoherence-born.md    [leaf — verbatim] source: ch.3 §"Deterministic Interference and The Measurement Effect"; Ohmic decoherence; Born rule derivation; fig:double_slit_wake
        nonlinear-telegrapher.md     [leaf — verbatim] source: ch.3 §"Non-Linear Dynamics and Topological Shockwaves"; eq:nonlinear_wave (the one labelled resultbox in ch.3); Euler-Heisenberg $E^4$ correction
        entanglement-mechanism.md    [leaf — verbatim] source: ch.3 §"Classical Causality of Quantum Entanglement (Bell's Theorem)"; topological phase-locked thread; $\Gamma=-1$ gear train; CHSH $= 2\sqrt{2}$; no-signaling theorem; resultboxes; fig:vacuum_dielectric_saturation

      ch4-continuum-electrodynamics/
        index.md                     [index] Ch.4 summary; master equation, operating regimes, saturation transition, MOND, Bullet Cluster; key results: eq:master_wave, eq:H_infinity, $a_{genesis}$; links to ch4 leaves
        master-equation.md           [leaf — verbatim] source: ch.4 §"The Unifying Master Equation"; eq:master_wave verbatim; resultboxes
        lc-electrodynamics.md        [leaf — verbatim] source: ch.4 §"Continuum Electrodynamics of the LC Condensate"; mass density $\rho_{bulk}$; kinematic mutual inductance $\nu_{kin}$; resultboxes
        operating-regimes-table.md   [leaf — verbatim] source: ch.4 §"Analytical Operating Regimes of the Vacuum" table "Formal Operating Regime Classification"; verbatim regime table; fig:operating_regimes
        magnetic-saturation.md       [leaf — verbatim] source: ch.4 §"The Macroscopic Yield Limit: The Magnetic Saturation Transition"; asteroid belts and Oort clouds; Sagnac-RLVE falsification; fig:dielectric_avalanche
        mond-hoop-stress.md          [leaf — verbatim] source: ch.4 §"Deriving MOND from Unruh-Hawking Hoop Stress" (label: sec:galactic_saturation); $a_{genesis}=cH_\infty/2\pi$; eq:H_infinity; resultboxes; fig:unruh_hawking_hoop_stress
        dark-sector.md               [leaf — verbatim] source: ch.4 §"Deriving MOND..." Dark Sector Comparison table; kinematic mutual inductance as dark matter; resultboxes
        bullet-cluster.md            [leaf — verbatim] source: ch.4 §"The Bullet Cluster: Refractive Tensor Shockwaves"; DAMA/LIBRA vs. XENONnT resolution; resultboxes

    operators-and-regimes/
      index.md                       [index] Domain C summary; universal spatial tension, 8 universal operators, regime map; key results: scale invariance theorem, operator definitions, domain catalog; links to ch5, ch6, ch7 indices

      ch5-universal-spatial-tension/
        index.md                     [index] Ch.5 summary; mass unification, scale invariance, FDTD proof; 3 resultboxes; links to ch5 leaves
        mass-unification.md          [leaf — verbatim] source: ch.5 §"The Unification of Mass"; $M\propto1/r$ derivation; vacuum compliance scalar $K\equiv\hbar/c$; resultboxes
        scale-invariance.md          [leaf — verbatim] source: ch.5 §"Scale Invariance across the Framework"; lepton tension limit; nuclear tension limit; fig:cross_scale; theorem-like framebox (no label)
        scale-invariant-predictions.md [leaf — verbatim] source: ch.5 §"Continuous FDTD Yee Lattice Proof" table "Scale-Invariant Mass Predictions"; verbatim prediction table; fig:fdtd_yee_lattice, fig:neon20_geometry
        fdtd-yee-proof.md            [leaf — verbatim] source: ch.5 §"Continuous FDTD Yee Lattice Proof" body; FDTD Yee lattice as continuous limit proof; resultboxes

      ch6-universal-operators/
        index.md                     [index] Ch.6 summary; 8 universal operators with labels and equations; key results: eq:saturation_sigma, eq:universal_gamma, eq:universal_pairwise, eq:y_to_s, eq:eigenvalue_target, eq:rg_target, eq:gamma_pack; links to ch6 leaves
        impedance-operator.md        [leaf — verbatim] source: ch.6 §"The Universal Impedance Operator" (label: sec:universal_impedance); eq:universal_impedance; resultboxes
        saturation-operator.md       [leaf — verbatim] source: ch.6 §"The Universal Saturation Operator" (label: sec:universal_saturation); eq:saturation_sigma, eq:universal_saturation; resultboxes
        reflection-coefficient.md    [leaf — verbatim] source: ch.6 §"The Universal Reflection Coefficient" (label: sec:universal_gamma); eq:universal_gamma, eq:universal_reflection; resultboxes
        pairwise-potential.md        [leaf — verbatim] source: ch.6 §"The Universal Pairwise Potential" (label: sec:universal_pairwise); eq:universal_pairwise; resultboxes
        y-to-s-conversion.md         [leaf — verbatim] source: ch.6 §"The Universal Y-to-S Conversion" (label: sec:universal_y_to_s); eq:y_to_s; multiport S-matrix; resultboxes
        eigenvalue-target.md         [leaf — verbatim] source: ch.6 §"The Universal Eigenvalue Target" (label: sec:universal_eigenvalue); eq:eigenvalue_target; resultboxes
        spectral-analyser.md         [leaf — verbatim] source: ch.6 §"The Universal Spectral Analyser" (label: sec:universal_spectral); resultboxes
        packing-reflection.md        [leaf — verbatim] source: ch.6 §"The Universal Packing Reflection" (label: sec:universal_packing); eq:rg_target, eq:gamma_pack; resultboxes; note: unlabelled scale-invariance framebox near this section

      ch7-regime-map/
        index.md                     [index] Ch.7 summary; 4 universal regimes, domain control parameter catalog (8 domains), regime equation sets, dimensional analysis; key results: eq:S_taylor, domain catalog; links to ch7 leaves
        four-regimes.md              [leaf — verbatim] source: ch.7 §"The Four Universal Regimes"; regime I–IV definitions ($r=A/A_c$); semiconductor analogy; perturbative expansion (Regime I); resultboxes
        domain-catalog.md            [leaf — verbatim] source: ch.7 §"Domain Control Parameter Catalog" (label: sec:domain_catalog); verbatim 8-domain table (EM/dielectric, EM/field, gravitational, BCS, magnetic, nuclear, grav-waves, galactic rotation)
        regime-equation-sets.md      [leaf — verbatim] source: ch.7 §"Regime-Specific Equation Sets"; verbatim equation sets per regime; resultboxes; eq:S_taylor
        dimensional-analysis.md      [leaf — verbatim] source: ch.7 §"Cross-Domain Dimensional Analysis" (label: sec:dimensional_analysis); dimensional consistency checks across domains; resultboxes
        experimental-design-space.md [leaf — verbatim] source: ch.7 §"The Experimental Design Space"; fig:regime_design_space; experimental parameter windows per regime
```

---

## 4. Navigation Spec

### Up-link format

Every document except `entry-point.md` carries exactly one up-link as line 1:

```
[↑ Vol 1: Foundations](../../index.md)                    ← from domain index
[↑ Axioms and Lattice](../index.md)                       ← from chapter index
[↑ Ch.1: Fundamental Axioms](../index.md)                 ← from leaf
```

Full chain examples:

```
entry-point.md (no up-link — root)
  vol1/index.md                         → [↑ Entry Point](../entry-point.md)
    vol1/axioms-and-lattice/index.md    → [↑ Vol 1: Foundations](../index.md)
      vol1/axioms-and-lattice/ch1-.../index.md → [↑ Axioms and Lattice](../index.md)
        vol1/axioms-and-lattice/ch1-.../axiom-definitions.md → [↑ Ch.1: Fundamental Axioms](../index.md)
```

For common/ documents:
```
  common/index.md                       → [↑ Entry Point](../entry-point.md)
    common/full-derivation-chain.md     → [↑ Common Resources](../index.md)
```

### Down-link format

Index documents list children in a `## Contents` section at the bottom:

```markdown
## Contents

- [Axioms and Lattice](axioms-and-lattice/index.md) — LC substrate definition, 4 axioms, macroscopic moduli
- [Dynamics](dynamics/index.md) — quantum formalism, master equation, dark sector
- [Operators and Regimes](operators-and-regimes/index.md) — universal operators, regime map
- [Ch.0: Introduction](ch0-intro.md) — contextualizing AVE; unnumbered; no resultboxes
```

### Cross-volume reference format

Two tiers, both in blockquote:

```markdown
> → Primary: [Universal Operators (Vol 1 Ch.6)](../../vol1/operators-and-regimes/ch6-universal-operators/index.md)
```
Use `→ Primary:` when the target defines a concept required to understand the current document.

```markdown
> ↗ See also: [Hydrogen Bond Derivation (Vol 5 Ch.2)](../../vol5/molecular/ch2-hydrogen-bonds/index.md)
```
Use `↗ See also:` for thematically related content that is not a hard dependency.

Cross-volume references from Vol 1 documents:
- Ch.1 §1.4 prose reference to Vol II → `↗ See also: [Vol 2: Subatomic](../../vol2/index.md)` (no specific label available)
- Ch.3 §3.4.2 "43.65 keV yield limit derived in Volume III, Chapter 1" → `→ Primary: [Vol 3 Ch.1 dielectric yield](../../vol3/...)` (label pending Vol 3 taxonomy)
- Ch.5 §5.2.1 "derived in full in Volume II, Chapter 5" → `↗ See also: [Vol 2 Ch.5](../../vol2/...)`
- Ch.4 §4.3.2 "PONDER-01 falsification bounds, Chapter 13" → `↗ See also: [Vol 4 Ch.13](../../vol4/...)` (Anomaly 3 — likely Vol IV)
- Ch.2 §2.2 "Chapter 12" reference → **no cross-reference link** until source resolved (Anomaly 2 — stale)

---

## 5. Shared Content Decision

**Recommendation: (a) Dedicated `ave-kb/common/` pages, referenced from each volume.**

Reasoning:
1. The backmatter files (`backmatter/02_full_derivation_chain.tex`,
   `backmatter/03_geometric_inevitability.tex`, `backmatter/12_mathematical_closure.tex`,
   `backmatter/05_universal_solver_toolchain.tex`) are shared files in the source tree — they
   are `\input`'d by multiple volumes. Duplicating them would create 8 divergent copies of
   verbatim content; if a distiller corrects an error in one copy, the others rot.

2. The `common/translation_*.tex` files are explicitly in the `common/` source directory.
   They are cross-domain reference tables — an agent navigating from any volume to check
   a dimensional equivalence should follow a single canonical path.

3. The single-authority pattern means link accuracy is checkable: if
   `ave-kb/common/full-derivation-chain.md` exists and all volume documents point to it,
   a grep for dead links finds all violations in one pass.

4. The `entry-point.md` → `common/index.md` → leaf path costs at most 2 hops from root,
   which is acceptable given the cross-cutting nature of the content.

**Exception**: `app:resolving_paradoxes` (App B: Theoretical Stress Tests) and
`app:computational_graph` are lightly cited and primarily relevant to Vol 1. If the
coordinator finds they appear only in Vol 1, they may move to `vol1/` to avoid cluttering
`common/`. This is a coordinator decision; the skeleton above places them in `common/`
as the conservative choice.

**Translation table file names** (Anomaly 8 — files not independently surveyed): The 8
translation table leaf filenames above (`translation-em.md`, etc.) are based on the 8 domains
listed in the ch.7 domain catalog. The distiller must confirm exact source filenames when
`common/translation_*.tex` files are opened. If the file count or naming differs, adjust
accordingly — the structural position is correct.

---

## 6. Acceptance Criteria

1. **Up-link completeness**: every file under `ave-kb/vol1/` except `vol1/index.md` contains
   a line matching `^\[↑ ` as its first non-empty line. Shell check:
   `find manuscript/ave-kb/vol1 -name "*.md" ! -name "index.md" -path "*/vol1/index.md" -prune -o -print | xargs grep -L '^\[↑ '`
   must return empty.

2. **Entry-point token budget**: `wc -w manuscript/ave-kb/entry-point.md` returns ≤ 2200
   (conservative 3000-token proxy). If exceeded, trim domain summaries — do not add content.

3. **Depth ceiling**: no file path under `ave-kb/vol1/` has more than 4 `/`-separated
   components after the `ave-kb/` prefix. Shell check:
   `find manuscript/ave-kb/vol1 -name "*.md" | awk -F/ 'NF-NF>4 {print}'`
   (equivalently: `awk -F/ '{if (NF > base+4) print}'` where base is the depth of `ave-kb/`).

4. **Leaf marker presence**: every leaf document (non-index, non-entry-point) contains
   `<!-- leaf: verbatim -->` on line 2. Shell check:
   `find manuscript/ave-kb/vol1 -name "*.md" ! -name "index.md" | xargs grep -L '<!-- leaf:'`
   must return only files intentionally excluded (none expected under vol1/).

5. **Leaf content fidelity**: no leaf document under `ave-kb/vol1/` contains a `## Summary`
   or `## Overview` heading (which would signal summarization rather than verbatim
   translation). Shell check:
   `grep -rl '^## Summary\|^## Overview' manuscript/ave-kb/vol1/` must return empty.

6. **CLAUDE.md invariant coverage**: each of the 11 invariants listed in §1 is referenced
   in at least 2 distinct volume subtrees in `ave-kb/`. Verifiable post-synthesis when
   all volumes are complete.

7. **All 64 resultboxes represented**: the distiller's leaf set must account for all ~64
   resultboxes from the main matter survey. The chapter-level resultbox counts are:
   Ch.1: 9, Ch.2: 8, Ch.3: 17, Ch.4: 15, Ch.5: 3, Ch.6: 6 (named results for 8 operators
   → 8 leaves covering them), Ch.7: 2 + regime table. Some leaves cover multiple
   resultboxes when they appear in the same section; the distiller must note any resultbox
   not covered by at least one leaf.

8. **Vol 1 volume index key results**: `ave-kb/vol1/index.md` must list at minimum: the
   4 axiom labels, `eq:master_wave`, `eq:H_infinity`, and a link to the regime map. An
   agent reading only `vol1/index.md` should know all major results exist and where to find
   them without reading any domain index.

9. **No orphaned backmatter**: all 5 backmatter appendices (`app:full_derivation_chain`,
   `app:verification`, `app:geometric_inevitability`, `app:solver_toolchain`,
   `app:translation_matrix`) have corresponding leaf files under `ave-kb/common/` and are
   linked from `ave-kb/common/index.md`.

10. **Cross-references are blockquoted**: every cross-volume reference in vol1 documents
    uses either `> → Primary:` or `> ↗ See also:` blockquote format. Prose-embedded cross-
    references are a navigation failure — they are invisible to an agent scanning for
    dependency links.

---

## 7. Anomaly Impact on Taxonomy

| # | Anomaly | Taxonomy Impact |
|---|---------|-----------------|
| 1 | Ch.0 entirely unnumbered | Leaf at vol1/ root (`ch0-intro.md`), not assigned to a domain; no resultboxes means no sub-leaves |
| 2 | "Chapter 12" reference in ch.2 unresolved | No cross-reference link added; distiller adds a note comment in `dielectric-rupture.md` |
| 3 | "Chapter 13" (PONDER-01) in ch.4 unresolved | `↗ See also:` placeholder pointing to Vol 4 top-level until Vol 4 taxonomy confirms exact path |
| 4 | Inverted logical dependency ch.3 uses $\rho_{bulk}$ from ch.4 | Note in `ch3-.../index.md`; no structural reordering; `→ Primary:` link from `schrodinger-from-circuit.md` or `paley-wiener-hilbert.md` to `lc-electrodynamics.md` |
| 5 | summarybox/exercisebox not used | No structural impact; exercises stay as plain text within chapter leaves if included |
| 6 | amsthm zero instances; one raw framebox in ch.6 | Scale invariance framebox content absorbed into `packing-reflection.md` or `scale-invariance.md` (nearest contextual leaf); distiller notes absence of label |
| 7 | All 11 macros unused | No macro substitution step for vol1 distillation; CLAUDE.md notes both macro and direct form |
| 8 | translation_*.tex not independently surveyed | Leaf filenames provisional; distiller confirms source filenames before writing; structural position (`common/`) is fixed |
| 9 | `app:full_derivation_chain` is vol1-first-class | Placed in `common/` not `vol1/`; `vol1/index.md` carries `→ Primary:` link to it |
| 10 | Backmatter inclusion varies by volume | All backmatter leaves in `common/`; per-volume inclusion differences are noted in each volume's domain index, not modeled structurally |
| 11 | Only `eq:nonlinear_wave` has resultbox title AND label | Distiller notes this in `nonlinear-telegrapher.md`; no structural consequence |
| 12 | Foreword resultbox "Applied Vacuum Unifying Equation" has no label | Not placed in vol1/ hierarchy (foreword is frontmatter invariant); if substantial, add a leaf under `common/` or `vol1/` — coordinator decision |

---

## 8. File Count Summary

| Category | Count |
|----------|-------|
| `ave-kb/CLAUDE.md` | 1 |
| `ave-kb/entry-point.md` | 1 |
| `ave-kb/common/` index | 1 |
| `ave-kb/common/` leaves | 14 (5 backmatter + 8 translation + 1 experiments) |
| `vol1/index.md` | 1 |
| `vol1/ch0-intro.md` (leaf) | 1 |
| Domain indices (3) | 3 |
| Chapter indices (7) | 7 |
| Leaves under ch1 | 6 |
| Leaves under ch2 | 5 |
| Leaves under ch3 | 9 |
| Leaves under ch4 | 7 |
| Leaves under ch5 | 4 |
| Leaves under ch6 | 8 |
| Leaves under ch7 | 5 |
| **Vol 1 subtotal (indices + vol-root leaves)** | **12 index files + 46 leaf files** |
| **Grand total (including common/, CLAUDE.md, entry-point)** | **~76 files** |

Note: the 46 vol1 leaves cover the ~64 resultboxes by grouping related resultboxes within the
same section into a single leaf. The distiller should not split leaves finer than section
boundaries unless a single section exceeds ~2000 tokens.
