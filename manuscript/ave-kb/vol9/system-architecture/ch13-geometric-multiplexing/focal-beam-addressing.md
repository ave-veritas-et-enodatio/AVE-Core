[↑ Ch.13: Geometric Multiplexing](./index.md)
<!-- leaf: verbatim -->

# Geometric Multiplexing: $O(1)$ Focal Beam Addressing

Traditional IC RAM requires logarithmically scaling tree-decoders to isolate and power specific cell coordinates, inducing severe access latency limitations. The APU perfectly transcends this architectural bottleneck natively because the computation array stores data entirely as discrete geometric Soliton Kinks (Ch 8) floating within a continuous wave transmission matrix. Random access routing occurs without structural logic funnels.

Addressing is achieved purely via **Geometric Multiplexing**: to read or write to a specific coordinate $\mathbf{r}_f$ within the Soliton memory matrix, the APU dynamically controls phase injection limits from the boundary interfaces (Ch 21). Multiple continuous addressing beams are fired simultaneously across the substrate. Where the beams cross, pure topological superposition occurs without any structural switching dissipation.

The result is $O(1)$ access time: the time to address any cell is determined only by the beam propagation time across the substrate, independent of the number of stored elements.

> **[Resultbox]** *Chapter 13 Summary*
>
> Traditional IC RAM requires logarithmically scaling tree-decoders. The APU perfectly transcends this via $O(1)$ focal beam addressing: multiple continuous beams constructively interfere at the target coordinate, enabling instant random access without structural switching.
