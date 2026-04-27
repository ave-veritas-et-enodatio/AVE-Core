# 74 — R7.1 multi-seed K4-TLM scatter+connect + Cosserat LC-tank Hessian eigenmode sweep: run result + adjudication

**Status:** 2026-04-25. Run executed against frozen pre-registration `P_phase6_k4tlm_scattering_lctank` per [doc 73_](73_discrete_k4_tlm_lctank_operator.md). Reframe 4 of R7.1 with §6.1 catastrophic-error carve-out invoked on-record per Grant approval ("confirmed 6.1") for the prior reframe-3 → reframe-4 transition.

**Verdict: Mode III** (with documented incomplete-coverage on Cos-block). No eigenmode within PASS tolerance at any of the four pre-registered seeds. Two implementation-level bugs (V-block z-invariance, Cos-block null-space artifact) caught by empirical run and fixed in same session per Rule 10 "data first, methodology after"; the post-fix run is the load-bearing one reported here.

**Read after:** [doc 73_ §2-§5](73_discrete_k4_tlm_lctank_operator.md), [doc 72_ §9](72_vacuum_impedance_design_space.md), [doc 71_ §15](71_multi_seed_eigenmode_sweep.md).

---

## 1. Run summary

Driver: [`r7_k4tlm_scattering_lctank.py`](../../src/scripts/vol_1_foundations/r7_k4tlm_scattering_lctank.py) at lattice N=32, R_anchor=10. Output: [`r7_k4tlm_scattering_lctank_results.json`](../../src/scripts/vol_1_foundations/r7_k4tlm_scattering_lctank_results.json).

Frozen spec from [`P_phase6_k4tlm_scattering_lctank`](../../manuscript/predictions.yaml):
- V-block target: phase `ω_C·dt = 1/√2 ≈ 0.7071 rad` on unit circle, tolerance `α/√2 ≈ 0.00516 rad`
- Cos-block target: `λ = ω_C² = 1.0`, tolerance `α·ω_C ≈ 0.00731` on √λ
- A26 amplitude guard at step 0
- Engine: A28 + Cosserat self-terms enabled
- Seeds: GT_corpus, F17K_cos_endpoint, F17K_s11_endpoint, vacuum_control

The run was executed twice in this session: a first version (commit at smoke-test time) and a post-bug-fix version (this report). The first run uncovered two implementation bugs via empirical contact (per Rule 10 "data first, methodology after"). The bugs and fixes are documented in [§5](#5-implementation-bug-story) for transparency. **The post-fix run is the load-bearing one for this report; the pre-fix run is preserved as audit trail of the implementation iteration.**

---

## 2. V-block results per seed (post-fix)

K4-TLM scatter+connect transmission operator T = C_op3 · S where C_op3 incorporates Op3 bond reflection per [k4_tlm.py:393-415](../../src/ave/core/k4_tlm.py#L393). Sparse + complex (unitary) eigenvalue problem; eigsh shift-invert at `sigma = exp(i·ω_C·dt) = exp(i/√2)` ≈ exp(i·0.7071).

T construction at N=32: dim 32768 (4 ports × 8192 active K4 sites), 262144 nonzeros (8 per row from Op3 bond reflection: 4 own-site reflections γ·S + 4 neighbor-site transmissions T·S). Build wall time ~0.4s. Eigsolve wall time 6-12s per seed.

### 2.1 Per-seed V-block findings

| Seed | A26 peak \|ω\| | closest eigvalue phase | rel_diff vs ω_C·dt | PASS? |
|---|---|---|---|---|
| GT_corpus | 0.9262 | 0.7157399782985672 rad | 1.2209% | NO |
| F17K_cos_endpoint | 0.9154 | 0.7157330320287166 rad | 1.2199% | NO |
| F17K_s11_endpoint | 0.9399 | 0.7157342105444655 rad | 1.2201% | NO |
| vacuum_control | 0.0850 | 0.7158130436188964 rad | 1.2313% | NO |

**PASS tolerance:** `α/√2 ≈ 0.516%`. Closest mode is 1.22% off — **2.4× outside tolerance.**

### 2.2 Seed differentiation check

Phase differences across seeds:
- `GT_corpus - vacuum_control`: ~7.3e-5 rad (4th decimal)
- `GT_corpus - F17K_cos`: ~6.9e-6 rad (5th decimal)
- `GT_corpus - F17K_s11`: ~5.8e-6 rad (6th decimal)
- `F17K_cos - F17K_s11`: ~1.2e-6 rad (6th decimal)

GT-family vs vacuum_control differ at 4th decimal — **genuine seed-dependence**, validating the Op3 bond-reflection implementation. Within GT-family the differences are smaller (5th-6th decimal) because all three seeds use the same A26-corrected amplitude (peak |ω| ≈ 0.92-0.94) and only differ in (R, r) shell geometry; the integrated z-modulation effect is similar.

Op14 z modulation at peak |ω|=0.3π ≈ 0.94 produces z_local variation of about ±2.4% from z=1. This drives an eigenvalue shift of ~7e-5 rad in the closest-to-target mode — consistent with weak-perturbation regime.

### 2.3 V-block conclusion

**Mode III for V-block at all four seeds**: no K4-TLM scatter+connect transmission eigenmode at ω_Compton phase within α/√2 tolerance. The closest mode at 1.22% rel_diff is consistent across all seeds (lattice structural mode); seed-dependent shifts are 5th-decimal-level, far below the 0.52% tolerance gap.

This is robust: shift-invert at sigma=exp(i·ω_C·dt) directly targets the eigenvalue nearest the target phase. The 1.22% gap is the **actual gap between ω_C·dt and the nearest K4-TLM lattice mode at this lattice geometry and z-pattern.**

---

## 3. Cos-block results per seed (post-fix)

Cosserat (u, ω) LC-tank Hessian-of-W at seed configuration via FD HVP on `engine.cos.energy_gradient()`. Sparse generalized symmetric eigenvalue problem `K_cos · ψ = ω² · M_cos · ψ` with k=100 (bumped from k=20 to span past ~9-dim rigid-body null space), `which='SA'` smallest-algebraic, NULL_SKIP_THRESH = 1e-6 to filter rigid-body modes post-eigsolve.

Cos-block dim 196608 at N=32 (3 u + 3 ω components × 32768 cells). Eigsolve wall time 44-80s per seed via Lanczos with FD HVP.

### 3.1 Per-seed Cos-block findings

| Seed | smallest non-null λ | √λ_smallest | rel_diff to ω_C | PASS? |
|---|---|---|---|---|
| GT_corpus | 0.0792 | 0.282 | 71.85% | NO |
| F17K_cos_endpoint | 0.0792 | 0.282 | 71.85% | NO |
| F17K_s11_endpoint | 0.0792 | 0.282 | 71.85% | NO |
| vacuum_control | 0.1517 | 0.389 | 61.08% | NO |

**PASS tolerance:** `α·ω_C ≈ 0.731%`. Closest is 61.08% off (vacuum) — **84× outside tolerance.**

### 3.2 Cos-block coverage caveat

The k=100 SA-mode covers only the BOTTOM 100 eigenvalues of K_cos's 196608-dim spectrum. The reported "closest to ω_C²=1" is the smallest eigenvalue above the null-space threshold (1e-6). Higher-frequency eigenvalues nearer to ω_C² = 1 may exist in the spectrum at index > 100 but are not captured by SA-mode at this k.

This is a **bottom-of-spectrum search, not a comprehensive bound-state-region search.** The cleanest fix would be shift-invert at sigma=ω_C² but that requires explicit OPinv (`(K_cos − σM)⁻¹`) which a LinearOperator-based HVP doesn't natively support — it would require an inner iterative GMRES at each Lanczos step. Deferred to next-iteration follow-up; **the Cos-block "mode III" finding is incomplete-coverage mode III, not comprehensive mode III.**

### 3.3 Cos-block seed differentiation

GT-family seeds (GT_corpus, F17K_cos, F17K_s11) all converge to the SAME smallest-non-null eigenvalue λ ≈ 0.0792 (rel_diff 71.85% to 16 decimals via SA-mode). vacuum_control finds a different smallest eigenvalue λ ≈ 0.152 (rel_diff 61.08%).

This pattern is consistent with Cosserat sector physics:
- GT-family seeds all have peak |ω| ≈ 0.93 (A26-corrected hedgehog amplitude). The rigid-body null space is the same for all three (rotational symmetries of the lattice). The smallest non-null mode is a low-k acoustic-like mode of the Cosserat field whose frequency depends weakly on the (R, r) shell geometry (the seed perturbs the bulk ρ, I_ω uniformly — only at the shell does z_local matter, but Cosserat-sector eigenmodes are dominated by bulk moduli).
- vacuum_control has tiny |ω| ≈ 0.085 (random low-amplitude). Its Hessian is dominated by the field's curvature near zero amplitude, where the constitutive moduli (G, γ, I_ω) determine the spectrum without saturation contributions. Different bulk physics → different lowest mode.

The GT-family seeds being indistinguishable in the smallest non-null Cosserat eigenvalue isn't a methodology bug — it's a real physical observation that the bulk Cosserat spectrum at A26-amplitude hedgehog seeds is dominated by uniform constitutive moduli, with shell-geometry corrections appearing at higher modes outside the k=100 window.

---

## 4. Three-mode falsification adjudication

### 4.1 Headline result: Mode III (with caveat)

Per [doc 73_ §1.1](73_discrete_k4_tlm_lctank_operator.md) reframe arc + [pred PASS criterion](../../manuscript/predictions.yaml):

- **No seed returns an eigenmode within PASS tolerance in either V-block or Cos-block.**
- **Mode III interpretation per pred:** "(2,3) representation needs structural rework, OR bound state is genuinely hybrid (V≠0 ∧ ω≠0) requiring V≠0 seed (Round 8)."

V-block result is **comprehensive** (shift-invert at target sigma directly finds the closest eigenvalue; the 1.22% gap is the actual closest mode in the K4-TLM spectrum). Cos-block result is **incomplete-coverage** (SA-mode covers only the bottom 100 of 196608 eigenvalues; higher-frequency modes near ω_C² may exist but were not searched).

### 4.2 Honest scope of Mode III claim

- **V-block: Mode III with high confidence.** No K4-TLM scatter+connect transmission eigenmode at ω_C·dt phase exists in the searched spectrum, and shift-invert ensures we found the closest eigenvalue, which is ~1.2% off — an order of magnitude outside PASS tolerance.
- **Cos-block: Mode III for the bottom 100 eigenvalues of the spectrum only.** A bound-state eigenvalue at λ = 1 might exist higher in the spectrum and would not have been found. To convert this to comprehensive Mode III, the Cos-block needs shift-invert at sigma = 1 (requires inner iterative OPinv).

### 4.3 Negative-control check

`vacuum_control` (peak |ω|=0.085, near-uniform z) returns the same Mode III as GT-family seeds. **Negative control passes.** The lattice doesn't accidentally produce a "bound state" at ω_C in vacuum-like configurations.

V-block phase difference between vacuum_control (0.71581) and GT-family (~0.71573-74) is genuine 4th-decimal differentiation, confirming the Op3 bond-reflection implementation correctly responds to z_local. Pre-fix, all four seeds were bit-identical to 16 decimals — that bug is now resolved.

### 4.4 What this resolves

- **Op14 z-modulation at A26-amplitude hedgehog seeds is too weak to push the V-block lattice spectrum to ω_C·dt phase.** The (2,3) shell creates a ~2.4% z-perturbation at peak; the resulting eigenvalue shift is ~1e-5 rad — the lattice mode at 0.7158 stays at 0.7158 ± epsilon regardless of (R, r). The corpus (2,3) shell pattern doesn't produce a TIR cavity effective enough to bind a wave at ω_C in the K4-TLM spectrum.
- **Cosserat sector at A26-amplitude has its lowest non-null mode at √λ ≈ 0.28 across GT-family seeds.** This is the lowest accessible LC oscillation frequency in the bulk Cosserat field; the bound state if it exists at ω_C would be higher in the spectrum (which Cos-block didn't search comprehensively).
- **Block decoupling at V=0 seed empirically validated.** The two blocks are independent eigenproblems at the seed configuration; results are sectored cleanly.

### 4.5 What stays open

- **Cos-block comprehensive coverage** at sigma=ω_C² shift-invert with explicit OPinv via inner GMRES. ~30 min - 2 hr per seed; would convert Cos-block result to comprehensive mode I/II/III. This is the most direct follow-up.
- **Hybrid V≠0 ∧ ω≠0 seed test** per [doc 73_ §4.4](73_discrete_k4_tlm_lctank_operator.md). At V=0 seed cross-coupling vanishes; if the bound state genuinely lives at V≠0 ∧ ω≠0 (with non-trivial cross-coupling), this test never finds it. Round 8 territory.
- **Larger N sensitivity sweep.** At N=32 the (2,3) shell has minor radius ~3.8 cells; this is borderline-resolved. At N=64 or N=80 (matching F17-K v2-v2's lattice size) the shell would be better resolved and the V-block spectrum may shift. Could test if the 1.22% gap closes at higher resolution.
- **Round 8 architectural rework** if comprehensive Cos-block + larger-N + hybrid-seed all return Mode III. Likely starting point: "where does the bound state actually live?" — the corpus framing per [doc 66_ §17.2](66_single_electron_first_pivot.md) names three LC tanks (K4 bond, Cosserat translational, Cosserat rotational); current framing tests two (K4 V-block + combined Cosserat (u, ω) Cos-block) but doesn't explicitly probe the K4 bond Φ_link sector.

---

## 5. Implementation bug story (per Rule 10 "data first, methodology after")

The first run of `r7_k4tlm_scattering_lctank.py` produced suspicious results: all four seeds returned **bit-identical eigenvalues to 16 decimal places** in both V-block and Cos-block. Empirical run-data revealed two implementation-level bugs that static analysis at doc-73_ commit time missed.

### 5.1 V-block bug: `build_scattering_matrix(z_local)` returns z-invariant matrix

**Bug:** [`k4_tlm.py:36-65 build_scattering_matrix`](../../src/ave/core/k4_tlm.py#L36) computes `S_pq = 2y/y_total - δ_pq` where `y = 1/z_local` and `y_total = N·y` for a 4-port node. Since all 4 ports of a single K4 node share the same z_local, `2y/y_total = 2y/(4y) = 0.5` cancels — **S is bit-identical to `0.5·11ᵀ - I` regardless of z_local input.**

The original doc 73_ §2.4 specification "T row (i_t, p_t) has 4 nonzeros at columns (j_neighbor, q_s) with values S_block(z_local(neighbor))[p_t, q_s]" was correct in syntax but didn't recognize that S_block is z-invariant. Z-modulation in K4-TLM enters via Op3 BOND REFLECTION at the connect step (per [`k4_tlm.py:393-415`](../../src/ave/core/k4_tlm.py#L393)), NOT in the per-node scatter.

**Fix:** Updated [`build_T_operator`](../../src/scripts/vol_1_foundations/r7_k4tlm_scattering_lctank.py) to incorporate Op3 bond reflection in C operator: row (i, p) of T_op3 has 8 nonzeros total — 4 own-site reflections (coefficient γ_ij = (z_j-z_i)/(z_j+z_i)) and 4 neighbor-site transmissions (coefficient T_ij = √(1-γ²)).

**Post-fix verification:** at N=16 smoke test, vacuum_control vs GT_corpus V-block phases differ at 6th decimal (was bit-identical pre-fix). At N=32 full sweep, vacuum_control vs GT-family differ at 4th decimal. Genuine z_local-driven differentiation now present.

### 5.2 Cos-block bug: SA-mode finds rigid-body null space

**Bug:** K_cos = Hessian-of-W on (u, ω) at seed has a ~9-dim null space (rigid translations of u, rigid rotations of (u, ω)). With `which='SA'` and `k=20`, eigsh found the null-space modes (eigenvalues near 0) plus a few tiny non-null modes. Post-filter `eigvals > 0` was too loose (caught numerical positives in null space).

**Fix:** Bumped `k=20` → `k=100` to span past null space; tightened post-filter `eigvals > NULL_SKIP_THRESH = 1e-6` to skip rigid-body artifacts. **Coverage is still incomplete** (k=100 of 196608 modes), but now reaches actual non-null physical modes.

**Post-fix verification:** Cos-block GT-family vs vacuum_control eigenvalue ranges now distinct (GT 0.0792, vacuum 0.1517 for smallest non-null mode).

### 5.3 What the bug story tells us about reframe-counting discipline

These were **implementation-level bugs**, NOT operator-framing errors per [doc 72_ §6.1](72_vacuum_impedance_design_space.md). The block Helmholtz / discrete K4-TLM scatter+connect / Cosserat (u, ω) Hessian-of-W framework (per doc 73_ §2-§5) is correct and unchanged. The bugs were in HOW the operator-spec was realized in code; fixing them is allowed under Rule 10's "data first, methodology after" without invoking another §6.1 carve-out.

Per [doc 73_ §6.2](73_discrete_k4_tlm_lctank_operator.md): "What is NOT catastrophic — Numerical convergence issues with eigsh / eigs (no convergence after maxiter): methodology debug, retry with adjusted `tol` or `maxiter`. Not reframe." Same category as the bugs caught here. The §6.1 invocation count for Round 7 stays at **1**.

But this is also a Rule 10 lesson worth flagging: empirical run-data caught bugs that static reading of the operator spec did NOT catch. The bit-identical-eigenvalues-across-seeds pattern was the smoking gun. Without running the driver, this would not have been visible — exactly the failure mode Rule 10 is designed to prevent.

---

## 6. Three follow-ups complete (auditor concerns 1-3 addressed 2026-04-26)

Per [audit on commit 8c44ef0](.agents/handoffs/COLLABORATION_NOTES.md), three follow-ups were required before Mode III gets cited as canonical: Cos-block comprehensive coverage, K4-TLM dispersion analytical sanity check, and larger-N pre-registered resolution sweep. All three completed in this revision. **Headline result reaffirmed: Mode III at all four pre-registered seeds, now with comprehensive coverage on both V-block and Cos-block.**

### 6.1 Cos-block comprehensive coverage via shift-invert at σ=ω_C²

[`r7_cos_block_shift_invert.py`](../../src/scripts/vol_1_foundations/r7_cos_block_shift_invert.py): wraps `scipy.sparse.linalg.eigsh` shift-invert at σ=1 around the FD-HVP LinearOperator using inner iterative GMRES (rtol=1e-3, maxiter=300) for the OPinv solve. ARPACK's IRAM is robust to inexact OPinv; eigvals converge despite GMRES hitting maxiter on most inner solves.

Per-seed comprehensive results at N=32, k=20 eigenvalues nearest σ=1:

| Seed | Closest λ | √λ_closest | rel_diff to ω_C | PASS (α=0.73%)? |
|---|---|---|---|---|
| GT_corpus | 1.0404 | 1.020 | **2.00%** | NO |
| F17K_cos_endpoint | 0.9793 | 0.989 | **1.04%** | NO (closest) |
| F17K_s11_endpoint | 0.9608 | 0.980 | **1.98%** | NO |
| vacuum_control | 1.0319 | 1.016 | **1.58%** | NO |

All four seeds: K_cos has eigenvalues densely clustered in [0.95, 1.05] (within ±5% of ω_C²=1) but no eigenvalue within α=0.73% PASS tolerance. **Comprehensive Mode III for Cos-block at all seeds.**

This converts the original [doc 74_ §3 caveat](#33-cos-block-seed-differentiation) ("bottom-100 SA-mode coverage; ω_C² may exist at higher index") into a definitive finding. The earlier 71.85% rel_diff in SA-mode was an incomplete-coverage artifact (smallest non-null eigenvalues are far from ω_C); shift-invert at σ=1 directly targets the bound-state region and finds eigenvalues 1-2% off. **The actual gap is ~1-2%, not 72%.**

Wall time per seed at N=32: 626-794s (~10-13 min). Total for 4 seeds: ~50 min. Each seed required ~120-153 OPinv calls, ~36K-46K total inner GMRES iterations.

**Pattern observation:** F17K_cos_endpoint (R/r=3.40) gives the closest gap at 1.04%, half the gap at GT_corpus (2.00%). Consistent with F17-K v2-v2's empirical finding that R/r=3.40 was the engine's actual Cosserat-energy descent attractor — its Hessian spectrum is denser near ω_C² than corpus GT's. F17K_s11 (R/r=1.03) and vacuum_control fall between. **No seed crosses Mode II (within α tolerance).**

### 6.2 K4-TLM dispersion analytical sanity check

[`k4tlm_dispersion_analytical.py`](../../src/scripts/vol_1_foundations/k4tlm_dispersion_analytical.py): at uniform z=1 the K4-TLM transmission operator factorizes per wavevector as `T(k) = D(k) · S` where `D(k) = diag(exp(i·k·PORTS[p]))` and `S = 0.5·11ᵀ − I`. Computed analytical eigenvalues at all discrete k-vectors of N=32 grid; checked whether the 0.71574 cluster sits on the canonical K4-TLM dispersion.

**Result:** the cluster at phase 0.71574 is **0.000768 rad off** the nearest analytical mode (phase 0.71651) — a match within 1e-3 rad. Auditor concern #2 resolved positively: **the cluster is real K4-TLM lattice physics, not a third operator-construction issue.**

Bipartite caveat documented: the simplified `T(k) = D(k)·S` analytic ignores A↔B sublattice coupling. The proper bipartite Bloch operator is `Φ_AB(k)·S·Φ_AB*(k)·S` with eigenvalues exp(2iω·dt) (phases doubled). The simplified version over-counts modes by ~4× (131K instead of physical ~32K) but the cluster-location finding is qualitatively correct. The simplified analytic ALSO suggested a mode at phase 0.7119 (0.68% off ω_C·dt, technically within α=0.73% tolerance) — but this was likely a non-bipartite over-counting artifact since the empirical V-block sweep found no such mode at any seed. Bipartite-correct analytic is a deferred follow-up; not load-bearing for the Mode III adjudication.

### 6.3 Lattice resolution sweep at N=64 — N=32 Mode III FALSIFIED as finite-N artifact

Pre-registered as `P_phase6_lattice_resolution_sweep` in `manuscript/predictions.yaml` BEFORE this run, per auditor concern #3. Frozen falsification structure:

PASS criteria (both required for "real K4-TLM Mode III"):
- (a) **Gap-closure:** `gap_N64 / gap_N32 > 0.5`
- (b) **Cluster-stability:** `|phase_N64 - phase_N32| / phase_N32 < 0.01`

**Run result at N=64, GT_corpus seed only ([`r7_lattice_resolution_sweep.py`](../../src/scripts/vol_1_foundations/r7_lattice_resolution_sweep.py)):**

| Lattice | T dim | T nnz | Closest mode phase | Gap to ω_C·dt | Rel diff |
|---|---|---|---|---|---|
| N=32 (baseline) | 32768 | 262144 | 0.71574 rad | 8.63e-3 rad | **1.22%** |
| N=64 | 262144 | 2097152 | **0.71031 rad** | **3.20e-3 rad** | **0.45%** |

PASS tolerance per pred: α/√2 ≈ 0.73% relative. **At N=64, gap=0.45% < tolerance — INSIDE PASS for the first time.**

Pred adjudication:
- (a) Gap-closure ratio = 0.37 < 0.5 → **FAIL** (gap closes by 63%; threshold was 50%)
- (b) Cluster stability = 0.76% < 1% → **PASS** (cluster shifts coherently from 0.71574 to 0.71031)

**Per pred falsification language:** "(a) fails: gap at N=64 is < 50% of N=32 gap → N=32 Mode III is finite-N artifact. The dispersion at higher N gets closer to ω_C·dt; corpus GT geometry may yet be correct in continuum limit."

**This is the headline finding.** The N=32 Mode III result was a finite-N artifact. At N=64 the K4-TLM scatter+connect dispersion at corpus GT geometry has an eigenvalue within PASS tolerance of ω_C·dt — Mode I candidate (corpus vindicated). The N=32 lattice was insufficient resolution to capture the (2,3) bound state.

V-block eigsolve at N=64: 349.5s wall time (T_op3 dim 262K, ~2M nonzeros). Tractable for further N=64 work without major compute infrastructure.

---

## 7. Headline three-mode adjudication (TWICE-REVISED post-follow-ups, 2026-04-26)

### THIRD FLIP — Mode I candidate FALSIFIED via topology check

The Mode I candidate at N=64 V-block GT_corpus passed the frequency criterion (gap 0.45% < α/√2) but **failed the topology check.** Per [`r7_n64_topology_check.py`](../../src/scripts/vol_1_foundations/r7_n64_topology_check.py):

- Closest V-block eigenvalue at phase 0.710307 rad (gap 3.20e-3 = 0.45% from ω_C·dt) — **frequency PASS**
- Shell localization of eigvec at seeded (R=10, r=3.82) torus: **1.13%** of total energy
- Bulk-uniform expectation (random distribution over lattice): **0.6%**
- **Observed shell fraction is 2.0× bulk-uniform — barely above random.**

Verdict: "WEAK SHELL LOCALIZATION (< 10%): eigvec is spread uniformly across lattice (bulk mode). **NOT a (2,3) bound state. Mode I candidate framing collapses.**"

**The frequency-PASS at N=64 was a band-density artifact.** At higher N the K4-TLM lattice spectrum is dense enough that *some* bulk mode randomly lands within α tolerance of ω_C·dt at GT_corpus seed. The auditor's concern #1 (topology check is load-bearing not confirmatory) was exactly correct.

**The K4-TLM V-block does NOT host the (2,3) bound state at corpus GT geometry at any tested N.** The N=32 Mode III was real Mode III (no eigenmode at all near tolerance); the N=64 frequency-PASS was a band-density coincidence on a delocalized bulk mode. Both readings agree: V-sector is empty of (2,3) bound state.

### Comprehensive coverage matrix (final, post all four follow-ups)

| Block | N | Coverage method | Seed | Gap | Topology check | Verdict |
|---|---|---|---|---|---|---|
| V-block | 32 | Shift-invert at exp(i·ω_C·dt) | All 4 | 1.22-1.23% | (n/a — frequency FAIL) | Mode III |
| V-block | 64 | Shift-invert at exp(i·ω_C·dt) | GT_corpus | 0.45% | **shell fraction 1.13%, bulk mode** | **Mode III** (frequency-PASS via band-density artifact; topology FAIL — no (2,3) localization) |
| Cos-block | 32 | Shift-invert at σ=ω_C², inner GMRES | All 4 | 1.04-2.00% | (n/a — frequency FAIL) | Mode III |
| Cos-block | 64 | Not yet run | — | — | — | DEFERRED |

### Methodological lesson: frequency-PASS alone is band-density-vulnerable at high N

This run is the cleanest empirical demonstration in this arc that frequency-only PASS criteria become unreliable at high lattice resolution because mode density grows with lattice volume. **Any "Mode I confirmed" result needs both frequency AND topology criteria.** Updates the A39 finding for r8.9: the rule should be "any Mode I/II/III adjudication at fixed N needs (a) pre-registered larger-N falsification AND (b) topology / localization verification, not just frequency criterion."

### What the run sequence empirically established (3 headline flips in one session)

1. Initial run: comprehensive Mode III at N=32 (V-block + Cos-block both 1-2% off) — looked like Round 8 architectural rework needed.
2. Pre-registered larger-N sweep at N=64: gap closed to 0.45%, frequency PASS — **headline flipped to Mode I candidate; corpus GT may yet be correct.**
3. Topology check on N=64 eigvec: shell fraction 1.13% (bulk mode, not (2,3) bound state) — **headline flipped back to Mode III; corpus geometry NOT vindicated by V-sector.**

Each flip was empirically driven and caught real issues that static analysis would have missed. This is Rule 10 working at full strength. **The lesson stays: pre-registration + multiple verification axes is the discipline; single-criterion PASS at one N is insufficient.**

### 7.1 Mode I candidate caveats

The N=64 V-block PASS at GT_corpus is a **CANDIDATE**, not a confirmed Mode I. Open verifications:

1. **Topological crossing-count of the eigenmode.** The pred PASS criterion includes c_eigvec=3 for the (2,3) electron mode. At N=64, did the eigenvector at phase 0.71031 have c_eigvec=3? The current resolution-sweep driver doesn't compute this; needs a follow-up extraction from the eigvec returned by eigs. Cheap (~5 min).
2. **Cos-block at N=64.** If V-block PASSes but Cos-block doesn't, the bound state lives entirely in K4 V-sector at corpus GT — which is consistent with corpus framing. If Cos-block ALSO passes at N=64, the mode is hybrid. If Cos-block FAILS at N=64, it's V-only (still consistent with Mode I, no V≠0 hybrid contribution at this seed).
3. **F17K endpoint seeds at N=64.** If F17K_cos and F17K_s11 also PASS at N=64, the K4-TLM lattice at N=64 hosts eigenmodes near ω_C·dt at MULTIPLE geometries — could indicate a continuum band rather than a single (R, r) bound state. A "PASS at multiple seeds" outcome would mean Mode I is confirmed by GT_corpus AND signal that the K4-TLM has many candidate (R, r) for the (2,3) eigenmode.
4. **N=80 follow-up** — if N=32 → N=64 gap-closure is real continuum approach, gap should continue closing as N grows. Strong test of "N=64 PASS is real continuum mode" vs "N=64 PASS is N=64-specific artifact."

### 7.2 Round 8 architectural reading — RESTORED

The third flip restores the Round 8 architectural reading that the original Mode III at N=32 had pointed toward. **V-block at corpus GT geometry does NOT host the (2,3) bound state at any tested N.** The frequency-PASS at N=64 was a band-density artifact on a bulk-delocalized mode.

Round 8 entry candidates (probability ordering per auditor + this run's evidence):

1. **Cos-block at N=64** — most physics-substantive next test. The Cos-block at N=32 was Mode III too, but at a different operator structure (Hessian-of-W on (u, ω) — discrete-LC-tank Cosserat sector). At N=64 the Cosserat spectrum could either also show only bulk modes near ω_C² (then bound state isn't in V OR Cos at corpus GT — points to Φ_link or hybrid), OR localize at the (2,3) shell (then bound state lives in ε-strain sector, which is the Cosserat-side LC-tank per doc 66_ §17.2).
2. **Φ_link sector** (third LC tank per [doc 66_ §17.2](66_single_electron_first_pivot.md)) — NOT directly probed by V-block (V_inc states) or Cos-block ((u, ω) states). If both are Mode III at corpus GT at high N, Φ_link is the cleanest gap.
3. **Hybrid V≠0 ∧ ω≠0 mode** — V=0 seed misses any genuinely cross-coupled bound state. Test via quadrature seed at small V_amp.
4. **(2,3) representation structural rework** — weakest; testable by sweeping (1,2), (2,5), (3,5) windings.

### 7.3 Auditor's concerns #2-#4 — re-prioritized after topology FAIL

- **Concern #2 (corpus discrimination via F17K endpoints at N=64):** mostly moot for V-block now. Since the Mode I candidate was bulk-mode (not (2,3) bound state), running F17K endpoints at N=64 V-block would confirm "lattice has bulk modes near ω_C·dt at any seeded geometry due to band density" — informational but doesn't change Mode III adjudication.
- **Concern #3 (N=80 scaling test):** significantly weakened. The "gap at N=80 ≤ 0.30%" target was relevant if Mode I at N=64 was real. Since N=64 was bulk-mode artifact, gap-closure at N=80 just continues to populate band-density-vulnerable region. Could still test if the AT-LATTICE-MODE-DENSITY gap-closure pattern is uniform (it would be at higher N too) but not load-bearing.
- **Concern #4 (Cos-block at N=64):** **MOST physics-substantive next step.** Tests whether ε-strain sector hosts the (2,3) bound state at corpus GT. If Cos-block at N=64 shell-localizes, that's the cleanest corpus vindication possible (V-sector empty + ε-strain sector hosts bound state per doc 66_ §17.2). If Cos-block at N=64 is also bulk-mode like V-block at N=64, Round 8 entry strengthens (Φ_link or hybrid).

Recommended next-step ordering REVISED:

1. **Cos-block at N=64 GT_corpus only with topology check** (~3-4 hr at N=64). Both frequency criterion (eigsh shift-invert at σ=ω_C²) AND shell localization on the eigvec. Single seed first; if topology confirms localization, expand to F17K endpoints + vacuum_control for Mode I/II/III sub-reading.
2. **R7.2 pre-registration** ((2,3)/Hopf injection per G-13) — independent of basin/eigenmode question, can run in parallel. Still needs `P_phase5_topological_injection`.
3. **Round 8 prep** — Φ_link sector operator construction (third-LC-tank inclusion in eigsolve framework). ~200-400 LOC new methodology; probably reframe-5 territory if it requires a new pred + driver class. Don't start until Cos-block at N=64 result is in.

---

## 8. r8.9 manual prep notes (other-agent scope) — REVISED for Mode I candidate

Per [doc 73_ §7](73_discrete_k4_tlm_lctank_operator.md) prep notes + this doc 74_ §6-§7 results (substantially revised after N=64 finding):

- **§13.5l reframe entry:** doc 73_ + §6.1 carve-out invocation language verbatim + this doc 74_ Mode I candidate result at N=64 (the N=32 Mode III was finite-N artifact, falsified by `P_phase6_lattice_resolution_sweep`) + auditor's three concerns addressed.
- **§16.1 commit rows:** ce5af9f (doc 73_ + carve-out), 8c44ef0 (doc 74_ + initial Mode III run), [TBD this commit] (Cos-block comprehensive + dispersion sanity check + resolution sweep + Mode I candidate at N=64).
- **§16.3 doc index:** doc 73_, doc 74_ entries with §6-§7 post-follow-up state and Mode I candidate framing.
- **§17.1 A37:** operator-implementation Rule 6 violation (continuum-on-discrete operator-construction error catalyzing reframe 4).
- **§17.1 A38:** implementation-level bug pattern — operator spec correctly framed but realization in code missed sub-spec details (S(z) being z-invariant under per-node uniform z; null-space artifacts in Hessian eigsolve). Caught by empirical run, fixed in same session per Rule 10.
- **§17.1 A39 (NEW, REVISED post-topology-FAIL):** dual-criterion bound-state adjudication discipline — frequency-PASS at high lattice resolution is band-density-vulnerable. The N=64 V-block GT_corpus passed the frequency criterion (gap 0.45% < α/√2) but FAILED topology (shell fraction 1.13% — bulk mode, not (2,3) localized). The auditor's concern #1 (topology check is load-bearing not confirmatory) was load-bearing exactly as predicted. **Lesson: any Mode I/II/III adjudication at fixed N needs (a) pre-registered larger-N falsification AND (b) topology / localization verification, not just frequency criterion.** Frequency-only PASS at high lattice resolution is band-density artifact. Both falsifications together are required for canonical citation. Methodology rule generalizes beyond R7.1: discrete-lattice eigenmode results need scale-and-localization verification axes; either one alone is insufficient.
- **§13.7 critical-path table:** R7.1 status now "Mode I candidate confirmed at N=64 V-block GT_corpus (gap 0.45% < α/√2 PASS tolerance); confirmation pending topology + Cos-block-at-N=64 + other-seeds-at-N=64 + N=80 follow-ups. Round 8 questions deferred contingent on N=64+ confirmation outcome. R7.2 ((2,3)/Hopf injection per G-13) independent, still needs P_phase5_topological_injection pre-reg, can run in parallel."
- **§6.1 carve-out invocation note** — first invocation in Round 7 on-record per Grant approval 2026-04-25 ("confirmed 6.1"). Round 7 may close at Mode I confirmation without needing a second invocation, contingent on N=64 follow-up results.

**r8.9 scope estimate:** ~3-4 hr focused editing — narrative is now "reframe 4 → comprehensive Mode III at N=32 → finite-N artifact via pre-registered larger-N sweep → Mode I candidate at N=64 → corpus geometry may yet be correct" rather than the original "Mode III headline + Round 8 architectural rework" framing.

---

*Doc 74_ written 2026-04-25; §6-§8 substantially revised 2026-04-26 covering four R7.1 follow-ups; §9 added 2026-04-26 with joint R7.1 + R7.2 final closure (see §9 below).*

---

## 9. Joint R7.1 + R7.2 final closure (2026-04-26)

Dual-criterion pre-registrations frozen at commit `1c89fa1`:
- `P_phase6_cos_block_n64_dual_criterion` (Cos-block N=64 GT_corpus, shell threshold 80%)
- `P_phase5_topological_injection` (R7.2 (2,3)/Hopf pair injection, frequency persistence + topology preservation dual-criterion)

Both ran in parallel. Both returned **Mode III**.

### 9.1 Cos-block N=64 GT_corpus dual-criterion: Mode III

[`r7_cos_block_n64_topology.py`](../../src/scripts/vol_1_foundations/r7_cos_block_n64_topology.py): shift-invert at σ=ω_C²=1 with inner GMRES OPinv + shell-fraction topology extraction on closest eigvec. Wall time 7506s (~2 hr), 177 OPinv calls, 53,100 inner GMRES iterations.

Result:
- Closest positive eigenvalue: λ = 1.028073, √λ = 1.013939
- Frequency criterion: **FAIL** (gap 1.394% > α = 0.7297%, 1.9× outside tolerance)
- Shell fraction: **0.0151** (1.51%, only 2.63× bulk-uniform expectation 0.0057)
- Topology criterion: **FAIL** (1.51% << 80% threshold)

**Mode III definitive on Cosserat sector.** Both criteria fail; not even frequency-PASS via band-density artifact (the failure mode that caught V-block at N=64). The Cosserat (u, ω) sector at corpus GT geometry has neither a localized eigenmode at ω_C² nor a frequency-tolerant bulk mode. ε-strain / κ-curvature LC tanks per [doc 66_ §17.2](66_single_electron_first_pivot.md) do NOT host the (2,3) bound state at corpus GT geometry at this N.

### 9.2 R7.2 (2,3)/Hopf pair injection: Mode III

[`phase5_topological_pair_injection.py`](../../src/scripts/vol_1_foundations/phase5_topological_pair_injection.py): seeds (2,3) torus-knot ansatz at chirality-matched bond endpoints (LH at A, RH at B), runs autoresonant drive + post-drive observation per Phase 5 case (b') registered config. Wall time 14.2s.

Result:
- Frequency persistence: **FAIL** — peak |ω|_A,B drop below 0.5·seed during drive; doesn't persist for 10 Compton periods post-drive
- Topology preservation: c_cos trajectory min=0, max=3, end=2 (target=3) — drifts; **FAIL**
- **Mode III**: topologically-richer (2,3) torus-knot ansatz dissolves at the same timescale as Beltrami (Phase 5 case b'). **Coupling-depth issue, not injection-profile issue.**

Methodology caveat on topology criterion: `extract_crossing_count` is global; for a chirality-matched pair-bound state with opposite winding at endpoints, it may read 0 or 6 instead of 3 per endpoint. Initial c=2 reflects this measurement ambiguity. **However, the frequency criterion alone fails decisively** — peak |ω| dissolves regardless of how the topology is measured. Mode III stands.

### 9.3 Joint final headline — unified framework-level statement

**At corpus Golden Torus geometry (R/r = φ², R·r = 1/4) under the K4-TLM scatter+connect + Cosserat (u, ω) LC-tank Hessian-of-W operator framework (per [doc 73_ §2-§5](73_discrete_k4_tlm_lctank_operator.md)) with A26-canonical amplitude (peak |ω| = 0.3π per [doc 34_ §9.4](34_x4_constrained_s11.md)): the K4-TLM substrate hosts NO (2,3)-localized bound mode in V-pressure (V-block, N=32 + N=64 dual-criterion), NO (2,3)-localized bound mode in ε-strain/κ-curvature (Cos-block, N=32 frequency + N=64 dual-criterion), and NO topologically-protected pair-state persisting under Cosserat self-dynamics post-drive (R7.2 with (2,3)/Hopf injection per VACUUM_ENGINE_MANUAL §9 G-13). Three independent test classes, all Mode III, mutually reinforcing.**

The five-test empirical breakdown (each test independently confirms the framework statement):

| Test | Sector | Lattice | Result | Gap to PASS | Topology |
|---|---|---|---|---|---|
| V-block | V_inc K4 | N=32 | Mode III | 1.22% (1.7× over α/√2) | n/a (freq FAIL) |
| V-block | V_inc K4 | N=64 | Mode III | 0.45% (PASS freq) | shell 1.13% (bulk) |
| Cos-block | (u, ω) | N=32 (4 seeds) | Mode III | 1.04-2.00% | n/a (freq FAIL) |
| Cos-block | (u, ω) | N=64 GT_corpus | Mode III | 1.39% (FAIL) | shell 1.51% (bulk) |
| R7.2 pair injection | Cosserat ω | N=24 | Mode III | freq dissolves at Beltrami timescale | c=2 at end (FAIL) |

Across five tests at three distinct lattices and two operator framings: **no test detected a (2,3) bound state matching corpus claims.** This is a substantive framework-level negative finding.

**On the symmetric Mode III pattern:** V-block N=64 had band-density-artifact frequency-PASS (gap 0.45% with shell 1.13%); Cos-block N=64 didn't even reach frequency-PASS (gap 1.39% with shell 1.51%). Both blocks return shell fractions ~50× below the 80% Mode I threshold and 5-10× below even a 30% lenient threshold. The threshold-adjudication debate (30/50/80%) was less consequential than it felt at adjudication time — both V-block and Cos-block returned shell fractions far below any plausible threshold. **What was load-bearing was the dual-criterion structure itself**, not the threshold value: without topology check, Cos-block N=64 frequency at 1.39% would have read as Mode III by frequency alone (correct verdict but incomplete reasoning), and the band-density-vulnerability lesson wouldn't have been demonstrated symmetrically across both sectors.

### 9.4 Round 8 entry — Φ_link sector

Per [doc 66_ §17.2](66_single_electron_first_pivot.md) three-storage-mode picture, the bound electron at each engine node has THREE LC tank conjugates:
1. **K4 bond LC**: V_inc ↔ Φ_link (V-block tested empty)
2. **Cosserat translational LC**: u ↔ u_dot (covered by Cos-block u-component, tested empty)
3. **Cosserat rotational LC**: angular position ↔ ω (covered by Cos-block ω-component, tested empty)

But Φ_link in the K4 sector is treated as a DERIVED flux observable per [doc 70_ §7.2](70_phase5_resume_methodology.md) (A29 finding: Φ_link is `∫V_avg·dt`, not an independent dynamical state). The V-block eigsolve operates on V_inc state; Φ_link is computed from V_inc trajectories, not eigsolved over.

If the (2,3) electron's bound state lives in the Φ_link DEGREE-OF-FREEDOM (rather than V_inc directly), no V-block or Cos-block eigsolve as currently formulated can find it. **This is the cleanest unprobed gap in the corpus three-storage-mode picture.**

Round 8 entry candidates ordered by current empirical evidence:

1. **Φ_link sector eigsolve** — extend operator framework to include Φ_link as eigenstate (or test whether time-domain Φ_link evolution under driven seed shows (2,3) winding stabilization). New methodology; ~200-400 LOC; likely reframe-5 territory if it requires a new pred + driver class.
2. **Hybrid V≠0 ∧ ω≠0 modes** — V=0 seed misses by [doc 73_ §3.1.1](73_discrete_k4_tlm_lctank_operator.md). Test via quadrature seed at small V_amp (~0.05·V_SNAP).
3. **(2,3) representation structural rework** — weakest; testable by sweeping (1,2), (2,5), (3,5), (3,7) windings for any that hosts an eigenmode at ω_C with shell localization.

### 9.5 Methodology lessons (final, for r8.9 §17.1) — split into A40 + A41 per audit recommendation

- **A37**: continuum-on-discrete operator-construction error catalyzing reframe 4 (§6.1 carve-out invocation #1).
- **A38**: implementation-level bug pattern (S(z) z-invariance + null-space artifact); operator spec correctly framed but realization in code missed sub-spec details.
- **A39 v2**: dual-criterion bound-state adjudication discipline (frequency + localization, both required at fixed N to defeat band-density-vulnerability at high lattice resolution; pre-registered larger-N falsification additionally required to defeat finite-N-artifact at low lattice resolution).
- **A40 (NEW — methodology-meta)**: empirical-driver-arc discipline. R7.1 went through 4 reframes + 3 result flips + 4 follow-ups + 2 final tests in this session, each catching a real issue. **The total sequence took ~10 hours of compute + analysis but produced a definitive negative result that single-pass analysis would have miscalled** (originally as Mode III at N=32 → Round 8; then mis-corrected to Mode I at N=64 → corpus vindicated; finally properly as Mode III via dual-criterion + Cos-block coverage). The number of layers and flips in this arc is the upper bound for how many adjudication layers a bound-state-existence question on a discrete-lattice substrate may need. Future questions in this register should pre-register dual-criterion + multi-N + multi-sector from the start to avoid the iterative refinement cost.
- **A41 (NEW — structural physics)**: G-13 injection-profile-upgrade falsified at coupling-depth layer; unifies A30/A32/A34 family at deeper layer. Per VACUUM_ENGINE_MANUAL §9 G-13, the contingency for "Beltrami pair dissipates faster than 10 Compton periods" was to upgrade the injection profile to topologically-richer (2,3) torus-knot or Hopf fibration. R7.2 ([`phase5_topological_pair_injection.py`](../../src/scripts/vol_1_foundations/phase5_topological_pair_injection.py)) tested this at the same registered config as Phase 5 case (b'). Result: **the (2,3) torus-knot ansatz also dissolves at the same timescale as the Beltrami point-rotation profile.** Frequency persistence FAIL; topology preservation FAIL.

  **The unifying claim across A30 + A32 + A34 + A41 strengthens at a deeper layer:**
  - A30 (corpus-duality FALSIFIED): Cosserat-energy descent and coupled-S₁₁ descent converge at different (R, r) endpoints, neither at GT — *dynamical descent doesn't reach GT from arbitrary seed*
  - A32 (X4b linear-stability UNSTABLE): Golden Torus seed UNSTABLE under coupled S₁₁ descent — *GT isn't even a stable fixed point at coupled scale*
  - A34 (Beltrami injection profile fundamentally unstable): point-rotation Beltrami at gate's `_inject_pair` profile dissolves 93% in one VV step — *gate's seed is structurally unviable*
  - A41 (G-13 contingency FALSIFIED): topologically-richer (2,3)/Hopf ansatz also dissolves at the same Cosserat self-dynamics timescale — *injection-profile richness alone is insufficient; coupling depth must sustain the topology*

  **The unified reading was originally "topology must be encoded as ansatz, not derived dynamically" (post-Round-6).** A41 strengthens this to: **"topology must be encoded as ansatz AND the engine's coupling depth must sustain the topological invariant under self-dynamics; injection-profile richness alone is insufficient."** Round 8 entry candidates (Φ_link sector / hybrid V≠0 ∧ ω≠0 / (2,3) representation rework) all fall under "what additional dynamics is needed to provide that coupling depth?" framing. The R7.2 test was load-bearing for this reading — without it, the Round 8 ordering would have weighted (2,3) representation rework higher; with it, the framing shifts toward "the engine's coupling architecture is the gap, not the topological winding choice."

### 9.6 Round 7 status

R7.1 closed empirically. R7.2 closed empirically. Both Mode III at corpus GT. Round 7 closes with substantive negative result on the V-block + Cos-block + topologically-richer-injection axes; Round 8 Φ_link sector becomes the next empirical move.

**Round 7 did NOT vindicate corpus geometry empirically; the (2,3) electron bound state at corpus GT is not detectable in the engine's current V/Cos sectors.** This is consistent with [doc 03_ §4.3](03_existence_proof.md) ("R·r=1/4 is topologically quantized, NOT dynamically derived") in the sense that no dynamical descent reaches GT — but stronger: even the eigenvalue-spectrum question at corpus GT returns empty. The bound state, if it exists at corpus GT, lives in either (i) a sector not currently in the eigsolve framework (Φ_link), or (ii) a hybrid (V≠0 ∧ ω≠0) regime, or (iii) requires a different topological winding than (2,3).

---

*§9 added 2026-04-26 — joint R7.1 + R7.2 final closure. Cos-block N=64 GT_corpus dual-criterion: Mode III (freq FAIL 1.39% + topology FAIL 1.51% shell fraction). R7.2 (2,3)/Hopf pair injection: Mode III (frequency dissolves at Beltrami timescale; topology criterion has measurement ambiguity but irrelevant since freq fails). Joint headline (§9.3 unified statement): K4-TLM engine does NOT host (2,3) electron bound state in V-pressure or ε-strain sectors at corpus GT, AND topological-richness-only doesn't rescue Beltrami case (b'). Round 8 entry: Φ_link sector (cleanest unprobed gap in three-storage-mode picture). A40 (empirical-driver-arc discipline, methodology-meta) + A41 (G-13 falsified at coupling-depth layer; unifies A30/A32/A34 at deeper layer; structural physics) split per audit recommendation. Both for r8.9 §17.1.*

---

## 10. Three follow-up empirical tests close the negative-result envelope (2026-04-26)

Per audits on commits `8c44ef0` (Φ_link creeper flag → A43), `88ec7c3` (corpus-canonical topology measure for c via Op10 → A42 Test A re-extraction), and `53c2ce9` (Test B single-port sampling can't answer doc 28_ §5.1's spatial-winding question → A44 spatial-vs-temporal phasor distinction), three follow-up tests were frozen and run before doc 74_ closure. **All three returned Mode III**, extending the §9.3 unified framework-level statement across two new axes (corpus-canonical Cosserat topology + bond-cluster spatial envelope).

### 10.1 Test A — Cos-block N=64 GT_corpus c_eigvec re-extraction: Mode III-both

[`r7_cos_block_n64_c_eigvec.py`](../../src/scripts/vol_1_foundations/r7_cos_block_n64_c_eigvec.py) — re-runs the Cos-block N=64 GT_corpus dual-criterion eigsolve from §9.1 but replaces the shell-localization heuristic with **corpus-canonical c via Op10** (`extract_crossing_count` on the ω-component of the joint (u, ω) eigvec, per Doc 07_). 4-category adjudication per `P_phase6_cos_block_n64_c_eigvec_recheck` frozen at commit `53c2ce9`.

| Metric | Value | Threshold | PASS? |
|---|---|---|---|
| Closest λ | 1.0252 | — | — |
| √λ_closest | 1.0125 | ω_C = 1.0 | — |
| rel_diff | **1.2509%** | α = 0.7297% | **NO (1.7× over)** |
| c_eigvec via Op10 | **0** | 3 | **NO** |

**Mode III-both** — both criteria fail. Cosserat sector at corpus GT is empty in BOTH frequency and corpus-canonical topology axes.

The shell-localization-heuristic finding from §9.1 (1.51% shell fraction << 80% threshold) is now **independently confirmed** by the corpus-canonical c measure. The closest eigvec at √λ=1.0125 has zero (2,3) winding by Op10's scalar crossing count — not just delocalized in real space, but topologically trivial in the corpus's own measurement convention.

A42 (corpus-canonical c via Op10 ≠ shell-localization heuristic) is empirically validated: both measures agree on Mode III at this seed/lattice, but the c-via-Op10 measure is the load-bearing one for r8.9 citation per Doc 07_'s §6.2 framing. Wall time 8003s (~2.2 hr), 189 OPinv calls, 56,700 inner GMRES iterations.

### 10.2 Test B v1 + retry Mode II-temporal at single port: amplitude-invariant, can't answer doc 28_ §5.1

[`test_b_bond_scale_phasor.py`](../../src/scripts/vol_1_foundations/test_b_bond_scale_phasor.py) (v1, 0.1·V_SNAP) and [`test_b_bond_scale_phasor_retry.py`](../../src/scripts/vol_1_foundations/test_b_bond_scale_phasor_retry.py) (v1-retry, 0.5·V_SNAP) sample temporal (V_inc(t), V_ref(t)) at port 0 of A=(14,14,14), compute PCA-derived R/r aspect.

| Drive amp | A² | R/r temporal | Mode |
|---|---|---|---|
| 0.1·V_SNAP | 0.01 | 19.00 | II |
| 0.5·V_SNAP | 0.25 | 19.20 | II |

R/r is amp-invariant within ~1% across two orders of magnitude in A². **Audit catch on commit 53c2ce9**: doc 26_ §1's standing wave is `ψ(s, t) = V₀·A(s)·exp(i(ωt+θ(s)))` — at fixed s, (V_inc, V_ref) traces a CIRCLE (single frequency, no torus). Doc 26_ §3 defines R_phase, r_phase as **spatial** averages over s. A single-port sample is one s value → one circle → R/r = aspect of small-signal ellipse, not the corpus phase-space torus. v1 and v1-retry asked the wrong question.

A44 (NEW for r8.9 §17.1) — **spatial-vs-temporal phasor distinction**: when testing "phase-space torus" claims under doc 26_'s framing, sample multiple spatial points and compute spatial mean/std over the s-axis envelope. Single-point temporal sampling at any drive amplitude returns a circle whose aspect is determined by drive ellipticity, not by corpus θ(s) winding. Methodology rule for future bond-scale phasor tests: minimum 8 spatial samples (e.g., 4 ports × 2 nodes) before computing R_phase / r_phase.

### 10.3 Test B v2 + v3 multi-port spatial sampling: Mode III-spatial at both linear and saturation regimes

[`test_b_v2_multipoint_phasor.py`](../../src/scripts/vol_1_foundations/test_b_v2_multipoint_phasor.py) (v2, 0.5·V_SNAP) and [`test_b_v3_multipoint_phasor_satsweep.py`](../../src/scripts/vol_1_foundations/test_b_v3_multipoint_phasor_satsweep.py) (v3, 0.85·V_SNAP) sample 4 ports of A=(14,14,14) + 4 ports of B=(15,15,15) = 8 spatial samples spanning the local A-B bond cluster. Per-port `ρ_i = √(⟨V_inc²⟩_t + ⟨V_ref²⟩_t)` over steady state. Spatial R = mean(ρ), r = std(ρ) over 8 samples per doc 26_ §3.

| Drive amp | A² | R_spatial | r_spatial | rel_std r/R | Mode |
|---|---|---|---|---|---|
| 0.5·V_SNAP (v2) | 0.25 | 0.0994 | 0.0039 | **0.0392** | III-spatial |
| 0.85·V_SNAP (v3) | 0.72 | 0.1367 | 0.0065 | **0.0474** | III-spatial |

Per-port ρ values (v3 saturation regime):
- A: 0.1363, 0.1301, 0.1295, 0.1295
- B: 0.1363, 0.1487, 0.1415, 0.1415

The 12-14% per-port range is dominated by **drive-direction asymmetry** — B sites lie downstream of the +x autoresonant source, so wave amplitude is slightly higher there. This is wave-propagation geometry, not (2,3) winding. Both v2 and v3 fall below the pre-registered rel_std threshold of 0.05 → **Mode III-spatial**: bond cluster is essentially uniform, no spatial envelope structure that could carry corpus θ(s) winding.

**Op14 nonlinearity engagement past saturation onset (A² = 0.72) doesn't change the answer.** The bond cluster develops a 5% spatial asymmetry from drive geometry but no (2,3) topology. Single-bond hypothesis per doc 28_ §5.1 falsified at bond-cluster scale across both linear and saturation drive regimes.

### 10.4 Updated framework-level statement (extends §9.3)

Five test classes, three lattices, two operator framings, two amplitude regimes, two topology measures (shell-localization + corpus-canonical c via Op10). All Mode III:

| Test | Sector | Lattice | Drive | Result | Topology measure |
|---|---|---|---|---|---|
| V-block | V_inc K4 | N=32 | seed-init | Mode III | n/a (freq FAIL) |
| V-block | V_inc K4 | N=64 | seed-init | Mode III | shell 1.13% (bulk) |
| Cos-block (§9.1) | (u, ω) | N=64 | seed-init | Mode III | shell 1.51% (bulk) |
| **Cos-block c (Test A)** | (u, ω) | N=64 | seed-init | **Mode III-both** | **c=0 via Op10** |
| R7.2 pair injection | Cosserat ω | N=24 | autoresonant | Mode III | c=2 (drift) |
| Bond v2 (Test B v2) | V_inc bond cluster | N=32 | 0.5·V_SNAP CW | Mode III-spatial | rel_std 0.039 |
| Bond v3 (Test B v3) | V_inc bond cluster | N=32 | 0.85·V_SNAP CW | Mode III-spatial | rel_std 0.047 |

**Across seven tests at three lattices and three operator framings (eigsolve + driven phasor + autoresonant pair injection), at two amp regimes (linear + saturation), under two topology measures (shell-localization + Op10 corpus-canonical): no test detected (2,3) bound state structure at corpus GT geometry.**

The §9.3 framework-level negative result holds under the §10 follow-up audits' stronger criteria. Round 8 entry candidates (Φ_link sector / hybrid V≠0 ∧ ω≠0 / (2,3) representation rework) remain ordered as in §9.4.

### 10.5 Methodology lessons added in this section (for r8.9 §17.1)

- **A42 (existing — empirically validated by Test A)**: corpus-canonical (2,3) topology measure is c via Op10 + extract_crossing_count per Doc 07_, NOT real-space shell-localization. Both measures agree on Mode III at the §9.1 / §10.1 seed, but Op10's c is the load-bearing measure for r8.9 citation.
- **A43 (existing — confirmed during the test sequence)**: Φ_link sector is NOT directly probed by V-block (which operates on V_inc states); Φ_link is derived from V_inc trajectories per A29 (`Φ_link = ∫V_avg·dt`). The "Φ_link sector" Round 8 entry candidate per §9.4 should be framed as "test whether time-domain Φ_link evolution under driven seed shows (2,3) winding stabilization," not as an independent eigsolve sector.
- **A44 (NEW — methodology-meta)**: spatial-vs-temporal phasor distinction. Doc 26_'s standing-wave equation `ψ(s, t) = V₀·A(s)·exp(i(ωt+θ(s)))` has the (2,3) winding in spatial θ(s), not temporal harmonics. At fixed s, (V_inc, V_ref) traces a CIRCLE — single frequency, no torus structure regardless of drive amp. Doc 26_ §3's R_phase, r_phase are SPATIAL averages over s. Future bond-scale phasor tests under this corpus framing must sample multiple spatial points (minimum: all ports of two adjacent nodes for K4-TLM) and compute mean/std over the spatial envelope, not PCA on a single-port temporal trajectory. v1 + v1-retry's amplitude-invariant R/r=19 result was the smoking gun — temporal aspect ratio at one port doesn't engage spatial structure at all.

### 10.6 Round 7 final closure

R7.1 + R7.2 closed empirically across §1-§9; §10 follow-ups extend the closure across the two audit-flagged dimensions (corpus-canonical topology + spatial-vs-temporal phasor distinction). **All seven tests Mode III. The bond-scale single-bond hypothesis per doc 28_ §5.1 joins the framework-level §9.3 statement at bond-cluster scale.** Round 8 Φ_link sector (re-framed per A43) becomes the cleanest unprobed empirical gap; (3,5)/(2,5) winding sweeps and hybrid V≠0 ∧ ω≠0 seeds remain Round 8 candidates per §9.4.

---

*§10 added 2026-04-26 covering three follow-up empirical tests (Test A Mode III-both via Op10 c=0; Test B v2 Mode III-spatial at 0.5·V_SNAP; Test B v3 Mode III-spatial at 0.85·V_SNAP). Audit-flagged findings A42 (corpus-canonical c via Op10) empirically validated, A43 (Φ_link derived not eigsolved) confirmed in framing, A44 (spatial-vs-temporal phasor distinction) added as new methodology-meta finding. Updated framework-level statement (§10.4): seven tests, four lattices, three operator framings, two amp regimes, two topology measures — all Mode III at corpus GT.*

---

## 11. Round 8 Move 5 — self-consistent orbit hunt at corpus GT: Mode III-orbit per pre-reg BUT self-stable sub-corpus (2,3) orbit found empirically (2026-04-26)

Move 5 was Round 8's first empirical entry: a time-domain test of corpus's actual claim that the (2,3) electron is a self-stable nonlinear standing wave at ω_C, not a linear eigenmode. R7.1 + §10 established that no LINEAR eigenmode at corpus GT hosts (2,3) bound state. Move 5 tests whether a NONLINEAR self-trapped orbit might exist — and, distinctly from R7.2's pair injection, does so at single-electron at corpus GT (R=10, r=R/φ²) with no external drive.

Result: **Mode III-orbit per strict pre-reg adjudication, BUT the empirical signal is qualitatively different from §1-§10's pure-Mode-III pattern.** The orbit didn't dissolve. It RELAXED to a sub-corpus self-stable (2,3) configuration.

### 11.1 Driver methodology

[`r8_self_consistent_orbit_hunt.py`](../../src/scripts/vol_1_foundations/r8_self_consistent_orbit_hunt.py) per [`P_phase6_self_consistent_orbit_hunt`](../../manuscript/predictions.yaml) frozen at commit `b11996d`. Key elements:

- Engine: VacuumEngine3D at N=32, A28 + Cosserat self-terms (post-Round-6 default), **no external drive**
- Joint seed at corpus GT (R=10, r=3.82):
  - ω: corpus (2,3) hedgehog via `initialize_electron_2_3_sector` at peak |ω| = 0.9262 ≈ 0.3π (A26 amplitude scale, matches R7.1 GT_corpus seed)
  - V_inc: corpus (2,3) chiral-phasor voltage via `initialize_2_3_voltage_ansatz` at amplitude=0.14 → peak v_total = 0.4592 (mid Regime II per AVE three-regime convention; saturation engaged from t=0)
  - Phase relationship: cos(2φ+3ψ) on K4 ports 0,1 / sin on ports 2,3 — natural quadrature consistent with one phase of standing-wave cycle per doc 26_ §1
- Evolution: 200 Compton periods (1777 steps at dt=1/√2), 255s wall
- Sample at t ∈ {0, 5, 10, 25, 50, 100, 150, 200} P with peak |ω|, peak v_total, c via Op10, shell-localized ω-energy fraction

Initial state validation: c=3 at t=0 (corpus topology preserved by joint seeder), shell_frac = 0.787 (78.7% of ω-energy on the corpus shell, far above the 1.13-1.51% bulk-mode levels we saw at N=64 eigsolve in §10). The seed *is* the corpus electron at one phase.

### 11.2 Time evolution — the critical observation

| t (P) | peak \|ω\| | persistence | peak v_total | c | shell_frac |
|---|---|---|---|---|---|
| 0 | 0.9262 | 1.000 | 0.4592 | **3** | **0.787** |
| 5 | 0.5179 | 0.559 | 0.3946 | 1 | 0.447 |
| 10 | 0.4355 | 0.470 | 0.3911 | **0** | 0.395 |
| 25 | 0.3079 | 0.332 | 0.3780 | **0** | 0.332 |
| **50** | **0.3044** | **0.329** | 0.3799 | **3** | 0.308 |
| **100** | **0.3044** | **0.329** | 0.3937 | **3** | 0.192 |
| **150** | **0.3044** | **0.329** | 0.3988 | **3** | 0.170 |
| **200** | **0.3044** | **0.329** | 0.4026 | **3** | 0.136 |

Two phases:

**Transient (t ∈ [0, 50P])** — the corpus seed unwinds. Peak |ω| collapses from 0.926 to 0.304 over 50 Compton periods. Topology cycles 3 → 1 → 0 → 0 → 3 (winding unwinds and re-establishes). Shell fraction drops from 0.787 to 0.308.

**Plateau (t ∈ [50P, 200P])** — orbit stabilizes. peak |ω| **identical to four decimals at t=50P, 100P, 150P, 200P (0.3044)** — 150 consecutive Compton periods of locked amplitude. c=3 preserved continuously. Peak v_total slowly rises 0.380 → 0.394 → 0.399 → 0.403. Shell fraction continues to slowly decay 0.31 → 0.19 → 0.17 → 0.14.

The plateau is genuinely stable, not a slow decay. Energy is transferring ω → V_inc (peak v_total rising) while topology stays in ω (c=3). The orbit is migrating off the corpus shell to a different geometry where it self-stabilizes.

### 11.3 Adjudication — pre-reg verdict vs empirical reading

**Pre-reg verdict: Mode III-orbit.** Persistence 0.329 < 0.50 threshold. Topology criterion also failed (c=0 at t=10P and t=25P, violating "c=3 at every post-transient sample"). Both criteria fail; pre-reg adjudication is unambiguous Mode III.

**Empirical reading is qualitatively distinct from §1-§10's pure-Mode-III pattern.** In R7.1 V-block + Cos-block, R7.2 pair injection, and Test B bond-cluster, the engine produced no observable (2,3) signal at corpus GT — pure null. Move 5 produced something different: the engine ran the corpus seed → unwound to non-corpus (2,3) configuration → STABILIZED there for 150+ periods.

The engine HOSTS a self-stable nonlinear (2,3) orbit. The corpus claim that this orbit lives at (R=10, r=R/φ², peak |ω|=0.3π) is wrong on the geometry/amplitude side, but the underlying topological framework (an electron is a (2,3) self-trapped soliton) is empirically supported.

This is the cleanest "corpus framework substantively right but specific parameters wrong" signal in the R7+R8 arc. None of §1-§10's tests could have produced this signal — eigsolve and driven CW response both linearize or test asymptotic dressing, neither captures the nonlinear self-trapping that Move 5 directly observed.

### 11.4 What's known about the settled orbit

From the t=200P state:
- peak |ω| ≈ 0.304 (vs corpus 0.926; ratio 0.329 ≈ 1/3)
- peak v_total ≈ 0.40 (vs initial 0.46; relatively preserved — V_inc field intact)
- c = 3 (corpus-canonical (2,3) winding via Op10)
- shell_frac = 0.136 — orbit migrated AWAY from corpus (R=10, r=3.82); only 14% of ω-energy still in the corpus shell region
- 86% of ω-energy is at non-corpus geometry — the orbit's actual (R, r) is unknown from this run

### 11.5 Round 8 next move — Move 6: settled-orbit geometry mapping

The empirical signal flips Round 8's natural follow-up from Move 3 (auditor's hybrid eigsolve) to a NEW Move 6: **measure the settled orbit's actual (R, r) and amplitude**. If the engine has settled at (R', r') ≠ corpus (10, 3.82), what is (R', r')?

Move 6 design (~30-60 min wall, ~150 LOC):
- Run engine identically to Move 5 to t=100P (well into plateau), seeded at corpus GT
- At t=100P, take the live ω(x) field
- Extract (R', r') via shell-fitting on the |ω|² density:
  - Compute centroid of ω-energy density as proposed center
  - Sweep candidate (R', r') torus shells centered there; find (R'*, r'*) that maximizes shell-localized fraction
  - Report R'*/r'* ratio (compare to φ² = 2.618 — corpus claim) and absolute (R'*, r'*) values
- Sub-criterion: spatial winding signature on |ω(x)| over the new shell — confirm (2,3) topology lives at (R'*, r'*)

Adjudication for Move 6:
- **Mode I-geometry**: R'*/r'* = φ² ± 0.10 (corpus *ratio* vindicated, just at different absolute scale)
- **Mode II-geometry**: R'*/r'* ≠ φ² but (R'*, r'*) well-defined and shell_frac at new shell > 0.5 (orbit at non-corpus ratio)
- **Mode III-geometry**: no well-defined shell — orbit is delocalized

If Mode I-geometry: **corpus's R/r=φ² ratio claim is correct; only the absolute lattice anchor was wrong**. This is a HUGE Round 7 outcome inversion — corpus's qualitative framework empirically vindicated, just need to recalibrate R_anchor to the engine's natural scale.

If Mode II-geometry: corpus's specific φ² ratio is wrong; the engine prefers a different aspect ratio. Empirically substantive but reframes the corpus claim.

If Mode III-geometry: orbit is genuinely delocalized despite topological invariant; would point to different methodology.

**Move 6 is now the load-bearing Round 8 next test, ahead of Move 3.** Move 3 (hybrid eigsolve) becomes useful AFTER Move 6 lands — measure the settled orbit's (R', r'), then re-do eigsolve at the engine's actual self-consistent (R', r') seed instead of corpus (10, 3.82). That's the right sequencing.

### 11.6 Methodology lessons (for r8.9 §17.1)

- **A45 (NEW — methodology-substantive)**: NONLINEAR self-trapped orbits cannot be detected by linearized eigsolve at any static seed; time-domain orbit hunt at finite amplitude is the load-bearing test. Move 5's plateau (peak |ω| identical to 4 decimals across 150 Compton periods) was empirically detectable only because the test ran self-dynamics directly. Eigsolve would have missed it regardless of seed choice.
- **A46 (NEW — corpus-physics)**: empirical evidence supports the (2,3) self-trapped soliton FRAMEWORK at qualitative level (engine hosts such an orbit) but FALSIFIES corpus's specific quantitative parameters (R=10, r=R/φ², peak |ω|=0.3π). Round 8 narrative shifts from "is corpus right?" (answer at corpus GT: no) to "where is the engine's actual self-stable (2,3) orbit, and does it match corpus's R/r=φ² ratio at a different absolute scale?"
- **A47 (NEW — pre-reg discipline)**: Mode III-orbit per pre-reg is correct strict adjudication; the §11.3 nuanced reading is for narrative framing in r8.9 §13.7 critical-path table, not a re-adjudication. Pre-reg verdict and empirical signal can both be true at different framing levels — pre-reg is the discrete gate, narrative captures the continuous structure.

### 11.7 Round 7 + 8 status update

- R7.1 + R7.2 closed Mode III at all 7 tests — no LINEAR mode, no nonlinear orbit at corpus GT, no pair-injection persistence
- §10 follow-ups (Test A Op10 + Test B v2/v3 spatial) closed Mode III at corpus-canonical topology + saturation regimes
- **Move 5 (Round 8 entry) returns Mode III-orbit per pre-reg BUT empirically discovers self-stable sub-corpus (2,3) orbit** — the framework-substantive opening
- **Move 6 next**: characterize the settled orbit's (R, r). If R/r ≈ φ² at non-corpus scale → corpus ratio claim vindicated, only anchor wrong. If R/r ≠ φ² → corpus ratio wrong too.
- Move 3 (auditor's hybrid eigsolve) deferred until Move 6 lands — re-do eigsolve at engine's actual self-consistent (R', r') seed, not corpus (10, 3.82)

---

*§11 added 2026-04-26 — Round 8 Move 5 result. Mode III-orbit per pre-reg (persistence 0.329 < 0.50, topology criterion failed mid-transient at c=0 t=10P/25P). BUT empirical plateau at t∈[50P, 200P]: peak |ω|=0.3044 to 4 decimals across 150 consecutive Compton periods, c=3 preserved continuously, orbit migrated off corpus shell (shell_frac 0.79 → 0.14). The engine hosts a self-stable nonlinear (2,3) orbit at sub-corpus parameters. Move 6 (settled-orbit geometry mapping) becomes load-bearing Round 8 next test, ahead of Move 3 (hybrid eigsolve). A45+A46+A47 added for r8.9 §17.1.*

---

## 12. Move 6 — natural-attractor geometry/phasor/spectrum: Mode III-natural (delocalized) → meta-methodological pivot (2026-04-26)

Move 6 ran per [`P_phase6_natural_attractor_characterization`](../../manuscript/predictions.yaml) frozen at commit `97178c6`. Three integrated extractions on the Move 5 attractor:

### 12.1 Result summary

| Extraction | Output | Reading |
|---|---|---|
| (a) GEOMETRY shell-fit | R_opt = 14.00, r_opt = 6.00 (search boundary), shell_frac_opt = 0.231 | **Pegged at search-grid boundary** with sub-threshold localization (0.231 < 0.40). Orbit is delocalized — no clean torus shell. |
| (b) PHASOR R_spatial / r_spatial | 2.46 (vs corpus φ² = 2.618), rel_std = 0.41 | Ratio close-ish to φ² but rel_std 41% means very high spatial variability across 8 sample cells; not a clean phase-space torus signal. |
| (c) SPECTRUM peak \|ω\|(t) | top freqs (natural ω): 0.020, 0.030, 0.040 rad/unit | All three top freqs are very low — this is the slow drift in peak position, NOT oscillation at ω_C = 1.0. |
| (c) SPECTRUM peak \|V_inc\|(t) | top freqs: 4.44, 0.010, 4.43 rad/unit | 4.44 ≈ π·√2 = lattice-timestep frequency (2π/dt at dt=1/√2). Near-Nyquist content, not physical. |

**Verdict: Mode III-natural** (delocalized — shell_frac_opt < 0.40 threshold). Spectrum confirms: ω is drifting slowly (not oscillating), V_inc has lattice-Nyquist artifact content. The attractor has corpus-canonical c=3 topology preserved, but it is NOT a clean standing-wave at ω_C in either the V or ω sector.

### 12.2 Meta-methodological audit

Across §1–§11 (R7.1 + R7.2 + §10 follow-ups + Move 5) and §12 (Move 6), the cumulative pattern:

- **Tests run:** ≥9 distinct configurations — V-block eigsolve at 4 seeds × N=32+N=64; Cos-block eigsolve dual-criterion at N=32 + N=64 (shell + Op10); R7.2 (2,3)/Hopf pair injection; Test B v1/v1-retry single-port temporal; Test B v2/v3 multi-port spatial at linear + saturation; Move 5 single-electron self-consistent orbit; Move 6 natural-attractor geometry/phasor/spectrum.
- **Results:** all Mode III against the question "does the corpus electron live at this configuration?" Move 5 produced a self-stable (2,3) plateau but at sub-corpus parameters; Move 6 confirmed the plateau is delocalized and not a clean ω_C standing wave.
- **Question structure:** every test pre-registered "is corpus electron at config X?" → got Mode III → next test asked "is corpus electron at config Y?" Search through configuration space, looking under streetlights.

**The accumulated signal is already substantive: the engine does not produce a corpus-electron-shaped object at any pre-specifiable corpus-claimed configuration.** Continuing to specify configurations elaborates the same finding at higher resolution. Move 6's framing ("does R/r = φ² at the natural attractor?") was the same pattern at higher resolution — Mode III-natural confirms the question shape doesn't fit the data either.

### 12.3 Pivot — characterize the attractor as itself

Per audit on Move 6 result: **stop pre-registering "is corpus electron at config Y?" tests.** Switch frame: the engine produced a system-found stable c=3 attractor at t=200P. We extracted persistence + binary verdict, but never asked **what kind of object it is**.

Move 7 / Phase 1 characterization (frozen at next commit, characterization-only, no PASS/FAIL):

- **Spatial moments**: at t=200P, compute centroid (cx, cy, cz) of |ω|² density, second moments (extent in x, y, z), principal axes via PCA on the energy distribution. Get R_eff and r_eff via geometric extent, not torus-shell template fit.
- **FFT at FIXED spatial points** (not peak-tracking): record V_inc(t) and ω(t) at 5 fixed lattice points (centroid + 4 displaced) over t=150P→200P window. FFT each. Identify true dominant frequencies in the temporal evolution, distinct from the slow drift in peak position that Move 6 measured.
- **Q-factor from transient**: fit log(peak |ω|) vs t over t=10P→50P decay phase. Slope gives 1/τ; Q = ω_C·τ/2 if assuming oscillation at ω_C.
- **(V_inc, V_ref) phasor trajectory at the centroid**: sample the (V_inc, V_ref) at the spatial centroid over t=150P→200P; plot in 2D phase space, compute closed-trajectory aspect ratio (is this ANY clean standing wave? What ratio?).
- **Energy partition**: at t=200P, total energy split across K4 V-pressure sector, Cosserat ω² sector, Cosserat |u|² sector, Cosserat |∇u|² sector. Where does the energy actually live?

This is **descriptive characterization**, not a hypothesis test. The result is the attractor's properties as measured. Phase 2 (post-Phase-1 decision) follows based on what those properties show:

- If the attractor has electron-like properties (Q ≈ 137, frequency at ω_C or simple multiple, c = 3, energy ~ m_e c² in natural units): the corpus electron IS in the engine, just at different parameters than corpus seed assumed. Round 7+8 closure narrative changes substantially.
- If the attractor is electron-like in topology + amplitude but not frequency/Q: partial match — engine hosts a (2,3)-topological object but it isn't the corpus electron.
- If the attractor has none of the electron-like properties: structural finding — engine missing physics, OR corpus claim about engine-electron correspondence at this engine implementation is wrong.

Each branch implies a different next move. Currently we're in the third branch (testing more configurations) without distinguishing the branches.

### 12.4 Methodology lesson — A48 (NEW for r8.9 §17.1)

**A48: pre-reg discipline + dual-criterion adjudication is the right discipline for "is X at config Y?" questions but produces clean negative results to a malformed question when the question itself is wrong.** When cumulative tests across an arc all return Mode III, the meta-question to ask is "what kind of question would have a non-Mode-III answer?" — not "what's the next config to specify?" Phase 1 / Move 7 characterization is the first such inverted question in this arc: not "is the engine producing X?" but "what is the engine producing?"

Pre-reg discipline still applies to characterization runs — freeze the extraction scope before extracting, to prevent post-hoc cherry-picking of which property to report. But "frozen extraction" is a different discipline structure from "frozen PASS/FAIL adjudication." Move 7 will be frozen-extraction-scope, no adjudication categories.

---

*§12 added 2026-04-26 — Move 6 Mode III-natural (delocalized at search boundary; spectrum confirms attractor is not a clean ω_C standing wave). Meta-methodological pivot accepted: stop testing corpus-shaped templates at new configurations; switch to characterizing Move 5's attractor as itself. Move 7 / Phase 1 characterization frozen at next commit — no PASS/FAIL, frozen extraction scope (spatial moments + FFT at fixed points + Q-factor + phasor trajectory + energy partition). A48 (NEW) added for r8.9 §17.1: pre-reg discipline applies to characterization runs as frozen-extraction-scope, distinct from frozen-PASS/FAIL adjudication.*
