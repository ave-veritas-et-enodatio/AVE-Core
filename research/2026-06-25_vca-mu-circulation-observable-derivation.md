# VCA route-C step-1 — substrate-native derivation of the circulation-keyed vacuum μ-grade observable

**Status:** DERIVATION MEMO (step 1) — design memo for the observable + normalization +
constitutive law. **The build (route-C step 2) HAS SINCE LANDED on branch
`engine/mu-circulation-keying`** (fdtd_3d.py + fdtd_3d_jax.py + test_vca_mu_circulation_keying.py);
this memo is committed for provenance. See the build-status banner below for what changed against
the design proposal — in particular the grid-invariance correction (FIX A) and the loaded-μ
energy result.

> **⚑ BUILD-STATUS BANNER (post-implementation, route-C step 2 + fix-pass).**
> The constitutive law `μ_eff,i = μ_0/√(1−A_I,i²)`, `A_I,i = curl_h_i·ℓ_node/I_max` (per-component,
> INCREASING relativistic inductor) is implemented in `_compute_local_mu` (numpy, canonical) and
> `_compute_local_mu_kernel` (JAX twin). Three corrections from the adversarial fix-pass:
> - **NORMALIZATION IS A FIRST-CUT, NOT GRID-INVARIANT (FIX A).** The executed kernel keys on the
>   UNDIVIDED discrete `curl_h` ([A/m]) × ℓ_node. For a FIXED PHYSICAL field a finite difference
>   scales ∝ dx, so the executed `A_I ∝ dx` — verified empirically (A_I halves when dx halves).
>   The §2 "dx cancels against ℓ_node/dx" form is the PROPOSED (un-ratified) normalization, NOT
>   what executes. Grant signed off the **ℓ_node DIRECTION** (2026-06-25 "use ell_node instead of
>   dx"), NOT a grid-invariance claim. The proper per-cell ∮H·dl → I_max factor remains the §2/§8 #1
>   OPEN "derive, don't invent" item. **MOOT for the static-B null** (A_I=0 for any factor); **LIVE
>   only for a dynamic driver.** Code docstrings + the test module say so plainly; a strict-xfail
>   test (`test_grid_invariance_fixed_physical_field_xfail`) records the gap and flips green when
>   the proper normalization lands.
> - **LOADED-μ ENERGY IS CONSERVATIVE (FIX C).** A genuinely-loaded run (A_I≈0.77, μ≈1.56·μ_0, ε
>   linearized so only μ is nonlinear, short interior window) gives secular |dH/H| ≈ 7.1e-3 with a
>   μ-attributable excess over the linear baseline of ≈ 1.4e-3 — bounded, no secular growth. The
>   stateless half-step curl_h recompute (§6 option (b)) is energy-honest under loading. The
>   wrong-integrator control trips (>1) and JAX↔numpy agree to ~1e-15 under load.
> - **α-ECHO FLAGGED (FIX F).** ℓ_node=ℏ/(m_e c) and I_max=ξ_topo·c carry the electron
>   calibration → the threshold SCALE is an α-echo (CONSISTENCY class, §7); the keying STRUCTURE is
>   α-clean. Documented in code + §7, not removed.

**Date:** 2026-06-25
**Lane:** implementer (memo only)
**Repo state at authoring:** branch `engine/mu-circulation-keying` @ `00f1e97b` (Merge PR#432).
**Pre-work skills fired:** `substrate-native-check` (operator/observable construction in prose —
trigger 6), `phase-space-coordinate-check` (the kernel argument is a phase-space reactance
coordinate, A46), `consistency-vs-emergence` (the I_max scalar carries `e` — magnitude class is
the load-bearing tag), `verify-before-cite` (every file:line below was grepped on HEAD; stale
line numbers from the upstream maps are flagged inline).

> **⚑ STATE NOTE (read first).** The free-EM μ-channel is ALREADY LINEAR on `main` per the
> VCA-R01 resolution (`src/ave/core/fdtd_3d.py:260` returns `mu_base`; commit `4d0d6e5f`
> "VCA-R01 (RESOLVED): free-EM mu-channel is linear"). This memo does NOT propose unmaking that.
> It scopes the observable + normalization + constitutive law for a *future* dispersive-μ /
> bound-circulation refinement, and surfaces the regime/sector decision (free-EM vs bound) that
> Grant must make BEFORE any I-keyed code lands. See §6 + §8.

---

## §1 — THE OBSERVABLE: I_cell = ∮H·dℓ per Yee cell (node-safe; the answer to Blocker B)

The substrate-native μ-grade kernel argument is the **internal circulating current** `I`, a
rate/flux variable — NOT the static field magnitude `|B|`. The canon is explicit:
`node-up-small-large-signal.md:109` defines the inductor's variable as the circulating
current `I ∝ ∮H·dℓ` "sustained" (a flux variable, contrasted with the varactor's potential
variable `V ∝ E` at :107). The coordinate-discipline box at `node-up-small-large-signal.md:114`
tags `A_I` as a **phase-space / reactance** coordinate (A46) and warns that keying μ on the
static `|B|` magnitude measures the wrong coordinate (:118).

**The discrete observable already lives inside the stepper.** The Ampère/displacement-current
half-step computes the discrete curl-of-H once per cell-face per component (cites re-pinned to
the post-build executed sites, route-C step 2 landed; the design-memo authoring cites
`:332/337/342` were against `00f1e97b` BEFORE any engine code existed):

- `fdtd_3d.py:522`  `curl_h_x = (Hz[:,1:,1:]-Hz[:,:-1,1:]) - (Hy[:,1:,1:]-Hy[:,1:,:-1])`  (in `update_electric_field`)
- `fdtd_3d.py:523`  `curl_h_y = (Hx[1:,:,1:]-Hx[1:,:,:-1]) - (Hz[1:,:,1:]-Hz[:-1,:,1:])`
- `fdtd_3d.py:524`  `curl_h_z = (Hy[1:,1:,:]-Hy[:-1,1:,:]) - (Hx[1:,1:,:]-Hx[1:,:-1,:])`

(The same stencils are recomputed in `update_magnetic_field` at `fdtd_3d.py:440-450` to KEY μ
— the stateless half-step recompute the build chose, memo §6 option (b).)

Each is the oriented difference of two H-edge pairs = the **4-edge ∮H·dℓ loop around one cell
face**, with units `[A/m]` (since H is `[A/m]` and the difference is dimensionless per the Yee
stencil). The substrate-native per-cell current threading the face is therefore:

```
I_cell  =  curl_h_component · dx          [A/m] · [m]  =  [A]   (ampere)
```

This is the discrete `∮H·dℓ` (Ampère's law: the line integral of H around a loop equals the
current threading it). It is a **pure finite oriented sum scaled by `dx`** — ZERO divisions; in
particular NO `/|B|` and NO `/|H|`. That is exactly why it is the node-safe answer to **Blocker B**:
the rejected pointwise form `|dB/dt|/|B| = ω·|tan(ωt)|` diverges to `A_I ≈ 2.1e10` at every
wave zero-crossing; the discrete-curl `I_cell` has no `|B|` in the denominator and is bounded by
the finite H field, so it cannot diverge.

Reuse note: `curl_h_{x,y,z}` is born in `update_electric_field` (`fdtd_3d.py:430-455`,
post-build), but the H-update (`update_magnetic_field`, `fdtd_3d.py:386-428`) is where μ_eff is
consumed — one half-step earlier. So `I_cell` must be either (a) stashed as per-cell engine state
across the half-step, or (b) recomputed as the curl-H sum inside the magnetic half-step. **The
build chose (b)** — a stateless recompute of the curl-of-H inside `update_magnetic_field` keyed on
H^n updating that same H^n (no staleness; the loaded-μ energy test confirms it conserves, see the
build-status banner). See §6.

---

## §2 — THE NORMALIZATION (the sign-off item): A_I = I_cell / I_max

The dimensionless kernel argument is `A_I = I_cell / I_max` with:

```
I_max = ξ_topo · c = 124.3840330668883 A  ≈ 124.384 A   (units: amperes)
```

verified live: `XI_TOPO = e/ℓ_node = 4.1490047447053624e-07 C/m` (`constants.py:323-324`),
`C_0 = 299792458.0 m/s` (`constants.py:110`), `L_NODE = ħ/(m_e c) = 3.8615926772e-13 m`
(`constants.py:278`); product `= 124.3840330668883 A`, cross-check `e·c/ℓ_node` identical.
Units: `(C/m)·(m/s) = C/s = A`, so `A_I = I_cell/I_max` is `A/A` = dimensionless. **PASS.**

### The SCALAR threshold I_max is CLOSED (no free factor)

`I_max = ξ_topo·c` is fixed two independent ways: (1) canonically as the V→I, V_yield→I_max dual
of the varactor under the single Axiom-4 kernel (`relativistic-inductor.md:15,:18`,
clm-p5cf3t); (2) re-grounded by the rest-energy mapping
`E_0 = ½ L_0 I_max² = ½(ξ_topo⁻² m_0)(ξ_topo c)² = ½ m_0 c²` (`relativistic-inductor.md:28`).
No free factor lives in the constant itself.
**Classification (consistency-vs-emergence): the scalar I_max is DERIVED** (`node-up-small-large-signal.md:346`,
arithmetic-verified), but it carries `e` (via ξ_topo = e/ℓ_node), so any magnitude that rides on
it is an **α-echo at the value level** — see §7.

### The per-cell MAP I_cell → I_max is OPEN (the actual sign-off item)

The question "is I_max closed?" and "is the per-cell normalization closed?" have **opposite
answers.** The scalar is closed; the map from a Yee-cell H-circulation onto that scalar is NOT.
The corpus says so explicitly: the per-cell circulation → I_max map "must be derived, not
invented" (the open per-cell normalization item flagged in the route-C research doc; restated
here because it is the load-bearing gap).

The substrate reason it is open: `I_max` was defined against the **node** geometry
(`ξ_topo = e/ℓ_node` is a per-node line-charge density), i.e. the natural circulation contour is
the node perimeter `~ℓ_node`. But the engine's `dx` is a **computational grid scalar explicitly
NOT ℓ_node** (`fdtd_3d.py` carries `self.dx` as a free knob; the docstring distinguishes it from
`ℓ_node`). On a coarse continuum grid `dx ≫ ℓ_node`. The discrete `∮H·dℓ` is taken around a cell
face of perimeter `~dx`, so a naive `I_cell = curl_h · dx` measures the current threading a
`dx`-scale loop, while `I_max` is the threshold for a `ℓ_node`-scale loop. There is therefore an
**implicit geometric factor `(dx/ℓ_node)` (or its inverse, depending on contraction convention)**
between a Yee-cell circulation and the node-scale current `I_max` was defined against, and that
factor is NOT in the current `I_MAX = XI_TOPO * C_0`.

**Proposed substrate-native normalization (for Grant to ratify or reject):**

```
A_I  =  (I_cell / I_max) · (ℓ_node / dx)
     =  (curl_h_component · dx / I_max) · (ℓ_node / dx)
     =  curl_h_component · ℓ_node / I_max          [the dx cancels]
```

Justification (substrate-first-for-numbers): the physical observable the kernel responds to is
the **node-scale** circulation, not the grid-cell-scale one. The clean cancellation of `dx` is
the tell that the right normalization is contour-rescaled to the node: `A_I` should be
independent of the arbitrary computational grid spacing `dx`, because the saturation physics
lives at `ℓ_node`, not at the mesh. Equivalently, `A_I = curl_h · ℓ_node / I_max`
= `(∮H·dℓ on a node-perimeter loop) / I_max`. This makes `A_I` a pure phase-space reactance
coordinate (A46-clean), grid-invariant by construction.

**This is the §8 sign-off item #1.** I am NOT asserting this factor is canonical — it is a
substrate-first *proposal* with an honest "derive, don't invent" flag. The alternative (the
factor is genuinely 1, i.e. the curl is to be read at the lattice scale and the lattice IS the
node) is a coherent Grant-decidable position too; it just makes `A_I` grid-dependent, which I
flag as the cost.

### Why the OPEN factor is MOOT for the static-B / PVLAS verdict (but LIVE for any dynamic driver)

Under a static external B, `∂B/∂t = 0 ⟹` no Faraday EMF `⟹ I_circ = 0` exactly. So
`A_I = I_cell/I_max = 0` for **any finite normalization** — the per-cell factor multiplies zero.
The R3 result `A_I=0 ⟹ S_μ=1 ⟹ δn_μ=0` (`pvlas-static-b-verdict.md:37-43`, "analytically
exact, not a numerical fit") is therefore robust to the normalization gap. The factor only
becomes load-bearing for a **dynamic / large-signal I-keyed** driver, where `I_circ ≠ 0`. Grant
sign-off requested: confirm the open factor is moot for the PVLAS/static verdict but live for any
AC-onset driver.

---

## §3 — THE CONSTITUTIVE LAW + DIRECTION: μ_eff(A_I)

**Canonical choice for the VACUUM μ-grade: the relativistic INDUCTOR (μ INCREASES, diverges).**

```
μ_eff(A_I) = μ_0 / √(1 − A_I²)            (= μ_0 / S(A_I),  S(A_I) = √(1 − A_I²))
```

Cite: `relativistic-inductor.md:15` `L_eff(I) = L_0/√(1−(I/I_max)²)`, clm-p5cf3t; restated
`L_eff(I) = L_0/S(A_I)`, `A_I = I/I_max` at `pvlas-static-b-verdict.md:22` and
`node-up-small-large-signal.md:95`. Since `μ ∝ L`, `μ_eff = μ_0/√(1−A_I²)` — μ INCREASES and
diverges as `I → I_max` (the slew-rate-collapse / relativistic-mass-onset behavior,
`relativistic-inductor.md:32`).

**This is NOT genuinely ambiguous — the two forms are different SECTORS, not a fork.** The
DECREASING form `μ_eff = μ_0·√(1−(B/B_c)²)` (= μ_0·S) is real but is the **matter / Meissner**
kernel, keyed on the static applied `|B|` approaching `B_c` (inductor shorts → total
screening), implemented in `ave.axioms.scale_invariant.mu_eff` (`def mu_eff` at
scale_invariant.py:198 — re-pinned; the authoring cite `:42` is the module-docstring index, not
the definition), the sector-agnostic `√(1−(A/A_yield)²)` kernel. Its callers are all MATTER, all
B-amplitude-keyed by design:

- `superconductor.py:101` `meissner_mu_eff(...) → _si_mu_eff(B_applied, B_critical, ...)`
  (Meissner static-flux exclusion; SHOULD respond to static B; `_si_mu_eff` imported :44).
- `yang_mills.py:115` `mu = mu_eff(B_field, yield_limit=B_SNAP, clip=True)` (lattice-cell energy
  bound on static |B|).
- `bond_energy_solver.py:108-112` covalent-bond matter solver (`saturation_factor(V_local,V_SNAP)`
  on ε; `B_local = MU_0·|H|` on the matter μ path).

So at a given operating point there is no contradiction: the vacuum μ-grade (increasing, keyed on
circulation `I`) and the superconductor μ (decreasing, keyed on applied `|B|→B_c`) are different
kernels with different arguments in different sectors. `node-up-small-large-signal.md:383`
states this explicitly: `scale_invariant.mu_eff()` is "unchanged — it is the sector-agnostic
kernel used by genuine static-B MATTER callers ... correct as-is." **Direction verdict: vacuum
μ-grade = μ_0/√(1−A_I²) (INCREASING). No fork at the value level.** (Sector-naming-hygiene
flag in §8 #3.)

---

## §4 — THE TWO LIMITS (the payoff): static transparency (EMERGENT) vs AC-onset loading

| Drive | Internal circulation | A_I | S_μ = √(1−A_I²) | μ_eff | Optical effect |
|---|---|---|---|---|---|
| **Static uniform B** (DC magnet) | ∂B/∂t=0 ⟹ I_circ=0 | 0 | 1 | μ_0 | **transparent** (δn_μ=0) |
| **Propagating / current-carrying B** | I_circ ≠ 0 | >0 | <1 | μ_0/S > μ_0 | **μ loads** (AC-onset) |

**Static-B transparency is EMERGENT, not hard-coded.** Because the observable is `∮H·dℓ` and a
static uniform B threads zero net circulation through any interior cell (`curl H = 0` for a
source-free static field), `I_cell = 0` falls out of the discrete curl identically — the code
never special-cases "static B → transparent." This is the substrate reason the PVLAS-class
static-B null is *categorical* and field-strength-independent (`pvlas-static-b-verdict.md:41,:89-93`):
AVE predicts ZERO static-B vacuum birefringence at ANY field strength, a clean falsifier (a
detection at the QED level would falsify it).

**AC-onset is the forward prediction.** A *propagating* or *current-carrying* B has
`I_circ ≠ 0`, so `A_I > 0` and `μ` loads. This is the structurally-distinct AVE signature: μ
turns on with **circulation rate**, not field magnitude.

**E-side duality (one Axiom-4 law, two sectors).** The ε-grade is the **varactor**, keyed on the
potential variable `V ∝ E`: a static (or DC-biased) electric field IS a real operating-point
bias and DOES load the capacitor — `A_V = |E|/V_yield > 0 ⟹ S_ε < 1 ⟹` birefringent
(`node-up-small-large-signal.md:202-204` "a static E is a real operating-point bias for the
V-keyed varactor — it loads"; `pvlas-static-b-verdict.md:96` "the real test is the E-route"). The
asymmetry — **static E loads ε but static B does not load μ** — is precisely the
**capacitor/inductor duality** under a single Axiom-4 kernel: the capacitor responds to a
potential (which a DC field supplies), the inductor responds to a current/rate (which a DC field
does not). `relativistic-inductor.md:18`: both are "projections of the single Axiom 4 kernel onto
the electric and magnetic sectors." This duality, not a symmetry-breaking posit, is what makes
the E-route the live birefringence test and the static-B route a categorical null.

---

## §5 — THE BIREFRINGENCE SPLIT: what circulation-keying needs to produce par-vs-perp

A static external B gives `A_I = 0` uniformly ⟹ `S_μ = 1` everywhere ⟹ an **isotropic null**,
NO directional split (`pvlas-static-b-verdict.md:37-43`). To produce a deviatoric par-vs-perp
**split** (the optical signature), circulation-keying needs a **sustained, direction-selective
internal circulation** — a nonzero `A_I` with a preferred axis, i.e. `∂B/∂t ≠ 0` driving
*anisotropic* vacuum circulation. A DC magnet cannot supply this; this is the substrate reason
the birefringence falsifier is the E-route (R2), not the static-B route (R3).

The split structure to match is the bench's **deviatoric** form: under a linearly-polarized pump
the scalar Axiom-4 kernel becomes a uniaxial probe (optic axis ∥ pump), and the leading
differential is `δn_bir = n_par − n_perp → −½ A²` — exactly **2× the isotropic −¼ A² shift**.
The isotropic index shift is `δn = (1−A²)^¼ − 1 ≈ −¼ A²` (`bench/birefringence.py:8`,
coefficient `−1/4` tagged MANIFESTATION at :41); the deviatoric −½ A² lives at the node level in
the SPLIT of the `L_i·C_i` pairs on the ε/C side: `vacuum_node_circuit.py` strains only `lC`
(the metric-varactor sector that carries the index, `deviatoric` classmethod at :162, cite
`vacuum-birefringence-e4.md:12` at :168) so `c_x ≠ c_y` = birefringence; the isotropic regime
(`isotropic_saturated` at :144-159) co-scales L and C equally ⟹ `Z = Z_0`, `Γ = 0`, no split.

For a circulation-keyed **μ** to produce a deviatoric split, the same logic must apply on the
**lL** (inductive) side: an anisotropic `A_I(direction)` straining `lL_x ≠ lL_y`, giving
`c_x ≠ c_y` from the μ sector. The current node-circuit `deviatoric` strains only `lC` (ε);
a μ-route split would need the dual deviatoric on `lL` — which only a direction-selective
sustained circulation can drive.

**3D-srs wash-out caveat (may need a 1D read).** A 3D FDTD on the 2-transverse-DOF srs lattice
averages over polarization directions; a genuine par-vs-perp split keyed on a *directional*
circulation can wash out in a 3D ensemble read the same way directional optical signatures do.
The bench's deviatoric form is read cleanest on a **1D / single-polarization** configuration
where "par" and "perp" are unambiguous axes. Recommend any μ-split test be designed as a 1D (or
fixed-polarization) read first, not a 3D-srs ensemble — flag for the test-design stage, not this
memo.

---

## §6 — CONSTRAINTS FOR THE BUILD

> ⚑ The `fdtd_3d.py` line cites in this section (`_compute_local_mu :222`, `mu_base :260`,
> energy `:407,:432`, dead-diagnostic `:249-250`) describe the **pre-build `00f1e97b` baseline**
> (free-EM μ linear, returning `mu_base`). The build has since landed: `_compute_local_mu` is now
> at `fdtd_3d.py:270` and DOES the circulation keying (no longer returns `mu_base`); the energy
> `u_m` sites are at `:553`/`:578`; the dead `B_local/B_SNAP` diagnostic was REPLACED by the A_I²
> peak diagnostic (constraint #1 §8 #5 actioned). These pre-build cites are retained for design
> provenance — see the BUILD-STATUS BANNER for the live sites.

1. **Vacuum-μ-grade-only sites.** A circulation-keyed μ touches ONLY the FDTD-private vacuum μ
   path: `fdtd_3d.py:_compute_local_mu` (:222) and its JIT twin `fdtd_3d_jax.py`
   `_compute_local_mu_kernel`. PRESERVE all four B-amplitude-keyed **matter** callers unchanged:
   `superconductor.meissner_mu_eff` (:101), `yang_mills` (:115/:162), `bond_energy_solver`
   (:108-112), and the shared kernel `ave.axioms.scale_invariant.mu_eff` itself (it stays
   B-amplitude-keyed for matter — `node-up-small-large-signal.md:383`). The architectural seam is
   already in place: the FDTD vacuum path no longer CALLS the shared kernel (it returns
   `mu_base` directly at `fdtd_3d.py:260`), so vacuum-μ and matter-μ are already in different code
   paths. A circulation-keyed vacuum μ is a *vacuum-path-private* change.

2. **DO NOT TOUCH the bound/κ-keyed μ engine.** The Cosserat **bound-resonator** μ is a separate,
   α-carrying engine keyed on internal **curvature κ** (bound circulation), NOT external |B| and
   NOT the free-EM circulation: `src/ave/topological/cosserat_field_3d.py` uses
   `A² = |eps|²/eps_yield² + |kappa|²/omega_yield²` (verified `:411`) and
   `KAPPA_CHIRAL_ELECTRON = ALPHA · KAPPA_TILDE_ELECTRON` (verified `:131`); the `A2_mu_base`
   /`A2_mu` lines re-verify at `:599`/`:605`. ⚑ CORRECTION: the file is at `ave/topological/`, NOT
   `ave/core/` — the earlier ":599/:605 STALE" note was a wrong-path artifact, not a moved file;
   at the correct path all four lines are live. This is the "bound/self-trapped circulation
   saturates μ at ANY frequency" engine the FDTD docstring delegates to — the bound-resonator μ,
   distinct
   from the free-EM vacuum μ-grade.

3. **Energy-method per-cell circulation storage.** The energy-method sites
   (`fdtd_3d.py:407,:432`, currently linear `½μ_0μ_r|H|²`) would need the same per-cell `I_cell`
   state if μ becomes nonlinear, because a post-hoc snapshot has no rate available (Blocker A).
   Under the current linear resolution this is moot; under a circulation-keyed refinement the
   per-cell circulation state must be stored, not recomputed from a snapshot.

4. **α-clean.** `A_I = I_cell/I_max` must be computed from `I_max = ξ_topo·c` (which carries `e`,
   hence α at the *value* level — §7) — but the FORM (the saturation onset structure) is α-free.
   Keep the structural test (does μ load with circulation? at what A_I onset?) separate from any
   magnitude that rides I_max, so the structural chord is not confounded with the α-echo.

5. **Energy-gate-live.** Any I-keyed μ driver must keep `H = T + V` conservation live over the
   recording window AND record the reactance pair (C-state `V_inc`/ω AND L-state `Φ_link`/ω_dot)
   per Rule-10 reactance-tracking — a single-phase snapshot cannot distinguish a static config
   from an oscillator caught at peak.

---

## §7 — HONEST SCOPE

The **magnitude** stays an α-echo: `I_max = ξ_topo·c` carries `e` (via `ξ_topo = e/ℓ_node`), so
any saturation threshold or differential coefficient that rides `I_max` inherits α at the value
level — the same α-echo family as the E-route OQ-1 ratio `7.5/α³ ≈ 1.93e7`
(`node-up-small-large-signal.md:216,:351,:364`). Per consistency-vs-emergence: a magnitude
derived through `I_max` is **CONSISTENCY / α-echo-at-value**, NOT a clean emergence claim — do
not headline it as a from-scratch number.

The **bankable AVE-distinct chord** is the **STRUCTURE**, not the magnitude:
(a) the categorical **static-B transparency** (δn_μ=0 at ANY field strength — a clean falsifier,
emergent from `∮H·dℓ=0`, not hard-coded); and
(b) the **AC-onset asymmetry** — μ loads with circulation *rate*, ε loads with potential, the
capacitor/inductor duality under one Axiom-4 law. These are categorical, structural, O(1)
predictions independent of the α-echo magnitude. That asymmetry + AC-onset structure is the
make-or-break forward prediction; the number is downstream and echoes α.

---

## §8 — FRAMING FORKS FOR GRANT (the explicit sign-off items)

1. **Per-cell normalization factor (the primary sign-off item).** Does the canonical
   `I_cell → A_I` map carry the proposed `(ℓ_node/dx)` rescaling — i.e.
   `A_I = curl_h·ℓ_node/I_max` (grid-invariant, node-scale, dx cancels) — OR is the factor
   genuinely 1 (read the curl at the lattice scale, `A_I = curl_h·dx/I_max`, grid-dependent)?
   Plumber-physical: is the saturation threshold `I_max` the current threading a **node-perimeter**
   loop (`~ℓ_node`), in which case a Yee-cell circulation must be contour-rescaled to the node;
   or is the lattice cell itself the node? This is "derive, don't invent" — I propose the
   node-rescaled form on substrate-first grounds (the physics lives at ℓ_node, A_I should not
   depend on an arbitrary mesh `dx`), but flag it as a proposal, not canon. **Moot for the
   static/PVLAS verdict** (`A_I=0` for any factor); **live for any AC-onset driver.**

2. **Saturation direction — confirm NO fork (verdict: no fork, but confirm).** Vacuum μ-grade =
   `μ_0/√(1−A_I²)` (INCREASING, relativistic inductor, `relativistic-inductor.md:15`). The
   DECREASING `μ_0·√(1−(B/B_c)²)` is the matter/Meissner kernel in a different sector
   (`scale_invariant.mu_eff`, `superconductor.py`), NOT the vacuum free-EM grade — so the two are
   not opposite at the same operating point. Confirm Grant agrees this is a sector distinction,
   not a value-level fork.

3. **Regime/sector decision — does this even land on the free-EM path?** The free-EM μ-channel
   is currently LINEAR by the VCA-R01 resolution (`fdtd_3d.py:260`, commit `4d0d6e5f`), because
   every wave a coarse Yee grid represents runs at ω ≪ ω_C so `S_μ→1` to machine precision. With
   `dx ≫ ℓ_node`, even a correctly-wired `I_cell` gives `A_I ~ 1e-8` for representative waves — so
   a circulation-keyed free-EM μ never saturates on this grid (consistent with the linear
   conclusion). So: is `I_cell` intended for **(a)** the free-EM path (which would re-introduce
   the saturation VCA-R01 deliberately removed, and which never fires on a coarse grid anyway), or
   **(b)** the separate dispersive-μ(ω) / bound-circulation workstream the docstring routes to the
   Cosserat κ-keyed path? These are different reviews. My read: the observable is correct and
   substrate-native, but on the free-EM grid it is a *latent* capability (zero effect at
   representable ω), and the *active* circulation-saturation already lives in the bound κ-keyed
   Cosserat engine. Grant decides whether route-C step-1 is scoping the latent free-EM channel or
   the active bound channel.

4. **Sector-naming hygiene (minor, flag-don't-fix).** `scale_invariant.mu_eff` (μ_0·S,
   DECREASING, matter) and the vacuum relativistic-inductor (μ_0/S, INCREASING) share the bare
   name "μ_eff"/"permeability." They are physically opposite directions for different sectors —
   the same class of cross-sector misread VCA-R01 was. Recommend a sector-header docstring guard
   on `scale_invariant.mu_eff` (NOT a rename) before any I-keyed vacuum-μ code lands nearby.

5. **Dead diagnostic block (minor, flag-don't-fix).** `fdtd_3d.py:249-250` computes
   `B_local = μ_0·|H|`, `ratio_sq = (B_local/b_yield)²` — a dead-but-retained diagnostic that
   keys on `B_SNAP`, the very scale `node-up-small-large-signal.md` says is NOT the μ-kernel
   argument. It is a stale-read trap for future auditors. Recommend the implementer annotate it
   harder or drop it (Grant call).

6. **B-yield-scale fork (carried-open, untouched by this memo).** Two corpus magnetic-yield
   scales disagree by ~5×: `B_SNAP = 1.89e9 T` (energy-density-matched) vs `E_yield/c ≈ 3.77e8 T`
   (ε-proxy via cB↔E duality), ratio ≈ 5.0 (`pvlas-static-b-verdict.md:56-62`, ⚑FLAG, unresolved).
   This does NOT touch the R3 δn_μ=0 verdict (A_I=0 regardless of which B-scale) NOR the
   circulation observable (which keys on I_max, not B_SNAP), but it remains load-bearing for the
   matter callers (`yang_mills`, `bond_energy_solver`) and is a standing Grant decision.

---

## Verification ledger (verify-before-cite, all grepped on HEAD @ 00f1e97b)

| Claim | Source | Status on HEAD |
|---|---|---|
| I_max = ξ_topo·c = 124.3840330668883 A | `constants.py:110,278,323-324` + live compute | VERIFIED |
| curl_h discrete ∮H·dℓ | `fdtd_3d.py:332,337,342` | VERIFIED (verbatim) |
| free-EM μ returns mu_base (linear) | `fdtd_3d.py:260` | VERIFIED |
| L_eff = L_0/√(1−(I/I_max)²), I_max=ξ_topo·c | `relativistic-inductor.md:15,:18`, clm-p5cf3t | VERIFIED |
| ½L_0 I_max² = ½m_0c² rest-energy closure | `relativistic-inductor.md:28` | VERIFIED |
| A_I = I/I_max phase-space coord (A46) | `node-up-small-large-signal.md:95,:114,:118` | VERIFIED |
| static B: A_I=0 ⟹ S_μ=1 ⟹ δn_μ=0 exact | `pvlas-static-b-verdict.md:37-43` | VERIFIED |
| matter μ kernel (decreasing) = scale_invariant | `def mu_eff` at `scale_invariant.py:198` (authoring cite `:42` = docstring index); callers superconductor.py:44,:101 / yang_mills.py:115 / bond_energy_solver.py:108-112 | RE-PINNED (module at `ave.axioms.scale_invariant`, NOT core) |
| deviatoric −½A² split, ε/lC only | `bench/birefringence.py:8,:41`; `vacuum_node_circuit.py:144-168` | VERIFIED (birefringence at `src/ave/bench/`, NOT core) |
| κ-keyed bound μ, KAPPA_CHIRAL=ALPHA·KAPPA_TILDE | `src/ave/topological/cosserat_field_3d.py:131` (KAPPA_CHIRAL), `:411` (A_sq), `:599` (A2_mu_base), `:605` (A2_mu) | RE-VERIFIED at `topological/` path: ALL FOUR live — the earlier ":599/:605 STALE" note was itself the wrong-path artifact (file is `topological/`, not `core/`) |
| B-yield ~5× fork | `pvlas-static-b-verdict.md:56-62` | VERIFIED |

**Path corrections** (flag-don't-fix, re-verified during the fix-pass): the matter μ kernel
lives at `ave.axioms.scale_invariant` (not `ave.core.scale_invariant`), `def mu_eff` at `:198`
(authoring cite `:42` = the docstring index); the birefringence bench lives at
`src/ave/bench/birefringence.py` (not `src/ave/core/birefringence.py`); the κ-keyed bound-μ
engine lives at `src/ave/topological/cosserat_field_3d.py` (not `core/`), where `:131`/`:411`/
`:599`/`:605` are ALL live. ⚑ The earlier ":599/:605 STALE on this HEAD" claim was itself the
wrong-path artifact (the file was looked for under `core/`); at the correct `topological/` path
the lines verify. Verify-before-cite caught a cite-of-a-cite error in the design memo's own
ledger.
