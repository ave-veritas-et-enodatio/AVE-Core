[↑ Ch. 10: Three Open Problems from Lattice Topology](./index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: mroghg -->

## The Hubble Tension

### The Problem

Two classes of measurements give discrepant values for $H_0$:

- **CMB (Planck):** $H_0 = 67.4 \pm 0.5$ km/s/Mpc
- **Local (SH0ES):** $H_0 = 73.04 \pm 1.0$ km/s/Mpc

The tension is $\Delta H_0 \approx 5.6$ km/s/Mpc ($>4\sigma$).

### AVE Resolution: $H_\infty$ Is the Prediction

> **[Examplebox]** *Deriving the Asymptotic Hubble Rate*
>
> **Problem:** The Cosmology community is divided by the "Hubble Tension" where CMB measurements ($67.4$) drastically deviate from local Cepheid measurements ($73.0$). Evaluate the theoretical midpoint using AVE.
>
> **Solution:** AVE predicts $H_0$ from pure lattice first principles without referencing redshift catalogs. At Layer 7 of the derivation chain (Volume 1, Appendix B), the asymptotic expansion rate for a lattice-genesis model balances node generation against the holographic thermal capacity. The resulting algebraic limit is:
>
> $$
> H_\infty = \frac{28\pi\,m_e^3\,c\,G}{\hbar^2\,\alpha^2}
> $$
>
> Evaluating this using the fundamental calibration constants yields:
>
> $$
> H_\infty \approx 69.32\;\text{km/s/Mpc}
> $$
>
> This is **not a fit**; every factor is rigorously derived from lattice structure and bounding limits. The prediction sits flawlessly inside the tension band interior, $2.9\%$ above the Planck CMB analysis and $5.1\%$ below the SH0ES local structure calculations, formally explaining the asymmetric systematics causing the data divide.

### Position Within the Tension

| **Measurement** | **$H_0$ (km/s/Mpc)** | **$\Delta$ from AVE** |
|---|---|---|
| Planck (CMB) | $67.4 \pm 0.5$ | AVE is $+2.9\%$ above |
| **AVE** | **69.32** | **prediction** |
| SH0ES (local) | $73.04 \pm 1.0$ | AVE is $-5.1\%$ below |
| Midpoint | 70.22 | AVE is $-1.3\%$ below |

The AVE prediction sits in the *interior* of the tension band, 2.9% above Planck and 5.1% below SH0ES.

### Explanation of the Asymmetry

The tension arises from *asymmetric systematics* in the two measurement methods:

- **CMB (low):** The CMB path integral traverses predominantly low-density voids ($n_e \approx 0.01$ cm$^{-3}$). The impedance-weighted path average yields a slightly lower effective $c$ and hence a lower inferred $H_0$.
- **Local (high):** Cepheid and SN measurements probe nearby structure (galactic environments, $n_e \approx 0.05$ cm$^{-3}$). Higher local impedance yields higher effective $c$ and higher inferred $H_0$.

At CMB frequencies ($\nu \approx 160$ GHz), the raw plasma dispersion effect is $\sim\!10^{-12}$. However, the systematic arises not from dispersion but from the impedance-dependent calibration of the standard candle distance ladder.

---
