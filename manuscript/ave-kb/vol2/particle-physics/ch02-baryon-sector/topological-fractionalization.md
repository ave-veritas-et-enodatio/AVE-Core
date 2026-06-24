[↑ Ch.2 — Baryon Sector](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-mnb3lt, clm-67jn9o, clm-w8jn3q]
-->

## Topological Fractionalization: The Origin of Quarks
<!-- claim-quality: clm-67jn9o -->

<!-- claim-quality: clm-mnb3lt (proton total charge $Q_{total}=+1e$ derives from the Borromean structure that fixes the proton-mass eigenvalue) -->
In the AVE framework, charge is defined as an integer topological winding number ($N \in \mathbb{Z}$). True fractional twists are mechanically forbidden, as they would sever the continuous manifold. The fractional quark charge paradox is resolved via the mathematics of **Topological Fractionalization** on a frustrated discrete graph. The proton possesses a total, integer effective electric charge of $Q_{total} = +1e$. Because the three loops of the $6^3_2$ Borromean linkage are mutually entangled, the total global phase twist is distributed across a degenerate structural ground state. In a non-linear dielectric substrate, a composite defect with internal permutation symmetry generates a discrete CP-violating $\theta$-vacuum phase. By the **Witten Effect**, a topological magnetic defect embedded in a $\theta$-vacuum acquires a fractionalized effective electric charge:

> **[Resultbox]** *Topological Fractionalization (Witten Effect)*
>
> $$
> q_{eff} = n + \frac{\theta}{2\pi}e
> $$

The $6_{2}^{3}$ Borromean linkage possesses three-fold permutation symmetry ($\mathbb{Z}_{3}$). This topological constraint restricts the allowed degenerate phase angles of the local trapped vacuum to mathematical thirds ($\theta\in\{0,\pm2\pi/3,\pm4\pi/3\}$). Substituting these discrete angles into the Witten charge equation yields the effective fractional charges observed in nature ($q_{eff}\in\{\pm1/3e,\pm2/3e\}$). Quarks are thus defined as deconfined topological quasiparticles.

> **[Examplebox]** *Evaluating Quark Fractional Charges via the Witten Effect*
>
> **Problem:** The $6^3_2$ Borromean linkage possesses discrete $\mathbb{Z}_3$ permutation symmetry, restricting the topological phase angles of the trapped vacuum to mathematical thirds ($\theta = \pm 2\pi/3, \pm 4\pi/3$). Evaluate the effective electric charges of these deconfined topological quasiparticles using the Witten Effect.
>
> **Solution:** The Witten equation dictates topological fractionalization natively without fundamental point-particles:
>
> $$
> q_{eff} = n_{twist} + \frac{\theta}{2\pi} e
> $$
>
> Assuming an uncharged base node ($n_{twist} = 0$), substitute the allowed permutation angles.
> For $\theta = \pm 2\pi/3$:
>
> $$
> q_{eff} = 0 + \frac{\pm 2\pi/3}{2\pi} e = \pm \frac{1}{3} e
> $$
>
> For $\theta = \pm 4\pi/3$:
>
> $$
> q_{eff} = 0 + \frac{\pm 4\pi/3}{2\pi} e = \pm \frac{2}{3} e
> $$
>
> These exact evaluations derive the Down ($-\frac{1}{3}e$) and Up ($+\frac{2}{3}e$) quark charge states directly from the discrete group symmetries of the Borromean linkage without fractionalising the unbroken substrate itself.

---

## Two-Ontology Reconciliation: these fractions are the EFFECTIVE dressing of the FUNDAMENTAL integer charge
<!-- claim-quality: clm-w8jn3q -->

**Grant-ratified 2026-06-23.** The Witten fractional charges above (Ontology A) and the integer charge-linking $\mathcal{Q} \in \mathbb{Z}$ (Ontology B — the proton's $Q_{total} = +1e$, the neutron's literal $+1 + (-1) = 0$ at `neutron-identification.md:13,24`) are **NOT contradictory.** They are nested:

- **Ontology B is FUNDAMENTAL.** Charge is the integer linking number $\mathcal{Q} = \mathrm{Link}(\partial\Omega, \mathbf{F}_{\text{substrate}}) \in \mathbb{Z}$ — a 1D line/loop boundary integral ([`../../../common/boundary-observables-m-q-j.md`](../../../common/boundary-observables-m-q-j.md), the $\mathcal{Q}$ row of the three canonical boundary observables).
- **Ontology A is the EFFECTIVE appearance.** The fractions $\pm 1/3, \pm 2/3$ are a *dressing* of the integer, carried by the soliton's body angular momentum $\mathcal{J} = \mathrm{Wind}(\partial\Omega)$ — a *separate* 2D surface boundary integral. The dressed effective charge is $q_{eff} = \mathcal{Q} + \theta/2\pi$ with $\mathcal{Q}$ the fundamental integer and $\theta/2\pi$ the effective $\mathcal{J}$-dressing.

**The mechanism is the $\mathcal{Q}/\mathcal{J}$ boundary-integral separability.** A rigid body-frame rotation $\mathcal{J}$ leaves the linking integer $\mathcal{Q}$ INVARIANT (linking is a topological invariant — a rigid rotation cannot change it). So $\mathcal{J}$ dresses the EFFECTIVE charge WITHOUT touching the FUNDAMENTAL integer. This supplies the substrate-native mechanism for the A↔B compatibility the corpus already half-states at `neutron-identification.md:67` (*"the two ontologies make the same predictions about observables; AVE's mechanical picture is the substrate explanation of why the SM ontology works"*). **The two ontologies are therefore RECONCILED, not in tension.**

> **Honesty note (Rule-11) — CLASS: FORM / CONSISTENCY, not a chord.** The per-constituent share is $1/N$ by symmetry for ANY $N$; the substrate excludes no $N$ (swept $N \in \{2,3,4,5\}$). The denominator VALUE $3$ is FED IN — it is the OBSERVED proton loop count ($N=3$ from the $6_2^3$ Borromean asserted at `proton-identification.md:22`; "why exactly 3 loops" is OPEN). There is NO 3-loop stability theorem. So the reconciliation is a structural advance (it replaces the hard-coded literal `theta_angles = [0, (2*np.pi)/3, (4*np.pi)/3]` at `tensors.py:106` with a symmetry-forced $1/N$ share, AND cleanly separates fundamental-integer from effective-dressing) — but it does NOT make the $3$ derived. The remaining chord-decider is whether the lattice FORCES exactly-3-loop Borromean stability (OPEN, parked). Full provenance: `research/2026-06-23_witten-angular-momentum-charge_result.md` (lands via PR #396; plain-text reference pending that merge); register entry `clm-w8jn3q` ([`../../../vol2/claim-quality.md`](../../claim-quality.md)).

---
