# 75 — Cosserat sector saturation asymmetry: V·S, T·1 violates Ax 3 in principle, BUT empirically negligible at relevant amplitudes (Diag A Mode I)

**Status:** 2026-04-27. Diag A pre-fix result: **Mode I** per [`P_ax5_cosserat_wave_speed_amplitude_dependence`](../../manuscript/predictions.yaml) frozen at commit `36d6e0d`. Wave-speed drift across the pre-registered amplitude range A ∈ [0.01, 2.0] is **0.06%** — well within the ±5% adjudication tolerance. Engine fix NOT applied per pre-reg Mode I → "Doc 75_ becomes informational; engine fix not needed; Pass 2 not run."

**TL;DR:** The V·S, T·1 saturation asymmetry diagnosed in [`cosserat_field_3d.py:545-587`](../../src/ave/topological/cosserat_field_3d.py#L545) (V_potential gets S factor) vs [`cosserat_field_3d.py:1204-1209`](../../src/ave/topological/cosserat_field_3d.py#L1204) (T_kinetic does NOT) is an in-principle violation of Ax 3 energy conservation. But empirically, the wave-speed drift it predicts is ~50× weaker than the analytical estimate suggested at low-to-moderate amplitudes, and only becomes detectable at A ≥ 4 (per supplementary scan). **Move 11's 5.5% H_cos drift CANNOT be primarily from this mechanism, and the Round 7+8 universal Mode III pattern is NOT explained by V·S, T·1 wave-speed drift.** Both findings need alternative explanations.

**Read after:** [doc 41_ §T2](41_cosserat_time_domain_validation.md), [doc 74_ §15](74_r7_k4tlm_lctank_run_result.md).

---

## 1. The conservation principle

Ax 3 (Effective Action / Hamiltonian flow / unitarity) requires the system's Lagrangian to have time-translation symmetry for total energy to be conserved by Noether. In a saturated medium where saturation factor `S(A²(x,t))` is dynamic, the Lagrangian's coefficients become time-dependent through `S`. For energy conservation to hold, `S` must enter `T` and `V` in a structurally consistent way — typically symmetrically (both ·S, both /S, etc.) so the EOM is just the rescaled bare wave equation.

The plumber-physics restatement: in the LC-tank picture for any wave-bearing sector, **L** (motion-side, inductive) and **C** (rest-side, capacitive) must co-saturate. Saturation can act on the impedance `z = √(L/C)` while preserving the wave speed `v = 1/√(L·C)` if `L → L·g, C → C/g` (similarity transformation). Or saturation can leave both `z` and `v` unchanged if `L → L·g, C → C·g` proportionally. The asymmetric case `L → L·g, C → C·1` (or any unmatched scaling) generally breaks energy conservation when `g(t)` varies dynamically.

AVE's K4-TLM sector satisfies this trivially by lattice geometry: `dx, dt` are fixed lattice parameters, so local `c_local = dx/dt` is amplitude-invariant by construction. The saturation acts on Op14-mediated bond reflection at site boundaries; the per-cell wave speed is preserved.

The Cosserat continuum sector does NOT satisfy this trivially because `G, G_c, K, γ` (rest-side moduli) and `ρ, I_ω` (motion-side inertias) are bulk-defined parameters that can be modulated independently. The implementation chose to saturate moduli but not inertias.

## 2. The engine code violates the symmetric-saturation requirement

Phase 1 audit (read-only of [`cosserat_field_3d.py`](../../src/ave/topological/cosserat_field_3d.py)):

- [`_energy_density_saturated`](../../src/ave/topological/cosserat_field_3d.py#L545) at lines 545–587:
  ```python
  W = (
      (W_cauchy * G + W_micropolar * G_c) * S_eps_sq
      + W_kappa * gamma * S_kappa_sq
      + W_op10 * k_op10
      + W_refl * k_refl
      + W_hopf * k_hopf
  )
  ```
  All Cauchy + micropolar + curvature potential terms multiplied by `S_eps_sq` and `S_kappa_sq` factors → **V_potential saturates as V·S**.

- [`kinetic_energy()`](../../src/ave/topological/cosserat_field_3d.py#L1204) at lines 1204–1209:
  ```python
  K_u = 0.5 * self.rho * np.sum((self.u_dot * mask) ** 2)
  K_w = 0.5 * self.I_omega * np.sum((self.omega_dot * mask) ** 2)
  ```
  with `self.rho = 1.0` (line 760) and `self.I_omega = 1.0` (line 771) as **constants, never modulated**. T_kinetic does NOT saturate.

- [`step()`](../../src/ave/topological/cosserat_field_3d.py#L1228) at lines 1228–1285: velocity-Verlet uses `a_u = -∂E/∂u / ρ`, `a_w = -∂E/∂w / I_ω` with constant `ρ, I_ω` → integrator inherits the asymmetric saturation.

**No compensating mechanism found** in the integrator, PML, or constitutive paths. The asymmetry is structural.

The mathematical prediction:
- `c_T² = G·S/ρ` → `c_T drifts as √S(A²)`
- `c_R² = γ·S/I_ω` → `c_R drifts as √S(A²)`
- `m_Cosserat² = 4·G_c·S/I_ω` → `m_Cosserat² drifts as S(A²)`

For the Diag A wavepacket setup (rotational, `G_c = 0`, `γ = 1`, `λ = 12`, peak amplitude A), the gradient saturation kernel `S_kappa_sq = 1 - |∇ω|²/ω_yield²` predicted ~3-5% c drift at A=2 from the time-averaged `|∇ω|²` over the packet. **Empirical Diag A result: 0.06% drift at A=2.** ~50× weaker than the analytical estimate.

## 3. Diag A pre-fix result — Mode I per pre-reg

[`r8_diag_a_cosserat_wave_speed.py`](../../src/scripts/vol_1_foundations/r8_diag_a_cosserat_wave_speed.py) ran at the engine's unmodified state. Cosserat-only setup, `use_saturation=True`, `G_c = 0` (gapless rotational), `γ = 1`, `ρ = 1`, `I_ω = 1`. Wavepacket via `initialize_gaussian_wavepacket_omega` at `λ = 12`, `σ = 3`, propagating +x, axis=z. 200 timesteps, centroid-tracking polynomial fit for wave speed.

| Amplitude A | v_measured | v / v_low | Drift |
|---|---|---|---|
| 0.01 | 0.791769 | 1.0000 | reference |
| 0.1 | 0.791769 | 1.0000 | 0.0% |
| 0.5 | 0.791765 | 1.0000 | 0.0% |
| 1.0 | 0.791734 | 1.0000 | -0.0% |
| 2.0 | 0.791317 | 0.9994 | **-0.06%** |

**Pre-reg verdict: Mode I.** c is amplitude-invariant within ±5%. Drift across the registered range is 0.06%, two orders of magnitude below the pre-reg's ±5% threshold for Mode II.

H_drift_max remained ~1e-3 across all amplitudes — consistent with velocity-Verlet's expected O(dt²) numerical drift, not a saturation-driven effect.

## 4. Supplementary high-amplitude scan (post-hoc, not pre-registered)

To characterize the asymmetry's amplitude-dependence beyond the pre-registered range, a follow-up scan ran at A ∈ {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0}. Saved at [`r8_diag_a_supplementary_high_amp_results.json`](../../src/scripts/vol_1_foundations/r8_diag_a_supplementary_high_amp_results.json).

| Amplitude A | v_measured | v / v_low | Drift |
|---|---|---|---|
| 1.0 | 0.791734 | 1.0000 | reference |
| 2.0 | 0.791317 | 0.9995 | -0.05% |
| 3.0 | 0.789435 | 0.9971 | -0.29% |
| 4.0 | 0.783545 | 0.9897 | **-1.04%** |
| 5.0 | 0.764435 | 0.9655 | **-3.45%** |
| 6.0 | -0.086672 | (catastrophic) | catastrophic — packet doesn't propagate |
| 8.0 | -0.018418 | (catastrophic) | catastrophic |

The asymmetry IS empirically real: drift becomes detectable at A ≥ 4 and reaches ~3.4% at A = 5 before the wavepacket's local gradient amplitude exceeds `ω_yield` and the system collapses. **But within the pre-registered range A ∈ [0.01, 2.0], drift is sub-percent.**

## 5. Why the analytical prediction was off by ~50×

The Phase 1 prediction estimated that for `λ = 12`, `A = 2`, peak `|∇ω|² ≈ A²·k² = 0.55`, ratio to `ω_yield² = π² ≈ 9.87` gives `S_kappa_sq ≈ 0.945`, predicting a 3% wave-speed drop. Observed: 0.06%.

Possible reasons the empirical effect is so much weaker:
- **Spatial averaging**: the wave packet has Gaussian envelope (σ=3 cells); only a small fraction of the packet's volume sees the peak gradient. The energy-density-weighted average of `S_kappa_sq` is much closer to 1 than the peak-gradient estimate suggests.
- **Time averaging**: the gradient `|∇ω|² = A²·k²·sin²(kx)·envelope²` has a `sin²` factor whose time-average over a wave cycle is 1/2. The instantaneous saturation oscillates; the propagation-relevant effective `S` is the cycle-averaged value.
- **Packet→standing-wave conversion**: as the saturation reduces wave speed locally, the packet partially reflects/diffracts rather than uniformly slowing. Centroid-tracking measures the dominant packet's group velocity, which may be less sensitive to local saturation than the analytical estimate assumed.

Whatever the precise reason, the empirical conclusion stands: **the V·S, T·1 asymmetry's effect on rotational wave-packet speed is negligible at A ≤ 2 and only ~3% at A = 5, far below what's needed to explain Round 7+8's universal Mode III pattern.**

## 6. Implication for Move 11 H_cos drift + Round 7+8 Mode III

Move 11 measured 5.5% H_cos drift over 50 Compton periods at corpus seed (peak |ω| ≈ 0.93 ≈ A=1 in Diag A's amplitude scale). Per Diag A's measurement at A=1: drift is essentially 0. **Move 11's 5.5% H_cos drift CANNOT be primarily from V·S, T·1 wave-speed asymmetry.** Some other mechanism is responsible.

Candidates for the H_cos drift's actual cause:
- **PML coupling**: K4-TLM uses a PML boundary that absorbs wave energy; K4↔Cosserat coupling might be leaking energy through PML in a way that affects only Cosserat's H accounting. Worth checking H_K4 separately and computing H_total.
- **Cosserat self-terms**: `enable_cosserat_self_terms=True` adds Op10, refl, Hopf terms that have their own dynamic evolution; energy in these terms might not be tracked in `total_energy()`'s saturation-consistent way.
- **Numerical drift at the engine's coupled-sector CFL limit**: doc 41 §7 noted 0.8-0.9% Hamiltonian drift with mass-gap modes active; coupled K4+Cosserat at full A26 amplitude could be 6× that for non-saturation reasons.
- **Op14 cross-coupling integrator**: Φ_link accumulator + non-local Op14 z-modulation may have implicit time-integration paths whose conservation properties are non-trivial.

Round 7+8 Mode III pattern: per Diag A, eigenfrequencies don't drift significantly with amplitude in the relevant regime. So the universal Mode III is NOT primarily from "engine's eigenfrequency spectrum drifts with amplitude → fixed-σ eigsolve unreliable." That hypothesis is **falsified** at the amplitudes corpus seed runs at.

The Round 7+8 result stands as it was: the engine genuinely does not produce a (2,3) bound state matching corpus claims at corpus GT geometry, and the reason is NOT V·S, T·1 wave-speed drift. The "natural attractor as itself" characterization (Move 7+7b+10) is still the productive direction.

## 7. The engine fix is queued, not urgent

Per pre-reg Mode I, the fix described in §4 of the original [plan](../../.claude/plans/yes-bring-notes-up-binary-giraffe.md) (`T = ½·(ρ·S)·|u̇|² + ½·(I_ω·S)·|ω̇|²` with corresponding integrator update) is NOT applied in this commit. The asymmetry is structural and worth fixing for cleanness, but:

- It doesn't affect Round 7+8's verdicts (asymmetry's impact is sub-percent at relevant amplitudes)
- The fix introduces non-trivial complexity in the integrator (Verlet with time-varying effective inertia requires care)
- High-amplitude regimes where the asymmetry matters (A ≥ 4) are also regimes where the wavepacket's local gradient is approaching rupture; the saturation kernel itself becomes the dominant nonlinearity, and a clean V·S + T·S vs V·S + T·1 distinction may be moot

Recommendation: queue as engine cleanliness work (E-070 entry), not urgent Round 8 path. If R7.1 / Move 5 / R7.2 reruns are eventually motivated by other physics findings, the engine fix becomes a precondition. For now, no rerun is planned because the V·S, T·1 issue isn't load-bearing for the corpus-electron question.

## 8. Vol 2 Ch 7 reconciliation — reframed

[Vol 2 Ch 7 lines 985-993](../../manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex) explicitly states `c_eff = c_0·√(1-A²)` for the OBSERVABLE wave speed under saturation. The original doc 75_ plan framed this as needing reconciliation with substrate-level v invariance.

With Diag A's Mode I result, the substrate-level v IS approximately invariant in the engine's actual implementation (within sub-percent at A ≤ 2). So Vol 2 Ch 7's `c_eff` statement actually applies to the OBSERVABLE-LEVEL wave speed (refractive-index-slowed waves through saturated media at extreme conditions), and the substrate-level v is approximately preserved in the relevant amplitude range.

The substrate-vs-observable distinction the plan proposed is still valid framing, but the empirical magnitude of the substrate-level deviation is much smaller than the analytical prediction suggested. Vol 2 Ch 7's `c_eff = c_0·√(1-A²)` framing is consistent with the engine's behavior at extreme amplitudes (A ≥ 4 where Diag A confirms drift) but slightly overstates the effect at corpus operating amplitudes (A ≈ 1 where Diag A shows essentially no drift).

## 9. A54 (NEW for r8.10 §17.1)

**A54 — Pre-registered diagnostic falsified an analytical prediction at the relevant amplitude regime; code-level audit was correct in principle but quantitatively misleading.** The Phase 1 audit identified the V·S, T·1 asymmetry in `_energy_density_saturated` vs `kinetic_energy()` at the structural level — confirmed correct. The analytical prediction that the asymmetry would produce `c_T, c_R, m_Cosserat` drifts of ~5% at A=2 was empirically falsified by Diag A: drift is 0.06% at A=2, ~50× weaker than predicted. The error pathway: estimating from peak-gradient instead of energy-density-weighted average over the wavepacket; cycle-averaging factor of 1/2 that wasn't accounted for; possible packet→standing-wave conversion mitigation. **Lesson:** even when a code-level audit is structurally correct, the quantitative predictions about what the asymmetry produces empirically must be tested by a frozen pre-reg before downstream consequences are claimed. Round 7+8 Mode III pattern was suspected to be driven by this asymmetry; Diag A says it's not. Doc 75_'s framing changes from "diagnose+fix → R7.1/Move 5/R7.2 reruns" to "asymmetry is real but doesn't drive Round 7+8; H_cos drift needs alternative cause."

---

*Doc 75_ written 2026-04-27 with Diag A pre-fix result (Mode I per pre-reg) + supplementary high-amp scan (asymmetry detectable at A ≥ 4 only). Engine fix queued as cleanliness work (E-070), not urgent. Round 7+8 closure narrative unchanged from doc 74_ §15 — corpus-electron question stays open at the substrate-natural attractor characterization level. H_cos drift (Move 11) and ρ(T,V)=+0.366 still need an alternative explanation; V·S, T·1 wave-speed asymmetry is empirically ruled out as the primary cause.*
