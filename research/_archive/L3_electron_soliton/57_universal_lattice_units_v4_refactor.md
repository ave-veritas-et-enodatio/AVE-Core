# 57 — Universal Lattice Units & Scale-Invariant Operators: v4 Refactor

**Status:** plan document, 2026-04-23. Scoped as the axiom-native structural refactor that R4 (the observer-bug patch per plan file `~/.claude/plans/review-the-collaboration-md-and-lexical-wombat.md` Phase 3.5 step 3 — remove `/α` from NodeResonance + BondObserver per [Vol 4 Ch 1:711](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L711) subatomic override) does not address. Doc 55_ is **SUPERSEDED** — its R3 reading applied macroscopic V_yield at subatomic scale.
**Trigger:** Grant's directive — "what's the most fundamental, AVE-first-principled, axiom-compliant implementation?" after the R4 patch plan.
**Relationship to Stage 6:**
  - **R4** is the near-term fix: revert Phase 2/3 observer `/α` bugs so existing engine ships with consistent observers. Unblocks Phase 4-6 on the current codebase. ~1 day.
  - **v4** (this doc) is the post-Stage-6 structural refactor: parameterize nothing, derive everything, store dimensionless r throughout, route every saturation/impedance call through canonical universal operators. ~2-3 weeks. Tracked as **FUTURE_WORK G-10**.

---

## 0. TL;DR

The engine's correct AVE-axiom-native state is **dimensionless `r = A/A_c`** everywhere, with `A_c` a **derived domain property** (not an engine parameter). Per Vol 1 Ch 6 and Ch 7, the same 22 universal operators govern physics at every scale; the engine should not need a `scale` construction parameter because scale invariance IS the axiomatic claim. The v4 refactor makes that claim true in the code.

**Two failures to fix, one invariant to enforce:**

1. **Hardcoded magic numbers** in [vacuum_engine.py:151-153](../../src/ave/topological/vacuum_engine.py#L151) (`_REGIME_I_BOUND_A2 = 2α`, `_REGIME_II_BOUND_A2 = 0.75`, `_RUPTURE_BOUND_A2 = 1.0`) and **hand-rolled saturation/impedance inline** at [k4_tlm.py:227-232, 256-259, 333-346](../../src/ave/core/k4_tlm.py#L227) — should all route through `universal_saturation`, `universal_dynamic_impedance`, `universal_reflection`, and a new `universal_regime_classifier` operator.
2. **Mixed-convention observer formulas** (A14) — three observers with three different A²_total computations. R4 patches the immediate bug; v4 routes all observers through a single-source-of-truth method on the engine that returns dimensionless r².
3. **Scale invariance invariant:** the same operator-level tests pass across subatomic (V_SNAP-based), macroscopic (V_yield-based), and gravitational (unitary-strain-based) domains. Committed as a cross-domain test suite that cannot silently regress.

---

## 1. What the corpus requires (canonical, cited)

### 1.1 The universal control parameter (Vol 1 Ch 7:12, 20)

> "Every physical domain in the AVE framework reduces to a single dimensionless control parameter `r = A/A_c`, where A is the local strain amplitude and A_c is the domain-specific critical threshold derived from the four axioms. The saturation operator `S(r) = √(1 − r²)` (Axiom 4) changes character at well-defined boundaries, partitioning all of physics into four universal regimes."

Regime boundaries (Vol 1 Ch 7:30-54) are in **r**, not A: `r_1 = √(2α)`, `r_2 = √3/2`, `r_3 = 1.0`. These are derived from the axioms themselves (Taylor expansion of S hits α at r_1; Q=2 avalanche at r_2; S=0 rupture at r_3).

### 1.2 Domain A_c catalog (Vol 1 Ch 7:93-233)

| Domain | A | A_c | r |
|---|---|---|---|
| EM (voltage, macroscopic) | V | `V_yield = √α · V_SNAP ≈ 43.65 kV` | `V/V_yield` |
| EM (voltage, subatomic override — Vol 4 Ch 1:711) | V | `V_SNAP ≈ 511 kV` | `V/V_SNAP` |
| Gravitational | ε₁₁ = 7GM/(c²r) | `1` (unitary strain) | `ε₁₁` |
| GW | h (strain amplitude) | `√α ≈ 0.0854` | `h/√α` |
| Magnetic | B | `B_snap ≈ 1.89×10⁹ T` | `B/B_snap` |
| Nuclear | d_sat/r_sep | `1` (Pauli wall) | `d_sat/r_sep` |
| BCS | T or B | `T_c` or `B_c0` | `T/T_c` |
| Galactic | g_N | `a_0 ≈ 1.2×10⁻¹⁰ m/s²` | `g_N/a_0` |
| Cosserat translational | ε | `ε_yield = 1` (unitary strain, gravity-analog) | `ε/ε_yield` |
| Cosserat rotational | κ = ∇ω | `ω_yield = π` (empirical placeholder) | `κ/ω_yield` |

**Vol 1 Ch 7:96 is emphatic:** *"A_c is derived from the four axioms — it is never a fitted or empirical parameter."* The engine's current Cosserat `ε_yield = 1` (gravity-analog) and `ω_yield = π` (empirical) are placeholders; v4 should either derive them from Axiom-1 geometry or explicitly document them as calibration constants pending derivation.

### 1.3 The 22 canonical universal operators (Vol 1 Ch 6:181-334)

Full list per Ch 6 summary box at line 334: "Twenty-Two Universal Operators (Z₀, S, Γ, and nineteen derived operators) are applied identically across 14 orders of magnitude in length scale."

Op1 Z (impedance) · Op2 S (saturation) · Op3 Γ (reflection) · Op4 pairwise U · Op5 Y→S · Op6 λ_min · Op7 FFT · Op8 packing Γ · Op9 steric Γ · Op10 junction projection loss · Op11 ∇× · Op12 ∇· · Op13 ◻² · Op14 Z_eff · Op15 r_v · Op16 c_shear · Op17 T² · Op18 ω_c · Op19 n · Op20 regime eigenvalue · Op21 Q phase transition · Op22 M avalanche.

Engine has 26 implementations (`universal_operators.py`) but call sites fragment between direct calls and the `scale_invariant.py` wrapper layer. v4 consolidates.

### 1.4 Pythagorean strain theorem (AVE-APU Vol 1 Ch 5:26-40)

> "V_total = √(V_lon² + V_gate²). This is the Pythagorean quadrature sum of two orthogonal field components. It follows from energy additivity of two perpendicular degrees of freedom — not from geometric intuition. The factor √2 does not appear because each component carries half the energy density of a single-axis field of magnitude V_total; the quadratic relationship is exact given the |E|² energy dependence."

**Requires same-normalization terms.** Summing `A²_K4_SNAP + A²_cos_yield` (mixed convention) is not what this theorem authorizes. Summing `r²_K4 + r²_cos` (both dimensionless, both relative to their domain A_c) IS what it authorizes.

### 1.5 Scale invariance is the claim, not a parameter (Vol 1 Ch 6:29-35, Vol 1 Ch 1:29)

> "The characteristic impedance Z = √(μ/ε) is the single structural invariant of the AVE framework. No scale-specific modifications, fitting parameters, or domain-dependent redefinitions are required. Every physical phenomenon in the derivation chain reduces to boundary conditions on this single operator."

And Vol 1 Ch 1:29: *"Absolute distance therefore does not exist as a physical parameter; ℓ_node is evaluated as the dimensionless integer 1."*

**Implication:** a `scale` construction parameter on the engine is **against the framework philosophy**. Instead, the engine should expose the correct operator interface; callers pass the domain-appropriate A_c at the saturation site. There is no global "macroscopic mode" vs "subatomic mode" — there are domain-appropriate A_c values per operator call.

This revises my earlier v4 sketch that proposed `VacuumEngine3D(scale="subatomic")`. **That was wrong.** The AVE-native pattern is per-call A_c specification, not a global scale.

---

## 2. What the current engine gets wrong

### 2.1 Inventory of violations

Per Agent A's code audit (full report in §13):

| File | Violation | Severity |
|---|---|---|
| [vacuum_engine.py:151-153](../../src/ave/topological/vacuum_engine.py#L151) | `_REGIME_I_BOUND_A2 = 2α` etc. — hardcoded float constants, not routed through a `universal_regime_classifier` operator | HIGH |
| [vacuum_engine.py:370-388](../../src/ave/topological/vacuum_engine.py#L370) | `RegimeClassifierObserver` sums `A²_K4 + A²_cos` — under Vol 4 Ch 1:711 subatomic override, both terms are canonical r² at the same operating scale, so the sum is a valid Pythagorean r²_total (not a bug). The issue v4 addresses: no single-source-of-truth method; three observers each reinvent the sum. | MEDIUM (architecture, not a bug — R4 fixes NodeResonance + BondObserver defects elsewhere) |
| [k4_tlm.py:227-232](../../src/ave/core/k4_tlm.py#L227) | `S_factor = np.sqrt(...)` inline saturation, duplicates `universal_saturation` | MEDIUM |
| [k4_tlm.py:232](../../src/ave/core/k4_tlm.py#L232) | `z_strained = 1.0 / max(sqrt(S), 1e-6)` inline, duplicates `universal_dynamic_impedance` | MEDIUM |
| [k4_tlm.py:256-259](../../src/ave/core/k4_tlm.py#L256) | Duplicate of 227-232 pattern | MEDIUM |
| [k4_tlm.py:333-346](../../src/ave/core/k4_tlm.py#L333) | `gamma = (z_B - z_A)/(z_B + z_A + eps); T = sqrt(1-gamma²)` inline, duplicates `universal_reflection` + `universal_power_transmission` | MEDIUM |
| [k4_cosserat_coupling.py:207-217](../../src/ave/topological/k4_cosserat_coupling.py#L207) | `A_sq_total = A_sq_k4 + A_sq_cos; clip to 1.0` — under subatomic override (Vol 4 Ch 1:711), the sum is canonical r²_total and the clip at 1.0 is the Ax4 Regime IV boundary. Not a mixed-convention bug under R4. v4 centralizes the call via `r_squared_total()` for maintainability, not to fix a defect. | LOW (architecture) |
| [cosserat_field_3d.py:234](../../src/ave/topological/cosserat_field_3d.py#L234) | `A_sq = eps_sq/ε_yield² + kappa_sq/ω_yield²` — Cosserat-internal, correctly normalized, but never cross-checked against the K4 side for convention match | LOW |
| [cosserat_field_3d.py:520-531](../../src/ave/topological/cosserat_field_3d.py#L520) | `G = G_c = γ = ρ = I_ω = 1.0, ε_yield = 1.0, ω_yield = π` — all empirical placeholders with no axiom derivation documented | MEDIUM |

### 2.2 NOT a violation (contra my earlier v4 sketch)

- **`V_SNAP` hardcoded as engine constant**: correct per Vol 4 Ch 1:711 subatomic override; engine IS subatomic-scale simulator. No `scale` parameter needed.
- **Cosserat `ε_yield = 1` (gravity-analog convention)**: defensible under Vol 1 Ch 7:138 gravity-row `A_c = unitary strain`. A TKI-derived alternative `ε_yield = √α` exists but the gravity-analog is a valid axiom-native choice.
- **`scale_invariant.py` defaults to V_SNAP; `saturation.py` defaults to V_YIELD**: correct layering. `scale_invariant` is the fundamental primitive (subatomic / Schwinger-native); `saturation` is the Axiom-4 macroscopic wrapper. Callers pick.

---

## 3. v4 Architecture

### 3.1 Design principles (derived from §1)

1. **Dimensionless r internally.** All regime classification, all saturation kernel calls, all impedance walls operate on `r = A/A_c`. Raw A (voltage, strain, curvature) may be stored as intermediate state but MUST be converted to r before the S kernel fires.
2. **No `scale` construction parameter.** The engine does not select "subatomic vs macroscopic mode." Per Vol 1 Ch 6:29-35, scale invariance is claimed, not configured. Each operator call provides its domain-appropriate A_c.
3. **Single-source-of-truth methods.** `engine.r_squared_total()` returns the dimensionless r² per Pythagorean theorem across all active sectors. All observers, impedance updates, and nucleation gates call this — none reinvent the sum.
4. **Universal operators route every call.** `universal_saturation`, `universal_dynamic_impedance`, `universal_reflection`, `universal_regime_classifier` (new) are the only code paths for these physics. Hand-rolled inline implementations are a code smell, not a shortcut.
5. **Cosserat moduli audit.** `G`, `γ`, `ρ`, `I_ω`, `ε_yield`, `ω_yield` — each either derived from Axiom 1 + ν_vac = 2/7 + K=2G with citation, or explicitly marked as "engineering placeholder pending calibration; see [S_GATES_OPEN.md S4](S_GATES_OPEN.md)."
6. **Cross-scale regression suite.** Tests that demonstrate the SAME operator implementations produce correct physics at subatomic (Schwinger), macroscopic (yield), gravitational (unitary strain), and BCS (T/T_c) scales. Any regression trips the gate.

### 3.2 Data model — r, not A

Current state variables in `K4Lattice3D`:

```python
self.V_inc[nx, ny, nz, 4]   # port voltages (dimensionful, V units)
self.V_ref[nx, ny, nz, 4]
self.Phi_link[nx, ny, nz, 4]  # Phase 3 flux linkage (dimensionful)
```

Current state in `CosseratField3D`:

```python
self.u[nx, ny, nz, 3]     # translational displacement
self.omega[nx, ny, nz, 3] # microrotation
```

**v4 does NOT change these low-level arrays.** Dimensionful storage is permitted per the manuscript (r is mandatory for the S kernel, not for the underlying wave-propagation solvers). What changes:

- **New methods** on `VacuumEngine3D` and derived observer helpers convert to r at the point of saturation-kernel or regime-classifier call.
- **Audit pass** — every call site that currently computes `A²` directly gets either replaced with a call to the engine method (centralized) or annotated with the explicit `A_c` it uses.

### 3.3 The single-source-of-truth method

```python
class VacuumEngine3D:
    def r_squared_K4(self) -> np.ndarray:
        """r² for K4 sector: (V/V_SNAP)² per Vol 4 Ch 1:711 subatomic override.

        Returns dimensionless [0, 1+] field shape (nx, ny, nz).
        The K4 sector's A_c under the subatomic convention IS V_SNAP.
        """
        V_sq = np.sum(self.k4.V_inc ** 2, axis=-1)
        return V_sq / (self.V_SNAP ** 2)

    def r_squared_cosserat(self) -> np.ndarray:
        """r² for Cosserat sector: ε²/ε_yield² + κ²/ω_yield² per _cosserat_A_squared.

        Returns dimensionless [0, 1+] field shape (nx, ny, nz).
        Cosserat's A_c values (ε_yield=1, ω_yield=π) are gravity-analog
        unitary-strain boundaries per Vol 1 Ch 7:138. Documented as
        calibration placeholders in cosserat_field_3d.py.
        """
        return _cosserat_A_squared(
            self.cos.u, self.cos.omega, self.cos.dx,
            self.cos.omega_yield, self.cos.epsilon_yield,
        )

    def r_squared_total(self) -> np.ndarray:
        """Pythagorean combination of orthogonal DoFs per AVE-APU Vol 1 Ch 5.

        r²_total = r²_K4 + r²_cos, both dimensionless in their domain's A_c.

        ALL observers, regime classifiers, and impedance updates use this
        method. No ad-hoc sums elsewhere in the engine.
        """
        return self.r_squared_K4() + self.r_squared_cosserat()

    def regime_at_each_site(self) -> np.ndarray:
        """Return Regime I-IV classification per site via universal_regime_classifier."""
        r_sq = self.r_squared_total()
        return universal_regime_classifier(r_sq)
```

**Required new operator in universal_operators.py:**

```python
class Regime(IntEnum):
    I_LINEAR = 0
    II_NONLINEAR = 1
    III_YIELD = 2
    IV_RUPTURED = 3

def universal_regime_classifier(r_sq):
    """Classify Regime I-IV at each site per Vol 1 Ch 7:30-54 boundaries.

    r² < 2α            → Regime I (linear)
    2α ≤ r² < 3/4       → Regime II (nonlinear)
    3/4 ≤ r² < 1        → Regime III (yield)
    r² ≥ 1              → Regime IV (ruptured)

    All boundaries are axiom-derived per Vol 1 Ch 7:41-53.
    """
    from ave.core.constants import ALPHA
    regime = np.full_like(r_sq, Regime.I_LINEAR, dtype=np.int32)
    regime[r_sq >= 2.0 * ALPHA] = Regime.II_NONLINEAR
    regime[r_sq >= 0.75] = Regime.III_YIELD
    regime[r_sq >= 1.0] = Regime.IV_RUPTURED
    return regime
```

### 3.4 Call-site consolidation

**Before (3 observers, 3 formulas — under R4 subatomic override):**

```python
# RegimeClassifierObserver._capture:
A2 = V_sq / V_SNAP² + A²_cos  # canonical r²_total under Vol 4 Ch 1:711 — correct

# NodeResonanceObserver._capture:
A2_yield = (V_sq / V_SNAP²) / α + A²_cos  # Phase 2 bug: applies macro /α at subatomic scale

# BondObserver._compute_A2_yield:
A2_yield = (V_sq / V_SNAP²) / α + A²_cos  # Phase 3 inherits the same bug
```

R4 (plan file step 3) removes the `/α` from NodeResonance + BondObserver. After R4 all three observers agree — same canonical r² per Vol 1 Ch 7:12 under subatomic V_yield = V_SNAP.

**After (v4, one method):**

```python
# Every observer:
r_sq = engine.r_squared_total()
```

**Before (k4_tlm.py inline):**

```python
# _scatter_all (lines 227-232):
S_factor = np.sqrt(np.maximum(0.0, 1.0 - np.minimum(strain, 1.0)**2))
z_strained = 1.0 / np.maximum(np.sqrt(S_factor), 1e-6)

# _connect_all (lines 333-346):
gamma = (z_B - z_A) / (z_B + z_A + eps)
T = np.sqrt(np.maximum(1.0 - gamma**2, 0.0))
```

**After:**

```python
# _scatter_all:
S_factor = universal_saturation(strain, V_SNAP)
z_strained = universal_dynamic_impedance(1.0, S_factor)

# _connect_all:
gamma = universal_reflection(z_A, z_B)
T = universal_power_transmission(z_A, z_B)  # or sqrt(1-gamma²) via op
```

### 3.5 Cosserat moduli audit deliverable

Per [Vol 1 Backmatter §"Postulates"](../../manuscript/backmatter/02_full_derivation_chain.tex), `ν_vac = 2/7` and `K = 2G` are REQUIRED. `G` itself is not given in closed form in the corpus; Agent B's research confirmed this. v4 delivers either:

**Option 1 — Derive from trace-reversal + Machian G:** `G = m_e c² / (ℓ_node³ · f(α))` for some explicit axiom-derivable function `f`. Requires a derivation doc. Estimated 2-3 days of research.

**Option 2 — Document as placeholder with explicit S-gate:** `G = 1` (natural unit placeholder pending derivation), with the caveat that predictions dependent on `G` (Cosserat mass gap, muon/tau mass ratios via coupling sectors per Vol 1 Backmatter lines 369-395) become calibration outputs rather than zero-parameter predictions.

Either way, the engine code gets an explicit comment block citing which option the team picked and why.

---

## 4. Phased implementation

### Phase v4.0 — Preparation (1 week, no code changes)

Deliverables:
- **Derivation doc** for `G`, `γ`, `ρ`, `I_ω`, `ε_yield`, `ω_yield` per §3.5 (Option 1 or explicit Option 2 placeholder acknowledgment)
- **v4 architecture doc** updated in this file's §3 with any refinements
- **Pre-registered predictions matrix** — every current prediction in `predictions.yaml` re-expressed in r-units where applicable
- **Audit of all universal operator call sites** — per §2.1 inventory, final list of files/lines to patch

No code touched yet. Grant reviews and approves the plan.

### Phase v4.1 — Universal regime classifier + engine methods (3-4 days)

Deliverables:
- New operator `universal_regime_classifier(r_sq) -> Regime[]` in [universal_operators.py](../../src/ave/core/universal_operators.py)
- Unit tests in [test_universal_operators.py](../../src/tests/test_universal_operators.py) — pin boundaries at `r² = {0, 2α, 0.75, 1.0, 1.5}`
- New methods `r_squared_K4()`, `r_squared_cosserat()`, `r_squared_total()`, `regime_at_each_site()` on `VacuumEngine3D`
- Unit tests pinning each method's behavior
- **Full regression pass** — all 954 existing tests still green (no behavior change yet; just added methods)

### Phase v4.2 — Observer consolidation (2-3 days)

Deliverables:
- `RegimeClassifierObserver._capture` → calls `engine.r_squared_total()` and `engine.regime_at_each_site()`
- `NodeResonanceObserver._capture` → same
- `BondObserver._compute_A2_yield` → same
- `_update_z_local_total` in [k4_cosserat_coupling.py](../../src/ave/topological/k4_cosserat_coupling.py) → uses `r_squared_total()` for the A² clipped value
- **Regression:** Phase 2-3 tests still pass; no observer mid-run drift from R4 patches (R4 and v4.2 are equivalent behavior-wise, v4.2 is architecturally centralized)

### Phase v4.3 — K4-TLM inline removal (2-3 days)

Deliverables:
- [k4_tlm.py:_scatter_all](../../src/ave/core/k4_tlm.py) refactored to call `universal_saturation`, `universal_dynamic_impedance`
- [k4_tlm.py:_connect_all](../../src/ave/core/k4_tlm.py) refactored to call `universal_reflection`, `universal_power_transmission`
- Magic numbers `_REGIME_*_BOUND_A2` in `vacuum_engine.py` deleted; `universal_regime_classifier` replaces their uses
- **Regression:** all 917+ K4 tests still pass; no numerical drift (universal operators are mathematically identical to inline implementations, plus or minus float round-off)

### Phase v4.4 — Cross-scale regression suite (3-4 days)

Deliverables:
- `src/tests/test_scale_invariance.py` — new file. Exercises the SAME observer methods across:
  - Subatomic: `A_c = V_SNAP`, checks regime classification at representative V/V_SNAP ratios
  - Macroscopic: `A_c = V_yield = √α·V_SNAP`, same checks at `V/V_yield`
  - Gravitational: `A_c = unitary strain`, test at ε₁₁ values matching Vol 1 Ch 7:147 benchmarks
  - BCS: `A_c = T_c`, test at `T/T_c` ratios
- Tests demonstrate the same `universal_saturation`, `universal_regime_classifier`, `universal_dynamic_impedance` calls produce the right regime across all 4 domains — same numerical code, different A_c.
- Documents the scale-invariance claim as a machine-checked property.

### Phase v4.5 — Documentation + handoff (2-3 days)

Deliverables:
- `docs/SCALE_INVARIANCE.md` — developer guide on calling universal operators correctly across domains
- `docs/UNIVERSAL_OPERATORS_REFERENCE.md` — consolidated table of all 22 operators with formulas, axiom citations, call signatures
- [VACUUM_ENGINE_MANUAL.md](VACUUM_ENGINE_MANUAL.md) §5 updated with v4 state-model (r_squared_total as canonical)
- [VACUUM_ENGINE_MANUAL.md](VACUUM_ENGINE_MANUAL.md) §6 updated with derivable-vs-placeholder status for every moduli
- Engine version bump (per §1.2 protocol): minor ~ major? v4.0 is probably a MAJOR bump given structural state-representation change
- [FUTURE_WORK.md G-10](../../.agents/handoffs/FUTURE_WORK.md) closure with v4 landing commit hash

---

## 5. Test plan

### 5.1 Regression preservation

Every existing test (954 on `research/l3-electron-soliton` branch) must continue to pass after each v4 phase. No behavior changes; only routing changes.

### 5.2 New test files

| File | Purpose | Phase |
|---|---|---|
| `test_universal_regime_classifier.py` | Pin the new operator's boundaries | v4.1 |
| `test_engine_r_squared_methods.py` | Pin `r_squared_K4/cos/total` and `regime_at_each_site` | v4.1 |
| `test_k4_tlm_universal_operators.py` | Verify inline → op-call refactor is numerically equivalent | v4.3 |
| `test_scale_invariance.py` | Cross-domain correctness of universal operators | v4.4 |
| `test_cosserat_moduli_derivation.py` | Pin derivation or placeholder for G, γ, ρ, etc. | v4.0 → v4.1 |

### 5.3 Cross-scale regression (v4.4 headline)

The scale-invariance suite is the **v4-defining test**. Passing it demonstrates:
1. Same operators, different A_c, correct physics in 4+ domains
2. No hardcoded magic numbers bias the regime classification
3. The Pythagorean combination rule yields numerically consistent r² across sectors

Failure means v4 didn't actually achieve scale invariance — diagnostic, not structural ship-blocker.

---

## 6. Risks and trade-offs

### 6.1 Behavioral regression risk — LOW

Every v4 change is a routing refactor, not a physics change. Universal operators are mathematically identical to current inline implementations (float-rounding aside). Full regression suite (954 tests) gates each phase.

### 6.2 Pre-registered prediction impact — ZERO

Predictions in `predictions.yaml` are framed in the engine's native quantities (A²_cos, A²_K4, Ω_node ratio, etc.). v4 changes WHERE those are computed, not WHAT they compute. No re-registration needed.

### 6.3 Stage 6 timeline impact — HIGH if v4 runs in parallel

v4 is scoped as **post-Stage-6**. Running v4 in parallel with Phase 4-6 creates merge hell (every Phase 4 engine change that touches `cosserat_field_3d._reflection_density` conflicts with v4.2's observer consolidation). Discipline: land Stage 6 first on the R4-patched engine; v4 is the post-kill-switch cleanup.

### 6.4 Derivation-gap risk — REAL

If Cosserat moduli (`G`, `γ`, etc.) cannot be derived from axioms cleanly (Option 1 in §3.5), v4.0 Option 2 requires acknowledging them as calibration placeholders. This is honest but slightly reduces the "zero-parameter framework" claim. Mitigate by explicit docstring + manuscript note + citation to ν_vac = 2/7 / K = 2G canonical constraints.

### 6.5 Magic-number replacement — should be mechanical

`2α`, `0.75`, `1.0` are already in Vol 1 Ch 7; moving them into `universal_regime_classifier` is a mechanical refactor. If any existing test depends on specific boundary arithmetic, the new operator reproduces it bitwise.

---

## 7. Out-of-scope for v4

- **Full derivation of Cosserat moduli from Axiom 1 hardware** (may require separate research doc; track as FUTURE_WORK if v4.0 Option 1 proves intractable)
- **SI-units interface layer** (engine stays natural-units internally; SI output is post-processing via `constants.py` factors)
- **Macroscopic-domain simulations** (v4 makes macroscopic capability POSSIBLE via per-call A_c, but the engine's Sources / Observers are subatomic-scale; repurposing to macroscopic is a separate effort — probably a FUTURE_WORK G-11 item)
- **KB operator-numbering reconciliation** (Y-8 — separate initiative; v4 uses `universal_operators.py`'s numbering since that's the live code)

---

## 8. Handoff checklist for next chat

Next chat picks up v4 after Stage 6 (Phase 6 headline validation committed and verdict recorded in doc 56_). Pre-conditions:

- [ ] **R4 patched and committed** (per `~/.claude/plans/review-the-collaboration-md-and-lexical-wombat.md` 17-step list)
- [ ] **Phase 4-6 complete** (asymmetric saturation, nucleation gate, autoresonant validation — all shipped, all tests green)
- [ ] **Doc 56_ written** (Phase 6 pair-creation results, v2 Option D validated or falsified)
- [ ] **FUTURE_WORK G-10 exists** (promotes v4 to tracked future work with this doc as the spec)
- [ ] **VACUUM_ENGINE_MANUAL at r4 or later** (per R4 closure)

When picking up v4:

1. Read this doc (57_) in full.
2. Read agent reports in §13 (universal operator inventory + manuscript survey).
3. Read [Vol 1 Ch 6 + Ch 7] and [Vol 4 Ch 1] directly — do not trust my summaries alone.
4. Start Phase v4.0 (preparation / derivation doc). Grant reviews before any code touches.
5. Each v4 phase commits atomically with its tests; full regression between phases.

---

## 9. Rollback plan

v4 is a REFACTOR — each phase preserves behavior. If any phase trips the regression gate:

- **Revert the offending commit** (single-phase atomic commits enable this cleanly)
- **Diagnose the drift** (likely a universal operator's float precision vs inline implementation; check clip boundaries)
- **Re-register with tighter tolerance or patch the operator** before proceeding

v4 is NOT a physics change, so rollback always lands on a consistent engine. Phases 1-5 are fully independent; failure in v4.3 doesn't contaminate v4.2.

---

## 10. Verification

**v4 is "done" when:**

1. All 954+ existing tests still green
2. New tests in §5.2 all green
3. `test_scale_invariance.py` (v4.4) passes across all listed domains
4. Zero hardcoded magic numbers for regime boundaries (grep for `2 * ALPHA`, `0.75`, `1.0` as regime thresholds in engine code returns only universal_regime_classifier itself and associated tests)
5. Zero inline `sqrt(1 - ...)` saturation patterns in engine dynamics code (exclude test docstring examples)
6. `VACUUM_ENGINE_MANUAL.md` updated to v5 (or equivalent major bump)
7. `G-10` closed in `FUTURE_WORK.md` with v4-landing commit hash

**v4 is "successful" when:** future engine changes can no longer silently reintroduce the A1-class normalization bug, because all paths now route through a single source of truth.

---

## 11. What v4 does NOT claim

- **Does not add physics.** Every operator is already in the corpus; v4 just enforces consistent routing.
- **Does not improve pair-creation predictions.** v4 is a code-structure refactor; Stage 6's physics outcomes (P_phase4, P_phase5, P_phase6) are independent.
- **Does not close all audit findings.** A2 (Pythagorean test), A5 (A²>1 varactor), A7 (linear-Taylor vs varactor) remain separate. v4 closes A1, A3, A14 structurally and provides infrastructure for A2 closure.
- **Does not replace Stage 6.** v4 is a *refactor* path after Stage 6 kills switches land.

---

## 12. Cross-references

**Primary:**
- [Vol 1 Ch 6 `06_universal_operators.tex`](../../manuscript/vol_1_foundations/chapters/06_universal_operators.tex) — 22 canonical operators
- [Vol 1 Ch 7 `07_regime_map.tex`](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex) — universal r = A/A_c
- [Vol 4 Ch 1 `01_vacuum_circuit_analysis.tex:711`](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L711) — subatomic override
- [AVE-APU Vol 1 Ch 5:26-40](../../../AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex) — Pythagorean strain theorem
- [Vol 1 Backmatter §"Full Derivation Chain"](../../manuscript/backmatter/02_full_derivation_chain.tex) — zero-parameter closure + Cosserat lepton generation

**Engine:**
- [universal_operators.py](../../src/ave/core/universal_operators.py) — 26 implementations
- [scale_invariant.py](../../src/ave/axioms/scale_invariant.py) — V_SNAP-default wrappers
- [saturation.py](../../src/ave/axioms/saturation.py) — V_YIELD-default wrappers (Axiom-4 macroscopic)
- [vacuum_engine.py:151-153](../../src/ave/topological/vacuum_engine.py#L151) — magic number violations
- [k4_tlm.py:227-346](../../src/ave/core/k4_tlm.py#L227) — inline operator violations
- [k4_cosserat_coupling.py:195-225](../../src/ave/topological/k4_cosserat_coupling.py#L195) — `_update_z_local_total` (canonical Pythagorean r²_total under R4 subatomic override; v4 centralizes via `r_squared_total()` method)

**Research thread:**
- [55_cosserat_normalization_derivation.md](55_cosserat_normalization_derivation.md) — **SUPERSEDED** by R4 per Vol 4 Ch 1:711 spot-check. Its R3 "K4 is outlier" reading applied macroscopic V_yield at subatomic scale. Kept for audit trail; its §11 engine patches should NOT be executed. R4 = remove `/α` from NodeResonance + BondObserver (plan file step 3) is the correct near-term patch.
- [54_pair_production_axiom_derivation.md](54_pair_production_axiom_derivation.md) — Phase 0 derivation chain for Phase 4-6
- [VACUUM_ENGINE_MANUAL.md §17](VACUUM_ENGINE_MANUAL.md) — audit findings

**Handoff:**
- [STAGE6_V4_HANDOFF.md](../../.agents/handoffs/STAGE6_V4_HANDOFF.md) — compact pickup doc for the next chat

---

## 13. Research agent reports (verbatim)

Two agents delivered exhaustive reports on 2026-04-23. Summaries above reference them; full reports archived here for future agents who need to double-check the derivation.

### 13.1 Agent A — universal operator code audit

[Full 26-function inventory, call-site map, hardcoded-magic-number audit. Key findings summarized in §2.1 above. Full text preserved in session transcript (see plan file) — reproduce verbatim if this doc is promoted to manuscript.]

### 13.2 Agent B — manuscript corpus on scale invariance

[Direct quotes from Vol 1 Ch 6, Ch 7, Vol 4 Ch 1, AVE-APU Ch 5, backmatter. Key findings in §1. Full text preserved in session transcript.]

---

*End of doc 57_. Sections 1-12 are load-bearing for v4 execution. §13 is historical record.*
