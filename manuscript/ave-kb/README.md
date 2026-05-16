# Applied Vacuum Engineering — Knowledge Base

The AVE KB is a navigable Markdown distillation of an 8-volume LaTeX physics manuscript. It is organized for reference and cross-volume navigation by readers already familiar with the source material — it is not an introduction to AVE theory.

> **⚡ A-034 Canonical (2026-05-15 evening): Universal Saturation-Kernel
> Strain-Snap Mechanism.** Axiom 4's saturation kernel $S(A) = \sqrt{1-A^2}$
> is the universal mechanism governing every topological-reorganization
> event at every scale. **19 canonical instances span 21 orders of
> magnitude** (atomic dielectric breakdown → BCS superconductivity at
> 0.00% error → solar flares NOAA 40-yr validated → BH ring-down 1.7%
> from GR → cosmic K4 crystallization). Per Grant 2026-05-15: *"the
> bulk response of the lattice to strain is universal."* See [common/
> trampoline-framework §7.5](common/trampoline-framework.md), Vol 3 Ch 4
> §sec:tki_strain_snap, backmatter Ch 7 (`07_universal_saturation_kernel.tex`),
> and L5 [`research/L5/axiom_derivation_status.md`](../../research/L5/axiom_derivation_status.md)
> A-034 for the canonical entries.

[Usage](#using-the-system) is in the last section of this README.

## What the KB Contains

The manuscript derives all physical observables — particle masses, coupling constants, bond energies, cosmological parameters — from four topological axioms plus three canonical hardware scales ($\ell_{node}$, $\alpha$, $G$), all three of which are themselves derived (see Vol 1 Ch 8 for the Golden Torus derivation of $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$). The KB distills the manuscript into leaf documents (verbatim LaTeX→Markdown translation) organized under a hierarchy of index documents.

## Hierarchy

The KB is 3–5 levels deep:

```
entry-point.md
└── vol{N}/index.md                    (volume index)
    └── vol{N}/{domain}/index.md       (domain index)
        └── vol{N}/{domain}/{chapter}/index.md   (chapter index)
            └── vol{N}/{domain}/{chapter}/{leaf}.md  (leaf)
```

Not every volume uses all five levels. Some domains collapse chapter and domain into a single index.

## Navigating

**Start at `entry-point.md`.** Each index level carries two navigation sections:

- `## Key Results` — verbatim table of what this node covers, taken directly from the source
- `## Derivations and Detail` — table of links to child documents with one-line descriptions

**Exception — navigation-pointer indexes:** Two indexes contain no original results and substitute a `> **Navigation note:**` blockquote for `## Key Results`, stating explicitly that results reside in the destination leaves (`common/translation-tables/index.md`, `vol5/common/index.md`). Absence of `## Key Results` is not a defect if a Navigation note is present.

**Exception — `entry-point.md`:** The top-level entry point uses inline key results per volume rather than a `## Key Results` table. It is a special case and does not follow the two-section index pattern.

Follow down-links to go deeper. Follow the `[↑ Parent]` up-link on line 1 of any document to reorient.

**Cross-volume references** appear at the bottom of index and leaf documents:

- `> → Primary:` — required dependency; the linked document must be read to understand the current one
- `> ↗ See also:` — optional suggestion; related content that is not a prerequisite

## Cross-Cutting Invariants

`ave-kb/CLAUDE.md` documents invariants that apply across all volumes: notation ($\mathcal{M}_A$, $\ell_{node}$, Op-N operators), tcolorbox rendering rules, axiom numbering, physical constants, and cross-reference format conventions. Read it before navigating across volumes; it resolves notation ambiguities that arise from the multi-volume scope.

## Leaf Documents

Every leaf document begins:

```
[↑ Parent Name](../index.md)
<!-- leaf: verbatim -->
```

The `<!-- leaf: verbatim -->` marker means the content is a direct LaTeX→Markdown translation with no editorial changes. Equations, table values, and structural choices reflect the source exactly.

Cross-volume reference target leaves carry a third structural annotation on line 3: `<!-- path-stable: referenced from {vol} as {label} -->`. See `CONVENTIONS.md` for the full PATH-STABLE spec (INVARIANT-S6).

## Common Resources

`ave-kb/common/` holds shared content not owned by any volume: the unified experimental falsification index, full derivation chain, mathematical closure documents, solver toolchain reference, and domain translation tables.

## Volume Index

| Volume | Contents |
|---|---|
| [Vol 1: Foundations](vol1/index.md) | $\mathcal{M}_A$ vacuum lattice, four axioms, nonlinear dielectric saturation, transmission line mathematics. Derives $\ell_{node}$, $p_c$, $Z_0$, $H_\infty$, and the master equation. |
| [Vol 2: The Subatomic Scale](vol2/index.md) | Fermionic particles as Faddeev-Skyrme solitons. Baryon masses, lepton masses, electroweak mixing, PMNS matrix, quark fractional charges. |
| [Vol 3: Macroscopic Physics](vol3/index.md) | Gravity, relativity, condensed matter, and cosmology as impedance-matching regimes. GR field equations from trace-reversed TLM; superconductivity, melting point of water, galactic rotation. |
| [Vol 4: Applied Vacuum Engineering](vol4/index.md) | Engineering translation into falsifiable hardware via the Vacuum Circuit Analysis framework. Chiral antennas, ponderomotive thrusters, topological SMES, SPICE simulation suite. |
| [Vol 5: Topological Biology](vol5/index.md) | Zero-free-parameter biology from AVE axioms. Amino acids as SPICE circuits; protein folding as $S_{11}$ minimization; validated against 20 PDB structures. |
| [Vol 6: Periodic Table of Knots](vol6/index.md) | Nuclear masses and 3D geometries for $Z=1$–119 via AVE mutual impedance summation. Explicit alpha-particle cluster placement; semiconductor-regime classification. |

## Using the System

* Start the agent

```bash
# from project root
claude --model opus --effort max --agent kb-docent manuscript/ave-kb
```

OR

```bash
# from this directory
claude --model opus --effort max --agent kb-docent .
```

Note: agent defaults to opus

* initiate the session

```bash
> /kb-start

  Searched for 2 patterns, read 3 files (ctrl+o to expand)

⏺ Ready. No previously explored topics on record. What would you like to explore?

  The KB covers six volumes of the AVE framework:

  1. Foundations — vacuum lattice, four axioms, master equation
  2. Subatomic Scale — particle masses, electroweak mixing, neutrino sector
  3. Macroscopic Physics — gravity, cosmology, condensed matter
  4. Applied Vacuum Engineering — circuit theory, hardware programs, simulation
  5. Topological Biology — amino acid circuits, protein folding, H-bond derivation
  6. Periodic Table of Knots — nuclear masses, alpha-cluster geometries

  Plus shared common resources (translation tables, experimental falsification index, derivation chains).

>
``` 

Ask your question and begin the exploration process. When you're done with a particular topic:

```bash
> /kb-next [optional-new-question]
```

Use `/kb-next` with no arguments to close out a session (will save state of current topic). when docent asks for next topic to write to ave-kb/session/new_topic.md just tell it you are done (if you're feeling polite) or close the terminal.

You can revisit any previous topic - it will be listed under `ave-kb/session/*.md`

**recommended**: set up status line monitoring of model and context usage

* install jq - ```brew install jq```

```bash
> /statusline show model name and context percentage with a progress bar
```

claude code will ask to create a ~/.claude shell script and modify settings.json.
you will not need to restart to see the status bar.
