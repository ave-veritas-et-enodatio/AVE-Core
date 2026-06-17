# Keystone Coupling — Continuum `dH_c/dt` Conservation Proof (PIECE 1)

**2026-06-16 · keystone bug-vs-substrate discriminator, PIECE 1 (per `_orchestration/2026-06-16_keystone-discriminator-spec.md`).**
**Mandate:** convert the "continuum cancellation is EXACT" claim from *asserted* (engine docstring `a1_cosserat_convergence_engine.py:374`) to *forced* (a derivation), WITH the boundary term — because bulk-cancellation is necessary, not sufficient.

> **PROVENANCE + VERIFICATION STATUS.** This derivation was done in the orchestration session (the PIECE-1 sub-agent failed twice on transient infrastructure — a stream-watchdog stall and a server rate-limit — before writing anything). It is therefore **explicitly staged for independent adversarial verification** (the lane that writes must not be the lane that verifies): the three load-bearing steps are flagged **[VERIFY]** for the re-verify panel to re-derive or refute. Do NOT bank a keystone verdict on this until those clear.

## 1. The discrete coupling (verbatim from `a1_cosserat_convergence_engine.py` @ `c5595558`)
One Hamiltonian term, summed over interior/alive cells:

  H_c = κ̃ Σ  g(A_V) · V · Ξ · 𝟙_interior ,   Ξ = (∇×ω)_z   (tetrahedral-stencil curl, `_cosserat_axial_curl_tet`)

with the **coupling window** `g = g_front(A_V)` a Gaussian shell (`coupling_support='front'`) or sigmoid ramp (`'saturated_interior'`) in the A1 strain amplitude `A_V = strain_A_V()`, masked to alive K4 sites:

  g = exp(−(A_V − front_center)² / (2·front_width²)) · mask_alive     (`_front_window`, `:332`)

The reciprocal forces (`_coupling_forces`, `:366`), with **g treated as frozen** w.r.t. the variation:

  f_V  = −δH_c/δV = −κ̃ g Ξ
  f_ω_y = −δH_c/δω_y = −κ̃ ∂_x†(gV) ,   f_ω_x = +κ̃ ∂_y†(gV)

where `∂_j†` = `adjoint_tetrahedral_divergence` (`cosserat_field_3d.py:161`), the **exact discrete adjoint** of the same tetrahedral gradient the curl is built from. The engine numerically verifies the adjoint identity `⟨s,Ξ⟩ = ⟨∂†s, ω⟩` to float precision (Phase-22 audit `a8232246` reproduced it: `⟨grad s,T⟩=⟨s,adj_div T⟩=23.317`).

The forces enter each sector's own Verlet acceleration (`step_coupled`, `:430`): `a_V += f_V` (Sector A leapfrog), `a_ω += f_ω/I_ω` (Sector B sub-cycled velocity-Verlet, **f_ω frozen once per outer step**, mask-projected mid-step).

## 2. The exact continuum residual — `R = κ̃ ∫ ġ V Ξ`  **[VERIFY — the core algebra]**
For the total `H = E_bulk + H_cosserat + H_c`, with the self-sectors conserving under their own (PML-excluded) symplectic integrators, the coupling residual is

  R ≡ f_V·V̇ + f_ω·ω̇ + dH_c/dt .

Expand the exact total derivative of the discrete `H_c = κ̃ Σ g V Ξ`:

  dH_c/dt = κ̃ Σ [ **ġ V Ξ** + g V̇ Ξ + g V Ξ̇ ] .

Term by term:
- **g V̇ Ξ** : `κ̃ Σ gΞ·V̇ = −f_V·V̇`  (since `f_V = −κ̃ g Ξ`).  → cancels the V-work.
- **g V Ξ̇** : `Ξ̇ = (∇×ω̇)_z`. By the **exact** discrete adjoint, `κ̃ Σ gV(∇×ω̇)_z = κ̃ Σ[∂_x†(gV)ω̇_y − ∂_y†(gV)ω̇_x] = −(f_ω·ω̇)`.  → cancels the ω-work. (Sign check: `f_ω·ω̇ = f_ω_y ω̇_y + f_ω_x ω̇_x = κ̃[−∂_x†(gV)ω̇_y + ∂_y†(gV)ω̇_x] = −κ̃ Σ gV Ξ̇`.)
- **ġ V Ξ** : survives. `ġ = (∂g/∂A_V)(dA_V/dt)`.

Therefore the V- and ω-work **cancel the explicit-V and explicit-ω parts of `dH_c/dt` exactly**, leaving the single exact residual

  **R = κ̃ Σ ġ · V · Ξ = κ̃ ∫ (∂g/∂A_V)(dA_V/dt) · V · Ξ  d³r .**

This is the **dropped `∂g/∂V` variational term**: the window `g` tracks the live A1 amplitude `A_V`, but `f_V = −κ̃ g Ξ` omits the `−κ̃ V Ξ (∂g/∂A_V)(∂A_V/∂V)` piece needed to make it the *exact* `δH_c/δV`. So `f_V` is the functional derivative of `H_c` at **frozen g**, not live g.

## 3. The boundary flux — no BOUNDARY-INJECTION on the periodic grid  **[VERIFY]**
The spec requires accounting the IBP boundary flux `∮(gV)(ω×n̂)dS`. On the engine's grid the curl/adjoint use **periodic `np.roll`** (a torus — *no domain boundary*), and the discrete tetrahedral adjoint is **exact and boundary-free** (the verified `⟨s,Ξ⟩=⟨∂†s,ω⟩` identity holds *globally*, for any field including the alive-masked `g·mask_alive·V` — the adjoint identity does not acquire a surface term from masking). So:

- The continuum IBP surface term **does not appear as a separate boundary flux** on the periodic discrete grid; its analog is absorbed into the bulk via the periodic adjoint and **re-emerges entirely inside `R`** as the `∇/∂` acting on `g` (i.e. the `ġ` / `∂g/∂A_V` structure).
- **⇒ No `BOUNDARY-INJECTION` bin on the periodic engine.** The spec's "boundary flux on the active Γ=−1 wall" concern is real *in spirit* but its discrete realization is the **moving-window residual `R`**, not a surface term. (Caveat **[VERIFY]**: this hinges on periodicity of the force operators. If any force operator used a non-periodic BC, a genuine surface term would re-appear; the engine uses `np.roll` throughout `_coupling_forces`, so it does not.)

## 4. Outcome
- **Bulk continuum `dH_c/dt` CANCELS EXACTLY for frozen g** (functional derivatives exact + periodic adjoint boundary-free). **The `:374` docstring claim is FORCED — conditioned on `ġ=0`.**
- **No `BOUNDARY-INJECTION`** on the periodic grid (§3).
- **The live-window coupling is NOT exactly conservative:** the exact residual is `R = κ̃∫ġVΞ`, nonzero whenever `g` and `Ξ` overlap *and* `A_V` is in motion (the `'saturated_interior'` RUNG-2 config). In the DEFAULT `'front'` config `g` and `Ξ` have **disjoint support** (`_front_window` Layer-b finding) so `g·V·Ξ≡0` ⇒ `R≡0` ⇒ conservative *and inert*.

## 5. THE LOAD-BEARING REFINEMENT — the ladder's binary is incomplete; add a **freeze-g control**
`R = κ̃∫ġVΞ` is **dt-INDEPENDENT** (it ∝ `dA_V/dt`, a physical velocity, not a timestep). So in the ladder's RUNG-2, **a moving-window pump would PLATEAU as dt→0 and be mis-binned `SUBSTRATE-PUMP`** — yet it is a **fixable model choice**, not a deep substrate negative. It is removed by either: (a) **freezing the window** (`ġ≡0`: hold `g` at a fixed configuration), or (b) **adding the missing force** `f_V^extra = −κ̃ V Ξ (∂g/∂A_V)(∂A_V/∂V)` so `f_V` becomes the exact `δH_c/δV` for live g.

**⇒ RUNG-2 cannot distinguish `WINDOW-MODEL-PUMP` (fixable) from a genuine `SUBSTRATE-PUMP` without a freeze-g control.** The discriminator the proof contributes:

> **Freeze-g control (run alongside RUNG-2):** repeat the forced-overlap dt→0 sweep with `g` held STATIC (`ġ≡0`). If the plateau **vanishes** with g frozen → the pump is the dropped-`∂g/∂V` moving-window term = **`WINDOW-MODEL-PUMP`** (fixable: freeze the window or add `f_V^extra`; keystone stays open). If the plateau **persists** with g frozen → it is a genuine continuum **`SUBSTRATE-PUMP`** (keystone leans negative). Equivalently/additionally: measure `R = κ̃ΣġVΞ` directly each step and check it accounts for the measured `dH/dt`.

This is the §3-spirit of the spec ("bulk-cancellation necessary not sufficient") realized on the **window** rather than the spatial boundary: the residual is real, dt-independent, and would otherwise masquerade as substrate.

## 6. Numerical confirmation — TARGETED, deferred to the re-verify
A bounded numerical check (not yet run here): on one saturated `'saturated_interior'` config, evaluate `R = κ̃ Σ ġ V Ξ` per step (with `ġ = (g_t − g_{t−1})/dt`) and confirm it **accounts for the measured `dH/dt`** of the B_int witness; then confirm freezing `g` drives `dH/dt → 0` (modulo the discrete SOURCE-2/3 artifacts the ladder isolates). This is the cleanest closure and is specified for the adversarial re-verify panel / a freeze-g RUNG-2 control.

## Summary verdict (analytical, pending [VERIFY])
**CLEAN-CONTINUUM-CONSERVATIVE for frozen g; NO BOUNDARY-INJECTION on the periodic grid; the `:374` claim is FORCED conditioned on `ġ=0`.** The live-window coupling carries an exact, dt-independent residual `R=κ̃∫ġVΞ` (dropped `∂g/∂V`) that the ladder would mis-read as `SUBSTRATE-PUMP` — so a **freeze-g control is required in RUNG-2** to separate the fixable `WINDOW-MODEL-PUMP` from a genuine substrate negative. The bug-vs-substrate binary becomes a **trbinary**: integrator-artifact (dt→0) / window-model-pump (plateau but freeze-g-removable) / substrate-pump (plateau, freeze-g-persistent).
