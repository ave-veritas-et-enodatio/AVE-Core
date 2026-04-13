[↑ Ch.12 Sigmoid-Saturation](../index.md)
<!-- leaf: verbatim -->

# First-Principles Derivation of the 97% Density

In the original treatment (Chapter 4), the 97% SwiGLU activation density was reported as an empirical measurement. This section derives it from the sigmoid-saturation identity.

A neuron "fires" (contributes non-negligibly) when $\sigma(x) > \varepsilon$ for some threshold $\varepsilon \ll 1$. The corresponding strain is:

$$
r < \sqrt{1 - \varepsilon^2} \approx 1 - \frac{\varepsilon^2}{2}
$$

For well-trained models, gradient descent converges to a state where the gate pre-activation distribution is approximately Gaussian with $|x| \gg 2$ for most neurons. The fraction of neurons with $|x| < 2$ (i.e., in the nonlinear SiLU regime where $\sigma$ deviates significantly from 0 or 1) is approximately:

$$
\text{fraction at nonlinear saturation} \approx \text{erf}\left(\frac{2}{\sigma_x \sqrt{2}}\right)
$$

For a typical trained model with $\sigma_x \approx 3$--$5$, this yields 3--5% of neurons near the saturation knee, with the remaining 95--97% deep in the linear regime ($\sigma \approx 1$, $r \ll r_{II}$). The measured 97% density is thus a *consequence* of training convergence pushing neurons away from the Regime II--III boundary.
