[↑ Ch.10 Attention Impedance](../index.md)
<!-- leaf: verbatim -->

# Extending the Impedance Framework to Attention

Chapters 5--8 established the $\Gamma$-driven pruning framework for the feed-forward (FFN) sublayer, treating each SwiGLU neuron as a two-port element with coupled impedance $Z_j = \|w_{\text{gate}}\| \times \|w_{\text{up}}\|$. The attention sublayer presents a fundamentally different topology: instead of $n_{ff}$ parallel neurons, it consists of $n_{\text{heads}}$ parallel *heads*, each a three-stage cascade of Query, Key, and Value projections.

## Per-Head Impedance

Each attention head $h$ transforms the input through three weight matrices: $W_Q^{(h)}$, $W_K^{(h)}$, and $W_V^{(h)}$. The coupled impedance of head $h$ is defined as the product of the three projection norms:

$$
Z_h = \|W_Q^{(h)}\|_F \times \|W_K^{(h)}\|_F \times \|W_V^{(h)}\|_F
$$

where $\|\cdot\|_F$ denotes the Frobenius norm (computed as the sum of squared row norms across the head's $d_{\text{head}}$ rows).

The output projection $W_O$ is excluded from the impedance calculation for the same reason the down-projection is excluded in the FFN: it serves as the output matching network coupling the head's output back to the residual bus. Including $W_O$ would require full dequantization of the quantized output weight matrix---an operation too expensive for load-time computation.
