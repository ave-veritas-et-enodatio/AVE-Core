# 73 — Discrete K4-TLM scatter+connect + Cosserat LC-tank Hessian operator construction (reframe 4 of R7.1, §6.1 catastrophic-error carve-out invoked)

**Status:** 2026-04-25. **Reframe 4 of R7.1, §6.1 catastrophic-error carve-out explicitly invoked, on-record per Grant approval ("confirmed 6.1," 2026-04-25).** Mathematical-detail layer for the discrete-substrate operator construction that the previous reframes (1, 2, 3) successively approached but did not reach. No new pre-registration drafted in this doc; pre-registration follows after §1-§5 sign-off, per the same discipline as doc 72_ → reframe 3.

**Read after:** [doc 66_ §14 + §17.2](66_single_electron_first_pivot.md), [doc 67_ §17-§26](67_lc_coupling_reciprocity_audit.md), [doc 71_ §13-§15](71_multi_seed_eigenmode_sweep.md), [doc 72_ §1-§8](72_vacuum_impedance_design_space.md). [STAGE6_V4_HANDOFF.md §R7.1](.agents/handoffs/STAGE6_V4_HANDOFF.md) carries the original Round 7 R7.1 forecast.

**Skip §1's history if you only need the math:** §2-§5 are the operator-construction spec.

---

## 1. Why doc 73_ exists — §6.1 carve-out invoked

### 1.1 The reframe arc

Four reframes of R7.1 in this session:

| Reframe | Operator framing | Status | Caught by | Layer of error |
|---|---|---|---|---|
| 1 | Single-seed Hessian-of-W on Cosserat (forecast §R7.1) | Never registered | — | — |
| 2 (`P_phase6_eigensolver_multiseed`, commit `c69e79c`) | Multi-seed Hessian-of-W on joint (u, ω, V_inc, V_ref) | Retracted (A36) | External audit (Flag A V=0 cross-block; Flag B X4a shape correlation) | Operator over joint state misses sectoral structure |
| 3 (`P_phase6_helmholtz_eigenmode_sweep`, commit `675141e`) | Multi-seed block Helmholtz on (V, ω) joint with continuum graph Laplacian for V-block | Retracted (this doc) | Self-audit triggered by Grant pulse-check ("are you being an AVE engineer?") | V-block continuum-Laplacian approximation does not represent K4-TLM scatter+connect at finite N |
| 4 (this doc, no pred yet) | K4-TLM scatter+connect transmission eigenmode for V; Cosserat (u, ω) LC-tank Hessian-of-W; Op14 cross-coupling | Pending sign-off + pred drafting | (Doc 73_ aims to land at this layer correctly) | TBD — auditor leans (a) deeper layers genuinely needed; (b) reframe-loop anti-pattern risk |

Each reframe was substantive. Each layer was load-bearing. Pattern across A35 → A36 → A37: discipline tightening (production-retroactive → within-session-pre-implementation → within-session-during-implementation), but the same Rule 6 vulnerability pattern keeps surfacing one layer below where the previous round's design-space articulation looked.

### 1.2 §6.1 carve-out invocation, on-record

Doc 72_ §6.1 commitment language:

> *"Reframe 3 of R7.1; subsequent fresh-session run is committed to operator choice barring catastrophic methodology error. Pre-emptive operator changes before run are not allowed except for catastrophic errors (load-bearing physics error in operator construction itself)."*

Reframe-3 driver (`r7_helmholtz_eigenmode_sweep.py` at commit `675141e`) had a documented "engineering approximation": V-block built as weighted K4 graph Laplacian instead of K4-TLM scatter+connect. On smoke-test self-audit, this approximation was identified as **load-bearing** at finite N=32:

- Continuum-vs-discrete corrections at K4-TLM operating regime (N=32, mode scale ~10 cells): O((10/32)²) ≈ 10%.
- Eigenmode PASS tolerance: ω_Compton ± α ≈ 0.7%.
- Approximation error is ~14× the PASS tolerance — **comfortably outside the noise floor**.

Compounding factors:
- Op14 z-modulation creates rapidly-varying impedance at saturation gradients; continuum-vs-discrete corrections concentrate there.
- [Vol 1 Ch 8:49-50](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex#L49-L50) handoff comment: "K4-TLM exhausted (node-level Axiom 4 no-op for 4-port symmetric junctions per 32_ §10.2)" — discrete substrate has *qualitatively less expressive power* than continuum approximation. Mode classes hostable in graph-Laplacian eigsolve simply cannot exist in K4-TLM scatter+connect.
- Mode (III) under graph Laplacian could be misread as "Round 8 architectural rework" when actual cause is "continuum approximation finds modes that don't lift to K4-TLM."

These are exactly the conditions under which §6.1 specifies the carve-out applies. The operator construction has a load-bearing physics error that would invalidate any result regardless of what data the reframe-3 sweep produces.

**§6.1 carve-out invocation approved by Grant 2026-04-25 (on-record):**

> *Grant: "confirmed 6.1"*

This invocation goes on-record (here in §1.2 + r8.9 manual entry §17.1 A37 + §13.5l reframe note) so future audits can verify whether the §6.1 carve-out is being invoked legitimately or is becoming a routine escape valve from the "data first, methodology after" Rule 10 commitment. Per auditor recommendation: this is the FIRST §6.1 carve-out invocation; if a SECOND happens within Round 7, the discipline must be heavier (formal verification / dimensional analysis of operator structure before any code).

### 1.3 What this doc does NOT do

Per audit recommendation: **no new pre-registration drafted in this doc.** Doc 73_ articulates the discrete operator construction in mathematical detail; pre-registration follows after §1-§5 sign-off in a separate commit unit (matching the doc 72_ → reframe 3 discipline pattern that worked correctly at the §1.1-§1.4 conceptual layer but stopped short at the §3.1 operator-syntax layer).

---

## 2. K4-TLM scatter+connect eigenvalue formulation (operator part i)

### 2.1 The substrate dynamics in time-domain form

K4-TLM at each timestep `dt = dx/(c·√2)` (per [k4_tlm.py:144](../../src/ave/core/k4_tlm.py#L144)):

```
Scatter:  V_ref(t)[i, p] = Σ_q  S_pq(z_local(i; t)) · V_inc(t)[i, q]
Connect:  V_inc(t+dt)[i, p] = V_ref(t)[neighbor(i, p), opposite_port(p)]
```

with `S(z_local)` the 4×4 unitary scattering matrix per [k4_tlm.py:36-65](../../src/ave/core/k4_tlm.py#L36):

```
At z_local = 1:    S_ij = ½ - δ_ij                   (uniform vacuum)
At z_local ≠ 1:    S_ij = 2·y/y_total - δ_ij        where y = 1/z_local, y_total = Σ_j y_j
```

`neighbor(i, p)` is the neighbor of node `i` along port `p` per the K4 tetrahedral connectivity (PORTS = [(+1,+1,+1), (+1,-1,-1), (-1,+1,-1), (-1,-1,+1)] with sign flip for B sublattice). `opposite_port(p)` is the port-index correspondence at the neighbor (port `p` on a Type-A node maps to port `p` on the neighboring Type-B node by construction — see [k4_tlm.py:86-90](../../src/ave/core/k4_tlm.py#L86)).

### 2.2 Frequency-domain ansatz: standing-wave eigenmode at fixed ω

For a standing-wave eigenmode at fixed angular frequency ω, ansatz:

```
V_inc(t)[i, p] = V₀[i, p] · exp(i·ω·t)
V_ref(t)[i, p] = U₀[i, p] · exp(i·ω·t)
```

Substituting into the time-domain dynamics (with `z_local(i)` time-independent at the fixed seed Cosserat configuration):

```
Scatter:  U₀[i, p] = Σ_q  S_pq(z_local(i)) · V₀[i, q]                    (1)
Connect:  V₀[i, p] · exp(i·ω·dt) = U₀[neighbor(i, p), opposite_port(p)]    (2)
```

Equation (2) is the discrete-time advancement: at frequency ω, V_inc one timestep later equals V_inc now multiplied by `exp(i·ω·dt)`. Substituting (1) into (2):

```
V₀[i, p] · exp(i·ω·dt) = Σ_q  S_pq(z_local(neighbor(i, p))) · V₀[neighbor(i, p), q · "opposite_port"]
```

Rewriting in matrix-vector form, with `V₀` flattened over (site, port) into a single vector ψ ∈ ℂ^{N_active · 4}:

```
        T(z_local) · ψ = exp(i·ω·dt) · ψ                                   (3)
```

where `T(z_local) = C · S(z_local)` is the **scatter-then-connect transmission operator**. `S(z_local)` is the block-diagonal scattering matrix (one 4×4 block per active node). `C` is the **connect operator** — the sparse permutation matrix encoding `V_inc(t+dt)[i, p] ← V_ref(t)[neighbor(i, p), opposite_port(p)]`.

### 2.3 Eigenvalue problem

Equation (3) is a **unitary eigenvalue problem**. Eigenvalues lie on the unit circle in ℂ:

```
T(z_local) · ψ_n = λ_n · ψ_n         |λ_n| = 1         λ_n = exp(i·ω_n·dt)
```

Bound-state question: does any eigenvalue λ_n = exp(i·ω_C·dt) exist where ω_C = ω_Compton = 1 in engine natural units?

Equivalently, we want phases θ_n = arg(λ_n) = ω_n·dt with `ω_n = θ_n/dt`. For dt = 1/√2 in natural units (per [k4_tlm.py:144](../../src/ave/core/k4_tlm.py#L144) with c=1, dx=1), the target phase is **θ_target = ω_C · dt = 1/√2 ≈ 0.7071 rad**.

PASS criterion (refined for unitary eigenvalue): `|θ_n - 1/√2| < α/√2 ≈ 0.00516 rad`.

### 2.4 Operator construction (sparse, complex, NOT Hermitian)

Two sparse matrices for the V-block:

- **S(z_local)** ∈ ℂ^{4N_active × 4N_active}: block-diagonal, one 4×4 block per active node. Each 4×4 block is real-symmetric (since the unitary scattering matrix is real and symmetric for the AVE port structure), but sparse-block-diagonal structure encodes site-by-site impedance modulation.
- **C** ∈ ℂ^{4N_active × 4N_active}: sparse permutation matrix (pure ±1 entries, exactly one nonzero per row per column). Encodes the `neighbor(i, p)` connectivity.

Composite: `T = C · S` ∈ ℂ^{4N_active × 4N_active}. Sparse, NOT Hermitian (T is unitary; eigenvalues on unit circle, eigenvectors orthonormal in standard inner product).

**Key distinction from reframe-3 graph Laplacian:** the operator `T` is unitary with eigenvalues on the unit circle; the graph Laplacian has eigenvalues on the non-negative real axis. Different mathematical objects with different physical meaning. `T`'s eigenvalues directly encode time-domain frequencies via `λ = exp(i·ω·dt)`; graph Laplacian eigenvalues encode continuum spatial mode (k², not ω·dt).

### 2.5 Eigsolve method

`scipy.sparse.linalg.eigs` (general — not eigsh) in shift-invert mode at `sigma = exp(i · ω_C · dt) = exp(i / √2)`. For `k=10` eigenvalues nearest the target phase. T is sparse + unitary; shift-invert with explicit factorization of (T - σI) is tractable at N_active ≈ 8K nodes (N=32, half-and-half A/B sublattice with all-even/all-odd indexing): T dimension 32K × 32K, sparse with ~16 nonzeros per row.

**No LinearOperator / FD HVP needed for V-block.** T is materializable. Reframe-3's HVP issue is sector-specific to ω.

### 2.6 What stays unchanged from prior framings

A26 amplitude guard at step 0 (peak |ω| ∈ [0.85, 1.15]·0.3π for GT-family seeds), seed list (GT_corpus, F17K_cos_endpoint, F17K_s11_endpoint, vacuum_control), three-mode falsification structure (Mode I corpus-vindicated / Mode II engine-basin-elsewhere / Mode III no-eigenmode), Op14 z_local computation from seed Cosserat ω configuration via `(1 - A²)^(-1/4)` formula. All transferable.

---

## 3. Cosserat (u, ω) LC-tank Hessian-of-W formulation (operator part ii)

### 3.1 Why Hessian (not Helmholtz) for the Cosserat sector

Per [doc 66_ §17.2](66_single_electron_first_pivot.md) corpus framing: Cosserat carries **two LC tanks per node**:

- **Translational LC:** `u ↔ u_dot` (displacement ↔ velocity, 90° phase-locked in standing wave)
- **Rotational LC:** angular position ↔ ω (90° phase-locked)

These are **discrete-LC oscillators**, not continuum-wave systems. The eigenmode question for the Cosserat sector is "what are the LC oscillation frequencies of small perturbations around the seeded (u, ω) configuration?" — which is exactly **small-oscillation analysis around an equilibrium configuration**.

The mathematical operator for small-oscillation analysis is the **Hessian of W around the equilibrium**. This is correct AVE-native physics for the Cosserat sector, distinct from the (incorrect) Hessian-of-W-over-joint-state framing in retracted reframe 2.

The reframe-3 "Helmholtz" rhetorical framing for the Cosserat sector was a continuum dress on a discrete-LC substrate. Reframe 4 corrects this: K4-TLM is wave (continuum-limit-ish via scatter+connect with finite-dt corrections), Cosserat is discrete-LC (Hessian small-oscillation eigenvalue).

### 3.2 The Cosserat W functional

Per [`cosserat_field_3d.py:512`](../../src/ave/topological/cosserat_field_3d.py#L512) — Cosserat W density at each site is the sum of:

```
W = (2/3) G (tr ε)² + G ε_sym · ε_sym + G_c ε_antisym · ε_antisym + γ |∇ω|² + W_refl + W_hopf + W_chiral
```

where:
- ε_ij = ∂_i u_j - ε_{ijk} ω_k (Cosserat strain — couples u and ω)
- κ = ∇ω (Cosserat curvature — pure ω)
- W_refl = reflection penalty (saturation kernel)
- W_hopf = Hopf invariant density
- W_chiral = chirality-biased asymmetric saturation

The **Cosserat sector state** is ψ_cos = (u, ω) ∈ ℝ^{6 N_total} (3 components of u + 3 components of ω per node, defined on full N³ grid).

### 3.3 Equations of motion (Cosserat dynamics)

Per [`cosserat_field_3d.py:1228-1284`](../../src/ave/topological/cosserat_field_3d.py#L1228) Velocity-Verlet step:

```
ρ · ü = -∂W/∂u           ← translational equation of motion
I_ω · ω̈ = -∂W/∂ω         ← rotational equation of motion
```

where ρ (mass density per site) and I_ω (rotational inertia per site) are the engine's Cosserat mass parameters. Both default to 1.0 in natural units per [`cosserat_field_3d.py:758-771`](../../src/ave/topological/cosserat_field_3d.py#L758).

### 3.4 Small-oscillation linearization

For the standing-wave / bound-state question, expand around the seed configuration `(u_seed, ω_seed)`:

```
u(t) = u_seed + δu · exp(i·ω·t)
ω(t) = ω_seed + δω · exp(i·ω·t)
```

Substituting and linearizing the equations of motion (assuming `(u_seed, ω_seed)` is sufficiently close to a stationary point that linear analysis is valid — see §3.6 caveat):

```
-ω² · M_cos · δψ = -K_cos · δψ                                   (4)
```

where:
- `δψ = (δu, δω)ᵀ` — flattened perturbation state vector
- `M_cos` = block-diagonal `diag(ρ I_3·N, I_ω I_3·N)` — Cosserat mass matrix
- `K_cos = ∂²W/∂(u, ω)²|_{seed}` — Hessian of W at seed configuration

This is a **standard generalized symmetric eigenvalue problem** on (4):

```
        K_cos · δψ = ω² · M_cos · δψ                              (5)
```

Eigenvalues λ_n = ω_n². For real-symmetric K_cos and positive-definite M_cos, eigenvalues are real (positive for stable eigenmodes around equilibrium, negative for unstable directions).

### 3.5 Operator construction (sparse, real-symmetric)

`K_cos ∈ ℝ^{6 N_total × 6 N_total}`. Built via FD HVP on `engine.cos.energy_gradient()` per the existing reframe-3 driver pattern (`build_K_omega_op` extended to include u). Cross-blocks `∂²W/∂u∂ω` are nonzero per the ε_ij = ∂_i u_j - ε_{ijk} ω_k strain coupling — these encode the C↔L coupling within the Cosserat sector itself.

Mass matrix `M_cos = diag(ρ I_{3N}, I_ω I_{3N})` — sparse diagonal.

Eigsolve via `scipy.sparse.linalg.eigsh(K_cos, M=M_cos, k=20, which='SA')` — symmetric, mass-weighted, smallest-algebraic to find the lowest LC oscillation modes. Tolerance per pred PASS criterion: eigenvalue ω_n² where `|ω_n - ω_C| < α · ω_C ≈ 0.00731` rad/(natural time unit).

### 3.6 Caveat: seed need not be a stationary point of W

Linearization (5) is mathematically valid around ANY configuration, but eigenvalues of K_cos at non-stationary seeds include negative values (unstable directions). Physical interpretation as "LC oscillation frequencies" is rigorous only at stationary points; at non-stationary seeds, eigenvalues describe the local Hessian spectrum which may include both stable (positive) and unstable (negative) modes.

For the multi-seed sweep:
- GT_corpus seed: not a stationary point at coupled scale (per F17-K v3 (i)). Hessian spectrum at GT may have negative eigenvalues for the unstable directions.
- F17K endpoint seeds: were stationary points of either Cosserat-energy descent OR coupled-S₁₁ descent (per F17-K v2-v2). Hessian spectrum should be more stable.
- Interpretation rule: report ALL eigenvalues (positive and negative); the "did we find ω_C eigenmode" question applies to positive eigenvalues only. Negative eigenvalues are diagnostic about seed non-stationarity, not about (2,3) bound-state physics.

This is an honest framing: the bound-state eigenmode question is well-posed AT STATIONARY POINTS of W, and the four seeds represent four candidate stationary points (with varying degrees of evidence about whether they are actually stationary). Mode I/II/III adjudication reads off the spectrum at each seed.

---

## 4. Op14 cross-coupling at the seed (operator part iii)

### 4.1 What couples K4 and Cosserat sectors

[`k4_cosserat_coupling.py:329-376`](../../src/ave/topological/k4_cosserat_coupling.py#L329) — `_update_z_local_total` sets K4's `z_local_field` from the sum of K4 and Cosserat contributions to A²:

```
A²_total(x) = A²_K4(x) + A²_Cosserat(x)
A²_K4(x) = |V_inc|²(x) / V_SNAP²
A²_Cosserat(x) = ε²(x)/ε_yield² + κ²(x)/ω_yield²    (V=0 at seed → only Cosserat contributes)
z_local(x) = (1 - A²_total(x))^(-1/4)
```

At V=0 seed: A²_total = A²_Cosserat, so z_local at the seed is fully determined by ω_seed (and u_seed). This means S(z_local) depends on ω_seed, and the V-block T operator encodes the seed Cosserat configuration as the cavity geometry.

### 4.2 First-order coupling: V perturbation senses ω perturbation

For perturbations `δV_inc, δω` around the seed:

```
δz_local(x) ≈ (∂z_local/∂A²) · (∂A²_Cosserat/∂ω · δω + ∂A²_K4/∂V_inc · δV_inc)
```

At V=0 seed: `∂A²_K4/∂V_inc = 0` (multiplicative; vanishes at V_inc=0). So:

```
δz_local(x) = (∂z_local/∂A²) · (∂A²_Cosserat/∂ω) · δω
```

This δz_local then perturbs S(z_local), which perturbs T(z_local), which perturbs the V-block eigenvalue equation (3). The cross-coupling C_Vω of (block) operator is:

```
C_Vω = (∂T/∂z_local) · (∂z_local/∂ω)|_{seed}   ∈ ℂ^{4N_active × 6N_total}
```

### 4.3 Where the cross-block vanishes at V=0 seed

The cross-block `C_Vω · δω` acts on the V-block by perturbing T, which acts on the V-block eigenvector ψ_V. If at the seed `ψ_V = 0` (V=0), then `T · ψ_V = 0` regardless of δT. So the cross-block contribution to the joint eigenvalue equation **vanishes when ψ_V = 0**.

Equivalently: at V=0 seed, the joint operator is block-diagonal in the (V_block ⊕ Cos_block) basis. This is the **same V=0 decoupling result as reframe-3 doc 72_ §3.1.1**, restated for the discrete operator framework. Block decoupling means we can eigsolve V-block (eq. 3) and Cos-block (eq. 5) independently, and concatenate eigenvectors.

### 4.4 Full cross-coupled formulation (deferred to V≠0 seed work)

The cross-block C_Vω is generically nonzero at V≠0 seed (e.g., quadrature seed via `initialize_quadrature_2_3_eigenmode`). Then the joint eigenvalue problem is:

```
[ T(z_local)        C_Vω        ] [ ψ_V ]      [ exp(i·ω·dt) · I    0          ] [ ψ_V ]
[                                ] [     ] = ... [                               ] [     ]
[   C_ωV          K_cos          ] [ δψ_cos ]    [        0          ω² · M_cos ] [δψ_cos]
```

But this mixes UNITARY (V-block, eigenvalues on circle) and SYMMETRIC (Cos-block, eigenvalues on real axis) eigenvalue problems. The joint formulation is mathematically non-standard. **Not in scope for reframe 4 driver**; flagged as Round 8 territory if reframe 4 mode (III) result demands it.

For reframe 4: V=0 seed, block-decoupled, eigsolve V and Cos sectors independently. The "block" framing is preserved; cross-coupling is **structurally present but evaluates to zero at the seed**, exactly as §3.1.1 documented for the (incorrect-operator) reframe 3 case.

---

## 5. Joint operator dimension count + sparse structure (operator part iv)

### 5.1 Active site counts at N=32

K4-TLM active sites are all-even (i,j,k) ∪ all-odd (i,j,k) per [k4_tlm.py:205-206](../../src/ave/core/k4_tlm.py#L205):

```
N_active_K4 = (N/2)³ + (N/2)³ = 2 · (N/2)³
At N=32:    N_active_K4 = 2 · 16³ = 8192
```

Cosserat field lives on full grid:
```
N_active_Cos = N³ = 32768
```

### 5.2 V-block: T = C · S(z_local) ∈ ℂ^{32768 × 32768}

- 4 ports per active node × 8192 active nodes = **32,768 V-state DOFs**
- T is sparse: each row has O(1) nonzeros (one connect target per port × 4 ports = 4 nonzeros from C) modulated by 4×4 scattering block at each node. **~32K nonzeros total.**
- T is unitary, NOT Hermitian. eigs (general, not eigsh) with shift-invert at σ = exp(i / √2) for k=10 eigenvalues nearest the Compton phase.
- Memory: 32K × 32K complex sparse ≈ 1 MB. Trivial.
- eigsolve wall time estimate: ~1-10 seconds with ARPACK shift-invert.

### 5.3 Cos-block: K_cos ∈ ℝ^{196608 × 196608}

- 6 components per node × 32768 nodes = **196,608 Cos-state DOFs** (3 u + 3 ω)
- K_cos via FD HVP on `engine.cos.energy_gradient()` extended to include u-derivative. Sparse but not materialized; LinearOperator wrapper.
- M_cos = diag(ρ I, I_ω I) — sparse diagonal, 196K diagonal entries.
- eigsolve via `eigsh(K_cos, M=M_cos, k=20, which='SA', tol=1e-5, maxiter=2000)`.
- HVP cost per call: 2 × `engine.cos.energy_gradient()` (centered FD). At N=32 each gradient call is ~0.5-2 seconds (JAX-jit-compiled). Lanczos for k=20: ~100 HVPs ≈ 2-5 minutes per seed.

### 5.4 Total memory + compute at N=32

- V-block: ~1 MB sparse, ~10 s eigsolve
- Cos-block: 196K × 196K Hessian NOT materialized (LinearOperator HVP); ~5 min eigsolve via Lanczos
- Per seed: ~5-15 min wall time
- Four seeds: ~20-60 min wall time

**Tractable single fresh-session for the multi-seed sweep.** No need for cluster compute.

### 5.5 Engineering choices documented for reproducibility

| Choice | Reframe 4 spec | Reframe 3 (retracted) | Reframe 2 (retracted) |
|---|---|---|---|
| V-block operator | Discrete K4-TLM scatter+connect T = C·S | Continuum graph Laplacian | Hessian-of-W on V_inc |
| V-block eigenvalue type | Unitary (\|λ\|=1, λ=exp(iω·dt)) | Real-symmetric (λ=ω²) | Real-symmetric (λ=ω²) |
| V-block eigsolve | scipy.sparse.linalg.eigs with shift-invert at σ=exp(i/√2) | eigsh with which='SM' | eigsh with sigma shift-invert |
| Cos-block state | (u, ω) joint, 6N³ DOFs | ω only, 3N³ DOFs | (u, ω) included in joint state |
| Cos-block operator | Hessian-of-W on (u, ω) at seed | Hessian-of-W on ω at seed (rhetorically dressed as "Helmholtz") | Hessian-of-W over (u, ω, V_inc, V_ref) joint |
| Cross-coupling at V=0 seed | Vanishes (decoupled) | Vanishes (decoupled) | Vanishes silently (Flag A — eigsh returns Cosserat-only modes) |
| ω_Compton target | Phase θ = ω_C·dt = 1/√2 ≈ 0.7071 rad on unit circle (V) + λ = ω_C² = 1 (Cos) | λ = ω_C² = 1 (both blocks) | λ = ω_C² = 1 (joint) |

---

## 6. Reframe-counting commitment + reframe-5 escalation discipline

### 6.1 This is reframe 4, on-record

Reframe 4 of R7.1 in this session arc. §6.1 carve-out invoked once. Per auditor recommendation: a **second** §6.1 invocation in Round 7 must be paired with **heavier scaffolding before any further code**. Specifically:

- Formal verification / dimensional analysis on operator structure before code lands.
- Independent peer review of the operator-construction math (audit external to this session) before pred drafting.
- Explicit Grant approval at the operator-math-articulation layer (this doc 73_), not just at the §6.1 invocation layer.

This commitment goes in r8.9 §13.5l and §17.1 A37.

### 6.2 What constitutes catastrophic methodology error after doc 73_

Same as before: load-bearing physics error in operator construction itself that would invalidate any result regardless of what data the run produces. Specifically for reframe-4 operator:

- V-block: T = C · S(z_local) construction has a load-bearing error if C's connect permutation is wrong (incorrect tetrahedral neighbor mapping) or S's impedance modulation is wrong (incorrect functional form for z_local(A²)).
- Cos-block: K_cos construction has a load-bearing error if Hessian-of-W computation fails to produce a real-symmetric matrix at the seed (numerical asymmetry > 1e-6 in HVP).
- Cross-coupling: load-bearing error if the V=0 decoupling claim is wrong (i.e., if at V=0 the cross-block does NOT vanish, indicating the formulation has missed a term).

These are testable. Doc 73_ §7 + the next driver build in fresh session should include integrity checks for each.

### 6.3 What is NOT catastrophic (post-data-first per Rule 10)

- Eigenvalues at V-block don't include exp(i·ω_C·dt) phase, OR Cos-block doesn't include ω_C² eigenvalue: this is **mode (III) physics finding**, not methodology error. Per Rule 10, analyze data first.
- Numerical convergence issues with eigsh / eigs (no convergence after maxiter): methodology debug, retry with adjusted `tol` or `maxiter`. Not reframe.
- Negative eigenvalues at non-stationary seeds (per §3.6): expected, diagnostic, not error.
- Discrepancies between Mode result at different N (resolution sensitivity): informational, may be flagged for follow-up but doesn't invalidate the headline pred at the registered N=32.

---

## 7. r8.9 manual prep notes (other-agent scope)

For the next manual revision (r8.9), other-agent scope per Grant directive:

### 7.1 §13.5l reframe entry

Round 7 Stage 1 reframe 4 — discrete K4-TLM scatter+connect transmission eigenmode formulation per doc 73_ §2 + Cosserat (u, ω) LC-tank Hessian-of-W per doc 73_ §3 + Op14 cross-coupling that vanishes at V=0 seed per doc 73_ §4. Replaces retracted reframe 3 (`P_phase6_helmholtz_eigenmode_sweep`, commit `675141e`) per §6.1 catastrophic-error carve-out invocation.

**§6.1 carve-out invocation, on-record:** Grant explicit approval 2026-04-25 ("confirmed 6.1"). First §6.1 invocation in Round 7. A second invocation must be paired with heavier scaffolding (formal verification / independent operator-math review).

### 7.2 §16.1 commit row

`<this commit hash> — research(L3 Stage 6 Round 7): doc 73_ + reframe 4 — discrete K4-TLM scatter+connect + Cosserat LC-tank Hessian-of-W + Op14 cross-coupling; §6.1 catastrophic-error carve-out invoked on-record per Grant approval; P_phase6_helmholtz_eigenmode_sweep RETRACTING (no successor pred yet — pred follows post doc 73_ sign-off)`.

### 7.3 §16.3 doc index

Add doc 73_ entry: "73_discrete_k4_tlm_lctank_operator.md — Discrete K4-TLM scatter+connect + Cosserat LC-tank Hessian-of-W operator construction. Reframe 4 of R7.1 with §6.1 carve-out invoked on-record. No new pre-registration in this doc; pred follows after §1-§5 sign-off."

### 7.4 §17.1 A37 (NEW)

A37 — operator-implementation Rule 6 violation at fifth layer. Reframe-3 V-block operator chosen as continuum graph Laplacian when discrete K4-TLM scatter+connect is load-bearing. Caught by self-audit triggered by Grant pulse-check ("are you being an AVE engineer?"). §6.1 catastrophic-error carve-out invoked on-record per Grant approval; first invocation in Round 7. Family with A22 (inline operators duplicate canonical universals) + A30 (corpus-duality falsification) + A35 (basin-as-Stage-0 framing) + A36 (Hessian-of-W on joint state when sectoral structure is load-bearing). Meta-pattern: progressively deeper operator-construction layers requiring increasingly fine-grained methodology audit. Latency tightening (A35: production-retroactive → A36: within-session-pre-implementation → A37: within-session-during-implementation) is real progress; absolute count of layers is uncomfortable. Per auditor recommendation: a second §6.1 invocation in Round 7 must be paired with heavier scaffolding before any further code.

### 7.5 Critical-path table update

R7.1 status: reframe 4 in progress per doc 73_; pre-registration pending §1-§5 sign-off. R7.2 unaffected.

---

## 8. Open items deferred to fresh-session pred drafting

After Grant signs off on §1-§5:

1. **Draft `P_phase6_k4tlm_scattering_lctank` pre-registration** in `manuscript/predictions.yaml`. Specify V-block PASS criterion (eigenvalue phase within α/√2 of 1/√2 rad), Cos-block PASS criterion (eigenvalue within α·ω_C of ω_C² = 1), three-mode falsification with sector sub-reading. Frozen at commit time.
2. **Replace driver scaffold** `r7_helmholtz_eigenmode_sweep.py` (commit `675141e`, retracted) with `r7_k4tlm_scattering_lctank.py` per §2-§5 spec. Reuse `build_scattering_matrix(z_local)` from `k4_tlm.py:36-65`. Estimated ~150-250 LOC reusing existing engine code.
3. **Retract `P_phase6_helmholtz_eigenmode_sweep`** from frozen pred per Rule 12 (preserve body, retraction marker in name + notes prefix).
4. **Run the multi-seed sweep** at the four pre-registered seeds (GT_corpus, F17K_cos_endpoint, F17K_s11_endpoint, vacuum_control). Wall time ~20-60 min at N=32 per §5.4 estimate.
5. **Three-mode adjudication + doc 74_ result + adjudication.**

---

*Doc 73_ written 2026-04-25. Reframe 4 of R7.1 with §6.1 catastrophic-error carve-out invoked on-record per Grant approval ("confirmed 6.1"). Articulates discrete K4-TLM scatter+connect transmission eigenmode formulation (V-block, unitary eigenvalue problem) + Cosserat (u, ω) LC-tank Hessian-of-W formulation (Cos-block, real-symmetric eigenvalue problem) + Op14 cross-coupling that vanishes at V=0 seed (block decoupling). Cross-repo references intact: AVE-HOPF Smith chart (chiral_antenna_q_analysis.py:644), AVE-VirtualMedia three-regime Γ (generate_reflection_profile.py), AVE-Protein TDI canonical (protein_fold.py:260-326). No new pre-registration in this doc; pred follows after §1-§5 sign-off, matching the doc 72_ → reframe 3 discipline pattern. Reframe 5 escalation discipline: a second §6.1 invocation in Round 7 must be paired with formal verification / independent operator-math review before any further code.*
