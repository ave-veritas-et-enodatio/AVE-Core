# DERIVATION — X37: the srs vertex equivalent circuit, EXTRACTED from bond geometry (TL discontinuity analysis)

**Date:** 2026-07-10 · **Branch:** `analysis/x37-junction-parasitics` · **Prereg (FROZEN):** [`2026-07-10_x37-junction-parasitics_prereg_FROZEN.md`](2026-07-10_x37-junction-parasitics_prereg_FROZEN.md) (commit `167f28ce`, pushed 2026-07-10T06:38:47Z — before this doc)

**SECTOR HEADER.** MODE = linear small-signal band structure. REGIME = cold, sub-yield, lossless (reactive-only). SECTOR = scalar / compression channel (Phase 1); vertex DOF = the breathing/dilatational compliance of the junction region (fully-symmetric 3-arm mode). Vector/torsion scoped out (prereg §8).

**CLASS.** MIXED: the g-factor VALUE is derived-geometric (§5 shows MU_0/EPSILON_0/ℓ_node cancel); the SCALE ω_C = c/ℓ_node is dimensional-forced/identity, used only as a reporting unit.

---

## 1. The memoryless baseline (what X37 must recover as f→0) — Rule-14 reuse of #604

The srs vacuum is a **distributed transmission-line network**: bonds are TLs (per-unit-length `L' = μ₀`, `C' = ε₀`; `Z_0 = √(L'/C')`, phase velocity `c = 1/√(L'C')`), and the memoryless vertex enforces common node voltage + KCL (no stored junction energy). The validated #604 survey ([`2026-07-09_srs-band-survey_result.md`](2026-07-09_srs-band-survey_result.md)) gives the scalar dispersion as the coined-walk / TL arccos map:

```
ω(k) = ω_link · θ(k),   θ(k) = arccos( μ(k)/3 ),   ω_link = √3 · ω_C
```

where `μ(k)` is an eigenvalue of the 4×4 srs Bloch adjacency `A(k)` (`μ ∈ [−3, 3]`), and `θ ≡ β_link·ℓ` is the **bond electrical length**. Band top at the π-mode `μ = −3`: `θ = arccos(−1) = π` ⇒

```
ω_top(memoryless) = π · √3 · ω_C = 5.441398 ω_C   (at H)      ← the G-B reference, from #604
```

**KCL derivation of the map (the hook X37 modifies).** For a lossless bond of electrical length θ, the symmetric two-port ABCD is `[[cosθ, jZ_0 sinθ],[jY_0 sinθ, cosθ]]`; its two-node indefinite admittance is `Y_bond = (1/(jZ_0 sinθ))·[[cosθ, −1],[−1, cosθ]]`. Memoryless KCL at a z=3 node, Bloch-reduced (`Σ_nbr V_n = μ V_node`):

```
3 cosθ − μ = 0   ⇒   cosθ = μ/3   ⇒   θ = arccos(μ/3).      (memoryless)
```

X37's entire job is to add the junction reactance to this KCL and re-solve.

---

## 2. The vertex as a TL discontinuity — the C3v symmetric/antisymmetric decomposition

Three identical semi-infinite lines meet at 120° in the vertex plane (C3v symmetry). A symmetric lossless reciprocal 3-port junction has a scattering matrix fixed by symmetry up to **two** eigen-reflections:

- **Symmetric (breathing) eigenmode** `(1,1,1)/√3` — all three arms in phase. Memoryless value **Γ_S = +1**: pushing equal in-phase waves in from all three ports, KCL `Σ I = 0` has nowhere for the net current to go ⇒ total reflection, the node voltage swings ⇒ the breathing mode sees an **OPEN**.
- **Antisymmetric (differential) eigenmodes** `(1,−1,0)`, `(1,1,−2)` — memoryless value **Γ_A = −1**: the differential mode sees a **SHORT** (the node is a virtual ground for it).

(Check: the memoryless star S-matrix `S_ij = 2/3 − δ_ij` has row-sum 1 ⇒ symmetric eigenvalue +1; `S_ii − S_ij = −1` ⇒ differential eigenvalue −1. ✓)

**Which mode does the scalar band TOP couple to?** The band top is the π-mode (`μ = −3`), fully staggered: every node is out of phase with ALL its neighbors, so at any node the three arms are equivalent (all neighbors at `−V_node`). The local excitation is therefore the **symmetric / breathing** combination ⇒ **the compression band ceiling couples to the symmetric-mode reflection Γ_S** — the OPEN, dressed by the junction's stored energy. This is the circuit statement of the walk's "compression engages the shunt compliance."

---

## 3. Extracting the junction equivalent circuit (the finite-extent parasitic)

The finite merge region (extent `d`) stores excess energy relative to the ideal point-junction, in two channels:

- **Shunt compliance C_j (the accumulator).** The extra volume of compressible medium at the node stores electric/compression energy `½ C_j V_node²` when the node voltage swings. Modeled as a length-`d` piece of the medium's shunt capacitance:
  ```
  C_j = s_C · ε₀ · d        (shunt, node → compression-background)
  ```
- **Series inertance L_j (the throat).** As arm currents crowd/redistribute entering the node, the junction region stores excess magnetic/kinetic energy. Modeled as a length-`d` series inductance split between the two ends of each arm (X/2 per end, preserving node symmetry):
  ```
  L_j = s_L · μ₀ · d        (series, in each arm)
  ```

`s_L, s_C = O(1)` **geometric shape factors** set by the 120° convergence + srs twist. **Honest flag (surfaced, not silently fixed):** the precise values of `s_L, s_C` require the transverse field profile of the junction, which requires a **bond transverse scale that canon does not provide** (prereg §2). The natural leading normalization — *the junction stores the same excess energy as a length-`d` piece of ordinary line* — is `s_L = s_C = 1`; this is a **modeling choice**, and both `s` and the extent `d` are swept (§6). Neither the memoryless recovery (G-B) nor the topology class (§4) depends on the exact `s`; the MAGNITUDE of the ceiling shift does — that is precisely the G-C closability finding.

---

## 4. The loaded dispersion + the topology class

Dress each bond with the series `X/2` at both ends and put the shunt `jB = jωC_j` at the node. The dressed symmetric two-port has (first order in the small products, exact form in the driver):

```
A_dress = cosθ − (x/2) sinθ,    B_dress = jZ_0 (sinθ + x cosθ),   x ≡ X·Y_0 = s_L f θ,   p ≡ B·Z_0 = s_C f θ
```

Bloch-reduced loaded KCL at the z=3 node ( `3·A_dress + jB·B_dress = μ` ):

```
μ = 3 cosθ − f θ ( (3/2) s_L + s_C ) sinθ + O(f²).                (LOADED)
```

**Extent → electrical length.** The junction is a fraction `f = d/ℓ` of the bond, so its electrical length is `f·θ`; that is why the loading terms are `s·f·θ` — the reactance grows with both extent and frequency (a capacitor/inductor, not a resonant trap in the through-path). The junction's own LC self-resonance is

```
ω_vertex = 1/√(L_j C_j) = c / (√(s_L s_C) · f · ℓ) = ω_C / (√(s_L s_C) · f).
```

**Band top (`μ = −3`), connected-band ceiling.** Note `sin(π) = 0`, so `μ(θ=π) = −3` for ALL `f` — the isolated H-point survives. But the **connected** manifold (continuously reachable from the acoustic point `θ=0, μ=3`) tops out at the FIRST `θ` where the descending `μ(θ)` reaches the adjacency floor `−3`; the parasitic drives `μ(θ)` *below* `−3` (unphysical) just under `π`, **opening a zone-edge stop-band** and dropping the connected ceiling. Solving `μ(θ)=−3` for the first crossing:

```
θ_top = π ( 1 − κ f ) + O(f²),   κ = s_L + (2/3) s_C            ⇒   g_scalar(f) = √3 · θ_top = π√3 ( 1 − κ f ) + O(f²).
```

**TOPOLOGY CLASS (the deliverable).** Both the shunt accumulator (`s_C`) and the series throat (`s_L`) **LOWER** the ceiling — any added reactance stores energy, slows the network, and pins the cutoff DOWN — by **opening a zone-edge gap**. The vertex is a **REACTIVE LOW-PASS** load, NOT a resonant series-trap in the through-path and NOT a parallel-bypass (it does **not** lift) and NOT a clean partitioned-η. This **confirms** the walk's accumulator lean (compression engages the shunt compliance) and **adds** the series throat; it **refutes** any "junction lifts the ceiling" expectation. Whether the junction resonance sits above the memoryless top (`ω_vertex > π√3 ω_C`, memoryless nearly intact) or below it (junction caps the band) is set by the crossover `f_crit = 1/(π√3·√(s_L s_C)) ≈ 0.184` (for `s=1`).

### 4a. Driver-time refinement (Rule 10) — the combined ceiling is NON-ADDITIVE

Running the exact connected-band solver (not the linearization) surfaced a subtlety the O(f) analysis hides. The linear coefficient `κ = s_L + (2/3) s_C` is the correct slope of the LOCAL `μ(θ)` and **matches the exact solve to <0.1% for a SINGLE active channel** (pure shunt-C `s_L=0`, or pure series-L `s_C=0`; verified `test_single_channel_anchor_matches_exact`). But when **both** channels are on, the connected-band ceiling is **NOT** lowered by the sum of the two drops: it tracks the **stronger** channel (here the throat, `−dg/df ≈ π√3` for `s_L=1`, vs `≈ (2/3)π√3` for `s_C=1`). Mechanism: once `s_C > 0` the loaded `μ(θ)` goes **non-monotonic near the zone edge** — it dips below the adjacency floor `−3` at the throat-set first crossing, then **recovers** above `−3` (a thin re-entrant sliver up to the isolated `θ=π` point, where `μ(π) = −3 + s_L s_C f²π² > −3`). The connected-band ceiling is the **first** `μ=−3` crossing (throat-dominated); the accumulator's extra loading is **absorbed into the re-entrant gap ABOVE that crossing**, not into a further lowering of the connected top. So the additive anchor `π√3(1 − (s_L+2/3 s_C)f)` **over-predicts** the combined drop; the exact combined curve overlays the pure-throat curve (result figure Panel A). This does not change the headline (both channels lower the ceiling; swing ≈ 31% over `f∈[0,0.5]` at `s=1` ⇒ extent-dominated ⇒ branch iii). It sharpens the topology statement: **the vertex opens a re-entrant zone-edge gap; the CONNECTED ceiling is set by the stronger reactive channel, and the FULL spectrum acquires a thin re-entrant sliver up to the isolated H-point.**

---

## 5. Anti-install proof — the extraction is dimensionless in ℓ_node units (G-A)

Every junction quantity enters the dispersion only through the dimensionless products `x = X·Y_0` and `p = B·Z_0`:

```
p = ω C_j Z_0 = ω (s_C ε₀ f ℓ)(√(μ₀/ε₀)) = s_C f · (ω ℓ √(μ₀ε₀)) = s_C f · (ω ℓ / c) = s_C f · θ
x = ω L_j Y_0 = ω (s_L μ₀ f ℓ)(√(ε₀/μ₀)) = s_L f · (ω ℓ / c) = s_L f · θ
```

**MU_0 and EPSILON_0 cancel identically; ℓ_node folds into `θ = ω/ω_C` (a reporting unit).** The dispersion is a pure function of `(θ, f, s_L, s_C)` — all geometric — so `g = ω_top/ω_C` is a pure number and no physical scale is an input. The vertex-parasitic module therefore imports **no** scale from `constants.py`: not `OMEGA_C`, not `M_E`, not `L_CELL`/`C_CELL`; nowhere is `1/√(L_j C_j)` set equal to `ω_C` (that was the #613 install). G-A is enforced at code level by an AST/source scan of the extraction functions.

---

## 6. Vertex-extent derivation + the closability question (G-C)

The parasitic exists only because `d > 0`, and **canon fixes no transverse bond scale** (constants.py has only `ℓ_node` and the *larger* `ℓ_c = √6·ℓ_node`; no bond radius, core radius, or filling fraction). Consequences:

- **Canon-faithful limit `f → 0`:** 1D-line bonds ⇒ point junction ⇒ parasitic → 0 ⇒ memoryless `π√3 ω_C` exact (G-B). Not a rescue — what the canonical 1D-line geometry literally implies.
- **Upper-bound probe `f = 0.5`:** the Wigner–Seitz half-bond (the node "owns" the medium out to each bond midpoint). A geometry-only central estimate from the 120° field-merge overlap is a **modeling choice, not a canonical number** (flagged).
- **Sweep:** `g_scalar(f)` over `f ∈ [0, 0.5]`, sensitivity `dg/df` reported first-class. With `s_L = s_C = 1` the exact connected-band ceiling drops ~5% at `f=0.05`, ~9% at `f=0.1`, ~18% at `f=0.2`, ~38% at `f=0.5` (swing ≫ the 10% branch-(iii) threshold). **This is the load-bearing finding: the ceiling is extent-dominated ⇒ the junction question is NOT closable at the TL-abstraction level without a bond transverse scale** — which is exactly why X36 had to install one. The FORM is derived; the MAGNITUDE is not canon-determined.

---

## 7. Which branch this points to (the driver decides by the frozen rule)

Given the extent-dominated swing, the physics points to **branch (iii)** — bank honestly: the vertex clock's SCALE is not closable at TL abstraction. But the FROZEN rule (prereg §6) is applied by the driver on the COMPUTED swing, not pre-ordained here. The topology class (reactive low-pass, ceiling pinned down ∝ extent) and the derived FORM `g = π√3(1 − κf)`, `κ = s_L + (2/3)s_C`, stand regardless of branch.

**What would flip it to branch (i):** if canon (or Grant) supplies a bond transverse scale making `f ≲ 0.02`, the ceiling recovers `π√3` within tolerance and the vertex clock = the walk clock (X33 two-clock question closes in-engine). That is the surfaced pre-test-physics question, not a lane decision.

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
