# Phase 3 — Reflection From Saturation: Op9 via Op2 + Op14 + Op3

**Status:** DRAFT. Derives the continuum self-avoidance mechanism for the Cosserat soliton by composing three scale-invariant universal operators pointwise on the field. Complements `11_` (Op10 screening); together they should deliver Ch 8's three geometric constraints.
**Prerequisites:** `00_`–`11_`; [`manuscript/vol_1_foundations/chapters/06_universal_operators.tex:334`](../../manuscript/vol_1_foundations/chapters/06_universal_operators.tex#L334) (scale-invariance declaration); [`src/ave/core/universal_operators.py:106-210`](../../src/ave/core/universal_operators.py#L106) (atomic-scale realization of the chain).
**Sequel:** extend `cosserat_field_3d.py` with a $\Gamma^2$ reflection term, rerun validator.

---

## §1  What `11_` established and what it didn't

`11_` promoted Op10 to continuum as the Faddeev-Skyrme 4-derivative wedge term, with coefficient fixed by the Gauss's-law / Z₀ = 1 magnetic-energy reading. Commit-and-test result at 64³:

- **Topology preserved at perturbed start** ($c = 3$).
- **Minor radius $r$ collapsed to ~1 lattice cell** from both initial conditions.
- **Ch 8's three dimensionless ratios failed** by large margins (screening ratio 4–11 vs target 0.25).

Energy-landscape diagnostic ([Session 2026-04-20, §"Describe the energy landscape"]) showed why:

- Total energy monotone downhill in $r$ on the accessible range; no local minimum in $r$ above the Nyquist floor.
- Op10's wedge density $W_4$ peaks near the Golden-Torus $r$ but its contribution is ~4% of total energy — a bump on a slope, not a wall.
- The lattice gradient operator averages sub-grid features, *killing* the Derrick stabilization that would resist collapse in the strict continuum.

**The missing physics: Ch 8's "self-avoidance constraint" $2(R - r) = d$.** This constraint is not encoded by Op10 (crossing-loss / screening). It is encoded by Op9 — **Steric Reflection ($\Gamma_{\text{steric}}$)**, AVE's reflection-coefficient operator applied at strand proximity ([`universal_operators.py:462`](../../src/ave/core/universal_operators.py#L462)).

Ch 8's three constraints map to three universal operators, not one:

| Ch 8 regime | Operator | Axiom |
|---|---|---|
| Nyquist ($d = 1\,\ell_{\text{node}}$) | Op2 (Saturation $S$) | Axiom 4 |
| Self-avoidance ($R - r = 1/2$) | Op9 (Γ_steric, reflection) | Axiom 3 |
| Screening ($R \cdot r = 1/4$) | Op10 (Y_loss, crossing drain) | Axioms 1+2 |

`11_` implemented the third. This document derives the second.

---

## §2  Scale invariance is load-bearing — we don't need a new operator

From [`06_universal_operators.tex:334`](../../manuscript/vol_1_foundations/chapters/06_universal_operators.tex#L334):

> *"Twenty-Two Universal Operators ($Z_0$, $S$, $\Gamma$, and nineteen derived operators) are applied identically across 14 orders of magnitude in length scale. Characteristic impedance, dielectric saturation, and reflection coefficient constitute the complete operator basis; all macroscopic phenomena decompose into these three primitives."*

And from [`universal_operators.py:5-6`](../../src/ave/core/universal_operators.py#L5):

> *"This module defines the ten fundamental, scale-invariant operators of the Applied Vacuum Engineering (AVE) framework."*

**Consequence:** there is no "Op9 continuum promotion" to derive. Op9 already is the composition of three scale-invariant primitives — Op2 (S), Op14 (Z_eff), Op3 (Γ) — applied pointwise to a local strain amplitude $A$. The atomic solver performs this composition discretely (pairwise over nodes). The Cosserat-field version performs it continuously (pointwise on the field). **Same operators, different lattice scale.**

The atomic-scale realization ([`universal_pairwise_energy`](../../src/ave/core/universal_operators.py#L106), lines 117-124) already exhibits the chain:

```
A(r)  = d_sat/r                     (strain amplitude)
Z(r)  = Z_0 / (1 - A²)^(1/4)        (Op14 from Op2)
Γ(r)  = (Z - Z_0)/(Z + Z_0)         (Op3)
U(r) ∝ Γ² × local flux              (reflection energy)
```

The Phase-3 task is to write down the same chain for the Cosserat strain amplitude $A(\mathbf{r})$, not for the atomic pairwise distance.

---

## §3  The chain, continuum form

### 3.1  Local strain amplitude $A(\mathbf{r})$

At each lattice node, the Cosserat field has two scalar strain invariants:

$$|\varepsilon|^2(\mathbf{r}) = \varepsilon_{ij}\,\varepsilon_{ij}, \qquad |\kappa|^2(\mathbf{r}) = \kappa_{ij}\,\kappa_{ij}$$

already computed in [`_energy_density_saturated`](../../src/ave/topological/cosserat_field_3d.py#L118). Axiom 4 sets the yield amplitudes $\varepsilon_{\text{yield}}$ and $\omega_{\text{yield}} = \pi/\ell_{\text{node}}$.

The natural scalar strain amplitude combining both:

$$A^2(\mathbf{r}) \;:=\; \frac{|\varepsilon|^2}{\varepsilon_{\text{yield}}^2} \;+\; \frac{|\kappa|^2}{\omega_{\text{yield}}^2}
\tag{3.1}$$

**Judgment call [JC-A] (reasonable default):** sum-of-squares combination as written, with equal weighting, analogous to how the atomic $A = d_{\text{sat}}/r$ collapses multi-body contributions into a single scalar. Alternative: separate $S_\varepsilon$ and $S_\kappa$ (as the current saturated energy already has them), giving two separate $\Gamma$ terms. Sum-of-squares is simpler and AVE-native per scale-invariance; separate treatment adds a second parameter. Recommendation: use (3.1).

### 3.2  Local saturation $S(\mathbf{r})$ — Op2

$$S(\mathbf{r}) \;:=\; \sqrt{1 - A^2(\mathbf{r})}
\tag{3.2}$$

This is Axiom 4 scalar saturation, identical to [`universal_saturation`](../../src/ave/core/universal_operators.py#L62). $S \in [0, 1]$: $S = 1$ is relaxed (vacuum), $S = 0$ is at yield. The current solver already computes $S_\varepsilon^2$ and $S_\kappa^2$ componentwise in the saturation kernel; the change here is to compose them into a single scalar $S$ and use it downstream.

### 3.3  Local impedance $Z_{\text{eff}}(\mathbf{r})$ — Op14

$$Z_{\text{eff}}(\mathbf{r}) \;:=\; \frac{Z_0}{S(\mathbf{r})^{1/4}}
\tag{3.3}$$

Op14 Dynamic Impedance ([universal_operators.py:715+]). In natural impedance units $Z_0 = 1$ (per `10_` chirality/scalar-Z resolution), this is simply $Z_{\text{eff}} = S^{-1/4}$. Diverges as $S \to 0$ — the Pauli-wall behavior of the atomic solver, now at every Cosserat-field site.

### 3.4  Local reflection $\Gamma(\mathbf{r})$ — Op3

Op3 reflection coefficient:

$$\Gamma \;=\; \frac{Z_2 - Z_1}{Z_2 + Z_1}$$

In the continuum limit of adjacent lattice nodes $\mathbf{r}_1$ and $\mathbf{r}_2 = \mathbf{r}_1 + \delta\mathbf{r}$:

$$\Gamma(\mathbf{r}) \;\approx\; \frac{Z_{\text{eff}}(\mathbf{r}) - Z_{\text{eff}}(\mathbf{r} - \delta\mathbf{r})}{Z_{\text{eff}}(\mathbf{r}) + Z_{\text{eff}}(\mathbf{r} - \delta\mathbf{r})} \;\xrightarrow{\delta \to 0}\; \frac{\delta\mathbf{r}}{2}\cdot\frac{\nabla Z_{\text{eff}}}{Z_{\text{eff}}} \;=\; \frac{\delta\mathbf{r}}{2}\cdot\nabla\ln Z_{\text{eff}}
\tag{3.4}$$

So the local reflection amplitude per unit separation is $\frac{1}{2}\nabla\ln Z_{\text{eff}}$. Equivalently, using $Z_{\text{eff}} = Z_0 S^{-1/4}$ and $\ln Z_{\text{eff}} = \ln Z_0 - \tfrac{1}{4}\ln S$:

$$\nabla\ln Z_{\text{eff}} \;=\; -\tfrac{1}{4}\,\nabla\ln S \;=\; -\frac{1}{4S}\,\nabla S
\tag{3.5}$$

Where $S \to 1$ (relaxed vacuum), $\nabla\ln S \to 0$ and $\Gamma \to 0$: no reflection in the vacuum, as expected. Where $S \to 0$ (at-yield region), the logarithmic derivative diverges — strong local reflection, which is the self-avoidance wall.

### 3.5  The reflection-energy penalty

Op3 applied at an impedance boundary produces a fractional power reflection $|\Gamma|^2$. In the atomic solver ([`universal_pairwise_energy`](../../src/ave/core/universal_operators.py#L152)):

$$U(r) \;=\; -\frac{K}{r}\,(T^2 - R^2) \;=\; -\frac{K}{r}\,(1 - 2\Gamma^2)$$

For the Cosserat field, the analog is a local energy *density* penalty proportional to $\Gamma^2$ times the local energy-flux density. The simplest (and scale-invariant) choice:

$$\mathcal{L}_{\text{reflection}}(\mathbf{r}) \;=\; k_{\text{refl}}\,\Gamma^2(\mathbf{r})\,|\boldsymbol{\nabla}\ln Z_{\text{eff}}|^2 \;\cdot\; (\text{local flux density})
$$

Combining (3.4)-(3.5), $\Gamma^2$ is itself already $\propto |\nabla\ln Z_{\text{eff}}|^2$ (times a length-squared), so the natural Lagrangian density is

$$\boxed{\;\;\mathcal{L}_{\text{reflection}}(\mathbf{r}) \;=\; k_{\text{refl}}\cdot\frac{|\nabla S|^2}{S^2}\;\;}
\tag{3.6}$$

(dropping the $-\tfrac{1}{4}$ factor into the coefficient $k_{\text{refl}}$).

This has exactly the right qualitative behavior:
- In the vacuum, $S \to 1$, $\nabla S \to 0$, $\mathcal{L}_{\text{reflection}} \to 0$. No penalty where there's no strain.
- Approaching yield, $S \to 0$, the $1/S^2$ factor diverges — strong repulsion from strand proximity.
- The $|\nabla S|^2$ factor localizes the penalty at impedance *gradients*, not just impedance spikes — exactly Op3's reflection-at-a-boundary structure, not Op2's scalar saturation.

### 3.6  Coefficient pinning: structural reading — $k_{\text{refl}} = 1$

Under the scale-invariance reading (§2), there is **no free parameter**: Γ's normalization is $(Z_2 - Z_1)/(Z_2 + Z_1)$, dimensionless, with no prefactor. Op14 and Op2 contribute $Z_0 = 1$ (scalar impedance per `10_`). The continuum chain $A \to S \to Z \to \Gamma$ carries through with no free coefficient.

**Structural commitment: $k_{\text{refl}} = 1$.** If the physics holds, the validator will produce Ch 8's geometry. If not, the specific deviation tells us which step in the chain picks up an additional factor (most likely the $Z_0 = 1$ vs $Z_0 = 377$ Ω dimensionful convention at some step).

This is the same commit-and-test discipline as `11_`'s JC-2 (path 2D): no calibration, one structural statement, then a falsification test.

---

## §4  Implementation spec

### 4.1  Changes to [`cosserat_field_3d.py`](../../src/ave/topological/cosserat_field_3d.py)

1. Compute $A^2(\mathbf{r})$ as a scalar field from $|\varepsilon|^2/\varepsilon_{\text{yield}}^2 + |\kappa|^2/\omega_{\text{yield}}^2$ (clipped to $[0, 1]$ to keep $S$ real).
2. Compute $S(\mathbf{r}) = \sqrt{1 - A^2(\mathbf{r})}$ as a scalar field.
3. Compute $\nabla S$ via the existing tetrahedral-gradient operator.
4. Compute the reflection density $|\nabla S|^2 / (S^2 + \varepsilon_{\text{reg}})$, with a small $\varepsilon_{\text{reg}}$ to regularize the $1/S^2$ at exact yield (JAX autograd safety; analogous to the sqrt-of-zero regularization applied to Rodrigues in `11_`).
5. Add this density to the total energy inside `_energy_density_saturated` and `_energy_density_bare`, with coefficient $k_{\text{refl}}$ (default 1.0).
6. Propagate `k_refl` through the jit compiled energy/grad functions.

### 4.2  Unit tests

- `test_reflection_density_zero_on_vacuum`: $\mathbf{u} = \boldsymbol{\omega} = 0$ everywhere → $A = 0$, $S = 1$, $\nabla S = 0$ → density = 0.
- `test_reflection_density_nonzero_on_2_3_ansatz`: (2,3) initial ansatz → $A > 0$ in the shell, $S < 1$ there, $\nabla S \ne 0$ at shell boundary → density > 0 somewhere.
- `test_reflection_density_diverges_near_yield`: construct a field with $A^2 \to 1$ at a site → density grows without bound (or is capped by $\varepsilon_{\text{reg}}$).
- `test_reflection_gradient_matches_finite_difference`: strict autograd-vs-FD test at a probe site, same style as the existing saturation test.

### 4.3  Validator

Same [`validate_cosserat_alpha_via_ch8_ratios.py`](../../src/scripts/vol_1_foundations/validate_cosserat_alpha_via_ch8_ratios.py) at $64^3$, dual-run protocol (exact Golden Torus init + perturbed $\pm 30\%$). Acceptance criteria unchanged from `09_` §5.

---

## §5  What we expect to see if the chain is complete

Qualitative prediction: with both Op10 (wedge screening) and the Op9-via-Op3 reflection term active, the energy landscape should now have:

- **A local minimum in $r$** (rather than a monotone slope to zero). The reflection wall activates as strands compress ($A \to 1$) and blocks further collapse.
- **A local minimum in $R$** (less critical — Op10 contributes to this via wedge density concentration on the shell).
- **Topology preserved** ($c = 3$) from both initial conditions.
- **Ch 8's three dimensionless ratios** emerging at the relaxation fixed point.

Quantitatively: $(R, r) \to (\varphi/2, (\varphi - 1)/2) \cdot $ scale, $(R-r)/d \to 1/2$, $R\,r/d^2 \to 1/4$, $\alpha^{-1} \to 4\pi^3 + \pi^2 + \pi$.

---

## §6  Failure modes and interpretations

- **No minimum in $r$ appears; still collapses.** The reflection term is too weak numerically, or Ω-yield/ε-yield pinning is off. Most likely candidate: the $S$ combination in (3.1) uses the wrong yield constants. Diagnose by inspecting local $A^2$ values during relaxation.
- **Minimum in $r$ appears, but at the wrong value.** The chain is structurally correct; relative strength between Op10 and Op9-via-Op3 is off. Re-examine the coefficient assumption $k_{\text{refl}} = 1$, or the combined-vs-separate $A^2$ judgment call (JC-A).
- **All three Ch 8 ratios hit.** Phase-3 success. The Ch 8 geometry emerges from the three scale-invariant operators composed on the Cosserat field.

Each failure mode falsifies a specific structural commitment and points at a specific doc/line to revise. Predictions-before-validation discipline (per `09_`).

---

## §7  Queue impact

No new queue items yet — this doc itself closes the "missing self-avoidance operator" gap identified at the end of `11_`'s commit-and-test. If the validation succeeds, the $\alpha^{-1} = 137.036$ derivation ab initio from AVE axioms is closed end-to-end, and this doc becomes a load-bearing reference.

If the validation fails, the specific failure mode will generate one new queue item at that time.

---

## §8  Status

Ready for implementation. One judgment call flagged (JC-A: combined vs separate $A^2$); recommendation to use combined per scale-invariance. No coefficient to adjudicate — $k_{\text{refl}} = 1$ by structural commitment.

Next steps:
1. Implement §4.1 in the solver.
2. Add §4.2 tests.
3. Run the validator per §4.3.
4. Report the energy-landscape diagnostic alongside the numerical result (per the 2026-04-20 convention).
