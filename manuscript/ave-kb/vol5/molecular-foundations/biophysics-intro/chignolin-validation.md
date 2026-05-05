[↑ Biophysics Introduction](../index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: u4vmgk, a3rby3 -->

---

## Validation: Chignolin (CLN025)

The 10-residue Chignolin mini-protein (CLN025: YYDPETGTWY) is the benchmark system for the AVE folding engine (Volume V). Using zero adjustable parameters, the engine folds from an extended chain to a $\beta$-hairpin with:

<!-- claim-quality: u4vmgk -->
> **[Resultbox]** *Chignolin Validation*
>
> $$
> \text{RMSD}_{\text{backbone}} = 2.59 \text{ Å} \quad \text{(sub-3 Å: Level 6 Emergence)}
> $$

<!-- claim-quality: a3rby3 (this engine validation runs the protein-folding $S_{11}$ free-energy functional — Vol 5's namespace-collision use of $S_{11}$ vs the EE reflection-coefficient meaning is flagged in the cross-cutting notation-hazard entry) -->
This validation uses the *same three functions* as every other chapter in this volume: `impedance()`, `saturation_factor()`, and `reflection_coefficient()`. The protein backbone is not "biology" — it is a transmission line.

---
