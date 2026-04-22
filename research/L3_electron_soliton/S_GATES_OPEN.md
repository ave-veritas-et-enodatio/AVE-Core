# S-Gate Adjudications — Open Decisions for the AVE-Ideal Coupled Simulator

**Status:** **ALL RESOLVED 2026-04-22 (Grant)** — Phase II cleared to start.
**Parent plan:** `~/.claude/plans/document-list-for-next-chat-compressed-thunder.md`
**Phase I informant:** [41_cosserat_time_domain_validation.md](41_cosserat_time_domain_validation.md)

## RESOLVED DECISIONS

| Gate | Decision | Rationale |
|---|---|---|
| **S1** | **D** — `(V²/V_SNAP²)·_reflection_density(u, ω)` | Pure Axiom-4 reuse, zero new params, lowest SM/QED leakage risk |
| **S2** | **γ** — defer (not applicable under S1-D, which is phase-insensitive) | S1-D uses `\|V\|²` magnitude, not port phases, so port-pairing is moot |
| **S3** | **A** — no amplitude gate | Rule 6: "shouldn't modify without explicit axiom-derived justification; should fall out" — S1-D is already naturally gated via `_reflection_density`'s 1/S² structure |
| **S4** | **A** — natural units ρ = I_ω = 1 | Lattice-natural; SI calibration deferred post-Phase-III |
| **S5** | **B** — unified leapfrog | Same algorithm as Phase I Verlet (`cfl_dt` validated); K4 scatter+connect is already a leapfrog-style two-step; Vol 4 Ch 1 §sec:solver_selection justifies shared-dt time-domain |
| **S6** | **A** — soft/diagnostic (measure Q, don't enforce) | "It should fall out" — Rule 6 / AVE-native: let dynamics decide whether Q conserves (hard constraint would be a QED-style gauge postulate) |

**Phase II is now unblocked. File to create:
[`src/ave/topological/k4_cosserat_coupling.py`](../../src/ave/topological/k4_cosserat_coupling.py).**

---
*Original adjudication proposal below preserved for audit.*
---

---

## How to use this doc

For each S-gate below:
- Read the **Question**, the concrete **Options**, and the **Recommendation**.
- Either **approve the recommendation**, **pick a different option**, or
  say "research more" and I'll launch targeted investigation before the
  next session.
- Most gates are **reversible** — if Phase III data shows the choice was
  wrong, we can swap it with a localized code change.
- Gates marked "⚠ baked in" are harder to revisit — chose carefully.

---

## S1 — Coupling Lagrangian form

### Question
What is the explicit form of the coupling term `L_coupling(V; u, ω)` that
lets the scalar K4 field and tensor Cosserat field talk to each other?

### Why this matters
This single term controls *every* K4↔Cosserat interaction: how a
high-amplitude photon drives the Cosserat strain (→ electron formation),
and how the Cosserat shell modulates the K4 impedance (→ TIR mirror).
If the form is wrong, nothing else works.

### Options

**Option A — Scalar amplitude × rotational energy density** (simplest, empirical):
```
L_c = κ_A · |V|² · (α_u · |strain(u, ω)|² + α_ω · |curvature(ω)|²)
```
- Physics: the scalar amplitude GATES the Cosserat stiffness. Higher |V|
  → photon locally stiffens the lattice → ω responds.
- Free parameters: κ_A, α_u, α_ω (3 scalars).
- Axiom compliance: ✓ scalar, rotation-invariant. No gauge structure imposed.
- Rule-6 risk: LOW — this is an ad-hoc coupling, not a QED import.

**Option B — Gauge-like coupling** (QED-analog):
```
L_c = −e_eff · V · (u, ω)-current
```
- Physics: mimics the minimal coupling `A_μ · j^μ` of QED, treating V
  as a gauge potential and (u, ω) derivatives as a current.
- Free parameters: e_eff (1 scalar), but imports the whole minimal-coupling
  algebraic structure.
- Axiom compliance: ? — no axiom mandates a U(1) gauge current.
- Rule-6 risk: **HIGH** — this is explicitly QED-like and would be hard
  to defend as "axiom-derived, not SM-imported".

**Option C — Topological helicity coupling**:
```
L_c = κ_H · V · (A · B)_ω
```
where `(A · B)_ω` is the helicity density of the ω field (ω · ∇×ω type).
- Physics: the scalar field sources Cosserat helicity (and vice versa).
- Free parameters: κ_H (1 scalar).
- Axiom compliance: ✓ — Axiom 2 ([Q] ≡ [L]) naturally connects scalar
  linking to rotational helicity.
- Rule-6 risk: LOW — native topological construct.

**Option D — Built from existing `_s11_density` / `_reflection_density`**:
```
L_c = (V² / V_SNAP²) · _reflection_density(u, ω)
```
- Physics: the already-Axiom-4-derived reflection energy is amplitude-
  modulated by |V|². Re-uses the existing machinery without introducing
  new coefficients.
- Free parameters: ZERO new coefficients (inherits from `omega_yield`,
  `epsilon_yield`).
- Axiom compliance: ✓✓ — directly Axiom 4.
- Rule-6 risk: LOWEST — no new imports, pure reuse of existing AVE
  operators.

### Recommendation: **Option D** (baked-in reuse of `_reflection_density`)

**Reasoning:**
- Lowest parameter count (0 new).
- Directly tied to Axiom 4 (the only axiom that NEEDS the coupling to
  exist, per the TIR mechanism of §37).
- Pure code reuse — we already have
  [`_reflection_density`](../../src/ave/topological/cosserat_field_3d.py)
  and it produces exactly the Γ vs amplitude curve we want.
- If this fails in Phase III, we can swap to Option A (adds 3 free
  parameters) or C (adds 1) without rewriting architecture.

### Reversibility
✓ reversible — the coupling enters at one place
(`k4_cosserat_coupling.py`). Swapping Option D → A requires editing ~30
lines.

### Data that would help decide
Phase III results (try D first; if it converges on (R/r) ≈ φ², done;
if not, try A; if A fails, try C).

---

## S2 — Port-quadrature pairing

### Question
The K4 has 4 ports `{0, 1, 2, 3}`. In the `V → ω` coupling direction,
we need to map port patterns to rotational axes. Which two ports form
the "real" quadrature pair and which form the "imaginary" pair?

### Why this matters
This determines which K4 scalar mode drives which Cosserat rotational
axis — i.e., the photon-polarization ↔ electron-spin-axis mapping.

### Options

**Option α — {0,1}/{2,3} pairing** (current Phase B port-weight convention):
- Port 2,3 are "forward" for +x̂ propagation (T₂ amplitude on these two)
- Port 0,1 are "backward" for +x̂
- Mapping: (forward ports, backward ports) → (Re, Im) of ω_⊥

**Option β — {0,2}/{1,3} pairing** (anti-diamond chirality convention):
- Mixes forward+backward ports per quadrature
- May or may not respect the K4 bipartite A/B structure

**Option γ — defer; let the coupling term decide**:
- Option D (S1 recommendation) doesn't reference port indices at all — it
  couples scalar `|V|²` (a magnitude, not a phase) to `_reflection_density`.
- Port pairing becomes moot for the specific coupling we've chosen.

### Recommendation: **Option γ (defer)**

**Reasoning:** S1 Option D doesn't reference port phases, so S2 becomes
moot until/unless we swap to a phase-sensitive coupling (Options A, B, C
of S1). If that swap happens, we re-open S2.

### Reversibility
✓ — orthogonal to other gates.

---

## S3 — Saturation-gate threshold `A²_c`

### Question
At what photon amplitude does the V→(u,ω) coupling TURN ON?

### Why this matters
Controls when a photon starts "exciting" the Cosserat field. Too low:
every linear-regime photon leaks into the electron sector (unphysical).
Too high: photons have to be near rupture to interact (no electron
formation until A² → 1).

### Options

**Option A — No gate (`A²_c = 0`)**: coupling is always on, strength
scales smoothly with |V|². Matches S1 Option D (∝ V²·reflection density).

**Option B — Regime boundary (`A²_c = √(2α) ≈ 0.121`)**: coupling off
below the Regime I → II boundary, turns on in Regime II.

**Option C — Mid-Regime II (`A²_c = 1/2`)**: symmetric midpoint, coupling
off in passband, on when wave is clearly saturating.

**Option D — Regime III boundary (`A²_c = √3/2 ≈ 0.866`)**: coupling only
in Regime III (near-rupture); linear and moderate-amplitude photons pass
through unaffected.

### Recommendation: **Option A (no gate)** if we take S1 Option D

**Reasoning:** S1 Option D's coupling strength is `(V²/V_SNAP²)·_reflection_density`.
- `_reflection_density` already contains the Op3/Axiom-4 saturation
  structure — it's near zero in Regime I, rises in Regime II, diverges
  near Regime III (via 1/S² regulator).
- Multiplying by V²/V_SNAP² adds an amplitude envelope that further
  suppresses low-amplitude leakage.
- So the coupling is already AXIOMATICALLY GATED without a hard
  threshold. Adding one would be redundant.

If we take S1 Option A or C instead, then S3 Option B is recommended
(couple at Regime I → II boundary).

### Reversibility
✓ — single threshold value in the coupling function.

---

## S4 — Cosserat mass/speed parameters (ρ, I_ω)

### Question
What values should we use for the Cosserat translational inertia `ρ`
and rotational inertia `I_ω`?

### Why this matters (REFRAMED AFTER PHASE I)
Phase I revealed that in natural units with `G = G_c = γ = 1`:
- `c_R = √(γ/I_ω) = 1/√I_ω` — rotational band propagation speed
- `m² = 4·G_c/I_ω = 4/I_ω` — rotational mass gap
- Both scale with `1/I_ω`. So I_ω is ONE number that controls both.

This is NOT the speed of light (that's in the K4 sector). It's the
electron sector's characteristic scale.

### Options

**Option A — Natural units `ρ = I_ω = 1`**: all quantities dimensionless
in the simulator; calibration to SI happens post-Phase-III via the
electron mass measurement.

**Option B — Calibrate to Compton wavelength now**: pick I_ω such that
`m = 1/λ_C` in lattice units. Pre-commits to a specific dimensional
anchor.

**Option C — Calibrate to electron rest mass now**: pick I_ω such that
`m·ℏ·c = m_e·c²`. Same concern as B — commits to SI before we have
Phase III data.

### Recommendation: **Option A (natural units, defer calibration)**

**Reasoning:**
- Phase I already runs in these units cleanly.
- The SI calibration depends on the coupled-sim output (the electron
  soliton's measured R/r vs Ch 8 Golden Torus), which we don't have yet.
- Rule-6 / §39: α is calibration input; better to DEFER the
  dimensionful anchoring until we've seen the soliton, rather than
  force-fit.

### Reversibility
✓ — rho / I_omega are just constructor args.

---

## S5 — Integrator (operator-split vs unified Hamiltonian)

### Question
For the coupled K4 ⊗ Cosserat simulator, do we step:
- K4 step → Cosserat step → apply coupling → repeat (**operator-split**)
- or solve a single unified Hamiltonian with symplectic integration?

### Why this matters (REFRAMED AFTER PHASE I)
Phase I showed operator-split Verlet is sufficient for the linear
Cosserat regime (|ΔH/H| < 1% over many periods). But the FULL
potential (with Op10 + Hopf + saturation terms) blew up at linear CFL.
So the choice depends on which terms are active in the coupled run.

### Options

**Option A — Operator-split velocity-Verlet**: K4 uses its existing
scatter+connect (already step-like); Cosserat uses the Phase-I
`step()`; coupling applied as an additive force at each step. Simple,
backward-compatible, proven for linear Cosserat.

**Option B — Unified leapfrog with explicit coupling force**: single
`dt`, both sectors evolve via velocity-Verlet with the coupling term
contributing to both forces simultaneously. Still O(dt²) but more
accurate on energy conservation across the coupling.

**Option C — Symplectic (implicit midpoint)**: unconditionally stable,
energy-conserving to machine precision, but requires solving a nonlinear
system at each step (expensive).

### Recommendation: **Option B (unified leapfrog)**

**Reasoning:**
- Operator-split (Option A) has a coupling-order error that manifests
  as secular energy drift under strong coupling (Option D of S1 makes
  the coupling strong near A² ~ 1, exactly the regime we care about).
- Unified leapfrog is only marginally more complex — single dt, single
  accelerations-update per step.
- If Phase III shows this isn't enough, fall back to Option C.

### Reversibility
✓ — integrator is confined to `K4CosseratCoupledSim.step()`.

### Data that would help decide
Phase III: run with Option B, check |ΔH/H|. If < 5% over the capture
animation (~500 steps), done. If larger, escalate to Option C.

---

## S6 — Linking-number conservation (hard vs soft)

### Question
Axiom 2 says `[Q] ≡ [L]` (charge = linking number). In the coupled sim,
do we:
- **Hard constraint**: enforce `Q` conserved exactly (no pair-creation
  possible)?
- **Soft constraint**: allow Q to drift; measure it as a diagnostic; the
  dynamics decide whether it conserves?

### Why this matters
Hard constraint forbids pair production (electron-positron creation at
high-enough photon amplitude). That's a physical prediction: is there
pair production in AVE or not?

### Options

**Option A — Soft (diagnostic only)**: compute Q via
[`extract_crossing_count`](../../src/ave/topological/cosserat_field_3d.py)
at each frame, report drift. Don't enforce.

**Option B — Hard (projection after each step)**: project (u, ω) back
onto the Q=original topological sector after every step. Mathematically
cleaner but computationally expensive.

**Option C — Hybrid**: soft by default, but flag when Q drifts by more
than ε and investigate whether it's physics (pair production onset) or
numerical (dispersive mode leakage).

### Recommendation: **Option A (soft / diagnostic)**

**Reasoning:**
- Physics first: let the dynamics decide. If Phase III shows Q drifts
  at saturation onset, that's an honest prediction about AVE admitting
  pair creation. If Q stays fixed, that's also a prediction.
- Rule-6 risk of Option B (hard): enforcing conservation is a GAUGE
  POSTULATE — it's what QED does for electric charge. We shouldn't
  import that without seeing AVE first choose it naturally.
- Soft is the simplest and preserves the most information.

### Reversibility
✓ — adding Option B's projection is straightforward if Phase III data
justifies it.

---

## Summary table — my recommended defaults

| Gate | Question | Recommendation | Reversibility |
|---|---|---|---|
| **S1** | Coupling Lagrangian form | **Option D** — `(V²/V_SNAP²)·_reflection_density` (reuse existing Axiom-4 machinery, 0 new params) | ✓ |
| **S2** | Port-quadrature pairing | **γ — defer** (moot under S1 D) | ✓ |
| **S3** | A²_c saturation gate | **A — no gate** (already axiomatically gated by S1 D) | ✓ |
| **S4** | Cosserat `ρ, I_ω` | **A — natural units `ρ = I_ω = 1`**, defer SI calibration | ✓ |
| **S5** | Integrator | **B — unified leapfrog** with coupled forces | ✓ |
| **S6** | Q conservation | **A — soft (diagnostic)**; let dynamics decide | ✓ |

If you approve all six defaults, Phase II can begin immediately with:
- 1 new file: `src/ave/topological/k4_cosserat_coupling.py`
- ~300 lines of glue code
- Estimated 3–5 days to a working Phase II module + 2 days for the
  minimal validation test.

If you want to override any, tell me which gate and which option (or
describe a different option you want — e.g. "S1 = my own idea XYZ").

---

## Non-gate flagged items (for later)

These aren't S-gate decisions but are flagged forward from Phase I /
Phase A-C:

- **F1** — Factor-of-2 mass correction (`m² = 4·G_c/I_ω`, not `2·G_c/I_ω`).
  Verify Ch 8 Golden Torus Q_H derivation is consistent or flag as
  corpus-level correction.
- **F2** — Ground-state stability under full-potential Verlet blew up
  (Phase I T2 original attempt). Multi-rate integrator or tighter dt
  needed for Phase III; out of scope for S-gates.
- **F3** — α as calibration (§39) — this affects how Phase III results
  map to SI. Not blocking S-gates but relevant to interpretation.
- **F4** — Manuscript updates for the Phase-I mass finding. The
  statement "Cosserat sector is natively massive via G_c" should
  appear somewhere in Vol 1; currently it's only in 41_.

None of F1-F4 block Phase II.
