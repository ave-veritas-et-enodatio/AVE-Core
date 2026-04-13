[↑ Ch.12 Sigmoid-Saturation](../index.md)
<!-- leaf: verbatim -->

# The Zero-Bias Prediction

The Regime II $\to$ III boundary $r_{II} = \sqrt{3}/2$ maps *exactly* to $x = 0$: the zero pre-activation. This is a parameter-free prediction of the AVE framework:

$$
\boxed{r_{II} = \frac{\sqrt{3}}{2} \iff x = 0 \iff \sigma = \frac{1}{2}}
$$

A neuron with zero gate pre-activation ($w_{\text{gate}} \cdot x = 0$) sits precisely at the Regime II--III boundary. This is the onset of structural load-bearing: the SiLU gate passes exactly 50% of the signal, and the neuron transitions from linear processing to nonlinear saturation.
