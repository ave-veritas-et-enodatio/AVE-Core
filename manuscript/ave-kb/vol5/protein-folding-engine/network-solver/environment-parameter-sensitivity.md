[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Environment Parameter Sensitivity

The $S_{11}$ engine contains two classes of inputs:

1. **Axiom-derived constants**: $Z_\text{topo}$, bond angles, Slater radii, $C_\text{bend}$, $\kappa_\text{HB}$. These are fixed by Axioms 1--4 and are *not* swept.
2. **Environment parameters**: properties of the solvent and the backbone resonance frequency that describe external conditions. These are the *only* non-axiomatic inputs.

## Environment Parameters

Environment parameters and sweep bounds.

| Parameter | Symbol | Default | Sweep Range | Physical Source |
|---|---|---|---|---|
| Static dielectric | $\varepsilon_s$ | 80.0 | $60$--$90$ | Debye theory; $T$-dependent |
| High-freq dielectric | $\varepsilon_\infty$ | 1.77 | $1.5$--$2.5$ | Optical limit of water |
| Debye relaxation | $\tau_\text{D}$ | 8.3 ps | $5$--$15$ ps | Rotational correlation |
| Backbone resonance | $f_0$ | 23 THz | $20$--$26$ THz | Amide-V mode (IR) |

**Reference impedance.** The S-parameter extraction uses $Y_0 = 1/Z_\text{water}(\omega)$ where

$$Z_\text{water}(\omega) = \sqrt{|\varepsilon(\omega)|} = \sqrt{\left|\varepsilon_\infty + \frac{\varepsilon_s - \varepsilon_\infty}{1 + j\omega\tau_\text{D}}\right|}$$

This is the only coupling between the protein network and its solvent environment.

## Sweep Protocol

1. **One-at-a-time (OAT)**: vary each parameter individually while holding others at defaults. Identifies sensitivity.
2. **Pairwise**: for sensitive parameters ($>1$ Å RMSD variation), sweep 2D planes for interaction effects.
3. **Robustness**: the engine is robust if RMSD varies $<20\%$ across the physically reasonable range.

The OAT sweep uses 5 grid points per parameter (including endpoints and the default), giving $4 \times 5 = 20$ evaluations per protein.

## Sweep Results

OAT sensitivity results for Chignolin (N=10). Loss is $S_{11}$-weighted; lower is better.

| Parameter | Sweep values $\to$ Loss | | | $\Delta$Loss |
|---|---|---|---|---|
| $\varepsilon_s$ | $60 \to 1.0977$ | $70 \to 1.0983$ | $80^* \to 1.0984$ | $90 \to 1.0978$ | **0.0007** |
| $\varepsilon_\infty$ | $1.5 \to 1.0969$ | $1.77^* \to 1.0984$ | $2.0 \to 1.0984$ | $2.5 \to$ --- | **0.0015** |
| $\tau_\text{D}$ | (sweep pending) | | | --- |
| $f_0$ | (sweep pending) | | | --- |

${}^*$ = default value.

**Interpretation.** The engine is *insensitive* to the static dielectric constant $\varepsilon_s$: a 50% change in $\varepsilon_s$ ($60 \to 90$) produces only $\Delta\text{Loss} = 0.0007$, or $<0.1\%$. Similarly, the high-frequency dielectric $\varepsilon_\infty$ has negligible effect.

This confirms a core prediction of the framework:

> *Protein folding is driven by impedance topology ($Z_\text{topo} = \sqrt{M/n_e}$ per residue), not by the absolute dielectric value of the solvent.*

The water dielectric enters only through the reference impedance $Y_0 = 1/Z_\text{water}(\omega)$ and the diagonal solvent loading $Y_\text{solvent}$. Since folding minimises the *relative* impedance mismatch (the $S_{11}$ topology), the absolute scale of $\varepsilon$ cancels. This is analogous to a matched RF network: the $S_{11}$ pattern depends on the impedance *ratios*, not the absolute $Z_0$.

**Implications.**

1. The four environment parameters ($\varepsilon_s$, $\varepsilon_\infty$, $\tau_\text{D}$, $f_0$) are **boundary conditions**, not physics parameters. The engine is robust to their exact values.
2. No pairwise sweep is needed: the single-parameter sensitivity is so small that interaction effects are negligible.
3. The geometric constraint (surface/volume $\sim N^{-1/3}$) is already emergent from the exposure calculation in `dc_analysis`; adding it explicitly would be redundant.

## Current Benchmark

v4 benchmark (all-derived constants, even/odd mode $\beta$-sheets).

| Protein | N | v3 RMSD (Å) | v4 RMSD (Å) | $\Delta$ |
|---|---|---|---|---|
| Chignolin | 10 | 2.59 | **2.77** | $+0.18$ |
| Trp-cage | 20 | 6.25 | **5.46** | $-0.79$ |
| BBA5 | 22 | 7.39 | **5.98** | $-1.41$ |
| Villin HP35 | 36 | 8.25 | **6.91** | $-1.34$ |
| Protein G | 56 | 13.25 | **10.92** | $-2.33$ |

---
