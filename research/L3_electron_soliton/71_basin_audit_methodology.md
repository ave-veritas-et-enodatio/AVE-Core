# 71 — Stage 0 basin-mapping audit: empirical characterization of W functional stationary states

**Status:** 2026-04-25. Round 7 Stage 0 precondition. Per session-end audit and Grant directive ("audit the engine first, we need to understand what we are doing at every level"), characterizes the actual stationary states of the engine's Cosserat W functional under TDI mode before R7.1/R7.2 commit to Golden Torus as the linearization point.

**Read after:** [doc 66_ §16](66_single_electron_first_pivot.md), [doc 67_ §17-§26](67_lc_coupling_reciprocity_audit.md), [doc 70_ §7](70_phase5_resume_methodology.md). [STAGE6_V4_HANDOFF.md §R7](.agents/handoffs/STAGE6_V4_HANDOFF.md) carries the Round 7 forecast that this Stage 0 conditions.

---

## 1. Why this is the Stage 0 precondition

Five independent empirical findings across Round 5–6 + Phase 5 resume converge on the same observation:

1. **F17-K v2-v2** (commit `4c9fbea`): dual descent under saturation pin converges at R/r=3.40 (Cosserat-energy) and R/r=1.03 (coupled S₁₁) — neither at corpus Golden Torus φ²=2.62.
2. **F17-K v3 (i)** (commit `3fede52`): X4b linear-stability test at GT seed — perturbation grows 5.3× over 30 iters under coupled S₁₁ (UNSTABLE), 1.81× under Cosserat-energy (MARGINAL). GT is not a stable fixed point of either descent direction at coupled scale.
3. **Phase 5 case (b')** (commit `ede4008`): point-rotation Beltrami pair seed dissolves 93% in ONE Velocity-Verlet step regardless of drive presence. Engine self-dynamics scatter the seed without external forcing.
4. **doc 66_ §16 / line 489**: TDI test with `damping_gamma=0.1` and Cosserat-only (2,3) seed at peak |ω|=0.3π — same step-1 catastrophic energy loss as without damping; 800-step chaotic decay; brief transit through (2,3)-preserving high-Γ² configuration at step 5 but system leaves it; never settles.
5. **Round 6 closure framing**: "topology is encoded by ansatz initialization (doc 34_ X4 pattern), not by dynamical descent." Empirically validated at multiple levels.

These are five views of one underlying phenomenon: **the corpus-canonical ansatz patterns (Golden Torus geometry, (2,3) hedgehog, point-rotation Beltrami) are not stationary states of the engine's discretized W functional.** The engine's W has stationary states — somewhere — but they have never been empirically characterized.

Round 7 Stage 1 (sparse eigensolver linearization around GT) and Stage 2 ((2,3)/Hopf injection at GT-geometry endpoints) both implicitly assume corpus GT IS the engine basin. If it isn't, both stages scaffold on a different basin than they think. Stage 0 closes that gap empirically before either stage commits.

## 2. What "stationary state" means here

The engine's Cosserat W functional ([cosserat_field_3d.py:512](../../src/ave/topological/cosserat_field_3d.py#L512)) is the integrand of total_energy() — Hopf + Beltrami + chiral-saturation + reflection-penalty contributions. A stationary state of W is a configuration `(u★, ω★)` satisfying both:

```
∂W/∂u  = 0   at (u★, ω★)
∂W/∂ω  = 0   at (u★, ω★)
```

Stationary points are basin minima (stable equilibria) OR saddles (unstable equilibria). Basin-mapping distinguishes the two via **convergence behavior under TDI gradient flow**: a basin attracts trajectories from a neighborhood; a saddle does not.

What corpus claims about stationary states (load-bearing for R7.1/R7.2):
- doc 03_ §4.3: "R·r=1/4: topologically quantized, NOT dynamically derived... the Lagrangian must be *consistent with* but does not by itself produce." Reading: GT is consistent with W stationarity but isn't the unique attractor.
- doc 34_ X4a/X4b: empirical Cosserat-only sweep finds bound state at peak |ω|=0.3π near GT. Reading: bound state exists in Cosserat-only sector at GT — but coupled engine introduces additional terms (K4 sector, reflection penalty under self-terms) that may move stationarity.

## 3. Methodology — TDI gradient flow

The Cosserat integrator at [cosserat_field_3d.py:1228-1284](../../src/ave/topological/cosserat_field_3d.py#L1228) supports two modes:

- **Pure VV** (`damping_gamma = 0`, default): energy-conserving Velocity-Verlet on (u, ω). System oscillates around equilibrium configurations. Cannot identify stationary points — energy is conserved, so trajectories are level-set bounded.
- **TDI** (`damping_gamma > 0`): adds multiplicative velocity decay `decay = max(0, 1 - γ·dt)` after the second-half-kick. Bleeds kinetic energy and settles toward Hamiltonian-stationary states. The right tool for basin-mapping.

Auditor TDI subtlety (incorporated): under SiLU saturation kernel (Ax4), TDI may settle on the saturation manifold (sites at S < 0.95) rather than off it (S > 0.95 indicating uniform-non-saturated). Both are valid stationary points but represent different physical regimes. The driver records local saturation `S = √(1 - A²)` at convergence and labels each basin "free" (S★ > 0.95) or "manifold-bound" (S★ < 0.95). Reporting clarity, not methodology objection.

Reasoning that TDI is the right tool, despite doc 66_ §16's negative result with γ=0.1: that prior test interpreted "system never settles" as falsifying the bound state. The basin audit reinterprets the same dynamics as REVEALING the W landscape — wherever the system flows under TDI is where the stationary points (or attractor manifolds) are. "Doesn't settle to GT" is itself a basin-map result.

## 4. A26 contamination guard (audit Flag 1)

`initialize_electron_2_3_sector` ([cosserat_field_3d.py:777](../../src/ave/topological/cosserat_field_3d.py#L777)) ships with `amplitude_scale = 1.0` default, which corresponds to canonical `√3/2·π ≈ 2.72` peak — the static Regime II/III boundary. Bound state per doc 34_ §9.4 lives at peak `|ω| = 0.3π ≈ 0.942`. Default amplitude is wrong for any audit interpreting "GT seed" as "GT bound-state amplitude."

The fix is in the codebase: pass `amplitude_scale = 0.3 / (np.sqrt(3.0) / 2.0) ≈ 0.3464` to recover peak `|ω| = 0.3π`.

Driver guard (belt-and-suspenders): immediately after seed initialization and before the first integrator step, the driver computes `peak_omega = max(|ω|)` over the lattice and asserts `0.85 · 0.3π < peak_omega < 1.15 · 0.3π` (within 15% of target). If the assertion fails, the driver halts with a clear error message naming A26. This makes the seed-amplitude precondition explicit and machine-checkable. Any audit interpretation that depends on "GT seed at correct amplitude" is then immune to silent A26 contamination.

(Note: r8.6 manual table lists A26 fix as "uncommitted in working tree" — that's stale; `amplitude_scale` parameter is committed. Separate finding for r8.7.)

## 5. Seed sweep design

Six seeds cover three orthogonal questions:

| Seed | (R, r) target | c | Question tested |
|---|---|---|---|
| `GT_corpus` | `(φ², 1/φ²)` ≈ `(2.618, 0.382)` | 3 | **Headline pred (a, b, c).** Does GT family converge to a common basin, and is that basin at corpus GT? |
| `GT_perturb_+5%` | `(1.05·φ², 1.05/φ²)` | 3 | **Basin existence (a).** Does +5% pull back toward GT_corpus's attractor? |
| `GT_perturb_-5%` | `(0.95·φ², 0.95/φ²)` | 3 | **Basin existence (a).** Does -5% pull back toward GT_corpus's attractor? |
| `F17K_cos_endpoint` | `(R, r) such that R/r=3.40` matching v2-v2 | 3 | **Consistency check.** Does TDI from this seed converge consistent with v2-v2's Cosserat-energy descent endpoint? |
| `F17K_s11_endpoint` | `(R, r) such that R/r=1.03` matching v2-v2 | 3 | **Consistency check.** Does TDI from this seed converge consistent with v2-v2's coupled-S₁₁ descent endpoint? |
| `random_low_amp` | uniform random ω, peak 0.05 | 0 | **Vacuum sanity.** Does the lattice relax to E=0 trivial vacuum from sub-saturation noise? |

For each seed, run TDI to convergence (`ΔE/E < 1e-6` AND `|velocity| < 1e-3` over a 50-step window) or 1000-step cap, whichever first.

The (R, r) parameterization for F17-K endpoints reads from F17-K v2-v2 final state (extract via [coupled_self_saturation.py](../../src/scripts/vol_1_foundations/coupled_self_saturation.py) recorded values), not re-derived from scratch — this is a consistency check, so use what F17-K reported.

## 6. Pre-registered prediction `P_basin_audit_GT_stationarity`

**Strengthened per audit Flag 2** (basin-existence test extended over GT family, not just GT_corpus alone):

> Under TDI mode (`damping_gamma=0.1`, no saturation pin, N=24, central bond, `amplitude_scale = 0.3 / (√3/2)` ≈ 0.3464 satisfying A26 guard), the three GT-family seeds {`GT_corpus`, `GT_perturb_+5%`, `GT_perturb_-5%`} all converge within 1000 TDI steps to a stationary point `(R★, r★)` such that:
>
> **(a)** All three runs converge to a COMMON `(R★, r★)`:
>   `max(|R_i - R_j|) < 0.10·φ²` AND `max(|r_i - r_j|) < 0.05/φ²` over the three runs.
>   *Reading:* the GT region is a basin (common attractor), not a ridge.
>
> **(b)** The common attractor lies at corpus GT:
>   `|R★ - φ²| < 0.10` AND `|r★ - 1/φ²| < 0.05`.
>   *Reading:* engine basin matches corpus.
>
> **(c)** Topology + relaxation:
>   `c★ = 3` preserved in all three runs AND `E★ < 0.5 · E_seed` in all three runs.
>   *Reading:* topological sector is metastable; substantial energy relaxation occurred (not a saddle escape to vacuum).

**Falsification — three-way mode resolution:**

- **(a) fails** (seeds diverge to different attractors): the GT region is not a basin. Either it's a ridge between multiple basins (each ±5% perturbation slides into a different attractor) or fragmented landscape. Result reveals the actual local attractor structure for each starting point.
- **(b) fails with (a) passing** (common attractor exists, but at a different `(R★, r★)`): the engine has a basin near GT, but it's NOT at corpus GT. F17-K v2-v2's R/r=3.40 (or some other point) was the actual basin all along. Engine W functional or its coefficient settings need revision before R7.1 linearizes around GT. **This is the prior-expected outcome**.
- **(c) fails** (`c★ = 0` or `E★ ≥ 0.5·E_seed`): topology not preserved by TDI in c=3 sector — matches doc 66_:489 framing. Indicates W has no metastable c=3 attractor at this resolution; engine cannot host a (2,3) bound state without external pinning.

**Prior, stated honestly:** expect (b) to fail. F17-K v2-v2 already established R/r=3.40 (Cosserat-energy descent) and R/r=1.03 (coupled-S₁₁ descent) as Cosserat / coupled descent endpoints. TDI on the full W is a related gradient flow; the most likely outcome is convergence toward one of those points or a nearby one, NOT corpus GT. If so, the actual attractor location is the Stage 0 headline finding and Round 7 Stages 1+2 re-frame against it.

## 7. Driver scope

[`phase5_basin_audit.py`](../../src/scripts/vol_1_foundations/phase5_basin_audit.py) — ~200 LOC.

Per-seed flow:
1. Build `VacuumEngine3D` (N=24, pml=4, T=0, A28 + self-terms enabled, no drive sources).
2. Set `engine.cos.damping_gamma = 0.1` (TDI mode).
3. Initialize ω via `initialize_electron_2_3_sector(R_target, r_target, amplitude_scale=0.3464)` for GT-family seeds; bespoke seeders for F17-K endpoints + random vacuum.
4. **A26 guard:** assert peak |ω| ∈ [0.85·0.3π, 1.15·0.3π] for GT-family seeds. Halt with clear error if violated.
5. Record initial state: (R₀, r₀, c₀, E₀, |ω|_peak,0, S_peak,0).
6. Run TDI loop. Record (R(t), r(t), c(t), E(t), |ω|_peak(t), S_peak(t)) every 10 steps.
7. Convergence check every 50 steps: ΔE/|E| < 1e-6 over the last 50 steps AND max(|u_dot|, |omega_dot|) < 1e-3.
8. Cap at 1000 steps if not converged.
9. Output: per-seed JSON with full trajectory + final state + convergence flag + saturation label ("free" vs "manifold-bound").

Aggregate flow:
1. Run all 6 seeds sequentially.
2. Build summary table: seed name | (R★, r★) | c★ | E★/E₀ | converged? | saturation label | basin pull-distance from start.
3. Evaluate falsification predicates (a)+(b)+(c) for the GT-family triplet → final PASS/FAIL with reason.
4. Emit ASCII summary to stdout + write `phase5_basin_audit_results.json` next to driver.
5. (Optional plot deferred to fresh-session interpreter — output JSON is sufficient for adjudication.)

Wall time estimate: 6 seeds × 1000 TDI steps × ~1.5 min/seed ≈ 10–15 min on N=24, single-process.

## 8. What this resolves and what stays open

**Resolves:**
- Empirical answer to "where are the engine W functional's stationary states?" — at least near the GT-family + F17-K-endpoint regions of (R, r) space.
- Whether corpus GT is a basin minimum, saddle, or non-stationary in the engine's discretization at N=24.
- Calibrates downstream R7.1 (linearization point) and R7.2 (injection target geometry) against actual engine basins.

**Stays open** (deferred follow-ups, not in this Stage 0 scope):
- **Saturation-pin variant.** F17-K v2-v2 used `_project_omega_to_saturation` after every step. This audit deliberately omits the pin to isolate the W gradient flow. If the no-pin result differs substantively from v2-v2's pinned result, the pin is itself a creeper hypothesis and warrants a separate test.
- **Multi-bond seeds.** Audit is single-bond, central-cell. Pair-injection seeds + multi-soliton seeds are R7.2 territory.
- **Larger N / resolution sensitivity.** Audit at N=24. If basin location drifts substantially with N, that's a discretization finding; deferred to a separate resolution-sweep audit.
- **A31 — F17-K Phase 6 sparse eigensolver methodology.** The audit *characterizes* the basin; the eigensolver *linearizes around* a basin. R7.1 follows this audit; eigensolver chooses a real basin to linearize at, not a presumed one.
- **r8.7 manual closure.** Other-agent scope.

## 9. Stage relationship to Round 6 closure (audit Flag 3 framing)

Round 6 closed the **single-electron + pair-injection methodology characterization arc**: the corpus-canonical seeds (Golden Torus, (2,3) hedgehog, point-rotation Beltrami) dissolve under engine self-dynamics → topology must be encoded as ansatz, not derived dynamically. That conclusion is intact and not reopened by Stage 0.

Stage 0 is **upstream** of R7.1/R7.2 — it asks the WHICH-BASIN question that both stages presuppose. The Round 6 finding "corpus seeds dissolve under self-dynamics" generalizes to "corpus seeds are off-stationary in the engine's W"; Stage 0 maps where the actual stationary points are. Not "Round 6 wasn't really closed" — rather "Round 7 needs one more empirical anchor before linearization-or-injection commits to GT geometry."

The r8.7 manual entry should frame this as **Round 7 Stage 0 scoping the precondition for Stages 1+2**, distinct from Round 6 closure.

---

## 10. First 3 actions for fresh-session interpreter

1. **Read this doc in full** (especially §6 pre-registered prediction and §8 falsification mode resolution).
2. **Verify the driver matches the pre-registration** — driver argument defaults must match §3 (γ=0.1, N=24, no pin, A26 guard) and §6 tolerances. Pre-registration is frozen at commit time; driver must match it, not the reverse.
3. **Run the driver** (`python src/scripts/vol_1_foundations/phase5_basin_audit.py`). Expected wall time 10–15 min. Per-seed convergence flags + falsification predicates emitted to stdout. JSON output recorded for the result interpretation step.

After run: add §11 result + adjudication to this doc. If (b) fails (prior-expected), name the actual `(R★, r★)` and update [STAGE6_V4_HANDOFF.md §R7.1](.agents/handoffs/STAGE6_V4_HANDOFF.md#L885) (eigensolver linearization point) + §R7.2 (injection target geometry) accordingly.

---

*Doc 71_ written 2026-04-25 — Stage 0 basin-mapping audit methodology. Strengthened pre-registration per audit Flag 2 (GT-family triplet, not GT_corpus alone). A26 contamination guard per Flag 1 (driver asserts peak |ω| ∈ [0.85, 1.15]·0.3π at step 0). Saturation manifold reporting per TDI subtlety. Round 6 closure framing aligned per Flag 3 (Stage 0 conditions Round 7 Stages 1+2; not retraction of Round 6). Driver scaffold delivered in same commit; run deferred to fresh session per Round 7 discipline.*
