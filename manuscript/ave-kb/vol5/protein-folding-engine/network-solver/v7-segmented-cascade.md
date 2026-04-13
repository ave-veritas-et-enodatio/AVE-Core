[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Segmented Cascade Solver (v7)

## The NERF Error Propagation Problem

The backbone is constructed serially via the NERF algorithm: changing torsion angle $\varphi_1$ rigidly rotates all downstream atoms ($i = 2, 3, \ldots, N$). The gradient $\partial S_{11}/\partial\varphi_1$ is therefore dominated by a geometric lever-arm artifact, not the local impedance mismatch signal.

For small chains ($N \leq Q = 7$), the lever arm is bounded and the v4 Adam solver converges reliably (loss $\approx 1/Q^2$). For larger chains, the gradient signal is corrupted by downstream propagation, causing the global optimizer to find compensatory solutions rather than true impedance minima.

## Segmented Cascade Architecture

The backbone quality factor $Q = 7$ defines the **coherence length**---the number of residues over which torsion angles are coherently coupled. Beyond $Q$ residues, the NERF error propagation decoheres the gradient signal.

The v7 solver exploits this by decomposing the chain into $Q$-length segments and folding them sequentially:

> **[Resultbox]** *v7 Segmented Cascade*
>
> 1. **Phase 1: SEGMENT** ($N \to C$ sequential). Divide the chain into segments of length $L = Q = 7$. Fold each segment in the full-chain context with upstream segments frozen. This mirrors *cotranslational folding* in biology and serial filter tuning in RF design.
> 2. **Phase 2: COUPLE**. Optimise only the junction angles (2 DOF per junction, $\varphi_j$ and $\psi_j$) using the full-chain loss function and gradient. This patches the inter-segment couplings.
> 3. **Phase 3: CONSTRAINED REFINE**. Polish the full chain, but clamp each angle to $\pm\text{BW}/2 = \pm 1/(2Q)$ radians from its Phase 2 value. This bandwidth constraint prevents NERF error propagation from corrupting the locally correct segment structures.

The segment length $L = Q = 7$ is *derived* from the backbone coherence length $Q = \lfloor d_0/a_0 \rceil$ (see `protein_bond_constants.py`). The bandwidth constraint $\pm 1/(2Q) \approx \pm 4.1^\circ$ is the half-bandwidth of the backbone resonator. No new constants are introduced.

## v7 Benchmark

v7 segmented cascade benchmark with complete circuit model. The cascade solver handles the richer loss landscape created by the additional coupling mechanisms, achieving sub-10 Å on Protein G for the first time. Loss = $|S_{11}|^2$, lower is better.

| Protein | $N$ | v4 RMSD (Å) | v7 RMSD (Å) | v7 Loss |
|---|---|---|---|---|
| Chignolin | 10 | 2.96 | 3.00 | 0.553 |
| Trp-cage | 20 | 6.14 | 6.20 | 0.823 |
| BBA5 | 21 | 6.23 | 6.19 | **0.025** |
| Villin HP35 | 36 | 6.80 | 8.52 | 0.327 |
| Protein G | 56 | 18.62 | **9.91** | 0.419 |

**Key observations.**

1. **Protein G sub-10 Å**: The cascade solver achieves 9.91 Å on Protein G, compared to 18.62 Å for v4 Adam with the complete circuit. The cascade handles the richer landscape by initialising each segment in the correct local context.
2. **BBA5 root convergence**: Loss $= 0.025 \approx 1/Q^2$, indicating a true impedance eigenstate has been found.
3. **Phase 3 constrained refinement**: The bandwidth constraint ($\pm 1/(2Q)$ radians) prevents NERF error propagation from corrupting locally correct structures. Without this constraint, Protein G's Phase 3 loss doubles (from 0.45 to 1.05).
4. **Sequential $N \to C$ cascade**: Chain loss decreases monotonically as segments are added (Protein G: $6.41 \to 6.08 \to 5.60 \to 4.58 \to 3.34 \to 3.02 \to 1.82 \to 0.88$), confirming that each segment benefits from the upstream structural context.

---
