# H_couple — Status Clarification (2026-06-20)

**Class-C status note; no `clm-` minted.** Written to settle a recurring "is H_couple a blocker?" question raised across the node-scattering → varactor → Fork-B arc and the vol_9 §6 figure slots.

**TL;DR.** H_couple is **not a blocker** and **not unimplemented**. The coupling *term* is coded, α-free, and conserving. The only remaining gap is a **structural coupled-eigensolve figure** (vol_9 §6 slot iii). And the chord-payoff it superficially enables — "derive 1/α from the coupled network" — is **adjudicated CIRCULAR and forbidden to re-pose.**

---

## 1. H_couple EXISTS (coded, α-free, conserving)

$$H_{\text{couple}} = \tilde\kappa \int g\, V\, \Omega_w \, d^3r, \qquad \Omega_w = (\nabla\times w)\cdot\hat{x}, \qquad \tilde\kappa = \frac{pq}{p+q} = \frac{6}{5}\ (\alpha\text{-FREE}).$$

It is the **chiral cross-sector coupling** between the A1 / mass V-sector and the photon-director winding (the "chiral circulator" of the graded-vacuum-network reframe). The strength `κ̃ = 6/5` is **α-free** (topological `pq/(p+q)`), not a tuned constant.

Coded loci (verified 2026-06-20, `main @ 19d55266`):
- `src/ave/core/cross_sector_coupling.py:76,102,152` — the canonical `H_couple` forms (`κ̃ ∫ g V Ω_w` and the `w·(∇×ω)` variant).
- `src/ave/core/crystal_graft_v4.py:27,144,175` — `H_couple` inside the **joint conserving Hamiltonian**: `TOTAL H = E_V + E_w + E_ω + H_couple` conserves (the "energize-LOCK"; the continuum cancellation is exact).
- `src/ave/core/crystal_engine.py:227,253` — `H_couple = γ ∫ g_front·V·Ω_w`, `γ = κ̃ = 6/5`.
- `src/ave/core/unified_genesis_engine.py:15` — photon `w` + chiral `H_couple` (`κ̃ = 6/5`).

So the coupling **mechanism** exists and runs in the dynamical engines.

## 2. The only gap = the coupled EIGENSOLVE (a figure, not a mechanism)

`H_couple` exists for the **dynamics** (the genesis engine integrates it). What is **not** wired is `H_couple` into the `graded_vacuum_network.py` **spectral** solver — i.e. the coupled **mode-splitting / avoided-crossing** eigenvalue computation. This is exactly vol_9 §6 slot (iii)'s "coupled arm" (`fig:vol9_forkA_discriminator`: *Q vs coupling, mode-splitting (coupled) vs free-crossing (isolated)*).

- The **isolation** leg (the confined eigenmode is lossless, `Q → ∞`) **is** built (PR #297, `graded_vacuum_network.py`).
- The **coupled** spectral arm is **not** wired in.

This is a **structural-completeness item** (one figure / one solver path), **NOT** a missing mechanism.

## 3. NOT blocking

- **Fork-B** (saturation-tank mass confinement) operates on the isolation / stiffness operator (`L = adjoint_div(D∇)`) — it does **not** need `H_couple`.
- The **genesis / coupling dynamics** already use `H_couple`.
- The only thing the coupled-eigensolve gates is the **vol_9 §6 slot (iii) coupled mode-splitting figure**, currently honestly flagged deferred.

## 4. GUARDRAIL — the chord-payoff is adjudicated-CIRCULAR; do NOT re-pose

The tempting next move — *"derive the loaded / radiative `Q = 1/α` from the coupled network / EM-port admittance"* — is **adjudicated CIRCULAR** (gate `wmighcz1z`, 2026-06-19; canonical at [`electron-bound-resonator-coverage.md:161`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md): *"do NOT re-pose to a Build-B slot"*):

- **(a)** the engine's radiative leak is **literally `1.0 − alpha`** (`cvr_model.py:161` `gamma_mag_sq_leak`) — feeding it back to "derive" `137` is the **instrument-echo trap**.
- **(b)** the genuinely α-free edge-radiation answer is **already** the cold-cage `Q ≈ 30.8` closed-negative.
- There is **no α-free path to `137`** through the loaded port. The slot stays EMPTY (anti-substitution).

So spawning a build to "work on `H_couple` to derive the electron `Q`" would **re-pose an explicitly-forbidden circular question**. `α` stays a **scoped standing echo** (see the α-echo register / form-value meta-finding).

## 5. Scope of any future H_couple work

The **only** legitimate remaining `H_couple` build is the **structural coupled-eigensolve**: wire `H_couple` into the `graded_vacuum` spectral solver to produce the coupled mode-splitting figure (vol_9 §6 slot iii). That is a **consistency / structural** result — *does the coupling produce an avoided-crossing? (a yes/no structural signature)* — **NOT** a value-chord, and it must **not** be narrated as an α-derivation. Optional, non-urgent; can follow the Fork-B arc.

**Cross-links:** `device-circuit-models.md` (graded-network / Fork-A discriminator), [`electron-bound-resonator-coverage.md:161`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md) (loaded-Q adjudication), `theorem-3-1-q-factor.md` (loaded-Q reframe), the α-echo / form-value register.
