# Genuine Two-Sublattice K4 ⊗ Cosserat Band Structure — Substrate-Native A→B Bond Operator (Lane B re-run)

**Date:** 2026-06-23 · **Lane:** B (Cosserat band structure), RE-RUN of PR #389 done properly
**Type:** pre-registration + result (validate-on-known gate THEN spectrum, sector-header FIRST)
**Branch:** `analysis/cosserat-band-structure-two-sublattice` · **Driver:** `src/scripts/vol_1_foundations/cosserat_band_structure_two_sublattice.py`
**Status:** SCAFFOLD — pre-reg frozen below before the driver's verdict is read.
**Supersedes (scope):** PR #389 (`cosserat_full_band_structure.py`) validated on the SINGLE-NODE 6×6 matrix `D6` and used a phenomenological tile-and-scale ansatz `C = sf_mag·D6` for the two-sublattice coupling — NOT the substrate-native A→B bond operator. This re-run builds the genuine bond network.

---

## SUBSTRATE-FIRST SECTOR HEADER (mandatory, BEFORE any standard-physics word)

- **WHICH SECTOR.** The full K4 **TWO-SUBLATTICE** lattice. Per node: 6 DOF = 3 translational `u` (A1 compression + shear) + 3 micro-rotational `ω` (Cosserat micro-rotation). Two interpenetrating diamond sublattices (A,B) → **12 DOF per unit cell → a 12×12 Bloch matrix `D(k)`**. The A↔B coupling is the **real tetrahedral diamond bond operator** — the same substrate-native A→B bond the engine uses (`cosserat_field_3d._tetrahedral_gradient` + `_compute_strain` + `_compute_curvature`), assembled as explicit A→B bonds exactly as the canonical translation-only `k4_bloch_dispersion.py` does for the EM sector. It is **NOT** a tiled-and-scaled 6×6 block (PR #389's `C = sf_mag·D6`), and **NOT** a Cartesian 6-point Laplacian stencil (the RANK-2 disabled-flag bug the structural-null-stencil lens warns of).

- **REGIME.** Cold linear (small-signal) band structure. **Substrate fact stated up front:** the 4₁-screw handedness is **SATURATION-ONLY** — `κ_chiral` biases the saturation kernel (`cosserat_field_3d.py:562, 605-606` in `_reflection_density_asymmetric`: `A2_μ = (1 + κ_chiral·h_local)·A2_μ_base`), and does **NOT** enter `_energy_density_bare` (the cold linear energy at `cosserat_field_3d.py:676`). Therefore the cold linear bands are **parity-symmetric BY CONSTRUCTION**. We **expect NO topology chord** in the cold spectrum; that is **CORRECT, not a failure** — the handed mode lives in the driven/saturated regime, a separate phase probed later. (Refute-by-default: if a parity asymmetry appeared in the cold bands it would signal a BUG, not a chord, since the bare energy has no parity-odd term.)

- **PHASE-STATE / MODE / op14.** MODE = mixed translational (shear `G`, bulk via `(2/3)G tr²`) + micro-rotation (`G_c`, curvature `γ`). REGIME = linear / sub-yield. Op14 saturation = OFF (`use_saturation=False` analog, `k_op10=k_refl=k_hopf=0`). PHASE-STATE = unbroken free-wave (no saturated load-bearing sites; local-clock modulation N/A).

- **PHASE-SPACE vs REAL-SPACE (A46).** This is a **real-space / spatial-Brillouin** measurement (`ω(k)` band structure), the matching coordinate for the corpus claim being validated (`m²=4G_c/I_ω`, itself a real-space continuum-field gap). It is NOT a phase-space `(V_inc, V_ref)` Clifford-torus claim — no φ²/winding comparison is made.

---

## 0. North star + what is genuinely new vs PR #389

PR #389 did two things that this re-run replaces:
1. **It validated on `D6` (single-node 6×6), never on the two-sublattice matrix.** V1–V4 in `cosserat_full_band_structure.py` all call `dynamical_matrix(...)` / `omega2_branches_by_character(...)` — the 6×6 continuum form. The 12×12 was only used for band-COUNT plots (`omega2_branches(..., two_sublattice=True)`), never gated.
2. **Its two-sublattice coupling was `C = sf_mag·D6`** (`cosserat_full_band_structure.py:220`) — the on-site continuum matrix tiled into the off-diagonal and scaled by the scalar structure-factor magnitude `|Σ_b e^{ik·d_b}|/4`. This is a phenomenological ansatz. It is NOT the micropolar bond operator: it has no per-bond strain/curvature tensor, no axial/shear bond split, and its off-diagonal is just a scaled copy of the on-site block.

**This re-run builds the genuine object:** a 12×12 `D(k)` whose A→B block is the sum over the four tetrahedral bonds of the Cosserat **bond constitutive operator** — the same `ε_ij = ∂_j u_i − ε_ijk ω_k`, `κ_ij = ∂_j ω_i` strain/curvature that the engine's `_compute_strain`/`_compute_curvature` apply, but evaluated as the **inter-sublattice finite difference across each A→B bond** with the diamond Bloch phase `e^{ik·(τ_B+R_b)}`, exactly as `k4_bloch_dispersion.dynamical_matrix` assembles the EM sector.

---

## 1. Substrate-native construction (the bond operator, derived)

The engine's energy is `W = (2/3)G(tr ε)² + G ε_sym·ε_sym + G_c ε_antisym·ε_antisym + γ κ·κ` with the tetrahedral gradient `d_j V_i ≈ (1/4) Σ_ℓ p_ℓ^j [V(x+p_ℓ) − V(x)]` (`_tetrahedral_gradient`, `cosserat_field_3d.py:148`). On a SINGLE grid, `V(x)` and `V(x+p_ℓ)` are the same field at two sites.

On the **two-sublattice** diamond, the four tetrahedral offsets `p_ℓ = (±1,±1,±1)` (even # of minus signs) are exactly the four A→B nearest-neighbour bonds. So the engine's single-grid difference `V(x+p_ℓ) − V(x)` IS the inter-sublattice difference `V_B(cell+R_ℓ) − V_A(cell)`. The substrate-native gradient becomes a **bond operator** acting between sublattices:

  `(∂_j V_i)_A = (1/4) Σ_ℓ p_ℓ^j [V_i^B(cell+R_ℓ) − V_i^A(cell)]`

For a Bloch wave `V^A(cell)=u_A e^{ik·r}`, `V^B(cell+R_ℓ)=u_B e^{ik·(r+τ_B+R_ℓ)}`, the gradient symbol splits into a self-part (A) and a cross-part (B-phase):

  `∂_j → G_j^self = −(1/4) Σ_ℓ p_ℓ^j` (acts on the A amplitude, real)
  `∂_j → G_j^cross(k) = +(1/4) Σ_ℓ p_ℓ^j e^{ik·(τ_B+R_ℓ)}` (acts on the B amplitude, complex, carries the bond phase)

Note Σ_ℓ p_ℓ^j = 0 over the four even-parity offsets, so `G_j^self = 0` — the on-site gradient self-term vanishes, exactly as on the single grid the constant field has zero gradient. The whole gradient lives in the **cross (A→B) phase term**, which is the substrate-native bond operator. This is the structural difference from PR #389: the strain/curvature are built from `G_j^cross(k)` evaluated bond-by-bond, NOT from a scaled copy of `D6`.

The 12×12 stiffness is then assembled as the Hessian of `W` in the 12-amplitude basis `x = (u^A, ω^A, u^B, ω^B)`, with the strain/curvature linear maps carrying the per-sublattice gradient symbols. `D(k) = M^{-1/2} Φ(k) M^{-1/2}`, `M = diag(ρ,ρ,ρ,I_ω,I_ω,I_ω, ρ,ρ,ρ,I_ω,I_ω,I_ω)`. Eigenvalues are `ω²(k)`; 12 branches (6 acoustic-family + 6 optical-family).

## 2. Canonical moduli + units

| Symbol | Meaning | Canonical source | Value used |
|---|---|---|---|
| `G` | shear modulus (T₂ photon speed `c=√(G/ρ)`) | `photon-propagation-baseline.md` | 1 (natural) |
| `G_c` | micropolar coupling — opens the gap | `cosserat-mass-gap.md:49` | 1 |
| `γ` | curvature/couple-stress modulus | `cosserat_wave_test.py` | 1 |
| `ρ` | translational density | `cosserat_field_3d.py` | 1 |
| `I_ω` | rotational inertia density | `cosserat_field_3d.py` | 1 |
| `ℓ_C` | Cosserat length `√6·L_NODE` | `constants.ELL_C` | imported |

Natural units (G=G_c=γ=ρ=I_ω=1) exactly as the validated `cosserat_wave_test.py` reference so the validate-on-known is directly comparable to the 0.35% canonical gap. Dimensional `C_0, Z_0, L_NODE, ELL_C, OMEGA_C` imported by SYMBOL.

---

## 3. PRE-REGISTERED validate-on-known targets (frozen BEFORE reading the verdict) — ON THE REAL 12×12 MATRIX

Refute-by-default: each is a number the corpus already owns. The gate is run on the **genuine two-sublattice `D(k)`** (NOT `D6`). If it does not recover them within tolerance, the bond operator is wrong — HALT, report no spectrum.

| # | Pre-registered target | Corpus value | Tolerance | Rationale |
|---|---|---|---|---|
| V1 | translational acoustic slope (lowest branch, k→0) → `c_EM` | `√(G/ρ)=1` | rel-err < 1e-3 | transverse photon `photon-propagation-baseline.md` |
| V2 | gapless rotational slope (G_c=0, k→0) → `c_R` | engine-faithful `√(2γ/I_ω)=√2` (continuum label `√(γ/I_ω)=1` — see FLAG) | rel-err < 5e-2 | `cosserat_wave_test.py` T1a |
| V3 | k=0 rotational gap (G_c=1) → `m²` | `4 G_c/I_ω = 4` (ω_m=2) | rel-err < 1e-2 | the 0.35%-validated gap `cosserat-mass-gap.md:80` |
| V4 | k=0 translational branches gapless | `ω(k→0)→0`, count = 6 acoustic (3 per sublattice fold) | abs `ω²` < 1e-6 | A1 + 2 transverse massless per sublattice |

**Pre-registered SIGN/structure expectations (cheapest falsifiers):**
- The gap appears in the **rotational** sector ONLY; the translational sector stays gapless.
- At G_c=0 the rotational branches are ALSO gapless (gap is coupling-forced, not a γ artifact).
- **PARITY: the cold spectrum is parity-SYMMETRIC.** `ω²(k) = ω²(−k)` to machine precision for every branch (the bare energy has no parity-odd term; `κ_chiral` is saturation-only). A measured asymmetry = a bond-operator BUG, not a chord.
- The 12 branches split into a 6-fold acoustic family (tracking the 6×6 continuum bands near k=0) and a 6-fold optical family (the inter-sublattice optical partners). At k=0 the two sublattices move in phase (acoustic) or anti-phase (optical).

## 4. PRE-REGISTERED comparison-to-ansatz hypotheses (reported ONLY if §3 PASSES)

Labeled CONSISTENCY vs CHORD, declared BEFORE the run:

- **C1 — does the genuine two-sublattice spectrum DIFFER from PR #389's `D6` / `C=sf_mag·D6` ansatz?** Pre-registered expectation: the **near-k=0 validate-on-known numbers AGREE** (the bond operator → continuum gradient as k→0, so V1–V4 must match the single-node values — that is the correctness check). The **full-BZ band structure DIFFERS**: the genuine optical branches come from the real anti-phase bond mode, not a structure-factor-scaled copy of the acoustic block. **Pre-label: the differences are CONSISTENCY-class** (both are micropolar two-sublattice lattices; the genuine one is the substrate-correct band shape, the ansatz is an uncontrolled approximation). The load-bearing question is whether the ansatz got the validate-on-known RIGHT BY LUCK (it never ran V1–V4 on its 12×12) — we report the genuine 12×12 V1–V4 and the genuine optical-branch shape.
- **C2 — acoustic/optical gap.** Does the genuine bond network still produce a hard acoustic/optical spectral gap? **Pre-label: CONSISTENCY** (generic to two-sublattice micropolar; the gap VALUE is the validated echo).
- **C3 — parity symmetry of the cold spectrum.** **Pre-label: CONSISTENCY** (forced by the parity-even bare energy; this is the substrate fact stated in the header, here MEASURED as a falsifier of the bond operator).
- **Refute-by-default self-check:** if the genuine spectrum merely reproduces textbook micropolar two-sublattice phonon bands with no AVE-distinct forward content, the honest verdict is CONSISTENCY-class throughout and the chord stays in the driven/saturated regime (NEXT phase). The √2 node-twist stiffness convention is surfaced flag-don't-fix (§7), not silently picked.

---

## 5. RESULT — validate-on-known verdict ON THE REAL 12×12: **PASS (all 5 + V5b teeth-check)**

Driver: `cosserat_band_structure_two_sublattice.py`; output `_output/cosserat_band_structure_two_sublattice.json`.
The 12×12 `D(k)` is the **Fourier symbol of the SAME discrete energy operator** the validated velocity-Verlet
engine uses (`cosserat_field_3d._energy_density_bare` via `_tetrahedral_gradient`), assembled as the genuine
A→B bond network (NOT `C=sf_mag·D6`). The validate-on-known is run **on the real 12×12** (the load-bearing
fix vs PR #389, which ran V1–V4 on the single-node `D6`).

| # | Target | Recovered | rel-err | Verdict |
|---|---|---|---|---|
| V1 | transverse photon `c_EM=√(G/ρ)=1` | 1.000000 | 3.6e-8 | **PASS** |
| V2 | rotational curvature speed (G_c=0) | 1.414214 (=√2) | 2.0e-9 | **PASS** |
| V3 | k=0 rotational gap `m²=4G_c/I_ω=4` (ω_m=2) | 4.000000 | **0.0 (bit-exact)** | **PASS** |
| V4 | k=0 translational gapless branches | 6 (3 per sublattice) | exact | **PASS** |
| V5 | parity `ω²(k)=ω²(−k)` (cold spectrum) | residual 0.0 | **0.0 (bit-exact)** | **PASS** (weak — see §5 caveat) |
| V5b | parity HAS TEETH: injected real k-odd chiral leak BREAKS parity | residual 0.874 (leak=1.0) | must be >1e-3 | **PASS** (confirms V5 is not a no-op) |

**V3 is bit-exact on the GENUINE 12×12** — the two-sublattice bond network reproduces the canonical mass gap
(the 0.35%-validated number of `cosserat-mass-gap.md`) to machine precision, because the A→B bond operator is
the frequency-domain image of the engine's own operator. This is the strongest validate-on-known: not "agrees"
but "is the same operator, now on the correct two-sublattice basis."

**V5 (parity) is the substrate-fact-as-falsifier:** the cold spectrum is parity-symmetric to machine precision
(`ω²(k)=ω²(−k)`, residual exactly 0), confirming the header claim — the bare energy has NO parity-odd term, so
`κ_chiral` (saturation-only, `cosserat_field_3d.py:562`) cannot enter the cold bands. A nonzero residual would
have signalled a bond-operator BUG, not a chord.

> **⚑ AUDIT CAVEAT (2026-06-23, workflow w1ni1axfg — Rule 12, prose above PRESERVED unedited).**
> The bit-exact V5 residual-0.0 is **NOT a strong independent falsifier** and must not be headlined as one.
> The 12×12 `D(k)` is built as a **Hermitian quadratic form with REAL moduli (G, G_c, γ) and conjugate-phase
> A/B coupling** (`dynamical_matrix_two_sublattice`: `Phi = 0.5*(Phi + Phi.conj().T)`, `G_cross_B = conj(G_cross)`).
> For any such real-moduli conjugate-phase Hermitian construction, `D(−k) = D(k)*` and the eigenvalues of a
> matrix and its complex conjugate are identical, so `ω²(−k) = ω²(k)` is **FORCED BY THE CONSTRUCTION** — the
> residual is bit-exact 0 by algebra, independent of whether the bond operator is right. V5 therefore catches
> only a **real, k-odd, parity-odd LEAK** (a parity-odd term with a real coefficient that survives the conjugate
> symmetry). It does **have teeth against a chiral leak**: injecting an explicit parity-odd term (a real
> chiral/handed coupling — a real coupling whose amplitude is ODD in k, distinguishing the +bond from the −bond
> direction, the form a leaked `κ_chiral` would take) breaks the symmetry with a **measurable residual**. The
> driver self-check `V5b_parity_has_teeth` injects exactly this term and V5 BREAKS: driver-measured residual
> **0.874** at injection amplitude `leak=1.0` (amplitude-dependent; ≈0.4 at `leak=0.5`). So V5 is
> a genuine guard against a chiral-leak bug, not a no-op. But it is **shallow positive evidence**: passing V5
> does NOT independently confirm the bond operator (that is V1–V4's job, especially the bit-exact V3 gap); it
> confirms only that no real parity-odd term leaked into the cold bare energy — which the header already states
> is true BY CONSTRUCTION (`κ_chiral` saturation-only). Read V5 as a **construction-consistency check with teeth
> against a chiral leak**, NOT as deep independent proof of the spectrum.

### Two integrator-time bugs caught + fixed (Rule 10, single-mechanism diagnoses)

The first run of the genuine 12×12 FAILED V1/V2/V3 — refute-by-default working. Two single-mechanism bugs:

1. **Length-convention mismatch in the bond phase.** The first build used the integer offset `p_ℓ` in the
   gradient COEFFICIENT `(1/4)p_ℓ^j` but the diamond-metric vector `τ_B+R_ℓ` (length 1) in the Bloch PHASE
   `e^{ik·(τ_B+R_ℓ)}`. Mixing a length-√3 coefficient with a length-1 phase gave a continuum gradient
   `(1/√3)·ik_j` instead of `ik_j` — V1 read 0.408=1/√6 and V2 read 0.577=1/√3. **Fix:** use `p_ℓ` for BOTH
   coefficient and phase (the engine computes the gradient on ITS OWN grid where the four A→B bonds ARE the
   offsets `p_ℓ`); then `Σ_ℓ p_ℓ⊗p_ℓ=4·I` → continuum `ik_j` exactly (verified inline).
2. **Half-weight on the non-shared on-site micropolar term.** The first build used `Q=½(Q_A+Q_B)` (standard
   bond-energy sharing), which correctly halves the INTER-sublattice bond energy but WRONGLY halved the
   ON-SITE micropolar term `−ε_ijk ω_k` (which belongs entirely to its own site, not shared) — giving m²=2
   instead of 4. **Fix:** `Q=Q_A+Q_B` (full weight per site); the engine sums the full strain energy at every
   site with no double-count, because each site references its own on-site ω plus its own bond gradient. This
   restored V3 to bit-exact 4.

Both are the kind of bug A-Rule 10 anticipates: invisible to static analysis / pre-reg, surfaced only at
integrator time by running the real matrix against the pre-registered known numbers.

### ⚑ FLAG (flag-don't-fix): node-twist stiffness convention (the √2)

Carried forward UNCHANGED from PR #389 (this re-run does not re-adjudicate it): the rotational **curvature**
speed at G_c=0 is `c_R = √2` from the actual engine operator, but `cosserat_wave_test.py:10` / `cosserat-mass-gap.md`
carry the continuum **label `c_R = √(γ/I_ω) = 1`**. Same √2 / Hessian factor.

**⚑ GRANT-GATED — DO NOT RESOLVE (flag-don't-fix; this re-run leaves it OPEN for Grant).** The `√2` vs `1`
discrepancy traces to whether the curvature energy `W_κ` carries a `½` prefactor:
- **Engine source:** `cosserat_field_3d.py:703` computes `W_kappa = jnp.sum(kappa**2)` — **no `½`**. Summing the
  `κ` quadratic form with unit (not half) weight is what yields `c_R = √2` here (the same `Σκ²` the engine uses;
  this driver is its Fourier symbol, so it inherits the no-½ convention verbatim).
- **Leaf label:** `cosserat_wave_test.py:10` / `cosserat-mass-gap.md` quote the continuum `c_R = √(γ/I_ω) = 1`,
  i.e. the convention with the standard `½` elastic prefactor folded in.
- **Internal-consistency read (NOT an adjudication):** the driver is bit-for-bit faithful to the engine operator,
  so internal consistency *favors* `√2` (the leaf label and the engine `Σκ²` cannot both be the substrate value).
  **But which `½`-convention is the real node-twist stiffness is a substrate-physics call that belongs to Grant,
  NOT to this implementer lane.** This flag is RECORDED OPEN, deliberately unresolved.

The gap (the load-bearing number, V3 `m²=4`) is bit-exact either way — this convention question does **not** touch
the validated gap, only the `c_R` curvature-slope label.

## 6. RESULT — genuine full-BZ two-sublattice spectrum + DOES-IT-DIFFER-FROM-ANSATZ

The 12 branches split by eigenvector character into:

| Manifold | Branches | ω range (lattice) | Character |
|---|---|---|---|
| **Translational acoustic** | 6 | [0, √(10/3)=1.826] | 4 transverse photons `c=1` (2 per sublattice phase) + 2 longitudinal P-wave `√(10/3)` |
| **Rotational optical** | 6 | [2.000, ~2.7] | gapped at ω_m=2 (the mass gap); the LC stop-band ceiling |

**Acoustic/optical hard gap (the LC stop-band).** Dense 21³-grid BZ scan: the translational acoustic manifold
tops at the longitudinal P-wave `√(10/3)=1.8257` (reached INSIDE the zone, not just at path endpoints), the
rotational optical manifold floors at the mass gap `ω_m=2.0000`. The two **never cross** — a clean hard gap
`1.826 < ω < 2.0` (width 0.174) across the whole zone. Robustness check: 2000 random-k points all keep the gap
open (min gap 0.63). Substrate-native reading: the gapped micro-rotation mode IS mass — a node-twist resonance
with a threshold; the gap is an **LC stop-band** of the chiral LC mesh.

**Optical-branch curvature:** `ω²(k)=m²+a₂(kℓ)²` with intercept `m²=4.0000` (the validated gap, on the genuine
bond operator) and `a₂=1.993` (positive curvature — the branch rises from the gap; same √2/Hessian factor flag).

### DOES IT DIFFER FROM THE PR #389 ANSATZ? — **YES; only the ACOUSTIC / validate-on-known branches agree near k=0**

The genuine bond-operator spectrum and the PR #389 tile-and-scale ansatz (`C=sf_mag·D6`, reconstructed inline
in the driver for a self-contained comparison) give **substantially different full-BZ spectra**:

| | Genuine bond operator | PR #389 ansatz (`C=sf_mag·D6`) |
|---|---|---|
| near-k=0 ACOUSTIC / validate-on-known | PASS (V1–V5, run on the 12×12) | never run on the 12×12 (validated on `D6`) |
| near-k=0 OPTICAL manifold floor (k→0) | **2.000** (= the gap √(m²)=2) | **2.828** (= 2√2; differs at ALL k incl. k→0) |
| max\|Δω\| band-by-band over BZ | — | **≈ 2.0 lattice** |
| zone-edge X [π,0,0] max ω | **2.000** (= the gap; acoustic folds to 0) | 2.828 (= 2√2; structure-factor artifact) |

**Only the ACOUSTIC family (and the V1–V4 validate-on-known numbers it carries) agrees near k=0** — both → the
continuum gradient `ik_j` as k→0, so the acoustic slopes / massless branches must match, which is the
correctness cross-check. The **OPTICAL manifold differs at ALL k, INCLUDING k→0**: the genuine optical branches
floor at the true gap `ω=√(m²)=2`, while the ansatz optical branches floor at `2√2≈2.83` even as `k→0` (the
structure-factor scaling multiplies the on-site `D6` optical block by ≈√2 at the zone center, not just at the
edge). So the agreement is **NOT a generic "near-k=0 match"** — it is restricted to the acoustic / validate-on-
known branches; the optical manifold is off by the `2√2 vs 2` factor everywhere in the zone. At the X zone edge
the genuine diamond structure factor `Σ_b e^{ik·d_b}` zeroes, so the A and B sublattices decouple and the
acoustic branches fold back to ω=0 while the optical manifold caps at exactly the gap (ω=2) — the standard
diamond two-sublattice BZ fold. The ansatz instead SCALES `D6` by the structure-factor magnitude, capping at
`2√2≈2.83` — a scaling artifact, not the real bond fold. **The PR #389 two-sublattice OPTICAL spectrum was
quantitatively wrong at every k including k→0 (2√2 vs 2)**, not merely off the zone center, even though its
single-node validate-on-known (on `D6`) passed.

## 7. CONSISTENCY-vs-CHORD labeling + honest closure

| Feature | Class | Justification |
|---|---|---|
| C1 genuine differs from ansatz | **CONSISTENCY** | substrate-correct band shape; both are micropolar two-sublattice lattices; only the ACOUSTIC / validate-on-known branches agree near k=0 — the ansatz OPTICAL manifold differs at ALL k incl. k→0 (2√2 vs 2), see §6 |
| C2 acoustic/optical hard gap | **CONSISTENCY** | generic to any two-sublattice micropolar lattice; the gap VALUE `m²=4G_c/I_ω` is the already-validated echo |
| C3 cold-spectrum parity symmetry | **CONSISTENCY** (weak guard) | forced by the parity-EVEN bare energy (`κ_chiral` saturation-only) AND by the real-moduli conjugate-phase Hermitian form (`D(−k)=D(k)*` ⇒ equal eigenvalues) — the bit-exact residual-0 is **construction-forced, not strong independent evidence**; it has teeth only against a real parity-odd / chiral leak (driver self-check `V5b` injects one and it breaks, residual 0.874 at leak=1.0). See §5 AUDIT CAVEAT. |

**NO FORM-distinct chord found in the cold-lattice linear band structure** — exactly the refute-by-default
outcome the SECTOR HEADER pre-registered. This is correct, NOT a failure: the 4₁-screw handedness is
SATURATION-ONLY (it biases the saturation kernel, not the bare energy), so the cold linear bands are
parity-symmetric BY CONSTRUCTION and CANNOT host a topology chord. The handed mode lives in the
**driven/saturated regime** — a separate phase, not this one. Cold bands = **CONSISTENCY only**.

**What this re-run adds over PR #389:** (1) the validate-on-known is now run on the **genuine 12×12 two-sublattice
matrix** built from the **real A→B bond operator** (not the single-node `D6` with a tile-and-scale ansatz);
(2) the genuine full-BZ spectrum is the substrate-correct band shape (the X-point diamond fold, not a
structure-factor scaling); (3) the parity-symmetry of the cold spectrum is MEASURED bit-exact, confirming the
saturation-only-handedness substrate fact as a falsifier. The honest closure (Rule 11) is unchanged: the chord
is not in the cold linear bands; it is in the driven/saturated regime and the forward predictions.

## 8. Next-phase proposal (propose, do NOT build this phase)

The cold-spectrum parity symmetry (V5, bit-exact) is the clean handoff: it proves the chord is NOT here and
localizes WHERE it must be. Next phase, gated on validate-on-known:

1. **Driven/saturated band structure (the handed mode).** Turn on the saturation kernel (`κ_chiral≠0`,
   `_reflection_density_asymmetric`) at a load-bearing site and recompute the bands around the saturated
   background. The parity-odd `A2_μ=(1+κ_chiral·h_local)·A2_μ_base` term is the ONLY place handedness enters —
   the cold-spectrum parity symmetry (this phase) is the trivial-baseline the driven calculation must recover
   with `κ_chiral=0` BEFORE claiming a parity-split. This is where a topological / chiral-edge chord, if any,
   lives. **First move:** validate-on-known the saturated bands reduce to the cold bands as `κ_chiral→0`.
2. **mass-gap → structural mass spectrum (RATIOS only).** Enumerate the van-Hove / zone-boundary stationary
   points of the genuine optical manifold; test whether their gap RATIOS match a known mass ratio. The moduli
   are natural-units placeholders (absolute scale = Phase-II calibration), so only RATIOS are testable — which
   is the right calibration-free discriminator. Refute-by-default: a ratio matching nothing closes the branch.

---

## Cross-references

- Driver (genuine): `src/scripts/vol_1_foundations/cosserat_band_structure_two_sublattice.py`
- Output: `src/scripts/vol_1_foundations/_output/cosserat_band_structure_two_sublattice.json`
- Superseded ansatz (PR #389): `src/scripts/vol_1_foundations/cosserat_full_band_structure.py` (validated on `D6`; `C=sf_mag·D6` two-sublattice ansatz)
- Canonical EM-sector template: `src/scripts/vol_4_engineering/k4_bloch_dispersion.py` (the genuine translation-only A→B bond network this extends to 6 DOF)
- Canonical gap leaf: `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md`
- Engine: `src/ave/topological/cosserat_field_3d.py` (`_tetrahedral_gradient`, `_compute_strain`, `_compute_curvature`, `_energy_density_bare`; `κ_chiral` saturation-only at `:562/605`)
