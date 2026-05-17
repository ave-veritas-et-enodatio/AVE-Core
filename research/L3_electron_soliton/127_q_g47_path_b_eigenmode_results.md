# 127 — Q-G47 Path B: K=2G Eigenmode Extraction Results — PARTIAL PASS with ambiguities

**Date:** 2026-05-16 late evening
**Branch:** `research/l3-electron-soliton`
**Status:** **STRUCTURAL PASS at K=2G operating point** (clean 1/7, 2/7 fractions emerge exactly). **NUMERICAL PROXIMITY** of soft-shear eigenvalue to u_0* target (4/21 ≈ 0.190 vs 0.187; 2% match). **INTERPRETATION AMBIGUOUS** — eigenvalue is not a displacement amplitude, so identification with "u_0*" is not literal.
**Per Grant directive 2026-05-16 late evening:** "yes proceed and make sure to fully challenge and report results, ask me about any ambiguities."
**Script:** `src/scripts/verify/q_g47_path_b_k4_eigenmode.py`
**JSON cache:** `src/scripts/verify/q_g47_path_b_k4_eigenmode_results.json`

---

## §0 TL;DR

Per doc 126 Path B recommendation: extended the Q-G47 Session 15 Keating
K4 scaffold with full 9-DOF Hessian + `scipy.linalg.eigh` eigenvalue
extraction at the K=2G operating point.

**Three concrete results, all derived analytically AND verified numerically**:

1. **K=2G locates at k_θ/k_a = 1/7 EXACTLY** with K_relaxed = 4/9,
   G_relaxed = 2/9, ν = 2/7 — the AVE canonical vacuum Poisson ratio.
   Analytical derivation: K_relaxed = 4k_a/9, G_relaxed = 2k_a·k_s/(k_a+2k_s),
   constraint K=2G gives 7k_s = k_a EXACTLY (§4.5.3).

2. **Soft shear eigenvalue λ_G = (4/3)·k_s = 4/21 ≈ 0.1905** —
   E-irrep deviatoric mode of the K4 cubic group (the (1,-1,0) and
   (1,1,-2) deviatoric directions). KEY structural fact:
   **E-irrep has ZERO axial bond deformation** by K4 symmetry, so
   λ_G depends ONLY on bond-bending k_s, not stretching k_a (§4.5.5).
   Within 2% of A-029 target u_0* = 0.187, within 4% of p* = 8πα = 0.18335.

3. **Bulk mode eigenvalue λ_K = (4/3)·k_a = 4/3, frequency ratio ω_K/ω_G = √7**
   — clean ratio reflecting the K=2G constraint 7ν=2 (§4.5.6).
   Bulk mode is A₁ irrep, pure axial deformation, ZERO transverse and ZERO
   internal-mode coupling (§4.5.4).

**Verdict (fully challenged + analytically verified + axiom-reviewed)**:

- **STRUCTURAL PASS at K=2G operating-point construction (Cauchy K4)** —
  k_s = k_a/7, ν = 2/7, K = 4k_a/9, G = 2k_a/9 all EXACT
- **ANALYTICAL DERIVATION COMPLETE for Cauchy-K4 eigenvalues** — 4/3 (bulk)
  and 4/21 (soft shear) from K4 cubic irrep decomposition
- **NUMERICAL PROXIMITY** at 2% level: λ_G = 4/21 ≈ 0.1905 vs A-029 u_0* = 0.187
- **CRITICAL GAP**: Path B is **CAUCHY-Keating, NOT Cosserat-Keating** —
  missing 3 microrotational DOFs per node (Axiom 1 specifies 6 DOFs: 3 trans
  + 3 rot, Path B uses only 3 trans). See §6.7 for full axiom-review.
- **THE 0.187 PROXIMITY DOES NOT CONSTITUTE COSSERAT VERIFICATION** — could
  be (α) Cauchy projection of deeper Cosserat result, (β) coincidence, or
  (γ) real eigenvalue with intrinsic discrepancy from 0.187 / p*

**Required for full Axiom-1 compliance**: extend scaffold to 12 DOFs per
unit cell (6 strain + 3 translation + 3 microrotation), add explicit
Cosserat couple-stress moduli α, β, γ + chiral coupling. ~1-2 sessions of
additional work. NOT done in Path B.

**Seven ambiguities surfaced for Grant adjudication** in §6 (six original
+ Ambiguity 7 = axiom-review gap).

---

## §1 Setup: extending Session 15 Keating scaffold

### §1.1 What was added to the Session 15 framework

Session 15 (`q_g47_session15_k4_cosserat_stabilized.py`) provided:
- `KeatingBond` class with axial $k_a$ + bending $k_\theta$ stiffnesses
- `unit_cell_energy_keating()` for arbitrary strain + internal-mode displacement
- `relaxed_energy_keating()` via BFGS on internal DOF
- `extract_KG_relaxed()` for static K/G extraction

Path B adds (in `q_g47_path_b_k4_eigenmode.py`):
- **9-DOF Hessian** built via numerical 4-point mixed second differences
  - DOFs: 6 macro-strain components + 3 internal optic-mode components
- **`scipy.linalg.eigh(H, M)`** for full eigenvalue decomposition
- **Channel projections** of eigenvectors onto K-channel (hydrostatic
  strain, 1 dim), G-channel (deviatoric strain, 5 dims), internal channel
  (optic-mode displacement, 3 dims)
- **`brentq` operating-point locator** for k_θ/k_a* such that K_relaxed
  = 2 G_relaxed

### §1.2 K=2G operating point (Step 1 result)

| Quantity | Value | Notes |
|---|---|---|
| k_θ/k_a* | **1/7** = 0.142857 | EXACT (brentq converged to 10⁻¹⁰) |
| K_relaxed* | **4/9** = 0.444444 | EXACT |
| G_relaxed* | **2/9** = 0.222222 | EXACT |
| K/G | 2.000000 | by construction |
| **ν Poisson** | **2/7** = 0.285714 | EXACT, matches AVE canonical |
| (ℓ_c/d)² continuous (Session 17) | 6 | structural derivation |
| Discrete k_θ/(k_a · d²) | 0.143 | numerical result |
| **DISCREPANCY** | factor 42 | discrete-continuous prefactor |

**Observation 1**: Both k_θ/k_a = 1/7 and ν = 2/7 are clean fractions
with denominator 7. The 7 comes from the algebraic constraint K=2G in
3D isotropic elasticity:
$$\frac{K}{G} = \frac{2(1+\nu)}{3(1-2\nu)} = 2 \;\Rightarrow\; 7\nu = 2$$

So the 7 is the **constraint dimension** at K=2G. The 1/7 in the bond
ratio is a non-trivial consequence — the Keating K4 model self-engineers
to this clean value at the operating point.

**Observation 2** (CHALLENGE): The discrete k_θ/k_a = 1/7 ≈ 0.143 vs
Session 17's continuous prediction (ℓ_c/d)² = 6 differ by a factor of 42
(= 6 × 7). This means EITHER:
- (a) Session 17's prefactor "2" in χ_K = 2(ℓ_c/d)² is wrong, or
- (b) The discrete-continuous mapping k_θ/(k_a · d²) ↔ (ℓ_c/d)² has an
      additional dimensionless prefactor not captured by Session 16's dictionary
- (c) The continuous picture targets χ_K = 12 (per A-032) and that's
      NOT the K=2G operating point — it's a different operating point

**Reading**: option (c) is most consistent — A-032's χ_K = 12 is the
Cosserat **dressing coefficient**, not the K=2G operating-point bond
ratio. They're different physical quantities.

---

## §2 Eigenvalue spectrum at K=2G

### §2.1 The 9 eigenvalues (Step 2 result)

```
λ_0 = +0.190476      ← soft shear, doubly degenerate
λ_1 = +0.190476
λ_2 = +0.486434      ← mixed shear+internal, triply degenerate
λ_3 = +0.486434
λ_4 = +0.486434
λ_5 = +1.333333      ← pure bulk, singlet
λ_6 = +3.132614      ← high-freq mixed, triply degenerate
λ_7 = +3.132614
λ_8 = +3.132614
```

**Exact identifications**:
- λ_0 = λ_1 = **4/21** = 0.1904762
- λ_5 = **4/3** = 1.3333333
- Frequency ratio ω_K/ω_G = √(λ_K/λ_G) = √((4/3)/(4/21)) = √7 ≈ 2.6458

**Group theory consistency**: For K4 cubic symmetry (proper rotation
group $T$ with |T|=12), the strain representation $S^2(\mathbb{R}^3)$
decomposes as $A_1 \oplus E \oplus T_2$ (1+2+3 dimensions = 6).
Cf. eigenvalue degeneracies: 1 (bulk, $A_1$) + 2 (shear, $E$) + 3 (shear,
$T_2$) + 3 (internal modes, $T_1$ or $T_2$).
**Degeneracy pattern matches** ✓.

### §2.2 The 4/21 vs 0.187 question

The soft shear eigenvalue **λ_G = 4/21 ≈ 0.190476** is the closest
match to A-029's u_0* = 0.187 among the spectrum.

Numerical comparison:
| Target | Value | Δ vs 4/21 | Fractional |
|---|---|---|---|
| u_0* (A-029 magic angle) | 0.187 | +0.00348 | +1.86% |
| p* = 8πα (fabric weave density) | 0.18335 | +0.00713 | +3.89% |
| √(1/28) (K_0/G_0=14/9 magic angle) | 0.18898 | +0.00149 | +0.79% |
| √(1/42) (K_0/G_0=5/3 magic angle) | 0.15430 | +0.03618 | +23.5% |
| (r_sec/d - 1) over-bracing | 0.187 | +0.00348 | +1.86% |

**The closest match is √(1/28) = 0.189** which corresponds to the
K_0/G_0 = 14/9 (ν=0.235) variant of the magic-angle equation —
**NOT** the Cauchy-baseline K_0/G_0 = 5/3 form.

This is consistent with my doc 124 §3.2 finding that **exact match to
0.187 requires K_0/G_0 = 14/9, not 5/3**.

### §2.3 What does λ_G represent physically?

λ_G is the **soft shear eigenvalue of the strain Hessian** at the K=2G
operating point. Dimensionally:

$$\lambda_G = \left.\frac{d^2 U}{dx^2}\right|_{x=0}\bigg/\text{(mass)}$$

This is **[stiffness] / [mass] = [ω²]** if interpreted as a vibrational
frequency squared.

To compare to u_0* (a dimensionless **displacement amplitude**),
need additional reasoning:

- **Direct comparison numerical**: λ_G = 4/21 ≈ 0.190 vs u_0* = 0.187
  ⇒ proximity within 2%, but units don't match
- **As scaled u_0**: if u_0 is taken to be a NORMALIZED amplitude such
  that the soft-shear mode's restoring stiffness IS u_0 in some specific
  units, then identification is coherent
- **As thermal RMS**: u_0_rms² ∝ kT/(M·λ_G) → larger λ_G means smaller
  thermal amplitude. With T = T_CMB = 2.725 K and substrate-mass units,
  u_0_rms = √(kT/(M·λ_G)) — but lattice units don't give physical scale
  without additional input

**No interpretation is unambiguously the right one**. The numerical
proximity is suggestive but doesn't constitute a literal identification.

---

## §3 Eigenvector projections (Step 3 result)

For each eigenmode, project the eigenvector onto K-channel (hydrostatic),
G-channel (deviatoric), and internal channel:

| Mode | λ | K_amp | G_amp | int_amp | K_frac | G_frac | int_frac |
|---|---|---|---|---|---|---|---|
| 0,1 | 0.190 | 0.000 | 1.000 | 0.000 | 0% | **100%** | 0% |
| 2,3,4 | 0.486 | 0.000 | 0.963 | 0.732 | 0% | 80% | 60% |
| 5 | 1.333 | **1.000** | 0.000 | 0.000 | **100%** | 0% | 0% |
| 6,7,8 | 3.133 | 0.000 | 1.035 | 0.681 | 0% | 84% | 55% |

**Critical structural fact**: Modes 0,1 (the soft shear eigenstates at
λ_G = 4/21) are **PURE external shear** with **ZERO** coupling to the
internal optic mode. The Cosserat dressing (internal-mode coupling)
appears only in Modes 2,3,4 (at λ=0.486) and Modes 6,7,8 (at λ=3.13).

**Question**: which eigenmode IS the "K=2G operating point eigenmode"?

- **Option (i)**: the soft shear mode (0,1) — lowest frequency, purely
  shear, no Cosserat. Argument: this is what dominates at the operating
  point because it's lowest energy.

- **Option (ii)**: the bulk mode (5) — pure K-channel, λ_K = 4/3 = 2·(2/3).
  Argument: this is the K-mode itself.

- **Option (iii)**: the mixed shear+internal modes (2,3,4) — these are
  the ones with Cosserat dressing structure, hence the magic-angle
  physics.

- **Option (iv)**: the relevant quantity is the eigenvalue RATIO ω_K/ω_G
  = √7 ≈ 2.65, not any one eigenvalue.

**Cannot disambiguate without additional input from Grant on what "the
K=2G eigenmode" precisely means in his framing.**

---

## §4 Amplitude ratios — no clean 0.187 match

For each mode with non-zero coupling, compute amplitude ratios that could
candidate-match 0.187:

| Mode | int_amp/G_amp | G_amp/total | int_amp/(G+int) |
|---|---|---|---|
| 2,3,4 | 0.760 | 0.796 | 0.432 |
| 6,7,8 | 0.658 | 0.835 | 0.397 |

**None of these amplitude ratios match 0.187** at any meaningful precision.

The eigenvector projections do NOT give a number close to 0.187 in any
obvious normalization.

**Implication**: if the framework's "u_0*" is supposed to be an
eigenvector amplitude (per Picture A in primer Q-G47 section), then the
discrete Keating K4 scaffold does NOT directly produce 0.187 as an
eigenvector amplitude. Only the soft shear EIGENVALUE (4/21 ≈ 0.190)
is close.

---

## §4.5 Analytical derivation of the eigenvalue structure (added post-numerical)

The numerical eigenvalues turn out to be **exact rationals derivable by hand**.
Documenting the closed-form derivations so this is a real analytical
verification, not just a numerical curve fit.

### §4.5.1 K_relaxed = 4 k_a / 9

For uniform strain ε_xx = ε_yy = ε_zz = α (so trace = 3α):
- Each bond direction n̂_i has |n̂_i| = 1
- ε·n̂_i = α n̂_i (since ε = α·I)
- Axial: (n̂·ε·n̂) = α for every bond
- Transverse: ε·n̂ - n̂(n̂·ε·n̂) = α n̂ - α n̂ = 0 (pure axial)
- Cross-term to internal mode: (k_a - k_s)·Σ(n̂·ε·n̂)(n̂·u_int) involves
  Σ n̂_i = 0, so **NO coupling between bulk strain and internal mode**

So K_relaxed = K_rigid:
$$U_K = \frac{1}{2} k_a \cdot 4\alpha^2 = 2 k_a \alpha^2$$
$$K = \frac{2 U_K}{(3\alpha)^2} = \frac{4 k_a}{9}$$

✓ exact, matches numerical.

### §4.5.2 G_relaxed = 2 k_a k_s / (k_a + 2 k_s)

For pure ε_xy = γ/2 (engineering shear γ), each bond's axial component is
n_x n_y γ. For K4 bonds, (n_x n_y) takes values ±1/3, giving axial² = γ²/9
per bond, sum = 4γ²/9. Transverse² per bond = γ²/18, sum = 2γ²/9.

Including internal-mode relaxation, only the c-component of u_int couples
to γ (z-axis is the special direction perpendicular to the xy-shear plane).
Computing the Hessian block + minimizing over c gives (full derivation in
`/tmp/analytical_verify.py`):

$$G_{\text{relaxed}} = \frac{2 k_a k_s}{k_a + 2 k_s}$$

✓ exact, matches numerical (at k_a=1, k_s=1/7: G = 2/9).

### §4.5.3 K = 2G solution: k_s = k_a / 7

Setting K_relaxed = 2 G_relaxed:
$$\frac{4 k_a}{9} = \frac{4 k_a k_s}{k_a + 2 k_s}$$
$$k_a + 2 k_s = 9 k_s$$
$$\boxed{k_s = k_a / 7}$$

✓ EXACT analytical result. The 1/7 in the bond ratio at K=2G is **forced
by the algebraic constraint structure**, not a numerical coincidence.

### §4.5.4 λ_K = (4/3) k_a (bulk eigenvalue, A₁ irrep)

For the bulk eigenvector (1/√3)(1,1,1,0,0,0,0,0,0):
- Strain ε_xx = ε_yy = ε_zz = 1/√3
- α = 1/√3, U = 2 k_a · (1/3) = (2/3) k_a
- Eigenvalue = 2U/||v||² = **(4/3) k_a**

At k_a = 1: λ_K = 4/3 ≈ 1.3333 ✓

### §4.5.5 λ_G = (4/3) k_s (E-irrep shear eigenvalue) — THE KEY RESULT

For the E-irrep deviatoric direction D1: ε_xx = +ε, ε_yy = -ε, ε_zz = 0.

For each K4 bond direction n̂_i = (±1, ±1, ±1)/√3:
- n̂·ε·n̂ = n_x²·ε - n_y²·ε = (1/3)·ε - (1/3)·ε = **0** ← KEY FACT
- |ε·n̂|² = n_x²·ε² + n_y²·ε² = 2ε²/3
- transverse² = |ε·n̂|² - (n̂·ε·n̂)² = 2ε²/3 - 0 = **2ε²/3**

The E-irrep shear has **NO axial bond deformation** — the K4 symmetry
forces the (1, -1, 0) and (1, 1, -2) deviatoric directions to deform
bonds only transversely. So the E-mode eigenvalue depends ONLY on k_s,
not k_a.

Per-bond transverse energy: (1/2)·k_s·(2ε²/3) = k_s ε²/3
Sum 4 bonds: (4 k_s/3) ε²

For unit normalized eigenvector (ε = 1/√2):
U(normalized) = (4 k_s/3)·(1/2) = 2 k_s/3
Eigenvalue = 2·U/||v||² = **(4/3) k_s**

At k_s = 1/7 (K=2G operating point):
$$\boxed{\lambda_G = \frac{4}{3} \cdot \frac{1}{7} = \frac{4}{21} \approx 0.190476}$$

✓ EXACT analytical result.

### §4.5.6 Frequency ratio ω_K/ω_G = √(k_a/k_s)

$$\frac{\omega_K}{\omega_G} = \sqrt{\frac{\lambda_K}{\lambda_G}} = \sqrt{\frac{(4/3) k_a}{(4/3) k_s}} = \sqrt{\frac{k_a}{k_s}}$$

At K=2G operating point: ω_K/ω_G = √7 ≈ 2.6458.

### §4.5.7 The structural identity (4/21 = (4/3)·(1/7))

The soft shear eigenvalue 4/21 decomposes into TWO factors with clean
physical meanings:

- **(4/3)** = K4 lattice geometric prefactor (from 4 bonds × tetrahedral coordination × 1/3 dimensional factor)
- **(1/7)** = bond-bending ratio k_s/k_a at K=2G operating point (from 7ν=2 constraint)

So 4/21 = (4/3)·(1/7) is the product of K4 geometry × K=2G constraint.

The numerical proximity to 0.187 = u_0* requires asking: is **0.187 ≈ (4/3)·(1/7)**?

- (4/3)·(1/7) = 0.190476
- 0.187 vs 0.190476 → **1.86% gap**
- 0.18335 (= p* = 8πα) vs 0.190476 → **3.89% gap**

The gap is NOT zero. So either:
- (i) The discrete Keating K4 has an intrinsic 4/21 that's structurally
      different from u_0* = 0.187 and p* = 0.183, OR
- (ii) The discrete result has a discretization correction that closes
      the 2-4% gap in the continuum limit

**Verifying (ii) requires either a multi-site convergence study OR a
continuous-field analytical derivation showing how (1/7) becomes p* = 8πα
in the continuous K4 Cosserat limit.** Neither is done by Path B.

---

## §5 What does match: structural numerology

The Keating K4 K=2G scaffold produces a STRUCTURALLY CLEAN spectrum with
deep number-theoretic content:

| Result | Value | Structural origin |
|---|---|---|
| k_θ/k_a* | 1/7 | K=2G constraint (7ν=2 in 3D isotropic) |
| ν Poisson | 2/7 | same |
| K_relaxed* | 4/9 | K4 coordination × axial stiffness × 1/9 dim |
| G_relaxed* | 2/9 | half of K (by construction K=2G) |
| λ_G | 4/21 | K_relaxed · 3/7 = G_relaxed · 6/7 |
| λ_K | 4/3 | 3 × K_relaxed |
| ω_K/ω_G | √7 | (4/3)/(4/21) = 7 → ω-ratio = √7 |
| Mode degeneracies | 1+2+3+3 | matches K4 strain irrep decomp $A_1 \oplus E \oplus T_2$ |

This is a "clean" result in the sense that all eigenvalues are
simple rationals (4/21, 4/3) and reflect the K=2G constraint
dimension 7.

**The 0.190 ≈ 0.187 proximity is consistent with**:
- (i) Real structural identity at the continuous-field level with
      ~few% discretization corrections (Session 16 framing — discrete
      Keating is just discretization of continuous Cosserat field)
- (ii) Coincidence among small numbers in K4 physics

Without a closed-form derivation showing (4/21)_discrete →
(0.187)_continuous in the d/ℓ_node → 0 limit, can't resolve.

---

## §6 SIX AMBIGUITIES SURFACED FOR GRANT ADJUDICATION

Per "ask me about any ambiguities" directive:

### §6.1 Ambiguity 1: Which eigenmode IS "the K=2G mode"?

The spectrum has 9 eigenmodes at K=2G. Four candidates per §3:
- (i) Soft shear (Modes 0,1) at λ=4/21
- (ii) Pure bulk (Mode 5) at λ=4/3
- (iii) Mixed shear+internal (Modes 2,3,4) at λ=0.486
- (iv) The ratio ω_K/ω_G = √7

Which is "the" magic-angle eigenmode in your framing? Or is it a
combination?

### §6.2 Ambiguity 2: Eigenvalue vs eigenvector identification

λ_G = 4/21 ≈ 0.190 is an **EIGENVALUE** (stiffness/ω²), not an
amplitude. u_0* = 0.187 is a **DIMENSIONLESS AMPLITUDE** (in A-029
framing). Identifying them requires a specific dimensional convention.

Is your intended identification:
- (a) Numerical equality up to discretization corrections (current
      reading)
- (b) Thermal RMS amplitude u_0_rms = √(kT/(M·λ_G)) at T_CMB
      (requires physical mass scale)
- (c) Something else (specify)?

### §6.3 Ambiguity 3: Discrete-continuous prefactor

Discrete k_θ/k_a = 1/7 at K=2G vs continuous (ℓ_c/d)² = 6 (Session 17)
differ by factor 42. Three reconciliation options:

- (a) Session 17's prefactor "2" in χ_K = 2(ℓ_c/d)² is wrong → χ_K = 12
      forces (ℓ_c/d)² = 12, not 6
- (b) The discrete-continuous mapping needs an additional factor of
      42 (= 6 × 7)
- (c) χ_K = 12 is NOT the K=2G operating point bond ratio — they're
      different physical quantities (this is my current best reading)

Which is your intended framing?

### §6.4 Ambiguity 4: Cauchy 5/3 vs ν=2/7 reconciliation

Session 2 derived K_0/G_0 = 5/3 (ν = 1/4) as the "Cauchy baseline."
Session 6 §3.2 magic-angle equation uses K_0/G_0 = 5/3.
But the K=2G operating point requires K/G = 2 (ν = 2/7).

So the framework has:
- Baseline (u_0 = 0): K/G = 5/3 (Cauchy)
- Operating point (u_0 = u_0*): K/G = 2 (magic angle)
- Difference: dressing by Cosserat couple-stress

The Keating scaffold's k_θ/k_a sweep moves K/G from ∞ → 0 monotonically.
At k_θ/k_a = 0.15: K/G = 5/3 (Cauchy baseline).
At k_θ/k_a = 1/7: K/G = 2 (magic angle).

So k_θ/k_a is acting as the "dressing parameter" in the discrete model
— BUT it's NOT u_0. It's a different control variable.

How do we map "u_0 = dressing amplitude" to "k_θ/k_a = bond ratio"
in your framing? Without that mapping, can't translate u_0* = 0.187 to a
specific k_θ/k_a* operating point that should give specific eigenvalues.

### §6.5 Ambiguity 5: Discretization artifact vs real result?

Session 16 reframed Sessions 12-15 as "discretization of continuous
Cosserat field." Under that reading, the discrete eigenvalues are
APPROXIMATIONS to the true continuous-field eigenvalues with O(d/L)
corrections where L is the macroscopic length scale.

If the true continuous-field eigenvalue is exactly p* = 8πα = 0.18335,
the discrete result 4/21 = 0.19048 is **3.9% off**, consistent with
expected discretization error.

Question: does this 3.9% gap close in the continuum limit, or does the
discrete K4 lattice have its own intrinsic 4/21 result that's
structurally distinct from the continuous prediction?

(Settling this requires a 2-site → 4-site → 8-site convergence study.
Path B as scoped doesn't do this; Sessions 18+ would.)

### §6.5b Ambiguity 5b (NEW from analytical derivation): 4/21 vs p* = 8πα

The analytical eigenvalue **λ_G = (4/3)·(1/7) = 4/21 ≈ 0.190476** has a
clean two-factor structure:
- **(4/3)**: K4 lattice geometry prefactor (4 bonds × tetrahedral × dim)
- **(1/7)**: K=2G constraint bond ratio (from 7ν=2)

For this to equal p* = 8πα = 0.18335 EXACTLY, would need either:
- **(α) Discretization correction**: discrete (4/3)·(1/7) → continuous
      8π/137.036 with 3.9% correction in lattice→continuum limit. Plausible
      but unproven.
- **(β) Structural identity**: 4/(3·7) ≡ 8π/137 modulo some α-suppressed
      correction. Specifically: 4/(3·7) = 0.190476, vs 8π/137.036 = 0.18335,
      relative difference 0.0389 ≈ 5α (since 5α ≈ 0.0365). The 5α-correction
      could come from electroweak loop dressing at the substrate scale.
- **(γ) Different operating point**: maybe K=2G in continuous Cosserat
      isn't exactly the K=2G in discrete Keating; there's a renormalization
      from discrete→continuous.

This is a SPECIFIC TESTABLE QUESTION: is the continuous-field Cosserat
eigenvalue of the K=2G E-irrep shear mode equal to:
- 0.190476 = (4/3)(1/7) (discrete prediction), OR
- 0.18335 = 8π/α^(-1) (p* prediction)?

Path C (continuous-field analytical, doc 125) would resolve this. Not
done by Path B.

### §6.6 Ambiguity 6: Mode 2,3,4 at λ=0.486 — significance?

Modes 2,3,4 are the "Cosserat-dressed shear modes" — only modes with
both G_amp > 0 and int_amp > 0. Their eigenvalue is λ = 0.486 ≈ 1/2.

The exact eigenvalue is 0.486434, which is suspiciously close to 1/2.

Is this a meaningful structural quantity? 1/2 corresponds to ν = 0 in
3D isotropic (incompressible-shear). Or it could be 2/3 - 1/6 (some
specific decomposition).

Or — more interestingly — could the "K=2G mode" Grant means actually be
THIS mode (with Cosserat dressing) rather than the pure-shear soft mode
(0,1) without dressing?

If λ_mixed = 1/2 is the right eigenvalue, then **0.500 vs 0.187** does
NOT match — different ballpark entirely.

---

## §6.7 CRITICAL: Axiom review reveals Path B is incomplete

Per Grant directive "review the axioms" (2026-05-16 late evening), I re-read
Vol 1 Ch 1 + canonical axiom files. Path B violates / partially honors:

### §6.7.1 Axiom 1 — Cosserat micropolar (6 DOFs per node) — **VIOLATED**

Per Axiom 1 canonical statement (`eq_axiom_1.tex:20`, `axiom-definitions.md:12`):

> "Each node is **micropolar** (Cosserat-type), carrying **six intrinsic
> degrees of freedom** per node: three **translational** (capacitive
> coupling ε₀, identified with the electric field) and three
> **microrotational** (inductive coupling μ₀, identified with the magnetic
> field). **The Cosserat microrotational DOF IS the substrate-native origin
> of intrinsic spin**."

**Path B uses 9 DOFs per unit cell**: 6 macro-strain + **3 translational
internal**. The **3 microrotational internal DOFs (φ_x, φ_y, φ_z) are
MISSING**.

The Keating bond-bending k_θ in Path B captures the EFFECT of Cosserat
couple-stress on bond-axis-deviation, but does NOT include the explicit
microrotational field φ. This is per Session 16's framing: Sessions 12-15
are a "DISCRETIZATION" of continuous Cosserat, not a faithful
discrete-Cosserat representation.

**A full-Cosserat K4 scaffold would have 12 DOFs per unit cell** (6 strain
+ 6 internal: 3 translation + 3 microrotation), giving 12 eigenvalues with
a different spectrum.

### §6.7.2 Axiom 1 — I4₁32 right-handed chirality — **VIOLATED**

Axiom 1 specifies right-handed chiral $I4_1 32$ space group. Path B's
K4_BOND_DIRECTIONS are signed but the energy form is achiral (no L/R
asymmetry). Adding chirality would require chiral coupling terms
(e.g., Cosserat $\alpha$ modulus mixing translation × rotation with
parity-breaking sign).

### §6.7.3 Axiom 1 — LC oscillator structure — **NOT REPRESENTED**

Axiom 1 specifies "every node is intrinsically an LC oscillator" with
translation ↔ E (capacitive) and rotation ↔ B (inductive) coupling. Path
B treats nodes as purely mechanical (no L-C separation, no EM coupling).

### §6.7.4 Axiom 3 — Maxwell Lagrangian — **NOT REPRESENTED**

Axiom 3 specifies $\mathcal{L}_{node} = \frac{1}{2}\epsilon_0|\partial_t \mathbf{A}_n|^2 - \frac{1}{2\mu_0}|\nabla \times \mathbf{A}_n|^2$.
Path B uses Keating mechanical energy, not this Maxwell form. Equivalent
in linear limit per Axiom 1's LC duality, but the explicit EM coupling is absent.

### §6.7.5 Axiom 4 — K=2G SYM operating point — **HONORED ✓**

Per Axiom 4 (`eq_axiom_4.tex:23`):
> "Symmetry classification: SYM (ε and μ saturate together, vacuum K = 2G)"

Path B's K=2G operating point IS the SYM operating point. ✓

### §6.7.6 Axiom 4 — Saturation kernel S(A) = √(1-A²) — **NOT EXCITED**

Path B operates in linear regime (small-amplitude eigenmodes). S(A) ≈ 1.
This is appropriate for eigenmode analysis but doesn't test the nonlinear
saturation physics.

### §6.7.7 What this means for the 4/21 ≈ 0.187 result

The eigenvalue λ_G = 4/21 ≈ 0.1905 is the soft shear eigenvalue of a
**CAUCHY-Keating K4 lattice**, NOT a full-Cosserat K4 lattice. Three
possibilities:

- **(α) The 4/21 ≈ 0.187 proximity is the Cauchy PROJECTION of a deeper
      Cosserat result**: adding the 3 microrotational DOFs would
      renormalize 4/21 → something closer to 0.187 (or p* = 0.1834).
      Plausible since the missing physics adds 3 new modes that could
      couple with the existing soft shear.

- **(β) The 4/21 ≈ 0.187 proximity is coincidence at the Cauchy level**:
      the full Cosserat soft shear is structurally different. The Cauchy
      proximity is fortuitous.

- **(γ) The microrotational DOFs decouple from the soft shear mode at
      the K=2G operating point**: E-irrep deviatoric shear (modes 0,1
      in Path B) had ZERO axial coupling and ZERO internal coupling.
      Maybe the same E-irrep structure has ZERO microrotational
      coupling. If so, 4/21 IS the correct Cosserat result for this
      mode, and the 0.187 gap is a real discrepancy needing resolution.

**Cannot distinguish (α), (β), (γ) without extending the scaffold to 12 DOFs.**

### §6.7.8 Required next step for full Axiom-1 compliance

A "Path B+" should:
1. Add 3 microrotational DOFs (φ_x, φ_y, φ_z) to the internal DOF set
   (total 12 DOFs per unit cell)
2. Add explicit Cosserat couple-stress moduli α, β, γ per Session 17
   dimensional framework
3. Add chiral coupling terms (right-handed I4₁32 sign convention)
4. Solve the 12-DOF eigenvalue problem
5. Compare the soft shear eigenvalue to 4/21 (current Cauchy result) and
   to 0.187 / p* = 8πα targets
6. Identify which modes carry rotational vs translational character

This is **~1-2 additional sessions**, building on Path B's analytical
machinery. NOT done as part of this verification.

---

## §7 Honest verdict

**STRUCTURAL PASS at the construction level**:
- ✓ K=2G operating point self-engineers to k_θ/k_a = 1/7, ν = 2/7
- ✓ Eigenvalue spectrum is clean (4/21, 4/3, simple rationals)
- ✓ Mode degeneracies (1+2+3+3) match K4 cubic symmetry decomposition
- ✓ Frequency ratio ω_K/ω_G = √7 reflects K=2G constraint dimension 7

**NUMERICAL PROXIMITY for soft shear eigenvalue**:
- ⚠ λ_G = 4/21 ≈ 0.1905 vs target 0.187 — 2% match
- ⚠ Same vs p* = 8πα = 0.1834 — 4% match
- ⚠ But eigenvalue ≠ amplitude — identification not literal

**FAILS at the literal-amplitude interpretation**:
- ✗ No eigenvector projection produces 0.187 in any obvious normalization
- ✗ The amplitude ratios are int/G = 0.76, int/total = 0.43 — not near 0.187

**SIX ambiguities unresolved** per §6.

**My recommended next move**: hold the verification at "PARTIAL PASS"
with six explicit ambiguities flagged. Don't claim closure of Sessions
19+. Grant should adjudicate which of the six readings (if any) is the
intended one before further session work.

If Grant's intended framing is Ambiguity 6.1 option (i) (soft shear) +
Ambiguity 6.2 option (a) (numerical equality up to discretization) +
Ambiguity 6.3 option (c) (χ_K=12 ≠ K=2G bond ratio), then the verification
is **NUMERICAL PROXIMITY PASS with 2% accuracy** — this is the most
generous reading.

If Grant intends Ambiguity 6.6 (mode 2,3,4 as the dressed mode), then
verification **FAILS** (0.486 ≠ 0.187 by 160%).

---

## §8 What this means for doc 123 trampoline-analogy improvement queue

Per doc 124 §4: the queue was conditioned on Q-G47 19+ verification PASSes
with structural OR numerical closure.

This doc gives:
- STRUCTURAL PASS at construction level → execute queue content
- NUMERICAL PROXIMITY 2% → conditional on reading interpretation
- FAILS at literal amplitude → DON'T claim quantitative precision

**Recommendation**: execute doc 123 queue with the structural-PASS framing
in Step 6.5, noting that numerical-precision verification at the eigenmode
level requires resolving the six ambiguities in §6.

The queue's primer content (fabric weave density, p* = 8πα, "α IS the
fabric density") is INDEPENDENT of the eigenvalue match — it stands on
the geometric Theorem 3.1 derivation, not on Q-G47 19+ closure. So it
lands cleanly with or without §2.2 numerical proximity.

---

## §9 Files added/modified

**Added**:
- `src/scripts/verify/q_g47_path_b_k4_eigenmode.py` (executable verification)
- `src/scripts/verify/q_g47_path_b_k4_eigenmode_results.json` (cached results)
- `research/L3_electron_soliton/127_q_g47_path_b_eigenmode_results.md` (this doc)

**Not modified** (held pending Grant adjudication):
- `manuscript/ave-kb/common/trampoline-analogy-primer.md` Q-G47 section
- AVE-QED Sessions 12-17 docs
- Doc 124 (verification attempt) — superseded by this doc for the
  eigenmode question

---

## §10 Cross-references

- [doc 122 — Q-G47 19+ scope adjudication](122_q_g47_sessions_19_plus_scope_adjudication.md) — (a)+(b) framework
- [doc 123 — trampoline-analogy queue](123_trampoline_analogy_improvement_queue.md) — conditional on this verification
- [doc 124 — verification attempt](124_q_g47_19_verification_attempt.md) — STRUCTURAL PASS, numerical pending
- [doc 125 — eigenvalue plan](125_k4_standing_wave_eigenvalue_plan.md) — Path A/B/C options
- [doc 126 — first-pass scope discovery](126_q_g47_19_standing_wave_eigenmode_first_pass.md) — Path B recommended
- AVE-QED Sessions 12-17 — discrete K4 scaffold history
- AVE-QED Session 17 — continuous Cosserat axiom-level dimensional framework
- A-029 (Vol 3 Ch 1:33-37) — magic angle u_0* = 0.187, r_sec/d = 1.187
- A-032 — χ_K = 12 path-count multiplicity
- Trampoline primer §2.5 — p* = 8πα fabric weave density (Theorem 3.1)
