[↑ Ch.3 Universal Operator Mapping](../index.md)
<!-- leaf: verbatim -->

# Impedance Definition for the FFN Two-Port

In the classic LLM SwiGLU architecture, the node operates as a two-port network coupling a non-linear gate parameter and a linear output projection. The generalized impedance for this virtual component is defined by the product of the port norms:

$$
Z_j = \frac{\|w_{\text{gate}, j}\|^2}{d} \times \frac{\|w_{\text{up}, j}\|^2}{d}
$$

The down-projection ($w_{\text{down}}$) is correctly excluded from this impedance calculation, as it serves purely as the output matching network coupling the node back to the residual bus.
