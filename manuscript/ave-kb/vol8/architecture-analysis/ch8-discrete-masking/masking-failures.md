[↑ Ch.8 Discrete Masking](../index.md)
<!-- leaf: verbatim -->

# Why Continuous Masking Fails

The continuous $S(r)$ mask attenuates the hidden activations *without* modifying the down-projection weight matrix $W_{\text{down}}$. Each surviving neuron $j$ contributes a ghost signal $S(r_j) \cdot h_j$ to the down-projection, where $0 < S(r_j) < 1$ for neurons near the buckling threshold.

Since $W_{\text{down}}$ was trained to receive the *full-amplitude* hidden state, the attenuated inputs create a distributed impedance mismatch across the residual bus. The per-layer reflection coefficient

$$
\Gamma = \frac{Z_{\text{pruned}} - Z_{\text{original}}}{Z_{\text{pruned}} + Z_{\text{original}}}
$$

measures this mismatch. In the top layers (L25--L31), $|\Gamma|^2 > 0.83$, meaning over 83% of the signal energy is reflected rather than transmitted. This catastrophic reflection accumulates through the 32-layer residual stack, shifting the logit distribution enough to redirect the model's reasoning path.

# Why Binary Masking Also Fails

The binary mask is equivalent to injecting *exact zeros* into 40% of the hidden channels. While this eliminates the ghost contributions, $W_{\text{down}}$ still has columns indexed to those channels. The matrix-vector product

$$
y = W_{\text{down}} \cdot h_{\text{masked}}
$$

now receives a vector with 40% of its entries identically zero. Since $W_{\text{down}} \in \mathbb{R}^{d \times n_{ff}}$ was not restructured, the computation is equivalent to dropping 40% of the down-projection's input features---an extreme perturbation that destabilizes the output distribution so severely that the model immediately emits the stop token.
