# Phase 1 — Electron Invariants in Universal-Operator Language

**Status:** Phase 1 wrap-up. Reframes the electron's topological characterization in AVE-native universal-operator language (per user hint 2026-04-20: "invariant usually comes with the universals in AVE"). Resolves — or reframes — queue items [7] and [8].
**Prerequisites:** `00_` – `06_`; [`src/ave/core/universal_operators.py`](../../src/ave/core/universal_operators.py) (file header + Op10 at line 535).

**Primary finding:** AVE's native topological invariant for the electron is the **scalar crossing number $c = 3$**, not the Hopfion-literature pair $(w_1, w_2)$. The major-vs-minor assignment I've been wrestling with across `02_` §7.2, `05_`, `06_`, and queue [8] is a category error imported from external topology literature — **AVE's universal operators don't care which axis is major.** This substantially revises the framing of earlier docs; queue items to follow.

---

## §1  Why this matters

User hint 2026-04-20: *"invariant usually comes with the universals in AVE."*

Survey of [`src/ave/core/universal_operators.py`](../../src/ave/core/universal_operators.py) confirms this strongly. The file header enumerates the canonical operator basis:

```
1. Impedance (Z)               — Axiom 1
2. Saturation (S)              — Axiom 4
3. Reflection (Γ)              — Axiom 3
4. Pairwise Energy (U)         — Axioms 1-4
5. Y-Matrix → S-Matrix (Y→S)   — Axiom 3 (multiport)
6. Eigenvalue Target (λ_min)   — Axiom 3 (eigenstate)
7. Spectral Analysis (FFT)     — DSP complement
8. Packing Reflection (Γ_pack) — Axioms 3+4 (macroscopic)
9. Steric Reflection (Γ_steric) — Axiom 3 (pairwise exclusion)
10. Junction Projection Loss (Y) — Axioms 1+2 (crossing geometry)
11. Topological Curl (∇×V)
12. Topological Divergence (∇·V)
13. D'Alembertian Wave (◻²)
14. Dynamic Impedance (Z_eff)
15. Virtual Strain Iso (r_v)
```

Plus Op21 (Quality Factor $Q = \ell$) and Op22 (Avalanche $M$ with topological $n$) at line 845+. Each is scale-invariant and domain-agnostic.

**The operator that handles topology is Op10 — Junction Projection Loss.** Reading lines 535–633 carefully, Op10's entire content for the topological invariant is a single scalar: $c$, the number of crossings per orbit.

---

## §2  Op10 — the canonical topological invariant in AVE

The operator's closed form ([`universal_operators.py:575–579`](../../src/ave/core/universal_operators.py#L575)):

$$\boxed{\quad Y_{\text{loss}}(\theta, c) = c \cdot \frac{1 - \cos\theta}{2\pi^2} \quad}$$

where:
- $\theta$: junction angle between incident and transmitted waveguide directions on the discrete lattice
- $c$: number of crossings per orbit — **the topological invariant**

The docstring is explicit: *"c is the number of crossings per orbit (topological invariant)."* Cross-scale validated in the operator's own comment (line 598–603):

| Scale | $\theta$ | $c$ |
|---|---|---|
| Protein | $109.47°$ | $1$ |
| Baryon | $90°$ | $6$ |
| Atomic Boron | $90°$ | $2$–$4$ |

**Critically:** $c$ is a scalar integer, not a pair, not a tuple, not direction-dependent. The operator returns the same $Y_{\text{loss}}$ regardless of which axis of the torus is "major" or "minor." **This is what Grant meant by "invariants come with the universals."**

The $2\pi^2$ denominator is the spin-1/2 half-cover of the Clifford torus (same constant that gives Ch 8 $\Lambda_{\text{surf}} = \pi^2$), derived from the operator's own structural argument (line 558–569) — so Op10 IS the Ch-8 half-cover observable, re-expressed as a universal operator.

---

## §3  The electron's $c$

From Ch 8 and [`src/ave/topological/faddeev_skyrme.py:17`](../../src/ave/topological/faddeev_skyrme.py#L17):

> *"The electron's topology is an unknot ($0_1$), but its phase winding number follows the (2,3) pattern with $c_3 = 3$ crossings."*

**For the electron: $c = 3$.**

This is THE AVE-native invariant that characterizes the electron topologically. Not a pair. One number. A scalar integer.

The "(2,3)" is *torus-knot type notation*, where:
- **2**: the series index — fixed at 2 for the entire $(2,q)$ torus-knot ladder (electron, proton, baryons, etc.) per the `(2,q)` stability rule (q odd) in [`faddeev_skyrme.py:18`](../../src/ave/topological/faddeev_skyrme.py#L18).
- **3**: the crossing count $c$ — the actual invariant. For proton, $c=5$ (cinquefoil); for Δ, $c=7$; and so on. Successive baryon generations step $c$ by 2.

The formula that relates knot-type to crossing count for $(2, q)$: $c = q$ when $q \geq 3$. Verified: trefoil $(2,3) \to c=3$; cinquefoil $(2,5) \to c=5$; septafoil $(2,7) \to c=7$.

---

## §4  What this dissolves

### 4.1  The major-minor ambiguity (queue [8])

In `02_` §7.2, `03_` §4.3, `05_` throughout, and `06_` §3, I treated the electron's topology as a Hopfion-literature winding pair $(w_1, w_2) = (2, 3)$ and spent substantial effort adjudicating which number goes on the major vs minor cycle of the Clifford torus (`06_` §6, queue [8], chat reasoning about energy minimization giving $(3,2)$).

**This entire thread is a category error.** AVE's universal-operator language does not assign winding numbers to axes. It uses $c = 3$, a scalar. The "(2,3)" in AVE is *knot-type notation*, not a $(w_1, w_2)$ pair. The major-vs-minor assignment is a Hopfion-literature convenience that AVE's own operators don't use.

**Queue [8] resolves: no assignment is needed.** The electron has $c = 3$, and that's the AVE-native invariant. `02_` §7.2 should be revised to express the topological boundary condition in terms of $c$ rather than $(w_1, w_2)$. Similar revisions for `03_`, `05_`, `06_`.

### 4.2  The Williamson-van der Mark tension (queue [7])

In `06_` I set up an elaborate projection chain to reconcile AVE's $(2,3)$ with WvdM's 2:1. The honest reframing:

- **AVE:** electron is a **(2,3)-type torus-knot phase structure with $c = 3$**. Phase-space topology on the Clifford torus. Scalar invariant: $c$.
- **WvdM:** electron wavefront path is a **(2,1) torus winding, $c = 0$ (unknot)** in physical space. This IS the specific semi-classical photon trajectory — and per the canonical Alexander-Conway classification, $(2,1)$ is not a knot, it's an unknotted closed curve with a 2:1 winding ratio on the torus.

Under the universal-operator reframing, these two "electrons" are characterized by:

| | AVE phase-space picture | WvdM physical-path picture |
|---|---|---|
| Crossing count $c$ | $3$ | $0$ (unknot) |
| Torus winding pair $(p, q)$ | $(2, 3)$ | $(2, 1)$ |
| Space | Clifford $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ (phase-space shell) | Physical $\mathbb{R}^3$ (photon trajectory) |

**These are different observables on different tori.** WvdM's 2:1 ratio is a geometric path winding; AVE's $(2,3)$ is a phase-space knot type. They can both be true simultaneously because they characterize different slices of the same electron.

This is a *stronger* resolution than the "different invariants at different projection levels" story in `06_`. Not only are they at different projection levels; they're different *kinds* of invariants (phase-space knot topology vs geometric path ratio).

### 4.3  Reading (a) vs Reading (b) (revisited)

In `01_` §10, `05_`, I spent time distinguishing Reading (a) (Sutcliffe Hopfion with $Q_H = 6$) from Reading (b) (factorized SU(2) with dual-$U(1)$ winding). Under the universal-operator reframing:

- **Reading (a):** uses Hopf invariant, a pure-math pure-S² construct. Not native to AVE's operator basis.
- **Reading (b):** uses $(w_1, w_2)$ pair — ALSO not native to AVE. It's just a different Hopfion-literature convention.
- **Neither is the AVE-native picture.** AVE-native: $c = 3$ via Op10.

This suggests `01_` §4 should be significantly simplified. The four candidate identities (C1–C4) for the $\hat{\mathbf{n}} \leftrightarrow \boldsymbol{\omega}$ map are still relevant (they're about the field variable, not the invariant), but the "(2,3) phase winding" readings (a)/(b)/(c) were all downstream of an imported-literature framing that AVE doesn't use.

---

## §5  The electron via universal operators — revised characterization

The electron in AVE-native language:

1. **Cosserat field.** Under C3, the electron is a localized ground-state configuration of $\boldsymbol{\omega}(\mathbf{r})$ with $U(\mathbf{r}) = \exp(i\boldsymbol{\sigma}\cdot\boldsymbol{\omega}/2) \in SU(2)$.

2. **Topological sector.** Characterized by $c = 3$ crossings — the $(2, 3)$ entry in the $(2, q)$ torus-knot ladder.

3. **Op10 consequence.** At Clifford-torus crossings (angle $\theta = \pi/2$):
$$Y_{\text{loss}} = 3 \cdot \frac{1 - \cos(\pi/2)}{2\pi^2} = \frac{3}{2\pi^2} \approx 0.152$$
   This is the fractional energy projection loss per orbit at a single crossing. The electron's ground state accommodates this loss three times (once per crossing).

4. **Op21 consequence.** $Q = \ell$ — but Ch 8's $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038$ is a **composite** Q-factor from multipole decomposition, not a simple mode count. Op21 supplies the single-mode ingredient; Ch 8 sums three multipole contributions.

5. **Op22 consequence.** Avalanche factor with $n_{\text{topology}} = 3$ determines how the electron's Cosserat soliton responds to driving near breakdown — relevant for Phase-3 autoresonance checks.

6. **Op11–Op12 consequence.** Topological curl/divergence map the winding integrals onto the K4 discretization. For the $(2, 3)$ sector, the integrated curl over the Clifford shell returns quantized integer values consistent with $c = 3$.

No mention of $(w_1, w_2)$, major, minor, or Hopf invariants is required.

---

## §6  Phase-3 validation map (revised)

The Phase-3 Cosserat field solver produces a relaxed ground-state $\boldsymbol{\omega}^\star(\mathbf{r})$. The validation checks are:

1. **Extract $c$ from the solved field.** Integrate the Op11 topological curl along canonical closed curves on the emergent toroidal shell; count crossings of the preimage curves of $\hat{\mathbf{n}}$ on a suitable projection plane. **Require $c = 3$.**

2. **Extract Golden-Torus radii $(R, r)$.** Locate the shell's major and minor radii by direct geometric measurement of the relaxed field's isosurfaces. **Require $(R, r) = (\varphi/2, (\varphi-1)/2) \pm$ tolerance.**

3. **Extract Q-factor via multipole decomposition.** Integrate $\Lambda_{\text{vol}}, \Lambda_{\text{surf}}, \Lambda_{\text{line}}$ over the solved field. **Require $\alpha^{-1} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}} = 4\pi^3 + \pi^2 + \pi$.**

4. **Check Op10 at crossings.** Measure junction-projection loss at the three topological crossings. **Require $Y_{\text{loss}}^{\text{per-crossing}} \approx 1/(2\pi^2)$, summed to $3/(2\pi^2)$.**

All four are derivable from the solved field; no Hopfion-literature machinery needed.

---

## §7  Queue updates

Queue items to reflect the universal-operator reframing:

- **[8]** (major-minor convention): **mark as resolved — no assignment needed.** The distinction was imported from Hopfion literature and is not AVE-native. Requeue only if Phase-3 numerics reveals an axis-dependent observable that the universal operators miss.
- **[9]** (new): revise `02_` §7.2 topological boundary condition to express the electron sector in terms of $c = 3$ (scalar) rather than $(w_1, w_2)$ pair. Retain the SU(2) field formulation (from C3 canonization) but drop the factorized base+fibre boundary-condition specification in favor of a single crossing-number specification.
- **[10]** (new): revise `06_` §3, §5, §8 — the projection map becomes simpler: AVE and WvdM speak the same $(p, q)$ torus-knot language but on different tori (phase-space vs physical-space), giving $c = 3$ vs $c = 0$ for the respective observables. No Cosserat → EM projection-chain contortions needed.
- **[11]** (new): revise `05_` §8 — the three-readings framework is superseded by "invariant = $c = 3$." Readings (a)/(b)/(c) all collapse; what remains is the field-formulation choice (C3 SU(2) embedding, as adjudicated in `01_` §10).
- **[1]** (still valid): Ch 8 footnote clarifying unknot vs phase-winding remains important — the universal-operator reframing doesn't change the need for Ch 8 to clarify that the spatial flux tube is unknotted while the phase structure has $c = 3$.
- **[2], [4], [5], [6], [7]** carry through with light rephrasing; none is invalidated.

---

## §8  Status

**Phase 1 wrap-up: substantially advanced.** The major-minor ambiguity is resolved (as dissolved rather than answered). The WvdM tension is resolved (as different tori / different observables). The remaining open items are:

- Queue [4]: rigorous existence/uniqueness proofs for the Cosserat variational problem (standard adaptation of Hopfion-literature; still to be formalized).
- Queue [9], [10], [11]: re-expressing earlier docs in universal-operator language. Moderate-effort editorial work, adds clarity.
- Phase-2 discretization design can proceed once the above cleanups land.

**This is a good stopping point for Phase 1.** The theoretical spine is complete, framed in AVE-native language, with all previously-open tensions resolved or dissolved.
