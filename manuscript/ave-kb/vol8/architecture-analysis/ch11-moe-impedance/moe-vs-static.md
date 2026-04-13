[↑ Ch.11 MoE Impedance](../index.md)
<!-- leaf: verbatim -->

# Static vs Dynamic Impedance Media

This distinction maps directly to the physical classification of media:

- **Dense transformers** are analogous to a *rigid waveguide*: every section conducts, impedance is fixed, and the only degree of freedom is structural excision of low-impedance sections. The $\Gamma$-driven pruning framework (Chapters 5--8) operates in this regime.
- **MoE architectures** are analogous to a *switched transmission line*: the router dynamically connects and disconnects branches per token, implementing real-time impedance matching. The 91% of compute that is "pruned" is not wasted---it is the router correctly rejecting high-$\Gamma$ paths.
