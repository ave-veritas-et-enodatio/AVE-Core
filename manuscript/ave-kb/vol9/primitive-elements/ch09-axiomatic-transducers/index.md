[↑ Primitive Elements](../index.md)

# Ch.9: Axiomatic Transducers ($50\,\Omega \to 376.73\,\Omega$)

The Axiomatic Transducer addresses the $7.53\times$ impedance mismatch between the $50\,\Omega$ RF external domain and the $376.73\,\Omega$ VCA vacuum, which without intervention reflects 58.7% of incident power. The Klopfenstein taper profile is the unique equi-ripple optimum, reducing reflections to $< 0.01\%$.

## Key Results

| Result | Statement |
|---|---|
| Step Reflection | $\Gamma_{step} = (376.73 - 50)/(376.73 + 50) = +0.766$; $|\Gamma|^2 = 58.7\%$ reflected |
| Transmission Without Taper | $T = 1 - |\Gamma_{step}|^2 = 41.3\%$ — unacceptable for hardware |
| Klopfenstein Taper Length | $L \approx 70\,\mu\text{m}$ at $f_{CC} = 1.832\,\text{THz}$ in SOI ($\kappa_{topo} = 3.9$) |
| Passband Reflectance | $< 0.01\%$ ($< -40\,\text{dB}$) across all frequencies above $f_{CC}$ |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Impedance Matching Proof](./impedance-matching-proof.md) | Step reflection calculation, Klopfenstein profile derivation, taper length design |
| [Transducer JAX Validation](./transducer-jax-validation.md) | Simulation of taper reflectance across passband |
