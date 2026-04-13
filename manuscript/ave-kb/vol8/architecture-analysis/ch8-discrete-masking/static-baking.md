[↑ Ch.8 Discrete Masking](../index.md)
<!-- leaf: verbatim -->

# Why Static Baking Succeeds

Static baking (Chapter 5) removes the corresponding *rows* from $W_{\text{gate}}$ and $W_{\text{up}}$, and the corresponding *columns* from $W_{\text{down}}$, simultaneously. The result is a structurally coherent smaller matrix:

$$
y = W_{\text{down}}' \cdot h' \quad \text{where } W_{\text{down}}' \in \mathbb{R}^{d \times n_{ff}'},\ n_{ff}' < n_{ff}
$$

This preserves the impedance ratio $Z_{\text{out}}/Z_{\text{in}}$ because both numerator and denominator are scaled by the same topological pruning, yielding $\Gamma \approx 0$.
