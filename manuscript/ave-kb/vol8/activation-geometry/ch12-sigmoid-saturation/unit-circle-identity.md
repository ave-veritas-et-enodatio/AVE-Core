[↑ Ch.12 Sigmoid-Saturation](../index.md)
<!-- leaf: verbatim -->

# The Unit Circle Identity

The AVE saturation operator $S(r) = \sqrt{1 - r^2}$ maps the normalized strain $r \in [0,1]$ to the fraction of signal transmitted through the medium. In the virtual medium, the SiLU nonlinearity $\text{SiLU}(x) = x \cdot \sigma(x)$ gates the hidden activations, where $\sigma(x) = 1/(1 + e^{-x})$ is the logistic sigmoid.

The gating fraction of signal passed by a SiLU neuron is:

$$
\text{gate fraction} = \frac{\text{SiLU}(x)}{x} = \sigma(x)
$$

The exact relationship between $\sigma(x)$ and $S(r)$ is derived by setting:

$$
\sigma(x) = S(r) = \sqrt{1 - r^2}
$$

Solving for $r$:

$$
r^2 = 1 - \sigma(x)^2
$$

This yields the fundamental identity:

$$
\boxed{\sigma(x)^2 + r^2 = 1}
$$

The sigmoid gate fraction and the AVE strain ratio lie on the **unit circle**. This is not an approximation---it is the *definition* of the correct mapping between the virtual activation field and the AVE strain variable.
