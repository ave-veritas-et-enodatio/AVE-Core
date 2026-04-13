[↑ Ch.9 Gamma Scaling](../index.md)
<!-- leaf: verbatim -->

# The 97% SwiGLU Density Constraint

The 97% activation density is no longer a purely empirical observation. Chapter 12 derives the sigmoid-saturation identity $\sigma(x)^2 + r^2 = 1$, which maps the SiLU gate directly to the AVE saturation operator. The 97% density reflects training convergence pushing neurons into Regimes I--II ($r \ll r_{II}$, $\sigma \approx 1$), with only 3% near the Regime II--III boundary ($\sigma \approx 0.5$, $r \approx 0.866$).

For architectures with intrinsic sparsity---Mixture of Experts models where only $K$ of $N_{\text{experts}}$ activate per token---the framework's predictions are fundamentally different. See Chapter 11.
