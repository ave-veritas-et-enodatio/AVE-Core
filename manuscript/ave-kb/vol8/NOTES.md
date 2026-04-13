[↑ Vol 8: Virtual Media](index.md)
<!-- leaf: verbatim -->

# Vol 8 Local Notes

## Raw-Form Notation Policy

Vol 8 uses raw math forms ($Z_0$, $\mu_0$) directly throughout the source LaTeX. The shorthand macros `\Zvac`, `\permeability`, etc., used in other volumes do not appear in Vol 8, with a single exception: `\Zvac` at `08_discrete_manifold_masking.tex` line 48, which was translated to `$Z_0$` in the KB leaf (`masking-protocol.md`). All other Vol 8 math uses raw forms. Distillers must preserve raw forms; do not substitute shorthand macros.

## Z-Proportionality Inversion Scope

In physical and biological media, impedance scales inversely with amplitude: $Z \propto 1/A$ (low impedance = high throughput). In virtual media (LLM weight matrices), this relationship inverts: $Z \propto A$ (high amplitude = high impedance). This is the hardware/software isomorphism inversion, established in Ch.2 ("Where the Isomorphism Inverts"). The Axiom 4 saturation operator and the failure threshold at $r \geq 1.0$ remain universal across both regimes; only the directional coupling between $Z$ and $A$ reverses.

## Pending-Autotune Result Markers

Three leaves contain `<!-- status: pending-autotune -->` on line 3, indicating the source material had results marked as pending:

- `saturation-pruning/ch4-experimental-audit/quantitative-results.md` — calibrated maxima for 8B, 4B, 9B models are pending
- `saturation-pruning/ch5-global-ac-scope/global-ac-correction.md` — marker included per taxonomy requirement; pending items originate from ch4 and ch9 tables
- `architecture-analysis/ch9-gamma-scaling/autotune-results.md` — 8B autotune is pending; three table cells contain "pending" entries

These markers signal that the source content may be incomplete. An agent reading these leaves should not treat pending entries as confirmed results.
