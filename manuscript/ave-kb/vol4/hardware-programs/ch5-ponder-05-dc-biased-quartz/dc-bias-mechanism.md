[↑ Ch.5 PONDER-05 DC-Biased Quartz](index.md)
<!-- leaf: verbatim -->

## The Nonlinear Operating Regime

The universal saturation kernel $S$ (Axiom 4) governs *two* measurable quantities with opposite behaviours:

> **[Resultbox]** *Nonlinear Dielectric Saturation Regime*
>
> $$
> \varepsilon_{eff}(V) = \varepsilon_0 \cdot \underbrace{\sqrt{1 - \left(\frac{V}{V_{yield}}\right)^{\!2}}}_{S \;\to\; 0}
> \qquad\qquad
> C_{eff}(V) = \frac{C_0}{\underbrace{\sqrt{1 - \left(\frac{V}{V_{yield}}\right)^{\!2}}}_{S \;\to\; 0}} \;\to\; \infty
> $$

where $V_{yield} = \sqrt{\alpha} \cdot V_{snap} \approx 43.65\text{ kV}$. At $V_{DC} = 30\text{ kV}$:

$$
S\big|_{30\text{kV}} = \sqrt{1 - \left(\frac{30}{43.65}\right)^{\!2}} = \sqrt{1 - 0.4724} \approx 0.726
$$

The constitutive permittivity *drops* to $72.6\%$ of its zero-field value (the vacuum becomes a weaker dielectric), while the measured capacitance *rises* to $1/0.726 \approx 137.7\%$ (the node absorbs more displacement current under strain).

## DC Cross-Term Amplification

When a small AC signal $V_{ac}\sin(\omega t)$ rides on a large DC bias $V_{DC}$, the total squared field contains a cross term:

> **[Resultbox]** *DC Cross-Term Amplification*
>
> $$
> |E|^2 = (V_{DC} + V_{ac}\sin\omega t)^2 = V_{DC}^2 + 2V_{DC}V_{ac}\sin\omega t + V_{ac}^2\sin^2\omega t
> $$

The $2V_{DC}V_{ac}$ cross term provides **linear amplification** of the AC signal. For $V_{DC} = 30\text{ kV}$ and $V_{ac} = 500\text{ V}$:

$$
\text{Amplification} = \frac{2V_{DC}}{V_{ac}} = \frac{2 \times 30{,}000}{500} = 120\times
$$

This $120\times$ cross-term amplification transforms a barely detectable AC-only thrust into a $469\,\mu\text{N}$ signal---nearly $500\times$ above the $1\,\mu\text{N}$ torsion balance detection floor.

---
