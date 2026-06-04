[↑ Research](index.md)

# Phasor↔real-space area bijection — Class-B→Class-2 lift candidate (RESULT)

**Status**: RESULT — analytical derivation complete. **VERDICT: Class B confirmed.** The last α-¼ lift-path closes.
**Prereg**: [`2026-06-04_alpha-class2-bijection-prereg.md`](2026-06-04_alpha-class2-bijection-prereg.md) (FROZEN @ `063c548b`).
**Branch**: `analysis/2026-06-04-alpha-class2-bijection` (off `main`); worktree-isolated.
**Question (Q-EMBED-SEL-1 §7.3)**: can the named identification *phasor-enclosed-area = Nyquist-cell-area* (which holds α⁻¹ = 4π³+π²+π at **Class B**) be **derived** from K4 + Cosserat primitives, lifting it to **Class 2**? Or is it an irreducible normalization / α-substitution?

**One-line verdict**: the bridge K is **α-free on input** (B1 PASS), but closing the bijection to the golden-torus value R·r = ¼ **requires substituting the empirical value of α** — the honestly-built bridge forces R·r → 4π²α ≈ 0.288 in V_yield-canonical units, **not** ¼ = 0.25. **B3 FAILS → Class B.**

**Skills fired**: `ave-prereg` (read FROZEN prereg in full + corpus-grep §0 anchors); `ave-canonical-leaf-pull` (energy-quantum + cross-scale-bridge class: ch8, Q-EMBED-SEL-1 §2.3, kinetic-yield-threshold, z0-derivation, natural-units-cheatsheet, translation-circuit:173); `phase-space-coordinate-check` (the K-bridge IS the phasor↔real-space coordinate seam — kept the bijection as the thing-under-test, never silently equated the two coordinate areas); `consistency-vs-emergence` v1.3 (NEW-primitive test: no new K4+Cosserat primitive derived; the closure to ¼ rests on substituting α); `substrate-native-check` (K4 bond LC tank L_cell=μ₀ℓ, C_cell=ε₀ℓ + ξ_topo; no Lagrangian/gradient-descent leak); `ave-ee-first-mapping` (C_bond∘ξ_topo voltage→charge→length built EE-native); `ave-canonical-source` (all constants from `constants.py`; sanity-script imports, no hardcoded α/137 literal); `ave-driver-script-honesty` (R,r kept SYMBOLIC to the end; α NEVER imported into K; no fit-to-¼); `ave-discrimination-check` (SM-counterfactual in §VERDICT); `verify-before-cite` (every load-bearing citation grep-verified at the cited line — see §AUDITOR QUEUE provenance table).

---

## §RESULT — the K-derivation + the circularity audit

### R.0 — What is under test (phase-space-coordinate-check, fired first)

The named identification (Q-EMBED-SEL-1 §2.3(ii) **verbatim**, `2026-05-31_Q-EMBED-SEL-1_step_c_result.md:69`) equates:

- a **phasor reactive energy** — the closed loop integral ∮V dI around the bond's (V_inc, V_ref) ellipse, semi-axes (R, r) — living in **phase-space (voltage coordinates)**, per `translation-circuit.md:173`: *"the bond's incident/reflected voltage waves … E ~ (V_inc+V_ref), B ~ (V_inc−V_ref)/Z"*; with
- a **real-space cross-section area** — the Nyquist cell π(d/2)², d = ℓ_node — living in **real-space (length² coordinates)**.

The bridge between [voltage²] and [length²] is a dimensionful constant **K**. Per `phase-space-coordinate-check`, **this bridge IS the coordinate seam, and the equation πR·r = A_cell is the thing under test — not an assumption.** The §2.3 closure works in lattice-natural units (Z₀=1, ℓ_node=1, V_snap→1/√α) and *sets the overall constant to unity*; the entire Class-B↔Class-2 question is the status of K.

Per the Q3 mandate (Grant 2026-06-04): R, r are **voltage-phasor semi-axes (in volts)**; the "R = 0.809 ℓ_node" quotes are POST-BRIDGE. The derivation **starts from the V-phasor and derives the ℓ_node expression** via the explicit Z₀ ∘ C_bond ∘ ξ_topo chain. Starting from ℓ_node-unit R,r is disallowed (begs the question). **R, r are held symbolic to the end.**

### R.1 — α-free canonical primitives (Step 0 input set)

All from `src/ave/core/constants.py` (line refs); each verified α-free in SI:

| Primitive | constants.py | SI definition | α-free? |
|---|---|---|---|
| ℓ_node | `L_NODE` :234 | ℏ/(m_e c) | ✅ (four-base) |
| V_snap | `V_SNAP` :373 | m_e c²/e | ✅ |
| Z₀ | `Z_0` (μ₀c) | √(μ₀/ε₀) | ✅ |
| ξ_topo | `XI_TOPO` :246 | e/ℓ_node | ✅ |
| L_cell | `z0-derivation.md:19` | μ₀ ℓ_node | ✅ |
| C_cell | `z0-derivation.md:19` | ε₀ ℓ_node | ✅ |
| ω_C | `theorem-3-1-q-factor.md:27` | c/ℓ_node | ✅ |

The **four-base convention** (`natural-units-cheatsheet.md:21`): {ℓ_node, c, ℏ, m_e} are set to 1; *charge e is NOT among the four bases.* This is the structural pivot of the whole audit (R.4 below).

### R.2 — Build the bridge from the explicit chain (Step 1)

The candidate bridge is **C_bond (V→Q) ∘ ξ_topo (Q→L)** (per the prereg's TKI clarification: TKI alone is [Q]≡[L]; it does NOT by itself bridge voltage↔length — the full chain does). EE-native (`ave-ee-first-mapping`):

```
V  --(C_cell)-->  Q = C_cell · V     [Coulombs]      (capacitor charge)
Q  --(/ξ_topo)->  L = Q / ξ_topo      [meters]        (ξ_topo = e/ℓ_node = Q/L)
```

so a **voltage maps to a length** with factor
$$\frac{L}{V} = \frac{C_\text{cell}}{\xi_\text{topo}} = \frac{\varepsilon_0\,\ell_\text{node}}{e/\ell_\text{node}} = \frac{\varepsilon_0\,\ell_\text{node}^2}{e} = \frac{\varepsilon_0\,\hbar^2}{c^2 e\, m_e^2}\quad\left[\frac{\text{m}}{\text{V}}\right].$$

The V-phasor ellipse area π·R·r (semi-axes in volts) maps to a **real area**
$$A_\text{phasor→real} = \pi\,R\,r\left(\frac{C_\text{cell}}{\xi_\text{topo}}\right)^2 = \pi\,R\,r\cdot K,\qquad K \equiv \left(\frac{C_\text{cell}}{\xi_\text{topo}}\right)^2 = \left(\frac{\varepsilon_0\,\hbar^2}{c^2 e\, m_e^2}\right)^2\ \left[\frac{\text{m}^2}{\text{V}^2}\right].$$

**K is built entirely from {ε₀, ℏ, c, e, m_e}.** Numerically (sanity-script, α never imported): K = (8.2408×10⁻¹⁸ m/V)² = 6.791×10⁻³⁵ m²/V².

### R.3 — The bijection (Step 3) — keep R,r symbolic

The Nyquist cell real area is A_cell = π(ℓ_node/2)² = π ℏ²/(4 c² m_e²). Imposing the bijection **πR·r·K = A_cell** and solving for the *required* R·r (still in volts²):

$$\boxed{\;R\cdot r\big|_\text{required} = \frac{A_\text{cell}}{\pi K} = \frac{c^2 e^2 m_e^2}{4\,\varepsilon_0^2\,\hbar^2}\;}\quad[\text{V}^2]\qquad(= 5.4895\times10^{8}\ \text{V}^2).$$

This is a **definite α-free SI quantity** — good so far. The question is whether it **equals the corpus's R·r = ¼** when expressed in the natural amplitude units.

### R.4 — The circularity audit (Step 0, the dispositive step)

**B1 — input-side α check (airtight enumeration).** The free symbols of K and of R·r|_required are *exactly* {c, e, ε₀, ℏ, m_e} — every one a four-base / Maxwell primitive; **α appears in NEITHER.** I did not feed α in. The √α that pervades lattice-natural units is an **output** of how the charge e scales against the four-base {ℓ_node, c, ℏ, m_e}: because e is not one of the four bases, `e_native = √α` and `V_snap_native = 1/√α` (`natural-units-cheatsheet.md:59`). **B1 PASS-direction: the bridge K is α-free on input.**

**The closure to ¼, however, is where α enters.** Express the required R·r against the two candidate amplitude scales:

| normalization | R·r\|_required equals | substitute α = e²/4πε₀ℏc |
|---|---|---|
| V_snap units (R·r / V_snap²) | e⁴/(4c²ε₀²ℏ²) | **4π²α²** ≈ 0.002102 |
| V_yield-canonical units (R·r / V_yield²), V_yield=√α·V_snap | πe²/(cε₀ℏ) | **4π²α** ≈ 0.2881 |

In the lattice-natural V_yield units the corpus uses, **R·r\|_required = 4π²α ≈ 0.2881, NOT ¼ = 0.25.** The golden-torus value is **missed by ~13%** (factor 0.868). The honestly-built α-free bridge does **not** reproduce R·r = ¼.

**The cell-filling condition, run directly.** "Photon phasor fills exactly one Nyquist cell" ⇒ map V_yield through the bridge to a length and require it = the cell tube radius ℓ_node/2:
$$\frac{C_\text{cell}}{\xi_\text{topo}}\,V_\text{yield} = \frac{\ell_\text{node}}{2}\ \Rightarrow\ \frac{V_\text{yield}}{V_\text{snap}} = \frac{e^2}{2c\varepsilon_0\hbar} = \boxed{2\pi\alpha}.$$
But the canonical kinetic-yield value (`kinetic-yield-threshold.md:21`) is V_yield/V_snap = **√α**. The bridge-forced 2πα and the canonical √α agree only at α = 1/(4π²) ≈ 0.0253 — **not CODATA α (0.007297)**. Equivalently, demanding R·r = ¼ in V_yield units forces 4π²α = ¼ ⇒ α = 1/(16π²) ≈ 0.006333 — again **not CODATA α**.

**Conclusion of the audit.** The corpus's clean R·r = ¼ and V_yield = √α·V_snap are **not outputs** of the cell-filling bridge. They are recovered **only** by (a) substituting the empirical value of α into the normalization, OR (b) invoking the natural-unit choice that "sets the overall constant K to unity" — i.e. *defining* the V-axis scale to be V_yield and *declaring* one unit of phasor area = one cell. Both are the **free-normalization / α-substitution escape** the prereg pre-registered as the Class-B fallback. The √α in V_yield traces to `kinetic-yield-threshold.md:16` — which the prereg itself flags as **substituting** α (*"by substituting the fundamental definition of the fine-structure constant (α = e²/4πε₀ℏc)"* — verbatim) — not deriving it geometrically.

### R.5 — Why the bridge cannot derive ¼ (the explanatory mechanism)

A single mechanism explains every numerical near-miss above (4π²α ≠ ¼; 2πα ≠ √α; the implied α-values 1/16π², 1/4π² ≠ CODATA): **the bijection is one scalar equation in one dimensionless unknown (the amplitude-to-length normalization), and α is precisely that normalization.** The four-base unit system has *already spent* its freedom pinning {ℓ_node, c, ℏ, m_e}; the charge-scale (hence the voltage-scale at which "one cell is filled") is the *one remaining* dimensionless ratio, and that ratio **is** α (by α = e²/4πε₀ℏc). There is no second, independent geometric condition in the kinematic unit-bridge to over-determine α — the (2,3)-winding / ropelength / golden-ratio content that fixes R−r = ½ and the *ratio* R/r lives in the **selection** layer (dressed-eigenmode dynamics), which is explicitly out of scope here (prereg §4 "no re-litigation of selection"). The kinematic bridge alone has exactly enough freedom to *absorb* α and exactly zero freedom to *predict* it. This is the same structural fact the four prior dynamic engine tests found (S₁₁-landscape flatness; `audit/2026-06-02_alpha-lift-*`) and the 2026-06-04 adversarial re-challenge confirmed — now established **kinematically/analytically**, complementing the dynamical negative.

### R.6 — New-primitive test (consistency-vs-emergence v1.3)

Does the work derive a **new K4+Cosserat primitive**? **No.** The chain reuses only canonical primitives (L_cell, C_cell, ξ_topo, Z₀, ω_C). The one step that would have to be *derived* for a Class-2 lift — that one quantum of bond reactive energy fills exactly one Nyquist cell **at the amplitude the substrate independently fixes** — is exactly the step that, run honestly, lands on 4π²α ≠ ¼ and therefore must **import** α to close. No new primitive is produced; the work **formalizes (and now falsifies the α-freedom of) an existing identification.** Per v1.3, classification cannot be promoted past the canonical source's Class-B ceiling without a named new substrate-primitive, and none exists.


## §VERDICT — placeholder (filled incrementally)

## §AUDITOR QUEUE — placeholder (filled incrementally)
