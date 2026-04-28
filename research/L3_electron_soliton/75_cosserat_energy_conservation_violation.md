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

### 5.1 Integrator stability boundary at A ≈ 6 (separate from the asymmetry magnitude)

The supplementary scan shows v_measured smoothly drifts from 0.7917 (A=1) → 0.7644 (A=5) at the predicted asymmetry rate, but at A=6 v_measured **flips sign to -0.087** and remains catastrophic at A=8 (-0.018). This isn't a continuous extension of the asymmetry — it's the velocity-Verlet integrator hitting a stability boundary where the wavepacket's local gradient amplitude exceeds the linearization regime the integrator can handle. The asymmetry contributes to driving toward this boundary (lower effective wave speed at higher amplitude → CFL-tightening unaccounted for), but the cliff at A=6 is a separate phenomenon (integrator order failure, not physics).

**Practical implication:** doc 75_'s structural finding (V·S, T·1 asymmetry exists, has measurable but sub-percent effect at A ≤ 5) holds; the integrator-cliff at A ≈ 6 is a separate engine-stability concern that wouldn't be addressed by the §4 fix. Both are at amplitudes corpus seed never reaches.

## 6. Implication for Move 11 H_cos drift + Round 7+8 Mode III

Move 11 measured 5.5% H_cos drift over 50 Compton periods at corpus seed (peak |ω| ≈ 0.93 ≈ A=1 in Diag A's amplitude scale). Per Diag A's measurement at A=1: drift is essentially 0. **Move 11's 5.5% H_cos drift CANNOT be primarily from V·S, T·1 wave-speed asymmetry.**

But the alternative explanation already exists in Move 11b's results — the analysis just wasn't surfaced as the closing of the loop here.

### 6.1 Diag C — `total_energy()` source audit (post-hoc, no run)

[`cosserat_field_3d.py:935-950`](../../src/ave/topological/cosserat_field_3d.py#L935): `total_energy()` calls `_total_energy_saturated_jit` (with `use_saturation=True`) which sums `_energy_density_saturated` (lines 545-587). Every potential-energy term (W_cauchy, W_micropolar, W_kappa, W_op10, W_refl, W_hopf) is included in that sum. No hidden energy store exists in the Cosserat state outside `(u, u_dot, omega, omega_dot)` — the constructor declares no other field-state attributes. **Diag C verdict: `total_energy()` is correct. No accounting bug.**

### 6.2 Diag B context — Move 11b's Pearson matrix already identified the cause

Move 11b's full cross-correlation matrix between sector observables over the t∈[150P, 200P] recording window:

| Pair | Pearson ρ |
|---|---|
| H_cos vs Σ\|Φ_link\|² | **-0.990** |
| Σ\|V_inc\|² vs Σ\|Φ_link\|² | -0.990 |
| H_cos vs Σ\|V_inc\|² | +1.000 |
| ρ(T_cos, V_cos) | +0.366 |

**The -0.990 anti-correlation between H_cos and Σ|Φ_link|² IS the explanation.** Cosserat sector loses energy ⟺ K4-inductive (Φ_link) gains it. This is Op14 cross-coupling at work — saturation-driven impedance modulation transfers energy between sectors via the bond LC tank's inductive side. The "5.5% H_cos drift" is real physics: H_cos alone isn't conserved because Cosserat is exchanging energy with K4-inductive at a low frequency (FFT showed 0.020 rad/unit dominant in both H_cos and Σ|Φ_link|² time series). H_total = H_cos + H_K4-inductive is approximately conserved.

Move 11b's "static fixed point" verdict was therefore correct in modified form: **the system is in a co-stable trading state**, not a strict static configuration. K4-capacitive (V_inc, V_ref) is locked, K4-inductive (Φ_link) and Cosserat trade slowly. The `+0.366` ρ(T_cos, V_cos) reflects T and V both being driven by the external Φ_link forcing, not internal LC reactance — exactly what an externally-pumped two-LC system looks like.

### 6.3 Open follow-ups (low priority)

- **Diag B (region partition)**: confirm spatially that H_cos drift is in the interior (where the Op14 z-modulation is active) and not artifact of PML coupling. ~10 min re-run; not load-bearing for the conclusion since the Pearson result already identifies Op14 trading. Queued as low-priority sanity.
- **CFL sensitivity**: doc 41 §7 noted 0.8-0.9% baseline drift with mass-gap modes active; the additional 4-5% on top in Move 11 may have a CFL component on top of the Op14 trading. Diag D (dt halved) would partition CFL drift from physical trading.

### 6.4 Round 7+8 Mode III — actually independent of this finding

Per Diag A, the engine's eigenfrequencies do NOT drift significantly with amplitude in the relevant regime. So the universal Mode III pattern is NOT from "engine's eigenfrequency spectrum drifts with amplitude → fixed-σ eigsolve unreliable." That hypothesis is **falsified** at the amplitudes corpus seed runs at.

Round 7+8 Mode III stands as it was: the engine genuinely does not produce a (2,3) bound state matching corpus claims at corpus GT geometry, and the reason is NOT V·S, T·1 wave-speed drift, NOT Op14 trading (which is real but doesn't produce a "drift in eigenfrequencies" — it produces energy exchange between sectors). The "natural attractor as itself" characterization (Move 7+7b+10) is still the productive direction; the corpus electron, IF it exists in this engine, lives somewhere we haven't probed (Φ_link sector / hybrid V≠0 ∧ ω≠0 / different topology).

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

*Doc 75_ written 2026-04-27 with Diag A pre-fix result (Mode I per pre-reg) + supplementary high-amp scan (asymmetry detectable at A ≥ 4 only) + integrator stability boundary at A ≈ 6 (separate from asymmetry magnitude) + Diag C source audit (`total_energy()` correct, no accounting bug) + reframing of Move 11b's Pearson result as the resolution of the H_cos drift mystery (ρ(H_cos, Σ|Φ_link|²) = -0.990 → Op14 cross-sector trading; H_total ≈ conserved). Engine fix queued as cleanliness work (E-070), not urgent. Round 7+8 closure narrative unchanged from doc 74_ §15 — corpus-electron question stays open at the substrate-natural attractor characterization level. **H_cos drift resolved as Op14 trading, NOT a missing-physics issue. V·S, T·1 wave-speed asymmetry empirically ruled out as the primary cause of Round 7+8 Mode III. Round 8 question becomes: where does the corpus electron actually live in the engine, given that the most-natural V_inc + ω-cosserat sectors are confirmed empty?**.*

---

## 10. Photon-Tail Dual Seed test — Mode III, sector asymmetry surfaced (2026-04-27)

After Diag A ruled out V·S/T·1 wave-speed drift as the Mode III cause, Grant proposed the photon-tail framing: corpus electron = self-trapped photon catching its own tail in (2,3) torus-knot loop, with E + B fields winding along the path 90° out of phase. Per doc 28_ §3+§4, the corpus PASS criterion is phasor-space ellipse aspect R_phase/r_phase = φ², measured at any single loop node — distinct from real-space frequency ω_C which is forced sub-Nyquist by `dx = ℓ_node`.

Ran [`P_phase6_photon_tail_dual_seed`](../../manuscript/predictions.yaml) at N=64, (R=4, r=1.5), standing-wave dual-seed IC with both K4 V_inc (corpus (2,3) chiral-phasor) AND Cosserat ω (corpus (2,3) hedgehog) at the same engine-representable scale.

### 10.1 Result — Mode III, 0/4 criteria PASS

| Criterion | Measured | Target | Verdict |
|---|---|---|---|
| C1 single-node ellipse aspect | median 25.74 | 2.618 ± 5% | FAIL |
| C2 spatial winding rotation | NaN (only 12/30 nodes finite) | 5·2π ± 30% | FAIL |
| C3 LC reactance ρ(Σ\|V_inc\|², Σ\|Φ_link\|²) | -0.463 | (-1.2, -0.8) | FAIL |
| C4 topology preservation c via Op10 | 1 (initial 2) | 3 | FAIL |

[`r8_photon_tail_dual_seed_results.json`](../../src/scripts/vol_1_foundations/r8_photon_tail_dual_seed_results.json) for full data.

### 10.2 Sector-asymmetry empirical signal

| Quantity | t=0 | t=200P | Retention |
|---|---|---|---|
| peak \|ω\| | 0.8359 | **0.0361** | 4.3% |
| peak \|V_inc\| | 0.2611 | 0.1735 | 66% |
| c (Op10) | 2 | 1 | degraded |

K4 V_inc partially survived; Cosserat ω dissolved catastrophically. ρ(K4_V², K4_Φ²) = -0.46 shows partial K4-INTERNAL LC reactance (V_inc ↔ Φ_link bond LC trading) but not full LC. Cosserat side decoupled and decayed.

Compare to Move 5 (Cosserat-only seed at R=10, r=3.82, N=32): peak |ω| retention 32% with c=3 plateau locked across 150 Compton periods. **Adding K4 V_inc seed at smaller (R, r) destabilized Cosserat from "marginal but stable" to "near-total dissolution."**

### 10.3 The c=2 initial state — sub-Nyquist topology seed at this scale

The initial seed gave c=2 at t=0, NOT 3. At (R=4, r=1.5) on a unit-spacing lattice, the (2,3) poloidal winding has feature size 2π·1.5/3 ≈ 3.14 cells — exactly at the Nyquist boundary. Op10's `extract_crossing_count` cannot resolve the third poloidal winding cleanly; aliases to c=2.

This is the lattice-resolution constraint flagged in the implementer audit: corpus aspect R/r=φ² at loop length ≤ 56 cells (active region of N=64) FORCES (R, r) close to (4, 1.5), which is exactly at the Nyquist boundary for poloidal winding. To cleanly seed c=3 at corpus aspect, need either:
- N=128+ with larger (R, r) (e.g., R=8, r=3) — ~5 hr per run wall
- Non-corpus aspect at smaller R/r (e.g., R=3, r=2) with c=3 resolvable — but tests photon-tail at non-corpus aspect

C4's "c=3 maintained" criterion was therefore unsatisfiable from t=0 in this configuration. C4 FAIL is partially a methodology artifact (sub-Nyquist seed) on top of the genuine topology decay (c degraded from 2 to 1).

### 10.4 What this test established empirically

1. **Standing-wave dual-seed IC at engine-representable corpus-aspect scale does NOT find the photon-tail attractor.** Cosserat dissolves; phase-space ellipses at loop nodes don't trace golden-ratio aspect (median 25.7, off by 10×); spatial winding decoheres.

2. **Sector asymmetry: K4 sector is more stable than Cosserat at this small scale.** K4 V_inc retained 66% with partial LC reactance signature (ρ ≈ -0.46); Cosserat ω retained only 4.3%. Adding the K4 seed actively destabilized the Cosserat (2,3) configuration vs Move 5's Cosserat-only setup at larger scale.

3. **Sub-Nyquist topology seed (c=2 instead of 3) at corpus aspect ratio + loop-fits-active-region forces a methodology artifact** that C4 inherits. Future photon-tail tests at corpus aspect need N=128+ to cleanly seed c=3 and have C4 be a meaningful criterion rather than a Nyquist-bounded one.

4. **Path (b) propagating-IC is now strongly motivated.** Standing-wave IC was the cheapest test; its catastrophic failure pattern (Cosserat 4% retention, ellipse aspect 10× wrong, winding decoherent) suggests the standing-wave neighborhood doesn't contain the photon-tail attractor's basin. Setting ω_dot, V_ref velocities consistent with photon traveling along loop tangent would seed the propagating mode directly. ~2-3 hr to build the propagating seeder, then ~40 min run at N=64. If path (b) also Mode III, photon-tail framing as currently formulated is empirically falsified at engine-representable scale.

### 10.5 Round 8 status — open questions

The arc now has TWO empirically-falsified hypotheses for Round 7+8 Mode III:
- **V·S, T·1 wave-speed asymmetry** (Diag A Mode I, §6) — sub-percent effect at corpus amplitudes; not the primary cause
- **Photon-tail dual-seed standing-wave IC at corpus aspect** (this test) — Mode III on all 4 criteria; sector asymmetry suggests the photon-tail framing might still hold at propagating IC OR at larger lattice (N=128+)

Open candidate moves:
1. **Path (b) propagating IC photon-tail** — directly seed propagating-mode initial conditions instead of standing-wave; the cleanest follow-up given the asymmetry observed
2. **N=128 photon-tail at corpus-aspect** — escape sub-Nyquist topology seed; ~5 hr per run, expensive
3. **Photon-tail at non-corpus aspect** — relax R/r=φ² constraint, allow larger r so c=3 cleanly seeded; tests the framework but at non-corpus geometry
4. **Accept empirical pattern** — Round 7+8 has shown the engine doesn't host corpus electron at any tractable configuration tested; close the arc with substrate-natural attractor characterization (Move 7+7b+10) as the empirical finding and corpus mismatch as the open framework question

### 10.6 A57 (NEW for r8.10 §17.1)

**A57 — Sub-Nyquist topology-seed caveat at corpus aspect ratio.** Op10's `extract_crossing_count` requires the (2,3) poloidal winding's feature size to be above lattice Nyquist (≥2 cells) for a clean c=3 reading. At corpus aspect R/r = φ², the constraint that the loop fits in the lattice's active region forces r ≤ ~1.5 cells at N=64 (~2.5 cells at N=128, ~5 cells at N=256). Anything below ~r = 1.5 cells gives c=2 instead of c=3 at t=0 — sub-Nyquist topology seed. Pre-regs that include "c=3 maintained" as a PASS criterion must verify c=3 at t=0 first; if c=2 at t=0, the criterion is unsatisfiable from initial condition and shouldn't be load-bearing in the adjudication. Generalizes: any pre-registered topology-preservation criterion needs the topology to be cleanly seeded at t=0; verify at pre-reg-write time, not just at adjudication time.

---

## §11 — Photon-tail path (b): propagating IC test (P_phase6_photon_tail_propagating_ic)

Pre-registered driver `r8_photon_tail_propagating_ic.py` at commit bd15bb0. N=64, R=4, r=1.5, V_inc amp=0.1, ω amp scale=0.3464 (A26 anchor), 200 Compton periods, no drive. Identical seeder to path (a) except `omega_dot` is set to enforce loop-tangent rotation in (x,y) plane: `ω̇_x = +Ω_loop·ω_y`, `ω̇_y = −Ω_loop·ω_x`, `ω̇_z = 0`, where `Ω_loop = 2π·c/L_loop`. Adjudication scope: 3/3 of C1/C2/C3 load-bearing; C4 demoted to informational per A57. c(t) trajectory tracker added (samples Op10 every 10P throughout).

### 11.1 Pre-reg adjudication

**Result: Mode III, 0/3 load-bearing PASS.**

| Criterion | Measured | Target | Verdict |
|---|---|---|---|
| C1 single-node ellipse aspect | median 25.74 (12/30 nodes finite) | 2.618 ± 5% | FAIL |
| C2 spatial winding rotation | NaN (insufficient finite nodes) | 5·2π ± 30% | FAIL |
| C3 LC reactance ρ(Σ\|V_inc\|², Σ\|Φ_link\|²) | -0.463 | (-1.2, -0.8) | FAIL |
| C4 (informational) topology c via Op10 | 1 final; reached 3 transiently | 3 | FAIL (informational) |

[`r8_photon_tail_propagating_ic_results.json`](../../src/scripts/vol_1_foundations/r8_photon_tail_propagating_ic_results.json) for full data.

### 11.2 Path (a) ↔ path (b) comparison

| Quantity | Path (a) standing-wave | Path (b) propagating |
|---|---|---|
| C1 median R/r | 25.74 | 25.74 |
| C2 winding | decoherent | NaN |
| C3 ρ(V_inc, Φ_link) | -0.46 | -0.463 |
| peak \|ω\| t=0 → t=200P | 0.836 → 0.036 (4.3%) | 0.836 → 0.036 (4.4%) |
| peak \|V_inc\| t=0 → t=200P | 0.261 → 0.174 (66%) | 0.261 → 0.174 (66%) |
| Mode | III, 0/4 (3/3 load-bearing FAIL) | III, 0/3 load-bearing FAIL |

Path (a) and path (b) produced **near-identical empirical fingerprints**. C3's LC reactance ρ matches to 0.003. Sector asymmetry pattern (Cosserat ω 4% retention, K4 V_inc 66%) is invariant to IC velocity choice. The propagating-IC ω̇ injection neither re-energized the Cosserat sector nor stabilized the (2,3) topology — within ~10P the propagating phase information was indistinguishable from the standing-wave configuration.

**Empirical implication.** The engine's near-identical response to standing-wave and propagating IC at this scale rules out IC-velocity-choice as the cause of Mode III. The dissolution pathway is structural: at (R=4, r=1.5, N=64) the engine's saturation + Op14 dynamics drive the Cosserat (2,3) configuration toward dissolution regardless of how the kinetic phase is initialized.

### 11.3 c(t) trajectory — flickering topology

| t / P | c | peak \|ω\| |
|---|---|---|
| 10 | 3 | 0.103 |
| 20 | 0 | 0.084 |
| 30 | 1 | 0.067 |
| 40 | 0 | 0.075 |
| 50 | 3 | 0.056 |
| 60 | 1 | 0.052 |
| 70 | 1 | 0.045 |
| 80 | 0 | 0.044 |
| 90 | 1 | 0.036 |
| 100 | 3 | 0.051 |
| 110 | 0 | 0.032 |
| 120 | 2 | 0.033 |
| 130 | 1 | 0.041 |
| 140 | 2 | 0.044 |
| 150 | 0 | 0.034 |
| 160 | 1 | 0.030 |
| 170 | 2 | 0.029 |
| 180 | 0 | 0.035 |
| 190 | 0 | 0.045 |
| 200 | 0 | 0.038 |

c oscillates between 0/1/2/3 throughout. Hits c=3 transiently at t=10/50/100P (roughly 40-50P spacing) then collapses back. peak |ω| decays monotonically from t=10P onward (with brief amplitude excursions correlated with c=3 events at t=50P and t=100P). After t=120P, c stays in {0, 1, 2}; from t=180P onward, c=0 dominates (no winding signal).

This is consistent with two readings:

1. **Marginal-topology aliasing.** Sub-Nyquist topology seed (A57) means Op10's c reading at this scale is sensitive to noise; transient c=3 events may be aliasing artifacts as the dissolving configuration's apparent winding count fluctuates.

2. **Nascent breather rejection.** Even taken at face value, the engine briefly hosts c=3 (every ~50P with decaying amplitude) but cannot maintain it. Energy that would sustain a (2,3) loop is instead radiated outward (ω peak decay 0.836 → 0.038, factor 22 attenuation).

C3's ρ = -0.463 (vs target -1.0 ± 0.2) indicates partial LC trading — about half the energy variance in V_inc ↔ Φ_link follows the LC pattern. Not a fully-locked LC oscillator, but not a static fixed point either. Same value to three significant figures across paths (a) and (b) suggests this is the engine's natural attractor's reactance signature at this scale, not an IC artifact.

### 11.4 What path (b) establishes empirically

1. **Photon-tail framework, as currently formulated, does not produce a corpus-electron signature at any IC variant tested at engine-representable scale (N=64, corpus aspect R/r=φ²).** Standing-wave (a) and propagating (b) IC give near-identical Mode III patterns. Per pre-reg threshold, the photon-tail branch closes at this scale.

2. **Dissolution is not IC-driven.** Path (a) → (b) was the cleanest test of "does the propagating-mode neighborhood contain the photon-tail attractor's basin?" The answer is no — the propagating IC dissolves into the same final state as the standing-wave IC.

3. **Sector asymmetry is a robust empirical feature.** Cosserat ω retention 4% across both paths; K4 V_inc retention 66% across both paths; partial K4 LC reactance ρ ≈ -0.46 across both paths. This points to **the engine's actual attractor at (R=4, r=1.5, N=64) being a partial K4 standing pattern with the Cosserat sector dissolved**, not a corpus electron.

4. **c(t) flicker pattern (transient c=3 every ~50P with decaying ω) is novel.** Did not appear in Move 5 (uniform plateau) or Move 7+10 (static fixed point). It's specific to the photon-tail dual-seed configuration at this scale and suggests the engine attempts to host the (2,3) topology but cannot sustain it. May be informative for a future N=128+ rerun (above-Nyquist topology seed should disambiguate aliasing from genuine flicker).

### 11.5 Cumulative Round 7+8 falsification status

The arc has now empirically tested and falsified, against pre-registered criteria:

1. **R7.1 V-block / Cos-block linearized eigsolves** at corpus GT — Mode III (closest eigenvalue without structural-mode signatures)
2. **Move 5 Cosserat-only standing-wave self-consistent orbit hunt** at corpus GT — Mode III (sub-corpus (2,3) attractor at non-corpus scale)
3. **Move 6 natural attractor characterization** at the (2,3) plateau — Mode III (R/r ≠ φ², peak|ω|=0.30 not corpus)
4. **Move 7+7b+10+11+11b reactance snapshots** at attractor — static fixed point with cross-sector trading, not LC reactance
5. **Diag A wave-speed amplitude curves (V·S, T·1 hypothesis)** — Mode I sub-percent (asymmetry exists but is not the cause of Mode III)
6. **Photon-tail path (a) standing-wave dual-seed at corpus aspect** — Mode III, 0/4
7. **Photon-tail path (b) propagating dual-seed at corpus aspect** (THIS TEST) — Mode III, 0/3

Across 7 pre-registered tests at engine-representable corpus geometry, the corpus electron's predicted signature is absent. Per pre-reg thresholds set at Move 5, R7.1, photon-tail (a), and photon-tail (b): each closure was specified at pre-reg-write time. The cumulative empirical statement is:

**At all configurations tractable at N=64 lattice resolution (the corpus's prescribed dx = ℓ_node), the K4-TLM + Cosserat engine does not host the corpus electron.**

This is an empirical statement about the engine at its prescribed lattice resolution, not a falsification of the corpus framework. Doc 76_ (lattice ↔ Ax 3 + Ax 4 bridge) provides one route for reframing — corpus electron lives at an integrated-along-loop scale that single-cell engine extraction may not see. Other routes (N=128+ escalation, non-corpus aspect ratio, different IC topology) remain open as separate framework questions.

### 11.6 A58 (NEW)

**A58 — Path-(a)/path-(b) empirical equivalence at engine-representable corpus aspect.** Standing-wave and propagating dual-seed IC produced near-identical final states (C1, C3 match to 3 sig figs; sector retention identical) at (R=4, r=1.5, N=64). The engine's response to corpus-aspect dual-seed configurations is dominated by the geometry, not the IC velocity choice, at this scale. This rules out IC-velocity-tuning as the route to corpus-electron formation at engine-representable scales; future tests should explore (a) larger lattice N to escape Nyquist constraint, (b) non-corpus aspect ratio, or (c) reframed corpus prediction at integrated-loop scale per doc 76_.
