# Phase 1 — Reading (a) ↔ Reading (b) Equivalence Check

**Status:** Phase 1 wrap-up task. Pressure-test of Reading (b) (canonized in `01_` §10 and implemented in `02_` §7.2) against Reading (a) (Sutcliffe-2007 torus-Hopfion convention).
**Prerequisites:** `01_` §10, `02_` §7.2, `03_` §4.3.

**Finding, surfaced first:** Reading (b) as written in `02_` §7.2 is **NOT equivalent** to Reading (a) Sutcliffe torus Hopfion. They describe genuinely different topological sectors. This is a flag-don't-fix finding requiring your adjudication before Phase 2 begins.

The rest of this document works the check in detail.

---

## §1  Goal of this check

Verify that the canonical topological sector for the electron — Reading (b): "$(w_1, w_2) = (2, 3)$ dual-$U(1)$ winding on the Clifford torus" — is equivalent as a homotopy class to Reading (a): "Hopfion with Hopf invariant $Q_H = 6$ and $(2, 3)$-torus-knot preimages" (Sutcliffe 2007 convention).

If the two readings are equivalent, external literature (Sutcliffe 2007, Battye-Sutcliffe 1998, Hietarinta-Salo 2000) provides numerical validation data + the existing methodology for computing torus-Hopfion ground states transfers directly.

If the two readings are not equivalent, we are committed to a topological sector that has no published numerical precedent, and validation must be internal.

---

## §2  Reading (a) formulated precisely

The Sutcliffe-2007 torus Hopfion of type $(p, q)$ is a map $\mathbf{\hat{n}}: \mathbb{R}^3 \to S^2$ with asymptotic condition $\hat{\mathbf{n}} \to \hat{\mathbf{z}}$ at infinity, given (in the standard ansatz) by

$$\hat{\mathbf{n}}(\mathbf{r}) = \big(\sin\Phi(\mathbf{r})\cos\Theta(\mathbf{r}),\ \sin\Phi(\mathbf{r})\sin\Theta(\mathbf{r}),\ \cos\Phi(\mathbf{r})\big)$$

with:

- $\Phi(\mathbf{r})$: a polar angle function localizing the Hopfion to a toroidal region, $\Phi = 0$ at infinity, $\Phi = \pi$ at the core centerline
- $\Theta(\mathbf{r}) = p\,\varphi + q\,\psi$: a **single combined phase** built from the azimuthal angle $\varphi$ (around the $\hat{\mathbf{z}}$ axis) and a meridional angle $\psi$ (around a toroidal ring)

The key structural fact: **$\Theta$ is a single scalar function of position**, not two independent phases. The $(p, q)$ is a decomposition of $\Theta$ into two cycle contributions, but the field carries one phase, not two.

**Topological invariants of Reading (a):**

- **Hopf invariant** $Q_H = p \cdot q$. For the electron case $(p, q) = (2, 3)$: $Q_H = 6$.
- Preimages of $\hat{\mathbf{n}} = \hat{\mathbf{z}}'$ (any fixed unit vector) trace out $(p, q)$-torus knots on the bounding toroidal shell. For $(2, 3)$: trefoil knots.
- Any two generic preimages link with linking number $pq = 6$.
- Reference: Sutcliffe 2007 Proc. R. Soc. A **463**, 3001; also Manton-Sutcliffe 2004 Ch 9.

---

## §3  Reading (b) as written in `02_` §7.2

From `02_` §7.2, the electron's topological sector under Reading (b) is specified by two *independent* field conditions on the Clifford-torus shell at radii $(R, r)$ with major/meridian coordinates $(\theta_1, \theta_2)$:

$$\hat{\mathbf{n}}(\theta_1, \theta_2 = \text{const}) = \big(\sin\phi_\star\cos 2\theta_1,\ \sin\phi_\star\sin 2\theta_1,\ \cos\phi_\star\big) \quad (\text{eq. 7.2a})$$

$$\alpha_\parallel(\theta_1 = \text{const}, \theta_2) = 3\theta_2 + \text{const} \quad (\text{eq. 7.2b})$$

with $\alpha_\parallel$ the $U(1)$ fibre phase of the $SU(2) \to S^2$ projection.

Equivalently, the SU(2) field factorizes on the shell:

$$U(\theta_1, \theta_2) = U_{\hat{n}}(\theta_1) \cdot U_\alpha(\theta_2)$$

with $U_{\hat n}$ an $SU(2)$ element whose projection $\hat{\mathbf{n}}$ winds twice as $\theta_1$ traverses $[0, 2\pi)$, and $U_\alpha$ a pure $U(1)$ rotation by $3\theta_2$ about a fixed axis.

**The two phase windings are independent functions of independent coordinates.** This is the essential structural difference from Reading (a).

---

## §4  Topological analysis of Reading (b)

### 4.1  Hopf invariant of the $\hat{\mathbf{n}}$-field alone

Under Reading (b), what is the Hopf invariant of the S²-projection $\hat{\mathbf{n}}$?

On the Clifford torus, $\hat{\mathbf{n}}(\theta_1, \theta_2) = (\sin\phi_\star \cos 2\theta_1,\ \sin\phi_\star \sin 2\theta_1,\ \cos\phi_\star)$ does not depend on $\theta_2$ at all. The preimage of any fixed $\hat{\mathbf{n}}_0 \in S^2$ on the Clifford torus is either empty (if $\hat{\mathbf{n}}_0$ is not on the circle swept by $\hat{\mathbf{n}}$) or a finite set of meridional circles (if $\hat{\mathbf{n}}_0$ is on the swept circle — two preimages of each specific $\hat{\mathbf{n}}_0$ due to the 2× winding).

Extend $\hat{\mathbf{n}}$ off the torus smoothly to $\hat{\mathbf{z}}$ at infinity. The preimages of generic $\hat{\mathbf{n}}_0 \in S^2$ in all of $\mathbb{R}^3$ are meridional circles on the torus (the extended field decays to constant $\hat{\mathbf{z}}$ outside and contributes nothing extra).

**Two parallel meridional circles on a torus are not linked.** Their linking number is zero.

Therefore, under Reading (b) as written:

$$\boxed{Q_H(\hat{\mathbf{n}}) = 0}$$

— topologically trivial in the S² Hopf sense.

### 4.2  Why "winding 2 around the major axis" doesn't imply non-trivial $Q_H$

It's tempting to think $\hat{\mathbf{n}}$ winding twice around the major axis should carry topological charge. But:

$$\pi_1(S^2) = 0$$

Any map $S^1 \to S^2$ is continuously contractible to a constant. The "2× winding" of $\hat{\mathbf{n}}$ around $\theta_1$ is a smooth curve on $S^2$ that traces a circle twice — this is homotopic to a constant map via uniform shrinking.

Only maps $S^3 \to S^2$ can have non-trivial topology ($\pi_3(S^2) = \mathbb{Z}$, detected by the Hopf invariant). The Hopf invariant sees three-dimensional linking structure, not one-dimensional winding.

**Reading (b)'s n̂ field has no three-dimensional linking structure** because its preimages are parallel circles with no mutual linking. Hence $Q_H = 0$.

### 4.3  Where is the (2, 3) topology in Reading (b)?

The $(2, 3)$ pair of windings in Reading (b) lives in:

- $w_1 = 2$: the winding of $\hat{\mathbf{n}}$ around $\theta_1$ — an element of $\pi_1(S^2)$, which is trivial, so this winding is not a global topological charge but a local boundary condition.
- $w_2 = 3$: the winding of $\alpha_\parallel$ around $\theta_2$ — an element of $\pi_1(S^1)$, which is $\mathbb{Z}$, so this IS a nontrivial charge: the $U(1)$ fibre has a real winding.

The electron's topological charge under Reading (b) is **the $U(1)$ winding $w_2 = 3$**, carried by the fibre of the SU(2) field, not by the S² projection. The $w_1 = 2$ is a boundary-condition prescription for the fibre-bundle structure, not a separately quantized charge.

Under Reading (b), the electron is a $w_{U(1)} = 3$ vortex on a 2-winding-around-$\theta_1$ spinor bundle over the torus. This is **a different object than a Hopfion.**

---

## §5  Conclusion: (a) ≢ (b)

Reading (a) (Sutcliffe Hopfion with $Q_H = 6$) and Reading (b) (factorized SU(2) with $w_{U(1)} = 3$ on a double-wound spinor bundle) are **topologically distinct sectors**. They are not equivalent homotopy classes.

| Property | Reading (a) | Reading (b) |
|---|---|---|
| Field is | S² unit vector $\hat{\mathbf{n}}$ | Full SU(2) element $U$ (not reducible to $\hat{\mathbf{n}}$) |
| Phase structure | Single combined phase $\Theta = 2\varphi + 3\psi$ | Factorized: $2\theta_1$ in S² base, $3\theta_2$ in U(1) fibre |
| Topological invariant | Hopf invariant $Q_H = 6$ | U(1) fibre winding $w_{U(1)} = 3$ on twice-wound bundle |
| External literature | Sutcliffe 2007, Battye-Sutcliffe 1998 | No direct precedent found (see §7) |
| Preimage structure | (2,3) torus-knot curves | Meridional circles (of $\hat{\mathbf{n}}$); interior lines of U(1) fibre |

---

## §6  Implications

1. **The `01_` §10 and `02_` §7.2 writing of Reading (b) should not claim equivalence to Sutcliffe Hopfions.** The adjudication in `01_` §10.1 noting Reading (a) as a "fallback" was right to distinguish them, but my subsequent writing in `02_` and `03_` sometimes used Reading-a language ("torus-knot preimages," "linking number") that implied equivalence. Queue item [6] below corrects this.

2. **Reading (b) has no direct external literature precedent.** Hopfions (Reading a) have a developed numerical and analytical literature. U(1)-vortex-on-spinor-bundle objects (Reading b) have scattered literature in liquid-crystal and superconductor contexts (Anderson-Toulouse monopoles, boojums, skyrmion-vortex composites) but no published $(2, 3)$ torus-sector torus-winding case that I can point to.

3. **Reading (b) is closer to Reading (c) than to Reading (a).** The joint pair $(w_1, w_2) = (2, 3)$ with $w_1$ a local boundary datum and $w_2$ the global U(1) charge is a joint-invariant structure, not a single-invariant Hopfion.

4. **We have a decision to make before Phase 2.** Either:

   - **(α)** Stay with Reading (b) as written — the factorized SU(2) sector. Accept that external literature validation is limited; Phase-3 numerics becomes the primary validation mechanism. The Cosserat framework's SU(2)-native identity (C3) is a natural fit for this reading.
   - **(β)** Switch to Reading (a) — the Sutcliffe Hopfion. Rewrite `02_` §7.2 to use the combined phase $\Theta = 2\varphi + 3\psi$. Gain direct external literature leverage. But: this uses only the S² projection, losing the U(1) fibre information that makes Ch 8's spin-1/2 half-cover argument natural under C3.
   - **(γ)** Investigate whether Ch 8's Golden-Torus geometry uniquely selects one. The $R \cdot r = 1/4$ argument in `03_` §4.3 used the SU(2) half-cover; does it also work (or fail) under Reading (a)'s pure-S² field?

---

## §7  Where the Cosserat canonization (C3) points — amended 2026-04-20

**Amendment note:** Original §7 argued that Reading (a) "drops the U(1) fibre entirely" while Reading (b) retains it natively. That was overstated. Reading (a) written as a full SU(2) field (not just an S² field) *does* carry fibre-phase content — it just expresses it through the combined Hopfion phase $\Theta = 2\varphi + 3\psi$ rather than as a separately-tracked variable. Both (a) and (b) are valid SU(2)-field formulations; they differ in how the $(2, 3)$ winding is distributed between the base and fibre sectors. Whether one ends up energy-minimizing and the other not is a Phase-3 numerical question, not a Phase-1 topological one.

Under C3, the primary field is the Cosserat microrotation $\boldsymbol{\omega}$ with SU(2) element $U = \exp(i\boldsymbol{\sigma}\cdot\boldsymbol{\omega}/2)$. Both Reading (a) and Reading (b) are specific ansätze for how the $(2, 3)$ winding is realized in $U$:

- **Reading (a):** single combined phase in $U$: $\Theta(\mathbf{r}) = 2\varphi(\mathbf{r}) + 3\psi(\mathbf{r})$, giving preimages that are $(2, 3)$-torus knots. $Q_H(\hat{\mathbf{n}}) = 6$.
- **Reading (b):** factorized $U = U_{\text{base}}(\theta_1) \cdot U_{\text{fibre}}(\theta_2)$ with independent winding in each sector. $Q_H(\hat{\mathbf{n}}) = 0$; topological content is in the U(1) fibre winding.

Which reading is physical in AVE — i.e., which ground state the energy-minimizing dynamics of $\mathcal{L}_{\text{AVE}}$ actually produces — is **a Phase-3 numerics question.** It's premature for Phase-1 to lock this in.

**Revised recommendation:** Hold Reading (b) as the canonical *boundary-condition prescription* for Phase-1 writeups, but do not treat the distinction between (a) and (b) as settled. Phase 3 adjudicates.

**Your adjudication required** for Phase-1 documentation language: either (i) treat the two readings as distinct Phase-3 hypotheses to be tested numerically; or (ii) commit to (a) now (simpler, more literature); or (iii) commit to (b) now (more Cosserat-faithful in sense of `00_` §2, less literature).

---

## §8  Questions for adjudication

1. **Does Reading (b) stand, or do we switch to Reading (a)?** My recommendation is (b), staying with the full Cosserat/SU(2) structure. If (a), we rewrite `02_` §7.2 and much of `03_` to use the single-combined-phase Sutcliffe ansatz.

2. **If (b): do we rename Reading (c) or merge it into (b)?** Reading (b) as carefully analyzed in this document *is* a joint-invariant $(w_1, w_2)$ structure — which was (c)'s framing in `01_` §10. The three readings may collapse to two: (a) vs (b)/(c), with (b) = (c).

3. **If (b): what literature do we cite for validation?** Hopfion literature (Sutcliffe) becomes a "related work" citation rather than a validation target. Candidates for closer precedent: Anderson-Toulouse monopoles (liquid crystals), skyrmion-vortex composites (chiral magnets), boojums (liquid helium). Phase-1 sub-task: literature landscape for U(1)-fibre-on-S²-base sectors.

---

## §9  Queue updates

**Item [6]:** correct `01_` §10 and `02_` §7.2 + `03_` §4.3 to avoid implying Reading (b) ≡ Reading (a). Specifically remove any phrasing that equates the factorized SU(2) sector with a Sutcliffe Hopfion. Queued in `DOCUMENTATION_UPDATES_QUEUE.md`.

---

## §10  Status

Reading-(a)-vs-Reading-(b) equivalence: **FALSE.** They are distinct topological sectors.

Phase-1 wrap-up impact: Reading (c) observable search is no longer a separate task — it is partially answered by this document, which shows Reading (b) already carries joint-invariant structure. Remaining Phase-1 wrap-up: rigorous existence/uniqueness proofs (queue [4]), adjudication of §8 questions.
