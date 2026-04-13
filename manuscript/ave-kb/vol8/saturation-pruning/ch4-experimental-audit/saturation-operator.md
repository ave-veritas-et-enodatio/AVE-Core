[↑ Ch.4 Experimental Audit](../index.md)
<!-- leaf: verbatim -->

# Implementation of the Saturation Operator

Axiomatic pruning is strictly parameter-free. For a multi-layer perceptron lattice, the operator demands an emergent boundary derived naturally from the network's own structural strain. The coupled impedance of each SwiGLU neuron $j$ in layer $\ell$ is:

$$
Z_j = \|w_{\text{gate}, j}\|^2 \times \|w_{\text{up}, j}\|^2
$$

The per-layer characteristic impedance is the mean:

$$
A_c^2(\ell) = \frac{1}{N_\ell} \sum_{j=1}^{N_\ell} Z_j
$$

Neurons are sorted by ascending $Z_j$ and pruned from weakest until the cumulative per-layer reflection coefficient $|\Gamma|^2$ reaches the $\gamma$ ceiling.
