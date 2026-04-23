# 50 — Phase III-B v2: Autoresonant + Dark-Wake Pair Creation Test

**Status:** completed 2026-04-22 (r1); rewritten 2026-04-23 (r2, later r3).
**Revision history:**
  - **r1 (2026-04-22)** — original writeup; headline `A²_cos = 1.009 crossed rupture boundary`.
  - **r2 (2026-04-23)** — distribution rewrite (20-seed sweep: 1.009 is 0/20 reproducible on post-Phase-3 engine per [VACUUM_ENGINE_MANUAL §10.12](VACUUM_ENGINE_MANUAL.md)); axiom-first convention reframe per [Vol 1 Ch 7](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex) + [doc 55_](55_cosserat_normalization_derivation.md); forward-chain audit with inline `[axiom-flag]` annotations; driver + observer + source code audited. **Superseded by r3 — r2's R3 framing missed Vol 4 Ch 1:711 subatomic override.**
  - **r3 (2026-04-23, same day)** — R4 correction per [Vol 4 Ch 1:711](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L711) subatomic override. At subatomic scale (VacuumEngine3D's operating regime), **V_yield ≡ V_SNAP** — so engine's `A² = V²/V_SNAP²` IS canonical `r² = V²/V_yield²`, not a macro-outlier. [A14 CATEGORY-ERROR framing retracted]: `RegimeClassifierObserver.max_A2_total` sum is a valid Pythagorean r² under subatomic convention, not a mixed-normalization bug. [Schwinger-at-137 framing retracted]: at subatomic V_yield = V_SNAP, AVE's pair-production onset and the QED Schwinger field collapse to the same r = 1. Distribution regression (0/20 reproduce 1.009) is the remaining honest issue; decoupled from normalization. Doc 55_ superseded; see its R4 banner. Engine patches follow plan file's R4 step list.

**Parent plan:** `~/.claude/plans/document-list-for-next-chat-compressed-thunder.md` Stage 4d
**Depends on:**
  - [48_pair_creation_frequency_sweep.md](48_pair_creation_frequency_sweep.md) — v1 baseline
  - [49_dark_wake_bemf_foc_synthesis.md](49_dark_wake_bemf_foc_synthesis.md) — mechanism synthesis
  - [46_vacuum_engine_scope.md](46_vacuum_engine_scope.md) — engine architecture
  - [54_pair_production_axiom_derivation.md](54_pair_production_axiom_derivation.md) — axiom-derivation chain
  - [55_cosserat_normalization_derivation.md](55_cosserat_normalization_derivation.md) — **SUPERSEDED**; R3 direction was wrong per Vol 4 Ch 1:711 subatomic override. Kept for audit trail.
  - [manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:711](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L711) — **subatomic V_yield override (load-bearing for r3 convention)**
  - [VACUUM_ENGINE_MANUAL.md](VACUUM_ENGINE_MANUAL.md) §10.4, §10.12, §17 A14, A17 (A14 annotation flip to R4 pending)

---

## 0. Audit frame (r2, R4-corrected in r3)

### 0.1 Convention declaration (R4 — subatomic override)

Per [Vol 1 Ch 7:12, :20, :33](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L12) (canonical AVE regime map): **every domain reduces to a dimensionless control parameter `r = A / A_c` where `A_c` is the domain-specific Regime IV entry boundary, with the universal saturation operator `S(r) = √(1 − r²)`**. Regime IV begins at `r = 1` uniformly across domains.

Per [Vol 4 Ch 1:711](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L711) (numerical value at scale): at **subatomic scale** (bond energy solvers, Yang-Mills confinement, pair production), `v_yield` is overridden to `V_SNAP ≈ 511 kV`. At macroscopic scale (HV capacitors), the default `V_yield = √α · V_SNAP ≈ 43.65 kV` applies. **VacuumEngine3D operates at subatomic scale** (K4 lattice with `ℓ_node = ℏ/(m_ec) = Compton wavelength`; simulates pair nucleation), so **V_yield ≡ V_SNAP** for this engine.

**Consequence — engine's V_SNAP-normalization IS the canonical `r²`:**

- K4 sector: `A²_K4 = V²/V_SNAP² = r²_K4` ([`k4_cosserat_coupling.py:208`](../../src/ave/topological/k4_cosserat_coupling.py#L208)). Canonical per Vol 1 Ch 7:12 with subatomic `V_yield = V_SNAP`.
- Cosserat sector: `A²_cos = ε²/ε_yield² + κ²/ω_yield² = r²_cos` ([`_cosserat_A_squared`](../../src/ave/topological/k4_cosserat_coupling.py#L63)) with `ε_yield = 1`, `ω_yield = π`. The `ε_yield = 1` value is **TKI-derived** under subatomic convention: σ_yield = V_yield·e/ℓ_node³ with subatomic V_yield = V_SNAP gives σ_yield = m_ec²/ℓ_node³ = 1 in natural units; with G = 1, ε_yield = σ_yield/G = 1 exactly. **Not empirical placeholder** — closed-form Ax2-TKI + Ax3 derivation.
- Regime boundaries `{2α, 3/4, 1}` at [vacuum_engine.py:151-153](../../src/ave/topological/vacuum_engine.py#L151): **[Ax1+4-DERIVED]** per Vol 1 Ch 7:41-51 — 2α is small-signal self-coupling threshold, 3/4 is Q = ℓ_min = 2 radiating-multipole onset, 1.0 is Ax4 rupture. Applied to subatomic r² directly.
- Pythagorean sum `r²_total = r²_K4 + r²_cos` is valid (AVE-APU Vol 1 Ch 5 Pythagorean strain theorem) because both terms are canonical r² at the same operating scale.

**`A²_cos = 1` is the Axiom-4 Cosserat Regime IV entry (Ax4 rupture / pair-production onset per [Vol 1 Ch 7:53,115](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L53)).** Under subatomic override, this is also where the QED Schwinger field sits numerically (V_yield = V_SNAP collapses the distinction — see §0.2). **No yield-vs-SNAP normalization split at this scale.**

### 0.2 "Rupture" terminology — scale-dependent V_yield (r3)

Vol 1 Ch 7:115 and :130 appear to give different numerical values for "Schwinger":

- **Vol 1 Ch 7:53, :115** (EM-dielectric subsection, `r = V/V_yield`): "Schwinger pair production: r = 1.0 — Regime IV boundary."
- **Vol 1 Ch 7:130** (EM-field-strength subsection, `r = E/E_yield`): "Schwinger critical field corresponds to r = V_SNAP/V_yield = 1/√α ≈ 11.7, deep in Regime IV."

**Not a manuscript defect — scale-dependence under the universal form `r = V/V_yield`.** V_yield takes different numerical values at different scales per Vol 4 Ch 1:711:

- **Macroscopic scale** (HV capacitors, lab EM): V_yield = √α · V_SNAP ≈ 43.65 kV. At this scale, Vol 1 Ch 7:115's "AVE pair-production onset" (r = 1 = V_yield = 43 kV) is 12 orders of magnitude below Vol 1 Ch 7:130's "QED Schwinger field" (at V = V_SNAP = 511 kV, so r = V_SNAP/V_yield = 1/√α ≈ 11.7). There is real headroom within Regime IV here: AVE's varactor-divergence onset is at V_yield; QED's Schwinger is 11.7× deeper. AVE-PONDER's autoresonant mechanism exploits this — it can nucleate pairs at r = 1 (V_yield), orders of magnitude below the brute-force QED Schwinger point.
- **Subatomic scale** (bond LC tanks, pair production): V_yield is **overridden to V_SNAP**. Each K4 node stores m_ec²/tank at rest; the saturation threshold is the full V_SNAP because the tank can't hold more. **V_yield and V_SNAP collapse to the same thing at this scale** — there's no "deeper Regime IV" past V_SNAP because the tank is full. r = 1 is both Ax4 rupture AND Schwinger onset simultaneously.

**This doc r3 uses the subatomic convention** (engine's operating scale per §0.1). `max A²_cos ≈ 1` = Axiom-4 Cosserat Regime IV entry = AVE pair-production onset = Schwinger point (all the same event at this scale). **No "Schwinger is 2 orders further out" framing** — that was an artifact of applying macro-scale numerical V_yield to subatomic-scale engine data (r2 error, corrected in r3).

**Physical interpretation — varactor form:** `C_eff = C_0/√(1 − r²)` mathematically blows up at r=1 as the boundary of its Regime-II validity; past r=1, `S` becomes imaginary and `C_eff` flips character per [doc 54_ §6a](54_pair_production_axiom_derivation.md) (mode-conversion onset). Vol 1 Ch 7:247's `C_eff → ∞` / `= ∞` notation is shorthand for this phase boundary, not a physical infinity. Manual §3.1: "impedance diverges **then inverts** at V_yield." Capacitance doesn't actually take infinite values; the classical LC description stops applying at the Regime IV boundary.

### 0.3 Known engine defects affecting v2 numbers

1. **[A14 — RESOLVED under R4 subatomic override]** Earlier r2 flagged `RegimeClassifierObserver.max_A2_total = A²_K4 + A²_Cos` at [vacuum_engine.py:376](../../src/ave/topological/vacuum_engine.py#L376) as a mixed-normalization bug per doc 55_'s R3 direction. **This was wrong.** Under Vol 4 Ch 1:711 subatomic override, **both A²_K4 (V²/V_SNAP² with subatomic V_yield = V_SNAP) and A²_Cos (ε²/ε_yield² + κ²/ω_yield² with TKI-derived ε_yield = 1) are canonical r² at the same operating scale**. The Pythagorean sum per AVE-APU Vol 1 Ch 5 IS valid. No bug. The `/α` conversions present in [NodeResonanceObserver:428](../../src/ave/topological/vacuum_engine.py#L428) and [BondObserver:433](../../src/ave/topological/vacuum_engine.py#L433) are the actual defect — they apply macro-scale conversion to subatomic-scale K4 data. R4 patch (plan file step 3) removes the `/α` lines; R3 dual-accessor direction is not pursued. See §6.10 for the full R4 audit.
2. **[A17 — distribution regression]** 20-seed sweep on post-Phase-3 engine returned `max A²_cos` range **[0.7677, 0.9983]**, median **0.8683**, IQR [0.81, 0.92]; **0/20 seeds reach 1.009**; 2/20 within ±0.05 of 1.009. See [VACUUM_ENGINE_MANUAL §10.12](VACUUM_ENGINE_MANUAL.md) for full sweep verdict. Either Phase 2 (commit 719f3ec) / Phase 3 (3a599ca) perturbed the Cosserat trajectory, or the original v2 was a lucky-tail seed. Bisection 719f3ec vs 3a599ca recommended. **Orthogonal to the R4 convention adjudication** — the distribution regression is a real engine/seed issue regardless of normalization framing.
3. **[A7 — linear-Taylor PLL, not Ax4-native]** [`AutoresonantCWSource.apply`:723](../../src/ave/topological/vacuum_engine.py#L723) uses `ω(t) = ω₀·max(1e-3, 1 − K_drift·A²_probe)` — a linear expansion of the Axiom-4-native varactor form. Taylor-truncated from `(1 − A²)^(1/4)` at small A², the leading term is `1 − A²/4`, implying **axiom-native K_drift = 1/4, not the engine's empirical 0.5**. See §6.3 for the audit proposal. (Under R4 the probe `A²_SNAP = 0.393` is already canonical r² at subatomic scale — no conversion needed; the earlier r2 "architecture may be working in wrong normalization" concern was an R3-era artifact, now retracted.)

### 0.4 Tag key for `[axiom-flag]` annotations below

| Tag | Meaning |
|---|---|
| `[AxN-DERIVED]` | Full derivation chain from one or more of the 4 axioms exists, cited with file:line |
| `[AxN+M-DERIVED]` | Chain uses multiple axioms |
| `[AXIOM-ADJACENT]` | Functional form uses axioms, but a gate-choice / selection is engineering adjudication (tracked in [S_GATES_OPEN.md](S_GATES_OPEN.md)) |
| `[EMPIRICAL]` | Tuned from sweep / calibrated to data; no axiom-derivation chain |
| `[PORTED]` | Copied from sibling repo (AVE-Propulsion / AVE-PONDER / etc.); K4-native derivation pending |
| `[HEURISTIC]` | Chosen for convenience or numerical-stability; no first-principles attempt |
| `[CONJECTURE]` | Observation-based hypothesis (distinct from pre-registered prediction) |
| `[CATEGORY-ERROR-r2-RETRACTED]` | r2 flagged certain claims as category errors based on R3 (doc 55_) framing; under R4 these are not category errors. Tag retained only for audit trail where it appears. |
| `[r2-ERROR-r3-CORRECTED]` | r2 conclusions based on R3 that r3 corrects |

---

## 1. Experimental design

### 1.1 Configuration matrix (8 configs per seed)

Focused smaller-than-v1 sweep. v1 had 16 configs (4λ × 2amp × 2T); v2 uses 8 configs (4λ × 1amp × 2T) for direct v1-vs-v2 comparison at v1's peak-`max A²_cos` amplitude.

| Parameter | Value | Axiom status |
|---|---|---|
| Wavelength λ (cells) | `{3.5, 5, 7, 10}` | **[AXIOM-ADJACENT]** — Ax1 gives `ℓ_node = 1` but specific λ values are sweep design |
| Amplitude | `0.5 · V_SNAP` | **[EMPIRICAL]** — from v1 peak; places source V² at `A²_K4_SNAP = 0.25` at origin (within Regime II, `2α ≤ A² < 3/4`). See §6.1 |
| Temperature | `{0, 0.1}` m_e c² units (= {0, 5.93 × 10⁸ K} SI) | **[Ax3-DERIVED]** thermal init per [47_](47_thermal_lattice_noise.md); specific T values [EMPIRICAL] (0 baseline + hot) |
| Source type | `AutoresonantCWSource` (K_drift=0.5 per Stage 4c) | **[AXIOM-ADJACENT]** — varactor-softening Duffing is Ax4; PLL control loop is engineering adjudication on top of Ax4. See §6.3 |
| K4 lattice size | N = 40, pml = 5 | **[EMPIRICAL / ENGINEERING]** — chosen for ~3 wavelengths interior; PML rolloff is FDTD standard |
| Outer steps | 300 (v1 was 240) | **[EMPIRICAL]** — chosen "for PLL to track"; should be derivable from t_ramp + t_sustain once those are pinned. See §6.4 |

### 1.2 Observers attached per run

Per [driver:106-113](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py#L106):

- `RegimeClassifierObserver(cadence=5)` — regime cell counts, `max_A2_k4`, `max_A2_cos`, `max_A2_total`. ⚠ `max_A2_total` suffers A14 mixing; use `max_A2_cos` and `max_A2_k4` separately.
- `TopologyObserver(cadence=5, threshold_frac=0.7)` — centroid detection. **[EMPIRICAL override]** — default is 0.3 (H1 falsified per [doc 52_](52_h1_threshold_sweep.md)); 0.7 is post-H1 tightening to avoid thermal-noise false positives. See §6.5.
- `EnergyBudgetObserver(cadence=5)` — K4 / Cosserat / coupling energy partition. **[Ax3-DERIVED]** — Hamiltonian from effective-action (cosserat_field_3d energy functional).
- `DarkWakeObserver(cadence=5, propagation_axis=0)` — τ_zx shear-strain diagnostic. **[PORTED]** from [AVE-Propulsion/simulate_warp_metric_tensors.py:75-95](../../../AVE-Propulsion/src/scripts/simulate_warp_metric_tensors.py). K4-native derivation pending; see §6.6.

### 1.3 Pre-registered outcomes (from r1 plan, verbatim)

- **P_IIIb-v2-pair** — Cosserat localized (≥ 2 centroids at `threshold_frac = 0.7`), dark wake shows constructive interference at collision plane. FIRST NUMERICAL AVE PAIR CREATION. **[HEURISTIC thresholds]** — the `≥ 2` centroid + `max A²_cos ≥ 0.5` cuts in [driver:132](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py#L132) are post-hoc adjudication choices, not axiom-derived. See §6.7.
- **P_IIIb-v2-partial** — Cosserat response structurally different from v1 but no full pair.
- **P_IIIb-v2-no-change** — Same distributed-plateau as v1. Would falsify the AVE-Propulsion Ch 5 interpretation.

## 2. Results

### 2.1 Raw results table (single-seed, r1 original)

Original single-seed run values. These are retained as historical data; see §2.3 for the 20-seed distribution that supersedes them.

| Run | λ | T | ω·τ | max A²_K4 | max A²_cos | max τ_zx | #centroids | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | 3.5 | 0.00 | 1.80 | 0.393 | 0.000 | 0.151 | 0 | v2-no-change |
| 2 | 5.0 | 0.00 | 1.26 | 0.134 | 0.000 | 0.059 | 0 | v2-no-change |
| 3 | 7.0 | 0.00 | 0.90 | 0.112 | 0.000 | 0.040 | 0 | v2-no-change |
| 4 | 10.0 | 0.00 | 0.63 | 0.104 | 0.000 | 0.041 | 0 | v2-no-change |
| 5 | 3.5 | 0.10 | 1.80 | 0.393 | **1.009** † | 0.151 | 0 | v2-partial |
| 6 | 5.0 | 0.10 | 1.26 | 0.134 | 0.856 | 0.059 | 0 | v2-partial |
| 7 | 7.0 | 0.10 | 0.90 | 0.112 | 0.824 | 0.040 | 0 | v2-partial |
| 8 | 10.0 | 0.10 | 0.63 | 0.104 | 0.837 | 0.041 | 0 | v2-partial |

(All amp = 0.5·V_SNAP, N=40, n_steps=300, K_drift=0.5, default seed.)

† **The 1.009 headline is now known to be a tail outcome** — see §2.3.

**[Ax1-DERIVED]** max_A2_K4 values (column 5): bit-identical for T=0 and T=0.1 runs because K4 initializes deterministically under default `thermalize_V=False` ([vacuum_engine.py:889](../../src/ave/topological/vacuum_engine.py#L889)) and sources are deterministic. All Cosserat variance in column 6 is seed-driven thermal-init variance.

### 2.2 Cold-vacuum control (T=0) — C1 CONFIRMED

**[Ax1-DERIVED]** [46_ §2.1, C1-finding](46_vacuum_engine_scope.md): at T = 0, AVE vacuum is deterministic — no sub-ℓ_node fluctuations. All 4 T=0 runs give `max A²_cos = 0.000` exactly (bit-level) across single-seed and 20-seed sweeps. Autoresonant drive on a cold vacuum behaves identically to fixed-f CW — zero Cosserat response.

The **dark wake IS nonzero at T=0** (τ_zx grows with ω·τ, reaching 0.151 at high-f). This is the K4 V²-gradient × Z_local signature — it operates on the K4 substrate independent of Cosserat excitation and is bit-identical across seeds. **[PORTED formula + Ax1-consistent computation]** — see §6.6 for the axiom-status of the τ_zx form.

### 2.3 Hot regime (T = 0.1) — distribution rewrite (supersedes r1)

Per [VACUUM_ENGINE_MANUAL §10.12](VACUUM_ENGINE_MANUAL.md), 20 explicit RNG seeds on the v2 headline config (λ=3.5, T=0.1, K_drift=0.5, amp=0.5·V_SNAP, N=40, 300 outer steps) on the **current engine (post-Phase-3 commit `3a599ca`)**. Artifact: `/tmp/v2_reproducibility_sweep.{npz,png}`.

**Distribution of max A²_cos across 20 seeds at (λ=3.5, T=0.1):**

| Metric | Value |
|---|---|
| Range | **[0.7677, 0.9983]** |
| Median | **0.8683** |
| IQR | [0.8097, 0.9181] |
| max A²_K4 (bit-identical across seeds) | 0.3934 |
| max τ_zx (bit-identical across seeds) | 0.1507 |
| Seeds at or above 1.009 | **0 / 20** |
| Seeds within ±0.05 of 1.009 | 2 / 20 |

**[AXIOM-FLAG R4 subatomic convention per §0.1]:** "`max A²_cos`" is the peak of `ε²/ε_yield² + κ²/ω_yield²` across active sites — canonical `r²_cos` per Vol 1 Ch 7:12 with ε_yield = 1 (TKI-derived at subatomic scale per §0.1). A²_cos = 1 is the Ax4 Cosserat Regime IV entry / AVE pair-production onset (equivalent to QED Schwinger at this scale per §0.2); the varactor form's classical description mode-converts there (not a literal C → ∞).

**Axiom-4 interpretation:** In the best-case seed (0.9983), the Cosserat sector reaches **99.8% of the Ax4 Cosserat rupture boundary** — the r = 1 pair-production-onset / Schwinger-onset point (unified at subatomic scale per §0.2). In the median seed (0.8683), the Cosserat sector reaches **Regime III** (yield zone: `3/4 ≤ r² < 1`, per Vol 1 Ch 7:47-51 Q=1/S=ℓ_min=2 radiating-multipole derivation) but does not cross to Regime IV. **Zero seeds cross to Regime IV.** At subatomic scale there is no "deeper Regime IV" past r=1 (V_yield and V_SNAP collapse per Vol 4 Ch 1:711) — r=1 IS the hard ceiling.

Comparison vs v1 (fixed-f CW) at matched (λ, T=0.1, amp=0.5):

| λ | ω·τ | v1 max A²_cos (single seed, r1) | v2 median (20 seeds, r2) | v2 [min, max] | Qualitative change |
|---|---|---|---|---|---|
| 3.5 | 1.80 | 0.895 | **0.87** | [0.77, 1.00] | approaches V_yield in tail; median at yield onset |
| 5.0 | 1.26 | 0.873 | **0.856** † | single-seed v2 value | slight decrease |
| 7.0 | 0.90 | 0.962 | **0.824** † | single-seed v2 value | decrease at old v1 peak |
| 10.0 | 0.63 | 0.893 | **0.837** † | single-seed v2 value | slight decrease |

† The 20-seed sweep in [VACUUM_ENGINE_MANUAL §10.12] was only run at λ=3.5. Values at λ∈{5,7,10} are single-seed and **should be re-swept before being cited as definitive**. Flagged for FUTURE_WORK.

**Axiom-native σ(ω) shape observation:** Single-seed v1 had a peak at ω·τ=0.9 (λ=7); single-seed v2 shows monotonic increase with ω·τ. Whether the monotonic shape is robust across seeds at all λ requires the full 4λ × 20-seed sweep (not yet run). Provisional finding; re-confirm before final adjudication.

**[AxN-FLAG: cause of the 0/20 non-reproducibility] [AXIOM-ADJACENT + A17-FLAG]:** per [VACUUM_ENGINE_MANUAL §17 A17](VACUUM_ENGINE_MANUAL.md), two non-exclusive explanations: (a) Phase 2 / Phase 3 subtly perturbed the coupled Cosserat trajectory via JAX recompile / `_connect_all` touches (commits `719f3ec` / `3a599ca`); (b) the 1.009 r1 headline was a lucky-tail seed. Bisection `719f3ec` vs `3a599ca` distinguishes; not yet executed. **Orthogonal to the axiom-first convention work in this doc** — distribution reporting is correct regardless of cause.

### 2.4 Dark-wake amplitude is frequency-dependent

Per the r1 sweep, max τ_zx grows ~4× from ω·τ = 0.9 to ω·τ = 1.8:

| ω·τ | max τ_zx |
|---|---|
| 0.63 | 0.041 |
| 0.90 | 0.040 |
| 1.26 | 0.059 |
| 1.80 | 0.151 |

**[PORTED formula + Ax1-consistent implementation]** — The τ_zx computation in [`DarkWakeObserver`](../../src/ave/topological/vacuum_engine.py) uses the AVE-native K4 tetrahedral gradient (correctly handles bipartite sublattice per manual §4.2), so the computation is Ax1-consistent. **However, the formula itself (τ_zx ∝ Z_local · ∂(V²/V_SNAP²)/∂x) is ported from [AVE-Propulsion/simulate_warp_metric_tensors.py:75-95](../../../AVE-Propulsion/src/scripts/simulate_warp_metric_tensors.py) without a K4-native first-principles derivation.** The formula is compatible with Rule-6 (impedance-gradient × field-gradient is natural impedance-matching / TLM language) but has not been derived in-house from Axiom 1 K4 dynamics. See §6.6.

τ_zx is **bit-identical across seeds** (confirmed: 0.1507 exactly at λ=3.5 T=0.1 across all 20 seeds). This is diagnostic of the K4 sector's determinism — the dark-wake signal is a K4-V² gradient, deterministic once `thermalize_V=False`.

### 2.5 Verdict adjudication (r2)

| Prediction | r1 adjudication | r2 adjudication | Evidence |
|---|---|---|---|
| **P_IIIb-v2-pair** (≥ 2 centroids, localized) | NOT OBSERVED | **Still NOT OBSERVED** across 20 seeds | Zero centroids at threshold_frac=0.7 in all configs; max A²_cos approach ≠ localization |
| **P_IIIb-v2-partial** (different than v1) | CONFIRMED | **PROVISIONAL — re-sweep needed** | λ=3.5 distribution differs from v1 single-seed (v1 0.895 sits near v2 median 0.87); other λ are single-seed v2 and can't be compared yet to single-seed v1 beyond ±variance |
| **P_IIIb-v2-no-change** (same as v1) | FALSIFIED | **NOT-YET-ADJUDICABLE** without 4λ × N-seed sweep of both v1 and v2 | r1's falsification rested on single-seed comparison; distribution-matched comparison not available |

**Net r2 verdict:** The autoresonant drive IS doing something physically observable (K4-side τ_zx scaling with ω is deterministic and real, no seed dependence). The Cosserat-side σ(ω) shape change between v1 and v2 is **claimed but not proven at distribution level**; a matched-seeds sweep of both v1 (fixed-f CW) and v2 (autoresonant CW) is required. No pair nucleation under any configuration. This is a **structural limit** (Phase 4+ addresses it per [VACUUM_ENGINE_MANUAL §11.9](VACUUM_ENGINE_MANUAL.md) + [doc 54_ §6](54_pair_production_axiom_derivation.md)), not a drive-tuning issue.

## 3. Interpretation

### 3.1 The autoresonant mechanism IS doing something — K4-side only (so far)

**Robust findings** (deterministic, seed-independent):

1. **K4 sector response scales as expected.** `max_A2_K4 = 0.393` at λ=3.5 (Regime II per Vol 1 Ch 7:30-33, `2α ≤ r² < 3/4`). **[Ax1+4-DERIVED]** — the K4 sector under deterministic drive follows Axiom-1 wave propagation + Axiom-4 saturation; no seed variance.
2. **Dark wake τ_zx grows ~4× with frequency ω·τ ∈ {0.9, 1.8}.** **[PORTED formula + Ax1-consistent computation]** — per §2.4, formula ported from AVE-Propulsion without K4-native derivation; computation uses K4 tetrahedral gradient correctly; signal is seed-deterministic.

**Claimed findings requiring re-sweep to be robust:**

3. ~~σ(ω) peak location shifted (v1 peaked at ω·τ=0.9; v2 rises monotonically to ω·τ=1.8)~~ — **[CONJECTURE]** based on single-seed v1 vs single-seed v2 at λ∈{5,7,10}. At λ=3.5 where 20-seed data exists, distributions overlap (v1 0.895 single-seed vs v2 median 0.87, IQR [0.81, 0.92]). **Claim a distribution-shape change only after matched-seeds sweep of both.**
4. A²_cos crosses 1.0 at λ=3.5 — **[Ax4-DERIVED interpretation, distribution-level unreliable]**. Under R4 subatomic convention (§0.1), r1's headline framing "first numerical approach of the Axiom-4 rupture boundary" was **axiom-correct** — r=1 is the Ax4 Cosserat Regime IV entry = AVE pair-production onset = QED Schwinger onset (unified at subatomic scale). **However, the number itself does not reproduce:** 0/20 seeds reach 1.009 on current engine; median 0.87 (inside Regime III, below r=1); best 0.9983. **Updated r3 claim:** "the autoresonant configuration brings ~1/20 of seeds to within 0.2% of the Ax4 Cosserat Regime IV boundary; median trajectory stops inside Regime III (r ≈ 0.93)." The r1 axiom-framing was right; the single-seed generalization was wrong. The r2 `[CATEGORY-ERROR]` flag on this item was itself an R3-framing artifact (retracted).

### 3.2 No pair formation observed — structural, not tunable

At `threshold_frac = 0.7`, no centroids detected in any config across all 20 seeds. **[Ax4-DERIVED diagnosis, per [doc 54_ §6](54_pair_production_axiom_derivation.md) + [VACUUM_ENGINE_MANUAL §11.9](VACUUM_ENGINE_MANUAL.md)]:**

Under the current **single-kernel symmetric saturation** `S(r) = √(1 − r²)`, the Axiom-4-native flux-tube confinement mechanism (Γ = −1 impedance walls at saturated endpoints trapping a standing-wave LC mode with mass m_e) **cannot form**. Asymmetric μ/ε saturation with chirality bias (`κ_chiral = 1.2α`, **[Ax2-DERIVED]** per [doc 20_ Sub-Theorem 3.1.1](20_chirality_projection_sub_theorem.md)) is required — this is what Stage 6 Phase 4 will add (reopens S1 gate per [S_GATES_OPEN.md](S_GATES_OPEN.md)).

**Pair-creation null result is not a drive-tuning limitation. It is an engine-structural limitation.** No amount of threshold_frac lowering, K_drift sweeping, or point-collision geometry can produce pair nucleation without the asymmetric-saturation + topology-injection mechanism (Phases 4 + 5). See §5, §6 for the axiom-native roadmap.

### 3.3 Two response regimes hypothesis (downgraded from r1)

r1 claimed "two distinct physics regimes, both AVE-native":
- v1 (fixed-f): peak at ω·τ=0.9 → "optimal detuning endurance"
- v2 (autoresonant, K_drift=0.5): monotonic increase with ω·τ → "cascade regime activates"

**r2 status: [CONJECTURE — not proven at distribution level].** The "two regimes" framing hinges on single-seed comparisons at λ∈{5,7,10} (§2.3 table †). Until a matched-seeds sweep is done for both v1 and v2, this is a hypothesis not a claim.

If the distribution-level shape change survives re-sweep, **the axiom-chain is [Ax4-DERIVED + AXIOM-ADJACENT]:** varactor-softening Duffing response is Ax4 ([doc 54_ §4](54_pair_production_axiom_derivation.md) + [Vol 4 Ch 1:127-142](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L127)); the PLL-feedback control loop is an engineering adjudication built ON TOP of Ax4 (not a new axiom).

### 3.4 Why centroids weren't detected — hypotheses

**H1 — measurement (threshold_frac)**: **[FALSIFIED by [doc 52_](52_h1_threshold_sweep.md)].** Lowering threshold_frac below 0.3 produces count explosion = thermal-noise granularity, not localized cores. 0.7 is the post-H1 empirical compromise.

**H2 — physics (symmetric saturation can't confine)**: **[Ax4-DERIVED, confirmed by doc 54_ §6].** Current single-S kernel has no mechanism for Γ = −1 impedance wall formation. Axiom-native flux-tube confinement requires μ/ε asymmetric split (Phase 4).

**H3 — geometry (plane-CW over-symmetrizes)**: **[CONJECTURE]** per [doc 53_ §2.1](53_pair_production_flux_tube_synthesis.md) + [VACUUM_ENGINE_MANUAL §11.4](VACUUM_ENGINE_MANUAL.md). Plane symmetry does not pick a preferred pair-nucleation site. A point-collision source (narrow-Gaussian) might break the degeneracy. Whether this is sufficient absent H2-resolution is unclear without Phase 4 first.

**H4 — amplitude (higher amp / higher K_drift)**: **[CONJECTURE]** — but both of these are empirical knobs, not axiom-derived controls. Upgrading the PLL to axiom-native varactor form (`ω₀·(1 − A²)^(1/4)` eliminating K_drift) is the prior move; see §6.3.

## 4. What Stage 4 + Phase III-B v2 delivers (r2)

Retaining r1's bullets with axiom-audit tags:

- **Dark-wake τ_zx diagnostic** — Pearson correlation with |V|² = 0.994 across 20 seeds. **[PORTED formula from [AVE-Propulsion/simulate_warp_metric_tensors.py:75-95](../../../AVE-Propulsion/src/scripts/simulate_warp_metric_tensors.py), Ax1-consistent K4-gradient implementation]**. K4-native first-principles derivation pending; see §6.6.
- **Working autoresonant drive** — Stable K_drift ∈ {0, 2.0}; frequency drift tracks A²_probe (Stage 4c validation). **[AXIOM-ADJACENT]** — varactor-softening is Ax4, PLL feedback is engineering. Linear-Taylor implementation (K_drift=0.5) **diverges from Ax4-native varactor form at A² > 0.3** per [VACUUM_ENGINE_MANUAL §17 A7](VACUUM_ENGINE_MANUAL.md); proposed axiom-native replacement in §6.3.
- **Two σ(ω) regimes mapped** — **[CONJECTURE — not proven at distribution level]**, retained as open hypothesis. Matched-seeds re-sweep across λ∈{3.5, 5, 7, 10} × 20 seeds × 2 drive types required for robust claim.
- **A²_cos ≈ 1 approached — axiom-correct framing per R4 subatomic convention, but distribution-level unreliable** — **[Ax4-DERIVED framing, A17 distribution regression]**. Under §0.1's subatomic override, r=1 IS the Ax4 Cosserat Regime IV entry / pair-production onset / Schwinger onset (collapsed at this scale per §0.2), so "first numerical approach of the Axiom-4 rupture boundary" was the right axiom framing. **But the r1 headline's single-seed 1.009 does not reproduce** (0/20 on current engine, median 0.87, best 0.9983). Superseded by §2.3 distribution: the autoresonant configuration reaches within 0.2% of r=1 in ~1/20 seeds; does not cross. Cause (code regression vs tail outcome) pending bisection.
- ⚠ **Pair creation demo: not achieved** — structural per [doc 54_ §6 + VACUUM_ENGINE_MANUAL §11.9], not tunable. Requires Phase 4 (asymmetric μ/ε saturation) + Phase 5 (PairNucleationGate). See §6.

## 5. Open questions (r2)

1. **After R4 engine patches land (plan file step 3):** re-run the 20-seed sweep on post-patch HEAD. Under R4, NodeResonanceObserver and BondObserver lose their `/α` conversions (reverting to the direct sum RegimeClassifier always used). Verify: `max_A2_cos` unchanged (Cosserat-only path, no `/α` ever applied); `max_A2_total` unchanged (RegimeClassifier was already correct); NodeResonanceObserver / BondObserver scalars should shift by the missing `/α` factor.
2. **Bisection 719f3ec vs 3a599ca** — isolates whether Phase 2 (`NodeResonanceObserver` JAX import chain) or Phase 3 (`_connect_all` `Phi_link` accumulation) caused the 0/20 non-reproduction of the 1.009 headline, or if it's pure seed-variance from single-seed r1.
3. **4λ × 20-seed × 2-drive sweep** — needed to robustly adjudicate "two σ(ω) regimes" distribution-level claim. Per 1 above, run after R3 accessors land so normalizations are explicit.
4. **Matched-energy metric** — P_phase6_autoresonant (headline Phase 6 prediction) requires "autoresonant vs fixed-f at matched energy." Current v1 vs v2 sweep matches (λ, amp, T) but not total injected energy (CW vs autoresonant consume power differently). Phase 6 design must fix this.
5. **τ_zx K4-native derivation** — see §6.6. Decide: derive in-house from Ax1 (new research doc), or keep [PORTED] with explicit annotation in VACUUM_ENGINE_MANUAL.

## 6. Axiom-first audit findings (new in r2)

**Flag-don't-fix discipline:** each item below surfaces a non-axiom-derivable engine or driver choice with a proposed axiom-native replacement. Grant adjudicates; I do not silently apply.

### 6.1 `amplitude = 0.5 · V_SNAP` — [EMPIRICAL, from v1 sweep]

**Where:** [driver:168,181](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py#L181).
**Status:** Chosen because v1 showed peak `max A²_cos` at this amplitude. Rationale is empirical curve-fitting, not axiom-derivable.
**Ax-consistent rationale (retrofittable):** In SNAP units, `amp = 0.5` gives `A²_K4_SNAP = 0.25` at source origin, placing the K4 sector in **Regime II** (`2α ≤ r² < 3/4`) per Vol 1 Ch 7:30-33. This is the large-signal regime where Ax4 corrections are non-trivial but not yet saturated — the natural sweep domain for observing saturation-driven Cosserat response. **Proposed reframing:** label as "Regime II K4 placement per Ax4," keeping the empirical value but grounding the choice in Vol 1 Ch 7's regime map.

### 6.2 `sigma_yz = 3.5` / `t_ramp_periods = 3.0` / `t_sustain_periods = 25.0` — [EMPIRICAL]

**Where:** [driver:65-66, 95, 102](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py#L65).
**Proposed axiom-native forms:**
- `sigma_yz ≥ 2·λ` for plane-wave approximation. **[Ax1-grounded]** — per Vol 1 Ch 1 K4 anisotropy, transverse profile narrower than 2λ breaks the plane-wave port-coupling assumption behind the T₂ projection at [vacuum_engine.py:125](../../src/ave/topological/vacuum_engine.py#L125). For λ=3.5, `sigma_yz ≥ 7.0`; current `3.5` violates this. **Flag for re-examination.**
- `t_ramp ≥ π/ω = half_period` for spectral-content purity. **[Ax1-grounded]** — K4 dispersion has support on `ω ∈ [0, c·√2 · 2π/ℓ_node]`; sharp transients leak spectrum. Current 3 periods is well above π/ω; safe.
- `t_sustain ≥ Q · period` where **[Ax4-DERIVED]** `Q = 1/S(r)` is the quality factor at working-point r. For K_drift=0.5 driving to `A²_K4 ≈ 0.25` (Regime II), `S ≈ √(0.75) = 0.87`, so `Q ≈ 1.15`. Current 25 periods is well above — safe. At deeper saturation (`A²_probe ≈ 0.5`), `Q ≈ 1.4` still < 25. Axiom-native justification retrofittable.

### 6.3 `K_drift = 0.5` — [EMPIRICAL Stage-4c tune] — axiom-native replacement available

**Where:** [vacuum_engine.py:723](../../src/ave/topological/vacuum_engine.py#L723), [driver:31,69,96,103](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py#L31).

**Current form:**
```python
shift_factor = max(1e-3, 1.0 - self.K_drift * A_sq_probe)  # linear Taylor
```

**Ax4-native form** ([doc 54_ §4](54_pair_production_axiom_derivation.md), [Vol 4 Ch 1:127-142](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L127), and already implemented in [`NodeResonanceObserver`](../../src/ave/topological/vacuum_engine.py#L546)):
```python
shift_factor = (1.0 - A_sq_probe) ** 0.25  # Ω_node / ω₀ per Ax4 varactor
```

**Derivation:** From Axiom 4 saturation `C_eff(V) = C_0/√(1 − (V/V_yield)²)`, the LC resonance `ω = 1/√(L·C_eff) = ω₀ · (1 − A²)^(1/4)`. This is the **exact** Axiom-4 varactor-softening frequency, with no free coefficient. **Regime of validity:** Regime II (`√(2α) ≤ r < √3/2`) — where the varactor form describes smooth saturation. At r=1 (Regime IV boundary) the LC description mode-converts per §0.2; the PLL operates below r=1 and drives toward it, never at it, so the form's boundary behavior is not invoked. (A PLL that actually reached r=1 would see ω → 0 and the feedback loop would freeze — which is physical behavior at the mode-conversion transition, not a pathology.)

**Linear-Taylor comparison:**
- Axiom-native at A² ≪ 1: `(1−A²)^(1/4) ≈ 1 − A²/4 − 3A⁴/32 − ...`, so leading term = `1 − A²/4`
- Engine current: `1 − 0.5·A²` — **twice the axiom-native leading coefficient**
- At A² = 0.3 (where NodeResonanceObserver driver shows divergence per [VACUUM_ENGINE_MANUAL §17 A7](VACUUM_ENGINE_MANUAL.md)): axiom-native → 0.915, engine-current → 0.85 (~7% low)
- At A² = 0.5: axiom-native → 0.841, engine-current → 0.75 (~11% low)

**Proposed replacement:** upgrade [`AutoresonantCWSource.apply`](../../src/ave/topological/vacuum_engine.py#L710) to use the Ax4-native varactor form directly. **Zero new parameters** (K_drift is eliminated). Backward-compat note: the manifest entry `P_phase6_autoresonant` and its "at matched energy" framing is unaffected (autoresonant nature is preserved; only the feedback law becomes axiom-native).

**[r2-ERROR-r3-CORRECTED] Normalization caveat retracted:** r2 flagged a concern that the SNAP-normalized probe (`A²_probe = V²/V_SNAP²`) would require `/α` conversion to match a yield convention, and that this would make the varactor shift-factor imaginary for any driven A² > α ≈ 0.0073. **This was an R3-framing artifact.** Under R4 subatomic override (§0.1), the engine's SNAP-normalized A² IS the canonical r² at VacuumEngine3D's operating scale. So the axiom-native shift law is simply `shift_factor = (1 − A²_probe_SNAP)^(1/4)` with no conversion; at A²_K4_SNAP = 0.393 this gives `0.885` — well-behaved, no imaginary issue. The PLL architecture is in the correct normalization; the only remaining question is replacing the linear Taylor with the full varactor form (§6.3 proposal above).

### 6.4 `n_outer_steps = 300` — [EMPIRICAL — "for PLL to track"]

**Where:** [driver:9, 67](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py#L9).
**Ax-consistent form:** `n_steps ≥ (t_ramp + t_sustain) / outer_dt`. With `outer_dt = 1/√2` (Ax1-derived from K4 anisotropy, [manual §4.3](VACUUM_ENGINE_MANUAL.md)), t_ramp=3·period, t_sustain=25·period, period=2π/ω: for λ=3.5, period=3.5, so `t_ramp+t_sustain = 98`, and `n_steps ≥ 98·√2 ≈ 139`. Current 300 is 2.2× this — safe margin. **Proposed:** make `n_steps` derived from `t_ramp + t_sustain + t_decay + safety_margin` rather than hardcoded.

### 6.5 `threshold_frac = 0.7` (TopologyObserver override) — [EMPIRICAL post-H1]

**Where:** [driver:107](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py#L107).
**Status:** Default `0.3` was [falsified by H1 in doc 52_](52_h1_threshold_sweep.md) — low thresholds produce thermal-noise granularity, not localized cores. `0.7` is the current empirical compromise.
**Proposed axiom-native replacement:** derive from SNR analysis of the centroid peak distribution vs thermal-init variance. A test of the form `threshold = mean(|ω|²) + k·σ(|ω|²)` with `k ≈ 3` would be a principled alternative. Not blocking; flag as G-item in FUTURE_WORK.

### 6.6 `τ_zx` formula — [PORTED from AVE-Propulsion, K4-native derivation pending]

**Where:** [DarkWakeObserver in vacuum_engine.py:647+](../../src/ave/topological/vacuum_engine.py#L647); formula from [AVE-Propulsion/simulate_warp_metric_tensors.py:75-95](../../../AVE-Propulsion/src/scripts/simulate_warp_metric_tensors.py).
**Form:** `τ_zx ∝ Z_local · ∂(V²/V_SNAP²) / ∂x` (using K4 tetrahedral gradient to respect bipartite sublattice).
**Status:** Ax1-consistent computation (tetrahedral gradient); Rule-6-compatible conceptually (impedance × field-gradient is natural TLM / impedance-matching language). But the exact functional form came from AVE-PONDER FDTD simulations and has not been derived in-house from Axiom 1 K4-TLM dynamics.
**Proposed axiom-native reconstruction:** would spawn a new research doc (56_ or later) tracing τ_zx from first principles using the K4 S-matrix + port-shift identities. Non-trivial (~2-3 days). **Flag-and-defer** per [doc 55_ §13] cross-repo references are noted but re-derivation is queued.

### 6.7 Driver verdict thresholds `max_A2_cos ≥ 0.5 AND n_centroids ≥ 2` — [HEURISTIC]

**Where:** [driver:131-137](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py#L131).
**Status:** Pre-registered outcome categories (v2-pair / v2-partial / v2-no-change) are fine as human adjudication labels. But the specific thresholds `A²_cos ≥ 0.5` (for "partial") and `n_centroids ≥ 2` (for "pair") have no axiom derivation — `0.5` is half-of-Regime-III, `2` is the minimum pair count.
**Proposed axiom-native replacement:** retire the thresholded verdict. Report `max_A2_cos` distribution and `n_centroids` distribution directly; let Grant adjudicate verdict based on distribution shape, not single-bin cutoffs.

### 6.8 `probe_x_offset = 4` — [HEURISTIC] — likely breaks at small λ

**Where:** [vacuum_engine.py:682, 701-708](../../src/ave/topological/vacuum_engine.py#L682).
**Status:** "Cells downstream of source for PLL feedback." No axiom derivation; picked by intuition.
**Proposed axiom-native form:** **[Ax1-grounded]** coherence length of the driven K4 mode = λ / (2π·√2) in natural units (the √2 is the K4 anisotropy factor from manual §4.3). For λ=3.5 → ~0.4 cells; for λ=10 → 1.1 cells. **Current `probe_x_offset=4` is well past coherence length at every λ in v2 sweep.** This calls into question whether the probe measures coherent source strain or a decorrelated downstream slice.
**Flag:** the PLL architecture may be reading the wrong quantity. Needs either axiom-native re-derivation of what to probe, or empirical validation that probe-at-offset-4 gives a meaningful A²_probe despite being past coherence length.

### 6.9 `_REGIME_II_BOUND_A2 = 0.75` (not a v2 driver choice, but observer-side) — [Ax1+4-DERIVED]

**Corpus-search result (Rule 8 before flagging):** per [Vol 1 Ch 7:47-51](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L47), the II/III boundary derives from:
- Quality factor `Q(r) = 1/S(r) = 1/√(1−r²)` (Ax4 saturation)
- Minimum radiating multipole `ℓ_min = 2` (Ax1 K4 topology)
- Yield regime begins at `Q = ℓ_min = 2` ⇒ `S = 1/2` ⇒ `r² = 3/4`

**This IS axiom-derived** ([Ax1+4-DERIVED]). The audit agent's initial flag of "no derivation chain found" was incorrect — rule 8 (corpus-search before flagging) resolved this to a full derivation. Preserved here as a positive audit example.

### 6.10 `[A14 — RegimeClassifierObserver line 376]` `A2 = A2_k4 + A2_cos` — [RESOLVED under R4 subatomic override]

**Where:** [vacuum_engine.py:376](../../src/ave/topological/vacuum_engine.py#L376).
**r2 position (retracted):** r2 flagged this as a "mixed-normalization bug" per doc 55_'s R3 reading — summing SNAP-normalized A²_K4 + yield-normalized A²_Cos.
**r3 position:** **Not a bug.** Under [Vol 4 Ch 1:711 subatomic override](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L711), V_yield ≡ V_SNAP at VacuumEngine3D's operating scale, so A²_K4 = V²/V_SNAP² IS canonical r²_K4 (not SNAP-outlier). Similarly A²_Cos uses TKI-derived ε_yield = 1 — canonical r²_cos at subatomic scale. **The sum is a valid Pythagorean r²_total** per AVE-APU Vol 1 Ch 5:26-37. Vol 1 Ch 7:12's universal form is satisfied.
**The actual R4 patch** (per plan file step 3): remove the `/α` lines from **[NodeResonanceObserver._capture:428-432](../../src/ave/topological/vacuum_engine.py#L428)** and **[BondObserver._compute_A2_yield:430-438](../../src/ave/topological/vacuum_engine.py#L430)**, which apply macro-scale conversion to subatomic-scale data. After R4, all three observers use the same direct sum that `RegimeClassifierObserver` has always computed.
**Impact on this doc:** `max_A2_total` values throughout §2.1 are **correct as-reported** under R4 subatomic convention. (The r2 ⚠ warnings on `max_A2_total` in the depends-on block and §0.3 were also retracted in r3 — they reflected the R3 misreading.)

## 7. Items flagged to Grant for adjudication (r2, updated in r3)

Per flag-don't-fix, these need your decision:

1. **§6.3 — K_drift PLL replacement.** Upgrade `AutoresonantCWSource.apply` to Ax4-native `(1 − A²)^(1/4)` (eliminates K_drift = free parameter)? Or keep linear-Taylor with K_drift = 1/4 (axiom-linearized) as a Stage-4c-preserving compromise? **[r2 "wrong normalization" concern retracted in r3]** — under R4 subatomic convention, the probe is already in canonical r² at A²_SNAP scale; no conversion needed, shift-factor stays real.
2. **§6.6 — τ_zx K4-native derivation.** Spawn new research doc (56_) to derive from Ax1, or keep [PORTED] with explicit annotation and defer to post-Stage-6? Non-trivial (~2-3 days) if derived in-house.
3. **§6.8 — `probe_x_offset = 4` past coherence length at all v2 λ.** Evidence the PLL may be reading decorrelated signal. Three sub-questions: (a) does the PLL actually work meaningfully under this configuration? (b) would an at-source probe (`offset=0`) give better results? (c) flag-only and defer to Phase 6 headline validation?
4. **§1.3 / §6.7 — verdict thresholds.** Retire `max_A2_cos ≥ 0.5 AND n_centroids ≥ 2` thresholded verdict, in favor of distribution-shape reporting? Would require re-running sweep with distribution aggregation.
5. **§2.3 table † — single-seed values at λ∈{5,7,10}.** Re-sweep these at 20 seeds each before any distribution-level claim? (Non-trivial compute: 3 λ × 20 seeds × 300 steps × 2 drive types ~ 1 hour.)
6. **§0.2 — "Schwinger" scale-dependence.** Under R4, AVE's pair-production onset (Vol 1 Ch 7:115) and QED Schwinger (Vol 1 Ch 7:130) collapse to r=1 at subatomic scale. At macroscopic scale they differ by 1/√α. This is physically sensible (two different systems) but terminology-wise "Schwinger" means two things in Vol 1 Ch 7 depending on scale. For future manuscript pass: reserve "Schwinger" strictly for QED V_SNAP event (macro scale use), give AVE's V_yield onset a distinct name (e.g., "AVE rupture-onset" or "varactor divergence")? Or accept the overload with a glossary note?

## 8. Known limitations (reminder, now with tags)

1. **threshold_frac = 0.7** — **[EMPIRICAL, §6.5]**. Below: thermal-noise count explosion. Above: misses sub-peak structure.
2. **K_drift = 0.5 single Stage-4c tune** — **[EMPIRICAL, §6.3]**. Ax4-native replacement available.
3. **`AutoresonantCWSource` is simplified PLL (strain-dependent frequency shift), not full PI-PLL with phase detection** — **[AXIOM-ADJACENT simplification]**. If axiom-native (1−A²)^(1/4) upgrade (§6.3) is insufficient, full PI-PLL is the next step.
4. **Thermal V initialization skipped (thermalize_V=False)** — **[Ax3-DERIVED choice]** per [47_ §2.2](47_thermal_lattice_noise.md). At T=0.1, thermalize_V would rupture the vacuum (exceeds AVE Schwinger temperature 3.44 MK).
5. **v2 uses N=40 (v1 was N=48).** **[EMPIRICAL]**. Results qualitatively consistent across sizes but not numerically identical.
6. **Single-seed values at λ∈{5,7,10}** — see §2.3 †. Distribution reports only available at λ=3.5 in current data.
7. **`max_A2_total` from RegimeClassifierObserver** — **[A14 RESOLVED under R4 subatomic override, §6.10]**. Under Vol 4 Ch 1:711 subatomic convention, A²_K4 and A²_cos are both canonical r²; the sum is valid Pythagorean r²_total. No fix to RegimeClassifierObserver needed; R4 patch removes `/α` from NodeResonance + BondObserver instead (see plan file step 3).
8. **τ_zx formula ported, not K4-native-derived** — **[PORTED, §6.6]**. Computation is Ax1-consistent; form is AVE-Propulsion-origin.

## 9. Artifacts

- [src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py) — sweep driver (audited in §6; configs [EMPIRICAL] with Ax-compatible rationales available)
- `/tmp/phase_iiib_v2_sweep.npz` — r1 single-seed raw numpy archive (8 configs)
- `/tmp/phase_iiib_v2_summary.png` — r1 4-panel summary
- `/tmp/phase_iiib_v2_log.txt` — r1 per-run log
- **[NEW r2]** `/tmp/v2_reproducibility_sweep.npz` — 20-seed sweep at λ=3.5, T=0.1 (the distribution replacing the 1.009 headline)
- **[NEW r2]** `/tmp/v2_reproducibility_sweep.png` — 20-seed sweep 4-panel plot
- [src/scripts/vol_1_foundations/v2_reproducibility_seed_sweep.py](../../src/scripts/vol_1_foundations/v2_reproducibility_seed_sweep.py) — 20-seed sweep script (currently untracked; commit alongside this r2 doc)
