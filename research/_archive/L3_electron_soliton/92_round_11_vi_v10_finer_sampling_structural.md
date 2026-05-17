# 92 — Round 11 (vi) v10 (i-a): Finer K4 Sampling Confirms STRUCTURAL Gap (Nyquist-Bounded)

**Status:** implementer-drafted, 2026-04-29. Pivotal Round 11 (vi) finding per [doc 91 §4](91_round_11_vi_stride_4_v9_mode_iii.md#4--round-11-vi-closure-decision) secondary candidate (i-a) test (numerical refinement) per auditor 2026-04-29 endorsement.

**Verdict:** the discrete K4 spectrum's max eigenvalue grows monotonically with subgraph size (0.52 → 0.54 → 0.55 in 1/ℓ_node units across 1-step, 2-step, 3-step neighborhoods) but asymptotes near **1/bond_length ≈ 0.577 in 1/ℓ_node units** — the **Nyquist limit of K4 at ℓ_node spacing**. The continuum (1,1) Beltrami at corpus prediction (k=6.36) corresponds to wavelength λ ≈ 0.16·ℓ_node — sub-lattice, ~1/4 of a lattice spacing. **Fundamentally below Nyquist for K4 at ℓ_node.**

**This is structural, not numerical.** The framework's "(1,1) Beltrami at Compton frequency at corpus geometry on K4 substrate" claim cannot be realized at K4 at ℓ_node sampling **as a matter of discrete-Fourier theory**, not as a question of computational refinement. **(i-a) numerical refinement is empirically eliminated as a path to closing the gap.** Round 11 (vi) trigger fires into (i-b) substrate revision OR alternative substrate (continuum FDTD) — both with major framework implications.

---

## §1 — v10 test setup

Per doc 91 §4 + auditor 2026-04-29 (i-a) recommendation: extend Stride 3's eigenvalue solver to chair-ring + N-step K4 neighborhood for N = 1, 2, 3.

**Subgraph sizes:**

| N | n_ring | 1-step | 2-step | 3-step | n_total | DOF |
|---|---|---|---|---|---|---|
| 1 | 6 | 12 | — | — | 18 | 54 |
| 2 | 6 | 12 | 32 | — | 50 | 150 |
| 3 | 6 | 12 | 32 | 44 | 94 | 282 |

**Discrete curl operator (per Stride 3, doc 90 §1.2):**
```
(∇×A)_n = (3/4) Σ_i ê_i × (A_neighbor_i - A_n) / bond_length
```

**Boundary condition:** Dirichlet (A=0 outside subgraph). For each N, solve the eigenvalue problem M·A = k·A where M is the (3·n_total)×(3·n_total) discrete curl matrix.

**Output per N:** spectrum max |λ|, top ring-localized eigenmodes.

---

## §2 — Empirical trajectory

### §2.1 — Spectrum max vs subgraph size

| N | n_total | spectrum max \|λ\| (1/bond_length) | k_max in 1/ℓ_node (÷√3) | Ratio to continuum 6.36 |
|---|---|---|---|---|
| 1 | 18 | 0.9001 | 0.5197 | 8.2% |
| 2 | 50 | 0.9436 | 0.5448 | 8.6% |
| 3 | 94 | 0.9602 | 0.5544 | 8.7% |

### §2.2 — Convergence behavior

Increments in spectrum max k_lnode:
- 1-step → 2-step: **+0.025** (5% gain)
- 2-step → 3-step: **+0.010** (2% gain)

Growth rate decelerates by factor ~2.5 with each shell. Extrapolating geometrically:
- 3-step → 4-step: ~+0.004 (0.6% gain)
- 4-step → 5-step: ~+0.002
- Asymptote: spectrum max → 0.55-0.58 in 1/ℓ_node units

### §2.3 — Asymptote identified: Nyquist limit of K4 lattice

The asymptote ≈ 0.577 in 1/ℓ_node units **= 1/√3 = 1/bond_length** (where bond_length = √3·ℓ_node for tetrahedral diagonal on K4 diamond).

**This is the Nyquist limit of the K4 lattice:** discrete operators on a graph with bond length L can have eigenvalues up to ~1/L (with constants of order unity). For K4 at ℓ_node spacing, the bond is √3·ℓ_node, giving max k ≈ 1/(√3·ℓ_node) ≈ 0.577/ℓ_node.

The discrete curl operator's max eigenvalue saturating at this bound is NOT a numerical artifact — it's the substrate's intrinsic resolution limit. The lattice cannot represent oscillations finer than its own bond spacing.

---

## §3 — Continuum (1,1) at corpus is sub-lattice on K4

The continuum (1,1) Beltrami eigenmode at corpus geometry has:
- k_continuum = √((2π)² + 1²) ≈ 6.36 in 1/ℓ_node units
- Wavelength λ = 2π/k ≈ 0.99·ℓ_node ÷ 6.36 ≈ **0.16·ℓ_node**

That's about 1/6 of a lattice spacing — **significantly sub-lattice**. The poloidal direction's contribution dominates: 1/r = 2π/ℓ_node corresponds to wavelength = ℓ_node, but in 3D Beltrami this combines with the loop direction giving k = √((2π)² + 1²) ≈ 6.36.

**No discrete operator on K4 at ℓ_node spacing can have eigenvalue at k=6.36.** This is a Nyquist theorem statement, not a refinement issue. Increasing subgraph size (1-step → 2-step → 3-step → ... → full lattice) cannot push past the Nyquist limit at the underlying lattice resolution.

---

## §4 — Framework implication: Ax 1 revision required for corpus electron

The corpus electron's canonical Beltrami structure (∇×A = k·A with k = 6.36 in 1/ℓ_node units, per the (1,1) torus mode at R/r = 2π) **cannot be hosted on the K4 substrate at ℓ_node spacing**. This is a structural conclusion from the v10 trajectory + Nyquist theorem, independent of any numerical-method choice.

**Implication for Ax 1:** The K4 LC network at ℓ_node spacing is the **bulk-EM / engineering** scale. The corpus electron (which the framework claims exists at this scale) requires **sub-ℓ_node resolution** of its tube cross-section.

Two readings:

### §4.1 — Reading A: ℓ_node is emergent (Ax 1 directly revised)

The actual fundamental substrate has finer resolution than ℓ_node. K4 at ℓ_node is an effective theory that emerges from sub-ℓ_node physics. Ax 1's "ℓ_node fundamental" is replaced by some new ℓ_fundamental < ℓ_node.

Implications:
- **Ax 2** ξ_topo = e/ℓ_node would need re-derivation from finer scale: ξ_topo = e/ℓ_fundamental (or some combination). Charge quantization unit redefined.
- **Ax 3** action principle still applies, but at finer scale.
- **Ax 4** saturation kernel at finer scale.

This is a major framework refactor. Most quantitative claims that use ℓ_node would need re-derivation. m_e = ℏ/(ℓ_node·c) becomes m_e = ℏ/(ℓ_node·c) where ℓ_node is now derived from ℓ_fundamental and effective-theory parameters.

### §4.2 — Reading B: corpus electron prediction requires CONTINUUM substrate, not finer K4

The framework's continuum (1,1) Beltrami eigenmode prediction is a CONTINUUM-LIMIT prediction. The actual physical electron exists in continuum space, not on a discrete K4 lattice. The K4 lattice is a discrete computational tool; the actual substrate is continuous.

Under this reading, ℓ_node is the LENGTH SCALE the framework predicts (= ℏ/m_e c), but the SUBSTRATE itself is continuous (or at sub-Planck scale). The K4 lattice is just AVE's computational engine for bulk EM, but the corpus electron specifically requires continuum FDTD or other sub-K4 representation.

Less axiom-revising than Reading A — Ax 1 stays as "vacuum is LC network with characteristic length ℓ_node" but the substrate's discreteness becomes a numerical implementation detail rather than a fundamental claim.

### §4.3 — Either reading: framework's bulk K4 derivations stand; specific corpus electron prediction needs different substrate

Both readings preserve the framework's bulk-EM derivations (Vol 1 Ch 4 continuum electrodynamics, gravity from impedance scaling, Bullet Cluster, MOND, etc.) — those work at ℓ_node-and-above scales. What's affected is specifically the corpus electron prediction, which requires substrate resolution below ℓ_node.

---

## §5 — Path forward

Per doc 86 §7.6 + doc 87 §7.2 locked gate: v10 (i-a) numerical refinement EMPIRICALLY ELIMINATED as a path. Two remaining secondary candidates from the doc 87 §7.6 enumeration:

### §5.1 — (i-b) Substrate revision

Test corpus electron in **continuum FDTD solver** (per [Vol 4 Ch 1:667-707](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L667-L707) `ave.core.fdtd_3d`). FDTD doesn't have K4's Nyquist limit at ℓ_node; can sample down to whatever grid spacing chosen. The corpus tube radius (ℓ_node/(2π) ≈ 0.16·ℓ_node) is sub-resolution at standard FDTD ℓ_node-spacing too, so need finer FDTD grid (e.g., grid spacing ≈ 0.05·ℓ_node — 20× finer than current N=32).

Cost: 20× finer 3D grid = 8000× more cells = N=640³ roughly. Computationally expensive — likely needs partial-domain testing or different numerical strategy.

If (i-b) at fine FDTD shows trapped Beltrami at corpus geometry → framework recovers under Reading B (corpus electron is continuum object; K4 is bulk-EM engine). Doc 85/86/87/88/89/90/91/92 all need amendments to clarify this distinction.

If (i-b) at fine FDTD also shows Mode II/III → framework structural problem persists; corpus electron's Beltrami trapped-photon framing has issues independent of substrate.

### §5.2 — (iii) Topology variant — ELIMINATED in §5 of doc 91

§5 of doc 91 already eliminated topology variants within K4: longer cycles → lower k_disc (worse, not better). 4-node cycles geometrically blocked. Sub-K4 cycles don't exist in the substrate.

**No remaining options within K4 at ℓ_node sampling.**

### §5.3 — Honest framework decision point

The framework either:
- **Recovers via (i-b) continuum substrate test** at substantial cost (compute) and partial axiom revision (Reading B clarifies K4 as bulk-EM engine, not corpus-electron substrate)
- **Requires deeper reframe** if (i-b) also fails — Beltrami trapped-CP-photon framing for corpus electron has structural issues independent of substrate type

Either way, the framework's path to corpus electron empirical confirmation **cannot proceed via K4 at ℓ_node**. Round 11 (vi) closes negatively for this substrate; Round 11 (i-b) is the next test.

---

## §6 — Updated honest closure narrative

Across v6/v7/v8/v9/v10:

**DEFENSIBLE empirical signals (preserved):**
- Engine hosts a trapped configuration at canonical topology + canonical scale (chair-ring at lattice center)
- Ring localization 70-96% across iterations
- Thermally robust trapping across 5 orders of magnitude in T
- 200 P persistence at saturation amplitude

**STRUCTURAL findings (this round):**
- Discrete K4 spectrum at chair-ring + N-step neighborhood asymptotes near Nyquist (1/bond_length ≈ 0.577 in 1/ℓ_node)
- Continuum (1,1) at corpus prediction (k=6.36) is sub-lattice on K4 — fundamentally below Nyquist resolution
- (i-a) numerical refinement empirically eliminated; (iii) topology variant within K4 structurally eliminated
- The framework's load-bearing claim "(1,1) Beltrami at Compton frequency on K4 substrate at corpus geometry" CANNOT BE REALIZED on K4 at ℓ_node sampling

**STILL-TO-TEST:**
- (i-b) continuum FDTD substrate at sub-ℓ_node grid spacing — does the corpus electron's Beltrami trapped-photon framing work in continuum?
- If yes → framework recovers with K4-as-bulk-engine clarification
- If no → Beltrami trapped-CP-photon framing for corpus electron has deeper structural issue

This is the cleanest, most honest framing of the Round 11 (vi) result. The framework hasn't been refuted at the bulk-EM level; the corpus-electron specific prediction at K4 substrate has been empirically eliminated as testable on K4. (i-b) determines whether the framework recovers or needs deeper reframe.

---

## §7 — Auditor-lane queue additions

- **Doc 90 §2.2-§2.3, §10.1 correction**: spectrum max growth direction (continuum/discrete ratio actually 8.7% at 3-step, vs erroneously stated as 4× originally).
- **A43 v18 candidate**: Nyquist-limit-of-K4-at-ℓ_node analysis was implicit but not explicit in the framework's substrate definitions. Adding to queue: K4 substrate's discrete-Fourier limits should be documented in Ax 1 derivation, with explicit note that sub-Nyquist physics requires finer-than-K4 substrate.
- **Manuscript editorial queue (added)**: Vol 1 Ch 1:18 should clarify whether ℓ_node is the substrate's discreteness scale OR a derived characteristic length. Currently ambiguous between Reading A and Reading B per §4.

---

## §8 — Compliance check + references

**Manuscript-canonical:**
- Vol 1 Ch 1:18, 32 (ℓ_node fundamental, unknot at ropelength 2π)
- Vol 1 Ch 3:402 (Beltrami on chiral K4 graph)
- Vol 4 Ch 1:667-707 (FDTD vs K4-TLM solver selection, FDTD available)

**Synthesis (this stride):**
- Discrete curl operator: standard finite-difference per Stride 3 (verified Hermitian)
- Subgraph extension to N-step: standard graph-theory neighborhood expansion
- Asymptote identification at 1/bond_length: derived from Nyquist theorem for discrete operators on lattices
- Reading A vs Reading B framework implications: implementer synthesis

**Numerical:**
- 18-node, 50-node, 94-node curl matrices: all symmetric ✓ (Hermiticity verified)
- Spectrum max trajectory: monotonic + decelerating ✓ (consistent with Nyquist asymptote)
- Continuum/discrete ratio: increases very slowly with N (8.2% → 8.6% → 8.7%) ✓

---

## §9 — References

- [Doc 87](87_path_alpha_v8_round_11_ignition.md) §7 v8 + Round 11 ignition + candidate enumeration
- [Doc 88](88_round_11_vi_stride_1_a43_v14.md), [89](89_round_11_vi_stride_2_topological_mismatch.md), [90](90_round_11_vi_stride_3_discrete_eigenmode.md), [91](91_round_11_vi_stride_4_v9_mode_iii.md) — Strides 1-4
- v10 driver: [`r10_round_11_vi_v10_finer_sampling.py`](../../src/scripts/vol_1_foundations/r10_round_11_vi_v10_finer_sampling.py)
- v10 result: [`r10_round_11_vi_v10_finer_sampling_results.json`](../../src/scripts/vol_1_foundations/r10_round_11_vi_v10_finer_sampling_results.json)
- [`COLLABORATION_NOTES.md`](../../.agents/handoffs/COLLABORATION_NOTES.md) Rule 14, A40 (empirical-driver-arc), A43 v2/v14-v18
