# 89 — Round 11 (vi) Stride 2: Topological Mismatch Between (p,q) Torus and Chair-Ring 1-Graph

**Status:** implementer-drafted, 2026-04-29. Stride 2 work record per [doc 88 §3.3](88_round_11_vi_stride_1_a43_v14.md#33--stride-2-plan-deferred-to-fresh-session) Stride 2 plan. Continues the analytical work begun at Stride 1.

**Scope:** identify the topological-completeness mismatch between the continuum (p,q) Beltrami eigenmode framework and the discrete chair-ring graph — load-bearing for the eigenmode derivation. **NOT** the full 1-graph eigenmode derivation (deferred to Stride 3 / fresh session).

**Verdict:** the 6-node chair-ring is a 1-graph (closed cycle), not a 2-torus surface. The (p,q) torus knot Beltrami eigenmode framework requires INDEPENDENT poloidal and toroidal directions — the 1-graph has only the toroidal direction. The corpus electron's tube cross-section (radius ℓ_node/(2π) per Vol 1 Ch 1:18) is sub-lattice on K4 and cannot be resolved by adding more nodes within the K4 substrate. **The eigenmode derivation must proceed on the 1-graph with K4-chiral structure, NOT as a continuum (p,q) projection onto an insufficient discretization.**

---

## §1 — The topological mismatch

### §1.1 — Continuum (p,q) Beltrami eigenmode requires 2-torus surface

The eigenvalue formula k² = (p/r)² + (q/R)² for (p,q) Beltrami eigenmode applies to a 2-torus surface T² with major radius R and minor radius r. The mode is parameterized by two independent angles:

- **Toroidal angle φ ∈ [0, 2π):** rotation around the central axis of the torus (the loop's "long way around")
- **Poloidal angle θ ∈ [0, 2π):** rotation around the tube's cross-section (the "short way around")

The (p,q) winding means: traversing the torus once, the curve completes p full poloidal cycles and q full toroidal cycles. For (1,1): one full poloidal × one full toroidal cycle, which is the unknot path on the torus surface.

A 2-torus has two independent dimensions (φ and θ), each with its own length scale (R and r respectively). The Beltrami eigenmode amplitude depends on BOTH directions: A = A_θ(φ, θ)·ê_θ + A_φ(φ, θ)·ê_φ, with both components varying as functions of both angles.

### §1.2 — The 6-node chair-ring is a 1-graph (closed cycle), not a 2-torus

The 6-node hexagonal chair-ring on K4 (per [doc 83 §6.1](83_phase1_bond_pair_vs_bond_cluster_scale.md) traversal) is a graph with:
- 6 nodes (alternating A/B sublattice sites)
- 6 bonds (closed cyclic connectivity)
- Topology: a closed 1-cycle (homologically S¹)

There is only ONE direction on this graph: the toroidal direction (going around the closed loop). There is no separate poloidal direction encoded in the graph structure.

Each ring node has 4 K4 ports, but only 2 are in-ring bonds (the cyclic neighbors). The other 2 ports lead to non-ring K4 nodes that are NOT part of the chair-ring graph as-defined.

### §1.3 — Empirical evidence: trapped state IS 1D on K4

From v6/v7/v8 dimensional inspection (post-v6 detailed analysis):
- Near-ring shell (2-step neighborhood, K4-active sites): **0.00% energy**
- 6 ring nodes: **96-98% energy**
- Far bulk (rest of interior): 1-4% (numerical drift + boundary scatter, NOT physical leakage)

The trapped state is empirically confined to the 6 ring nodes — a 1-dimensional structure on the K4 lattice. The tube cross-section direction is NOT excited in the trapping dynamics.

### §1.4 — Why "more lattice points" doesn't fix this

The corpus electron's tube radius is **sub-lattice** on K4:
- Per [Vol 1 Ch 1:18](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex#L18): tube radius = ℓ_node/(2π) ≈ 0.16·ℓ_node
- Per [Vol 2 Ch 7:357](../../manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex#L357): tube radius = ℓ_node (= 1·ℓ_node)
- Either way: ≤ 1 lattice spacing

The K4 lattice cannot sample inside the tube cross-section because the tube is at-or-below the lattice resolution. Adding more chair-ring nodes (8-node, 12-node) doesn't add poloidal sampling — it just makes the toroidal sampling finer.

To resolve the tube cross-section, the substrate would need finer-than-K4 sampling: continuum FDTD, or a sub-lattice K4 refinement that doesn't exist in the AVE engine.

### §1.5 — Topological-completeness conclusion

**The (p,q) torus knot Beltrami eigenmode framework cannot be applied to the chair-ring graph at corpus geometry.** The framework requires 2-torus surface structure with both poloidal and toroidal directions; the chair-ring + K4 substrate at corpus scale provides only the toroidal direction.

This is independent of:
- The R/r corpus-citation status (A43 v14 from doc 88 §1)
- The dispersion-vs-curl-eigenvalue distinction (doc 88 §2.5)

It's a topological structure issue: the discrete object (chair-ring 1-graph) doesn't have the same topological dimensions as the continuum object ((p,q) torus knot 2-torus) the formula assumes.

---

## §2 — Implications for Round 11 (vi) resolution candidates

Per doc 88 §2.4, five candidate resolutions for the dimensional inconsistency:

**(1) Continuum formula doesn't apply to discrete K4** — **CONFIRMED with deeper reason.** Not just discrete-vs-continuum; the discrete object is topologically different (1-graph vs 2-torus). Even a fully refined discrete K4 sampling can't recover (p,q) structure if the tube cross-section is sub-lattice.

**(2) Corpus electron isn't (1,1)** — POSSIBLE but only if reframed: maybe the canonical electron isn't a (p,q) torus knot at all. Per [backmatter/05:302](../../manuscript/backmatter/05_universal_solver_toolchain.tex#L302) verbatim: *"the trefoil (2,3) soliton is NOT the electron (which is an unknot 0_1, NOT a torus knot)."* The unknot 0_1 in the topological-knot-theory sense is a 1-graph (closed curve), not a (p,q) torus knot. So the corpus electron canonically IS a 1-graph object, NOT a torus-knot 2-surface.

**(3) Dispersion vs curl eigenvalue distinction** — STILL APPLICABLE. Even on a 1-graph, the relationship between time-domain frequency (= rest mass / ℏ) and spatial Beltrami curl eigenvalue may be independent. Stride 3 must derive both for the 1-graph eigenmode.

**(4) R, r values aren't ~(1, 1/(2π))** — **STRONGEST per §1.4.** The corpus electron's tube radius is sub-lattice on K4. There IS no (R, r) pair that represents the corpus electron at K4 resolution because the tube cross-section is unresolvable. The "geometry" parameter is just R (loop radius); r is below resolution.

**(5) Beltrami claim isn't load-bearing in (p,q) sense** — **STRENGTHENED.** [Vol 1 Ch 3:402](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex#L402) verbatim: *"The electron unknot (0_1) is a Beltrami standing wave (∇×A = k·A) on the chiral K_4 graph."* Says "Beltrami on the chiral K4 graph" — doesn't specify (p,q) torus framework. Reading literally: Beltrami is on the 1-graph, NOT the 2-torus. The (p,q) torus knot framework was implementer-imposed via doc 85 §3.2 derivation; the corpus statement is more general.

**Stride 2 conclusion:** the canonical reading per Vol 1 Ch 3:402 + backmatter/05:302 is **Beltrami eigenmode on the chiral K4 graph** (1-graph), NOT (p,q) torus knot Beltrami eigenmode (2-torus). The doc 85 §3.2 framework imported continuum 2-torus structure that doesn't match the discrete K4 substrate at corpus scale.

---

## §3 — What this changes about Round 11 (vi) Stride 3 plan

Updated Stride 3 plan (replaces doc 88 §3.3 sketch):

1. **Choose framing path:** the canonical Vol 1 Ch 3:402 reading is "Beltrami on chiral K4 graph." Stride 3 derives the eigenmode in this framework, NOT the (p,q) torus formulation.

2. **Define discrete operators on the 1-graph chair-ring:**
   - Vector field A: 3D vector at each of 6 ring nodes (12 → 18 DOF, since each ring node has 3 vector components)
   - Discrete Laplacian on the 1-graph: ΔA_n = A_{n+1} - 2·A_n + A_{n-1} (cyclic, per-component)
   - Discrete curl on K4 chiral graph: requires local 4-port structure at each ring node + the chair-ring's specific bond directions

3. **Beltrami eigenvalue problem:** find A such that ∇×A = k·A on the 1-graph chair-ring with K4-chiral structure. This is a finite-dimensional eigenvalue problem (18 × 18 matrix, with chiral K4 constraints reducing the effective dimension).

4. **Compton-frequency identification:** is the canonical k for the corpus electron set by ω_C/c (free-wave dispersion)? Or determined by the standing-wave time-domain oscillation independent of spatial curl eigenvalue per (3) in §2? Stride 3 must adjudicate.

5. **TRUE Beltrami standing wave IC for v9:** uniform time-phase across all bonds, magnitudes per the discrete A_0(node) eigenvector from step 3. NOT (p,q) torus mode.

Estimated cost: 2-3 fresh sessions of careful linear algebra + finite-difference eigenmode work.

---

## §4 — Refines the closure-narrative walkback further

Per doc 87 §3.4 + doc 88 §3.2.1: v6/v7/v8's empirical anchoring claim is "engine hosts a trapped configuration at canonical topology + canonical scale" but NOT "engine hosts the corpus electron at canonical Beltrami structure."

§1-§2 above sharpens this further:

- **The framework's "(1,1) Beltrami at Compton frequency at corpus geometry" claim was WRONG TOPOLOGICAL TYPE** — it imported (p,q) torus 2-surface structure that doesn't apply to the chair-ring 1-graph.
- The canonical Vol 1 Ch 3:402 statement is "Beltrami on chiral K4 graph" — this IS load-bearing for the corpus electron, but Beltrami in the 1-graph sense, not (p,q) torus.
- v6/v7/v8's empirical signals (96% localization, thermal robustness, 200P persistence) are still real. They're signals for *some* trapped configuration on the chair-ring 1-graph. Whether that configuration is the canonical Beltrami 1-graph eigenmode is what Stride 3 must verify by deriving the eigenmode and constructing v9 IC.

The walkback is cleaner now: v6/v7/v8 didn't fail to test Beltrami; they tested the WRONG Beltrami (continuum 2-torus instead of discrete 1-graph). Stride 3 will test the right one.

---

## §5 — Compliance check + open questions for Grant

**Manuscript-canonical citations grep-verified:**
- [Vol 1 Ch 1:18](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex#L18) ✓ unknot, tube radius ℓ_node/(2π)
- [Vol 1 Ch 3:402](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex#L402) ✓ "Beltrami standing wave on chiral K_4 graph" (no (p,q) qualifier)
- [Vol 2 Ch 7:357](../../manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex#L357) ✓ orbital-scale tube radius = ℓ_node
- [backmatter/05:302](../../manuscript/backmatter/05_universal_solver_toolchain.tex#L302) ✓ electron = unknot 0_1, NOT torus knot

**Synthesis claims (this stride):**
- §1.5 topological mismatch identification — built from canonical statements + standard differential topology
- §2 candidate-resolution evaluation — implementer synthesis selecting (4) and (5) as strongest
- §3 Stride 3 plan — implementer synthesis on what Stride 3 needs to do given §1-§2 findings

**Open questions for Grant adjudication (per Rule 16):**

1. **Is the canonical reading of Vol 1 Ch 3:402 "Beltrami on chiral K4 graph" = 1-graph Beltrami, OR = (p,q) torus Beltrami with K4 as the substrate hosting the torus?** §2 (5) reads it as 1-graph. The doc 85 §3.2 derivation read it as torus. These are substantively different and the corpus statement doesn't disambiguate explicitly.

2. **Is the corpus electron's tube cross-section a load-bearing physical structure, or a continuum-limit artifact?** If it's load-bearing (electron has internal tube structure), the framework needs sub-lattice resolution that K4 doesn't provide. If it's a continuum-limit artifact (electron is fundamentally a 1D ring + the "tube" is a continuum smoothing), the K4 chair-ring is the right discretization.

3. **Acceptable for Stride 3 to proceed with the 1-graph Beltrami framing per §2 (5), or should we pause for explicit corpus adjudication first?** Per always-research-before-asking + manuscript-over-research, the Vol 1 Ch 3:402 verbatim doesn't specify (p,q); Stride 3 can proceed with the 1-graph reading provisionally. But if Grant's intuition says the tube IS load-bearing, that changes Stride 3 substantively.

---

## §7 — Correction per Grant 2026-04-29: K4 is 3D-connected; chair-ring isn't pure 1-graph

> **🟡 SUBSTANTIVE CORRECTION (added 2026-04-29 post-Grant pushback per Rule 12 retraction-preserves-body):** §1.2's claim that "the 6-node chair-ring is a 1-graph (closed cycle), not a 2-torus surface" is **overstated**. The chair-ring graph as the in-ring-bonds-only subgraph IS a 1-graph (6 nodes, 6 in-ring bonds, closed cycle). But the chair-ring NODES embedded in the full K4 lattice are **3D-connected** — each ring node has 4 K4 ports providing access in 4 tetrahedral directions, of which only 2 are in-ring and 2 are out-of-ring.

### §7.1 — Correct K4 structure at chair-ring nodes

At each chair-ring node, the 4 K4 ports decompose:

| Port | Direction (A-site) | Connects to | Role at chair-ring |
|---|---|---|---|
| 0 | (+1,+1,+1)/√3 | tetrahedral B-neighbor | IN-RING or OUT-OF-RING (depends on which node) |
| 1 | (+1,-1,-1)/√3 | tetrahedral B-neighbor | IN-RING or OUT-OF-RING |
| 2 | (-1,+1,-1)/√3 | tetrahedral B-neighbor | IN-RING or OUT-OF-RING |
| 3 | (-1,-1,+1)/√3 | tetrahedral B-neighbor | IN-RING or OUT-OF-RING |

For ring node 0 = A(0,0,0): in-ring ports 0 (toward ring node 1) and 2 (toward ring node 5); out-of-ring ports 1 and 3 (toward non-ring K4 lattice nodes).

The 2 out-of-ring ports point in directions that approximately span the **local poloidal plane** (perpendicular to the ring tangent at that node). They DO provide spatial degrees of freedom for poloidal-direction A field components.

### §7.2 — What v6/v7/v8 actually did wrong

v6/v7/v8 IC explicitly **zeroed the out-of-ring ports**:

```python
# Only set V_inc + Phi_link on the bond's IN-RING port
engine.k4.V_inc[ix_a, iy_a, iz_a, port_a] = v_value  # in-ring port only
engine.k4.Phi_link[ix_a, iy_a, iz_a, port_a] = phi_value  # in-ring port only
# Out-of-ring ports stayed at zero
```

The empirical observation "0% energy at near-ring shell" wasn't because the substrate is 1D — it's because **the IC didn't seed the poloidal direction**. The trapped state stayed 1D because the IC never gave it transverse degrees of freedom to populate.

This is a substantively different finding than §1.5 / §3 claimed. Corrections to those sections:

- **§1.5 retracted:** the chair-ring is NOT topologically forbidden from hosting (p,q) torus modes. The substrate has 3D access via out-of-ring ports.
- **§2 (1) "Continuum formula doesn't apply" still partially correct** but for a different reason: discretization density, not topological completeness.
- **§2 (5) "Beltrami isn't load-bearing in (p,q) sense" overstated** — Vol 1 Ch 3:402's "Beltrami on chiral K_4 graph" might still refer to (p,q) torus Beltrami if the K4 graph hosts the 2-torus structure via 3D port access.

### §7.3 — What survives: poloidal sampling density issue

The §1.5 finding is weaker than originally framed but not entirely wrong. The full (p,q) torus Beltrami framework requires continuous variation in the poloidal direction (p winding cycles around the cross-section). For p ≥ 1 winding:

- **Need at least 3 poloidal samples per cross-section** (Nyquist + 1 for one full cycle)
- **Chair-ring has 2 out-of-ring ports per ring node → 2 poloidal samples per cross-section**
- **2 samples is sub-Nyquist for p ≥ 1**

So the chair-ring + 1-step K4 neighborhood CAN host approximate poloidal structure (better than the 1D-only IC of v6/v7/v8), but is sub-Nyquist for full (p,q) winding representation. This is a **discretization-density issue**, not a topological-completeness issue. To get above Nyquist for p=1, would need more poloidal sampling — e.g., chair-ring + 2-step K4 neighborhood (more out-of-ring nodes) might give 4+ poloidal samples per cross-section.

### §7.4 — Updated Stride 3 plan

Replaces §3:

1. **Choose framing path:** the canonical Vol 1 Ch 3:402 reading is "Beltrami on chiral K4 graph." Stride 3 derives the eigenmode in this framework, using the FULL K4 4-port structure at each chair-ring node (not just in-ring bonds).

2. **Define discrete operators on the chair-ring + K4 neighborhood:**
   - Vector field A: 3D vector at each chair-ring node + immediate K4 neighbors (≥ 18 nodes total: 6 ring + 12 out-of-ring 1-step neighbors)
   - Discrete Laplacian on the K4 graph (uses all 4 ports per node, not just in-ring 2)
   - Discrete curl on the chiral K4 graph (uses local 4-port structure with chirality)

3. **Beltrami eigenvalue problem:** find A such that ∇×A = k·A on the chair-ring + K4 neighborhood graph. Output: discrete A_0(node) eigenvector + corresponding k_Beltrami_discrete value.

4. **Compton-frequency identification:** is the canonical k for the corpus electron set by ω_C/c (free-wave dispersion)? Or determined by the standing-wave time-domain oscillation independent of spatial curl eigenvalue? Stride 3 must adjudicate.

5. **TRUE Beltrami standing wave IC for v9:**
   - Set V_inc and Phi_link on **ALL 4 ports** of each ring node (not just in-ring 2)
   - Magnitudes per the discrete A_0(node) eigenvector
   - Includes out-of-ring port contributions for poloidal direction
   - Uniform time-phase across all bonds

6. **Sampling-density check:** with 2 poloidal samples per cross-section (chair-ring + 1-step K4 neighborhood), is the (1,1) Beltrami mode adequately represented at K4 resolution? If sub-Nyquist warning fires, may need to extend to 2-step K4 neighborhood (more poloidal sampling).

Estimated cost: 2-3 fresh sessions; output v9 IC specification.

### §7.5 — Closure-narrative implications

The doc 87 §3.4 + doc 88 §3.2.1 walkback ("trapped configuration of some kind, NOT confirmed Beltrami") is **slightly less severe** than I framed it after doc 89. Specifically:

- The framework's "(p,q) Beltrami at corpus geometry" claim isn't topologically impossible; it's substrate-resolution-limited at K4 scale
- v6/v7/v8 didn't fail to test (p,q) Beltrami due to topological mismatch — they failed because the IC zeroed the poloidal port directions
- v9 with corrected IC seeding all 4 ports at each ring node IS a legitimate test of the (p,q) Beltrami framework on the K4 substrate

The walkback still stands ("trapped configuration of some kind") because v6/v7/v8 didn't seed poloidal direction. But the path forward is clearer: v9 must include out-of-ring port seeding.

### §7.6 — A43 v16 candidate

Per A43 v2 lane-symmetric anyone-must-grep: the "chair-ring is 1-graph" framing in §1.5 was implementer overstatement that propagated through Stride 2's commit and the v8 commit message walkback. Caught by Grant's "3-connected graph" pushback within ~1 turn — clean cross-lane catch.

Auditor-lane queue addition: A43 v16 — chair-ring 1-graph overstatement (substrate is 3D-connected via K4 4-port structure; in-ring bonds form 1-cycle but full K4 lattice connectivity is 3D). Catches a topological-vs-substrate-sampling distinction that wasn't cleanly separated in §1-§3.

---

## §6 — References

- [Doc 87](87_path_alpha_v8_round_11_ignition.md), [Doc 88](88_round_11_vi_stride_1_a43_v14.md) — Stride 1 + audit-integration addendum
- [Doc 85 §3.2](85_kelvin_beltrami_foc_axiom_grounded_derivation.md) — original (p,q) torus eigenvalue derivation (now flagged as wrong topological type for K4 chair-ring)
- [Vol 1 Ch 1:18, 32](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex)
- [Vol 1 Ch 3:402](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex#L402)
- [Vol 2 Ch 7:357](../../manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex#L357)
- [backmatter/05:302](../../manuscript/backmatter/05_universal_solver_toolchain.tex#L302)
- [`COLLABORATION_NOTES.md`](../../.agents/handoffs/COLLABORATION_NOTES.md) Rule 14 (substrate-derives), Rule 16 (ask-Grant-fundamental-physics), A43 v2 (anyone-must-grep), A43 v14/v15 (R/r + tube radius corpus-inconsistencies)
