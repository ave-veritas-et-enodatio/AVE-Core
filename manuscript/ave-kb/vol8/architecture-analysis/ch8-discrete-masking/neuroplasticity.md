[↑ Ch.8 Discrete Masking](../index.md)
<!-- leaf: verbatim -->

# The Neuroplasticity Boundary

The preceding analysis established that structural excision is the only valid pruning mechanism for a software manifold. A more fundamental question remains: *what determines which neurons to excise?*

Early work in this volume applied the dynamic regime boundaries of the AVE saturation operator---$r_I = \sqrt{2\alpha}$, $r_{II} = \sqrt{3}/2$, $r_{III} = 1.0$---as thresholds on the *static weight norms* of frozen model parameters. This produced systematic semantic collapse across every model tested (3B, 4B, 8B, 9B parameters).

## The Category Error

The dynamic regime boundaries describe the behavior of a medium *under active load*:

- A biological synapse under inference exhibits **neuroplasticity**---the medium physically reshapes in response to the propagating signal. The $S(r)$ saturation operator accurately models this process, and the yield limit $r_{III} = 1.0$ corresponds to excitotoxic breakdown.
- An LLM during training exhibits analogous dynamics: gradient descent applies iterative stress to the weight manifold, and the equilibrium distribution is the result of this dynamic process.
- An LLM during **inference** has **zero neuroplasticity**. The weights are frozen constants. No node strains, yields, or approaches breakdown.

Applying dynamic yielding thresholds to static impedance values is a category error. The weights during inference are the *impedance* of a passive transmission line---not the amplitude of a wave propagating through it.

## The Correct Mapping

| **AVE Concept** | **Physical Medium** | **LLM Inference** |
|---|---|---|
| Impedance $Z$ | $\sqrt{L/C}$ per section | $\|w_j\|$ per neuron (static) |
| Amplitude $A$ | Field strength (dynamic) | Activation $x$ (dynamic) |
| Saturation $S(r)$ | Medium response | SiLU gate on activations |

The $S(r)$ operator correctly describes what the SiLU gate does to *activations* during the forward pass---it is the saturation mechanism of the virtual medium. But $S(r)$ does not act on frozen weights. The frozen weight distribution is a **fossil record** of past training stress, not a living system under load.

## The Static Filter Framework

Since the weights are static impedance, pruning is a filter design problem. Each transformer layer is a two-port ABCD cascade section with transfer matrix:

$$
\begin{bmatrix} A & B \\ C & D \end{bmatrix}_{total} = \prod_{i=1}^{N} \begin{bmatrix} A & B \\ C & D \end{bmatrix}_i
$$

The pruning question becomes: *which sections of the static transmission line contribute negligibly to the transfer function?*

Neurons with low coupled impedance ($\|w_{\text{gate}}\| \times \|w_{\text{up}}\|$ relative to the per-layer mean) contribute negligible signal transformation. The per-layer mean serves as $A_c$ (the local characteristic impedance), and neurons below a fraction of this mean can be structurally excised.

Experimental validation on Llama 3.1 8B with the per-layer ABCD framework produced the first correct semantic output from a pruned model: the baked network correctly answered "What is 2+2?" with "4" while achieving $+43\%$ throughput and maintaining $|\Gamma|^2 < 0.01$ across all layers.

## Conclusion

The Z--A inversion (Chapter 2) dictates that the *only* valid structural modification in the software medium is **dimensional excision**: simultaneous removal of rows and columns. Channel-wise masking---whether continuous or binary---violates Axiom 3 (least reflected action) by creating an impedance discontinuity between the hidden state and the down-projection.

$$
\boxed{\text{Software manifold} \implies \text{excision (reshape)} \neq \text{attenuation (mask)}}
$$

Furthermore, the pruning *threshold* must be determined by the static transmission line properties of the frozen weight manifold (per-layer ABCD cascade impedance contribution), **not** by the dynamic regime boundaries of the $S(r)$ saturation operator. The dynamic regime boundaries apply to the activation field at runtime (via the SiLU gate), not to the static weight structure.

$$
\boxed{\text{Frozen weights (no neuroplasticity)} \implies \text{static filter design} \neq \text{dynamic yielding physics}}
$$

This result validates that the static baking pipeline with per-layer ABCD cascade analysis is the axiomatically correct implementation for the virtual medium.
