# Phase 2 Wrap-up — Five Sub-problems from `08_` §9

**Status:** Phase 2 wrap-up. Resolves the five sub-problems flagged in [`08_discretization_design.md`](08_discretization_design.md) §9, producing a Phase-3-ready implementation spec.
**Prerequisites:** `00_` – `08_`.

**Summary of findings:** four of the five sub-problems resolve cleanly. Sub-problem 1 (tetrahedral-gradient coefficients) reveals an honest wrinkle: the nearest-neighbor tetrahedral gradient is only **first-order consistent**, not second-order as claimed in `08_` §3.2. The leading error term has a specific structure that cancels on a two-level stencil. Recommendations for both levels below; queue item [12] added for `08_` §3.2 correction.

---

## §1  Tetrahedral-gradient least-squares coefficients (→ correction to `08_` §3.2)

### 1.1  Setup

On the diamond substrate, each Type-A node has 4 tetrahedral neighbors at offsets

$$\mathbf{p}_0 = (+,+,+),\ \mathbf{p}_1 = (+,-,-),\ \mathbf{p}_2 = (-,+,-),\ \mathbf{p}_3 = (-,-,+)$$

(with unit components; each $|\mathbf{p}_\ell| = \sqrt{3}$). The goal: estimate the gradient $\nabla V$ at the A-site from the four differences $\Delta V_\ell = V(\mathbf{x} + \mathbf{p}_\ell) - V(\mathbf{x})$.

### 1.2  Least-squares coefficients

For a smooth field, Taylor expansion gives $\Delta V_\ell \approx \mathbf{p}_\ell \cdot \nabla V$. Over-determined system (4 equations, 3 unknowns). Normal-equations solution:

$$\nabla V = (P^\top P)^{-1} P^\top \Delta, \quad P = \begin{pmatrix} \mathbf{p}_0^\top \\ \vdots \\ \mathbf{p}_3^\top \end{pmatrix} \in \mathbb{R}^{4\times 3}$$

Direct computation yields $P^\top P = 4 I_3$, so $(P^\top P)^{-1} = \tfrac{1}{4} I_3$, giving the closed-form coefficients:

$$\boxed{\quad\partial_j V\big|_{\text{A-site}} \approx \frac{1}{4}\sum_{\ell=0}^{3} p_\ell^{\,j}\,\Delta V_\ell\quad}$$

For Type-B sites, substitute $\mathbf{p}_\ell \to -\mathbf{p}_\ell$ (equivalent to flipping the sign of the right-hand side).

Verification on a linear field $V = x$: $\Delta V_\ell = p_\ell^x$, giving $\partial_x V = \tfrac{1}{4}(1 + 1 + 1 + 1) = 1$ ✓. Exact on linear fields.

### 1.3  Honest consistency analysis — **amendment to `08_` §3.2**

Taylor expansion to second order:

$$\Delta V_\ell = \mathbf{p}_\ell \cdot \nabla V + \tfrac{1}{2}\,p_\ell^{\,k} p_\ell^{\,l}\,\partial_k\partial_l V + O(|\mathbf{p}|^3)$$

Substituting into the formula:

$$\partial_j V_{\text{discrete}} = \frac{1}{4}\sum_\ell p_\ell^{\,j} p_\ell^{\,k}\partial_k V + \frac{1}{8}\sum_\ell p_\ell^{\,j} p_\ell^{\,k} p_\ell^{\,l}\partial_k\partial_l V + O(\Delta x^2)$$

Using the identity $\sum_\ell p_\ell^{\,j} p_\ell^{\,k} = 4\delta_{jk}$ (diagonal), the first term gives $\partial_j V$ exactly. But the triple sum $\sum_\ell p_\ell^{\,j} p_\ell^{\,k} p_\ell^{\,l}$ is **not zero** — for $(j, k, l)$ all distinct it equals $4$ (by direct computation on the four tetrahedral vectors).

So the leading error is

$$\partial_j V_{\text{discrete}} - \partial_j V = \frac{1}{2}\sum_{k \neq j,\ l \neq j,\ k \neq l} \partial_k\partial_l V + O(\Delta x^2) = \partial_{k'}\partial_{l'} V + O(\Delta x^2)$$

where $(k', l')$ is the pair of axes distinct from $j$. **This is a first-order error, not second-order as claimed in `08_` §3.2.** The estimator is exact on linear fields but picks up a spurious contribution from mixed second partials.

### 1.4  Mitigation — symmetrized A+B combined estimator

The mixed-partial error has opposite sign on A-sites vs B-sites (because $\mathbf{p}_\ell \to -\mathbf{p}_\ell$ flips the sign of the triple product). Averaging the A-site estimator with a neighboring B-site estimator cancels the leading error, restoring second-order consistency. Concretely:

$$\partial_j V_{\text{2nd-order}} = \frac{1}{2}\left[\partial_j V_{\text{A}}^{(\text{formula})} + \partial_j V_{\text{B}}^{(\text{formula})}\right]$$

where both are evaluated at nominally the same location (e.g., via staggered mid-edge positioning analogous to Yee cells in FDTD). The A-B symmetrized operator is $O(\Delta x^2)$-consistent.

### 1.5  Recommendation for Phase 3

- **Baseline implementation (fast path):** nearest-neighbor A-site or B-site tetrahedral gradient. First-order consistent. Acceptable for initial convergence tests at $64^3$–$96^3$.
- **Production implementation:** A+B symmetrized estimator (§1.4). Second-order consistent. Required for publication-grade grid-convergence claims.

**Queue item [12] (new):** correct `08_` §3.2 claim of "second-order consistency" to "first-order for the naive tetrahedral-gradient estimator; second-order for the A+B symmetrized version." Add explicit derivation from this section.

---

## §2  Saturation-kernel choice — **decision: scalar-invariant**

From `02_` §5: apply $S(x; x_{\text{yield}})$ to either scalar invariants $|\varepsilon|^2 = \varepsilon_{ij}\varepsilon_{ij}$ and $|\kappa|^2 = \kappa_{ij}\kappa_{ij}$, or to each component individually.

**Decision: scalar-invariant.**

**Why:**

1. **Frame invariance.** The Cosserat Lagrangian is a rotational scalar. Applying the saturation kernel to scalar invariants preserves this structure. Per-component saturation breaks rotational symmetry — the kernel would depend on the choice of coordinate axes.
2. **Physical interpretation.** Axiom 4 says the field saturates when total strain magnitude approaches the Nyquist yield. "Total magnitude" is a scalar — $|\varepsilon|$ or $|\kappa|$. Per-component saturation would mean component-A saturates while component-B does not, even when their magnitudes are similar, which has no physical justification.
3. **Consistency with existing code.** [`faddeev_skyrme.py:138`](../../src/ave/topological/faddeev_skyrme.py#L138) applies `universal_saturation` to the scalar radial gradient $\partial_r\phi$. This is the 1D analog of scalar-invariant saturation. Extending to 3D: $|\kappa|$ is the scalar invariant.
4. **Computational cost.** Scalar-invariant is cheaper — one `sqrt` and one `saturation` call per lattice site, vs 9 (tensor-component) or 6 (symmetric-tensor-component) calls per site.

**Implementation:** at each alive node, compute $|\kappa|^2 = \kappa_{ij}\kappa_{ij}$ (sum over all 9 components), then apply `universal_saturation(sqrt(|kappa|^2), pi/ell_node)` to obtain the scalar multiplier. Multiply the tensor $\kappa$ by this scalar before computing the energy contribution $W_\kappa^{\text{sat}} = \gamma\,(S\,|\kappa|)^2$.

Revisit per-component only if Phase-3 convergence tests reveal spurious isotropy breaking (e.g., the relaxed electron soliton has unphysical oblate/prolate distortion aligned with coordinate axes).

---

## §3  $c$-extraction operator — **decision: Op11 curl integration primary, preimage-counting as sanity check**

Two candidate operators for reading $c$ from the relaxed field:

**(a) Op11 topological-curl integration.** Compute the circulation of a "phase gradient" field around canonical closed contours on the shell. For an SU(2) field $U = \exp(i\boldsymbol{\sigma}\cdot\boldsymbol{\omega}/2)$, the relevant phase is the azimuthal angle of the Hopf-projected $\hat{\mathbf{n}}$. The contour integral on the major cycle gives $w_1$; on the meridian cycle gives $w_2$. Crossing count recovered via $c = q$ under the $(2, q)$ torus-knot convention (where $q$ is the dominant winding contributor for the $(2, q)$ ladder).

Implementation: use [`universal_topological_curl`](../../src/ave/core/universal_operators.py#L640) on the gradient of $\hat{\mathbf{n}}$ on the Clifford shell, integrate around the two canonical curves.

**(b) Preimage counting.** Numerically find the preimage set $\hat{\mathbf{n}}^{-1}(\hat{\mathbf{n}}_0)$ for generic $\hat{\mathbf{n}}_0 \in S^2$ (e.g., randomly chosen), and count how the preimage curve threads a reference surface (the equatorial disc of the electron's bounding torus). The threading count is $c$.

**Decision: (a) primary, (b) as sanity check.**

- (a) is simpler to implement, uses an existing universal operator, and is robust to field noise (integrates over a full contour, smoothing out high-frequency artifacts).
- (b) requires finding level-set curves numerically, which is brittle near singularities or at low-amplitude regions. Useful as a cross-check when (a)'s integral is ambiguous (e.g., at boundary-ambiguous shell radii).

**Implementation sketch:**

```python
def extract_crossing_count(u_field, w_field, alive_mask, shell_radii=(R, r)):
    # Project SU(2) → S² to get n̂
    n_hat = project_SU2_to_S2(w_field)
    # Extract azimuthal phase on the Clifford shell at (R, r)
    phase = extract_azimuthal_phase_on_shell(n_hat, shell_radii)
    # Contour-integrate the phase gradient around both cycles
    w1 = integrate_phase_gradient_on_cycle(phase, cycle='major')
    w2 = integrate_phase_gradient_on_cycle(phase, cycle='minor')
    # AVE convention: c = q from the (2, q) ladder
    return max(abs(w1), abs(w2))
```

Expected: $c = 3$ for the electron. Acceptance tolerance: exact integer match (no fractional crossings expected; the contour integral is topologically quantized).

---

## §4  Initial-guess shell radii — **decision: dual-run protocol (exact + perturbed)**

**Decision:** run the Phase-3 solver from two independent initial conditions:

1. **Exact Golden Torus initial guess:** $(R_0, r_0) = (\varphi/2, (\varphi - 1)/2) \approx (0.809, 0.309)$. Fast convergence expected; verifies the Lagrangian has a stationary point at the analytical prediction.
2. **Perturbed off-Golden initial guess:** $(R_0, r_0) = (1.0, 0.4)$, or similar off-Golden starting point. Slower convergence expected; verifies the Lagrangian's dynamics **selects** the Golden Torus rather than trivially reading it from the initialization.

Both runs should converge to the same final $(R, r)$. If only the exact starting point converges, the Lagrangian is not genuinely selecting the Golden Torus — which is a failure-to-derive result that must be surfaced, not hidden.

**Convergence criterion:** $\|(R, r) - (\varphi/2, (\varphi - 1)/2)\|_\infty < 10^{-3}$ (per §5 tolerances).

The perturbed-run validation is the physics-meaningful test. The exact-run validation is a sanity check. **Both** are Phase-3 acceptance requirements.

---

## §5  Validation tolerances — **decision: fixed before Phase-3 runs begin**

Per the scientific-workflow discipline stated in `00_` (predictions before validation), we commit to these tolerances in advance:

| Quantity | Prediction | Tolerance | Rationale |
|---|---|---|---|
| Major radius $R$ | $\varphi/2 \approx 0.80902$ | $\|R - \varphi/2\| < 10^{-3}$ | Three significant figures; accessible at $96^3$ grid |
| Minor radius $r$ | $(\varphi-1)/2 \approx 0.30902$ | $\|r - (\varphi-1)/2\| < 10^{-3}$ | Same |
| Crossing count $c$ | $3$ | exact integer $= 3$ | Topologically quantized; no tolerance needed |
| $\alpha^{-1}$ | $4\pi^3 + \pi^2 + \pi \approx 137.0363$ | $\|\alpha^{-1}_\text{extracted} - 137.0363\| < 10^{-3}$ | Relative error $\sim 10^{-5}$, consistent with $R,r$ tolerance |
| Total energy $\mathcal{E}_\text{ground}$ | same as $\alpha^{-1}$ (with $\gamma = 1$) | $|\mathcal{E} - 137.0363| < 10^{-3}$ | Same |
| Constraint residuals | $(R{-}r{-}\tfrac12, Rr{-}\tfrac14, d{-}1)$ all zero | $\|\text{residuals}\|_\infty < 10^{-3}$ | Must jointly hold |

**Failure modes and their interpretations:**

- $c \neq 3$: the initial-condition topology was not preserved during gradient descent. Step-size too large, or saturation kernel failing. Phase-3 bug.
- $(R, r)$ far from Golden Torus but $c = 3$ holds: the Lagrangian does not select the Golden Torus. **This is a falsification of Phase-1 theory** — would require revision of `02_`/`03_` arguments about the three Ch 8 constraints.
- $\alpha^{-1}$ off but $(R, r)$ correct: the multipole-Q extraction is buggy, or the $\gamma = 1$ pinning is wrong. Revisit `04_` pinning check.
- Constraint residuals fail: the three Ch 8 constraints aren't being reproduced by the solver. Revisit `03_` §4 derivations against numerical data.

Each failure mode points at a specific doc for revision. This is the "predictions-before-validation" discipline working as intended.

---

## §6  Queue updates

**Item [12] (new):** Correct `08_` §3.2 "second-order consistency" claim.
- **File:** [`08_discretization_design.md`](08_discretization_design.md) §3.2
- **Change:** Replace the "second-order consistency" phrasing with the honest statement: the naive nearest-neighbor tetrahedral gradient is **first-order consistent** (error proportional to mixed second partials $\partial_k\partial_l V$ for distinct $k, l \neq j$). Second-order consistency requires the A+B symmetrized estimator of §1.4 above.
- **Why:** `08_` overclaimed. Surfaced in §1.3 of this doc. Leaving the claim would mislead Phase-3 implementation efforts about expected convergence rates.
- **Status:** queued.

---

## §7  Status

All five Phase-2 wrap-up sub-problems resolved. Key decisions:

| Sub-problem | Decision |
|---|---|
| Gradient coefficients | Closed-form $\partial_j V \approx \tfrac{1}{4}\sum_\ell p_\ell^{\,j}\,\Delta V_\ell$; baseline first-order, A+B-symmetrized second-order for production |
| Saturation kernel | Scalar-invariant (not per-component) |
| $c$-extraction | Op11 curl integration primary; preimage-counting as sanity check |
| Initial guess | Dual run — exact Golden Torus + perturbed off-Golden |
| Validation tolerances | $10^{-3}$ for real-valued quantities; exact integer for $c$; committed before Phase-3 runs |

Queue item [12] added (`08_` §3.2 correction).

**Phase 2 is closed.** Phase 3 (actual coding of `src/ave/topological/cosserat_field_3d.py`) can begin.
