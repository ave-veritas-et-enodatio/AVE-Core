[↑ Research](index.md)

# Phasor↔real-space area bijection — Class-B→Class-2 lift candidate (RESULT)

**Status**: RESULT — analytical derivation complete. **VERDICT: Class B confirmed.** The last α-¼ lift-path closes.
**Prereg**: [`2026-06-04_alpha-class2-bijection-prereg.md`](2026-06-04_alpha-class2-bijection-prereg.md) (FROZEN @ `947b2c49`, incl. §8 completeness addendum).
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

In the lattice-natural V_yield units the corpus uses, **R·r\|_required = 4π²α ≈ 0.2881, NOT ¼ = 0.25.** The bridge value **overshoots** ¼ by a factor 0.2881/0.25 = **1.152** (≈15% high; equivalently ¼ is 0.868× the bridge value — the sanity script reports the 1.152 form). The honestly-built α-free bridge does **not** reproduce R·r = ¼.

**The cell-filling condition, run directly.** "Photon phasor fills exactly one Nyquist cell" ⇒ map V_yield through the bridge to a length and require it = the cell tube radius ℓ_node/2:
$$\frac{C_\text{cell}}{\xi_\text{topo}}\,V_\text{yield} = \frac{\ell_\text{node}}{2}\ \Rightarrow\ \frac{V_\text{yield}}{V_\text{snap}} = \frac{e^2}{2c\varepsilon_0\hbar} = \boxed{2\pi\alpha}.$$
But the canonical kinetic-yield value (`kinetic-yield-threshold.md:21`) is V_yield/V_snap = **√α**. The bridge-forced 2πα and the canonical √α agree only at α = 1/(4π²) ≈ 0.0253 — **not CODATA α (0.007297)**. Equivalently, demanding R·r = ¼ in V_yield units forces 4π²α = ¼ ⇒ α = 1/(16π²) ≈ 0.006333 — again **not CODATA α**.

**Conclusion of the audit.** The corpus's clean R·r = ¼ and V_yield = √α·V_snap are **not outputs** of the cell-filling bridge. They are recovered **only** by (a) substituting the empirical value of α into the normalization, OR (b) invoking the natural-unit choice that "sets the overall constant K to unity" — i.e. *defining* the V-axis scale to be V_yield and *declaring* one unit of phasor area = one cell. Both are the **free-normalization / α-substitution escape** the prereg pre-registered as the Class-B fallback. The √α in V_yield traces to `kinetic-yield-threshold.md:16` — which the prereg itself flags as **substituting** α (*"by substituting the fundamental definition of the fine-structure constant (α = e²/4πε₀ℏc)"* — verbatim) — not deriving it geometrically.

### R.5 — Why the bridge cannot derive ¼ (the explanatory mechanism)

A single mechanism explains every numerical near-miss above (4π²α ≠ ¼; 2πα ≠ √α; the implied α-values 1/16π², 1/4π² ≠ CODATA): **the bijection is one scalar equation in one dimensionless unknown (the amplitude-to-length normalization), and α is precisely that normalization.** The four-base unit system has *already spent* its freedom pinning {ℓ_node, c, ℏ, m_e}; the charge-scale (hence the voltage-scale at which "one cell is filled") is the *one remaining* dimensionless ratio, and that ratio **is** α (by α = e²/4πε₀ℏc). There is no second, independent geometric condition in the kinematic unit-bridge to over-determine α — the (2,3)-winding / ropelength / golden-ratio content that fixes R−r = ½ and the *ratio* R/r lives in the **selection** layer (dressed-eigenmode dynamics), which is explicitly out of scope here (prereg §4 "no re-litigation of selection"). The kinematic bridge alone has exactly enough freedom to *absorb* α and exactly zero freedom to *predict* it. This is the same structural fact the four prior dynamic engine tests found (S₁₁-landscape flatness; `audit/2026-06-02_alpha-lift-*`) and the 2026-06-04 adversarial re-challenge confirmed — now established **kinematically/analytically**, complementing the dynamical negative.

### R.6 — New-primitive test (consistency-vs-emergence v1.3)

Does the work derive a **new K4+Cosserat primitive**? **No.** The chain reuses only canonical primitives (L_cell, C_cell, ξ_topo, Z₀, ω_C). The one step that would have to be *derived* for a Class-2 lift — that one quantum of bond reactive energy fills exactly one Nyquist cell **at the amplitude the substrate independently fixes** — is exactly the step that, run honestly, lands on 4π²α ≠ ¼ and therefore must **import** α to close. No new primitive is produced; the work **formalizes (and now falsifies the α-freedom of) an existing identification.** Per v1.3, classification cannot be promoted past the canonical source's Class-B ceiling without a named new substrate-primitive, and none exists.


## §VERDICT — Class B confirmed (the last α-¼ lift-path closes)

### V.1 — PASS-criteria adjudication (prereg §3, evaluated)

| Bar | Condition | Result | Evidence |
|---|---|---|---|
| **B1 — non-circular** | K is α-free on input | ✅ **PASS** | K = (C_cell/ξ_topo)² has free symbols {c, e, ε₀, ℏ, m_e}; no α (R.4, AST-verified in sanity script) |
| **B2 — forced** | K's value fixed by canonical constants, no free *dimensionful* slack | ✅ (bridge is forced) | K = 6.791×10⁻³⁵ m²/V², a definite combination of canonical constants |
| **B3 — bijection emergent** | πR·r = A_cell follows WITHOUT imposing K=1 or R·r=¼ | ❌ **FAIL** | bridge forces R·r → **4π²α** ≈ 0.288 in V_yield units, **not** ¼; closing to ¼ requires α = 1/16π² (≠ CODATA). Cell-filling forces V_yield/V_snap = **2πα** ≠ canonical √α (R.4) |
| **B-fallback** | K is a free normalization OR the closure substitutes α | ✅ **TRIGGERED** | the closure to ¼ / √α is recovered only by substituting the empirical α, or by the natural-unit choice that sets the overall constant to unity |

Lift requires **B1 ∧ B2 ∧ B3**. **B3 fails. → Class B confirmed.**

### V.2 — The explicit derive-vs-substitute adjudication (the discriminator)

The prereg's discriminator: *does requiring the photon phasor to fill exactly one Nyquist cell **FORCE** √α to the golden-torus value (DERIVED, Class 2), or does it require **SUBSTITUTING** α / leave a free normalization (Class B)?*

**Answer: it SUBSTITUTES.** Two independent reads of the same scalar equation both show α entering at the closure, never at the input:

1. **R·r read** — the α-free bridge forces R·r\|_required = 4π²α·V_yield² . The corpus golden-torus value R·r = ¼·V_yield² is recovered **iff** 4π²α = ¼, which is a *statement about the numerical value of α* (and a false one: it gives α = 1/16π² ≈ 0.006333, missing CODATA 0.007297 by ~13%). The geometry does **not** force ¼; matching ¼ forces (a wrong) α.

2. **V_yield read** — "phasor fills one cell" forces V_yield/V_snap = 2πα via the α-free bridge, whereas the canonical kinetic-yield value is √α. These coincide only at α = 1/4π² ≈ 0.0253 (again ≠ CODATA). So the substrate's *own* saturation amplitude (√α·V_snap, `kinetic-yield-threshold.md:21`) and the *cell-filling* amplitude (2πα·V_snap) are **different physical scales** — the bijection is not an identity the substrate satisfies; it is a normalization one *imposes*.

The canonical √α in V_yield is itself imported by **substitution**, not derivation: `kinetic-yield-threshold.md:16` states *verbatim* it follows *"by substituting the fundamental definition of the fine-structure constant (α = e²/4πε₀ℏc)."* So even the amplitude scale the §2.3 closure leans on is an α-substitution, exactly as the prereg's HARD honesty line anticipated. **Q2's reframe (V_yield = geometric mean of string-tension × Coulomb-coupling) is correct and makes the lift *meaningful to attempt* — but the geometric-mean structure does not, on the kinematic unit-bridge, *output* √α; it *consumes* the Coulomb coupling e²/4πε₀ = αℏc, which is α substituted in.**

### V.3 — The single explanatory mechanism (Rule 11 honest closure)

Every near-miss (4π²α ≠ ¼; 2πα ≠ √α; implied α ∈ {1/16π², 1/4π²} ≠ CODATA) has **one cause**: the four-base unit convention {ℓ_node, c, ℏ, m_e} has already spent all dimensional freedom; the *one* remaining dimensionless ratio — the charge/voltage scale at which "one cell is filled" — **is α** (definitionally, α = e²/4πε₀ℏc). A *kinematic* unit-bridge is a single scalar relation with a single free normalization, so it has exactly enough freedom to **absorb** α and **zero** freedom to **predict** it. Over-determining α needs a *second, independent* condition — and that condition lives in the **selection** layer (which dressed-eigenmode dynamics, R−r=½ self-avoidance, and the R/r golden ratio supply), explicitly **out of scope** here (prereg §4). This is the clean, decisive failure of a pre-registered prediction with a single mechanism explaining all failures — the discipline working at full strength (Rule 11). **Branch closed; no rescue attempted.**

This **kinematic/analytical** negative complements the **dynamical** negatives already on record (the four 2026-06-02 `audit/2026-06-02_alpha-lift-*` engine tests + S₁₁-landscape flatness + the 2026-06-04 adversarial re-challenge that held): the bijection cannot be lifted to Class 2 by *either* the dynamics (selection) *or* the kinematics (this unit-bridge).

### V.4 — SM-counterfactual (ave-discrimination-check)

This is a **negative** result, so the discrimination check runs in reverse — is there a *positive* AVE-distinct claim hiding here that I must avoid over-stating? **No.** What the audit establishes is the *absence* of an AVE-distinct derivation: the bridge is α-free but α-uninformative. In SM/QED, α is a measured input with no derivation; nothing here changes that. The honest framing is therefore symmetric with SM: AVE's α⁻¹ = 4π³+π²+π remains a **closed-form geometric identification whose scale (~1/137) is forced by the Compton-resonance trapping condition but whose exact value rests on ONE substrate-geometric identification per route that the substrate does not independently select** (the existing canonical Class-B framing at `ch8-alpha-golden-torus.md:11`). This result **does not** add an AVE-distinct empirical anchor and **must not** be promoted as one. It *strengthens* the Class-B caveat by closing one of the two named lift-routes analytically.

### V.5 — Classification (consistency-vs-emergence v1.3)

**Class B (axiom-manifestation with a named identification), unchanged — and now with the α-freedom of the phasor↔real-space bijection explicitly falsified.** No new K4+Cosserat primitive is derived (R.6). The phasor-area = Nyquist-cell-area step remains canonical INPUT, not Class-2 emergence; the kinematic bridge that might have derived it instead requires α to be substituted. Per v1.3, promotion past the canonical Class-B ceiling requires a named new substrate-primitive, and there is none.

## §AUDITOR QUEUE

Implementer-lane surfacing per Rule 15 + flag-don't-fix. The auditor lands the manuscript / KB / `COLLABORATION_NOTES` entries; I surface the findings + provenance below. **No KB/manuscript files were edited by this session** — result lives in `research/` + the sanity script only.

### AQ-1 (top item) — close the gate-(b) `R·r=1/4` phasor-radius question with this kinematic negative

`translation-circuit.md:173` flags *verbatim*: *"the R·r=1/4 phasor-radius question that lives in this sector is a separate, **gate-(b)-pending** claim."* **This result resolves that gate-(b) for the kinematic unit-bridge: it does NOT lift — the bijection requires substituting α (B3 FAIL).** Auditor action: when consolidating the pending I/Q-quadrature canonical leaf, record that the kinematic phasor↔real-space area bijection is **Class B (α-substituted), analytically closed 2026-06-04** — alongside the dynamical negatives. Recommend the gate-(b) marker be updated from "pending" to "resolved-negative (kinematic)" with this doc as anchor. **Do not** read this as resolving the *linear-quadrature decomposition* row itself (that is gate-(a), separate and not under test here).

### AQ-2 — the Class-B caveat at `ch8-alpha-golden-torus.md:11` can cite a second closed lift-route

The ch8 Class-B caveat (clm-0ktpcn, the `> Class B caveat (honest-α relabel)` block) currently lists the dynamical negatives (the four `audit/2026-06-02_alpha-lift-*` + S₁₁-flatness + the 2026-06-04 adversarial re-challenge) and states *"A Class 2 lift would require deriving the phasor↔real-space area bijection from K4 + Cosserat primitives — identified as a separate workstream candidate (see Phase 1 result §7.3)."* **That separate workstream (Q-EMBED-SEL-1 §7.3) is now executed and returns Class B (negative).** Auditor action (lands the edit): append to the caveat that the §7.3 kinematic-bijection lift-route has been **analytically attempted and closed Class B** (this doc), so **both** named lift-routes — dynamical *selection* and kinematic *unit-bridge* — are now closed. The caveat's honest framing strengthens; the chapter title/Class-B framing is unchanged.

### AQ-3 — `COLLABORATION_NOTES` / closure-roadmap: Q-EMBED-SEL-1 §7.3 status → CLOSED (Class B)

The §7.3 lift-candidate is the last open α-¼ lift-path. With this analytical negative + the prior dynamical negatives + the 2026-06-04 adversarial re-challenge that held, **the α-¼ lift programme is closed at Class B on all named routes.** Surface for the auditor's roadmap queue: mark Q-EMBED-SEL-1 §7.3 (phasor↔real-space bijection lift) CLOSED-NEGATIVE; no remaining open lift-route for α⁻¹ = 4π³+π²+π beyond first-principles z₀-from-K4 (a *different* route, still open, untouched here).

### AQ-4 — DO NOT promote as a positive anchor (ave-discrimination-check carry-forward)

This is a clean negative; it adds no AVE-distinct empirical anchor (V.4). Flag for the auditor: ensure no foreword / predictions-matrix promotion derives from this doc. The only corpus-state change is **caveat-strengthening** (a named lift-route closed), not a new positive claim.

### Provenance table (verify-before-cite — all grep-verified at cited line, 2026-06-04)

| Citation | Line content (verified) |
|---|---|
| `2026-05-31_Q-EMBED-SEL-1_step_c_result.md:69` | "(ii) **Phasor enclosed area = per-Compton-cycle reactive energy** … the enclosed area πRr in ℓ_node² units equals the bond's per-Compton-cycle reactive energy (up to the unit-system overall constant that the lattice-natural-units choice sets to unity)" |
| `kinetic-yield-threshold.md:16` | "By **substituting** the fundamental definition of the fine-structure constant (α = e²/4πε₀ℏc), the kinetic yield limit simplifies" |
| `kinetic-yield-threshold.md:21` | E_k = √(F_yield · e²/4πε₀) = √((m_e²c³/ℏ)(αℏc)) = **√α · m_e c²** |
| `z0-derivation.md:19` | L_cell = μ₀ ℓ_node,  C_cell = ε₀ ℓ_node |
| `natural-units-cheatsheet.md:59` | V_SNAP = m_e c²/e → native **1/√α**, SI 511,000 V |
| `translation-circuit.md:173` (common) | "E ~ (V_inc+V_ref), B ~ (V_inc−V_ref)/Z … the R·r=1/4 phasor-radius question … is a separate, **gate-(b)-pending** claim" |
| `ch8-alpha-golden-torus.md:11` | the Class-B caveat block (clm-0ktpcn) listing the closed lift-routes |
| `constants.py` `L_NODE` | `L_NODE = HBAR/(M_E*C_0)` (α-free) |
| `constants.py` `XI_TOPO` | `XI_TOPO = e_charge/L_NODE` (α-free) |
| `constants.py` `V_SNAP` | `V_SNAP = (M_E*C_0**2)/e_charge` (α-free) |
| `constants.py` `V_YIELD` | `V_YIELD = np.sqrt(ALPHA)*V_SNAP` (carries α — the suspect; per `kinetic-yield-threshold.md` an α-substitution) |

### Files this session produced (worktree-isolated, branch `analysis/2026-06-04-alpha-class2-bijection`)
- `research/2026-06-04_alpha-class2-bijection-result.md` (this doc)
- `src/scripts/vol_1_foundations/alpha_class2_bijection_circularity_audit.py` (sanity-check; `make verify` PASSES; DAG anti-cheat clean; α-free construction AST-verified)

