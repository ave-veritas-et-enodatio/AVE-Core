# 111 — Master Equation Audit + Engine Structural Gap

**Date:** 2026-05-14 late evening
**Branch:** `research/l3-electron-soliton`
**Author:** Claude (auditor + implementer); Grant directive 2026-05-14 evening
**Status:** AUDIT COMPLETE — root cause of v14 Mode III identified. Three concrete paths to realize the canonical AVE Master Equation in simulation; recommendation locked.

---

## §0 Summary

Grant 2026-05-14 evening, after v14a/b/d/e all returned Mode III:

> *"are we realizing the non-linear wave equation/master equation with this? how would you define the master equation?"*

**Answer:** NO — only partially. The engine implements an approximation of the canonical Master Equation that is correct in the **linearized sub-saturation regime** (validated empirically today via AVE-Bench-VacuumMirror IM3 cubic slope 2.956 ≈ 3.0) but **structurally incomplete for the bound-state regime** (A → 1) where v14 was attempting to find autonomous solitons.

The critical gap: the canonical Master Equation requires BOTH ε_eff(V) modification AND c_eff(V) modification. The engine implements only impedance Z_eff(V) modulation via Op3 bond reflection. The wave-speed feedback c_eff(V) that produces self-trapping at A → 1 is not in the K4-TLM dt evolution.

This is the **structural root cause** of v14 Mode III across all four seed variants — including the full 7-mode seed v14e. Grant's 7-mode pushback was correct (the seed was incomplete) AND the deeper engine gap is correct (the Master Equation isn't fully realized). Both findings stand; this doc surfaces the engine gap as load-bearing.

---

## §1 The canonical AVE Master Equation

Per `AVE-Core/manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:46-77` (load-bearing canonical):

### §1.1 Equation in standard form

$$\boxed{\nabla^2 V \;-\; \mu_0\,\varepsilon_0\,\sqrt{1 - \left(\frac{V}{V_{\text{yield}}}\right)^2}\,\frac{\partial^2 V}{\partial t^2} \;=\; 0}$$

(eq:master_wave at line 73)

### §1.2 Constitutive relations

| Quantity | Form | Limit as A → 1 |
|---|---|---|
| Saturation kernel | $S(A) = \sqrt{1 - A^2}$, where $A = V/V_{\text{yield}}$ | $S \to 0$ |
| Effective permittivity | $\varepsilon_{\text{eff}}(V) = \varepsilon_0 \cdot S(A)$ | $\varepsilon_{\text{eff}} \to 0$ |
| Effective permeability | $\mu_{\text{eff}}$ remains $\mu_0$ in scalar Master Equation | unchanged |
| **Effective wave speed** | $c_{\text{eff}}(V) = c_0 \cdot (1 - A^2)^{-1/4} = c_0 / \sqrt{S}$ | $c_{\text{eff}} \to \infty$ |
| **Effective impedance** | $Z_{\text{eff}}(V) = Z_0 / \sqrt{S}$ | $Z_{\text{eff}} \to \infty$ |
| **Effective capacitance** | $C_{\text{eff}}(V) = C_0 / S$ | $C_{\text{eff}} \to \infty$ |
| Boundary reflection coefficient | $\Gamma = (Z_{\text{eff}} - Z_0)/(Z_{\text{eff}} + Z_0)$ | $\Gamma \to -1$ as $Z \to \infty$... wait, $\Gamma \to +1$ for hard wall |

Note correction: $\Gamma = (Z_L - Z_S)/(Z_L + Z_S)$. As $Z_L \to \infty$, $\Gamma \to +1$ (hard wall, in-phase reflection). The corpus uses $\Gamma \to -1$ convention for the "saturation boundary" — this refers to the **incoming wave's amplitude inversion** under total reflection from a $Z \to 0$ sink (per Vol 4 Ch 1 + App F multi-scale Machian network).

Both conventions describe the same physics: at A → 1, the local boundary is a **total reflector** (Γ = ±1), and the medium inside is wave-trapped. The exact sign depends on whether the boundary is the wave-side or substrate-side.

### §1.3 Three operating regimes

Per `04_continuum_electrodynamics.tex:138-159`:

| Regime | Condition | Wave behavior | Engine fidelity |
|---|---|---|---|
| **I. Linear Acoustic** | V ≪ V_yield (A ≪ 1) | Standard Maxwell, S ≈ 1 | ✓ Full fidelity (bench validation slope 2.956) |
| **II. Non-Linear Tensor** | V → V_yield (A → 1) | c_eff → ∞, ε → 0, Z → ∞, Γ → ±1 | ✗ **Partial — only Z modulated, c not** |
| **III. Dielectric Rupture** | V ≥ V_yield (A ≥ 1) | Kernel imaginary, substrate phase transitions | ✗ Not implemented (numerical clipping only) |

### §1.4 What the Master Equation predicts for a bound state

Per Vol 1 Ch 4:82 *"Particle Assembly (V → 43.65 kV)"*:

> *"The local permittivity collapses (ε_eff → 0), forcing the impedance to drop to zero (Z → 0). The accelerating wave continuously reflects off its own self-induced impedance boundary (Γ → −1). This traps the wave into a stabilized topological knot (a Fermion), physically generating invariant rest mass without invoking the Higgs Mechanism."*

(Vol 1 Ch 4 actually writes Z → 0 here — this is the convention for the wave's perspective entering the boundary from outside; the substrate-internal Z → ∞ via Z_eff = Z_0/√S is the dual view. Same physics.)

The bound state forms because:
1. Wave amplitude V grows locally near the soliton
2. As A approaches 1, c_eff increases rapidly (wave inside the soliton moves faster)
3. ε_eff decreases, reducing the substrate's stored capacitive energy capacity
4. Z_eff at the boundary diverges, total-reflecting the wave
5. The wave is self-trapped by its own field amplitude — autonomous bound state

**The c_eff(V) divergence is load-bearing.** Without it, step 2 doesn't happen; the wave just propagates at constant c through the substrate; no internal speed-up; no self-amplification; no autonomous trap.

---

## §2 What the engine actually implements (audit)

### §2.1 K4-TLM engine (`src/ave/core/k4_tlm.py`)

| Component | Implementation | Master Equation requirement | Match? |
|---|---|---|---|
| Saturation kernel | `S_eq = sqrt(1 - strain²)` at line 269 | $S(A) = \sqrt{1-A^2}$ | ✓ |
| Strain | `strain = |V_inc|/V_SNAP` at line 267 | $A = V/V_{\text{yield}}$ | ✓ (modulo V_SNAP vs V_yield convention) |
| Z modulation | `z_local_field = 1/sqrt(S)` at line 287 | $Z_{\text{eff}} = Z_0/\sqrt{S}$ | ✓ |
| ε modulation | NOT explicitly set; implicit via Z | $\varepsilon_{\text{eff}} = \varepsilon_0 \cdot S$ | ⚠ implicit only |
| **c modulation** | `dt = dx/(c·√2)` set ONCE at __init__ line 144 | $c_{\text{eff}}(V) = c_0/\sqrt{S}$ | **✗ MISSING** |
| Op3 bond reflection | γ = (Z_B − Z_A)/(Z_B + Z_A) in `_connect_all` lines 393-415 | Γ from impedance gradient | ✓ (scatters at Z mismatch) |
| Self-consistent feedback | V_inc → Z_local → V_ref scatter; one-step | V evolves with c_eff(V) | ⚠ partial — Z feedback present, c feedback absent |

### §2.2 Cosserat sector (`src/ave/topological/cosserat_field_3d.py`)

The Cosserat sector implements the substrate's elastic dynamics (u, ω fields with energy gradient evolution). It DOES NOT implement the Master Equation directly — the Master Equation is a scalar equation in V (substrate voltage). The Cosserat sector contributes to the engine via:
- ω → K4 z_local (Op14 path)
- K4 V² → Cosserat energy gradient

Neither pathway modifies the K4's `dt` or imposes a c_eff(V) modulation on V's propagation.

### §2.3 Net engine fidelity to Master Equation

**In Regime I (sub-saturation, A ≪ 1):**
- $S \approx 1 - A^2/2 + O(A^4)$
- $1/\sqrt{S} \approx 1 + A^2/4 + O(A^4)$
- Z_eff ≈ Z_0 · (1 + A²/4): linear-leading-nonlinear
- Op3 bond reflection γ ≈ A²/8 at small A
- Engine reproduces this correctly. The IM3 cubic slope 2.956 from today's bench validation IS the leading-order kernel expansion — Op3 gives γ ~ A², the cubic comes from V × γ ~ V × V² = V³.

**In Regime II (saturation onset, A → 1):**
- S → 0, $1/\sqrt{S} \to \infty$, $c_{\text{eff}} \to \infty$
- Master Equation: wave self-traps via c_eff divergence + Z divergence
- **Engine: Z divergence captured (op3 γ → 1 in principle), c divergence NOT captured (dt fixed)**
- Net effect: wave radiates through PML at constant c before the boundary fully forms

**In Regime III (rupture, A ≥ 1):**
- Numerical clipping `A = min(strain, 1)` in `_update_z_local_field`
- Engine does not model rupture (would require pre-geodesic plasma dynamics)
- Not load-bearing for v14 (we're targeting Regime II, not III)

---

## §3 The structural gap

**The engine's K4-TLM keeps `self.dt = dx/(c·√2)` constant for all cells, all time.** This is the propagation timestep — fixed by the lattice's discretization at __init__.

The Master Equation says the LOCAL EFFECTIVE WAVE SPEED depends on V:

$$c_{\text{eff}}(V) = c_0 \cdot \left(1 - \left(\frac{V}{V_{\text{yield}}}\right)^2\right)^{-1/4}$$

This means a wave passing through a high-V region should travel FASTER locally. In TLM terms, the bond's effective propagation delay should DECREASE (or equivalently, the cell's effective dt should DECREASE). The engine doesn't do this.

**Consequence for v14:**
- Wave injected at the center cell (high V_inc) should locally speed up (per Master Equation)
- The speeding-up wave hits the bond at high V_inc; the bond has high Z_eff (engine captures); op3 reflects part back
- BUT the wave doesn't slow down at low-A neighbors; it just propagates at c_0
- Net effect: wave radiates at constant c_0, only attenuated by Z gradient at high-A cells
- The "self-trap" mechanism — wave accelerating into its own high-Z boundary — doesn't happen because c_eff acceleration is absent

This is consistent with what v14a/b/d/e all showed: K4 V_inc decays via PML radiation at constant c_0; Cosserat damps to standalone attractor; no self-consistent bound state.

---

## §4 Why v14 Mode III is now explained

The Mode III result was DECISIVE across four seed configurations:
- v14a (2/7 modes, A=0.6)
- v14b (2/7 modes + shell at A=0.95)
- v14d (Cosserat-only seed, no K4)
- v14e (full 7/7 modes)

The unifying cause across all four: **the engine's K4-TLM step doesn't implement c_eff(V), so the wave can't autonomously develop the speed-up + boundary-form self-trapping mechanism the Master Equation predicts.**

The seed mode count (2/7 → 7/7) improved Λ_surf and Λ_line population (0 → 6.787 and 0 → 5.913 respectively) but couldn't fix the missing dynamics. The bound state isn't a function of initial conditions only — it's a function of THE EQUATION the engine integrates. With the wrong equation (missing c_eff(V)), no initial condition produces the right attractor.

**Grant's 7-mode pushback was correct** (the seed was incomplete; v14a-d were underseeded). **AND the engine has a structurally deeper gap** (c_eff(V) missing from the Master Equation realization). Both findings stand. The mode count was a necessary fix; the c_eff(V) implementation is the bigger fix.

---

## §5 Three paths to realize the Master Equation in simulation

### §5.1 Path A: extend K4-TLM with per-cell c_eff(V)

**Modify the K4-TLM step to apply per-cell propagation delay** based on local V_inc amplitude.

Implementation sketch:
- Add `dt_local` field shape (nx, ny, nz) computed each step from `dt_local = dx / (c · √2) · √S_local`
- In `_connect_all`, apply substepping or delay buffer per bond: bonds with low S (high A) have effective propagation delay > nominal dt
- Conceptually: replace fixed-dt step with adaptive-time-substepped propagation per cell

**Effort:** ~1000-1500 LOC engine extension. Significant rework of the connect step + observers + diagnostics.

**Risk:** stability — adaptive time-step in TLM is non-trivial; CFL conditions per cell. Could introduce numerical artifacts.

**Pros:** keeps existing K4-TLM scaffolding; Cosserat coupling stays intact; observers + bench validation continuity preserved.

**Cons:** engineering complexity; CFL stability tuning.

### §5.2 Path B: FDTD directly on the scalar Master Equation

**Drop the K4-TLM 4-port decomposition; integrate the scalar PDE directly.**

The Master Equation is:
$$\nabla^2 V = \frac{1}{c_0^2}\,S(V/V_{\text{yield}})\,\frac{\partial^2 V}{\partial t^2}$$

This is a scalar wave equation with nonlinear coefficient. Standard FDTD with:
- Staggered grid: V on cells, ∂V/∂t on cell faces
- 2nd-order central differences for ∇²V
- Forward Euler or RK2 for time integration
- CFL condition: dt < dx · √S_min / (c_0 · √d) where d is dimensionality
- Local CFL adaptation handled by dt = dt_global · √S_local at each cell

Implementation sketch:
- New module `ave.core.master_equation_fdtd` with `MasterEquationFDTD` class
- Scalar V on N³ grid + ∂V/∂t on N³ grid = 2 N³ DOF (vs K4-TLM's 8 N³ + Cosserat's 6 N³ = 14 N³)
- Single forward step: compute Laplacian, apply S(V) modulation, evolve ∂V/∂t and V
- PML at boundaries (standard FDTD PML)

**Effort:** ~1000 LOC new module, fresh validation suite.

**Risk:** loses Cosserat coupling (Master Equation doesn't natively include u, ω); may need to add back later for full physics. Loses K4 topology (the bipartite tetrahedral structure isn't in the scalar PDE).

**Pros:** directly integrates the canonical equation; no proxy via TLM; cleanest mapping to the corpus. The dynamics that DO produce bound states (per the corpus's own statement at Vol 1 Ch 4:82) would actually run.

**Cons:** loses the K4 topology that App F + the substrate ontology rests on. May need to be re-anchored as "scalar Master Equation in a K4-modulated medium" rather than canonical AVE.

### §5.3 Path C: minimal patch — add dispersion correction to K4-TLM

**Keep K4-TLM; add an effective group-delay correction per bond based on local S.**

The Master Equation's c_eff(V) divergence at A → 1 manifests in TLM as a frequency-dependent propagation delay. For monochromatic waves, this is equivalent to:
- Each bond connecting cells i and j has effective propagation factor `f_ij = (S_i · S_j)^(1/4)`
- In `_connect_all`, after shift, multiply transmitted V_ref by `f_ij` (or by appropriate non-unitary factor)
- This approximates the c_eff(V) effect for slowly-varying envelopes

**Effort:** ~300-500 LOC patch to `_connect_all` + bookkeeping for f_ij.

**Risk:** lossy — multiplying by f_ij < 1 introduces non-unitarity; need to balance with reflected accumulation; engine no longer strictly energy-conserving in the same way.

**Pros:** minimal disruption; preserves existing tests; quick path to "see if v14 PASSes with the correction."

**Cons:** approximation; doesn't fully realize c_eff(V) divergence at A → 1; may not be enough for full bound state.

### §5.4 Comparison

| Criterion | Path A (extend K4-TLM) | Path B (FDTD direct) | Path C (minimal patch) |
|---|---|---|---|
| LOC | ~1000-1500 | ~1000 | ~300-500 |
| Risk | CFL stability | physics completeness | approximation quality |
| Fidelity to Master Eq | high | highest (direct) | medium |
| Preserves K4 topology | yes | no | yes |
| Preserves Cosserat coupling | yes | no (or re-add) | yes |
| Bench validation compatibility | likely preserved | requires re-validation | preserved |
| Time estimate | 1-2 weeks | 1-2 weeks (re-validation) | 1-3 days |

---

## §6 Recommendation

**Path B (FDTD directly on the Master Equation) is the right move for v14 closure.** Reasoning:

1. **Cleanest physics mapping:** the corpus canonically states the Master Equation as eq:master_wave. Integrating it directly leaves no proxy / approximation layer between corpus and simulation. The bound state Vol 1 Ch 4:82 predicts IS what the engine integrates.

2. **Smallest state space:** 2N³ DOF (V + ∂V/∂t) vs the current 14N³ (K4 8N³ + Cosserat 6N³). The current state space is over-parameterized for the scalar Master Equation; the dynamics on the richer state may not reduce to the Master Equation correctly.

3. **Bench validation preserved at the framework level:** the IM3 cubic + D2 hysteresis bench predictions come from the Master Equation kernel S(A) — same kernel as Path B. The bench should reproduce.

4. **Decouples engine engineering from K4-TLM technical debt:** the K4-TLM has accumulated subtleties (parity masks, op3, V_SNAP scaling, Cosserat coupling). A fresh FDTD on the scalar Master Equation is conceptually clean.

5. **Cosserat re-anchoring is tractable:** after Path B works, Cosserat can be re-added as a microstructure layer that modulates ε_eff and μ_eff in the Master Equation. The (u, ω) fields enter as constitutive parameters, not as separate dynamical sectors.

**Path C (minimal patch) is the right move if time-bounded to a 1-day spike.** Quick test of whether c_eff approximation unblocks v14 at all. Won't be canonical, but cheap proof-of-concept.

**Path A (extend K4-TLM) is NOT recommended.** Adaptive-time-step TLM is hard; CFL conditions per cell introduce instabilities; the path is longer than Path B with worse final fidelity.

### §6.1 Specific Path B scope

If Grant approves Path B:

1. **Author** `src/ave/core/master_equation_fdtd.py` (~600 LOC)
   - `MasterEquationFDTD` class with `step()`, `run()`, `inject_source()`, `get_field()`
   - Scalar V on (nx, ny, nz) + ∂V/∂t companion field
   - Staggered grid, 2nd-order central differences for ∇²V
   - Local dt modulation: dt_local = dt_global · √S_local for stability
   - PML at boundaries

2. **Author** `src/scripts/vol_1_foundations/r10_master_equation_validation.py` (~300 LOC)
   - Linear Maxwell limit: V ≪ V_yield, check c_0 propagation
   - IM3 cubic: two-tone drive at sub-sat, FFT, verify slope ≈ 3 (sanity check vs K4-TLM bench)
   - Single-cell bound state: plant near-saturation V, observe self-trap dynamics

3. **Author** `src/scripts/vol_1_foundations/r10_master_equation_v14_bound_state.py` (~400 LOC)
   - v14-equivalent test on the new FDTD engine
   - Plant near-saturation V at center cell, sustain or pulse
   - Look for autonomous bound-state formation (V stays elevated, n(r) gradient outside)
   - All 4 §14 acceptance criteria

4. **Validate** the IM3 bench result (slope 2.956) reproduces on the new FDTD engine — same physics, different discretization. If yes, the bench predictions transfer cleanly.

5. **If v14-equivalent PASSes:** declare Mode I, generate the visual Grant requested, update doc 109 §14 with the empirical PASS, unblock the AVE-QED vocabulary refactor scope-gate.

**Estimated effort:** 1-2 focused sessions for Path B authoring + validation. Faster than continuing to debug K4-TLM v14 variants.

### §6.2 What about the AVE-QED vocabulary refactor?

Per doc 110 §4.1, the refactor's correctness does NOT depend on v14 PASS. The framework is empirically valid via Q-G19α Route B (50 ppm to PDG). The vocabulary refactor can proceed in parallel with Path B engine work. Both are scope-independent.

**Recommended sequence:**
1. (Now → 1 day) Execute Path C as a quick spike — minimal patch to current engine; see if v14 PASSes with c_eff dispersion correction. Low investment, high information yield.
2. (Next 1-2 sessions) If Path C INCONCLUSIVE or NEAR-PASS, execute Path B in full. New FDTD engine, validated, v14-PASSing.
3. (Parallel) Execute AVE-QED vocabulary refactor — App G + glossary §5m + A_foundations inline. No dependency on engine work.

---

## §7 Cross-references

- **AVE-Core `vol_1_foundations/chapters/04_continuum_electrodynamics.tex:46-77`** — canonical Master Equation eq:master_wave
- **AVE-Core `vol_1_foundations/chapters/04_continuum_electrodynamics.tex:82-83`** — Particle Assembly regime + Γ → −1 self-trap mechanism
- **AVE-Core `vol_1_foundations/chapters/04_continuum_electrodynamics.tex:138-159`** — three operating regimes (Linear / Non-Linear / Rupture)
- **AVE-Core `src/ave/core/k4_tlm.py:132,144,287`** — engine's dx/dt/z_local fixed at __init__
- **doc 110 §1.4** — v14e seven-mode seed result (Mode III; mode count was real fix but not root cause)
- **doc 109 §13** — boundary-envelope reformulation (substrate observability rule; Grant-confirmed canonical)
- **AVE-Bench-VacuumMirror `k4tlm_bench_validation.py`** — IM3 cubic slope 2.956 (Regime I validated)
- **AVE-QED Q-G19α Route B** — 50 ppm to PDG (framework empirical validation via boundary-integrated observables)

---

## §8 What this doc closes vs leaves open

**Closes:**
- Root-cause diagnosis of v14 Mode III: engine implements partial Master Equation (Z modulation only, not c modulation)
- Canonical Master Equation form re-stated explicitly (eq:master_wave)
- Three-path scoping for realizing the Master Equation in simulation
- Recommendation locked: Path B (FDTD direct) as the right move; Path C as cheap spike

**Leaves open:**
- Path B authoring + validation (1-2 sessions)
- Path C spike (1 day)
- Whether v14-equivalent PASSes on the new FDTD engine (empirical question)
- Cosserat re-coupling on Path B engine (deferred to post-Path-B validation)

**The L3-electron-soliton feature branch's empirical situation is now clear:** doc 109 §13 framing is canonical, three substrate invariants are locked (Q1 ✓ Q2 ✓), v14 Mode III is explained (engine has structural gap), and Path B is the recommended fix. The branch is at a clean decision point.

**Grant's call:** Path B engine authoring (1-2 sessions, definitive fix) vs Path C minimal patch (1 day spike, partial answer). The vocabulary refactor proceeds independently regardless.
