[↑ Ch.11 MoE Impedance](../index.md)
<!-- leaf: verbatim -->

# The Testable Prediction

The AVE framework makes a specific, falsifiable prediction for MoE architectures:

$$
\boxed{\text{Expert static impedance ranking} \approx \text{Router frequency ranking}}
$$

Experts with low coupled impedance $Z_e = \|W_{\text{gate},e}\| \times \|W_{\text{up},e}\|$ should be routed less frequently. The static $\Gamma$-derived impedance mask should correlate with the empirical routing frequency distribution.

If confirmed, this would enable **pre-culling**: permanently removing experts that are never (or rarely) routed, reducing both the model's VRAM footprint and the router's candidate pool.

## Hardware Limitations

This prediction remains experimentally unverified. The two available MoE models---Qwen3.5-35B-A3B (21 GB weights) and GLM-4.7B-Flash (17 GB weights)---both exceed the 19 GB GPU working set of the Apple M4 Pro used for all experiments in this volume.

MoE models are inherently VRAM-intensive: they store all $N_{\text{expert}}$ expert weight matrices even though only $K$ activate per token. The Qwen3.5-35B-A3B model has 35B total parameters but only 3B active parameters per token---a 91% sparsity ratio built into the architecture.

## Conclusion

Dense transformers operate with static impedance (97% SwiGLU density, Chapter 9). The $\Gamma$-driven framework achieves $+6.4\%$ throughput through structural excision of the weak tail.

MoE architectures operate with dynamic impedance (91% expert sparsity). The router implements Axiom 3 in real time. The AVE prediction---that static impedance ranking correlates with routing frequency---awaits verification on hardware with sufficient VRAM.

$$
\boxed{\text{Dense} \implies \text{static } \Gamma\text{-pruning}; \quad \text{MoE} \implies \text{dynamic } \Gamma\text{-routing}}
$$

