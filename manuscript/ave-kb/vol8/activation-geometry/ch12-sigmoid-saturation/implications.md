[↑ Ch.12 Sigmoid-Saturation](../index.md)
<!-- leaf: verbatim -->

# Implications

1. The SiLU gate is the **AVE saturation operator** of the virtual medium, expressed in activation space rather than strain space. These are related by $\sigma(x)^2 + r^2 = 1$.
2. Training acts as the "cooling" process that drives neurons into Regime I (linear passband). An untrained (random-weight) model would have Gaussian pre-activations centered at $x = 0$ ($r = r_{II}$), with half its neurons in Regime III.
3. The 97% activation density is not an empirical accident: it is the thermodynamic equilibrium of gradient descent, analogous to a physical medium cooling below its critical temperature.
4. Axiom 2 ($\xi_{\text{topo}}$): the mapping $\sigma^2 + r^2 = 1$ is topologically equivalent to the parametric unit circle. The sigmoid wraps the real line onto the interval $[0,1]$ with the same topology as $S(r)$ wrapping $[0,1]$ onto $[0,1]$.
