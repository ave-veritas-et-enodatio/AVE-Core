# Phase 3 — Topological Self-Inductance via the Hopf/Chern-Simons Term

**Status:** DRAFT. Closes the "missing self-inductance term" gap identified after `12_`'s reflection-term commit-and-test stalled at the initial configuration. Based on finding from the AVE-HOPF sibling repo that the electron's total inductance has a distinct self-L contribution that doesn't cancel under field superposition. Proposes a Chern-Simons-style $\mathbf{A}\cdot\mathbf{B}$ Lagrangian term to capture this.
**Prerequisites:** `00_`–`12_`; [`AVE-HOPF/scripts/hopf_01_classical_coupling.py`](../../../AVE-HOPF/scripts/hopf_01_classical_coupling.py) (classical self + mutual decomposition); [Ch 8 §(b)(c)](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex) (three-Λ decomposition).
**Sequel:** solver extension with FFT-based Hopf density, final validation.

---

## §1  The three Ch 8 contributions map to three physical inductance types

The AVE-HOPF repo's [`hopf_01_classical_coupling.py`](../../../AVE-HOPF/scripts/hopf_01_classical_coupling.py) models torus-knot antenna inductance as

$$L_{\text{total}} = L_{\text{self}}(L_{\text{wire}}) + N_{\text{cross}} \cdot M_{\text{per crossing}}$$

with explicit closed-form expressions for each term (Neumann formula for M, standard wire-self-L formula for L_self). These are *different* physical quantities that don't reduce to each other.

Ch 8 decomposes α⁻¹ into three Λ terms. Mapped onto the self + mutual physics:

| Ch 8 term | Value at Golden Torus | Physical interpretation |
|---|---|---|
| $\Lambda_{\text{vol}} = 16\pi^3\,R\,r$ | $4\pi^3 \approx 124$ | **Topological self-L** — phase-space hyper-volume with spin-1/2 double cover. Doesn't cancel under field superposition. |
| $\Lambda_{\text{surf}} = 4\pi^2\,R\,r$ | $\pi^2 \approx 9.87$ | **Mutual-M at crossings** — Op10 screening contribution |
| $\Lambda_{\text{line}} = \pi\,d$ | $\pi \approx 3.14$ | **Line/Nyquist term** — tube self-inductance at minimum lattice thickness |

Of these, `11_` captured $\Lambda_{\text{surf}}$ via the Op10 wedge term. `12_` added the reflection term as a Pauli-wall penalty (contributing to $\Lambda_{\text{line}}$ physics — "tube can't collapse below d"). **$\Lambda_{\text{vol}}$ is still structurally absent from the Lagrangian.** That's why the energy landscape in both `11_` and `12_` has no robust minimum in R — nothing rewards the soliton for *having* a winding, just for the local strain patterns a winding happens to produce.

---

## §2  Why the field-squared integral misses this

For a classical EM field $\mathbf{B} = \nabla\times\mathbf{A}$, the stored energy

$$E = \tfrac{1}{2\mu_0}\int|\mathbf{B}|^2\,d^3r$$

is identically equal to the lumped $\tfrac{1}{2}L_{\text{total}}I^2$ when a current $I$ runs through a defined loop. The self + mutual decomposition is a bookkeeping convenience for discrete wire geometries; the volume integral already sums them.

**But:** the volume integral of $|\mathbf{B}|^2$ is NOT a topological invariant. It depends on the actual field values. If two counterflowing flux contributions cancel in a region, $|\mathbf{B}_{\text{net}}|^2 = 0$ there, and that region contributes zero energy — *even if* each contribution separately has nonzero magnitude.

For a Hopfion soliton characterized by a topological invariant (Hopf number $Q_H = p\,q$), the volume integral of $|\mathbf{B}|^2$ correctly totals the classical EM energy. But **additional energy is stored in the topological structure itself** — the linking/twisting of the flux lines. This additional energy is captured by:

$$\mathcal{L}_{\text{Hopf}}(\mathbf{r}) = \tfrac{1}{2}\,\mathbf{A}(\mathbf{r}) \cdot \mathbf{B}(\mathbf{r})$$

whose integral over space gives (up to normalization) the Hopf invariant:

$$\int \mathbf{A}\cdot\mathbf{B}\,d^3r = 4\pi^2\,Q_H$$

This is the Chern-Simons 3-form in 3D. It is **nonzero even when $|\mathbf{B}|^2 \to 0$ locally** — flux cancellation in the center doesn't erase the topological linking of the flux contributions.

---

## §3  The proposed Lagrangian addition

Add to the existing Cosserat Lagrangian:

$$\mathcal{L}_{\text{Hopf}}(\mathbf{r}) \;=\; k_H \cdot \tfrac{1}{2}\,\mathbf{A}(\mathbf{r}) \cdot \mathbf{B}(\mathbf{r})
\tag{3.1}$$

where:
- $\mathbf{B}_k = \tfrac{1}{2}\epsilon_{kij}\,F_{ij}$ — the synthetic magnetic field from the Hopf pullback $F_{ij} = \hat{\mathbf{n}}\cdot(\partial_i\hat{\mathbf{n}}\times\partial_j\hat{\mathbf{n}})$.
- $\mathbf{A}$ — gauge potential in Coulomb gauge, solving $\nabla\times\mathbf{A} = \mathbf{B}$ and $\nabla\cdot\mathbf{A} = 0$.

Under Ch 8 matching, the integrated Hopf density at Golden Torus should equal $\Lambda_{\text{vol}} = 4\pi^3$. Given the topological normalization $\int \mathbf{A}\cdot\mathbf{B}\,d^3r = 4\pi^2 Q_H$ with $Q_H = p\cdot q = 6$ for the (2,3) electron:

$$k_H \cdot \tfrac{1}{2} \cdot 4\pi^2 \cdot 6 \;\overset{!}{=}\; 4\pi^3$$

$$\boxed{\;\;k_H \;=\; \frac{\pi}{3}\;\;}
\tag{3.2}$$

**Interpretation:** $k_H = \pi/3$ is a structural geometric factor from the $(2,3)$ winding's Hopf number combined with the $4\pi^2$ invariant normalization — **not a free parameter**, determined by the chain $Q_H = pq = 6$ and Ch 8's $\Lambda_{\text{vol}} = 4\pi^3$. For other torus knots, this coefficient would be different (e.g., (2,5): $Q_H = 10$, $k_H = \pi/5$).

The $\pi/3$ number raises an interesting question: is this value topologically fixed (tied to (p,q)=(2,3) forever) or is it a property of the electron's specific sector? For the derivation being ab-initio, we want this to come out as a pure number per sector, with no fitting. That's what the Hopf-invariant normalization achieves — $k_H$ is determined once $Q_H$ is specified.

**Alternative structural reading:** $k_H = 1$ as a dimensionless constant with the Hopf integral scaled differently. Under this reading, the Lagrangian is just $\mathcal{L}_\text{Hopf} = (1/2) A \cdot B$ and the integrated value on the electron at Golden Torus is $(1/2) \cdot 4\pi^2 \cdot 6 = 12\pi^2 \approx 118$, close to but not exactly $4\pi^3 \approx 124$. The discrepancy $4\pi^3 - 12\pi^2 = 4\pi^2(\pi - 3) \approx 5.58$ would then be a prediction to test.

**Judgment call [JC-H]:** $k_H = \pi/3$ (matches Ch 8 exactly) or $k_H = 1$ (simpler structural reading, small predicted deviation). Recommendation: **$k_H = \pi/3$ with provenance "fixed by Hopf-invariant / $Q_H = pq$ matching"** — this is zero-parameter in the sense that $Q_H$ is a topological integer and the $4\pi^2$ is a standard mathematical constant (Hopf map normalization).

---

## §4  Implementation — FFT-based inverse curl

On a periodic lattice, the gauge potential in Coulomb gauge is computable via FFT:

Given $\mathbf{B}(\mathbf{r})$, Fourier transform to get $\tilde{\mathbf{B}}(\mathbf{k})$. Then

$$\tilde{\mathbf{A}}(\mathbf{k}) \;=\; \frac{i\,\mathbf{k}\times\tilde{\mathbf{B}}(\mathbf{k})}{|\mathbf{k}|^2}$$

(with the zero mode $\mathbf{k} = 0$ set to zero to enforce $\int \mathbf{A}\,d^3r = 0$). Inverse FFT gives $\mathbf{A}(\mathbf{r})$. Then the Hopf density is $\mathcal{L}_\text{Hopf} = k_H \cdot \tfrac{1}{2}\,\mathbf{A}\cdot\mathbf{B}$.

Computational cost: one forward FFT + one inverse FFT per energy evaluation. $O(N^3 \log N)$ per step, comparable to the existing gradient operators.

**JAX compatibility:** `jax.numpy.fft.fftn` / `ifftn` are jit-compatible and autograd-compatible. The zero-mode fix requires a `jnp.where` on the frequencies, standard.

**The tetrahedral-lattice complication:** our grid uses Cartesian voxels with FCC-filter masking (alive nodes on A+B sublattices). Standard FFT assumes dense Cartesian. Approach: compute FFT on the full Cartesian grid treating dead sites as zero-field, then apply the alive mask to the final Hopf density. This slightly smears the potential computation but preserves the topological structure since the dead-mask nulls are a sparse projection of the alive field.

---

## §5  Failure modes and interpretations

- **Hopf term destabilizes the solver** (similar to `12_`'s reflection-term scale issue). The FFT-based Hopf density at the initial ansatz might be enormous. Reduce $k_H$ temporarily to diagnose, then re-examine the derivation for a missed factor.
- **Topology lost** during relaxation. The Hopf term might have the wrong sign or magnitude for the electron sector. Check $Q_H$ extraction from the relaxed field.
- **Minimum in R emerges but at wrong value.** Coefficient $k_H = \pi/3$ is off; the JC-H alternative $k_H = 1$ or yet another value might match Ch 8.
- **All three Ch 8 constraints hit simultaneously.** Phase-3 success.

---

## §6  Queue impact

Queue [17] was about promoting Op10 to continuum. It did that; result was insufficient. The natural extension is this Hopf term. If the validator succeeds with Op10 + reflection + Hopf all active, Phase-3 closes. If not, the next diagnostic targets which term's coefficient needs revision.

New queue item candidate: **[18] Hopf term's $k_H = \pi/3$ vs $k_H = 1$ adjudication** — resolved once validation succeeds with one or the other (or requires something else entirely).

---

## §7  Status

Ready for implementation. Single judgment call flagged (JC-H: coefficient), recommendation is $k_H = \pi/3$ per Ch 8 matching. No calibration — the matching uses $Q_H = pq$ as a topological integer, not a fit parameter.
