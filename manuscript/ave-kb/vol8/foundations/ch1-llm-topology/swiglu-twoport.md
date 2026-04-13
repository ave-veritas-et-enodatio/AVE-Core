[↑ Ch.1 LLM Topology](index.md)
<!-- leaf: verbatim -->

# Axiom 1: The SwiGLU Two-Port Node and Coupled Amplitude

Under Axiom 1, the vacuum is modeled as a cascaded LC network. In an LLM, the fundamental processing unit is the two-port SwiGLU neuron. A naive analysis might map the nonlinear activation (gate weight) as the sole amplitude contributor. However, the true signal power passing through the node requires computing the fully coupled system.

For a random unit-variance input vector $x$ of dimension $d$, the coupled root-mean-square (RMS) amplitude $A_j$ of neuron $j$ is derived from the product of the non-linear modulator ($w_{\text{gate}}$) and the linear carrier ($w_{\text{up}}$):

$$
A_j^2 = \left( \frac{\|w_{\text{gate}, j}\|^2}{d} \right) \times \left( \frac{\|w_{\text{up}, j}\|^2}{d} \right)
$$

Note that the down-projection ($w_{\text{down}}$) is correctly excluded from this local saturation term, as it serves purely as the output matching network coupling the node back to the residual bus.
