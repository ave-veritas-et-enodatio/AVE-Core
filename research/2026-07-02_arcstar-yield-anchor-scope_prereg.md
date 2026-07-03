# PREREG — `arc* < ℓ_node` forward prediction: scope to benchtop-testable claim OR internal refinement

**Date:** 2026-07-02
**Lane:** research / scoping (bounded — NOT an epic). HOLD canonization. Do NOT merge — push + report.
**Branch:** `analysis/arcstar-yield-anchor-scope` (off `origin/main` @ `a00ec11a` — includes the merged Axiom-4 arc, PR #460)
**Source result:** [`2026-07-02_axiom4-moduli-hierarchy_result.md`](2026-07-02_axiom4-moduli-hierarchy_result.md) (PR #460) §4 — the forward prediction: a compressible K4 strut settles at a self-consistent fixed arc-length `arc* = 4ρ/(4ρ+1)·ℓ_node`, so the saturation kernel's effective yield strain is `arc* < ℓ_node` by O(1/ρ), ~4.5–11% short of the bare bond length (ρ = slenderness² ∈ [2, 5.3]).
**Discipline fired:** `ave-prereg` (this doc), `substrate-native-check`, `ave-discrimination-check`, `pre-test-physics-check`, `ave-canonical-source`.

---

## 1. Derivation target (precise, one sentence each task)

1. **Pin the prefactor.** Replace the tent 2-segment kinematic `arc = 2√((A/2)² + S²)` with the continuum-elastica curvature integral for a bowing K4 bond, recompute `arc*(ρ)`, and report whether the O(1/ρ) structure and the 4.5–11% band survive, shift, or become model-robust.
2. **Resolve the yield anchoring.** Determine whether the *measurable* yield (V_yield / the saturation-curve knee) is anchored to the bond length `ℓ_node` (Case a — arc* moves the knee ~5–11%, a direct measurable) or to α via `V_YIELD = √α·V_snap` (Case b — arc*<ℓ_node shows up as a DISCREPANCY between the geometric yield and the α-defined V_yield; the discrepancy is the observable).
3. **Discrimination-check + bench connection.** Determine whether arc*<ℓ_node produces a bench-measurable knee-position deviation (a NEW discriminator) or is an AVE-internal self-consistency refinement (geometric-vs-α yield), and run the SM-counterfactual: is the arc* shift AVE-distinct-vs-SM, or a refinement of the *existing* (already-AVE-distinct) saturation curve.

## 1.5 Physical picture (mechanical, pre-corpus-grep)

- **What is bowing/saturating:** a single K4 strut (bond) between two nodes, over-braced by the sub-isostatic z=4 < 2d=6 misfit. Under axial compression it can either shorten (stretch channel, stiffness k_a) or bow sideways (bend channel, stiffness k_s). ρ = k_a/k_s = slenderness² sets which channel wins.
- **The self-consistent arc-length:** minimizing U = ½k_a(arc − ℓ)² + ½k_s S² over the bow S at fixed axial projection A gives a fixed operating arc-length `arc* = 4ρ/(4ρ+1)·ℓ_node`, independent of A (tent kinematic). The saturation kernel S(A) = ½·arc*·√(1 − (A/arc*)²) is then an exact quarter-arc in u = A/arc*.
- **Where the Γ=−1 boundary is:** the electron's A1 mass core / the local vacuum cell's saturation knee. The bow collapses (vertical tangent) at A = arc* < ℓ_node.
- **The discrete onset:** the saturation knee — the "spike" (C_eff = C_0/S → ∞) or "rolloff" (C_diel ∝ S) at ~85% of E_yield (√3/2 = R_II, the non-linear→saturated boundary).
- **Scale that matters:** dimensionless. arc*/ℓ_node is a pure number; the ε_c = 1 − arc* = 1/(4ρ+1) deficit is O(1/ρ). The α-circularity lesson (MEMORY: `thermal_chirality_cosmology`) says any chord must be a DIMENSIONLESS RATIO — so the arc*/ℓ_node ratio is the right object.

## 2. Corpus state (grep-verified)

**Status: OPEN (a forward prediction flagged for scoping in §4/§7 of the source result), with the anchoring already SETTLED in the KB.**

Prior work cited (verbatim, verified this session):
- `research/2026-07-02_axiom4-moduli-hierarchy_result.md:37` — the tent result + the explicit caveat: *"the prefactor `4ρ/(4ρ+1)` is specific to the tent 2-segment kinematic; a continuum-elastica curvature integral could shift the prefactor. The **structural** conclusions — `arc* < ℓ_node` by `O(1/ρ)`, and the √-in-`u` exactness — are model-robust."*
- `research/2026-07-02_axiom4-moduli-hierarchy_result.md:43` — the quantified band: *"11.1% at `ρ=2`, 4.5% at `ρ=5.3`"* (ε_c = 1/(4ρ+1)).
- `src/ave/core/constants.py:455` — `V_SNAP = (M_E * C_0**2) / e_charge` (≈ 511 kV) — DEFINITIONAL (rest energy / e).
- `src/ave/core/constants.py:464` — `V_YIELD = np.sqrt(ALPHA) * V_SNAP` (≈ 43.65 kV) — **α-anchored**.
- `src/ave/core/constants.py:282` — `L_NODE = HBAR / (M_E * C_0)` — DEFINITIONAL (Compton).
- `src/ave/core/constants.py:475` — `E_YIELD = V_YIELD / L_NODE` (≈ 1.13e17 V/m) — the FIELD couples BOTH α (via V_YIELD) AND ℓ_node.
- `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md:127` (def-vyvsn1 = T2, Grant 2026-06-30), verbatim: *"$V_{\text{yield}}=\sqrt{\alpha}\cdot V_{\text{snap}}$ EXACTLY, so the two are NOT independent per-sector thresholds (the $\sqrt{\alpha}$ is an $\alpha$-echo; $A=\sqrt\alpha$ is a Class-C echo operating point)."* — **this settles Task 2 toward Case (b): the measurable yield is α-anchored.**
- `manuscript/ave-kb/vol4/claim-quality.md:78` — the OPEN measurement-sector question (C_0/S longitudinal-A1 compliance spike ÷S vs C_diel ∝ S transverse rolloff ×S), Grant-flagged.
- EE-bench leaves: `vol4/falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md:36` (knee "at roughly 85% of E_yield"), `ee-bench-plateau.md:26`, `vol4/simulation/ch17-hardware-netlists/ee-bench-netlist.md`. The 85% = √3/2 = R_II (`constants.py:485`, R_II = √3/2 = the non-linear→saturated boundary) — itself a fixed fraction of the α-anchored E_yield.

**No prior elastica-curvature-integral recomputation of arc*(ρ) exists** (grep of research/ for "elastica" returns only keyword-adjacent hits in unrelated docs, and the source result explicitly leaves it open). Task 1 is genuinely open + narrow.

## 3. Predictions (with dimensional analysis)

### Task 1 — the elastica prefactor
- **Prediction:** the O(1/ρ) structure SURVIVES (it is a slenderness-expansion generic, not a tent artifact). The exact prefactor shifts from `4/(4ρ+1)` toward an elastica curvature-integral value with the same leading 1/ρ scaling but a different O(1) coefficient. Expect the band to shift modestly (not by an order of magnitude) — likely to a slightly *smaller* deficit at fixed ρ, because a smooth bow stores bend energy more efficiently than a tent kink (a tent concentrates all curvature at one point → over-penalizes bend → over-bows → over-shrinks arc). **Dimensional check:** ε_c = 1 − arc*/ℓ_node is dimensionless; it must be a pure function of ρ = k_a/k_s (dimensionless stiffness ratio) alone. At the canonical ρ ∈ [2, 5.3] (K=2G-locked), ε_c(tent) = {0.111, 0.045}. Elastica expected same OOM: ε_c(elastica) ~ O(0.03–0.11).
- **Falsifier:** if the elastica integral gives ε_c NOT ∝ 1/ρ at leading order (e.g. 1/√ρ or 1/ρ²), the O(1/ρ) structural claim of the source result is WRONG and must be walked back.

### Task 2 — the anchoring verdict
- **Prediction: Case (b) — α-anchored.** The corpus (`resonant-lc-solitons.md:127`) states V_yield = √α·V_snap EXACTLY, and V_snap = m_e c²/e is definitional (rest energy / e). The measurable knee is therefore pinned to α, NOT to a geometric ℓ_node-arc-length. So arc*<ℓ_node does NOT move the measurable knee; it surfaces as a DISCREPANCY between (i) the geometric yield strain the kernel would predict from arc* and (ii) the α-defined V_yield the corpus calibrates to. The discrepancy IS the observable — but it is an AVE-INTERNAL consistency statement (geometric-vs-α), not a directly-measured knee shift.
- **Dimensional check:** V_YIELD/V_SNAP = √α = 0.0854 (dimensionless, α-set). arc*/ℓ_node = 4ρ/(4ρ+1) = {0.889, 0.955} (dimensionless, ρ-set / K=2G-set). These are TWO INDEPENDENT dimensionless numbers with DIFFERENT provenance (α-echo vs K=2G-import). The prediction is that the measurable is the FIRST (α), and arc* is the SECOND — they do not multiply into the observable knee position; the knee stays at √α·V_snap.
- **Falsifier:** if a corpus leaf anchors the measurable V_yield to ℓ_node·(geometric arc) rather than √α·V_snap, Case (a) holds and arc* moves the knee ~5–11% directly.

### Task 3 — discrimination verdict
- **Prediction: INTERNAL REFINEMENT, not a new bench falsifier.** The whole saturation curve S(A) = √(1−A²) is already AVE-distinct vs SM (SM has flat ε_0; the knee at all is the discriminator). arc*<ℓ_node sharpens AVE's OWN structure (renormalizes A → u = A/arc*, moves the geometric collapse point), but does NOT add a NEW AVE-vs-SM discriminator: SM predicts flat C(E) regardless of arc*, so the arc* shift is invisible against the SM null. The bench discriminator remains "is there a knee at all near √3/2·E_yield," which arc* refines but does not create.
- **SM-counterfactual (Step 2):** SM predicts flat ε_0, no knee — arc* is a ~5% correction to the *position/normalization* of a knee SM says shouldn't exist. A 5% shift of an AVE-internal feature against an SM null is not independently discriminating. **Step 2.5 axis:** the discriminator is the EXISTENCE of the knee (magnitude/shape of the whole curve), not the exact knee position; arc* touches only the position → non-discriminating vs SM.
- **Falsifier:** if arc*<ℓ_node predicted a knee-position shift LARGE enough (and in a direction) that a bench could distinguish "arc*-corrected AVE" from "bare-ℓ_node AVE" AND that distinction mapped to an SM-vs-AVE separation, it would be a bench falsifier. Prediction: it does not (the α-anchoring absorbs it).

## 4. Discriminating outcomes

- **Outcome A (predicted):** elastica confirms O(1/ρ) (band shifts modestly, structure robust); anchoring is Case (b) α-anchored; verdict = INTERNAL REFINEMENT. arc*<ℓ_node banks as a sharpening of AVE's own kernel normalization, NOT a new cRIO C_eff(V) bench target. Recommendation: bank, do not graduate to bench spec.
- **Outcome B (alternative):** anchoring turns out Case (a) ℓ_node-anchored (a corpus leaf pins the measurable to geometry) → arc*<ℓ_node moves the knee ~5–11% → a candidate bench-measurable. Would warrant a scoped cRIO test spec IF the shift is also AVE-vs-SM distinct (unlikely per Step 2, since SM has no knee to shift).
- **Outcome C (null / falsification):** elastica breaks the O(1/ρ) structure (band not ∝ 1/ρ) → the source result's structural claim is wrong → walk-back the "O(1/ρ), model-robust" line in the merged result (Rule 12, 🔴 header; do NOT refill).

## 5. Falsifier (of this scoping's framing)

If the corpus anchoring is genuinely ℓ_node-geometric (not α) AND the elastica arc* shift is both large and AVE-vs-SM-distinct, then "internal refinement" is the wrong verdict and this graduates to a bench falsifier. The load-bearing check is Task 2's anchoring grep — get it wrong and the whole verdict flips.

## 6. No-overclaim commitment

An honest "internal refinement" is the PREDICTED and fully-valid outcome. Do NOT inflate a 5% renormalization of AVE's own kernel into a new AVE-vs-SM chord. The α-circularity lesson (MEMORY `thermal_chirality_cosmology`: chord must be a dimensionless ratio; α re-enters through the √α bias ladder) is the standing guard — arc*/ℓ_node is a K=2G-imported ratio, not an α-free chord.
