# 71 — Multi-seed R7.1 eigenmode sweep (corpus-canonical replacement for the retracted Stage 0 basin audit)

**Status:** 2026-04-25. **REFRAMED twice.** §13 frozen pre-registration `P_phase6_eigensolver_multiseed` (commit `c69e79c`) is **provisionally retained but conditioned on [doc 72_](72_vacuum_impedance_design_space.md) design-space sign-off**. Audit flags A (V_inc seed at zero produces decoupled Jacobian) and B (shape correlation against pre-coupling X4a is over-strict) surfaced after §13 commit; doc 72_ resolves both by reframing the operator from Hessian-of-W to Helmholtz wave-eigenmode (§13's "sparse generalized-eigenvalue Jacobian" framing is upstream-incorrect — Helmholtz is the AVE-native wave-equation operator). If doc 72_ §1-§5 sign off cleanly, §13 retracts and is replaced by `P_phase6_helmholtz_eigenmode_sweep`; if not, §13 stays.

**Reframe-1 history (this header):** Originally written as "Stage 0 basin-mapping audit." Self-audit per Grant directive ("review COLLABORATION_NOTES, are you trapped in known patterns?") found the basin-audit framing was a Rule 6 / Rule 8 / Rule 10-corollary violation: gradient-descent on Cosserat W is a SM-style minimization where the corpus-native concept for a bound state is a **standing-wave eigenmode of coupled K4+Cosserat dynamics** (Helmholtz / acoustic-cavity formulation per [doc 67_ §23.4](67_lc_coupling_reciprocity_audit.md#L23)). R7.1's sparse eigensolver IS the corpus-canonical tool; the basin audit reinvented R7.1's scope under a worse framing.

**Reframe per Grant 2026-04-25:**
- §1-§12 below are RETAINED as audit trail and as informational empirical context (TDI flow under W is informative for interpreting "no eigenmode at any seed" outcome, even if it isn't load-bearing for R7.1's go/no-go).
- New §13-§14 below are the **active pre-registration**: multi-seed R7.1 sparse eigensolver sweep with three-mode falsification structure.
- Pre-registration `P_basin_audit_GT_stationarity` (commit `1bc1652`) is **retracted-superseded** in `manuscript/predictions.yaml`, replaced by `P_phase6_eigensolver_multiseed` (§13.4 below).
- Manual r8.7 (other-agent scope) gains **A35** documenting the basin-audit-as-Stage-0 framing as a Rule 6/8/10 violation, family with A22 (inline operators duplicate canonical universals) and A30 (corpus-duality falsification) — same class of corpus-bypassing methodology errors, caught earlier in the cycle this time.

**Read after:** [doc 66_ §16](66_single_electron_first_pivot.md), [doc 67_ §17-§26](67_lc_coupling_reciprocity_audit.md) (especially §23.4 acoustic-cavity / Helmholtz framing), [doc 70_ §7](70_phase5_resume_methodology.md). [STAGE6_V4_HANDOFF.md §R7.1](.agents/handoffs/STAGE6_V4_HANDOFF.md#L885) carries the original Round 7 R7.1 forecast that §13 strengthens.

**Skip to §13 for the active pre-registration.** §1-§12 are preserved as audit trail; their content is no longer load-bearing for Round 7 directly but is informational empirical context.

---

## Original §1 (retained per Rule 12) — Why this WAS framed as Stage 0 precondition

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

## 11. Run result (fresh session 2026-04-25): pre-registration FAILED-TO-EXECUTE

Run executed against frozen pre-registration `P_basin_audit_GT_stationarity` (commit `1bc1652`). Driver halted on the first seed at the A26 contamination guard:

```
── seed: GT_corpus ──
  seed state: R=2.541 r=0.000 c=2 E=3.1438 |ω|_peak=0.3433 S_peak=0.939
AssertionError: A26 GUARD FAILED for seed 'GT_corpus':
  peak |ω|=0.3433 outside [0.8011, 1.0838] (target 0.3π=0.9425).
  Verify amplitude_scale=0.3464 is being applied.
```

The guard worked exactly as designed (per §4) — caught the seed-amplitude mismatch before any downstream interpretation got contaminated. But the root cause is upstream of the seeder, in the **pre-registration's geometry**:

### 11.1 Diagnostic sweep

Direct seeding test at four `(N, R_target, r_target)` regimes, holding `amplitude_scale = 0.3 / (√3/2) ≈ 0.3464` constant:

| N  | R_target | r_target | seeded \|ω\|_peak | R_measured | r_measured | c |
|----|----------|----------|-------------------|------------|------------|---|
| 24 | 2.618 (= φ²)        | 0.382 (= 1/φ²)      | **0.343** (37% of 0.943) | 2.541 | **0.000** | **2** |
| 24 | 8.000               | 3.056 (= 8/φ²)      | 0.917 (97% of 0.943)     | 7.623 | 2.541 | 3 |
| 32 | 12.000              | 4.584 (= 12/φ²)     | 0.931 (99%)              | 12.455 | 4.484 | 3 |
| 80 | 20.000              | 7.639 (= 20/φ²)     | 0.939 (99.6%)            | 20.449 | 7.481 | 3 |

The pattern is unambiguous. At `r_target = 1/φ² ≈ 0.382` lattice cells the hedgehog is sub-lattice — `extract_shell_radii()` cannot resolve the half-max width and returns r=0.000. The crossing-counter sees 2 crossings instead of 3 (winding number undersampled). Peak |ω| is 37% of continuous because the closest available lattice site is ~1.3·r_opt off the continuous peak.

At any N where the geometry is well-resolved (R ≥ ~6 cells, r ≥ ~1 cell), the seeder produces peak |ω| within ~3% of the continuous 0.943 target and the (R, r, c) extractors return sensible values.

### 11.2 Root cause — pre-reg conflated corpus *ratio* with literal cell counts

The corpus claims about Golden Torus geometry are **ratios**: R/r = φ², R·r = 1/4 (in Compton-derived units, not lattice cells). [F17-K v2-v2](../../src/scripts/vol_1_foundations/coupled_s11_eigenmode.py#L234-L242) understood this — it sets `R = 20.0` (well-resolved at N=80) and `r = R / PHI_SQ ≈ 7.64` (well-resolved). The lattice scale is set by lattice considerations; the φ² ratio is what's tested.

[Doc 71_ §6](#6-pre-registered-prediction-p_basin_audit_gt_stationarity) committed `R = φ² ≈ 2.618` and `r = 1/φ² ≈ 0.382` as literal lattice cells. That was wrong. At N=24 those values are sub-lattice. The pre-registration is geometrically incoherent — no lattice resolution can make it run cleanly because the corpus values aren't lattice-cell numbers.

### 11.3 Audit flags from external review re-read in this light

The auditor's **Flag 2** (basin-existence test extended over GT family) flagged the pre-reg scope but didn't catch the geometry bug. The auditor's earlier note about **F17-K endpoint seeds** (*"recommend digging out v2-v2's actual final (R, r) coordinates"*) was hinting at exactly this — F17-K's coordinates are in resolved-lattice units, not corpus literals. I waved that off as "the audit will tell us if ratios are themselves attractors regardless of anchor." The waving-off was wrong: the geometry has to be resolved before any audit question is meaningful.

The discipline lesson is the same as [doc 67_ §17 / A28](67_lc_coupling_reciprocity_audit.md): pre-registration commits must be cross-checked against the actual prior driver inventory before locking. F17-K v2-v2 was right there in the same scripts directory; one grep would have surfaced the (N=80, R=20.0) pattern.

### 11.4 What this resolves and what doesn't

**Resolves:**
- The A26 contamination guard works as designed and is load-bearing for Stage 0. Without it, the audit would have produced numerical results (R★, r★, E★, c★) at sub-lattice geometry that downstream interpreters could mistake for engine-basin findings. Guard fired on step 0; guard is correct.
- Pre-registration `P_basin_audit_GT_stationarity` (commit `1bc1652`) has a methodology bug, NOT a falsified prediction. The pred's three-way failure-mode resolution doesn't apply because the experiment never staged.
- F17-K v2-v2's (R/r=3.40 at N=80, R=20) result is not invalidated. It used the right geometry conventions; my pre-reg used wrong ones.

**Doesn't resolve:**
- The actual basin-mapping question (which Stage 0 was supposed to answer). Pending re-pre-registration at corrected geometry.
- Whether the sub-lattice finding itself is informative. Reading: "Corpus minor radius `1/φ²` is sub-lattice at N=24" is a TRIVIAL finding (it's a unit-conversion artifact, not engine physics). Reading: "Engine basin location can't be tested until geometry is well-resolved" is the methodology-correction lesson. Both are surface findings; neither is the deep finding the audit was meant to produce.

### 11.5 Status of `P_basin_audit_GT_stationarity` (commit `1bc1652`)

Per Rule 12 (*retraction preserves the original body; rationale in section header*): the §6 pre-registration body remains as the audit trail of what was committed. This §11 is the failure-to-execute record. The pred itself is **NOT FALSIFIED** — it cannot be falsified because the experiment didn't stage. Treat it as **methodology-bug retracted, awaiting re-pre-registration at corrected geometry**.

Re-pre-registration scope (pending Grant adjudication, not committed in this turn):
- **Option A — N=24 with resolved geometry:** R=8.0 (well-resolved at N=24), r = 8.0/φ² ≈ 3.06. Same lattice as original pre-reg; new (R, r) anchor. Wall time still ~10-15 min.
- **Option B — N=80 matching F17-K v2-v2:** R=20.0, r ≈ 7.64. Larger lattice; wall time ~1-2 hours per seed (6 seeds → 6-12 hours total). Direct comparability with F17-K v2-v2 endpoints (which then become exact coordinates, not back-derived from ratios).
- **Option C — single-N decision deferred until methodology question resolved:** does the basin location depend on N? If yes (resolution-sensitive), Stage 0 needs a sweep. If no (resolution-independent at well-resolved N), one well-chosen N suffices.

Re-pre-registration also needs to revise the F17-K endpoint seed parameters. As pre-registered, those used `(R=φ², r=φ²/3.40)` and `(R=φ², r=φ²/1.03)` — same sub-lattice issue. They need actual F17-K v2-v2 final coordinates, not back-derived ratios. (This is what the auditor flagged earlier and I waved off.)

---

*Doc 71_ written 2026-04-25 — Stage 0 basin-mapping audit methodology. Strengthened pre-registration per audit Flag 2 (GT-family triplet, not GT_corpus alone). A26 contamination guard per Flag 1 (driver asserts peak |ω| ∈ [0.85, 1.15]·0.3π at step 0). Saturation manifold reporting per TDI subtlety. Round 6 closure framing aligned per Flag 3 (Stage 0 conditions Round 7 Stages 1+2; not retraction of Round 6). Driver scaffold delivered in same commit; run deferred to fresh session per Round 7 discipline.*

*§11 added 2026-04-25 (same fresh session) — run executed against frozen pre-registration; A26 guard fired on first seed (peak |ω|=0.343 vs target 0.943); root cause is pre-registration geometry bug (R=φ² in literal lattice cells is sub-lattice at any reasonable N — corpus values are RATIOS, not cell counts). F17-K v2-v2 already had the right pattern (N=80 R=20). Re-pre-registration at corrected geometry pending Grant adjudication. Pre-reg `P_basin_audit_GT_stationarity` (commit `1bc1652`) is methodology-bug retracted, NOT falsified.*

---

## 12. v2 pre-registration `P_basin_audit_GT_stationarity_v2` (DRAFT — RETRACTED, not committed)

**Retracted 2026-04-25 same fresh session.** §12 was drafted as "fix v1's geometry bug, run again." Self-audit per Grant ("review COLLABORATION_NOTES, are you trapped in known patterns?") found the entire basin-audit framing (v1 + v2) was a Rule 6/8/10 violation. Continuing v2 would be the creeper extending — a fig-leaf in §12 saying "v2 will be cleaner" doesn't change that the question itself is wrong-flavor. v2 NOT committed. The §12 body below remains as audit trail of the methodology iteration that was caught and reframed.

### Original §12 body (DRAFT, NOT EXECUTED) follows:

### 12.1 What changed

Two methodology fixes from v1:

1. **Lattice scale separated from corpus ratio.** v1 conflated R=φ² as both a corpus-ratio claim AND a literal lattice-cell count. v2 picks a lattice anchor `R_anchor` based on lattice-resolution considerations, and tests the **ratio** R★/r★ against corpus φ² (the actual corpus claim).
2. **Predicates on ratios, not absolute cells.** v1's `|R★ - φ²| < 0.10` made sense only if R was literally φ² cells. v2 expresses (a)+(b) in terms of R★/r★ ratio. F17-K consistency-check predicates also expressed as ratios (R/r=3.40 and R/r=1.03 from v2-v2) — which is what F17-K v2-v2 actually reported. Absolute (R★, r★) coordinates of v2-v2 endpoints are not preserved in `coupled_s11_eigenmode.py:_snapshot()` (only S₁₁, c, peak_omega, peak_V, energies tracked); ratio-based consistency check is the only available comparison without re-running v2-v2.

### 12.2 Lattice anchor choice (R_anchor = 6.0 at N=24)

Diagnostic sweep at N=24 with `amplitude_scale = 0.3 / (√3/2)` constant:

| Seed | R_target | r_target | R+r | seeded \|ω\|_peak | A26 guard | (R_meas, r_meas, c) |
|---|---|---|---|---|---|---|
| GT_corpus       | 6.00 | 2.29 | 8.29 | 0.899 | PASS | (5.59, 2.03, 3) |
| GT_perturb_+5%  | 6.30 | 2.41 | 8.71 | 0.903 | PASS | (6.61, 2.03, 3) |
| GT_perturb_-5%  | 5.70 | 2.18 | 7.88 | 0.895 | PASS | (5.59, 2.03, 3) |
| F17K_cos        | 6.00 | 1.76 | 7.76 | 0.872 | PASS | (5.59, 1.52, 3) |
| F17K_s11        | 6.00 | 5.83 | 11.83 | 0.936 | PASS | (5.59, 5.59, 3) |

All six geometries produce peak |ω| within A26 guard window [0.801, 1.084], c=3 preserved at seed, (R, r) extractor returns sensible values. R+r partially exceeds N=24 PML-trimmed alive halfwidth (8 cells from center) on several seeds, but the hedgehog peak |ω| is still clean (lattice partial-clipping doesn't break the seed mechanically — it just truncates the ω field at the alive boundary, which is also how the engine integrates).

`R_anchor=6.0` chosen because: (i) all seeds resolve cleanly, (ii) wall time at N=24 is ~3-5 min total for 6 seeds × 1000 TDI steps, (iii) consistency with v1's lattice scale (no compute re-allocation), (iv) F17-K v2-v2 endpoint geometries (R/r=1.03 horn torus) just-fit at this R, would fail at higher R.

`N=24` retained from v1 (Phase 5 registered config). Larger-N sensitivity sweep is a deferred follow-up.

### 12.3 v2 pre-registered prediction (DRAFT)

> Under TDI mode (`damping_gamma=0.1`, no saturation pin, **N=24, R_anchor=6.0**, central-cell (2,3) hedgehog with `amplitude_scale = 0.3 / (√3/2)` ≈ 0.3464 satisfying A26 contamination guard), the three GT-family seeds converge within 1000 TDI steps to a **common ratio** `(R★/r★)`:
>
> - `GT_corpus`: R_target=6.0, r_target=6.0/φ²
> - `GT_perturb_+5%`: R_target=6.3, r_target=6.3/φ²
> - `GT_perturb_-5%`: R_target=5.7, r_target=5.7/φ²
>
> **PASS criteria (all three required):**
>
> **(a)** All three runs converge to a COMMON ratio:
>   `max(|ratio_i - ratio_j|) < 0.10·φ² ≈ 0.262` over the three runs (10% relative).
>   *Reading:* GT region is a basin (common attractor in ratio space).
>
> **(b)** The common ratio is at corpus GT:
>   `|⟨ratio⟩ - φ²| < 0.10·φ² ≈ 0.262`.
>   *Reading:* engine basin matches corpus φ² ratio.
>
> **(c)** Topology + relaxation:
>   `c★ = 3` preserved in all three runs AND `E★ < 0.5·E_seed` in all three runs.
>   *Reading:* topological sector metastable; substantial relaxation.
>
> **F17-K consistency-check sub-predicates** (diagnostic, not part of headline pass):
>
> - F17K_cos seed (R_target=6, r_target=6/3.40) under TDI → ratio R★/r★ within 10% relative of 3.40 (Cosserat-energy basin per v2-v2).
> - F17K_s11 seed (R_target=6, r_target=6/1.03) under TDI → ratio within 10% relative of 1.03 (coupled-S₁₁ basin per v2-v2).
> - random_low_amp seed → relaxes to E ≈ 0 (vacuum sanity).
>
> **FALSIFICATION (any one of (a), (b), (c) for headline):**
>
> - **(a) fails**: GT region is not a basin in ratio space. ±5% perturbations slide into different ratio attractors. Result reveals local landscape per seed.
> - **(b) fails with (a) passing**: common attractor at a different ratio. F17-K v2-v2's R/r=3.40 (or other) was the engine basin all along. Engine W functional or coefficients need revision before R7.1 linearizes around GT.
> - **(c) fails**: topology not preserved by TDI in c=3 sector. Engine has no metastable c=3 attractor at this resolution.
>
> **Prior, stated honestly:** still expect (b) to fail, for the same reason as v1. F17-K v2-v2's reported R/r=3.40 (energy) and 1.03 (S₁₁) were ratio findings; TDI on full W is a related gradient flow likely to converge to one of those ratios, not corpus φ².

### 12.4 Driver changes for v2

[`phase5_basin_audit.py`](../../src/scripts/vol_1_foundations/phase5_basin_audit.py) update scope (~30-50 LOC delta):

- Replace `(PHI_SQ, INV_PHI_SQ)` literal cell anchors with `R_ANCHOR = 6.0` and derive r from R_anchor / ratio.
- Restate predicates in ratio space: compute `ratio_i = R_meas_i / r_meas_i`, then check `(a)` ratio spread, `(b)` mean ratio vs φ². Tolerances 10% relative.
- Add F17K consistency-check sub-predicate evaluation (informational, not part of headline).
- Update output JSON schema: add `ratio_final` per seed.

A26 guard, TDI integrator, saturation-manifold reporting all unchanged. Wall time ~3-5 min total.

### 12.5 v1 retraction handling

Per Rule 12 (preserve body, update header) — applied to predictions.yaml as well:

- v1 entry `P_basin_audit_GT_stationarity` (commit `1bc1652`): retain in `predictions.yaml`. Update `notes` field to prepend a `RETRACTED (methodology bug)` marker pointing to §11 + §12. Body retained.
- v2 entry `P_basin_audit_GT_stationarity_v2`: new entry below v1 in predictions.yaml. `pre_registered: true`, points to doc 71_ §12 (this section) and updated driver. Treated as the active pred for the next run.

### 12.6 Approval question for Grant

This §12 is a draft. Items requiring sign-off before commit + run:

1. **Lattice anchor R=6.0 at N=24** (vs N=32 R=10 for cleaner geometry margin, vs N=80 R=20 for direct F17-K v2-v2 comparability). My recommendation: R=6.0 at N=24. Rationale above.
2. **Ratio-based predicates** (vs absolute-cell predicates with re-derived tolerances). My recommendation: ratio-based, since corpus claim IS a ratio and lattice quantization adds 0.4-cell noise to absolute (R, r) extractors that ratio measure largely cancels.
3. **v1 retracted-but-retained vs replaced-in-place** in predictions.yaml. My recommendation: retained-with-retraction-marker (audit trail clean).

If all three are go, next step is: update driver, add v2 entry to predictions.yaml, mark v1 retracted, commit as one logical unit ("research(... Stage 0 v2): re-pre-registration at corrected geometry"), then run.

*(End of original §12 draft. v2 NOT executed — see §13 below for the active reframe.)*

---

## 13. RETRACTED — Multi-seed R7.1 sparse eigensolver sweep (Hessian-of-W framing superseded by block Helmholtz per doc 72_)

**Retracted 2026-04-25 same fresh session per Rule 12.** §13 framed R7.1 as "linearize coupled K4+Cosserat dynamics around each seed ansatz, build sparse generalized-eigenvalue Jacobian" — i.e., **Hessian-of-W** eigsolve. External audit on commit `c69e79c` flagged two issues:

- **Flag A:** at V=0 seed, ∂²W/∂V∂ω cross-block of the Hessian vanishes (Op14 is multiplicative in V), decoupling K4↔Cosserat in the Jacobian. Eigsh returns Cosserat-only modes; mode (III) becomes uninterpretable.
- **Flag B:** shape correlation > 0.85 against pre-coupling doc 34_ X4a profile is over-strict — coupling distorts the bound-state shape; valid eigenmodes could fail the conjunction.

Both flags vanish under the **block Helmholtz on (V, ω) joint** framing per [doc 72_ §3.1](72_vacuum_impedance_design_space.md). The deeper finding from doc 72_'s self-audit: Hessian-of-W is a **SM-style minimization** framing on a wave-propagation substrate (Rule 6 violation by the operator choice itself). Helmholtz wave-eigenmode is the AVE-native operator for bound-state analysis; this is concept §1.1 of doc 72_.

§13 body retained below as audit trail of the methodology iteration (per Rule 12). Active pre-registration is now `P_phase6_helmholtz_eigenmode_sweep` per [§15](#15-active--multi-seed-r71-block-helmholtz-eigenmode-sweep-active-2026-04-25). Original §13 follows:

### Original §13 (Hessian-of-W framing, superseded):

### 13.1 Why the basin audit was the wrong question

Per the self-audit findings (header):

- **Rule 6 violation.** TDI gradient descent on Cosserat W is SM-style minimization. The corpus-native concept for a bound state is a standing-wave eigenmode of K4+Cosserat dynamics — found via the Helmholtz / acoustic-cavity formulation per [doc 67_ §23.4](67_lc_coupling_reciprocity_audit.md#L23) + the de-broglie-standing-wave KB leaf in vol2 Ch 7. Not minimization; spectral.
- **Rule 8 inverse violation.** R7.1's sparse eigensolver IS the AVE-native tool. Bypassing it for "basin audit" reinvented R7.1's scope under different (worse) language.
- **Rule 10 corollary.** "Basin audit as Stage 0 precondition" became a creeper compound — accumulated through diagnosis → auditor confirmation (same-source bias) → v1 build → v1 fail → v2 draft, without ever pressure-testing the framing itself against "just run R7.1 at multiple seeds, that IS the precondition."

### 13.2 What the basin audit was *trying* to address

The original concern that motivated Stage 0 was: **R7.1 (per [§R7.1](.agents/handoffs/STAGE6_V4_HANDOFF.md#L885) of STAGE6_V4_HANDOFF) was scoped to linearize at corpus Golden Torus geometry. F17-K v2-v2's R/r=3.40 (Cosserat-energy descent) and R/r=1.03 (coupled-S₁₁ descent) suggest the engine basin isn't at corpus GT.** Linearizing at the wrong basin produces a Jacobian that's not load-bearing for the bound-state question.

The right resolution is NOT a basin audit. It's **strengthening R7.1 to multi-seed from the start**: run the sparse eigensolver at GT, F17K_cos, F17K_s11 in the same session, and read the basin question off the eigenvalue results directly.

### 13.3 Multi-seed R7.1 — three-mode falsification structure

Per Grant directive 2026-04-25:

> Three sharp falsification modes:
> 1. Eigenmode at ω_Compton at GT → corpus vindicated.
> 2. Eigenmode at ω_Compton at F17K endpoints (not GT) → engine basin is the right linearization, corpus geometry was wrong.
> 3. No eigenmode at ω_Compton at any seed → (2,3) representation needs structural rework.

These are mutually exclusive empirical outcomes. R7.1 multi-seed asks the eigenvalue question at three geometries; the answer (which seed, if any, returns an eigenmode at ω_Compton) is the basin-vs-corpus question, the "is GT the right linearization point" question, AND the "does the engine host a (2,3) bound state at all" question, all read off in one run.

### 13.4 Pre-registration `P_phase6_eigensolver_multiseed` (frozen at commit)

Methodology:
- **Sparse eigensolver:** linearize coupled K4+Cosserat dynamics around each seed ansatz, build sparse generalized-eigenvalue Jacobian (`A u = λ B u`) per the Helmholtz form per [doc 67_ §23.4](67_lc_coupling_reciprocity_audit.md#L23).
- **Lattice geometry:** N=32, R_anchor=10. Larger N than the v1/v2 basin audit because the F17K_s11 endpoint at R/r=1.03 needs r ≈ 9.71 cells (won't fit at N=24 alive halfwidth=8); N=32 alive halfwidth ≈ 12 cells accommodates all three seeds. Sparse Jacobian dimension ≈ 6·N³ = 196,608 — tractable for `scipy.sparse.linalg.eigsh`.
- **Seeds:** four total.
  - `GT_corpus`: R=10, r = 10/φ² ≈ 3.82 (corpus-claim ratio R/r=φ²)
  - `F17K_cos_endpoint`: R=10, r = 10/3.40 ≈ 2.94 (F17-K v2-v2 Cosserat-energy descent endpoint ratio)
  - `F17K_s11_endpoint`: R=10, r = 10/1.03 ≈ 9.71 (F17-K v2-v2 coupled-S₁₁ descent endpoint ratio)
  - `vacuum_control`: random low-amplitude (peak |ω|=0.05) — control seed where no (2,3) topology is present; eigensolver should return only trivial / continuum eigenmodes here.
- **Amplitude:** all GT-family seeds use `amplitude_scale = 0.3 / (√3/2) ≈ 0.3464` (A26-corrected) for the (2,3) hedgehog. A26 guard at step 0 (peak |ω| ∈ [0.85, 1.15]·0.3π) per same logic as v1 §4.
- **Eigenvalue target:** seek the lowest 5 eigenvalues `λ` near `ω_Compton²` using `scipy.sparse.linalg.eigsh(A, M=B, k=5, sigma=ω_C², which='LM')`. The `sigma`-shift mode is the standard tool for finding interior eigenvalues near a target.
- **Tolerances:** an eigenmode "exists at ω_Compton" if `|√λ - ω_C| < α · ω_C` (i.e., within fine-structure-constant accuracy per original §R7.1 draft sub-pred). Q-factor extracted from boundary impedance: pass if `|Q - 1/α| / (1/α) < 0.05` (5% relative). Eigenmode shape match to doc 34_ X4a's amplitude-sweep best-amplitude profile: pass if normalized-correlation > 0.85.

**Pre-registered prediction `P_phase6_eigensolver_multiseed`:**

> At least one of {`GT_corpus`, `F17K_cos_endpoint`, `F17K_s11_endpoint`} returns an eigenmode at `ω_Compton ± α · ω_C` with Q-factor `1/α ± 5%` and shape correlation `> 0.85` against doc 34_ X4a profile. `vacuum_control` returns no nontrivial eigenmode in the same window.

**Three-way mode resolution** (which seed succeeds determines the basin question):

- **(I) GT_corpus passes** (with or without F17K endpoints also passing). **Reading:** Corpus Golden Torus geometry is empirically the engine bound-state location at coupled scale. F17-K v2-v2's R/r=3.40 and 1.03 were dynamical-descent artifacts (different objectives, different gradient-flow attractors) but the spectral bound state is at corpus GT. R7.1 vindicated as originally scoped.
- **(II) F17K_cos and/or F17K_s11 passes; GT_corpus fails.** **Reading:** Engine bound state is at the F17-K v2-v2 attractor geometry, NOT at corpus GT. Corpus geometric claim (R·r = 1/4, R/r = φ²) is empirically wrong AT COUPLED-ENGINE SCALE. The engine W functional and its coefficient settings produce a (2,3) eigenmode at a geometry that disagrees with corpus. Major framework-level finding — likely surfaces a load-bearing detail in [doc 34_ §9.4](34_x4_constrained_s11.md) X4a/X4b empirical sweep (Cosserat-only) that's broken under coupling. Engine W or corpus geometry derivation (or both) needs revision.
- **(III) No seed passes.** **Reading:** The (2,3) topological representation as currently implemented in `cosserat_field_3d.py` does not host a bound state at ω_Compton at any tested geometry. Either the (2,3) ansatz is structurally wrong for the electron in this engine (wrong winding, wrong amplitude scaling, wrong field sector — e.g., bound state lives in the K4 V_inc sector instead of Cosserat ω) or the coupled K4+Cosserat dynamics needs additional terms beyond what's currently implemented. Most disruptive outcome; requires Round 8 architectural rework.

`vacuum_control` is the negative-control seed. If it returns a nontrivial eigenmode at ω_Compton (which mode (I)/(II)/(III) all expect it NOT to), the eigensolver itself is broken or the coupled-dynamics linearization captures a continuum mode mistakenly. That's a methodology bug, not a physics finding — re-check sparse Jacobian assembly.

### 13.5 v1 basin-audit results status

Per Grant 2026-04-25: **retained as informational empirical context, not Stage 0 precondition.**

The v1 run executed against the sub-lattice geometry and was halted by the A26 guard before any stationary-point data was collected. So v1 has zero post-step empirical content — it has methodology-failure content (geometry bug surfaced, A26 guard validated). [§11](#11-run-result-fresh-session-2026-04-25-pre-registration-failed-to-execute) records this trail.

If R7.1 multi-seed returns mode (III) (no eigenmode at any seed), one diagnostic move is: revisit the basin-audit *informational* question at corrected geometry (R_anchor=6 or 10 at N=32). What attractor does TDI on full W actually find? That informs the Round 8 rework direction. So the v1 driver remains in the repo as informational tooling — not the Stage 0 precondition, but a useful diagnostic if R7.1 forces Round 8.

### 13.6 r8.7 manual closure note (other-agent scope)

Per session-end discipline (Manual r8.x updates are other-agent's scope per Grant directive 2026-04-25), r8.7 needs to capture:

- §16.1: rows for this commit (rename + reframe + retract v1 + add v2 retraction + add `P_phase6_eigensolver_multiseed` pre-reg)
- §16.3: doc 71 entry update (filename + scope changed from "Stage 0 basin-mapping audit" to "Multi-seed R7.1 eigenmode sweep")
- §17 **A35 (NEW):** basin-audit-as-Stage-0 was a Rule 6/8/10 methodology error. Family with **A22** (inline operators duplicate canonical universals — corpus-bypass at the operator level) and **A30** (corpus-duality falsification — corpus claim of energy ≈ S₁₁ co-locate at GT, falsified empirically at coupled scale). All three are corpus-bypassing errors at different layers; A35 was caught earlier in the cycle (within-session self-audit triggered by Grant directive) than A22 or A30. Methodology lesson: **before scaffolding a "diagnostic precondition" upstream of an existing R7.x stage, grep the corpus for the AVE-native tool that addresses the precondition's question; if it exists, strengthen R7.x's scope rather than building parallel infrastructure.** Multi-seed R7.1 IS the strengthening; basin audit was parallel infrastructure on a creeper framing.

### 13.7 First 3 actions for fresh-session R7.1 implementer

1. **Read this doc §13 in full** (especially §13.4 frozen pre-registration and three-mode resolution). Do NOT read §1-§12 except as audit-trail context — those are retracted scope.
2. **Verify pre-registration `P_phase6_eigensolver_multiseed`** matches in `manuscript/predictions.yaml`. Pre-registration is frozen at commit time; driver must match it.
3. **Build the R7.1 sparse eigensolver driver** — `r7_eigensolver_multiseed.py` (or similar), ~300 LOC per original §R7.1 estimate. Approach: assemble sparse Jacobian by automatic differentiation (`jax.jacrev` of total-W w.r.t. flattened state vector `(u, ω, V_inc, V_ref)`) at each seed; mass matrix is identity for Cosserat sector + impedance-weighted for K4 sector; use `scipy.sparse.linalg.eigsh(A, M=B, k=5, sigma=ω_C², which='LM')`. Then run, evaluate three-mode predicates, write §15 result + adjudication.

---

## 14. SUPERSEDED — Driver scope notes for §13 Hessian-of-W framing (informational, not pre-registered)

**Superseded 2026-04-25** alongside §13 retraction. These driver scope notes were for the Hessian-of-W operator (§13 framing). Active driver scope for the block Helmholtz framing lives in [doc 72_ §5](72_vacuum_impedance_design_space.md). The V=0 decoupling subtlety (which was Flag A under Hessian-of-W) is now documented as the desired V-block + ω-block decomposition behavior in [doc 72_ §3.1.1](72_vacuum_impedance_design_space.md). §14 body retained as audit trail of the Hessian-of-W driver-design iteration.

### Original §14 (driver scope notes for retracted §13 Hessian-of-W framing):


### 14.1 Reuse vs. write-new

Reuse (already in repo, unchanged):
- [`cosserat_field_3d.py:initialize_electron_2_3_sector`](../../src/ave/topological/cosserat_field_3d.py#L777) — A26-corrected (2,3) hedgehog seeder, applies `amplitude_scale` parameter.
- [`cosserat_field_3d.py:total_energy`](../../src/ave/topological/cosserat_field_3d.py#L935) — Cosserat W functional.
- [`vacuum_engine.py:VacuumEngine3D.from_args`](../../src/ave/topological/vacuum_engine.py#L1616) — A28+self-terms engine config.

Write new:
- Coupled K4+Cosserat W (Hopf + Beltrami + chiral-saturation + reflection penalty + K4 wave-energy term). Existing `engine.cos.total_energy()` covers Cosserat sector only; K4 sector needs to be added per [k4_tlm.py](../../src/ave/core/k4_tlm.py) wave-equation Hamiltonian.
- Sparse Jacobian assembly (autodiff via JAX `jacrev`).
- `eigsh` wrapper + boundary-impedance Q-factor extractor.
- Shape-match to doc 34_ X4a profile (correlation metric).

### 14.2 Pitfalls flagged from prior F17-K work

- **A28 + self-terms ARE the post-Round-6 default.** Set `disable_cosserat_lc_force=True` and `enable_cosserat_self_terms=True` in `VacuumEngine3D.from_args`. Legacy defaults are wrong for any post-Round-6 work.
- **K4 amplitude is zero at seed time.** The eigensolver linearizes around a state where Cosserat ω is seeded at hedgehog and K4 V_inc=0. Op14 z_local coupling between K4↔Cosserat is therefore zero in the seed Jacobian (no V_inc to couple). The eigensolver returns Cosserat-only modes at first order. To capture K4-coupled bound modes, the linearization needs to include first-order K4 perturbations explicitly — not zero-amplitude seed.
- **Saturation pin** is OFF (matches v1 §3 reasoning — pin masks the W gradient).
- **A26 guard at step 0** is mandatory (per v1 §4 — caught the geometry bug that started this rabbit hole).

### 14.3 What the run resolves and what stays open

**Resolves once run:**
- The three-mode question above (which seed, if any, hosts the bound state).
- R7.1's linearization-point question for any downstream methodology.
- The basin-vs-corpus geometry empirical question, via mode (I)/(II) split.

**Stays open** (post-R7.1, mode-dependent):
- If mode (I): R7.2 ((2,3)/Hopf injection per G-13) runs at corpus GT geometry; Round 7 closes.
- If mode (II): r8.x reconstruction of corpus geometry derivation; Round 7 closes after corpus revision lands.
- If mode (III): Round 8 architectural rework — likely starting with "where does the bound state live? K4 sector? Coupled non-(2,3) topology? Different field representation?"

*(End of original §13 body — superseded by §14 ACTIVE below.)*

---

## 15. ACTIVE — Multi-seed R7.1 block Helmholtz eigenmode sweep (active 2026-04-25)

Per [doc 72_](72_vacuum_impedance_design_space.md) design-space articulation. The Hessian-of-W framing in §13 is superseded; the AVE-native operator for bound-state analysis is **block Helmholtz on the joint `(V, ω)` state vector**. Active pre-registration is `P_phase6_helmholtz_eigenmode_sweep` (replaces `P_phase6_eigensolver_multiseed`).

### 15.1 Why this isn't reframe 4 / commitment to v2 operator choice

This is **reframe 3** of R7.1 in one session arc (single-seed Hessian → multi-seed Hessian → multi-seed block Helmholtz). Per [doc 72_ §6.1](72_vacuum_impedance_design_space.md): the fresh-session run committed against `P_phase6_helmholtz_eigenmode_sweep` is committed to operator choice. Post-run methodology adjustments are allowed under Rule 10 ("data first, methodology adjustments after"); pre-emptive operator changes before run are not, except for catastrophic methodology error (load-bearing physics error in operator construction itself).

Two prior reframes were both substantive corrections (multi-seed strengthening for Round 7 scoping; block Helmholtz for AVE-native operator). Reframe 4 would be loop continuation; the §6.1 commitment + Rule 10 anchor close that loop.

### 15.2 Quick map of §15 vs §13

| Aspect | §13 (RETRACTED Hessian) | §14 (ACTIVE block Helmholtz) |
|---|---|---|
| Operator | `∂²W/∂(u,ω,V,V_ref)²` Hessian, autodiff via JAX jacrev | Block Helmholtz on (V, ω) joint, direct sparse construction |
| Cross-coupling at V=0 | Vanishes silently → K4↔Cosserat decouple, eigsh returns Cosserat-only modes (Flag A) | Vanishes per §3.1.1 footnote → V-block + ω-block returned simultaneously, sector-energy-split diagnostic reads off "which sector" |
| Bound-state shape | Correlation > 0.85 against pre-coupling X4a (over-strict, Flag B) | `c_eigvec = 3` binary PASS + shape correlation > 0.60 informational (Q4 two-tier) |
| Visualization | (R, r) sweep returning {ω_n} | 3D Smith chart Extension A `(Re(Γ), Im(Γ), ω)` per doc 72_ §2.1 |
| LOC | ~300 | ~290 |
| Pred | `P_phase6_eigensolver_multiseed` (commit `c69e79c`, retracted) | `P_phase6_helmholtz_eigenmode_sweep` (this commit) |

### 15.3 Read order for fresh-session R7.1 implementer

1. **[Doc 72_](72_vacuum_impedance_design_space.md) in full** — methodology + commitment language + operator framing. §6.1 reframe-3 commitment is load-bearing.
2. **§14 of this doc** — quick orientation that §13 is superseded; §14's pred is active.
3. **`P_phase6_helmholtz_eigenmode_sweep` in `manuscript/predictions.yaml`** — frozen pre-registration. Build to match it; halt-and-flag if deviation surfaces, do NOT modify the pred.
4. **Build driver `r7_helmholtz_eigenmode_sweep.py`** (~290 LOC per doc 72_ §5).
5. **Run + interpret** against three-mode falsification (mode I / II / III) plus sector-energy-split (V-dominant / hybrid / ω-dominant) plus shape correlation informational. Empirical data first; if unexpected, analyze data before considering methodology revision.
6. **Write doc 72_ §9 result + adjudication** (or new doc 73_ if appropriate).

### 15.4 What §13 retains (for audit-trail readers)

§13's body retains all the multi-seed scoping logic, three-mode falsification structure, lattice geometry choice, A26 contamination guard, and seed list — all of which carry over to §14 unchanged. The retraction is specifically about **operator choice** (Hessian-of-W → block Helmholtz). Everything else built on §13 is reusable.

---
