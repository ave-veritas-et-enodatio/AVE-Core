# Vacuum-Varactor Scatter Operator — the S(A)-reading admittance scatter

**Date:** 2026-06-20
**Branch:** `analysis/2026-06-20-vacuum-varactor-scatter` (off `origin/main` @ `32f29c67`)
**Module:** `src/ave/solvers/vacuum_varactor_scatter.py`
**Tests:** `src/tests/test_vacuum_varactor_scatter.py` (25 tests, all pass)
**Lane:** implementer
**Status:** DELIVERED — all four validate-on-known gates PASS; the
scramble-changes-operator demonstration PASSES (the Fork-B unblocker).

---

## 0. What this is (and is NOT)

**GOAL.** Make the trivalent shunt-junction scattering operator *READ* the local
saturation `S(A)`, wiring the canonical Axiom-4 varactor coupling
(`C_eff = C0 / S`, the longitudinal μ-load) into the scatter. Before this work,
`chiral_lattice.scatter_matrix(n, z_local=1.0)` (chiral_lattice.py:81-102)
**ignored its `z_local` argument** — an unimplemented docstring promise — so the
operator was **saturation-blind** (the dead-code path the Fork-B NO-GO found).

**Verified dead-code (origin/main @ 32f29c67):**
`scatter_matrix(3)` and `scatter_matrix(3, z_local=99.0)` return the **identical**
matrix. `z_local` never reaches the assembly (chiral_lattice.py:101 builds
`(2/n)J - I` with no reference to `z_local`).

**NOT in scope (Fork-B is the next step):** the Fork-B confinement verdict (does
the saturation tank confine the A1 mass?) and the quarter-arc shape
discriminator. This work delivers **only** the S(A)-reading operator + its four
validate-on-known gates + the scramble-changes-operator demonstration.

---

## 1. The core change — admittance-weighted scatter

The bedrock scatter is the **equal-admittance** shunt-junction reduction
(chiral_lattice.py:89, `V = (2/n) Σ_j V_j^inc`):

```
S_ij = (2/n) - δ_ij                                                  (bedrock)
```

This module implements its **admittance-weighted generalization**, derived from
the *same* shunt-junction KCL but retaining per-port admittance `Y_i` instead of
factoring it out:

```
V_i = V_i^inc + V_i^ref = V             (shunt: common node voltage)
Σ_i Y_i (V_i^inc - V_i^ref) = 0         (KCL)
=> V = 2 (Σ_j Y_j V_j^inc) / (Σ_k Y_k)
=> S_ij = 2 Y_j / (Σ_k Y_k) - δ_ij                                   (this work)
```

Setting all `Y_j` equal recovers `(2/n)J - I` — the bedrock is the
uniform-admittance special case (chiral_lattice.py:89). The bedrock `(2/n)J - I`
path stays intact and reproducible (gate 1; 14 bedrock tests still pass).

**Two senses of "exact" (kept distinct throughout this doc):**

- **bit-level exact** (`np.array_equal`, byte-for-byte equality) holds at `S = 1`
  i.e. `A = 0` (the vacuum case): `Y` is *literally* the all-ones vector `Y0·𝟙`, so
  `2 Y_j/Σ_k Y_k = 2/n` is computed by the *same float ops* as the bedrock and the
  result is **identical to the last bit** (gate 1, `max|d| = 0.0`).
- **exact-to-roundoff** (`np.allclose`, `atol≤1e-13`) holds for *any* saturated but
  **uniform** field (e.g. `A = 0.9` everywhere, or a per-node-uniform field): the
  common factor `Y = Y0/√S` cancels *algebraically* but the cancellation runs through
  a non-trivial `Σ` and division, so the agreement is to floating-point roundoff
  (`max|d| ~ 1e-16`), **not** bit-identical. The physics (the per-node-uniform no-op)
  is the same; the *numerical* statement is the weaker `allclose` one.

Wherever this doc writes "EXACTLY" for the **`A = 0`** vacuum row it means
**bit-level** (`array_equal`); for any **saturated-uniform** row it means
**exact-to-roundoff** (`allclose 1e-13`). The two are flagged separately in the
table below and asserted with the matching predicate in the tests
(`test_equal_admittance_recovers_bedrock_exactly` uses `array_equal`;
`test_per_node_uniform_load_does_not_change_scatter` uses `allclose atol=1e-13`).

### The varactor map (canonical Axiom-4)

```
Bond admittance:   Y_bond = Y0 / sqrt(S(A_bond))
Bond impedance:    Z_bond = Z0 * sqrt(S(A_bond))
Kernel:            S(A) = sqrt(1 - (A/A_yield)^2)   [crystal_engine.py:191, IMPORTED]
```

As the core saturates (`S -> 0`): `Z_bond -> 0` => `Γ -> -1` — the **mass cage,
the Z->0 SHORT, the corrected sign** (NOT a Z->inf bag). This is the
**longitudinal μ-LOAD** — the `Z_eff = Z0·√S` form is at
crystal_engine.py:463,477-478 (`gamma_bulk`: "Z_eff = Z0·√S → 0 ... Γ → −1", then
`Z_eff = S ** 0.5`), NOT the **forbidden ε-load** (`Z_eff = Z0/√S -> ∞`, `Γ = +1`;
the EPSILON-LOAD FORBID scope assertion at crystal_engine.py:466-468).

---

## 2. PER-BOND, NOT PER-NODE — the load-bearing Fork-B Finding 2

A **per-NODE-uniform** admittance **cancels** at the shunt junction: a common
factor `Y` in every `Y_j` cancels in `2 Y_j / Σ_k Y_k`, reducing back to
`(2/n)J - I` *regardless of S*. So the saturation must enter as **per-BOND
(directed-edge)** admittances that differ across ports (the S-gradient across the
connect-map), or the operator stays S-blind.

**Verified explicitly (srs L=2, diamond L=4):**

| Load | result vs bedrock | max\|dScatter\| |
|---|---|---|
| `A = 0` scalar (vacuum) | **== bedrock EXACTLY** | `0.0` |
| `A = 0.9` UNIFORM (deep, per-node) | **== bedrock** (Finding-2 no-op) | `~1e-16` |
| per-NODE `(N,)` varying, uniform-within-node | **== bedrock** | `~1e-16` |
| **per-BOND `(N,d)` varying** | **DIFFERS** | `0.17` (srs) / `0.11` (dia) |

The third row is the sharp one: a saturation field that varies *across nodes* but
is *uniform within each node* still cancels. It is the **per-port gradient** that
the operator reads — exactly the physical content the Fork-B NO-GO found was dead.

---

## 3. Validate-on-known — the four gates (HALT if any fails)

All four PASS. Frame-labels per `consistency-vs-emergence`.

### GATE 1 — `S = 1` everywhere → scatter `== (2/n)J - I` BIT-LEVEL EXACT  [IDENTITY]

Recovers the bedrock **bit-for-bit** (`np.array_equal`, `max|d| = 0.0`, srs +
diamond). At `A = 0 ⇒ S = 1` the admittance is *literally* `Y0·𝟙` so `2/n` is
computed by the identical float ops — this is the **bit-level-exact** sense (cf. the
**exact-to-roundoff** `allclose 1e-13` agreement for any *saturated*-uniform field,
Sec. 1). Algebraic reduction, true by construction (equal-Y → `2Y/(nY) - δ = (2/n) - δ`).

### GATE 2 — per-PORT-distinct admittance → scatter `!= (2/n)J - I`  [MANIFESTATION]

Proves it genuinely reads `z`. `max|d| = 0.183` (srs) / `0.149` (diamond). If this
had collapsed to the bedrock, the operator would be S-blind (the dead-code failure
mode) → HALT. It did not.

### GATE 3 — ALPHA-FREE  [CONSISTENCY / STRUCTURAL]

`ALPHA` is **never imported into the scatter path** (structural guard:
`"ALPHA" not in vars(module)`; `Q_TANK`, `ELECTRON` likewise absent). Under
`α → 2α`, the operator is **bit-identical**: `|dQ/Q| = 0.0` (Q = Frobenius norm of
the assembled per-bond-saturated operator). α lives only in the dimensionful
`V_YIELD = √α · V_SNAP` (constants.py:427); the scatter reads the **dimensionless**
`A = |V|/V_yield`, so `V_yield` (and hence α) **cancels** before the operator sees
it. α-invariance is **structural**, the load-bearing frame-independent anchor.

### GATE 4 — driven-frame cold-cage radiative-Q floor `~30`  [CONSISTENCY]

**What was reproduced:** the **structural radiative-Q floor** `Z_RADIATION = Z_0/(4π)
≈ 29.98 Ω` (constants.py:717), recovered *through* the admittance scatter. A node
port loaded by the free-space radiation impedance sees `Y_rad/Y_0 = Z_0/Z_RADIATION
= 4π` (exact), and the reflection looking into the bound node is
`Γ_bound = (1 - 4π)/(1 + 4π) ≈ -0.853` — a strong (not total) radiative short. The
floor number itself is `Z_RADIATION ≈ 29.98`.

**`Z_RADIATION ≈ 29.98` and `Q_ringdown ≈ 30.8` are BAND-CONSISTENT, NOT an
IDENTITY (DEC-5).** This is the load-bearing scope correction. The two ~30s are
**both inside the `[20,45]` radiative-Q floor band**, which is the honest, defensible
claim — but they are **`~2.7%` apart** (`|30.8 − 29.98|/29.98 = 2.74%`), and treating
them as the **same number** is exactly what a **pinned corpus anti-coincidence test
guards against**:

> `src/tests/test_graded_vacuum_network_isolation.py:119-124`,
> `test_anti_coincidence_Q_is_not_Z_radiation`:
> *"DEC-5 anti-coincidence: confirm the solver computes Q from the dynamics and is
> NOT silently the constant `Z_RADIATION = Z_0/(4π) = 29.98` (which sits in the
> `[20,45]` band). The open-port Q is `~1e5`, nowhere near 29.98."*
> — `assert abs(r["Q"] - 29.98) > 1.0`.

DEC-5 exists precisely because `29.98` sits in the same band as a dynamically-computed
`Q`, and a silent `Q == Z_RADIATION` would be a coincidence-magnet bug (a hard-coded
constant masquerading as computed dynamics). So the correct framing is: the cold-cage
ringdown **sits in the same radiative-Q-floor band** as the structural `Z_RADIATION`
anchor — **not** "the cold-cage sits *on* this anchor" (which would assert the very
identity DEC-5 forbids). Band-consistent ✅; identity ❌ (DEC-5-guarded).

**HONEST SCOPE GAP (flagged, not papered).** The cold-cage `Q_ringdown ≈ 30.8` is a
property of the engine's **dynamical real-space FDTD ring-down** —
`make_cage_engine(N=72)` + 6000 leapfrog steps + Hilbert-envelope decay-time fit
(test_l3_mass_cage.py:743, `test_t3_4_bound_eigenmode_of_posited_cage`). It is
**NOT** a property of this **static scattering matrix**: a scattering operator does
not, by itself, produce a decay time. So this gate does **not** re-run that
dynamical ringdown — that is engine FDTD scope. I **did** confirm the engine's
cold-cage test passes on this branch (`EXIT=0`, the test asserts a finite positive
`Q_ringdown` and the module docstring records `≈30.8`). The operator reproduces the
**structural radiative-Q floor** (`Z_RADIATION ≈ 29.98`, in the `[20,45]` band); it
does **not** independently re-derive the `30.8` ring-down number, and per DEC-5 the
two are **band-consistent, not identical**. This is the gate's honest closure:
structural floor ✅, dynamical ring-down = engine-scope, identity = DEC-5-forbidden,
all flagged.

---

## 4. THE KEY DELIVERABLE — scrambling S(A) CHANGES the operator (Fork-B unblocker)

This is what unblocks Fork-B. Take a per-bond saturation field `A`, then a
**scrambled** `A'` (the **same values**, permuted across directed bonds), and show
the assembled operator **changes**:

| net | max\|d𝓢\| | operator changed? |
|---|---|---|
| srs[right] (L=2) | `0.259` | **YES** |
| diamond (L=4) | `0.156` | **YES** |

`max|d𝓢| > 0` proves the operator **reads** saturation — the exact thing the
Fork-B NO-GO found was dead. A **negative control** confirms the signal is the
per-bond gradient and not assembly noise: scrambling a **uniform** field is a
no-op (`max|d| ~ 1e-14`, and the result still equals the bedrock).

---

## 5. Substrate-native-check (walked before the first line of numerical code)

- **K4 / graph.** The admittance scatter is the Op5 shunt KCL with per-port
  admittance, composed with the lattice's **own** directed-edge CONNECT
  permutation (`connect_index`, chiral_lattice.py:133-147). Built **from** the
  bond-graph, never a Cartesian posit.
- **Cosserat.** The varactor reads the **A1 dilatation** saturation `S(A)` (bulk /
  longitudinal sector). The `(2,3)` **winding** (charge-3) is **not** wired in —
  A1 ⊥ T2 honoured.
- **phase-space vs real-space.** The scatter lives in **n-PORT amplitude space** =
  the `(V_inc, V_ref)` phasor coordinates, the matching coordinates for the
  impedance. `S` enters as a dimensionless per-bond admittance weight, **not** a
  real-space Cartesian field compared against `φ²`.
- **Op14.** `S(A)=√(1-A²)` is the canonical kernel, **IMPORTED** from
  `crystal_engine` (delegates to `CrystalEngine.saturation_kernel`,
  crystal_engine.py:191), **not** hardcoded.
- **no-phasor-wire / EPSILON-LOAD FORBID.** The A1 scalar stays **common-mode**; the
  varactor is the longitudinal `C_eff = C0/S` μ-load giving `Z->0 / Γ=-1`
  (the μ-load `Z_eff = Z0·√S` form, crystal_engine.py:463,477-478), **not** the
  transverse ε-load (Z->∞ / Γ=+1; the EPSILON-LOAD FORBID at
  crystal_engine.py:466-468). The winding is not wired into the breather's own
  `(V_inc, V_ref)` phasor (master-equation.md:20, the two-3s disambiguation).

---

## 6. Honest caveats and the documented floor

- **Deep-saturation `Γ` is capped by the canonical floor — set by `A_cap`, not
  `S_min`.** The reachable `Γ ≈ -0.45` floor is set by the **amplitude clip `A_cap =
  0.99`**, *not* by the saturation floor `S_min = 0.05`. The canonical kernel
  (crystal_engine.py:191) is `S = √(max(1 − A², S_min²))`, so the floor on `S` is
  `S_min = 0.05` only if it binds — but the `A_cap` clip caps `A` at `0.99` *first*,
  giving `1 − A_cap² = 1 − 0.99² = 0.0199`, which is **larger** than `S_min² = 0.0025`.
  So `A_cap` is the **binding** constraint and `S_min` is **non-binding**:

  ```
  A clipped to A_cap = 0.99
    ⇒ S = √(1 − 0.99²) = √0.0199 = 0.1411   (NOT √S_min = 0.224 — S_min never binds)
    ⇒ Z = Z0·√S = √0.1411 = 0.3756
    ⇒ Γ = (Z − 1)/(Z + 1) = (0.3756 − 1)/(0.3756 + 1) = -0.454.
  ```

  The earlier framing ("`Z = √S_min ≈ 0.224 ⇒ Γ ≈ -0.45`") had the **wrong binding
  parameter**: `√S_min = 0.224` would give `Γ = -0.635`, *not* the observed `-0.45`.
  The numeric floor `≈ -0.45` is correct (and is what the operator computes); the
  *cause* is the `A_cap` amplitude clip, not the `S_min` saturation floor. Dropping
  **both** caps pushes `Γ -> -1` monotonically (at `A = 0.999999` with the clip
  released, `Γ < -0.9`). The **sign** and the **monotone-toward-(-1) trend** are the
  physics; the achievable depth is a floor parameter (`A_cap`), documented honestly —
  not a bug.
- **Gate 4 is a structural radiative-Q-floor anchor, not a dynamical re-derivation,
  and `Z_RADIATION ≈ 29.98` is band-consistent-not-identical to the cold-cage
  `Q_ringdown ≈ 30.8`** (Sec. 3, GATE 4 — both in the `[20,45]` band, `~2.7%` apart;
  the identity is explicitly guarded against by DEC-5,
  `test_graded_vacuum_network_isolation.py:119-124`).
- **The gates are mostly identity/consistency-class, by design.** Gate 1 is an
  identity (algebraic reduction); gates 3-4 are consistency/structural. The one
  manifestation-class result is gate 2 + the scramble demo: the operator's output
  **demonstrably depends on the saturation field**. That dependence is the whole
  deliverable — it is what was previously dead.

---

## 7. What this unblocks (and what it does not claim)

This delivers the **prerequisite** for any genuine saturation test: an operator
that actually reads `S(A)`. It does **not** claim the saturation tank confines the
A1 mass (Fork-B), nor does it discriminate the quarter-arc shape — both explicitly
out of scope. The next step (Fork-B) can now ask the confinement question against an
operator that is no longer S-blind.

**Symmetric-standard note.** The honest framing is *peer-mapped*: gate 4 reproduces
a *structural* anchor, not the dynamical ring-down number — stated plainly. The
operator-reads-saturation result (gate 2 + scramble) is a clean positive; it is the
narrow, load-bearing claim and it stands.
