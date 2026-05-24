# Phase 2 — Discretization Design for the Cosserat Field on K4

**Status:** Phase 2 entry. Translates the continuum Lagrangian $\mathcal{L}_{\text{AVE}}$ from `02_` §6 into a discrete computational framework on the K4 substrate, suitable for Phase-3 numerical implementation.
**Prerequisites:** `00_` – `07_`; [`src/ave/core/k4_tlm.py`](../../src/ave/core/k4_tlm.py); [`src/ave/core/universal_operators.py`](../../src/ave/core/universal_operators.py).

The existing AVE K4-TLM solver has already solved the substrate discretization problem for the translational ($\mathbf{u}$) sector. Phase 2 extends that pattern to the Cosserat microrotation ($\boldsymbol{\omega}$) sector, producing a unified discrete field representation for $\mathcal{L}_{\text{AVE}}$.

---

## §1  Design goal

Produce a discrete computational representation of the Cosserat field $(\mathbf{u}(\mathbf{r}), \boldsymbol{\omega}(\mathbf{r}))$ on the K4 diamond substrate that:

1. **Faithfully encodes K4 topology** (4-coordinate tetrahedral connectivity, diamond lattice structure).
2. **Admits efficient vectorized implementation** on a Cartesian backing store (NumPy / JAX / PyTorch compatible).
3. **Supports discrete operators for the kinematic tensors** $\varepsilon_{ij}$ (strain) and $\kappa_{ij}$ (curvature-twist) of `02_` §2.
4. **Applies the Axiom-4 saturation kernel** consistently with existing universal-operator conventions.
5. **Imposes the $c = 3$ topological boundary condition** (`07_` §3) as a numerical constraint on the electron ground state.
6. **Fits within the Phase-3 compute budget** (MacBook Pro M4, 32 GB unified memory — `00_` §8).

---

## §2  The existing K4-TLM pattern

[`src/ave/core/k4_tlm.py`](../../src/ave/core/k4_tlm.py) implements the K4 substrate dynamics for the translational sector via a specific design pattern. It is worth naming because Phase 2 follows it directly.

**Pattern: Cartesian-grid-with-FCC-filter.**

- **Storage.** A regular Cartesian array of shape $(n_x, n_y, n_z)$.
- **FCC filter.** Only lattice sites satisfying $(x + y + z) \bmod 2 = 0$ are "alive" — they carry field data. The other sites are structural padding for stencil alignment.
- **Bipartite sublattices.** Alive sites split into Type A (e.g. $(x+y+z)/2$ even) and Type B (odd). Type A connects to Type B via four tetrahedral offset vectors:

  $$
  \begin{aligned}
  \mathbf{p}_0 &= (+1, +1, +1) &\mathbf{p}_1 &= (+1, -1, -1) \\
  \mathbf{p}_2 &= (-1, +1, -1) &\mathbf{p}_3 &= (-1, -1, +1)
  \end{aligned}
  $$

  Type B connects to Type A via the negatives $-\mathbf{p}_i$. This reproduces the diamond (sp³ tetrahedral) coordination of Axiom 1 exactly without maintaining an adjacency list.
- **Operations vectorized.** Array-wide reads and writes via NumPy slicing of $(i, j, k, i{\pm}1, j{\pm}1, k{\pm}1)$ neighborhoods, with the FCC parity mask applied as a boolean filter.
- **Dispersion.** $\Delta t = \Delta x / (c_0 \sqrt{2})$ for stability on the diamond geometry.

**Why this pattern works well:**

- Native GPU vectorization via the Cartesian backing.
- No graph-traversal bookkeeping; neighbor lookups are constant-offset indices.
- Diamond topology is structurally exact — every alive node has exactly 4 tetrahedral neighbors, no exceptions at interior.
- Compatible with standard ML stencil libraries (JAX `jax.lax.conv`, PyTorch `Conv3d`).
- Scales cleanly; the only overhead vs plain cubic FDTD is the FCC mask (which is ~half-occupied).

---

## §3  Extending the pattern to the Cosserat field

The translational sector of `k4_tlm.py` uses scalar/vector voltages on 4-port junctions (Op5 scattering matrix). The Cosserat field needs more: 6 degrees of freedom per alive node — the 3 components of $\mathbf{u}$ and the 3 components of $\boldsymbol{\omega}$.

### 3.1 Field storage

Extend the Cartesian backing to carry the full Cosserat field:

```
u_field: np.ndarray shape (n_x, n_y, n_z, 3)  # translational displacement
w_field: np.ndarray shape (n_x, n_y, n_z, 3)  # Cosserat microrotation
alive_mask: np.ndarray shape (n_x, n_y, n_z) bool  # FCC parity filter
```

At each alive site, store the 6 Cosserat DOFs. At dead sites, the field values are undefined and masked out of all operations. For float32, a $128^3$ domain stores $\approx 100$ MB per field — comfortable on the M4 32 GB budget.

### 3.2 Discrete kinematic tensors

From `02_` §2:

$$\varepsilon_{ij} = \partial_j u_i - \epsilon_{ijk}\,\omega_k, \qquad \kappa_{ij} = \partial_j \omega_i$$

Spatial derivatives use the K4 tetrahedral neighborhood. For the derivative $\partial_j u_i$ at a Type A node:

$$(\partial_j u_i)|_{\text{A-site}} \approx \frac{1}{4}\sum_{\ell=0}^{3}\,\frac{u_i(\mathbf{x} + \mathbf{p}_\ell) - u_i(\mathbf{x})}{|\mathbf{p}_\ell|}\,\hat{\mathbf{p}}_\ell^{(j)}$$

where $\hat{\mathbf{p}}_\ell^{(j)}$ is the $j$-th component of the normalized tetrahedral offset vector. This is the K4 analogue of the central-difference gradient on a cubic grid. Type B nodes use $-\mathbf{p}_\ell$ instead.

The factor $1/4$ averages over the four tetrahedral bonds. Dimensional consistency: for each bond, $(\Delta u)/|\mathbf{p}_\ell|$ is the directional derivative along the bond; projecting onto the Cartesian $j$-axis via $\hat{\mathbf{p}}_\ell^{(j)}$ and averaging the four bonds gives an unbiased estimator of $\partial_j u_i$ on the diamond lattice. This is equivalent to solving a 4-direction least-squares problem for the gradient vector, which has closed-form coefficients for the tetrahedral offsets.

Same formula applies for $\partial_j \omega_i$ to get $\kappa_{ij}$.

### 3.3 Axiom-4 saturation kernel

Apply `universal_saturation` (from [`universal_operators.py:57`](../../src/ave/core/universal_operators.py#L57)) to the scalar invariants of $\varepsilon$ and $\kappa$:

- $|\varepsilon|^2 := \varepsilon_{ij}\varepsilon_{ij}$ with yield $1$ (`02_` §5)
- $|\kappa|^2 := \kappa_{ij}\kappa_{ij}$ with yield $\pi/\ell_{\text{node}} = \pi$ in natural units (`02_` §5)

Compute the scalar saturation factor at each alive node, then apply it to the tensor before computing the energy contribution. This is the **scalar-invariant** saturation scheme preferred in `02_` §5. For the electron ground state this should suffice; if Phase-3 convergence tests reveal artifacts (e.g., spurious symmetry breaking), we revisit with per-component saturation.

### 3.4 Euler-Lagrange update

For the static ground-state problem (`02_` §10, equations 10.1 + 10.2 with $\ddot{\mathbf{u}} = \ddot{\boldsymbol{\omega}} = 0$), we solve iteratively via gradient descent on the discretized energy functional:

$$\mathbf{u}^{(n+1)} = \mathbf{u}^{(n)} - \eta\,\frac{\partial \mathcal{E}}{\partial \mathbf{u}}, \qquad \boldsymbol{\omega}^{(n+1)} = \boldsymbol{\omega}^{(n)} - \eta\,\frac{\partial \mathcal{E}}{\partial \boldsymbol{\omega}}$$

with $\eta$ a learning rate chosen by backtracking line search or an Adam-style adaptive scheme. Energy computation uses the discretized $W^{\text{sat}}$ of `02_` §5 summed over alive nodes. Convergence is declared when $\|\nabla \mathcal{E}\|_\infty < $ tolerance (e.g., $10^{-8}$).

For the **dynamic problem** (Phase-3 extensions, time-resolved Cosserat dynamics), the Euler-Lagrange equations become the full (10.1) + (10.2), time-stepped with the K4 dispersion $\Delta t = \Delta x / (c_0 \sqrt{2})$. This is a second-phase implementation — start with static.

---

## §4  The three strategies, reconsidered

Before examining implementation, re-evaluate the three discretization strategies from `00_` §6 in light of the K4-TLM pattern.

| Strategy | Verdict |
|---|---|
| **(A) Direct K4 graph discretization.** Explicit adjacency list, graph-traversal operators. | **Rejected.** Vectorization-hostile. No advantage over the Cartesian-with-FCC-filter pattern. Would require reimplementing stencil operators that already exist in NumPy/JAX as array operations. |
| **(B) Cubic voxelization, K4 as coarse substrate.** K4 at a subset of voxel centers; intermediate voxels interpolate. | **Rejected** for the ground-state problem. Adds interpolation artifacts; $\ell_{\text{node}}$ becomes a multi-voxel scale, reducing resolution. Possibly useful for Phase-3 dynamic simulations with long propagation, but unnecessary here. |
| **(B′) Cartesian-with-FCC-filter (new designation).** The existing K4-TLM pattern. FCC parity mask, tetrahedral offset neighborhoods, vectorized Cartesian storage. | **Recommended.** Matches existing AVE code conventions, vectorizes natively, encodes K4 topology exactly. |
| **(C) Hybrid with refined stencils at defect cores.** Uniform (B′) plus local mesh refinement near the electron core. | **Phase-3 fallback** if (B′) shows convergence issues at the Nyquist-scale defect core. Not needed initially. |

**Adoption: (B′) Cartesian-with-FCC-filter.** This is structurally the same pattern as [`k4_tlm.py`](../../src/ave/core/k4_tlm.py) — extended from 1 field (voltage) to 6 DOFs (translation + microrotation) per alive node.

---

## §5  Topological boundary condition: imposing $c = 3$ numerically

Per `07_` §3, the electron topological sector is characterized by a single scalar: $c = 3$ crossings. Imposing this numerically is more subtle than a simple Dirichlet condition.

### 5.1 Initialization with embedded $c = 3$ structure

Start the solver with a field configuration that already carries $c = 3$. A natural choice (adapting the Sutcliffe Hopfion ansatz from B11, but as initial condition, not final):

$$\boldsymbol{\omega}_0(\mathbf{r}) = \Omega_{\max} \cdot \Phi(\rho)\,\hat{\mathbf{e}}(\theta, \psi),\qquad \hat{\mathbf{e}} = (\sin\phi_\star\cos\Theta, \sin\phi_\star\sin\Theta, \cos\phi_\star),\qquad \Theta = 2\varphi + 3\psi$$

with $\rho, \theta, \varphi, \psi$ toroidal-shell coordinates centered on an initial guess at the Golden Torus. $\Phi(\rho)$ is a localizing radial profile. $\Omega_{\max} = \pi$ per `03_` §4.1.

The combined phase $\Theta = 2\varphi + 3\psi$ generates preimages that are $(2, 3)$ torus-knot curves — carrying $c = 3$.

**Why this initialization is consistent with `07_`:** the choice of "combined phase" vs "factorized phase" is an ansatz, not a topology. $\Theta = 2\varphi + 3\psi$ gives $c = 3$ unambiguously; it's also the simplest field to initialize and is the convention the Sutcliffe-2007 numerical literature uses.

### 5.2 Conservation during gradient descent

Gradient descent preserves the crossing number if the energy functional is non-singular (no tearing of the field) and the step size is small enough. The saturation kernel prevents singular gradients (enforces the Nyquist cap), so the $c$-preserving property should hold in practice. **Verification** during Phase 3: recompute $c$ from the relaxed field using the Op11 (topological curl) integral + preimage-counting, and confirm $c = 3$ is preserved throughout.

### 5.3 Far-field decay

As $|\mathbf{r}| \to \infty$, impose $\boldsymbol{\omega} \to 0$ (and thus $U \to \mathbb{1}$). Numerically: Dirichlet-zero boundary conditions at the domain edge, with the domain large enough that the soliton's tail decays below numerical noise before reaching the boundary. For an M4 budget of $128^3$ with $\ell_{\text{node}} = 1$, the soliton core ($R \approx \varphi/2 \approx 0.8$) plus tail (decay scale $\sim$ several $\ell_{\text{node}}$) should comfortably fit in the central $\sim 30$–$50$ lattice sites, leaving 50+ sites of decay buffer to the edge.

### 5.4 Absorbing boundary (optional)

For time-dependent Phase-3 dynamics, a PML (perfectly matched layer) at the domain edges may be needed. `k4_tlm.py` already has `pml_thickness` support — inherit.

---

## §6  Convergence analysis requirements

Before Phase-3 production runs, we need to establish:

1. **Grid independence.** Run the same problem at $48^3$, $64^3$, $96^3$, $128^3$. Verify that the extracted Golden-Torus radii $(R, r)$, the ground-state energy $\mathcal{E}$, and the crossing count $c$ all converge to grid-independent limits. Expected: second-order convergence in $\Delta x$ for the tensor-gradient operators.
2. **Operator consistency.** The discrete Cosserat strain and curvature operators (§3.2) should reproduce the continuum values on smooth test fields. Unit tests: apply the discrete operators to analytic smooth fields (e.g., rigid rotation, uniform shear) and verify the known continuum values are recovered at the alive nodes.
3. **Energy-stability.** Gradient descent should monotonically decrease $\mathcal{E}$. Step-size instability should trigger learning-rate reduction via backtracking.
4. **Topology preservation.** $c$ measured from the evolving field should remain 3 throughout gradient descent; any flip in $c$ indicates a numerical tear requiring time-step reduction.

---

## §7  Implementation plan — connection to existing AVE code

New module: **`src/ave/topological/cosserat_field_3d.py`** (proposed path per `02_` §12). Not yet written.

Inherits / extends:

- **`k4_tlm.py`**: use `K4Lattice3D.__init__` pattern for Cartesian-with-FCC-filter setup. Reuse the tetrahedral offset vectors $\mathbf{p}_0 \ldots \mathbf{p}_3$, the alive-node mask construction, and the PML scaffolding.
- **`universal_operators.py`**: use `universal_saturation` (Op2) for kernel application; use `universal_topological_curl` (Op11) for diagnostic extraction of the winding integrals; use `universal_junction_projection_loss` (Op10) as the validation target for $c = 3$ at Clifford-torus crossings.
- **`src/ave/core/constants.py`**: reuse `C_0`, `Z_0`, `V_SNAP`, `V_YIELD` conventions; inherit the pinning $G = G_c = \gamma = 1$ in natural units (`04_` §6).

New content:

- Cosserat strain + curvature operators (§3.2).
- Saturated energy functional (§3.3).
- Gradient-descent update loop (§3.4).
- Topological-boundary-condition initializer (§5.1).
- Diagnostics: extract $(R, r)$, $c$, multipole Q-factor decomposition from relaxed field.

Length estimate: **500–800 LOC** for the solver core, plus a similar amount for tests and diagnostics. Moderate but bounded.

---

## §8  Compute budget confirmation

From `00_` §8:

- **$64^3$ voxels**: 6 MB/field snapshot. Single iteration on M4 CPU: ~seconds. Full convergence: minutes. Appropriate for initial convergence experiments.
- **$96^3$**: 20 MB/snapshot. Comfortable working resolution.
- **$128^3$**: 50 MB/snapshot. Fits. Full iteration history (if retained for visualization) can reach $\sim 10$ GB — watch memory carefully or checkpoint intermittently.

**Numerical backends (ranked):**

1. **NumPy + Numba** (CPU, JIT). Reliable, debuggable, no Apple-Silicon tooling surprises. First-pass implementation target.
2. **JAX (`jax_platform_name = 'metal'`)**. GPU acceleration where supported; CPU fallback elsewhere. Add after NumPy implementation is validated.
3. **PyTorch MPS**. Only if JAX-Metal hits walls.

---

## §9  Open sub-problems for Phase 2 wrap-up

1. **Tetrahedral-gradient least-squares coefficients (§3.2).** Derive the closed-form coefficients for the $(\partial_j V_i)$ operator on the diamond lattice and verify second-order consistency on smooth test fields. A short standalone derivation, $\sim$2 pages of algebra.
2. **Saturation-kernel choice (§3.3).** Scalar-invariant (default) vs per-component for $\kappa$. Smooth choice on symmetry grounds is scalar-invariant; the alternative is cheap to add if it becomes necessary.
3. **$c$-extraction operator (§5.2).** Define a numerical operator that reads $c$ from the field — either via Op11 topological-curl integration on canonical contours or via S²-preimage-intersection counting. Either suffices; pick based on numerical robustness.
4. **Initial-guess shell radii (§5.1).** Start at $(R, r) = (\varphi/2, (\varphi - 1)/2)$ exactly (the Ch 8 prediction), or perturb by 10–20% to confirm convergence from an off-Golden starting point? Both, probably — the off-Golden convergence check validates the Lagrangian selects the Golden Torus rather than trivially reading it off the initialization.
5. **Validation tolerances.** Fix the exact numerical tolerances for "converged" Golden-Torus recovery, $c = 3$ preservation, and $\alpha^{-1}$ reproduction. Tentative: $|R - \varphi/2| < 10^{-3}$, $c = 3$ exactly, $|\alpha^{-1} - (4\pi^3 + \pi^2 + \pi)| < 10^{-3}$.

---

## §10  Status

Phase 2 entry doc established. The Cartesian-with-FCC-filter pattern (inherited from `k4_tlm.py`) is adopted. Cosserat extension designed. Compute budget confirmed.

**Phase-2 wrap-up remaining:**

- The five sub-problems of §9 — mostly short standalone derivations and design decisions.
- A solver-architecture mini-doc (`09_solver_architecture.md`) fleshing out §7 at publication rigor, if desired before coding.

**Phase-3 entry** (actual coding of `cosserat_field_3d.py`) proceeds once §9 items are addressed or accepted as Phase-3 discovery tasks.
