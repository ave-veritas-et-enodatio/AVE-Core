# 83 — Round 10+ Phase 1 Direction 3'.1 Reframe: Bond-Pair vs Bond-Cluster Scale

**Status:** implementer-drafted with auditor + Grant pushback, 2026-04-28. Research-tier follow-up doc to round_10_plan.md Phase 1 Direction 3'.1 derivability gate-decision dialogue (commits `6d27e58` doc 79 v5.1 → `cfb203a` doc 81 → `48ee43d` round_10_plan.md → `35cc818` operators.md + Direction 3.4/3.5 corrections → `2a684a4` path α v4 → `d4b0495` path α v4b).

**Per Rule 9 v2 + auditor catch + Grant's multi-bond-framing challenge:** Phase 1 path α v1-v4(b) tested bond-CLUSTER scale, NOT corpus-canonical bond-PAIR scale. Direction 3'.1 gate-decision is YES on substrate-resolvability of (ε) bound-state-vs-free-state interpretation, but the entire path α arc tested the wrong object class for corpus electron comparison. Doc 83 captures the reframe.

**NOT a closure-doc revision.** Doc 79 v5.1 closure stands; this is research-tier follow-up scoping Direction 3'.2 work at the correct object class.

---

## §1 Context

Round 10+ Phase 1 Direction 3'.1 was specified in [round_10_plan.md](round_10_plan.md) commit `48ee43d` as: *"Pre-test for derivability — can Op10 c=3 carrier preservation under Move 10's non-standard topology finding be rewritten as l=2 angular-node-count signature? If YES → (ε) has lattice-resolvable instantiation; if NO → (ε) requires continuum-scale framework."*

The gate-decision dialogue with Grant during Phase 1 execution surfaced multiple substrate-derived findings via Rule 14 + Rule 16:
- Mutual-inductance mechanism between K4 nodes is the substrate-native 3-axis stabilization
- (2,3) topology + 6-lobe internal structure
- Genesis-inherited cosmic chirality per doc 59 §5.4 + lattice-genesis chirality propagation
- Bipartite K4 RH/LH port pairing (k4_tlm.py:521-529 — research-tier diagnostic)
- Vol 1 Ch 8:49 (manuscript corpus) confirms K4 4-port symmetric junction has node-level Ax 4 no-op

Per the dialogue + auditor's review of path α v4 results, two converging concerns surfaced:

1. **Auditor catch (commit `2a684a4` review):** Path α v1-v4 use multi-cell extended-torus IC at N=32, R=10, r=R/φ²≈3.82 — that's bond-CLUSTER scale (~10×ℓ_node). Doc 79 v5.1 closure + doc 28 §3 explicitly establish corpus-canonical electron is bond-PAIR scale (single A-B + neighborhood, ~ℓ_node). The seed-axis question only matters at bond-cluster scale because there's an extended torus geometry to orient.

2. **Grant's challenge:** The multi-cell extended-torus IC framing itself is research-effort scaffolding, NOT corpus. It was chosen because we needed enough cells per winding period for Nyquist-resolution of the (2,3) spatial winding (~6-8 cells per winding period). That's a research-effort engineering choice driven by lattice resolution constraints, not a corpus prediction about electron spatial extent.

The two concerns converge on: **Phase 1 path α arc tested the wrong object class for corpus electron comparison.**

---

## §2 Direction 3'.1 gate-decision result

**Decision: YES on (ε) substrate-resolvability — but with revised understanding of what "lattice-resolvable" means.**

The substrate-derived mechanism for the corpus electron's 3-axis stabilization at a saturated bond-pair has three components (per Phase 1 dialogue):

1. **K4 4-port geometry (Ax 1):** at every K4 node, 4 transmission-line ports at tetrahedral angles (109.47°). Bare scatter+connect treats all 4 ports equivalently as a single permutation orbit (T_d-symmetric). Path α v4b confirmed this empirically — RH/LH chirality pairing per `k4_tlm.py:524` is a DIAGNOSTIC computation, NOT a coupling-strength asymmetry in dynamics.

2. **Mutual-inductance coupling between adjacent K4 LC-tank bonds:** the K4 scatter+connect dynamics IS literally per-port mutual inductance between adjacent LC tanks. Φ_link is L-state, V_inc/V_ref is C-state, the connect step is the L↔C coupling between adjacent bonds. At a saturated bond-pair, the saturated bond couples to its 3 lateral non-saturated neighbors via 3 mutual inductances. Per Move 11b empirical ρ(H_cos, Σ\|Φ_link\|²) = -0.990, this trading channel is empirically active.

3. **Genesis-inherited global chirality (research-tier per doc 59 §5.4):** the cosmic-scale RH/LH labeling is set at primordial seed event + propagated cell-by-cell via bond-coupling. Universe-wide single-domain. Manifests as helicity diagnostic h = (V_0+V_2)² − (V_1+V_3)² with bipartite A/B sublattice sign-flip. NOT a dynamic coupling-strength modifier; structural sign convention per Vol 1 Ch 8:49 K4 symmetry.

Substrate-native interpretation of corpus electron: a saturated A-B bond-pair with mutual-inductance coupling to 3 lateral neighbors, global-chirality-inherited helicity sign, internal (2,3) phase-space winding per doc 28 §5.1, all at scale ~ℓ_node.

This **IS lattice-resolvable** at engine resolution — but at bond-pair scale, not bond-cluster scale.

---

## §3 Empirical findings from Phase 1 path α arc — all at bond-CLUSTER scale

Path α v1 (commit `6d27e58` baseline), v2 (commit `8b80c85`), v3 (commit `6d27e58`/`baadc33`), v4 (commit `2a684a4`), v4b (commit `d4b0495`) all use:
- N=32 lattice with PML=4 (interior 24³)
- IC: multi-cell extended-torus seed at R=10 ℓ_node, r=R/φ²≈3.82 ℓ_node (Cartesian-z torus axis)
- A28+Cosserat self-terms enabled
- Move 5 saturated attractor at peak |ω|=0.3π, stable for 150+ P
- Sampling at top-K |V_inc[port_i]|² cells → bond-pairs embedded in the multi-cell saturated attractor

**Empirical findings (research-tier interpretation, all at bond-cluster scale):**

| Finding | Source | Interpretation |
|---|---|---|
| Mode III on R/r=φ² across 10 pre-registered tests | Doc 79 v5.1 | Bond-cluster R/r ≠ φ² in any sampled sector at engine resolution |
| ω-orbit aspect e2/e1 ≈ 1.25, planarity ~0.5 | v3, v4, v4b | Bond-cluster ω-trajectory is volumetric ellipsoid; ratio mean ~1.25 with 22-30% spread (n=2 per port) |
| 100% CCW chirality on (Φ_link, \|ω\|) at port-0 bonds | v3 v5.1 §7.6.4 | Port-0-specific chirality detection (sampling along seed's primary axis); not robust across all ports |
| Bare TLM C_4 symmetric (RH-mean ≈ LH-mean Δ = 1.5%) | v4 + v4b | Confirmed empirically; chirality pairing is DIAGNOSTIC not coupling-asymmetry |
| Aspect within-pair spreads 22-30% at n=2 | v4b | Bond-position-dependent variability, NOT structural RH-vs-LH asymmetry |

**These are all bond-cluster-scale findings.** The corpus electron's bond-pair-scale properties are NOT directly measured by these tests.

---

## §4 The scale mismatch (Rule 14 substrate-derives at the right object class)

| Object | Spatial scale | Tractable at engine N=32? | Tested in path α v1-v4(b)? |
|---|---|---|---|
| Corpus electron (bond-pair) | ~ℓ_node ≈ 10⁻¹³ m | Phase-space phasor: YES; Real-space spatial winding: NO (sub-Nyquist) | NO directly |
| Bond-cluster extended torus (research scaffold) | ~10×ℓ_node | YES | YES (path α v1-v4b) |
| Atomic shell envelope | ~10⁵×ℓ_node (Bohr radius) | NO at N=32 | NO |
| HOPF antenna macroscopic | ~10²⁵×ℓ_node | NO at N=32 | NO |

**The bond-cluster IC was implemented because:**
- Real-space (2,3) spatial winding requires 6-8 cells per winding period (Nyquist) → minimum R ≈ 6-10 cells
- That's bond-cluster scale, NOT bond-pair scale
- A57 sub-Nyquist topology seed concern (doc 74 §15.4) flagged this directly: "at corpus aspect R/r=φ², the loop fits at r ≤ 1.5 cells which is sub-Nyquist for c=3 winding read"
- Research-effort decision: test at the smallest tractable cluster scale, hope the dynamics extrapolate to bond-pair physics

Per Grant's challenge + auditor's catch: **this extrapolation isn't justified**. The bond-cluster object is a different physical thing than the corpus electron, even if they share topological signatures.

---

## §5 Doc 28 §5.1 phasor test is PHASE-SPACE — not constrained by real-space Nyquist

**Critical observation:** doc 28 §5.1 specifies the canonical electron test as:
> "Extract V_inc/V_ref phasor trajectory on a SINGLE A-B bond from existing TLM 96³ simulation. Plot in (Re, Im) phase space. Check if it traces a torus with R/r ≈ φ²."

This is a **phase-space measurement at a single bond-pair**, NOT a real-space spatial-winding measurement. The phasor trajectory in (V_inc[t], V_ref[t]) coordinates over time at one A-B bond doesn't require resolving spatial winding; it requires resolving temporal dynamics at the bond.

Path α v1 ran exactly this spec but on bond-pairs **embedded in the multi-cell extended attractor**. The bond-pairs sampled were single-cell, but the surrounding context was multi-cell.

**Per A57 sub-Nyquist concern, the multi-cell context may not be needed at all** for the phase-space measurement. A SINGLE saturated A-B bond IC, with no extended torus, should be sufficient for the doc 28 §5.1 test if the test is purely phase-space.

This is the **bond-pair-scale test that hasn't been run yet.**

---

## §6 Direction 3'.2 reframe: bond-pair-scale phase-space phasor test

**Proposed Direction 3'.2 work** (NOT Direction 3'.2 as originally specified in round_10_plan.md, which assumed bond-cluster IC):

### 6.1 Bond-pair-scale IC

Initialize a single saturated A-B bond at engine resolution. Operationally:
- Pick a center cell A and its tetrahedral neighbor B (e.g., A at (16, 16, 16), B at (17, 17, 17) via port 0)
- Set V_inc at A and B to peak amplitude (A²→A_c²) on port 0 (the bond direction)
- Set Φ_link at A's port 0 to corresponding L-state (90° quadrature with V_inc)
- Other ports / cells: zero or thermal floor
- Cosserat: ω at A and B in the plane perpendicular to bond axis (port 0 = (1,1,1)/√3)

This is bond-pair scale — single A-B saturated bond + small neighborhood. NO extended torus.

### 6.2 Phase-space phasor measurement

Run engine evolution at bond-pair scale IC. Measure:
- (V_inc[t], V_ref[t]) phasor trajectory at the A-B bond
- (Φ_link[t], ω[t]) trading channel per Move 11b empirical signature
- (V_inc[t], Φ_link[t]) LC tank quadrature per substrate-native LC-pair structure

Compute:
- 2D PCA on (V_inc, V_ref) phasor → ellipse R/r per doc 28 §5.1 spec
- Hilbert chirality on (Φ_link, |ω|) per v3 v5.1 finding
- (2,3) winding pattern detection in phase-space

### 6.3 Adjudication

**Mode I-corpus-electron-confirmed:** R/r = φ² ± 5% on phasor ellipse + chirality detected → corpus electron confirmed at bond-pair scale; Phase 1 path α v1-v4(b) findings re-contextualize as "bond-cluster scale extrapolation that doesn't directly test corpus prediction"

**Mode II-partial:** some corpus signatures match at bond-pair scale, others don't → identify which subset of signatures the corpus electron actually has

**Mode III:** R/r ≠ φ² even at bond-pair scale → falsifies the corpus prediction at the right object class

### 6.4 Cost

- Implementation: ~1-2 fresh sessions to build bond-pair IC + driver
- Run: ~5-7 min per IC variant
- Multiple IC variants worth testing (port 0, port 1, ..., different relative phases) — single Phase 1 follow-up arc

---

## §7 What this means for the broader Phase 1 + Round 10+ plan

### 7.1 Path α v1-v4(b) results stay valid AT bond-cluster scale

The empirical findings remain real:
- v3: ω-orbit aspect ~1.25 with 0.5 planarity at port-0-saturated bonds in multi-cell attractor
- v4: bare TLM C_4 symmetric (RH-mean ≈ LH-mean)
- v4b: aspect spread 22-30% at n=2 per chirality pair (bond-position-dependent variability)

These describe **what the engine produces at bond-cluster scale under (2,3) Cartesian-z seed IC**. They are NOT direct measurements of the corpus electron.

### 7.2 Direction 3'.1 gate-decision YES, but reframed

(ε) bound-state-vs-free-state interpretation IS lattice-resolvable, but the test must be at **bond-pair scale**, not bond-cluster. Path α v1-v4(b) tested bond-cluster, which is the wrong object class.

### 7.3 Direction 3'.2 specification updated

Instead of "derive (n, l, m_l) → K4 bond-pair coordinate map" at multi-cell scale, Direction 3'.2 work is now:
- Build bond-pair-scale IC (single saturated A-B bond, no extended torus)
- Run doc 28 §5.1 phase-space phasor test at bond-pair scale
- Compare to corpus prediction R/r = φ²
- Identify what bond-pair-scale corpus electron looks like empirically (separate from bond-cluster behavior)

### 7.4 Doc 79 v5.1 closure stands

The closure said: "10 pre-registered tests at engine-representable corpus GT, all Mode III on R/r=φ²." That's empirically correct AT bond-cluster scale. The closure shape "Mode III canonical + one structural partial positive" stays. What changes:
- Path α v3 v5.1 §7.6.4 100% CCW finding is port-0-specific (per v4/v4b) — Rule-12-style addendum to v5.1 already queued for auditor-lane
- Whether the path α v1-v4(b) Mode III results say anything about corpus electron at corpus scale (bond-pair) is now flagged as open question

### 7.5 Round 10+ plan amendments

[round_10_plan.md](round_10_plan.md) Direction 3'.2 description should be updated to specify bond-pair-scale IC. The current description references multi-cell extended-torus implicitly (inheriting from path α v1-v4 framing). Auditor-lane editorial work.

---

## §8 A43 v12 implementer-side instance flagged

During Phase 1 dialogue, I cited [VACUUM_ENGINE_MANUAL.md](VACUUM_ENGINE_MANUAL.md) line 1173 as "corpus explicitly states" for the K4-tetrahedral-symmetry claim.

**Catch:** VACUUM_ENGINE_MANUAL.md lives in `research/L3_electron_soliton/` — it's a research-tier doc summarizing our work, NOT canonical corpus (which is `manuscript/` only).

**Verification:** the underlying claim ("K4 4-port junction is symmetric, no preferred direction at node") IS verified at canonical corpus per [`manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex` line 49](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex):
> "K4-TLM exhausted (node-level Axiom 4 no-op for 4-port symmetric junctions per 32_ section 10.2)"

So the underlying claim was correct, but the citation was wrong (research-tier presented as corpus-tier). A43 v2 lane-symmetric implementer-side instance, cumulative now 12 worked examples across the session arc.

**Correction lands in this commit's predecessor commit (`d4b0495` v4b commit message).** Auditor-lane queue addition for COLLABORATION_NOTES Rule 8 A43 v2 worked-examples body.

---

## §9 Open questions for Direction 3'.2 implementation

Surfaced for next Phase 1 fresh session or Grant's adjudication:

**Q1: bond-pair IC operational specification.** What exactly does a bond-pair-scale (2,3) IC look like at engine resolution? Possibilities:
- (a) Single saturated A-B bond (V_inc = peak amplitude at A and B port 0; zero elsewhere) + Cosserat ω in perpendicular plane
- (b) Saturated bond + thermal floor surrounding (gives the "neighborhood" implicit in "bond-pair + neighborhood")
- (c) Pair production-style IC: two seed bonds at opposite chirality, allow them to self-organize

**Q2: phase-space (2,3) winding detection method.** Path α v1 used PCA on (V_inc, V_ref) trajectory at single bond. For bond-pair-scale IC, is PCA the right method, or do we need explicit (2,3) torus-knot fitting?

**Q3: relating bond-pair findings to multi-cell empirical observations.** If bond-pair-scale tests give different R/r values than bond-cluster tests, what's the relationship? Are bond-cluster aspects "averaged" bond-pair aspects, or are they fundamentally different objects?

**Q4: chirality detection at bond-pair scale.** Path α v3 v5.1 100% CCW was port-0-specific in multi-cell IC. At bond-pair scale (single saturated bond, no extended geometry), does chirality detection look different?

**Q5: Rule 16 fundamental physics check.** What does Grant's plumber-physical intuition say about a bond-pair-scale electron? Standing wave between two saturated walls (Γ→-1 at both A and B nodes)? LC oscillation between A's bond port and B's bond port? Multi-port junction with one saturated port + 3 lateral coupling channels?

---

## §10 References

- [round_10_plan.md](round_10_plan.md) — Round 10+ plan (Phase 1 Direction 3'.1)
- [`79_l3_branch_closure_synthesis.md`](79_l3_branch_closure_synthesis.md) v5.1 — L3 closure (corpus-canonical bond-pair framing)
- [`81_l3_followup_questions.md`](81_l3_followup_questions.md) — post-closure follow-up
- [`28_two_node_electron_synthesis.md`](28_two_node_electron_synthesis.md) §3-§5 — corpus-canonical bond-pair + phase-space (2,3) framing
- [`74_r7_k4tlm_lctank_run_result.md`](74_r7_k4tlm_lctank_run_result.md) §15.4 — A57 sub-Nyquist topology seed concern
- [`75_cosserat_energy_conservation_violation.md`](75_cosserat_energy_conservation_violation.md) §6.2 — Op14 trading channel empirical signature
- [`manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex`](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex) line 49 — Vol 1 Ch 8 K4-TLM 4-port symmetric junction (manuscript corpus)
- [`manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex`](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex) line 402 — Vol 1 Ch 3 electron rotation axis n̂ (manuscript corpus)
- [`manuscript/ave-kb/common/operators.md`](../../manuscript/ave-kb/common/operators.md) — Op1-Op22 catalog (commit `35cc818`)
- Path α drivers + results: r9_path_alpha_bond_pair_phasor.py + v2/v3 + r10_path_alpha_v4_port_mixed.py + v4b
- COLLABORATION_NOTES Rule 9 v2 (right-kind-of-question), Rule 14 (substrate-derives), Rule 16 (ask-Grant-fundamental-physics), A43 v2 (anyone-must-grep — v12 instance flagged in §8), A48 (frozen-extraction-scope)
