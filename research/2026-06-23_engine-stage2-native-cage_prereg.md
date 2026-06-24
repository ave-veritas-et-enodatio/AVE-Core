# STAGE 2 PREREG — THE NATIVE CAGE (RE-FROZEN, pre-run, the first make-or-break)

**Status:** RE-FROZEN pre-registration. Pre-run. NO make-or-break simulation
executed at re-freeze time. **Re-freeze 2026-06-23 applies the three adjudicated
corrections from rigor gate `wg9rsjep8`** (CORRECTION 1: §5.1 sign flip
PLUS→MINUS, the blocker; CORRECTION 2: single-1/S code-enforced; CORRECTION 3:
CFL by measured-ρ). The rigor gate's read-AND-RUN pass EMPIRICALLY established
L_native is POSITIVE-semidefinite (L(r²)=−6 EXACT, adjoint ratio +1), forcing
the MINUS. §14.2/§14.3/§14.4 downgraded to RESOLVED-here.
**SHA-pin:** `9fe5b9c2cdc5c9b28e40ff507222201de03057d1` (origin/main HEAD at freeze).
**Branch:** `analysis/engine-stage2-native-cage-run` (off origin/main; main is PROTECTED — Grant merges).
**Supersedes:** the original freeze on `analysis/engine-stage2-native-cage-prereg`
(which froze the WRONG §5.1 PLUS — an unresolved contradiction with §14.2).
**Epic:** `_orchestration/2026-06-23_full-engine-pathway.md` Stage 2 ("THE NATIVE CAGE").
**Prior stages:** Stage 0 ✅ (#399 merged, α-clean spine), Stage 1 ✅ (#401 audited PASS, transverse modes).

---

## 0. THE RE-SCOPED MAKE-OR-BREAK (load-bearing — read this first)

### 0.1 What is NOT the make-or-break (the STALE framing, retired here)

The epic's surface phrasing — *"the K4 stencil was never tried WITH c_eff(V)"*
(`_orchestration/2026-06-23_full-engine-pathway.md:12`) — is **STALE for the
STATIC existence question and must NOT be the make-or-break.** The static
native c_eff(V) eigenmode existence is **ALREADY ESTABLISHED**:

- `graded_vacuum_network.py` implements c_eff(V) on the native tetrahedral K4
  stencil: `stiffness_profile()` (`:245-252`, "Local bulk stiffness
  c_eff²/c0² = 1/S(A)") and `_native_laplacian_with_stiffness()` (`:255-265`,
  divergence-form `adjoint_div(D·grad)` on `TETRA_OFFSETS`), with the μ-load
  SHORT Γ=−1 confinement (`:209-213`).
- It **RAN PASSING**: `test_graded_vacuum_network_isolation.py` GATE2
  (`:92-97`) — EM port CLOSED ⇒ Hermitian ⇒ Im(ω)=0 ⇒ **Q=∞ lossless-confined**
  (Q=1.4e16, Im(ω)=4e-17); GATE4 (`:106-110`) — bound mode **gapped (ω_re>0),
  localized, Nyquist-resolved**.

So a gapped, discrete, core-localized **static** bound mode of the native
c_eff(V) operator **exists**. That is this Stage's **validate-on-known
PRECONDITION**, not its open question.

### 0.2 The GENUINELY-OPEN make-or-break (what this prereg registers)

> **Does a seeded SECH precursor (v14 Mode-I config: N=24, A=0.85, sech)
> TIME-DOMAIN self-trap and PERSIST — a localized breathing core that does NOT
> disperse (Mode I) — on the native tetrahedral K4 stencil, with the co-acting
> cage engaged?**

Two scope locks, both load-bearing:

1. **POSITED PERSISTENCE ONLY — NOT genesis self-formation.** We seed an
   already-localized eigen-precursor and ask whether the native dynamics HOLD
   it (Mode I) or SHED it (Mode III). We do **NOT** claim
   formation-from-free-precursor: that is the **leaning-negative
   keystone-pump** (the convergence-engine coupling pumps H at dt→0;
   [[project_keystone_energize_lock_negative]]). Genesis is out of scope.

2. **TIME-DOMAIN, not frequency-domain.** Static eigenmode existence (§0.1) is
   a frequency-domain property of the linearized operator. **Self-trap +
   persistence is a nonlinear, time-domain property** — the c_eff(V) kernel is
   amplitude-dependent, so the dynamical question (does the breathing
   wavepacket hold together under its own nonlinear dispersion on the native
   stencil) is **not answered** by the static eigensolve. This is the open rung.

### 0.3 Why this is genuinely untested (the Cartesian-artifact risk)

**Every existing time-domain self-trap PASS is on a Cartesian 7-point
stencil**, verified at freeze:

- `MasterEquationFDTD._laplacian` (`master_equation_fdtd.py:122-139`) is the
  Cartesian 7-point Laplacian; `step` (`:200-211`) is the Cartesian leapfrog.
  The v14 Mode-I PASS (`test_master_equation_v14_mode_i.py`) runs on it.
- `CrystalEngine._laplacian` (`crystal_engine.py:154`) and `_laplacian_vec`
  (`:169`) are ALSO 7-point Cartesian; `step` (`:265-268`) uses them. The
  SELF-FOCUS anchor (`test_cage_stiffening_wall.py:56-66`, the sech arm) runs
  on it.

So the entire time-domain self-trap literature is **Cartesian**. The native
operator (`graded_vacuum_network.py`) exists ONLY as a **frequency-domain
eigensolver** — there is **no native time-domain leapfrog stepper yet**
(surfaced as a flag, §14.1; this Stage scaffolds it). The make-or-break: does
the Cartesian time-domain self-trap **survive transcription to the native
tetrahedral stencil**, or is it a square-grid artifact?

### 0.4 The two-sided make-or-break (both outcomes are legitimate results)

- **Mode I (persists natively):** the self-trap is a substrate property, not a
  Cartesian artifact. The native cage hosts a dynamical bound breathing core.
- **Mode III (disperses natively, even WITH the correct sech seed + co-acting
  cage):** the self-trap was a **Cartesian artifact**. This is a **clean
  FALSIFICATION**, reported early, NOT a bug to debug away (§11). A native
  Mode-III with the correct seed and co-acting cage is the real
  make-or-break finding.

## 1. SUBSTRATE-FIRST SECTOR HEADER (before any standard word)

Walked via `substrate-native-check` BEFORE any numerical-code scaffold:

- **Which sector?** The **A1 longitudinal-dilatation SCALAR V-sector** (the
  "mass-3", the Heaviside/Gibbs-excised scalar grade — physical, NOT
  Gauss-deleted; [[feedback_no_qed_longitudinal_scalar_is_real]]). A single
  scalar field `V` = bond-axial dilatation amplitude. This is **ORTHOGONAL to
  the transverse photon** (`master-equation.md:20`, the genesis-24
  double-count caution): the (2,3) micro-rotation winding (charge/spin) is
  **NEVER wired into this scalar cage** (`converter_on=False`). Chirality (κ̃)
  is OUT of scope for Stage 2 (frozen input that bites at saturation in Stage
  4, §9.4).

- **Does the engine carry that DOF?** Yes, but only Cartesian-natively today.
  The scalar V-sector dynamics are validated on the **Cartesian** leapfrog
  (`MasterEquationFDTD` / `CrystalEngine` bulk branch). The **native
  tetrahedral** carrier exists for the STATIC operator
  (`graded_vacuum_network._native_laplacian_with_stiffness`) but **NOT yet for
  time-domain integration** (§14.1 flag).

- **K4 / stencil:** the spatial operator is the **tetrahedral
  gradient/divergence** on the diamond-K4 stencil (4 tetrahedral diagonal
  offsets `TETRA_OFFSETS`, `cosserat_field_3d.py:134`; K4 connectivity z=3, do
  NOT flip 3→4). The composition `adjoint_div · grad` is the native diamond
  Laplacian (`graded_vacuum_network.py:30-36`). The Cartesian 7-point Laplacian
  is **FORBIDDEN (HR1)** as an operating grid; it is retained ONLY as a
  continuum cross-check reference (§8 bin c).

- **Cosserat:** N/A for Stage 2 (the micro-rotation grade is Stage 4). The
  scalar cage carries the A1 grade alone.

- **Op14:** the confinement wall = a **μ-load SHORT** (Z_core→0, Γ→−1, settled
  PR#260). Saturation kernel `S(A)=(1−A²)^exponent`, exponent=0.5 primary
  (√S, μ-load-justified), 0.25 sensitivity (DEC-1).

- **Cold vs saturated:** SPLIT (§2). Core: near-yield/saturated (A→1, the
  cage). Surround + ringdown: cold/sub-yield/lossless.

- **Phase-space vs real-space (A46):** the test is posed and measured in
  **real-space lattice field** coordinates (V-peak amplitude, |V|² energy
  density, interior-peak persistence). The corpus claim being tested — *a
  localized longitudinal-dilatation breathing core persists* — is itself a
  real-space field-localization claim. **Coordinates match.** No phase-space
  φ²/Clifford-torus/impedance-plane claim is at issue at this rung, so no
  phase-space-coordinate mismatch (`phase-space-coordinate-check` cleared).

- **Common category-error guard:** do NOT ride the standard noun "soliton
  binding energy / energy basin" onto this — there is **no Lagrangian /
  gradient-descent / energy-min** here. The dynamics are a **leapfrog
  scatter+connect** (`∂²V/∂t² = c_eff²·L[V]`); the lattice IS the computation.

## 2. REGIME / PHASE-STATE DECLARATION — the SPLIT regime

Per `ave-regime-phase-state-check`, declared BEFORE any substrate-response
claim. Stage 2 is a **SPLIT regime** — two co-located but distinct regimes,
which is the physical reality of a saturated soliton in a cold vacuum:

| Locus | MODE | REGIME | PHASE-STATE | Why |
|---|---|---|---|---|
| **Core** (r ≲ σ_core) | longitudinal-bulk (A1 scalar) | **near-yield / saturated** (A→1) | the cage | S(A)→S_min stiffens c_eff²=c0²/S; this engages the μ-load Γ=−1 wall. The cage cannot exist without near-yield saturation. |
| **Surround + ringdown observable** (r ≳ σ_core, the radiated/shed field) | longitudinal-bulk | **COLD / sub-yield / lossless** | the ideal reactive regime | Q≈30.8 cold radiating cage + the 2.3–2.9 cell radiation/breathing floor live HERE. The shed field propagates linearly (S≈1) and the ringdown-Q extraction assumes lossless-reactive surround. |

**Why the split matters for the verdict (artifact-vs-falsification guard):**

- The persistence observable (does the core hold) is a **near-yield/saturated**
  question — it can only be asked where the cage exists. A null measured in a
  regime where the cage CANNOT exist (e.g. a cold sub-yield seed that never
  saturates) would be an **artifact, NOT a falsification**
  ([[feedback_regime_phase_state_discipline]]). The seed amplitude A=0.85 is
  chosen specifically to engage saturation (min n_EM < 0.97 at core, per the
  v14 known-good `test_master_equation_v14_mode_i.py:114-128`).

- The radiation/dispersion SNR floor (the nuisance, §7) lives in the **cold
  surround** — it is the lossless-reactive baseline against which a persistent
  core must rise. The verdict is NOT "did the field move" (cold-regime noise)
  but "did the saturated core's energy/amplitude persist above the cold
  radiation floor over ≥K periods."

- Time dilation / scalar effects are regime-free; rate-asymmetry/rectification
  (Stage 6 territory) are NOT at issue here. Stage 2 reads only the
  scalar persistence amplitude — no rectification claim.

## 3. VCA (vacuum-circuit-analysis) FRAMING — the cage = the impedance short + bulk stiffening

Per `VCA` (the vacuum is a real graded impedance network; the cage is a
circuit object, not a potential well). The **as-built native cage is the
co-acting series of TWO impedance elements**, both keyed on the saturation
S(A):

1. **The bulk stiffening (the distributed element).** Under saturation the
   local bulk stiffness rises: `c_eff²/c0² = 1/S(A)` → 1/S_min in the core
   (`stiffness_profile`, `graded_vacuum_network.py:245-252`; same kernel as
   `MasterEquationFDTD.c_eff_squared`, `master_equation_fdtd.py:148-151`). In
   circuit terms this is a position-dependent **propagation impedance / phase
   velocity gradient** — the medium stiffens where the field is strong,
   creating a self-focusing graded-index lens. This is the c_eff(V)
   self-steepening that drives Mode-I nucleation.

2. **The μ-load Γ=−1 boundary short (the terminating element).** At the core
   boundary the impedance falls to a reflective short:
   `Z_eff = Z0·√S → 0` as A→1, giving **Γ_bulk = (Z_eff−1)/(Z_eff+1) → −1**
   (`crystal_engine.gamma_bulk`, `:460-491`, μ-load-scoped; matches the
   canonical live wall `cosserat_field_3d.py:500,1647-1648`). A Γ=−1 short
   reflects the breathing energy back into the core — the trapping boundary
   condition. Z0≡1 in engine units; this is the MAGNETIC μ-load (NOT an
   ε-load, which would give Γ=+1 the OPEN anti-trap — scope guard at
   `crystal_engine.py:471-474`).

### 3.1 ADJUDICATION B = CO-ACTING (Grant-ratified this session, conditioned on rigor)

Test the **AS-BUILT native cage with BOTH knobs engaged simultaneously**:
c_eff(V) bulk stiffening AND the μ-load Γ=−1 boundary short. The bulk and
boundary are **not separable** in the real soliton — the as-built cage is the
single physical object.

- **DO NOT** isolate the bulk term as a separate PRIMARY run.
- Isolation (bulk-only, no Γ-wall, or Γ-wall-only continuum surround) is a
  **FALLBACK DIAGNOSTIC ONLY**, run iff the co-acting cage returns Mode III —
  to localize which element failed. It is NOT a verdict axis.

**Rationale (VCA):** a transmission line terminated in a graded-index taper
PLUS a reflective short is one resonant cavity; measuring the taper alone or
the short alone tells you about a different (non-physical) circuit. The
co-acting cage is the resonant object whose Q the lossless eigenframe already
witnessed (Q=∞ closed-port, GATE2). Stage 2 asks whether the **time-domain**
energy in that same co-acting cavity persists.

## 4. THE CO-ACTING NATIVE OPERATOR SPEC (Adjudication B) — exact, with provenance

### 4.1 The native spatial operator (the divergence-form variable-coefficient Laplacian)

The native cage operator is the **self-adjoint divergence-form** Laplacian on
the tetrahedral K4 stencil:

```
L[V]  =  adjoint_tetrahedral_divergence( D(r) · tetrahedral_gradient(V) )
```

with `D(r) = c_eff²(r)/c0² = 1/S(A(r))` the per-site dimensionless bulk
stiffness (the bulk-stiffening element, §3.1). Each factor is pinned to its
solver docstring + the axiom chain:

| Factor | Source (verified at SHA-pin) | Axiom / provenance |
|---|---|---|
| `tetrahedral_gradient` | `cosserat_field_3d` (re-exported `graded_vacuum_network.py:100-105`); grad on `TETRA_OFFSETS` | native K4 stencil, HR1 (no Cartesian 7-pt) |
| `adjoint_tetrahedral_divergence` | same | discrete adjoint of grad ⇒ symmetric PSD form |
| `D = 1/S(A)` | `stiffness_profile()` `graded_vacuum_network.py:245-252` | c_eff²=c0²/S, A-034 kernel `master_equation_fdtd.py:26-32` |
| `S(A) = (1−A²)^exp` clipped `[S_min,1]` | `saturation_kernel()` `:222-231` | Op14; DEC-1 exp=0.5 primary / 0.25 sensitivity |
| divergence-form assembly | `_native_laplacian_with_stiffness()` `:255-265` | keeps the Hermitian part a proper stiffness (loss only via port) |

This is **EXACTLY** the operator the static eigensolve already validated
(`graded_vacuum_network._build_sparse_stiffness` `:340-403`,
`_native_laplacian_with_stiffness` `:255-265`). Stage 2 reuses this spatial
operator verbatim and drives it in **time** (the new piece, §5).

`L` is **symmetric positive-semidefinite** (it is the discrete stiffness form
`gradᵀ D grad`; nullspace = constant/rigid modes; empirically L(r²)=−6 EXACT,
adjoint ratio +1, re-verified at the run SHA). The time-domain wave equation
is therefore `∂²V/∂t² = −c0²·L[V]` (the **MINUS** restoring sign: `L` is the PSD
stiffness, so `−L = ∇²`), giving real ω² ≥ 0. The leapfrog update inherits this
MINUS (§5.1) — the eigensolver's `H x = ω² x` PSD convention and the leapfrog's
MINUS are the SAME sign convention (`graded_vacuum_network.py:133-138`).

> **⚑ Convention flag (§14.2) — RESOLVED at re-freeze (`wg9rsjep8`):** the
> eigensolver writes the operator as `H x = ω² x` with `L` the PSD stiffness
> (`solve_isolation_Q` `:469-541`). The leapfrog uses the **MINUS** restoring
> sign (`−dt²·c0²·L_native`, §5.1) so that `−c0²·L_native` is the restoring
> (not anti-restoring) operator. The continuum-limit cross-check (§8c) is the
> witness that the sign is right — a flipped sign (PLUS) blows up, not
> disperses, and would NOT recover the Cartesian v14 Mode-I. (Empirically
> confirmed by `wg9rsjep8`: PLUS → inf in ~20 steps; MINUS → bounded.)

### 4.2 The co-acting μ-load Γ=−1 wall (the terminating short)

The Γ=−1 wall is **NOT a separately-applied boundary operator** — it is the
**same S(A) field** read through the impedance route. The bulk stiffening (D)
and the boundary short (Γ) are **two readouts of one saturation field**, which
is exactly why Adjudication B treats them as co-acting (§3.1):

- `D(r) = 1/S(A(r))` drives the dynamics (the stiffening lens).
- `Z_eff(r) = √S(A(r))`, `Γ_bulk(r) = (Z_eff−1)/(Z_eff+1)` is the **diagnostic
  readout** of the wall depth at each step (`crystal_engine.gamma_bulk`
  `:460-491`; `gamma_from_S_floor` `fork_b_saturation_tank.py:97-108`). The
  acceptance bin (§8b) tracks `gamma_bulk_min` over the run.

Because both are functions of the **same evolving A(r,t)**, the wall deepens
exactly when and where the core saturates — they cannot be engaged separately
without altering the physical object. (This is the substrate-native reason
Adjudication B is co-acting, not a convenience.)

### 4.3 Native-grid alignment (cheap, part of Stage 2)

Confirm the srs net / K4-diamond / tetrahedral stencil are the SAME native node
set (z=3) or align them, per epic Open-item (`:41`). `TETRA_OFFSETS` (4
diagonals) is the canonical scalar stencil here; `stencil_provenance()`
(`graded_vacuum_network.py:192-203`) is the no-Cartesian gate
(`cartesian_7pt_imported: False`). This is a native + cheap scaffold step, NOT
a Cartesian bridge.

## 5. THE TIME-DOMAIN INTEGRATOR + DISCRETIZATION (leapfrog, dt/CFL, grid, boundary)

### 5.1 The integrator — second-order leapfrog (validated Cartesian engine structure, native PSD L swapped in WITH THE SIGN CORRECTED)

The native time-domain stepper is the **same second-order leapfrog** the
validated Cartesian engine uses (`master_equation_fdtd.step` `:200-211`,
`crystal_engine.step` `:265-268`), with the **only** change being the spatial
operator `L` — **and a SIGN FLIP forced by the sign-convention difference
between the two operators** (corrected here, see freeze-record note below):

```
V^{n+1} = 2·V^n − V^{n-1} − dt² · c0² · L_native[V^n]
```

where `L_native[V] = adjoint_tetrahedral_divergence(D·tetrahedral_gradient(V))`
(§4.1) replaces the Cartesian `_laplacian`, with `D = c_eff²/c0² = 1/S(A)`
folded into the divergence coefficient **exactly once**, and `c0 = 1`.

**Why the MINUS (the load-bearing sign — was the §5.1 freeze bug):** `L_native`
is the discrete stiffness form `gradᵀ D grad`, which is **POSITIVE-
semidefinite** — empirically L(const)=0, L(linear)=0, **L(r²)=−6 EXACT**
(re-verified at the run SHA, `_native_scalar_laplacian`), ⟨u, L_native u⟩ =
+‖grad u‖² ≥ 0, adjoint ratio = +1.0. So **L_native = +gradᵀgrad =
−(continuum Laplacian)**. The physical wave equation is
`∂²V/∂t² = +c_eff²·∇²V` with `∇² = −L_native`, hence
`∂²V/∂t² = −c_eff²·L_native[V]` — the restoring term carries a **MINUS**. This
is the OPPOSITE of the Cartesian `step`, where `_laplacian` returns the
NEGATIVE-semidefinite form (`Σnbr − 6·center`, `master_equation_fdtd.py:130-138`,
≈ +∇²) and the PLUS sign is correct. Copying the Cartesian PLUS onto the PSD
native operator is anti-restoring → exponential blowup.

**Single-1/S, code-enforced (CORRECTION 2, §14.3):** the full
`c_eff²(V) = c0²/S` is folded into the divergence coefficient `D` inside
`_native_laplacian_with_stiffness` (`graded_vacuum_network.py:264`), so the
stepper steps with `dt²·c0²·L_native[V]` and **MUST NOT** additionally multiply
by `c_eff²(V)` / `1/S`. The Cartesian template DOES multiply by `c_eff_squared`
(`master_equation_fdtd.py:202-204`); transcribing it verbatim would apply 1/S
**twice** (= 1/S_min² = 1e6 in the saturated core). A unit test pins the
per-step core-operator magnitude to scale as 1/S_min, NOT 1/S_min² (§B gate).

> **FREEZE-RECORD NOTE (sign correction, re-freeze 2026-06-23, cite rigor gate
> `wg9rsjep8`):** the original §5.1 froze the WRONG **PLUS**
> (`+dt²·c_eff²·L_native`). The read-AND-RUN rigor gate `wg9rsjep8`
> **empirically established** that L_native is POSITIVE-semidefinite
> (L(r²)=−6 EXACT, adjoint ratio +1), so the PLUS is anti-restoring: a direct
> integration showed PLUS → exponential blowup (1.02 → 10.7 → 251 → inf in
> ~20 steps) while MINUS → bounded (0.68 → 0.21). §14.2 had already flagged the
> PLUS as wrong but the contradiction was left UNRESOLVED in the frozen §5.1.
> This re-freeze RESOLVES the contradiction in §5.1 itself: the frozen update
> is now MINUS. (Adjacent §14.2/§14.3 flags are downgraded to RESOLVED-here.)

Initial condition: `V_prev = V_seed.copy()` (∂_tV=0, at-rest seed — the v14
method, `test_master_equation_v14_mode_i.py:62-64`,
`cage_stiffening_wall.py:116-117`).

### 5.2 dt / CFL — FROZEN by MEASURED spectral radius (CORRECTION 3, NOT the Cartesian √3 heuristic)

**Frozen CFL (the rigorous native bound):** for the leapfrog wave equation
`V^{n+1} = 2V^n − V^{n-1} − dt²·c0²·L_native[V^n]`, stability requires
`dt²·ρ(c0²·L_native) ≤ 4`, i.e. `dt ≤ 2/√(ρ·c0²)`. The frozen choice is

```
dt = cfl_safety · 2 / √(ρ_measured · c0²)        cfl_safety = 0.4,  c0 = 1
```

where **`ρ_measured` is the spectral radius of the assembled SATURATED native
operator** (power-iteration on the assembled sparse `c0²·L_native` evaluated on
the v14 saturated seed field `D = 1/S(A)`, NOT the cold operator). In the
saturated core `ρ scales as ρ_cold / S_min`. `ρ_measured` is **pinned in the
freeze record at run-start** and the run uses exactly this dt.

- `cfl_safety = 0.4` (the validated v14 value, `test_master_equation_v14_mode_i.py:33`).
- **Cold-operator sanity (lower-bound only, NOT the operating CFL):**
  `ρ(L_native cold, N=24) ≈ 1.0` — NOT the Cartesian 12, because the
  tetrahedral gradient carries a **0.25 prefactor** (`cosserat_field_3d.py:157`).
- **The Cartesian `√3` heuristic is DROPPED as the operating bound.** It reads
  `dt = cfl_safety·dx/(c_eff_max·√3)` (`master_equation_fdtd.py:90-94`) and is
  retained ONLY as a **lower-bound sanity cross-check** (it is ~7× over-
  conservative vs the measured-ρ bound here — safe, but not the frozen dt). The
  native tetrahedral stencil has a different spectral radius than the Cartesian
  6-axis stencil (flag §14.4, RESOLVED-here by measured-ρ), so the Cartesian
  `√3` CFL is **not the correct bound** for the native operator. Record both
  the heuristic dt and the measured-ρ dt in the freeze record; the run uses the
  measured-ρ dt (and asserts it is ≤ the heuristic dt as a sanity gate).

### 5.3 Grid N + geometry

- **Primary N = 24** (the v14 Mode-I config, `test_master_equation_v14_mode_i.py:28`;
  matches the SELF-FOCUS anchor box and the scattering box). `dx = 0.5`
  (v14, `:31`). This makes the native run **directly comparable** to the v14
  known-good and the radiation-floor anchor.
- **Convergence witness:** also run N=32 (v14 canonical upper, `:28`) and N=20
  to confirm the verdict (persist/disperse) is N-robust, not a single-grid
  artifact (mirrors the eigensolve's Q-grows-with-N convergence sweep,
  `test_graded_vacuum_network_isolation.py:79-85`). The verdict bin must AGREE
  across N (a verdict that flips with N is UNRESOLVED, §8).

### 5.4 Boundary handling

- **PML absorbing layer**, `pml_thickness = 4` (v14, `:32`;
  `cage_stiffening_wall.py:68`). Quadratic sponge damping
  (`_build_damping_mask`, `master_equation_fdtd.py:107-120`). The PML absorbs
  the radiated/shed field so the interior persistence question is clean.
- **PML-EXCLUSION on every field observable (A-Rule 10 corollary):** all
  energy/amplitude reads filter to the interior
  `pml_thickness ≤ {i,j,k} ≤ N−pml_thickness−1` BEFORE any peak/argpartition
  extraction (`_bulk._interior_slice` `:172-178`,
  `CrystalEngine.interior_mask`). PML cells return frozen-absorbing artifact,
  not interior physics. **The verdict observable is interior-only.**
- The native tetrahedral gradient uses periodic `roll` internally
  (`_build_sparse_stiffness` `:366-371`); the PML damping mask multiplies
  `V_new` each step (as in the Cartesian engine) so the periodic wrap energy is
  absorbed at the sponge before it re-enters the interior. **⚑ Flag §14.5:**
  confirm the periodic-roll native operator + the (non-periodic) PML sponge
  compose without a wrap-around leak — the eigensolve uses a periodic cube with
  an interior matched port, not a PML sponge, so this composition is new for
  the time-domain native run.

## 6. THE SEED — sech eigen-profile (v14 Mode-I config), NOT the Gaussian

### 6.1 The frozen seed (exact form, verified against the v14 known-good)

```
center = N // 2
coords = arange(N) − center
X, Y, Z = meshgrid(coords, coords, coords, indexing="ij")
r = sqrt(X² + Y² + Z²) · dx
V_seed = A · (1 / cosh(r / SEED_RADIUS))
V[:]      = V_seed
V_prev[:] = V_seed.copy()          # ∂_tV = 0 (at-rest)
```

with the **frozen v14 Mode-I config**: `N=24`, `dx=0.5`, `A = 0.85`,
`SEED_RADIUS = 2.5`.

**VERIFIED at freeze (this is mandatory per the seed-trap fix):** this exact
form + normalization matches the v14 known-good byte-for-byte:

- `test_master_equation_v14_mode_i.py:57-64`:
  `seed = SEED_AMPLITUDE * (1.0 / np.cosh(r / SEED_RADIUS))`, with
  `SEED_AMPLITUDE=0.85`, `SEED_RADIUS=2.5`, `N=24`, `DX=0.5`,
  `r = sqrt(X²+Y²+Z²)*DX`, `engine.V_prev[:] = seed.copy()`. **IDENTICAL.**
- `cage_stiffening_wall.py:110-117` (the SELF-FOCUS anchor's `_seed`,
  `profile="sech"`): `seed = amp * (1.0 / np.cosh(r / width))`,
  `engine.V[:] = seed; engine.V_prev[:] = seed.copy()`. **IDENTICAL** (the
  anchor calls it with `amp=0.85, width=2.5, N=24, dx=0.5`,
  `test_cage_stiffening_wall.py:40`).

There is **no separate amplitude normalization** — `A=0.85` is the peak field
in V_yield units (V_yield=1), the strain at r=0. This engages saturation
(min n_EM = S^0.5 < 0.97 at core, the v14 saturation-engaged criterion
`test_master_equation_v14_mode_i.py:114-128`).

### 6.2 Why NOT the Gaussian (the Mode-III false-negative trap, baked in)

**Explicitly DO NOT** reuse `graded_vacuum_network.saturated_core_strain()`
(`:234-242`) or `CrystalEngine.seed_bulk(...helical=False)` — both plant a
**GAUSSIAN** `A·exp(−r²/2σ²)`. The Gaussian is **corpus-PINNED to DISPERSE**:

- `test_cage_stiffening_wall.py:68-76` (`test_gaussian_seed_bulk_disperses`):
  the prereg §2 `seed_bulk` Gaussian **DISPERSES at every frac** — no growth
  beyond seed, the wall does NOT deepen below t0.
- `test_cage_stiffening_wall.py:12-14` (docstring): *"the Gaussian is not in
  the breather's basin"* — the cage's nucleation is **PROFILE-selective**.
- `test_cage_stiffening_wall.py:79-86` (`test_profile_sensitivity_identical_box`):
  in the IDENTICAL box at matched amplitude, the **sech self-focuses** and the
  **Gaussian disperses** — the discriminator is the seed PROFILE, not the
  amplitude.

**Seeding the Gaussian on the native stencil would manufacture a Mode-III
false-negative** — it would disperse for a reason that has nothing to do with
the native-vs-Cartesian question (it disperses on Cartesian too). The only
informative seed is the breather-basin profile, the sech. This is the central
false-negative trap the seed choice exists to avoid.

### 6.3 What a clean native Mode-III would mean (the make-or-break logic)

If the **sech** seed (the known breather-basin profile that self-focuses on
Cartesian) **disperses on the native stencil with the co-acting cage**, that is
the make-or-break finding: the self-trap was a **Cartesian artifact**, not a
substrate property (§0.4, §11). The Gaussian-disperse is a control that proves
the apparatus can see dispersion; the sech-disperse (if it happens) is the
falsification.

## 7. THE OBSERVABLES — energy/amplitude (NOT centroid); the radiation-floor SNR nuisance

### 7.1 The persistence observable MUST be energy/amplitude, NOT centroid

The frozen primary observable is **mean interior-peak |V| over the
post-transient window** — the v14 breathing criterion
(`test_master_equation_v14_mode_i.py:91-95`, V_peak mean) — read on the
PML-excluded interior (`cage_persistence_trace`, `_bulk.py:512-536`,
`interior peak |V|`). Companion energy metric: interior `Σ|V|²`
(`interior_energy`, `_bulk.py:211-216`).

**Why NOT a centroid metric (the WALL-engine verdict, baked in):**

- For a shell-like / breathing-core distribution, the **centroid of a shell is
  the empty middle** — centroid sampling misses the energy-density structure
  ([density-peak-vs-centroid, A-Rule 10 corollary]).
- The single-blob **radiation/breathing floor is 2.3–2.9 cells** (verified
  `mass_sector_two_body_scattering_results.json`:
  `per_separation[0..2].radiation_floor_cells = 2.524 / 2.339 / 2.935`). A
  centroid wanders by O(2–3 cells) just from breathing/radiation, so
  **centroid SNR < 1** — the centroid cannot distinguish a persistent core
  from a dispersing one. This is the WALL-engine verdict: centroid is
  uninformative here.
- The **energy/amplitude** metric does not have this problem: a persistent
  core holds its peak |V| and interior |V|² above the cold radiation floor; a
  dispersing core's peak |V| and interior energy decay toward the floor. The
  amplitude/energy contrast is large (the sech/Gaussian separation is large,
  `cage_stiffening_wall.py:71-72`).

### 7.2 The radiation-floor SNR nuisance (explicit Stage-2 nuisance)

The cold surround carries a **radiation/breathing floor of 2.3–2.9 cells**
(above). This is an explicit Stage-2 SNR nuisance, NOT a verdict axis. It sets:

- The **persistence threshold floor** (§8a): a core "persists" only if its mean
  post-transient interior-peak |V| stays a stated factor ABOVE the cold
  radiation/dispersion baseline (the disperse arm's late-window level), not
  merely nonzero.
- The **breathing-vs-decay discrimination** (§8a): mean V_peak with bounded
  std/mean (breathing, `test_master_equation_v14_mode_i.py:98-111`,
  std/mean ∈ [0.05, 0.5]) distinguishes a live breathing core from both a
  damped (std/mean→0) and a diverging (std/mean>0.5) one. The radiation floor
  is the noise this must rise above.

### 7.3 The reactance-pair recording (A-Rule 10: don't snapshot one phase)

Per the reactance-pair-tracking corollary, the time-domain run records BOTH
states of the bulk reactance pair over the FULL recording window, every step:

- **C-state** (the capacitive reactance): interior-peak |V| and `ω` (the field
  amplitude / stored compression).
- **L-state** (the inductive reactance): interior-peak `∂_tV` and the breathing
  `ω` (the flow; `record_breathing_dVdt`, `_bulk.py:436-446` — DC-free, kills
  the slow core-offset relaxation so the breathing eigenmode is resolvable).

A single-phase snapshot is consistent with BOTH a static plant and an
oscillator caught at peak — the pair is required to certify a genuine breathing
mode. `ringdown_Q` (§9.3) reads the L-state envelope.

### 7.4 The wall-depth diagnostic observable

`gamma_bulk_min` over the run (the μ-load short depth, §4.2,
`crystal_engine.gamma_bulk` `:460-491`), interior-only. This is the §8b
acceptance axis (monotonic deepening), recorded every step alongside the
persistence observable.

## 8. PRE-REGISTERED ACCEPTANCE BINS (frozen, falsifiable, numeric)

All bins frozen pre-run. The verdict (Mode I / Mode III) is the conjunction of
the four bins below. The thresholds mirror the v14 known-good (the Cartesian
reference the native run must match in the continuum limit) so the native run is
adjudicated against the **same** numeric criteria the Cartesian self-trap passed
— this is the discriminating axis (`ave-discrimination-check`: the bins
separate native-persist from native-disperse with a control proving the
apparatus sees both).

### 8a. PRIMARY — Mode-I persistence vs Mode-III dispersion (the make-or-break)

Run window: `N_STEPS_TOTAL = 600`, `N_STEPS_TRANSIENT = 200` (v14,
`test_master_equation_v14_mode_i.py:39-41`); post-transient window = 400 steps.
"≥K periods" = the post-transient window must span ≥ K=5 breathing periods
(`T_breath = 2π/ω_cutoff`, ω from `cutoff_eigenfrequency`); if <5 periods,
extend to `N_STEPS_TOTAL` such that the window covers ≥5 periods (production
mode) — recorded, not a free knob.

**MODE I (PERSISTS) — ALL must hold (interior, PML-excluded):**

| # | Criterion | Threshold | Source anchor |
|---|---|---|---|
| I-1 | mean V_peak (post-transient) > threshold | **> 0.2** (bound state persists, doesn't decay) | `test_master_equation_v14_mode_i.py:91-95` |
| I-2 | breathing signature std/mean | **> 0.05** (genuinely breathing, not damped) | `:98-103` |
| I-3 | not diverging std/mean | **< 0.5** (bound, not catastrophic) | `:106-111` |
| I-4 | saturation engaged (min n_EM=S^0.5 at core) | **< 0.97** | `:114-128` |
| I-5 | persists above radiation floor | mean V_peak (post-transient) **> 1.5×** the matched-amplitude Gaussian-control late-window level (§7.2) | radiation floor 2.3–2.9 cells |
| I-6 | bounded (no genesis-24 detonation) | max\|V\| **< 10.0** over the run | `cage_stiffening_wall.py:77` (DETONATION_MAX_V) |
| I-7 | N-robust | I-1…I-6 hold at N=24 AND the verdict bin agrees at N=20, N=32 | §5.3 |

**MODE III (DISPERSES) — the falsification:** I-1 fails (mean V_peak ≤ 0.2 OR
late-window |V| shrinks below 0.5× seed, `cage_stiffening_wall.py:76`) with the
**sech** seed and the co-acting cage. **Reported as a clean FALSIFICATION**
(§11), NOT debugged.

**CONTROL (apparatus-sees-dispersion):** the matched-amplitude **Gaussian**
seed (A=0.85, same box) MUST register DISPERSES (mean V_peak shrinks; the wall
does not deepen) — `test_cage_stiffening_wall.py:68-76`. If the Gaussian
control does NOT disperse, the apparatus is broken and the run is VOID
(not a verdict).

**UNRESOLVED:** verdict bin flips across N (I-7 fails), or the window covers
< 5 breathing periods and cannot be extended within budget.

### 8b. gamma_bulk_min — MONOTONIC-DEEPENING (NOT literal reach-−1)

Literal Γ=−1 is **unreachable by construction** (verified at freeze): the
μ-load floor `gamma_bulk_min` floors at **−0.4539** at A_cap=0.99
(`test_cage_stiffening_wall.py:108`, S^0.5 corrected;
`naive_gamma_floor` `cage_stiffening_wall.py:80-96`) and deepens to **≈−0.94**
only at near-total saturation S_min=1e-3
(`test_fork_b_saturation_tank.py:96-104`, `gamma_from_S_floor(1e-3)≈−0.939`).
Numerically re-verified at freeze: Γ(S=√(1−0.99²))=−0.4539; Γ(S=1e-3)=−0.9387;
legacy S^0.25 floor = −0.2400.

**Frozen acceptance (sign-safe, anchor-matched):**

| # | Criterion | Threshold |
|---|---|---|
| Γ-1 | `gamma_bulk_min` deepens monotonically toward −1 with saturation depth (more negative as the core saturates) | strictly decreasing trend over the saturation sweep; final < t0 by ≥ DEEPEN_ABS=0.005 (`cage_stiffening_wall.py:75`) |
| Γ-2 | sign-safe (never flips positive) | `gamma_bulk_min < 0` at all saturated points; an ε-load Γ=+1 would falsify the μ-load identity |
| Γ-3 | floor anchor at A_cap=0.99 | `gamma_bulk_min ≈ −0.4539` (abs 0.01) at A_cap=0.99, S^0.5 |
| Γ-4 | deep anchor at near-total | `gamma_bulk_min ≈ −0.94` (−0.95 < Γ < −0.93) at S_min=1e-3 |
| Γ-5 | exponent robustness (DEC-1) | Γ-1…Γ-4 hold for exponent=0.5 (primary); report exponent=0.25 (legacy floor −0.2400) as sensitivity |

**NEVER bin on reaching literal −1** (`cage_stiffening_wall.py:19-21`,
`test_cage_stiffening_wall.py:98-112`: magnitude is apparatus-qualified).

### 8c. CONTINUUM CROSS-CHECK — recovers the Cartesian v14 Mode-I (Cartesian = reference only)

The native run MUST recover the Cartesian v14 Mode-I **in the continuum limit**
(dx→0 / N→large), per epic (`:24,38`; Grant 2026-06-24: Cartesian = continuum
cross-check ONLY, not an operating grid).

| # | Criterion | Threshold |
|---|---|---|
| C-1 | Cartesian reference reproduces v14 Mode-I (re-run for this Stage) | the four v14 bins (I-1…I-4) PASS on `MasterEquationFDTD` at N=24, dx=0.5 |
| C-2 | native → Cartesian convergence | the native breathing ω_cutoff and mean V_peak approach the Cartesian values as dx halves (N=24→48 at fixed physical box), trend monotone, residual shrinking |

**Logic:** C is the reference axis. If the **native** run is Mode III (8a) but
C-1 passes, the conclusion is **self-trap = Cartesian artifact** (the make-or-
break finding). If native is Mode I (8a) AND C-2 converges, the self-trap is a
substrate property. C-1 failing would itself be a regression alarm on the
reference (report, do not proceed).

### 8d. NATIVE ringdown_Q — honest, α-free, the SOLE time-domain Q-extractor

| # | Criterion | Threshold |
|---|---|---|
| Q-1 | native `ringdown_Q` is the SOLE time-domain Q-extractor | no other Q path; Q = ω₀·τ/2 from the Hilbert-envelope decay (`_bulk.ringdown_Q` `:486-509`) |
| Q-2 | Q is MEASURED, never baked | no '137'/'0.00729' literal in the Q path; Q NOT in the 117–157 α-leak band |
| Q-3 | finite radiating Q is honest | the open/radiating native cage Q is finite (geometric leak, not lossless); cross-ref the cold radiating Q≈30.8 (`test_l3_mass_cage.py:25`, `test_stage0_alpha_clean_spine.py:152-176` Q≈30.75) — NOT a chord, the documented echo-not-chord negative |
| Q-4 | lossless limit honest | the closed-port / linear-standing native cage rings to Q=∞ honestly (Im(ω)=0 eigenframe, GATE2; finite-grid time-domain Q is window-sensitive — corpus-named, NOT a leak, `_spine.lossless_ringdown_Q` `:146-182`) |

Q is a **diagnostic** at this Stage (the chord Q=1/α is NOT claimed; Stage 2 is
not the α-Q rung). Q-2 is a hard α-leak gate (§9, §10).

## 9. α-CLEAN DISCIPLINE (the immune system inherited from Stage 0)

Inherited verbatim from the Stage-0 spine
(`test_stage0_alpha_clean_spine.py`, `_spine.py`,
`graded_vacuum_network.py:111-114`). Every element below is a HARD-STOP at run
time, not a soft check.

### 9.1 The guard triad (import-time, on every Stage-2 module)

`ALPHA / ALPHA_COLD_INV / Q_TANK / ELECTRON / RHO_BULK` are NOT reachable in
the Stage-2 scaffold's globals (`assert_spine_globals_alpha_clean`,
`_spine.py:242-265`; the same triad as `graded_vacuum_network.py:111-114`,
`_spine.py:76-80`). The guard is LIVE (a deliberately-injected ALPHA trips it,
`test_stage0_alpha_clean_spine.py:133-144`). Bare dimensionful magnitudes are
lazy-imported at point-of-use (`_bulk.py:89-95`) so they never enter module
globals.

### 9.2 κ̃ = 6/5, NOT κ_chiral = α·κ̃

The chiral coupling input is `KAPPA_TILDE_ELECTRON = 6/5`
(`cosserat_field_3d.py:94`, α-free, the electron (2,3) torus factor
pq/(p+q)) — **NOT** `kappa_chiral = α·κ̃` (the α-baked form,
`cosserat_field_3d.py:131`). The α-baked `CosseratField3D` Q-readout
(golden-torus = α⁻¹ at R·r=¼, `:2425`) is EXCLUDED — its DOF are reused
elsewhere; its Q-readout is never imported into the spine (epic `:16`).
**Chirality is OUT of scope for Stage 2** — κ̃ is a frozen input that bites at
saturation in **Stage 4**, not here (the scalar cage does not engage the
winding; `converter_on=False`).

### 9.3 ringdown_Q = the SOLE time-domain Q-extractor

`_bulk.ringdown_Q` (`:486-509`) — Hilbert-envelope decay fit, Q=ω₀·τ/2, α-free
by construction; Q=∞ honest in the flat limit. No alternative Q path. No
closed-form 137, no Q_TANK, no ELECTRON instance.

### 9.4 The literal scrubber + the 117–157 landing-zone exclusion

- **Literal scrubber** (source-level, `assert_no_alpha_literal_in_spine`,
  `_spine.py:222-239`): no '137' / '0.00729' literal in the verdict-determining
  Stage-2 code path. Extend the inspected-function set to cover the native
  time-domain stepper + the persistence/verdict functions.
- **117–157 landing-zone gate:** any measured Q (native ringdown, native
  radiating cross-ref) MUST NOT land in the 117–157 band — a Q in that band is
  an α-leak (`test_stage0_alpha_clean_spine.py:102-105,114-116,173-176`). The
  cold radiating cage is Q≈30.8 (far below the band, the documented
  echo-not-chord negative); a sudden 137 would be a leak, HARD-STOP.

## 10. CI GATE + ANTI-SELF-VALIDATION (A47)

### 10.1 The native gates (do NOT bank a single-run native result)

Per the rigor requirement, do NOT bank a single-run native result without a
gate. Two native CI gates at pinned tolerance:

- **GATE-Γ (native gamma_bulk_min):** the native run's `gamma_bulk_min`
  satisfies §8b — at A_cap=0.99: Γ ≈ −0.4539 ± 0.01; at S_min=1e-3:
  −0.95 < Γ < −0.93; sign-safe; monotonic. SHA-pinned regression anchors
  (`test_cage_stiffening_wall.py:107-108`, `test_fork_b_saturation_tank.py:96`).
- **GATE-Q (native ringdown_Q):** the native radiating cross-ref Q is finite,
  positive, and NOT in 117–157 (§8d Q-3, §9.4). SHA-pinned tolerance band
  around the documented Q≈30.8 cross-ref (band, not knife-edge: order-of-
  magnitude per HR3, `graded_vacuum_network.py:285-289`).

### 10.2 Anti-self-validation (A47 — the gate must not validate the engine against itself)

The gates are constructed so they **cannot validate the engine against its own
output**:

- The Γ anchors (−0.4539, −0.94, −0.2400) are **closed-form algebraic** values
  of `Γ=(√S−1)/(√S+1)` at the saturation floors — computed independently of any
  time-domain run (`naive_gamma_floor` / `gamma_from_S_floor` are pure
  functions of S, no engine state). The native run's Γ is checked against the
  **algebra**, not against a prior native run.
- The persistence thresholds (V_peak>0.2, std/mean band, n_EM<0.97) are the
  **Cartesian v14 known-good** criteria — an EXTERNAL reference the native run
  must independently meet, not a native self-consistency loop.
- The α-leak gates (117–157, literal scrubber, guard triad) check the run is
  **NOT** reproducing a CODATA-derived target — they are anti-self-validation
  by design (they FAIL if the engine reproduces the imported α-echo).
- **No CODATA/SI substitution in any verdict input.** All thresholds are
  α-free dimensionless ratios or v14-engine-natural values. Per
  `consistency-vs-emergence`: the Γ and persistence inputs are NOT
  CODATA-derived through SI substitution (the A47 v17 trap) — they are kernel
  algebra (Γ) and the engine's own breathing criterion (persistence).

## 11. HONEST-CLOSURE COMMITMENT (Rule 11) — the disperse outcome IS the finding

**Pre-committed, before any run:** if the **sech** seed (the correct
breather-basin profile) with the **co-acting** cage (Adjudication B) returns
**Mode III (disperses) on the native tetrahedral stencil**, that is a
**legitimate FALSIFICATION**, reported early — NOT a bug to debug away.

- The mechanism, if it happens, has a single name: **the self-trap was a
  Cartesian-stencil artifact** (the square-grid 7-point Laplacian supported a
  bound breather the native tetrahedral z=3 stencil does not). One mechanism
  explains the whole result — that is the discipline working at full strength.
- **WRONG reaction (forbidden):** debug toward a rescue — re-tuning S_min, the
  seed width, dt, the port, or swapping to the bulk-isolation fallback to
  *manufacture* a native Mode I. The isolation fallback (§3.1) is a DIAGNOSTIC
  to localize the failure, NOT a rescue path to a different verdict.
- **RIGHT reaction:** record the clean negative, name the mechanism
  (Cartesian-artifact), close the native-cage make-or-break branch with a
  FALSIFIED verdict, and surface the corpus-state change (the epic's "native
  cage" milestone returns FALSIFIED; the two-grid bridge does NOT dissolve as
  hoped — the native engine cannot host the dynamical self-trap).
- **Do NOT drop adjudication criteria post-hoc** to convert Mode III → Mode I.
  The §8 bins are frozen here, pre-run.
- **Substitution-not-retraction (Rule 12 / A47 v11b):** a FALSIFIED verdict
  does NOT get refilled with a new unverified rescue hypothesis. If native
  Mode III holds, the slot stays FALSIFIED; any new "the native cage works if
  …" hypothesis gets a new version number with its own verification chain.

The Gaussian apparatus-control (§8a) guarantees a Mode-III is a real
dispersion, not a dead apparatus.

## 12. CLASSIFICATION (consistency-vs-emergence)

Per `consistency-vs-emergence`, every threshold/target is tagged:

- **Stage 2 is a CONSISTENCY check, NOT an emergence/chord claim.** It asks
  whether a KNOWN Cartesian property (the v14 self-trap) survives transcription
  to the native stencil. A PASS = "the native stencil is CONSISTENT with the
  Cartesian self-trap" (manifestation/consistency class). It is NOT a novel
  AVE-distinct prediction (the chord lives in forward predictions —
  optical-activity sign-flip, (q·ℓ_node)⁴ dispersion, GW-echo;
  [[project_state_of_ave_and_testing_pivot]]).

| Input / target | Class | Why |
|---|---|---|
| V_peak>0.2, std/mean band, n_EM<0.97 (persistence) | **consistency** | the engine's own v14 breathing criterion; native must match the Cartesian known-good |
| Γ anchors −0.4539 / −0.94 / −0.2400 | **identity** | closed-form algebra Γ=(√S−1)/(√S+1) at saturation floors; not a fit, not CODATA |
| continuum cross-check (native→Cartesian) | **consistency** | convergence to a known reference |
| native ringdown_Q ≈ 30.8 cross-ref | **manifestation (echo)** | the documented echo-not-chord cold-cage Q; explicitly NOT the α-Q chord |
| static eigenmode existence (precondition) | **consistency** | GATE2/GATE4 already passing |

- **NO emergence (Class D) claim anywhere in Stage 2. NO chord.** The α-Q chord
  (Q=1/α=137) is EXCLUDED by construction (§9); reproducing it would be an
  α-leak HARD-STOP, not a success.
- **Symmetric-standard note:** a native Mode-I "consistency" result is no weaker
  than the corresponding SM scaffolding (SM also does not derive its soliton
  profiles from first principles); the object-level knife (no smuggled fit, no
  CODATA substitution, apparatus-control present) stays sharp regardless.

## 13. OPEN ITEMS + FORWARD-GUARD FENCES (non-blocking)

Cheap-text forward fences (pinned now so later stages can't drift into them).
Stage 2 touches NONE of these:

- **ξ_machian fence (Stage 3).** G enters Stage 3 as a **dimensionless modulus
  ratio** (K=2G = a form-identity, MERGED PR#261). Newton-G's **dimensionful
  value is a FIT** (u₀* back-solved), NOT derived
  ([[project_form_value_meta_finding]]). Stage 2 touches neither K=2G's value
  nor G's dimensionful magnitude — pinned forward.

- **Equilibrium-not-flow thermal fence (future).** Any future thermal layer is
  an **EQUILIBRIUM bath** (symmetry-breaking = gapped-mode FREEZE-OUT, E live /
  B frozen; δ_strain is SIGN-ONLY, ~1e-38, unobservable), NOT a flow/transport
  layer. Stage 2 has **no thermal bath** — pinned forward.

- **Native-grid alignment** (§4.3, part of Stage 2 but cheap): confirm srs /
  K4-diamond / tetrahedral are the same z=3 node set (epic `:41`).

- **Stage-4 α-contaminant** (carry-forward): `chiral_lattice_vector_sat.py:15`
  imports ALPHA (the saturated genesis engine, natural Stage-4 host). α-clean it
  before Stage 3/4 hosts the dynamical shear (epic `:39`). Stage 2 does not
  import it.

- **Cosserat mass-gap CI gap:** the 0.35% validate (T=π) is script-recorded;
  Stage 4 must SHA-pin it (epic `:40`). Not a Stage-2 item.

## 14. RIGOR CONCERNS / AMBIGUITIES SURFACED AT FREEZE (flag-don't-fix)

Surfaced for Grant/auditor adjudication; NOT silently resolved. Each is a real
gap I hit while grounding the spec in the code at the SHA-pin.

**14.1 — There is no native time-domain stepper yet (the central scaffold-to-be-built).**
`graded_vacuum_network.py` is a **frequency-domain eigensolver** only
(`solve_isolation_Q` / `solve_isolation_Q_sparse`). The native spatial operator
`_native_laplacian_with_stiffness` (`:255-265`) exists, but **no native
leapfrog stepper exists** — `_bulk.py`'s time-domain helpers
(`make_cage_engine`, `breathing_kick_cage`, `cage_persistence_trace`,
`ringdown_Q`) all route through `CrystalEngine` / `MasterEquationFDTD`, which
are **Cartesian 7-point** (`crystal_engine.py:154`,
`master_equation_fdtd.py:122`). **Stage 2's first scaffold task is to build the
native leapfrog** (compose `_native_laplacian_with_stiffness` into the §5.1
leapfrog with the §5.4 PML). This prereg specifies it; it does not yet exist.
This is the single largest piece of new code and the main place a bug can hide.

**14.2 — Sign-convention bridge between eigensolver and leapfrog. ✅ RESOLVED at
re-freeze (rigor gate `wg9rsjep8`, 2026-06-23): the frozen §5.1 update is now
MINUS (`−dt²·c0²·L_native`). The contradiction this flag named — §5.1 froze the
WRONG PLUS while §14.2 said MINUS — is resolved IN §5.1 itself. Empirically:
PLUS → blowup (1.02→10.7→251→inf, ~20 steps); MINUS → bounded (0.68→0.21). Body
below preserved for audit trail.** The
eigensolver poses `H x = ω² x` with `L` the PSD stiffness
(`graded_vacuum_network.py:469-541`). The leapfrog restoring operator is
`+c0²·L_native` with the wave equation `∂²V/∂t² = −c0²·L·V`? The PSD `L` is the
stiffness `gradᵀD grad` (positive); the physical wave operator is
`∂²V/∂t² = c_eff²·∇²V` where `∇² = −L` (the Cartesian `_laplacian` returns the
NEGATIVE-semidefinite Laplacian `Σnbr − 6·center`, while the native
`adjoint_div·grad` returns the POSITIVE-semidefinite form). **Sign mismatch
risk:** the native `L` (PSD) and the Cartesian `∇²` (NSD) differ in sign — the
leapfrog must use `V_new = 2V − V_prev − dt²·c_eff²·L_native[V]` (MINUS, because
`L_native` is the PSD stiffness) to match `+c_eff²·∇²` of the Cartesian engine.
**This sign must be verified by the continuum cross-check (§8c C-2): a flipped
sign blows up, it does not disperse.** Flagged because the §5.1 update as
written (`+dt²·c0²·L_native`) is WRONG if `L_native` is PSD — the correct sign
is MINUS. Surfacing, not silently fixing: the scaffold author must verify the
sign against `_native_scalar_laplacian` on a known mode (L(r²)=const,
L(linear)=0, `graded_vacuum_network.py:133-138`) BEFORE the production run.

**14.3 — Double-application of 1/S risk. ✅ RESOLVED at re-freeze (rigor gate
`wg9rsjep8`, 2026-06-23): CORRECTION 2 makes the single-1/S rule CODE-ENFORCED.
§5.1 steps with `dt²·c0²·L_native` and a unit test pins the per-step core-
operator magnitude to scale as 1/S_min (NOT 1/S_min²) on the v14 saturated seed
(§B validation gate). Body below preserved for audit trail.**
`_native_laplacian_with_stiffness`
already folds `D = 1/S = c_eff²/c0²` into the divergence coefficient (`:264`).
If the leapfrog ALSO multiplies by `c_eff²(V)` (as the Cartesian `step` does,
`master_equation_fdtd.py:202-204`), the stiffening is applied **twice**. The
§5.1 frozen convention (fold the full c_eff² into D, step with `dt²·c0²·L_native`)
avoids this — but the scaffold must NOT additionally call `c_eff_squared`. This
is the most likely silent bug; pinned explicitly.

**14.4 — CFL √3 is a Cartesian heuristic, not valid for the tetrahedral
stencil. ✅ RESOLVED at re-freeze (rigor gate `wg9rsjep8`, 2026-06-23):
CORRECTION 3 freezes `dt = 0.4·2/√(ρ_measured·c0²)` with ρ_measured by power-
iteration on the assembled SATURATED operator, pinned in the freeze record. The
Cartesian √3 heuristic is demoted to a lower-bound sanity cross-check only
(~7× over-conservative). Cold ρ ≈ 1.0 (the 0.25 grad prefactor), NOT 12. Body
below preserved for audit trail.** The native operator's 4 diagonal offsets
give a different spectral
radius than the Cartesian 6-axis stencil. §5.2's mitigation (measure
`ρ(c0²·L_native)` by power-iteration, `dt=0.4·2/√ρ`) is the rigorous fix;
flagged so the run does not silently inherit an unstable dt.

**14.5 — Periodic-roll native operator vs non-periodic PML sponge.** The native
gradient uses periodic `roll` (`graded_vacuum_network.py:366-371`); the PML is a
non-periodic sponge. Their composition is NEW for the time-domain native run
(the eigensolve used a periodic cube + interior matched port, not a PML). A
wrap-around leak would corrupt the persistence read. Verify the composition on
a cold free pulse (energy absorbed at the sponge, no wrap re-entry) before the
saturated run.

**14.6 — Epic prose still carries the STALE "never tried with c_eff(V)"
framing.** `_orchestration/2026-06-23_full-engine-pathway.md:12` reads "The K4
stencil was never tried WITH c_eff(V)" and `:24` frames the static existence as
open. This is **STALE for the STATIC question** (the static native c_eff(V)
eigenmode demonstrably exists, §0.1, GATE2/GATE4 passing). It is **correct only
for the TIME-DOMAIN question** (§0.2). This prereg corrects the scope; the epic
prose should be updated by the auditor to "the native time-domain self-trap was
never tried" to avoid re-litigating the settled static existence. **Surfaced for
the auditor to land** (I do not edit the epic; lane discipline). Conflict
recorded with both citations: epic `:12,24` (stale) vs
`graded_vacuum_network.py:245-265` + `test_graded_vacuum_network_isolation.py:92-110`
(static existence established).

**14.7 — `_spine.py:50-55` says the spine "runs on the Cartesian leapfrog
grid".** The Stage-0 spine docstring states the K4 collapse is deferred to
"Stage 3" and the cold spine "runs on the Cartesian leapfrog grid". The epic
was **re-architected 2026-06-24 to NATIVE-FIRST** (`:9-14`), making Stage 2 (not
Stage 3) the native-stencil rung. The spine docstring predates the
re-architecture. Not a blocker for Stage 2 (Stage 2 builds its own native
stepper), but the "Stage 3 two-grid bridge" language in `_spine.py:50-55,84-100`
is now superseded ("the bridge is GONE", epic `:31`). Surfaced for the auditor;
I do not edit the spine.

**14.8 — `kappa_tilde` carried in `NativeOperatorConfig` but unused in the
isolation D-block.** `graded_vacuum_network.NativeOperatorConfig` carries
`kappa_tilde=6/5` (`:179`) "for Build-B H_couple, NOT used in the isolation
D-block". Stage 2's scalar cage likewise does NOT use κ̃ (chirality out of
scope, §9.2). Confirm the native time-domain scaffold does not accidentally
wire κ̃ into the scalar dynamics (it must remain a frozen, unused-here input).

---

### FREEZE RECORD

- **SHA-pin:** `9fe5b9c2cdc5c9b28e40ff507222201de03057d1` (origin/main HEAD).
- **Frozen:** all §8 bins, the §6 seed, the §4/§5 operator+integrator, the
  §9/§10 α-clean gates. Pre-run. NO make-or-break simulation executed.
- **Verified-at-freeze:** sech seed byte-identical to v14 known-good (§6.1);
  Γ anchors −0.4539 / −0.9387 / −0.2400 re-computed (§8b); static native
  eigenmode existence GATE2/GATE4 passing (§0.1); both production engines
  confirmed Cartesian 7-pt (§0.3).
- **Skills applied:** substrate-native-check (§1), ave-regime-phase-state-check
  (§2), VCA (§3), consistency-vs-emergence (§12), ave-canonical-source (§9),
  ave-discrimination-check (§8), verify-before-cite (all file:line cites
  grep-verified at SHA-pin), flag-don't-fix (§14), phase-space-coordinate-check
  (§1, cleared — real-space match).

### RE-FREEZE RECORD (2026-06-23 — three adjudicated corrections from rigor gate `wg9rsjep8`)

- **Trigger:** the read-AND-RUN rigor gate `wg9rsjep8` EMPIRICALLY confirmed a
  sign bug frozen into §5.1 (the WRONG PLUS), contradicting §14.2's MINUS — an
  UNRESOLVED contradiction in the original freeze. Resolved here in §5.1 itself.
- **Adjudicated math (re-verified at the run SHA against the live code):**
  `L_native = adjoint_tetrahedral_divergence(D·tetrahedral_gradient(V))`,
  `D = 1/S(A)` (`graded_vacuum_network.py:255-265`), is **POSITIVE-
  semidefinite**: L(const)=0, L(linear)=0, **L(r²)=−6 EXACT** (mean −6.0,
  std 0.0); adjoint ratio +1.0. So `L_native = +gradᵀgrad = −(continuum
  Laplacian)`. Cold ρ(L_native, N=24) ≈ 1.0 (the 0.25 grad prefactor,
  `cosserat_field_3d.py:157`), NOT the Cartesian 12.
- **CORRECTION 1 (BLOCKER):** §5.1 update PLUS→MINUS. Frozen update verbatim:
  `V^{n+1} = 2·V^n − V^{n-1} − dt²·c0²·L_native[V^n]` (c_eff²/c0²=1/S folded into
  D inside L_native; c0=1). Empirical proof: PLUS → blowup
  (1.02→10.7→251→inf, ~20 steps); MINUS → bounded (0.68→0.21).
- **CORRECTION 2 (BLOCKER):** single-1/S, code-enforced. The stepper steps with
  `dt²·c0²·L_native[V]` and MUST NOT additionally multiply by `c_eff²`/`1/S`
  (the Cartesian template at `master_equation_fdtd.py:202-204` does — that would
  apply 1/S twice = 1/S_min²=1e6 in the core). Unit test pins the per-step core-
  operator magnitude to scale as 1/S_min, NOT 1/S_min², on the v14 saturated seed.
- **CORRECTION 3:** CFL by measured-ρ. Frozen `dt = 0.4·2/√(ρ_measured·c0²)`,
  ρ_measured by power-iteration on the assembled SATURATED operator (ρ/S_min in
  the core), pinned in the freeze record at run-start. Cartesian √3 demoted to a
  lower-bound sanity cross-check only (~7× over-conservative).
- **§14 status:** §14.2 / §14.3 / §14.4 downgraded to ✅ RESOLVED-here (bodies
  preserved for audit trail). §14.1 (native stepper to build), §14.5 (PML/wrap),
  §14.6–§14.8 (auditor-to-land / scope) remain OPEN as before.
- **Re-freeze remains PRE-RUN for the make-or-break** — the make-or-break sim is
  NOT executed at re-freeze; the corrected prereg is committed FIRST, then the
  stepper is built and the validation gates run, with a HARD HALT before the
  make-or-break.
