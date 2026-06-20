[↑ Ch. 10: Three Open Problems from Lattice Topology](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-4vwsjc]
-->

## The Baryon Asymmetry

> 🔴 **SUPERSEDED HEADLINE (Rule-12 walk-back, 2026-06-20).** The original Initial-release headline below — *"0.38% error, zero free parameters, every factor from lattice geometry"* — is **RETRACTED**. Per auditor **FINDING 2** (2026-06-10, recorded in [`research/2026-06-10_freeze-handedness-survey_note.md:50`](../../../../../research/2026-06-10_freeze-handedness-survey_note.md)), this result is **consistency-class with an imported electroweak-baryogenesis formula** (the substrate supplies the $\delta_{CP}$, $g_*$, $C_{sph}$ assignments; the $\alpha_W^4 C_{sph}/g_*$ scaffold is SM-imported), **not emergence-class — do not headline**. The governing claim **`clm-4vwsjc`** is pinned **confidence 0.4 / "do not build on, rework needed"** ([`vol2/claim-quality.md:483-486,491,496`](../../claim-quality.md)).
>
> **COMPOSITE CONSISTENCY-CHECK, not a zero-parameter derivation.** The formula is the standard electroweak-sphaleron baryogenesis scaffold ($C_{sph} = 28/79$ is the textbook SM Harvey-Turner conversion factor; $\alpha_W^4$ rides $\alpha$ [an AVE echo] and is the dominant magnitude-setter; $g_* = 7^3/4 = 85.75$ is asserted/reverse-validated, not independently measured; $\delta_{CP} = \pi/\kappa_{FS}$ is an asserted lattice-chirality fraction) with two AVE-flavored factor-identifications. **SYMMETRIC-STANDARD (what survives):** the **order-of-magnitude** result ($\eta \sim 6 \times 10^{-10}$) is peer-or-ahead of the SM, which cannot produce $\eta$ at all — CKM CP-violation undershoots by $\sim$8 orders, and the $m_H = 125$ GeV electroweak transition is a crossover (no out-of-equilibrium), so the SM needs BSM physics (leptogenesis) that *fits* $\eta$ with $\sim$10 unmeasured, renormalized heavy-neutrino parameters. AVE lands the right order of magnitude with $\sim$2 tuned factors and a shared $C_{sph}$. **The OOM-level consistency is the real, defensible result; the retracted part is the sub-percent precision and the "zero free parameters" parameter-count claim.**
>
> **Non-reproducible headline number (2026-06-20 re-investigation).** No code path yields the headline $6.08 \times 10^{-10}$ / $0.38\%$. The canonical engine (`lattice_chirality()` in [`src/ave/axioms/open_problems.py`](../../../../../src/ave/axioms/open_problems.py), using the **thermal** $\kappa_{FS} = 24.95$) gives $\eta = 6.05 \times 10^{-10}$ (**0.79%**); the leaf's own literals $0.126 \times 0.0328^4 \times 0.354 / 85.75$ give $6.02 \times 10^{-10}$ (1.30%); the cold-$8\pi$ algebra ($\delta_{CP} = \pi/8\pi = 1/8$) gives $6.01 \times 10^{-10}$ (1.51%). The displayed number has been corrected to the **engine-canonical 6.05×10⁻¹⁰ / 0.79%** below.
>
> **$\kappa_{FS}$ cold-vs-thermal inconsistency (flagged, not silently resolved).** The body displays the **cold** form $\delta_{CP} = \pi/8\pi = 1/8 = 0.125$ ([`constants.py:727`](../../../../../src/ave/core/constants.py) `KAPPA_FS_COLD = 8\pi`), but the engine uses the **thermal** $\kappa_{FS} = 24.95$ ([`constants.py:791`](../../../../../src/ave/core/constants.py)) giving $\delta_{CP} = 0.126$. The engine (thermal) is the live, CI-gated code path and is treated as canonical here. Whether cold or thermal $\kappa_{FS}$ is the *physically correct* divisor for the baryogenesis δ_CP is a substrate-physics call left OPEN for Grant adjudication (flag-don't-fix); it does not affect the order-of-magnitude conclusion (both give $\eta \sim 6 \times 10^{-10}$).
>
> *Body below preserved verbatim per Rule 12; only the displayed result number and the headline framing line are corrected in place (marked).*

### The Problem

The universe contains $\sim\!6 \times 10^{-10}$ baryons per photon, but essentially zero antibaryons. The Sakharov conditions require:

1. Baryon number violation
2. C and CP violation
3. Departure from thermal equilibrium

Standard Model CP violation is insufficient by several orders of magnitude.

### AVE Resolution: Lattice Chirality

The AVE lattice (SRS/K4 crystal) has **definite chirality** --- it is not superimposable on its mirror image.

1. **C violation:** The lattice itself breaks charge conjugation because the SRS structure has a definite handedness (left or right).
2. **CP violation:** The $(2,q)$ torus knots are chiral --- a trefoil is not equivalent to its mirror image. Combined with the lattice chirality, this produces CP violation at the fundamental level.
3. **Equilibrium departure:** The electroweak phase transition provides the necessary out-of-equilibrium conditions, as in the standard picture.

### Quantitative Derivation

The CP-violating phase from lattice chirality is:

$$
\delta_{CP} = \frac{\pi}{\kappa_{FS}} \approx 0.126
$$

This is the fraction of the torus knot phase winding that is asymmetric under mirror reflection.

The baryon-to-photon ratio follows from electroweak baryogenesis:

> **[Resultbox]** *Baryon-to-Photon Ratio*
>
> $$
> \eta = \frac{\delta_{CP} \,\cdot\, \alpha_W^4 \,\cdot\, C_{sph}}{g_*}
> $$

The factors entering the formula (see the SUPERSEDED-HEADLINE note above for which are AVE-derived vs SM-imported vs asserted):

1. $\alpha_W = \alpha/\sin^2\theta_W \approx 0.0328$ (weak coupling; rides $\alpha$, an AVE echo; dominant magnitude-setter).
2. $C_{sph} = (8N_f + 4N_H)/(22N_f + 13N_H) = 28/79$ — the **textbook SM Harvey-Turner sphaleron conversion factor**, with asserted $N_f = 3$ (torus knot generations $c=3,5,7$ below $T_{EW}$) and $N_H = 1$ (SRS lattice Goldstone mode).
3. $g_* = 7^3/4 = 85.75$, identified from $\nu_{vac} = 2/7$ — **asserted/reverse-validated against $\eta_{obs}$, not independently measured.**

Evaluating (engine-canonical, thermal $\kappa_{FS} = 24.95 \Rightarrow \delta_{CP} = 0.126$):

$$
\eta \approx \frac{0.126 \times (0.0328)^4 \times 0.354}{85.75} \approx 6.05 \times 10^{-10}
$$

The observed value is $\eta_{obs} = 6.1 \times 10^{-10}$.

**Result: order-of-magnitude consistency-check, $\eta \approx 6.05 \times 10^{-10}$ (0.79% — engine-canonical thermal $\kappa_{FS}$; the displayed cold-$8\pi$ algebra gives $6.01 \times 10^{-10}$ / 1.51%).** [Original Initial-release line read "*Result: 0.38% error. Zero free parameters. Every factor from lattice geometry.*" — RETRACTED, see SUPERSEDED-HEADLINE note above: the 6.08×10⁻¹⁰ / 0.38% figure is non-reproducible by any code path, and the "zero free parameters" claim is walked back per FINDING 2.]

Note: the Standard Model uses $g_* = 106.75$ (yielding 20% error). The AVE derivation $g_* = 7^3/4$ from the lattice Poisson ratio eliminates this discrepancy.

---
