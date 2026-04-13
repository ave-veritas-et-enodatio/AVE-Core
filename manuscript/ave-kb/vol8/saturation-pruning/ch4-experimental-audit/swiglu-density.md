[↑ Ch.4 Experimental Audit](../index.md)
<!-- leaf: verbatim -->

# SwiGLU Activation Density

Runtime activation telemetry on Llama 3.1 8B revealed that **97% of SwiGLU neurons fire** on any given prompt. The SiLU gate passes nearly all neurons into the linear regime ($S(r) \approx 1$). This establishes a fundamental boundary:

*Dense transformers at Q4_K quantization are near-unsaturated media.*

The 97% density measurement confirms that prompt-dependent activation culling is not viable for dense architectures. The SiLU nonlinearity provides soft gating but does not create sparse activations at the population level. The 3% that are below threshold contribute negligible compute.
