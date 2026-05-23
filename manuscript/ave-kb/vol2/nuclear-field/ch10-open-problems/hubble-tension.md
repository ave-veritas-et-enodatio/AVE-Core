[↑ Ch. 10: Three Open Problems from Lattice Topology](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-mroghg]
-->

## The Hubble Tension

### The Problem

Two classes of measurements give discrepant values for $H_0$:

- **CMB (Planck):** $H_0 = 67.4 \pm 0.5$ km/s/Mpc
- **Local (SH0ES):** $H_0 = 73.04 \pm 1.0$ km/s/Mpc

The tension is $\Delta H_0 \approx 5.6$ km/s/Mpc ($>4\sigma$).

### AVE Resolution: $H_\infty$ as Geometric Consistency Identity

> **[Examplebox]** *The Asymptotic Hubble Geometric Consistency Identity*
>
> **Problem:** The Cosmology community is divided by the "Hubble Tension" where CMB measurements ($67.4$) drastically deviate from local Cepheid measurements ($73.0$). Evaluate where AVE's geometric closure of $G$ and the cosmological horizon lands in this band.
>
> **Solution:** AVE's geometric closure of $G$ in [Vol 3 Ch 1 §Fundamental Unity of Gravity and Expansion](../../../vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md) routes the Machian-impedance integration through $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$, with the cosmological horizon $R_H \equiv c/H_\infty$ substituted in. Rearranging the closure produces the algebraic identity:
>
> $$
> H_\infty = \frac{28\pi\,m_e^3\,c\,G}{\hbar^2\,\alpha^2}
> $$
>
> Evaluating this using CODATA $G$ + lattice-derived $\alpha$ yields:
>
> $$
> H_\infty \approx 69.32\;\text{km/s/Mpc}
> $$
>
> This is **not an independent first-principles prediction** of $H_\infty$; it is a geometric self-consistency identity rearrangement of $G$'s Machian-impedance derivation (the same algebraic relation written two ways). The numerical value follows by identity from CODATA $G$ + the geometric relation. The corpus-honest framing per [Vol 3 Ch 1 §Asymptotic Hubble Constant](../../../vol3/gravity/ch01-gravity-yield/asymptotic-hubble-constant.md): *"This equation does not 'predict' the Hubble constant from first principles alone; rather, it represents a consistency proof. It shows that Macroscopic Gravity ($G$) and the Cosmological Horizon ($H_\infty$) are not independent physical phenomena --- they are the same geometric limit evaluated from different topological reference frames."* That the consistency identity lands inside the Planck-SH0ES tension band (interior, within $1\sigma$ of TRGB) is the substantive empirical observation: the framework's geometric constraint between $G$ and $H_\infty$ is internally compatible with measured $H_0$. Promoting to an emergence-class prediction (Class D) requires a closed-form derivation of $G$ from substrate-local thermodynamics (lattice tension, equipartition, generation rate per node) that does not route through $R_H$; that Chain B' derivation is currently open per `closure-roadmap.md` (Tier 3 entry — Chain B' independent G derivation) and the Vol 3 Ch 5 open-work statement at [`cosmological-constant-closure.md`](../../../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md).
> >
> > **Refinement per `consistency-vs-emergence` v1.1 (Grant canonized 2026-05-19 EOD)**: more precisely, the relation is a **Class E operating-point projection** that includes Class C consistency-check sub-structure. Per [`omega-freeze-cosmic-grain-cascade.md:13-16`](../../../common/omega-freeze-cosmic-grain-cascade.md), $\{G, H_\infty, \hat{\Omega}_{\text{freeze}}, \alpha\}$ are joint-constrained at substrate operating point $u_0^* \approx 0.187$ via the $R_H/\ell_{\text{node}} \sim 10^{39}$ topological bridge. The framework's testable content is the joint constraint on these N observables — failure of any one falsifies the operating-point and therefore the entire substrate model — not four independent percent-error claims. Class C is true (CODATA $G$ → SI substitution recovers $H_\infty$); Class E is also true and stronger (the joint constraint defines the framework's actual falsifiability surface).

### Position Within the Tension

| **Measurement** | **$H_0$ (km/s/Mpc)** | **$\Delta$ from AVE** |
|---|---|---|
| Planck (CMB) | $67.4 \pm 0.5$ | AVE is $+2.9\%$ above |
| **AVE** $H_\infty$ | **69.32** | **consistency identity** |
| SH0ES (local) | $73.04 \pm 1.0$ | AVE is $-5.1\%$ below |
| Midpoint | 70.22 | AVE is $-1.3\%$ below |

The AVE geometric consistency identity sits in the *interior* of the tension band, 2.9% above Planck and 5.1% below SH0ES.

### Explanation of the Asymmetry

The tension arises from *asymmetric systematics* in the two measurement methods:

- **CMB (low):** The CMB path integral traverses predominantly low-density voids ($n_e \approx 0.01$ cm$^{-3}$). The impedance-weighted path average yields a slightly lower effective $c$ and hence a lower inferred $H_0$.
- **Local (high):** Cepheid and SN measurements probe nearby structure (galactic environments, $n_e \approx 0.05$ cm$^{-3}$). Higher local impedance yields higher effective $c$ and higher inferred $H_0$.

At CMB frequencies ($\nu \approx 160$ GHz), the raw plasma dispersion effect is $\sim\!10^{-12}$. However, the systematic arises not from dispersion but from the impedance-dependent calibration of the standard candle distance ladder.

---
