# T_ij stress-register + X44b — the ONE-BUILD-SERVES-FOUR CHARTER

**Date:** 2026-07-14
**Class:** charter (draft the discriminator BEFORE any solver / driver) — the F6-charter pattern (`research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md`; the #662 remanence-charter model: charter doc + frozen-bin candidates + fireable-vs-entailed + fool-modes + Ax3/reconciliation carve). **Charter first; PR DO-NOT-MERGE; the build + the four preregs land in a follow-on arc after this charter's review.** No solver code and no driver in this PR.
**Grant GO:** 2026-07-14 — the registers-first plan of record is **RATIFIED** (Grant 2026-07-13, `_orchestration/2026-07-10_rulings-docket.md:457`): build order **registers (T_ij + depletion) → X44b → F6**; one materialization build discharges the shared flux-object debt before the sector charters fire.
**Frozen prereg(s):** downstream sibling files (one per consumer) — **not created in this commit**; freeze-by-push BEFORE each consumer's driver, gated on this charter's review and on the build landing.
**Companion inputs (read first):** the registers-walk framing note (`research/2026-07-13_registers-walk_framing.md` §1–§3 + continuation); the X44 Komar-source result §7 (`research/2026-07-12_x44-komar-source_result.md:186-215`, the escalation options — option 5 = X44b); the Wall-A ruling (`_orchestration/2026-07-10_rulings-docket.md:511-624`); the cavity-census Stage-1 FROZEN prereg (`research/2026-07-14_cavity-census-stage1_prereg_FROZEN.md`, on branch `analysis/cavity-census-stage1`; Stage-2 is this register's consumer (c)).

---

## Sector header (mandatory)

- **SECTOR** — the T_ij register is a **two-sector object**: the **A1 dilatation-mass channel** (bulk/shear elastic stress, `constants.py:766` `G_VAC = RHO_BULK·C²`) **and** the **T2 / Cosserat micro-rotation channel** (the couple-stress `σ^A` that drives node rotation — the charge/helicity/spin DOF, `micropolar_bloch.py:72,88-90`; `cosserat_field_3d.py:28`). **A1 ⊥ T2**: the register carries both and **never cross-wires** them ("A confines/holds B" is forbidden). The wave-side (transverse-EM Maxwell stress) is the **reactive store at the envelope interface**, not an independent source (§3 transducer ontology).
- **MODE** — Stage-1 use is **cold, static, bound-resonator** stress: the materialized flux object the engine has never written, not a driven mode (`research/2026-07-13_registers-walk_framing.md:7`). Consumer (a) X44b adds a **static, force-balanced (virialized)** family; consumer (b)/(c) read at an **eigenmode boundary**; the driven leg is secondary and per-consumer.
- **REGIME** — **cold-linear elastic + Op14-saturated envelope**. The constitutive moduli are the linear-response Lamé/couple-stress constants; the envelope is where the linear-response identity breaks (`S(A)→0`, the yield surface). A linear-only read of an intrinsically-saturated envelope is **ARTIFACT-eligible, not a negative** (regime-discipline; the census Plumber-Q3 fence).
- **PHASE-STATE** — cold medium for the elastic register; driven-toward-self-stiffened only where a consumer's prereg declares it. **Local-clock modulation is live at the envelope**: the momentum flux weights by `c_eff²(V)` (the saturated local speed), **not** the bare `c²` (see §2.3, Flag F2).
- **Instrument** — the build **extends `cosserat_field_3d`** (materialize `σ_ij` from its existing `ε_ij`/`κ_ij` fields) + a `T^ij` spatial momentum-flux (generalize the scalar `T^0x` at `annihilation_engine.py:173-181`). **No new engine class** — the reconciliation gate (§2.3) is the certificate that this is assembly, not a fourth solver.
- **consistency-vs-emergence** — the register itself is **manifestation-class** (it materializes a flux the moduli already imply). The four consumers split: X44b (a) and the electron T_rr (d) are **consistency-class** (do the engine's own registers close a known ledger); the ENVELOPE-EIGENMODE gate (b) is **discovery-class either way** (§3b); the census Stage-2 (c) can reach **emergence-class** only through the (2,3)-selection import→derivation door its own prereg fences off.

**Register:** AVE substrate + EE (Cosserat/micropolar elasticity, couple-stress, Maxwell stress at a matched interface, native K4 tetrahedral divergence). **Not** a Cauchy-symmetric continuum (that welds the swivels shut — Q1), **not** a QED stress tensor, **not** a Cartesian-stencil `∇·σ` (that is the disabled-DOF stencil bug the gate exists to catch).

> **★QUARANTINE — Grant-walked RULING-GRADE INPUTS, not canon.** Three walk inputs set the *shape* of this charter and are quarantine-tagged wherever they appear: (i) the **transducer ontology** (§3 of the framing note — the envelope is the transducer between transverse-EM stress and lattice mechanical stress); (ii) **Q1/Q2 rulings** (carry the twist; the brace = ⟨Maxwell stress⟩ of the (2,3) winding at its own envelope, `_orchestration/2026-07-10_rulings-docket.md:458-459`); (iii) **Grant's balance≡yield conjecture** (the continuation (a.4) — yield derives from opposite-but-equal stresses balancing across the envelope, and that balance-locus ≡ the `A_yield` level-set). These are **walk-record**, not results; each consumer's frozen prereg carries the bins that discharge them. **Nothing in this charter canonizes.**

---

## §0 · One-paragraph charter

The engine goes **strain → energy → force and skips `σ_ij` entirely by design** (`cosserat_field_3d.py:14`: "The energy gradient is computed by jax.grad — no hand-derived stress tensors"). Four independent arcs are each blocked on the same missing object — a materialized **stress / momentum-flux register**: **(a)** X44b cannot run the faithful Komar test without a `+3∫p` Tolman stress term (`research/2026-07-12_x44-komar-source_result.md:147-155`); **(b)** the ENVELOPE-EIGENMODE gate cannot compare `σ_ij` across the electron's envelope; **(c)** the cavity-census Stage-2 self-consistency audit cannot compare mode-stress to lattice-stress at the settled radius; **(d)** the electron brace is a **force not a pressure** and needs `T_rr(r)` (`research/2026-06-30_electron-portmap-derivation_result.md:250-254`). This charter specifies **ONE build** — the constitutive contraction `σ_ij = λδ_ij ε_kk + 2με_(ij) + couple-stress(κ)` **carrying the asymmetric `σ^A`**, plus the spatial momentum flux `T^ij`, plus **the reconciliation gate** (`∇·σ` on the native K4 tetrahedral stencil ≡ the existing autodiff `−∂E/∂u` to machine precision) — that serves all four consumers, each of which freezes its own prereg at its own arc. The gate is the reconcile-don't-declare exemplar: it is the only certificate that the hand-assembled `σ` is native-substrate physics and not a Cartesian-stencil leak.

## §1 · Physical picture (substrate)

### 1.1 What the medium already carries (implicitly)

All moduli are live and provenance-tagged; the register **assembles**, it does not add physics:

| quantity | value / source | FORM/VALUE tag |
|---|---|---|
| shear modulus `G_VAC` | `RHO_BULK·C²` (`constants.py:766`) | VALUE (import basis `{ρ_bulk, c}`) |
| string tension `G_STRING` | `T_EM/ℓ` (`constants.py:762`) | VALUE-import |
| bulk / `V_LONG` from `K=2G` | `constants.py:781`, `:769-773` | **VALUE — GR-IMPORTED (PR#261); do NOT upgrade to "derived"** |
| Machian bulk modulus `κ_grav` | `c⁴/7G` (`backreaction.py:84`) | VALUE-import (gravity sector) |
| couple-stress `γ` / `κ_rot` | `micropolar_bloch.py:72,88-90`; `cosserat_field_3d.py:28` | VALUE-import |
| Cosserat balance laws (as comments) | `micropolar_bloch.py:33-35`; `trampoline-framework.md:47,87,356` | FORM (the σ_ij ≠ σ_ji structure) |
| the two rank-2 fields that exist | `ε_ij` and `κ_ij` (`cosserat_field_3d.py:175-191`) | — |

**The gap.** The only rank-2 fields materialized today are `ε_ij` and `κ_ij`; **no live object** is named `σ_ij / T_ij / stress_tensor / momentum_flux / force_density` (two-method absence check, grounding-card R4/R5). This is a **materialization gap, not a physics gap** — FAIL-by-design.

### 1.2 The transducer ontology (★QUARANTINE — Grant-walked, sets the register's shape)

> **Grant, verbatim (framing note §3):** "the envelope is the transducer between transverse EM stress and lattice mechanical stress; all mechanical stress derives from, and returns to, the physical lattice."

Matter's `T_ij` is **two coupled halves at the envelope interface**: the **wave-side** (the winding's cycle-averaged transverse-EM Maxwell stress, *including the angular flux* — the couple-stress / spin channel) and the **lattice-side** (the full Cosserat `σ`). The envelope is the equilibrium interface; the wave-side is the reactive store, not an independent source. **Wording rail (binding):** the cycle-averaging is a **Jensen magnitude** (`⟨S⟩ < S(⟨A⟩)`, `chiral-thrust-derivation.md:28,51`) whose **direction is set by external geometry, not the kernel** — the kernel is even-in-A and cannot rectify (`research/2026-06-08_rrad-l-rectification_result.md:66-78`). **Never write "the kernel rectifies."**

### 1.3 One build serves four — the unbuilt bridge

The corpus has **two unconnected virials** and **zero electron-side `+3∫p`/Tolman hits** (grounding-card Convergence-1; `categorization.py:155-168`). The bridge is exactly the missing stress: the general `σ_ij` register manufactures the electron's `T_rr` as a special case, and `T_rr` is the object every consumer needs. **One build discharges the shared materialization debt** (`research/2026-07-13_registers-walk_framing.md:60-67`, §2(e)).

## §2 · THE BUILD SPEC

**Scope:** this section specifies the ONE build. It is written as a spec for the follow-on arc; **no code lands in this PR.**

### 2.1 The constitutive contraction — carrying the asymmetric σ^A

Materialize the stress from the live moduli and the existing strain/curvature fields:

```
σ_ij = λ δ_ij ε_kk  +  2μ ε_(ij)  +  couple-stress term in κ_ij
```

- **λ, μ** — the vacuum Lamé pair from the live moduli: `μ = G_VAC = ρ_bulk c²` (shear), `K = 2G` (bulk), `λ = K − (2/3)μ`. **All VALUE-imported; `K=2G` carries the GR-IMPORTED tag (PR#261) — no upgrade to "derived."**
- **ε_(ij)** — the symmetric strain; **but the strain itself is already Cosserat**: `ε_ij = ∂_j u_i − ε_ijk ω_k` (`cosserat_field_3d.py` `_compute_strain`, :175-191), so the micro-rotation `ω` is already wired into `ε`.
- **★ THE ASYMMETRIC PART IS MANDATORY (Q1 ruling — carry the twist).** The antisymmetric `σ^A_ij = (σ_ij − σ_ji)/2` is **the source of couple stress — the moment per unit area that drives microrotation** (`trampoline-framework.md:87`, verbatim). A Cauchy-symmetric-only `σ` **deletes spin from the stress ledger** (`research/2026-07-13_registers-walk_framing.md:82`). The couple-stress term is built on `κ_ij = ∂_j ω_i` with the modulus `γ`/`κ_rot` (`micropolar_bloch.py:72,88-90`). **A symmetric reduction is NOT acceptable** — it is a disabled-DOF stencil bug, not a simplification (structural-null stencil lens).
- **FORM/VALUE:** the *structure* (`σ_ij ≠ σ_ji`, the two-modulus split) is FORM-derived from the Cosserat axioms; the *moduli values* are VALUE-imported.

### 2.2 The spatial momentum flux T^ij

Today **only the single scalar `T^0x` exists**: `field_momentum_x` returns `P_x = −∫ (∂_tV)(∂_xV)/c_eff²(V) dV` (interior-only, V-sector, x-axis; `annihilation_engine.py:173-181` — re-verified verbatim this session). The build generalizes this to the **full rank-2 spatial momentum flux** `T^ij` (all i,j; the wave-side Maxwell stress *including the angular/couple-stress flux* per §1.2), so momentum transport is a tensor, not a single scalar witness.

### 2.3 ★ THE RECONCILIATION GATE — the reconcile-don't-declare exemplar

**`∇·σ` on the NATIVE K4 tetrahedral stencil MUST equal the existing autodiff `−∂E/∂u` to machine precision.**

- The engine deliberately carries **no** hand-derived stress today (`cosserat_field_3d.py:14`); force is `a_u = −∂E/∂u / ρ` via `jax.grad` (`:2004-2020`). The load-bearing native operator is `_tetrahedral_gradient` (defined `cosserat_field_3d.py:148`, load-bearing call in `_compute_strain` `:177`).
- **The gate:** assemble `σ_ij` from §2.1 **independently** of the energy autodiff, take its divergence with `_tetrahedral_gradient` (the native K4 stencil, NOT a Cartesian `np.gradient`), and require, per node and per sector (A1 and T2/ω):

  ```
  ‖ ∇·σ |_K4  −  (−∂E/∂u) ‖ / ‖∂E/∂u‖  <  1e-10   (machine precision)
  ```

- **Why this is the exemplar (per the identity-break leaf's vacuous-detector knife, `identity-break-test-design.md`):** the gate is **not** a conservation identity — it reconciles two **independently computed** objects (a hand-assembled constitutive `σ` vs the autodiff force) that agree ONLY if the stencil is substrate-native. A Cartesian-stencil `σ` will **fail** the gate on any configuration with non-trivial `σ^A`; that failure is the certificate. **No PASS may be booked off a tautology** (e.g. differentiating the same `E` twice).

> **★ Flag F1 (grounding-card refinement, flag-don't-fix).** Grounding-card receipt R5 wrote `T^0x = −∫(∂_tV)(∂_xV)/c²`. The **live code divides by `c_eff²(V)`** (the Op14-saturated local speed, `c_eff_squared(self.V)`), **not** the constant `c²`. This is load-bearing: at the envelope where `S(A)→0`, `c_eff²` departs sharply from `c²`, so the momentum flux must weight by the **local clock**, not the bare vacuum speed (local-clock-modulation discipline). The `T^ij` build inherits this weighting; a `c²`-weighted flux would misread the envelope. Recorded as a receipt refinement, not a card failure.

## §3 · THE FOUR CONSUMERS (each with its acceptance test)

The ONE build (§2) is pulled by four arcs. Each freezes its **own** prereg at its **own** arc; this charter names the consumer, its regime/sector, its acceptance test, and (in §4) its frozen-bin candidates + fool-modes. **The build lands first; the consumers fire staggered** (§5).

### (a) X44b — the faithful Komar test

**Regime/sector:** A1 dilatation / gravity; static, **force-balanced (virialized)** family; **linear-ε clock** (cold-linear). Consistency-class (certification of the latent `#86` M_eff-vs-far-field gap).

**What it is.** X44 (`research/2026-07-12_x44-komar-source_result.md`) tested a **density-only `√S` weight** and banked **frozen bin (iii) UNRECONCILED** (`η_mixed = +1.05`, O(1), resolution-stable). Its §5b/§7 named *why*, and named the completion path (escalation option 5 = **X44b**). The three ingredients it found absent/mismatched, now supplied by the T_ij register:

1. **A linear-in-ε clock weight** — the engine's OWN gravitational redshift register `n = 1 + (2/7)ε` (`backreaction.py:647-651`), **NOT** the EM operating-point quadratic `√S` (the #652 wrong-register lesson: `√S` is the EM-transverse register, `n_eff`-overload; `research/2026-07-12_x44-komar-source_result.md:126-138`).
2. **The `+3∫p` Tolman/stress term** — supplied by the new register's `T_rr` (consumer (d)) and full `σ_ij`. Structurally absent before: `gaussian_blob` is a bare prescribed scalar `T₀₀` with no `T_{ij}` companion (`:151-155`).
3. **A force-balanced (virialized) test family** — a self-consistent hydrostatic source, NOT the prescribed `gaussian_blob` (which is not force-balanced).

**★ SOURCE-side theorem-target (Grant-walked, framing §3).** Bound transverse content carries the **radiation equation of state `p = u/3`**. A Komar/Tolman source weights `(ρ + 3p)`, so pure wave content contributes `(ρ + 3·u/3) = ρ + u` — a **factor-2 doubling for the wave part**. This is the *same* factor-2 as the derived light-deflection doubling: light couples to the transverse Cosserat-shear index `n_⊥ = 1 + (2/7)χ_vol → 4GM/bc²` (the observed 1.75″), bridged by `z = (n_temporal − 1)/2` — a propagating signal picks up 2× the local clock (`temporal-spatial-lattice-decomposition.md:26,28`, re-verified; note the W1 walk-back: deflection is the (2/7) transverse index, **not** `n_spatial`, which would give 18GM/bc²). **This is a THEOREM-TARGET, not a result** — the claim owed is that the envelope's wave-side `T_rr`, fed through the Komar source, reproduces the deflection doubling *from the source side*. FORM-class (a factor-2, not a magnitude).

**Acceptance test.** On a **virialized** family (residual force per node < the gate tol of §2.3), compute `η_mixed = slope(m_g/M_eff − 1 vs f)` under the linear-ε clock, **with and without** the `+3∫p` term:
- **without `+3∫p`:** the ladder predicts `η ≈ −1` (the linear-clock overshoot: `∫ρφ = 2W = −2U`, `:140-145`).
- **with `+3∫p` (`= +U` by the static virial):** the ledger closes to `M − U` ⇒ **`|η| < 1e-3`** (RECONCILE).
Unlike X44, **reconcile is STRUCTURALLY REACHABLE**, so a miss is a **real falsification of RULED (c)** — not a regime artifact (`:198-215`, §4b). PASS = the ladder rung `η ≈ −1 → 0` is traversed *by adding the computed stress term*, not by tuning.

### (b) THE ENVELOPE-EIGENMODE GATE (Grant's balance≡yield conjecture)

**Regime/sector:** A1 + T2 at the electron's envelope; cold-linear eigenmode + Op14-saturated wall; **RADIUS-DISCRIMINATING**. **Discovery-class either way.**

**What it is.** Read `σ_ij` on **both sides of the electron's envelope** and locate two surfaces independently: the **stress-balance locus** (where the register's `σ_ij` is opposite-but-equal across the envelope) and the **strain-yield locus** (the `A_yield` / `S(A)→0` level-set). Grant's conjecture (framing continuation (a.4), ★QUARANTINE): *yield derives from opposite-but-equal stresses balancing across the envelope, and that balance-locus ≡ the `A_yield` level-set* — i.e. **they coincide.**

> **★ Flag F3 (flag-don't-fix — a live contradiction the gate adjudicates).** Grant's balance≡yield conjecture (**they coincide**) contradicts the **corpus's accepted radius numbers**, which put the two surfaces **~10× apart**:
> - **balance locus** = the hollow-vortex binding equilibrium `R* = Γ/√σ ≈ 1.6 ℓ_node` (electron/reduced-Compton scale; `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/hollow-vortex-binding.md:49`);
> - **yield floor** = the Wall-A ropelength floor `ℓ_node/(2π) ≈ 0.159 ℓ_node` (the `S(A)→0`/`A_yield` ground-state surface; `_orchestration/2026-07-10_rulings-docket.md:522-538`, `606`).
> - ratio `1.6 / 0.159 ≈ 10.06`.
>
> Both file paths recorded verbatim; **not silently reconciled** (Grant adjudicates). Rider: the `1.6` is itself **DIMENSIONALLY-FORCED / soft** — "a consistency check, not a discriminating test" (`hollow-vortex-binding.md:133`) — so a "two walls" verdict rests on a soft number, and a "coincide" verdict means one of the two accepted numbers is wrong.

**Acceptance test (RADIUS-DISCRIMINATING; the gate must let "two walls" win).** Report `R_balance` (σ_ij opposite-equal crossing) and `R_yield` (the `A²=2α` / `S→0` level-set) as **independent** dimensionless radii in `ℓ_node` units, with the §2.3 grid-resolution uncertainty. Bins: **COINCIDE** (`|R_balance − R_yield| < 2·Δgrid` ⇒ balance≡yield **confirmed**, and one of `{1.6, 0.159}` is thereby wrong — a discovery) / **TWO-WALLS** (`R_balance ≈ 1.6`, `R_yield ≈ 0.159`, ~10× apart ⇒ only the gap-closing model is rejected; balance and yield are distinct surfaces) / **INCONCLUSIVE**. **The gate must be built so TWO-WALLS is winnable** — it must NOT force coincidence. *Discovery either way.*

### (c) CENSUS STAGE-2 — the self-consistency audit

**Regime/sector:** A1 imposed wall + T2 interior mode; the settled-radius eigenmode. Consistency-class; **the ONLY outcome class that re-opens D3 is a Stage-2 balance failure** (`research/2026-07-14_cavity-census-stage1_prereg_FROZEN.md`, §5 D3-movement map).

**What it is.** The cavity-census Stage-1 (FROZEN prereg, branch `analysis/cavity-census-stage1`) imposes a `Γ=−1` TIR wall and reads **existence-given-boundary** (which winding class is the ground-state closure). **Stage 2 (task #45) rides THIS register:** at the census-settled radius `R_wall`, compare the **mode-stress** (`σ_ij` of the interior eigenmode the census found) against the **lattice-stress** (the `σ_ij` the imposed wall applies) — the self-consistency the static-wall Stage-1 explicitly does NOT test (Stage-1 Fence 2: "self-consistency is Stage 2").

**Acceptance test.** At `R_wall`, does the mode's own `σ_ij` reach the **yield stress** `σ_yield` at the wall (the ENVELOPE leg: the near-field IS a real yield envelope, not an arbitrary Dirichlet clamp)?
- **`σ_mode(R_wall) = σ_yield` within tol** ⇒ **SELF-CONSISTENT / ENVELOPE leg supported** (the wall the census imposed is the wall the mode would itself raise).
- **mismatch requiring interior structure the singularity forbids** ⇒ **RE-OPENS D3** (the one outcome class that genuinely does).
The read is at the **energy-density peak of the shell** (density-peak sampling, not centroid — a shell's centroid is empty), with PML-cell exclusion before any top-K extraction (Rule-10 corollary).

### (d) The electron T_rr — the brace's missing integration

**Regime/sector:** T2/Cosserat winding at its own envelope; cold-static; consistency-class (with an INCONCLUSIVE caveat carried).

**What it is.** The electron brace as derived is a **FORCE, not a pressure**: `B_a = −dU_rot/dr = +L_w²/(m_eff r³)` is energy/length [N], not energy/volume [Pa] (`research/2026-06-30_electron-portmap-derivation_result.md:250-254`; `sign(dF/dr) = sign(3−p)` at `:364-373`). Q2 ruling (★QUARANTINE): the brace **= ⟨Maxwell stress⟩ of the (2,3) winding evaluated at its own envelope**; the general `σ_ij` build manufactures `T_rr` as that special case. **Carry the caveats:** the one force-balance sim was **INCONCLUSIVE** (`r⁻³` not reproduced, `|L_w|` drifts 16–17% under lossless evolution; `research/2026-06-30_electron-bind-sim_result.md:17,110-121,147`); `clm-jwyy6l` "#90 mass IS inductance" is at **solidity 0.30, do-not-build-on** (`manuscript/ave-kb/vol2/claim-quality.md:717`) — rest-mass store is A1, not inductance.

**Acceptance test.** From the register's `T_rr(r)` (read off the eigenmode's OWN stress, **never** the seeded template `ê_w`), reproduce the derived brace: (i) the `r⁻³` scaling of `∫ T_rr dA`, and (ii) feed `+3∫p_electron = +U` (the electron virial `E_elec = E_mag = ½m_e c²`, `research/2026-06-30_electron-portmap-derivation_result.md:489-495`) into consumer (a). **Reactance-pair discipline (Rule-10):** track `L_w` over the recording window; if `L_w` drifts (as in the inconclusive bind-sim), the `r⁻³` read is **INCONCLUSIVE, not a PASS** — the `L_w = const` premise the brace rests on must be satisfied for the read to count. Do NOT build on `clm-jwyy6l 0.30`.
