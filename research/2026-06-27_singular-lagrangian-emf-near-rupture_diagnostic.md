# DIAGNOSTIC — The Lagrangian-EMF coupling is structurally singular near rupture (∂L/∂V² ∝ 1/S_ε → ∞)

**Date:** 2026-06-27 · **Lane:** implementer · **Branch:** `analysis/stabilized-electron-retract-salvage`
**Status:** Diagnostic note (CONSISTENCY-class)
**Scope:** Coupled K4↔Cosserat lattice — the autograd Lagrangian-EMF reciprocal channel
**Class (consistency-vs-emergence):** **CONSISTENCY** — this records a structural property of the engine's
own discretized operator; it is brought into the record so the off-by-default flag is grounded in a
*substrate-native* reason, not a tuning convenience. No CODATA input, no manifestation/identity/emergence
target is asserted. **No new `clm-` ID is minted here** (deferred to Grant per consistency-vs-emergence).

**Provenance:** salvaged from the retracted result
[`research/2026-06-26_stabilized-electron-feedback-loop_result.md`](2026-06-26_stabilized-electron-feedback-loop_result.md)
(§2). That result is retracted as an artifact on three axes (energy unbounded / α-in-α-out tautology /
not reproducible — see its retraction header). The §2 singularity analysis is the *one* finding not
contaminated by those axes; it is a structural property of the operator stencil, independent of the
parameter sweep, the damping crutch, and the α-injections. It is extracted here standalone.

**Cross-ref:** [`research/2026-06-21_emf-lenz-sign-correction_result.md`](2026-06-21_emf-lenz-sign-correction_result.md)
(the EMF source sign `−2` fix; consistency-class engine-correctness, off-by-default unchanged).

---

## 0. TL;DR

The autograd Lagrangian-EMF reciprocal channel (`use_lagrangian_emf_coupling`, OFF by default) is
**structurally singular** as the substrate approaches the electric-sector rupture boundary
($S_\varepsilon \to 0$, i.e. $V \to V_{\text{snap}}$):

$$\frac{\partial L_c}{\partial V^2} \;\propto\; \frac{1}{S_\varepsilon} \;\xrightarrow[S_\varepsilon \to 0]{}\; \infty .$$

This is **why the channel must stay off-by-default near rupture** — a substrate-native structural property of
the discretized asymmetric-reflection operator, **not** a script artifact and **not** a numerical-tolerance
issue. The engine's own code already encodes this conclusion at two independent sites
(`k4_cosserat_coupling.py:269` "both signs blow up → default False unchanged";
`cosserat_field_3d.py:577-627` the asymmetric reflection density with `inv_S_eps = 1/√(S_ε²+eps_reg)`).
This note makes the structural reason explicit and citable.

---

## 1. Where the 1/S_ε enters — the operator chain

The per-port Lagrangian-EMF source is computed by autograd through the *asymmetric reflection density*, not
by hand. The chain is:

1. **EMF source** (`k4_cosserat_coupling.py`, `_compute_emf_per_port`, line ~801):
   $$\text{EMF}_c[k] = -2\,V_{\text{inc}}[k]\,\frac{\partial L_c}{\partial V_{\text{sq}}}$$
   with $\partial L_c/\partial V_{\text{sq}}$ obtained by JAX autograd of the coupling energy
   (`_coupling_grad_with_V_sq_asymmetric`). The `−2` sign is the corrected Lenz back-EMF sign (see cross-ref);
   the singularity below is **sign-independent** — it lives in the *magnitude* $|\partial L_c/\partial V_{\text{sq}}|$.

2. **Coupling energy** $L_c$ is built from the asymmetric reflection density
   (`cosserat_field_3d.py:554-630`, `_reflection_density_asymmetric`). The reflection coefficient is
   (`cosserat_field_3d.py:578`):
   $$\Gamma \approx \tfrac{1}{4}\!\left[\frac{\nabla S_\mu}{S_\mu} - \frac{\nabla S_\varepsilon}{S_\varepsilon}\right],
     \qquad S_\varepsilon = \sqrt{1 - A^2_\varepsilon},\;\; A^2_\varepsilon \ni \frac{V^2}{V_{\text{SNAP}}^2}.$$
   The electric-sector saturation $A^2_\varepsilon$ carries the $V^2/V_{\text{SNAP}}^2$ term, so
   $S_\varepsilon \to 0$ exactly as $V \to V_{\text{snap}}$ (deep saturation / rupture boundary).

3. **The explicit $1/S_\varepsilon$** appears in the code as `inv_S_eps`
   (`cosserat_field_3d.py:624`):
   ```
   inv_S_eps = 1.0 / jnp.sqrt(S_eps * S_eps + eps_reg)
   ```
   and is multiplied into the gradient (`cosserat_field_3d.py:627`):
   ```
   gamma_vec = 0.25 * (grad_S_mu * inv_S_mu[..., None] - grad_S_eps * inv_S_eps[..., None])
   ```

When autograd differentiates the energy $L_c$ (a function of $\Gamma^2 \propto (\dots/S_\varepsilon)^2$)
with respect to $V^2$, the chain rule pulls down the $S_\varepsilon$-denominator structure, so
$\partial L_c/\partial V^2$ inherits a $1/S_\varepsilon$-class denominator that **diverges as
$S_\varepsilon \to 0$**. The `eps_reg = 1e-6` regulariser only floors the divergence numerically; it does not
remove the structural pole, and near rupture it produces an arbitrarily large — and physically
unbounded — feedback force.

---

## 2. Why this is substrate-native, not a script artifact

The singularity is a property of the **discretized asymmetric-impedance operator itself**, derived from the
substrate's own saturation kinematics ($S_\varepsilon = \sqrt{1-A^2_\varepsilon}$, the electric-sector
saturation factor that vanishes at rupture). It does **not** depend on:

- the retracted result's parameter sweep, damping crutch, or α-injections (those are the artifact;
  this is orthogonal to them);
- a choice of EMF sign (`+2` vs the corrected `−2`): the divergence is in
  $|\partial L_c/\partial V^2|$, so **both signs blow up** near rupture. This is exactly what the engine
  records at `k4_cosserat_coupling.py:269`:
  > *"… a SIGN-INDEPENDENT redundancy where BOTH signs blow up. So use_lagrangian_emf_coupling=False default
  > is UNCHANGED."*
- a numerical tolerance: shrinking `eps_reg` makes the force *larger*, not better-behaved — the hallmark of a
  genuine pole, not a roundoff issue.

**Physical reading (sector-native):** at the electric-sector rupture boundary the asymmetric-impedance
reflection wall ($\Gamma \to -1$) is forming via $S_\varepsilon \to 0$; the Lagrangian-EMF reciprocal, which
sources from $\partial(\text{reflection energy})/\partial V^2$, sees the same vanishing denominator and would
inject an unbounded back-EMF into the K4 V-sector. That is non-physical as an *interior* force — the wall is a
boundary phenomenon, and feeding its formation gradient back as a volumetric EMF source double-counts the
Op14 varactor channel (see `k4_cosserat_coupling.py:262-271`).

---

## 3. Consequence — the off-by-default flag is structurally grounded

`use_lagrangian_emf_coupling = False` (default, `k4_cosserat_coupling.py:223`) is therefore the **correct
substrate-native default near rupture**, for a structural reason: the channel is singular there. This note
records that reason so the flag is no longer justified only by empirical "it blows up" observation but by the
operator's pole structure.

**Scope / limits (honest):**
- This is a CONSISTENCY-class diagnostic about the engine's *own* operator. It is **not** a physics claim
  about electron confinement, mass, or any emergence target.
- It does **not** rehabilitate any part of the retracted result. The "balanced flywheel lock" and
  "$\bar\varepsilon \to \alpha$" claims remain retracted; this note extracts only the structural singularity
  observation.
- No `clm-` ID is minted here. If this should be promoted to a tracked claim (e.g. an invariant about the
  Lagrangian-EMF channel near rupture), that promotion is **deferred to Grant** per the
  consistency-vs-emergence discipline.

---

## 4. Citation index (verify-before-cite — all verified against `origin/main`, 2026-06-27)

| Claim | File:line (`origin/main`) | Verbatim anchor |
| :--- | :--- | :--- |
| Both signs blow up → default unchanged | `src/ave/topological/k4_cosserat_coupling.py:269` | "where BOTH signs blow up. So use_lagrangian_emf_coupling=False default is UNCHANGED" |
| Flag default = False | `src/ave/topological/k4_cosserat_coupling.py:223` | "use_lagrangian_emf_coupling: bool = False," |
| EMF source `−2·V_inc·∂L/∂V_sq` | `src/ave/topological/k4_cosserat_coupling.py:801,855` | "EMF_c[k] = -2·V_inc[k]·∂L_c/∂V_sq" |
| Asymmetric reflection density Γ ≈ ¼[∇S_μ/S_μ − ∇S_ε/S_ε] | `src/ave/topological/cosserat_field_3d.py:578` | "Γ ≈ (1/4) [∇S_μ/S_μ − ∇S_ε/S_ε]" |
| `inv_S_eps = 1/√(S_ε²+eps_reg)` | `src/ave/topological/cosserat_field_3d.py:624` | "inv_S_eps = 1.0 / jnp.sqrt(S_eps * S_eps + eps_reg)" |
| `gamma_vec` multiplies in inv_S_eps | `src/ave/topological/cosserat_field_3d.py:627` | "gamma_vec = 0.25 * (grad_S_mu * inv_S_mu... - grad_S_eps * inv_S_eps...)" |
