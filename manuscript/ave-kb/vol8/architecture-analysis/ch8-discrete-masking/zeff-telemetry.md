[↑ Ch.8 Discrete Masking](../index.md)
<!-- leaf: verbatim -->

# Axiom 1: Effective Impedance Telemetry ($Z_{eff}$)

In the AVE Framework (Axiom 1), a physical medium transmits signal action governed by its characteristic impedance $Z_0$. As the spatial saturation $S(r)$ approaches zero, the effective impedance of the local medium approaches infinity:

$$
Z_{\text{eff}} = \frac{Z_0}{\sqrt{S(r)}}
$$

where $Z_0 \approx 376.73\,\Omega$ is the vacuum impedance of the unstrained medium.

During the runtime mask test (Pass B), direct $Z_{\text{eff}}$ telemetry was implemented per neuron. As local structures approached the thermodynamic yield limit ($r^2 \to 1.0$), the peak impedance of surviving neurons in the overloaded layers (L25--L31) was measured at $\approx 3600\,\Omega$---nearly $10\times$ the baseline impedance. This extreme resistance physically acts as an open circuit, providing the mechanical explanation for the drop in signal transmission.
